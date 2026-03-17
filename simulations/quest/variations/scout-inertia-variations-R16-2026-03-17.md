Written to `simulations/quest/golden/scout-inertia-variate-R16-2026-03-17.md`.

---

## R16 Summary

**5 variations, all predicted 235/235 + C-53 pass.**

### Variation axes

| V | Axis | Key change from R15 |
|---|------|---------------------|
| V-01 | C-53 only (section-based, Section 1A/1B) | `## Q3` → `## SECTION 1A -- Q3`; `## Q4` → `## SECTION 1B -- Q4`; gate body: `Return to Section 1A if Q3 shows N; return to Section 1B if Q4 shows N.` |
| V-02 | C-53 only (stage-based reference form) | `### Q3` → `### STAGE 2A -- Q3`; `### Q4` → `### STAGE 2B -- Q4`; gate body: `Return to Stage 2A if Q3 shows N; return to Stage 2B if Q4 shows N.` |
| V-03 | C-53 on phrasing-register scaffold | Section 1A/1B naming; per-artifact routing; domain-prefix A-23 style unchanged |
| V-04 | C-53 on consolidated-bridge scaffold | Stage 2A/2B naming; per-artifact routing; combined gate heading (A-36) unchanged |
| V-05 | C-53 on all-axes-combined scaffold | No renaming; artifact-name targets: `Q3 SECTION (FM->ACTOR BRIDGE)` / `Q4 SECTION (FM->TRIGGER BRIDGE)` in all-caps |

### Key design decisions

**C-53 target form**: Two separate conditional clauses in the gate body, each keyed to a specific artifact ID (Q3 / Q4), each pointing to a distinct non-overlapping return target. The disjunctive R15 form (`If either shows N: return to Section 1`) passes C-51 but fails C-53 — one conditional, shared target, artifact failure is not independently addressable.

**Section/stage renaming rationale**: To create per-artifact routing targets with unambiguous names, Q3/Q4 sections are labeled with sub-section identifiers (Section 1A/1B or Stage 2A/2B) in V-01 through V-04. V-05 uses Q3/Q4 artifact names directly as section identifiers — no renaming needed since they are already unambiguous standalone sections.

**A-37 consistency preserved**: Section 1A/1B extends the SECTION schema; Stage 2A/2B extends the STAGE schema. Neither introduces a nomenclature conflict.

**V-04 C-51 resolved**: R15 V-04's gate body had no explicit return path (C-51 borderline). R16 adds the per-artifact routing, resolving C-51 and satisfying C-53 simultaneously.

### Open questions for scoring

- Does Section 1A/1B sub-section granularity satisfy A-37 schema-consistency?
- Does Stage 2A/2B sub-stage naming satisfy A-37 within Stage 2's consolidated structure?
- Does V-05's artifact-name-based routing (`Q3 SECTION` / `Q4 SECTION`) satisfy C-53's distinct-target requirement without ordinal labels?
