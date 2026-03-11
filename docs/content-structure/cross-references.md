# Cross-references

Cross-references connect related topics and help readers navigate documentation efficiently. In online documentation, cross-references are typically hyperlinks, but the principles of effective referencing apply regardless of format.

## Formatting cross-references

### Links vs inline text

Use hyperlinks for cross-references whenever the output format supports them. For print or non-hypertext formats, use descriptive text references.

**Online (hyperlinked):**

"For pin configuration details, see [GPIO configuration](../config/gpio.md)."

**Print or non-hypertext:**

"For pin configuration details, see *GPIO configuration* on page 42."

### Cross-reference format

Use a consistent format throughout your documentation:

* "See [Topic name](link)" for directing readers to another topic
* "For more information, see [Topic name](link)" when providing supplementary detail
* "For details, see [Topic name](link)" as a shorter alternative
* "As described in [Topic name](link)" when referencing previously covered material

**Example:**

"Configure the device tree overlay as described in [Device tree configuration](../config/devicetree.md). For details about individual properties, see the [Device tree bindings reference](../api/dt-bindings.md)."

## Writing effective cross-references

### Describe the destination

Tell readers what they will find at the cross-referenced location. Don't just provide a link without context.

**Avoid:**

"See [this page](../setup.md)."

**Use:**

"For installation prerequisites and setup instructions, see [Setting up the nRF Connect SDK](../setup.md)."

### Use cross-references to avoid repetition

Instead of repeating information, reference the authoritative source. This ensures consistency and reduces maintenance.

**Avoid:**

Repeating the same 10-step installation procedure in every tutorial.

**Use:**

"Before starting this tutorial, complete the steps in [Installing the nRF Connect SDK](../setup/install.md)."

### Place cross-references strategically

**At the beginning of a topic** for prerequisites:

"This guide assumes you have completed [Setting up your development environment](../setup.md)."

**Within body text** for related concepts:

"The [device tree](../config/devicetree.md) defines the hardware configuration for your application."

**At the end of a topic** for further reading:

"## Related topics

* [BLE advertising configuration](../ble/advertising.md)
* [Connection parameters](../ble/connection.md)
* [BLE security](../ble/security.md)"

## When to use cross-references

Use cross-references when:

* Readers need prerequisite knowledge covered elsewhere
* Related information exists in another topic
* You want to avoid duplicating content
* Technical details are covered in a reference guide
* Alternative approaches are documented separately

## When not to use cross-references

Avoid cross-references when:

* The information is short enough to include directly
* The cross-reference would interrupt a critical procedure
* Readers need the information immediately (include it inline instead)
* Too many cross-references would fragment the topic

**Guideline:** If sending readers to another page would disrupt their current task, include the essential information on the current page and add the cross-reference as supplementary.

## Avoiding "above" and "below"

Don't use spatial references like "above," "below," "preceding," or "following" to refer to content elsewhere in your documentation. Online readers may enter a page from any point, and responsive layouts may reflow content.

**Avoid:**

* "As mentioned above..."
* "See the table below for details"
* "The preceding section describes..."
* "In the following example..."

**Use:**

* "As described in [BLE connection setup](../ble/connect.md)..."
* "Table 1 lists the supported peripherals"
* "[GPIO configuration](../config/gpio.md) describes the pin assignments"
* "The following code example demonstrates advertising initialization:" (acceptable when the example immediately follows)

### When "following" is acceptable

Use "following" only when the referenced content appears immediately after the current sentence, with no intervening content:

**Acceptable:**

"Use the following command to build the application:

```bash
west build -b nrf52840dk_nrf52840
```"

**Not acceptable:**

"The following sections describe the three configuration methods."

(Several sections and headings intervene before the reader reaches all three methods. Use specific cross-references instead.)

## Using "previous," "next," and "following"

For sequential content (tutorials, multi-step guides), use "previous" and "next" only when the sequence is clearly defined.

**Acceptable:**

* "In the [previous tutorial](../tutorial-01.md), you set up the development environment."
* "In the [next section](#configuring-ble), you will configure BLE advertising."

**Avoid for non-sequential content:**

* "The previous page discussed..." (reader may not have come from that page)

## Nordic-specific cross-reference examples

**Referencing SDK documentation:**

"For a complete list of Kconfig options, see the [nRF Connect SDK Kconfig reference](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/kconfig/)."

**Referencing API documentation:**

"The `bt_le_adv_start()` function is documented in the [Bluetooth advertising API](../api/bt_adv.md)."

**Referencing hardware documentation:**

"For the complete pin assignment, see the [nRF52840 DK hardware description](../hardware/nrf52840dk.md)."

**Referencing external standards:**

"The implementation follows the [Bluetooth Core Specification v5.3](https://www.bluetooth.com/specifications/) (external link)."
