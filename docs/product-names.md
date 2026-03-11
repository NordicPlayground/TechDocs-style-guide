# Product names

This page defines how to write Nordic Semiconductor product names in documentation. For the authoritative list of current product names, see the Product names page in the Marketing space (Confluence).

Do not use product names before they are officially announced or launched without approval from the responsible TPM, Product Director, and Launch Manager.

## Article usage

### Main product names (ICs)

Treat main product names (IC part numbers) as proper nouns. Do not use an article unless the name is followed by a descriptor.

| Context | Example |
| ------- | ------- |
| **Standalone (no article)** | nRF52840 is an ultra-low power 2.4 GHz wireless SoC. |
| **With descriptor (use "the")** | The nRF52840 SoC is part of the nRF52 Series. |
| **First mention in a document** | The nRF52840 from Nordic Semiconductor is an ultra-low power... |
| **Exception (product pages, briefs, user guides)** | nRF52840 is a multiprotocol SoC for... |

### Supporting products

Supporting products (development kits, evaluation kits, software, tools) require "the" before the product name.

| Product type | Example |
| ------------ | ------- |
| **Development kits** | The nRF52840 DK is a hardware development platform. |
| **Evaluation kits** | The nPM1100 EK is a dedicated evaluation kit. |
| **Software** | The nRF Connect SDK is the common software development kit for Nordic products. |
| **Tools** | The Programmer app in nRF Connect for Desktop allows you to flash firmware. |
| **Prototyping platforms** | The Nordic Thingy:91 is a battery-operated prototyping platform. |
| **Cloud services** | The nRF Cloud is a cloud platform for Nordic devices. |

### Special leading characters

For terms with special leading characters, choose the article that matches the pronunciation.

**Example:** "an `#include` statement" (pronounced "an include statement")

## Product taxonomy

### Family

A product family is a group of products in the same broad product category. Product families can contain multiple product series.

* **First mention:** The nPM Family from Nordic Semiconductor
* **Subsequent references:** The family, the nPM Family

### Series

A product series is a group of products in the same product category and generation with common hardware and software architecture.

* **First mention:** The nRF52 Series from Nordic Semiconductor
* **Subsequent references:** The series, the nRF52 Series

**Referencing multiple series:**

| | Example |
| --- | --- |
| **Allowed** | The SDK supports the nRF91, nRF53, and nRF52 Series devices. |
| **Not allowed** | nRF Series, nRF5 Series, nRF5x Series, nRF9 Series, nRF9x Series |

**Current product series:** nRF91 Series, nRF70 Series, nRF54H Series, nRF54L Series, nRF53 Series, nRF52 Series, nRF51 Series, nRF22 Series.

### Sub-series

A product sub-series is a subset of a product series sharing common properties. Sub-series is not a brand; use it as an optional technical term when it adds clarity.

**Example:** nRF54LM sub-series, nRF54LV sub-series

## Writing product names

### ICs

For each IC, follow this pattern:

* **First mention:** The [product] from Nordic Semiconductor
* **Subsequent references:** The product name alone, or "the [product type]"

**Examples:**

* First mention: "The nRF5340 from Nordic Semiconductor is a dual-core wireless SoC."
* Subsequent: "The nRF5340 supports Bluetooth Low Energy and Thread." or "Configure the SoC for..."

### Development kits and prototyping platforms

* **First mention:** The [product] from Nordic Semiconductor
* **Subsequent references:** The product name, the DK, the kit

**Thingy products:**

* First mention: "The Nordic Thingy:91 from Nordic Semiconductor"
* Subsequent: "Thingy:91" or "the Thingy"

### nRF Connect SDK

* **First mention:** The nRF Connect SDK from Nordic Semiconductor
* **Subsequent references:** The nRF Connect SDK, the SDK
* **Not allowed:** NCS (reach out to PMT for exceptions)

**nRF Connect SDK Add-ons:**

* Plural: The nRF Connect SDK Add-ons from Nordic Semiconductor
* Singular: The nRF Connect SDK add-on
* First occurrence must include "nRF Connect SDK" before "Add-ons"

**Bare Metal option:**

* In filenames, folder names, C code, Kconfig: `bare_metal` or `bm`
* Do not use: baremetal (as a single word) or bare-metal (hyphenated)

### Desktop apps (nRF Connect for Desktop)

* **First mention:** The [app name] app in nRF Connect for Desktop
* **Subsequent references:** The [app name] app, the app, the desktop app, or [app name] alone
* First occurrence must mention nRF Connect for Desktop

**Desktop apps:** Bluetooth Low Energy, Board Configurator, Cellular Monitor, Direct Test Mode, nPM PowerUP, Power Profiler, Programmer, Quick Start, RSSI Viewer, Serial Terminal, Toolchain Manager.

**Example:**

* First mention: "Open the Quick Start app in nRF Connect for Desktop."
* Subsequent: "The Quick Start app guides you through the initial setup."

### Mobile apps

* **First mention:** The [app name] from Nordic Semiconductor
* **Subsequent references:** The [app name], the app, the mobile app

### Cloud services

* **First mention:** The [service name] from Nordic Semiconductor
* **Subsequent references:** The [service name], the service

**Cloud services:** nRF Cloud, nRF Cloud Location Services, nRF Cloud Security Services.

## Formatting rules

### Capitalization

Product names are proper nouns. Preserve the original capitalization in all contexts.

| Correct | Incorrect |
| ------- | --------- |
| nRF52840 | NRF52840, Nrf52840, nrf52840 |
| nRF Connect SDK | NRF Connect SDK, nrf connect sdk |
| Nordic Thingy:91 | Nordic thingy:91, NORDIC THINGY:91 |
| nPM1300 | NPM1300, Npm1300 |

### Headings

Product names in headings follow the same capitalization as in body text. Do not alter the product name to match heading capitalization style.

**Correct:** "Working with nRF52840 DK"

**Incorrect:** "Working with NRF52840 DK"

### Product names at the start of a sentence

When a product name starts with a lowercase letter (nRF, nPM), do not capitalize it at the start of a sentence. Restructure the sentence if needed.

**Avoid:** "nRF52840 is an ultra-low power SoC." (starting a sentence with lowercase)

**Preferred:** "The nRF52840 is an ultra-low power SoC." (add article)

**Also acceptable for product-specific pages:** "nRF52840 is an ultra-low power SoC." (exception for product pages, product briefs, and user guide introductions)

### Plural forms

Do not pluralize product names. Use the product name as a modifier.

| Correct | Incorrect |
| ------- | --------- |
| nRF52840 devices | nRF52840s |
| nRF52840 DK boards | nRF52840 DKs |

### Pronunciation guide

When a product name might be mispronounced, include a pronunciation guide on first mention in audio/video content documentation.

**Example:** nPM2100 is pronounced "N.P.M. twenty-one-hundred" (/ˈɛnpiːɛm/).
