# draft-brainstorm Skill Prompt Variations — Round 13

**Skill:** draft-brainstorm
**Round:** 13
**Date:** 2026-03-15
**Rubric:** v12 (C-01 through C-40)
**Baseline:** R12 treats C-01 through C-39 as non-negotiable. R13 adds C-40 as formally declared.
All 5 variations must satisfy C-28 through C-40 as a baseline.

---

## R13 Axis Selection

R12 confirmed C-28 through C-39 stable. The scorecard identified two R13 targets:

- **C-27 (2-round persistent gap):** Phase 7 challenge table in R12 V-01 uses a single T-3 column
  with `(name Phase 4 dims)` as a prose instruction — anchor field labels appear inside cells,
  not in column headers. C-27 requires anchor field names to appear IN THE TABLE SCHEMA — as
  column headers or row labels — not as instructions about what to write in a single merged cell.
  Closing C-27 requires splitting T-3 into 5 anchor-named columns, or using row labels that carry
  the field names by schema.

- **C-40 (new in v12, already passed by R12 V-01):** BREACH tier labels must propagate into every
  contributing phase's exit gates and inline correction triggers. R12 V-01 achieved this; R13
  must preserve it across all 5 variations.

| Variation | Primary Axis | Novel Structural Feature |
|-----------|--------------|--------------------------|
| V-01 | Split T-3 challenge columns (C-27 direct closure) | Phase 7 table has 5 anchor-named T-3 sub-columns; Table 1B ledger updated to reference split schema |
| V-02 | Phase 1 schema declaration drives C-27 | Table 1A T-3 test pre-commits the 5 Phase 7 column labels; Phase 7 implements declared schema |
| V-03 | Phrasing register: conversational with C-27 | Descriptive register; split T-3 columns embedded naturally in prose-style phase instructions |
| V-04 | Anchor-challenge bidirectional column binding (C-27 + C-31) | Phase 4 anchor rows carry "Phase 7 Column" binding to exact column names; Phase 7 headers mirror anchor schema |
| V-05 | Full R13 stack | V-01 split columns + V-02 Phase 1 declaration + V-04 bidirectional binding + C-40 propagation + two-pass terminal audit |

---

## V-01 — Single-axis: Split T-3 Challenge Columns (C-27 Direct Closure)

**Variation axis:** Phase 7 challenge table splits the T-3 evaluation into five separate columns,
one per Do Nothing anchor field, so the anchor field labels ("T-3:Costs", "T-3:Benefits",
"T-3:Competitive Threshold", "T-3:Bypasses", "T-3:Preserves") appear as column headers in the
table schema — not as prose instructions inside a single merged cell.

**Hypothesis:** C-27 has failed two rounds because anchor field names appeared only as
instructions to include in cell content, not as structural column headers. Splitting T-3 into
five dedicated columns whose headers ARE the anchor field labels closes C-27 by making the
binding visible at the schema level. The split also makes T-3 evaluation auditable column-by-
column rather than requiring a cell to be parsed for which dims were named.

---

```
You are generating a brainstorm artifact for the topic: `{{topic}}`
Output date: `{{date}}`
Artifact path: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 1 — CHALLENGE FRAMEWORK + LEDGER BLUEPRINT + BREACH TAXONOMY
Entry: Start of session.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Declare three co-equal Phase 1 artifacts. All three must be complete before Phase 2 begins.

#### Table 1A — Challenge Framework

| ID | Test | Pass Threshold | Survival Condition |
|----|------|----------------|--------------------|
| T-1 | Differentiation | Candidate offers a meaningfully distinct mechanism from every other `**` candidate in the pool | Removing this candidate eliminates an approach not covered by the remaining 4 picks |
| T-2 | Topic Fit | Candidate's rationale names a specific dimension of `{{topic}}` — not a generic claim that applies to any topic | Rationale would fail if the topic were swapped out |
| T-3 | Inertia Displacement | Candidate is evaluated against all 5 Phase 4 anchor fields independently: Costs, Benefits, Competitive Threshold, Bypasses, Preserves. Must clear ≥3 fields with PASS. | PASS on ≥3 of the 5 anchor-named Phase 7 columns |
| T-4 | Category Coverage | Removing this `**` pick collapses the top-5 set below 3 distinct categories | Candidate's category is not represented by the other 4 picks |

Survival threshold: All four tests must PASS. A candidate clearing 3 of 4 is not a `**` pick.
Challenge framework locked after Phase 1 exit — modification is a BREACH-FATAL.

#### Table 1B — Evidence Ledger Blueprint

| Phase | Contributing Phase Name | Ledger Field Populated | Ledger Violation Condition |
|-------|------------------------|------------------------|---------------------------|
| Phase 3 | Architecture Declaration | AMEND Source column + Primary Challenge Test column on every row | Any row missing either column = ledger violation |
| Phase 4 | Do Nothing Anchor | Challenge Binding column on every anchor field row | Any anchor row missing Challenge Binding = ledger violation |
| Phase 5 | Diverge | Name + Pitch on every candidate row | Any candidate missing Name or Pitch = ledger violation |
| Phase 6 | Cluster + T-Evidence | T-Evidence column with structured notation `T-1:[v] · T-2:[v] · T-3:[dims cleared] · T-4:[v]` on every row | Blank T-Evidence cell = ledger violation |
| Phase 7 | Adversarial Challenge | Ph6 Pre-Score column + T-3 evaluated via 5 anchor-named columns (T-3:Costs, T-3:Benefits, T-3:Competitive Threshold, T-3:Bypasses, T-3:Preserves) | Missing Ph6 Pre-Score column = ledger violation; merged T-3 column (no split) = ledger violation |

#### Table 1C — BREACH Severity Taxonomy

| Severity | Definition | Correction Protocol | Continue Before Correcting? |
|----------|-----------|---------------------|-----------------------------|
| BREACH-MINOR | A required column present but missing entries for <1/3 of rows; AMEND directions overlap on one axis; threshold stated without a specific category reference; Net Position names conclusion without displacement condition | Correct the specific cells in-place. Mark corrected cells `[corrected]`. | YES — correct inline, then continue |
| BREACH-MAJOR | A required column entirely absent; concentration cap exceeded at phase exit; candidate count outside 20–40 at Phase 6 exit; fewer than 5 PASS verdicts available after Phase 7; Phase 9A Declared Severity column missing; T-3 not split into 5 anchor-named columns in Phase 7 | HALT the current phase. Reconstruct the affected table. Do not advance until full table is corrected and re-verified. | NO — halt and reconstruct |
| BREACH-FATAL | Candidates generated before Phase 1 declared; `**` marks assigned before Phase 7 completes; Do Nothing anchor entirely absent; challenge framework modified after Phase 1 lock | STOP all generation. Discard all output from the originating phase forward. Restart that phase from scratch. | NO — stop and restart |

Exit Phase 1:
- [ ] Table 1A: T-1 through T-4 with Pass Threshold and Survival Condition — BREACH-FATAL if absent
- [ ] Table 1A: T-3 explicitly names all 5 anchor fields and references 5 Phase 7 column labels — BREACH-MAJOR if anchor fields not named in T-3 pass condition
- [ ] Table 1A: Challenge framework locked
- [ ] Table 1B: 5 contributing phases; Phase 7 row explicitly references split T-3 column schema — BREACH-MAJOR if Phase 7 ledger row absent or merged-column
- [ ] Table 1C: All 3 severity tiers with Definition, Correction Protocol, Continue decision — BREACH-MAJOR if any tier missing
- [ ] Any FAIL → identify BREACH tier from Table 1C, apply per-tier protocol before Phase 2
Ledger obligation satisfied: Phase 1 framework, blueprint, BREACH taxonomy declared.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — AMEND ADJUSTMENTS
Entry: Phase 1 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write exactly 3 pool-shaping adjustments before architecture or candidates are generated.

| # | Dimension | Direction | Downstream Effect on Pool |
|---|-----------|-----------|--------------------------|
| A1 | | Expands / Narrows / Redirects | |
| A2 | | Expands / Narrows / Redirects | |
| A3 | | Expands / Narrows / Redirects | |

Rules:
- Dimension: name a specific axis — "be more creative" fails C-05
- Direction: A1, A2, A3 must pull in non-overlapping directions — if two share a direction:
  BREACH-MINOR, revise the overlapping adjustment before exit
- Downstream Effect: name specific candidate types that would surface or be displaced in
  `{{topic}}`'s context — "more options" is generic and fails C-12

Exit Phase 2:
- [ ] Exactly 3 rows; all columns filled — BREACH-MINOR if any column blank
- [ ] Directions are all distinct — if duplicate detected: BREACH-MINOR, revise before exit
- [ ] Downstream Effects are `{{topic}}`-specific — BREACH-MINOR if any is generic
- [ ] Any FAIL → identify BREACH tier from Table 1C, apply per-tier protocol before Phase 3
Ledger obligation satisfied: AMEND adjustments declared; pool-shaping committed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3 — ARCHITECTURE DECLARATION
Entry: Phase 2 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Declare category structure before generating any candidates.

| Category | Description | Target Count | % of Pool | AMEND Source | Primary Challenge Test |
|----------|-------------|--------------|-----------|--------------|------------------------|

Total: ______

Rules:
- At least 4 distinct categories
- Concentration cap: if largest category is ≥40% of total, redistribute before continuing —
  exceeding cap at phase exit is BREACH-MAJOR
- Totals must sum to 20–40
- Every row must carry AMEND Source (A1/A2/A3 or "Core") and Primary Challenge Test (T-1/T-2/T-3/T-4)
  — any row missing either column entry: BREACH-MINOR if <1/3 rows missing; BREACH-MAJOR if
  either column is entirely absent from the table
- At least 1 category must list T-3 as Primary Challenge Test — BREACH-MAJOR if absent
- Compute % of Pool inline; concentration cap must be verifiable by column value

Exit Phase 3:
- [ ] 4+ categories; % of Pool computed; no category ≥40% — BREACH-MAJOR if cap exceeded
- [ ] AMEND Source column present; every row populated — BREACH-MINOR/<1/3 missing, BREACH-MAJOR/column absent
- [ ] Primary Challenge Test column present; ≥1 row lists T-3 — BREACH-MAJOR if column absent or no T-3 row
- [ ] Totals sum to 20–40 — BREACH-MAJOR if outside range
- [ ] Any FAIL → identify BREACH tier from Table 1C, apply per-tier protocol before Phase 4
Ledger obligation satisfied: Architecture table carries AMEND Source and Primary Challenge Test.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — DO NOTHING ANCHOR
Entry: Phase 3 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write the status quo anchor after architecture is declared. Bypasses and Preserves must
reference specific Phase 3 category labels by name.

| Field | Content | Challenge Binding |
|-------|---------|-------------------|
| Costs | [specific costs of the status quo for `{{topic}}`] | T-3 |
| Benefits | [genuine appeal of continuing with current approach — why inertia is attractive] | T-3 |
| Competitive Threshold | [minimum advantage an alternative must demonstrate to displace this anchor; reference a specific Phase 3 category] | T-3 |
| Bypasses | [which Phase 3 category labels the status quo renders unnecessary — name at least 1 by label] | T-3 |
| Preserves | [what a transition from the status quo would put at risk for `{{topic}}`] | T-3 |
| Net Position | [integrated judgment: does inertia currently dominate? name the specific condition under which it stops dominating] | T-3 synthesis |

Rules:
- Costs AND Benefits must both be present with `{{topic}}`-specific content — costs-only: BREACH-MINOR
- Bypasses and Preserves must reference Phase 3 category labels by name — generic: BREACH-MINOR
- Net Position must name a displacement condition — "inertia is strong" without a condition: BREACH-MINOR
- Challenge Binding column must be present on every row — column absent: BREACH-MAJOR
- Do Nothing does NOT count toward the 20–40 candidate total

Exit Phase 4:
- [ ] All 6 field rows present with `{{topic}}`-specific content
- [ ] Costs AND Benefits both present — BREACH-MINOR if costs-only
- [ ] Competitive Threshold references a Phase 3 category — BREACH-MINOR if generic
- [ ] Bypasses and Preserves name Phase 3 category labels — BREACH-MINOR if generic
- [ ] Net Position is integrative and names a displacement condition — BREACH-MINOR if not
- [ ] Challenge Binding column present; every row populated — BREACH-MAJOR if column absent
- [ ] Any FAIL → identify BREACH tier from Table 1C, apply per-tier protocol before Phase 5
Ledger obligation satisfied: Anchor table carries Challenge Binding on every row.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5 — DIVERGE (Name + Pitch Only)
Entry: Phase 4 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Generate candidate names and one-line pitches only. Do not assign categories, rationales,
or T-Evidence yet — idea generation is separated from categorization.
Do not mark any candidate `**` — marking is deferred to Phase 7.

Output: numbered list, Name | Pitch pairs only. Target 22–38 entries.

Rules:
- No category, rationale, or T-Evidence in this phase — adding them: BREACH-MINOR, remove before exit
- If one conceptual area dominates before you finish: pause, shift angle before continuing —
  inline check against Phase 3 concentration commitments
- Any Name or Pitch left blank: BREACH-MINOR, correct before exit

Exit Phase 5:
- [ ] 22–38 Name+Pitch pairs; no categories/rationales/T-Evidence assigned — BREACH-MINOR if extra fields present
- [ ] No `**` marks — BREACH-FATAL if any `**` assigned before Phase 7
- [ ] No blank Name/Pitch cells — BREACH-MINOR if any blank
Ledger obligation satisfied: Diverge output available for cluster phase.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6 — CLUSTER + T-EVIDENCE
Entry: Phase 5 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Assign Category and Rationale to every candidate, then annotate T-Evidence.

| # | Name | Pitch | Category | Rationale | T-Evidence |
|---|------|-------|----------|-----------|------------|

T-Evidence format: `T-1:PASS/PARTIAL/FAIL · T-2:PASS/PARTIAL/FAIL · T-3:[dims cleared, e.g. Costs+Benefits] · T-4:PASS/PARTIAL/FAIL`

Rules:
- Rationale must reference a specific dimension of `{{topic}}` — generic rationale: BREACH-MINOR
- T-Evidence column must be present; blank cells: BREACH-MINOR if <1/3 rows blank,
  BREACH-MAJOR if column absent or >1/3 rows blank
- Check concentration cap on completion: if any category now exceeds 40%, redistribute
  before exiting — BREACH-MAJOR if cap exceeded at exit
- Final candidate count must be 20–40 — BREACH-MAJOR if outside range

Exit Phase 6:
- [ ] All candidates have all 4 anatomy fields — BREACH-MAJOR if any field missing
- [ ] T-Evidence column present with structured notation on every row — BREACH-MAJOR if column absent
- [ ] No category exceeds 40% — BREACH-MAJOR if cap exceeded
- [ ] Candidate count 20–40 — BREACH-MAJOR if outside range
- [ ] Any FAIL → identify BREACH tier from Table 1C, apply per-tier protocol before Phase 7
Ledger obligation satisfied: Cluster table with T-Evidence structured notation on every row.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — ADVERSARIAL CHALLENGE
Entry: Phase 6 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Identify 8–10 tentative top candidates by T-Evidence pre-score. Do NOT mark `**` yet.

Challenge table — T-3 is evaluated via 5 dedicated anchor-field columns:

| # | Candidate | Ph6 Pre-Score | T-1: Differentiation | T-2: Topic Fit | T-3: Costs | T-3: Benefits | T-3: Competitive Threshold | T-3: Bypasses | T-3: Preserves | T-4: Category Coverage | T-3 Dims Cleared | Verdict |
|---|-----------|--------------|---------------------|---------------|-----------|--------------|--------------------------|--------------|---------------|----------------------|-----------------|---------|

Rules:
- Ph6 Pre-Score: carry forward T-Evidence notation exactly from Phase 6 — column absent: BREACH-MAJOR
- T-3 anchor field columns (T-3:Costs through T-3:Preserves): each column header uses the Phase 4
  anchor field label exactly. Enter PASS / PARTIAL / FAIL for each field independently.
  Do NOT merge into a single T-3 column — merged column (no split): BREACH-MAJOR
- T-3 Dims Cleared: count how many T-3 anchor columns show PASS (e.g., "3 of 5")
- Verdict: PASS if T-1, T-2, T-4 all PASS and T-3 Dims Cleared ≥ 3; otherwise FAIL (name failing test)
- Select exactly 5 `**` candidates from PASS verdicts, spanning ≥3 categories
- If fewer than 5 PASS verdicts: BREACH-MAJOR — return to Phase 6, strengthen candidates

Exit Phase 7:
- [ ] Ph6 Pre-Score column present and populated — BREACH-MAJOR if absent
- [ ] T-3 evaluated via 5 separate anchor-named columns (Costs/Benefits/Competitive Threshold/Bypasses/Preserves) — BREACH-MAJOR if merged into single T-3 column
- [ ] T-3 column headers use Phase 4 anchor field labels exactly — BREACH-MINOR if any header renamed
- [ ] Exactly 5 PASS verdicts selected as `**` candidates spanning ≥3 categories
- [ ] No `**` marks assigned before this phase — BREACH-FATAL if any pre-assigned
- [ ] Any FAIL → identify BREACH tier from Table 1C, apply per-tier protocol
Ledger obligation satisfied: Challenge table with Ph6 Pre-Score + 5 anchor-named T-3 columns.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 8 — ARTIFACT ASSEMBLY
Entry: Phase 7 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Assemble the final artifact at: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md

Structure:
1. Header: topic, date, candidate count (20–40), `**` count (exactly 5)
2. AMEND section: A1, A2, A3 with dimension, direction, downstream effect
3. Candidate pool: grouped by category, `**` marks on exactly 5
4. Do Nothing / Status Quo section: 6-field anchor table, outside the numbered pool

Exit Phase 8:
- [ ] Artifact written to correct path
- [ ] Header, AMEND, pool, Do Nothing all present
- [ ] `**` count in artifact = 5 — BREACH-FATAL if count wrong or `**` candidates didn't pass Phase 7

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9A — TERMINAL LEDGER AUDIT
Entry: Phase 8 complete.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Audit the evidence ledger. Phase 9B may not begin until Phase 9A is complete and all rows COMPLETE.

| Phase | Ledger Field Expected | Status (COMPLETE / VIOLATION) | Declared Severity | Notes |
|-------|----------------------|-------------------------------|-------------------|-------|
| Phase 3 | AMEND Source column + Primary Challenge Test column on every row | | | |
| Phase 4 | Challenge Binding column on every anchor row | | | |
| Phase 5 | Name + Pitch on every candidate row | | | |
| Phase 6 | T-Evidence with structured notation on every row | | | |
| Phase 7 | Ph6 Pre-Score column + 5 anchor-named T-3 columns (Costs/Benefits/Competitive Threshold/Bypasses/Preserves) | | | |

Rules:
- Declared Severity: classify any VIOLATION as BREACH-MINOR, BREACH-MAJOR, or BREACH-FATAL
  using Table 1C — no violation may be recorded without a severity classification
- Apply Table 1C correction protocol for the declared severity before Phase 9B
- All rows must reach COMPLETE before Phase 9B begins

Exit Phase 9A:
- [ ] All 5 ledger rows assessed with Status and Declared Severity
- [ ] All VIOLATION rows corrected per Table 1C protocol
- [ ] Declared Severity column populated for every row (COMPLETE rows carry "N/A")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9B — CRITERION CHECKLIST
Entry: Phase 9A complete — all 5 ledger rows COMPLETE.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Row | Criterion | Status | Declared Severity if FAIL |
|-----|-----------|--------|--------------------------|
| 1 | Candidate count 20–40 (excluding Do Nothing) | PASS/FAIL | BREACH-MAJOR |
| 2 | Every candidate has all 4 anatomy fields | PASS/FAIL | BREACH-MAJOR |
| 3 | Exactly 5 `**` marks in artifact | PASS/FAIL | BREACH-MAJOR |
| 4 | Do Nothing present with 6 fields including Net Position | PASS/FAIL | BREACH-MAJOR |
| 5 | AMEND has 3 adjustments with dimension, direction, downstream effect | PASS/FAIL | BREACH-MINOR |
| 6 | Phase 3 architecture has AMEND Source column, all rows populated | PASS/FAIL | BREACH-MAJOR |
| 7 | Phase 3 architecture has Primary Challenge Test column, ≥1 row T-3 | PASS/FAIL | BREACH-MAJOR |
| 8 | Phase 6 cluster has T-Evidence with structured notation | PASS/FAIL | BREACH-MAJOR |
| 9 | Phase 7 challenge has Ph6 Pre-Score carryforward column | PASS/FAIL | BREACH-MAJOR |
| 10 | `**` candidates span ≥3 categories | PASS/FAIL | BREACH-MAJOR |
| 11 | Phase 4 anchor Challenge Binding column present; Net Position maps to T-3 synthesis | PASS/FAIL | BREACH-MAJOR |
| 12 | Table 1C BREACH taxonomy present in Phase 1 with all 3 tiers | PASS/FAIL | BREACH-FATAL |
| 13 | Phase 9A Declared Severity column populated for all audit rows | PASS/FAIL | BREACH-MAJOR |
| 14 | Phase 7 T-3 evaluated via 5 separate anchor-named columns (Costs/Benefits/Competitive Threshold/Bypasses/Preserves) | PASS/FAIL | BREACH-MAJOR |

Apply Table 1C correction protocol for every FAIL before finalizing the artifact.
```

---

## V-02 — Single-axis: Phase 1 Schema Declaration Drives C-27

**Variation axis:** Table 1A's T-3 test row pre-commits the exact column names that Phase 7 must
use for T-3 evaluation. The T-3 Pass Threshold field in Phase 1 names all 5 Phase 7 column
labels so that the challenge table schema is locked before any generation begins — not assembled
at Phase 7 time. Phase 7 is then instructed to implement the declared schema, making column
presence a Phase 1 contract rather than a Phase 7 instruction.

**Hypothesis:** R12 V-01's BREACH taxonomy in Phase 1 closed C-38 and C-40 by pre-committing
correction behavior as a contract. Applying the same logic to C-27: pre-committing the T-3
column split in Phase 1's Table 1A makes the schema a declared constraint, not an emergent
formatting choice. If Phase 7 omits a split column, it is a Phase 1 contract violation —
BREACH-MAJOR — rather than a prose-instruction miss.

---

```
You are generating a brainstorm artifact for the topic: `{{topic}}`
Output date: `{{date}}`
Artifact path: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 1 — CHALLENGE FRAMEWORK + LEDGER BLUEPRINT + BREACH TAXONOMY
Entry: Start of session.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Declare three co-equal Phase 1 artifacts. All three must be complete before Phase 2 begins.

#### Table 1A — Challenge Framework

| ID | Test | Pass Threshold | Phase 7 Column Schema | Survival Condition |
|----|------|----------------|-----------------------|--------------------|
| T-1 | Differentiation | Meaningfully distinct mechanism from every other `**` candidate | Single column: "T-1: Differentiation" | Removing this candidate eliminates an approach not covered elsewhere |
| T-2 | Topic Fit | Rationale names a specific dimension of `{{topic}}` — not generic | Single column: "T-2: Topic Fit" | Rationale fails if topic is swapped out |
| T-3 | Inertia Displacement | PASS on ≥3 of 5 anchor fields evaluated independently | **Five columns required:** "T-3: Costs" / "T-3: Benefits" / "T-3: Competitive Threshold" / "T-3: Bypasses" / "T-3: Preserves" — each column header must use this exact label | Names ≥3 of the 5 Phase 7 anchor-named columns |
| T-4 | Category Coverage | Candidate's category absent from the other 4 `**` picks | Single column: "T-4: Category Coverage" | Removing this pick collapses top-5 below 3 categories |

Survival threshold: All four tests must PASS. 3/4 is not a `**` pick.
T-3 Phase 7 column schema is LOCKED at Phase 1 exit — using a different schema is a BREACH-MAJOR.
Challenge framework locked after Phase 1 exit — modification is a BREACH-FATAL.

#### Table 1B — Evidence Ledger Blueprint

| Phase | Contributing Phase Name | Ledger Field Populated | Ledger Violation Condition |
|-------|------------------------|------------------------|---------------------------|
| Phase 3 | Architecture Declaration | AMEND Source column + Primary Challenge Test column on every row | Any row missing either column = ledger violation |
| Phase 4 | Do Nothing Anchor | Challenge Binding column on every anchor field row | Any anchor row missing Challenge Binding = ledger violation |
| Phase 5 | Diverge | Name + Pitch on every candidate row | Any candidate missing Name or Pitch = ledger violation |
| Phase 6 | Cluster + T-Evidence | T-Evidence column with structured notation `T-1:[v] · T-2:[v] · T-3:[dims cleared] · T-4:[v]` on every row | Blank T-Evidence cell = ledger violation |
| Phase 7 | Adversarial Challenge | Ph6 Pre-Score column + T-3 evaluated via the 5 locked Table 1A column names | Missing Ph6 Pre-Score or deviation from locked T-3 schema = ledger violation |

#### Table 1C — BREACH Severity Taxonomy

| Severity | Definition | Correction Protocol | Continue Before Correcting? |
|----------|-----------|---------------------|-----------------------------|
| BREACH-MINOR | A required column present but entries missing for <1/3 of rows; AMEND directions overlap on one axis; Net Position names conclusion without displacement condition | Correct specific cells in-place. Mark `[corrected]`. | YES — correct inline, then continue |
| BREACH-MAJOR | A required column entirely absent; concentration cap exceeded at phase exit; candidate count outside 20–40; fewer than 5 PASS verdicts after Phase 7; Phase 9A Declared Severity column missing; Phase 7 T-3 schema deviates from Table 1A locked schema | HALT current phase. Reconstruct affected table. Do not advance until corrected and re-verified. | NO — halt and reconstruct |
| BREACH-FATAL | Candidates generated before Phase 1 declared; `**` marks assigned before Phase 7 completes; Do Nothing anchor absent; challenge framework or T-3 schema modified after Phase 1 lock | STOP all generation. Discard output from originating phase forward. Restart from scratch. | NO — stop and restart |

Exit Phase 1:
- [ ] Table 1A: T-3 row "Phase 7 Column Schema" cell names all 5 required column labels — BREACH-MAJOR if absent
- [ ] Table 1A: T-3 schema locked — BREACH-FATAL if modified after exit
- [ ] Table 1A: T-1/T-2/T-4 schema locked with column names
- [ ] Table 1B: Phase 7 row references "5 locked Table 1A column names" — BREACH-MAJOR if absent
- [ ] Table 1C: All 3 tiers with Definition, Correction Protocol, Continue decision — BREACH-MAJOR if any tier absent
- [ ] Any FAIL → identify BREACH tier from Table 1C, apply per-tier protocol before Phase 2
Ledger obligation satisfied: Phase 1 framework, blueprint, BREACH taxonomy, T-3 column schema declared.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — AMEND ADJUSTMENTS
Entry: Phase 1 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write exactly 3 pool-shaping adjustments before architecture or candidates are generated.

| # | Dimension | Direction | Downstream Effect on Pool |
|---|-----------|-----------|--------------------------|
| A1 | | Expands / Narrows / Redirects | |
| A2 | | Expands / Narrows / Redirects | |
| A3 | | Expands / Narrows / Redirects | |

Rules:
- Dimension: name a specific axis — "be more creative" fails
- Direction: all three must differ — two sharing a direction: BREACH-MINOR, revise before exit
- Downstream Effect: name specific candidate types for `{{topic}}`'s context — generic: BREACH-MINOR

Exit Phase 2:
- [ ] Exactly 3 rows; all columns filled — BREACH-MINOR if any column blank
- [ ] Directions all distinct — BREACH-MINOR if duplicate, revise before exit
- [ ] Downstream Effects `{{topic}}`-specific — BREACH-MINOR if any generic
- [ ] Any FAIL → identify BREACH tier from Table 1C, apply per-tier protocol before Phase 3
Ledger obligation satisfied: AMEND adjustments declared.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3 — ARCHITECTURE DECLARATION
Entry: Phase 2 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Declare category structure before any candidates are generated.

| Category | Description | Target Count | % of Pool | AMEND Source | Primary Challenge Test |
|----------|-------------|--------------|-----------|--------------|------------------------|

Total: ______

Rules:
- At least 4 distinct categories
- Concentration cap ≥40% at exit: BREACH-MAJOR
- AMEND Source and Primary Challenge Test columns required on every row — BREACH-MAJOR if either
  column absent; BREACH-MINOR if <1/3 entries missing
- At least 1 category lists T-3 as Primary Challenge Test — BREACH-MAJOR if absent

Exit Phase 3:
- [ ] 4+ categories; % of Pool computed; no category ≥40%
- [ ] AMEND Source column present; every row populated
- [ ] Primary Challenge Test column present; ≥1 row T-3
- [ ] Any FAIL → identify BREACH tier, apply per-tier protocol before Phase 4
Ledger obligation satisfied: Architecture table carries AMEND Source and Primary Challenge Test.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — DO NOTHING ANCHOR
Entry: Phase 3 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write the status quo anchor after architecture is declared.

| Field | Content | Challenge Binding |
|-------|---------|-------------------|
| Costs | | T-3 |
| Benefits | | T-3 |
| Competitive Threshold | | T-3 |
| Bypasses | [name Phase 3 category labels] | T-3 |
| Preserves | | T-3 |
| Net Position | [integrated judgment + displacement condition] | T-3 synthesis |

Rules:
- All 6 rows required — BREACH-MAJOR if Challenge Binding column absent
- Bypasses/Preserves must name Phase 3 category labels — BREACH-MINOR if generic
- Net Position must name displacement condition — BREACH-MINOR if missing condition
- Costs AND Benefits both required — BREACH-MINOR if costs-only

Exit Phase 4:
- [ ] All 6 rows present with `{{topic}}`-specific content
- [ ] Challenge Binding column present — BREACH-MAJOR if absent
- [ ] Net Position integrative with named condition — BREACH-MINOR if not
- [ ] Any FAIL → identify BREACH tier, apply per-tier protocol before Phase 5
Ledger obligation satisfied: Anchor table carries Challenge Binding on every row.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5 — DIVERGE (Name + Pitch Only)
Entry: Phase 4 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Generate 22–38 Name+Pitch pairs only. No categories, rationales, or T-Evidence.
No `**` marks — deferred to Phase 7.

- Blank cells: BREACH-MINOR, correct before exit
- Extra fields added (category/rationale): BREACH-MINOR, remove before exit

Exit Phase 5:
- [ ] 22–38 pairs; no extra fields; no `**` marks
Ledger obligation satisfied: Diverge output available for cluster phase.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6 — CLUSTER + T-EVIDENCE
Entry: Phase 5 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| # | Name | Pitch | Category | Rationale | T-Evidence |
|---|------|-------|----------|-----------|------------|

T-Evidence format: `T-1:PASS/PARTIAL/FAIL · T-2:PASS/PARTIAL/FAIL · T-3:[dims cleared] · T-4:PASS/PARTIAL/FAIL`

- Generic rationale: BREACH-MINOR
- T-Evidence column absent: BREACH-MAJOR; >1/3 rows blank: BREACH-MAJOR; <1/3 blank: BREACH-MINOR
- Concentration cap exceeded at exit: BREACH-MAJOR
- Count outside 20–40 at exit: BREACH-MAJOR

Exit Phase 6:
- [ ] All candidates have 4 anatomy fields
- [ ] T-Evidence with structured notation on every row
- [ ] No category ≥40%; count 20–40
- [ ] Any FAIL → identify BREACH tier, apply per-tier protocol before Phase 7
Ledger obligation satisfied: Cluster table with T-Evidence structured notation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — ADVERSARIAL CHALLENGE
Entry: Phase 6 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Identify 8–10 top candidates. Do NOT mark `**` yet.

Implement the Table 1A locked column schema. Phase 7 table must use exactly these column labels:

| # | Candidate | Ph6 Pre-Score | T-1: Differentiation | T-2: Topic Fit | T-3: Costs | T-3: Benefits | T-3: Competitive Threshold | T-3: Bypasses | T-3: Preserves | T-4: Category Coverage | T-3 Dims Cleared | Verdict |
|---|-----------|--------------|---------------------|---------------|-----------|--------------|--------------------------|--------------|---------------|----------------------|-----------------|---------|

Rules:
- Ph6 Pre-Score: carry forward T-Evidence from Phase 6 exactly — absent: BREACH-MAJOR
- T-3 column labels must match the 5 locked names from Table 1A exactly — any deviation: BREACH-MAJOR
- Do NOT merge T-3 into a single column — merged schema violates Table 1A lock: BREACH-MAJOR
- T-3 Dims Cleared: count of PASS cells across 5 T-3 columns
- Verdict: PASS if T-1+T-2+T-4 all PASS and T-3 Dims Cleared ≥ 3; else FAIL
- Select 5 `**` candidates from PASS verdicts, spanning ≥3 categories
- Fewer than 5 PASS verdicts: BREACH-MAJOR

Exit Phase 7:
- [ ] Ph6 Pre-Score column present and populated — BREACH-MAJOR if absent
- [ ] T-3 implemented as 5 anchor-named columns matching Table 1A schema exactly — BREACH-MAJOR if merged or relabeled
- [ ] 5 `**` candidates selected from PASS verdicts spanning ≥3 categories
- [ ] No `**` assigned before Phase 7 — BREACH-FATAL if pre-assigned
- [ ] Any FAIL → identify BREACH tier, apply per-tier protocol
Ledger obligation satisfied: Challenge table implements locked Table 1A schema.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 8 — ARTIFACT ASSEMBLY
Entry: Phase 7 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Assemble artifact at: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md
Structure: Header · AMEND (A1/A2/A3) · Pool grouped by category · Do Nothing anchor table.
`**` count must equal 5. BREACH-FATAL if `**` candidates did not survive Phase 7.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9A — TERMINAL LEDGER AUDIT
Entry: Phase 8 complete. Phase 9B may not begin until all rows COMPLETE.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Phase | Ledger Field Expected | Status | Declared Severity | Notes |
|-------|----------------------|--------|-------------------|-------|
| Phase 3 | AMEND Source + Primary Challenge Test columns, every row | | | |
| Phase 4 | Challenge Binding column, every row | | | |
| Phase 5 | Name + Pitch, every candidate row | | | |
| Phase 6 | T-Evidence structured notation, every row | | | |
| Phase 7 | Ph6 Pre-Score + 5 locked T-3 anchor columns matching Table 1A schema | | | |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9B — CRITERION CHECKLIST
Entry: Phase 9A complete — all 5 rows COMPLETE.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Row | Criterion | Status | Declared Severity if FAIL |
|-----|-----------|--------|--------------------------|
| 1 | Candidate count 20–40 | PASS/FAIL | BREACH-MAJOR |
| 2 | Every candidate has all 4 anatomy fields | PASS/FAIL | BREACH-MAJOR |
| 3 | Exactly 5 `**` marks | PASS/FAIL | BREACH-MAJOR |
| 4 | Do Nothing with 6 fields including Net Position | PASS/FAIL | BREACH-MAJOR |
| 5 | AMEND 3 adjustments with dimension/direction/downstream | PASS/FAIL | BREACH-MINOR |
| 6 | Architecture AMEND Source column, all rows | PASS/FAIL | BREACH-MAJOR |
| 7 | Architecture Primary Challenge Test column, ≥1 T-3 row | PASS/FAIL | BREACH-MAJOR |
| 8 | Cluster T-Evidence structured notation | PASS/FAIL | BREACH-MAJOR |
| 9 | Phase 7 Ph6 Pre-Score carryforward column | PASS/FAIL | BREACH-MAJOR |
| 10 | `**` candidates span ≥3 categories | PASS/FAIL | BREACH-MAJOR |
| 11 | Anchor Challenge Binding column; Net Position → T-3 synthesis | PASS/FAIL | BREACH-MAJOR |
| 12 | Table 1C BREACH taxonomy in Phase 1 with all 3 tiers | PASS/FAIL | BREACH-FATAL |
| 13 | Phase 9A Declared Severity populated for all rows | PASS/FAIL | BREACH-MAJOR |
| 14 | Phase 7 T-3 schema = Table 1A locked 5-column schema | PASS/FAIL | BREACH-MAJOR |
```

---

## V-03 — Single-axis: Phrasing Register (Conversational) with C-27 Closure

**Variation axis:** Descriptive, conversational register throughout — phases explained as
"here's what you're doing and why" rather than imperative bullet commands. The C-27 closure
(split T-3 columns) is embedded naturally in descriptive phrasing rather than as a schema lock
instruction. BREACH tier labels are preserved but voiced as consequences rather than commands.

**Hypothesis:** Previous rounds have used uniform imperative register across all variations.
A conversational descriptive register may produce different compliance patterns — lower syntactic
friction may improve understanding of structural requirements like the split T-3 schema, while
potentially reducing overly rigid copy-paste behavior in edge cases. This tests whether C-27
closure survives register change.

---

```
You are generating a brainstorm artifact for the topic: `{{topic}}`
Output date: `{{date}}`
Artifact path: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md

This prompt walks you through the brainstorm in structured phases. Each phase does one job.
Read each phase fully before starting it. Don't jump ahead.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 1 — Before You Generate Anything
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Before a single idea is generated, lock three things in place. These become the rules for
everything that follows — you can't change them once this phase is done.

**The challenge framework (Table 1A).** These are the four tests every top-5 candidate must
pass. Declare them now so the pool is built against pre-stated criteria, not post-hoc
rationalization.

| ID | Test | What Passing Looks Like | How It's Checked in Phase 7 |
|----|------|------------------------|------------------------------|
| T-1 | Differentiation | The candidate offers a mechanism not present in any other `**` pick | Removing it loses a distinct angle |
| T-2 | Topic Fit | The rationale names something specific about `{{topic}}` — not a generic claim | Would fail if you swapped in a different topic |
| T-3 | Inertia Displacement | The candidate is measurably better than staying put on at least 3 of the 5 anchor fields you'll write in Phase 4 | Evaluated across 5 separate anchor-field columns in Phase 7: "T-3: Costs", "T-3: Benefits", "T-3: Competitive Threshold", "T-3: Bypasses", "T-3: Preserves" — not as a single merged column |
| T-4 | Category Coverage | The `**` set wouldn't span 3 categories without this pick | Removing it drops coverage below 3 |

T-3 note: In Phase 7 you'll use five separate columns — one for each anchor field by name. That's
what makes the evaluation structured rather than impressionistic.

All four tests must pass. Three-out-of-four is not a top-5 pick.
Lock the framework here — changing it after this phase would be BREACH-FATAL.

**The evidence ledger blueprint (Table 1B).** Each phase below contributes a specific artifact
to an evidence ledger. Record what each phase is supposed to produce so the terminal audit
can check it concretely.

| Phase | What It Contributes | How You'll Know It's There |
|-------|--------------------|-----------------------------|
| Phase 3 | Architecture table with AMEND Source and Primary Challenge Test columns, every row populated | Both columns visible in table schema; no blank rows |
| Phase 4 | Anchor table with Challenge Binding column on every field row | Column present; 6 rows all populated |
| Phase 5 | Name+Pitch pairs, no blank cells | Every row has both fields |
| Phase 6 | T-Evidence column with structured notation on every candidate row | No blank T-Evidence cells |
| Phase 7 | Ph6 Pre-Score carryforward + T-3 evaluated as 5 anchor-named columns | Ph6 column present; T-3 split into Costs/Benefits/Competitive Threshold/Bypasses/Preserves headers |

**The violation taxonomy (Table 1C).** When something goes wrong, the severity determines how
to respond. Different problems warrant different interruptions.

| Tier | What It Covers | What to Do | Can You Continue? |
|------|---------------|-----------|-------------------|
| BREACH-MINOR | Missing individual cells (not a whole column); one overlapping AMEND direction; Net Position without a displacement condition | Fix the specific cells in-place. Note them as `[corrected]`. | Yes — fix inline and keep going |
| BREACH-MAJOR | An entire required column absent from any table; concentration cap exceeded; candidate count outside 20–40; T-3 evaluated as a merged column instead of 5 anchor-named columns; fewer than 5 survivors after Phase 7 | Stop the current phase. Reconstruct the deficient table from scratch. Don't move forward until re-verified. | No — halt and fix |
| BREACH-FATAL | Any idea generated before Phase 1 complete; any `**` mark assigned before Phase 7 concludes; Do Nothing anchor missing from the artifact; challenge framework altered after Phase 1 | Stop entirely. Discard everything from the originating phase forward. Start that phase again. | No — full restart |

Check Phase 1 before moving on:
- Table 1A present with all four tests, including T-3's 5-column schema description — if T-3 column schema absent: BREACH-MAJOR
- Challenge framework and T-3 column schema locked
- Table 1B present with all 5 contributing phases
- Table 1C present with all 3 tiers and their protocols
If anything is missing, apply the appropriate tier protocol before continuing.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — Shape the Pool Before You Build It (AMEND)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

These three adjustments decide what kind of pool you'll generate. Write them now, before
architecture or ideas, so they actually shape the output rather than describe it after the fact.

| # | Dimension Being Shifted | Direction | What This Surfaces or Displaces in {{topic}}'s Context |
|---|------------------------|-----------|--------------------------------------------------------|
| A1 | | Expands / Narrows / Redirects | |
| A2 | | Expands / Narrows / Redirects | |
| A3 | | Expands / Narrows / Redirects | |

Each adjustment names a specific dimension (not "be more creative"), a direction, and a
downstream consequence for the pool. If two adjustments push in the same direction, you have a
BREACH-MINOR — revise one before moving on. Generic downstream effects ("more options") that
don't reference `{{topic}}`'s context are also BREACH-MINOR.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3 — Declare the Pool's Shape (Architecture)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Before generating ideas, commit to the categories you'll use. This prevents the pool from
drifting into whatever ideas came to mind most easily.

| Category | Description | Target Count | % of Pool | AMEND Source | Primary Challenge Test |
|----------|-------------|--------------|-----------|--------------|------------------------|

At least 4 categories. No single category should exceed 40% of the total — compute % of Pool
inline so the cap is verifiable by column value. At least one category must be there primarily
to serve T-3 (Inertia Displacement). Every row needs an AMEND Source (which adjustment drove
this category) and a Primary Challenge Test.

Missing AMEND Source or Primary Challenge Test columns entirely: BREACH-MAJOR. Missing a few
individual row entries: BREACH-MINOR.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — Write the Status Quo Anchor
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This is the Do Nothing entry. It's not the weakest candidate — it's the benchmark every other
idea has to beat. Write it after architecture so Bypasses and Preserves can reference the
Phase 3 category labels you just declared.

| Field | Content | Challenge Binding |
|-------|---------|-------------------|
| Costs | What staying put actually costs for `{{topic}}` | T-3 |
| Benefits | What's genuinely attractive about not changing — why teams choose inertia | T-3 |
| Competitive Threshold | What an alternative must concretely demonstrate to displace this — name a Phase 3 category | T-3 |
| Bypasses | Which Phase 3 category labels the status quo makes unnecessary (name them) | T-3 |
| Preserves | What a transition would put at risk for `{{topic}}` | T-3 |
| Net Position | Does inertia currently dominate? Under what specific condition does it stop? | T-3 synthesis |

The Challenge Binding column is required — absent: BREACH-MAJOR. Costs-only without Benefits:
BREACH-MINOR. Bypasses/Preserves referencing no Phase 3 categories: BREACH-MINOR. Net Position
without a named displacement condition: BREACH-MINOR.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5 — Generate Ideas (Names and Pitches Only)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Generate a numbered list of 22–38 Name | Pitch pairs. Nothing else yet — no categories,
rationales, or T-Evidence. Categories come in Phase 6 when you can see the whole set at once.

No `**` marks. That happens in Phase 7 after the challenge. Assigning `**` here is BREACH-FATAL.

If you notice one area dominating as you write, shift direction before continuing — check the
Phase 3 concentration commitments.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6 — Assign Categories, Rationales, and T-Evidence
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Now go through the Phase 5 list and assign all four anatomy fields plus a T-Evidence pre-score.

| # | Name | Pitch | Category | Rationale | T-Evidence |
|---|------|-------|----------|-----------|------------|

T-Evidence format: `T-1:PASS/PARTIAL/FAIL · T-2:PASS/PARTIAL/FAIL · T-3:[dims cleared] · T-4:PASS/PARTIAL/FAIL`

Rationale must be `{{topic}}`-specific — generic: BREACH-MINOR. T-Evidence column absent:
BREACH-MAJOR. More than 1/3 of rows without T-Evidence: BREACH-MAJOR. Final count outside
20–40: BREACH-MAJOR. Any category exceeding 40%: BREACH-MAJOR.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — Challenge the Top Candidates
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Identify 8–10 tentative top candidates by their T-Evidence score. Run them through the
Phase 1 challenge framework. Do not assign `**` yet — that's only for survivors.

The challenge table uses separate columns for each T-3 anchor field. This is what makes the
T-3 evaluation structural rather than judgmental — each anchor field gets its own verdict.

| # | Candidate | Ph6 Pre-Score | T-1: Differentiation | T-2: Topic Fit | T-3: Costs | T-3: Benefits | T-3: Competitive Threshold | T-3: Bypasses | T-3: Preserves | T-4: Category Coverage | T-3 Dims Cleared | Verdict |
|---|-----------|--------------|---------------------|---------------|-----------|--------------|--------------------------|--------------|---------------|----------------------|-----------------|---------|

Ph6 Pre-Score carries the Phase 6 T-Evidence forward exactly — missing this column: BREACH-MAJOR.

For each T-3 column, enter PASS/PARTIAL/FAIL based on whether the candidate's rationale
demonstrates advantage on that Phase 4 anchor dimension. T-3 Dims Cleared = count of PASSes
across the 5 columns. If you merged T-3 into one column instead of splitting it: BREACH-MAJOR.

Verdict: PASS when T-1+T-2+T-4 all pass and T-3 Dims Cleared ≥ 3. Otherwise FAIL.
Select 5 survivors as `**` picks spanning at least 3 categories.
Fewer than 5 survivors: BREACH-MAJOR, return to Phase 6 and strengthen candidates.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 8 — Write the Artifact
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write the artifact to: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md

Include: header with topic/date/counts, AMEND section (A1/A2/A3), candidate pool grouped by
category with exactly 5 `**` marks, and the Do Nothing anchor table outside the numbered pool.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9A — Check the Ledger
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Before the criterion checklist, audit the evidence ledger. Phase 9B waits until all rows
reach COMPLETE.

| Phase | What It Was Supposed to Produce | Status | Declared Severity | Notes |
|-------|--------------------------------|--------|-------------------|-------|
| Phase 3 | AMEND Source + Primary Challenge Test columns, every row | | | |
| Phase 4 | Challenge Binding column, every row | | | |
| Phase 5 | Name + Pitch, every candidate row | | | |
| Phase 6 | T-Evidence structured notation, every row | | | |
| Phase 7 | Ph6 Pre-Score column + T-3 as 5 anchor-named columns | | | |

For any VIOLATION: declare its severity using Table 1C, apply the correction protocol, then
re-check the row before marking COMPLETE.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9B — Criterion Checklist
Entry: Phase 9A all rows COMPLETE.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Row | Criterion | Status | Tier if FAIL |
|-----|-----------|--------|--------------|
| 1 | 20–40 candidates | PASS/FAIL | BREACH-MAJOR |
| 2 | All 4 anatomy fields on every candidate | PASS/FAIL | BREACH-MAJOR |
| 3 | Exactly 5 `**` marks | PASS/FAIL | BREACH-MAJOR |
| 4 | Do Nothing with 6 fields including Net Position | PASS/FAIL | BREACH-MAJOR |
| 5 | AMEND with 3 actionable adjustments + downstream effects | PASS/FAIL | BREACH-MINOR |
| 6 | Architecture AMEND Source + Primary Challenge Test columns | PASS/FAIL | BREACH-MAJOR |
| 7 | Phase 7 T-3 as 5 anchor-named columns (not merged) | PASS/FAIL | BREACH-MAJOR |
| 8 | Phase 7 Ph6 Pre-Score carryforward | PASS/FAIL | BREACH-MAJOR |
| 9 | Phase 6 T-Evidence with structured notation | PASS/FAIL | BREACH-MAJOR |
| 10 | `**` spans ≥3 categories | PASS/FAIL | BREACH-MAJOR |
| 11 | Phase 4 Challenge Binding column present | PASS/FAIL | BREACH-MAJOR |
| 12 | Table 1C BREACH taxonomy in Phase 1 | PASS/FAIL | BREACH-FATAL |
| 13 | Phase 9A Declared Severity column populated | PASS/FAIL | BREACH-MAJOR |
```

---

## V-04 — Combination: Anchor-Challenge Bidirectional Column Binding (C-27 + C-31)

**Variation axis:** Phase 4 anchor table carries a "Phase 7 Column" binding field on every row
that names the exact Phase 7 challenge column header the field maps to. Phase 7 challenge table
uses those exact field names as column headers. This creates bidirectional traceability: anchor
→ challenge (via Phase 4's "Phase 7 Column" field) and challenge → anchor (via Phase 7's
column headers). C-31 and C-27 are satisfied by schema in both directions simultaneously.

**Hypothesis:** Previous rounds satisfied C-31 (anchor binds to Phase 1 test ID) but not C-27
(challenge table column headers name anchor field labels). V-04 extends C-31's anchor binding
field to point forward to Phase 7 column names rather than backward to Phase 1 test IDs,
creating a binding from anchor to challenge table schema. Combined with Phase 7 using those
names as actual headers, the traceability runs in both directions.

---

```
You are generating a brainstorm artifact for the topic: `{{topic}}`
Output date: `{{date}}`
Artifact path: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 1 — CHALLENGE FRAMEWORK + LEDGER BLUEPRINT + BREACH TAXONOMY
Entry: Start of session.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Declare three co-equal Phase 1 artifacts.

#### Table 1A — Challenge Framework

| ID | Test | Pass Threshold | Survival Condition |
|----|------|----------------|--------------------|
| T-1 | Differentiation | Meaningfully distinct mechanism from every other `**` candidate | Removing eliminates an approach not covered elsewhere |
| T-2 | Topic Fit | Rationale names a specific dimension of `{{topic}}` | Fails if topic swapped out |
| T-3 | Inertia Displacement | PASS on ≥3 of 5 Phase 4 anchor fields; evaluated in Phase 7 via one column per anchor field, columns named after anchor fields | ≥3 PASS verdicts across Phase 7 anchor-field columns |
| T-4 | Category Coverage | Candidate's category absent from the other 4 `**` picks | Removing collapses top-5 below 3 categories |

Survival threshold: All 4 must PASS. 3/4 is not a `**` pick.

#### Table 1B — Evidence Ledger Blueprint

| Phase | Contributing Phase Name | Ledger Field Populated | Violation Condition |
|-------|------------------------|------------------------|---------------------|
| Phase 3 | Architecture | AMEND Source + Primary Challenge Test on every row | Column absent or row missing either entry |
| Phase 4 | Do Nothing Anchor | "Challenge Test" column (T-3 per analytical field) AND "Phase 7 Column" column (naming exact Phase 7 header) on every row | Either column absent from anchor table |
| Phase 5 | Diverge | Name + Pitch, every row | Any blank cell |
| Phase 6 | Cluster + T-Evidence | T-Evidence structured notation on every row | Blank T-Evidence cells or absent column |
| Phase 7 | Adversarial Challenge | Ph6 Pre-Score + T-3 evaluated using Phase 4 anchor field labels as column headers | Ph6 absent or T-3 column headers don't match Phase 4 anchor field labels |

#### Table 1C — BREACH Severity Taxonomy

| Severity | Definition | Correction Protocol | Continue Before Correcting? |
|----------|-----------|---------------------|-----------------------------|
| BREACH-MINOR | Column present but <1/3 entries missing; AMEND directions overlap; Net Position without displacement condition | Correct cells in-place. Mark `[corrected]`. | YES |
| BREACH-MAJOR | Required column entirely absent; concentration cap exceeded; count outside 20–40; Phase 4 "Phase 7 Column" binding column absent; Phase 7 T-3 headers don't match Phase 4 anchor labels; fewer than 5 survivors | HALT. Reconstruct affected table. Re-verify before advancing. | NO |
| BREACH-FATAL | Candidates before Phase 1; `**` before Phase 7; Do Nothing absent; challenge framework altered after lock | STOP. Discard from originating phase. Restart. | NO |

Exit Phase 1:
- [ ] Table 1A T-3 references Phase 4 anchor-field columns — BREACH-MAJOR if absent
- [ ] Table 1B Phase 4 row explicitly names "Phase 7 Column" binding field — BREACH-MAJOR if absent
- [ ] Table 1C all 3 tiers with protocols — BREACH-MAJOR if any tier missing
- [ ] Any FAIL → identify BREACH tier, apply per-tier protocol before Phase 2
Ledger obligation satisfied: Phase 1 framework, blueprint, BREACH taxonomy declared.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — AMEND ADJUSTMENTS
Entry: Phase 1 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| # | Dimension | Direction | Downstream Effect on Pool |
|---|-----------|-----------|--------------------------|
| A1 | | | |
| A2 | | | |
| A3 | | | |

Three adjustments; non-overlapping directions; `{{topic}}`-specific downstream effects.
Overlapping directions: BREACH-MINOR. Generic effects: BREACH-MINOR.

Exit Phase 2:
- [ ] 3 rows; all columns filled; directions non-overlapping; effects `{{topic}}`-specific
- [ ] Any FAIL → identify BREACH tier, apply per-tier protocol before Phase 3
Ledger obligation satisfied: AMEND adjustments declared.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3 — ARCHITECTURE DECLARATION
Entry: Phase 2 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Category | Description | Target Count | % of Pool | AMEND Source | Primary Challenge Test |
|----------|-------------|--------------|-----------|--------------|------------------------|

At least 4 categories; no category ≥40%; ≥1 category lists T-3.
AMEND Source and Primary Challenge Test columns required — BREACH-MAJOR if either column absent.

Exit Phase 3:
- [ ] 4+ categories; cap enforced; ≥1 T-3 row; both columns populated
- [ ] Any FAIL → identify BREACH tier, apply per-tier protocol before Phase 4
Ledger obligation satisfied: Architecture table with AMEND Source and Primary Challenge Test.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — DO NOTHING ANCHOR (BIDIRECTIONAL BINDING)
Entry: Phase 3 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write the status quo anchor with THREE binding columns: content, the Phase 1 test it satisfies,
and the exact Phase 7 challenge table column header that will evaluate it.

| Field | Content | Challenge Test | Phase 7 Column |
|-------|---------|---------------|----------------|
| Costs | [specific costs for `{{topic}}`] | T-3 | T-3: Costs |
| Benefits | [why inertia is genuinely appealing] | T-3 | T-3: Benefits |
| Competitive Threshold | [advantage level needed to displace; name a Phase 3 category] | T-3 | T-3: Competitive Threshold |
| Bypasses | [Phase 3 category labels status quo renders unnecessary] | T-3 | T-3: Bypasses |
| Preserves | [what a transition would put at risk for `{{topic}}`] | T-3 | T-3: Preserves |
| Net Position | [integrated judgment: does inertia dominate? displacement condition?] | T-3 synthesis | T-3: Dims Cleared |

Rules:
- "Phase 7 Column" column must be present on every row — absent: BREACH-MAJOR
- "Phase 7 Column" cell values must exactly match the column header names used in Phase 7 — mismatch: BREACH-MINOR
- "Challenge Test" column required; Net Position row maps to "T-3 synthesis" — absent: BREACH-MAJOR
- Costs AND Benefits required — costs-only: BREACH-MINOR
- Bypasses/Preserves must name Phase 3 category labels — generic: BREACH-MINOR
- Net Position must name displacement condition — absent: BREACH-MINOR

Exit Phase 4:
- [ ] All 6 rows; "Phase 7 Column" column present on every row — BREACH-MAJOR if column absent
- [ ] "Phase 7 Column" values match Phase 7 column headers — BREACH-MINOR if any mismatch
- [ ] "Challenge Test" column present; Net Position → T-3 synthesis — BREACH-MAJOR if absent
- [ ] Bypasses/Preserves name Phase 3 categories — BREACH-MINOR if generic
- [ ] Net Position integrative with condition — BREACH-MINOR if not
- [ ] Any FAIL → identify BREACH tier, apply per-tier protocol before Phase 5
Ledger obligation satisfied: Anchor table carries Challenge Test and Phase 7 Column binding on every row.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5 — DIVERGE (Name + Pitch Only)
Entry: Phase 4 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

22–38 Name+Pitch pairs. No categories, rationales, T-Evidence, or `**` marks.
Blank cells: BREACH-MINOR. Extra fields added: BREACH-MINOR. `**` assigned: BREACH-FATAL.

Exit Phase 5:
- [ ] 22–38 pairs; no extra fields; no `**`
Ledger obligation satisfied: Diverge output available for cluster phase.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6 — CLUSTER + T-EVIDENCE
Entry: Phase 5 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| # | Name | Pitch | Category | Rationale | T-Evidence |
|---|------|-------|----------|-----------|------------|

T-Evidence format: `T-1:PASS/PARTIAL/FAIL · T-2:PASS/PARTIAL/FAIL · T-3:[dims cleared, using Phase 4 field labels] · T-4:PASS/PARTIAL/FAIL`

Generic rationale: BREACH-MINOR. T-Evidence column absent: BREACH-MAJOR. >1/3 rows blank: BREACH-MAJOR.
Count outside 20–40: BREACH-MAJOR. Concentration cap exceeded: BREACH-MAJOR.

Exit Phase 6:
- [ ] All 4 anatomy fields + T-Evidence on every row — BREACH-MAJOR if any field absent
- [ ] No category ≥40%; count 20–40
- [ ] Any FAIL → identify BREACH tier, apply per-tier protocol before Phase 7
Ledger obligation satisfied: Cluster table with T-Evidence.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — ADVERSARIAL CHALLENGE
Entry: Phase 6 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Identify 8–10 top candidates. Do NOT assign `**` yet.

Build the challenge table using the Phase 4 anchor field labels as T-3 column headers. The
"Phase 7 Column" values in Phase 4 specify exactly which headers to use — implement them:

| # | Candidate | Ph6 Pre-Score | T-1: Differentiation | T-2: Topic Fit | T-3: Costs | T-3: Benefits | T-3: Competitive Threshold | T-3: Bypasses | T-3: Preserves | T-4: Category Coverage | T-3 Dims Cleared | Verdict |
|---|-----------|--------------|---------------------|---------------|-----------|--------------|--------------------------|--------------|---------------|----------------------|-----------------|---------|

Rules:
- Ph6 Pre-Score: carry forward T-Evidence from Phase 6 exactly — absent: BREACH-MAJOR
- T-3 column headers must match Phase 4 "Phase 7 Column" values exactly — mismatch: BREACH-MINOR;
  merging T-3 into single column: BREACH-MAJOR
- T-3 Dims Cleared: count of PASS across 5 T-3 columns
- Verdict: PASS if T-1+T-2+T-4 PASS and T-3 Dims Cleared ≥ 3; else FAIL
- 5 `**` candidates from PASS verdicts spanning ≥3 categories
- Fewer than 5 PASS verdicts: BREACH-MAJOR

Exit Phase 7:
- [ ] Ph6 Pre-Score present — BREACH-MAJOR if absent
- [ ] T-3 implemented as 5 columns with Phase 4 anchor field labels as headers — BREACH-MAJOR if merged
- [ ] T-3 headers match Phase 4 "Phase 7 Column" values — BREACH-MINOR if mismatch
- [ ] 5 `**` from PASS verdicts spanning ≥3 categories
- [ ] No `**` before Phase 7 — BREACH-FATAL if pre-assigned
- [ ] Any FAIL → identify BREACH tier, apply per-tier protocol
Ledger obligation satisfied: Challenge table implements Phase 4 anchor-field column binding.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 8 — ARTIFACT ASSEMBLY
Entry: Phase 7 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write artifact at: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md
Header · AMEND (A1/A2/A3) · Pool by category with 5 `**` · Do Nothing anchor.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9A — TERMINAL LEDGER AUDIT
Entry: Phase 8 complete. Phase 9B waits until all rows COMPLETE.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Phase | Ledger Field Expected | Status | Declared Severity | Notes |
|-------|----------------------|--------|-------------------|-------|
| Phase 3 | AMEND Source + Primary Challenge Test columns, every row | | | |
| Phase 4 | Challenge Test + Phase 7 Column binding columns, every row | | | |
| Phase 5 | Name + Pitch, every row | | | |
| Phase 6 | T-Evidence structured notation, every row | | | |
| Phase 7 | Ph6 Pre-Score + T-3 as 5 anchor-field-named columns matching Phase 4 | | | |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9B — CRITERION CHECKLIST
Entry: Phase 9A all rows COMPLETE.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Row | Criterion | Status | Tier if FAIL |
|-----|-----------|--------|--------------|
| 1 | 20–40 candidates | PASS/FAIL | BREACH-MAJOR |
| 2 | All 4 anatomy fields | PASS/FAIL | BREACH-MAJOR |
| 3 | Exactly 5 `**` | PASS/FAIL | BREACH-MAJOR |
| 4 | Do Nothing with 6 fields + Net Position | PASS/FAIL | BREACH-MAJOR |
| 5 | AMEND 3 adjustments with downstream effects | PASS/FAIL | BREACH-MINOR |
| 6 | Architecture AMEND Source + Primary Challenge Test columns | PASS/FAIL | BREACH-MAJOR |
| 7 | Phase 7 T-3 as 5 anchor-named columns | PASS/FAIL | BREACH-MAJOR |
| 8 | Phase 7 Ph6 Pre-Score carryforward | PASS/FAIL | BREACH-MAJOR |
| 9 | Phase 6 T-Evidence structured notation | PASS/FAIL | BREACH-MAJOR |
| 10 | `**` spans ≥3 categories | PASS/FAIL | BREACH-MAJOR |
| 11 | Phase 4 Challenge Test + Phase 7 Column binding columns present | PASS/FAIL | BREACH-MAJOR |
| 12 | Table 1C BREACH taxonomy in Phase 1 | PASS/FAIL | BREACH-FATAL |
| 13 | Phase 9A Declared Severity populated | PASS/FAIL | BREACH-MAJOR |
| 14 | Phase 7 T-3 column headers match Phase 4 Phase 7 Column values | PASS/FAIL | BREACH-MAJOR |
```

---

## V-05 — Full R13 Stack: C-27 + C-40 + Two-Pass Audit

**Variation axis:** All advances from R12 V-01 (BREACH tier propagation, C-40) plus V-01 R13's
split T-3 columns (C-27) plus bidirectional anchor binding from V-04 plus a two-pass terminal
audit (Reconstruct → Assess, C-39) that includes an explicit Phase 9A row for T-3 column
schema verification.

**Hypothesis:** C-27 closure requires split T-3 columns in Phase 7 (addressed by V-01–V-04).
C-40 requires BREACH tier labels in every contributing phase's exit gates and inline triggers
(already solid in R12 V-01; must be preserved under all R13 innovations). The two-pass audit
adds an evidence reconstruction layer that forces the model to re-read what Phase 7 actually
produced — anchoring the C-27 verdict in observed column headers, not recalled intention.
Together these three axes should close C-27, maintain C-40, and deepen C-39 compliance.

---

```
You are generating a brainstorm artifact for the topic: `{{topic}}`
Output date: `{{date}}`
Artifact path: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 1 — CHALLENGE FRAMEWORK + LEDGER BLUEPRINT + BREACH TAXONOMY
Entry: Start of session.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Declare three co-equal Phase 1 artifacts before any generation begins.

#### Table 1A — Challenge Framework

| ID | Test | Pass Threshold | Phase 7 Column Schema | Survival Condition |
|----|------|----------------|-----------------------|--------------------|
| T-1 | Differentiation | Meaningfully distinct mechanism from every other `**` candidate | "T-1: Differentiation" (single column) | Removing eliminates a distinct approach |
| T-2 | Topic Fit | Rationale names a specific dimension of `{{topic}}` — not generic | "T-2: Topic Fit" (single column) | Fails if topic swapped out |
| T-3 | Inertia Displacement | PASS on ≥3 of 5 anchor fields; evaluated via 5 separate columns | **Five columns required** — headers must be exactly: "T-3: Costs" / "T-3: Benefits" / "T-3: Competitive Threshold" / "T-3: Bypasses" / "T-3: Preserves" | ≥3 PASS across the 5 anchor-named columns |
| T-4 | Category Coverage | Removing this `**` pick collapses top-5 below 3 categories | "T-4: Category Coverage" (single column) | Category absent from other 4 picks |

Survival threshold: All 4 must PASS. 3/4 is not a `**` pick.
T-3 five-column schema is LOCKED after Phase 1 exit — merging or relabeling is BREACH-FATAL.
Full challenge framework locked — modification is BREACH-FATAL.

#### Table 1B — Evidence Ledger Blueprint

| Phase | Phase Name | Ledger Field Populated | Violation Condition | BREACH Tier |
|-------|-----------|------------------------|---------------------|-------------|
| Phase 3 | Architecture | AMEND Source column + Primary Challenge Test column, every row | Any row missing either column | BREACH-MAJOR |
| Phase 4 | Do Nothing Anchor | "Challenge Test" column + "Phase 7 Column" column on every row | Either column absent | BREACH-MAJOR |
| Phase 5 | Diverge | Name + Pitch on every candidate row | Any blank cell | BREACH-MINOR |
| Phase 6 | Cluster + T-Evidence | T-Evidence column: `T-1:[v] · T-2:[v] · T-3:[dims cleared] · T-4:[v]` on every row | Column absent or >1/3 rows blank | BREACH-MAJOR |
| Phase 7 | Adversarial Challenge | Ph6 Pre-Score column + T-3 as 5 anchor-named columns matching Table 1A schema | Ph6 absent; T-3 merged or relabeled | BREACH-MAJOR/FATAL |

Note: Table 1B now carries a BREACH Tier column — every violation has a pre-declared severity.

#### Table 1C — BREACH Severity Taxonomy

| Severity | Definition | Correction Protocol | Continue Before Correcting? |
|----------|-----------|---------------------|-----------------------------|
| BREACH-MINOR | Column present but <1/3 entries missing; AMEND directions overlap on one pair; Net Position without displacement condition; T-3 column header uses minor label variant | Fix specific cells in-place. Mark `[corrected]`. | YES — correct inline, then continue |
| BREACH-MAJOR | Required column entirely absent; concentration cap exceeded at exit; candidate count outside 20–40; Phase 4 binding columns absent; Phase 7 T-3 columns missing or merged into fewer than 5; Ph6 Pre-Score absent; fewer than 5 survivors | HALT current phase. Reconstruct affected table. Re-verify before advancing. | NO — halt and reconstruct |
| BREACH-FATAL | Candidates generated before Phase 1; `**` assigned before Phase 7; Do Nothing anchor absent; challenge framework or T-3 schema modified after Phase 1 lock | STOP all generation. Discard from originating phase forward. Restart that phase. | NO — stop and restart |

Exit Phase 1:
- [ ] Table 1A: T-3 row "Phase 7 Column Schema" cell names all 5 required column labels — BREACH-MAJOR if absent
- [ ] Table 1A: T-3 schema and full framework locked — any post-lock modification is BREACH-FATAL
- [ ] Table 1B: 5 contributing phases; each row carries BREACH Tier — BREACH-MAJOR if tier column absent
- [ ] Table 1C: All 3 tiers with Definition, Correction Protocol, Continue decision — BREACH-MAJOR if any tier missing
- [ ] Any FAIL → identify BREACH tier from Table 1C, apply per-tier protocol before Phase 2
Ledger obligation satisfied: Phase 1 framework, blueprint with BREACH tiers, taxonomy declared.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — AMEND ADJUSTMENTS
Entry: Phase 1 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write exactly 3 pool-shaping adjustments before architecture or candidates are generated.

| # | Dimension | Direction | Downstream Effect on Pool |
|---|-----------|-----------|--------------------------|
| A1 | | Expands / Narrows / Redirects | |
| A2 | | Expands / Narrows / Redirects | |
| A3 | | Expands / Narrows / Redirects | |

Rules:
- Dimension: specific axis — "be more creative" is not a dimension, BREACH-MINOR
- Direction: all three must differ — two sharing a direction: BREACH-MINOR, revise before exit
- Downstream Effect: `{{topic}}`-specific — generic ("more options"): BREACH-MINOR

Exit Phase 2:
- [ ] Exactly 3 rows; all columns filled — BREACH-MINOR if any column blank
- [ ] Directions non-overlapping — BREACH-MINOR if duplicate; revise before exit
- [ ] Downstream Effects `{{topic}}`-specific — BREACH-MINOR if any generic
- [ ] Any FAIL → identify BREACH tier from Table 1C, apply per-tier protocol before Phase 3
Ledger obligation satisfied: AMEND adjustments declared; pool-shaping committed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3 — ARCHITECTURE DECLARATION
Entry: Phase 2 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Declare category structure before generating any candidates.

| Category | Description | Target Count | % of Pool | AMEND Source | Primary Challenge Test |
|----------|-------------|--------------|-----------|--------------|------------------------|

Total: ______

Rules:
- At least 4 distinct categories
- Concentration cap: ≥40% at exit: BREACH-MAJOR
- AMEND Source + Primary Challenge Test required on every row:
  - Column absent: BREACH-MAJOR
  - <1/3 row entries missing: BREACH-MINOR
- At least 1 category lists T-3 as Primary Challenge Test — BREACH-MAJOR if absent
- Totals 20–40 — outside range: BREACH-MAJOR

Exit Phase 3:
- [ ] 4+ categories; % computed; no category ≥40% — BREACH-MAJOR if cap exceeded
- [ ] AMEND Source column present; all rows populated — BREACH-MAJOR/absent, BREACH-MINOR/<1/3 missing
- [ ] Primary Challenge Test column present; ≥1 T-3 row — BREACH-MAJOR if absent or no T-3 row
- [ ] Any FAIL → identify BREACH tier from Table 1C, apply per-tier protocol before Phase 4
Ledger obligation satisfied: Architecture with AMEND Source and Primary Challenge Test columns.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — DO NOTHING ANCHOR (BIDIRECTIONAL BINDING)
Entry: Phase 3 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write the status quo anchor after architecture is declared. Include THREE columns: content,
the Phase 1 test satisfied, and the exact Phase 7 column header that evaluates this field.

| Field | Content | Challenge Test | Phase 7 Column |
|-------|---------|---------------|----------------|
| Costs | [specific costs for `{{topic}}`] | T-3 | T-3: Costs |
| Benefits | [why inertia is genuinely appealing] | T-3 | T-3: Benefits |
| Competitive Threshold | [advantage required to displace; name Phase 3 category] | T-3 | T-3: Competitive Threshold |
| Bypasses | [Phase 3 category labels status quo renders unnecessary] | T-3 | T-3: Bypasses |
| Preserves | [what transition risks for `{{topic}}`] | T-3 | T-3: Preserves |
| Net Position | [integrated judgment; displacement condition named explicitly] | T-3 synthesis | T-3: Dims Cleared |

Rules:
- "Phase 7 Column" column required; absent: BREACH-MAJOR
- "Phase 7 Column" values must exactly match Table 1A locked column labels — mismatch: BREACH-MINOR
- "Challenge Test" column required; Net Position → T-3 synthesis — absent: BREACH-MAJOR
- Costs AND Benefits required — costs-only: BREACH-MINOR
- Bypasses/Preserves must name Phase 3 categories — generic: BREACH-MINOR
- Net Position must name displacement condition — absent: BREACH-MINOR

Exit Phase 4:
- [ ] All 6 rows; "Challenge Test" column present — BREACH-MAJOR if absent
- [ ] "Phase 7 Column" column present; all values match Table 1A schema — BREACH-MAJOR/absent, BREACH-MINOR/mismatch
- [ ] Costs AND Benefits present — BREACH-MINOR if costs-only
- [ ] Bypasses/Preserves name Phase 3 categories — BREACH-MINOR if generic
- [ ] Net Position integrative with condition — BREACH-MINOR if not
- [ ] Any FAIL → identify BREACH tier from Table 1C, apply per-tier protocol before Phase 5
Ledger obligation satisfied: Anchor table carries Challenge Test + Phase 7 Column binding on every row.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5 — DIVERGE (Name + Pitch Only)
Entry: Phase 4 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Generate 22–38 Name+Pitch pairs. No categories, rationales, T-Evidence, or `**` marks.

- Blank cells: BREACH-MINOR, correct before exit
- Extra fields (category/rationale added early): BREACH-MINOR, remove before exit
- `**` marks assigned: BREACH-FATAL — remove immediately

Exit Phase 5:
- [ ] 22–38 pairs; no extra fields; no `**` — any `**`: BREACH-FATAL
Ledger obligation satisfied: Diverge output available for cluster phase.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6 — CLUSTER + T-EVIDENCE
Entry: Phase 5 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Assign Category, Rationale, and T-Evidence to every candidate.

| # | Name | Pitch | Category | Rationale | T-Evidence |
|---|------|-------|----------|-----------|------------|

T-Evidence format: `T-1:PASS/PARTIAL/FAIL · T-2:PASS/PARTIAL/FAIL · T-3:[dims cleared using Phase 4 field labels] · T-4:PASS/PARTIAL/FAIL`

- Generic rationale: BREACH-MINOR
- T-Evidence column absent: BREACH-MAJOR
- >1/3 rows blank: BREACH-MAJOR; <1/3 rows blank: BREACH-MINOR
- Concentration cap exceeded at exit: BREACH-MAJOR
- Count outside 20–40 at exit: BREACH-MAJOR

Exit Phase 6:
- [ ] All candidates have all 4 anatomy fields — BREACH-MAJOR if any field missing from any row
- [ ] T-Evidence column present; structured notation on every row — BREACH-MAJOR if column absent
- [ ] No category ≥40% — BREACH-MAJOR if exceeded
- [ ] Count 20–40 — BREACH-MAJOR if outside range
- [ ] Any FAIL → identify BREACH tier from Table 1C, apply per-tier protocol before Phase 7
Ledger obligation satisfied: Cluster table with T-Evidence structured notation on every row.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — ADVERSARIAL CHALLENGE
Entry: Phase 6 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Identify 8–10 top candidates by T-Evidence score. Do NOT assign `**` yet.

Build the challenge table implementing the Table 1A locked schema. T-3 is evaluated via 5
separate columns whose headers are the Phase 4 anchor field labels (matching the Phase 4
"Phase 7 Column" values exactly):

| # | Candidate | Ph6 Pre-Score | T-1: Differentiation | T-2: Topic Fit | T-3: Costs | T-3: Benefits | T-3: Competitive Threshold | T-3: Bypasses | T-3: Preserves | T-4: Category Coverage | T-3 Dims Cleared | Verdict |
|---|-----------|--------------|---------------------|---------------|-----------|--------------|--------------------------|--------------|---------------|----------------------|-----------------|---------|

Rules:
- Ph6 Pre-Score: carry forward T-Evidence from Phase 6 exactly — absent: BREACH-MAJOR
- T-3 column headers must match Table 1A locked schema AND Phase 4 "Phase 7 Column" values — mismatch: BREACH-MINOR; merging T-3 into fewer than 5 columns: BREACH-MAJOR
- T-3 Dims Cleared: count of PASS across 5 T-3 anchor columns
- Verdict: PASS if T-1+T-2+T-4 PASS and T-3 Dims Cleared ≥ 3; else FAIL (name failing test)
- 5 `**` candidates from PASS verdicts spanning ≥3 categories
- Fewer than 5 PASS verdicts: BREACH-MAJOR — return to Phase 6, strengthen

Exit Phase 7:
- [ ] Ph6 Pre-Score column present and populated — BREACH-MAJOR if absent
- [ ] T-3 as 5 anchor-named columns matching Table 1A schema and Phase 4 Phase 7 Column values — BREACH-MAJOR if merged; BREACH-MINOR if headers are labeled but don't match exactly
- [ ] 5 `**` from PASS verdicts; `**` spans ≥3 categories
- [ ] No `**` before this phase — BREACH-FATAL if pre-assigned
- [ ] Any FAIL → identify BREACH tier from Table 1C, apply per-tier protocol
Ledger obligation satisfied: Challenge table with Ph6 Pre-Score + 5 anchor-named T-3 columns.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 8 — ARTIFACT ASSEMBLY
Entry: Phase 7 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write artifact at: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md
Header · AMEND (A1/A2/A3) · Pool by category with exactly 5 `**` · Do Nothing anchor.
`**` count must be 5. BREACH-FATAL if any `**` candidate did not survive Phase 7.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9A — TERMINAL LEDGER AUDIT (TWO-PASS: RECONSTRUCT → ASSESS)
Entry: Phase 8 complete. Phase 9B may not begin until all Assess rows COMPLETE.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Pass 1 — Reconstruct.** For each contributing phase, describe row-by-row what was ACTUALLY
PRODUCED in this execution. Do not render any compliance verdict yet. Re-read your output.

| Phase | What Phase Actually Produced | Key Schema Elements Observed |
|-------|------------------------------|------------------------------|
| Phase 3 | [describe columns present in the architecture table you wrote; list AMEND Source and Primary Challenge Test entries observed] | Columns: / T-3 row present?: |
| Phase 4 | [describe Challenge Test and Phase 7 Column binding columns as actually written; list the 6 field rows and their Phase 7 Column values] | Phase 7 Column values: / Net Position condition: |
| Phase 5 | [describe the diverge output: count, any extra fields or `**` marks observed] | Count: / Extra fields: |
| Phase 6 | [describe T-Evidence column as actually written: notation format, blank row count, category concentration] | T-Evidence format used: / Blank rows: |
| Phase 7 | [describe Phase 7 table columns as actually written — list every T-3 column header name you used] | T-3 column headers observed: / Ph6 Pre-Score present?: |

**Pass 2 — Assess.** Apply ledger criteria and violation definitions against Reconstruct
evidence. Derive verdicts from what Phase 1 (Reconstruct) showed, not from expectation.

| Phase | Ledger Field Expected | Status (COMPLETE / VIOLATION) | Declared Severity | Correction Applied |
|-------|----------------------|-------------------------------|-------------------|--------------------|
| Phase 3 | AMEND Source + Primary Challenge Test columns, every row | | | |
| Phase 4 | Challenge Test + Phase 7 Column columns; all 6 rows; Phase 7 Column values match Table 1A schema | | | |
| Phase 5 | Name + Pitch every row; no extra fields; no `**` | | | |
| Phase 6 | T-Evidence structured notation; no >1/3 blank; count 20–40 | | | |
| Phase 7 | Ph6 Pre-Score present; T-3 as 5 anchor-named columns matching Table 1A + Phase 4 values | | | |

For any VIOLATION in the Assess table: declare severity using Table 1C, apply the correction
protocol, re-examine the Reconstruct row, and update to COMPLETE before Phase 9B.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9B — CRITERION CHECKLIST
Entry: Phase 9A Assess pass complete — all 5 rows COMPLETE.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Row | Criterion | Status | Declared Severity if FAIL |
|-----|-----------|--------|--------------------------|
| 1 | Candidate count 20–40 (excluding Do Nothing) | PASS/FAIL | BREACH-MAJOR |
| 2 | Every candidate has all 4 anatomy fields | PASS/FAIL | BREACH-MAJOR |
| 3 | Exactly 5 `**` marks in artifact | PASS/FAIL | BREACH-MAJOR |
| 4 | Do Nothing with 6 fields including Net Position | PASS/FAIL | BREACH-MAJOR |
| 5 | AMEND 3 adjustments with dimension / direction / downstream effect | PASS/FAIL | BREACH-MINOR |
| 6 | Architecture AMEND Source column; all rows populated | PASS/FAIL | BREACH-MAJOR |
| 7 | Architecture Primary Challenge Test column; ≥1 T-3 row | PASS/FAIL | BREACH-MAJOR |
| 8 | Phase 6 T-Evidence with structured notation | PASS/FAIL | BREACH-MAJOR |
| 9 | Phase 7 Ph6 Pre-Score carryforward column | PASS/FAIL | BREACH-MAJOR |
| 10 | `**` candidates span ≥3 categories | PASS/FAIL | BREACH-MAJOR |
| 11 | Phase 4 Challenge Test column + Phase 7 Column binding column; Net Position → T-3 synthesis | PASS/FAIL | BREACH-MAJOR |
| 12 | Table 1C BREACH taxonomy in Phase 1; all 3 tiers | PASS/FAIL | BREACH-FATAL |
| 13 | Phase 9A Declare Severity column populated for all Assess rows | PASS/FAIL | BREACH-MAJOR |
| 14 | Phase 7 T-3 implemented as 5 anchor-named columns matching Table 1A locked schema | PASS/FAIL | BREACH-MAJOR |
| 15 | Phase 9A structured as two passes (Reconstruct then Assess); Reconstruct is row-by-row | PASS/FAIL | BREACH-MAJOR |

Apply Table 1C correction protocol for every FAIL before finalizing artifact.
```
