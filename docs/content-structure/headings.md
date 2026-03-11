# Headings

Headings provide structure and visual reference, aiding content scanning. Use them consistently across all content types. Treat headings as an outline: top-level for major subjects, second-level for distinct subtopics within larger sections. Ensure headings are specific and introduce new topics in an interesting way. Avoid consecutive headings without intervening text. Skip subheadings if you are unable to identify at least two distinct topics.

## Writing headings

Use the following recommendations when writing headings.

### Use headings judiciously

One heading level is usually plenty for a page or two of content. For long content, you might need to use additional heading levels.

### Keep headings short and simple

Put the most important idea at the beginning. Be as specific as you can, and be even more detailed with lower-level headings. For example, a second-level heading should be more specific than a first-level heading.

### Use task-appropriate phrasing and parallel form

Use phrasing that fits the content and keep the same grammatical form for all headings at the same level.

* **Task-related headings** – Prefer infinitive phrases (for example, *To create a configuration*) or imperative verb phrases. For procedures or steps, infinitive phrases are often clearest.
* **Non-task headings** – Use noun phrases (for example, *Headings*, *GPIO configuration*) or other forms that match the level.
* **Parallel form at the same level** – Use one consistent form for all headings at that level. If one heading at a level uses a gerund (for example, *Opening*, *Installing*, *Deploying*), use gerunds for the other headings at that level too. If you use noun phrases or infinitive phrases at a level, keep that form for siblings.
* **Don't force parallelism** – Don't choose a gerund (or any form) only to match other headings if it would misrepresent the content. For example, avoid *Understanding management operations* next to *Creating a managed object* if "understanding" wrongly implies the user must understand before doing; use *Management operations* instead so the heading stays accurate.

### Focus on what matters to customers

Focus on what matters to customers and choose words they'd use themselves. In most cases, don't talk about products, features, or commands in headings. Concentrate on what customers can achieve or what they need to know.

### Use parallel sentence structure

Use parallel sentence structure for all headings at the same level. Match the type of phrase across siblings—for example, all noun phrases, all infinitive phrases, or all gerunds at that level. Consistency makes the outline easier to scan and the hierarchy clearer. See [Use task-appropriate phrasing and parallel form](#use-task-appropriate-phrasing-and-parallel-form) for when to use which form and when not to force a form for parallelism.

### Repeat the heading subject in following text

Don't start the text after a heading with a pronoun. Repeat the main subject for clarity:

| Weak opening | Strong opening |
|--------------|----------------|
| **GPIO Configuration**</br>These allow flexible pin assignment. | **GPIO Configuration**</br>GPIO pins allow flexible pin assignment. |
| **DMA Transfers**</br>This method reduces CPU overhead. | **DMA Transfers**</br>DMA transfers reduce CPU overhead. |

Repetition reinforces the topic and helps readers who scan headings independently of body text.

### Provide context for technical elements

Include descriptive nouns when headings reference commands, files, or code elements:

| Lacks context | Has context |
|---------------|-------------|
| `nrfutil` | The `nrfutil` command |
| `config.json` | The `config.json` configuration file |
| `main.c` | The `main.c` source file |

Descriptive nouns clarify what type of element you're discussing.

### Avoid acronym definitions in headings

Use either the full term or the acronym in headings, not both:

| Cluttered | Clean |
|-----------|-------|
| Bluetooth Low Energy (BLE) Configuration | Bluetooth Low Energy configuration |
| Using the UART (Universal Asynchronous Receiver/Transmitter) | Using the UART |

Define the acronym in the body text immediately following the heading.

### Limit heading depth

Use a maximum of four heading levels. Deeper nesting indicates organizational problems:

* **Level 1**: Major chapter or topic divisions
* **Level 2**: Primary subtopics
* **Level 3**: Detailed subsections
* **Level 4**: Specific procedures or concepts

If you need a fifth level, restructure your content. Break the section into multiple topics or consolidate related information.

### Use at least two headings per level

Avoid single subheadings under a parent heading:

| Single subheading | Multiple subheadings |
|-------------------|---------------------|
| **Power Management**</br>   • Low-power modes | **Power Management**</br>   • Low-power modes</br>   • Active power optimization |

A single subheading often indicates the content could be integrated into the parent section or needs further subdivision.

### Don't repeat higher-level headings in subheadings

Don't repeat the exact text of a parent (higher-level) heading in its subheadings. Similarly, don't repeat the chapter or topic title in section headings. Subheadings should add specificity or a new angle, not echo the parent. Repeating the same words wastes space and makes the outline harder to scan.

### Include text before the first heading

Include some introductory text before the first first-level heading in a chapter or topic. Give readers a short lead-in so the first heading doesn't appear at the very top with no context.

### Avoid most punctuation

* **Period** - Don't end headings with a period.
* **Question mark or an exclamation point** - can be used if it's needed for meaning, but these should be extreme exceptions.
    * For example: *Not seeing what you want?* or *What can we help you find?*
* **Ampersands (&) or plus signs (+)** - avoid unless you're referring to UI that contains them or space is limited.
* **Hyphens** - in resized windows or mobile devices, they can result in awkward line breaks.
* Use *vs.,* not *v*. or *versus,* in headings.

## Formatting headings

### Use sentence-style capitalization for headings

That means that you capitalize the first word, any proper nouns, and the first word after a colon (if there is one). Everything else is lowercase.

**Examples:**

* Set up the deployment environment
* My account

### Break two-line headings carefully

Unless you're writing content for a responsive design (which breaks lines dynamically to fit the screen), break the heading in a way that makes sense and balances the length of the two lines. (Shift + Enter inserts a manual line break in many authoring tools.)

* Keep adjectives and prepositions with the words they modify.

* Keep hyphenated words and multiple-word proper nouns (such as *New York*) on the same line.

* Break after punctuation.

* Break naturally, at the end of a complete phrase, if possible.

* If you can't fit a headline on two lines, rewrite it.

### Use vertical spacing to make headings stand out

Headings typically have extra space above them and often less space below them. Close proximity between the heading and the text that follows it communicates to the reader that they're related. Heading spacing is built into heading styles in most templates. Use those styles to control spacing in a consistent way.

### Don't use extra line breaks

Don't use extra line breaks to increase heading spacing. In responsive web design, the layout and screen elements (including headings) adjust to the screen size automatically, whether they're viewed on mobile devices, tablets, laptops, or desktops. Extra line breaks might detract from the content appearance on mobile devices.
