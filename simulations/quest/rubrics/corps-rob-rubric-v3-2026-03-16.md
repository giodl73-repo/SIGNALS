**corps-rob rubric v3** written to `simulations/quest/rubrics/corps-rob-rubric-v3-2026-03-16.md`.

---

**Two new aspirational criteria extracted from R2:**

| ID | Signal | Source |
|----|--------|--------|
| C-14 | Pre-finding severity calibration | V-01 — silent triage step deciding full severity distribution holistically before writing any finding; Triage Note when all findings land at the same level |
| C-15 | Risk register update protocol | V-03 — Update Protocol section specifying trigger events, owner role, and revisit cadence; makes the register a process artifact, not a snapshot |

**Distinction from existing criteria:**

- C-14 vs C-12: C-12 checks the *outcome* (severity varies). C-14 checks for evidence of *process* (pre-calibration or justified uniformity). A variation can fail C-14 while passing C-12 if severity varies by accident, and can pass C-14 while technically failing C-12 if all findings are genuinely HIGH with a documented rationale.
- C-15 vs C-13: C-13 checks for a Status column. C-15 requires an Update Protocol section that answers when/who/how-often. C-15 gates on C-13 passing — no protocol without the column.

**Scoring impact:**

| | v2 | v3 |
|--|----|----|
| Aspirational pool | 5 criteria × 5 pts = 25 | 7 criteria × 5 pts = 35 |
| Max composite | 115 | 125 |
| Golden threshold | 80 (unchanged) | 80 (unchanged) |
ve of the role loaded from
  .roles/ -- not a generic review. The role orientation, lens, and expertise
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

### C-14 -- Pre-Finding Severity Calibration
- **Category**: depth
- **Weight**: aspirational
- **Source**: R2 V-01 -- silent triage calibration step that decides the full
  severity distribution holistically before any finding is written, preventing
  per-finding inflation. Triage Note required when all findings land at the same
  level.
- **Text**: Before writing findings, output demonstrates that severity distribution
  was decided holistically -- the most critical concern in the stage is assigned
  HIGH, the least critical is assigned LOW, and the spread reflects the actual risk
  landscape rather than per-finding inflation. When all findings in a stage share
  the same severity level, output includes a Triage Note explaining why the
  distribution is genuinely uniform rather than an artifact of uncalibrated rating.
- **Pass condition**: Evidence of holistic calibration in at least one stage: either
  an explicit calibration statement, a demonstrated HIGH-to-LOW spread across
  findings, or a Triage Note when severity is uniform. A stage where every finding
  is HIGH with no justification fails this criterion. A stage with a documented
  rationale for uniform severity (e.g., "all three findings are HIGH due to timeline
  compression with no recovery path") satisfies it.

---

### C-15 -- Risk Register Update Protocol
- **Category**: coverage
- **Weight**: aspirational
- **Source**: R2 V-03 -- Update Protocol section on the risk register specifying
  when and how to update status values post-session, transforming the register from
  a snapshot into a process artifact.
- **Text**: The tpm stage risk register (C-07) includes not only status fields
  (C-13) but also an explicit Update Protocol: guidance on what events trigger a
  status change, who owns each update, and how frequently the register should be
  revisited. Without an update protocol, a status column is a snapshot; with one,
  the register becomes a living artifact that survives the ROB session.
- **Pass condition**: Risk register output includes a dedicated Update Protocol
  section or block that specifies: (1) what events or milestones trigger a status
  change for a risk entry, (2) the owner responsible for status updates (by role,
  not by name), and (3) a revisit cadence or trigger condition. A register with a
  Status column but no update guidance does not satisfy this criterion -- C-13 must
  also pass for C-15 to be scoreable.

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
| C-14 | Pre-finding severity calibration       | aspirational  | depth       | v3    |
| C-15 | Risk register update protocol          | aspirational  | coverage    | v3    |

---

## Example Score Calculations

**Minimal pass (not golden)** -- all 5 essential pass, 1/3 recommended, 0/7 aspirational:

```
composite = (5/5 * 60) + (1/3 * 30) + (0/7 * 35)
          = 60 + 10 + 0
          = 70
```

Not golden (composite < 80). Need 2/3 recommended to reach threshold.

---

**Baseline golden** -- all 5 essential pass, 2/3 recommended, 0/7 aspirational:

```
composite = (5/5 * 60) + (2/3 * 30) + (0/7 * 35)
          = 60 + 20 + 0
          = 80
```

Golden threshold met (all essential pass, composite = 80).

---

**Strong** -- all 5 essential pass, 3/3 recommended, 2/7 aspirational:

```
composite = 60 + 30 + (2/7 * 35)
          = 60 + 30 + 10
          = 100
```

---

**R2 V-01 equivalent** -- all essential, 2/3 recommended, 1/7 aspirational (C-12):

```
composite = 60 + 20 + (1/7 * 35)
          = 60 + 20 + 5
          = 85
```

---

**R2 V-02 equivalent** -- all essential, 2/3 recommended, 1.5/7 aspirational (C-11 PASS + C-12 PARTIAL):

```
composite = 60 + 20 + (1.5/7 * 35)
          = 60 + 20 + 7.5
          = 87.5
```

---

**Perfect** -- all essential, all recommended, all aspirational:

```
composite = 60 + 30 + 35 = 125
```

---

## Version History

| Version | Date       | Change |
|---------|------------|--------|
| v1      | 2026-03-16 | Initial -- 5 essential, 3 recommended, 2 aspirational (max 100) |
| v2      | 2026-03-16 | R1 signals -- added C-11 conditional verdict itemization, C-12 finding severity discrimination, C-13 risk register status lifecycle (max 115) |
| v3      | 2026-03-16 | R2 signals -- added C-14 pre-finding severity calibration, C-15 risk register update protocol (max 125) |
