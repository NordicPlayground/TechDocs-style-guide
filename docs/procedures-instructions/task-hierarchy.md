# Task hierarchy

Technical documentation uses a hierarchy of instructional elements to guide readers through work of varying complexity. Understanding these levels helps you choose the right structure for each piece of procedural content.

## Levels of the task hierarchy

### Task

A task is a high-level goal that a reader wants to accomplish. It may involve multiple procedures and decision points.

**Examples of tasks:**

* Set up a BLE peripheral application
* Deploy firmware over the air
* Configure power management for a battery-operated device

Tasks are often too broad for a single procedure. They serve as the organizing principle for a section or chapter.

### Procedure

A procedure is a self-contained set of steps that accomplishes a specific, well-defined outcome within a task. A task may include multiple procedures performed in sequence.

**Examples of procedures:**

* Install the nRF Connect SDK
* Configure BLE advertising parameters
* Flash the application to the development kit

Each procedure has a clear start, a series of steps, and a verifiable result.

### Step

A step is a single action within a procedure. Each step describes one thing the reader does.

**Examples of steps:**

* "Open `prj.conf` in a text editor."
* "Set `CONFIG_BT_DEVICE_NAME` to your desired device name."
* "Click **Build** in the nRF Connect for VS Code toolbar."

### Substep

A substep breaks a complex step into smaller parts. Use substeps when a single step contains multiple closely related actions that must be performed together.

**Example:**

1. Configure the device name:

    a. Open `prj.conf`.

    b. Add the line `CONFIG_BT_DEVICE_NAME="My Device"`.

    c. Save the file.

## Mapping tasks to documentation structure

### When to use a task-level topic

Create a task-level topic when the goal spans multiple procedures or requires the reader to make decisions about which procedures to follow.

**Structure:**

* Title describing the goal
* Introduction explaining the task and its context
* Overview of the procedures involved
* Links to individual procedure topics (or procedures inline, if they're short)
* Verification of the overall result

**Example: "Setting up a BLE peripheral application"**

This task-level topic would introduce the goal, list prerequisites, and link to procedures for configuring the project, writing the application code, building, and flashing.

### When to use a procedure-level topic

Create a procedure-level topic when the instructions lead to a single, specific outcome.

**Structure:**

* Title starting with a verb
* Brief introduction (1-2 sentences: what and why)
* Prerequisites
* Numbered steps
* Expected result

**Example: "Configure BLE advertising parameters"**

### When to use inline steps

For very short procedures (2-3 steps) that are part of a larger topic, write the steps inline rather than creating a separate topic.

**Example (inline within a concept topic):**

"To verify the connection, run `nrfjprog --ids` and confirm that the device serial number appears in the output."

## Organizing multi-procedure tasks

### Sequential procedures

When procedures must be performed in order, make the sequence explicit through numbering, headings, or introductory text.

**Example structure:**

"## Setting up your development environment

Complete these procedures in order:

1. [Install prerequisites](#install-prerequisites)
2. [Install the nRF Connect SDK](#install-the-nrf-connect-sdk)
3. [Install the toolchain](#install-the-toolchain)
4. [Verify the installation](#verify-the-installation)"

### Branching procedures

When the reader must choose between procedures based on their situation, present the decision clearly before presenting the options.

**Example structure:**

"## Flashing firmware

Choose the method that matches your setup:

* **Using nRF Connect for VS Code:** [Flash with the VS Code extension](#flash-with-vs-code)
* **Using the command line:** [Flash with west](#flash-with-west)
* **Using the Programmer app:** [Flash with the Programmer app](#flash-with-programmer)"

### Optional procedures

Clearly mark procedures that are optional. Explain when and why a reader might choose to perform them.

**Example:**

"## (Optional) Configure debug logging

Enable debug logging to troubleshoot connection issues during development. Skip this section for production builds."

## Nesting limits

### Maximum nesting depth

Limit procedural nesting to three levels: task → procedure → step (with substeps). Deeper nesting creates confusion and makes content harder to follow.

If you find yourself creating sub-sub-steps, restructure the content:

* Split the procedure into multiple smaller procedures
* Extract complex steps into their own procedure
* Simplify the instructions

### Step count limits

Limit procedures to 10 steps. If a procedure exceeds 10 steps:

* Look for steps that can be combined
* Split the procedure into two or more procedures
* Extract setup steps into a prerequisites section

## Naming conventions

### Task titles

Use noun phrases or "How to" phrases for task-level topics:

* "BLE peripheral setup" (noun phrase)
* "How to set up a BLE peripheral" (how-to phrase)

### Procedure titles

Use imperative verb phrases or "To" phrases:

* "Configure BLE advertising" (imperative)
* "To configure BLE advertising" (to-phrase, useful in context)

### Step text

Use imperative verb phrases:

* "Open the configuration file."
* "Add the following line."
* "Build and flash the application."

Keep the naming convention consistent within each documentation set.
