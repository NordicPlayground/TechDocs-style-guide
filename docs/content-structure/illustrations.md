# Illustrations

Illustrations — diagrams, screenshots, photographs, and other visual elements — complement text by showing what words alone cannot convey efficiently. Use illustrations strategically to clarify complex concepts, show spatial relationships, and demonstrate procedures.

## When to use illustrations

Use an illustration when:

* A concept involves spatial relationships (circuit layouts, network topologies, architecture diagrams)
* A procedure involves visual elements (UI interactions, physical connections)
* A comparison is easier to understand visually than in text
* A process flow has branches or parallel paths
* Text alone would require lengthy, complex descriptions

Don't use an illustration when:

* The information is simple enough to convey in a sentence
* The illustration would merely decorate the page
* The content changes frequently (illustrations are expensive to update)
* The same information is already clear from the text

## Types of illustrations

### Block diagrams

Use block diagrams to show system architecture, data flow, and component relationships.

**Best for:**

* SoC internal architecture (showing CPU, peripherals, memory)
* Protocol stacks (showing layers and their interactions)
* Application architecture (showing modules and dependencies)
* Network topologies (showing devices and connections)

### Flowcharts

Use flowcharts to show decision processes, state machines, and sequential workflows.

**Best for:**

* Boot sequences
* State machine diagrams
* Error handling flows
* Decision trees (choosing the right protocol, selecting a configuration)

### Sequence diagrams

Use sequence diagrams to show interactions between components over time.

**Best for:**

* BLE connection establishment sequences
* API call sequences
* Communication protocol exchanges
* OTA firmware update procedures

### Screenshots

Use screenshots to show tool interfaces, configuration screens, and expected output.

**Best for:**

* nRF Connect for VS Code interface elements
* Programmer app operations
* Power Profiler Kit output
* Terminal output showing expected results

See [UI interactions](../procedures-instructions/ui-interactions.md) for screenshot best practices.

### Photographs

Use photographs when physical setup or hardware identification matters.

**Best for:**

* Development kit hardware identification (button locations, LED positions, connector types)
* Physical wiring connections
* Antenna placement

### Schematic excerpts

Use schematic excerpts to show electrical connections relevant to the discussion.

**Best for:**

* GPIO pin connections
* External component wiring
* Power supply configurations

## Creating effective illustrations

### Design for clarity

* Use clean, simple designs with minimal visual clutter
* Limit the number of elements to what is necessary
* Use consistent colors, shapes, and line styles
* Ensure text labels are large enough to read
* Use high contrast between elements

### Use consistent visual language

Establish and maintain conventions across all illustrations:

* Use the same shapes for the same types of components
* Use consistent color coding (for example, blue for BLE, green for Thread)
* Apply the same line styles for the same types of relationships
* Use a consistent font and text size

### Size and resolution

* Create illustrations at a resolution suitable for your output format
* For web documentation, target a minimum width of 600 pixels
* Use vector formats (SVG) when possible for scalability
* Ensure illustrations are readable on mobile devices

### Accessibility

Every illustration must have a text alternative for users who cannot see it.

* Write descriptive alt text for every image
* For complex diagrams, provide a text description in the surrounding content
* Don't embed essential information only in illustrations — include it in the text as well

See [Accessibility](../writing-tips/accessibility.md) for alt text guidelines.

## Placing illustrations in documentation

### Position relative to text

Place illustrations immediately after the text that introduces or references them. Don't force readers to scroll or navigate to find the illustration.

**Example:**

"Figure 1 shows the connection between the nRF52840 DK and an external sensor.

*[Image: nRF52840 DK connected to BME280 sensor via I2C, with SDA on P0.26 and SCL on P0.27]*"

### Description before, additional information after

Place the descriptive introduction *before* the illustration and any supplementary explanation *after* it. This follows the natural reading flow: the reader learns what to look for, sees the illustration, then reads additional details.

**Pattern:**

1. Introductory text describing what the illustration shows
2. The illustration
3. Additional explanation, callout descriptions, or related details

**Example:**

"Figure 2 shows the power consumption profile during a BLE advertising event.

*[Image: Power consumption during BLE advertising showing peaks at TX and RX events]*

The initial peak corresponds to the radio ramp-up phase. The three subsequent peaks are the advertising transmissions on channels 37, 38, and 39."

### Introduce before showing

Always reference an illustration in the text before it appears. Don't insert an illustration without textual context.

**Avoid:**

Placing a diagram between two paragraphs with no reference in either paragraph.

**Use:**

"The following diagram shows the BLE connection state machine:" followed by the diagram.

### Provide captions

Use descriptive captions that tell readers what the illustration shows and why it matters.

**Weak caption:**

"Figure 1: System architecture."

**Strong caption:**

"Figure 1: nRF52840 BLE peripheral application architecture showing the application layer, BLE stack, and hardware abstraction layer."

### Number illustrations consistently

In formal or long documents, number illustrations sequentially (Figure 1, Figure 2). In shorter online topics, numbering is optional.

## Maintaining illustrations

### Keep illustrations current

Outdated illustrations are worse than no illustrations. Update illustrations when:

* The software UI changes
* The hardware design changes
* The documented process changes
* New components are added

### Store source files

Keep editable source files for all illustrations (SVG files, drawing tool project files). Rasterized images (PNG, JPG) cannot be easily modified.

### Use a consistent tool

Standardize on a diagramming tool for the team. This ensures consistency in style and makes it easier for any team member to update illustrations.

### Separate text from images

Keep translatable text outside of image files when possible. Embedded text requires creating new images for each language. Use callout labels, numbered callouts with a legend, or overlay text that can be managed separately.

## Nordic Figure Guidelines

For Nordic-specific illustration requirements — including color palettes, sizing conventions, file formats, and branding rules — refer to the Nordic Figure Guidelines. These guidelines define the visual standards that ensure consistency across all Nordic documentation.
