Written to `simulations/quest/golden/program-plan-variate-R6-2026-03-16.md`.

---

## R6 Variate Summary

**Three single-axis variations, two combined:**

| Variation | Primary axis | C-22 | C-23 | C-24 | Key design move |
|-----------|-------------|------|------|------|----------------|
| V-01 | Inertia framing (C-22) | PASS | FAIL | FAIL | Recommended criteria (C-05/C-06/C-07) in ALL THREE artifact types: BAD block, correction table, AND inline template annotations |
| V-02 | Lifecycle emphasis (C-23) | side-effect PASS | PASS | FAIL | Same `# requires: <artifact> from Zone: <name> (C-05)` format at BOTH zone header AND skills line for all four dependent zones |
| V-03 | Output format (C-24) | side-effect PASS | FAIL | PASS | `gate_fail:` / `gate_pass:` / `gate:` as YAML sibling keys — contrast survives comment stripping |
| V-04 | C-22 + C-23 | PASS | PASS | FAIL | Full recommended annotation in both artifact types + symmetric dual-position deps |
| V-05 | Golden (C-22+C-23+C-24) | PASS | PASS | PASS | All three axes + R5 V-05 foundation |

**Key new move in C-24**: `gate_fail:` and `gate_pass:` are actual YAML keys the model encounters as structure, not comments it can scan past. The model writes `gate:` using `gate_pass:` as the model, then deletes the contrast fields from the final output — but the generation encounter is structural.
