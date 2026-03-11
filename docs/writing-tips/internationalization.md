# Internationalization

Write documentation that can be easily translated and understood by a global audience. Nordic products are used worldwide, so content must work across cultures, languages, and locales.

## Writing for translation

### Use simple sentence structure

Translators produce higher-quality translations when source sentences are clear and straightforward.

* Keep sentences under 25 words
* Use subject-verb-object order
* Avoid complex subordinate clause chains
* Use one idea per sentence

### Avoid idioms and colloquialisms

Idiomatic expressions don't translate literally and may be meaningless or offensive in other languages.

**Avoid:**

* "Out of the box" → Use: "by default" or "without additional configuration"
* "Up and running" → Use: "operational" or "running"
* "Boils down to" → Use: "reduces to" or "essentially means"
* "At the end of the day" → Use: "ultimately" or remove entirely
* "Hit the ground running" → Use: "start immediately" or "begin productively"
* "Low-hanging fruit" → Use: "easily achievable improvements"
* "Under the hood" → Use: "internally" or "in the implementation"
* "Gotcha" → Use: "common pitfall" or "known issue"
* "Rule of thumb" → Use: "general guideline"
* "Heads up" → Use: "note" or "important"

### Avoid humor and cultural references

Humor relies on cultural context and rarely translates well. What seems lighthearted in one culture may confuse or offend in another.

* Don't use jokes or puns
* Don't reference pop culture, sports, or holidays
* Don't use culture-specific metaphors
* Don't use sarcasm or irony

### Avoid slang and informal language

Use standard, formal English that translators can work with reliably.

**Avoid:**

* "gonna," "wanna," "kinda"
* "cool," "awesome," "nifty"
* "stuff," "things" (be specific)
* "a bunch of" → Use: "several" or specify the number

### Use consistent terminology

Use the same English term for the same concept throughout your documentation. Varying terminology creates confusion and inconsistency in translations.

**Inconsistent (creates translation problems):**

"Start the application. Launch the program. Run the software."

**Consistent:**

"Start the application. Start the application on the second device."

When a term has been defined in the [Glossary](../glossary.md), use that term consistently.

## Locale-sensitive content

### Date and time formats

Date formats vary by region. Use unambiguous formats or follow ISO 8601.

**Ambiguous:**

"02/04/26" (February 4 or April 2?)

**Unambiguous:**

"2026-02-04" (ISO 8601)
"February 4, 2026" (written out)

### Number formats

Decimal separators and thousands separators vary by locale.

**Locale-dependent:**

* "1,000.50" (US/UK)
* "1.000,50" (Germany, Brazil)
* "1 000,50" (France, Sweden)

**In documentation:** Use the format standard for your primary audience and note the convention if there is potential for confusion. In code examples, always use the period as the decimal separator.

### Units of measurement

Use SI (metric) units as the primary measurement system. Include imperial equivalents in parentheses only when the audience expects them.

**Example:**

"The antenna is 30 mm long."

Not: "The antenna is 1.18 inches long."

For temperature, use Celsius in technical specifications:

"Operating temperature range: -40 °C to 85 °C"

### Currency

Avoid currency references in technical documentation. When necessary, use ISO 4217 currency codes.

**Example:**

"The development kit costs approximately 45 USD."

Not: "The development kit costs about $45."

### Address and phone formats

Don't assume a specific address or phone number format. If you must reference contact information, use a format appropriate for the region.

## Writing for non-native English speakers

Much of Nordic's documentation audience reads English as a second language. Write with these readers in mind.

### Use standard vocabulary

Prefer common English words over rare or literary alternatives.

| Complex word | Simpler alternative |
| ------------ | ------------------- |
| Utilize | Use |
| Commence | Start, begin |
| Terminate | End, stop |
| Facilitate | Help, enable |
| Subsequently | Then, after |
| Aforementioned | Previous, earlier |
| Notwithstanding | Despite, even though |

### Avoid phrasal verbs when possible

Phrasal verbs (verb + particle combinations) are difficult for non-native speakers. See [Phrasal verbs](../grammar/verbs.md#phrasal-verbs) for details.

| Phrasal verb | Alternative |
| ------------ | ----------- |
| Set up | Configure, install |
| Turn on | Enable, activate |
| Figure out | Determine |
| Come up with | Create, develop |
| Run into | Encounter |

### Avoid ambiguous pronouns

Pronouns like "it," "this," "that," and "they" can be ambiguous, especially for readers parsing complex sentences in a second language.

**Ambiguous:**

"Configure the device tree and the Kconfig file. It determines the hardware layout."
(Does "it" refer to the device tree or the Kconfig file?)

**Clear:**

"Configure the device tree and the Kconfig file. The device tree determines the hardware layout."

### Avoid negative constructions

Positive statements are easier to translate and understand than negative ones. Double negatives are especially problematic.

**Negative:**

"The operation does not fail unless the buffer is not allocated."

**Positive:**

"The operation succeeds when the buffer is allocated."

## Cultural considerations

### Avoid stereotypes and assumptions

Don't assume knowledge of specific cultural practices, holidays, educational systems, or social norms.

### Use inclusive examples

When examples include names, locations, or scenarios, use a variety that reflects a global audience.

**Example names:** Use names from diverse cultures. Avoid using only English-language names.

**Example locations:** Vary locations rather than defaulting to US or European cities.

### Avoid directional and color symbolism

Directional references (left-right, top-bottom) can have different cultural associations. Color symbolism varies widely across cultures (red means danger in some cultures, good fortune in others).

In technical documentation, use color only to enhance meaning that is already communicated through text or symbols.

## Preparing content for localization

### Separate text from images

Embed translatable text in the documentation source, not in images. Text embedded in images requires creating new images for each language.

### Allow for text expansion

Translated text is often 20-30% longer than English. Design layouts and UI strings with expansion in mind.

### Use translatable string formats

In code examples that include user-facing strings:

```c
LOG_INF("Connection established");
```

Comment strings that require translation:

```c
/* Translatable: displayed to user */
const char *msg = "Device ready";
```

### Provide context for translators

When a term has multiple meanings, add context to help translators choose the correct translation. For example, "port" can mean a network port, a hardware port, or porting software.
