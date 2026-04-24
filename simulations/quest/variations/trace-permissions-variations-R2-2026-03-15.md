Here are the 5 Round 2 variations, each targeting the new rubric v2 criteria:

---

## Round 2 Variation Map

| Variation | Axis | New Criteria Targeted |
|-----------|------|-----------------------|
| **V-01** | Output format — per-entity inline gap tally | C-10 (single-axis) |
| **V-02** | Role sequence — full-verdict per-role escalation spine | C-11 (single-axis) |
| **V-03** | Lifecycle emphasis — named inventory gate with per-entity FLS confirmation | C-12 (single-axis) |
| **V-04** | Combined: inline gap stream + gate-then-proceed checkpoint | C-10 + C-12 |
| **V-05** | Combined: verdict-per-role discipline + Dataverse stock defaults as baseline | C-11 + C-10 (via deviation framing) |

---

**Key mechanisms per new criterion:**

**C-10 (real-time gap accumulation)** — V-01 requires a mandatory ENTITY GAP TALLY block after each entity section before advancing; V-04 has an open Inline Gap Stream with Part B gate audits that enumerate stream IDs. Both make deferred consolidation structurally impossible.

**C-11 (explicit non-escalation documentation)** — V-02 requires a ROLE ESCALATION VERDICT block closing every role section with per-vector verdicts and a named rule-out summary; V-05 mandates a CLOSED CASE statement for every role including read-only roles ("no Write, no Assign, no escalation vector").

**C-12 (phase-gate completeness checkpoint)** — V-03 has two mandatory PHASE GATE tables (inventory → analysis → remediation) that list entities, fields, and scope decisions by name; V-04's gates include Part B gap stream audits that enumerate IDs and confirm no inline signals were collapsed.

The file is at `simulations/quest/golden/trace-permissions-variate-R2-2026-03-15.md`.
