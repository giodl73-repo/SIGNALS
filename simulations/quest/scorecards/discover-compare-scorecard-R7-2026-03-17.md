Scorecard written. Here is the full result:

---

## discover-compare R7 — Scorecard

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": []}
```

---

### Summary

| Variation | C-20 | C-21 | Composite | Golden |
|-----------|------|------|-----------|--------|
| V-01 | PASS | PASS | **100.00** | YES |
| V-02 | PARTIAL — register over-recalls ANCHOR[0] | PASS | 99.64 | YES |
| V-03 | PARTIAL — Add-C over-recalls REG | PASS | 99.64 | YES |
| V-04 | PARTIAL — Weight over-recalls REG | PASS | 99.64 | YES |
| V-05 | PASS | PARTIAL — Weight single-polarity FAULT | 99.64 | YES |

---

### Key Resolutions

**V-01 on C-20: PASS** — confirmed. ANCHOR[0]-only at Add-C and Weight is the correct minimal form. REG is established in Phase 0 and inherited; option-addition and weight paths are ANCHOR[0] consumers, not register re-declarers. Explicit REG recall at these paths = over-recall.

**V-02 on C-20: PARTIAL** — confirmed. ANCHOR[0] at the register path fires over-recall correctly. Status-quo evaluation is not part of register override; C-20 penalizes surplus tokens.

**V-03/V-04 TESTING → PARTIAL** — both resolve to 99.64. The "projected PASS" interpretation (REG required for execution) does not hold. REG-framed outputs at option-addition and weight paths are produced from inherited register context, not from an explicit path-local recall. The projections were wrong on this branch.

**V-05 on C-21: PARTIAL** — confirmed. Single-polarity FAULT at one AMEND path yields PARTIAL, not FAIL. C-21 grades proportionally across paths; zero-tolerance does not apply.

---

### Projected vs. Actual

| Hypothesis | Projected | Actual | Match |
|------------|-----------|--------|-------|
| V-01 C-20 PASS / 100.00 | 100.00 | 100.00 | YES |
| V-02 C-20 PARTIAL / 99.64 | 99.64 | 99.64 | YES |
| V-03 TESTING | 100.00 | 99.64 | **NO** — over-recall at Add-C |
| V-04 TESTING | 100.00 | 99.64 | **NO** — over-recall at Weight |
| V-05 C-21 PARTIAL / 99.64 | 99.64 | 99.64 | YES |

3 of 5 match. V-03/V-04 resolved in the opposite direction from the optimistic projection. v6 rubric is now fully calibrated — no open questions remain.
|
| **C-21 FAULT propagates to AMEND** | **PASS** | **PASS** | **PASS** | **PASS** | **PARTIAL** |

---

### Scoring Worksheet

Aspirational: PASS=1.0, PARTIAL=0.5; denominator=14; weight=10

| Variation | Essential 4/4 | Recommended 3/3 | Aspirational /14 | Composite |
|-----------|--------------|-----------------|-----------------|-----------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 14/14 = 10.00 | **100.00** |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 13.5/14 = 9.64 | **99.64** |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 13.5/14 = 9.64 | **99.64** |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 13.5/14 = 9.64 | **99.64** |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 13.5/14 = 9.64 | **99.64** |

---

### Projected vs. Actual

| Hypothesis | Projected | Actual | Match |
|------------|-----------|--------|-------|
| V-01 C-20 PASS / 100.00 | 100.00 | 100.00 | YES |
| V-02 C-20 PARTIAL / 99.64 | 99.64 | 99.64 | YES |
| V-03 C-20 TESTING (100.00 or 99.64) | 100.00 (projected PASS) | 99.64 | NO -- REG is over-recall at Add-C |
| V-04 C-20 TESTING (100.00 or 99.64) | 100.00 (projected PASS) | 99.64 | NO -- REG is over-recall at Weight |
| V-05 C-21 PARTIAL / 99.64 | 99.64 | 99.64 | YES |

**V-03/V-04 resolution:** "Any register token required for their execution" at option-addition and weight paths is satisfied by Phase 0 inheritance. These paths produce token outputs (FEAS-C, INERT-C, WEIGHT); their REG-framing is inherited, not re-declared. Adding explicit REG recall = over-recall. V-01's ANCHOR[0]-only form is the correct minimal for both paths.

---

### Excellence Signals (from V-01)

1. **Minimal recall is correct recall** -- REG declared once in Phase 0 propagates to all downstream phases without path-local re-declaration; option-addition and weight paths are ANCHOR[0] consumers, not REG consumers.
2. **AMEND path-type asymmetry** -- register path requires REG (its function is register re-declaration); option-addition and weight paths require ANCHOR[0] (their function involves status-quo comparison); token sets differ by operational function, not by convention.
3. **Dual-polarity FAULT discipline holds across all amendment paths** -- C-18 one-liner form propagates intact; no degradation at the primary/AMEND boundary.

---

### Key Decisions for R8

C-20 and C-21 are now calibrated. V-01 is the stable 100/100 form under v6. No open questions remain on these two criteria. v6 rubric is complete and stable. R7 produces no new patterns -- the V-03/V-04 boundary confirms over-recall at non-register AMEND paths fires C-20 PARTIAL, exactly as defined.
