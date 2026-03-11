# Editorial process

A consistent editorial process ensures documentation quality, accuracy, and alignment with the style guide. Define clear stages from planning through publication to maintain high standards across all contributors.

## Documentation lifecycle

### 1. Planning

Before writing, define the scope and goals of the documentation.

**Planning activities:**

* Identify the target audience and their needs
* Determine the document type (see [Document types](document-types.md))
* Outline the content structure
* Identify dependencies (product features, release timelines, SME availability)
* Estimate the effort and set milestones

**Planning outputs:**

* Content outline or topic list
* Audience definition
* Timeline with review milestones

### 2. Drafting

Write the first draft following the style guide. Focus on completeness and accuracy rather than polish.

**Drafting guidelines:**

* Follow the appropriate document type structure
* Include all required sections (introduction, prerequisites, steps, result)
* Use placeholder text for information you need to verify with SMEs
* Mark questions and uncertainties clearly (for example, with TODO comments)
* Write in the active voice and imperative mood for procedures

### 3. Self-review

Review your own draft before requesting peer review. Check for:

* Style guide compliance (voice, tense, terminology)
* Technical accuracy (test all procedures)
* Completeness (no missing steps or undefined terms)
* Clarity (no ambiguous instructions)
* Consistent formatting

### 4. Peer review

Have at least one colleague review the content.

**Types of peer review:**

* **Technical review:** A subject matter expert (SME) verifies accuracy
* **Editorial review:** A writer or editor checks style, clarity, and structure
* **Usability review:** A representative user tests procedures

### 5. Revision

Address review feedback and update the draft. If changes are substantial, request another review cycle.

### 6. Publication

Publish the final content through your documentation pipeline.

**Pre-publication checks:**

* All review comments are resolved
* Links are valid
* Images render correctly
* Navigation entries are in place
* Build completes without errors

### 7. Maintenance

Published documentation requires ongoing maintenance.

**Maintenance triggers:**

* Product updates or new releases
* Reader feedback reporting errors
* Broken links or outdated references
* Style guide changes

## Review types

### Technical review

**Reviewer:** Subject matter expert (developer, engineer, product manager)

**Focus:**

* Are the technical facts correct?
* Are the procedures accurate and complete?
* Are the code examples correct and functional?
* Are the prerequisites comprehensive?
* Are there technical nuances that the writer missed?

**How to request:**

Provide the reviewer with:

* The draft content (link or document)
* Specific questions you need answered
* Context about the audience and purpose
* A realistic deadline

### Editorial review

**Reviewer:** Technical writer, editor, or experienced peer

**Focus:**

* Does the content follow the style guide?
* Is the writing clear and concise?
* Is the structure logical and scannable?
* Are terms used consistently?
* Is the tone appropriate for the audience?

### Usability review

**Reviewer:** Someone matching the target audience profile

**Focus:**

* Can the reader complete the procedures successfully?
* Where does the reader hesitate or get confused?
* Is any information missing?
* Are the prerequisites clear and sufficient?
* Does the reader achieve the expected outcome?

## Providing feedback

### For reviewers

When reviewing documentation:

* Be specific about what needs to change and why
* Suggest alternatives, don't just identify problems
* Distinguish between required changes and suggestions
* Focus on the reader's experience, not personal preference
* Prioritize issues by impact (accuracy errors > style issues > minor wording)

**Effective feedback examples:**

* "Step 3 produces an error on macOS. The correct command is `brew install cmake`."
* "The introduction doesn't explain who this guide is for. Consider adding an audience statement."
* "This paragraph has three ideas. Split it so readers can scan more effectively."

**Ineffective feedback examples:**

* "This doesn't work." (What doesn't work? Where? What did you observe?)
* "I don't like this section." (Why? What would improve it?)
* "Change 'utilize' to 'use'." (Good catch, but more helpful to note the pattern: "The style guide prefers 'use' over 'utilize' throughout.")

### For writers receiving feedback

When receiving feedback:

* Don't take feedback personally — it improves the documentation
* Ask for clarification when feedback is vague
* Explain your rationale when you disagree, but be open to changing your mind
* Prioritize fixing accuracy issues immediately
* Track recurring feedback to improve your writing process

## Editorial standards

### Minimum review requirements

Define minimum review requirements based on content risk:

| Content type | Minimum review |
| ------------ | -------------- |
| New getting started guide | Technical + editorial + usability |
| New conceptual topic | Technical + editorial |
| Procedure update | Technical |
| Minor text correction | Self-review |
| API reference (auto-generated) | Technical spot-check |

### Review turnaround

Set expectations for review turnaround times:

* Minor reviews (typos, small updates): 1-2 business days
* Standard reviews (new topics): 3-5 business days
* Complex reviews (architecture changes, new guides): 1-2 weeks

### Version control

Use version control (Git) for all documentation:

* Create branches for new content or significant changes
* Use pull requests for review
* Don't merge without the required approvals
* Write clear commit messages describing the change

## Continuous improvement

### Track documentation quality

Monitor indicators of documentation quality:

* Reader feedback (positive and negative)
* Support ticket volume for documented topics
* Page views and time-on-page analytics
* Procedure completion rates (if measurable)
* Review cycle time and rework frequency

### Retrospectives

Periodically review the editorial process itself:

* What types of errors recur most frequently?
* Where do review cycles stall?
* What feedback do readers provide most often?
* What improvements would reduce maintenance burden?

Use these insights to refine the process, update the style guide, and improve writer training.
