Written to `simulations/quest/rubrics/discover-feasibility-alt-rubric-v2-2026-03-18.md`.

---

## What changed in v2

**Three new aspirational criteria** extracted from R1 excellence signals:

**C-11 — STRATEGY forward-declaration + proceed gate** (from V-02's by-construction mechanism)
STRATEGY must explicitly name the components it is pre-committing for ARCHITECT and gate progress on at least half carrying a Build/Buy/Use recommendation. Distinct from C-08 (which checks coverage) — C-11 checks the *declaration structure* that makes coverage by-construction. A 100%-coverage STRATEGY that doesn't name components as ARCHITECT-bound still fails C-11.

**C-12 — ARCHITECT semantic back-reference to STRATEGY** (from V-02's cross-reference pattern)
ARCHITECT must contain an explicit reference to STRATEGY decisions ("Using the STRATEGY decisions above," etc.), establishing informational dependency rather than mere physical adjacency. C-10 (ordering) and C-12 (dependency) are independent: an output can pass C-10 while failing C-12 if ARCHITECT is self-contained.

**C-13 — Preamble ordering directive consistent with template section sequence** (from V-03's PARTIAL failure mode)
When a preamble says "write X before Y," the template body must also present X before Y. The V-03 PARTIAL is the canonical failure case: explicit preamble prohibition + template body conflict = ~70% compliance probability rather than by-construction guarantee. This is a template design test, not a model output test.

**Scoring denominator** updated from `/2` to `/5` for the aspirational block. Maximum composite unchanged at 100.
w, (3) "Not building this means:" line in VERDICT, (4) "Inertia saved:" line on every amendment in AMENDMENTS. Any surface omitted fails this criterion. |
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

---

## Scoring

```
Composite = (essential_pass    / 5  * 60)
          + (recommended_pass  / 3  * 30)
          + (aspirational_pass / 5  * 10)
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
- **N/A handling**: C-05, C-07, and C-09 pass as N/A when no focus is active. C-10, C-11, and C-12 pass N/A if the output contains no STRATEGY section. C-13 passes N/A if no ordering directive appears in the preamble.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-18 | New session. Carries forward C-01 through C-08 (all confirmed PASS 100.0 in 2026-03-17 R7). Aspirational pool trimmed to C-09 (confirmed) + C-10 (STRATEGY-before-ARCHITECT, from R7 excellence signals; pending empirical validation). Aspirational denominator /2. |
| v2 | 2026-03-18 | R1 validates C-10 (V-02 PASS, V-01 FAIL, V-03 PARTIAL). Three new aspirational criteria extracted from R1 excellence signals: C-11 (forward-declaration + proceed gate, from V-02 by-construction mechanism), C-12 (ARCHITECT semantic back-reference to STRATEGY, from V-02 cross-reference pattern), C-13 (preamble-template ordering consistency, from V-03 PARTIAL failure mode). Aspirational denominator updated from /2 to /5. |
