# Reader-focused writing

Technical documentation exists to help readers accomplish their goals. Write from the reader's perspective, not from the perspective of the product, the development team, or the organization.

## Focus on the reader's task

Readers come to documentation with a specific goal. Structure your content to help them achieve that goal as quickly as possible.

### Ask "What does the reader need?"

Before writing, identify:

* What task the reader wants to complete
* What the reader already knows
* What information the reader needs from you
* What the reader will do after reading

### Write for the reader's workflow

Organize content in the order the reader needs it, not in the order the product was designed or the features were implemented.

**Product-focused (how it was built):**

"The BLE stack initializes the Host Controller Interface, configures the Link Layer, sets up the Logical Link Control and Adaptation Protocol, and then enables the Generic Access Profile."

**Reader-focused (how to use it):**

"To start BLE on your device:

1. Enable BLE in `prj.conf` with `CONFIG_BT=y`.
2. Call `bt_enable()` in your application code.
3. Register a callback for connection events."

## Use second person

Address the reader directly with "you." Second person is more engaging, clearer, and shorter than alternatives.

**Second person (preferred):**

"You can configure up to four simultaneous BLE connections."

**Third person (distant):**

"The developer can configure up to four simultaneous BLE connections."

**First person plural (avoid):**

"We can configure up to four simultaneous BLE connections."

### Imperative mood in procedures

In step-by-step instructions, use the imperative mood (implied "you"). This is the most direct way to write procedures.

**Imperative (preferred):**

"Open `prj.conf` and add `CONFIG_BT=y`."

**Not imperative (wordy):**

"You should open `prj.conf` and then you need to add `CONFIG_BT=y`."

## Don't write from the product's perspective

Avoid describing features in terms of what the product does or what the development team created. Frame everything in terms of what the reader can accomplish.

**Product-focused:**

"The nRF Connect SDK provides a comprehensive set of libraries for Bluetooth Low Energy development, including support for GATT services, advertising, and connection management."

**Reader-focused:**

"Use the nRF Connect SDK BLE libraries to create GATT services, configure advertising, and manage connections."

**Product-focused:**

"We added a new power profiling feature in v2.5.0."

**Reader-focused:**

"In v2.5.0, you can measure real-time power consumption using the new power profiling feature."

## Don't assume knowledge

### State prerequisites explicitly

Don't assume readers have background knowledge unless you have stated the prerequisites. If a topic requires specific knowledge or setup, say so at the beginning.

**Example:**

"**Prerequisites:**

* nRF Connect SDK v2.5.0 or later installed
* nRF52840 DK connected via USB
* Basic familiarity with C programming"

### Define terms on first use

When introducing a term that readers may not know, define it briefly or link to a definition.

**Example:**

"The device tree, a data structure that describes the hardware configuration, defines which peripherals are available to your application."

### Don't assume tool familiarity

If a procedure uses a specific tool, provide enough context for readers to locate and use it.

**Insufficient:**

"Run the debug command."

**Sufficient:**

"In nRF Connect for VS Code, click **Run and Debug** in the Activity Bar, then click **Start Debugging**."

## Don't talk down to readers

### Avoid minimizing language

Words like "just," "simply," "easily," and "obviously" suggest that a task is trivial. If the reader is struggling, these words make them feel incompetent.

**Avoid:**

* "Simply add the configuration option"
* "Just flash the firmware"
* "You can easily configure the device"

**Use:**

* "Add the configuration option"
* "Flash the firmware"
* "Configure the device"

See [Bias-free communication](bias-free-communication.md) for more on avoiding condescending tone.

### Don't over-explain obvious concepts

Trust readers to understand common concepts without lengthy explanations. Focus your explanations on what is unique or complex.

**Over-explained:**

"A file is a collection of data stored on your computer. You can open a file using a text editor. A text editor is a program that lets you view and modify text files."

**Appropriately concise:**

"Open `prj.conf` in a text editor."

### Don't under-explain complex concepts

The flip side: don't assume readers understand domain-specific concepts that may be new to them. Provide definitions, examples, and links for specialized topics.

## Help readers recover from errors

Anticipate where readers might go wrong and provide guidance for recovery.

### Include troubleshooting sections

After procedures with common failure points, add a troubleshooting section:

"**Troubleshooting:**

If the build fails with `CONFIG_BT not set`:

1. Verify that `CONFIG_BT=y` is in `prj.conf`.
2. Ensure no syntax errors exist in the configuration file.
3. Run `west build --pristine` to perform a clean build."

### Describe expected outcomes

Tell readers what success looks like so they can confirm they are on the right track.

**Example:**

"After flashing, the LED1 on the DK blinks at 1 Hz. If the LED does not blink, verify the USB connection and repeat the flashing step."

## Write for the reader's time

Readers have limited time and patience. Respect their time by being concise and getting to the point.

* Put the most important information first
* Don't repeat yourself
* Don't include information that doesn't serve the reader's goal
* Use cross-references instead of duplicating content
* Provide a summary or overview for long topics
