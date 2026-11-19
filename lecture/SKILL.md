---
name: cc-lecture-script
description: >
  Create a 120-minute lecture script (format v2) for a session in any batch.
  Triggered by /create-lecture-script "Module" "Session" "Topics" "LOs" "Yes|No" "curriculum.csv" ["announcement text"].
  Handles the full pipeline: curriculum context, creator agent writes the script, verifier agent
  checks and fixes it, output saved to SessionName_YYYY-MM-DD/lecture_script.md with images/ and data/.
---

# Lecture Script Skill

A lecture script is the mentor's single document for a 120-minute session. It uses one Why, What and How, walked in four topics (Topic 1 to 4), with four quizzes.

## Standards the creator and verifier enforce

Full rules live in `lecture/guidelines.md` and `lecture/terms.md`. In short:

- Fixed order: Agenda, Scenario, Problem Statement, What We Will Use, How, Topic 1 to 4, Closing: Outcome & Summary, Announcements (only if Yes), Launch the Feedback Poll.
- Learning Objectives appear verbatim in the Agenda, grouped 1 to 2 per topic. Deep LOs get more minutes and more "Extending it" variations; light LOs get a quick check and return in the Closing. No depth label.
- Inside a topic: bridge question, Example, Extending it, Quiz. Exactly four quizzes.
- Accuracy 100%. Every code block is run and its output pasted. SQL uses MySQL on a real server with a fixed "today". If under 98% confident, ask.
- One famous Indian company as framing only; the Scenario layout varies per script; the data (100 to 150 rows with edge cases) is invented for teaching.
- Bridges to earlier sessions use only what the batch's curriculum CSV lists as completed.
- Banned: "synthetic", "Step" as a name for a lecture part, I Do/We Do/You Do, Recap, Break, Exit Ticket and the other terms in `terms.md`. 🎯 is the only emoji.

## Inputs

1. Module name (context only, never printed)
2. Session name
3. Topics
4. Learning Objectives
5. Announcements: Yes or No (optional text)
6. Batch curriculum CSV

## Pipeline

1. Create `SessionName_YYYY-MM-DD/` with `images/` and `data/`.
2. `lecture/tools/curriculum_context.py` reads the CSV and reports what the batch completed. It asks when a column or the session cannot be matched.
3. `agent_lecture_creator` writes the script, data, charts and runs `check_script.py`.
4. `agent_lecture_verifier` reviews 10 categories, re-runs the code, fixes in place (up to 3 passes) and returns Accepted or Rejected.
5. The command reports the path, status, scenario, topic grouping and bridges used.
