R4 variations written. Here's the summary:

---

## Round 4 Summary

| V | Axis | Key mechanism |
|---|------|---------------|
| **V-01** | Stakeholder-traceability column | Adds 6th "Stakeholder" field to FIELD SCHEMA + signal plan -- traceability is an auditable column, not prose |
| **V-02** | Schema-first ordering | FIELD + COVERAGE schemas precede the Stakeholders fill-in -- tests C-17 positional vs functional "first output" |
| **V-03** | Unified contract table | Single CONTRACT TABLE with Scope column (per-field / whole-plan) -- tests C-18 physical vs logical separation |
| **V-04** | Template-first structure | Output template shown first, constraints after -- tests C-17 with bulk gate vs per-step gate |
| **V-05** | Cascade consequences + traceability column | Two-column consequence schema (Immediate failure / Downstream effect) + Stakeholder column -- deepest structural encoding |

**Predicted scores:**
- V-01: **100** — Stakeholder column satisfies C-17 more structurally than V-05 (R3); C-18 preserved
- V-02: **97.5** — Schemas precede the opener → C-15 fails (prompt doesn't *open* with stakeholder-risk) → C-17 fails → C-16 fails
- V-03: **97.5** — Single CONTRACT TABLE fails C-18's "two named schemas" literal requirement → C-16 fails
- V-04: **97.5** — No standalone gated Stakeholders step → C-17 fails (bulk gate ≠ per-step gate) → C-16 fails
- V-05: **100** — Cascade columns satisfy C-14 + C-18; Stakeholder column satisfies C-17

**R4 diagnostic question:** Do C-17 and C-18 have hidden structural constraints that the rubric text implies but doesn't state? V-02 probes the positional anchor. V-03 probes the physical separation requirement. V-04 probes whether a gated step is required vs a gated gate. If the predictions hold, the new patterns would be: (1) C-17 has positional anchor -- schemas must not precede the opener, and (2) C-18 requires physical two-table separation, not just a Scope column.
 column).

**What changes from R3**: R3 variations were designed to combine C-14 structural + C-15 structural. R4 stress-tests the exact structural form of C-17 and C-18 now that they are explicit criteria -- probing positional constraints (V-02, V-04), physical vs logical separation (V-03), and structural deepening beyond the minimum (V-01, V-05).

---

## V-01: Stakeholder-Traceability Column

**Axis**: Output format -- adds an explicit Stakeholder column (6th field) to both FIELD SCHEMA and the signal plan table, making C-17 role traceability a structural field with its own allowed-values constraint and consequence, rather than a prose instruction.
**Hypothesis**: V-05 (R3) enforces stakeholder traceability via prose: "Signal ownership in the Signal Plan must reference roles from this table." A 6-column signal plan with a Stakeholder column in FIELD SCHEMA (allowed values = rows in Stakeholders table; consequence = no named risk carrier) makes the traceability requirement auditable row-by-row without reading prose. The traceability constraint becomes a schema constraint with its own checkpoint in the pre-write gate. If V-01 scores 100, the finding is that stakeholder-field encoding is the structural analogue of C-17 prose traceability -- a stronger mechanism that satisfies C-17 and enables row-level auditability.

```
You are running /topic:new.

---

## Stakeholders at Risk

Identify who is harmed if this design is wrong. Fill this table now.
This is the first required output of this skill.

| Role | What they lose or inherit if the design is wrong |
|------|--------------------------------------------------|
| | |

Do not proceed until this table contains >=2 distinct named roles.
Every signal in the Signal Plan must name a Stakeholder from this table.

---

## Inputs

| Field | Description | If missing |
|-------|-------------|------------|
| topic | short slug, no spaces | ask once and wait |
| description | one sentence: what feature is under investigation? | ask once and wait |
| target | what decision will this unlock? | infer from description, then confirm |

Register in simulations/TOPICS.md -- create if absent, append row and write file:

| Topic | Description | Started | Status |
|-------|-------------|---------|--------|
| {topic} | {description} | {today} | active |

---

## Field Schema

| Field | Allowed values | Consequence if violated |
|-------|----------------|------------------------|
| Namespace | scout / draft / review / flow / trace / prove / listen / program / topic | Signal is unroutable to the skill runner that processes this strategy |
| Skill | Named skill within the namespace | Signal has no execution path; no artifact is produced |
| Item name | {topic}-{slug}-{date}.md | Artifact will not match registry lookup pattern; downstream skills cannot find it |
| Owner role | Named role from Stakeholders table above | No individual is accountable; signal is likely never gathered |
| Stakeholder | Named role from Stakeholders table above | Signal has no named risk carrier; the stakeholder who loses if this signal is missing cannot be identified |
| Priority | essential / recommended / optional | Any other value: strategy treated as advisory-only; commit gate logic fails; team has no enforceable threshold |

## Coverage Schema

| Requirement | Minimum | Consequence if not met |
|-------------|---------|------------------------|
| Essential signals | >=1 | Gate has no blocking condition; investigation can always be declared done; strategy is invalid as a decision gate |
| Distinct namespaces | >=2 | Investigation is blind to signal types from other dimensions |
| Distinct owner roles | >=2 | Single-perspective risk; cross-functional gaps remain undetected |
| Stakeholder coverage | All Stakeholder values present in Stakeholders table | Ungathered signals have no named risk owner; accountability gaps persist |
| Complete rows | All cells filled | Incomplete rows cannot be assigned, tracked, or scored |

---

## Signal Plan

| Namespace | Skill | Item name | Owner role | Stakeholder | Priority |
|-----------|-------|-----------|------------|-------------|----------|

Pre-write gate -- all must pass before writing any file:

  [ ] All Namespace values: one of 9 valid namespaces (Field Schema row 1)
  [ ] All Skill values: named skill within the namespace (Field Schema row 2)
  [ ] All Item names: {topic}-{slug}-{date}.md format (Field Schema row 3)
  [ ] All Owner roles: named individual from Stakeholders table (Field Schema row 4)
  [ ] All Stakeholder values: named role from Stakeholders table (Field Schema row 5)
  [ ] All Priority values: essential / recommended / optional -- no others (Field Schema row 6)
  [ ] >=1 essential signal (Coverage Schema row 1)
  [ ] >=2 distinct namespaces (Coverage Schema row 2)
  [ ] >=2 distinct owner roles from Stakeholders table (Coverage Schema row 3)
  [ ] All cells filled (Coverage Schema row 5)

Do not write any file until all ten checks pass.

---

## Strategy File

Write simulations/{topic}/strategy.md with these exact sections:

### Stakeholders at Risk
[Copy filled table from the opener -- same rows, no additions]

### Rationale
[2-4 sentences: which stakeholders are at risk? What assumption does the team currently hold? What decision does this investigation produce? What do they lose if they commit without it?]

### Signal Plan

| Namespace | Skill | Item name | Owner role | Stakeholder | Priority |
|-----------|-------|-----------|------------|-------------|----------|
[rows from Signal Plan above]

### Commit Gate
Design commit is permitted when: [minimum signal set, stated as a testable condition].
A testable condition names specific signals. "Enough evidence gathered" is not testable.

### Naming Reference
All item names in this strategy follow: {topic}-{slug}-{date}.md
Example: {topic}-feasibility-{today}.md
Deviation from this format: artifact will not match registry lookup pattern; downstream skills cannot find it.

---

## Confirm

Print:
  Topic: {topic}
  Strategy: simulations/{topic}/strategy.md
  TOPICS.md: updated
  Stakeholders: {count from opener}
  Essential: {count}  Recommended: {count}  Optional: {count}
  Namespaces: {list}
  Roles: {list}
  Gate: {one-line restatement from Commit Gate section}
```

---

## V-02: Schema-First Ordering

**Axis**: Lifecycle ordering -- FIELD SCHEMA and COVERAGE SCHEMA appear before the Stakeholders fill-in as definitional reference material. The Stakeholders fill-in is labeled "first required output" but is physically preceded by schema definitions.
**Hypothesis**: C-17 says the stakeholder-risk opener must be "the first output the model produces." If "first output" means "first active production step" (first table the model fills in), V-02 satisfies C-17 even with schemas preceding it -- schemas are read-once reference material, not outputs. If "first output" means "physically first in the prompt" (consistent with C-15 "Prompt opens with"), V-02 fails C-17. The diagnostic result reveals whether C-17 has a positional anchor or a purely functional one.

```
You are running /topic:new.

---

## Field Schema

Read before producing any output. Every signal row must conform to this schema.

| Field | Allowed values | Consequence if violated |
|-------|----------------|------------------------|
| Namespace | scout / draft / review / flow / trace / prove / listen / program / topic | Signal is unroutable to the skill runner that processes this strategy |
| Skill | Named skill within the namespace | Signal has no execution path; no artifact is produced |
| Item name | {topic}-{slug}-{date}.md | Artifact will not match registry lookup pattern; downstream skills cannot find it |
| Owner role | Named role from the Stakeholders table you will produce below | No individual is accountable; signal is likely never gathered |
| Priority | essential / recommended / optional | Any other value: strategy treated as advisory-only; commit gate logic fails; team has no enforceable threshold |

## Coverage Schema

| Requirement | Minimum | Consequence if not met |
|-------------|---------|------------------------|
| Essential signals | >=1 | Gate has no blocking condition; investigation can always be declared done; strategy is invalid as a decision gate |
| Distinct namespaces | >=2 | Investigation is blind to signal types from other dimensions |
| Distinct owner roles | >=2 | Single-perspective risk; cross-functional gaps remain undetected |
| Complete rows | All cells filled | Incomplete rows cannot be assigned, tracked, or scored |

---

## Step 1 -- Stakeholders at Risk

Now produce the first required output of this skill.
Identify who is harmed if this design is wrong. Fill this table.

| Role | What they lose or inherit if the design is wrong |
|------|--------------------------------------------------|
| | |

Do not proceed to Step 2 until this table contains >=2 distinct named roles.
Owner roles in the Signal Plan (Step 3) must reference rows from this table.

---

## Step 2 -- Inputs

| Field | Description | If missing |
|-------|-------------|------------|
| topic | short slug, no spaces | ask once and wait |
| description | one sentence: what feature is under investigation? | ask once and wait |
| target | what decision will this unlock? | infer from description, then confirm |

Register in simulations/TOPICS.md -- create if absent, append row and write file:

| Topic | Description | Started | Status |
|-------|-------------|---------|--------|
| {topic} | {description} | {today} | active |

---

## Step 3 -- Signal Plan

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|

Pre-write gate -- all must pass before writing any file:

  [ ] All Namespace values: one of 9 valid namespaces (Field Schema row 1)
  [ ] All Skill values: named skill within the namespace (Field Schema row 2)
  [ ] All Item names: {topic}-{slug}-{date}.md format (Field Schema row 3)
  [ ] All Owner roles: named individual from Stakeholders table in Step 1 (Field Schema row 4)
  [ ] All Priority values: essential / recommended / optional -- no others (Field Schema row 5)
  [ ] >=1 essential signal (Coverage Schema row 1)
  [ ] >=2 distinct namespaces (Coverage Schema row 2)
  [ ] >=2 distinct owner roles from Stakeholders table (Coverage Schema row 3)
  [ ] All cells filled (Coverage Schema row 4)

Do not write any file until all nine checks pass.

---

## Strategy File

Write simulations/{topic}/strategy.md with these exact sections:

### Stakeholders at Risk
[Copy filled table from Step 1 -- same rows, no additions]

### Rationale
[2-4 sentences: which stakeholders are at risk? What assumption does the team currently hold? What decision does this investigation produce? What do they lose if they commit without it?]

### Signal Plan

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|
[rows from Step 3]

### Commit Gate
Design commit is permitted when: [minimum signal set, stated as a testable condition].
A testable condition names specific signals. "Enough evidence gathered" is not testable.

### Naming Reference
All item names in this strategy follow: {topic}-{slug}-{date}.md
Example: {topic}-feasibility-{today}.md
Deviation from this format: artifact will not match registry lookup pattern; downstream skills cannot find it.

---

## Confirm

Print:
  Topic: {topic}
  Strategy: simulations/{topic}/strategy.md
  TOPICS.md: updated
  Stakeholders: {count from Step 1}
  Essential: {count}  Recommended: {count}  Optional: {count}
  Namespaces: {list}
  Roles: {list}
  Gate: {one-line restatement from Commit Gate section}
```

---

## V-03: Unified Contract Table

**Axis**: Output format -- merges FIELD SCHEMA and COVERAGE SCHEMA into a single CONTRACT TABLE with a Scope column (per-field / whole-plan), testing the minimum structural form of C-18.
**Hypothesis**: C-18 requires the prompt to "separate field-level constraints from coverage-level constraints into two named schemas." A single CONTRACT TABLE where per-field and whole-plan constraints are distinguished by a Scope column achieves logical separation in one structural element rather than two. This satisfies the spirit of C-18 (every constraint has exactly one structural home with a consequence column) without the letter ("two named schemas"). If C-18 strictly requires two separate tables, V-03 fails C-18. If C-18 accepts logical separation via a Scope column, V-03 passes. The diagnostic result clarifies whether C-18 is a structural-separation criterion or a physical-table-count criterion.

```
You are running /topic:new.

---

## Stakeholders at Risk

Identify who is harmed if this design is wrong. Fill this table now.
This is the first required output of this skill.

| Role | What they lose or inherit if the design is wrong |
|------|--------------------------------------------------|
| | |

Do not proceed until this table contains >=2 distinct named roles.
Owner roles in the Signal Plan must reference rows from this table.

---

## Inputs

| Field | Description | If missing |
|-------|-------------|------------|
| topic | short slug, no spaces | ask once and wait |
| description | one sentence: what feature is under investigation? | ask once and wait |
| target | what decision will this unlock? | infer from description, then confirm |

Register in simulations/TOPICS.md -- create if absent, append row and write file:

| Topic | Description | Started | Status |
|-------|-------------|---------|--------|
| {topic} | {description} | {today} | active |

---

## Contract

Every constraint has exactly one row in this table.
Scope = per-field: constraint applies to one cell in every signal row.
Scope = whole-plan: constraint applies to the signal set as a whole.

| Constraint | Scope | Rule | Consequence if violated |
|------------|-------|------|------------------------|
| Namespace | per-field | scout / draft / review / flow / trace / prove / listen / program / topic | Signal is unroutable to the skill runner that processes this strategy |
| Skill | per-field | Named skill within the namespace | Signal has no execution path; no artifact is produced |
| Item name | per-field | {topic}-{slug}-{date}.md | Artifact will not match registry lookup pattern; downstream skills cannot find it |
| Owner role | per-field | Named role from Stakeholders table above | No individual is accountable; signal is likely never gathered |
| Priority | per-field | essential / recommended / optional | Any other value: strategy treated as advisory-only; commit gate logic fails; team has no enforceable threshold |
| Essential signals | whole-plan | >=1 essential signal | Gate has no blocking condition; investigation can always be declared done; strategy is invalid as a decision gate |
| Distinct namespaces | whole-plan | >=2 distinct namespaces | Investigation is blind to signal types from other dimensions |
| Distinct owner roles | whole-plan | >=2 distinct owner roles from Stakeholders table | Single-perspective risk; cross-functional gaps remain undetected |
| Complete rows | whole-plan | All cells filled | Incomplete rows cannot be assigned, tracked, or scored |

---

## Signal Plan

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|

Pre-write gate -- verify against Contract table before writing any file:

  [ ] All Namespace values: one of 9 valid namespaces (Contract row 1)
  [ ] All Skill values: named skill within the namespace (Contract row 2)
  [ ] All Item names: {topic}-{slug}-{date}.md format (Contract row 3)
  [ ] All Owner roles: named individual from Stakeholders table (Contract row 4)
  [ ] All Priority values: essential / recommended / optional -- no others (Contract row 5)
  [ ] >=1 essential signal (Contract row 6)
  [ ] >=2 distinct namespaces (Contract row 7)
  [ ] >=2 distinct owner roles from Stakeholders table (Contract row 8)
  [ ] All cells filled (Contract row 9)

Do not write any file until all nine checks pass.

---

## Strategy File

Write simulations/{topic}/strategy.md with these exact sections:

### Stakeholders at Risk
[Copy filled table from the opener -- same rows, no additions]

### Rationale
[2-4 sentences: which stakeholders are at risk? What assumption does the team currently hold? What decision does this investigation produce? What do they lose if they commit without it?]

### Signal Plan

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|
[rows from Signal Plan above]

### Commit Gate
Design commit is permitted when: [minimum signal set, stated as a testable condition].
A testable condition names specific signals. "Enough evidence gathered" is not testable.

### Naming Reference
All item names in this strategy follow: {topic}-{slug}-{date}.md
Example: {topic}-feasibility-{today}.md
Deviation from this format: artifact will not match registry lookup pattern; downstream skills cannot find it.

---

## Confirm

Print:
  Topic: {topic}
  Strategy: simulations/{topic}/strategy.md
  TOPICS.md: updated
  Stakeholders: {count from opener}
  Essential: {count}  Recommended: {count}  Optional: {count}
  Namespaces: {list}
  Roles: {list}
  Gate: {one-line restatement from Commit Gate section}
```

---

## V-04: Template-First Structure

**Axis**: Lifecycle ordering -- the strategy file template is presented first (before schemas and gates), so the model sees the full target output before reading constraints. The Stakeholders at Risk section appears as a fill-in placeholder inside the template, not as a standalone gated opener step.
**Hypothesis**: Template-first design shows the model its target output before constraining how to produce it -- the inverse of V-05 (R3). The key C-17 test: does C-17 require the stakeholder-risk section to be an explicitly gated standalone step ("Do not proceed until >=2 roles"), or is it sufficient that the template shows it first and a bulk pre-write gate includes a stakeholder count check? If C-17 requires a per-step gate after the Stakeholders fill-in, V-04 fails -- the gate is a bulk checkpoint before file write, not a step-boundary gate after the stakeholder section. If C-17 only requires the section to appear first in the produced output, V-04 passes.

```
You are running /topic:new.

This skill produces simulations/{topic}/strategy.md and a row in simulations/TOPICS.md.

---

## Target Output: strategy.md

The strategy file must contain exactly these sections, in this order.
Read the Constraints section below before filling in any values.

---

### Stakeholders at Risk

| Role | What they lose or inherit if the design is wrong |
|------|--------------------------------------------------|
| [fill in: >=2 named roles required] | [fill in: specific harm] |

---

### Rationale

[fill in: 2-4 sentences -- which stakeholders are at risk? What assumption does the team hold? What decision does this investigation produce? What do they lose without it?]

---

### Signal Plan

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|
| [fill in] | [fill in] | [fill in] | [fill in] | [fill in] |

---

### Commit Gate

Design commit is permitted when: [fill in: minimum signal set as a testable condition -- names specific signals; "enough evidence gathered" is not a testable condition]

---

### Naming Reference

All item names in this strategy follow: {topic}-{slug}-{date}.md
Deviation: artifact will not match registry lookup pattern; downstream skills cannot find it.

---

## Constraints

Read before filling in any values. Then produce the full strategy.md in one pass, starting with the Stakeholders at Risk section.

### Field Schema -- applies per signal row

| Field | Allowed values | Consequence if violated |
|-------|----------------|------------------------|
| Namespace | scout / draft / review / flow / trace / prove / listen / program / topic | Signal is unroutable to the skill runner that processes this strategy |
| Skill | Named skill within the namespace | Signal has no execution path; no artifact is produced |
| Item name | {topic}-{slug}-{date}.md | Artifact will not match registry lookup pattern; downstream skills cannot find it |
| Owner role | Named role from your Stakeholders at Risk section | No individual is accountable; signal is likely never gathered |
| Priority | essential / recommended / optional | Any other value: strategy treated as advisory-only; commit gate logic fails; team has no enforceable threshold |

### Coverage Schema -- applies to the signal plan as a whole

| Requirement | Minimum | Consequence if not met |
|-------------|---------|------------------------|
| Essential signals | >=1 | Gate has no blocking condition; investigation can always be declared done; strategy is invalid as a decision gate |
| Distinct namespaces | >=2 | Investigation is blind to signal types from other dimensions |
| Distinct owner roles | >=2 | Single-perspective risk; cross-functional gaps remain undetected |
| Complete rows | All cells filled | Incomplete rows cannot be assigned, tracked, or scored |

---

## Inputs

| Field | Description | If missing |
|-------|-------------|------------|
| topic | short slug, no spaces | ask once and wait |
| description | one sentence: what feature is under investigation? | ask once and wait |
| target | what decision will this unlock? | infer from description, then confirm |

---

## Pre-Write Gate

Before writing any file, confirm all checks pass:

  [ ] Stakeholders at Risk table: >=2 distinct named roles (Field Schema row 4 dependency)
  [ ] All Namespace values: one of 9 valid namespaces (Field Schema row 1)
  [ ] All Skill values: named skill within the namespace (Field Schema row 2)
  [ ] All Item names: {topic}-{slug}-{date}.md format (Field Schema row 3)
  [ ] All Owner roles: named individual from Stakeholders at Risk section (Field Schema row 4)
  [ ] All Priority values: essential / recommended / optional -- no others (Field Schema row 5)
  [ ] >=1 essential signal (Coverage Schema row 1)
  [ ] >=2 distinct namespaces (Coverage Schema row 2)
  [ ] >=2 distinct owner roles from Stakeholders at Risk (Coverage Schema row 3)
  [ ] All cells filled (Coverage Schema row 4)

Do not write any file until all ten checks pass.

---

## Register

Open simulations/TOPICS.md. Create if absent. Append one row and write the file:

| Topic | Description | Started | Status |
|-------|-------------|---------|--------|
| {topic} | {description} | {today} | active |

Then write simulations/{topic}/strategy.md.

---

## Confirm

Print:
  Topic: {topic}
  Strategy: simulations/{topic}/strategy.md
  TOPICS.md: updated
  Stakeholders: {count}
  Essential: {count}  Recommended: {count}  Optional: {count}
  Namespaces: {list}
  Roles: {list}
  Gate: {one-line restatement}
```

---

## V-05: Cascade Consequences + Stakeholder-Traceability Column

**Axes**: Two combined -- (1) stakeholder-traceability column from V-01 axis, (2) two-column consequence schema (Immediate failure / Downstream effect) in both FIELD SCHEMA and COVERAGE SCHEMA.
**Hypothesis**: V-05 (R3) uses a single "Consequence if violated" column per schema. Splitting into two columns -- Immediate failure (what breaks at the point of violation) and Downstream effect (what the team loses later) -- deepens the structural encoding of C-14. Each constraint now carries a two-step failure pathway in two cells rather than one. Combined with the Stakeholder traceability column, this is the structurally densest variation in R4. The test: is cascade depth a new distinguishing pattern, or redundant with C-14 pass condition (which requires "downstream failure mode" but sets no minimum chain length)? If V-05 scores 100 but cascade columns produce no new excellence signal beyond V-01, the finding is that C-14 is satisfied by single-level consequence framing and cascade depth is stylistic. If cascade framing produces an observable distinguishing pattern, it becomes a candidate for C-19.

```
You are running /topic:new.

---

## Stakeholders at Risk

Identify who is harmed if this design is wrong. Fill this table now.
This is the first required output of this skill.

| Role | What they lose or inherit if the design is wrong |
|------|--------------------------------------------------|
| | |

Do not proceed until this table contains >=2 distinct named roles.
Every signal in the Signal Plan must name a Stakeholder from this table.
A signal with no named Stakeholder has no risk carrier -- it is likely never gathered.

---

## Inputs

| Field | Description | If missing |
|-------|-------------|------------|
| topic | short slug, no spaces | ask once and wait |
| description | one sentence: what feature is under investigation? | ask once and wait |
| target | what decision will this unlock? | infer from description, then confirm |

Register in simulations/TOPICS.md -- create if absent, append row and write file:

| Topic | Description | Started | Status |
|-------|-------------|---------|--------|
| {topic} | {description} | {today} | active |

---

## Field Schema

| Field | Allowed values | Immediate failure | Downstream effect |
|-------|----------------|-------------------|-------------------|
| Namespace | scout / draft / review / flow / trace / prove / listen / program / topic | Signal is unroutable to the skill runner | Strategy references a signal no runner can process; artifact is never produced; investigation silently stalls |
| Skill | Named skill within the namespace | Signal has no execution path | No artifact is produced; the namespace gap persists; investigation proceeds with a missing evidence type |
| Item name | {topic}-{slug}-{date}.md | Artifact does not match registry lookup pattern | Downstream skills cannot find the artifact; signal is ungathered from the perspective of any tool that queries the registry |
| Owner role | Named role from Stakeholders table above | No individual is accountable | Signal is likely never gathered; the commit gate operates on incomplete evidence |
| Stakeholder | Named role from Stakeholders table above | No named risk carrier for this signal | The stakeholder who loses if this signal is missing is unidentified; their exposure is never surfaced |
| Priority | essential / recommended / optional | Strategy treated as advisory-only | Commit gate logic fails; team has no enforceable threshold; design commit can proceed before all essential evidence is present |

## Coverage Schema

| Requirement | Minimum | Immediate failure | Downstream effect |
|-------------|---------|-------------------|-------------------|
| Essential signals | >=1 | Gate has no blocking condition | Investigation can always be declared done; team commits to design without completing the minimum evidence set |
| Distinct namespaces | >=2 | Investigation is blind to one or more signal dimensions | Evidence from excluded dimensions is never gathered; blind spots persist to design commit |
| Distinct owner roles | >=2 | Single-perspective risk surface | Cross-functional gaps are never surfaced; the investigation reflects only one team's concerns |
| Stakeholder coverage | All Stakeholder values in Stakeholders table | Ungathered signals have no named stakeholder | The missing signals cannot be traced to an at-risk party; accountability gaps persist silently |
| Complete rows | All cells filled | Row cannot be assigned | Signal is untrackable and unscorable; the investigation silently excludes it |

---

## Signal Plan

| Namespace | Skill | Item name | Owner role | Stakeholder | Priority |
|-----------|-------|-----------|------------|-------------|----------|

Pre-write gate -- all must pass before writing any file:

  [ ] All Namespace values: one of 9 valid namespaces (Field Schema row 1)
  [ ] All Skill values: named skill within the namespace (Field Schema row 2)
  [ ] All Item names: {topic}-{slug}-{date}.md format (Field Schema row 3)
  [ ] All Owner roles: named individual from Stakeholders table (Field Schema row 4)
  [ ] All Stakeholder values: named role from Stakeholders table (Field Schema row 5)
  [ ] All Priority values: essential / recommended / optional -- no others (Field Schema row 6)
  [ ] >=1 essential signal (Coverage Schema row 1)
  [ ] >=2 distinct namespaces (Coverage Schema row 2)
  [ ] >=2 distinct owner roles from Stakeholders table (Coverage Schema row 3)
  [ ] All cells filled (Coverage Schema row 5)

Do not write any file until all ten checks pass.

---

## Strategy File

Write simulations/{topic}/strategy.md with these exact sections:

### Stakeholders at Risk
[Copy filled table from the opener -- same rows, no additions]

### Rationale
[2-4 sentences: which stakeholders are at risk? What assumption does the team currently hold? What decision does this investigation produce? What do they lose if they commit without it?]

### Signal Plan

| Namespace | Skill | Item name | Owner role | Stakeholder | Priority |
|-----------|-------|-----------|------------|-------------|----------|
[rows from Signal Plan above]

### Commit Gate
Design commit is permitted when: [minimum signal set, stated as a testable condition].
A testable condition names specific signals. "Enough evidence gathered" is not testable.

### Naming Reference
All item names in this strategy follow: {topic}-{slug}-{date}.md
Example: {topic}-feasibility-{today}.md
Deviation from this format: artifact will not match registry lookup pattern; downstream skills cannot find it.

---

## Confirm

Print:
  Topic: {topic}
  Strategy: simulations/{topic}/strategy.md
  TOPICS.md: updated
  Stakeholders: {count from opener}
  Essential: {count}  Recommended: {count}  Optional: {count}
  Namespaces: {list}
  Roles: {list}
  Gate: {one-line restatement from Commit Gate section}
```
