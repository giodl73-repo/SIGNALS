**corps-rob rubric v2 written** to `simulations/quest/rubrics/corps-rob-rubric-v2-2026-03-16.md`.

**Three new aspirational criteria extracted from R1:**

| ID | Signal | Source |
|----|--------|--------|
| C-11 | Conditional verdict itemization | V-04 TPM — conditions cited by finding/risk ID, not buried in prose rationale |
| C-12 | Finding severity discrimination | V-05 — "severity must vary" producing real triage, not uniform inflation |
| C-13 | Risk register status lifecycle | V-02 — Status column (OPEN/WATCH/MITIGATED) making the register a living artifact |

**Scoring impact:**

- Aspirational pool: 2 criteria × 5 pts → 5 criteria × 5 pts
- Max composite: 100 → 115
- Golden threshold unchanged (80 absolute) — baseline golden still requires all essential + 2/3 recommended

The C-02 partial pattern (role lens in header vs inside finding cell) was *not* added as a new criterion — it's already the C-02 pass condition; V-02 and V-04's failures there are an enforcement signal for the *skill*, not a gap in the rubric.
eadership`, `## Stage: tpm`).
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

### C-11 -- Conditional Verdict Itemization
- **Category**: depth
- **Weight**: aspirational
- **Source**: R1 V-04 -- tpm go/no-go with conditions cited by finding/risk ID
  rather than embedded in rationale prose.
- **Text**: When any stage verdict is conditional (APPROVED WITH CONDITIONS /
  GO WITH CONDITIONS or equivalent), the conditions are enumerated as discrete
  numbered items, each with an explicit owner and a resolution path. A conditional
  verdict that states conditions only as prose rationale does not satisfy this
  criterion.
- **Pass condition**: At least one conditional verdict in the run lists its
  conditions as >= 2 numbered or bulleted items. Each item names: (1) what must
  happen, (2) who owns it, and (3) a reference to the finding or risk driving the
  condition (by ID or description). Prose rationale alone does not qualify.

---

### C-12 -- Finding Severity Discrimination
- **Category**: depth
- **Weight**: aspirational
- **Source**: R1 V-05 -- "severity must vary" instruction producing real triage
  rather than uniform risk inflation.
- **Text**: Across all findings in a run, severity labels demonstrate real
  discrimination -- not uniform inflation or deflation. A run where every finding
  carries the same severity rating indicates insufficient triage regardless of
  finding count.
- **Pass condition**: Across all findings in the run, at least one finding is rated
  HIGH and at least one finding is rated below HIGH (MED or LOW or equivalent). A
  run that assigns all findings to the same severity tier fails this criterion, even
  if finding count and format are otherwise correct.

---

### C-13 -- Risk Register Status Lifecycle
- **Category**: coverage
- **Weight**: aspirational
- **Source**: R1 V-02 -- risk register table with Status column (OPEN / WATCH /
  MITIGATED) making the register usable as a living artifact beyond the initial run.
- **Text**: The structured risk register produced by the tpm stage (C-07) includes
  a Status column tracking each risk's resolution state. Status makes the register
  useful beyond the initial ROB session -- a reviewer can re-open the artifact and
  see what has been mitigated since the last run.
- **Pass condition**: The risk register table or structured list includes a Status
  field for each entry with a value from a defined vocabulary (OPEN / WATCH /
  MITIGATED or equivalent three-state model). A register without status fields does
  not satisfy this criterion.

---

## Criterion Summary

| ID   | Text (short)                           | Weight        | Category    | Added |
|------|----------------------------------------|---------------|-------------|-------|
| C-01 | Stage identity and labeling            | essential     | format      | v1    |
| C-02 | Role-loaded perspective                | essential     | correctness | v1    |
| C-03 | ROB document format compliance         | essential     | format      | v1    |
| C-04 | Actionable findings (2x per stage)     | essential     | depth       | v1    |
| C-05 | Explicit go/no-go in tpm stage         | essential     | correctness | v1    |
| C-06 | Cross-stage coherence                  | recommended   | depth       | v1    |
| C-07 | Structured risk register in tpm        | recommended   | depth       | v1    |
| C-08 | Exec-office cascade tracing            | recommended   | coverage    | v1    |
| C-09 | Inter-stage blocker detection          | aspirational  | depth       | v1    |
| C-10 | Cross-cutting theme elevation          | aspirational  | depth       | v1    |
| C-11 | Conditional verdict itemization        | aspirational  | depth       | v2    |
| C-12 | Finding severity discrimination        | aspirational  | depth       | v2    |
| C-13 | Risk register status lifecycle         | aspirational  | coverage    | v2    |

---

## Example Score Calculations

**Minimal pass (not golden)** -- all 5 essential pass, 1/3 recommended, 0/5 aspirational:

```
composite = (5/5 * 60) + (1/3 * 30) + (0/5 * 25)
          = 60 + 10 + 0
          = 70
```

Not golden (composite < 80). Need 2/3 recommended to reach threshold.

---

**Baseline golden** -- all 5 essential pass, 2/3 recommended, 0/5 aspirational:

```
composite = (5/5 * 60) + (2/3 * 30) + (0/5 * 25)
          = 60 + 20 + 0
          = 80
```

Golden threshold met (all essential pass, composite = 80).

---

**Strong** -- all 5 essential pass, 3/3 recommended, 2/5 aspirational:

```
composite = 60 + 30 + 10
          = 100
```

---

**Perfect** -- all essential, all recommended, all aspirational:

```
composite = 60 + 30 + 25 = 115
```

---

## Version History

| Version | Date       | Change |
|---------|------------|--------|
| v1      | 2026-03-16 | Initial -- 5 essential, 3 recommended, 2 aspirational (max 100) |
| v2      | 2026-03-16 | R1 signals -- added C-11 conditional verdict itemization, C-12 finding severity discrimination, C-13 risk register status lifecycle (max 115) |
