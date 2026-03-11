# Scannable writing

Most online readers scan content rather than reading word by word. Research shows that users read only 20-28% of text on a typical web page. Structure your writing to accommodate this behavior.

## Keep paragraphs short

Limit paragraphs to 3-7 lines (approximately 40-75 words). Short paragraphs create visual white space, reduce cognitive load, and make content less intimidating.

**Too long (12 lines):**

A dense paragraph covering multiple topics with no visual breaks makes it difficult for readers to find the specific information they need, forces them to read every word, and increases the chance they will abandon the page entirely before finding what they came for.

**Right length (4 lines):**

Keep paragraphs focused on a single idea. Readers scan for the information they need and skip everything else. Short paragraphs make scanning faster and more effective.

## One idea per paragraph

Each paragraph should communicate a single concept. When you find yourself shifting topics, start a new paragraph.

**Avoid (multiple ideas in one paragraph):**

"The nRF52840 supports Bluetooth Low Energy 5.3 with extended advertising, coded PHY, and 2M PHY. It includes a 64 MHz Arm Cortex-M4 processor. The device supports Thread and Zigbee protocols as well. Power consumption in System OFF mode is 400 nA."

**Use (one idea per paragraph):**

"The nRF52840 supports Bluetooth Low Energy 5.3 with extended advertising, coded PHY, and 2M PHY. It also supports Thread and Zigbee protocols.

The device includes a 64 MHz Arm Cortex-M4 processor with floating point unit.

Power consumption in System OFF mode is 400 nA."

## Lead with the main point

Place the most important information in the first sentence of each paragraph and each section. This follows the inverted pyramid structure used in journalism: lead with the conclusion, then provide supporting details.

**Avoid (burying the key information):**

"After reviewing the hardware specifications and comparing the available options, considering power consumption requirements and protocol support, you should use the nRF52840 for applications requiring both Bluetooth Low Energy and Thread."

**Use (leading with the point):**

"Use the nRF52840 for applications that require both Bluetooth Low Energy and Thread support. The nRF52840 offers the lowest power consumption among multiprotocol devices in the nRF52 Series."

## Use topic sentences effectively

Start each section or major paragraph with a clear topic sentence that tells readers what to expect.

**Example topic sentences:**

* "Three configuration options control BLE advertising behavior."
* "The build system requires west version 0.14 or later."
* "Power management reduces current consumption during idle periods."

Readers scanning headings and first sentences should get a complete summary of your document.

## Visual scanning patterns

Online readers follow predictable scanning patterns. The most common is the F-pattern: readers scan horizontally across the top, then vertically down the left side, occasionally scanning horizontally again.

### Optimize for scanning behavior

**Front-load important words.** Place key terms at the beginning of headings, list items, and sentences.

**Avoid:**

* "A guide to configuring Bluetooth Low Energy advertising"
* "Information about power management settings"

**Use:**

* "Bluetooth Low Energy advertising configuration"
* "Power management settings"

**Use visual hierarchy.** Headings, subheadings, bold text, and lists create visual landmarks that guide scanning.

**Break up walls of text.** Use a combination of:

* Headings every 2-4 paragraphs
* Bulleted or numbered lists
* Tables for comparative information
* Code examples for technical details
* Admonitions for important notes

## Write clearly and simply

Use plain language to reduce reading time and improve comprehension.

* Use common words over technical jargon when possible
* Keep sentences under 25 words
* Prefer active voice
* Use present tense
* Avoid unnecessary qualifiers ("very," "really," "basically")

## Replace text with tables, charts, and figures

When information involves comparisons, sequences, or relationships, consider whether a visual format communicates more effectively than prose.

**Better as a table:**

| Protocol | Range | Data Rate | Power |
| -------- | ----- | --------- | ----- |
| BLE | 100 m | 2 Mbps | Low |
| Thread | 100 m | 250 kbps | Low |
| Wi-Fi | 50 m | 600 Mbps | High |

**Rather than:**

"Bluetooth Low Energy has a range of approximately 100 meters, supports data rates up to 2 Mbps, and has low power consumption. Thread also has a range of approximately 100 meters but supports data rates of 250 kbps with low power consumption. Wi-Fi has a shorter range of about 50 meters but supports data rates up to 600 Mbps, though with higher power consumption."

## Write meaningful headings

Headings are the most-read content on any page. Make them descriptive and specific.

**Vague headings:**

* "Overview"
* "Details"
* "More Information"

**Descriptive headings:**

* "BLE advertising configuration overview"
* "GPIO pin assignment details"
* "Power consumption reference"

Use parallel structure across headings at the same level. If one heading starts with a verb, all sibling headings should start with verbs.

## Use bulleted lists and jump lists

Convert series of three or more items into bulleted lists. They are faster to scan than inline lists.

**Inline (harder to scan):**

"The nRF Connect SDK supports nRF52840, nRF5340, nRF9160, and nRF54 Series devices."

**Bulleted (easier to scan):**

"The nRF Connect SDK supports:

* nRF52840
* nRF5340
* nRF9160
* nRF54 Series"

Use jump lists (linked lists at the top of long pages) to help readers navigate directly to the section they need.

## Condense text carefully

Reducing word count improves scannability, but don't sacrifice clarity or completeness.

**Safe to cut:**

* Introductory phrases ("It should be noted that...", "It is important to mention...")
* Redundant modifiers ("completely finished", "absolutely essential")
* Filler words ("actually", "basically", "really", "very")
* Restating information already covered

**Don't cut:**

* Technical details needed for accuracy
* Prerequisites and warnings
* Context that prevents errors
* Steps in procedures
