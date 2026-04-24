---

# quest-golden Variate -- Round 4

**Rubric:** v3 (C-01--C-14, E=5, R=3, A=6)
**Saved:** `simulations/quest/golden/quest-golden-variate-R4-2026-03-16.md`

---

## Pre-Generation: R3 Baseline Analysis (v3 Applied Retroactively)

The best R3 variation (V-04, combination output-format x phrasing-register) scores **96.67** on v3 with two gaps:

| Criterion | R3 V-04 on v3 | Gap |
|-----------|---------------|-----|
| C-13 | PARTIAL | GATE 1 says "essential FAIL" -- misses the PARTIAL case |
| C-14 | FAIL | Gate instructions in preamble only; no field inside scorecard instances |

R3 V-03 (SQS framing) fixes C-14 but fails C-11 and C-13. No R3 variation passes C-11 + C-12 + C-13 + C-14 simultaneously.

---

## Round 4 Variation Map

| V | Axis | Type | What Changes | Target |
|---|------|------|--------------|--------|
| V-01 | phrasing-register | single | GATE 1 adds "PARTIAL or FAIL"; GATE 2 adds "only when GATE 1 already SATISFIED" | C-13 |
| V-02 | output-format | single | Scorecard block gets required `Gate-independence record:` section (2 binary fields) | C-14 |
| V-03 | inertia-framing | single | SQS expanded to 3 named failure modes (C-12/C-13/C-14); per-scorecard SQS citation required | C-13, C-14 |
| V-04 | phrasing-register x output-format | combination P1 | V-01 + V-02 | C-13, C-14 |
| V-05 | lifecycle-emphasis x phrasing-register | combination P2 | STEP 2 split into 2A/2B-GATE1/2C-GATE2; gate-specific prohibitions + independence declarations inside sub-steps | C-13, C-14 |

---

## Scoring Summary

| V | C-13 | C-14 | Composite | Verdict |
|---|------|------|-----------|---------|
| V-01 | **PASS** | FAIL | 98.33 | GOLDEN |
| V-02 | PARTIAL | **PASS** | 98.33 | GOLDEN |
| V-03 | PARTIAL | PASS | 98.33 | GOLDEN |
| V-04 | **PASS** | **PASS** | **100** | **GOLDEN** |
| V-05 | **PASS** | **PASS** | **100** | **GOLDEN** |

All 5 variations GOLDEN. **Trial converged: Y (5/5).**

---

## Excellence Signals

**Signal 1 — C-13: PARTIAL → PASS** (V-01, phrasing-register)
Mechanism: adding "PARTIAL or FAIL" to GATE 1's prohibition sentence closes the PARTIAL case the baseline left open. Single-word change, binary effect.

**Signal 2 — C-14: FAIL → PASS** (V-02, output-format)
Mechanism: moving the gate-independence requirement from preamble instruction to a required labeled field inside each scorecard block converts a promise into per-instance evidence.

**Signal 3 — C-13 mechanism variant** (V-05, lifecycle combination)
V-05 achieves C-13 PASS via gate-scoped structural containment -- each gate's prohibition is embedded inside its own sub-step, making misapplication structurally impossible. V-04 achieves the same score via prohibition language in a shared block. These are distinct enforcement mechanisms with the same outcome at 100.

---

## QU2 / QU3 / QU4

**QU2:** When each gate's prohibition sentence is embedded inside a structurally isolated sub-step -- with the prior gate's sub-step explicitly closed before the next opens -- C-13 compliance is structurally enforced because lifecycle position prevents the prohibition from being applied to the wrong gate, regardless of how the operator reads the shared scoring block.

**QU3 — Proposed C-15:**

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-15 | **Gate-scoped structural containment** -- each scoring gate occupies a dedicated sub-step with explicit entry and exit boundaries | behavior | aspirational | Scoring section contains at least two named sub-steps for threshold evaluation; each begins with an entry boundary referencing the prior sub-step's completion; each ends with an explicit completion declaration. Gate labels inside a single shared step without entry/exit boundaries fail this criterion. |

**QU4 — Defer.** V-04 (no lifecycle split) also scores 100 on C-13. C-15 should be codified only if R5 testing shows gate-scoped containment produces measurably higher C-13 compliance under context pressure than prohibition-sentence-only approaches. Apply after R5 evidence.

---

## Dual Convergence Check

**Trial converged: Y** (5/5 GOLDEN)
**Quest plateau: N** — R4 produced 3 excellence signals (C-13, C-14, Signal 3). Plateau requires 0 signals for 2 consecutive rounds.

**Convergence verdict: Not dual convergence.** Trial dimension done; quest dimension needs at least 2 more consecutive zero-signal rounds.

**Best golden candidate entering R5:** V-04 (phrasing-register x output-format, composite 100) — achieves all 14 criteria through the simplest structure. V-05 scores identically but with greater complexity; the C-15 case for preferring it is deferred to R5.

**R5 target:** 0 new excellence signals. If C-15 is tested and fails to differentiate from V-04, R5 plateaus. R6 would then be the final confirmation round. If C-15 shows measurable benefit and is added as a criterion, the denominator shifts to /7 and the loop continues.
