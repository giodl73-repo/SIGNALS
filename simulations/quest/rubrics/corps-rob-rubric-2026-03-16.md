Rubric written to `simulations/quest/rubrics/corps-rob-rubric-2026-03-16.md`.

**corps-rob v1 rubric summary:**

| Tier | Criteria | Max |
|------|----------|-----|
| Essential (5) | C-01 stage labeling, C-02 role-loaded perspective, C-03 ROB format compliance, C-04 actionable findings (2x/stage), C-05 go/no-go in tpm | 60 |
| Recommended (3) | C-06 cross-stage coherence, C-07 structured risk register, C-08 exec-office cascade tracing | 30 |
| Aspirational (2) | C-09 inter-stage blocker detection, C-10 cross-cutting theme elevation | 10 |

**Total max: 100. Golden threshold: all essential pass + composite >= 80.**

The rubric is structurally aligned with `org-rob` v1 (same 5 essential criteria — the skills are identical in behavior, just in different namespaces). C-08 is slightly different: where org-rob uses "spire cascade," corps-rob uses "exec-office cascade" to match the corps skill's `exec-office` stage name from the description. The scoring model is simpler than org-rob v5 (which accumulated 19 criteria over 5 rounds) — appropriate for a v1 that can evolve through quest simulation.
 composite score.

---

## Essential Criteria

*Output must satisfy all five. Any essential failure = not golden regardless of
composite score.*

### C-01 -- Stage Identity and Labeling
- **Category**: format
- **Weight**: essential
- **Text**: Every stage in the output is explicitly labeled with its name. The
  stage header identifies which stage is running -- not inferred from context or
  implied by position. A reader must be able to locate any stage without parsing
  surrounding prose.
- **Pass condition**: Each stage in the output includes a labeled header
  identifying it by name (e.g., `## Stage: leadership`, `## Stage: tpm`).
  No stage is anonymous or identified only by position.

---

### C-02 -- Role-Loaded Perspective
- **Category**: correctness
- **Weight**: essential
- **Text**: Each stage review reflects the perspective of the role loaded from
  .craft/roles/ -- not a generic review. The role orientation, lens, and expertise
  shape which concerns are raised. A PM flags adoption and alignment risk; a TPM
  flags schedule and delivery risk; an architect flags coupling and interface risk.
- **Pass condition**: At least one finding per stage is grounded in the loaded
  role's documented lens. Generic findings that any role could have written do not
  satisfy this criterion. The stage header or ROLE: line names the loaded persona.

---

### C-03 -- ROB Document Format Compliance
- **Category**: format
- **Weight**: essential
- **Text**: Output follows the ROB stage document format: stage header, role
  identity, numbered findings with severity, and a stage verdict. All four
  structural elements must be present for each stage run.
- **Pass condition**: For each stage run: (1) stage header present, (2) role
  identity stated, (3) at least one finding with a severity label (HIGH / MED / LOW
  or equivalent), (4) explicit stage verdict (APPROVED / APPROVED WITH CONDITIONS /
  BLOCKED / DEFERRED or equivalent). All four elements required per stage.

---

### C-04 -- Actionable Findings
- **Category**: depth
- **Weight**: essential
- **Text**: Each stage produces at least 2 concrete findings or decision points.
  Findings name a specific concern, not a category. Each finding has an implied or
  explicit owner and a suggested resolution or next step.
- **Pass condition**: Total findings >= 2 * N_stages_run. Each finding is specific
  (references the artifact or topic, not just the domain). At least half of all
  findings include a resolution path or owner.

---

### C-05 -- Go/No-Go Signal in TPM Stage
- **Category**: correctness
- **Weight**: essential
- **Text**: When the tpm stage runs (including via --stage all), output includes
  an explicit go/no-go recommendation with rationale. The verdict is not implied or
  buried -- it is a top-level statement.
- **Pass condition**: tpm stage output contains an unambiguous GO / NO-GO /
  GO WITH CONDITIONS verdict as a labeled top-level element, accompanied by at
  least one sentence of rationale citing a specific finding by ID or description.

---

## Recommended Criteria

*Output is better with these. Each adds material value.*

### C-06 -- Cross-Stage Coherence
- **Category**: depth
- **Weight**: recommended
- **Text**: When multiple stages run, later stages reference or escalate findings
  from earlier stages. The escalation chain (teams -> pm -> tpm) is visible: a
  teams finding becomes a pm alignment item, which becomes a tpm risk. Later stages
  do not ignore what earlier stages found.
- **Pass condition**: At least 2 cross-stage references in any multi-stage run
  (e.g., "teams raised X; pm confirms X is unresolved; tpm registers X as risk
  R-02"). Each reference names the upstream stage and finding.

---

### C-07 -- Structured Risk Register in TPM Stage
- **Category**: depth
- **Weight**: recommended
- **Text**: The tpm stage produces a structured risk register, not a prose list.
  Each entry has a title, severity, likelihood, and mitigation. The register is
  machine-scannable and forms the primary input for the go/no-go verdict.
- **Pass condition**: tpm stage includes a risk register table or structured list
  with >= 3 entries, each containing: title, severity, likelihood, and mitigation.
  At least one risk is rated HIGH. A prose narrative does not satisfy this criterion.

---

### C-08 -- Exec-Office Cascade Tracing
- **Category**: coverage
- **Weight**: recommended
- **Text**: When the exec-office stage runs (including via --stage all), output
  traces how S-office missions cascade down to the artifact or topic under review.
  At least one mission-to-artifact link is explicit: mission -> program -> artifact
  alignment or gap is named.
- **Pass condition**: exec-office stage output names at least one S-office mission
  (or exec-office strategic objective) by name and traces its alignment or
  misalignment to the artifact under review with a specific example. Abstract
  references to "strategic goals" do not satisfy this criterion.

---

## Aspirational Criteria

*Raise the bar once essential and recommended are stable.*

### C-09 -- Inter-Stage Blocker Detection
- **Category**: depth
- **Weight**: aspirational
- **Text**: Output explicitly identifies when a finding from one stage creates a
  hard blocker for a downstream stage. Blockers are surfaced proactively, not
  discovered retroactively. The blocking finding, the upstream stage, and the
  downstream stage impact are all named.
- **Pass condition**: At least 1 inter-stage blocker is named in a multi-stage run,
  with the upstream stage, the blocking finding ID (or description), and the
  downstream stage impact stated explicitly (e.g., "teams finding F-03 blocks tpm
  go/no-go: ownership unresolved before risk can be rated").

---

### C-10 -- Cross-Cutting Theme Elevation
- **Category**: depth
- **Weight**: aspirational
- **Text**: When the same concern surfaces in 2 or more stages, output recognizes
  the pattern and elevates it as a cross-cutting theme above the individual stage
  findings. Cross-cutting themes receive priority weighting and are visible at the
  document level, not buried inside a single stage.
- **Pass condition**: At least 1 cross-cutting theme is named at the document level
  (e.g., in a Synthesis or Themes section), citing the 2+ stages that surfaced it
  and explaining why repetition increases severity. The theme must be distinct from
  the individual stage findings -- a copy of a finding from one stage does not
  satisfy this criterion.

---

## Criterion Summary

| ID   | Text (short)                           | Weight        | Category    |
|------|----------------------------------------|---------------|-------------|
| C-01 | Stage identity and labeling            | essential     | format      |
| C-02 | Role-loaded perspective                | essential     | correctness |
| C-03 | ROB document format compliance         | essential     | format      |
| C-04 | Actionable findings (2x per stage)     | essential     | depth       |
| C-05 | Explicit go/no-go in tpm stage         | essential     | correctness |
| C-06 | Cross-stage coherence                  | recommended   | depth       |
| C-07 | Structured risk register in tpm        | recommended   | depth       |
| C-08 | Exec-office cascade tracing            | recommended   | coverage    |
| C-09 | Inter-stage blocker detection          | aspirational  | depth       |
| C-10 | Cross-cutting theme elevation          | aspirational  | depth       |

---

## Example Score Calculations

**Minimal golden** -- all 5 essential pass, 1/3 recommended pass, 0/2 aspirational:

```
composite = (5/5 * 60) + (1/3 * 30) + (0/2 * 10)
          = 60 + 10 + 0
          = 70
```

Not golden (composite < 80). Need 2/3 recommended to reach threshold.

---

**Baseline golden** -- all 5 essential pass, 2/3 recommended pass, 0/2 aspirational:

```
composite = (5/5 * 60) + (2/3 * 30) + (0/2 * 10)
          = 60 + 20 + 0
          = 80
```

Golden threshold met (all essential pass, composite = 80).

---

**Strong** -- all 5 essential pass (++), 3/3 recommended pass (++), 1/2 aspirational:

```
composite = 60 + 30 + 5
          = 95
```

---

**Perfect** -- all essential ++, all recommended ++, all aspirational ++:

```
composite = 60 + 30 + 10 = 100
```
