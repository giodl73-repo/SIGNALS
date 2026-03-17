Written to `simulations/quest/golden/topic-roadmap-variate-R9-2026-03-17.md`.

---

**Round 9 — Five variations summary:**

| Var | Axis | C-21 | C-22 | C-23 |
|-----|------|------|------|------|
| V-01 | Dual-site INERTIA-GATE | **Target** | -- | -- |
| V-02 | Restart isolation clause | inherit | **Target** | -- |
| V-03 | Standalone verdict vocabulary | inherit | -- | **Target** |
| V-04 | C-21 + C-22 combined | **Target** | **Target** | -- |
| V-05 | Full integration | **Target** | **Target** | **Target** |

**What each variation adds over R8 V-05:**

- **V-01**: `[Site 1 of 2 -- Phase 5 entry]` and `[Site 2 of 2 -- Phase 6 entry]` labels, with Phase 6 explicitly stating "enforced independently at this site, without relying on Phase 5 to carry the constraint."

- **V-02**: Two parallel clauses at Phase 1 barrier — `FIRST-RUN ISOLATION` (existing) and `RESTART ISOLATION` (new) — the restart clause explicitly names re-reading to reconstruct state as a C-22 violation.

- **V-03**: `## Verdict Vocabulary` standalone block between Phase 4 and Phase 5 defining DEFEATED/HOLDS with forward paths. Phase 5 says "Apply the Verdict Vocabulary defined above. Do not redefine here."

- **V-04**: V-01 + V-02. Dual-site labels and restart clause; verdict semantics remain embedded in Phase 5.

- **V-05**: All three. The three mechanisms are spatially separated — restart clause at Phase 1, verdict vocabulary block before Phase 5, dual-site gates at Phase 5/6 boundaries.
