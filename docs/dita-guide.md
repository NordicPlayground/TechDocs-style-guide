# DITA-specific guidelines

This page collects DITA-specific authoring details that do not fit cleanly on the general style pages. Use the generic guidance on the related pages first, and use this page only for DITA-specific mechanics, reuse patterns, and publishing constraints.

## When to use this page

Use this page when you are working in a DITA workflow and need guidance that is specific to DITA markup, reuse, or publishing behavior.

For the generic rules, start with these pages:

* [Typographic conventions](typographic-conventions.md)
* [Illustrations](content-structure/illustrations.md)
* [Tables](content-structure/tables.md)
* [Cross-references](content-structure/cross-references.md)
* [Notes, cautions, and warnings](content-structure/notes-cautions-tips.md)
* [Trademarks](trademarks.md)

## Figures and images

In DITA workflows, keep figure markup focused on content rather than layout.

* Create the figure at the correct size before adding it to the source.
* Do not size the image inline in the code.
* Let the publishing pipeline handle figure placement and alignment when that workflow supports it.
* Keep figure titles and alt text in the source.

Use this kind of structure when your DITA workflow expects a figure element:

```xml
<fig>
  <title>Power consumption during Bluetooth LE advertising</title>
  <image href="ble-advertising-power.svg">
    <alt>Power consumption profile during a Bluetooth LE advertising event</alt>
  </image>
</fig>
```

## Tables and footnotes

Use DITA table markup only when you are working in a DITA source set. Keep the general table-writing rules on the [Tables](content-structure/tables.md) page.

Additional DITA-specific points:

* Use the table model required by the documentation set, such as CALS tables.
* Keep notes out of table entries. If the information applies only to the table, use a footnote instead.
* Use numerals for footnotes and reuse the same footnote number when the same explanation applies to multiple cells.
* In workflows that require linked footnotes, use the project-specific `xref` pattern so the footnote appears after the table instead of at the end of the page.

Example pattern:

```xml
<entry>Dynamic (H/L)<sup><xref href="#circuit_config/config_sup_1" format="dita">1</xref></sup></entry>
...
<p><sup id="config_sup_1">1</sup> Input thresholds are level and hold-time controlled.</p>
```

## Cross-references and key-based links

Write cross-references so the sentence still reads well after DITA processing.

* Add explicit link text when the default generated text would make the sentence awkward.
* Include the descriptive noun in the sentence when needed, such as *register*, *signal*, or *chapter*.
* Use `keyref` when a keyed destination gives you a more stable reusable reference.
* Avoid output that adds unnecessary "on page ..." wording when the sentence already identifies the destination clearly.

Examples:

```xml
<p>The register <xref href="power.dita#power/register.MAINREGSTATUS">MAINREGSTATUS</xref> can be used for reading out the current supply voltage mode.</p>
```

```xml
<xref keyref="RADIO.CRCPOLY">CRCPOLY</xref>
```

## Note elements in DITA

Use the same severity meanings as the generic [Notes, cautions, and warnings](content-structure/notes-cautions-tips.md) page.

Approved note types in the Nordic source material are:

* `note`
* `caution`
* `warning`

Keep note tags for content that genuinely needs callout treatment. Do not use them as a visual styling shortcut.

Example:

```xml
<note type="warning">
  Do not exceed the maximum input voltage of 3.6 V on the GPIO pins.
</note>
```

## Trademark reuse in DITA

When a DITA documentation set uses shared trademark definitions, prefer reuse over manual inline markup.

* Pull trademarked names from the shared `keydef` or terminology source when that source exists.
* Use the project mechanism for `conkeyref`-based reuse instead of manually adding the trademarked text each time.
* Keep the first-occurrence trademark treatment aligned with the shared terms definition.

## Legacy workflow notes

Some DITA source sets still depend on project-specific tooling and publishing behavior. Preserve those workflow conventions only when you are maintaining that legacy content.

* Do not copy DITA-only processing assumptions into Markdown guidance.
* Keep publishing-specific details out of generic style pages unless they affect the editorial rule itself.
