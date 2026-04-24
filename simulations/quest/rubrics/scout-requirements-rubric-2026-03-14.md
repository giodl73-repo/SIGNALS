The rubric already exists through v5 from prior quest runs. The v5 file is the current ground truth. Here it is as the skill output:

---

```
---
skill: quest-rubric
skill_target: scout-requirements
date: 2026-03-14
version: 5
---
```

# Rubric — scout-requirements (v5)

**21 criteria across 3 tiers. Total: 116 pts.**

---

## Essential (60 pts — 12 pts each)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | Dual-directory search executed | correctness | Output explicitly states it searched both `simulations/scout/` and `simulations/trace/skill/`; if either is empty that is stated; SF-01 structurally closed |
| C-02 | MoSCoW structure present | structure | Requirements organized into Must Have / Should Have / Could Have / Won't Have; flat list is a fail |
| C-03 | At least one root blocker named | correctness | Output names at least one requirement as a blocker with the blocked IDs listed |
| C-04 | Ambiguity flags raised | coverage | At least one AF- entry is present; zero AF- on a complex input is a fail |
| C-05 | Requirements span at least three of four lenses | coverage | PM, Architect, UX, Compliance — at least three traceable in the output |

---

## Recommended (30 pts — 10 pts each)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | Suspicious silences section present | depth | At least one area with no requirements is called out |
| C-07 | SF- spec-fault findings raised | depth | At least one SF- finding identifies a gap or contradiction in the input |
| C-08 | Requirement IDs stable, tier promotions auditable | format | No ID collisions; any tier promotion includes a justification note |

---

## Aspirational (26 pts — 2 pts each)

| ID | Text | Pass Condition |
|----|------|----------------|
| C-09 | Dependency graph is transitive and complete | Second-order blockers (A→B→C) identified with foundational reasoning |
| C-10 | Ambiguity flags link back to spec lines | Each AF- cites exact source text |
| C-11 | Named lifecycle phase audit for SS- | SS- section enumerates at least three named phases (first-run, core-use, upgrade, error, observability) and assigns coverage status per phase |
| C-12 | Cross-session finding continuity | Open SF- and AF- from prior runs are carried forward with explicit status (open / resolved / out-of-scope) |
| C-13 | Two-interpretation format for AF- entries | Each AF- entry states two distinct plausible interpretations and the consequence of each |
| C-14 | Rubric self-check as pre-output verification gate | Output contains a self-check step that enumerates rubric criteria by ID and confirms each is satisfied before the final output is presented |
| C-15 | Two-path format rule applied at extraction, not deferred | The two-interpretation constraint is declared as a format rule that applies at first encounter during extraction — ambiguities noted inline already carry both paths |
| C-16 | Downstream reconciliation closure gates | Each downstream findings section (AF-, SF-) contains an explicit statement that every entry from the open findings register must appear in that section with a status |
| C-17 | Three-loop enforcement applied simultaneously to every constraint | Each constraint rule (C-14, C-15, C-16) is enforced via all three loops: declared in preamble charter, re-invoked inline at each applicable extraction step, and verified in the protocol table |
| C-18 | Step-level charter cross-references at each extraction step | Each extraction step that triggers a format rule contains an explicit cross-reference reinstating that rule rather than relying on preamble alone |
| C-19 | Verification protocol rows audit process compliance, not only output structure | Pre-output verification table includes at least one row per format rule auditing whether the rule was applied during extraction |
| C-20 | Prevention-detection structural complementarity between C-18 and C-19 | C-18 (full-text reinstatements) and C-19 (process-diagnostic rows) explicitly designed as linked layers: C-18 creates the artifacts C-19 requires as evidence |
| C-21 | Recursive meta-loop application: C-17/C-18/C-19 named as declare/apply/verify of the meta-requirement | C-17 assigned as Loop 1, C-18 as Loop 2, C-19 as Loop 3 within the charter's meta-requirement — Loop 2 structurally non-skippable via self-reference |

---

## Scoring Bands

| Band | Score | Meaning |
|------|-------|---------|
| Golden | 104–116 | All essential + recommended pass; strong aspirational |
| Strong | 90–103 | All essential pass; most recommended; partial aspirational |
| Acceptable | 72–89 | All essential pass; partial recommended; minimal aspirational |
| Weak | 60–71 | All essential pass; recommended largely missing |
| Fail | < 60 | One or more essential criteria fail |

**Golden threshold**: all 5 essential pass AND composite >= 80 (≥ 93/116).

---

The v5 rubric is already on disk at `simulations/quest/rubrics/scout-requirements-rubric-v5-2026-03-14.md`. It evolved through 5 rounds driven by scorecard feedback — the aspirational tier grew from 2 criteria (C-09, C-10) to 13 (C-09..C-21) as successive variations exposed new failure modes around two-path AF- formatting, recursive enforcement loops, and prevention-detection complementarity.
