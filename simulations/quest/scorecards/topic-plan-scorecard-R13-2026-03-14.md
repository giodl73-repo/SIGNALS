## topic-plan — Round 13 Scoring (v12 rubric)

**Trace artifact**: placeholder — evaluating prompt structure only

---

## Rubric Criteria Pass/Fail by Variation

### Essential Criteria — 5 criteria, 60 pts max (12 pts each)

| Criterion | Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|------|
| C-01 Read strategy.md | Step 1 Stated-Field Extractor present | PASS | PASS | PASS | PASS | PASS |
| C-02 Read signal artifacts | Step 3a Signal Analyst with Glob | PASS | PASS | PASS | PASS | PASS |
| C-03 Identifies delta not inventory | Step 4 anti-pattern label + PASS/FAIL exhibit | PASS | PASS | PASS | PASS | PASS |
| C-04 Typed proposals | ADD/REMOVE/REPRIORITIZE enumerated | PASS | PASS | PASS | PASS | PASS |
| C-05 Confirmation gate | Step 9 "Reply YES" + "Waiting." | PASS | PASS | PASS | PASS | PASS |

**Essential: 60/60 all variations. All essential PASS.**

---

### Recommended Criteria — 3 criteria, 30 pts max (10 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Evidence per change | Evidence column in Proposals | PASS | PASS | PASS | PASS | PASS |
| C-07 Before/after diff | Diff table Before/After columns | PASS | PASS | PASS | PASS | PASS |
| C-08 All three change types | Null rows ADD-0/REMOVE-0/REPRIORITIZE-0 | PASS | PASS | PASS | PASS | PASS |

**Recommended: 30/30 all variations.**

---

### Aspirational Criteria — 33 criteria, 165 pts max (5 pts each)

| Criterion | Evidence | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----------|------|------|------|------|------|
| C-09 Namespace coverage gaps | Step 5 stage-relative audit, 9 namespaces | P | P | P | P | P |
| C-10 Conflicting signals | Step 6 CF-NN table with Implication column | P | P | P | P | P |
| C-11 Typed gate verb | "Reply YES to apply" | P | P | P | P | P |
| C-12 Explicit no-change rows | ADD-0/REMOVE-0/REPRIORITIZE-0 null rows | P | P | P | P | P |
| C-13 Inline evidence brackets | Diff Evidence `[file.md — ≤10 words]` | P | P | P | P | P |
| C-14 Anti-inventory warning | Step 4 "anti-pattern label + PASS/FAIL exhibit" | P | P | P | P | P |
| C-15 All 9 namespaces named | Step 5 lists scout through topic | P | P | P | P | P |
| C-16 Two-level traceability | Delta Finding [Rule 4] + Evidence artifact | P | P | P | P | P |
| C-17 Explicit conflict absence | CF-00 null row | P | P | P | P | P |
| C-18 Structured delta format | "Strategy assumed X / Signal revealed Y" columns | P | P | P | P | P |
| C-19 Proposal ID in diff | Proposal column in Diff table | P | P | P | P | P |
| C-20 Delta Finding in all types | ADD/REMOVE/REPRIORITIZE all carry [Rule 4] | P | P | P | P | P |
| C-21 Column-completeness declaration | "The following columns are mandatory. Do not omit any column." at each step | P | P | P | P | P |
| C-22 Active anti-pattern self-naming | Step 4 "Stop. Write (1) the anti-pattern label" | P | P | P | P | P |
| C-23 Pre-reproduced null templates | All null sites carry verbatim template + (Rule 3) citation as "do not omit" proxy | P | P | P | P | P |
| C-24 Unstated-assumption extraction | Step 2 with 5 scan dimensions (a)–(e) | P | P | P | P | P |
| C-25 "If unchanged" column | Proposals table with decision-gate language | P | P | P | P | P |
| C-26 Schema-first priming | Full output schema declared before Step 1 | P | P | P | P | P |
| C-27 Cascade schema checkpoints | Upfront schema + Step 7 verbatim + Step 8 verbatim = 3 checkpoints | P | P | P | P | P |
| C-28 Named role + scan dimensions | "Assumption Archaeologist" + 5 dimensions (a)–(e) | P | P | P | P | P |
| C-29 Back-fill column | Step 3b adjudicates Contradicted?/Supported?/No coverage | P | P | P | P | P |
| C-30 Forward-reasoning columns | "Why this matters" + "Delta candidate?" in assumption table | P | P | P | P | P |
| C-31 Decision-gate framing for inertia | "no degradation named = preference not decision" at Step 7 | P | P | P | P | P |
| C-32 Reversibility taxonomy | [Rule 1: (1)/(2)/(3)] in schema and commitment | P | P | P | P | P |
| C-33 Full assumption schema upfront | 5-column assumption table in upfront schema block | P | P | P | P | P |
| C-34 Enumerated columns carry value list + prose prohibition | Rule 1 with FAIL examples + "prose not valid" at Step 7 checkpoint | P | P | P | P | P |
| C-35 Assumption columns independently populated | Rule 2 independence test governs all assumption columns | P | P | P | P | P |
| C-36 Named pre-schema rule block | "COLUMN CONTRACT (binding before reading any file)" with numbered rules | P | P | P | P | P |
| C-37 Operationalized independence test | Rule 2 "Can I fill this cell without reading…?" with PASS/FAIL at Step 2 | P | P | P | P | P |
| **C-38** Pass/fail example symmetry | See detail below | **P** | **P** | **PRT** | **PRT** | **PRT** |
| C-39 Step-level activation cross-reference | Step 2 "Apply the COLUMN CONTRACT Rule 2 PASS/FAIL exhibit before populating" | P | P | P | P | P |
| C-40 Null enforcement in CONTRACT | Rule 3 in CONTRACT + "(Rule 3)" at every null site | P | P | P | P | P |
| C-41 Schema column inline rule annotations | `[Rule N: ...]` on all enumerated-value columns in upfront schema | P | P | P | P | P |

**P = PASS (5 pts), PRT = PARTIAL (3 pts)**

#### C-38 Detail — Pass/Fail Example Symmetry

**V-01**: Rule 1 has PASS+FAIL for all 5 columns (Type, Reversibility, Delta candidate?, Consistent with strategy?, Defender verdict). Rule 2 has 4+4. Rule 3 has paired examples. Full symmetry. **PASS (5 pts)**

**V-02**: Rule 1 symmetric 4+4. Rule 5 PASS examples are the scale table values themselves (U-1 through U-5, H/M/L — concrete, labeled within the scale definition); FAIL examples explicitly labeled below. Symmetric in coverage if scale values count as PASS examples (reasonable since they are the exhaustive valid-value set). **PASS (5 pts)**

**V-03**: Rule 1 PASS: 5 columns (adds Prediction match). Rule 1 FAIL: 4 columns — Consistent with strategy? has no FAIL counterpart. Minor asymmetry. **PARTIAL (3 pts)**

**V-04**: Rule 1 PASS: 5 columns. Rule 1 FAIL: 3 columns (Type, Reversibility, Defender verdict) — missing Delta candidate? and Consistent with strategy? FAIL examples. Moderate asymmetry. **PARTIAL (3 pts)**

**V-05**: Rule 1 PASS: 6 columns (adds Prediction match + Defender verdict). Rule 1 FAIL: 3 columns (Type, Prediction match, Defender verdict) — missing Reversibility, Delta candidate?, Consistent with strategy? FAIL examples. Three gaps: more asymmetric than V-03/V-04. **PARTIAL (3 pts)**

---

## Score Computation

| Variation | Essential (60) | Recommended (30) | Aspirational (165) | **Total** |
|-----------|---------------|------------------|--------------------|-----------|
| V-01 | 60 | 30 | 33×5 = **165** | **255** |
| V-02 | 60 | 30 | 33×5 = **165** | **255** |
| V-03 | 60 | 30 | 32×5 + 3 = **163** | **253** |
| V-04 | 60 | 30 | 32×5 + 3 = **163** | **253** |
| V-05 | 60 | 30 | 32×5 + 3 = **163** | **253** |

**Golden threshold: 150 — all variations clear comfortably.**

---

## Ranking

1. **V-01** — 255 pts | Defender + urgency-free | C-38 full symmetry
1. **V-02** — 255 pts | Urgency/signal quality (Rule 5) | C-38 scale table satisfies PASS symmetry
3. **V-03** — 253 pts | Prediction-first | C-38 PARTIAL (1 missing FAIL column)
3. **V-04** — 253 pts | Defender + urgency | C-38 PARTIAL (2 missing FAIL columns)
3. **V-05** — 253 pts | Full ceiling | C-38 PARTIAL (3 missing FAIL columns)

---

## Excellence Signals — V-01 and V-02 (co-top scorers)

### Why V-01 and V-02 held the ceiling while V-03/V-04/V-05 slipped

**V-03/V-04/V-05 all introduced new enumerated columns** (Prediction match, additional Defender verdict instances) as PASS examples in Rule 1, but omitted FAIL examples for pre-existing columns in the same rule. The pattern: adding a new column to the set without maintaining FAIL coverage for the existing columns. This is the R13 failure signal — FAIL example completeness degrades under column expansion.

**V-01 maintained complete symmetry** because it added only one new column (Defender verdict) and provided both PASS and FAIL for it alongside all existing columns.

**V-02 achieved equivalent ceiling** because Rule 5 columns (Urgency, Signal quality) are governed by a separate rule section where the scale table itself constitutes exhaustive PASS examples — no asymmetry can form since the scale IS the complete valid set.

### New structural patterns (candidates for v13 criteria)

**Pattern A — from V-01: Defender back-propagation protocol**

The Defender step (7b) has a typed three-way disposition:
- `Withdrawn` → update original Step 7 row with "[WITHDRAWN after Defender step]" + exclude from diff
- `Strengthened` → update `If unchanged` cell in Step 7 with sharpened degradation case from Architect response
- `Unchanged` → proceed as-is

This is a **linked revision chain** not captured by any v12 criterion. C-25 requires the `If unchanged` column to exist; no criterion requires it to be updatable in response to a counter-argument loop. The Defender introduces a two-step echo: challenge → response → trace of update back to source row. A v13 criterion could test whether proposal changes are back-propagated with a typed disposition record.

**Pattern B — from V-02: Urgency-Reversibility calibration constraint**

Rule 5 introduces a cross-column consistency check embedded in the step instruction:

> "U-4 or U-5 proposals must have Reversibility (2) or (3) — if they do not, revisit Reversibility before proceeding."

This is a **structural constraint not captured by C-32** (which only requires the Reversibility column to exist with three values) or by any existing criterion. The calibration constraint forces resolution of any urgency/reversibility mismatch *before* the diff is built — it's a mechanical quality gate between the urgency assignment and the diff step. A v13 criterion could test whether high-urgency proposals are constrained to non-trivially-reversible change types, making the urgency score load-bearing rather than decorative.

---

## Summary

- All 5 variations clear all 5 essential criteria and all 3 recommended criteria.
- The v12 rubric cannot distinguish R13's new mechanisms (Defender, prediction-first, urgency) since no criteria target them yet.
- The only rubric-level differentiator is C-38 (pass/fail example symmetry), where V-01 and V-02 hold full symmetry while V-03/V-04/V-05 accumulate FAIL-example gaps as column count grows.
- The two excellence patterns from the top scorers — Defender back-propagation and Urgency-Reversibility calibration — are strong candidates for v13 criteria.

```json
{"top_score": 255, "all_essential_pass": true, "new_patterns": ["Defender back-propagation: typed Withdrawn/Strengthened/Unchanged disposition links Step 7b verdict back to Step 7 source row — update of If-unchanged cell is mandatory on Strengthened verdict, creating a traced revision chain not captured by any v12 criterion", "Urgency-Reversibility calibration constraint: U-4/U-5 proposals must resolve to Reversibility (2) or (3) before proceeding to diff — cross-column consistency check embedded in step instruction makes urgency score structurally load-bearing rather than decorative"]}
```
