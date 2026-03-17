Now I have the skill format pattern from `scout-competitors` and `scout-feasibility`. The body is a dense, directive instruction paragraph — but `scout-inertia` needs structural scaffolding to target A-11/A-12/A-13/A-14/A-15. Variations can extend the format where structure demands it.

---

# scout-inertia Prompt Variations — Round 7

## Axis Map

| Variation | Axis | Single/Combined |
|-----------|------|-----------------|
| V-01 | Role sequence (FM Analyst first) | Single |
| V-02 | Output format (tabular column schema) | Single |
| V-03 | Lifecycle emphasis (fail-first, C-05 structurally first) | Single |
| V-04 | Tabular + FM inventory table | Combined (A-13 + A-14) |
| V-05 | Tabular + FM inventory + BRIDGE dual-closure | Combined (A-13 + A-14 + A-12) |

---

## V-01 — Role Sequence: FM Analyst First

**Axis**: Role sequence
**Hypothesis**: Running Failure Mode Analyst before Defeat Condition Strategist produces stronger C-04 content — the strategist has labeled FM-[N] citations to ground defeat conditions, preventing generic "value proposition" defeats that read like marketing copy rather than failure analysis.

```
You are running /scout:inertia for topic: {topic}.

Inertia -- the choice to do nothing -- is the primary competitor to every feature. Your job is
to answer one question: why does inertia lose? If you cannot answer that with evidence, stop
and name what is missing.

Run three roles in sequence. Each role reads all previous output before writing.

ROLE 1 -- FAILURE MODE ANALYST
Name the specific workaround in use: the actual practice (not "a manual process"), the role
that owns it, how often it runs, and the ongoing cost with a unit. Then enumerate at least 3
failure modes -- scenarios where the workaround breaks, produces errors, corrupts silently,
requires rework, or cannot scale. Label each FM-01, FM-02, FM-03 (continue as needed). For
each FM: (a) describe the concrete scenario, (b) name the role affected, (c) name the
observable trigger -- the specific condition that causes the failure, not "when it breaks",
(d) state whether the failure is silent or visible to the user. Generic pain points
("manual is slow") do not qualify. Concrete failures ("CSV export silently truncates rows
over 65,536 -- no error surfaced") qualify.

ROLE 2 -- SWITCHING COST AUDITOR
Read Role 1 before writing. Quantify at least two switching cost categories: (1) migration
effort in time or money, cited to a specific role, and (2) at least one of: training
overhead, process disruption, or in-flight work at risk. Every cost carries a unit.
"Significant" without a number fails. Declare Inertia Threat Score: HIGH / MEDIUM / LOW.
Default is HIGH. Any non-HIGH declaration requires a quantified justification.

ROLE 3 -- DEFEAT CONDITION STRATEGIST
Read Roles 1-2 before writing. Identify at least 3 conditions under which teams abandon the
workaround and adopt the feature. Each condition must: (a) name a specific team type or
segment -- not "users", (b) be falsifiable -- "teams switch when workaround fails files
> 10MB" passes; "teams switch when they see the value" fails, (c) cite at least one FM
label from Role 1 by identifier. These conditions are the answer to "why does inertia lose."
If you cannot write them, return to Role 1 -- the failure modes are not concrete enough.

Write artifact to: simulations/scout/inertia/{topic}-scout-inertia-{date}.md
```

---

## V-02 — Output Format: Tabular Column Schema

**Axis**: Output format
**Hypothesis**: Requiring named column schemas throughout makes criterion gaps structurally visible as blank cells without a full read (A-13). A row with a blank "Role Affected" cell is a visible C-01 violation. A row with a blank "Trigger Condition" cell is a visible C-05 gap. Prose cannot expose these gaps at a glance; tables can.

```
You are running /scout:inertia for topic: {topic}.

Inertia is the primary competitor. Answer: why does inertia lose? Evidence required. A blank
cell in a required column is an unanswered criterion -- leave it blank rather than filling it
with a placeholder.

Produce the artifact with the following section structure and table schemas. Prose lists are
not acceptable where a table is specified.

SECTION 1 -- WORKAROUND PROFILE (prose, one paragraph)
Name: (a) the specific workaround -- named practice or tool, not "manual process",
(b) the role that owns it, (c) execution cadence, (d) ongoing cost with a unit.

SECTION 2 -- FAILURE MODE INVENTORY
Table columns: FM-[N] | Scenario | Role Affected | Trigger Condition | Silent or Visible | Impact
Minimum 3 rows. "Scenario" names a concrete event. "Trigger Condition" is the specific
observable event that causes the failure. "Silent or Visible" answers: does the system
surface an error, or does the failure propagate undetected?

SECTION 3 -- SWITCHING COST ANALYSIS
Table columns: Cost Category | Quantified Cost | Unit | Role Bearing Cost
Minimum 2 rows. "Quantified Cost" is a number. "Unit" is the unit string. A row with a
blank Unit cell fails C-02.

SECTION 4 -- INERTIA THREAT SCORE
Declared value: HIGH / MEDIUM / LOW. Default HIGH. One-sentence justification required for
any non-HIGH declaration.

SECTION 5 -- DEFEAT CONDITIONS
Table columns: DC-[N] | Condition Statement | Team Type | FM-[N] Link | Falsifiable? | Observable Evidence
Minimum 3 rows. "Team Type" names a specific segment. "FM-[N] Link" cites at least one
row from Section 2. "Falsifiable?" is Y or N -- only Y rows count toward the C-04 minimum.
"Observable Evidence" names the metric or event that would confirm the condition was reached.

Write artifact to: simulations/scout/inertia/{topic}-scout-inertia-{date}.md
```

---

## V-03 — Lifecycle Emphasis: Fail-First

**Axis**: Lifecycle emphasis (C-05 structurally first, satisfies A-10)
**Hypothesis**: Placing failure modes as the structural first output section forces the analyst to enumerate workaround weaknesses before committing to a switching cost or defeat narrative. This prevents a common failure pattern: defeat conditions written first and FMs retrofitted to support a pre-formed conclusion. The trailing self-check converts content gaps into visible unanswered questions.

```
You are running /scout:inertia for topic: {topic}.

Inertia is the active, habitual choice to keep a working solution. Teams that choose it are
not passive -- they are continuing something that has worked before. Your analysis begins
with that solution's failure modes, not with your argument against it.

FAIL-FIRST DECLARATION: Identify all known failure modes of the current workaround before
any other analysis. This section is structural first because defeat conditions are only
credible when grounded in observed failures. An analysis that begins with "why the feature
wins" and works backward has already failed.

SECTION 1 -- WORKAROUND FAILURE MODES (write before any other section)
Name the workaround: specific practice, role that owns it, ongoing cost with a unit.
Then enumerate at least 3 failure modes where it breaks, corrupts silently, requires rework,
or cannot scale. Label FM-01, FM-02, FM-03... For each: name the scenario, the role
affected, the observable trigger, and whether the failure is silent or visible. Generic
pain points do not qualify. Concrete, observable scenarios do.

SECTION 2 -- SWITCHING COST ANALYSIS
Given the failure modes above: what does it cost teams to stop? Quantify at least two
categories with units. Cite the role bearing each cost. Declare Inertia Threat Score
(HIGH default; justify any non-HIGH with a quantified condition from this section).

SECTION 3 -- DEFEAT CONDITIONS
Given both sections above: under what specific, testable conditions do teams switch? At
least 3 conditions. Each must name a team type (not "users"), be falsifiable, and cite
at least one FM label. These are the answer to "why does inertia lose." If you cannot
write them, return to Section 1 -- the failure modes are not concrete enough yet.

SECTION 4 -- SELF-CHECK (answer each with one sentence before finalizing)
SQ-1: Is every FM scenario concrete enough to be observed without interpretation?
SQ-2: Does every switching cost carry a unit?
SQ-3: Does every defeat condition name a team type and cite an FM?
SQ-4: Would a skeptic accept each defeat condition as falsifiable?

Write artifact to: simulations/scout/inertia/{topic}-scout-inertia-{date}.md
```

---

## V-04 — Combined: Tabular Column Schema + FM Inventory Table

**Axes**: Output format (A-13) + dedicated FM inventory table (A-14)
**Hypothesis**: A-13 alone makes column gaps visible. A-14 adds a harder structural guarantee: FM-[N] identifiers are pre-assigned in a dedicated, titled table before the defeat condition table is written, making it impossible to write DC-[N] without a prior FM-[N] reference. A DC row with a blank FM Link column is a structurally visible citation violation.

```
You are running /scout:inertia for topic: {topic}.

Inertia is the primary competitor. This analysis must answer: why does inertia lose?
If evidence is absent, stop and name what is missing. A blank cell in a required column
marks an unanswered criterion -- leave it blank rather than filling it with a placeholder.

Produce the artifact in the exact section order below. The FM Inventory table is written
first and serves as the primary key for all DC-[N] citations.

SECTION 1 -- WORKAROUND PROFILE (prose, one paragraph)
Name: (a) specific workaround -- named practice or tool, not a category,
(b) role that owns it, (c) execution cadence, (d) ongoing cost with a unit.

SECTION 2 -- FM INVENTORY (write before Sections 3-5)
Title this section exactly: "FM Inventory"
Table columns: FM-[N] | Scenario | Role Affected | Trigger Condition | Failure Type | Impact
Minimum 3 rows. Assign FM-01, FM-02, FM-03 in sequence. This table is the primary key.
No FM-[N] identifier may appear in any later section unless it was first assigned here.
"Trigger Condition" must name the specific observable event, not a category. "Failure Type"
is one of: silent / visible / cascading.

SECTION 3 -- SWITCHING COST ANALYSIS
Table columns: Cost Category | Quantified Cost | Unit | Role Bearing Cost | FM-[N] Link
Minimum 2 rows. "Quantified Cost" is a number. "Unit" is required; blank Unit cells fail C-02.
"FM-[N] Link" is optional but strongly encouraged where the cost is caused by a specific FM.

SECTION 4 -- INERTIA THREAT SCORE
Declared value: HIGH / MEDIUM / LOW. Default HIGH. One-sentence justification required
for any non-HIGH. Reference at least one cost from Section 3.

SECTION 5 -- DEFEAT CONDITIONS
Table columns: DC-[N] | Condition Statement | Team Type | FM-[N] Link | Falsifiable? | Observable Evidence
Minimum 3 rows. "FM-[N] Link" must reference a valid FM-[N] from the Section 2 inventory --
free-text descriptions and blank cells both fail this column. "Team Type" names a specific
segment. "Falsifiable?" is Y or N; only Y rows count toward the C-04 minimum.

Write artifact to: simulations/scout/inertia/{topic}-scout-inertia-{date}.md
```

---

## V-05 — Combined: Tabular + FM Inventory + BRIDGE Dual-Closure

**Axes**: Output format (A-13) + FM inventory table (A-14) + BRIDGE dual-closure (A-12)
**Hypothesis**: The R7 target combination. Tabular column schema (A-13) exposes FM→actor and FM→trigger as visible column slots. FM inventory table (A-14) pre-assigns FM-[N] before any DC-[N] can cite them. BRIDGE dual-closure (A-12) adds two named structural checkpoints that must both resolve before defeat conditions are written: Q3 closes the FM→actor chain (every FM has a named role), Q4 closes the FM→trigger chain (every FM has a named observable trigger). Both chains are verifiable independently of output reading order.

```
You are running /scout:inertia for topic: {topic}.

Inertia is the primary competitor to every feature. This analysis must answer: why does
inertia lose? If evidence is absent, name what is missing and stop.

Produce the artifact using the exact section structure below. Each BRIDGE checkpoint is a
gate: proceed to the next section only after the checkpoint resolves. A blank cell in a
required column marks an unanswered criterion -- leave it blank.

SECTION 1 -- WORKAROUND PROFILE (prose, one paragraph)
Name: (a) specific workaround -- named practice or tool, not a category,
(b) role that owns it, (c) execution cadence, (d) ongoing cost with a unit.

SECTION 2 -- FM INVENTORY
Title this section exactly: "FM Inventory"
Table columns: FM-[N] | Scenario | Role Affected | Trigger Condition | Failure Type | Impact
Minimum 3 rows. Assign FM-01, FM-02, FM-03 in sequence. This is the primary key table.
No FM-[N] may appear in any later section unless assigned here first.

BRIDGE Q3 -- FM-TO-ACTOR CLOSURE
For each FM-[N] in Section 2, confirm "Role Affected" is populated with a named role --
not "users", not "teams", a role title. If any row has a blank or generic value, populate
it now before proceeding. Close with exactly one of:
  "Q3 CLOSED -- all FM-[N] actors named."
  "Q3 AMENDED -- FM-[N] actor updated: [FM identifier] -> [populated value]."
Do not proceed to Section 3 until Q3 is closed.

BRIDGE Q4 -- FM-TO-TRIGGER CLOSURE
For each FM-[N] in Section 2, confirm "Trigger Condition" names the specific observable
event that causes the failure -- not "when it breaks", the actual condition. If any row
has a vague or blank trigger, populate it now before proceeding. Close with exactly one of:
  "Q4 CLOSED -- all FM-[N] triggers named."
  "Q4 AMENDED -- FM-[N] trigger updated: [FM identifier] -> [populated value]."
Do not proceed to Section 3 until Q4 is closed.

SECTION 3 -- SWITCHING COST ANALYSIS
Table columns: Cost Category | Quantified Cost | Unit | Role Bearing Cost | FM-[N] Link
Minimum 2 rows. "Unit" is required on every row. "FM-[N] Link" is optional but encouraged.

SECTION 4 -- INERTIA THREAT SCORE
Declared value: HIGH / MEDIUM / LOW. Default HIGH. Justify any non-HIGH with a quantified
condition from Section 3.

SECTION 5 -- DEFEAT CONDITIONS
Table columns: DC-[N] | Condition Statement | Team Type | FM-[N] Link | Falsifiable? | Observable Evidence
Minimum 3 rows. "FM-[N] Link" must reference a valid FM-[N] from Section 2 -- blank cells
and free-text descriptions both fail. "Falsifiable?" is Y or N; only Y rows count.

SECTION 6 -- COMPLETENESS CHECKLIST
Binary checklist. Mark each [ ] or [x]:
[ ] C-01: Workaround named with specific practice, role, and unit cost
[ ] C-02: At least 2 switching costs with quantified units
[ ] C-03: Inertia Threat Score declared
[ ] C-04: At least 3 defeat conditions with Falsifiable? = Y
[ ] C-05: At least 3 FM-[N] rows in FM Inventory
[ ] Q3: FM-to-actor chain closed (all FM-[N] have named roles)
[ ] Q4: FM-to-trigger chain closed (all FM-[N] have named observable triggers)
[ ] DC citations: every DC-[N] row cites a valid FM-[N] from Section 2

Write artifact to: simulations/scout/inertia/{topic}-scout-inertia-{date}.md
```

---

## Variation Summary

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| Role sequence enforced | FM first | -- | -- | -- | -- |
| Tabular column schema (A-13) | -- | yes | -- | yes | yes |
| FM Inventory as titled table (A-14) | -- | -- | -- | yes | yes |
| BRIDGE Q3 FM→actor (A-12a) | -- | -- | -- | -- | yes |
| BRIDGE Q4 FM→trigger (A-12b) | -- | -- | -- | -- | yes |
| Fail-first structural position (A-10) | -- | -- | yes | -- | -- |
| Trailing completeness checklist (A-15) | -- | -- | partial | -- | yes |
| Per-criterion embedded prompts (A-11) | -- | -- | yes | -- | -- |
| FM-[N] as primary key for DC citations | -- | -- | -- | yes | yes |

**R7 target** is V-05. **Structural simplest** is V-02 or V-03 for baseline comparison. V-04 is the stepping stone to V-05 — if V-04 fails A-12 again (as R6 uniformly did), V-05 makes the bridge checkpoints impossible to skip.
