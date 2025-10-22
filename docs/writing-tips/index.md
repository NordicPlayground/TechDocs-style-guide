# Writing tips

To improve readability and comprehension, choose your words wisely and use them consistently. Concise, clear sentences save space, are easy to understand, and facilitate scanning.

## Write short, simple sentences

* Give customers just enough information to make decisions confidently. Prune every excess word. Replace complex sentences and paragraphs with lists and tables.

* Punctuating a sentence with more than a few commas usually indicates a complex sentence. Consider rewriting it or breaking it into multiple sentences.

* Avoid linking more than three phrases or clauses by using coordinate conjunctions such as *and,* *or,* or *but.* Better yet, avoid linking more than two.

| **Use this** |         **Not this**          |
|--------------|-------------------------------|
| Ready to buy? Contact us. | If you're ready to purchase Office 365 for your organization, contact your Microsoft account representative. |
| Create a chart that's just right for your data by using the Recommend Charts command on the Insert tab. | The Recommended Charts command on the Insert tab recommends charts that are likely to represent your data well. Use the command when you want to visually present data, and you're not sure how to do it. |

## Get to the point fast

Lead with what’s most important. Front-load keywords for scanning. Make customer choices and next steps obvious.

| **Use this** |         **Not this**          |
|--------------|-------------------------------|
| Save time by creating a document template that includes the styles, formats, and page layouts you use most often. Then use the template whenever you create a new document. | Templates provide a starting point for creating new documents. A template can include the styles, formats, and page layouts you use frequently. Consider creating a template if you often use the same page layout and style for documents. |

## Revise weak writing

Most of the time, start each statement with a verb. Edit out *you can* and *there is, there are, there were*.

| **Use this** |         **Not this**          |
|--------------|-------------------------------|
| Store files online, access them from all your devices, and share them with coworkers. | You can access Office apps across your devices, and you get online file storage and sharing. |

## Word choice

To improve readability and comprehension, choose your words wisely and use them consistently. If you mean the same thing, use the same word.

### Choose simple verbs without modifiers

| **Use this** |         **Not this**          |
|--------------|-------------------------------|
|     use      |     utilize, make use of      |
|    remove    | extract, take away, eliminate |
|     tell     |       inform, let know        |

### Don’t use two or three words when one will do

| **Use this** |        **Not this**        |
|--------------|----------------------------|
|      to      | in order to, as a means to |
|     also     |        in addition         |
|   connect    |   establish connectivity   |

### Use one word for a concept

Use one word for a concept, and use it consistently. Avoid using synonyms to refer to the same concept or feature. Don’t use the same word to refer to multiple concepts or features.

### Choose words that have one clear meaning

|                    **Use this**                     |                   **Not this**                    |
|-----------------------------------------------------|---------------------------------------------------|
| *Because* you created the table, you can change it. | *Since* you created the table, you can change it. |

#### Similar words with different meanings

| Term          | Definition |
| ------------- | ---------- |
| Send vs. issue | *Send* implies an intended receiver.</br>**Example:** The system sends a warning to the host.</br></br>*Issue* is where something is put out for anything that is looking for it to read it.</br>**Example:** An event register and interrupt are available for each measurement and are issued once the measurement has been completed. |

### Omit unnecessary adverbs—words

Omit unnecessary adverbs—words that describe how, when, or where. Unless they're important to the meaning of a statement, leave them out.

Examples:

* quite
* very
* quickly
* easily
* effectively

### Be careful with words that can be both nouns and verbs

Use words that can be both nouns and verbs carefully—*file, post, mark, screen, record,* and *report,* for example. Use the sentence structure and context to eliminate ambiguity.

### Don’t use verbs as nouns or nouns as verbs

|      **Use this**      |    **Not this**    |
| ---------------------- | ------------------ |
| open an invitation     | open an invite     |
| affect performance     | impact performance |
| download the paper     | get the download   |
| respond to the request | respond to the ask |

### Use contractions

Write using the same, everyday words you use in conversation.

* Use common contractions, such as *it's, you're, that's,* and *don't,* to create a friendly, informal tone.
* Don't mix contractions and their spelled-out equivalents in UI text. For example, don't use *can't* and *cannot* in the same UI.
* Never form a contraction from a noun and a verb, such as *Nordic's developing a lot of new products.*
* Avoid ambiguous or awkward contractions, such as *there'd, it'll,* and *they'd.*
* Steer clear of overly casual forms like *gonna, wanna, gotta,* or archaic forms like *'twas, 'tis.*
* Match subject-verb agreement when contracting: use *doesn't* with singular subjects, not *don't*.
  * Incorrect: "The nRF Connect SDK don't support that protocol version."
  * Correct: "The nRF Connect SDK doesn't support that protocol version."

#### Match formality to content type

Adjust your use of contractions based on the documentation context:

* In urgent safety warnings, use complete words to convey seriousness.
  * Warning format: "Do not flash firmware while the device operates under external power."
  * Warning format: "Do not interrupt the secure boot process."
* In error-prevention instructions, full words reinforce the importance.
  * Example: "Do not exceed the maximum GPIO current rating of 15 mA."
* In tutorial content and general guidance, contractions maintain friendliness.
  * Example: "You can't enable both modes simultaneously."

#### Clarity in apostrophe use

Technical documentation requires precision with apostrophes that mark contractions versus possession:

* The pattern *word's* can mean either "word is/has" or show ownership, leading to misreading.
  * Unclear: "The application's optimized for low power consumption."
  * Better: "The application is optimized for low power consumption."
  * Or: "The application's power optimization reduces consumption." (clearly possessive)
* When describing technical components, favor clarity over brevity.
  * Unclear: "The UART's transmitting data at 115200 baud."
  * Better: "The UART is transmitting data at 115200 baud."
* Product names with possessive forms work fine when ownership is unambiguous.
  * Clear: "The nRF52840's radio supports multiple protocols." (the radio belonging to nRF52840)

#### Distinguish "it's" from "its"

These two forms cause frequent confusion in technical writing:

* Use *it's* only when you mean "it is" and the sentence maintains clarity.
  * Example: "The build system detects dependencies; it's automatic."
* Use *its* for possession without an apostrophe.
  * Example: "The SoC manages its power states independently."
* When describing technical operations, consider whether "it" references a clear subject.
  * Vague: "After initialization, it's configured with default values."
  * Specific: "After initialization, the device is configured with default values."
* Rewrite sentences where either reading could make sense.
  * Confusing: "The peripheral checks its status when it's polled by the CPU."
  * Clearer: "The peripheral checks status when the CPU polls it."
