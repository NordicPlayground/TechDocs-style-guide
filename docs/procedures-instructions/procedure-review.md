# Procedure review

Review procedures systematically to ensure accuracy, completeness, and usability. A procedure that contains errors or missing steps wastes readers' time and erodes trust in the documentation.

## Review checklist

### Accuracy

- [ ] Every step produces the described result
- [ ] Commands, file paths, and configuration values are correct
- [ ] Screenshots and illustrations match the current software version
- [ ] Prerequisites are accurate and complete
- [ ] Expected output matches what the reader actually sees

### Completeness

- [ ] All necessary steps are included (no implied or assumed steps)
- [ ] Prerequisites list everything the reader needs before starting
- [ ] The expected result is described so readers can verify success
- [ ] Error conditions are addressed or linked to troubleshooting
- [ ] Platform-specific differences are documented

### Usability

- [ ] Steps are numbered in the correct order
- [ ] Each step describes a single action
- [ ] The procedure has 10 or fewer steps (split if longer)
- [ ] Step text uses imperative mood
- [ ] Technical terms are defined or linked
- [ ] The procedure can be completed by the target audience

### Consistency

- [ ] The formatting follows the style guide conventions
- [ ] Terminology matches the glossary
- [ ] The procedure structure matches similar procedures in the documentation
- [ ] UI element names match the current interface

## Testing procedures

### Walk-through testing

The most effective way to verify a procedure is to perform it yourself, step by step, on a clean system.

**Walk-through guidelines:**

1. Start from the stated prerequisites (don't assume additional setup)
2. Follow each step exactly as written, without filling in gaps from your own knowledge
3. Note where you hesitate, re-read, or need to interpret
4. Record any error messages or unexpected results
5. Verify the final outcome matches the expected result

### Fresh-eyes testing

Have someone unfamiliar with the procedure test it. They will catch assumptions and gaps that the author overlooks.

**Who to involve:**

* A colleague from a different team
* A new team member
* Someone with the same skill level as the target audience

### Environment testing

Test procedures on all supported platforms and configurations:

* Different operating systems (Windows, macOS, Linux)
* Different software versions
* Different hardware configurations (if applicable)
* Both clean installations and existing environments

## Common procedure problems

### Missing steps

Steps that seem obvious to the author but are not obvious to the reader. Look for:

* Navigation steps ("Open the file" — but which file, and where?)
* Selection steps ("Select the device" — but how to identify the right one?)
* Confirmation steps ("Click OK" or "Press Enter" after a configuration change)
* Saving steps ("Save the file" after editing)

### Ambiguous steps

Steps that can be interpreted in multiple ways.

**Ambiguous:**

"Configure the project."

**Clear:**

"Open `prj.conf` and add `CONFIG_BT=y` on a new line."

### Wrong order

Steps that work only when performed in a specific order but are documented in a different order. Test the exact documented sequence.

### Missing context

Lack of information about:

* Why a step is necessary (affects reader confidence)
* What the result of a step should be (affects verification)
* What to do if a step fails (affects error recovery)

### Outdated content

Information that was correct for a previous version but no longer applies. Common sources of outdated content:

* UI changes (buttons moved, renamed, or removed)
* API changes (functions renamed, parameters changed)
* Default values changed
* New prerequisites added

## Review frequency

### When to review

Review procedures when:

* A new software version is released
* The documented tool or product changes
* Readers report problems or confusion
* A related procedure is updated (cascade effects)
* A set review period has elapsed (quarterly or semi-annually)

### Prioritize high-traffic procedures

Focus review efforts on procedures that:

* Are viewed most frequently (check analytics)
* Are part of the getting-started experience
* Have received reader feedback or bug reports
* Involve irreversible actions (flashing, erasing)

## Documentation feedback

### Enable reader feedback

Provide a mechanism for readers to report procedure problems:

* "Was this page helpful?" feedback widget
* Link to file an issue
* Contact information for the documentation team

### Track and act on feedback

Categorize procedure feedback by type:

* **Incorrect step** — Fix immediately
* **Missing step** — Add the step and test the updated procedure
* **Unclear step** — Rewrite for clarity
* **Outdated content** — Update and verify the entire procedure
* **Enhancement request** — Evaluate and prioritize
