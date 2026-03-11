# Error messages

Documenting error messages effectively helps users diagnose problems, find solutions, and return to productive work. Accurate reproduction of error text is critical for searchability.

## Reproducing exact message text

Always reproduce error messages exactly as they appear on screen. Exact text allows users to search for the error and find your documentation.

**Guidelines:**

* Copy the complete error message text, including punctuation and capitalization
* Don't paraphrase or summarize the error message
* Don't correct grammar or spelling in the error message (document it as displayed)
* Include error codes if present

**Example:**

The following error appears when the device cannot establish a BLE connection:

```
ERROR: bt_conn: Failed to establish connection (err -11)
```

If the error text is too long to reproduce inline, use a code block:

```
[00:00:05.123,456] <err> bt_hci_core: opcode 0x2006 status 0x0c
[00:00:05.123,789] <err> bt_conn: Failed to create connection
```

## Formatting guidelines

### Use monospace for error text

Format error messages in monospace (code) font to distinguish them from your documentation text.

**Inline:** If you see the error `CONFIG_BT not set`, enable Bluetooth in your project configuration.

**Block:** For multiline errors, use code blocks:

```
CMake Error at CMakeLists.txt:15:
  The source directory "/app" does not contain a CMakeLists.txt file.
```

### Distinguish error context from error text

Clearly separate the actual error message from your explanatory text.

**Example structure:**

1. Describe when the error occurs
2. Show the exact error text
3. Explain the cause
4. Provide the solution

### Error message tables

For multiple related errors, use a table format:

| Error Message | Cause | Solution |
| ------------- | ----- | -------- |
| `CONFIG_BT not set` | Bluetooth is not enabled in project configuration | Add `CONFIG_BT=y` to `prj.conf` |
| `No boards found` | Device is not connected or not recognized | Check USB connection and install drivers |
| `west: command not found` | west tool is not installed or not in PATH | Install west: `pip install west` |

## Including troubleshooting information

Every documented error should include troubleshooting guidance.

### Describe the cause

Explain why the error occurs in clear, non-technical language when possible.

**Example:**

"This error occurs when the flash memory is write-protected. The bootloader enables write protection after a successful firmware update to prevent accidental modifications."

### Provide solutions

List concrete steps to resolve the error. If multiple solutions exist, order them from most likely to least likely.

**Example:**

**Error:** `west build: FATAL ERROR: board not found: nrf52840dk_nrf52840`

**Cause:** The board identifier does not match any known board in the SDK.

**Solutions:**

1. Verify the board name matches exactly. Run `west boards` to list available boards.
2. Ensure the nRF Connect SDK is installed correctly. Run `west update` to refresh board definitions.
3. Check that your SDK version supports this board. See the [release notes](../releases.md) for supported boards.

### Include prevention tips

When appropriate, explain how to avoid the error in the future.

**Example:**

"To prevent connection timeout errors, ensure the advertising interval is set to 100 ms or less for fast connections. For battery-powered devices, consider using a shorter advertising duration with periodic restarts."

## Explaining error codes

When errors include numeric codes, provide a reference for interpreting them.

### Error code format

Document error codes consistently:

* **Numeric codes:** `Error -11` means "resource temporarily unavailable"
* **Hexadecimal codes:** `0x0C` corresponds to "command disallowed"
* **Named constants:** `NRF_ERROR_NO_MEM` indicates "insufficient memory"

### Error code tables

For APIs or protocols with many error codes, provide a reference table:

| Code | Name | Description |
| ---- | ---- | ----------- |
| 0 | NRF_SUCCESS | Operation completed successfully |
| 4 | NRF_ERROR_NO_MEM | Insufficient memory for the operation |
| 7 | NRF_ERROR_INVALID_PARAM | Invalid parameter supplied |
| 8 | NRF_ERROR_INVALID_STATE | Operation not permitted in current state |
| 12 | NRF_ERROR_TIMEOUT | Operation timed out |

### Link to complete references

For extensive error code lists, link to the API reference rather than duplicating the full list:

"For a complete list of error codes, see the [nrfx error codes reference](../api/errors.md)."

## Writing style for error documentation

### Use neutral language

Don't blame the user for errors. Focus on the situation and the solution.

**Avoid:**

* "You made an error in the configuration"
* "This error is caused by incorrect user input"

**Use:**

* "The configuration contains an invalid value"
* "This error indicates a mismatch between the configuration and the hardware"

### Be specific about actions

Tell users exactly what to do, not just what went wrong.

**Avoid:**

"Fix the configuration and try again."

**Use:**

"Set `CONFIG_HEAP_MEM_POOL_SIZE` to at least 2048 in `prj.conf`, then rebuild the application."

### Group related errors

Organize error documentation by category (build errors, runtime errors, connection errors) or by the stage where they occur (setup, compilation, flashing, runtime).
