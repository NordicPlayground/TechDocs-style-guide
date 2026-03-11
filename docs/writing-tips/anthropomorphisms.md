# Anthropomorphisms

Anthropomorphism is the attribution of human characteristics, emotions, or intentions to non-human entities. In technical writing, this means describing software, hardware, or systems as if they can think, want, feel, or make decisions.

## Why avoid anthropomorphisms

Anthropomorphic language creates several problems in technical documentation:

* **Inaccuracy.** Software doesn't "want" anything. Hardware doesn't "think." Attributing human qualities to technology misrepresents how systems work.
* **Translation problems.** Anthropomorphic expressions are difficult to translate accurately. Many languages don't have equivalent constructions.
* **Ambiguity.** Saying a program "knows" something obscures the actual mechanism (a configuration file, an environment variable, a stored value).
* **Debugging confusion.** When readers troubleshoot, they need precise descriptions of system behavior, not metaphors about intent.

## Common anthropomorphisms to avoid

| Anthropomorphic | Accurate alternative |
| --------------- | -------------------- |
| The application thinks... | The application processes... |
| The system wants you to... | The system requires... |
| The compiler sees the error | The compiler detects the error |
| The device knows the address | The device stores the address |
| The program tries to connect | The program attempts to connect |
| The SDK lets you configure | Use the SDK to configure |
| The debugger finds the bug | The debugger identifies the bug |
| The system refuses the connection | The system rejects the connection |
| Bluetooth tells the device | Bluetooth sends a notification to the device |
| The nRF Connect SDK understands | The nRF Connect SDK supports |

## Types of anthropomorphism

### Attributing intelligence

Don't describe software or hardware as understanding, knowing, remembering, learning, or deciding (unless documenting actual machine learning functionality).

**Avoid:**

* "The bootloader decides which firmware to run"
* "The nRF52840 remembers the bonding information"
* "The stack learns the network topology"

**Use:**

* "The bootloader selects the firmware image based on the validation result"
* "The nRF52840 stores the bonding information in flash memory"
* "The stack builds the network topology from routing messages"

### Attributing desire or intent

Don't describe systems as wanting, needing, trying, or wishing.

**Avoid:**

* "The compiler wants a semicolon at line 42"
* "The protocol needs to establish a connection first"
* "The debugger is trying to find the breakpoint"

**Use:**

* "The compiler expects a semicolon at line 42"
* "A connection must be established before data transfer"
* "The debugger searches for the breakpoint"

### Attributing emotion

Don't describe systems as happy, unhappy, confused, or frustrated.

**Avoid:**

* "The system is confused by the duplicate entry"
* "The build fails because CMake is unhappy with the path"

**Use:**

* "The system cannot process the duplicate entry"
* "The build fails because CMake cannot resolve the path"

### Attributing action with judgment

Don't describe systems as refusing, insisting, complaining, or warning (with implied emotional judgment).

**Avoid:**

* "The firewall refuses to allow the connection"
* "The linter complains about the indentation"

**Use:**

* "The firewall blocks the connection"
* "The linter reports an indentation error"

## When anthropomorphism is acceptable

### User-facing messages that use "we"

Marketing content and some UI messages intentionally use first-person plural. This doesn't apply to technical documentation, but be aware of the distinction.

### Established technical terms

Some anthropomorphic terms have become standard technical terminology. Use them when they are the accepted term in the domain.

**Acceptable established terms:**

* "The process sleeps for 100 ms" (standard OS terminology)
* "The server listens on port 8080" (standard networking terminology)
* "The daemon watches for file changes" (standard systems terminology)
* "The parent thread spawns a child thread" (standard concurrency terminology)
* "The garbage collector reclaims unused memory" (standard memory management term)

When using these terms, no alternative is needed because the anthropomorphic term is the standard.

### Instructional context with "let"

The construction "[tool] lets you [action]" is mildly anthropomorphic but widely accepted in user-facing documentation. Prefer the direct imperative when possible, but "lets you" is acceptable.

**Acceptable:**

"The nRF Connect for VS Code extension lets you build applications, flash devices, and debug firmware."

**Preferred (more direct):**

"Use the nRF Connect for VS Code extension to build applications, flash devices, and debug firmware."

## Guideline

When describing system behavior, ask: "Is this describing what the system *does* or what it *feels*?" Technical documentation should describe observable behavior, mechanisms, and outcomes — not motivations, preferences, or emotions.
