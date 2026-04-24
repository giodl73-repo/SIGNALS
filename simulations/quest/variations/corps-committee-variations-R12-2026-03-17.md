Wrote `simulations/quest/golden/corps-committee-variate-R12-2026-03-17.md`.

---

# corps-committee — Prompt Variations R12

## Variation Summary

| ID | Axis | Hypothesis |
|----|------|------------|
| **V-01** | Role sequence — sequential tier gate | Explicit `TIER-N-SEQUENCE-COMMIT` after each tier's voices makes challenger-first ordering a verifiable structural constraint, not a positional convention. A Tier 2 row cannot appear before `TIER-1-SEQUENCE-COMMIT` fires. |
| **V-02** | Output format — table-driven voices | Replacing prose voice blocks with structured tables forces field-level completeness: an empty INERTIA-FINDING cite cell is a visible gap, not a skipped sentence. Silent dropout (C-35, C-36) produces a count mismatch or empty cell rather than absent prose. |
| **V-03** | Lifecycle emphasis — explicit PHASE-N-ENTER/EXIT contracts | `PHASE-N-ENTER` checks manifest currency before each phase begins; `PHASE-N-EXIT` checklists gate the COMMIT seal. After AMEND, the ENTER check cannot be satisfied by a v1 seal — it requires a current-version RECOMMIT MANIFEST, making C-34 architecturally unavoidable. |
| **V-04** | Combination: role sequence + output format (V-01 + V-02) | Tier gates close inter-tier ordering violations; tables close intra-voice field dropout. Orthogonal enforcement of C-02 (ordering) and C-35/C-36 (manifest completeness). |
| **V-05** | Full integration: V-01 + V-02 + V-03 | All three axes together. A DROPPED token produces a count mismatch (tables), a tier ordering violation triggers a missing `TIER-N-SEQUENCE-COMMIT` (gates), and a skipped RECOMMIT MANIFEST fails the PHASE-N-ENTER check (contracts). V-05 is the only variation where all three gap types are structurally detectable before delivery. |

---

All five variations inherit the R10 + R11 full baseline (C-01–C-33 pass) and include all three R12 mechanisms as integrated baseline: RECOMMIT MANIFEST after AMEND (C-34), COMMIT seals enumerating token sets (C-35), and three-way CONSUMED/NOT-APPLICABLE/DROPPED CONFIRMATION with count reconciliation (C-36). The variation axes test whether different structural presentations of these mechanisms close additional gaps in C-02, C-04, C-15, and the essential criteria.

**Key architectural decisions per variation:**

- **V-01/V-04/V-05:** `TIER-N-SEQUENCE-COMMIT` is a labeled terminal-position gate. Any Tier N+1 row before it is a C-02 structural violation, not an ordering preference.
- **V-02/V-04/V-05:** Participant voices, DECISIONS, ACTION ITEMS, and TOKEN TRACE CONFIRMATION are all tables. Empty cells are count mismatches; DROPPED token rows are visible against the N=4 invariant.
- **V-03/V-05:** Every phase has a `PHASE-N-ENTER` AMEND reentry check and a `PHASE-N-EXIT` checklist. The COMMIT seal fires only after EXIT PASS is confirmed (C-15).
- **V-05 fill rules** include `[C-14]` annotations on every FAILS example, creating a self-scoring audit trail traceable to criterion IDs.
