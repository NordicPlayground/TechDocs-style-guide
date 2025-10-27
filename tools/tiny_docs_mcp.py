# tiny_docs_mcp.py
from __future__ import annotations
import sqlite3, pathlib, json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("TechDocsStyleGuideMCP")
DB = "docs_index.db"

# exclude only the *root* README.md
def _exclude_root_readme(root: pathlib.Path, p: pathlib.Path) -> bool:
    try:
        rel = p.resolve().relative_to(root.resolve()).as_posix()
    except Exception:
        return False
    return rel == "README.md"

# skip typical noise dirs
EXCLUDE_DIRS = {".git", ".hg", ".svn", ".venv", "venv", "node_modules", "dist", "build", "out", ".tox",
                ".mypy_cache", ".pytest_cache", "__pycache__"}

def _conn():
    c = sqlite3.connect(DB)
    c.execute("PRAGMA journal_mode=WAL;")
    c.execute("PRAGMA synchronous=NORMAL;")
    return c

def _reset_schema(cur):
    cur.execute("DROP TABLE IF EXISTS docs;")
    cur.execute("""
      CREATE VIRTUAL TABLE docs USING fts5(
        path UNINDEXED, title, content, tokenize='porter'
      );
    """)

def _walk(root: pathlib.Path):
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if any(part in EXCLUDE_DIRS for part in p.parts):
            continue
        if p.suffix.lower() not in {".md", ".rst"}:
            continue
        if _exclude_root_readme(root, p):
            continue
        yield p

def _rel(root: pathlib.Path, p: pathlib.Path) -> str:
    return p.resolve().relative_to(root.resolve()).as_posix()

@mcp.tool()
def reindex(root: str = ".") -> str:
    """
    Rebuild the index from scratch for all .md/.rst under 'root'.
    Excludes the *root* README.md and common build/VC dirs.
    """
    rootp = pathlib.Path(root).resolve()
    c = _conn(); cur = c.cursor()
    _reset_schema(cur)
    rows = []
    for p in _walk(rootp):
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        rows.append((_rel(rootp, p), p.stem, text))
    if rows:
        cur.executemany("INSERT INTO docs(path,title,content) VALUES(?,?,?)", rows)
    c.commit(); c.close()
    return f"Indexed {len(rows)} files from {rootp}"

@mcp.tool()
def search(query: str, k: int = 8) -> str:
    """
    Full-text search. Returns JSON: [{id,title,path,snippet,resource_uri}]
    """
    c = _conn(); c.row_factory = sqlite3.Row
    cur = c.cursor()
    cur.execute("""
      SELECT rowid, path, title,
             snippet(docs, 2, '[', ']', ' … ', 12) AS snippet
      FROM docs
      WHERE docs MATCH ?
      ORDER BY rank
      LIMIT ?
    """, (query, k))
    out = []
    for r in cur.fetchall():
        rid = int(r["rowid"])
        out.append({
            "id": rid,
            "title": r["title"],
            "path": r["path"],              # repo-relative path (e.g. docs/…)
            "snippet": r["snippet"],
            "resource_uri": f"doc://by-id/{rid}"
        })
    c.close()
    return json.dumps(out, ensure_ascii=False, indent=2)

@mcp.resource("doc://by-id/{rowid}")
def get_doc_by_id(rowid: int) -> str:
    """
    Fetch the full plain content for a search hit by numeric id.
    """
    c = _conn(); c.row_factory = sqlite3.Row
    cur = c.cursor()
    row = cur.execute("SELECT content FROM docs WHERE rowid=?", (rowid,)).fetchone()
    c.close()
    if not row:
        raise FileNotFoundError(f"No doc with id={rowid}")
    return row["content"]

if __name__ == "__main__":
    mcp.run(transport="stdio")
