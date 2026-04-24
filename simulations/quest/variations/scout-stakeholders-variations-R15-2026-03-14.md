Written to `simulations/quest/rubrics/scout-stakeholders-rubric-v15-variate-R15-2026-03-15.md`.

---

## Round 15 — scout-stakeholders variations summary

All five carry C-37 + C-38 + C-39 (mandatory for 245/245 under v15). Three new structural axes explored:

| Variation | Axis | New Gate Label | Step |
|-----------|------|---------------|------|
| V-01 | Conflict escalation tier | `FAIL_NO_ESCALATION_PATH` | Step 1a-ext |
| V-02 | Trajectory velocity prefill | `FAIL_UNCALIBRATED_VELOCITY` | Step 3a → Phase 3 grid |
| V-03 | Synthesis coverage gate | `FAIL_SYNTHESIS_GAP` | Step 8b |
| V-04 | V-01 + V-02 | Both above | — |
| V-05 | V-01 + V-02 + V-03 | All three | — |

**Structural properties being tested:**

- **V-01** — Escalation tier extends Step 1a with a parallel `Escalation Owner / Trigger / Action` table per conflict. Distinct from C-06: C-06 fires on missing resolution pathway; `FAIL_NO_ESCALATION_PATH` fires on missing escalation tier independent of resolution pathway completeness.

- **V-02** — Step 3a mirrors C-38 (calibrated probability bands) but for trajectory velocity. Three named bands: `ACCELERATING / STABLE / DECELERATING` with explicit observable indicators. Phase 3 grid gains a `Velocity` column that must draw exclusively from the prefill. Distinct from `FAIL_NO_TRAJECTORY`: trajectory direction can be present with the velocity label absent.

- **V-03** — Step 8b (between amendment and synthesis) is a coverage audit table. Every Phase 3 grid row must either appear in synthesis or have a documented omission justification. Distinct from `FAIL_NO_SYNTHESIS` (C-32): synthesis can exist and be fully attributed while silently dropping a grid stakeholder.

All five are predicted 245/245 under v15. New gate labels are candidates for C-40/C-41/C-42 in v16.
