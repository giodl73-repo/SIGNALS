# corps-rob rubric v15

**v15 summary: 2 new criteria from R14 excellence signals**

| ID | Criterion | Signal | Dependency |
|----|-----------|--------|------------|
| C-45 | Exclusivity Declaration Protected-Count Annotation | R14's universal C-43 pass shows all variations enumerate both C-30 and C-34 with label+description pairs -- the next distinguishing form explicitly states the count of protected criteria ("exactly 2 criteria require glossary scope"), making the enumeration count-verifiable and flagging silent additions when new glossary-scope criteria are introduced | C-43 |
| C-46 | RULE AUDIT-TABLE Bidirectional Condition Enumeration | R14's universal C-44 pass shows all variations declare AUDIT RESULT block independence -- the next distinguishing form enumerates both branches explicitly as numbered conditions: (1) when table is present: AUDIT RESULT block preserved beneath it; (2) when table is absent: AUDIT RESULT block still required -- making independence a complete conditional coverage rather than a single unconditional mandate | C-44 |

**Scoring impact:**

| | v14 | v15 |
|--|-----|-----|
| Aspirational pool | 36 x 5 = 180 | 38 x 5 = 190 |
| Max composite | 270 | 280 |
| Golden threshold | 80 (unchanged) | 80 (unchanged) |

**Retroactive R14 under v15:**
- C-45 not scoreable: R14 universal C-43 pass provides label+description pairs but no count annotation
- C-46 not scoreable: R14 universal C-44 pass provides unconditional mandate language but no explicit two-branch enumeration

**C-45 -- Exclusivity Declaration Protected-Count Annotation** (format / aspirational)
- Signal: R14 Signal 1 -- Universal C-43 pass across all R14 variations produces identical glossary preambles enumerating C-30 (Run-Level Preamble Schema with Named Post-Stage Reference) and C-34 (Conditional Item vs Condition Enum Disambiguation) as full label+description pairs. C-43 requires each enumerated criterion to use the paired form; it does not require the declaration to state how many criteria are enumerated. A glossary that enumerates "C-30 (...) and C-34 (...)" satisfies C-43 regardless of whether the count is stated. The absence of a count leaves a gap: a generator adding a third glossary-scope criterion could inline the first two by name while treating the third as satisfiable inline, without any declared count to trigger revision. An explicit count annotation -- "exactly 2 criteria require glossary scope: C-30 (...) and C-34 (...)" -- closes this gap. The count is auditable independently of the enumeration: a reader can verify the count without re-reading the full list, and a change in the set of protected criteria requires a count update, making silent additions structurally detectable.
- Distinction from C-43: C-43 requires each enumerated criterion to be expressed as a label-plus-description pair. C-45 requires the declaration to additionally state the count of protected criteria explicitly before or alongside the enumeration. A declaration with full label+description pairing satisfies C-43 but not C-45 without the count annotation. Only a declaration that states "exactly N criteria..." (or equivalent count-fixing language) alongside the labeled pairs satisfies C-45. C-43 must pass for C-45 to be scoreable.

**C-46 -- RULE AUDIT-TABLE Bidirectional Condition Enumeration** (format / aspirational)
- Signal: R14 Signal 2 -- Universal C-44 pass across all R14 variations produces RULE AUDIT-TABLE declarations with unconditional mandate language ("mandatory regardless of table presence"). C-44 requires the independence declaration to state the AUDIT RESULT block is required whether or not the table is present -- a single unconditional statement satisfies C-44. V-02's R13 signal text states: "preserved BENEATH the table and is mandatory regardless of table presence." This is a combined additive+independence statement but still expressed as a single continuous clause. The next distinguishing form enumerates both conditional branches as separate numbered items: (1) when table is present: AUDIT RESULT block is preserved beneath it; (2) when table is absent: AUDIT RESULT block is still required. Enumerated branches make the coverage complete in a verifiable way: a reader can confirm both halves are stated without parsing a combined clause. A generator producing the section can check each branch independently. A single unconditional statement satisfies C-44; only explicit enumeration of both branches satisfies C-46.
- Distinction from C-44: C-44 requires RULE AUDIT-TABLE to include a printed statement declaring the AUDIT RESULT block as mandatory regardless of table presence -- unconditional language. C-46 requires that independence to be stated as two enumerated conditional branches: the present-table case (AUDIT RESULT block preserved beneath) and the absent-table case (AUDIT RESULT block still required). A single "mandatory regardless" statement satisfies C-44 but not C-46. Only a rule with both branches enumerated as distinct numbered items satisfies C-46. C-44 must pass for C-46 to be scoreable.

**Dependencies:**
- C-45 requires C-43 to pass.
- C-46 requires C-44 to pass.

**Persistent gap for R15:** C-45 requires an explicit count annotation not present in R14's universal C-43 pass. C-46 requires enumerated bidirectional branches not present in R14's universal C-44 pass. C-39 (IB-02 Urgency Gradient Cascade) remains universally unsatisfied. Ideal R15 adds a count annotation to the glossary exclusivity declaration (C-45), enumerates both branches in RULE AUDIT-TABLE (C-46), and makes a first C-39 attempt, targeting 275/280 (98.2%).

---

**v14 summary: 2 new criteria from R13 excellence signals**

| ID | Criterion | Signal | Dependency |
|----|-----------|--------|------------|
| C-43 | Criterion Enumeration Label-Plus-Description Pairing | V-01's C-42 pass enumerates each protected criterion with both its ID label and a parenthetical functional description ("C-30 (Run-Level Preamble Schema with Named Post-Stage Reference)" and "C-34 (Conditional Item vs Condition Enum Disambiguation)") -- C-42 requires label or description; C-43 requires both simultaneously, making each enumeration entry self-contained without rubric lookup | C-42 |
| C-44 | AUDIT RESULT Block Independence Declaration | V-02's C-35 pass adds "mandatory regardless of table presence" to the additive constraint -- C-35 requires the table to be declared non-replacing; C-44 requires the AUDIT RESULT block to be declared independently mandatory (not conditionally required by the table's presence), establishing two-way artifact independence | C-35 |

**Scoring impact:**

| | v13 | v14 |
|--|-----|-----|
| Aspirational pool | 34 x 5 = 170 | 36 x 5 = 180 |
| Max composite | 260 | 270 |
| Golden threshold | 80 (unchanged) | 80 (unchanged) |

**Retroactive R13 under v14:**
- V-01: 250 (gains C-43 PASS: label+description pairing present; C-44 not scoreable: C-35 FAIL)
- V-02: 250 (gains C-44 PASS: "mandatory regardless of table presence" present; C-43 not scoreable: C-42 not scoreable since C-40 FAIL)

**C-43 -- Criterion Enumeration Label-Plus-Description Pairing** (format / aspirational)
- Signal: R13 Signal 1 -- V-01's C-42 pass enumerates protected criteria as "C-30 (Run-Level Preamble Schema with Named Post-Stage Reference)" and "C-34 (Conditional Item vs Condition Enum Disambiguation)". Each entry pairs the criterion ID label with a parenthetical functional description. C-42 requires the exclusivity enumeration to name each criterion by label or functional description -- either alone satisfies C-42. V-01's implementation provides both simultaneously: the ID anchors the criterion precisely; the parenthetical description communicates the criterion's function without requiring the reader to consult the rubric. A glossary whose enumeration uses labels alone (e.g., "C-30 and C-34") satisfies C-42 but not C-43 -- a generator can copy the labels without understanding the criteria they represent. A glossary whose enumeration provides functional descriptions alone satisfies C-42 but not C-43 -- the criterion ID is the stable reference that survives criterion renaming or rubric restructuring. Only an enumeration that provides both the label and a parenthetical functional description for each protected criterion satisfies C-43.
- Distinction from C-42: C-42 requires the glossary exclusivity declaration to enumerate specific protected criteria by label or functional description. C-43 requires those entries to include both: a criterion ID label and a parenthetical functional description that identifies the criterion's function without lookup. The distinction is between an enumeration that identifies (C-42) and one that is self-documenting (C-43). C-42 must pass for C-43 to be scoreable.

**C-44 -- AUDIT RESULT Block Independence Declaration** (format / aspirational)
- Signal: R13 Signal 2 -- V-02's C-35 pass includes "The AUDIT RESULT block with per-condition (a)/(b)/(c) enumeration is preserved BENEATH the table and is mandatory regardless of table presence." The phrase "mandatory regardless of table presence" is the key signal: it establishes that the AUDIT RESULT block's mandatory status is independent of the table's existence. C-35 requires the additive constraint (table inserted above, not replacing AUDIT RESULT block). V-02 goes further: it declares the AUDIT RESULT block would be required even if the table were absent -- the two artifacts are independently mandatory, not merely co-present with a defined ordering. Without the independence declaration, a reader could interpret the additive constraint as: "if you add the table, keep the AUDIT RESULT block." With it, the reading is unambiguous: "the AUDIT RESULT block is always mandatory; the table's presence or absence does not change that." A format spec that declares the additive constraint without the independence statement leaves open a conditional reading -- C-44 closes it.
- Distinction from C-35: C-35 requires RULE AUDIT-TABLE to declare the table is inserted above the AUDIT RESULT block and not replacing it, with explicit preservation of C-29's per-condition enumeration beneath the table. C-44 requires the declaration to additionally state that the AUDIT RESULT block is mandatory regardless of whether the table is present -- establishing independence rather than ordering. A rule that says "table inserted above; AUDIT RESULT block preserved beneath" satisfies C-35 but not C-44. Only a rule that additionally declares "AUDIT RESULT block is mandatory regardless of table presence" or equivalent independence language satisfies C-44. C-35 must pass for C-44 to be scoreable.

**Dependencies:**
- C-43 requires C-42 to pass.
- C-44 requires C-35 to pass.

**Persistent gap for R14:** No R13 variation combines C-43 and C-44. V-01 passes C-43 but fails C-35 (blocking C-44). V-02 passes C-44 but fails C-40 (blocking C-42 and C-43). C-39 (IB-02 Urgency Gradient Cascade) remains universally unsatisfied -- no variation declares the urgency cascade constraint. Ideal R14 combines V-01's full glossary stack (C-40 + C-42 + C-43), V-02's table stack (C-35 + C-41 + C-44), and a first attempt at C-39, targeting 265/270 (98.1%).

---

## Essential Criteria

*All five must pass. A run that fails any essential criterion does not reach golden regardless of composite score.*

### C-01 -- Stage Identity and Labeling
- **Category**: format
- **Weight**: essential
- **Text**: Every stage output begins with an unambiguous stage header that names
  the stage by its identifier (e.g., `## Stage: teams`, `## Stage: pm`,
  `## Stage: tpm`, `## Stage: leadership`, `## Stage: exec-office`). No stage
  is anonymous or identified only by position.
- **Pass condition**: Every stage run includes a labeled stage header matching
  the stage name. No stage is anonymous or identified only by position.

---

### C-02 -- Role-Loaded Perspective
- **Category**: correctness
- **Weight**: essential
- **Text**: Each stage review reflects the perspective of the role loaded from
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
- **Text**: Output conforms to the ROB document format: each stage section contains
  findings, a verdict or recommendation, and where applicable a TPM summary block.
  The structure is a document artifact, not a conversational response -- sections
  are labeled, findings are enumerated, and verdicts are distinct from findings.
- **Pass condition**: Each stage output contains: (1) at least one labeled finding
  block, (2) a verdict or recommendation (even tentative), and (3) for the tpm
  stage, a TPM-level summary. Conversational prose without structural sections does
  not satisfy this criterion.

---

### C-04 -- Actionable Findings (2x per stage)
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

### C-22 -- Post-Stage Role-Concern Gap Scan
- **Category**: coverage
- **Weight**: aspirational
- **Source**: R5 V-01 -- "Role Concern Gaps" post-stage section that scans all
  stages to verify C-16 (role-lens pre-declaration) compliance and names any stage
  where the pre-declaration was absent. A run where all stages contain declarations
  applies RULE ZERO-STATE: "ROLE CONCERN GAPS: NONE". Makes C-16 compliance
  falsifiable at the document level rather than requiring per-stage inspection.
- **Text**: Output includes a dedicated post-stage section that audits whether
  every stage produced a role-concern pre-declaration (C-16). The section names any
  stage where the declaration was missing. When no stages are missing, the section
  carries an explicit zero-state declaration. The audit is a document-level artifact
  that aggregates per-stage compliance into a single scannable result -- it does not
  replace per-stage declarations but makes the completeness check visible.
- **Distinction from C-16**: C-16 requires the role-concern pre-declaration within
  each stage. C-22 requires a post-stage audit that verifies C-16 compliance across
  all stages and surfaces gaps. A run where every stage contains the declaration
  passes C-16 but can still fail C-22 (no gap scan exists). A run can have C-22
  present (gap scan exists) even when C-16 fails some stages -- C-22 makes the
  failure explicit rather than invisible. C-16 does not need to pass for C-22 to be
  scoreable.
- **Pass condition**: Output includes a labeled post-stage section (e.g., ROLE
  CONCERN GAPS, ROLE LENS AUDIT, or equivalent) that: (1) names each stage that
  lacked a role-concern pre-declaration, or (2) includes an explicit zero-state
  declaration (e.g., "ROLE CONCERN GAPS: NONE") if all stages complied. The section
  must appear after all stage findings. An implicit absence of gap discussion does
  not satisfy this criterion.

---

### C-23 -- Post-Stage Triage Note Gap Scan
- **Category**: coverage
- **Weight**: aspirational
- **Source**: R5 V-01 ("Triage Note Gaps" post-stage section) and R5 V-03
  ("Triage Note Gaps" post-stage section) -- both variations independently included
  a dedicated post-stage audit for C-18 (universal triage note) compliance. The
  convergence across two independent primary-axis variations is a strong signal.
- **Text**: Output includes a dedicated post-stage section that audits whether
  every stage produced a Triage Note (C-18). The section names any stage where the
  Triage Note was absent. When no stages are missing, the section carries an
  explicit zero-state declaration (e.g., "TRIAGE NOTE GAPS: NONE"). The audit
  aggregates per-stage triage note compliance into a single document-level artifact,
  making completeness verifiable without per-stage inspection.
- **Distinction from C-18**: C-18 requires a Triage Note in every stage. C-23
  requires a post-stage audit that verifies C-18 compliance across all stages and
  names gaps. Per-stage compliance (C-18) is orthogonal to having the completeness
  audit (C-23). A run can pass C-18 (all stages have notes) without C-23 (no audit
  section exists). A run can have C-23 present even when C-18 fails some stages --
  the scan makes failures actionable. C-18 does not need to pass for C-23 to be
  scoreable.
- **Pass condition**: Output includes a labeled post-stage section (e.g., TRIAGE
  NOTE GAPS, TRIAGE AUDIT, or equivalent) that: (1) names each stage that lacked a
  Triage Note, or (2) includes an explicit zero-state declaration (e.g., "TRIAGE
  NOTE GAPS: NONE") if all stages complied. The section must appear after all stage
  findings. An implicit absence of gap discussion does not satisfy this criterion.

---

### C-24 -- Multi-Type Post-Stage Audit Suite
- **Category**: coverage
- **Weight**: aspirational
- **Source**: R5 V-01 -- three independent post-stage check sections (Calibration
  Errors + Role Concern Gaps + Triage Note Gaps), each covering a distinct
  pre-commitment dimension and each applying RULE ZERO-STATE. The suite pattern
  means no pre-commitment type can silently fail -- each has its own named audit
  section with an explicit clean-state declaration when compliance is achieved.
- **Text**: Output includes a suite of three or more independent post-stage audit
  sections, each covering a distinct pre-commitment dimension. Each section has its
  own scope (e.g., calibration block compliance, role-concern declaration compliance,
  triage note compliance), its own zero-state protocol, and its own named gaps list.
  The suite provides comprehensive document-level visibility across all pre-commitment
  types simultaneously, without requiring a reader to scan individual stages for
  each compliance dimension independently.
- **Distinction from C-17**: C-17 requires at least one enforcement audit section
  covering one pre-commitment type. C-24 requires a suite of three or more
  independent sections covering distinct pre-commitment dimensions. Satisfying C-17
  with a single enforcement section does not satisfy C-24. C-17 must pass for C-24
  to be scoreable.
- **Pass condition**: Output includes three or more distinct labeled post-stage
  audit sections, each with a different pre-commitment scope (e.g., calibration
  compliance, role-concern compliance, triage note compliance, or equivalent). Each
  section must independently satisfy the C-19 zero-state protocol: it either names
  gaps or carries an explicit zero-state declaration. Three sections covering the
  same pre-commitment type (e.g., three calibration audits) do not satisfy this
  criterion -- scope diversity is required.

---

### C-25 -- Triage Note Field-Level Compliance Audit
- **Category**: coverage
- **Weight**: aspirational
- **Source**: R6 V-02 -- TRIAGE NOTE GAPS section enumerating three distinct
  failure conditions: (a) absent section, (b) missing named field (HIGH DRIVER /
  LOW ANCHOR / DISTRIBUTION FACTOR), (c) placeholder content. The audit checks not
  just whether a Triage Note exists but whether every named field is populated with
  substantive content. This is a strictly deeper audit than presence-checking alone.
- **Text**: The post-stage triage note gap scan (C-23) validates each Triage Note
  at the field level, not just at the section level. For each stage, the audit
  checks three failure conditions independently: the section is absent, a named
  field is missing, or a named field contains placeholder or non-substantive content
  (e.g., "TBD", "N/A", or a copy of the field label with no explanation). All three
  conditions are named in the audit even when none are triggered -- the zero-state
  declaration covers field-level compliance, not just section presence.
- **Distinction from C-23**: C-23 requires the gap scan to exist and to name stages
  where the Triage Note section was absent. C-25 requires the gap scan to descend
  into each note's named fields and flag field-level gaps or placeholder content.
  A scan that checks only section presence satisfies C-23 but not C-25. C-23 must
  pass for C-25 to be scoreable. C-21 (named triage field vocabulary) must also
  pass -- field-level checking presupposes named fields exist.
- **Pass condition**: The triage note gap scan section enumerates three failure
  conditions (absent section, missing named field, placeholder content) and checks
  each stage's Triage Note against all three. When a field is present but contains
  only placeholder text, the section flags it as a gap. A scan that reports only
  section presence or absence does not satisfy this criterion. C-21 and C-23 must
  both pass for C-25 to be scoreable.

---

### C-26 -- Named Audit Rule with Anti-Pattern Specification
- **Category**: format
- **Weight**: aspirational
- **Source**: R6 V-03 -- RULE AUDIT-SUITE expressed as a named format rule with
  explicit anti-pattern declarations: "merged section does not satisfy" and "same
  dimension three times does not satisfy". Named rules with anti-patterns close the
  gap between the positive requirement and adjacent-but-wrong implementations that
  comply with the letter while violating the intent. The anti-patterns are printed
  artifacts that make the rule self-defending.
- **Text**: The multi-type audit suite requirement (C-24) is expressed as a named
  format rule (e.g., RULE AUDIT-SUITE or equivalent) with explicit anti-pattern
  declarations printed alongside the rule. Anti-patterns name at least two ways a
  run could appear to satisfy the requirement while actually failing it -- for
  example, merging all audit sections into one (violates scope independence) or
  repeating the same pre-commitment dimension three times (violates scope diversity).
  The anti-patterns are not prose commentary; they are labeled declarations in the
  format specification.
- **Distinction from C-24**: C-24 requires three distinct post-stage audit sections
  with scope diversity. C-26 requires the requirement itself to be encoded as a
  named rule with anti-patterns. A run can satisfy C-24 (three sections, correct
  scopes) without satisfying C-26 (the sections exist but the format rule is not
  named and no anti-patterns are declared). C-24 must pass for C-26 to be scoreable.
- **Pass condition**: Output includes a named format rule for the audit suite
  requirement (a label such as RULE AUDIT-SUITE:, AUDIT SUITE RULE:, or equivalent)
  accompanied by at least two explicitly labeled anti-pattern declarations identifying
  implementations that do not satisfy the rule. Anti-patterns must be distinct (one
  structural, one content-based is sufficient) and must be labeled rather than
  embedded in prose rationale. C-24 must pass for C-26 to be scoreable.

---

### C-27 -- Gap-Scan Absence as Format Error
- **Category**: format
- **Weight**: aspirational
- **Source**: R6 V-01 -- absence of the ROLE CONCERN GAPS section is declared a
  format error, not a missing aspiration. Elevating absence to a format error changes
  the framing: the gap scan is no longer optional improvement but a structural
  requirement whose omission invalidates the format. This is a stronger compliance
  signal than requiring the section to exist (C-22/C-23) -- it names the consequence
  of omission in the format spec itself.
- **Text**: The format specification explicitly declares that absence of any
  mandatory post-stage gap-scan section (C-22 or C-23) constitutes a format error.
  The declaration is a printed rule in the format spec, not an implicit expectation.
  A format error has a defined consequence -- the run's format compliance fails
  regardless of other scores. This distinguishes a format spec that requires a
  section from one that enforces it by naming the failure mode.
- **Distinction from C-22 and C-23**: C-22 requires the ROLE CONCERN GAPS section
  to exist. C-23 requires the TRIAGE NOTE GAPS section to exist. C-27 requires the
  format spec to declare that their absence is a format error -- escalating from
  "section required" to "absence is a named failure mode." A format spec that says
  "include this section" satisfies C-22/C-23 on output; only a spec that also says
  "absence = format error" satisfies C-27. C-22 or C-23 must pass for C-27 to be
  scoreable.
- **Pass condition**: The format specification includes an explicit printed
  declaration that absence of at least one mandatory post-stage gap-scan section
  (role-concern or triage-note) constitutes a format error (e.g., "ROLE CONCERN
  GAPS: absence = format error", "TRIAGE NOTE GAPS: required; omission is a format
  violation", or equivalent). The declaration must use error/violation language --
  "strongly recommended" or "should include" do not satisfy this criterion. C-22 or
  C-23 must pass for C-27 to be scoreable.

---

### C-28 -- Named Field-Level Audit Schema
- **Category**: format
- **Weight**: aspirational
- **Source**: R7 V-01 -- TRIAGE NOTE AUDIT SCHEMA with (a)/(b)/(c) labeled
  conditions. The three failure conditions of the field-level audit are expressed as
  a named schema declaration, distinct from any per-stage audit instance. The named
  schema makes the audit structure portable: the three conditions are declared once
  and applied per stage, not re-described inline at each stage. A named schema
  separates structure from application and makes the audit contract explicit.
- **Text**: The field-level audit conditions required by C-25 are expressed as a
  named schema artifact (e.g., TRIAGE NOTE AUDIT SCHEMA:) with labeled condition
  indices -- (a) absent section, (b) missing named field, (c) placeholder content --
  declared as a reusable structure before or alongside the per-stage audit instances.
  The schema is a format-level declaration, not embedded prose: it appears once,
  names each condition, and is referenced by the per-stage results. A variation that
  re-describes the conditions inline within each stage audit without a named schema
  declaration does not satisfy this criterion.
- **Distinction from C-25**: C-25 requires the gap scan to check three failure
  conditions per stage. C-28 requires those conditions to be declared as a named
  schema with labeled indices, separate from their per-stage application. C-25 can
  pass (three conditions checked inline per stage) without C-28 (no named schema
  artifact). Only a named schema declaration -- e.g., TRIAGE NOTE AUDIT SCHEMA with
  labeled (a)/(b)/(c) -- satisfies C-28. C-25 must pass for C-28 to be scoreable.
- **Pass condition**: Output includes a labeled schema declaration (e.g., TRIAGE
  NOTE AUDIT SCHEMA:, FIELD AUDIT SCHEMA:, or equivalent) that names three distinct
  failure conditions with labeled indices ((a), (b), (c) or equivalent). The schema
  appears as a named artifact in the format specification or as a preamble to the
  audit section -- not embedded in per-stage prose. C-25 must pass for C-28 to be
  scoreable.

---

### C-29 -- Enumerated Condition Zero-State
- **Category**: format
- **Weight**: aspirational
- **Source**: R7 V-01 -- TRIAGE NOTE AUDIT RESULT block enumerating all three
  schema conditions as individually clean, rather than a single aggregate "NONE"
  declaration. The enumerated zero-state echoes the schema structure (C-28) in the
  clean case: each condition is confirmed checked and clean independently. This
  closes the loop between the named schema and the per-stage result -- a reader can
  verify that each condition was evaluated, not just that no aggregate violation was
  found.
- **Text**: When a field-level audit (C-25) finds no violations in a stage, the
  zero-state is an enumerated result block that lists each schema condition (C-28)
  as individually clean -- e.g., "(a) NONE", "(b) NONE", "(c) NONE" -- rather than
  a single aggregate "NONE" declaration. The enumerated zero-state makes condition-
  level coverage explicit: a reader can confirm that each condition was checked
  without inferring it from silence or a single-line summary.
- **Distinction from C-19 and C-25**: C-19 requires an explicit zero-state
  declaration when no violations exist (e.g., "TRIAGE NOTE GAPS: NONE"). C-25
  requires three-condition checking per stage. C-29 requires the zero-state to
  enumerate each condition's clean status individually, mirroring the structure of
  the named schema (C-28). "TRIAGE NOTE GAPS: NONE" satisfies C-19 but not C-29 --
  it is a single aggregate declaration. Only a per-condition enumeration (e.g.,
  TRIAGE NOTE AUDIT RESULT block listing each condition as clean) satisfies C-29.
  C-25 and C-28 must both pass for C-29 to be scoreable.
- **Pass condition**: When the field-level audit section reports a zero-violation
  result for a stage, the zero-state is an enumeration that lists each schema
  condition separately as producing no violations. The enumeration uses the same
  condition labels as the named schema (C-28). A single "NONE" or "CLEAN"
  declaration without per-condition enumeration does not satisfy this criterion.
  C-25 and C-28 must both pass for C-29 to be scoreable.

---

### C-30 -- Run-Level Preamble Schema with Named Post-Stage Reference
- **Category**: format
- **Weight**: aspirational
- **Source**: R8 V-05 -- TRIAGE NOTE AUDIT SCHEMA and ROLE CONCERN AUDIT SCHEMA
  both declared in the run-level preamble before any stage output begins. Each
  post-stage audit section references the preamble schema by name ("preamble
  declaration applies") rather than restating the schema inline. The structural
  separation between declaration (preamble) and application (post-stage section)
  is explicit and visible: a reader can confirm the schema is not re-described at
  each application site. V-02 achieves this for the triage note schema alone;
  V-05 achieves it for both schemas simultaneously.
- **Text**: The named schema(s) required by C-28 are declared at run level in a
  preamble -- before any stage output begins -- and each post-stage audit section
  that applies the schema references it by name rather than redeclaring the
  conditions inline. The preamble declaration is visibly separate from its
  application: the schema is defined once, and post-stage sections cite the
  definition by name. A schema co-located with the post-stage audit section
  (declared in the section header or body) satisfies C-28 but not C-30 -- the
  structural separation between declaration and application is the distinguishing
  requirement.
- **Distinction from C-28**: C-28 requires a named schema artifact with labeled
  condition indices. The schema can appear inside the post-stage audit section
  (as in V-01, where it appears within RULE AUDIT-SUITE's Triage Note Compliance
  section) or in the section header (as in V-04). C-30 requires the schema to be a
  run-level preamble declaration and the post-stage section to reference it by name.
  C-28 establishes the schema as a named artifact; C-30 lifts it to run-level scope
  and enforces named reference over inline redeclaration. C-28 must pass for C-30
  to be scoreable.
- **Pass condition**: The format specification includes at least one named schema
  (C-28-compliant) declared in a run-level preamble before any stage output begins.
  At least one post-stage audit section references the preamble schema by name
  (e.g., "preamble declaration applies", "see TRIAGE NOTE AUDIT SCHEMA declared
  above", or equivalent) rather than restating the conditions inline. C-28 must
  pass for C-30 to be scoreable.

---

### C-31 -- Rule Citation Anchors in Post-Stage Section Headers
- **Category**: format
- **Weight**: aspirational
- **Source**: R8 V-05 -- each post-stage audit section header contains inline
  citations of the named rules it implements, e.g., `[RULE CONDITION-ENUM applies]`
  and `[RULE BOOKEND-AUDIT: absence of this section is a FORMAT VIOLATION]`.
  Named rules cited in the header are checkable at output generation time: a model
  generating the section can read the constraint from the section header without
  re-scanning the preamble. This is distinct from declaring rules in a preamble
  (which requires back-referencing) or referencing them in the body (which comes
  after the section is already opened).
- **Text**: Each post-stage audit section header includes inline citations of the
  named rules it applies. The citations are in the header itself -- not only in the
  preamble rule declaration or in the section body. At least one citation names a
  compliance constraint (e.g., "this rule prohibits aggregate NONE" or "absence of
  this section is a FORMAT VIOLATION"). Inline header citations make the constraint
  visible to a reader or generator at the moment the section is opened, without
  requiring a preamble scan.
- **Distinction from C-26 and C-27**: C-26 requires a named audit rule (RULE
  AUDIT-SUITE or equivalent) with labeled anti-patterns declared in the preamble.
  C-27 requires format-error escalation language for absence of gap sections, also
  in the preamble. Both criteria are satisfied by preamble-level declarations alone.
  C-31 requires those named rules to be echoed as inline citations inside the
  section headers they govern. A format spec can pass C-26 and C-27 (rules declared
  in preamble) without passing C-31 (rules not cited in section headers). At least
  one named rule (C-26 or C-27) must pass for C-31 to be scoreable.
- **Pass condition**: At least one post-stage audit section header includes an
  inline citation of a named rule it implements (e.g., `[RULE CONDITION-ENUM
  applies]`, `[RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION]`, or equivalent).
  The citation must appear in the section header, not only in the preamble or
  section body. At least one named rule (C-26 or C-27) must pass for C-31 to be
  scoreable.

---

### C-32 -- Carry-Forward Structural Artifact
- **Category**: format
- **Weight**: aspirational
- **Source**: R9 V-04, V-05 -- RULE CARRY-FORWARD: mandatory per-stage CARRY
  FORWARD sections as labeled artifacts before the Calibration Block. Each section
  lists named findings carried from the previous stage; when nothing carries, the
  section uses an explicit CARRY: NONE zero-state. This makes cross-stage references
  verifiable structural artifacts rather than incidental prose observations embedded
  in findings or verdicts. V-04 and V-05 both implement RULE CARRY-FORWARD; the
  5 carry sites in a 6-stage run guarantee >= 2 named cross-stage references,
  satisfying C-06 as a structural consequence rather than a prose byproduct.
- **Text**: Cross-stage references (C-06) are implemented as mandatory per-stage
  CARRY FORWARD sections -- labeled artifacts appearing before findings begin in
  each stage -- rather than as prose observations embedded in findings or verdicts.
  Each CARRY FORWARD section lists what was carried from the previous stage by
  name. When nothing carries, the section carries an explicit zero-state line
  (CARRY: NONE or equivalent). The structural form guarantees that cross-stage
  references are locatable, scannable, and auditable without reading the full stage
  prose.
- **Distinction from C-06**: C-06 requires at least 2 cross-stage references in a
  multi-stage run and allows those references to appear anywhere in the stage output
  (findings, verdict, prose observation). C-32 requires those references to take the
  form of structured per-stage CARRY FORWARD sections with labeled entries and
  explicit zero-states. A run can pass C-06 (cross-stage references exist in
  findings prose) without passing C-32 (no structured carry block). C-06 must pass
  for C-32 to be scoreable.
- **Pass condition**: At least one stage in the run includes a labeled CARRY FORWARD
  block (or equivalent per-stage carry artifact) appearing before the first finding.
  When nothing carries from the previous stage, the block includes an explicit
  zero-state line (e.g., CARRY: NONE, CARRY FORWARD: NONE, or equivalent). The
  block must be structurally distinct from findings -- carry items are not embedded
  in findings prose. C-06 must pass for C-32 to be scoreable.

---

### C-33 -- Synthesis Non-Audit Declaration
- **Category**: format
- **Weight**: aspirational
- **Source**: R9 V-03, V-05 -- RULE SYNTHESIS declares the SYNTHESIS section
  explicitly as a summary-level analysis artifact, not an audit section, preventing
  it from contributing to RULE AUDIT-SUITE's three required sections. V-03 and
  V-05 both implement this declaration; V-03's scorecard confirms that SYNTHESIS
  "not an audit section per RULE SYNTHESIS declaration; three audit sections remain
  distinct and independent." Without this declaration, the presence of SYNTHESIS
  creates structural ambiguity -- a generator might count it as one of the three
  audit sections, reducing the required count from three to two and triggering
  ANTI-PATTERN-1 (merged/collapsed scope) or ANTI-PATTERN-2 (section count error).
- **Text**: When a SYNTHESIS section is present (C-09, C-10), the format
  specification includes an explicit named declaration that SYNTHESIS is not an
  audit section and does not count toward RULE AUDIT-SUITE's three required
  sections. The declaration is a printed rule or annotation -- it is not inferred
  from structural position or formatting. Without the explicit non-audit declaration,
  SYNTHESIS's presence introduces scope ambiguity that can corrupt the audit suite
  count.
- **Distinction from C-09 and C-10**: C-09 requires a dedicated BLOCKERS
  subsection within SYNTHESIS naming upstream-stage, finding ID, and downstream
  impact. C-10 requires a CROSS-CUTTING THEMES subsection naming document-level
  themes with multi-stage citations. Both are satisfied by the content of SYNTHESIS.
  C-33 requires a named declaration in the format specification that SYNTHESIS does
  not contribute to the RULE AUDIT-SUITE section count. A run can pass C-09 and
  C-10 (SYNTHESIS content correct and complete) without passing C-33 (no non-audit
  declaration present). C-09 or C-10 must pass for C-33 to be scoreable.
- **Pass condition**: The format specification includes a labeled declaration (e.g.,
  RULE SYNTHESIS, a named rule, or an explicit annotation on the SYNTHESIS section)
  stating that SYNTHESIS is not an audit section and does not count toward RULE
  AUDIT-SUITE's required section count. The declaration must be a named printed
  artifact -- a SYNTHESIS section that happens to be formatted differently from
  audit sections does not satisfy this criterion without the explicit declaration.
  C-09 or C-10 must pass for C-33 to be scoreable.

---

### C-34 -- Conditional Item vs Condition Enum Disambiguation
- **Category**: format
- **Weight**: aspirational
- **Source**: R9 V-04, V-05 -- RULE CONDITIONAL-ITEM annotated with an explicit
  disambiguation "[governs conditional verdicts -- distinct from RULE
  CONDITION-ENUM]". Both RULE CONDITIONAL-ITEM and RULE CONDITION-ENUM involve
  enumeration but govern structurally different constructs: RULE CONDITION-ENUM
  governs audit schema result blocks using labeled (a)/(b)/(c) conditions; RULE
  CONDITIONAL-ITEM governs conditional verdict items using numbered what/owner/ref
  entries. Without the annotation, a generator may apply audit-schema enumeration
  patterns (a/b/c) to the verdict block, or numbered verdict patterns to the audit
  result block, corrupting both.
- **Text**: When both conditional verdict itemization (C-11) and field-level audit
  schemas (C-25/C-28) are present, the format specification includes a printed
  annotation on RULE CONDITIONAL-ITEM declaring it explicitly distinct from RULE
  CONDITION-ENUM and naming the distinction. The annotation is a labeled rule-level
  declaration -- not a prose explanation in a section body -- so a generator
  encounters the disambiguation at the point of rule declaration, before either
  construct is applied.
- **Distinction from C-11**: C-11 requires conditional verdicts to enumerate >= 2
  numbered items each naming what/owner/ref. C-34 requires the format specification
  to declare RULE CONDITIONAL-ITEM as explicitly distinct from RULE CONDITION-ENUM
  with a labeled annotation at the rule level. A run can pass C-11 (numbered items
  present and correct) without passing C-34 (no disambiguation annotation printed).
  C-11 and C-28 must both pass for C-34 to be scoreable.
- **Pass condition**: The format specification includes a labeled rule or annotation
  for conditional verdict itemization that explicitly distinguishes it from audit
  schema condition enumeration (e.g., "[governs conditional verdicts -- distinct
  from RULE CONDITION-ENUM]", "RULE CONDITIONAL-ITEM: numbered what/owner/ref items;
  not to be confused with RULE CONDITION-ENUM (a/b/c audit conditions)", or
  equivalent language naming both constructs and declaring their separation). The
  disambiguation must appear in the rule declaration, not in section prose. C-11
  and C-28 must both pass for C-34 to be scoreable.

---

### C-35 -- Audit Table Additive-Not-Replacement Constraint
- **Category**: format
- **Weight**: aspirational
- **Source**: R9 V-02, V-05 -- RULE AUDIT-TABLE declares the stage-per-row table
  as inserted above the AUDIT RESULT block, not as a replacement for it. V-05
  confirms: "AUDIT RESULT block beneath the table (RULE CONDITION-ENUM applies)."
  V-02 confirms: "AUDIT RESULT block preserved beneath." The additive constraint is
  printed in the rule declaration. Without it, adding a table layer could silently
  void C-29 (enumerated condition zero-state) by structurally replacing the
  per-condition enumeration with a table row that summarizes rather than enumerates.
- **Text**: When the enforcement audit section uses a structured table (C-20), the
  format specification declares the table as additive -- inserted above the existing
  AUDIT RESULT block, not as a replacement for it. The AUDIT RESULT block's
  per-condition enumeration (C-29) is explicitly preserved beneath the table. The
  additive constraint is a named requirement in the format specification: it ensures
  that structural additions (new table layers) cannot silently void prior-round
  criteria (enumerated zero-states). A format spec that requires the table but does
  not explicitly preserve the AUDIT RESULT block leaves the structural relationship
  ambiguous and allows C-29 to be silently dropped.
- **Distinction from C-20**: C-20 requires the enforcement audit to use a structured
  table with >= 4 named columns covering stage, pre-commitment, honored status, and
  deviation. C-35 requires the table to be declared additive -- inserted above the
  AUDIT RESULT block, not replacing it -- with explicit preservation of C-29's
  enumerated per-condition result. A run can pass C-20 (table exists with correct
  columns) without passing C-35 (no additive constraint declared; AUDIT RESULT block
  may be absent). C-20 and C-29 must both pass for C-35 to be scoreable.
- **Pass condition**: The format specification includes a named rule or annotation
  for the enforcement audit table (RULE AUDIT-TABLE or equivalent) that explicitly
  states the table is inserted above the AUDIT RESULT block and does not replace it.
  The AUDIT RESULT block's per-condition enumeration (C-29) must be present beneath
  the table in the output. A table without the additive constraint declaration does
  not satisfy this criterion, even if the AUDIT RESULT block happens to be present.
  C-20 and C-29 must both pass for C-35 to be scoreable.

---

### C-36 -- Synthesis Positive-Artifact Subsection Schema
- **Category**: format
- **Weight**: aspirational
- **Source**: R10 V-03 -- RULE SYNTHESIS defined as a positive artifact with 5
  required subsections. V-01 and V-02 implement RULE SYNTHESIS as a non-audit
  exclusion (C-33): they declare what SYNTHESIS is not. V-03 elevates this: RULE
  SYNTHESIS enumerates the required subsections that a well-formed SYNTHESIS must
  contain. The named subsection schema makes SYNTHESIS a first-class positive
  artifact -- a generator must produce all named subsections, and a reviewer can
  audit SYNTHESIS completeness per-subsection independently. Without the subsection
  schema, a SYNTHESIS section can satisfy C-33 (declared non-audit) while remaining
  structurally open-ended: any content qualifies as long as it does not claim audit
  status.
- **Text**: When RULE SYNTHESIS is present (C-33), the format specification
  additionally enumerates the required subsections of SYNTHESIS as a named schema.
  The schema declares what SYNTHESIS must contain -- at minimum the subsections
  carrying blocker detection (C-09) and theme elevation (C-10) -- but extends to
  a complete structural inventory. The subsection schema makes SYNTHESIS a positive
  artifact: both the non-audit exclusion (C-33) and the structural requirements
  (C-36) are declared, and each is independently auditable.
- **Distinction from C-33**: C-33 requires RULE SYNTHESIS to declare the section
  is not an audit section and does not count toward RULE AUDIT-SUITE. C-36 requires
  RULE SYNTHESIS to additionally enumerate its required subsections as a named
  schema with >= 3 labeled entries. A RULE SYNTHESIS that says "NOT an audit
  section; does NOT count toward RULE AUDIT-SUITE" satisfies C-33 but not C-36.
  Only a RULE SYNTHESIS that also declares "must contain: [subsection 1],
  [subsection 2], [subsection 3], ..." satisfies C-36. C-33 must pass for C-36 to
  be scoreable.
- **Pass condition**: RULE SYNTHESIS (or equivalent) includes an enumeration of
  >= 3 labeled required subsections that a well-formed SYNTHESIS must contain. The
  subsections are declared as mandatory components, not as examples or suggestions.
  A RULE SYNTHESIS that names only the non-audit status (C-33) without enumerating
  subsection requirements does not satisfy this criterion. C-33 must pass for C-36
  to be scoreable.

---

### C-37 -- Dual Illustrative Baseline Examples
- **Category**: format
- **Weight**: aspirational
- **Source**: R10 V-03 -- "Dual IB-01+IB-02 baselines." V-01 and V-02 both carry
  a single baseline example (Single IB-01). V-03 introduces a second baseline
  (IB-02) demonstrating a structurally distinct case. A single baseline anchors
  a generator to one positive exemplar; a paired baseline provides contrast. IB-01
  establishes the minimal acceptable case; IB-02 demonstrates a distinct variation
  -- a more complex structural axis, a different scope, an edge case, or an
  alternative valid form. Dual baselines allow triangulation of the acceptable
  range: a generator can identify what is common across both examples (required) and
  what varies between them (acceptable variation). Single-exemplar anchoring
  produces false negatives (novel-but-correct outputs rejected as deviating from
  the single template) and false positives (degenerate copies of the single exemplar
  accepted as correct).
- **Text**: The format specification includes at least two labeled illustrative
  baseline examples -- a primary (IB-01) and a secondary (IB-02) -- demonstrating
  structurally distinct cases. The pair provides contrast: IB-01 and IB-02 differ
  in scenario, structural axis, scope, or complexity. A second example that is a
  minor surface variation of the first (same structure, different topic wording)
  does not satisfy this criterion -- the two baselines must demonstrate distinct
  structural patterns or decision points that a single exemplar cannot capture.
- **Distinction from C-30**: C-30 requires named schemas to be declared in the
  run-level preamble before stage output begins, with post-stage sections citing
  the preamble schema by name. C-37 requires at least two illustrative baseline
  examples demonstrating structurally distinct cases. Orthogonal requirements.
  A run can satisfy C-30 without satisfying C-37. C-37 has no upstream dependency.
- **Pass condition**: The format specification includes at least two labeled
  illustrative baseline examples (IB-01 and IB-02, or equivalent paired labels)
  demonstrating structurally distinct cases. The two examples must differ in at
  least one structural dimension (not merely topic surface). A single baseline
  example does not satisfy this criterion regardless of its complexity. No upstream
  dependency -- C-37 is scoreable independently.

---

### C-38 -- Carry Forward Inertia-ID Dual-Baseline Attribution Column
- **Category**: format
- **Weight**: aspirational
- **Source**: R11 V-04, V-05 -- CARRY FORWARD blocks in both 230-scoring variations
  include an Inertia ID column tagging each carried finding by IB-01, IB-02, both,
  or N/A. The column is absent in V-01 (which has dual baselines but no Inertia ID
  column), and not scoreable for V-02 (C-37 FAIL) or V-03 (C-32 FAIL). The Inertia
  ID column closes the dual-baseline audit chain at the cross-stage handoff artifact:
  a TPM assigning risk register entries to a baseline does not need to re-read stage
  prose; the attribution is structurally settled at the carry block level. The column
  is cost-free to add to any CARRY FORWARD block but makes IB-01/IB-02 attribution
  verifiable across the full cross-stage handoff chain without per-stage prose
  inspection.
- **Text**: When both CARRY FORWARD structural artifacts (C-32) and dual illustrative
  baselines (C-37) are present, the CARRY FORWARD block includes an explicit Inertia
  ID column that tags each carried finding by its baseline attribution: IB-01, IB-02,
  both, or N/A. The column is present in every CARRY FORWARD block, including zero-
  state blocks (where it appears but carries no entries). The baseline attribution at
  the carry-block level enables TPM risk register construction to proceed without
  re-reading stage prose for each carried finding.
- **Distinction from C-32**: C-32 requires the CARRY FORWARD block to exist with
  labeled entries and an explicit CARRY: NONE zero-state when nothing carries. C-38
  requires the block to additionally include an Inertia ID column that attributes
  each carried finding to IB-01, IB-02, both, or N/A. A CARRY FORWARD block with
  labeled entries but no Inertia ID column satisfies C-32 but not C-38. C-32 and
  C-37 must both pass for C-38 to be scoreable.
- **Pass condition**: At least one CARRY FORWARD block in the run includes an
  explicit Inertia ID column (or equivalent labeled baseline attribution field)
  tagging each carried finding as IB-01, IB-02, both, or N/A. The column must be
  present as a structural element of the block, not as an inline annotation within
  finding descriptions. C-32 and C-37 must both pass for C-38 to be scoreable.

---

### C-39 -- IB-02 Urgency Gradient Downstream Citation Cascade
- **Category**: depth
- **Weight**: aspirational
- **Source**: R11 V-05 -- temporal IB-02 framing (12-month projection vs IB-01
  current snapshot) introduces an Urgency Gradient value that cascades into
  mandatory downstream citations. When Urgency Gradient = HIGH, the format
  specification requires: (1) the Go/No-Go table must cite IB-02 explicitly, (2)
  at least one Risk Register entry must name delay-compounding as the inertia
  driver, and (3) the Inertia Pressure Summary must name the compounding path
  explicitly. This cascade is absent in V-04's dimensional framing (technical vs
  organizational), which does not produce a gradient value capable of propagating
  structural constraints to downstream sections. The cascade makes delay-cost
  analysis a verdict-shaping input, not additive documentation.
- **Text**: When IB-02 carries a temporal or urgency axis (e.g., a 12-month
  projection, a delay-compounding scenario, or an urgency gradient value), the
  format specification declares an explicit cascade constraint: if the IB-02
  Urgency Gradient is HIGH, named downstream sections are structurally required to
  cite IB-02. At minimum, the cascade covers the Go/No-Go verdict (must cite IB-02),
  the Risk Register (at least one entry must name the delay-compounding or urgency
  driver from IB-02), and the Inertia Pressure Summary (must name the compounding
  path). The cascade is a printed constraint in the format specification -- it is not
  satisfied by a run that happens to cite IB-02 in downstream sections without a
  declared cascade rule.
- **Distinction from C-37**: C-37 requires paired illustrative baseline examples
  demonstrating structurally distinct cases. C-39 requires an IB-02 Urgency Gradient
  cascade constraint to be declared in the format specification -- a causal chain
  from baseline attribute value (HIGH gradient) to mandatory downstream section
  behavior. A run can satisfy C-37 (two structurally distinct baselines present)
  without satisfying C-39 (no cascade constraint declared, even if IB-02 is
  temporal). C-37 must pass for C-39 to be scoreable.
- **Pass condition**: The format specification includes an explicit declared cascade
  rule: when IB-02 Urgency Gradient = HIGH (or equivalent urgency/temporal
  threshold), at least two named downstream sections are explicitly required to cite
  or incorporate IB-02. The cascade must name the sections and state what IB-02
  must contribute to each (e.g., "Go/No-Go must cite IB-02", "Risk Register must
  include a delay-compounding entry attributed to IB-02"). A run that cites IB-02
  in downstream sections without a declared cascade rule does not satisfy this
  criterion. C-37 must pass for C-39 to be scoreable.

---

### C-40 -- Named Rule Glossary Exclusivity Declaration
- **Category**: format
- **Weight**: aspirational
- **Source**: R11 Signal 1 -- V-01 and V-03 fail both C-30 and C-34 for the same
  root cause: no RUN-LEVEL RULE GLOSSARY. Both criteria require the glossary as
  their structural home: C-30 requires preamble-scope schema declaration with named
  post-stage reference; C-34 requires disambiguation annotation at the rule-
  declaration level. Neither can be satisfied by inline declarations in stage
  templates or section bodies. V-04 and V-05 gain 10 points over V-01/V-03 from
  this single structural decision. C-40 captures the constraint as an explicit
  format rule: the glossary must declare itself as the exclusive site for named
  rule requirements, so a generator that inlines a rule in a stage template cannot
  claim it satisfies a named-rule criterion.
- **Text**: The RUN-LEVEL RULE GLOSSARY includes an explicit self-declaration naming
  itself as the exclusive locus for named format rule declarations. The declaration
  states that named-rule requirements (including but not limited to C-30 preamble
  schema citations and C-34 disambiguation annotations) are satisfied only by
  glossary-level rule declarations -- inline declarations co-located with application
  sites (stage templates, section headers, verdict blocks) do not satisfy named-rule
  criteria. The exclusivity declaration is a printed artifact in the glossary, not
  an implicit structural convention. Without it, a generator may satisfy named-rule
  criteria with inline declarations and produce a structurally correct-appearing
  output that fails the preamble-separation and declaration-scope requirements.
- **Distinction from C-30**: C-30 requires at least one named schema to be declared
  in a run-level preamble before stage output begins, with post-stage sections
  citing it by name. C-40 requires the glossary itself to carry an explicit self-
  declaration of exclusivity -- that it is the only site where named rule
  declarations satisfy named-rule criteria. A glossary that declares schemas at
  preamble scope and generates correct post-stage citations satisfies C-30 but not
  C-40. Only a glossary that additionally includes a printed exclusivity declaration
  satisfies C-40. C-30 must pass for C-40 to be scoreable.
- **Pass condition**: The RUN-LEVEL RULE GLOSSARY includes a labeled exclusivity
  declaration (e.g., "This glossary is the exclusive site for named rule
  declarations -- inline rule declarations in stage templates or section bodies do
  not satisfy named-rule criteria", or equivalent language naming the constraint).
  The declaration must appear in the glossary as a printed artifact, not as a
  section header or structural convention. C-30 must pass for C-40 to be scoreable.

---

### C-41 -- RULE AUDIT-TABLE Named Anti-Pattern Declaration
- **Category**: format
- **Weight**: aspirational
- **Source**: R12 Signal 2 -- V-02's RULE AUDIT-TABLE carries an explicit
  anti-pattern: "Table that replaces the AUDIT RESULT block, silently dropping
  C-29." C-35 requires the additive constraint to be declared (table inserted above
  AUDIT RESULT block, not replacing it). V-02 goes further: the rule names the
  failure mode as a labeled anti-pattern and cites the criterion voided by that
  failure (C-29). This parallels C-26's anti-pattern requirement on RULE AUDIT-SUITE
  and applies the same pattern to RULE AUDIT-TABLE. Without a named anti-pattern,
  a generator can implement a table that structurally replaces the AUDIT RESULT
  block while nominally declaring the additive constraint in the rule header -- the
  anti-pattern closes that gap by naming the disqualifying implementation explicitly.
- **Text**: RULE AUDIT-TABLE (C-35) includes a labeled anti-pattern declaration
  naming the table-as-AUDIT-RESULT-replacement as the disqualifying failure mode,
  with an explicit reference to the criterion it silently drops (C-29 or equivalent).
  The anti-pattern is a printed declaration in the rule, not a prose note: it names
  what a non-conforming implementation looks like and which criterion it voids. This
  makes the additive constraint self-defending -- a generator encounters the failure
  mode explicitly at the point of rule declaration, before the section is generated.
- **Distinction from C-35**: C-35 requires RULE AUDIT-TABLE to declare the table is
  additive -- inserted above the AUDIT RESULT block and not replacing it -- with
  explicit preservation of C-29's enumerated per-condition result. C-41 requires the
  rule to additionally include a labeled anti-pattern declaration naming the
  table-as-AUDIT-RESULT-replacement failure mode and citing the criterion it silently
  drops. A RULE AUDIT-TABLE with the additive constraint but no named anti-pattern
  satisfies C-35 but not C-41. Only a rule that both declares the additive constraint
  and explicitly names the disqualifying anti-pattern satisfies C-41. C-35 must pass
  for C-41 to be scoreable.
- **Distinction from C-26**: C-26 requires RULE AUDIT-SUITE (the multi-type audit
  suite requirement) to carry at least two labeled anti-pattern declarations. C-41
  requires RULE AUDIT-TABLE (the enforcement audit table additive constraint) to
  carry a named anti-pattern for the table-as-replacement failure mode. The two
  rules govern different constructs; C-41 applies C-26's anti-pattern discipline to
  a second named rule. C-35 must pass for C-41 to be scoreable; C-26 does not need
  to pass.
- **Pass condition**: RULE AUDIT-TABLE (or equivalent enforcement audit table rule)
  includes a labeled anti-pattern declaration (e.g., "Anti-pattern: Table that
  replaces the AUDIT RESULT block, silently dropping C-29" or equivalent language
  naming the failure mode and the criterion voided). The anti-pattern must be a
  named printed declaration in the rule -- prose commentary in a section body does
  not satisfy this criterion. The criterion cited as voided must be identifiable
  (C-29, enumerated condition zero-state, or equivalent label). C-35 must pass for
  C-41 to be scoreable.

---

### C-42 -- Glossary Exclusivity Named-Criterion Enumeration
- **Category**: format
- **Weight**: aspirational
- **Source**: R12 Signal 1 -- V-01's C-40 pass demonstrates generic exclusivity
  language: "This glossary is the exclusive locus for named format rule declarations
  ... Named-rule requirements cannot be satisfied by inline rule declarations in
  stage templates or section bodies." This satisfies C-40. V-01 does not, however,
  enumerate the specific named-rule criteria protected by the exclusivity constraint.
  C-42 captures the stronger form: the exclusivity declaration names C-30 (preamble
  schema with named post-stage reference) and C-34 (conditional item vs condition
  enum disambiguation) or equivalent criterion labels as the criteria whose
  satisfaction requires glossary scope. Without enumeration, the declaration is a
  general constraint; a generator may still satisfy named-rule criteria by inlining
  the specific schema or annotation in question without recognizing that the criterion
  explicitly requires glossary scope. With enumeration, the declaration is
  self-documenting: each protected criterion is named, and a generator reading the
  glossary encounters the full list of criteria that cannot be satisfied inline.
- **Text**: The RUN-LEVEL RULE GLOSSARY's exclusivity declaration (C-40) additionally
  enumerates the specific named-rule criteria whose satisfaction requires glossary-
  scope declarations. At minimum, the enumeration names the criteria corresponding
  to preamble schema with named post-stage reference (C-30 or equivalent) and
  conditional item vs condition enum disambiguation (C-34 or equivalent). The
  enumeration is a printed list in the exclusivity declaration -- it names each
  protected criterion by label or functional description, not by general category
  only. Generic language ("named-rule requirements") without criterion enumeration
  satisfies C-40 but not C-42.
- **Distinction from C-40**: C-40 requires the glossary to carry a printed
  exclusivity declaration stating that named-rule requirements cannot be satisfied by
  inline declarations. C-42 requires that declaration to additionally enumerate the
  specific criteria it protects, naming at least two by label (e.g., C-30, C-34) or
  functional description. A glossary with generic exclusivity language satisfies
  C-40 but not C-42. Only a glossary whose exclusivity declaration names the
  specific criteria that require glossary scope satisfies C-42. C-40 must pass for
  C-42 to be scoreable.
- **Pass condition**: The glossary exclusivity declaration (C-40-compliant) includes
  a printed enumeration of at least two named-rule criteria whose satisfaction
  requires glossary-scope declaration. The enumeration names each criterion by label
  (e.g., "C-30: preamble schema named reference" and "C-34: conditional item
  disambiguation") or by an equivalent functional description that uniquely
  identifies the criterion. Generic language naming only the category ("preamble
  schemas", "disambiguation annotations") without identifying specific criteria does
  not satisfy this criterion. C-40 must pass for C-42 to be scoreable.

---

### C-43 -- Criterion Enumeration Label-Plus-Description Pairing
- **Category**: format
- **Weight**: aspirational
- **Source**: R13 Signal 1 -- V-01's C-42 pass enumerates protected criteria as
  "C-30 (Run-Level Preamble Schema with Named Post-Stage Reference)" and "C-34
  (Conditional Item vs Condition Enum Disambiguation)". Each entry is a criterion
  ID label paired with a parenthetical functional description. C-42 requires
  enumeration by label or functional description -- either alone satisfies C-42.
  V-01's implementation provides both simultaneously: the ID label anchors the
  criterion precisely and survives rubric restructuring; the parenthetical description
  communicates the criterion's function without requiring the reader to look it up.
  A glossary enumerating labels alone (e.g., "C-30 and C-34") satisfies C-42 but
  leaves a generator that does not know the rubric unable to derive the function from
  the ID. A glossary enumerating functional descriptions alone satisfies C-42 but
  loses the stable criterion reference if criteria are renumbered. Only label-plus-
  description pairing is simultaneously stable (anchored to ID) and self-documenting
  (readable without the rubric).
- **Text**: Each criterion enumerated in the glossary exclusivity declaration (C-42)
  is expressed as a label-plus-description pair: the criterion ID label followed
  immediately by a parenthetical functional description that identifies the
  criterion's purpose without requiring rubric lookup. The pairing applies to every
  enumerated criterion -- a declaration that provides label-plus-description for one
  criterion and label-only for another does not fully satisfy C-43. The functional
  description must be substantive: a restatement of the criterion ID (e.g., "C-30
  (C-30)") or a trivially short phrase (e.g., "C-30 (preamble)") does not satisfy
  this criterion.
- **Distinction from C-42**: C-42 requires the enumeration to name each protected
  criterion by label or functional description -- either form satisfies C-42. C-43
  requires both the label and a substantive parenthetical functional description for
  each enumerated criterion. A declaration that names criteria by ID alone satisfies
  C-42 but not C-43. A declaration that names criteria by functional description
  alone satisfies C-42 but not C-43. Only a declaration that pairs each criterion
  ID with its functional description satisfies C-43. C-42 must pass for C-43 to be
  scoreable.
- **Pass condition**: The glossary exclusivity enumeration (C-42-compliant) presents
  every enumerated criterion as a label-plus-description pair: the criterion ID
  label (e.g., C-30) followed by a parenthetical functional description (e.g.,
  "Run-Level Preamble Schema with Named Post-Stage Reference") that identifies the
  criterion's function without requiring rubric consultation. All enumerated criteria
  must use the paired format -- partial pairing (some criteria with description,
  some without) does not satisfy this criterion. C-42 must pass for C-43 to be
  scoreable.

---

### C-44 -- AUDIT RESULT Block Independence Declaration
- **Category**: format
- **Weight**: aspirational
- **Source**: R13 Signal 2 -- V-02's C-35 pass includes "The AUDIT RESULT block
  with per-condition (a)/(b)/(c) enumeration is preserved BENEATH the table and is
  mandatory regardless of table presence." The phrase "mandatory regardless of table
  presence" is the key signal: it establishes that the AUDIT RESULT block's
  mandatory status is independent of the table's existence -- not just that the
  table does not replace it (C-35), but that the block is required whether or not
  the table is present at all. C-35 requires the additive constraint: table inserted
  above, not replacing. V-02 goes further with a two-way independence declaration:
  (1) if the table is present, the AUDIT RESULT block is preserved beneath it; (2)
  if the table were absent, the AUDIT RESULT block would still be required. The
  independence declaration prevents the conditional reading of C-35 -- "keep AUDIT
  RESULT when table is added" -- from being misread as "AUDIT RESULT is only
  required when the table is present." Without the independence declaration, a
  generator could interpret the additive constraint as establishing the table as
  the trigger for AUDIT RESULT block presence. With it, the AUDIT RESULT block is
  unconditionally mandatory and the table is the optional addition.
- **Text**: RULE AUDIT-TABLE (C-35) additionally declares the AUDIT RESULT block
  as independently mandatory -- required regardless of whether the table is present.
  The independence declaration is a printed statement in the rule: it establishes
  that the AUDIT RESULT block's mandatoriness is not conditioned on the table's
  existence. The additive constraint (C-35) establishes ordering: table above AUDIT
  RESULT. The independence declaration (C-44) establishes unconditional status: AUDIT
  RESULT required whether or not table is present. Both are required for a complete
  declaration of the two artifacts' relationship.
- **Distinction from C-35**: C-35 requires RULE AUDIT-TABLE to declare the table
  is inserted above the AUDIT RESULT block and not replacing it. The additive
  constraint establishes that adding the table does not remove the AUDIT RESULT
  block. C-44 requires the rule to additionally declare the AUDIT RESULT block as
  mandatory regardless of table presence -- establishing that the block's mandatory
  status is independent of the table. A rule that declares the additive constraint
  without the independence statement allows the conditional reading: AUDIT RESULT is
  required when the table is present (but perhaps not otherwise). Only a rule that
  explicitly states the AUDIT RESULT block is "mandatory regardless of table
  presence" or equivalent unconditional language satisfies C-44. C-35 must pass for
  C-44 to be scoreable.
- **Pass condition**: RULE AUDIT-TABLE (or equivalent) includes a printed statement
  declaring the AUDIT RESULT block as mandatory regardless of whether the table is
  present (e.g., "mandatory regardless of table presence", "required whether or not
  the table is present", "independently required -- table presence does not
  condition AUDIT RESULT block", or equivalent unconditional language). The
  statement must be a printed declaration in the rule, not derivable from the
  additive constraint alone. C-35 must pass for C-44 to be scoreable.

---

### C-45 -- Exclusivity Declaration Protected-Count Annotation
- **Category**: format
- **Weight**: aspirational
- **Source**: R14 Signal 1 -- Universal C-43 pass across all R14 variations
  produces identical glossary preambles enumerating C-30 (Run-Level Preamble
  Schema with Named Post-Stage Reference) and C-34 (Conditional Item vs Condition
  Enum Disambiguation) as full label+description pairs. C-43 requires each
  enumerated criterion to use the paired form; it does not require the declaration
  to state how many criteria are enumerated. A glossary that enumerates "C-30 (...)
  and C-34 (...)" satisfies C-43 regardless of whether the count is stated. The
  absence of a count leaves a gap: a generator adding a third glossary-scope
  criterion could inline the first two by name while treating the third as
  satisfiable inline, without any declared count to trigger revision. An explicit
  count annotation -- "exactly 2 criteria require glossary scope: C-30 (...) and
  C-34 (...)" -- closes this gap. The count is auditable independently of the
  enumeration: a reader can verify the count without re-reading the full list, and
  a change in the set of protected criteria requires a count update, making silent
  additions structurally detectable.
- **Text**: The glossary exclusivity declaration (C-42/C-43) additionally states
  the count of protected criteria explicitly alongside the enumeration. The count
  annotation precedes or accompanies the criterion list as a fixed numeric claim
  (e.g., "exactly 2 criteria require glossary scope" or "N criteria are protected
  from inline satisfaction: C-30 (...) and C-34 (...)"). The count must match the
  enumerated list exactly and must use count-fixing language -- phrasing like "the
  following criteria" without a count does not satisfy this criterion. The count
  annotation makes the enumeration verifiable by count without re-reading the full
  list, and makes silent additions detectable: adding a criterion to the protected
  set requires updating the count, which surfaces as an explicit change rather than
  an appended entry.
- **Distinction from C-43**: C-43 requires each enumerated criterion to be expressed
  as a label-plus-description pair -- both the criterion ID label and a parenthetical
  functional description. C-45 requires the declaration to additionally state the
  count of protected criteria explicitly (e.g., "exactly 2 criteria..."). A
  declaration with full label+description pairing for all enumerated criteria
  satisfies C-43 but not C-45 without the count annotation. Only a declaration
  that both uses the paired form (C-43) and fixes the count (C-45) satisfies both.
  C-43 must pass for C-45 to be scoreable.
- **Pass condition**: The glossary exclusivity declaration includes an explicit
  count annotation stating the number of protected criteria (e.g., "exactly N
  criteria require glossary scope", "N criteria are protected", or equivalent
  count-fixing language) alongside the criterion enumeration. The count must be a
  specific number -- a phrase like "the following criteria" without a numeral does
  not satisfy this criterion. The stated count must match the actual number of
  enumerated criteria. C-43 must pass for C-45 to be scoreable.

---

### C-46 -- RULE AUDIT-TABLE Bidirectional Condition Enumeration
- **Category**: format
- **Weight**: aspirational
- **Source**: R14 Signal 2 -- Universal C-44 pass across all R14 variations
  produces RULE AUDIT-TABLE declarations with unconditional mandate language
  ("mandatory regardless of table presence"). C-44 requires the independence
  declaration to state the AUDIT RESULT block is required whether or not the table
  is present -- a single unconditional statement satisfies C-44. The signal text
  ("preserved BENEATH the table and is mandatory regardless of table presence") is
  a combined additive+independence statement expressed as a single continuous clause.
  The next distinguishing form enumerates both conditional branches as separate
  numbered items: (1) when table is present -- AUDIT RESULT block is preserved
  beneath it; (2) when table is absent -- AUDIT RESULT block is still required.
  Enumerated branches make coverage verifiable: a reader confirms both halves are
  present without parsing a combined clause. A generator producing the section can
  check each branch independently. A single unconditional statement satisfies C-44;
  only explicit enumeration of both branches satisfies C-46.
- **Text**: RULE AUDIT-TABLE (C-44) states the AUDIT RESULT block's independence
  using explicit two-branch enumeration: one numbered item covering the present-
  table case (AUDIT RESULT block preserved beneath the table) and one numbered item
  covering the absent-table case (AUDIT RESULT block still required). The two
  branches are structurally distinct items, not a single combined clause. The
  enumeration makes the independence declaration a complete conditional coverage:
  a reader can confirm both cases are handled without inference from a shorthand
  statement. A rule that states "mandatory regardless of table presence" satisfies
  C-44 but does not enumerate both branches -- C-46 requires the enumerated form.
- **Distinction from C-44**: C-44 requires RULE AUDIT-TABLE to include a printed
  statement declaring the AUDIT RESULT block as mandatory regardless of table
  presence -- unconditional language. C-46 requires that independence to be stated
  as two enumerated conditional branches: the present-table case and the absent-
  table case as separate numbered or labeled items. A single "mandatory regardless"
  statement satisfies C-44 but not C-46. A rule that enumerates: "(1) when table is
  present: AUDIT RESULT block is preserved beneath it; (2) when table is absent:
  AUDIT RESULT block is still required" satisfies both. Only the enumerated form
  satisfies C-46. C-44 must pass for C-46 to be scoreable.
- **Pass condition**: RULE AUDIT-TABLE (or equivalent) states the AUDIT RESULT
  block's independence using at least two enumerated items covering distinct cases:
  (1) the present-table case and (2) the absent-table case. Each item must be a
  distinct numbered or labeled declaration, not a combined clause. The two items
  together must cover both conditional branches -- a rule that states one branch
  without the other does not satisfy this criterion even if the stated branch
  implies independence. C-44 must pass for C-46 to be scoreable.

---

## Criterion Summary

| ID   | Text (short)                                  | Weight        | Category    | Added |
|------|-----------------------------------------------|---------------|-------------|-------|
| C-01 | Stage identity and labeling                   | essential     | format      | v1    |
| C-02 | Role-loaded perspective                       | essential     | correctness | v1    |
| C-03 | ROB document format compliance                | essential     | format      | v1    |
| C-04 | Actionable findings (2x per stage)            | essential     | depth       | v1    |
| C-05 | Explicit go/no-go in tpm stage                | essential     | correctness | v1    |
| C-06 | Cross-stage coherence                         | recommended   | depth       | v1    |
| C-07 | Structured risk register in tpm               | recommended   | depth       | v1    |
| C-08 | Exec-office cascade tracing                   | recommended   | coverage    | v1    |
| C-09 | Inter-stage blocker detection                 | aspirational  | depth       | v1    |
| C-10 | Cross-cutting theme elevation                 | aspirational  | depth       | v1    |
| C-11 | Conditional verdict itemization               | aspirational  | depth       | v2    |
| C-12 | Finding severity discrimination               | aspirational  | depth       | v2    |
| C-13 | Risk register status lifecycle                | aspirational  | coverage    | v2    |
| C-14 | Pre-finding severity calibration              | aspirational  | depth       | v3    |
| C-15 | Risk register update protocol                 | aspirational  | coverage    | v3    |
| C-16 | Role-lens pre-declaration                     | aspirational  | depth       | v4    |
| C-17 | Pre-commitment enforcement audit              | aspirational  | depth       | v4    |
| C-18 | Universal per-stage triage note               | aspirational  | depth       | v4    |
| C-19 | Zero-deviation explicit declaration           | aspirational  | depth       | v5    |
| C-20 | Enforcement audit structured table            | aspirational  | format      | v5    |
| C-21 | Named triage field vocabulary                 | aspirational  | format      | v5    |
| C-22 | Post-stage role-concern gap scan              | aspirational  | coverage    | v6    |
| C-23 | Post-stage triage note gap scan               | aspirational  | coverage    | v6    |
| C-24 | Multi-type post-stage audit suite             | aspirational  | coverage    | v6    |
| C-25 | Triage note field-level compliance            | aspirational  | coverage    | v7    |
| C-26 | Named audit rule with anti-patterns           | aspirational  | format      | v7    |
| C-27 | Gap-scan absence as format error              | aspirational  | format      | v7    |
| C-28 | Named field-level audit schema                | aspirational  | format      | v8    |
| C-29 | Enumerated condition zero-state               | aspirational  | format      | v8    |
| C-30 | Preamble schema with named reference          | aspirational  | format      | v9    |
| C-31 | Rule citation anchors in headers              | aspirational  | format      | v9    |
| C-32 | Carry-forward structural artifact             | aspirational  | format      | v10   |
| C-33 | Synthesis non-audit declaration               | aspirational  | format      | v10   |
| C-34 | Conditional item vs condition enum disambig.  | aspirational  | format      | v10   |
| C-35 | Audit table additive-not-replacement          | aspirational  | format      | v10   |
| C-36 | Synthesis positive-artifact subsection schema | aspirational  | format      | v11   |
| C-37 | Dual illustrative baseline examples           | aspirational  | format      | v11   |
| C-38 | Carry forward inertia-ID baseline column      | aspirational  | format      | v12   |
| C-39 | IB-02 urgency gradient cascade constraint     | aspirational  | depth       | v12   |
| C-40 | Named rule glossary exclusivity declaration   | aspirational  | format      | v12   |
| C-41 | RULE AUDIT-TABLE named anti-pattern           | aspirational  | format      | v13   |
| C-42 | Glossary exclusivity named-criterion enum.    | aspirational  | format      | v13   |
| C-43 | Criterion enumeration label-plus-description  | aspirational  | format      | v14   |
| C-44 | AUDIT RESULT block independence declaration   | aspirational  | format      | v14   |
| C-45 | Exclusivity declaration protected-count annot.| aspirational  | format      | v15   |
| C-46 | RULE AUDIT-TABLE bidirectional cond. enum.    | aspirational  | format      | v15   |
