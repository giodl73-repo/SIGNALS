# draft-brainstorm Skill Prompt Variations — Round 15

**Skill:** draft-brainstorm
**Round:** 15
**Date:** 2026-03-15
**Rubric:** v14 (C-01 through C-44)
**Baseline:** R14 closes C-41 and C-42 as stable baselines — all 5 R14 variations PASS. R15 targets C-43 and C-44.

---

## R15 Axis Selection

R14 confirmed C-41 (Table 1B BREACH Tier column) and C-42 (Phase 9A Reconstruct T-3 header enumeration) stable across all 5 variations. The v14 rubric adds two new aspirational criteria extracted from R14 V-04 and V-05 excellence signals:

- **C-43**: Anchor Citation as mandatory Phase 6 cluster column — a dedicated column, separate from T-Evidence, recording the specific anchor field labels (e.g., "Costs", "Bypasses") cited in each candidate's Rationale at generation time. C-43 transforms Phase 7 T-3 from first-pass evaluation to adjudication of pre-declared claims.
- **C-44**: Bidirectional gate schema — every phase carries a named ENTRY TABLE (specific predecessor artifacts, one row each) AND a named EXIT TABLE (departure conditions with BREACH tier column). C-29 entry conditions and C-19 exit gates already required the information; C-44 requires table schema form at every phase boundary, with ENTRY TABLEs naming specific artifacts — not just "Phase N exit gates passed."

R14 V-04 had bidirectional tables but ENTRY TABLEs mixed specific artifact names with generic "Phase N exit gates: all PASS" rows. R14 V-05 had the Anchor Citation requirement stated in Phase 4 as a forward pre-commitment but no dedicated cluster column schema — the Phase 6 Anchor Citation appeared in the table but as an instruction, not a ledger-tracked obligation.

| Variation | Primary Axis | Novel Structural Feature |
|-----------|--------------|--------------------------|
| V-01 | C-44 single-axis | ENTRY TABLEs name specific predecessor artifacts (no generic "Phase N exit gates" rows); EXIT TABLEs carry BREACH tier column |
| V-02 | C-43 single-axis | Anchor Citation as a Table 1B ledger obligation; Phase 6 cluster column schema with dedicated "Anchor Citation" column |
| V-03 | C-43 single-axis (anchor-forward) | Phase 4 produces Anchor Field Label Reference sub-artifact; Phase 6 loads it as Step 0 before cluster generation; inline conditional rewrites zero-citation rationales |
| V-04 | C-43 + C-44 combined | Artifact-specific ENTRY TABLEs + Anchor Citation ledger obligation; both C-43 and C-44 as co-required phase obligations |
| V-05 | C-43 + C-44 + Phase 7 adjudication reframe | Phase 7 renamed Evidence Triage; Ph6 Anchor Citation is first column loaded; T-3 evaluation framed as adjudication of pre-declared claims, not first-pass judgment |

---

## V-01 — Single-axis: C-44 Entry Table Artifact Specificity

**Variation axis:** Lifecycle emphasis — every phase boundary carries a full ENTRY TABLE where each row names a specific predecessor artifact by name and source phase. No row may read "Phase N exit gates: all PASS" — the artifact must be named. EXIT TABLEs carry a BREACH tier column. No C-43 change — standard T-Evidence only.

**Hypothesis:** R14 V-04 had bidirectional tables but ENTRY TABLEs still used generic preconditions alongside specific ones. C-44 requires every ENTRY TABLE row to name a specific artifact. The hypothesis is that forcing artifact-level specificity in entry conditions makes the dependency chain auditable in Phase 9A: the Reconstruct pass can verify not just that phases executed but that the specific required artifacts were present. This also prevents "phantom" phase execution where a phase runs but was actually missing its prerequisite output.

---

```
You are generating a brainstorm artifact for the topic: `{{topic}}`
Output date: `{{date}}`
Artifact path: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 1 — CHALLENGE FRAMEWORK + LEDGER CONTRACT + BREACH TAXONOMY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 1
| Predecessor Artifact | Source | Required State |
|---------------------|--------|----------------|
| (session root — no predecessor) | — | — |

Declare three co-equal Phase 1 artifacts before any generation begins.

#### Table 1A — Challenge Framework

| ID | Test | Pass Threshold | Phase 7 Column Schema | Survival Condition |
|----|------|----------------|-----------------------|--------------------|
| T-1 | Differentiation | Meaningfully distinct mechanism from every other `**` candidate | "T-1: Differentiation" | Removing this candidate eliminates an approach not covered by remaining 4 |
| T-2 | Topic Fit | Rationale names a specific dimension of `{{topic}}` — not generic | "T-2: Topic Fit" | Rationale fails if topic is swapped out |
| T-3 | Inertia Displacement | PASS on ≥3 of 5 anchor fields evaluated independently | **Five columns:** "T-3: Costs" / "T-3: Benefits" / "T-3: Competitive Threshold" / "T-3: Bypasses" / "T-3: Preserves" — exact labels locked at Phase 1 | ≥3 PASS cells across 5 anchor-named T-3 columns |
| T-4 | Category Coverage | Candidate's category absent from other 4 `**` picks | "T-4: Category Coverage" | Removing this pick collapses top-5 below 3 categories |

Survival threshold: all 4 tests PASS. T-3 schema LOCKED at Phase 1 exit — deviation is BREACH-MAJOR. Framework LOCKED — modification is BREACH-FATAL.

#### Table 1B — Ledger Contract (Blueprint + Taxonomy fused; per-row correction authority)

| Phase | Phase Name | Ledger Field | Violation Condition | BREACH Tier | Correction Action | Continue? |
|-------|-----------|--------------|---------------------|-------------|-------------------|-----------|
| 3 | Architecture | AMEND Source + Primary Challenge Test cols on every row | Any row missing either column | BREACH-MAJOR | Halt. Add col. Repopulate. Re-verify. | NO |
| 4 | Do Nothing Anchor | Challenge Binding col on every anchor row | Any row missing Challenge Binding | BREACH-MAJOR | Halt. Add col. Correct all rows. | NO |
| 5 | Diverge | Name + Pitch on every candidate row | Any candidate missing Name or Pitch | BREACH-MINOR | Correct in-place. Mark `[corrected]`. | YES |
| 6 | Cluster + T-Evidence | T-Evidence col with structured notation `T-1:[v]·T-2:[v]·T-3:[dims]·T-4:[v]` on every row | Col absent; >1/3 rows unstructured | BREACH-MAJOR if col absent; BREACH-MINOR if <1/3 blank | Col absent: halt, add, repopulate. Blank: correct inline. | Col absent: NO. Cells: YES |
| 7 | Adversarial Challenge | Ph6 Pre-Score col + T-3 via 5 locked anchor-named cols | Missing Ph6 Pre-Score; merged T-3 col; labels deviate | BREACH-FATAL if `**` pre-assigned; BREACH-MAJOR for schema deviations | Pre-assigned `**`: stop, discard Phase 7+, restart. Schema: halt, reconstruct. | NO |

#### Table 1C — BREACH Severity Taxonomy

| Severity | Definition | Correction Protocol | Continue? |
|----------|------------|---------------------|-----------|
| BREACH-MINOR | Recommended field absent; <1/3 rows missing content; overlapping AMEND directions | Correct in-place; mark `[corrected]` | YES |
| BREACH-MAJOR | Required ledger column absent; concentration cap exceeded; count outside 20–40; T-3 schema deviated | HALT; reconstruct affected table; re-verify before advancing | NO |
| BREACH-FATAL | Candidates before Phase 1; `**` before Phase 7; anchor absent; framework modified after lock | STOP; discard from originating phase; restart | NO |

EXIT TABLE — Phase 1
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Table 1A: T-1/T-2/T-3/T-4 with Phase 7 column schema; T-3 names all 5 labels | BREACH-FATAL |
| Table 1B: 5 obligation rows; BREACH Tier + Correction Action + Continue? columns populated | BREACH-MAJOR |
| Table 1C: all 3 severity tiers with correction protocols | BREACH-MAJOR |
| Challenge framework locked; T-3 schema locked | — |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — AMEND ADJUSTMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 2
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Table 1A (Challenge Framework) | Phase 1 | T-1/T-2/T-3/T-4 declared; T-3 schema locked (5 column labels) |
| Table 1B (Ledger Contract) | Phase 1 | 5 obligation rows; BREACH Tier column populated on every row |
| Table 1C (BREACH Taxonomy) | Phase 1 | 3 severity tiers with correction protocols |

Write exactly 3 pool-shaping adjustments before architecture or candidates are generated.

| # | Dimension | Direction | Downstream Effect on Pool |
|---|-----------|-----------|--------------------------|
| A1 | | | |
| A2 | | | |
| A3 | | | |

Rules: Dimension names a specific axis; Directions non-overlapping (one expands, one narrows, one redirects — not all pointing the same way); Downstream Effects `{{topic}}`-specific.

EXIT TABLE — Phase 2
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Exactly 3 AMEND rows; Dimension + Direction + Downstream Effect columns filled | BREACH-MINOR if any col blank |
| Directions distinct (non-overlapping) | BREACH-MINOR if duplicate direction |
| Downstream Effects reference `{{topic}}` specifically | BREACH-MINOR if generic |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3 — ARCHITECTURE DECLARATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 3
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| AMEND Adjustments Table (A1/A2/A3) | Phase 2 | 3 rows; Dimension + Direction + Downstream Effect filled |

Declare category structure before generating any candidates.

| Category | Description | Target Count | % of Pool | AMEND Source | Primary Challenge Test |
|----------|-------------|--------------|-----------|--------------|------------------------|

Total: ______

Rules: ≥4 categories; largest ≤40% of pool; totals 20–40; every row has AMEND Source (A1/A2/A3) + Primary Challenge Test (T-1/T-2/T-3/T-4); ≥1 row lists T-3. If largest category ≥40% — redistribute before exit (BREACH-MAJOR if not corrected).

EXIT TABLE — Phase 3
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| ≥4 distinct categories; % of Pool computed | BREACH-MAJOR |
| No category ≥40% of total | BREACH-MAJOR |
| AMEND Source column present; every row populated | BREACH-MAJOR |
| Primary Challenge Test column present; ≥1 row lists T-3 | BREACH-MAJOR |
| Total count 20–40 | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — DO NOTHING ANCHOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 4
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Category Architecture Table | Phase 3 | ≥4 categories; AMEND Source + Primary Challenge Test columns; ≥1 T-3 row; ≤40% cap |
| AMEND Adjustments Table (A1/A2/A3) | Phase 2 | 3 rows with Dimension + Direction + Downstream Effect |

Write the status quo anchor grounded in the Phase 3 category architecture. Bypasses and Preserves must reference specific Phase 3 category labels.

| Field | Content | Challenge Binding |
|-------|---------|-------------------|
| Costs | [active costs of status quo for `{{topic}}`] | T-3 |
| Benefits | [genuine appeal of status quo — why inertia persists] | T-3 |
| Competitive Threshold | [minimum advantage an alternative must demonstrate; reference ≥1 Phase 3 category] | T-3 |
| Bypasses | [Phase 3 category labels the status quo renders unnecessary — name ≥1 by label] | T-3 |
| Preserves | [what a transition would put at risk for `{{topic}}`] | T-3 |
| Net Position | [integrated judgment: does inertia dominate? name the displacement condition] | T-3 synthesis |

Rules: All 6 fields present; Costs AND Benefits both present (costs-only: BREACH-MINOR); Bypasses + Preserves name Phase 3 labels (generic: BREACH-MINOR); Net Position names a displacement condition (directional-only: BREACH-MINOR); Challenge Binding col present on every row (absent: BREACH-MAJOR per Table 1B). Do Nothing does NOT count toward 20–40 candidate total.

EXIT TABLE — Phase 4
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| All 6 field rows present with `{{topic}}`-specific content | BREACH-MAJOR |
| Challenge Binding column present; all 6 rows populated | BREACH-MAJOR |
| Costs AND Benefits both present | BREACH-MINOR |
| Bypasses + Preserves name Phase 3 category labels | BREACH-MINOR |
| Net Position names a displacement condition | BREACH-MINOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5 — DIVERGE (Name + Pitch Only)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 5
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Do Nothing Anchor Table (6 fields) | Phase 4 | Costs/Benefits/Competitive Threshold/Bypasses/Preserves/Net Position; Challenge Binding column |
| Category Architecture Table | Phase 3 | Category labels and slot budgets available |

Generate 22–38 Name+Pitch pairs only. No categories, rationales, or T-Evidence yet. No `**` marks — BREACH-FATAL if assigned before Phase 7.

| # | Name | Pitch (one line) |
|---|------|-----------------|

EXIT TABLE — Phase 5
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| 20–40 candidate rows (Name + Pitch only) | BREACH-MAJOR |
| No categories, rationales, or `**` marks assigned | BREACH-MINOR if present |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6 — CLUSTER + T-EVIDENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 6
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Diverge List | Phase 5 | 20–40 Name+Pitch rows; no categories or rationales |
| Category Architecture Table | Phase 3 | Category labels with slot budgets |
| Do Nothing Anchor Table | Phase 4 | 6 anchor fields; Challenge Binding column |

Assign Category, Rationale, and T-Evidence to every candidate from Phase 5.

| # | Name | Category | Rationale | T-Evidence |
|---|------|----------|-----------|------------|

- **T-Evidence format**: `T-1:[PASS/PARTIAL/FAIL]·T-2:[PASS/PARTIAL/FAIL]·T-3:[dims cleared]·T-4:[PASS/PARTIAL/FAIL]`
- T-3 dims cleared: list the specific anchor field labels where the Rationale demonstrates superiority (e.g., "Costs+Bypasses")
- Rationale must be `{{topic}}`-specific — generic rationale swappable to any topic: BREACH-MINOR
- Concentration inline check: if any category reaches 40% of total rows — redistribute before continuing (BREACH-MAJOR)

EXIT TABLE — Phase 6
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| T-Evidence column present; structured notation on every row | BREACH-MAJOR if col absent; BREACH-MINOR if <1/3 blank |
| No category exceeds 40% | BREACH-MAJOR |
| All candidates from Phase 5 present | BREACH-MAJOR |
| Rationales reference `{{topic}}` specifically | BREACH-MINOR if >1/5 generic |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — ADVERSARIAL CHALLENGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 7
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Cluster Table | Phase 6 | T-Evidence column with structured notation; all rows populated |
| Do Nothing Anchor Table | Phase 4 | 6 fields declared; Challenge Binding column present |
| Table 1A (Challenge Framework) | Phase 1 | T-3 column schema locked (5 labels: Costs/Benefits/Competitive Threshold/Bypasses/Preserves) |

Challenge every candidate. Do not mark `**` yet — BREACH-FATAL if any `**` assigned in this phase.

Column schema (mandatory):
`| # | Name | Ph6 Pre-Score | T-1: Differentiation | T-2: Topic Fit | T-3: Costs | T-3: Benefits | T-3: Competitive Threshold | T-3: Bypasses | T-3: Preserves | T-4: Category Coverage | Verdict |`

- **Ph6 Pre-Score**: copy T-Evidence structured notation from Phase 6 verbatim
- **T-3 columns**: use exact anchor field labels from Table 1A (five columns; merged single-column is BREACH-MAJOR)
- T-3 PASS threshold: ≥3 PASS cells across 5 anchor-named columns; PARTIAL counts as half

EXIT TABLE — Phase 7
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Ph6 Pre-Score column present; populated from Phase 6 T-Evidence | BREACH-MAJOR |
| T-3 evaluated via 5 separate columns using locked anchor field labels | BREACH-MAJOR |
| No `**` marks assigned | BREACH-FATAL if present |
| All candidates evaluated with Verdict | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 8 — MARK + FINALIZE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 8
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 7 Challenge Table | Phase 7 | All candidates evaluated; Ph6 Pre-Score column present; 5 T-3 anchor-named columns; no `**` marks |
| Table 1A (Survival Threshold) | Phase 1 | All 4 tests PASS required for `**` |

Select the top 5 candidates. Apply `**` to exactly 5 entries in the Phase 6 cluster table. Top-5 set must span ≥3 distinct categories. Removing any one pick must eliminate a distinct angle. If <5 survive all 4 tests — select 5 by partial score, note any compromise.

EXIT TABLE — Phase 8
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Exactly 5 `**` marks applied | BREACH-FATAL |
| `**` set spans ≥3 distinct categories | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9A — TERMINAL LEDGER AUDIT (Reconstruct → Assess)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 9A
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 8 Output (`**` marks applied) | Phase 8 | Exactly 5 `**` marks on Cluster Table |
| Phase 7 Challenge Table | Phase 7 | All candidates evaluated; no post-Phase-8 modifications |
| All contributing phases (3–7) | Phases 3–7 | Exit gates declared passed |

Phase 9B may not begin until Phase 9A is complete and all ledger rows are COMPLETE.

**RECONSTRUCT PASS** — For each ledger row, describe what was concretely produced in this execution (one row per contributing phase):

| Phase | Obligation | What Was Actually Produced | COMPLETE? |
|-------|-----------|---------------------------|-----------|
| Phase 3 | AMEND Source + Primary Challenge Test cols | [describe: column names present, row count] | Y/N |
| Phase 4 | Challenge Binding col on anchor table | [describe: column present, rows mapped] | Y/N |
| Phase 5 | Name + Pitch on every candidate | [describe: row count, any blank cells] | Y/N |
| Phase 6 | T-Evidence structured notation | [describe: notation format used, blank row count] | Y/N |
| Phase 7 | Ph6 Pre-Score col + T-3 anchor-named cols | **T-3 column headers observed: [enumerate each T-3-prefixed header exactly as written in Phase 7]** Expected: T-3: Costs / T-3: Benefits / T-3: Competitive Threshold / T-3: Bypasses / T-3: Preserves. Match result per header: [MATCH/MISMATCH for each]. C-27 verdict: PASS/PARTIAL/FAIL | Y/N |

**ASSESS PASS** — Apply ledger criteria and violation definitions:

| Ledger Row | Status | Declared Severity | Action Required |
|-----------|--------|-------------------|----------------|
| Phase 3 architecture | COMPLETE/VIOLATION | | |
| Phase 4 anchor | COMPLETE/VIOLATION | | |
| Phase 5 diverge | COMPLETE/VIOLATION | | |
| Phase 6 T-Evidence | COMPLETE/VIOLATION | | |
| Phase 7 challenge | COMPLETE/VIOLATION | | |

Correct all VIOLATION rows before advancing to Phase 9B.

EXIT TABLE — Phase 9A
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Reconstruct pass completed (one row per contributing phase) | BREACH-MAJOR |
| T-3 column headers enumerated for Phase 7 row; C-27 verdict rendered | BREACH-MAJOR |
| Assess pass completed; Declared Severity populated for all rows | BREACH-MAJOR |
| All ledger rows COMPLETE | BREACH-FATAL |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9B — CRITERION CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 9B
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 9A Terminal Ledger Audit | Phase 9A | Reconstruct + Assess passes complete; all 5 ledger rows COMPLETE; C-27 verdict rendered |

| Row | Criterion | Status | Severity if FAIL |
|-----|-----------|--------|-----------------|
| 1 | Candidate count 20–40 (excl. Do Nothing) | PASS/FAIL | BREACH-MAJOR |
| 2 | Every candidate has Name + Pitch + Category + Rationale | PASS/FAIL | BREACH-MAJOR |
| 3 | Exactly 5 `**` marks | PASS/FAIL | BREACH-FATAL |
| 4 | Do Nothing present with 6 fields incl. Net Position | PASS/FAIL | BREACH-MAJOR |
| 5 | AMEND has 3 adjustments; each names dimension + downstream effect | PASS/FAIL | BREACH-MINOR |
| 6 | Architecture table: AMEND Source col; every row populated | PASS/FAIL | BREACH-MAJOR |
| 7 | Architecture table: Primary Challenge Test col; ≥1 row T-3 | PASS/FAIL | BREACH-MAJOR |
| 8 | Phase 6 cluster: T-Evidence with structured notation | PASS/FAIL | BREACH-MAJOR |
| 9 | Phase 7 challenge: Ph6 Pre-Score carryforward column | PASS/FAIL | BREACH-MAJOR |
| 10 | `**` set spans ≥3 categories | PASS/FAIL | BREACH-MAJOR |
| 11 | Phase 4 anchor Challenge Binding col; Net Position maps to T-3 synthesis | PASS/FAIL | BREACH-MAJOR |
| 12 | Table 1C BREACH taxonomy: all 3 tiers | PASS/FAIL | BREACH-FATAL |
| 13 | Phase 9A Declared Severity column populated | PASS/FAIL | BREACH-MAJOR |
| 14 | Phase 7 T-3 via 5 separate anchor-named columns | PASS/FAIL | BREACH-MAJOR |
| 15 | Table 1B carries BREACH Tier column; all rows populated | PASS/FAIL | BREACH-MAJOR |
| 16 | Phase 9A Reconstruct T-3 step complete; C-27 verdict rendered | PASS/FAIL | BREACH-MAJOR |

Apply Table 1C correction protocol for every FAIL before writing the artifact.

EXIT TABLE — Phase 9B
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| All 16 rows checked | BREACH-MINOR |
| All FAIL rows corrected | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WRITE — ARTIFACT ASSEMBLY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — WRITE
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 9B Criterion Checklist | Phase 9B | All 16 rows PASS or corrected |
| Cluster Table with `**` marks | Phase 8 | Exactly 5 `**` marks |
| AMEND Adjustments Table | Phase 2 | 3 adjustments for AMEND section |
| Do Nothing Anchor Table | Phase 4 | 6 fields for dedicated section |

Write the artifact to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

Structure:
1. `# {{topic}} — Brainstorm Pool`
2. `## AMEND` — 3 labeled adjustments (A1/A2/A3)
3. `## Do Nothing` — status quo with costs, benefits, net position
4. Category sections with candidates grouped; `**` on top-5 entries
5. Each entry: **Name** — Pitch — Rationale
```

---

## V-02 — Single-axis: C-43 Anchor Citation Column (Ledger Pre-commitment)

**Variation axis:** Inertia framing — the Do Nothing anchor is pre-committed as a generative scaffold, not a terminal comparator. A dedicated "Anchor Citation" column in Phase 6 records which anchor field labels each candidate's Rationale explicitly cites at generation time. This is distinct from T-Evidence dims cleared (C-32/C-33): T-Evidence records challenge-readiness verdicts; Anchor Citation records the specific displacement claims declared. Table 1B carries this as a BREACH-MAJOR obligation. No C-44 change — standard R14 V-05 entry/exit gate format.

**Hypothesis:** R14 V-05 pre-committed the anchor citation requirement in Phase 4 ("every candidate's Rationale must cite ≥1 anchor field") but did not give it its own Phase 6 column separate from T-Evidence. When the citation obligation is embedded in T-3 dims cleared, Phase 7 merges evaluation and evidence in a single column. Splitting Anchor Citation into its own column forces the model to explicitly name the anchor field being displaced at write time — making Phase 7 an adjudication step rather than a judgment step.

---

```
You are generating a brainstorm artifact for the topic: `{{topic}}`
Output date: `{{date}}`
Artifact path: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 1 — CHALLENGE FRAMEWORK + LEDGER CONTRACT + BREACH TAXONOMY
Entry: Start of session.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Declare three co-equal Phase 1 artifacts before any generation begins.

#### Table 1A — Challenge Framework

| ID | Test | Pass Threshold | Phase 7 Column Schema | Survival Condition |
|----|------|----------------|-----------------------|--------------------|
| T-1 | Differentiation | Meaningfully distinct mechanism from every other `**` candidate | "T-1: Differentiation" | Removing this candidate eliminates an approach not covered by remaining 4 |
| T-2 | Topic Fit | Rationale names a specific dimension of `{{topic}}` — not generic | "T-2: Topic Fit" | Rationale fails if topic is swapped out |
| T-3 | Inertia Displacement | PASS on ≥3 of 5 anchor fields evaluated independently | **Five columns:** "T-3: Costs" / "T-3: Benefits" / "T-3: Competitive Threshold" / "T-3: Bypasses" / "T-3: Preserves" — exact labels locked | ≥3 PASS cells across 5 anchor-named T-3 columns |
| T-4 | Category Coverage | Candidate's category absent from other 4 `**` picks | "T-4: Category Coverage" | Removing this pick collapses top-5 below 3 categories |

Survival: all 4 tests PASS. T-3 schema LOCKED at Phase 1 exit — deviation is BREACH-MAJOR. Framework LOCKED — modification is BREACH-FATAL.

#### Table 1B — Ledger Contract (Blueprint + Taxonomy fused; per-row correction authority)

| Phase | Phase Name | Ledger Field | Violation Condition | BREACH Tier | Correction Action | Continue? |
|-------|-----------|--------------|---------------------|-------------|-------------------|-----------|
| 3 | Architecture | AMEND Source + Primary Challenge Test cols on every row | Any row missing either column | BREACH-MAJOR | Halt. Add col. Repopulate. | NO |
| 4 | Do Nothing Anchor | Challenge Binding col on every anchor row | Any row missing Challenge Binding | BREACH-MAJOR | Halt. Add col. Correct rows. | NO |
| 5 | Diverge | Name + Pitch on every candidate row | Missing Name or Pitch | BREACH-MINOR | Correct in-place. | YES |
| 6 | Cluster T-Evidence | T-Evidence col with `T-1:[v]·T-2:[v]·T-3:[dims]·T-4:[v]` on every row | Col absent; >1/3 unstructured | BREACH-MAJOR if absent; BREACH-MINOR if <1/3 | Col absent: halt, add, repopulate. | Col absent: NO |
| 6 | Cluster Anchor Citation | Anchor Citation col; every row cites ≥1 anchor field label | Col absent; >1/3 rows blank | BREACH-MAJOR if col absent; BREACH-MINOR if <1/3 blank | Col absent: halt, add, repopulate. Blank: rewrite Rationale, add citation. | Col absent: NO |
| 7 | Adversarial Challenge | Ph6 Pre-Score col + Ph6 Anchor Citation col + T-3 via 5 locked cols | Missing either carryforward col; merged T-3 | BREACH-FATAL if `**` pre-assigned; BREACH-MAJOR for schema | Discard Phase 7+, restart / halt, reconstruct. | NO |

#### Table 1C — BREACH Severity Taxonomy

| Severity | Definition | Correction Protocol | Continue? |
|----------|------------|---------------------|-----------|
| BREACH-MINOR | Recommended field absent; <1/3 rows missing; overlapping AMEND directions; anchor citation missing from <1/3 rationales | Correct in-place; mark `[corrected]` | YES |
| BREACH-MAJOR | Required ledger column absent; concentration cap exceeded; count outside 20–40; T-3 schema deviated; Anchor Citation col absent | HALT; reconstruct affected table; re-verify | NO |
| BREACH-FATAL | Candidates before Phase 1; `**` before Phase 7; anchor absent; framework modified after lock | STOP; discard; restart | NO |

Exit Phase 1:
- [ ] Table 1A: T-1 through T-4; T-3 names all 5 labels — BREACH-FATAL if absent
- [ ] Table 1B: 6 obligation rows (2 rows for Phase 6); BREACH Tier + Correction Action + Continue? cols populated — BREACH-MAJOR if any col absent
- [ ] Table 1C: all 3 tiers with correction protocols — BREACH-MAJOR if any tier missing
Ledger obligation satisfied: Phase 1 artifacts declared.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — AMEND ADJUSTMENTS
Entry: Phase 1 exit gates passed. Table 1A locked; Table 1B populated.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write exactly 3 pool-shaping adjustments before architecture or candidates are generated.

| # | Dimension | Direction | Downstream Effect on Pool |
|---|-----------|-----------|--------------------------|
| A1 | | | |
| A2 | | | |
| A3 | | | |

Rules: Dimension is a specific axis; Directions non-overlapping; Downstream Effects `{{topic}}`-specific.

Exit Phase 2:
- [ ] Exactly 3 rows; all columns filled — BREACH-MINOR if any col blank
- [ ] Directions distinct — BREACH-MINOR if duplicate
- [ ] Effects `{{topic}}`-specific — BREACH-MINOR if generic
Ledger obligation satisfied: AMEND adjustments declared.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3 — ARCHITECTURE DECLARATION
Entry: Phase 2 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Category | Description | Target Count | % of Pool | AMEND Source | Primary Challenge Test |
|----------|-------------|--------------|-----------|--------------|------------------------|

Total: ______

Rules: ≥4 categories; largest ≤40%; totals 20–40; AMEND Source + Primary Challenge Test on every row; ≥1 row T-3. Largest ≥40% — redistribute before exit (BREACH-MAJOR).

Exit Phase 3:
- [ ] ≥4 categories; % computed; no category ≥40% — BREACH-MAJOR
- [ ] AMEND Source col present; all rows populated — BREACH-MAJOR
- [ ] Primary Challenge Test col; ≥1 row T-3 — BREACH-MAJOR
- [ ] Total 20–40 — BREACH-MAJOR
Ledger obligation satisfied: Architecture table carries AMEND Source and Primary Challenge Test.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — DO NOTHING ANCHOR
Entry: Phase 3 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write the status quo anchor grounded in Phase 3 architecture. Bypasses + Preserves must reference specific Phase 3 category labels.

| Field | Content | Challenge Binding |
|-------|---------|-------------------|
| Costs | | T-3 |
| Benefits | | T-3 |
| Competitive Threshold | | T-3 |
| Bypasses | [name ≥1 Phase 3 category label] | T-3 |
| Preserves | | T-3 |
| Net Position | [integrated judgment + displacement condition] | T-3 synthesis |

Pre-commitment for Phase 6: Every candidate's Rationale must cite ≥1 anchor field by its exact label from this table (e.g., "displaces Costs by...", "addresses Bypasses dimension..."). This citation becomes the Anchor Citation column entry. Rationales with no anchor field citation: Anchor Citation = BLANK, which triggers BREACH-MINOR per Table 1B Phase 6 row if >1/3 of rows blank.

Exit Phase 4:
- [ ] All 6 field rows with `{{topic}}`-specific content — BREACH-MAJOR if any absent
- [ ] Challenge Binding col present; all rows populated — BREACH-MAJOR
- [ ] Costs AND Benefits both present — BREACH-MINOR if costs-only
- [ ] Bypasses + Preserves name Phase 3 labels — BREACH-MINOR if generic
- [ ] Net Position names displacement condition — BREACH-MINOR if not
Ledger obligation satisfied: Anchor table (6 fields) with Challenge Binding on every row.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5 — DIVERGE (Name + Pitch Only)
Entry: Phase 4 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Generate 22–38 Name+Pitch pairs only. No categories, rationales, anchor citations, T-Evidence. No `**` marks — BREACH-FATAL.

| # | Name | Pitch (one line) |
|---|------|-----------------|

Exit Phase 5:
- [ ] 20–40 candidates; Name + Pitch only — BREACH-MAJOR if outside range
- [ ] No categories, rationales, or `**` assigned — BREACH-MINOR if present
Ledger obligation satisfied: Diverge list produced.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6 — CLUSTER + T-EVIDENCE + ANCHOR CITATION
Entry: Phase 5 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Assign Category, Rationale, T-Evidence, and Anchor Citation to every candidate. The Anchor Citation column is a SEPARATE column from T-Evidence — it records the specific anchor field labels cited in the Rationale, not a challenge-readiness verdict.

| # | Name | Category | Rationale | Anchor Citation | T-Evidence |
|---|------|----------|-----------|-----------------|------------|

**Anchor Citation format**: list the specific anchor field labels from Phase 4 that the Rationale explicitly cites by name (e.g., "Costs", "Bypasses + Competitive Threshold", "Net Position"). Use Phase 4 field labels exactly. If the Rationale makes no anchor field displacement claim — rewrite the Rationale to establish at least one anchor reference before entering the Anchor Citation. Blank Anchor Citation is permitted only if the Rationale genuinely cannot reference any anchor dimension (mark "N/A — structural"); >1/3 blank triggers BREACH-MINOR per Table 1B.

**T-Evidence format**: `T-1:[PASS/PARTIAL/FAIL]·T-2:[PASS/PARTIAL/FAIL]·T-3:[dims cleared]·T-4:[PASS/PARTIAL/FAIL]`
T-3 dims cleared: list anchor field labels where Rationale demonstrates superiority (e.g., "Costs+Bypasses"). This is derived from Anchor Citation but records the verdict level, not just the citation.

Concentration inline check: if any category reaches 40% of total rows — redistribute before continuing (BREACH-MAJOR).

Exit Phase 6:
- [ ] All 4 anatomy fields + Anchor Citation + T-Evidence on every candidate — BREACH-MAJOR if Anchor Citation col absent
- [ ] Anchor Citation col: ≤1/3 rows blank — BREACH-MINOR if between 1/3 and 1/2; BREACH-MAJOR if col absent
- [ ] T-Evidence col: structured notation on every row — apply Table 1B Phase 6 T-Evidence row
- [ ] No category ≥40% — BREACH-MAJOR
- [ ] Rationales `{{topic}}`-specific — BREACH-MINOR if >1/5 generic
Ledger obligation satisfied: Cluster table with T-Evidence AND Anchor Citation on every row.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — ADVERSARIAL CHALLENGE
Entry: Phase 6 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Challenge every candidate. Load Ph6 Pre-Score and Ph6 Anchor Citation from Phase 6 before evaluating. Do not mark `**` yet — BREACH-FATAL if assigned.

Column schema (mandatory):
`| # | Name | Ph6 Pre-Score | Ph6 Anchor Citation | T-1: Differentiation | T-2: Topic Fit | T-3: Costs | T-3: Benefits | T-3: Competitive Threshold | T-3: Bypasses | T-3: Preserves | T-4: Category Coverage | Verdict |`

- **Ph6 Pre-Score**: copy T-Evidence from Phase 6 verbatim
- **Ph6 Anchor Citation**: copy Anchor Citation from Phase 6 verbatim
- **T-3 columns**: five separate columns using exact Phase 4 field labels (merged column: BREACH-MAJOR)
- T-3 evaluation: for each anchor-named column, check Ph6 Anchor Citation first — if the label appears, adjudicate whether the Rationale demonstrates superiority; if absent from Ph6 Anchor Citation, evaluate Rationale text for implicit support
- T-3 PASS threshold: ≥3 PASS cells across 5 columns

Exit Phase 7:
- [ ] Ph6 Pre-Score col present and populated from Phase 6 — BREACH-MAJOR if absent
- [ ] Ph6 Anchor Citation col present and populated from Phase 6 — BREACH-MAJOR if absent
- [ ] T-3 via 5 separate anchor-named cols using locked labels — BREACH-MAJOR if merged
- [ ] No `**` marks assigned — BREACH-FATAL if present

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 8 — MARK + FINALIZE
Entry: Phase 7 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Select top 5 from Phase 7 verdicts. Apply `**` to exactly 5 entries in Phase 6 cluster table. Top-5 set must span ≥3 categories. Removing any one must lose a distinct angle.

Exit Phase 8:
- [ ] Exactly 5 `**` marks applied — BREACH-FATAL
- [ ] `**` set spans ≥3 categories — BREACH-MAJOR
Ledger obligation satisfied: `**` marks assigned.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9A — TERMINAL LEDGER AUDIT (Reconstruct → Assess)
Entry: Phase 8 complete.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Phase 9B may not begin until Phase 9A is complete and all ledger rows are COMPLETE.

**RECONSTRUCT PASS** — Describe what each contributing phase concretely produced in this execution:

| Phase | Obligation | What Was Actually Produced | COMPLETE? |
|-------|-----------|---------------------------|-----------|
| Phase 3 | AMEND Source + Primary Challenge Test cols | [col names present; row count] | Y/N |
| Phase 4 | Challenge Binding col on anchor table | [col present; rows mapped] | Y/N |
| Phase 5 | Name + Pitch on every candidate | [row count; any blanks] | Y/N |
| Phase 6 T-Evidence | T-Evidence structured notation | [notation format; blank row count] | Y/N |
| Phase 6 Anchor Citation | Anchor Citation col | [col present; labels used; blank row count; cite 3 example entries] | Y/N |
| Phase 7 | Ph6 Pre-Score col + Ph6 Anchor Citation col + T-3 cols | **T-3 column headers observed: [enumerate each T-3-prefixed header exactly]** Expected: T-3: Costs / T-3: Benefits / T-3: Competitive Threshold / T-3: Bypasses / T-3: Preserves. Match per header: [MATCH/MISMATCH]. C-27 verdict: PASS/PARTIAL/FAIL. Ph6 Anchor Citation col present: Y/N | Y/N |

**ASSESS PASS**:

| Ledger Row | Status | Declared Severity | Action |
|-----------|--------|-------------------|--------|
| Phase 3 architecture | | | |
| Phase 4 anchor | | | |
| Phase 5 diverge | | | |
| Phase 6 T-Evidence | | | |
| Phase 6 Anchor Citation | | | |
| Phase 7 challenge | | | |

Correct all VIOLATION rows before Phase 9B.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9B — CRITERION CHECKLIST
Entry: Phase 9A complete — all 6 ledger rows COMPLETE.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Row | Criterion | Status | Severity if FAIL |
|-----|-----------|--------|-----------------|
| 1–16 | [same as V-01 rows 1–16] | | |
| 17 | Phase 6 Anchor Citation col present; every candidate cites ≥1 anchor field | PASS/FAIL | BREACH-MAJOR if col absent; BREACH-MINOR if <1/3 blank |
| 18 | Phase 7 Ph6 Anchor Citation col present; populated from Phase 6 | PASS/FAIL | BREACH-MAJOR |

Apply Table 1C protocol for every FAIL before writing artifact.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WRITE — ARTIFACT ASSEMBLY
Entry: Phase 9B complete.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

Structure: Title → AMEND (A1/A2/A3) → Do Nothing (costs, benefits, net position) → Category sections with candidates grouped; `**` on top-5; each entry: Name — Pitch — Rationale.
```

---

## V-03 — Single-axis: C-43 Anchor-Forward Scaffolding (Phase 4 Label Reference)

**Variation axis:** Inertia framing — Phase 4 produces a dedicated "Anchor Field Label Reference" sub-artifact that Phase 6 must load as its first step before assigning any row. The reference table pre-formats the exact label strings Phase 6 must use in the Anchor Citation column. An inline conditional inside Phase 6's row-writing instruction rewrites any Rationale that would produce a blank citation before the Anchor Citation cell is entered.

**Hypothesis:** V-02 declares the Anchor Citation obligation in Table 1B and instructs Phase 6 to cite anchor field labels — but the citation vocabulary is implicit (the model must recall Phase 4 field names). When the Rationale is being written for the 25th candidate, the anchor field labels may have drifted from Phase 4's exact strings. A Phase 4 Label Reference sub-artifact — a small named table containing the exact label strings — functions as a citation vocabulary that Phase 6 loads explicitly, making label drift detectable by column structure. The inline conditional further ensures that zero-citation Rationales are caught and corrected at write time, not at Phase 9A audit time.

---

```
You are generating a brainstorm artifact for the topic: `{{topic}}`
Output date: `{{date}}`
Artifact path: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 1 — CHALLENGE FRAMEWORK + LEDGER CONTRACT + BREACH TAXONOMY
Entry: Start of session.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### Table 1A — Challenge Framework

| ID | Test | Pass Threshold | Phase 7 Column Schema | Survival Condition |
|----|------|----------------|-----------------------|--------------------|
| T-1 | Differentiation | Meaningfully distinct mechanism from every other `**` candidate | "T-1: Differentiation" | Removing this candidate eliminates an approach not covered by remaining 4 |
| T-2 | Topic Fit | Rationale names a specific dimension of `{{topic}}` | "T-2: Topic Fit" | Rationale fails if topic is swapped out |
| T-3 | Inertia Displacement | PASS on ≥3 of 5 anchor fields independently | **Five columns:** "T-3: Costs" / "T-3: Benefits" / "T-3: Competitive Threshold" / "T-3: Bypasses" / "T-3: Preserves" — labels locked | ≥3 PASS cells across 5 anchor-named T-3 columns |
| T-4 | Category Coverage | Candidate's category absent from other 4 `**` picks | "T-4: Category Coverage" | Removing this collapses top-5 below 3 categories |

T-3 schema LOCKED at Phase 1 exit. Framework LOCKED — modification is BREACH-FATAL.

#### Table 1B — Ledger Contract (per-row correction authority)

| Phase | Phase Name | Ledger Field | Violation Condition | BREACH Tier | Correction | Continue? |
|-------|-----------|--------------|---------------------|-------------|------------|-----------|
| 3 | Architecture | AMEND Source + Primary Challenge Test cols | Any row missing either col | BREACH-MAJOR | Halt; add col; repopulate | NO |
| 4 | Do Nothing Anchor | Challenge Binding col + Anchor Field Label Reference sub-artifact | Challenge Binding absent; Label Reference not produced | BREACH-MAJOR | Halt; add col; produce reference | NO |
| 5 | Diverge | Name + Pitch on every row | Missing Name or Pitch | BREACH-MINOR | Correct in-place | YES |
| 6 | Cluster T-Evidence | T-Evidence `T-1:[v]·T-2:[v]·T-3:[dims]·T-4:[v]` on every row | Col absent; >1/3 unstructured | BREACH-MAJOR if absent | Col absent: halt, add, repopulate | NO |
| 6 | Cluster Anchor Citation | Anchor Citation col; labels match Phase 4 Reference exactly | Col absent; >1/3 blank; label strings deviate from Reference | BREACH-MAJOR if col absent; BREACH-MINOR if <1/3 blank or label drift | Col absent: halt, add, repopulate. Blank: trigger inline rewrite. | NO if absent |
| 7 | Adversarial Challenge | Ph6 Pre-Score + Ph6 Anchor Citation cols + T-3 via 5 locked cols | Missing carryforward col; merged T-3 | BREACH-FATAL if `**` pre-assigned; BREACH-MAJOR schema | Discard/restart or halt/reconstruct | NO |

#### Table 1C — BREACH Taxonomy

| Severity | Definition | Correction | Continue? |
|----------|------------|------------|-----------|
| BREACH-MINOR | Recommended field absent; <1/3 rows missing; overlapping AMEND; label drift in <1/3 citations | Correct in-place; mark `[corrected]` | YES |
| BREACH-MAJOR | Required col absent; cap exceeded; count outside 20–40; T-3 schema deviated; Anchor Citation col absent | HALT; reconstruct; re-verify | NO |
| BREACH-FATAL | Candidates before Phase 1; `**` before Phase 7; anchor absent; framework modified | STOP; discard; restart | NO |

Exit Phase 1:
- [ ] Table 1A: T-3 names all 5 labels — BREACH-FATAL if absent
- [ ] Table 1B: 6 rows (2 for Phase 6); BREACH Tier + Correction + Continue? cols populated — BREACH-MAJOR if absent
- [ ] Table 1C: all 3 tiers — BREACH-MAJOR if any missing

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — AMEND ADJUSTMENTS
Entry: Phase 1 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| # | Dimension | Direction | Downstream Effect on Pool |
|---|-----------|-----------|--------------------------|
| A1 | | | |
| A2 | | | |
| A3 | | | |

Rules: non-overlapping directions; effects `{{topic}}`-specific.

Exit Phase 2:
- [ ] 3 rows; all cols filled — BREACH-MINOR if any blank
- [ ] Directions distinct — BREACH-MINOR if duplicate
- [ ] Effects `{{topic}}`-specific — BREACH-MINOR if generic

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3 — ARCHITECTURE DECLARATION
Entry: Phase 2 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Category | Description | Target Count | % of Pool | AMEND Source | Primary Challenge Test |
|----------|-------------|--------------|-----------|--------------|------------------------|

Total: ______

Rules: ≥4 categories; largest ≤40%; totals 20–40; AMEND Source + Primary Challenge Test on every row; ≥1 row T-3.

Exit Phase 3:
- [ ] ≥4 categories; % computed; no category ≥40% — BREACH-MAJOR
- [ ] AMEND Source col populated on every row — BREACH-MAJOR
- [ ] Primary Challenge Test col; ≥1 row T-3 — BREACH-MAJOR
- [ ] Total 20–40 — BREACH-MAJOR

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — DO NOTHING ANCHOR + ANCHOR FIELD LABEL REFERENCE
Entry: Phase 3 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 4A — Write the Do Nothing anchor grounded in Phase 3 architecture:

| Field | Content | Challenge Binding |
|-------|---------|-------------------|
| Costs | | T-3 |
| Benefits | | T-3 |
| Competitive Threshold | [reference ≥1 Phase 3 category] | T-3 |
| Bypasses | [name ≥1 Phase 3 category label] | T-3 |
| Preserves | | T-3 |
| Net Position | [integrated judgment; name displacement condition] | T-3 synthesis |

Step 4B — Produce the Anchor Field Label Reference sub-artifact. This is the citation vocabulary for Phase 6's Anchor Citation column. Use these EXACT label strings — no paraphrasing:

```
ANCHOR FIELD LABEL REFERENCE (cite these strings verbatim in Phase 6 Anchor Citation column):
  Label 1: Costs
  Label 2: Benefits
  Label 3: Competitive Threshold
  Label 4: Bypasses
  Label 5: Preserves
  Label 6: Net Position
```

This reference is a Phase 4 ledger artifact. Phase 6 must load it before assigning any row.

Exit Phase 4:
- [ ] All 6 anchor field rows with `{{topic}}`-specific content — BREACH-MAJOR if any absent
- [ ] Challenge Binding col present; all rows populated — BREACH-MAJOR
- [ ] Anchor Field Label Reference produced with all 6 labels listed — BREACH-MAJOR if absent
- [ ] Costs AND Benefits both present — BREACH-MINOR
- [ ] Net Position names displacement condition — BREACH-MINOR
Ledger obligation satisfied: Anchor table + Anchor Field Label Reference declared.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5 — DIVERGE (Name + Pitch Only)
Entry: Phase 4 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Generate 22–38 Name+Pitch pairs only. No categories, rationales, anchor citations, T-Evidence. No `**` — BREACH-FATAL.

| # | Name | Pitch (one line) |
|---|------|-----------------|

Exit Phase 5:
- [ ] 20–40 candidates; Name + Pitch only — BREACH-MAJOR

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6 — CLUSTER + T-EVIDENCE + ANCHOR CITATION
Entry: Phase 5 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Step 6-0: Load Anchor Field Label Reference from Phase 4.** The 6 labels available for Anchor Citation column are: Costs | Benefits | Competitive Threshold | Bypasses | Preserves | Net Position. Use these exact strings. Label drift (e.g., "competitive threshold" lowercase, "bypass" instead of "Bypasses") is BREACH-MINOR — correct to match Phase 4 reference exactly.

Assign Category, Rationale, Anchor Citation, and T-Evidence to every candidate.

| # | Name | Category | Rationale | Anchor Citation | T-Evidence |
|---|------|----------|-----------|-----------------|------------|

**Row-writing instruction**: For each candidate:
1. Write the Rationale (topic-specific; name the specific mechanism for `{{topic}}`)
2. Scan the Rationale for explicit references to anchor field labels. Ask: which of {Costs, Benefits, Competitive Threshold, Bypasses, Preserves, Net Position} does this Rationale name or address?
3. **Inline conditional**: if the answer is "none" — the Rationale is not grounded in the anchor. Rewrite to add one anchor displacement claim (e.g., "reduces the ongoing Costs of...") before entering the Anchor Citation. Do not leave Anchor Citation blank if the candidate can plausibly address any anchor field.
4. Enter Anchor Citation using exact label strings from the Phase 4 Reference. If multiple labels apply, join with " + " (e.g., "Costs + Bypasses").
5. Derive T-Evidence from Rationale and Anchor Citation. T-3 dims cleared = anchor field labels where Rationale demonstrates superiority.

Concentration check: if any category reaches 40% — redistribute before continuing (BREACH-MAJOR).

Exit Phase 6:
- [ ] Anchor Citation col present; uses Phase 4 Reference label strings — BREACH-MAJOR if col absent
- [ ] ≤1/3 rows have blank Anchor Citation — BREACH-MINOR if between 1/3 and 1/2; BREACH-MAJOR col absent
- [ ] Label strings match Phase 4 Reference exactly — BREACH-MINOR for label drift in <1/3 rows
- [ ] T-Evidence structured notation on every row — BREACH-MAJOR if col absent
- [ ] No category ≥40% — BREACH-MAJOR
Ledger obligation satisfied: Cluster table with Anchor Citation (Phase 4 Reference labels) and T-Evidence.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — ADVERSARIAL CHALLENGE
Entry: Phase 6 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Load Phase 6 Anchor Citation and T-Evidence before evaluating. Do not mark `**` — BREACH-FATAL.

Column schema:
`| # | Name | Ph6 Pre-Score | Ph6 Anchor Citation | T-1: Differentiation | T-2: Topic Fit | T-3: Costs | T-3: Benefits | T-3: Competitive Threshold | T-3: Bypasses | T-3: Preserves | T-4: Category Coverage | Verdict |`

- **Ph6 Pre-Score**: copy T-Evidence from Phase 6 verbatim
- **Ph6 Anchor Citation**: copy Anchor Citation from Phase 6 verbatim
- **T-3 columns**: five separate columns; for each, check Ph6 Anchor Citation first — if the label appears, adjudicate; if absent, assess Rationale for implicit evidence
- T-3 PASS threshold: ≥3 PASS cells

Exit Phase 7:
- [ ] Ph6 Pre-Score col present and populated — BREACH-MAJOR
- [ ] Ph6 Anchor Citation col present and populated — BREACH-MAJOR
- [ ] T-3 via 5 separate locked cols — BREACH-MAJOR if merged or label drift
- [ ] No `**` — BREACH-FATAL

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 8 — MARK + FINALIZE
Entry: Phase 7 exit gates passed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Select top 5. Apply `**` to exactly 5 entries in Phase 6 cluster table. Top-5 must span ≥3 categories.

Exit Phase 8:
- [ ] Exactly 5 `**` — BREACH-FATAL
- [ ] ≥3 categories — BREACH-MAJOR

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9A — TERMINAL LEDGER AUDIT (Reconstruct → Assess)
Entry: Phase 8 complete.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Phase 9B may not begin until Phase 9A complete and all ledger rows COMPLETE.

**RECONSTRUCT PASS**:

| Phase | Obligation | What Was Actually Produced | COMPLETE? |
|-------|-----------|---------------------------|-----------|
| Phase 3 | AMEND Source + Primary Challenge Test cols | [col names; row count] | Y/N |
| Phase 4 | Challenge Binding col + Label Reference | [col present; Reference produced: list the 6 labels as they appear] | Y/N |
| Phase 5 | Name + Pitch | [row count; blanks] | Y/N |
| Phase 6 T-Evidence | Structured notation | [format; blank count] | Y/N |
| Phase 6 Anchor Citation | Anchor Citation col; Phase 4 Reference labels | [col present; label strings used — cite 3 examples; label drift detected: Y/N; blank count] | Y/N |
| Phase 7 | Ph6 Pre-Score + Ph6 Anchor Citation + T-3 cols | **T-3 headers observed: [enumerate each exactly]** Expected: T-3: Costs / T-3: Benefits / T-3: Competitive Threshold / T-3: Bypasses / T-3: Preserves. Match per header: [MATCH/MISMATCH]. C-27 verdict. | Y/N |

**ASSESS PASS**:

| Ledger Row | Status | Declared Severity | Action |
|-----------|--------|-------------------|--------|
| Phase 3 architecture | | | |
| Phase 4 anchor + Label Reference | | | |
| Phase 5 diverge | | | |
| Phase 6 T-Evidence | | | |
| Phase 6 Anchor Citation | | | |
| Phase 7 challenge | | | |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9B — CRITERION CHECKLIST
Entry: Phase 9A complete — all 6 ledger rows COMPLETE.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Rows 1–16 as in V-01; plus:]

| 17 | Phase 4 Anchor Field Label Reference produced with all 6 labels | PASS/FAIL | BREACH-MAJOR |
| 18 | Phase 6 Anchor Citation col present; labels match Phase 4 Reference strings | PASS/FAIL | BREACH-MAJOR if absent; BREACH-MINOR if label drift |
| 19 | Phase 7 Ph6 Anchor Citation col present; populated from Phase 6 | PASS/FAIL | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WRITE — ARTIFACT ASSEMBLY
Entry: Phase 9B complete.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

Structure: Title → AMEND (A1/A2/A3) → Do Nothing (costs, benefits, net position) → Category sections; `**` on top-5; each entry: Name — Pitch — Rationale.
```

---

## V-04 — Combined: C-43 + C-44 (Artifact-Specific ENTRY TABLEs + Anchor Citation Ledger Obligation)

**Variation axes:** C-44 (artifact-specific ENTRY TABLEs at every phase) combined with C-43 (Anchor Citation as a Table 1B ledger obligation with BREACH-MAJOR tier). Both improvements applied simultaneously. V-01 establishes C-44; V-02 establishes C-43; V-04 tests whether they compose cleanly without introducing conflicting complexity.

**Hypothesis:** C-43 and C-44 operate on different phase boundaries: C-43 adds a Phase 6 column obligation and a Phase 7 carryforward column; C-44 upgrades the entry/exit gate schema at every phase. There is no structural conflict — C-44 makes the ENTRY TABLE for Phase 6 name the "Phase 5 Diverge List" and "Phase 4 Anchor Field Label Reference" as specific predecessor artifacts, and C-43 makes the Phase 6 EXIT TABLE include an "Anchor Citation col present" departure condition. When both are active, every phase boundary is doubly specific: the ENTRY TABLE names the artifacts that must exist, and the EXIT TABLE confirms the artifacts that were produced. This creates an end-to-end traceability scaffold where Anchor Citation evidence is both required to be present (C-43) and required to be named as a ENTRY TABLE prerequisite at Phase 7 (C-44).

---

```
You are generating a brainstorm artifact for the topic: `{{topic}}`
Output date: `{{date}}`
Artifact path: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 1 — CHALLENGE FRAMEWORK + LEDGER CONTRACT + BREACH TAXONOMY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 1
| Predecessor Artifact | Source | Required State |
|---------------------|--------|----------------|
| (session root — no predecessor) | — | — |

#### Table 1A — Challenge Framework

| ID | Test | Pass Threshold | Phase 7 Column Schema | Survival Condition |
|----|------|----------------|-----------------------|--------------------|
| T-1 | Differentiation | Meaningfully distinct mechanism from every other `**` candidate | "T-1: Differentiation" | Removing this eliminates an approach not covered by remaining 4 |
| T-2 | Topic Fit | Rationale names a specific dimension of `{{topic}}` — not generic | "T-2: Topic Fit" | Rationale fails if topic swapped |
| T-3 | Inertia Displacement | PASS on ≥3 of 5 anchor fields independently | **Five columns:** "T-3: Costs" / "T-3: Benefits" / "T-3: Competitive Threshold" / "T-3: Bypasses" / "T-3: Preserves" — exact labels locked | ≥3 PASS cells across 5 anchor-named T-3 columns |
| T-4 | Category Coverage | Candidate's category absent from other 4 `**` picks | "T-4: Category Coverage" | Removing collapses top-5 below 3 categories |

T-3 schema LOCKED at Phase 1 exit — deviation BREACH-MAJOR. Framework LOCKED — modification BREACH-FATAL.

#### Table 1B — Ledger Contract (Blueprint + Taxonomy fused)

| Phase | Phase Name | Ledger Field | Violation Condition | BREACH Tier | Correction | Continue? |
|-------|-----------|--------------|---------------------|-------------|------------|-----------|
| 3 | Architecture | AMEND Source + Primary Challenge Test cols on every row | Any row missing either col | BREACH-MAJOR | Halt; add col; repopulate | NO |
| 4 | Do Nothing Anchor | Challenge Binding col on every anchor row | Any row missing Challenge Binding | BREACH-MAJOR | Halt; add col; correct rows | NO |
| 5 | Diverge | Name + Pitch on every candidate row | Missing Name or Pitch | BREACH-MINOR | Correct in-place | YES |
| 6 | Cluster T-Evidence | T-Evidence `T-1:[v]·T-2:[v]·T-3:[dims]·T-4:[v]` on every row | Col absent; >1/3 unstructured | BREACH-MAJOR if col absent | Halt; add col; repopulate | NO |
| 6 | Cluster Anchor Citation | Anchor Citation col; every row cites ≥1 anchor field label from Phase 4 | Col absent; >1/3 blank | BREACH-MAJOR if col absent; BREACH-MINOR if <1/3 blank | Col absent: halt, add, repopulate. Blank: rewrite Rationale inline. | NO if absent |
| 7 | Adversarial Challenge | Ph6 Pre-Score + Ph6 Anchor Citation cols + T-3 via 5 locked cols | Missing carryforward col; merged T-3 | BREACH-FATAL if `**` pre-assigned; BREACH-MAJOR schema | Discard+restart or halt+reconstruct | NO |

#### Table 1C — BREACH Taxonomy

| Severity | Definition | Correction | Continue? |
|----------|------------|------------|-----------|
| BREACH-MINOR | Recommended field absent; <1/3 rows missing; overlapping AMEND directions | Correct in-place; mark `[corrected]` | YES |
| BREACH-MAJOR | Required col absent; concentration cap exceeded; count outside 20–40; T-3 schema deviated; Anchor Citation col absent | HALT; reconstruct; re-verify | NO |
| BREACH-FATAL | Candidates before Phase 1; `**` before Phase 7; anchor absent; framework modified after lock | STOP; discard; restart | NO |

EXIT TABLE — Phase 1
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Table 1A: T-1/T-2/T-3/T-4 with Phase 7 schema; T-3 names all 5 labels | BREACH-FATAL |
| Table 1B: 6 obligation rows; BREACH Tier + Correction + Continue? cols populated | BREACH-MAJOR |
| Table 1C: all 3 tiers | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — AMEND ADJUSTMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 2
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Table 1A (Challenge Framework) | Phase 1 | T-1/T-2/T-3/T-4 declared; T-3 schema locked (5 column labels) |
| Table 1B (Ledger Contract) | Phase 1 | 6 obligation rows; BREACH Tier col populated |
| Table 1C (BREACH Taxonomy) | Phase 1 | 3 severity tiers with correction protocols |

Write exactly 3 pool-shaping adjustments.

| # | Dimension | Direction | Downstream Effect on Pool |
|---|-----------|-----------|--------------------------|
| A1 | | | |
| A2 | | | |
| A3 | | | |

Rules: non-overlapping directions; effects `{{topic}}`-specific.

EXIT TABLE — Phase 2
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Exactly 3 rows; all cols filled | BREACH-MINOR |
| Directions distinct | BREACH-MINOR |
| Effects `{{topic}}`-specific | BREACH-MINOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3 — ARCHITECTURE DECLARATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 3
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| AMEND Adjustments Table (A1/A2/A3) | Phase 2 | 3 rows; Dimension + Direction + Downstream Effect filled |

| Category | Description | Target Count | % of Pool | AMEND Source | Primary Challenge Test |
|----------|-------------|--------------|-----------|--------------|------------------------|

Total: ______

Rules: ≥4 categories; largest ≤40%; totals 20–40; AMEND Source + Primary Challenge Test on every row; ≥1 row T-3. Largest ≥40% — redistribute before exit (BREACH-MAJOR).

EXIT TABLE — Phase 3
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| ≥4 categories; % computed; no category ≥40% | BREACH-MAJOR |
| AMEND Source col; all rows populated | BREACH-MAJOR |
| Primary Challenge Test col; ≥1 row T-3 | BREACH-MAJOR |
| Total 20–40 | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — DO NOTHING ANCHOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 4
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Category Architecture Table | Phase 3 | ≥4 categories; AMEND Source + Primary Challenge Test cols; ≥1 T-3 row; ≤40% cap |
| AMEND Adjustments Table (A1/A2/A3) | Phase 2 | 3 rows with Dimension + Direction + Downstream Effect |

Write the Do Nothing anchor grounded in Phase 3 architecture. Bypasses + Preserves must name specific Phase 3 category labels.

| Field | Content | Challenge Binding |
|-------|---------|-------------------|
| Costs | | T-3 |
| Benefits | | T-3 |
| Competitive Threshold | [reference ≥1 Phase 3 category] | T-3 |
| Bypasses | [name ≥1 Phase 3 category label] | T-3 |
| Preserves | | T-3 |
| Net Position | [integrated judgment; displacement condition] | T-3 synthesis |

Rules: Costs AND Benefits both present (BREACH-MINOR if costs-only); Bypasses + Preserves name Phase 3 labels (BREACH-MINOR if generic); Net Position names displacement condition; Challenge Binding col present (BREACH-MAJOR if absent).

EXIT TABLE — Phase 4
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| All 6 field rows with `{{topic}}`-specific content | BREACH-MAJOR |
| Challenge Binding col; all rows populated | BREACH-MAJOR |
| Costs AND Benefits both present | BREACH-MINOR |
| Bypasses + Preserves name Phase 3 labels | BREACH-MINOR |
| Net Position names displacement condition | BREACH-MINOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5 — DIVERGE (Name + Pitch Only)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 5
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Do Nothing Anchor Table (6 fields) | Phase 4 | Costs/Benefits/Competitive Threshold/Bypasses/Preserves/Net Position; Challenge Binding col present |
| Category Architecture Table | Phase 3 | Category labels and slot budgets |

Generate 22–38 Name+Pitch pairs only. No categories, rationales, anchor citations. No `**` — BREACH-FATAL.

| # | Name | Pitch (one line) |
|---|------|-----------------|

EXIT TABLE — Phase 5
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| 20–40 candidates; Name + Pitch only | BREACH-MAJOR |
| No categories, rationales, or `**` assigned | BREACH-MINOR if present |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6 — CLUSTER + T-EVIDENCE + ANCHOR CITATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 6
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Diverge List | Phase 5 | 20–40 Name+Pitch rows; no categories or rationales assigned |
| Category Architecture Table | Phase 3 | Category labels with slot budgets |
| Do Nothing Anchor Table (6 fields) | Phase 4 | 6 anchor field labels available: Costs, Benefits, Competitive Threshold, Bypasses, Preserves, Net Position |

Assign Category, Rationale, Anchor Citation, and T-Evidence to every candidate. These are 4 separate columns — do not merge Anchor Citation into T-Evidence.

| # | Name | Category | Rationale | Anchor Citation | T-Evidence |
|---|------|----------|-----------|-----------------|------------|

**Anchor Citation format**: list Phase 4 anchor field labels the Rationale explicitly cites (e.g., "Costs", "Bypasses + Competitive Threshold"). Inline conditional: if Rationale addresses no anchor field — rewrite to add one displacement claim before entering Anchor Citation (BREACH-MINOR per blank row; >1/3 blank triggers Table 1B Phase 6 Anchor Citation row).

**T-Evidence format**: `T-1:[PASS/PARTIAL/FAIL]·T-2:[PASS/PARTIAL/FAIL]·T-3:[dims cleared]·T-4:[PASS/PARTIAL/FAIL]`
T-3 dims cleared are derived from Anchor Citation (the fields cited that also demonstrate superiority).

Concentration inline check: any category at 40% — redistribute before continuing (BREACH-MAJOR).

EXIT TABLE — Phase 6
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Anchor Citation col present; ≤1/3 rows blank | BREACH-MAJOR if col absent; BREACH-MINOR if <1/3 blank |
| T-Evidence col; structured notation on every row | BREACH-MAJOR if col absent |
| No category ≥40% | BREACH-MAJOR |
| All candidates from Phase 5 present | BREACH-MAJOR |
| Rationales `{{topic}}`-specific | BREACH-MINOR if >1/5 generic |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — ADVERSARIAL CHALLENGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 7
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Cluster Table (with Anchor Citation + T-Evidence cols) | Phase 6 | Anchor Citation col present; T-Evidence col present; ≤1/3 rows blank in Anchor Citation |
| Do Nothing Anchor Table | Phase 4 | 6 fields; Challenge Binding col present |
| Table 1A (Challenge Framework + T-3 Schema) | Phase 1 | T-3 column schema locked: Costs/Benefits/Competitive Threshold/Bypasses/Preserves |

Challenge every candidate. Load Ph6 Pre-Score and Ph6 Anchor Citation from Phase 6 before evaluating. Do not mark `**` — BREACH-FATAL.

Column schema:
`| # | Name | Ph6 Pre-Score | Ph6 Anchor Citation | T-1: Differentiation | T-2: Topic Fit | T-3: Costs | T-3: Benefits | T-3: Competitive Threshold | T-3: Bypasses | T-3: Preserves | T-4: Category Coverage | Verdict |`

- **Ph6 Pre-Score**: copy T-Evidence from Phase 6 verbatim
- **Ph6 Anchor Citation**: copy Anchor Citation from Phase 6 verbatim
- **T-3 columns**: 5 separate locked cols; for each, Ph6 Anchor Citation is primary evidence — adjudicate pre-declared claims rather than forming new judgments
- T-3 PASS threshold: ≥3 PASS cells

EXIT TABLE — Phase 7
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Ph6 Pre-Score col present; populated from Phase 6 | BREACH-MAJOR |
| Ph6 Anchor Citation col present; populated from Phase 6 | BREACH-MAJOR |
| T-3 via 5 separate anchor-named cols; labels match Table 1A schema | BREACH-MAJOR if merged or label deviation |
| No `**` marks assigned | BREACH-FATAL if present |
| All candidates evaluated with Verdict | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 8 — MARK + FINALIZE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 8
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 7 Challenge Table | Phase 7 | All candidates evaluated; Ph6 Pre-Score + Ph6 Anchor Citation cols present; 5 T-3 anchor-named cols; no `**` marks |
| Table 1A (Survival Threshold) | Phase 1 | All 4 tests PASS required |

Apply `**` to exactly 5 entries in Phase 6 cluster table. Top-5 must span ≥3 categories; removing any one must lose a distinct angle.

EXIT TABLE — Phase 8
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Exactly 5 `**` marks applied | BREACH-FATAL |
| `**` set spans ≥3 categories | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9A — TERMINAL LEDGER AUDIT (Reconstruct → Assess)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 9A
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 8 Output (`**` marks applied to Cluster Table) | Phase 8 | Exactly 5 `**` marks |
| Phase 7 Challenge Table | Phase 7 | Ph6 Pre-Score + Ph6 Anchor Citation cols present; 5 T-3 cols |
| Phase 6 Cluster Table | Phase 6 | Anchor Citation + T-Evidence cols present |
| All contributing phases (3–7) | Phases 3–7 | Exit gates declared passed |

Phase 9B may not begin until Phase 9A complete and all ledger rows COMPLETE.

**RECONSTRUCT PASS**:

| Phase | Obligation | What Was Actually Produced | COMPLETE? |
|-------|-----------|---------------------------|-----------|
| Phase 3 | AMEND Source + Primary Challenge Test cols | [col names; row count] | Y/N |
| Phase 4 | Challenge Binding col | [col present; rows mapped] | Y/N |
| Phase 5 | Name + Pitch | [row count; blanks] | Y/N |
| Phase 6 T-Evidence | Structured notation | [format used; blank count] | Y/N |
| Phase 6 Anchor Citation | Anchor Citation col | [col present; anchor field labels used — 3 examples; blank count] | Y/N |
| Phase 7 | Ph6 Pre-Score + Ph6 Anchor Citation + T-3 cols | **T-3 headers observed: [enumerate each T-3-prefixed header exactly]** Expected: T-3: Costs / T-3: Benefits / T-3: Competitive Threshold / T-3: Bypasses / T-3: Preserves. Match per header: [MATCH/MISMATCH]. C-27 verdict. Ph6 Anchor Citation col present: Y/N | Y/N |

**ASSESS PASS**:

| Ledger Row | Status | Declared Severity | Action |
|-----------|--------|-------------------|--------|
| Phase 3 architecture | | | |
| Phase 4 anchor | | | |
| Phase 5 diverge | | | |
| Phase 6 T-Evidence | | | |
| Phase 6 Anchor Citation | | | |
| Phase 7 challenge | | | |

Correct all VIOLATION rows before Phase 9B.

EXIT TABLE — Phase 9A
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Reconstruct pass: one row per contributing phase (6 rows) | BREACH-MAJOR |
| T-3 headers enumerated for Phase 7 row; C-27 verdict rendered | BREACH-MAJOR |
| Assess pass: Declared Severity populated for all rows | BREACH-MAJOR |
| All 6 ledger rows COMPLETE | BREACH-FATAL |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9B — CRITERION CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 9B
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 9A Terminal Ledger Audit | Phase 9A | Reconstruct + Assess passes complete; all 6 ledger rows COMPLETE; C-27 verdict rendered |

| Row | Criterion | Status | Severity if FAIL |
|-----|-----------|--------|-----------------|
| 1 | Candidate count 20–40 (excl. Do Nothing) | PASS/FAIL | BREACH-MAJOR |
| 2 | Every candidate: Name + Pitch + Category + Rationale | PASS/FAIL | BREACH-MAJOR |
| 3 | Exactly 5 `**` marks | PASS/FAIL | BREACH-FATAL |
| 4 | Do Nothing: 6 fields incl. Net Position | PASS/FAIL | BREACH-MAJOR |
| 5 | AMEND: 3 adjustments; each names dimension + downstream effect | PASS/FAIL | BREACH-MINOR |
| 6 | Architecture: AMEND Source col; all rows populated | PASS/FAIL | BREACH-MAJOR |
| 7 | Architecture: Primary Challenge Test col; ≥1 row T-3 | PASS/FAIL | BREACH-MAJOR |
| 8 | Phase 6: T-Evidence structured notation | PASS/FAIL | BREACH-MAJOR |
| 9 | Phase 7: Ph6 Pre-Score carryforward col | PASS/FAIL | BREACH-MAJOR |
| 10 | `**` set spans ≥3 categories | PASS/FAIL | BREACH-MAJOR |
| 11 | Phase 4 anchor Challenge Binding col; Net Position maps to T-3 synthesis | PASS/FAIL | BREACH-MAJOR |
| 12 | Table 1C: all 3 BREACH tiers | PASS/FAIL | BREACH-FATAL |
| 13 | Phase 9A Declared Severity col populated | PASS/FAIL | BREACH-MAJOR |
| 14 | Phase 7 T-3 via 5 separate anchor-named cols | PASS/FAIL | BREACH-MAJOR |
| 15 | Table 1B carries BREACH Tier col; all rows populated | PASS/FAIL | BREACH-MAJOR |
| 16 | Phase 9A Reconstruct T-3 step complete; C-27 verdict rendered | PASS/FAIL | BREACH-MAJOR |
| 17 | Phase 6 Anchor Citation col present; ≤1/3 rows blank | PASS/FAIL | BREACH-MAJOR if absent; BREACH-MINOR if <1/3 blank |
| 18 | Phase 7 Ph6 Anchor Citation col present; populated from Phase 6 | PASS/FAIL | BREACH-MAJOR |

EXIT TABLE — Phase 9B
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| All 18 rows checked | BREACH-MINOR |
| All FAIL rows corrected | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WRITE — ARTIFACT ASSEMBLY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — WRITE
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 9B Criterion Checklist | Phase 9B | All 18 rows PASS or corrected |
| Cluster Table with `**` marks | Phase 8 | Exactly 5 `**` marks |
| AMEND Adjustments Table | Phase 2 | 3 adjustments |
| Do Nothing Anchor Table | Phase 4 | 6 fields |

Write to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

Structure: Title → AMEND (A1/A2/A3) → Do Nothing (costs, benefits, net position) → Category sections; `**` on top-5; each entry: Name — Pitch — Rationale.
```

---

## V-05 — Combined: C-43 + C-44 + Phase 7 Evidence Triage Reframe

**Variation axes:** C-44 (artifact-specific ENTRY TABLEs) combined with C-43 (Anchor Citation ledger obligation) and a Phase 7 structural reframe: Phase 7 is renamed "Evidence Triage" and structured as a carryforward-adjudication layer. Ph6 Anchor Citation is the first data column loaded, and the phase instruction explicitly states that T-3 evaluation adjudicates pre-declared displacement claims, not first-pass judgments. This directly operationalizes the rubric's C-43 pass condition language: "the anchor becomes a generative scaffold throughout pool formation, not a terminal comparator."

**Hypothesis:** V-04 adds both C-43 and C-44 but leaves Phase 7 as an "Adversarial Challenge" with the T-3 evaluation framed generically. The C-43 rubric states: "When C-43 is satisfied, Phase 7 T-3 evaluation adjudicates pre-declared displacement claims rather than forming first-pass judgments." This framing difference matters because it changes what the model does when it encounters a T-3 column: instead of evaluating "does this candidate beat the status quo on Costs?" it evaluates "the candidate pre-declared a Costs citation — does the Rationale's claim hold up?" The first is a judgment call; the second is an adjudication call. An adjudication call is lower variance because the evidence is already recorded. If the Anchor Citation column is populated with "Costs + Bypasses," the Phase 7 evaluation of T-3: Costs should be "this candidate cited Costs; does the Rationale's Costs claim demonstrate superiority?" — a structured verification, not an open question.

---

```
You are generating a brainstorm artifact for the topic: `{{topic}}`
Output date: `{{date}}`
Artifact path: simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 1 — CHALLENGE FRAMEWORK + LEDGER CONTRACT + BREACH TAXONOMY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 1
| Predecessor Artifact | Source | Required State |
|---------------------|--------|----------------|
| (session root — no predecessor) | — | — |

#### Table 1A — Challenge Framework

| ID | Test | Pass Threshold | Phase 7 Column Schema | Survival Condition |
|----|------|----------------|-----------------------|--------------------|
| T-1 | Differentiation | Meaningfully distinct mechanism from every other `**` candidate | "T-1: Differentiation" | Removing this eliminates an approach not covered by remaining 4 |
| T-2 | Topic Fit | Rationale names a specific dimension of `{{topic}}` | "T-2: Topic Fit" | Rationale fails if topic swapped |
| T-3 | Inertia Displacement — adjudicated from Phase 6 evidence | PASS on ≥3 of 5 anchor fields; evidence sourced from Ph6 Anchor Citation | **Five columns:** "T-3: Costs" / "T-3: Benefits" / "T-3: Competitive Threshold" / "T-3: Bypasses" / "T-3: Preserves" — exact labels locked | ≥3 PASS cells; T-3 evaluation is adjudication of Phase 6 Anchor Citation claims, not first-pass judgment |
| T-4 | Category Coverage | Candidate's category absent from other 4 `**` picks | "T-4: Category Coverage" | Removing collapses top-5 below 3 categories |

**T-3 adjudication protocol (locked at Phase 1)**: For each T-3 anchor column in Phase 7 — (1) read Ph6 Anchor Citation; (2) if the field label appears: adjudicate whether the Rationale's claim demonstrates superiority (PASS = strong claim, PARTIAL = weak claim, FAIL = claim doesn't hold); (3) if the label is ABSENT from Ph6 Anchor Citation: evaluate Rationale for implicit support (usually PARTIAL or FAIL, unless Rationale explicitly references that anchor dimension without using the label). T-3 PASS threshold: ≥3 PASS cells across 5 columns.

T-3 schema LOCKED at Phase 1 exit. Framework LOCKED — modification BREACH-FATAL.

#### Table 1B — Ledger Contract (Blueprint + Taxonomy fused)

| Phase | Phase Name | Ledger Field | Violation Condition | BREACH Tier | Correction | Continue? |
|-------|-----------|--------------|---------------------|-------------|------------|-----------|
| 3 | Architecture | AMEND Source + Primary Challenge Test cols on every row | Any row missing either col | BREACH-MAJOR | Halt; add col; repopulate | NO |
| 4 | Do Nothing Anchor | Challenge Binding col on every anchor row | Any row missing Challenge Binding | BREACH-MAJOR | Halt; add col; correct rows | NO |
| 5 | Diverge | Name + Pitch on every candidate row | Missing Name or Pitch | BREACH-MINOR | Correct in-place | YES |
| 6 | Cluster T-Evidence | T-Evidence `T-1:[v]·T-2:[v]·T-3:[dims]·T-4:[v]` on every row | Col absent; >1/3 unstructured | BREACH-MAJOR if col absent | Halt; add col; repopulate | NO |
| 6 | Cluster Anchor Citation | Anchor Citation col; every row cites ≥1 anchor field label by name | Col absent; >1/3 blank | BREACH-MAJOR if col absent; BREACH-MINOR if <1/3 blank | Col absent: halt, add, repopulate. Blank: rewrite Rationale inline. | NO if absent |
| 7 | Evidence Triage | Ph6 Anchor Citation col (first data col) + Ph6 Pre-Score col + T-3 via 5 locked cols | Missing Ph6 Anchor Citation as first col; missing Ph6 Pre-Score; merged T-3 | BREACH-FATAL if `**` pre-assigned; BREACH-MAJOR schema | Discard+restart or halt+reconstruct | NO |

#### Table 1C — BREACH Taxonomy

| Severity | Definition | Correction | Continue? |
|----------|------------|------------|-----------|
| BREACH-MINOR | Recommended field absent; <1/3 rows missing; overlapping AMEND directions | Correct in-place; mark `[corrected]` | YES |
| BREACH-MAJOR | Required col absent; concentration cap exceeded; count outside 20–40; T-3 schema deviated; Anchor Citation col absent; Ph6 Anchor Citation not first col in Phase 7 | HALT; reconstruct; re-verify | NO |
| BREACH-FATAL | Candidates before Phase 1; `**` before Phase 7; anchor absent; framework modified after lock | STOP; discard; restart | NO |

EXIT TABLE — Phase 1
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Table 1A: all 4 tests; T-3 names all 5 labels; T-3 adjudication protocol declared | BREACH-FATAL |
| Table 1B: 6 obligation rows; BREACH Tier + Correction + Continue? cols populated | BREACH-MAJOR |
| Table 1C: all 3 tiers | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — AMEND ADJUSTMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 2
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Table 1A (Challenge Framework + T-3 Adjudication Protocol) | Phase 1 | T-1/T-2/T-3/T-4 declared; adjudication protocol locked; T-3 schema locked (5 col labels) |
| Table 1B (Ledger Contract) | Phase 1 | 6 obligation rows; BREACH Tier col populated |
| Table 1C (BREACH Taxonomy) | Phase 1 | 3 severity tiers |

| # | Dimension | Direction | Downstream Effect on Pool |
|---|-----------|-----------|--------------------------|
| A1 | | | |
| A2 | | | |
| A3 | | | |

Rules: non-overlapping directions; effects `{{topic}}`-specific.

EXIT TABLE — Phase 2
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Exactly 3 rows; Dimension + Direction + Downstream Effect filled | BREACH-MINOR |
| Directions distinct | BREACH-MINOR |
| Effects `{{topic}}`-specific | BREACH-MINOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3 — ARCHITECTURE DECLARATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 3
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| AMEND Adjustments Table (A1/A2/A3) | Phase 2 | 3 rows; Dimension + Direction + Downstream Effect filled |

| Category | Description | Target Count | % of Pool | AMEND Source | Primary Challenge Test |
|----------|-------------|--------------|-----------|--------------|------------------------|

Total: ______

Rules: ≥4 categories; largest ≤40%; totals 20–40; AMEND Source + Primary Challenge Test on every row; ≥1 row T-3. Largest ≥40% — redistribute (BREACH-MAJOR).

EXIT TABLE — Phase 3
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| ≥4 categories; % computed; no category ≥40% | BREACH-MAJOR |
| AMEND Source col; all rows populated | BREACH-MAJOR |
| Primary Challenge Test col; ≥1 row T-3 | BREACH-MAJOR |
| Total 20–40 | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — DO NOTHING ANCHOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 4
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Category Architecture Table | Phase 3 | ≥4 categories; AMEND Source + Primary Challenge Test cols; ≥1 T-3 row; ≤40% cap |
| AMEND Adjustments Table (A1/A2/A3) | Phase 2 | 3 rows |

Write the Do Nothing anchor grounded in Phase 3 architecture. Bypasses + Preserves must name specific Phase 3 category labels.

| Field | Content | Challenge Binding |
|-------|---------|-------------------|
| Costs | | T-3 |
| Benefits | | T-3 |
| Competitive Threshold | [reference ≥1 Phase 3 category] | T-3 |
| Bypasses | [name ≥1 Phase 3 category label] | T-3 |
| Preserves | | T-3 |
| Net Position | [integrated judgment; displacement condition] | T-3 synthesis |

**Anchor Citation vocabulary (for Phase 6)**: The 6 field labels above — Costs, Benefits, Competitive Threshold, Bypasses, Preserves, Net Position — are the citation vocabulary for Phase 6's Anchor Citation column. Phase 6 must cite these labels by name. Candidates that cite none of these labels have not engaged with the anchor.

EXIT TABLE — Phase 4
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| All 6 field rows with `{{topic}}`-specific content | BREACH-MAJOR |
| Challenge Binding col; all rows populated | BREACH-MAJOR |
| Costs AND Benefits both present | BREACH-MINOR |
| Bypasses + Preserves name Phase 3 labels | BREACH-MINOR |
| Net Position names displacement condition | BREACH-MINOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5 — DIVERGE (Name + Pitch Only)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 5
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Do Nothing Anchor Table (6 fields + anchor citation vocabulary) | Phase 4 | All 6 fields; Challenge Binding col; citation vocabulary declared |
| Category Architecture Table | Phase 3 | Category labels and slot budgets |

Generate 22–38 Name+Pitch pairs only. No categories, rationales, anchor citations, T-Evidence. No `**` — BREACH-FATAL.

| # | Name | Pitch (one line) |
|---|------|-----------------|

EXIT TABLE — Phase 5
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| 20–40 candidates; Name + Pitch only | BREACH-MAJOR |
| No categories, rationales, or `**` | BREACH-MINOR if present |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6 — CLUSTER + ANCHOR CITATION + T-EVIDENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 6
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Diverge List | Phase 5 | 20–40 Name+Pitch rows; no categories |
| Category Architecture Table | Phase 3 | Category labels with slot budgets |
| Do Nothing Anchor Table + Citation Vocabulary | Phase 4 | 6 field labels: Costs, Benefits, Competitive Threshold, Bypasses, Preserves, Net Position |

Assign Category, Rationale, Anchor Citation, and T-Evidence to every candidate. Column order: Category → Rationale → Anchor Citation → T-Evidence (the Anchor Citation must be written before T-Evidence, because T-3 dims cleared derive from the Anchor Citation).

| # | Name | Category | Rationale | Anchor Citation | T-Evidence |
|---|------|----------|-----------|-----------------|------------|

**Anchor Citation is written BEFORE T-Evidence** for every row. This ordering matters: Phase 7 adjudicates Anchor Citation claims; T-Evidence records whether the claim clears the T-3 threshold. The citation is the evidence declaration; the T-Evidence verdict is derived from it.

**Anchor Citation format**: list Phase 4 field labels cited by name (e.g., "Costs", "Bypasses + Net Position"). Inline conditional: if Rationale names no anchor field — rewrite the Rationale to add one displacement claim referencing a specific anchor field, then enter the citation. Do not leave Anchor Citation blank unless the candidate structurally cannot address any anchor dimension (mark "N/A — structural"); >1/3 blank triggers BREACH-MINOR.

**T-Evidence format**: `T-1:[PASS/PARTIAL/FAIL]·T-2:[PASS/PARTIAL/FAIL]·T-3:[dims cleared]·T-4:[PASS/PARTIAL/FAIL]`
T-3 dims cleared: anchor field labels where the Rationale demonstrates superiority — derived from Anchor Citation entries.

Concentration check: any category at 40% — redistribute before continuing (BREACH-MAJOR).

EXIT TABLE — Phase 6
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Anchor Citation col present; ≤1/3 rows blank | BREACH-MAJOR if col absent; BREACH-MINOR if <1/3 blank |
| Anchor Citation written before T-Evidence in every row | BREACH-MINOR if ordering violated |
| T-Evidence col; structured notation on every row | BREACH-MAJOR if col absent |
| No category ≥40% | BREACH-MAJOR |
| All Phase 5 candidates present | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — EVIDENCE TRIAGE
(formerly "Adversarial Challenge" — reframed as adjudication of pre-declared Phase 6 claims)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 7 (Evidence Triage)
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Cluster Table with Anchor Citation col | Phase 6 | Anchor Citation col present; ≤1/3 rows blank; col written before T-Evidence |
| Cluster Table T-Evidence col | Phase 6 | T-Evidence col present; structured notation on all rows |
| Do Nothing Anchor Table | Phase 4 | 6 fields; Challenge Binding col present |
| Table 1A (T-3 Adjudication Protocol + Schema) | Phase 1 | T-3 col schema: Costs/Benefits/Competitive Threshold/Bypasses/Preserves; adjudication protocol declared |

**Load Phase 6 evidence first. This phase adjudicates pre-declared displacement claims — do not form first-pass judgments.**

Step 7-0 (load): For each candidate, read Ph6 Anchor Citation before writing any T-3 cell. The Ph6 Anchor Citation declares which anchor dimensions the candidate has pre-committed to displacing. T-3 evaluation verifies those claims — it does not re-ask "which anchor fields does this candidate beat?"

Do not mark `**` yet — BREACH-FATAL if assigned in this phase.

Column schema (Ph6 Anchor Citation is the FIRST data column after Name):
`| # | Name | Ph6 Anchor Citation | Ph6 Pre-Score | T-1: Differentiation | T-2: Topic Fit | T-3: Costs | T-3: Benefits | T-3: Competitive Threshold | T-3: Bypasses | T-3: Preserves | T-4: Category Coverage | Verdict |`

- **Ph6 Anchor Citation (first data col)**: copy Anchor Citation from Phase 6 verbatim — this column is loaded BEFORE T-3 evaluation begins
- **Ph6 Pre-Score**: copy T-Evidence from Phase 6 verbatim
- **T-3 column adjudication** (apply Table 1A protocol for each of the 5 cols):
  - If Ph6 Anchor Citation contains this field's label: adjudicate the Rationale's claim — PASS (strong, specific claim with mechanism), PARTIAL (claim present but weak or vague), FAIL (claim doesn't hold or contradicts Do Nothing anchor)
  - If Ph6 Anchor Citation does NOT contain this field's label: assess Rationale for implicit support — usually PARTIAL or FAIL; PASS only if Rationale explicitly names the anchor field without the label
- T-3 PASS threshold: ≥3 PASS cells across 5 cols

EXIT TABLE — Phase 7
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Ph6 Anchor Citation col present as FIRST data col; populated from Phase 6 | BREACH-MAJOR |
| Ph6 Pre-Score col present; populated from Phase 6 | BREACH-MAJOR |
| T-3 via 5 separate anchor-named cols; labels match Table 1A schema | BREACH-MAJOR if merged or deviation |
| T-3 adjudication followed Table 1A protocol (cite-check before judgment) | BREACH-MINOR if protocol not followed |
| No `**` assigned | BREACH-FATAL if present |
| All candidates evaluated with Verdict | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 8 — MARK + FINALIZE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 8
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 7 Evidence Triage Table | Phase 7 | All candidates evaluated; Ph6 Anchor Citation col present; Ph6 Pre-Score col present; 5 T-3 anchor-named cols; no `**` marks |
| Table 1A (Survival Threshold) | Phase 1 | All 4 tests PASS required |

Apply `**` to exactly 5 entries in Phase 6 cluster table. Top-5 must span ≥3 categories; removing any one must lose a distinct angle.

EXIT TABLE — Phase 8
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Exactly 5 `**` marks applied | BREACH-FATAL |
| `**` set spans ≥3 categories | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9A — TERMINAL LEDGER AUDIT (Reconstruct → Assess)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 9A
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 8 Output (`**` marks applied) | Phase 8 | Exactly 5 `**` marks on Cluster Table |
| Phase 7 Evidence Triage Table | Phase 7 | Ph6 Anchor Citation col (first data col) + Ph6 Pre-Score col + 5 T-3 cols |
| Phase 6 Cluster Table | Phase 6 | Anchor Citation + T-Evidence cols present |
| All contributing phases (3–7) | Phases 3–7 | Exit gates passed |

Phase 9B may not begin until Phase 9A complete and all ledger rows COMPLETE.

**RECONSTRUCT PASS**:

| Phase | Obligation | What Was Actually Produced | COMPLETE? |
|-------|-----------|---------------------------|-----------|
| Phase 3 | AMEND Source + Primary Challenge Test cols | [col names; row count] | Y/N |
| Phase 4 | Challenge Binding col + anchor citation vocabulary | [col present; 6 labels declared] | Y/N |
| Phase 5 | Name + Pitch | [row count; blanks] | Y/N |
| Phase 6 T-Evidence | Structured notation | [format; blank count] | Y/N |
| Phase 6 Anchor Citation | Anchor Citation col; pre-T-Evidence ordering | [col present; labels used — 3 examples; blank count; confirm written before T-Evidence: Y/N] | Y/N |
| Phase 7 | Ph6 Anchor Citation col (first data col) + Ph6 Pre-Score + T-3 cols | **T-3 headers observed: [enumerate each T-3-prefixed header exactly as written]** Expected: T-3: Costs / T-3: Benefits / T-3: Competitive Threshold / T-3: Bypasses / T-3: Preserves. Match per header: [MATCH/MISMATCH]. C-27 verdict. Ph6 Anchor Citation as first data col: Y/N | Y/N |

**ASSESS PASS**:

| Ledger Row | Status | Declared Severity | Action |
|-----------|--------|-------------------|--------|
| Phase 3 architecture | | | |
| Phase 4 anchor | | | |
| Phase 5 diverge | | | |
| Phase 6 T-Evidence | | | |
| Phase 6 Anchor Citation | | | |
| Phase 7 evidence triage | | | |

Correct all VIOLATION rows before Phase 9B.

EXIT TABLE — Phase 9A
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Reconstruct pass: 6 rows (one per contributing phase) | BREACH-MAJOR |
| T-3 headers enumerated for Phase 7 row; C-27 verdict rendered | BREACH-MAJOR |
| Phase 6 Anchor Citation ordering confirmed (written before T-Evidence) | BREACH-MINOR |
| Ph6 Anchor Citation as first data col in Phase 7 confirmed | BREACH-MAJOR |
| Assess pass: Declared Severity populated for all rows | BREACH-MAJOR |
| All 6 ledger rows COMPLETE | BREACH-FATAL |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9B — CRITERION CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 9B
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 9A Terminal Ledger Audit | Phase 9A | Reconstruct + Assess passes complete; all 6 ledger rows COMPLETE; C-27 verdict rendered; Ph6 Anchor Citation ordering confirmed |

| Row | Criterion | Status | Severity if FAIL |
|-----|-----------|--------|-----------------|
| 1 | Candidate count 20–40 (excl. Do Nothing) | PASS/FAIL | BREACH-MAJOR |
| 2 | Every candidate: all 4 anatomy fields | PASS/FAIL | BREACH-MAJOR |
| 3 | Exactly 5 `**` marks | PASS/FAIL | BREACH-FATAL |
| 4 | Do Nothing: 6 fields incl. Net Position | PASS/FAIL | BREACH-MAJOR |
| 5 | AMEND: 3 adjustments; dimension + downstream effect | PASS/FAIL | BREACH-MINOR |
| 6 | Architecture: AMEND Source col | PASS/FAIL | BREACH-MAJOR |
| 7 | Architecture: Primary Challenge Test col; ≥1 row T-3 | PASS/FAIL | BREACH-MAJOR |
| 8 | Phase 6: T-Evidence structured notation | PASS/FAIL | BREACH-MAJOR |
| 9 | Phase 7: Ph6 Pre-Score carryforward col | PASS/FAIL | BREACH-MAJOR |
| 10 | `**` set spans ≥3 categories | PASS/FAIL | BREACH-MAJOR |
| 11 | Phase 4 Challenge Binding col; Net Position maps to T-3 synthesis | PASS/FAIL | BREACH-MAJOR |
| 12 | Table 1C: all 3 BREACH tiers | PASS/FAIL | BREACH-FATAL |
| 13 | Phase 9A Declared Severity col populated | PASS/FAIL | BREACH-MAJOR |
| 14 | Phase 7 T-3 via 5 separate anchor-named cols | PASS/FAIL | BREACH-MAJOR |
| 15 | Table 1B BREACH Tier col; all rows populated | PASS/FAIL | BREACH-MAJOR |
| 16 | Phase 9A Reconstruct T-3 step complete; C-27 verdict rendered | PASS/FAIL | BREACH-MAJOR |
| 17 | Phase 6 Anchor Citation col present; ≤1/3 blank | PASS/FAIL | BREACH-MAJOR if absent |
| 18 | Phase 7 Ph6 Anchor Citation col present as FIRST data col | PASS/FAIL | BREACH-MAJOR |
| 19 | T-3 adjudication followed Table 1A cite-check protocol in Phase 7 | PASS/FAIL | BREACH-MINOR |

EXIT TABLE — Phase 9B
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| All 19 rows checked | BREACH-MINOR |
| All FAIL rows corrected | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WRITE — ARTIFACT ASSEMBLY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — WRITE
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 9B Criterion Checklist | Phase 9B | All 19 rows PASS or corrected |
| Cluster Table with `**` marks | Phase 8 | Exactly 5 `**` marks |
| AMEND Adjustments Table | Phase 2 | 3 adjustments |
| Do Nothing Anchor Table | Phase 4 | 6 fields |

Write to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

Structure: Title → AMEND (A1/A2/A3) → Do Nothing (costs, benefits, net position) → Category sections; `**` on top-5; each entry: Name — Pitch — Rationale.
```

