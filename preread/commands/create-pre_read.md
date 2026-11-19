# create-pre_read

Create a complete, reviewed, curiosity-first pre-read for a session in any batch.

## Usage

```
/create-pre_read "Module Name" "Session Name" "Topic 1; Topic 2; ..." "Objective 1; Objective 2; ..." "Yes|No" ["setup text or link"]
```

## Example

```
/create-pre_read "Core Programming & Analytical Foundations" "Probability Distributions" "Discrete vs continuous; Binomial; Normal and z-scale; Empirical rule" "Classify a random variable as discrete or continuous; Compute a binomial probability for a stated number of successes; Compute a normal probability by standardising to the z-scale; Apply the empirical rule to estimate the proportion of values within k standard deviations" "No"
```

## Arguments (quoted strings, in order)

| Position | Argument | Notes |
|---|---|---|
| 1 | Module name | Context only. Never printed in the pre-read |
| 2 | Session name | Becomes the title |
| 3 | Topics | The only topics the pre-read may mention |
| 4 | Learning objectives | Decide what the outcome bullets say |
| 5 | Setup | `Yes` adds the Set Up section. `No` leaves it out |
| 6 | Setup text | Only when setup is Yes: the pasted setup text or documentation link |

Anything missing from arguments 1 to 5 is asked for once. Nothing is guessed.

## What This Command Does

1. **Parses** the arguments and asks for anything missing
2. **Creates folder**: `{SessionName}_{YYYY-MM-DD}/` in the workspace root
3. **Invokes `agent_preread_creator`** which picks one unused, course-relevant scenario and writes `preread.md` with Bloom's-verb outcome bullets and tested code previews
4. **Invokes `agent_preread_verifier`** which checks 10 categories and fixes issues in place
5. **Reports** the saved path, the verdict and the scenario used

## Output

```
{SessionName}_{YYYY-MM-DD}/
└── preread.md
```

No PNG is created. The Mermaid mental map renders inside `preread.md`.

## Pipeline Reference

- Creator agent: `.claude/agents/agent_preread_creator.md`
- Reviewer agent: `.claude/agents/agent_preread_verifier.md`
- Full skill spec: `preread/SKILL.md`
- Guidelines: `preread/guidelines.md`
- Template: `preread/template.md`
