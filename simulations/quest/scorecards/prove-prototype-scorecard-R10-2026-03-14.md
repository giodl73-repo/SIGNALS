# Round 10 Scoring — prove-prototype (v10, 232 pts)

## Baseline: R9-V-03 (~201 pts assumed)

R9-V-03 is assumed to pass all essential (C-01–C-05), all recommended (C-06–C-08), and all aspirational criteria through C-29 — including C-23, C-24, C-25, C-26, C-27, C-28, C-29 — but **fails C-30, C-31, C-32**, and all excellence criteria (C-11–C-15), based on the rubric's gap analysis.

Point breakdown:
- Essential: 5 × 12 = 60
- Recommended: 3 × 10 = 30
- Aspirational (C-09, C-10, C-16–C-29): 15 × 7 + C-26 at 6 = 111
- Excellence: 0
- **Base: 201 pts**

---

## V-01 — FRAMER Prohibition Adds Routing Text

**Axis**: C-31 (single change)
**Change**: FRAMER role header adds: *"inertia competitor identification prohibited in DESIGN — belongs exclusively in CALIBRATE"* in three locations.

| Criterion | Status | Evidence |
|-----------|--------|----------|
| C-01 through C-10 | PASS | Inherited from R9-V-03; structural change doesn't affect scope, hypothesis, measurement, or prediction criteria |
| C-16 through C-29 | PASS | Inherited; CALIBRATE structure, role labels, lifecycle containers, gate markers all unchanged |
| **C-31** | **PASS** | Routing language present: prohibition names DESIGN as source and CALIBRATE as required destination — role-label scan can now independently verify placement without entering either container |
| C-32 | FAIL | CALIBRATE COMPLETE still reads "inertia competitor identified, B-00 committed, outperform threshold stated" — B-00 label present but value absent |
| C-30 | FAIL | No three-column table introduced |
| C-11–C-15 | FAIL | No excellence criteria added |

**V-01 score: 201 + 7 = 208 pts**

---

## V-02 — CALIBRATE COMPLETE Value Embedding

**Axis**: C-32 (single change)
**Change**: CALIBRATE COMPLETE now reads: `inertia competitor identified = "[name]", B-00 committed = [value], outperform threshold stated = [condition]`

| Criterion | Status | Evidence |
|-----------|--------|----------|
| C-01 through C-10 | PASS | Inherited |
| C-16 through C-29 | PASS | Inherited; CALIBRATE structure, competitor framing, gate markers unchanged |
| C-31 | FAIL | FRAMER role still uses column-entry form without routing destination — role-label scan cannot verify CALIBRATE as required destination |
| **C-32** | **PASS** | COMPLETE line embeds all three elements with actual values: competitor name, B-00 numeric value, threshold condition — scan-only auditor can verify the triple without reading container body |
| C-30 | FAIL | No three-column table |
| C-11–C-15 | FAIL | No excellence criteria added |

**V-02 score: 201 + 7 = 208 pts**

---

## V-03 — CALIBRATE Header Enumeration

**Axis**: Lifecycle emphasis (single change)
**Change**: CALIBRATE container header becomes a numbered list: *"1. Measure inertia competitor baseline; 2. Commit B-00; 3. State outperform threshold"*

| Criterion | Status | Evidence |
|-----------|--------|----------|
| C-01 through C-10 | PASS | Inherited |
| C-16 through C-29 | PASS | Inherited; enumerated header clarifies but doesn't extend C-28 (already passing) or C-29 (already passing) |
| C-31 | FAIL | No FRAMER routing prohibition added |
| C-32 | FAIL | COMPLETE line is unchanged — header enumeration makes the audit contract visible at the top of the container but does not satisfy the requirement that the COMPLETE *line itself* embeds result values |
| C-30 | FAIL | No three-column table |
| C-11–C-15 | FAIL | No excellence criteria added |

**Note**: V-03 improves human readability and telegraphs intent, but rubric criteria are evaluated on structural markers and completion-line content — neither of which V-03 alters. No new criteria satisfied.

**V-03 score: 201 pts (no change)**

---

## V-04 — FRAMER Routing + CALIBRATE Value Embedding (Combined)

**Axis**: C-31 + C-32 (safe baseline combination)
**Change**: V-01 routing language applied to all three FRAMER prohibition locations AND V-02 value embedding in CALIBRATE COMPLETE.

| Criterion | Status | Evidence |
|-----------|--------|----------|
| C-01 through C-10 | PASS | Inherited |
| C-16 through C-29 | PASS | Inherited; both modifications reinforce already-passing container structure |
| **C-31** | **PASS** | Routing text in FRAMER prohibition: "must NOT appear in DESIGN — belongs exclusively in CALIBRATE" — role-label scan now independently detectable |
| **C-32** | **PASS** | CALIBRATE COMPLETE embeds: competitor name + B-00 value + threshold condition — triple confirmed at completion line |
| C-30 | FAIL | No three-column table |
| C-11–C-15 | FAIL | No excellence criteria; without C-30, C-12 (effect-size by construction) remains unmet |

**Regression check**: V-01 routing language and V-02 value embedding operate on independent structural elements (FRAMER role header vs. CALIBRATE completion line); no interference expected.

**V-04 score: 201 + 7 + 7 = 215 pts**

---

## V-05 — V-04 + Three-Column Results Table (Ceiling Attempt)

**Axis**: C-31 + C-32 + C-30 combined
**Change**: V-04 plus a three-column table in Phase 7 with columns: *Predicted Outcome | Observed Outcome | Baseline (inertia competitor)*

| Criterion | Status | Evidence |
|-----------|--------|----------|
| C-01 through C-10 | PASS | Inherited |
| C-16 through C-29 | PASS | Inherited; C-26 (baseline comparison in completion lines) already passing, C-30 extends it structurally |
| **C-31** | **PASS** | From V-01 component: FRAMER routing prohibition present |
| **C-32** | **PASS** | From V-02 component: CALIBRATE COMPLETE embeds triple with values |
| **C-30** | **PASS** | Three-column table in Phase 7 with all three columns populated: predicted outcome, observed outcome, inertia competitor baseline — structural completeness enforced by table format |
| **C-12** | **PASS** | By construction: per rubric, "a populated three-column results table is a structural expression of effect size (C-12) by construction" — +2 pts (excellence) |
| C-11, C-13–C-15 | FAIL | No other excellence criteria addressed by these modifications |

**Regression check**: Three-column table in Phase 7 does not alter CALIBRATE or FRAMER structure; C-31 and C-32 gains preserved. C-30 prerequisite chain satisfied (C-26 already passing).

**V-05 score: 201 + 7 + 7 + 7 + 2 = 224 pts**

---

## Composite Score Summary

| Variation | Score | / 232 | Delta vs. R9-V-03 | New Criteria |
|-----------|-------|-------|-------------------|--------------|
| V-03 | 201 | 86.6% | +0 | None |
| V-01 | 208 | 89.7% | +7 | C-31 |
| V-02 | 208 | 89.7% | +7 | C-32 |
| V-04 | 215 | 92.7% | +14 | C-31 + C-32 |
| **V-05** | **224** | **96.6%** | **+23** | **C-31 + C-32 + C-30 + C-12** |

**Ranking**: V-05 > V-04 > V-01 = V-02 > V-03

---

## Excellence Signals from V-05

**1. Routing language makes prohibitions scannable across two independent dimensions.** A prohibition that states only what's excluded ("Must NOT write: inertia competitor identification") creates a single detection surface — body-text reading. A prohibition that adds routing destination ("prohibited in DESIGN — belongs exclusively in CALIBRATE") creates a second, independent surface: role-label scanning alone can verify both that FRAMER excluded the content AND that CALIBRATE owns it. C-31 + C-29 now operate orthogonally.

**2. Completion lines with embedded values collapse audit into a single scan line.** The shift from labels ("B-00 committed") to label-value pairs ("B-00 committed = 42ms") upgrades CALIBRATE COMPLETE from a phase-assertion to a structured audit record. A reader scanning only completion lines can verify the full triple — competitor, value, threshold — without entering the container body. This is the qualitative difference between C-20/C-22 and C-32.

**3. Three-column table satisfies C-12 by structural construction, not by explicit quantification.** By requiring all three columns (predicted / observed / baseline) to be populated, the table enforces that the reader cannot ignore the effect-size comparison — the delta between observed and baseline is unavoidable. This makes C-12 (effect-size quantification) a structural byproduct of C-30 rather than a separate prose requirement.

---

```json
{"top_score": 224, "all_essential_pass": true, "new_patterns": ["FRAMER prohibition must specify routing destination ('belongs exclusively in CALIBRATE'), not just exclusion, to enable role-label scan independent of container scan", "CALIBRATE COMPLETE must embed actual result values for all three triple elements — not just labels — so a scan-only auditor can verify full discharge without reading the container body", "Three-column table (predicted / observed / baseline) encodes effect size by structural construction, satisfying C-12 as a byproduct without requiring separate explicit quantification prose"]}
```
