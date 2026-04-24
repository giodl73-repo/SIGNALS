## trace-state · R20 Score · Rubric v18

---

### Scoring Basis

- Pool: 46 aspirational criteria (C-09..C-55)
- Unit: 50/46 ≈ 1.09 pts
- PARTIAL unit: 0.55 pts
- R19 baselines: V-01/V-03 = 28 PASS (80.5); V-02 = 29 PASS (81.6); V-04/V-05 = 37 PASS (90.3)
- R20 target: C-54 for V-01/V-03; C-54 + C-55 for V-04/V-05

---

### V-01 — Sales, Single-Pass Tabular

**R20 changes assessed:**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-51 | PASS (carried) | Arc Position column in LIFECYCLE EPOCH MAP; all four canonical roles assigned per epoch row (C11); GATE B confirms |
| C-52 | auto-FAIL | Single-domain |
| C-53 | auto-FAIL | Single-pass |
| C-54 | **PASS** | C12 in CONSTRAINT MATRIX mandates "IS NOT an [epoch-label] finding; IS a [structural-role] finding" within the remediation implication body. GATE A and GATE D carry explicit C12 acknowledgments. EPOCH-CLUSTER ANALYSIS has a dedicated C-54 REQUIREMENT block with mandatory IS-NOT/IS form and a complete example: "IS NOT a QUALIFY epoch-name finding; IS a Gate boundary structural-role finding." The contrast appears in the remediation implication field itself — not only in preamble or criterion annotation. Prerequisites C-49 + C-51 both PASS. |
| C-55 | auto-FAIL | Single-domain |

**R20 new PASS: C-54. Total PASS: 29.**

**Score: 50 + 29 × 1.09 = 81.6**

---

### V-02 — Finance, Single-Pass Tabular (Carried)

**R20 changes assessed:**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-51 | PASS (carried) | Arc Position column; Finance epoch arc positions named per epoch in LIFECYCLE EPOCH MAP |
| C-52 | auto-FAIL | Single-domain |
| C-53 | auto-FAIL | Single-pass |
| C-54 | PASS (carried) | IS-NOT/IS canonical contrast already present in R19: "IS NOT a REVIEW epoch-name finding; IS a Gate boundary structural-role finding" in V-02 SYNERGY REQUIREMENT block and remediation implication template. C-54 PASS is carried unchanged. |
| C-55 | auto-FAIL | Single-domain |

**R20 new PASS: none (carried). Total PASS: 29.**

**Score: 50 + 29 × 1.09 = 81.6**

---

### V-03 — Customer Service, Step-Block Format

**R20 changes assessed:**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-51 | PASS (carried) | `[Arc: structural role]` inline tags on LIFECYCLE EPOCH MAP epoch entries; ECL-3 step names structural role of highest-density epoch; format-neutral path confirmed |
| C-52 | auto-FAIL | Single-domain |
| C-53 | auto-FAIL | Single-pass |
| C-54 | **PASS** | C11 R20 extension explicitly adds: "The ECL-4 remediation step IS REQUIRED to use the IS-NOT/IS canonical contrast form: 'IS NOT an [epoch-label] finding; IS a [structural-role] finding.' An ECL-4 step that IS role-grounded without explicit IS-NOT/IS contrast IS NOT C-54-compliant." GATE A adds C11 acknowledgment for ECL-4 contrast. GATE D confirms ECL-4 WILL contain IS-NOT/IS contrast within step body. ECL-4 template provides the Required ECL-4 form with complete example: "RESOLUTION epoch Arc Terminal settlement carries [N] of [total] defects — IS NOT a RESOLUTION epoch-name finding; IS a Terminal settlement structural-role finding." Per rubric scoring note: step-block format may satisfy C-54 within the ECL-3 or ECL-4 step; the step names both the negated epoch label and the affirmed structural role. Prerequisites C-49 (via ECL section) + C-51 (via Arc-tags) both PASS. |
| C-55 | auto-FAIL | Single-domain |

**R20 new PASS: C-54. Total PASS: 29.**

**Score: 50 + 29 × 1.09 = 81.6**

> Format-neutral C-54 path confirmed: step-block ECL-4 is a valid C-54 surface; the required contrast form is present within the remediation step body, not only in section preamble.

---

### V-04 — Finance → Sales, Two-Pass

**R20 changes assessed:**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-51 | PASS (carried) | Arc Position column in both Finance and Sales LIFECYCLE EPOCH MAPs; epoch-level structural role assignments present per domain |
| C-52 | PASS (carried) | EPOCH-CLUSTER spans both Finance and Sales epoch vocabularies; cross-domain highest-density epoch named; remediation implication targets inter-domain handoff boundary (R18) |
| C-53 | PASS (carried) | BRIDGE TABLE with source-domain/target-domain labeling on F-to-S rows; C-47 citations reference named bridge rows (R18) |
| C-54 | **PASS** | C12 R20 encodes IS-NOT/IS per domain requirement. Finance per-domain remediation template: "IS NOT a [Finance-epoch-label] epoch-name finding; IS a [Finance-structural-role] structural-role finding." Sales per-domain remediation template: "IS NOT a [Sales-epoch-label] epoch-name finding; IS a [Sales-structural-role] structural-role finding." Both appear within their respective C-49-bearing per-domain remediation fields (not preamble-only). C-54 requires at least one C-49 finding with IS-NOT/IS contrast — both domains carry it; no PARTIAL. C-49 + C-51 both PASS per domain. |
| C-55 | **PASS** | C12 R20 extension encodes C-55 requirement: "The cross-domain EPOCH-CLUSTER ANALYSIS remediation implication IS REQUIRED to name the structural roles on BOTH sides of the Finance to Sales handoff boundary." The EPOCH-CLUSTER ANALYSIS inter-domain template provides the C-55 form: "IS NOT a Finance-[epoch-label] to Sales-[epoch-label] handoff problem; IS a Finance-[structural-role] to Sales-[structural-role] structural mismatch at the inter-domain handoff boundary." Example confirms structural roles on both sides: "IS NOT a Finance-REVIEW to Sales-OPEN-TRACK handoff problem; IS a Finance-Gate-boundary to Sales-Entry-boundary structural mismatch." C-52 PASS (carried) and C-51 PASS per domain satisfy C-55 prerequisites. Single-pass auto-FAIL does not apply (multi-pass). |

**R20 new PASS: C-54, C-55. Total PASS: 39.**

**Score: 50 + 39 × 1.09 = 92.5**

---

### V-05 — Finance → Sales → CS, Three-Pass

**R20 changes assessed:**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-51 | PASS (carried) | Arc Position column in all three LIFECYCLE EPOCH MAPs (Finance, Sales, CS); C13 violation enforced on missing Arc Position rows |
| C-52 | PASS (carried) | EPOCH-CLUSTER spans all three domain epoch vocabularies; cross-domain highest-density epoch + inter-domain handoff remediation implications (R18) |
| C-53 | PASS (carried) | BRIDGE TABLE F-to-S and BRIDGE TABLE S-to-CS; C-47 citations reference named bridge rows (R18); PARTIAL rule for missing rows is satisfied — both inter-domain bridge tables present |
| C-54 | **PASS** | C13 R20 encodes C-54 per domain across all three: "Each domain's per-domain C-49 remediation finding IS REQUIRED to use IS-NOT/IS canonical contrast form." Three independent per-domain remediation templates: Finance ("IS NOT a [Finance-epoch-label]…; IS a [Finance-structural-role]…"), Sales (same form), CS (same form). All three appear within per-domain remediation fields — not preamble-only. Three separate C-54-bearing findings; no PARTIAL. |
| C-55 | **PASS** | C13 R20 extension: both inter-domain handoff remediations required to name structural roles on BOTH sides of BOTH boundaries. Finance-to-Sales C-55 form present with example: "IS NOT a Finance-REVIEW to Sales-OPEN-TRACK handoff problem; IS a Finance-Gate-boundary to Sales-Entry-boundary structural mismatch." Sales-to-CS C-55 form present with example: "IS NOT a Sales-ADVANCE to CS-INTAKE handoff problem; IS a Sales-Approval-event to CS-Entry-boundary structural mismatch." Both inter-domain handoff boundaries satisfy the C-55 naming requirement independently. C-52 PASS and C-51 per domain PASS satisfy prerequisites. |

**R20 new PASS: C-54, C-55. Total PASS: 39.**

**Score: 50 + 39 × 1.09 = 92.5**

---

### Round 20 Score Table

| Variant | New PASS | Total PASS | Score |
|---------|----------|------------|-------|
| V-01 (Sales, single-pass tabular) | C-54 | 29 | **81.6** |
| V-02 (Finance, single-pass carried) | — | 29 | **81.6** |
| V-03 (CS, step-block) | C-54 | 29 | **81.6** |
| V-04 (Finance→Sales, two-pass) | C-54, C-55 | 39 | **92.5** |
| V-05 (Finance→Sales→CS, three-pass) | C-54, C-55 | 39 | **92.5** |

**Top score: V-04 and V-05 tied at 92.5. All predicted R20 scores confirmed.**

---

### Excellence Signals

**V-04 / V-05 are jointly top-scoring.** What made them better than V-01/V-02/V-03:

1. **DOMAIN DEPENDENCY DECLARATION pre-announces C-55 structural-role form.** Both V-04 and V-05 extend the C-50 DOMAIN DEPENDENCY DECLARATION with an "Arc Position cross-domain note" that explicitly names the structural-role requirement for the EPOCH-CLUSTER handoff remediation before any epoch maps exist. C-50 only requires naming the source-of-record domain and dependency chain — V-04/V-05 go beyond by declaring *the form* the inter-domain synthesis must take ("The boundary IS NOT the Finance-APPROVAL to Sales-ADVANCE boundary; it IS the Finance Gate-boundary or Approval-event structural role to the Sales Entry-boundary structural role boundary"). This creates a front-to-back structural commitment: the dependency declaration seeds the synthesis conclusion. A reader can verify C-55 compliance by comparing the DOMAIN DEPENDENCY DECLARATION arc-position note against the EPOCH-CLUSTER synthesis output.

2. **Single CONSTRAINT MATRIX row encodes both C-54 and C-55 as a unified epoch-role-grounding constraint.** C12 (V-04) and C13 (V-05) fuse per-domain IS-NOT/IS (C-54) and cross-domain structural-role handoff naming (C-55) into one constraint ID. This is architecturally significant: it signals that per-domain role-grounding (C-54) and cross-domain role-grounding (C-55) are semantically coupled — satisfying both requires a single coherent structural-role vocabulary deployed at two scales simultaneously. The single-row encoding also reveals the dependency direction: a practitioner must first satisfy C-54 per domain before C-55 at the handoff boundary is achievable, and the constraint row enforces this ordering by describing both requirements in the same scope.

---

```json
{"top_score": 92.5, "all_essential_pass": true, "new_patterns": ["DOMAIN DEPENDENCY DECLARATION pre-announces C-55 structural-role form before epoch maps exist — the C-50 topology statement is extended with an Arc Position cross-domain note that names the structural roles that will appear in the EPOCH-CLUSTER inter-domain handoff remediation, creating a verifiable front-to-back commitment", "Single CONSTRAINT MATRIX row encodes both C-54 per-domain IS-NOT/IS and C-55 cross-domain structural-role handoff requirements as a unified epoch-role-grounding constraint, exposing their semantic coupling and ordering dependency"]}
```
