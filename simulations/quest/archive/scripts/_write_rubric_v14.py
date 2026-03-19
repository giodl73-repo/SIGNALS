
# Script to write v14 rubric
import pathlib

dest = pathlib.Path("C:/src/sim/simulations/quest/rubrics/scout-size-rubric-v14-2026-03-17.md")

content = """\
Written to `simulations/quest/rubrics/scout-size-rubric-v14-2026-03-17.md`.

---

## v14 summary

**3 new criteria extracted from R13 excellence signals. Aspirational denominator: 30 -> 33.**

| ID | Name | Source | Axis | Relationship |
|----|------|--------|------|-------------|
| C-39 | PHASE SEALED blocks carry role attribution | V-05 R13 | Accountability | C-38 extension -- SEALED block present (C-38) != role-attributed SEALED block (C-39) |
| C-40 | Relational-constraint fields enumerate cross-field disqualifying form | V-05 R13 | Constraint precision | C-36 extension -- vocabulary tag present (C-36) != relational failure class named (C-40) |
| C-41 | Phase 2 non-access rule enumerates prohibited gap candidates | V-05 R13 | Structural disqualification | C-20 complement -- closure mesh prevents field bleed (C-20); C-41 prevents basis-negation gaps |

**v13 champion achieved.** V-05 R13 scored **100.00** (30/30 aspirational under v13), confirming the v13 ceiling.

**R13 scores under v14** (retroactive):

| Variation | Asp. (/33) | Score | C-39 | C-40 | C-41 |
|-----------|-----------|-------|------|------|------|
| V-05 | 33/33 | 100.00 | PASS | PASS | PASS |
| V-02 | 29/33 | 98.79 | FAIL | PASS | FAIL |
| V-04 | 29/33 | 98.79 | FAIL | FAIL | FAIL |
| V-01 | 28/33 | 98.48 | FAIL | FAIL | FAIL |
| V-03 | 28/33 | 98.48 | FAIL | FAIL | FAIL |

**v14 champion**: V-05 R13 (100.00 -- satisfies C-39 + C-40 + C-41 as the source variation).
**Observation**: C-40 retroactively promotes V-02 to 29/33 alongside V-04. V-02's Tier-Destination tag
`[FAIL: same as current, MODERATE, non-vocabulary...]` included the cross-field disqualifying form,
satisfying C-40 even though V-02 was not designed to target it.

**Target for R14**: Extract new patterns beyond the V-05 ceiling. Current ceiling criteria:
role-attributed phase seals (C-39), relational disqualifying forms on dual-constraint fields (C-40),
Phase 2 structural gap disqualification list (C-41).

**Scoring model updated**: `aspirational_pass / 33 * 10` (was `/30`).

**C-29 scope updated** to include C-39, C-40, C-41 in the structural criteria set.

---

### Rationale for C-39, C-40, C-41

- **C-39** completes the phase governance *accountability* axis. C-38 requires SEALED blocks at each
  phase boundary -- a completion-confirmation mechanism. C-39 adds role attribution to each block:
  the analyst or role chartered to own the phase must appear as the named confirming agent at the
  seal. Without attribution, a SEALED block is a checklist without an owner; with attribution, it is
  a signed handoff. The charter declares the role; the PHASE SEALED block confirms the role acted.
  V-05 R13 is the first variation to attribute each seal: "The Inertia Analyst confirms ALL before
  Phase 1 opens", "The Sizing Analyst confirms ALL", "The Risk Assessor confirms ALL".

- **C-40** closes the gap between C-36 compliance in format and C-36 compliance in content. C-36
  requires every vocabulary-constrained field to carry a `[FAIL: ...]` tag. Some fields carry a
  second constraint beyond vocabulary membership -- they must also satisfy a relational condition
  (e.g., Tier-Destination must differ from the current complexity tier). A tag that enumerates only
  vocabulary failures ("MODERATE, non-vocabulary") is well-formed under C-36 but incomplete: it
  misses the relational failure class ("same tier as current"). V-04 R13 reached 29/30 under v13
  with C-36 PARTIAL precisely because its Tier-Destination used `[must differ: ...]` phrasing rather
  than `[FAIL: same tier as current, MODERATE, non-vocabulary...]`. V-05 is the first to enumerate
  the relational disqualifying form as a distinct failure class. C-40 makes this distinction
  a criterion in its own right.

- **C-41** extends structural gap prevention to Phase 2's confidence analysis. C-20 prevents
  cross-phase field bleed by requiring bilateral closure guards. C-28/C-29/C-30 require the
  per-criterion self-check to carry exact disqualifying forms. C-41 addresses a different failure
  mode in Phase 2: basis-negation gaps -- gap statements that contradict or merely echo the stated
  confidence basis rather than extending it with genuine unknowns. V-05 R13 introduces a positive
  disqualification list in Phase 2's non-access rule, explicitly enumerating all prohibited gap
  candidate forms. By naming what would fail as a gap, the output prevents disqualified forms
  structurally rather than relying on behavioral restraint. V-05 is the first variation to include
  this mechanism.

**R13 scores under v14:**

| Variation | Asp. (/33) | Score | Criteria advanced |
|-----------|-----------|-------|------------------|
| V-05 (role-attributed SEALED + relational [FAIL:] tag + Phase 2 gap disqualification) | 33/33 | 100.00 | C-39 + C-40 + C-41 |
| V-02 (C-36 PASS, Tier-Destination tag includes relational disqualifier) | 29/33 | 98.79 | C-36 + C-40 |
| V-04 (C-37 + C-38 PASS) | 29/33 | 98.79 | C-37 + C-38 |
| V-01 | 28/33 | 98.48 | C-37 |
| V-03 | 28/33 | 98.48 | C-38 |

No R13 variation other than V-05 achieves all three new criteria simultaneously. The v14 ceiling is
set by V-05; R14 variations must introduce new patterns to raise the bar to v15.

---

## Purpose

This rubric scores the output of the `scout-size` skill against 41 criteria grouped into three
tiers: Essential (must pass), Recommended (output is better with these), and Aspirational
(raise the bar). A scorecard runner evaluates each criterion as PASS, PARTIAL, or FAIL and
computes a composite score.

---

## Essential Criteria (60 points total)

### C-01 -- Complexity tier uses controlled vocabulary
- **Weight**: essential
- **Category**: correctness
- **Description**: Output assigns exactly one of four vocabulary terms: LOW / MEDIUM / HIGH / XL.
  No other phrasing is acceptable. "MODERATE", "medium-high", "3 out of 5", "complex", or any
  other term are hard fails. The vocabulary is load-bearing -- downstream skills (program-plan,
  etc.) parse it.
- **Pass condition**: Output contains exactly one of: LOW / MEDIUM / HIGH / XL as the complexity
  tier label. Any other term or phrasing fails regardless of whether the intent is correct.

### C-02 -- Timeline signal is a sprint range with lower and upper bound
- **Weight**: essential
- **Category**: correctness
- **Description**: Output gives a sprint range estimate (e.g., "3-5 sprints") with both a lower
  and an upper bound. Calendar-based estimates ("Q3", "by end of quarter") and point estimates
  ("3 sprints") are hard fails. A range communicates the inherent uncertainty of sizing; a
  single number implies false precision.
- **Pass condition**: Output states a timeline as a sprint range with both a lower and an upper
  bound (e.g., "2-4 sprints"). A calendar date, point estimate, or any format other than N-M
  sprints fails.

### C-03 -- Surface area is quantified by integration points
- **Weight**: essential
- **Category**: correctness
- **Description**: Surface area section identifies discrete integration points (APIs, hooks,
  namespaces, data stores, UI surfaces, external systems). Must be a count or enumerated list
  -- not a vague qualifier like "moderate surface area".
- **Pass condition**: Output names or counts at least 2 distinct integration points, or
  explicitly states 0-1 with reasoning.

### C-04 -- Inertia check is present and names the workaround cost
- **Weight**: essential
- **Category**: coverage
- **Description**: Output includes an explicit inertia check that names what teams currently
  do without this feature (the workaround) and characterizes its cost (time, error rate,
  manual effort, missing capability). Absence of this section is a hard fail -- it is the
  signal's differentiator from a raw estimate.
- **Pass condition**: A clearly labeled inertia check section or paragraph identifies the
  current workaround and states at least one cost dimension.

### C-05 -- Confidence level is stated with basis
- **Weight**: essential
- **Category**: depth
- **Description**: Output states a confidence level (percentage, tier, or LOW/MED/HIGH label)
  AND gives the primary reason for that level (e.g., "HIGH confidence -- surface area
  well-understood from existing flow skill", "LOW confidence -- cross-service dependencies
  uncharted"). Confidence without basis is not actionable.
- **Pass condition**: Confidence level is present AND at least one sentence explains why that
  level was assigned.

---

## Recommended Criteria (30 points total)

### C-06 -- Team-size signal names required specializations
- **Weight**: recommended
- **Category**: depth
- **Description**: Team-size signal goes beyond headcount to name the types of specialists
  required (e.g., "1 backend + 1 infra", not just "2 engineers"). This lets program-plan
  route work correctly.
- **Pass condition**: Team-size signal identifies at least one role or specialization, not
  just a number.

### C-07 -- Complexity rating is justified with at least one driver
- **Weight**: recommended
- **Category**: depth
- **Description**: The complexity tier (C-01) is accompanied by the primary driver that
  determined the rating -- e.g., "HIGH because of distributed transaction boundary", "LOW
  because isolated namespace with no shared state". Bare tier labels are less useful
  downstream.
- **Pass condition**: At least one sentence following or inline with the complexity tier
  names what pushed it to that level.

### C-08 -- AMEND instructions modify the stated output, not the process
- **Weight**: recommended
- **Category**: behavior
- **Description**: When an AMEND directive is present (adjust confidence thresholds or focus
  on a complexity dimension), the output reflects the amendment in its content -- e.g., a
  revised confidence level, or expanded analysis of the named dimension. The skill should
  not just acknowledge the amendment; it should change the artifact.
- **Pass condition**: If AMEND is invoked, at least one substantive change in the output
  (different tier, revised confidence, expanded section) can be traced to the amendment.
  If no AMEND is present, criterion is scored as pass by default.

---

## Aspirational Criteria (10 points total)

### C-09 -- Sizing signal explicitly scopes what is NOT included
- **Weight**: aspirational
- **Category**: depth
- **Description**: Output states at least one thing the sizing does NOT cover (out-of-scope
  sub-systems, deferred complexity, assumptions made). This prevents silent misreads when
  program-plan consumes the signal.
- **Pass condition**: At least one explicit exclusion, assumption, or out-of-scope boundary
  is named.

### C-10 -- Inertia check includes a break-even signal
- **Weight**: aspirational
- **Category**: depth
- **Description**: Beyond naming the workaround cost, the output estimates when building the
  feature pays off relative to continued workaround cost -- even as a rough qualitative signal
  ("break-even at ~4 uses/week", "never breaks even if adoption stays below 3 teams"). This
  is the highest-value form of the inertia check for investment decisions.
- **Pass condition**: Output contains a break-even estimate or explicitly states that
  break-even cannot be assessed and why.

### C-11 -- Each named specialization states its implementation ownership
- **Weight**: aspirational
- **Category**: depth
- **Description**: Team-size signal goes beyond naming roles (C-06) to state what each
  specialization owns during implementation -- e.g., "1 backend (owns event schema + storage
  layer) + 1 infra (owns deployment pipeline)". Without ownership scope, the role list is
  decorative and program-plan still needs a follow-up conversation to assign work.
- **Pass condition**: At least one named specialization includes a description of its
  implementation scope or ownership area.

### C-12 -- Confidence section names specific unknowns that would change the rating
- **Weight**: aspirational
- **Category**: depth
- **Description**: A confidence basis (C-05) is actionable only when the output also names
  the specific unknowns that, if resolved, would raise or lower the rating -- e.g., "LOW
  confidence; HIGH once cross-service contracts are published." A basis without named unknowns
  leaves the reader unable to close the gap.
- **Pass condition**: At least one concrete unknown is named that would move the confidence
  level if resolved, or output explicitly states no remaining unknowns.

### C-13 -- Closing synthesis integrates signals, not just restates them
- **Weight**: aspirational
- **Category**: depth
- **Description**: Output contains a concluding statement that draws a decision-relevant
  conclusion by cross-referencing two or more signal dimensions -- e.g., "HIGH complexity +
  LOW confidence in dependency map argues for deferral until contracts are published" or
  "LOW surface area + HIGH inertia cost argues for fast-track even at MEDIUM complexity."
  A closing that merely restates each field in sequence is juxtaposition, not synthesis.
- **Pass condition**: At least one sentence cross-references two or more signal dimensions
  (complexity, timeline, confidence, inertia) to produce a directional recommendation or
  decision-relevant observation.

### C-14 -- Open unknowns appear in a dedicated section with typed fields
- **Weight**: aspirational
- **Category**: structure
- **Description**: Naming unknowns inside the confidence basis paragraph makes omissions
  hard to detect. When unknowns appear in a structurally separate section with typed fields
  (Unknown: / Impact: / Movement:), any gap is visually self-evident.
- **Pass condition**: Open unknowns (or an explicit "no open unknowns" declaration) appear
  in a named section or block separate from the confidence basis, with at least one
  field-typed entry or a structured HIGH-confidence fallback statement.

### C-15 -- Synthesis confirms or revises a prior stated hypothesis
- **Weight**: aspirational
- **Category**: depth
- **Description**: A synthesis derived post-hoc from already-populated fields can still be
  juxtaposition dressed as reasoning. When the output commits to a preliminary hypothesis
  earlier and the synthesis explicitly confirms or revises that commitment, the reasoning
  is verifiable -- the model cannot retroactively produce a conclusion that merely echoes
  the inputs.
- **Pass condition**: A preliminary hypothesis or prior estimate appears before the detailed
  analysis sections, and the synthesis section explicitly states whether the hypothesis was
  confirmed, revised, or partially revised, with the dimension that changed.

### C-16 -- AMEND cascades to synthesis when the amended dimension is cited there
- **Weight**: aspirational
- **Category**: behavior
- **Description**: Extension of C-08 and C-13. When an AMEND directive changes a signal
  dimension that is also referenced in the synthesis, the synthesis must be re-evaluated
  to reflect whether the cross-signal conclusion still holds. Acknowledging the AMEND in
  the amended section but leaving the synthesis unchanged is a silent contradiction.
- **Pass condition**: If AMEND is invoked and the amended dimension appears in the synthesis,
  the synthesis conclusion is updated or explicitly reaffirmed in light of the amendment.
  Default pass if no AMEND is present, or if the amended dimension is not cited in the
  synthesis.

### C-17 -- Aspirational sections name their failure mode
- **Weight**: aspirational
- **Category**: depth
- **Description**: For synthesis (C-13) and unknowns (C-12), an output that explicitly
  distinguishes the required form from the anti-pattern demonstrates that the model is not
  passively populating fields but actively enforcing quality. Examples: noting that restating
  sections in sequence is juxtaposition and does not satisfy synthesis; noting that a
  placeholder unknown ("dependencies may exist") does not satisfy the named-unknowns
  requirement.
- **Pass condition**: At least one aspirational section (synthesis or unknowns) contains a
  sentence that names the anti-pattern being avoided or explicitly states what form of
  response would fail the criterion.

### C-18 -- A pre-analysis self-check gate precedes the first dimension section
- **Weight**: aspirational
- **Category**: structure
- **Description**: A self-check confirmation block before the first analysis section ensures
  scope boundary and break-even are resolved as preconditions, not afterthoughts. Without
  this gate, models defer exclusions and break-even until the end or omit them entirely.
  Structural gate, not a section reminder.
- **Pass condition**: A self-check, confirmation block, or pre-flight step appears before the
  first analysis section and requires the model to explicitly address scope boundary (what
  is NOT included) and break-even signal before proceeding. Inline reminders within sections
  do not satisfy this criterion.

### C-19 -- Sections that could receive duplicate field types carry explicit prohibition guards
- **Weight**: aspirational
- **Category**: structure
- **Description**: When a canonical section exists for a field type (e.g., OPEN UNKNOWNS for
  unknowns), adjacent sections that could plausibly receive the same content must carry an
  explicit prohibition rule -- "do not list unknowns here." This makes cross-contamination
  impossible rather than merely unlikely.
- **Pass condition**: When a canonical section exists for a field type, at least one adjacent
  section that could plausibly receive the same content carries an explicit prohibition rule.

### C-20 -- Complete closure mesh: every canonical section is closed bilaterally
- **Weight**: aspirational
- **Category**: structure
- **Description**: Extension of C-19. C-19 requires at least one adjacent section to be
  closed against a canonical field type. C-20 requires every section that could receive a
  canonical field type to be closed from every direction -- no unguarded adjacent section
  remains for any canonical field type.
- **Pass condition**: For every canonical home section (OPEN UNKNOWNS, SCOPE EXCLUSIONS,
  etc.), ALL sections that could plausibly receive the same content carry explicit prohibition
  rules -- no unguarded adjacent section remains for any canonical field type.

### C-21 -- Pre-flight gate elicits a preliminary hypothesis before analysis proceeds
- **Weight**: aspirational
- **Category**: structure
- **Description**: Folds the hypothesis commitment into the pre-flight gate. When the gate
  requires the model to state its predicted tier and timeline before any dimension is analyzed,
  the hypothesis is verifiable against gate inputs rather than constructed post-hoc from
  completed fields. Passes C-18 and C-15 independently does not satisfy C-21: the hypothesis
  must be elicited inside the gate.
- **Pass condition**: The pre-flight gate (satisfying C-18) includes a step requiring a
  preliminary complexity tier and timeline estimate to be stated before the first analysis
  section opens, AND the synthesis section explicitly confirms or revises this gate-elicited
  commitment.

### C-22 -- Synthesis names the gate commitment site at both ends of the chain
- **Weight**: aspirational
- **Category**: structure
- **Description**: Refinement of C-21. Synthesis must name the gate's structural label
  explicitly -- once when anchoring the prior commitment and once when closing the verdict.
  Without naming the structural anchor, synthesis references an implied prior commitment
  that a reader cannot verify structurally.
- **Pass condition**: Synthesis section explicitly names the pre-flight gate (or equivalent
  structural label) when anchoring the prior commitment AND when stating the confirm/revise
  verdict. An output that satisfies C-21 but refers to the hypothesis only as "my earlier
  estimate" without naming its structural home fails C-22.

### C-23 -- Prohibition guards name the canonical home, not just state the exclusion
- **Weight**: aspirational
- **Category**: structure
- **Description**: Refinement of C-20. Prohibition rules must name the canonical home: "scope
  was resolved in PRE-FLIGHT GATE, not in analysis steps" rather than "do not include scope
  exclusions here." The navigational reference completes the guard -- a reader following the
  prohibition knows exactly where the excluded content belongs.
- **Pass condition**: For at least one canonical field type (scope exclusions, open unknowns),
  the prohibition guards in adjacent sections name the canonical home section by label -- not
  just state a bare exclusion.

### C-24 -- Synthesis provides a structured commitment-chain trace, not just a prose reference
- **Weight**: aspirational
- **Category**: structure
- **Description**: Refinement of C-22. A structured trace makes all three steps of the
  commitment chain scannable without parsing narrative: (1) the gate-committed hypothesis,
  (2) the analysis findings that bear on it, (3) the confirm/revise verdict. A prose paragraph
  that mentions the gate twice satisfies C-22 but embeds the chain in sentences.
- **Pass condition**: Synthesis includes a structured block, labeled list, or field-formatted
  trace that explicitly places the gate commitment, the analysis evidence, and the verdict on
  separate labeled lines or fields -- not folded into a single prose paragraph.

### C-25 -- PRE-FLIGHT GATE forward-references the sections that enforce its scope and hypothesis
- **Weight**: aspirational
- **Category**: structure
- **Description**: Complement of C-23. C-23 requires guards (in adjacent sections) to name
  the canonical home -- the inbound direction. C-25 requires the canonical home to name its
  enforcement sections outbound -- e.g., "Scope exclusions committed here are enforced in:
  SURFACE AREA, COMPLEXITY, INERTIA CHECK, and SYNTHESIS." Together C-23 and C-25 form a
  fully bidirectional navigational mesh.
- **Pass condition**: PRE-FLIGHT GATE (or the canonical home for scope exclusions and hypothesis
  commitment) includes a statement that names at least two downstream sections responsible for
  enforcing its scope exclusions or hypothesis commitment.

### C-26 -- Synthesis embeds a structural AMEND re-evaluation directive
- **Weight**: aspirational
- **Category**: behavior
- **Description**: Refinement of C-16. C-16 is behavioral -- did the output change when AMEND
  was invoked? C-26 requires the synthesis section itself to carry a written directive
  ("If an AMEND directive is present and affects a dimension cited in this section, re-evaluate
  the cross-signal conclusion before closing") so that AMEND cascade is structurally enforced
  regardless of whether AMEND is invoked in the current run.
- **Pass condition**: The synthesis section contains an explicit written rule or directive
  requiring re-evaluation of its cross-signal conclusion when an AMEND directive is present
  -- independent of whether AMEND is invoked in the current run.

### C-27 -- Every aspirational section carries a dedicated FAILURE MODE labeled block
- **Weight**: aspirational
- **Category**: depth
- **Description**: Refinement of C-17. C-17 requires at least one aspirational section to
  name its failure mode. C-27 requires every aspirational section with a nontrivial pass
  condition to carry a dedicated labeled FAILURE MODE block -- not an inline anti-pattern
  mention embedded in prose. A labeled block cannot be absent without a visible structural
  gap.
- **Pass condition**: Every aspirational section with a nontrivial pass condition (synthesis
  and open unknowns at minimum) contains a dedicated labeled FAILURE MODE block or blockquote
  -- not an inline anti-pattern mention embedded in prose.

### C-28 -- Output includes a per-criterion self-check trace covering all aspirational criteria
- **Weight**: aspirational
- **Category**: structure
- **Description**: Adds a distinct self-check block after the complete output that explicitly
  evaluates each aspirational criterion by ID, with pass/fail determination and supporting
  evidence cited per criterion. This is a meta-verification layer above section-level FAILURE
  MODE blocks (C-27): C-27 places failure-mode signals inside each content section; C-28
  requires a separate artifact that systematically audits every criterion collectively.
- **Pass condition**: Output includes a structured block or section -- distinct from the content
  sections and their FAILURE MODE blocks -- that traces each aspirational criterion by ID to an
  explicit pass/fail determination with supporting evidence.

### C-29 -- Self-check items for all structural criteria include exact structural disqualifying forms
- **Weight**: aspirational
- **Category**: structure
- **Description**: Refinement of C-28. Every structural criterion (C-18 through C-27, C-33,
  C-35, C-36, C-38, C-39, C-40, C-41) in the self-check carries both a pass condition and an
  exact disqualifying form -- a specific structural pattern that looks like compliance but fails.
  Older structural criteria must not regress to pass-only descriptions as the denominator grows.
- **Pass condition**: Self-check items for all structural criteria (C-18 through C-27, C-33,
  C-35, C-36, C-38, C-39, C-40, C-41) include both a pass condition and an exact structural
  disqualifying form. An output that satisfies C-28 with exact disqualifying forms only for
  the latest-round criteria fails C-29 unless every structural criterion carries equivalent
  precision.

### C-30 -- Self-check items for all depth and behavior aspirational criteria include exact disqualifying forms
- **Weight**: aspirational
- **Category**: structure
- **Description**: Refinement of C-29. C-29 requires exact disqualifying forms for structural
  criteria. C-30 extends this requirement to depth and behavior criteria (C-09 through C-17,
  C-34, C-37). An output can pass C-29 with full structural precision while depth/behavior
  self-check items carry only pass conditions.
- **Pass condition**: Self-check items for all depth and behavior aspirational criteria (C-09
  through C-17, C-34, C-37) include both a pass condition and an exact disqualifying form. An
  output that satisfies C-29 with exact disqualifying forms only for structural criteria fails
  C-30 unless every depth/behavior criterion carries equivalent disqualifying-form precision.

### C-31 -- Self-check provides complete criterion coverage across all weight classes
- **Weight**: aspirational
- **Category**: structure
- **Description**: Refinement of C-28. C-28 bounds the self-check at aspirational criteria;
  essential and recommended criteria (C-01-C-08) are outside the verification trace. A
  complete verification artifact should audit every criterion regardless of weight class --
  an essential failure disqualifies the output entirely, yet the self-check under C-28 cannot
  detect it.
- **Pass condition**: The per-criterion self-check (satisfying C-28) includes coverage of all
  essential (C-01-C-05) and recommended (C-06-C-08) criteria in addition to all aspirational
  criteria -- each with a pass/fail determination and supporting evidence. An output that
  satisfies C-28+C-29+C-30 with a complete aspirational audit fails C-31 if essential or
  recommended criteria are absent from the verification trace.

### C-32 -- Self-check items for all essential and recommended criteria include exact disqualifying forms
- **Weight**: aspirational
- **Category**: structure
- **Description**: Refinement of C-31. C-31 requires the self-check to extend coverage to
  essential and recommended criteria -- each with a pass/fail determination and supporting
  evidence. C-32 requires those entries to carry the same disqualifying-form precision that
  C-29 established for structural criteria and C-30 established for depth/behavior criteria.
  Precision parity across weight classes is C-32's discriminator.
- **Pass condition**: Self-check items for all essential (C-01-C-05) and recommended (C-06-C-08)
  criteria include both a pass condition and an exact disqualifying form -- a specific output
  pattern that satisfies the surface signal but fails the criterion. An output that satisfies
  C-31 with essential/recommended entries carrying only pass conditions fails C-32.

### C-33 -- Inertia check is the structural opener (precedes all analysis sections)
- **Weight**: aspirational
- **Category**: structure
- **Description**: The inertia check section appears in document order before the complexity
  tier (C-01 field), timeline estimate (C-02 field), surface area section (C-03 content), and
  confidence level (C-05 field). This ensures the status-quo workaround baseline is established
  before any analysis dimension receives a value. Without this ordering, a complexity tier or
  timeline estimate can be assigned without the model having reasoned through what teams
  currently do without the feature. An output can pass C-04 (inertia present, workaround + cost
  named) and still fail C-33 if the inertia content appears after the complexity or timeline
  fields are populated.
  Sourced from V-01 R11 "Inertia as Structural Bookend" -- the first R11 variation to achieve
  100.00 under v11.
- **Pass condition**: Inertia check section appears in document order before the first of:
  complexity tier field, timeline sprint range field, surface area section content, and
  confidence level field. Inertia content appearing inline within or structurally after any
  of those fields fails C-33.

### C-34 -- Inertia check uses a 4-field structured format: Workaround, Ongoing Cost, Cost Direction, Key Driver
- **Weight**: aspirational
- **Category**: depth
- **Description**: Refinement of C-04 and C-10. C-04 requires the workaround to be named
  and one cost dimension characterized. C-10 adds a break-even estimate. C-34 requires the
  inertia check to use a 4-field structured format that adds Cost Direction (is the workaround
  cost trend increasing / stable / decreasing?) and Key Driver (what causal factor creates the
  cost?). Cost Direction converts a static cost observation into a temporal signal -- it tells
  whether the do-nothing path is deteriorating or stabilizing. Key Driver converts a symptom
  into a cause -- it names what removing the workaround would actually fix. An inertia check
  that names the workaround and its cost passes C-04; adding break-even passes C-10; C-34
  requires the full 4-field treatment to make the cost analysis auditable as an investment
  signal.
  Sourced from V-01 R11 -- 4-column table: Workaround / Ongoing Cost / Cost Direction /
  Key Driver.
- **Pass condition**: Inertia check entry contains four explicitly named fields or columns:
  Workaround (what teams do today), Ongoing Cost (what it costs), Cost Direction (trend),
  and Key Driver (causal factor). An inertia entry that names the workaround and cost but
  omits direction and causal driver fails C-34, even if it passes C-04 and C-10.

### C-35 -- Disqualifying forms appear as inline constraint tags at write-time in column headers or field labels
- **Weight**: aspirational
- **Category**: structure
- **Description**: Refinement of C-32. C-32 requires exact disqualifying forms in the
  per-criterion self-check -- a post-completion review artifact that detects violations after
  the output is written. C-35 requires those disqualifying forms to also appear inline in
  column headers or field labels at the moment of production, so the author encounters the
  constraint when filling in the field. C-32 enforces disqualifying-form precision
  *retroactively* (self-check detects violations); C-35 enforces it *proactively*
  (point-of-use tags prevent violations). Together they form a two-layer compliance system:
  prevention at write-time (C-35) and verification at review-time (C-32). An output that
  passes C-32 with a complete disqualifying-form self-check but carries no inline constraint
  tags in column headers fails C-35. An output with point-of-use tags on all
  vocabulary-constrained fields but no self-check passes C-35 and fails C-32.
  Sourced from V-04 R11 -- column headers carry `[FAIL: MODERATE, medium-high, 3/5, or any
  non-vocabulary term]` inline on the complexity column at point-of-use.
- **Pass condition**: At least the vocabulary-constrained essential fields (complexity tier
  C-01 and timeline format C-02) carry inline constraint tags in their column header or field
  label naming the exact failing forms. Tags must appear at the column header or field label
  level; prose instruction in the section body does not satisfy C-35. An output with a
  complete disqualifying-form self-check (C-32) but no point-of-use constraint tags fails
  C-35.

### C-36 -- Constraint tags cover ALL vocabulary-constrained fields, not just the C-01/C-02 minimum
- **Weight**: aspirational
- **Category**: structure
- **Description**: Extension of C-35. C-35 establishes the write-time prevention mechanism
  with a minimum threshold: at least the Complexity Tier (C-01) and Timeline (C-02) column
  headers must carry inline `[FAIL: ...]` constraint tags. C-36 extends that same discipline
  to every vocabulary-constrained field in the output -- Confidence Level, Cost Direction,
  Tier-Destination (where applicable), FTE/team-size fields carrying constrained vocabulary,
  and any other column header where an exact disqualifying form applies. The C-35 minimum
  (two fields) does not satisfy C-36. The distinction matters because a Confidence Level
  column accepting "MEDIUM-HIGH" or a Cost Direction column accepting "worsening" are
  structural failures of the same kind as a Complexity Tier column accepting "MODERATE" --
  each vocabulary-constrained field benefits equally from a write-time guard.
  Sourced from V-01 R12 -- the first variation to achieve full-field write-time constraint
  tag coverage: Complexity Tier, Timeline, Confidence Level, Cost Direction, Tier-Destination
  (both rows), and FTE column headers all carrying inline `[FAIL: ...]` tags.
- **Pass condition**: Every vocabulary-constrained column header or field label in the output
  carries an inline `[FAIL: ...]` constraint tag naming the exact disqualifying forms. An
  output satisfying C-35 with only the C-01 and C-02 minimum fails C-36 if any remaining
  vocabulary-constrained field is untagged. An output with Complexity, Timeline, and
  Confidence Level tagged but Cost Direction or FTE untagged fails C-36.

### C-37 -- Inertia check uses a 5-field format: adds Cost Trajectory to the 4-field minimum
- **Weight**: aspirational
- **Category**: depth
- **Description**: Extension of C-34. C-34 requires four fields: Workaround, Ongoing Cost,
  Cost Direction, Key Driver. Cost Direction captures the vector of change -- is the workaround
  cost growing, stable, or shrinking? C-37 adds Cost Trajectory, which captures the *shape*
  of that change over time: accelerating (cost compounds each period), stable (cost is growing
  but at a constant rate), plateauing (growth is decelerating toward a ceiling), or reversing
  (a mitigation is underway and cost is improving). Direction answers "which way?" Trajectory
  answers "at what rate and shape?" A workaround that is worsening linearly has a different
  urgency profile than one that is compounding -- Trajectory makes the urgency signal
  quantitatively auditable in a way Direction alone cannot. C-34 4-field minimum does not
  satisfy C-37.
  Sourced from V-02 R12 -- the first variation to introduce Cost Trajectory as a fifth named
  inertia field.
- **Pass condition**: Inertia check entry contains five explicitly named fields or columns:
  Workaround, Ongoing Cost, Cost Direction, Cost Trajectory (shape of change: accelerating /
  stable / plateauing / reversing), and Key Driver. An inertia entry satisfying C-34 (4-field)
  fails C-37 if Cost Trajectory is absent or conflated with Cost Direction. The distinction
  between Direction and Trajectory must be structurally explicit -- a single combined field
  named "Cost Trend" does not satisfy C-37.

### C-38 -- PHASE SEALED blocks appear at the end of each phase as structured completion checklists
- **Weight**: aspirational
- **Category**: structure
- **Description**: Extension of C-20 (complete closure mesh). C-20 prevents cross-phase
  field production by requiring each phase to name what it exclusively owns and to prohibit
  production of fields owned by adjacent phases -- a contamination-prevention mechanism.
  C-38 adds a distinct completion-confirmation mechanism: a PHASE SEALED block with a
  structured checklist at the end of each phase, confirming that all phase-required fields
  are resolved and non-empty before the next phase opens. C-20 prevents contamination during
  production; C-38 confirms completeness at the phase boundary. Together they form a two-layer
  phase governance system: C-20 guards against producing the wrong fields, C-38 guards against
  leaving required fields unresolved. An output can satisfy C-20 with complete cross-phase
  prohibitions and fail C-38 if no per-phase SEALED checklist is present. A single SEALED
  block at the end of the full output does not satisfy C-38 -- one block per phase is required.
  Sourced from V-03 R12 -- introduces PHASE 0 SEALED (4-item checklist confirming inertia
  fields), PHASE 1 SEALED (9-item checklist confirming all sizing dimensions), and PHASE 2
  SEALED (3-item checklist confirming synthesis and self-check).
- **Pass condition**: Output contains a PHASE SEALED block at the end of Phase 0, Phase 1,
  and Phase 2. Each block is a structured checklist (minimum 3 items per block) naming the
  phase-specific fields that must be confirmed resolved before the next phase opens. Checklist
  items must name specific fields, not use generic completion language ("all fields complete"
  does not satisfy C-38). A single terminal SEALED block covering all phases fails C-38.

### C-39 -- PHASE SEALED blocks carry role attribution naming the confirming analyst
- **Weight**: aspirational
- **Category**: structure
- **Description**: Extension of C-38. C-38 requires a PHASE SEALED checklist at the end of
  each phase (Phase 0, Phase 1, Phase 2), with minimum 3 specific items per block confirming
  phase-required fields are resolved. C-39 requires each SEALED block to attribute the
  confirmation to a named role -- the analyst or role chartered to own that phase. Role
  attribution reinforces the charter governance system at every phase boundary: the same role
  named in the charter declaration appears again at the phase seal, creating an accountable
  confirmation chain. Phase 0's SEALED block must name the Inertia Analyst (or equivalent);
  Phase 1's must name the Sizing Analyst (or equivalent); Phase 2's must name the Risk
  Assessor or Synthesis owner (or equivalent). Without attribution, a SEALED block is a
  checklist without an owner; with attribution, it is a signed handoff from a chartered role.
  An output satisfying C-38 (three SEALED blocks present, specific items per block) fails
  C-39 if none of the blocks name a role as the confirming agent. Generic completion language
  ("phase complete", "checklist done", "ALL confirmed") satisfies C-38 if items are specific
  but fails C-39 if no role is named as the confirming subject.
  Sourced from V-05 R13 -- the first variation to attribute each phase seal to a named role:
  "The Inertia Analyst confirms ALL before Phase 1 opens", "The Sizing Analyst confirms ALL",
  "The Risk Assessor confirms ALL".
- **Pass condition**: Each PHASE SEALED block at Phase 0, Phase 1, and Phase 2 explicitly
  names a specific role or analyst title as the confirming agent -- the role must appear as
  the grammatical subject of the confirmation statement ("The [Role] confirms ALL..."). A
  SEALED block with the required specific checklist items but no named role fails C-39.
  An output satisfying C-38 with all three SEALED blocks present fails C-39 if none carry
  role attribution.

### C-40 -- Relational-constraint fields enumerate the cross-field disqualifying form as an explicit failure class
- **Weight**: aspirational
- **Category**: structure
- **Description**: Extension of C-36. C-36 requires every vocabulary-constrained column
  header to carry an inline `[FAIL: ...]` constraint tag naming exact disqualifying forms.
  Some fields carry a dual constraint: they must be from a controlled vocabulary AND must
  satisfy a cross-field relational condition (e.g., Tier-Destination must differ from the
  current complexity tier -- not merely be a valid vocabulary term). C-40 requires that for
  such dual-constraint fields, the `[FAIL: ...]` tag explicitly enumerates the relational
  disqualifying form as a separate failure class ("same tier as current"), not just the
  vocabulary failures ("MODERATE, non-vocabulary"). A tag that lists only vocabulary
  disqualifying forms on a dual-constraint field satisfies C-36's format requirement but
  fails C-40 if the cross-field failure case is absent. The distinction matters: a
  Tier-Destination of LOW can fail because it equals the current tier (relational failure)
  independently of whether it is a vocabulary-valid term -- each is a distinct failure mode
  requiring explicit enumeration. Phrasing like `[must differ: LOW / MEDIUM / HIGH / XL]`
  specifies valid options but neither uses `[FAIL:]` prefix nor names the relational
  disqualifying form; it fails both C-36 and C-40. Phrasing like `[FAIL: MODERATE,
  non-vocabulary -- must be: LOW / MEDIUM / HIGH / XL]` satisfies C-36 but fails C-40 if
  "same tier as current" is absent.
  Sourced from V-05 R13 -- the first variation whose Tier-Destination tag reads `[FAIL: same
  tier as current, MODERATE, non-vocabulary -- must differ from current: LOW / MEDIUM / HIGH
  / XL]`, explicitly separating the relational disqualifier from vocabulary disqualifiers.
  Note: V-02 R13 also satisfies C-40 -- its Tier-Destination tag `[FAIL: same as current,
  MODERATE, non-vocabulary...]` includes the cross-field failure class, even though V-02 was
  not designed to target C-40 specifically.
- **Pass condition**: For every field in the output that carries both a vocabulary constraint
  and a relational constraint (a constraint dependent on another field's value, such as "must
  differ from current"), the inline `[FAIL: ...]` tag names the specific relational
  disqualifying form (e.g., "same tier as current") as a distinct failure class alongside
  vocabulary disqualifying forms. An output satisfying C-36 (all fields tagged in `[FAIL:]`
  format) fails C-40 if any dual-constraint field's tag omits the cross-field failure case.
  An output with no dual-constraint fields in scope satisfies C-40 by vacuous pass.

### C-41 -- Phase 2 includes a positive disqualification list for prohibited gap candidates
- **Weight**: aspirational
- **Category**: structure
- **Description**: Extension of C-20 (complete closure mesh) and C-28 (per-criterion
  self-check). Phase 2 in the skill's output typically includes a confidence gap analysis --
  open unknowns or basis gaps that would lower the confidence rating. A behavioral compliance
  approach relies on the analyst knowing what constitutes a valid gap vs. a basis-negation
  gap. C-41 requires Phase 2 to include a structural non-access rule that enumerates all
  prohibited gap candidate forms as an explicit positive disqualification list -- naming
  specific gap statement types that look like valid gaps but fail because they negate the
  stated confidence basis rather than extend it (basis-negation gaps), or because they are
  placeholders without specific unknowns (e.g., "dependencies may exist", "risks are present").
  By enumerating prohibited forms explicitly, the output prevents disqualified gap types
  structurally rather than relying on behavioral restraint. C-20 closes field bleed across
  phases; C-41 closes bad-form gap statements within Phase 2 itself. An output can satisfy
  C-20 with complete cross-phase prohibitions and C-28 with a full per-criterion self-check
  and fail C-41 if Phase 2 carries no explicit disqualification list for prohibited gap
  candidates. A single sentence saying "avoid vague gaps" without naming specific prohibited
  forms does not satisfy C-41.
  Sourced from V-05 R13 -- the first variation to include a non-access rule in Phase 2 with
  an explicit enumeration of all prohibited gap candidate forms, augmenting the self-test
  with a positive disqualification list and preventing basis-negation gaps at the structural
  level rather than the behavioral level.
- **Pass condition**: Phase 2 (or the confidence gap / open unknowns section of Phase 2)
  contains a dedicated structural rule -- a labeled block, named list, or non-access directive
  -- that explicitly enumerates at least two specific prohibited gap candidate forms: statement
  types that would be rejected as basis-negation, placeholder, or structurally invalid gaps.
  The disqualification list must name specific forms (not generic guidance); a rule stating
  "all gap candidates must name a specific unknown" without listing what fails is insufficient.
  The list must be structural, not prose-embedded.

---

## Scoring Model

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 33 * 10)
```

**Golden threshold**: All 5 essential criteria pass AND composite >= 80.

| Band | Composite | Meaning |
|------|-----------|---------|
| Gold | >= 80, all essential pass | Publish-ready sizing signal |
| Silver | >= 60, all essential pass | Useful but missing depth |
| Bronze | >= 40, <=2 essential fail | Partial signal, needs revision |
| Fail | Any essential fail | Output not usable downstream |

---

## Evaluation Notes

- C-04 (inertia check) is the highest-signal differentiator -- a sizing output without it
  is indistinguishable from a naive estimate.
- C-02 (sprint range) guards against false precision; point estimates imply certainty that
  sizing signals never have.
- C-08 only activates on AMEND invocations; default-pass otherwise to avoid penalizing
  non-amend runs.
- Surface area (C-03) and team-size (C-06) together feed `program-plan` routing -- weak
  values here are the most common downstream failure mode.
- C-11 and C-12 are upward refinements of C-06 and C-05 respectively: an output can pass
  the essential/recommended bar and still fail these if ownership scope and named unknowns
  are absent.
- C-13 is the hardest aspirational to pass mechanically; it requires the model to reason
  across dimensions rather than populate fields in sequence.
- C-14 is a structural refinement of C-12 -- output can pass C-12 with prose-embedded
  unknowns and still fail C-14; C-14 rewards the form that makes omissions self-evident.
- C-15 is a structural refinement of C-13 -- hypothesis-first forces the conclusion to be
  verifiable against a prior commitment, not constructed post-hoc.
- C-16 activates only on AMEND + synthesis overlap; default-pass otherwise.
- C-17 passes when the output demonstrates anti-pattern awareness, not merely avoidance.
- C-18 and C-19 are structural gate criteria sourced from R3: C-18 requires a pre-write
  gate (not a section reminder) that fires before any dimension field is filled; C-19
  requires adjacent sections to be closed against field bleed, not merely that a canonical
  section exists. An output can pass C-14 and still fail C-19 if the confidence section
  carries no prohibition.
- C-20 is a refinement of C-19 sourced from R4. Passing C-19 requires at least one adjacent
  section closed; C-20 requires every canonical home to be fully surrounded -- bilateral
  closure in all directions.
- C-21 integrates C-18 and C-15 at the structural level, sourced from the R4 gap where
  C-15 fails in both top-scoring variations. Passing both C-18 and C-15 independently does
  not satisfy C-21: the hypothesis must be elicited inside the gate.
- C-22 is a refinement of C-21 sourced from R5. Passing C-21 requires hypothesis in gate
  and synthesis confirmation. C-22 requires synthesis to name the gate's structural label
  at both the anchor and the verdict.
- C-23 is a refinement of C-20 sourced from R5. Passing C-20 requires all adjacent sections
  to carry prohibition rules. C-23 requires at least one of those rules to name the canonical
  home by label.
- C-24 is a refinement of C-22 sourced from R6. Passing C-22 allows prose synthesis that
  mentions the gate twice. C-24 requires a structured, scannable commitment-chain trace on
  separate labeled lines.
- C-25 is the outbound complement of C-23, sourced from R6. C-23 closes the inbound direction
  (guards name home); C-25 closes the outbound direction (home names guards). Together they
  form a fully bidirectional navigational mesh.
- C-26 is a structural upgrade of C-16, sourced from R7. C-16 defaults to pass when no AMEND
  is invoked. C-26 requires a written directive enforcing AMEND re-evaluation structurally --
  independent of whether AMEND fires.
- C-27 is a structural upgrade of C-17, sourced from R7. C-17 requires at least one
  aspirational section to name its failure mode. C-27 requires every aspirational section to
  carry a dedicated labeled FAILURE MODE block.
- C-28 is a meta-layer above C-27, sourced from R8. C-27 ensures section-level failure-mode
  blocks. C-28 requires a separate collective self-check artifact that evaluates every
  criterion by ID.
- C-29 is a refinement of C-28, sourced from R8. C-28 requires the self-check to exist.
  C-29 requires structural criteria items (C-18-C-27, C-33, C-35, C-36, C-38, C-39, C-40,
  C-41) to include exact disqualifying forms. Coverage uniformity across structural criteria
  is the discriminator. Note: v14 expands the structural criteria set to include C-39, C-40,
  and C-41.
- C-30 is a category extension of C-29, sourced from R9. C-29 achieves structural-category
  uniformity. C-30 requires the same treatment for depth/behavior criteria (C-09-C-17, C-34,
  C-37). An output can pass C-29 and fail C-30 if any depth/behavior criterion in the
  self-check carries only a pass condition.
- C-31 is a scope extension of C-28, sourced from R9. C-28 bounds the self-check at
  aspirational criteria. C-31 extends the verification scope to include essential and
  recommended criteria. An output can satisfy C-28+C-29+C-30 with a complete aspirational
  audit and fail C-31 if essential and recommended criteria have no verification trace entries.
- C-32 is a precision extension of C-31, sourced from R10. C-31 requires essential and
  recommended criteria to be present in the self-check. C-32 requires those entries to carry
  exact disqualifying forms -- the same precision treatment C-29 established for structural
  criteria and C-30 for depth/behavior criteria. V-04 R10 is the first variation to achieve
  complete precision parity across all weight classes.
- C-33 is a position criterion sourced from R11. C-04 requires inertia to be present. C-33
  requires it to be first -- the structural opener before any analysis dimension is assigned.
  An output can pass C-04 and fail C-33 if the inertia check appears after the complexity
  tier or timeline estimate fields.
- C-34 is a structural precision criterion sourced from R11. C-04 requires workaround + one
  cost dimension. C-33 requires inertia to be first. C-34 requires the inertia entry to have
  four named fields: Workaround, Ongoing Cost, Cost Direction, and Key Driver. An output can
  pass C-04 and C-10 (break-even present) and fail C-34 if the Cost Direction and Key Driver
  fields are absent.
- C-35 is a write-time enforcement criterion sourced from R11. C-32 achieves disqualifying-form
  precision in the post-completion self-check. C-35 achieves it at the point-of-use column
  header level. An output can pass C-32 with a complete self-check and fail C-35 if no
  vocabulary-constrained column header carries an inline `[FAIL: ...]` constraint tag.
  Together C-32 and C-35 form a two-layer system: detection (C-32) and prevention (C-35).
- C-36 is a coverage criterion sourced from R12. C-35 establishes write-time prevention with
  a minimum of C-01 and C-02 fields tagged. C-36 requires all vocabulary-constrained fields
  to be tagged at write-time -- Confidence Level, Cost Direction, Tier-Destination, FTE, and
  any other column carrying constrained vocabulary. An output can pass C-35 with two fields
  tagged and fail C-36 if any remaining vocab-constrained column is untagged. V-01 R12 is
  the first variation to achieve comprehensive coverage.
- C-37 is a temporal resolution criterion sourced from R12. C-34 requires 4 inertia fields
  including Cost Direction (vector). C-37 requires a fifth field -- Cost Trajectory -- that
  captures the shape of cost change over time (accelerating / stable / plateauing / reversing).
  Direction and Trajectory are distinct: Direction answers "which way?" Trajectory answers
  "at what rate and pattern?" An output satisfying C-34 fails C-37 if Cost Trajectory is
  absent or if Direction and Trajectory are conflated into a single field. V-02 R12 is the
  first variation to separate these.
- C-38 is a phase completion criterion sourced from R12. C-20 prevents cross-phase field
  production. C-38 adds per-phase completion confirmation via PHASE SEALED blocks -- structured
  checklists at the end of Phase 0, Phase 1, and Phase 2, each confirming that phase-required
  fields are resolved before the next phase opens. An output satisfying C-20 with complete
  cross-phase prohibitions fails C-38 if PHASE SEALED blocks are absent or consolidated into
  a single terminal block. V-03 R12 is the first variation to introduce this mechanism.
- C-39 is a phase accountability criterion sourced from R13. C-38 requires SEALED blocks at
  each phase boundary. C-39 requires each block to name the role responsible for the
  confirmation -- the chartered analyst for that phase. An output satisfying C-38 with three
  complete SEALED blocks fails C-39 if no role is named as the confirming agent. Role
  attribution transforms a checklist into a signed handoff, reinforcing the charter governance
  system at every phase transition. V-05 R13 is the first variation to introduce role-attributed
  SEALED blocks.
- C-40 is a dual-constraint precision criterion sourced from R13. C-36 requires all
  vocabulary-constrained fields to carry `[FAIL: ...]` tags. C-40 extends this to dual-constraint
  fields -- fields that must be from a controlled vocabulary AND satisfy a cross-field relational
  condition (e.g., Tier-Destination must differ from the current tier). An output satisfying
  C-36 on all vocabulary fields fails C-40 if a dual-constraint field's tag enumerates only
  vocabulary failures without naming the relational disqualifying form ("same tier as current").
  V-05 R13 is the first variation to explicitly enumerate the relational failure class. V-02 R13
  also satisfies C-40 incidentally -- its Tier-Destination tag included "same as current" even
  though V-02 was not designed to target this criterion.
- C-41 is a Phase 2 structural disqualification criterion sourced from R13. C-20 closes field
  bleed across phases. C-41 closes bad-form gap statements within Phase 2: it requires a
  non-access rule that positively enumerates prohibited gap candidate forms (basis-negation,
  placeholder). Passing C-20 with full cross-phase closure and C-28 with a complete self-check
  does not satisfy C-41 -- the positive disqualification list for prohibited gap forms is a
  distinct structural artifact targeting a distinct failure mode. V-05 R13 is the first
  variation to include this mechanism.

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-17 | Initial rubric -- 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-17 | Added C-11, C-12, C-13; aspirational denominator 2 -> 5 |
| v3 | 2026-03-17 | Added C-14, C-15, C-16, C-17; aspirational denominator 5 -> 9; sourced from R2 excellence signals |
| v4 | 2026-03-17 | Added C-18, C-19; aspirational denominator 9 -> 11; sourced from R3 |
| v5 | 2026-03-17 | Added C-20, C-21; aspirational denominator 11 -> 13; sourced from R4 |
| v6 | 2026-03-17 | Added C-22, C-23; aspirational denominator 13 -> 15; sourced from R5 |
| v7 | 2026-03-17 | Added C-24, C-25; aspirational denominator 15 -> 17; sourced from R6 |
| v8 | 2026-03-17 | Added C-26, C-27; aspirational denominator 17 -> 19; sourced from R7 |
| v9 | 2026-03-17 | Added C-28, C-29; aspirational denominator 19 -> 21; sourced from R8 |
| v10 | 2026-03-17 | Added C-30, C-31; aspirational denominator 21 -> 23; sourced from R9 |
| v11 | 2026-03-17 | Added C-32; aspirational denominator 23 -> 24; sourced from R10 -- V-04 R10 first to achieve complete disqualifying-form precision parity across all weight classes (structural via C-29, depth/behavior via C-30, essential/recommended via C-32) |
| v12 | 2026-03-17 | Added C-33 (inertia as structural opener), C-34 (inertia 4-field format), C-35 (point-of-use constraint tags); aspirational denominator 24 -> 27; sourced from R11 -- V-05 R11 first to combine all three, achieving 100.00 under v12 |
| v13 | 2026-03-17 | Added C-36 (comprehensive constraint tag coverage), C-37 (5-field inertia -- Cost Trajectory), C-38 (PHASE SEALED completion blocks); aspirational denominator 27 -> 30; sourced from R12 -- three independent single-axis advances; no R12 variation achieves all three simultaneously; v13 champion requires combining C-36 + C-37 + C-38 |
| v14 | 2026-03-17 | Added C-39 (role-attributed PHASE SEALED blocks), C-40 (relational-constraint field disqualifying form), C-41 (Phase 2 positive disqualification list for prohibited gap candidates); aspirational denominator 30 -> 33; sourced from R13 -- V-05 R13 achieves 100.00 under both v13 and v14 (33/33); C-40 retroactively promotes V-02 R13 to 29/33 alongside V-04; C-29 scope expanded to include C-39/C-40/C-41 |
"""

dest.write_text(content, encoding="utf-8")
print(f"Written {len(content)} bytes to {dest}")
