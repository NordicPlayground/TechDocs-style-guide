# Words ending in -ing

A word ending in *–ing* can be a verb, a noun, or an adjective. Use "–ing" words with care. The sentence should make it clear which role the word plays.

For example, we don't know whether the heading, "Meeting requirements", will be a discussion of how to meet requirements or the requirements for a meeting.

These examples are clearer:

* The meeting requirements
* Meeting the requirements
* The requirements for the meeting
* How to meet the requirements

## Understanding dual-meaning problems

Words ending in -ing or -ed create confusion when they can function as either action words or descriptors. Readers cannot tell which interpretation you intended.

### When -ing words create two possible meanings

Consider this sentence: "Configuring peripherals requires administrator access."

This could mean either:
- The act of configuring peripherals requires access (action-focused reading)
- The peripherals that handle configuration require access (descriptor-focused reading)

The same pattern appears in many technical contexts:

* "Updating firmware may cause device resets."
  - Could mean: The process of updating firmware may cause resets
  - Could mean: Firmware that performs updates may cause resets
* "Programming tools are available in the SDK."
  - Could mean: Tools for programming are available
  - Could mean: Tools that program themselves are available (unlikely but grammatically possible)

### When -ed words create ambiguity

Past participles (-ed forms) pose similar challenges when they could modify different parts of a sentence:

* "The API returns values configured in the device tree."
  - Which configuration applies where? To the values? To the return process?
  - Clearer: "The API returns the values that are configured in the device tree."
* "Sensors connected to GPIO pins trigger interrupts."
  - Are the sensors connected, or do they trigger connected interrupts?
  - Clearer: "Sensors that connect to GPIO pins will trigger interrupts."

## Solutions for -ing word ambiguity

### Strategy 1: Insert determiners

Add "the," "a," "your," or "this" between the -ing word and the following noun:

* Original: "Debugging applications demands specialized hardware."
* With determiner: "Debugging the applications demands specialized hardware." (now clearly an action)

This works when you want the action interpretation. For the descriptor interpretation, use a different strategy.

### Strategy 2: Convert to compound nouns

Replace the -ing word with a related noun or adjective form:

* Original: "Testing devices must meet quality standards."
* As compound: "Test devices must meet quality standards." (now clearly a type of device)
* Alternative: "Device tests must meet quality standards." (reordered to remove ambiguity)

### Strategy 3: Relocate the modifier

Move the -ing or -ed phrase to a position where only one interpretation makes sense:

* Original: "The driver processes packets received from the network using DMA."
  - Does DMA apply to processing or to receiving?
* Relocated: "Using DMA, the driver processes packets received from the network." (DMA clearly applies to processing)
* Also clear: "The driver processes packets that were received from the network using DMA." (DMA clearly applies to receiving)

### Strategy 4: Expand into multiple sentences

Break complex constructions into separate statements:

* Original: "Enable logging features configured for real-time monitoring."
  - Are the features configured? Or does logging happen during configuration?
* Expanded: "Configure the features for real-time monitoring. Then enable logging."
* Alternative: "Enable the logging features. These features are configured for real-time monitoring."

### Strategy 5: Choose different verbs

Rewrite using verbs that don't create -ing/-ed forms:

* Original: "Flashing bootloader files requires caution."
* Alternative: "Flash the bootloader files with caution."
* Also works: "Exercise caution when you flash bootloader files."

## Practical guidelines

Apply these principles when writing or reviewing technical content:

* **In headings**: Avoid bare -ing words. Use "How to..." or noun forms instead.
  - Weak: "Connecting devices"
  - Better: "How to connect devices" or "Device connections"
* **In procedures**: Favor clear imperative verbs over -ing forms.
  - Weak: "Enabling debugging requires setting flags."
  - Better: "To enable debugging, set the appropriate flags."
* **In descriptions**: Spell out relationships explicitly.
  - Weak: "The modified registers control power states."
  - Better: "The registers that you modified control power states."
* **In warnings**: Eliminate any possibility of misreading.
  - Weak: "Disconnecting devices may cause data loss."
  - Better: "Data loss may occur if you disconnect devices during operation."

When you notice an -ing or -ed word near a noun, pause and verify that only one reading makes sense. If you can imagine two interpretations, your readers certainly will.
