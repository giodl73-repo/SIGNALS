## mock-accept Round 5 Scorecard — Rubric v5

---

### Structural Inventory

Before scoring: map what each variation carries at the key contested locations.

| Feature | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| C-20 form | **TABLE** (3-col) | prose | prose | **TABLE** | **TABLE** |
| C-21 form | prose enforcement | **ENFORCEMENT NOTE block** | prose enforcement | **ENFORCEMENT NOTE block** | **ENFORCEMENT NOTE block** |
| C-22 candidate | absent | absent | **present** | absent | **present** |
| Violation: field | absent | **present** | absent | **present** | **present** |
| CANARY TERMINOLOGY TABLE | present | present | present | present | present |
| Semantics: in Branch B | present | present | present | present | present |
| Subject-check sub-step | present | present | present | present | present |
| Two-list partition + guards | present | present | present | present | present |

---

### Per-Criterion Scoring — All Variations

#### Essential (60 pts — 12 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** — FORBIDDEN OUTPUTS TRIAD + completeness check + AUTO-RULE CONTAMINATION GUARD | PASS | PASS | PASS | PASS | PASS |
| **C-02** — Triad labels [EVIDENCE-HEAVY], [TIER-CRITICAL], [COMPLIANCE] all present | PASS | PASS | PASS | PASS | PASS |
| **C-03** — Status written back in-place; CANARY GATE emitted | PASS | PASS | PASS | PASS | PASS |
| **C-04** — Review artifact with 4-col table, P1/P2/P3 next-steps, cross-namespace risk statement | PASS | PASS | PASS | PASS | PASS |
| **C-05** — MOCK-ACCEPTED two-slot argument: Slot 2 (Contrast) + Slot 1 (Structural position) structurally separate | PASS | PASS | PASS | PASS | PASS |

**Essential subtotal**: 60 / 60 all variations.

---

#### Recommended (30 pts — 10 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-06** — Entity-naming grammar on all sub-questions (no yes/no substitution) | PASS | PASS | PASS | PASS | PASS |
| **C-07** — Two-list partition output; ARCH-GUARD-BYPASS + STRATEGY-TO-PM-GUARD-BYPASS named at guard sites | PASS | PASS | PASS | PASS | PASS |
| **C-08** — Evaluation-driven REAL-REQUIRED template complete: trigger field, Failing evaluation, Failing verdict, Claim, Subject-check, Error-code, Artifact state | PASS | PASS | PASS | PASS | PASS |

**Recommended subtotal**: 30 / 30 all variations.

---

#### Aspirational (1.25 pts each; denominator 13; max 16.25)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-09** through **C-16** (inherited R3 patterns — all confirmed present in R4 V-05 baseline) | 8× PASS | 8× PASS | 8× PASS | 8× PASS | 8× PASS |
| **C-17** — `Semantics: SUCCESS` labeled field in Branch B | PASS | PASS | PASS | PASS | PASS |
| **C-18** — CANARY TERMINOLOGY TABLE as dedicated non-conflation structure | PASS | PASS | PASS | PASS | PASS |
| **C-19** — Subject-check metacognitive sub-step on Error-code | PASS | PASS | PASS | PASS | PASS |
| **C-20** — Branch-anchor exemplars on both Subject-check branches | PASS — table form, both rows structurally independent | PASS — prose form, both branches named | PASS — prose form, both branches named | PASS — table form | PASS — table form |
| **C-21** — Enforcement note following CANARY TERMINOLOGY TABLE | PASS — prose: "These are distinct. Do NOT conflate them." | PASS — ENFORCEMENT NOTE block with Rule:/Distinction:/Violation: | PASS — prose form | PASS — ENFORCEMENT NOTE block | PASS — ENFORCEMENT NOTE block |

**Aspirational subtotal**: 13 × 1.25 = 16.25 / 16.25 all variations.

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 60 | 30 | 16.25 | **106.25** |
| V-02 | 60 | 30 | 16.25 | **106.25** |
| V-03 | 60 | 30 | 16.25 | **106.25** |
| V-04 | 60 | 30 | 16.25 | **106.25** |
| **V-05** | 60 | 30 | 16.25 | **106.25** |

All five variations hit the v5 ceiling. The v5 rubric is saturated — no variation can exceed 106.25 under current scoring.

---

### Excellence Signals — Cross-Variation Differential Analysis

R4 V-05 already satisfied all 21 criteria. R5 targeted structural promotion of C-20 and C-21 plus the C-22 candidate. What the R5 differential reveals:

#### C-22 — Cross-template completeness assertion

**Evidence from V-03 and V-05** (lines 839–840 in V-03; lines 1437–1438 in V-05):
```
Verify: all 7 field rows above are mapped before filling either template below.
A partial table (fewer than 7 rows) does not satisfy this correspondence requirement.
```

**V-01, V-02, V-04**: CROSS-TEMPLATE RELATIONSHIP BLOCK has no completeness check — table ends at row 7 and templates begin immediately. A model can silently truncate the table with no named error firing.

**Differential**: V-03/V-05 PASS; V-01/V-02/V-04 FAIL.

**Pattern**: "Count-anchored completeness assertion immediately following the CROSS-TEMPLATE RELATIONSHIP BLOCK, before either template definition begins. Partial-table condition named explicitly." Applies the same completeness-check mechanism as the FORBIDDEN OUTPUTS TRIAD to the template correspondence table.

---

#### C-23 — Named `Violation:` field in ENFORCEMENT NOTE block

**Evidence from V-02, V-04, V-05** (lines 615–621 in V-02; lines 1217–1222 in V-04; lines 1521–1526 in V-05):
```
ENFORCEMENT NOTE:
    Rule: Do NOT conflate CANARY SUPPRESSED with CANARY-FALSE-POSITIVE.
    Distinction: CANARY SUPPRESSED = correct disclosure of incomplete edits (not an error).
                 CANARY-FALSE-POSITIVE = assertion emitted when condition is false (named error).
    Violation: Emitting CANARY ASSERTION when one or more Status fields remain as
               "MOCK (awaiting review)" = CANARY-FALSE-POSITIVE. Treat as named error.
```

**V-01, V-03**: enforcement prose only — "These are distinct. Do NOT conflate them." — names the prohibition but does not name the error that fires if violated. The consequence of conflation is not a checkable contract.

**Differential**: V-02/V-04/V-05 PASS; V-01/V-03 FAIL.

**Pattern**: "Dedicated ENFORCEMENT NOTE block after CANARY TERMINOLOGY TABLE with a named `Violation:` field that identifies the exact error code (CANARY-FALSE-POSITIVE) as the consequence of conflation. Enforcement note becomes a checkable contract, not a trailing prohibition sentence."

This is structurally distinct from C-21 (which requires only that enforcement follows the table). C-23 requires that the enforcement block carries a `Violation:` field naming the specific downstream error.

---

### Ceiling Impact

C-22 and C-23 each add one aspirational slot:

| State | Denominator | Max aspirational | Total ceiling |
|-------|-------------|-----------------|---------------|
| v5 (current) | 13 | 16.25 | **106.25** |
| v6 (with C-22 + C-23) | 15 | 18.75 | **108.75** |

V-05 passes both C-22 and C-23. V-03 passes C-22 only. V-02/V-04 pass C-23 only. V-01 passes neither.

Under a prospective v6 rubric:
- **V-05: 108.75** (new ceiling)
- V-03: 107.5 (C-22 only)
- V-02, V-04: 107.5 (C-23 only)
- V-01: 106.25

**V-05 is the champion** — the only variation achieving both new patterns simultaneously.

---

### Dual Convergence Status

R4 V-05 established: all 21 criteria PASS. R5 reveals: the skill can still differentiate at the excellence layer through two structural upgrades that C-21's PASS threshold did not require. The dual convergence signal is therefore **not yet reached** — R6 should confirm V-05 as the golden prompt by running it as a live skill execution and verifying no new differential patterns emerge.

---

```json
{"top_score": 106.25, "all_essential_pass": true, "new_patterns": ["cross-template completeness assertion — count-anchored Verify after CROSS-TEMPLATE RELATIONSHIP BLOCK naming partial-table condition explicitly (C-22)", "named Violation: field in dedicated ENFORCEMENT NOTE block converting enforcement prohibition into checkable contract with downstream error code (C-23)"]}
```
