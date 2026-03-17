---
skill: quest-variate
skill_target: crew-check
date: 2026-03-17
round: 5
rubric: crew-check-rubric-v5-2026-03-17.md
---

# crew-check — Variate R5

5 complete prompt body variations for the `crew-check` skill.
Single-axis first (V-01 through V-03), then two-axis combinations (V-04, V-05).

Registry context assumed: `.craft/roles/signal/` contains `inertia-advocate.md`,
`pm.md`, `architect.md` (and whatever else the workspace adds).

Rubric v5 reminder:
- Essential (must-pass): C-01 role source, C-02 matrix structure, C-03 perspective fidelity,
  C-04 depth compliance, C-05 severity presence
- Recommended: C-06 finding specificity, C-07 recommendation actionability, C-08 severity calibration
- Aspirational (v2): C-09 cross-role synthesis, C-10 AMEND responsiveness,
  C-11 lens-anchoring step, C-12 severity calibration contract, C-13 challenger-first sequencing
- Aspirational (v3): C-14 readiness-gate framing, C-15 severity-sorted matrix output,
  C-16 hard-halt execution gate
- Aspirational (v4): C-17 named halt identifier system, C-18 AMEND gate-audit sub-command
- Aspirational (v5 additions): C-19 self-routing halt messages, C-20 executable audit output

Design intent for R5: All five variations hold the R4 floor (C-11 through C-18 present in all).
R4 V-03 and V-05 both contained C-19 incidentally; R4 V-02 and V-05 contained C-20 incidentally.
R5 makes both load-bearing and intentional. Single-axis variations isolate each new criterion
in a structurally distinct form from R4. V-04 and V-05 combine with the R4 floor in ways
that create new structural properties.

Axes selected for R5:
- V-01: Self-routing halts with sub-gate precision (C-19 depth — routes to specific sub-gate, not just role)
- V-02: Audit-as-numbered-action-queue (C-20 depth — ordered list format, not table, top-to-bottom execution)
- V-03: Two-tier halt classification — BLOCKING vs SCOPED (new axis; C-19 and C-20 earned incidentally)
- V-04: Cross-referenced halt + audit (C-19 + C-20 tight coupling — halt message cites audit entry, audit entry carries command)
- V-05: Recovery-first flow (all four C-17+C-18+C-19+C-20, plus recovery block surfaces before AMEND on failed runs)

Axes explored in R4 that R5 builds on: C-17 named halt IDs, C-18 structured gate-audit output,
C-19 self-routing halts (pioneered in R4 V-03), C-20 executable audit (pioneered in R4 V-02 and V-05).

---

## V-01

**Axis**: Self-routing halts with sub-gate precision
**Hypothesis**: R4 V-03 embedded a re-entry command in every halt message, but routed at role
granularity: `--amend rerun:{role}` reruns the entire role from sub-gate G4a regardless of
which sub-gate actually failed. If G4c (severity) failed but G4a and G4b passed, the user
reruns two steps that already worked. V-01 routes at sub-gate granularity: a G4c failure
embeds `--amend rerun:G4c-{role}`, resuming from the severity sub-gate rather than from the
lens anchor. The halt message is not just self-routing — it is precisely routed. The bet: sub-gate
precision reduces re-execution waste on multi-reviewer runs where early sub-gates reliably
pass and only later ones fail (severity calibration is the most common late-gate failure).
This is C-19 deepened: the halt message still tells you what to type next, but it now tells
you the minimum re-entry point rather than the conservative full-role restart.

---

You are running `/crew-check`.

Your task: pass the provided artifact through the registered org roles and produce a
severity-sorted review matrix. Two structural properties govern this run:

1. **Readiness gates**: you are not ready to advance past any gate until its condition is
   fully met. Every transition is a readiness assertion.

2. **Precisely-routed hard halts**: every unmet gate produces the named halt message from
   the registry and embeds the minimum re-entry command. The re-entry command routes to the
   specific sub-gate that failed — not the entire role, not the entire run. No partial output.
   No silent skips. No over-restarting.

---

### Halt registry (defined once; trigger exactly as written)

Each halt message ends with: `→ To continue: /crew-check [artifact] [re-entry command]`
Re-entry routes to the minimum restart point.

Substitutions: `{role}` = role file name (no extension); `{value}` = the invalid value received.

| Gate ID | Halt message | Re-entry command |
|---------|--------------|-----------------|
| `G1` | `HALT [G1]: .craft/roles/ absent or empty. Not ready to select reviewers.` | `--amend reload` |
| `G4a-{role}` | `HALT [G4a-{role}]: Lens anchor absent. Not ready for the finding for {role}.` | `--amend rerun:G4a-{role}` |
| `G4b-{role}` | `HALT [G4b-{role}]: No artifact surface named. Not ready for severity for {role}.` | `--amend rerun:G4b-{role}` |
| `G4c-{role}` | `HALT [G4c-{role}]: Severity '{value}' invalid. Not ready to stage {role}.` | `--amend rerun:G4c-{role}` |
| `G4d-{role}` | `HALT [G4d-{role}]: Recommendation has no location. Not ready to stage {role}.` | `--amend rerun:G4d-{role}` |
| `G5` | `HALT [G5]: Matrix sort failed — severity values inconsistent. Resolve before rendering.` | `--amend reload` |

When a halt fires: output the halt message, then on the next line: `→ To continue: /crew-check [artifact] [re-entry command]`

---

### GATE 1 [G1] — Registry

**You are not ready to select reviewers until this gate is passed.**

Read every file in `.craft/roles/`. Role pool = all discovered files. Zero invented roles.
For each: name, archetype, `orientation.frame`, `expertise.relevance`.

If `.craft/roles/` absent or empty: output `HALT [G1]` with its re-entry command. Stop.

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

Only HIGH (3), MEDIUM (2), LOW (1) are valid. Any other label triggers `HALT [G4c-{role}]`
with its re-entry command.

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

**G4a-{role} — Lens anchor** *(readiness condition: not ready for the finding)*
Write: `Lens: "[quote or paraphrase from orientation.frame or lens.verify]"`
If absent: output `HALT [G4a-{role}]` with its re-entry command.
Re-entry routes here: `--amend rerun:G4a-{role}` resumes from this step.

**G4b-{role} — Finding with named surface** *(readiness condition: not ready for severity)*
Name the specific artifact surface: section, field, assumption, diagram element.
For challenger roles: state whether the status-quo alternative is demonstrably better,
worse, or equivalent.
If no surface can be named: output `HALT [G4b-{role}]` with its re-entry command.
Re-entry routes here: `--amend rerun:G4b-{role}` resumes from this step, skipping G4a.

**G4c-{role} — Valid severity** *(readiness condition: not ready for recommendation)*
Apply Gate 2 contract. Assign label; track score internally for sorting.
If value outside HIGH / MEDIUM / LOW: output `HALT [G4c-{role}]` with its re-entry command.
Re-entry routes here: `--amend rerun:G4c-{role}` resumes from this step, skipping G4a–G4b.

**G4d-{role} — Recommendation with location** *(readiness condition: not ready to stage)*
One concrete action: what to do AND where in the artifact.
If location absent: output `HALT [G4d-{role}]` with its re-entry command.
Re-entry routes here: `--amend rerun:G4d-{role}` resumes from this step, skipping G4a–G4c.

Stage the row only when G4a through G4d all pass.

---

### GATE 5 [G5] — Sort and render

**You are not ready to write the synthesis until: all rows staged AND sort succeeds.**

Sort all staged rows by severity score descending (3 → 2 → 1).
Within the same score: challenger rows before domain rows.

If rows cannot be consistently ordered: output `HALT [G5]` with its re-entry command. Resolve.

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
> - Rerun from specific sub-gate: `/crew-check [artifact] --amend rerun:G4{a|b|c|d}-{role-name}`
> - Rerun role from G4a: `/crew-check [artifact] --amend rerun:G4a-{role-name}` *(conservative full-role restart)*
> - Rerun from Gate 1: `/crew-check [artifact] --amend reload`
> - Gate audit: `/crew-check [artifact] --amend halts`
>   - Focused: `/crew-check [artifact] --amend halts:{gate-id}`
>
> `--amend halts` output format:
>
> ```
> HALT AUDIT — [N] gate(s) fired this run:
>
> Gate ID       | Gate name        | Message triggered                          | Re-entry command
> --------------|------------------|--------------------------------------------|------------------------------------------
> G4c-pm        | Severity value   | HALT [G4c-pm]: Severity 'CRITICAL'...      | --amend rerun:G4c-pm
> G4d-architect | Recommendation   | HALT [G4d-architect]: No location...       | --amend rerun:G4d-architect
>
> No gates fired → "No halts recorded this run."
> ```
>
> Note: every halt message already contains its precise re-entry command.
> `--amend halts` aggregates all fired gates for multi-failure runs.

---

---

## V-02

**Axis**: Audit-as-numbered-action-queue
**Hypothesis**: R4 V-02 defined the audit output as a four-column table: gate ID, gate name,
message triggered, resolution step. A table is readable but not executable — the user must
parse the table, identify the resolution step, then construct the re-entry command manually.
V-02 replaces the table with a numbered sequential list: `N. [GATE-ID] [what failed] → [paste
command]`. The list is sorted by gate execution order so the user can work top-to-bottom without
prioritization judgment. Each entry is a complete action: the number is execution sequence, the
gate ID is the handle, the description is human-readable context, the paste command is the
literal invocation. The bet: a numbered action queue is a different cognitive artifact than a
reference table — it is a task list you execute, not a table you read. C-20 is not just "the
audit entry contains a command" (which V-04 in R4 achieved); it is "the audit is an ordered
procedure." C-19 is still earned: every halt message still embeds its re-entry command inline.

---

You are running `/crew-check`.

Your task: pass the provided artifact through the registered org roles and produce a
severity-sorted review matrix. Two structural properties govern this run:

1. **Readiness gates**: you are not ready to advance past any gate until its condition is
   fully met.

2. **Hard halts with ordered action audit**: every unmet gate produces a named halt message
   with its embedded re-entry command. After any halt, `--amend halts` returns a numbered
   action queue — a sequential list of paste-ready commands for every gate that fired this run,
   ordered by gate execution order. No partial output. No silent skips. No puzzle-solving.

---

### Halt registry (defined once; trigger exactly as written)

Each halt fires with its embedded re-entry command on the next line.

Substitutions: `{role}` = role file name (no extension); `{value}` = the invalid value received.

| Gate ID | Halt message | Re-entry command |
|---------|--------------|-----------------|
| `G1` | `HALT [G1]: .craft/roles/ absent or empty. Not ready to proceed.` | `--amend reload` |
| `G4a-{role}` | `HALT [G4a-{role}]: Lens anchor absent. Not ready for finding for {role}.` | `--amend rerun:{role}` |
| `G4b-{role}` | `HALT [G4b-{role}]: No surface named. Not ready for severity for {role}.` | `--amend rerun:{role}` |
| `G4c-{role}` | `HALT [G4c-{role}]: Severity '{value}' invalid. Not ready to stage {role}.` | `--amend rerun:{role}` |
| `G4d-{role}` | `HALT [G4d-{role}]: No location in recommendation. Not ready to stage {role}.` | `--amend rerun:{role}` |
| `G5` | `HALT [G5]: Severity values inconsistent. Matrix sort blocked.` | `--amend reload` |

When a halt fires: output halt message, then: `→ To continue: /crew-check [artifact] [re-entry command]`

---

### GATE 1 [G1] — Registry

**You are not ready to select reviewers until this gate is passed.**

Read every file in `.craft/roles/`. Role pool = all discovered files. Zero invented roles.
For each: name, archetype, `orientation.frame`, `expertise.relevance`.

If `.craft/roles/` absent or empty: output `HALT [G1]` with its re-entry command. Stop.

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

Only HIGH (3), MEDIUM (2), LOW (1) are valid.

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
If absent: output `HALT [G4a-{role}]` with its re-entry command. Do not proceed.

**G4b-{role} — Finding with named surface** *(readiness condition: not ready for severity)*
Name the specific artifact surface: section, field, assumption, diagram element.
For challenger roles: state whether the status-quo alternative is demonstrably better,
worse, or equivalent.
If no surface can be named: output `HALT [G4b-{role}]` with its re-entry command.

**G4c-{role} — Valid severity** *(readiness condition: not ready for recommendation)*
Apply Gate 2 contract. If value outside HIGH / MEDIUM / LOW: output `HALT [G4c-{role}]`
with its re-entry command. Revise.

**G4d-{role} — Recommendation with location** *(readiness condition: not ready to stage)*
One concrete action: what to do AND where.
If location absent: output `HALT [G4d-{role}]` with its re-entry command. Revise.

Stage the row only when G4a through G4d all pass.

---

### GATE 5 [G5] — Sort and render

**You are not ready to write the synthesis until: all rows staged AND sort succeeds.**

Sort all staged rows by severity score descending (3 → 2 → 1).
Within the same score: challenger rows before domain rows.

If rows cannot be consistently ordered: output `HALT [G5]` with its re-entry command.

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|
*[rows sorted: HIGH first, then MEDIUM, then LOW; challengers before domain within each tier]*

Gate 5 passed when: matrix rendered, sorted, no blank cells.

---

### GATE 6 — Priority summary

**You are not ready to write the cross-role synthesis until this gate is passed.**

```
HIGH:   [N] finding(s) — [one-phrase summary, or "none"]
MEDIUM: [N] finding(s) — [one-phrase summary, or "none"]
LOW:    [N] finding(s) — [one-phrase summary, or "none"]
```

Gate 6 passed when: summary written.

---

### Cross-role synthesis

2–3 sentences: name convergence, name conflict, or "No cross-role signal detected."

---

### AMEND

> **AMEND**
> - Add reviewer: `/crew-check [artifact] --amend add:{role-name}` *(inserted in archetype sequence)*
> - Full registry: `/crew-check [artifact] --depth deep`
> - Re-run role from G4a: `/crew-check [artifact] --amend rerun:{role-name}`
> - Re-run from Gate 1: `/crew-check [artifact] --amend reload`
> - **Action queue**: `/crew-check [artifact] --amend halts`
>   - Focused: `/crew-check [artifact] --amend halts:{gate-id}`
>
> `--amend halts` output — numbered action queue, gate execution order, paste-ready:
>
> ```
> ACTION QUEUE — [N] gate(s) fired this run (execute top to bottom):
>
> 1. [G4a-pm] Lens anchor missing
>    → /crew-check [artifact] --amend rerun:pm
>
> 2. [G4c-architect] Severity 'CRITICAL' invalid
>    → /crew-check [artifact] --amend rerun:architect
>
> All actions complete → re-run: /crew-check [artifact]
> No gates fired → "No halts recorded this run."
> ```
>
> Each entry: number (execution order) · gate ID (handle) · human-readable description ·
> paste command on the next line. Execute 1 → 2 → ... → re-run.
> `--amend halts:{gate-id}` returns only that entry.

---

---

## V-03

**Axis**: Two-tier halt classification — BLOCKING vs SCOPED
**Hypothesis**: Not all halts are equally disruptive. G1 and G5 failures block the entire run —
there is nothing to show. G4 sub-gate failures block one row — other rows may still be valid.
Treating both as identical halts conflates two different recovery situations: a G1 failure
requires fixing the directory and restarting; a G4c failure for one role requires fixing one
cell and continuing. V-03 classifies halts into two tiers: BLOCKING (run-level, must fix before
any output) and SCOPED (row-level, halt is localized, other rows proceed). BLOCKING halts get
a prominent full-stop output with restart command; SCOPED halts get inline annotation and a
row-targeted re-entry command. The bet: matching halt presentation to halt scope reduces
recovery work — a user hitting a SCOPED halt should not feel like they need to restart the
entire run. C-19 is earned incidentally (every halt includes its re-entry command); C-20 is
earned incidentally (audit separates BLOCKING from SCOPED, each entry includes a re-entry command).

---

You are running `/crew-check`.

Your task: pass the provided artifact through the registered org roles and produce a
severity-sorted review matrix. Two structural properties govern this run:

1. **Readiness gates**: you are not ready to advance past any gate until its condition is met.

2. **Tier-classified hard halts**: every gate failure produces a named halt message with
   an embedded re-entry command. Halt tier determines scope:
   - **BLOCKING**: run-level failure. No output produced. Full restart required.
   - **SCOPED**: row-level failure. That row is skipped; other rows continue. Targeted re-entry.

---

### Halt registry (defined once; trigger exactly as written)

Substitutions: `{role}` = role file name (no extension); `{value}` = the invalid value received.

**BLOCKING halts** (run-level — no output until resolved):

| Gate ID | Halt message | Re-entry command |
|---------|--------------|-----------------|
| `G1` | `HALT [G1] BLOCKING: .craft/roles/ absent or empty. Not ready to select reviewers.` | `--amend reload` *(after fixing directory)* |
| `G5` | `HALT [G5] BLOCKING: Severity values inconsistent. Not ready to render matrix.` | `--amend reload` *(after resolving severity)* |

**SCOPED halts** (row-level — row is skipped; other rows proceed):

| Gate ID | Halt message | Re-entry command |
|---------|--------------|-----------------|
| `G4a-{role}` | `HALT [G4a-{role}] SCOPED: Lens anchor absent for {role}. Row skipped.` | `--amend rerun:{role}` |
| `G4b-{role}` | `HALT [G4b-{role}] SCOPED: No surface named for {role}. Row skipped.` | `--amend rerun:{role}` |
| `G4c-{role}` | `HALT [G4c-{role}] SCOPED: Severity '{value}' invalid for {role}. Row skipped.` | `--amend rerun:{role}` |
| `G4d-{role}` | `HALT [G4d-{role}] SCOPED: No location in recommendation for {role}. Row skipped.` | `--amend rerun:{role}` |

For BLOCKING halts: `→ Run cannot continue. Fix and: /crew-check [artifact] [re-entry command]`
For SCOPED halts: `→ Row excluded from matrix. Fix and: /crew-check [artifact] [re-entry command]`

---

### GATE 1 [G1 BLOCKING] — Registry

**You are not ready to select reviewers until this gate is passed.**

Read every file in `.craft/roles/`. Role pool = all discovered files. Zero invented roles.
For each: name, archetype, `orientation.frame`, `expertise.relevance`.

If `.craft/roles/` absent or empty: output `HALT [G1] BLOCKING` with its re-entry command. Stop.

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

Only HIGH (3), MEDIUM (2), LOW (1) are valid. Any other label triggers the appropriate
SCOPED halt for that role.

Gate 2 passed when: scale is locked here.

---

### GATE 3 — Reviewer selection

**Standard (default)**: Select 2–4 roles whose domain intersects the artifact type.
One rationale sentence per selection.
Challenger archetype roles always included regardless of relevance score.

**`--depth deep`**: Queue = entire pool. No rationale required.

Gate 3 passed when: queue is non-empty, rationale written (standard depth).

---

### GATE 4 — Per-reviewer execution [G4a through G4d per role; SCOPED halts]

**For each role, all four sub-gates must pass for the row to be staged.**
**SCOPED halt in any sub-gate: skip the row, continue with remaining roles.**

Process challenger archetype roles first, then others alphabetically.

For each role `{role}`:

**G4a-{role} — Lens anchor** *(readiness condition: not ready for the finding)*
Write: `Lens: "[quote or paraphrase from orientation.frame or lens.verify]"`
If absent: output `HALT [G4a-{role}] SCOPED` with its re-entry command. Skip this row.

**G4b-{role} — Finding with named surface** *(readiness condition: not ready for severity)*
Name the specific artifact surface: section, field, assumption, diagram element.
For challenger roles: state whether the status-quo alternative is demonstrably better,
worse, or equivalent.
If no surface can be named: output `HALT [G4b-{role}] SCOPED` with its re-entry command.
Skip this row.

**G4c-{role} — Valid severity** *(readiness condition: not ready for recommendation)*
Apply Gate 2 contract. If value outside HIGH / MEDIUM / LOW: output `HALT [G4c-{role}]
SCOPED` with its re-entry command. Skip this row.

**G4d-{role} — Recommendation with location** *(readiness condition: not ready to stage)*
One concrete action: what to do AND where. If location absent: output `HALT [G4d-{role}]
SCOPED` with its re-entry command. Skip this row.

Stage the row only when G4a through G4d all pass.

---

### GATE 5 [G5 BLOCKING] — Sort and render

**You are not ready to write the synthesis until: all rows staged AND sort succeeds.**

Sort all staged rows by severity score descending (3 → 2 → 1).
Within the same score: challenger rows before domain rows.

If rows cannot be consistently sorted: output `HALT [G5] BLOCKING` with its re-entry
command. This is a BLOCKING halt: the matrix cannot render until severity values are
consistent.

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|
*[rows sorted: HIGH first, then MEDIUM, then LOW; challengers before domain within each tier]*

Gate 5 passed when: matrix rendered, sorted, no blank cells.

If any rows were excluded by SCOPED halts, note below the matrix:
`[N] row(s) excluded by SCOPED halts. Run /crew-check [artifact] --amend halts to review.`

---

### Cross-role synthesis

2–3 sentences: name convergence, name conflict, or "No cross-role signal detected."
Note: synthesis reflects only staged rows; excluded rows are flagged separately.

---

### AMEND

> **AMEND**
> - Add reviewer: `/crew-check [artifact] --amend add:{role-name}` *(inserted in archetype sequence)*
> - Full registry: `/crew-check [artifact] --depth deep`
> - Fix and rerun excluded role: `/crew-check [artifact] --amend rerun:{role-name}`
> - Restart from Gate 1: `/crew-check [artifact] --amend reload`
> - **Halt audit**: `/crew-check [artifact] --amend halts`
>
> `--amend halts` output — tier-separated, each entry includes re-entry command:
>
> ```
> HALT AUDIT — [N] BLOCKING, [N] SCOPED:
>
> BLOCKING (must resolve to complete run):
>   none
>
> SCOPED (rows excluded; run is otherwise complete):
>   G4c-inertia-advocate | Severity 'CRITICAL' invalid
>   → /crew-check [artifact] --amend rerun:inertia-advocate
>
>   G4a-pm | Lens anchor absent
>   → /crew-check [artifact] --amend rerun:pm
>
> No halts recorded → "No halts recorded this run."
> ```

---

---

## V-04

**Axes**: Self-routing halts + Executable audit, cross-referenced
**Hypothesis**: In R4, C-19 (self-routing halts) and C-20 (executable audit) were implemented
independently. R4 V-03 had C-19: halt message contained a re-entry command. R4 V-02 had C-20:
audit entries contained commands. But the two systems did not reference each other — a halt
message did not cite the audit entry for that gate, and an audit entry did not back-reference
its source halt. V-04 cross-references them: every halt message ends with
`→ To continue: /crew-check [artifact] --amend rerun:{role}  [or see: --amend halts:G4c-{role}]`
and every audit entry for that gate contains both the resolution step and the re-entry command.
The two systems form a closed loop: a user who fires a halt can either act on the inline command
or consult the audit entry for a richer description. Both paths lead to the same paste command.
The bet: cross-referencing eliminates the choice paralysis of "do I use the inline command or
look at the audit?" — either path is complete. This is C-19 and C-20 as complementary systems,
not parallel ones.

---

You are running `/crew-check`.

Your task: pass the provided artifact through the registered org roles and produce a
severity-sorted review matrix. Three structural properties govern this run:

1. **Readiness gates**: you are not ready to advance past any gate until its condition is met.

2. **Self-routing hard halts**: every unmet gate produces a named halt message that contains
   two paths to recovery — an inline re-entry command and a reference to the audit entry for
   that specific gate.

3. **Executable audit**: `--amend halts` returns an audit block where every entry contains
   both a human-readable resolution step AND a paste-ready re-entry command. The audit is a
   command menu cross-referenced against the halt registry. No partial output. No silent skips.

---

### Halt registry (defined once; trigger exactly as written)

Substitutions: `{role}` = role file name (no extension); `{value}` = the invalid value received.

| Gate ID | Halt message |
|---------|--------------|
| `G1` | `HALT [G1]: .craft/roles/ absent or empty. Not ready to select reviewers.` |
| `G4a-{role}` | `HALT [G4a-{role}]: Lens anchor absent. Not ready for finding for {role}.` |
| `G4b-{role}` | `HALT [G4b-{role}]: No surface named. Not ready for severity for {role}.` |
| `G4c-{role}` | `HALT [G4c-{role}]: Severity '{value}' invalid. Not ready to stage {role}.` |
| `G4d-{role}` | `HALT [G4d-{role}]: No location in recommendation. Not ready to stage {role}.` |
| `G5` | `HALT [G5]: Severity values inconsistent. Not ready to render matrix.` |

When a halt fires, output the halt message then both recovery paths:
```
→ Quick fix: /crew-check [artifact] --amend rerun:{role}
→ Full audit entry: /crew-check [artifact] --amend halts:{gate-id}
```
(For G1 and G5: quick fix is `--amend reload`; audit entry is `--amend halts:G1` or `--amend halts:G5`.)

---

### GATE 1 [G1] — Registry

**You are not ready to select reviewers until this gate is passed.**

Read every file in `.craft/roles/`. Role pool = all discovered files. Zero invented roles.
For each: name, archetype, `orientation.frame`, `expertise.relevance`.

If `.craft/roles/` absent or empty: output `HALT [G1]` with both recovery paths. Stop.

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

Only HIGH (3), MEDIUM (2), LOW (1) are valid.

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
If absent: output `HALT [G4a-{role}]` with both recovery paths. Do not proceed.

**G4b-{role} — Finding with named surface** *(readiness condition: not ready for severity)*
Name the specific artifact surface: section, field, assumption, diagram element.
For challenger roles: state whether the status-quo alternative is demonstrably better,
worse, or equivalent.
If no surface can be named: output `HALT [G4b-{role}]` with both recovery paths.

**G4c-{role} — Valid severity** *(readiness condition: not ready for recommendation)*
Apply Gate 2 contract. Assign label; track score internally.
If value outside HIGH / MEDIUM / LOW: output `HALT [G4c-{role}]` with both recovery paths.

**G4d-{role} — Recommendation with location** *(readiness condition: not ready to stage)*
One concrete action: what to do AND where in the artifact.
If location absent: output `HALT [G4d-{role}]` with both recovery paths.

Stage the row only when G4a through G4d all pass.

---

### GATE 5 [G5] — Sort and render

**You are not ready to write the synthesis until: all rows staged AND sort succeeds.**

Sort all staged rows by severity score descending (3 → 2 → 1).
Within the same score: challenger rows before domain rows.

If rows cannot be consistently ordered: output `HALT [G5]` with both recovery paths. Resolve.

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|
*[rows sorted: HIGH first, then MEDIUM, then LOW; challengers before domain within each tier]*

Gate 5 passed when: matrix rendered, sorted, no blank cells.

---

### GATE 6 — Priority summary

**You are not ready to write the cross-role synthesis until this gate is passed.**

```
HIGH:   [N] finding(s) — [one-phrase summary, or "none"]
MEDIUM: [N] finding(s) — [one-phrase summary, or "none"]
LOW:    [N] finding(s) — [one-phrase summary, or "none"]
```

Gate 6 passed when: summary written.

---

### Cross-role synthesis

2–3 sentences: name convergence, name conflict, or "No cross-role signal detected."

---

### AMEND

> **AMEND**
> - Add reviewer: `/crew-check [artifact] --amend add:{role-name}` *(inserted in archetype sequence)*
> - Full registry: `/crew-check [artifact] --depth deep`
> - Re-run role from G4a: `/crew-check [artifact] --amend rerun:{role-name}`
> - Restart from Gate 1: `/crew-check [artifact] --amend reload`
> - **Gate audit**: `/crew-check [artifact] --amend halts`
>   - Focused: `/crew-check [artifact] --amend halts:{gate-id}`
>
> `--amend halts` output — each entry cross-referenced with its halt message, plus paste command:
>
> ```
> HALT AUDIT — [N] gate(s) fired this run:
>
> G4c-pm
>   Halt fired: HALT [G4c-pm]: Severity 'CRITICAL' invalid. Not ready to stage pm.
>   Resolution: Assign HIGH, MEDIUM, or LOW. Revise the severity cell for pm.
>   Re-entry: /crew-check [artifact] --amend rerun:pm
>
> G4a-architect
>   Halt fired: HALT [G4a-architect]: Lens anchor absent. Not ready for finding for architect.
>   Resolution: Quote or paraphrase from architect.orientation.frame or architect.lens.verify.
>   Re-entry: /crew-check [artifact] --amend rerun:architect
>
> No gates fired → "No halts recorded this run."
> ```
>
> Each entry: gate ID · full halt message · resolution instruction · paste command.
> `--amend halts:{id}` returns only that entry.
> Note: every halt message already contains Quick-fix and Full-audit-entry commands inline.
> The audit provides the full resolution description when the inline command is not enough.

---

---

## V-05

**Axes**: All four C-17+C-18+C-19+C-20, plus recovery-first flow
**Hypothesis**: R4 V-05 was the full integration of C-17 and C-18 plus C-19 and C-20. All four
mechanisms were present. The AMEND block was the terminus of the skill — a user who needed to
recover had to scroll to the AMEND section to find the audit command. V-05 R5 adds a structural
element that eliminates that scroll: a RECOVERY BLOCK that surfaces immediately before the AMEND
section when any halt fires during the run. The recovery block is a compact numbered action list
of all fired gates — in execution order, with paste-ready commands — making recovery the primary
visible output of a failed run and review the primary visible output of a passing run. The recovery
block is not duplicated in the AMEND section; the AMEND section remains the full command reference.
The bet: surfacing the recovery list immediately before AMEND means a user never has to locate the
audit sub-command — the action list is already there. C-19 (halts self-route) and C-20 (audit is
executable) are both satisfied by the recovery block AND by the AMEND audit format, making the
two mechanisms redundant in the best sense: either alone is sufficient for recovery; together they
guarantee it.

---

You are running `/crew-check`.

Your task: pass the provided artifact through the registered org roles and produce a
severity-sorted review matrix. Four structural properties govern this run:

1. **Readiness gates**: you are not ready to advance past any gate until its condition is fully
   met. Every transition is a readiness assertion.

2. **Named hard halts**: every unmet gate produces the specific halt message from the registry.
   Halt IDs are stable handles — they appear verbatim in registry, gate headers, halt messages,
   AMEND routing, and audit output. No partial output. No silent skips.

3. **Self-routing halts**: every halt message ends with its re-entry command. The halt tells you
   what went wrong AND what to type next. No secondary lookup required for single-gate recovery.

4. **Recovery-first output**: if any halts fired during the run, a RECOVERY BLOCK appears before
   the AMEND section — a numbered action list of all fired gates with paste-ready commands, ordered
   by gate execution order. If no halts fired, no recovery block appears.

---

### Halt registry (defined once; trigger exactly as written)

Each entry: Gate ID, halt message, re-entry command.
Substitutions: `{role}` = role file name (no extension); `{value}` = the invalid value received.

| Gate ID | Halt message | Re-entry command |
|---------|--------------|-----------------|
| `G1` | `HALT [G1]: .craft/roles/ absent or empty. Not ready to select reviewers.` | `--amend reload` |
| `G4a-{role}` | `HALT [G4a-{role}]: Lens anchor absent. Not ready for finding for {role}.` | `--amend rerun:{role}` |
| `G4b-{role}` | `HALT [G4b-{role}]: No surface named. Not ready for severity for {role}.` | `--amend rerun:{role}` |
| `G4c-{role}` | `HALT [G4c-{role}]: Severity '{value}' invalid. Not ready to stage {role}.` | `--amend rerun:{role}` |
| `G4d-{role}` | `HALT [G4d-{role}]: No location in recommendation. Not ready to stage {role}.` | `--amend rerun:{role}` |
| `G5` | `HALT [G5]: Severity values inconsistent. Not ready to render matrix.` | `--amend reload` |

When a halt fires: output halt message, then: `→ To continue: /crew-check [artifact] [re-entry command]`

---

### GATE 1 [G1] — Registry

**You are not ready to select reviewers until this gate is passed.**

Read every file in `.craft/roles/`. Role pool = all discovered files. Zero invented roles.
For each: name, archetype, `orientation.frame`, `expertise.relevance`.

If `.craft/roles/` absent or empty: output `HALT [G1]` with its re-entry command. Stop.

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

Only HIGH (3), MEDIUM (2), LOW (1) are valid.

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
If no surface can be named: output `HALT [G4b-{role}]` with re-entry command.

**G4c-{role} — Valid severity** *(readiness condition: not ready for recommendation)*
Apply Gate 2 contract. Assign label; track score internally.
If value outside HIGH / MEDIUM / LOW: output `HALT [G4c-{role}]` with re-entry command.

**G4d-{role} — Recommendation with location** *(readiness condition: not ready to stage)*
One concrete action: what to do AND where in the artifact.
If location absent: output `HALT [G4d-{role}]` with re-entry command.

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

### RECOVERY BLOCK *(appears only if any halt fired during this run)*

If no halts fired: omit this section entirely.

If any halts fired:

```
RECOVERY — [N] gate(s) fired this run (paste and execute in order):

1. [G4a-pm] Lens anchor absent
   → /crew-check [artifact] --amend rerun:pm

2. [G4c-inertia-advocate] Severity 'BLOCKER' invalid
   → /crew-check [artifact] --amend rerun:inertia-advocate

After all fixes: /crew-check [artifact]
```

This block is a complete action list. Execute top-to-bottom. No audit lookup needed.
Each entry: execution number · gate ID · one-line description · paste command.

---

### AMEND

> **AMEND**
> - Add reviewer: `/crew-check [artifact] --amend add:{role-name}` *(inserted in archetype sequence)*
> - Full registry: `/crew-check [artifact] --depth deep`
> - Re-run role from G4a: `/crew-check [artifact] --amend rerun:{role-name}`
> - Restart from Gate 1: `/crew-check [artifact] --amend reload`
> - Show unsorted matrix: `/crew-check [artifact] --amend unsorted`
> - **Gate audit**: `/crew-check [artifact] --amend halts`
>   - Focused: `/crew-check [artifact] --amend halts:{gate-id}`
>
> `--amend halts` output — each fired gate entry is a paste-ready action:
>
> ```
> HALT AUDIT — [N] gate(s) fired this run:
>
> Gate ID          | Gate name      | Message triggered                              | Re-entry command
> -----------------|----------------|------------------------------------------------|----------------------------------------
> G4a-pm           | Lens anchor    | HALT [G4a-pm]: Lens anchor absent...           | /crew-check [artifact] --amend rerun:pm
> G4c-inertia-adv  | Severity       | HALT [G4c-inertia-advocate]: 'BLOCKER'...      | /crew-check [artifact] --amend rerun:inertia-advocate
>
> No gates fired → "No halts recorded this run."
> ```
>
> Note: the RECOVERY BLOCK above is the primary action list for failed runs.
> `--amend halts` provides the detailed audit format for reference, multi-session replay,
> or when the recovery block has scrolled out of view.
> Every halt message also contains its re-entry command inline.
> Three independent recovery paths; any one is sufficient.
