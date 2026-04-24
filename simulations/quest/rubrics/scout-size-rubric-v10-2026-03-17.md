Written to `simulations/quest/rubrics/scout-size-rubric-v10-2026-03-17.md`.

---

**Two new aspirational criteria added (C-30 through C-31):**

| ID | Pattern source | What it checks |
|----|----------------|----------------|
| **C-30** | V-05 R9 "depth/behavior precision gap" | Self-check items for all depth and behavior aspirational criteria (C-09–C-17) include exact disqualifying forms alongside pass conditions. V-05 achieves C-29 (structural criteria C-18–C-27 have exact disqualifying forms) but leaves depth/behavior self-check items as pass-condition descriptions only — the same asymmetry C-18–C-25 had before C-29 required structural precision there. Passing C-29 does not satisfy C-30 if depth/behavior criteria carry only pass conditions. |
| **C-31** | V-05 R9 "self-check bounded at aspirational" | The per-criterion self-check (C-28) extends coverage to essential (C-01–C-05) and recommended (C-06–C-08) criteria in addition to all 23 aspirational criteria. V-05 achieves complete aspirational precision under C-28+C-29+C-30 but does not audit essential or recommended criteria — leaving the two highest-consequence weight classes outside the verification trace. Passing C-28+C-29+C-30 does not satisfy C-31 if essential/recommended criteria have no entries. |

**What makes these genuinely new:**

- C-30 is not a refinement of C-29. C-29 achieves structural-category uniformity across C-18–C-27. C-30 requires depth/behavior-category uniformity across C-09–C-17. An output can pass C-29 with a fully precise structural self-check block and still fail C-30 if every depth/behavior criterion carries only a pass condition. Coverage category is the discriminator.

- C-31 is not a refinement of C-30. C-28+C-29+C-30 require complete aspirational precision (all 23 criteria, exact disqualifying forms across all categories). C-31 requires the self-check to extend beyond aspirational criteria to cover all weight classes. Weight class scope is the discriminator: C-31 asks whether all 31 criteria are in the verification trace, not only the 23 aspirational ones.

**Scoring model:** aspirational denominator bumped 21 → 23. Max composite unchanged at 100.

**Expected R9 scores under v10:**

| Variation | Aspirational | Score |
|-----------|-------------|-------|
| V-01 (structural AMEND directive only) | 18/23 (fails C-27, C-28, C-29, C-30, C-31) | 97.83 |
| V-02 (dedicated FAILURE MODE blocks only) | 18/23 (fails C-26, C-28, C-29, C-30, C-31) | 97.83 |
| V-03 (C-26 + C-27, no self-check) | 19/23 (fails C-28, C-29, C-30, C-31) | 98.26 |
| V-04 (self-check + definition-level C-26/C-27 items) | 20/23 (fails C-29, C-30, C-31) | 98.70 |
| V-05 (full integration + uniform structural precision) | 21/23 (fails C-30, C-31) | 99.13 |

V-05 drops from 21/21 (perfect under v9) to 21/23 under v10. The two new criteria split cleanly: C-30 targets the depth/behavior precision gap that persists even in V-05's self-check; C-31 targets the aspirational-only scope boundary that persists even with C-28+C-29+C-30 fully satisfied. The R10 gold standard requires closing both.
### C-06 -- Team-size signal names required specializations
- **Weight**: recommended
- **Category**: depth
- **Description**: Team-size signal goes beyond headcount to name the types of
  specialists required (e.g., "1 backend + 1 infra", not just "2 engineers"). This
  lets program-plan route work correctly.
- **Pass condition**: Team-size signal identifies at least one role or specialization,
  not just a number.

### C-07 -- Complexity rating is justified with at least one driver
- **Weight**: recommended
- **Category**: depth
- **Description**: The complexity tier (C-01) is accompanied by the primary driver
  that determined the rating -- e.g., "HIGH because of distributed transaction boundary",
  "LOW because isolated namespace with no shared state". Bare tier labels are less
  useful downstream.
- **Pass condition**: At least one sentence following or inline with the complexity
  tier names what pushed it to that level.

### C-08 -- AMEND instructions modify the stated output, not the process
- **Weight**: recommended
- **Category**: behavior
- **Description**: When an AMEND directive is present (adjust confidence thresholds or
  focus on a complexity dimension), the output reflects the amendment in its content --
  e.g., a revised confidence level, or expanded analysis of the named dimension. The
  skill should not just acknowledge the amendment; it should change the artifact.
- **Pass condition**: If AMEND is invoked, at least one substantive change in the output
  (different tier, revised confidence, expanded section) can be traced to the amendment.
  If no AMEND is present, criterion is scored as pass by default.

---

## Aspirational Criteria (10 points total)

### C-09 -- Sizing signal explicitly scopes what is NOT included
- **Weight**: aspirational
- **Category**: depth
- **Description**: Output states at least one thing the sizing does NOT cover
  (out-of-scope sub-systems, deferred complexity, assumptions made). This prevents
  silent misreads when program-plan consumes the signal.
- **Pass condition**: At least one explicit exclusion, assumption, or out-of-scope
  boundary is named.

### C-10 -- Inertia check includes a break-even signal
- **Weight**: aspirational
- **Category**: depth
- **Description**: Beyond naming the workaround cost, the output estimates when building
  the feature pays off relative to continued workaround cost -- even as a rough
  qualitative signal ("break-even at ~4 uses/week", "never breaks even if adoption stays
  below 3 teams"). This is the highest-value form of the inertia check for investment
  decisions.
- **Pass condition**: Output contains a break-even estimate or explicitly states that
  break-even cannot be assessed and why.

### C-11 -- Each named specialization states its implementation ownership
- **Weight**: aspirational
- **Category**: depth
- **Description**: Team-size signal goes beyond naming roles (C-06) to state what each
  specialization owns during implementation. Without ownership scope, the role list is
  decorative and program-plan still needs a follow-up conversation to assign work.
  Sourced from V-02 Step 6 and V-03 INERTIA ANALYST, both of which required "what they
  own during the build."
- **Pass condition**: At least one named specialization includes a description of its
  implementation scope or ownership area.

### C-12 -- Confidence section names specific unknowns that would change the rating
- **Weight**: aspirational
- **Category**: depth
- **Description**: A confidence basis (C-05) is actionable only when the output also
  names the specific unknowns that, if resolved, would raise or lower the rating. A
  basis without named unknowns leaves the reader unable to close the gap. Sourced from
  V-02 Step 6 and V-03 RISK, both present in the two highest-scoring R1 variations.
- **Pass condition**: At least one concrete unknown is named that would move the
  confidence level if resolved, or output explicitly states no remaining unknowns.

### C-13 -- Closing synthesis integrates signals, not just restates them
- **Weight**: aspirational
- **Category**: depth
- **Description**: Output contains a concluding statement that draws a decision-relevant
  conclusion by cross-referencing two or more signal dimensions. A closing that merely
  restates each field in sequence is juxtaposition, not synthesis. Sourced from V-03 R1:
  "verbose juxtaposition over true synthesis" was the primary structural gap in the
  role-sequence variation.
- **Pass condition**: At least one sentence cross-references two or more signal
  dimensions (complexity, timeline, confidence, inertia) to produce a directional
  recommendation or decision-relevant observation.

### C-14 -- Open unknowns appear in a dedicated section with typed fields
- **Weight**: aspirational
- **Category**: structure
- **Description**: Refinement of C-12. Naming unknowns inside the confidence basis
  paragraph makes omissions hard to detect. When unknowns appear in a structurally
  separate section with typed fields (Unknown: / Impact: / Movement:), any gap is
  visually self-evident. Sourced from V-02 R2, where the section boundary made omission
  structurally impossible to hide. Output can still pass C-12 with prose-embedded
  unknowns; C-14 rewards the higher-reliability structural form.
- **Pass condition**: Open unknowns (or an explicit "no open unknowns" declaration)
  appear in a named section or block separate from the confidence basis, with at least
  one field-typed entry or a structured HIGH-confidence fallback statement.

### C-15 -- Synthesis confirms or revises a prior stated hypothesis
- **Weight**: aspirational
- **Category**: depth
- **Description**: Refinement of C-13. A synthesis derived post-hoc from already-
  populated fields can still be juxtaposition dressed as reasoning. When the output
  commits to a preliminary hypothesis earlier and the synthesis explicitly confirms or
  revises that commitment, the reasoning is verifiable. Sourced from V-04 R2, the
  "Hypothesis-Revision" variation.
- **Pass condition**: A preliminary hypothesis or prior estimate appears before the
  detailed analysis sections, and the synthesis section explicitly states whether the
  hypothesis was confirmed, revised, or partially revised, with the dimension that
  changed.

### C-16 -- AMEND cascades to synthesis when the amended dimension is cited there
- **Weight**: aspirational
- **Category**: behavior
- **Description**: Extension of C-08 and C-13. When an AMEND directive changes a signal
  dimension that is also referenced in the synthesis, the synthesis must be re-evaluated
  to reflect whether the cross-signal conclusion still holds. Acknowledging the AMEND in
  the amended section but leaving the synthesis unchanged is a silent contradiction.
  Sourced from R2 pattern: "AMEND cascade to synthesis."
- **Pass condition**: If AMEND is invoked and the amended dimension appears in the
  synthesis, the synthesis conclusion is updated or explicitly reaffirmed in light of the
  amendment. Default pass if no AMEND is present, or if the amended dimension is not
  cited in the synthesis.

### C-17 -- Aspirational sections name their failure mode
- **Weight**: aspirational
- **Category**: depth
- **Description**: For synthesis (C-13) and unknowns (C-12), an output that explicitly
  distinguishes the required form from the anti-pattern demonstrates active quality
  enforcement, not passive field population. Sourced from the V-05 R2 "Rules:
  sub-sections" pattern, where explicit negative examples were the primary driver of
  execution reliability at score 100.
- **Pass condition**: At least one aspirational section (synthesis or unknowns) contains
  a sentence that names the anti-pattern being avoided or explicitly states what form of
  response would fail the criterion.

### C-18 -- A pre-analysis self-check gate precedes the first dimension section
- **Weight**: aspirational
- **Category**: structure
- **Description**: V-05 was the only R3 variation to pass both C-09 (scope exclusions)
  and C-10 (break-even signal) -- exclusively because it mandated a self-check
  confirmation block before the first analysis section. Without this gate, models defer
  exclusions and break-even until the end or omit them. Structural gate, not a section
  reminder. Sourced from R3.
- **Pass condition**: A self-check, confirmation block, or pre-flight step appears before
  the first analysis section and requires the model to explicitly address scope boundary
  (what is NOT included) and break-even signal before proceeding. Inline reminders within
  sections do not satisfy this criterion.

### C-19 -- Sections that could receive duplicate field types carry explicit prohibition guards
- **Weight**: aspirational
- **Category**: structure
- **Description**: V-03 scored C-14 PARTIAL in R3: a dedicated OPEN UNKNOWNS section
  existed, but the CONFIDENCE section still carried a Gap field with no prohibition --
  the structural separation was leaky. This prohibition guard is a distinct structural
  property from having a canonical home section. Sourced from V-03 R3 "Leaky separation"
  finding.
- **Pass condition**: When a canonical section exists for a field type (e.g., OPEN
  UNKNOWNS for unknowns), at least one adjacent section that could plausibly receive the
  same content carries an explicit prohibition rule.

### C-20 -- Complete closure mesh: every canonical section is closed bilaterally
- **Weight**: aspirational
- **Category**: structure
- **Description**: V-02 R4 demonstrated "comprehensive bilateral closure." V-01 R4 passes
  C-19 (CONFIDENCE carries a prohibition against unknowns) but fails C-20: SURFACE AREA
  and COMPLEXITY carry no prohibition against scope exclusions. C-20 requires every
  section that could receive a canonical field type to be closed from every direction.
  An output can pass C-19 with partial closure and still fail C-20.
- **Pass condition**: For every canonical home section, ALL sections that could plausibly
  receive the same content carry explicit prohibition rules -- no unguarded adjacent
  section remains for any canonical field type.

### C-21 -- Pre-flight gate elicits a preliminary hypothesis before analysis proceeds
- **Weight**: aspirational
- **Category**: structure
- **Description**: Both V-01 and V-02 in R4 fail C-15 despite being the two highest-
  scoring variations -- the preliminary hypothesis has no structural anchor forcing it
  before analysis. A variation that folds the hypothesis commitment into the pre-flight
  gate forces the model to state its predicted tier and timeline before any dimension is
  analyzed. Structural advancement beyond C-15 (hypothesis exists but is standalone) and
  C-18 (gate exists but does not elicit hypothesis). Sourced from the R4 structural gap.
- **Pass condition**: The pre-flight gate (satisfying C-18) includes a step requiring a
  preliminary complexity tier and timeline estimate to be stated before the first analysis
  section opens, AND the synthesis section explicitly confirms or revises this
  gate-elicited commitment. An output that passes C-18 and C-15 independently (gate
  present, hypothesis present but not inside the gate) does not satisfy C-21.

### C-22 -- Synthesis names the gate commitment site at both ends of the chain
- **Weight**: aspirational
- **Category**: structure
- **Description**: Refinement of C-21. C-22 requires synthesis to name the gate's
  structural label explicitly -- once when anchoring the prior commitment ("the hypothesis
  committed in PRE-FLIGHT GATE") and once when closing the verdict. Without naming the
  structural anchor, synthesis references an implied prior commitment that a reader cannot
  verify structurally. Sourced from R5 pattern: "Gate-as-atomic-commitment-block."
- **Pass condition**: Synthesis section explicitly names the pre-flight gate when
  anchoring the prior commitment AND when stating the confirm/revise verdict. An output
  that satisfies C-21 but refers to the hypothesis without naming its structural home
  fails C-22.

### C-23 -- Prohibition guards name the canonical home, not just state the exclusion
- **Weight**: aspirational
- **Category**: structure
- **Description**: Refinement of C-20. C-23 requires prohibition rules to name the
  canonical home: "scope was resolved in PRE-FLIGHT GATE, not in analysis steps" rather
  than "do not include scope exclusions here." Without naming the home, the prohibition
  is a dead end: it closes a door without pointing to the right room. Sourced from R5
  pattern: INERTIA CHECK guard naming canonical home.
- **Pass condition**: For at least one canonical field type, the prohibition guards in
  adjacent sections name the canonical home section by label. Guards reading only "do not
  include scope exclusions here" without specifying where they belong fail C-23.

### C-24 -- Synthesis provides a structured commitment-chain trace, not just a prose reference
- **Weight**: aspirational
- **Category**: structure
- **Description**: Refinement of C-22. C-24 requires a structured trace that makes all
  three steps of the commitment chain scannable without parsing narrative: (1) the
  gate-committed hypothesis, (2) the analysis findings that bear on it, (3) the
  confirm/revise verdict. A prose paragraph that mentions PRE-FLIGHT GATE twice satisfies
  C-22 but leaves the chain embedded in sentences. Sourced from R6 V-03 "No self-check
  machinery" annotation: V-04/V-05 R6 add a structured trace block making commitment-
  chain integrity auditable at a glance.
- **Pass condition**: Synthesis includes a structured block, labeled list, or
  field-formatted trace that explicitly places the gate commitment, the analysis evidence,
  and the verdict on separate labeled lines or fields. An output that satisfies C-22
  through prose alone fails C-24.

### C-25 -- PRE-FLIGHT GATE forward-references the sections that enforce its scope and hypothesis
- **Weight**: aspirational
- **Category**: structure
- **Description**: Complement of C-23. C-23 requires guards (in adjacent sections) to
  name the canonical home -- the inbound direction of the navigational mesh. C-25
  requires the canonical home (PRE-FLIGHT GATE) to name its enforcement sections outbound.
  Together C-23 and C-25 form a fully bidirectional navigational mesh: every guard points
  home (C-23) and every canonical home names its guards (C-25). Sourced from R6 V-05
  pattern: PRE-FLIGHT GATE includes a forward-reference list of enforcement sections.
- **Pass condition**: PRE-FLIGHT GATE includes a statement that names at least two
  downstream sections responsible for enforcing its scope exclusions or hypothesis
  commitment. A gate that commits scope and hypothesis without naming its enforcement
  sections fails C-25 even if those sections carry navigational guards back to the gate.

### C-26 -- Synthesis embeds a structural AMEND re-evaluation directive
- **Weight**: aspirational
- **Category**: behavior
- **Description**: Refinement of C-16. C-16 is behavioral and defaults to pass when no
  AMEND is present. C-26 requires the synthesis section itself to carry a written
  directive -- e.g., "If an AMEND directive is present and affects a dimension cited in
  this section, re-evaluate the cross-signal conclusion before closing" -- so that AMEND
  cascade is structurally enforced regardless of whether AMEND is invoked in the current
  run. An output that passes C-16 by default with no structural directive fails C-26.
  Sourced from V-02 R7.
- **Pass condition**: The synthesis section contains an explicit written rule or directive
  requiring re-evaluation of its cross-signal conclusion when an AMEND directive is
  present -- independent of whether AMEND is invoked in the current run. A synthesis that
  passes C-16 through default pass or incidental cascade without a structural directive
  fails C-26.

### C-27 -- Every aspirational section carries a dedicated FAILURE MODE labeled block
- **Weight**: aspirational
- **Category**: depth
- **Description**: Refinement of C-17. C-17 requires at least one aspirational section
  (synthesis or unknowns) to name its failure mode -- even as an inline sentence. C-27
  requires every aspirational section with a nontrivial pass condition to carry a
  dedicated labeled FAILURE MODE block, making non-compliance structurally visible
  without re-reading prose. An inline mention can be overlooked; a labeled FAILURE MODE
  block cannot be absent without a visible structural gap. Sourced from V-04/V-05 R7.
- **Pass condition**: Every aspirational section with a nontrivial pass condition
  contains a dedicated labeled FAILURE MODE block or blockquote -- not an inline
  anti-pattern mention embedded in prose. An output that passes C-17 with only inline
  failure-mode language fails C-27 unless that language appears in a structurally
  separate labeled block.

### C-28 -- Output includes a per-criterion self-check trace covering all aspirational criteria
- **Weight**: aspirational
- **Category**: structure
- **Description**: V-04 R8 adds a distinct self-check block after the complete output
  that explicitly evaluates each aspirational criterion by ID, with pass/fail
  determination and supporting evidence cited per criterion. This is a meta-verification
  layer that section-level FAILURE MODE blocks (C-27) cannot substitute for: C-27 places
  structural failure-mode signals inside each content section; C-28 requires a separate
  artifact that systematically audits every criterion collectively. V-03 achieves 19/19
  under v8 with dual FAILURE MODE blocks and a structural AMEND directive but carries no
  self-check machinery. Sourced from V-04 R8: the "27-criterion self-check."
- **Pass condition**: Output includes a structured block or section -- distinct from the
  content sections and their FAILURE MODE blocks -- that traces each aspirational
  criterion by ID to an explicit pass/fail determination with supporting evidence. An
  output that passes C-27 with dedicated FAILURE MODE blocks in every aspirational
  section but carries no collective per-criterion evaluation fails C-28.

### C-29 -- Self-check items for all structural criteria include exact structural disqualifying forms
- **Weight**: aspirational
- **Category**: structure
- **Description**: Refinement of C-28. V-04 includes definition-level discriminators in
  its self-check for C-26 and C-27 only. V-05 extends this treatment to all structural
  criteria (C-18 through C-27): every structural criterion carries an exact disqualifying
  form alongside its pass condition, not just the two most recently added. V-04 achieves
  precision for the latest-round criteria; V-05 achieves it uniformly across the full
  set, ensuring older structural criteria do not regress to pass-only descriptions as the
  denominator grows. Sourced from V-05 R8.
- **Pass condition**: Self-check items for all structural criteria (C-18 through C-27)
  include both a pass condition and an exact structural disqualifying form. An output that
  satisfies C-28 with exact disqualifying forms only for C-26 and C-27 fails C-29 unless
  every other structural criterion carries equivalent precision.

### C-30 -- Self-check items for all depth and behavior aspirational criteria include exact disqualifying forms
- **Weight**: aspirational
- **Category**: structure
- **Description**: Refinement of C-29. C-29 requires exact disqualifying forms for all
  structural criteria (C-18-C-27) in the per-criterion self-check. The depth and behavior
  criteria (C-09-C-17) in V-05's self-check carry only pass-condition descriptions -- the
  same state C-18-C-25 were in before C-29 required structural precision there. V-05
  achieves C-29 by extending disqualifying-form coverage uniformly to all structural
  criteria; the analogous gap is depth/behavior criteria (C-09-C-17) carrying only pass
  conditions. This creates an asymmetry: the structural criteria carry exact disqualifying
  forms, but the foundational depth/behavior criteria -- which define what quality content
  looks like -- do not. An output can pass C-29 with full structural precision while
  depth/behavior self-check items consist entirely of pass-condition descriptions.
  Sourced from V-05 R9 "depth/behavior precision gap": V-05 is the first variation to
  achieve 21/21 under v9 but leaves depth/behavior self-check items without the
  disqualifying-form precision that C-29 established for structural criteria.
- **Pass condition**: Self-check items for all depth and behavior aspirational criteria
  (C-09 through C-17) include both a pass condition and an exact disqualifying form -- a
  specific output pattern that satisfies the surface signal but fails the criterion. An
  output that satisfies C-29 with exact disqualifying forms only for structural criteria
  (C-18-C-27) fails C-30 unless every depth/behavior criterion carries equivalent
  disqualifying-form precision. Passing C-29 does not satisfy C-30 even if depth/behavior
  items exist in the self-check with only pass-condition descriptions.

### C-31 -- Self-check provides complete criterion coverage across all weight classes
- **Weight**: aspirational
- **Category**: structure
- **Description**: Refinement of C-28. C-28 requires a per-criterion self-check covering
  all aspirational criteria. Combined with C-29 and C-30, a complete aspirational
  self-check with full disqualifying-form precision exists. The self-check remains bounded
  at aspirational criteria by the C-28 definition; essential and recommended criteria
  (C-01-C-08) are outside the verification trace. A complete verification artifact should
  audit every criterion regardless of weight class -- an essential failure (e.g., sprint
  range as a point estimate) disqualifies the output entirely, yet the self-check under
  C-28 cannot detect it. Recommended failures (e.g., specializations named without
  ownership scope) are equally invisible. Extending the per-criterion audit to cover
  C-01-C-08 closes the scope gap: the self-check becomes a complete compliance trace
  across all 31 criteria, not a 23-criterion aspirational audit with an implicit
  assumption that essential and recommended criteria pass. Sourced from V-05 R9
  "self-check bounded at aspirational": V-05 achieves complete aspirational precision but
  does not extend the per-criterion audit to essential or recommended criteria, leaving
  the two highest-consequence weight classes outside the self-check scope.
- **Pass condition**: The per-criterion self-check (satisfying C-28) includes coverage of
  all essential (C-01-C-05) and recommended (C-06-C-08) criteria in addition to all
  aspirational criteria -- each with a pass/fail determination and supporting evidence. An
  output that satisfies C-28, C-29, and C-30 with a complete 23-criterion aspirational
  audit fails C-31 if essential or recommended criteria are absent from the verification
  trace.

---

## What makes C-30 and C-31 genuinely new (not redundant with v9)

**C-30 is not a refinement of C-29.** C-29 requires exact disqualifying forms for
structural criteria (C-18-C-27) -- the criteria that define structural architecture
properties: gates, closure meshes, commitment chains, AMEND directives, failure-mode
blocks. C-30 requires exact disqualifying forms for depth and behavior criteria
(C-09-C-17) -- the criteria that assess content quality and behavioral correctness.
V-05 satisfies C-29 with uniform structural precision but leaves the depth/behavior
self-check items as pass-condition descriptions only, creating a precision asymmetry
across criterion categories. Coverage category is the discriminator: C-29 achieves
structural-category uniformity; C-30 requires depth/behavior-category uniformity.
An output can pass C-29 with a fully precise structural self-check block and still
fail C-30 if every depth/behavior criterion carries only a pass condition.

**C-31 is not a refinement of C-30.** C-28, C-29, and C-30 together require the
self-check to cover all 23 aspirational criteria with exact disqualifying forms across
all aspirational categories. C-31 requires the self-check to extend its scope beyond
aspirational criteria to include essential and recommended criteria. The discriminator
is weight class, not precision within a class: C-31 asks whether the self-check treats
all 31 criteria as verifiable output properties, or only the 23 aspirational ones. An
output can pass C-28+C-29+C-30 with a complete 23-criterion aspirational audit at
maximum precision and still fail C-31 if essential and recommended criteria have no
entries in the verification trace.

---

## Scoring Model

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 23 * 10)
```

**Golden threshold**: All 5 essential criteria pass AND composite >= 80.

| Band | Composite | Meaning |
|------|-----------|---------|
| Gold | >= 80, all essential pass | Publish-ready sizing signal |
| Silver | >= 60, all essential pass | Useful but missing depth |
| Bronze | >= 40, <=2 essential fail | Partial signal, needs revision |
| Fail | Any essential fail | Output not usable downstream |

---

## Expected R9 scores under v10

| Variation | Aspirational | Score |
|-----------|-------------|-------|
| V-01 (structural AMEND directive only) | 18/23 (fails C-27, C-28, C-29, C-30, C-31) | 97.83 |
| V-02 (dedicated FAILURE MODE blocks only) | 18/23 (fails C-26, C-28, C-29, C-30, C-31) | 97.83 |
| V-03 (C-26 + C-27, no self-check) | 19/23 (fails C-28, C-29, C-30, C-31) | 98.26 |
| V-04 (self-check + definition-level C-26/C-27 items) | 20/23 (fails C-29, C-30, C-31) | 98.70 |
| V-05 (full integration + uniform structural precision) | 21/23 (fails C-30, C-31) | 99.13 |

V-05 is the R9 gold standard (21/21 under v9) but falls 2/23 under v10. The two new
criteria split across depth/behavior precision (C-30) and full-coverage scope extension
(C-31), establishing that the R10 gold standard requires both completing the
disqualifying-form treatment across all aspirational categories and extending the
self-check verification scope to all 31 criteria regardless of weight class.

---

## Evaluation Notes

- C-04 (inertia check) is the highest-signal differentiator -- a sizing output without
  it is indistinguishable from a naive estimate.
- C-02 (sprint range) guards against false precision; point estimates imply certainty
  that sizing signals never have.
- C-08 only activates on AMEND invocations; default-pass otherwise.
- Surface area (C-03) and team-size (C-06) together feed program-plan routing -- weak
  values here are the most common downstream failure mode.
- C-11 and C-12 are upward refinements of C-06 and C-05: an output can pass the
  essential/recommended bar and still fail these if ownership scope and named unknowns
  are absent.
- C-13 is the hardest aspirational to pass mechanically; it requires the model to reason
  across dimensions rather than populate fields in sequence.
- C-14 is a structural refinement of C-12 -- output can pass C-12 with prose-embedded
  unknowns and still fail C-14; C-14 rewards the form that makes omissions self-evident.
- C-15 is a structural refinement of C-13 -- hypothesis-first forces the conclusion to be
  verifiable against a prior commitment, not constructed post-hoc.
- C-16 activates only on AMEND + synthesis overlap; default-pass otherwise.
- C-17 passes when the output demonstrates anti-pattern awareness, not merely avoidance.
- C-18 and C-19 are structural gate criteria sourced from R3. C-18 requires a pre-write
  gate (not a section reminder); C-19 requires adjacent sections to be closed against
  field bleed. An output can pass C-14 and still fail C-19 if the confidence section
  carries no prohibition.
- C-20 is a refinement of C-19 sourced from R4. Passing C-19 requires at least one
  adjacent section closed; C-20 requires every canonical home to be fully surrounded.
  V-01 R4 passes C-19, fails C-20: scope exclusion canonical home has no adjacent
  prohibitions in SURFACE AREA or COMPLEXITY.
- C-21 integrates C-18 and C-15 at the structural level, sourced from the R4 gap where
  C-15 fails in both top-scoring variations. Passing both C-18 and C-15 independently
  does not satisfy C-21: the hypothesis must be elicited inside the gate.
- C-22 is a refinement of C-21 sourced from R5. Passing C-21 requires hypothesis in gate
  and synthesis confirmation. C-22 requires synthesis to name the gate's structural label
  at both the anchor and the verdict.
- C-23 is a refinement of C-20 sourced from R5. Passing C-20 requires all adjacent
  sections to carry prohibition rules. C-23 requires at least one of those rules to name
  the canonical home by label.
- C-24 is a refinement of C-22 sourced from R6. Passing C-22 allows prose synthesis that
  mentions the gate twice. C-24 requires a structured, scannable commitment-chain trace
  on separate labeled lines.
- C-25 is the outbound complement of C-23, sourced from R6. C-23 closes the inbound
  direction (guards name home); C-25 closes the outbound direction (home names guards).
  Together they form a fully bidirectional navigational mesh.
- C-26 is a structural upgrade of C-16, sourced from R7. C-16 defaults to pass when no
  AMEND is invoked. C-26 requires a written directive enforcing AMEND re-evaluation
  structurally -- independent of whether AMEND fires.
- C-27 is a structural upgrade of C-17, sourced from R7. C-17 requires at least one
  aspirational section to name its failure mode. C-27 requires every aspirational section
  to carry a dedicated labeled FAILURE MODE block.
- C-28 is a meta-layer above C-27, sourced from R8. C-27 ensures section-level
  failure-mode blocks. C-28 requires a separate collective self-check artifact that
  evaluates every criterion by ID.
- C-29 is a refinement of C-28, sourced from R8. C-28 requires the self-check to exist.
  C-29 requires structural criteria items (C-18-C-27) to include exact disqualifying
  forms. Coverage uniformity across structural criteria is the discriminator.
- C-30 is a category extension of C-29, sourced from R9. C-29 achieves structural-
  category uniformity (C-18-C-27 all have exact disqualifying forms). C-30 requires the
  same treatment for depth/behavior criteria (C-09-C-17). V-05 passes C-29 with full
  structural precision but leaves depth/behavior self-check items as pass-condition
  descriptions only. An output can pass C-29 and fail C-30 if any depth/behavior
  criterion in the self-check carries only a pass condition.
- C-31 is a scope extension of C-28, sourced from R9. C-28 bounds the self-check at
  aspirational criteria. C-31 extends the verification scope to include essential and
  recommended criteria. V-05 achieves complete aspirational precision but does not audit
  C-01-C-08. Essential failures are the most consequential (they disqualify the output);
  their absence from the self-check means the audit is structurally incomplete regardless
  of aspirational precision. An output can satisfy C-28+C-29+C-30 with a 23-criterion
  aspirational audit and fail C-31 if essential and recommended criteria have no
  verification trace entries.

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-17 | Initial rubric -- 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-17 | Added C-11 (specialization ownership), C-12 (named unknowns), C-13 (cross-signal synthesis); aspirational denominator 2 -> 5 |
| v3 | 2026-03-17 | Added C-14 (unknowns dedicated section), C-15 (hypothesis-revision lifecycle), C-16 (AMEND cascades to synthesis), C-17 (sections name failure modes); aspirational denominator 5 -> 9; sourced from R2 excellence signals |
| v4 | 2026-03-17 | Added C-18 (pre-analysis self-check gate), C-19 (cross-contamination prohibition guards); aspirational denominator 9 -> 11; sourced from R3 excellence signals |
| v5 | 2026-03-17 | Added C-20 (complete bilateral closure mesh), C-21 (pre-flight gate elicits preliminary hypothesis); aspirational denominator 11 -> 13; sourced from R4 |
| v6 | 2026-03-17 | Added C-22 (synthesis names gate commitment site at both ends), C-23 (prohibition guards name canonical home); aspirational denominator 13 -> 15; sourced from R5 |
| v7 | 2026-03-17 | Added C-24 (synthesis provides structured commitment-chain trace), C-25 (PRE-FLIGHT GATE forward-references its enforcement sections); aspirational denominator 15 -> 17; sourced from R6 |
| v8 | 2026-03-17 | Added C-26 (synthesis embeds structural AMEND re-evaluation directive), C-27 (every aspirational section carries dedicated FAILURE MODE labeled block); aspirational denominator 17 -> 19; sourced from R7 |
| v9 | 2026-03-17 | Added C-28 (per-criterion self-check trace covering all aspirational criteria), C-29 (self-check items for all structural criteria include exact structural disqualifying forms); aspirational denominator 19 -> 21; sourced from R8 |
| v10 | 2026-03-17 | Added C-30 (self-check items for all depth/behavior aspirational criteria include exact disqualifying forms), C-31 (self-check extends to cover essential and recommended criteria C-01-C-08); aspirational denominator 21 -> 23; sourced from R9 -- V-05 achieves 21/21 under v9 but its depth/behavior self-check items (C-09-C-17) carry only pass conditions creating a precision asymmetry relative to structural criteria (C-30 closes this asymmetry, requiring the disqualifying-form treatment C-29 established for structural criteria to apply uniformly across depth/behavior criteria), and V-05 bounds the self-check at aspirational criteria leaving essential and recommended criteria outside the verification trace (C-31 completes the self-check scope to all 31 criteria across all weight classes) |
