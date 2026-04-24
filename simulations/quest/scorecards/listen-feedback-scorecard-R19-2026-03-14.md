# listen-feedback — Round 19 Scoring (Rubric v17)

## Criterion Evaluation Matrix

### Essential Criteria (C-01 to C-05)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 — 12 persona cards | PASS | PASS | PASS | PASS | PASS |
| C-02 — NPS + justification per card | PASS | PASS | PASS | PASS | PASS |
| C-03 — Severity-labeled feedback | PASS | PASS | PASS | PASS | PASS |
| C-04 — Aggregate NPS + threshold | PASS | PASS | PASS | PASS | PASS |
| C-05 — Cross-persona theme matrix | PASS | PASS | PASS | PASS | PASS |

Evidence: All five variations specify the complete protocol structure — numbered field manifest, aggregate Step 5 with threshold 7.0, and theme matrix with peak-severity ordering. No variation fails any essential criterion. `all_essential_pass = true` for all.

---

### Recommended Criteria (R-01)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| R-01 — Blocking escalation section | PASS | PASS | PASS | PASS | PASS |

All variations include a dedicated blocker escalation section. V-01 names it "Step 2 — Blocker Escalation"; V-02 uses "Blocker Escalation" inline; V-03/V-04/V-05 carry the same structure.

---

### Depth Criteria — A-25 (UX-before-PM rationale co-located)

| V | Score | Evidence |
|---|-------|----------|
| V-01 | PARTIAL (3) | "UX Read precedes PM Read in this section." — ordering stated but rationale not co-located within the ordering instruction; no failure-mode prevented stated at the instruction point. |
| V-02 | PASS (5) | "Role ordering and rationale (stated here, at the ordering instruction): The UX Read runs before the PM Read. Failure mode prevented: if PM Read preceded UX Read, commercial framing would anchor usability assessment..." — rationale and failure mode are embedded in the ordering instruction itself. |
| V-03 | PASS (5) | Lifecycle-emphasis structure carries A-25 compliance from Round 18 baseline — rationale co-located. |
| V-04 | PASS (5) | Dual-enforcement structure retains A-25 compliance. |
| V-05 | PASS (5) | Derivation + co-located failure mode structure retains A-25 compliance. |

---

### Depth Criteria — A-27 (Failure mode annotation)

| V | Score | Evidence |
|---|-------|----------|
| V-01 | PARTIAL (3) | Structural enforcement present ([SCORE BLOCK] + [CI BLOCK] mandatory), but no failure mode named for the CI formula constraint within Step S.1 or at the constraint point. |
| V-02 | PARTIAL (3) | Inline formula reference; no failure mode annotation for CI formula. |
| V-03 | PARTIAL (3) | D.1–D.4 derivation phase enforces formula at generation time but does not name the failure mode within the derivation step. |
| V-04 | PARTIAL (3) | Dual enforcement adds verification robustness but failure mode for CI formula still not named at constraint point. |
| V-05 | PASS (5) | Failure mode named within D.1: "Without the formula parenthetical (±1.96·[SD_value]/√12) alongside the interval, the CI annotation cannot be verified against different score inputs — a reader cannot confirm whether the interval was computed as ±1.96·SD/√12 or via a different method." Co-located per A-31 pattern. |

---

### Depth Criteria — A-29 (CI formula present)

| V | Score | Evidence |
|---|-------|----------|
| V-01 | PASS (5) | Mandatory [CI BLOCK]: "CI Formula: ±1.96·(SD/√12)" + "Report as: '[mean] ± [margin] using formula ±1.96·[SD_value]/√12'" — output-format enforcement at inspection time. |
| V-02 | PARTIAL (3) | Inline formula in aggregate section; no structural enforcement block; template gap — formula could be omitted without triggering structural validation failure. |
| V-03 | PASS (5) | D.1 requires formula statement as first derivation step — generation-time enforcement; formula is input to computation, not output decoration. |
| V-04 | PASS (5) | Dual enforcement: derivation-phase (D.1) + output-format block. Formula verifiable at two independent levels. |
| V-05 | PASS (5) | Same dual enforcement as V-04, with additional failure mode annotation (A-31). |

---

### Depth Criteria — A-30 (Derivation-phase protocol)

| V | Score | Evidence |
|---|-------|----------|
| V-01 | FAIL (0) | No derivation phase. [CI BLOCK] operates at output-inspection time only. An evaluator could construct the CI block after computing the mean without ever having stated the formula as a required computation input. |
| V-02 | FAIL (0) | No derivation phase. Inline formula reference at reporting time only. |
| V-03 | PASS (5) | Explicit D.1–D.4 phase (D.1 state formula → D.2 compute SD → D.3 apply → D.4 report) makes formula omission structurally detectable before output inspection. |
| V-04 | PASS (5) | D.1–D.4 phase present; output-format block provides second enforcement layer. Pass condition satisfied. |
| V-05 | PASS (5) | D.1–D.4 phase present with failure mode co-located at D.1. |

---

### Depth Criteria — A-31 (CI formula failure mode at point of constraint)

| V | Score | Evidence |
|---|-------|----------|
| V-01 | FAIL (0) | [CI BLOCK] contains structural formula requirement but zero failure mode statement at that instruction. A reader following the [CI BLOCK] instruction encounters the rule without its epistemic grounding. |
| V-02 | FAIL (0) | No derivation phase, no co-located failure mode. |
| V-03 | FAIL (0) | D.1 requires formula statement but does not name the failure mode prevented by requiring it. The failure mode is absent from the constraint point. |
| V-04 | FAIL (0) | Dual enforcement adds verification points; neither enforcement location contains the failure mode statement. |
| V-05 | PASS (5) | Failure mode named within D.1 itself — co-located parallel to A-25 pattern. A reader following D.1 encounters both the rule ("state the CI formula: ±1.96·SD/√12") and the reason it must be present ("without it, a reader cannot confirm whether the interval was computed as ±1.96·SD/√12 or via a different method"). Single-pass comprehension; no cross-referencing required. |

---

## Composite Scores

### Scoring key
- Essential (C-01 to C-05): 10 pts each = 50 pts max
- Recommended (R-01): 5 pts
- A-criteria (visible): PASS = 5 pts, PARTIAL = 3 pts, FAIL = 0 pts; 5 criteria shown = 25 pts max
- Non-visible A-criteria baseline (~20 criteria): assumed at 75% (3.75 pts avg × 20 = 75 pts) for all variations, as no differentiating evidence available

| Criterion | Max | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-----|------|------|------|------|------|
| C-01 to C-05 | 50 | 50 | 50 | 50 | 50 | 50 |
| R-01 | 5 | 5 | 5 | 5 | 5 | 5 |
| A-25 | 5 | 3 | 5 | 5 | 5 | 5 |
| A-27 | 5 | 3 | 3 | 3 | 3 | 5 |
| A-29 | 5 | 5 | 3 | 5 | 5 | 5 |
| A-30 | 5 | 0 | 0 | 5 | 5 | 5 |
| A-31 | 5 | 0 | 0 | 0 | 0 | 5 |
| Non-visible baseline | 165 | 75 | 75 | 75 | 75 | 75 |
| **TOTAL** | **245** | **141** | **141** | **148** | **148** | **155** |

---

## Rankings

| Rank | Variation | Score | Key Differentiator |
|------|-----------|-------|-------------------|
| 1 | **V-05** | **155** | A-27 + A-29 + A-30 + A-31 all PASS; co-located failure mode at D.1 |
| 2 | **V-04** | **148** | A-29 + A-30 PASS (dual enforcement); A-31 FAIL |
| 2 | **V-03** | **148** | A-29 + A-30 PASS (derivation-phase); A-31 FAIL |
| 4 | **V-01** | **141** | A-29 PASS (output-format only); A-25 PARTIAL; A-30/A-31 FAIL |
| 4 | **V-02** | **141** | A-25 PASS; A-29 PARTIAL (weakest CI enforcement); A-30/A-31 FAIL |

V-04 and V-03 are tied — both add derivation phase (A-30) over V-01/V-02 but neither reaches A-31 compliance. V-04's dual enforcement adds robustness not captured in the current rubric; V-03's single derivation-phase is sufficient to pass A-30. V-01 and V-02 net-cancel: V-01 gains A-29 PASS but loses A-25 PARTIAL; V-02 gains A-25 PASS but loses A-29 PARTIAL.

---

## Excellence Signals

**V-05 — co-location as the structural principle**

The pattern holding V-05 above V-03/V-04 is not just that it adds a failure mode statement — it is that the failure mode appears *at the constraint point*, not in a separate rationale section. The reader following D.1 encounters the rule and its epistemic grounding in a single pass:

> "State the CI formula: ±1.96·SD/√12. Without the formula parenthetical ... the CI annotation cannot be verified against different score inputs."

This parallels A-25 exactly: A-25 requires UX-before-PM rationale within the ordering instruction; A-31 requires CI formula failure mode within the derivation step. Both are instances of the same structural principle: **enforcement and rationale are co-located so that compliance cannot be separated from understanding**.

V-01 enforces compliance (structure ensures formula is in output). V-03 enforces correctness (derivation ensures formula is computed first). V-05 enforces understanding (constraint instruction ensures reader knows *why* the formula is required). These are three distinct enforcement levels.

---

```json
{"top_score": 155, "all_essential_pass": true, "new_patterns": []}
```
