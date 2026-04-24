Round 3 variations written to `simulations/quest/variations/topic-new-variations-R3-2026-03-14.md`.

---

## Round 3 Summary

| V | Axis | Key mechanism |
|---|------|---------------|
| **V-01** | Template-column encoding | Constraints embedded in column header cells — the column spec IS the constraint; no separate prose rules section |
| **V-02** | Consequence table | Dedicated CONSTRAINT CONSEQUENCES TABLE before signal planning — C-14 satisfied as a structural TABLE COLUMN |
| **V-03** | Mandatory stakeholder-risk fill-in | WHO IS AT RISK becomes a STEP 1 with required TABLE OUTPUT — C-15 structurally enforced, not just framed |
| **V-04** | Field schema + coverage schema | Two schema tables (per-field and whole-plan) carry `Consequence if violated` as a column — C-14 + C-16 in one structure |
| **V-05** | Full structural contract | Every criterion C-01 through C-16 maps to exactly one structural element; no prose-only rules remain |

**Key R3 question**: R2 proved that *inclusion* of C-11/C-12/C-13 is necessary and sufficient for 100. R3 tests whether *structural enforcement* of C-14 and C-15 (not just their presence as prose) is itself a meaningfully different mechanism — i.e., do variations that structuralize those criteria score differently from ones that prose-include them?

**Predicted ceiling**: V-05. The diagnostic result will be whether V-01–V-03 miss C-14/C-15/C-16 due to partial structural coverage, which would prove that the R3 criteria require the full structural contract to satisfy — a stronger claim than the R2 finding.
nd C-16 simultaneously, making it the most efficient encoding. V-03 is the most novel: making C-15 structural requires producing a filled output table, which is a qualitatively different mechanism than the static WHO IS AT RISK paragraph in R2 V-04.

**What changes from R2**: R2 variations were designed to INCLUDE C-11/C-12/C-13 — they used prose-with-structure. R3 variations are designed so that removing any structural element directly causes a criterion to fail — the structure IS the enforcement, not a vehicle for prose instructions that enforce.

---

## V-01: Template-Column Encoding

**Axis:** Template-column encoding — constraints are embedded inside column header cells, not stated in separate prose rule blocks. The column specification carries the allowed values and the operational consequence in a single cell. No standalone "field rules" section is needed.
**Hypothesis:** When the column header IS the constraint (e.g., "Priority (essential / recommended / optional — any other value makes this strategy non-gating)"), the model reads a structural datum rather than an advisory sentence. C-16 is satisfied by construction — each constraint lives in a structural element (table header) rather than prose. Consequence framing at the column level satisfies C-14 pervasively at minimal length.

```
You are running /topic:new.

---

STEP 1 — COLLECT INPUT

| Field | Value | If missing |
|-------|-------|------------|
| topic | short slug, no spaces | ask once and wait |
| description | one sentence: what feature is under investigation? | ask once and wait |
| target | what decision does this investigation unlock? | infer from description, then confirm |

---

STEP 2 — REGISTER

Open simulations/TOPICS.md. Create if absent. Append one row and write the file:

| Topic | Description | Started | Status |
|-------|-------------|---------|--------|
| {topic} | {description} | {today} | active |

---

STEP 3 — BUILD SIGNAL PLAN

Fill every cell. The column headers define the allowed values and the consequence of deviation.

| Namespace (scout/draft/review/flow/trace/prove/listen/program/topic — any other value: signal unroutable to skill runner) | Skill (named skill in the namespace — any other value: no execution path, no artifact produced) | Item name ({topic}-{slug}-{today}.md — any other format: artifact misses lookup pattern, downstream skills cannot find it) | Owner role (named individual role such as PM/Engineer/Designer/Researcher/SRE — "team" or blank: no accountability, signal likely ungathered) | Priority (essential/recommended/optional — any other value: strategy treated as advisory-only, commit gate logic fails) |
|-----------|-------|-----------|------------|----------|

Pre-write gate — all must pass before STEP 4:

  [ ] >=1 signal marked essential — zero essential: gate has no blocking condition, strategy is invalid
  [ ] >=2 distinct namespaces — single namespace: investigation blind to other signal dimensions
  [ ] >=2 distinct owner roles — single role: single-perspective risk, cross-functional gaps undetected
  [ ] All cells filled — blank cell: row unassignable, untrackable, unscorable
  [ ] All priority values: essential / recommended / optional only

Do not proceed to STEP 4 until all five checks pass.

---

STEP 4 — WRITE STRATEGY FILE

Write simulations/{topic}/strategy.md:

## Rationale
[2-4 sentences: what assumption is the team relying on? what decision does this investigation produce? what is the cost of committing without it?]

## Signal Plan

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|
[rows from STEP 3]

## Commit Gate
Design commit is permitted when: [minimum signal set, as a testable condition — not "enough evidence gathered"].

## Naming Reference
All item names in this strategy follow: {topic}-{slug}-{date}.md
Example: {topic}-feasibility-{today}.md

---

STEP 5 — CONFIRM

Print:
  Topic: {topic}
  Strategy: simulations/{topic}/strategy.md
  TOPICS.md: updated
  Essential: {count}  Recommended: {count}  Optional: {count}
  Namespaces: {list}
  Roles: {list}
```

---

## V-02: Consequence Table

**Axis:** Consequence table — a dedicated CONSTRAINT CONSEQUENCES TABLE appears before signal planning. Each row names a constraint, states the rule, and states the downstream failure mode. This makes C-14 (pervasive consequence framing) a structural artifact rather than inline prose: the consequences live in a table column.
**Hypothesis:** A CONSEQUENCES TABLE makes consequence framing structural (C-16) rather than rhetorical. When consequences are table rows rather than prose sentences, they are harder to read past. The model that processes a table row like "Priority vocab | essential/recommended/optional | advisory-only; commit gate logic fails" has less surface area to miss than one that reads a multi-sentence paragraph saying the same thing. This is the minimal intervention to structuralize C-14.

```
You are running /topic:new.

---

STEP 1 — COLLECT INPUT

Read from the user's invocation:
  topic:       short slug, no spaces
  description: one sentence — what feature is under investigation?
  target:      what decision does this investigation unlock?

If topic or description is missing, ask once and wait.

---

CONSTRAINT CONSEQUENCES

Every constraint below has a named downstream failure. The failure applies immediately —
it is not a warning or preference.

| Constraint | Rule | Downstream failure if violated |
|------------|------|-------------------------------|
| Namespace | One of: scout / draft / review / flow / trace / prove / listen / program / topic | Signal is unroutable; no skill runner can process it |
| Item name | {topic}-{slug}-{date}.md exactly | Artifact does not match registry lookup pattern; downstream skills cannot find it |
| Owner role | Named individual role — not "team" or a blank | No individual is accountable; signal is likely never gathered |
| Priority vocab | Exactly: essential / recommended / optional | Strategy treated as advisory-only; commit gate logic cannot function; team has no enforceable threshold |
| Essential count | At least 1 essential signal | Gate has no blocking condition; investigation can always be declared done; strategy is invalid as a decision gate |
| Namespace coverage | At least 2 distinct namespaces | Investigation is blind to signal types from other dimensions |
| Role coverage | At least 2 distinct owner roles | Single-perspective; cross-functional risk surface unexamined |
| Cell completeness | Every cell filled | Incomplete row cannot be assigned, tracked, or scored |

---

STEP 2 — REGISTER

Open simulations/TOPICS.md. Create if absent. Append one row and write the file:

| Topic | Description | Started | Status |
|-------|-------------|---------|--------|
| {topic} | {description} | {today} | active |

---

STEP 3 — BUILD SIGNAL PLAN

Plan signals. Apply the CONSTRAINT CONSEQUENCES table above to every field in every row.

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|

Pre-write gate — verify against the CONSTRAINT CONSEQUENCES table before writing:

  [ ] All Namespace values: one of the 9 valid namespaces
  [ ] All Item names: {topic}-{slug}-{date}.md format
  [ ] All Owner roles: named individual roles
  [ ] All Priority values: essential / recommended / optional — no others
  [ ] >=1 essential signal
  [ ] >=2 distinct namespaces
  [ ] >=2 distinct owner roles
  [ ] All cells filled

Do not write the strategy file until all eight checks pass.

---

STEP 4 — WRITE STRATEGY FILE

Write simulations/{topic}/strategy.md:

## Rationale
[2-4 sentences: what is the team currently assuming? What decision does this investigation produce? What is the cost of committing to a design without it?]

## Signal Plan

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|
[rows from STEP 3]

## Commit Gate
Design commit is permitted when: [minimum signal set, stated as a testable condition].

## Naming Reference
All item names in this strategy follow: {topic}-{slug}-{date}.md
Example: {topic}-feasibility-{today}.md

---

STEP 5 — CONFIRM

Print:
  Topic: {topic}
  Strategy: simulations/{topic}/strategy.md
  TOPICS.md: updated
  Essential: {count}  Total: {count}
  Namespaces: {list}
  Roles: {list}
  Gate: {one-line restatement}
```

---

## V-03: Mandatory Stakeholder-Risk Fill-In

**Axis:** Mandatory stakeholder-risk fill-in — WHO IS AT RISK becomes STEP 1 with a required TABLE OUTPUT (not a static framing paragraph). The model fills in the stakeholder-risk table before any signal planning. Signal ownership in the plan is explicitly constrained to reference roles from that table.
**Hypothesis:** R2 V-04's WHO IS AT RISK section was a framing paragraph — structural in form (a named section), but static in content (the model read it, not wrote it). C-15 requires a structural element; a mandatory fill-in table that the model must produce is structurally stronger than one it reads. When the stakeholder-risk table is an output of STEP 1, C-15 is enforced by the step structure itself. Role differentiation in signal ownership then emerges from the model's own STEP 1 output, making C-08 a downstream consequence of C-15 rather than an independent checklist item.

```
You are running /topic:new.

---

STEP 1 — STAKEHOLDERS AT RISK

Before planning any signals, identify who is harmed if this design is wrong.
Fill in the table below. This is the first deliverable of this skill.

| Role | What they lose or inherit if the design is wrong |
|------|--------------------------------------------------|
| [role name] | [specific harm: what commitment they made, what they must build, what they must explain] |
| [add rows as needed] | |

Do not proceed to STEP 2 until this table contains at least 2 distinct named roles.

Signal ownership in STEP 4 must trace to roles from this table. A signal whose owner
is not in this table has no named stakeholder carrying its risk — it is likely ungathered.

---

STEP 2 — COLLECT INPUT

Read from the user's invocation:
  topic:       short slug, no spaces
  description: one sentence — what feature is under investigation?
  target:      what decision does this investigation unlock?

If topic or description is missing, ask once and wait.

---

STEP 3 — REGISTER

Open simulations/TOPICS.md. Create if absent. Append one row and write the file:

| Topic | Description | Started | Status |
|-------|-------------|---------|--------|
| {topic} | {description} | {today} | active |

---

STEP 4 — BUILD SIGNAL PLAN

For each signal, assign ownership to a role from your STAKEHOLDERS AT RISK table in STEP 1.

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|
| (scout/draft/review/flow/trace/prove/listen/program/topic) | {skill} | {topic}-{slug}-{today}.md | (role from STEP 1 table) | (essential/recommended/optional) |

Priority — three values only:
  essential     — blocks design commit; gate cannot close without this signal
  recommended   — adds confidence; not blocking
  optional      — pursue only if time permits

Any other value (high/medium/low/P1/required/critical/nice-to-have) makes this strategy
invalid as a commit gate. The downstream system treats it as advisory-only. The team
loses the ability to hold design commit at an enforceable threshold.

Pre-write gate — all must pass before STEP 5:

  [ ] >=1 signal marked essential — zero essential: gate has no blocking condition
  [ ] >=2 distinct namespaces — single namespace: investigation blind to other dimensions
  [ ] All owner roles trace to a row in the STEP 1 table — untraceable role: no named stakeholder carries the risk
  [ ] All cells filled — blank cell: row unassignable
  [ ] All priority values: essential / recommended / optional only

Do not proceed to STEP 5 until all five checks pass.

---

STEP 5 — WRITE STRATEGY FILE

Write simulations/{topic}/strategy.md:

## Stakeholders at Risk
[Copy the filled table from STEP 1]

## Rationale
[2-4 sentences: which stakeholders are at risk if this design is wrong? What assumption are they relying on? What decision does this investigation produce? What do they lose if the team commits without it?]

## Signal Plan

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|
[rows from STEP 4]

## Commit Gate
Design commit is permitted when: [minimum signal set, as a testable condition].

## Naming Reference
All item names in this strategy follow: {topic}-{slug}-{date}.md
Example: {topic}-feasibility-{today}.md

---

STEP 6 — CONFIRM

Print:
  Topic: {topic}
  Strategy: simulations/{topic}/strategy.md
  TOPICS.md: updated
  Stakeholders identified: {count from STEP 1}
  Essential: {count}  Total: {count}
  Namespaces: {list}
  Roles: {list}
```

---

## V-04: Field Schema + Coverage Schema (C-14 + C-16 Combined)

**Axes:** Field schema + coverage schema — two SCHEMA TABLES appear before signal planning. FIELD SCHEMA has columns: Field / Allowed values / Consequence if violated. COVERAGE SCHEMA has columns: Requirement / Minimum / Consequence if not met. This single structure satisfies both C-14 (every constraint carries its downstream failure, in a table column) and C-16 (every constraint enforced by a structural element — table row — not prose).
**Hypothesis:** The FIELD SCHEMA table is the most efficient encoding of C-14 + C-16 together: one table, one Consequence column, every field covered. The model that reads a table row "Priority / essential/recommended/optional / strategy treated as advisory-only; commit gate logic fails" has both the constraint and its consequence in a single datum. The schema separation also encodes the distinction between per-field rules (FIELD SCHEMA) and whole-plan coverage rules (COVERAGE SCHEMA), which maps directly onto the structure of C-03/C-04/C-05/C-06/C-08 without restating each criterion in prose.

```
You are running /topic:new.

---

STEP 1 — COLLECT INPUT

Read from the user's invocation:
  topic:       short slug, no spaces
  description: one sentence — what feature is under investigation?
  target:      what decision does this investigation unlock?

If topic or description is missing, ask once and wait.

---

STEP 2 — REGISTER

Open simulations/TOPICS.md. Create if absent. Append one row and write the file:

| Topic | Description | Started | Status |
|-------|-------------|---------|--------|
| {topic} | {description} | {today} | active |

---

STEP 3 — BUILD SIGNAL PLAN

Apply both schemas below to every row before writing the strategy file.

FIELD SCHEMA — applies per row:

| Field | Allowed values | Consequence if violated |
|-------|---------------|------------------------|
| Namespace | scout / draft / review / flow / trace / prove / listen / program / topic | Signal is unroutable to the skill runner that processes this strategy |
| Skill | Named skill within the namespace | Signal has no execution path; no artifact is produced |
| Item name | {topic}-{slug}-{date}.md | Artifact will not match registry lookup pattern; downstream skills cannot find it |
| Owner role | Named individual role (PM / Engineer / Designer / Researcher / SRE / other explicit) | No individual is accountable; signal is likely never gathered |
| Priority | essential / recommended / optional | Any other value: strategy treated as advisory-only; commit gate logic fails; team has no enforceable threshold before design commit |

COVERAGE SCHEMA — applies to the plan as a whole:

| Requirement | Minimum | Consequence if not met |
|-------------|---------|------------------------|
| Essential signals | >=1 | Gate has no blocking condition; investigation can always be declared done; strategy is invalid as a decision gate |
| Distinct namespaces | >=2 | Investigation is blind to signal types from dimensions outside the one covered |
| Distinct owner roles | >=2 | Single-perspective risk; cross-functional gaps remain undetected |
| Complete rows | All cells filled | Incomplete rows cannot be assigned, tracked, or scored |

Signal plan table:

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|

Pre-write gate — check against both schemas before writing any file:

  [ ] All Namespace values: one of 9 valid namespaces (FIELD SCHEMA row 1)
  [ ] All Item names: {topic}-{slug}-{date}.md format (FIELD SCHEMA row 3)
  [ ] All Owner roles: named individual roles (FIELD SCHEMA row 4)
  [ ] All Priority values: essential / recommended / optional (FIELD SCHEMA row 5)
  [ ] >=1 essential signal (COVERAGE SCHEMA row 1)
  [ ] >=2 distinct namespaces (COVERAGE SCHEMA row 2)
  [ ] >=2 distinct owner roles (COVERAGE SCHEMA row 3)
  [ ] All cells filled (COVERAGE SCHEMA row 4)

Do not proceed to STEP 4 until all eight checks pass.

---

STEP 4 — WRITE STRATEGY FILE

Write simulations/{topic}/strategy.md:

## Rationale
[2-4 sentences: what is the team currently assuming? What decision does this investigation produce? What is the cost of committing to a design without it?]

## Signal Plan

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|
[rows from STEP 3]

## Commit Gate
Design commit is permitted when: [minimum signal set, stated as a testable condition — not "enough evidence"].

## Naming Reference
All item names in this strategy follow: {topic}-{slug}-{date}.md
Example: {topic}-feasibility-{today}.md

---

STEP 5 — CONFIRM

Print:
  Topic: {topic}
  Strategy: simulations/{topic}/strategy.md
  TOPICS.md: updated
  Essential: {count}  Recommended: {count}  Optional: {count}
  Namespaces: {list}
  Roles: {list}
  Gate: {one-line restatement}
```

---

## V-05: Full Structural Contract (C-14 + C-15 + C-16 Fully Combined)

**Axes:** All three new R3 patterns combined — C-15 (stakeholder-risk opener) as a mandatory fill-in table, C-14 (pervasive consequence framing) as table columns in FIELD SCHEMA and COVERAGE SCHEMA, C-16 (structural enforcement of every criterion) by mapping each criterion to exactly one structural element. Every rule is a table row. Every gate is a checkbox. Every required output is a named section. No criterion is enforced by prose instruction alone.
**Hypothesis:** This is the structural ceiling for topic-new. Every criterion C-01 through C-16 maps to a named structural element; removing any one structural element would cause at least one criterion to fail. The stakeholder-risk fill-in produces output that feeds directly into signal ownership (C-15 + C-08 integrated structurally). Field and coverage schemas carry consequences as table columns (C-14 structural). Checkbox gate covers all coverage criteria (C-11). Dedicated sections cover C-09 and C-10 (C-13). If V-05 scores 100 and V-01–V-04 score lower on C-14/C-15/C-16, the finding is that structural enforcement of the aspirational criteria is a separate mechanism from structural enforcement of the essential and recommended criteria.

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
Signal ownership in the Signal Plan must reference roles from this table.

---

## Inputs

Collect before writing anything:

| Field | Description | If missing |
|-------|-------------|------------|
| topic | short slug, no spaces | ask once and wait |
| description | one sentence: what feature is under investigation? | ask once and wait |
| target | what decision will this unlock? | infer from description, then confirm |

Register in simulations/TOPICS.md — create if absent, append row and write file:

| Topic | Description | Started | Status |
|-------|-------------|---------|--------|
| {topic} | {description} | {today} | active |

---

## Field Schema

Every signal row must conform to this schema. Consequence applies immediately on violation.

| Field | Allowed values | Consequence if violated |
|-------|---------------|------------------------|
| Namespace | scout / draft / review / flow / trace / prove / listen / program / topic | Signal is unroutable to the skill runner that processes this strategy |
| Skill | Named skill within the namespace | Signal has no execution path; no artifact is produced |
| Item name | {topic}-{slug}-{date}.md | Artifact will not match registry lookup pattern; downstream skills cannot find it |
| Owner role | Named role from Stakeholders table above (or other explicit named role) | No individual is accountable; signal is likely never gathered |
| Priority | essential / recommended / optional | Any other value: strategy treated as advisory-only; commit gate logic fails; team has no enforceable threshold |

## Coverage Schema

| Requirement | Minimum | Consequence if not met |
|-------------|---------|------------------------|
| Essential signals | >=1 | Gate has no blocking condition; investigation can always be declared done; strategy is invalid as a decision gate |
| Distinct namespaces | >=2 | Investigation is blind to signal types from other dimensions |
| Distinct owner roles | >=2 | Single-perspective risk; cross-functional gaps remain undetected |
| Complete rows | All cells filled | Incomplete rows cannot be assigned, tracked, or scored |

---

## Signal Plan

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|

Pre-write gate — all must pass before writing any file:

  [ ] All Namespace values: one of 9 valid namespaces (Field Schema row 1)
  [ ] All Skill values: named skill within the namespace (Field Schema row 2)
  [ ] All Item names: {topic}-{slug}-{date}.md format (Field Schema row 3)
  [ ] All Owner roles: named individual from Stakeholders table (Field Schema row 4)
  [ ] All Priority values: essential / recommended / optional — no others (Field Schema row 5)
  [ ] >=1 essential signal (Coverage Schema row 1)
  [ ] >=2 distinct namespaces (Coverage Schema row 2)
  [ ] >=2 distinct owner roles from Stakeholders table (Coverage Schema row 3)
  [ ] All cells filled (Coverage Schema row 4)

Do not write any file until all nine checks pass.

---

## Strategy File

Write simulations/{topic}/strategy.md with these exact sections:

### Stakeholders at Risk
[Copy filled table from the opener — same rows, no additions]

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
