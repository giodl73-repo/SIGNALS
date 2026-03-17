---
skill: quest-variate
skill_target: crew-review
date: 2026-03-16
round: 5
rubric: crew-review-rubric-v5-2026-03-16.md
---

# crew-review -- Variate R5

5 complete prompt body variations. Single-axis first (V-01 through V-03), then
two-axis combinations (V-04, V-05).

**R5 design target**: R4 achieved C-20 and C-21 in separate variations but never
simultaneously. R4 V-01 got C-20 (named gate states, 5-condition closure) but failed C-21
because the anti-pattern exclusion was only in the gate's closure conditions, not inside
the escalation rule text itself. R4 V-02 got C-21 (anti-pattern inside escalation rule)
but failed C-20 because the gate had no named states or multi-condition closure predicate.
R5 tests whether they can coexist:

- V-01: C-20 + C-21 axis -- state machine gate with anti-pattern exclusion co-located in
  the escalation rule. The repair: add "not a sentence, not a note" inside the rule text
  while keeping the OPEN/CLOSED gate from R4 V-01. C-20 and C-21 now satisfied at the
  same structural site.
- V-02: C-21 primary + C-20 secondary -- builds on R4 V-02's strong C-21 escalation rule,
  adds the state machine gate (named states + multi-condition closure) that R4 V-02 lacked.
- V-03: C-19 + C-20 axis -- typed schema with column-level anti-pattern exclusions (C-19)
  plus a state machine gate (C-20). R4 V-03 had C-19; R4 V-01 had C-20. Tests whether a
  schema-first design can carry a full state machine gate without structural conflict.
- V-04: C-20 + C-21 as a structural unit -- gate closure conditions are expressed in terms
  of row production; the escalation rule that produces the rows names its prohibited form.
  C-20 and C-21 are causally linked: the gate closes because rows are produced; rows are
  correctly produced because the escalation rule names what a row is NOT.
- V-05: C-19 + C-20 + C-21 maximal -- typed schema anti-patterns (C-19), state machine
  gate (C-20), escalation anti-pattern inside the rule (C-21), plus full prior aspirational
  stack: C-11, C-12, C-13, C-15, C-16, C-17, C-18.

Registry context assumed: `.craft/roles/` contains `inertia-advocate.md`, `pm.md`,
`architect.md` (and whatever else the workspace adds). Role files include `archetype`,
`lens.verify`, `expertise.relevance` fields.

---

## V-01

**Axis**: Inertia framing (C-20 + C-21 co-located in gate mechanism)
**Hypothesis**: R4 V-01 failed C-21 because the prohibition on non-row escalation forms
appeared only as a gate closure condition ("each unfilled slot has produced a dedicated
row"), not inside the escalation rule itself. C-21 requires the prohibited form to be
named inside the escalation rule definition -- where the model encounters it at row
construction time, not at gate verification time. This variation keeps R4 V-01's state
machine gate intact (OPEN/CLOSED states, 5-condition closure predicate, C-20) and adds
the C-21 prohibition directly inside the slot-to-row escalation rule: "not a sentence
embedded in the challenger row's Findings cell, not a note appended below the row."
The gate condition and the escalation rule are now co-located -- one reads "each unfilled
slot has produced a dedicated row per the escalation rule," and the rule itself defines
both the required form and the prohibited forms. C-20 and C-21 are now satisfied at the
same structural site rather than across two separate mechanisms.

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

G1 state: **OPEN** (domain review is blocked while G1 is OPEN)

G1 closure predicate -- G1 transitions from OPEN to CLOSED only when ALL of the
following conditions are simultaneously true:
1. All roles with `archetype: challenger` in the role pool have run.
2. The null hypothesis 4-slot form has been attempted for each challenger role.
3. Every slot that could not be filled has produced a dedicated, separate matrix row
   as defined by the slot-to-row escalation rule below.
4. No slot has been silently omitted or collapsed with another slot into one sentence.
5. No generic placeholder ("some cost," "existing workflow," "the current process")
   has been accepted in place of a slot value.

**Domain review does not begin until G1 transitions to CLOSED.**

---

From the role pool, identify all roles with `archetype: challenger`. For each challenger
role, fill the null hypothesis 4-slot form:

> **Null hypothesis (4-slot form):**
> - **[SLOT-A]** We currently do ________ instead of building this.
> - **[SLOT-B]** The cost of that alternative is ________.
> - **[SLOT-C]** The switching cost to adopt this artifact is ________.
> - **[SLOT-D]** This artifact is worth acting on only if ________.

Fill each slot from artifact content or inferable workspace context.

**Slot-to-row escalation rule** -- mandatory, applies to each slot individually:

When a slot cannot be filled from the artifact:
1. Write `[not stated in artifact]` in that slot position.
2. Produce a **separate, dedicated matrix row** for that gap:
   | `[role-name]` | SLOT-[letter] gap: [slot label] not stated in artifact. Null hypothesis is incomplete without this. | HIGH | State [slot requirement] explicitly in the artifact before proceeding. |
3. **This row is a full matrix row.** It is NOT a sentence embedded within the
   challenger row's Findings cell. It is NOT a note or comment appended below the
   challenger row. It is NOT a parenthetical or footnote. It is a distinct,
   independently-scored row in the review matrix.
4. Each unfilled slot = one dedicated row. Two unfilled slots = two separate rows.

Generic placeholders ("some cost", "the existing workflow") count as unfilled.
Do not collapse two slots into one sentence.

Challenger severity (for the primary challenger row):
- HIGH: the "do nothing" case is credible and unaddressed in the artifact
- MEDIUM: inertia case is named but switching cost is not quantified
- LOW: artifact directly neutralizes the status quo argument

**Verify G1 closure predicate. All 5 conditions true? G1 state: CLOSED.**

---

### DOMAIN PHASE

**Entry condition: G1 must be CLOSED. Domain review is now permitted.**

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

Row order: challenger primary rows first, then slot-gap escalation rows (one per unfilled
slot, immediately after the challenger primary row, in slot-letter order), then domain
rows in selection order.

Column constraints:
- **Role**: must match a `.craft/roles/` filename stem
- **Severity**: exactly HIGH, MEDIUM, or LOW -- no other values

**Cross-role synthesis** (required, 2-3 sentences): name at least one convergence (two
roles raised the same concern) or one conflict (two roles disagree). Slot-gap escalation
rows count as findings for convergence detection. If genuinely absent: "No cross-role
signal detected -- findings are non-overlapping."

**AMEND** (required):

> **AMEND**
> - Add a reviewer: `/crew-review [artifact] --amend add:[role-name]`
> - Full registry run: `/crew-review [artifact] --depth deep`
> - Restrict to domain: `/crew-review [artifact] --amend scope:[domain]`
> - Re-open G1: `/crew-review [artifact] --amend rerun:challengers`

---

---

## V-02

**Axis**: Output format (C-21 escalation anti-pattern primary + C-20 gate secondary)
**Hypothesis**: R4 V-02 achieved C-21 -- the prohibited form ("Do not embed as a sentence
within a finding cell") was stated inside the escalation rule -- but failed C-20 because
the gate had no named states (OPEN/CLOSED) and no multi-condition closure predicate. The
gate was a sequence instruction ("run challengers before domain review"), not a state
machine. This variation takes R4 V-02's escalation rule structure as the anchor and adds
a proper state machine gate around the challenger bracket: two named states (OPEN/CLOSED)
and a multi-condition closure predicate (3+ enumerated conditions). C-21 is preserved
by keeping the anti-pattern prohibition inside the escalation rule text. C-20 is added
by surrounding that escalation rule with a named gate. The hypothesis is that the gate
and the rule are structurally separable: the gate defines when domain review unblocks
(C-20), the escalation rule defines how slot gaps are produced (C-21), and they coexist
without conflict.

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

**Gate G1 state: OPEN.** Domain review is blocked until G1 closes.

**G1 closure conditions** (all must hold before G1 closes):
1. All roles with `archetype: challenger` have run.
2. The null hypothesis 4-slot form has been attempted for each challenger role.
3. Every slot that could not be filled has been escalated per the slot-to-row rule below.

**Domain review does not begin until G1 closes.**

---

Find all roles in the pool with `archetype: challenger`. For each, attempt the null
hypothesis 4-slot form:

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
4. **Do not embed the gap finding as a sentence within the challenger row's Findings
   cell.** A finding embedded inside another row's cell is not a dedicated row.
5. **Do not append the gap as a note or comment below the challenger row.** An appended
   note is not a matrix row.
6. Each unfilled slot produces its own dedicated row. Two unfilled slots = two rows.

Generic placeholders ("some cost", "existing workflow") count as unfilled slots.
Do not collapse two slots into one sentence.

Challenger severity for the primary row:
- HIGH: inertia case is credible and unaddressed in the artifact
- MEDIUM: inertia case is named but switching cost is not quantified
- LOW: artifact directly neutralizes the status quo

**Verify G1 closure conditions. All 3 true? G1 state: CLOSED.**

---

### Step 3 -- Domain review

**Entry condition: G1 must be CLOSED.**

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
conflict (two roles disagree on priority or direction). Slot-gap escalation rows count as
findings for convergence detection -- if a domain reviewer also surfaces the same gap,
that is convergence. If genuinely absent: "No cross-role signal detected -- findings are
non-overlapping."

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

**Axis**: Output format (C-19 column anti-patterns + C-20 gate state machine)
**Hypothesis**: R4 V-03 achieved C-19 (column definitions name anti-pattern exclusions)
but the challenger phase was a sequence instruction, not a state machine gate -- so C-20
was out of reach. R4 V-01 achieved C-20 (named gate states, multi-condition closure) but
used a 4-column schema without anti-pattern exclusions in the column definitions -- so
C-19 was out of reach. The hypothesis is that schema-first design (declare the typed
output contract before execution) and a state machine gate (OPEN/CLOSED with enumerated
closure conditions) are structurally independent: the schema governs what cells contain
and the gate governs when phases unblock. They can coexist in the same prompt by placing
the schema declaration before PHASE 1 and the gate inside PHASE 2 where the challenger
bracket runs. This variation tests whether C-19 and C-20 can be achieved together without
either mechanism weakening the other.

---

You are running `/crew-review`.

Produce a structured crew review. Output schema is declared before execution and must
be followed exactly. The schema defines both valid values and excluded anti-patterns for
each column. The challenger bracket runs under a named gate with explicit state transitions.

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
column constraints including anti-pattern exclusions. Revise any cell that violates its
exclusion before writing. Do not write a row that fails validation.

After the table: a cross-role synthesis block and an AMEND block. Both are required.

---

### PHASE 1 -- LOAD

Open `.craft/roles/`. Read every file. Role pool = all files found.

Error halts -- unconditional, no soft fallback:
- Directory absent: `ERROR: .craft/roles/ not found.` Halt.
- Directory empty: `ERROR: .craft/roles/ is empty.` Halt.
- Any role file missing `lens.verify` or `expertise.relevance`:
  `ERROR: [role-name] missing required fields.` Halt.

Zero roles may be invented or substituted.

---

### PHASE 2 -- CHALLENGER BRACKET

**Gate G1 state: OPEN.** Domain review is structurally blocked.

**G1 closure predicate** -- G1 transitions OPEN -> CLOSED when all hold:
1. All roles with `archetype: challenger` have run.
2. The null hypothesis 4-slot form has been attempted for each challenger role.
3. Every slot that could not be filled has been escalated (per the escalation rule).
4. No slot has been silently omitted, collapsed, or approximated with a placeholder.

**Domain review does not begin until G1 transitions to CLOSED.**

---

Identify all roles with `archetype: challenger`. For each, fill the 4-slot form:

> **Null hypothesis (4-slot form):**
> - **[SLOT-A]** We currently do ________ instead of building this.
> - **[SLOT-B]** The cost of that alternative is ________.
> - **[SLOT-C]** The switching cost to adopt this artifact is ________.
> - **[SLOT-D]** This artifact is worth acting on only if ________.

Fill each slot from artifact content or inferable workspace context.

Slot escalation rule -- applies per slot:
- Cannot fill a slot: write `[not stated in artifact]` and log a HIGH finding in the
  matrix: "SLOT-[letter]: null hypothesis incomplete -- [slot name] not stated."
- Do not collapse two slots into one sentence.
- Generic placeholders count as unfilled.

For the challenger primary row, apply the per-row validation gate before writing.
The Lens cell for challenger roles: "As a [role], I care about whether the team has a
credible do-nothing alternative -- [specific concern from this role's lens.verify]."

Challenger severity for the primary row:
- HIGH: inertia case is credible and unaddressed in the artifact
- MEDIUM: inertia named but switching cost not quantified
- LOW: artifact directly neutralizes the status quo

**Verify G1 closure predicate. All 4 conditions true? G1 state: CLOSED.**

---

### PHASE 3 -- DOMAIN REVIEW

**Entry: G1 is CLOSED.**

Depth selection:
- Standard (default): select 2-4 roles (non-challenger) whose `expertise.relevance`
  intersects the artifact type. Include any `archetype: challenger` role regardless.
  Document each: "[role]: selected because [reason tied to artifact]."
- `--depth deep`: all non-challenger roles run.

For each selected domain role, apply the per-row validation gate before writing:
- Role cell: filename stem from `.craft/roles/` -- not invented ✓
- Lens cell: one sentence traceable to this role's `lens.verify` -- no restatement ✓
- Findings cell: names a specific artifact surface -- not abstract ✓
- Severity cell: exactly HIGH, MEDIUM, or LOW -- no freestyle label ✓
- Recommendation cell: names what to do and where -- no generic directive ✓

Execute challenger roles first; then all others.

---

### PHASE 4 -- OUTPUT

Write the 5-column table (Role, Lens, Findings, Severity, Recommendation).

Row order: challenger rows first (including any slot-gap escalation rows), then domain
rows in selection order.

**Cross-role synthesis** (required, 2-3 sentences): name at least one convergence or one
conflict. If genuinely absent: "No cross-role signal detected -- findings are
non-overlapping."

**AMEND** (required):

> **AMEND**
> - Add reviewer: `/crew-review [artifact] --amend add:[role-name]`
> - Full registry: `/crew-review [artifact] --depth deep`
> - Scope to domain: `/crew-review [artifact] --amend scope:[domain]`
> - Re-run challenger bracket: `/crew-review [artifact] --amend rerun:challengers`

---

---

## V-04

**Axes**: Inertia framing + Output format (C-20 + C-21 as structural unit)
**Hypothesis**: R4 placed C-20 and C-21 in separate variations -- V-01 had the state
machine gate but the escalation rule lacked the prohibition; V-02 had the prohibition
in the escalation rule but the gate had no named states. The gap was structural: neither
variation defined the gate and the escalation rule together. This variation makes them
a single structural unit by causal chaining: the gate's closure condition is expressed
in terms of row production ("every unfilled slot has produced a dedicated row per the
escalation rule below"), and the escalation rule names both the required form (a dedicated
row) and the prohibited form ("not embedded as a sentence within a finding cell; not an
appended note below the row"). The gate closes BECAUSE rows are produced. Rows are
correctly produced BECAUSE the rule names what they are not. C-20 (named states,
multi-condition closure) and C-21 (anti-pattern prohibition inside the rule definition)
become causally entangled: satisfying C-20 requires satisfying C-21's precondition.

---

You are running `/crew-review`.

This skill executes in two named phases separated by a state machine gate. Each phase
has explicit entry and exit conditions. Do not begin a phase until its entry condition
is satisfied.

---

### Step 1 -- Load registry

Read every file in `.craft/roles/`. Extract: role name, `archetype`, `lens.verify`,
`expertise.relevance`.

Error halts -- unconditional, no soft fallback, no partial execution:
- Directory absent: `ERROR: .craft/roles/ not found.` Halt.
- Directory empty: `ERROR: .craft/roles/ is empty.` Halt.
- Any file missing `lens.verify` or `expertise.relevance`:
  `ERROR: [role-name] missing required fields. Registry malformed.` Halt.

Role pool = all files found. Pool is locked. Zero roles may be invented.

---

### PHASE 1 -- CHALLENGER BRACKET

**Entry**: role pool locked
**Gate G1** -- challenger bracket gate

**G1 state: OPEN.** Domain review is blocked.

**G1 closure conditions** -- G1 transitions from OPEN to CLOSED when ALL hold:
1. All roles with `archetype: challenger` have run.
2. The null hypothesis 4-slot form has been attempted for each challenger role.
3. Every slot that could not be filled has produced a dedicated, separate matrix row
   as defined by the slot-to-row escalation rule below. A sentence embedded in the
   challenger row's Findings cell does NOT satisfy this condition. An appended note
   below the row does NOT satisfy this condition. Only a full 4-column matrix row
   satisfies this condition.
4. No slot has been silently omitted or collapsed with another slot.
5. No generic placeholder ("some cost", "existing process") has been accepted as filled.

**Domain review does not begin until G1 transitions to CLOSED.**

---

Identify all roles with `archetype: challenger`. For each, fill:

```
SLOT-A: We currently do [______] instead of building this.
SLOT-B: The cost of that alternative is [______].
SLOT-C: The switching cost to adopt this artifact is [______].
SLOT-D: This artifact is worth acting on only if [______].
```

Fill each slot from artifact content or inferable workspace context.

**Slot-to-row escalation rule** -- mandatory, applies to each slot individually:

When a slot cannot be filled:
1. Write `[not stated in artifact]` in that slot position.
2. Produce a **separate, dedicated matrix row** for that gap:
   | `[role-name]` | SLOT-[letter] gap: [slot label] not stated in artifact. Null hypothesis is incomplete. | HIGH | State [slot requirement] explicitly in the artifact before proceeding. |
3. **Do not embed the gap finding as a sentence within the challenger row's Findings
   cell.** This produces an inline annotation, not a matrix row, and does not satisfy
   G1 closure condition 3.
4. **Do not append the gap as a note below the challenger row.** This produces an
   appended comment, not a matrix row, and does not satisfy G1 closure condition 3.
5. Each unfilled slot = one row. Two unfilled slots = two separate rows.

Challenger severity for the primary row:
- HIGH: inertia case is credible and unaddressed
- MEDIUM: inertia named but switching cost not quantified
- LOW: artifact directly neutralizes the status quo

**Verify G1 closure conditions. All 5 true? G1 state: CLOSED.**

---

### PHASE 2 -- DOMAIN REVIEW AND OUTPUT

**Entry: G1 is CLOSED.**

Depth selection:
- Standard (default): select 2-3 non-challenger roles whose `expertise.relevance`
  intersects the artifact type. Document each: "[role]: selected because [reason]."
- `--depth deep`: all non-challenger roles run.

For each selected domain role:
1. Apply only that role's `lens.verify` perspective.
2. Name a specific artifact surface in each finding.
3. Severity: exactly HIGH, MEDIUM, or LOW -- no other values.
4. Recommendation: one action naming what to do and where.
5. Do not repeat a finding already raised by a prior reviewer.

**Review matrix** (4-column table):

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|

Row order:
1. Challenger primary row(s) from PHASE 1
2. Slot-gap escalation rows (one per unfilled slot, in slot-letter order)
3. Domain rows in selection order

**Cross-role synthesis** (required, 2-3 sentences): name at least one convergence or
conflict. Slot-gap rows count as findings for convergence detection. If absent: "No
cross-role signal detected -- findings are non-overlapping."

**AMEND** (required):

> **AMEND**
> - Add a reviewer: `/crew-review [artifact] --amend add:[role-name]`
> - Full registry run: `/crew-review [artifact] --depth deep`
> - Restrict to domain: `/crew-review [artifact] --amend scope:[domain]`
> - Reopen G1 (re-run challenger bracket): `/crew-review [artifact] --amend rerun:challengers`

---

---

## V-05

**Axes**: Output format + Inertia framing + Role sequence (C-19 + C-20 + C-21 maximal)
**Hypothesis**: All three R4/R5 aspirational criteria can be achieved simultaneously in
a single coherent design by combining: (1) a typed 5-column schema where every column
definition names its excluded anti-pattern (C-13 + C-19); (2) a named challenger bracket
as a discrete execution phase, with a state machine gate carrying named OPEN/CLOSED states
and a multi-condition closure predicate (C-15 + C-17 + C-20); (3) a slot-to-row escalation
rule that names the prohibited output form inside the rule definition itself (C-16 +
C-18 + C-21); plus a Lens column (C-12) and a structured null hypothesis template
(C-11). The three mechanisms are not in tension: the schema governs cell-level validity,
the gate governs phase-level sequencing, and the escalation rule governs slot-level
production. Each mechanism operates at a different structural level, so they reinforce
rather than conflict. The maximal design is a four-phase lifecycle: LOAD, CHALLENGER,
DOMAIN, RENDER -- where the schema, the gate, and the escalation rule are each visible
in the phase where they do their work.

---

You are running `/crew-review`.

Reviews execute in four named phases. Output schema is declared before execution. All
rows are validated against schema constraints -- including anti-pattern exclusions --
before being written. The challenger bracket closes under a named state machine gate;
domain review does not begin until the gate transitions to CLOSED.

---

### Output schema (declare before executing)

The final output is a 5-column markdown table.

| Column | Type -- valid | Anti-pattern excluded (NOT valid) |
|--------|--------------|-----------------------------------|
| Role | string -- filename stem from `.craft/roles/` at execution time | NOT: invented names; names from memory or prior runs; any name not in the registry at this execution |
| Lens | string -- one sentence: "As a [role], I care about [specific concern from `lens.verify`]" | NOT: generic role restatements ("As a PM, I review as a PM"); NOT: concerns borrowed from another role's lens; NOT: multi-sentence declarations |
| Findings | string -- names a specific artifact surface: section title, field name, diagram element, or named assumption | NOT: abstract observations without a named surface ("needs more detail", "unclear", "incomplete", "could be improved"); NOT: observations naming only the artifact as a whole |
| Severity | enum -- exactly `HIGH`, `MEDIUM`, or `LOW`; HIGH = blocks commitment; MEDIUM = must resolve before ship; LOW = advisory | NOT: freestyle labels (Critical, Minor, Warning, Blocker, Moderate, Severe); NOT: blank cells; NOT: combinations ("HIGH/MEDIUM") |
| Recommendation | string -- names (1) what to do and (2) where in the artifact | NOT: generic directives ("review this", "improve this section", "consider adding", "needs clarification"); NOT: recommendations without a named artifact location |

Per-row validation gate: before writing any row, verify all five cells against their
constraints including anti-pattern exclusions. If any cell violates its exclusion,
revise it until it passes. Do not write a row that fails validation.

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

**Entry**: PHASE 1 exit (pool locked)
**Gate G1** -- challenger bracket gate

**G1 state: OPEN.** Domain review is blocked.

**G1 closure predicate** -- G1 transitions from OPEN to CLOSED when ALL hold:
1. All roles with `archetype: challenger` have run.
2. The null hypothesis 4-slot form has been attempted for each challenger role.
3. For every slot that could not be filled: a dedicated, separate 5-column matrix row
   exists in the output, validated against the output schema above, with Severity = HIGH.
4. No unfilled slot has been silently omitted, collapsed into another slot, or
   approximated with a generic placeholder.

**Domain review does not begin until G1 transitions to CLOSED.**

---

**C1** Identify all roles with `archetype: challenger` in the pool.

**C2** For each challenger role, fill the null hypothesis 4-slot form:

```
SLOT-A: We currently do [______] instead of building this.
SLOT-B: The cost of that alternative is [______].
SLOT-C: The switching cost to adopt this artifact is [______].
SLOT-D: This artifact is worth acting on only if [______].
```

**C3** Fill each slot from artifact content or inferable workspace context.

**C4** Slot-to-row escalation rule -- mandatory, applies to each slot individually:

When a slot cannot be filled:
1. Write `[not stated in artifact]` in that slot position in the null hypothesis form.
2. Produce a **separate, dedicated matrix row** -- a full 5-column row following the
   output schema above:
   - Role: `[challenger-role-name]`
   - Lens: "As a [role], I care about null hypothesis completeness -- SLOT-[letter] is
     missing from the artifact."
   - Findings: "SLOT-[letter] gap: [slot label] not stated in the artifact. Null
     hypothesis is incomplete without this field."
   - Severity: HIGH
   - Recommendation: "State [slot requirement] explicitly in [artifact section] before
     this artifact proceeds to domain review."
3. **Do not embed this finding as a sentence within the challenger row's Findings cell.**
   A sentence inside another row's Findings cell is not a dedicated row and does not
   satisfy G1 closure condition 3.
4. **Do not append this as a note below the challenger row.** An appended note is not
   a matrix row and does not satisfy G1 closure condition 3.
5. Each unfilled slot = one dedicated row. Two unfilled slots = two separate rows.
6. Apply per-row validation gate before writing this row.

**C5** Challenger primary row:
- Lens cell: "As a [role], I care about [specific concern from this role's lens.verify]."
- Findings cell: includes the filled/attempted null hypothesis 4-slot form.
- Severity: HIGH (inertia case credible, unaddressed) / MEDIUM (named, cost unstated) /
  LOW (artifact directly neutralizes status quo).
- Recommendation: one action naming what to do and where.
- Apply per-row validation gate before writing.

**C6** Verify G1 closure predicate. All 4 conditions true? **G1 state: CLOSED.**
Any condition false? Resolve before proceeding to PHASE 3.

---

### PHASE 3 -- DOMAIN REVIEW

**Entry**: G1 is CLOSED (PHASE 2 exit)

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
   -- no generic restatement; concern traceable to this role's documented lens.
2. Findings cell: name a specific artifact surface. No abstract observations. No
   repeating a finding already raised by a prior reviewer.
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
