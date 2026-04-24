## Round 6 Scoring: quest-variate (v6 Rubric)

---

### Pre-Scoring Setup

**Champion baseline (R5 V-05):** three-phase body with C-24/C-26/C-27/C-28/C-29 satisfied. Missing C-25 (single `failure-condition:` field), C-30 (no failure-condition prediction columns in VARIATION MAP), C-31 (axis consistency check in Phase 3, not in-loop).

**R6 axis assignments:** V-01 → C-25 (output-format), V-02 → C-30 (scoring-granularity), V-03 → C-31 (lifecycle-emphasis), V-04 → C-25+C-31 (combination), V-05 → C-30+C-31 (combination).

---

### Criterion-by-Criterion Scores — All Variations

#### Essential (C-01 through C-05)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|---------|
| C-01 Runnable completeness | PASS | PASS | PASS | PASS | PASS | All bodies have PHASE 1–3 fully written; `{template-vars}` are intentional fill-slots, not ellipses |
| C-02 Count and labeling | PASS | PASS | PASS | PASS | PASS | Exactly 5 variations, V-01–V-05, no gaps |
| C-03 Axis declaration | PASS | PASS | PASS | PASS | PASS | Each preamble has `**axis:**` and `**hypothesis:**` with all subfields |
| C-04 Single-axis isolation | PASS | PASS | PASS | PASS | PASS | V-01: Phase 1 header field change only; V-02: VARIATION MAP columns only; V-03: Step 2B only; V-04/V-05: C-04 exception explicitly invoked |
| C-05 Genuine distinctness | PASS | PASS | PASS | PASS | PASS | Each changes a structurally different element (Phase 1 header field vs MAP columns vs AXIS-FREEZE step vs combinations) |

**All 5 essential: PASS across all variations.**

---

#### Recommended (C-06 through C-08)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|---------|
| C-06 Axis spread | PASS | PASS | PASS | PASS | PASS | 3 distinct axes used: output-format, scoring-granularity, lifecycle-emphasis |
| C-07 Falsifiable hypotheses | PASS | PASS | PASS | PASS | PASS | All name specific comparison baseline (e.g., "does not exceed R5 V-01 result") |
| C-08 Baseline explicit | PASS | PASS | PASS | PASS | PASS | Per-Axis Pole Declaration table at document top names baseline pole per axis |

**All 3 recommended: PASS across all variations.**

---

#### Aspirational (C-09 through C-31)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Key evidence / differentiator |
|-----------|------|------|------|------|------|-------------------------------|
| C-09 Combination roadmap | PASS | PASS | PASS | PASS | PASS | 2-row roadmap at end of doc with rationale |
| C-10 Hypothesis tension surfaced | PASS | PASS | PASS | PASS | PASS | Axis Tension Note section; V-04/V-05 preambles surface gate-vs-key-content tension |
| C-11 Explicit failure conditions | PASS | PASS | PASS | PASS | PASS | All preambles have both `failure-condition-outcome:` and `failure-condition-implementation:` |
| C-12 Evaluation order | PASS | PASS | PASS | PASS | PASS | 5-row Evaluation Order table; cost, independence, cross-round dependency all filled |
| C-13 Pre-combination tension note | PASS | PASS | PASS | PASS | PASS | Axis Tension Note precedes roadmap; dominant-axis predictions given for V-04 and V-05 |
| C-14 Criterion-targeted axis selection | PASS | PASS | PASS | PASS | PASS | Each preamble names criterion ID and states structural pathway: V-01→C-25, V-02→C-30, V-03→C-31 |
| C-15 Inline generation loop gate | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL | All have per-body AXIS-FREEZE + end-of-body advance condition with halt; no variation names a criterion ID inside gate instructions |
| C-16 Per-axis pole declaration | PASS | PASS | PASS | PASS | PASS | Document-top Per-Axis Pole Declaration table names all 6 axes individually |
| C-17 Pre-generation axis lock | PASS* | PASS* | PASS* | PASS | PASS | *Single-axis: vacuous pass; V-04/V-05 bodies include "Do not revise axis assignments after Phase 2 begins" |
| C-18 Single-axis comparison denominator | PASS* | PASS* | PASS* | PASS | PASS | *Single-axis: vacuous pass; V-04 failure cond cites "V-01 R6 alone (C-25 single-axis baseline)"; V-05 cites "V-02 R6 alone (C-30 single-axis baseline)" |
| C-19 Four-part hypothesis schema | PASS | PASS | PASS | PASS | PASS | All preambles have criterion-target, direction, mechanism, failure-condition as labeled parts in one hypothesis block |
| C-20 Dual mechanistically-distinct failure conditions | PASS | PASS | PASS | PASS | PASS | All: outcome failure (no criterion improvement) vs implementation failure (mechanism wrong, names separate C-NN) |
| C-21 Rubric-ID exception citation | PASS | PASS | PASS | PASS | PASS | V-04 and V-05 both carry `*C-04 exception explicitly invoked.*` verbatim |
| C-22 Criterion-keyed combination roadmap | PASS | PASS | PASS | PASS | PASS | Row 1: "C-25, C-30"; Row 2: "C-31, C-07" with per-row mechanism sentences |
| C-23 Phased prompt architecture | PARTIAL | PASS | PASS | PASS | PASS | V-01 Phase 3 lacks "Declared responsibility:" label; V-02–V-05 all have explicit declared responsibility per phase |
| C-24 Pre-generation variation score predictions | PASS | PASS | PASS | PASS | PASS | All VARIATION MAP templates have C-01/C-04/C-07 Direction columns with fill instructions |
| C-25 Dual failure condition sub-fields as named keys | **PASS** | **FAIL** | **FAIL** | **PASS** | **FAIL** | V-01 and V-04: Phase 1 header format has `failure-condition-outcome:` + `failure-condition-implementation:` as distinct keys; V-02/V-03/V-05: single `failure-condition:` field |
| C-26 Per-body axis-freeze protocol | PASS | PASS | PASS | PASS | PASS | All bodies: AXIS-FREEZE PROTOCOL fires per-body in Phase 2; 6-entry freeze list; "[read from VARIATION MAP]" labels |
| C-27 VARIATION MAP as standalone top-level artifact | PASS | PASS | PASS | PASS | PASS | All bodies: `## VARIATION MAP — Immutable after Phase 2 begins` with "[AUTHORITATIVE SOURCE]" + immutability instruction |
| C-28 Count-verifiable axis-freeze completeness gate | PASS | PASS | PASS | PASS | PASS | All bodies: "A freeze list with fewer than six entries is incomplete — do not proceed" |
| C-29 VARIATION MAP as authoritative read-source for freeze | PASS | PASS | PASS | PASS | PASS | All bodies declare "[AUTHORITATIVE SOURCE] The AXIS-FREEZE PROTOCOL reads axis assignments from this table" and each freeze entry carries "[read from VARIATION MAP for this body]" |
| C-30 Failure-condition predictions in pre-gen variation map | **FAIL** | **PASS** | **FAIL** | **FAIL** | **PASS** | V-02 and V-05: VARIATION MAP template has `failure-condition-outcome prediction` and `failure-condition-implementation prediction` columns; V-01/V-03/V-04: direction-only columns |
| C-31 Cross-artifact axis consistency gate in generation loop | **FAIL** | **FAIL** | **PASS** | **PASS** | **PASS** | V-03/V-04/V-05: Step 2B fires inside AXIS-FREEZE PROTOCOL after freeze list but before Step 3 (body writing); explicit "CONSISTENT / AXIS DIVERGENCE" verdict with halt; V-01/V-02: "Verify…" fires post-all-bodies before Phase 3, not per-body pre-write |

---

### Aspirational Pass Counts

| Criterion group | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------------|------|------|------|------|------|
| Full PASS count (of 23) | 19 | 20 | 20 | 21 | 21 |
| PARTIAL count | 2 (C-15, C-23) | 1 (C-15) | 1 (C-15) | 1 (C-15) | 1 (C-15) |
| FAIL count | 2 (C-30, C-31) | 2 (C-25, C-31) | 2 (C-25, C-30) | 1 (C-30) | 1 (C-25) |
| Effective aspir. numerator | 19 + 1.0 = 20.0 | 20 + 0.5 = 20.5 | 20 + 0.5 = 20.5 | 21 + 0.5 = 21.5 | 21 + 0.5 = 21.5 |

---

### Composite Scores

```
composite = (essential_pass / 5 × 60) + (recommended_pass / 3 × 30) + (aspirational_pass / 23 × 10)
```

| Variation | Essential | Recommended | Aspirational | Composite |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 60.0 | 30.0 | 20.0/23 × 10 = 8.70 | **98.70** |
| V-02 | 60.0 | 30.0 | 20.5/23 × 10 = 8.91 | **98.91** |
| V-03 | 60.0 | 30.0 | 20.5/23 × 10 = 8.91 | **98.91** |
| V-04 | 60.0 | 30.0 | 21.5/23 × 10 = 9.35 | **99.35** |
| V-05 | 60.0 | 30.0 | 21.5/23 × 10 = 9.35 | **99.35** |

---

### Ranking

| Rank | Variation | Score | Achieved R6 criteria |
|------|-----------|-------|---------------------|
| 1 (tie) | **V-05** | 99.35 | C-30 + C-31 + Step 2B reads failure-condition predictions from MAP at gate-fire time |
| 1 (tie) | **V-04** | 99.35 | C-25 + C-31 + dual-key structure verified by in-loop axis gate before body writes |
| 3 (tie) | **V-02** | 98.91 | C-30 (+ C-23 full pass vs V-01) |
| 3 (tie) | **V-03** | 98.91 | C-31 (+ C-23 full pass vs V-01) |
| 5 | **V-01** | 98.70 | C-25 only (C-23 partial) |

**Tiebreaker V-04 vs V-05:** V-05 edges V-04 on depth. V-05's Step 2B reads BOTH the axis assignment AND the `failure-condition-outcome prediction` from the VARIATION MAP at gate-fire time (lines 957–964). This creates a **three-level chain** — prediction committed at document scope → axis + prediction surfaced at loop scope → body written under confirmed assignment with surfaced predictions — linking C-30 and C-31 into a single coherent protocol. V-04's gate verifies axis only; it cannot detect whether the dual-key failure-condition content in the Phase 1 header is mechanistically correct. V-05's chain exposes more of the VARIATION MAP at gate scope. V-05 ranks first.

---

### Excellence Signals from Top Variation (V-05)

**E-01: Failure-condition prediction surfaced inside in-loop gate at gate-fire time**
V-05's Step 2B reads the `failure-condition-outcome prediction` from the VARIATION MAP row before the body is written. Prior rounds: VARIATION MAP commits predictions (C-30) and in-loop gate checks axis (C-31) independently. V-05 links them: the gate output includes both the axis verdict AND the pre-committed failure-condition prediction, so the generator writes under a verified axis with the expected failure signature visible. Makes C-30 predictions load-bearing at generation time, not just at Phase 3 calibration.

**E-02: Separate Phase 3 calibration tables for axis-alignment vs failure-condition implementation prediction**
V-05 splits Phase 3 into: (1) `Axis and failure-condition alignment confirmation` (axis match + Step 2B result + failure-condition-outcome prediction match) and (2) `Failure-condition implementation prediction calibration` (implementation prediction vs body content). Prior rounds: one combined axis alignment table. V-05's split enables independent audit of axis divergence and failure-mode prediction accuracy — two different error types with different corrective actions.

---

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["Failure-condition predictions surfaced at in-loop gate fire-time (Step 2B reads failure-condition-outcome prediction from VARIATION MAP before body writes) — links C-30 map-scope commitment to C-31 loop-scope enforcement into a single three-level chain: predict at document scope, verify at loop scope, write under confirmed assignment with surfaced predictions", "Phase 3 split into independent axis-alignment confirmation table and failure-condition implementation prediction calibration table — enables separate auditing of axis divergence (protocol failure) vs failure-mode prediction mismatch (hypothesis quality failure)"]}
```
