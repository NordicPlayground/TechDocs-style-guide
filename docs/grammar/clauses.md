# Clauses

Understanding the difference between restrictive and nonrestrictive clauses helps you write clear, unambiguous sentences and use punctuation correctly.

## Restrictive clauses

A restrictive clause (also called an essential or defining clause) provides information that is necessary to identify the noun it modifies. Without the clause, the meaning of the sentence changes.

**Characteristics:**

* Introduced by "that" (preferred in American English)
* No commas before or after the clause
* Removing the clause changes which item is being discussed

**Examples:**

"The configuration option **that controls advertising interval** is `CONFIG_BT_ADV_INT`."

(Identifies *which* configuration option. Without the clause, the reader doesn't know which option is meant.)

"Devices **that support Bluetooth 5.3** can use coded PHY."

(Restricts "devices" to only those supporting Bluetooth 5.3. Without the clause, the sentence would apply to all devices.)

"The function **that initializes the BLE stack** must be called before advertising starts."

(Identifies which specific function.)

## Nonrestrictive clauses

A nonrestrictive clause (also called a nonessential or non-defining clause) adds extra information about a noun that is already clearly identified. The clause can be removed without changing the core meaning.

**Characteristics:**

* Introduced by "which"
* Set off by commas
* Removing the clause doesn't change which item is being discussed

**Examples:**

"The nRF52840 DK, **which includes an onboard debugger**, supports all nRF Connect SDK samples."

(The nRF52840 DK is already identified. The clause adds extra information.)

"`CONFIG_BT_ADV_INT`, **which defaults to 100 ms**, controls the advertising interval."

(The configuration option is already identified by name. The clause provides supplementary detail.)

"The SoftDevice Controller, **which is Nordic's BLE link layer implementation**, handles time-critical radio operations."

(The SoftDevice Controller is already a specific item. The clause defines it for readers who may not be familiar with it.)

## "That" vs "which" — a quick guide

| | Restrictive | Nonrestrictive |
|---|---|---|
| **Relative pronoun** | that | which |
| **Commas** | No commas | Commas required |
| **Purpose** | Identifies which one | Adds extra information |
| **Can be removed?** | No (meaning changes) | Yes (meaning preserved) |

### Test: Can you remove the clause?

If you can remove the clause and the sentence still makes sense (still identifies the correct noun), the clause is nonrestrictive. Use "which" and commas.

If removing the clause makes the sentence vague or changes its meaning, the clause is restrictive. Use "that" and no commas.

**Test example:**

"The samples that use BLE are in the `bluetooth` folder."

Remove the clause: "The samples are in the `bluetooth` folder." — This changes the meaning (not *all* samples are in that folder). The clause is **restrictive**. Use "that," no commas. Correct as written.

"The `bluetooth` folder, which contains all BLE samples, is in the SDK root."

Remove the clause: "The `bluetooth` folder is in the SDK root." — Still makes sense and identifies the same folder. The clause is **nonrestrictive**. Use "which" with commas. Correct as written.

## Common errors

### Using "which" without commas for restrictive clauses

**Incorrect:**

"The devices which support Thread can form a mesh network."

**Correct (restrictive):**

"The devices that support Thread can form a mesh network."

**Correct (nonrestrictive, if all devices support Thread):**

"The devices, which support Thread, can form a mesh network."

### Using "that" for nonrestrictive clauses

**Incorrect:**

"The nRF52840 DK, that includes an onboard debugger, supports all samples."

**Correct:**

"The nRF52840 DK, which includes an onboard debugger, supports all samples."

### Missing commas around nonrestrictive clauses

**Incorrect:**

"The nRF Connect SDK which is free to download includes BLE libraries."

**Correct:**

"The nRF Connect SDK, which is free to download, includes BLE libraries."

## Relative clauses with "who" and "whom"

For clauses referring to people, use "who" (subject) or "whom" (object).

**Restrictive:**

"Developers who work with BLE should review the advertising guide."

(Identifies which developers.)

**Nonrestrictive:**

"Nordic engineers, who developed the SoftDevice Controller, optimized it for low power consumption."

(Adds information about already-identified people.)

## Placement of relative clauses

Place the relative clause immediately after the noun it modifies. Separating them creates ambiguity.

**Ambiguous:**

"The developer configured the device that crashed using the debugger."

(Did the device crash, or did the debugger crash?)

**Clear:**

"The developer used the debugger to configure the device that crashed."

**Or:**

"Using the debugger, the developer configured the device that crashed."

## Simplifying complex clauses

When a relative clause makes a sentence too long or complex, consider:

* Splitting into two sentences
* Using a participial phrase
* Restructuring the sentence

**Complex:**

"The `bt_le_adv_start()` function, which accepts a pointer to a `bt_le_adv_param` structure that contains the advertising interval, TX power, and other parameters, returns zero on success."

**Simplified:**

"The `bt_le_adv_start()` function accepts a pointer to a `bt_le_adv_param` structure and returns zero on success. The structure contains the advertising interval, TX power, and other parameters."
