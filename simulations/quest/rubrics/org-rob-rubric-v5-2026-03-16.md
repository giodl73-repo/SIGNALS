Written to `simulations/quest/rubrics/org-rob-rubric-v5-2026-03-16.md`.

---

**Two new criteria extracted from R5:**

**C-18 — Role Orientation Frame Citation** (correctness, aspirational)
Source: V-01 R5. The ROLE: line in each stage cites the specific `orientation.frame` field extracted from `.roles/`, not just the role name. Makes role loading verifiable at stage level, independent of per-finding Via: fields. C-02 asks "does the review reflect the role?"; C-18 asks "is the governing frame named so the claim is checkable?"

**C-19 — Schema-Enforced Lens Coverage** (format, aspirational)
Source: V-02 R5. Via: is positioned as the *second column* in the finding table — before Severity, before Owner — making lens omission structurally visible and achieving 100% coverage. C-14 requires 50%+; C-19 requires 100% enforced by column position. The field's position is the criterion, not just the coverage rate.

**Scoring changes:**

| | v4 | v5 |
|---|---|---|
| Aspirational criteria | C-09--C-17 (9) | C-09--C-19 (11) |
| Aspirational max | 18 | 22 |
| Total max | 108 | **112** |

The two new criteria are structurally independent — V-01 R5 earns C-18 ++ but C-19 o; V-02 R5 earns C-19 ++ but C-18 o. Same divergence pattern as V-02/V-03 on C-15/C-17.
ot just the coverage
rate.

**Scoring impact:**
- N_aspirational: 9 → 11
- Aspirational tier max: 18 → 22
- Total max: 108 → **112**

**R5 scores under v5:**

| Variation | R5 score (v4) | R5 score (v5) | Delta |
|-----------|--------------|--------------|-------|
| V-01 | 101 | **103** | +2 (C-18=++) |
| V-02 | 104 | **106** | +2 (C-19=++) |

C-18 and C-19 are structurally independent: V-01 earns C-18 ++ (orientation frame in ROLE:
line) but C-19 o (no Via: field). V-02 earns C-19 ++ (Via: as second column, 100% coverage)
but C-18 o (orientation frame not cited at stage level). Different structural paths to
different aspirational criteria -- same as the V-02/V-03 divergence on C-15/C-17.

---

## Scoring Framework

| Tier | Criteria | Max pts | ++ | + | o |
|------|----------|---------|----|---|---|
| Essential | C-01--C-05 | 60 | 12 | 12* | 0 |
| Recommended | C-06--C-08 | 30 | 10 | 7 | 0 |
| Aspirational | C-09--C-19 | 22 | 2 | 1 | 0 |

*Essential + = PASS. Both + and ++ earn full points for essential criteria.

**Total max: 60 + 30 + 22 = 112**

Any essential failure = not golden regardless of composite score.

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
  identifying it by name. No stage is anonymous.

---

### C-02 -- Role-Loaded Perspective
- **Category**: correctness
- **Weight**: essential
- **Text**: Each stage review reflects the perspective of the role loaded from
  .roles/ -- not a generic review. The role orientation, lens, and
  expertise shape which concerns are raised.
- **Pass condition**: At least one finding per stage is grounded in the loaded
  role documented lens (e.g., a PM flags adoption risk, a TPM flags schedule
  risk, an architect flags coupling). Generic findings that any role could have
  written do not satisfy this criterion.

---

### C-03 -- ROB Document Format Compliance
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

### C-04 -- Actionable Findings
- **Category**: depth
- **Weight**: essential
- **Text**: Each stage produces at least 2 concrete findings or decision points.
  Findings name a specific concern, not a category. Each finding has an implied
  or explicit owner and a suggested resolution or next step.
- **Pass condition**: Total findings >= 2 * N_stages_run. Each finding is specific
  (references the artifact, not just the domain). At least half of findings include
  a resolution path or owner.

---

### C-05 -- Go/No-Go Signal
- **Category**: correctness
- **Weight**: essential
- **Text**: When the tpm stage runs (including via --stage all), output includes
  an explicit go/no-go recommendation with rationale. The verdict is not implied or
  buried -- it is a top-level statement.
- **Pass condition**: tpm stage output contains an unambiguous GO / NO-GO /
  GO WITH CONDITIONS verdict as a labeled top-level element, accompanied by at
  least one sentence of rationale citing a specific finding.

---

## Recommended Criteria

*Output is better with these. Each adds material value.*

### C-06 -- Cross-Stage Coherence
- **Category**: depth
- **Weight**: recommended
- **Text**: When multiple stages run, later stages reference or escalate findings
  from earlier stages. The escalation chain (teams -> pm -> tpm) is visible: a
  teams finding becomes a pm alignment item, which becomes a tpm risk.
- **Pass condition**: At least 2 cross-stage references in any multi-stage run
  (e.g., "teams raised X; pm confirms X is unresolved; tpm registers X as risk R-02").

---

### C-07 -- Risk Register Structure
- **Category**: depth
- **Weight**: recommended
- **Text**: The tpm stage produces a structured risk register, not a prose list.
  Each entry has a title, severity, likelihood, and mitigation. The register is
  machine-scannable.
- **Pass condition**: tpm stage includes a risk register table or structured list
  with >= 3 entries, each containing title, severity, likelihood, and mitigation.
  At least one risk is rated HIGH.

---

### C-08 -- Spire Cascade Tracing
- **Category**: coverage
- **Weight**: recommended
- **Text**: When the spire stage runs, output traces how S-office missions cascade
  down to the artifact under review. At least one mission-to-artifact link is
  explicit: mission -> program -> artifact alignment or gap.
- **Pass condition**: spire stage output names at least one S-office mission by
  name and traces its alignment or misalignment to the artifact under review with
  a specific example.

---

## Aspirational Criteria

*Raise the bar once essential and recommended are stable.*

### C-09 -- Inter-Stage Blocker Detection
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

### C-10 -- Cross-Cutting Theme Elevation
- **Category**: depth
- **Weight**: aspirational
- **Text**: When the same concern surfaces in 2 or more stages, output recognizes
  the pattern and elevates it as a cross-cutting theme -- above the individual
  stage findings. Cross-cutting themes receive priority weighting.
- **Pass condition**: At least 1 cross-cutting theme is named at the document level
  (not buried inside a single stage), citing the 2+ stages that surfaced it and
  noting why the repetition increases severity.

---

### C-11 -- Phase Gate Contracts
- **Category**: depth
- **Weight**: aspirational
- **Text**: Each stage defines explicit entry and exit conditions that enforce
  cross-stage coherence structurally rather than narratively. Entry conditions
  state what must be true before the stage can proceed; exit conditions state
  what the stage certifies as resolved before handing off downstream.
- **Pass condition**: At least 2 stages in a multi-stage run include a Phase Gate
  block (or equivalent labeled section) with named entry conditions and named exit
  conditions. Exit conditions must reference at least one finding ID or open item
  from that stage, not just generic readiness language.
- **Source**: V-04 Round 1 -- only variation to hit 100. Phase gate contracts make
  C-06 structurally checkable instead of relying on narrative cross-references.
  V-02 R2 fails this criterion: finding registry accumulation is not equivalent
  to phase gate contracts.

---

### C-12 -- Dual-Direction Traceability
- **Category**: depth
- **Weight**: aspirational
- **Text**: Cross-stage finding propagation is acknowledged in both directions:
  the sending stage escalates the finding, and the receiving stage explicitly
  acknowledges receipt by finding ID. Traceability is not one-sided.
- **Pass condition**: In any multi-stage run with escalation, at least 1 receiving
  stage contains a Responds-to or Inherits field (or equivalent) citing the
  upstream finding ID (e.g., "Inherits: PM-F-02 -- ownership gap"). The downstream
  stage verdict must reference the inherited finding.
- **Source**: V-04 Round 1 -- dual-direction acknowledgment makes the escalation
  chain independently verifiable; no other Round 1 variation enforced the receiving
  side.

---

### C-13 -- Named Blocker Format
- **Category**: correctness
- **Weight**: aspirational
- **Text**: When a downstream finding retroactively invalidates an upstream verdict
  (e.g., arch-board finding overturns a tpm go), the output names this explicitly
  using a triad: upstream stage + blocking finding + required action. Retroactive
  invalidation is surfaced as a named event, not implied by silence.
- **Pass condition**: At least 1 retroactive invalidation scenario in a multi-stage
  run is expressed using the triad format: {upstream-stage} verdict affected by
  {finding-ID}: {reason}. Required action: {action}. The upstream stage and its
  original verdict must be identifiable from the named blocker.
- **Source**: V-04 Round 1 -- named format {AB-01} blocks tpm go/no-go: [reason].
  Upstream stage affected. Required action. was the sole mechanism enabling
  cross-stage retroactive invalidation. No other variation in Round 1 enforced this.

---

### C-14 -- Lens-Anchored Findings
- **Category**: correctness
- **Weight**: aspirational
- **Text**: Each finding cites the specific lens item or orientation frame from the
  loaded role (.roles/) that triggered it. Role-loading is verifiable at
  the finding level, not just at the stage level. A finding that could have been
  written by any role does not clear C-14, even if the stage header names a role.
- **Pass condition**: At least 50% of findings across the run include a Lens:,
  Via:, or equivalent field naming the specific role lens item that motivated the
  concern (e.g., "Lens: tpm.lens.schedule-risk" or "Via: orientation.frame --
  delivery velocity"). The cited lens item must exist in the loaded role file.
- **Source**: R2 scorecard -- both V-01 and V-02 scored + on C-02 (role lens
  shapes the stage orientation) but neither reached ++. The gap: no per-finding
  lens citation field was required. The ++ path on C-02 requires finding-level
  lens enforcement, which C-14 now rewards explicitly.

---

### C-15 -- Column-Invariant Verdict Format
- **Category**: format
- **Weight**: aspirational
- **Text**: Stage verdicts are expressed as table rows with named columns rather
  than prose blocks. Column-invariant output eliminates the structural ambiguity
  that allows omission of rationale or finding-ID citation. Prose verdicts satisfy
  C-03 but do not satisfy C-15.
- **Pass condition**: At least 2 stage verdicts in the run are expressed as rows
  in a named-column table containing at minimum: (1) status (GO / NO-GO / etc.),
  (2) rationale, (3) at least one finding-ID reference. Prose verdict blocks, even
  if they contain the same information, do not satisfy this criterion.
- **Source**: R2 scorecard -- V-02 scored ++ on C-03 because "verdict table is
  a structural table row, not prose." V-01 scored + because "prose template, not
  column invariant." C-03 pass condition does not distinguish these two structural
  forms. C-15 rewards the encoding that makes verdict omission structurally
  impossible.

---

### C-16 -- Synthesis Residual Open Items
- **Category**: depth
- **Weight**: aspirational
- **Text**: Synthesis contains a dedicated section enumerating all finding
  escalations that were sent upstream but not yet acknowledged or resolved
  downstream. This inventory makes gaps in the escalation chain structurally
  visible without requiring manual comparison of sending and receiving stages.
  A Dual-Direction Check table satisfies C-12; a Residual Open Items section
  satisfies C-16 -- they are complementary, not interchangeable.
- **Pass condition**: Synthesis output includes a Residual Open Items section (or
  equivalent labeled section) listing every finding where the downstream
  acknowledgment is absent or empty, naming: (1) the originating stage, (2) the
  finding ID, (3) the intended receiving stage, (4) the gap (e.g., Acknowledged
  As = empty). The section must be present even when the list is empty -- an
  empty residual section is a stronger signal than a missing one.
- **Source**: R2 scorecard -- V-02 achieved C-06 ++ partly via "Residual Open
  Items section flags any Acknowledged As = empty -- coherence failure is
  structurally visible." V-01 achieved C-06 ++ via Dual-Direction Check table
  instead. C-16 rewards the dedicated residual-items inventory as a distinct
  structural property separate from C-09 (prospective blocker detection) and C-12
  (per-finding dual-direction tracing).

---

### C-17 -- Stage-Maintained Finding Ledger
- **Category**: depth
- **Weight**: aspirational
- **Text**: A shared finding ledger is initialized before the first stage runs and
  actively maintained by each stage throughout the review. Unlike a synthesis
  registry compiled after the fact, the ledger is a write-as-you-go artifact:
  each stage appends new findings as rows and fills in Resolved By and Resolution
  for any inherited rows it closes. Stages cite the ledger by row number within
  their own output. The ledger serves as the authoritative cross-stage audit trail
  and is the primary source for Residual Open Items filtering (C-16).
- **Pass condition**: A named finding ledger (or equivalent table) is present,
  referenced by row number in at least 2 distinct stages, and contains at least
  one row where both Resolved By (the downstream stage) and Resolution are filled
  in -- demonstrating that a stage consumed and closed an upstream row. A
  synthesis-only registry that aggregates after all stages complete does not
  satisfy this criterion; the ledger must be written to incrementally.
- **Source**: V-03 R3 (Residual-Accumulator Model) -- achieves C-12 ++ via "each
  stage cites ledger row number and fills Resolved By + Resolution; ledger shows
  both sending and receiving sides," and C-16 ++ via "Residual Open Items section
  filters ledger rows where Resolved By = (pending)." No other R3 variation used a
  stage-maintained ledger as the primary cross-stage tracking artifact. V-02
  Finding Registry (managed centrally at synthesis) satisfies C-12 and C-16 via a
  different structural mechanism and does not satisfy C-17.

---

### C-18 -- Role Orientation Frame Citation
- **Category**: correctness
- **Weight**: aspirational
- **Text**: Each stage cites the specific `orientation.frame` (or equivalent named
  field) from the loaded .roles/ file in its stage-level ROLE: block. Role
  loading is verifiable at the stage level independently of per-finding Via: fields
  (C-14). A stage that names the role without surfacing the governing orientation
  frame satisfies C-02 but does not satisfy C-18.
- **Pass condition**: At least 2 stages in the run include a ROLE: line (or
  equivalent labeled block) that cites a specific named field from the loaded role
  file -- e.g., `orientation.frame`, `lens.primary`, or equivalent -- by field name
  and value. The cited field must be traceable to the .roles/ file. Naming
  the role alone (e.g., "Role: tpm") does not satisfy this criterion.
- **Source**: V-01 R5 (Phase Gate Contracts with Finding-ID Certification) --
  `orientation.frame` extracted from .roles/ and cited in ROLE: line of each
  stage, enabling per-stage verification that the correct review lens was loaded.
  C-02 requires at least one finding grounded in the role lens; C-18 requires the
  lens source to be cited at the stage header level. These are complementary:
  C-14 anchors lens citation to findings, C-18 anchors it to stage identity.

---

### C-19 -- Schema-Enforced Lens Coverage
- **Category**: format
- **Weight**: aspirational
- **Text**: The finding schema positions the lens citation field (Via:, Lens:, or
  equivalent) such that omission is structurally visible -- specifically, as the
  second column in the finding table, before Severity and Owner. This structural
  placement achieves 100% lens coverage across all findings without relying on
  prose instruction or per-finding discipline. C-14 requires 50%+ coverage; C-19
  requires 100% coverage enforced by column position.
- **Pass condition**: (1) The lens citation field appears as the second column in
  the finding table, before Severity and Owner in the schema. (2) 100% of findings
  in the run carry a lens citation value -- no finding has a blank or omitted lens
  field. A schema that satisfies C-14 at 50%+ but does not place the lens field
  second does not satisfy C-19. A schema that places the field second but has any
  blank lens values does not satisfy C-19.
- **Source**: V-02 R5 (Via-Field-Second Finding Schema) -- Via: positioned as
  SECOND field in every finding row (before Severity, before Owner), making
  omission structurally visible and achieving 100% coverage by schema enforcement.
  C-14 was designed to reward 50%+ finding-level lens citation; C-19 rewards the
  encoding discipline that makes the 50% floor structurally impossible to miss.
  V-01 R5 fails C-19: its finding schema is ID / Finding / Severity / Owner /
  Resolution Path with no Via: field.

---

## Criterion Summary

| ID   | Text (short)                         | Weight        | Category    |
|------|--------------------------------------|---------------|-------------|
| C-01 | Stage identity and labeling          | essential     | format      |
| C-02 | Role-loaded perspective              | essential     | correctness |
| C-03 | ROB document format compliance       | essential     | format      |
| C-04 | Actionable findings (2x per stage)   | essential     | depth       |
| C-05 | Explicit go/no-go in tpm stage       | essential     | correctness |
| C-06 | Cross-stage coherence                | recommended   | depth       |
| C-07 | Risk register structure in tpm       | recommended   | depth       |
| C-08 | Spire cascade tracing                | recommended   | coverage    |
| C-09 | Inter-stage blocker detection        | aspirational  | depth       |
| C-10 | Cross-cutting theme elevation        | aspirational  | depth       |
| C-11 | Phase gate contracts                 | aspirational  | depth       |
| C-12 | Dual-direction traceability          | aspirational  | depth       |
| C-13 | Named blocker format                 | aspirational  | correctness |
| C-14 | Lens-anchored findings               | aspirational  | correctness |
| C-15 | Column-invariant verdict format      | aspirational  | format      |
| C-16 | Synthesis residual open items        | aspirational  | depth       |
| C-17 | Stage-maintained finding ledger      | aspirational  | depth       |
| C-18 | Role orientation frame citation      | aspirational  | correctness |
| C-19 | Schema-enforced lens coverage        | aspirational  | format      |

---

## Scoring Model

| Tier | Criteria | Max pts (tier) | Max per criterion | ++ | + | o |
|------|----------|----------------|-------------------|----|---|---|
| Essential | C-01 to C-05 | 60 | 12 | 12 | 12* | 0 |
| Recommended | C-06 to C-08 | 30 | 10 | 10 | 7 | 0 |
| Aspirational | C-09 to C-19 | 22 | 2 | 2 | 1 | 0 |

*Essential + = PASS. Both + and ++ earn full points for essential criteria.

**Total max: 60 + 30 + 22 = 112**

Any essential failure = not golden regardless of composite score.

---

## Example Score Calculations

**Baseline golden** -- all essential pass, 2/3 recommended, 0/11 aspirational:

```
composite = (5/5 * 60) + (2/3 * 30) + (0/11 * 22)
          = 60 + 20 + 0
          = 80
```

Golden threshold met (all essential pass, composite = 80).

---

**V-01 R3** -- all essential ++, all recommended ++,
C-10/C-14 at ++, C-09/C-12/C-13 at +, C-11/C-15/C-16/C-17/C-18/C-19 at o:

```
aspirational = 1 + 2 + 0 + 1 + 1 + 2 + 0 + 0 + 0 + 0 + 0 = 7
composite    = 60 + 30 + 7 = 97
```

---

**V-02 R3** -- all essential ++, all recommended ++,
C-09/C-10/C-12/C-13/C-15/C-16 at ++, C-11/C-14/C-17/C-18/C-19 at o:

```
aspirational = 2 + 2 + 0 + 2 + 2 + 0 + 2 + 2 + 0 + 0 + 0 = 12
composite    = 60 + 30 + 12 = 102
```

Path: verdict registry (C-15) + Finding Registry (C-12, C-16). No stage-maintained
ledger (C-17=o), no orientation frame citation (C-18=o), no Via: second-column
schema (C-19=o).

---

**V-03 R3** -- all essential ++, all recommended ++,
C-09/C-10/C-12/C-13/C-16/C-17 at ++, C-11/C-14/C-15/C-18/C-19 at o:

```
aspirational = 2 + 2 + 0 + 2 + 2 + 0 + 0 + 2 + 2 + 0 + 0 = 12
composite    = 60 + 30 + 12 = 102
```

Path: residual-accumulator ledger (C-17) + Residual Open Items (C-16). No verdict
table (C-15=o), no lens fields (C-14=o). Reaches 102 via a structurally different
mechanism than V-02.

---

**V-01 R5** -- all essential ++, all recommended ++,
C-09/C-11/C-12/C-13/C-16/C-18 at ++, C-10 at +,
C-14/C-15/C-17/C-19 at o:

```
aspirational = 2 + 1 + 2 + 2 + 2 + 0 + 0 + 2 + 0 + 2 + 0 = 13
composite    = 60 + 30 + 13 = 103
```

Path: phase gate contracts (C-11) + orientation frame citation (C-18). No Via:
field in finding schema (C-14=o, C-19=o). C-18 ++ is the R5 addition; C-17 and
C-19 remain unreached.

---

**V-02 R5** -- all essential ++, all recommended ++,
C-09/C-10/C-12/C-13/C-14/C-15/C-16/C-19 at ++, C-11/C-17/C-18 at o:

```
aspirational = 2 + 2 + 0 + 2 + 2 + 2 + 2 + 2 + 0 + 0 + 2 = 18
composite    = 60 + 30 + 18 = 108
```

Path: verdict registry (C-15) + Finding Registry (C-12, C-16) + Via: second-column
schema (C-14, C-19). C-19 ++ is the R5 addition. No phase gate contracts (C-11=o),
no orientation frame citation (C-18=o), no stage-maintained ledger (C-17=o).

---

**Perfect score** -- all essential ++, 3/3 recommended ++, 11/11 aspirational ++:

```
composite = 60 + 30 + 22 = 112
```
