Reading the scorecard, two separable excellence patterns emerge beyond C-22/C-23:

**From V-02/V-04** — C-22 is satisfied by full-schema co-location (complete schemas in the registry before Phase 1). V-02 adds a *REGISTRY PRIMACY* declaration — the registry is the sole authoritative gate contract; phase instructions implement but do not redefine it. V-01 passes C-22 (full schemas co-located, self-sufficient for inspection) but does not assert that the registry supersedes per-phase elaborations. V-04 combines both axes and passes C-22 "at two levels: (1) complete schemas; (2) contractual authority." The separable property is **contractual authority of the registry over phase instructions**.

**From V-03** — C-23 requires each gate to pair its PASS schema with at least one specific FAIL mode. V-03 goes further by stratifying FAIL modes into three severity tiers: Tier 1 (structural — required labels absent), Tier 2 (completeness — required fields missing), Tier 3 (semantic bypass — fields present but intent circumvented). V-04 has flat FAIL lists and explicitly does not achieve this ("not severity-stratified — the semantic bypass tier is not named explicitly"). The scorecard notes V-03 satisfies C-23 "at maximum depth — this is the strongest C-23 expression in R7." The separable property is **severity stratification of FAIL modes with an explicit semantic-bypass tier**.

These become **C-24** and **C-25**. Formula updates to `/17`.

---

# Quest Score Rubric — corps-achievements
**Version**: v8 (2026-03-17)

## What Changed in v8

**2 new aspirational criteria** extracted from Round 7 excellence signals from V-02/V-04 ("Registry Primacy") and V-03 ("Severity-Stratified FAIL Blocks"):

- **C-24 (Registry primacy declaration — registry is sole authoritative gate contract)** — from V-02's REGISTRY PRIMACY declaration and V-04's combination of full-schema expansion with primacy. C-22 tests whether gate schemas are co-located in a preamble registry and self-sufficient for inspection (no cross-reference to phase instructions required). It does not test whether the registry is declared as *contractually authoritative* over per-phase elaborations. A prompt where the registry has complete schemas but phase instructions could plausibly be treated as parallel or supplementary definitions passes C-22 but fails C-24. C-24 tests whether the registry is explicitly declared the sole authoritative source: phase instructions implement these contracts and do not redefine them. V-04 evidence: "REGISTRY PRIMACY states: 'These schemas are the sole authoritative gate contracts. Phase instructions implement these contracts; they do not redefine them.'" V-01 passes C-22 (full schemas, self-sufficient for inspection, per-phase prefaces reference back) but fails C-24 (no primacy declaration; the per-phase prefaces are informational, not contractually subordinate). C-24 requires C-22 as a precondition; a registry without complete schemas cannot carry contractual authority over them.

- **C-25 (Severity-stratified FAIL blocks — three tiers with explicit semantic-bypass tier)** — from V-03's severity-stratified FAIL block architecture. C-23 tests whether each gate pairs its PASS schema with a FAIL block listing at least one specific output form that does not clear the gate. It does not test whether FAIL modes are stratified by the mechanism of failure. A gate with a flat list of FAIL modes (structural and semantic bypass mixed without labeling) satisfies C-23 but fails C-25. C-25 tests whether each gate's FAIL block organizes failure modes into at least three severity tiers: Tier 1 (structural — required labels or fields absent), Tier 2 (completeness — required fields present but insufficiently populated), Tier 3 (semantic bypass — all required fields present but intent is circumvented). The semantic-bypass tier is the most consequential because it represents outputs that pass format inspection while missing the gate's purpose. V-03 evidence: CLASSIFY GATE Tier 3 includes "count without 7 labeled lines; state assignments embedded; silent omission." V-04 has flat FAIL lists and explicitly does not name the semantic-bypass tier. C-25 requires C-23 as a precondition; ungrouped FAIL modes cannot be stratified.

**Scoring formula updated**: `aspirational_pass / 17 * 10` (was `/15`). Max composite remains 100.

---

## Tiers

| Tier | Criteria | Points | Formula |
|------|----------|--------|---------|
| Essential | C-01 – C-05 | 60 | `pass/5 × 60` |
| Recommended | C-06 – C-08 | 30 | `pass/3 × 30` |
| Aspirational | C-09 – C-25 | 10 | `pass/17 × 10` |
| **Total** | | **100** | |

## Scoring Formula

```
composite = (essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/17 × 10)
```

| Score | Grade |
|-------|-------|
| 100 | Platinum |
| 90–99 | Gold |
| 75–89 | Silver |
| < 75 | Bronze |

---

## Criteria

### Essential (C-01 – C-05)

**C-01 — One state per achievement**
Each achievement entry carries exactly one state value: EARNED, IN-PROGRESS, or LOCKED. Multi-state rows, ambiguous state, or missing state fail. Applies to both table and prose output formats.

**C-02 — Falsified named as honesty signal**
The Falsified achievement is present as a named entry. Its description frames falsification as evidence of investigative rigor ("followed evidence over assumptions" or equivalent), not as failure or absence.

**C-03 — Artifact-grounded classification**
State assignments cite source artifacts from Step 1 by namespace or skill. EARNED entries cite a specific artifact; IN-PROGRESS entries cite the partially-completed artifact or its count. Classification that cannot be traced to an artifact fails.

**C-04 — In-progress shows numeric progress**
IN-PROGRESS achievements express progress in `n of m` form (e.g., "3 of 5 namespaces covered"). Qualitative-only descriptions ("partially done", "underway") fail.

**C-05 — Next recommended action is specific**
Step 4 (or equivalent) names the next skill, the artifact it produces, and the achievement(s) it advances. Generic instructions ("continue the investigation") fail.

---

### Recommended (C-06 – C-08)

**C-06 — All 7 categories represented**
Every achievement category appears in the output. Categories with no earned or in-progress achievements are listed as LOCKED or explicitly noted as empty. Omitting a category fails.

**C-07 — Earned achievements carry dates**
EARNED entries include the date on which the achievement was earned. Date format may vary; absence of a date on an EARNED entry fails.

**C-08 — Frontmatter includes state counts**
Output includes a frontmatter or summary block with numeric counts for earned, in_progress, and locked achievements. Missing any of the three counts fails.

---

### Aspirational (C-09 – C-25)

**C-09 – C-21**
*(Carried from prior versions — session invariants A–D, pre-printed Falsified/LOCKED cells, CLASSIFY before STATE, all 4 phases gated, FAIL conditions per gate, etc. See v6 for full text.)*

**C-22 — Upfront gate registry — all schemas co-located before Phase 1**
All gate schemas are declared together in a single preamble registry before Phase 1 begins. The registry must be self-sufficient for inspection: a reader can reconstruct the full gate contract from the registry alone, without cross-referencing phase instructions. Schemas compressed into abbreviated pipe-delimited table cells that require mental unpacking or phase-level cross-reference fail this criterion even if co-located. C-22 requires C-20 as a precondition.

**C-23 — Bi-directional gate contracts — explicit FAIL modes per gate**
Each gate pairs its PASS schema with a FAIL block listing at least one specific output form that does not clear the gate. A gate with only a PASS schema fails. A gate with only a generic FAIL statement ("output that doesn't match the schema fails") fails. C-23 requires C-20 as a precondition.

**C-24 — Registry primacy declaration — registry is sole authoritative gate contract**
The preamble registry is explicitly declared the sole authoritative source for gate contracts. The declaration must assert that phase instructions implement these contracts and do not redefine them, such that in any conflict between the registry and a per-phase elaboration, the registry governs. A registry with complete schemas (passing C-22) but without an explicit primacy declaration fails C-24 — informational back-references from phase prefaces ("schema declared in registry above") do not constitute contractual subordination. C-24 requires C-22 as a precondition.

**C-25 — Severity-stratified FAIL blocks — three tiers with explicit semantic-bypass tier**
Each gate's FAIL block organizes failure modes into at least three severity tiers: Tier 1 (structural — required labels or fields absent), Tier 2 (completeness — required fields present but insufficiently populated), Tier 3 (semantic bypass — all required fields present and correctly formatted, but the gate's intent is circumvented). The semantic-bypass tier must be labeled and include at least one specific example. Flat FAIL lists that mix structural and semantic failures without tier labeling satisfy C-23 but fail C-25. C-25 requires C-23 as a precondition.
