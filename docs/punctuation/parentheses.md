# Parentheses

Parenthetical insertions create side channels within sentences. Readers must track both the main flow and the detour simultaneously. Use parentheses only when this dual-processing burden serves clarity.

## Evaluating parenthetical necessity

Apply this assessment when editing content in parentheses:

**Reading flow test**: Cover the parenthetical portion with your hand. Does the remaining sentence:
* Still make complete sense? → The parentheses may be appropriate
* Leave gaps or raise questions? → Integrate the content into main sentence structure
* Work better without the extra information? → Delete the parenthetical content

Parenthetical content should enhance understanding, not complete it.

## Technical documentation contexts

### Introducing shortened forms alongside full terms

When space permits, present both the complete technical name and its shortened form together:

* "Authenticated Encryption with Associated Data (AEAD) protects message integrity."
* "The System on Chip (SoC) integrates multiple functions."

Subsequent references use only the shortened form. Omit this pairing in space-constrained headings. Choose one form only.

### Cross-system measurement notation

When documenting physical specifications for international audiences, parentheses contain the secondary measurement system:

* "Spacing: 2.54 mm (0.1 in)" for metric-primary contexts
* "Length: 4 inches (101.6 mm)" for imperial-primary contexts

Establish this relationship once per specification type rather than repeating throughout.

### Embedded lists within flowing text

Letter or number markers within parentheses organize multiple items inside a sentence:

* "Initialization requires three steps: (1) power stabilization, (2) clock configuration, (3) peripheral enumeration."

Prefer separate list formatting when items exceed simple phrases.

### Reference and citation markers

Parentheses mark supplementary references without interrupting explanation:

* "The nRF9160 supports LTE-M Category M1. (Refer to 3GPP Release 13 for protocol details.)"

When the reference constitutes a complete sentence, punctuation stays inside the final parenthesis.

## Usage patterns that compromise clarity

### Ambiguity markers

Technical writing demands precision. Never use parentheses to hedge between singular and plural:

* **Ambiguous**: "Update the register(s) before proceeding"
* **Precise**: "Update all relevant registers before proceeding"
* **Alternative**: "Update the register before proceeding" (when always singular)

Choose specificity over vagueness.

### Programming interface notation

When discussing code elements generically, omit signature indicators:

* **Generic reference**: "The configure method sets device parameters"
* **Specific signature**: "The configure(uint8_t mode, uint16_t timeout) variant handles timeout specifications"

Empty signature markers imply a parameter-free form—use them only when documenting that specific implementation.

### Stacked parenthetical insertions

Multiple parenthetical statements in one paragraph fragment the information architecture:

* **Fragmented**: "The peripheral (configured via registers) communicates with the sensor (an external I2C device) during active mode (when not in sleep state)."

Break into discrete sentences or consolidate definitions into a glossary.

## Structural integration principles

When parenthetical content grows beyond a brief phrase:

1. **Convert to separate sentences** - Full explanations deserve full sentence status
2. **Move to notes or callouts** - Substantial tangents fit better in dedicated sections
3. **Reference glossary entries** - Repeated definitions belong in centralized glossaries
4. **Create cross-references** - Detailed specifications should live in dedicated reference sections

Parentheses work optimally for content that readers can productively skip without losing thread continuity.

