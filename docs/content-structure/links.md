# Links

Links are the primary navigation mechanism in online documentation. Well-crafted links help readers find related information, navigate complex topics, and accomplish tasks efficiently. Poorly constructed links frustrate readers and damage the credibility of your documentation.

## Where to place links

Place links where readers expect to find them and where they provide the most value.

### Tables of contents

Use links in tables of contents to give readers an overview of the document and allow direct navigation to sections.

### Summaries and introductions

Place links in topic summaries or introductory paragraphs to direct readers to detailed information.

**Example:**

"The nRF Connect SDK provides tools for developing Bluetooth Low Energy applications. For setup instructions, see [Installing the nRF Connect SDK](#). For a list of supported boards, see [Supported boards](#)."

### Lists

Use links within lists to organize related resources.

**Example:**

"Before you begin, review the following:

* [Hardware requirements](#)
* [Software prerequisites](#)
* [Supported operating systems](#)"

### Cross-references in body text

Use links in body text when referencing related concepts that readers may need to understand.

**Example:**

"Configure the [device tree](#) to enable the UART peripheral."

### Code examples

Link from code examples to the relevant API documentation.

**Example:**

"The following code initializes BLE advertising. For details on advertising parameters, see the [Bluetooth advertising API reference](#)."

### Glossary terms

Link specialized terms to their glossary definitions on first use.

## General linking strategies

### Avoid overlinking

Too many links overwhelm readers, fragment their attention, and make text harder to read.

**Guidelines:**

* Don't link to the same destination more than once per topic or page
* Don't link common terms that readers already understand
* Limit inline links to 2-3 per paragraph
* Don't link every mention of a product name or technical term

**Avoid:**

"Use the [nRF Connect SDK](#) to build [applications](#) for [nRF52840](#) [devices](#). The [nRF Connect SDK](#) supports [Bluetooth Low Energy](#), [Thread](#), and [Zigbee](#)."

**Use:**

"Use the [nRF Connect SDK](#) to build applications for nRF52840 devices. The SDK supports Bluetooth Low Energy, Thread, and Zigbee."

### Minimize clicks

Reduce the number of clicks readers need to reach essential information.

* Link directly to the relevant section, not just the parent page
* Use anchor links to specific headings when helpful
* Provide the most important information on the current page

### Prevent reader disorientation

Help readers maintain context when following links.

**Reserve link formatting for links only.** Don't apply link-like formatting (blue, underlined text) to non-linked content.

**Warn about unexpected destinations.** Let readers know when a link leads to:

* External websites
* File downloads
* Content in a different language
* Content that requires authentication

**Example:**

"For the full specification, see the [Bluetooth Core Specification](https://www.bluetooth.com/specifications/) (external site, PDF download)."

**Ensure return navigation.** Readers should always be able to find their way back to where they started.

### Include links that answer reader questions

Anticipate what readers might ask after reading your content, and provide links to those answers.

**Common reader questions:**

* "What does this term mean?" → Link to glossary
* "How do I do this?" → Link to relevant procedure
* "Where can I learn more?" → Link to detailed reference
* "What are the prerequisites?" → Link to setup guide

### Use links to condense content

Instead of repeating information, link to the authoritative source. This keeps topics short and ensures information stays up to date.

**Avoid:**

Repeating the full setup procedure in every tutorial.

**Use:**

"Before you begin, complete the [initial setup](#)."

### Provide links in lists when possible

When listing multiple related items, use a list with links rather than inline links in a paragraph.

**Less scannable:**

"You can use the Programmer app, the nrfjprog command-line tool, or the nRF Connect for VS Code extension to flash firmware."

**More scannable:**

"Flash firmware using one of these tools:

* [Programmer app](#)
* [nrfjprog command-line tool](#)
* [nRF Connect for VS Code](#)"

### Place links at the end of topics

Group related links at the end of a topic under a "Related topics" or "Next steps" heading. This keeps body text readable and provides a clear path forward.

**Example:**

```
## Next steps

* [Configure BLE advertising](#)
* [Set up scanning](#)
* [Establish a connection](#)
```

### Test link validity

Verify that all links work correctly before publishing. Broken links erode trust and frustrate readers.

* Include link checking in your build process
* Verify external links periodically (they change without notice)
* Use relative links for internal references when possible
* Monitor link health after documentation updates

## Crafting link text

### Provide context in link text

Link text should tell readers where the link leads without requiring them to read surrounding text. Screen reader users often navigate by links, hearing link text out of context.

**Avoid:**

* "Click [here](#) for setup instructions"
* "See [this page](#) for details"
* "More information [available](#)"

**Use:**

* "[Set up the nRF Connect SDK](#)"
* "[Configuration reference](#)"
* "[BLE advertising API reference](#)"

### Weave link text into sentence structure

Links should fit naturally into the sentence. The sentence should be grammatically correct with or without the link.

**Avoid:**

"To learn about BLE, [click here](#)."

**Use:**

"Learn about [BLE advertising parameters](#) before configuring your device."

### Choose key words or phrases for link text

Select words that describe the destination content. Use nouns and noun phrases rather than verbs or generic terms.

**Effective link text:**

* "[GPIO configuration guide](#)"
* "[nRF52840 DK hardware layout](#)"
* "[Power management API](#)"

**Weak link text:**

* "[Read more](#)"
* "[See details](#)"
* "[Learn more](#)"

### Choose appropriate length for link text

Link text should be 1-5 words. Avoid extremely short links (single characters) and overly long links (entire sentences).

**Too short:**

"For details, see [n](#)RF52840 specifications."

**Too long:**

"[Read about all the features and specifications of the nRF52840 SoC including GPIO, UART, SPI, and I2C peripherals](#)."

**Right length:**

"See the [nRF52840 specifications](#) for peripheral details."

### Write scannable link text

Use distinctive, descriptive text for each link on a page. Avoid using the same link text for different destinations.

**Avoid:**

* "[Learn more](#)" ... "[Learn more](#)" ... "[Learn more](#)"

**Use:**

* "[BLE documentation](#)" ... "[Thread documentation](#)" ... "[Zigbee documentation](#)"

### Match link text to destination titles

Link text should closely match the title or heading of the destination page. This helps readers confirm they've arrived at the right location.

**Destination page title:** "Configuring BLE Advertising Parameters"

**Good link text:** "Configure [BLE advertising parameters](#)"

**Confusing link text:** "Set up your [wireless configuration](#)"

### Don't use quotation marks around link text

Link formatting (color, underline) is sufficient to distinguish links from surrounding text.

**Avoid:**

See "[nRF Connect SDK documentation](#)" for details.

**Use:**

See the [nRF Connect SDK documentation](#) for details.

### Avoid "click here"

"Click here" is device-specific (assumes a mouse), provides no context, and is meaningless to screen reader users navigating by links.

**Avoid:**

* "Click here to download the SDK"
* "Click here for more information"
* "Click here to see the API reference"

**Use:**

* "[Download the nRF Connect SDK](#)"
* "See the [installation guide](#) for details"
* "[BLE API reference](#)"
