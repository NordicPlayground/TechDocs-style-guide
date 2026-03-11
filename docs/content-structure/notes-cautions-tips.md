# Notes, cautions, and warnings

Admonitions (also called callouts) highlight information that readers need to notice. Use them to draw attention to important details, potential problems, or safety hazards without interrupting the flow of the main text.

Nordic follows the ANSI/ISO standard for admonition severity levels. Use "Caution" instead of "Attention."

## Types of admonitions

### Note

Essential information in a neutral tone. Notes provide additional information that is relevant but not critical to the main text. They clarify, expand, or add context.

**Use a note when:**

* The information supplements the main text.
* Readers benefit from knowing this, but can proceed without it.
* The detail applies to specific configurations or scenarios.

**Example syntax:**

```rST
.. note::
   The nRF52840 DK has two MCU reset buttons.
   The **RESET** button resets the nRF52840 SoC, while the **IF BOOT/RESET** button resets the interface MCU.
```

```markdown
!!! note
    The nRF52840 DK has two MCU reset buttons. The **RESET** button resets the nRF52840 SoC, while the **IF BOOT/RESET** button resets the interface MCU.
```

### Caution

Risk of damage to data, hardware, software, or a broken procedure. Cautions alert readers to potential problems that could cause data loss, system damage, or procedure failure.

**Use a caution when:**

* An action could cause data loss.
* A configuration could damage hardware or software.
* Incorrect steps could make the system unstable or break a procedure.
* An irreversible action is described.

**Example syntax:**

```rST
.. caution::
   Erasing the flash memory removes all stored data, including bonding information and application data.
   This action cannot be undone.
```

```markdown
!!! caution
    Erasing the flash memory removes all stored data, including bonding information and application data. This action cannot be undone.
```

### Warning

Risk of personal injury or loss of life. Warnings are the highest severity admonition and must be used only for genuine safety hazards.

**Use a warning when:**

* An action could cause physical harm.
* Incorrect voltage or connections could injure a person.
* Physical safety is a concern.

**Example syntax:**

```rST
.. warning::
   Do not exceed the maximum input voltage of 3.6 V on the GPIO pins.
   Exceeding this voltage can damage equipment and pose a safety risk.
```

```markdown
!!! warning
    Do not exceed the maximum input voltage of 3.6 V on the GPIO pins. Exceeding this voltage can damage equipment and pose a safety risk.
```


## Choosing the right admonition

| Severity | Type | ANSI/ISO standard | Consequence of ignoring |
| -------- | ---- | ----------------- | ----------------------- |
| Low | Note | -- | Incomplete understanding |
| High | Caution | ANSI/ISO | Data loss, hardware/software damage, broken procedure |
| Highest | Warning | ANSI/ISO | Personal injury or loss of life |

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

```
!!! warning
    Erasing the device removes all stored data.

1. Connect the device via USB.
2. Run `nrfjprog --eraseall`.
```

**Incorrect placement:**

```
1. Connect the device via USB.
2. Run `nrfjprog --eraseall`.

!!! warning
    Erasing the device removes all stored data.
```

### Don't place admonitions inside procedures

Don't insert admonitions between steps in a numbered procedure. They break the visual flow and can confuse readers about which step the admonition relates to.

**Avoid:**

```
1. Open the project.
2. Edit `prj.conf`.

    !!! note
        The file may not exist yet.

3. Build the application.
```

**Preferred:**

Put the note content within the step text:

```
1. Open the project.
2. Edit `prj.conf`. If the file does not exist, create it in the application root directory.
3. Build the application.
```

Or place the note before the procedure if it applies broadly.

### Don't stack admonitions

Avoid placing multiple admonitions in sequence. Multiple consecutive callouts create visual noise and reduce the impact of each one.

**Avoid:**

```markdown
!!! note
    Note content here.

!!! warning
    Warning content here.
```

**Better:** Combine related information into a single admonition, or integrate the less critical items into the main text.

## Notes vs footnotes

Notes and footnotes serve different purposes. Do not use them interchangeably.

### Notes

Notes appear in the body text as admonitions. They provide supplementary information related to the surrounding content.

**Use notes in:** Body text, procedures, concept topics.

### Footnotes

Footnotes provide clarifications for content within tables. Notes do not belong inside table cells; use footnotes instead.

**Footnote rules:**

* Use footnotes only in tables.
* Use numerals (1, 2, 3), not symbols (*, †, ‡).
* Place the footnote numeral as a superscript in the table cell.
* List footnotes below the table in numerical order.
* Reuse the same footnote number when the same clarification applies to multiple cells.

**Example:**

| Pin | Function | Voltage |
| --- | -------- | ------- |
| P0.13 | LED1 | 3.0 V |
| P0.14 | LED2 | 3.0 V |
| P0.26 | SDA¹ | 1.8 V² |
| P0.27 | SCL¹ | 1.8 V² |

¹ I2C interface pins. Configure pull-up resistors externally.
² Directly connected to the nRF52840 1.8 V rail. Do not apply 3.3 V.

## Avoid overuse

Overusing admonitions diminishes their effectiveness. If every paragraph has an admonition, readers start ignoring them.

**Guidelines:**

* Limit admonitions to 1-2 per page section.
* Reserve cautions and warnings for genuinely hazardous situations.
* If most content would be in admonitions, restructure the topic instead.
* Ask: "Does this information truly need to stand out, or can it be in the main text?".
