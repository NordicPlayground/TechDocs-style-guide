# Writing for all abilities

## Put the person first

In general, refer to a person who has a kind of disability, not a disabled person.

## Write brief, meaningful, and focused text

Be especially clear and concise in instructions for product setup, basic features, input methods, and accessibility features.

## Lead with what matters most

Leading with the most important information helps readers know immediately where to focus their attention.

## Write short and simple paragraphs

Keep paragraphs short and sentence structure simple. Aim for one verb per sentence. Read text aloud and imagine it spoken by a screen reader.

## Use parallel writing structures for similar things

For example, use singular nouns for each top-level heading. Or, use a verb to start each item in a list.

## Spell out words like *and, plus,* and *about.*

Screen readers can misread text that uses special characters like the plus sign (+) and tilde (~).

## Write brief link text

Write brief but meaningful link text. Links should make sense without the surrounding text.

## Distinguish link text visually

Use redundant visual cues, such as both color and underline.

## Don’t force line breaks

Don’t force line breaks (also known as hard returns) within sentences and paragraphs. They may not work well in resized windows or with enlarged text.

## Emphasize important points

Emphasize important points visually and stylistically. Lists, headings, and tables reinforce relationships between concepts. Provide summary information about the table, and use concise and specific column headings.

## Use heading styles

Use heading styles instead of text formatting. Heading levels communicate the hierarchy of content.

## Don’t use directional terms only

Don’t use directional terms as the only clue to location. *Left, right, up, down, above,* and *below* aren’t very useful for people who use screen-reading software. If you must use a directional term, provide additional text about the location, such as *in the* ***Save As*** *dialog box, on the* ***Standard*** *toolbar,* or *in the title bar.*

## Document alternate input methods

In product documentation, document all supported modes of interaction, input commands, and keyboard shortcuts. Include mice, keyboards, voice recognition devices, game controllers, gestures, and other interaction modes.

## Use generic verbs for all input methods

Use generic verbs that apply to all input methods and devices. Avoid verbs like *click* (mouse) and *swipe* (touch) that don't make sense with some alternative input methods used for accessibility.

## Alternative text for images

Alternative text (alt text) provides text descriptions of images for people using screen readers or when images don't load. Writing effective alt text is crucial for accessibility.

### Alt text for images

Write concise, descriptive alt text that conveys the essential information or function of the image.

**Guidelines:**

* Describe the content and function, not the appearance
* Keep alt text concise (aim for 150 characters or less)
* Don't start with "Image of" or "Picture of" (screen readers announce it's an image)
* Include relevant context from surrounding text when needed
* For linked images, describe the destination or function

**Examples for Nordic documentation:**

**Avoid:**

* Alt text: "Image of a circuit board"

**Use:**

* Alt text: "nRF52840 DK showing button and LED locations"

**Functional images:**

**Avoid:**

* Alt text: "Picture"

**Use:**

* Alt text: "Download nRF Connect SDK" (describes the link function)

**Technical diagrams:**

**Avoid:**

* Alt text: "Diagram"

**Use:**

* Alt text: "BLE connection state machine showing transitions between disconnected, advertising, and connected states"

### Alt text for complex graphics

Complex graphics like architecture diagrams, flowcharts, and detailed schematics need more comprehensive descriptions.

**Two-part approach:**

1. **Short alt text**: Brief description (< 150 characters)
2. **Long description**: Detailed explanation in the surrounding text or a linked page

**Example for flow diagram:**

```html
<img src="ble-advertising-flow.png"
     alt="BLE advertising state flow diagram">
```

**Surrounding text provides detail:**

"Figure 1 shows the BLE advertising state flow. The device starts in the idle state. When `bt_le_adv_start()` is called, it transitions to the advertising state. From advertising, the device can either return to idle (when advertising stops) or transition to connected (when a central device connects). From the connected state, the device returns to idle when disconnected."

**For architecture diagrams:**

**Short alt text:** "nRF Connect SDK architecture layers"

**Detailed description in text:** "The nRF Connect SDK consists of four main layers: Application layer (user applications), nRF layer (Nordic-specific drivers and libraries), Zephyr RTOS layer (kernel and subsystems), and Hardware layer (nRF SoCs and external components). Each layer interfaces with the layer directly below it."

**For complex wiring diagrams:**

**Short alt text:** "nRF52840 DK UART wiring diagram"

**Detailed description:** Provide a table or list describing each connection:

| Connection | From | To |
| ---------- | ---- | -- |
| TX | nRF52840 P0.06 | USB-UART RX |
| RX | nRF52840 P0.08 | USB-UART TX |
| GND | nRF52840 GND | USB-UART GND |

### Alt text for decorative images

Decorative images that don't convey information or functionality should have empty alt text.

**Use empty alt text for:**

* Design elements (borders, dividers)
* Purely decorative graphics
* Images whose content is fully explained in surrounding text

**Example:**

```html
<img src="decorative-line.png" alt="">
```

**Note:** Use `alt=""` (empty string), not omitting the alt attribute. Screen readers treat missing alt attributes differently than empty alt text.

**When an image is truly decorative:**

* Icon next to a text label that duplicates the icon's meaning
* Decorative photographs that don't add information
* Visual spacers or design elements

**Example:**

```html
<button>
  <img src="download-icon.png" alt="">
  Download SDK
</button>
```

The button text "Download SDK" provides the information, so the icon's alt text should be empty.

## WCAG guidelines

Follow Web Content Accessibility Guidelines (WCAG) to ensure your documentation is accessible.

### WCAG principles

**Perceivable:** Information must be presentable to users in ways they can perceive

* Provide text alternatives for non-text content
* Provide captions and alternatives for multimedia
* Make content adaptable and distinguishable

**Operable:** User interface components must be operable

* Make all functionality available from keyboard
* Give users enough time to read and use content
* Don't design content that causes seizures
* Help users navigate and find content

**Understandable:** Information and operation must be understandable

* Make text readable and understandable
* Make content appear and operate in predictable ways
* Help users avoid and correct mistakes

**Robust:** Content must be robust enough for various technologies

* Maximize compatibility with current and future tools
* Ensure content works with assistive technologies

### WCAG compliance levels

* **Level A:** Minimum accessibility (essential features)
* **Level AA:** Recommended standard for most organizations
* **Level AAA:** Highest level of accessibility

**Target Level AA for technical documentation** as it provides a good balance of accessibility and practicality.

### Key WCAG requirements for technical docs

**Text alternatives (WCAG 1.1.1 - Level A):**

* Provide alt text for all informative images
* Use empty alt text for decorative images
* Provide transcripts for audio content

**Color contrast (WCAG 1.4.3 - Level AA):**

* Text must have at least 4.5:1 contrast ratio with background
* Large text (18pt or 14pt bold) needs 3:1 minimum
* Don't rely solely on color to convey information

**Resize text (WCAG 1.4.4 - Level AA):**

* Content must be readable when text size is increased to 200%
* Use relative units (em, rem, %) instead of fixed pixels

**Keyboard accessible (WCAG 2.1.1 - Level A):**

* All functionality must be available via keyboard
* Document keyboard shortcuts
* Ensure logical tab order

**Meaningful sequence (WCAG 1.3.2 - Level A):**

* Present content in a logical reading order
* Use proper heading hierarchy
* Structure lists correctly

**Headings and labels (WCAG 2.4.6 - Level AA):**

* Use descriptive headings
* Label form elements clearly
* Use semantic HTML heading tags (h1, h2, h3)

## Screen reader considerations

Write with screen reader users in mind to improve accessibility.

**Structure content logically:**

* Use semantic HTML (headings, lists, tables)
* Maintain logical heading hierarchy (h1 → h2 → h3)
* Use lists for sequential or related items

**Write descriptive link text:**

**Avoid:**

* "Click [here](#) for more information"
* "Read [more](#)"
* "[Learn more](#)"

**Use:**

* "[Download the nRF Connect SDK](#)"
* "[Configure BLE advertising parameters](#)"
* "[View nRF52840 specifications](#)"

Screen readers often navigate by links, so users hear link text out of context. Make links meaningful on their own.

**Avoid directional-only references:**

**Avoid:**

* "See the image above"
* "In the table below"
* "On the left sidebar"

**Use:**

* "See Figure 1: BLE state diagram"
* "Table 1 lists the supported peripherals"
* "In the navigation menu, select Configuration"

**Provide context for code examples:**

**Example:**

"The following code example initializes BLE advertising with a 100 ms interval:"

```c
struct bt_le_adv_param adv_param = {
    .interval_min = BT_GAP_ADV_FAST_INT_MIN_2,
    .interval_max = BT_GAP_ADV_FAST_INT_MAX_2,
};
```

"After setting the parameters, call `bt_le_adv_start()` to begin advertising."

**Tables:**

* Provide table captions
* Use header cells (<th>) for column and row headers
* Keep tables simple when possible
* Consider lists for simple two-column data

**Icons and symbols:**

* Don't rely on icons alone
* Provide text labels or titles
* Use ARIA labels when needed

**Interactive elements:**

* Ensure buttons and controls have descriptive labels
* Provide instructions for complex interactions
* Announce state changes (for example:, "Configuration saved")
