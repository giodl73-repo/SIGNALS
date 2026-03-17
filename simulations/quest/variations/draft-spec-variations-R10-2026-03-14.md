Written to `simulations/quest/rubrics/draft-spec-rubric-v10-variate-R10-2026-03-15.md`.

---

## Quest Variate — `draft-spec` — Round 10 (Rubric v10)

### Axis Map

| Variation | Primary Axis | Hypothesis |
|-----------|-------------|------------|
| **V-01** | C-30 — gate token column-content check (minimal base) | C-30 passes via two-condition invalidity rule in [INERTIA-ANALYZED]: Condition 1 (table presence) + Condition 2 (column-level R-ID population). C-31/C-32 absent to isolate. |
| **V-02** | C-32 — AMPLIFIED dual sub-slot structural format (on V-01 base) | C-32 passes when AMPLIFIED rows carry pre-printed "Risk:" and "R-ID:" as structurally independent labeled fields in the table template. C-31 absent. |
| **V-03** | C-31 — waiver propagation structural rule (on V-01 base) | C-31 passes via named structural rule in Phase 1 + chain closure in [INERTIA-ANALYZED]: PM-COVERAGE-TABLE waiver → "R-ID WAIVED" cell marker → Condition 2 exemption. C-32 absent. |
| **V-04** | C-30+C-31+C-32 on R9 V-04 base (split registers, C-22/C-23/C-26/C-27) | All three compose with split [IG-REGISTER]/[ID-REGISTER] architecture without breaking any R9 V-04 axes. |
| **V-05** | Full combination — all 32 v10 criteria; target 175/175 | All three new criteria integrate into R9 V-05 base: C-30 adds Condition 2 to [INERTIA-ANALYZED]; C-31 closes the waiver chain; C-32 adds pre-printed dual sub-slots to AMPLIFIED rows. |

### Key structural additions in R10

**C-30**: [INERTIA-ANALYZED] now names two conditions explicitly — Condition 1 (table presence, the C-21-level check) and Condition 2 (column-level R-ID population). Meeting Condition 1 without Condition 2 is declared invalid.

**C-31**: Phase 1 gains a named structural waiver-propagation rule. The chain is closed in [INERTIA-ANALYZED]: `[PM-COVERAGE-TABLE] "C-03 WAIVER" → [IG-REGISTER] "R-ID WAIVED" marker → Condition 2 exemption`. A behavioral note without the structural declaration fails C-31.

**C-32**: AMPLIFIED rows in [IG-REGISTER] carry pre-printed sub-slots — `Risk: [...]` and `R-ID: [...]` — as independently labeled structural fields in the table template. A prose instruction or combined-prose statement without pre-printed labels fails C-32 even if both elements are present.
