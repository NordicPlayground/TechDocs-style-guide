# Lists

Lists are a great way to present complex text in a way that's easy to scan.

Lists work best when they have two to seven items. Each item should be fairly short—the reader should be able to see at least two, and preferably three, list items at a glance. It’s OK to have a couple of short paragraphs in a list item, but don’t exceed that length too often.

Make items in a list parallel. For example, each item should be a noun or a phrase that starts with a verb.

## Choosing list format

Decide between inline and vertical lists based on item count and complexity:

| Item characteristics | Format | Example |
|---------------------|--------|---------|
| Four or fewer single-word items of equal weight | Inline with commas | The SDK supports , Thread, Zigbee, and Matter. |
| Five or more items | Vertical list | The SDK supports:</br>• BLE</br>• Thread</br>• Zigbee</br>• Matter</br>• Proprietary protocols |
| Any multi-word items | Vertical list | Configure these parameters:</br>• TX power level</br>• Channel frequency</br>• Modulation scheme |
| Items containing links | Vertical list | See these guides:</br>• [Getting Started]</br>• [API Reference] |

Vertical lists enhance scannability for complex or numerous items.

## Managing long lists

Lists exceeding nine items become difficult to scan. Consider these restructuring approaches:

* **Categorize and split**: Divide into logical groupings with separate subheadings
  - Instead of one 20-item list of functions, create four 5-item lists grouped by category
* **Use nested lists**: Organize primary categories with secondary items beneath
* **Convert to table**: When items have multiple attributes, tabular format may work better
* **Question necessity**: Does every item truly belong? Remove marginal entries.

Long lists often indicate organizational opportunities—look for natural divisions.

## Bulleted lists

Use a bulleted list for things that have something in common but don’t need to appear in a particular order.

For example: The database owner can:

* Create and delete a database.
* Add, delete, or modify a document.
* Add, delete, or modify any information in the database.

## Numbered lists

Use a numbered list for sequential items (like a procedure) or prioritized items (like a top 10 list).

For example: To sign on to a database

1. On the **File** menu, select **Open database**.
1. In **Username**, enter your name.
1. In **Password**, enter your password, and then select **OK**.

### Numbered lists versus procedures

Numbered lists show sequence or priority but aren't action steps. Distinguish them from procedures:

| Looks like procedure (confusing) | Clear numbered list |
|----------------------------------|---------------------|
| The build process involves:</br>1. Compile source files</br>2. Link object files</br>3. Generate binary | The build process involves these operations:</br>1. Compiling source files</br>2. Linking object files</br>3. Generating binary output |

Use gerunds or descriptive nouns in numbered lists. Reserve imperative verbs exclusively for actual procedural steps.

### Item equivalence

All items within a list should carry similar weight and certainty:

| Mixed certainty levels | Equivalent items |
|------------------------|------------------|
| The nRF9160 includes:</br>• LTE-M modem</br>• GPS receiver</br>• Possibly secure element</br>• Maybe external flash | The nRF9160 includes:</br>• LTE-M modem</br>• GPS receiver</br>• Secure element</br></br>Optional components:</br>• External flash memory |

Separate optional or conditional items into distinct lists or explanatory text.

## Introductory text

Make sure the purpose of the list is clear. Introduce the list with a heading, a complete sentence, or a fragment that ends with a colon.

If you introduce a list with a heading, don't use explanatory text after the heading. Also, don't use a colon or period after the heading.

### Complete introductions before lists

Never insert a list between the start and end of a sentence:

| Fragmented | Complete |
|------------|----------|
| The bootloader validates:</br>• Firmware signature</br>• Version compatibility</br>• Memory boundaries</br>and then initializes peripherals. | The bootloader validates firmware signature, version compatibility, and memory boundaries, then initializes peripherals.</br></br>**Or restructure:**</br>The bootloader performs validation and initialization. Validation includes:</br>• Firmware signature</br>• Version compatibility</br>• Memory boundaries |

List introductions must form complete grammatical units before the list begins.

### Grammatical completeness in list items

List items must stand as complete grammatical units, not sentence fragments requiring the introduction to complete them:

| Dependent fragments | Independent items |
|---------------------|-------------------|
| Enable DMA when you:</br>• Need high throughput</br>• Want to reduce CPU load</br>• Have large data transfers | Enable DMA in these situations:</br>• Your application needs high throughput</br>• You want to reduce CPU load</br>• Large data transfers occur frequently |

Each item should make sense even if read without the introduction.

### Introduction phrasing

Avoid ending list introductions with prepositions or verb forms that create awkward transitions:

| Weak introduction | Strong introduction |
|-------------------|---------------------|
| DMA is useful for:</br>• High-speed transfers</br>• CPU offloading | DMA provides benefits in these scenarios:</br>• High-speed transfers</br>• CPU offloading |
| The peripheral supports:</br>• I2C mode</br>• SPI mode | The peripheral supports multiple modes:</br>• I2C mode</br>• SPI mode |

Complete introductions create cleaner separation between introduction and list content.

### Avoid verb-dependent introductions

Don't end introductions with modal verbs (can, must, should) or "to" expecting list items to complete the verb phrase:

| Verb-dependent | Self-contained |
|----------------|----------------|
| To configure the peripheral, you must:</br>• Enable the clock</br>• Set pin modes</br>• Initialize registers | Configure the peripheral with these steps:</br>• Enable the clock</br>• Set pin modes</br>• Initialize registers |
| This section explains how to:</br>• Flash firmware</br>• Debug applications | This section covers these tasks:</br>• Flashing firmware</br>• Debugging applications |

Independent introductions work better for international audiences and translation.

## Capitalization

Begin each item in a list with a capital letter unless there's a reason not to (for example, it’s a command that's always lowercase). If necessary, rewrite the list item so that all items begin with capital letters or all items begin with lowercase words.

## Punctuation

In bulleted and numbered lists, end each list item with a period if:

* Any item forms a complete sentence when combined with the list introduction that precedes the colon.

* Don’t use periods if all items have three or fewer words or if the items are UI labels, headings, subheadings, or strings.

* Any item by itself is a complete sentence.

Don’t use semicolons, commas, or conjunctions (like *and* or *or*) at the end of list items.
