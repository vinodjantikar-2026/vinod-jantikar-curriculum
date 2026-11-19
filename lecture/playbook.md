# <font color='#1d4ed8'>Lecture Script Playbook (Format v2)</font>

How to turn **any** session (module, session name, topics, learning objectives, batch curriculum) into a script in the frozen v2 format of `template.md`. Finished examples are in `examples/`.

---

## <font color='blue'>1. Inputs</font>

| Input | Example |
|:--|:--|
| Module (context only, never printed) | Core Programming & Analytical Foundations |
| Session name | Text and Dates with Calculated Columns |
| Topics | String functions; Date functions; Derived columns; ... |
| Learning Objectives (verbatim) | Apply string functions to clean and combine text columns; ... |
| Announcements | Yes or No (with text, optional) |
| Batch curriculum CSV | the batch's curriculum file |
| Duration | 120 minutes |

The Learning Objectives appear **verbatim** in the Agenda, in teaching order. They are grouped, not repeated as headings.

---

## <font color='blue'>2. Framing the LOs into four topics</font>

A script has one Why, one What and one How. The How is walked in **four topics** (Topic 1 to Topic 4).

| Decision | Rule |
|:--|:--|
| Grouping | Group 1 or 2 LOs per topic, in teaching order. LOs that use the same data or tool share a topic. |
| Depth | Pick the deep LOs (the ones learners must be able to do alone). Give them more minutes and more "Extending it" variations. |
| Breadth | Light LOs (names, parts, simple formats) get one quick "Extending it" and appear again in the Closing. They are never skipped. |
| Showing depth | By minutes and by the number of variations. Never write "deep" or "light" in the script. |
| Quizzes | Exactly four, one at the end of each topic, aimed at the topic's main (deep) LO. |
| Fewer or more LOs | 3 LOs: one topic gets a single LO and a longer Example. 7 or more LOs: group three light ones in one topic. The count stays four topics. |

Example (7 LOs, MySQL): Topic 1 text (1 LO), Topic 2 dates (parts light, interval deep), Topic 3 columns (derived deep, aliases taught while building), Topic 4 tidy and test (ROUND/CAST light, IS NULL deep).

---

## <font color='blue'>3. Method</font>

| Stage | Do this | Check before moving on |
|:-:|:--|:--|
| 1 | **Read the curriculum context.** Run `lecture/tools/curriculum_context.py`. Note the sessions completed before this one and the tools and ideas they covered. | Bridge only to what the CSV lists as completed. |
| 2 | **Pick one scenario**, a famous Indian company as framing only, not used in earlier scripts, whose single decision needs every LO. | Each LO answers part of one question. |
| 3 | **Write the question** the whole lecture answers, and the poll. | It can be answered in the Closing in one sentence. |
| 4 | **Frame the LOs** into four topics (section 2) and set minutes. | Agenda adds up to 120. |
| 5 | **Design the data** (100 to 150 rows when code is used) with edge cases. Save in `data/`. | Row count, planned nulls, edge cases present. |
| 6 | **Write the lecture-level What** (short, section 4). | A learner can see every tool or idea before the Topics. |
| 7 | **Write Topics 1 to 4:** bridge question, Example, Extending it, Quiz. | The bridge opens from the previous result. No Why/What/How headings. |
| 8 | **Run every code block** and paste the output exactly. Cross-check key numbers. | Re-running gives identical output. |
| 9 | **Draw charts** from the same numbers (PNG in `images/`, dpi 200, `width="900"`). | No overlapping labels; every file exists. |
| 10 | **Close** with the answer, the Outcome, the Summary, Announcements (only if Yes) and "Launch the Feedback Poll". | Reveals the poll. Nothing new is taught. |

---

## <font color='blue'>4. The lecture-level What</font>

- **Tool-heavy topics (SQL, libraries):** one intro line and one toolkit table (Topic / Tools / In one line). Formulas and warnings go in the topic where the tool is first used.
- **Maths topics:** a terms table plus the key formulas in LaTeX, because the formulas are the lecture's What. Keep it to one screen.
- Never a per-topic What. Never a long glossary.

---

## <font color='blue'>5. Using the batch curriculum</font>

`curriculum_context.py` reads the batch CSV (column names vary, so it maps them by name) and reports the sessions before the target and the next one.

- Use it as **bridge sentences in plain prose**, at the start of Topic 1 and where a tool is reused ("you used `GROUP BY` last week").
- Reuse tools and ideas the learners have completed, and reuse their earlier datasets' style only if it fits.
- Never mention a tool, term or session the CSV does not list before this session as already known.
- Never write "Builds on", "Connects To" or a metadata line.

---

## <font color='blue'>6. Choosing the scenario</font>

Use the company only as a familiar setting. Never claim it uses these numbers.

| Session type | Setting | Decision it frames | Typical data |
|:--|:--|:--|:--|
| Distributions, sampling, A/B tests | Swiggy or Zomato delivery | Which delivery promise to show | Delivery minutes, on-time flags |
| Regression, prediction | Ola or Uber-style cabs | Fare to show before booking | Distance, fare |
| Regression with several features | Flipkart or Amazon India orders | Delivery charge or return risk | Weight, distance, order value |
| Classification, churn | Jio, Airtel or PhonePe | Which user is likely to leave | Usage, tenure, plan |
| Time series, forecasting | IRCTC bookings or UPI volumes | Demand next week | Daily counts |
| Risk, returns | Zerodha or Groww | How risky a portfolio is | Daily returns |
| Pricing, discounts | Nykaa or BigBasket baskets | Which offer to run | Basket value, discount |
| SQL, cleaning, joins | Flipkart orders, Zomato restaurants | Which orders or restaurants need action | Orders table, ratings |

**Vary the Scenario shape.** Use a table, a short story, a before/after, a single risk or a comparison. Two consecutive scripts must not open with the same layout.

---

## <font color='blue'>7. Edge cases to build into the data</font>

| Case | Why |
|:--|:--|
| Smallest and largest values | Show the range and where predictions stop being safe |
| Repeated values (ties) | Same input, different outcomes |
| A few outliers | Show what squared errors or averages do to them |
| A floor or cap (minimum fare, maximum discount) | A real rule that bends the pattern |
| Rare category or zero count | Show empty groups |
| Missing values (empty and empty-string) | Only when an LO is about cleaning or NULL |
| Messy text (spaces, mixed case) | Only for text LOs |
| Month-end and year-end dates | Only for date LOs |

Generate once with a fixed seed, check with a second tool, then freeze the file.

---

## <font color='blue'>8. SQL sessions</font>

- Use MySQL syntax and say it in the title, for example "(MySQL)". Write "MySQL 8.0 or later" in the setup note.
- Deliver the dataset as `data/<name>.sql` (CREATE TABLE plus INSERT) with a CSV copy.
- Run every query on a real server and paste the table output exactly. Add `ORDER BY` with a tie-breaker (the id) wherever order matters.
- Use a fixed "today" (for example 15 March 2026), never `CURDATE()`.
- Include error outputs that teach, copied from the server.
- Do not use a clause the session has not taught, unless it is explained in one line where it appears.

---

## <font color='blue'>9. What never changes</font>

- Order: Agenda, Scenario, Problem Statement, What We Will Use, How, Topic 1 to 4, Closing, Announcements (if Yes), Launch the Feedback Poll.
- Inside a topic: bridge question, Example, Extending it, Quiz. "I Do", "We Do", "Recap" are never written.
- Four quizzes: Question, four Options, Correct Answer, one-line reason for every option.
- Colours, red `🎯 Instructor Note` (one or two lines), LaTeX for all maths, 10 lines or fewer per code block, `Code Explanation` or `Logic Explanation` after every block.
- "Give learners 30 seconds to respond in chat."
- The words "synthetic" and "Step" (as a name for a lecture part) are never written.

---

## <font color='blue'>10. Final checklist</font>

1. Agenda minutes = 120; LOs verbatim; every LO appears once.
2. Four Topic sections and four quizzes.
3. Every output matches a fresh run of the code; key numbers match a second method.
4. Every quiz answer is recomputed; each wrong option is wrong for a stated reason.
5. Every domain statement is true; extrapolation and outlier warnings are stated where relevant.
6. No forward references; no repeated explanation across topics.
7. Bridges to earlier sessions use only what the curriculum CSV lists as completed.
8. Banned words absent (see `terms.md`); 🎯 is the only emoji; every image file exists.
9. `check_script.py` passes.
