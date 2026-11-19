Parse the arguments: $ARGUMENTS

The arguments are quoted strings in this order:
1. module_name — the module the session belongs to (context only, never printed in the script)
2. session_name — the session title
3. topics — the topics to cover, separated by semicolons
4. learning_objectives — the Learning Objectives, separated by semicolons (they appear verbatim in the Agenda)
5. announcements — `Yes` or `No`
6. curriculum_csv — path to the batch's curriculum CSV
7. announcement_text — optional, only when announcements is Yes

If any of arguments 1 to 6 is missing, ask for all missing inputs in one short message. Never guess them.
If announcements is `Yes` and there is no announcement_text, use the default mentor note from the template.
If announcements is `No`, the script has no Announcements section.

Execute the following pipeline:

## Step 1 — Create the output folder

Run from the workspace root (the folder that contains `lecture/`):

```python
from datetime import date
import re, os

session_name = "<parsed from arg 2>"
root = os.getcwd()
assert os.path.isdir(os.path.join(root, 'lecture')), "Run this from the workspace root"
safe_name = re.sub(r'[^\w\s-]', '', session_name).strip().replace(' ', '_')
folder_name = f"{safe_name}_{date.today().strftime('%Y-%m-%d')}"
folder_path = os.path.join(root, folder_name)
os.makedirs(os.path.join(folder_path, 'images'), exist_ok=True)
os.makedirs(os.path.join(folder_path, 'data'), exist_ok=True)
print(folder_path)
```

If `{folder_path}/lecture_script.md` already exists, ask the user before overwriting it.

## Step 2 — Read the batch curriculum

Run `python3 lecture/tools/curriculum_context.py "<curriculum_csv>" "<session_name>" --json`.
- Exit code 2 means a column or the session could not be matched. Show the `ASK:` lines to the user, get the answer, then continue. Never guess.
- Pass the JSON (completed sessions, completed topics, next session) to the creator.

## Step 3 — Invoke the creator agent

Spawn the `agent_lecture_creator` agent with:
- module_name, session_name, topics, learning_objectives, announcements, announcement_text
- curriculum_context (the JSON from Step 2)
- folder_path (from Step 1)

Wait for it to finish. It saves `lecture_script.md`, `images/` and `data/` in the folder. It runs every code block, pastes real outputs, and runs `lecture/tools/check_script.py` before handing over.

## Step 4 — Invoke the verifier agent

Spawn the `agent_lecture_verifier` agent with:
- script_path: `{folder_path}/lecture_script.md`
- module_name, session_name, topics, learning_objectives, announcements
- curriculum_context

## Step 5 — Report

Print to the user:
- Path to the saved `lecture_script.md`
- Status: Accepted / Rejected, with iterations and fixes applied
- The scenario, and how the four topics group the LOs (with minutes)
- Which earlier sessions were used as bridges
- Anything unverified (for example a tool that could not be run) and any question that needs the user's answer
