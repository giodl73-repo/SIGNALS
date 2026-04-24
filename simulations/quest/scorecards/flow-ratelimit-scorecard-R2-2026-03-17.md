## Quest Score — flow-ratelimit Round 2

**Rubric**: v2 (120-pt composite, 5 essential, 3 recommended, 6 aspirational)
**Variations**: V-01 (lifecycle-first / structural gap lock) and V-02 (dual-state format contract)

---

## V-01 — Scorecard

**Axis**: Structural gap audit FIRST, volume cascade SECOND via sequential section lock

### Essential (60 pts)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | First-limit Ordering | **PASS** | Section 3 provides arithmetic template: "At [volume] req/min, [component] exhausts [limit] of [threshold] because [calculation]. This occurs before [next limit]..." — forces binding constraint with calculation before listing others. |
| C-02 | Backpressure Propagation Chain | **PASS** | Section 4 requires causal chain with directional mechanism template including two hops minimum; explicitly rejects "both components are affected." |
| C-03 | User Experience at Each Throttle Tier | **PASS** | Section 5 asks error/delay, silent vs visible, recovery path per tier. |
| C-04 | Unprotected Burst Path Identification | **PASS** | Section 1 is a dedicated structural audit table requiring all three protections per path with UNPROTECTED marking. Explicitly excludes "controls at a different tier" from passing. |
| C-05 | Retry-After Handling Gap Check | **PASS** | Section 9 dedicated to Retry-After, lists equivalent headers, requires failure mode description. |

**Essential: 5/5 → 60 pts**

### Recommended (30 pts)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Cascading Throttle Failure | **PASS** | Section 6 defines cascade vs. independent; requires compounding effect on throughput/error rate. |
| C-07 | Numeric Rate Limit Specificity | **PASS** | Section 2 requires numeric threshold per limit, [estimated] label for unknowns. |
| C-08 | Volume-to-Behavior Mapping | **PASS** | Section 7 table: Volume Range / First Limit Hit / User-Visible Behavior / Retry-After Handled. |

**Recommended: 3/3 → 30 pts**

### Aspirational (30 pts)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Per-bottleneck Mitigation Prescriptions | **PASS** | Section 8 requires "exact action, connector setting, or pattern," baseline before, behavior after; explicitly rejects generic advice. |
| C-10 | Quantified Impact at Load Spike | **PARTIAL** | Section 7 volume table is present but doesn't force numeric degradation estimates derived from stated rate limits (e.g., "42% of requests queued"). Behavior descriptions are qualitative. |
| C-11 | Burst Gap Classification (Structural vs. Incidental) | **PASS** | Section 1 table column "Gap Type" requires Structural/Incidental classification with "name the condition" for Incidental. Explicit definitions provided. |
| C-12 | Dual-state Volume Mapping (Baseline vs. Protected) | **FAIL** | Section 7 table has columns: Volume Range / First Limit Hit / User-Visible Behavior / Retry-After Handled — no BASELINE vs. PROTECTED split. Dual-state not enforced. |
| C-13 | Verdict-before-Evidence Structure | **PARTIAL** | Section 3 forces arithmetic before listing secondary limits and says "State the binding constraint explicitly," which is a commitment position. But it sits mid-document after Section 1 and 2 — no doc-level labeled verdict before any evidence. Labeled commitment is structural, not global. |
| C-14 | Baseline-delta Mitigation | **PASS** | Section 8 explicitly: "State the baseline behavior before the mitigation / State the system behavior after." Directly enforces before/after per mitigation without naming C-14. |

**Aspirational: 4 PASS + 2 PARTIAL = 5.0 effective / 6 → 25 pts**

### V-01 Composite

```
essential:    60
recommended:  30
aspirational: 25  (5.0/6 × 30)
─────────────────
composite:   115 / 120
```

**Band: GOLD** (>= 95, all essential pass)

---

## V-02 — Scorecard

**Axis**: Format contract preamble — BASELINE / PROTECTED dual-column on every table and mitigation

### Essential (60 pts)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | First-limit Ordering | **PASS** | "Binding Constraint Analysis" section with bold labeled format **Binding constraint**: [component] — [limit] — exhausted at [volume] because [arithmetic], then list in order. |
| C-02 | Backpressure Propagation Chain | **PASS** | Section requires at least two hops, directionality, and user-observable terminus. |
| C-03 | User Experience at Each Throttle Tier | **PASS** | Table with What User Sees / Silent or Visible / Recovery Path per tier. |
| C-04 | Unprotected Burst Path Identification | **PASS** | Table with Gap Type (Structural/Incidental/Protected) and Missing Control(s); three-control check implied by gap taxonomy. |
| C-05 | Retry-After Handling Gap Check | **PASS** | Dedicated "Retry-After Handling Assessment" section with failure mode requirement. |

**Essential: 5/5 → 60 pts**

### Recommended (30 pts)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Cascading Throttle Failure | **PASS** | Section explicitly distinguishes cascade from independent limits hitting under load. |
| C-07 | Numeric Rate Limit Specificity | **PASS** | Rate Limit Inventory with [est] labels required. |
| C-08 | Volume-to-Behavior Mapping | **PASS** | Volume-to-Behavior Map table present and enhanced with BASELINE/PROTECTED columns. |

**Recommended: 3/3 → 30 pts**

### Aspirational (30 pts)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Per-bottleneck Mitigation Prescriptions | **PASS** | Table columns: Finding / BASELINE STATE / PROTECTED STATE / Specific Change Required; generic advice clause "will be discarded." |
| C-10 | Quantified Impact at Load Spike | **FAIL** | Volume map has baseline/protected columns but no requirement to derive numeric failure percentages from stated rate limits. Qualitative only. |
| C-11 | Burst Gap Classification (Structural vs. Incidental) | **PASS** | Gap Type taxonomy in burst path table requires Structural/Incidental/Protected with condition for Incidental. |
| C-12 | Dual-state Volume Mapping (Baseline vs. Protected) | **PASS** | Volume-to-Behavior Map has explicit BASELINE Behavior / PROTECTED Behavior / Delta columns — strongest C-12 enforcement of either variation. |
| C-13 | Verdict-before-Evidence Structure | **PARTIAL** | **Binding constraint**: bold label in the analysis section is the closest this prompt gets to a commitment-before-evidence position. The format contract preamble doesn't require a global verdict at document head; the labeled constraint appears within a mid-document section. |
| C-14 | Baseline-delta Mitigation | **PASS** | Mitigation table BASELINE STATE / PROTECTED STATE columns plus "Mitigations that describe improvements without referencing the current baseline condition will be discarded" — strong enforcement. |

**Aspirational: 4 PASS + 1 PARTIAL + 1 FAIL = 4.5 effective / 6 → 22.5 pts**

### V-02 Composite

```
essential:    60
recommended:  30
aspirational: 22.5  (4.5/6 × 30)
─────────────────
composite:   112.5 / 120
```

**Band: GOLD** (>= 95, all essential pass)

---

## Head-to-Head

| | V-01 | V-02 |
|---|------|------|
| Essential | 5/5 | 5/5 |
| Recommended | 3/3 | 3/3 |
| C-09 Mitigations | PASS | PASS |
| C-10 Quantified load | PARTIAL | FAIL |
| C-11 Gap classification | PASS | PASS |
| C-12 Dual-state volume | **FAIL** | **PASS** |
| C-13 Verdict-first | PARTIAL | PARTIAL |
| C-14 Baseline-delta | PASS | PASS |
| **Composite** | **115** | **112.5** |

**Winner: V-01 (115 / 120)**

V-01's margin comes from C-10 PARTIAL vs V-02's FAIL. V-02 wins C-12 cleanly but not enough to close the gap.

---

## Excellence Signals — V-01

**ES-1: Sequential section lock as a commitment device.** "Do not proceed to Section 2 until this table is complete." Forcing the structural gap audit before any volume math prevents the model from rationalizing a partially-protected path as "covered at a higher tier" once it already has the volume numbers in view. The lock creates ordered epistemic commitment, not just ordered output sections.

**ES-2: Explicit inline negative exclusion.** "A path that has throttle controls but at a higher tier than the one it hits does NOT qualify as protected." Anticipatory negative examples inside the section instruction suppress the most common misclassification before it happens. V-02's taxonomy (Protected/Structural/Incidental) achieves similar coverage but requires inferring the exclusion from definitions rather than stating it explicitly.

**ES-3: Three-protection checklist enumeration.** Naming all three required controls (concurrency cap, Retry-After retry policy, connector-tier rate guard) as a discrete checklist — not just "adequate controls" — closes the definitional gap that allows a path with one control to be classified as protected. Neither variation fully enforces C-10 (quantified load); this remains the open gap across both.

---

## Gap Note — Round 2 Open

**C-10 (Quantified Impact at Load Spike)** is PARTIAL in V-01, FAIL in V-02. No variation has closed it. Closing it requires a prompt instruction that mandates arithmetic: e.g., "State the percentage of requests expected to queue beyond [threshold] at the stated load multiplier, derived from the numeric limits in Section 2." R3 should carry at least one variation targeting C-10 specifically.

---

```json
{"top_score": 115, "all_essential_pass": true, "new_patterns": ["sequential section lock forces staged epistemic commitment before volume analysis prevents tier-rationalization of unprotected paths", "inline negative exclusion within section instruction suppresses most common misclassification before model generates the error"]}
```
