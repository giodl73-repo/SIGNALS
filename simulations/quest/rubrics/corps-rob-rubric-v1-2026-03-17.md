---
skill: quest-rubric
skill_target: corps-rob
date: 2026-03-17
version: 1
---

# Scoring Rubric -- corps-rob

## Purpose

`corps-rob` runs a Review of Business (ROB) for a given topic across six staged
governance functions: `leadership` (exec briefing), `teams` (all team self-reviews),
`pm` (PM cross-alignment), `tpm` (risk register + go/no-go), `arch-board`
(architecture board), `exec-office` (S-office missions cascade). Roles loaded from
`org.yaml` and `.craft/roles/`. Flags: `--stage all` (full sequence), `--stage [name]`
(single stage), `--scope [group]` (one division or tribe).

This rubric defines what a passing `corps-rob` output looks like and is the objective
function for `/quest-golden`.

---

## Scoring Formula

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

**Golden threshold**: all essential criteria pass AND composite >= 80.

---

## Essential Criteria

*Must all pass. Without these the output is not useful.*

### C-01 -- Stage Identity
- **Category**: format
- **Weight**: essential
- **Text**: Output clearly identifies each stage that was run using the canonical label
  (`leadership`, `teams`, `pm`, `tpm`, `arch-board`, `exec-office`). Each stage section
  is headed by both the stage name and the role conducting it. No stage is anonymous and
  no stage is silently merged with another.
- **Pass condition**: Every stage run has a section header containing the canonical stage
  name and the name or role title of the assigned persona. Labels must match the six
  canonical names exactly -- no substitutions or abbreviations.

---

### C-02 -- Role-Loaded Perspective
- **Category**: correctness
- **Weight**: essential
- **Text**: Each stage review reflects the documented lens of the persona loaded from
  `.craft/roles/` via `org.yaml` -- not a generic review any role could have written.
  The role's orientation shapes which concerns are surfaced and how they are framed.
- **Pass condition**: At least one finding per stage is grounded in the loaded persona's
  specific lens (e.g., a TPM flags schedule risk and dependency gaps, a Principal Architect
  flags interface coupling, a PM flags adoption risk, a Chief of Staff flags mission
  alignment). Findings that are fully generic -- applicable by any reviewer to any topic --
  do not satisfy this criterion for any stage in which they appear.

---

### C-03 -- ROB Document Format
- **Category**: format
- **Weight**: essential
- **Text**: Each stage document follows the ROB format: stage header, role identity,
  numbered findings with severity labels, and an explicit stage verdict. All four structural
  elements are required per stage.
- **Pass condition**: For each stage run, all four are present: (1) stage header with
  canonical name, (2) role identity statement, (3) at least one finding carrying a severity
  label (HIGH / MED / LOW or equivalent), (4) an explicit stage verdict using one of the
  four tokens: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED.

---

### C-04 -- Actionable Findings
- **Category**: depth
- **Weight**: essential
- **Text**: Each stage produces at least two concrete findings. Each finding names a
  specific concern -- not a category or domain name. Each finding carries an explicit or
  implied owner and a resolution path or next step.
- **Pass condition**: Total findings across all stages >= 2 * N_stages_run. Each finding
  references the specific artifact or topic under review, not just the problem domain.
  At least 50% of findings include an owner (role name) and a resolution action. "Needs
  attention" or "review required" alone does not constitute a resolution.

---

### C-05 -- TPM Go/No-Go Signal
- **Category**: correctness
- **Weight**: essential
- **Text**: When the `tpm` stage runs (including via `--stage all`), output contains an
  explicit go/no-go recommendation. The verdict is not implied, buried in prose, or
  deferred to a future stage -- it is a top-level labeled statement in the tpm section.
- **Pass condition**: `tpm` stage output contains an unambiguous GO / NO-GO /
  GO WITH CONDITIONS verdict as a labeled, top-level element (heading, bold label, or
  equivalent structural marker), accompanied by at least one sentence of rationale that
  cites a specific finding ID or risk ID.

---

## Recommended Criteria

*Output is better with these. Each adds material value.*

### C-06 -- Risk Register Structure
- **Category**: depth
- **Weight**: recommended
- **Text**: The `tpm` stage produces a structured risk register, not a prose narrative.
  Each entry carries a title, severity, likelihood, and mitigation. The register is
  machine-scannable and actionable.
- **Pass condition**: `tpm` stage includes a risk register table or structured list with
  >= 3 entries. Each entry contains: title (specific risk name), severity (HIGH/MED/LOW),
  likelihood (HIGH/MED/LOW), and mitigation (concrete action). At least one risk is rated
  HIGH severity. Prose-only risk summaries do not satisfy this criterion.

---

### C-07 -- Exec-Office Mission Cascade
- **Category**: coverage
- **Weight**: recommended
- **Text**: When the `exec-office` stage runs, output traces how at least one named
  S-office mission cascades down to the artifact under review. The mission must be named
  by title -- not paraphrased as "strategic priorities" or "company goals". Alignment or
  gap must be stated explicitly with a specific example.
- **Pass condition**: `exec-office` stage output names at least one S-office mission by
  its actual title and traces the path from that mission to the artifact with an explicit
  ALIGNED / PARTIAL / GAP verdict. Vague alignment claims ("supports our direction")
  do not pass. A Mission Cascade table with at least one populated row satisfies this.

---

### C-08 -- Cross-Stage Coherence
- **Category**: depth
- **Weight**: recommended
- **Text**: When multiple stages run, later stages reference or escalate findings from
  earlier stages. The escalation chain (teams -> pm -> tpm) is visible in the output:
  a teams finding becomes a pm alignment issue, which becomes a tpm risk register entry.
- **Pass condition**: At least 2 cross-stage references appear in any multi-stage run.
  Each reference names the source stage, the source finding ID, and how the current stage
  confirms, escalates, or contradicts it (e.g., "teams F-02 escalated: pm confirms
  ownership still unresolved"). Forward-looking references ("future stages should watch X")
  do not count -- references must look backward.

---

## Aspirational Criteria

*Raise the bar once essential and recommended are stable.*

### C-09 -- Inter-Stage Blocker Detection
- **Category**: depth
- **Weight**: aspirational
- **Text**: Output explicitly surfaces when a finding in one stage creates a hard blocker
  for a downstream stage. Blockers are identified at the stage boundary where they arise,
  not discovered retroactively at a later stage.
- **Pass condition**: At least 1 inter-stage blocker is named in a multi-stage run,
  specifying: the upstream stage that raised it, the blocking finding ID, the downstream
  stage it blocks, and the reason the downstream stage cannot proceed (e.g., "teams F-03
  blocks tpm go/no-go: data ownership unresolved, risk register cannot be finalized").
  A BLOCKER CHECK section or equivalent structural marker at the stage close satisfies
  this if populated with a concrete finding reference.

---

### C-10 -- Cross-Cutting Theme Elevation
- **Category**: depth
- **Weight**: aspirational
- **Text**: When the same concern surfaces in 2 or more stages independently, output
  recognizes the pattern and elevates it as a cross-cutting theme above individual stage
  findings. The theme names why repetition across stages increases severity beyond any
  single-stage instance.
- **Pass condition**: At least 1 cross-cutting theme is named at the document level (in a
  Cross-Cutting Themes section or equivalent, not embedded inside a single stage), citing
  the 2+ stages that surfaced it and explaining the elevated severity. Copying one finding
  verbatim from one stage and labeling it a theme does not satisfy this -- the theme must
  characterize the pattern of recurrence.

---

## Criterion Summary

| ID   | Text (short)                         | Weight        | Category    |
|------|--------------------------------------|---------------|-------------|
| C-01 | Stage identity and labeling          | essential     | format      |
| C-02 | Role-loaded perspective              | essential     | correctness |
| C-03 | ROB document format compliance       | essential     | format      |
| C-04 | Actionable findings (2x per stage)   | essential     | depth       |
| C-05 | Explicit go/no-go in tpm stage       | essential     | correctness |
| C-06 | Risk register structure in tpm       | recommended   | depth       |
| C-07 | Exec-office mission cascade          | recommended   | coverage    |
| C-08 | Cross-stage coherence (2+ refs)      | recommended   | depth       |
| C-09 | Inter-stage blocker detection        | aspirational  | depth       |
| C-10 | Cross-cutting theme elevation        | aspirational  | depth       |

---

## Example Score Calculations

**All essential pass, 2 of 3 recommended pass, 0 of 2 aspirational pass:**

```
composite = (5/5 * 60) + (2/3 * 30) + (0/2 * 10)
          = 60 + 20 + 0
          = 80
```

Golden threshold met (all essential pass, composite = 80).

**All essential pass, 3/3 recommended pass, 1/2 aspirational pass:**

```
composite = (5/5 * 60) + (3/3 * 30) + (1/2 * 10)
          = 60 + 30 + 5
          = 95
```

**Any essential failure = not golden regardless of composite.**
