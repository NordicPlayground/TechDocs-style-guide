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
