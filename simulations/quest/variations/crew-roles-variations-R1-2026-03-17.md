Now I have full context. Generating all 5 variations:

---

## crew-roles Skill Body Variations — Round 1

---

### V-01
**Axis**: Inertia framing — status-quo challenger is named first, defined before all other roles, lens anchored to domain-specific costs

**Hypothesis**: Naming the inertia-advocate first and giving it a domain-grounded template forces the model to pull domain terms early, improving C-02 and C-10 without any additional instruction for those criteria.

```
Generate a typed role registry for a domain.

## Step 1 — Name the inertia-advocate first

Before identifying any other roles, characterize the status quo for the input domain:
- What system, process, or pattern is currently in use?
- What are its documented costs, migration risks, or user habits?

Write the inertia-advocate role file. Its lens must include at least one verify question
referencing a specific cost or artifact from the domain above (not a generic "why change?").

## Step 2 — Derive the remaining roles from domain context

Analyze the product, codebase, or spec provided. Identify the expert perspectives that would
catch problems the inertia-advocate cannot: technical depth, product judgment, user empathy,
strategy, and operational risk. Do not use generic archetypes — derive role names and expertise
from what you read.

Minimum: 3 roles total (including the inertia-advocate).
Target: cover at least 3 of: technical, product, strategy, ops orientations.

## Step 3 — Populate all 5 required fields for every role

Each role file must contain:
- orientation: one sentence on what frame this role applies and who it serves
- lens: verify (questions ending in ?) and simplify (rules starting with an imperative verb)
- expertise: domain-specific depth and relevance — no generic "software engineering depth"
- scope: the organizational reach (component, service, cross-team, org-wide)
- collaborates_with: names of other roles in this registry (must match actual role file names)

## Step 4 — Write output

Write one markdown file per role to: .craft/roles/{area}/
{area} is derived from the input domain — not "roles" or "default".
```

---

### V-02
**Axis**: Output format — explicit per-field template with examples replaces prose description

**Hypothesis**: Showing a concrete role file template with examples for each field eliminates the most common failure modes (missing fields, generic expertise, statement-style lens) by anchoring the model to the exact format the rubric inspects.

```
Generate a typed role registry for a domain. Analyze the product, codebase, or spec to
determine what expert perspectives are needed. Write one markdown file per role.

## Role file template

Use this exact structure for every role file:

---
name: {role-name}
orientation: {one sentence — what frame this role applies and whose interests it serves}
expertise:
  depth: {domain-specific expertise — reference actual patterns, systems, or concerns from the input}
  relevance: {why this perspective is needed for this domain specifically}
scope: {component | service | cross-team | org-wide}
collaborates_with:
  - {exact name of another role file in this registry}
lens:
  verify:
    - {falsifiable question ending in ?}
    - {falsifiable question ending in ?}
  simplify:
    - {directive starting with imperative verb, e.g. "Remove X if Y is unused."}
    - {directive starting with imperative verb}
---

## Required roles

1. inertia-advocate — always present. Orientation: challenges every proposal with why the
   current approach is sufficient. Lens verify questions must include: "Why is the existing
   {specific system or pattern in this domain} insufficient for this use case?"

2. At least 2 additional roles derived from the input domain. Cover at least 3 of:
   technical / product / strategy / ops orientations.

## Scope guidance

Assign distinct scope levels across the registry. Do not give every role the same scope.
Use at least 2 different values from: component, service, cross-team, org-wide.

## collaborates_with integrity

Every name in a collaborates_with list must match the filename of another role in this
registry. Resolve all references before writing.

## Output path

.craft/roles/{area}/   where {area} reflects the actual input domain.
```

---

### V-03
**Axis**: Role sequence — prescribe an explicit 4-step discovery algorithm before any writing begins

**Hypothesis**: Making domain analysis an explicit numbered phase (before role creation) forces the model to surface domain-specific terms that then flow into expertise and lens fields, improving C-04 and C-10 without needing to repeat domain-specificity instructions per field.

```
Generate a typed role registry for a domain.

Run the following four phases in order. Do not skip to writing until Phase 3 is complete.

### Phase 1 — Domain scan

Read the input. Extract and list:
- Key systems, APIs, or components mentioned
- Primary user types or stakeholders
- Known constraints, risks, or failure modes
- Existing processes or patterns that would be disrupted

This list becomes the vocabulary pool for expertise and lens fields.

### Phase 2 — Perspective inventory

From the domain scan, identify the expert perspectives that would catch problems across
these categories: technical (architecture, reliability, security), product (PM, UX, customers),
strategy (business case, go-to-market), ops (compliance, support, migration).

List candidate roles. For each, note: what do they uniquely see that others miss?

Always include: inertia-advocate. Its unique view is why the status quo is already sufficient.

Minimum 3 roles. Target 4-6.

### Phase 3 — Cross-reference audit

Before writing files:
- Assign a filename to each role (kebab-case, e.g. api-reliability-engineer.md)
- List all collaborates_with pairs and verify both sides name real roles in the list
- Verify scope values span at least 2 distinct levels

Fix any orphan references or scope collisions.

### Phase 4 — Write role files

For each role, write a markdown file with all 5 fields:

  orientation     — frame this role applies; whose interests it serves
  expertise       — depth (domain-specific, from Phase 1 vocabulary) + relevance
  scope           — component | service | cross-team | org-wide
  collaborates_with — verified names from Phase 3
  lens
    verify        — questions ending in ? that test falsifiable conditions
    simplify      — directives starting with an imperative verb

Output path: .craft/roles/{area}/
```

---

### V-04
**Axis**: Lifecycle emphasis + formal phrasing register — 4-phase lifecycle with explicit contracts, imperative technical language throughout

**Hypothesis**: Framing the skill as a formal lifecycle with phase contracts (not just a task list) signals to the model that each phase has a defined output state that feeds the next, reducing the chance that late phases (collaborates_with resolution, scope gradient) are dropped under pressure to finish.

```
You are executing the crew-roles skill. The skill runs in four phases. Each phase has a
defined output. Do not advance to the next phase until the current phase output is complete.

---

PHASE 1 — SETUP
Input: domain name, product spec, codebase, or any artifact describing what is being built.
Output: domain vocabulary list — the specific systems, patterns, user types, and risks present
in the input. This list is mandatory input to Phase 2.

If no input is provided, halt and request it.

---

PHASE 2 — ROLE DERIVATION
Input: domain vocabulary from Phase 1.
Output: a role manifest — a table listing: role name, orientation category, scope level,
and at least one domain term from Phase 1 that will appear in its expertise field.

Rules:
- Include exactly one inertia-advocate. Orientation: adversarial — challenges all proposals
  with domain-specific reasons the status quo is sufficient.
- Include at least 2 additional roles. Together, cover at least 3 orientation categories
  (technical, product, strategy, ops).
- Assign scope levels so at least 2 distinct levels appear across the manifest.
- Assign filenames in kebab-case. These are the canonical names for collaborates_with.

Do not write role files yet.

---

PHASE 3 — COLLABORATES_WITH RESOLUTION
Input: role manifest from Phase 2.
Output: an adjacency map — for each role, which other roles it collaborates with.

Rules:
- Every name in the adjacency map must be a filename from the manifest. No orphans.
- Each role must list at least 1 collaborator.
- The inertia-advocate should be referenced by at least 1 other role.

Resolve any orphan references before advancing.

---

PHASE 4 — FILE GENERATION
Input: manifest (Phase 2) + adjacency map (Phase 3).
Output: one markdown file per role at .craft/roles/{area}/

Each file must contain these fields:
  orientation     — one sentence, frame + stakeholder
  expertise       — depth (domain-specific term required) + relevance
  scope           — value from manifest
  collaborates_with — names from adjacency map
  lens
    verify        — at least 2 questions, each ending in ?
    simplify      — at least 2 rules, each starting with an imperative verb

The {area} directory segment must reflect the actual input domain.
```

---

### V-05
**Axis**: Full integration — inertia prominence (V-01) + template enforcement (V-02) + discovery algorithm (V-03) + formal lifecycle (V-04) + lens actionability enforcement inline

**Hypothesis**: The combination of explicit domain scan, inertia-first role naming, concrete field template with examples, and collaborates_with pre-validation addresses all 10 rubric criteria in a single pass. Expected to score highest on composite, at the cost of verbosity.

```
You are executing the crew-roles skill. Generate a typed role registry for the input domain.

## Phase 1 — Domain scan (do not skip)

Read the input artifact. Extract:
- Systems, APIs, or data stores present in the domain
- User types and their primary workflows
- Constraints, risks, or known failure modes
- Any existing process or pattern that would be displaced

Record these as a vocabulary list. Every expertise field in Phase 3 must reference at least
one term from this list.

## Phase 2 — Role planning

Name the inertia-advocate first. Before listing any other roles, characterize:
  - What is currently in place in this domain?
  - What are the specific costs of migrating away from it?
  - What user habits depend on it?

These answers become the inertia-advocate's lens content.

Then derive additional roles from the vocabulary list. Target at least 3 orientation
categories across the full registry:
  technical  — e.g. architect, reliability engineer, security reviewer
  product    — e.g. PM, UX designer, customer advocate
  strategy   — e.g. business lead, go-to-market, exec sponsor
  ops        — e.g. compliance, support, migration

Minimum 3 roles total. Assign filenames (kebab-case). Assign scope levels — use at least
2 distinct levels across the registry (component, service, cross-team, org-wide).

Validate collaborates_with before writing: every name must match a filename in this list.

## Phase 3 — Write role files

Write one markdown file per role. Use this exact field structure:

```md
---
name: {kebab-case matches filename}
orientation: {one sentence — frame applied + stakeholder served}
expertise:
  depth: {domain-specific — must include a term from Phase 1 vocabulary}
  relevance: {why this perspective is essential for this domain}
scope: {component | service | cross-team | org-wide}
collaborates_with:
  - {filename of another role in this registry}
lens:
  verify:
    - {question ending in ?}
    - {question ending in ?}
  simplify:
    - {imperative verb phrase, e.g. "Collapse X and Y into a single interface."}
    - {imperative verb phrase}
---
```

The inertia-advocate's verify section must include at least one question naming a
specific system, pattern, or artifact from Phase 1 — not generic "why change?" language.

## Phase 4 — Output

Write all files to: .craft/roles/{area}/
{area} is derived from the input domain. Do not use "roles", "default", or any generic segment.

After writing, print a registry summary:
| Role | Orientation | Scope | Collaborates With |
listing all generated roles. This confirms the output path and cross-reference integrity.
```

---

### Variation Summary

| ID | Axis | Primary Rubric Target | Expected Strength | Expected Risk |
|----|------|-----------------------|-------------------|---------------|
| V-01 | Inertia framing first | C-02, C-10 | Domain-grounded inertia lens | May skip C-06 lens format without explicit instruction |
| V-02 | Explicit field template | C-01, C-06 | No missing fields, format enforced | Discovery phase absent; C-04 may still produce generic expertise |
| V-03 | Discovery algorithm | C-04, C-08 | Domain vocabulary flows into all fields | No inertia prominence; C-10 depends on model initiative |
| V-04 | Lifecycle + formal register | C-07, C-09 | Phase contracts prevent late-phase drop | Verbose; model may truncate Phase 1 under token pressure |
| V-05 | Full integration | All 10 criteria | Highest composite ceiling | Longest prompt; single-axis failure mode is opacity |
