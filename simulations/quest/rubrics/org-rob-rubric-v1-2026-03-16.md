---
skill: quest-rubric
skill_target: org-rob
date: 2026-03-16
version: 1
---

# Scoring Rubric — org-rob

## Purpose

`org-rob` runs a Review of Business (ROB) governance stage for a repo or artifact.
Six stages: `leadership` (VP briefing), `teams` (12 team self-reviews), `pm` (PM
cross-alignment), `tpm` (risk register + go/no-go), `arch-board` (architecture board
review), `spire` (S-office missions cascade). Roles loaded from `.craft/roles/`.
Use cases: ship decisions, quarterly planning, major architecture changes.

This rubric defines what a passing org-rob output looks like. It is the objective
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

### C-01 — Stage Identity
- **Category**: format
- **Weight**: essential
- **Text**: Output clearly names each stage that was run using the canonical label
  (`leadership`, `teams`, `pm`, `tpm`, `arch-board`, `spire`). Each section is
  headed by the stage name and the role type conducting it.
- **Pass condition**: Every stage run has a section header that includes both the
  canonical stage name and the role conducting it. No stage is anonymous.

---

### C-02 — Role-Loaded Perspective
- **Category**: correctness
- **Weight**: essential
- **Text**: Each stage review reflects the perspective of the role loaded from
  `.craft/roles/` — not a generic review. The role's orientation, lens, and
  expertise shape which concerns are raised.
- **Pass condition**: At least one finding per stage is grounded in the loaded
  role's documented lens (e.g., a PM flags adoption risk, a TPM flags schedule
  risk, an architect flags coupling). Generic findings that any role could have
  written do not satisfy this criterion.

---

### C-03 — ROB Document Format
- **Category**: format
- **Weight**: essential
- **Text**: Output follows the ROB stage document format: stage header, role
  identity, numbered findings with severity, and a stage verdict. All four
  structural elements must be present for each stage.
- **Pass condition**: For each stage run: (1) stage header present, (2) role
  identity stated, (3) at least one finding with severity label (HIGH/MED/LOW
  or equivalent), (4) explicit stage verdict (APPROVED / APPROVED WITH CONDITIONS
  / BLOCKED / DEFERRED or equivalent).

---

### C-04 — Actionable Findings
- **Category**: depth
- **Weight**: essential
- **Text**: Each stage produces at least 2 concrete findings or decision points.
  Findings name a specific concern, not a category. Each finding has an implied
  or explicit owner and a suggested resolution or next step.
- **Pass condition**: Total findings >= 2 * N_stages_run. Each finding is specific
  (references the artifact, not just the domain). At least half of findings include
  a resolution path or owner.

---

### C-05 — Go/No-Go Signal
- **Category**: correctness
- **Weight**: essential
- **Text**: When the `tpm` stage runs (including via `--stage all`), output includes
  an explicit go/no-go recommendation with rationale. The verdict is not implied or
  buried — it is a top-level statement.
- **Pass condition**: `tpm` stage output contains an unambiguous GO / NO-GO /
  GO WITH CONDITIONS verdict as a labeled top-level element, accompanied by at
  least one sentence of rationale citing a specific finding.

---

## Recommended Criteria

*Output is better with these. Each adds material value.*

### C-06 — Cross-Stage Coherence
- **Category**: depth
- **Weight**: recommended
- **Text**: When multiple stages run, later stages reference or escalate findings
  from earlier stages. The escalation chain (teams -> pm -> tpm) is visible: a
  teams finding becomes a pm alignment item, which becomes a tpm risk.
- **Pass condition**: At least 2 cross-stage references in any multi-stage run
  (e.g., "teams raised X; pm confirms X is unresolved; tpm registers X as risk R-02").

---

### C-07 — Risk Register Structure
- **Category**: depth
- **Weight**: recommended
- **Text**: The `tpm` stage produces a structured risk register, not a prose list.
  Each entry has a title, severity, likelihood, and mitigation. The register is
  machine-scannable.
- **Pass condition**: `tpm` stage includes a risk register table or structured list
  with >= 3 entries, each containing title, severity, likelihood, and mitigation.
  At least one risk is rated HIGH.

---

### C-08 — Spire Cascade Tracing
- **Category**: coverage
- **Weight**: recommended
- **Text**: When the `spire` stage runs, output traces how S-office missions cascade
  down to the artifact under review. At least one mission-to-artifact link is
  explicit: mission -> program -> artifact alignment or gap.
- **Pass condition**: `spire` stage output names at least one S-office mission by
  name and traces its alignment or misalignment to the artifact under review with
  a specific example.

---

## Aspirational Criteria

*Raise the bar once essential and recommended are stable.*

### C-09 — Inter-Stage Blocker Detection
- **Category**: depth
- **Weight**: aspirational
- **Text**: Output explicitly identifies when a finding from one stage creates a
  hard blocker for a downstream stage. Blockers are surfaced proactively, not
  discovered retroactively.
- **Pass condition**: At least 1 inter-stage blocker is named in a multi-stage run,
  with the upstream stage, the blocking finding, and the downstream stage impact
  stated explicitly (e.g., "teams finding F-03 blocks tpm go/no-go: ownership
  unresolved").

---

### C-10 — Cross-Cutting Theme Elevation
- **Category**: depth
- **Weight**: aspirational
- **Text**: When the same concern surfaces in 2 or more stages, output recognizes
  the pattern and elevates it as a cross-cutting theme — above the individual stage
  findings. Cross-cutting themes receive priority weighting.
- **Pass condition**: At least 1 cross-cutting theme is named at the document level
  (not buried inside a single stage), citing the 2+ stages that surfaced it and
  noting why the repetition increases severity.

---

## Criterion Summary

| ID   | Text (short)                        | Weight        | Category    |
|------|-------------------------------------|---------------|-------------|
| C-01 | Stage identity and labeling         | essential     | format      |
| C-02 | Role-loaded perspective             | essential     | correctness |
| C-03 | ROB document format compliance      | essential     | format      |
| C-04 | Actionable findings (2x per stage)  | essential     | depth       |
| C-05 | Explicit go/no-go in tpm stage      | essential     | correctness |
| C-06 | Cross-stage coherence               | recommended   | depth       |
| C-07 | Risk register structure in tpm      | recommended   | depth       |
| C-08 | Spire cascade tracing               | recommended   | coverage    |
| C-09 | Inter-stage blocker detection       | aspirational  | depth       |
| C-10 | Cross-cutting theme elevation       | aspirational  | depth       |

---

## Example Score Calculation

All 5 essential pass, 2 of 3 recommended pass, 0 of 2 aspirational pass:

```
composite = (5/5 * 60) + (2/3 * 30) + (0/2 * 10)
          = 60 + 20 + 0
          = 80
```

Golden threshold met (all essential pass, composite = 80).

All 5 essential pass, 3/3 recommended pass, 2/2 aspirational pass = 100.
Any essential failure = not golden regardless of composite.
