## <span style="color:#2F7DDE">{SESSION_NAME}</span>

### <span style="color:#2F7DDE">Mental Map</span>

```mermaid
%%{init: {'flowchart': {'nodeSpacing': 45, 'rankSpacing': 55, 'padding': 20}}}%%
flowchart TB
  CUR["<b>Current Session</b><br/>{SESSION_NAME}"]
  Q["<b>The Big Question</b><br/><i>{ONE_CURIOUS_QUESTION_ABOUT_THE_TOPIC}</i>"]
  CV["<b>Course use case</b><br/>{HOW_IT_IS_USED_IN_THIS_COURSE_WITH_A_NUMBER_OR_NAMED_EXAMPLE}"]
  RL["<b>Real-world example</b><br/>{THE_SCENARIO_IN_ONE_LINE}"]

  CUR ==> Q
  Q ==>|&nbsp;Used in the course&nbsp;| CV
  Q ==>|&nbsp;Seen in real life&nbsp;| RL

  classDef currSes fill:#ffe0b2,stroke:#ef6c00,color:#4e342e,stroke-width:3px
  classDef ask fill:#e3f2fd,stroke:#1565c0,color:#0d47a1,stroke-width:3px
  classDef val fill:#e8f5e9,stroke:#2e7d32,color:#1b5e20

  class CUR currSes
  class Q ask
  class CV,RL val

  linkStyle default stroke-width:3px
```

---

### <span style="color:#2F7DDE">What You'll Learn</span>

Have you ever wondered {HOW_A_FAMILIAR_THING_IN_THE_SCENARIO_HAPPENS_ON_ITS_OWN}?

By the end of this session, you will be able to:

- <span style="color:#D9660B">**{BLOOM_VERB_1}**</span> {WHAT_THE_STUDENT_DOES_1_IN_PLAIN_WORDS_WITH_A_NUMBER_OR_NAMED_ITEM}.
- <span style="color:#D9660B">**{BLOOM_VERB_2}**</span> {WHAT_THE_STUDENT_DOES_2}.
- <span style="color:#D9660B">**{BLOOM_VERB_3}**</span> {WHAT_THE_STUDENT_DOES_3}.
- <span style="color:#D9660B">**{BLOOM_VERB_4}**</span> {WHAT_THE_STUDENT_DOES_4}.

> <span style="color:#2F7DDE">**Topics you will meet:**</span> {TOPIC_NAMES_COMMA_SEPARATED}.
>
> Join the session to learn each of these in detail.

---

### <span style="color:#2F7DDE">Why You Are Learning This Topic</span>

{STORY_4_TO_6_SHORT_SENTENCES_ABOUT_THE_SCENARIO}

{DEFINE_THE_CORE_TERM_ONCE: A <span style="color:#D9660B">**term**</span> means PLAIN_MEANING.}

{ONE_SENTENCE_LINKING_IT_TO_THE_COURSE}

> <span style="color:#2F7DDE">**Think about it:**</span> {ONE_QUESTION_THE_STORY_RAISES}

---

### <span style="color:#2F7DDE">{SCENARIO_NAME} Puzzle</span>

{ONE_LINE_INTRODUCING_THE_SCENARIO_DATA}

| {COLUMN_1} | {COLUMN_2} |
|:----------:|:----------:|
| {ROW_1} | {VALUE_1} |
| {ROW_2} | {VALUE_2} |
| {ROW_3} | {VALUE_3} |

<span style="color:#D9660B">**What you want to happen:**</span>

- {WISH_1}
- {WISH_2}
- {WISH_3}

{OPTIONAL_PREVIEW: test the code before keeping it. Delete this paragraph and the code block when the topic has no code}

> <span style="color:#D9660B">**Wonder about this:**</span>
>
> - {WONDER_QUESTION_1}
> - {WONDER_QUESTION_2}

---

### <span style="color:#2F7DDE">Think It Through</span>

There is no wrong first try. Keep your guesses for the session.

**1. {QUESTION_1}**
Hint: {ONE_LINE_HINT_1}

**2. {QUESTION_2}**
Hint: {ONE_LINE_HINT_2}

**3. {QUESTION_3}**
Hint: {ONE_LINE_HINT_3}

---

### <span style="color:#2F7DDE">One Question to Carry Into the Session</span>

> <span style="color:#2F7DDE">**{ONE_BOLD_QUESTION}**</span>
>
> {ONE_FOLLOW_UP_QUESTION}

{SET_UP_BLOCK: when Setup = Yes, add a --- rule and the block below. When Setup = No, delete this line and the block.}

---

### <span style="color:#2F7DDE">Set Up Before the Session</span>

> <span style="color:#2F7DDE">**Do this before the session starts.**</span> {ONE_PLAIN_SENTENCE_NAMING_THE_TOOL_AND_WHY} {THE_PASTED_SETUP_TEXT_OR_LINK_EXACTLY_AS_GIVEN_WITH_GRAMMAR_CORRECTED}