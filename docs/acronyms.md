# Acronyms and abbreviations

**What is an acronym?**
An acronym is an abbreviation formed from the initial letters of other words and pronounced as a word (for example, Secure Domain Firmware is abbreviated as "SDFW"). Use acronyms carefully to maintain clarity for your readers.

Acronyms and abbreviations can affect clarity, tone, and SEO. Some are widely recognized, while others are known only to niche audiences. Always consider whether using an acronym enhances clarity for your target audience.

In machine-translated content, avoid using acronyms that are also common English words, like *RAM*, as they may be translated incorrectly without context.

## First use rule

Write every product name, feature name, and technical term in full on its first use on each page, with the acronym in parentheses. After the first use, the acronym alone is acceptable.

**Pattern:** Full Name (ACRONYM) on first use, then ACRONYM for subsequent uses.

**Example:**

"The nRF Connect SDK provides Secure Domain Firmware (SDFW) to ensure secure boot and maintain firmware integrity in IoT devices. Developers can use SDFW to enhance the security of Nordic Semiconductor products."

This rule applies per page. If a reader lands on any page, they must find the full term defined before the acronym is used.

**Exceptions:** Some acronyms are so universally recognized that they do not require spelling out: *USB, FAQ, URL, LED, RAM, CPU, API*. However, always consider your audience and context.

## Do not create unofficial acronyms

Do not invent new acronyms for Nordic products or features. Use only officially established abbreviations.

**Example:**

* Do not abbreviate "nRF Connect SDK" as "NCS" or "NCSDK"
* Do not abbreviate "Secure Partition Manager" as "SPM"
* Do not abbreviate "Nordic Secure Partition Manager" as "NSPM"

See [Product names](product-names.md) for the authoritative list of accepted product name forms.

## Only use widely recognized acronyms

Use acronyms only if they are widely recognized by your audience. Refer to the [Glossary](glossary.md) for commonly accepted acronyms. If an acronym is listed in *[The American Heritage Dictionary](https://ahdictionary.com/)*, it can be used without further explanation. Always check official internal documentation before using an acronym.

## Avoid introducing acronyms used only once

If an acronym appears only once in your content, spell out the term instead. Introducing an acronym for a single use adds unnecessary complexity and may confuse readers.

**Exception**: For SEO purposes, you may use both the spelled-out term and the acronym together, but do this sparingly to avoid clutter. Avoid "alphabet soup" by minimizing back-to-back acronyms in a sentence.

## Avoid using acronyms in headings

Avoid using an acronym in a heading unless absolutely necessary for SEO. Instead, spell out the term in full. Acronyms in headings can reduce readability, especially for non-technical audiences.

If a heading contains an acronym, the first use rule still applies: provide the full term with the acronym in parentheses in the first sentence of the body text below the heading.

## Capitalize or lowercase the spelled-out term appropriately

Lowercase all words in the spelled-out form of an acronym, except for proper nouns. Capitalize the names of protocols, specifications, and official terms, as they are considered proper nouns.

**Examples:**

* Peripheral Resource System (PRS)
* Bluetooth® Low Energy (BLE)

## Use *a* or *an* based on pronunciation

Always base the choice of *a* or *an* on the pronunciation of the acronym. If the acronym begins with a vowel sound, use *an*. If it begins with a consonant sound, use *a*.

**Examples:**

* an nRF52840 SoC
* a BLE connection
* an SDFW feature
* an LTE-M network

For acronyms like *SQL*, use *an* if pronouncing it as 'ess-cue-el', but use *a* if pronounced as 'sequel'. Avoid using acronyms that create awkward phrasing when paired with *a* or *an*. If clarity suffers, consider spelling out the term.

## Pluralize acronyms correctly

To make an acronym plural, add a lowercase *s*. Do not use an apostrophe to form the plural.

**Examples:**

* three Software Development Kit (SDK) releases → then: "the SDKs include..."
* multiple Development Kits (DKs)

| Correct | Incorrect |
| ------- | --------- |
| SDKs | SDK's |
| DKs | DK's |
| GPIOs | GPIO's |

If the acronym stands for a term that is already plural, do not add an *s*. Ensure readers can clearly distinguish between single and plural references.

## Avoid possessive forms of acronyms

Avoid possessive forms of acronyms to improve clarity. Rephrase sentences to avoid ambiguity.

**Examples:**

* Instead of "the CPU’s efficiency," write "the efficiency of the CPU."
* Instead of "the BLE’s specifications," write "the specifications of the BLE."
* the nRF Connect SDK updates
* the purpose of the SDFW documentation
* the developer's guide

## Special cases for acronyms

In internal documentation or communication, acronyms that are well-known within the organization but not externally should still be spelled out for clarity if the content is intended for a wider audience.

## Acronyms in graphics and tables

When using acronyms in figure captions or tables, spell out the term in a note or include a legend if it may not be widely recognized.

**Example:**
In a table header: "nRF52840 Development Kit (DK)" should be spelled out in a note or included in a legend for clarity.

## Exceptions to avoiding acronyms

In technical specifications or space-constrained elements like tables or diagrams, acronyms may be used more freely, but their definitions should be provided elsewhere in the document to ensure reader understanding.

## Direct expression over abbreviated Latin

Technical writing prioritizes immediate comprehension. Replace inherited Latin shortcuts with clear English equivalents:

| Traditional shortcut | Direct expression | Context |
| --- | --- | --- |
| e.g. | for example | Introducing sample cases |
| i.e. | specifically | Narrowing to exact meaning |
| etc. | among others, and more | Indicating incomplete lists |
| viz. | namely | Introducing precise identification |

Benefits of direct expression:
* Global readers process familiar English faster than Latin conventions
* Automated translation systems handle plain language more reliably
* Screen readers pronounce English words naturally versus stumbling over abbreviations

## Per-page definitions for non-linear reading

Readers navigate technical documentation non-linearly. Any page can be the reader's entry point, so the first use rule applies independently on each page.

* **Each page** must define every acronym on first use, regardless of whether another page already defines it.
* **Multi-section documents**: Treat major sections as independent starting points if they have separate URLs or anchors.
* **Tutorials vs reference**: Tutorials following a strict sequence may relax this within a single tutorial flow, but reference material must define terms independently on every page.

**Example:**

* Page 1 introduces "Bluetooth Low Energy (BLE)" and uses BLE throughout
* Page 2, read independently, also introduces "Bluetooth Low Energy (BLE)" at first mention
* A reader jumping directly to Page 2 encounters no undefined acronyms

Within a single page, do not redefine the same acronym multiple times. Define it once at first use, then use the acronym for the rest of the page.

## Preventing word-form confusion

Some abbreviations create recognizable words that carry unintended meanings. Apply punctuation to prevent misreading:

* Add periods when the abbreviation spells a different word.
  * "no." prevents reading "number" as the word "no"
  * "fig." clarifies "figure" versus "fig" the fruit
* Technical initialisms rarely need punctuation—they don't form words.
  * SPI, I2C, UART, PWM remain unpunctuated
* Geographic abbreviations traditionally include periods in American English.
  * "U.S." for United States

Test: If readers might momentarily parse your abbreviation as a different word, add periods for distinction.

## Density versus clarity optimization

Space-constrained elements permit different abbreviation density than flowing text:

**Condensed contexts** (tables, diagrams, UI labels):
* Abbreviate liberally to fit constrained layouts
* Example: Column headers use "Temp (°C)" instead of "Temperature (degrees Celsius)"
* Provide definitions in table notes, legends, or nearby body text

**Standard contexts** (paragraphs, procedures, explanations):
* Spell out uncommon terms
* Use established acronyms after definition
* Prioritize reading flow over space efficiency

**Decision framework**: If removing a single abbreviation breaks your layout, you're in condensed context. If it merely makes the layout longer, you're in standard context.

## Terms to avoid

Avoid creating unnecessary acronyms or using non-standard abbreviations that reduce clarity.

### Avoid these common mistakes:

| **Don't Use** | **Use Instead** | **Reason** |
| ------------- | --------------- | ---------- |
| FW | firmware | Too informal, spell out |
| HW | hardware | Too informal, spell out |
| SW | software | Too informal, spell out |
| DB | database | Can be confused with decibel (dB) |
| repo | repository | Too informal for documentation |
| docs | documentation | Too informal for documentation |
| config | configuration | Too informal for documentation |

### Nordic-specific guidance:

* **Product names**: Do not create unofficial acronyms for Nordic products (see [Product names](product-names.md))
  - Write "nRF Connect SDK" not "NCS" or "NCSDK"
  - Write "nRF52840 Development Kit (DK)" on first use, then "DK" is acceptable

* **Tool names**: Use established abbreviations only, after spelling out on first use
  - "Development Kit (DK)" → then "DK"
  - "Software Development Kit (SDK)" → then "SDK"
  - "Real-Time Operating System (RTOS)" → then "RTOS"

* **Technical terms**: Follow industry standards, but still spell out on first use per page
  - "General Purpose Input/Output (GPIO)" → then "GPIO"
  - "Universal Asynchronous Receiver/Transmitter (UART)" → then "UART"
  - "Serial Peripheral Interface (SPI)" → then "SPI"

## Commonly confused terms

Be careful with terms that look similar or sound alike.

### Common confusions:

**It's vs. Its**

* **It's** = It is (contraction)
* **Its** = possessive form
* *Example*: "It's important to check its status"

**Affect vs. Effect**

* **Affect** = verb meaning to influence
* **Effect** = noun meaning result
* *Example*: "This setting affects the output" vs. "The effect is noticeable"

**That vs. Which**

* **That** = restrictive clause (no comma)
* **Which** = non-restrictive clause (with comma)
* *Example*: "The device that supports BLE" vs. "The nRF52840, which supports BLE, ..."

**Ensure vs. Insure vs. Assure**

* **Ensure** = make certain
* **Insure** = provide insurance
* **Assure** = tell someone confidently
* *Example*: "Ensure the device is powered"

### Nordic-specific term clarifications:

**Device vs. Board vs. DK**

* **Device**: The IC/SoC itself (nRF52840)
* **Board**: Specific Zephyr-related term
* **DK**: Specifically Nordic Development Kit boards

**Peripheral vs. Interface**

* **Peripheral**: Hardware module within SoC (UART peripheral)
* **Interface**: Connection method or API (serial interface)

**Mode vs. State**

* **Mode**: User-configurable setting (Sleep mode)
* **State**: System-determined condition (Connected state)
