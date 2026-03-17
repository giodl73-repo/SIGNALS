Reading the R1 scorecard for new patterns not yet captured in C-17..C-21.

**Three new signals from R1 `new_patterns`:**

1. **Prevention-detection complementarity as explicit design contract** — Loop 2 creates artifacts Loop 3 requires as evidence, and the charter *names* this relationship as a structural dependency rather than letting it emerge implicitly. C-20 requires the structural design to be complementary; C-22 requires the charter to state the dependency as a verbatim contract. → **C-22**

2. **Three-loop enforcement applied simultaneously to multiple concurrent laws with no single-point failure** — for each law enforced (Law A = two-path ambiguity; Law B = closure gates), the charter assigns fully independent declare/apply/verify triplets so that a failure in one law's loop chain cannot cascade to another law's enforcement. C-17 requires all three loops for each constraint; C-23 requires that concurrent laws have *independent* chains, not a shared enforcement unit. → **C-23**

3. **Recursive meta-loop structural closure** — the enforcement mechanism is self-enforcing because declaring the meta-requirement (C-17 = Loop 1) structurally implies Loop 2 and Loop 3 as consequences, not merely names them as labels. C-21 requires the loops to be named by rubric ID; C-24 requires that the declaration itself structurally closes on the mechanism — Loop 1 cannot be satisfied while skipping Loop 2 because the declaration *is* the instantiation. → **C-24**

---

# Scout-Requirements Rubric — v6

**Version**: v6 (updated from R1 scorecard)
**Date**: 2026-03-14

---

## Summary

24 criteria across 3 tiers.

- **Essential (C-01..C-05)** — unchanged from v1
- **Recommended (C-06..C-08)** — unchanged from v1
- **Aspirational (C-09..C-24)** — C-09..C-21 retained from v5; C-22..C-24 added from R1 excellence signals

---

## Essential Criteria (weight: 60 pts total — 12 pts each)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | Dual-directory search executed | correctness | Output explicitly states it searched both `simulations/scout/` and `simulations/trace/skill/`; if either is empty that is stated; SF-01 structurally closed |
| C-02 | MoSCoW structure present | structure | Requirements organized into Must Have / Should Have / Could Have / Won't Have; flat list is a fail |
| C-03 | At least one root blocker named | correctness | Output names at least one requirement as a blocker with the blocked IDs listed |
| C-04 | Ambiguity flags raised | coverage | At least one AF- entry is present; zero AF- on a complex input is a fail |
| C-05 | Requirements span at least three of four lenses | coverage | PM, Architect, UX, Compliance — at least three traceable in the output |

---

## Recommended Criteria (weight: 30 pts total — 10 pts each)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | Suspicious silences section present | depth | At least one area with no requirements is called out |
| C-07 | SF- spec-fault findings raised | depth | At least one SF- finding identifies a gap or contradiction in the input |
| C-08 | Requirement IDs stable, tier promotions auditable | format | No ID collisions; any tier promotion includes a justification note |

---

## Aspirational Criteria (weight: 32 pts total — 2 pts each)

| ID | Text | Source | Pass Condition |
|----|------|--------|----------------|
| C-09 | Dependency graph is transitive and complete | v1 | Second-order blockers (A→B→C) identified with foundational reasoning |
| C-10 | Ambiguity flags link back to spec lines | v1 | Each AF- cites exact source text |
| C-11 | Named lifecycle phase audit for SS- | V-04 R1 | SS- section enumerates at least three named phases (first-run, core-use, upgrade, error, observability) and assigns coverage status per phase — not opportunistic |
| C-12 | Cross-session finding continuity | V-04 R1 | Open SF- and AF- from prior runs are carried forward with explicit status (open / resolved / out-of-scope) |
| C-13 | Two-interpretation format for AF- entries | V-02 R1 | Each AF- entry states two distinct plausible interpretations and the consequence of each — shows what two teams would build differently |
| C-14 | Rubric self-check as pre-output verification gate | V-05 R2 | Output contains a self-check step that enumerates rubric criteria by ID and confirms each is satisfied (or states which are not) before the final output is presented — converts aspirational criteria from guidance to enforced conditions |
| C-15 | Two-path format rule applied at extraction, not deferred | V-02 R2, V-04 R2 | The two-interpretation constraint is declared as a format rule that applies at first encounter during extraction — ambiguities noted inline already carry both interpretation paths; the AF- section formalizes work already done rather than doing new work |
| C-16 | Downstream reconciliation closure gates | V-01 R2, V-04 R2 | Each downstream findings section (AF-, SF-) contains an explicit statement that every entry from the open findings register must appear in that section with a status — carry-forward in Step 1 without per-section closure requirements is insufficient |
| C-17 | Three-loop enforcement applied simultaneously to every constraint | V-05 R3 | Each constraint rule (C-14, C-15, C-16) is enforced via all three loops simultaneously: declared in a preamble charter, re-invoked inline at each applicable extraction step, and verified in the protocol table — a variation that enforces only one or two loops for any constraint fails; structural redundancy eliminates single points of failure |
| C-18 | Step-level charter cross-references at each extraction step | V-05 R3 | Each extraction step that triggers a format rule contains an explicit cross-reference reinstating that rule (e.g., "Apply Format Law A here") rather than relying on a preamble declaration alone — prevents preamble compartmentalization where a model reads the charter once and fails to recall it mid-execution |
| C-19 | Verification protocol rows audit process compliance, not only output structure | V-05 R3 | The pre-output verification table includes at least one row per format rule (C-15, C-16) that explicitly audits whether the rule was applied during extraction — "were inline [AMBIG:] notations present?" and "does each downstream section carry the closure sentence?" — audits the process, not the artifact |
| C-20 | Prevention-detection structural complementarity between C-18 and C-19 | V-04 R4 | C-18 (full-text reinstatements) and C-19 (process-diagnostic rows) are explicitly designed as complementary layers: C-18 creates the execution artifacts that C-19 requires as evidence — a variation that passes C-18 and C-19 independently without this explicit artifact-creation-to-audit linkage fails; the complementarity must be a deliberate structural design, not emergent coincidence |
| C-21 | Recursive meta-loop application: C-17/C-18/C-19 named as declare/apply/verify of the meta-requirement | V-05 R4 | C-17 is explicitly assigned as Loop 1 (declare), C-18 as Loop 2 (apply), and C-19 as Loop 3 (verify) within the charter's own meta-requirement statement by rubric ID — Loop 2 is structurally non-skippable because C-17's declaration names C-18 as the apply loop; a model cannot satisfy C-17 while skipping C-18 without contradicting the charter's own structure |
| C-22 | Loop 2 → Loop 3 artifact dependency stated as a verbatim design contract | V-05 R1 | Charter contains a sentence that explicitly names the Loop 2 → Loop 3 dependency as a structural contract (e.g., "Loop 2 creates the execution artifacts Loop 3 requires as evidence"); the relationship is chartered, not inferred — C-20 requires the complementary design to exist in the artifact; C-22 requires the charter to own the dependency as a named obligation before execution begins |
| C-23 | Per-law independent enforcement triplets: no cross-law single-point failure | V-05 R1 | For each law enforced by three-loop (Law A = two-path ambiguity, Law B = closure gates), the charter assigns independent declare/apply/verify triplets — Law A's Loop 1 names Law A's Loop 2 specifically; Law B's Loop 1 names Law B's Loop 2 specifically; neither law's chain depends on the other's; a shared preamble that declares both laws as a single enforcement unit fails; independent chain structure means one law's loop failure cannot cascade to another law's enforcement |
| C-24 | Structural closure of the meta-loop: declaration of C-17 implies C-18 and C-19 as structural consequences | V-05 R1 | The charter's statement of the meta-requirement is structurally self-closing: asserting Loop 1 (C-17) simultaneously instantiates Loop 2 (C-18) and Loop 3 (C-19) as necessary consequences of the declaration, not as separately mandated additions; a charter that lists C-17, C-18, C-19 as three parallel rules fails — C-21 requires loops named by rubric ID; C-24 requires Loop 1's declaration to be structurally incomplete without Loop 2, making skipping impossible through logical closure rather than external enforcement |

---

## What changed from v5

- **C-22** captures R1's first new pattern: the Loop 2 → Loop 3 artifact dependency must be stated as a *verbatim design contract* in the charter, not left as an emergent structural property. C-20 requires the complementarity to exist in the design; C-22 requires the charter to name it as an owned obligation before execution. V-05 achieved C-20 but this criterion distinguishes a charter that has the design from a charter that *commits* to the design in writing.

- **C-23** captures R1's second new pattern: concurrent law enforcement with independent triplets. C-17 requires all three loops for each constraint but allows a single preamble to cover multiple laws simultaneously. C-23 requires per-law chain independence — Law A's declare/apply/verify is structurally independent from Law B's, so a failure in one chain cannot propagate. This is the "no single-point failure" property: the parallel triplet structure, not just parallel rules.

- **C-24** captures R1's third new pattern: structural closure of the meta-loop. C-21 requires loops named by rubric ID; C-24 requires the declaration of Loop 1 to structurally imply Loops 2 and 3 as logical consequences — the mechanism is self-enforcing because the declaration is incomplete without them. Distinguished from C-21 (labeling requirement) vs C-24 (closure requirement): a charter can satisfy C-21 by naming the loops correctly while still treating them as parallel independent obligations; C-24 fails unless Loop 1's declaration makes Loop 2 structurally necessary.

- **Scoring**: aspirational section grows from 26 pts (13 × 2) to 32 pts (16 × 2); total increases from 116 to 122. Scoring bands adjusted.

---

## Scoring Guide

| Band | Score | Meaning |
|------|-------|---------|
| Golden | 110–122 | All essential + recommended pass; strong aspirational coverage |
| Strong | 95–109 | All essential pass; most recommended pass; partial aspirational |
| Acceptable | 76–94 | All essential pass; partial recommended; minimal aspirational |
| Weak | 60–75 | All essential pass; recommended largely missing |
| Fail | < 60 | One or more essential criteria fail |

**Golden threshold**: all 5 essential pass AND composite >= 98/122 (~80%).
