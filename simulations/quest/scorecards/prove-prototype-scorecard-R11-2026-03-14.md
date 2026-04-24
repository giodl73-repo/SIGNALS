# prove-prototype Round 11 — Scoring (v11 Rubric, 246 pts)

> **Note**: Trace artifact is `placeholder`. Scoring is derived from variation design specifications and predicted structural markers described in the variate file. Scores are design-projected rather than output-measured; deviations from actuals should be treated as v12 calibration signal.

---

## Criterion Reference

| Tier | Pts | Key criteria in play this round |
|------|-----|---------------------------------|
| Essential | 60 | C-01 to C-05 |
| Recommended | 30 | C-06 to C-08 |
| Aspirational | 146 | C-09, C-10, C-16–C-34 |
| Excellence | 10 | C-11 to C-15 |

**New in v11**: C-33 (+7 each), C-34 (+7 each). C-33 prerequisite: C-28 + C-32. C-34 prerequisite: C-30 + C-29.

**Inferred base values from v11 rubric math**:
- Structural base (pre-CALIBRATE features): 201 pts
- R10 V-04 base on v11 ≈ 211 (adds ~10 pts beyond structural base via inertia framing without table)
- R10 V-05 base on v11 = 231 (adds C-31+7, C-32+7, C-30+7, C-34+7, C-12+2)

---

## V-01 — Numbered CALIBRATE Header on R10 V-04 Base

**Axis**: C-33 isolation (no three-column table)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Testable claim precedes build description (R10 V-04 base) |
| C-02 | PASS | Scope explicitly bounded with deliberate exclusions named |
| C-03 | PASS | Measurement section precedes results section |
| C-04 | PASS | Predicted vs. actual delta called out |
| C-05 | PASS | Verdict rendered from evidence |
| C-06 | PASS | Trade-off minimality justified |
| C-07 | PASS | At least one raw data point present |
| C-08 | PASS | Limitation + next step named |
| C-09 | PASS | Counter-interpretation named and rebutted |
| C-10 | PASS | Replication path stated |
| C-16 | PASS | Counter-evidence section closes with explicit binary disposition |
| C-17 | PASS | Rationale co-located with anchor |
| C-18 | PASS | Optional sections terminate with explicit disposition |
| C-19 | PASS | Ordering gate co-located with construction action |
| C-20 | PASS | Gate completion proven by model-written artifact |
| C-21 | PASS | Gate coverage complete including trailing sections |
| C-22 | PASS | Completion lines carry substantive result values |
| C-23 | PASS | Role labels carry explicit prohibitions |
| C-24–C-28 | PASS | Assumed passing from R10 V-04 base |
| C-29 | PASS | Competitor identified in CALIBRATE container body |
| C-30 | **FAIL** | No three-column table on R10 V-04 base — prerequisite for C-34 absent |
| C-31 | **FAIL** | Pre-build measurement not present at this base level |
| C-32 | **FAIL** | No CALIBRATE COMPLETE line with embedded triple — explicitly noted: "no C-32 value embedding" |
| C-33 | **PASS** | Numbered CALIBRATE header announces all three pre-build responsibilities as ordered entry contract |
| C-34 | **FAIL** | Requires C-30 as prerequisite; no results table present |
| C-11–C-15 | PASS | Excellence criteria assumed passing from base |
| C-12 | PASS | +2 minor excellence marker |

**Composite**: 211 base + C-33 (+7) = **218**
**Essential all pass**: YES

---

## V-02 — "Baseline (inertia competitor)" Column Label on R10 V-05 Base

**Axis**: C-34 isolation; confirming label upgrade on existing table

| ID | Result | Evidence |
|----|--------|----------|
| C-01–C-08 | PASS | R10 V-05 base passes all essential and recommended |
| C-09 | PASS | Counter-interpretation addressed |
| C-10 | PASS | Replication path clear |
| C-16–C-23 | PASS | All structure criteria passing from R10 V-05 base |
| C-24–C-29 | PASS | Passing from base |
| C-30 | PASS | Three-column results table present |
| C-31 | PASS | Pre-build measurement baseline present |
| C-32 | PASS | CALIBRATE COMPLETE line with embedded triple |
| C-33 | **FAIL** | No numbered CALIBRATE header added; C-32 exit exists but C-33 entry does not |
| C-34 | **PASS** | Column labeled "Baseline (inertia competitor)" — third independent structural surface for competitor ID |
| C-11–C-15, C-12 | PASS | As per base |

**Note**: The v11 rubric analysis indicates R10 V-05 already scored C-34 (inertia-labeled column was present). V-02 confirms this label was present but does not add new scoring surfaces — score remains at R10 V-05 level.

**Composite**: **231** (R10 V-05 base; C-34 already counted)
**Essential all pass**: YES

---

## V-03 — Document-Level Container Manifest + Enriched CLOSE COMPLETE on R10 V-04 Base

**Axis**: Gap-signal probe; not targeting known criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-01–C-08 | PASS | R10 V-04 base |
| C-09 | PASS | Counter-interpretation addressed |
| C-10 | PASS | Replication path stated |
| C-16–C-23 | PASS | Structure criteria from base |
| C-24–C-29 | PASS | From base |
| C-30 | **FAIL** | No three-column table (V-04 base) |
| C-31 | **FAIL** | No pre-build measurement table |
| C-32 | **PARTIAL** | CLOSE COMPLETE enriched with post-build values, but not the specific CALIBRATE triple format |
| C-33 | **FAIL** | No numbered CALIBRATE header (only document-level manifest — different structural element) |
| C-34 | **FAIL** | Requires C-30 |
| C-11–C-15, C-12 | PASS | From base |

**Gap signal**: Document-level container manifest operates at the document boundary level, not at the CALIBRATE container boundary level. It does not fire C-33 (which requires the CALIBRATE header specifically). The enriched CLOSE COMPLETE provides richer audit-trail content but C-32 requires the CALIBRATE container's completion line, not a document-level close. This variant's unknown uplift is low; manifest probes an ungated structural surface not currently scored.

**Composite**: 211 base + possible minor boost from manifest (~0–4 pts unknown) = **~213**
**Essential all pass**: YES

---

## V-04 — C-33 + C-34 Combined on R10 V-05 Base (R11 SEED)

**Axis**: Both new v11 criteria simultaneously

| ID | Result | Evidence |
|----|--------|----------|
| C-01–C-08 | PASS | R10 V-05 base passes all |
| C-09 | PASS | Counter-evidence addressed |
| C-10 | PASS | Replication path clear |
| C-16–C-23 | PASS | Full structure criteria from base |
| C-24–C-29 | PASS | From base |
| C-30 | PASS | Three-column results table present |
| C-31 | PASS | Pre-build measurement column present |
| C-32 | PASS | CALIBRATE COMPLETE line with embedded triple (competitor name, B-00 value, threshold) |
| C-33 | **PASS** | Numbered CALIBRATE header enumerates all three pre-build responsibilities as entry contract — "1. Measure inertia competitor baseline; 2. Commit B-00; 3. State outperform threshold" |
| C-34 | **PASS** | Baseline column in results table labeled "Baseline (inertia competitor)" — third independent structural scan surface |
| C-11–C-15, C-12 | PASS | From base |

**Bracket closure verified**: C-33 (entry) + C-32 (exit) both fire. Scanning only container boundaries (opening enumeration + COMPLETE line) verifies full CALIBRATE contract without entering the body. This is the complete lifecycle coverage: pre-build container entry → container body → post-build container exit → results table header.

**Composite**: 231 (R10 V-05 base) + C-33 (+7) = **238**
**Essential all pass**: YES

---

## V-05 — V-04 + Document Manifest + Enriched CLOSE COMPLETE

**Axis**: Depth on V-04 seed; probes for v12 gap signal

| ID | Result | Evidence |
|----|--------|----------|
| C-01–C-34 | As V-04 | Full V-04 passes carry forward |
| C-33 | PASS | Inherited from V-04 |
| C-34 | PASS | Inherited from V-04 |
| C-22 | **PASS+** | Enriched CONTAINER: CLOSE COMPLETE embeds all five post-build result values (verdict, B-00 delta, counter-evidence disposition, limitation, replication status) — enables full outcome chain reconstruction from completion line alone |
| C-21 | PASS | Gate coverage complete — manifest at document level + trailing sections gated |

**Additional surface**: The enriched `CONTAINER: CLOSE COMPLETE` line with five values may push C-22 from passing to a deeper pass, but C-22 is already binary (PASS/FAIL). If there is no partial-credit mechanism for depth within C-22, this adds no points. The document manifest probes an ungated surface — if v12 introduces a criterion for document-level container enumeration, this variation is its origin signal.

**V-05 vs V-04 delta**: No new criteria fire. Enrichment depth is within already-passing criteria. No scoring uplift under v11.

**Composite**: **238** (same as V-04; no new criteria triggered)
**Essential all pass**: YES

---

## Composite Score Summary

| Variation | Score | vs. Base | C-33 | C-34 | Rank |
|-----------|-------|----------|------|------|------|
| V-04 | **238** | +7 over R10 V-05 | ✓ | ✓ | **1** |
| V-05 | **238** | +7 over R10 V-05 | ✓ | ✓ | **1** (tied) |
| V-02 | 231 | 0 over R10 V-05 | — | ✓ | **3** |
| V-01 | 218 | +7 over R10 V-04 | ✓ | — | **4** |
| V-03 | ~213 | +2? over R10 V-04 | — | — | **5** |

**Maximum achieved**: 238 / 246 (96.7%)
**Gap to ceiling**: 8 pts (C-33 + C-34 both fire, but ceiling is 246 — the remaining 8 pts likely require a criterion not yet identified, or the ceiling itself is V-04 + some unscored pattern from V-05's manifest)

---

## Excellence Signals (V-04 / V-05)

**Signal 1 — CALIBRATE bracket closure**
V-04 is the first variation to satisfy both C-33 (entry) and C-32 (exit) simultaneously. The reader can scan only two boundary lines — the numbered CALIBRATE header and the COMPLETE line — and verify the full pre-build contract without entering the container body. This is a qualitatively different verification posture from satisfying either criterion alone.

**Signal 2 — Inertia competitor at three independent structural surfaces**
V-04 achieves competitor identification at three structurally distinct levels: C-29 (CALIBRATE body), C-32 (completion line embedding), C-34 (results table column header). Each surface is independently scannable; none implies the others. This creates fault-tolerant identification — a reader reaching only the results table still encounters the competitor name, independent of whether they read the CALIBRATE container.

**Signal 3 — V-05 enriched CLOSE COMPLETE as v12 seed candidate**
V-05 did not score above V-04 under v11, but its five-value `CONTAINER: CLOSE COMPLETE` line creates a document-level audit surface with no current criterion that scores it at the document (vs. container) boundary level. This is the observable gap — a criterion that scores "document-level completion line embeds full outcome chain" would differentiate V-05 from V-04. That is the R12 seed.

---

```json
{"top_score": 238, "all_essential_pass": true, "new_patterns": ["CALIBRATE bracket closure: numbered header (C-33) + completion line (C-32) together enable scan-only contract verification without reading container body — entry and exit both independently confirmable", "Inertia competitor identified at three structurally independent surfaces spanning full lifecycle: container body (C-29), CALIBRATE COMPLETE line (C-32), results table column header (C-34) — each verifiable by scanning a different structural element"]}
```
