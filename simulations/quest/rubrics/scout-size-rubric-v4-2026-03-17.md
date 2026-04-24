Written to `simulations/quest/rubrics/scout-size-rubric-v4-2026-03-17.md`.

---

**Two new aspirational criteria added (C-18 through C-19):**

| ID | Pattern source | What it checks |
|----|----------------|----------------|
| **C-18** | V-05 R3 "Pre-write gate" | A self-check confirmation block precedes the first analysis section, requiring scope boundary and break-even to be resolved before any dimension field is filled — structural gate, not an inline reminder |
| **C-19** | V-03 R3 "Leaky separation" (C-14 PARTIAL) | Adjacent sections that could receive a field type already owned by a canonical section carry an explicit prohibition rule — not just that a canonical section exists, but that neighboring sections are closed against bleed |

**What makes these genuinely new (not redundant with v3):**
- C-18 is not a refinement of C-09/C-10. Those check *presence* of scope exclusions and break-even. C-18 checks whether the *structural mechanism* (pre-write gate before section sequence) forces those fields as preconditions. You can pass C-09 and C-10 without C-18 — but only V-05 passed all three.
- C-19 is not a refinement of C-14. C-14 checks that unknowns have a canonical home section. C-19 checks that the sections *adjacent* to that home are explicitly closed. V-03 passes C-14 at the "has a section" level but fails C-19 — the CONFIDENCE Gap field with no prohibition is exactly the gap this criterion catches.

**Scoring model:** aspirational denominator bumped 9 -> 11. Max composite unchanged at 100.
urfaces, external systems). Must be a count or
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

---

## Scoring Model

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 11 * 10)
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

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-17 | Initial rubric — 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-17 | Added C-11 (specialization ownership), C-12 (named unknowns), C-13 (cross-signal synthesis); aspirational denominator 2 -> 5 |
| v3 | 2026-03-17 | Added C-14 (unknowns dedicated section), C-15 (hypothesis-revision lifecycle), C-16 (AMEND cascades to synthesis), C-17 (sections name failure modes); aspirational denominator 5 -> 9; sourced from R2 excellence signals |
| v4 | 2026-03-17 | Added C-18 (pre-analysis self-check gate), C-19 (cross-contamination prohibition guards); aspirational denominator 9 -> 11; sourced from R3 excellence signals — V-05 pre-write gate (only variation to pass C-09 + C-10), V-03 leaky separation finding (C-14 PARTIAL) |
