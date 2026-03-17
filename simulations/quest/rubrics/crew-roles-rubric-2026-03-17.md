# crew-roles Rubric — v2

**Namespace**: org
**Skill**: org-roles (crew-roles)
**Last updated**: 2026-03-17
**Status**: active

---

## Summary

**5 essential (C-01..C-05)**
- C-01: All 5 required fields present on every role file (orientation, lens, expertise, scope, collaborates_with)
- C-02: Inertia-advocate always present with adversarial lens
- C-03: Output written to `.craft/roles/{area}/` (downstream contract for org-review/org-committee)
- C-04: Domain specificity — roles derived from input, not generic archetypes
- C-05: Minimum 3 roles

**3 recommended (C-06..C-08)**
- C-06: Lens actionability — verify questions end in `?`, simplify rules start with imperative verb
- C-07: collaborates_with references resolve to actual role files (no orphans)
- C-08: Perspective diversity — 3+ orientation categories (technical, product, strategy, ops)

**5 aspirational (C-09..C-13)**
- C-09: Scope gradient — 2+ distinct scope levels
- C-10: Inertia-advocate lens domain-grounded (specific costs/risks, not generic "why change?")
- C-11: Vocabulary-forced-field — Phase 1 vocabulary list is explicitly referenced by every expertise field
- C-12: Inertia pre-characterization — 3-question sub-section characterizes current system before writing inertia-advocate
- C-13: Registry summary table as self-verification — Role/Orientation/Scope/Collaborates-With table printed after writing

**Formula**: essential 60 + recommended 30 + aspirational 10. Golden = all essential pass + composite >= 80.
With all 5 essential + 2/3 recommended you land exactly at 80. Each aspirational criterion is worth 2 points.

---

## Essential Criteria (60% weight — must all pass for Golden)

### C-01 | All 5 Required Fields Present on Every Role File
- **Weight**: essential
- **Category**: format
- **Text**: Every role file in the output registry must contain all five required fields:
  `orientation`, `lens`, `expertise`, `scope`, and `collaborates_with`. Missing or empty fields
  cause silent failures in org-review and org-committee executions that depend on the registry.
  A role file that contains placeholders ("TBD", "TODO", or empty strings) is treated the same
  as a missing field.
- **Pass condition**: Every role file in `.craft/roles/{area}/` has all 5 fields present and
  non-empty. A single role file with any field missing or placeholder-valued fails this criterion.

### C-02 | Inertia-Advocate Role Always Present
- **Weight**: essential
- **Category**: correctness
- **Text**: The role registry contains exactly one inertia-advocate (or equivalent devil-advocate)
  role whose lens is explicitly oriented toward challenging every proposal with why the status quo
  is sufficient. This role is non-negotiable regardless of domain, team size, or registry scope.
- **Pass condition**: A role file exists whose name or orientation identifies it as the
  inertia-advocate. The role's lens verify questions must include at least one question of the form
  "why is the current approach insufficient?" or equivalent. Absence of this role, or presence of a
  role named "inertia-advocate" but with a lens that does not challenge the proposal, fails this
  criterion.

### C-03 | Output Written to Correct Directory Path
- **Weight**: essential
- **Category**: format
- **Text**: All role files are written to `.craft/roles/{area}/` where `{area}` is derived from the
  input domain. The directory path is the contract that downstream skills (org-review, org-committee)
  use to discover the registry by glob. A registry written to any other path is invisible to those
  skills.
- **Pass condition**: Files exist at `.craft/roles/{area}/*.md`. The `{area}` segment is non-generic
  (not "roles" or "default") and reflects the actual domain input. A single flat file or a file
  written to the wrong path fails this criterion.

### C-04 | Domain Specificity — Roles Derived From Input Context
- **Weight**: essential
- **Category**: correctness
- **Text**: Role names, expertise fields, and lens questions are specific to the input domain,
  product, or codebase — not copy-pasted generic archetypes. The skill is required to analyze the
  input to determine what perspectives are needed. A registry that could apply equally to any
  product signals the analysis was skipped.
- **Pass condition**: At least half of the generated roles (excluding inertia-advocate) have
  expertise or lens fields that reference domain-specific terms, patterns, or concerns traceable
  to the input. A role whose expertise field contains only generic language (e.g., "technical
  depth in software engineering") with no domain anchoring fails this criterion.

### C-05 | Minimum Role Count
- **Weight**: essential
- **Category**: coverage
- **Text**: The registry contains at least 3 distinct role files. A 1- or 2-role registry
  (e.g., only inertia-advocate plus one other) does not provide the multi-perspective coverage
  that the skill is designed to generate.
- **Pass condition**: 3 or more role files exist in the output directory. The inertia-advocate
  counts toward the minimum.

---

## Recommended Criteria (30% weight — improve quality)

### C-06 | Lens Fields Are Actionable
- **Weight**: recommended
- **Category**: depth
- **Text**: Verify questions in each role's lens end with a `?` and test a falsifiable condition
  about the artifact (e.g., "Does the API contract handle partial failures?"). Simplify rules are
  stated as directives starting with an imperative verb (e.g., "Remove X if Y is not used.",
  "Collapse A and B into a single interface."). Vague lens language (e.g., "check quality",
  "consider edge cases") does not guide a downstream org-review execution.
- **Pass condition**: Every role file has at least 1 verify question ending in `?` and at least
  1 simplify rule starting with an imperative verb. A role with lens fields present but written as
  statements instead of questions/directives fails this criterion.

### C-07 | collaborates_with References Are Internally Consistent
- **Weight**: recommended
- **Category**: correctness
- **Text**: Every role name listed in a `collaborates_with` field matches the name of another role
  file in the same registry. Orphan references (referencing roles that don't exist in the output)
  cause silent failures in org-committee simulations that try to seat the referenced roles.
- **Pass condition**: 90% or more of `collaborates_with` entries resolve to an existing role file
  in the output directory. A registry where half the collaborator references are unresolvable fails
  this criterion even if the individual role files are otherwise complete.

### C-08 | Perspective Diversity — At Least 3 Distinct Orientations
- **Weight**: recommended
- **Category**: coverage
- **Text**: The role registry covers perspectives from at least 3 of the following orientation
  categories: technical (architect, engineer, reliability), product (PM, UX, customer), strategy
  (exec, business, go-to-market), and operations (security, compliance, support). A registry
  dominated by a single orientation type produces one-dimensional reviews.
- **Pass condition**: At least 3 orientation categories are represented across the role files.
  A registry of 5 engineers and 1 inertia-advocate with no product or strategy perspective fails
  this criterion.

---

## Aspirational Criteria (10% weight — raise the bar; 2 pts each)

### C-09 | Scope Gradient — At Least 2 Distinct Scope Levels
- **Weight**: aspirational
- **Category**: depth
- **Text**: The `scope` field across role files spans at least 2 distinct levels of organizational
  reach (e.g., component-level, service-level, cross-team, org-wide). A registry where every role
  has the same scope level does not capture the different review distances that the skill is
  designed to assemble. Level distribution should be tuned to the domain scale.
- **Pass condition**: At least 2 distinct scope values appear across all role files. The distinction
  must be meaningful — 2 roles with "component" and "component-level" are the same level. Roles
  with entirely unspecified scope ("all", "general") do not count toward the gradient.

### C-10 | Inertia-Advocate Lens Is Domain-Grounded
- **Weight**: aspirational
- **Category**: depth
- **Text**: The inertia-advocate's lens verify questions reference specific domain costs, migration
  risks, or existing user habits drawn from the input — not generic "why change?" prompts. A
  domain-grounded inertia challenge is more useful to an org-review execution than a template
  challenge that applies to any proposal.
- **Pass condition**: The inertia-advocate's lens contains at least 1 verify question that
  references a domain-specific term, pattern, or artifact from the input (e.g., "Does migrating
  off `{current_system}` outweigh the benefit?" rather than "Is the current approach sufficient?").
  A generic inertia-advocate lens passes C-02 but fails C-10.

### C-11 | Vocabulary-Forced-Field — Phase 1 List Drives Every Expertise Field
- **Weight**: aspirational
- **Category**: depth
- **Text**: The skill execution produces a named vocabulary list from the input in Phase 1
  (system names, patterns, protocols, domain terms) and every expertise field is explicitly
  required to reference at least one term from that list. This structural constraint eliminates
  generic content without repeating "be specific" instructions on every field. Skills that
  instruct specificity without a vocabulary anchor produce correct output under attentive execution
  but regress to generic infill under model drift.
- **Pass condition**: Evidence in the output that a vocabulary list was derived from the input
  (e.g., a Phase 1 extraction block, inline commentary, or cross-references in expertise fields
  to named systems/patterns from the input). At least half of the non-inertia-advocate roles have
  expertise fields containing a term that is traceable to the input document rather than general
  engineering vocabulary. A skill that instructs domain specificity without a Phase 1 vocabulary
  anchor does not satisfy this criterion even if the output happens to be specific.

### C-12 | Inertia Pre-Characterization Before Writing Inertia-Advocate
- **Weight**: aspirational
- **Category**: depth
- **Text**: Before writing the inertia-advocate role file, the skill execution answers at least 3
  characterization questions about the current state: (1) what is the current system or approach
  being displaced?, (2) what are the concrete migration costs or integration risks?, and (3) what
  user habits or workflows depend on the status quo? These answers supply the raw material for
  domain-grounded lens verify questions. Skills that skip this sub-section and write the
  inertia-advocate directly produce verify questions that generalize across proposals rather than
  challenging the specific proposal under review.
- **Pass condition**: The inertia-advocate's lens verify questions reference at least 2 of the 3
  characterization dimensions (current system name, a concrete cost/risk, or a named user habit
  or workflow). A lens that passes C-02 (adversarial orientation present) but only asks generic
  status-quo questions fails this criterion.

### C-13 | Registry Summary Table Printed as Self-Verification Step
- **Weight**: aspirational
- **Category**: correctness
- **Text**: After all role files are written, the skill prints a summary table with columns
  `Role | Orientation | Scope | Collaborates With` listing every role in the registry. This
  forces the execution to traverse all collaborates_with references at output time, surfacing
  orphan references and scope homogeneity before the user reviews the registry. Without this
  step, cross-reference errors and scope uniformity are only discoverable by manual inspection.
- **Pass condition**: A summary table (or equivalent structured listing) appears in the skill
  output after the role files are written. The table covers all generated roles and includes
  at minimum the role name, orientation, scope, and collaborates_with values. An execution that
  writes role files but provides no post-write summary does not satisfy this criterion even if
  the files themselves are correct.

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
```

**Golden threshold**: All 5 essential criteria pass AND composite >= 80.

| Outcome    | Condition |
|------------|-----------|
| Golden     | C-01 through C-05 all pass, composite >= 80 |
| Acceptable | All essential pass, composite >= 70 |
| Needs work | Any essential fails OR composite < 70 |

**Partial credit**: A criterion scored PARTIAL contributes half its point value.

---

## Failure Mode Reference

| Failure | Likely Criterion | Signal |
|---------|-----------------|--------|
| Role file missing orientation or lens | C-01 | Required field absent or "TBD" |
| No inertia-advocate in registry | C-02 | Registry has no devil-advocate role |
| Inertia-advocate present but lens does not challenge status quo | C-02 | Verify questions are constructive, not adversarial |
| Files written to wrong path | C-03 | Output at `roles/` root or `output/` instead of `.craft/roles/{area}/` |
| Generic expertise fields with no domain anchoring | C-04 | "Software engineering depth" with no domain terms |
| Only 1-2 roles generated | C-05 | Inertia-advocate + one other = insufficient registry |
| Verify questions written as statements, not questions | C-06 | No `?` on verify lines |
| Simplify rules are passive or descriptive, not directives | C-06 | "Should consider X" instead of "Remove X" |
| collaborates_with names don't match any role file | C-07 | Orphan reference; downstream committee fails to seat the role |
| All roles are engineers with no product or strategy perspective | C-08 | Single-orientation registry |
| Every role has the same scope value | C-09 | No scope gradient; all component-level or all org-wide |
| Inertia-advocate lens uses generic "why change?" language | C-10 | No domain-specific cost or migration risk referenced |
| Expertise fields contain no terms from Phase 1 vocabulary | C-11 | Domain specificity present but not structurally enforced via vocabulary list |
| Inertia-advocate verify questions generalize across proposals | C-12 | No current system name, migration cost, or user habit referenced |
| No post-write summary table in output | C-13 | Role files written but cross-references and scope not self-verified at execution time |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-17 | Initial rubric — 5E/3R/2A |
| v2 | 2026-03-17 | Add C-11 (vocabulary-forced-field), C-12 (inertia pre-characterization), C-13 (registry summary table) from R1 excellence signals; update formula to aspirational/5; expand failure mode table |
