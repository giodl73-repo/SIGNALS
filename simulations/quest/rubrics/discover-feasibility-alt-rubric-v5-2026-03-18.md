Written to `simulations/quest/rubrics/discover-feasibility-alt-rubric-v5-2026-03-18.md`.

---

## What changed in v5

**Two new aspirational criteria** from R6 patterns:

**C-17 — VERDICT prerequisites block is guarded by an explicit iff-condition as static body text**
From V-03 pattern (C-02 FAIL): the iff guard must be authored as static template body text — `[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]` — not left to model inference. Extends C-16's body-encoding principle to VERDICT conditional rendering. Distinct from C-02 (output behavior) — C-17 tests the template mechanism. A template may fail C-17 (no guard text) while a model incidentally suppresses prerequisites in a single test (C-02 PASS), making the guarantee probabilistic rather than structural. V-03 is the canonical failure case: guard removed → C-02 FAIL in output; C-17 would have caught the defect upstream. Passes N/A if no prerequisites block exists.

**C-18 — AMENDMENTS template independently authors three structurally orthogonal sub-lines per amendment**
From V-02 pattern (C-04 PARTIAL, C-06 PASS): each amendment entry must be three independently-removable sub-lines — (1) action line naming the component, (2) color-transition line with color change and score-delta, (3) "Inertia saved:" line closing the four-surface inertia narrative. V-02 isolates orthogonality cleanly: removing sub-line 3 → C-04 PARTIAL while C-06 PASS; removing sub-line 2 → C-06 FAIL while C-04 surface 4 intact. Distinct from C-04 and C-06 (output presence) — C-18 tests whether the template explicitly authors all three as independent obligations. Passes N/A if no AMENDMENTS section exists.

**Scoring denominator**: `/8` → `/10`. Maximum composite unchanged at 100.

**Floor calculations under v5:**
- V-03 pattern: `(4/5 × 60) + (3/3 × 30) + (9/10 × 10) = 87.000` (vs 88.000 in v4 — C-17 FAIL absorbed)
- V-02 pattern: `(4.5/5 × 60) + (3/3 × 30) + (9/10 × 10) = 93.000` (vs 94.000 in v4 — C-18 FAIL absorbed)
cause C-06 FAIL while leaving C-04 surface 4 intact. A template that merges multiple sub-structures into a single line, or omits any sub-line, fails C-18. This is a template-authoring check distinct from C-04 (which tests inertia surface presence in the output) and C-06 (which tests amendment traceability in the output): C-18 tests whether the template explicitly authors all three sub-structures as independent obligations. Passes N/A if the template contains no AMENDMENTS section.

**Scoring denominator** updated from `/8` to `/10` for the aspirational block. Maximum composite unchanged at 100.

**Floor calculation for worst-case set (V-03 pattern under v5):**
```
Composite = (4/5 * 60) + (3/3 * 30) + (9/10 * 10) = 48 + 30 + 9 = 87.000
```
vs 88.000 in v4 — the `/10` denominator absorbs C-17 FAIL in the V-03 pattern set (C-02 FAIL essential + C-17 FAIL aspirational).

**V-02 composite under v5:**
```
Composite = (4.5/5 * 60) + (3/3 * 30) + (9/10 * 10) = 54 + 30 + 9 = 93.000
```
vs 94.000 in v4 — C-18 FAIL absorbs into the `/10` denominator (C-04 PARTIAL essential + C-18 FAIL aspirational).

**R6 patterns absorbed into evaluation notes (not new criteria):**
- C-17/C-02 independence confirmed: C-02 tests whether the guard works in output; C-17 tests whether the guard is written in the template body. A model may suppress prerequisites correctly in a single test run while C-17 fails — the guarantee is not structural, only probabilistic. The V-03 evidence establishes that removing the explicit guard text causes C-02 FAIL in output; C-17 is the mechanism check that would have caught the template defect upstream.
- C-18/C-04/C-06 orthogonality confirmed: V-02 isolates the three-line structure cleanly. C-06 PASS with C-04 PARTIAL proves that the color-transition traceability sub-structure and the inertia-continuity sub-structure are independently satisfiable. C-18 makes the independence structural by requiring all three sub-lines to be explicitly authored as separate template obligations.

---

## What changed in v4

**One new aspirational criterion** from R3 patterns:

**C-16 — Proceed-gate and back-reference mechanism text is body-encoded independently of section ordering**
From V-04 pattern: body preserves STRATEGY→ARCHITECT order, but mechanism sentences are removed. Result: C-10 PASS, C-14 PASS, C-11 FAIL, C-12 FAIL. The key insight: ordering guarantee does not subsume mechanism completeness — the proceed-gate and confirmation sentences must be explicitly authored as body text. C-16 is a text-presence check orthogonal to both C-11 (forward-declaration timing) and C-12 (semantic cross-reference). It detects the case where mechanism text was never written at all, regardless of ordering state.

**Scoring denominator** updated from `/7` to `/8`. Maximum composite unchanged at 100.

**Floor calculation for worst-case set (V-03 pattern):**
```
Composite = (5/5 * 60) + (3/3 * 30) + (1.5/8 * 10) = 91.875
```
vs 92.143 in v3 — the `/8` denominator absorbs C-16 FAIL in the compound-failure set.

**R3 patterns absorbed into evaluation notes (not new criteria):**
- C-14/C-15 independence confirmed: each fires on a distinct condition (body ordering vs. preamble conflict); V-02 isolates C-14 FAIL + C-15 PASS cleanly. Already captured in existing pass conditions; added as a C-16 evaluation note reminder.
- Zero-cost C-13 upgrade holds under `/8`: N/A and PASS both contribute 1 to the numerator, so the upgrade path remains cost-free when C-14 holds.

---

## What changed in v3

**Two new aspirational criteria** from R2 patterns:

**C-14 — Template body is the sole structural source for section ordering: preamble directive is documentational, not instrumental**
From V-04's zero-cost C-13 upgrade. The key insight: when the body already enforces STRATEGY-before-ARCHITECT, a matching preamble directive *documents* the guarantee rather than *creating* a model-compliance dependency. Distinct from C-13 (preamble-body agreement) -- C-14 asks whether the body would hold the ordering *even with no preamble at all*.

**C-15 — Structural guarantee chain is cascade-safe: C-11 and C-12 are by-construction reachable when C-10 holds**
From V-05's four-criterion cascade at 93.000. A preamble-template conflict doesn't just break C-13 -- it degrades C-10 from structural to probabilistic, which makes C-11 forward-declarations and C-12 back-references runtime-dependent rather than by-construction. A cascade-safe template prevents this by making the body the authoritative ordering source. In practice, C-14 PASS implies C-15 PASS; score independently to expose the load-bearing relationship.

**Scoring denominator** updated from `/5` to `/7` for the aspirational block. Maximum composite unchanged at 100.

---

## Essential Criteria

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | INFERENCE GATE has all required fields | completeness | essential | Feature, Team, and Timeline are all present and non-empty in the INFERENCE GATE section before any analysis begins. Focus is optional; its absence does not fail C-01. |
| C-02 | VERDICT has score + label consistent with range, prerequisites iff FEASIBLE WITH CAVEATS + RED | correctness | essential | VERDICT contains a numeric score (0-100) and a label (NOT FEASIBLE, FEASIBLE WITH CAVEATS, or FEASIBLE) both present. Label is consistent with score range: <50 = NOT FEASIBLE, 50-74 = FEASIBLE WITH CAVEATS, >=75 = FEASIBLE. Prerequisites listed iff label is FEASIBLE WITH CAVEATS and at least one RED component exists. |
| C-03 | ARCHITECT table has traffic-light ratings with RED Blockers | correctness | essential | Every component row in the ARCHITECT table carries GREEN, YELLOW, or RED. Every RED-rated component has a corresponding RED Blockers entry with all three sub-fields: blocker statement, Lift condition, and Do-nothing cost. "No RED components." is acceptable iff no RED rows exist. |
| C-04 | Inertia surfaces in all four required locations | coverage | essential | All four inertia surfaces present: (1) INERTIA: STATUS QUO section with Baseline sentence, (2) Do-nothing cost column in ARCHITECT table with a value on every row, (3) "Not building this means:" line in VERDICT, (4) "Inertia saved:" line on every amendment in AMENDMENTS. Any surface omitted fails this criterion. |
| C-05 | When focus is active, focus content is woven into existing sections | behavior | essential | If a focus value is provided (compliance, stakeholders, requirements, naming, size, or other), the focus-specific content appears integrated within the relevant existing sections -- not appended as a new standalone section after AMENDMENTS. Fails if focus content is additive-only (appended block). Passes automatically (N/A) if no focus is active. |

---

## Recommended Criteria

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | AMENDMENTS are traceable to RED or YELLOW components | depth | recommended | Every amendment names the specific component it addresses, states the color transition, and includes a score-delta estimate. Amendments not tied to a rated component, or missing the color transition, fail this criterion. |
| C-07 | Focus integration visibly influences the base analysis | depth | recommended | When focus is active, the focus content demonstrably changes the base analysis -- not just accompanies it. Passes automatically (N/A) if no focus is active. |
| C-08 | STRATEGY: BUILD-VS-BUY covers at least half of components | coverage | recommended | At least 50% of the components listed in the ARCHITECT table carry an explicit Build / Buy / Use existing recommendation in the STRATEGY section. |

---

## Aspirational Criteria

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | Focus constraint propagates to 2+ downstream sections | coverage | aspirational | When focus is active, the focus-introduced constraint must appear in at least two distinct downstream sections (e.g., ARCHITECT, INERTIA, VERDICT, AMENDMENTS). Presence in only one section fails C-09. Passes N/A if no focus is active. |
| C-10 | STRATEGY section precedes ARCHITECT table to structurally guarantee C-08 coverage | behavior | aspirational | The STRATEGY section appears before the ARCHITECT table in the output, converting C-08 from an output-checked instruction into a by-construction property -- every ARCHITECT component row has a prior STRATEGY entry because STRATEGY was already written at evaluation time. A response where ARCHITECT precedes STRATEGY fails C-10 even if C-08 passes independently. Passes N/A if the output contains no STRATEGY section. |
| C-11 | STRATEGY uses forward-declaration with proceed gate -- C-08 by-construction | behavior | aspirational | STRATEGY explicitly names the components it will hand off to ARCHITECT and commits a Build / Buy / Use recommendation for each before any ARCHITECT row appears. At least half of those declared components carry an explicit recommendation in STRATEGY (the proceed gate). A STRATEGY section that makes coverage recommendations without declaring them as forward commitments for ARCHITECT, or that does not name the components it is pre-committing, fails C-11. Passes N/A if the output contains no STRATEGY section. |
| C-12 | ARCHITECT section opens with an explicit back-reference to STRATEGY decisions | behavior | aspirational | The ARCHITECT section contains a semantic cross-reference to the prior STRATEGY section (e.g., "Using the STRATEGY decisions above," "Per the STRATEGY commitments," or equivalent). This establishes that ARCHITECT ratings are informationally dependent on STRATEGY, not merely adjacent to it. A stand-alone ARCHITECT section that does not reference STRATEGY fails C-12 even if STRATEGY physically precedes it and C-10 passes. Passes N/A if the output contains no STRATEGY section. |
| C-13 | Preamble ordering directive is consistent with template section sequence -- no structural conflict | behavior | aspirational | When the template contains an explicit section ordering directive (e.g., "Write STRATEGY before ARCHITECT"), the template body must present those sections in the same stated order. A preamble instruction that conflicts with the template body's section sequence creates a structural execution-order conflict: the model may follow template order rather than the preamble directive, making the guarantee probabilistic rather than by-construction. Fails if preamble and template body disagree on section order. Passes N/A if no ordering directive appears in the preamble. |
| C-14 | Template body is the sole structural source for section ordering: preamble directive is documentational, not instrumental | behavior | aspirational | The STRATEGY-before-ARCHITECT ordering must be enforced by the template body's section sequence independently of any preamble directive. When the body already enforces ordering, a matching preamble directive is purely documentational -- it converts C-13 from N/A to active PASS at zero composite cost without introducing a new model-compliance dependency. When the body does not enforce ordering, any preamble directive becomes instrumental: the guarantee then depends on model compliance with a text instruction rather than template structure. Fails if the template body places ARCHITECT before STRATEGY (the preamble cannot substitute for structural ordering). Passes N/A if no STRATEGY section exists. |
| C-15 | Structural guarantee chain is cascade-safe: C-11 and C-12 are by-construction reachable when C-10 holds | behavior | aspirational | The three ordering-dependent aspirational mechanisms (C-10, C-11, C-12) must be independently satisfiable without resolving a preamble-template ordering conflict at execution time. C-11 forward-declaration and C-12 semantic back-reference are by-construction reachable only when the template body places STRATEGY before ARCHITECT. A preamble-template conflict (C-13 FAIL) degrades C-10 from by-construction to probabilistic, cascading to C-11 and C-12: forward-declarations have no structural guarantee of preceding ARCHITECT rows, and back-references have no guaranteed target. A cascade-safe template embeds ordering in the body such that each of C-10, C-11, and C-12 can be satisfied or failed independently of preamble state. Fails if a preamble-template ordering conflict makes C-11 and C-12 runtime-dependent rather than structurally guaranteed. Passes N/A if no STRATEGY section exists. |
| C-16 | Proceed-gate and back-reference mechanism text is body-encoded independently of section ordering | behavior | aspirational | The STRATEGY section body text contains an explicit proceed-gate sentence -- language that names the components to be handed off to ARCHITECT and commits a Build/Buy/Use recommendation for at least half of them, stated as a forward commitment before ARCHITECT evaluation begins (not merely a backward reference to components already listed in ARCHITECT). AND the ARCHITECT section body text contains an explicit confirmation sentence -- language that cites the prior STRATEGY section by name as the basis for the current ratings. Both mechanism sentences must be present as static body text. This is a text-presence check distinct from C-11 (which tests forward-declaration timing) and C-12 (which tests semantic cross-reference): a template may satisfy C-10 and C-14 while failing C-16 when the mechanism sentences are absent (V-04 pattern), and may fail C-16 when mechanism text was replaced by backward-reference language (V-02/V-03 pattern). Fails if either mechanism sentence is absent from the template body. Passes N/A if no STRATEGY section exists. |
| C-17 | VERDICT prerequisites block is guarded by an explicit iff-condition as static body text | behavior | aspirational | The VERDICT prerequisites block must be preceded by an explicit iff-guard authored as static template body text (e.g., `[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]`), not left to model inference at runtime. This is a template-mechanism check distinct from C-02 (which tests output behavior -- whether prerequisites appear iff the condition holds): C-17 tests whether the suppression instruction exists as explicit body text. A template that renders the prerequisites block unconditionally (V-03 pattern: guard removed, block always present) fails C-17. A template that expects the model to infer suppression from context without an explicit guard also fails C-17. The failure modes are independent: a model may incidentally suppress prerequisites in a passing test case (C-02 PASS) while the template lacks the guard text (C-17 FAIL), making the guarantee probabilistic rather than structural. Passes N/A if the template contains no prerequisites block. |
| C-18 | AMENDMENTS template independently authors three structurally orthogonal sub-lines per amendment | behavior | aspirational | Each amendment entry in the AMENDMENTS template must be authored as three independently-removable sub-lines: (1) an action line naming the specific component addressed, (2) a color-transition line specifying the component, color change, and score-delta estimate, and (3) an "Inertia saved:" line closing the four-surface inertia narrative. Structural orthogonality: removing any sub-line degrades exactly one rubric criterion without affecting the others -- sub-line 2 satisfies C-06 traceability, sub-line 3 satisfies C-04 surface 4. The V-02 evidence isolates this: removing sub-line 3 causes C-04 PARTIAL while C-06 remains PASS; removing sub-line 2 would cause C-06 FAIL while C-04 surface 4 remains PASS. A template that merges sub-structures into a single line, omits any sub-line, or presents the three obligations as a single combined instruction fails C-18. Passes N/A if the template contains no AMENDMENTS section. |

---

## Scoring

```
Composite = (essential_pass    / 5  * 60)
          + (recommended_pass  / 3  * 30)
          + (aspirational_pass / 10 * 10)
```

PARTIAL scores count as 0.5 for the formula. PARTIAL on any essential criterion fails the Golden threshold regardless of composite score.

**Golden threshold**: all 5 essential criteria pass (no PARTIALs) AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Golden | all essential (no PARTIAL) + >= 80 | Ship-ready; alt version validates the unified hypothesis |
| Passing | all essential (PARTIAL allowed) + 60-79 | Usable, recommended gaps noted |
| Failing | any essential fails or PARTIAL | Not useful as a feasibility artifact |

---

## Evaluation Notes

- **C-05 is the diagnostic criterion for the A/B test**: the entire point of the alt version is that focus is woven in, not appended. Score C-05 strictly -- a new section added after AMENDMENTS is a structural failure even if the content is correct.
- **C-07 and C-05 are complementary**: C-05 checks structure (where focus content lives), C-07 checks effect (whether it changed the analysis). An output can pass C-05 (focus is woven in) but fail C-07 (the base sections are unchanged). The alt version wins the A/B test only if both pass.
- **C-04 partial pattern**: the Do-nothing cost column in the ARCHITECT table is the most frequently omitted inertia surface. Score each row independently -- one blank cell in a multi-row table is a PARTIAL.
- **C-09 is a propagation test, not a presence test**: identify the constraint introduced by focus, then trace it forward. If it does not recur in a second section, score FAIL.
- **C-10 is a section-ordering test**: verify STRATEGY section heading appears before ARCHITECT section heading. A correct ARCHITECT table that happens to precede STRATEGY still fails C-10. Do not infer ordering from content quality.
- **C-11 is a forward-declaration test, not a coverage test**: C-08 already checks that STRATEGY covers >=50% of components. C-11 checks whether STRATEGY explicitly names those components as forward commitments for ARCHITECT and states the proceed gate. A STRATEGY section that achieves 100% Build/Buy/Use coverage without naming components as ARCHITECT-bound fails C-11. The signal is the declaration structure, not the coverage count.
- **C-12 is a semantic dependency test**: physical ordering (C-10) and semantic dependency (C-12) are independent. An output can pass C-10 (STRATEGY physically precedes ARCHITECT) while failing C-12 (ARCHITECT makes no reference to STRATEGY decisions). Full structural integrity requires both.
- **C-13 is a template design test, not a model output test**: score based on whether the template's preamble ordering directive and its section body sequence agree. If they conflict, score FAIL regardless of how the model resolved the conflict in practice. The R1 evidence from V-03 is the canonical failure case: preamble says "STRATEGY before ARCHITECT"; template body places ARCHITECT before STRATEGY; model compliance is probabilistic (~70%) rather than by-construction.
- **C-14 is a body-independence test, not a preamble-agreement test**: C-13 checks that preamble and body agree. C-14 checks whether the body would enforce the ordering guarantee even if no preamble directive existed. A template can pass C-13 (preamble and body agree) while failing C-14 (body places ARCHITECT before STRATEGY, so the ordering is only enforced through the preamble instruction). The V-04 R2 finding establishes the positive case: when the body already enforces ordering, adding a matching preamble directive is zero cost -- documentational, not instrumental.
- **C-15 is a cascade-safety test**: score by asking whether a C-13 FAIL scenario would cascade to C-10 PARTIAL, C-11 FAIL, and C-12 FAIL simultaneously. If the template body places STRATEGY before ARCHITECT (C-14 passes), cascade is structurally impossible -- C-15 passes. If the body places ARCHITECT before STRATEGY (C-14 fails), a preamble conflict cascades through the chain -- C-15 fails. In practice, C-14 PASS implies C-15 PASS and C-14 FAIL implies C-15 FAIL. Score them independently to surface the load-bearing relationship. The V-05 R2 cascade (93.000 composite, four simultaneous failures) is the canonical failure case.
- **C-16 is a text-presence check, orthogonal to ordering state**: C-11 tests forward-declaration timing (STRATEGY commits before ARCHITECT evaluates); C-12 tests semantic back-reference (ARCHITECT cites STRATEGY by name). C-16 isolates mechanism text presence from ordering: it asks whether the proceed-gate sentence exists in STRATEGY body text and the confirmation sentence exists in ARCHITECT body text, regardless of which section physically precedes the other. A template may fail C-16 while passing C-10 and C-14 (V-04 pattern: correct body ordering but mechanism sentences removed). A template may also fail C-16 while failing C-10 (V-02/V-03 pattern: inverted body with backward-reference text replacing the proceed-gate sentence). Score C-16 by identifying whether each mechanism sentence is present as explicit template language -- do not infer from ordering state. C-14/C-15 independence reminder: C-14 fires on body-ordering inversion regardless of preamble state (V-02: C-14 FAIL, C-15 PASS when no preamble exists); C-15 fires only when a preamble-template conflict degrades C-10 to probabilistic (V-03). Do not tie C-15's verdict to C-14's verdict -- they detect distinct failure conditions.
- **C-17 is a template-mechanism test, not an output-behavior test**: C-02 tests whether prerequisites appear in output iff the condition holds. C-17 tests whether the iff-guard is written as explicit static body text in the template. The two failure modes are independent: a template may lack the guard text (C-17 FAIL) while a model happens to suppress prerequisites correctly in a given test case (C-02 PASS) -- the guarantee is probabilistic, not structural. Score C-17 by locating the prerequisites block in the template and checking whether it is preceded by an explicit conditional guard instruction. The V-03 R6 evidence is the canonical failure case: guard removed, prerequisites rendered unconditionally, C-02 FAIL in output. C-17 would have caught the template defect before running a test case.
- **C-18 is a template-authoring test, not an output-presence test**: C-04 surface 4 and C-06 already test whether specific amendment content appears in output. C-18 tests whether the template explicitly authors all three sub-lines as independent, named obligations. Score by locating each amendment entry in the template and verifying that three distinct sub-line instructions are present: an action line, a color-transition line, and an "Inertia saved:" line. Merged instructions (e.g., "include component name, color change, score delta, and inertia savings in a single line") fail C-18 even if the resulting output would satisfy C-04 and C-06. The V-02 R6 evidence is the canonical failure case: sub-line 3 removed, C-04 PARTIAL in output, C-06 PASS -- proving the sub-lines are structurally orthogonal and must be independently authored.
- **N/A handling**: C-05, C-07, and C-09 pass as N/A when no focus is active. C-10, C-11, C-12, C-14, C-15, and C-16 pass N/A if the output contains no STRATEGY section. C-13 passes N/A if no ordering directive appears in the preamble. C-17 passes N/A if the template contains no prerequisites block. C-18 passes N/A if the template contains no AMENDMENTS section.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-18 | New session. Carries forward C-01 through C-08 (all confirmed PASS 100.0 in 2026-03-17 R7). Aspirational pool trimmed to C-09 (confirmed) + C-10 (STRATEGY-before-ARCHITECT, from R7 excellence signals; pending empirical validation). Aspirational denominator /2. |
| v2 | 2026-03-18 | R1 validates C-10 (V-02 PASS, V-01 FAIL, V-03 PARTIAL). Three new aspirational criteria extracted from R1 excellence signals: C-11 (forward-declaration + proceed gate, from V-02 by-construction mechanism), C-12 (ARCHITECT semantic back-reference to STRATEGY, from V-02 cross-reference pattern), C-13 (preamble-template ordering consistency, from V-03 PARTIAL failure mode). Aspirational denominator updated from /2 to /5. |
| v3 | 2026-03-18 | R2 validates C-11 and C-12 (symmetric 2-point cost each, independently removable, non-redundant -- V-02 and V-03). Two new aspirational criteria extracted from R2 excellence signals: C-14 (template body is the sole structural source for ordering -- preamble directive is documentational not instrumental, from V-04 zero-cost C-13 upgrade), C-15 (structural guarantee chain is cascade-safe -- C-11 and C-12 by-construction reachable when C-10 holds, from V-05 four-criterion cascade at 93.000). Aspirational denominator updated from /5 to /7. |
| v4 | 2026-03-18 | R3 validates C-14/C-15 independence (V-02: C-14 FAIL, C-15 PASS confirms detectors are pairwise-independent). One new aspirational criterion extracted from R3 patterns: C-16 (proceed-gate and back-reference mechanism text is body-encoded independently of ordering -- from V-04 pattern showing C-10/C-14 PASS with C-11/C-12 FAIL when mechanism sentences removed). Aspirational denominator updated from /7 to /8. V-03 floor under v4: 91.875 (vs 92.143 in v3). |
| v5 | 2026-03-18 | R6 yields two new aspirational criteria. C-17 (VERDICT prerequisites block guarded by explicit iff-condition as static body text -- from V-03 pattern: C-02 FAIL when guard removed; extends C-16 body-encoding principle to VERDICT conditional rendering). C-18 (AMENDMENTS independently authors three structurally orthogonal sub-lines per amendment -- from V-02 pattern: C-04 PARTIAL + C-06 PASS when "Inertia saved:" removed proves action/color-transition/inertia-continuity are independently removable). Aspirational denominator updated from /8 to /10. V-03 floor under v5: 87.000 (vs 88.000 in v4). V-02 composite under v5: 93.000 (vs 94.000 in v4). |
