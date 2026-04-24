---
skill: quest-rubric
skill_target: org-roles
date: 2026-03-16
version: 4
supersedes: org-roles-rubric-v3-2026-03-16.md
---

# Scoring Rubric: org-roles (v4)

Evaluates output from the `org-roles` skill, which generates a typed role registry for a domain by analyzing product, codebase, or spec context and emitting structured role files to `.roles/{area}/`.

**v4 changes**: Added C-18, C-19, C-20 from Round 3 excellence signals. Aspirational denominator updated from 9 to 12. Notes for Evaluators extended.

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
| C-08 | **Collaborates_with accuracy** — collaboration relationships are architecturally sound and directionally meaningful; if role A lists role B, role B's scope plausibly requires input from or produces output for role A. The instruction explicitly prohibits both phantom role references and universalist listing. | correctness | recommended | PASS if every `collaborates_with` entry names another role that exists in the output set, and the pairing reflects a genuine handoff or dependency (not just "everyone works with everyone"). The skill instruction must prohibit (1) phantom roles — names absent from the role set, and (2) universalist listing — "works with everyone" or equivalent. FAIL if either prohibition is absent from the instruction, or if the output contains phantom names or universalist entries. PARTIAL if only one of the two prohibitions is present in the instruction. |

---

### Aspirational (10 pts total — raise the bar)

| ID | Text | Category | Weight | Pass Condition |
|----|------|----------|--------|----------------|
| C-09 | **Role differentiation** — each role's `lens.verify_questions` surface concerns that no other role would catch; the set of roles together covers the decision surface without redundant overlap. | depth | aspirational | PASS if a reviewer can identify at least one verify question per role that is unique to that role's frame and would be missed by all other roles in this registry. FAIL if two or more roles share the majority of their verify questions or if any role's questions are a strict subset of another's. |
| C-10 | **Registry summary completeness** — the skill emits a registry summary artifact (inline comment, frontmatter, or companion file) whose content is fully specified: area name, total role count, stock roles listed by name, domain experts listed by name with their derivation source, and any coverage gaps the skill detected in Step 1. | format | aspirational | PASS if a summary artifact exists that explicitly states all five required fields: area, total count, stock role names, domain expert names with derivation source, detected gaps. FAIL if the summary is a heading-only stub (step named but content undefined), or if any of the five fields is absent and the caller must inspect individual files to reconstruct that information. |
| C-11 | **Context-first derivation ordering** — domain experts are derived from context analysis before stock roles are loaded; the skill's step sequence forces the model to name domain-specific concerns before encountering the PM/Architect/Strategy archetypes. | design | aspirational | PASS if the skill's step sequence places context analysis and domain expert derivation in earlier steps than stock role emission, and the domain expert `frame` fields reference concerns identified in the context analysis step. FAIL if stock roles are defined before domain experts are derived, or if domain expert frames could have been written without reading context (i.e., they are generic archetypes with domain labels applied after the fact). |
| C-12 | **Failure-mode-named field constraints** — schema field instructions name the exact failure mode to avoid, not just the positive requirement; for sibling fields that tend to collapse into restatements (e.g., `frame`/`serves`, `verify_questions`/`simplify_rules`), the instruction explicitly states what not to do. | design | aspirational | PASS if at least two schema field instructions include a negative constraint that names the specific failure mode (e.g., "Must be a different statement from frame, not a paraphrase" rather than "frame and serves must differ"), and the stock role examples demonstrate the constraint by construction rather than instruction alone. FAIL if all field instructions are phrased purely as positive requirements, leaving the failure mode implicit. |
| C-13 | **Explicit step output format** — every skill step that names an output artifact defines the artifact's format fields, required content, and structure explicitly; no step is a heading-only stub. | completeness | aspirational | PASS if every step that produces an artifact (role file, registry summary, or other output) specifies the exact fields, format, and minimum required content for that artifact within the step definition. FAIL if any step names an output (e.g., "Write the registry summary") without defining what that output must contain — heading-only stubs are a structural omission, not a documentation gap. |
| C-14 | **Collaborates_with typed dual-failure prohibition** — the `collaborates_with` field instruction names both failure modes with explicit type labels: FAILURE MODE (type 1) for phantom/non-existent role references; FAILURE MODE (type 2) for universalist listing ("works with everyone"). Typed labeling goes beyond the dual-prohibition required by C-08; it gives the model a recovery path when it detects a violation. | design | aspirational | PASS if the instruction labels both failure modes with distinct type identifiers (numbered, named, or equivalent). PARTIAL if both prohibitions are present (satisfying C-08) but neither carries a type label or named classification. FAIL if either prohibition is absent (C-08 already fails in that case; C-14 inherits the failure). |
| C-15 | **Registry heading-stub failure mode** — the REGISTRY.md step explicitly names the heading-only stub as a FAIL condition: a section header present with no required content beneath it is not a complete registry entry. This forces the model to distinguish structural presence from content completion. | design | aspirational | PASS if the registry step (or its associated output format spec) includes a named FAIL example of the form: "'## Registry Summary' with no content below it fails C-10" or equivalent. PARTIAL if the registry step defines a completion condition (see C-16) that implicitly prevents a heading stub, but does not name the stub failure mode explicitly. FAIL if no heading-stub failure mode is named and no completion condition is defined. |
| C-16 | **Step completion condition** — every output-producing step defines a binary completion test the model can apply before proceeding: not just a format template, but a checkable condition that determines whether the step is done. Format definition (C-13) and completion condition (C-16) are distinct requirements. | completeness | aspirational | PASS if every step that emits an artifact includes a completion condition expressed as a verifiable test (e.g., "all five fields are present", "every derived expert names its source concern", "no field is an empty string"). PARTIAL if at least one output step has a completion condition but others do not. FAIL if no step defines a completion condition and the model must infer doneness from format alone. |
| C-17 | **Worked examples in field constraints** — at least one failure-mode-named constraint (see C-12) includes a worked example or before/after illustration, not just a label. A label names the failure; a worked example shows it. Both together allow the model to calibrate rather than guess at the boundary. | depth | aspirational | PASS if at least three schema field instructions include a concrete worked example (a filled-in bad value, a before/after pair, or a labeled counter-example). PARTIAL if at least one worked example is present but fewer than three fields are illustrated. FAIL if all failure-mode constraints are label-only with no illustrative content. |
| C-18 | **Contrastive worked example pairs** — every field instruction that includes a worked example shows both a failure specimen and a passing specimen in the same field comment; showing only one direction leaves the boundary calibration incomplete. A label names the failure (C-12). A bad example shows it (C-17). A bad-plus-good pair closes the loop by also showing what correct looks like from the same vantage. | depth | aspirational | PASS if at least two schema field instructions include a WORKED EXAMPLE (bad) and WORKED EXAMPLE (good) pair in the same field comment — both directions in the same location. PARTIAL if at least one field has a contrastive pair but fewer than two fields have both directions. FAIL if all worked examples (even those satisfying C-17) show only one direction. |
| C-19 | **Enumerated multi-item completion gate** — each output-producing step's completion condition (C-16 level) is expressed as a numbered or bulleted checklist with at least three independently verifiable items, not a single compound predicate; a multi-item gate exposes individual failure points that a single "all conditions met" test would collapse and hide. | completeness | aspirational | PASS if every output-producing step has a completion gate listing at least three independently verifiable items (e.g., Phase 2 gate: 1) all four stock role names present, 2) inertia-advocate has a status-quo question, 3) no domain-expert names appear in stock role frames, 4) each role has a distinct frame). PARTIAL if at least one step has a multi-item gate (three or more items) but other output steps have only a single-condition test or no condition. FAIL if no step has a multi-item gate. |
| C-20 | **Domain-specific registry extension** — the registry summary template explicitly designates at least one field beyond the required five as a domain-specific extension slot, and that field is grounded in the context analysis step; the extension is named in the step output spec before any role is written, not added ad hoc to the final artifact. Registry extensibility is evidence that the skill design reached beyond the required baseline into the domain it was asked to model. | design | aspirational | PASS if the registry step's output template includes at least one named extension field that is (a) distinct from the five required fields and (b) references a concern identified in the context/domain analysis step. FAIL if the registry template contains only the five required fields with no extension mechanism, or if any additional field is not grounded in an earlier context analysis step. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 12 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Gold | all essential + >= 80 | Production-quality role registry |
| Silver | all essential + 70-79 | Usable but lens/collaboration depth missing |
| Bronze | 4/5 essential + any score | Structural gaps; not ready for downstream skills |
| Fail | < 4 essential pass | Output not useful |

---

## What changed from v3

| Delta | Detail |
|-------|--------|
| +C-18 | **Contrastive worked example pairs** (from V-01 C-17 PASS: "each has WORKED EXAMPLE (bad) and WORKED EXAMPLE (good)") — C-17 requires any worked example; C-18 requires that each illustrated field show both the failure form and the passing form in the same comment; PARTIAL if one or more fields have a pair but fewer than two fields do; FAIL if all examples show only one direction |
| +C-19 | **Enumerated multi-item completion gate** (from V-02 C-16 PASS: "GATE checklist at every phase — Phase 1 (4 conditions), Phase 2 (4), Phase 3 (3), Phase 4 (5), Phase 5 (6)") — C-16 requires any completion condition; C-19 requires a numbered/bulleted checklist with at least three independently verifiable items per step; PARTIAL if at least one step has a multi-item gate but others do not; FAIL if no step has a multi-item gate |
| +C-20 | **Domain-specific registry extension** (from V-03 C-10 PASS: "adds 'Inertia surface' field beyond the five required — derived from domain analysis") — C-10 tests baseline completeness (five required fields); C-20 tests whether the template reaches beyond the baseline with at least one domain-grounded extension field defined before role writing begins; FAIL if no extension field exists or if it is not grounded in Step 1 context analysis |
| Formula | Aspirational denominator updated `/9` → `/12` to account for twelve aspirational criteria (C-09 through C-20) |

## Scoring formula impact on Round 3 scores

Round 3 variates scored against v3 with aspirational /9. Against v4 (/12), new criteria (C-18 through C-20) are evaluated for the first time. Approximate v4 retroactive scores:

```
V-01: (5/5)*60 + (3/3)*30 + (9.5/12)*10  =  60.0 + 30.0 + 7.92  =  97.92  GOLDEN
      [C-16 PARTIAL (0.5); C-18 PASS: paired bad/good in three fields; C-19 FAIL: no multi-item gate; C-20 FAIL: no extension field]

V-02: (5/5)*60 + (3/3)*30 + (9.0/12)*10  =  60.0 + 30.0 + 7.50  =  97.50  GOLDEN
      [C-17 FAIL; C-18 FAIL: no worked examples at all; C-19 PASS: 4-6 item gate at every phase; C-20 FAIL: no extension field]

V-03: (5/5)*60 + (3/3)*30 + (9.0/12)*10  =  60.0 + 30.0 + 7.50  =  97.50  GOLDEN
      [C-16 PARTIAL (0.5); C-17 FAIL; C-18 FAIL; C-19 FAIL; C-20 PASS: "Inertia surface" field grounded in Step 1]

V-04: (5/5)*60 + (3/3)*30 + (approx 10.5/12)*10  =  60.0 + 30.0 + 8.75  =  98.75  GOLDEN
      [C-16 PASS (full gate at every phase per v3 retroactive); C-17 PASS; C-18 PASS (paired bad/good); C-19 PASS (multi-item gates); C-20 unknown — scorecard cut at C-09]
```

V-04 retains highest probable score. All four variates remain GOLDEN. The ceiling rises from /9 to /12; the GOLDEN gate (all essential pass + composite >= 80) does not move.

---

## Notes for Evaluators

- **C-01 takes priority**: a role file missing any schema field invalidates C-06, C-07, C-08 for that role. Score what is present; note what is absent.
- **C-01/C-07 naming risk**: the schema must use exact field names `verify_questions` and `simplify_rules` (not `verify`/`simplify`). Downstream skills (org-review, org-chart) read role files by exact field name. A schema that uses shortened names passes manual review but fails integration.
- **C-02 (devil-advocate)** is non-negotiable for Signal's design philosophy. A generic "critic" role that challenges quality rather than the status quo does not satisfy this criterion.
- **C-05 vs. C-03**: the stock roles (C-03) are always expected; domain expert roles (C-05) prove the skill read context. Evaluate them independently.
- **C-08 vs. C-14**: C-08 requires that both prohibitions exist in the instruction. C-14 requires that they be explicitly typed with labels. A variate can PASS C-08 (both present) and PARTIAL C-14 (not typed). Evaluate C-08 first; if C-08 fails, C-14 inherits the failure.
- **C-09** requires a comparative read across all role files — do not evaluate per-file in isolation.
- **C-10 vs. C-13**: C-10 tests whether the registry summary *content* is complete (all five fields present). C-13 tests whether *every step* that names an output defines its format. A skill can fail C-13 (heading-only stub in Step 5) while also failing C-10 (no summary content). Fix C-13 first — it is the structural cause of C-10 failures.
- **C-10 vs. C-15**: C-10 tests content completeness (five fields). C-15 tests whether the stub failure mode is named as a FAIL condition. A variate can PASS C-10 (all five fields present) and still FAIL C-15 (no explicit stub-failure-mode instruction). Evaluate independently.
- **C-10 vs. C-20**: C-10 tests the required five fields. C-20 tests for domain-specific extension beyond those five. A variate can PASS C-10 (all five present) and FAIL C-20 (no extension field). A variate cannot PASS C-20 while failing C-10 — extension presupposes the baseline.
- **C-11 (context-first ordering)**: evaluate by reading the step sequence, not the output. If stock roles appear in Step 1 and domain experts in Step 3, C-11 fails regardless of how domain-specific the output looks.
- **C-12 (failure-mode-named constraints)**: look for negative constructions in schema field comments — "not a paraphrase", "not a description", "not a generic archetype". A schema that only states the positive ("frame is an epistemic viewpoint") is weaker than one that names the failure ("frame must not restate serves").
- **C-13 vs. C-16**: C-13 is about output *format* (field names, structural shape). C-16 is about *completion condition* (a binary test the model applies before proceeding). A step can define its output format (PASS C-13) without defining when that output is considered done (FAIL C-16). Both are required for the strongest skill designs.
- **C-16 vs. C-19**: C-16 requires any completion condition per step. C-19 requires that condition to be a multi-item checklist (three or more independent items). A step with a single condition ("all five fields are present") PASSES C-16 and FAILS C-19. Evaluate C-16 first; if C-16 fails, C-19 inherits the failure.
- **C-17 vs. C-18**: C-17 requires at least one worked example per field comment (bad value, before/after, or counter-example). C-18 requires that at least two of those field comments show both a bad AND a good example — both directions in the same location. A field comment with only "FAILURE: task list — e.g., 'write tests, review PRs'" is C-17 level. The same comment that also adds "PASS: epistemic lens — e.g., 'Sees every proposal through the lens of operational cost'" is C-18 level. Evaluate C-17 first; a variate that fails C-17 cannot PASS C-18.
- **C-18 (contrastive pairs)**: count field comments that contain both directions, not fields that mention failure AND separate fields that mention success. Both directions must appear in the same field comment to constitute a contrastive pair.
- **C-19 (multi-item gate)**: count independently verifiable items per gate — items that could each individually fail while others pass. A gate that lists "1) output written, 2) output complete" is not multi-item in the C-19 sense; both items test the same condition from different angles. A gate where each item references a distinct schema element or constraint is multi-item.
- **C-20 (domain-specific extension)**: verify that the extension field is named in the step output spec before the role files are written — not discovered by reading the final artifact. An "Inertia surface" field that appears only in the finished REGISTRY.md does not satisfy C-20; it must appear in the step's output template so the model knows to populate it.
