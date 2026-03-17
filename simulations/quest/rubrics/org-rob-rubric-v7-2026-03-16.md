Written to `simulations/quest/rubrics/org-rob-rubric-v7-2026-03-16.md`.

---

**Three new criteria extracted from R7:**

**C-21 -- Inertia Anchor** (depth, aspirational)
Pre-stage INERTIA BASELINE named once, propagated as Inertia Impact in ledger rows, Inertia Link in risk register, Inertia Pressure Summary in synthesis. Status-quo displacement tracked end-to-end structurally, not via prose assertion.

**C-22 -- Extensible Violation Taxonomy** (format, aspirational)
VIOLATION-09+ present in schema, signaling the taxonomy is open-ended. Every future structural requirement gets a VIOLATION-NN identifier. Requires C-20. A taxonomy capped at VIOLATION-08 does not satisfy C-22.

**C-23 -- Self-Documenting Violation Rationale** (format, aspirational)
At least 3 VIOLATION-NN entries include a consequence paragraph -- *why* the anti-pattern degrades the review, not just *what* it is. Requires C-20. Independent of C-22.

**Scoring changes:**

| | v6 | v7 |
|---|---|---|
| Aspirational criteria | C-09--C-20 (12) | C-09--C-23 (15) |
| Aspirational max | 24 | **30** |
| Total max | 114 | **120** |

The R7 perfect-round note is preserved: all five variations at 114/114 under v6, rescoring under v7 in progress. The violation taxonomy now has three independent structural properties -- named (C-20), extensible (C-22), self-documenting (C-23) -- achievable independently or in combination.
 the taxonomy as closed does not satisfy C-22, even if it satisfies C-20.

**C-23 -- Self-Documenting Violation Rationale** (format, aspirational)

The explanatory rationale pattern: each VIOLATION-NN entry includes a paragraph
explaining WHY the anti-pattern undermines review quality -- not just WHAT the
anti-pattern is. The rationale addresses downstream consequences or degraded
outcomes rather than restating the rule. Self-documenting violations reduce
borderline-compliant output without changing enforcement structure. C-23 requires
C-20 (violation taxonomy must exist before rationale can be added to it).

**Scoring changes:**

| | v6 | v7 |
|---|---|---|
| Aspirational criteria | C-09--C-20 (12) | C-09--C-23 (15) |
| Aspirational max | 24 | 30 |
| Total max | 114 | **120** |

**R7 scores under v6 (all five variations at maximum):**

All five R7 variations reached 114/114 under v6. R7 is the convergence round:
once C-20 (named violation taxonomy) is satisfied, the other 19 criteria are
structurally assured by the cumulative mechanisms from R1--R6. R7 is being
rescored under v7 to establish which variations achieve C-21, C-22, and C-23.

### v6 (2026-03-16) -- C-20 from R6

C-20 (Named Violation Taxonomy) extracted from V-03 R6. V-03 R6 scores 114;
V-01 and V-02 R6 score 108 and 107 (C-20=o). Total max bumped from 112 to 114.

### v5 (2026-03-15) -- C-18 and C-19 from R5

C-18 (Role Orientation Frame Citation) from V-01 R5; C-19 (Schema-Enforced Lens
Coverage) from V-02 R5. Total max bumped from 108 to 112.

### v4 (2026-03-15) -- C-17 from R3

C-17 (Stage-Maintained Finding Ledger) from V-03 R3. Total max bumped from 106 to 108.

### v3 (2026-03-14) -- C-14 through C-16 from R2

C-14, C-15, C-16 extracted from R2 divergence. Total max bumped from 100 to 106.

### v2 (2026-03-14) -- C-09 through C-13 from R1

C-09 through C-13 extracted from V-04 R1. Total max bumped from 90 to 100.

### v1 (2026-03-14) -- Initial rubric

C-01 through C-08 (essential and recommended tier only).

---

## Scoring Framework

| Tier | Criteria | Max pts | ++ | + | o |
|------|----------|---------|----|---|---|
| Essential | C-01--C-05 | 60 | 12 | 12* | 0 |
| Recommended | C-06--C-08 | 30 | 10 | 7 | 0 |
| Aspirational | C-09--C-23 | 30 | 2 | 1 | 0 |

*Essential + = PASS. Both + and ++ earn full points for essential criteria.

**Total max: 60 + 30 + 30 = 120**

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
  .craft/roles/ -- not a generic review. The role orientation, lens, and
  expertise shape which concerns are raised.
- **Pass condition**: At least one finding per stage is grounded in the loaded
  role's documented lens (e.g., a PM flags adoption risk, a TPM flags schedule
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
  loaded role (.craft/roles/) that triggered it. Role-loading is verifiable at
  the finding level, not just at the stage level. A finding that could have been
  written by any role does not clear C-14, even if the stage header names a role.
- **Pass condition**: At least 50% of findings across the run include a Lens:,
  Via:, or equivalent field naming the specific role lens item that motivated the
  concern (e.g., "Lens: tpm.lens.schedule-risk" or "Via: orientation.frame --
  delivery velocity"). The cited lens item must exist in the loaded role file.
- **Source**: R2 scorecard -- both V-01 and V-02 scored + on C-02 but neither
  reached ++. The gap: no per-finding lens citation field was required. The ++
  path on C-02 requires finding-level lens enforcement, which C-14 now rewards
  explicitly.

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
  column invariant." C-15 rewards the encoding that makes verdict omission
  structurally impossible.

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
  Items section flags any Acknowledged As = empty." V-01 achieved C-06 ++ via
  Dual-Direction Check table instead. C-16 rewards the dedicated residual-items
  inventory as a distinct structural property separate from C-09 and C-12.

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
- **Source**: V-03 R3 (Residual-Accumulator Model) -- achieves C-12 ++ via each
  stage citing ledger row number and filling Resolved By + Resolution, and C-16 ++
  via Residual Open Items filtering ledger rows where Resolved By = (pending). V-02
  Finding Registry (managed centrally at synthesis) does not satisfy C-17.

---

### C-18 -- Role Orientation Frame Citation
- **Category**: correctness
- **Weight**: aspirational
- **Text**: Each stage cites the specific `orientation.frame` (or equivalent named
  field) from the loaded .craft/roles/ file in its stage-level ROLE: block. Role
  loading is verifiable at the stage level independently of per-finding Via: fields
  (C-14). A stage that names the role without surfacing the governing orientation
  frame satisfies C-02 but does not satisfy C-18.
- **Pass condition**: At least 2 stages in the run include a ROLE: line (or
  equivalent labeled block) that cites a specific named field from the loaded role
  file -- e.g., `orientation.frame`, `lens.primary`, or equivalent -- by field name
  and value. The cited field must be traceable to the .craft/roles/ file. Naming
  the role alone (e.g., "Role: tpm") does not satisfy this criterion.
- **Source**: V-01 R5 -- `orientation.frame` extracted from .craft/roles/ and cited
  in ROLE: line of each stage, enabling per-stage verification of the correct lens.
  C-14 anchors lens citation to findings; C-18 anchors it to stage identity.

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
  second does not satisfy C-19.
- **Source**: V-02 R5 -- Via: positioned as SECOND field in every finding row,
  making omission structurally visible and achieving 100% coverage by schema
  enforcement. V-01 R5 fails C-19: its finding schema has no Via: field.

---

### C-20 -- Named Violation Taxonomy
- **Category**: format
- **Weight**: aspirational
- **Text**: Every structural rule in the schema has a corresponding named violation
  type -- VIOLATION-01, VIOLATION-02, etc. -- with an explicit identifier and a
  description of the anti-pattern it prohibits. Rules are expressed in both
  positive form ("X must be present") and prohibition form ("Omitting X is
  VIOLATION-NN: [description]"). Named violations make anti-pattern detection
  mechanistic: any reviewer can ask "was VIOLATION-NN committed?" independently
  of prose interpretation. A schema that states requirements positively but has
  no enumerated violation taxonomy does not satisfy C-20 regardless of how many
  structural rules it contains.
- **Pass condition**: At least 5 distinct structural rules in the schema each have
  a corresponding named VIOLATION-NN identifier (or equivalent enumerated
  anti-pattern label) with a description of the violation. Violation identifiers
  must be distinct (no two rules share an ID) and referenced in the pass/fail
  language of the schema (e.g., "A blank Via: cell is VIOLATION-03"). A schema
  with prohibition language that does not assign enumerated IDs to violations does
  not satisfy this criterion.
- **Source**: V-03 R6 (Prohibition-Mode Enforcement) -- all structural rules
  expressed as named VIOLATION types (VIOLATION-01 through VIOLATION-08+), making
  the schema self-policing. VIOLATION-08 prohibits cross-cutting themes named only
  in a single stage (drives C-10 ++ -- the mechanism that distinguishes V-03 R6
  at ++ from V-02 R6 at + on C-10). No R1--R5 variation enumerated violations by
  name and number. C-20 is structurally independent of C-19 and C-15: V-01 and
  V-02 R6 each achieve both C-18 and C-19 without naming violations.

---

### C-21 -- Inertia Anchor
- **Category**: depth
- **Weight**: aspirational
- **Text**: A named inertia baseline element is written as a first-class schema
  element before Stage 1 runs and propagates its identity through every downstream
  structural artifact: as an Inertia Impact column in the finding ledger, as an
  Inertia Link field in the risk register, and as an Inertia Pressure Summary
  section in synthesis. Status-quo displacement is tracked end-to-end without
  prose assertion -- each structural position that carries inertia data names the
  pre-stage baseline by ID. A schema that raises inertia concerns in finding prose
  but does not define a named baseline element propagated to at least 2 structural
  positions does not satisfy C-21.
- **Pass condition**: (1) A named INERTIA BASELINE (or equivalent labeled element)
  appears before Stage 1, defining the status-quo position being displaced.
  (2) At least 2 downstream structural positions reference this baseline by name
  or ID -- e.g., Inertia Impact in ledger rows, Inertia Link in risk register
  entries, or equivalent named fields. (3) Synthesis includes an Inertia Pressure
  Summary (or equivalent labeled section) that traces displacement from the named
  baseline. Inertia commentary embedded in finding prose without a pre-stage
  baseline element does not satisfy this criterion.
- **Source**: R7 scorecards -- Inertia Anchor pattern first appeared as a
  first-class schema element in R7. Prior rounds tracked inertia concerns via
  finding prose or risk register entries without a named pre-stage baseline.
  C-21 rewards the structural discipline of seeding a named baseline before any
  stage runs and requiring every inertia-bearing artifact to carry a reference
  to that baseline, making displacement measurable across the review timeline.

---

### C-22 -- Extensible Violation Taxonomy
- **Category**: format
- **Weight**: aspirational
- **Text**: The violation taxonomy is designed as an open-ended series: VIOLATION
  numbering continues beyond the initial VIOLATION-01..08 set, and the schema
  commits to assigning a named VIOLATION-NN to every new structural requirement
  added in the future. VIOLATION-09 or higher appearing in the schema is the
  canonical signal of extensibility. A schema that reaches VIOLATION-08 and treats
  the taxonomy as closed -- adding new requirements in prose form without extending
  the violation series -- does not satisfy C-22, even if it satisfies C-20. C-22
  requires C-20 (violation taxonomy must exist before it can be extensible).
- **Pass condition**: (1) The violation taxonomy includes at least one VIOLATION-09
  or higher identifier (i.e., the series extends beyond the initial eight).
  (2) The schema makes explicit -- either by statement or by structural pattern --
  that future structural requirements will receive VIOLATION-NN identifiers rather
  than prose prohibitions. A schema that names VIOLATION-09 for a specific new rule
  satisfies (1); a schema that includes an open-ended VIOLATION-09+ slot or states
  "new requirements extend this taxonomy" satisfies (2). Both conditions must hold.
- **Source**: R7 scorecards -- VIOLATION-09 first appeared as an extensible
  taxonomy slot in R7, signaling that the violation taxonomy is architecturally
  open-ended. V-03 R6 defined VIOLATION-01..08 as a complete set; R7 introduced
  the extensibility principle. C-22 is structurally independent of C-23: a schema
  can have VIOLATION-09+ without explanatory rationale per violation.

---

### C-23 -- Self-Documenting Violation Rationale
- **Category**: format
- **Weight**: aspirational
- **Text**: Each VIOLATION-NN entry includes a rationale paragraph explaining WHY
  the anti-pattern undermines review quality -- not just WHAT the anti-pattern is.
  The rationale addresses downstream consequences or degraded outcomes ("without
  named ownership, downstream stages cannot certify resolution") rather than
  restating the rule ("owner field must be non-blank"). Self-documenting violations
  reduce borderline-compliant output without changing enforcement structure: a
  reviewer who understands why VIOLATION-05 matters will not produce technically-
  compliant-but-vacuous exit conditions. A violation entry that states the
  prohibition and anti-pattern description but provides no consequence reasoning
  does not satisfy C-23. C-23 requires C-20 (violation taxonomy must exist first).
- **Pass condition**: At least 3 VIOLATION-NN entries in the taxonomy each include
  a rationale paragraph (distinct from the anti-pattern description) that: (1)
  states a consequence or degraded outcome caused by the violation, (2) does not
  merely restate the rule in different words. A rationale that says "this matters
  because the field is required" does not satisfy the consequence requirement. A
  rationale that says "without named escalation IDs, the receiving stage cannot
  distinguish new findings from inherited ones, breaking dual-direction
  traceability" satisfies the consequence requirement.
- **Source**: R7 scorecards -- self-documenting violation rationale first appeared
  in R7. V-03 R6 named violations with anti-pattern descriptions but without
  consequence reasoning; R7 variations enriched each VIOLATION-NN with explanatory
  paragraphs. C-23 is independent of C-22: a schema can have thorough rationale
  for VIOLATION-01..08 without extending to VIOLATION-09+. The combination C-20 ++
  C-22 ++ C-23 produces a violation taxonomy that is named, extensible, and
  self-documenting.

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
| C-20 | Named violation taxonomy             | aspirational  | format      |
| C-21 | Inertia anchor                       | aspirational  | depth       |
| C-22 | Extensible violation taxonomy        | aspirational  | format      |
| C-23 | Self-documenting violation rationale | aspirational  | format      |

---

## Scoring Model

| Tier | Criteria | Max pts (tier) | Max per criterion | ++ | + | o |
|------|----------|----------------|-------------------|----|---|---|
| Essential | C-01 to C-05 | 60 | 12 | 12 | 12* | 0 |
| Recommended | C-06 to C-08 | 30 | 10 | 10 | 7 | 0 |
| Aspirational | C-09 to C-23 | 30 | 2 | 2 | 1 | 0 |

*Essential + = PASS. Both + and ++ earn full points for essential criteria.

**Total max: 60 + 30 + 30 = 120**

Any essential failure = not golden regardless of composite score.

---

## Example Score Calculations

**Baseline golden** -- all essential pass, 2/3 recommended, 0/15 aspirational:

```
composite = (5/5 * 60) + (2/3 * 30) + (0/15 * 30)
          = 60 + 20 + 0
          = 80
```

Golden threshold met (all essential pass, composite = 80).

---

**V-01 R3** -- all essential ++, all recommended ++,
C-10/C-14 at ++, C-09/C-12/C-13 at +, C-11/C-15--C-23 at o:

```
aspirational = 1 + 2 + 0 + 1 + 1 + 2 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 7
composite    = 60 + 30 + 7 = 97
```

---

**V-02 R3** -- all essential ++, all recommended ++,
C-09/C-10/C-12/C-13/C-15/C-16 at ++, C-11/C-14/C-17--C-23 at o:

```
aspirational = 2 + 2 + 0 + 2 + 2 + 0 + 2 + 2 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 12
composite    = 60 + 30 + 12 = 102
```

Path: verdict registry (C-15) + Finding Registry (C-12, C-16). No stage-maintained
ledger (C-17=o), no orientation frame citation (C-18=o), no Via: second-column
schema (C-19=o), no violation taxonomy (C-20=o), no inertia anchor (C-21=o),
no extensible taxonomy (C-22=o), no violation rationale (C-23=o).

---

**V-03 R3** -- all essential ++, all recommended ++,
C-09/C-10/C-12/C-13/C-16/C-17 at ++, C-11/C-14/C-15/C-18--C-23 at o:

```
aspirational = 2 + 2 + 0 + 2 + 2 + 0 + 0 + 2 + 2 + 0 + 0 + 0 + 0 + 0 + 0 = 12
composite    = 60 + 30 + 12 = 102
```

Path: residual-accumulator ledger (C-17) + Residual Open Items (C-16). No verdict
table (C-15=o), no lens fields (C-14=o). Reaches 102 via a structurally different
mechanism than V-02.

---

**V-01 R5** -- all essential ++, all recommended ++,
C-09/C-11/C-12/C-13/C-16/C-18 at ++, C-10 at +,
C-14/C-15/C-17/C-19--C-23 at o:

```
aspirational = 2 + 1 + 2 + 2 + 2 + 0 + 0 + 2 + 0 + 2 + 0 + 0 + 0 + 0 + 0 = 13
composite    = 60 + 30 + 13 = 103
```

Path: phase gate contracts (C-11) + orientation frame citation (C-18). No Via:
field in finding schema (C-14=o, C-19=o), no stage ledger (C-17=o), no violation
taxonomy (C-20=o), no inertia anchor (C-21=o), no extensible taxonomy (C-22=o),
no violation rationale (C-23=o). C-18 ++ is the R5 addition.

---

**V-02 R5** -- all essential ++, all recommended ++,
C-09/C-10/C-12/C-13/C-14/C-15/C-16/C-19 at ++, C-11/C-17/C-18/C-20--C-23 at o:

```
aspirational = 2 + 2 + 0 + 2 + 2 + 2 + 2 + 2 + 0 + 0 + 2 + 0 + 0 + 0 + 0 = 18
composite    = 60 + 30 + 18 = 108
```

Path: verdict registry (C-15) + Finding Registry (C-12, C-16) + Via: second-column
schema (C-14, C-19). C-19 ++ is the R5 addition. No phase gate contracts (C-11=o),
no orientation frame citation (C-18=o), no stage ledger (C-17=o), no violation
taxonomy (C-20=o), no inertia anchor (C-21=o), no extensible taxonomy (C-22=o),
no violation rationale (C-23=o).

---

**V-01 R6** -- all essential ++, all recommended ++,
C-09/C-10/C-12/C-13/C-14/C-15/C-16/C-18/C-19 at ++,
C-11/C-17/C-20--C-23 at o:

```
aspirational = 2 + 2 + 0 + 2 + 2 + 2 + 2 + 2 + 0 + 2 + 2 + 0 + 0 + 0 + 0 = 18
composite    = 60 + 30 + 18 = 108
```

Path: V-02 R5 base (C-19++) + Frame: in ROLE block (C-18++). First variation to
achieve both C-18 and C-19 simultaneously. No phase gate contracts (C-11=o), no
stage ledger (C-17=o), no violation taxonomy (C-20=o), no inertia anchor (C-21=o),
no extensible taxonomy (C-22=o), no violation rationale (C-23=o).

---

**V-02 R6** -- all essential ++, all recommended ++,
C-09/C-11/C-12/C-13/C-14/C-16/C-18/C-19 at ++, C-10 at +,
C-15/C-17/C-20--C-23 at o:

```
aspirational = 2 + 1 + 2 + 2 + 2 + 2 + 0 + 2 + 0 + 2 + 2 + 0 + 0 + 0 + 0 = 17
composite    = 60 + 30 + 17 = 107
```

Path: V-01 R5 base (C-11++, C-18++) + Via: as second column addition (C-19++).
C-10 at + because cross-cutting theme detection remains manually identified (no
VIOLATION-08 to enforce document-level surfacing). No column-invariant verdict
table (C-15=o), no stage ledger (C-17=o), no violation taxonomy (C-20=o), no
inertia anchor (C-21=o), no extensible taxonomy (C-22=o), no violation rationale
(C-23=o).

---

**V-03 R6** -- all essential ++, all recommended ++,
all aspirational C-09--C-20 at ++, C-21--C-23 at o:

```
aspirational = 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 0 + 0 + 0 = 24
composite    = 60 + 30 + 24 = 114
```

Path: V-05 R5 base (all C-09--C-17 ++) + VIOLATION-01 (C-18++) + VIOLATION-02/03
(C-19++) + full violation taxonomy (C-20++). VIOLATION-08 elevates C-10 from + to
++ by prohibiting single-stage-only theme elevation. First variation to achieve
perfect score under v6. Inertia anchor pattern had not yet emerged (C-21=o);
violation taxonomy closed at VIOLATION-08 (C-22=o); no consequence rationale per
violation (C-23=o).

---

**R7 all variations (under v6)** -- five variations at 114/114.

R7 is the convergence round: once C-20 is satisfied, the other 19 criteria are
structurally assured. Rescoring R7 under v7 is in progress to assign C-21, C-22,
and C-23 ratings per variation. R8's natural question: does the inertia axis (C-21)
belong in recommended once it stabilizes across all variations?

---

**Perfect score (v7)** -- all essential ++, 3/3 recommended ++, 15/15 aspirational ++:

```
composite = 60 + 30 + 30 = 120
```
