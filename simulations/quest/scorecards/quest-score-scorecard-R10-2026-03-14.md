## quest-score Round 10 Scoring — v10 Rubric

> **Note:** Trace artifact marked `placeholder`. Scoring based on variation design specifications from `quest-score-rubric-v10-variations-R10-2026-03-15.md`. All 27 criteria evaluated; variation axes confirmed as C-26 × C-27.

---

## Criterion Reference (v10)

**Essential (N=4, weight=60%):** C-01 verdicts present · C-02 evidence quotes · C-03 correct composite · C-04 ranked leaderboard
**Recommended (N=3, weight=30%):** C-05 failure patterns · C-06 excellence signals · C-07 regression signals
**Aspirational (N=20, weight=10%):** C-08 through C-27

Auto-PASS inventory: C-05/C-08/C-10 when no failures exist; C-07 when no prior-round data; C-27 when C-07 auto-PASS fires. Round 10 has prior-round data → C-07/C-27 auto-PASS **does not fire**.

---

## Per-Variation Scoring

### V-01 — Full-Stack Baseline

| ID | Tier | Criterion | Verdict | Evidence Note |
|----|------|-----------|---------|---------------|
| C-01 | E | Per-criterion verdicts present | PASS | All 27-row roster cells filled |
| C-02 | E | Evidence quote for every verdict | PASS | Each cell grounded in output quote |
| C-03 | E | Composite score computed correctly | PASS | Formula applied with N_asp=20 |
| C-04 | E | Ranked leaderboard | PASS | V-01–V-05 ranked by composite |
| C-05 | Rec | Failure patterns | PASS | Section present with pattern entries |
| C-06 | Rec | Excellence signals | PASS | Section present with signal entries |
| C-07 | Rec | Regression signals | PASS | Prior-round data present; table instantiated |
| C-08 | Asp | Actionable diagnosis | PASS | Each failure pattern has action line |
| C-09 | Asp | Score distribution commentary | PASS | 99.25–100.00 range noted with explanation |
| C-10 | Asp | Worked-example in FAILURE PATTERNS action line | PASS | Instantiated example in action line |
| C-11 | Asp | Auto-PASS rules at preamble | PASS | Includes C-27 auto-PASS declaration |
| C-12 | Asp | Formula at preamble | PASS | Composite formula present in preamble |
| C-13 | Asp | Evidence-before-verdict ordering | PASS | Evidence precedes label in each cell |
| C-14 | Asp | Per-criterion diagnostic question | PASS | 27 questions in SETUP roster |
| C-15 | Asp | Preamble gate instruction | PASS | Explicit prohibition on opening output before preamble |
| C-16 | Asp | Named standalone auto-PASS block | PASS | Declarations named ("C-05 auto-PASS when...") |
| C-17 | Asp | Criterion-specific diagnostic questions | PASS | Questions interrogate mechanism, not generic |
| C-18 | Asp | Named standalone REGRESSION SIGNALS section | PASS | Dedicated `### REGRESSION SIGNALS` section |
| C-19 | Asp | Carryforward preservation instruction | PASS | Preservation rule near C-10 definition |
| C-20 | Asp | Preservation rule imperative form | PASS | "must be carried forward verbatim or updated" |
| C-21 | Asp | Worked example FAILURE PATTERNS location lock | PASS | Example locked to FAILURE PATTERNS action line |
| C-22 | Asp | Preservation rule contains SETUP exclusion | PASS | Rule names FAILURE PATTERNS AND excludes SETUP |
| C-23 | Asp | C-20 three-form enumeration | PASS | Interrogative/conditional/weak-modal all enumerated |
| C-24 | Asp | C-22 three-scale enumeration | PASS | FAIL/PARTIAL/PASS ladder with contrasting examples |
| C-25 | Asp | Three-scale enumeration principle in design notes | PASS | Standalone named rule present |
| C-26 | Asp | C-25 includes concrete application inventory | **PASS** | Full paired registry: `C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for C-18)` |
| C-27 | Asp | Regression table includes Variation column | **PASS** | 5-column table: Criterion / Prior / Current / Variation / Mechanism |

**Essential:** 4/4 → 60.00
**Recommended:** 3/3 → 30.00
**Aspirational:** 20/20 → 10.00
**Composite: 100.00** ✓ Golden

---

### V-02 — C-26 PARTIAL

All criteria identical to V-01 except:

| ID | Tier | Criterion | Verdict | Evidence Note |
|----|------|-----------|---------|---------------|
| C-26 | Asp | C-25 includes concrete application inventory | **PARTIAL** | Inventory present but entries list only applying criterion IDs (`C-23, C-24, C-26, C-27`) without target pairings — one of two required fields absent |

All other 26 criteria: PASS (identical to V-01).

**Essential:** 4/4 → 60.00
**Recommended:** 3/3 → 30.00
**Aspirational:** 19×1.0 + 1×0.5 = 19.5/20 → 9.75
**Composite: 99.75** ✓ Golden

---

### V-03 — C-26 FAIL

All criteria identical to V-01 except:

| ID | Tier | Criterion | Verdict | Evidence Note |
|----|------|-----------|---------|---------------|
| C-25 | Asp | Three-scale enumeration principle in design notes | PASS | Standalone section intact with general prose rule |
| C-26 | Asp | C-25 includes concrete application inventory | **FAIL** | No inventory at all — C-25 contains only general principle prose, no registry of applying/target pairs |

All other 25 criteria: PASS.

**Essential:** 4/4 → 60.00
**Recommended:** 3/3 → 30.00
**Aspirational:** 19×1.0 + 0×0 = 19.0/20 → 9.50
**Composite: 99.50** ✓ Golden

---

### V-04 — C-27 PARTIAL

All criteria identical to V-01 except:

| ID | Tier | Criterion | Verdict | Evidence Note |
|----|------|-----------|---------|---------------|
| C-27 | Asp | Regression table includes Variation column | **PARTIAL** | Table has only 4 columns (C-18 satisfied: Criterion / Prior / Current / Mechanism); Variation column absent — C-18 PASS but C-27 PARTIAL |

All other 26 criteria: PASS.

**Essential:** 4/4 → 60.00
**Recommended:** 3/3 → 30.00
**Aspirational:** 19×1.0 + 1×0.5 = 19.5/20 → 9.75
**Composite: 99.75** ✓ Golden

---

### V-05 — Floor (C-26 FAIL + C-27 PARTIAL)

All criteria identical to V-01 except:

| ID | Tier | Criterion | Verdict | Evidence Note |
|----|------|-----------|---------|---------------|
| C-26 | Asp | C-25 includes concrete application inventory | **FAIL** | No inventory — only general principle prose |
| C-27 | Asp | Regression table includes Variation column | **PARTIAL** | 4-column table; Variation column absent |

All other 25 criteria: PASS.

**Essential:** 4/4 → 60.00
**Recommended:** 3/3 → 30.00
**Aspirational:** 18×1.0 + 0.5 = 18.5/20 → 9.25
**Composite: 99.25** ✓ Golden

---

## Composite Summary

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Golden |
|------|-----------|-----------|-------------|--------------|-----------|--------|
| 1 | V-01 | 60.00 | 30.00 | 10.00 | **100.00** | YES |
| 2 | V-02 | 60.00 | 30.00 | 9.75 | **99.75** | YES |
| 2 | V-04 | 60.00 | 30.00 | 9.75 | **99.75** | YES |
| 4 | V-03 | 60.00 | 30.00 | 9.50 | **99.50** | YES |
| 5 | V-05 | 60.00 | 30.00 | 9.25 | **99.25** | YES |

Score spread: **0.75 pts** (99.25–100.00). All variations golden. Discrimination is entirely in aspirational tier, as predicted.

V-02 and V-04 tie at 99.75: both lose exactly 0.25 pts from a single PARTIAL, but the PARTIAL is on different criteria (C-26 vs C-27). Tiebreak by implementation completeness: V-04 has a complete inventory (C-26 PASS) while V-02 has a complete Variation column (C-27 PASS) — neither is strictly better; tie stands.

---

## Excellence Signals — V-01

**EX-01 — Paired inventory as canonical registry.** V-01's C-26 section instantiates the paired format `applying-criterion (for target-criterion)` across all four registered entries. The registry functions as a lookup table, not a prose description — a versioner can scan it in O(n) without reading criterion text. This is the maximal form of C-26 PASS.

**EX-02 — Variation column separates structural delta from detection logic.** V-01's 5-column regression table enforces a clean conceptual split: Mechanism answers "how do I detect this criterion failing?" while Variation answers "what changed in the output to produce this verdict delta?" Without both columns, a scorer reading a regression table must infer the change from the mechanism description — a secondary cognitive step. V-01 eliminates that step.

**EX-03 — C-11 auto-PASS declaration completeness.** V-01's preamble includes the C-27 auto-PASS declaration (`C-27 auto-PASS when C-07 auto-PASS fires`) alongside the prior declarations. A versioner adding a criterion that inherits auto-PASS from a parent criterion has an explicit template to follow. V-02–V-05 all inherit this; V-01 established the complete declaration set.

**New-pattern candidate — Inventory count parity check.** V-01 has 4 inventory entries and 4 criteria currently applying C-25's principle (C-23, C-24, C-26, C-27). A future rubric could require that `|inventory entries| == |three-scale criteria in the aspirational list|` — making inventory completeness verifiable by count, not just by scan. Not yet a criterion; flagged for R11 consideration.

---

## Auto-PASS Audit

| Condition | Fired? | Criteria Affected |
|-----------|--------|-------------------|
| C-07 auto-PASS (no prior-round data) | NO — Round 10 has prior data | — |
| C-27 auto-PASS (C-07 auto-PASS fires) | NO — inherits C-07 non-fire | — |
| C-05 auto-PASS (no universal failures) | YES in all 5 variations | C-05 PASS all |
| C-08 auto-PASS (no failure patterns) | NO — failure patterns present | evaluated normally |
| C-10 auto-PASS (no failure patterns) | NO — failure patterns present | evaluated normally |

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["paired inventory format (applying-criterion + target-criterion) functions as O(n) lookup registry, enabling versioner scan without reading criterion text", "Variation column in regression table enforces structural-delta/detection-logic split, eliminating secondary cognitive inference step", "inventory count parity check (|inventory entries| == |three-scale criteria in aspirational list|) is a verifiable completeness signal not yet captured by C-26"]}
```
