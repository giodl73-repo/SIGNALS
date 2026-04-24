## quest-score — topic-retro R8

> **Note:** Instructions reference V-01 through V-05. Only V-01 and V-02 were provided. Scoring proceeds on the two available variations.

---

## V-01 — Lifecycle Emphasis

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Signal inventory lists every artifact | PASS | Phase 2 table requires namespace, date, prediction; "No omissions" stated |
| C-02 | Accuracy uses predicted-vs-actual comparison | PASS | Actual outcome + C/P/W columns explicit in Phase 2 |
| C-03 | Gap analysis identifies missing signals | PASS | Phase 4 table requires namespace + signal type per gap |
| C-04 | Exactly one Echo | PASS | Phase 1 requires single-sentence Echo |
| C-05 | Overall accuracy judgment rendered | PASS | "Overall accuracy judgment" instruction closes Phase 2 |
| C-06 | Gap signals actionable | PASS | Phase 4 "Concrete next action" column; generic advice explicitly ruled out |
| C-07 | Accuracy differentiated by namespace | PASS | Phase 2 explicitly instructs per-namespace breakdown after full table |
| C-08 | AMEND scope respected | PASS | Instruction at top covers inventory, accuracy, gaps, and Echo |
| C-09 | Calibration trend surfaced | PASS | Calibration Trend section requires prior retro comparison; fallback for no prior retro included |
| C-10 | Echo feeds back into signal design | PASS | Phase 5 "Echo feedback loop" requires concrete change proposal, not just "we learned X" |
| C-11 | Per-namespace accuracy uses explicit formula | PASS | Same `(C×100+P×50)/(C+P+W)` formula applied per-namespace |
| C-12 | Echo phase precedes accuracy scoring | PASS | Phase 1 → Phase 2 structural order enforced |
| C-13 | Formula embedded in column header | PASS | `Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1→62.5]` is the header |
| C-14 | Echo-accuracy conflict named when tension arises | PASS | Phase 3 conflict audit explicitly handles this |
| C-15 | Column header includes worked example | PASS | `[e.g. C=2,P=1,W=1→62.5]` present in header |
| C-16 | Conflict audit runs unconditionally | PASS | Phase 3: "runs regardless of whether you perceive tension"; explicit no-conflict acknowledgment required |
| C-17 | Echo carries explicit immutability label | PASS | `ECHO (LOCKED)` block header |
| C-18 | Output divided into named/numbered phases | PASS | Phase 0–5 structural labels |
| C-19 | Explicit phase boundary markers | PASS | "Phase boundary: [X]. Proceed to Phase Y." between every phase |
| C-20 | Status-quo foil section | PASS | Phase 5 foil table with three named comparison dimensions |
| C-21 | Echo Lock Record is multi-field artifact | PASS | Four fields: WHEN locked, LOCK STATUS, Authorized conflict response, Echo statement |
| C-22 | Foil records prior belief before signals opened | PASS | Phase 0 captures prior belief before Phase 1; Phase 5 foil explicitly references Phase 0 and instructs "must draw from Phase 0 prior belief — not reconstructed from hindsight" |

**Essential:** 5/5 × 60 = **60**
**Recommended:** 3/3 × 30 = **30**
**Aspirational:** 14/14 × 10 = **10**
**V-01 composite: 100.0**

---

## V-02 — Output Format (Tables-First)

> **Note:** V-02 is structurally incomplete as provided — Steps 1 and 2 only. Steps covering gap analysis, per-namespace rollup, calibration trend, feedback loop, foil, and phase boundaries are absent. Scored on what is present.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Signal inventory lists every artifact | PASS | Step 2: "Every signal artifact for this topic. No omissions." |
| C-02 | Accuracy uses predicted-vs-actual | PASS | Prediction, Actual outcome, C/P/W columns present |
| C-03 | Gap analysis identifies missing signals | FAIL | No gap analysis step present |
| C-04 | Exactly one Echo | PASS | Step 1 requires single-sentence Echo |
| C-05 | Overall accuracy judgment rendered | FAIL | No overall judgment instruction; row-level scores only |
| C-06 | Gap signals actionable | FAIL | No gap analysis step |
| C-07 | Accuracy differentiated by namespace | FAIL | Table has Namespace column enabling grouping, but no per-namespace rollup step instructed |
| C-08 | AMEND scope respected | PASS | "Restrict inventory, accuracy, gaps, and Echo to specified scope" at top |
| C-09 | Calibration trend surfaced | FAIL | No calibration section |
| C-10 | Echo feeds back into signal design | FAIL | No feedback loop step |
| C-11 | Per-namespace explicit formula | FAIL | No per-namespace rollup step; C-07 fails, so C-11 cannot pass |
| C-12 | Echo precedes accuracy scoring | PASS | Step 1 → Step 2 ordering |
| C-13 | Formula in column header | PASS | `Score: (C×100+P×50)/(C+P+W) [e.g. C=3,P=1,W=0→91.7]` is the header |
| C-14 | Echo-accuracy conflict named | PASS | "Conflict with Echo?" column with "Yes/No — note if Yes" runs per row; combined with LOCKED Echo record, tension is nameable |
| C-15 | Header includes worked example | PASS | `[e.g. C=3,P=1,W=0→91.7]` present in header |
| C-16 | Conflict audit unconditional | PASS | "The last column runs unconditionally. Enter 'No conflict' if none exists." — explicit result required in all cases; this is a pre-populated revision log column per rubric definition |
| C-17 | Echo carries immutability label | PASS | `ECHO (LOCKED)` block header |
| C-18 | Named/numbered phases | FAIL | Only Step 1 and Step 2 present; incomplete phase structure |
| C-19 | Phase boundary markers | FAIL | No boundary declarations |
| C-20 | Status-quo foil section | FAIL | No foil step |
| C-21 | Echo Lock Record multi-field | PASS | WHEN locked, LOCK STATUS, Authorized conflict response fields present |
| C-22 | Foil records prior belief before signals opened | FAIL | No Phase 0 equivalent; no foil section |

**Essential:** 3/5 × 60 = **36**
**Recommended:** 1/3 × 30 = **10**
**Aspirational:** 7/14 × 10 = **5**
**V-02 composite: 51.0**

---

## Ranking

| Rank | Variation | Score | Essential | Recommended | Aspirational |
|------|-----------|-------|-----------|-------------|--------------|
| 1 | V-01 Lifecycle Emphasis | **100.0** | 5/5 | 3/3 | 14/14 |
| 2 | V-02 Tables-First | **51.0** | 3/5 | 1/3 | 7/14 |

---

## Excellence Signals (from V-01)

**Phase 0 PRE-RETRO epistemic capture as a standalone phase** — Placing prior belief capture in its own named phase, sealed before Phase 1 opens signals, is what makes C-22 structurally enforceable. Without Phase 0 as a distinct sealed phase, the foil's "Without This Retro" column is always vulnerable to hindsight reconstruction.

**Foil table with three named comparison dimensions** — V-01 breaks the foil into three rows (signal accuracy assumption, Echo assumption, signal design default) rather than a single binary comparison. This forces the retro to address consequence at multiple levels and makes cost-of-inaction more specific than C-20 alone requires.

**Two-pass accuracy computation** — Phase 2 fills the full artifact table first, then computes per-namespace rollup using the same formula. The explicit sequencing (table → rollup) prevents per-namespace scoring from being estimated rather than derived.

**Calibration graceful fallback** — "No prior retro available — calibration baseline established here" makes C-09 a required output even in Round 1, establishing forward continuity rather than treating baseline-setting as a skip condition.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Phase 0 prior-belief capture as a sealed standalone phase makes C-22 structurally enforceable rather than prose-dependent", "Foil table with three named comparison dimensions (accuracy, Echo, signal design) strengthens C-20 specificity", "Calibration graceful fallback turns C-09 into a required baseline-setting event when no prior retro exists"]}
```
