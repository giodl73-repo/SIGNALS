# prove-interview -- Skill Body Variations -- R11

**Skill:** prove-interview
**Round:** 11
**Rubric version:** v11
**Date:** 2026-03-15

---

## R11 Axis Map

| Variation | Single/Combined | Axis | Hypothesis |
|-----------|----------------|------|------------|
| V-01 | Single | Margin-Boundary Column (C-31) | Adding a third column to the verdict threshold table that names the deciding evidence factor at each adjacent-level boundary closes the ambiguity left by a two-column constitutive-definition table -- adjacent levels can no longer have overlapping evidence configurations that fit both simultaneously |
| V-02 | Single | Sub-Phase Independence Gate (C-32) | Decomposing Phase 0 into named sub-phases (0A, 0B, 0C), each with its own entry and exit gate whose conditions do not overlap, makes C-32 a structural byproduct of gate completion -- satisfying 0C's exit gate (sequence + predictions) cannot satisfy 0A's exit gate (stickiness factors enumerated) |
| V-03 | Single | Output Format (Margin-Native Table) | Rendering the verdict threshold table with a required Margin column forces C-31 as a structural completion -- a table with an empty Margin cell is visibly incomplete in a way that a prose omission is not, making the margin declaration a format obligation rather than an authorial memory task |
| V-04 | Combined | Margin-Boundary Column + Sub-Phase Independence Gates + Lifecycle Emphasis | Both new criteria as exit gate conditions: the 0B sub-phase exit gate requires the margin column to be populated, and the 0A/0B/0C decomposition enforces C-32 architecturally -- neither criterion can be satisfied by the other sub-phase's gate |
| V-05 | Combined | Full Apparatus -- C-31 Margins + C-32 Sub-Phase Independence + All C-26/27/28/29/30 from R10 | The maximal variation: R10 V-05's full apparatus extended with the margin-definition column in Phase 0B (C-31) and explicit per-sub-phase entry/exit gates with non-overlapping scope declarations (C-32) -- all seven late-aspirational criteria satisfied by architectural consequence |

Single-axis variations: V-01 (margin-boundary column), V-02 (sub-phase independence gate), V-03 (output format)
Combination variations: V-04 (C-31 + C-32 + lifecycle), V-05 (all seven late-aspirational criteria)

New R11 territory probed:
- **Margin-boundary column** (V-01, V-03, V-04, V-05): each adjacent-level pair in the verdict threshold table carries a deciding-factor declaration -- what evidence configuration tips the classification from one level to the neighbor, not just what the central case of each level looks like
- **Sub-phase independence gates** (V-02, V-04, V-05): Phase 0 decomposed so that 0A, 0B, and 0C each carry independent entry and exit gates whose scope conditions are mutually exclusive -- satisfying one sub-phase's gate is architecturally prohibited from satisfying another's
- **C-31 as 0B gate condition** (V-04, V-05): the margin column is an exit gate requirement for Phase 0B -- without margin definitions, 0B does not pass
- **C-32 as scope-separation enforcement** (V-02, V-04, V-05): each sub-phase's exit gate names criteria that are explicitly out of scope for every other sub-phase, making overlap mechanically verifiable

---

## V-01 -- Margin-Boundary Column (C-31 focus)

**Variation axis:** Margin-Boundary Column
**Hypothesis:** R10's V-01 required a constitutive threshold definition for each verdict level -- what evidence configuration produces STRONG VALIDATION vs VALIDATION vs MIXED etc. That two-column table satisfies C-29 but leaves adjacent levels potentially overlapping: a piece of evidence might technically satisfy both VALIDATION's definition and MIXED's. When the table requires a third column declaring the deciding factor at each adjacent-level boundary -- what specifically tips the verdict from one level to its neighbor -- the ambiguity closes. C-31 is satisfied by completing the margin column, not by authorial care about edge cases.

---

You are running prove-interview for the topic: {topic}

Before designing any subject, complete the OPENING COMMITMENT. Both sections must pass their gates before you proceed to subject design.

---

**OPENING COMMITMENT -- Section A: Verdict Decision Function with Margin Definitions**

This section establishes the classification system as a non-overlapping decision function. Each level must carry two declarations: (1) the constitutive threshold -- what evidence configuration produces this classification -- and (2) the margin from its lower neighbor -- what evidence factor tips the verdict from the level below to this one. When synthesis runs, you will show which threshold row the actual evidence crossed and why the margin places it on this side rather than the adjacent one.

| Verdict level | Constitutive threshold | Margin from lower neighbor |
|---------------|------------------------|----------------------------|
| STRONG VALIDATION | [evidence configuration -- name types, tier sources, re-weighting outcomes that produce this level] | [what evidence factor tips VALIDATION to STRONG VALIDATION -- the deciding property that the VALIDATION threshold lacks] |
| VALIDATION | [evidence configuration] | [what evidence factor tips MIXED to VALIDATION -- the deciding property that distinguishes this from MIXED when evidence is ambiguous] |
| MIXED | [evidence configuration] | [what evidence factor tips INVALIDATION to MIXED -- the deciding property that the INVALIDATION threshold lacks] |
| INVALIDATION | [evidence configuration] | [what evidence factor tips STRONG INVALIDATION to INVALIDATION -- what STRONG INVALIDATION has that this does not] |
| STRONG INVALIDATION | [evidence configuration] | [baseline -- no lower neighbor; state the minimum evidence floor that distinguishes this from INVALIDATION going down] |

Replace bracketed text with {topic}-specific definitions. Rules:
- Constitutive threshold column: name evidence configurations (types, tier sources, re-weighting outcomes). A definition that restates the level name fails the exit gate.
- Margin column: name the deciding factor at the boundary between this level and its lower neighbor. A margin that restates the constitutive definition fails the exit gate -- it must name what is decisive when evidence configurations for two adjacent levels overlap.

Gate: every cell in both the Constitutive threshold and Margin columns is populated with specific, non-self-referential content before proceeding to Section B.

---

**OPENING COMMITMENT -- Section B: Signal Categories Sought**

Signal categories this interview targets: [enumerate which of RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION you need evidence for, and why each is needed for {topic}]

Gate: at least two distinct signal categories named with per-category rationale.

---

For each subject, in order (design all subjects before any transcripts):

**SUBJECT CARD**

Role: [job title and organizational position]
Prior knowledge: [what this subject has direct experience with -- specific domain and depth]
Blind spots: [what their position structurally prevents them from seeing -- not blank, not "none"]
Disposition: [expected posture toward {topic}]
Primary concern: [the one thing driving their responses]
[INCUMBENT only] Inertia baseline: [the specific current practice anchoring this subject and what makes switching costly]

**TRANSCRIPT**

[5-8 exchanges in this subject's distinct voice. Questions are anchored to the subject's declared primary concern and prior knowledge. For INCUMBENT: at least one question names the inertia baseline directly. Answers are not interchangeable across subjects.]

MOMENT: [SURPRISING or CONFIRMING] -- [state the prior expectation and how this moment confirmed it or departed from it -- tie to a specific prediction, not to general surprise]

**EVIDENCE EXTRACTION**

[3-5 items, after all transcripts are complete. Do not merge with transcript or synthesis.]

- [Evidence item] | TYPE: [RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION] | STRENGTH: [STRONG / MODERATE / WEAK] | RATIONALE: [non-blank, non-self-referential -- name what makes this item robust or fragile as evidence]

---

After all subjects and extraction:

**SYNTHESIS**

Cross-subject aggregation: name at least one convergence and one contradiction. For the contradiction, cite both subjects by name and both specific conflicting evidence items.

Inertia/adoption partition:
- INERTIA SIGNALS: [with subject names and evidence item references]
- ADOPTION SIGNALS: [with subject names and evidence item references]

Epistemic re-weighting: for each subject's declared blind spots, name which evidence items should be down-weighted and what evidence would resolve the gap.

**NET VERDICT with threshold and margin audit**

Classification: [STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION]

Threshold crossed: [name the verdict level row whose constitutive definition the actual evidence satisfies -- show which specific evidence items meet the threshold criteria]

Margin placed: [return to the Margin column. Name the deciding factor at the boundary between this level and the adjacent level below. Show why the actual evidence crosses that margin -- and why it does not reach the margin separating this level from the level above (or, for STRONG VALIDATION, why the floor is exceeded).]

---

## V-02 -- Sub-Phase Independence Gate (C-32 focus)

**Variation axis:** Sub-Phase Independence Gate
**Hypothesis:** R10's V-04 placed all Phase 0 content in a single combined phase with three sections (0-A: verdict table, 0-B: sequence blueprint, 0-C: signal categories) and a single combined exit gate. A single-phase structure allows one section's content to crowd out another's -- the verdict frame can expand into the space reserved for the sequence blueprint and both can pass a combined gate while one section's requirements were actually satisfied by the other's content. When Phase 0 is decomposed into independently-gated sub-phases -- 0A for verdict function, 0B for sequence blueprint, 0C for signal categories -- each with an exit gate that names scope conditions explicitly out-of-scope for the other sub-phases, satisfying 0B's exit gate (sequence blueprint complete) cannot logically satisfy 0A's exit gate (constitutive verdict thresholds populated). C-32 is satisfied by the gate architecture, not by authorial discipline.

---

You are running prove-interview for the topic: {topic}

Execute in named phases. Phase 0 is decomposed into three independently-gated sub-phases. Each sub-phase has its own exit gate with scope conditions that do not overlap with the other sub-phases. A sub-phase is complete only when its own exit gate passes -- completing another sub-phase does not forward-certify this one.

---

**PHASE 0A -- VERDICT DECISION FUNCTION**

Scope: this sub-phase concerns only the classification system -- verdict levels and their constitutive threshold definitions. Sequence logic, signal categories, and subject design are out of scope for this sub-phase's gate.

Entry gate: none.
Exit gate (0A only): every verdict level row carries a constitutive evidence-configuration definition naming types, tier sources, and re-weighting outcomes; no row restates the level name; the table has at least five levels; sequence blueprint content (who runs first, what contrast is maximized) is absent from this sub-phase. Completing 0B or 0C does not pass this gate.

| Verdict level | Constitutive threshold -- what evidence configuration produces this classification |
|---------------|-----------------------------------------------------------------------------------|
| STRONG VALIDATION | [evidence configuration] |
| VALIDATION | [evidence configuration] |
| MIXED | [evidence configuration] |
| INVALIDATION | [evidence configuration] |
| STRONG INVALIDATION | [evidence configuration] |

Replace bracketed text with {topic}-specific definitions. A definition that restates the level name fails this gate. A definition that incorporates sequence or signal-category content is out of scope and fails this gate.

---

**PHASE 0B -- SEQUENCE BLUEPRINT**

Scope: this sub-phase concerns only the tier sequence and the contrast rationale for each adjacency. Verdict thresholds and signal categories are out of scope for this sub-phase's gate.

Entry gate: Phase 0A exit gate passed.
Exit gate (0B only): tier sequence declared; one adjacency block per consecutive pair; each block names what the preceding tier establishes and what the following tier's departure will be measured against; a statement of what contrast is lost if the order is reversed is present for each adjacency; verdict threshold content (what evidence produces which classification level) is absent from this sub-phase. Completing 0A or 0C does not pass this gate.

Tier sequence: [list in order]

For each consecutive pair:

ADJACENCY [Tier A -> Tier B]
Tier A establishes: [what evidence, posture, or baseline Tier A's interview produces that is worth measuring Tier B's departures against]
Tier B departure measured against: [what specific signal becomes interpretable in Tier B's evidence because Tier A ran first]
Contrast lost if reversed: [one sentence -- what signal would become noise or be absent if the order were flipped]

Complete one adjacency block per consecutive pair.

---

**PHASE 0C -- SIGNAL CATEGORIES**

Scope: this sub-phase concerns only the signal categories sought and the per-tier predictions. Verdict thresholds and sequence rationale are out of scope for this sub-phase's gate.

Entry gate: Phase 0A and 0B exit gates passed.
Exit gate (0C only): signal categories enumerated with per-category rationale; one prediction block per planned subject tier; each block names expected posture, evidence anchor, confirming signal, and surprising signal; predictions are specific enough to be auditable in synthesis; verdict-level threshold content and adjacency-contrast content are absent from this sub-phase. Completing 0A or 0B does not pass this gate.

Signal categories sought: [enumerate which of RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION and why each is needed for {topic}]

For each subject tier:

TIER PREDICTION -- [tier label]
Expected posture: [specific stance -- name what they will anchor in, not merely that they will take a position]
Expected evidence anchor: [the specific concern, practice, or experience their answers will orbit]
Confirming signal: [what evidence would confirm this prediction -- name type and content]
Surprising signal: [what departure would be diagnostic -- specific enough to determine after the interview, not just "unexpected"]

---

**PHASE 1 -- SUBJECT DESIGN**

Entry gate: Phases 0A, 0B, and 0C exit gates all passed.
Exit gate: all subject card fields non-blank and specific; blind spots names a structural limitation, not a tautology; INCUMBENT inertia baseline names a specific practice; subject tier labels match the Phase 0B declared sequence.

For each subject, in the Phase 0B sequence order:

Subject tier: [matching Phase 0B sequence]
Role: [job title and organizational position]
Prior knowledge: [direct experience -- specific domain and depth]
Blind spots: [structural limitation -- not blank, not "none"]
Disposition: [expected posture toward {topic}]
Primary concern: [the one thing driving their responses]
[INCUMBENT only] Inertia baseline: [specific current practice and switching cost -- must be a named practice, not "current workflow"]

---

**PHASE 2 -- TRANSCRIPT**

Entry gate: all Phase 1 subject cards complete.
Exit gate: all transcripts complete before any extraction begins; each transcript closes with a MOMENT line that cites a Phase 0C tier prediction by content; INCUMBENT transcript contains at least one question naming the inertia baseline directly; answers are not interchangeable across subjects.

For each subject, in Phase 0B sequence order:

[5-8 exchanges in the subject's distinct voice. Questions probe the declared primary concern and prior knowledge.]

MOMENT: [SURPRISING or CONFIRMING] -- [state which Phase 0C tier prediction this moment confirms or departs from, identified by content. Where applicable, name the Phase 0B adjacency baseline that makes this moment's departure interpretable.]

---

**PHASE 3 -- EVIDENCE EXTRACTION**

Entry gate: all transcripts complete.
Exit gate: 3-5 items per subject; type, strength, and rationale present for each; rationale non-blank and non-self-referential; extraction not merged with transcript or synthesis.

For each subject:

- [Evidence item] | TYPE: [RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION] | STRENGTH: [STRONG / MODERATE / WEAK] | RATIONALE: [non-blank, non-self-referential]

---

**PHASE 4 -- SYNTHESIS**

Entry gate: all extraction complete.
Exit gate: cross-subject aggregation, inertia/adoption partition, epistemic re-weighting, sequence contrast audit, prediction delta, verdict threshold audit, and net verdict all present with content-level evidence references.

**Cross-subject aggregation**

Convergence: [finding + subject names + evidence items]
Contradiction: [both subjects by name + both specific conflicting evidence items]

**Inertia/adoption partition**

INERTIA SIGNALS: [with subject names and evidence item references]
ADOPTION SIGNALS: [with subject names and evidence item references]

**Epistemic re-weighting**

For each subject's declared blind spots: name which evidence items should be down-weighted and what evidence would resolve the gap.

**Sequence contrast audit** (closes Phase 0B)

Return to Phase 0B. For each adjacency block:
- Adjacency: [Tier A -> Tier B]
- Predicted contrast: [restate]
- Observed: [CONFIRMED / CONTRADICTED / ABSENT -- name specific evidence items or record absence]

**Prediction delta** (closes Phase 0C)

Return to Phase 0C tier predictions. For each:
- Tier: [label]
- Prediction: [restate]
- Classification: [CONFIRMED / CONTRADICTED / ABSENT / PARTIAL]
- Evidence: [specific items that determined this classification]

**Verdict threshold audit** (closes Phase 0A)

Return to Phase 0A. Name the threshold row the actual evidence satisfies:
- Classification: [level name]
- Threshold crossed: [restate the constitutive definition and show which specific evidence items meet it]
- Adjacent level considered and rejected: [name the next level's threshold and state why the evidence does not reach it -- or why the evidence exceeds the level below]

**Net verdict**

[One or two sentences. Classification must match the threshold audit above.]

---

## V-03 -- Output Format: Margin-Native Table (C-31 format axis)

**Variation axis:** Output format (Margin-Native Table)
**Hypothesis:** R10's V-03 used table-native format to force C-29 (constitutive threshold) and C-30 (sequence blueprint) as structural completions -- empty cells are visibly incomplete. R11's V-03 extends the table-native approach to the new margin-boundary requirement: the verdict threshold table carries a required Margin column with specific per-boundary instructions. A table with an empty Margin cell is visibly incomplete, making C-31 a format obligation rather than an authorial memory task. The Margin column's cell instructions also prevent self-referential entries by naming the specific property that must be declared.

---

You are running prove-interview for the topic: {topic}

All output is table-native. Every section is a named table. Complete all OPENING TABLES before designing any subject.

---

### VERDICT THRESHOLD TABLE

| Level | Evidence configuration | Margin: deciding factor at lower boundary |
|-------|------------------------|-------------------------------------------|
| STRONG VALIDATION | [name types, tier sources, re-weighting outcomes that produce this classification] | [what evidence factor tips the verdict from VALIDATION to STRONG VALIDATION -- the property that VALIDATION's configuration lacks; must be more specific than "stronger evidence"] |
| VALIDATION | [evidence configuration] | [what evidence factor tips the verdict from MIXED to VALIDATION -- the decisive property when evidence fits both descriptions; must name the boundary factor, not restate the definition] |
| MIXED | [evidence configuration] | [what evidence factor tips the verdict from INVALIDATION to MIXED -- what INVALIDATION's configuration lacks that would push it to MIXED] |
| INVALIDATION | [evidence configuration] | [what evidence factor tips the verdict from STRONG INVALIDATION to INVALIDATION -- what STRONG INVALIDATION has that tips back to INVALIDATION level] |
| STRONG INVALIDATION | [evidence configuration] | [floor: no lower neighbor; state the minimum evidence condition that distinguishes this from INVALIDATION] |

Instructions:
- Evidence configuration column: name evidence types, tier sources, and re-weighting outcomes. A cell that restates the level name fails this table's gate.
- Margin column: name the deciding factor at each lower boundary. A margin cell that restates the adjacent level's constitutive definition fails this table's gate -- it must name the factor that resolves ambiguity when evidence fits both adjacent definitions.
- All cells must be populated before proceeding to the SEQUENCE BLUEPRINT TABLE.

---

### SEQUENCE BLUEPRINT TABLE

| Position | Tier | Establishes | Measured-against | Contrast lost if reversed |
|----------|------|-------------|------------------|--------------------------|
| 1 | | [what this tier's position makes possible as a baseline or adoption frame] | [what following tiers' departures are measured against because of this tier's position] | [what signal would be uninterpretable or absent without this tier going first] |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |

Instructions:
- Add or remove rows to match your planned subject count. Minimum two rows.
- Measured-against column: reference the preceding tier's Establishes content -- what the preceding tier created that this tier is measured against.
- Contrast-lost column: name a specific signal that becomes uninterpretable without this tier's position, not a generic statement about ordering.

---

For each subject, in declared sequence order:

### SUBJECT CARD TABLE

| Field | Value |
|-------|-------|
| Tier | [matching SEQUENCE BLUEPRINT row] |
| Role | |
| Prior knowledge | |
| Blind spots | [not blank, not "none" -- name the structural limitation] |
| Disposition | |
| Primary concern | |
| Inertia baseline | [INCUMBENT only -- named practice + switching cost; "N/A" for non-incumbents] |

---

### TRANSCRIPT TABLE

| # | Question | Answer | Moment-Type | Anchor / Margin reference |
|---|----------|--------|-------------|--------------------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

Instructions:
- Moment-Type: blank for most rows. Exactly one row per subject carries SURPRISING or CONFIRMING.
- Anchor / Margin reference: for the Moment-Type row, state (a) the prior expectation, (b) the relevant SEQUENCE BLUEPRINT row that makes this departure interpretable, and (c) whether the departure is diagnostic at a margin boundary in the VERDICT THRESHOLD TABLE.
- Answer column: written in the subject's distinct voice -- not interchangeable across tiers.
- Add rows 6-8 as needed.

---

### EVIDENCE TABLE

| # | Evidence item | Type | Strength | Rationale |
|---|---------------|------|----------|-----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

Instructions:
- Type: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION
- Strength: STRONG / MODERATE / WEAK
- Rationale: non-blank, non-self-referential
- Minimum 3 rows, maximum 5

---

Repeat SUBJECT CARD TABLE + TRANSCRIPT TABLE + EVIDENCE TABLE for each subject before synthesis.

---

### CROSS-SUBJECT SYNTHESIS TABLE

| Dimension | Finding | Supporting subjects | Conflicting subjects |
|-----------|---------|--------------------|--------------------|
| Convergence | | | |
| Contradiction | | [both named + specific evidence items] | [both named + specific evidence items] |
| Dominant theme | | | |

### INERTIA/ADOPTION PARTITION TABLE

| Signal type | Item | Subject | Evidence item reference |
|------------|------|---------|------------------------|
| INERTIA | | | |
| ADOPTION | | | |

### NET VERDICT TABLE

| Classification | Threshold row crossed | Margin placed | Statement |
|---------------|-----------------------|---------------|-----------|
| [STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION] | [name the VERDICT THRESHOLD TABLE row whose evidence configuration the actual evidence satisfies] | [name the Margin column entry for the boundary between this level and the adjacent level -- show which side of the boundary the actual evidence falls on and why] | [one or two sentences] |

---

## V-04 -- Combined: Margin-Boundary Column + Sub-Phase Independence Gates + Lifecycle Emphasis

**Variation axis:** Margin-Boundary Column (C-31) + Sub-Phase Independence Gates (C-32) + Lifecycle Emphasis
**Hypothesis:** C-31 and C-32 are structurally interdependent: C-31 requires the margin column in the verdict threshold table (a 0B-scope requirement), and C-32 requires that 0B's scope is architecturally separated from 0A's scope and 0C's scope. When both criteria are exit gate conditions for their respective sub-phases -- 0A's gate requires constitutive threshold definitions (C-29 scope), 0B's gate requires both constitutive definitions and margin columns (C-29 + C-31 scope), 0C's gate requires sequence blueprint and tier predictions (C-30 + C-27 scope) -- the criteria become structural byproducts of completing the gates rather than aspirational additions. The sub-phase decomposition enforces C-32 by making each gate's scope declaration explicit and non-overlapping: the 0B gate requires margin content that 0A's gate does not check for, and 0C's gate requires sequence content that neither 0A nor 0B checks for.

---

You are running prove-interview for the topic: {topic}

Execute in named phases. Phase 0 is decomposed into three independently-gated sub-phases with non-overlapping scope. Each sub-phase has its own entry gate and exit gate. Satisfying one sub-phase's exit gate does not satisfy another's -- scope is declared per sub-phase and is mutually exclusive.

---

**PHASE 0A -- VERDICT DECISION FUNCTION**

Scope: verdict level names and constitutive threshold definitions only. Margin declarations, sequence logic, and tier predictions are out of scope. If your 0A content contains adjacency-contrast reasoning or prediction commitments, it has exceeded its scope and will fail the 0A gate.

Entry gate: none.
Exit gate (0A only): the verdict level table is present; every row carries a constitutive evidence-configuration definition naming types, tier sources, and re-weighting outcomes; no row restates the level name; no margin-boundary or sequence content is present in this sub-phase.

| Verdict level | Constitutive threshold |
|---------------|------------------------|
| STRONG VALIDATION | |
| VALIDATION | |
| MIXED | |
| INVALIDATION | |
| STRONG INVALIDATION | |

Replace bracketed text with {topic}-specific constitutive definitions. Definitions that restate the level name fail the exit gate.

---

**PHASE 0B -- VERDICT MARGINS + SEQUENCE BLUEPRINT**

Scope: margin-boundary declarations for the verdict threshold table AND the tier sequence blueprint. Constitutive threshold definitions belong to 0A (reference them, do not rewrite them here). Tier predictions belong to 0C.

Entry gate: Phase 0A exit gate passed.
Exit gate (0B only): (1) every adjacent-level boundary in the verdict threshold table carries a margin declaration naming the deciding evidence factor that tips the verdict from one level to the adjacent one; no margin cell restates the adjacent level's constitutive definition; (2) tier sequence declared with one adjacency block per consecutive pair -- each block names what the preceding tier establishes and what the following tier's departure is measured against; contrast-lost statement present for each adjacency. Constitutive threshold rewrites and tier prediction blocks are out of scope and fail this gate.

**0B-1: Verdict Margin Declarations**

For each pair of adjacent levels, declare the deciding factor at the boundary:

| Boundary | Margin -- deciding evidence factor that tips the verdict from lower to upper level |
|----------|-----------------------------------------------------------------------------------|
| STRONG INVALIDATION -> INVALIDATION | [what evidence factor tips the verdict upward -- the property STRONG INVALIDATION lacks] |
| INVALIDATION -> MIXED | [deciding factor] |
| MIXED -> VALIDATION | [deciding factor] |
| VALIDATION -> STRONG VALIDATION | [deciding factor] |

Instructions: each margin cell must name the deciding property at that boundary -- the factor that resolves ambiguity when evidence plausibly fits both adjacent levels. A margin that restates either level's constitutive definition fails this gate.

**0B-2: Sequence Blueprint**

Tier sequence: [list in order]

For each consecutive pair:

ADJACENCY [Tier A -> Tier B]
Tier A establishes: [what posture, evidence type, or baseline Tier A's interview produces]
Tier B departure measured against: [what becomes interpretable in Tier B's evidence because Tier A ran first]
Contrast lost if reversed: [one sentence]

---

**PHASE 0C -- TIER PREDICTIONS**

Scope: per-tier prediction blocks only. Verdict thresholds, margin declarations, and sequence rationale belong to 0A and 0B.

Entry gate: Phase 0B exit gate passed.
Exit gate (0C only): one prediction block per planned subject tier; each block names expected posture, evidence anchor, confirming signal, and surprising signal; predictions are specific enough to be auditable in Phase 4; verdict threshold or margin content is absent from this sub-phase; sequence adjacency content is absent (reference the 0B sequence, do not restate it).

For each planned subject tier:

TIER PREDICTION -- [tier label]
Expected posture: [specific stance -- name what they will anchor in]
Expected evidence anchor: [the specific concern, practice, or experience their answers will orbit]
Confirming signal: [what evidence would confirm this prediction -- name type and content]
Surprising signal: [what departure would be diagnostic -- specific enough to determine after the interview]

---

**PHASE 1 -- SUBJECT DESIGN**

Entry gate: Phases 0A, 0B, and 0C exit gates all passed.
Exit gate: all subject card fields non-blank and specific; blind spots names a structural limitation; INCUMBENT inertia baseline names a specific practice traceable to Phase 0B sequence; subject tier labels match the 0B declared sequence.

For each subject, in Phase 0B sequence order:

Subject tier: [matching Phase 0B sequence]
Role: [job title and organizational position]
Prior knowledge: [direct experience -- specific domain and depth]
Blind spots: [structural limitation -- not blank, not "none"]
Disposition: [expected posture toward {topic}]
Primary concern: [the one thing driving their responses]
[INCUMBENT only] Inertia baseline: [specific current practice and switching cost]

---

**PHASE 2 -- TRANSCRIPT**

Entry gate: all Phase 1 subject cards complete.
Exit gate: all transcripts complete before any extraction; each transcript closes with a MOMENT line citing a Phase 0C tier prediction by content and -- where applicable -- the Phase 0B adjacency baseline that makes the departure interpretable; INCUMBENT transcript names the inertia baseline directly in at least one question.

For each subject, in Phase 0B sequence order:

[5-8 exchanges in the subject's distinct voice. Answers not interchangeable across subjects.]

MOMENT: [SURPRISING or CONFIRMING] -- [cite the Phase 0C prediction by content; where applicable name the Phase 0B adjacency baseline that gives this departure its diagnostic value]

---

**PHASE 3 -- EVIDENCE EXTRACTION**

Entry gate: all transcripts complete.
Exit gate: 3-5 items per subject; type, strength, rationale present; rationale non-blank and non-self-referential; not merged with transcript or synthesis.

For each subject:

- [Evidence item] | TYPE: [RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION] | STRENGTH: [STRONG / MODERATE / WEAK] | RATIONALE: [non-blank, non-self-referential]

---

**PHASE 4 -- SYNTHESIS**

Entry gate: all extraction complete.
Exit gate: cross-subject aggregation, inertia/adoption partition, epistemic re-weighting, sequence contrast audit, prediction delta, verdict margin audit, and net verdict all present with content-level evidence references.

**Cross-subject aggregation**

Convergence: [finding + subject names + evidence items]
Contradiction: [both subjects by name + both specific conflicting evidence items]

**Inertia/adoption partition**

INERTIA SIGNALS: [with subject names and evidence item references]
ADOPTION SIGNALS: [with subject names and evidence item references]

**Epistemic re-weighting**

For each subject's declared blind spots: name which evidence items should be down-weighted and what evidence would resolve the gap.

**Sequence contrast audit** (closes Phase 0B-2)

Return to Phase 0B-2 adjacency blocks. For each:
- Adjacency: [Tier A -> Tier B]
- Predicted contrast: [restate]
- Observed: [CONFIRMED / CONTRADICTED / ABSENT -- name specific evidence items]

**Prediction delta** (closes Phase 0C)

Return to Phase 0C. For each tier prediction:
- Tier: [label]
- Prediction: [restate]
- Classification: [CONFIRMED / CONTRADICTED / ABSENT / PARTIAL]
- Evidence: [specific items]

**Verdict margin audit** (closes Phase 0A + 0B-1)

Return to Phase 0A for the constitutive threshold and Phase 0B-1 for the margin declaration.
- Classification: [level name]
- Threshold crossed: [restate Phase 0A constitutive definition and show which evidence items meet it]
- Margin placed: [return to Phase 0B-1. Name the boundary between this level and its neighbors. Show which side of each boundary the actual evidence falls on. State whether the margin factor that would push the verdict to the next higher level is present or absent -- and what its presence or absence implies.]

**Net verdict**

[One or two sentences. Classification must match the verdict margin audit above.]

---

## V-05 -- Combined: Full Apparatus -- C-31 Margins + C-32 Sub-Phase Independence + All C-26/27/28/29/30

**Variation axis:** Verdict thresholds + Margin definitions (C-29 + C-31) + Sub-phase independence gates (C-32) + INERTIA PROFILE (C-26) + Per-tier predictions (C-27) + PREDICTION DELTA (C-28) + Contrast-sequence blueprint (C-30)
**Hypothesis:** R10 V-05 established the three-sub-phase Phase 0 structure (0A inertia, 0B verdict function, 0C sequence + predictions) and all five late-aspirational criteria (C-26 through C-30) as architectural consequences. R11 V-05 extends this by: (1) adding the margin-definition column to Phase 0B's verdict threshold table, making C-31 an exit gate requirement alongside C-29; and (2) declaring each sub-phase's scope explicitly as mutually exclusive, with exit gate conditions that name what is out of scope -- making C-32 verifiable by gate architecture rather than inferred from content placement. All seven late-aspirational criteria (C-26 through C-32) are satisfied by structural consequence: satisfying 0A's exit gate (stickiness factors enumerated) cannot satisfy 0B's exit gate (margin column populated), and satisfying 0B's exit gate cannot satisfy 0C's exit gate (per-tier predictions specific and committed).

---

You are running prove-interview for the topic: {topic}

Execute in named phases. Each phase has an entry gate and an exit gate. Phase 0 is decomposed into three independently-gated sub-phases with mutually exclusive scope: satisfying one sub-phase's exit gate cannot satisfy another's. Do not advance past any exit gate until it passes.

---

**PHASE 0A -- INERTIA PROFILE**

Scope: status-quo practices being displaced and their stickiness factors only. Verdict-level classifications, margin declarations, sequence logic, and tier predictions are out of scope. If your 0A content contains a verdict threshold table or tier sequence, it has exceeded its scope.

Entry gate: none.
Exit gate (0A only): at least one practice row complete with at least two named stickiness factors, a switching cost estimate with one-sentence justification naming the specific cost driver, and a displacement target tier; all cells populated with specific content; no verdict threshold or sequence blueprint content present.

Before designing any subject, profile the status quo {topic} would displace:

| Practice name | Stickiness factors | Switching cost | Displacement target tier |
|---------------|--------------------|----------------|--------------------------|
| | [at least two named factors: e.g., workflow dependency, sunk investment, social proof, learned behavior, vendor lock-in] | [High / Medium / Low -- one-sentence justification naming the specific cost driver] | [which subject tier most directly embodies this practice] |

Add rows for each distinct practice displaced. These stickiness factors propagate forward: they constrain incumbent question design in Phase 2 and are audited in INERTIA PROFILE ACCOUNTING in Phase 4.

---

**PHASE 0B -- VERDICT DECISION FUNCTION WITH MARGINS**

Scope: verdict level definitions and margin-boundary declarations only. Inertia stickiness factors belong to 0A (reference them, do not redeclare them). Sequence blueprint and tier predictions belong to 0C.

Entry gate: Phase 0A exit gate passed.
Exit gate (0B only): (1) every verdict level row carries a constitutive evidence-configuration definition naming types, tier sources, and re-weighting outcomes; no row restates the level name; (2) every adjacent-level boundary row in the margin table carries a deciding-factor declaration naming the evidence property that resolves classification ambiguity at that boundary; no margin cell restates either adjacent level's constitutive definition; (3) inertia profile content and tier prediction content are absent from this sub-phase. Completing 0A or 0C does not pass this gate.

**0B-I: Constitutive Threshold Definitions**

| Verdict level | Constitutive threshold |
|---------------|------------------------|
| STRONG VALIDATION | [evidence configuration -- name types, tier sources, re-weighting outcomes] |
| VALIDATION | [evidence configuration] |
| MIXED | [evidence configuration] |
| INVALIDATION | [evidence configuration] |
| STRONG INVALIDATION | [evidence configuration] |

Replace bracketed text with {topic}-specific definitions. Definitions that restate the level name fail the exit gate.

**0B-II: Margin-Boundary Declarations**

For each pair of adjacent levels, declare the deciding factor:

| Boundary | Margin -- deciding evidence factor that tips the verdict from lower to upper level |
|----------|-----------------------------------------------------------------------------------|
| STRONG INVALIDATION -> INVALIDATION | [the property STRONG INVALIDATION lacks that, if present, would push the verdict upward; must not restate either level's constitutive definition] |
| INVALIDATION -> MIXED | [deciding factor] |
| MIXED -> VALIDATION | [deciding factor] |
| VALIDATION -> STRONG VALIDATION | [deciding factor] |

Instructions: each margin cell names the evidence property that is decisive at that boundary when evidence configurations for the two adjacent levels overlap. A margin cell that restates a constitutive definition fails the exit gate -- it must identify the boundary-resolving factor, not the central case.

---

**PHASE 0C -- SEQUENCE BLUEPRINT + TIER PREDICTIONS**

Scope: tier sequence rationale and per-tier prediction blocks only. Verdict thresholds and margin declarations belong to 0B; inertia stickiness factors belong to 0A.

Entry gate: Phase 0A and 0B exit gates passed.
Exit gate (0C only): (1) tier sequence declared; one adjacency block per consecutive pair -- each block names what the preceding tier establishes and what the following tier's departure is measured against; contrast-lost statement present per adjacency; (2) one prediction block per planned subject tier; each block names expected posture, evidence anchor, confirming signal, and surprising signal specific enough to be auditable; predictions using "may" without committed direction do not pass; verdict threshold content and inertia profile content are absent. Completing 0A or 0B does not pass this gate.

**0C-I: Sequence Blueprint**

Tier sequence: [list in order]

For each consecutive pair:

ADJACENCY [Tier A -> Tier B]
Tier A establishes: [what posture, evidence type, or baseline Tier A's interview produces that is worth measuring Tier B's departures against]
Tier B departure measured against: [what becomes interpretable in Tier B's evidence because Tier A ran first]
Contrast lost if reversed: [one sentence]

**0C-II: Tier Predictions**

For each planned subject tier:

TIER PREDICTION -- [tier label]
Expected posture: [specific stance -- name what they will anchor in; trace incumbent anchors to a named Phase 0A practice row]
Expected evidence anchor: [the specific practice, concern, or experience their answers will orbit]
Confirming signal: [what evidence would confirm this prediction -- name type and content]
Surprising signal: [what departure would be diagnostic -- specific enough to be determinable after the interview]

Complete one prediction block per tier.

---

**PHASE 1 -- SUBJECT DESIGN**

Entry gate: Phases 0A, 0B, and 0C exit gates all passed.
Exit gate: all subject card fields non-blank and specific; blind spots names a structural limitation, not a tautology; INCUMBENT's inertia anchor traces to a named Phase 0A practice row; subject tier labels match the Phase 0C sequence.

For each subject, in Phase 0C sequence order:

Subject tier: [matching Phase 0C sequence]
Role: [job title and organizational position]
Prior knowledge: [direct experience -- specific domain and depth]
Blind spots: [structural limitation -- not blank, not "none"]
Disposition: [expected posture toward {topic}]
Primary concern: [the one thing driving their responses]
[INCUMBENT only] Inertia anchor: [Phase 0A practice name and stickiness factor this subject's answers will orbit]

---

**PHASE 2 -- TRANSCRIPT**

Entry gate: all Phase 1 subject cards complete.
Exit gate: all transcripts complete before any extraction begins; each transcript closes with a MOMENT line citing a Phase 0C tier prediction by content and -- where applicable -- the relevant Phase 0C adjacency baseline; INCUMBENT transcript contains at least one question naming the declared inertia anchor directly.

For each subject, in Phase 0C sequence order:

[5-8 exchanges in the subject's distinct voice. Answers are grounded in declared prior knowledge and primary concern. Answers are not interchangeable across subjects -- register, vocabulary, and framing must be distinctly theirs.]

MOMENT: [SURPRISING or CONFIRMING] -- [state which Phase 0C tier prediction this moment confirms or departs from, identified by content. Where this moment's diagnostic value depends on a preceding tier's established baseline, name that baseline and the relevant Phase 0C adjacency block.]

---

**PHASE 3 -- EVIDENCE EXTRACTION**

Entry gate: all transcripts complete.
Exit gate: 3-5 items per subject; type, strength, rationale, and profile relevance tag present for each; rationale non-blank and non-self-referential; not merged with transcript or synthesis.

For each subject:

- [Evidence item] | TYPE: [RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION] | STRENGTH: [STRONG / MODERATE / WEAK] | RATIONALE: [non-blank, non-self-referential] | PROFILE RELEVANCE: [STICKINESS / LIMITATION / DISPLACEMENT / EXTERNAL]

PROFILE RELEVANCE tags which Phase 0A inertia profile dimension the evidence speaks to. EXTERNAL marks items outside the profile scope.

---

**PHASE 4 -- SYNTHESIS**

Entry gate: all extraction complete.
Exit gate: all seven synthesis sections present with content-level evidence references -- none may be marked "see above" or left blank.

**Cross-subject aggregation**

Convergence: [finding + subject names + evidence items]
Contradiction: [both subjects by name + both specific conflicting evidence items -- assertion without named items fails this section]

**Inertia/adoption partition**

INERTIA SIGNALS: [with subject names and evidence item references]
ADOPTION SIGNALS: [with subject names and evidence item references]

**INERTIA PROFILE ACCOUNTING** (closes Phase 0A)

Return to Phase 0A. For each declared stickiness factor:
- Confirmed: which subject? Which evidence item? Content-level reference.
- Absent: name the factor and record the absence as a finding -- not an omission.

**Epistemic re-weighting**

For each subject's declared blind spots: name which evidence items should be down-weighted and what evidence would resolve the gap.

**PREDICTION DELTA** (closes Phase 0C-II)

Return to Phase 0C tier predictions. For each prediction, classify:

Tier: [label]
Prediction: [restate from Phase 0C]
Classification: [CONFIRMED / CONTRADICTED / ABSENT / PARTIAL]
Evidence: [name specific items that determined this classification -- ABSENT must record what was predicted and did not appear]

**SEQUENCE CONTRAST AUDIT** (closes Phase 0C-I)

Return to Phase 0C adjacency blocks. For each:
- Adjacency: [Tier A -> Tier B]
- Predicted contrast: [restate]
- Observed: [CONFIRMED / CONTRADICTED / ABSENT -- name specific evidence items or record absence]

**VERDICT MARGIN AUDIT** (closes Phase 0B)

Return to Phase 0B-I for constitutive thresholds and Phase 0B-II for margin declarations.

Classification: [level name]
Threshold crossed: [restate the Phase 0B-I constitutive definition and show which specific evidence items meet it]
Margin placed: [return to Phase 0B-II. For the boundary between this classification and the level above: name the margin factor and state whether the actual evidence satisfies it (determining whether the verdict reaches the higher level). For the boundary between this classification and the level below: name the margin factor and state whether the actual evidence satisfies it (confirming the verdict exceeds the lower level). Both boundary placements must be stated.]

**Net verdict**

[One or two sentences. Classification must match the VERDICT MARGIN AUDIT above.]
