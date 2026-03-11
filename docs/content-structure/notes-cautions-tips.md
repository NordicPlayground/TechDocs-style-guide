# Notes, cautions, and tips

Admonitions (also called callouts) highlight information that readers need to notice. Use them to draw attention to important details, potential problems, or helpful suggestions without interrupting the flow of the main text.

## Types of admonitions

### Note

Notes provide additional information that is relevant but not essential to the main text. They clarify, expand, or add context.

**Use a note when:**

* The information supplements the main text
* Readers benefit from knowing this, but can proceed without it
* The detail applies to specific configurations or scenarios

**MkDocs syntax:**

```markdown
!!! note
    The nRF52840 DK has two MCU reset buttons. The **RESET** button resets the nRF52840 SoC, while the **IF BOOT/RESET** button resets the interface MCU.
```

### Tip

Tips provide helpful suggestions, best practices, or shortcuts. They improve the reader's experience but are not required for success.

**Use a tip when:**

* You want to suggest a more efficient approach
* There's a shortcut or time-saving technique
* The information improves the reader's workflow

**MkDocs syntax:**

```markdown
!!! tip
    Use `west build --pristine` to perform a clean build when switching between board targets. This prevents build errors caused by cached files from the previous target.
```

### Important

Important admonitions highlight information that affects the outcome of a task or the behavior of a system. Readers need this information to succeed.

**Use important when:**

* The information affects the result of a procedure
* Missing this detail causes incorrect behavior (but not damage)
* A prerequisite or requirement applies

**MkDocs syntax:**

```markdown
!!! important
    Enable `CONFIG_BT` in `prj.conf` before building any BLE application. Without this option, BLE functionality is not included in the build.
```

### Warning

Warnings alert readers to potential problems that could cause data loss, system instability, or security vulnerabilities. Readers must read warnings before proceeding.

**Use a warning when:**

* An action could cause data loss
* A configuration could create a security vulnerability
* Incorrect steps could make the system unstable
* An irreversible action is described

**MkDocs syntax:**

```markdown
!!! warning
    Erasing the flash memory removes all stored data, including bonding information and application data. This action cannot be undone.
```

### Caution (Danger)

Cautions alert readers to conditions that could cause hardware damage, personal injury, or permanent equipment failure.

**Use a caution when:**

* An action could damage hardware
* Incorrect voltage or connections could cause harm
* Physical safety is a concern

**MkDocs syntax:**

```markdown
!!! danger
    Do not exceed the maximum input voltage of 3.6 V on the GPIO pins. Exceeding this voltage permanently damages the nRF52840 SoC.
```

## Choosing the right admonition

| Severity | Type | Consequence of ignoring |
| -------- | ---- | ----------------------- |
| Lowest | Tip | Missed optimization or shortcut |
| Low | Note | Incomplete understanding |
| Medium | Important | Incorrect result or unexpected behavior |
| High | Warning | Data loss, instability, or security issue |
| Highest | Caution / Danger | Hardware damage or personal injury |

## Writing effective admonitions

### Keep admonitions concise

Admonitions lose their impact when they are too long. Aim for 1-3 sentences. If you need more space, the content may belong in the main text.

**Too long:**

An admonition with an entire paragraph of background, multiple code examples, and a list of steps. Move this to the main text.

**Right length:**

```markdown
!!! warning
    Back up your configuration before running `west update`. The update process may overwrite local modifications to SDK files.
```

### Describe the consequence

Tell readers what happens if they ignore the admonition. This helps them assess the urgency.

**Without consequence (less effective):**

```markdown
!!! warning
    Set `CONFIG_HEAP_MEM_POOL_SIZE` to at least 2048.
```

**With consequence (more effective):**

```markdown
!!! warning
    Set `CONFIG_HEAP_MEM_POOL_SIZE` to at least 2048. A smaller heap causes runtime memory allocation failures that result in BLE connection drops.
```

### Use the imperative mood

Start admonition text with a direct instruction or clear statement.

**Imperative (direct):**

"Back up your data before proceeding."

**Declarative (less direct):**

"It is recommended that you back up your data before proceeding."

## Placement rules

### Place admonitions before the related action

Put warnings and cautions *before* the step they relate to, not after. Readers need to see the warning before they perform the action.

**Correct placement:**

"!!! warning
    Erasing the device removes all stored data.

1. Connect the device via USB.
2. Run `nrfjprog --eraseall`."

**Incorrect placement:**

"1. Connect the device via USB.
2. Run `nrfjprog --eraseall`.

!!! warning
    Erasing the device removes all stored data."

### Don't place admonitions inside procedures

Don't insert admonitions between steps in a numbered procedure. They break the visual flow and can confuse readers about which step the admonition relates to.

**Avoid:**

"1. Open the project.
2. Edit `prj.conf`.

    !!! note
        The file may not exist yet.

3. Build the application."

**Preferred:**

Put the note content within the step text:

"1. Open the project.
2. Edit `prj.conf`. If the file does not exist, create it in the application root directory.
3. Build the application."

Or place the note before the procedure if it applies broadly.

### Don't stack admonitions

Avoid placing multiple admonitions in sequence. Multiple consecutive callouts create visual noise and reduce the impact of each one.

**Avoid:**

```markdown
!!! note
    Note content here.

!!! tip
    Tip content here.

!!! warning
    Warning content here.
```

**Better:** Combine related information into a single admonition, or integrate the less critical items into the main text.

## Avoid overuse

Overusing admonitions diminishes their effectiveness. If every paragraph has an admonition, readers start ignoring them.

**Guidelines:**

* Limit admonitions to 1-2 per page section
* Reserve warnings and cautions for genuinely dangerous situations
* If most content would be in admonitions, restructure the topic instead
* Ask: "Does this information truly need to stand out, or can it be in the main text?"
