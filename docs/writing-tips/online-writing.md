# Online writing

Writing for online consumption differs fundamentally from writing for print. Online readers scan, skip, and navigate non-linearly. Structure and present your content to accommodate these behaviors.

## How online reading differs from print

**Non-linear reading.** Online readers rarely start at the beginning and read through to the end. They arrive at any page from search results, bookmarks, or cross-references.

**Scan first, read second.** Readers scan headings, bold text, and the first words of paragraphs to decide whether to read more closely.

**Shorter attention spans.** Screen reading is slower and more tiring than print reading. Readers spend less time on each page and are quicker to leave.

**Multiple devices.** Content must work on desktop monitors, tablets, and phones with varying screen sizes.

## Writing for search

Online readers often find documentation through search engines. Structure your content to be search-friendly.

### Use keywords naturally

Include the terms readers are likely to search for, but weave them into natural sentences.

**Example:**

"Configure BLE advertising parameters to control how the nRF52840 broadcasts its presence to nearby devices." (Naturally includes "BLE advertising parameters" and "nRF52840" as likely search terms.)

### Write descriptive page titles

Page titles appear in search results and browser tabs. Make them specific and descriptive.

**Avoid:**

* "Configuration"
* "Getting Started"
* "Reference"

**Use:**

* "BLE advertising configuration"
* "Getting started with the nRF Connect SDK"
* "GPIO API reference"

### Write informative introductions

The first paragraph of each page often appears as the search result snippet. Make it a clear summary of the page content.

**Example:**

"The nRF Connect SDK build system uses CMake and west to compile applications for Nordic devices. This guide explains how to configure build options, select build targets, and troubleshoot common build errors."

## Structuring content for online reading

### Make every page self-contained

Each page should make sense on its own. Don't assume readers have read the previous page.

**Include on every page:**

* A clear title describing the content
* A brief introduction or summary
* Prerequisites or links to prerequisite topics
* The core content
* Cross-references to related information

### Keep pages focused

Each page should address a single topic or task. If a page covers multiple topics, split it into separate pages or use clear section headings.

**Guideline:** If a page requires more than 3-4 scrolls (approximately 1500-2000 words), consider splitting it.

### Use progressive disclosure

Present information in layers: summary first, then details. Let readers choose their depth.

**Layer 1 (summary):** "The nRF52840 supports three low-power modes."

**Layer 2 (overview):** A table comparing the three modes with key characteristics.

**Layer 3 (detail):** Dedicated sections for each mode with configuration instructions.

### Provide navigation aids

Help readers orient themselves within your documentation:

* Use breadcrumbs to show location in the hierarchy
* Include a table of contents for long pages
* Add "Related topics" or "Next steps" sections
* Use consistent heading structures across similar pages

## Writing web-friendly text

### Front-load information

Place the most important information at the beginning of the page, paragraph, and sentence.

**Print style (builds to conclusion):**

"Given the power constraints of battery-operated IoT devices, the importance of efficient protocol selection, and the range requirements of typical deployments, BLE is the recommended protocol for the nRF52840."

**Online style (leads with conclusion):**

"Use BLE as the primary protocol for battery-operated nRF52840 deployments. BLE provides the best balance of power efficiency, range, and data rate for IoT applications."

### Use meaningful link text

Readers scan for links. Make link text descriptive enough to understand out of context. See [Links](../content-structure/links.md) for detailed guidance.

### Write scannable content

Use structural elements to break up text:

* **Headings** every 2-4 paragraphs
* **Bulleted lists** for 3+ related items
* **Numbered lists** for sequential steps
* **Tables** for comparative data
* **Code blocks** for commands and configurations
* **Admonitions** for warnings and notes

See [Scannable writing](scannable-writing.md) for more techniques.

### Keep sentences short

Aim for an average sentence length of 15-20 words. Vary sentence length for rhythm, but avoid sentences longer than 25 words.

## Online-specific formatting

### White space

Online content needs more white space than print. White space improves readability on screen and reduces visual fatigue.

* Leave space between sections
* Use short paragraphs (3-7 lines)
* Don't pack too much content into a single view
* Use line spacing appropriate for screen reading

### Font and text considerations

When choosing formatting:

* Use adequate font sizes (16px minimum for body text)
* Maintain sufficient contrast between text and background
* Avoid long lines of text (60-80 characters per line is optimal)
* Don't rely solely on color to convey meaning (consider color-blind readers)

### Avoid print-specific references

Don't use language that assumes a print format.

**Avoid:**

* "On the next page..."
* "Turn to Chapter 5"
* "See the facing page"
* "This manual contains..."

**Use:**

* "In the next section..."
* "See [Chapter 5: Configuration](#)"
* "See [Power management](#)"
* "This documentation covers..."

## Testing your content

Verify that your online content works well for readers:

* Read it on a mobile device
* Test all links
* Check that headings create a logical outline
* Verify that each page makes sense without context from other pages
* Confirm that search terms appear naturally in the text
