Written to `simulations/quest/rubrics/corps-rob-rubric-v5-2026-03-16.md`.

---

**Three new criteria extracted from R4:**

| ID | Signal | Source |
|----|--------|--------|
| C-19 | Zero-deviation explicit declaration | V-02 "VIOLATIONS: NONE required even for clean runs" + V-03 "TRIAGE NOTE GAPS: NONE even for clean runs" — both independently converged on the same pattern |
| C-20 | Enforcement audit structured table | V-02 Full Enforcement Audit table (Stage / Pre-Commitment / Declared / Honored / Deviation) — tabular format vs. prose |
| C-21 | Named triage field vocabulary | V-03 HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR named fields — labeled structure makes calibration machine-scannable and cross-run comparable |

**Distinctions from existing criteria:**

- C-19 vs C-17: C-17 requires flagging non-zero violations. C-19 requires an affirmative "VIOLATIONS: NONE" declaration on clean runs. A run can flag violations correctly (C-17 pass) without ever saying "none" on clean sections (C-19 fail).
- C-20 vs C-17: C-17 requires a labeled enforcement section. C-20 requires it to be a named-column table. Prose audit passes C-17; only tabular passes C-20.
- C-21 vs C-18: C-18 requires the three Triage Note content elements. C-21 requires those elements to be printed as named field labels. Prose covering all three passes C-18; only labeled fields pass C-21.

**Scoring impact:**

| | v4 | v5 |
|--|----|----|
| Aspirational pool | 10 criteria x 5 pts = 50 | 13 criteria x 5 pts = 65 |
| Max composite | 140 | 155 |
| Golden threshold | 80 (unchanged) | 80 (unchanged) |

**Retroactive R4 scores under v5:**

- V-01: 100 (unchanged — C-19/20/21 not present)
- V-02: 115 (gains C-19 + C-20, was 105)
- V-03: 110 (gains C-19 + C-21, was 100)
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

### C-16 -- Role-Lens Pre-Declaration
- **Category**: depth
- **Weight**: aspirational
- **Source**: R3 V-01 -- ROLE LENS field in the Calibration Block; before any
  finding is written, the role's specific fear or primary concern about this topic
  is articulated as a printed artifact. A loaded role file contains general lens
  orientation; this criterion requires a topic-specific instantiation of that lens
  before findings begin.
- **Text**: Before writing findings in a stage, output includes an explicit
  declaration of what the loaded role most fears or is most concerned about in the
  context of this specific topic. The declaration is a named field or labeled block
  -- it is not inferred from the findings after the fact. Generic role descriptions
  ("a PM cares about alignment") do not satisfy this criterion; the declaration must
  be specific to the artifact or topic under review.
- **Distinction from C-02**: C-02 checks that findings reflect the role's
  perspective. C-16 checks for a printed pre-finding declaration of the role's
  topic-specific concern. A variation can pass C-02 (findings happen to reflect the
  role) without passing C-16 (no upfront declaration). A variation can pass C-16
  even if the subsequent findings are weak.
- **Pass condition**: At least one stage in the run includes a labeled pre-finding
  field naming what the loaded role most fears about this specific topic (e.g.,
  ROLE LENS:, ROLE CONCERN:, or equivalent). The field content is topic-specific
  (references the artifact, domain, or risk area under review) and appears before
  the first finding in that stage.

---

### C-17 -- Pre-Commitment Enforcement Audit
- **Category**: depth
- **Weight**: aspirational
- **Source**: R3 V-01 (CALIBRATION ENFORCEMENT appendix) and R3 V-02 (UPDATE
  PROTOCOL ENFORCEMENT appendix) -- a post-run section that audits whether
  pre-commitment artifacts (calibration spread declarations, update protocol
  columns) were actually honored in the output. Makes pre-commitments falsifiable
  by closing the loop between declared intent and delivered output.
- **Text**: Output includes a post-run enforcement section that audits at least one
  pre-commitment artifact declared earlier in the run -- a calibration spread, an
  update protocol, a role lens declaration, or equivalent. The audit names the
  pre-commitment, checks whether the output honored it, and flags any stage or entry
  where the commitment was not met. A run that declares pre-commitments but never
  audits them does not satisfy this criterion.
- **Distinction from C-14 and C-15**: C-14 requires calibration pre-commitment.
  C-15 requires update protocol. C-17 requires a post-run audit that verifies those
  commitments were kept -- a meta-artifact that makes the system self-checking.
  C-17 can be satisfied by auditing any single pre-commitment type.
- **Pass condition**: Output includes a labeled enforcement or audit section (e.g.,
  CALIBRATION ENFORCEMENT, UPDATE PROTOCOL ENFORCEMENT, or equivalent) that: (1)
  names the pre-commitment being audited, (2) checks each stage or register entry
  against that commitment, and (3) explicitly flags any instance where the
  pre-commitment was not honored. The audit section must appear after the findings
  it audits. A pre-commitment with no audit does not satisfy this criterion.

---

### C-18 -- Universal Per-Stage Triage Note
- **Category**: depth
- **Weight**: aspirational
- **Source**: R3 V-03 -- mandatory Triage Note in every stage regardless of
  severity distribution; documents the calibration decision even when severity
  varies, creating a full per-stage audit trail of triage reasoning rather than
  requiring notes only for the edge case of uniform severity.
- **Text**: Every stage in the run includes a Triage Note documenting the
  calibration decision: which concern drove the HIGH assignment, which concern was
  demoted to LOW, and what shaped the severity distribution. The note is present
  regardless of whether findings have a spread or are uniform -- the absence of a
  note in a stage with varied severity is the same gap as in a stage with uniform
  severity.
- **Distinction from C-14**: C-14 requires evidence of holistic calibration and
  mandates a Triage Note only when severity is uniform. C-18 requires a Triage Note
  in every stage unconditionally -- it creates a complete record of calibration
  decisions rather than requiring documentation only of the degenerate case. A
  variation can pass C-14 (no note needed because severity varies) while failing
  C-18 (note required even when severity varies).
- **Pass condition**: Every stage run includes a labeled Triage Note (or equivalent
  calibration log field) that states: (1) which concern was ranked most critical
  (-> HIGH), (2) which concern was ranked least critical (-> LOW or MED), and (3)
  what factor drove the distribution decision (e.g., "scope of blast radius",
  "reversibility", "timeline compression"). A run where any stage lacks a Triage
  Note fails this criterion, even if severity varies appropriately in that stage.

---

### C-19 -- Zero-Deviation Explicit Declaration
- **Category**: depth
- **Weight**: aspirational
- **Source**: R4 V-02 (VIOLATIONS: NONE required even for clean runs in the
  Enforcement Audit table) and R4 V-03 (TRIAGE NOTE GAPS: NONE required even for
  clean runs in the Triage Note Enforcement section) -- both variations independently
  converged on the same pattern: an audit that finds nothing must say so explicitly
  rather than staying silent.
- **Text**: Any audit, enforcement, or gap-check section in the output must include
  an explicit zero-deviation statement when no violations or gaps exist. The absence
  of violations must be declared, not implied by silence. This distinguishes a
  system that checked and found nothing from one that did not check at all. A
  section that ends after listing entries without a zero-state confirmation leaves
  ambiguity about whether the check was performed.
- **Distinction from C-17**: C-17 requires the enforcement audit to flag instances
  where a pre-commitment was not honored. C-19 requires an affirmative zero-state
  declaration when no violations exist -- "VIOLATIONS: NONE", "GAPS: NONE", or
  equivalent. A run can satisfy C-17 (correctly flags a real violation) without
  satisfying C-19 (no explicit zero-state on a clean-run enforcement section).
  C-17 must also pass for C-19 to be scoreable against the enforcement audit.
- **Pass condition**: Each audit, enforcement, or gap-check section in the run that
  finds no deviations includes an explicit labeled zero-state line (e.g.,
  "VIOLATIONS: NONE", "GAPS: NONE", "TRIAGE NOTE GAPS: NONE", or equivalent). A
  section that simply ends without a zero-state line after confirming clean status
  does not satisfy this criterion. If the section finds real violations, C-19 is
  not applicable for that section -- it applies only to sections reporting a clean
  result.

---

### C-20 -- Enforcement Audit Structured Table Format
- **Category**: format
- **Weight**: aspirational
- **Source**: R4 V-02 -- Full Enforcement Audit table with named columns (Stage /
  Pre-Commitment / Declared / Honored / Deviation), each stage getting a row, the
  table machine-scannable per pre-commitment type. A prose narrative covering the
  same content does not produce the same scannability or cross-run comparability.
- **Text**: When a pre-commitment enforcement audit (C-17) is present, the audit
  section uses a named-column table rather than prose. Each column serves a distinct
  function: the stage or scope, the pre-commitment that was declared, what was
  actually delivered, whether the commitment was honored, and any deviation. A prose
  audit that covers the same ground is not machine-scannable across stages and does
  not produce a reusable artifact structure.
- **Distinction from C-17**: C-17 requires the enforcement audit to exist as a
  labeled section with three functional requirements. C-20 requires the audit to use
  a structured table with named columns. A prose enforcement audit can satisfy C-17;
  only a tabular one satisfies C-20. C-17 must also pass for C-20 to be scoreable.
- **Pass condition**: The enforcement audit section uses a table (or equivalent
  structured list) with >= 4 named columns covering: (1) stage or scope, (2) the
  pre-commitment declared, (3) whether it was honored, and (4) any deviation. Prose
  narrative does not qualify. A table with unnamed or unlabeled columns does not
  satisfy this criterion.

---

### C-21 -- Named Triage Field Vocabulary
- **Category**: format
- **Weight**: aspirational
- **Source**: R4 V-03 -- Triage Note uses three explicitly named fields (HIGH
  DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR), creating a reusable calibration
  vocabulary that is machine-scannable and comparable across sessions and runs.
  Prose Triage Notes covering the same content are not cross-run comparable.
- **Text**: Triage Notes use a consistent named-field vocabulary for calibration
  decisions: a labeled field for the factor that drove the highest severity
  assignment, a labeled field for the factor that anchored the lowest severity
  assignment, and a labeled field for the contextual factor that shaped the overall
  distribution. Named fields make triage decisions scannable, reusable, and
  comparable across sessions without re-reading prose.
- **Distinction from C-18**: C-18 requires a Triage Note in every stage containing
  three content elements (HIGH driver, LOW anchor, distribution factor). C-21
  requires those elements to use named field labels. A Triage Note in prose that
  covers all three elements passes C-18 but not C-21. Only a Triage Note with
  labeled fields (e.g., HIGH DRIVER:, LOW ANCHOR:, DISTRIBUTION FACTOR: or
  equivalent named vocabulary) satisfies C-21. C-18 must also pass for C-21 to be
  scoreable.
- **Pass condition**: At least one Triage Note in the run uses named field labels
  for: (1) the driver of the HIGH severity assignment, (2) the anchor for the LOW
  severity assignment, and (3) the factor that shaped the overall severity
  distribution. The labels must be explicit field names printed before each content
  element -- prose sentences that contain the same information without field labels
  do not satisfy this criterion.

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
| C-16 | Role-lens pre-declaration              | aspirational  | depth       | v4    |
| C-17 | Pre-commitment enforcement audit       | aspirational  | depth       | v4    |
| C-18 | Universal per-stage triage note        | aspirational  | depth       | v4    |
| C-19 | Zero-deviation explicit declaration    | aspirational  | depth       | v5    |
| C-20 | Enforcement audit structured table     | aspirational  | format      | v5    |
| C-21 | Named triage field vocabulary          | aspirational  | format      | v5    |

---

## Scoring Impact

| | v4 | v5 |
|--|----|----|
| Aspirational pool | 10 criteria x 5 pts = 50 | 13 criteria x 5 pts = 65 |
| Max composite | 140 | 155 |
| Golden threshold | 80 (unchanged) | 80 (unchanged) |

---

## Example Score Calculations

**Minimal pass (not golden)** -- all 5 essential pass, 1/3 recommended, 0/13 aspirational:

```
composite = (5/5 * 60) + (1/3 * 30) + (0 * 5)
          = 60 + 10 + 0
          = 70
```

Not golden (composite < 80). Need 2/3 recommended to reach threshold.

---

**Baseline golden** -- all 5 essential pass, 2/3 recommended, 0/13 aspirational:

```
composite = (5/5 * 60) + (2/3 * 30) + (0 * 5)
          = 60 + 20 + 0
          = 80
```

Golden threshold met (all essential pass, composite = 80).

---

**Strong** -- all 5 essential pass, 3/3 recommended, 2/13 aspirational:

```
composite = 60 + 30 + (2 * 5)
          = 60 + 30 + 10
          = 100
```

---

**R4 V-01 equivalent** -- all essential, 2/3 recommended, 4/13 aspirational (C-12, C-13, C-14, C-16):

```
composite = 60 + 20 + (4 * 5)
          = 60 + 20 + 20
          = 100
```

---

**R4 V-02 equivalent** -- all essential, 2/3 recommended, 7/13 aspirational (C-12, C-13, C-14, C-15, C-17, C-19, C-20):

```
composite = 60 + 20 + (7 * 5)
          = 60 + 20 + 35
          = 115
```

---

**R4 V-03 equivalent** -- all essential, 2/3 recommended, 6/13 aspirational (C-12, C-13, C-14, C-18, C-19, C-21):

```
composite = 60 + 20 + (6 * 5)
          = 60 + 20 + 30
          = 110
```

---

**Perfect** -- all essential, all recommended, all aspirational:

```
composite = 60 + 30 + 65 = 155
```

---

## Version History

| Version | Date       | Change |
|---------|------------|--------|
| v1      | 2026-03-16 | Initial -- 5 essential, 3 recommended, 2 aspirational (max 100) |
| v2      | 2026-03-16 | R1 signals -- added C-11 conditional verdict itemization, C-12 finding severity discrimination, C-13 risk register status lifecycle (max 115) |
| v3      | 2026-03-16 | R2 signals -- added C-14 pre-finding severity calibration, C-15 risk register update protocol (max 125) |
| v4      | 2026-03-16 | R3 signals -- added C-16 role-lens pre-declaration, C-17 pre-commitment enforcement audit, C-18 universal per-stage triage note (max 140) |
| v5      | 2026-03-16 | R4 signals -- added C-19 zero-deviation explicit declaration, C-20 enforcement audit structured table, C-21 named triage field vocabulary (max 155) |
