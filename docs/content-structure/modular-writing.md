# Modular writing

Modular writing structures documentation as self-contained, reusable units of information called topics. Each topic addresses a single subject and can stand alone or be assembled with other topics into larger documents.

## What is a topic?

A topic is a unit of information that:

* Addresses a single subject or answers a single question
* Has a clear title that identifies its content
* Makes sense when read independently
* Can be reused in multiple contexts without modification
* Has a consistent internal structure

## Topic types

Most technical documentation content falls into three primary topic types.

### Concept topics

Concept topics explain what something is, why it matters, or how it works at a high level. They provide background knowledge readers need before performing tasks.

**Structure:**

1. Title (noun phrase or "About [topic]")
2. Definition or overview
3. Explanation with supporting details
4. Diagrams or illustrations (if helpful)
5. Cross-references to related tasks or reference material

**Example title:** "Bluetooth Low Energy advertising"

**Example content:**

"BLE advertising is the process by which a device broadcasts data packets to announce its presence and capabilities. Nearby devices can discover the advertising device by scanning for these packets.

Advertising operates on three dedicated channels (37, 38, and 39) to minimize interference with data channels."

### Task topics

Task topics describe how to accomplish a specific goal. They contain step-by-step procedures.

**Structure:**

1. Title (verb phrase: "Configure..." or "How to configure...")
2. Brief introduction (what the task accomplishes and when to do it)
3. Prerequisites (if any)
4. Procedure (numbered steps)
5. Result or verification (what the user should see after completing the task)
6. Cross-references to related tasks

**Example title:** "Configure BLE advertising parameters"

### Reference topics

Reference topics provide detailed, factual information that readers look up rather than read sequentially. They are typically organized in tables, lists, or structured entries.

**Structure:**

1. Title (noun phrase)
2. Brief introduction
3. Reference content (tables, lists, or structured entries)
4. Cross-references to related concepts or tasks

**Example titles:** "Kconfig options reference," "Error codes," "API function reference"

## Benefits of modular writing

### Reuse

Write a topic once and use it in multiple deliverables. A single "Installing the nRF Connect SDK" topic can appear in every getting-started guide without duplication.

**Example:** A prerequisites section included in multiple tutorials:

```markdown
{!includes/prerequisites-ncs.md!}
```

### Consistency

When information exists in one place, updates propagate to all locations where the topic is used. No more conflicting versions of the same procedure.

### Easier maintenance

Small, focused topics are easier to review, update, and test than long monolithic documents. When an API changes, update one reference topic instead of searching through multiple guides.

### Flexible assembly

Assemble topics into different collections for different audiences or products. The same set of BLE topics can appear in guides for nRF52840 and nRF5340, with device-specific topics swapped in as needed.

### Translation efficiency

Translators work on individual topics. When a topic changes, only that topic needs retranslation, not the entire document.

## Writing effective topics

### Make topics self-contained

Each topic should provide enough context to be understood on its own. Don't assume readers have read other topics first.

**Include:**

* A clear, descriptive title
* Brief context or introduction
* All information needed to understand the topic or complete the task
* Cross-references for related information (but not required to understand the current topic)

**Avoid:**

* "As described in the previous section..."
* Pronouns that reference other topics ("it," "this" without clear antecedent)
* Steps that depend on information only found in another topic without linking to it

### Keep topics focused

If a topic covers more than one subject, split it. A common sign that a topic needs splitting:

* The title requires "and" (e.g., "Installation and Configuration" → two topics)
* The topic has more than 4-5 major sections
* Different audiences need different parts of the topic
* The topic exceeds 1000-1500 words

### Use consistent structure

Apply the same structure to similar topic types throughout your documentation. Readers learn the pattern and can find information faster.

**All task topics should follow the same pattern:**

1. Introduction → 2. Prerequisites → 3. Steps → 4. Result

**All reference topics should follow the same pattern:**

1. Introduction → 2. Reference table or list → 3. Related topics

### Write meaningful titles

Topic titles serve as the primary navigation mechanism. Make them specific, descriptive, and consistent.

**Concept topic titles** use noun phrases:

* "BLE advertising modes"
* "Thread network topology"
* "Power management states"

**Task topic titles** use verb phrases:

* "Configure BLE advertising"
* "Flash firmware using nrfjprog"
* "Debug with the nRF Connect for VS Code extension"

**Reference topic titles** identify the content type:

* "GPIO API reference"
* "Kconfig options"
* "Error codes"

## Assembling topics into documents

### Define a logical sequence

Arrange topics in an order that makes sense for the reader's journey:

1. Concept topics that provide background
2. Task topics that guide the reader through the work
3. Reference topics that provide lookup information

### Create navigation and context

Use a table of contents, index, or landing page to tie topics together. Provide cross-references between related topics so readers can navigate between them.

### Use conditional content sparingly

When topics need minor variations for different contexts (different devices, different operating systems), use conditional content or variables rather than creating duplicate topics.

**Example:**

"Flash the firmware to the {device_name}:" where `{device_name}` is replaced by the target device in the build.

Reserve full topic variants for cases where the content differs substantially.

## Transitioning to modular writing

If your documentation is currently written as long, monolithic documents:

1. **Identify natural topic boundaries.** Look for heading breaks, subject changes, and audience shifts.
2. **Extract the most-reused content first.** Prerequisites, setup procedures, and common tasks benefit most from modularization.
3. **Establish topic templates.** Create templates for each topic type to ensure consistency.
4. **Convert incrementally.** Don't try to modularize everything at once. Start with new content and convert existing content as it comes up for revision.
