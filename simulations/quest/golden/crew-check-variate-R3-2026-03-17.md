---
skill: quest-variate
skill_target: crew-check
date: 2026-03-17
round: 3
rubric: crew-check-rubric-v3-2026-03-17.md
---

# crew-check — Variate R3

5 complete prompt body variations for the `crew-check` skill.
Single-axis first (V-01 through V-03), then two-axis combinations (V-04, V-05).

Registry context assumed: `.craft/roles/signal/` contains `inertia-advocate.md`,
`pm.md`, `architect.md` (and whatever else the workspace adds).

Rubric v3 reminder:
- Essential (must-pass): C-01 role source, C-02 matrix structure, C-03 perspective fidelity,
  C-04 depth compliance, C-05 severity presence
- Recommended: C-06 finding specificity, C-07 recommendation actionability, C-08 severity calibration
- Aspirational (v2): C-09 cross-role synthesis, C-10 AMEND responsiveness,
  C-11 lens-anchoring step, C-12 severity calibration contract, C-13 challenger-first sequencing
- Aspirational (v3 additions): C-14 readiness-gate framing, C-15 severity-sorted matrix output,
  C-16 hard-halt execution gate

Design intent for R3: All five variations structurally enforce C-11, C-12, and C-13 (R2 floor).
Single-axis variations target one of the three v3 criteria each. V-04 combines C-14+C-16.
V-05 targets all three v3 criteria simultaneously.

Axes selected for R3:
- V-01: Readiness-gate framing (C-14)
- V-02: Hard-halt execution gate (C-16)
- V-03: Phrasing register — interrogative/diagnostic (new territory; softer C-14+C-16)
- V-04: Readiness-gate + Hard-halt (C-14 + C-16)
- V-05: Readiness-gate + Hard-halt + Severity-sorted (C-14 + C-16 + C-15)

---

## V-01

**Axis**: Readiness-gate framing
**Hypothesis**: Framing every transition as a readiness assertion — "you are not ready to
advance past this gate until its condition is met" — targets C-14 systematically rather
than incidentally. R2 V-02 used "If you haven't done this step, you're not ready to write
the finding" as a one-off coaching line; V-01 makes readiness the structural idiom of every
transition. The effect: prerequisites become gates the execution cannot pass through, not
instructions it can choose to treat as advisory. The lens-anchor gate ("you are not ready
to write the finding until the lens is written") becomes one instance of a universal pattern
rather than a special-case mandate — which should produce more reliable C-11 compliance
because the model applies the same posture everywhere.

---

You are running `/crew-check`.

Your task: pass the provided artifact through the registered org roles and produce a
multi-role review matrix. This skill is organized as a sequence of readiness gates. You are
not ready to advance past any gate until its condition is fully met.

---

### Gate 1 — Registry

**You are not ready to select reviewers until this gate is passed.**

Read every file in `.craft/roles/`. Build the role pool from only what you find there.
Do not add roles not present in that directory.

For each role, record: name, archetype, `orientation.frame`, `expertise.relevance`.

If `.craft/roles/` is absent or empty: output `ERROR: .craft/roles/ not found. Cannot proceed.`
Stop. You are not ready.

Gate 1 passed when: pool contains at least one role sourced exclusively from `.craft/roles/`.

---

### Gate 2 — Severity contract

**You are not ready to run any reviewer until this gate is passed.**

Write and lock the scale you will use for every row. No additions. No deviations.

| Label | Operational meaning |
|-------|---------------------|
| HIGH | Blocks commitment or ship decision — cannot be deferred |
| MEDIUM | Must resolve before shipping — does not block commitment |
| LOW | Advisory — fix if time permits |

Only HIGH, MEDIUM, LOW are valid. If a row would produce any other value, you are not
ready to stage that row. Revise until the value is one of these three.

Gate 2 passed when: the scale is written and locked here.

---

### Gate 3 — Reviewer selection

**You are not ready to run reviews until this gate is passed.**

**Standard (default)**: Select 2–4 roles whose domain intersects the artifact type.
Write one sentence per selection explaining why this role for this specific artifact.
Challenger archetype roles are always included regardless of relevance score.

**`--depth deep`**: Select all roles. No selection rationale needed.

Gate 3 passed when: the reviewer queue is non-empty and rationale is written (standard depth).

---

### Gate 4 — Lens anchor (sub-gate per reviewer)

**You are not ready to write the finding for any reviewer until this sub-gate is passed.**

Before writing the finding, quote or paraphrase one line from this role's `orientation.frame`
or `lens.verify`. Write it as:

> Lens: "[quote or paraphrase]"

You are not ready to write the finding before this line exists. A review without a lens
anchor is not a review — it is generic observation that does not reflect the role's
documented perspective.

Sub-gate passed when: the lens quote is written and the finding has been shaped by it.

---

### Running each reviewer

Process roles in order: challenger archetype roles first, then others.

For each role, pass all four sub-gates in sequence:

1. **Gate 4** (lens anchor) — write the lens before anything else
2. **Find**: Name the specific artifact surface this lens would flag — section heading,
   field name, stated assumption, diagram element. You are not ready to assign severity
   until a specific surface is named.
3. **Severity**: Apply Gate 2 contract. You are not ready to write the recommendation
   until severity is assigned with exactly one of the three valid labels.
4. **Recommendation**: One concrete action — what to do and where in the artifact.
   You are not ready to stage the row until the recommendation names a location.

For challenger roles: you are not ready to stage the row until the finding names the null
hypothesis — what the team currently does instead of this artifact, and whether that
alternative is demonstrably better, worse, or equivalent.

---

### Gate 5 — Review matrix

**You are not ready to write the synthesis until this gate is passed.**

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|

Rows appear in execution order: challenger rows first, then domain roles.

Gate 5 passed when: matrix is rendered with all rows, no blank cells.

---

### Gate 6 — Cross-role synthesis

**You are not ready to present the AMEND block until this gate is passed.**

2–3 sentences after the matrix:
- Name at least one convergence: two roles independently flagged the same concern area.
- Name any conflict: two roles assign different severity to the same surface.
- If neither: "No cross-role signal detected."

Gate 6 passed when: synthesis is written.

---

### AMEND

> **AMEND**
> - Add reviewer: `/crew-check [artifact] --amend add:[role-name]` *(inserted in archetype sequence)*
> - Full registry: `/crew-check [artifact] --depth deep`
> - Re-run single role: `/crew-check [artifact] --amend rerun:[role-name]`
> - Re-run from Gate 1: `/crew-check [artifact] --amend reload`

---

---

## V-02

**Axis**: Hard-halt execution gate
**Hypothesis**: Defining a named halt registry upfront — every gate failure has an exact
error message, triggered exactly as written — transforms the skill from a rule list into
an execution contract with visible failure modes. R1 and R2 both included "ERROR+halt if
absent" for the role-pool gate but did not extend the halt contract to per-reviewer gates
(lens anchor, severity value, recommendation location). V-02 makes C-16 comprehensive: the
halt contract covers all four cell-level constraints, not just the registry precondition. A
model that treats "do not proceed without X" as advisory will skip; a model that sees "output
HALT [G4-{role}]: Lens anchor absent" as the only valid response to a missing lens will not.
Explicit halt messages at every gate also produce a recoverable failure log via the AMEND
`--amend halts` command, which is a practical debugging affordance R1/R2 lacked.

---

You are running `/crew-check`.

Your task: pass the provided artifact through the registered org roles and produce a
multi-role review matrix. This skill operates under a hard-halt contract: when a precondition
fails, you output the designated halt message and stop that gate. No partial output. No
silent skips.

---

### Halt registry (defined once; trigger exactly as written)

| Gate | Halt message |
|------|--------------|
| G1 registry | `HALT [G1]: .craft/roles/ not found or empty. No role pool. Cannot proceed.` |
| G4 lens | `HALT [G4-{role}]: Lens anchor not written for {role}. Finding blocked until lens is quoted.` |
| G4 severity | `HALT [G4-{role}]: Severity value '{value}' is not valid. Must be HIGH, MEDIUM, or LOW. Row cannot be staged.` |
| G4 location | `HALT [G4-{role}]: Recommendation for {role} does not name a location. Row cannot be staged.` |
| G5 empty | `HALT [G5]: No valid rows staged. Review matrix cannot be rendered.` |

Any condition not listed here does not trigger a halt. Continue with best available data and
note the gap inline.

---

### Step 1 — Load the registry [Gate G1]

Read every file in `.craft/roles/`. Build the role pool from only what you find there.
Do not add roles not present in that directory.

For each role: name, archetype, `orientation.frame`, `expertise.relevance`.

If `.craft/roles/` is absent or empty: output `HALT [G1]` message exactly. Stop.

---

### Step 2 — Lock the severity contract

Before running any reviewer, lock this scale. No additions. No deviations.

| Label | Operational meaning |
|-------|---------------------|
| HIGH | Blocks commitment or ship decision |
| MEDIUM | Must resolve before shipping; does not block commitment |
| LOW | Advisory; fix if time permits |

If a reviewer row produces a value outside HIGH / MEDIUM / LOW: output
`HALT [G4-{role}]` severity message with the offending value. Revise before staging.

---

### Step 3 — Select reviewers

**Standard (default)**: Select 2–4 roles whose domain intersects the artifact type.
Write one sentence per selection explaining why this role for this artifact.
Challenger archetype roles are always included.

**`--depth deep`**: Select all roles. No rationale needed.

---

### Step 4 — Run each reviewer [Gate G4 per role]

Process roles in order: challenger archetype first, then others alphabetically.

For each role:

**a. Anchor the lens** [G4 lens gate]
Quote or paraphrase one line from this role's `orientation.frame` or `lens.verify`.
Write it as: `Lens: "[quote]"`

If this step is skipped or the quote is absent: output `HALT [G4-{role}]` lens message.
Do not proceed to the finding until the lens is written.

**b. Find**
Name the specific artifact surface this lens flags: section heading, field, stated
assumption, diagram element. Name required. If no specific surface can be named, note the
gap inline — this does not trigger a halt but does mark the finding as incomplete.

**c. Assign severity** [G4 severity gate]
Apply the contract from Step 2. If the assigned value is not HIGH, MEDIUM, or LOW:
output `HALT [G4-{role}]` severity message with the offending value. Revise, then continue.

**d. Recommend** [G4 location gate]
One concrete action: what to do and where in the artifact.
If the recommendation does not name a location: output `HALT [G4-{role}]` location
message. Revise, then continue.

For challenger roles: the finding must state whether the status-quo alternative is
demonstrably better, worse, or equivalent to what this artifact proposes. If the artifact
does not name what it replaces, that absence is the finding: HIGH severity.

---

### Step 5 — Review matrix [Gate G5]

If no valid rows are staged: output `HALT [G5]` message. Stop.

Otherwise:

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|

Rows in execution order: challenger first, then domain roles.

---

### Step 6 — Cross-role synthesis

2–3 sentences:
- Name at least one convergence or conflict across rows.
- If neither: "No cross-role signal detected."

---

### AMEND

> **AMEND**
> - Add reviewer: `/crew-check [artifact] --amend add:[role-name]`
> - Full registry: `/crew-check [artifact] --depth deep`
> - Re-run single role: `/crew-check [artifact] --amend rerun:[role-name]`
> - Show halt log: `/crew-check [artifact] --amend halts` *(lists every gate that fired this run)*

---

---

## V-03

**Axis**: Phrasing register — interrogative/diagnostic
**Hypothesis**: Structuring the skill as a series of diagnostic questions the model must
answer — rather than imperatives it must follow — produces a softer but durable form of
C-14 and C-16: each question makes the "not ready" condition explicit without using formal
halt language, and the sequence of Q1 → Q2 → Q3 → Q4 per reviewer creates a natural gate
stack. The key bet: models may engage more authentically with "What does this role actually
care about? Quote it." than with "Quote one line from orientation.frame." The imperative
names the mechanism; the question names the intent. C-11 (lens-anchoring) in particular
may benefit — a model answering "what does this role actually care about?" is more likely
to surface genuine orientation content than one executing "quote one line" as a formatting
directive. R1 V-04 used SHALL-language (formal imperative); R2 V-02 used coaching voice
(warm second-person); V-03 uses diagnostic questions (neutral analytical).

---

You are running `/crew-check`.

Your task: pass the provided artifact through the registered org roles and produce a
multi-role review matrix. This skill is structured as a diagnostic interrogation — at each
stage, you answer a set of questions before proceeding. The answers drive the output.

---

### Stage 1 — Registry diagnostic

**Answer these before doing anything else:**

1. Does `.craft/roles/` exist and contain at least one file?
   - No → Output: `ERROR: .craft/roles/ not found.` Stop here.
   - Yes → Continue.

2. What roles are present? For each file, record: name, archetype, `orientation.frame`,
   `expertise.relevance`.

3. Are there any roles in the pool that were not sourced from `.craft/roles/`?
   There must not be. The pool is exactly what the directory contains, nothing more.

**Registry answer:** [list of discovered roles with archetype]

---

### Stage 2 — Depth and selection diagnostic

**Answer these before selecting reviewers:**

1. Is `--depth deep` flagged?
   - Yes → Queue = entire role pool. No rationale needed. Skip to Stage 3.
   - No → Depth = standard. Continue.

2. (Standard) Which 2–4 roles have `expertise.relevance` or `orientation.frame` that
   intersects the artifact's subject, namespace, or type?
   Answer one sentence per candidate: *why this role for this specific artifact?*

3. Are there any roles with `archetype: challenger` in the pool?
   If yes → they are automatically in the queue regardless of relevance score.

**Selection answer:** [queue with rationale, or "all roles — deep depth"]

---

### Stage 3 — Severity contract

**Answer this before any reviewer runs:**

What do HIGH, MEDIUM, and LOW mean operationally?

- **HIGH**: the finding blocks a commitment or ship decision. It cannot be deferred.
- **MEDIUM**: the finding must be resolved before shipping, but does not block commitment.
- **LOW**: advisory — worth fixing if time permits, but doesn't hold up commitment or ship.

Are these the only valid severity values you will use in this run?

**Answer:** Yes — HIGH, MEDIUM, LOW only. Any other label is not a valid answer.

---

### Stage 4 — Per-reviewer diagnostic

Process roles in order: challenger archetype roles first, then selected domain roles.

For each role, answer these questions in order before writing the matrix row:

**Q1: What does this role actually care about?**
Quote or paraphrase one line from their `orientation.frame` or `lens.verify`.
Write it as the lens before writing anything else.

> Lens: "[quote or paraphrase from role file]"

If you cannot quote or paraphrase from the role file, you are not ready to write the finding.

**Q2: What does this artifact do or fail to do under that lens?**
Name the specific surface in the artifact where the concern lives. Which section heading,
field, assumption, or diagram element are you pointing at? If you cannot name a specific
surface, the finding is not ready — revisit Q1.

**Q3: How serious is this finding?**
Apply Stage 3 contract. Is it HIGH, MEDIUM, or LOW?
If the answer is anything else, it is not a valid answer — pick again.

**Q4: What should the author do, and exactly where in the artifact?**
Concrete action with a location. Not a directive. "Address this concern" is not an answer.
If your answer doesn't name a location, it's not specific enough yet.

For challenger archetype roles, also answer:

**Q5: What is the null hypothesis?**
What does the team currently do instead of this artifact? Is that alternative demonstrably
better, worse, or equivalent? If the artifact does not name what it replaces, that is the
finding: "Not stated — artifact cannot justify adoption costs it has not acknowledged."

---

### Stage 5 — Review matrix

Compile the diagnostic answers into the matrix:

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|

Order: challenger rows first (from Q5 findings), then domain rows.

---

### Stage 6 — Cross-role synthesis

After the matrix, answer:
- Did two or more reviewers land on the same concern independently? Name it.
- Did any reviewers disagree on severity for the same surface? Name it.
- If neither: "No cross-role signal detected."

---

### AMEND

> **AMEND**
> - Add reviewer: `/crew-check [artifact] --amend add:[role-name]`
> - Full registry: `/crew-check [artifact] --depth deep`
> - Re-run diagnostic for one role: `/crew-check [artifact] --amend rerun:[role-name]`
> - Revisit Stage 3: `/crew-check [artifact] --amend rerun:severity`

---

---

## V-04

**Axes**: Readiness-gate framing + Hard-halt execution gate
**Hypothesis**: Combining C-14 (readiness-gate framing) with C-16 (hard-halt contract)
creates a gate stack with two reinforcing properties. Readiness-gate framing changes the
internal question from "did I follow the rule?" to "am I actually ready?" — it frames
prerequisites as states the execution cannot be in, not instructions it can choose to
treat as advisory. Hard-halt makes the failure mode explicit: when a gate fails, the output
is a specific named message, not a silent skip or degraded partial run. Together they form a
contract where (1) every transition requires a named readiness condition, AND (2) failing
any condition produces a visible, recoverable error. V-01 had readiness framing but softer
failure modes; V-02 had hard halts but standard imperative transitions. V-04 tests whether
the combination is materially stronger than either alone. The severity-sorted render
(challenger rows before domain rows within each tier) is included as a natural consequence
of the sort step — C-15 compliance without making sort the primary axis.

---

You are running `/crew-check`.

Your task: pass the provided artifact through the registered org roles and produce a
severity-sorted review matrix. Two structural properties govern every transition in this run:

1. **Readiness gates**: every transition is a readiness assertion. You are not ready to
   advance past any gate until its condition is fully met. Prerequisites are gates, not
   guidelines.

2. **Hard halts**: every unmet gate produces a specific halt message and stops that gate.
   No partial output. No silent skips. Revise and re-enter.

---

### Halt registry (defined once; trigger exactly as written)

| Gate | Halt message |
|------|--------------|
| G1 registry | `HALT [G1]: .craft/roles/ not found or empty. Not ready to select reviewers.` |
| G4 lens | `HALT [G4-{role}]: Lens anchor not written. Not ready to write the finding for {role}.` |
| G4 severity | `HALT [G4-{role}]: Severity '{value}' invalid. Not ready to stage row for {role}.` |
| G4 location | `HALT [G4-{role}]: Recommendation has no location. Not ready to stage row for {role}.` |

---

### Gate 1 — Registry

**You are not ready to proceed until: role pool is built exclusively from `.craft/roles/`.**

Read every file in `.craft/roles/`. Record: name, archetype, `orientation.frame`,
`expertise.relevance`. Role pool = discovered files only. Zero invented roles.

If directory absent or empty: output `HALT [G1]` exactly. Stop.

Gate 1 passed when: pool is non-empty, every entry traced to a discovered file.

---

### Gate 2 — Severity contract

**You are not ready to run any reviewer until: severity scale is written and locked.**

| Label | Score | Operational meaning |
|-------|-------|---------------------|
| HIGH | 3 | Blocks commitment or ship decision |
| MEDIUM | 2 | Must resolve before shipping; does not block commitment |
| LOW | 1 | Advisory; fix if time permits |

Only HIGH, MEDIUM, LOW are valid labels. Score is used for sorting only; only the label
appears in the matrix. Any other label triggers `HALT [G4-{role}]` severity message.

Gate 2 passed when: scale is locked here.

---

### Gate 3 — Reviewer selection

**You are not ready to run reviews until: the reviewer queue is declared.**

**Standard (default)**: Select 2–4 roles whose domain intersects the artifact type.
Write one rationale sentence per selection.
Challenger archetype roles are always included.

**`--depth deep`**: Queue = entire pool. No rationale required.

Gate 3 passed when: queue is non-empty and rationale written (standard depth).

---

### Gate 4 — Per-reviewer execution (four sub-gates per role)

**You are not ready to stage any row until all four sub-gates for that role are passed.**

Process roles: challenger archetype first, then others alphabetically.

For each role:

**Sub-gate G4a — Lens anchor**
You are not ready to write the finding until the lens is quoted.
Write: `Lens: "[quote or paraphrase from orientation.frame or lens.verify]"`
If absent: output `HALT [G4-{role}]` lens message. Revise.

**Sub-gate G4b — Finding with named surface**
You are not ready to assign severity until a specific artifact surface is named.
Name the section, field, assumption, or diagram element the finding references.

For challenger roles: you are not ready to stage the row until the finding addresses the
null hypothesis — what the team currently does instead, and whether it is demonstrably
better, worse, or equivalent.

**Sub-gate G4c — Valid severity**
You are not ready to write the recommendation until severity is assigned.
Apply Gate 2 contract. If value is not HIGH, MEDIUM, or LOW: output `HALT [G4-{role}]`
severity message. Revise.

**Sub-gate G4d — Recommendation with location**
You are not ready to stage the row until the recommendation names what AND where.
If the recommendation lacks a location: output `HALT [G4-{role}]` location message. Revise.

Gate 4 passed for a role when: all four sub-gates are satisfied and the row is staged.

---

### Gate 5 — Review matrix

**You are not ready to write the synthesis until: matrix is rendered from staged rows.**

Sort rows by severity score descending (HIGH first, then MEDIUM, then LOW).
Within each tier: challenger rows before domain rows.

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|

Gate 5 passed when: matrix rendered with no blank cells.

---

### Gate 6 — Cross-role synthesis

**You are not ready to present the AMEND block until this gate is passed.**

2–3 sentences:
- Name at least one convergence: two or more roles independently flagged the same area.
- Name any conflict: two roles assigned different severity to the same surface.
- If neither: "No cross-role signal detected."

Gate 6 passed when: synthesis written.

---

### AMEND

> **AMEND**
> - Add reviewer: `/crew-check [artifact] --amend add:[role-name]` *(inserted in archetype sequence)*
> - Full registry: `/crew-check [artifact] --depth deep`
> - Re-run from Gate 4: `/crew-check [artifact] --amend rerun:[role-name]`
> - Re-run from Gate 1: `/crew-check [artifact] --amend reload`
> - Show halt log: `/crew-check [artifact] --amend halts`
> - Show unsorted matrix: `/crew-check [artifact] --amend unsorted`

---

---

## V-05

**Axes**: Readiness-gate framing + Hard-halt execution gate + Severity-sorted output
**Hypothesis**: Full R3 integration targeting all three new v3 criteria simultaneously.
C-14 (readiness-gate framing) is the structural idiom of every transition — every gate is
a readiness assertion, not a rule. C-16 (hard-halt) is a named halt registry triggered
exactly when any gate fails — every failure mode is visible and recoverable, not silent.
C-15 (severity-sorted output) is enforced by a dedicated sort step before render, with its
own halt condition: a matrix that cannot be sorted consistently has inconsistent severity
values, which surfaces calibration failure at render time. The three mechanisms form a
coherent contract: readiness gates ensure you are not in a state that can produce invalid
output; hard halts ensure gate failures are not absorbed silently; severity sort ensures
the final output reflects calibration, not execution order. A run that reaches the AMEND
block has by construction passed all three.

---

You are running `/crew-check`.

Your task: pass the provided artifact through the registered org roles and produce a
severity-sorted review matrix. Three structural properties govern this run:

1. **Readiness gates**: you are not ready to advance past any gate until its condition is
   fully met. Every transition is a readiness assertion.

2. **Hard halts**: every unmet gate produces a specific halt message and stops that gate.
   No partial output. No silent skips. The failure is visible and addressable.

3. **Severity-sorted output**: the matrix is sorted by severity score (HIGH first, then
   MEDIUM, then LOW) before rendering. This is a structural forcing function — a matrix
   that cannot be sorted consistently has inconsistent severity values. Sorting exposes
   calibration failures at render time, not after.

---

### Halt registry (defined once; trigger exactly as written)

| Gate | Halt message |
|------|--------------|
| G1 registry | `HALT [G1]: .craft/roles/ absent or empty. Not ready to proceed.` |
| G4 lens | `HALT [G4-{role}]: Lens anchor absent. Not ready for finding.` |
| G4 severity | `HALT [G4-{role}]: Severity '{value}' invalid. Must be HIGH (3), MEDIUM (2), or LOW (1). Not ready to stage.` |
| G4 location | `HALT [G4-{role}]: Recommendation has no location. Not ready to stage.` |
| G5 sort | `HALT [G5]: Matrix sort failed — severity values inconsistent. Resolve before rendering.` |

---

### GATE 1 — Registry

**You are not ready to select reviewers until this gate is passed.**

Read every file in `.craft/roles/`. Role pool = all discovered files. Zero invented roles.
For each: name, archetype, `orientation.frame`, `expertise.relevance`.

If `.craft/roles/` absent or empty: output `HALT [G1]`. Stop.

Gate 1 passed when: pool is non-empty, every entry traced to a discovered file.

---

### GATE 2 — Severity contract

**You are not ready to run any reviewer until this gate is passed.**

Lock this scale. The numeric score is used only for sorting; only the label appears in
matrix output.

| Label | Score | Operational meaning |
|-------|-------|---------------------|
| HIGH | 3 | Blocks commitment or ship decision |
| MEDIUM | 2 | Must resolve before shipping; does not block commitment |
| LOW | 1 | Advisory; fix if time permits |

Only HIGH (3), MEDIUM (2), LOW (1) are valid. Any other label triggers the G4 severity halt.

Gate 2 passed when: scale is locked here.

---

### GATE 3 — Reviewer selection

**You are not ready to run reviews until this gate is passed.**

**Standard (default)**: Select 2–4 roles whose domain intersects the artifact type.
Write one rationale sentence per selection.
Challenger archetype roles always included regardless of relevance score.

**`--depth deep`**: Queue = entire pool. No rationale required.

Gate 3 passed when: queue is non-empty, rationale written (standard depth).

---

### GATE 4 — Per-reviewer execution (four sub-gates per role)

**You are not ready to stage a row until all four sub-gates are passed for that role.**

Process challenger archetype roles first; then others alphabetically.

**G4a — Lens anchor** *(readiness condition: not ready for the finding)*
Write: `Lens: "[quote or paraphrase from orientation.frame or lens.verify]"`
If absent: output `HALT [G4-{role}]` lens message. Revise before continuing.

**G4b — Finding with named surface** *(readiness condition: not ready for severity)*
Name the specific artifact surface this lens flags: section, field, assumption, diagram
element. For challenger roles: state the null hypothesis — what the team currently does
instead of this artifact, and whether that alternative is demonstrably better, worse, or
equivalent.

**G4c — Valid severity** *(readiness condition: not ready for recommendation)*
Apply Gate 2 contract. Assign the label; track the score internally for sorting.
If value is outside HIGH / MEDIUM / LOW: output `HALT [G4-{role}]` severity message. Revise.

**G4d — Recommendation with location** *(readiness condition: not ready to stage)*
One concrete action: what to do AND where in the artifact.
If location is absent: output `HALT [G4-{role}]` location message. Revise.

Stage the row only when G4a through G4d are all passed.

---

### GATE 5 — Sort and render

**You are not ready to render the matrix until: all rows are staged AND the sort succeeds.**

**Sort step**: order all staged rows by severity score descending (3 → 2 → 1).
Within the same score: challenger rows before domain rows.

Can all rows be ordered consistently?
- Yes → proceed to render.
- No → output `HALT [G5]`. Identify which rows have inconsistent severity values. Resolve.
  Re-sort. You are not ready to render until the sort succeeds.

**Render**:

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|
*[rows sorted: HIGH first, then MEDIUM, then LOW; challengers before domain within each tier]*

Gate 5 passed when: matrix rendered, sorted, no blank cells.

---

### GATE 6 — Priority summary

**You are not ready to write cross-role synthesis until this gate is passed.**

One line per severity tier:

```
HIGH:   [N] finding(s) — [one-phrase summary of the blocking concern, or "none"]
MEDIUM: [N] finding(s) — [one-phrase summary, or "none"]
LOW:    [N] finding(s) — [one-phrase summary, or "none"]
```

Gate 6 passed when: summary written.

---

### Cross-role synthesis

2–3 sentences:
- Name at least one convergence: two roles independently flagged the same concern area.
- Name any conflict: two roles assigned different severity to the same surface.
- If neither: "No cross-role signal detected."

---

### AMEND

> **AMEND**
> - Add reviewer: `/crew-check [artifact] --amend add:[role-name]` *(inserted in archetype sequence)*
> - Full registry: `/crew-check [artifact] --depth deep`
> - Re-run single role: `/crew-check [artifact] --amend rerun:[role-name]`
> - Re-run from Gate 1: `/crew-check [artifact] --amend reload`
> - Show unsorted matrix: `/crew-check [artifact] --amend unsorted`
> - Show halt log: `/crew-check [artifact] --amend halts` *(lists every gate that fired this run)*

---
