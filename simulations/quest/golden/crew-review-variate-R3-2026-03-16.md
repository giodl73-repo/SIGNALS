---
skill: quest-variate
skill_target: crew-review
date: 2026-03-16
round: 3
rubric: crew-review-rubric-v3-2026-03-16.md
---

# crew-review -- Variate R3

5 complete prompt body variations. Single-axis first (V-01 through V-03), then
two-axis combinations (V-04, V-05).

**R3 design target**: No variation yet achieves C-12 + C-13 + C-09 + C-11 + C-15 + C-16
simultaneously. R3 explores three paths toward that combination:
- V-01: C-15 + C-16 as primary axis (challenger phase + slot escalation)
- V-02: C-12 + C-13 as primary axis (typed schema + lens column)
- V-03: register only -- conversational voice carrying full aspirational structure
- V-04: C-15 + C-16 + C-12 + C-13 combined in a lifecycle frame
- V-05: archetype-ordered sequence + C-12 + C-13 + C-15 + C-16 all present

Registry context assumed: `.roles/` contains `inertia-advocate.md`, `pm.md`,
`architect.md` (and whatever else the workspace adds). Role files include `archetype`,
`lens.verify`, `expertise.relevance` fields.

---

## V-01

**Axis**: Inertia framing
**Hypothesis**: Declaring the challenger pass as a named, self-contained execution phase
-- with a 4-slot null hypothesis form where each empty slot auto-escalates to a HIGH
finding -- produces a review where the inertia case cannot be satisfied by silence,
approximation, or position alone. C-09 (challenger leads) is correct-by-construction when
the challenger phase is a closed bracket that the domain phase cannot interrupt.

---

You are running `/crew-review`.

Route the artifact through the org registry and produce a multi-role review matrix.

---

### Step 1 -- Load the registry

Read every file in `.roles/`. Extract each role's name, `archetype`, `lens.verify`,
and `expertise.relevance`.

Error conditions (all halt execution immediately):
- `.roles/` is absent: `ERROR: .roles/ not found. Cannot proceed.`
- `.roles/` is present but empty: `ERROR: .roles/ is empty. Cannot proceed.`
- A role file is missing `lens.verify` or `expertise.relevance`:
  `ERROR: [role-name] missing required fields. Registry malformed. Cannot proceed.`

Role pool = all files found. Zero roles may be fabricated.

---

### CHALLENGER PHASE

**This is a named execution phase. Domain review does not begin until this phase is
complete.**

From the role pool, identify all roles with `archetype: challenger`. Run each one now.

For each challenger role, produce a null hypothesis using this 4-slot form:

> **Null hypothesis (4-slot form):**
> - **[SLOT-A]** We currently do ________ instead of building this.
> - **[SLOT-B]** The cost of that alternative is ________.
> - **[SLOT-C]** The switching cost to adopt this artifact is ________.
> - **[SLOT-D]** This artifact is worth acting on only if ________.

Fill each slot from artifact content or inferable context.

Slot escalation rule -- mandatory, applies per slot:
- A slot that cannot be filled from the artifact: write `[not stated in artifact]` in
  that slot, then log a HIGH finding: "SLOT-[letter]: null hypothesis incomplete --
  [slot name] not stated in artifact."
- Do not collapse multiple slots into one sentence.
- Generic placeholders ("some cost," "the current workflow") count as unfilled slots.

Challenger severity logic:
- HIGH: the "do nothing" case is credible and unaddressed in the artifact
- MEDIUM: inertia case is named but switching cost is not quantified
- LOW: artifact directly neutralizes the status quo argument

**CHALLENGER PHASE closes here.**

---

### DOMAIN PHASE

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

**DOMAIN PHASE closes here.**

---

### Step 2 -- Review matrix

Write the full review as a 4-column table:

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|

Row order: challenger roles first (from CHALLENGER PHASE), then domain roles in
selection order.

Column constraints:
- **Role**: must match a `.roles/` filename stem
- **Severity**: exactly HIGH, MEDIUM, or LOW -- no other values

---

### Step 3 -- Cross-role synthesis

2-3 sentences after the matrix. Name at least one convergence (two roles raised the same
concern) or one conflict (two roles disagree on priority or direction). If genuinely
absent: "No cross-role signal detected -- findings are non-overlapping."

---

### Step 4 -- AMEND

> **AMEND**
> - Add a reviewer: `/crew-review [artifact] --amend add:[role-name]`
> - Full registry run: `/crew-review [artifact] --depth deep`
> - Restrict to domain: `/crew-review [artifact] --amend scope:[domain]`

---

---

## V-02

**Axis**: Output format
**Hypothesis**: Declaring a 5-column output schema -- with Lens as a required column, typed
constraints per column, and a per-row validation gate before any row is written -- makes
C-12 (lens-lock) and C-13 (typed contracts) correct-by-construction: a missing lens entry
is a visible column gap, and a non-conforming severity value cannot pass the validation
gate. This approach targets the gap from R2: V-01 achieved C-12 but only partial C-13
(no explicit named validation pass).

---

You are running `/crew-review`.

Produce a structured crew review for the provided artifact. Output format is declared
before execution and must be followed exactly.

---

### Output schema (read before executing)

The review is a single markdown table with five columns:

| Column | Type | Constraint |
|--------|------|------------|
| Role | string | Must match a filename stem in `.roles/`. Zero fabricated names. If no match exists, the role may not appear. |
| Lens | string | One sentence: "As a [role], I care about [specific concern from this role's lens.verify]." No generic restatements (e.g., "As a PM, I review as a PM" does not pass). Must be traceable to this role's documented lens, not the prior role's. |
| Findings | string | Must name a specific artifact surface: a section title, field name, diagram element, or named assumption. Generic observations without a named surface are invalid. |
| Severity | enum | Exactly one of: `HIGH`, `MEDIUM`, `LOW`. No other values. HIGH = blocks commitment. MEDIUM = must resolve before ship. LOW = advisory. |
| Recommendation | string | One concrete action. Must name (1) what to do and (2) where in the artifact. Generic directives ("review this section") are invalid. |

Per-row validation gate: before writing any row, verify all five cells against their
constraints. If any cell fails, revise it until it passes. Do not write a row that
fails validation.

After the table: a cross-role synthesis block and an AMEND block. Both are required.
A missing block fails the output contract.

---

### Execution

**Phase 1 -- Load**

Open `.roles/`. Read every file. Available role pool = all files found.
- Directory absent: `ERROR: .roles/ not found.` and stop.
- Directory empty: `ERROR: .roles/ is empty.` and stop.
- Any role file missing `lens.verify` or `expertise.relevance`:
  `ERROR: [role-name] missing required fields.` and stop.

**Phase 2 -- Select**

Default (standard): select 2-4 roles whose `expertise.relevance` intersects the artifact
type. Include any role with `archetype: challenger` regardless of relevance. Document each
selection in one sentence.

`--depth deep`: select all roles in the registry.

**Phase 3 -- Review**

Execute roles in this order: `archetype: challenger` first, then all others.

For each role, produce a review. Apply the per-row validation gate before writing:
- Role name is in `.roles/` ✓
- Lens is one sentence traceable to this role's lens.verify ✓
- Finding names a specific artifact surface ✓
- Severity is exactly HIGH, MEDIUM, or LOW ✓
- Recommendation names what to do and where ✓

For challenger roles: the Lens sentence opens with the null hypothesis framing
("As an inertia-advocate, I care about whether the team has a credible alternative today").
The Findings cell must name what the team currently does instead of adopting this artifact.

**Phase 4 -- Output**

Write the 5-column table. Then:

**Cross-role synthesis** (required, 2-3 sentences):
Name at least one convergence (two roles flag the same concern area) or one conflict
(two roles disagree). If genuinely absent: "No cross-role signal detected."

**AMEND** (required):

> **AMEND**
> - Add reviewer: `/crew-review [artifact] --amend add:[role-name]`
> - Full registry: `/crew-review [artifact] --depth deep`
> - Scope to domain: `/crew-review [artifact] --amend scope:[domain]`
> - Re-run single role: `/crew-review [artifact] --amend rerun:[role-name]`

---

---

## V-03

**Axis**: Phrasing register
**Hypothesis**: A conversational, directive voice -- "go do X," "name the thing," short
declarative sentences -- can carry the full aspirational structure (C-11 through C-16)
without the formality of typed schema tables. If the hypothesis holds, register is
independent of structural quality. If it fails, the formality of schema declarations
is doing structural work that instruction proximity cannot replicate.

---

You are running `/crew-review`. Here is exactly what you do.

---

**Load the org**

Go to `.roles/`. Read every file. That directory is your complete reviewer pool --
don't invent anyone who isn't there.

Three stops before you go any further:
- If the directory doesn't exist: stop, output `ERROR: .roles/ not found.`
- If the directory is empty: stop, output `ERROR: .roles/ is empty.`
- If any role file is missing `lens.verify` or `expertise.relevance`: stop, output
  `ERROR: [role-name] is missing required fields.`

---

**Challenger Phase -- runs before anything else**

Find every role with `archetype: challenger`. Run them all. This whole bracket closes
before any domain reviewer speaks.

For each challenger, fill in this form -- all four blanks, no exceptions:

> We currently do **[what the team does today]** instead of building this.
> The cost of that alternative is **[specific cost -- time, errors, or fragility]**.
> The switching cost to adopt this is **[what would need to change]**.
> This is worth acting on only if **[the condition that makes inertia unacceptable]**.

Can't fill a blank? That's their HIGH finding. Write `[not stated in artifact]` in that
blank and log it: "Null hypothesis incomplete -- [blank name] not stated in artifact."
Don't squash two blanks into one sentence. Don't use vague placeholders.

How bad is the inertia case?
- HIGH: doing nothing is plausible and the artifact doesn't argue against it
- MEDIUM: the artifact names the alternative but doesn't price the switch
- LOW: the artifact knocks down the status quo directly

**Challenger Phase done. Domain Phase starts now.**

---

**Pick your domain reviewers**

Standard run (default): pick 2-3 roles from the registry (not challengers) whose job
actually touches this artifact. One sentence per pick: why this role, not someone else.

`--depth deep`: everyone runs.

---

**Run each domain reviewer**

For each one, do four things in order:

1. **Lock the lens.** One sentence: "As a [role], I care about [the specific concern from
   this role's lens.verify]." Name the actual concern, not just the role title.

2. **Find something specific.** Point to a section title, field name, diagram, or named
   assumption in the artifact. Don't say "this needs work." Say "Section 3's scope
   enumeration is missing X."

3. **Call the severity.** HIGH, MEDIUM, or LOW -- nothing else.
   - HIGH: can't proceed without fixing this
   - MEDIUM: fix before shipping
   - LOW: good to fix, not blocking

4. **Tell them what to do and where.** Exact surface, exact action.

Don't repeat a finding another reviewer already raised.

---

**Write the matrix**

| Role | Findings | Severity | Recommendation |

Challenger rows first, then domain rows in the order you ran them. Every cell is specific.
No generic findings, no generic recommendations.

---

**Cross-role read**

After the table: did two reviewers independently raise the same concern? That's your
highest-confidence signal -- name it. Did two disagree? Name that too. Neither? Say so.

---

**AMEND**

Tell them what they can do next:

> **AMEND**
> - Add a reviewer: `/crew-review [artifact] --amend add:[role-name]`
> - Run everyone: `/crew-review [artifact] --depth deep`
> - Focus on one domain: `/crew-review [artifact] --amend scope:[domain]`

---

---

## V-04

**Axes**: Inertia framing + Lifecycle emphasis
**Hypothesis**: Embedding the challenger bracket as a hard phase gate in a 4-phase lifecycle
-- where DOMAIN cannot begin until CHALLENGER has exited, and where the null hypothesis
form carries per-slot escalation logic -- produces the strongest possible guarantee for
C-09/C-15 (challenger leads because it's a phase, not a hint) and C-11/C-16 (template
enforced because the exit condition of CHALLENGER depends on slot completion, not
instruction compliance). This combines V-01's inertia framing with V-05 R1's phase
lifecycle structure.

---

You are running `/crew-review`.

This skill executes in four phases. Each phase has entry and exit conditions. Do not begin
a phase until its entry condition is met. Do not leave a phase until its exit condition
is satisfied.

---

## PHASE 1 -- LOAD

**Entry**: artifact provided
**Exit**: role pool locked and verified

**L1** Open `.roles/`. Read every file in the directory.
**L2** For each file, extract: role name, `archetype`, `lens.verify`, `expertise.relevance`.
**L3** Error halts -- unconditional, no soft fallback:
  - Directory absent: `ERROR: .roles/ not found.` Halt.
  - Directory empty: `ERROR: .roles/ is empty.` Halt.
  - Any file missing `lens.verify` or `expertise.relevance`:
    `ERROR: [role-name] missing required fields. Registry malformed.` Halt.
**L4** Role pool = all roles found. Pool is locked. Zero roles may be invented or added.

---

## PHASE 2 -- CHALLENGER BRACKET

**Entry**: role pool locked (PHASE 1 exit)
**Exit**: all challenger roles have produced a completed null hypothesis form; any
incomplete slot has been escalated to a HIGH finding

**C1** Identify all roles in the pool with `archetype: challenger`.
**C2** For each challenger role, fill this null hypothesis form:

```
Null hypothesis -- 4-slot form:
  SLOT-A: We currently do [______] instead of building this.
  SLOT-B: The cost of that alternative is [______].
  SLOT-C: The switching cost to adopt this artifact is [______].
  SLOT-D: This artifact is worth acting on only if [______].
```

**C3** Slot completion rules:
  - Fill each slot from artifact content or inferable workspace context.
  - Slot that cannot be filled: write `[not stated in artifact]` AND log a HIGH finding
    in the matrix: "SLOT-[letter]: null hypothesis -- [slot name] not stated in artifact."
    Severity: HIGH.
  - Do not collapse two slots into one sentence.
  - Generic placeholders ("some alternative," "existing process") count as unfilled.

**C4** Challenger severity:
  - HIGH: inertia case is credible and the artifact does not address it
  - MEDIUM: inertia case is named but switching cost is not quantified
  - LOW: artifact directly neutralizes the status quo

**C5** CHALLENGER BRACKET exit condition: every slot is either filled or escalated.
No challenger may exit with a silent or collapsed slot.

**Domain review does not begin until PHASE 2 exits.**

---

## PHASE 3 -- DOMAIN REVIEW

**Entry**: CHALLENGER BRACKET exited (PHASE 2 exit)
**Exit**: all selected domain roles have produced a validated review row

**D1** Depth selection:
  - Standard (default): select 2-3 roles (non-challenger) whose `expertise.relevance`
    intersects the artifact type. Document each selection: "[role]: selected because [reason]."
  - `--depth deep`: select all non-challenger roles in the pool.

**D2** For each selected domain role, in selection order:
  1. **Lens declaration** (required before findings): one sentence -- "As a [role], I care
     about [specific concern from this role's lens.verify]." No generic role restatements.
  2. **Finding**: name a specific artifact surface (section title, field, diagram, named
     assumption). Do not repeat a finding already raised by a prior reviewer.
  3. **Severity**: exactly HIGH, MEDIUM, or LOW -- no other values.
  4. **Recommendation**: one action naming what to do and where in the artifact.

**D3** DOMAIN REVIEW exit condition: all selected roles have produced validated rows.

---

## PHASE 4 -- RENDER

**Entry**: all review rows complete (PHASE 3 exit)
**Exit**: output delivered

**R1** Write the review matrix:

```
| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|
[challenger rows from PHASE 2 first, then domain rows in selection order]
```

**R2** Cross-role synthesis (required):

2-3 sentences. Name at least one convergence (two roles raised the same concern) or one
conflict (two roles disagree). If genuinely absent: "No cross-role signal detected --
findings are non-overlapping."

**R3** AMEND block (required):

> **AMEND**
> - Add a reviewer: `/crew-review [artifact] --amend add:[role-name]`
> - Full registry run: `/crew-review [artifact] --depth deep`
> - Restrict to domain: `/crew-review [artifact] --amend scope:[domain]`
> - Re-run a phase: `/crew-review [artifact] --amend rerun:challenger`

---

---

## V-05

**Axes**: Output format + Role sequence
**Hypothesis**: Combining archetype-derived execution order (from R1 V-04) with a 5-column
typed schema that includes Lens (from R2 V-01) AND embedding the challenger bracket as the
first named group in the archetype sequence (not an exception clause) targets all six
aspirational criteria in a single coherent design: C-11 via mandatory null hypothesis,
C-12 via Lens column, C-13 via typed schema with validation gate, C-14 via three-level
halt, C-15 via archetype group 1 as a named execution block, C-16 via per-slot escalation.

---

You are running `/crew-review`.

Reviews execute in archetype-group sequence. Output schema is declared before execution
and all rows are validated against it before being written.

---

### Output schema (declare before executing)

The final output is a 5-column markdown table:

| Column | Type | Constraint |
|--------|------|------------|
| Role | string | Must match a `.roles/` filename stem. No invented names. |
| Lens | string | One sentence: "As a [role], I care about [specific concern from lens.verify]." Must name the role's actual lens, not a generic restatement of the role title. |
| Findings | string | Names a specific artifact surface: section title, field name, diagram element, or named assumption. Generic observations without a named surface are invalid. |
| Severity | enum | Exactly one of: `HIGH`, `MEDIUM`, `LOW`. No other values. HIGH = blocks commitment. MEDIUM = must resolve before ship. LOW = advisory. |
| Recommendation | string | One action naming (1) what to do and (2) where in the artifact. Generic directives ("improve this section") are invalid. |

Per-row validation: before writing any row, verify all five cells satisfy their constraints.
Revise any failing cell before proceeding.

---

### Step 1 -- Load registry

Read every file in `.roles/`. Extract: role name, `archetype`, `lens.verify`,
`expertise.relevance`.

Error halts (unconditional -- no fallback, no partial execution):
- `.roles/` absent: `ERROR: .roles/ not found.` Halt.
- `.roles/` empty: `ERROR: .roles/ is empty.` Halt.
- Any file missing `lens.verify` or `expertise.relevance`:
  `ERROR: [role-name] missing required fields. Registry malformed.` Halt.

Role pool = all files found. Pool is locked. Zero roles may be invented.

---

### Step 2 -- Build execution queue

Assign each role in the pool to an archetype group. Groups execute in this order:

```
Group 1 (runs first): archetype: challenger
Group 2:              archetype: product
Group 3:              archetype: technical
Group 4:              archetype: quality
Group 5 (runs last):  all other archetypes; roles with no archetype field appended here
```

Within each group: order alphabetically by role name.

Depth gate:
- Standard (default): from groups 2-5, select roles whose `expertise.relevance` intersects
  the artifact type. Target 2-4 total (Group 1 always runs in full regardless of depth).
  Document each selection: "[role]: selected because [reason tied to artifact]."
- `--depth deep`: all roles in all groups run.

---

### Step 3 -- Group 1 bracket (challenger -- runs before all other groups)

Execute all Group 1 roles now. Group 1 closes before Group 2 begins.

For each Group 1 role, the Lens cell opens with:
> "As an inertia-advocate, I care about whether a credible do-nothing alternative exists today."

The Findings cell must include a null hypothesis in this 4-slot form:

```
  SLOT-A: We currently do [______] instead of building this.
  SLOT-B: The cost of that alternative is [______].
  SLOT-C: The switching cost to adopt this is [______].
  SLOT-D: This is worth acting on only if [______].
```

Per-slot escalation (applies to each slot individually):
- Slot that cannot be filled: write `[not stated in artifact]` in that slot AND log a
  separate HIGH finding row: "Null hypothesis -- SLOT-[letter]: [slot name] not stated
  in artifact." Severity: HIGH.
- Do not collapse two slots into one sentence.
- Generic placeholders count as unfilled slots.

Apply per-row validation gate before writing the Group 1 row.

**Group 1 closes here. Group 2 begins next.**

---

### Step 4 -- Groups 2-5 (domain review)

Execute selected roles in group order. For each role:
1. Lens cell: "As a [role], I care about [specific concern from this role's lens.verify]."
2. Findings cell: name a specific artifact surface. No repeating a prior reviewer's finding.
3. Severity: HIGH / MEDIUM / LOW only.
4. Recommendation: what to do + where.

Apply per-row validation gate before writing each row.

---

### Step 5 -- Write output

**Header:**
```
Crew Review: [artifact name or type]
Depth: standard | deep
Groups run: [list groups executed]
Roles: [list all role names in execution order]
```

**Review matrix** (5 columns, rows in execution order):

| Role | Lens | Findings | Severity | Recommendation |
|------|------|----------|----------|----------------|

**Cross-role synthesis** (required):
2-3 sentences. At least one convergence (two roles raised the same concern) or one
conflict (two roles disagree). If absent: "No cross-role signal detected -- findings
are non-overlapping."

**AMEND** (required):

> **AMEND**
> - Add reviewer (inserted by archetype group): `/crew-review [artifact] --amend add:[role-name]`
> - Full registry: `/crew-review [artifact] --depth deep`
> - Scope to group: `/crew-review [artifact] --amend scope:group[N]`
> - Re-run Group 1: `/crew-review [artifact] --amend rerun:challengers`

---
