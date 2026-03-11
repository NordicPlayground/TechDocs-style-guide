# Jargon

Jargon is the technical terminology or characteristic idiom of a special activity or group. Differentiating jargon from technical terminology is tricky. First, check the [Glossary](../glossary.md). If you don't find the term, the following checklist can help.

* If you think a term is jargon, it probably is.
* If it's an acronym or abbreviation, it may be jargon. Spell it out for clarity.
* If a reviewer questions your use of a term, it may be jargon.
* If the term is used in *The Wall Street Journal* or *The New York Times,* or in general-interest magazines, such as *Time* or *Newsweek,* it might be appropriate for some audiences.
* If the term is used in technical periodicals such as *CNET* or *Recode,* it's probably OK to use for technical audiences.

## When to avoid jargon

Don't use jargon if:

* You can use a more familiar term, such as *symbol* instead of *glyph.*
* The term is familiar to only a small segment of your readers.
* The term isn't specific to software, networking, cloud services, and so on.

Avoid business, marketing, and journalistic jargon, such as using *leverage* to mean *take advantage of.*

## Use technical terms carefully and consistently

Sometimes everyday words are given new meanings, like *cloud, batch,* or *dashboard*. Over time, some technical terms become widely understood, but before that happens, they can be confusing to people who aren't familiar with them. Use technical terms when they're the clearest way to communicate your message, but use them with care.

Here are technical terminology resources to check:

* [Glossary](../glossary.md)
* [*The American Heritage Dictionary*](https://ahdictionary.com/).
* [W3C](https://www.w3.org/standards/xml)
* [IEEE](https://www.ieee.org/index.html).
* *[PMI Lexicon of Project Management Terms](https://www.pmi.org/PMBOK-Guide-and-Standards/PMI-lexicon.aspx)*
* [FDIC List of Abbreviations and Glossary of Terms (Appendix B)](https://www.fdic.gov/bank/historical/managing/documents/history-consolidated.pdf).
* [Webopedia.com](https://www.webopedia.com/)
* [BusinessDictionary.com](https://www.businessdictionary.com/)
* [Whatis.TechTarget.com](https://whatis.techtarget.com/).

## Don't create a new term

Don't create a new term if an existing one serves your purpose. If you must create a new term, verify that it isn't already being used to mean something else.

Most people know the common definition of words. Use words in the most familiar sense, or define them if you can't. Be careful with common words that have industry-specific uses. Assume customers know the common definition of the word, not the industry-specific definition. If you must use the industry-specific definition, define the word in context.

|                   Situation                    |                 Example                  |
| ---------------------------------------------- | ---------------------------------------- |
| Don't create a new word from an existing word. | Don't use *bucketize* to mean *group.*   |
| Don't apply a new meaning to an ordinary word. | Don't use *graveyard* to mean *archive.* |

## Avoid Latin abbreviations

Do not use Latin abbreviations in documentation. They are unfamiliar to many readers, especially non-native English speakers, and create translation problems.

| Don't use | Use instead |
| --------- | ----------- |
| e.g. | for example, such as |
| i.e. | that is, in other words |
| etc. | and so on (see exception below) |
| viz. | namely, specifically |
| ergo | therefore |
| et al. | and others |
| vs. | compared to, against, or spell out "versus" |
| via | through, by using |
| per | for each, according to (context-dependent) |

**Exception:** "etc." is acceptable in space-constrained contexts such as table cells or UI labels where brevity is essential. In running text, use "and so on" or rephrase to list the items explicitly.

**Example:**

* **Avoid:** "The SDK supports multiple protocols, e.g., BLE, Thread, etc."
* **Use:** "The SDK supports multiple protocols, such as BLE, Thread, and Zigbee."

## Prefer simple words

Choose commonly understood words over formal or complex alternatives. Simple words are easier to read, translate, and understand.

| Complex word | Simpler alternative |
| ------------ | ------------------- |
| assist | help |
| commence | begin, start |
| consequently | so |
| constitute | make up, form |
| demonstrate | show |
| facilitate | help, make easier |
| furnish | provide, give |
| implement | carry out, set up |
| in addition | also |
| in order to | to |
| indicate | show, point to |
| modify | change |
| obtain | get |
| permit | let, allow |
| prior to | before |
| provide | give |
| regarding | about |
| require | need |
| shall | must (for requirements), will (for future) |
| should | must (if mandatory), consider (if optional) |
| subsequently | then, later, after |
| terminate | end, stop |
| utilize | use |

### "Shall" and "should"

Avoid *shall* and *should* in technical documentation. These words have specific legal meanings in standards documents and are ambiguous in general documentation.

* Use **must** when something is mandatory.
* Use **will** for statements of fact about future behavior.
* Use **can** when something is possible.
* Use **consider** or **we recommend** when something is optional but encouraged.

| Avoid | Use |
| ----- | --- |
| You shall configure the device before use. | You must configure the device before use. |
| The system should respond within 10 ms. | The system responds within 10 ms. |
| Users should back up their data. | Back up your data before updating. |
