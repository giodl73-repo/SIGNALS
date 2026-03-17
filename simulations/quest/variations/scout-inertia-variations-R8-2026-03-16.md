# scout-inertia — Rubric v8 Variations R8

---

## V-01 — Single axis: Output format (tabular column schema)

**Axis**: Output format — every section uses a pre-specified table template with column schema
**Hypothesis**: Pre-declared columns make FM→actor and FM→trigger visible as blank cells without requiring a full read; the FM Inventory primary key constraint stated in the table header prevents DC rows from citing unassigned FM-[N] identifiers.
**Targets**: A-13, A-14, A-16

---

You are performing an inertia competitor analysis for a software feature. The inertia competitor is the option to do nothing — teams keep their current workaround rather than adopting this feature.

Your output must answer the central question: **Why does inertia lose?** If you cannot answer that, state what information is missing and stop.

---

### SECTION 1 — FAILURE MODE INVENTORY

Complete this table **before writing anything else**. Every FM-[N] identifier used in any subsequent section must appear as a row in this table first.

> **PRIMARY KEY CONSTRAINT: No FM-[N] identifier may appear in any downstream section (including the Defeat Conditions table) unless it has an assigned row in this table. Assign FM-[N] identifiers here first. Referencing an unassigned FM-[N] elsewhere is a structural error.**

| FM-[N] | Failure Mode Description (specific, observable) | Actor — role that experiences this | Trigger — condition that causes this | Frequency | Severity |
|--------|--------------------------------------------------|-------------------------------------|--------------------------------------|-----------|----------|
| FM-01  |                                                  |                                     |                                      |           |          |
| FM-02  |                                                  |                                     |                                      |           |          |
| FM-03  |                                                  |                                     |                                      |           |          |

Rules:
- Minimum 2 rows required
- Actor must name a role (not "user" or "team")
- Trigger must name a condition (not "sometimes" or "when overloaded")
- Add rows as needed

---

### SECTION 2 — WORKAROUND PROFILE

| Field | Value |
|-------|-------|
| Workaround name (specific tool/file type/procedure name) | |
| Role that performs it | |
| Ongoing cost with unit (e.g., "2 hours/week") | |
| Tool or system involved | |
| When the workaround is invoked (trigger) | |

Describe the workaround in one paragraph. Use the values above. Do not use generic labels like "a manual process" — name the specific artifact, file format, or named step.

---

### SECTION 3 — SWITCHING COST BREAKDOWN

| Cost Category | Description | Estimate | Unit | Role Bearing the Cost |
|---------------|-------------|----------|------|-----------------------|
| Migration effort | | | | |
| Training overhead | | | | |
| Process disruption | | | | |
| In-flight work at risk | | | | |

Rules:
- At least 2 rows must be non-blank
- Every estimate must carry a unit (hours, days, dollars, incidents)
- "Significant" without a number fails

---

### SECTION 4 — INERTIA THREAT SCORE

| Field | Value |
|-------|-------|
| Threat score (HIGH / MEDIUM / LOW) | |
| Justification if not HIGH (quantified condition required) | |

Default is HIGH. Any deviation requires a quantified condition naming a threshold, percentage, or measurable state.

---

### SECTION 5 — DEFEAT CONDITIONS

> **Referential integrity rule: Every FM-[N] cited in this table must have a prior row in the FM Inventory (Section 1). Do not introduce new FM identifiers here.**

| DC-[N] | Defeat Condition (falsifiable — names a threshold or failure event) | FM Reference | Evidence or Signal |
|--------|---------------------------------------------------------------------|--------------|-------------------|
| DC-01  |                                                                     |              |                   |
| DC-02  |                                                                     |              |                   |

Rules:
- Minimum 2 rows required
- Each condition must be falsifiable ("teams switch when workaround fails on files > 10MB" passes; "teams switch when they see the value" fails)
- FM Reference must point to an assigned FM-[N] from Section 1

---

### SECTION 6 — DEFEAT NARRATIVE

In 2–3 paragraphs, explain why inertia loses. Reference at least two defeat conditions (DC-[N]) and at least two failure modes (FM-[N]) from the tables above. This is the answer to the central question.

---

### COMPLETENESS CHECK

| Criterion | Check (Y / N) |
|-----------|---------------|
| C-01: Workaround named specifically — tool/procedure name, role, ongoing cost with unit | |
| C-02: At least two switching cost categories quantified with units | |
| C-03: Inertia threat score declared HIGH / MEDIUM / LOW | |
| C-04: At least two falsifiable defeat conditions in Section 5 | |
| C-05: At least two failure modes in FM Inventory with non-blank Actor and Trigger | |

Any N must be resolved before the output is complete.

---

## V-02 — Single axis: Lifecycle emphasis (fail-first declaration)

**Axis**: Lifecycle emphasis — failure modes section is structurally first; analysis opens with what breaks before describing what exists
**Hypothesis**: Opening with "what breaks" reframes inertia as a countdown against observable failure modes rather than a defense of the status quo; C-05 is answered before any advocacy framing appears, preventing the vocabulary collision where workaround strengths crowd out failure analysis.
**Targets**: A-10

---

You are performing an inertia competitor analysis for a software feature. Inertia is the strongest competitor any feature faces. Your job is not to argue for the feature — your job is to find the cracks in inertia's armor. Start there.

**The first question is always: where does the current workaround fail?** Answer that before you describe the workaround itself.

---

### SECTION 1 — WHERE THE WORKAROUND FAILS (C-05 — answer first)

Before describing what teams currently do, identify the specific scenarios where what they currently do breaks, produces errors, causes re-work, or cannot scale.

For each failure mode, answer three things:
- What specifically goes wrong (observable outcome, not a pain point)
- Who experiences it (the named role)
- What condition triggers it

Generic pain points ("manual is slow", "it doesn't scale") do not count. Concrete failure modes do ("the CSV export silently truncates rows above 65,536 — no error is surfaced, the data-ops engineer only finds out during the downstream join").

Write at least two failure modes. Number them FM-01, FM-02, FM-03, etc.

---

### SECTION 2 — WORKAROUND PROFILE (C-01)

Now describe the current workaround specifically.

Answer these before writing:
- What is the specific name of the current workaround — not "a manual process" but the named tool, file type, export step, or scheduled job?
- Who performs it (role name)?
- What is the ongoing cost per week or sprint, with a unit?

Write one paragraph that answers all three. A response that names the specific artifact and role and states "the data-ops team spends 2 hours per week exporting and cleaning CSV files" passes. A response that says "teams use manual methods" fails on every dimension.

---

### SECTION 3 — SWITCHING COST (C-02)

Identify and quantify at least two categories of switching cost. For each cost:
- Name the category (migration effort / training overhead / process disruption / in-flight work at risk)
- State the estimate with a unit (hours, days, dollars, incidents)
- Name the role that bears it

Write this as a labeled list. Each entry must carry a number and a unit. "Significant" without a unit fails.

---

### SECTION 4 — INERTIA THREAT SCORE (C-03)

Declare an explicit inertia threat score: **HIGH**, **MEDIUM**, or **LOW**.

The default is HIGH. If you declare MEDIUM or LOW, state the specific quantified condition that justifies the deviation (a percentage, threshold, or measurable state). An output that lists switching costs without aggregating them into a declared threat level has not completed the analysis.

Inertia threat score: ___

Justification if not HIGH: ___

---

### SECTION 5 — DEFEAT CONDITIONS (C-04)

Return to the failure modes identified in Section 1. For each failure mode, ask: at what point does this failure become severe enough that teams abandon the workaround?

Identify at least two specific, distinct, testable conditions under which teams switch. Each condition must be falsifiable — it must name a threshold, a failure event, or a measurable trigger that can be observed and tested. Reference the failure mode that drives it (FM-01, FM-02, etc.).

"Teams switch when workaround fails to handle files above 10MB (FM-01)" passes.
"Teams switch when they see the value" fails.

---

### SECTION 6 — WHY INERTIA LOSES

Synthesize. In 2–3 paragraphs, explain why inertia loses this particular competition. Connect the failure modes (Section 1) to the defeat conditions (Section 5). Name the failure modes by number. Name the defeat conditions explicitly. Do not argue that the feature is good — argue that the workaround's failure modes eventually force the switch.

---

### COMPLETENESS REVIEW

Before submitting, verify:

- **C-05** (failure modes): Did you name at least two specific failure modes with an observable outcome, a named role, and a trigger condition? ___
- **C-01** (workaround): Did you name the specific workaround tool or procedure, the role, and the quantified ongoing cost with a unit? ___
- **C-02** (switching cost): Did you quantify at least two cost categories with units? ___
- **C-03** (threat score): Did you declare an explicit score (HIGH / MEDIUM / LOW)? ___
- **C-04** (defeat conditions): Did you state at least two falsifiable conditions with FM references? ___

Resolve any "no" before the output is final.

---

## V-03 — Single axis: Phrasing register (criterion-labeled question mapping)

**Axis**: Phrasing register — each section opens with a criterion-labeled embedded question; every question names its criterion ID explicitly
**Hypothesis**: Labeling each question C-01 through C-05 makes any unanswered prompt a structurally visible gap by criterion ID; an unlabeled question can be answered obliquely, but a question labeled "C-03" either has a threat score or it visibly does not.
**Targets**: A-11, A-17, A-18

---

You are running a scout-inertia analysis. Inertia is the competitor that wins by default — teams keep using what they have. Your output maps that default option: what it costs to stay, where it fails, and the specific conditions under which it stops winning.

Five criteria are essential. Every one must be answered. Each section below contains the criterion question. If you cannot answer a criterion question, state that explicitly — do not skip it.

---

### C-01 — WORKAROUND SPECIFICITY

> **[C-01] What is the specific name of the current workaround (name the tool, file format, or named procedure — not "a manual process"), who performs it (name the role), and what is the ongoing operational cost with a unit?**

Answer C-01 here.

Then write one paragraph describing the workaround in full context — when it runs, who invokes it, what artifact it produces, and what happens downstream.

---

### C-02 — SWITCHING COST QUANTIFICATION

> **[C-02] What are at least two distinct categories of switching cost (migration effort, training overhead, process disruption, in-flight work at risk), and what is the estimate for each with a unit attributed to a named role?**

Answer C-02 here. Use a labeled list. Format each item as:

- [Category]: [estimate] [unit] — borne by [role]

Every item must carry a number and a unit. "Significant cost" without a unit fails this criterion.

---

### C-03 — INERTIA THREAT SCORE

> **[C-03] What is the inertia threat score for this feature — HIGH, MEDIUM, or LOW? If not HIGH, what is the quantified condition that justifies the lower score?**

Answer C-03 here.

State the score on its own line. If MEDIUM or LOW, state the justification immediately below. An output that describes switching costs without declaring an aggregated score has not answered C-03.

Threat score: ___

---

### C-04 — DEFEAT CONDITIONS

> **[C-04] Under what specific, falsifiable conditions do teams abandon the workaround? Name at least two conditions. Each must identify a threshold, failure event, or measurable trigger — not a sentiment or general preference.**

Answer C-04 here.

Use a numbered list. For each condition, state:
1. The observable event or threshold
2. The failure mode that drives it (FM-01, FM-02, etc. — from Section C-05 below)
3. The evidence or signal that this condition is real

"Teams switch when workaround fails to process files above 10MB — FM-02 — confirmed in support tickets from Q3" passes.
"Teams switch when they see the value" fails.

---

### C-05 — WORKAROUND FAILURE MODES

> **[C-05] What are at least two specific scenarios where the current workaround breaks, produces errors, causes re-work, or cannot scale? Each failure mode must name an observable outcome, the role that experiences it, and the condition that triggers it.**

Answer C-05 here.

Assign FM-[N] identifiers. Format each as:

**FM-01**: [Observable outcome] / Actor: [role] / Trigger: [condition]

Generic pain points ("manual is slow", "doesn't scale") fail this criterion. Concrete failure modes with an observable outcome pass.

---

### SYNTHESIS — WHY INERTIA LOSES

In 2–3 paragraphs, connect the failure modes (C-05) to the defeat conditions (C-04) to explain why inertia loses. Reference FM-[N] and DC-[N] identifiers. This is the answer to the central question of the skill.

---

### COMPLETENESS CHECKLIST

| Criterion | Answered? (Y / N) |
|-----------|-------------------|
| C-01: Workaround named — specific name, role, unit cost | ☐ |
| C-02: Two or more switching costs with units attributed to roles | ☐ |
| C-03: Inertia threat score declared (HIGH / MEDIUM / LOW) | ☐ |
| C-04: Two or more falsifiable defeat conditions with FM references | ☐ |
| C-05: Two or more failure modes with observable outcome, actor, and trigger | ☐ |

Check each box. Any unchecked item requires resolution before the output is complete.

---

## V-04 — Combination: Fail-first + FM inventory table with primary key constraint

**Axis**: A-10 + A-13 + A-14 + A-16 — fail-first declaration combined with FM inventory as a dedicated named table carrying an explicit primary key constraint rule
**Hypothesis**: Fail-first ordering ensures the FM Inventory is the opening structural artifact; the primary key constraint stated in the table header prevents DC rows from citing FM-[N] identifiers that were not pre-assigned, making referential integrity a structural property rather than a review concern.
**Targets**: A-10, A-13, A-14, A-16

---

You are performing an inertia competitor analysis for a software feature. Inertia is the option to do nothing — teams keep their current workaround. Your output answers one question: **Why does inertia lose?**

Start by cataloging where the workaround fails. That is the foundation of the entire analysis.

---

### SECTION 1 — FM INVENTORY (Failure Mode Inventory)

**This table is the first artifact of the analysis.** Complete it before proceeding to any other section.

> **PRIMARY KEY RULE: FM-[N] is the primary key for this table. Every FM-[N] identifier referenced anywhere in this document — in the Defeat Conditions table, in the synthesis, in any prose — must have a corresponding row here. An FM-[N] that appears downstream without a row in this table is a referential integrity error. Assign identifiers here first.**

| FM-[N] | Failure Mode — specific, observable outcome | Actor — named role experiencing this | Trigger — condition that causes this | Frequency estimate | Severity (H/M/L) |
|--------|---------------------------------------------|--------------------------------------|--------------------------------------|-------------------|-----------------|
| FM-01  |                                             |                                      |                                      |                   |                 |
| FM-02  |                                             |                                      |                                      |                   |                 |
| FM-03  |                                             |                                      |                                      |                   |                 |

Completion rules:
- Minimum 2 rows
- Actor: a named role, not "user" or "anyone"
- Trigger: a named condition, not "sometimes" or "under load"
- Outcome: an observable event, not a feeling or frustration

Do not proceed to Section 2 until this table has at least 2 complete rows.

---

### SECTION 2 — WORKAROUND PROFILE

Answer before writing:
- What is the specific name of this workaround — the named tool, export step, file format, or scheduled procedure?
- Who performs it (role)?
- What is the ongoing operational cost with a unit?

Write one paragraph using these answers. Do not use generic labels. Name the specific artifact, format, or procedure.

---

### SECTION 3 — SWITCHING COST TABLE

| Cost Category | Description | Estimate | Unit | Role |
|---------------|-------------|----------|------|------|
| Migration effort | | | | |
| Training overhead | | | | |
| Process disruption | | | | |
| In-flight work at risk | | | | |

At least 2 rows must be non-blank. Every estimate must carry a unit. "Significant" without a number fails.

---

### SECTION 4 — INERTIA THREAT SCORE

Declare the score and close it.

Inertia threat score: [ **HIGH** / MEDIUM / LOW ]

The default is HIGH. If declaring MEDIUM or LOW, write the quantified condition immediately below — a threshold, percentage, or measurable state that justifies the deviation.

Justification (if not HIGH):

---

### SECTION 5 — DEFEAT CONDITIONS TABLE

> **Referential integrity rule: Every FM-[N] in the FM Reference column must have a prior row in the FM Inventory (Section 1). Do not introduce new FM-[N] identifiers in this table. If a defeat condition references a failure mode not yet in the inventory, return to Section 1 and add the row first.**

| DC-[N] | Defeat Condition — falsifiable, names threshold or failure event | FM Reference | Signal or Evidence |
|--------|------------------------------------------------------------------|--------------|-------------------|
| DC-01  |                                                                  |              |                   |
| DC-02  |                                                                  |              |                   |

Completion rules:
- Minimum 2 rows
- Each condition must name a threshold or event ("fails on files > 10MB" passes; "teams decide to change" fails)
- FM Reference must point to an assigned row in Section 1

---

### SECTION 6 — SYNTHESIS

In 2–3 paragraphs, explain why inertia loses. Ground the argument in specific failure modes (FM-[N]) and defeat conditions (DC-[N]) from the tables above. Reference identifiers explicitly. The argument closes when it answers: given these failure modes and these defeat conditions, what is the sequence of events that ends with teams switching?

---

### COMPLETENESS CHECK

| Criterion | Met? (Y / N) |
|-----------|--------------|
| C-01: Workaround named specifically with role and unit cost | |
| C-02: At least two switching cost categories with units | |
| C-03: Inertia threat score declared | |
| C-04: At least two falsifiable defeat conditions referencing FM-[N] from Section 1 | |
| C-05: At least two failure modes in FM Inventory with Actor and Trigger columns complete | |
| Referential integrity: no FM-[N] in DC table that lacks a Section 1 row | |

Any N requires resolution before the output is complete.

---

## V-05 — Combination: Full v8 scaffold (A-10 + A-13 + A-14 + A-16 + A-12 + A-17 + A-18)

**Axis**: Full structural scaffold — fail-first, tabular FM Inventory with primary key constraint, explicit BRIDGE artifact labels for Q3 (FM→actor) and Q4 (FM→trigger), criterion-labeled questions for all five essentials, binary trailing checklist
**Hypothesis**: This is the first variation where A-12 (BRIDGE dual-closure) has a structural scaffold that can carry it: the FM Inventory table pre-assigns FM-[N] identifiers (A-14+A-16), the Q3-BRIDGE and Q4-BRIDGE column labels explicitly name the two closure artifacts, fail-first ordering (A-10) positions them as analysis anchors rather than post-hoc decorations, and the binary trailing checklist (A-18) makes any missing coverage visible as an unchecked box.
**Targets**: A-10, A-12, A-13, A-14, A-16, A-17, A-18

---

You are performing an inertia competitor analysis for a software feature. Inertia is the default competitor — the option to do nothing, to keep the current workaround. It is the strongest competitor a feature faces because it requires no decision to win.

Your output answers one question: **Why does inertia lose?**

If you cannot answer that question, state what is missing and stop. Do not produce a partial output that looks complete.

---

### SECTION 1 — FM INVENTORY (Failure Mode Inventory) — COMPLETE FIRST

**Structural rule: This is the first section of every scout-inertia analysis. Complete it before writing any other section.**

The FM Inventory is the primary key table for this analysis.

> **PRIMARY KEY CONSTRAINT: FM-[N] is the primary key. No FM-[N] identifier may appear anywhere else in this document — not in the Defeat Conditions table, not in prose, not in any section — unless it has a row assigned here. Assign FM-[N] identifiers in this table first. Any downstream reference to an unassigned FM-[N] is a structural error.**

| FM-[N] | Failure Mode — specific, observable outcome (not a pain point) | **Q3-BRIDGE — Actor** (named role experiencing this failure) | **Q4-BRIDGE — Trigger** (condition that causes this failure) | Frequency | Severity |
|--------|----------------------------------------------------------------|--------------------------------------------------------------|-------------------------------------------------------------|-----------|----------|
| FM-01  |                                                                |                                                              |                                                             |           |          |
| FM-02  |                                                                |                                                              |                                                             |           |          |
| FM-03  |                                                                |                                                              |                                                             |           |          |

> **Q3-BRIDGE** closes the FM→Actor chain: every failure mode must have a named role as its actor. A blank Q3-BRIDGE cell means an unanchored failure mode — the analysis cannot proceed until it is filled.
>
> **Q4-BRIDGE** closes the FM→Trigger chain: every failure mode must have a named trigger condition. A blank Q4-BRIDGE cell means an unrooted failure mode — no defeat condition can be derived from it.

Completion rules:
- Minimum 2 rows required
- Q3-BRIDGE (Actor): must name a role — "data-ops engineer" passes, "user" or "team" fails
- Q4-BRIDGE (Trigger): must name a condition — "file exceeds 10MB" passes, "under load" or "sometimes" fails
- Do not proceed until both bridge columns are non-blank in at least 2 rows

---

### SECTION 2 — WORKAROUND PROFILE

> **[C-01] What is the specific name of the current workaround — not "a manual process" but the named tool, file format, export step, or scheduled procedure? Who performs it (name the role)? What is the ongoing operational cost with a unit (hours/week, dollars/sprint, incidents/month)?**

Answer C-01 here before writing the paragraph below.

Workaround name:
Role that performs it:
Ongoing cost with unit:

Expand into one paragraph using these values. Name the specific artifact or procedure. Do not use "a manual process" or "current tooling" as substitutes.

---

### SECTION 3 — SWITCHING COST BREAKDOWN

> **[C-02] What are at least two categories of switching cost — migration effort plus at least one of training overhead, process disruption, or in-flight work at risk — and what is the estimate for each with a unit attributed to a named role?**

Answer C-02 here.

| Cost Category | Description | Estimate | Unit | Role |
|---------------|-------------|----------|------|------|
| Migration effort | | | | |
| Training overhead | | | | |
| Process disruption | | | | |
| In-flight work at risk | | | | |

At least 2 rows must be non-blank with estimates and units. "Significant" without a number fails C-02.

---

### SECTION 4 — INERTIA THREAT SCORE

> **[C-03] What is the inertia threat score — HIGH, MEDIUM, or LOW? If not HIGH, what quantified condition justifies the deviation?**

Answer C-03 here.

Inertia threat score: [ HIGH / MEDIUM / LOW ]

Justification if not HIGH (quantified condition required):

Default is HIGH. Any deviation requires a named threshold or measurable state.

---

### SECTION 5 — DEFEAT CONDITIONS

> **[C-04] Under what specific, falsifiable conditions do teams abandon the workaround? Name at least two conditions. Each must identify an observable threshold or failure event, not a sentiment or general value judgment. Reference the FM-[N] that drives each condition.**

Answer C-04 here.

> **Referential integrity rule: Every FM-[N] in the FM Reference column must have an assigned row in the FM Inventory (Section 1). Do not introduce new FM-[N] identifiers here. If a defeat condition requires a new failure mode, return to Section 1, add the row with Q3-BRIDGE and Q4-BRIDGE filled, then return here.**

| DC-[N] | Defeat Condition — falsifiable, names threshold or failure event | FM Reference | Signal or Evidence |
|--------|------------------------------------------------------------------|--------------|-------------------|
| DC-01  |                                                                  |              |                   |
| DC-02  |                                                                  |              |                   |

Completion rules:
- Minimum 2 rows
- Each condition must be falsifiable (names a threshold or observable event)
- FM Reference must point to an assigned FM-[N] from Section 1

---

### SECTION 6 — FAILURE MODES IN CONTEXT (C-05 — explicit coverage)

> **[C-05] For each FM-[N] in the FM Inventory, describe the specific scenario in which the current workaround breaks, produces an error, causes re-work, or cannot scale. The scenario must be observable — something a team member would encounter and recognize.**

Answer C-05 here.

Expand each FM-[N] with one sentence of observable scenario context. If the FM Inventory has 3 rows, this section has 3 entries. Entries that restate the FM description without adding scenario context do not pass C-05.

---

### SECTION 7 — SYNTHESIS

In 2–3 paragraphs, explain why inertia loses. Anchor the argument in specific FM-[N] and DC-[N] identifiers. Connect the Q3-BRIDGE actors and Q4-BRIDGE triggers from Section 1 to the defeat conditions in Section 5 — name which role experiences which failure mode under which trigger, and which defeat condition that failure mode drives. This is the explicit closure of both bridge chains.

The synthesis is complete when it answers: given the Q3-BRIDGE actors, the Q4-BRIDGE triggers, and the DC defeat conditions, what is the specific sequence of events that ends with teams switching?

---

### COMPLETENESS CHECKLIST — BINARY FORMAT

Check each box. Y = criterion met with evidence in the output. N = not met, requires resolution before output is final.

| # | Criterion | Y / N |
|---|-----------|-------|
| C-01 | Workaround named specifically — named tool/procedure, named role, quantified ongoing cost with unit | ☐ |
| C-02 | At least two switching cost categories quantified with units attributed to named roles | ☐ |
| C-03 | Inertia threat score declared (HIGH / MEDIUM / LOW) | ☐ |
| C-04 | At least two falsifiable defeat conditions with FM-[N] references from Section 1 | ☐ |
| C-05 | At least two failure modes with observable scenario context, Q3-BRIDGE (Actor) non-blank, Q4-BRIDGE (Trigger) non-blank | ☐ |
| REF | No FM-[N] appears in any section without a prior row in FM Inventory | ☐ |
| BRIDGE | Q3-BRIDGE column is non-blank in all FM Inventory rows used in defeat conditions | ☐ |
| BRIDGE | Q4-BRIDGE column is non-blank in all FM Inventory rows used in defeat conditions | ☐ |

Any unchecked box is an unresolved structural gap. Do not submit with unchecked boxes.

---

## Variation Summary

| Variation | Axis | Primary Targets | Key Structural Feature |
|-----------|------|-----------------|------------------------|
| V-01 | Output format — tabular schema | A-13, A-14, A-16 | FM Inventory primary key constraint declared in table header; all sections table-driven |
| V-02 | Lifecycle emphasis — fail-first | A-10 | Section 1 = failure modes; prose-dominant; C-05 answered before workaround is described |
| V-03 | Phrasing register — criterion-labeled questions | A-11, A-17, A-18 | Every section opens with [C-0N] labeled question; binary trailing checklist |
| V-04 | Combination: fail-first + FM table with constraint | A-10, A-13, A-14, A-16 | FM Inventory opens analysis; primary key rule blocks downstream FM-[N] citations |
| V-05 | Combination: full v8 scaffold | A-10, A-12, A-13, A-14, A-16, A-17, A-18 | Q3-BRIDGE and Q4-BRIDGE named as column labels; binary checklist covers all 5 criteria + referential integrity |
