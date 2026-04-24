---
skill: quest-rubric
skill_target: org-roles
date: 2026-03-16
version: 2
supersedes: org-roles-rubric-v1-2026-03-15.md
---

# Scoring Rubric: org-roles (v2)

Evaluates output from the `org-roles` skill, which generates a typed role registry for a domain by analyzing product, codebase, or spec context and emitting structured role files to `.roles/{area}/`.

**v2 changes**: Added C-11, C-12, C-13 from Round 1 excellence signals E-1, E-2, E-3. Aspirational denominator updated from 2 to 5. Notes for Evaluators extended.

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
| C-10 | **Registry summary completeness** — the skill emits a registry summary artifact (inline comment, frontmatter, or companion file) whose content is fully specified: area name, total role count, stock roles listed by name, domain experts listed by name with their derivation source, and any coverage gaps the skill detected in Step 1. | format | aspirational | PASS if a summary artifact exists that explicitly states all five required fields: area, total count, stock role names, domain expert names with derivation source, detected gaps. FAIL if the summary is a heading-only stub (step named but content undefined), or if any of the five fields is absent and the caller must inspect individual files to reconstruct that information. |
| C-11 | **Context-first derivation ordering** — domain experts are derived from context analysis before stock roles are loaded; the skill's step sequence forces the model to name domain-specific concerns before encountering the PM/Architect/Strategy archetypes. | design | aspirational | PASS if the skill's step sequence places context analysis and domain expert derivation in earlier steps than stock role emission, and the domain expert `frame` fields reference concerns identified in the context analysis step. FAIL if stock roles are defined before domain experts are derived, or if domain expert frames could have been written without reading context (i.e., they are generic archetypes with domain labels applied after the fact). |
| C-12 | **Failure-mode-named field constraints** — schema field instructions name the exact failure mode to avoid, not just the positive requirement; for sibling fields that tend to collapse into restatements (e.g., `frame`/`serves`, `verify_questions`/`simplify_rules`), the instruction explicitly states what not to do. | design | aspirational | PASS if at least two schema field instructions include a negative constraint that names the specific failure mode (e.g., "Must be a different statement from frame, not a paraphrase" rather than "frame and serves must differ"), and the stock role examples demonstrate the constraint by construction rather than instruction alone. FAIL if all field instructions are phrased purely as positive requirements, leaving the failure mode implicit. |
| C-13 | **Explicit step output format** — every skill step that names an output artifact defines the artifact's format fields, required content, and structure explicitly; no step is a heading-only stub. | completeness | aspirational | PASS if every step that produces an artifact (role file, registry summary, or other output) specifies the exact fields, format, and minimum required content for that artifact within the step definition. FAIL if any step names an output (e.g., "Write the registry summary") without defining what that output must contain — heading-only stubs are a structural omission, not a documentation gap. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
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
- **C-01/C-07 naming risk**: the schema must use exact field names `verify_questions` and `simplify_rules` (not `verify`/`simplify`). Downstream skills (org-review, org-chart) read role files by exact field name. A schema that uses shortened names passes manual review but fails integration.
- **C-02 (devil-advocate)** is non-negotiable for Signal's design philosophy. A generic "critic" role that challenges quality rather than the status quo does not satisfy this criterion.
- **C-05 vs. C-03**: the stock roles (C-03) are always expected; domain expert roles (C-05) prove the skill read context. Evaluate them independently.
- **C-09** requires a comparative read across all role files — do not evaluate per-file in isolation.
- **C-10 vs. C-13**: C-10 tests whether the registry summary *content* is complete (all five fields present). C-13 tests whether *every step* that names an output defines its format. A skill can fail C-13 (heading-only stub in Step 5) while also failing C-10 (no summary content). Both criteria fail independently; fix C-13 first — it is the structural cause of C-10 failures.
- **C-11 (context-first ordering)**: evaluate by reading the step sequence, not the output. If stock roles appear in Step 1 and domain experts in Step 3, C-11 fails regardless of how domain-specific the output looks. The ordering constraint prevents template anchoring at generation time, not at evaluation time.
- **C-12 (failure-mode-named constraints)**: look for negative constructions in schema field comments — "not a paraphrase", "not a description", "not a generic archetype". A schema that only states the positive ("frame is an epistemic viewpoint") is weaker than one that names the failure ("frame must not restate serves"). Evaluate the schema's internal instructions, not just whether the output happens to comply.
