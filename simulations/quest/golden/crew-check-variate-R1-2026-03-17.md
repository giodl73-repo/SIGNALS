---
skill: quest-variate
skill_target: crew-check
date: 2026-03-17
round: 1
rubric: crew-check-rubric-2026-03-17.md
---

# crew-check — Variate R1

5 complete prompt body variations for the `crew-check` skill.
Single-axis first (V-01 through V-03), then two-axis combinations (V-04, V-05).

Registry context assumed: `.craft/roles/signal/` contains `inertia-advocate.md`,
`pm.md`, `architect.md` (and whatever else the workspace adds).

Rubric reminder:
- Essential (must-pass): C-01 role source, C-02 matrix structure, C-03 perspective fidelity,
  C-04 depth compliance, C-05 severity presence
- Recommended: C-06 finding specificity, C-07 recommendation actionability, C-08 severity calibration
- Aspirational: C-09 cross-role synthesis, C-10 AMEND responsiveness

---

## V-01

**Axis**: Role sequence (severity-anchored ordering)
**Hypothesis**: Running roles in decreasing order of expected severity impact — challenger
first, then product, then technical — causes each subsequent reviewer to calibrate against
the severity landscape already established, making C-08 (severity calibration consistency)
a structural property of the output rather than a luck-dependent one.

---

You are running `/crew-check`.

Your task: pass the provided artifact through the registered org roles and produce a
multi-role review matrix. Role execution order is determined by expected severity impact,
not arbitrary sequence.

---

### Step 1 — Load the registry

Read every file in `.craft/roles/`. Build the role pool from only what you find there.
Do not add roles not present in that directory.

If `.craft/roles/` is absent or empty: output `ERROR: .craft/roles/ not found. Halting.`

For each role, record: name, archetype, `orientation.frame`, `expertise.relevance`.

---

### Step 2 — Determine depth and select reviewers

**Standard (default)**: Select 2–4 roles whose domain intersects the artifact type.
Write one sentence per selection: why this role over others for this artifact.
Target: roles whose `expertise.relevance` names a namespace or domain present in the artifact.

**`--depth deep`**: Select all roles. No selection rationale needed — the flag is self-explanatory.

---

### Step 3 — Order by severity footprint

Before running any reviews, sort the selected roles into this execution sequence:

1. `archetype: challenger` — these roles find the highest-severity gaps first
2. `archetype: product` — product risks run second
3. `archetype: technical` — technical risks run third
4. Any remaining archetypes — run last, alphabetically by role name

Within each tier, order alphabetically. This sequence is fixed for the run.

Reason: each reviewer implicitly inherits the severity frame established by prior rows.
A LOW finding late in the run means every prior reviewer already surfaced the real blockers.

---

### Step 4 — Run each reviewer

For each role in sequence order:

- Lock the lens: what does this role actually care about? (one sentence from their
  `orientation.frame` or `lens.verify`)
- Find something specific in the artifact: name the section, field, decision, or assumption
- Assign severity using this consistent scale:
  - **HIGH**: blocks commitment or ship decision
  - **MEDIUM**: must resolve before shipping, does not block commitment
  - **LOW**: advisory, fix if time permits
- Write a recommendation naming (1) what to do and (2) where in the artifact

Do not duplicate a finding already raised by an earlier reviewer.

For `challenger` roles: the finding must name the null hypothesis — what the team does
today instead of this artifact, and whether that alternative is actually worse.

---

### Step 5 — Review matrix

Output the full matrix after all reviews are complete:

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|

Rows appear in execution order (challenger → product → technical → other).

- **Role**: exact name from `.craft/roles/` file stem
- **Findings**: specific observation tied to a named artifact surface
- **Severity**: HIGH / MEDIUM / LOW — these are the only valid values
- **Recommendation**: concrete action naming what and where

---

### Step 6 — Cross-role synthesis

After the matrix, 2–3 sentences:
- Name at least one convergent finding: two roles that independently flagged the same concern
- Name any conflict: roles that disagree on priority or approach
- If neither: write "No cross-role signal detected."

---

### Step 7 — AMEND

> **AMEND**
> - Add reviewer: `/crew-check [artifact] --amend add:[role-name]` *(inserted in archetype sequence)*
> - Full registry: `/crew-check [artifact] --depth deep`
> - Reorder only: `/crew-check [artifact] --amend reorder:[custom sequence]`

---

---

## V-02

**Axis**: Output format (labeled-block format, no table)
**Hypothesis**: Using labeled key-value blocks per reviewer — instead of a table — makes
the four-cell contract (C-02) structurally impossible to violate: each label must have a
value, and a missing label is immediately visible. Tables allow empty cells to hide;
labeled blocks cannot hide what isn't there.

---

You are running `/crew-check`.

Produce a multi-role review of the provided artifact. Output uses labeled blocks, not
a table. Each reviewer gets their own block. No block may have a missing label.

---

### Load

Read `.craft/roles/`. Build role pool from files found. No invented roles.
If directory missing: `ERROR: .craft/roles/ not found.` Stop.

---

### Select

**Standard**: Choose 2–4 roles relevant to the artifact. Note one rationale line per role.
Any `challenger` archetype role is always included.

**`--depth deep`**: Use all roles.

---

### Review

For each selected role, run the review. Then write a labeled block in this exact format:

```
---
Role: [name from .craft/roles/]
Findings: [specific observation tied to a named section, field, or decision in the artifact]
Severity: [HIGH | MEDIUM | LOW]
Recommendation: [concrete action — what to do and where in the artifact]
---
```

Rules:
- Every label must be present and non-empty. A blank value is a structural failure.
- **Findings** must name something specific in the artifact (not generic boilerplate).
- **Severity** must be exactly one of: HIGH, MEDIUM, LOW. No other values.
- **Recommendation** must be actionable: "add X to section Y" not "improve this area."

For `challenger` archetype roles: Findings must include the null hypothesis.
State what the team does today as an alternative, and why this artifact is or is not
demonstrably better.

---

### Synthesis

After all blocks, a synthesis section:

**Convergences** (required): name at least one concern raised by 2+ roles independently.
If none: "No convergent findings across reviewers."

**Conflicts** (optional): name any case where two roles disagree on severity or approach.

---

### AMEND

> **AMEND**
> - Add reviewer: `/crew-check [artifact] --amend add:[role-name]`
> - Full registry: `/crew-check [artifact] --depth deep`
> - Replace a finding: `/crew-check [artifact] --amend rerun:[role-name]`

---

---

## V-03

**Axis**: Lifecycle emphasis (phase-gated, minimal prose)
**Hypothesis**: Structuring the skill as explicit numbered phases — each with a single
pass/fail exit condition before the next phase begins — produces the most reliable C-01
(role traceability) and C-04 (depth compliance) scores, because the model cannot produce
output before role loading is verified and depth is declared.

---

You are running `/crew-check`.

This skill has four phases. Each phase has one exit condition. Do not proceed to the
next phase until the exit condition is met.

---

**PHASE 1 — LOAD**
Exit condition: role pool built and locked.

1. Open `.craft/roles/`.
2. Read every file. Extract: name, archetype, `orientation.frame`, `expertise.relevance`.
3. Role pool = all files found. No additions, no inventions.
4. If directory missing or empty: halt. Output: `ERROR: .craft/roles/ unavailable.`
5. Exit condition met when pool contains at least one role.

---

**PHASE 2 — SELECT**
Exit condition: reviewer queue declared and rationale written.

1. Check for `--depth deep`:
   - Present → queue = entire pool. Depth = deep. Go to step 4.
   - Absent → depth = standard. Continue.
2. (Standard) Select 2–4 roles whose `expertise.relevance` intersects the artifact type.
   Always include `challenger` archetype roles regardless of relevance score.
3. Write one rationale line per selected role: `[name]: selected because [reason].`
4. Output at top of result: `Depth: [standard|deep] | Roles: [comma-separated names]`
5. Exit condition met when queue is non-empty and rationale is written.

---

**PHASE 3 — EXECUTE**
Exit condition: all queued roles have a validated review row.

For each role in queue (challenger archetype first, then others):

a. Lens: what does this role care about? (one sentence from their `orientation.frame`)
b. Finding: what does the artifact do or fail to do for this lens?
   — Must name a specific surface: section title, field name, diagram element, stated assumption.
   — Generic observations without an artifact surface fail validation.
c. Severity: HIGH (blocks commitment) / MEDIUM (fix before ship) / LOW (advisory).
   Only these three values are valid.
d. Recommendation: one concrete action. Must name what and where. Generic directives fail.

For challenger roles: finding must name the null hypothesis (what the team does today
instead of this artifact, and whether that is demonstrably worse).

Validate each row before writing it. If any cell fails: revise, then write.

---

**PHASE 4 — RENDER**
Exit condition: complete output delivered.

R1. Header block:
```
Crew Check: [artifact name]
Depth: [standard|deep]
Roles: [list]
```

R2. Review matrix:
```
| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|
[rows in execution order]
```

R3. Cross-role synthesis (required):
2–3 sentences naming at least one convergence or conflict.
If none: "No cross-role signal detected."

R4. AMEND block (required):
> **AMEND**
> - Add reviewer: `/crew-check [artifact] --amend add:[role-name]`
> - Full registry: `/crew-check [artifact] --depth deep`
> - Scope restriction: `/crew-check [artifact] --amend scope:[domain]`

Output complete. Phase 4 exit condition met.

---

---

## V-04

**Axes**: Output format + Phrasing register (combination)
**Hypothesis**: A schema-first contract (format defined before any execution)
combined with formal, declarative register ("each row SHALL contain") eliminates C-02
and C-05 failures structurally — the schema makes blank cells impossible; formal SHALL
language makes the model treat each constraint as binding rather than advisory, which
also improves C-03 (perspective fidelity) by forcing explicit role-lens anchoring
before each finding.

---

You are running `/crew-check`.

**Output contract is defined here. It applies to every row of output. Read it before executing.**

---

### Output contract

The primary deliverable is a review matrix. Every row in the matrix SHALL conform to:

| Column | Constraint |
|--------|-----------|
| Role | SHALL be the filename stem of a role file in `.craft/roles/`. MAY NOT be invented. |
| Findings | SHALL name at least one specific artifact surface — a section heading, a named field, a diagram element, or a stated assumption. SHALL reflect the reviewing role's documented orientation, not generic review voice. |
| Severity | SHALL be exactly one of: `HIGH`, `MEDIUM`, `LOW`. No other values are permitted. HIGH = blocks commitment. MEDIUM = must resolve before ship. LOW = advisory. |
| Recommendation | SHALL be a concrete action naming (1) what to do and (2) where in the artifact. SHALL NOT be a generic directive such as "improve this" or "address the concern." |

A row that violates any constraint SHALL be revised before appearing in the output.

The output also SHALL contain:
- A selection rationale block (standard depth only)
- A cross-role synthesis block (all depths)
- An AMEND block (all depths)

---

### Execution

**Stage 1 — Registry**

Read `.craft/roles/`. Build the available role pool from the files present.
The pool is strictly limited to discovered files. If `.craft/roles/` is absent:
output `ERROR: .craft/roles/ not found.` Execution halts.

**Stage 2 — Role selection**

Apply depth rule:
- Standard (default): select 2–4 roles whose documented `expertise.relevance` intersects
  the artifact's type, namespace, or subject. Roles with `archetype: challenger` SHALL
  always be selected in standard depth.
- `--depth deep`: select all roles. No selection rationale required.

For standard depth, write the selection rationale:
`[role-name] selected: [one sentence tying their relevance to this artifact's content].`

**Stage 3 — Review execution**

Execute roles in this order: challenger archetype first, then all other selected roles.

For each role:

1. Anchor the lens: quote or paraphrase one line from the role's `orientation.frame`
   or `lens.verify` to establish the perspective for this review.
2. Produce finding: locate something in the artifact this lens would flag.
   Name the artifact surface explicitly.
3. Assign severity per contract.
4. Write recommendation per contract.
5. Validate row against output contract. If any cell fails: revise before proceeding.

For `challenger` archetype roles: the Findings cell SHALL include the null hypothesis.
Format: "The team currently [X] instead of this. That alternative is [better/equivalent/worse]
because [reason]. This artifact justifies acting only if [condition]."

**Stage 4 — Output**

Write the review matrix. Then:

**Cross-role synthesis** (required):
2–3 sentences. SHALL name at least one convergence (two roles flagged the same concern)
or one conflict (two roles assign different severity to the same surface).
If neither: "No cross-role signal detected across this reviewer set."

**AMEND** (required):

> **AMEND**
> - Add reviewer: `/crew-check [artifact] --amend add:[role-name]`
> - Full registry: `/crew-check [artifact] --depth deep`
> - Restrict scope: `/crew-check [artifact] --amend scope:[domain]`
> - Amend finding: `/crew-check [artifact] --amend rerun:[role-name]`

---

---

## V-05

**Axes**: Role sequence + Inertia framing + Lifecycle emphasis (full integration)
**Hypothesis**: The full integration approach — archetype-sequenced execution,
an explicit inertia mandate embedded as the Phase 1 exit condition, and phase-gated
lifecycle — produces the highest composite score by addressing each rubric tier
with a dedicated structural guarantee: C-01/C-04 via phase gates; C-02/C-05 via
row validation; C-03/C-08 via archetype sequencing; C-06/C-07 via specificity rules;
C-09 via required synthesis; C-10 via AMEND block.

---

You are running `/crew-check`.

This skill runs in four phases with hard exit conditions. Role execution is structured
by archetype tier. The inertia case is the first thing produced — before any domain review.

---

## PHASE 1 — REGISTRY + INERTIA

**Entry condition**: artifact provided
**Exit condition**: role pool locked AND null hypothesis on the table

**P1.1** Open `.craft/roles/`. Read every file.
Extract from each: name, archetype, `orientation.frame`, `expertise.relevance`.
Role pool = all files discovered. Zero roles may be invented.
If `.craft/roles/` missing: output `ERROR: registry unavailable.` Halt.

**P1.2** Identify all roles with `archetype: challenger`. They run in this phase.

**P1.3** For each challenger role, produce the inertia finding before any other review:

> State the null hypothesis explicitly:
> "The team currently does [X] instead of this artifact. That alternative costs [Y]
> in effort/time/risk. This artifact is worth acting on only if [Z]."
>
> Fill all three variables from artifact content. If the artifact does not name what
> it replaces, that is itself the challenger's finding: HIGH severity, because an
> artifact that doesn't know its alternative cannot justify the switching cost.
>
> Severity logic for challenger roles:
> - HIGH: inertia case is credible and unaddressed in the artifact
> - MEDIUM: inertia is named but switching cost is not quantified
> - LOW: artifact directly neutralizes the status quo argument with evidence

**P1.4** Write the challenger row(s) to a staging buffer. Do not render yet.

**Exit condition met**: pool locked and all challenger rows staged.

---

## PHASE 2 — SELECT

**Entry condition**: Phase 1 complete
**Exit condition**: full reviewer queue declared

**P2.1** Check depth flag:
- `--depth deep`: queue = full pool. Depth = deep. Skip to P2.3.
- Absent: depth = standard. Continue.

**P2.2** (Standard only) From non-challenger roles, select 2–3 whose
`expertise.relevance` or `orientation.frame` intersects the artifact's content.
Write one rationale sentence per selection.

**P2.3** Final queue = challenger roles (from Phase 1) + selected domain roles.
Output at document top: `Depth: [standard|deep] | Roles: [names in execution order]`

**Exit condition met**: queue finalized, rationale written.

---

## PHASE 3 — DOMAIN REVIEWS

**Entry condition**: Phase 2 complete
**Exit condition**: all non-challenger queue members have validated review rows

For each domain role in queue order:

1. **Lock the lens** (one sentence from `orientation.frame`): establishes what this
   role cares about, distinct from every other role.
2. **Find**: locate something in the artifact this lens would flag. Name the artifact
   surface — section title, field, assumption, diagram element. No unnamed surfaces pass.
3. **Severity**: HIGH / MEDIUM / LOW. Only these three values.
4. **Recommendation**: one concrete action naming what to do and where. Not a directive.

Do not repeat a finding already staged by a challenger reviewer.

Validate each row before staging:
- Role name matches a `.craft/roles/` file
- Finding names a specific artifact surface
- Severity is exactly HIGH, MEDIUM, or LOW
- Recommendation is concrete (names what and where)

If any cell fails: revise before staging.

**Exit condition met**: all queued roles have validated rows staged.

---

## PHASE 4 — RENDER

**Entry condition**: all rows staged (Phase 1 challenger rows + Phase 3 domain rows)
**Exit condition**: complete output delivered

**R1. Header**
```
Crew Check: [artifact name or type]
Depth: [standard|deep]
Roles: [list in execution order]
```

**R2. Review matrix** — flush from staging buffer, challenger rows first:

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|
*[one row per reviewer, in execution order]*

**R3. Cross-role synthesis** (required):
2–3 sentences. Name at least one:
- **Convergence**: two or more roles independently flagged the same concern area
- **Conflict**: two roles assign different severity to the same artifact surface

If neither exists: "No cross-role signal detected — findings are non-overlapping."

**R4. AMEND block** (required):

> **AMEND**
> - Add reviewer (inserted in archetype sequence): `/crew-check [artifact] --amend add:[role-name]`
> - Full registry run: `/crew-check [artifact] --depth deep`
> - Skip inertia phase: `/crew-check [artifact] --amend skip:challengers` *(changes output contract)*
> - Re-run single role: `/crew-check [artifact] --amend rerun:[role-name]`
> - Restrict to domain: `/crew-check [artifact] --amend scope:[domain]`

Output complete. Phase 4 exit condition met.

---
