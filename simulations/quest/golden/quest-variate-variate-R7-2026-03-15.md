# quest-variate Variate — Round 7

**Date:** 2026-03-15
**Skill:** quest-variate
**Rubric:** v7 (C-01 through C-34; essential C-01–C-05)
**Round:** R7 — 3 single-axis passes + 2 combination passes (C-04 combination exception applies to V-04 and V-05)

---

## Pre-Generation: Per-Axis Pole Declaration (C-16)

Before any variation body is written, declare the baseline pole for each axis.

**Champion baseline:** the R6 V-03 body (lifecycle-emphasis single-axis pass) — a three-phase
generator with a standalone pre-phase `## VARIATION MAP` section carrying a "Do not revise after
Phase 2 begins" instruction and a declaration that the AXIS-FREEZE PROTOCOL reads axis
assignments from this table (C-29). Phase 1 uses a flat header format: `criterion-target:`,
`direction:`, `mechanism:`, and `failure-condition:` appear as independent top-level fields —
no parent `hypothesis:` grouping. Phase 1 and Phase 2 have no `Declared responsibility:`
labeled key; responsibilities are communicated through phase titles and opening prose only
(C-23 pass, C-33 fail for Phase 1 and Phase 2). Phase 3 carries `Declared responsibility:` as
an explicit labeled key. Phase 2 includes the AXIS-FREEZE PROTOCOL with Steps 1, 2 (six named
per-axis freeze declarations), Step 2B (cross-artifact consistency check with named verdict
token `Consistency verdict: CONSISTENT | AXIS DIVERGENCE` — C-32 satisfied), and Step 3. The
VARIATION MAP table carries per-variation per-criterion directional predictions (C-24 satisfied)
but no failure-condition prediction columns (C-30 not satisfied). No `champion-baseline:` field
in variation body labels (inertia-framing not explicit at body level — C-08 partial, C-16
partial for per-axis denomination at body scope).

| Axis | Baseline Pole (Champion = R6 V-03) | R7 Committed Variation Pole |
|------|-----------------------------------|-----------------------------|
| output-format | Phase 1 and Phase 2 communicate responsibility through phase title and opening prose only — `Declared responsibility:` labeled key absent in Phase 1 and Phase 2 (C-33 fails for those phases); Phase 3 carries the labeled key; flat top-level hypothesis fields (no parent grouping, C-19 not structurally enforced) | V-01 single: add `Declared responsibility:` labeled key immediately after the phase title in Phase 1 and Phase 2 — all three phases now carry the key; key text names the specific structural responsibility for each phase; no other field, section, or protocol changes |
| phrasing-register | Flat imperative register for hypothesis in Phase 1 headers — `criterion-target:`, `direction:`, `mechanism:`, `failure-condition:` are independent top-level fields with no parent grouping; a generator can satisfy each field individually without treating them as a single structured hypothesis entry; C-19 not forced by schema | V-02 single: replace the four flat top-level hypothesis fields with a nested `hypothesis:` parent block carrying four labeled sub-fields — `criterion-target:`, `direction:`, `mechanism:`, `failure-condition:` — as required children; schema structure forces all four parts present and grouped within a single entry; C-19 compliance structurally detectable by presence of `hypothesis:` parent key with all four sub-fields non-blank |
| inertia-framing | No `champion-baseline:` field in variation body label format; the status-quo competitor (prior-round champion variation) is implicit from the VARIATION MAP baseline description in the pre-generation section only; not referenced at variation-body scope; C-08 partially satisfied (baseline inferable), C-16 partial (per-axis pole not cited at body level) | V-03 single: add `champion-baseline:` as a required field in the variation body label format, immediately after the Phase 1 header block and before the AXIS-FREEZE PROTOCOL; field names the prior-round champion variation by round and variation ID with the specific pole this variation changes from; makes the status-quo competitor explicit at variation-body scope |
| lifecycle-emphasis | In-loop Step 2B cross-artifact axis consistency check with named binary verdict token `Consistency verdict: [CONSISTENT | AXIS DIVERGENCE]` — fires after six-entry freeze list, before Step 3; divergence caught before body writing begins; C-31 and C-32 both satisfied | Not tested R7; held at R6 V-03 pole |
| role-sequence | Commitment phase (Phase 1) before generation phase (Phase 2) before findings phase (Phase 3); AXIS-FREEZE PROTOCOL fires at start of each body before writing; VARIATION MAP committed before Phase 1 | Not tested R7; held at baseline |
| scoring-granularity | VARIATION MAP carries per-variation per-criterion directional predictions (C-24); no failure-condition-outcome or failure-condition-implementation prediction columns (C-30 not satisfied) | Not tested R7; held at R6 V-03 pole |

This table is the isolation reference. Only the committed axis changes per variation body; all
other axes hold at their baseline pole.

---

## VARIATION MAP — Immutable after Phase 2 begins (C-27, C-29, C-30)

**[AUTHORITATIVE SOURCE] The AXIS-FREEZE PROTOCOL in Phase 2 reads axis assignments from this
table. Do not revise after Phase 2 begins.**

| V | Axis | Pass Type | Criterion Target | C-01 Direction | C-04 Direction | C-07 Direction | failure-condition-outcome prediction | failure-condition-implementation prediction |
|---|------|-----------|-----------------|----------------|----------------|----------------|--------------------------------------|----------------------------------------------|
| V-01 | output-format | single-axis | C-33 | no-change: adding labeled keys to phase headers does not alter section completeness requirements for variation bodies | no-change: phase-title labeling additions do not cross axis boundaries or tempt axis drift | no-change: phase responsibility labels do not alter hypothesis quality or falsifiability | C-33 pass rate does not improve beyond the R6 V-03 partial result (Phase 3 key only); `Declared responsibility:` labels in Phase 1 and Phase 2 add no structural detectability benefit over responsibility communicated through phase titles, and C-33 should be reconsidered as a C-23 extension in R8 | `Declared responsibility:` labels are added to Phase 1 and Phase 2 but at least one label text restates the phase title rather than naming a specific structural commitment distinct from the title, independently failing C-23 because the stated responsibility must add information beyond the phase title to constitute a genuine declaration |
| V-02 | phrasing-register | single-axis | C-19 | no-change: nested schema labeling does not change which sections must be present | risk-low: hypothesis schema forces mechanism naming, which could tempt an over-specific axis description that bleeds into a second axis | up: four-part nested schema forces all hypothesis components present and grouped in a single entry, directly improving C-07 falsifiability rates by requiring mechanism as a distinct labeled field | C-19 pass rate does not improve beyond zero (C-19 was not the primary target of any prior single-axis pass); schema adds no constraint benefit if generators produce all four parts naturally in flat prose, making C-19 a formatting artifact | Four-part schema parent `hypothesis:` block is present in the template but the `mechanism:` sub-field in generated variation bodies contains a restatement of the `direction:` value rather than a causal pathway, independently failing C-07 because mechanism must name the structural pathway from axis change to criterion outcome, not predict the outcome |
| V-03 | inertia-framing | single-axis | C-08, C-16 | no-change: champion-baseline citation does not change section completeness requirements | risk-medium: champion-baseline field names a prior-round variation body, which could tempt the generator to adopt content from that body rather than making a single axis change | no-change: explicit champion citation does not alter hypothesis quality | C-08 and C-16 pass rates do not improve beyond the R6 V-03 inferable-baseline result; explicit `champion-baseline:` field at variation-body scope adds no disambiguation benefit if the pre-generation per-axis pole table is already authoritative | `champion-baseline:` field is populated but the cited variation ID lacks a round qualifier (e.g., names "V-03" rather than "V-03 R6"), independently failing C-16 because the per-axis pole declaration must unambiguously identify the baseline variation — an unqualified label is ambiguous across rounds |
| V-04 | output-format x phrasing-register | combination (R7 Priority 1 — V-01 R7 `Declared responsibility` keys x V-02 R7 four-part hypothesis schema) | C-33, C-19 | up: same mechanism as V-01 | risk-medium: dual structural additions increase contamination surface; phase label additions and hypothesis schema additions are independent changes both affecting Phase 1 | up: compound — labeled phase responsibilities prime the generator to treat all phase fields structurally; four-part hypothesis schema enforces structure on the hypothesis fields specifically; both mechanisms reinforce structural completeness in Phase 1 | C-33 and C-19 pass rates do not jointly exceed V-01 R7 alone (C-33 single-axis baseline) and V-02 R7 alone (C-19 single-axis baseline); combination provides no compound benefit over independent single-axis results | `Declared responsibility:` key is present in Phase 1 and Phase 2, and four-part `hypothesis:` schema is present in Phase 1 headers, but the `hypothesis: mechanism:` sub-field text collapses the mechanism into an outcome restatement, independently failing C-07 even though the structural form is correct |
| V-05 | output-format x inertia-framing | combination (R7 Priority 2 — V-01 R7 `Declared responsibility` keys x V-03 R7 `champion-baseline` field) | C-33, C-08/C-16 | up: same mechanism as V-01 | risk-medium: champion-baseline field at body level is the primary contamination source | no-change: combination of phase labels and champion citation does not alter hypothesis quality | C-33 and C-08/C-16 pass rates do not jointly exceed V-01 R7 alone (C-33 single-axis baseline) and V-03 R7 alone (C-08/C-16 single-axis baseline); combination provides no compound benefit over independent single-axis results | `champion-baseline:` field is present in variation bodies and `Declared responsibility:` keys are present in all phases, but the `champion-baseline:` citation names "V-03" without a round qualifier, independently failing C-34 because the inertia-framing comparison denominator must be round-qualified to be unambiguous across experimental iterations |

---

## V-01 — Output Format: Declared Responsibility Key in All Phases

**axis:** output-format
**criterion-targeted:** C-33 — "In the phased prompt architecture (satisfying C-23), each phase
carries its declared responsibility as an explicitly labeled key." Mechanism: the R6 V-03
champion communicates Phase 1 responsibility through the title `PHASE 1 — COMMIT VARIATION
HEADERS` and Phase 2 responsibility through `PHASE 2 — GENERATE VARIATION BODIES` — both pass
C-23 (responsibility stated) but fail C-33 (no labeled key). Phase 3 carries the explicit key.
Adding the labeled key to Phase 1 and Phase 2 converts all three phases to C-33-compliant
declarations: a scorecard can confirm compliance by field presence without parsing phase prose.

**hypothesis:**
- **criterion-target:** C-33
- **direction:** increases C-33 pass rates; C-23 retention: no-change (responsibility already
  stated in all phases — the label adds structural detectability, not new content)
- **mechanism:** because adding `Declared responsibility:` immediately after the phase title in
  Phase 1 and Phase 2 converts responsibility communication from an implicit (title-derived) form
  to an explicit labeled form — a scorecard can check for the key without parsing the narrative
  or inferring responsibility from the title. The key also constrains the generator: to fill it,
  a non-trivial statement of the phase's specific structural commitment must be written, making
  implicit omissions visible as a blank required field.
- **failure-condition-outcome:** if C-33 pass rate does not exceed the R6 V-03 partial result
  (Phase 3 key only), the labeled keys in Phase 1 and Phase 2 add no detectability benefit over
  title-implied responsibility, and output-format should be pointed at a different structural
  element in R8.
- **failure-condition-implementation:** if the `Declared responsibility:` label text in Phase 1
  or Phase 2 restates the phase title in different words rather than naming a specific structural
  commitment (e.g., "Phase 1 responsibility: commit variation headers" duplicates the title
  without adding information), this independently fails C-23 because the stated responsibility
  must constitute a genuine declaration of what this phase does — not a label that is cosmetically
  present but semantically empty.

**baseline-delta:** `Declared responsibility:` labeled key added immediately after `PHASE 1 —
COMMIT VARIATION HEADERS` and immediately after `PHASE 2 — GENERATE VARIATION BODIES`. Phase 3
key is unchanged. No other field, section, instruction, or protocol changes.

**completeness-risk:** Phase 2 `Declared responsibility:` key — generators may write a label
that restates "generate variation bodies" (the title) rather than specifying the AXIS-FREEZE
PROTOCOL as the structural commitment mechanism.

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

## VARIATION MAP — Immutable after Phase 2 begins

Before Phase 1 begins, commit the axis assignment and per-variation per-criterion directional
predictions for each of the {N} planned variations. Fill every row and every direction cell.
A direction cell without both a verdict and a mechanism sentence is not complete.

| V | Assigned Axis | Criterion Target | C-01 Direction | C-04 Direction | C-07 Direction | Notes |
|---|--------------|-----------------|----------------|----------------|----------------|-------|
[Fill all {N} rows. Each direction cell: verdict (up / down / no-change) + one sentence
mechanism stating why that criterion moves in that direction for this specific axis change.
Do not proceed to Phase 1 until all rows are filled.]

**Do not revise this table after Phase 2 begins.
The AXIS-FREEZE PROTOCOL in Phase 2 reads axis assignments from this table.**

PHASE 1 — COMMIT VARIATION HEADERS
Declared responsibility: lock axis assignments by writing a complete variation header for each
planned variation — every field populated, no field blank, axis value must exactly match the
VARIATION MAP assignment for that row.

Before writing any variation body, commit a full variation header for each of the {N} axes
assigned in the VARIATION MAP. Every field required. No field may be blank.

Header format:

```
variation: V-NN
axis: [axis name — must match VARIATION MAP assigned axis for this V]
pole: [one phrase — the specific change this variation makes on this axis]
baseline-delta: [one sentence — the single structural element that changes, nothing else]
completeness-risk: [the section most at risk of omission in this specific body]
criterion-target: [C-NN by ID]
direction: [increases / decreases / stabilizes] [criterion name] pass rates
mechanism: [structural pathway from axis change to criterion outcome — name the mechanism,
            not the outcome]
failure-condition: [if criterion pass rate does not exceed [V-NN RN result], the mechanism
                   is refuted. Name the prior-round comparison baseline with round qualifier.]
score-prediction:
  C-01: [pass / partial / fail] — [one sentence mechanism]
  C-04: [pass / partial / fail] — [name the contamination risk for this axis]
  C-07: [pass / partial / fail] — [name the structural element producing hypothesis quality]
  C-09: [pass / partial / fail] — [one sentence mechanism]
```

Review all {N} headers. Verify every axis matches the VARIATION MAP. Commit. Do not revise
axis assignments after Phase 2 begins.

PHASE 2 — GENERATE VARIATION BODIES
Declared responsibility: write each committed variation body in full under the AXIS-FREEZE
PROTOCOL — the committed axis is the only element that changes from the baseline; every section
written out; no placeholders; no cross-references to other variations.

For each committed header, write the complete variation body. The AXIS-FREEZE PROTOCOL reads
the committed axis from the VARIATION MAP — the authoritative source.

AXIS-FREEZE PROTOCOL (fires once per body, before writing begins):

  Step 1 — Read: state the axis name assigned in the VARIATION MAP for this body (V-NN:
  [axis name]). [read from VARIATION MAP]

  Step 2 — Write one freeze declaration for every axis in the canonical list:
    - role-sequence:       [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - output-format:       [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - lifecycle-emphasis:  [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - phrasing-register:   [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - inertia-framing:     [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - scoring-granularity: [FROZEN | COMMITTED — read from VARIATION MAP for this body]

  All six canonical axes must appear. Exactly one marked COMMITTED. Five marked FROZEN.
  A freeze list with fewer than six entries is incomplete — do not proceed until all six
  entries are present.

  Step 2B — Cross-artifact axis consistency check (fires before Step 3):
    - VARIATION MAP assigned axis for this V-NN: [state the axis from the VARIATION MAP row]
      [read from VARIATION MAP]
    - Phase 1 header declared axis for this V-NN: [state the axis from the Phase 1 header]
    - Consistency verdict: [CONSISTENT | AXIS DIVERGENCE]
    - If AXIS DIVERGENCE: state which artifact carries the incorrect axis assignment and halt.
      Do not proceed to Step 3 until the divergence is resolved and the verdict reads CONSISTENT.

  Step 3 — Write the body: change only the COMMITTED axis. Write the full body — every
  section, every instruction. No diffs. No cross-references to other variations.
  Every structural section present.

Label format:

### V-NN — [Axis: Pole Description]

[variation header from Phase 1 — do not revise]

AXIS-FREEZE PROTOCOL:
[Step 1: VARIATION MAP axis declaration for this V]
[Step 2: six-entry freeze list — all six canonical axes filled, each labeled "read from VARIATION MAP"]
[Step 2B: VARIATION MAP axis, Phase 1 header axis, Consistency verdict: CONSISTENT / AXIS DIVERGENCE]
[Step 3: "Proceeding to write COMMITTED axis change only."]

[COMPLETE SKILL BODY — all sections, all instructions, fully written]

Do not begin the next variation until the current body is complete, the AXIS-FREEZE PROTOCOL
shows all six canonical axis entries, and Step 2B shows CONSISTENT.

PHASE 3 — FINDINGS
Declared responsibility: confirm in-loop axis consistency (post-generation audit), calibrate
VARIATION MAP predictions against actual body structures, identify combination candidates, rank
evaluation order, designate anchor.

1. Axis alignment confirmation (post-generation audit — all in-loop Step 2B checks should
   have already caught any divergence; this table is a post-generation confirmation only):

| V | Axis (VARIATION MAP) | Axis (Phase 1 header) | Step 2B In-Loop Result | Post-Generation Match? |
|---|---------------------|----------------------|------------------------|------------------------|

Flag any post-generation mismatch as ESCAPED DIVERGENCE — a protocol failure.

2. Prediction calibration:

| V | Axis | C-07 Predicted (MAP) | C-07 Structure Present in Body | Prediction Correct? | Mis-prediction Mechanism |
|---|------|----------------------|-------------------------------|---------------------|--------------------------|

For each wrong prediction, state in one sentence why the structural element did not behave
as the mechanism predicted.

3. Combination candidates (compound-effects model):

| Priority | Axis Pair | V-NN Basis | Failure Modes Per Axis | Residual Weakness After First Axis Only | Compound Criterion Effect (Both Active) | Criteria Targeted |
|----------|-----------|------------|------------------------|-----------------------------------------|-----------------------------------------|-------------------|

Column rules: Failure Modes cites criterion ID per axis. Residual Weakness is a concrete gap,
not a restatement. Compound Criterion Effect names a criterion ID distinct from what either
axis achieves alone. A row with any blank column is omitted.

Priority rationale: one sentence per HIGH or MEDIUM row.

4. Evaluation order:

| Priority | V | Axis | Cost | Independence | Cross-Round Dependency | Sequencing Rationale |
|----------|----|------|------|--------------|------------------------|----------------------|

Cross-round dependency format: "R[round] / V-NN / [metric name]" or "none."

5. Anchor: one variation. Justify structural impact, isolation quality, detectable failure
   condition — one sentence each.

---

## V-02 — Phrasing Register: Four-Part Nested Hypothesis Schema

**axis:** phrasing-register
**criterion-targeted:** C-19 — "At least one variation's hypothesis field is composed of all
four named parts: (1) criterion-target (C-NN by ID), (2) directional prediction, (3) causal
mechanism (because...), and (4) explicit failure condition (if...). C-19 requires all four parts
to be present and structurally labeled within a single hypothesis entry." Mechanism: the R6 V-03
champion uses flat top-level fields (`criterion-target:`, `direction:`, `mechanism:`,
`failure-condition:` each as independent keys). A generator can populate each field in isolation
without recognizing that together they constitute a structured four-part hypothesis entry — C-19
compliance requires reading all four fields and verifying they form a coherent unit. Adding a
parent `hypothesis:` block with the four parts as labeled required sub-fields makes C-19
compliance structurally detectable by schema presence: the generator must fill the parent block,
and the block heading signals that these four elements are a single logical unit.

**hypothesis:**
- **criterion-target:** C-19
- **direction:** increases C-19 pass rates; increases C-07 falsifiability rates (mechanism
  sub-field requirement forces a causal statement, not an outcome statement)
- **mechanism:** because grouping `criterion-target:`, `direction:`, `mechanism:`, and
  `failure-condition:` under a parent `hypothesis:` key converts C-19 compliance from a content
  judgment (are all four parts present and coherent across four independent fields?) to a schema
  check (is the `hypothesis:` parent key present with all four sub-fields non-blank?). The
  register shift — from imperative top-level instruction to structured nested schema — also
  constrains the generator: the `mechanism:` sub-field label explicitly names what it requires
  (a causal pathway), reducing conflation with the `direction:` field.
- **failure-condition:** if C-19 pass rate does not exceed zero (C-19 was not the primary
  target of any R6 or earlier single-axis pass), the nested schema adds no constraint benefit
  over flat top-level fields, and phrasing-register should be redirected to C-07 mechanism
  quality without the four-part grouping in R8.
- **failure-condition-implementation:** if the `mechanism:` sub-field in generated variation
  bodies contains a restatement of the `direction:` value — naming the predicted outcome rather
  than the causal pathway — the schema is formally present but semantically empty, independently
  failing C-07 because mechanism must name the structural pathway from axis change to criterion
  outcome, not the outcome itself.

**baseline-delta:** Phase 1 header format: the four flat top-level fields `criterion-target:`,
`direction:`, `mechanism:`, `failure-condition:` are replaced by a single parent `hypothesis:`
block with those four as required labeled sub-fields. No other field in the header changes.
No other section, instruction, or protocol changes.

**completeness-risk:** `hypothesis: mechanism:` sub-field — generators tend to write the
predicted outcome ("increases C-19 pass rates") rather than the structural causal pathway
("because the parent block schema requires all four sub-fields non-blank...").

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

## VARIATION MAP — Immutable after Phase 2 begins

Before Phase 1 begins, commit the axis assignment and per-variation per-criterion directional
predictions for each of the {N} planned variations. Fill every row and every direction cell.
A direction cell without both a verdict and a mechanism sentence is not complete.

| V | Assigned Axis | Criterion Target | C-01 Direction | C-04 Direction | C-07 Direction | Notes |
|---|--------------|-----------------|----------------|----------------|----------------|-------|
[Fill all {N} rows. Each direction cell: verdict (up / down / no-change) + one sentence
mechanism. Do not proceed to Phase 1 until all rows are filled.]

**Do not revise this table after Phase 2 begins.
The AXIS-FREEZE PROTOCOL in Phase 2 reads axis assignments from this table.**

PHASE 1 — COMMIT VARIATION HEADERS

Before writing any variation body, commit a full variation header for each of the {N} axes
assigned in the VARIATION MAP. Every field required. No field may be blank.

Header format:

```
variation: V-NN
axis: [axis name — must match VARIATION MAP assigned axis for this V]
pole: [one phrase — the specific change this variation makes on this axis]
baseline-delta: [one sentence — the single structural element that changes, nothing else]
completeness-risk: [the section most at risk of omission in this specific body]
hypothesis:
  criterion-target: [C-NN by ID]
  direction: [increases / decreases / stabilizes] [criterion name] pass rates
  mechanism: [one sentence — the structural pathway from axis change to criterion outcome;
              begin "because..." and name the mechanism, not the predicted outcome]
  failure-condition: [if criterion pass rate does not exceed [V-NN RN result], the mechanism
                     is refuted. Name the prior-round baseline with round qualifier.]
score-prediction:
  C-01: [pass / partial / fail] — [one sentence mechanism]
  C-04: [pass / partial / fail] — [name the contamination risk for this axis]
  C-07: [pass / partial / fail] — [name the structural element producing hypothesis quality]
  C-09: [pass / partial / fail] — [one sentence mechanism]
```

The `hypothesis:` block must contain all four sub-fields, each non-blank. A header with any
sub-field blank is incomplete — revise before advancing to Phase 2. The `mechanism:` sub-field
must begin "because..." and name a structural pathway — a restatement of `direction:` does not
qualify.

Review all {N} headers. Verify every axis matches the VARIATION MAP. Every `hypothesis:` block
has all four sub-fields non-blank and `mechanism:` starts with "because...". Commit. Do not
revise axis assignments after Phase 2 begins.

PHASE 2 — GENERATE VARIATION BODIES

For each committed header, write the complete variation body. The AXIS-FREEZE PROTOCOL reads
the committed axis from the VARIATION MAP — the authoritative source.

AXIS-FREEZE PROTOCOL (fires once per body, before writing begins):

  Step 1 — Read: state the axis name assigned in the VARIATION MAP for this body (V-NN:
  [axis name]). [read from VARIATION MAP]

  Step 2 — Write one freeze declaration for every axis in the canonical list:
    - role-sequence:       [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - output-format:       [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - lifecycle-emphasis:  [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - phrasing-register:   [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - inertia-framing:     [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - scoring-granularity: [FROZEN | COMMITTED — read from VARIATION MAP for this body]

  All six canonical axes must appear. Exactly one marked COMMITTED. Five marked FROZEN.
  A freeze list with fewer than six entries is incomplete — do not proceed until all six
  entries are present.

  Step 2B — Cross-artifact axis consistency check (fires before Step 3):
    - VARIATION MAP assigned axis for this V-NN: [state the axis from the VARIATION MAP row]
      [read from VARIATION MAP]
    - Phase 1 header declared axis for this V-NN: [state the axis from the Phase 1 header]
    - Consistency verdict: [CONSISTENT | AXIS DIVERGENCE]
    - If AXIS DIVERGENCE: state which artifact carries the incorrect axis assignment and halt.
      Do not proceed to Step 3 until the divergence is resolved and the verdict reads CONSISTENT.

  Step 3 — Write the body: change only the COMMITTED axis. Write the full body — every
  section, every instruction. No diffs. No cross-references to other variations.
  Every structural section present.

Label format:

### V-NN — [Axis: Pole Description]

[variation header from Phase 1 — do not revise]

AXIS-FREEZE PROTOCOL:
[Step 1: VARIATION MAP axis declaration for this V]
[Step 2: six-entry freeze list — all six canonical axes filled, each labeled "read from VARIATION MAP"]
[Step 2B: VARIATION MAP axis, Phase 1 header axis, Consistency verdict: CONSISTENT / AXIS DIVERGENCE]
[Step 3: "Proceeding to write COMMITTED axis change only."]

[COMPLETE SKILL BODY — all sections, all instructions, fully written]

Do not begin the next variation until the current body is complete, the AXIS-FREEZE PROTOCOL
shows all six canonical axis entries, and Step 2B shows CONSISTENT.

PHASE 3 — FINDINGS
Declared responsibility: confirm in-loop axis consistency (post-generation audit), hypothesis
schema compliance audit, identify combination candidates, rank evaluation order, designate anchor.

1. Axis alignment confirmation (post-generation audit):

| V | Axis (VARIATION MAP) | Axis (Phase 1 header) | Step 2B In-Loop Result | Post-Generation Match? |
|---|---------------------|----------------------|------------------------|------------------------|

Flag any post-generation mismatch as ESCAPED DIVERGENCE — a protocol failure.

2. Hypothesis schema audit:

| V | `hypothesis:` parent key present? | All 4 sub-fields non-blank? | `mechanism:` starts "because..."? | C-19 compliant? |
|---|-----------------------------------|-----------------------------|------------------------------------|-----------------|

A row with "No" in column 4 fails C-19. A row with "No" in column 3 fails C-07 regardless
of schema presence.

3. Combination candidates (compound-effects model):

| Priority | Axis Pair | V-NN Basis | Failure Modes Per Axis | Residual Weakness After First Axis Only | Compound Criterion Effect (Both Active) | Criteria Targeted |
|----------|-----------|------------|------------------------|-----------------------------------------|-----------------------------------------|-------------------|

Column rules: Failure Modes cites criterion ID per axis. Residual Weakness is a concrete gap.
Compound Criterion Effect names a criterion ID distinct from what either axis achieves alone.
A row with any blank column is omitted. Priority rationale: one sentence per HIGH or MEDIUM row.

4. Evaluation order:

| Priority | V | Axis | Cost | Independence | Cross-Round Dependency | Sequencing Rationale |
|----------|----|------|------|--------------|------------------------|----------------------|

Cross-round dependency format: "R[round] / V-NN / [metric name]" or "none."

5. Anchor: one variation. Justify structural impact, isolation quality, detectable failure
   condition — one sentence each.

---

## V-03 — Inertia Framing: Champion-Baseline Field at Variation-Body Scope

**axis:** inertia-framing
**criterion-targeted:** C-08 (baseline explicit), C-16 (per-axis pole declaration) — the R6
V-03 champion satisfies C-08 and C-16 at pre-generation scope (the per-axis pole table names
the champion baseline per axis before any body is written). At variation-body scope, the prior-
round champion is not named — a reviewer reading a single variation body cannot identify the
specific prior-round variation it competes with without consulting the pre-generation section.
Adding a `champion-baseline:` field at the top of each variation body makes the status-quo
competitor explicit at body scope: the field names the prior-round champion by round and
variation ID and states the specific pole being changed, so any single body is self-contained
with respect to its competitive reference.

**hypothesis:**
- **criterion-target:** C-08, C-16
- **direction:** increases C-08 and C-16 pass rates at variation-body scope; reduces reviewer
  burden when examining individual variation bodies in isolation
- **mechanism:** because a `champion-baseline:` field at the top of each variation body names
  the prior-round champion variation by round-qualified ID and describes the specific pole being
  changed — converting the baseline from "inferable from the pre-generation section" (C-08
  partial) to "explicitly declared at body scope" (C-08 full); and from "declared per-axis at
  document scope only" (C-16 partial) to "declared at the variation body scope where the change
  is made" (C-16 stronger — the pole being changed is cited where the change occurs).
- **failure-condition:** if C-08 and C-16 pass rates do not improve beyond the R6 V-03
  inferable-baseline result, the `champion-baseline:` field at body scope adds no disambiguation
  benefit over the pre-generation per-axis pole table, and inertia-framing should be pointed at
  a different structural scope in R8.
- **failure-condition-implementation:** if the `champion-baseline:` field is populated but the
  cited variation ID lacks a round qualifier (e.g., "V-03" rather than "V-03 R6"), the field
  independently fails C-16 because the per-axis pole declaration must unambiguously identify the
  baseline variation — an unqualified label is ambiguous across rounds where variation labels
  repeat, defeating the purpose of explicit champion citation.

**baseline-delta:** the variation body Label format gains one required field — `champion-baseline:`
— immediately after the Phase 1 header block and before the AXIS-FREEZE PROTOCOL. Format:
`[V-NN RN: one sentence describing the specific pole this variation changes from]`. Round
qualifier required. No other field, section, instruction, or protocol changes.

**completeness-risk:** `champion-baseline:` round qualifier — generators tend to write the
variation ID without the round tag (e.g., "V-03" vs "V-03 R6"), making the citation ambiguous.

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

## VARIATION MAP — Immutable after Phase 2 begins

Before Phase 1 begins, commit the axis assignment and per-variation per-criterion directional
predictions for each of the {N} planned variations. Fill every row and every direction cell.
A direction cell without both a verdict and a mechanism sentence is not complete.

| V | Assigned Axis | Criterion Target | C-01 Direction | C-04 Direction | C-07 Direction | Notes |
|---|--------------|-----------------|----------------|----------------|----------------|-------|
[Fill all {N} rows. Each direction cell: verdict (up / down / no-change) + one sentence
mechanism. Do not proceed to Phase 1 until all rows are filled.]

**Do not revise this table after Phase 2 begins.
The AXIS-FREEZE PROTOCOL in Phase 2 reads axis assignments from this table.**

PHASE 1 — COMMIT VARIATION HEADERS

Before writing any variation body, commit a full variation header for each of the {N} axes
assigned in the VARIATION MAP. Every field required. No field may be blank.

Header format:

```
variation: V-NN
axis: [axis name — must match VARIATION MAP assigned axis for this V]
pole: [one phrase — the specific change this variation makes on this axis]
baseline-delta: [one sentence — the single structural element that changes, nothing else]
completeness-risk: [the section most at risk of omission in this specific body]
criterion-target: [C-NN by ID]
direction: [increases / decreases / stabilizes] [criterion name] pass rates
mechanism: [structural pathway from axis change to criterion outcome — name the mechanism,
            not the outcome]
failure-condition: [if criterion pass rate does not exceed [V-NN RN result], the mechanism
                   is refuted. Name the prior-round comparison baseline with round qualifier.]
score-prediction:
  C-01: [pass / partial / fail] — [one sentence mechanism]
  C-04: [pass / partial / fail] — [name the contamination risk for this axis]
  C-07: [pass / partial / fail] — [name the structural element producing hypothesis quality]
  C-09: [pass / partial / fail] — [one sentence mechanism]
```

Review all {N} headers. Verify every axis matches the VARIATION MAP. Commit. Do not revise
axis assignments after Phase 2 begins.

PHASE 2 — GENERATE VARIATION BODIES

For each committed header, write the complete variation body. The AXIS-FREEZE PROTOCOL reads
the committed axis from the VARIATION MAP — the authoritative source.

AXIS-FREEZE PROTOCOL (fires once per body, before writing begins):

  Step 1 — Read: state the axis name assigned in the VARIATION MAP for this body (V-NN:
  [axis name]). [read from VARIATION MAP]

  Step 2 — Write one freeze declaration for every axis in the canonical list:
    - role-sequence:       [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - output-format:       [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - lifecycle-emphasis:  [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - phrasing-register:   [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - inertia-framing:     [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - scoring-granularity: [FROZEN | COMMITTED — read from VARIATION MAP for this body]

  All six canonical axes must appear. Exactly one marked COMMITTED. Five marked FROZEN.
  A freeze list with fewer than six entries is incomplete — do not proceed until all six
  entries are present.

  Step 2B — Cross-artifact axis consistency check (fires before Step 3):
    - VARIATION MAP assigned axis for this V-NN: [state the axis from the VARIATION MAP row]
      [read from VARIATION MAP]
    - Phase 1 header declared axis for this V-NN: [state the axis from the Phase 1 header]
    - Consistency verdict: [CONSISTENT | AXIS DIVERGENCE]
    - If AXIS DIVERGENCE: state which artifact carries the incorrect axis assignment and halt.
      Do not proceed to Step 3 until the divergence is resolved and the verdict reads CONSISTENT.

  Step 3 — Write the body: change only the COMMITTED axis. Write the full body — every
  section, every instruction. No diffs. No cross-references to other variations.
  Every structural section present.

Label format:

### V-NN — [Axis: Pole Description]

[variation header from Phase 1 — do not revise]

champion-baseline: [V-NN RN — one sentence: the prior-round champion variation and the specific
                   pole this variation changes from. Name the champion by round and variation ID.
                   Format: "V-NN RN: the [axis] baseline pole was [description]; this variation
                   changes [specific element] to [new value]." Round qualifier required — citing
                   "V-NN" without the round tag is a completeness failure.]

AXIS-FREEZE PROTOCOL:
[Step 1: VARIATION MAP axis declaration for this V]
[Step 2: six-entry freeze list — all six canonical axes filled, each labeled "read from VARIATION MAP"]
[Step 2B: VARIATION MAP axis, Phase 1 header axis, Consistency verdict: CONSISTENT / AXIS DIVERGENCE]
[Step 3: "Proceeding to write COMMITTED axis change only."]

[COMPLETE SKILL BODY — all sections, all instructions, fully written]

Do not begin the next variation until the current body is complete, the AXIS-FREEZE PROTOCOL
shows all six canonical axis entries, and Step 2B shows CONSISTENT.

PHASE 3 — FINDINGS
Declared responsibility: confirm in-loop axis consistency (post-generation audit), champion-
baseline citation audit, identify combination candidates, rank evaluation order, designate anchor.

1. Axis alignment confirmation (post-generation audit):

| V | Axis (VARIATION MAP) | Axis (Phase 1 header) | Step 2B In-Loop Result | Post-Generation Match? |
|---|---------------------|----------------------|------------------------|------------------------|

Flag any post-generation mismatch as ESCAPED DIVERGENCE — a protocol failure.

2. Champion-baseline audit:

| V | champion-baseline field present? | Round qualifier present in citation? | Pole description matches VARIATION MAP baseline pole? |
|---|----------------------------------|--------------------------------------|-------------------------------------------------------|

A row with "No" in column 2 is a completeness failure. A row with "No" in column 3 independently
fails C-16 (ambiguous denominator). A row with "No" in column 4 indicates inertia-framing
contamination.

3. Combination candidates (compound-effects model):

| Priority | Axis Pair | V-NN Basis | Failure Modes Per Axis | Residual Weakness After First Axis Only | Compound Criterion Effect (Both Active) | Criteria Targeted |
|----------|-----------|------------|------------------------|-----------------------------------------|-----------------------------------------|-------------------|

Column rules: Failure Modes cites criterion ID per axis. Residual Weakness is a concrete gap.
Compound Criterion Effect names a criterion ID distinct from what either axis achieves alone.
A row with any blank column is omitted. Priority rationale: one sentence per HIGH or MEDIUM row.

4. Evaluation order:

| Priority | V | Axis | Cost | Independence | Cross-Round Dependency | Sequencing Rationale |
|----------|----|------|------|--------------|------------------------|----------------------|

Cross-round dependency format: "R[round] / V-NN / [metric name]" or "none."

5. Anchor: one variation. Justify structural impact, isolation quality, detectable failure
   condition — one sentence each.

---

## V-04 — Combination: Output Format x Phrasing Register

**axis:** output-format x phrasing-register
**pass-type:** combination (R7 Priority 1 — V-01 R7 `Declared responsibility` keys in all
phases x V-02 R7 four-part nested `hypothesis:` schema in Phase 1 headers)
*C-04 exception explicitly invoked.*

**hypothesis:** Combining `Declared responsibility:` labeled keys in all phases (V-01 R7,
output-format axis: Phase 1 and Phase 2 carry the key in addition to Phase 3) with a four-part
nested `hypothesis:` schema in Phase 1 headers (V-02 R7, phrasing-register axis: four sub-fields
grouped under a parent `hypothesis:` key) increases C-33 and C-19 jointly beyond what either
axis achieves alone:
- **criterion-target:** C-33 (primary), C-19 (secondary)
- **direction:** increases C-33 and C-19 pass rates beyond what either axis achieves alone
- **mechanism:** V-01 R7 alone satisfies C-33 (all three phases carry `Declared responsibility:`
  as a labeled key) but Phase 1 header hypothesis fields remain flat — C-19 compliance still
  requires a post-hoc content judgment on four independent top-level fields. V-02 R7 alone
  satisfies C-19 (four-part schema present in Phase 1 headers) but Phase 1 and Phase 2 still
  communicate their responsibilities through titles only — C-33 not satisfied. The combination
  produces a scaffold where every phase declares its structural commitment via a labeled key
  (output-format axis) AND Phase 1 headers enforce the four-part hypothesis as a single grouped
  schema (phrasing-register axis) — the only R7 configuration where both C-33 structural
  detectability and C-19 schema completeness are simultaneously active at Phase 1 scope.
- **failure-condition-outcome:** if C-33 and C-19 pass rates do not jointly exceed V-01 R7 alone
  (C-33 single-axis baseline) and V-02 R7 alone (C-19 single-axis baseline), the combination
  provides no compound benefit and these axes should remain as independent single-axis variations
  in R8 rather than being promoted as a compound configuration.
- **failure-condition-implementation:** if `Declared responsibility:` keys are present in all
  phases and the four-part `hypothesis:` schema is present in Phase 1 headers, but the
  `hypothesis: mechanism:` sub-field text collapses the mechanism into an outcome restatement,
  the combination independently fails C-07 — the schema structure is present (C-19 formal
  compliance) but the mechanism content is absent (C-07 fail), demonstrating that schema
  presence does not guarantee mechanism quality.

---

**Combination pass: output-format x phrasing-register**
*C-04 exception explicitly invoked. `Declared responsibility:` keys in Phase 1 and Phase 2
(output-format axis) and four-part nested `hypothesis:` schema in Phase 1 headers (phrasing-
register axis) are both active. The generated variations are still single-axis — each changes
one axis from the baseline skill. The combination applies to the generation scaffolding
structure, not to the individual variations themselves.*

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

## VARIATION MAP — Immutable after Phase 2 begins

Before Phase 1 begins, commit the axis assignment and per-variation per-criterion directional
predictions for each of the {N} planned variations. Fill every row and every direction cell.
A direction cell without both a verdict and a mechanism sentence is not complete.

| V | Assigned Axis | Criterion Target | C-01 Direction | C-04 Direction | C-07 Direction | Notes |
|---|--------------|-----------------|----------------|----------------|----------------|-------|
[Fill all {N} rows. Each direction cell: verdict (up / down / no-change) + one sentence
mechanism. Do not proceed to Phase 1 until all rows are filled.]

**Do not revise this table after Phase 2 begins.
The AXIS-FREEZE PROTOCOL in Phase 2 reads axis assignments from this table.**

PHASE 1 — COMMIT VARIATION HEADERS
Declared responsibility: lock axis assignments by writing a complete variation header for each
planned variation — every field populated, no field blank, `hypothesis:` block present with all
four sub-fields non-blank, axis value matching the VARIATION MAP assignment exactly.

Before writing any variation body, commit a full variation header for each of the {N} axes
assigned in the VARIATION MAP. Every field required. No field may be blank.

Header format:

```
variation: V-NN
axis: [axis name — must match VARIATION MAP assigned axis for this V]
pole: [one phrase — the specific change this variation makes on this axis]
baseline-delta: [one sentence — the single structural element that changes, nothing else]
completeness-risk: [the section most at risk of omission in this specific body]
hypothesis:
  criterion-target: [C-NN by ID]
  direction: [increases / decreases / stabilizes] [criterion name] pass rates
  mechanism: [one sentence — the structural pathway from axis change to criterion outcome;
              begin "because..." and name the mechanism, not the predicted outcome]
  failure-condition: [if criterion pass rate does not exceed [V-NN RN result], the mechanism
                     is refuted. Name the prior-round baseline with round qualifier.]
score-prediction:
  C-01: [pass / partial / fail] — [one sentence mechanism]
  C-04: [pass / partial / fail] — [name the contamination risk for this axis]
  C-07: [pass / partial / fail] — [name the structural element producing hypothesis quality]
  C-09: [pass / partial / fail] — [one sentence mechanism]
```

The `hypothesis:` block must contain all four sub-fields, each non-blank. The `mechanism:`
sub-field must begin "because..." and name a structural pathway — a restatement of `direction:`
does not qualify. A header with a blank sub-field or a mechanism that names an outcome rather
than a pathway is incomplete — revise before advancing to Phase 2.

Review all {N} headers. Verify every axis matches the VARIATION MAP. Every `hypothesis:` block
has all four sub-fields non-blank and `mechanism:` starts with "because...". Commit. Do not
revise axis assignments after Phase 2 begins.

PHASE 2 — GENERATE VARIATION BODIES
Declared responsibility: write each committed variation body in full under the AXIS-FREEZE
PROTOCOL — the committed axis is the only element that changes from the baseline; every section
written out; no placeholders; no cross-references to other variations.

For each committed header, write the complete variation body. The AXIS-FREEZE PROTOCOL reads
the committed axis from the VARIATION MAP — the authoritative source.

AXIS-FREEZE PROTOCOL (fires once per body, before writing begins):

  Step 1 — Read: state the axis name assigned in the VARIATION MAP for this body (V-NN:
  [axis name]). [read from VARIATION MAP]

  Step 2 — Write one freeze declaration for every axis in the canonical list:
    - role-sequence:       [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - output-format:       [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - lifecycle-emphasis:  [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - phrasing-register:   [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - inertia-framing:     [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - scoring-granularity: [FROZEN | COMMITTED — read from VARIATION MAP for this body]

  All six canonical axes must appear. Exactly one marked COMMITTED. Five marked FROZEN.
  A freeze list with fewer than six entries is incomplete — do not proceed until all six
  entries are present.

  Step 2B — Cross-artifact axis consistency check (fires before Step 3):
    - VARIATION MAP assigned axis for this V-NN: [state the axis from the VARIATION MAP row]
      [read from VARIATION MAP]
    - Phase 1 header declared axis for this V-NN: [state the axis from the Phase 1 header]
    - Consistency verdict: [CONSISTENT | AXIS DIVERGENCE]
    - If AXIS DIVERGENCE: state which artifact carries the incorrect axis assignment and halt.
      Do not proceed to Step 3 until the divergence is resolved and the verdict reads CONSISTENT.

  Step 3 — Write the body: change only the COMMITTED axis. Write the full body — every
  section, every instruction. No diffs. No cross-references to other variations.
  Every structural section present.

Label format:

### V-NN — [Axis: Pole Description]

[variation header from Phase 1 — do not revise]

AXIS-FREEZE PROTOCOL:
[Step 1: VARIATION MAP axis declaration for this V]
[Step 2: six-entry freeze list — all six canonical axes filled, each labeled "read from VARIATION MAP"]
[Step 2B: VARIATION MAP axis, Phase 1 header axis, Consistency verdict: CONSISTENT / AXIS DIVERGENCE]
[Step 3: "Proceeding to write COMMITTED axis change only."]

[COMPLETE SKILL BODY — all sections, all instructions, fully written]

Do not begin the next variation until the current body is complete, the AXIS-FREEZE PROTOCOL
shows all six canonical axis entries, and Step 2B shows CONSISTENT.

PHASE 3 — FINDINGS
Declared responsibility: post-generation axis consistency audit, hypothesis schema compliance
audit, combination candidates, evaluation order, anchor designation.

1. Axis alignment confirmation (post-generation audit):

| V | Axis (VARIATION MAP) | Axis (Phase 1 header) | Step 2B In-Loop Result | Post-Generation Match? |
|---|---------------------|----------------------|------------------------|------------------------|

Flag any ESCAPED DIVERGENCE as a protocol failure.

2. Hypothesis schema audit:

| V | `hypothesis:` block present? | All 4 sub-fields non-blank? | `mechanism:` starts "because..."? | Mechanism names pathway (not outcome)? | C-19 compliant? |
|---|------------------------------|-----------------------------|------------------------------------|----------------------------------------|-----------------|

A row with "No" in column 5 fails C-19. A row with "No" in column 4 fails C-07.

3. Combination candidates (compound-effects model):

| Priority | Axis Pair | V-NN Basis | Failure Modes Per Axis | Residual Weakness After First Axis Only | Compound Criterion Effect (Both Active) | Criteria Targeted |
|----------|-----------|------------|------------------------|-----------------------------------------|-----------------------------------------|-------------------|

Column rules: Failure Modes cites criterion ID per axis. Residual Weakness is a concrete gap.
Compound Criterion Effect names a criterion ID distinct from what either axis achieves alone.
A row with any blank column is omitted. Priority rationale: one sentence per HIGH or MEDIUM row.

4. Evaluation order:

| Priority | V | Axis | Cost | Independence | Cross-Round Dependency | Sequencing Rationale |
|----------|----|------|------|--------------|------------------------|----------------------|

Cross-round dependency format: "R[round] / V-NN / [metric name]" or "none."

5. Anchor: one variation. Justify structural impact, isolation quality, detectable failure
   condition — one sentence each.

---

## V-05 — Combination: Output Format x Inertia Framing

**axis:** output-format x inertia-framing
**pass-type:** combination (R7 Priority 2 — V-01 R7 `Declared responsibility` keys in all
phases x V-03 R7 `champion-baseline:` field at variation-body scope)
*C-04 exception explicitly invoked.*

**hypothesis:** Combining `Declared responsibility:` labeled keys in all phases (V-01 R7,
output-format axis) with `champion-baseline:` field at variation-body scope (V-03 R7, inertia-
framing axis) increases C-33 and C-08/C-16 jointly beyond what either axis achieves alone:
- **criterion-target:** C-33 (primary), C-08 and C-16 (secondary)
- **direction:** increases C-33, C-08, and C-16 pass rates beyond what either axis achieves alone
- **mechanism:** V-01 R7 alone satisfies C-33 (all phases carry `Declared responsibility:` key)
  but has no `champion-baseline:` field at variation-body scope — the status-quo competitor is
  implicit at body level, requiring the reviewer to consult the pre-generation section. V-03 R7
  alone adds `champion-baseline:` at body scope (C-08/C-16 stronger) but Phase 1 and Phase 2
  still communicate responsibilities through titles only (C-33 not satisfied). The combination
  produces a scaffold where phase responsibilities are structurally declared (C-33) AND the
  status-quo competitor is explicitly named at the variation-body scope where the change is made
  (C-08/C-16 at body scope) — the only R7 configuration where both structural declarations
  (phase-level and body-level) are simultaneously active.
- **failure-condition-outcome:** if C-33 and C-08/C-16 pass rates do not jointly exceed V-01 R7
  alone (C-33 single-axis baseline) and V-03 R7 alone (C-08/C-16 single-axis baseline), the
  combination provides no compound benefit and these axes should remain as independent single-
  axis variations in R8 rather than being promoted as a compound configuration.
- **failure-condition-implementation:** if `Declared responsibility:` keys are present in all
  phases and `champion-baseline:` fields are present in all variation bodies, but the
  `champion-baseline:` citation uses an unqualified variation ID ("V-03" rather than "V-03 R6"),
  the combination independently fails C-34 — the inertia-framing comparison denominator must be
  round-qualified to be unambiguous across experimental iterations, and an unqualified label
  defeats the C-08/C-16 explicitness benefit the `champion-baseline:` field was added to provide.

---

**Combination pass: output-format x inertia-framing**
*C-04 exception explicitly invoked. `Declared responsibility:` keys in Phase 1 and Phase 2
(output-format axis) and `champion-baseline:` field at variation-body scope (inertia-framing
axis) are both active. The generated variations are still single-axis — each changes one axis
from the baseline skill. The combination applies to the generation scaffolding structure, not
to the individual variations themselves.*

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

## VARIATION MAP — Immutable after Phase 2 begins

Before Phase 1 begins, commit the axis assignment and per-variation per-criterion directional
predictions for each of the {N} planned variations. Fill every row and every direction cell.
A direction cell without both a verdict and a mechanism sentence is not complete.

| V | Assigned Axis | Criterion Target | C-01 Direction | C-04 Direction | C-07 Direction | Notes |
|---|--------------|-----------------|----------------|----------------|----------------|-------|
[Fill all {N} rows. Each direction cell: verdict (up / down / no-change) + one sentence
mechanism. Do not proceed to Phase 1 until all rows are filled.]

**Do not revise this table after Phase 2 begins.
The AXIS-FREEZE PROTOCOL in Phase 2 reads axis assignments from this table.**

PHASE 1 — COMMIT VARIATION HEADERS
Declared responsibility: lock axis assignments by writing a complete variation header for each
planned variation — every field populated, no field blank, axis value matching the VARIATION
MAP assignment exactly.

Before writing any variation body, commit a full variation header for each of the {N} axes
assigned in the VARIATION MAP. Every field required. No field may be blank.

Header format:

```
variation: V-NN
axis: [axis name — must match VARIATION MAP assigned axis for this V]
pole: [one phrase — the specific change this variation makes on this axis]
baseline-delta: [one sentence — the single structural element that changes, nothing else]
completeness-risk: [the section most at risk of omission in this specific body]
criterion-target: [C-NN by ID]
direction: [increases / decreases / stabilizes] [criterion name] pass rates
mechanism: [structural pathway from axis change to criterion outcome — name the mechanism,
            not the outcome]
failure-condition: [if criterion pass rate does not exceed [V-NN RN result], the mechanism
                   is refuted. Name the prior-round comparison baseline with round qualifier.]
score-prediction:
  C-01: [pass / partial / fail] — [one sentence mechanism]
  C-04: [pass / partial / fail] — [name the contamination risk for this axis]
  C-07: [pass / partial / fail] — [name the structural element producing hypothesis quality]
  C-09: [pass / partial / fail] — [one sentence mechanism]
```

Review all {N} headers. Verify every axis matches the VARIATION MAP. Commit. Do not revise
axis assignments after Phase 2 begins.

PHASE 2 — GENERATE VARIATION BODIES
Declared responsibility: write each committed variation body in full under the AXIS-FREEZE
PROTOCOL — the committed axis is the only element that changes from the baseline; every section
written out; no placeholders; no cross-references to other variations; `champion-baseline:`
field populated with round-qualified prior-champion citation before the AXIS-FREEZE PROTOCOL.

For each committed header, write the complete variation body. The AXIS-FREEZE PROTOCOL reads
the committed axis from the VARIATION MAP — the authoritative source.

AXIS-FREEZE PROTOCOL (fires once per body, before writing begins):

  Step 1 — Read: state the axis name assigned in the VARIATION MAP for this body (V-NN:
  [axis name]). [read from VARIATION MAP]

  Step 2 — Write one freeze declaration for every axis in the canonical list:
    - role-sequence:       [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - output-format:       [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - lifecycle-emphasis:  [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - phrasing-register:   [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - inertia-framing:     [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - scoring-granularity: [FROZEN | COMMITTED — read from VARIATION MAP for this body]

  All six canonical axes must appear. Exactly one marked COMMITTED. Five marked FROZEN.
  A freeze list with fewer than six entries is incomplete — do not proceed until all six
  entries are present.

  Step 2B — Cross-artifact axis consistency check (fires before Step 3):
    - VARIATION MAP assigned axis for this V-NN: [state the axis from the VARIATION MAP row]
      [read from VARIATION MAP]
    - Phase 1 header declared axis for this V-NN: [state the axis from the Phase 1 header]
    - Consistency verdict: [CONSISTENT | AXIS DIVERGENCE]
    - If AXIS DIVERGENCE: state which artifact carries the incorrect axis assignment and halt.
      Do not proceed to Step 3 until the divergence is resolved and the verdict reads CONSISTENT.

  Step 3 — Write the body: change only the COMMITTED axis. Write the full body — every
  section, every instruction. No diffs. No cross-references to other variations.
  Every structural section present.

Label format:

### V-NN — [Axis: Pole Description]

[variation header from Phase 1 — do not revise]

champion-baseline: [V-NN RN — one sentence: the prior-round champion variation and the specific
                   pole this variation changes from. Name the champion by round and variation ID.
                   Format: "V-NN RN: the [axis] baseline pole was [description]; this variation
                   changes [specific element] to [new value]." Round qualifier required — citing
                   "V-NN" without the round tag is a completeness failure.]

AXIS-FREEZE PROTOCOL:
[Step 1: VARIATION MAP axis declaration for this V]
[Step 2: six-entry freeze list — all six canonical axes filled, each labeled "read from VARIATION MAP"]
[Step 2B: VARIATION MAP axis, Phase 1 header axis, Consistency verdict: CONSISTENT / AXIS DIVERGENCE]
[Step 3: "Proceeding to write COMMITTED axis change only."]

[COMPLETE SKILL BODY — all sections, all instructions, fully written]

Do not begin the next variation until the current body is complete, the AXIS-FREEZE PROTOCOL
shows all six canonical axis entries, and Step 2B shows CONSISTENT.

PHASE 3 — FINDINGS
Declared responsibility: post-generation axis consistency audit, champion-baseline citation
audit, combination candidates, evaluation order, anchor designation.

1. Axis alignment confirmation (post-generation audit):

| V | Axis (VARIATION MAP) | Axis (Phase 1 header) | Step 2B In-Loop Result | Post-Generation Match? |
|---|---------------------|----------------------|------------------------|------------------------|

Flag any ESCAPED DIVERGENCE as a protocol failure.

2. Champion-baseline and Declared responsibility audit:

| V | All 3 phases carry `Declared responsibility:` key? | `champion-baseline:` field present in body? | Round qualifier present in champion citation? | Champion pole matches VARIATION MAP baseline? |
|---|-----------------------------------------------------|----------------------------------------------|-----------------------------------------------|-----------------------------------------------|

A "No" in column 2 fails C-33. A "No" in column 3 is a completeness failure.
A "No" in column 4 independently fails C-34 (ambiguous denominator). A "No" in column 5
indicates inertia-framing contamination — the cited pole does not match the declared axis
baseline.

3. Combination candidates (compound-effects model):

| Priority | Axis Pair | V-NN Basis | Failure Modes Per Axis | Residual Weakness After First Axis Only | Compound Criterion Effect (Both Active) | Criteria Targeted |
|----------|-----------|------------|------------------------|-----------------------------------------|-----------------------------------------|-------------------|

Column rules: Failure Modes cites criterion ID per axis. Residual Weakness is a concrete gap.
Compound Criterion Effect names a criterion ID distinct from what either axis achieves alone.
A row with any blank column is omitted. Priority rationale: one sentence per HIGH or MEDIUM row.

4. Evaluation order:

| Priority | V | Axis | Cost | Independence | Cross-Round Dependency | Sequencing Rationale |
|----------|----|------|------|--------------|------------------------|----------------------|

Cross-round dependency format: "R[round] / V-NN / [metric name]" or "none."

5. Anchor: one variation. Justify structural impact, isolation quality, detectable failure
   condition — one sentence each.

---

## Combination Roadmap (C-09, C-22)

Axis pairings available for R8 based on R7 results. Evaluated after R7 single-axis passes
are scored.

| Priority | Axis Pair | V-NN Basis | Residual Weakness After First Axis Only | Compound Criterion Effect (Both Active) | Criteria Targeted |
|----------|-----------|------------|----------------------------------------|-----------------------------------------|-------------------|
| HIGH | output-format x phrasing-register | V-01 R7 x V-02 R7 | V-01 R7 alone: all phases have `Declared responsibility:` key, but hypothesis schema remains flat — C-19 not forced; V-02 R7 alone: four-part schema enforced in headers, but Phase 1 and Phase 2 have no `Declared responsibility:` key — C-33 not satisfied | Combining both: Phase 1 carries both the `Declared responsibility:` key (phase commitment structurally declared) and the four-part `hypothesis:` schema (hypothesis structurally enforced) simultaneously — first R7 configuration where C-33 and C-19 are both structurally detectable at Phase 1 scope | C-33, C-19, C-07 |
| HIGH | output-format x inertia-framing | V-01 R7 x V-03 R7 | V-01 R7 alone: all phases labeled, but no body-level champion citation — reviewer must consult pre-generation section to identify the status-quo competitor; V-03 R7 alone: body-level champion citation present, but Phase 1 and Phase 2 lack `Declared responsibility:` key — C-33 not satisfied | Combining both: every phase structurally declares its commitment (C-33) AND every variation body names the specific prior-round champion it competes with (C-08/C-16 at body scope) — two complementary structural declarations at different scopes | C-33, C-08, C-16 |
| MEDIUM | phrasing-register x inertia-framing | V-02 R7 x V-03 R7 | V-02 R7 alone: four-part schema enforced, but champion baseline is implicit at body level; V-03 R7 alone: champion citation present, but hypothesis schema remains flat | Combining both: four-part schema forces all hypothesis parts grouped (C-19) AND champion-baseline citation makes the comparison denominator explicit at body scope (C-08/C-16) — the mechanism sentence in the schema can directly reference the champion pole, creating a linked hypothesis-to-baseline traceability chain | C-19, C-08, C-16 |

---

## Evaluation Order (C-12)

| Priority | V | Axis | Cost | Independence | Cross-Round Dependency | Sequencing Rationale |
|----------|----|------|------|--------------|------------------------|----------------------|
| 1 | V-01 | output-format | low: single label addition to two phase headers | independent of V-02 and V-03 single-axis results | none — C-33 not targeted in any prior single-axis pass | Establishes C-33 baseline for R7; required denominator for V-04 and V-05 combination passes |
| 2 | V-02 | phrasing-register | low: header format schema change only | independent of V-01 and V-03 results | none — C-19 not targeted in any prior single-axis pass | Establishes C-19 baseline for R7; required denominator for V-04 combination pass |
| 3 | V-03 | inertia-framing | low: one field addition to label format | independent of V-01 and V-02 results | none | Establishes C-08/C-16 body-scope baseline for R7; required denominator for V-05 combination pass |
| 4 | V-04 | output-format x phrasing-register | medium: requires V-01 R7 and V-02 R7 results to assess compound benefit | depends on V-01 and V-02 results | R7 / V-01 / C-33 pass rate; R7 / V-02 / C-19 pass rate | Combination only meaningful if both V-01 and V-02 pass their criterion targets |
| 5 | V-05 | output-format x inertia-framing | medium: requires V-01 R7 and V-03 R7 results | depends on V-01 and V-03 results | R7 / V-01 / C-33 pass rate; R7 / V-03 / C-08 pass rate | Combination only meaningful if both V-01 and V-03 pass their criterion targets |

---

## Pre-Combination Axis Tension Note (C-13)

**output-format x phrasing-register tension (V-04):** Phase 1 now carries two structural
additions: a `Declared responsibility:` key (output-format axis) and a nested `hypothesis:`
schema (phrasing-register axis). Both add length and structural weight to Phase 1. If Phase 1
becomes so long that generators truncate variation bodies to fit context limits, output-format
dominates — the phase label is shorter and less likely to be compressed. Prediction: if one
axis is dropped under context pressure, phrasing-register drops first (the schema is more
verbose); C-33 survives but C-19 fails. Run V-01 and V-02 independently first to confirm
neither alone causes truncation before running V-04.

**output-format x inertia-framing tension (V-05):** The `champion-baseline:` field (inertia-
framing axis) is placed at variation-body level, not at phase level. The `Declared responsibility:`
keys (output-format axis) are at phase level. These two additions operate at different scopes
and have no structural overlap — tension is low. However, the `champion-baseline:` field requires
a round-qualified citation, which itself tests C-34. If generators write the citation without a
round qualifier, this fails C-34 in V-05 even if C-33 is satisfied. Prediction: output-format
dominates (phase-level label is enforced by phase structure); inertia-framing is the failure
mode to watch.

---

## Axis-Tension Pre-Ranking (C-13)

If V-04 and V-05 must each have one axis drop, which dominates?

- **V-04:** output-format dominates phrasing-register. The `Declared responsibility:` key is a
  single line addition; the `hypothesis:` block is a multi-line schema that requires four sub-
  fields to be populated. Under generation pressure, the schema is more likely to be collapsed
  back to flat fields. Run V-02 (phrasing-register single-axis) first to confirm schema
  compliance before running V-04.

- **V-05:** output-format dominates inertia-framing. The `Declared responsibility:` keys are
  anchored to phase structure (always present as phase opens); the `champion-baseline:` field is
  in the label format (inside the generation loop, one per body). Under context pressure, the
  per-body field is more likely to be omitted than the per-phase key. Run V-03 (inertia-framing
  single-axis) first to confirm champion-baseline compliance before running V-05.

---

## Anchor

**V-01** (output-format, C-33).

- Structural impact: converts all three phases to C-33-compliant `Declared responsibility:`
  labeled keys — the only axis change in R7 that directly satisfies a new v7 criterion with a
  single structural addition.
- Isolation quality: the change is exactly one element per phase (add one labeled line after
  the phase title in Phase 1 and Phase 2); no other protocol, field, or section affected.
- Detectable failure condition: if Phase 1 or Phase 2 `Declared responsibility:` key text
  restates the phase title without adding structural specificity, C-23 is independently violated
  — detectable by comparing the key text against the phase title verbatim.
