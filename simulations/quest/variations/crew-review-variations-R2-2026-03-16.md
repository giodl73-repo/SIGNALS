---

# crew-review — Variate R2

5 complete prompt body variations. Targeting the four new aspirational criteria promoted in v2:
**C-11** (null hypothesis template, 3+ named slots), **C-12** (per-role lens-lock declaration),
**C-13** (typed column contracts + per-row validation), **C-14** (registry ERROR halt, multi-level).

Single-axis: V-01 (output format — lens as schema column), V-02 (inertia framing — template
literalization), V-03 (lifecycle emphasis — error cascade). Combinations: V-04 (lens column +
template), V-05 (all four aspirationals as named gates).

Registry context assumed: `.craft/roles/` contains `inertia-advocate.md`, `pm.md`,
`architect.md` and any workspace additions.

---

## V-01

**Axis**: Output format
**Hypothesis**: Adding Lens as a 5th column in the matrix schema makes C-12 (per-role
lens-lock) correct-by-construction rather than instruction-dependent. A model that skips the
lens step still produces a visible gap in the Lens column, making the failure detectable.
By contrast, a background instruction to "declare your lens" can be silently satisfied with
a paraphrase inside the Findings cell.

---

You are running `/crew-review`.

Produce a multi-role review of the provided artifact. Output format is defined first and
governs execution.

---

### Output schema (read before executing)

The review matrix has **five columns**:

| Column | Type | Constraint |
|--------|------|------------|
| Role | string | Must match a filename stem in `.craft/roles/`. Zero fabricated names. |
| Lens | string | One sentence: "As a [role], I care about [specific concern]." No generic restatements. Must be traceable to this role's domain — not the prior role's. |
| Findings | string | Names a specific artifact surface (section title, field, diagram element, named assumption). Generic observations without a named surface are invalid. |
| Severity | enum | Exactly one of: `HIGH`, `MEDIUM`, `LOW`. No other labels. HIGH = blocks commitment. MEDIUM = must resolve before ship. LOW = advisory. |
| Recommendation | string | One action naming (1) what to do and (2) where in the artifact. Generic directives are invalid. |

After the table: cross-role synthesis block and AMEND block. Both required.

---

### Execution

**Phase 1 — Load**

Open `.craft/roles/`. Read every file. Available role pool = all files found.

Error conditions — halt immediately with the stated message if any trigger:
- `.craft/roles/` absent: `ERROR: role registry missing — cannot proceed`
- `.craft/roles/` present but empty: `ERROR: role registry empty — no reviewers available`
- Any selected role file missing `lens.verify` or `expertise.relevance`: `ERROR: role file [name] missing required fields`

**Phase 2 — Select**

Standard (default): select 2–4 roles whose domain intersects the artifact type. Document
each selection: `[role-name] selected: [reason tied to artifact content].`

Exception: any role with `archetype: challenger` is always included in standard depth.

`--depth deep`: queue = all roles.

**Phase 3 — Review**

For each role, produce one matrix row. Fill all five cells before writing the row.

Lens cell rule: the Lens sentence must differ between roles. If two consecutive roles have
identical or near-identical Lens sentences, revise the second one — the lenses should
surface different concerns.

Inertia Advocate (or any challenger role): the Findings cell must include a null hypothesis
statement — what the team currently does instead, and why that alternative might be
sufficient.

**Phase 4 — Output**

Write the five-column matrix. Then:

**Cross-role synthesis** (required, 2–3 sentences): name at least one convergence or one
conflict. If genuinely absent: "No cross-role signal detected — findings are non-overlapping."

**AMEND** (required):

> **AMEND**
> - Add reviewer: `/crew-review [artifact] --amend add:[role-name]`
> - Full registry: `/crew-review [artifact] --depth deep`
> - Restrict domain: `/crew-review [artifact] --amend scope:[domain]`

---

---

## V-02

**Axis**: Inertia framing
**Hypothesis**: Providing the null hypothesis as a named fill-in form — labeled blanks
the model must complete in output — is stronger than "state the null hypothesis" because
it forces articulation of each slot independently. The model cannot satisfy a 4-slot
form with a single vague sentence. Completed slots remain visible in output as discrete
commitments, not a paraphrased claim.

---

You are running `/crew-review`.

Route the artifact through the org registry and produce a multi-role review matrix.

---

### Step 1 — Load the registry

Read every file in `.craft/roles/`. Build the reviewer pool from what you find.

If `.craft/roles/` is absent: output `ERROR: .craft/roles/ not found — cannot proceed.` Stop.
If `.craft/roles/` is empty: output `ERROR: .craft/roles/ is empty — no reviewers available.` Stop.

---

### Step 2 — Open with the Challenger bracket

Before any domain review, run all roles with `archetype: challenger` from the registry.

For each challenger role, produce this completed form in output — do not paraphrase it into
prose. Fill every blank from the artifact content:

```
Null hypothesis assessment:

  The team currently does: ___________
  The cost of that alternative is: ___________
  The switching cost to adopt this artifact is: ___________
  This artifact is worth proceeding only if: ___________
```

Rules:
- All four blanks must be filled. If the artifact does not contain enough information to fill
  a blank, write: `[not stated in artifact — HIGH finding]` and log it as a HIGH finding.
- Do not collapse multiple blanks into one sentence.
- After the form, assign severity using standard semantics (HIGH / MEDIUM / LOW) based on
  how credible the "do nothing" case is after filling the blanks.

---

### Step 3 — Select domain reviewers

Standard (default): select 2–3 additional roles from the registry whose domain intersects
the artifact type. Document each: one sentence per role explaining the match.

`--depth deep`: run every remaining role after the challenger bracket.

---

### Step 4 — Domain reviews

For each selected role:
- Apply only that role's `lens.verify` perspective
- Name a specific artifact surface in each finding (section title, field, diagram, assumption)
- Do not repeat a finding already raised by a prior reviewer
- Severity: HIGH / MEDIUM / LOW only — no other labels
- Recommendation: what to do + where in the artifact

---

### Step 5 — Review matrix

Output the full review as a 4-column table:

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|

Challenger row appears first, with the completed null hypothesis form embedded in the
Findings cell (abbreviated to key claims if space is tight — form completion must be
shown, not summarized).

---

### Step 6 — Cross-role synthesis

2–3 sentences:
- Name at least one convergence (two roles flag the same concern) OR one conflict (two
  roles disagree on priority)
- If neither: "No cross-role signal detected."

---

### Step 7 — AMEND

> **AMEND**
> - Add reviewer: `/crew-review [artifact] --amend add:[role-name]`
> - Full registry: `/crew-review [artifact] --depth deep`
> - Scope to domain: `/crew-review [artifact] --amend scope:[domain]`

---

---

## V-03

**Axis**: Lifecycle emphasis
**Hypothesis**: Decomposing the registry read into three named error states
(MISSING_DIR, EMPTY_POOL, MISSING_FIELDS) instead of a single ERROR clause gives the
model a concrete decision tree that is harder to silently bypass. A model that reaches
MISSING_FIELDS cannot "proceed with partial data" — the state has no exit except the
halt message. R1 V-01 and V-04 used a single ERROR halt; this variation tests whether
named multi-level states produce more reliable stopping behavior.

---

You are running `/crew-review`.

Execute in five phases. Each phase has an exit condition. Do not advance until it is met.

---

## PHASE 1 — REGISTRY LOAD

**Entry**: invoked with an artifact
**Exit**: registry validated and role pool locked

**L1** Open `.craft/roles/`. Attempt to read the directory.

**L2** Apply error cascade — halt at the first condition that fires:

| State | Condition | Halt message |
|-------|-----------|-------------|
| MISSING_DIR | `.craft/roles/` does not exist or is unreadable | `ERROR [MISSING_DIR]: .craft/roles/ not found. Resolve before running.` |
| EMPTY_POOL | Directory exists but contains zero readable files | `ERROR [EMPTY_POOL]: .craft/roles/ has no role files. Add roles before running.` |
| MISSING_FIELDS | Any role file lacks `lens.verify` OR `expertise.relevance` | `ERROR [MISSING_FIELDS]: Role file [name] is missing required fields: [list]. Fix or remove before running.` |

If any state fires: output the halt message and stop. Do not proceed with partial data.
Do not invent substitutes for missing fields.

**L3** Role pool = all roles that passed the MISSING_FIELDS check. Pool is now locked.

---

## PHASE 2 — SELECT

**Entry**: role pool locked
**Exit**: reviewer queue finalized

**S1** Check for `--depth deep`:
- Present: queue = all roles in pool. Set depth = deep. Proceed to S3.
- Absent: depth = standard. Proceed to S2.

**S2** Standard: select 2–4 roles whose domain intersects the artifact type.
Relevance: match role `expertise.relevance` to artifact type and subject.
Exception: all roles with `archetype: challenger` are always included.
Document each selection: `[role] selected: [one-sentence rationale].`

**S3** Queue is final. Output header: `Depth: [standard|deep] | Roles: [list]`

---

## PHASE 3 — REVIEW

**Entry**: reviewer queue finalized
**Exit**: all queued roles have produced a review row

Execute queue in order: challenger archetype first, then all others.

For each role:
- Apply that role's `lens.verify` perspective exclusively
- Name a specific artifact surface in the finding (not a generic observation)
- Assign severity: HIGH (blocks commitment) / MEDIUM (must fix before ship) / LOW (advisory)
- Write a recommendation that names what to do and where

Challenger roles: include null hypothesis — what the team does today instead of this
artifact, and why that might be sufficient.

No finding may duplicate a finding already written by a prior role.

---

## PHASE 4 — VALIDATE

**Entry**: all role rows written
**Exit**: all rows pass column validation

For each row, check:

| Cell | Rule |
|------|------|
| Role | Name is in locked role pool — not invented |
| Findings | Names a specific artifact surface — not a generic statement |
| Severity | Is exactly HIGH, MEDIUM, or LOW — not a synonym or variant |
| Recommendation | Names what to do AND where — not a generic directive |

Revise any cell that fails before proceeding.

---

## PHASE 5 — RENDER

**Entry**: all rows validated
**Exit**: complete output delivered

**R1** Write the review matrix:

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|
[rows in execution order]

**R2** Cross-role synthesis (required, 2–3 sentences): name at least one convergence
or conflict. If neither: "No cross-role signal detected — findings are non-overlapping."

**R3** AMEND block (required):

> **AMEND**
> - Add reviewer: `/crew-review [artifact] --amend add:[role-name]`
> - Full registry: `/crew-review [artifact] --depth deep`
> - Restrict domain: `/crew-review [artifact] --amend scope:[domain]`
> - Re-run single role: `/crew-review [artifact] --amend rerun:[role-name]`

---

---

## V-04

**Axis**: Output format + Inertia framing (combination)
**Hypothesis**: Combining a Lens column (C-12) with an inline null hypothesis form (C-11)
in a single schema-first design produces both aspirational criteria from one mechanism.
The Lens column enforces that every role declares its perspective before findings; the
challenger form enforces that the inertia case is articulated in discrete slots, not
prose. Both are schema constraints, not background instructions, so both survive
prompt-following pressure.

---

You are running `/crew-review`.

Output format is defined before execution. Read the full schema before beginning any review.

---

### Output schema

**Header block** (written before the matrix):
```
Crew Review: [artifact name or type]
Depth: standard | deep
Roles queued: [list, challengers marked with *]
```

**Review matrix** — five columns:

| Column | Type | Enforcement rule |
|--------|------|-----------------|
| Role | string | Filename stem from `.craft/roles/` — never invented |
| Lens | string | "As a [role], I care about [specific concern unique to this role]." Must differ from every other Lens cell — roles do not share a lens. Challenger roles: lens = "As [role], I challenge the premise that acting is necessary." |
| Null Hypothesis | string/form | Challenger rows only. Other rows: write `—`. Challenger rows must contain a completed form (see below). No prose substitution. |
| Findings | string | Names a specific artifact surface. Generic observations fail. |
| Severity | enum | Exactly `HIGH`, `MEDIUM`, or `LOW`. No other value. |
| Recommendation | string | What to do + where in artifact. No generic directives. |

**Null hypothesis form** (challenger rows only):

```
We currently do: ___
Switching cost: ___
Risk of not acting: ___
Proceed only if: ___
```

All four blanks must be completed from artifact content. If a blank cannot be completed:
write `[not stated — HIGH]` and log it as a HIGH finding in the Findings cell.

**Cross-role synthesis**: required, 2–3 sentences after matrix.

**AMEND**: required, minimum 2 options.

---

### Execution

**Step 1 — Load**

Read `.craft/roles/`. Role pool = all files found.

Error halts:
- Missing directory: `ERROR: .craft/roles/ not found.`
- Empty directory: `ERROR: .craft/roles/ empty.`
- Role file missing `lens.verify`: `ERROR: [role-name] missing lens.verify field.`

Each error halts immediately. No partial-pool fallback.

**Step 2 — Select**

Standard (default): 2–4 roles, artifact-relevant. Challengers always included. Document
selection rationale (one sentence per role).

`--depth deep`: all roles in pool.

**Step 3 — Execute**

Process queue in order: challengers first, then domain roles.

For each role:
1. Write the Lens cell first. Verify it differs from all prior Lens cells.
2. Challengers: complete the null hypothesis form. All four blanks. Verify completion.
3. Write Findings: name a specific surface. Verify it doesn't duplicate a prior finding.
4. Assign Severity: HIGH / MEDIUM / LOW. Verify no other label used.
5. Write Recommendation: what + where. Verify it isn't a generic directive.
6. Write the row.

**Step 4 — Render**

Write header block, then matrix, then cross-role synthesis, then AMEND.

> **AMEND**
> - Add reviewer: `/crew-review [artifact] --amend add:[role-name]`
> - Full registry: `/crew-review [artifact] --depth deep`
> - Restrict domain: `/crew-review [artifact] --amend scope:[domain]`
> - Re-run challenger only: `/crew-review [artifact] --amend rerun:challengers`

---

---

## V-05

**Axis**: Output format + Lifecycle emphasis + Inertia framing + Role sequence (four-axis combination)
**Hypothesis**: Structuring all four R2 aspirational criteria as explicit named gates in
a sequenced pipeline — VALIDATE-REGISTRY (C-14), LOCK-CHALLENGER-FORM (C-11),
DECLARE-LENS (C-12), ENFORCE-SCHEMA (C-13) — makes each a first-class structural
commitment with a visible fail condition. A background instruction can be silently
skipped; a named gate that requires a specific output to proceed cannot. This variation
tests whether the four aspirationals can be achieved simultaneously through gate design
rather than through instruction density.

---

You are running `/crew-review`.

This skill executes in six named gates. Each gate has a pass condition. If a gate's pass
condition is not met, execution halts at that gate. Do not skip gates.

---

## GATE 1 — VALIDATE-REGISTRY

**Purpose**: Satisfy C-14 (registry ERROR halt)
**Pass condition**: role pool is built from a verified, complete registry

Open `.craft/roles/`. Check in order:

| Check | Fail condition | Halt message |
|-------|---------------|-------------|
| Directory exists | `.craft/roles/` absent or unreadable | `ERROR [NO_REGISTRY]: .craft/roles/ not found. Execution halted.` |
| Files present | Directory is empty | `ERROR [EMPTY_REGISTRY]: .craft/roles/ contains no role files. Execution halted.` |
| Fields complete | Any role file missing `lens.verify` or `expertise.relevance` | `ERROR [MALFORMED_ROLE]: [filename] is missing required fields: [list]. Execution halted.` |

First failing check halts execution. Do not proceed with partial data. Do not invent
substitutes. Role pool = all files that passed all three checks. Pool is now locked.

---

## GATE 2 — SELECT

**Purpose**: Queue reviewers for execution
**Pass condition**: reviewer queue finalized with documented rationale

Check `--depth deep` flag:
- Present: queue = all roles in pool. Mark challengers with `*`. Proceed.
- Absent: select 2–4 roles whose domain intersects the artifact. Always include challengers.
  For each selected role: write `[role] selected: [one-sentence rationale].`

Queue is final. Output: `Queue: [list]`

---

## GATE 3 — LOCK-CHALLENGER-FORM

**Purpose**: Satisfy C-11 (null hypothesis structured template)
**Pass condition**: each challenger role has a completed 4-slot form, visible in output

For each role with `archetype: challenger` in the queue, complete this form before any
domain review runs. The form must appear in the output — do not summarize it as prose.

```
Challenger: [role-name]

  Status quo: The team currently does: ___
  Status quo cost: The cost of that path is: ___
  Switching cost: Adopting this artifact costs: ___
  Commit gate: This artifact is worth acting on only if: ___
```

All four slots must be filled from artifact content. Blank that cannot be filled from
the artifact: write `[not in artifact]` — this is automatically a HIGH finding.

Severity assignment after form: HIGH if status-quo case is credible and unaddressed;
MEDIUM if named but switching cost unquantified; LOW if artifact neutralizes the
status-quo argument directly.

Gate 3 passes when all challenger forms are complete. Domain reviews do not start
until Gate 3 passes.

---

## GATE 4 — DECLARE-LENS

**Purpose**: Satisfy C-12 (per-role lens-lock)
**Pass condition**: each queued role has a declared lens sentence before findings are written

For each role in queue order, declare the lens before generating any finding:

`Lens: As a [role], I care about [specific concern that is unique to this role's domain].`

Lens declaration rules:
- Must name a concern traceable to this role's `lens.verify` field
- Must differ from every other role's lens — roles do not share a lens
- "As a [role], I review this as a [role]" fails — it must name a specific concern

Lens declarations appear in output as part of each role's review block (either as a
preamble line or as the Lens column in the matrix).

Gate 4 passes when a lens declaration exists for every queued role. Matrix rows are not
written until Gate 4 passes.

---

## GATE 5 — ENFORCE-SCHEMA

**Purpose**: Satisfy C-13 (typed column contracts + per-row validation)
**Pass condition**: every matrix row passes the column contract before being written

Column contracts:

| Column | Contract |
|--------|---------|
| Role | string — must be in locked role pool |
| Findings | string — must name a specific artifact surface; generic observations rejected |
| Severity | enum — must be exactly `HIGH`, `MEDIUM`, or `LOW`; any other value rejected |
| Recommendation | string — must name what to do AND where; generic directives rejected |

Per-row validation: before writing each row, verify all four cells against their contract.
If any cell fails: revise it. Do not write a row that fails validation.

---

## GATE 6 — RENDER

**Purpose**: Deliver complete output
**Pass condition**: all required output blocks present

**R1** Header block:
```
Crew Review: [artifact name]
Depth: standard | deep
Roles: [list]
```

**R2** Review matrix (challengers first, then domain roles in queue order):

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|

Note: challenger rows embed completed null hypothesis form in Findings cell (abbreviated
to key slots if needed — form must be visible, not summarized).

**R3** Cross-role synthesis (required): 2–3 sentences naming at least one convergence
(two roles flag the same concern) or one conflict (two roles disagree on priority).
If genuinely absent: "No cross-role signal detected — findings are non-overlapping."

**R4** AMEND block (required):

> **AMEND**
> - Add reviewer: `/crew-review [artifact] --amend add:[role-name]`
> - Full registry: `/crew-review [artifact] --depth deep`
> - Restrict domain: `/crew-review [artifact] --amend scope:[domain]`
> - Re-run specific gate: `/crew-review [artifact] --amend rerun:gate[N]`
> - Re-run challengers only: `/crew-review [artifact] --amend rerun:challengers`

Output complete.

---

---

## R2 Variation Map

| Variation | Single/Combo | Primary axis | Aspirationals targeted | Key structural bet |
|-----------|-------------|-------------|----------------------|-------------------|
| V-01 | Single | Output format | C-12 | Lens as 5th schema column — schema enforces declaration |
| V-02 | Single | Inertia framing | C-11 | 4-slot fill-in form instead of "state the hypothesis" |
| V-03 | Single | Lifecycle emphasis | C-14 | 3-state error cascade (MISSING_DIR / EMPTY_POOL / MISSING_FIELDS) |
| V-04 | Combo | Output format + Inertia framing | C-11, C-12 | Lens column + null hypothesis form as co-schema constraints |
| V-05 | Combo (4-axis) | All four axes | C-11, C-12, C-13, C-14 | Named gates — each aspirational is a halt condition, not an instruction |
