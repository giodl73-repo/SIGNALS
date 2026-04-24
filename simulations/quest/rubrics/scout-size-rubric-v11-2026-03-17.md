**C-32** is the single new criterion extracted from R10.

**Pattern source**: V-04 R10 — essential/recommended entries in the self-check carry a three-column table (ID / What to verify / Failing form), giving each C-01-C-08 item an exact disqualifying form alongside its pass condition.

**Why it's genuinely new**: C-31 tests weight-class *scope* (are C-01-C-08 present in the self-check at all?). C-32 tests weight-class *precision* (do those entries carry exact disqualifying forms?). V-03 passes C-31 with flat pass/fail entries for C-01-C-08 and fails C-32 because no essential/recommended item specifies the exact output pattern that would fail it. The criterion completes the precision-parity axis that C-29 opened for structural criteria and C-30 extended to depth/behavior aspirational criteria.

**Scoring update**: aspirational denominator 23 → 24. Max composite unchanged at 100.

| Variation | Aspirational | Score |
|-----------|-------------|-------|
| V-01 (C-30 only) | 22/24 (fails C-31, C-32) | 99.17 |
| V-02 (C-31 only) | 22/24 (fails C-30, C-32) | 99.17 |
| V-03 (C-30 + C-31, flat essential/recommended checklist) | 23/24 (fails C-32) | 99.58 |
| V-04 (disqualifying forms for C-01-C-08) | 24/24 | **100.00** |
with both lower and upper bound
  for the timeline signal.

### C-03 — Surface area is quantified by integration points
- **Weight**: essential
- **Category**: correctness
- **Description**: Surface area section identifies discrete integration points (APIs,
  hooks, namespaces, data stores, UI surfaces, external systems). Must be a count or
  enumerated list — not a vague qualifier like "moderate surface area".
- **Pass condition**: Output names or counts at least 2 distinct integration points,
  or explicitly states 0-1 with reasoning.

### C-04 — Inertia check is present and names the workaround cost
- **Weight**: essential
- **Category**: coverage
- **Description**: Output includes an explicit inertia check that names what teams
  currently do without this feature (the workaround) and characterizes its cost
  (time, error rate, manual effort, missing capability). Absence of this section
  is a hard fail — it is the signal's differentiator from a raw estimate.
- **Pass condition**: A clearly labeled inertia check section or paragraph identifies
  the current workaround and states at least one cost dimension.

### C-05 — Confidence level is stated with basis
- **Weight**: essential
- **Category**: depth
- **Description**: Output states a confidence level (percentage, tier, or LOW/MED/HIGH
  label) AND gives the primary reason for that level (e.g., "HIGH confidence — surface
  area well-understood from existing flow skill", "LOW confidence — cross-service
  dependencies uncharted"). Confidence without basis is not actionable.
- **Pass condition**: Confidence level is present AND at least one sentence explains
  why that level was assigned.

---

## Recommended Criteria (30 points total)

### C-06 — Team-size signal names required specializations
- **Weight**: recommended
- **Category**: depth
- **Description**: Team-size signal goes beyond headcount to name the types of
  specialists required (e.g., "1 backend + 1 infra", not just "2 engineers"). This
  lets program-plan route work correctly.
- **Pass condition**: Team-size signal identifies at least one role or specialization,
  not just a number.

### C-07 — Complexity rating is justified with at least one driver
- **Weight**: recommended
- **Category**: depth
- **Description**: The complexity tier (C-01) is accompanied by the primary driver
  that determined the rating — e.g., "HIGH because of distributed transaction
  boundary", "LOW because isolated namespace with no shared state". Bare tier labels
  are less useful downstream.
- **Pass condition**: At least one sentence following or inline with the complexity
  tier names what pushed it to that level.

### C-08 — AMEND instructions modify the stated output, not the process
- **Weight**: recommended
- **Category**: behavior
- **Description**: When an AMEND directive is present (adjust confidence thresholds
  or focus on a complexity dimension), the output reflects the amendment in its
  content — e.g., a revised confidence level, or expanded analysis of the named
  dimension. The skill should not just acknowledge the amendment; it should
  change the artifact.
- **Pass condition**: If AMEND is invoked, at least one substantive change in the
  output (different tier, revised confidence, expanded section) can be traced to
  the amendment. If no AMEND is present, criterion is scored as pass by default.

---

## Aspirational Criteria (10 points total)

### C-09 — Sizing signal explicitly scopes what is NOT included
- **Weight**: aspirational
- **Category**: depth
- **Description**: Output states at least one thing the sizing does NOT cover
  (out-of-scope sub-systems, deferred complexity, assumptions made). This prevents
  silent misreads when program-plan consumes the signal.
- **Pass condition**: At least one explicit exclusion, assumption, or out-of-scope
  boundary is named.

### C-10 — Inertia check includes a break-even signal
- **Weight**: aspirational
- **Category**: depth
- **Description**: Beyond naming the workaround cost, the output estimates when
  building the feature pays off relative to continued workaround cost — even as
  a rough qualitative signal ("break-even at ~4 uses/week", "never breaks even
  if adoption stays below 3 teams"). This is the highest-value form of the
  inertia check for investment decisions.
- **Pass condition**: Output contains a break-even estimate or explicitly states
  that break-even cannot be assessed and why.

### C-11 — Each named specialization states its implementation ownership
- **Weight**: aspirational
- **Category**: depth
- **Description**: Team-size signal goes beyond naming roles (C-06) to state what
  each specialization owns during implementation — e.g., "1 backend (owns event
  schema + storage layer) + 1 infra (owns deployment pipeline)". Without ownership
  scope, the role list is decorative and program-plan still needs a follow-up
  conversation to assign work. Sourced from V-02 Step 6 and V-03 INERTIA ANALYST,
  the two highest-scoring R1 variations, both of which required "what they own during
  the build."
- **Pass condition**: At least one named specialization includes a description of
  its implementation scope or ownership area.

### C-12 — Confidence section names specific unknowns that would change the rating
- **Weight**: aspirational
- **Category**: depth
- **Description**: A confidence basis (C-05) is actionable only when the output also
  names the specific unknowns that, if resolved, would raise or lower the rating —
  e.g., "LOW confidence; HIGH once cross-service contracts are published." A basis
  without named unknowns leaves the reader unable to close the gap. Sourced from
  V-02 Step 6 ("name the specific unknowns driving it down") and V-03 RISK ("Name
  any unknowns that would move confidence down"), both present in the two
  highest-scoring R1 variations.
- **Pass condition**: At least one concrete unknown is named that would move the
  confidence level if resolved, or output explicitly states no remaining unknowns.

### C-13 — Closing synthesis integrates signals, not just restates them
- **Weight**: aspirational
- **Category**: depth
- **Description**: Output contains a concluding statement that draws a decision-
  relevant conclusion by cross-referencing two or more signal dimensions — e.g.,
  "HIGH complexity + LOW confidence in dependency map argues for deferral until
  contracts are published" or "LOW surface area + HIGH inertia cost argues for
  fast-track even at MEDIUM complexity." A closing that merely restates each field
  in sequence is juxtaposition, not synthesis. Sourced from V-03 R1 deduction:
  "verbose juxtaposition over true synthesis" was the primary structural gap in
  the role-sequence variation.
- **Pass condition**: At least one sentence cross-references two or more signal
  dimensions (complexity, timeline, confidence, inertia) to produce a directional
  recommendation or decision-relevant observation.

### C-14 — Open unknowns appear in a dedicated section with typed fields
- **Weight**: aspirational
- **Category**: structure
- **Description**: Refinement of C-12. Naming unknowns inside the confidence basis
  paragraph makes omissions hard to detect — the reader must parse prose to notice
  a missing entry. When unknowns appear in a structurally separate section with typed
  fields (Unknown: / Impact: / Movement:), any gap is visually self-evident. Sourced
  from V-02 R2, the "Unknowns-as-Section" variation, which scored full marks on C-12
  precisely because the section boundary made omission structurally impossible to hide.
  Output can still pass C-12 with prose-embedded unknowns; C-14 rewards the
  higher-reliability structural form.
- **Pass condition**: Open unknowns (or an explicit "no open unknowns" declaration)
  appear in a named section or block separate from the confidence basis, with at least
  one field-typed entry or a structured HIGH-confidence fallback statement.

### C-15 — Synthesis confirms or revises a prior stated hypothesis
- **Weight**: aspirational
- **Category**: depth
- **Description**: Refinement of C-13. A synthesis derived post-hoc from already-
  populated fields can still be juxtaposition dressed as reasoning. When the output
  commits to a preliminary hypothesis earlier ("initial hypothesis: MEDIUM complexity,
  3-5 sprints") and the synthesis explicitly confirms or revises that commitment,
  the reasoning is verifiable — the model cannot retroactively produce a conclusion
  that merely echoes the inputs. Sourced from V-04 R2, the "Hypothesis-Revision"
  variation, which achieved the strongest structural guarantee of genuine C-13
  cross-dimensional reasoning.
- **Pass condition**: A preliminary hypothesis or prior estimate appears before the
  detailed analysis sections, and the synthesis section explicitly states whether
  the hypothesis was confirmed, revised, or partially revised, with the dimension
  that changed.

### C-16 — AMEND cascades to synthesis when the amended dimension is cited there
- **Weight**: aspirational
- **Category**: behavior
- **Description**: Extension of C-08 and C-13. When an AMEND directive changes a
  signal dimension that is also referenced in the synthesis (e.g., AMEND raises
  confidence and synthesis cited LOW confidence as the deferral argument), the
  synthesis must be re-evaluated to reflect whether the cross-signal conclusion
  still holds. Acknowledging the AMEND in the amended section but leaving the
  synthesis unchanged is a silent contradiction. Sourced from R2 pattern:
  "AMEND cascade to synthesis — amendment must re-evaluate synthesis when the
  amended dimension changes the cross-signal conclusion."
- **Pass condition**: If AMEND is invoked and the amended dimension appears in the
  synthesis, the synthesis conclusion is updated or explicitly reaffirmed in light
  of the amendment. Default pass if no AMEND is present, or if the amended
  dimension is not cited in the synthesis.

### C-17 — Aspirational sections name their failure mode
- **Weight**: aspirational
- **Category**: depth
- **Description**: For synthesis (C-13) and unknowns (C-12), an output that
  explicitly distinguishes the required form from the anti-pattern demonstrates
  that the model is not passively populating fields but actively enforcing quality.
  Examples: noting that restating sections in sequence is juxtaposition and does
  not satisfy synthesis; noting that a placeholder unknown ("dependencies may exist")
  does not satisfy the named-unknowns requirement. Sourced from the V-05 R2
  "Rules: sub-sections" pattern, where explicit negative examples and hard mandates
  were the primary driver of execution reliability at score 100.
- **Pass condition**: At least one aspirational section (synthesis or unknowns)
  contains a sentence that names the anti-pattern being avoided or explicitly states
  what form of response would fail the criterion.

### C-18 — A pre-analysis self-check gate precedes the first dimension section
- **Weight**: aspirational
- **Category**: structure
- **Description**: V-05 was the only R3 variation to pass both C-09 (scope exclusions)
  and C-10 (break-even signal) — exclusively because it mandated a self-check
  confirmation block before the first analysis section. Without this gate, models
  defer exclusions and break-even until the end or omit them entirely because the
  section sequence does not force the question. A self-check that fires before any
  dimension field is filled ensures scope boundary and break-even are resolved as
  preconditions, not afterthoughts. Structural gate, not a section reminder.
- **Pass condition**: A self-check, confirmation block, or pre-flight step appears
  before the first analysis section and requires the model to explicitly address
  scope boundary (what is NOT included) and break-even signal before proceeding.
  Inline reminders within sections do not satisfy this criterion.

### C-19 — Sections that could receive duplicate field types carry explicit prohibition guards
- **Weight**: aspirational
- **Category**: structure
- **Description**: V-03 scored C-14 PARTIAL in R3: a dedicated OPEN UNKNOWNS section
  existed with typed fields, but the CONFIDENCE section still carried a Gap field
  with no prohibition — the structural separation was leaky. V-01, V-04, and V-05
  all included an explicit "do not list unknowns here" mandate inside the confidence
  section, making cross-contamination impossible rather than merely unlikely.
  This prohibition guard is a distinct structural property from having a canonical
  home section: a section can exist without its adjacent sections being closed.
  Sourced from the V-03 R3 "Leaky separation" finding.
- **Pass condition**: When a canonical section exists for a field type (e.g., OPEN
  UNKNOWNS for unknowns, SYNTHESIS for cross-signal conclusions), at least one
  adjacent section that could plausibly receive the same content carries an explicit
  prohibition rule (e.g., "do not embed unknowns here — list them in OPEN UNKNOWNS").

### C-20 — Complete closure mesh: every canonical section is closed bilaterally
- **Weight**: aspirational
- **Category**: structure
- **Description**: V-02 R4 demonstrated "comprehensive bilateral closure" — the
  exemplary form of C-19 that C-19's minimum pass does not capture. V-01 R4 passes
  C-19 (CONFIDENCE carries a prohibition against unknowns) but fails C-20: SURFACE
  AREA and COMPLEXITY carry no prohibition against scope exclusions, leaving the scope
  exclusion canonical home one-way protected. V-02 closes every direction: SURFACE
  AREA ("Do not include scope exclusions here."), COMPLEXITY ("Do not list what is
  out of scope here."), CONFIDENCE ("Do not list unknowns here."), SYNTHESIS (closed
  against both unknowns and scope exclusions), and OPEN UNKNOWNS ("Do not list
  unknowns in CONFIDENCE above or in SYNTHESIS below."). The difference between C-19
  and C-20 is the difference between one lock and a full containment mesh: C-19
  requires at least one adjacent section to be closed; C-20 requires every section
  that could receive a canonical field type to be closed from every direction.
- **Pass condition**: For every canonical home section (OPEN UNKNOWNS, SCOPE
  EXCLUSIONS, etc.), ALL sections that could plausibly receive the same content carry
  explicit prohibition rules — no unguarded adjacent section remains for any canonical
  field type.

### C-21 — Pre-flight gate elicits a preliminary hypothesis before analysis proceeds
- **Weight**: aspirational
- **Category**: structure
- **Description**: Both V-01 and V-02 in R4 fail C-15 despite being the two highest-
  scoring variations. V-01 has a pre-flight gate (C-18 PASS) but no preliminary
  hypothesis. V-02 has comprehensive bilateral closure (C-20 PASS) but also no
  preliminary hypothesis. In both cases, the preliminary hypothesis is structurally
  independent of the gate and therefore omitted. A variation that folds the hypothesis
  commitment into the pre-flight gate forces the model to state its predicted tier and
  timeline before any dimension is analyzed — making the hypothesis verifiable against
  the gate inputs (scope boundary and break-even signal already resolved), not
  constructed post-hoc from completed fields. This is a structural advancement beyond
  C-15 (hypothesis exists but is standalone) and C-18 (gate exists but does not elicit
  hypothesis): the gate becomes the site of the commitment. Sourced from the R4
  structural gap where C-15 fails in both top variations because the hypothesis has
  no structural anchor forcing it before analysis.
- **Pass condition**: The pre-flight gate (satisfying C-18) includes a step requiring
  a preliminary complexity tier and timeline estimate to be stated before the first
  analysis section opens, AND the synthesis section explicitly confirms or revises this
  gate-elicited commitment. An output that passes C-18 and C-15 independently (gate
  present, hypothesis present but not inside the gate) does not satisfy C-21.

### C-22 — Synthesis names the gate commitment site at both ends of the chain
- **Weight**: aspirational
- **Category**: structure
- **Description**: Refinement of C-21. An output satisfies C-21 by placing the
  hypothesis inside the pre-flight gate and having synthesis confirm or revise it.
  C-22 requires synthesis to name the gate's structural label explicitly — once when
  anchoring the prior commitment ("the hypothesis committed in PRE-FLIGHT GATE") and
  once when closing the verdict ("this confirms/revises the preliminary hypothesis
  committed in PRE-FLIGHT GATE"). Without naming the structural anchor, synthesis
  references an implied prior commitment that a reader cannot verify structurally.
  V-03/V-04/V-05 all achieve this: SYNTHESIS instructs "look back at PRE-FLIGHT GATE
  — state whether the analysis confirms, revises, or partially revises the preliminary
  hypothesis committed there," and the closing line names the gate again. Sourced from
  R5 pattern: "Gate-as-atomic-commitment-block — synthesis references the gate by name
  at both ends, making the commitment chain structurally verifiable."
- **Pass condition**: Synthesis section explicitly names the pre-flight gate (or
  equivalent structural label) when anchoring the prior commitment AND when stating
  the confirm/revise verdict. An output that satisfies C-21 but refers to the
  hypothesis only as "my earlier estimate" or "the preliminary hypothesis" without
  naming its structural home fails C-22.

### C-23 — Prohibition guards name the canonical home, not just state the exclusion
- **Weight**: aspirational
- **Category**: structure
- **Description**: Refinement of C-20. An output satisfies C-20 by ensuring every
  adjacent section carries a prohibition rule for each canonical field type. C-23
  requires those prohibition rules to name the canonical home: "scope was resolved
  in PRE-FLIGHT GATE, not in analysis steps" rather than "do not include scope
  exclusions here." The navigational reference completes the guard — a reader
  following the prohibition knows exactly where the excluded content belongs and
  where to find it. Without naming the home, the prohibition is a dead end: it
  closes a door without pointing to the right room. V-02 R4 partial: guards in
  INERTIA CHECK say "Do not add scope qualifications here" but do not name
  PRE-FLIGHT GATE as the canonical home. V-03/V-04/V-05 close this: the INERTIA
  CHECK guard reads "scope was resolved in PRE-FLIGHT GATE, not in analysis steps,"
  completing the navigational chain. Sourced from R5 pattern: "INERTIA CHECK
  prohibition guard — the guard names the canonical home rather than merely stating
  exclusion."
- **Pass condition**: For at least one canonical field type (scope exclusions, open
  unknowns), the prohibition guards in adjacent sections name the canonical home
  section by label — not just state a bare exclusion. Guards reading only "do not
  include scope exclusions here" without specifying where they belong fail C-23.

### C-24 — Synthesis provides a structured commitment-chain trace, not just a prose reference
- **Weight**: aspirational
- **Category**: structure
- **Description**: Refinement of C-22. An output satisfies C-22 by naming PRE-FLIGHT
  GATE at both the anchor and the verdict close in prose synthesis. C-24 requires a
  structured trace that makes all three steps of the commitment chain scannable without
  parsing narrative: (1) the gate-committed hypothesis, (2) the analysis findings that
  bear on it, (3) the confirm/revise verdict. A prose paragraph that mentions PRE-FLIGHT
  GATE twice satisfies C-22 but leaves the chain embedded in sentences — a reader must
  re-read to check logical continuity. A structured trace (e.g., a labeled block:
  "Gate commitment: MEDIUM / 3-5 sprints | Analysis: surface area LOW, no cross-service
  dependencies | Verdict: revised DOWN to LOW / 2-3 sprints") makes the chain auditable
  at a glance. Sourced from R6 V-03 axis annotation "No self-check machinery" — V-04/
  V-05 R6 demonstrate that a structured trace block hardens commitment-chain integrity
  beyond the prose-reference form required by C-22.
- **Pass condition**: Synthesis includes a structured block, labeled list, or
  field-formatted trace that explicitly places the gate commitment, the analysis
  evidence, and the verdict on separate labeled lines or fields — not folded into a
  single prose paragraph. An output that satisfies C-22 through prose alone fails C-24.

### C-25 — PRE-FLIGHT GATE forward-references the sections that enforce its scope and hypothesis
- **Weight**: aspirational
- **Category**: structure
- **Description**: Complement of C-23. C-23 requires guards (in adjacent sections) to
  name the canonical home — the inbound direction of the navigational mesh. C-25
  requires the canonical home (PRE-FLIGHT GATE) to name its enforcement sections
  outbound — e.g., "Scope exclusions committed here are enforced in: SURFACE AREA,
  COMPLEXITY, INERTIA CHECK, and SYNTHESIS." Without this forward-reference, the gate
  is a declaration that assumes its enforcement sections exist and honor it; with it,
  the gate is a contract that explicitly names its guarantors. Together C-23 and C-25
  form a fully bidirectional navigational mesh: every guard points home (C-23) and
  every canonical home names its guards (C-25). Sourced from R6 V-05 pattern where
  PRE-FLIGHT GATE includes a forward-reference list naming the sections that will
  enforce its scope commitment.
- **Pass condition**: PRE-FLIGHT GATE (or the canonical home for scope exclusions and
  hypothesis commitment) includes a statement that names at least two downstream
  sections responsible for enforcing its scope exclusions or hypothesis commitment.
  A gate that commits scope and hypothesis without naming its enforcement sections
  fails C-25 even if those sections carry navigational guards back to the gate.

### C-26 — Synthesis embeds a structural AMEND re-evaluation directive
- **Weight**: aspirational
- **Category**: behavior
- **Description**: Refinement of C-16. C-16 is behavioral: did the output change when
  AMEND was invoked? It defaults to pass when no AMEND is present, which means an
  output can achieve C-16 compliance on every run without ever containing a structural
  rule that guarantees cascade behavior. C-26 requires the synthesis section itself to
  carry a written directive — e.g., "If an AMEND directive is present and affects a
  dimension cited in this section, re-evaluate the cross-signal conclusion before
  closing" — so that AMEND cascade is structurally enforced regardless of whether AMEND
  is invoked in the current run. An output that passes C-16 by default (no AMEND
  invoked) with no structural directive in synthesis fails C-26; an output that passes
  C-16 because AMEND happened to cascade correctly in execution, but carries no
  written re-evaluation rule, also fails C-26. Sourced from V-02 R7: the only variation
  where SYNTHESIS contains an explicit AMEND re-evaluation instruction written into the
  section template, making C-16 compliance a structural property rather than a
  behavioral one.
- **Pass condition**: The synthesis section contains an explicit written rule or
  directive requiring re-evaluation of its cross-signal conclusion when an AMEND
  directive is present — independent of whether AMEND is invoked in the current run.
  A synthesis that passes C-16 through default pass or incidental cascade without a
  structural directive fails C-26.

### C-27 — Every aspirational section carries a dedicated FAILURE MODE labeled block
- **Weight**: aspirational
- **Category**: depth
- **Description**: Refinement of C-17. C-17 requires at least one aspirational section
  (synthesis or unknowns) to name its failure mode — even as an inline sentence
  ("a generic placeholder fails this criterion"). C-27 requires every aspirational
  section with a nontrivial pass condition to carry a dedicated labeled FAILURE MODE
  block that states the anti-pattern explicitly, making non-compliance structurally
  visible without re-reading prose. The distinction between inline mention and dedicated
  block is not cosmetic: an inline mention can be overlooked, while a labeled FAILURE
  MODE block cannot be absent without a visible structural gap. V-01 fails because OPEN
  UNKNOWNS carries no failure-mode coverage at all. V-02 and V-03 fail because their
  OPEN UNKNOWNS failure-mode coverage is an inline phrase embedded in a requirement
  sentence — not a dedicated labeled block. V-04/V-05 pass because both SYNTHESIS and
  OPEN UNKNOWNS carry standalone FAILURE MODE blockquotes. Sourced from V-04/V-05 R7.
- **Pass condition**: Every aspirational section with a nontrivial pass condition
  (synthesis and open unknowns at minimum) contains a dedicated labeled FAILURE MODE
  block or blockquote — not an inline anti-pattern mention embedded in prose. An output
  that passes C-17 (one section names failure mode) with only inline failure-mode
  language fails C-27 unless that language appears in a structurally separate labeled
  block.

### C-28 — Output includes a per-criterion self-check trace covering all aspirational criteria
- **Weight**: aspirational
- **Category**: structure
- **Description**: V-04 R8 adds a distinct self-check block after the complete output
  that explicitly evaluates each aspirational criterion by ID, with pass/fail
  determination and supporting evidence cited per criterion. This is a meta-verification
  layer that section-level FAILURE MODE blocks (C-27) cannot substitute for: C-27 places
  structural failure-mode signals inside each content section; C-28 requires a separate
  artifact that systematically audits every criterion collectively. V-03 achieves 19/19
  under v8 with dual FAILURE MODE blocks (C-27) and a structural AMEND directive (C-26)
  but carries no self-check machinery — structural failure-mode blocks at the section
  level guarantee visibility of anti-patterns within each section but do not guarantee
  that every pass condition was explicitly evaluated. V-04 closes this gap by making
  compliance-evaluation itself a structural artifact. Sourced from V-04 R8: the
  "27-criterion self-check."
- **Pass condition**: Output includes a structured block or section — distinct from
  the content sections and their FAILURE MODE blocks — that traces each aspirational
  criterion by ID to an explicit pass/fail determination with supporting evidence.
  An output that passes C-27 with dedicated FAILURE MODE blocks in every aspirational
  section but carries no collective per-criterion evaluation fails C-28.

### C-29 — Self-check items for all structural criteria include exact structural disqualifying forms
- **Weight**: aspirational
- **Category**: structure
- **Description**: Refinement of C-28. V-04 includes definition-level discriminators in
  its self-check for C-26 and C-27 only. V-05 extends this treatment to all structural
  criteria (C-18 through C-27): every structural criterion carries an exact disqualifying
  form alongside its pass condition, not just the two most recently added. V-04 achieves
  precision for the latest-round criteria; V-05 achieves it uniformly across the full
  set, ensuring older structural criteria do not regress to pass-only descriptions as
  the denominator grows. Sourced from V-05 R8.
- **Pass condition**: Self-check items for all structural criteria (C-18 through C-27)
  include both a pass condition and an exact structural disqualifying form — a specific
  structural pattern that looks like compliance but fails. An output that satisfies C-28
  with exact disqualifying forms only for C-26 and C-27 fails C-29 unless every other
  structural criterion carries equivalent precision.

### C-30 — Self-check items for all depth and behavior aspirational criteria include exact disqualifying forms
- **Weight**: aspirational
- **Category**: structure
- **Description**: Refinement of C-29. C-29 requires exact disqualifying forms for all
  structural criteria (C-18-C-27) in the per-criterion self-check. The depth and behavior
  criteria (C-09-C-17) in V-05's self-check carry only pass-condition descriptions — the
  same state C-18-C-25 were in before C-29 required structural precision there. V-05
  achieves C-29 by extending disqualifying-form coverage uniformly to all structural
  criteria; the analogous gap is depth/behavior criteria (C-09-C-17) carrying only pass
  conditions. This creates an asymmetry: the structural criteria carry exact disqualifying
  forms, but the foundational depth/behavior criteria — which define what quality content
  looks like — do not. An output can pass C-29 with full structural precision while
  depth/behavior self-check items consist entirely of pass-condition descriptions.
  Sourced from V-05 R9 "depth/behavior precision gap."
- **Pass condition**: Self-check items for all depth and behavior aspirational criteria
  (C-09 through C-17) include both a pass condition and an exact disqualifying form — a
  specific output pattern that satisfies the surface signal but fails the criterion. An
  output that satisfies C-29 with exact disqualifying forms only for structural criteria
  (C-18-C-27) fails C-30 unless every depth/behavior criterion carries equivalent
  disqualifying-form precision. Passing C-29 does not satisfy C-30 even if depth/behavior
  items exist in the self-check with only pass-condition descriptions.

### C-31 — Self-check provides complete criterion coverage across all weight classes
- **Weight**: aspirational
- **Category**: structure
- **Description**: Refinement of C-28. C-28 requires a per-criterion self-check covering
  all aspirational criteria. Combined with C-29 and C-30, a complete aspirational
  self-check with full disqualifying-form precision exists. The self-check remains bounded
  at aspirational criteria by the C-28 definition; essential and recommended criteria
  (C-01-C-08) are outside the verification trace. A complete verification artifact should
  audit every criterion regardless of weight class — an essential failure (e.g., sprint
  range as a point estimate) disqualifies the output entirely, yet the self-check under
  C-28 cannot detect it. Recommended failures (e.g., specializations named without
  ownership scope) are equally invisible. Extending the per-criterion audit to cover
  C-01-C-08 closes the scope gap: the self-check becomes a complete compliance trace
  across all 31 criteria, not a 23-criterion aspirational audit with an implicit
  assumption that essential and recommended criteria pass. Sourced from V-05 R9
  "self-check bounded at aspirational."
- **Pass condition**: The per-criterion self-check (satisfying C-28) includes coverage of
  all essential (C-01-C-05) and recommended (C-06-C-08) criteria in addition to all
  aspirational criteria — each with a pass/fail determination and supporting evidence. An
  output that satisfies C-28, C-29, and C-30 with a complete 23-criterion aspirational
  audit fails C-31 if essential or recommended criteria are absent from the verification
  trace.

### C-32 — Self-check items for all essential and recommended criteria include exact disqualifying forms
- **Weight**: aspirational
- **Category**: structure
- **Description**: Refinement of C-31. C-31 requires the self-check to extend coverage
  to essential (C-01-C-05) and recommended (C-06-C-08) criteria — each with a pass/fail
  determination and supporting evidence. V-03 satisfies C-31 with flat checklist entries
  for C-01-C-08: each criterion has a pass/fail determination, but the items carry only
  pass-condition descriptions with no disqualifying form. V-04 extends the
  disqualifying-form treatment initiated by C-29 (structural criteria) and C-30
  (depth/behavior aspirational criteria) to all essential and recommended criteria:
  each C-01-C-08 item in V-04's self-check carries both a pass condition and an exact
  failing form (e.g., for C-02: "a point estimate '3 sprints' fails even if sprint
  range language appears elsewhere in the output"; for C-04: "naming the workaround
  without a cost dimension fails"). This completes disqualifying-form parity across all
  weight classes — structural (C-29), depth/behavior aspirational (C-30), and
  essential/recommended (C-32). An output can pass C-31 with a full 31-criterion
  coverage trace and still fail C-32 if essential and recommended self-check items
  consist of pass-condition descriptions only. Sourced from V-04 R10 "essential/
  recommended disqualifying-form extension": V-04 is the first variation to achieve
  complete precision uniformity — exact disqualifying forms for every criterion across
  all weight classes and all categories.
- **Pass condition**: Self-check items for all essential (C-01-C-05) and recommended
  (C-06-C-08) criteria include both a pass condition and an exact disqualifying form —
  a specific output pattern that satisfies the surface signal but fails the criterion.
  An output that satisfies C-31 with essential/recommended entries carrying only pass
  conditions fails C-32. Passing C-31 does not satisfy C-32 if any essential or
  recommended self-check item lacks a disqualifying-form specification.

---

## What makes C-32 genuinely new (not redundant with v10)

**C-32 is not a refinement of C-31.** C-31 extends the self-check's scope to include
essential and recommended criteria — weight class scope is C-31's discriminator. C-32
requires those newly-included items to carry the same disqualifying-form precision
that C-29 established for structural criteria and C-30 established for depth/behavior
criteria. Precision parity across weight classes is C-32's discriminator.

An output can pass C-31 with a flat checklist covering all 32 criteria (pass/fail
entries for each, evidence cited) and still fail C-32 if the essential/recommended
entries carry only pass-condition descriptions. C-31 tests whether C-01-C-08 are
present in the verification trace; C-32 tests whether those entries have the same
precision treatment that the aspirational entries receive under C-29 and C-30.

The progression is a single axis extended across four weight-class/category
combinations:
- C-29: structural aspirational criteria (C-18-C-27) — exact disqualifying forms
- C-30: depth/behavior aspirational criteria (C-09-C-17) — exact disqualifying forms
- C-32: essential and recommended criteria (C-01-C-08) — exact disqualifying forms

Together C-29, C-30, and C-32 require that every criterion in the self-check — across
all three aspirational categories and both non-aspirational weight classes — carries
an exact disqualifying form. The self-check becomes a complete, uniform precision
audit at 32 criteria, not a graduated system where structural precision is highest and
essential/recommended precision lowest.

---

## Scoring Model

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 24 * 10)
```

**Golden threshold**: All 5 essential criteria pass AND composite >= 80.

| Band | Composite | Meaning |
|------|-----------|---------|
| Gold | >= 80, all essential pass | Publish-ready sizing signal |
| Silver | >= 60, all essential pass | Useful but missing depth |
| Bronze | >= 40, <=2 essential fail | Partial signal, needs revision |
| Fail | Any essential fail | Output not usable downstream |

---

## Expected R10 scores under v11

| Variation | Aspirational | Score |
|-----------|-------------|-------|
| V-01 (depth/behavior disqualifying forms only) | 22/24 (fails C-31, C-32) | 99.17 |
| V-02 (essential/recommended scope extension only) | 22/24 (fails C-30, C-32) | 99.17 |
| V-03 (minimal combination C-30 + C-31) | 23/24 (fails C-32) | 99.58 |
| V-04 (fuller integration, disqualifying forms for C-01-C-08) | 24/24 | **100.00** |

V-03 drops from 23/23 (100.00 under v10) to 23/24 (99.58). The new criterion targets
the precision gap V-03 leaves in the essential/recommended self-check entries: flat
checklist pass/fail records without disqualifying forms. V-04 is the R10 gold standard
— the first variation to achieve complete disqualifying-form precision across all weight
classes and categories.

---

## Evaluation Notes

- C-04 (inertia check) is the highest-signal differentiator — a sizing output without
  it is indistinguishable from a naive estimate.
- C-02 (sprint range) guards against false precision; point estimates imply certainty
  that sizing signals never have.
- C-08 only activates on AMEND invocations; default-pass otherwise to avoid penalizing
  non-amend runs.
- Surface area (C-03) and team-size (C-06) together feed `program-plan` routing — weak
  values here are the most common downstream failure mode.
- C-11 and C-12 are upward refinements of C-06 and C-05 respectively: an output can
  pass the essential/recommended bar and still fail these if ownership scope and named
  unknowns are absent.
- C-13 is the hardest aspirational to pass mechanically; it requires the model to
  reason across dimensions rather than populate fields in sequence.
- C-14 is a structural refinement of C-12 — output can pass C-12 with prose-embedded
  unknowns and still fail C-14; C-14 rewards the form that makes omissions self-evident.
- C-15 is a structural refinement of C-13 — hypothesis-first forces the conclusion to
  be verifiable against a prior commitment, not constructed post-hoc.
- C-16 activates only on AMEND + synthesis overlap; default-pass otherwise.
- C-17 passes when the output demonstrates anti-pattern awareness, not merely avoidance.
- C-18 and C-19 are structural gate criteria sourced from R3: C-18 requires a pre-write
  gate (not a section reminder) that fires before any dimension field is filled; C-19
  requires adjacent sections to be closed against field bleed, not merely that a
  canonical section exists. An output can pass C-14 and still fail C-19 if the
  confidence section carries no prohibition.
- C-20 is a refinement of C-19 sourced from R4. Passing C-19 requires at least one
  adjacent section closed; C-20 requires every canonical home to be fully surrounded —
  bilateral closure in all directions.
- C-21 integrates C-18 and C-15 at the structural level, sourced from the R4 gap where
  C-15 fails in both top-scoring variations. Passing both C-18 and C-15 independently
  does not satisfy C-21: the hypothesis must be elicited inside the gate.
- C-22 is a refinement of C-21 sourced from R5. Passing C-21 requires hypothesis in
  gate and synthesis confirmation. C-22 requires synthesis to name the gate's structural
  label at both the anchor and the verdict.
- C-23 is a refinement of C-20 sourced from R5. Passing C-20 requires all adjacent
  sections to carry prohibition rules. C-23 requires at least one of those rules to
  name the canonical home by label.
- C-24 is a refinement of C-22 sourced from R6. Passing C-22 allows prose synthesis
  that mentions the gate twice. C-24 requires a structured, scannable commitment-chain
  trace on separate labeled lines.
- C-25 is the outbound complement of C-23, sourced from R6. C-23 closes the inbound
  direction (guards name home); C-25 closes the outbound direction (home names guards).
  Together they form a fully bidirectional navigational mesh.
- C-26 is a structural upgrade of C-16, sourced from R7. C-16 defaults to pass when no
  AMEND is invoked. C-26 requires a written directive enforcing AMEND re-evaluation
  structurally — independent of whether AMEND fires.
- C-27 is a structural upgrade of C-17, sourced from R7. C-17 requires at least one
  aspirational section to name its failure mode. C-27 requires every aspirational
  section to carry a dedicated labeled FAILURE MODE block.
- C-28 is a meta-layer above C-27, sourced from R8. C-27 ensures section-level
  failure-mode blocks. C-28 requires a separate collective self-check artifact that
  evaluates every criterion by ID.
- C-29 is a refinement of C-28, sourced from R8. C-28 requires the self-check to exist.
  C-29 requires structural criteria items (C-18-C-27) to include exact disqualifying
  forms. Coverage uniformity across structural criteria is the discriminator.
- C-30 is a category extension of C-29, sourced from R9. C-29 achieves structural-
  category uniformity (C-18-C-27 all have exact disqualifying forms). C-30 requires the
  same treatment for depth/behavior criteria (C-09-C-17). An output can pass C-29 and
  fail C-30 if any depth/behavior criterion in the self-check carries only a pass
  condition.
- C-31 is a scope extension of C-28, sourced from R9. C-28 bounds the self-check at
  aspirational criteria. C-31 extends the verification scope to include essential and
  recommended criteria. An output can satisfy C-28+C-29+C-30 with a 23-criterion
  aspirational audit and fail C-31 if essential and recommended criteria have no
  verification trace entries.
- C-32 is a precision extension of C-31, sourced from R10. C-31 requires essential and
  recommended criteria to be present in the self-check. C-32 requires those entries to
  carry exact disqualifying forms — the same precision treatment C-29 established for
  structural criteria and C-30 for depth/behavior criteria. An output can satisfy C-31
  with a flat pass/fail checklist for C-01-C-08 and fail C-32 if no essential or
  recommended entry specifies the exact output pattern that would fail the criterion.
  V-04 R10 is the first variation to achieve complete precision parity across all weight
  classes: exact disqualifying forms for structural (C-29), depth/behavior aspirational
  (C-30), and essential/recommended (C-32) criteria in the same self-check artifact.

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-17 | Initial rubric — 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-17 | Added C-11 (specialization ownership), C-12 (named unknowns), C-13 (cross-signal synthesis); aspirational denominator 2 -> 5 |
| v3 | 2026-03-17 | Added C-14 (unknowns dedicated section), C-15 (hypothesis-revision lifecycle), C-16 (AMEND cascades to synthesis), C-17 (sections name failure modes); aspirational denominator 5 -> 9; sourced from R2 excellence signals |
| v4 | 2026-03-17 | Added C-18 (pre-analysis self-check gate), C-19 (cross-contamination prohibition guards); aspirational denominator 9 -> 11; sourced from R3 excellence signals |
| v5 | 2026-03-17 | Added C-20 (complete bilateral closure mesh), C-21 (pre-flight gate elicits preliminary hypothesis); aspirational denominator 11 -> 13; sourced from R4 |
| v6 | 2026-03-17 | Added C-22 (synthesis names gate commitment site at both ends), C-23 (prohibition guards name canonical home); aspirational denominator 13 -> 15; sourced from R5 |
| v7 | 2026-03-17 | Added C-24 (synthesis provides structured commitment-chain trace), C-25 (PRE-FLIGHT GATE forward-references its enforcement sections); aspirational denominator 15 -> 17; sourced from R6 |
| v8 | 2026-03-17 | Added C-26 (synthesis embeds structural AMEND re-evaluation directive), C-27 (every aspirational section carries dedicated FAILURE MODE labeled block); aspirational denominator 17 -> 19; sourced from R7 |
| v9 | 2026-03-17 | Added C-28 (per-criterion self-check trace covering all aspirational criteria), C-29 (self-check items for all structural criteria include exact structural disqualifying forms); aspirational denominator 19 -> 21; sourced from R8 |
| v10 | 2026-03-17 | Added C-30 (self-check items for all depth/behavior aspirational criteria include exact disqualifying forms), C-31 (self-check extends to cover essential and recommended criteria C-01-C-08); aspirational denominator 21 -> 23; sourced from R9 — V-05 achieves 21/21 under v9 but depth/behavior self-check items (C-09-C-17) carry only pass conditions (C-30 closes this asymmetry) and self-check is bounded at aspirational criteria leaving C-01-C-08 outside the verification trace (C-31 extends scope to all 31 criteria) |
| v11 | 2026-03-17 | Added C-32 (self-check items for all essential and recommended criteria include exact disqualifying forms); aspirational denominator 23 -> 24; sourced from R10 — V-03 achieves 23/23 under v10 (first to pass C-30+C-31 together) but essential/recommended self-check entries (C-01-C-08) carry only pass-condition descriptions, leaving precision asymmetry between aspirational criteria (exact disqualifying forms via C-29+C-30) and essential/recommended criteria (pass conditions only); V-04 closes this by extending the disqualifying-form treatment to all essential and recommended self-check items, completing precision parity across all weight classes |
