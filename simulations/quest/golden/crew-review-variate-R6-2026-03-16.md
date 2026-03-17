---
skill: quest-variate
skill_target: crew-review
date: 2026-03-16
round: 6
rubric: crew-review-rubric-v5-2026-03-16.md
---

# crew-review -- Variate R6

5 complete prompt body variations. Single-axis first (V-01 through V-03), then
two-axis combinations (V-04, V-05).

**R6 design target**: R5 established that C-20 and C-21 can coexist and achieved the
full aspirational stack in R5 V-05. R6 does not chase new aspirational criteria -- it
asks whether structural alternatives to the imperative step-sequence architecture can
make the full stack (especially C-17, C-18, C-20, C-21) more reliably satisfied across
invocations:

- V-01: Phrasing register -- full declarative contract form. Replace all imperative
  steps with property declarations. The review is not "execute these steps"; it is
  "produce output satisfying these typed invariants." Tests whether the aspirational
  chain survives a register transformation from imperative to declarative.
- V-02: Lifecycle emphasis -- AMEND as a pre-delivery phase, not trailing output.
  Five named lifecycle phases: LOAD, CHALLENGE, REVIEW, VALIDATE, AMEND. VALIDATE is
  new: before the matrix is written, each row is explicitly checked. AMEND becomes a
  phase with an entry condition and its own output contract, not a bulleted afterthought.
- V-03: Role sequence -- execution manifest contract. Before any role runs, declare
  a numbered execution manifest (slot 1 = challenger, slots 2-N = domain roles ranked
  by relevance). The manifest is written and locked before execution. Cross-role
  synthesis can reference slot numbers. Makes C-06 directly verifiable from the manifest.
- V-04: Phrasing register + Inertia framing -- peer-voice challenger with state machine
  gate. The challenger bracket uses natural-language peer-voice framing ("let's hear
  the strongest case for doing nothing") while the gate beneath it is a state machine
  (OPEN/CLOSED, multi-condition closure). Tests whether challenger framing register
  affects C-09/C-11 satisfaction while C-20 remains structurally intact.
- V-05: Lifecycle + Output format + Role sequence -- verification-first maximal.
  All prior aspirational mechanisms (C-11 through C-21) plus an explicit pre-output
  criterion-check table: before writing the final matrix, the model verifies each
  aspirational criterion and marks it satisfied/unsatisfied. The criterion-check table
  is visible in the output. Tests whether meta-verification at a dedicated checkpoint
  improves full-stack reliability.

Registry context assumed: `.craft/roles/` contains `inertia-advocate.md`, `pm.md`,
`architect.md` (and whatever else the workspace adds). Role files include `archetype`,
`lens.verify`, `expertise.relevance` fields.

---

## V-01

**Axis**: Phrasing register (declarative contract form)
**Hypothesis**: Every prior variation (R1-R5) expresses the review as a sequence of
imperative steps: "Step 1, do X. Step 2, do Y. If condition, then Z." This register
makes execution order the load-bearing structure -- the model must follow the steps and
can drift between them. A declarative form inverts this: the output is declared as a
typed contract with named invariants, and execution is whatever produces output satisfying
those invariants. The gate, the escalation rule, the schema, and the AMEND section become
properties the output must have -- not instructions to follow in sequence. The hypothesis
is that invariant-based declarations produce more reliable aspirational criterion
satisfaction than step-based instructions, because a declared invariant is checked at
output time rather than recalled at execution time. This variation tests whether the full
aspirational chain (especially C-20: named gate states, C-21: anti-pattern prohibition
in escalation rule) survives transformation from imperative to declarative register.

---

You are running `/crew-review`.

The output of this skill is a typed artifact. The artifact is defined below as a contract.
Your job is to produce an output that satisfies every property in the contract. Execution
approach is your choice; the contract is not optional.

---

### CONTRACT: crew-review artifact

**Property R1 -- Registry grounding**
Every role name in the output corresponds to a file that exists in `.craft/roles/` at
execution time. No role is invented, recalled from a prior run, or substituted.
- If `.craft/roles/` is absent: output exactly `ERROR: .craft/roles/ not found.` Stop.
- If `.craft/roles/` is present but empty: output exactly `ERROR: .craft/roles/ is empty.` Stop.
- If any role file is missing `lens.verify` or `expertise.relevance`: output exactly
  `ERROR: [role-name] missing required fields. Registry malformed.` Stop.
These error conditions are unconditional halts. No partial output is produced.

---

**Property R2 -- Challenger-first invariant**
The output begins with a challenger bracket. The challenger bracket is COMPLETE before
any domain reviewer row appears. "Complete" means:

> Challenger bracket complete :=
>   (a) all roles in `.craft/roles/` with `archetype: challenger` have been processed,
>   AND (b) the null hypothesis 4-slot form has been attempted for each,
>   AND (c) every unfilled slot has been escalated per Property R3,
>   AND (d) no slot was silently omitted, collapsed, or filled with a generic placeholder.

The output encodes this invariant as Gate G1:
- **G1 states**: OPEN or CLOSED
- **G1 initial state**: OPEN
- **G1 closure predicate**: G1 transitions OPEN -> CLOSED when (a), (b), (c), (d) all hold
- **G1 enforcement**: no domain reviewer row may appear in the output while G1 is OPEN

G1 state is shown explicitly in the output as `[G1: OPEN]` or `[G1: CLOSED]`.

---

**Property R3 -- Null hypothesis template and slot escalation contract**
Each challenger role's review includes a 4-slot null hypothesis form:
- SLOT-A: We currently do [______] instead of building this.
- SLOT-B: The cost of that alternative is [______].
- SLOT-C: The switching cost to adopt this artifact is [______].
- SLOT-D: This artifact is worth acting on only if [______].

Fill each slot from artifact content or inferable workspace context.

When a slot cannot be filled, the escalation contract applies -- mandatory, per slot:
1. Write `[not stated in artifact]` in that slot position.
2. Produce a **separate, dedicated matrix row** with this exact structure:
   - Role: `[challenger-role-name]`
   - Findings: `SLOT-[letter] gap: [slot label] not stated in artifact. Null hypothesis
     is incomplete without this.`
   - Severity: `HIGH`
   - Recommendation: `State [slot requirement] explicitly in the artifact before
     proceeding to domain review.`
3. This dedicated row is the ONLY valid escalation form. The following forms do NOT
   satisfy Property R3 and do NOT satisfy G1 closure predicate (c):
   - A sentence embedded within the challenger row's Findings cell
   - A note or comment appended below the challenger row
   - A parenthetical or footnote anywhere in the output
4. Each unfilled slot = one dedicated row. Two unfilled slots = two rows.

Generic placeholders ("some cost", "existing workflow", "the current process") count as
unfilled slots. Do not collapse two slots into one sentence.

---

**Property R4 -- Review matrix schema**
The output contains a single review matrix with these four columns:
- **Role**: filename stem from `.craft/roles/`; no invented names
- **Findings**: names a specific artifact surface (section title, field name, diagram
  element, named assumption); not abstract observations
- **Severity**: exactly HIGH, MEDIUM, or LOW; no other values; not blank
- **Recommendation**: names (1) what to do and (2) where in the artifact; not generic

Row order:
1. Challenger primary row(s) (G1 must be OPEN when these are written)
2. Slot-gap escalation rows in slot-letter order (written during G1 OPEN)
3. G1 transitions to CLOSED
4. Domain reviewer rows in selection order (written only after G1 CLOSED)

---

**Property R5 -- Depth selection**
Standard depth (default): 2-3 domain roles whose `expertise.relevance` intersects the
artifact type. Each selection documented in one sentence. No role appears twice.
`--depth deep`: all non-challenger roles in the registry.

---

**Property R6 -- Cross-role synthesis**
The output includes a synthesis block (2-3 sentences) naming at least one convergence
(two roles raised the same concern) or one conflict (two roles disagree). Slot-gap
escalation rows count as findings for convergence detection. If genuinely absent:
`No cross-role signal detected -- findings are non-overlapping.`

---

**Property R7 -- AMEND section**
The output ends with an AMEND section listing at least four specific options:

> **AMEND**
> - Add a challenger: `/crew-review [artifact] --amend add:[challenger-role-name]`
> - Add a domain reviewer: `/crew-review [artifact] --amend add:[role-name]`
> - Full registry run: `/crew-review [artifact] --depth deep`
> - Re-open G1: `/crew-review [artifact] --amend rerun:challengers`

---

Produce the crew-review artifact for the provided input. The artifact satisfies
Properties R1-R7 or is not a valid crew-review output.

---

---

## V-02

**Axis**: Lifecycle emphasis (AMEND as pre-delivery phase with entry condition)
**Hypothesis**: In all prior variations, AMEND is a trailing bulleted section written
after the review matrix. It has no entry condition, no output contract, and produces
generic options regardless of what the review found. This is a lifecycle design flaw:
AMEND options should be derived from the review results. A domain gap found by the
architect should produce an amendment option that names the architect and the gap; an
unfilled null hypothesis slot should produce an amendment option that re-opens G1 for
that slot specifically. This variation restructures the skill as five named lifecycle
phases -- LOAD, CHALLENGE, REVIEW, VALIDATE, AMEND -- where VALIDATE (new) explicitly
checks each matrix row against the schema before committing it, and AMEND has an entry
condition (VALIDATE complete), a derivation rule (options are drawn from findings), and
an output contract (at least one option per unfilled HIGH finding). The hypothesis is
that making AMEND a first-class phase improves C-08 specificity while the VALIDATE phase
improves the reliability of schema criteria (C-02, C-03, C-13) by forcing an explicit
checkpoint before the matrix is finalized.

---

You are running `/crew-review`.

This skill executes in five lifecycle phases. Complete each phase in order. Phase entry
conditions are enforced -- do not begin a phase until its entry condition is met.

---

### PHASE 1 -- LOAD

**Entry**: artifact provided
**Exit**: role pool locked

Read every file in `.craft/roles/`. Extract: role name, `archetype`, `lens.verify`,
`expertise.relevance`.

Error halts -- unconditional, no soft fallback, no partial execution:
- Directory absent: `ERROR: .craft/roles/ not found.` Halt.
- Directory empty: `ERROR: .craft/roles/ is empty.` Halt.
- Any file missing `lens.verify` or `expertise.relevance`:
  `ERROR: [role-name] missing required fields. Registry malformed.` Halt.

Role pool = all files found. Zero roles may be invented.

---

### PHASE 2 -- CHALLENGE

**Entry**: PHASE 1 exit (role pool locked)
**Gate G1 state: OPEN** -- domain review is blocked until G1 closes.

**G1 closure predicate** -- G1 transitions OPEN -> CLOSED when ALL hold:
1. All roles with `archetype: challenger` in the pool have run.
2. The null hypothesis 4-slot form has been attempted for each.
3. Every slot that could not be filled has produced a separate dedicated matrix row per
   the slot-to-row escalation rule below.
4. No slot has been silently omitted, collapsed with another slot, or approximated with
   a generic placeholder ("some cost", "existing workflow").
5. G1 state has been explicitly evaluated and written as `[G1: CLOSED]`.

**Domain review does not begin until G1 transitions to CLOSED.**

---

For each challenger role, fill the 4-slot null hypothesis form:

> **Null hypothesis (4-slot form):**
> - **[SLOT-A]** We currently do ________ instead of building this.
> - **[SLOT-B]** The cost of that alternative is ________.
> - **[SLOT-C]** The switching cost to adopt this artifact is ________.
> - **[SLOT-D]** This artifact is worth acting on only if ________.

Fill each slot from artifact content or inferable workspace context.

**Slot-to-row escalation rule** -- mandatory, per slot:
When a slot cannot be filled from the artifact:
1. Write `[not stated in artifact]` in that slot position.
2. Produce a **separate, dedicated matrix row**:
   | `[role-name]` | SLOT-[letter] gap: [slot label] not stated in artifact. Null hypothesis
   is incomplete without this. | HIGH | State [slot requirement] explicitly in the
   artifact before proceeding. |
3. Do not embed the gap as a sentence within the challenger row's Findings cell.
4. Do not append the gap as a note below the challenger row.
5. Each unfilled slot produces its own dedicated row. Two unfilled = two rows.

Challenger severity (primary row): HIGH if inertia case is credible and unaddressed;
MEDIUM if inertia named but switching cost unstated; LOW if artifact neutralizes it.

Verify G1 closure predicate. All 5 conditions true? Write `[G1: CLOSED]`. Proceed to
PHASE 3.

---

### PHASE 3 -- REVIEW

**Entry**: G1 is CLOSED (PHASE 2 exit)

Depth selection:
- Standard (default): select 2-3 non-challenger roles whose `expertise.relevance`
  intersects the artifact type. Document each: "[role]: selected because [reason]."
- `--depth deep`: all non-challenger roles run.

For each selected domain role:
1. Apply only that role's `lens.verify` perspective.
2. Name a specific artifact surface in each finding.
3. Severity: exactly HIGH, MEDIUM, or LOW.
4. Recommendation: one action naming what to do and where.
5. Do not repeat a finding already raised by a prior reviewer.

Collect all rows (challenger primary, slot-gap escalation, domain) into a draft matrix.
Do not write the final output yet -- PHASE 4 validates the draft first.

---

### PHASE 4 -- VALIDATE

**Entry**: all rows collected (PHASE 3 exit)
**Exit**: matrix validated and finalized

For each row in the draft matrix, verify:
- Role cell: filename stem exists in `.craft/roles/` -- not invented
- Findings cell: names a specific artifact surface -- not an abstract observation
- Severity cell: exactly HIGH, MEDIUM, or LOW -- no freestyle label, not blank
- Recommendation cell: names what to do + where in the artifact -- not generic

If a cell fails: revise it before writing the final matrix. A row that cannot be made
to pass validation is removed from the matrix and logged as:
`[VALIDATION REMOVED: [role] -- [reason]]`

Write the validated matrix:

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|

Row order:
1. Challenger primary row(s) from PHASE 2
2. Slot-gap escalation rows (one per unfilled slot, in slot-letter order)
3. Domain rows in selection order

Write cross-role synthesis (required, 2-3 sentences): name at least one convergence or
conflict. Slot-gap rows count as findings for convergence detection. If absent:
`No cross-role signal detected -- findings are non-overlapping.`

---

### PHASE 5 -- AMEND

**Entry**: PHASE 4 exit (matrix validated and written)
**Output contract**: at least 4 amendment options; at least one option is derived from
a HIGH finding or unfilled slot found in this review run.

Derive AMEND options from review results:
- For each unfilled null hypothesis slot found: include option to re-open G1 with
  that slot's requirement specified.
- For each HIGH domain finding: include option to add a reviewer from the relevant
  expertise domain if one exists in the registry and was not selected.
- Always include: full registry run option and scope-restriction option.

Write the AMEND section:

> **AMEND**
> - [derived option 1: specific to this review's findings]
> - [derived option 2: specific to this review's findings]
> - Full registry run: `/crew-review [artifact] --depth deep`
> - Restrict scope: `/crew-review [artifact] --amend scope:[domain]`
> - Re-open G1: `/crew-review [artifact] --amend rerun:challengers`

Each option must be specific -- name the role, slot, or section it targets. Generic
options ("add more reviewers") are not valid.

---

---

## V-03

**Axis**: Role sequence (numbered execution manifest)
**Hypothesis**: All prior variations determine role execution order at runtime using
rules like "challengers first, then domain roles." The order is computed during
execution and is not visible as a declared artifact before execution begins. This
makes execution order implicit and makes C-06 (depth flag respected) difficult to
verify without counting matrix rows after the fact. This variation introduces an
execution manifest: before any role runs, the model declares a numbered sequence
listing every role that will run, in execution order, with its archetype and relevance
justification. Slot 1 is always the challenger bracket. Slots 2-N are domain roles
ranked by artifact relevance. The manifest is written and committed before execution
begins. The review then executes in manifest order and references slot numbers in
cross-role synthesis ("slot 2 and slot 4 converge on..."). The hypothesis is that a
visible, pre-declared manifest makes execution order a first-class artifact, improves
C-06 verification by making the selection decision explicit before any finding is
written, and enables more precise cross-role convergence/conflict detection by giving
each row a stable reference number.

---

You are running `/crew-review`.

Produce a structured crew review. Execution order is declared as a numbered manifest
before any review runs. The manifest is committed before execution begins.

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

### Step 2 -- Declare execution manifest

Before any role runs, write the execution manifest. The manifest lists every role that
will execute, in order, with its slot number, archetype, and selection rationale.

**Manifest format:**

```
Execution manifest -- crew-review
Depth: [standard | deep]
Artifact type: [inferred from artifact]

Slot 1: [challenger-role-name] (archetype: challenger) -- always runs first
[Slot 2: [role-name] (archetype: [type]) -- selected because [reason tied to artifact]]
[Slot 3: [role-name] (archetype: [type]) -- selected because [reason tied to artifact]]
...
```

Slot assignment rules:
- Slot 1: all roles with `archetype: challenger`. If the registry contains multiple
  challenger roles, they share slot 1 and run sequentially within it.
- Slots 2-N (standard): select 2-3 non-challenger roles whose `expertise.relevance`
  intersects the artifact type. Rank by relevance strength; highest relevance = slot 2.
- Slots 2-N (deep): all non-challenger roles, ranked by relevance then alphabetical.

The manifest is locked after writing. Roles not in the manifest may not appear in the
matrix. Roles in the manifest may not be skipped.

---

### Step 3 -- Challenger bracket (Slot 1)

**Gate G1 state: OPEN.** Domain review is blocked until G1 closes.

**G1 closure predicate** -- G1 transitions OPEN -> CLOSED when ALL hold:
1. All Slot 1 roles have run.
2. The null hypothesis 4-slot form has been attempted for each Slot 1 role.
3. Every slot that could not be filled has produced a dedicated, separate matrix row
   per the slot-to-row escalation rule.
4. No slot has been silently omitted, collapsed, or approximated with a placeholder.

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
2. Produce a **separate, dedicated matrix row**:
   | `[role-name]` | SLOT-[letter] gap: [slot label] not stated. Null hypothesis incomplete. | HIGH | State [slot requirement] explicitly before proceeding. |
3. Do not embed as a sentence within the challenger row's Findings cell.
4. Do not append as a note below the challenger row.
5. Each unfilled slot = one row. Two unfilled slots = two rows.

Generic placeholders count as unfilled. Do not collapse slots.

Challenger severity (primary row): HIGH if inertia is credible and unaddressed; MEDIUM
if inertia named but switching cost unstated; LOW if artifact neutralizes it.

**Verify G1 closure predicate. All 4 conditions true? G1 state: CLOSED.**

---

### Step 4 -- Domain review (Slots 2-N)

**Entry condition: G1 is CLOSED.**

Execute each slot in manifest order. For each slot:
1. Apply only that role's `lens.verify` perspective.
2. Name a specific artifact surface in each finding.
3. Severity: exactly HIGH, MEDIUM, or LOW -- no other values.
4. Recommendation: one action naming what to do and where.
5. Do not repeat a finding already raised by a lower-numbered slot.

---

### Step 5 -- Output

Write the review matrix:

| Slot | Role | Findings | Severity | Recommendation |
|------|------|----------|----------|----------------|

Column constraints:
- **Slot**: integer from the manifest
- **Role**: filename stem from `.craft/roles/`
- **Severity**: exactly HIGH, MEDIUM, or LOW

Row order: Slot 1 primary row(s) first, then slot-gap escalation rows (labeled with
their Slot 1 parent), then Slots 2-N in manifest order.

**Cross-role synthesis** (required, 2-3 sentences): reference slot numbers when naming
convergences or conflicts (e.g., "Slot 1 and Slot 3 both identify the missing switching
cost estimate"). If absent: `No cross-role signal detected -- findings are non-overlapping.`

**AMEND** (required):

> **AMEND**
> - Add to manifest slot [N+1]: `/crew-review [artifact] --amend add:[role-name]`
> - Full manifest: `/crew-review [artifact] --depth deep`
> - Restrict manifest to slots 1-2: `/crew-review [artifact] --amend scope:[domain]`
> - Re-open G1 (rerun slot 1): `/crew-review [artifact] --amend rerun:challengers`

---

---

## V-04

**Axes**: Phrasing register + Inertia framing (peer-voice challenger with state machine gate)
**Hypothesis**: The challenger bracket in all prior variations is written in formal
protocol register: "Gate G1 state: OPEN. Domain review does not begin until G1 transitions
to CLOSED." This register is precise but impersonal -- it describes a mechanism, not a
reason. The challenger role in practice represents a named perspective: the person in
the room who says "wait, why are we building this?" This variation tests whether the
challenger bracket can be written in peer-voice register -- natural language that makes
the inertia argument feel like a real colleague's objection -- while keeping the state
machine gate structurally intact. The challenger introduction uses first-person framing
("Before this reaches the rest of the crew, the inertia-advocate gets the floor. Their
job is the strongest possible case for doing nothing."). The gate definition underneath
this framing is still a typed state machine with OPEN/CLOSED states and a multi-condition
closure predicate. The slot-to-row escalation rule still names its prohibited forms
inside the rule definition. The hypothesis is that phrasing register and structural
mechanism are orthogonal: a conversational challenger introduction does not weaken C-20
(gate states + multi-condition closure) or C-21 (anti-pattern prohibition inside the
escalation rule), while the conversational register may improve C-09/C-11 satisfaction
by making the null hypothesis feel like a genuine argument rather than a form to fill.

---

You are running `/crew-review`.

Route the artifact through the full org. Before any domain reviewer weighs in, the
challenger role makes the case for doing nothing. The challenger bracket closes under
a formal gate; only then do domain reviewers run.

---

### Step 1 -- Load the registry

Read every file in `.craft/roles/`. Extract: role name, `archetype`, `lens.verify`,
`expertise.relevance`.

Error halts -- unconditional, no soft fallback:
- Directory absent: `ERROR: .craft/roles/ not found.` Halt.
- Directory empty: `ERROR: .craft/roles/ is empty.` Halt.
- Any file missing `lens.verify` or `expertise.relevance`:
  `ERROR: [role-name] missing required fields. Registry malformed.` Halt.

Role pool = all files found. Zero roles may be invented.

---

### Step 2 -- The challenger gets the floor

Before this artifact reaches anyone else, it has to answer the strongest version of
"why are we building this instead of doing nothing?" That is the challenger role's job.

Find every role in the pool with `archetype: challenger`. Each one goes first. Their
review opens with a direct null hypothesis: the best case for staying with what the
team already does.

**Challenger bracket gate**

The rest of the review is behind Gate G1. G1 is currently **OPEN**, which means no
domain reviewer runs until the challenger bracket is complete.

G1 has two states: **OPEN** and **CLOSED**.

G1 transitions from OPEN to CLOSED only when all of the following are simultaneously
true:
1. Every role with `archetype: challenger` in the pool has run.
2. The null hypothesis 4-slot form has been attempted for each challenger role.
3. Every slot that could not be filled has produced a dedicated, separate matrix row --
   as defined by the slot-to-row escalation rule below. No slot has been handled any
   other way.
4. No slot has been silently omitted, collapsed with another slot into one sentence,
   or approximated with a generic placeholder ("some cost", "the existing workflow",
   "the current process").
5. G1's closure has been explicitly verified and written as `[G1: CLOSED]`.

**The rest of this review does not run until G1 is CLOSED.**

---

**Null hypothesis -- 4-slot form**

Ask each challenger role to make the "do nothing" case explicit. Fill these four slots
from the artifact content or inferable workspace context:

> - **[SLOT-A]** We currently do ________ instead of building this.
> - **[SLOT-B]** The cost of that alternative is ________.
> - **[SLOT-C]** The switching cost to adopting this artifact is ________.
> - **[SLOT-D]** This artifact is worth acting on only if ________.

If a slot cannot be filled, the artifact has a gap that matters. The slot-to-row
escalation rule applies:

**Slot-to-row escalation rule** -- mandatory, applies to each slot individually:
1. Write `[not stated in artifact]` in that slot position.
2. Log a **separate, dedicated matrix row** for the gap:
   | `[role-name]` | SLOT-[letter] gap: [slot label] not stated in artifact. The null
   hypothesis cannot be evaluated without this. | HIGH | State [slot requirement]
   explicitly in the artifact before this review proceeds. |
3. **This row is a full matrix entry -- it is NOT a sentence embedded within the
   challenger row's Findings cell. It is NOT a note appended below the challenger row.
   It is NOT a parenthetical comment.** A gap finding that is not its own matrix row
   does not satisfy G1 closure condition 3 and does not close the gate.
4. Each unfilled slot = one dedicated row. Two unfilled slots = two separate rows.
   Do not merge them.

How severe is the challenger's primary finding?
- HIGH: the "do nothing" case is credible and the artifact does not address it
- MEDIUM: the status quo is named in the artifact but switching cost is unstated
- LOW: the artifact directly neutralizes the inertia argument

**Verify G1 closure conditions. All 5 true? Write `[G1: CLOSED]`.** G1 is now CLOSED.

---

### Step 3 -- Domain reviewers (after G1 closes)

**Entry condition: G1 is CLOSED.**

Now the rest of the crew runs.

Depth selection:
- Standard (default): pick 2-3 roles (non-challenger) whose `expertise.relevance`
  connects to this artifact. Say in one sentence why each was selected.
- `--depth deep`: run every non-challenger role in the pool.

For each domain role:
1. Apply only that role's `lens.verify` perspective -- not a generic observer's view.
2. Name a specific part of the artifact in each finding: a section, field, diagram
   element, or named assumption.
3. Severity: HIGH / MEDIUM / LOW -- nothing else.
4. Recommendation: one concrete action naming what to do and where in the artifact.
5. Do not repeat a finding already raised by a prior reviewer.

---

### Step 4 -- Output

Write the review as a 4-column table:

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|

Row order: challenger primary row(s) first, then any slot-gap escalation rows in
slot-letter order, then domain rows in selection order.

**Cross-role synthesis** (required, 2-3 sentences): name at least one convergence
(two roles raised the same concern) or one conflict (two roles disagree). Slot-gap rows
count as findings -- if a domain reviewer surfaces the same missing field, that is
convergence. If genuinely absent: `No cross-role signal detected -- findings are
non-overlapping.`

**AMEND** (required):

> **AMEND**
> - Add a reviewer: `/crew-review [artifact] --amend add:[role-name]`
> - Full registry: `/crew-review [artifact] --depth deep`
> - Scope to domain: `/crew-review [artifact] --amend scope:[domain]`
> - Re-open G1 (re-run challenger bracket): `/crew-review [artifact] --amend rerun:challengers`

---

---

## V-05

**Axes**: Lifecycle emphasis + Output format + Role sequence (verification-first maximal)
**Hypothesis**: R5 V-05 achieved the full aspirational stack in a single variation by
combining all mechanisms. It did not include an explicit verification step. The question
is whether the aspirational chain (C-11 through C-21) is more reliably satisfied if the
model explicitly verifies each criterion at a dedicated checkpoint before writing the
final output. This variation adds PHASE 4 VERIFY between domain review and final render:
at that checkpoint, the model produces a criterion-check table listing each aspirational
criterion and whether this output satisfies it (YES/NO/PARTIAL). The verification table
is visible in the output. If any criterion fails verification that the prompt was designed
to satisfy, the relevant phase is re-executed before final render. The hypothesis is that
meta-verification at a dedicated checkpoint catches aspirational criterion failures that
would otherwise surface only at scoring time -- particularly C-20 (gate named states +
closure predicate) and C-21 (anti-pattern prohibition inside escalation rule), which are
construction-time criteria that can satisfy the letter but miss the intent.

The full mechanism stack:
- C-11: null hypothesis 4-slot template (3+ named blanks)
- C-12: per-role lens-lock declaration before findings
- C-13 + C-19: typed 5-column schema with anti-pattern exclusions in column definitions
- C-15: challenger bracket as named execution phase
- C-16 + C-18: slot-level escalation to dedicated HIGH matrix rows
- C-17 + C-20: state machine gate with named OPEN/CLOSED states and multi-condition
  closure predicate
- C-21: anti-pattern prohibition named inside the escalation rule definition itself
- NEW: PHASE 4 VERIFY checkpoint with explicit criterion-check table

---

You are running `/crew-review`.

Reviews execute in five named phases. Output schema is declared before execution. All
rows are validated against schema constraints -- including anti-pattern exclusions --
before being written. The challenger bracket closes under a named state machine gate;
domain review does not begin until the gate transitions to CLOSED. A verification
checkpoint runs before final render.

---

### Output schema (declare before executing)

The final output is a 5-column markdown table.

| Column | Type -- valid | Anti-pattern excluded (NOT valid) |
|--------|--------------|-----------------------------------|
| Role | string -- filename stem from `.craft/roles/` at execution time | NOT: invented names; names from memory or prior runs; any name not present in the registry at this execution |
| Lens | string -- one sentence: "As a [role], I care about [specific concern from `lens.verify`]" | NOT: generic role restatements ("As a PM, I review as a PM"); NOT: concerns borrowed from another role's lens; NOT: multi-sentence declarations |
| Findings | string -- names a specific artifact surface: section title, field name, diagram element, or named assumption | NOT: abstract observations without a named surface ("needs more detail", "unclear", "incomplete", "could be improved"); NOT: observations naming only the artifact as a whole |
| Severity | enum -- exactly `HIGH`, `MEDIUM`, or `LOW`; HIGH = blocks commitment; MEDIUM = must resolve before ship; LOW = advisory | NOT: freestyle labels (Critical, Minor, Warning, Blocker, Moderate, Severe); NOT: blank cells; NOT: combinations ("HIGH/MEDIUM") |
| Recommendation | string -- names (1) what to do and (2) where in the artifact | NOT: generic directives ("review this", "improve this section", "consider adding", "needs clarification"); NOT: recommendations without a named artifact location |

Per-row validation gate: before writing any row, verify all five cells against their
constraints including anti-pattern exclusions. Revise any violating cell before writing.
Do not write a row that fails validation.

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
   exists in the draft output, validated against the output schema above, Severity = HIGH.
4. No unfilled slot has been silently omitted, collapsed into another slot, or
   approximated with a generic placeholder ("some cost", "the existing workflow").

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
   A sentence inside another row's Findings cell is not a dedicated row. A dedicated row
   is a full 5-column entry in the matrix with its own Role, Lens, Findings, Severity,
   and Recommendation cells. Anything else does not satisfy G1 closure condition 3.
4. **Do not append this as a note or comment below the challenger row.** An appended
   note is not a matrix row. It does not satisfy G1 closure condition 3.
5. Each unfilled slot = one dedicated row. Two unfilled slots = two separate rows.
6. Apply the per-row validation gate before writing this row.

**C5** Challenger primary row:
- Lens: "As a [role], I care about [specific concern from this role's lens.verify]."
- Findings: the filled/attempted 4-slot form plus the challenger's primary concern.
- Severity: HIGH (inertia credible, unaddressed) / MEDIUM (named, cost unstated) /
  LOW (artifact directly neutralizes status quo).
- Recommendation: one concrete action naming what to do and where.
- Apply per-row validation gate before writing.

**C6** Verify G1 closure predicate. All 4 conditions true?

Write: `[G1: CLOSED -- conditions 1-4 verified]`

**G1 state: CLOSED.** Proceed to PHASE 3.

Any condition false? Resolve before proceeding.

---

### PHASE 3 -- DOMAIN REVIEW

**Entry**: G1 is CLOSED (PHASE 2 exit)

**D1** Depth selection:
- Standard (default): from roles NOT with `archetype: challenger`, select those whose
  `expertise.relevance` intersects the artifact type. Target 2-4. Document each:
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
   No generic restatement. Concern must be traceable to this role's documented lens.
2. Findings cell: name a specific artifact surface. No abstract observations. No
   repeating a finding already raised by a lower-group or earlier-alphabetical reviewer.
3. Severity: exactly HIGH, MEDIUM, or LOW.
4. Recommendation: what to do + where -- no generic directive.
5. Apply per-row validation gate before writing the row.

---

### PHASE 4 -- VERIFY

**Entry**: all rows collected (PHASE 3 exit)
**Exit**: verification complete; matrix ready for render

Before writing the final output, verify the draft against the aspirational criteria
in the active rubric. Write a criterion-check table:

| Criterion | Description | Status | Evidence in this draft |
|-----------|-------------|--------|------------------------|
| C-11 | Null hypothesis uses 3+ named fill-in slots, all completed | [YES/NO/PARTIAL] | [slot letters present/absent] |
| C-12 | Per-role lens-lock declaration before each role's findings | [YES/NO/PARTIAL] | [present in all rows / missing in [role]] |
| C-13 | Typed column contracts with per-row validation gate visible | [YES/NO/PARTIAL] | [schema table present / validation gate applied] |
| C-15 | Challenger bracket declared as a named execution phase | [YES/NO/PARTIAL] | [PHASE 2 header present / phase name visible] |
| C-16 | Empty slot -> logged HIGH finding per slot | [YES/NO/PARTIAL] | [N escalation rows present for M unfilled slots] |
| C-17 | Challenger phase gate has explicit exit condition blocking domain review | [YES/NO/PARTIAL] | [G1 closure predicate present / blocking statement present] |
| C-18 | Empty-slot escalation produces separate matrix row, not inline annotation | [YES/NO/PARTIAL] | [escalation rows are distinct matrix rows] |
| C-19 | At least one column definition names an explicit anti-pattern exclusion | [YES/NO/PARTIAL] | [column, anti-pattern text cited] |
| C-20 | Gate has named OPEN/CLOSED states and 2+ enumerated closure conditions | [YES/NO/PARTIAL] | [state names present / N closure conditions listed] |
| C-21 | Escalation rule names prohibited output form inside the rule definition | [YES/NO/PARTIAL] | ["Do not embed..." present inside rule / not in separate instruction] |

If any criterion that was designed to be satisfied in this variation scores NO:
- Return to the relevant phase and revise.
- Re-check after revision.

If any criterion scores PARTIAL: note the gap and proceed to PHASE 5 without revision
(PARTIAL is acceptable; revision is only mandatory for NO).

---

### PHASE 5 -- RENDER

**Entry**: PHASE 4 verification complete
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
3. Domain rows in group/alphabetical order

**R3** Cross-role synthesis (required, 2-3 sentences): name at least one convergence
(two roles raised the same concern) or one conflict (two roles disagree). Slot-gap rows
count as findings for convergence detection. If absent: `No cross-role signal detected
-- findings are non-overlapping.`

**R4** AMEND (required):

> **AMEND**
> - Add reviewer (by archetype group): `/crew-review [artifact] --amend add:[role-name]`
> - Full registry: `/crew-review [artifact] --depth deep`
> - Scope to group: `/crew-review [artifact] --amend scope:group[N]`
> - Reopen G1 (re-run challenger bracket): `/crew-review [artifact] --amend rerun:challengers`
> - Re-run single role: `/crew-review [artifact] --amend rerun:[role-name]`

---
