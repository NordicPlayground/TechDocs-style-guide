# Nouns and pronouns

## Capitalization and proper nouns

Proper nouns are one of a kind—unique people, places, and things. Capitalize proper nouns wherever they occur.

Proper nouns include:

* Names and titles of individuals.
* Unique, named places, organizations, events, shows, corporate and philanthropic programs, and other things.
* Product, service, app, and tool names.
* Trademarks.
* Titles of books, songs, and other published works.
* Managed standards, such as Bluetooth.

If there's more than one of a thing, it's a common noun. For example, there are lots of chief operating officers, so "chief operating officer" is a common noun. There's only one "Latasha Sharp, Chief Operating Officer", so that's a proper noun.

Don't capitalize common nouns unless they begin a sentence or the situation
calls for title-style capitalization. Most technology concepts, product categories, devices, and features are common nouns, not proper nouns. Examples of common nouns include "cloud computing, smartphone, e-commerce," and "open source".

### Capitalizing technology terms

Capitalize technology terms as proper nouns only when:

* You need to distinguish a component or product, such as SQL Server, from a general technology with a similar name, such as an SQL database server.

* The terms are typically capitalized in the industry. Search *[The American Heritage Dictionary](https://ahdictionary.com/),* reputable internet sites, and industry-specific dictionaries. Don't rely on unedited websites.

If you're not sure whether a term is a proper noun (and thus capitalized) or a common noun (lowercase), check *[The American Heritage Dictionary](https://ahdictionary.com/)* and the [Glossary](../glossary.md). Default to lowercase unless there's a compelling reason to capitalize the term.

For guidelines for sentence-style and title-style capitalization, see [Capitalization](../capitalization.md).

## Plural nouns

To check the spelling of plural forms of words derived from Latin and Greek that retain their Latin or Greek endings (typically *-a, -us, -um, -on, -ix,* or -*ex*), see specific entries in the [Glossary](../glossary.md) and *[The American Heritage Dictionary](https://ahdictionary.com/).*

| **Noun** | **Plural form** | **Examples** |
| -------- | --------------- | ------------ |
| Common and proper nouns ending in "s" | If the noun ends in "s", add "es". | the Johnsons <br /> the Joneses <br /> biases |
| Singular abbreviation | Add an "s", even if the abbreviation ends in *s.* | ISVs <br /> DBMSs |
| Plural abbreviation | If an abbreviation already represents a plural, don't add an "s".| MFC (Microsoft Foundation Classes) |
| Single letter | Add an apostrophe and an "s". <br /> The letter itself (but not the apostrophe or the ending "s") is italic. | *x*'s |
| Number | Add an "s" | the 1950s|
| Variable | Don't add ("s") to a word to indicate that it could be either singular or plural unless you have no other choice. Use the plural form instead. | Wait for x minutes. |

## Pronouns and gender

Don't use gendered pronouns in generic references. Instead, rewrite—for example, use the second person ("you"). Or refer to a person's role ("customer", "employee", or "client").

### Pronouns and collective nouns

Collective nouns like "company" take a singular pronoun. Don't use a plural pronoun like "they" for a collective noun. If the emphasis is on the individuals in a group, it's OK to use a plural pronoun with a singular noun.

Examples:

* Meet with up to 250 people.
* All they need is a phone or internet connection.
* The company upgraded its cloud storage solution to Microsoft Azure.

## Pronoun reference distance

Pronouns create links between sentences. The further apart a pronoun sits from what it represents, the harder readers work to maintain understanding.

### Test your pronoun links

Apply this test when editing: Can you identify what a pronoun represents within three seconds? If you hesitate, your readers will too.

Problem indicators:
* Multiple nouns appear between the pronoun and its reference
* The pronoun starts a new paragraph or section
* Two or more items could logically fit as the pronoun's reference
* The sentence remains unclear even after rereading the previous sentence

### Strengthen weak pronoun links

**Technique 1: Repeat the specific term**

Replace the pronoun with the exact technical term, even if repetition seems awkward:

* Weak link: "Configure the UART baud rate before enabling DMA transfers. It must match the peripheral clock frequency."
* Strong: "Configure the UART baud rate before enabling DMA transfers. The baud rate must match the peripheral clock frequency."

**Technique 2: Add identifying context**

Keep the pronoun but add qualifying words that narrow the reference:

* Weak link: "The application allocates memory for packet buffers and protocol headers. These consume approximately 4 KB."
* Strong: "The application allocates memory for packet buffers and protocol headers. These allocations consume approximately 4 KB."

**Technique 3: Restructure for proximity**

Move the pronoun closer to what it represents, or combine sentences:

* Separated: "Power consumption increases when multiple radio protocols operate simultaneously. The nRF5340 manages this through dynamic switching. It reduces current draw during idle periods."
* Proximate: "The nRF5340 manages power consumption when multiple radio protocols operate simultaneously. The SoC reduces current draw during idle periods through dynamic switching."

### Paragraph and section boundaries

Pronouns rarely work well across these boundaries. Reintroduce the specific term:

* Across boundary: "The I2C controller supports clock stretching for slow peripherals.\n\n**Configuration steps**\n\nIt requires specific register settings."
* Reintroduced: "The I2C controller supports clock stretching for slow peripherals.\n\n**Configuration steps**\n\nThe I2C controller requires specific register settings."

### Demonstrative pronouns in technical contexts

Words like "this," "that," "these," and "those" work as pointers but need clear targets in technical writing:

* Pointer without target: "Enable interrupt handling and configure priority levels. This improves response time."
  - Question: What improves response time? Enabling? Configuring? Both?
* Pointer with target: "Enable interrupt handling and configure priority levels. This configuration improves response time."

Common additions that clarify demonstrative pronouns:
* this → this setting, this approach, this configuration
* that → that value, that register, that specification
* these → these parameters, these functions, these requirements
* those → those addresses, those peripherals, those constraints

### Ownership pronouns in hardware descriptions

Possessive pronouns (its, their) become ambiguous when describing interconnected hardware:

* Ambiguous ownership: "Connect the debugger to the target board through the SWD interface. Check its voltage level before powering on."
  - Whose voltage? Debugger's? Board's? Interface's?
* Clear ownership: "Connect the debugger to the target board through the SWD interface. Check the target board's voltage level before powering on."

### Technical review checklist

During editing, mark each pronoun and verify:
1. Does one specific term fit this pronoun?
2. Could a different term also fit logically?
3. Would a new reader identify the reference immediately?

If you answer "no" to question 1 or "yes" to question 2, replace the pronoun with its specific reference.
