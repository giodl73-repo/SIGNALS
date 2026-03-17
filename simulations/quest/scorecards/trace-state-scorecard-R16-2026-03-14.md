# Quest Score: trace-state — Round 16

**Evaluation context**: Trace artifact is `placeholder` — scoring prompt design against rubric, not a live output.
**Scoring weights**: Essential 60% (5 × 12 pts) · Recommended 30% (3 × 10 pts) · Aspirational 10% (37 × 0.270 pts)

---

## Baseline Assumption (R1–R15 accumulated)

All five variations inherit the same prompt structure. The R15 baseline satisfies:

| Bucket | Criteria | Status | Pts |
|--------|----------|--------|-----|
| Essential | C-01 to C-05 | PASS — template enforces before/after states, preconditions, INV registry, anomaly sweep, domain labels | 60.00 |
| Recommended | C-06 to C-08 | PASS — `[REJECTED]` step required, numbered step template, Phase 3D covers race conditions | 30.00 |
| Aspirational C-09–C-43 | 35 criteria | PASS — accumulated through R15: sweep table, dual-pass detection, LOCKED/OPEN, Gap Record template, Role B, pre-detection commitment, global standards registry, APPLICATION SENTENCE (C-42), 6-row Phase 3E (C-43) | 9.45 |

**Baseline aspirational**: 35 × 0.270 = 9.45 pts

**New this round**: C-44 and C-45 are NOT in baseline.

---

## Variation-by-Variation Assessment

### V-01 — Blocking APPLICATION SENTENCE Gate

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01–C-08 | PASS | Baseline |
| C-09–C-43 | PASS | Baseline |
| **C-44** | **PASS** | Every exit certification opens with "PHASE N: COMPLETE is BLOCKED until all four gates below are satisfied." Scoring Protocol gate text explicitly names a restate-only SCORING PROTOCOL as the blocking condition, per C-44's exact gate language requirement. APPLICATION SENTENCE appears inline per phase. |
| **C-45** | **FAIL** | No ANTI-MASKING RULE callout block in Phase 3E header. No "Exit gate requires all six sub-scan rows populated" requirement. C-43's 6-row table is preserved but the exit gate and named constraint are absent. |

**Aspirational**: 35 + 1 (C-44) = 36 × 0.270 = **9.72**
**Total**: 60 + 30 + 9.72 = **99.72**

---

### V-02 — Named ANTI-MASKING RULE (C-45)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01–C-08 | PASS | Baseline |
| C-09–C-43 | PASS | Baseline |
| **C-44** | **FAIL** | Single-axis variation — no blocking gate language for APPLICATION SENTENCE. V-02 targets C-45 only; the Scoring Protocol gate may remain a checkbox without blocking framing. |
| **C-45** | **PASS** | Named `ANTI-MASKING RULE` callout block appears in Phase 3E header *before* Role B pre-detection — satisfies C-45's "named constraint before detection begins" requirement. Exit certification titled "Exit gate requires all six sub-scan rows populated" with per-row individual checkboxes satisfies the all-populated mechanical gate. |

**Aspirational**: 35 + 1 (C-45) = 36 × 0.270 = **9.72**
**Total**: 60 + 30 + 9.72 = **99.72**

---

### V-03 — Pre-Game Contracts (PART 0.0C + 0.0D)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01–C-08 | PASS | Baseline |
| C-09–C-43 | PASS | Baseline |
| **C-44** | **PARTIAL** | `0C: Per-Phase Exit Contract` seals the 4-gate model before PART 1 — a strong pre-game commitment. However, C-44 explicitly requires the APPLICATION SENTENCE to be "a named checkpoint *in the phase exit certification*" that "blocks PHASE N: COMPLETE from being declared." If the per-phase exit certifications still show checkboxes without "BLOCKED until" language at invocation time, the pre-game contract satisfies the spirit but not the structural location requirement. 0.5 credit. |
| **C-45** | **PARTIAL** | `0D: Phase 3E Row Independence Contract` commits to anti-masking before PART 1. C-45 requires the rule to appear "in the phase header before detection begins" — a Phase 3E-local constraint. A global pre-game entry in PART 0 may not place the rule where C-45 locates it (in the phase header). 0.5 credit. |

**Aspirational**: 35 + 2 × 0.135 = 35 + 0.27 = 35.27 effective × 0.270... recomputed as: 35 × 0.270 + 2 × 0.135 = 9.45 + 0.27 = **9.72**
**Total**: 60 + 30 + 9.72 = **99.72**

---

### V-04 — Compound (V-01 Blocking + V-02 Anti-Masking)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01–C-08 | PASS | Baseline |
| C-09–C-43 | PASS | Baseline |
| **C-44** | **PASS** | V-01 blocking gate language at each phase exit certification — "BLOCKED until all four gates" with Scoring Protocol gate naming restate-only as blocking condition. |
| **C-45** | **PASS** | V-02 named `ANTI-MASKING RULE` callout in Phase 3E header + exit certification requiring all six sub-scan rows populated with per-row checkboxes. |

**Aspirational**: 37 × 0.270 = **9.99**
**Total**: 60 + 30 + 9.99 = **99.99**

---

### V-05 — Compound + Imperative Modals + PART 5 Reconciliation

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01–C-08 | PASS | Baseline |
| C-09–C-43 | PASS | Baseline |
| **C-44** | **PASS** | V-04 blocking language; MUST/BLOCKED/ADVANCE imperative throughout makes "BLOCKED until" unambiguous across all gate invocations. |
| **C-45** | **PASS** | V-04 anti-masking rule; imperative framing hardens per-row independence requirement. |
| C-31/C-34/C-37 reinforcement | Existing PASS — strengthened | MUST/BLOCKED/ADVANCE language tightens LOCKED/OPEN mechanics and Gap Record unlock signal — no new criteria, but reduces optional-boilerplate risk for criteria already passing. |
| C-25 / C-21 (PART 5) | Existing PASS — reinforced | C/FP/FN calibration score is a PART 5 restoration. If baseline already has this from R5, no score delta. If it was silently degraded, V-05 restores two criteria. |

**Aspirational**: 37 × 0.270 = **9.99** (same rubric ceiling as V-04; qualitative execution advantage outside rubric scope)
**Total**: 60 + 30 + 9.99 = **99.99**

---

## Composite Score Summary

| Rank | Variation | C-44 | C-45 | Aspirational | **Total** |
|------|-----------|------|------|--------------|-----------|
| 1 (tie) | **V-04** | PASS | PASS | 9.99 | **99.99** |
| 1 (tie) | **V-05** | PASS | PASS | 9.99 | **99.99** |
| 3 (tie) | V-01 | PASS | FAIL | 9.72 | 99.72 |
| 3 (tie) | V-02 | FAIL | PASS | 9.72 | 99.72 |
| 3 (tie) | V-03 | PARTIAL | PARTIAL | 9.72 | 99.72 |

**Tiebreak**: V-05 preferred over V-04 — imperative modal language (MUST/BLOCKED/ADVANCE) throughout hardens all gating criteria against optional-boilerplate treatment. V-05 also provides insurance if C-25/C-21 were degraded in the baseline.

**Single-axis tie explanation**: V-01, V-02, and V-03 each contribute the same arithmetic (0.27 pts) — one full pass for one new criterion, or two half-passes. Different mechanism, same score.

---

## Excellence Signals (from V-04/V-05)

**1. Compound-axis dominance**
The single-axis constraint — that each of V-01 and V-02 captures exactly one of the two new R16 criteria — is not a hypothesized gap, it's a structural ceiling. No single-axis variation can score above 99.72. V-04 and V-05 break the ceiling by treating C-44 and C-45 as a jointly necessary pair, not independent options. Pattern: when two criteria form a mechanically interdependent gate model (4-gate exit + 6-row anti-masking), the rubric rewards their co-occurrence.

**2. Blocking language belongs at point of invocation, not only in pre-game**
V-03 tests whether pre-sealing in PART 0 is equivalent to per-phase blocking language. It is not — C-44 explicitly places the gate "in the phase exit certification." The pre-game contract reduces ambiguity about what the four gates are, but does not satisfy the criterion's structural location requirement. Excellence: the blocking declaration must appear where the model will encounter it when it considers declaring PHASE N: COMPLETE.

**3. Imperative modal register as a no-cost criterion reinforcement (V-05)**
MUST/BLOCKED/ADVANCE throughout adds no new rubric criteria but statistically reduces the risk that existing gate criteria are treated as optional prose. This is the correct place to apply style enhancement — after the structure satisfies all criteria, not as a substitute for structural gating.

---

```json
{"top_score": 99.99, "all_essential_pass": true, "new_patterns": ["compound-axis dominance: combining V-01 blocking-gate framing with V-02 ANTI-MASKING RULE callout in one variation achieves both C-44 and C-45 where each single-axis variation captures only one — the two criteria are mechanically interdependent and should be co-targeted", "blocking language belongs at point of invocation: C-44 requires the APPLICATION SENTENCE gate to appear in the phase exit certification itself, not only in a pre-game PART 0 contract; pre-game sealing (V-03) commits to the structure but does not satisfy the per-phase location requirement"]}
```
