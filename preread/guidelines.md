# Pre-Read DNA Rules

This file defines every rule that governs how a pre-read is written.
The Creator agent reads it before writing. The Reviewer agent checks against it.

A pre-read is not a lesson. It makes a beginner curious about the session. It tells them what they will be able to do,
why it matters, and leaves them with a question that the session answers.

---

## Audience

- Complete beginners. Assume zero prior knowledge of the topic.
- Students who may feel nervous about technical content.
- Write as a friendly guide who wants the student to turn up curious and calm.

---

## Inputs

| Input | Rule |
|---|---|
| Module Name | Context only. Use it to pick a course-relevant scenario and to write the Course use case. Never print it in the pre-read. |
| Session Name | The title. |
| Topics | The only topics the pre-read may mention. Technical names appear only in the Topics callout and the one core-term definition. |
| Learning Objectives | Decide what the outcome bullets say. Never copy their wording. Never write "learning objective" or "LO". |
| Setup (Yes or No) | Yes: add the Set Up section using the text or link the user pasted. No: leave the section out completely. |

If any input is missing, ask for all missing inputs in one short message. Never guess a missing input.

---

## Scenario Rules

- Use exactly ONE scenario for the whole pre-read. It is a small everyday situation that every beginner knows.
- It must be easy to picture in one sentence.
- It must be relevant to the course. Use the Module Name and Topics so it mirrors the real work students will do.
- It must carry every topic and every learning objective. Test each one against it before writing.
- Never reuse a scenario from an earlier pre-read. Before choosing, read the Real-world example box of every
  `*/preread.md` in the workspace root. Reject a scenario that matches one already used, even with different data.
- Do not repeat the scenario's details in two sections to fill space. Each section adds something new.
- The only other example allowed is the Course use case box in the Mental Map.
- If no scenario is easy, relevant, unused and carries every topic, ask the user before writing. Offer 2 options.

---

## Structure

Every pre-read has these sections in this order. No section is renamed or reordered.

| # | Heading | Level |
|---|---|---|
| 0 | Session Name (coloured span) | H2 |
| 1 | Mental Map | H3 |
| 2 | What You'll Learn | H3 |
| 3 | Why You Are Learning This Topic | H3 |
| 4 | {Scenario name} Puzzle | H3 |
| 5 | Think It Through | H3 |
| 6 | One Question to Carry Into the Session | H3 |
| 7 | Set Up Before the Session | H3, only when Setup = Yes |

Separate sections with a `---` rule. Do not add other sections.

---

## Section Rules

### Mental Map
- One Mermaid `flowchart TB` with the init line from the template.
- Exactly 4 boxes: Current Session (session title only), The Big Question (its own box), Course use case, Real-world example.
- The Course use case and the Real-world example must describe different things.
- The Course use case is specific to the course and holds a number or a named example.
- Arrows: Current Session to The Big Question, then The Big Question to each of the two example boxes.
- Use `&nbsp;` around arrow labels. Use the three classDefs from the template and `linkStyle default stroke-width:3px`.
- Use `&amp;` if a label needs an ampersand.
- No PNG is saved. The block renders wherever the page is viewed.

### What You'll Learn
- One hook sentence: "Have you ever wondered ...?" about a familiar moment in the scenario.
- One lead-in line: "By the end of this session, you will be able to:".
- 4 to 6 outcome bullets written to Bloom's Taxonomy. Each starts with ONE observable action verb as the orange bold phrase and says what the student does, with a number or named item from the scenario.
  - Choose the verb at the level of the objective it covers:
  - Remember: name, list, recall, identify
  - Understand: classify, explain, describe, interpret, summarise, predict
  - Apply: calculate, determine, solve, use, apply, estimate, demonstrate
  - Analyze: compare, differentiate, trace, examine
  - Evaluate: judge, justify, check, critique
  - Create: design, build, write, plan
  - Never open a bullet with: understand, know, learn, discover, appreciate, explore. Say "calculate", never "compute".
  - Never repeat an opening verb in one pre-read. Use a synonym from the same level. Order bullets from lower to higher level.
- Every learning objective is covered. No bullet is a topic name. No technical name appears in the bullets.
- A blockquote "Topics you will meet:" listing the topic names, then the line "Join the session to learn each of these in detail."

### Why You Are Learning This Topic
- 4 to 6 short sentences telling the scenario as a story the student has lived.
- Define the core term once: A **term** means plain meaning.
- One sentence linking it to the course.
- End with a "Think about it:" blockquote holding one question.

### Puzzle section
- Named after the scenario, for example "The Delivery App Puzzle".
- One intro line, then a small Markdown table of the scenario data with 3 to 6 rows.
- "What you want to happen:" with 3 short bullets.
- Optional: a read-only preview of 3 lines or fewer, introduced by "Here is how it might start. You do not need to
  understand it yet." Skip it when the topic has no code. Test it before keeping it (see Writing Rules).
- A "Wonder about this:" blockquote with 2 questions. Never explain the answers.

### Think It Through
- Exactly 3 questions on the same scenario, each with a one-line hint. Never give answers.
- Open with: "There is no wrong first try. Keep your guesses for the session."
- Questions must not need a concept the pre-read has not shown.

### One Question to Carry Into the Session
- A blockquote with one bold question and one follow-up question.

### Set Up Before the Session (only when Setup = Yes)
- A blockquote opening with "Do this before the session starts." in blue bold.
- One plain sentence naming the tool and why.
- The pasted text or link, exactly as given, with grammar corrected.
- Never invent, guess or change a link. If no link was pasted, ask for it.

---

## Writing Rules

- Every sentence has 20 words or fewer. One idea per sentence.
- Active voice. Address the reader as "you". Warm, curious and never talking down. No emojis.
- Use plain words. Write "use", not "utilize". Replace vague words with a number or a name.
- No jargon without a plain meaning in the same sentence.
- Never write: leverage, utilize, robust, seamlessly, empower, cutting-edge, dive into, delve, "learning objective", "LO".
- Never write these vague words. Use an exact fact, number or name instead: various, several, many, some, things, stuff, etc., basically, simply, easily, just, really, very, a lot, kind of, powerful, robust, efficient, modern, advanced, better, good, great, nice, handy, useful.
- Write at about a grade 7 reading level. The reader should feel calm and capable, never tested.
- Bold each key term once, at first use, and give its plain meaning right away.
- Use no tool, library or concept that is not in the topics.
- Python is the only language in code previews. Use realistic named data, never abstract values.
- Test every code preview before it goes in. Put the snippet and the few setup lines it needs (named data, imports) in a scratch file and run it with `python3 -I`. It must run without errors, and its output must match anything the pre-read implies. If a needed library is not installed, check the snippet with `ast.parse`, never claim it ran, and report it as "not executed". Never keep code that has been neither run nor parsed.

---

## Formatting Rules

- Colours: blue `#2F7DDE` for headings and callout labels, orange `#D9660B` for key terms and action phrases. No other colours in the text.
- Use `<span style="color:...">` for colour. Use bold inside the span.
- Callouts are standard Markdown blockquotes. Never use `:::` boxes.
- Code blocks are 3 lines or fewer. The only other fenced block is the Mermaid diagram.
- One blank line between every paragraph and list. Use tables only for the scenario data.
- No italics except inside the Mermaid question box.

---

## Length

- Body about 300 to 500 words, not counting the Mermaid block or code.
- No section may dominate the page.

---

## Output

```
{SessionName}_{YYYY-MM-DD}/
└── preread.md
```

- The folder sits in the workspace root. No PNG and no other file is saved.
- The Reviewer fixes the file in place. It never creates a side file or report file.
