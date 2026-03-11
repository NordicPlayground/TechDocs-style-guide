# Writing step-by-step instructions

Follow these guidelines to help you create clear, easy-to-follow instructions, whether you're writing simple, single-step procedures or complex
procedures that consist of multiple steps.

## Complex procedures

Complex instructions often consist of multiple steps formatted as a numbered list. For multiple-step procedures in numbered lists:

* Format procedures consistently so customers can find them easily by scanning.

* Use the heading to tell customers what the instructions will help them do. Choose one phrasing style for the headings, and write them all the same way (in parallel structure).

    * For example: To add an account
    * For example: Add an account

* Use a separate numbered entry for each step. It's OK to combine short steps that occur in the same place in the UI.

* Include actions that finalize a step, such as OK or Apply buttons.

* Use complete sentences with verbs in the imperative form.

* Use consistent sentence structures. For example, always use a phrase when you need to tell the customer where to start. The rest of the time, start each sentence with a verb.
    * On the ribbon, go to the **Design** tab.
    Open Photos.
    For **Alignment**, choose **Left**.

* Capitalize the first word in each step.

* Use a period after each step.
     * **Exception:** When instructing customers to type input that doesn't include end punctuation, don’t use a period. Try to format the text so that the user input appears on a new line.

* Limit a procedure to seven or fewer steps. Try to fit all the steps on the same screen.

## Single-step procedures

If you're using a consistent format for step-by-step instructions, use the same format for single-step instructions, but replace the number with a bullet.

## Tips for writing steps

Make sure the customer knows where the action should take place before you describe the action.

* If the instruction appears in the same UI where the action occurs, it’s usually not necessary to provide location details.

* If you need to make sure the customer begins in the right place, provide a brief phrase at the beginning of the step.
     * For example: On the **Design** tab, select **Header Row**.

* If there’s a chance of confusion, provide an introductory step.
    * For example: On the ribbon, go to the **Design** tab.

## Instructions with right angle brackets

Abbreviate simple sequences by using right angle brackets. Include a space before and after each bracket, and don't make the brackets bold.

* For example: Select **Accounts** > **Other accounts** > **Add an account**.

Screen readers may skip over brackets and read instructions such as **Menu** > **Go To** > **Folders** as *Menu Go To Folders,* which might confuse customers. Check with an accessibility expert before using this approach.

## Developing task information

Before writing procedures, understand your audience and analyze the tasks they need to accomplish. Good task analysis ensures you provide the right level of detail and include all necessary information.

### Perform audience analysis

Identify your readers' skill level, background knowledge, and goals. This determines how much context and explanation to include.

**Questions to answer:**

* What is their experience level with Nordic products?
* What development environment do they use?
* Are they embedded systems experts or new to IoT development?
* What is their primary goal (prototyping, production, learning)?

**Adjust your content accordingly:**

* **For beginners**: Explain concepts, provide context, define terms
* **For experienced developers**: Focus on Nordic-specific details, assume general knowledge
* **For mixed audiences**: Provide links to prerequisite information

### Perform user task analysis

Understand what users actually need to accomplish, not just what the feature can do. This helps you organize procedures around user goals.

**Ask:**

* What is the user trying to achieve?
* What prerequisite knowledge or setup is required?
* What are the critical steps that must succeed?
* Where do users commonly encounter problems?
* What is the expected outcome?

**Example analysis for "Configure BLE advertising":**

* **User goal**: Make device discoverable to BLE central devices
* **Prerequisites**: BLE stack initialized, device configured
* **Critical steps**: Set advertising parameters, load advertising data, start advertising
* **Common issues**: Wrong advertising interval, missing advertising data
* **Expected outcome**: Device appears in BLE scanner applications

### Provide only necessary task information

Include information users need to complete the task, but avoid unnecessary details that add cognitive load.

**Include:**

* Prerequisites and requirements
* Steps to complete the task
* Expected results or success indicators
* Troubleshooting for common problems

**Omit or link to:**

* Background theory (unless essential)
* Alternative methods (unless necessary for context)
* Exhaustive parameter lists (provide examples and link to reference)

**Avoid:**

* "The nRF52840 includes a powerful 64 MHz Arm Cortex-M4 processor with floating point unit, which provides excellent performance for BLE applications. The BLE controller supports all BLE 5.3 features including extended advertising, 2M PHY, and long range. To configure advertising..." [Too much background]

**Use:**

* "To make your nRF52840 device discoverable, configure BLE advertising:

### Including prerequisites

Clearly state what users need before starting. This prevents frustration and wasted time.

#### Introductory paragraphs

Start procedures with a brief introduction that includes prerequisites and context.

**Example:**

"This procedure configures BLE advertising for the nRF52840. Before you begin, ensure that:

* The nRF Connect SDK is installed and configured
* Your application initializes the BLE stack
* You have determined your advertising interval and data

After completing this procedure, your device will be discoverable by BLE central devices."

#### First step as prerequisite

For simple prerequisites, include them as the first step.

**Example:**

1. Ensure the BLE stack is initialized
2. Define your advertising data structure
3. Configure advertising parameters
4. Start advertising

#### Cross-references to basic procedures

For complex prerequisites, link to other procedures rather than repeating them.

**Example:**

"This procedure assumes you have completed [Setting up the nRF Connect SDK](#) and [Initializing the BLE stack](#)."

### Providing examples

Include examples that help users apply the instructions to their specific situation.

#### Practical data

Use realistic values and scenarios from actual Nordic development.

**Avoid generic examples:**

```c
// Configure advertising
config.interval = X;
config.timeout = Y;
```

**Use realistic Nordic examples:**

```c
// Configure advertising for a heart rate sensor
config.interval = BT_GAP_ADV_FAST_INT_MIN_2;  // 100 ms
config.timeout = BT_GAP_ADV_TIMEOUT_LIMITED;   // 180 seconds
```

#### Short examples

Keep examples focused on the concept being explained. Don't include entire applications.

**Too long:**

```c
// 50 lines of complete application code
```

**Right size:**

```c
// Configure advertising parameters
struct bt_le_adv_param adv_param = {
    .id = BT_ID_DEFAULT,
    .options = BT_LE_ADV_OPT_CONNECTABLE,
    .interval_min = BT_GAP_ADV_FAST_INT_MIN_2,
    .interval_max = BT_GAP_ADV_FAST_INT_MAX_2,
};
```

#### Clarifying text

Explain what the example demonstrates and how users can adapt it.

**Example:**

"This example configures fast advertising for a connectable device. For a non-connectable beacon, remove `BT_LE_ADV_OPT_CONNECTABLE` from the options."

## Writing effective procedures

Well-structured procedures guide users through tasks efficiently and reduce the chance of errors.

### Write procedures that are easy to follow

Help users complete tasks successfully by providing clear structure and adequate context.

#### Establish context

Begin each procedure with a brief statement of what the procedure accomplishes and when to use it.

**Example:**

"Use this procedure to configure GPIO pins for input with pull-up resistors. This is typically used for button inputs."

#### Maximum 10 steps per procedure

Keep procedures to 10 steps or fewer. If a task requires more steps, break it into multiple procedures or create a higher-level task that links to sub-procedures.

**If you have more than 10 steps:**

* Break into logical sub-tasks
* Create a main procedure that references sub-procedures
* Use a task map to show the relationship

**Example - Instead of 15 steps:**

Main procedure: "Configuring BLE advertising"
1. Prepare advertising data (links to sub-procedure)
2. Set advertising parameters (links to sub-procedure)
3. Start advertising (2-3 steps)

#### Include prerequisites

State prerequisites clearly at the beginning so users can gather necessary information or complete preparatory steps.

**Example:**

"Before starting this procedure, ensure you have:

* A configured nRF52840 DK with power
* The nRF Connect SDK installed
* Your device's MAC address (found on the board label)"

#### Provide explanatory text

When a step needs clarification, add explanation in a separate paragraph below the step rather than making the step itself longer.

**Avoid:**

1. Configure the `CONFIG_BT_DEVICE_NAME` parameter in `prj.conf` to set your device's Bluetooth name, which will be visible to other devices during scanning and must be 248 characters or less, though shorter names are recommended for better user experience.

**Use:**

1. Set `CONFIG_BT_DEVICE_NAME` in `prj.conf` to configure your device's Bluetooth name.

   The device name appears when central devices scan for BLE peripherals. Use a descriptive name that helps users identify your device. Keep names under 20 characters for compatibility with all platforms.

#### Include all required information

Don't assume users will infer information. State explicitly what they need to do.

**Avoid:**

1. Configure the clock source
2. Set up the advertising parameters
3. Start advertising

**Use:**

1. In `prj.conf`, set `CONFIG_CLOCK_CONTROL_NRF_K32SRC_XTAL` to enable the external 32 kHz crystal
2. In your application code, configure advertising parameters using `bt_le_adv_param`
3. Call `bt_le_adv_start()` to begin advertising

### Place procedures appropriately

Structure your documentation so procedures are easy to find and understand in context.

#### Inside sections, not standalone

Embed procedures within conceptual sections that provide context. Don't create standalone procedure pages without explanation.

**Avoid:**

* Document structure: "configure-gpio.md" (just the procedure)

**Use:**

* Document structure: "gpio-configuration.md" (overview + procedure + examples)

#### First or second level, not third

Place procedure headings at the first or second heading level for visibility. Third-level procedures are harder to find in navigation.

**Avoid:**

```markdown
# GPIO Configuration
## Overview
### Procedure: Configure GPIO Pin
```

**Use:**

```markdown
# GPIO Configuration
## Overview
## Configure a GPIO pin
[procedure steps]
## Advanced GPIO Configuration
[procedure steps]
```

#### Don't nest procedures

Each procedure should be independent. Don't embed one complete procedure inside another.

**Avoid:**

**To configure BLE advertising:**
1. Set advertising parameters
2. Configure advertising data:
   **To configure advertising data:**
   1. Define data structure
   2. Load manufacturer data
   3. Add service UUIDs
3. Start advertising

**Use:**

**To configure BLE advertising:**
1. Set advertising parameters (see [Configure advertising parameters](#))
2. Configure advertising data (see [Configure advertising data](#))
3. Start advertising

### Use procedure headings appropriately

Procedure headings should clearly communicate the task's purpose.

#### "To..." or "How to..." format

Use task-oriented headings that start with "To" or follow a "How to" pattern.

**Use:**

* "To configure GPIO pins for button input"
* "To enable BLE advertising"
* "To flash firmware to the nRF52840 DK"

**Or use action-oriented headings:**

* "Configure GPIO pins for button input"
* "Enable BLE advertising"
* "Flash firmware to the nRF52840 DK"

**Avoid question format:**

* "How do I configure GPIO pins?" (Use statement instead)

#### Succinct but meaningful

Make headings specific enough to distinguish between similar procedures, but concise enough to scan easily.

**Too vague:**

* "Configure the device" (Which device? Configure what?)

**Too detailed:**

* "Configure the nRF52840 GPIO pins P0.13 and P0.14 as inputs with pull-up resistors for button 1 and button 2"

**Right level:**

* "Configure GPIO pins for button inputs"

#### No colon at end

Don't end procedure headings with a colon.

**Avoid:**

* "To configure GPIO pins:"

**Use:**

* "To configure GPIO pins"

#### Indicate method (Command Line, GUI)

When multiple methods exist, indicate the method in the heading.

**Examples:**

* "To build the application (command line)"
* "To build the application (nRF Connect for VS Code)"
* "To flash firmware (nrfjprog)"
* "To flash firmware (Programmer app)"

### Use one method per procedure

Don't mix command-line and GUI steps within a single procedure. Create separate procedures for different methods.

**Avoid:**

**To flash firmware:**
1. Open nRF Connect for Desktop
2. Or, run `nrfjprog --program app.hex`
3. If using the GUI, click Program
4. If using command line, add `--verify`

**Use:**

**To flash firmware (Programmer app):**
1. Open the Programmer app in nRF Connect for Desktop
2. Select your device
3. Add the HEX file
4. Click **Write**

**To flash firmware (command line):**
1. Connect your device
2. Run `nrfjprog --program app.hex --verify`

## Writing effective steps

Individual steps should be clear, concise, and actionable.

### Order and number steps

Present steps in logical sequence and use appropriate numbering.

#### Logical order

Arrange steps in the order users must perform them. Don't make users jump around or backtrack.

**Avoid:**

1. Click **Program**
2. Select your device (do this first)
3. Add the HEX file

**Use:**

1. Select your device
2. Add the HEX file
3. Click **Program**

#### Don't number single-step procedures

If a procedure has only one action, use a bullet point instead of numbering.

**Avoid:**

**To reset the device:**
1. Press the **RESET** button

**Use:**

**To reset the device:**

* Press the **RESET** button

#### Letters for substeps

Use letters (a, b, c) for substeps when a single step contains multiple related actions.

**Example:**

1. Configure the advertising parameters:
   a. Set the advertising interval to 100 ms
   b. Enable the connectable flag
   c. Set the timeout to 180 seconds
2. Start advertising

Use substeps sparingly. If you have many substeps, consider breaking them into separate main steps.

#### (Optional) for optional steps

Mark optional steps clearly with "(Optional)" at the start.

**Example:**

1. Set `CONFIG_BT_DEVICE_NAME` in `prj.conf`
2. (Optional) Set `CONFIG_BT_DEVICE_APPEARANCE` to specify the device type
3. Build the application

### Make each step short (one action)

Each step should contain a single action or closely related group of actions.

#### Maximum 20 words

Keep steps concise. If a step exceeds about 20 words, consider splitting it or moving explanation to a separate paragraph.

**Avoid:**

1. Open the nRF Connect for Desktop application, navigate to the Programmer tool, select your device from the list on the left side, and then click the Add HEX file button to browse for your firmware file.

**Use:**

1. Open the Programmer tool in nRF Connect for Desktop.
2. Select your device from the device list.
3. Click **Add HEX file** and select your firmware file.

#### Explanatory text in separate paragraph

Add explanations, tips, or context in a separate paragraph below the step, not within the step itself.

**Example:**

1. Set `CONFIG_BT_CTLR_TX_PWR_PLUS_8` in `prj.conf` to increase transmission power.

   Higher transmission power increases range but also increases power consumption. Use +8 dBm for maximum range in open space, or use lower power settings for battery-powered devices.

#### Don't bury steps in paragraphs

Extract actions from paragraphs and format them as numbered steps.

**Avoid:**

To flash firmware, first connect your device to your computer using a USB cable. Once connected, open the Programmer application. You should then select your device and add the HEX file containing your firmware.

**Use:**

To flash firmware:
1. Connect your device to your computer using USB.
2. Open the Programmer application.
3. Select your device.
4. Add your HEX file.

### Write steps as complete sentences

Format steps as clear, grammatical sentences.

#### Imperative mood

Start steps with an action verb in imperative mood (command form).

**Use:**

* "Click **Build**"
* "Set CONFIG_BT_DEVICE_NAME"
* "Connect the device"

**Avoid:**

* "You should click **Build**"
* "CONFIG_BT_DEVICE_NAME should be set"
* "The device needs to be connected"

#### Active verb at start

Begin with the action the user performs.

**Use:**

* "Open the terminal"
* "Enter the device name"
* "Select your board"

**Avoid:**

* "The terminal should be opened"
* "Your device name can be entered"
* "The board must be selected"

#### Don't use command names as verbs

Don't turn command or function names into verbs.

**Avoid:**

* "nrfjprog the firmware to your device"
* "Git clone the repository"
* "Build the application using west build"

**Use:**

* "Use nrfjprog to flash firmware to your device"
* "Clone the repository using Git"
* "Build the application by running `west build`"

### Write meaningful steps

Make steps specific and actionable, with appropriate level of detail for the audience and method.

#### GUI: state what to do

For GUI procedures, describe the action and the UI element.

**Use:**

* "Click **File** > **Open**"
* "In the **Configuration** panel, select **Enable BLE**"
* "Clear the **Use default settings** checkbox"

**Provide location context when needed:**

* "In the left sidebar, click **Devices**"
* "From the **Build** menu, select **Clean Build**"

#### Command-line: task focus, then syntax

For command-line procedures, state the task first, then provide the command.

**Avoid:**

1. `west build -b nrf52840dk_nrf52840`
2. `west flash`

**Use:**

1. Build the application for the nRF52840 DK:

   ```bash
   west build -b nrf52840dk_nrf52840
   ```

2. Flash the application to your device:

   ```bash
   west flash
   ```

#### Use branching appropriately

Handle conditional steps clearly.

##### Same procedure, different conditions

When steps vary based on conditions within the same procedure:

**Example:**

3. Configure power mode:
   * If using battery power, set `CONFIG_PM_DEVICE` to enable power management
   * If using USB power, power management is optional

##### Indicate condition in main step

Make the condition clear at the start of the step.

**Example:**

4. If your application uses BLE bonds, set `CONFIG_BT_SETTINGS=y` to enable settings storage.

##### Consider separate procedures for complex branching

If branching becomes complex, create separate procedures.

**Instead of:**

**To build the application:**
1. If you're using nRF52840, run `west build -b nrf52840dk_nrf52840`, but if you're using nRF5340, you'll need to choose between network core and application core...
[continues with increasingly complex branching]

**Use:**

Create separate procedures:

* "To build for the nRF52840 SoC"
* "To build for the nRF5340 application core"
* "To build for the nRF5340 network core"
