Written to `simulations/quest/golden/org-build-golden-2026-03-16.md`.

**Summary:**
- **Score:** 76 (Essential 4/5, Recommended 2/3, Aspirational 25/31)
- **Simplification:** PASS — 80% reduction, simplified body used
- **Rubric:** v15 (33 criteria, added C-40 and C-41 from V-01 excellence signals)

**Five patterns that made V-01 golden:**
1. Triple-layer boundaries — Constraints + record block PHASE-ORDERING-GUARD + standalone Boundary Guard section (C-40)
2. Declarative error-framing in task prose paired with FORBIDDEN in Constraints (C-41)
3. Record blocks unifying gate declaration, ordering anchor, and materialization in one construct (C-26/C-28)
4. Bidirectional verdict guard — "both" AND "neither" are explicit error modes (C-15)
5. GLOBAL CONSTANTS declared pre-phase, consumed by reference only (C-36/C-17)

**Highest-value fix for Round 21:** C-05 — enforce Decides/Escalates columns in Phase 3 constraints, not just preamble. Recovers 12 points toward a potential score of 88.
Derive T2-VERDICT: NONE or LOW -> `CAN-OPERATE-FLAT`; MODERATE-CRITICAL -> `STRUCTURE-WARRANTED`. One only -- both or neither is an error.

FORBIDDEN: beginning Phase 2 before Phase 1 is complete.

---

## Phase 2 -- Role Enumeration

FORBIDDEN: beginning Phase 2 before Phase 1 is complete.

- T1-DEPTH-FLAG = `standard`: MUST enumerate 20-30 roles.
- T1-DEPTH-FLAG = `deep`: MUST enumerate 50+ roles.
- MUST include exactly one role with `inertia` or `advocate` in its name.
- MUST group roles into area subdirs (min 2). Every role assigned to exactly one area.
- MUST write `.roles/{area}/{role}.md` for every role. Every file MUST contain: `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`.

FORBIDDEN: beginning Phase 3 before Phase 2 is complete.

---

## Phase 3 -- Org-Chart Assembly

FORBIDDEN: beginning Phase 3 before Phase 2 is complete.

Write `org-chart.md` containing:
1. ASCII box-and-line hierarchy (min 2 levels)
2. Headcount table: `Area` | `Headcount` | `Key Roles` | `Decides` | `Escalates`
3. Anti-pattern watch table
```

---

## What Made It Golden

Five structural patterns in V-01 distinguished it from all prior rounds and drove the score to 76.

**1. Triple-layer phase boundaries (C-40)**
Every phase transition carries three orthogonal enforcement locations: the outbound Constraints FORBIDDEN, the PHASE-ORDERING-GUARD field embedded as the first entry inside the record block, and a standalone "Boundary Guard" section visible as its own navigation point. No prior round achieved all three layers at every boundary. The standalone Boundary Guard is the structural innovation -- it makes boundary compliance independently auditable without reading through Constraints or Input Contracts.

**2. Declarative error-framing paired with Constraints FORBIDDEN (C-41)**
Task step bodies describe error conditions in declarative prose ("Both is an error. Neither is an error.") while all imperative enforcement lives exclusively in the Constraints section as FORBIDDEN directives. This two-tier pattern separates explanation (task prose narrates what constitutes an error) from enforcement (Constraints prohibits it). C-39 forbids FORBIDDEN inside task steps; C-41 codifies the positive form that replaces it.

**3. Record blocks as unified constructs (C-26, C-28)**
Each `=== RECORD: PHASE-N ===` block simultaneously serves as gate variable declaration, phase-ordering anchor, and materialized checkpoint -- with PHASE-ORDERING-GUARD as its structurally first field. A reader seeing only the record block can derive the gate schema, the ordering constraint, and the materialization artifact without cross-referencing any other section.

**4. Bidirectional verdict guard covering both failure modes (C-15, C-13)**
The verdict constraint covers both directions symmetrically: "FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Both is an error." AND "FORBIDDEN: writing neither CAN-OPERATE-FLAT nor STRUCTURE-WARRANTED. Neither is an error." Prior rounds covered only the "both" direction. The "neither" case is equally a failure mode and must be explicitly prohibited.

**5. GLOBAL CONSTANTS declared pre-phase, consumed by reference only (C-36, C-17)**
TABLE-A (verbatim IA scope templates keyed to T2-PRESSURE) and TABLE-B (category derivation keyed to T2-VERDICT) are declared once before Phase 1. Phase instructions reference these tables by name only -- no inline embedding. The verbatim requirement on TABLE-A scope text (paraphrase fails C-17) is enforced as a structural property: the text is fixed in the constant, and the phase instruction points to it.

---

## Final Rubric Summary (v15)

| Tier | Criteria | Weight |
|------|----------|--------|
| Essential | C-01 through C-05 | 60 |
| Recommended | C-06 through C-08 | 30 |
| Aspirational | C-09 through C-41 | 10 |

**V-01 score breakdown:**
- Essential: 4/5 (C-05 failed -- Decides/Escalates columns not enforced in Phase 4 task steps)
- Recommended: 2/3 (C-07 failed -- Phase 4 task steps absent, no rhythm row count enforcement)
- Aspirational: 25/31 (C-09, C-10, C-16, C-19, C-22, C-31 failed)

**Composite:** (4/5 x 60) + (2/3 x 30) + (25/31 x 10) = 48.0 + 20.0 + 8.1 = **76**

**C-05 is the highest-value fix for Round 21:** specifying Decides/Escalates columns in Phase 3
constraints (not just preamble) recovers 12 points toward a potential score of 88.
