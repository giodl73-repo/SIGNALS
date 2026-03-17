---
skill: quest-variate
skill_target: crew-roles
date: 2026-03-17
round: 2
rubric: crew-roles-rubric-v2-2026-03-17.md
---

# crew-roles — Variate R2

5 complete prompt body variations for the `crew-roles` skill.
Single-axis first (V-01 through V-03), then two-axis combinations (V-04, V-05).

Round 2 targets the three new aspirational criteria introduced in rubric v2:
- **C-11** Vocabulary-Forced-Field: Phase 1 vocabulary list anchors every expertise field
- **C-12** Inertia Pre-Characterization: 3-question sub-section before writing the inertia-advocate
- **C-13** Registry Summary Table: Role/Orientation/Scope/Collaborates-With table after writing

Rubric reminder (v2):
- Essential (must-pass): C-01 all 5 fields present, C-02 inertia-advocate, C-03 correct path, C-04 domain specificity, C-05 min 3 roles
- Recommended: C-06 lens actionability, C-07 collaborates_with resolves, C-08 perspective diversity
- Aspirational: C-09 scope gradient, C-10 inertia lens domain-grounded, C-11 vocabulary-forced-field, C-12 inertia pre-characterization, C-13 registry summary table

---

## V-01

**Axis**: Vocabulary-Forced-Field (single axis — C-11 target)
**Hypothesis**: Requiring a named vocabulary extraction in Phase 1, and structurally mandating
that every expertise field reference at least one term from it, prevents generic role output
without repeating "be specific" instructions on every field. C-04 and C-11 become structural
properties rather than luck-dependent outcomes.

---

You are running `/org-roles`.

Generate a typed role registry for the provided domain. Write role files to `.craft/roles/{area}/`.

---

### Phase 1 — Domain Vocabulary Extraction

Before writing any roles, extract a vocabulary list from the input.

Read the input (product description, codebase, spec, or domain name). Extract:

- **System names**: named products, services, modules, APIs, data stores in the input
- **Domain patterns**: design patterns, workflows, protocols, or architectural decisions named
- **Key nouns**: terms that are specific to this domain and would not appear in a generic product

Output this section first:

```
## Domain Vocabulary

Systems: [comma-separated list]
Patterns: [comma-separated list]
Key terms: [comma-separated list]
```

This vocabulary list is the anchor for all expertise fields. Every expertise field written in
Phase 3 must reference at least one term from this list. If a term from the list does not
appear in any expertise field, add it to the role most likely to care about it.

---

### Phase 2 — Role Selection

From the vocabulary and input context, determine what expert perspectives are needed.

**Stock roles** (always included unless input context makes them irrelevant):
- Product Manager — feature value and user adoption
- Architect — system design and integration seams
- Inertia Advocate — status quo defense (generated separately in Phase 3b)

**Domain roles** (auto-selected from vocabulary):
Scan the vocabulary list. For each major system or pattern named, ask: is there a perspective
that cannot be covered by PM or Architect? If yes, add a domain expert role.

Minimum: 3 roles including inertia-advocate.

List the selected roles and one justification line each before writing files.

---

### Phase 3a — Write Domain Role Files

For each non-inertia role, write `.craft/roles/{area}/{role-name}.md`:

```markdown
# {Role Name}

## orientation
frame: {one sentence: what question does this role answer?}
serves: {who benefits from this perspective — e.g., "team shipping the feature", "downstream consumers"}

## lens
verify:
  - {question ending in ?}
  - {question ending in ?}
simplify:
  - {imperative verb phrase — e.g., "Remove X if Y is not used"}
  - {imperative verb phrase}

## expertise
depth: {senior | staff | principal}
relevance: {one sentence referencing at least one term from the Domain Vocabulary list}

## scope
{component | service | cross-team | org-wide}

## collaborates_with
- {role-name}
```

Constraint: `expertise.relevance` must contain at least one term from the Phase 1 vocabulary
list. If you cannot write a relevance sentence that references a vocabulary term, the role is
too generic — refine the role name to a more specific perspective.

---

### Phase 3b — Inertia Advocate

Before writing the inertia-advocate file, answer these three questions explicitly:

1. **Current system**: What is the system or approach this domain is replacing or extending?
2. **Migration costs**: What are the concrete costs or risks of moving away from the current system?
3. **User habits**: What workflows or habits does the current system support that users depend on?

Write a `## Inertia Pre-Characterization` block with these three answers before writing the file.

Then write `.craft/roles/{area}/inertia-advocate.md`:

- `orientation.frame`: "Challenge every proposal with why the current approach is sufficient."
- `lens.verify`: At least 2 questions that reference specifics from the pre-characterization block
  (current system name, a named cost, or a named user habit). Generic "why change?" questions
  do not satisfy this constraint.
- `lens.simplify`: Rules for removing scope creep or unvalidated assumptions from proposals
- `expertise.relevance`: Reference to the current system named in pre-characterization
- `scope`: cross-team (the status quo spans the whole domain by default)
- `collaborates_with`: PM (inertia challenge is a product-level question)

---

### Phase 4 — AMEND

> **AMEND**
> - Add a domain role: `/org-roles {domain} --amend add:{role-name}` *(derived from input vocabulary)*
> - Adjust level distribution: `/org-roles {domain} --amend levels:{senior|staff|principal}`
> - Replace a role: `/org-roles {domain} --amend replace:{old}:{new}`

---

---

## V-02

**Axis**: Inertia framing (single axis — C-12 target)
**Hypothesis**: An explicit 3-question inertia pre-characterization block — current system name,
migration costs, user habits — forces verify questions to reference concrete status-quo dimensions
rather than generalizing across proposals. C-10 and C-12 become structural outcomes because the
raw material (named system, named costs, named habits) is extracted before the verify questions
are written.

---

You are running `/org-roles`.

Generate a typed role registry for the provided domain. Write role files to `.craft/roles/{area}/`.
All 5 required fields must be present on every role file: orientation, lens, expertise, scope,
collaborates_with.

---

### Step 1 — Inertia Pre-Characterization

Before writing any role files, run this sub-section. The output is required and gates the
inertia-advocate role.

Answer these three questions about the current state of the domain:

**Q1: Current system**
What is the named system, tool, process, or approach that this domain uses today?
If the input does not name one, derive it from context (e.g., manual workflow, existing service,
competing tool). Write it as a proper noun: "the current approach is [X]."

**Q2: Migration costs**
What are the concrete costs or risks of moving from [X] to the proposed approach?
Name at least one: integration work, retraining effort, data migration risk, pipeline disruption,
team ramp time. Vague answers ("it's risky") do not satisfy this question.

**Q3: User habits**
What workflows, automations, or daily habits depend on [X]?
Name at least one observable behavior: "users currently do [Y] using [X] which would change."

Write the block before any role files:

```
## Inertia Pre-Characterization

Current system: [name — not "existing approach"]
Migration cost: [named cost or risk]
User habit: [named workflow or behavior]
```

This block supplies the raw material for the inertia-advocate's verify questions.
At least 2 of the 3 dimensions must appear in the inertia-advocate's lens.

---

### Step 2 — Role Selection

Determine what expert perspectives the domain requires.

**Always include**:
- Product Manager (feature value, user adoption)
- Inertia Advocate (status quo defense)
- One technical perspective derived from the domain (architect, SRE, security, data — whichever
  is most relevant given the input)

**Add domain roles** if the input introduces systems, protocols, or user populations that PM
and Architect cannot adequately represent.

List selected roles and one justification line each. Minimum 3 roles.

---

### Step 3 — Write Role Files

For each role, write `.craft/roles/{area}/{role-name}.md` using this structure:

```markdown
# {Role Name}

## orientation
frame: {one sentence: what question does this role answer?}
serves: {who benefits from this perspective}

## lens
verify:
  - {question ending in ?}
  - {question ending in ?}
simplify:
  - {Imperative verb phrase}
  - {Imperative verb phrase}

## expertise
depth: {senior | staff | principal}
relevance: {one sentence specific to this domain — no generic engineering language}

## scope
{component | service | cross-team | org-wide}

## collaborates_with
- {role-name matching another file in this registry}
```

**Inertia-advocate constraint**: The `lens.verify` section must contain at least 2 questions
that reference specifics from the Inertia Pre-Characterization block:
- At least one question must name the current system from Q1
- The remaining questions must reference a named cost (Q2) or a named user habit (Q3)

A question like "Is the current approach sufficient?" fails this constraint.
A question like "Does migrating off [current system] cost more than [named cost] in pipeline
rewrite time?" passes.

---

### Step 4 — AMEND

> **AMEND**
> - Add a role: `/org-roles {domain} --amend add:{role-name}`
> - Adjust scope distribution: `/org-roles {domain} --amend scope:{level}`
> - Re-characterize inertia: `/org-roles {domain} --amend reinertia` *(re-runs Step 1 with more context)*

---

---

## V-03

**Axis**: Output format (single axis — C-13 target)
**Hypothesis**: A mandatory Registry Summary Table printed after all role files are written forces
the execution to traverse all collaborates_with references and scope values at output time,
surfacing orphan references and scope homogeneity before the user reviews the registry.
C-07 and C-13 become verifiable at a glance; C-09 (scope gradient) also improves because the
table makes scope uniformity immediately visible.

---

You are running `/org-roles`.

Generate a typed role registry for the provided domain. Write role files to `.craft/roles/{area}/`.

---

### Step 1 — Context Analysis

Read the input. Determine:
- Domain name (becomes `{area}` in the output path)
- What types of expertise the domain requires
- What system or approach the domain currently uses (needed for inertia-advocate)

---

### Step 2 — Role Selection

Determine which roles to generate.

**Stock roles** (always included):
- Product Manager — adoption, user value
- Architect — system design and integration
- Inertia Advocate — status quo challenge

**Domain roles** (auto-selected from input):
For each major technical or operational concern in the input that cannot be covered by PM or
Architect, add a specialist role.

List all selected roles and a one-line rationale per role. Minimum 3 roles total.

---

### Step 3 — Write Role Files

For each role, write `.craft/roles/{area}/{role-name}.md`:

```markdown
# {Role Name}

## orientation
frame: {one sentence: what question does this role answer?}
serves: {who benefits}

## lens
verify:
  - {question ending in ?}
  - {question ending in ?}
simplify:
  - {Imperative: Remove X if...}
  - {Imperative: Collapse/Defer/Move X...}

## expertise
depth: {senior | staff | principal}
relevance: {one sentence specific to this domain and input context}

## scope
{component | service | cross-team | org-wide}

## collaborates_with
- {role-name}
```

**Inertia-advocate rules**:
- `orientation.frame`: must include the phrase "challenge" or "status quo"
- `lens.verify`: must include at least one question of the form "why is [current approach] insufficient?"
  where [current approach] is specific to the domain (not generic)
- `scope`: cross-team (the inertia challenge is not component-scoped)

**Lens rules (all roles)**:
- Every verify item ends in `?`
- Every simplify item starts with an imperative verb (Remove, Collapse, Defer, Merge, Move)

---

### Step 4 — Registry Summary Table

After writing all role files, produce this table:

```
## Registry Summary

| Role | Orientation (frame excerpt) | Scope | Collaborates With |
|------|-----------------------------|-------|-------------------|
| {role-name} | {first 8 words of frame} | {scope value} | {comma-separated names} |
```

Include every role file written. This table is the self-verification step.

**After the table, check**:
1. **Orphan references**: Do all names in "Collaborates With" match a Role column entry?
   If not, mark them: `{name} [UNRESOLVED]` and add the missing role or remove the reference.
2. **Scope gradient**: Do at least 2 distinct values appear in the Scope column?
   If all roles have the same scope, revise 1–2 roles to reflect their actual organizational reach.

If either check reveals an issue, fix it before delivering the output. State what you fixed.

---

### Step 5 — AMEND

> **AMEND**
> - Add a role: `/org-roles {domain} --amend add:{role-name}` *(table re-runs after addition)*
> - Adjust levels: `/org-roles {domain} --amend levels`
> - Expand registry: `/org-roles {domain} --amend expand` *(adds 2–3 more domain specialists)*

---

---

## V-04

**Axes**: Vocabulary-Forced-Field + Inertia Pre-Characterization (C-11 + C-12 combination)
**Hypothesis**: Combining vocabulary extraction with inertia pre-characterization creates a
mutually reinforcing structure. The vocabulary list surfaces the concrete current system that
the inertia-advocate must challenge, and the inertia questions ensure the vocabulary's highest-
signal terms (the current system name and its costs) make it into the inertia verify questions.
Neither can drift to generic language because each is anchored to the other's output.

---

You are running `/org-roles`.

Generate a typed role registry for the provided domain. Write role files to `.craft/roles/{area}/`.

This skill runs in 4 phases. Phases 1 and 2 must complete before any role files are written.

---

### Phase 1 — Domain Vocabulary

Read the input. Extract and name:

```
## Domain Vocabulary

Systems: [named services, tools, platforms, stores — proper nouns from the input]
Patterns: [named architectural patterns, workflows, protocols from the input]
Key terms: [domain-specific nouns that distinguish this domain from generic software]
```

This vocabulary list governs all expertise fields in Phase 3. Every `expertise.relevance` field
must reference at least one term from Systems, Patterns, or Key terms.

If the input is sparse (fewer than 3 terms across all categories), expand by inference:
"Input names [X]; the domain likely also involves [Y, Z] based on [X]'s known architecture."
Label inferred terms `[inferred]`. Inferred terms satisfy the vocabulary constraint.

---

### Phase 2 — Inertia Pre-Characterization

Before writing the inertia-advocate, answer these three questions using the vocabulary from Phase 1:

**Q1: Current system**
What system, tool, or workflow from the Phase 1 vocabulary list represents the status quo?
If nothing in the vocabulary is a "current" thing being displaced, ask: what does the team use
*instead* of the proposed domain approach? Write: "Current system: [name from vocabulary]."

**Q2: Migration cost**
What is the concrete cost of moving away from the current system?
Reference at least one vocabulary term in your answer.
Write: "Migration cost: [named cost or risk referencing a vocabulary term]."

**Q3: User habit**
What daily workflow or habit depends on the current system?
Write: "User habit: [named workflow or observable behavior]."

```
## Inertia Pre-Characterization

Current system: [name]
Migration cost: [named cost referencing vocabulary term]
User habit: [named behavior]
```

---

### Phase 3 — Write Role Files

**For each non-inertia role**, write `.craft/roles/{area}/{role-name}.md`:

```markdown
# {Role Name}

## orientation
frame: {one sentence: what question does this role answer?}
serves: {who benefits}

## lens
verify:
  - {question ending in ?}
  - {question ending in ?}
simplify:
  - {Imperative verb phrase}
  - {Imperative verb phrase}

## expertise
depth: {senior | staff | principal}
relevance: {sentence containing at least one Phase 1 vocabulary term}

## scope
{component | service | cross-team | org-wide}

## collaborates_with
- {role-name}
```

**Vocabulary constraint**: Each `expertise.relevance` must contain a term from the Phase 1
vocabulary list. If you cannot write a specific relevance sentence, the role is under-scoped —
rename it to a more specific perspective that vocabulary can anchor.

**For the inertia-advocate**, write `.craft/roles/{area}/inertia-advocate.md`:

- `orientation.frame`: "Challenge every proposal with why [current system from Phase 2] is sufficient."
  The current system name must appear in the frame.
- `lens.verify`: 3 questions. Each must reference at least one of:
  - The current system name (from Phase 2, Q1)
  - The migration cost (from Phase 2, Q2)
  - The user habit (from Phase 2, Q3)
  Generic questions ("Is the current approach sufficient?") fail this constraint.
- `expertise.relevance`: Must reference the current system from Phase 2 plus at least one
  vocabulary term from Phase 1.
- `scope`: cross-team
- `collaborates_with`: PM (the status quo argument is a product decision)

**Selection**: Stock roles (PM, Architect, Inertia Advocate) plus domain roles derived from
Phase 1 vocabulary. Minimum 3 roles total.

---

### Phase 4 — AMEND

> **AMEND**
> - Add a domain role: `/org-roles {domain} --amend add:{role-name}`
> - Refresh vocabulary: `/org-roles {domain} --amend vocabulary` *(re-runs Phase 1 with additional input)*
> - Re-characterize inertia: `/org-roles {domain} --amend reinertia` *(re-runs Phase 2)*
> - Adjust level distribution: `/org-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-05

**Axes**: Vocabulary-Forced-Field + Inertia Pre-Characterization + Registry Summary Table
         (C-11 + C-12 + C-13 — full integration)
**Hypothesis**: All three new aspirational criteria addressed structurally in a phase-gated
execution: Phase 1 vocabulary extraction anchors every expertise field (C-11); Phase 2
inertia pre-characterization grounds the status-quo challenge (C-12); Phase 4 registry
summary table self-verifies cross-references and scope diversity (C-13). The phases are
sequenced so each feeds the next — vocabulary supplies inertia characterization, and the
summary table forces a post-write traversal that catches anything the earlier phases missed.

---

You are running `/org-roles`.

Generate a typed role registry for the provided domain. Write role files to `.craft/roles/{area}/`.

**4 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

## PHASE 1 — VOCABULARY EXTRACTION

**Entry**: domain input provided
**Exit condition**: vocabulary list is written and contains at least 3 distinct terms

Read the input. Extract:

```
## Domain Vocabulary

Systems: [named products, services, modules, APIs, data stores]
Patterns: [architectural patterns, protocols, workflows, design decisions]
Key terms: [domain-specific nouns traceable to the input]
```

If the input has fewer than 3 terms across categories, extend by inference.
Label inferred terms `[inferred]` and state the basis: "inferred from [X]."

**Exit condition met**: vocabulary table present with 3+ terms.

---

## PHASE 2 — INERTIA PRE-CHARACTERIZATION

**Entry**: Phase 1 complete
**Exit condition**: all 3 characterization answers written and at least one vocabulary term
  appears in each answer

Using the Phase 1 vocabulary, answer:

**Q1 — Current system**
What named system or approach from the vocabulary does the domain currently rely on?
If none is explicitly named, state the closest current-state equivalent.
Answer must be a proper noun or named entity, not "the existing solution."

**Q2 — Migration cost**
What is the concrete cost or risk of replacing or extending the current system?
Reference at least one vocabulary term (system name, pattern, or key term).
"It's risky" does not satisfy this question. Name the risk category and its source.

**Q3 — User habit**
What observable workflow or daily behavior depends on the current system?
Name the behavior and the system it depends on.

```
## Inertia Pre-Characterization

Current system: [named entity]
Migration cost: [named cost or risk, referencing vocabulary term]
User habit: [named workflow or observable behavior]
```

**Exit condition met**: all 3 answers written and at least one vocabulary term present in each.

---

## PHASE 3 — WRITE ROLE FILES

**Entry**: Phases 1 and 2 complete
**Exit condition**: all role files written with all 5 fields present and vocabulary/inertia
  constraints satisfied

**Role selection**: Determine which perspectives the domain needs.

Stock roles (always included):
- `pm` — Product Manager: feature value, adoption, user experience
- `architect` — System Architect: integration seams, technical boundaries, non-functional requirements
- `inertia-advocate` — Status Quo Challenger: generated last, after all domain roles

Domain roles: For each major system or pattern in the Phase 1 vocabulary that PM and Architect
cannot adequately represent, add a specialist. Minimum 1 domain role beyond stock.

List selected roles and one-line rationale before writing files.

---

**For each non-inertia role**, write `.craft/roles/{area}/{role-name}.md`:

```markdown
# {Role Name}

## orientation
frame: {one sentence: what question does this role answer?}
serves: {who benefits from this perspective}

## lens
verify:
  - {question ending in ?}
  - {question ending in ?}
simplify:
  - {Imperative verb — Remove / Collapse / Defer / Merge / Move}
  - {Imperative verb — Remove / Collapse / Defer / Merge / Move}

## expertise
depth: {senior | staff | principal}
relevance: {sentence containing at least one Phase 1 vocabulary term}

## scope
{component | service | cross-team | org-wide}

## collaborates_with
- {role-name matching another file in this registry}
```

**Vocabulary constraint (C-11)**: Each `expertise.relevance` field must reference at least one
term from Phase 1 vocabulary. If a relevance sentence contains no vocabulary terms, it is
insufficiently specific — revise the role name or relevance before writing the file.

---

**For the inertia-advocate**, write `.craft/roles/{area}/inertia-advocate.md`:

Use the Phase 2 characterization as raw material:

- `orientation.frame`: "Challenge every proposal with evidence that [current system from Q1]
  remains sufficient given [migration cost from Q2]." The current system name must appear verbatim.
- `lens.verify`: 3 questions. Distribution constraint:
  - At least 1 question must name the current system (Q1) directly
  - At least 1 question must reference the named migration cost or risk (Q2)
  - At least 1 question must reference the user habit or dependent workflow (Q3)
  Generic questions ("Is the current approach insufficient?") fail even if the role otherwise passes C-02.
- `lens.simplify`: At least 2 imperative rules for eliminating scope that cannot survive inertia scrutiny
- `expertise.relevance`: Must reference the current system (Q1) and at least one Phase 1 vocabulary term
- `scope`: cross-team
- `collaborates_with`: pm

**Exit condition met**: all role files written; every `expertise.relevance` field contains a
vocabulary term; inertia-advocate's lens.verify references Q1, Q2, and Q3 dimensions.

---

## PHASE 4 — REGISTRY SUMMARY TABLE

**Entry**: Phase 3 complete
**Exit condition**: summary table written, orphan check passed, scope gradient confirmed

After writing all role files, produce:

```
## Registry Summary

| Role | Orientation Frame (excerpt) | Scope | Collaborates With |
|------|-----------------------------|-------|-------------------|
```

One row per role file. The `Role` column must match the file stem exactly.
`Collaborates With` lists every name from the role's `collaborates_with` field.

**Self-verification checks** (run after producing the table):

**Check 1 — Orphan references**
For every name in the `Collaborates With` column: does a matching entry exist in the `Role`
column? Mark any that do not: `{name} [UNRESOLVED]`. For each unresolved entry, either:
- Add the missing role to the registry, or
- Remove the reference from the role file that cites it
State what action was taken.

**Check 2 — Scope gradient**
Does the `Scope` column contain at least 2 distinct values?
If all rows show the same scope value, identify 1–2 roles whose actual organizational reach
differs from that value and revise their scope fields. State what was changed.

**Exit condition met**: table written, no `[UNRESOLVED]` entries remain, at least 2 distinct
scope values appear.

---

## AMEND

> **AMEND**
> - Add a domain role: `/org-roles {domain} --amend add:{role-name}` *(vocabulary constraint applies; table re-runs)*
> - Refresh vocabulary: `/org-roles {domain} --amend vocabulary` *(re-runs Phase 1 with additional input)*
> - Re-characterize inertia: `/org-roles {domain} --amend reinertia` *(re-runs Phase 2, rewrites inertia-advocate)*
> - Adjust level distribution: `/org-roles {domain} --amend levels:{senior|staff|principal}`
> - Full registry deep-run: `/org-roles {domain} --amend expand` *(adds 2-3 more domain specialists)*

---
