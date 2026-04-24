Written to `simulations/quest/golden/topic-retro-variate-R12-2026-03-17.md`.

---

## R12 — Five Variations Summary

**Base:** R11-V-05 (all C-22 through C-29 integrations carried forward).
**New criteria targeted:** C-30 and C-31.

---

### Variation Axes and Hypotheses

| ID | Axis | C-30 mechanism | C-31 mechanism | Hypothesis |
|----|------|----------------|----------------|------------|
| **V-01** | C-30 single | Phase 8 SEAL: three independent fields — `This score` / `COPY-VERIFIED` / `COPY-SOURCE` | R11-V-05 trailing bullet list (unchanged) | R11-V-05 fuses verification state + source into one checklist item; splitting into three independently addressable fields satisfies "named fields" requirement |
| **V-02** | C-31 single | R11-V-05 SEAL (COPY-VERIFIED inline, unchanged) | `## DESIGN GUARANTEES` two-column table (Mechanism / Guarantee) with section header | Bullet list appended to phase content reads as a note; header-titled table creates the structural separation that makes the section independently locatable |
| **V-03** | Phrasing register | SCORE TRANSFER COMMAND block: 4 numbered imperative steps; step 3 names COPY-VERIFIED and "Phase 6 verdict" explicitly | `**EXECUTION CONTRACT**` bold header with headline-imperative lines per mechanism | Tests whether behavioral compliance framing achieves both criteria without structural token complexity; risk: rubric may require named *fields*, not prose prohibitions |
| **V-04** | C-30 + C-31 combined | Three-field SEAL (V-01) | `## DESIGN GUARANTEES` table (V-02) | Zero-interference test — V-01 modifies Phase 8 SEAL only, V-02 modifies post-execution section only; independent modifications, no phase-level conflict |
| **V-05** | Full integration | Three-field SEAL (V-01) + Phase 8 cell template carries `COPY-VERIFIED [source: Phase 6 verdict]` inline | `## PRE-EXECUTION CONTRACT` table before Phase 1 + condensed trailing audit reference | Maximum structural redundancy: C-30 in three locations (body instruction, cell format string, three SEAL fields); C-31 as a prospective contract positioned before Phase 1 output |

---

### Design Decisions Per Variation

**V-01 gap analysis:** R11-V-05's single SEAL item `[ ] This score: {number}/100 — COPY-VERIFIED: confirm...` contains both the verification label and the source name, but as inline commentary on one item. C-30 requires the SEAL to encode them as *named fields*. Three separate items make each independently confirmable.

**V-02 gap analysis:** A two-column `## DESIGN GUARANTEES` table with a section header creates the structural separation C-31 requires. Each row names a mechanism and its specific enforcement element — a reviewer can confirm the copy guard, the slot template, or the AMEND mechanism by reading one row, not by tracing through 9 phase specifications.

**V-03 risk:** C-30 says "SEAL encode both the verified state and the origin as named fields." Imperative prose (`step 3: label COPY-VERIFIED [source: Phase 6 verdict]`) may satisfy the content requirement while failing the "named fields" structural requirement — likely PARTIAL. Useful for comparison.

**V-05 key innovation:** Moving the guarantees table to pre-Phase-1 position makes it a *prospective* contract. C-31 says a reviewer should be able to "audit the key guarantees without reconstructing them from phase text" — positioning them before the phases means an auditor reads the contract before seeing any phase output. This is a structural argument for PASS rather than PARTIAL.
