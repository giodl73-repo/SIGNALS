Saved to `simulations/quest/golden/flow-lifecycle-variate-R5-v5-2026-03-15.md`.

---

## Round 5 — Five Variations

**Targets**: C-20 (Per-Step Sequential Gate Coverage), C-21 (Exception Flow Handling Role), C-22 (Production Gate Failure Declaration)

---

### V-01 — Output Format: Gate Saturation at Three Boundaries
**Axis**: Output format | **Target**: C-20 only

Three "do not proceed" gates at distinct schema boundaries, each naming what it locks and what it unlocks:
- **Gate 1**: Role Registry → Phase Table
- **Gate 2**: Phase Table → State Table
- **Gate 3**: Scan Summary → Artifact

Exception catalog has no Handler column (C-21 absent). Production gate states CLOSED condition without failure declaration (C-22 absent). Tests whether gate distribution across three named boundaries satisfies C-20 at minimum threshold.

---

### V-02 — Role Sequence: Exception Ownership Column
**Axis**: Role sequence + output format | **Target**: C-21 only

Exception catalog adds `Handler (R-ID)` column with inline mandatory rule in the column header: *"Blank Handler is a fail -- it means the exception has no accountable owner."* Role Registry includes an Exception Handler Y/N column.

Only one gate (at artifact production) — C-20 absent (satisfies C-13, not C-20). No failure declaration in gate — C-22 absent. Tests whether a mandatory column with inline enforcement produces consistent exception ownership when gate saturation is absent.

---

### V-03 — Phrasing Register: Gate Failure Declaration
**Axis**: Phrasing register | **Target**: C-22 only

Step-numbered imperative format (R4 V-03 register). Production gate reads:

> *Do not write the artifact until Scan Summary shows status CLOSED. Writing the artifact when Scan Summary is OPEN is a structural fail — the output is an incomplete lifecycle trace where at least one path has no named terminal, and it must be discarded.*

One gate only (C-20 absent). Exception flows use prose "Owner: [R-ID]" but no column enforcement (C-21 marginal). Tests whether failure declaration in the gate text changes output quality from condition-only gates.

---

### V-04 — Combined: Gate Saturation + Exception Ownership (C-20 + C-21)
**Axes combined**: Output format + Role sequence | **Targets**: C-20 + C-21

Four gates at four boundaries: (1) Role Registry → Phase Table, (2) Phase Table → State Table, (3) Exception Catalog → Terminals (enforces Handler completion), (4) Scan Summary → Artifact.

Gate 3 is the novel element: *"Do not proceed to Terminal Declaration until every exception row has a Handler (R-ID) populated."* The gate creates structural interdependence between exception ownership and forward progress. Production gate exists but no failure declaration (C-22 absent) — isolates the gate-saturation + exception-ownership combination.

---

### V-05 — Full Lock: C-20 + C-21 + C-22 + C-18/C-19 Carry-Through
**Axes combined**: All three new + R4 carry-through | **Targets**: C-20, C-21, C-22, C-18, C-19

The explicit reference implementation. Every criterion is a named structural decision:

| Criterion | Structural Decision |
|-----------|---------------------|
| C-20 | 4 named gates at 4 boundaries; each names section locked + unlocked |
| C-21 | Handler (R-ID) mandatory column + Gate 3 enforces completion before terminals |
| C-22 | Gate 4 text: *"is a structural fail — incomplete trace, must be discarded"* |
| C-18 | ≥5 inline negation rules embedded in column headers (Role Name, Entry Trigger, Exit Trigger, Decision Condition, Fallback, Handler, Trigger Condition, SLA Impact) |
| C-19 | Two scan tables (per-state + per-exception) with CLOSED status condition |

V-05 answers: what does a prompt look like when C-18 through C-22 are all deliberately designed in, not emergent from format?
