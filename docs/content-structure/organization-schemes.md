# Organization schemes

How you organize documentation determines whether readers can find what they need. Choose an organizational scheme that matches how your audience thinks about the content.

## Common organizational schemes

### Alphabetical

Organize content in alphabetical order when readers know the exact name of what they are looking for.

**Best for:**

* API references
* Glossaries
* Configuration option lists
* Error code references

**Example:**

A Kconfig reference listing all configuration options alphabetically:

* `CONFIG_BT` - Enable Bluetooth subsystem
* `CONFIG_BT_CENTRAL` - Enable BLE central role
* `CONFIG_BT_PERIPHERAL` - Enable BLE peripheral role
* `CONFIG_GPIO` - Enable GPIO driver

**Limitation:** Alphabetical order assumes readers know the correct term. It fails when readers search by concept rather than name.

### Task-based

Organize content around what readers need to accomplish. Group related tasks together and order them by workflow.

**Best for:**

* Getting started guides
* Tutorials
* How-to documentation
* Development workflows

**Example:**

* Setting up the development environment
* Creating your first application
* Building and flashing
* Debugging your application
* Optimizing power consumption

**Advantage:** Task-based organization directly matches the reader's goal. It answers "How do I...?" questions.

### Conceptual (topic-based)

Organize content by subject area. Group related concepts together regardless of task sequence.

**Best for:**

* Reference documentation
* Architecture overviews
* Protocol descriptions
* Feature documentation

**Example (nRF Connect SDK documentation):**

* Bluetooth Low Energy
    * Advertising
    * Scanning
    * Connections
    * Security
* Thread
    * Network formation
    * Routing
    * Border router
* Matter
    * Device types
    * Commissioning

### Chronological

Organize content by time sequence or the order in which events occur.

**Best for:**

* Release notes
* Changelogs
* Migration guides
* Boot sequence documentation

**Example:**

* v2.5.0 (2026-01-15) - Added nRF54 Series support
* v2.4.0 (2025-10-01) - Thread 1.3 certification
* v2.3.0 (2025-06-15) - Matter 1.2 support

### By complexity

Organize content from simple to complex, building on previously introduced concepts.

**Best for:**

* Learning paths
* Multi-part tutorials
* Progressive skill building

**Example:**

1. Beginner: Blink an LED
2. Intermediate: BLE beacon application
3. Advanced: BLE mesh network with OTA updates

### By audience

Organize content by the reader's role or experience level when different audiences need different information about the same product.

**Best for:**

* Products with diverse user groups
* Documentation that spans hardware and software
* Content serving both beginners and experts

**Example:**

* For hardware engineers: Schematic design, PCB layout, antenna matching
* For firmware developers: SDK setup, API reference, debugging
* For product designers: Certification, power profiling, range testing

## Choosing the right scheme

Match the organizational scheme to the content type and reader need:

| Reader question | Best scheme | Example |
| --------------- | ----------- | ------- |
| "How do I...?" | Task-based | Getting started guide |
| "What is...?" | Conceptual | Architecture overview |
| "Where is the X option?" | Alphabetical | API reference |
| "What changed?" | Chronological | Release notes |
| "I'm a beginner" | By complexity | Tutorial series |
| "I'm a hardware engineer" | By audience | Role-specific guides |

Most documentation sets combine multiple schemes. Use task-based organization for guides, alphabetical for references, and conceptual grouping for the overall structure.

## Combining schemes effectively

### Primary and secondary organization

Choose a primary scheme for your top-level structure and secondary schemes within sections.

**Example:**

* **Primary (conceptual):** Bluetooth Low Energy, Thread, Zigbee
* **Secondary (task-based):** Within BLE: Getting started, Configuration, Troubleshooting
* **Tertiary (alphabetical):** Within Configuration: API reference sorted alphabetically

### Navigation support

Regardless of primary organization, provide multiple navigation paths:

* **Table of contents** follows the primary scheme
* **Search** lets readers find content regardless of organization
* **Cross-references** connect related topics across schemes
* **Index** (for comprehensive documentation) provides alphabetical access

## Maintaining consistent organization

### Apply schemes consistently

Once you choose a scheme for a section, apply it consistently. Don't mix alphabetical and task-based ordering within the same list or navigation level.

### Review organization periodically

As documentation grows, the original organizational scheme may become strained. Review the structure when:

* Readers frequently report difficulty finding information
* New content doesn't fit the existing structure
* The table of contents exceeds 3-4 levels of nesting
* Related topics are scattered across different sections

### Document your scheme

Record the organizational rationale for your documentation set so that future contributors maintain consistency. Include:

* The primary organizational scheme and why it was chosen
* Rules for where new content should be placed
* Naming conventions for sections and pages
