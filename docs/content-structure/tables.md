# Tables

Tables make complex information easier to understand by presenting it in a clear structure. Don't use a table
just to present a list of items that are similar. Use a list instead.

|             Tables are sometimes useful for       |                           Example                              |
| ------------------------------------------------- | -------------------------------------------------------------- |
| Data or values                                    | Text formats and their associated HTML codes                   |
| Simple instructions                               | User interface actions and their associated keyboard shortcuts |
| Categories of things with examples                | SKUs and the products they include                             |
| Collections of things with two or more attributes | Event dates with times and locations                           |

## Content

Make sure the purpose of the table is clear with a table title or brief introduction if necessary.

Place information that identifies the contents of a row in the leftmost column of the table.

* For example, in a table that describes commands, put the command names in the left column.

Make entries in a table parallel.

* For example, make all the items within a column a noun or a phrase that starts with a verb.

* Use *Not applicable* or *None.* instead of leaving a cell blank .

| Function                | Description                                                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------ |
| AddUsersToEncryptedFile | Adds user keys to the specified encrypted file                                                                     |
| Cancello                | Cancels all pending input and output (I/O) operations that are issued by the calling thread for the specified file |
| CancelloEx              | Marks any outstanding I/O operations for the specified file handle                                                 |
| GetTempFileName         | Creates a name for a temporary file                                                                                |

## Header rows

Distinguish the text in the header row by making the font larger, bolder, or a different color.

Don’t organize a table so that the column heading forms a complete sentence when combined with the cell contents.

In long tables, make sure the header row is always visible. For example, on the web, use a fixed header row that stays in place during scrolling. Or, in a downloadable document, occasionally repeat the header row.

## Capitalization

Use sentence-style capitalization for the table title and each column heading.

Use sentence-style capitalization for the text in cells unless there’s a reason not to (for example, keywords that must be lowercase).

## Punctuation

If there’s text that introduces the table, it should be a complete sentence and end with a period, not a colon.

Don’t use ellipses at the end of column headings.

For the text in cells, use periods or other end punctuation only if the cells contain complete sentences or a mixture of fragments and sentences.

## Table placement

Place tables appropriately in the flow of your documentation to maintain readability and logical structure.

### Don't insert tables mid-sentence

Complete your sentence before introducing a table. Don't split a sentence across a table.

**Avoid:**

The nRF52840 supports the following peripherals

| Peripheral | Count |
| ---------- | ----- |
| UART       | 2     |
| SPI        | 3     |

which can be configured using the device tree.

**Use:**

The nRF52840 supports multiple peripherals.
The following table lists the available peripherals:

| Peripheral | Count |
| ---------- | ----- |
| UART       | 2     |
| SPI        | 3     |

Configure these peripherals using the device tree.

### Table numbering for formal documents

For formal documentation or specifications that require references to tables, use numbered tables with descriptive captions.

**Format:** Table X: [Descriptive caption]

**Example:**

**Table 1: nRF9160 power consumption in different modes**

| Mode       | Current Draw |
| ---------- | ------------ |
| Active LTE | 13 mA        |
| PSM        | 2.7 µA       |
| System OFF | 400 nA       |

Reference numbered tables consistently in your text:

* "See Table 1 for power consumption details"
* "Table 2 shows the GPIO configuration options"
* "As shown in Table 3, the nRF52840 supports multiple radio protocols"

Use table numbering only when:

* You need to reference tables from multiple locations in the document
* The document follows a formal specification or standards format
* The document contains many tables that readers need to navigate

For most web-based documentation, descriptive headings work better than numbered tables.
