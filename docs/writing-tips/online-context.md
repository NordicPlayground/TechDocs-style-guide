# Online context

Online documentation exists in a different context from print. Readers arrive from search engines, bookmarks, and cross-references. They may land on any page without having read the preceding content. Write each topic to work independently while maintaining coherence within the larger documentation set.

## Every page is page one

In online documentation, any page can be the reader's entry point. Don't assume readers have followed a sequential path through your content.

### Provide context on every page

Each page should answer three questions within the first few lines:

1. **What is this about?** A clear title and introductory sentence.
2. **Who is this for?** State or imply the audience.
3. **What do I need to know first?** Prerequisites or links to background.

**Example:**

"# Configure BLE advertising

Set the advertising interval, TX power, and payload for your BLE peripheral application.

**Prerequisites:** Complete [Getting started with BLE](#) before configuring advertising parameters."

### Avoid assuming prior reading

Don't use phrases that assume the reader has been following along:

**Avoid:**

* "As we discussed earlier..."
* "Continuing from the previous section..."
* "Now that you have completed the setup..."
* "Remember the configuration file from Chapter 2..."

**Use:**

* "As described in [BLE overview](#)..."
* "After completing [Initial setup](#)..."
* Link to the specific prerequisite topic

### Provide enough context to orient readers

Even when a page focuses on a narrow topic, include enough context for readers to understand where it fits.

**Example introduction:**

"The nRF Connect SDK uses Kconfig to manage build-time configuration options. This page describes BLE-specific Kconfig options. For general Kconfig usage, see [Kconfig overview](#)."

## Information orientation

Online readers typically have one of four information needs. Understanding these helps you structure content effectively.

### Goal-oriented (task)

The reader wants to accomplish something specific.

**They ask:** "How do I...?"

**Provide:** Step-by-step procedures with clear outcomes.

### Problem-oriented (troubleshooting)

The reader has encountered an issue and needs to resolve it.

**They ask:** "Why does...?" or "How do I fix...?"

**Provide:** Symptoms, causes, and solutions. Use exact error messages for searchability.

### Learning-oriented (concept)

The reader wants to understand how something works.

**They ask:** "What is...?" or "How does...work?"

**Provide:** Explanations, diagrams, and examples with links to related procedures.

### Reference-oriented (lookup)

The reader needs a specific fact or parameter.

**They ask:** "What is the default value of...?" or "What are the parameters for...?"

**Provide:** Tables, lists, and structured reference content.

## Maintaining coherence

While each page should work independently, the documentation set should feel cohesive.

### Use consistent terminology

Use the same term for the same concept everywhere. Don't call it "development kit" on one page and "DK" on another and "eval board" on a third without establishing these as synonyms.

### Use consistent structure

Apply the same patterns to similar content. If one BLE configuration page uses "Overview → Configuration → Example → Reference," all BLE configuration pages should follow the same structure.

### Cross-reference generously

Connect related topics with cross-references. This compensates for the non-linear reading path by creating multiple routes between related information.

**At the beginning (prerequisites):**

"This guide assumes familiarity with [BLE concepts](#)."

**In the body (related concepts):**

"The [device tree](#) defines the hardware configuration."

**At the end (next steps):**

"## Next steps

* [Test BLE connections](#)
* [Optimize power consumption](#)"

### Provide navigation landmarks

Help readers understand where they are in the documentation:

* Use breadcrumbs
* Include section overviews (landing pages) for major topic areas
* Maintain a clear and consistent table of contents
* Use "Related topics" sections

## Writing for different entry points

### From search engines

Readers arriving from search often look for a specific answer. Make sure:

* Page titles contain the key terms readers search for
* The first paragraph summarizes what the page covers
* Error messages and common queries appear in the text

### From cross-references

Readers following a link from another page have some context but may not know the details. Make sure:

* The page title matches or closely resembles the link text
* The introduction provides enough context without the referring page

### From table of contents

Readers browsing the table of contents scan titles for relevance. Make sure:

* Titles are specific and descriptive
* The hierarchy is logical and consistent
* Related topics are grouped together

## Context preservation techniques

### Repeat key terms

In online writing, it's acceptable to repeat the subject noun rather than using a pronoun when the antecedent might be unclear across sections.

**Print style (pronouns):**

"The nRF52840 supports BLE 5.3. It can advertise on coded PHY."

**Online style (clear antecedent):**

"The nRF52840 supports BLE 5.3. The nRF52840 can advertise on coded PHY."

Use judgment: repeat the noun when a reader scanning individual paragraphs might lose context, but don't repeat excessively within a paragraph.

### Summarize before detailing

Start sections with a brief summary of what follows. This helps readers who scan decide whether to read the full section.

### Use descriptive headings

Headings should communicate the content of their sections without requiring readers to have read the preceding section. See [Scannable writing](scannable-writing.md) for heading guidelines.
