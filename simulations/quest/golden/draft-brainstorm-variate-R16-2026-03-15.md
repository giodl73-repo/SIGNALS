# draft-brainstorm Skill Prompt Variations — Round 16

**Skill:** draft-brainstorm
**Round:** 16
**Date:** 2026-03-15
**Rubric:** v15 (C-01 through C-48)
**Baseline:** R15 closes C-43 at 4/5 PASS (V-01 FAIL) and C-44 at 3/5 PASS (V-02, V-03 FAIL). All 5 R15 variations were PARTIAL on C-35. R16 promotes C-43 + C-44 + C-46 to shared baseline. Targets: C-45, C-47, C-48 first stable runs; C-35 fix across all variations.

---

## R16 Axis Selection

R15's remaining instabilities after v14 scoring:
- **C-43** (Anchor Citation column in Phase 6): V-01 R15 FAIL — V-01 was C-44 single-axis only, no Anchor Citation column added.
- **C-44** (ENTRY TABLE + EXIT TABLE schemas at every phase): V-02, V-03 R15 FAIL — both used prose entry conditions and checkbox exit gates.
- **C-35** (affirmative ledger obligation bullets): all 5 R15 PARTIAL — EXIT TABLE BREACH rows do not satisfy the "Ledger obligation satisfied: [contribution]" declaration.

R15 V-05 introduced all 4 v15 excellence signals. Gap analysis vs. full PASS:
- **C-45**: V-05 R15 had prose ordering instruction + EXIT TABLE row, but no ordering annotation in the column schema declaration itself. Pass requires an explicit instruction in the schema: "Anchor Citation written before T-Evidence" as part of the column schema header, not only in prose instructions.
- **C-46**: V-05 R15 named Phase 7 "Evidence Triage" + Ph6 Anchor Citation as first data col — likely PASS. R16 promotes to baseline.
- **C-47**: V-05 R15 Reconstruct Phase 6 row had "confirm written before T-Evidence: Y/N" — a yes/no confirmation, not a statement of observed ordering. Pass requires stating the observed column sequence, not just confirming it.
- **C-48**: V-05 R15 Phase 5 ENTRY TABLE said "citation vocabulary declared" without listing the specific labels. Pass requires "Costs, Benefits, Competitive Threshold, Bypasses, Preserves" enumerated by name.

| Variation | Primary Axis | Novel Structural Feature |
|-----------|--------------|--------------------------|
| V-01 | C-45 single-axis | Phase 6 column schema header carries explicit "Anchor Citation precedes T-Evidence" ordering annotation; row protocol sequenced: (1) write Anchor Citation, (2) derive T-Evidence |
| V-02 | C-48 single-axis | Phase 5 ENTRY TABLE dedicated row enumerates all 5 anchor field labels by name as declared vocabulary |
| V-03 | C-35 single-axis | Every contributing phase exit carries "Ledger obligation satisfied: [contribution]" bullet after EXIT TABLE — affirmative declaration separate from BREACH rows |
| V-04 | C-45 + C-48 combined | Ordering annotation in cluster schema + vocabulary labels in Phase 5 ENTRY TABLE |
| V-05 | C-45 + C-47 + C-48 + C-35 full stack | Ordering annotation, Reconstruct observed-ordering state, vocabulary labels enumerated, affirmative ledger obligation bullets |

---

## V-01 — Single-axis: C-45 Ordering Annotation in Cluster Schema

**Variation axis:** Lifecycle emphasis — the Phase 6 column schema declaration carries an explicit ordering annotation so that the constraint "Anchor Citation precedes T-Evidence" is visible in the schema header itself, not only in prose instructions. Row-writing protocol is explicitly sequenced: Step 1 write Anchor Citation, Step 2 derive T-Evidence from it. All other elements (C-43, C-44, C-46) match the R15 V-05 baseline.

**Hypothesis:** R15 V-05 had an ordering instruction in bold prose and in the EXIT TABLE, but the column schema line itself (`| # | Name | Category | Rationale | Anchor Citation | T-Evidence |`) carries no ordering label. The C-45 pass condition requires the ordering to appear "as an explicit instruction or schema declaration" — the schema header is the most structurally unambiguous place to declare it, because a model that skips prose instructions still reads the column schema. When the ordering annotation is in the schema header, any output that reverses the columns is a structurally detectable BREACH at the column schema level, not just a prose-reminder miss.

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
| T-3 | Inertia Displacement — adjudicated from Ph6 Anchor Citation | PASS on ≥3 of 5 anchor fields evaluated independently; evidence sourced from Ph6 Anchor Citation | **Five columns:** "T-3: Costs" / "T-3: Benefits" / "T-3: Competitive Threshold" / "T-3: Bypasses" / "T-3: Preserves" — exact labels locked at Phase 1 | ≥3 PASS cells across 5 anchor-named T-3 columns; T-3 adjudicates Phase 6 pre-declared claims |
| T-4 | Category Coverage | Candidate's category absent from other 4 `**` picks | "T-4: Category Coverage" | Removing this pick collapses top-5 below 3 categories |

T-3 adjudication protocol (locked): For each T-3 column in Phase 7 — read Ph6 Anchor Citation first; if label present: adjudicate Rationale claim (PASS/PARTIAL/FAIL); if absent: assess implicit support (typically PARTIAL/FAIL). T-3 schema LOCKED — deviation is BREACH-MAJOR. Framework LOCKED — modification is BREACH-FATAL.

#### Table 1B — Ledger Contract (Blueprint + Taxonomy fused)

| Phase | Phase Name | Ledger Field | Violation Condition | BREACH Tier | Correction Action | Continue? |
|-------|-----------|--------------|---------------------|-------------|-------------------|-----------|
| 3 | Architecture | AMEND Source + Primary Challenge Test cols on every row | Any row missing either col | BREACH-MAJOR | Halt. Add col. Repopulate. Re-verify. | NO |
| 4 | Do Nothing Anchor | Challenge Binding col on every anchor row | Any row missing Challenge Binding | BREACH-MAJOR | Halt. Add col. Correct all rows. | NO |
| 5 | Diverge | Name + Pitch on every candidate row | Any candidate missing Name or Pitch | BREACH-MINOR | Correct in-place. Mark [corrected]. | YES |
| 6 | Cluster T-Evidence | T-Evidence col with structured notation `T-1:[v]·T-2:[v]·T-3:[dims]·T-4:[v]` on every row | Col absent; >1/3 rows unstructured | BREACH-MAJOR if col absent; BREACH-MINOR if <1/3 blank | Col absent: halt, add, repopulate. Blank: correct inline. | Col absent: NO |
| 6 | Cluster Anchor Citation | Anchor Citation col; every row cites ≥1 anchor field label from Phase 4 | Col absent; >1/3 rows blank | BREACH-MAJOR if col absent; BREACH-MINOR if <1/3 blank | Col absent: halt, add, repopulate. Blank: rewrite Rationale, add citation. | Col absent: NO |
| 7 | Evidence Triage | Ph6 Anchor Citation col (first data col) + Ph6 Pre-Score col + T-3 via 5 locked cols | Missing Ph6 Anchor Citation first; missing Ph6 Pre-Score; merged T-3 | BREACH-FATAL if `**` pre-assigned; BREACH-MAJOR for schema deviations | Pre-assigned `**`: discard Phase 7+, restart. Schema: halt, reconstruct. | NO |

#### Table 1C — BREACH Severity Taxonomy

| Severity | Definition | Correction Protocol | Continue? |
|----------|------------|---------------------|-----------|
| BREACH-MINOR | Recommended field absent; <1/3 rows missing content; overlapping AMEND directions; anchor citation missing from <1/3 rationales | Correct in-place; mark [corrected] | YES |
| BREACH-MAJOR | Required ledger column absent; concentration cap exceeded; count outside 20–40; T-3 schema deviated; Anchor Citation col absent; Ph6 Anchor Citation not first col in Phase 7 | HALT; reconstruct affected table; re-verify before advancing | NO |
| BREACH-FATAL | Candidates before Phase 1; `**` before Phase 7; anchor absent; framework modified after lock | STOP; discard from originating phase; restart | NO |

EXIT TABLE — Phase 1
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Table 1A: T-1/T-2/T-3/T-4 with Phase 7 col schema; T-3 names all 5 labels; adjudication protocol declared | BREACH-FATAL |
| Table 1B: 6 obligation rows (2 Phase 6 rows); BREACH Tier + Correction + Continue? cols populated on every row | BREACH-MAJOR |
| Table 1C: all 3 severity tiers with correction protocols | BREACH-MAJOR |
| T-3 schema locked; framework locked | — |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — AMEND ADJUSTMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 2
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Table 1A (Challenge Framework) | Phase 1 | T-1/T-2/T-3/T-4 declared; T-3 schema locked (5 col labels); adjudication protocol locked |
| Table 1B (Ledger Contract) | Phase 1 | 6 obligation rows; BREACH Tier col populated on every row |
| Table 1C (BREACH Taxonomy) | Phase 1 | 3 severity tiers with correction protocols |

Write exactly 3 pool-shaping adjustments before architecture or candidates are generated.

| # | Dimension | Direction | Downstream Effect on Pool |
|---|-----------|-----------|--------------------------|
| A1 | | | |
| A2 | | | |
| A3 | | | |

Rules: Dimension names a specific axis; Directions non-overlapping (one expands, one narrows, one redirects — not all pointing the same way); Downstream Effects reference `{{topic}}` specifically.

EXIT TABLE — Phase 2
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Exactly 3 AMEND rows; Dimension + Direction + Downstream Effect cols filled | BREACH-MINOR if any col blank |
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

Rules: ≥4 categories; largest ≤40% of pool; totals 20–40; every row has AMEND Source (A1/A2/A3) + Primary Challenge Test (T-1/T-2/T-3/T-4); ≥1 row lists T-3. Inline check: if largest category ≥40% — redistribute before exit (BREACH-MAJOR if not corrected).

EXIT TABLE — Phase 3
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| ≥4 distinct categories; % of Pool computed on every row | BREACH-MAJOR |
| No category ≥40% of total | BREACH-MAJOR |
| AMEND Source col present; every row populated | BREACH-MAJOR |
| Primary Challenge Test col present; ≥1 row lists T-3 | BREACH-MAJOR |
| Total count 20–40 | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — DO NOTHING ANCHOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 4
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Category Architecture Table | Phase 3 | ≥4 categories; AMEND Source + Primary Challenge Test cols; ≥1 T-3 row; ≤40% cap enforced |
| AMEND Adjustments Table (A1/A2/A3) | Phase 2 | 3 rows with Dimension + Direction + Downstream Effect |

Write the status quo anchor grounded in Phase 3 architecture. Bypasses and Preserves must name specific Phase 3 category labels.

| Field | Content | Challenge Binding |
|-------|---------|-------------------|
| Costs | [active costs of status quo for `{{topic}}`] | T-3 |
| Benefits | [genuine appeal of status quo — why inertia persists] | T-3 |
| Competitive Threshold | [minimum advantage an alternative must demonstrate; reference ≥1 Phase 3 category] | T-3 |
| Bypasses | [Phase 3 category labels the status quo renders unnecessary — name ≥1 by label] | T-3 |
| Preserves | [what a transition would put at risk for `{{topic}}`] | T-3 |
| Net Position | [integrated judgment: does inertia dominate? name the displacement condition] | T-3 synthesis |

**Anchor Citation vocabulary for Phase 6**: The 6 field labels above — Costs, Benefits, Competitive Threshold, Bypasses, Preserves, Net Position — are the citation strings for Phase 6's Anchor Citation column. Phase 6 must cite these labels by name. Candidates citing none of these labels have not engaged with the anchor.

Do Nothing does NOT count toward the 20–40 candidate total.

EXIT TABLE — Phase 4
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| All 6 field rows present with `{{topic}}`-specific content | BREACH-MAJOR |
| Challenge Binding col present; all 6 rows populated | BREACH-MAJOR |
| Costs AND Benefits both present | BREACH-MINOR |
| Bypasses + Preserves name Phase 3 category labels | BREACH-MINOR |
| Net Position names a displacement condition (not directional-only) | BREACH-MINOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5 — DIVERGE (Name + Pitch Only)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 5
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Do Nothing Anchor Table (6 fields) | Phase 4 | Costs/Benefits/Competitive Threshold/Bypasses/Preserves/Net Position rows; Challenge Binding col present |
| Category Architecture Table | Phase 3 | Category labels and slot budgets available |

Generate 22–38 Name+Pitch pairs only. No categories, rationales, anchor citations, or T-Evidence. No `**` marks — BREACH-FATAL if assigned before Phase 7.

| # | Name | Pitch (one line) |
|---|------|-----------------|

EXIT TABLE — Phase 5
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| 20–40 candidate rows (Name + Pitch only) | BREACH-MAJOR |
| No categories, rationales, anchor citations, or `**` marks assigned | BREACH-MINOR if present |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6 — CLUSTER + ANCHOR CITATION + T-EVIDENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 6
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Diverge List | Phase 5 | 20–40 Name+Pitch rows; no categories or rationales assigned |
| Category Architecture Table | Phase 3 | Category labels with slot budgets |
| Do Nothing Anchor Table + Citation Vocabulary | Phase 4 | 6 field labels: Costs, Benefits, Competitive Threshold, Bypasses, Preserves, Net Position |

**C-45 ORDERING CONSTRAINT: Anchor Citation is written before T-Evidence in every row. This ordering is enforced at the column schema level — T-Evidence derives from Anchor Citation and must come after it.**

Phase 6 cluster column schema (Anchor Citation precedes T-Evidence — write Anchor Citation first, then derive T-Evidence):
| # | Name | Category | Rationale | Anchor Citation [write first] | T-Evidence [derived from Anchor Citation — write second] |

**Row-writing protocol (follow in sequence for each candidate):**
1. Write Rationale — topic-specific; name the specific mechanism for `{{topic}}`
2. **Write Anchor Citation** — scan Rationale for references to Phase 4 field labels (Costs, Benefits, Competitive Threshold, Bypasses, Preserves, Net Position). Enter exact label strings from Phase 4. If multiple labels apply, join with " + ". Inline check: if Rationale addresses no anchor field — rewrite to add one displacement claim before entering Anchor Citation. Do not skip this step.
3. **Derive T-Evidence** — from Rationale and Anchor Citation. T-Evidence format: `T-1:[PASS/PARTIAL/FAIL]·T-2:[PASS/PARTIAL/FAIL]·T-3:[dims cleared]·T-4:[PASS/PARTIAL/FAIL]`. T-3 dims cleared = anchor field labels where Rationale demonstrates superiority (derived from Anchor Citation).

Concentration check: if any category reaches 40% of total rows — redistribute before continuing (BREACH-MAJOR).

EXIT TABLE — Phase 6
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Anchor Citation col present; uses Phase 4 label strings; ≤1/3 rows blank | BREACH-MAJOR if col absent; BREACH-MINOR if <1/3 blank |
| Anchor Citation written before T-Evidence per C-45 ordering constraint | BREACH-MINOR if ordering violated |
| T-Evidence col present; structured notation on every row | BREACH-MAJOR if col absent |
| No category ≥40% | BREACH-MAJOR |
| All Phase 5 candidates present | BREACH-MAJOR |
| Rationales reference `{{topic}}` specifically | BREACH-MINOR if >1/5 generic |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — EVIDENCE TRIAGE
(adjudication of pre-declared Phase 6 claims — not first-pass evaluation)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 7 (Evidence Triage)
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Cluster Table — Anchor Citation col | Phase 6 | Anchor Citation col present; ≤1/3 rows blank; written before T-Evidence per C-45 |
| Cluster Table — T-Evidence col | Phase 6 | T-Evidence col present; structured notation on all rows |
| Do Nothing Anchor Table | Phase 4 | 6 fields; Challenge Binding col present |
| Table 1A (T-3 Adjudication Protocol + Schema) | Phase 1 | T-3 col schema locked: Costs/Benefits/Competitive Threshold/Bypasses/Preserves; adjudication protocol declared |

**Load Phase 6 evidence first. Ph6 Anchor Citation is the first data column. This phase adjudicates pre-declared displacement claims — do not form first-pass judgments.**

Step 7-0 (load): For each candidate, read Ph6 Anchor Citation before writing any T-3 cell. The citation declares which anchor dimensions the candidate has pre-committed to displacing. T-3 verifies those claims.

Do not mark `**` — BREACH-FATAL if assigned in this phase.

Column schema (Ph6 Anchor Citation is FIRST data column after Name):
`| # | Name | Ph6 Anchor Citation | Ph6 Pre-Score | T-1: Differentiation | T-2: Topic Fit | T-3: Costs | T-3: Benefits | T-3: Competitive Threshold | T-3: Bypasses | T-3: Preserves | T-4: Category Coverage | Verdict |`

- **Ph6 Anchor Citation (first data col)**: copy Anchor Citation from Phase 6 verbatim — loaded BEFORE T-3 evaluation
- **Ph6 Pre-Score**: copy T-Evidence from Phase 6 verbatim
- **T-3 adjudication** (5 cols, Table 1A protocol): if label present in Ph6 Anchor Citation: adjudicate claim; if absent: assess implicit support
- T-3 PASS threshold: ≥3 PASS cells

EXIT TABLE — Phase 7
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Ph6 Anchor Citation col present as FIRST data col; populated from Phase 6 | BREACH-MAJOR |
| Ph6 Pre-Score col present; populated from Phase 6 T-Evidence | BREACH-MAJOR |
| T-3 via 5 separate anchor-named cols; labels match Table 1A schema | BREACH-MAJOR if merged or label deviation |
| T-3 adjudication followed Table 1A cite-check protocol | BREACH-MINOR if protocol not followed |
| No `**` marks assigned | BREACH-FATAL if present |
| All candidates evaluated with Verdict | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 8 — MARK + FINALIZE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 8
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 7 Evidence Triage Table | Phase 7 | All candidates evaluated; Ph6 Anchor Citation col (first data col); Ph6 Pre-Score col; 5 T-3 anchor-named cols; no `**` marks |
| Table 1A (Survival Threshold) | Phase 1 | All 4 tests PASS required for `**` |

Select top 5 candidates. Apply `**` to exactly 5 entries in the Phase 6 cluster table. Top-5 set must span ≥3 distinct categories. Removing any one pick must eliminate a distinct angle. If <5 survive all 4 tests — select 5 by partial score, note any compromise.

EXIT TABLE — Phase 8
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Exactly 5 `**` marks applied to Phase 6 cluster table | BREACH-FATAL |
| `**` set spans ≥3 distinct categories | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9A — TERMINAL LEDGER AUDIT (Reconstruct → Assess)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 9A
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 8 Output (`**` marks applied) | Phase 8 | Exactly 5 `**` marks on Cluster Table |
| Phase 7 Evidence Triage Table | Phase 7 | Ph6 Anchor Citation (first data col) + Ph6 Pre-Score + 5 T-3 cols; all candidates evaluated |
| Phase 6 Cluster Table | Phase 6 | Anchor Citation + T-Evidence cols present; ordering constraint applied |
| All contributing phases (3–7) | Phases 3–7 | Exit tables completed |

Phase 9B may not begin until Phase 9A is complete and all ledger rows are COMPLETE.

**RECONSTRUCT PASS** — describe what was concretely produced in this execution (one row per contributing phase):

| Phase | Obligation | What Was Actually Produced | COMPLETE? |
|-------|-----------|---------------------------|-----------|
| Phase 3 | AMEND Source + Primary Challenge Test cols | [col names present; row count] | Y/N |
| Phase 4 | Challenge Binding col on anchor table | [col present; rows mapped; Net Position mapped to T-3 synthesis] | Y/N |
| Phase 5 | Name + Pitch on every candidate | [row count; any blank cells] | Y/N |
| Phase 6 T-Evidence | Structured notation | [format used; blank row count] | Y/N |
| Phase 6 Anchor Citation | Anchor Citation col; Phase 4 label strings; C-45 ordering | [col present; label examples (cite 3); blank count; Anchor Citation written before T-Evidence: Y/N] | Y/N |
| Phase 7 | Ph6 Anchor Citation (first col) + Ph6 Pre-Score + T-3 cols | **T-3 headers observed: [enumerate each T-3-prefixed header exactly as written in Phase 7 output]** Expected: T-3: Costs / T-3: Benefits / T-3: Competitive Threshold / T-3: Bypasses / T-3: Preserves. Match per header: [MATCH/MISMATCH for each]. C-27 verdict: PASS/PARTIAL/FAIL. Ph6 Anchor Citation as first data col: Y/N | Y/N |

**ASSESS PASS** — apply ledger criteria and violation definitions:

| Ledger Row | Status | Declared Severity | Action Required |
|-----------|--------|-------------------|----------------|
| Phase 3 architecture | COMPLETE/VIOLATION | | |
| Phase 4 anchor | COMPLETE/VIOLATION | | |
| Phase 5 diverge | COMPLETE/VIOLATION | | |
| Phase 6 T-Evidence | COMPLETE/VIOLATION | | |
| Phase 6 Anchor Citation | COMPLETE/VIOLATION | | |
| Phase 7 evidence triage | COMPLETE/VIOLATION | | |

Correct all VIOLATION rows before advancing to Phase 9B.

EXIT TABLE — Phase 9A
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Reconstruct pass completed: 6 rows (one per contributing phase) | BREACH-MAJOR |
| T-3 headers enumerated for Phase 7 row; C-27 verdict rendered | BREACH-MAJOR |
| Phase 6 Anchor Citation ordering confirmed (written before T-Evidence: Y/N) | BREACH-MINOR |
| Ph6 Anchor Citation confirmed as first data col in Phase 7 | BREACH-MAJOR |
| Assess pass completed; Declared Severity populated on all rows | BREACH-MAJOR |
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
| 2 | Every candidate: Name + Pitch + Category + Rationale | PASS/FAIL | BREACH-MAJOR |
| 3 | Exactly 5 `**` marks | PASS/FAIL | BREACH-FATAL |
| 4 | Do Nothing: 6 fields incl. Net Position | PASS/FAIL | BREACH-MAJOR |
| 5 | AMEND: 3 adjustments; each names dimension + downstream effect | PASS/FAIL | BREACH-MINOR |
| 6 | Architecture: AMEND Source col; every row populated | PASS/FAIL | BREACH-MAJOR |
| 7 | Architecture: Primary Challenge Test col; ≥1 row T-3 | PASS/FAIL | BREACH-MAJOR |
| 8 | Phase 6: T-Evidence structured notation on all rows | PASS/FAIL | BREACH-MAJOR |
| 9 | Phase 7: Ph6 Pre-Score carryforward col present | PASS/FAIL | BREACH-MAJOR |
| 10 | `**` set spans ≥3 distinct categories | PASS/FAIL | BREACH-MAJOR |
| 11 | Phase 4 anchor Challenge Binding col; Net Position maps to T-3 synthesis | PASS/FAIL | BREACH-MAJOR |
| 12 | Table 1C: all 3 BREACH tiers with correction protocols | PASS/FAIL | BREACH-FATAL |
| 13 | Phase 9A Declared Severity col populated on all rows | PASS/FAIL | BREACH-MAJOR |
| 14 | Phase 7 T-3 via 5 separate anchor-named cols | PASS/FAIL | BREACH-MAJOR |
| 15 | Table 1B BREACH Tier col; all rows populated | PASS/FAIL | BREACH-MAJOR |
| 16 | Phase 9A Reconstruct T-3 step complete; C-27 verdict rendered | PASS/FAIL | BREACH-MAJOR |
| 17 | Phase 6 Anchor Citation col present; ≤1/3 rows blank | PASS/FAIL | BREACH-MAJOR if absent |
| 18 | Phase 7 Ph6 Anchor Citation col present as FIRST data col | PASS/FAIL | BREACH-MAJOR |
| 19 | Phase 6 cluster schema: "Anchor Citation precedes T-Evidence" ordering annotation present; row protocol sequenced | PASS/FAIL | BREACH-MINOR |

Apply Table 1C correction protocol for every FAIL before writing the artifact.

EXIT TABLE — Phase 9B
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| All 19 rows checked | BREACH-MINOR |
| All FAIL rows corrected per Table 1C protocol | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WRITE — ARTIFACT ASSEMBLY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — WRITE
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 9B Criterion Checklist | Phase 9B | All 19 rows PASS or corrected |
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

## V-02 — Single-axis: C-48 Vocabulary Gate in Phase 5 ENTRY TABLE

**Variation axis:** Lifecycle emphasis — Phase 5's ENTRY TABLE includes a dedicated row that lists all 5 anchor field label strings by name (Costs, Benefits, Competitive Threshold, Bypasses, Preserves) as declared vocabulary. This makes anchor citation vocabulary an explicit entry precondition for diverge, so candidates can be generated with the anchor's displacement vocabulary actively available from the first row written. All other elements match V-01 (C-43, C-44, C-45, C-46).

**Hypothesis:** R15 V-05 Phase 5 ENTRY TABLE said "citation vocabulary declared" in the Required State column — a boolean presence check. The C-48 pass condition requires the specific field labels to be enumerated in the vocabulary row itself, so the model has the actual strings available when writing Phase 5 pitches. When the labels are listed in the ENTRY TABLE, Phase 5 generation happens with the full anchor vocabulary in working context rather than as a recalled expectation. This enables retrofitting-free Phase 6: candidates written with vocabulary awareness tend to have rationales that already reference anchor fields, making Phase 6 Anchor Citation annotation a confirmation rather than a construction task.

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
| T-3 | Inertia Displacement — adjudicated from Ph6 Anchor Citation | PASS on ≥3 of 5 anchor fields; evidence sourced from Ph6 Anchor Citation | **Five columns:** "T-3: Costs" / "T-3: Benefits" / "T-3: Competitive Threshold" / "T-3: Bypasses" / "T-3: Preserves" — exact labels locked | ≥3 PASS cells; T-3 adjudicates pre-declared Ph6 claims |
| T-4 | Category Coverage | Candidate's category absent from other 4 `**` picks | "T-4: Category Coverage" | Removing collapses top-5 below 3 categories |

T-3 adjudication protocol (locked): read Ph6 Anchor Citation first; if label present: adjudicate claim; if absent: assess implicit support. T-3 schema LOCKED — deviation BREACH-MAJOR. Framework LOCKED — modification BREACH-FATAL.

#### Table 1B — Ledger Contract (Blueprint + Taxonomy fused)

| Phase | Phase Name | Ledger Field | Violation Condition | BREACH Tier | Correction Action | Continue? |
|-------|-----------|--------------|---------------------|-------------|-------------------|-----------|
| 3 | Architecture | AMEND Source + Primary Challenge Test cols on every row | Any row missing either col | BREACH-MAJOR | Halt. Add col. Repopulate. | NO |
| 4 | Do Nothing Anchor | Challenge Binding col on every anchor row | Any row missing Challenge Binding | BREACH-MAJOR | Halt. Add col. Correct rows. | NO |
| 5 | Diverge | Name + Pitch on every candidate row | Missing Name or Pitch | BREACH-MINOR | Correct in-place. | YES |
| 6 | Cluster T-Evidence | T-Evidence col `T-1:[v]·T-2:[v]·T-3:[dims]·T-4:[v]` on every row | Col absent; >1/3 unstructured | BREACH-MAJOR if col absent | Halt; add; repopulate | NO |
| 6 | Cluster Anchor Citation | Anchor Citation col; every row cites ≥1 anchor field label | Col absent; >1/3 blank | BREACH-MAJOR if absent; BREACH-MINOR if <1/3 blank | Col absent: halt, add, repopulate. Blank: rewrite Rationale inline. | NO if absent |
| 7 | Evidence Triage | Ph6 Anchor Citation (first col) + Ph6 Pre-Score + T-3 via 5 locked cols | Missing Ph6 Anchor Citation first; missing Ph6 Pre-Score; merged T-3 | BREACH-FATAL if `**` pre-assigned; BREACH-MAJOR schema | Discard+restart or halt+reconstruct | NO |

#### Table 1C — BREACH Severity Taxonomy

| Severity | Definition | Correction Protocol | Continue? |
|----------|------------|---------------------|-----------|
| BREACH-MINOR | Recommended field absent; <1/3 rows missing; overlapping AMEND directions | Correct in-place; mark [corrected] | YES |
| BREACH-MAJOR | Required ledger col absent; concentration cap exceeded; count outside 20–40; T-3 schema deviated; Anchor Citation col absent; Ph6 Anchor Citation not first col in Phase 7 | HALT; reconstruct; re-verify | NO |
| BREACH-FATAL | Candidates before Phase 1; `**` before Phase 7; anchor absent; framework modified after lock | STOP; discard; restart | NO |

EXIT TABLE — Phase 1
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Table 1A: all 4 tests; T-3 names all 5 labels; adjudication protocol declared | BREACH-FATAL |
| Table 1B: 6 obligation rows; BREACH Tier + Correction + Continue? cols populated | BREACH-MAJOR |
| Table 1C: all 3 tiers with correction protocols | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — AMEND ADJUSTMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 2
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Table 1A (Challenge Framework) | Phase 1 | T-1/T-2/T-3/T-4 declared; T-3 schema locked (5 col labels); adjudication protocol locked |
| Table 1B (Ledger Contract) | Phase 1 | 6 obligation rows; BREACH Tier col populated |
| Table 1C (BREACH Taxonomy) | Phase 1 | 3 severity tiers with correction protocols |

| # | Dimension | Direction | Downstream Effect on Pool |
|---|-----------|-----------|--------------------------|
| A1 | | | |
| A2 | | | |
| A3 | | | |

Rules: non-overlapping directions; effects `{{topic}}`-specific.

EXIT TABLE — Phase 2
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Exactly 3 rows; all cols filled | BREACH-MINOR if any blank |
| Directions distinct (non-overlapping) | BREACH-MINOR |
| Downstream Effects reference `{{topic}}` | BREACH-MINOR if generic |

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
| ≥4 categories; % of Pool computed; no category ≥40% | BREACH-MAJOR |
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
| AMEND Adjustments Table | Phase 2 | 3 rows with Dimension + Direction + Downstream Effect |

Write the Do Nothing anchor grounded in Phase 3 architecture. Bypasses + Preserves must name specific Phase 3 category labels.

| Field | Content | Challenge Binding |
|-------|---------|-------------------|
| Costs | [active costs of status quo] | T-3 |
| Benefits | [genuine appeal of status quo] | T-3 |
| Competitive Threshold | [minimum advantage; reference ≥1 Phase 3 category] | T-3 |
| Bypasses | [Phase 3 category labels rendered unnecessary] | T-3 |
| Preserves | [what transition would put at risk] | T-3 |
| Net Position | [integrated judgment; displacement condition] | T-3 synthesis |

**Anchor Citation vocabulary (declared for Phase 5 and Phase 6)**: The 5 displacement field labels — Costs, Benefits, Competitive Threshold, Bypasses, Preserves — are the citation vocabulary. These exact strings must be used in Phase 6 Anchor Citation. Net Position is available as a synthesis citation. Phase 5 generation should be informed by this vocabulary.

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
| Do Nothing Anchor Table (6 fields) | Phase 4 | All 6 fields present; Challenge Binding col |
| Anchor citation vocabulary: Costs, Benefits, Competitive Threshold, Bypasses, Preserves | Phase 4 | These exact field label strings declared in Phase 4 and available as citation vocabulary for Phase 6 Anchor Citation column |
| Category Architecture Table | Phase 3 | Category labels and slot budgets |

**Vocabulary awareness**: The anchor field labels — Costs, Benefits, Competitive Threshold, Bypasses, Preserves — are now available. When writing pitches, candidates whose pitches gesture toward displacing any of these anchor dimensions are well-positioned for Phase 6 Anchor Citation annotation. No Anchor Citation is written in Phase 5 — only Name + Pitch.

Generate 22–38 Name+Pitch pairs only. No categories, rationales, anchor citations. No `**` — BREACH-FATAL.

| # | Name | Pitch (one line) |
|---|------|-----------------|

EXIT TABLE — Phase 5
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| 20–40 candidate rows (Name + Pitch only) | BREACH-MAJOR |
| No categories, rationales, anchor citations, or `**` assigned | BREACH-MINOR if present |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6 — CLUSTER + ANCHOR CITATION + T-EVIDENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 6
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Diverge List | Phase 5 | 20–40 Name+Pitch rows; no categories or rationales |
| Category Architecture Table | Phase 3 | Category labels with slot budgets |
| Do Nothing Anchor Table + Citation Vocabulary | Phase 4 | 6 field labels: Costs, Benefits, Competitive Threshold, Bypasses, Preserves, Net Position |

**C-45 ORDERING CONSTRAINT: Anchor Citation is written before T-Evidence in every row.**

Phase 6 cluster column schema (Anchor Citation precedes T-Evidence — write Anchor Citation first, then derive T-Evidence):
| # | Name | Category | Rationale | Anchor Citation [write first] | T-Evidence [derived from Anchor Citation — write second] |

**Row-writing protocol:**
1. Write Rationale — topic-specific
2. **Write Anchor Citation** — cite Phase 4 label strings (Costs, Benefits, Competitive Threshold, Bypasses, Preserves, Net Position). Inline check: if none cited — rewrite Rationale to add one displacement claim, then enter Anchor Citation.
3. **Derive T-Evidence** — `T-1:[PASS/PARTIAL/FAIL]·T-2:[PASS/PARTIAL/FAIL]·T-3:[dims cleared]·T-4:[PASS/PARTIAL/FAIL]`. T-3 dims cleared derived from Anchor Citation.

Concentration check: any category at 40% — redistribute (BREACH-MAJOR).

EXIT TABLE — Phase 6
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Anchor Citation col present; Phase 4 labels; ≤1/3 blank | BREACH-MAJOR if col absent; BREACH-MINOR if <1/3 blank |
| Anchor Citation written before T-Evidence per C-45 | BREACH-MINOR if ordering violated |
| T-Evidence col; structured notation on every row | BREACH-MAJOR if col absent |
| No category ≥40% | BREACH-MAJOR |
| All Phase 5 candidates present | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — EVIDENCE TRIAGE
(adjudication of pre-declared Phase 6 claims)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 7 (Evidence Triage)
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Cluster Table — Anchor Citation col | Phase 6 | Anchor Citation col present; ≤1/3 blank; written before T-Evidence |
| Cluster Table — T-Evidence col | Phase 6 | Structured notation on all rows |
| Do Nothing Anchor Table | Phase 4 | 6 fields; Challenge Binding col |
| Table 1A (T-3 Adjudication Protocol) | Phase 1 | T-3 schema locked; adjudication protocol declared |

Load Phase 6 evidence. Ph6 Anchor Citation is first data column. Do not mark `**` — BREACH-FATAL.

Column schema (Ph6 Anchor Citation FIRST):
`| # | Name | Ph6 Anchor Citation | Ph6 Pre-Score | T-1: Differentiation | T-2: Topic Fit | T-3: Costs | T-3: Benefits | T-3: Competitive Threshold | T-3: Bypasses | T-3: Preserves | T-4: Category Coverage | Verdict |`

EXIT TABLE — Phase 7
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Ph6 Anchor Citation col present as FIRST data col | BREACH-MAJOR |
| Ph6 Pre-Score col present | BREACH-MAJOR |
| T-3 via 5 separate anchor-named cols | BREACH-MAJOR if merged |
| No `**` assigned | BREACH-FATAL if present |
| All candidates evaluated with Verdict | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 8 — MARK + FINALIZE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 8
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 7 Evidence Triage Table | Phase 7 | All candidates evaluated; Ph6 Anchor Citation (first col); Ph6 Pre-Score; 5 T-3 cols; no `**` |
| Table 1A (Survival Threshold) | Phase 1 | All 4 tests PASS required |

Apply `**` to exactly 5 entries in Phase 6 cluster table. Top-5 must span ≥3 categories.

EXIT TABLE — Phase 8
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Exactly 5 `**` marks | BREACH-FATAL |
| `**` set spans ≥3 categories | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9A — TERMINAL LEDGER AUDIT (Reconstruct → Assess)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 9A
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 8 Output | Phase 8 | Exactly 5 `**` marks on Cluster Table |
| Phase 7 Evidence Triage Table | Phase 7 | Ph6 Anchor Citation (first col) + Ph6 Pre-Score + 5 T-3 cols |
| Phase 6 Cluster Table | Phase 6 | Anchor Citation + T-Evidence cols |
| All contributing phases (3–7) | Phases 3–7 | Exit tables completed |

Phase 9B may not begin until Phase 9A complete and all ledger rows COMPLETE.

**RECONSTRUCT PASS**:

| Phase | Obligation | What Was Actually Produced | COMPLETE? |
|-------|-----------|---------------------------|-----------|
| Phase 3 | AMEND Source + Primary Challenge Test cols | [col names; row count] | Y/N |
| Phase 4 | Challenge Binding col + citation vocabulary | [col present; 6 labels declared] | Y/N |
| Phase 5 | Name + Pitch | [row count; blanks] | Y/N |
| Phase 6 T-Evidence | Structured notation | [format; blank count] | Y/N |
| Phase 6 Anchor Citation | Anchor Citation col; labels; ordering | [col present; label examples (3); blank count; Anchor Citation before T-Evidence: Y/N] | Y/N |
| Phase 7 | Ph6 Anchor Citation (first col) + Ph6 Pre-Score + T-3 cols | **T-3 headers observed: [enumerate each T-3-prefixed header exactly]** Expected: T-3: Costs / T-3: Benefits / T-3: Competitive Threshold / T-3: Bypasses / T-3: Preserves. Match: [MATCH/MISMATCH each]. C-27 verdict. Ph6 Anchor Citation first col: Y/N | Y/N |

**ASSESS PASS**:

| Ledger Row | Status | Declared Severity | Action Required |
|-----------|--------|-------------------|----------------|
| Phase 3 architecture | | | |
| Phase 4 anchor | | | |
| Phase 5 diverge | | | |
| Phase 6 T-Evidence | | | |
| Phase 6 Anchor Citation | | | |
| Phase 7 evidence triage | | | |

EXIT TABLE — Phase 9A
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Reconstruct pass: 6 rows complete | BREACH-MAJOR |
| T-3 headers enumerated; C-27 verdict rendered | BREACH-MAJOR |
| Phase 6 Anchor Citation ordering confirmed | BREACH-MINOR |
| Ph6 Anchor Citation confirmed as first data col in Phase 7 | BREACH-MAJOR |
| Assess pass: Declared Severity populated | BREACH-MAJOR |
| All 6 ledger rows COMPLETE | BREACH-FATAL |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9B — CRITERION CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 9B
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 9A Terminal Ledger Audit | Phase 9A | Reconstruct + Assess complete; all 6 ledger rows COMPLETE; C-27 verdict rendered |

| Row | Criterion | Status | Severity if FAIL |
|-----|-----------|--------|-----------------|
| 1 | Candidate count 20–40 | PASS/FAIL | BREACH-MAJOR |
| 2 | Every candidate: all 4 anatomy fields | PASS/FAIL | BREACH-MAJOR |
| 3 | Exactly 5 `**` marks | PASS/FAIL | BREACH-FATAL |
| 4 | Do Nothing: 6 fields incl. Net Position | PASS/FAIL | BREACH-MAJOR |
| 5 | AMEND: 3 adjustments; dimension + downstream effect | PASS/FAIL | BREACH-MINOR |
| 6 | Architecture: AMEND Source col; all rows | PASS/FAIL | BREACH-MAJOR |
| 7 | Architecture: Primary Challenge Test col; ≥1 row T-3 | PASS/FAIL | BREACH-MAJOR |
| 8 | Phase 6: T-Evidence structured notation | PASS/FAIL | BREACH-MAJOR |
| 9 | Phase 7: Ph6 Pre-Score carryforward col | PASS/FAIL | BREACH-MAJOR |
| 10 | `**` set spans ≥3 categories | PASS/FAIL | BREACH-MAJOR |
| 11 | Phase 4 Challenge Binding col; Net Position → T-3 synthesis | PASS/FAIL | BREACH-MAJOR |
| 12 | Table 1C: all 3 BREACH tiers | PASS/FAIL | BREACH-FATAL |
| 13 | Phase 9A Declared Severity col | PASS/FAIL | BREACH-MAJOR |
| 14 | Phase 7 T-3 via 5 separate anchor-named cols | PASS/FAIL | BREACH-MAJOR |
| 15 | Table 1B BREACH Tier col; all rows populated | PASS/FAIL | BREACH-MAJOR |
| 16 | Phase 9A Reconstruct T-3 step; C-27 verdict | PASS/FAIL | BREACH-MAJOR |
| 17 | Phase 6 Anchor Citation col present; ≤1/3 blank | PASS/FAIL | BREACH-MAJOR if absent |
| 18 | Phase 7 Ph6 Anchor Citation col as FIRST data col | PASS/FAIL | BREACH-MAJOR |
| 19 | Phase 6 ordering annotation present (C-45); row protocol sequenced | PASS/FAIL | BREACH-MINOR |
| 20 | Phase 5 ENTRY TABLE vocabulary row: labels Costs/Benefits/Competitive Threshold/Bypasses/Preserves enumerated by name | PASS/FAIL | BREACH-MINOR |

EXIT TABLE — Phase 9B
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| All 20 rows checked | BREACH-MINOR |
| All FAIL rows corrected | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WRITE — ARTIFACT ASSEMBLY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — WRITE
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 9B Criterion Checklist | Phase 9B | All 20 rows PASS or corrected |
| Cluster Table with `**` marks | Phase 8 | Exactly 5 `**` marks |
| AMEND Adjustments Table | Phase 2 | 3 adjustments |
| Do Nothing Anchor Table | Phase 4 | 6 fields |

Write to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

Structure: Title → AMEND (A1/A2/A3) → Do Nothing (costs, benefits, net position) → Category sections; `**` on top-5; each entry: Name — Pitch — Rationale.
```

---

## V-03 — Single-axis: C-35 Affirmative Ledger Obligation Bullets

**Variation axis:** Process emphasis — every contributing phase exit carries an explicit "Ledger obligation satisfied: [contribution]" bullet after the EXIT TABLE. This is structurally distinct from EXIT TABLE BREACH rows: BREACH rows enforce the violation side; the obligation bullet affirms the contribution side. All other elements match V-01 (C-43, C-44, C-45, C-46).

**Hypothesis:** All 5 R15 variations were PARTIAL on C-35 because they had EXIT TABLE BREACH rows naming consequences for missing ledger fields, but no separate affirmative statement confirming what was contributed. The C-35 pass condition explicitly distinguishes these: "EXIT TABLE BREACH rows satisfy the violation side but not the affirmative declaration." The fix is a named "Ledger obligation satisfied: [description]" bullet placed after the EXIT TABLE at every contributing phase — Phases 3, 4, 5, 6, and 7. This makes evidence-ledger maintenance a first-class exit criterion while the EXIT TABLE continues to satisfy C-44.

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
| T-3 | Inertia Displacement — adjudicated from Ph6 Anchor Citation | PASS on >=3 of 5 anchor fields; evidence from Ph6 Anchor Citation | **Five columns:** "T-3: Costs" / "T-3: Benefits" / "T-3: Competitive Threshold" / "T-3: Bypasses" / "T-3: Preserves" — exact labels locked | >=3 PASS cells; adjudicates pre-declared claims |
| T-4 | Category Coverage | Candidate's category absent from other 4 `**` picks | "T-4: Category Coverage" | Removing collapses top-5 below 3 categories |

T-3 adjudication protocol (locked): read Ph6 Anchor Citation first; adjudicate present labels; assess implicit support for absent labels. Schema LOCKED — deviation BREACH-MAJOR. Framework LOCKED — modification BREACH-FATAL.

#### Table 1B — Ledger Contract

| Phase | Phase Name | Ledger Field | Violation Condition | BREACH Tier | Correction Action | Continue? |
|-------|-----------|--------------|---------------------|-------------|-------------------|-----------|
| 3 | Architecture | AMEND Source + Primary Challenge Test cols on every row | Any row missing either col | BREACH-MAJOR | Halt. Add col. Repopulate. | NO |
| 4 | Do Nothing Anchor | Challenge Binding col on every anchor row | Any row missing Challenge Binding | BREACH-MAJOR | Halt. Add col. Correct rows. | NO |
| 5 | Diverge | Name + Pitch on every candidate row | Missing Name or Pitch | BREACH-MINOR | Correct in-place. | YES |
| 6 | Cluster T-Evidence | T-Evidence col `T-1:[v]·T-2:[v]·T-3:[dims]·T-4:[v]` | Col absent; >1/3 unstructured | BREACH-MAJOR if absent | Halt; add; repopulate | NO |
| 6 | Cluster Anchor Citation | Anchor Citation col; >=1 label per row | Col absent; >1/3 blank | BREACH-MAJOR if absent; BREACH-MINOR if <1/3 blank | Absent: halt, add, repopulate. Blank: rewrite inline. | NO if absent |
| 7 | Evidence Triage | Ph6 Anchor Citation (first) + Ph6 Pre-Score + T-3 5 locked cols | Missing first col; missing Pre-Score; merged T-3 | BREACH-FATAL if `**` pre-assigned; BREACH-MAJOR schema | Discard+restart / halt+reconstruct | NO |

#### Table 1C — BREACH Severity Taxonomy

| Severity | Definition | Correction Protocol | Continue? |
|----------|------------|---------------------|-----------|
| BREACH-MINOR | Recommended field absent; <1/3 rows missing; overlapping AMEND | Correct in-place; mark [corrected] | YES |
| BREACH-MAJOR | Required col absent; cap exceeded; count outside 20-40; T-3 deviated; Ph6 Anchor Citation not first | HALT; reconstruct; re-verify | NO |
| BREACH-FATAL | Candidates before Phase 1; `**` before Phase 7; anchor absent; framework modified | STOP; discard; restart | NO |

EXIT TABLE — Phase 1
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Table 1A: all 4 tests; T-3 names 5 labels; adjudication protocol declared | BREACH-FATAL |
| Table 1B: 6 obligation rows; BREACH Tier + Correction + Continue? cols populated | BREACH-MAJOR |
| Table 1C: all 3 tiers with correction protocols | BREACH-MAJOR |

**Ledger obligation satisfied:** Phase 1 — Challenge Framework (Table 1A), Ledger Contract (Table 1B), and BREACH Taxonomy (Table 1C) declared as co-equal pre-generation artifacts.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — AMEND ADJUSTMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 2
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Table 1A (Challenge Framework) | Phase 1 | T-1/T-2/T-3/T-4 declared; T-3 schema locked; adjudication protocol locked |
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
| Exactly 3 rows; all cols filled | BREACH-MINOR |
| Directions non-overlapping | BREACH-MINOR |
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

Rules: >=4 categories; largest <=40%; totals 20-40; AMEND Source + Primary Challenge Test on every row; >=1 row T-3. Largest >=40% — redistribute (BREACH-MAJOR).

EXIT TABLE — Phase 3
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| >=4 categories; % computed; no category >=40% | BREACH-MAJOR |
| AMEND Source col; all rows populated | BREACH-MAJOR |
| Primary Challenge Test col; >=1 row T-3 | BREACH-MAJOR |
| Total 20-40 | BREACH-MAJOR |

**Ledger obligation satisfied:** Phase 3 — Architecture Table produced with AMEND Source column (A1/A2/A3 on every row) and Primary Challenge Test column (T-1/T-2/T-3/T-4 on every row, >=1 T-3 row).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — DO NOTHING ANCHOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 4
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Category Architecture Table | Phase 3 | >=4 categories; AMEND Source + Primary Challenge Test cols; >=1 T-3 row; <=40% cap |
| AMEND Adjustments Table | Phase 2 | 3 rows |

Write the Do Nothing anchor grounded in Phase 3 architecture. Bypasses + Preserves must name specific Phase 3 category labels.

| Field | Content | Challenge Binding |
|-------|---------|-------------------|
| Costs | | T-3 |
| Benefits | | T-3 |
| Competitive Threshold | [reference >=1 Phase 3 category] | T-3 |
| Bypasses | [name >=1 Phase 3 category label] | T-3 |
| Preserves | | T-3 |
| Net Position | [integrated judgment; displacement condition] | T-3 synthesis |

Anchor Citation vocabulary for Phase 6: Costs, Benefits, Competitive Threshold, Bypasses, Preserves, Net Position.

EXIT TABLE — Phase 4
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| All 6 field rows with `{{topic}}`-specific content | BREACH-MAJOR |
| Challenge Binding col; all rows populated | BREACH-MAJOR |
| Costs AND Benefits both present | BREACH-MINOR |
| Bypasses + Preserves name Phase 3 labels | BREACH-MINOR |
| Net Position names displacement condition | BREACH-MINOR |

**Ledger obligation satisfied:** Phase 4 — Do Nothing Anchor Table produced with Challenge Binding column on all 6 rows; Net Position maps to T-3 synthesis; anchor citation vocabulary declared.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5 — DIVERGE (Name + Pitch Only)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 5
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Do Nothing Anchor Table (6 fields) | Phase 4 | All 6 fields; Challenge Binding col |
| Category Architecture Table | Phase 3 | Category labels and slot budgets |

Generate 22-38 Name+Pitch pairs only. No categories, rationales, anchor citations. No `**` — BREACH-FATAL.

| # | Name | Pitch (one line) |
|---|------|-----------------|

EXIT TABLE — Phase 5
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| 20-40 candidate rows (Name + Pitch only) | BREACH-MAJOR |
| No categories, rationales, or `**` assigned | BREACH-MINOR if present |

**Ledger obligation satisfied:** Phase 5 — Diverge List produced with Name and Pitch on every candidate row; count within 20-40; no premature annotations.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6 — CLUSTER + ANCHOR CITATION + T-EVIDENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 6
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Diverge List | Phase 5 | 20-40 Name+Pitch rows |
| Category Architecture Table | Phase 3 | Category labels with slot budgets |
| Do Nothing Anchor Table + Citation Vocabulary | Phase 4 | 6 field labels: Costs, Benefits, Competitive Threshold, Bypasses, Preserves, Net Position |

**C-45 ORDERING CONSTRAINT: Anchor Citation precedes T-Evidence in every row.**

Phase 6 cluster column schema (Anchor Citation precedes T-Evidence — write Anchor Citation first, then derive T-Evidence):
| # | Name | Category | Rationale | Anchor Citation [write first] | T-Evidence [derived — write second] |

Row protocol: (1) Write Rationale; (2) Write Anchor Citation (Phase 4 label strings; if none cited — rewrite Rationale); (3) Derive T-Evidence from Anchor Citation. T-Evidence: `T-1:[v]·T-2:[v]·T-3:[dims]·T-4:[v]`.

Concentration check: any category at 40% — redistribute (BREACH-MAJOR).

EXIT TABLE — Phase 6
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Anchor Citation col present; <=1/3 blank | BREACH-MAJOR if absent; BREACH-MINOR if <1/3 blank |
| Anchor Citation written before T-Evidence per C-45 | BREACH-MINOR if ordering violated |
| T-Evidence col; structured notation | BREACH-MAJOR if absent |
| No category >=40% | BREACH-MAJOR |
| All Phase 5 candidates present | BREACH-MAJOR |

**Ledger obligation satisfied:** Phase 6 — Cluster Table produced with (a) Anchor Citation column using Phase 4 label strings, written before T-Evidence per C-45 ordering constraint; (b) T-Evidence column with structured notation on all candidate rows.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — EVIDENCE TRIAGE
(adjudication of pre-declared Phase 6 claims)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 7 (Evidence Triage)
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Cluster Table — Anchor Citation col | Phase 6 | Anchor Citation col present; <=1/3 blank; written before T-Evidence |
| Cluster Table — T-Evidence col | Phase 6 | Structured notation on all rows |
| Do Nothing Anchor Table | Phase 4 | 6 fields; Challenge Binding col |
| Table 1A (T-3 Adjudication Protocol) | Phase 1 | Schema locked; adjudication protocol declared |

Load Phase 6 evidence. Ph6 Anchor Citation is FIRST data column. Do not mark `**` — BREACH-FATAL.

Column schema:
| # | Name | Ph6 Anchor Citation | Ph6 Pre-Score | T-1: Differentiation | T-2: Topic Fit | T-3: Costs | T-3: Benefits | T-3: Competitive Threshold | T-3: Bypasses | T-3: Preserves | T-4: Category Coverage | Verdict |

EXIT TABLE — Phase 7
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Ph6 Anchor Citation col present as FIRST data col | BREACH-MAJOR |
| Ph6 Pre-Score col present | BREACH-MAJOR |
| T-3 via 5 separate anchor-named cols | BREACH-MAJOR if merged |
| No `**` assigned | BREACH-FATAL if present |
| All candidates evaluated | BREACH-MAJOR |

**Ledger obligation satisfied:** Phase 7 — Evidence Triage Table produced with Ph6 Anchor Citation as first data column, Ph6 Pre-Score carryforward column, and T-3 evaluated via 5 separate anchor-named columns (T-3: Costs / T-3: Benefits / T-3: Competitive Threshold / T-3: Bypasses / T-3: Preserves) on all rows.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 8 — MARK + FINALIZE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 8
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 7 Evidence Triage Table | Phase 7 | All evaluated; Ph6 Anchor Citation first; Ph6 Pre-Score; 5 T-3 cols; no `**` |
| Table 1A (Survival Threshold) | Phase 1 | All 4 tests PASS required |

Apply `**` to exactly 5 entries in Phase 6 cluster table. Top-5 must span >=3 categories.

EXIT TABLE — Phase 8
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Exactly 5 `**` marks | BREACH-FATAL |
| `**` set spans >=3 categories | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9A — TERMINAL LEDGER AUDIT (Reconstruct -> Assess)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 9A
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 8 Output | Phase 8 | Exactly 5 `**` marks |
| Phase 7 Evidence Triage Table | Phase 7 | Ph6 Anchor Citation first + Ph6 Pre-Score + 5 T-3 cols |
| Phase 6 Cluster Table | Phase 6 | Anchor Citation + T-Evidence cols |
| Contributing phases 3-7 | Phases 3-7 | Exit tables + ledger obligation bullets completed |

Phase 9B may not begin until Phase 9A complete and all ledger rows COMPLETE.

**RECONSTRUCT PASS**:

| Phase | Obligation | What Was Actually Produced | COMPLETE? |
|-------|-----------|---------------------------|-----------|
| Phase 3 | AMEND Source + Primary Challenge Test cols + obligation bullet | [col names; row count; bullet text] | Y/N |
| Phase 4 | Challenge Binding col + obligation bullet | [col present; Net Position -> T-3 synthesis; bullet text] | Y/N |
| Phase 5 | Name + Pitch + obligation bullet | [row count; bullet text] | Y/N |
| Phase 6 T-Evidence | Structured notation + obligation bullet | [format; blank count; bullet text] | Y/N |
| Phase 6 Anchor Citation | Anchor Citation col; C-45 ordering + obligation bullet | [col present; label examples; Anchor Citation before T-Evidence: Y/N; bullet text] | Y/N |
| Phase 7 | Ph6 Anchor Citation first + Ph6 Pre-Score + T-3 cols + obligation bullet | **T-3 headers observed: [enumerate each exactly]** Expected: T-3: Costs / T-3: Benefits / T-3: Competitive Threshold / T-3: Bypasses / T-3: Preserves. Match: [MATCH/MISMATCH each]. C-27 verdict. Ph6 Anchor Citation first col: Y/N. Obligation bullet text. | Y/N |

**ASSESS PASS**:

| Ledger Row | Status | Declared Severity | Action Required |
|-----------|--------|-------------------|----------------|
| Phase 3 architecture | | | |
| Phase 4 anchor | | | |
| Phase 5 diverge | | | |
| Phase 6 T-Evidence | | | |
| Phase 6 Anchor Citation | | | |
| Phase 7 evidence triage | | | |

EXIT TABLE — Phase 9A
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Reconstruct pass: 6 rows complete | BREACH-MAJOR |
| T-3 headers enumerated; C-27 verdict rendered | BREACH-MAJOR |
| Phase 6 Anchor Citation ordering confirmed (before T-Evidence: Y/N) | BREACH-MINOR |
| Ph6 Anchor Citation confirmed as first data col in Phase 7 | BREACH-MAJOR |
| Obligation bullet text recorded for all contributing phases | BREACH-MAJOR |
| Assess pass: Declared Severity populated | BREACH-MAJOR |
| All 6 ledger rows COMPLETE | BREACH-FATAL |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9B — CRITERION CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 9B
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 9A Terminal Ledger Audit | Phase 9A | Reconstruct + Assess complete; all 6 ledger rows COMPLETE; C-27 verdict; obligation bullets verified |

| Row | Criterion | Status | Severity if FAIL |
|-----|-----------|--------|-----------------|
| 1 | Candidate count 20-40 | PASS/FAIL | BREACH-MAJOR |
| 2 | Every candidate: all 4 anatomy fields | PASS/FAIL | BREACH-MAJOR |
| 3 | Exactly 5 `**` marks | PASS/FAIL | BREACH-FATAL |
| 4 | Do Nothing: 6 fields incl. Net Position | PASS/FAIL | BREACH-MAJOR |
| 5 | AMEND: 3 adjustments; dimension + downstream effect | PASS/FAIL | BREACH-MINOR |
| 6 | Architecture: AMEND Source col | PASS/FAIL | BREACH-MAJOR |
| 7 | Architecture: Primary Challenge Test col; >=1 row T-3 | PASS/FAIL | BREACH-MAJOR |
| 8 | Phase 6: T-Evidence structured notation | PASS/FAIL | BREACH-MAJOR |
| 9 | Phase 7: Ph6 Pre-Score carryforward col | PASS/FAIL | BREACH-MAJOR |
| 10 | `**` set spans >=3 categories | PASS/FAIL | BREACH-MAJOR |
| 11 | Phase 4 Challenge Binding col; Net Position -> T-3 synthesis | PASS/FAIL | BREACH-MAJOR |
| 12 | Table 1C: all 3 BREACH tiers | PASS/FAIL | BREACH-FATAL |
| 13 | Phase 9A Declared Severity col | PASS/FAIL | BREACH-MAJOR |
| 14 | Phase 7 T-3 via 5 separate anchor-named cols | PASS/FAIL | BREACH-MAJOR |
| 15 | Table 1B BREACH Tier col; all rows | PASS/FAIL | BREACH-MAJOR |
| 16 | Phase 9A Reconstruct T-3 step; C-27 verdict | PASS/FAIL | BREACH-MAJOR |
| 17 | Phase 6 Anchor Citation col present; <=1/3 blank | PASS/FAIL | BREACH-MAJOR if absent |
| 18 | Phase 7 Ph6 Anchor Citation col as FIRST data col | PASS/FAIL | BREACH-MAJOR |
| 19 | Phase 6 ordering annotation present (C-45) | PASS/FAIL | BREACH-MINOR |
| 20 | Every contributing phase (3,4,5,6,7) has "Ledger obligation satisfied: [contribution]" bullet (C-35) | PASS/FAIL | BREACH-MAJOR if any missing |

EXIT TABLE — Phase 9B
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| All 20 rows checked | BREACH-MINOR |
| All FAIL rows corrected | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WRITE — ARTIFACT ASSEMBLY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — WRITE
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 9B Criterion Checklist | Phase 9B | All 20 rows PASS or corrected |
| Cluster Table with `**` marks | Phase 8 | Exactly 5 `**` marks |
| AMEND Adjustments Table | Phase 2 | 3 adjustments |
| Do Nothing Anchor Table | Phase 4 | 6 fields |

Write to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

Structure: Title -> AMEND (A1/A2/A3) -> Do Nothing (costs, benefits, net position) -> Category sections; `**` on top-5; each entry: Name — Pitch — Rationale.
```

---

## V-04 — Combined: C-45 + C-48 (Ordering Annotation + Vocabulary Gate)

**Variation axes:** C-45 (Phase 6 column schema ordering annotation) combined with C-48 (Phase 5 ENTRY TABLE vocabulary row enumerating all 5 anchor field labels by name). V-01 establishes C-45; V-02 establishes C-48; V-04 tests whether they compose cleanly. Both changes operate at different phase boundaries and have no structural conflict: C-48 gates Phase 5 on vocabulary availability; C-45 enforces ordering within Phase 6 generation. Together they create an end-to-end vocabulary pipeline: vocabulary declared in Phase 4, gated in Phase 5 ENTRY TABLE with named labels, enforced in Phase 6 schema ordering.

**Hypothesis:** C-45 ensures displacement evidence is committed before challenge-readiness annotation at the cell level. C-48 ensures the vocabulary for that displacement evidence is actively in context from before the first candidate pitch is written. When both are active, the prompt creates a three-stage vocabulary discipline: Phase 4 declares the labels, Phase 5 ENTRY TABLE names them as a precondition, and Phase 6 enforces their citation order relative to T-Evidence. No retrofitting at any stage.

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
| T-1 | Differentiation | Meaningfully distinct mechanism from every other `**` candidate | "T-1: Differentiation" | Removing eliminates approach not covered by remaining 4 |
| T-2 | Topic Fit | Rationale names a specific dimension of `{{topic}}` | "T-2: Topic Fit" | Rationale fails if topic swapped |
| T-3 | Inertia Displacement — adjudicated from Ph6 Anchor Citation | PASS on >=3 of 5 anchor fields; evidence from Ph6 Anchor Citation | **Five columns:** "T-3: Costs" / "T-3: Benefits" / "T-3: Competitive Threshold" / "T-3: Bypasses" / "T-3: Preserves" — exact labels locked | >=3 PASS cells; adjudicates pre-declared claims |
| T-4 | Category Coverage | Category absent from other 4 `**` picks | "T-4: Category Coverage" | Removing collapses top-5 below 3 categories |

T-3 adjudication protocol (locked): read Ph6 Anchor Citation first; adjudicate present labels; assess implicit for absent. Schema LOCKED — deviation BREACH-MAJOR. Framework LOCKED — modification BREACH-FATAL.

#### Table 1B — Ledger Contract

| Phase | Phase Name | Ledger Field | Violation Condition | BREACH Tier | Correction | Continue? |
|-------|-----------|--------------|---------------------|-------------|------------|-----------|
| 3 | Architecture | AMEND Source + Primary Challenge Test cols | Any row missing either col | BREACH-MAJOR | Halt; add col; repopulate | NO |
| 4 | Do Nothing Anchor | Challenge Binding col on every row | Any row missing | BREACH-MAJOR | Halt; add col; correct rows | NO |
| 5 | Diverge | Name + Pitch on every row | Missing Name or Pitch | BREACH-MINOR | Correct in-place | YES |
| 6 | Cluster T-Evidence | T-Evidence col `T-1:[v]*T-2:[v]*T-3:[dims]*T-4:[v]` | Col absent; >1/3 unstructured | BREACH-MAJOR if absent | Halt; add; repopulate | NO |
| 6 | Cluster Anchor Citation | Anchor Citation col; >=1 label per row; before T-Evidence | Col absent; >1/3 blank | BREACH-MAJOR if absent; BREACH-MINOR if <1/3 blank | Absent: halt, add, repopulate | NO if absent |
| 7 | Evidence Triage | Ph6 Anchor Citation (first col) + Ph6 Pre-Score + T-3 5 cols | Missing first col; missing Pre-Score; merged T-3 | BREACH-FATAL if `**` pre-assigned; BREACH-MAJOR schema | Discard+restart / halt+reconstruct | NO |

#### Table 1C — BREACH Taxonomy

| Severity | Definition | Correction | Continue? |
|----------|------------|------------|-----------|
| BREACH-MINOR | Recommended field absent; <1/3 rows missing; overlapping AMEND | Correct in-place; mark [corrected] | YES |
| BREACH-MAJOR | Required col absent; cap exceeded; count outside 20-40; T-3 deviated; Ph6 Anchor Citation not first | HALT; reconstruct; re-verify | NO |
| BREACH-FATAL | Candidates before Phase 1; `**` before Phase 7; anchor absent; framework modified | STOP; discard; restart | NO |

EXIT TABLE — Phase 1
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Table 1A: all 4 tests; T-3 names 5 labels; adjudication protocol declared | BREACH-FATAL |
| Table 1B: 6 obligation rows; BREACH Tier + Correction + Continue? cols populated | BREACH-MAJOR |
| Table 1C: all 3 tiers | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — AMEND ADJUSTMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 2
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Table 1A | Phase 1 | T-1/T-2/T-3/T-4 declared; T-3 schema locked; adjudication protocol locked |
| Table 1B | Phase 1 | 6 obligation rows; BREACH Tier col populated |
| Table 1C | Phase 1 | 3 severity tiers |

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
| Directions non-overlapping | BREACH-MINOR |
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

Rules: >=4 categories; largest <=40%; totals 20-40; AMEND Source + Primary Challenge Test every row; >=1 T-3. Largest >=40% — redistribute (BREACH-MAJOR).

EXIT TABLE — Phase 3
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| >=4 categories; % computed; no category >=40% | BREACH-MAJOR |
| AMEND Source col; all rows | BREACH-MAJOR |
| Primary Challenge Test col; >=1 row T-3 | BREACH-MAJOR |
| Total 20-40 | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — DO NOTHING ANCHOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 4
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Category Architecture Table | Phase 3 | >=4 categories; AMEND Source + Primary Challenge Test; >=1 T-3; <=40% cap |
| AMEND Adjustments Table | Phase 2 | 3 rows |

| Field | Content | Challenge Binding |
|-------|---------|-------------------|
| Costs | | T-3 |
| Benefits | | T-3 |
| Competitive Threshold | [reference >=1 Phase 3 category] | T-3 |
| Bypasses | [name >=1 Phase 3 category label] | T-3 |
| Preserves | | T-3 |
| Net Position | [integrated judgment; displacement condition] | T-3 synthesis |

**Anchor Citation vocabulary (declared for Phase 5 and Phase 6)**: The 5 displacement labels — Costs, Benefits, Competitive Threshold, Bypasses, Preserves — plus Net Position are the citation vocabulary. Exact strings required in Phase 6 Anchor Citation column.

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
| Do Nothing Anchor Table (6 fields) | Phase 4 | All 6 fields; Challenge Binding col |
| Anchor citation vocabulary: Costs, Benefits, Competitive Threshold, Bypasses, Preserves | Phase 4 | These exact 5 field label strings declared in Phase 4 and available as citation vocabulary for Phase 6 Anchor Citation column |
| Category Architecture Table | Phase 3 | Category labels and slot budgets |

Vocabulary awareness: anchor labels Costs, Benefits, Competitive Threshold, Bypasses, Preserves are available. Pitches may gesture toward displacing these dimensions. No Anchor Citation written in Phase 5 — only Name + Pitch.

Generate 22-38 Name+Pitch pairs only. No categories, rationales, anchor citations. No `**` — BREACH-FATAL.

| # | Name | Pitch (one line) |
|---|------|-----------------|

EXIT TABLE — Phase 5
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| 20-40 rows (Name + Pitch only) | BREACH-MAJOR |
| No categories, rationales, or `**` | BREACH-MINOR if present |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6 — CLUSTER + ANCHOR CITATION + T-EVIDENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 6
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Diverge List | Phase 5 | 20-40 Name+Pitch rows |
| Category Architecture Table | Phase 3 | Category labels with slot budgets |
| Do Nothing Anchor Table + Citation Vocabulary | Phase 4 | 6 field labels: Costs, Benefits, Competitive Threshold, Bypasses, Preserves, Net Position |

**C-45 ORDERING CONSTRAINT: Anchor Citation is written before T-Evidence in every row. This ordering is enforced at the column schema level — T-Evidence derives from Anchor Citation and must come after it.**

Phase 6 cluster column schema (Anchor Citation precedes T-Evidence — write Anchor Citation first, then derive T-Evidence):
| # | Name | Category | Rationale | Anchor Citation [write first] | T-Evidence [derived from Anchor Citation — write second] |

Row-writing protocol:
1. Write Rationale (topic-specific)
2. Write Anchor Citation — cite Phase 4 label strings (Costs, Benefits, Competitive Threshold, Bypasses, Preserves, Net Position). Inline check: if none — rewrite Rationale to add one displacement claim, then enter Anchor Citation.
3. Derive T-Evidence from Anchor Citation: `T-1:[v]*T-2:[v]*T-3:[dims]*T-4:[v]`. T-3 dims = anchor field labels where Rationale demonstrates superiority.

Concentration check: any category at 40% — redistribute (BREACH-MAJOR).

EXIT TABLE — Phase 6
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Anchor Citation col present; Phase 4 labels; <=1/3 blank | BREACH-MAJOR if absent; BREACH-MINOR if <1/3 blank |
| Anchor Citation written before T-Evidence per C-45 | BREACH-MINOR if ordering violated |
| T-Evidence col; structured notation | BREACH-MAJOR if absent |
| No category >=40% | BREACH-MAJOR |
| All Phase 5 candidates present | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — EVIDENCE TRIAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 7 (Evidence Triage)
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Cluster Table — Anchor Citation col | Phase 6 | Present; <=1/3 blank; written before T-Evidence per C-45 |
| Cluster Table — T-Evidence col | Phase 6 | Structured notation all rows |
| Do Nothing Anchor Table | Phase 4 | 6 fields; Challenge Binding col |
| Table 1A | Phase 1 | T-3 schema locked; adjudication protocol declared |

Load Phase 6 evidence. Ph6 Anchor Citation is FIRST data column. Do not mark `**` — BREACH-FATAL.

Column schema (Ph6 Anchor Citation FIRST):
| # | Name | Ph6 Anchor Citation | Ph6 Pre-Score | T-1: Differentiation | T-2: Topic Fit | T-3: Costs | T-3: Benefits | T-3: Competitive Threshold | T-3: Bypasses | T-3: Preserves | T-4: Category Coverage | Verdict |

EXIT TABLE — Phase 7
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Ph6 Anchor Citation col as FIRST data col | BREACH-MAJOR |
| Ph6 Pre-Score col present | BREACH-MAJOR |
| T-3 via 5 separate anchor-named cols | BREACH-MAJOR if merged |
| No `**` assigned | BREACH-FATAL if present |
| All candidates evaluated | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 8 — MARK + FINALIZE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 8
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 7 Evidence Triage Table | Phase 7 | Evaluated; Ph6 Anchor Citation first; Ph6 Pre-Score; 5 T-3; no `**` |
| Table 1A | Phase 1 | All 4 tests PASS required |

Apply `**` to exactly 5 entries in Phase 6 cluster table. Top-5 spans >=3 categories.

EXIT TABLE — Phase 8
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Exactly 5 `**` marks | BREACH-FATAL |
| `**` set spans >=3 categories | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9A — TERMINAL LEDGER AUDIT (Reconstruct -> Assess)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 9A
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 8 Output | Phase 8 | Exactly 5 `**` |
| Phase 7 Evidence Triage Table | Phase 7 | Ph6 Anchor Citation first + Ph6 Pre-Score + 5 T-3 |
| Phase 6 Cluster Table | Phase 6 | Anchor Citation + T-Evidence; C-45 ordering applied |
| Contributing phases 3-7 | Phases 3-7 | Exit tables completed |

Phase 9B may not begin until Phase 9A complete and all ledger rows COMPLETE.

**RECONSTRUCT PASS**:

| Phase | Obligation | What Was Actually Produced | COMPLETE? |
|-------|-----------|---------------------------|-----------|
| Phase 3 | AMEND Source + Primary Challenge Test cols | [col names; row count] | Y/N |
| Phase 4 | Challenge Binding col + citation vocabulary | [col present; 6 labels declared] | Y/N |
| Phase 5 | Name + Pitch | [row count; blanks] | Y/N |
| Phase 6 T-Evidence | Structured notation | [format; blank count] | Y/N |
| Phase 6 Anchor Citation | Anchor Citation col; labels; C-45 ordering | [col present; label examples (3); blank count; Anchor Citation before T-Evidence: Y/N] | Y/N |
| Phase 7 | Ph6 Anchor Citation first + Ph6 Pre-Score + T-3 cols | **T-3 headers observed: [enumerate each exactly]** Expected: T-3: Costs / T-3: Benefits / T-3: Competitive Threshold / T-3: Bypasses / T-3: Preserves. Match: [MATCH/MISMATCH each]. C-27 verdict. Ph6 Anchor Citation first col: Y/N | Y/N |

**ASSESS PASS**:

| Ledger Row | Status | Declared Severity | Action Required |
|-----------|--------|-------------------|----------------|
| Phase 3 architecture | | | |
| Phase 4 anchor | | | |
| Phase 5 diverge | | | |
| Phase 6 T-Evidence | | | |
| Phase 6 Anchor Citation | | | |
| Phase 7 evidence triage | | | |

EXIT TABLE — Phase 9A
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Reconstruct pass: 6 rows | BREACH-MAJOR |
| T-3 headers enumerated; C-27 verdict | BREACH-MAJOR |
| Phase 6 ordering confirmed (Anchor Citation before T-Evidence: Y/N) | BREACH-MINOR |
| Ph6 Anchor Citation confirmed first in Phase 7 | BREACH-MAJOR |
| Assess pass: Declared Severity populated | BREACH-MAJOR |
| All 6 ledger rows COMPLETE | BREACH-FATAL |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9B — CRITERION CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 9B
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 9A | Phase 9A | Reconstruct + Assess complete; all 6 rows COMPLETE; C-27 verdict; Ph6 Anchor Citation ordering confirmed |

| Row | Criterion | Status | Severity if FAIL |
|-----|-----------|--------|-----------------|
| 1 | Count 20-40 | PASS/FAIL | BREACH-MAJOR |
| 2 | Every candidate: all 4 anatomy fields | PASS/FAIL | BREACH-MAJOR |
| 3 | Exactly 5 `**` | PASS/FAIL | BREACH-FATAL |
| 4 | Do Nothing: 6 fields | PASS/FAIL | BREACH-MAJOR |
| 5 | AMEND: 3 adjustments; dimension + downstream effect | PASS/FAIL | BREACH-MINOR |
| 6 | Architecture: AMEND Source col | PASS/FAIL | BREACH-MAJOR |
| 7 | Architecture: Primary Challenge Test; >=1 T-3 | PASS/FAIL | BREACH-MAJOR |
| 8 | Phase 6: T-Evidence structured notation | PASS/FAIL | BREACH-MAJOR |
| 9 | Phase 7: Ph6 Pre-Score col | PASS/FAIL | BREACH-MAJOR |
| 10 | `**` spans >=3 categories | PASS/FAIL | BREACH-MAJOR |
| 11 | Phase 4 Challenge Binding; Net Position -> T-3 synthesis | PASS/FAIL | BREACH-MAJOR |
| 12 | Table 1C: all 3 tiers | PASS/FAIL | BREACH-FATAL |
| 13 | Phase 9A Declared Severity col | PASS/FAIL | BREACH-MAJOR |
| 14 | Phase 7 T-3: 5 separate anchor-named cols | PASS/FAIL | BREACH-MAJOR |
| 15 | Table 1B BREACH Tier col; all rows | PASS/FAIL | BREACH-MAJOR |
| 16 | Phase 9A Reconstruct T-3 step; C-27 verdict | PASS/FAIL | BREACH-MAJOR |
| 17 | Phase 6 Anchor Citation col; <=1/3 blank | PASS/FAIL | BREACH-MAJOR if absent |
| 18 | Phase 7 Ph6 Anchor Citation as FIRST data col | PASS/FAIL | BREACH-MAJOR |
| 19 | Phase 6 ordering annotation (C-45); row protocol sequenced | PASS/FAIL | BREACH-MINOR |
| 20 | Phase 5 ENTRY TABLE vocabulary row: Costs/Benefits/Competitive Threshold/Bypasses/Preserves by name (C-48) | PASS/FAIL | BREACH-MINOR |

EXIT TABLE — Phase 9B
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| All 20 rows checked | BREACH-MINOR |
| All FAIL rows corrected | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WRITE — ARTIFACT ASSEMBLY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — WRITE
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 9B Checklist | Phase 9B | All 20 rows PASS or corrected |
| Cluster Table with `**` | Phase 8 | Exactly 5 `**` |
| AMEND Table | Phase 2 | 3 adjustments |
| Do Nothing Anchor Table | Phase 4 | 6 fields |

Write to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`
Structure: Title -> AMEND -> Do Nothing -> Category sections; `**` on top-5; Name — Pitch — Rationale.
```

---

## V-05 — Full Stack: C-45 + C-47 + C-48 + C-35

**Variation axes:** All four v15 criteria combined: C-45 (ordering annotation in cluster schema), C-47 (Phase 9A Reconstruct states observed column ordering for Phase 6), C-48 (Phase 5 ENTRY TABLE enumerates vocabulary labels by name), C-35 (affirmative ledger obligation bullets at every contributing phase). This variation is the maximal expression of the v15 rubric — all new criteria active simultaneously, plus the C-35 fix that all 5 R15 variations missed.

**Hypothesis:** C-47 is the key addition beyond V-04. V-05 R15's Reconstruct Phase 6 row said "confirm written before T-Evidence: Y/N" — a boolean confirmation. The C-47 pass condition requires stating the OBSERVED column ordering (e.g., "Anchor Citation is column 5, T-Evidence is column 6 — Anchor Citation precedes T-Evidence: CONFIRMED"), not just a yes/no. This is the same discipline C-42 applied to Phase 7 T-3 headers: enumerate what was actually observed, don't just confirm expectations. When all four criteria are active together, the prompt creates a complete evidence chain: vocabulary declared (Phase 4) -> vocabulary gated by name (Phase 5 ENTRY) -> citation ordered before verdict (Phase 6 schema) -> Phase 7 adjudicates ordered claims -> Reconstruct verifies both Phase 7 headers AND Phase 6 ordering state -> C-35 makes every contribution affirmative.

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
| T-1 | Differentiation | Meaningfully distinct mechanism from every other `**` candidate | "T-1: Differentiation" | Removing eliminates approach not covered by remaining 4 |
| T-2 | Topic Fit | Rationale names a specific dimension of `{{topic}}` | "T-2: Topic Fit" | Rationale fails if topic swapped |
| T-3 | Inertia Displacement — adjudicated from Ph6 Anchor Citation | PASS on >=3 of 5 anchor fields; evidence from Ph6 Anchor Citation | **Five columns:** "T-3: Costs" / "T-3: Benefits" / "T-3: Competitive Threshold" / "T-3: Bypasses" / "T-3: Preserves" — exact labels locked | >=3 PASS cells; adjudicates pre-declared claims |
| T-4 | Category Coverage | Category absent from other 4 `**` picks | "T-4: Category Coverage" | Removing collapses top-5 below 3 categories |

T-3 adjudication protocol (locked): read Ph6 Anchor Citation first; if label present adjudicate claim (PASS/PARTIAL/FAIL); if absent assess implicit. Schema LOCKED. Framework LOCKED — modification BREACH-FATAL.

#### Table 1B — Ledger Contract

| Phase | Phase Name | Ledger Field | Violation Condition | BREACH Tier | Correction | Continue? |
|-------|-----------|--------------|---------------------|-------------|------------|-----------|
| 3 | Architecture | AMEND Source + Primary Challenge Test cols | Any row missing either | BREACH-MAJOR | Halt; add; repopulate | NO |
| 4 | Do Nothing Anchor | Challenge Binding col on every row | Any row missing | BREACH-MAJOR | Halt; add; correct | NO |
| 5 | Diverge | Name + Pitch on every row | Missing Name or Pitch | BREACH-MINOR | Correct in-place | YES |
| 6 | Cluster T-Evidence | T-Evidence col `T-1:[v]*T-2:[v]*T-3:[dims]*T-4:[v]` | Col absent; >1/3 unstructured | BREACH-MAJOR if absent | Halt; add; repopulate | NO |
| 6 | Cluster Anchor Citation | Anchor Citation col; >=1 label; before T-Evidence | Col absent; >1/3 blank | BREACH-MAJOR if absent; BREACH-MINOR <1/3 | Absent: halt, add, repopulate | NO if absent |
| 7 | Evidence Triage | Ph6 Anchor Citation (first col) + Ph6 Pre-Score + T-3 5 locked cols | Missing first col; missing Pre-Score; merged T-3 | BREACH-FATAL if `**` pre-assigned; BREACH-MAJOR schema | Discard+restart / halt+reconstruct | NO |

#### Table 1C — BREACH Taxonomy

| Severity | Definition | Correction | Continue? |
|----------|------------|------------|-----------|
| BREACH-MINOR | Recommended field absent; <1/3 rows missing; overlapping AMEND | Correct in-place; mark [corrected] | YES |
| BREACH-MAJOR | Required col absent; cap exceeded; count outside 20-40; T-3 deviated; Ph6 Anchor Citation not first | HALT; reconstruct; re-verify | NO |
| BREACH-FATAL | Candidates before Phase 1; `**` before Phase 7; anchor absent; framework modified | STOP; discard; restart | NO |

EXIT TABLE — Phase 1
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Table 1A: all 4 tests; T-3 names 5 labels; adjudication protocol declared | BREACH-FATAL |
| Table 1B: 6 obligation rows; BREACH Tier + Correction + Continue? cols | BREACH-MAJOR |
| Table 1C: all 3 tiers | BREACH-MAJOR |

**Ledger obligation satisfied:** Phase 1 — Challenge Framework (Table 1A), Ledger Contract (Table 1B with BREACH Tier col on all 6 rows), and BREACH Taxonomy (Table 1C, 3 tiers) declared as co-equal pre-generation artifacts.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — AMEND ADJUSTMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 2
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Table 1A (Challenge Framework) | Phase 1 | T-1/T-2/T-3/T-4 declared; T-3 schema locked; adjudication protocol locked |
| Table 1B (Ledger Contract) | Phase 1 | 6 obligation rows; BREACH Tier col populated |
| Table 1C (BREACH Taxonomy) | Phase 1 | 3 severity tiers with correction protocols |

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
| Directions non-overlapping | BREACH-MINOR |
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

Rules: >=4 categories; largest <=40%; totals 20-40; AMEND Source + Primary Challenge Test every row; >=1 T-3.

EXIT TABLE — Phase 3
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| >=4 categories; % computed; no category >=40% | BREACH-MAJOR |
| AMEND Source col; all rows | BREACH-MAJOR |
| Primary Challenge Test col; >=1 row T-3 | BREACH-MAJOR |
| Total 20-40 | BREACH-MAJOR |

**Ledger obligation satisfied:** Phase 3 — Architecture Table produced with AMEND Source column (A1/A2/A3 every row) and Primary Challenge Test column (T-1/T-2/T-3/T-4 every row, >=1 T-3 row present).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — DO NOTHING ANCHOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 4
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Category Architecture Table | Phase 3 | >=4 categories; AMEND Source + Primary Challenge Test; >=1 T-3; <=40% cap |
| AMEND Adjustments Table | Phase 2 | 3 rows |

| Field | Content | Challenge Binding |
|-------|---------|-------------------|
| Costs | | T-3 |
| Benefits | | T-3 |
| Competitive Threshold | [reference >=1 Phase 3 category] | T-3 |
| Bypasses | [name >=1 Phase 3 category label] | T-3 |
| Preserves | | T-3 |
| Net Position | [integrated judgment; displacement condition] | T-3 synthesis |

**Anchor Citation vocabulary (declared for Phase 5 and Phase 6)**: The 5 displacement labels — Costs, Benefits, Competitive Threshold, Bypasses, Preserves — plus Net Position. These exact strings are the citation vocabulary. Phase 5 ENTRY TABLE gates on this vocabulary; Phase 6 must cite these strings by name.

EXIT TABLE — Phase 4
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| All 6 field rows with `{{topic}}`-specific content | BREACH-MAJOR |
| Challenge Binding col; all rows populated | BREACH-MAJOR |
| Costs AND Benefits both present | BREACH-MINOR |
| Bypasses + Preserves name Phase 3 labels | BREACH-MINOR |
| Net Position names displacement condition | BREACH-MINOR |

**Ledger obligation satisfied:** Phase 4 — Do Nothing Anchor Table produced with Challenge Binding column on all 6 rows; Net Position maps to T-3 synthesis; anchor citation vocabulary (Costs, Benefits, Competitive Threshold, Bypasses, Preserves, Net Position) declared for Phase 5 and Phase 6.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5 — DIVERGE (Name + Pitch Only)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 5
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Do Nothing Anchor Table (6 fields) | Phase 4 | All 6 fields; Challenge Binding col |
| Anchor citation vocabulary: Costs, Benefits, Competitive Threshold, Bypasses, Preserves | Phase 4 | These exact 5 field label strings declared in Phase 4 and available as citation vocabulary for Phase 6 Anchor Citation column |
| Category Architecture Table | Phase 3 | Category labels and slot budgets |

Vocabulary awareness: anchor field labels Costs, Benefits, Competitive Threshold, Bypasses, Preserves are available. Pitches may gesture toward displacing these dimensions. No Anchor Citation written in Phase 5 — only Name + Pitch.

Generate 22-38 Name+Pitch pairs only. No categories, rationales, anchor citations, T-Evidence. No `**` — BREACH-FATAL.

| # | Name | Pitch (one line) |
|---|------|-----------------|

EXIT TABLE — Phase 5
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| 20-40 rows (Name + Pitch only) | BREACH-MAJOR |
| No categories, rationales, or `**` | BREACH-MINOR if present |

**Ledger obligation satisfied:** Phase 5 — Diverge List produced with Name and Pitch on every candidate row (20-40 count); no premature annotation; anchor citation vocabulary available in context for Phase 6.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6 — CLUSTER + ANCHOR CITATION + T-EVIDENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 6
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Diverge List | Phase 5 | 20-40 Name+Pitch rows |
| Category Architecture Table | Phase 3 | Category labels with slot budgets |
| Do Nothing Anchor Table + Citation Vocabulary | Phase 4 | 6 field labels: Costs, Benefits, Competitive Threshold, Bypasses, Preserves, Net Position |

**C-45 ORDERING CONSTRAINT: Anchor Citation is written before T-Evidence in every row. This ordering is enforced at the column schema level — T-Evidence derives from Anchor Citation and must come after it.**

Phase 6 cluster column schema (Anchor Citation precedes T-Evidence — write Anchor Citation first, then derive T-Evidence):
| # | Name | Category | Rationale | Anchor Citation [write first] | T-Evidence [derived from Anchor Citation — write second] |

Row-writing protocol:
1. Write Rationale (topic-specific; name specific mechanism for `{{topic}}`)
2. **Write Anchor Citation** — cite Phase 4 label strings (Costs, Benefits, Competitive Threshold, Bypasses, Preserves, Net Position). Inline check: if no labels cited — rewrite Rationale to add one displacement claim, then enter Anchor Citation. Do not skip.
3. **Derive T-Evidence** from Rationale and Anchor Citation: `T-1:[PASS/PARTIAL/FAIL]*T-2:[PASS/PARTIAL/FAIL]*T-3:[dims cleared]*T-4:[PASS/PARTIAL/FAIL]`. T-3 dims = anchor field labels where Rationale demonstrates superiority.

Concentration check: any category at 40% — redistribute (BREACH-MAJOR).

EXIT TABLE — Phase 6
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Anchor Citation col present; Phase 4 labels used; <=1/3 blank | BREACH-MAJOR if col absent; BREACH-MINOR <1/3 blank |
| Anchor Citation written before T-Evidence per C-45 ordering constraint | BREACH-MINOR if violated |
| T-Evidence col; structured notation every row | BREACH-MAJOR if col absent |
| No category >=40% | BREACH-MAJOR |
| All Phase 5 candidates present | BREACH-MAJOR |

**Ledger obligation satisfied:** Phase 6 — Cluster Table produced with (a) Anchor Citation column using Phase 4 label strings, written before T-Evidence per C-45 ordering constraint; (b) T-Evidence column with structured `T-1:[v]*T-2:[v]*T-3:[dims]*T-4:[v]` notation on all candidate rows.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — EVIDENCE TRIAGE
(adjudication of pre-declared Phase 6 claims — not first-pass evaluation)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 7 (Evidence Triage)
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Cluster Table — Anchor Citation col | Phase 6 | Present; <=1/3 blank; written before T-Evidence per C-45 ordering constraint |
| Cluster Table — T-Evidence col | Phase 6 | Structured notation all rows; derived from Anchor Citation |
| Do Nothing Anchor Table | Phase 4 | 6 fields; Challenge Binding col present |
| Table 1A (T-3 Adjudication Protocol + Schema) | Phase 1 | T-3 schema locked: Costs/Benefits/Competitive Threshold/Bypasses/Preserves; adjudication protocol declared |

**Load Phase 6 evidence first. Ph6 Anchor Citation is the FIRST data column. This phase adjudicates pre-declared displacement claims — do not form first-pass judgments.**

Step 7-0 (load): For each candidate, read Ph6 Anchor Citation before writing any T-3 cell. The citation declares which anchor dimensions the candidate has pre-committed to displacing.

Do not mark `**` — BREACH-FATAL.

Column schema (Ph6 Anchor Citation FIRST data column):
| # | Name | Ph6 Anchor Citation | Ph6 Pre-Score | T-1: Differentiation | T-2: Topic Fit | T-3: Costs | T-3: Benefits | T-3: Competitive Threshold | T-3: Bypasses | T-3: Preserves | T-4: Category Coverage | Verdict |

- Ph6 Anchor Citation (first data col): copy from Phase 6 verbatim — loaded BEFORE T-3 evaluation
- Ph6 Pre-Score: copy T-Evidence from Phase 6 verbatim
- T-3 (5 cols, Table 1A protocol): if label in Ph6 Anchor Citation — adjudicate claim; if absent — assess implicit support
- T-3 threshold: >=3 PASS cells

EXIT TABLE — Phase 7
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Ph6 Anchor Citation col present as FIRST data col; populated from Phase 6 | BREACH-MAJOR |
| Ph6 Pre-Score col present; populated from Phase 6 T-Evidence | BREACH-MAJOR |
| T-3 via 5 separate anchor-named cols; labels match Table 1A | BREACH-MAJOR if merged or deviation |
| T-3 adjudication followed cite-check protocol | BREACH-MINOR |
| No `**` assigned | BREACH-FATAL if present |
| All candidates evaluated with Verdict | BREACH-MAJOR |

**Ledger obligation satisfied:** Phase 7 — Evidence Triage Table produced with Ph6 Anchor Citation as first data column (carryforward from Phase 6), Ph6 Pre-Score carryforward, and T-3 evaluated via 5 separate anchor-named columns (T-3: Costs / T-3: Benefits / T-3: Competitive Threshold / T-3: Bypasses / T-3: Preserves) on all candidate rows.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 8 — MARK + FINALIZE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 8
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 7 Evidence Triage Table | Phase 7 | All evaluated; Ph6 Anchor Citation first; Ph6 Pre-Score; 5 T-3 cols; no `**` |
| Table 1A (Survival Threshold) | Phase 1 | All 4 tests PASS required |

Apply `**` to exactly 5 entries in Phase 6 cluster table. Top-5 spans >=3 categories; removing any one loses a distinct angle.

EXIT TABLE — Phase 8
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| Exactly 5 `**` marks | BREACH-FATAL |
| `**` set spans >=3 categories | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9A — TERMINAL LEDGER AUDIT (Reconstruct -> Assess)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 9A
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 8 Output | Phase 8 | Exactly 5 `**` marks |
| Phase 7 Evidence Triage Table | Phase 7 | Ph6 Anchor Citation first + Ph6 Pre-Score + 5 T-3 cols; all evaluated |
| Phase 6 Cluster Table | Phase 6 | Anchor Citation + T-Evidence cols; C-45 ordering applied |
| Contributing phases 3-7 | Phases 3-7 | Exit tables + ledger obligation bullets completed |

Phase 9B may not begin until Phase 9A complete and all ledger rows COMPLETE.

**RECONSTRUCT PASS** — describe what was concretely produced (one row per contributing phase):

| Phase | Obligation | What Was Actually Produced | COMPLETE? |
|-------|-----------|---------------------------|-----------|
| Phase 3 | AMEND Source + Primary Challenge Test cols + obligation bullet | [col names; row count; bullet text recorded] | Y/N |
| Phase 4 | Challenge Binding col + citation vocabulary + obligation bullet | [col present; 6 labels declared; bullet text recorded] | Y/N |
| Phase 5 | Name + Pitch + obligation bullet | [row count; blanks; bullet text recorded] | Y/N |
| Phase 6 T-Evidence | Structured notation + obligation bullet | [format used; blank row count; bullet text recorded] | Y/N |
| Phase 6 Anchor Citation | Anchor Citation col; labels; C-45 ordering; obligation bullet | [col present; label examples (cite 3 actual strings used); blank count; **Column ordering observed: Anchor Citation is column [N], T-Evidence is column [N+1] — Anchor Citation precedes T-Evidence: CONFIRMED/VIOLATION**; bullet text recorded] | Y/N |
| Phase 7 | Ph6 Anchor Citation first + Ph6 Pre-Score + T-3 cols + obligation bullet | **T-3 headers observed: [enumerate each T-3-prefixed header exactly as written in Phase 7 output]** Expected: T-3: Costs / T-3: Benefits / T-3: Competitive Threshold / T-3: Bypasses / T-3: Preserves. Match per header: [MATCH/MISMATCH]. C-27 verdict: PASS/PARTIAL/FAIL. Ph6 Anchor Citation as first data col: Y/N. Obligation bullet text recorded. | Y/N |

**ASSESS PASS**:

| Ledger Row | Status | Declared Severity | Action Required |
|-----------|--------|-------------------|----------------|
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
| Reconstruct pass: 6 rows complete | BREACH-MAJOR |
| T-3 headers enumerated for Phase 7 row; C-27 verdict rendered | BREACH-MAJOR |
| Phase 6 Anchor Citation column ordering STATED (not just confirmed Y/N): "Anchor Citation is column [N], T-Evidence is column [N+1]" | BREACH-MINOR if stated as Y/N only |
| Ph6 Anchor Citation confirmed as first data col in Phase 7 | BREACH-MAJOR |
| Obligation bullet text recorded for all contributing phases (3,4,5,6,7) | BREACH-MAJOR if any missing |
| Assess pass: Declared Severity populated on all rows | BREACH-MAJOR |
| All 6 ledger rows COMPLETE | BREACH-FATAL |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 9B — CRITERION CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — Phase 9B
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 9A Terminal Ledger Audit | Phase 9A | Reconstruct + Assess complete; all 6 ledger rows COMPLETE; C-27 verdict rendered; Phase 6 column ordering state recorded (not just Y/N); Ph6 Anchor Citation ordering confirmed; obligation bullets recorded for all contributing phases |

| Row | Criterion | Status | Severity if FAIL |
|-----|-----------|--------|-----------------|
| 1 | Candidate count 20-40 | PASS/FAIL | BREACH-MAJOR |
| 2 | Every candidate: all 4 anatomy fields | PASS/FAIL | BREACH-MAJOR |
| 3 | Exactly 5 `**` marks | PASS/FAIL | BREACH-FATAL |
| 4 | Do Nothing: 6 fields incl. Net Position | PASS/FAIL | BREACH-MAJOR |
| 5 | AMEND: 3 adjustments; dimension + downstream effect | PASS/FAIL | BREACH-MINOR |
| 6 | Architecture: AMEND Source col; all rows | PASS/FAIL | BREACH-MAJOR |
| 7 | Architecture: Primary Challenge Test col; >=1 row T-3 | PASS/FAIL | BREACH-MAJOR |
| 8 | Phase 6: T-Evidence structured notation | PASS/FAIL | BREACH-MAJOR |
| 9 | Phase 7: Ph6 Pre-Score carryforward col | PASS/FAIL | BREACH-MAJOR |
| 10 | `**` set spans >=3 categories | PASS/FAIL | BREACH-MAJOR |
| 11 | Phase 4 Challenge Binding col; Net Position -> T-3 synthesis | PASS/FAIL | BREACH-MAJOR |
| 12 | Table 1C: all 3 BREACH tiers | PASS/FAIL | BREACH-FATAL |
| 13 | Phase 9A Declared Severity col populated | PASS/FAIL | BREACH-MAJOR |
| 14 | Phase 7 T-3 via 5 separate anchor-named cols | PASS/FAIL | BREACH-MAJOR |
| 15 | Table 1B BREACH Tier col; all rows | PASS/FAIL | BREACH-MAJOR |
| 16 | Phase 9A Reconstruct T-3 step; C-27 verdict | PASS/FAIL | BREACH-MAJOR |
| 17 | Phase 6 Anchor Citation col; <=1/3 blank | PASS/FAIL | BREACH-MAJOR if absent |
| 18 | Phase 7 Ph6 Anchor Citation col as FIRST data col | PASS/FAIL | BREACH-MAJOR |
| 19 | Phase 6 ordering annotation present; row protocol sequenced (C-45) | PASS/FAIL | BREACH-MINOR |
| 20 | Phase 5 ENTRY TABLE vocabulary row names Costs/Benefits/Competitive Threshold/Bypasses/Preserves by name (C-48) | PASS/FAIL | BREACH-MINOR |
| 21 | Phase 9A Reconstruct Phase 6 row states observed column ordering ("Anchor Citation is column N, T-Evidence is column N+1") not just Y/N (C-47) | PASS/FAIL | BREACH-MINOR if stated as Y/N only |
| 22 | Every contributing phase exit (3,4,5,6,7) has "Ledger obligation satisfied: [contribution]" bullet (C-35) | PASS/FAIL | BREACH-MAJOR if any contributing phase missing bullet |

EXIT TABLE — Phase 9B
| Departure Condition | BREACH Tier if FAIL |
|--------------------|---------------------|
| All 22 rows checked | BREACH-MINOR |
| All FAIL rows corrected per Table 1C | BREACH-MAJOR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WRITE — ARTIFACT ASSEMBLY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENTRY TABLE — WRITE
| Predecessor Artifact | Source Phase | Required State |
|---------------------|--------------|----------------|
| Phase 9B Criterion Checklist | Phase 9B | All 22 rows PASS or corrected |
| Cluster Table with `**` marks | Phase 8 | Exactly 5 `**` marks |
| AMEND Adjustments Table | Phase 2 | 3 adjustments |
| Do Nothing Anchor Table | Phase 4 | 6 fields |

Write to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

Structure: Title -> AMEND (A1/A2/A3) -> Do Nothing (costs, benefits, net position) -> Category sections; `**` on top-5; each entry: Name — Pitch — Rationale.
```
