# Sentence structure

Clear sentence structure makes documentation easier to read, translate, and understand. Follow these guidelines to write sentences that communicate effectively.

## Keep sentences short

Aim for an average sentence length of 15-20 words. Vary the length for rhythm, but keep individual sentences under 25 words.

**Too long (38 words):**

"When you are developing a Bluetooth Low Energy application using the nRF Connect SDK, you should configure the advertising parameters in the project configuration file before building the application so that the device broadcasts correctly."

**Better (two sentences, 15 and 14 words):**

"Configure BLE advertising parameters in `prj.conf` before building your application. This ensures the device broadcasts with the correct settings."

## One idea per sentence

Each sentence should express a single thought. If a sentence contains two independent ideas, split it.

**Two ideas (split these):**

"The nRF52840 supports BLE 5.3 and it has a 64 MHz Arm Cortex-M4 processor."

**One idea per sentence:**

"The nRF52840 supports BLE 5.3. It includes a 64 MHz Arm Cortex-M4 processor."

## Sentence patterns

### Subject-verb-object (SVO)

Use the standard English SVO order. Place the subject first, then the verb, then the object. Readers process this pattern fastest.

**SVO (clear):**

"The build system compiles the application."

**Inverted (harder to process):**

"Compiled by the build system is the application."

### Put conditions before instructions

When a sentence includes a condition and an action, put the condition first. This prevents readers from starting an action that doesn't apply to them.

**Condition first (correct):**

"If your application uses Bluetooth, add `CONFIG_BT=y` to `prj.conf`."

**Action first (reader may act before reading the condition):**

"Add `CONFIG_BT=y` to `prj.conf` if your application uses Bluetooth."

### Put time references first

When a sentence describes when something happens, place the time reference at the beginning.

**Time first:**

"After the device resets, the bootloader validates the firmware image."

**Time buried:**

"The bootloader validates the firmware image after the device resets."

## Active voice vs passive voice

Use active voice as the default. Active voice is more direct, shorter, and easier to understand.

**Active (preferred):**

"The bootloader validates the firmware image."

**Passive (avoid when possible):**

"The firmware image is validated by the bootloader."

### When passive voice is acceptable

Use passive voice when:

* The actor is unknown or irrelevant: "The connection is terminated after 30 seconds of inactivity."
* The object is more important than the actor: "The firmware image is stored in the external flash."
* Active voice would create an awkward sentence
* Describing a system behavior where no user action is involved

See [Verbs](verbs.md) for more guidance on active and passive voice.

## Parallel structure

Use the same grammatical pattern for items in a series, list items, and headings at the same level.

### In lists

**Parallel (all verb phrases):**

* Configure the advertising parameters
* Build the application
* Flash the firmware
* Verify the output

**Not parallel (mixed structures):**

* Configure the advertising parameters
* Building the application
* The firmware should be flashed
* Verification

### In series

**Parallel:**

"The nRF52840 supports Bluetooth Low Energy, Thread, and Zigbee."

**Not parallel:**

"The nRF52840 supports Bluetooth Low Energy, and it works with Thread, and Zigbee is also supported."

### In headings

**Parallel (all gerund phrases):**

* Installing the SDK
* Configuring the project
* Building the application
* Flashing the firmware

**Not parallel:**

* Installing the SDK
* Project configuration
* How to build
* Flash the firmware

## Avoid complex sentence constructions

### Limit subordinate clauses

Avoid stacking multiple subordinate clauses in a single sentence.

**Too complex:**

"When you build an application that uses the BLE subsystem, which requires the SoftDevice controller, that must be configured before the application starts, you need to set the correct memory regions."

**Simplified:**

"BLE applications require the SoftDevice controller. Configure the controller before the application starts. Set the correct memory regions in the configuration."

### Avoid nested parenthetical statements

Parenthetical remarks inside parenthetical remarks make sentences hard to follow.

**Avoid:**

"The nRF52840 DK (which includes the nRF52840 SoC (the most advanced chip in the nRF52 Series)) supports all major IoT protocols."

**Use:**

"The nRF52840 DK includes the nRF52840 SoC, the most advanced chip in the nRF52 Series. It supports all major IoT protocols."

### Avoid long introductory phrases

Keep introductory phrases short. If the introduction exceeds 10 words, consider restructuring the sentence.

**Too long:**

"In order to ensure that the application correctly handles the Bluetooth Low Energy connection event, register a callback function."

**Better:**

"To handle BLE connection events, register a callback function."

## Word order for clarity

### Place modifiers next to what they modify

Misplaced modifiers create ambiguity.

**Ambiguous:**

"The developer debugged the application using the IDE that crashed."
(Did the IDE crash, or the application?)

**Clear:**

"Using the IDE, the developer debugged the application that crashed."

### Avoid dangling modifiers

A dangling modifier describes something that isn't present in the sentence.

**Dangling:**

"After resetting the device, the LED turns on."
(The LED didn't reset the device.)

**Correct:**

"After you reset the device, the LED turns on."

## Using "that" and "which"

Use "that" for restrictive clauses (essential information, no commas). Use "which" for nonrestrictive clauses (additional information, with commas).

**Restrictive (that):**

"The configuration option that controls advertising interval is `CONFIG_BT_ADV_INT`."
(Identifies which specific option.)

**Nonrestrictive (which):**

"The `CONFIG_BT_ADV_INT` option, which controls advertising interval, defaults to 100 ms."
(Adds extra information about an already-identified option.)

See [Clauses](clauses.md) for detailed guidance on restrictive and nonrestrictive clauses.
