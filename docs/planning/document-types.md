# Document types

Different types of documentation serve different purposes. Choose the right document type based on the reader's needs and the information you want to convey.

## Primary document types

### Getting started guide

A getting started guide walks a new user through the minimum steps needed to begin using a product or tool.

**Purpose:** Get the reader from zero to a working setup as quickly as possible.

**Characteristics:**

* Short and focused (ideally completable in under 30 minutes)
* Covers only the essentials — omits advanced options
* Targets new users with no prior experience
* Ends with a working result (a running application, a connected device)
* Links to more detailed documentation for next steps

**Example:** "Getting started with the nRF Connect SDK" — covers installation, first build, and first flash.

### Tutorial

A tutorial teaches a concept or skill through a guided, hands-on exercise. Unlike a getting started guide, a tutorial focuses on learning rather than setup.

**Purpose:** Teach the reader how to do something by guiding them through a concrete example.

**Characteristics:**

* Follows a learning path (builds knowledge incrementally)
* Includes explanations of *why*, not just *how*
* Produces a meaningful result that demonstrates the concept
* May take longer than a getting started guide
* Assumes the reader has completed initial setup

**Example:** "Building a BLE peripheral" — teaches BLE concepts while building a working application.

### How-to guide

A how-to guide provides step-by-step instructions for accomplishing a specific task. It assumes the reader already understands the relevant concepts.

**Purpose:** Help an experienced user accomplish a specific goal.

**Characteristics:**

* Focused on a single task or outcome
* Assumes relevant background knowledge
* Provides steps without lengthy explanations
* May cover edge cases and alternatives
* Includes troubleshooting for common problems

**Example:** "How to configure BLE advertising parameters" — assumes the reader understands BLE and wants to adjust specific settings.

### Conceptual guide

A conceptual guide explains how something works, why it was designed that way, or how components relate to each other.

**Purpose:** Help the reader understand a system, architecture, or concept.

**Characteristics:**

* Explains *what* and *why*, not *how*
* Uses diagrams, analogies, and examples
* Provides context for tasks documented elsewhere
* Doesn't include step-by-step procedures
* Links to related how-to guides and references

**Example:** "BLE advertising overview" — explains advertising modes, parameters, and trade-offs without prescribing configuration steps.

### Reference

A reference provides structured, factual information that readers look up as needed. It is organized for quick retrieval, not sequential reading.

**Purpose:** Provide detailed, authoritative information about specific items (functions, configuration options, error codes).

**Characteristics:**

* Organized alphabetically, categorically, or by structure
* Uses consistent formatting for each entry
* Comprehensive (covers every item in a set)
* Minimal prose — uses tables, lists, and structured entries
* Updated systematically when the product changes

**Example:** "Kconfig reference" — lists every configuration option with its type, default value, and description.

### Release notes

Release notes document what changed between product versions.

**Purpose:** Inform users about new features, changes, fixes, and known issues.

**Characteristics:**

* Organized by version (most recent first)
* Categorized by type (new features, changes, bug fixes, known issues)
* Concise entries (1-2 sentences per item)
* Links to detailed documentation for new features
* Includes migration guidance for breaking changes

#### nRF Connect SDK release notes

The nRF Connect SDK follows specific conventions for release notes. These guidelines apply to new release entries and to updates of existing release notes.

**Structure**

Divide release notes into sections by product area, library, or subsystem. Add links throughout both the release highlights and the changelog sections.

Include a "Documentation" section for substantial documentation edits that do not fall into the product-specific sections.

**Change categories**

Within each section, organize changes using these categories (include only the categories that apply):

* **Added** -- New features, new samples, new APIs
* **Updated** -- Changes to existing functionality
* **Fixed** -- Bug fixes and corrections
* **Deprecated** -- Features scheduled for removal
* **Removed** -- Features that have been removed

List individual changes as sub-bullet points under the relevant category. If a section has only a single change, a list structure is not required.

Each change should appear only once in the release notes. Do not duplicate entries across sections.

**Writing style for entries**

Start each entry with a simple, concise sentence. Omit the leading action verb from the clause.

**Preferred:**

* "Support for nRF54L15 in the BLE controller."
* "An issue with UART flow control on nRF52840 (NCSDK-12345)."

**Avoid:**

* "Added support for nRF54L15 in the BLE controller." (redundant -- the "Added" category already conveys the action)
* "Fixed an issue with UART flow control." (the "Fixed" category already conveys the action)

**Jira ticket references**

Include the Jira ticket number for each change. If the ticket number is not present in the pull request, ask the author to provide it.

**Sample and library changes**

Structure changes to samples and libraries with global changes first, then per-sample details:

*Global changes (apply to multiple samples):*

* All samples:
    * New samples X, Y, and Z.
    * A common issue with HTTP samples (NCSDK-12345).

*Per-sample changes:*

* Sample A:
    * Added:
        * New feature X.
        * New feature Y.
    * Updated:
        * Feature Z configuration.
    * An issue with initialization (NCSDK-12346).

* Sample B:
    * New feature X.
    * Feature Y configuration.

**Maintaining old release notes**

When updating previously published release notes:

*Kconfig option renames or removals:* When old Kconfig options are renamed or removed, update each occurrence in the release notes to prevent build errors. Remove the `:kconfig:` directive from old occurrences and wrap the option name in double backticks: `` `old_option_name` ``. Add the Kconfig update as a new entry in the current release notes.

*Grammar and style corrections:* Fix grammar errors and style issues in old release notes without changing the intended meaning of the original sentences (unless the information is factually incorrect).

*Build errors:* Fix any issue in old release notes that causes errors during documentation compilation.

### Migration guide

A migration guide helps users move from one version to another when there are breaking changes.

**Purpose:** Help existing users update their projects to work with a new version.

**Characteristics:**

* Lists all breaking changes with remediation steps
* Organized by subsystem or component
* Includes before/after code examples
* Covers both required and recommended changes
* Tested against real migration scenarios

## Choosing the right type

| Reader question | Document type |
| --------------- | ------------- |
| "I'm new, where do I start?" | Getting started guide |
| "How do I learn about BLE?" | Tutorial |
| "How do I change the advertising interval?" | How-to guide |
| "How does the BLE stack work?" | Conceptual guide |
| "What parameters does `bt_le_adv_start()` accept?" | Reference |
| "What changed in v2.5.0?" | Release notes |
| "How do I update from v2.4.0 to v2.5.0?" | Migration guide |

## Combining document types

Most documentation sets include all these types, organized into a cohesive structure. A common pattern:

1. **Getting started** section (getting started guides)
2. **Guides** section (tutorials and how-to guides)
3. **Concepts** section (conceptual guides)
4. **Reference** section (API references, Kconfig references)
5. **Release information** (release notes, migration guides)

Keep document types distinct. Don't mix step-by-step procedures into a conceptual guide, and don't add lengthy explanations to a reference page. When content crosses types, split it into separate topics and cross-reference.

## Content reuse across types

Some information appears in multiple document types. Use cross-references and content inclusion to maintain a single source of truth:

* Concept introductions in tutorials link to the full conceptual guide
* How-to guides link to the reference for detailed parameter descriptions
* Getting started guides link to tutorials for continued learning
* All types link to the glossary for term definitions

## Revision history

The revision history reflects the main reasons for a document update: new features, compatibility changes, new product versions, or corrections to incorrect information.

### Writing revision history entries

**Use a top-level approach.** Document macro-level changes only. Don't list every sentence that was rewritten or every typo that was fixed.

**Combine related changes.** If an update touches multiple sections for the same reason (for example, adding a new peripheral), describe it as one entry.

**Be concise.** Each entry should be one or two sentences.

**Don't list boilerplate changes.** Routine formatting updates, template changes, or standard text adjustments don't belong in the revision history.

**Use "Editorial changes" as a catch-all.** When a revision includes only minor text improvements, grammar fixes, or clarifications, add a single bullet:

* Editorial changes.

### Example revision history

| Version | Date | Description |
| ------- | ---- | ----------- |
| 1.2.0 | 2026-01-15 | Added nRF54L15 support. Updated GPIO configuration for nRF54L Series. |
| 1.1.0 | 2025-10-01 | Added power profiling chapter. Updated BLE advertising examples for SDK v2.5.0. |
| 1.0.1 | 2025-08-15 | Corrected pin assignments in Table 3. Editorial changes. |
| 1.0.0 | 2025-06-01 | Initial release. |

## Document versioning

Use a consistent versioning scheme to communicate the significance of document changes.

### General documents

| Increment | Format | When to use | Example |
| --------- | ------ | ----------- | ------- |
| **Major** | 1.x | Hardware or IC modifications that change the documented product | 1.0 to 2.0 |
| **Minor** | x.1 | Additional features, compatibility updates, new tools or software | 1.0 to 1.1 |
| **Revision** | x.x.1 | Critical documentation errors only (use sparingly) | 1.1 to 1.1.1 |

### Software documentation

| Increment | Format | When to use | Example |
| --------- | ------ | ----------- | ------- |
| **Major** | 1.x | API or behavior changes; application code may need modification | 1.0 to 2.0 |
| **Minor** | x.1 | New features or API additions; application code may need modification | 2.0 to 2.1 |
| **Revision** | x.x.1 | Bug fixes and performance improvements; no application code changes needed | 2.1 to 2.1.1 |
| **Build** | x.x.x-a | New build of a non-production version | 2.1.1-beta1 |

### Versioning guidelines

* Increment only the level that matches the most significant change. Reset lower levels to zero when incrementing a higher level (1.2.3 becomes 2.0.0 for a major change).
* Use revision increments sparingly. Reserve them for corrections to critical errors in published documentation.
* Align documentation versions with product versions when practical. This helps readers match the documentation to their installed software or hardware revision.
