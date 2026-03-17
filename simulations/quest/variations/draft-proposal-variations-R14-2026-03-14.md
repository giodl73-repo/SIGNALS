Written to `simulations/quest/rubrics/draft-proposal-rubric-v14-variate-R14-2026-03-15.md`.

---

## Round 14 Variate — Summary

**What's in the document:**

5 complete, runnable skill body prompt variations for `draft-proposal` against v14 rubric (/31 denominator, C-38 = inline exemplar in T-37 CONDITION field).

---

### Variation axes and hypotheses

| Var | Axis | Hypothesis | Designed fails | Score |
|-----|------|-----------|----------------|-------|
| V-01 | Role sequence (Architect-first) | C-38 can fail independently when C-37 PASSES — T-37 abstract condition fires T-38 even though T-37 itself never fires | C-38 | 99.68 |
| V-02 | Output format (compact PM-first) | C-38 PASS when T-37 fires — inline exemplar in T-37 CONDITION satisfies C-38 even though C-37 fails | C-37 | 99.68 |
| V-03 | Lifecycle emphasis (stale 37-row table) | C-38 fails independently from a v13-era table: T-37 exists with abstract condition; T-38 absent; C-38 fails behaviorally with no T-38 finding | C-24 + C-38 | 99.35 |
| V-04 | Phrasing register + role combination | C-38 achievable in conversational register; fails orthogonal to new criterion | C-25 + C-33 | 99.35 |
| V-05 | Inertia framing + combination | All three depth/exemplar criteria fail simultaneously against structurally compliant Phase 9b | C-36 + C-37 + C-38 | 99.03 |

---

### Key discriminators established by R14

1. **C-38 is initialization-testable**: A reviewer reads the T-37 CONDITION cell in the static amendment table spec — no Phase 9b execution required. V-01 (C-37 PASS, T-38 fires) and V-03 (stale table, no T-38 row, C-38 still evaluable) both confirm this.

2. **C-38 does not cascade from C-37**: V-02 demonstrates C-37 FAIL + C-38 PASS (T-37 fires but exemplar is present). V-05 demonstrates C-37 FAIL + C-38 FAIL independently. The two criteria are orthogonal.

3. **Stale-table path for C-38**: A v13-era 37-row table can still pass C-38 if T-37 CONDITION carries the exemplar (C-24 FAIL, C-38 PASS). V-03 takes the opposite path: abstract T-37 condition → C-24 FAIL + C-38 independent fail.

4. **V-02 is the C-38 PASS reference**: T-37 CONDITION carries `"row-level confirmation 'R-NN IDs applied to risk row' fires T-37"` — the exact exemplar from the R13 excellence signal, embedded in the trigger spec where C-38 requires it.
