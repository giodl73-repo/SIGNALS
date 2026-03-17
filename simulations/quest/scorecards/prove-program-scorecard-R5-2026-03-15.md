## prove-program R5 — Scoring Report

### Baseline Assumptions

All five variations are described as building on the **R4 V-05 floor** ("role sequence + verbatim blockquotes + named gates + inline FAIL"), which covers C-01 through C-19 completely.

**R4 V-05 floor score:** 145/160
- Essential (C-01–C-05): 60/60
- Recommended (C-06–C-08): 30/30
- Aspirational C-09–C-19 (11 × 5): 55/55
- New R5 criteria C-20–C-22: 0/15

---

### Per-Variation Scoring

#### C-01 through C-19 (All Variations — R4 Floor)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| C-01 Distinct hypothesis | PASS | PASS | PASS | PASS | PASS | R4 floor |
| C-02 >=2 experiment types | PASS | PASS | PASS | PASS | PASS | R4 floor |
| C-03 Feed-forward | PASS | PASS | PASS | PASS | PASS | R4 floor |
| C-04 Synthesis contrast | PASS | PASS | PASS | PASS | PASS | R4 floor |
| C-05 Qx.md format | PASS | PASS | PASS | PASS | PASS | R4 floor |
| C-06 Principles >=2 | PASS | PASS | PASS | PASS | PASS | R4 floor |
| C-07 Confidence levels | PASS | PASS | PASS | PASS | PASS | R4 floor |
| C-08 Flexibility | PASS | PASS | PASS | PASS | PASS | R4 floor |
| C-09 Falsification | PASS | PASS | PASS | PASS | PASS | R4 floor |
| C-10 Cross-namespace | PASS | PASS | PASS | PASS | PASS | R4 floor |
| C-11 Audit ledger | PASS | PASS | PASS | PASS | PASS | R4 floor |
| C-12 COMPLETE markers | PASS | PASS | PASS | PASS | PASS | R4 floor |
| C-13–C-16 (v3 asp.) | PASS | PASS | PASS | PASS | PASS | R4 floor |
| C-17 Verbatim blockquotes | PASS | PASS | PASS | PASS | PASS | R4 floor ("verbatim blockquotes") |
| C-18 Gates exist | PASS | PASS | PASS | PASS | PASS | R4 floor ("named gates") |
| C-19 Global FAIL conditions | PASS | PASS | PASS | PASS | PASS | R4 floor ("inline FAIL") |

**Subtotal (all):** 145/145

---

#### R5 New Criteria — C-20, C-21, C-22

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence note |
|-----------|------|------|------|------|------|---------------|
| **C-20** Gate-enforced hypothesis + falsification pre-check | **PASS** | FAIL | FAIL | **PASS** | **PASS** | V-01 axis: GATE-1 is a two-row A∧B table with a single named PASS. Explicit conjunction, not checklist. V-02/V-03 have no such gate. V-04/V-05 inherit from V-01. |
| **C-21** Gate-enforced confidence calibration | FAIL | **PASS** | FAIL | **PASS** | **PASS** | V-02 axis: GATE-CAL placed before synthesis; FAIL condition explicitly names "all high" as insufficient. Presence alone does not satisfy. V-01/V-03 absent. V-04/V-05 inherit from V-02. |
| **C-22** Per-consumer-block embedded citation contract | FAIL | FAIL | **PASS** | FAIL | **PASS** | V-03 axis: anti-pointer prohibition embedded in each consumer block's INPUT section as named clause "citation contract (local to this block):" — not a global preamble. V-01/V-02 absent. V-04 inherits C-20+C-21 but not C-22. V-05 adds all three. |

**R5 delta (×5 each):**

| Variation | C-20 | C-21 | C-22 | R5 delta |
|-----------|------|------|------|----------|
| V-01 | +5 | 0 | 0 | **+5** |
| V-02 | 0 | +5 | 0 | **+5** |
| V-03 | 0 | 0 | +5 | **+5** |
| V-04 | +5 | +5 | 0 | **+10** |
| V-05 | +5 | +5 | +5 | **+15** |

---

### Composite Scores

| Variation | Axes | Floor | R5 Delta | **Total** | All Essential |
|-----------|------|-------|----------|-----------|---------------|
| V-01 | C-20 | 145 | +5 | **150** | YES |
| V-02 | C-21 | 145 | +5 | **150** | YES |
| V-03 | C-22 | 145 | +5 | **150** | YES |
| V-04 | C-20+C-21 | 145 | +10 | **155** | YES |
| **V-05** | C-20+C-21+C-22 | 145 | +15 | **160** | YES |

**Ranking:** V-05 > V-04 > V-01 = V-02 = V-03

---

### Excellence Signals from V-05

Three structural patterns elevated V-05 to 160/160:

**1. Atomic conjunction gate (C-20)**
GATE-1 uses a literal two-row table (Condition A / Condition B) with a single PASS line that fires only when both rows are TRUE. This prevents the checklist failure mode where each condition is satisfied in isolation but the conjunction is never explicitly evaluated. One gate, one boolean output.

**2. Calibration gate with named non-uniformity FAIL (C-21)**
GATE-CAL does not test whether confidence values are *present* — it tests whether they are *differentiated*. The FAIL condition names "all HIGH" explicitly as an invalid outcome. This closes the loophole where a writer satisfies C-07 (presence) by assigning the same label to every finding.

**3. Per-block citation contracts (C-22)**
Rather than one global anti-pointer rule at document top, V-05 repeats the prohibition as the opening clause of each consumer block's INPUT section, labeled "citation contract (local to this block):". This removes the failure mode where a writer reads the global rule once and skips it for later blocks. The contract travels with the block.

---

```json
{"top_score": 160, "all_essential_pass": true, "new_patterns": ["atomic-conjunction-gate: one gate with explicit two-row boolean table forces conjunction semantics over checklist substitution", "calibration-gate-non-uniformity: FAIL condition names the uniform-label pattern specifically, closing the presence-vs-differentiation loophole", "per-block-citation-contract: anti-pointer prohibition embedded locally in each consumer block INPUT section, not delegated to a single global rule"]}
```
