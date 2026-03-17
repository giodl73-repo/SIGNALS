Written to `simulations/quest/rubrics/scout-size-rubric-v6-2026-03-17.md`.

---

**Two new aspirational criteria added (C-22 through C-23):**

| ID | Pattern source | What it checks |
|----|----------------|----------------|
| **C-22** | V-03/V-04/V-05 R5 "Gate-as-atomic-commitment-block" | Synthesis names the pre-flight gate's structural label at both the anchor ("the hypothesis committed in PRE-FLIGHT GATE") and the verdict close. Passing C-21 (hypothesis in gate + synthesis confirms it) does not satisfy C-22 if synthesis references the hypothesis without naming its structural site. |
| **C-23** | V-02 R4 gap / V-03/V-04/V-05 R5 close | Prohibition guards name the canonical home by label — "scope was resolved in PRE-FLIGHT GATE, not in analysis steps" rather than bare "do not include here." Passing C-20 (all adjacent sections guarded) does not satisfy C-23 if no guard provides the navigational reference. |

**What makes these genuinely new (not redundant with v5):**

- C-22 is not a refinement of C-21. C-21 checks whether the hypothesis is inside the gate and whether synthesis confirms/revises it. C-22 checks whether synthesis names the gate by its structural label — once at the anchor, once at the verdict close. An output can pass C-21 with "my earlier estimate was confirmed" (structurally unanchored) and fail C-22.

- C-23 is not a refinement of C-20. C-20 checks whether every adjacent section carries a prohibition. C-23 checks whether those prohibitions name where the excluded content belongs. V-02 passes C-20 with INERTIA CHECK guards that say "do not add scope qualifications here" — and fails C-23 because the guard is a dead end without naming PRE-FLIGHT GATE as the destination.

**Scoring model:** aspirational denominator bumped 13 → 15. Max composite unchanged at 100.

**Expected R5 scores under v6:**

| Variation | Aspirational | Score |
|-----------|-------------|-------|
| V-01 (gate-embedded hypothesis) | 13/15 (fails C-20, C-23) | 98.67 |
| V-02 (full bilateral closure) | 13/15 (fails C-21, C-22) | 98.67 |
| V-03/V-04/V-05 | 15/15 | 100 |
, missing capability). Absence of this section
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
  that determined the rating — e.g., "HIGH because of distributed transaction boundary",
  "LOW because isolated namespace with no shared state". Bare tier labels are less
  useful downstream.
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
  AREA ("Do not include scope exclusions here. Scope exclusions belong in SCOPE
  EXCLUSIONS below."), COMPLEXITY ("Do not list what is out of scope here."),
  CONFIDENCE ("Do not list unknowns here... listing an unknown creates a second,
  structurally invisible record."), SYNTHESIS (closed against both unknowns and scope
  exclusions), and OPEN UNKNOWNS ("Do not list unknowns in CONFIDENCE above or in
  SYNTHESIS below."). The difference between C-19 and C-20 is the difference between
  one lock and a full containment mesh: C-19 requires at least one adjacent section
  to be closed; C-20 requires every section that could receive a canonical field type
  to be closed from every direction. An output can pass C-19 with partial closure and
  still fail C-20 if any canonical home lacks complete adjacent prohibition coverage.
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
  references an implied prior commitment that a reader cannot verify structurally:
  "I earlier estimated MEDIUM" points to an unlocated claim; "PRE-FLIGHT GATE
  committed MEDIUM" is structurally traceable. V-03/V-04/V-05 all achieve this:
  SYNTHESIS instructs "look back at PRE-FLIGHT GATE — state whether the analysis
  confirms, revises, or partially revises the preliminary hypothesis committed there,"
  and the closing line names the gate again. Sourced from R5 pattern:
  "Gate-as-atomic-commitment-block — synthesis references the gate by name at both
  ends, making the commitment chain structurally verifiable."
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
  completing the navigational chain. An output can pass C-20 with bare prohibitions
  ("do not include here" in all adjacent sections) and still fail C-23 if no
  prohibition names where the excluded content belongs. Sourced from R5 pattern:
  "INERTIA CHECK prohibition guard — the guard names the canonical home ('scope was
  resolved in PRE-FLIGHT GATE') rather than merely stating exclusion."
- **Pass condition**: For at least one canonical field type (scope exclusions, open
  unknowns), the prohibition guards in adjacent sections name the canonical home
  section by label — not just state a bare exclusion. Guards reading only "do not
  include scope exclusions here" without specifying where they belong fail C-23.

---

## Scoring Model

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 15 * 10)
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
  bilateral closure in all directions. V-01 R4 passes C-19, fails C-20: scope exclusion
  canonical home (PRE-FLIGHT GATE) has no adjacent prohibitions in SURFACE AREA or
  COMPLEXITY.
- C-21 integrates C-18 and C-15 at the structural level, sourced from the R4 gap where
  C-15 fails in both top-scoring variations. Passing both C-18 and C-15 independently
  does not satisfy C-21: the hypothesis must be elicited inside the gate, not placed
  elsewhere before analysis.
- C-22 is a refinement of C-21 sourced from R5. Passing C-21 requires hypothesis in
  gate and synthesis confirmation. C-22 requires synthesis to name the gate's structural
  label at both the anchor and the verdict — "committed in PRE-FLIGHT GATE" not "my
  earlier estimate." An output can pass C-21 and fail C-22 if the synthesis confirmation
  is structurally unanchored.
- C-23 is a refinement of C-20 sourced from R5. Passing C-20 requires all adjacent
  sections to carry prohibition rules. C-23 requires at least one of those rules to
  name the canonical home by label, not just state a bare exclusion. An output can pass
  C-20 with all adjacent sections guarded and still fail C-23 if no guard names where
  the excluded content belongs.

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-17 | Initial rubric — 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-17 | Added C-11 (specialization ownership), C-12 (named unknowns), C-13 (cross-signal synthesis); aspirational denominator 2 -> 5 |
| v3 | 2026-03-17 | Added C-14 (unknowns dedicated section), C-15 (hypothesis-revision lifecycle), C-16 (AMEND cascades to synthesis), C-17 (sections name failure modes); aspirational denominator 5 -> 9; sourced from R2 excellence signals |
| v4 | 2026-03-17 | Added C-18 (pre-analysis self-check gate), C-19 (cross-contamination prohibition guards); aspirational denominator 9 -> 11; sourced from R3 excellence signals — V-05 pre-write gate, V-03 leaky separation finding |
| v5 | 2026-03-17 | Added C-20 (complete bilateral closure mesh), C-21 (pre-flight gate elicits preliminary hypothesis); aspirational denominator 11 -> 13; sourced from R4 — V-02 comprehensive bilateral closure, structural gap where C-15 fails in both top-scoring R4 variations due to hypothesis having no structural anchor inside the gate |
| v6 | 2026-03-17 | Added C-22 (synthesis names gate commitment site at both ends), C-23 (prohibition guards name canonical home); aspirational denominator 13 -> 15; sourced from R5 — V-03/V-04/V-05 gate-as-atomic-commitment-block pattern (synthesis names PRE-FLIGHT GATE at anchor and verdict) and INERTIA CHECK guard naming canonical home ("scope was resolved in PRE-FLIGHT GATE") rather than bare exclusion |
