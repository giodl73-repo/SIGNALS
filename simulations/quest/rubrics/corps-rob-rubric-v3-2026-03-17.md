Here is the complete updated rubric as written.

---

**What changed in v3:**

Two new aspirational criteria extracted from R3 excellence signals:

| ID | Name | Pattern | Source |
|----|------|---------|--------|
| C-14 | Stage-Open Briefing Envelope | `stage-open-briefing-envelope` | V-03 + V-04 both achieve C-08 "PASS (strong)" via this mechanism; V-02 fails C-08 partially specifically because it is absent. Forces role-loading to operate on forwarded context *at stage open* before any findings are written. |
| C-15 | Anti-Redundancy Synthesis Constraint | `anti-redundancy-synthesis-constraint` | V-04 specific. When both Cross-Stage References (findings body) and CROSS-STAGE SYNTHESIS (handoff packet) appear, an explicit guard ("Must add substance not already stated in the Cross-Stage References section above") prevents the two mechanisms from collapsing into copies of each other. |

**Scoring change:** N_aspirational goes from 5 to 7. Formula is unchanged: `(N_pass/7 * 10)`. Each full aspirational pass is now worth 10/7 ≈ 1.4 pts instead of 2 pts.

**Re-grades:**
- V-04 R3: 7/7 aspirational PASS → **100** (was 99 under v2; ceiling unchanged)
- V-03 R3: C-14 PASS, C-15 FAIL, C-10 FAIL → 5/7 → **97.1**
- V-01 R3: C-14 FAIL, C-15 FAIL, C-11 PARTIAL → 4.5/7 → **96.4**

**Design note:** C-14 explains *why* V-02 fails C-08 partially in R3 — the diagnostic now has a name. C-15 captures the extra mile that distinguishes V-04 from V-03 even when both have the triple coherence mechanism.
 canonical label
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
  `.roles/` via `org.yaml` -- not a generic review any role could have written.
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

### C-11 -- Handoff Packet at Stage Close
- **Category**: structure
- **Weight**: aspirational
- **Source**: R1 excellence signal -- V-04 pattern `handoff-packet-at-stage-close`
- **Text**: Each stage (from Stage 2 onward in a multi-stage run) closes with a formal
  HANDOFF PACKET section that catalogs cross-stage references to prior findings. The
  handoff packet makes C-08 (cross-stage coherence) a process output rather than a
  model-recall artifact -- every stage is structurally forced to scan what came before.
  In a 6-stage full run this produces a minimum of 5 structured cross-stage entries.
- **Pass condition**: Each stage after the first contains a dedicated HANDOFF PACKET (or
  equivalent labeled section) at the stage close. Each packet lists at least one
  cross-stage reference entry giving: source stage name, source finding ID, and
  relationship type (confirms / escalates / contradicts). A 3-stage run must contain a
  minimum of 5 cross-stage entries distributed across all packets.

---

### C-12 -- Stage-Boundary Blocker Field
- **Category**: structure
- **Weight**: aspirational
- **Source**: R1 excellence signal -- V-04 pattern `stage-boundary-blocker-detection`
- **Text**: Each stage close contains a BLOCKER field (as part of the handoff packet or
  as a standalone structural marker). The field is populated at the stage boundary where
  the blocker arises -- not deferred to a later stage or collected retroactively in a
  document-level ledger. A post-hoc escalation ledger at the document end does not satisfy
  this criterion because it cannot detect blockers before the downstream stage runs.
- **Pass condition**: Each stage close contains a BLOCKER: YES / NO field (or equivalent
  labeled element). For every YES entry, the field names: the blocking finding ID, the
  downstream stage that is blocked, and the specific reason the downstream stage cannot
  proceed without resolution. A BLOCKER: NO entry is acceptable and still satisfies the
  structural requirement for that stage.

---

### C-13 -- Inertia Anchor and Per-Stage Inertia Check
- **Category**: depth
- **Weight**: aspirational
- **Source**: R1 excellence signal -- V-04 pattern `inertia-anchor-per-stage-check`
- **Text**: The run opens with an INERTIA ANCHOR section that names what the topic
  displaces and who bears the cost of change. Each stage then opens with an INERTIA CHECK
  that forces the reviewing role to articulate the status-quo pressure from their own
  perspective before writing findings. This mechanism grounds C-02 (role-loaded
  perspective) in concrete inertia context rather than relying on the model to infer it.
- **Pass condition**: Output contains an INERTIA ANCHOR (or equivalent labeled section)
  before Stage 1 that names at least one specific thing displaced by the topic and
  identifies the cost-bearer (team, system, or process). At least 3 stage sections contain
  an INERTIA CHECK (or equivalent labeled step) that frames the status-quo tension from
  the reviewing role's specific perspective -- not a generic "change is hard" statement.

---

### C-14 -- Stage-Open Briefing Envelope
- **Category**: structure
- **Weight**: aspirational
- **Source**: R3 excellence signal -- V-03 and V-04 pattern `stage-open-briefing-envelope`
- **Text**: Each stage (from Stage 2 onward) opens with a BRIEFING ENVELOPE section that
  distills what the current reviewing role should attend to from prior stages, filtered
  through their specific role lens. The envelope forces C-02 role-loading to operate on
  forwarded cross-stage context before any findings are written -- the role does not just
  receive prior findings verbatim, it selects which ones are relevant from its own
  perspective. In a 6-stage full run this produces 5 lens-filtered distillations. Without
  this mechanism, C-08 cross-stage coherence is structurally enforced only at the close
  (via handoff packet) but not at the open, leaving a gap where the reviewing role begins
  writing findings without first scanning what came before through its lens.
- **Pass condition**: Each stage after the first contains a BRIEFING ENVELOPE (or
  equivalent labeled section) at the stage open. Each envelope: (1) names the reviewing
  role's lens explicitly, (2) lists forwarded concerns selected as relevant from that
  role's perspective -- not a verbatim copy of prior findings but a role-filtered
  selection, (3) carries an instruction (explicit or demonstrated) that selection must be
  lens-directed. A "Must be lens-directed" instruction in the template satisfies the
  structural requirement if the output demonstrates genuine selection. A 6-stage full run
  requires at least 5 envelopes; a 3-stage run requires at least 2.

---

### C-15 -- Anti-Redundancy Synthesis Constraint
- **Category**: depth
- **Weight**: aspirational
- **Source**: R3 excellence signal -- V-04 pattern `anti-redundancy-synthesis-constraint`
- **Text**: When both a Cross-Stage References section (in the findings body) and a
  CROSS-STAGE SYNTHESIS section (in the handoff packet) appear in the same stage, an
  explicit anti-redundancy constraint prevents the synthesis from being a copy of the
  references. The two coherence mechanisms serve different purposes: the references section
  surfaces backward citations as they become relevant to individual findings; the synthesis
  section at the close names the downstream significance of the collected cross-stage
  picture. Without a constraint, the synthesis collapses into a restatement of the
  references, eliminating the value added by the second mechanism.
- **Pass condition**: When C-08 and C-11 both pass in the same run, at least one stage
  contains an explicit anti-redundancy instruction or demonstrates non-redundant synthesis.
  "Must add substance not already stated in the Cross-Stage References section above" or
  equivalent satisfies the structural requirement. A handoff synthesis that mirrors the
  wording of the corresponding cross-stage references section does not satisfy this
  criterion even if both sections are present. Acceptable substance added by the synthesis
  includes: risk escalation beyond any single reference, naming of a pattern across
  multiple references, or a specific downstream action not stated in any individual
  reference.

---

## Criterion Summary

| ID   | Text (short)                              | Weight        | Category    |
|------|-------------------------------------------|---------------|-------------|
| C-01 | Stage identity and labeling               | essential     | format      |
| C-02 | Role-loaded perspective                   | essential     | correctness |
| C-03 | ROB document format compliance            | essential     | format      |
| C-04 | Actionable findings (2x per stage)        | essential     | depth       |
| C-05 | Explicit go/no-go in tpm stage            | essential     | correctness |
| C-06 | Risk register structure in tpm            | recommended   | depth       |
| C-07 | Exec-office mission cascade               | recommended   | coverage    |
| C-08 | Cross-stage coherence (2+ refs)           | recommended   | depth       |
| C-09 | Inter-stage blocker detection             | aspirational  | depth       |
| C-10 | Cross-cutting theme elevation             | aspirational  | depth       |
| C-11 | Handoff packet at stage close             | aspirational  | structure   |
| C-12 | Stage-boundary blocker field              | aspirational  | structure   |
| C-13 | Inertia anchor and per-stage check        | aspirational  | depth       |
| C-14 | Stage-open briefing envelope              | aspirational  | structure   |
| C-15 | Anti-redundancy synthesis constraint      | aspirational  | depth       |

---

## Example Score Calculations

**All essential pass, 2 of 3 recommended pass, 0 of 7 aspirational pass:**

```
composite = (5/5 * 60) + (2/3 * 30) + (0/7 * 10)
          = 60 + 20 + 0
          = 80
```

Golden threshold met (all essential pass, composite = 80).

**All essential pass, 3/3 recommended pass, 3/7 aspirational pass:**

```
composite = (5/5 * 60) + (3/3 * 30) + (3/7 * 10)
          = 60 + 30 + 4.3
          = 94.3
```

**All essential pass, 3/3 recommended pass, 7/7 aspirational pass (ceiling):**

```
composite = (5/5 * 60) + (3/3 * 30) + (7/7 * 10)
          = 60 + 30 + 10
          = 100
```

**R3 top score under v3 (V-04: all 15 criteria PASS):**

```
composite = (5/5 * 60) + (3/3 * 30) + (7/7 * 10)
          = 60 + 30 + 10
          = 100
```

V-04 scored 99 under v2 (C-10 was PARTIAL in R1; C-10 PASS in R3). Under v3, V-04 R3
scores 100 because C-14 (briefing envelope) and C-15 (anti-redundancy constraint) directly
match its own structural patterns. The ceiling is unchanged -- the new criteria do not
penalize earlier variates, they identify what V-04 R3 was already doing that had no name.

**R3 V-03 re-graded under v3 (C-10 FAIL, C-14 PASS, C-15 FAIL, all others PASS):**

```
composite = (5/5 * 60) + (3/3 * 30) + (5/7 * 10)
          = 60 + 30 + 7.1
          = 97.1
```

V-03 gains C-14 (it has the briefing envelope) but fails C-15 (no explicit anti-redundancy
constraint between its cross-stage references and synthesis sections) and still fails C-10.

**Any essential failure = not golden regardless of composite.**
