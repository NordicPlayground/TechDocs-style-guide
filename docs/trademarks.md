# Trademarks

Nordic trademarks will be collected and maintained by marketing. See [Trademarks](https://nordicsemi.atlassian.net/wiki/spaces/MAR/pages/132941867/Trademarks) in their space for a complete list. For Nordic product names see [Product names](https://nordicsemi.atlassian.net/wiki/spaces/MAR/pages/132940950/Product+names). See also RMF pp. 188 - 193.

## Adding trademarks with conkeyref

We add trademarks to our documentation using conkeyref. Trademarksare listed in [Infocenter/keydef/terms.dita](https://projecttools.nordicsemi.no/bitbucket/projects/TECHDOC/repos/infocenter/browse/keydef/terms.dita). In our documentation, each occurrence of a third party product or company name should use the conkeyref instead of marking up the text.

## General guidelines

In principle, trade names and trademarks do not need to have any trademark symbol used with them. We use it for those organizations we have a relationship with as a courtesy.

A relationship means:

* Any third party components we use on a PCB board (for example dev kit) or with our ICs.
* Protocols that we have strong links to the organizations that run them i.e., ANT+ and Bluetooth.

## Trademark terminology

Understanding trademark terminology helps you use trademarks correctly in documentation.

| **Term** | **Definition** | **Example** |
| -------- | -------------- | ----------- |
| **Trademark (™)** | A word, phrase, symbol, or design that identifies the source of goods or services and distinguishes them from others | Nordic Semiconductor™ |
| **Registered trademark (®)** | A trademark that has been officially registered with a government trademark office | Bluetooth® |
| **Service mark (℠)** | Similar to a trademark, but identifies services rather than products | Nordic DevAcademy℠ |
| **Trade name** | The official name under which a company does business | Nordic Semiconductor ASA |
| **Brand name** | A name given by a company to a product or service | nRF Connect SDK |
| **Legend** | The trademark attribution statement, typically at the bottom of a page or in a legal section | "Bluetooth is a registered trademark of Bluetooth SIG, Inc." |

### Trademark vs. registered trademark

* **™** indicates an unregistered trademark (common law rights)
* **®** indicates a trademark registered with a national trademark office
* Use the symbol that matches the trademark owner's usage

## Proper use of trademarks

Trademarks must be used correctly to maintain their legal protection and show respect for trademark owners.

### Trademark symbols (™, ®, ℠)

Use trademark symbols according to these guidelines:

**When to use symbols:**

* On first and most prominent use of the trademark in a document
* In marketing materials and product names
* When referencing third-party trademarks per their guidelines
* In headers, titles, or other prominent locations

**When symbols may be omitted:**

* Subsequent uses after the first marked occurrence
* In body text after establishing the trademark in the introduction
* In technical specifications where frequent use would clutter the text

**Example:**

"The nRF Connect SDK supports Bluetooth® wireless technology for developing IoT applications. Configure Bluetooth settings in the device configuration file..."

[First use has ®, subsequent uses omit it]

### Symbol placement

Place the trademark symbol immediately after the trademark, with no space:

* **Correct:** Bluetooth®
* **Incorrect:** Bluetooth ®, Bluetooth ® , Bluetooth (®)

Position symbols as superscripts when formatting allows:

* HTML/Markdown: `Bluetooth<sup>®</sup>` renders as Bluetooth®
* Plain text: Bluetooth(R) or Bluetooth® depending on available characters

### Trademarks as adjectives, not nouns

Always use trademarks as adjectives modifying a noun, never as nouns themselves.

**Incorrect use (as nouns):**

* "Connect using Bluetooth"
* "Install the nRF Connect SDK"
* "Use Zephyr for your application"

**Correct use (as adjectives):**

* "Connect using Bluetooth® wireless technology"
* "Install the nRF Connect SDK development kit"
* "Use the Zephyr® RTOS for your application"

**Acceptable shortened forms after first use:**

* First mention: "Bluetooth® Low Energy technology"
* Later mentions: "Bluetooth Low Energy" (adjective + descriptive term)

### Don't pluralize or use possessive

Trademarks should never be pluralized or made possessive.

**Avoid:**

* "We tested three nRF52840s"
* "The Bluetooth's range is..."
* "Multiple Zephyrs running simultaneously"

**Use:**

* "We tested three nRF52840 devices"
* "The Bluetooth connection's range is..."
* "Multiple Zephyr RTOS instances running simultaneously"

## Trademarks in online works

Web-based documentation requires additional considerations for trademark use.

### Link trademark symbols appropriately

When trademarks appear in links, apply the symbol to the full trademark, not the link:

**Correct:**

* [Learn about Bluetooth® technology](https://www.bluetooth.com)
* [Download the nRF Connect SDK](https://www.nordicsemi.com)

Don't place trademark symbols in the link text if they're not part of the natural link label.

### Provide trademark attributions

Include a trademark attribution section or footer on web pages:

**Example:**

"Bluetooth® is a registered trademark of Bluetooth SIG, Inc. nRF Connect SDK is a trademark of Nordic Semiconductor ASA. All other trademarks are the property of their respective owners."

### Maintain trademarks in metadata

When appropriate, include trademarks in:

* Page titles: "nRF Connect SDK - Bluetooth® Development"
* Meta descriptions: "Develop Bluetooth Low Energy applications with the nRF Connect SDK"
* Image alt text: "Bluetooth Low Energy connection diagram"

## Third-party trademarks

When referencing other companies' trademarks, follow their trademark guidelines.

### Check trademark owner guidelines

Before using a third-party trademark, review the owner's trademark usage guidelines:

* Bluetooth SIG: [Brand Guide](https://www.bluetooth.com/brand-guide)
* Arm: [Trademark List](https://www.arm.com/company/policies/trademarks)
* Wi-Fi Alliance: [Brand Guidelines](https://www.wi-fi.org/who-we-are/our-brands)

### Use correct trademark forms

Use the exact form specified by the trademark owner:

* Bluetooth® wireless technology (not "BLE", or "Bluetooth Smart" unless specifically appropriate)
* Arm® Cortex®-M4 processor (not "ARM Cortex M4" or "Cortex-M4 CPU")
* Wi-Fi® technology (not "WiFi" or "Wifi")

### Include required attributions

Some trademark owners require specific attribution statements. Include these in your documentation:

**Example:**

"Bluetooth® is a registered trademark of Bluetooth SIG, Inc. Any use of the Bluetooth trademarks by Nordic Semiconductor ASA is under license."

### Don't create confusion

Never use trademarks in a way that:

* Implies endorsement by the trademark owner (unless you have permission)
* Suggests your product is made by the trademark owner
* Dilutes or tarnishes the trademark

**Avoid:**

* "Nordic's Bluetooth solution" (implies ownership of the Bluetooth trademark)

**Use:**

* "Nordic's Bluetooth® technology implementation"
* "Nordic devices with Bluetooth Low Energy support"

## Company Trademarks

| Company       | Trademark Guidelines |
| ------------- | -------------------- |
| Altium        | Do not mark. [Copyrights and Trademarks](http://www.altium.com/copyrights-and-trademarks) |
| ANT+          | ANT™ ANT+™ (See ANT+ Brand Guide: "The trademark symbol is to be used in the first appearance of the word and then dropped. Text is to be in all capitals with no space or periods in between the letters or '+'." ) |
| Apache        | Do not mark. |
| Apple         | Do not mark. [Apple Trademark List](http://www.apple.com/legal/intellectual-property/trademark/appletmlist.html) |
| Arduino       | Do not mark. [Arduino FAQ](https://www.arduino.cc/en/Main/FAQ) |
| Arm           | For Arm trademarks, see the [Arm Trademark List](https://www.arm.com/company/policies/trademarks). |
| Bluetooth     | For Bluetooth trademarks and usage, see the [Bluetooth Brand Guide](https://www.bluetooth.com/brand-guide). Bluetooth® (italics + reg trademark on the first and most prominent use/when first used in text - We emphasize all!) See Brand Best Practices and Guidelines. |
| Canonical     | Do not mark. [Ubuntu Visual Identity](https://wiki.ubuntu.com/Artwork/VisualIdentity?action=AttachFile&do=get&target=ubuntu_interim_guides_03June.pdf) |
| CoreMark      | CoreMark® [EEMBC CoreMark](https://www.eembc.org/coremark/) |
| EEMBC         | Do not mark, includes CoreMark. |
| Gill Electronics | Do not mark. (TesLink®) |
| Google        | Do not mark. |
| IAR           | Do not mark. [IAR Trademarks](https://www.iar.com/metapages/trademarks/) |
| Intel         | Do not mark. [Intel Trademarks](http://www.intel.com/content/www/us/en/trademarks/symbols-acknowledgments.html) |
| InvenSense    | InvenSense® SmartMotion® (No brand guide?) |
| Matter        | Do not mark. |
| Microsoft     | Do not mark. Microsoft® Microsoft Windows® (General Microsoft Trademark Guidelines; Include an attribution of Microsoft ownership of the trademark(s) in the credit notice section of your documentation or advertisement—follow this format: Microsoft Encarta MSN and Windows are either registered trademarks or trademarks of Microsoft Corporation in the United States and/or other countries.) |
| NFC           | Do not mark. See NFC Branding. Statement: NFC Forum and the NFC Forum logo are trademarks of the Near Field Communication Forum. (N-mark is TM.) |
| NuCurrent Inc.| Do not mark. (No brand guide?) |
| Python        | Do not mark. Python® (The first or most prominent mention of a Python trademark should be immediately followed by a symbol for registered trademark: "®" or "(r)". For example "Python® ..."; See [PSF Trademarks](https://www.python.org/psf/trademarks/)) |
| SEGGER        | J-Link J-Trace - No mark. |
| Synaptics     | Synaptics®, ClickPad™, TouchPad™ (No brand guide?) |
| Wi-Fi Alliance| Wi-Fi®, Wi-Fi CERTIFIED™ [Wi-Fi Brands](https://www.wi-fi.org/who-we-are/our-brands) |
| Zigbee        | Do not mark. |
