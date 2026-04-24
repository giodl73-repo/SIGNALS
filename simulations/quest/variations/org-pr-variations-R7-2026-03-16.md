**org-pr R7 variations written** to `simulations/quest/golden/org-pr-variate-R7-2026-03-16.md`.

---

## Round 7 Summary

**Investigation questions answered:**

| Question | Answer |
|----------|--------|
| C-12/C-13 at V-03 complexity? | **Yes** — fire in V-01 with no priority table or axis declaration |
| Embedded conflict preserves C-23? | **Yes** — phrase survives in Authority Chain section |
| Embedded conflict preserves C-22? | **No** — C-22 requires a conflict table; embedded instruction fails |
| C-26 backports cheaply? | **Yes** — single opening phrase, +0.59 pts |
| Embedded path cap? | **99.41** — C-22 FAIL is the permanent ceiling |

**Composite scores against v7:**

| V | Axis | Score |
|---|------|-------|
| V-01 | C-12+C-13 at V-03, no C-26 | 98.82 |
| V-02 | V-01 + C-26 + reconciliation | 99.41 |
| V-03 | Embedded conflict + C-26 | 98.82 |
| V-04 | V-03 + escape closure | 99.41 |
| V-05 | R6 V-04 + "three governance axes" | **100.00** |

**Key finding**: V-05 is just R6 V-04 with one sentence added. C-26 was the only gap. The 3-axis table's axes (authority chain / inertia / conflict resolution column) are non-redundant, so C-27 PASS was already implicit — it only needed the explicit count declaration to surface.

**R8 direction**: Test whether C-22 can be satisfied with a per-role inline conflict row (rather than a global standalone section), giving the embedded path a shot at 100.00.
