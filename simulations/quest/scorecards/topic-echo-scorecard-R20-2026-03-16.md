# Quest Score — topic-echo — Round 20

**Rubric:** v20 | **Trace:** placeholder | **Date:** 2026-03-16

---

## Scoring Basis

All five variations inherit the R19 V-05 base (350/350 under v19). The three new aspirational criteria (C-61, C-62, C-63) each carry 5 points, raising the max composite from 350 → 365.

**Base decomposition (all variations):**
- Essential (C-01–C-05): 60 pts — 5 × 12
- Recommended: 30 pts — 3 × 10
- Aspirational C-06–C-60: 260 pts — 52 × 5
- **Subtotal (pre-R20):** 350

---

## Essential Criteria — All Variations

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Pts |
|----|-----------|:----:|:----:|:----:|:----:|:----:|:---:|
| C-01 | Named surprise with departure framing | PASS | PASS | PASS | PASS | PASS | 12 |
| C-02 | Signal tracing per surprise | PASS | PASS | PASS | PASS | PASS | 12 |
| C-03 | Design impact assessed per surprise | PASS | PASS | PASS | PASS | PASS | 12 |
| C-04 | Synthesis not summary | PASS | PASS | PASS | PASS | PASS | 12 |
| C-05 | Surprise specificity | PASS | PASS | PASS | PASS | PASS | 12 |
| | **Essential subtotal** | **60** | **60** | **60** | **60** | **60** | |

All variations pass essential. All qualify as candidates.

---

## R20 Delta Criteria

### C-61 — `GATE-TOKEN-REGISTRY-COVERS-DERIVED-GATE`
*Prerequisites: C-58 + C-60. Registry must self-extend to include GT-04 (CROSS-CITATION-CONSISTENT) when C-60 is simultaneously satisfied.*

| Variation | Result | Evidence |
|-----------|:------:|---------|
| V-01 (Axis A) | **PASS** | GATE-TOKEN-REGISTRY lists GT-04 with step location Step 9 and prerequisite C-60; diff-detectable four-token completeness maintained |
| V-02 (Axis B) | FAIL | C-60 present but registry not extended; GT-04 absent from declared inventory; diff-against-registry cannot detect missing GT-04 |
| V-03 (Axis C) | FAIL | C-60 present; Step 9 produces GT-04 token; registry not extended; C-58 prerequisite unmet |
| V-04 (A+B) | **PASS** | Registry includes GT-04 (inherits Axis A); same evidence as V-01 |
| V-05 (A+B+C) | **PASS** | Registry includes GT-04; same evidence as V-01/V-04 |

---

### C-62 — `TOKEN-CONTENT-REQUIREMENT-COMPREHENSIVE`
*Prerequisites: C-59 + C-60. TOKEN CONTENT REQUIREMENT must cover all four gate tokens including GT-04's format contract (table columns, MATCH assertion, count).*

| Variation | Result | Evidence |
|-----------|:------:|---------|
| V-01 (Axis A) | FAIL | C-60 present; TOKEN CONTENT REQUIREMENT covers GT-01..GT-03 only; GT-04 format contract absent; C-59 prerequisite unmet |
| V-02 (Axis B) | **PASS** | TOKEN CONTENT REQUIREMENT declares GT-04 format contract: per-pair table columns, MATCH assertion format, count field; C-59 and C-60 both satisfied |
| V-03 (Axis C) | FAIL | C-60 present but not C-59; TOKEN CONTENT REQUIREMENT does not cover GT-04 |
| V-04 (A+B) | **PASS** | TOKEN CONTENT REQUIREMENT comprehensive (inherits Axis B); same evidence as V-02 |
| V-05 (A+B+C) | **PASS** | TOKEN CONTENT REQUIREMENT comprehensive; same evidence as V-02/V-04 |

---

### C-63 — `CROSS-CITATION-TRAVERSAL-FREE-EXPLICIT`
*Prerequisite: C-60. Step 9 must carry an explicit verification note naming what sections are NOT required, in parity with C-55's self-certifying standard for GT-01..GT-03.*

| Variation | Result | Evidence |
|-----------|:------:|---------|
| V-01 (Axis A) | FAIL | C-60 satisfied; Step 9 present; no explicit traversal-free verification note; GT-04's self-certifying contract implied but undeclared |
| V-02 (Axis B) | FAIL | C-60 satisfied; Step 9 present; same gap — no explicit note naming sections not required |
| V-03 (Axis C) | **PASS** | Step 9 carries explicit note: "CROSS-CITATION-CONSISTENT can be verified from the per-citation table without consulting STILL-LIVE FILTER or CITATION-COMPLETENESS-MANIFEST"; names sections not required in parity with C-55 |
| V-04 (A+B) | FAIL | Axis A + Axis B present; Axis C absent; traversal-free note missing from Step 9 |
| V-05 (A+B+C) | **PASS** | Step 9 carries explicit verification note (inherits Axis C); same evidence as V-03 |

---

## Composite Scores

| Variation | Axes | Essential | Recommended | Aspirational (pre-R20) | C-61 | C-62 | C-63 | **v20 Total** |
|-----------|------|:---------:|:-----------:|:----------------------:|:----:|:----:|:----:|:-------------:|
| V-01 | A | 60 | 30 | 260 | 5 | 0 | 0 | **355** |
| V-02 | B | 60 | 30 | 260 | 0 | 5 | 0 | **355** |
| V-03 | C | 60 | 30 | 260 | 0 | 0 | 5 | **355** |
| V-04 | A+B | 60 | 30 | 260 | 5 | 5 | 0 | **360** |
| **V-05** | **A+B+C** | **60** | **30** | **260** | **5** | **5** | **5** | **365** |

---

## Ranking

| Rank | Variation | Score | Gap to max |
|------|-----------|:-----:|:----------:|
| 1 | **V-05 (A+B+C)** | **365** | 0 |
| 2 | V-04 (A+B) | 360 | −5 |
| 3 | V-01 (A) | 355 | −10 |
| 3 | V-02 (B) | 355 | −10 |
| 3 | V-03 (C) | 355 | −10 |

---

## Excellence Signals — V-05

Three patterns distinguish V-05 from all other variations simultaneously:

**`GATE-TOKEN-REGISTRY-COVERS-DERIVED-GATE`**
The registry was established for GT-01..GT-03 (three-token world of C-55). When C-60 adds GT-04, the registry self-extends rather than deferring currency to a future round. The structural move: treat derived gate tokens with the same inventory discipline as original gate tokens — a registry that does not know about tokens produced by subsequently satisfied criteria is accurate but not current.

**`TOKEN-CONTENT-REQUIREMENT-COMPREHENSIVE`**
The TOKEN CONTENT REQUIREMENT section grows with the gate token set. V-05 declares the full format contract for GT-04 (table columns, MATCH assertion, count field) alongside GT-01..GT-03's contracts. The structural move: format contract coverage is a completeness property — a section that covers three of four tokens leaves the consuming reviewer unable to verify the fourth token's format from the artifact alone.

**`CROSS-CITATION-TRAVERSAL-FREE-EXPLICIT`**
Step 9 carries a verification note naming what sections are NOT required to verify CROSS-CITATION-CONSISTENT. The structural move: contract parity — the original three gate tokens have explicit self-certifying contracts (per C-55); GT-04 must have the same. The traversal-free property is real in V-03 but undeclared; V-05 makes it explicit, closing the gap between what is true and what is auditable from text alone.

**Closure property:** The three patterns form a closure set. C-61 makes the registry current. C-62 makes the format contract section current. C-63 makes the verification contract explicit. No further structural gap exists at the C-58+C-59+C-60 intersection — the intersection is now fully closed.

---

## Gate Chain Update

R10 output auditable → R11 output non-defeatable → R12 enforcement legible → R13 structure navigable → R14 element addressable → R15 address citation-activated → R16 citation exhaustively manifested, bidirectionally indexed, and chain-grounded → R17 tokens self-certifying, gates independent, manifest rows inline-evidenced → R18 token inventory declared, manifest token extended for inline-evidence, cross-layer citation consistent → R19 registry self-extends for derived gate tokens, token format contracts comprehensive, cross-citation verification contract traversal-free explicit → **R20 max composite 365/365 achieved; C-58+C-59+C-60 intersection fully closed.**

---

```json
{"top_score": 365, "all_essential_pass": true, "new_patterns": ["GATE-TOKEN-REGISTRY-COVERS-DERIVED-GATE", "TOKEN-CONTENT-REQUIREMENT-COMPREHENSIVE", "CROSS-CITATION-TRAVERSAL-FREE-EXPLICIT"]}
```
