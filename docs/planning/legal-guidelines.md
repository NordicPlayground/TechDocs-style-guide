# Legal guidelines

Technical documentation must comply with legal requirements regarding copyright, confidential information, and intellectual property. Follow these guidelines to protect Nordic Semiconductor, its partners, and its customers.

## Copyright

### What copyright protects

Copyright protects the expression of ideas, not the ideas themselves. In documentation, this means:

* **Protected:** Specific wording, sentence structure, organization, and presentation of content
* **Not protected:** Facts, concepts, procedures, and technical specifications (though their specific expression is protected)

### Using copyrighted material

Do not copy text, images, diagrams, or code from copyrighted sources without permission.

**Guidelines:**

* Do not reproduce text from third-party documentation, books, or websites
* Do not copy images or diagrams from external sources
* Do not include substantial portions of third-party code examples without a compatible license
* Always write original content that explains concepts in your own words

### When you can reference copyrighted material

You may:

* Link to third-party content instead of reproducing it
* Briefly summarize publicly available information in your own words
* Quote short passages with proper attribution (fair use)
* Reference standard specifications by name and section number

### Copyright notices

Include copyright notices as required by your organization's policy. Typically, documentation includes a copyright notice in the footer or on the title page:

"Copyright (c) 2026 Nordic Semiconductor ASA. All rights reserved."

## Confidential information

### What is confidential

Confidential information includes:

* Unreleased product specifications
* Internal roadmaps and plans
* Customer-specific information
* Internal tools and processes not intended for public disclosure
* Security-sensitive implementation details
* Pre-release API changes

### Preventing accidental disclosure

Before publishing any documentation:

* Verify that all technical details have been cleared for public disclosure
* Remove internal comments, notes, and TODO items
* Check that code examples don't contain internal paths, server names, or credentials
* Ensure screenshots don't show confidential information in title bars, file paths, or background windows
* Review API references to ensure only public APIs are documented

### Classification guidelines

Follow your organization's information classification policy. Common levels include:

* **Public:** Available to anyone (published documentation, public APIs)
* **Internal:** Available within the organization only
* **Confidential:** Restricted to specific teams or individuals
* **Strictly confidential:** Highly sensitive, limited distribution

When in doubt about whether information is public, treat it as confidential and verify before publishing.

## Third-party content

### Open-source licenses

When documenting open-source components (such as Zephyr RTOS), comply with the license terms:

* Acknowledge the project and its license
* Don't claim open-source code as proprietary
* Include required license notices in documentation that reproduces open-source code
* Follow contribution guidelines when contributing documentation upstream

### Standards and specifications

When referencing industry standards (Bluetooth, Thread, Matter, Zigbee):

* Reference the standard by name and version
* Don't reproduce substantial portions of the specification
* Link to the official specification when possible
* Note when Nordic's implementation differs from or extends the standard

### Partner and vendor content

When documenting third-party tools, libraries, or hardware:

* Verify you have permission to include specific details
* Use proper trademark attributions (see [Trademarks](../trademarks.md))
* Link to official documentation rather than reproducing it
* Keep third-party information up to date

## Code examples in documentation

### Original code

Code examples you write for documentation are typically covered by the documentation's license. Ensure they follow your organization's licensing policy.

### Third-party code

When including code from external sources:

* Verify the license permits reproduction
* Include the required attribution or license notice
* Note the source in a comment or accompanying text
* Minimize the amount of third-party code included

### Customer code

Never include actual customer code in public documentation, even anonymized. Create original examples that demonstrate the same concepts.

## Screenshots and images

### Screenshots of your own products

Screenshots of Nordic tools and products are generally safe to include. Check that:

* The screenshot doesn't show unreleased features
* No confidential data appears in the screenshot
* The UI version matches the documented software version

### Screenshots of third-party products

Before including screenshots of third-party products:

* Check the product's documentation and terms of use
* Some products explicitly permit screenshots for documentation
* When in doubt, describe the UI in text instead of using screenshots
* Always use current, accurate screenshots (not mockups)

### Stock images and icons

Use only properly licensed images. Verify that:

* The license permits commercial use
* Attribution requirements are met
* The license covers your distribution channels

## Disclaimer requirements

### External links

When linking to external websites, consider including a disclaimer that Nordic doesn't control and isn't responsible for external content.

See [URLs and web addresses](../urls-web-addresses.md) for detailed guidance on linking to external content.

### Accuracy and completeness

Documentation typically includes a disclaimer regarding accuracy. Your organization's legal team defines the specific language.

### Limitation of liability

Technical documentation should not make guarantees about product performance that exceed the product's official specifications. Use precise language:

**Avoid:**

"The nRF52840 guarantees a range of 200 meters."

**Use:**

"The nRF52840 supports a range of up to 200 meters in open-air conditions, depending on antenna design and environmental factors."

## Review process

### Legal review triggers

Request legal review when documentation:

* Includes third-party content or substantial references
* Describes patented technologies
* Makes performance claims
* Includes open-source license information
* Discusses security features or certifications
* Contains customer case studies or testimonials

### Pre-publication checklist

Before publishing, verify:

- [ ] No confidential information is disclosed
- [ ] Copyright notices are present and current
- [ ] Third-party trademarks are used correctly
- [ ] External links include appropriate disclaimers
- [ ] Code examples are original or properly licensed
- [ ] Screenshots don't contain sensitive information
- [ ] Performance claims match official specifications
