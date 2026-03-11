# Task organization

Organize procedural content so that readers can find the right procedure, understand what it accomplishes, and complete it successfully. Good task organization reduces errors and saves readers time.

## Grouping related procedures

### By workflow

Group procedures that belong to the same workflow together, in the order they are typically performed.

**Example (BLE development workflow):**

1. Create a new application
2. Configure BLE settings
3. Implement GATT services
4. Build the application
5. Flash the firmware
6. Test the BLE connection

### By feature area

Group procedures by the feature or subsystem they relate to.

**Example (nRF Connect SDK configuration):**

* Bluetooth configuration
    * Configure advertising
    * Configure scanning
    * Configure connection parameters
* Thread configuration
    * Configure Thread network
    * Configure border router
* Power management
    * Configure sleep modes
    * Configure wake-up sources

### By complexity

Arrange procedures from basic to advanced within each group.

**Example:**

* Basic: Configure a simple BLE beacon
* Intermediate: Create a BLE peripheral with custom GATT services
* Advanced: Implement BLE mesh with relay and proxy features

## Structuring a procedure topic

### Title

Start with an action verb. The title should clearly describe the outcome.

**Good titles:**

* "Configure BLE advertising parameters"
* "Flash firmware using nrfjprog"
* "Set up a Thread border router"

**Avoid:**

* "BLE advertising" (not actionable)
* "Advertising parameter configuration procedure" (verbose)

### Introduction

Provide 1-3 sentences explaining what the procedure accomplishes and when to use it. Don't repeat information from the title.

**Example:**

"Set the advertising interval, TX power, and advertising data to control how your device appears to nearby BLE scanners. Adjust these parameters to balance discoverability and power consumption."

### Prerequisites

List everything the reader needs before starting. Include:

* Required hardware and connections
* Required software versions
* Configuration that must be in place
* Skills or knowledge assumed
* Procedures that must be completed first

**Example:**

"**Before you begin:**

* Connect the nRF52840 DK to your computer via USB.
* Install the nRF Connect SDK v2.5.0 or later.
* Complete [Setting up the development environment](../setup/environment.md)."

### Procedure steps

Write steps in numbered order. See [Step-by-step instructions](step-by-step-instructions.md) for detailed guidance on writing individual steps.

### Expected result

Describe what the reader should observe after completing the procedure. This lets them verify success.

**Example:**

"After flashing, the nRF52840 DK restarts and LED1 begins blinking at 1 Hz. Open a BLE scanner application on your phone to verify the device is advertising with the name you configured."

### Troubleshooting

If the procedure has common failure points, include a troubleshooting section or link to one.

## Handling alternatives

### Multiple methods for the same task

When readers can achieve the same result using different tools or approaches, present each method separately with a clear selector.

**Example using tabs (MkDocs Material):**

```markdown
=== "VS Code"

    1. Click **Terminal** > **Run Build Task**.
    2. Select the board target.
    3. Click **Build**.

=== "Command line"

    Run the following command:

    ```bash
    west build -b nrf52840dk_nrf52840
    ```
```

### Platform-specific procedures

When steps differ by operating system, use tabs or clearly labeled sections.

**Example:**

```markdown
=== "Windows"

    Open a command prompt and run:

    ```
    nrfjprog --program firmware.hex --verify
    ```

=== "macOS / Linux"

    Open a terminal and run:

    ```bash
    nrfjprog --program firmware.hex --verify
    ```
```

## Procedure length guidelines

| Procedure length | Recommendation |
| ---------------- | -------------- |
| 1-2 steps | Include inline in the parent topic |
| 3-10 steps | Standard procedure format |
| 11-15 steps | Consider splitting into two procedures |
| 16+ steps | Split into multiple procedures |

## Connecting procedures to concepts

### Link context to procedures

Before a procedure, link to or briefly summarize the concepts readers need to understand.

**Example:**

"BLE advertising controls how your device appears to scanners. For background on advertising modes and parameters, see [BLE advertising concepts](../concepts/ble-advertising.md).

## Configure advertising parameters

1. Open `prj.conf`..."

### Link procedures to reference material

After a procedure, link to reference material for readers who want more detail.

**Example:**

"For the complete list of advertising configuration options, see the [BLE Kconfig reference](../reference/kconfig-bt.md)."

## Maintaining procedure accuracy

### Test procedures regularly

Run through every procedure periodically to verify accuracy. Code changes, SDK updates, and tool changes can silently invalidate steps.

### Version-specific procedures

When a procedure applies only to specific software versions, state the version requirement clearly.

**Example:**

"These instructions apply to nRF Connect SDK v2.5.0 and later. For earlier versions, see [v2.4.0 setup guide](../archive/setup-v2.4.md)."

### Keep procedures up to date

When the product changes, update the procedure immediately. Outdated procedures that produce errors are worse than no documentation at all.
