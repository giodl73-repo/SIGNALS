---
skill: quest-variate
skill_target: crew-review
date: 2026-03-16
round: 7
rubric: crew-review-rubric-v6-2026-03-16.md
---

# crew-review -- Variate R7

5 complete prompt body variations. Single-axis first (V-01 through V-03), then
two-axis combinations (V-04, V-05).

**R7 design target**: R6 introduced C-22 (slot-anchored matrix with numbered cross-references)
and C-23 (validation as a named discrete execution phase). No R6 variation achieved both
simultaneously: V-03 passed C-22 (Slot column + slot-number synthesis) but failed C-23;
V-02 passed C-23 (PHASE 4 VALIDATE) but failed C-22. Additionally, C-12 (per-role lens-lock
declaration) failed across all five R6 variations -- it is the only aspirational criterion
never achieved in any round. R7 targets three open gaps:

- V-01: Slot-anchored matrix (single axis) -- strengthens C-22 by making the Slot column a
  typed schema column with its own contract, and requiring slot-number references in synthesis
  and AMEND as a typed output obligation, not a convention. R6 V-03 achieved C-22 incidentally
  via the execution manifest; V-01 R7 makes it load-bearing by design.
- V-02: Named VALIDATE phase with Lens column (single axis) -- adds Lens as a typed schema
  column with anti-pattern exclusion to the R6 V-02 five-phase structure. Targets C-23 (VALIDATE
  phase, inherited), C-12 (Lens column forces per-role lens-lock), and C-19 (Lens column
  definition names anti-pattern exclusion). Tests whether C-12 can be satisfied by elevating
  Lens from an execution instruction to a required schema column.
- V-03: Lens as typed schema column (single axis) -- isolated lens-column axis. Five-column
  schema includes Lens with typed contract and anti-pattern exclusion. No Slot column, no
  named VALIDATE phase. Clean single-axis test of whether schema elevation of Lens achieves
  C-12 and C-19 without introducing confounding changes.
- V-04: Slot-anchored + Named VALIDATE phase (two axes) -- combines V-01 and V-02 mechanisms
  to achieve C-22 + C-23 simultaneously. Tests structural independence: the Slot column is a
  matrix-schema property; the VALIDATE phase is an execution-model property. They should not
  interfere.
- V-05: Slot + VALIDATE + Lens maximal (three axes) -- targets the full aspirational stack
  including all three persistent gaps. Six-column schema: Slot, Role, Lens, Findings, Severity,
  Recommendation. Named VALIDATE phase. Slot manifest with downstream slot-number references.
  Also carries the full prior aspirational stack from R5 V-05 (C-11 through C-21).

Registry context assumed: `.craft/roles/` contains `inertia-advocate.md`, `pm.md`,
`architect.md` (and whatever else the workspace adds). Role files include `archetype`,
`lens.verify`, `expertise.relevance` fields.

---

## V-01

**Axis**: Role sequence (slot-anchored matrix as typed schema obligation)
**Hypothesis**: R6 V-03 achieved C-22 because its execution manifest assigned slot numbers
and its synthesis block referenced them -- but this was a consequence of the manifest
architecture, not a designed constraint. The Slot column existed; slot-number references in
synthesis appeared because the manifest primed them. The weakness: if the model omits the
manifest or skips the slot-reference obligation in synthesis, C-22 fails silently. This
variation makes C-22 structurally mandatory by (1) declaring Slot as a typed schema column
with its own contract before execution begins, (2) defining slot-number assignment rules as
part of the schema, and (3) making slot-number reference in synthesis and AMEND a typed
output requirement -- not a convention. The schema says: synthesis MUST reference slot numbers
when naming convergences or conflicts; AMEND options MUST use slot numbers when targeting
specific findings. The hypothesis is that typed output obligations produce more reliable
C-22 satisfaction than execution-manifest conventions, because a typed contract is checked at
output construction time while a convention is recalled at synthesis-generation time.

---

You are running `/crew-review`.

Route the artifact through the org registry. Output is a typed artifact defined by the schema
below. Execution order is declared as a numbered manifest before any role runs.

---

### Output schema (declare before executing)

The review artifact uses a 5-column matrix. Column contracts are binding:

| Column | Type -- valid | Contract detail |
|--------|--------------|-----------------|
| Slot | integer -- assigned sequentially from 1; Slot 1 = challenger bracket | One integer per row. Slot-gap escalation rows inherit the Slot number of their parent challenger row (e.g., "1a", "1b"). Domain rows are numbered 2, 3, ... in manifest order. |
| Role | string -- filename stem from `.craft/roles/` at execution time | NOT: invented names; names recalled from prior runs; any name absent from the registry at this execution. |
| Findings | string -- names a specific artifact surface: section title, field name, diagram element, or named assumption | NOT: abstract observations without a named surface ("needs more detail", "unclear", "incomplete"). |
| Severity | enum -- exactly `HIGH`, `MEDIUM`, or `LOW` | HIGH = blocks commitment; MEDIUM = conditions commitment; LOW = advisory. NOT: freestyle labels; blank cells; combinations. |
| Recommendation | string -- names (1) what to do and (2) where in the artifact | NOT: generic directives ("review this section", "consider improving", "needs clarification"). |

**Synthesis output contract**: The cross-role synthesis block MUST reference slot numbers when
naming convergences or conflicts. Format: "Slot [N] and Slot [M] both find..." or "Slot [N]
conflicts with Slot [M] on...". Synthesis using only role names -- without slot numbers --
does not satisfy the synthesis output contract. If no convergence or conflict exists:
`No cross-role signal detected -- findings are non-overlapping.`

**AMEND output contract**: Each AMEND option that targets a specific finding or role MUST name
the slot number. Format: `--amend add:slot[N+1]:[role-name]` or `--amend rerun:slot[N]`.
Generic AMEND options (full registry run, scope restriction) do not require slot numbers.

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

### Step 2 -- Declare slot manifest

Before any role runs, write the slot manifest. The manifest assigns a slot number to every
role that will execute. The manifest is committed before execution begins.

```
Slot manifest -- crew-review
Depth: [standard | deep]
Artifact type: [inferred from artifact]

Slot 1:  [challenger-role-name] (archetype: challenger)
Slot 2:  [role-name] (archetype: [type]) -- selected because [reason tied to artifact]
Slot 3:  [role-name] (archetype: [type]) -- selected because [reason tied to artifact]
...
```

Assignment rules:
- Slot 1: all roles with `archetype: challenger`. If multiple challengers exist, they share
  Slot 1 and run sequentially within it.
- Slots 2-N (standard): 2-3 non-challenger roles whose `expertise.relevance` intersects the
  artifact type. Ranked by relevance strength; highest = Slot 2.
- Slots 2-N (deep): all non-challenger roles, ranked by relevance then alphabetical.

The manifest is locked after writing. Roles absent from the manifest may not appear in the
matrix. Roles in the manifest may not be skipped.

---

### Step 3 -- Challenger bracket (Slot 1)

**Gate G1 state: OPEN.** Domain review is blocked until G1 closes.

**G1 closure predicate** -- G1 transitions OPEN -> CLOSED when ALL hold:
1. All Slot 1 roles have run.
2. The null hypothesis 4-slot form has been attempted for each Slot 1 role.
3. Every slot that could not be filled has produced a separate dedicated matrix row per
   the slot-to-row escalation rule below.
4. No slot was silently omitted, collapsed with another slot, or approximated with a
   generic placeholder ("some cost", "existing workflow", "the current process").
5. G1 state has been explicitly evaluated and written: `[G1: CLOSED]`.

**Domain review does not begin until G1 transitions to CLOSED.**

---

For each Slot 1 role, fill the null hypothesis 4-slot form:

> - **[SLOT-A]** We currently do ________ instead of building this.
> - **[SLOT-B]** The cost of that alternative is ________.
> - **[SLOT-C]** The switching cost to adopt this artifact is ________.
> - **[SLOT-D]** This artifact is worth acting on only if ________.

Fill from artifact content or inferable workspace context.

**Slot-to-row escalation rule** -- mandatory, per slot:
When a slot cannot be filled:
1. Write `[not stated in artifact]` in that slot position.
2. Produce a **separate, dedicated matrix row** assigned to Slot 1 (sub-lettered: 1a, 1b,
   etc.) with these cells:
   - Slot: `1[letter]` (e.g., 1a for SLOT-A gap)
   - Role: `[challenger-role-name]`
   - Findings: `SLOT-[letter] gap: [slot label] not stated in artifact. Null hypothesis is
     incomplete without this.`
   - Severity: `HIGH`
   - Recommendation: `State [slot requirement] explicitly in the artifact before proceeding.`
3. **Do not embed this finding as a sentence within the challenger row's Findings cell.**
   A sentence inside another row's Findings cell is not a dedicated row and does not satisfy
   G1 closure condition 3.
4. **Do not append this as a note or comment below the challenger row.** An appended note
   is not a matrix row and does not satisfy G1 closure condition 3.
5. Each unfilled slot = one dedicated row. Two unfilled slots = two rows.

Verify G1 closure predicate. All 5 conditions true? Write `[G1: CLOSED]`. Proceed to Step 4.

---

### Step 4 -- Domain review (Slots 2-N)

**Entry condition: G1 is CLOSED.**

Execute each slot in manifest order. For each:
1. Apply only that role's `lens.verify` perspective.
2. Name a specific artifact surface in the Findings cell.
3. Severity: exactly HIGH, MEDIUM, or LOW.
4. Recommendation: what to do + where.
5. Do not repeat a finding raised by a lower-numbered slot.

---

### Step 5 -- Output

Write the review matrix (5-column schema from the output contract above):

| Slot | Role | Findings | Severity | Recommendation |
|------|------|----------|----------|----------------|

Row order:
1. Slot 1 primary row(s)
2. Slot-gap escalation rows (Slot 1a, 1b, ... in slot-letter order)
3. Slots 2-N in manifest order

**Cross-role synthesis** (required -- must satisfy synthesis output contract):
Reference slot numbers. "Slot [N] and Slot [M] both find [shared concern]." Name at least
one convergence or conflict. Slot-gap rows count as findings. If absent:
`No cross-role signal detected -- findings are non-overlapping.`

**AMEND** (required -- must satisfy AMEND output contract):

> **AMEND**
> - Add to manifest as Slot [N+1]: `/crew-review [artifact] --amend add:slot[N+1]:[role-name]`
> - Rerun Slot 1 (challenger bracket): `/crew-review [artifact] --amend rerun:slot1`
> - Full manifest: `/crew-review [artifact] --depth deep`
> - Restrict to Slots 1-2: `/crew-review [artifact] --amend scope:[domain]`

---

---

## V-02

**Axis**: Lifecycle emphasis (named VALIDATE phase with Lens as typed column)
**Hypothesis**: R6 V-02 achieved C-23 (VALIDATE as named phase) but failed C-12 (per-role
lens-lock) because the Lens declaration was an execution instruction buried in the domain
review step -- the model was told to "apply only that role's lens.verify perspective" but
not required to produce a visible lens statement in the output. C-12 requires a lens
declaration that is visible in the output as a declared constraint before that role's findings.
The repair: elevate Lens from an execution instruction to a required output schema column,
with its own typed contract and anti-pattern exclusion. A schema column is checked at
output-construction time; an execution instruction is recalled during generation. This
variation inherits R6 V-02's five-phase structure (LOAD, CHALLENGE, REVIEW, VALIDATE, AMEND)
and adds a 5-column output schema that includes Lens as a first-class column -- before
Findings, after Role. The VALIDATE phase checks all five columns including the Lens cell.
The hypothesis is that (a) the named VALIDATE phase reliably achieves C-23, (b) the Lens
schema column reliably achieves C-12, and (c) the Lens column definition with anti-pattern
exclusion achieves C-19, all without structural interference.

---

You are running `/crew-review`.

This skill executes in five lifecycle phases. Complete each phase in order. Phase entry
conditions are enforced. The output schema is declared before execution begins.

---

### Output schema (declared before PHASE 1 executes)

The review artifact is a 5-column matrix. All column contracts are binding. The VALIDATE
phase checks every cell against these contracts before the matrix is written.

| Column | Type -- valid | Anti-pattern excluded |
|--------|--------------|----------------------|
| Role | string -- filename stem from `.craft/roles/` at execution time | NOT: invented names; names recalled from prior runs; any name not in the registry at this execution |
| Lens | string -- one sentence: "As a [role], I care about [specific concern traceable to this role's `lens.verify`]." | NOT: generic role restatements ("As a PM, I review as a PM"); NOT: concerns borrowed from another role's lens; NOT: multi-sentence declarations; NOT: lens cells that merely restate the role name |
| Findings | string -- names a specific artifact surface: section title, field name, diagram element, or named assumption | NOT: abstract observations without a named surface ("needs more detail", "unclear", "incomplete", "could be improved") |
| Severity | enum -- exactly `HIGH`, `MEDIUM`, or `LOW`; HIGH = blocks commitment; MEDIUM = conditions commitment; LOW = advisory | NOT: freestyle labels (Critical, Minor, Warning, Blocker); NOT: blank cells; NOT: combinations |
| Recommendation | string -- names (1) what to do and (2) where in the artifact | NOT: generic directives ("review this", "improve this section", "consider adding") |

---

### PHASE 1 -- LOAD

**Entry**: artifact provided
**Exit**: role pool locked

Read every file in `.craft/roles/`. Extract: role name, `archetype`, `lens.verify`,
`expertise.relevance`.

Error halts -- unconditional, no soft fallback:
- Directory absent: `ERROR: .craft/roles/ not found.` Halt.
- Directory empty: `ERROR: .craft/roles/ is empty.` Halt.
- Any file missing `lens.verify` or `expertise.relevance`:
  `ERROR: [role-name] missing required fields. Registry malformed.` Halt.

Role pool = all files found. Pool locked. Zero roles may be invented.

---

### PHASE 2 -- CHALLENGE

**Entry**: PHASE 1 exit (role pool locked)
**Gate G1 state: OPEN** -- domain review is blocked until G1 closes.

**G1 closure predicate** -- G1 transitions OPEN -> CLOSED when ALL hold:
1. All roles with `archetype: challenger` in the pool have run.
2. The null hypothesis 4-slot form has been attempted for each challenger role.
3. Every slot that could not be filled has produced a separate, dedicated matrix row per
   the slot-to-row escalation rule below.
4. No slot was silently omitted, collapsed with another slot, or approximated with a
   generic placeholder ("some cost", "existing workflow").
5. G1 state has been explicitly evaluated and written: `[G1: CLOSED]`.

**Domain review does not begin until G1 transitions to CLOSED.**

---

For each challenger role, fill the null hypothesis 4-slot form:

> - **[SLOT-A]** We currently do ________ instead of building this.
> - **[SLOT-B]** The cost of that alternative is ________.
> - **[SLOT-C]** The switching cost to adopt this artifact is ________.
> - **[SLOT-D]** This artifact is worth acting on only if ________.

Fill from artifact content or inferable workspace context.

**Slot-to-row escalation rule** -- mandatory, per slot:
When a slot cannot be filled:
1. Write `[not stated in artifact]` in that slot position.
2. Produce a **separate, dedicated matrix row**:
   - Role: `[challenger-role-name]`
   - Lens: "As a [role], I care about null hypothesis completeness -- SLOT-[letter] cannot
     be evaluated."
   - Findings: `SLOT-[letter] gap: [slot label] not stated in artifact. Null hypothesis
     is incomplete without this.`
   - Severity: `HIGH`
   - Recommendation: `State [slot requirement] explicitly in the artifact before
     proceeding to domain review.`
3. **Do not embed this finding as a sentence within the challenger row's Findings cell.**
   A sentence inside another row's Findings cell is not a dedicated row and does not satisfy
   G1 closure condition 3.
4. **Do not append this as a note or comment below the challenger row.** An appended note
   is not a matrix row and does not satisfy G1 closure condition 3.
5. Each unfilled slot = one dedicated row. Two unfilled slots = two rows.

Challenger primary row:
- Lens: "As a [role], I care about [specific concern from this role's `lens.verify`]."
- Findings: the filled/attempted 4-slot form plus the challenger's primary concern.
- Severity: HIGH (inertia credible, unaddressed) / MEDIUM (named, cost unstated) /
  LOW (artifact neutralizes status quo).
- Recommendation: one concrete action naming what to do and where.

Verify G1 closure predicate. All 5 conditions true? Write `[G1: CLOSED]`. Proceed to PHASE 3.

---

### PHASE 3 -- REVIEW

**Entry**: G1 is CLOSED (PHASE 2 exit)

Depth selection:
- Standard (default): 2-3 non-challenger roles whose `expertise.relevance` intersects the
  artifact type. Document each: "[role]: selected because [reason]."
- `--depth deep`: all non-challenger roles run.

For each selected domain role, collect a draft row:
1. Lens cell: "As a [role], I care about [specific concern from this role's `lens.verify`]."
   The concern must be traceable to this role's documented lens -- not a generic observer view.
2. Findings cell: name a specific artifact surface. Do not repeat a finding already raised.
3. Severity: exactly HIGH, MEDIUM, or LOW.
4. Recommendation: what to do + where.

Collect all rows (challenger primary, slot-gap escalation, domain) into a draft matrix.
Do not write the final output yet -- PHASE 4 validates the draft first.

---

### PHASE 4 -- VALIDATE

**Entry**: all rows collected (PHASE 3 exit)
**Exit**: every row validated; matrix ready to write

For each row in the draft matrix, check all five cells against the output schema above:
- Role cell: filename stem exists in `.craft/roles/` at this execution -- not invented.
- Lens cell: one sentence, "As a [role], I care about [specific concern from lens.verify]."
  If the Lens cell is a generic restatement of the role name, revise it before writing.
- Findings cell: names a specific artifact surface -- not abstract. If abstract, revise.
- Severity cell: exactly HIGH, MEDIUM, or LOW. If not, revise.
- Recommendation cell: names what to do + where. If generic, revise.

A row that cannot be made to pass validation is removed from the draft matrix and logged as:
`[VALIDATION REMOVED: [role] -- [reason]]`

Write the validated matrix:

| Role | Lens | Findings | Severity | Recommendation |
|------|------|----------|----------|----------------|

Row order:
1. Challenger primary row(s) from PHASE 2
2. Slot-gap escalation rows (one per unfilled slot, in slot-letter order)
3. Domain rows in selection order

---

### PHASE 5 -- AMEND

**Entry**: PHASE 4 exit (matrix validated and written)
**Output contract**: at least 4 amendment options; at least one is derived from a HIGH
finding or unfilled slot found in this review run.

Write cross-role synthesis (required, 2-3 sentences) before AMEND: name at least one
convergence (two roles raised the same concern) or one conflict (two roles disagree). Slot-gap
rows count as findings for convergence detection. If absent:
`No cross-role signal detected -- findings are non-overlapping.`

Derive AMEND options from review results:
- For each unfilled slot: include option to re-open G1 for that specific slot.
- For each HIGH domain finding: include option to add a reviewer from the relevant domain.
- Always include: full registry run and scope-restriction options.

Write the AMEND section:

> **AMEND**
> - [derived option 1: specific to this review's findings]
> - [derived option 2: specific to this review's findings]
> - Full registry run: `/crew-review [artifact] --depth deep`
> - Restrict scope: `/crew-review [artifact] --amend scope:[domain]`
> - Re-open G1: `/crew-review [artifact] --amend rerun:challengers`

Each option must name the role, slot, or section it targets.

---

---

## V-03

**Axis**: Output format (Lens as typed schema column with anti-pattern exclusion)
**Hypothesis**: C-12 requires each reviewer row to be preceded by or opened with a one-sentence
lens declaration traceable to that role's `lens.verify`. In every prior variation, the lens
declaration is an execution instruction: "apply only that role's lens.verify perspective" or
"before writing findings, state the lens." Execution instructions are recalled during
generation; they are not structural constraints on the output. If the model treats the lens
declaration as optional or elides it under context pressure, C-12 fails silently -- there is
no schema violation, only a missing instruction-follower. This variation tests whether
elevating Lens to a required output schema column changes the reliability profile for C-12.
A 5-column schema (Role, Lens, Findings, Severity, Recommendation) makes every row require
a Lens cell. The Lens column definition includes an explicit anti-pattern exclusion: "NOT:
generic role restatements." This produces C-12 (visible lens declaration per row) and C-19
(anti-pattern named in column definition) simultaneously. No Slot column, no named VALIDATE
phase -- clean single-axis isolation of the Lens-column mechanism.

---

You are running `/crew-review`.

Route the artifact through the org registry. Output is a 5-column matrix. The Lens column
is required for every row.

---

### Output schema

The review matrix uses five columns. Column contracts are binding on every row:

| Column | Type -- valid | Anti-pattern excluded |
|--------|--------------|----------------------|
| Role | string -- filename stem from `.craft/roles/` at execution time | NOT: invented names; names from memory or prior runs |
| Lens | string -- one sentence: "As a [role], I care about [specific concern traceable to this role's `lens.verify`]." The concern must be specific to this role's documented expertise -- not a generic observer concern. | NOT: generic role restatements ("As a PM, I review as a PM", "As an architect, I evaluate architecture"); NOT: concerns that are not traceable to this role's `lens.verify` field; NOT: multi-sentence declarations; NOT: absent Lens cells |
| Findings | string -- names a specific artifact surface: section title, field name, diagram element, or named assumption | NOT: abstract observations without a named surface ("needs more detail", "unclear", "incomplete") |
| Severity | enum -- exactly `HIGH`, `MEDIUM`, or `LOW`; HIGH blocks commitment; MEDIUM conditions commitment; LOW is advisory | NOT: freestyle labels; blank cells; combinations |
| Recommendation | string -- names (1) what to do and (2) where in the artifact | NOT: generic directives; recommendations without a named artifact location |

**Per-row validation gate**: Before writing any row, verify all five cells against their
column contracts including anti-pattern exclusions. If the Lens cell contains a generic
restatement, revise it before writing. Do not write a row with a failing Lens cell.

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

**Gate G1 state: OPEN.** Domain review is blocked until G1 closes.

**G1 closure predicate** -- G1 transitions OPEN -> CLOSED when ALL hold:
1. All roles with `archetype: challenger` in the pool have run.
2. The null hypothesis 4-slot form has been attempted for each challenger role.
3. Every slot that could not be filled has produced a dedicated, separate matrix row per
   the slot-to-row escalation rule below.
4. No slot was silently omitted, collapsed, or approximated with a generic placeholder
   ("some cost", "existing workflow", "the current process").
5. G1 has been explicitly evaluated and written: `[G1: CLOSED]`.

**Domain review does not begin until G1 transitions to CLOSED.**

---

For each challenger role, fill the null hypothesis 4-slot form:

> - **[SLOT-A]** We currently do ________ instead of building this.
> - **[SLOT-B]** The cost of that alternative is ________.
> - **[SLOT-C]** The switching cost to adopt this artifact is ________.
> - **[SLOT-D]** This artifact is worth acting on only if ________.

Fill from artifact content or inferable workspace context.

**Slot-to-row escalation rule** -- mandatory, per slot:
When a slot cannot be filled:
1. Write `[not stated in artifact]` in that slot position.
2. Produce a **separate, dedicated matrix row** -- a full 5-column row following the output
   schema above:
   - Role: `[challenger-role-name]`
   - Lens: "As a [role], I care about null hypothesis completeness -- SLOT-[letter] is
     missing."
   - Findings: `SLOT-[letter] gap: [slot label] not stated in artifact. Null hypothesis
     is incomplete without this.`
   - Severity: `HIGH`
   - Recommendation: `State [slot requirement] explicitly in the artifact before
     proceeding.`
3. **Do not embed this as a sentence within the challenger row's Findings cell.** A sentence
   inside another row's Findings cell is not a dedicated row and does not satisfy G1
   closure condition 3.
4. **Do not append this as a note below the challenger row.** An appended note is not a
   matrix row and does not satisfy G1 closure condition 3.
5. Each unfilled slot = one dedicated row. Two unfilled slots = two rows.

Apply per-row validation gate to each row before writing.

Verify G1 closure predicate. All 5 conditions true? Write `[G1: CLOSED]`. Proceed to Step 3.

---

### Step 3 -- Domain review

**Entry condition: G1 is CLOSED.**

Depth selection:
- Standard (default): 2-3 non-challenger roles whose `expertise.relevance` intersects the
  artifact type. Document each: "[role]: selected because [reason]."
- `--depth deep`: all non-challenger roles run.

For each selected role:
1. Lens cell: "As a [role], I care about [specific concern from this role's `lens.verify`]."
   Check against Lens column contract. Not a generic restatement -- revise before writing.
2. Findings cell: name a specific artifact surface. Do not repeat a finding already raised.
3. Severity: exactly HIGH, MEDIUM, or LOW.
4. Recommendation: what to do + where.
5. Apply per-row validation gate before writing.

---

### Step 4 -- Output

Write the review matrix (5-column schema):

| Role | Lens | Findings | Severity | Recommendation |
|------|------|----------|----------|----------------|

Row order:
1. Challenger primary row(s) from Step 2
2. Slot-gap escalation rows (one per unfilled slot, in slot-letter order)
3. Domain rows in selection order

**Cross-role synthesis** (required, 2-3 sentences): name at least one convergence (two roles
raised the same concern) or one conflict (two roles disagree). Slot-gap rows count as findings.
If absent: `No cross-role signal detected -- findings are non-overlapping.`

**AMEND** (required):

> **AMEND**
> - Add a reviewer: `/crew-review [artifact] --amend add:[role-name]`
> - Full registry: `/crew-review [artifact] --depth deep`
> - Scope to domain: `/crew-review [artifact] --amend scope:[domain]`
> - Re-open G1: `/crew-review [artifact] --amend rerun:challengers`

---

---

## V-04

**Axes**: Role sequence + Lifecycle emphasis (slot-anchored matrix + named VALIDATE phase)
**Hypothesis**: C-22 and C-23 are structurally independent: C-22 is a matrix-schema property
(the Slot column assigns numbered anchors; synthesis and AMEND use slot numbers), while C-23
is an execution-model property (validation is a named phase at the same level as CHALLENGE
and REVIEW). They were achieved separately in R6 V-03 (C-22) and R6 V-02 (C-23), which
suggests they emerged from different mechanisms with no structural coupling. This variation
tests whether they coexist without interference: a slot manifest and Slot column from
V-01 R7 is combined with the named VALIDATE phase from V-02 R6. The hypothesis is that
adding a Slot column to the output schema does not affect phase-level execution, and naming
VALIDATE as a discrete phase does not affect slot-number assignment or synthesis-contract
obligations. If both mechanisms operate independently, the variation should achieve C-22
and C-23 simultaneously for the first time.

---

You are running `/crew-review`.

This skill executes in five lifecycle phases. Execution order is declared as a numbered
slot manifest before PHASE 1. The output schema includes a Slot column. PHASE 4 validates
the draft matrix before it is written.

---

### Output schema (declared before execution)

The review artifact uses a 5-column matrix:

| Column | Type -- valid | Contract detail |
|--------|--------------|-----------------|
| Slot | integer or sub-lettered integer -- Slot 1 = challenger; 1a/1b = slot-gap escalation rows; 2, 3, ... = domain roles in manifest order | Assigned from the slot manifest. Every row has a Slot value. |
| Role | string -- filename stem from `.craft/roles/` at execution time | NOT: invented names; names not in the registry at this execution. |
| Findings | string -- names a specific artifact surface: section title, field name, diagram element, or named assumption | NOT: abstract observations without a named surface. |
| Severity | enum -- exactly `HIGH`, `MEDIUM`, or `LOW` | HIGH blocks commitment; MEDIUM conditions; LOW advisory. NOT: freestyle labels; blank cells. |
| Recommendation | string -- names (1) what to do and (2) where in the artifact | NOT: generic directives without a named artifact location. |

**Synthesis output contract**: synthesis MUST reference slot numbers when naming convergences
or conflicts. "Slot [N] and Slot [M] both find..." If absent:
`No cross-role signal detected -- findings are non-overlapping.`

**AMEND output contract**: options targeting specific findings MUST use slot numbers:
`--amend rerun:slot[N]` or `--amend add:slot[N+1]:[role-name]`.

---

### Slot manifest (declare before PHASE 1)

Write the slot manifest before any phase executes:

```
Slot manifest -- crew-review
Depth: [standard | deep]
Artifact type: [inferred]

Slot 1:  [challenger-role-name] (archetype: challenger)
Slot 2:  [role-name] (archetype: [type]) -- selected because [reason]
Slot 3:  [role-name] (archetype: [type]) -- selected because [reason]
...
```

Rules: Slot 1 = all challenger roles. Slots 2-N (standard) = 2-3 non-challenger roles ranked
by `expertise.relevance` relevance to artifact type. Slots 2-N (deep) = all non-challenger
roles. Manifest is locked before execution. Roles absent from manifest may not appear in
matrix.

---

### PHASE 1 -- LOAD

**Entry**: slot manifest declared
**Exit**: role pool locked

Read every file in `.craft/roles/`. Extract: role name, `archetype`, `lens.verify`,
`expertise.relevance`.

Error halts -- unconditional, no soft fallback:
- Directory absent: `ERROR: .craft/roles/ not found.` Halt.
- Directory empty: `ERROR: .craft/roles/ is empty.` Halt.
- Any file missing `lens.verify` or `expertise.relevance`:
  `ERROR: [role-name] missing required fields. Registry malformed.` Halt.

Role pool = all files found. Pool locked. Zero roles may be invented.

---

### PHASE 2 -- CHALLENGE

**Entry**: PHASE 1 exit (pool locked)
**Gate G1 state: OPEN.** Domain review blocked until G1 closes.

**G1 closure predicate** -- G1 transitions OPEN -> CLOSED when ALL hold:
1. All Slot 1 roles have run.
2. The null hypothesis 4-slot form has been attempted for each Slot 1 role.
3. Every slot that could not be filled has produced a separate, dedicated matrix row per
   the slot-to-row escalation rule below.
4. No slot was silently omitted, collapsed, or approximated with a generic placeholder.
5. G1 has been explicitly evaluated and written: `[G1: CLOSED]`.

**Domain review does not begin until G1 transitions to CLOSED.**

---

For each Slot 1 role, fill the 4-slot null hypothesis form:

> - **[SLOT-A]** We currently do ________ instead of building this.
> - **[SLOT-B]** The cost of that alternative is ________.
> - **[SLOT-C]** The switching cost to adopt this artifact is ________.
> - **[SLOT-D]** This artifact is worth acting on only if ________.

Fill from artifact content or inferable workspace context.

**Slot-to-row escalation rule** -- mandatory, per slot:
When a slot cannot be filled:
1. Write `[not stated in artifact]` in that slot position.
2. Produce a **separate, dedicated matrix row** -- full 5-column row:
   - Slot: `1[letter]` (e.g., 1a for SLOT-A gap)
   - Role: `[challenger-role-name]`
   - Findings: `SLOT-[letter] gap: [slot label] not stated in artifact. Null hypothesis
     is incomplete without this.`
   - Severity: `HIGH`
   - Recommendation: `State [slot requirement] explicitly in the artifact before
     proceeding to domain review.`
3. **Do not embed this finding as a sentence within the challenger row's Findings cell.**
   A sentence inside another row's Findings cell is not a dedicated row and does not satisfy
   G1 closure condition 3.
4. **Do not append as a note or comment below the challenger row.** An appended note is not
   a matrix row and does not satisfy G1 closure condition 3.
5. Each unfilled slot = one dedicated row. Two unfilled = two rows.

Challenger primary row Severity: HIGH (inertia credible, unaddressed) / MEDIUM (named, cost
unstated) / LOW (artifact neutralizes status quo).

Verify G1 closure predicate. All 5 conditions true? Write `[G1: CLOSED]`. Proceed to PHASE 3.

---

### PHASE 3 -- REVIEW

**Entry**: G1 is CLOSED (PHASE 2 exit)

Depth selection:
- Standard: 2-3 non-challenger roles (Slots 2-N from manifest) whose `expertise.relevance`
  intersects the artifact type.
- `--depth deep`: all non-challenger roles per manifest.

For each domain slot, collect a draft row:
1. Apply only that role's `lens.verify` perspective.
2. Name a specific artifact surface in Findings.
3. Severity: exactly HIGH, MEDIUM, or LOW.
4. Recommendation: what to do + where.
5. Do not repeat a finding raised by a lower-numbered slot.

Collect all rows into draft matrix. Do not write final output -- PHASE 4 validates first.

---

### PHASE 4 -- VALIDATE

**Entry**: all rows collected (PHASE 3 exit)
**Exit**: matrix validated and ready to write

For each row in the draft matrix, verify:
- Slot cell: integer or sub-lettered integer consistent with the manifest
- Role cell: filename stem exists in `.craft/roles/` -- not invented
- Findings cell: names a specific artifact surface -- not abstract
- Severity cell: exactly HIGH, MEDIUM, or LOW
- Recommendation cell: names what to do + where

Revise any failing cell before writing. A row that cannot pass validation is removed and
logged as: `[VALIDATION REMOVED: [role] -- [reason]]`

Write the validated matrix:

| Slot | Role | Findings | Severity | Recommendation |
|------|------|----------|----------|----------------|

Row order:
1. Slot 1 primary row(s)
2. Slot-gap escalation rows (Slot 1a, 1b, ... in slot-letter order)
3. Slots 2-N in manifest order

---

### PHASE 5 -- AMEND

**Entry**: PHASE 4 exit

**Cross-role synthesis** (required, 2-3 sentences -- must satisfy synthesis output contract):
Reference slot numbers. "Slot [N] and Slot [M] both find [shared concern]." Name at least one
convergence or conflict. Slot-gap rows count as findings. If absent:
`No cross-role signal detected -- findings are non-overlapping.`

**AMEND** (required -- must satisfy AMEND output contract):

> **AMEND**
> - Add to manifest as Slot [N+1]: `/crew-review [artifact] --amend add:slot[N+1]:[role-name]`
> - Rerun Slot 1 (challenger bracket): `/crew-review [artifact] --amend rerun:slot1`
> - Full manifest: `/crew-review [artifact] --depth deep`
> - Restrict to Slots 1-2: `/crew-review [artifact] --amend scope:[domain]`

---

---

## V-05

**Axes**: Role sequence + Lifecycle emphasis + Output format (slot-anchored + VALIDATE phase
+ Lens column -- maximal)
**Hypothesis**: Three persistent aspirational gaps remain unachieved in any single variation:
C-22 (slot-anchored matrix with numbered cross-references), C-23 (validation as a named
discrete execution phase), and C-12 (per-role lens-lock declaration). V-01 R7 isolates C-22;
V-02 R7 combines C-23 + C-12; V-04 R7 combines C-22 + C-23. No variation has attempted all
three simultaneously. This variation is the maximal combination: a 6-column output schema
(Slot, Role, Lens, Findings, Severity, Recommendation) carrying typed contracts with
anti-pattern exclusions for Lens and Findings columns; a numbered slot manifest; a named
VALIDATE phase; and the full prior aspirational stack from R5 V-05 (C-11 through C-21). The
hypothesis is that the three mechanisms are structurally independent and additive: the Slot
column is a schema property; the VALIDATE phase is an execution-model property; the Lens
column is a schema property. They should coexist without interference and produce simultaneous
satisfaction of C-12, C-22, and C-23 alongside the established aspirational stack.

---

You are running `/crew-review`.

This skill executes in five lifecycle phases. The output schema -- including a Slot column
and a Lens column -- is declared before execution begins. Execution order is declared as a
numbered slot manifest. PHASE 4 validates the draft matrix before final render.

---

### Output schema (declared before execution)

The review artifact is a 6-column matrix. All column contracts are binding. The per-row
validation gate in PHASE 4 enforces every cell against these contracts.

| Column | Type -- valid | Anti-pattern excluded |
|--------|--------------|----------------------|
| Slot | integer or sub-lettered integer -- Slot 1 = challenger bracket; 1a/1b/1c/1d = slot-gap escalation rows in slot-letter order; 2, 3, ... = domain roles in manifest order | NOT: absent Slot cells; NOT: non-integer labels; NOT: Slot values that conflict with the manifest |
| Role | string -- filename stem from `.craft/roles/` at execution time | NOT: invented names; names recalled from prior runs; any name not present in the registry at this execution |
| Lens | string -- one sentence: "As a [role], I care about [specific concern traceable to this role's `lens.verify`]." | NOT: generic role restatements ("As a PM, I review as a PM"); NOT: concerns not traceable to this role's `lens.verify` field; NOT: multi-sentence declarations; NOT: absent Lens cells; NOT: Lens cells that merely restate the role name |
| Findings | string -- names a specific artifact surface: section title, field name, diagram element, or named assumption | NOT: abstract observations without a named surface ("needs more detail", "unclear", "incomplete", "could be improved"); NOT: observations naming only the artifact as a whole |
| Severity | enum -- exactly `HIGH`, `MEDIUM`, or `LOW`; HIGH = blocks commitment; MEDIUM = conditions commitment; LOW = advisory | NOT: freestyle labels (Critical, Minor, Warning, Blocker, Moderate, Severe); NOT: blank cells; NOT: combinations ("HIGH/MEDIUM") |
| Recommendation | string -- names (1) what to do and (2) where in the artifact | NOT: generic directives ("review this", "improve this section", "consider adding", "needs clarification"); NOT: recommendations without a named artifact location |

**Synthesis output contract**: synthesis MUST reference slot numbers when naming convergences
or conflicts. "Slot [N] and Slot [M] both find..." Role-name-only references do not satisfy
this contract.

**AMEND output contract**: options targeting specific findings MUST use slot numbers.
`--amend rerun:slot[N]`, `--amend add:slot[N+1]:[role-name]`.

---

### Slot manifest (declare before PHASE 1)

Before any phase executes, write and commit the slot manifest:

```
Slot manifest -- crew-review
Depth: [standard | deep]
Artifact type: [inferred from artifact]

Slot 1:  [challenger-role-name] (archetype: challenger)
Slot 2:  [role-name] (archetype: [type]) -- selected because [reason tied to artifact]
Slot 3:  [role-name] (archetype: [type]) -- selected because [reason tied to artifact]
...
```

Rules: Slot 1 = all roles with `archetype: challenger`. Slots 2-N (standard) = 2-3
non-challenger roles ranked by `expertise.relevance` to artifact type. Slots 2-N (deep) =
all non-challenger roles ranked by relevance then alphabetical. Manifest is locked. Roles
absent from manifest may not appear in the matrix. Roles in the manifest may not be skipped.

---

### PHASE 1 -- LOAD

**Entry**: slot manifest committed
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

### PHASE 2 -- CHALLENGE

**Entry**: PHASE 1 exit (pool locked)
**Gate G1** -- challenger bracket gate

**G1 state: OPEN.** Domain review is blocked.

**G1 closure predicate** -- G1 transitions from OPEN to CLOSED when ALL hold:
1. All Slot 1 roles have run.
2. The null hypothesis 4-slot form has been attempted for each Slot 1 role.
3. For every slot that could not be filled: a dedicated, separate 6-column matrix row exists
   in the draft output, validated against the output schema above, Severity = HIGH.
4. No unfilled slot was silently omitted, collapsed into another slot, or approximated with
   a generic placeholder ("some cost", "the existing workflow", "the current process").

**Domain review does not begin until G1 transitions to CLOSED.**

---

**C1** Identify all Slot 1 roles (all roles with `archetype: challenger`).

**C2** For each Slot 1 role, fill the null hypothesis 4-slot form:

```
SLOT-A: We currently do [______] instead of building this.
SLOT-B: The cost of that alternative is [______].
SLOT-C: The switching cost to adopt this artifact is [______].
SLOT-D: This artifact is worth acting on only if [______].
```

**C3** Fill each slot from artifact content or inferable workspace context.

**C4** Slot-to-row escalation rule -- mandatory, applies to each slot individually:

When a slot cannot be filled:
1. Write `[not stated in artifact]` in that slot position in the 4-slot form.
2. Produce a **separate, dedicated matrix row** -- a full 6-column row following the output
   schema:
   - Slot: `1[letter]` (1a for SLOT-A gap, 1b for SLOT-B gap, etc.)
   - Role: `[challenger-role-name]`
   - Lens: "As a [role], I care about null hypothesis completeness -- SLOT-[letter] is
     missing from the artifact."
   - Findings: "SLOT-[letter] gap: [slot label] not stated in the artifact. Null hypothesis
     is incomplete without this field."
   - Severity: HIGH
   - Recommendation: "State [slot requirement] explicitly in [artifact section] before
     this artifact proceeds to domain review."
3. **Do not embed this finding as a sentence within the challenger row's Findings cell.**
   A sentence inside another row's Findings cell is not a dedicated row. A dedicated row
   is a full 6-column entry in the matrix. Anything else does not satisfy G1 closure
   condition 3.
4. **Do not append this as a note or comment below the challenger row.** An appended note
   is not a matrix row. It does not satisfy G1 closure condition 3.
5. Each unfilled slot = one dedicated row. Two unfilled slots = two separate rows.
6. Apply per-row validation gate (PHASE 4 contract) before writing this row.

**C5** Challenger primary row:
- Slot: 1
- Lens: "As a [role], I care about [specific concern from this role's `lens.verify`]."
- Findings: the filled/attempted 4-slot form plus the challenger's primary concern.
- Severity: HIGH (inertia credible, unaddressed) / MEDIUM (named, cost unstated) /
  LOW (artifact directly neutralizes status quo).
- Recommendation: one concrete action naming what to do and where.
- Apply per-row validation gate before writing.

**C6** Verify G1 closure predicate. All 4 conditions true?

Write: `[G1: CLOSED -- conditions 1-4 verified]`

**G1 state: CLOSED.** Proceed to PHASE 3.

---

### PHASE 3 -- REVIEW

**Entry**: G1 is CLOSED (PHASE 2 exit)

**D1** Depth selection:
- Standard (default): from non-Slot-1 roles, select those whose `expertise.relevance`
  intersects the artifact type. Target 2-4. Document each: "[role]: selected because [reason]."
- `--depth deep`: all non-Slot-1 roles per manifest.

**D2** Execute each slot in manifest order. For each slot:
1. Lens cell: "As a [role], I care about [specific concern from this role's `lens.verify`]."
   Check against Lens column anti-pattern exclusion. Not a generic restatement.
2. Findings cell: name a specific artifact surface. No abstract observations. No repeating
   a finding already raised by a lower-numbered slot.
3. Severity: exactly HIGH, MEDIUM, or LOW.
4. Recommendation: what to do + where in the artifact.

Collect all rows into draft matrix. Do not write final output -- PHASE 4 validates first.

---

### PHASE 4 -- VALIDATE

**Entry**: all rows collected (PHASE 3 exit)
**Exit**: verification complete; matrix ready for PHASE 5 render

For each row in the draft matrix, verify all six cells against the output schema:
- Slot: consistent with manifest; sub-lettered for slot-gap escalation rows
- Role: filename stem exists in `.craft/roles/` at this execution
- Lens: one sentence, traceable to `lens.verify`, not a generic restatement
- Findings: names a specific artifact surface, not abstract
- Severity: exactly HIGH, MEDIUM, or LOW
- Recommendation: names what to do + where

If a cell fails: revise before writing. A row that cannot pass is removed and logged:
`[VALIDATION REMOVED: [role] -- [reason]]`

Write a criterion-check table before writing the final matrix:

| Criterion | Description | Status | Evidence in this draft |
|-----------|-------------|--------|------------------------|
| C-11 | 4-slot null hypothesis form attempted; all slots filled or escalated | [YES/NO/PARTIAL] | [slot letters present, escalation rows count] |
| C-12 | Lens cell present and non-generic for every row | [YES/NO/PARTIAL] | [all rows have specific Lens / missing in [role]] |
| C-13 | Column contracts with per-row validation gate visible | [YES/NO/PARTIAL] | [schema table present / PHASE 4 validates before write] |
| C-15 | Challenger bracket declared as named execution phase | [YES/NO/PARTIAL] | [PHASE 2 CHALLENGE header present] |
| C-16 | Unfilled slot -> logged HIGH finding per slot | [YES/NO/PARTIAL] | [N escalation rows for M unfilled slots] |
| C-17 | Challenger phase gate has explicit exit condition blocking domain review | [YES/NO/PARTIAL] | [G1 closure predicate + blocking statement present] |
| C-18 | Slot-gap escalation produces separate matrix row, not inline annotation | [YES/NO/PARTIAL] | [escalation rows are distinct 6-column matrix entries] |
| C-19 | At least one column definition names anti-pattern exclusion | [YES/NO/PARTIAL] | [Lens column, Findings column anti-patterns cited] |
| C-20 | Gate has named OPEN/CLOSED states and 2+ enumerated closure conditions | [YES/NO/PARTIAL] | [OPEN/CLOSED present / 4 closure conditions listed] |
| C-21 | Escalation rule names prohibited output form inside the rule definition | [YES/NO/PARTIAL] | ["Do not embed..." inside C4 escalation rule] |
| C-22 | Matrix has Slot column; downstream elements reference slot numbers | [YES/NO/PARTIAL] | [Slot column present / synthesis uses "Slot N and Slot M..."] |
| C-23 | Validation declared as named phase at same level as CHALLENGE and REVIEW | [YES/NO/PARTIAL] | [PHASE 4 VALIDATE header present] |

If any designed-to-satisfy criterion scores NO: return to the relevant phase and revise.
PARTIAL: note the gap and proceed.

---

### PHASE 5 -- RENDER

**Entry**: PHASE 4 verification complete

**R1** Header:

```
Crew Review: [artifact name or type]
Depth: standard | deep
Slots: [list slot numbers and roles]
Roles: [list in slot order]
```

**R2** Review matrix (6 columns, rows in slot order):

| Slot | Role | Lens | Findings | Severity | Recommendation |
|------|------|------|----------|----------|----------------|

Row order:
1. Slot 1 primary row(s) from PHASE 2
2. Slot-gap escalation rows (1a, 1b, ... in slot-letter order)
3. Slots 2-N in manifest order

**R3** Cross-role synthesis (required -- must satisfy synthesis output contract):
Reference slot numbers. "Slot [N] and Slot [M] both find [shared concern]." Name at least
one convergence or conflict. Slot-gap rows count as findings for convergence detection. If
absent: `No cross-role signal detected -- findings are non-overlapping.`

**R4** AMEND (required -- must satisfy AMEND output contract):

> **AMEND**
> - Add to manifest as Slot [N+1]: `/crew-review [artifact] --amend add:slot[N+1]:[role-name]`
> - Rerun Slot 1 (challenger bracket): `/crew-review [artifact] --amend rerun:slot1`
> - Full manifest: `/crew-review [artifact] --depth deep`
> - Restrict to Slot 1 only: `/crew-review [artifact] --amend scope:challengers`
> - Rerun single slot: `/crew-review [artifact] --amend rerun:slot[N]`

---
