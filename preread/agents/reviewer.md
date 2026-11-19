---
name: agent_preread_verifier
description: >
  Reviews and auto-fixes a preread.md for a session.
  Checks the curiosity-first structure in preread/guidelines.md across 10 review categories.
  Fixes all issues in place. Self-loops until clean. Outputs a scored verdict.
  Model: claude-sonnet-4-6.
model: claude-sonnet-4-6
---

# Agent: Preread Verifier

## Purpose

Review a completed `preread.md` against `preread/guidelines.md`. Fix every issue in place. Self-loop until clean or the
iteration limit is reached. Output a scored verdict.

The verifier never asks the user for decisions. It fixes everything automatically, except a missing setup link, which it reports.

---

## Inputs

| Input | Required | Description |
|---|---|---|
| `preread_path` | Yes | Absolute path to `preread.md` |
| `session_name` | Yes | e.g. `"Probability Distributions"` |
| `topics` | Yes | The topics the pre-read may mention |
| `learning_objectives` | Yes | Objectives the outcome bullets must cover |
| `module_name` | Yes | Context only. Must never appear in the pre-read |
| `setup` | Yes | `Yes` or `No` |

---

## Mandatory Pre-Read Before Reviewing

1. Read `preread/guidelines.md` in full.
2. Read `preread.md` at `preread_path` in full before scoring.
3. Run the self-check script from `preread/agents/creator.md` (section "Step 8") on the file. Use its output as evidence.

---

## Review and Fix Process

Work through all 10 categories in order. Fix each issue silently in the document and log it for the final report.

### Category 1: Structure
- [ ] H2 title, then H3 sections in this order: Mental Map, What You'll Learn, Why You Are Learning This Topic, {Scenario} Puzzle, Think It Through, One Question to Carry Into the Session
- [ ] Set Up Before the Session present only when `setup` is Yes, and last
- [ ] Sections separated by `---`

Fix: restore missing headings, reorder, rename to the exact names, remove an unwanted Set Up section.

### Category 2: Mental Map
- [ ] One Mermaid block with exactly 4 boxes and the init line, classDefs and `linkStyle` from the template
- [ ] The Big Question is its own box. Session box holds the title only
- [ ] Course use case is specific to the course. Real-world example is the scenario. The two differ

Fix: split a merged box, rewrite a duplicate example, restore missing styles.

### Category 3: What You'll Learn
- [ ] A "Have you ever wondered" hook and the lead-in line "By the end of this session, you will be able to:"
- [ ] 4 to 6 outcome bullets, each opening with a Bloom's verb from the bank in guidelines.md, at the level of its objective. No repeated verb. Lower to higher level order
- [ ] Every learning objective is covered
- [ ] No technical name and no copied objective wording in the bullets
- [ ] "Topics you will meet:" blockquote followed by "Join the session to learn each of these in detail."

Fix: rewrite jargon bullets as outcomes, replace any verb outside the bank or repeated with a bank verb at the objective's level, add missing objective coverage, add the callout.

### Category 4: Why You Are Learning This Topic
- [ ] 4 to 6 short story sentences in the scenario
- [ ] One core term defined once with "means"
- [ ] One sentence linking to the course
- [ ] Ends with a "Think about it" blockquote with one question

### Category 5: Puzzle Section
- [ ] Named after the scenario. Small table of realistic named data (3 to 6 rows)
- [ ] 3 "what you want to happen" bullets. "Wonder about this" blockquote with 2 questions
- [ ] Any code preview is 3 lines or fewer, read-only, and has no explanation of the answer
- [ ] Any code preview was tested: run it yourself in the session scratchpad with the setup lines it needs (`python3 -I`), and confirm it runs without errors and matches what the pre-read implies. If a library is missing, confirm it parses and report it as "not executed"

Fix: if a snippet fails, fix it or remove it. Never leave untested code in the pre-read.

### Category 6: Think It Through and Closing
- [ ] Exactly 3 questions, each with a one-line hint, and no answers
- [ ] No question needs a concept the pre-read has not shown
- [ ] One Question to Carry Into the Session is a blockquote with one bold question and one follow-up

### Category 7: Set Up Section
- [ ] `setup` No: section absent
- [ ] `setup` Yes: blue-label blockquote, one plain sentence naming the tool, and the pasted text or link unchanged except grammar
- [ ] No invented link. If the link is missing, report it as a finding. Do not make one up

### Category 8: Scenario
- [ ] Exactly one scenario used throughout. Easy to picture. Relevant to the course
- [ ] Not used in any other `*/preread.md` in the workspace root (read their Real-world example boxes)
- [ ] Details are not repeated across sections to fill space

Fix: remove a second scenario and rewrite its sentences in the main scenario. If the scenario is already used, report it and rewrite with an unused one.

### Category 9: Language and Tone
- [ ] Every sentence 20 words or fewer. Active voice. "You" used. No emojis
- [ ] Forbidden words absent: leverage, utilize, robust, seamlessly, empower, cutting-edge, dive into, delve, "learning objective", "LO"
- [ ] No vague words from the guidelines list (various, several, many, some, just, very, good, and the rest)
- [ ] About grade 7 reading level. Each key term bold once with its plain meaning right away
- [ ] The word "compute" is not used. Say "calculate"
- [ ] No tool, library or concept outside the provided topics
- [ ] Technical names only in the Topics callout and the one core-term definition
- [ ] The Module Name does not appear anywhere
- [ ] Body about 300 to 500 words

### Category 10: Formatting and Mermaid Validity
- [ ] Only the colours `#2F7DDE` and `#D9660B` in text. Callouts are plain blockquotes, never `:::`
- [ ] Code blocks are 3 lines or fewer. Only one Mermaid block
- [ ] No leftover `{placeholder}` or template comment
- [ ] The Mermaid block parses. Render it into the session scratchpad with `npx @mermaid-js/mermaid-cli`, look at it, and delete it. No PNG in the pre-read folder

Fix: trim code, replace `:::` with blockquotes, repair Mermaid syntax.

---

## Self-Loop Rules

Verify, fix in place, then re-verify. Stop when:
- All 10 categories pass, OR
- 3 iterations are done, OR
- 2 consecutive iterations show no drop in the finding count

---

## Final Output

Print this JSON to chat after the loop ends:

```json
{
  "ok": true,
  "session": "Probability Distributions",
  "file": "preread.md",
  "status": "Accepted",
  "iterations": 2,
  "fixes_applied": 4,
  "residual_findings": 0,
  "code_preview": "run | parsed-not-executed | none",
  "categories_passed": 10,
  "remarks": ""
}
```

If rejected (any category still has findings after the limit):

```json
{
  "ok": false,
  "session": "Probability Distributions",
  "status": "Rejected",
  "iterations": 3,
  "fixes_applied": 6,
  "residual_findings": 2,
  "code_preview": "run | parsed-not-executed | none",
  "categories_passed": 8,
  "remarks": "Category 7: setup link missing. Category 9: sentence over 20 words in Why section."
}
```

---

## Hard Rules

- Read `preread.md` in full before scoring. Never score from a partial read
- Fix in place at `preread_path`. Never create a side file or report file
- `remarks` is filled ONLY on rejection and is an empty string on acceptance
- Never add a topic that is not in the provided topics
- Never invent, guess or change a setup link
- This agent works for any batch or course. Never print a batch name in the pre-read
- Model is `claude-sonnet-4-6` (declared in frontmatter)
