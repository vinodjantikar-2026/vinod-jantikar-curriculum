# Lecture Script Guidelines (Format v2, frozen)

A lecture script is the mentor's single document for a 120-minute session. It reads top to bottom as one story, in one Why, What, How structure.

## 1. Non-negotiables
1. **Pedagogy order is fixed.** Agenda, Scenario, Problem Statement (Why), What We Will Use (What), How with Topic 1 to 4 (How), Closing, Announcements (only if Yes), Launch the Feedback Poll.
2. **Accuracy is 100%.** Every number, definition, formula, output and quiz answer is verified. Facts, logic, domain meaning and topic relevance are all checked. If under 98% confident, stop and ask the user. Never guess.
3. **Topic relevance is 100%.** Teach only the given LOs and topics. Nothing outside them, except a short bridge to completed sessions.
4. **LOs are verbatim** in the Agenda, in teaching order, each appearing once.

## 2. Structure
- **Agenda:** table of four Topics (Topic / What we do / Learning objectives covered / Minutes) and a Closing row. Total is 120. One Instructor Note on pacing.
- **Scenario:** a famous Indian company as framing only. The layout varies per script. Instructor Note: the data is invented, no claim about the company.
- **Problem Statement:** a short story of a mistake with its consequence, one purple question, a poll Instructor Note.
- **What We Will Use:** once, short. SQL or tool topics: one intro line and a toolkit table. Maths topics: a terms table and key formulas.
- **How: Walking Through …:** a Mermaid flow of Topic 1 to 4 and the Closing. Every node has a `style` line with a dark fill and `color:#ffffff` (white text), copied from the template.
- **Topic 1 to 4:** a purple bridge question, then Example, one or more Extending it, and one Quiz. No Why/What/How headings.
- **Closing: Outcome & Summary:** answer the Problem Statement using each topic once, Outcome table, "Therefore,", reveal the poll, Summary table (one row per LO plus Practical value).

## 3. Framing the LOs
- Group 1 or 2 LOs per topic. Deep LOs get more minutes and more variations. Light LOs get a quick check and appear again in the Closing.
- Show depth by time and by the count of "Extending it", never by a label.
- Four quizzes in total, one per topic, about one per 30 minutes.

## 4. Code and outputs
- 10 lines or fewer per block. Run every block. Paste the output exactly. Python outputs from a real run; SQL outputs from a real MySQL server.
- SQL: MySQL syntax, a fixed "today", `ORDER BY` with a tie-breaker, errors copied from the server when taught.
- "Predict before running: What will happen?" before the first run, with a short Instructor Note holding the expected answer.
- Explain under Code Explanation (one bullet per line or group) or Logic Explanation.
- Maths in LaTeX. Key formula in `\boxed{}`.

## 5. Visuals and data
- Charts are PNG in `images/`, drawn from the same numbers as the code, dpi 200, embedded with `<p align="center"><img src="images/x.png" alt="…" width="900"></p>`.
- Datasets: 100 to 150 rows with planned edge cases, in `data/`. SQL gets `data/<name>.sql` and a CSV copy.

## 6. Instructor Notes and chat
- Red heading `<font color="red">**🎯 Instructor Note**</font>`, 1 to 2 lines. Used for expected answers, poll answers, warnings, pacing.
- Chat prompts: "Give learners 30 seconds to respond in chat."

## 7. Quiz format
Question / Options A to D / Correct Answer / Explanation with a one-line reason for every option. Distractors are plausible mistakes. The correct letter varies across the four quizzes.

## 8. Language
Plain words, short sentences, mentor wording. No forward references. See `terms.md`.

## 9. Using the curriculum CSV
Bridge only to sessions listed before the target. Reuse their tools in plain prose at the start of Topic 1 and where a tool returns. If a needed column is missing from the CSV, ask the user.

## 10. Announcements
Input Yes: add the `Announcements` section with the user's text, or the default mentor note. Input No: omit the section entirely. The final red "Launch the Feedback Poll" header is always present.
