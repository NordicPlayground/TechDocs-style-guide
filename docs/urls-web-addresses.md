# URLs and web addresses

In content for a general audience, use *address* rather than *URL*. In content for a technical audience, don't spell out *URL* on first mention. If you have a reason to spell out URL, use *uniform* *resource locator*.

Use *a,* not *an,* as an article preceding *URL*.

## References to specific sites and domains

Don't include *https://* in a URL. Include the protocol only if it's something other than HTTP, such as File Transfer Protocol (FTP).

* For example: www.nordicsemi.com/products
* For example: ftp://example.com/downloads/myfile.txt

The trailing slash at the end of a URL is optional. In most cases, leave it off. Never use a trailing slash in a URL that ends with a file name.

Most of the time, use lowercase for URLs, email addresses, and newsgroup addresses.

To refer to an entire website or top-level domain, such as Nordicsei.com, omit *http://www* from the URL and capitalize only the first letter of the URL, even if the site name is capitalized differently.

## Grammar and formatting

Use *of* (not *for*) to describe the relationship of the word *URL* to a resource. Use the preposition *at* with the location of a specific address.

* For example: Search results include the URL of the page.
* For example: Learn more about Microsoft products and services at [www.nordicsemi.com](https://www.nordicsemi.com/).

If the reader might think the period at the end of a sentence is part of the URL, rewrite the sentence or set the URL off.

* For example: Go to [nordicsemi.com/products](https://nordicsemi.com/products) to learn more about our product offerings.

Write brief but meaningful link text, using the title or a description of a page rather than a generic phrase like *click here*. In alt text for a graphic that links to another location, state clearly that the graphic is a link.

* For example: (Alt text) Picture of a circuit board with PIN01 circled in red.

## Referencing external websites

When linking to external websites, follow these guidelines to ensure links remain useful and appropriate.

### Determining which site to reference

Link to external sites that provide value to your readers, but consider these factors:

**Link to external sites when:**

* The site provides official specifications or standards (for example, Bluetooth SIG, IEEE)
* The content is maintained by a reputable organization
* The information significantly enhances understanding
* The site is likely to remain stable and accessible
* The content is not easily replicated or summarized in your documentation

**Avoid linking to external sites when:**

* The content frequently changes or may become unavailable
* You can include the essential information directly in your documentation
* The site requires registration or payment to access
* The site's reliability or authority is questionable
* The content is primarily promotional

**Examples of appropriate external links:**

* Official specifications: "See the [Bluetooth Core Specification](https://www.bluetooth.com/specifications/specs/) for detailed protocol information"
* Standards bodies: "The [Internet Engineering Task Force (IETF)](https://www.ietf.org/) maintains the CoAP specification"
* Manufacturer documentation: "Refer to [Arm's Cortex-M4 Technical Reference Manual](https://developer.arm.com/documentation/) for processor details"

### Determining which URL to use

Choose the most stable and appropriate URL for external references.

**Prefer stable URLs:**

* Link to main topic pages rather than deep navigation paths
* Use permalinks when available
* Choose versioned documentation URLs when referencing specific versions
* Avoid URLs with session IDs, tracking parameters, or temporary tokens

**Examples:**

**Avoid:**

* `https://example.com/docs/en-us/v2.5/temp/getting-started?sessionid=abc123`

**Use:**

* `https://example.com/docs/getting-started` (stable page)
* `https://example.com/docs/v2.5/getting-started` (versioned, if needed)

**For Nordic-specific examples:**

* Link to `https://www.nordicsemi.com/Products` rather than deep product pages that may reorganize
* Use `https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/` for current SDK docs
* Use specific version URLs like `https://developer.nordicsemi.com/nRF_Connect_SDK/doc/2.5.0/` when referencing version-specific information

### Adding disclaimers

Include disclaimers for external links to manage user expectations and legal considerations.

**Standard disclaimer format:**

Include a general disclaimer in your site footer or in a dedicated section:

"This documentation may contain links to third-party websites. Nordic Semiconductor ASA is not responsible for the content of external sites. External links are provided for convenience only."

**Inline disclaimers for specific contexts:**

When linking to particularly important or sensitive external resources, include inline notes:

**Example:**

"The Bluetooth SIG maintains the official [Bluetooth Core Specification](https://www.bluetooth.com/specifications/specs/). Nordic Semiconductor is not responsible for content on external websites."

**When to use inline disclaimers:**

* Links to commercial sites or products
* Links that might become outdated
* Links to third-party tools or software
* Links to community-maintained resources

### Preventing unapproved references

Control which external sites appear in your documentation to maintain quality and avoid inappropriate associations.

**Establish approval processes:**

* Create a list of pre-approved external reference sites
* Require review for new external links
* Periodically audit external links for appropriateness and availability

**Pre-approved categories:**

* Official standards organizations (Bluetooth SIG, IEEE, IETF)
* Component manufacturer documentation (Arm, specific IC vendors)
* Open-source project official sites (Zephyr, Linux Foundation projects)
* Nordic Semiconductor official sites and partner sites

**Require approval for:**

* Commercial product sites
* Community forums and unofficial resources
* Third-party tutorial sites
* Social media links
* Competitors' documentation

**Link review checklist:**

- [ ] Does the site provide significant value that can't be provided internally?
- [ ] Is the site maintained by a reputable organization?
- [ ] Is the URL stable and likely to remain available?
- [ ] Does the content align with Nordic's values and message?
- [ ] Have you checked the site for inappropriate content?
- [ ] Is a disclaimer provided if needed?

**Document your policy:**

Create internal guidelines for technical writers about:

* Which external sites can be linked without approval
* The approval process for new external references
* How often to audit external links
* What to do when external links break

**Link maintenance:**

* Regularly check external links (quarterly or bi-annually)
* Update broken links or remove them
* Consider using link checking tools in your build process
* Document link changes in release notes or changelogs

**Example approval workflow:**

1. Writer identifies need for external reference
2. Writer checks pre-approved list
3. If not pre-approved, writer submits link for review with justification
4. Reviewer assesses link against criteria
5. Approved links added to documentation and pre-approved list (if appropriate)
6. Periodic audits ensure links remain appropriate and functional
