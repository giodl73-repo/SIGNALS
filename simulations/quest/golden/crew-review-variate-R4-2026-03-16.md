---
skill: quest-variate
skill_target: crew-review
date: 2026-03-16
round: 4
rubric: crew-review-rubric-v4-2026-03-16.md
---

# crew-review -- Variate R4

5 complete prompt body variations. Single-axis first (V-01 through V-03), then
two-axis combinations (V-04, V-05).

**R4 design target**: Three new aspirational criteria introduced in v4 rubric. R3 sourced
each one from a different variation but no single variation hit all three. R4 explores:
- V-01: C-17 axis -- named exit gate on challenger phase (formal structural block)
- V-02: C-18 axis -- each unfilled slot produces a separate dedicated matrix row
- V-03: C-19 axis -- every column definition names its anti-pattern exclusion
- V-04: C-17 + C-18 combination -- gate exit condition defined in terms of row production
- V-05: C-17 + C-18 + C-19 maximal -- all three new aspirational plus all prior aspirational

Registry context assumed: `.craft/roles/` contains `inertia-advocate.md`, `pm.md`,
`architect.md` (and whatever else the workspace adds). Role files include `archetype`,
`lens.verify`, `expertise.relevance` fields.

---

## V-01

**Axis**: Inertia framing (challenger phase gate)
**Hypothesis**: Replacing the challenger phase sequence instruction ("run challengers first")
with a named, explicitly-opened gate -- where the gate has a defined open state, a closed
state, and a closure condition -- makes domain review structurally blocked until the
condition is met, not instruction-dependent. C-17 requires that the blocking be stated as
a constraint ("domain review does not begin until gate G1 closes"), not as a sequence
hint ("run challengers before domain reviewers"). A gate with named state produces the
structural block; proximity-of-instruction does not.

---

You are running `/crew-review`.

Route the artifact through the org registry and produce a multi-role review matrix.

---

### Step 1 -- Load the registry

Read every file in `.craft/roles/`. Extract each role's name, `archetype`, `lens.verify`,
and `expertise.relevance`.

Error conditions -- all halt execution immediately, no soft fallback:
- `.craft/roles/` is absent: `ERROR: .craft/roles/ not found. Cannot proceed.`
- `.craft/roles/` is present but empty: `ERROR: .craft/roles/ is empty. Cannot proceed.`
- A role file is missing `lens.verify` or `expertise.relevance`:
  `ERROR: [role-name] missing required fields. Registry malformed. Cannot proceed.`

Role pool = all files found. Zero roles may be fabricated.

---

### CHALLENGER PHASE

**Gate G1 -- challenger bracket gate**

G1 state: OPEN (domain review is blocked)

G1 closure condition -- all of the following must be true before G1 closes:
1. All roles with `archetype: challenger` have run.
2. The null hypothesis 4-slot form has been attempted for each challenger role.
3. Every slot that could not be filled has been escalated to a HIGH finding.
4. No slot has been silently omitted, collapsed with another slot, or left as a
   generic placeholder.

**Domain review does not begin until G1 closes.**

---

From the role pool, identify all roles with `archetype: challenger`. Run each one now.

For each challenger role, fill this null hypothesis 4-slot form:

> **Null hypothesis (4-slot form):**
> - **[SLOT-A]** We currently do ________ instead of building this.
> - **[SLOT-B]** The cost of that alternative is ________.
> - **[SLOT-C]** The switching cost to adopt this artifact is ________.
> - **[SLOT-D]** This artifact is worth acting on only if ________.

Fill each slot from artifact content or inferable workspace context.

Slot escalation rule -- mandatory, applies per slot:
- A slot that cannot be filled: write `[not stated in artifact]` in that slot, then
  log a HIGH finding: "SLOT-[letter]: null hypothesis incomplete -- [slot name] not
  stated in artifact."
- Generic placeholders ("some cost," "existing workflow") count as unfilled.
- Do not collapse two slots into one sentence.

Challenger severity:
- HIGH: the "do nothing" case is credible and unaddressed in the artifact
- MEDIUM: inertia case is named but switching cost is not quantified
- LOW: artifact directly neutralizes the status quo argument

**G1 state: CLOSED** (all closure conditions satisfied)

---

### DOMAIN PHASE

**Entry condition: G1 must be closed. Domain review is now permitted to begin.**

Depth rules:
- **Standard** (default): select 2-3 roles from the pool (excluding challengers) whose
  `expertise.relevance` intersects the artifact's type and subject matter. Write one
  sentence per selection explaining the match.
- **`--depth deep`**: run every non-challenger role in the registry.

For each selected domain role:
- Apply only that role's `lens.verify` perspective
- Name a specific artifact surface in each finding (section title, field name, diagram
  element, named assumption)
- Do not repeat a finding already raised by a prior reviewer
- Severity: HIGH / MEDIUM / LOW only -- no other labels
- Recommendation: one concrete action naming what to do and where in the artifact

---

### Output

Write the review as a 4-column table:

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|

Row order: challenger roles first (from CHALLENGER PHASE), then domain roles in
selection order.

Column constraints:
- **Role**: must match a `.craft/roles/` filename stem
- **Severity**: exactly HIGH, MEDIUM, or LOW -- no other values

After the table:

**Cross-role synthesis** (required, 2-3 sentences): name at least one convergence (two
roles raised the same concern) or one conflict (two roles disagree). If genuinely absent:
"No cross-role signal detected -- findings are non-overlapping."

**AMEND** (required):

> **AMEND**
> - Add a reviewer: `/crew-review [artifact] --amend add:[role-name]`
> - Full registry run: `/crew-review [artifact] --depth deep`
> - Restrict to domain: `/crew-review [artifact] --amend scope:[domain]`
> - Re-open G1 with an additional challenger: `/crew-review [artifact] --amend rerun:challengers`

---

---

## V-02

**Axis**: Output format (empty-slot escalation as separate matrix row)
**Hypothesis**: When a null hypothesis slot cannot be filled, escalating it to a separate
dedicated matrix row -- following the same 4-column schema as every domain finding -- makes
the incompleteness independently scorable: the gap is visible, labeled, and holds its own
severity and recommendation. Embedding the gap as a sentence within the challenger row's
Findings cell produces a slot gap that exists inside a finding; producing a separate row
produces a slot gap that IS a finding. C-18 requires the latter. The distinction is not
editorial -- it changes what the output contract commits to: the empty-slot gap must be
countable in the matrix alongside domain findings, not nested inside the challenger row.

---

You are running `/crew-review`.

Produce a structured crew review for the provided artifact.

---

### Step 1 -- Load registry

Read every file in `.craft/roles/`. Extract: role name, `archetype`, `lens.verify`,
`expertise.relevance`.

Error halts -- unconditional, no soft fallback:
- Directory absent: `ERROR: .craft/roles/ not found.` Halt.
- Directory empty: `ERROR: .craft/roles/ is empty.` Halt.
- Any file missing `lens.verify` or `expertise.relevance`:
  `ERROR: [role-name] missing required fields. Registry malformed.` Halt.

Role pool = all files found. Zero roles may be invented.

---

### Step 2 -- Challenger bracket

Find all roles with `archetype: challenger`. Run each one before any domain review.

For each challenger role, attempt the null hypothesis 4-slot form:

```
SLOT-A: We currently do [______] instead of building this.
SLOT-B: The cost of that alternative is [______].
SLOT-C: The switching cost to adopt this artifact is [______].
SLOT-D: This artifact is worth acting on only if [______].
```

Fill each slot from artifact content or inferable workspace context.

**Slot-to-row escalation rule** -- mandatory, applies to each slot independently:

If a slot cannot be filled from the artifact:
1. Write `[not stated in artifact]` in that slot position in the null hypothesis form.
2. Produce a **separate, dedicated matrix row** for that gap -- a full 4-column row
   following the same schema as every domain finding in the matrix:

   | `[role-name]` | SLOT-[letter] gap: [slot label] not stated in artifact. Null hypothesis is incomplete without this. | HIGH | State [slot requirement] explicitly in the artifact before proceeding with crew review. |

3. Place this row immediately after the challenger's primary row in the matrix.
4. Do not embed the gap as a sentence within the challenger row's Findings cell.
5. Do not append the gap as a note or comment below the row.
6. Each unfilled slot produces its own dedicated row. Two unfilled slots = two rows.

Generic placeholders ("some cost", "existing workflow") count as unfilled slots.
Do not collapse two slots into one sentence.

Challenger severity (for the primary challenger row):
- HIGH: inertia case is credible and unaddressed in the artifact
- MEDIUM: inertia case is named but switching cost is not quantified
- LOW: artifact directly neutralizes the status quo

---

### Step 3 -- Domain review

Depth selection:
- **Standard** (default): select 2-3 roles (non-challenger) whose `expertise.relevance`
  intersects the artifact type. Document each selection: "[role]: selected because [reason]."
- **`--depth deep`**: select all non-challenger roles in the pool.

For each selected domain role:
1. Apply only that role's `lens.verify` perspective.
2. Name a specific artifact surface in each finding.
3. Severity: exactly HIGH, MEDIUM, or LOW -- no other values.
4. Recommendation: one concrete action naming what to do and where.
5. Do not repeat a finding already raised by a prior reviewer.

---

### Step 4 -- Review matrix

Write the review as a 4-column table:

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|

Row order:
1. Challenger primary row(s)
2. Slot-gap escalation rows (one per unfilled slot, immediately after their challenger row)
3. Domain rows in selection order

Every cell is specific. No generic findings. No generic recommendations.

---

### Step 5 -- Cross-role synthesis

2-3 sentences. Name at least one convergence (two roles raised the same concern) or one
conflict (two roles disagree on priority or direction). Note: slot-gap escalation rows
count as findings for convergence detection -- if a domain reviewer also surfaces the
same gap, that is convergence. If genuinely absent: "No cross-role signal detected --
findings are non-overlapping."

---

### Step 6 -- AMEND

> **AMEND**
> - Add a reviewer: `/crew-review [artifact] --amend add:[role-name]`
> - Full registry run: `/crew-review [artifact] --depth deep`
> - Restrict to domain: `/crew-review [artifact] --amend scope:[domain]`
> - Re-run challenger bracket: `/crew-review [artifact] --amend rerun:challengers`

---

---

## V-03

**Axis**: Output format (anti-pattern exclusion in typed column constraints)
**Hypothesis**: A typed output schema that defines both what IS valid (positive constraint)
and what IS NOT valid (named anti-pattern exclusion) inside each column's type definition
is self-documenting about its own failure modes. C-13 requires that column contracts be
visible; C-19 requires that at least one column contract name the specific anti-pattern it
excludes. The hypothesis is that naming the anti-pattern inside the constraint definition
-- not as a separate general instruction -- prevents the exact failure mode it targets,
because the model encounters the exclusion at the same moment it constructs the cell.
A separate general instruction to "avoid generic findings" applies globally but is
evaluated separately; an exclusion inside the column definition is evaluated per-cell
at construction time.

---

You are running `/crew-review`.

Produce a structured crew review. Output schema is declared before execution and must
be followed exactly. The schema defines both valid values and excluded anti-patterns for
each column.

---

### Output schema (read before executing)

The review is a single markdown table with five columns:

| Column | Type -- valid | Anti-pattern excluded (NOT valid) |
|--------|--------------|-----------------------------------|
| Role | string -- filename stem from `.craft/roles/` at execution time | NOT: invented role names; names from memory or prior runs; names not present in the registry at this execution |
| Lens | string -- one sentence: "As a [role], I care about [specific concern from this role's `lens.verify`]" | NOT: generic role restatements ("As a PM, I review as a PM"); NOT: concerns taken from a different role's lens; NOT: lens statements longer than one sentence |
| Findings | string -- names a specific artifact surface: a section title, field name, diagram element, or named assumption | NOT: abstract observations without a named surface ("needs more detail", "unclear", "incomplete", "could be improved"); NOT: findings that name only the artifact as a whole |
| Severity | enum -- exactly `HIGH`, `MEDIUM`, or `LOW`; HIGH = blocks commitment; MEDIUM = must resolve before ship; LOW = advisory | NOT: freestyle labels (Critical, Minor, Warning, Blocker, Moderate, Severe); NOT: blank cells; NOT: combinations ("HIGH/MEDIUM") |
| Recommendation | string -- names (1) what to do and (2) where in the artifact | NOT: generic directives ("review this", "improve this section", "consider adding more", "needs clarification"); NOT: actions without a named artifact location |

Per-row validation gate: before writing any row, verify all five cells against their
column constraints. If any cell would violate its anti-pattern exclusion, revise it until
it no longer violates. Do not write a row that fails validation.

After the table: a cross-role synthesis block and an AMEND block. Both are required.

---

### Execution

**Phase 1 -- Load**

Open `.craft/roles/`. Read every file. Role pool = all files found.

Error halts -- unconditional, no soft fallback:
- Directory absent: `ERROR: .craft/roles/ not found.` Halt.
- Directory empty: `ERROR: .craft/roles/ is empty.` Halt.
- Any role file missing `lens.verify` or `expertise.relevance`:
  `ERROR: [role-name] missing required fields.` Halt.

Zero roles may be invented or substituted.

**Phase 2 -- Select**

Default (standard): select 2-4 roles whose `expertise.relevance` intersects the artifact
type. Include any role with `archetype: challenger` regardless of relevance. Document each
selection: "[role]: selected because [reason tied to artifact]."

`--depth deep`: select all roles in the registry.

**Phase 3 -- Review**

Execute roles in this order: `archetype: challenger` first, then all others.

For each role, apply the per-row validation gate before writing the row:
- Role name is in `.craft/roles/` -- not invented ✓
- Lens is one sentence traceable to this role's `lens.verify` -- no generic restatement ✓
- Finding names a specific artifact surface -- not an abstract observation ✓
- Severity is exactly HIGH, MEDIUM, or LOW -- no freestyle label ✓
- Recommendation names what to do and where -- no generic directive ✓

For challenger roles: the Lens cell opens with a null hypothesis framing. The Findings
cell names what the team currently does instead of adopting this artifact.

**Phase 4 -- Output**

Write the 5-column table (Role, Lens, Findings, Severity, Recommendation).

**Cross-role synthesis** (required, 2-3 sentences): name at least one convergence or one
conflict. If genuinely absent: "No cross-role signal detected."

**AMEND** (required):

> **AMEND**
> - Add reviewer: `/crew-review [artifact] --amend add:[role-name]`
> - Full registry: `/crew-review [artifact] --depth deep`
> - Scope to domain: `/crew-review [artifact] --amend scope:[domain]`
> - Re-run single role: `/crew-review [artifact] --amend rerun:[role-name]`

---

---

## V-04

**Axes**: Inertia framing + Output format (gate exit condition tied to row production)
**Hypothesis**: The most direct path to C-17 + C-18 simultaneously is to define the
challenger phase exit condition in terms of row production: the gate does not close until
every unfilled slot has been promoted to a dedicated matrix row. This creates a causal
link -- the gate is satisfied by the C-18 artifact (the separate row), not by the
declaration that escalation happened. If the gate exits and domain review begins, then
by the gate's own definition every unfilled slot has already produced a row; C-18 is
therefore enforced by the gate mechanism itself, not by a separate instruction. C-17
and C-18 become mutually reinforcing: satisfying C-17 requires satisfying C-18.

---

You are running `/crew-review`.

This skill executes in three phases. Each phase has named entry and exit conditions.
Do not begin a phase until its entry condition is satisfied.

---

### PHASE 1 -- LOAD

**Entry**: artifact provided
**Exit**: role pool locked and verified

**L1** Open `.craft/roles/`. Read every file.
**L2** Extract from each file: role name, `archetype`, `lens.verify`, `expertise.relevance`.
**L3** Error halts -- unconditional, no fallback, no partial execution:
  - Directory absent: `ERROR: .craft/roles/ not found.` Halt.
  - Directory empty: `ERROR: .craft/roles/ is empty.` Halt.
  - Any file missing `lens.verify` or `expertise.relevance`:
    `ERROR: [role-name] missing required fields. Registry malformed.` Halt.
**L4** Role pool = all roles found. Pool is now locked. Zero roles may be invented.

---

### PHASE 2 -- CHALLENGER BRACKET

**Entry**: PHASE 1 exit
**Gate G1** -- challenger bracket gate

G1 exit condition (all must be true before PHASE 3 may begin):
1. All roles with `archetype: challenger` have run.
2. The null hypothesis 4-slot form has been attempted for each challenger role.
3. For each slot that could not be filled: a **dedicated, separate matrix row** exists
   in the output -- a full 4-column row (Role, Findings, Severity, Recommendation)
   following the same schema as domain findings, with severity HIGH.
4. No unfilled slot has been handled by inline sentence, appended note, or collapse
   with another slot.
5. No slot has been silently omitted.

**Domain review does not begin until G1 exits.**

---

**C1** Identify all roles in the pool with `archetype: challenger`.

**C2** For each challenger role, fill this null hypothesis 4-slot form:

```
SLOT-A: We currently do [______] instead of building this.
SLOT-B: The cost of that alternative is [______].
SLOT-C: The switching cost to adopt this artifact is [______].
SLOT-D: This artifact is worth acting on only if [______].
```

**C3** Fill each slot from artifact content or inferable workspace context.

**C4** Slot-to-row escalation (applies to each slot individually, required for G1 exit):
- Slot that cannot be filled: write `[not stated in artifact]` in that slot AND produce
  a dedicated separate matrix row:

  | `[role-name]` | SLOT-[letter] gap: [slot label] not stated. Null hypothesis is incomplete. | HIGH | Add [slot requirement] to artifact explicitly before committing to crew review. |

  This row must appear in the matrix. It must be its own row, not a sentence within
  the challenger's primary Findings cell. Two unfilled slots = two separate rows.
  Generic placeholders count as unfilled.

**C5** Challenger severity for the primary row:
  - HIGH: inertia case is credible and unaddressed
  - MEDIUM: inertia named but switching cost not quantified
  - LOW: artifact directly neutralizes the status quo

**C6** Verify G1 exit condition. All 5 conditions true? G1 exits. Proceed to PHASE 3.
     Any condition false? Return to C2 and resolve before proceeding.

---

### PHASE 3 -- DOMAIN REVIEW AND OUTPUT

**Entry**: G1 exits (PHASE 2 exit)

**Depth selection**:
- Standard (default): select 2-3 non-challenger roles whose `expertise.relevance`
  intersects the artifact type. Document each: "[role]: selected because [reason]."
- `--depth deep`: all non-challenger roles run.

**Per domain role**:
1. Apply only that role's `lens.verify` perspective.
2. Name a specific artifact surface in each finding.
3. Severity: exactly HIGH, MEDIUM, or LOW only.
4. Recommendation: one action naming what to do and where.
5. Do not repeat a finding already raised by a prior reviewer.

**Output**:

Write the review matrix as a 4-column table:

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|

Row order:
1. Challenger primary row(s) from PHASE 2
2. Slot-gap escalation rows (one per unfilled slot, in slot-letter order)
3. Domain rows in selection order

**Cross-role synthesis** (required, 2-3 sentences): name at least one convergence or
conflict. Slot-gap rows count as findings for convergence detection. If absent:
"No cross-role signal detected -- findings are non-overlapping."

**AMEND** (required):

> **AMEND**
> - Add a reviewer: `/crew-review [artifact] --amend add:[role-name]`
> - Full registry run: `/crew-review [artifact] --depth deep`
> - Restrict to domain: `/crew-review [artifact] --amend scope:[domain]`
> - Reopen G1 (re-run challenger bracket): `/crew-review [artifact] --amend rerun:challengers`

---

---

## V-05

**Axes**: Output format + Inertia framing + Role sequence (C-17 + C-18 + C-19 maximal)
**Hypothesis**: The three new aspirational criteria can be achieved simultaneously in a
single coherent design by combining: (1) a typed 5-column schema where every column
definition names its excluded anti-pattern (C-13 + C-19), (2) a named challenger bracket
phase with an explicit exit gate defined in terms of dedicated row production (C-15 +
C-17 + C-16 + C-18), and (3) a Lens column that requires one-sentence perspective
declarations traceable to each role's `lens.verify` (C-12). The hypothesis is that these
three mechanisms are mutually reinforcing rather than conflicting: the schema's column
constraints enforce C-19 at the cell level, the gate's exit condition enforces C-18 at
the phase level, and the Lens column enforces C-12 at the row level. Together they
produce a review where every failure mode named by the rubric is caught by a structural
mechanism, not by instruction proximity.

---

You are running `/crew-review`.

Reviews execute in archetype-group sequence. Output schema is declared before execution.
All rows are validated against schema constraints -- including anti-pattern exclusions --
before being written. The challenger bracket closes under a named exit gate; domain review
does not begin until the gate exits.

---

### Output schema (declare before executing)

The final output is a 5-column markdown table.

| Column | Type -- valid | Anti-pattern excluded (NOT valid) |
|--------|--------------|-----------------------------------|
| Role | string -- filename stem from `.craft/roles/` at execution time | NOT: invented names; names from memory or prior runs; any name not in the registry |
| Lens | string -- one sentence: "As a [role], I care about [specific concern from `lens.verify`]" | NOT: generic restatements ("As a PM, I review as a PM"); NOT: concerns from another role's lens; NOT: multi-sentence declarations |
| Findings | string -- names a specific artifact surface: section title, field name, diagram element, or named assumption | NOT: abstract observations without a named surface ("needs more detail", "unclear", "incomplete"); NOT: observations about the artifact as a whole without a specific surface |
| Severity | enum -- exactly `HIGH`, `MEDIUM`, or `LOW`; HIGH = blocks commitment; MEDIUM = must resolve before ship; LOW = advisory | NOT: freestyle labels (Critical, Minor, Warning, Blocker); NOT: blank cells; NOT: combinations |
| Recommendation | string -- names (1) what to do and (2) where in the artifact | NOT: generic directives ("review this", "improve this section", "consider adding"); NOT: recommendations without a named artifact location |

Per-row validation gate: before writing any row, verify all five cells against their
constraints, including anti-pattern exclusions. Revise any failing cell before writing.

---

### PHASE 1 -- LOAD

**Entry**: artifact provided
**Exit**: role pool locked and verified

**L1** Open `.craft/roles/`. Read every file.
**L2** Extract: role name, `archetype`, `lens.verify`, `expertise.relevance`.
**L3** Error halts -- unconditional, no soft fallback:
  - Directory absent: `ERROR: .craft/roles/ not found.` Halt.
  - Directory empty: `ERROR: .craft/roles/ is empty.` Halt.
  - Any file missing `lens.verify` or `expertise.relevance`:
    `ERROR: [role-name] missing required fields. Registry malformed.` Halt.
**L4** Role pool = all roles found. Pool locked. Zero roles may be invented.

---

### PHASE 2 -- CHALLENGER BRACKET

**Entry**: PHASE 1 exit
**Gate G1** -- challenger bracket gate

**G1 exit condition** (all must be true before PHASE 3 begins):
1. All roles with `archetype: challenger` have run.
2. Null hypothesis 4-slot form attempted for each challenger role.
3. For every slot that could not be filled from the artifact: a **dedicated, separate
   matrix row** exists -- a full 5-column row following the output schema above, with
   Severity = HIGH. This row is in the matrix. It is not a sentence inside another
   row's Findings cell. It is not an appended note.
4. No unfilled slot has been silently omitted, collapsed, or approximated.

**Domain review does not begin until G1 exits.**

---

**C1** Identify all roles with `archetype: challenger` in the pool.

**C2** For each challenger role, fill this null hypothesis 4-slot form:

```
SLOT-A: We currently do [______] instead of building this.
SLOT-B: The cost of that alternative is [______].
SLOT-C: The switching cost to adopt this artifact is [______].
SLOT-D: This artifact is worth acting on only if [______].
```

**C3** Fill each slot from artifact content or inferable workspace context.

**C4** For each unfilled slot -- slot-to-row escalation (required for G1 exit):
  1. Write `[not stated in artifact]` in that slot position.
  2. Produce a dedicated separate matrix row:
     - Role: `[challenger-role-name]`
     - Lens: "As a [role], I care about whether the null hypothesis can be stated
       completely -- SLOT-[letter] is missing."
     - Findings: "SLOT-[letter] gap: [slot label] not stated in the artifact.
       Null hypothesis is incomplete without this field."
     - Severity: HIGH
     - Recommendation: "State [slot requirement] explicitly in [artifact section]
       before this artifact proceeds to domain review."
  3. Apply per-row validation gate to this row before writing.
  4. Generic placeholders count as unfilled. Two unfilled slots = two separate rows.

**C5** Challenger primary row severity:
  - HIGH: inertia case is credible and unaddressed
  - MEDIUM: inertia named but switching cost not quantified
  - LOW: artifact directly neutralizes the status quo

**C6** Apply per-row validation gate to the challenger primary row before writing.

**C7** Verify G1 exit condition. All 4 conditions true? G1 exits.
     Any condition false? Resolve before proceeding to PHASE 3.

---

### PHASE 3 -- DOMAIN REVIEW

**Entry**: G1 exits (PHASE 2 exit)

**D1** Depth selection:
  - Standard (default): from roles NOT in `archetype: challenger`, select those whose
    `expertise.relevance` intersects the artifact type. Target 2-4 total. Document each:
    "[role]: selected because [reason tied to artifact]."
  - `--depth deep`: all non-challenger roles run.

**D2** Assign each selected role to its archetype group. Execute in group order:
  - Group 2: `archetype: product`
  - Group 3: `archetype: technical`
  - Group 4: `archetype: quality`
  - Group 5: all other archetypes; roles with no archetype field appended here

  Within each group: alphabetical by role name.

**D3** For each selected role, in execution order:
  1. Lens cell: "As a [role], I care about [specific concern from this role's lens.verify]."
     -- no generic restatement; concern must be traceable to this role's documented lens.
  2. Findings cell: name a specific artifact surface. No abstract observations.
     No repeating a finding already raised by a prior reviewer.
  3. Severity: exactly HIGH, MEDIUM, or LOW -- no other values.
  4. Recommendation: what to do + where in the artifact -- no generic directive.
  5. Apply per-row validation gate before writing the row.

---

### PHASE 4 -- RENDER

**Entry**: all rows complete (PHASE 3 exit)
**Exit**: output delivered

**R1** Header:

```
Crew Review: [artifact name or type]
Depth: standard | deep
Groups run: [list]
Roles: [list in execution order]
```

**R2** Review matrix (5 columns, rows in execution order):

| Role | Lens | Findings | Severity | Recommendation |
|------|------|----------|----------|----------------|

Row order:
1. Challenger primary row(s) from PHASE 2
2. Slot-gap escalation rows (one per unfilled slot, in slot-letter order)
3. Domain rows in group order

**R3** Cross-role synthesis (required, 2-3 sentences): name at least one convergence
(two roles raised the same concern) or one conflict (two roles disagree). Slot-gap rows
count as findings for convergence detection. If absent: "No cross-role signal detected --
findings are non-overlapping."

**R4** AMEND (required):

> **AMEND**
> - Add reviewer (inserted by archetype group): `/crew-review [artifact] --amend add:[role-name]`
> - Full registry: `/crew-review [artifact] --depth deep`
> - Scope to group: `/crew-review [artifact] --amend scope:group[N]`
> - Reopen G1 (re-run challenger bracket): `/crew-review [artifact] --amend rerun:challengers`
> - Re-run single role: `/crew-review [artifact] --amend rerun:[role-name]`

---
