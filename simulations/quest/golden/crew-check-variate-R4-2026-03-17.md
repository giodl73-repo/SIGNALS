---
skill: quest-variate
skill_target: crew-check
date: 2026-03-17
round: 4
rubric: crew-check-rubric-v4-2026-03-17.md
---

# crew-check — Variate R4

5 complete prompt body variations for the `crew-check` skill.
Single-axis first (V-01 through V-03), then two-axis combinations (V-04, V-05).

Registry context assumed: `.roles/signal/` contains `inertia-advocate.md`,
`pm.md`, `architect.md` (and whatever else the workspace adds).

Rubric v4 reminder:
- Essential (must-pass): C-01 role source, C-02 matrix structure, C-03 perspective fidelity,
  C-04 depth compliance, C-05 severity presence
- Recommended: C-06 finding specificity, C-07 recommendation actionability, C-08 severity calibration
- Aspirational (v2): C-09 cross-role synthesis, C-10 AMEND responsiveness,
  C-11 lens-anchoring step, C-12 severity calibration contract, C-13 challenger-first sequencing
- Aspirational (v3): C-14 readiness-gate framing, C-15 severity-sorted matrix output,
  C-16 hard-halt execution gate
- Aspirational (v4 additions): C-17 named halt identifier system, C-18 AMEND gate-audit sub-command

Design intent for R4: All five variations hold the R3 floor (C-11 through C-16 present in all).
R3 V-04 and V-05 both scored 106/106 — they already contained the C-17 and C-18 patterns
incidentally. R4 makes them load-bearing and intentional. Single-axis variations isolate each
new criterion; V-04 and V-05 combine with the R3 floor in structurally distinct ways.

Axes selected for R4:
- V-01: Named halt IDs as four-position bindings (C-17)
- V-02: Structured gate-audit output (C-18)
- V-03: Self-routing halt messages (C-17 variant — halt messages embed re-entry commands)
- V-04: Named halt IDs + structured gate-audit (C-17 + C-18)
- V-05: Full v4 integration (C-17 + C-18 + self-routing + priority summary + audit-as-AMEND-menu)

Axes not yet explored (covered in R1–R3): role sequence, output format variation,
lifecycle emphasis, phrasing register (coaching/interrogative/SHALL), inertia framing,
phase-gated lifecycle, severity-sorted as primary axis.

---

## V-01

**Axis**: Named halt identifier system — four-position binding
**Hypothesis**: R3 V-02 and V-04 defined halt IDs in a registry and output them verbatim in
error messages. That is two positions. V-01 R4 adds two more: (1) each gate header cites its
own halt ID in brackets, so the model encounters the ID in the structure before it encounters
it in the error, and (2) AMEND re-entry routing uses halt IDs as keys rather than role names
or stage names. The claim: when the same identifier appears in four independent positions —
registry definition, gate header, error message, AMEND routing key — it becomes a stable
handle the model cannot forget mid-run. The naming also becomes more granular: instead of
flat `G4-{role}-lens`, the sub-gate IDs encode `G4a`, `G4b`, `G4c`, `G4d` as positional
qualifiers, making the identity of the failure legible without reading the message body.

---

You are running `/crew-check`.

Your task: pass the provided artifact through the registered org roles and produce a
severity-sorted review matrix. Two structural properties govern every transition:

1. **Readiness gates**: you are not ready to advance past any gate until its condition is
   fully met. Prerequisites are gates, not guidelines.

2. **Named hard halts**: every unmet gate produces the specific halt message from the registry
   below. Halt identifiers are stable handles — they appear verbatim in (1) this registry,
   (2) each gate header, (3) every halt message, and (4) AMEND re-entry commands. No partial
   output. No silent skips.

---

### Halt registry (defined once; trigger exactly as written)

Substitutions: `{role}` = role file name (no extension); `{value}` = the invalid value received.

| Gate ID | Halt message |
|---------|--------------|
| `G1` | `HALT [G1]: .roles/ absent or empty. Not ready to select reviewers.` |
| `G4a-{role}` | `HALT [G4a-{role}]: Lens anchor absent. Not ready to write the finding for {role}.` |
| `G4b-{role}` | `HALT [G4b-{role}]: No specific artifact surface named. Not ready to assign severity for {role}.` |
| `G4c-{role}` | `HALT [G4c-{role}]: Severity '{value}' invalid. Not ready to stage row for {role}.` |
| `G4d-{role}` | `HALT [G4d-{role}]: Recommendation has no location. Not ready to stage row for {role}.` |
| `G5` | `HALT [G5]: Matrix sort failed — severity values inconsistent. Resolve before rendering.` |

---

### GATE 1 [G1] — Registry

**You are not ready to select reviewers until this gate is passed.**

Read every file in `.roles/`. Role pool = all discovered files. Zero invented roles.
For each: name, archetype, `orientation.frame`, `expertise.relevance`.

If `.roles/` absent or empty: output `HALT [G1]` exactly. Stop.

Gate 1 passed when: pool is non-empty, every entry traced to a discovered file.

---

### GATE 2 — Severity contract

**You are not ready to run any reviewer until this gate is passed.**

Lock this scale. Numeric score used only for sorting; only the label appears in matrix output.

| Label | Score | Operational meaning |
|-------|-------|---------------------|
| HIGH | 3 | Blocks commitment or ship decision |
| MEDIUM | 2 | Must resolve before shipping; does not block commitment |
| LOW | 1 | Advisory; fix if time permits |

Only HIGH (3), MEDIUM (2), LOW (1) are valid. Any other label triggers `HALT [G4c-{role}]`.

Gate 2 passed when: scale is locked here.

---

### GATE 3 — Reviewer selection

**You are not ready to run reviews until this gate is passed.**

**Standard (default)**: Select 2–4 roles whose domain intersects the artifact type.
Write one rationale sentence per selection.
Challenger archetype roles are always included regardless of relevance score.

**`--depth deep`**: Queue = entire pool. No rationale required.

Gate 3 passed when: queue is non-empty, rationale written (standard depth).

---

### GATE 4 — Per-reviewer execution [G4a through G4d per role]

**You are not ready to stage a row until all four sub-gates pass for that role.**

Process challenger archetype roles first, then others alphabetically.

For each role `{role}`:

**G4a-{role} — Lens anchor**
*(readiness condition: not ready to write the finding)*
Write: `Lens: "[quote or paraphrase from orientation.frame or lens.verify]"`
If absent: output `HALT [G4a-{role}]` exactly. Revise before continuing.

**G4b-{role} — Finding with named surface**
*(readiness condition: not ready to assign severity)*
Name the specific artifact surface this lens flags: section heading, field name, stated
assumption, diagram element. For challenger roles: state the null hypothesis — what the
team currently does instead of this artifact, and whether that alternative is demonstrably
better, worse, or equivalent. If no specific surface can be named: output `HALT [G4b-{role}]`.
Note the gap inline; this does not block the row but marks the finding as incomplete.

**G4c-{role} — Valid severity**
*(readiness condition: not ready to write the recommendation)*
Apply Gate 2 contract. Assign the label; track score internally for sorting.
If value is outside HIGH / MEDIUM / LOW: output `HALT [G4c-{role}]` with the offending value. Revise.

**G4d-{role} — Recommendation with location**
*(readiness condition: not ready to stage the row)*
One concrete action: what to do AND where in the artifact.
If location is absent: output `HALT [G4d-{role}]`. Revise.

Stage the row only when G4a through G4d are all passed.

---

### GATE 5 [G5] — Sort and render

**You are not ready to write the synthesis until: all rows staged AND sort succeeds.**

Sort all staged rows by severity score descending (3 → 2 → 1).
Within the same score: challenger rows before domain rows.

If rows cannot be consistently ordered: output `HALT [G5]`. Identify the inconsistent rows.
Resolve. Re-sort. You are not ready to render until the sort succeeds.

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|
*[rows sorted: HIGH first, then MEDIUM, then LOW; challengers before domain within each tier]*

Gate 5 passed when: matrix rendered, sorted, no blank cells.

---

### Cross-role synthesis

2–3 sentences:
- Name at least one convergence: two roles independently flagged the same concern area.
- Name any conflict: two roles assigned different severity to the same surface.
- If neither: "No cross-role signal detected."

---

### AMEND

> **AMEND**
> - Add reviewer: `/crew-check [artifact] --amend add:{role-name}` *(inserted in archetype sequence)*
> - Full registry: `/crew-check [artifact] --depth deep`
> - Re-run role from G4a: `/crew-check [artifact] --amend rerun:G4-{role-name}` *(routes to G4a for that role)*
> - Re-run from Gate 1: `/crew-check [artifact] --amend reload:G1`
> - Show halt log: `/crew-check [artifact] --amend halts`
>
> AMEND routing uses gate IDs as keys: `rerun:G4-{role}` routes to sub-gate G4a for `{role}`;
> `reload:G1` routes back to the registry gate. Any gate ID from the halt registry is a valid
> routing key.

---

---

## V-02

**Axis**: Structured gate-audit output
**Hypothesis**: In R3, `--amend halts` appeared as a parenthetical annotation: "(lists every gate
that fired this run)." The user knew the sub-command existed but not what it would show. V-02 R4
defines the exact output format of `--amend halts` and elevates it to the primary debugging
interface: after any halt, the first recovery action is to run the audit, which returns a
structured block — Gate ID, gate name, halt message triggered, and resolution step — for every
gate that fired this run. Defining the format forces the model to track gate firings throughout
execution, not just produce them on demand. The secondary bet: a structured audit with resolution
steps compresses the feedback-fix cycle to a single lookup rather than re-reading the full skill
body. This axis does not change the naming scheme (which V-01 targets) — it changes what the
names produce when queried post-run.

---

You are running `/crew-check`.

Your task: pass the provided artifact through the registered org roles and produce a
severity-sorted review matrix. Two structural properties govern this run:

1. **Readiness gates**: you are not ready to advance past any gate until its condition is
   fully met. Prerequisites are gates, not guidelines.

2. **Hard halts with gate audit**: every unmet gate produces a named halt message and stops
   that gate. After any halt, the primary recovery tool is `--amend halts` — a structured
   audit block listing every gate that fired this run, with resolution steps. No partial
   output. No silent skips.

---

### Halt registry (defined once; trigger exactly as written)

| ID | Halt message |
|----|--------------|
| `G1` | `HALT [G1]: .roles/ absent or empty. Cannot proceed.` |
| `G4-{role}-lens` | `HALT [G4-{role}-lens]: Lens anchor absent. Finding blocked for {role}.` |
| `G4-{role}-severity` | `HALT [G4-{role}-severity]: Severity '{value}' invalid. Row blocked for {role}.` |
| `G4-{role}-location` | `HALT [G4-{role}-location]: Recommendation has no location. Row blocked for {role}.` |
| `G5` | `HALT [G5]: Severity values inconsistent. Matrix sort blocked.` |

---

### GATE 1 [G1] — Registry

**You are not ready to proceed until: role pool built exclusively from `.roles/`.**

Read every file in `.roles/`. Role pool = discovered files only. Zero invented roles.
For each: name, archetype, `orientation.frame`, `expertise.relevance`.

If `.roles/` absent or empty: output `HALT [G1]` exactly. Stop.

---

### GATE 2 — Severity contract

**You are not ready to run any reviewer until: severity scale is written and locked.**

| Label | Score | Operational meaning |
|-------|-------|---------------------|
| HIGH | 3 | Blocks commitment or ship decision |
| MEDIUM | 2 | Must resolve before shipping; does not block commitment |
| LOW | 1 | Advisory; fix if time permits |

Only HIGH (3), MEDIUM (2), LOW (1) are valid. Any other label triggers `HALT [G4-{role}-severity]`.

---

### GATE 3 — Reviewer selection

**Standard (default)**: Select 2–4 roles whose domain intersects the artifact type.
One rationale sentence per selection.
Challenger archetype roles always included regardless of relevance score.

**`--depth deep`**: Queue = entire pool. No rationale required.

---

### GATE 4 — Per-reviewer execution

**You are not ready to stage a row until all four sub-steps pass for that role.**

Process challenger archetype roles first, then others alphabetically.

For each role `{role}`:

**a. Lens anchor** *(readiness condition: not ready for the finding)*
Write: `Lens: "[quote or paraphrase from orientation.frame or lens.verify]"`
If absent: output `HALT [G4-{role}-lens]`. Do not proceed to finding.

**b. Finding with named surface** *(readiness condition: not ready for severity)*
Name the specific artifact surface: section, field, assumption, diagram element.
For challenger roles: state whether the status-quo alternative is demonstrably better,
worse, or equivalent to what this artifact proposes.

**c. Valid severity** *(readiness condition: not ready for recommendation)*
Apply Gate 2 contract. If value is outside HIGH / MEDIUM / LOW: output
`HALT [G4-{role}-severity]` with the offending value. Revise.

**d. Recommendation with location** *(readiness condition: not ready to stage)*
One concrete action: what to do AND where in the artifact.
If location is absent: output `HALT [G4-{role}-location]`. Revise.

---

### GATE 5 [G5] — Sort and render

**You are not ready to write the synthesis until: all rows staged AND sort succeeds.**

Sort by severity score descending (3 → 2 → 1). Within the same score: challenger rows before
domain rows. If sort fails: output `HALT [G5]`. Resolve before rendering.

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|

Gate 5 passed when: matrix rendered, sorted, no blank cells.

---

### Cross-role synthesis

2–3 sentences: name convergence, name conflict, or "No cross-role signal detected."

---

### AMEND

> **AMEND**
> - Add reviewer: `/crew-check [artifact] --amend add:{role-name}` *(inserted in archetype sequence)*
> - Full registry: `/crew-check [artifact] --depth deep`
> - Re-run single role: `/crew-check [artifact] --amend rerun:{role-name}`
> - Re-run from Gate 1: `/crew-check [artifact] --amend reload`
> - **Gate audit**: `/crew-check [artifact] --amend halts`
>   - Focused: `/crew-check [artifact] --amend halts:{gate-id}` *(single entry)*
>
> `--amend halts` output format:
>
> ```
> HALT AUDIT — [N] gate(s) fired this run:
>
> Gate ID                | Gate name        | Message triggered                                 | Resolution step
> -----------------------|------------------|---------------------------------------------------|------------------------------
> G4-architect-lens      | Lens anchor      | HALT [G4-architect-lens]: Lens anchor absent...   | Provide lens quote; rerun role
> G4-architect-severity  | Severity value   | HALT [G4-architect-severity]: Severity 'CRITICAL' | Assign HIGH, MEDIUM, or LOW
>
> No gates fired → "No halts recorded this run."
> ```
>
> `--amend halts:{id}` returns only the entry for that gate ID, or "No match for {id}."

---

---

## V-03

**Axis**: Self-routing halt messages
**Hypothesis**: When a halt fires, the user knows what went wrong but must locate the fix: scan
the AMEND block, identify the right sub-command, and construct the invocation. V-03 eliminates
that lookup by embedding the re-entry command directly in the halt message. The halt registry
gains a third column (re-entry command), and every fired halt message ends with
`→ To continue: /crew-check [artifact] --amend [command]`. The halt IS the fix instruction.
This is a C-17 variant (halt IDs are still named and stable) but the primary design decision
is about what happens next — not just that the failure is visible, but that the failure is
immediately actionable without any secondary lookup. V-01 made IDs appear in more places;
V-03 makes the ID useful by loading the follow-on action into the message itself. The axis
produces a qualitatively different recovery experience: a model that halts has the next step
in the same output, not two reads away.

---

You are running `/crew-check`.

Your task: pass the provided artifact through the registered org roles and produce a
severity-sorted review matrix. Two structural properties govern this run:

1. **Readiness gates**: you are not ready to advance past any gate until its condition is
   fully met.

2. **Self-routing hard halts**: every unmet gate produces a named halt message that includes
   the AMEND re-entry command for that exact failure. The halt message tells you what went
   wrong AND what to type next. No partial output. No silent skips. No secondary lookup.

---

### Halt registry (defined once; trigger exactly as written)

Each entry has three parts: Gate ID, halt message, re-entry command. When a halt fires, output
all three in sequence.

| Gate ID | Halt message | Re-entry command |
|---------|--------------|-----------------|
| `G1` | `HALT [G1]: .roles/ absent or empty. Not ready to proceed.` | *(fix the directory, then)* `/crew-check [artifact] --amend reload` |
| `G4-{role}-lens` | `HALT [G4-{role}-lens]: Lens anchor absent for {role}. Not ready to write the finding.` | `/crew-check [artifact] --amend rerun:{role}` |
| `G4-{role}-severity` | `HALT [G4-{role}-severity]: Severity '{value}' invalid for {role}. Not ready to stage row.` | `/crew-check [artifact] --amend rerun:{role}` |
| `G4-{role}-location` | `HALT [G4-{role}-location]: Recommendation has no location for {role}. Not ready to stage row.` | `/crew-check [artifact] --amend rerun:{role}` |
| `G5` | `HALT [G5]: Severity values inconsistent. Matrix sort blocked.` | `/crew-check [artifact] --amend reload` |

When a halt fires, output the halt message followed by: `→ To continue: [re-entry command]`

---

### GATE 1 [G1] — Registry

**You are not ready to select reviewers until this gate is passed.**

Read every file in `.roles/`. Role pool = all discovered files. Zero invented roles.
For each: name, archetype, `orientation.frame`, `expertise.relevance`.

If `.roles/` absent or empty: output `HALT [G1]` with its re-entry command. Stop.

---

### GATE 2 — Severity contract

**You are not ready to run any reviewer until this gate is passed.**

Lock this scale. Score used only for sorting; only the label appears in matrix output.

| Label | Score | Operational meaning |
|-------|-------|---------------------|
| HIGH | 3 | Blocks commitment or ship decision |
| MEDIUM | 2 | Must resolve before shipping; does not block commitment |
| LOW | 1 | Advisory; fix if time permits |

Only HIGH (3), MEDIUM (2), LOW (1) are valid. Any other label triggers `HALT [G4-{role}-severity]`
with its re-entry command.

---

### GATE 3 — Reviewer selection

**Standard (default)**: Select 2–4 roles whose domain intersects the artifact type.
One rationale sentence per selection.
Challenger archetype roles always included.

**`--depth deep`**: Queue = entire pool. No rationale required.

---

### GATE 4 — Per-reviewer execution

**You are not ready to stage a row until all four sub-steps pass.**

Process challenger archetype roles first, then others alphabetically.

For each role `{role}`:

**a. Lens anchor** *(readiness condition: not ready for the finding)*
Write: `Lens: "[quote or paraphrase from orientation.frame or lens.verify]"`
If absent: output `HALT [G4-{role}-lens]` with its re-entry command. Do not proceed.

**b. Finding with named surface** *(readiness condition: not ready for severity)*
Name the specific artifact surface: section, field, assumption, diagram element.
For challenger roles: state whether the status-quo alternative is demonstrably better,
worse, or equivalent to what this artifact proposes.

**c. Valid severity** *(readiness condition: not ready for recommendation)*
Apply Gate 2 contract. If value outside HIGH / MEDIUM / LOW: output
`HALT [G4-{role}-severity]` with its re-entry command. Revise.

**d. Recommendation with location** *(readiness condition: not ready to stage)*
One concrete action: what to do AND where.
If location absent: output `HALT [G4-{role}-location]` with its re-entry command. Revise.

---

### GATE 5 [G5] — Sort and render

**You are not ready to write the synthesis until: all rows staged AND sort succeeds.**

Sort by severity score descending. Within same score: challenger rows before domain rows.
If sort fails: output `HALT [G5]` with its re-entry command. Resolve. Re-sort.

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|

Gate 5 passed when: matrix rendered, sorted, no blank cells.

---

### Cross-role synthesis

2–3 sentences: name convergence, name conflict, or "No cross-role signal detected."

---

### AMEND

> **AMEND**
> - Add reviewer: `/crew-check [artifact] --amend add:{role-name}`
> - Full registry: `/crew-check [artifact] --depth deep`
> - Re-run single role: `/crew-check [artifact] --amend rerun:{role-name}`
> - Re-run from Gate 1: `/crew-check [artifact] --amend reload`
> - Show halt log: `/crew-check [artifact] --amend halts` *(lists every gate ID that fired this run)*
>
> Note: every halt message already contains its re-entry command. The AMEND block is provided
> for proactive navigation; the halt message is the primary recovery instruction.

---

---

## V-04

**Axes**: Named halt identifier system + Structured gate-audit output
**Hypothesis**: C-17 and C-18 are structurally coupled — named IDs (C-17) are what make the
gate-audit (C-18) meaningful. V-04 combines both explicitly: halt IDs appear in four positions
throughout execution (C-17), and `--amend halts` produces a structured audit block that
references those same IDs (C-18). The coupling is the point: a model that encounters `G4a-{role}`
in the gate header, outputs it verbatim in the halt message, then sees it listed by name in the
audit block has three independent evidence trails for the same failure. The audit is not just a
log — it is a cross-reference into the named halt system. V-02 defined the audit format without
emphasizing the naming system; V-01 defined the naming system without the structured audit.
V-04 is the combination where each reinforces the other.

---

You are running `/crew-check`.

Your task: pass the provided artifact through the registered org roles and produce a
severity-sorted review matrix. Two structural properties govern every transition:

1. **Readiness gates**: you are not ready to advance past any gate until its condition is
   fully met. Prerequisites are gates, not guidelines.

2. **Named hard halts with gate audit**: every unmet gate produces the specific halt message
   from the registry below. Halt identifiers are stable — they appear verbatim in (1) this
   registry, (2) each gate header, (3) every halt message, and (4) AMEND routing keys.
   After any halt, `--amend halts` returns a structured audit block cross-referencing those
   same IDs. No partial output. No silent skips.

---

### Halt registry (defined once; trigger exactly as written)

Substitutions: `{role}` = role file name; `{value}` = the invalid value received.

| Gate ID | Halt message |
|---------|--------------|
| `G1` | `HALT [G1]: .roles/ absent or empty. Not ready to select reviewers.` |
| `G4a-{role}` | `HALT [G4a-{role}]: Lens anchor absent. Not ready to write the finding for {role}.` |
| `G4b-{role}` | `HALT [G4b-{role}]: No specific artifact surface named. Not ready to assign severity for {role}.` |
| `G4c-{role}` | `HALT [G4c-{role}]: Severity '{value}' invalid. Not ready to stage row for {role}.` |
| `G4d-{role}` | `HALT [G4d-{role}]: Recommendation has no location. Not ready to stage row for {role}.` |
| `G5` | `HALT [G5]: Matrix sort failed — severity values inconsistent. Resolve before rendering.` |

---

### GATE 1 [G1] — Registry

**You are not ready to select reviewers until this gate is passed.**

Read every file in `.roles/`. Role pool = all discovered files. Zero invented roles.
For each: name, archetype, `orientation.frame`, `expertise.relevance`.

If `.roles/` absent or empty: output `HALT [G1]` exactly. Stop.

Gate 1 passed when: pool is non-empty, every entry traced to a discovered file.

---

### GATE 2 — Severity contract

**You are not ready to run any reviewer until this gate is passed.**

Lock this scale. Numeric score used only for sorting; only the label appears in matrix output.

| Label | Score | Operational meaning |
|-------|-------|---------------------|
| HIGH | 3 | Blocks commitment or ship decision |
| MEDIUM | 2 | Must resolve before shipping; does not block commitment |
| LOW | 1 | Advisory; fix if time permits |

Only HIGH (3), MEDIUM (2), LOW (1) are valid. Any other label triggers `HALT [G4c-{role}]`.

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

### GATE 4 — Per-reviewer execution [G4a through G4d per role]

**You are not ready to stage a row until all four sub-gates pass for that role.**

Process challenger archetype roles first, then others alphabetically.

For each role `{role}`:

**G4a-{role} — Lens anchor**
*(readiness condition: not ready to write the finding)*
Write: `Lens: "[quote or paraphrase from orientation.frame or lens.verify]"`
If absent: output `HALT [G4a-{role}]` exactly. Revise before continuing.

**G4b-{role} — Finding with named surface**
*(readiness condition: not ready to assign severity)*
Name the specific artifact surface: section heading, field name, stated assumption, diagram
element. For challenger roles: state the null hypothesis — what the team currently does instead
of this artifact, and whether that alternative is demonstrably better, worse, or equivalent.
If no surface can be named: output `HALT [G4b-{role}]`. Note the gap inline; continue.

**G4c-{role} — Valid severity**
*(readiness condition: not ready to write the recommendation)*
Apply Gate 2 contract. Assign the label; track score internally.
If value outside HIGH / MEDIUM / LOW: output `HALT [G4c-{role}]` with the offending value. Revise.

**G4d-{role} — Recommendation with location**
*(readiness condition: not ready to stage the row)*
One concrete action: what to do AND where in the artifact.
If location absent: output `HALT [G4d-{role}]`. Revise.

Stage the row only when G4a through G4d all pass.

---

### GATE 5 [G5] — Sort and render

**You are not ready to write the synthesis until: all rows staged AND sort succeeds.**

Sort all staged rows by severity score descending (3 → 2 → 1).
Within the same score: challenger rows before domain rows.

If rows cannot be consistently ordered: output `HALT [G5]`. Identify inconsistent rows.
Resolve. Re-sort. You are not ready to render until the sort succeeds.

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|
*[rows sorted: HIGH first, then MEDIUM, then LOW; challengers before domain within each tier]*

Gate 5 passed when: matrix rendered, sorted, no blank cells.

---

### Gate 6 — Cross-role synthesis

**You are not ready to present the AMEND block until this gate is passed.**

2–3 sentences:
- Name at least one convergence: two roles independently flagged the same concern area.
- Name any conflict: two roles assigned different severity to the same surface.
- If neither: "No cross-role signal detected."

Gate 6 passed when: synthesis written.

---

### AMEND

> **AMEND**
> - Add reviewer: `/crew-check [artifact] --amend add:{role-name}` *(inserted in archetype sequence)*
> - Full registry: `/crew-check [artifact] --depth deep`
> - Re-run role from G4a: `/crew-check [artifact] --amend rerun:G4-{role-name}` *(routes to G4a for that role)*
> - Re-run from Gate 1: `/crew-check [artifact] --amend reload:G1`
> - **Gate audit**: `/crew-check [artifact] --amend halts`
>   - Focused: `/crew-check [artifact] --amend halts:{gate-id}`
>
> `--amend halts` output format:
>
> ```
> HALT AUDIT — [N] gate(s) fired this run:
>
> Gate ID       | Gate name        | Message triggered                            | Resolution step
> --------------|------------------|----------------------------------------------|----------------------------------
> G4a-pm        | Lens anchor      | HALT [G4a-pm]: Lens anchor absent...         | Provide lens quote; --amend rerun:G4-pm
> G4c-pm        | Severity value   | HALT [G4c-pm]: Severity 'CRITICAL' invalid   | Assign HIGH, MEDIUM, or LOW
>
> No gates fired → "No halts recorded this run."
> ```

---

---

## V-05

**Axes**: Named halt IDs + Structured gate-audit + Self-routing halt messages + Priority summary
+ Audit-as-AMEND-menu
**Hypothesis**: Full v4 integration. Each mechanism strengthens the others: named halt IDs
(C-17) make the audit (C-18) a cross-reference, not just a log. Self-routing halt messages
(V-03 pattern) compress the feedback-fix cycle. The priority summary tier (R3 V-05 pattern)
makes the triage state explicit before synthesis. Audit-as-AMEND-menu closes the loop: the
audit block includes ready-to-paste re-entry commands per fired gate, making the recovery path
a single copy-paste rather than a manual lookup. A run that reaches the AMEND block has passed
all gates. A run that fires any halt leaves the user holding a structured action list, not a
diagnostic puzzle.

---

You are running `/crew-check`.

Your task: pass the provided artifact through the registered org roles and produce a
severity-sorted review matrix. Four structural properties govern this run:

1. **Readiness gates**: you are not ready to advance past any gate until its condition is fully
   met. Every transition is a readiness assertion.

2. **Named hard halts**: every unmet gate produces the specific halt message from the registry.
   Halt IDs are stable handles — they appear verbatim in registry, gate headers, error messages,
   AMEND routing, and audit output. No partial output. No silent skips.

3. **Self-routing halts**: every halt message ends with its re-entry command. The halt tells you
   what went wrong AND what to type next. No secondary lookup required.

4. **Severity-sorted output**: the matrix is sorted by severity score before rendering. A matrix
   that cannot be consistently sorted has inconsistent severity values — the sort exposes
   calibration failures at render time.

---

### Halt registry (defined once; trigger exactly as written)

Each entry: Gate ID, halt message, re-entry command.
Substitutions: `{role}` = role file name; `{value}` = the invalid value received.

| Gate ID | Halt message | Re-entry command |
|---------|--------------|-----------------|
| `G1` | `HALT [G1]: .roles/ absent or empty. Not ready to select reviewers.` | *(fix directory)* `--amend reload` |
| `G4a-{role}` | `HALT [G4a-{role}]: Lens anchor absent. Not ready for finding for {role}.` | `--amend rerun:G4-{role}` |
| `G4b-{role}` | `HALT [G4b-{role}]: No surface named. Not ready for severity for {role}.` | `--amend rerun:G4-{role}` |
| `G4c-{role}` | `HALT [G4c-{role}]: Severity '{value}' invalid. Not ready to stage {role}.` | `--amend rerun:G4-{role}` |
| `G4d-{role}` | `HALT [G4d-{role}]: No location in recommendation. Not ready to stage {role}.` | `--amend rerun:G4-{role}` |
| `G5` | `HALT [G5]: Matrix sort failed — severity values inconsistent. Resolve before rendering.` | `--amend reload` |

When a halt fires: output the halt message, then: `→ To continue: /crew-check [artifact] [re-entry command]`

---

### GATE 1 [G1] — Registry

**You are not ready to select reviewers until this gate is passed.**

Read every file in `.roles/`. Role pool = all discovered files. Zero invented roles.
For each: name, archetype, `orientation.frame`, `expertise.relevance`.

If absent or empty: output `HALT [G1]` with re-entry command. Stop.

Gate 1 passed when: pool is non-empty, every entry traced to a discovered file.

---

### GATE 2 — Severity contract

**You are not ready to run any reviewer until this gate is passed.**

Lock this scale. Numeric score used only for sorting; only the label appears in matrix output.

| Label | Score | Operational meaning |
|-------|-------|---------------------|
| HIGH | 3 | Blocks commitment or ship decision |
| MEDIUM | 2 | Must resolve before shipping; does not block commitment |
| LOW | 1 | Advisory; fix if time permits |

Only HIGH (3), MEDIUM (2), LOW (1) are valid. Any other label triggers `HALT [G4c-{role}]`.

Gate 2 passed when: scale is locked here.

---

### GATE 3 — Reviewer selection

**You are not ready to run reviews until this gate is passed.**

**Standard (default)**: Select 2–4 roles whose domain intersects the artifact type.
One rationale sentence per selection.
Challenger archetype roles always included regardless of relevance score.

**`--depth deep`**: Queue = entire pool. No rationale required.

Gate 3 passed when: queue is non-empty, rationale written (standard depth).

---

### GATE 4 — Per-reviewer execution [G4a through G4d per role]

**You are not ready to stage a row until all four sub-gates pass for that role.**

Process challenger archetype roles first, then others alphabetically.

For each role `{role}`:

**G4a-{role} — Lens anchor** *(readiness condition: not ready for the finding)*
Write: `Lens: "[quote or paraphrase from orientation.frame or lens.verify]"`
If absent: output `HALT [G4a-{role}]` with re-entry command. Do not proceed.

**G4b-{role} — Finding with named surface** *(readiness condition: not ready for severity)*
Name the specific artifact surface: section, field, assumption, diagram element.
For challenger roles: state the null hypothesis — what the team currently does instead,
and whether it is demonstrably better, worse, or equivalent.
If no surface can be named: output `HALT [G4b-{role}]` with re-entry command. Note gap inline.

**G4c-{role} — Valid severity** *(readiness condition: not ready for recommendation)*
Apply Gate 2 contract. Assign label; track score internally.
If value outside HIGH / MEDIUM / LOW: output `HALT [G4c-{role}]` with re-entry command. Revise.

**G4d-{role} — Recommendation with location** *(readiness condition: not ready to stage)*
One concrete action: what to do AND where.
If location absent: output `HALT [G4d-{role}]` with re-entry command. Revise.

Stage the row only when G4a through G4d all pass.

---

### GATE 5 [G5] — Sort and render

**You are not ready to write the priority summary until: all rows staged AND sort succeeds.**

Sort all staged rows by severity score descending (3 → 2 → 1).
Within the same score: challenger rows before domain rows.

If rows cannot be consistently ordered: output `HALT [G5]` with re-entry command. Resolve.

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|
*[rows sorted: HIGH first, then MEDIUM, then LOW; challengers before domain within each tier]*

Gate 5 passed when: matrix rendered, sorted, no blank cells.

---

### GATE 6 — Priority summary

**You are not ready to write the cross-role synthesis until this gate is passed.**

```
HIGH:   [N] finding(s) — [one-phrase summary of blocking concern, or "none"]
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
> - Add reviewer: `/crew-check [artifact] --amend add:{role-name}` *(inserted in archetype sequence)*
> - Full registry: `/crew-check [artifact] --depth deep`
> - Re-run role from G4a: `/crew-check [artifact] --amend rerun:G4-{role-name}`
> - Re-run from Gate 1: `/crew-check [artifact] --amend reload`
> - Show unsorted matrix: `/crew-check [artifact] --amend unsorted`
> - **Gate audit**: `/crew-check [artifact] --amend halts`
>
> `--amend halts` output format — each fired gate entry includes a ready-to-paste re-entry command:
>
> ```
> HALT AUDIT — [N] gate(s) fired this run:
>
> Gate ID    | Gate name     | Message triggered                            | Re-entry command
> -----------|---------------|----------------------------------------------|-------------------------------------
> G4a-pm     | Lens anchor   | HALT [G4a-pm]: Lens anchor absent...         | /crew-check [artifact] --amend rerun:G4-pm
> G4c-pm     | Severity      | HALT [G4c-pm]: Severity 'CRITICAL' invalid   | /crew-check [artifact] --amend rerun:G4-pm
>
> No gates fired → "No halts recorded this run."
> ```
>
> The audit block IS the action list. Each entry is a complete re-entry instruction.
> Note: every halt message already contains its re-entry command inline.
> `--amend halts` aggregates all fired gates for multi-failure runs.
