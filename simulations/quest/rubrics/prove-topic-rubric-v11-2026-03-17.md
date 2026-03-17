Written to `simulations/quest/rubrics/prove-topic-rubric-v11-2026-03-17.md`.

---

**v11 summary:**

**3 new aspirational criteria (C-39 through C-41), no reductions. Aspirational pool: 30 -> 33 pts. Total: 104 -> 107.**

| ID | Signal source | What it codifies |
|----|--------------|-----------------|
| C-39 | R10 all variations | SESSION INVARIANTS standalone block explicitly enumerates all five active invariants (A/B/C/D/E) as a unified complete system with canonical labels and stage-scope annotations — goes beyond C-12 (A-D floor) + C-36 (E added separately) to require unified five-invariant declaration |
| C-40 | R10 V-02/V-04/V-05 | ROLE A initialization reads Stage 0 synthesis_closure_form + synthesis_mandate_label by field name, creating three-anchor chain Stage 0 -> ROLE A -> Stage 5 parallel to C-27 (ROLE A contract) -> C-31 (Stage 5 gate) contract-verification pattern |
| C-41 | R10 V-03/V-05 | Stage 0 EXIT SIGNAL explicitly confirms synthesis_closure_form matches the pre-registered CAMPAIGN CLOSURE CANONICAL FORM by naming both, closing the registration-to-commitment loop at Stage 0 — not deferred to Stage 5 |

**R10 composite scores under v11:**

| Variation | Total | New pts |
|-----------|-------|---------|
| V-01 | 104/107 | +C-39 |
| V-02 | 104/107 | +C-40 |
| V-03 | 104/107 | +C-41 |
| V-04 | 105/107 | +C-39, C-40 |
| V-05 | 106/107 | +C-39, C-40, C-41 |

V-05 is the convergence candidate at 106/107. The new structural pattern is a **three-anchor pre-commitment chain** binding Stage 0, ROLE A initialization, and Stage 5 into a single continuous verification spine:
`C-39` (unified five-invariant SESSION INVARIANTS) completes the governance registration layer.
`C-40` (ROLE A reads Stage 0 fields by name) creates the Stage 0 -> ROLE A verification link.
`C-41` (CLOSURE CANONICAL FORM matched at Stage 0) closes the registration-to-commitment loop before any role executes.

Together C-39/C-40/C-41 extend the C-27/C-31/C-37 pre-commitment architecture into a fully cross-wired three-anchor chain: the pre-registered canonical form (C-35) is verified against Stage 0 commitment at Stage 0 time (C-41); Stage 0 commitments are verified at ROLE A initialization (C-40); ROLE A initialization now carries all four pre-stage commitments (incumbent_anchor_read, displacement_read_contract, synthesis_closure_form_read, synthesis_mandate_label_read); Stage 5 ENTRY CONDITIONS verify all upstream commitments by field name.

---

## Essential Criteria (50 pts total -- campaign fails without these)

### C-01 -- All 6 EXIT SIGNALs Declared in Order

- **Weight**: essential (10 pts)
- **Category**: correctness
- **Text**: All six campaign EXIT SIGNALs are declared in the correct order: gate_open
  (ROLE B / Stage 0), hypothesis_locked (Stage 1), websearch_complete (Stage 2),
  interview_complete (Stage 3), prototype_complete (Stage 4), synthesis_complete (Stage 5).
- **Pass condition**: Output contains all six EXIT SIGNAL declarations, each explicitly
  labeled and in the correct stage sequence. Any missing EXIT SIGNAL = FAIL. EXIT SIGNALs
  out of sequence = FAIL.

### C-02 -- All 6 Artifacts Written and Confirmed

- **Weight**: essential (10 pts)
- **Category**: behavior
- **Text**: All six artifact write operations are confirmed in output: scout artifact
  (ROLE B / Stage 0), hypothesis canvas (Stage 1), websearch artifact (Stage 2),
  interview artifact (Stage 3), prototype artifact (Stage 4), and synthesis handoff
  (Stage 5). Each confirmation must name the artifact path or file, or state the write
  as confirmed. Silent omission of any artifact write confirmation = FAIL.

### C-03 -- Session Invariant D Verbatim at S2/S3/S4

- **Weight**: essential (10 pts)
- **Category**: correctness
- **Text**: SESSION INVARIANTS registers the canonical Invariant D template wording for
  Stages 2, 3, and 4, and each stage ENTRY CONDITIONS echo the registered template verbatim.
- **Pass condition**: The SESSION INVARIANTS block registers the canonical template wording
  for all three Invariant D checkpoints. Each stage ENTRY CONDITIONS or INCUMBENT CHECK
  TABLE intro echoes the registered template verbatim. The three registered templates cover
  SESSION INVARIANTS Invariant D: Stage 2 template ("Does [evidence item] support the
  displacement of..."), Stage 3 template ("Does [practitioner account] reveal a viable
  transition path..."), Stage 4 template ("Does [prototype result] make a credible case for
  displacing..."). Any deviation from registered template wording = FAIL.

### C-04 -- Synthesis Verdict Present

- **Weight**: essential (10 pts)
- **Category**: correctness
- **Text**: Stage 5 SYNTHESIS DECLARATIONS contains hypothesis_verdict with a binary or
  qualified verdict, confidence_composite as a numeric value, and key_risk as a named
  statement.
- **Pass condition**: Stage 5 output contains all three: hypothesis_verdict (SUPPORTED,
  REFUTED, PARTIALLY SUPPORTED, or equivalent binary/qualified verdict), confidence_composite
  (numeric value 1-10), and key_risk (named risk statement). All three must be labeled
  key-value pairs. Any field missing or verdict present only as embedded prose = FAIL.

### C-05 -- Null Tally Chain Cross-Checked

- **Weight**: essential (10 pts)
- **Category**: correctness
- **Text**: Stage 4 cross-checks the running null tally count from Stage 3, and Stage 5
  Block 3 reconstructs the full S2-S3-S4 null tally chain and cross-checks against
  Stage 4 null_tally_final.
- **Pass condition**: Stage 4 output contains a null_tally_cross_check field explicitly
  comparing the running count from Stage 3 to Stage 4 final count with a match assertion
  (true/false). Stage 5 Block 3 output reconstructs the S2/S3/S4 chain explicitly and
  cross-checks vs Stage 4 null_tally_final. Any stage omitting the cross-check = FAIL.

---

## Recommended Criteria (24 pts total -- output is better with these)

### C-06 -- Gate S Scout Loader Executes

- **Weight**: recommended (8 pts)
- **Category**: coverage
- **Text**: ROLE B executes and either confirms scout_loaded = true or halts campaign
  with CAMPAIGN BLOCKED.
- **Pass condition**: Output shows ROLE B execution with scout_artifact field populated
  (path named or stated as not found) and gate_s_cleared explicitly set to true or false.
  If false, output must show "CAMPAIGN BLOCKED" and record the blocking step.
  Silent omission of ROLE B = FAIL.

### C-07 -- Handoff Table All 11 Fields With Derivation

- **Weight**: recommended (8 pts)
- **Category**: format
- **Text**: Stage 5 HANDOFF TABLE contains all 11 required fields, each with a
  [derived from: X] annotation.
- **Pass condition**: HANDOFF TABLE in Stage 5 contains every field from the PRE-COMMITTED
  HANDOFF SCHEMA: scout_anchor, incumbent_threat_locked, hypothesis, counter_hypothesis,
  s2_ce_verdict, s3_ce_verdict, s4_ce_verdict, null_tally_final, co_activation_confirmed,
  incumbent_defense_closed, confidence_composite (11 total, plus schema_compliance_confirmed
  as confirmation row). Every field carries [derived from: X] annotation. Any unlabeled
  field = FAIL.

### C-08 -- Counter-Hypothesis Resolution

- **Weight**: recommended (8 pts)
- **Category**: depth
- **Text**: Stage 5 resolves the counter-hypothesis from Stage 1 with an explicit verdict
  and citation.
- **Pass condition**: Stage 5 COUNTER-HYPOTHESIS RESOLUTION TABLE contains the
  counter-hypothesis value carried from Stage 1 and assigns a verdict of REFUTED,
  PARTIALLY REFUTED, or OPEN RISK. OPEN RISK triggers one-tier confidence reduction
  (stated in output). Missing table or verdict without citation = FAIL.

---

## Aspirational Criteria (33 pts total -- raise the bar)

### C-09 -- Atomic Dual-Lock Fires When Warranted

- **Weight**: aspirational (1 pt)
- **Category**: behavior
- **Text**: When null_tally_final >= 3, the ATOMIC DUAL-LOCK activates both SESSION
  INVARIANT A (adversarial review) and SESSION INVARIANT B (confidence cap) explicitly.
- **Pass condition**: If null_tally_final >= 3 in the output, Stage 5 declares:
  co_activation_confirmed: dual_lock_fired, names the adversarial_reviewer_type registered
  at campaign open, and applies confidence_composite -= 2 with the hard-cap note. If
  null_tally_final < 3, criterion is satisfied by co_activation_confirmed: not_triggered.
  Fired dual-lock without both Lock 1 and Lock 2 = FAIL.
- **v2 signal**: Differentiated output quality at the evidence-ceiling edge case.
- **Reduced from 5 pts to 3 pts in v4**: C-18 covers the Invariant E structural checkpoint
  that makes all dual-lock mechanics architecturally consistent.
- **Reduced from 3 pts to 2 pts in v5**: C-22 extends the two-layer enforcement architecture
  to the binding mechanism itself.
- **Reduced from 2 pts to 1 pt in v6**: C-24 and C-26 further extend architectural coverage.
  C-09 is the 1-pt floor: did the dual-lock fire when warranted. Unchanged in v7, v8, v9,
  v10, v11.

### C-10 -- Incumbent Displacement Framing Throughout

- **Weight**: aspirational (1 pt)
- **Category**: depth
- **Text**: Every evidence item across all three check tables explicitly argues for or
  against displacement of the incumbent -- not merely describing the topic.
- **Pass condition**: Stage 2, 3, and 4 INCUMBENT CHECK TABLES each contain at least one
  Yes verdict (or a stated reason all are Inconclusive/No), and the Stage 5 evidence_summary
  cites the Stage 4 displacement verdict explicitly ("Stage 4 displacement verdict:
  [Yes/No/Pending]"). Generic summaries without displacement framing = FAIL.
- **v3 signal**: V-05 added per-stage "Displacement read:" fields (C-16). C-10 checks the
  framing in outputs; C-16 checks that the structural mechanism to produce it was present.
- **Reduced from 5 to 3 pts in v4**, **3 to 2 pts in v5**, **2 to 1 pt in v6**: C-25
  completes the chain. C-10 is the 1-pt floor: did Stage 5 cite the Stage 4 displacement
  verdict at all. Unchanged in v7, v8, v9, v10, v11.

### C-11 -- Invariant Enforcement Language is Mechanical, Not Advisory

- **Weight**: aspirational (1 pt)
- **Category**: correctness
- **Text**: Every SESSION INVARIANT uses explicit hard-failure language at its enforcement
  checkpoint, not advisory phrasing.
- **Pass condition**: At minimum, the enforcement statements for Invariant D (C-03), the
  null tally rule (C-05), and the handoff schema (C-07) use mechanical failure language:
  e.g., "deviation = format error", "mismatch = integrity failure", "unlabeled field = FAIL".
  Soft advisory language ("try to follow", "make sure to", "where possible") at any of these
  three checkpoints = FAIL.
- **Round 1 signal**: V-01 (score 90) kept hard-failure language intact. V-03 (score 62)
  softened to advisory and lost three essential PARTIALs.
- **Reduced from 3 to 2 pts in v4**, **2 to 1 pt in v5**: C-11 is the 1-pt floor: did
  mechanical language appear at the three checkpoints at all. Unchanged in v6, v7, v8, v9,
  v10, v11.

### C-12 -- SESSION INVARIANTS Registered in Standalone Pre-Stage Block

- **Weight**: aspirational (1 pt)
- **Category**: format
- **Text**: All SESSION INVARIANTS appear in a dedicated named block before Stage 0
  executes, in addition to any inline references within stage bodies.
- **Pass condition**: Output contains a named SESSION INVARIANTS section (TABLE or LIST)
  that appears before Stage 0 gate_open EXIT SIGNAL, enumerates all active invariants
  (A through D at minimum), and states each invariant activation condition. Invariants
  appearing only inline without a standalone pre-stage registration block = FAIL.
- **Round 1 signal**: V-02 (score 76) embedded invariants inline; C-03 and C-05 degraded.
- **Reduced from 3 to 2 pts in v3**, **2 to 1 pt in v6**: C-12 is the 1-pt floor: did the
  standalone block exist before Stage 0 at all. C-39 checks that the block presents all five
  invariants as a unified complete system; C-12 remains the 1-pt floor for any standalone
  block with A-D. Unchanged in v7, v8, v9, v10, v11.

### C-13 -- Stage 5 Synthesis Fields Isolated as Named Declarations

- **Weight**: aspirational (1 pt)
- **Category**: format
- **Text**: hypothesis_verdict, confidence_composite, and key_risk each appear as explicitly
  labeled standalone field declarations in Stage 5 -- not embedded within prose paragraphs.
- **Pass condition**: Each of the three fields appears as a labeled key-value pair
  (e.g., hypothesis_verdict: SUPPORTED, confidence_composite: 7, key_risk: [text]) that
  can be extracted by pattern-matching without reading surrounding prose. Any field
  identifiable only by reading prose context = FAIL.
- **Reduced from 3 to 2 pts in v4**, **2 to 1 pt in v7**: C-17 (SYNTHESIS DECLARATIONS
  with explicit prohibition) is the richer structural mechanism. C-13 is the 1-pt floor:
  did Stage 5 synthesis fields appear as labeled key-value pairs at all. Unchanged in v8,
  v9, v10, v11.

### C-14 -- Two-Layer Enforcement Architecture

- **Weight**: aspirational (1 pt)
- **Category**: correctness
- **Text**: Failure labels are registered canonically in the SESSION INVARIANTS block and
  echoed verbatim at each inline enforcement checkpoint, creating bidirectional enforcement.
- **Pass condition**: The SESSION INVARIANTS TABLE or LIST establishes the canonical failure
  label for each invariant (FORMAT ERROR for Invariant D, INTEGRITY FAILURE for null tally,
  DUAL-LOCK ERROR for dual-lock, ORDER ERROR for Invariant C, FAIL for handoff schema).
  Inline enforcement annotations at each stage checkpoint echo the exact label from the
  registered source. If inline labels diverge from registered labels, or if labels appear
  only inline without canonical registration in the SESSION INVARIANTS block = FAIL.
- **Round 2 signal**: V-04 and V-05 used this architecture. Drift at Stage 2 incurs FORMAT
  ERROR from two structural directions simultaneously, making soft deviation self-incriminating.
  Unchanged in v5, v6, v7, v8.
- **Reduced from 2 pts to 1 pt in v9**: C-34 extends the two-layer enforcement architecture
  into the Stage 5 synthesis instruction layer, specifically requiring the evidence_summary
  mandate to carry a registered failure label for omission. C-14 universally scored at partial
  (1/2) in R8 because dual-lock inline used "dual_lock_fired / BLOCKED" rather than the
  registered "DUAL-LOCK ERROR" label -- the two-layer pattern held for other invariants but
  degraded at dual-lock inline. C-14 is now the 1-pt floor: did bidirectional label
  enforcement architecture exist (SESSION INVARIANTS registration + inline echo) for any
  invariant at all. C-38 checks that Block 3 dual-lock annotations echo the verbatim
  registered DUAL-LOCK ERROR label at each lock step. Unchanged in v10, v11.

### C-15 -- CAMPAIGN OPEN Block Pre-Registers Displacement Context

- **Weight**: aspirational (1 pt)
- **Category**: format
- **Text**: A CAMPAIGN OPEN section appears before SESSION INVARIANTS registration, recording
  incumbent and incumbent_strength so all Invariant D checks operate against a named,
  persistent displacement frame.
- **Pass condition**: Output contains a CAMPAIGN OPEN block that appears before the SESSION
  INVARIANTS block and declares at minimum incumbent (the tool or practice being displaced)
  and incumbent_strength (quantified resistance level). Stages that define displacement
  context inline, re-establishing it per stage rather than carrying it forward = FAIL.
- **Reduced from 2 to 1 pt in v5**: C-21 captures the richer behavior. C-15 is the 1-pt
  floor: did CAMPAIGN OPEN block exist with incumbent and incumbent_strength.
  Unchanged in v6, v7, v8, v9, v10, v11.

### C-16 -- Per-Stage Displacement Read Fields

- **Weight**: aspirational (1 pt)
- **Category**: depth
- **Text**: Each of Stages 2, 3, and 4 includes a dedicated "Displacement read:" synthesis
  field summarizing the stage displacement verdict, in addition to the INCUMBENT CHECK TABLE.
- **Pass condition**: Each of Stages 2, 3, and 4 contains a labeled "Displacement read:"
  field that synthesizes whether the stage evidence supports, challenges, or is inconclusive
  about incumbent displacement. Stages that carry verdict information only in the INCUMBENT
  CHECK TABLE rows, without a synthesis field = FAIL.
- **Reduced from 2 to 1 pt in v5**: C-20 and C-23 extend the chain. C-16 is the 1-pt floor:
  did stages declare Displacement read fields at all. Unchanged in v6, v7, v8, v9, v10, v11.

### C-17 -- SYNTHESIS DECLARATIONS Section With Explicit Prohibition

- **Weight**: aspirational (1 pt)
- **Category**: format
- **Text**: Stage 5 opens with a named SYNTHESIS DECLARATIONS section whose header or
  preamble contains an explicit prohibition against embedding synthesis fields in prose.
- **Pass condition**: Stage 5 contains a distinctly named section (SYNTHESIS DECLARATIONS
  or equivalent) that appears before evidence_summary and whose header or preamble explicitly
  states that synthesis fields must not appear as prose sub-items. Qualifying language: "Do
  not embed these values in prose sentences. Each on its own line, extractable by label
  match." or equivalent explicit prohibition. A prompt that produces isolated fields
  (passing C-13) without explicit prohibition text in the section header = FAIL.
- **Reduced from 2 to 1 pt in v7**: C-29 (EXIT SIGNAL chain closure audit) extends SYNTHESIS
  DECLARATIONS from a structural prohibition declaration to a chain-closure confirmation.
  C-17 (prohibition declaration) + C-25 (citation present) + C-29 (EXIT SIGNAL audit) form
  a three-layer synthesis governance architecture. C-17 is the 1-pt floor: did a SYNTHESIS
  DECLARATIONS section with explicit prohibition text exist at all. Unchanged in v8, v9,
  v10, v11.

### C-18 -- Invariant E Checkpoint at Handoff Schema

- **Weight**: aspirational (1 pt)
- **Category**: format
- **Text**: The Stage 5 HANDOFF TABLE uses a named Invariant E enforcement checkpoint with
  a canonical failure label registered in SESSION INVARIANTS and echoed inline at the
  schema_compliance_confirmed row.
- **Pass condition**: The SESSION INVARIANTS block registers a canonical label for Invariant
  E (e.g., "Invariant E checkpoint -- FAIL" for any unlabeled or missing handoff schema
  field). The Stage 5 HANDOFF TABLE contains a schema_compliance_confirmed row that echoes
  this exact label (not a paraphrase). Handoff enforcement present but using ad-hoc phrasing
  not registered in SESSION INVARIANTS = FAIL. schema_compliance row absent = FAIL.
- **Round 3 signal**: V-01, C-07 evidence: "All 11 fields with [derived from: X]; Invariant E
  checkpoint -- FAIL present." Extends C-14 to Invariant E. Unchanged in v5, v6, v7, v8.
- **Reduced from 2 pts to 1 pt in v9**: C-18 universally passes in R8 and has done so for
  several rounds. The Invariant E checkpoint with registered label + schema_compliance_confirmed
  echo is well-established behavior. C-18 is the 1-pt floor: did Invariant E checkpoint exist
  with a registered label in SESSION INVARIANTS echoed at the schema_compliance_confirmed row.
  Note: C-36 elevates the Invariant E registration to a named SYNTHESIS EVIDENCE MANDATE row
  with SYNTHESIS-FAIL label; C-18 remains the 1-pt floor for any Invariant E registration.
  Unchanged in v10, v11.

### C-19 -- Invariant D Template Binding to CAMPAIGN OPEN

- **Weight**: aspirational (1 pt)
- **Category**: correctness
- **Text**: The displacement-question templates in SESSION INVARIANTS Invariant D explicitly
  interpolate [incumbent from CAMPAIGN OPEN], binding them structurally to the pre-registered
  displacement context rather than restating the incumbent inline.
- **Pass condition**: The SESSION INVARIANTS Invariant D entry contains template text that
  references the CAMPAIGN OPEN context by name (e.g., "Does [evidence item] support the
  displacement of [incumbent from CAMPAIGN OPEN]..."). Stage tables carry the bound template
  text. Templates that name the incumbent as a literal string, re-establishing it per stage,
  rather than binding to CAMPAIGN OPEN = FAIL.
- **Reduced from 2 to 1 pt in v5**: C-22 captures the richer behavior. C-19 is the 1-pt
  floor: does the template use [incumbent from CAMPAIGN OPEN] at all.
  Unchanged in v6, v7, v8, v9, v10, v11.

### C-20 -- Artifact Files Carry Displacement Read Field

- **Weight**: aspirational (1 pt)
- **Category**: depth
- **Text**: The websearch, interview, and prototype artifact files written in Stages 2, 3,
  and 4 each contain a labeled "Displacement read:" field in their artifact content, making
  displacement evidence portable outside the stage output.
- **Pass condition**: Each of the three write confirmations for {topic}-websearch-{date}.md,
  {topic}-interview-{date}.md, and {topic}-prototype-{date}.md includes, or the artifact
  described content includes, a labeled "Displacement read:" as part of the artifact body.
  A "Displacement read:" present only in stage output but not in artifact file content is
  insufficient. All three artifacts must carry the field = FAIL if any absent.
- **Reduced from 2 to 1 pt in v7**: C-28 (Stage 5 entry conditions gate on all three artifact
  Displacement reads) is the structural enforcement that C-20 enables. C-20 is the 1-pt
  floor: did artifact files carry Displacement read field at all. Unchanged in v8, v9, v10,
  v11.

### C-21 -- CAMPAIGN OPEN INCUMBENT ANCHOR With "Do Not Re-Establish" Prohibition

- **Weight**: aspirational (1 pt)
- **Category**: format
- **Text**: The CAMPAIGN OPEN block contains a named INCUMBENT ANCHOR sub-section and an
  explicit prohibition against re-establishing the incumbent per stage.
- **Pass condition**: CAMPAIGN OPEN contains (a) a labeled INCUMBENT ANCHOR sub-section
  isolating incumbent and incumbent_strength as a named unit and (b) explicit prohibition
  text stating the incumbent must not be re-established inline at individual stages (e.g.,
  "Do not re-establish the incumbent per stage. Carry forward from CAMPAIGN OPEN."). A flat
  key-value CAMPAIGN OPEN block without INCUMBENT ANCHOR labeling or prohibition text --
  even if incumbent and incumbent_strength are present (passing C-15) -- = FAIL.
- **Reduced from 2 to 1 pt in v6**: C-24 captures the richer behavior. C-21 is the 1-pt
  floor: did CAMPAIGN OPEN contain INCUMBENT ANCHOR sub-section + prohibition.
  Unchanged in v7, v8, v9, v10, v11.

### C-22 -- Invariant D Binding Resolution Note With Literal-String Failure Label

- **Weight**: aspirational (1 pt)
- **Category**: correctness
- **Text**: SESSION INVARIANTS Invariant D includes a binding resolution note naming how
  [incumbent from CAMPAIGN OPEN] resolves, and registers a canonical failure label for
  using the incumbent as a literal string in the template.
- **Pass condition**: The SESSION INVARIANTS Invariant D entry contains (a) a binding
  resolution note of the form "Binding: [incumbent from CAMPAIGN OPEN] resolves to
  incumbent_name" (or equivalent explicit resolution statement) and (b) a canonical failure
  label for the binding violation (e.g., "naming as literal string = FORMAT ERROR").
  Templates using [incumbent from CAMPAIGN OPEN] without a binding resolution note or
  failure label = FAIL.
- **Reduced from 2 to 1 pt in v6**: C-26 captures the richer sub-section precision.
  C-22 is the 1-pt floor: did Invariant D carry a binding resolution note + failure label.
  Unchanged in v7, v8, v9, v10, v11.

### C-23 -- Stage 5 Evidence Summary Cites Artifact Displacement Read by Value

- **Weight**: aspirational (1 pt)
- **Category**: depth
- **Text**: Stage 5 evidence_summary references the Displacement read value from at least
  one written artifact directly, confirming that artifact portability (C-20) was consumed
  by Stage 5 synthesis rather than bypassed.
- **Pass condition**: Stage 5 evidence_summary or SYNTHESIS DECLARATIONS body includes a
  direct citation of an artifact Displacement read field by value -- e.g., "websearch
  Displacement read: [value]" or equivalent labeled citation naming the artifact file and
  read value. Citing the Stage 4 displacement verdict without also citing any artifact
  Displacement read value = FAIL. All three artifacts cited is ideal; at least one must
  be cited.
- **Reduced from 2 to 1 pt in v6**: C-25 captures complete chain closure. C-23 is the
  1-pt floor: did Stage 5 cite at least one artifact Displacement read at all.
  Unchanged in v7, v8, v9, v10, v11.

### C-24 -- ROLE A Initialization Confirms INCUMBENT ANCHOR Binding Before Stage 0

- **Weight**: aspirational (1 pt)
- **Category**: correctness
- **Text**: ROLE A initialization explicitly reads and records the resolved incumbent value
  from CAMPAIGN OPEN INCUMBENT ANCHOR before Stage 0 gates, creating a pre-stage binding
  confirmation that mechanically enforces the prohibition registered in C-21.
- **Pass condition**: ROLE A initialization output (appearing before Stage 0 gate_open)
  contains a labeled confirmation reading the INCUMBENT ANCHOR value and recording the
  resolved binding (e.g., "INCUMBENT ANCHOR read: [resolved_value] confirmed. Invariant D
  binding active."). This confirmation must trace the resolved value to CAMPAIGN OPEN
  INCUMBENT ANCHOR by name. A CAMPAIGN OPEN INCUMBENT ANCHOR sub-section + prohibition
  present (passing C-21) without ROLE A explicitly reading and recording the binding = FAIL.
- **Reduced from 2 to 1 pt in v7**: C-27 captures the richer behavior. C-24 is the 1-pt
  floor: did ROLE A confirm INCUMBENT ANCHOR binding and record incumbent_anchor_read
  before Stage 0. Unchanged in v8, v9, v10, v11.

### C-25 -- Stage 5 Evidence Summary Cites All Three Artifact Displacement Reads

- **Weight**: aspirational (1 pt)
- **Category**: depth
- **Text**: Stage 5 evidence_summary cites the Displacement read value from all three
  written artifacts (websearch, interview, prototype), completing the Stage 2/3/4 artifact
  portability chain through Stage 5 synthesis.
- **Pass condition**: Stage 5 evidence_summary or SYNTHESIS DECLARATIONS body includes
  labeled citations of ALL THREE artifact Displacement reads -- from
  {topic}-websearch-{date}.md, {topic}-interview-{date}.md, and {topic}-prototype-{date}.md
  -- each identifying the artifact source and the read value. Citing only one or two artifact
  Displacement reads (passing C-23) without the third = FAIL.
- **Reduced from 2 to 1 pt in v7**: C-29 (EXIT SIGNAL records chain closure) converts C-25
  from an output check into the floor of a three-layer synthesis governance architecture
  (C-17 declaration + C-25 output + C-29 audit record). C-25 is the 1-pt floor: did Stage
  5 evidence_summary cite all three artifact Displacement reads. Unchanged in v8, v9, v10,
  v11.

### C-26 -- Invariant D Binding Note Names CAMPAIGN OPEN INCUMBENT ANCHOR as Source

- **Weight**: aspirational (1 pt)
- **Category**: correctness
- **Text**: The binding resolution note in SESSION INVARIANTS Invariant D explicitly names
  CAMPAIGN OPEN INCUMBENT ANCHOR (the named sub-section) as the binding source, not merely
  CAMPAIGN OPEN (the parent block), cross-wiring the SESSION INVARIANTS chain to the
  CAMPAIGN OPEN chain at sub-section precision.
- **Pass condition**: SESSION INVARIANTS Invariant D binding resolution note uses "CAMPAIGN
  OPEN INCUMBENT ANCHOR" (or the exact name of the INCUMBENT ANCHOR sub-section as
  registered in CAMPAIGN OPEN) as the binding source citation -- e.g., "Binding: [incumbent
  from CAMPAIGN OPEN INCUMBENT ANCHOR] resolves to incumbent_name." A binding note with
  resolution statement + failure label (passing C-22) that references only "CAMPAIGN OPEN"
  without the INCUMBENT ANCHOR sub-section qualifier = FAIL.
- **Reduced from 2 to 1 pt in v7**: C-27 incorporates sub-section precision as a
  prerequisite. C-26 is the 1-pt floor: did the Invariant D binding note name the CAMPAIGN
  OPEN INCUMBENT ANCHOR sub-section as the binding source at all. Unchanged in v8, v9, v10,
  v11.

### C-27 -- ROLE A Pre-Stage Initialization Commits Displacement Evidence Chain

- **Weight**: aspirational (1 pt)
- **Category**: correctness
- **Text**: ROLE A pre-stage initialization confirms both the INCUMBENT ANCHOR binding
  (satisfying C-24) and commits Stages 2, 3, and 4 to writing "Displacement read:" fields
  to their artifact bodies before Stage 0 gates open, unifying the binding chain and
  displacement evidence chain under a single pre-stage structural anchor.
- **Pass condition**: ROLE A initialization output (appearing before Stage 0 gate_open)
  contains both (a) incumbent_anchor_read confirming binding to CAMPAIGN OPEN INCUMBENT
  ANCHOR sub-section by name (satisfying C-24) and (b) an explicit displacement read
  contract statement committing Stages 2/3/4 to writing "Displacement read:" field to
  artifact content before Stage 5 entry (e.g., "Displacement read contract: Stages 2, 3, 4
  will write Displacement read field to artifact bodies. Stage 5 entry will confirm all
  three." or equivalent). ROLE A output that records incumbent_anchor_read without the
  displacement read contract = FAIL for C-27 (C-24 may still pass at 1 pt). Displacement
  read contract without incumbent_anchor_read tracing to INCUMBENT ANCHOR sub-section = FAIL.
- **Round 6 signal**: V-05 (Signal 1). ROLE A Step 2 confirms both incumbent_anchor_read
  AND Stages 2/3/4 committed to writing Displacement read fields, unifying the binding chain
  (C-24/C-26) and displacement evidence chain (C-16/C-20/C-25) under a single pre-stage
  anchor.
- **Reduced from 2 pts to 1 pt in v8**: C-31 captures the richer contract-to-gate
  traceability behavior. C-27 is now the 1-pt floor: did ROLE A pre-stage initialization
  commit both incumbent_anchor_read AND displacement_read_contract in a single block.
  C-40 further extends ROLE A initialization to verify Stage 0 forward-commitment fields
  by name; C-27 remains the 1-pt floor for the two-field ROLE A contract. Unchanged in v9,
  v10, v11.

### C-28 -- Stage 5 Entry Conditions Gate on Displacement Chain Completeness

- **Weight**: aspirational (1 pt)
- **Category**: format
- **Text**: Stage 5 ENTRY CONDITIONS include a structural gate requiring all three artifact
  Displacement reads to be confirmed written before synthesis begins, making chain
  completeness architecturally enforced at Stage 5 entry rather than relying on Stage 5
  synthesis to notice their absence.
- **Pass condition**: Stage 5 ENTRY CONDITIONS include a labeled completeness check of the
  form "[ ] All three artifact Displacement read fields confirmed written (websearch,
  interview, prototype) -- Stage 5 will consume all three" (or equivalent explicit
  statement). Stage 5 ENTRY CONDITIONS that gate only on the Stage 4 EXIT SIGNAL without
  an explicit displacement chain completeness check = FAIL. Displacement read completeness
  check appearing only in Stage 5 body (not as an entry condition) = FAIL.
- **Round 6 signal**: V-05 (Signal 2). V-05 added the explicit chain completeness check as
  a Stage 5 entry condition. C-20 checks artifact files carry the field; C-28 checks Stage
  5 actively gates on confirming all three were written before synthesis proceeds.
- **Reduced from 2 pts to 1 pt in v8**: C-31 captures the richer contract-verification
  behavior. C-28 is now the 1-pt floor: did Stage 5 ENTRY CONDITIONS include an explicit
  displacement chain completeness gate at all. Unchanged in v9, v10, v11.

### C-29 -- Stage 5 EXIT SIGNAL Names Displacement Read Chain Closure

- **Weight**: aspirational (1 pt)
- **Category**: correctness
- **Text**: Stage 5 EXIT SIGNAL explicitly confirms that all three artifact Displacement
  reads were cited in evidence_summary, converting the campaign final EXIT SIGNAL from a
  simple stage-completion declaration into a chain-closure audit record.
- **Pass condition**: Stage 5 EXIT SIGNAL output contains an explicit named confirmation
  that all three artifact Displacement reads were consumed in evidence_summary (e.g., "All
  three artifact Displacement reads cited in evidence_summary." or equivalent). A Stage 5
  EXIT SIGNAL declaring synthesis_complete without naming the displacement read chain
  closure = FAIL. C-29 also requires C-25 to pass: a Stage 5 EXIT SIGNAL claiming chain
  closure while evidence_summary does not cite all three artifact reads = FAIL.
- **Round 6 signal**: V-05 (Signal 3). V-05 EXIT SIGNAL: "All three artifact Displacement
  reads cited in evidence_summary." Elevates EXIT SIGNAL to chain-closure audit record.
  Creates declaration (C-17) + output (C-25) + audit record (C-29) three-layer architecture.
- **Reduced from 2 pts to 1 pt in v8**: C-32 captures the richer named-provenance behavior.
  C-29 is now the 1-pt floor: did Stage 5 EXIT SIGNAL declare displacement read chain
  closure at all. Unchanged in v9, v10, v11.

### C-30 -- evidence_summary Instruction Mandates All Three Artifact Displacement Read Citations

- **Weight**: aspirational (1 pt)
- **Category**: depth
- **Text**: The Stage 5 evidence_summary template or governing instruction explicitly
  mandates citation of all three artifact Displacement reads as a structural requirement --
  not conditionally or by advisory suggestion -- creating an instruction-level mandate that
  makes the three-citation output (C-25) structurally enforced rather than emergent from
  synthesis quality.
- **Pass condition**: The Stage 5 evidence_summary instruction or template body contains an
  explicit mandatory requirement for citing all three artifact Displacement reads by artifact
  type, phrased as a non-conditional requirement (e.g., "must cite all three artifact
  Displacement reads: websearch, interview, prototype", "required: cite websearch Displacement
  read, interview Displacement read, prototype Displacement read", or equivalent mandatory
  language naming all three artifact types). A conditional instruction ("Cite artifact
  Displacement reads if present") = FAIL. A Stage 4-verdict-only instruction without any
  artifact read citation mandate = FAIL. The mandate must name all three artifact types or
  equivalent enumeration.
- **Round 7 signal**: V-01 passes C-27 but fails C-25 because evidence_summary mandates
  only "cite Stage 4 displacement verdict explicitly" -- no artifact reads. V-02 passes C-28
  but fails C-25 because evidence_summary says "Cite artifact Displacement reads if present"
  -- conditional, not required. V-03 passes both C-23 and C-25 because evidence_summary
  explicitly instructs all three artifact reads. C-25 checks the output; C-30 checks the
  instruction constraining the output is mandatory. Unchanged in v9, v10, v11.

### C-31 -- Stage 5 Entry Gate Cross-References ROLE A Displacement Read Contract

- **Weight**: aspirational (1 pt)
- **Category**: format
- **Text**: Stage 5 ENTRY CONDITIONS displacement chain completeness gate (required for
  C-28) explicitly names the ROLE A displacement_read_contract field as the pre-stage
  commitment being verified, converting the entry gate from an independent structural check
  into a contract-verification step.
- **Pass condition**: Stage 5 ENTRY CONDITIONS chain completeness gate explicitly
  cross-references ROLE A displacement_read_contract by field name -- e.g., "[ ] All three
  artifact Displacement read fields confirmed written [per ROLE A displacement_read_contract]"
  or equivalent statement naming the ROLE A contract field. An entry gate that verifies
  artifact Displacement reads without cross-referencing displacement_read_contract by name
  (passing C-28) = FAIL. If C-27 fails (no ROLE A displacement_read_contract committed),
  C-31 automatically fails -- the gate cannot cross-reference a contract that was not
  committed.
- **Round 7 signal**: No R7 variation showed C-27 and C-28 cross-wired. When both coexist,
  the optimal pattern explicitly names displacement_read_contract in the entry gate, making
  the gate a contract-verification step. C-28 checks the gate exists; C-31 checks the gate
  is explicitly traced to the ROLE A contract by field name. Unchanged in v9, v10, v11.

### C-32 -- Stage 5 EXIT SIGNAL Names Each Artifact Type Individually in Chain Closure

- **Weight**: aspirational (1 pt)
- **Category**: correctness
- **Text**: Stage 5 EXIT SIGNAL chain closure declaration (required for C-29) names each of
  the three artifact types individually (websearch, interview, prototype) in the chain
  closure statement, converting the EXIT SIGNAL from a count-based assertion to a
  named-provenance audit trail.
- **Pass condition**: Stage 5 EXIT SIGNAL chain closure statement explicitly names all three
  artifact types by role -- websearch, interview, and prototype -- within the chain closure
  declaration (e.g., "Displacement read chain closed: websearch, interview, prototype cited
  in evidence_summary." or "All three artifact Displacement reads confirmed -- websearch
  Displacement read, interview Displacement read, prototype Displacement read -- chain
  closed." or equivalent). A chain closure statement claiming "all three" without
  individually naming each artifact type (passing C-29) = FAIL. Requires C-29 to pass.
- **Round 7 signal**: V-03 EXIT SIGNAL names each artifact type individually. Converts the
  chain closure from count assertion to named-provenance record. C-29 checks chain closure
  declared; C-32 checks each artifact type is individually named. Unchanged in v9, v10, v11.

### C-33 -- Stage 5 EXIT SIGNAL Carries Terminal Closure Declaration

- **Weight**: aspirational (1 pt)
- **Category**: correctness
- **Text**: Stage 5 EXIT SIGNAL appends an explicit terminal closure declaration ("Chain
  closed." or registered equivalent) as a distinct final phrase following the named-artifact
  enumeration (C-32), converting the EXIT SIGNAL from a named-provenance list into a
  self-certifying closure record.
- **Pass condition**: Stage 5 EXIT SIGNAL contains the named-artifact enumeration satisfying
  C-32, and additionally ends with a distinct terminal closure assertion appearing after the
  enumeration as a separate phrase or sentence (e.g., "Chain closed." or "Displacement read
  chain: closed." or equivalent explicit self-certification). The terminal assertion must
  appear as a separate phrase, not as a prefix or embedded header to the enumeration.
  Named enumeration without a terminal closure assertion (passing C-32) = FAIL.
  Requires C-32 to pass.
- **Round 8 signal**: V-05 EXIT SIGNAL: "Displacement read chain closed: websearch
  Displacement read, interview Displacement read, prototype Displacement read -- all three
  cited in evidence_summary. Chain closed." V-03 EXIT SIGNAL (passes C-32): "Displacement
  read chain closed: websearch Displacement read, interview Displacement read, prototype
  Displacement read -- all three cited in evidence_summary." V-03 names each artifact
  (C-32) but carries no terminal closure assertion. V-05 appends "Chain closed." as a
  self-certifying final statement distinct from the enumeration. C-32 checks each artifact
  type is individually named; C-33 checks the additional terminal self-certification is
  present. C-35 checks the terminal form was pre-registered as a canonical source before
  Stage 5 executes. Unchanged in v11.

### C-34 -- evidence_summary Instruction Registers Omission Failure Label

- **Weight**: aspirational (1 pt)
- **Category**: correctness
- **Text**: The Stage 5 evidence_summary mandatory instruction (required for C-30) includes
  a canonical failure label for omission of any artifact Displacement read citation,
  extending the two-layer enforcement architecture (C-14) into the Stage 5 synthesis
  instruction layer.
- **Pass condition**: The evidence_summary instruction or template (satisfying C-30 with
  non-conditional mandatory language naming all three artifact types) contains an explicit
  failure label for omission -- e.g., "Omission of any artifact Displacement read = FAIL",
  "omission = FAIL", or equivalent canonical failure label registered within the instruction
  body. A mandatory instruction that names all three artifact types without a registered
  failure label for omission (passing C-30 without FAIL label) = FAIL.
  Requires C-30 to pass.
- **Round 8 signal**: V-02, V-04, V-05 C-30 PASS evidence: "Must cite all three artifact
  Displacement reads (mandatory -- not conditional): websearch..., interview..., prototype...
  Omission of any artifact Displacement read = FAIL." The "Omission = FAIL" failure label
  is present in all three C-30-passing variations. V-01 and V-03 fail C-30 (advisory
  language) and therefore cannot achieve C-34. C-30 checks the instruction is mandatory and
  names all three artifact types; C-34 checks the instruction also registers a canonical
  failure label for omission -- extending two-layer enforcement architecture (C-14) from the
  SESSION INVARIANTS registration layer into the Stage 5 synthesis instruction layer itself.
  C-36 further elevates C-34 by requiring SESSION INVARIANTS to register Invariant E
  (SYNTHESIS EVIDENCE MANDATE, SYNTHESIS-FAIL) as the canonical source for the omission
  failure label, with the evidence_summary instruction echoing Invariant E by name.
  Unchanged in v11.

### C-35 -- CAMPAIGN CLOSURE CANONICAL FORM Pre-Registered Before Roles Execute

- **Weight**: aspirational (1 pt)
- **Category**: correctness
- **Text**: The prompt pre-registers the Stage 5 EXIT SIGNAL terminal closure form as a
  named CAMPAIGN CLOSURE CANONICAL FORM block (or equivalent) before ROLE A and ROLE B
  initialize, and Stage 5 EXIT SIGNAL echoes this block by registered name before the
  named-artifact enumeration.
- **Pass condition**: A named CAMPAIGN CLOSURE CANONICAL FORM block (or equivalent
  pre-stage canonical form registration) appears before the first role initialization,
  establishing the canonical terminal form for the Stage 5 EXIT SIGNAL chain closure
  (e.g., the registered form is "Chain closed." or equivalent). Stage 5 EXIT SIGNAL
  explicitly echoes the registered canonical form by its block name (e.g., "Echoing
  registered CAMPAIGN CLOSURE CANONICAL FORM:") immediately before or as part of the
  named-artifact enumeration. C-33 present (terminal "Chain closed." assertion) without
  a pre-registered canonical source block = FAIL. Stage 5 EXIT SIGNAL appends terminal
  closure assertion without referencing the pre-registered block by name = FAIL.
  Requires C-33 to pass.
- **Round 9 signal**: V-01/V-04/V-05. Converts C-33 (terminal closure behavioral output
  pattern) into a bidirectional enforcement architecture: registered canonical source block
  before roles execute + Stage 5 verbatim echo by registered block name. Structural analog
  of C-14 (registered SESSION INVARIANTS label + inline enforcement echo) applied to the
  Stage 5 EXIT SIGNAL closure form. Distinguishes variations that pre-register the terminal
  form from those where it emerges only from Stage 5 output without a registered source.
  C-41 adds Stage 0 consistency verification against the pre-registered form; C-35 remains
  the 1-pt floor for pre-registration + Stage 5 echo. Unchanged in v11.

### C-36 -- SESSION INVARIANTS Registers Invariant E as SYNTHESIS EVIDENCE MANDATE

- **Weight**: aspirational (1 pt)
- **Category**: correctness
- **Text**: The SESSION INVARIANTS block registers a named Invariant E (SYNTHESIS EVIDENCE
  MANDATE) with canonical failure label SYNTHESIS-FAIL (or equivalent), and the Stage 5
  evidence_summary instruction explicitly echoes Invariant E by name, creating full
  two-layer enforcement for C-34.
- **Pass condition**: The SESSION INVARIANTS block contains a named Invariant E entry
  (e.g., "Invariant E: SYNTHESIS EVIDENCE MANDATE") with a canonical failure label of
  SYNTHESIS-FAIL (or registered equivalent). The Stage 5 evidence_summary instruction
  explicitly echoes Invariant E by name and failure label (e.g., "SESSION INVARIANT E
  active -- omission = SYNTHESIS-FAIL" or "(echoes SESSION INVARIANTS Invariant E
  registered failure label)"). C-34 present (omission failure label in evidence_summary
  instruction, satisfying C-34) without SESSION INVARIANTS Invariant E registration =
  FAIL. evidence_summary instruction carries omission failure label but does not echo
  SESSION INVARIANTS Invariant E by name = FAIL. Requires C-34 to pass.
- **Round 9 signal**: V-02/V-04/V-05. Elevates C-34 from an inline Stage 5 instruction
  pattern to a fully registered SESSION INVARIANTS row, creating the same registered-source
  + inline-echo architecture as C-14 (two-layer enforcement). The C-14 bidirectional
  architecture now spans all five SESSION INVARIANTS: D (FORMAT ERROR), C (ORDER ERROR /
  FAIL), A (DUAL-LOCK ERROR), B (DUAL-LOCK ERROR), E (SYNTHESIS-FAIL). C-18 checks any
  Invariant E registration exists (1-pt floor); C-36 checks it is specifically named as
  SYNTHESIS EVIDENCE MANDATE with the SYNTHESIS-FAIL failure label and echoed at
  evidence_summary by Invariant E name. C-39 checks that all five invariants are presented
  as a unified complete system in the standalone block; C-36 remains the 1-pt floor for
  Invariant E named registration. Unchanged in v11.

### C-37 -- Stage 0 EXIT SIGNAL Pre-Commits Stage 5 Closure Form and Synthesis Mandate

- **Weight**: aspirational (1 pt)
- **Category**: correctness
- **Text**: Stage 0 gate_open EXIT SIGNAL contains named forward-commitment fields for the
  Stage 5 terminal closure form (synthesis_closure_form) and synthesis omission mandate
  label (synthesis_mandate_label), and Stage 5 ENTRY CONDITIONS verify both fields by name.
- **Pass condition**: Stage 0 gate_open EXIT SIGNAL explicitly declares both
  synthesis_closure_form (e.g., `synthesis_closure_form: 'Chain closed.'`) and
  synthesis_mandate_label (e.g., `synthesis_mandate_label: 'Omission = FAIL'`) as labeled
  forward-commitment fields within the EXIT SIGNAL body. Stage 5 ENTRY CONDITIONS
  explicitly reference and verify both fields by their field names (e.g., "[ ] Verify
  synthesis_closure_form committed at Stage 0" and "[ ] Verify synthesis_mandate_label
  committed at Stage 0"). A Stage 0 EXIT SIGNAL without both forward-commitment fields =
  FAIL. Stage 5 ENTRY CONDITIONS that do not verify Stage 0 commitment fields by name =
  FAIL.
- **Round 9 signal**: V-03/V-05. Creates a Stage 0 to Stage 5 structural pre-commitment
  chain parallel to the ROLE A displacement_read_contract (C-27) to Stage 5 entry
  verification (C-31) chain. Stage 0 now commits not only to scout artifact delivery
  (gate_s) but also to the terminal closure assertion form (C-33) and synthesis omission
  failure label (C-34) that Stage 5 must honor. Stage 5 ENTRY CONDITIONS verify both Stage
  0 commitments by field name, mirroring the C-31 contract-verification pattern. C-27/C-31
  creates the ROLE A pre-stage commitment chain; C-37 creates a parallel Stage 0 commitment
  chain for the closure and mandate properties. C-40 adds ROLE A verification of Stage 0
  fields, completing the three-anchor chain; C-37 remains the 1-pt floor for Stage 0
  forward-commitment + Stage 5 verification. Unchanged in v11.

### C-38 -- Block 3 Dual-Lock Step Annotations Echo DUAL-LOCK ERROR Verbatim

- **Weight**: aspirational (1 pt)
- **Category**: correctness
- **Text**: Each Block 3 adversarial review lock step annotation echoes "DUAL-LOCK ERROR"
  as the verbatim registered SESSION INVARIANTS label at the enforcement point, with an
  explicit parenthetical identifying the SESSION INVARIANT being echoed.
- **Pass condition**: Block 3 lock step annotations contain both (a) a lock step for
  bypassing adversarial review using the verbatim label "DUAL-LOCK ERROR" with a
  parenthetical referencing SESSION INVARIANT A (e.g., "Bypassing adversarial review =
  DUAL-LOCK ERROR. (echoes registered SESSION INVARIANT A label)") and (b) a lock step
  for softening or overriding the confidence cap using the verbatim label "DUAL-LOCK ERROR"
  with a parenthetical referencing SESSION INVARIANT B (e.g., "Softening or overriding cap
  = DUAL-LOCK ERROR. (echoes registered SESSION INVARIANT B label)"). Any Block 3 lock
  step using a divergent label (e.g., "BLOCKED", "dual_lock_fired", "co_activation") instead
  of the verbatim registered "DUAL-LOCK ERROR" label = FAIL. Both lock steps must carry
  the verbatim label with SESSION INVARIANT identification. Requires C-14 to pass.
- **Round 9 signal**: V-05 only. Resolves the R8 universal C-14 partial: across all R8
  variations, Block 3 inline annotations used "dual_lock_fired / BLOCKED" rather than the
  registered "DUAL-LOCK ERROR" label, causing C-14 to score partial for all R8 variations.
  V-05 in R9 echoes "DUAL-LOCK ERROR" verbatim at each Block 3 lock step with an explicit
  "(echoes registered SESSION INVARIANT A/B label)" parenthetical, completing the
  bidirectional label enforcement pattern for SESSION INVARIANTS A and B. C-14 checks
  bidirectional enforcement architecture exists for any invariant (1-pt floor); C-38 checks
  Block 3 dual-lock annotations carry the verbatim registered label at each lock step with
  SESSION INVARIANT identification. Together with C-36 (Invariant E: SYNTHESIS-FAIL), C-38
  completes the registered-label coverage for all five SESSION INVARIANTS. Unchanged in v11.

### C-39 -- SESSION INVARIANTS Block Declares All Five Invariants as Unified Complete System

- **Weight**: aspirational (1 pt)
- **Category**: format
- **Text**: The SESSION INVARIANTS standalone block explicitly presents all five active
  SESSION INVARIANTS (A, B, C, D, E) as a unified complete system -- each with its
  canonical failure label and governing stage-scope annotation -- rather than satisfying
  the A-D floor (C-12) and Invariant E (C-36) through incremental per-criterion additions.
- **Pass condition**: The SESSION INVARIANTS TABLE or LIST contains exactly five enumerated
  entries: Invariant A (DUAL-LOCK ERROR), Invariant B (DUAL-LOCK ERROR), Invariant C
  (ORDER ERROR or registered equivalent), Invariant D (FORMAT ERROR), and Invariant E
  (SYNTHESIS-FAIL or SYNTHESIS EVIDENCE MANDATE). Each entry must carry (a) its canonical
  failure label and (b) its governing stage-scope annotation (i.e., which stages the
  invariant is active in). A SESSION INVARIANTS block that enumerates only A-D (passing
  C-12) = FAIL. Invariant E present with SYNTHESIS-FAIL label (passing C-36) but without
  a governing stage-scope annotation = FAIL. Any invariant row missing either its canonical
  failure label or its stage-scope annotation = FAIL. Requires C-12 and C-36 to pass.
- **Round 10 signal**: All R10 variations. C-12 (standalone block, A-D minimum) and C-36
  (Invariant E as SYNTHESIS EVIDENCE MANDATE with SYNTHESIS-FAIL) are necessary but not
  sufficient for C-39. C-39 checks that the standalone block presents all five invariants
  in a single unified enumeration with complete structural entries for each -- the total
  governance system declared once, with stage-scope coverage showing when each invariant
  activates. Distinguishes variations that build the SESSION INVARIANTS block as a complete
  unified governance declaration from those where completeness emerges incrementally through
  the criteria.

### C-40 -- ROLE A Initialization Verifies Stage 0 Forward-Commitment Fields by Name

- **Weight**: aspirational (1 pt)
- **Category**: correctness
- **Text**: ROLE A pre-stage initialization explicitly reads and records both Stage 0
  forward-commitment fields (synthesis_closure_form and synthesis_mandate_label) by field
  name, creating a three-anchor verification chain: Stage 0 commit -> ROLE A read ->
  Stage 5 verify -- parallel to the C-27 (ROLE A contract) -> C-31 (Stage 5 gate) chain.
- **Pass condition**: ROLE A initialization output (appearing before Stage 0 gate_open)
  contains explicit read/acknowledgment of both synthesis_closure_form and
  synthesis_mandate_label by field name, with a statement tracing both fields to Stage 0
  EXIT SIGNAL as their committed source (e.g., "synthesis_closure_form read from Stage 0
  EXIT SIGNAL: 'Chain closed.' -- confirmed." and "synthesis_mandate_label read from Stage
  0 EXIT SIGNAL: 'Omission = FAIL' -- confirmed." or equivalent). ROLE A initialization
  that carries incumbent_anchor_read + displacement_read_contract (passing C-27) but does
  not additionally read and record synthesis_closure_form + synthesis_mandate_label from
  Stage 0 by field name = FAIL. ROLE A acknowledgment of Stage 0 fields without naming
  them by their field names = FAIL. Requires C-37 and C-27 to pass.
- **Round 10 signal**: R10 V-02/V-04/V-05. C-37 creates the Stage 0 forward-commitment;
  C-27 creates the ROLE A two-field initialization contract; C-40 connects them: ROLE A
  reads Stage 0 synthesis commitments by name, forming the middle anchor of the
  Stage 0 -> ROLE A -> Stage 5 chain. C-31 checks Stage 5 cross-references the ROLE A
  displacement_read_contract by field name (the Stage 5 end of the C-27 chain); C-40
  checks ROLE A cross-references Stage 0 synthesis commitments by field name (the ROLE A
  end of the C-37 chain). Together C-27/C-31/C-37/C-40 form a fully cross-wired
  pre-commitment verification spine across all three structural anchors.

### C-41 -- CAMPAIGN CLOSURE CANONICAL FORM Consistency Confirmed at Stage 0 EXIT SIGNAL

- **Weight**: aspirational (1 pt)
- **Category**: correctness
- **Text**: Stage 0 gate_open EXIT SIGNAL explicitly confirms that synthesis_closure_form
  committed at Stage 0 matches the pre-registered CAMPAIGN CLOSURE CANONICAL FORM by
  naming both, closing the registration-to-commitment consistency loop at Stage 0 rather
  than deferring consistency verification to Stage 5.
- **Pass condition**: Stage 0 gate_open EXIT SIGNAL contains an explicit consistency
  confirmation statement that (a) names the pre-registered CAMPAIGN CLOSURE CANONICAL FORM
  block by its registered name and (b) asserts that synthesis_closure_form committed at
  Stage 0 matches the registered canonical form (e.g., "synthesis_closure_form: 'Chain
  closed.' (matches registered CAMPAIGN CLOSURE CANONICAL FORM)" or "synthesis_closure_form
  committed consistent with CAMPAIGN CLOSURE CANONICAL FORM registration" or equivalent).
  A Stage 0 EXIT SIGNAL that carries synthesis_closure_form as a forward-commitment field
  (passing C-37) without an explicit consistency assertion naming the CAMPAIGN CLOSURE
  CANONICAL FORM block = FAIL. Consistency assertion present but not naming the
  CAMPAIGN CLOSURE CANONICAL FORM block by its registered name = FAIL.
  Requires C-35 and C-37 to pass.
- **Round 10 signal**: R10 V-03/V-05. C-35 pre-registers the CAMPAIGN CLOSURE CANONICAL
  FORM before roles execute; C-37 commits synthesis_closure_form at Stage 0 EXIT SIGNAL;
  C-41 verifies the two are consistent at Stage 0 time. Without C-41, the registration
  (C-35) and the Stage 0 commitment (C-37) are structurally independent -- a variation
  could pre-register "Chain closed." (C-35) but commit a different synthesis_closure_form
  at Stage 0 (C-37) without creating a divergence flag. C-41 closes this gap by requiring
  Stage 0 EXIT SIGNAL to explicitly assert consistency between the pre-registered canonical
  form and the Stage 0 forward commitment, naming both by their registered identifiers.
  Converts the Stage 0 EXIT SIGNAL from a commitment record into a registration-consistency
  verification step.

---

## Scoring Summary

| ID   | Text (short)                                                    | Weight       | Pts | Category    |
|------|-----------------------------------------------------------------|--------------|-----|-------------|
| C-01 | All 6 EXIT SIGNALs declared in order                           | essential    |  10 | correctness |
| C-02 | All 6 artifacts written + confirmed                            | essential    |  10 | behavior    |
| C-03 | Session Invariant D verbatim at S2/3/4                         | essential    |  10 | correctness |
| C-04 | Synthesis verdict + confidence present                         | essential    |  10 | correctness |
| C-05 | Null tally chain cross-checked                                 | essential    |  10 | correctness |
| C-06 | Gate S scout loader executes                                   | recommended  |   8 | coverage    |
| C-07 | Handoff table 11 fields + derivations                          | recommended  |   8 | format      |
| C-08 | Counter-hypothesis resolved with verdict                       | recommended  |   8 | depth       |
| C-09 | Atomic dual-lock fires when warranted                          | aspirational |   1 | behavior    |
| C-10 | Incumbent displacement framing throughout                      | aspirational |   1 | depth       |
| C-11 | Invariant enforcement language mechanical                      | aspirational |   1 | correctness |
| C-12 | SESSION INVARIANTS in standalone block                         | aspirational |   1 | format      |
| C-13 | Stage 5 synthesis fields isolated                              | aspirational |   1 | format      |
| C-14 | Two-layer enforcement architecture                             | aspirational |   1 | correctness |
| C-15 | CAMPAIGN OPEN pre-registers displacement                       | aspirational |   1 | format      |
| C-16 | Per-stage Displacement read fields                             | aspirational |   1 | depth       |
| C-17 | SYNTHESIS DECLARATIONS explicit prohibition                    | aspirational |   1 | format      |
| C-18 | Invariant E checkpoint at handoff schema                       | aspirational |   1 | format      |
| C-19 | Invariant D template binding to CAMPAIGN OPEN                  | aspirational |   1 | correctness |
| C-20 | Artifact files carry Displacement read field                   | aspirational |   1 | depth       |
| C-21 | CAMPAIGN OPEN INCUMBENT ANCHOR + prohibition                   | aspirational |   1 | format      |
| C-22 | Invariant D binding note with literal-use label                | aspirational |   1 | correctness |
| C-23 | Stage 5 cites artifact Displacement read value                 | aspirational |   1 | depth       |
| C-24 | ROLE A confirms INCUMBENT ANCHOR binding pre-S0                | aspirational |   1 | correctness |
| C-25 | Stage 5 cites all three artifact Displacement reads            | aspirational |   1 | depth       |
| C-26 | Invariant D binding note names INCUMBENT ANCHOR                | aspirational |   1 | correctness |
| C-27 | ROLE A initialization commits displacement evidence chain      | aspirational |   1 | correctness |
| C-28 | Stage 5 entry conditions gate on chain completeness            | aspirational |   1 | format      |
| C-29 | Stage 5 EXIT SIGNAL names displacement read chain closure      | aspirational |   1 | correctness |
| C-30 | evidence_summary instruction mandates all three reads          | aspirational |   1 | depth       |
| C-31 | Stage 5 entry gate cross-references ROLE A contract            | aspirational |   1 | format      |
| C-32 | Stage 5 EXIT SIGNAL names artifact types individually          | aspirational |   1 | correctness |
| C-33 | Stage 5 EXIT SIGNAL carries terminal closure declaration       | aspirational |   1 | correctness |
| C-34 | evidence_summary instruction registers omission label          | aspirational |   1 | correctness |
| C-35 | CAMPAIGN CLOSURE CANONICAL FORM pre-registered                 | aspirational |   1 | correctness |
| C-36 | SESSION INVARIANTS Invariant E as SYNTHESIS EVIDENCE MANDATE   | aspirational |   1 | correctness |
| C-37 | Stage 0 EXIT SIGNAL pre-commits Stage 5 closure form + mandate | aspirational |   1 | correctness |
| C-38 | Block 3 dual-lock annotations echo DUAL-LOCK ERROR verbatim    | aspirational |   1 | correctness |
| C-39 | SESSION INVARIANTS all five invariants as unified system       | aspirational |   1 | format      |
| C-40 | ROLE A verifies Stage 0 forward-commitment fields by name      | aspirational |   1 | correctness |
| C-41 | CAMPAIGN CLOSURE CANONICAL FORM consistency at Stage 0         | aspirational |   1 | correctness |
|      | **Total**                                                       |              | 107 |             |

**Essential** (50 pts): C-01 through C-05, 10 pts each.
**Recommended** (24 pts): C-06 through C-08, 8 pts each.
**Aspirational** (33 pts): C-09 (1) + C-10 (1) + C-11 (1) + C-12 (1) + C-13 (1)
  + C-14 (1) + C-15 (1) + C-16 (1) + C-17 (1) + C-18 (1) + C-19 (1) + C-20 (1)
  + C-21 (1) + C-22 (1) + C-23 (1) + C-24 (1) + C-25 (1) + C-26 (1)
  + C-27 (1) + C-28 (1) + C-29 (1) + C-30 (1) + C-31 (1) + C-32 (1)
  + C-33 (1) + C-34 (1) + C-35 (1) + C-36 (1) + C-37 (1) + C-38 (1)
  + C-39 (1) + C-40 (1) + C-41 (1) = 33 pts.

**Formula**: sum of individual criterion scores (PASS = full, PARTIAL = half rounded down, FAIL = 0).
**Golden**: all 5 essential PASS + composite >= 80.

---

## Composite Scores (R10 under v11)

| Variation | Essential | Recommended | Aspirational | Total |
|-----------|-----------|-------------|--------------|-------|
| V-01 | 50 | 24 | 30 | **104** |
| V-02 | 50 | 24 | 30 | **104** |
| V-03 | 50 | 24 | 30 | **104** |
| V-04 | 50 | 24 | 31 | **105** |
| V-05 | 50 | 24 | 32 | **106** |

**All five pass the golden threshold (all essential PASS + composite >= 80).**

Score basis: R10 v10 baseline = 103 for all five variations (inherited from V-05 R9).
C-39 adds 1 pt for all five R10 variations. C-40 adds 1 pt for V-02/V-04/V-05.
C-41 adds 1 pt for V-03/V-05. Aspirational pool grows from 30 to 33 pts (max);
total grows from 104 to 107.

Note on C-10: universal fail persists into R10. Pass condition requires evidence_summary
to cite "Stage 4 displacement verdict: [Yes/No/Pending]" as an explicit labeled field.
The current evidence_summary instruction mandates all three artifact Displacement reads
(C-25/C-30) and Stage 5 EXIT SIGNAL names each artifact type (C-32) -- but neither the
evidence_summary template nor its governing instruction names s4_displacement_verdict as
a required distinct labeled citation. This remains the open fail floor across all
variations.

---

## Ranking

1. **V-05** -- 106/107, three new patterns (highest structural density; full three-anchor
   chain: five-invariant unified SESSION INVARIANTS + Stage 0 verified at ROLE A +
   CLOSURE CANONICAL FORM consistency closed at Stage 0)
2. **V-04** -- 105/107, two new patterns (C-39 unified five-invariant block +
   C-40 ROLE A verifies Stage 0 fields)
3. **V-01** -- 104/107, one pattern (C-39 unified five-invariant SESSION INVARIANTS)
4. **V-02** -- 104/107, one pattern (C-40 Stage 0 commitment verified at ROLE A)
5. **V-03** -- 104/107, one pattern (C-41 CLOSURE CANONICAL FORM consistency at Stage 0)

V-01/V-02/V-03 are peer-ranked at 104/107. V-01 ranks first among peers because C-39
(unified five-invariant block) completes the registration architecture for all governance
invariants simultaneously; V-02 and V-03 extend the pre-commitment chain architecture
which is already partially covered by C-27/C-31/C-37.

---

## Excellence Signals -- Candidates for v12 C-42+

No new excellence signal patterns emerged from R10 beyond the three codified in v11
(C-39 through C-41). V-05 converges all three patterns at 106/107. Candidate axes for
v12 include:

- **C-10 resolution -- s4_displacement_verdict as labeled field in evidence_summary**:
  C-10 has been the universal fail since v6. The pass condition requires a labeled citation
  of "Stage 4 displacement verdict: [Yes/No/Pending]" as a distinct extractable field in
  evidence_summary. A variation that adds s4_displacement_verdict as a labeled key-value
  field alongside the three artifact Displacement read citations would close this gap.
  Note: C-10 is a 1-pt aspirational criterion with a narrow behavioral gap. A new C-42
  criterion may be premature; the gap may be closed by updating the evidence_summary
  instruction in the prompt without creating a new rubric criterion.

- **ROLE A four-field unified initialization block**: C-40 adds synthesis_closure_form_read
  and synthesis_mandate_label_read to the ROLE A initialization block (alongside
  incumbent_anchor_read and displacement_read_contract from C-27). A variation that presents
  all four ROLE A pre-stage fields as a unified named initialization checklist
  (e.g., "ROLE A PRE-STAGE INITIALIZATION: four-field checklist complete") would create
  a single structural anchor for all pre-stage commitments -- a stronger architectural
  statement than four fields in a block.

- **Stage 5 ENTRY CONDITIONS complete upstream verification matrix**: Stage 5 ENTRY
  CONDITIONS currently gate on displacement_read_contract (C-31) and Stage 0
  synthesis_closure_form + synthesis_mandate_label (C-37). A variation that presents Stage 5
  ENTRY CONDITIONS as an explicit upstream verification matrix naming all pre-stage
  commitments by anchor (ROLE A four-field block + Stage 0 EXIT SIGNAL fields) would
  convert Stage 5 entry from a list of gates into a contract-verification audit against
  all three structural anchors.

```json
{"top_score": 106, "max_score": 107, "all_essential_pass": true, "new_criteria": ["C-39: SESSION INVARIANTS all five invariants as unified complete system with canonical labels and stage-scope annotations -- completes unified governance declaration (all R10 variations)", "C-40: ROLE A initialization reads Stage 0 synthesis_closure_form + synthesis_mandate_label by field name -- creates three-anchor Stage 0 -> ROLE A -> Stage 5 verification chain (R10 V-02/V-04/V-05)", "C-41: Stage 0 EXIT SIGNAL confirms synthesis_closure_form matches CAMPAIGN CLOSURE CANONICAL FORM by naming both -- closes registration-to-commitment loop at Stage 0 (R10 V-03/V-05)"]}
```

---

## Version Notes

### v11 (2026-03-17)

**Three new aspirational criteria from R10 excellence signals**:

- **C-39 (1 pt)** -- SESSION INVARIANTS block declares all five invariants as unified
  complete system. Signal source: all R10 variations. C-12 (standalone block, A-D minimum)
  and C-36 (Invariant E as SYNTHESIS EVIDENCE MANDATE with SYNTHESIS-FAIL) are necessary
  but not sufficient. C-39 requires the standalone block to present all five invariants
  (A/B/C/D/E) as a unified complete enumeration, each carrying both its canonical failure
  label and its governing stage-scope annotation. Distinguishes variations that declare
  the complete governance system once from those where completeness is assembled through
  incremental per-criterion additions.

- **C-40 (1 pt)** -- ROLE A initialization verifies Stage 0 forward-commitment fields by
  name. Signal source: R10 V-02/V-04/V-05. C-37 creates the Stage 0 forward-commitment
  (synthesis_closure_form + synthesis_mandate_label); C-27 creates the ROLE A two-field
  initialization contract (incumbent_anchor_read + displacement_read_contract). C-40
  connects them: ROLE A initialization must explicitly read and record both Stage 0
  synthesis commitment fields by name, creating the middle anchor of the
  Stage 0 -> ROLE A -> Stage 5 chain. Structural analog of C-31 (Stage 5 cross-references
  ROLE A contract by field name) applied to the Stage 0 -> ROLE A direction. Together with
  C-27/C-31/C-37/C-40, forms a fully cross-wired pre-commitment verification spine.

- **C-41 (1 pt)** -- CAMPAIGN CLOSURE CANONICAL FORM consistency confirmed at Stage 0
  EXIT SIGNAL. Signal source: R10 V-03/V-05. C-35 pre-registers the CAMPAIGN CLOSURE
  CANONICAL FORM; C-37 commits synthesis_closure_form at Stage 0 EXIT SIGNAL. C-41 closes
  the gap between them: Stage 0 EXIT SIGNAL must explicitly assert that synthesis_closure_form
  is consistent with the pre-registered CAMPAIGN CLOSURE CANONICAL FORM, naming both.
  Without C-41, pre-registration (C-35) and Stage 0 commitment (C-37) are structurally
  independent and could diverge silently. C-41 converts Stage 0 EXIT SIGNAL from a
  commitment record into a registration-consistency verification step.

### v10 (2026-03-16)

**Four new aspirational criteria from R9 excellence signals**:

- **C-35 (1 pt)** -- CAMPAIGN CLOSURE CANONICAL FORM pre-registered before roles execute.
  Signal source: V-01/V-04/V-05 (R9). Converts C-33 (terminal "Chain closed." assertion)
  from a behavioral output pattern into a bidirectional enforcement architecture: a named
  CAMPAIGN CLOSURE CANONICAL FORM block pre-registered before any role initialization, with
  Stage 5 EXIT SIGNAL echoing the block by registered name. Structural analog of C-14
  (SESSION INVARIANTS registered label + inline echo) applied to the Stage 5 terminal
  closure form. C-33 checks the terminal assertion is present; C-35 checks the canonical
  form was pre-registered and Stage 5 echoes it by name.

- **C-36 (1 pt)** -- SESSION INVARIANTS registers Invariant E as SYNTHESIS EVIDENCE MANDATE.
  Signal source: V-02/V-04/V-05 (R9). Elevates C-34 (omission failure label in
  evidence_summary instruction) from an inline Stage 5 instruction to a named SESSION
  INVARIANTS row: "Invariant E: SYNTHESIS EVIDENCE MANDATE, failure label SYNTHESIS-FAIL."
  evidence_summary instruction echoes Invariant E by name with the registered SYNTHESIS-FAIL
  label. Completes the C-14 two-layer enforcement architecture across all five SESSION
  INVARIANTS (D=FORMAT ERROR, C=ORDER ERROR/FAIL, A=DUAL-LOCK ERROR, B=DUAL-LOCK ERROR,
  E=SYNTHESIS-FAIL). C-18 checks any Invariant E registration (1-pt floor); C-36 checks it
  is named as SYNTHESIS EVIDENCE MANDATE with SYNTHESIS-FAIL echoed at evidence_summary.

- **C-37 (1 pt)** -- Stage 0 EXIT SIGNAL pre-commits Stage 5 closure form and synthesis
  mandate. Signal source: V-03/V-05 (R9). Stage 0 gate_open EXIT SIGNAL names both
  synthesis_closure_form: 'Chain closed.' and synthesis_mandate_label: 'Omission = FAIL' as
  explicit forward-commitment fields. Stage 5 ENTRY CONDITIONS verify both by field name.
  Creates a Stage 0 to Stage 5 structural pre-commitment chain parallel to the ROLE A
  displacement_read_contract (C-27) to Stage 5 entry verification (C-31) chain. C-31 checks
  the contract-verification pattern for ROLE A; C-37 checks the forward-commitment pattern
  for Stage 0.

- **C-38 (1 pt)** -- Block 3 dual-lock step annotations echo DUAL-LOCK ERROR verbatim.
  Signal source: V-05 only (R9). Resolves the R8 universal C-14 partial: all R8 variations
  used "dual_lock_fired / BLOCKED" at Block 3 lock steps rather than the registered
  "DUAL-LOCK ERROR" label. V-05 in R9 echoes "DUAL-LOCK ERROR" verbatim at each of the two
  lock steps with explicit "(echoes registered SESSION INVARIANT A/B label)" parentheticals.
  Completes bidirectional label enforcement for SESSION INVARIANTS A and B. C-14 checks
  bidirectional architecture exists for any invariant (1-pt floor); C-38 checks Block 3
  dual-lock annotations carry the verbatim registered label at each lock step with SESSION
  INVARIANT identification.
