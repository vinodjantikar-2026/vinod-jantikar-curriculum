---
name: cc-preread
description: >
  Create a curiosity-first pre-read for a session in any batch.
  Triggered by /create-pre_read "Module Name" "Session Name" "Topics" "Learning Objectives" "Yes|No" ["setup text"].
  Handles the full pipeline: creator agent writes the preread, reviewer agent
  verifies it, output saved to SessionName_YYYY-MM-DD/preread.md (no PNG).
---

# Pre-Read Skill

## Preread Creation Pipeline

A pre-read makes a beginner curious about the session. It is not a lesson. It uses one everyday scenario, tells the
student what they will be able to do, and ends with a question that the session answers.

### Standards the creator and reviewer enforce

Full rules live in `preread/guidelines.md`. In short:

- One everyday scenario per pre-read. Easy to picture, relevant to the course, never reused from an earlier pre-read.
- What You'll Learn: a "Have you ever wondered" hook, the lead-in "By the end of this session, you will be able to:", then 4 to 6 outcome bullets.
  Each bullet opens with one Bloom's verb from the bank (Remember, Understand, Apply, Analyze, Evaluate, Create levels), never repeated.
- Sentences of 20 words or fewer, about a grade 7 reading level, and none of the banned vague words. Say "calculate", never "compute".
- Any code preview is run, or parsed and reported as not executed, before it stays.
- Technical names only in the Topics callout and one core-term definition. Never print the Module Name.
- Exactly 3 Think It Through questions with hints and no answers.
- The Set Up section appears only when Setup is Yes, and uses the pasted text without inventing a link.

### Inputs

| Input | Required | Example |
|---|---|---|
| `module_name` | Yes | `"Core Programming & Analytical Foundations"` (context only, never printed) |
| `session_name` | Yes | `"Probability Distributions"` |
| `topics` | Yes | `"Discrete vs continuous; Binomial; Normal and z-scale; Empirical rule"` |
| `learning_objectives` | Yes | `"Classify a random variable; Compute a binomial probability; ..."` |
| `setup` | Yes | `Yes` or `No` |
| `setup_text` | Only if setup is Yes | The setup text or documentation link to paste into the Set Up section |

### Step 1 — Parse Arguments

Read the quoted arguments from `$ARGUMENTS` in the order above. If any of the first five is missing, ask for all missing inputs
in one short message. Never guess. If `setup` is Yes and no setup text was given, ask for it.

### Step 2 — Create Output Folder

Run from the workspace root (the folder that contains `preread/`):

```python
from datetime import date
import re, os

safe_name = re.sub(r'[^\w\s-]', '', session_name).strip().replace(' ', '_')
folder_name = f"{safe_name}_{date.today().strftime('%Y-%m-%d')}"
folder_path = os.path.join(os.getcwd(), folder_name)
os.makedirs(folder_path, exist_ok=True)
```

### Step 3 — Invoke Creator Agent

Spawn `agent_preread_creator` (`.claude/agents/agent_preread_creator.md`) with `module_name`, `session_name`, `topics`,
`learning_objectives`, `setup`, `setup_text` and `folder_path`.

The creator picks one easy, course-relevant scenario that no earlier `*/preread.md` uses, writes `preread.md`, runs its
self-check script and confirms the Mermaid block parses. It saves no PNG.

### Step 4 — Invoke Reviewer Agent

Spawn `agent_preread_verifier` (`.claude/agents/agent_preread_verifier.md`) with:
- `preread_path`: `{folder_path}/preread.md`
- `module_name`, `session_name`, `topics`, `learning_objectives`, `setup`

It reviews 10 categories and fixes issues in place.

### Step 5 — Report

Print the final status (Accepted / Rejected), the saved `preread.md` path, the scenario used and any remarks.
Mention anything unverified, such as a pasted link.

---

## Output

```
{SessionName}_{YYYY-MM-DD}/
└── preread.md
```

---

## Reference Files

All canonical files live in the `preread/` folder of the workspace:

| File | Purpose |
|---|---|
| `preread/guidelines.md` | DNA rules: inputs, scenario rules, structure, writing and formatting rules |
| `preread/template.md` | The fixed section skeleton with placeholders |
| `preread/agents/creator.md` | Creator agent full spec, including the self-check script |
| `preread/agents/reviewer.md` | Verifier agent full spec, 10 review categories |
| `preread/commands/create-pre_read.md` | Command documentation |
