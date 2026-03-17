`simulations/quest/golden/trace-component-variate-R2-2026-03-15.md` written.

---

# trace-component R2 Variations — Summary

**5 variations generated. Rubric ceiling: 110 pts (v2 with C-10 + C-11).**

---

## Variation Map

| Var | Axis | C-10 target | C-11 target | Key mechanism |
|-----|------|-------------|-------------|---------------|
| V-01 | Role sequence (Citation Auditor) | ~ | + | Second role required to name upstream identifiers for every downstream claim; derivation chain check at end |
| V-02 | Output format (targeted tables + row citation) | + | + | Tables only for C-01/C-04; prose sections must cite EC-n/RR-n row IDs |
| V-03 | Lifecycle (phase registry + consume protocol) | ~ | + | Each phase emits a named registry; downstream phases open with "Consuming from Phase N" citing upstream identifiers |
| V-04 | Combined: format + lifecycle | + | + | Tables for C-01/C-04 (C-10) + registry/consume pattern (C-11) via orthogonal mechanisms |
| V-05 | Combined: role seq + phrasing register | ~ | + | Conversational expert + explicit "Citation Rule" constraint that must be followed inline throughout |

---

## Key Design Decisions vs R1

**What changed from R1:**

R1 V-02 (tables) and V-03 (phase gates) both reached Golden but neither explicitly targeted C-10/C-11 by name — they satisfied those properties incidentally. R2 variations are designed with C-10/C-11 as first-class targets:

- **V-01** tests the minimum viable C-11 intervention: a second role that audits citations without changing the first role's output format. The "derivation chain check" at the end of Role 2 makes the event→state→re-render→UI chain explicit by identifier.

- **V-02** is the most surgical C-10 intervention: tables *only* for C-01 and C-04 (the two sections the rubric names), with row-citation protocol (`EC-n`, `RR-n` references) in downstream prose. This isolates whether C-10 alone is sufficient for C-11, or whether prose-with-citations is weaker than structural phase gates.

- **V-03** tests C-11 without any tables. The registry/consume pattern is a structural enforcement device in prose: each phase's "Consuming from Phase N" block must name specific upstream identifiers as a *precondition* to writing the body, not as a post-hoc audit. This is the most direct port of what made R1 V-03 Golden.

- **V-04** is the combination expected to score highest — tables satisfy C-10 structurally; registry/consume satisfies C-11 structurally; neither depends on the other.

- **V-05** tests whether conversational register can carry C-11 via the Citation Rule constraint. R1 V-04 (conversational) stayed Acceptable partly because prose format hid gaps. V-05 adds the Citation Rule inline to test whether the constraint changes that outcome.
