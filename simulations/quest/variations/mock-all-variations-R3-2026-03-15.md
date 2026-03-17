Written to `simulations/quest/golden/mock-all-variate-R3-2026-03-15.md`.

---

## mock-all Variate — Round 3

### What R2 Left Open

| Criterion | Gap |
|-----------|-----|
| **C-14** — Explicit stop-gate phrase at each phase boundary | R2 named phases but no variation contained "Do not begin X until Y is complete." Phase names imply ordering; they don't qualify as gate instructions. |
| **C-15** — Artifact body content matches namespace's assigned category | "Write a plausible body" is not vocabulary-constrained. A HIGH-STRUCTURE body written in interview register passes C-07 while failing C-15. |

### Axis-Assignment Plan

| V | Axis | Targets | Predicted |
|---|------|---------|-----------|
| V-01 | lifecycle-emphasis | C-14, C-11 (side effect) | Stop-gate at each boundary; CLASSIFY gate fires before first artifact body |
| V-02 | output-format | C-11, C-12 | Pre-printed table skeleton + pre-printed HANDOFF block |
| V-03 | phrasing-register | C-15, C-13 | Per-category MUST/DO NOT vocabulary rules; rationale embedded at rule invocation |
| V-04 | lifecycle + output-format | C-14, C-11, C-12 | C-11 doubly guaranteed: structural and procedural |
| V-05 | all three | C-14, C-11, C-12, C-13, C-15 | Ceiling; risk is C-07 depth degrading under skeleton length pressure |

### Key design decisions

- **V-01 vs V-02 on C-11:** V-01 enforces pre-classification via a gate instruction (model must obey); V-02 enforces it structurally (table is already on the page). V-02 is the stronger guarantee — the pattern established by scout-feasibility R3.
- **V-03's C-13 placement:** Rationale embedded in the REAL-REQUIRED rule at invocation point, not as a post-hoc annotation on the coverage table. Harder to omit when it fires at the decision rather than after it.
- **V-05 trade-off signal:** If C-07 (artifact body depth) degrades in V-05 relative to V-01, skeleton length competes with generation quality — clean finding for Round 4.
