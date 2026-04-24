---
skill: quest-variate
skill_target: crew-roles
date: 2026-03-17
round: 3
rubric: crew-roles-rubric-v3-2026-03-17.md
---

# crew-roles — Variate R3

5 complete prompt body variations for the `crew-roles` skill.
Single-axis first (V-01 through V-03), then two-axis combinations (V-04, V-05).

Round 3 targets three new aspirational criteria introduced in rubric v3:
- **C-14** Scope-Gradient-Enforcement: structural gate (not soft instruction) checks scope after writing; if all same, identifies and revises 1–2 roles before delivery
- **C-15** Verification-Gate-Phase: ALL post-write checks bundled into a single explicitly named gate that blocks delivery — table, orphan check, and scope check together, not scattered
- **C-16** Vocabulary-Linked Inertia Q&A: each Q1/Q2/Q3 answer must reference at least one Phase 1 vocabulary term — wires C-11 and C-12 structurally, not independently satisfied

Baseline gap from R2 scorecard:
- C-14: PARTIAL in V-01, V-02, V-04 (scope instructed but never gated)
- C-15: V-03 R2 Step 4 had the checks but not an explicitly named blocking gate — bundling was accidental, not structural
- C-16: V-04 R2 required vocab in Q2 but not Q1/Q3; V-05 R2's exit condition covered all three but per-question prompting was inconsistent

---

## V-01

**Axis**: Verification-Gate-Phase (C-15 — single axis)
**Hypothesis**: An explicitly named "VERIFICATION GATE" phase — with per-check PASS declarations
required before proceeding and "DELIVERY BLOCKED" language — creates a forcing function that
a "Registry Summary" or "Step 4 checks" format cannot. When the gate is named and its blocking
intent is declared, model drift cannot silently drop or merge checks. Each check must clear
independently before the gate lifts.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

---

### Phase 1 — Domain Vocabulary

Read the input. Extract and label:

```
## Domain Vocabulary

Systems: [named products, services, modules, APIs — proper nouns from the input]
Patterns: [named workflows, protocols, architectural decisions from the input]
Key terms: [domain-specific nouns not present in generic engineering documentation]
```

Minimum 3 terms across categories. If the input yields fewer, extend by inference and label
inferred terms `[inferred]`.

---

### Phase 2 — Inertia Pre-Characterization

Before writing any role file, answer these three questions:

**Q1 — Current system**: What existing system, tool, or approach will this domain displace or extend?
**Q2 — Migration cost**: What concrete cost or risk does moving away from it create?
**Q3 — User habit**: What observable workflow or daily behavior depends on the current system?

```
## Inertia Pre-Characterization

Current system: [named entity]
Migration cost: [specific cost or risk]
User habit: [named workflow or observable behavior]
```

---

### Phase 3 — Write Role Files

Roles needed: PM, Architect, inertia-advocate, plus domain specialist(s) derived from Phase 1
vocabulary. Minimum 3 roles total.

For each role, write `.roles/{area}/{role-name}.md`:

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
  - {Imperative verb phrase — Remove / Defer / Collapse / Merge}
  - {Imperative verb phrase}

## expertise
depth: {senior | staff | principal}
relevance: {sentence referencing at least one Phase 1 vocabulary term}

## scope
{team | cross-team | org}

## collaborates_with
- {exact file stem of another role in this registry}
```

**Inertia-advocate constraints**:
- `orientation.frame` must name the current system from Q1
- `lens.verify`: at least 2 questions must reference Q1/Q2/Q3 dimensions by name
- `expertise.relevance`: must reference the current system from Q1
- `scope`: cross-team

Write all role files before proceeding to Phase 4.

---

### Phase 4 — VERIFICATION GATE

**DELIVERY IS BLOCKED. Complete all 4 checks in order. Each check must declare PASS before the
next check opens. If a check finds a defect, fix it and re-check before proceeding.**

---

**CHECK 1 — Registry Summary Table**

Write this table from the role files produced:

| Role | Frame (first 8 words) | Scope | Collaborates With |
|------|-----------------------|-------|-------------------|

One row per role file. Every cell must be filled. No placeholder text.

Declare: `CHECK 1: PASS` or `CHECK 1: FAIL — [issue]`

---

**CHECK 2 — Orphan Reference Resolution**

From the Collaborates With column: does every name match a Role column entry?
Flag mismatches: `{name} [UNRESOLVED]`.
For each unresolved entry: add the missing role or remove the reference. State action taken.

Declare: `CHECK 2: PASS` or `CHECK 2: FAIL — [issue, action taken]`

---

**CHECK 3 — Scope Gradient Enforcement**

From the Scope column: list all distinct scope values present.
Gate condition: at least 2 distinct values must appear.

If all roles share one scope value:
1. Identify 1–2 roles where actual organizational reach differs from the assigned value.
2. Revise their scope field.
3. State: "Revised {role-name} scope {old} → {new}: {reason}."
4. Re-list scope values to confirm distinct count ≥ 2.

Declare: `CHECK 3: PASS — scope values: [list]` or `CHECK 3: FAIL — [action taken]`

---

**CHECK 4 — Vocabulary Coverage**

From each role's `expertise.relevance` field: does it reference a Phase 1 vocabulary term?
Flag any that do not: `{role-name} [NO VOCAB TERM]`.
Revise flagged fields. State which vocabulary term was added and to which role.

Declare: `CHECK 4: PASS` or `CHECK 4: FAIL — [revisions made]`

---

All 4 checks declared PASS → **VERIFICATION GATE CLEAR. Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(gate re-runs after addition)*
> - Re-run gate: `/crew-roles {domain} --amend verify`
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-02

**Axis**: Vocabulary-Linked Inertia Q&A (C-16 — single axis)
**Hypothesis**: A per-answer format constraint — requiring `[vocab: {term}]` to mark the specific
vocabulary term used in each Q1/Q2/Q3 answer — makes vocabulary linkage verifiable at answer
generation time. An exit-condition check ("at least one vocab term in each answer") is evaluated
after the answer is written and can miss Q3 when Q1 and Q2 already reference terms. An in-answer
annotation requirement makes the linkage explicit during generation, not as a retrospective audit.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

---

### Phase 1 — Domain Vocabulary

Read the input. Extract and label:

```
## Domain Vocabulary

Systems: [named products, services, modules, APIs — proper nouns]
Patterns: [named workflows, protocols, architectural decisions]
Key terms: [domain-specific nouns traceable to the input]
```

Minimum 3 terms. Extend by inference if needed; label inferred terms `[inferred]`.

This vocabulary list is the anchor for Phase 2. **Every Q1/Q2/Q3 answer must reference at least
one term from this list by name.** If a question cannot be answered using vocabulary terms,
return to Phase 1 and extend the list before proceeding.

---

### Phase 2 — Inertia Pre-Characterization

Answer these three questions. **Each answer uses the required format: answer text followed by
`[vocab: {term}]` naming the specific vocabulary term referenced. An answer without a `[vocab]`
annotation fails this phase.**

**Q1 — Current system**
What existing system, tool, or approach from the Phase 1 vocabulary will this domain displace?
Required format: `Current system: [answer] [vocab: {term-from-Phase-1}]`

**Q2 — Migration cost**
What concrete cost or risk does replacing it create? Reference a vocabulary term.
Required format: `Migration cost: [answer] [vocab: {term-from-Phase-1}]`

**Q3 — User habit**
What observable workflow or daily behavior depends on the current system?
Required format: `User habit: [answer] [vocab: {term-from-Phase-1}]`

```
## Inertia Pre-Characterization

Current system: [answer] [vocab: {term}]
Migration cost: [answer] [vocab: {term}]
User habit: [answer] [vocab: {term}]
```

The `[vocab]` annotations are structural: C-11 (vocabulary extraction) and C-12 (inertia
characterization) are not independently satisfied — the Phase 2 answers draw vocabulary from
Phase 1 by name. If any answer lacks a `[vocab]` annotation, it must be rewritten.

---

### Phase 3 — Write Role Files

Roles needed: PM, Architect, inertia-advocate, plus domain specialist(s) from Phase 1 vocabulary.
Minimum 3 roles. List selected roles and one-line rationale before writing.

For each non-inertia role, write `.roles/{area}/{role-name}.md`:

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
  - {Imperative: Remove / Defer / Collapse / Merge}
  - {Imperative}

## expertise
depth: {senior | staff | principal}
relevance: {sentence referencing at least one Phase 1 vocabulary term}

## scope
{team | cross-team | org}

## collaborates_with
- {exact file stem of another role in this registry}
```

**For the inertia-advocate**, write `.roles/{area}/inertia-advocate.md`:
- `orientation.frame`: name the current system from Q1 verbatim
- `lens.verify`: 3 questions; each must reference the vocabulary term from the Q it corresponds to:
  - Question 1: references the current system (Q1 vocab term)
  - Question 2: references the migration cost dimension (Q2 vocab term)
  - Question 3: references the user habit dimension (Q3 vocab term)
- `expertise.relevance`: reference the Q1 vocab term plus one additional Phase 1 term
- `scope`: cross-team
- `collaborates_with`: pm

---

### Phase 4 — Registry Summary and Self-Check

After writing all role files:

| Role | Frame (first 8 words) | Scope | Collaborates With |
|------|-----------------------|-------|-------------------|

**Checks**:
1. **Orphan references**: Do all Collaborates With names match a Role entry? Fix any that don't.
2. **Scope gradient**: Do at least 2 distinct scope values appear? If all are identical, note the
   gap and revise 1–2 roles to reflect their actual organizational reach.

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}`
> - Re-run vocabulary linkage: `/crew-roles {domain} --amend vocab` *(re-runs Phase 1 + 2)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-03

**Axis**: Scope-Gradient-Enforcement (C-14 — single axis)
**Hypothesis**: Enforcing scope diversity at planning time — via a scope assignment table written
before role files — prevents homogeneous scope sets from being written in the first place. Post-
write correction requires undoing work already done. Pre-write scope planning surfaces the
gradient requirement when roles are still malleable, and a "revise before proceeding" gate makes
the correction point explicit before any file is written.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

---

### Step 1 — Domain Analysis

Read the input. Determine:
- Domain name (becomes `{area}` in the output path)
- Key systems, tools, or patterns in use
- Current system or approach this domain changes or extends
- What expert perspectives the domain requires

---

### Step 2 — Role Scope Planning Table

Before writing any role file, plan the registry in a scope assignment table.

**Scope definitions**:
- `team`: decisions and risks contained within a single team
- `cross-team`: requires coordination or sign-off from 2+ teams
- `org`: requires org-level alignment, policy, or executive visibility

Plan the registry:

| Role | Perspective Category | Scope Assignment | Justification |
|------|---------------------|------------------|---------------|
| pm | product | {scope} | {one reason} |
| architect | technical | {scope} | {one reason} |
| inertia-advocate | inertia | cross-team | default — status quo spans the domain |
| {domain-specialist} | domain | {scope} | {one reason} |

Include at least one domain specialist derived from the input. Add rows as needed.

---

**SCOPE AUDIT — complete before writing any role file:**

1. List all scope values from the Scope Assignment column.
2. Count distinct values.
3. Gate condition: at least 2 distinct values must appear.

**If all assigned scopes are identical**:
- Identify 1–2 roles where a different scope is defensible given the actual organizational reach.
- Revise their Scope Assignment in the table.
- State: "Revised {role-name} scope {old} → {new}: {reason}."
- Re-check distinct count.

Do not write any role file until the table contains at least 2 distinct scope values.
Confirm: `SCOPE AUDIT PASS — scope values: [list]`

---

### Step 3 — Write Role Files

Write each role from the planning table in order. Scope values come from the audited table —
do not change them during file writing.

For each role, write `.roles/{area}/{role-name}.md`:

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
  - {Imperative: Remove / Defer / Collapse / Merge}
  - {Imperative}

## expertise
depth: {senior | staff | principal}
relevance: {sentence specific to this domain — no generic engineering language}

## scope
{value from the scope planning table — do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**Inertia-advocate constraints**:
- `orientation.frame` must name the current system from Step 1 analysis
- `lens.verify`: at least 2 questions reference current-system name, migration cost, or user habit
- `scope`: cross-team (as planned in table)

---

### Step 4 — Registry Summary

After writing all role files:

| Role | Frame (first 8 words) | Scope | Collaborates With |
|------|----------------------|-------|-------------------|

**Orphan check**: Do all Collaborates With names match a Role entry?
Flag: `{name} [UNRESOLVED]`. Add the missing role or remove the reference.

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(scope planning re-runs)*
> - Revise scope plan: `/crew-roles {domain} --amend scope`
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-04

**Axes**: Verification-Gate-Phase + Scope-Gradient-Enforcement (C-15 + C-14)
**Hypothesis**: Combining a pre-write scope planning gate (V-03's Step 2 SCOPE AUDIT) with a
post-write VERIFICATION GATE (V-01's Phase 4) creates two enforcement points for scope diversity:
one that prevents homogeneous scope sets from being written, and one that catches any that slip
through. The bundled post-write gate also closes C-07 (orphan references) and C-13 (registry
table) simultaneously. Neither gate is redundant — the scope audit fires before files exist,
the verification gate fires after.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

---

### Phase 1 — Domain Vocabulary

Read the input. Extract and label:

```
## Domain Vocabulary

Systems: [named products, services, modules, APIs — proper nouns]
Patterns: [named workflows, protocols, architectural decisions]
Key terms: [domain-specific nouns traceable to the input]
```

Minimum 3 terms. Extend by inference if needed; label inferred terms `[inferred]`.

---

### Phase 2 — Inertia Pre-Characterization

Answer before writing any role:

**Q1 — Current system**: What existing system, tool, or approach does the domain use today?
**Q2 — Migration cost**: What concrete cost or risk does replacing it create? Reference a vocabulary term.
**Q3 — User habit**: What observable workflow depends on the current system?

```
## Inertia Pre-Characterization

Current system: [named entity]
Migration cost: [specific cost — referencing vocabulary term]
User habit: [named workflow or behavior]
```

---

### Phase 3 — Scope Planning Gate

Before writing role files, assign scope to each role. This gate fires before any file is written.

**Scope definitions**: `team` (within one team) | `cross-team` (2+ teams) | `org` (org-wide)

| Role | Perspective | Scope | Justification |
|------|-------------|-------|---------------|
| pm | product | {scope} | {reason} |
| architect | technical | {scope} | {reason} |
| inertia-advocate | inertia | cross-team | status quo spans the domain |
| {domain-specialist} | domain | {scope} | derived from Phase 1 vocabulary |

Add domain specialist rows for each major system or pattern from Phase 1 vocabulary that PM
and Architect cannot adequately represent.

**SCOPE AUDIT**:
List distinct scope values from the table. Gate condition: at least 2 distinct values.
If only 1 value appears: revise 1–2 roles in the table. State changes. Re-confirm count.
`SCOPE AUDIT PASS` — then proceed to Phase 4.

---

### Phase 4 — Write Role Files

Write each role from the Phase 3 planning table. Use the audited scope values.

For each non-inertia role, write `.roles/{area}/{role-name}.md`:

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
  - {Imperative: Remove / Defer / Collapse / Merge}
  - {Imperative}

## expertise
depth: {senior | staff | principal}
relevance: {sentence containing at least one Phase 1 vocabulary term}

## scope
{value from Phase 3 table — do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**For the inertia-advocate**, write `.roles/{area}/inertia-advocate.md`:
- `orientation.frame`: name the current system from Q1 verbatim
- `lens.verify`: 3 questions; each must reference a Q1/Q2/Q3 dimension
- `expertise.relevance`: reference Q1 current system + one Phase 1 vocabulary term
- `scope`: cross-team (from Phase 3 table)
- `collaborates_with`: pm

Write all role files before proceeding to Phase 5.

---

### Phase 5 — VERIFICATION GATE

**DELIVERY IS BLOCKED. All 3 checks must declare PASS before output is delivered.**

---

**CHECK 1 — Registry Summary Table**

| Role | Frame (first 8 words) | Scope | Collaborates With |
|------|-----------------------|-------|-------------------|

One row per role. All cells filled.
Declare: `CHECK 1: PASS` or `CHECK 1: FAIL — [issue]`

---

**CHECK 2 — Orphan Reference Resolution**

For every name in Collaborates With: does it appear in Role column?
Flag: `{name} [UNRESOLVED]`. For each: add role or remove reference. State action.
Declare: `CHECK 2: PASS` or `CHECK 2: FAIL — [action taken]`

---

**CHECK 3 — Scope Gradient Confirmation**

List distinct scope values from the Scope column.
Gate condition: at least 2 distinct values (already enforced in Phase 3; confirm here).
If Phase 3 scope audit was bypassed and all scopes are identical: enforce now — identify and
revise 1–2 roles. State changes.
Declare: `CHECK 3: PASS — scope values: [list]` or `CHECK 3: FAIL — [action taken]`

---

All 3 checks declared PASS → **VERIFICATION GATE CLEAR. Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(scope gate + verification gate re-run)*
> - Re-run scope planning: `/crew-roles {domain} --amend scope`
> - Re-run gate: `/crew-roles {domain} --amend verify`
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`

---

---

## V-05

**Axes**: Verification-Gate-Phase + Scope-Gradient-Enforcement + Vocabulary-Linked Inertia Q&A
         (C-15 + C-14 + C-16 — full synthesis)
**Hypothesis**: Three structural mechanisms at three different execution points create overlapping
guarantees. (1) Per-answer `[vocab: {term}]` annotation in Phase 2 wires C-11 and C-12 at answer
generation time — the linkage cannot be satisfied retroactively. (2) Pre-write scope planning
gate prevents homogeneous scope sets before files exist. (3) Named VERIFICATION GATE bundles all
post-write checks into a single blocking phase — orphan resolution, scope confirmation, and
vocabulary coverage all gate together. The three mechanisms do not duplicate each other: the
annotation enforces during Q&A, the scope gate enforces during planning, the verification gate
enforces after writing. Each catches a distinct failure mode at the point where correction is cheapest.

---

You are running `/crew-roles`.

Generate a typed role registry for the provided domain. Write role files to `.roles/{area}/`.
Every role file requires all 5 fields: `orientation` (frame, verify, simplify), `expertise` (depth,
relevance), `scope`, `collaborates_with`. Verify items end in `?`; simplify items are imperatives.

**5 phases. Each has an explicit exit condition. Do not proceed until the exit condition is met.**

---

### Phase 1 — DOMAIN VOCABULARY

**Entry**: domain input provided
**Exit**: vocabulary list written with at least 3 terms

Read the input. Extract and label:

```
## Domain Vocabulary

Systems: [named products, services, modules, APIs — proper nouns from the input]
Patterns: [named workflows, protocols, architectural decisions from the input]
Key terms: [domain-specific nouns not present in generic engineering documentation]
```

If input yields fewer than 3 terms, extend by inference. Label inferred terms `[inferred]` and
state the basis: "inferred from [X] because [reason]."

**Exit condition met**: vocabulary list present with 3+ terms.

---

### Phase 2 — INERTIA PRE-CHARACTERIZATION

**Entry**: Phase 1 complete
**Exit**: all 3 answers written; each contains a `[vocab: {term}]` annotation referencing a
         Phase 1 term; no answer is missing its annotation

Answer these three questions. **Each answer must reference at least one Phase 1 vocabulary term.
Use the required format: answer text followed by `[vocab: {term}]`. An answer missing its
annotation fails this phase — rewrite it before proceeding to Phase 3.**

**Q1 — Current system**
What system, tool, or approach from the Phase 1 vocabulary does the domain currently rely on?
If nothing in the vocabulary is explicitly a "current thing," identify the closest status-quo
equivalent and name it as a proper noun.
Required format: `Current system: [answer] [vocab: {term}]`

**Q2 — Migration cost**
What concrete cost or risk does moving away from the current system create?
Name the category: integration work, retraining, data migration, pipeline disruption, ramp time.
Reference a vocabulary term.
Required format: `Migration cost: [answer] [vocab: {term}]`

**Q3 — User habit**
What observable workflow or daily behavior depends on the current system?
Name the specific behavior: "users currently do [X] using [Y] which would change."
Reference a vocabulary term.
Required format: `User habit: [answer] [vocab: {term}]`

```
## Inertia Pre-Characterization

Current system: [answer] [vocab: {term}]
Migration cost: [answer] [vocab: {term}]
User habit: [answer] [vocab: {term}]
```

**Exit condition met**: 3 answers written, each contains a `[vocab: {term}]` annotation.
If any annotation is missing: rewrite that answer before proceeding.

---

### Phase 3 — SCOPE PLANNING GATE

**Entry**: Phase 2 complete
**Exit**: scope planning table written with at least 2 distinct scope values confirmed

Before writing role files, assign scope to each role. Scope values:
- `team` — decisions contained within one team
- `cross-team` — requires coordination across 2+ teams
- `org` — requires org-level alignment or executive visibility

Build the planning table:

| Role | Perspective | Scope | Justification |
|------|-------------|-------|---------------|
| pm | product | {scope} | {one reason based on input context} |
| architect | technical | {scope} | {one reason based on input context} |
| inertia-advocate | inertia | cross-team | status quo spans the full domain |
| {domain-specialist} | domain | {scope} | derived from Phase 1 vocabulary |

Add one or more domain specialist rows for systems or patterns in Phase 1 vocabulary that PM
and Architect cannot adequately represent.

**SCOPE AUDIT**:
1. List all distinct scope values from the Scope column.
2. Gate condition: at least 2 distinct values.
3. If only 1 value: identify 1–2 roles where actual organizational reach differs. Revise the
   table. State: "Revised {role} scope {old} → {new}: {reason}."
4. Confirm distinct count ≥ 2.

**Exit condition met**: `SCOPE AUDIT PASS — scope values: [list]`
Do not write any role file until scope audit passes.

---

### Phase 4 — WRITE ROLE FILES

**Entry**: Phase 3 complete (scope audit passed)
**Exit**: all role files written; every `expertise.relevance` references a Phase 1 vocabulary
         term; inertia-advocate verify covers Q1, Q2, Q3 using Phase 2 vocab terms

List selected roles and one-line rationale before writing files.

**For each non-inertia role**, write `.roles/{area}/{role-name}.md`:

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
  - {Imperative: Remove / Defer / Collapse / Merge / Move}
  - {Imperative}

## expertise
depth: {senior | staff | principal}
relevance: {sentence containing at least one Phase 1 vocabulary term}

## scope
{value from Phase 3 table — do not change}

## collaborates_with
- {exact file stem of another role in this registry}
```

**Vocabulary constraint**: Each `expertise.relevance` must reference a Phase 1 vocabulary term.
If a relevance sentence has no vocabulary term, the role is under-scoped — rename it to a more
specific perspective before writing the file.

**For the inertia-advocate**, write `.roles/{area}/inertia-advocate.md`:

- `orientation.frame`: "Challenge every proposal with evidence that [current system from Q1]
  remains sufficient given [migration cost from Q2]." The Q1 current system name must appear
  verbatim. The Q2 cost dimension must appear verbatim or by paraphrase.
- `lens.verify`: 3 questions with per-dimension distribution — each references a Phase 2 vocab term:
  - Question 1: names the current system (Q1 vocab term)
  - Question 2: references the migration cost or risk category (Q2 vocab term)
  - Question 3: references the user habit or dependent workflow (Q3 vocab term)
  A generic question ("Is the current approach sufficient?") fails even if 2 of 3 are specific.
- `lens.simplify`: at least 2 imperative rules for eliminating scope that fails inertia scrutiny
- `expertise.relevance`: reference Q1 vocab term + at least one other Phase 1 term
- `scope`: cross-team (from Phase 3 table)
- `collaborates_with`: pm

**Exit condition met**: all files written; every `expertise.relevance` contains a Phase 1 term;
inertia-advocate verify questions each reference Q1, Q2, Q3 vocabulary terms respectively.

---

### Phase 5 — VERIFICATION GATE

**Entry**: Phase 4 complete
**Exit**: all 4 checks declare PASS; gate explicitly confirmed before delivery

**DELIVERY IS BLOCKED. Complete all 4 checks in order. Each must declare PASS before the next
opens. Fix defects found in earlier checks before proceeding to later ones.**

---

**CHECK 1 — Registry Summary Table**

Write from the role files produced:

| Role | Frame (first 8 words) | Scope | Collaborates With |
|------|-----------------------|-------|-------------------|

One row per role file. Every cell filled. Role column must match file stems exactly.
Declare: `CHECK 1: PASS` or `CHECK 1: FAIL — [issue]`

---

**CHECK 2 — Orphan Reference Resolution**

For every name in Collaborates With: does it appear in the Role column?
Flag: `{name} [UNRESOLVED]`.
For each: add the missing role to the registry OR remove the reference from the citing file.
State action taken for each.
Gate condition: zero `[UNRESOLVED]` entries.
Declare: `CHECK 2: PASS` or `CHECK 2: FAIL — [actions taken]`

---

**CHECK 3 — Scope Gradient Confirmation**

List distinct scope values from the Scope column.
Gate condition: at least 2 distinct values (Phase 3 scope audit should have ensured this).
If Phase 3 was bypassed and all scopes are identical: enforce now — revise 1–2 roles. State changes.
Declare: `CHECK 3: PASS — scope values: [list]` or `CHECK 3: FAIL — [action taken]`

---

**CHECK 4 — Vocabulary Coverage**

For each role's `expertise.relevance`: does it reference a Phase 1 vocabulary term?
Flag: `{role-name} [NO VOCAB TERM]`. Revise the field. State which term was added.
Gate condition: zero `[NO VOCAB TERM]` entries.
Declare: `CHECK 4: PASS` or `CHECK 4: FAIL — [revisions made]`

---

All 4 checks declared PASS → **VERIFICATION GATE CLEAR. Delivering output.**

---

### AMEND

> **AMEND**
> - Add a role: `/crew-roles {domain} --amend add:{role-name}` *(scope gate + verification gate re-run)*
> - Refresh vocabulary: `/crew-roles {domain} --amend vocab` *(re-runs Phase 1; Phase 2 and Phase 4 update)*
> - Re-characterize inertia: `/crew-roles {domain} --amend reinertia` *(re-runs Phase 2; inertia-advocate rewrites)*
> - Re-run scope gate: `/crew-roles {domain} --amend scope` *(re-runs Phase 3)*
> - Re-run verification gate: `/crew-roles {domain} --amend verify` *(re-runs Phase 5)*
> - Adjust levels: `/crew-roles {domain} --amend levels:{senior|staff|principal}`
