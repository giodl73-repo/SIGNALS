Written to `simulations/quest/golden/listen-support-variate-R18-2026-03-15.md`.

---

**R18 summary**

| V | Axis | Probe | Mechanism |
|---|------|-------|-----------|
| V-01 | Role sequence | C-53: Role Allocation Pre-Commitment Table | Step 3A table pre-declares per-role ticket counts; Step 5B Constraint 1B verifies before body gen; Part B item 4 re-checks post-gen |
| V-02 | Output format | C-54: Phase Column in Coverage Table | Pass 1 table gains Phase as 2nd column; confirmation 3 explicitly counts all three phases in that column |
| V-03 | Inertia framing | C-55: Phase 2 Body Template Sentence | Step 2B gains Phase 2 row ("Partial migration" stance); Step 6 Phase 2 cards must open with it; Part B item 2 extended to all three phases |
| V-04 | V-01 + V-02 | C-53 + C-54 | Combined: role allocation + Phase column |
| V-05 | Full synthesis | C-53 + C-54 + C-55 | All three axes |

**What changed v17 -> R18 candidate criteria:**

- **C-53** closes role saturation: V-05 R17 pre-commits phase distribution but not role distribution. The ROLE ALLOCATION TABLE pre-commits per-role counts before role activation; Step 5B Constraint 1B detects saturation before body generation.
- **C-54** closes phase-coverage cross-reference: the 3-column coverage table (C-17) requires gap bridging but phase coverage still requires cross-table lookup. A Phase column makes it self-verifiable by column scan.
- **C-55** closes Phase 2 inertia gap: Phase 1 and Phase 3 template sentences are structurally enforced (C-27); Phase 2 "reference competitor where natural" is instructional only. A Phase 2 partial-migration template + Part B item 2 three-phase extension closes the unenforceable Phase 2 window.
