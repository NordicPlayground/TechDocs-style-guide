# Releases and deployment

This document summarizes the manual process for creating a GitHub release and publishing the style guide to GitHub Pages.

## Prerequisites

- Install Git, Python, the GitHub CLI, MkDocs, Material for MkDocs, and the MkDocs Macros plugin.
- Authenticate the GitHub CLI with an account that can create releases and push to the repository.
- Check out `main` and confirm that the working tree is clean.

## Create a release

1. Synchronize the local `main` branch with GitHub:

   ```bash
   git switch main
   git pull --ff-only origin main
   ```

2. Move the changes for the release from the `Main Branch` section of `CHANGELOG.md` to a dated release section.

3. Validate the documentation:

   ```bash
   mkdocs build --strict
   ```

4. Commit and push the changelog and any other release changes:

   ```bash
   git add CHANGELOG.md
   git commit -m "Prepare release X.Y.Z"
   git push origin main
   ```

5. Create the GitHub release from the updated `main` branch:

   ```bash
   gh release create vX.Y.Z \
     --target main \
     --title "TechDocs Style Guide vX.Y.Z" \
     --generate-notes
   ```

6. Confirm that the release and tag point to the expected commit:

   ```bash
   gh release view vX.Y.Z
   ```

## Deploy to GitHub Pages

The site uses the root of the `gh-pages` branch as its GitHub Pages source.

1. Build and push the site to `gh-pages`:

   ```bash
   mkdocs gh-deploy \
     --force \
     --message "Deploy documentation for vX.Y.Z"
   ```

2. Check the GitHub Pages deployment:

   ```bash
   gh run list --workflow pages-build-deployment --limit 1
   ```

3. Open [the published Nordic TechDocs Style Guide](https://nordicplayground.github.io/techdocs-style-guide/) and verify the updated content.
