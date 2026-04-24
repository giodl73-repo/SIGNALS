---
skill: quest-rubric
skill_target: org-roles
date: 2026-03-15
version: 1
---

# Scoring Rubric: org-roles

Evaluates output from the `org-roles` skill, which generates a typed role registry for a domain by analyzing product, codebase, or spec context and emitting structured role files to `.roles/{area}/`.

---

## Criteria

### Essential (60 pts total — all must pass)

| ID | Text | Category | Weight | Pass Condition |
|----|------|----------|--------|----------------|
| C-01 | **Role schema completeness** — every emitted role file contains all six required fields: `name`, `orientation` (with `frame` and `serves` sub-fields), `lens` (with `verify_questions` and `simplify_rules` sub-fields), `expertise` (with `depth` and `relevance` sub-fields), `scope`, and `collaborates_with`. | correctness | essential | PASS if 100% of role files contain all six top-level fields and the required sub-fields under `orientation`, `lens`, and `expertise`. FAIL if any field or sub-field is absent or empty in any role file. |
| C-02 | **Devil-advocate role present** — an inertia-check role exists whose stated purpose is to challenge every proposal by arguing the status quo is sufficient. | correctness | essential | PASS if at least one role file has a name or orientation that explicitly identifies it as a devil-advocate / status-quo challenger, and its `lens.verify_questions` include at least one question of the form "why is the current approach insufficient?" FAIL if no such role exists or its job is generic skepticism without a status-quo framing. |
| C-03 | **Stock roles present** — PM, Architect, and Strategy roles are always emitted regardless of domain input. | coverage | essential | PASS if the output directory contains at least one file identifiable as each of: a product manager role, a software/systems architect role, and a strategy/business role. FAIL if any of the three stock roles is absent. |
| C-04 | **Output location correct** — all role files are written to `.roles/{area}/` as individual Markdown files, where `{area}` reflects the domain derived from context. | format | essential | PASS if all files land in a `.roles/` subdirectory named after the target area, and each file is a `.md` file. FAIL if files are written to a different path, bundled into a single file, or the area subdirectory is missing or named generically (e.g., `default`). |
| C-05 | **At least one context-derived domain expert** — the role set includes at least one domain expert role whose name, frame, and verify questions are specific to the analyzed product/codebase/spec, not a generic template. | correctness | essential | PASS if at least one role has a `frame` that references a domain-specific concern (e.g., "data pipeline correctness", "auth boundary enforcement", "signal fidelity") that could not apply verbatim to an unrelated domain. FAIL if every role beyond the three stock roles is a generic archetype (e.g., "Domain Expert") with no domain-specific content. |

---

### Recommended (30 pts total — output is better with these)

| ID | Text | Category | Weight | Pass Condition |
|----|------|----------|--------|----------------|
| C-06 | **Orientation coherence** — `frame` describes the role's epistemic viewpoint and `serves` names the stakeholder or system concern that benefits from that perspective; the two sub-fields are internally consistent and non-redundant. | depth | recommended | PASS if, for every role, `frame` is a perspective statement (how this role sees the world) and `serves` is a beneficiary statement (who or what depends on this role's signal), and the two are logically related. FAIL if `serves` is a restatement of `frame`, or if either field is blank or generic ("users", "the team"). |
| C-07 | **Lens quality** — `verify_questions` are actionable and testable (answerable by reading artifacts or running code), and `simplify_rules` are opinionated constraints that reduce scope or remove ambiguity. | depth | recommended | PASS if each role's `verify_questions` list contains at least two questions that reference specific artifacts, behaviors, or measurable outcomes; and `simplify_rules` contains at least one rule that excludes or constrains (not just describes). FAIL if questions are rhetorical or unmeasurable, or if simplify_rules are restatements of scope rather than constraints. |
| C-08 | **Collaborates_with accuracy** — collaboration relationships are architecturally sound and directionally meaningful; if role A lists role B, role B's scope plausibly requires input from or produces output for role A. | correctness | recommended | PASS if every `collaborates_with` entry names another role that exists in the output set, and the pairing reflects a genuine handoff or dependency (not just "everyone works with everyone"). FAIL if `collaborates_with` contains names absent from the role set, or if every role lists every other role. |

---

### Aspirational (10 pts total — raise the bar)

| ID | Text | Category | Weight | Pass Condition |
|----|------|----------|--------|----------------|
| C-09 | **Role differentiation** — each role's `lens.verify_questions` surface concerns that no other role would catch; the set of roles together covers the decision surface without redundant overlap. | depth | aspirational | PASS if a reviewer can identify at least one verify question per role that is unique to that role's frame and would be missed by all other roles. FAIL if two or more roles share the majority of their verify questions or if any role's questions are a strict subset of another's. |
| C-10 | **Narrative completeness signal** — the skill emits a brief registry summary (inline comment, frontmatter, or companion file) stating the area covered, total role count, which stock roles were included, and which domain experts were derived from context — giving the caller a single-glance audit of role coverage. | format | aspirational | PASS if a summary artifact or header comment exists that names the area, counts roles, identifies stock vs. derived roles, and flags any coverage gaps the skill detected. FAIL if no such summary exists and the caller must inspect every file to reconstruct the registry. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Gold | all essential + >= 80 | Production-quality role registry |
| Silver | all essential + 70-79 | Usable but lens/collaboration depth missing |
| Bronze | 4/5 essential + any score | Structural gaps; not ready for downstream skills |
| Fail | < 4 essential pass | Output not useful |

---

## Notes for Evaluators

- **C-01 takes priority**: a role file missing any schema field invalidates C-06, C-07, C-08 for that role. Score what is present; note what is absent.
- **C-02 (devil-advocate)** is non-negotiable for Signal's design philosophy. A generic "critic" role that challenges quality rather than the status quo does not satisfy this criterion.
- **C-05 vs. C-03**: the stock roles (C-03) are always expected; domain expert roles (C-05) prove the skill read context. Evaluate them independently.
- **C-09** requires a comparative read across all role files — do not evaluate per-file in isolation.
