# Capitalization

Use sentence-style capitalization for most titles and headings. This means capitalizing only the first word and using lowercase for the rest, except for proper nouns like brands, products, and services.

## Sentence-style capitalization guidelines

* Capitalize the first word of any sentence, heading, title, UI label (such as a button or checkbox name), or standalone phrase.
* Always capitalize proper nouns. For more on proper nouns, see [Nouns and pronouns](grammar/nouns-pronouns.md).
* Use lowercase for all other words.
* Always capitalize the first word of a new sentence. Avoid starting sentences with words that are always lowercase.
* Capitalize the first letter of technical abbreviations, acronyms, and units of measurement after spelling them out at least once. For example, write "Central Processing Unit (CPU)" initially, then use "CPU" afterward.
* Once an acronym is defined, use only the acronym throughout the rest of the document.
  * Example: CPU.
* Avoid using plural forms of abbreviations and acronyms unless strictly necessary.

## Identifying proper nouns

When uncertain whether to capitalize a term, determine if it represents a specific named entity or a general category:

* A general category remains lowercase and typically includes words like "a," "an," "the," "some," or "any" before it.
  * Example: "Connect the device to a debugger" (any debugger from the category).
* A specific named product or entity uses capitalization and typically appears without preceding articles.
  * Example: "Launch nRF Connect for Desktop" (the specific application).

Apply this test when documenting software tools, hardware components, or development environments.

### Exceptions

| Situation | Examples |
|-----------|----------|
| Proper nouns, including brand, product, and service names, are always capitalized. If a title or heading includes a colon, capitalize the first word after it only if it is a proper noun. | The nRF Connect SDK helps developers create solutions efficiently. |
| Titles of blog posts, documentation articles, and press releases use sentence-style capitalization. | Develop with nRF Connect: Best practices for IoT projects |
| Figure captions and table captions should use sentence-style capitalization, ensuring consistency between captions and references in the text. | |
| Capitalize the first word after a colon if it introduces a complete sentence. | The following should be considered: Avoid unnecessary repetition. |
| Capitalize the first word after closing quotation marks if it begins a new sentence. | "Save your work frequently," the instructor said. |

## Lists, figures, and tables

* Use sentence-style capitalization for bullet points, numbered items in lists, and table headers.
* Maintain consistency between figure/table captions and references in the text.
* For continuation bullet points, avoid ending punctuation unless necessary for clarity.
* Use sentence-style capitalization for the terms "figure" and "table" when referring to specific items.
  * Example: See figure 3 for details.
* Use sentence-style capitalization for headers in appendices, indexes, and glossaries.
  * Example: "appendix A: hardware reference" or "glossary of terms."

## Structural document references

When referring to numbered or lettered document elements, capitalize the descriptor term:

* Capitalize organizational terms followed by identifiers.
  * Example: "Chapter 4 covers Bluetooth protocols."
  * Example: "Review the details in Section 2.3."
  * Example: "Appendix B contains troubleshooting steps."
  * Example: "Table 7 shows power consumption data."
  * Example: "Example 3 demonstrates pin configuration."
* When multiple steps are referenced together, keep the plural form lowercase.
  * Example: "Follow steps 2 through 6 to complete initialization."
* Use lowercase when no specific identifier follows.
  * Example: "The next section explains memory allocation."
  * Example: "Refer to the table below for specifications."

## Page number formatting

When directing readers to specific pages in printed or PDF documentation, keep the word "page" lowercase:

* Use lowercase for page number references.
  * Example: "Additional diagrams appear on page 87."
  * Example: "See page 12 for installation prerequisites."

## Illustration labels and callouts

For text annotations within diagrams, figures, and illustrations:

* Capitalize only the first word and any proper nouns in callout text.
  * Example: A diagram showing "Antenna connection" and "nRF9160 SiP."
* Keep technical abbreviations capitalized according to their standard form.
  * Example: Labels reading "UART interface" and "GPIO pins."
* Maintain consistency with how these terms appear in body text.

## Headings with symbols or special characters

* Retain symbols, special characters, and mathematical notation in headings. Apply sentence-style capitalization to all other words.
* When a heading includes symbols, special characters, or mathematical notation, retain the original formatting.
  * Example: "Understanding the @ sign" or "5G network overview."

## Technical terms and abbreviations

* Spell out technical terms (such as acronyms and abbreviations) at first occurrence, followed by the abbreviation in parentheses.
  * Example: Secure Partition Manager (SPM).
* Avoid plural forms of abbreviations and acronyms unless strictly necessary.
* When using an acronym in possessive form, add `'s` directly.
  * Example: The nRF5340's performance.
* Capitalize acronyms like "GHz" and "MHz" in numerical contexts, and do the same for units of measurement when used with numbers.
  * Example: "256 kB of RAM."
* Avoid using command names or technical terms in capitalized form unless required. For example, keep `nrfutil` as is without capitalization.
* Use lowercase for file names, directory paths, or command options unless explicitly required.
  * Example: `~/Documents/myfile.txt` should keep its original case.
* Follow language conventions for code snippets or commands in running text.
  * Example: "To create a directory, use the `mkdir` command."
* When a brand name is part of a hyphenated compound, only capitalize the brand name unless the second word is a proper noun.
  * Example: Nordic-certified technician.
* Maintain the original capitalization for brand names, such as CamelCase or internal capitalization, even when used within a sentence or heading.
  * Example: "nRF Connect SDK should retain CamelCase."

## Input device controls

Capitalize names of physical keys, buttons, and hardware controls:

* Treat individual key names as proper nouns.
  * Example: "Press the Return key to confirm."
  * Example: "Hold the Shift key while clicking."
* Capitalize combined keystrokes using the plus sign or hyphen.
  * Example: "Use Alt+Tab to switch windows."
  * Example: "Enter Ctrl-C to terminate the process."
* Apply the same principle to hardware buttons and switches on development boards.
  * Example: "Press the Reset button on the nRF52840 DK."
  * Example: "Toggle the Power switch to enable the circuit."

## Technical notation

Follow these capitalization rules for specialized technical notation:

* Keep "x" lowercase in hexadecimal addresses and memory values.
  * Example: "The register address is 0x4000."
  * Example: "Write 0xFF to clear the buffer."
* Maintain lowercase "x" in architecture designations.
  * Example: "Compatible with x86 and x64 architectures."
* Use lowercase "x" when expressing physical dimensions.
  * Example: "The PCB measures 40x30 millimeters."
* Keep "p" lowercase in pin designations that use this convention.
  * Example: "Connect to p0.13 for GPIO control."

## Variables and placeholders

Maintain lowercase formatting for placeholders and variables that users replace with actual values:

* Keep placeholder text lowercase unless it contains terms normally capitalized.
  * Example: "Enter your <username> in the login field."
  * Example: "Replace <device_id> with your actual device identifier."
  * Example: "Specify the <BoardName> parameter" (when "Name" requires capitalization).
* Apply this rule to command syntax, configuration examples, and API documentation.
  * Example: "Run `nrfutil device list --serial <serial_number>`."

## Physical component labels

Capitalize labels on physical hardware components when documenting their operation:

* Treat physical labels and markings as proper nouns.
  * Example: "Locate the LED labeled Status on the development kit."
  * Example: "Connect the cable to the Debug port."
  * Example: "The Mode switch controls operating states."
* Match the exact capitalization shown on the physical device when possible.

## Cross-references and UI labels

* Use sentence-style capitalization consistently for cross-references and UI labels.
  * Example: Refer to "mechanics of writing" and click the "save as draft" button.

## Commands and software elements in headings

* Keep commands or software elements in headings in their original case. Avoid modifying them for stylistic reasons.
  * Example: "Using the `nrfutil` command" instead of "Using the NrfUtil Command".

## Capitalization in parentheses

* If a parenthetical statement forms a complete sentence, capitalize the first word and place the punctuation inside the closing parenthesis.
  * Example: (This is a complete sentence.)
* If the parenthetical statement is not a complete sentence, do not capitalize the first word.
  * Example: (for example, using abbreviations).

## Quotation marks within a sentence

* If a complete sentence is quoted within a sentence, retain its original capitalization. If quoting a partial phrase, follow the sentence's capitalization.
  * Example: She said, "Be careful when proceeding," and continued her work.
  * Example: He described it as a "groundbreaking discovery" in his presentation.
* If a partial quoted phrase begins a new sentence, use sentence-style capitalization.
  * Example: "nRF52840 module performance" was the topic of discussion.

## References to specific versions or editions

* Use sentence-style capitalization for specific versions or editions, only capitalizing proper nouns.
  * Example: "version 2.0," "edition 2023," or "nRF Connect SDK version 1.9.0."

## Multilingual content capitalization

* When including non-English words or phrases, retain their original capitalization rules as per their language conventions.
  * Example: In Norwegian, "Trådløs teknologi" retains its noun capitalization, while in French, "intelligence artificielle" remains lowercase.

## Hyphenated words and compound adjectives in headings

* Use sentence-style capitalization for hyphenated compounds in headings and body text, capitalizing only proper nouns.
  * Example: Power-On/Off switch, self-correcting errors.
* Use lowercase for compound adjectives in body text unless they include a proper noun.
  * Example: "Client-server architecture."
* Avoid ambiguous capitalization involving gerunds and participles.
  * Example: Use "user-defined variables" rather than "User-Defined Variables" unless in a title context.

## Avoid unnecessary capitalization

Avoid the following forms of unnecessary capitalization:

* Do not use all uppercase for emphasis.
* Do not use all lowercase as a stylistic choice.
* Do not use internal capitalization (for example, *AutoScale* or *e-Book*) unless it is part of a brand name.
* Do not capitalize the spelled-out form of an acronym unless it is a proper noun.

### Emphasis methods

Never use capitalization solely to emphasize words or create visual impact:

* Use italic formatting for emphasis instead of capitals.
  * Correct: "The firmware *must* be updated before proceeding."
  * Incorrect: "The firmware MUST be updated before proceeding."
* Reserve all-caps only for established acronyms and constants.
  * Example: "The API returns an HTTP status code."
  * Example: "Define MAX_BUFFER_SIZE in your configuration."

### Exceptions

| Situation | Examples |
|-----------|----------|
| When words are joined by a slash, capitalize the word after the slash if the word before the slash is capitalized. | Country/region <br /> Turn on the On/off toggle. |

For more information on capitalization in hyphenated compound words, see [Hyphens](punctuation/dashes-and-hyphens.md).