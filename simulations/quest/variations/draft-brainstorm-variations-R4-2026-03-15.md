Written to `simulations/quest/golden/draft-brainstorm-variate-R4-2026-03-16.md`.

---

## Round 4 Summary

**5 variations generated. Axis selection:**

| Variation | Axis | Base | C-19 | C-20 | Projected |
|-----------|------|------|------|------|-----------|
| V-01 | Phrasing register -- imperative only | R3-V-01 | PASS | FAIL (isolated) | 120 |
| V-02 | Lifecycle emphasis -- consequence only | R3-V-01 | FAIL (isolated) | PASS | 120 |
| V-03 | Output format -- Peer Justification Table schema | R3-V-05 | PASS (structural) | PASS (structural) | 125 |
| V-04 | V-01 + V-02 combined | R3-V-01 | PASS | PASS | 122.5 |
| V-05 | Full stack (all 6 R3+R4 criteria) | R3-V-04 | PASS | PASS | 125 |

**Key design decisions:**

- **V-01 vs V-02** are clean single-axis isolations. V-01 proves that imperative form alone is sufficient for C-19 (the sentence must be written); V-02 proves that a consequence clause is independent of form (interrogative + consequence = C-20 PASS). Both land at 120.

- **V-03** tests a structural hypothesis: encoding C-19/C-20 into the output schema (a required table with fill-or-swap column rules) rather than into prose instructions. Schema-level enforcement should be more durable than instruction-level enforcement under prompt compression.

- **V-04 falls short of 125** (reaches 122.5) because it inherits R3-V-01's architecture, which passes C-18 via Phase 2 checks but doesn't have the full self-review structure of R3-V-04. C-15/C-16/C-17/C-18 all pass but the score ceiling is the missing C-15 from V-01... wait, actually V-04 inherits C-15 from R3-V-01 (which passes C-15 via mandatory `##` sections). The 122.5 comes from: 110 (C-01..C-14) + 2.5 (C-15) + 2.5 (C-16) + 2.5 (C-17) + 2.5 (C-18) + 2.5 (C-19) + 2.5 (C-20) = 122.5. Missing C-15? No -- R3-V-01 has it. Let me recheck... yes, 6x2.5 = 15, 110+15 = 125. V-04 should project at 125 too.

Corrected: V-04 also projects at **125** -- the rubric coverage table in the file shows all six R3+R4 criteria passing for V-04. The distinction vs V-05 is architectural only (two-phase vs multi-phase self-review structure), which doesn't affect scoring under rubric v4.
