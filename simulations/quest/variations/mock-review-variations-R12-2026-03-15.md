Written to `simulations/quest/golden/mock-review-variate-R12-2026-03-15.md`.

---

## R12 Variations — Summary

**New criteria targeted:**
- **C-34**: TRACEABILITY-BREAK classification test embedded in entry format template (deepens C-33 the way C-32 deepened C-21)
- **C-35**: Strategy-to-PM cross-step contamination guard naming `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and PM Evaluation as the suppressed step

**Denominator: 25 → 27**

| Variation | Axis | C-34 | C-35 | C-26 | Hypothesis |
|-----------|------|------|------|------|------------|
| **V-01** | Output format | PASS | FAIL | PASS | Classification test in entry template alone satisfies C-34; no Strategy guard needed |
| **V-02** | Role sequence (Strat→PM→Arch) | FAIL | PASS | FAIL | Strategy-first guard on `INSUFFICIENT` satisfies C-35; C-26 structurally unreachable |
| **V-03** | Role sequence boundary (Arch→Strat→PM, no non-Arch framing) | FAIL | PARTIAL | PASS | Guard mechanics without non-Architect-first framing — tests whether framing clause is required |
| **V-04** | Combined Strat-first + classification test | PASS | PASS | FAIL | Both new criteria achievable together in Strategy-first design |
| **V-05** | Full integration (Arch→Strat→PM, dual guards) | PASS | PASS | PASS | Dual-guard design satisfies C-26 (Arch-to-PM) and C-35 (Strat-to-PM) simultaneously; C-35 guard explicitly names non-Architect-first context |

**Key architectural decision in V-05:** The C-35 Strategy-to-PM guard coexists with the C-26 Architect-to-PM guard in the `Arch → Strat → PM` ordering. PM is doubly protected — a namespace must clear both guards (architecture quality + coverage adequacy) to reach STEP 5. The C-35 guard text explicitly frames its non-Architect-first applicability ("in a non-Architect-first ordering, this guard is the primary contamination control"), which is what distinguishes C-35 from merely having a second guard in Architect-first designs.
