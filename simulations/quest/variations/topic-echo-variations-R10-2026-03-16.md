Written to `simulations/quest/golden/topic-echo-variate-R10-v2-2026-03-16.md`.

---

## Round 10 Variations — `topic:echo`

**Base:** R9 V-05 (215/215 under v10). All five carry C-01–C-33.

**Gap identification:** Three structural commitments in the v10 prompt are enforced by specification but not auditable from output alone:

| Gap | Commitment enforced | What's missing |
|-----|---------------------|----------------|
| BC provenance | BC reads design materials only (same exclusion as EF) | No record of what BC scanned — unlike EF which has EF-INVOCATION-RECORD from C-33 |
| Phase transitions | Role exclusions enforce "no cross-phase reasoning" | No visible token confirms EF exited after Step 0, or BC after Step 1 |
| Filter selectivity | STILL-LIVE FILTER routes excluded candidates to topic-story | Which candidates were rejected and why is invisible — only accepted candidates appear |

**Three R10 axes:**

- **Axis A — BC Coverage Record:** BC produces `BC-COVERAGE-RECORD` after PBI freeze (parallel to `EF-INVOCATION-RECORD`), listing design materials scanned, signals excluded, and PBI completeness basis
- **Axis B — Phase Handover Tokens:** `PHASE-HANDOVER-EF` at end of Step 0 and `PHASE-HANDOVER-BC` at end of Step 1 confirm completing role, output produced, exclusion taking effect, and receiving role
- **Axis C — Discard Log:** Each STILL-LIVE FILTER NO decision produces a typed `DISCARD-[N]` entry with route + reason; `DISCARD-LOG-COMPLETE` token summarizes candidates considered / accepted / discarded

**Variation plan:**

| Variation | Axis A | Axis B | Axis C | Predicted v10 |
|-----------|:------:|:------:|:------:|:-------------:|
| V-01 | BC-COVERAGE-RECORD | — | — | 215/215 |
| V-02 | — | PHASE-HANDOVER tokens | — | 215/215 |
| V-03 | — | — | DISCARD LOG | 215/215 |
| V-04 | BC-COVERAGE-RECORD | PHASE-HANDOVER tokens | — | 215/215 |
| V-05 | BC-COVERAGE-RECORD | PHASE-HANDOVER tokens | DISCARD LOG | 215/215 |

**R10 progression layer candidate:** auditable record → symmetric provenance. R9 established that structural commitments should produce auditable records. R10 tests whether the same standard applies symmetrically across all roles (not just EF), all phase transitions, and all selection decisions that shape artifact composition.
