# org-pr — Quest Score — Round 7 (v7 Rubric)

**Skill**: org-pr | **Rubric**: v7 | **Date**: 2026-03-16
**N_essential**: 5 | **N_recommended**: 5 | **N_aspirational**: 17

---

## Essential Criteria (max 60 pts)

All variations PASS all essential criteria.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| C-01 Multi-role coverage | PASS | PASS | PASS | PASS | PASS | All have per-role review section with authority chain |
| C-02 P1/P2/P3 on every finding | PASS | PASS | PASS | PASS | PASS | Finding table requires P1/P2/P3 in Severity column |
| C-03 File-based role selection | PASS | PASS | PASS | PASS | PASS | Role Selection section: "identify roles by changed file surface area" |
| C-04 Explicit go/no-go verdict | PASS | PASS | PASS | PASS | PASS | Verdict section with Go/Conditional-Go/No-Go + derivation |
| C-05 Per-role structure / no bleeding | PASS | PASS | PASS | PASS | PASS | Named role header + isolated finding table per role |
| **Essential total** | **60** | **60** | **60** | **60** | **60** | |

---

## Recommended Criteria (max 30 pts)

All variations PASS all recommended criteria.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| C-06 Projection-aware consensus | PASS | PASS | PASS | PASS | PASS | "ALIGNED or DIVERGENT" projection convergence call |
| C-07 Conflict analysis (resolution present) | PASS | PASS | PASS | PASS | PASS | V-01/V-02: standalone table; V-03/V-04: embedded in Authority Chain; all have resolution logic |
| C-08 Locator self-correction gate | PASS | PASS | PASS | PASS | PASS | "Locator self-correction gate: If invalid → rewrite to most specific anchor" |
| C-09 Phase/lifecycle gating | PASS | PASS | PASS | PASS | PASS | Phase Gate section halts on post-merge PR |
| C-10 Downstream risk field | PASS | PASS | PASS | PASS | PASS | Downstream Risk column in per-role finding table |
| **Recommended total** | **30** | **30** | **30** | **30** | **30** | |

*C-07 note*: PASS requires presence of a conflict resolution mechanism, not a specific table format. C-22 (aspirational) tests the table format requirement specifically. V-03/V-04's embedded procedure satisfies C-07 but fails C-22.

---

## Aspirational Criteria (max 10 pts — N=17)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-11 Formula lock | PASS | PASS | PASS | PASS | PASS |
| C-12 Named invalid forms | PASS | PASS | PASS | PASS | PASS |
| C-13 Inertia / if-stays framing | PASS | PASS | PASS | PASS | PASS |
| C-14 Verdict escape closure | PARTIAL | PARTIAL | PARTIAL | PASS | PASS |
| C-15 Projection convergence call | PASS | PASS | PASS | PASS | PASS |
| C-16 Self-correction gate pre-commit | PASS | PASS | PASS | PASS | PASS |
| C-17 Role authority sequence declaration | PASS | PASS | PASS | PASS | PASS |
| C-18 Axis conflict resolution rule | N/A→PASS | N/A→PASS | N/A→PASS | N/A→PASS | PASS |
| C-19 Verdict hardening pair | PARTIAL | PARTIAL | PARTIAL | PASS | PASS |
| C-20 Priority table as composition mechanism | N/A→PASS | N/A→PASS | N/A→PASS | N/A→PASS | PASS |
| C-21 Authority-inertia reconciliation rule | N/A→PASS | PASS | PASS | PASS | PASS |
| C-22 Conflict resolution column | PASS | PASS | **FAIL** | **FAIL** | PASS |
| C-23 Judgment-elimination declaration | PASS | PASS | PASS | PASS | PASS |
| C-24 Correction-paired invalid form catalog | PASS | PASS | PASS | PASS | PASS |
| C-25 Co-occurrence coupling label | PASS | PASS | PASS | PASS | PASS |
| C-26 Governance scope declaration | **FAIL** | PASS | PASS | PASS | PASS |
| C-27 Priority axis non-redundancy | N/A→PASS | N/A→PASS | N/A→PASS | N/A→PASS | PASS |

### Evidence Notes

**C-12 (all)**: Three-form catalog (Untagged / Revision / Aggregate) with correction instructions in per-role section. R7 confirms: fires at V-03-level complexity without a priority table.

**C-13 (all)**: If-Stays Projection column present in per-role table. R7 confirms: fires independently of whether inertia is declared as a governance axis.

**C-14 V-01/V-02/V-03**: "There is no fourth outcome. Reclassify any P1 or accept No-Go." Both escape paths named but exclusion statement absent → PARTIAL. Caps C-19 at PARTIAL for same variations.

**C-14 V-04/V-05**: "No other escape path exists. A P1 + Go claim is invalid under this formula." Explicit exclusion closes the gap → PASS.

**C-18/C-20 V-01 through V-04**: No priority table present; N/A→PASS (single-axis or two-axis below table threshold). V-05: 3-axis Axis Composition Table triggers both as direct PASS.

**C-21 V-01**: If-stays column present but inertia is not declared as a governance axis — no reconciliation rule needed → N/A→PASS.

**C-21 V-02/V-03/V-04**: Opening declares "two governance axes: authority chain and inertia framing" + explicit reconciliation rule ("compounding cost — not a reclassification") → PASS.

**C-22 V-01/V-02**: Standalone Conflict Analysis section with resolution column using authority-position logic → PASS.

**C-22 V-03/V-04**: Conflict resolution embedded as procedural instruction in Authority Chain section. No standalone conflict table → FAIL. Permanent structural cap: 0.59 pts lost.

**C-23 V-03/V-04**: "derived mechanically from the authority chain — no judgment required" appears in the embedded conflict instruction. C-23 tests phrase presence, not location → PASS. Phrase survives embedding.

**C-26 V-01**: No axis count declaration. Axis structure inferrable only from section headers → FAIL.

**C-26 V-02/V-03/V-04**: "This prompt operates under two governance axes:" opens the prompt → PASS.

**C-26 V-05**: "This prompt operates under three governance axes." in the Axis Composition Table opening, with named axes in table rows → PASS.

**C-27 V-01 through V-04**: No priority table → N/A→PASS.

**C-27 V-05**: Three axes — authority chain (propagation direction / which role governs), inertia framing (finding content / what the if-stays says), conflict resolution column (conflict table output / how the resolution field is populated). Each governs a distinct domain unreachable from the other two. None is a subdivision or consequence of another → PASS.

---

## Aspirational Score Computation

| Variation | PASS count | PARTIAL (×0.5) | FAIL | PASS_equiv | Aspirational pts |
|-----------|-----------|-----------------|------|------------|-----------------|
| V-01 | 14 | 2 | 1 | 15.0 | **8.82** |
| V-02 | 15 | 2 | 0 | 16.0 | **9.41** |
| V-03 | 14 | 2 | 1 | 15.0 | **8.82** |
| V-04 | 16 | 0 | 1 | 16.0 | **9.41** |
| V-05 | 17 | 0 | 0 | 17.0 | **10.00** |

*V-01 PASS_equiv = 14 (direct PASS) + 1.0 (2 PARTIAL × 0.5) + 0 (C-26 FAIL) = 15.0*
*V-02 PASS_equiv = 15 (direct PASS) + 1.0 (2 PARTIAL × 0.5) = 16.0*
*V-03 PASS_equiv = 14 (direct PASS) + 1.0 (2 PARTIAL × 0.5) + 0 (C-22 FAIL) = 15.0*
*V-04 PASS_equiv = 16 (direct PASS) + 0 (C-22 FAIL) = 16.0*
*V-05 PASS_equiv = 17.0*

---

## Composite Score Summary

| Variation | Essential | Recommended | Aspirational | **Composite** | Rank |
|-----------|-----------|-------------|--------------|---------------|------|
| V-05 | 60 | 30 | 10.00 | **100.00** | #1 |
| V-02 | 60 | 30 | 9.41 | **99.41** | #2 |
| V-04 | 60 | 30 | 9.41 | **99.41** | #2 |
| V-01 | 60 | 30 | 8.82 | **98.82** | #4 |
| V-03 | 60 | 30 | 8.82 | **98.82** | #4 |

---

## Excellence Signals — V-05 Analysis

V-05 is R6 V-04 with one sentence added. The Axis Composition Table already existed; the 3-axis design was already non-redundant (C-27 PASS was structurally implicit). The only gap was C-26: the axis count was derivable from the table but never stated directly.

**Excellence Signal 1 — Explicit governance scope declaration as the opening statement**: "This prompt operates under three governance axes." The phrase does two things simultaneously: it fixes the count so axis-count disputes are foreclosed at the start, and it creates a forward-reference anchor for the table that follows. The signal's location (first substantive sentence under the section header) means a reviewer encounters the scope before any operational instruction — governance context precedes governance mechanics. This is the same pattern as C-23's judgment-elimination declaration: naming the boundary once, at the decision point, so reviewers cannot reopen it.

**Excellence Signal 2 — Non-redundant tripartite axis architecture (ordering / content / format)**: The 3-axis table in V-05 partitions governance into three non-overlapping domains — authority chain (which role's position governs conflict), inertia framing (what content appears in the surviving finding's if-stays field), conflict resolution column (how the resolution output is formatted in the conflict table). Each axis covers exactly one decision dimension; none is derivable from another. This is not simply "more axes" — it is the minimum-axis design that covers the three independent decision dimensions present in this skill's output. C-27 encodes the non-redundancy rule; V-05 demonstrates the stable architecture that satisfies it.

No new criteria candidates emerge. Both excellence signals are already captured in C-26 and C-27. The v7 criteria set is complete for the patterns visible at this complexity level.

---

## Round 7 Summary

**Confirmed findings:**

| Finding | Evidence |
|---------|----------|
| C-12/C-13 are complexity-independent | V-01 achieves PASS on both at V-03 complexity with no priority table |
| C-26 is the cheapest remaining gap at mid-complexity | V-01→V-02 delta = +0.59 pts from one opening sentence |
| Embedded conflict preserves C-23, breaks C-22 | V-03 PASS/FAIL pattern confirmed |
| Embedded-conflict path caps at 99.41 | V-04 confirms C-22 FAIL = permanent -0.59 ceiling |
| C-26 backports to 3-axis designs with no structural changes | V-05 = R6 V-04 + single phrase = 100.00 |

**R8 direction**: Two questions remain open. (a) Can C-22 be satisfied via a per-role inline conflict row (each role's table includes a conflict entry column), giving the embedded-conflict path a shot at 100.00 without a global Conflict Analysis section? (b) Can the 2-axis designs (V-02/V-04) reach 100.00 by adding a standalone Conflict Analysis table — removing the structural distinction between 2-axis and 3-axis paths?

---

```json
{"top_score": 100.00, "all_essential_pass": true, "new_patterns": []}
```
