Written to `simulations/quest/golden/mock-accept-variate-R9-2026-03-17.md`.

---

## Round 9 — Axis-Assignment Summary

**Baseline:** R8 V-01 (sole golden, 25/25 against v9 — `Namespace | Phase | Cost-of-MOCK` 3-column table)

R9 probes three structural questions that C-33 opens but doesn't mandate:

| Variation | Axis | Single change from R8 V-01 | Predicted |
|-----------|------|----------------------------|-----------|
| **V-01** | output-format | Phase moves to column 1: `Phase \| Namespace \| Cost-of-MOCK`; groups Architect rows above Strategy rows for phase-grouping scanability | 25/25 |
| **V-02** | lifecycle-emphasis | GATE E-COST gains per-phase count assertions: Architect rows must equal GATE C INERTIA LEDGER; Strategy rows must equal GATE D INERTIA LEDGER | 25/25 |
| **V-03** | inertia-framing | DEFAULT DECISION POSITION replaced with DECISION SCOREBOARD (`REAL-REQUIRED: 9 / MOCK-ACCEPTED: 0`); numeric counters updated at GATE C and GATE D | 25/25 |
| **V-04** | combined V-01+V-02 | Phase-first columns + GATE E-COST phase-split verification; Architect-first row ordering makes the per-phase count directly countable before the gate fires | 25/25 |
| **V-05** | combined V-01+V-02+V-03 | Full integration: Phase-first table + numeric scoreboard + GATE E-COST phase-split; complete audit chain from inertia declaration → per-gate movement → register aggregation → register verification | 25/25 |

**Key questions R9 answers:**

1. **Does C-33 require specific column ordering?** V-01 vs R8 V-01 (both pass; ordering is preference, not criterion)
2. **Should GATE E-COST verify the per-phase split?** V-02 converts C-33's structural possibility into a mandatory check — tests whether this is a distinct quality improvement or just stricter enforcement of what C-33 already implies
3. **Does numeric inertia framing change evaluation frame?** V-03 tests whether a scoreboard-format DEFAULT DECISION POSITION produces observably different behavior than prose-form C-30
