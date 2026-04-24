# draft-brainstorm Skill Prompt Variations — Round 12

**Skill:** draft-brainstorm
**Round:** 12
**Date:** 2026-03-15
**Rubric:** v11 (C-01 through C-39)
**Baseline:** R11 treats C-01 through C-37 as non-negotiable. R12 adds C-38 and C-39 as the
two new axes. All 5 variations must satisfy C-28 through C-37 as a baseline.

---

## R12 Axis Selection

R11 confirmed C-28 through C-37 stable across all variations. Identified two new excellence
signals from R11 V-02 and V-03:
- **C-38** (from V-02): BREACH-MINOR/MAJOR/FATAL severity taxonomy declared in Phase 1 Table
  1C; per-tier correction protocols; Phase 9A "Declared Severity" column
- **C-39** (from V-03): Two-pass terminal audit — Reconstruct pass (what each phase produced)
  before Assess pass (criteria verdicts)

R12 treats all eleven (C-28 through C-37) as non-negotiable baseline.
Axes under test: single-axis C-38, single-axis C-39, phrasing register with both,
tight bidirectional binding of C-38+C-39, full stack with all R12 advances.

| Variation | Primary Axis | Novel Structural Feature |
|-----------|--------------|--------------------------|
| V-01 | BREACH severity taxonomy (C-38) | Table 1C in Phase 1 with per-tier correction protocols; Phase 9A Declared Severity column |
| V-02 | Two-pass terminal audit (C-39) | Phase 9A split into Reconstruct pass (row-by-row) then Assess pass |
| V-03 | Phrasing register: conversational with C-38+C-39 | Conversational descriptive framing carries both new criteria without imperative language |
| V-04 | C-38 + C-39 bidirectional binding | Reconstruct pass classifies findings by severity; Assess pass applies tier-specific protocols |
| V-05 | Full R12 stack | C-38 taxonomy drives correction language throughout; C-39 audit mirrors C-11 two-pass structure |

---

## V-01 — Single-axis: BREACH Severity Taxonomy (C-38 Primary)

**Variation axis:** BREACH-MINOR/MAJOR/FATAL severity taxonomy declared as Table 1C in Phase 1,
with per-tier correction protocols applied throughout all contributing phases and a Declared
Severity column in Phase 9A.

**Hypothesis:** Pre-committing severity levels and per-tier correction protocols in Phase 1
produces calibrated, deterministic correction behavior at every violation site — rather than
uniform "fix before continuing" language that treats a missing column the same as generating
candidates before declaring the challenge framework.

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
| T-1 | Differentiation | Candidate offers a meaningfully distinct mechanism from every other `**` candidate in the pool | Removing this candidate eliminates an approach not covered elsewhere |
| T-2 | Topic Fit | Candidate's rationale names a specific dimension of `{{topic}}` — not a generic claim that applies to any topic | Rationale would fail if the topic were swapped out |
| T-3 | Inertia Displacement | Candidate demonstrates explicit advantage on ≥3 of the Phase 4 anchor dimensions: Costs · Benefits · Competitive Threshold · Bypasses · Preserves | Names at least 3 anchor dimension labels from Phase 4 |
| T-4 | Category Coverage | Removing this `**` pick collapses the top-5 set below 3 distinct categories | Candidate's category is not represented by the other 4 picks |

Survival threshold: All four tests must PASS. A candidate clearing 3 of 4 is not a `**` pick.
Challenge framework locked after Phase 1 exit — modification is a BREACH-FATAL.

#### Table 1B — Evidence Ledger Blueprint

| Phase | Contributing Phase Name | Ledger Field Populated | Ledger Violation Condition |
|-------|------------------------|------------------------|---------------------------|
| Phase 3 | Architecture Declaration | AMEND Source column + Primary Challenge Test column on every row | Any row missing either column = ledger violation |
| Phase 4 | Do Nothing Anchor | Challenge Binding column on every anchor field row | Any anchor row missing Challenge Binding = ledger violation |
| Phase 5 | Diverge | Name + Pitch on every candidate row | Any candidate missing Name or Pitch = ledger violation |
| Phase 6 | Cluster + T-Evidence | T-Evidence column with structured notation `T-1:[v] · T-2:[v] · T-3:[dims] · T-4:[v]` on every row | Blank T-Evidence cell = ledger violation |
| Phase 7 | Adversarial Challenge | Ph6 Pre-Score column carrying Phase 6 T-Evidence forward | Missing Ph6 Pre-Score column = ledger violation |

#### Table 1C — BREACH Severity Taxonomy

| Severity | Definition | Correction Protocol | Continue Before Correcting? |
|----------|-----------|---------------------|-----------------------------|
| BREACH-MINOR | A required column is present but has entries missing for fewer than 1/3 of rows; a threshold stated without a specific number; an AMEND direction claimed as distinct but overlapping a peer adjustment; a Net Position that states a conclusion without naming a displacement condition | Correct the specific cells in-place. Mark corrected cells with `[corrected]`. | YES — continue after inline correction |
| BREACH-MAJOR | A required column entirely absent from a table; concentration cap exceeded at a phase exit gate; fewer than 20 or more than 40 candidates in the pool at Phase 6 exit; fewer than 5 PASS verdicts available after Phase 7; Phase 9A Declared Severity column missing | HALT the current phase. Reconstruct the affected table or step from scratch. Do not advance to the next phase until the full table is corrected and re-verified. | NO — halt and reconstruct before continuing |
| BREACH-FATAL | Candidates generated before Phase 1 challenge framework declared; `**` marks assigned before Phase 7 adversarial challenge completes; Do Nothing anchor entirely absent from artifact; challenge framework modified after Phase 1 lock | STOP all generation. Return to the phase where the fatal breach originated. Discard all output from that phase forward. Restart that phase from scratch. | NO — stop and restart from origin phase |

Exit Phase 1:
- [ ] Table 1A: T-1 through T-4 with Pass Threshold, Survival Condition, and survival threshold declared
- [ ] Table 1A: T-3 names all five anchor dimensions by label
- [ ] Table 1A: Challenge framework locked
- [ ] Table 1B: 5 contributing phases with ledger field and violation condition
- [ ] Table 1C: All 3 severity tiers with Definition, Correction Protocol, and Continue decision
- [ ] Any FAIL → identify severity tier, apply correction protocol before Phase 2
Ledger obligation satisfied: Phase 1 framework, blueprint, and BREACH taxonomy declared.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — AMEND ADJUSTMENTS
Entry: Phase 1 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write exactly 3 pool-shaping adjustments before architecture or candidates are generated.
Each row must name a dimension, a direction, and a downstream effect.

| # | Dimension | Direction | Downstream Effect on Pool |
|---|-----------|-----------|--------------------------|
| A1 | | Expands / Narrows / Redirects | |
| A2 | | Expands / Narrows / Redirects | |
| A3 | | Expands / Narrows / Redirects | |

Rules:
- Dimension: name a specific axis — "be more creative" fails C-05
- Direction: all three must differ — if two share a direction: BREACH-MINOR, revise before exit
- Downstream Effect: name specific candidate types that would surface or be displaced in
  `{{topic}}`'s context — "more options" is generic and fails C-12

Exit Phase 2:
- [ ] Exactly 3 rows; all columns filled
- [ ] Directions are all distinct; if duplicate detected: apply BREACH-MINOR protocol
- [ ] Downstream Effects are `{{topic}}`-specific
- [ ] Any FAIL → identify severity, apply Table 1C protocol before Phase 3
Ledger obligation satisfied: AMEND adjustments declared, pool-shaping decisions committed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3 — ARCHITECTURE DECLARATION
Entry: Phase 2 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Declare category structure before generating any candidates.

| Category | Description | Target Count | % of Pool | AMEND Source | Primary Challenge Test |
|----------|-------------|--------------|-----------|--------------|------------------------|

Total: ______

Rules:
- At least 4 distinct categories required
- Concentration cap: if largest category is ≥40% of total, redistribute before continuing
  — exceeding cap at phase exit is BREACH-MAJOR
- Totals must sum to 20–40
- Every row must carry AMEND Source (A1/A2/A3) and Primary Challenge Test (T-1/T-2/T-3/T-4)
  — any row missing either column is a ledger violation; classify severity and correct
- At least 1 category must list T-3 as Primary Challenge Test
- Compute % of Pool inline; concentration cap must be verifiable by column value, not inference

Exit Phase 3:
- [ ] 4+ categories; % of Pool computed; no category ≥40%; totals sum to 20–40
- [ ] AMEND Source column: every row populated — missing entries: BREACH-MINOR if <1/3 rows,
  BREACH-MAJOR if column absent
- [ ] Primary Challenge Test column: every row populated; at least 1 row lists T-3
- [ ] Ledger obligation confirmed
- [ ] Any FAIL → identify severity, apply Table 1C protocol before Phase 4
Ledger obligation satisfied: Architecture table carries AMEND Source and Primary Challenge Test.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — DO NOTHING ANCHOR
Entry: Phase 3 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write the status quo anchor after architecture is declared — Bypasses and Preserves must
reference specific Phase 3 category labels.

| Field | Content | Challenge Binding |
|-------|---------|-------------------|
| Costs | [specific costs of the status quo for `{{topic}}`] | T-3 |
| Benefits | [genuine appeal of continuing with current approach — why inertia is attractive] | T-3 |
| Competitive Threshold | [minimum advantage an alternative must demonstrate to displace this anchor; name a Phase 3 category] | T-3 |
| Bypasses | [which Phase 3 category labels the status quo renders unnecessary; name at least one by label] | T-3 |
| Preserves | [what a transition from the status quo would put at risk for `{{topic}}`] | T-3 |
| Net Position | [integrated judgment: does inertia currently dominate? name the specific condition under which it stops dominating] | T-3 synthesis |

Rules:
- Costs AND Benefits must both be present with `{{topic}}`-specific content — costs-only: BREACH-MINOR
- Bypasses and Preserves must reference Phase 3 category labels by name — generic topology: BREACH-MINOR
- Net Position must name a displacement condition — "inertia is strong" without a condition: BREACH-MINOR
- Challenge Binding column must be present on every row — column absent: BREACH-MAJOR
- Do Nothing entry does NOT count toward the 20–40 candidate total

Exit Phase 4:
- [ ] All 6 fields present with `{{topic}}`-specific content
- [ ] Costs AND Benefits both present
- [ ] Competitive Threshold names a specific Phase 3 category
- [ ] Bypasses and Preserves reference Phase 3 category labels
- [ ] Net Position is integrative and names a displacement condition
- [ ] Challenge Binding column present; every row populated
- [ ] Any FAIL → identify severity, apply Table 1C protocol before Phase 5
Ledger obligation satisfied: Anchor table carries Challenge Binding column on every row.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5 — DIVERGE (Name + Pitch Only)
Entry: Phase 4 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Generate candidate names and one-line pitches only. Do not assign categories, rationales,
or T-Evidence yet — idea generation is separated from categorization (C-11).
Do not mark any candidate `**` — marking is deferred to Phase 7.

Output: numbered list, Name | Pitch pairs only. Target 22–38 entries.

Rules:
- No category assignment, rationale, or T-Evidence in this phase
- If you notice one conceptual area dominating before you finish: pause, shift to a different
  angle before continuing — inline check against Phase 3 concentration commitments
- Any Name or Pitch cell left blank is a ledger violation: BREACH-MINOR, correct before exit

Exit Phase 5:
- [ ] 22–38 Name+Pitch pairs generated; no categories or rationales assigned yet
- [ ] No `**` marks assigned
- [ ] Any blank Name/Pitch: BREACH-MINOR, correct inline
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
- T-Evidence column must be present; blank cells: BREACH-MINOR if <1/3 of rows,
  BREACH-MAJOR if column absent or >1/3 blank
- Check concentration cap on completion: if any category now exceeds 40%, redistribute
  before exiting — exceeding cap at exit: BREACH-MAJOR
- Final candidate count must be 20–40: outside range: BREACH-MAJOR

Exit Phase 6:
- [ ] All candidates have Name, Pitch, Category, Rationale — missing any field: BREACH-MAJOR
- [ ] T-Evidence column present with structured notation on every row
- [ ] No category exceeds 40% of pool
- [ ] Candidate count is 20–40
- [ ] Any FAIL → identify severity, apply Table 1C protocol before Phase 7
Ledger obligation satisfied: Cluster table with T-Evidence structured notation on every row.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — ADVERSARIAL CHALLENGE
Entry: Phase 6 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Identify 8–10 tentative top candidates. Do NOT mark `**` yet.

Challenge table:
| # | Candidate | T-1: Differentiation | T-2: Topic Fit | T-3: Inertia Displacement (name Phase 4 dims) | T-4: Category Coverage | Ph6 Pre-Score | Verdict |
|---|-----------|---------------------|---------------|-----------------------------------------------|------------------------|---------------|---------|

Rules:
- Ph6 Pre-Score: carry forward T-Evidence notation exactly from Phase 6
- T-3 column: name the specific Phase 4 anchor field labels the candidate clears
  (Costs / Benefits / Competitive Threshold / Bypasses / Preserves)
- Verdict: PASS (all 4 tests) or FAIL (name failing test) — 3/4 passing is FAIL
- Only PASS verdicts are eligible for `**` marking
- Select exactly 5 `**` candidates from PASS verdicts, spanning ≥3 categories
- If fewer than 5 PASS verdicts: BREACH-MAJOR — return to Phase 6, strengthen candidates
- If Ph6 Pre-Score column absent: BREACH-MAJOR
- If T-3 column uses generic language without anchor field names: BREACH-MINOR

Exit Phase 7:
- [ ] Ph6 Pre-Score column present and populated from Phase 6 T-Evidence
- [ ] T-3 column names Phase 4 anchor dims for every candidate
- [ ] Exactly 5 PASS verdicts selected as `**` candidates spanning ≥3 categories
- [ ] No `**` marks assigned until this phase completes
- [ ] Any FAIL → identify severity, apply Table 1C protocol
Ledger obligation satisfied: Adversarial challenge complete; `**` candidates identified.

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
- [ ] `**` count in artifact = 5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9A — TERMINAL LEDGER AUDIT
Entry: Phase 8 complete.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Audit the evidence ledger. Phase 9B may not begin until Phase 9A is complete and all rows
are COMPLETE.

| Phase | Ledger Field Expected | Status (COMPLETE / VIOLATION) | Declared Severity | Notes |
|-------|----------------------|-------------------------------|-------------------|-------|
| Phase 3 | AMEND Source column + Primary Challenge Test column on every row | | | |
| Phase 4 | Challenge Binding column on every anchor row | | | |
| Phase 5 | Name + Pitch on every candidate row | | | |
| Phase 6 | T-Evidence with structured notation on every row | | | |
| Phase 7 | Ph6 Pre-Score column present and populated | | | |

Rules:
- Declared Severity: classify any VIOLATION as BREACH-MINOR, BREACH-MAJOR, or BREACH-FATAL
  using Table 1C definitions — no violation may be recorded without a severity classification
- Apply the Table 1C correction protocol for the declared severity before proceeding
- All rows must reach COMPLETE before Phase 9B begins

Exit Phase 9A:
- [ ] All 5 ledger rows assessed with Status and Declared Severity
- [ ] All VIOLATION rows corrected per Table 1C protocol before Phase 9B
- [ ] Declared Severity column populated for every row (COMPLETE rows may carry "N/A")

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
| 11 | Phase 4 anchor Challenge Binding column present, Net Position maps to T-3 synthesis | PASS/FAIL | BREACH-MAJOR |
| 12 | Table 1C BREACH taxonomy present in Phase 1 with all 3 tiers | PASS/FAIL | BREACH-FATAL |
| 13 | Phase 9A Declared Severity column populated for all audit rows | PASS/FAIL | BREACH-MAJOR |

Apply Table 1C correction protocol for every FAIL before writing or finalizing the artifact.
```

---

## V-02 — Single-axis: Two-Pass Terminal Audit (C-39 Primary)

**Variation axis:** Phase 9A is explicitly structured as two sequential passes: (1) Reconstruct
pass — describe what each contributing phase actually produced in the current execution, row by
row, before any compliance verdict; (2) Assess pass — apply ledger criteria and violation
definitions against the reconstructed evidence.

**Hypothesis:** Forcing a Reconstruct pass before any Assess verdict grounds the audit in
freshly recalled evidence rather than memory-based expectation — the model must describe what
it actually produced, not what the prompt instructed it to produce, catching gaps that an
Assess-only pass would rationalize away.

---

```
You are generating a brainstorm artifact for the topic: `{{topic}}`
Output date: `{{date}}`
Artifact path: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 1 — CHALLENGE FRAMEWORK + LEDGER BLUEPRINT
Entry: Start of session.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### Table 1A — Challenge Framework

| ID | Test | Pass Threshold | Survival Condition |
|----|------|----------------|--------------------|
| T-1 | Differentiation | Meaningfully distinct mechanism from every other `**` candidate | Removing this candidate eliminates a distinct angle not covered elsewhere |
| T-2 | Topic Fit | Rationale names a specific dimension of `{{topic}}` — not generic | Rationale fails if topic is swapped out |
| T-3 | Inertia Displacement | Demonstrates advantage on ≥3 of: Costs · Benefits · Competitive Threshold · Bypasses · Preserves | Names ≥3 Phase 4 anchor dimension labels |
| T-4 | Category Coverage | Candidate's category not represented by the other 4 `**` picks | Removing this pick collapses top-5 below 3 categories |

Survival threshold: All 4 tests must PASS. 3/4 is not a `**` pick.
Framework locked at Phase 1 exit — any modification after lock is fatal.

#### Table 1B — Evidence Ledger Blueprint

| Phase | Phase Name | Ledger Field Populated | Violation Condition |
|-------|-----------|------------------------|---------------------|
| Phase 3 | Architecture Declaration | AMEND Source + Primary Challenge Test columns, every row | Any row missing either column |
| Phase 4 | Do Nothing Anchor | Challenge Binding column, every row | Any row missing Challenge Binding |
| Phase 5 | Diverge | Name + Pitch, every candidate row | Any candidate row missing Name or Pitch |
| Phase 6 | Cluster + T-Evidence | T-Evidence column with `T-1:[v] · T-2:[v] · T-3:[dims] · T-4:[v]` on every row | Blank T-Evidence cell |
| Phase 7 | Adversarial Challenge | Ph6 Pre-Score column, every challenge row | Missing Ph6 Pre-Score column |

Exit Phase 1:
- [ ] Table 1A: T-1 through T-4 with Pass Threshold, Survival Condition; T-3 names all 5 anchor dims
- [ ] Table 1A: Challenge framework locked
- [ ] Table 1B: 5 contributing phases declared with ledger field and violation condition
- [ ] Any FAIL → correct in-place before Phase 2
Ledger obligation satisfied: Phase 1 framework and blueprint declared.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — AMEND ADJUSTMENTS
Entry: Phase 1 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write 3 pool-shaping adjustments before architecture or candidates.

| # | Dimension | Direction | Downstream Effect on Pool |
|---|-----------|-----------|--------------------------|
| A1 | | Expands / Narrows / Redirects | |
| A2 | | Expands / Narrows / Redirects | |
| A3 | | Expands / Narrows / Redirects | |

Rules:
- All 3 Directions must differ; if two share a direction, revise one before exit
- Downstream Effect: name specific `{{topic}}`-relevant candidate types — "more options" fails
- Each adjustment must pull in a different direction from the others

Exit Phase 2:
- [ ] Exactly 3 rows; all columns filled; Directions distinct; Effects `{{topic}}`-specific
- [ ] Any FAIL → correct before Phase 3
Ledger obligation satisfied: AMEND adjustments declared.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3 — ARCHITECTURE DECLARATION
Entry: Phase 2 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Category | Description | Target Count | % of Pool | AMEND Source | Primary Challenge Test |
|----------|-------------|--------------|-----------|--------------|------------------------|

Total: ______

Rules:
- ≥4 categories; no single category ≥40% of total; totals sum to 20–40
- % of Pool column must be computed inline — concentration cap must be verifiable by value
- Every row: AMEND Source (A1/A2/A3) and Primary Challenge Test (T-1/T-2/T-3/T-4)
- At least 1 row must list T-3 as Primary Challenge Test
- If largest category is ≥40% before exit: redistribute before continuing

Exit Phase 3:
- [ ] 4+ categories; % of Pool computed; no category ≥40%; totals sum to 20–40
- [ ] AMEND Source and Primary Challenge Test columns present; every row populated; ≥1 T-3
- [ ] Ledger obligation confirmed
- [ ] Any FAIL → correct before Phase 4
Ledger obligation satisfied: Architecture table carries both required columns on every row.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — DO NOTHING ANCHOR
Entry: Phase 3 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write the status quo anchor after architecture is declared.

| Field | Content | Challenge Binding |
|-------|---------|-------------------|
| Costs | [specific costs of status quo for `{{topic}}`] | T-3 |
| Benefits | [genuine appeal of continuing — why inertia is attractive] | T-3 |
| Competitive Threshold | [minimum advantage needed to displace status quo; name a Phase 3 category] | T-3 |
| Bypasses | [Phase 3 category labels the status quo renders unnecessary; name at least one] | T-3 |
| Preserves | [what a transition would put at risk for `{{topic}}`] | T-3 |
| Net Position | [integrated judgment: does inertia dominate? name the specific condition under which it stops] | T-3 synthesis |

Rules:
- Bypasses and Preserves must name Phase 3 category labels — generic topology is a partial
- Net Position must name a specific displacement condition — "inertia is strong" fails
- Challenge Binding column must be present on every row — absent column is a ledger violation
- Do Nothing does NOT count toward the 20–40 candidate total

Exit Phase 4:
- [ ] All 6 fields with `{{topic}}`-specific content; Costs AND Benefits both present
- [ ] Competitive Threshold names a Phase 3 category; Bypasses and Preserves reference Phase 3 labels
- [ ] Net Position names a displacement condition
- [ ] Challenge Binding column present; every row populated
- [ ] Ledger obligation confirmed
Ledger obligation satisfied: Anchor table carries Challenge Binding on every row.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5 — DIVERGE (Name + Pitch Only)
Entry: Phase 4 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Generate Name + Pitch only. No categories, rationales, or T-Evidence yet. No `**` marks.
Target: 22–38 entries.

If one conceptual area is dominating before you finish diverging, shift to another angle
before continuing — guard against concentration before it becomes a Phase 6 problem.

Exit Phase 5:
- [ ] 22–38 Name+Pitch pairs; no categories, rationales, or `**` marks
Ledger obligation satisfied: Diverge output available for cluster.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6 — CLUSTER + T-EVIDENCE
Entry: Phase 5 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| # | Name | Pitch | Category | Rationale | T-Evidence |
|---|------|-------|----------|-----------|------------|

T-Evidence format: `T-1:PASS/PARTIAL/FAIL · T-2:PASS/PARTIAL/FAIL · T-3:[dims cleared] · T-4:PASS/PARTIAL/FAIL`

Rules:
- Rationale must reference a specific `{{topic}}` dimension — not generic
- T-Evidence column must be present; structured notation on every row; no blank cells
- Check concentration cap on completion: if any category ≥40%, redistribute before exit
- Final count must be 20–40

Exit Phase 6:
- [ ] All 4 anatomy fields on every candidate; T-Evidence column with structured notation on every row
- [ ] No category ≥40%; count 20–40
- [ ] Ledger obligation confirmed
Ledger obligation satisfied: Cluster table with T-Evidence notation on every row.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — ADVERSARIAL CHALLENGE
Entry: Phase 6 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Identify 8–10 tentative top candidates. Do NOT mark `**` yet.

| # | Candidate | T-1: Differentiation | T-2: Topic Fit | T-3: Inertia Displacement (name Phase 4 dims) | T-4: Category Coverage | Ph6 Pre-Score | Verdict |
|---|-----------|---------------------|---------------|-----------------------------------------------|------------------------|---------------|---------|

Rules:
- Ph6 Pre-Score: carry forward T-Evidence notation from Phase 6 exactly
- T-3 column: name Phase 4 anchor field labels cleared (Costs / Benefits / Competitive Threshold / Bypasses / Preserves)
- Verdict: PASS (all 4) or FAIL (name failing test) — 3/4 = FAIL
- Select exactly 5 `**` from PASS verdicts spanning ≥3 categories; assign `**` only after this table

Exit Phase 7:
- [ ] Ph6 Pre-Score column present; T-3 column names anchor dims; exactly 5 PASS → `**` spanning ≥3 categories
- [ ] Ledger obligation confirmed
Ledger obligation satisfied: Challenge complete; `**` candidates identified.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 8 — ARTIFACT ASSEMBLY
Entry: Phase 7 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write artifact to: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md

Structure:
1. Header: topic, date, candidate count, `**` count
2. AMEND section (A1, A2, A3)
3. Candidate pool grouped by category, exactly 5 `**` marks
4. Do Nothing section (6-field anchor table, outside numbered pool)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9A — TERMINAL LEDGER AUDIT (TWO-PASS)
Entry: Phase 8 complete.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Phase 9A has two mandatory passes. They must be executed sequentially.
Phase 9B may not begin until both passes are complete and all rows reach COMPLETE.

### Pass 1 — RECONSTRUCT

For each contributing phase, describe what it actually produced in this execution.
Do not render any compliance verdict in Pass 1. Describe only.

| Phase | What This Phase Actually Produced |
|-------|----------------------------------|
| Phase 3 | [Describe: how many categories, whether AMEND Source column was present, whether Primary Challenge Test column was present, what the category names were, what the % of Pool values were] |
| Phase 4 | [Describe: which 6 anchor fields were written, whether Challenge Binding column was present, what Net Position actually stated] |
| Phase 5 | [Describe: how many Name+Pitch pairs were generated, whether any categories or rationales appeared] |
| Phase 6 | [Describe: how many candidates in the cluster table, whether T-Evidence column was present, what notation format was used, whether any cells were blank] |
| Phase 7 | [Describe: how many candidates were challenged, whether Ph6 Pre-Score column was present, how many PASS verdicts, which 5 candidates received `**`, what categories they span] |

Rules for Reconstruct pass:
- One row per contributing phase — no phase may be skipped
- Describe what was actually produced, not what the prompt instructed
- Do not render COMPLETE / VIOLATION verdicts in this pass
- If a contributing phase produced no output for a required field, state that explicitly:
  "Phase 6 T-Evidence column: not present" or "Phase 4 Challenge Binding: absent"
- A prose summary of "Phase 6 went well" without describing specific columns does not
  constitute a Reconstruct row — name the specific field and whether it was present

### Pass 2 — ASSESS

Apply ledger criteria against the Reconstruct evidence to reach verdicts.

| Phase | Ledger Field Expected | Reconstruct Evidence (from Pass 1) | Status (COMPLETE / VIOLATION) | Notes |
|-------|----------------------|------------------------------------|-------------------------------|-------|
| Phase 3 | AMEND Source + Primary Challenge Test columns, every row | [reference Pass 1 finding] | | |
| Phase 4 | Challenge Binding column, every row | [reference Pass 1 finding] | | |
| Phase 5 | Name + Pitch, every candidate row | [reference Pass 1 finding] | | |
| Phase 6 | T-Evidence with structured notation, every row | [reference Pass 1 finding] | | |
| Phase 7 | Ph6 Pre-Score column present and populated | [reference Pass 1 finding] | | |

Rules for Assess pass:
- Reconstruct Evidence column must carry a specific reference to Pass 1 findings — "see above"
  without identifying the finding does not pass
- Status verdicts must be grounded in Pass 1 evidence, not in recalled expectation
- Any VIOLATION detected: correct before Phase 9B begins

Exit Phase 9A:
- [ ] Pass 1 Reconstruct complete: all 5 phases described with specific field-level observations
- [ ] Pass 2 Assess complete: all 5 rows carry Status and Reconstruct Evidence reference
- [ ] All VIOLATION rows corrected before Phase 9B

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9B — CRITERION CHECKLIST
Entry: Phase 9A complete — both passes done, all 5 ledger rows COMPLETE.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Row | Criterion | Status |
|-----|-----------|--------|
| 1 | Candidate count 20–40 (excluding Do Nothing) | PASS/FAIL |
| 2 | Every candidate has all 4 anatomy fields | PASS/FAIL |
| 3 | Exactly 5 `**` marks | PASS/FAIL |
| 4 | Do Nothing present with 6 fields including Net Position | PASS/FAIL |
| 5 | AMEND has 3 adjustments each with dimension, direction, downstream effect | PASS/FAIL |
| 6 | Phase 3 AMEND Source column: all rows populated | PASS/FAIL |
| 7 | Phase 3 Primary Challenge Test column: all rows populated; ≥1 T-3 | PASS/FAIL |
| 8 | Phase 6 T-Evidence: structured notation on every row | PASS/FAIL |
| 9 | Phase 7 Ph6 Pre-Score column present | PASS/FAIL |
| 10 | `**` candidates span ≥3 categories | PASS/FAIL |
| 11 | Phase 4 Challenge Binding column present; Net Position mapped to T-3 synthesis | PASS/FAIL |
| 12 | Phase 9A Reconstruct pass: all 5 phases described at field level | PASS/FAIL |
| 13 | Phase 9A Assess pass: all 5 rows carry Reconstruct Evidence reference | PASS/FAIL |

Any FAIL → correct before writing final artifact.
```

---

## V-03 — Single-axis: Phrasing Register (Conversational Descriptive with C-38 + C-39)

**Variation axis:** All structural requirements are expressed in conversational, descriptive
language rather than imperative commands. Inline conditionals are framed as guidance ("you'll
want to...") rather than directives ("you must..."). C-38 and C-39 are present but expressed
in the same register — severity taxonomy as a named reference table, two-pass audit as a
natural reading sequence.

**Hypothesis:** Conversational framing reduces prompt rigidity — the model receives structural
requirements as design intent rather than compliance checklist, potentially producing more
natural generative output while maintaining all structural properties. Risk: conversational
framing may reduce boundary enforcement.

---

```
You're running draft-brainstorm for `{{topic}}` (date: `{{date}}`).

The goal is a pool of 20–40 candidate ideas — more than you need — so the best ones can be
ranked and filtered. The artifact will live at:
  simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md

Here's the generation sequence. Work through it phase by phase.

---

### Step 1: Lock the Evaluation Framework (and Violation Reference)

Before any ideas exist, decide how you'll evaluate them. This prevents the evaluation criteria
from quietly drifting toward whatever you happened to generate.

Start with two tables.

**Challenge Framework** — four tests every `**` candidate must pass:

| Test | Name | What It Checks | How to Tell if It Passes |
|------|------|----------------|--------------------------|
| T-1 | Distinctiveness | Does this candidate cover ground no other top-5 pick covers? | Removing it would leave a gap |
| T-2 | Topic Fit | Does the rationale make a specific claim about `{{topic}}`? | The rationale would fail if you swapped in a different topic |
| T-3 | Inertia Displacement | Does it show real advantage over the status quo on at least 3 of: Costs · Benefits · Competitive Threshold · Bypasses · Preserves? | It names at least 3 anchor dimensions from Step 4 |
| T-4 | Category Coverage | Does it add a category that isn't covered by the other 4 top picks? | Top-5 would drop below 3 categories without it |

A candidate has to clear all four. Three out of four doesn't make the cut.
Once this table is written, treat it as fixed — adding tests later to rationalize a preferred
candidate is a violation of the process.

**Evidence Ledger Blueprint** — where each phase contributes to the record:

| Step | What It Contributes | What a Gap Looks Like |
|------|--------------------|-----------------------|
| Step 3 Architecture | AMEND Source column + Primary Challenge Test column on every category row | A category row missing either column |
| Step 4 Anchor | Challenge Binding column on every anchor field | Any anchor field row missing Challenge Binding |
| Step 5 Diverge | Name + Pitch on every candidate | Any candidate missing a name or pitch |
| Step 6 Cluster | T-Evidence column with structured notation on every row | A blank T-Evidence cell |
| Step 7 Challenge | Ph6 Pre-Score column in challenge table | Challenge table without Ph6 Pre-Score |

**Violation Severity Reference** — three levels of gap, three levels of response:

| Level | What It Looks Like | What to Do | Can You Continue First? |
|-------|-------------------|-----------|-----------------------|
| MINOR | A column is present but a few cells are empty (under a third); a threshold stated without a number; two AMEND directions that are more similar than distinct | Fix the specific cells inline, mark `[corrected]` | Yes — fix it and move on |
| MAJOR | A required column is entirely missing from a table; candidate count outside 20–40; fewer than 5 candidates surviving challenge; concentration cap exceeded at step exit | Stop the current step, rebuild the affected table, re-verify before continuing | No — rebuild first |
| FATAL | Ideas generated before the challenge framework is locked; `**` marks assigned before Step 7 completes; Do Nothing anchor entirely absent | Stop everything, go back to the step where this happened, discard output from that step forward | No — go back and restart from that step |

This severity reference is what the audit in Step 9 will use. Keep it in mind whenever you
hit a gap during generation.

Before moving to Step 2:
- Both tables are complete with all rows and columns filled
- Challenge framework is locked
- Violation severity reference is present with all 3 levels

---

### Step 2: Write the Three AMEND Adjustments

Write three ways the pool could be shaped differently before you generate any candidates.
These adjustments will influence the category structure in Step 3 — they're not an afterthought.

For each:
- Name the dimension being shifted (not "be more creative")
- Pick a direction: Expands, Narrows, or Redirects — and all three should differ
- Describe what kind of candidates would surface as a result, specifically for `{{topic}}`

| # | Dimension | Direction | Pool Effect |
|---|-----------|-----------|-------------|
| A1 | | | |
| A2 | | | |
| A3 | | | |

If two of the three adjustments point the same direction, that's a MINOR violation — revise
one before moving to Step 3.

---

### Step 3: Commit the Category Architecture

Decide the shape of your pool before generating anything. This is where the concentration
cap and AMEND sourcing get locked in.

| Category | Description | Target Count | % of Pool | AMEND Source | Primary Challenge Test |
|----------|-------------|--------------|-----------|--------------|------------------------|

A few things to watch:
- You'll want at least 4 distinct categories
- Compute % of Pool inline for each row — if your biggest category is already at 40% or more
  of the total, redistribute before continuing (that's a MAJOR violation at step exit if
  you don't)
- Every row should carry the AMEND Source (A1, A2, or A3) that motivated it, and the Primary
  Challenge Test (T-1 through T-4) it most directly supports
- At least one category should support T-3 — if none do, you won't have good displacement
  candidates in the pool

Before moving to Step 4:
- 4+ categories; % of Pool computed; nothing at or above 40%; totals sum to 20–40
- Every row carries AMEND Source and Primary Challenge Test
- At least one row lists T-3

*Ledger contribution: architecture table populates AMEND Source and Primary Challenge Test
columns for every row.*

---

### Step 4: Write the Do Nothing Anchor

Now that the category landscape exists, write the status quo as the primary comparator.
Writing it after Step 3 matters — Bypasses and Preserves should name specific Step 3 category
labels, not generic descriptions.

| Field | Content | Challenge Binding |
|-------|---------|-------------------|
| Costs | | T-3 |
| Benefits | | T-3 |
| Competitive Threshold | | T-3 |
| Bypasses | | T-3 |
| Preserves | | T-3 |
| Net Position | | T-3 synthesis |

A few things to make this useful:
- Costs and Benefits both need to be present — an anchor that only lists costs isn't honest
  about why inertia is appealing
- Competitive Threshold should name a specific Step 3 category as the benchmark
- Bypasses and Preserves should use actual Step 3 category labels
- Net Position should be an integrated judgment — "inertia is strong" is too vague; name
  the specific condition under which it would stop dominating
- The Challenge Binding column closes the traceability loop back to T-3; it needs to be on
  every row — missing it is a MAJOR violation

The Do Nothing entry doesn't count toward the 20–40 candidate total.

*Ledger contribution: anchor table carries Challenge Binding column on every row.*

---

### Step 5: Diverge — Names and Pitches Only

Generate candidate names and one-line pitches. Don't assign categories, rationales, or
T-Evidence yet — the idea is to separate generation from organization (this is the two-pass
structure that helps avoid anchoring early ideas to whatever category you wrote first).

No `**` marks yet — those come after the challenge in Step 7.

Target: 22–38 Name+Pitch entries.

If you notice one conceptual territory filling up fast, shift to another area before you
finish — it's easier to redistribute here than in Step 6.

*Ledger contribution: Name + Pitch on every candidate row.*

---

### Step 6: Cluster and Annotate

Now assign Category and Rationale to every candidate, and add a T-Evidence annotation.

| # | Name | Pitch | Category | Rationale | T-Evidence |
|---|------|-------|----------|-----------|------------|

For T-Evidence, use this format: `T-1:PASS/PARTIAL/FAIL · T-2:PASS/PARTIAL/FAIL · T-3:[dims cleared, e.g. Costs+Benefits] · T-4:PASS/PARTIAL/FAIL`

A few notes:
- Rationale should say something specific about `{{topic}}` — if it would read equally well
  for any topic, rewrite it
- Every row needs a T-Evidence entry; blank cells are ledger violations
- After you finish, check the concentration: if any category is now at 40% or more, move a
  few candidates before declaring Step 6 complete
- Final count needs to land between 20 and 40

*Ledger contribution: cluster table with T-Evidence structured notation on every row.*

---

### Step 7: Run the Adversarial Challenge

Pick 8–10 tentative top candidates. Don't mark `**` yet — that comes only after they survive
this table.

| # | Candidate | T-1: Distinctiveness | T-2: Topic Fit | T-3: Inertia Displacement (name Step 4 dims) | T-4: Category Coverage | Ph6 Pre-Score | Verdict |
|---|-----------|---------------------|---------------|----------------------------------------------|------------------------|---------------|---------|

Notes:
- Ph6 Pre-Score: carry the T-Evidence notation over from Step 6 exactly as written — this
  lets the challenge phase adjudicate existing evidence rather than re-generating judgment
- T-3 column should name the specific anchor field labels cleared (Costs, Benefits,
  Competitive Threshold, Bypasses, Preserves) — "displaces status quo" without naming dims
  is too vague
- Verdict is PASS (all 4) or FAIL (name which test failed) — 3/4 is a FAIL
- Select exactly 5 `**` from the PASS group, spanning at least 3 categories
- If you have fewer than 5 PASS verdicts, that's a MAJOR violation — strengthen some
  candidates in Step 6 before continuing

*Ledger contribution: adversarial challenge table with Ph6 Pre-Score carryforward.*

---

### Step 8: Assemble the Artifact

Write the final artifact at: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md

Structure:
1. Header with topic, date, candidate count, and `**` count
2. AMEND section — A1, A2, A3 each with dimension, direction, and pool effect
3. Candidate pool grouped by category, `**` marks on exactly 5
4. Do Nothing section — the 6-field anchor table, outside and after the numbered pool

---

### Step 9A: Terminal Audit — Two Passes

This is the evidence audit. It runs before the criterion checklist. Complete both passes
before moving to Step 9B.

**Pass 1 — Reconstruct**

For each contributing step, describe what it actually produced in this execution.
You're not evaluating yet — you're describing. Be specific at the field level.

| Step | What This Step Actually Produced |
|------|----------------------------------|
| Step 3 | [Describe: how many categories, whether AMEND Source column was present and complete, whether Primary Challenge Test column was present and complete, what % of Pool values were, whether any row was missing either column] |
| Step 4 | [Describe: which 6 anchor fields were written, whether Challenge Binding column was present, what the Net Position actually said, whether Bypasses and Preserves referenced Step 3 category names] |
| Step 5 | [Describe: how many Name+Pitch pairs were generated, whether any categorization or rationale appeared prematurely] |
| Step 6 | [Describe: total candidate count, whether T-Evidence column was present, what notation format was used, whether any cells were blank, whether concentration cap was met] |
| Step 7 | [Describe: how many candidates were challenged, whether Ph6 Pre-Score column was present, how many PASS verdicts, which 5 candidates received `**`, how many categories they span] |

The descriptions here are what Pass 2 will evaluate against. If a field was missing, say so
explicitly — "T-Evidence column: not present" rather than "Step 6 went as expected."

**Pass 2 — Assess**

Now evaluate the Reconstruct evidence against the ledger blueprint.

| Step | Ledger Field Expected | Evidence from Pass 1 | Status |
|------|----------------------|---------------------|--------|
| Step 3 | AMEND Source + Primary Challenge Test columns, every row | [reference Pass 1] | COMPLETE / VIOLATION |
| Step 4 | Challenge Binding column, every row | [reference Pass 1] | COMPLETE / VIOLATION |
| Step 5 | Name + Pitch, every row | [reference Pass 1] | COMPLETE / VIOLATION |
| Step 6 | T-Evidence with structured notation, every row | [reference Pass 1] | COMPLETE / VIOLATION |
| Step 7 | Ph6 Pre-Score column present | [reference Pass 1] | COMPLETE / VIOLATION |

For any VIOLATION: classify it (MINOR / MAJOR / FATAL using the Step 1 reference), apply the
correction protocol, and confirm it's resolved before starting Step 9B.

Before Step 9B:
- Pass 1 complete: all 5 steps described with specific field-level observations
- Pass 2 complete: all 5 rows carry Evidence reference and Status verdict
- All VIOLATIONs corrected

---

### Step 9B: Criterion Checklist

Only begin this step after Step 9A is complete and all ledger rows are COMPLETE.

| # | Check | Status |
|---|-------|--------|
| 1 | Candidate count is 20–40 (excluding Do Nothing) | PASS/FAIL |
| 2 | Every candidate has Name, Pitch, Category, and Rationale | PASS/FAIL |
| 3 | Exactly 5 `**` marks in the artifact | PASS/FAIL |
| 4 | Do Nothing has all 6 fields including Net Position | PASS/FAIL |
| 5 | AMEND has 3 adjustments each with dimension, direction, and pool effect | PASS/FAIL |
| 6 | Step 3 architecture AMEND Source column: all rows populated | PASS/FAIL |
| 7 | Step 3 architecture Primary Challenge Test column: all rows, ≥1 T-3 | PASS/FAIL |
| 8 | Step 6 cluster T-Evidence: structured notation on every row | PASS/FAIL |
| 9 | Step 7 Ph6 Pre-Score column present | PASS/FAIL |
| 10 | `**` candidates span ≥3 categories | PASS/FAIL |
| 11 | Step 4 Challenge Binding column present; Net Position maps to T-3 synthesis | PASS/FAIL |
| 12 | Step 1 violation severity reference present with all 3 tiers | PASS/FAIL |
| 13 | Step 9A Pass 1 reconstructed all 5 steps at field level | PASS/FAIL |
| 14 | Step 9A Pass 2 Evidence column references Pass 1 findings for every row | PASS/FAIL |

Any FAIL: correct before finalizing the artifact.
```

---

## V-04 — Combined: C-38 + C-39 Bidirectional Binding

**Variation axis:** BREACH severity taxonomy (C-38) and two-pass terminal audit (C-39) are
bound bidirectionally: the Reconstruct pass in Phase 9A explicitly classifies each gap by
severity tier as it discovers it, and the Assess pass applies the tier-specific correction
protocol declared in Phase 1 Table 1C. The two new criteria reinforce each other — severity
classification is not deferred to Assess, it is part of Reconstruct.

**Hypothesis:** When severity classification happens during the Reconstruct pass (not after),
the model must evaluate gap severity in the same pass where it describes what happened —
preventing the Assess pass from softening severity classifications after the fact. This
produces a stronger correction chain than either criterion alone.

---

```
You are generating a brainstorm artifact for the topic: `{{topic}}`
Output date: `{{date}}`
Artifact path: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 1 — CHALLENGE FRAMEWORK + LEDGER BLUEPRINT + BREACH TAXONOMY
Entry: Start of session.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Three Phase 1 artifacts. All must be complete before Phase 2.

#### Table 1A — Challenge Framework

| ID | Test | Pass Threshold | Survival Condition |
|----|------|----------------|--------------------|
| T-1 | Differentiation | Candidate's mechanism is distinct from every other `**` candidate | Removing it eliminates an approach absent elsewhere in the top-5 |
| T-2 | Topic Fit | Rationale makes a specific claim about `{{topic}}` | Rationale fails if topic is swapped |
| T-3 | Inertia Displacement | Demonstrates advantage on ≥3 of: Costs · Benefits · Competitive Threshold · Bypasses · Preserves | Names ≥3 Phase 4 anchor dimension labels |
| T-4 | Category Coverage | Candidate's category is not represented by the other 4 `**` picks | Top-5 would drop below 3 categories without it |

Survival threshold: All 4 must PASS. Framework locked at Phase 1 exit.

#### Table 1B — Evidence Ledger Blueprint

| Phase | Phase Name | Ledger Field | Violation Definition |
|-------|-----------|--------------|---------------------|
| Phase 3 | Architecture | AMEND Source + Primary Challenge Test columns, every row | Any architecture row missing either column |
| Phase 4 | Do Nothing Anchor | Challenge Binding column, every row | Any anchor row missing Challenge Binding |
| Phase 5 | Diverge | Name + Pitch, every candidate row | Any candidate row missing Name or Pitch |
| Phase 6 | Cluster + T-Evidence | T-Evidence with `T-1:[v] · T-2:[v] · T-3:[dims] · T-4:[v]` on every row | Blank T-Evidence cell |
| Phase 7 | Adversarial Challenge | Ph6 Pre-Score column, every challenge row | Missing Ph6 Pre-Score column |

#### Table 1C — BREACH Severity Taxonomy

| Tier | Signature | Correction Protocol | Resume? |
|------|-----------|---------------------|---------|
| BREACH-MINOR | Column present, <1/3 cells missing; threshold lacks numeric specificity; AMEND directions overlap partially; Net Position makes a directional claim without naming a displacement condition | Correct the specific cells inline; mark `[corrected]`; continue | YES |
| BREACH-MAJOR | Required column entirely absent; concentration cap exceeded at phase exit; candidate count outside 20–40; <5 PASS verdicts at Phase 7 exit; Phase 9A Reconstruct omits one or more contributing phases | Halt current phase; reconstruct affected table/step from scratch; re-verify; advance only after corrected | NO |
| BREACH-FATAL | Candidates generated before Phase 1 declared; `**` marks assigned before Phase 7 completes; Do Nothing anchor absent from artifact; challenge framework modified after lock | Stop; return to origin phase; discard all output from origin phase forward; restart that phase | NO |

Exit Phase 1:
- [ ] Table 1A: T-1 through T-4; T-3 names all 5 anchor dimension labels; survival threshold declared
- [ ] Table 1A: Challenge framework locked
- [ ] Table 1B: 5 phases declared with ledger field and violation definition
- [ ] Table 1C: 3 tiers declared with Signature, Correction Protocol, and Resume decision
- [ ] Any gap detected → classify tier (Table 1C) → apply correction protocol
Ledger obligation satisfied: Phase 1 framework, blueprint, and breach taxonomy declared.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — AMEND ADJUSTMENTS
Entry: Phase 1 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| # | Dimension | Direction | Downstream Pool Effect |
|---|-----------|-----------|------------------------|
| A1 | | Expands / Narrows / Redirects | |
| A2 | | Expands / Narrows / Redirects | |
| A3 | | Expands / Narrows / Redirects | |

Rules:
- Directions must all differ — duplicate direction: BREACH-MINOR, correct inline before exit
- Downstream effect must name `{{topic}}`-specific candidate types — generic language: BREACH-MINOR
- Dimension must be specific — "be more creative" is not a dimension

Exit Phase 2:
- [ ] 3 rows; all columns filled; Directions distinct; Effects `{{topic}}`-specific
- [ ] Any gap → classify via Table 1C → apply correction protocol
Ledger obligation satisfied: AMEND adjustments declared.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3 — ARCHITECTURE DECLARATION
Entry: Phase 2 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Category | Description | Target Count | % of Pool | AMEND Source | Primary Challenge Test |
|----------|-------------|--------------|-----------|--------------|------------------------|

Total: ______

Rules:
- ≥4 categories; no single category ≥40%; totals sum to 20–40
- % of Pool computed inline — if largest category is ≥40% before exit: BREACH-MAJOR
- Every row carries AMEND Source and Primary Challenge Test; missing column: BREACH-MAJOR;
  <1/3 rows missing an entry: BREACH-MINOR
- ≥1 category lists T-3 as Primary Challenge Test

Exit Phase 3:
- [ ] 4+ categories; % computed; no category ≥40%; sum 20–40
- [ ] Both columns present and fully populated; ≥1 T-3 row
- [ ] Any gap → Table 1C tier → correction protocol
Ledger obligation satisfied: Architecture carries AMEND Source and Primary Challenge Test.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — DO NOTHING ANCHOR
Entry: Phase 3 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Field | Content | Challenge Binding |
|-------|---------|-------------------|
| Costs | | T-3 |
| Benefits | | T-3 |
| Competitive Threshold | | T-3 |
| Bypasses | [name Phase 3 category labels] | T-3 |
| Preserves | [name Phase 3 category labels] | T-3 |
| Net Position | [integrated judgment + displacement condition] | T-3 synthesis |

Rules:
- Costs AND Benefits required — costs-only: BREACH-MINOR
- Bypasses/Preserves must reference Phase 3 labels — generic topology: BREACH-MINOR
- Net Position must name displacement condition — directional claim without condition: BREACH-MINOR
- Challenge Binding column required on every row — column absent: BREACH-MAJOR

Exit Phase 4:
- [ ] All 6 fields; Costs+Benefits both present; Bypasses/Preserves reference Phase 3 labels
- [ ] Net Position names displacement condition
- [ ] Challenge Binding column present, every row
- [ ] Any gap → Table 1C tier → correction protocol
Ledger obligation satisfied: Anchor carries Challenge Binding on every row.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5 — DIVERGE (Name + Pitch Only)
Entry: Phase 4 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Name + Pitch only. No categories, rationales, T-Evidence, or `**` marks. Target: 22–38 entries.
If one territory dominates before you finish, shift angle — inline concentration guard.

Exit Phase 5:
- [ ] 22–38 pairs; no categories, rationales, or `**`
Ledger obligation satisfied: Diverge pairs available for cluster.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6 — CLUSTER + T-EVIDENCE
Entry: Phase 5 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| # | Name | Pitch | Category | Rationale | T-Evidence |
|---|------|-------|----------|-----------|------------|

T-Evidence format: `T-1:PASS/PARTIAL/FAIL · T-2:PASS/PARTIAL/FAIL · T-3:[dims cleared] · T-4:PASS/PARTIAL/FAIL`

Rules:
- Rationale: `{{topic}}`-specific — generic: BREACH-MINOR; T-Evidence column absent: BREACH-MAJOR;
  <1/3 cells blank: BREACH-MINOR; ≥1/3 blank: BREACH-MAJOR
- Concentration cap at exit: ≥40% in one category: BREACH-MAJOR
- Count outside 20–40: BREACH-MAJOR

Exit Phase 6:
- [ ] All 4 anatomy fields; T-Evidence column with structured notation; ≥40% concentration absent; count 20–40
- [ ] Any gap → Table 1C tier → correction protocol
Ledger obligation satisfied: Cluster table with T-Evidence on every row.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — ADVERSARIAL CHALLENGE
Entry: Phase 6 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Identify 8–10 tentative top candidates. No `**` marks until this table is complete.

| # | Candidate | T-1: Differentiation | T-2: Topic Fit | T-3: Inertia Displacement (name Phase 4 dims) | T-4: Category Coverage | Ph6 Pre-Score | Verdict |
|---|-----------|---------------------|---------------|-----------------------------------------------|------------------------|---------------|---------|

Rules:
- Ph6 Pre-Score: carry T-Evidence from Phase 6 verbatim
- T-3 column: name specific Phase 4 anchor dims — generic language: BREACH-MINOR
- Verdict: PASS (all 4) or FAIL (name which test) — 3/4 = FAIL
- Exactly 5 PASS → `**`; spans ≥3 categories; <5 PASS available: BREACH-MAJOR
- Ph6 Pre-Score column absent: BREACH-MAJOR

Exit Phase 7:
- [ ] Ph6 Pre-Score column present; T-3 names anchor dims; exactly 5 `**` spanning ≥3 categories
- [ ] Any gap → Table 1C tier → correction protocol
Ledger obligation satisfied: Challenge complete; `**` candidates identified.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 8 — ARTIFACT ASSEMBLY
Entry: Phase 7 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Artifact: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md
Structure: Header → AMEND → Pool grouped by category (5 `**`) → Do Nothing section

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9A — TERMINAL LEDGER AUDIT (TWO-PASS WITH SEVERITY CLASSIFICATION)
Entry: Phase 8 complete.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Phase 9A runs two sequential passes. Phase 9B may not begin until both passes complete and
all rows reach COMPLETE.

### Pass 1 — RECONSTRUCT WITH SEVERITY PRE-CLASSIFICATION

For each contributing phase: (1) describe what it actually produced, field by field;
(2) identify any gap; (3) classify the gap severity using Table 1C.
Do not render COMPLETE / VIOLATION verdicts yet — only describe and pre-classify.

| Phase | What It Actually Produced | Gap Observed (if any) | Preliminary Severity |
|-------|--------------------------|----------------------|---------------------|
| Phase 3 | [Describe: category count, whether AMEND Source column was present and fully populated, whether Primary Challenge Test column was present and fully populated, % of Pool values, any missing cells] | [Describe gap, if any] | [BREACH-MINOR / BREACH-MAJOR / BREACH-FATAL / none] |
| Phase 4 | [Describe: which anchor fields were written, whether Challenge Binding column was present on every row, what Net Position stated, whether Bypasses/Preserves referenced Phase 3 labels] | | |
| Phase 5 | [Describe: candidate count, whether any categories or rationales appeared prematurely] | | |
| Phase 6 | [Describe: total candidate count, T-Evidence column presence, notation format, blank cells, concentration cap status] | | |
| Phase 7 | [Describe: how many candidates challenged, Ph6 Pre-Score column presence, PASS count, which 5 received `**`, category spread] | | |

Rules:
- Every phase must have a description row — skipping a phase is BREACH-MAJOR
- Gap and Preliminary Severity must be completed for every row, even if the answer is "none"
- Do not use "as expected" or "went well" — describe specific fields and their states

### Pass 2 — ASSESS AGAINST LEDGER BLUEPRINT

Apply ledger criteria using the Pass 1 descriptions as evidence. The Preliminary Severity
from Pass 1 carries forward — the Assess pass may not downgrade a severity classification
without an explicit justification.

| Phase | Ledger Field Expected | Pass 1 Evidence | Status | Final Severity | Correction Applied |
|-------|----------------------|-----------------|--------|----------------|-------------------|
| Phase 3 | AMEND Source + Primary Challenge Test columns, every row | [reference Pass 1 finding] | COMPLETE / VIOLATION | [from Pass 1, may upgrade but not silently downgrade] | |
| Phase 4 | Challenge Binding column, every row | [reference Pass 1 finding] | | | |
| Phase 5 | Name + Pitch, every candidate row | [reference Pass 1 finding] | | | |
| Phase 6 | T-Evidence with structured notation, every row | [reference Pass 1 finding] | | | |
| Phase 7 | Ph6 Pre-Score column present | [reference Pass 1 finding] | | | |

Rules:
- Pass 1 Evidence must be a specific reference — "see above" without identifying the field fails
- Final Severity: carry from Pass 1 preliminary; any upgrade requires naming new evidence;
  any downgrade requires explicit justification — silent downgrade is a BREACH-MINOR
- Apply Table 1C correction protocol for every VIOLATION before Phase 9B

Exit Phase 9A:
- [ ] Pass 1: all 5 phases described with Gap and Preliminary Severity
- [ ] Pass 2: all 5 rows carry Pass 1 Evidence reference, Status, Final Severity, Correction Applied
- [ ] All VIOLATION rows corrected before Phase 9B

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9B — CRITERION CHECKLIST
Entry: Phase 9A complete — both passes done, all ledger rows COMPLETE.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Row | Criterion | Status | Severity if FAIL |
|-----|-----------|--------|-----------------|
| 1 | Candidate count 20–40 (excluding Do Nothing) | PASS/FAIL | BREACH-MAJOR |
| 2 | Every candidate has all 4 anatomy fields | PASS/FAIL | BREACH-MAJOR |
| 3 | Exactly 5 `**` marks | PASS/FAIL | BREACH-MAJOR |
| 4 | Do Nothing: 6 fields including Net Position with displacement condition | PASS/FAIL | BREACH-MAJOR |
| 5 | AMEND: 3 adjustments each with dimension, direction, downstream effect | PASS/FAIL | BREACH-MINOR |
| 6 | Phase 3 AMEND Source column present, all rows populated | PASS/FAIL | BREACH-MAJOR |
| 7 | Phase 3 Primary Challenge Test column present; ≥1 row T-3 | PASS/FAIL | BREACH-MAJOR |
| 8 | Phase 6 T-Evidence: structured notation on every row | PASS/FAIL | BREACH-MAJOR |
| 9 | Phase 7 Ph6 Pre-Score column present | PASS/FAIL | BREACH-MAJOR |
| 10 | `**` candidates span ≥3 categories | PASS/FAIL | BREACH-MAJOR |
| 11 | Phase 4 Challenge Binding column; Net Position → T-3 synthesis | PASS/FAIL | BREACH-MAJOR |
| 12 | Table 1C BREACH taxonomy: all 3 tiers with Signature, Protocol, Resume | PASS/FAIL | BREACH-FATAL |
| 13 | Phase 9A Pass 1: all 5 phases described with Gap + Preliminary Severity | PASS/FAIL | BREACH-MAJOR |
| 14 | Phase 9A Pass 2: Final Severity column present; no silent downgrades | PASS/FAIL | BREACH-MAJOR |

Apply Table 1C correction for every FAIL before finalizing artifact.
```

---

## V-05 — Full R12 Stack

**Variation axis:** All structural advances from R11 through R12 fully integrated: challenge-first
lifecycle, entry condition chaining, ledger blueprint, per-phase ledger obligation bullets,
ledger-violation framing, BREACH severity taxonomy (Table 1C), and two-pass terminal audit
(Reconstruct → Assess). The Reconstruct pass classifies each gap by severity tier inline.
The Assess pass is structured to upgrade — but never silently downgrade — severity from Pass 1.

**Hypothesis:** The full stack, properly ordered with C-38 and C-39 mutually reinforcing,
closes every known gap in the prompt corpus: (1) violation language is calibrated and
consistent throughout; (2) the terminal audit grounds verdicts in freshly reconstructed
evidence rather than memory; (3) severity pre-classification in the Reconstruct pass prevents
Assess-phase softening. Predicted peak coverage.

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
This phase is the single source of truth for evaluation criteria, evidence obligations, and
violation response. Nothing generated in later phases may modify, extend, or reinterpret
these tables.

#### Table 1A — Challenge Framework

| ID | Test | Pass Threshold | Survival Condition |
|----|------|----------------|--------------------|
| T-1 | Differentiation | Candidate's mechanism is meaningfully distinct from every other `**` candidate in the pool | Removing this candidate would eliminate an approach not covered by any of the other 4 `**` picks |
| T-2 | Topic Fit | Rationale makes a specific claim about `{{topic}}` that would fail if the topic were replaced | Rationale cannot be generalized to a different topic without substantial rewriting |
| T-3 | Inertia Displacement | Demonstrates explicit advantage on ≥3 named dimensions: Costs · Benefits · Competitive Threshold · Bypasses · Preserves | Names at least 3 of these 5 Phase 4 anchor field labels by name |
| T-4 | Category Coverage | Candidate occupies a category not covered by any of the other 4 `**` picks | Removing this candidate collapses top-5 below 3 distinct categories |

Survival threshold: All 4 tests must PASS. A 3/4 pass rate is a FAIL.
Challenge framework is locked at Phase 1 exit. Any modification after lock = BREACH-FATAL.

#### Table 1B — Evidence Ledger Blueprint

| Phase | Phase Name | Required Ledger Contribution | Ledger Violation Definition |
|-------|-----------|------------------------------|----------------------------|
| Phase 3 | Architecture | AMEND Source column populated on every row; Primary Challenge Test column populated on every row | Any architecture row missing either column = ledger violation |
| Phase 4 | Do Nothing Anchor | Challenge Binding column populated on every anchor field row | Any anchor row missing Challenge Binding = ledger violation |
| Phase 5 | Diverge | Name and Pitch fields populated on every candidate row | Any candidate row missing Name or Pitch = ledger violation |
| Phase 6 | Cluster + T-Evidence | T-Evidence column with structured notation `T-1:[v] · T-2:[v] · T-3:[dims cleared] · T-4:[v]` on every candidate row | Blank T-Evidence cell = ledger violation; unstructured notation = BREACH-MINOR |
| Phase 7 | Adversarial Challenge | Ph6 Pre-Score column present in challenge table; every challenge row populated | Missing Ph6 Pre-Score column = ledger violation |

#### Table 1C — BREACH Severity Taxonomy

| Tier | Signature Patterns | Correction Protocol | Resume Generation? |
|------|--------------------|---------------------|-------------------|
| BREACH-MINOR | Column present but <1/3 of rows have missing entries; threshold stated but lacks a specific numeric value; AMEND directions partially overlap; Net Position makes a directional claim without naming a displacement condition; T-Evidence present but <1/3 of cells use unstructured notation | Correct the specific cells inline. Mark every corrected cell with `[corrected]`. Continue generation after inline correction. | YES |
| BREACH-MAJOR | A required column entirely absent from a table; concentration cap exceeded at a phase exit gate; candidate count outside 20–40 at Phase 6 exit; fewer than 5 PASS verdicts available at Phase 7; Phase 9A Reconstruct pass omits one or more contributing phases; Phase 9A Declared Severity column absent; Ph6 Pre-Score column absent from Phase 7 | Halt the current phase. Reconstruct the entire affected table or step from scratch. Re-verify against exit gate criteria. Do not advance to the next phase until the reconstruction is complete and clean. | NO |
| BREACH-FATAL | Candidates generated before Phase 1 challenge framework is declared and locked; `**` marks assigned before Phase 7 adversarial challenge table is complete; Do Nothing anchor absent from the final artifact; challenge framework modified after Phase 1 lock | STOP all generation immediately. Return to the phase where this breach originated. Discard all output generated from that phase forward. Restart that phase from scratch. | NO |

Violations throughout the prompt use BREACH-MINOR / BREACH-MAJOR / BREACH-FATAL framing —
not generic checklist language. This register is active from Phase 1 forward.

Exit Phase 1:
- [ ] Table 1A: T-1 through T-4 with Pass Threshold, Survival Condition; survival threshold declared; T-3 names all 5 anchor dimensions
- [ ] Table 1A: Challenge framework locked — modification after this point is BREACH-FATAL
- [ ] Table 1B: 5 contributing phases with Required Ledger Contribution and Violation Definition
- [ ] Table 1C: All 3 tiers with Signature Patterns, Correction Protocol, and Resume decision
- [ ] Any gap: apply Table 1C tier and correction protocol before Phase 2
Ledger obligation satisfied: Phase 1 framework, blueprint, and breach taxonomy declared.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — AMEND ADJUSTMENTS
Entry: Phase 1 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write the 3 pool-shaping adjustments before generating any architecture or candidates.
These adjustments will motivate the category selection in Phase 3.

| # | Dimension | Direction | Downstream Effect on Pool |
|---|-----------|-----------|--------------------------|
| A1 | | Expands / Narrows / Redirects | |
| A2 | | Expands / Narrows / Redirects | |
| A3 | | Expands / Narrows / Redirects | |

Rules:
- Dimension: name a specific axis — "be more creative" is not a dimension; fails C-05
- Direction: all three must differ — duplicate direction = BREACH-MINOR; correct inline
- Downstream Effect: name specific `{{topic}}`-relevant candidate types that would surface
  or be displaced — "more options" is generic = BREACH-MINOR; correct inline

Exit Phase 2:
- [ ] Exactly 3 rows; all 4 columns filled; Directions all distinct; Effects `{{topic}}`-specific
- [ ] Any gap: apply Table 1C tier and correction protocol before Phase 3
Ledger obligation satisfied: AMEND adjustments committed; pool-shaping decisions recorded.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3 — ARCHITECTURE DECLARATION
Entry: Phase 2 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Declare the category structure before any candidate is generated. This is the pool's skeleton.

| Category | Description | Target Count | % of Pool | AMEND Source | Primary Challenge Test |
|----------|-------------|--------------|-----------|--------------|------------------------|

Total: ______

Rules:
- At least 4 distinct categories; no single category ≥40% of total pool
- Compute % of Pool column inline for every row — the cap must be verifiable by column value
  — if largest category is ≥40% before exit: BREACH-MAJOR; redistribute before continuing
- Every row must carry AMEND Source (A1/A2/A3): column absent = BREACH-MAJOR;
  <1/3 rows missing an entry = BREACH-MINOR
- Every row must carry Primary Challenge Test (T-1/T-2/T-3/T-4): same rules apply
- At least 1 row must list T-3 as Primary Challenge Test; 0 T-3 rows = BREACH-MAJOR
- Totals must sum to 20–40

Exit Phase 3:
- [ ] 4+ categories; % of Pool computed; no category ≥40%; totals sum to 20–40
- [ ] AMEND Source column: present and fully populated
- [ ] Primary Challenge Test column: present, fully populated, ≥1 T-3 row
- [ ] Any gap: apply Table 1C tier and correction protocol before Phase 4
Ledger obligation satisfied: Architecture table carries AMEND Source and Primary Challenge Test on every row.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — DO NOTHING ANCHOR
Entry: Phase 3 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write the status quo as the primary comparator, after architecture exists so that Bypasses
and Preserves can reference specific Phase 3 category labels.

| Field | Content | Challenge Binding |
|-------|---------|-------------------|
| Costs | [specific costs of the status quo for `{{topic}}`] | T-3 |
| Benefits | [genuine appeal of the status quo — why inertia is attractive for `{{topic}}`] | T-3 |
| Competitive Threshold | [minimum advantage any alternative must demonstrate to displace this anchor; name a specific Phase 3 category] | T-3 |
| Bypasses | [Phase 3 category labels that the status quo renders unnecessary; name ≥1 by label] | T-3 |
| Preserves | [what a transition from the status quo would put at risk for `{{topic}}`] | T-3 |
| Net Position | [integrated judgment: does inertia currently dominate? Name the specific condition under which it would stop dominating] | T-3 synthesis |

Rules:
- Costs AND Benefits must both be present — costs-only = BREACH-MINOR; correct before exit
- Bypasses and Preserves must reference Phase 3 category labels — generic = BREACH-MINOR
- Net Position must name a displacement condition — directional claim without condition = BREACH-MINOR
- Challenge Binding column must be present on every row — absent column = BREACH-MAJOR
- Net Position must map to "T-3 synthesis" not "T-3" — conflation = BREACH-MINOR
- Do Nothing does NOT count toward the 20–40 candidate total

Exit Phase 4:
- [ ] All 6 fields present with `{{topic}}`-specific content
- [ ] Costs AND Benefits both present; Competitive Threshold names Phase 3 category
- [ ] Bypasses and Preserves reference Phase 3 category labels
- [ ] Net Position is integrative and names a displacement condition
- [ ] Challenge Binding column present, every row populated, Net Position → T-3 synthesis
- [ ] Any gap: apply Table 1C tier and correction protocol before Phase 5
Ledger obligation satisfied: Anchor table carries Challenge Binding column on every row.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5 — DIVERGE (Name + Pitch Only)
Entry: Phase 4 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Generate candidate names and one-line pitches only. No categories, rationales, T-Evidence,
or `**` marks in this phase — generation is deliberately separated from categorization (C-11).

Target: 22–38 Name+Pitch entries.

Rules:
- Do not assign Category, Rationale, or T-Evidence — doing so here is a protocol violation
- Do not mark any candidate `**` — BREACH-FATAL
- If one conceptual area is filling up before you finish: shift to a different angle before
  continuing — this is an inline guard against Phase 6 concentration problems
- Any candidate row with a blank Name or Pitch = BREACH-MINOR; correct inline

Exit Phase 5:
- [ ] 22–38 Name+Pitch pairs; no categories, rationales, or `**` marks
- [ ] Any gap: apply Table 1C tier and correction protocol before Phase 6
Ledger obligation satisfied: Diverge Name+Pitch pairs available for cluster phase.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6 — CLUSTER + T-EVIDENCE
Entry: Phase 5 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Assign Category and Rationale to every candidate. Then annotate T-Evidence for every row.

| # | Name | Pitch | Category | Rationale | T-Evidence |
|---|------|-------|----------|-----------|------------|

T-Evidence format: `T-1:PASS/PARTIAL/FAIL · T-2:PASS/PARTIAL/FAIL · T-3:[dims cleared, e.g. Costs+Benefits+Preserves] · T-4:PASS/PARTIAL/FAIL`

Rules:
- Rationale must reference a specific dimension of `{{topic}}` — generic rationale = BREACH-MINOR
- T-Evidence column absent = BREACH-MAJOR; <1/3 cells blank = BREACH-MINOR; ≥1/3 blank = BREACH-MAJOR
- Unstructured T-Evidence notation (not matching the format above) = BREACH-MINOR
- Check concentration cap on completion: any category ≥40% = BREACH-MAJOR; redistribute
- Candidate count outside 20–40 = BREACH-MAJOR

Exit Phase 6:
- [ ] All 4 anatomy fields on every candidate
- [ ] T-Evidence column present with structured notation on every row
- [ ] No category ≥40%; candidate count 20–40
- [ ] Any gap: apply Table 1C tier and correction protocol before Phase 7
Ledger obligation satisfied: Cluster table with T-Evidence structured notation on every row.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — ADVERSARIAL CHALLENGE
Entry: Phase 6 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Identify 8–10 tentative top candidates. Do NOT assign `**` marks yet — marks are assigned
only after this table is complete and exactly 5 PASS verdicts are confirmed.

| # | Candidate | T-1: Differentiation | T-2: Topic Fit | T-3: Inertia Displacement (name Phase 4 dims) | T-4: Category Coverage | Ph6 Pre-Score | Verdict |
|---|-----------|---------------------|---------------|-----------------------------------------------|------------------------|---------------|---------|

Rules:
- Ph6 Pre-Score: carry T-Evidence notation from Phase 6 forward verbatim — any modification
  to the pre-score before Phase 7 adjudication = BREACH-MINOR
- T-3 column: name specific Phase 4 anchor field labels cleared (Costs / Benefits /
  Competitive Threshold / Bypasses / Preserves) — "displaces status quo" without dims = BREACH-MINOR
- Verdict: PASS (all 4 tests) or FAIL (name which test failed) — 3/4 = FAIL
- Selecting fewer than 5 PASS-verdict candidates for `**` = BREACH-MAJOR
- Ph6 Pre-Score column absent = BREACH-MAJOR
- Assigning `**` before this table is complete = BREACH-FATAL

After table: assign exactly 5 `**` from PASS verdicts spanning ≥3 categories.

Exit Phase 7:
- [ ] Ph6 Pre-Score column present and populated from Phase 6 verbatim
- [ ] T-3 column names Phase 4 anchor dims for every candidate
- [ ] Exactly 5 PASS → `**`; `**` candidates span ≥3 categories
- [ ] Any gap: apply Table 1C tier and correction protocol before Phase 8
Ledger obligation satisfied: Challenge table with Ph6 Pre-Score carryforward complete.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 8 — ARTIFACT ASSEMBLY
Entry: Phase 7 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write the final artifact to: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md

Structure:
1. Header: topic, date, total candidate count (20–40), `**` count (exactly 5)
2. AMEND section: A1, A2, A3 — each with dimension, direction, downstream effect
3. Candidate pool: grouped by category with `**` marks on exactly 5 candidates
4. Do Nothing / Status Quo section: 6-field anchor table, outside and after the numbered pool

Exit Phase 8:
- [ ] Artifact written to correct path with all 4 structural sections
- [ ] `**` count in artifact = exactly 5; candidate count (excluding Do Nothing) = 20–40

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9A — TERMINAL LEDGER AUDIT (TWO-PASS: RECONSTRUCT THEN ASSESS)
Entry: Phase 8 complete.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Phase 9A has two mandatory sequential passes. Phase 9B may not begin until both passes are
complete and all Assess rows reach COMPLETE.

### Pass 1 — RECONSTRUCT WITH SEVERITY PRE-CLASSIFICATION

For each contributing phase: describe what it produced in this execution (not what was
instructed), identify any gap, and classify the gap severity using Table 1C.
No COMPLETE / VIOLATION verdicts in Pass 1 — only description, gap identification, and
preliminary severity classification.

| Phase | What It Actually Produced (field-level) | Gap Observed | Preliminary Severity |
|-------|----------------------------------------|--------------|---------------------|
| Phase 3 | [Describe: how many categories; whether AMEND Source column was present and which rows, if any, were unpopulated; whether Primary Challenge Test column was present and which rows, if any, were unpopulated; what the % of Pool values were; whether any row was missing either required column] | | [BREACH-MINOR / BREACH-MAJOR / BREACH-FATAL / none] |
| Phase 4 | [Describe: which 6 anchor fields were written; whether Challenge Binding column was present and on which rows; what Net Position actually stated and whether it named a displacement condition; whether Bypasses and Preserves referenced specific Phase 3 category names] | | |
| Phase 5 | [Describe: exact candidate count generated; whether any Category, Rationale, or T-Evidence appeared in this phase; whether any `**` marks appeared; whether any Name or Pitch cells were blank] | | |
| Phase 6 | [Describe: final candidate count; whether T-Evidence column was present; what notation format was used; how many cells, if any, were blank; what the highest-concentration category was and its % of Pool] | | |
| Phase 7 | [Describe: how many candidates were entered in the challenge table; whether Ph6 Pre-Score column was present; how many PASS verdicts were reached; which 5 candidates received `**`; how many distinct categories those 5 span; whether any `**` mark was assigned before table completion] | | |

Reconstruct rules:
- Every contributing phase must have a description row — omitting a phase = BREACH-MAJOR
- Gap must be identified even if the finding is "none" — leave blank is not acceptable
- Preliminary Severity must be classified for every row — "none" is an acceptable answer
  for rows with no gap detected
- Use specific field names: "Phase 6 T-Evidence column: present, structured notation on
  all 30 rows" — not "Phase 6 completed successfully"
- A prose summary without field-level observations does not constitute a Reconstruct row

### Pass 2 — ASSESS AGAINST LEDGER BLUEPRINT

Apply ledger criteria against Pass 1 descriptions. Preliminary Severity from Pass 1 carries
forward — any upgrade requires naming new evidence; any downgrade requires explicit
justification in the Notes field; silent downgrade = BREACH-MINOR.

| Phase | Ledger Field Expected | Pass 1 Evidence (reference) | Status | Final Severity | Notes / Correction Applied |
|-------|----------------------|----------------------------|--------|----------------|---------------------------|
| Phase 3 | AMEND Source + Primary Challenge Test columns; every row populated | [cite specific Pass 1 observation] | COMPLETE / VIOLATION | [from Pass 1; note if upgraded or downgraded and why] | |
| Phase 4 | Challenge Binding column; every anchor field row populated | [cite specific Pass 1 observation] | | | |
| Phase 5 | Name + Pitch; every candidate row; no premature categorization or `**` | [cite specific Pass 1 observation] | | | |
| Phase 6 | T-Evidence with structured notation; every row; no blanks | [cite specific Pass 1 observation] | | | |
| Phase 7 | Ph6 Pre-Score column present; every challenge row populated | [cite specific Pass 1 observation] | | | |

Assess rules:
- Pass 1 Evidence must cite a specific field-level observation from the Reconstruct table
- Status verdicts must be grounded in Pass 1 evidence — expectation-based verdicts are invalid
- Final Severity: carry from Pass 1 preliminary with explicit justification for any change
- Apply Table 1C correction protocol for every VIOLATION row before Phase 9B
- If a VIOLATION requires BREACH-MAJOR correction: halt, reconstruct, re-verify,
  and re-run the affected row in Pass 2 before proceeding

Exit Phase 9A:
- [ ] Pass 1: all 5 phases described at field level with Gap and Preliminary Severity
- [ ] Pass 2: all 5 rows carry Pass 1 Evidence reference, Status, Final Severity, and Notes
- [ ] All VIOLATION rows corrected per Table 1C protocol
- [ ] No silent severity downgrade without explicit justification

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9B — CRITERION CHECKLIST
Entry: Phase 9A complete — both passes done; all 5 ledger rows COMPLETE.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Row | Criterion | Status | Declared Severity if FAIL |
|-----|-----------|--------|--------------------------|
| 1 | Candidate count 20–40 (excluding Do Nothing) | PASS/FAIL | BREACH-MAJOR |
| 2 | Every candidate has all 4 anatomy fields (Name, Pitch, Category, Rationale) | PASS/FAIL | BREACH-MAJOR |
| 3 | Exactly 5 `**` marks in the artifact | PASS/FAIL | BREACH-MAJOR |
| 4 | Do Nothing present with 6 fields; Net Position names displacement condition | PASS/FAIL | BREACH-MAJOR |
| 5 | AMEND: 3 adjustments each with dimension, direction, and downstream effect | PASS/FAIL | BREACH-MINOR |
| 6 | Phase 3 AMEND Source column: present, all rows populated | PASS/FAIL | BREACH-MAJOR |
| 7 | Phase 3 Primary Challenge Test column: present, all rows populated, ≥1 T-3 row | PASS/FAIL | BREACH-MAJOR |
| 8 | Phase 6 T-Evidence: structured notation on every row, no blank cells | PASS/FAIL | BREACH-MAJOR |
| 9 | Phase 7 Ph6 Pre-Score column present and populated | PASS/FAIL | BREACH-MAJOR |
| 10 | `**` candidates span ≥3 categories | PASS/FAIL | BREACH-MAJOR |
| 11 | Phase 4 Challenge Binding column: present; Net Position → T-3 synthesis | PASS/FAIL | BREACH-MAJOR |
| 12 | Table 1C BREACH taxonomy declared in Phase 1 with all 3 tiers, all columns | PASS/FAIL | BREACH-FATAL |
| 13 | Phase 9A Pass 1: all 5 phases reconstructed at field level with Gap + Preliminary Severity | PASS/FAIL | BREACH-MAJOR |
| 14 | Phase 9A Pass 2: Final Severity column present; Pass 1 Evidence cited per row; no silent downgrades | PASS/FAIL | BREACH-MAJOR |
| 15 | Phase 1 challenge framework was locked before Phase 2; no modification after lock detected | PASS/FAIL | BREACH-FATAL |

Apply Table 1C correction protocol for every FAIL before finalizing the artifact.
```

---

## Axis Summary

| Variation | C-38 (Breach Taxonomy) | C-39 (Two-Pass Audit) | Bidirectional Binding | Phrasing Register |
|-----------|----------------------|----------------------|----------------------|-------------------|
| V-01 | PRIMARY: Table 1C declared in Phase 1; Declared Severity column in Phase 9A | Implicit (Phase 9A has a single pass; Phase 9B remains) | No | Formal imperative |
| V-02 | Absent (single-level violation language) | PRIMARY: Phase 9A split into Reconstruct then Assess; Pass 1 is description-only | No | Formal imperative |
| V-03 | Present as "Violation Severity Reference" table | Present as "Two Passes" in Step 9A | Weak (severity used in Pass 2 only) | Conversational descriptive |
| V-04 | Present as Table 1C; per-tier protocols throughout | Present as Phase 9A Reconstruct+Assess | STRONG: Preliminary Severity in Pass 1 carries into Final Severity in Pass 2; silent downgrade is BREACH-MINOR | Formal imperative |
| V-05 | Present as Table 1C; violation framing throughout all phases | Present as Phase 9A Reconstruct+Assess with field-level description requirements | STRONGEST: Pass 1 pre-classifies severity; Pass 2 may upgrade with evidence or downgrade with justification; silent downgrade = BREACH-MINOR | Formal imperative |

**Predicted excellence signals:**
- C-38 first appears with full tier definitions in V-01 and is present in V-03/V-04/V-05
- C-39 first appears with explicit two-pass structure in V-02 and is present in V-03/V-04/V-05
- V-04 introduces bidirectional severity binding between Reconstruct and Assess
- V-05 adds the "no silent downgrade" rule and "Preliminary Severity" column in Pass 1,
  which is the new excellence signal to watch for as a potential C-40

**Known unresolved gap from R11:** C-27 PARTIAL (anchor field names absent from Phase 7
column schema as structural headers rather than prose instructions). All 5 R12 variations
use `T-3: Inertia Displacement (name Phase 4 dims)` as a column header — this is the
closest any variation has come to PASS on C-27. Whether the parenthetical constitutes
"column header naming the anchor field labels" per the rubric requires scoring verification.
