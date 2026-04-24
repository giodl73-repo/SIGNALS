# draft-brainstorm Skill Prompt Variations — Round 14

**Skill:** draft-brainstorm
**Round:** 14
**Date:** 2026-03-15
**Rubric:** v13 (C-01 through C-42)
**Baseline:** R13 treats C-01 through C-40 as non-negotiable. C-27 closes as stable baseline — all
5 R13 variations PASS. R14 adds C-41 and C-42 as the new targets.

---

## R14 Axis Selection

R13 closed C-27 across all 5 variations and confirmed C-28 through C-40 stable. The scorecard
identified two R14 targets from R13 V-05 excellence signals:

- **C-41 (new in v13):** Table 1B BREACH Tier column — blueprint-taxonomy fusion at Phase 1
  declaration. R13 V-01 through V-04 carried "Ledger Violation Condition" in Table 1B, but not
  a "BREACH Tier" column that explicitly fuses each ledger obligation to a severity tier. R13
  V-05 included a BREACH Tier column. C-41 closes when every variation carries this column in
  Table 1B's schema at Phase 1.

- **C-42 (new in v13):** Phase 9A Reconstruct "T-3 column headers observed:" — forces literal
  re-reading of Phase 7 output before C-27 verdict. R13 Phase 9A audited T-3 column presence
  but did not require the model to explicitly list the headers it observes in Phase 7 before
  rendering the C-27 verdict. C-42 closes when Phase 9A contains a named "Reconstruct" step
  that quotes the observed headers and compares them against the expected labels before verdict.

| Variation | Primary Axis | Novel Structural Feature |
|-----------|--------------|--------------------------|
| V-01 | BREACH Tier fusion depth (C-41 direct) | Table 1B merged with per-row correction protocol — each row self-contained: obligation + BREACH Tier + correction action + may-continue flag |
| V-02 | Reconstruct protocol granularity (C-42 direct) | Phase 9A has a 5-step literal quote-and-compare reconstruct sequence before C-27 verdict |
| V-03 | Phrasing register: conversational with C-41 + C-42 | Conversational register throughout; C-41 BREACH Tier column and C-42 Reconstruct step embedded naturally in phase descriptions |
| V-04 | BREACH Tier fusion + lifecycle emphasis | Merged Table 1B/1C + bidirectional entry/exit gate tables at every phase boundary |
| V-05 | Full R14 stack | V-01 fusion depth + V-02 reconstruct granularity + V-04 bidirectional gates + 7-field anchor (Trajectory field added) |

---

## V-01 — Single-axis: BREACH Tier Fusion Depth (C-41 Direct)

**Variation axis:** Table 1B is redesigned as a fully self-contained ledger contract table where
every obligation row carries: Contributing Phase | Ledger Field | Ledger Violation Condition |
BREACH Tier | Correction Action | Continue Before Correcting. The BREACH Tier column fuses the
ledger blueprint with the severity taxonomy so that Table 1B alone is sufficient to respond to
any ledger violation — without needing to cross-reference Table 1C.

**Hypothesis:** C-41 targets blueprint-taxonomy fusion at Phase 1 declaration. The minimum
pass is adding a "BREACH Tier if Missing" column to Table 1B. The maximum fusion makes Table 1B
the sole violation-response authority by embedding the correction protocol directly in every row,
eliminating the need to look up Table 1C during generation. If each obligation row declares its
own tier and correction action, violation response becomes a row-local lookup — reducing the
distance between detection and correction protocol application.

---

```
You are generating a brainstorm artifact for the topic: `{{topic}}`
Output date: `{{date}}`
Artifact path: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 1 — CHALLENGE FRAMEWORK + LEDGER CONTRACT + BREACH TAXONOMY
Entry: Start of session.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Declare three co-equal Phase 1 artifacts before any generation begins.

#### Table 1A — Challenge Framework

| ID | Test | Pass Threshold | Phase 7 Column Schema | Survival Condition |
|----|------|----------------|-----------------------|--------------------|
| T-1 | Differentiation | Meaningfully distinct mechanism from every other `**` candidate | Single column: "T-1: Differentiation" | Removing this candidate eliminates an approach not covered by remaining 4 |
| T-2 | Topic Fit | Rationale names a specific dimension of `{{topic}}` — not generic | Single column: "T-2: Topic Fit" | Rationale fails if topic is swapped out |
| T-3 | Inertia Displacement | PASS on ≥3 of 5 anchor fields evaluated independently | **Five columns:** "T-3: Costs" / "T-3: Benefits" / "T-3: Competitive Threshold" / "T-3: Bypasses" / "T-3: Preserves" — each header must use this exact label | Candidate names ≥3 PASS cells across 5 anchor-named columns |
| T-4 | Category Coverage | Candidate's category not represented by other 4 `**` picks | Single column: "T-4: Category Coverage" | Removing this pick collapses top-5 below 3 categories |

Survival threshold: All four tests PASS. 3/4 is not a `**` pick.
Challenge framework locked after Phase 1 exit — modification is BREACH-FATAL.

#### Table 1B — Ledger Contract (Blueprint + Taxonomy fused)

| Phase | Contributing Phase | Ledger Field Populated | Violation Condition | BREACH Tier | Correction Action | Continue? |
|-------|--------------------|------------------------|---------------------|-------------|-------------------|-----------|
| 3 | Architecture | AMEND Source col + Primary Challenge Test col on every row | Any row missing either column | BREACH-MAJOR | Halt. Add missing column. Repopulate before Phase 4. | NO |
| 4 | Do Nothing Anchor | Challenge Binding col on every anchor field row | Any anchor row missing Challenge Binding | BREACH-MAJOR | Halt. Add Challenge Binding column. Correct all rows before Phase 5. | NO |
| 5 | Diverge | Name + Pitch on every candidate row | Any candidate missing Name or Pitch | BREACH-MINOR | Correct the blank cell in-place. Mark `[corrected]`. | YES |
| 6 | Cluster + T-Evidence | T-Evidence col with `T-1:[v]·T-2:[v]·T-3:[dims]·T-4:[v]` on every row | Blank T-Evidence cell; unstructured notation | BREACH-MAJOR if col absent; BREACH-MINOR if <1/3 rows blank | Absent col: halt and add before Phase 7. Blank cells: correct inline. | Col absent: NO. Cells: YES |
| 7 | Adversarial Challenge | Ph6 Pre-Score col + T-3 via 5 anchor-named cols matching Table 1A schema | Missing Ph6 Pre-Score; merged T-3 col; column labels deviate from Table 1A | BREACH-FATAL if `**` assigned before Phase 7; BREACH-MAJOR for schema deviations | Halt. Reconstruct Phase 7 table with correct schema. | NO |

Note: Table 1B is the sole violation-response authority. When a violation is detected, read the
row for the contributing phase, apply Correction Action, then continue or halt per the
Continue? flag.

#### Table 1C — BREACH Severity Taxonomy

| Severity | Definition | Correction Protocol | Continue Before Correcting? |
|----------|------------|---------------------|-----------------------------|
| BREACH-MINOR | Recommended field absent or generic; <1/3 rows missing structured content; overlap in AMEND directions on one axis | Correct in-place; mark `[corrected]` | YES |
| BREACH-MAJOR | Required ledger column absent; concentration cap exceeded at phase exit; candidate count outside 20–40; schema deviation in Phase 7 T-3 columns | HALT current phase; reconstruct affected table; re-verify before advancing | NO |
| BREACH-FATAL | Candidates generated before Phase 1 declared; `**` marks assigned before Phase 7 completes; anchor entirely absent; challenge framework modified after lock | STOP all generation; discard all output from originating phase forward; restart that phase | NO |

Exit Phase 1:
- [ ] Table 1A: T-1 through T-4 with Pass Threshold and Phase 7 Column Schema — BREACH-FATAL if absent
- [ ] Table 1A: T-3 row names all 5 Phase 7 column labels — BREACH-MAJOR if any label missing
- [ ] Table 1B: 5 obligation rows; BREACH Tier column present and populated on every row — BREACH-MAJOR if column absent
- [ ] Table 1B: Correction Action and Continue? columns present on every row — BREACH-MAJOR if absent
- [ ] Table 1C: All 3 severity tiers with Definition, Correction Protocol, Continue decision — BREACH-MAJOR if any tier missing
- [ ] Challenge framework locked
- [ ] Any FAIL → apply Table 1B or 1C correction protocol before Phase 2
Ledger obligation satisfied: Phase 1 framework, ledger contract (with BREACH Tier), taxonomy declared.

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
- Direction: A1, A2, A3 must pull in non-overlapping directions — duplicate direction: BREACH-MINOR,
  revise the overlapping adjustment before exit
- Downstream Effect: name specific candidate types that would surface or be displaced in
  `{{topic}}`'s context — "more options" is generic and fails C-12

Exit Phase 2:
- [ ] Exactly 3 rows; all columns filled — BREACH-MINOR if any column blank
- [ ] Directions are all distinct — BREACH-MINOR if duplicate; revise before exit
- [ ] Downstream Effects are `{{topic}}`-specific — BREACH-MINOR if generic
- [ ] Any FAIL → read Table 1B row for Phase 2 scope; apply correction protocol before Phase 3
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
  exceeding cap at phase exit is BREACH-MAJOR (Table 1B row for Phase 3)
- Totals must sum to 20–40
- Every row: AMEND Source (A1/A2/A3 or "Core") and Primary Challenge Test (T-1/T-2/T-3/T-4)
  — column absent: BREACH-MAJOR; <1/3 rows missing entry: BREACH-MINOR
- At least 1 category must list T-3 as Primary Challenge Test — BREACH-MAJOR if absent

Exit Phase 3:
- [ ] 4+ categories; % of Pool computed; no category ≥40% — BREACH-MAJOR if cap exceeded
- [ ] AMEND Source column present; every row populated — BREACH-MINOR/<1/3, BREACH-MAJOR/col absent
- [ ] Primary Challenge Test column present; ≥1 row lists T-3 — BREACH-MAJOR if absent
- [ ] Totals sum to 20–40 — BREACH-MAJOR if outside range
- [ ] Any FAIL → apply correction per Table 1B Phase 3 row before Phase 4
Ledger obligation satisfied: Architecture table carries AMEND Source and Primary Challenge Test.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — DO NOTHING ANCHOR
Entry: Phase 3 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write the status quo anchor after architecture is declared. Bypasses and Preserves must
reference specific Phase 3 category labels by name.

| Field | Content | Challenge Binding |
|-------|---------|-------------------|
| Costs | [specific active costs of the status quo for `{{topic}}`] | T-3 |
| Benefits | [genuine appeal of continuing — why inertia is attractive for `{{topic}}`] | T-3 |
| Competitive Threshold | [minimum advantage an alternative must demonstrate; reference a Phase 3 category] | T-3 |
| Bypasses | [which Phase 3 category labels the status quo renders unnecessary — name ≥1 by label] | T-3 |
| Preserves | [what a transition from the status quo would put at risk for `{{topic}}`] | T-3 |
| Net Position | [integrated judgment: does inertia currently dominate? name the specific condition under which it stops] | T-3 synthesis |

Rules:
- Costs AND Benefits must both be present with `{{topic}}`-specific content — costs-only: BREACH-MINOR
- Bypasses and Preserves must name Phase 3 category labels — generic: BREACH-MINOR
- Net Position must name a displacement condition — directional statement without condition: BREACH-MINOR
- Challenge Binding column must be present on every row — column absent: BREACH-MAJOR
- Do Nothing does NOT count toward the 20–40 candidate total

Exit Phase 4:
- [ ] All 6 field rows present with `{{topic}}`-specific content
- [ ] Costs AND Benefits both present — BREACH-MINOR if costs-only
- [ ] Competitive Threshold references a Phase 3 category — BREACH-MINOR if generic
- [ ] Bypasses and Preserves name Phase 3 category labels — BREACH-MINOR if generic
- [ ] Net Position names a displacement condition — BREACH-MINOR if not
- [ ] Challenge Binding column present; every row populated — apply Table 1B Phase 4 row if absent
- [ ] Any FAIL → apply correction per Table 1B Phase 4 row before Phase 5
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
- No category, rationale, or T-Evidence in this phase — adding them: BREACH-MINOR; remove before exit
- If one conceptual area dominates before you finish: pause, shift angle before continuing
- Any Name or Pitch left blank: BREACH-MINOR; correct before exit (Table 1B Phase 5 row)

Exit Phase 5:
- [ ] 22–38 Name+Pitch pairs; no categories/rationales/T-Evidence assigned
- [ ] No `**` marks — BREACH-FATAL if any `**` assigned before Phase 7
- [ ] No blank Name/Pitch cells — BREACH-MINOR; correct before exit
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
- T-Evidence column must be present; blank cells: BREACH-MINOR if <1/3 rows; BREACH-MAJOR if
  column absent (see Table 1B Phase 6 row for correction action)
- Check concentration cap on completion: if any category now exceeds 40%, redistribute
  before exiting — BREACH-MAJOR if cap exceeded at exit
- Final candidate count must be 20–40 — BREACH-MAJOR if outside range

Exit Phase 6:
- [ ] All candidates have all 4 anatomy fields — BREACH-MAJOR if any field missing
- [ ] T-Evidence column present with structured notation on every row — apply Table 1B Phase 6 row if not
- [ ] No category exceeds 40% — BREACH-MAJOR if cap exceeded
- [ ] Candidate count 20–40 — BREACH-MAJOR if outside range
- [ ] Any FAIL → apply correction per Table 1B Phase 6 row before Phase 7
Ledger obligation satisfied: Cluster table with T-Evidence structured notation on every row.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — ADVERSARIAL CHALLENGE
Entry: Phase 6 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Identify 8–10 tentative top candidates by T-Evidence pre-score. Do NOT mark `**` yet.

Challenge table — T-3 evaluated via 5 dedicated anchor-field columns as declared in Table 1A:

| # | Candidate | Ph6 Pre-Score | T-1: Differentiation | T-2: Topic Fit | T-3: Costs | T-3: Benefits | T-3: Competitive Threshold | T-3: Bypasses | T-3: Preserves | T-4: Category Coverage | T-3 Dims Cleared | Verdict |
|---|-----------|--------------|---------------------|---------------|-----------|--------------|--------------------------|--------------|---------------|----------------------|-----------------|---------|

Rules:
- Ph6 Pre-Score: carry forward T-Evidence notation exactly from Phase 6 — column absent:
  apply Table 1B Phase 7 row (BREACH-MAJOR)
- T-3 anchor field columns: each column header uses the Phase 4 anchor field label exactly,
  as pre-committed in Table 1A. Enter PASS / PARTIAL / FAIL for each field independently.
  Merged single T-3 column is a BREACH-MAJOR — apply Table 1B Phase 7 row
- T-3 Dims Cleared: count PASS cells across the 5 T-3 anchor columns (e.g., "3 of 5")
- Verdict: PASS if T-1, T-2, T-4 all PASS and T-3 Dims Cleared ≥ 3; otherwise FAIL
- Select exactly 5 `**` candidates from PASS verdicts, spanning ≥3 categories
- If fewer than 5 PASS verdicts: BREACH-MAJOR — return to Phase 6, strengthen candidates

Exit Phase 7:
- [ ] Ph6 Pre-Score column present and populated — apply Table 1B Phase 7 row if absent
- [ ] T-3 evaluated via 5 separate anchor-named columns (schema matches Table 1A exactly) — BREACH-MAJOR if merged
- [ ] T-3 column headers match Phase 4 anchor field labels — BREACH-MINOR if any header renamed
- [ ] Exactly 5 PASS verdicts selected as `**` candidates spanning ≥3 categories
- [ ] No `**` marks assigned before this phase — BREACH-FATAL if any pre-assigned
- [ ] Any FAIL → apply correction per Table 1B Phase 7 row
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
| Phase 7 | Ph6 Pre-Score column + 5 anchor-named T-3 columns | | | |

Reconstruct T-3 column headers observed:
Read the Phase 7 table header row. List the exact T-3 column headers as they appear:
  Observed: [list each T-3-prefixed header exactly as written in Phase 7]
  Expected: T-3: Costs | T-3: Benefits | T-3: Competitive Threshold | T-3: Bypasses | T-3: Preserves
  Match result per header: [MATCH / MISMATCH for each of the 5 expected labels]
  C-27 verdict: PASS (all 5 match) / PARTIAL (some match) / FAIL (single merged column or wrong labels)

Rules:
- Declared Severity: classify any VIOLATION per Table 1C — no violation recorded without severity
- Apply Table 1B correction protocol for the declared severity before Phase 9B
- All rows must reach COMPLETE before Phase 9B begins

Exit Phase 9A:
- [ ] All 5 ledger rows assessed with Status and Declared Severity
- [ ] Reconstruct T-3 headers step completed; C-27 verdict rendered
- [ ] All VIOLATION rows corrected per Table 1B correction protocol
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
| 14 | Phase 7 T-3 evaluated via 5 separate anchor-named columns | PASS/FAIL | BREACH-MAJOR |
| 15 | Table 1B carries BREACH Tier column; every row populated | PASS/FAIL | BREACH-MAJOR |
| 16 | Phase 9A Reconstruct T-3 step completed; C-27 verdict rendered | PASS/FAIL | BREACH-MAJOR |

Apply Table 1C correction protocol for every FAIL before finalizing the artifact.
```

---

## V-02 — Single-axis: Reconstruct Protocol Granularity (C-42 Direct)

**Variation axis:** Phase 9A's Reconstruct step is expanded to a 5-step literal quote-and-compare
protocol. Step 1 quotes the raw Phase 7 header row verbatim. Step 2 extracts only the T-3
prefixed headers. Step 3 maps each observed header to the expected label. Step 4 flags any
deviation as a schema violation with a BREACH tier. Step 5 renders the C-27 verdict from the
step 4 mapping table. The verdict is derived from evidence, not recalled from memory.

**Hypothesis:** C-42 closes when Phase 9A forces literal re-reading of Phase 7 output before
the C-27 verdict. The minimal implementation is a single "list headers, compare, verdict" step.
The risk of a minimal implementation is that the model summarizes the comparison from recall
rather than literal inspection. A 5-step protocol — quote verbatim, extract, map, flag, verdict
— breaks the comparison into discrete actions where each step's output is the input to the next,
making it impossible to skip the inspection and jump to verdict from memory.

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
| T-1 | Differentiation | Meaningfully distinct mechanism from every other `**` candidate | Single column: "T-1: Differentiation" | Removing this candidate eliminates an approach not covered by remaining 4 |
| T-2 | Topic Fit | Rationale names a specific dimension of `{{topic}}` — not generic | Single column: "T-2: Topic Fit" | Rationale fails if topic is swapped out |
| T-3 | Inertia Displacement | PASS on ≥3 of 5 anchor fields evaluated independently | **Five columns:** "T-3: Costs" / "T-3: Benefits" / "T-3: Competitive Threshold" / "T-3: Bypasses" / "T-3: Preserves" — exact labels locked at Phase 1 | Candidate names ≥3 PASS cells across 5 anchor-named T-3 columns |
| T-4 | Category Coverage | Candidate's category not represented by other 4 `**` picks | Single column: "T-4: Category Coverage" | Removing this pick collapses top-5 below 3 categories |

Survival threshold: All four tests PASS. 3/4 is not a `**` pick.
T-3 Phase 7 column schema is LOCKED at Phase 1 exit — deviation is BREACH-MAJOR.
Challenge framework locked after Phase 1 exit — modification is BREACH-FATAL.

#### Table 1B — Evidence Ledger Blueprint

| Phase | Contributing Phase Name | Ledger Field Populated | Ledger Violation Condition | BREACH Tier if Violated |
|-------|------------------------|------------------------|----------------------------|------------------------|
| Phase 3 | Architecture Declaration | AMEND Source col + Primary Challenge Test col on every row | Any row missing either column | BREACH-MAJOR |
| Phase 4 | Do Nothing Anchor | Challenge Binding col on every anchor field row | Any anchor row missing Challenge Binding | BREACH-MAJOR |
| Phase 5 | Diverge | Name + Pitch on every candidate row | Any candidate missing Name or Pitch | BREACH-MINOR |
| Phase 6 | Cluster + T-Evidence | T-Evidence col with structured notation `T-1:[v]·T-2:[v]·T-3:[dims]·T-4:[v]` on every row | Blank T-Evidence cell; unstructured notation | BREACH-MAJOR if col absent; BREACH-MINOR if <1/3 blank |
| Phase 7 | Adversarial Challenge | Ph6 Pre-Score col + T-3 via 5 locked anchor-named cols | Missing Ph6 Pre-Score; merged T-3 col; headers deviate from Table 1A | BREACH-MAJOR (BREACH-FATAL if `**` pre-assigned) |

#### Table 1C — BREACH Severity Taxonomy

| Severity | Definition | Correction Protocol | Continue Before Correcting? |
|----------|------------|---------------------|-----------------------------|
| BREACH-MINOR | Recommended field absent or generic; <1/3 rows missing structured content; AMEND directions overlap on one axis | Correct in-place; mark `[corrected]` | YES |
| BREACH-MAJOR | Required ledger column absent; concentration cap exceeded at phase exit; candidate count outside 20–40; T-3 schema deviation in Phase 7 | HALT current phase; reconstruct affected table; re-verify before advancing | NO |
| BREACH-FATAL | Candidates generated before Phase 1; `**` assigned before Phase 7 completes; anchor entirely absent; framework modified after lock | STOP; discard output from originating phase forward; restart that phase | NO |

Exit Phase 1:
- [ ] Table 1A: T-1 through T-4 with Pass Threshold and Phase 7 Column Schema — BREACH-FATAL if absent
- [ ] Table 1A: T-3 row names all 5 Phase 7 column labels exactly — BREACH-MAJOR if any label missing
- [ ] Table 1B: 5 obligation rows; BREACH Tier if Violated column present and populated — BREACH-MAJOR if column absent
- [ ] Table 1C: All 3 severity tiers with Definition, Correction Protocol, Continue decision — BREACH-MAJOR if any tier missing
- [ ] Challenge framework locked
- [ ] Any FAIL → identify BREACH tier from Table 1C, apply correction before Phase 2
Ledger obligation satisfied: Phase 1 framework, blueprint (with BREACH Tier column), taxonomy declared.

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
- Direction: A1, A2, A3 must pull in non-overlapping directions — duplicate: BREACH-MINOR, revise
- Downstream Effect: `{{topic}}`-specific — "more options" fails C-12

Exit Phase 2:
- [ ] Exactly 3 rows; all columns filled — BREACH-MINOR if any column blank
- [ ] Directions are all distinct — BREACH-MINOR if duplicate; revise before exit
- [ ] Downstream Effects are `{{topic}}`-specific — BREACH-MINOR if generic
Ledger obligation satisfied: AMEND adjustments declared.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3 — ARCHITECTURE DECLARATION
Entry: Phase 2 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Category | Description | Target Count | % of Pool | AMEND Source | Primary Challenge Test |
|----------|-------------|--------------|-----------|--------------|------------------------|

Total: ______

Rules: ≥4 categories; largest ≤40%; totals sum to 20–40; every row has AMEND Source and
Primary Challenge Test; ≥1 row lists T-3.

Exit Phase 3:
- [ ] 4+ categories; % computed; no category ≥40% — BREACH-MAJOR if cap exceeded
- [ ] AMEND Source column present; every row populated
- [ ] Primary Challenge Test column present; ≥1 row lists T-3
- [ ] Totals sum to 20–40
Ledger obligation satisfied: Architecture table carries AMEND Source and Primary Challenge Test.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — DO NOTHING ANCHOR
Entry: Phase 3 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Field | Content | Challenge Binding |
|-------|---------|-------------------|
| Costs | [active costs of status quo for `{{topic}}`] | T-3 |
| Benefits | [genuine appeal of status quo — why inertia is attractive] | T-3 |
| Competitive Threshold | [minimum advantage an alternative must show; reference a Phase 3 category] | T-3 |
| Bypasses | [Phase 3 category labels the status quo renders unnecessary — name ≥1] | T-3 |
| Preserves | [what a transition would put at risk for `{{topic}}`] | T-3 |
| Net Position | [integrated judgment: does inertia dominate? name displacement condition] | T-3 synthesis |

Rules: Costs+Benefits both present; Bypasses+Preserves name Phase 3 labels; Net Position
integrative not restatement; Challenge Binding column present on every row.

Exit Phase 4:
- [ ] All 6 field rows present
- [ ] Challenge Binding column present; all rows populated — BREACH-MAJOR if column absent
- [ ] Costs AND Benefits both present — BREACH-MINOR if costs-only
- [ ] Net Position names a displacement condition — BREACH-MINOR if not
Ledger obligation satisfied: Anchor table carries Challenge Binding on every row.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5 — DIVERGE (Name + Pitch Only)
Entry: Phase 4 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Generate 22–38 Name+Pitch pairs. No categories, rationales, or T-Evidence yet.
No `**` marks — BREACH-FATAL if any `**` assigned before Phase 7.

Exit Phase 5:
- [ ] 22–38 Name+Pitch pairs; no extra fields — BREACH-MINOR if extra fields present
- [ ] No `**` marks — BREACH-FATAL if any assigned
Ledger obligation satisfied: Diverge output available for cluster phase.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6 — CLUSTER + T-EVIDENCE
Entry: Phase 5 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| # | Name | Pitch | Category | Rationale | T-Evidence |
|---|------|-------|----------|-----------|------------|

T-Evidence format: `T-1:PASS/PARTIAL/FAIL · T-2:PASS/PARTIAL/FAIL · T-3:[dims cleared] · T-4:PASS/PARTIAL/FAIL`

Rationale must reference a specific dimension of `{{topic}}`. Concentration cap ≤40% enforced.
Final count 20–40.

Exit Phase 6:
- [ ] All 4 anatomy fields + T-Evidence on every row — BREACH-MAJOR if any field missing
- [ ] T-Evidence column with structured notation — BREACH-MAJOR if column absent
- [ ] No category ≥40%; count 20–40
Ledger obligation satisfied: Cluster table with T-Evidence structured notation on every row.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — ADVERSARIAL CHALLENGE
Entry: Phase 6 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Identify 8–10 tentative top candidates. Do NOT mark `**` yet.

| # | Candidate | Ph6 Pre-Score | T-1: Differentiation | T-2: Topic Fit | T-3: Costs | T-3: Benefits | T-3: Competitive Threshold | T-3: Bypasses | T-3: Preserves | T-4: Category Coverage | T-3 Dims Cleared | Verdict |
|---|-----------|--------------|---------------------|---------------|-----------|--------------|--------------------------|--------------|---------------|----------------------|-----------------|---------|

Ph6 Pre-Score: carry forward T-Evidence from Phase 6 exactly — column absent: BREACH-MAJOR.
T-3 anchor columns: use exact labels from Table 1A T-3 schema. Merged single T-3 column: BREACH-MAJOR.
Verdict: PASS if T-1, T-2, T-4 all PASS and T-3 Dims Cleared ≥3. Select exactly 5 `**` from PASS.

Exit Phase 7:
- [ ] Ph6 Pre-Score column present and populated
- [ ] T-3 via 5 separate anchor-named columns (schema matches Table 1A)
- [ ] Exactly 5 PASS verdicts selected as `**`; span ≥3 categories
- [ ] No `**` assigned before this phase — BREACH-FATAL if pre-assigned
Ledger obligation satisfied: Challenge table with Ph6 Pre-Score + 5 anchor-named T-3 columns.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 8 — ARTIFACT ASSEMBLY
Entry: Phase 7 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write artifact at: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md

Structure: Header | AMEND | Candidate pool grouped by category with `**` on 5 | Do Nothing anchor.

Exit Phase 8:
- [ ] Artifact written to correct path; all sections present; `**` count = 5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9A — TERMINAL LEDGER AUDIT
Entry: Phase 8 complete.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Audit the evidence ledger. Phase 9B may not begin until Phase 9A is complete and all rows COMPLETE.

| Phase | Ledger Field Expected | Status | Declared Severity | Notes |
|-------|----------------------|--------|-------------------|-------|
| Phase 3 | AMEND Source col + Primary Challenge Test col on every row | | | |
| Phase 4 | Challenge Binding col on every anchor row | | | |
| Phase 5 | Name + Pitch on every candidate row | | | |
| Phase 6 | T-Evidence with structured notation on every row | | | |
| Phase 7 | Ph6 Pre-Score col + 5 anchor-named T-3 cols | | | |

Reconstruct T-3 column headers observed — 5-step protocol:

Step 1 — Quote verbatim:
  Copy the Phase 7 table header row exactly as written, character for character:
  "[paste header row here]"

Step 2 — Extract T-3 headers:
  List only the headers that begin with "T-3:":
  Extracted: [list]

Step 3 — Map to expected labels:
  | Expected Label | Observed Label | Match? |
  |----------------|----------------|--------|
  | T-3: Costs | | MATCH / MISMATCH |
  | T-3: Benefits | | MATCH / MISMATCH |
  | T-3: Competitive Threshold | | MATCH / MISMATCH |
  | T-3: Bypasses | | MATCH / MISMATCH |
  | T-3: Preserves | | MATCH / MISMATCH |

Step 4 — Flag deviations:
  For each MISMATCH row: declare BREACH-MAJOR and state the correction (rename the header
  to the expected label; re-run Phase 7 if the column was merged or absent).

Step 5 — C-27 verdict:
  PASS: all 5 rows MATCH and observed labels are column headers (not row labels or cell content)
  PARTIAL: some rows MATCH; missing labels appeared as prose inside a single column
  FAIL: T-3 evaluated in a single merged column; anchor labels not present as column headers
  C-27 verdict: [PASS / PARTIAL / FAIL]

Rules:
- Step 1 must quote the Phase 7 header row — a paraphrase or description does not satisfy Step 1
- Step 3 mapping table must be complete before Step 5 verdict
- A BREACH-MAJOR from Step 4 must be corrected before Phase 9B begins

Exit Phase 9A:
- [ ] All 5 ledger rows assessed with Status and Declared Severity
- [ ] Reconstruct 5-step protocol completed; Step 3 mapping table fully populated
- [ ] C-27 verdict rendered from Step 5 (not from recall)
- [ ] All VIOLATION rows corrected per Table 1C protocol

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
| 12 | Table 1C BREACH taxonomy present with all 3 tiers | PASS/FAIL | BREACH-FATAL |
| 13 | Phase 9A Declared Severity column populated for all audit rows | PASS/FAIL | BREACH-MAJOR |
| 14 | Phase 7 T-3 evaluated via 5 separate anchor-named columns | PASS/FAIL | BREACH-MAJOR |
| 15 | Table 1B carries BREACH Tier if Violated column; every row populated | PASS/FAIL | BREACH-MAJOR |
| 16 | Phase 9A Reconstruct 5-step protocol completed; C-27 verdict from Step 5 | PASS/FAIL | BREACH-MAJOR |

Apply Table 1C correction protocol for every FAIL before finalizing.
```

---

## V-03 — Single-axis: Phrasing Register (Conversational with C-41 + C-42)

**Variation axis:** All phase instructions use conversational, present-tense descriptive framing.
Structural requirements — including the C-41 BREACH Tier column in Table 1B and the C-42
Reconstruct step in Phase 9A — are embedded naturally in the phase descriptions rather than
declared as formal schema requirements. Phase separators are lightweight section labels.

**Hypothesis:** Conversational phrasing reduces the cognitive cost of instruction parsing for
the executing model. When instructions narrate what is being built rather than mandate what must
be produced, the model treats the structure as purposeful context rather than a checklist to
satisfy at minimum viable level. The risk is that conversational framing softens the force of
structural requirements. This variation tests whether C-41 and C-42 can be passed under a
conversational register where the BREACH Tier column and Reconstruct step are introduced as
natural parts of the workflow rather than as explicitly mandated artifacts.

---

```
You are generating a brainstorm artifact for the topic: `{{topic}}`
Output date: `{{date}}`
Artifact path: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md

---

## Phase 1 — Setting up the challenge framework and ledger contract

You're beginning by building the evaluation infrastructure — everything you'll use to judge
candidates later. Nothing gets generated yet. Phase 1 has three things to produce.

First, build your challenge framework (Table 1A). You're declaring exactly how a `**` pick earns
its mark. Four tests: T-1 checks whether a candidate is genuinely distinct from its peers;
T-2 checks whether its rationale is specific to `{{topic}}` rather than generic; T-3 checks
whether it can displace the status quo by winning on at least 3 of 5 anchor dimensions — and
for T-3, you're pre-committing the exact Phase 7 column names right now, so there's no ambiguity
later: the five columns will be "T-3: Costs", "T-3: Benefits", "T-3: Competitive Threshold",
"T-3: Bypasses", and "T-3: Preserves"; T-4 checks whether removing the pick would collapse the
top-5 set below 3 categories. A candidate earns `**` only if it passes all four tests.

Second, build your ledger contract (Table 1B). You're declaring which phases contribute to the
evidence record, what each phase is responsible for producing, what a violation looks like, and —
this is important — what severity tier applies if that obligation is missed. The BREACH Tier
column in Table 1B is what fuses the ledger blueprint with the violation taxonomy: you don't
need to cross-reference a separate table to know what a missing Ph6 Pre-Score column costs you.
For Phase 7, the BREACH Tier is MAJOR for a missing Ph6 Pre-Score column or a merged T-3 column;
it's FATAL if `**` marks appear before Phase 7 completes.

Third, declare your violation taxonomy (Table 1C) with three tiers: MINOR (correct inline, keep
going), MAJOR (halt, reconstruct the affected table, re-verify), FATAL (stop, discard, restart
the originating phase). Each tier needs a clear definition and a correction protocol.

All three tables must be complete before you move on. The challenge framework is locked after
Phase 1 — changing T-3's column schema later is a BREACH-MAJOR.

Before you leave Phase 1, verify:
- Table 1A has T-1 through T-4 with the 5 Phase 7 T-3 column labels explicitly named
- Table 1B has 5 obligation rows, each with a BREACH Tier column entry
- Table 1C has all 3 tiers with definition, correction protocol, and continue decision

---

## Phase 2 — Writing the AMEND adjustments

Before you think about categories or candidates, write down three ways you could shape the
pool differently. These are your AMEND adjustments. Each one names a specific dimension to
shift (not "be more creative" — name the actual dimension), the direction of the shift, and
what it would do to the pool downstream for `{{topic}}`'s context specifically.

The three adjustments need to pull in genuinely different directions — if two of them are both
pushing toward "more ambitious", consolidate or redirect one before continuing.

When you're done, check: exactly 3 rows, all columns filled, directions distinct, downstream
effects are `{{topic}}`-specific.

---

## Phase 3 — Declaring the category architecture

Now you're committing to the shape of the pool before a single candidate is named. Build the
architecture table with these columns: Category, Description, Target Count, % of Pool,
AMEND Source, Primary Challenge Test.

You need at least 4 categories. No single category can hold 40% or more of the total pool — if
your biggest category is at or above that threshold, redistribute before you continue; leaving it
at 40%+ is a BREACH-MAJOR. The total target count should land between 20 and 40.

Every row gets an AMEND Source (A1, A2, or A3 — or "Core" for baseline coverage) and a Primary
Challenge Test. At least one category should be primarily serving T-3 — the inertia displacement
test — since that's what the Do Nothing anchor is designed to pressure.

Before you leave Phase 3, check that both AMEND Source and Primary Challenge Test are populated
on every row.

---

## Phase 4 — Writing the Do Nothing anchor

After committing to the category architecture, you write the status quo entry. This is the
comparator everything else will be measured against in Phase 7. The anchor needs 6 fields:
Costs, Benefits, Competitive Threshold, Bypasses, Preserves, and Net Position. Each gets a
Challenge Binding column entry mapping it back to T-3 (Net Position maps to "T-3 synthesis").

A few things that will cause problems later if you skip them: (1) Bypasses and Preserves need
to name actual Phase 3 category labels — if you write generics, the T-3 evaluation in Phase 7
will be weaker. (2) Net Position needs to name a specific condition under which inertia stops
dominating — a directional statement like "inertia is strong" without a condition is a BREACH-MINOR.
(3) The Challenge Binding column needs to be present and populated on every row — missing it is
a BREACH-MAJOR.

The Do Nothing entry does not count toward the 20–40 candidate total.

---

## Phase 5 — Diverge: names and pitches only

Generate candidate names and one-line pitches. Nothing else yet — no categories, no rationales,
no T-Evidence. You're in pure diverge mode; categorization comes in Phase 6. Target 22–38 pairs.

Don't mark anyone `**` — that's Phase 7 territory. If you mark `**` here, that's a BREACH-FATAL.

If one conceptual area starts dominating the list, pause and shift angle before continuing —
check yourself against the Phase 3 category commitments.

---

## Phase 6 — Cluster: assign category, rationale, and T-Evidence

Now take every candidate from Phase 5 and assign Category, Rationale, and T-Evidence to each.

The full cluster table has columns: #, Name, Pitch, Category, Rationale, T-Evidence.

For T-Evidence, use this format for every row:
`T-1:PASS/PARTIAL/FAIL · T-2:PASS/PARTIAL/FAIL · T-3:[dims cleared, e.g. Costs+Benefits] · T-4:PASS/PARTIAL/FAIL`

Rationale should be specific to `{{topic}}` — if it reads like it could apply to any topic,
rewrite it. After filling all rows, check concentration: if any category holds more than 40% of
the total, redistribute before exiting. Final count must be 20–40.

---

## Phase 7 — Adversarial challenge

Identify 8–10 tentative top candidates by T-Evidence. Build the challenge table. Do not assign
`**` marks yet.

The challenge table columns are:
`# | Candidate | Ph6 Pre-Score | T-1: Differentiation | T-2: Topic Fit | T-3: Costs | T-3: Benefits | T-3: Competitive Threshold | T-3: Bypasses | T-3: Preserves | T-4: Category Coverage | T-3 Dims Cleared | Verdict`

The five T-3 columns use the exact labels pre-committed in Table 1A. Do not merge them into a
single T-3 column — that's a BREACH-MAJOR. The Ph6 Pre-Score column carries forward each
candidate's T-Evidence from Phase 6 exactly.

Verdict rule: PASS if T-1, T-2, T-4 all PASS and T-3 Dims Cleared ≥3. Select exactly 5
`**` candidates from PASS verdicts, spanning at least 3 categories.

---

## Phase 8 — Write the artifact

Write the artifact at: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md

Include: header (topic, date, count, `**` count), AMEND section, candidate pool grouped by
category with `**` marks on exactly 5, and the Do Nothing anchor as its own section.

---

## Phase 9A — Terminal ledger audit

Run the ledger audit before the criterion checklist. Phase 9B can't begin until all ledger
rows show COMPLETE.

Build the audit table with columns: Phase | Ledger Field Expected | Status | Declared Severity | Notes.

For each of the 5 contributing phases (3 through 7), check whether the committed ledger field
is present and populated. Any VIOLATION needs a Declared Severity classification from Table 1C —
no violation is recorded without one.

Then run the Reconstruct step for T-3 column headers observed:

Read the Phase 7 table header row. List the T-3 column headers exactly as they appear in
Phase 7's output:
  Observed T-3 headers: [list]
  Expected headers: T-3: Costs | T-3: Benefits | T-3: Competitive Threshold | T-3: Bypasses | T-3: Preserves
  Match result: [MATCH / MISMATCH for each]
  C-27 verdict: PASS if all 5 match as column headers / PARTIAL if some match / FAIL if merged

Any MISMATCH is a BREACH-MAJOR — correct Phase 7 before Phase 9B.

---

## Phase 9B — Criterion checklist

Phase 9A must be complete before starting here.

| Row | Criterion | Status | Severity if FAIL |
|-----|-----------|--------|-----------------|
| 1 | Candidate count 20–40 | PASS/FAIL | BREACH-MAJOR |
| 2 | Every candidate has all 4 anatomy fields | PASS/FAIL | BREACH-MAJOR |
| 3 | Exactly 5 `**` marks | PASS/FAIL | BREACH-MAJOR |
| 4 | Do Nothing with 6 fields including Net Position | PASS/FAIL | BREACH-MAJOR |
| 5 | AMEND: 3 adjustments with dimension, direction, downstream effect | PASS/FAIL | BREACH-MINOR |
| 6 | Phase 3 AMEND Source column, all rows | PASS/FAIL | BREACH-MAJOR |
| 7 | Phase 3 Primary Challenge Test column, ≥1 T-3 row | PASS/FAIL | BREACH-MAJOR |
| 8 | Phase 6 T-Evidence with structured notation | PASS/FAIL | BREACH-MAJOR |
| 9 | Phase 7 Ph6 Pre-Score carryforward column | PASS/FAIL | BREACH-MAJOR |
| 10 | `**` candidates span ≥3 categories | PASS/FAIL | BREACH-MAJOR |
| 11 | Phase 4 Challenge Binding column; Net Position maps to T-3 synthesis | PASS/FAIL | BREACH-MAJOR |
| 12 | Table 1C BREACH taxonomy, all 3 tiers | PASS/FAIL | BREACH-FATAL |
| 13 | Phase 9A Declared Severity column populated | PASS/FAIL | BREACH-MAJOR |
| 14 | Phase 7 T-3 via 5 anchor-named columns | PASS/FAIL | BREACH-MAJOR |
| 15 | Table 1B BREACH Tier column present and populated | PASS/FAIL | BREACH-MAJOR |
| 16 | Phase 9A Reconstruct step completed; C-27 verdict rendered | PASS/FAIL | BREACH-MAJOR |

Correct any FAIL before finalizing.
```

---

## V-04 — Combined axes: BREACH Tier Fusion + Lifecycle Emphasis (Bidirectional Gate Sealing)

**Variation axes:** BREACH Tier fusion depth (C-41), lifecycle emphasis
**Hypothesis:** Bidirectional gate sealing — every phase opens with an explicit ENTRY TABLE
listing what must be satisfied from the preceding phase, and closes with an EXIT TABLE listing
what must be satisfied before the next phase — enforces the dependency chain from both sides.
Combined with a fused Table 1B/1C where every ledger obligation row carries its own violation
tier and correction protocol, the model has a row-local lookup for both the structural requirement
AND the violation response at every phase transition. This doubles the gate formalism: departure
from any phase is blocked by exit conditions; arrival at any phase is blocked by entry conditions
that name what predecessor outputs must exist.

---

```
You are generating a brainstorm artifact for the topic: `{{topic}}`
Output date: `{{date}}`
Artifact path: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 1 — CHALLENGE FRAMEWORK + LEDGER CONTRACT + BREACH TAXONOMY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 1
| Precondition | Status |
|--------------|--------|
| Start of session — no prior phases | SATISFIED |

Declare three co-equal Phase 1 artifacts before any generation begins.

#### Table 1A — Challenge Framework

| ID | Test | Pass Threshold | Phase 7 Column Schema | Survival Condition |
|----|------|----------------|-----------------------|--------------------|
| T-1 | Differentiation | Meaningfully distinct mechanism from every other `**` candidate | "T-1: Differentiation" | Removing this candidate eliminates an approach not covered by remaining 4 |
| T-2 | Topic Fit | Rationale names a specific dimension of `{{topic}}` — not generic | "T-2: Topic Fit" | Rationale fails if topic is swapped out |
| T-3 | Inertia Displacement | PASS on ≥3 of 5 anchor fields independently | **Five columns:** "T-3: Costs" / "T-3: Benefits" / "T-3: Competitive Threshold" / "T-3: Bypasses" / "T-3: Preserves" (exact labels locked) | Names ≥3 PASS cells across 5 anchor-named T-3 columns |
| T-4 | Category Coverage | Candidate's category absent from other 4 `**` picks | "T-4: Category Coverage" | Removing this collapses top-5 below 3 categories |

Survival: All 4 tests PASS. T-3 Phase 7 schema LOCKED at Phase 1 exit. Framework LOCKED at Phase 1 exit.

#### Table 1B — Ledger Contract (Blueprint + Taxonomy fused; per-row correction authority)

| Phase | Phase Name | Ledger Field Populated | Violation Condition | BREACH Tier | Correction Action | Continue? |
|-------|-----------|------------------------|---------------------|-------------|-------------------|-----------|
| 3 | Architecture | AMEND Source + Primary Challenge Test cols on every row | Any row missing either column | BREACH-MAJOR | Halt. Add missing column. Repopulate. Re-verify. | NO |
| 4 | Do Nothing Anchor | Challenge Binding col on every anchor row | Any anchor row missing Challenge Binding | BREACH-MAJOR | Halt. Add column. Correct all rows. | NO |
| 5 | Diverge | Name + Pitch on every candidate row | Any candidate missing Name or Pitch | BREACH-MINOR | Correct cell in-place. Mark `[corrected]`. | YES |
| 6 | Cluster + T-Evidence | T-Evidence col with `T-1:[v]·T-2:[v]·T-3:[dims]·T-4:[v]` on every row | Col absent; >1/3 rows unstructured | BREACH-MAJOR if col absent; BREACH-MINOR if <1/3 blank | Col absent: halt, add, repopulate. Blank cells: correct inline. | Col absent: NO. Cells: YES |
| 7 | Adversarial Challenge | Ph6 Pre-Score col + T-3 via 5 locked anchor-named cols | Missing Ph6 Pre-Score; merged T-3 col; header labels deviate from Table 1A | BREACH-FATAL if `**` pre-assigned; BREACH-MAJOR for schema deviations | Pre-assigned `**`: stop, discard Phase 7+, restart. Schema: halt, reconstruct. | NO |

#### Table 1C — BREACH Severity Taxonomy

| Severity | Definition | Correction Protocol | Continue? |
|----------|------------|---------------------|-----------|
| BREACH-MINOR | Recommended field absent; <1/3 rows missing content; overlapping AMEND directions | Correct in-place; mark `[corrected]` | YES |
| BREACH-MAJOR | Required ledger column absent; concentration cap exceeded at exit; count outside 20–40; T-3 schema deviated in Phase 7 | HALT; reconstruct affected table; re-verify before advancing | NO |
| BREACH-FATAL | Candidates before Phase 1; `**` before Phase 7; anchor absent; framework modified after lock | STOP; discard from originating phase; restart | NO |

EXIT TABLE — Phase 1
| Condition | Status | BREACH if FAIL |
|-----------|--------|----------------|
| Table 1A: T-1 through T-4 with Phase 7 Column Schema; T-3 names all 5 column labels | | BREACH-FATAL if absent |
| Table 1B: 5 obligation rows; BREACH Tier column present and populated on every row | | BREACH-MAJOR if column absent |
| Table 1B: Correction Action + Continue? columns present on every row | | BREACH-MAJOR if absent |
| Table 1C: All 3 severity tiers with Definition, Correction Protocol, Continue decision | | BREACH-MAJOR if any tier missing |
| Challenge framework locked | | — |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — AMEND ADJUSTMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 2
| Precondition | Status |
|--------------|--------|
| Phase 1 exit gates: all PASS | |
| Table 1A locked; T-3 column schema committed | |
| Table 1B BREACH Tier column populated on all 5 rows | |

Write exactly 3 pool-shaping adjustments before architecture or candidates are generated.

| # | Dimension | Direction | Downstream Effect on Pool |
|---|-----------|-----------|--------------------------|
| A1 | | | |
| A2 | | | |
| A3 | | | |

Rules: Dimension is a specific axis; Directions non-overlapping; Downstream Effects `{{topic}}`-specific.

EXIT TABLE — Phase 2
| Condition | Status | BREACH if FAIL |
|-----------|--------|----------------|
| Exactly 3 AMEND rows; all columns filled | | BREACH-MINOR if any col blank |
| Directions are all distinct | | BREACH-MINOR if duplicate |
| Downstream Effects are `{{topic}}`-specific | | BREACH-MINOR if generic |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3 — ARCHITECTURE DECLARATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 3
| Precondition | Status |
|--------------|--------|
| Phase 2 exit gates: all PASS | |
| 3 AMEND adjustments available; AMEND Source values (A1/A2/A3) ready to assign | |

Declare category structure. No candidates yet.

| Category | Description | Target Count | % of Pool | AMEND Source | Primary Challenge Test |
|----------|-------------|--------------|-----------|--------------|------------------------|

Total: ______

Rules: ≥4 categories; largest ≤40%; totals 20–40; every row has AMEND Source + Primary Challenge
Test; ≥1 row lists T-3. If largest category ≥40%, redistribute before exit — BREACH-MAJOR if not.

EXIT TABLE — Phase 3
| Condition | Status | BREACH if FAIL |
|-----------|--------|----------------|
| 4+ categories; % of Pool computed | | BREACH-MAJOR if <4 |
| No category ≥40% of total | | BREACH-MAJOR if cap exceeded |
| AMEND Source column present; every row populated | | BREACH-MAJOR if col absent |
| Primary Challenge Test column present; ≥1 row lists T-3 | | BREACH-MAJOR if col absent or no T-3 row |
| Totals sum to 20–40 | | BREACH-MAJOR if outside range |
| Ledger obligation: Table 1B Phase 3 row satisfied | | Per Table 1B row |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — DO NOTHING ANCHOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 4
| Precondition | Status |
|--------------|--------|
| Phase 3 exit gates: all PASS | |
| Architecture table with AMEND Source + Primary Challenge Test available | |
| Category labels available for Bypasses / Preserves reference | |

| Field | Content | Challenge Binding |
|-------|---------|-------------------|
| Costs | | T-3 |
| Benefits | | T-3 |
| Competitive Threshold | [reference a Phase 3 category label] | T-3 |
| Bypasses | [name ≥1 Phase 3 category label] | T-3 |
| Preserves | | T-3 |
| Net Position | [integrated judgment; name displacement condition] | T-3 synthesis |

Rules: Costs+Benefits both present; Bypasses+Preserves name Phase 3 labels; Net Position
integrative not restatement; Challenge Binding col present on every row.

EXIT TABLE — Phase 4
| Condition | Status | BREACH if FAIL |
|-----------|--------|----------------|
| All 6 field rows present with `{{topic}}`-specific content | | BREACH-MAJOR |
| Costs AND Benefits both present | | BREACH-MINOR if costs-only |
| Competitive Threshold references a Phase 3 category | | BREACH-MINOR if generic |
| Bypasses and Preserves name Phase 3 category labels | | BREACH-MINOR if generic |
| Net Position names a displacement condition | | BREACH-MINOR if not |
| Challenge Binding column present; all rows populated | | BREACH-MAJOR if col absent |
| Ledger obligation: Table 1B Phase 4 row satisfied | | Per Table 1B row |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5 — DIVERGE (Name + Pitch Only)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 5
| Precondition | Status |
|--------------|--------|
| Phase 4 exit gates: all PASS | |
| Do Nothing anchor (6 fields + Challenge Binding) available | |

Generate 22–38 Name+Pitch pairs only. No categories, rationales, T-Evidence. No `**` marks.

EXIT TABLE — Phase 5
| Condition | Status | BREACH if FAIL |
|-----------|--------|----------------|
| 22–38 Name+Pitch pairs | | BREACH-MAJOR if outside range |
| No extra fields (category/rationale/T-Evidence) | | BREACH-MINOR if present |
| No `**` marks | | BREACH-FATAL if any assigned |
| Ledger obligation: Table 1B Phase 5 row satisfied | | Per Table 1B row |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6 — CLUSTER + T-EVIDENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 6
| Precondition | Status |
|--------------|--------|
| Phase 5 exit gates: all PASS | |
| Diverge list (22–38 Name+Pitch pairs, no `**`) available | |
| Phase 3 category labels available for assignment | |

| # | Name | Pitch | Category | Rationale | T-Evidence |
|---|------|-------|----------|-----------|------------|

T-Evidence format: `T-1:P/PART/F · T-2:P/PART/F · T-3:[dims] · T-4:P/PART/F`
Rationale must be `{{topic}}`-specific. Cap: no category ≥40%.

EXIT TABLE — Phase 6
| Condition | Status | BREACH if FAIL |
|-----------|--------|----------------|
| All 4 anatomy fields + T-Evidence on every candidate | | BREACH-MAJOR |
| T-Evidence column present; structured notation on every row | | BREACH-MAJOR if col absent |
| No category ≥40% of total | | BREACH-MAJOR |
| Candidate count 20–40 | | BREACH-MAJOR |
| Ledger obligation: Table 1B Phase 6 row satisfied | | Per Table 1B row |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — ADVERSARIAL CHALLENGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 7
| Precondition | Status |
|--------------|--------|
| Phase 6 exit gates: all PASS | |
| Cluster table (with T-Evidence) available | |
| No `**` marks have been assigned | |

Identify 8–10 tentative top candidates. Do NOT mark `**` yet.

| # | Candidate | Ph6 Pre-Score | T-1: Differentiation | T-2: Topic Fit | T-3: Costs | T-3: Benefits | T-3: Competitive Threshold | T-3: Bypasses | T-3: Preserves | T-4: Category Coverage | T-3 Dims Cleared | Verdict |
|---|-----------|--------------|---------------------|---------------|-----------|--------------|--------------------------|--------------|---------------|----------------------|-----------------|---------|

Ph6 Pre-Score carries T-Evidence from Phase 6 exactly. T-3 columns use Table 1A locked schema.
Merged T-3 column: BREACH-MAJOR (apply Table 1B Phase 7 row). Verdict: T-1+T-2+T-4 PASS +
T-3 Dims Cleared ≥3 = PASS. Select exactly 5 `**` from PASS verdicts spanning ≥3 categories.

EXIT TABLE — Phase 7
| Condition | Status | BREACH if FAIL |
|-----------|--------|----------------|
| Ph6 Pre-Score column present and populated | | BREACH-MAJOR |
| T-3 via 5 anchor-named cols matching Table 1A schema | | BREACH-MAJOR if merged |
| Exactly 5 PASS verdicts; span ≥3 categories | | BREACH-MAJOR if <5 PASS |
| No `**` assigned before this phase | | BREACH-FATAL if pre-assigned |
| Ledger obligation: Table 1B Phase 7 row satisfied | | Per Table 1B row |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 8 — ARTIFACT ASSEMBLY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 8
| Precondition | Status |
|--------------|--------|
| Phase 7 exit gates: all PASS | |
| Exactly 5 `**` candidates identified from Phase 7 PASS verdicts | |

Write artifact at: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md
Structure: Header | AMEND | Pool by category (`**` on 5) | Do Nothing anchor.

EXIT TABLE — Phase 8
| Condition | Status | BREACH if FAIL |
|-----------|--------|----------------|
| Artifact at correct path | | — |
| All sections present | | BREACH-MAJOR |
| `**` count = 5 | | BREACH-FATAL if count wrong |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9A — TERMINAL LEDGER AUDIT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 9A
| Precondition | Status |
|--------------|--------|
| Phase 8 exit gates: all PASS | |
| Artifact assembled at correct path | |

Audit the evidence ledger. Phase 9B entry gate requires all ledger rows COMPLETE.

| Phase | Ledger Field Expected | Status | Declared Severity | Notes |
|-------|----------------------|--------|-------------------|-------|
| Phase 3 | AMEND Source col + Primary Challenge Test col on every row | | | |
| Phase 4 | Challenge Binding col on every anchor row | | | |
| Phase 5 | Name + Pitch on every candidate row | | | |
| Phase 6 | T-Evidence with structured notation on every row | | | |
| Phase 7 | Ph6 Pre-Score col + 5 anchor-named T-3 cols | | | |

Reconstruct T-3 column headers observed:
  Read the Phase 7 header row. List the exact T-3 column headers as they appear:
    Observed: [list each T-3-prefixed header verbatim]
    Expected: T-3: Costs | T-3: Benefits | T-3: Competitive Threshold | T-3: Bypasses | T-3: Preserves
    Per-label match: [MATCH / MISMATCH for each of the 5 expected labels]
    C-27 verdict: PASS (all 5 MATCH as column headers) / PARTIAL / FAIL (merged or wrong labels)
  Any MISMATCH: BREACH-MAJOR per Table 1B Phase 7 row — correct Phase 7 before Phase 9B.

EXIT TABLE — Phase 9A
| Condition | Status |
|-----------|--------|
| All 5 ledger rows assessed with Status and Declared Severity | |
| Reconstruct T-3 step completed; C-27 verdict rendered from observed output | |
| All VIOLATION rows corrected per Table 1B correction protocol | |
| Declared Severity column populated on every row | |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9B — CRITERION CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 9B
| Precondition | Status |
|--------------|--------|
| Phase 9A exit gates: all PASS | |
| All 5 ledger rows COMPLETE | |
| C-27 verdict rendered | |

| Row | Criterion | Status | Declared Severity if FAIL |
|-----|-----------|--------|--------------------------|
| 1 | Candidate count 20–40 | PASS/FAIL | BREACH-MAJOR |
| 2 | All 4 anatomy fields on every candidate | PASS/FAIL | BREACH-MAJOR |
| 3 | Exactly 5 `**` marks | PASS/FAIL | BREACH-MAJOR |
| 4 | Do Nothing with 6 fields including Net Position | PASS/FAIL | BREACH-MAJOR |
| 5 | AMEND: 3 adjustments, all 3 fields | PASS/FAIL | BREACH-MINOR |
| 6 | Phase 3 AMEND Source col, all rows | PASS/FAIL | BREACH-MAJOR |
| 7 | Phase 3 Primary Challenge Test col, ≥1 T-3 row | PASS/FAIL | BREACH-MAJOR |
| 8 | Phase 6 T-Evidence, structured notation | PASS/FAIL | BREACH-MAJOR |
| 9 | Phase 7 Ph6 Pre-Score carryforward | PASS/FAIL | BREACH-MAJOR |
| 10 | `**` candidates span ≥3 categories | PASS/FAIL | BREACH-MAJOR |
| 11 | Phase 4 Challenge Binding col; Net Position T-3 synthesis | PASS/FAIL | BREACH-MAJOR |
| 12 | Table 1C BREACH taxonomy, 3 tiers | PASS/FAIL | BREACH-FATAL |
| 13 | Phase 9A Declared Severity col populated | PASS/FAIL | BREACH-MAJOR |
| 14 | Phase 7 T-3 via 5 anchor-named cols | PASS/FAIL | BREACH-MAJOR |
| 15 | Table 1B BREACH Tier col present, all rows populated | PASS/FAIL | BREACH-MAJOR |
| 16 | Phase 9A Reconstruct step done; C-27 verdict from observed output | PASS/FAIL | BREACH-MAJOR |

Apply Table 1C correction protocol for every FAIL before finalizing.
```

---

## V-05 — Combined axes: Full R14 Stack (BREACH Tier Fusion + Reconstruct Granularity + 7-Field Anchor)

**Variation axes:** BREACH Tier fusion depth (C-41), Reconstruct protocol granularity (C-42),
inertia framing
**Hypothesis:** Adding a seventh anchor field — Trajectory (what the status quo looks like
in 12 months if preserved unchanged) — and requiring every candidate's Rationale to cite
≥1 anchor field by name makes the anchor structurally generative throughout Phase 6, not just
a terminal comparator at Phase 7. When candidates are generated in explicit reference to anchor
dimensions, the Phase 7 T-3 evaluation becomes adjudication of declared anchor-displacement
claims (Phase 6 already annotated them) rather than a first-pass judgment. Combined with V-01's
fused Table 1B and V-02's 5-step Reconstruct protocol, this variation tests whether the full
R14 stack improves consistency across all three new dimensions simultaneously.

---

```
You are generating a brainstorm artifact for the topic: `{{topic}}`
Output date: `{{date}}`
Artifact path: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 1 — CHALLENGE FRAMEWORK + LEDGER CONTRACT + BREACH TAXONOMY
Entry: Start of session.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Declare three co-equal Phase 1 artifacts. Nothing is generated before Phase 1 completes.

#### Table 1A — Challenge Framework

| ID | Test | Pass Threshold | Phase 7 Column Schema | Survival Condition |
|----|------|----------------|-----------------------|--------------------|
| T-1 | Differentiation | Meaningfully distinct mechanism from every other `**` candidate | "T-1: Differentiation" | Removing this candidate eliminates an approach not covered by remaining 4 |
| T-2 | Topic Fit | Rationale names a specific dimension of `{{topic}}` AND cites ≥1 anchor field by label | "T-2: Topic Fit" | Rationale fails if topic swapped; anchor citation absent is BREACH-MINOR in Phase 6 |
| T-3 | Inertia Displacement | PASS on ≥3 of 7 anchor fields independently | **Seven columns:** "T-3: Costs" / "T-3: Benefits" / "T-3: Competitive Threshold" / "T-3: Bypasses" / "T-3: Preserves" / "T-3: Net Position" / "T-3: Trajectory" — exact labels locked | Candidate names ≥3 PASS cells across 7 anchor-named T-3 columns |
| T-4 | Category Coverage | Candidate's category absent from other 4 `**` picks | "T-4: Category Coverage" | Removing this collapses top-5 below 3 categories |

Survival: All 4 tests PASS. T-2 anchor citation is required (enforced in Phase 6 T-Evidence).
T-3 Phase 7 schema LOCKED at Phase 1 exit — deviation is BREACH-MAJOR.
Challenge framework LOCKED at Phase 1 exit — modification is BREACH-FATAL.

#### Table 1B — Ledger Contract (Blueprint + Taxonomy fused; per-row correction authority)

| Phase | Phase Name | Ledger Field Populated | Violation Condition | BREACH Tier | Correction Action | Continue? |
|-------|-----------|------------------------|---------------------|-------------|-------------------|-----------|
| 3 | Architecture | AMEND Source col + Primary Challenge Test col on every row | Any row missing either column | BREACH-MAJOR | Halt. Add column. Repopulate. Re-verify. | NO |
| 4 | Do Nothing Anchor | Challenge Binding col on every anchor row (7 rows) | Any anchor row missing Challenge Binding | BREACH-MAJOR | Halt. Add column. Correct all rows. | NO |
| 5 | Diverge | Name + Pitch on every candidate row | Any candidate missing Name or Pitch | BREACH-MINOR | Correct in-place. Mark `[corrected]`. | YES |
| 6 | Cluster + T-Evidence | T-Evidence col with structured notation + Anchor Citation col on every row | T-Evidence col absent; Anchor Citation col absent; >1/3 rows missing anchor citation | BREACH-MAJOR if col absent; BREACH-MINOR if <1/3 rows missing citation | Col absent: halt, add, repopulate. Missing citations: correct inline. | Col absent: NO. Cells: YES |
| 7 | Adversarial Challenge | Ph6 Pre-Score col + T-3 via 7 locked anchor-named cols | Missing Ph6 Pre-Score; merged T-3 col; labels deviate from Table 1A | BREACH-FATAL if `**` pre-assigned; BREACH-MAJOR for schema deviations | Pre-assigned `**`: stop, discard Phase 7+, restart. Schema: halt, reconstruct. | NO |

#### Table 1C — BREACH Severity Taxonomy

| Severity | Definition | Correction Protocol | Continue? |
|----------|------------|---------------------|-----------|
| BREACH-MINOR | Recommended field absent; <1/3 rows missing content; AMEND directions overlap; anchor citation missing from <1/3 rationales | Correct in-place; mark `[corrected]` | YES |
| BREACH-MAJOR | Required ledger column absent; concentration cap exceeded; count outside 20–40; T-3 schema deviated; Anchor Citation col absent | HALT; reconstruct affected table; re-verify before advancing | NO |
| BREACH-FATAL | Candidates before Phase 1; `**` before Phase 7 completes; anchor absent; framework modified after lock | STOP; discard from originating phase; restart | NO |

Exit Phase 1:
- [ ] Table 1A: T-1 through T-4 with Phase 7 Column Schema; T-3 row names all 7 column labels — BREACH-FATAL if absent
- [ ] Table 1B: 5 obligation rows; BREACH Tier column present and populated; Correction Action + Continue? cols present — BREACH-MAJOR if any col absent
- [ ] Table 1C: All 3 severity tiers with Definition, Correction Protocol, Continue decision — BREACH-MAJOR if any tier missing
- [ ] Challenge framework locked; T-3 schema locked
- [ ] Any FAIL → apply Table 1B row correction or Table 1C protocol before Phase 2
Ledger obligation satisfied: Phase 1 framework, ledger contract (BREACH Tier column), taxonomy declared.

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

Rules: Dimension is a specific axis; Directions non-overlapping; Downstream Effects `{{topic}}`-specific.

Exit Phase 2:
- [ ] Exactly 3 rows; all columns filled — BREACH-MINOR if any col blank
- [ ] Directions distinct — BREACH-MINOR if duplicate
- [ ] Downstream Effects `{{topic}}`-specific — BREACH-MINOR if generic
Ledger obligation satisfied: AMEND adjustments declared; pool-shaping committed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3 — ARCHITECTURE DECLARATION
Entry: Phase 2 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Declare category structure before generating any candidates.

| Category | Description | Target Count | % of Pool | AMEND Source | Primary Challenge Test |
|----------|-------------|--------------|-----------|--------------|------------------------|

Total: ______

Rules: ≥4 categories; largest ≤40%; totals 20–40; every row has AMEND Source + Primary Challenge
Test; ≥1 row lists T-3. If largest ≥40%, redistribute before exit — BREACH-MAJOR if not.

Exit Phase 3:
- [ ] 4+ categories; % computed; no category ≥40% — BREACH-MAJOR if cap exceeded
- [ ] AMEND Source col present; every row populated
- [ ] Primary Challenge Test col present; ≥1 row lists T-3
- [ ] Totals 20–40
- [ ] Any FAIL → apply Table 1B Phase 3 row before Phase 4
Ledger obligation satisfied: Architecture table carries AMEND Source and Primary Challenge Test.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — DO NOTHING ANCHOR (7 fields)
Entry: Phase 3 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write the status quo anchor grounded in the Phase 3 architecture. Bypasses and Preserves must
reference specific Phase 3 category labels. The anchor now has 7 fields — the 6 from prior
rounds plus Trajectory.

| Field | Content | Challenge Binding |
|-------|---------|-------------------|
| Costs | [active costs of status quo for `{{topic}}`] | T-3 |
| Benefits | [genuine appeal of status quo — why inertia is attractive] | T-3 |
| Competitive Threshold | [minimum advantage an alternative must show; reference a Phase 3 category] | T-3 |
| Bypasses | [Phase 3 category labels the status quo renders unnecessary — name ≥1] | T-3 |
| Preserves | [what a transition would put at risk for `{{topic}}`] | T-3 |
| Net Position | [integrated judgment: does inertia dominate? name the displacement condition] | T-3 synthesis |
| Trajectory | [what the status quo looks like for `{{topic}}` in 12 months if preserved unchanged — improving, stable, or degrading, and on which specific dimensions] | T-3 |

Rules:
- All 7 fields must be present with `{{topic}}`-specific content
- Costs AND Benefits both present — costs-only: BREACH-MINOR
- Bypasses+Preserves name Phase 3 labels — generic: BREACH-MINOR
- Net Position names a displacement condition — directional-only: BREACH-MINOR
- Trajectory names specific dimensions expected to change — vague "things get worse": BREACH-MINOR
- Challenge Binding col present on every row — col absent: BREACH-MAJOR (Table 1B Phase 4 row)
- Do Nothing does NOT count toward 20–40 candidate total

Phase 6 rationale requirement (pre-committed here): Every candidate's Rationale must cite ≥1
anchor field by label (e.g., "displaces Costs by..."; "preserves Bypasses dimension...").
Rationales that fail to cite any anchor field: BREACH-MINOR per candidate.

Exit Phase 4:
- [ ] All 7 field rows present with `{{topic}}`-specific content — BREACH-MAJOR if any row absent
- [ ] Challenge Binding col present; all 7 rows populated — apply Table 1B Phase 4 row if absent
- [ ] Costs AND Benefits both present — BREACH-MINOR if costs-only
- [ ] Trajectory names specific dimensions — BREACH-MINOR if vague
- [ ] Net Position names displacement condition — BREACH-MINOR if not
- [ ] Any FAIL → apply Table 1B Phase 4 row before Phase 5
Ledger obligation satisfied: Anchor table (7 fields) carries Challenge Binding on every row.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5 — DIVERGE (Name + Pitch Only)
Entry: Phase 4 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Generate 22–38 Name+Pitch pairs only. No categories, rationales, anchor citations, T-Evidence.
No `**` marks — BREACH-FATAL if any `**` assigned before Phase 7.

Exit Phase 5:
- [ ] 22–38 Name+Pitch pairs; no extra fields
- [ ] No `**` marks — BREACH-FATAL if any assigned
Ledger obligation satisfied: Diverge output available.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6 — CLUSTER + T-EVIDENCE + ANCHOR CITATION
Entry: Phase 5 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Assign Category, Rationale, Anchor Citation, and T-Evidence to every candidate.

| # | Name | Pitch | Category | Rationale | Anchor Citation | T-Evidence |
|---|------|-------|----------|-----------|-----------------|------------|

Column definitions:
- **Rationale**: must reference a specific dimension of `{{topic}}` AND cite ≥1 anchor field by
  label (e.g., "addresses Costs by..."). Generic rationale with no anchor citation: BREACH-MINOR;
  correct inline before exit.
- **Anchor Citation**: list the anchor field(s) cited in the Rationale
  (e.g., "Costs", "Bypasses + Trajectory"). No anchor field cited: BREACH-MINOR per row.
- **T-Evidence**: `T-1:PASS/PARTIAL/FAIL · T-2:PASS/PARTIAL/FAIL · T-3:[anchor dims cleared] · T-4:PASS/PARTIAL/FAIL`
  For T-3 dims cleared, list the anchor field labels from Phase 4 that the candidate's Rationale
  demonstrates (e.g., "Costs+Benefits+Trajectory").

Rules:
- Anchor Citation col must be present — col absent: BREACH-MAJOR (Table 1B Phase 6 row)
- T-Evidence col must be present — col absent: BREACH-MAJOR
- Concentration cap ≤40%; final count 20–40

Exit Phase 6:
- [ ] All 4 anatomy fields + Anchor Citation + T-Evidence on every candidate
- [ ] Anchor Citation col present; every row has ≥1 anchor field cited — BREACH-MINOR if <1/3 absent
- [ ] T-Evidence col present; structured notation on every row — BREACH-MAJOR if col absent
- [ ] No category ≥40%; count 20–40
- [ ] Any FAIL → apply Table 1B Phase 6 row
Ledger obligation satisfied: Cluster table with T-Evidence + Anchor Citation on every row.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — ADVERSARIAL CHALLENGE
Entry: Phase 6 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Identify 8–10 tentative top candidates by T-Evidence. Do NOT mark `**` yet.

Challenge table — T-3 evaluated via 7 dedicated anchor-field columns as declared in Table 1A:

| # | Candidate | Ph6 Pre-Score | T-1: Differentiation | T-2: Topic Fit | T-3: Costs | T-3: Benefits | T-3: Competitive Threshold | T-3: Bypasses | T-3: Preserves | T-3: Net Position | T-3: Trajectory | T-4: Category Coverage | T-3 Dims Cleared | Verdict |
|---|-----------|--------------|---------------------|---------------|-----------|--------------|--------------------------|--------------|---------------|------------------|----------------|----------------------|-----------------|---------|

Rules:
- Ph6 Pre-Score: carry forward T-Evidence from Phase 6 exactly — col absent: BREACH-MAJOR
- 7 T-3 anchor columns: use exact labels from Table 1A. Merged single T-3 col: BREACH-MAJOR
- T-3 Dims Cleared: count PASS cells across all 7 T-3 anchor columns
- Verdict: T-1+T-2+T-4 PASS + T-3 Dims Cleared ≥3 = PASS
- Select exactly 5 `**` from PASS verdicts spanning ≥3 categories

Exit Phase 7:
- [ ] Ph6 Pre-Score col present and populated — apply Table 1B Phase 7 row if absent
- [ ] T-3 via 7 separate anchor-named cols; schema matches Table 1A exactly — BREACH-MAJOR if merged
- [ ] Exactly 5 PASS verdicts; span ≥3 categories
- [ ] No `**` assigned before this phase — BREACH-FATAL if pre-assigned
- [ ] Any FAIL → apply Table 1B Phase 7 row
Ledger obligation satisfied: Challenge table with Ph6 Pre-Score + 7 anchor-named T-3 columns.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 8 — ARTIFACT ASSEMBLY
Entry: Phase 7 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write artifact at: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md
Structure: Header | AMEND | Pool by category with `**` on 5 | Do Nothing anchor (7 fields).

Exit Phase 8:
- [ ] Artifact at correct path; all sections present; `**` count = 5 — BREACH-FATAL if wrong

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9A — TERMINAL LEDGER AUDIT
Entry: Phase 8 complete.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Phase 9B may not begin until Phase 9A is complete and all ledger rows COMPLETE.

| Phase | Ledger Field Expected | Status | Declared Severity | Notes |
|-------|----------------------|--------|-------------------|-------|
| Phase 3 | AMEND Source col + Primary Challenge Test col on every row | | | |
| Phase 4 | Challenge Binding col on every anchor row (7 rows) | | | |
| Phase 5 | Name + Pitch on every candidate row | | | |
| Phase 6 | T-Evidence + Anchor Citation cols; structured notation on every row | | | |
| Phase 7 | Ph6 Pre-Score col + 7 anchor-named T-3 cols | | | |

Reconstruct T-3 column headers observed — 5-step protocol:

Step 1 — Quote verbatim:
  Copy the Phase 7 table header row exactly as written:
  "[paste header row here]"

Step 2 — Extract T-3 headers:
  List only the headers that begin with "T-3:":
  Extracted: [list]

Step 3 — Map to expected labels:
  | Expected Label | Observed Label | Match? |
  |----------------|----------------|--------|
  | T-3: Costs | | MATCH / MISMATCH |
  | T-3: Benefits | | MATCH / MISMATCH |
  | T-3: Competitive Threshold | | MATCH / MISMATCH |
  | T-3: Bypasses | | MATCH / MISMATCH |
  | T-3: Preserves | | MATCH / MISMATCH |
  | T-3: Net Position | | MATCH / MISMATCH |
  | T-3: Trajectory | | MATCH / MISMATCH |

Step 4 — Flag deviations:
  For each MISMATCH: declare BREACH-MAJOR; apply Table 1B Phase 7 row correction action.
  For any column that was merged (evaluated as a single T-3 column): declare BREACH-MAJOR;
  halt and reconstruct Phase 7 table with 7 separate anchor-named T-3 columns.

Step 5 — C-27 verdict:
  PASS: all 7 rows MATCH; observed labels are column headers (not row labels or cell content)
  PARTIAL: some rows MATCH; missing labels appeared as prose in a single column
  FAIL: T-3 evaluated in a merged column; anchor labels not present as column headers
  C-27 verdict: [PASS / PARTIAL / FAIL]

Any BREACH-MAJOR from Step 4 must be corrected before Phase 9B begins.

Rules:
- Step 1 must quote Phase 7 header row verbatim — a paraphrase does not satisfy Step 1
- Step 3 mapping table must be complete before Step 5 verdict
- Declared Severity must be assigned to every VIOLATION audit row

Exit Phase 9A:
- [ ] All 5 ledger rows assessed with Status and Declared Severity
- [ ] Reconstruct 5-step protocol completed; Step 3 mapping table fully populated (7 rows)
- [ ] C-27 verdict rendered from Step 5 (not from recall)
- [ ] All VIOLATION rows corrected per Table 1B correction protocol

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9B — CRITERION CHECKLIST
Entry: Phase 9A complete — all 5 ledger rows COMPLETE.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Row | Criterion | Status | Declared Severity if FAIL |
|-----|-----------|--------|--------------------------|
| 1 | Candidate count 20–40 (excluding Do Nothing) | PASS/FAIL | BREACH-MAJOR |
| 2 | Every candidate has all 4 anatomy fields | PASS/FAIL | BREACH-MAJOR |
| 3 | Exactly 5 `**` marks in artifact | PASS/FAIL | BREACH-MAJOR |
| 4 | Do Nothing present with 7 fields including Net Position and Trajectory | PASS/FAIL | BREACH-MAJOR |
| 5 | AMEND has 3 adjustments with dimension, direction, downstream effect | PASS/FAIL | BREACH-MINOR |
| 6 | Phase 3 AMEND Source col, all rows populated | PASS/FAIL | BREACH-MAJOR |
| 7 | Phase 3 Primary Challenge Test col, ≥1 T-3 row | PASS/FAIL | BREACH-MAJOR |
| 8 | Phase 6 T-Evidence with structured notation | PASS/FAIL | BREACH-MAJOR |
| 9 | Phase 7 Ph6 Pre-Score carryforward col | PASS/FAIL | BREACH-MAJOR |
| 10 | `**` candidates span ≥3 categories | PASS/FAIL | BREACH-MAJOR |
| 11 | Phase 4 Challenge Binding col present (7 rows); Net Position maps to T-3 synthesis | PASS/FAIL | BREACH-MAJOR |
| 12 | Table 1C BREACH taxonomy, all 3 tiers | PASS/FAIL | BREACH-FATAL |
| 13 | Phase 9A Declared Severity col populated for all audit rows | PASS/FAIL | BREACH-MAJOR |
| 14 | Phase 7 T-3 via 7 separate anchor-named cols | PASS/FAIL | BREACH-MAJOR |
| 15 | Table 1B BREACH Tier col present; Correction Action + Continue? cols present; all rows populated | PASS/FAIL | BREACH-MAJOR |
| 16 | Phase 9A 5-step Reconstruct protocol completed; C-27 verdict from Step 5 | PASS/FAIL | BREACH-MAJOR |
| 17 | Phase 6 Anchor Citation col present; every candidate cites ≥1 anchor field | PASS/FAIL | BREACH-MINOR if <1/3; BREACH-MAJOR if col absent |

Apply Table 1C correction protocol for every FAIL before finalizing.
```
