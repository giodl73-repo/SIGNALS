Here are the 5 complete variations for **scout-inertia Round 9**, targeting the v9 rubric's new aspirational criteria (C-27, C-28, C-29):

---

## V-01 — Constraint-before-site placement (C-27)
**Single axis.** All structural constraints extracted into a named **CONSTRAINT MANIFEST** preamble block before Section 1. Each constraint is labeled (MANIFEST-01 through MANIFEST-04) and annotates which sections it governs. A model skipping the manifest bypasses all constraints simultaneously — making the skip structurally visible rather than a silent content gap.

## V-02 — Criterion-ID-labeled verification scan (C-28)
**Single axis.** Trailing checklist uses a **VERIFICATION SCAN** table with `[C-01]` through `[C-05-INT]` ID-labeled rows. The citation-point check at Section 5 is labeled `[C-05-INT]` for traceability. A failing item names its criterion by ID — no mapping step from property description to criterion number required. Version-stable: ID labels survive rubric reformulations.

## V-03 — Manifest-bound verbatim directives (C-29)
**Single axis.** Each section opens with a **SECTION DIRECTIVE** block co-located inside the section (not in a preamble). The FM Inventory table contains the verbatim identifier reproduction directive adjacent to the canonical FM-[N] strings it governs — the model reads the directive and the reference strings in a single pass.

## V-04 — C-27 + C-28 combination
CONSTRAINT MANIFEST with labeled IDs before governed sections + criterion-ID-labeled [bracket] notation throughout + ID-labeled citation-point check at Section 5 + ID-labeled trailing scan. Three labeled enforcement opportunities, none skippable without encountering an ID-labeled rule.

## V-05 — Full integration (C-27 + C-28 + C-29 + A-10 + A-12 + A-17 + A-18 + A-19 + A-20)
The full scaffold: constraint manifest before governed sections, verbatim directives co-located inside their tables, criterion-ID labeling at both enforcement points, fail-first declaration, Q3/Q4 named bridge artifacts with `(closes C-05 -> R-02)` and `(closes C-05 -> C-04)` criterion-chain references, all five criterion questions, binary checklist, bidirectional referential integrity, inline examples in every column label.

---

Written to: `simulations/quest/variations/scout-inertia-variations-R9-2026-03-17.md`
(governs Section 5)*
> Before completing any row in the Defeat Conditions table, confirm the FM Reference column contains only FM-[N] identifiers that already have rows in Section 1. An FM-[N] not yet in Section 1 must be added there first. This constraint applies at the point of citation, not only at the point of inventory.

> **MANIFEST-03 — Unit-Bearing Estimate Rule** *(governs Section 3)*
> Every switching cost estimate in Section 3 must carry an explicit unit — hours, days, dollars, incidents per sprint. A cost stated as "significant", "substantial", or "moderate" without a number and unit fails the quantification requirement and must be revised.

> **MANIFEST-04 — Falsifiability Rule** *(governs Section 5)*
> Every defeat condition in Section 5 must be falsifiable: it names an observable threshold, failure event, or measurable trigger. A condition like "teams switch when they see the value" is not falsifiable. A condition like "teams switch when the workaround fails on inputs exceeding 10MB" is falsifiable.

---

### SECTION 1 — FAILURE MODE INVENTORY

*(Governed by MANIFEST-01 above. Assign all FM-[N] identifiers here first.)*

| FM-[N] | Failure Mode — specific, observable outcome | Actor — named role | Trigger — named condition | Frequency | Severity (H/M/L) |
|--------|---------------------------------------------|-------------------|--------------------------|-----------|-----------------|
| FM-01  |                                             |                   |                          |           |                 |
| FM-02  |                                             |                   |                          |           |                 |
| FM-03  |                                             |                   |                          |           |                 |

Rules:
- Minimum 2 rows required
- Actor: named role, not "user" or "team"
- Trigger: named condition, not "sometimes" or "when busy"
- Outcome: observable — not a pain point or feeling

Do not proceed to Section 2 until at least 2 rows are complete.

---

### SECTION 2 — WORKAROUND PROFILE

What is the specific name of this workaround — the named tool, file format, export step, or scheduled procedure? Who performs it (named role)? What is the ongoing cost with a unit?

Write one paragraph. Do not use "a manual process" or "current tooling" — name the specific artifact.

---

### SECTION 3 — SWITCHING COST BREAKDOWN

*(Governed by MANIFEST-03 above. Every estimate must carry a unit.)*

| Cost Category | Description | Estimate | Unit | Role Bearing the Cost |
|---------------|-------------|----------|------|-----------------------|
| Migration effort | | | | |
| Training overhead | | | | |
| Process disruption | | | | |
| In-flight work at risk | | | | |

At least 2 rows must be non-blank. Any estimate without a unit fails MANIFEST-03.

---

### SECTION 4 — INERTIA THREAT SCORE

Inertia threat score: [ **HIGH** / MEDIUM / LOW ]

Default is HIGH. If MEDIUM or LOW, state the quantified condition — a threshold, percentage, or measurable state — that justifies the deviation.

Justification if not HIGH:

---

### SECTION 5 — DEFEAT CONDITIONS

*(Governed by MANIFEST-01 and MANIFEST-02 above. Verify FM references before filling.)*
*(Governed by MANIFEST-04 above. Every condition must be falsifiable.)*

> **Citation-Point Check (MANIFEST-02)**: Before filling any DC row, confirm each FM Reference contains an FM-[N] with an assigned Section 1 row. Add any missing row to Section 1 before proceeding.

| DC-[N] | Defeat Condition — falsifiable, names threshold or event | FM Reference (Section 1 only) | Signal or Evidence |
|--------|----------------------------------------------------------|-------------------------------|--------------------|
| DC-01  |                                                          |                               |                    |
| DC-02  |                                                          |                               |                    |

Minimum 2 rows. Each condition falsifiable per MANIFEST-04. FM Reference from Section 1 only per MANIFEST-01.

---

### SECTION 6 — SYNTHESIS

In 2–3 paragraphs, explain why inertia loses. Reference at least two FM-[N] identifiers and at least two DC-[N] identifiers by their assigned labels. Connect the failure modes to the defeat conditions.

---

### COMPLETENESS CHECKLIST

| Criterion | Met? (Y / N) |
|-----------|--------------|
| C-01: Workaround named — specific tool/procedure, named role, unit cost | |
| C-02: At least two switching costs with units | |
| C-03: Threat score explicitly declared (HIGH / MEDIUM / LOW) | |
| C-04: At least two falsifiable defeat conditions with FM references from Section 1 | |
| C-05: At least two failure modes with Actor and Trigger non-blank | |
| MANIFEST-01: No FM-[N] used without prior Section 1 row | |
| MANIFEST-02: All DC FM references verified against Section 1 | |

Any N requires resolution before the output is complete.

---

## V-02 — Single axis: Criterion-ID-labeled verification scan (C-28)

**Axis**: Phrasing register — every item in the trailing checklist names its criterion by explicit ID; the citation-point check in Section 5 is labeled by constraint ID for traceability
**Hypothesis**: Labeling each checklist item by criterion ID converts the checklist from a list of properties into an audit path by identifier. A reviewer who finds a failure traces it to a specific criterion ID without mapping property text to criterion descriptions. After a rubric version change, ID-labeled items remain stable while property-description items may drift or match multiple criteria.
**Targets**: C-28

---

You are performing an inertia competitor analysis for a software feature. Inertia is the option to do nothing — teams keep their current workaround. Your output answers one question: **Why does inertia lose?**

---

### SECTION 1 — FAILURE MODE INVENTORY

Complete this table first. FM-[N] is the primary key for this analysis.

> **PRIMARY KEY CONSTRAINT**: No FM-[N] identifier may appear in any downstream section unless it has a row assigned here. Enforced at assignment (this table) and at citation (Section 5 check labeled C-05-INT below).

| FM-[N] | Failure Mode — specific, observable outcome | Actor — named role | Trigger — named condition | Frequency | Severity (H/M/L) |
|--------|---------------------------------------------|-------------------|--------------------------|-----------|-----------------|
| FM-01  |                                             |                   |                          |           |                 |
| FM-02  |                                             |                   |                          |           |                 |
| FM-03  |                                             |                   |                          |           |                 |

Minimum 2 rows. Actor: named role, not "user". Trigger: named condition, not "sometimes".

---

### SECTION 2 — WORKAROUND PROFILE

Name the specific workaround (tool, file format, procedure name — not "a manual process"), the role that performs it, and the ongoing cost with a unit. Write one paragraph.

---

### SECTION 3 — SWITCHING COST BREAKDOWN

| Cost Category | Description | Estimate | Unit | Role |
|---------------|-------------|----------|------|------|
| Migration effort | | | | |
| Training overhead | | | | |
| Process disruption | | | | |
| In-flight work at risk | | | | |

At least 2 rows with estimates and units. "Significant" without a number fails.

---

### SECTION 4 — INERTIA THREAT SCORE

Inertia threat score: [ HIGH / MEDIUM / LOW ]

Default is HIGH. Deviation requires a quantified justification — threshold, percentage, or measurable state.

Justification if not HIGH:

---

### SECTION 5 — DEFEAT CONDITIONS

> **[C-05-INT] citation-point integrity check**: Before completing any DC row, verify every FM Reference has an assigned Section 1 row. An unassigned FM-[N] is a [C-05-INT] violation — add the Section 1 row first. The label [C-05-INT] makes this constraint traceable by ID: a violation here traces to C-05 (failure mode inventory) without content review.

| DC-[N] | Defeat Condition — falsifiable, names threshold or event | FM Reference | Evidence |
|--------|----------------------------------------------------------|--------------|----------|
| DC-01  |                                                          |              |          |
| DC-02  |                                                          |              |          |

Minimum 2 rows. Each condition falsifiable. FM Reference from Section 1 only.

---

### SECTION 6 — SYNTHESIS

In 2–3 paragraphs, explain why inertia loses. Name FM-[N] and DC-[N] identifiers explicitly.

---

### VERIFICATION SCAN — CRITERION-ID FORMAT

Each item is labeled by criterion ID. A failing item traces directly to its criterion — no mapping step required.

| Criterion ID | Verification Step | Pass? (Y / N) |
|--------------|-------------------|---------------|
| **[C-01]** | Section 2 names the specific workaround (not "a manual process"), names the role, and quantifies ongoing cost with a unit | |
| **[C-02]** | At least two Section 3 rows have non-blank estimates with explicit units — adjective-only estimates fail [C-02] regardless of context | |
| **[C-03]** | Section 4 declares an explicit score: HIGH, MEDIUM, or LOW — stated, not implied or described elsewhere | |
| **[C-04]** | At least two Section 5 rows name an observable threshold or failure event — sentiment or general preference fails [C-04] | |
| **[C-05]** | At least two Section 1 rows have non-blank Actor (named role, not "user") and Trigger (named condition, not "sometimes") | |
| **[C-05-INT]** | Every Section 5 FM Reference has a prior Section 1 row — citation-point constraint from [C-05-INT] check above | |

Any N identifies the failing criterion by ID. Resolve before the output is final.

---

## V-03 — Single axis: Manifest-bound verbatim directive (C-29)

**Axis**: Inertia framing — structural directives for exact reproduction of identifiers are embedded inside their respective table blocks as co-located mandate statements, not declared in a separate preamble
**Hypothesis**: A directive to reproduce FM-[N] identifiers character-for-character in DC references is more reliably applied when it lives inside the FM Inventory table and the DC table — where the reference strings are visible — than in a preamble the model reads before seeing the strings. The directive and its reference strings are read in a single pass; the constraint cannot be misapplied because it cannot be read without simultaneously reading the identifiers it governs.
**Targets**: C-29

---

You are performing an inertia competitor analysis for a software feature. Inertia is the option to do nothing — teams keep their current workaround. Your output answers one question: **Why does inertia lose?**

---

### SECTION 1 — FAILURE MODE INVENTORY

> **SECTION DIRECTIVE (read before filling this table)**
> Assign FM-[N] identifiers in the first column. These identifiers are the primary keys for this entire analysis. Every FM-[N] cited anywhere downstream must reproduce the identifier from this table character-for-character: "FM-01" not "fm-01", not "Failure Mode 1", not "FM 01". The canonical identifier forms are the values you assign in the rows below — reproduce them exactly at every downstream citation. This constraint cannot be satisfied retroactively; it is established by the identifiers you write here.
>
> **PRIMARY KEY CONSTRAINT**: No FM-[N] may appear in any downstream section without an assigned row here.

| FM-[N] | Failure Mode — specific, observable outcome | Actor — named role | Trigger — named condition | Frequency | Severity (H/M/L) |
|--------|---------------------------------------------|-------------------|--------------------------|-----------|-----------------|
| FM-01  |                                             |                   |                          |           |                 |
| FM-02  |                                             |                   |                          |           |                 |
| FM-03  |                                             |                   |                          |           |                 |

Minimum 2 rows. Actor: named role. Trigger: named condition. Observable outcome only.

---

### SECTION 2 — WORKAROUND PROFILE

> **SECTION DIRECTIVE (read before filling)**
> The workaround name must be the specific tool, file format, export step, or named procedure teams use today — not "a manual process", not "current tooling". The role must be named (e.g., "data-ops engineer"), not "the team". The ongoing cost must carry a unit. Generic descriptions fail C-01.

Workaround name (specific):
Role performing it:
Ongoing cost with unit:

Write one paragraph using these values.

---

### SECTION 3 — SWITCHING COST BREAKDOWN

> **SECTION DIRECTIVE (read before filling)**
> Every estimate must carry an explicit unit. "Significant" or "moderate" without a number and unit fails C-02. At least two rows must be non-blank with estimates and units.

| Cost Category | Description | Estimate | Unit | Role |
|---------------|-------------|----------|------|------|
| Migration effort | | | | |
| Training overhead | | | | |
| Process disruption | | | | |
| In-flight work at risk | | | | |

---

### SECTION 4 — INERTIA THREAT SCORE

> **SECTION DIRECTIVE (read before filling)**
> Declare the threat score explicitly as HIGH, MEDIUM, or LOW. An output that describes switching costs without declaring a score has not answered C-03. Default is HIGH. Any deviation requires a quantified condition — not a qualitative judgment.

Inertia threat score: [ HIGH / MEDIUM / LOW ]

Justification if not HIGH (quantified condition required):

---

### SECTION 5 — DEFEAT CONDITIONS

> **SECTION DIRECTIVE (read before filling this table)**
> The FM Reference column must contain FM-[N] identifiers reproduced character-for-character from the FM Inventory in Section 1. The canonical forms are assigned there — reproduce them exactly: "FM-01" not "FM1", not "Failure Mode 1". Before filling any DC row, verify the FM-[N] you are about to cite has an assigned Section 1 row. If the defeat condition requires a failure mode not yet in Section 1, add that row first.
>
> Every defeat condition must be falsifiable: it names a threshold, event, or measurable trigger. "Teams switch when they see the value" fails. "Teams switch when workaround fails on inputs above 10MB" passes.

| DC-[N] | Defeat Condition — falsifiable, names threshold or event | FM Reference (character-for-character from Section 1) | Evidence |
|--------|----------------------------------------------------------|-------------------------------------------------------|----------|
| DC-01  |                                                          |                                                       |          |
| DC-02  |                                                          |                                                       |          |

Minimum 2 rows.

---

### SECTION 6 — SYNTHESIS

> **SECTION DIRECTIVE (read before writing)**
> Use FM-[N] and DC-[N] identifiers by their exact assigned labels. Connect failure modes to defeat conditions to explain why inertia loses. A synthesis arguing the feature is good rather than explaining the workaround's failure does not answer the central question.

In 2–3 paragraphs, explain why inertia loses.

---

### COMPLETENESS CHECKLIST

| Criterion | Verified? (Y / N) |
|-----------|-------------------|
| C-01: Named workaround (specific tool/procedure), named role, unit cost | |
| C-02: Two or more switching costs with units | |
| C-03: Threat score explicitly declared (HIGH / MEDIUM / LOW) | |
| C-04: Two or more falsifiable defeat conditions with FM references | |
| C-05: Two or more failure modes — Actor non-blank, Trigger non-blank | |
| REF: No FM-[N] used without Section 1 row | |

Any N requires resolution.

---

## V-04 — Combination: Constraint-before-site manifest + criterion-ID-labeled verification (C-27 + C-28)

**Axis**: C-27 + C-28 — preamble manifest carrying all structural constraints before governed sections, combined with criterion-ID-labeled checks at both enforcement points (manifest IDs at source, citation-point check labeled at Section 5, ID-labeled trailing checklist)
**Hypothesis**: C-27 ensures the constraint is in view before any governed section is written. C-28 labeling at both the manifest and the trailing checklist means any failure is traceable by criterion ID at both the authoring point and the review point — three ID-labeled enforcement opportunities that a model cannot bypass without encountering the ID-labeled rule.
**Targets**: C-27, C-28

---

You are performing an inertia competitor analysis for a software feature. Inertia is the option to do nothing — teams keep their current workaround. Your output answers one question: **Why does inertia lose?** If you cannot answer that, state what is missing and stop.

---

### CONSTRAINT MANIFEST

All structural constraints are declared here, before the sections they govern.

> **[C-05-SRC — FM Primary Key Constraint]** *(governs Sections 1 and 5)*
> FM-[N] is the primary key. Every FM-[N] used in any section must have an assigned Section 1 row first. Checked at assignment ([C-05-SRC] here) and re-checked at citation ([C-05-INT] at Section 5 header).

> **[C-05-INT — Citation-Point Integrity]** *(governs Section 5)*
> Before completing any Defeat Conditions row, verify the FM Reference contains only FM-[N] with prior Section 1 rows. Missing rows must be added to Section 1 first. Labeled [C-05-INT] at Section 5 for traceability.

> **[C-02-UNIT — Unit-Bearing Estimate Rule]** *(governs Section 3)*
> Every estimate must carry an explicit unit. "Significant" or "moderate" without a number and unit fails [C-02-UNIT].

> **[C-04-FALS — Falsifiability Rule]** *(governs Section 5)*
> Every defeat condition must name an observable threshold, failure event, or measurable trigger. Sentiment fails [C-04-FALS].

---

### SECTION 1 — FAILURE MODE INVENTORY

*(Governed by [C-05-SRC] in Constraint Manifest above. Assign all FM-[N] identifiers here first.)*

> **[C-05] question**: Where specifically does the current workaround fail, produce errors, cause re-work, or hit a scale ceiling? For each failure mode: what observable outcome occurs, who experiences it (named role), and what condition triggers it?

| FM-[N] | Failure Mode — specific, observable outcome (e.g., CSV export silently truncates at 65,536 rows) | Actor — named role (e.g., data-ops engineer) | Trigger — named condition (e.g., file exceeds 10MB) | Frequency | Severity (H/M/L) |
|--------|--------------------------------------------------------------------------------------------------|---------------------------------------------|-----------------------------------------------------|-----------|-----------------|
| FM-01  |                                                                                                  |                                             |                                                     |           |                 |
| FM-02  |                                                                                                  |                                             |                                                     |           |                 |
| FM-03  |                                                                                                  |                                             |                                                     |           |                 |

Minimum 2 rows. Actor: named role. Trigger: named condition. Do not proceed until at least 2 rows are complete.

---

### SECTION 2 — WORKAROUND PROFILE

> **[C-01] question**: What is the specific name of the current workaround — the named tool, file type, or procedure — not "a manual process"? Who performs it (named role)? What is the ongoing cost with a unit?

Workaround name (specific tool/procedure):
Role performing it:
Ongoing cost with unit (e.g., 2 hours/week):

Write one paragraph using these values.

---

### SECTION 3 — SWITCHING COST BREAKDOWN

*(Governed by [C-02-UNIT] in Constraint Manifest above. Every estimate must carry a unit.)*

> **[C-02] question**: What are at least two categories of switching cost — migration effort plus at least one of training overhead, process disruption, or in-flight work at risk — and what is the quantified estimate for each with a unit?

| Cost Category | Description | Estimate (e.g., 3 days) | Unit | Role |
|---------------|-------------|------------------------|------|------|
| Migration effort | | | | |
| Training overhead | | | | |
| Process disruption | | | | |
| In-flight work at risk | | | | |

At least 2 rows with estimates and units.

---

### SECTION 4 — INERTIA THREAT SCORE

> **[C-03] question**: What is the inertia threat score — HIGH, MEDIUM, or LOW? If not HIGH, what specific quantified condition justifies the deviation?

Inertia threat score: [ HIGH / MEDIUM / LOW ]

Justification if not HIGH (quantified condition required):

---

### SECTION 5 — DEFEAT CONDITIONS

*(Governed by [C-05-INT] in Constraint Manifest above.)*

> **[C-05-INT citation-point check]**: Before filling any DC row, verify each FM Reference contains only FM-[N] identifiers with prior rows in Section 1. An unassigned FM-[N] is a [C-05-INT] violation — add the row to Section 1 first.

*(Governed by [C-04-FALS] in Constraint Manifest above.)*

> **[C-04] question**: Under what specific, falsifiable conditions do teams abandon the workaround? Each condition must name an observable threshold or failure event — not a sentiment or general preference.

| DC-[N] | Defeat Condition — falsifiable, names threshold or event | FM Reference | Evidence |
|--------|----------------------------------------------------------|--------------|----------|
| DC-01  |                                                          |              |          |
| DC-02  |                                                          |              |          |

Minimum 2 rows. Each condition falsifiable per [C-04-FALS]. FM Reference from Section 1 only per [C-05-INT].

---

### SECTION 6 — SYNTHESIS

In 2–3 paragraphs, explain why inertia loses. Name FM-[N] and DC-[N] identifiers explicitly. Connect failure modes to defeat conditions.

---

### VERIFICATION SCAN — CRITERION-ID FORMAT

Each item is labeled by criterion ID. Any failing item traces directly to its criterion — no mapping step required.

| Criterion ID | Verification Step | Pass? (Y / N) |
|--------------|-------------------|---------------|
| **[C-01]** | Section 2 names the specific workaround (not "a manual process"), names the role, and quantifies ongoing cost with a unit | |
| **[C-02]** | At least two Section 3 rows have estimates with explicit units — adjective-only estimates fail [C-02] | |
| **[C-03]** | Section 4 declares an explicit score: HIGH, MEDIUM, or LOW — stated, not implied | |
| **[C-04]** | At least two Section 5 rows name observable thresholds or failure events — sentiment fails [C-04] | |
| **[C-05]** | At least two Section 1 rows have non-blank Actor (named role) and Trigger (named condition) | |
| **[C-05-SRC]** | No FM-[N] appears downstream without a prior Section 1 row — manifest constraint [C-05-SRC] | |
| **[C-05-INT]** | Every Section 5 FM Reference has a prior Section 1 row — citation-point constraint [C-05-INT] | |

Any N identifies the failing criterion by ID. Resolve before the output is final.

---

## V-05 — Full combination: C-27 + C-28 + C-29 + A-10 + A-12 + A-17 + A-18 + A-19 + A-20

**Axis**: Full integration — constraint manifest before governed sections (C-27), criterion-ID-labeled verification at both enforcement points and in trailing checklist (C-28), verbatim directives co-located inside their governing blocks (C-29), fail-first declaration (A-10), named Q3/Q4 bridge artifacts with criterion-chain references (A-12), criterion questions for all five essentials (A-17), binary trailing checklist (A-18), bidirectional referential integrity (A-19), inline examples in all column labels (A-20)
**Hypothesis**: C-27 places constraints before governed sections. C-29 places verbatim identifier directives inside their governing tables so the model reads the directive and the canonical identifier strings in a single pass. C-28 at the citation-point check and the trailing checklist creates two ID-labeled audit points. A-12 Q3/Q4 named bridge artifacts close the FM->actor and FM->trigger chains structurally. The result: no constraint placement gap, no verbatim directive placement gap, and mechanical traceability by criterion ID at every enforcement point.
**Targets**: C-27, C-28, C-29, A-10, A-12, A-17, A-18, A-19, A-20

---

You are performing an inertia competitor analysis for a software feature. Inertia is the default competitor — the option to do nothing, to keep the current workaround. It requires no decision to win.

Your output answers one question: **Why does inertia lose?**

If you cannot answer that question, state what is missing and stop. Do not produce a partial output that appears complete.

---

## [FAIL-FIRST DECLARATION]

Start with failure modes. Every defeat condition and switching cost threshold is downstream of what the current workaround breaks. Enumerate failures first; everything else follows.

This analysis has two structural bridge artifacts:
- **Q3 — FM->ACTOR BRIDGE** (closes C-05 -> R-02): Every Section 1 failure mode must have a named actor. Q3 is complete when no Actor cell is blank or generic.
- **Q4 — FM->TRIGGER BRIDGE** (closes C-05 -> C-04): Every Section 1 failure mode must have a named trigger. Q4 is complete when no Trigger cell is blank or generic. Defeat conditions in Section 5 are derived from Q4 triggers.

---

### CONSTRAINT MANIFEST

All structural constraints are declared here, before any section they govern.

> **[C-05-SRC — FM Primary Key Constraint]** *(governs Sections 1 and 5)*
> FM-[N] is the primary key for this analysis. Every FM-[N] used in any section must have an assigned Section 1 row first. Reinforced at citation point labeled [C-05-INT] at Section 5.

> **[C-05-INT — Citation-Point Integrity]** *(governs Section 5)*
> Before completing any Defeat Conditions row, verify all FM Reference values exist in Section 1. An unassigned FM-[N] requires a Section 1 row before the DC row is completed.

> **[C-02-UNIT — Unit-Bearing Estimate Rule]** *(governs Section 3)*
> Every estimate must carry an explicit unit — hours, days, dollars, incidents per sprint. Adjective-only estimates fail [C-02-UNIT].

> **[C-04-FALS — Falsifiability Rule]** *(governs Section 5)*
> Every defeat condition must name an observable threshold, failure event, or measurable trigger. Sentiment and general preference fail [C-04-FALS].

---

### SECTION 1 — FAILURE MODE INVENTORY — COMPLETE FIRST

**Structural rule**: Complete this table before any other section. This is the foundation.

> **VERBATIM IDENTIFIER DIRECTIVE** (co-located with the identifier strings it governs): FM-[N] identifiers assigned in the first column are the canonical forms for this document. All downstream references must reproduce them character-for-character — "FM-01" not "fm-01", not "FM1", not "Failure Mode 1". Read the identifier you assign in a row here; reproduce it exactly at every downstream citation. This cannot be satisfied retroactively.
>
> **[C-05-SRC]** is enforced here: assign all FM-[N] identifiers in this table. No FM-[N] may appear anywhere downstream without a row here.
>
> **Q3 — FM->ACTOR BRIDGE** (closes C-05 -> R-02): Every row must have a named Actor. A blank Actor cell means an unanchored failure mode — Q3 is not closed until all rows have named actors.
>
> **Q4 — FM->TRIGGER BRIDGE** (closes C-05 -> C-04): Every row must have a named Trigger. A blank Trigger means an unrooted failure mode — no defeat condition can be derived from it. Q4 is not closed until all rows have named triggers.

> **[C-05] question**: Where does the current workaround fail, produce errors, cause re-work, or hit a scale ceiling? For each: what observable outcome, who experiences it (named role), what condition triggers it?

| FM-[N] | Failure Mode — specific, observable outcome (e.g., CSV export silently truncates at 65,536 rows — no error surfaced) | **Q3-BRIDGE — Actor** named role (e.g., data-ops engineer) | **Q4-BRIDGE — Trigger** named condition (e.g., file exceeds 10MB) | Frequency (e.g., 2x/sprint) | Severity (H/M/L) |
|--------|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|------------------------------------------------------------------|------------------------------|-----------------|
| FM-01  |                                                                                                                      |                                                           |                                                                  |                              |                 |
| FM-02  |                                                                                                                      |                                                           |                                                                  |                              |                 |
| FM-03  |                                                                                                                      |                                                           |                                                                  |                              |                 |

Completion rules:
- Minimum 2 rows
- Q3-BRIDGE (Actor): named role — "data-ops engineer" passes, "user" or "team" fails
- Q4-BRIDGE (Trigger): named condition — "file exceeds 10MB" passes, "under load" fails
- Do not proceed until both bridge columns are non-blank in at least 2 rows

---

### Q3/Q4 BRIDGE VERIFICATION

| Bridge | Chain | Status |
|--------|-------|--------|
| Q3 — FM->ACTOR BRIDGE (closes C-05 -> R-02) | All Section 1 Actor cells non-blank with named roles | Open / Closed |
| Q4 — FM->TRIGGER BRIDGE (closes C-05 -> C-04) | All Section 1 Trigger cells non-blank with named conditions | Open / Closed |

Do not proceed until both show Closed.

---

### SECTION 2 — WORKAROUND PROFILE

> **[C-01] question**: What is the specific name of the current workaround — the named tool, file format, export step, or procedure? Not "a manual process". Who performs it (named role)? What is the ongoing cost with a unit?

Workaround name (specific — e.g., "weekly CSV export to shared drive via SFTP"):
Role performing it (e.g., "data-ops engineer"):
Ongoing cost with unit (e.g., "2 hours/week"):

Write one paragraph using these values.

---

### SECTION 3 — SWITCHING COST BREAKDOWN

*(Governed by [C-02-UNIT] in Constraint Manifest. Every estimate must carry an explicit unit.)*

> **[C-02] question**: What are at least two categories of switching cost — migration effort plus at least one of training overhead, process disruption, or in-flight work at risk — with a quantified estimate and unit for each?

| Cost Category | Description | Estimate (e.g., 3 days) | Unit (e.g., days, hours, $) | Role bearing the cost (e.g., data-ops team) |
|---------------|-------------|------------------------|-----------------------------|----------------------------------------------|
| Migration effort | | | | |
| Training overhead | | | | |
| Process disruption | | | | |
| In-flight work at risk | | | | |

At least 2 rows non-blank with estimates and units.

---

### SECTION 4 — INERTIA THREAT SCORE

> **[C-03] question**: What is the inertia threat score — HIGH, MEDIUM, or LOW? If not HIGH, what specific quantified condition justifies the deviation?

Inertia threat score: [ HIGH / MEDIUM / LOW ]

Justification if not HIGH (quantified condition — not a qualitative judgment):

Default is HIGH. Any deviation requires a named threshold or measurable state.

---

### SECTION 5 — DEFEAT CONDITIONS

*(Governed by [C-05-INT] in Constraint Manifest. Verify FM references before filling.)*
*(Governed by [C-04-FALS] in Constraint Manifest. Every condition must be falsifiable.)*

> **[C-05-INT citation-point check]** *(labeled for mechanical traceability)*: Before completing any DC row, confirm every FM Reference has a prior assigned Section 1 row. An unassigned FM-[N] is a [C-05-INT] violation — add the Section 1 row first, then return.
>
> **VERBATIM IDENTIFIER DIRECTIVE** (co-located with the FM reference strings it governs): FM Reference values must reproduce the canonical FM-[N] identifiers from Section 1 character-for-character. Read the identifier as assigned in Section 1; reproduce it exactly in the FM Reference column here.

> **[C-04] question**: Under what specific, falsifiable conditions do teams abandon the workaround? Each condition must name an observable threshold or failure event and be checkable by a reader.

| DC-[N] | Defeat Condition — falsifiable, names threshold or event (e.g., "workaround fails on files >10MB") | FM Reference (character-for-character from Section 1) | Signal or Evidence |
|--------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------|--------------------|
| DC-01  |                                                                                                     |                                                       |                    |
| DC-02  |                                                                                                     |                                                       |                    |

Minimum 2 rows. Each condition falsifiable per [C-04-FALS]. FM Reference character-for-character from Section 1 per [C-05-INT].

---

### SECTION 6 — SYNTHESIS

In 2–3 paragraphs, explain why inertia loses. Anchor the argument in FM-[N] and DC-[N] identifiers. Connect the Q3-BRIDGE actors and Q4-BRIDGE triggers from Section 1 to the defeat conditions in Section 5 — name which role experiences which failure under which trigger, and which defeat condition that failure drives. The synthesis is complete when it answers: given the Q3-BRIDGE actors, the Q4-BRIDGE triggers, and the DC defeat conditions, what is the sequence of events that ends with teams switching?

---

### VERIFICATION SCAN — CRITERION-ID FORMAT

Each item is labeled by criterion ID. Any failing item traces to its criterion without content review.

| Criterion ID | Verification Step | Pass? (Y / N) |
|--------------|-------------------|---------------|
| **[C-01]** | Section 2 names the specific workaround (not "a manual process"), names the role, quantifies ongoing cost with unit | |
| **[C-02]** | At least two Section 3 rows have estimates with explicit units — adjective-only estimates fail [C-02] | |
| **[C-03]** | Section 4 declares an explicit score: HIGH, MEDIUM, or LOW | |
| **[C-04]** | At least two Section 5 rows name observable thresholds or failure events — sentiment fails [C-04] | |
| **[C-05]** | At least two Section 1 rows have non-blank Q3-BRIDGE (named role) and Q4-BRIDGE (named condition) | |
| **[C-05-SRC]** | No FM-[N] appears downstream without a prior Section 1 row | |
| **[C-05-INT]** | Every Section 5 FM Reference has a prior Section 1 row | |
| **[Q3]** | Q3-BRIDGE column non-blank in all Section 1 rows used in Section 5 | |
| **[Q4]** | Q4-BRIDGE column non-blank in all Section 1 rows used in Section 5 | |

Any N must be resolved. The criterion ID label identifies the failing criterion without requiring content review.

---

## Variation Summary

| Variation | Axis | Primary Targets | Key Structural Feature |
|-----------|------|-----------------|------------------------|
| V-01 | Constraint manifest preamble | C-27 | CONSTRAINT MANIFEST block before all governed sections; citation-point check inline at Section 5; manifest IDs govern sections by explicit annotation |
| V-02 | Criterion-ID-labeled verification | C-28 | Trailing VERIFICATION SCAN uses [bracket] criterion IDs; citation-point check at Section 5 labeled [C-05-INT] for traceability |
| V-03 | Manifest-bound verbatim directives | C-29 | SECTION DIRECTIVE blocks inside each table; verbatim reproduction instruction inside FM Inventory adjacent to canonical identifier strings |
| V-04 | Manifest + ID-labeled scan | C-27, C-28 | Constraint manifest with labeled IDs before sections; criterion-labeled questions inside sections; ID-labeled verification scan at end |
| V-05 | Full integration | C-27, C-28, C-29, A-10, A-12, A-17, A-18, A-19, A-20 | Constraint manifest + verbatim directives co-located inside tables + ID-labeled scan at both enforcement points + Q3/Q4 bridge artifacts + fail-first + all five criterion questions + binary checklist + inline column examples |
