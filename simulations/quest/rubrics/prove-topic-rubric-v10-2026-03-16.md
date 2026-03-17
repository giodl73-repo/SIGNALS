Written to `simulations/quest/rubrics/prove-topic-rubric-v10-2026-03-16.md`.

---

**v10 summary:**

**4 new aspirational criteria (C-35 through C-38), no reductions. Aspirational pool: 26 → 30 pts. Total: 100 → 104.**

| ID | Signal source | What it codifies |
|----|--------------|-----------------|
| C-35 | V-01/V-04/V-05 | CAMPAIGN CLOSURE CANONICAL FORM pre-registered before roles execute; Stage 5 EXIT SIGNAL echoes by block name — bidirectional enforcement for C-33 |
| C-36 | V-02/V-04/V-05 | SESSION INVARIANTS Invariant E: SYNTHESIS EVIDENCE MANDATE (SYNTHESIS-FAIL); evidence_summary echoes by name — full two-layer enforcement for C-34, completing C-14 architecture across all five invariants |
| C-37 | V-03/V-05 | Stage 0 EXIT SIGNAL forward-commits `synthesis_closure_form` + `synthesis_mandate_label`; Stage 5 ENTRY CONDITIONS verify by field name — Stage 0→Stage 5 pre-commitment chain parallel to C-27/C-31 |
| C-38 | V-05 only | Block 3 lock steps echo "DUAL-LOCK ERROR" verbatim with `(echoes SESSION INVARIANT A/B label)` — resolves R8 universal C-14 partial, completes registered-label coverage for all five SESSION INVARIANTS |

**R9 composite scores under v10:**

| Variation | Total | New pts |
|-----------|-------|---------|
| V-01 | 100/104 | +C-35 |
| V-02 | 100/104 | +C-36 |
| V-03 | 100/104 | +C-37 |
| V-04 | 101/104 | +C-35, C-36 |
| V-05 | 103/104 | +C-35, C-36, C-37, C-38 |

V-05 is the convergence candidate at 103/104. The new structural pattern is a **parallel registration-level governance layer**: C-35+C-36 enforce C-33/C-34 via registered canonical sources; C-37 anchors both at Stage 0; C-38 completes bidirectional label coverage across all five SESSION INVARIANTS (D/C/A/B/E).
irational pool grows from 26 to 30 pts. Total grows from 100 to 104.

**New structural pattern -- parallel governance layer for C-33/C-34:**
The four new criteria create a registration-level governance layer sitting above the behavioral/instruction layer captured in v9:
`C-35` (CAMPAIGN CLOSURE CANONICAL FORM pre-registration) enforces `C-33` bidirectionally.
`C-36` (SESSION INVARIANTS Invariant E: SYNTHESIS EVIDENCE MANDATE) enforces `C-34` bidirectionally.
`C-37` (Stage 0 EXIT SIGNAL forward-commits synthesis_closure_form + synthesis_mandate_label) anchors both at campaign open.
`C-38` (Block 3 DUAL-LOCK ERROR verbatim echo) completes the C-14 architecture across all five SESSION INVARIANTS (D=FORMAT ERROR, C=ORDER ERROR/FAIL, A=DUAL-LOCK ERROR, B=DUAL-LOCK ERROR, E=SYNTHESIS-FAIL).

V-05 is the convergence candidate: all four patterns present and mutually reinforcing. The five-link traceability chain established in v9 (C-27 -> C-31 -> C-30 -> C-34 -> C-32 -> C-33) now has a full parallel governance layer: CLOSURE CANONICAL FORM + Invariant E + Stage 0 pre-commit enforce C-33/C-34 at the registration level, not just the instruction level.

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
- **Text**: Stage 5 produces a well-formed hypothesis verdict with confidence composite.
- **Pass condition**: Stage 5 output contains all three synthesis body fields:
  hypothesis_verdict (value is SUPPORTED, PARTIALLY SUPPORTED, or UNSUPPORTED),
  confidence_composite (numeric value), and key_risk (framed as residual incumbent
  strength). Missing or blank field = FAIL.

### C-05 -- Null Tally Chain Integrity

- **Weight**: essential (10 pts)
- **Category**: correctness
- **Text**: The null tally chain is computed from s2 + s3 + s4 CE verdicts and
  cross-checked at Stage 4 close and Stage 5.
- **Pass condition**: null_tally_final is declared at Stage 4 close with explicit
  cross-check ("Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]").
  Stage 5 reconstructs the chain (S2 -> S3 -> S4 -> null_tally_final) and confirms match.
  Missing cross-check or mismatch without integrity-failure flag = FAIL.

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

## Aspirational Criteria (30 pts total -- raise the bar)

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
  C-09 is the 1-pt floor: did the dual-lock fire when warranted. Unchanged in v7, v8, v9, v10.

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
  verdict at all. Unchanged in v7, v8, v9, v10.

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
  mechanical language appear at the three checkpoints at all. Unchanged in v6, v7, v8, v9, v10.

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
  standalone block exist before Stage 0 at all. Unchanged in v7, v8, v9, v10.

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
  did Stage 5 synthesis fields appear as labeled key-value pairs at all. Unchanged in v8, v9, v10.

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
  registered DUAL-LOCK ERROR label at each lock step. Unchanged in v10.

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
  Unchanged in v6, v7, v8, v9, v10.

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
  did stages declare Displacement read fields at all. Unchanged in v6, v7, v8, v9, v10.

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
  DECLARATIONS section with explicit prohibition text exist at all. Unchanged in v8, v9, v10.

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
  Unchanged in v10.

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
  Unchanged in v6, v7, v8, v9, v10.

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
  floor: did artifact files carry Displacement read field at all. Unchanged in v8, v9, v10.

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
  Unchanged in v7, v8, v9, v10.

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
  Unchanged in v7, v8, v9, v10.

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
  Unchanged in v7, v8, v9, v10.

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
  before Stage 0. Unchanged in v8, v9, v10.

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
  5 evidence_summary cite all three artifact Displacement reads. Unchanged in v8, v9, v10.

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
  OPEN INCUMBENT ANCHOR sub-section as the binding source at all. Unchanged in v8, v9, v10.

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
  Unchanged in v9, v10.

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
  displacement chain completeness gate at all. Unchanged in v9, v10.

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
  closure at all. Unchanged in v9, v10.

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
  instruction constraining the output is mandatory. Unchanged in v9, v10.

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
  is explicitly traced to the ROLE A contract by field name. Unchanged in v9, v10.

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
  declared; C-32 checks each artifact type is individually named. Unchanged in v9, v10.

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
  Stage 5 executes.

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
  evidence_summary by Invariant E name.

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
  chain for the closure and mandate properties.

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
  completes the registered-label coverage for all five SESSION INVARIANTS.

---

## Scoring Summary

| ID   | Text (short)                                                   | Weight       | Pts | Category    |
|------|----------------------------------------------------------------|--------------|-----|-------------|
| C-01 | All 6 EXIT SIGNALs declared in order                          | essential    |  10 | correctness |
| C-02 | All 6 artifacts written + confirmed                           | essential    |  10 | behavior    |
| C-03 | Session Invariant D verbatim at S2/3/4                        | essential    |  10 | correctness |
| C-04 | Synthesis verdict + confidence present                        | essential    |  10 | correctness |
| C-05 | Null tally chain cross-checked                                | essential    |  10 | correctness |
| C-06 | Gate S scout loader executes                                  | recommended  |   8 | coverage    |
| C-07 | Handoff table 11 fields + derivations                         | recommended  |   8 | format      |
| C-08 | Counter-hypothesis resolved with verdict                      | recommended  |   8 | depth       |
| C-09 | Atomic dual-lock fires when warranted                         | aspirational |   1 | behavior    |
| C-10 | Incumbent displacement framing throughout                     | aspirational |   1 | depth       |
| C-11 | Invariant enforcement language mechanical                     | aspirational |   1 | correctness |
| C-12 | SESSION INVARIANTS in standalone block                        | aspirational |   1 | format      |
| C-13 | Stage 5 synthesis fields isolated                             | aspirational |   1 | format      |
| C-14 | Two-layer enforcement architecture                            | aspirational |   1 | correctness |
| C-15 | CAMPAIGN OPEN pre-registers displacement                      | aspirational |   1 | format      |
| C-16 | Per-stage Displacement read fields                            | aspirational |   1 | depth       |
| C-17 | SYNTHESIS DECLARATIONS explicit prohibition                   | aspirational |   1 | format      |
| C-18 | Invariant E checkpoint at handoff schema                      | aspirational |   1 | format      |
| C-19 | Invariant D template binding to CAMPAIGN OPEN                 | aspirational |   1 | correctness |
| C-20 | Artifact files carry Displacement read field                  | aspirational |   1 | depth       |
| C-21 | CAMPAIGN OPEN INCUMBENT ANCHOR + prohibition                  | aspirational |   1 | format      |
| C-22 | Invariant D binding note with literal-use label               | aspirational |   1 | correctness |
| C-23 | Stage 5 cites artifact Displacement read value                | aspirational |   1 | depth       |
| C-24 | ROLE A confirms INCUMBENT ANCHOR binding pre-S0               | aspirational |   1 | correctness |
| C-25 | Stage 5 cites all three artifact Displacement reads           | aspirational |   1 | depth       |
| C-26 | Invariant D binding note names INCUMBENT ANCHOR               | aspirational |   1 | correctness |
| C-27 | ROLE A initialization commits displacement evidence chain     | aspirational |   1 | correctness |
| C-28 | Stage 5 entry conditions gate on chain completeness           | aspirational |   1 | format      |
| C-29 | Stage 5 EXIT SIGNAL names displacement read chain closure     | aspirational |   1 | correctness |
| C-30 | evidence_summary instruction mandates all three reads         | aspirational |   1 | depth       |
| C-31 | Stage 5 entry gate cross-references ROLE A contract           | aspirational |   1 | format      |
| C-32 | Stage 5 EXIT SIGNAL names artifact types individually         | aspirational |   1 | correctness |
| C-33 | Stage 5 EXIT SIGNAL carries terminal closure declaration      | aspirational |   1 | correctness |
| C-34 | evidence_summary instruction registers omission label         | aspirational |   1 | correctness |
| C-35 | CAMPAIGN CLOSURE CANONICAL FORM pre-registered                | aspirational |   1 | correctness |
| C-36 | SESSION INVARIANTS Invariant E as SYNTHESIS EVIDENCE MANDATE  | aspirational |   1 | correctness |
| C-37 | Stage 0 EXIT SIGNAL pre-commits Stage 5 closure form + mandate | aspirational |   1 | correctness |
| C-38 | Block 3 dual-lock annotations echo DUAL-LOCK ERROR verbatim   | aspirational |   1 | correctness |
|      | **Total**                                                      |              | 104 |             |

**Essential** (50 pts): C-01 through C-05, 10 pts each.
**Recommended** (24 pts): C-06 through C-08, 8 pts each.
**Aspirational** (30 pts): C-09 (1) + C-10 (1) + C-11 (1) + C-12 (1) + C-13 (1)
  + C-14 (1) + C-15 (1) + C-16 (1) + C-17 (1) + C-18 (1) + C-19 (1) + C-20 (1)
  + C-21 (1) + C-22 (1) + C-23 (1) + C-24 (1) + C-25 (1) + C-26 (1)
  + C-27 (1) + C-28 (1) + C-29 (1) + C-30 (1) + C-31 (1) + C-32 (1)
  + C-33 (1) + C-34 (1) + C-35 (1) + C-36 (1) + C-37 (1) + C-38 (1) = 30 pts.

**Formula**: sum of individual criterion scores (PASS = full, PARTIAL = half rounded down, FAIL = 0).
**Golden**: all 5 essential PASS + composite >= 80.

---

## Composite Scores (R9 under v10)

| Variation | Essential | Recommended | Aspirational | Total |
|-----------|-----------|-------------|--------------|-------|
| V-01 | 50 | 24 | 26 | **100** |
| V-02 | 50 | 24 | 26 | **100** |
| V-03 | 50 | 24 | 26 | **100** |
| V-04 | 50 | 24 | 27 | **101** |
| V-05 | 50 | 24 | 29 | **103** |

**All five pass the golden threshold (all essential PASS + composite >= 80).**

Score basis: R9 v9 baseline = 99 for all five variations. C-35 adds 1 pt for V-01/V-04/V-05.
C-36 adds 1 pt for V-02/V-04/V-05. C-37 adds 1 pt for V-03/V-05. C-38 adds 1 pt for V-05
only. Aspirational pool grows from 26 to 30 pts (max); total grows from 100 to 104.

---

## Ranking

1. **V-05** -- 103/104, all four excellence signal patterns (highest structural density; sole
   carrier of C-38 dual-lock label precision completing bidirectional coverage for all five
   SESSION INVARIANTS)
2. **V-04** -- 101/104, two excellence signal patterns (C-35 CLOSURE CANONICAL FORM +
   C-36 Invariant E as SYNTHESIS EVIDENCE MANDATE)
3. **V-01** -- 100/104, one pattern (C-35 CLOSURE CANONICAL FORM pre-registration)
4. **V-02** -- 100/104, one pattern (C-36 SESSION INVARIANTS Invariant E with SYNTHESIS-FAIL)
5. **V-03** -- 100/104, one pattern (C-37 Stage 0 EXIT SIGNAL forward pre-commitment chain)

V-01 and V-02 are peer-ranked at 100/104; V-03 ranks last because Stage 0 pre-commit tests
a distinct structural axis (Stage 0 to Stage 5 forward chain) but does not extend the
SESSION INVARIANTS registration layer as C-35 and C-36 do.

---

## Excellence Signals -- Candidates for v11 C-39+

No new excellence signal patterns emerged from R9 beyond the four codified in v10 (C-35
through C-38). V-05 converges all four patterns. Candidate axes for v11 include:

- **Full SESSION INVARIANTS five-invariant coverage in standalone block**: C-12 currently
  requires A through D at minimum; C-36 adds Invariant E. A variation that registers all five
  SESSION INVARIANTS (A/B/C/D/E) with canonical labels and failure language in the standalone
  pre-stage block as a unified five-invariant architecture would exceed the current
  per-criterion scope.
- **Stage 0 pre-commit chain verified at ROLE A initialization**: C-37 creates the Stage 0
  commitment; C-27 creates the ROLE A initialization contract. A variation that explicitly
  cross-verifies Stage 0 commitments at ROLE A initialization (naming Stage 0 fields by name
  in ROLE A output) would create a three-anchor chain (Stage 0 -> ROLE A -> Stage 5) parallel
  to the C-27 -> C-31 contract-verification pattern.
- **CAMPAIGN CLOSURE CANONICAL FORM verified against Stage 0 forward commitments**: C-35
  requires pre-registration before roles execute and Stage 5 echo by name. A variation that
  additionally verifies the pre-registered form is consistent with Stage 0
  synthesis_closure_form (C-37) at Stage 0 EXIT SIGNAL time would close the
  registration-to-commitment loop at Stage 0.

```json
{"top_score": 103, "max_score": 104, "all_essential_pass": true, "new_criteria": ["C-35: CAMPAIGN CLOSURE CANONICAL FORM pre-registration -- bidirectional enforcement for C-33 (V-01/V-04/V-05)", "C-36: SESSION INVARIANTS Invariant E as SYNTHESIS EVIDENCE MANDATE with SYNTHESIS-FAIL -- full two-layer enforcement for C-34 completing C-14 architecture across all five SESSION INVARIANTS (V-02/V-04/V-05)", "C-37: Stage 0 EXIT SIGNAL pre-commits synthesis_closure_form and synthesis_mandate_label verified at Stage 5 ENTRY CONDITIONS by field name -- Stage 0 to Stage 5 pre-commitment chain (V-03/V-05)", "C-38: Block 3 dual-lock annotations echo DUAL-LOCK ERROR verbatim with SESSION INVARIANT A/B identification -- resolves R8 universal C-14 partial (V-05 only)"]}
```

---

## Version Notes

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

**No reductions** (all existing criteria at 1-pt floor; essential and recommended unchanged).
Aspirational pool grows from 26 to 30 pts. Total grows from 100 to 104.

**Structural pattern -- parallel registration-level governance layer**:
The four new criteria form a governance layer above the behavioral/instruction layer captured
in v9. C-35 + C-36 create registration-level enforcement for C-33/C-34 (canonical source +
echo). C-37 creates a Stage 0 forward-commitment chain for both properties. C-38 completes
the C-14 registered-label coverage for all five SESSION INVARIANTS. V-05 achieves the
maximum score (103/104) as the convergence candidate where all four patterns are present and
mutually reinforcing. The single missing point reflects a consistent partial (scoring 0) in
the aspirational tier across all R9 variations.

---

### v9 (2026-03-16)

Two new aspirational criteria from R8 excellence signals: C-33 (Stage 5 EXIT SIGNAL carries
terminal closure declaration, 1 pt), C-34 (evidence_summary instruction registers omission
failure label, 1 pt). Two reductions: C-14 (2->1), C-18 (2->1). New structural pattern:
five-link traceability chain (C-27 -> C-31 -> C-30 -> C-34 -> C-32 -> C-33).

### v8 (2026-03-16)

Three new aspirational criteria from R7 excellence signals: C-30 (evidence_summary
instruction mandates all three artifact reads, 1 pt), C-31 (Stage 5 entry gate
cross-references ROLE A displacement read contract, 1 pt), C-32 (Stage 5 EXIT SIGNAL names
each artifact type individually in chain closure, 1 pt). Three reductions: C-27 (2->1),
C-28 (2->1), C-29 (2->1). New structural pattern: contract-to-synthesis traceability chain
(C-27 contract commitment + C-31 contract-verification gate + C-30 instruction mandate +
C-32 named-provenance exit audit).

### v7 (2026-03-16)

Three new aspirational criteria from R6 V-05 excellence signals: C-27 (ROLE A pre-stage
initialization commits displacement evidence chain, 2 pts), C-28 (Stage 5 entry conditions
gate on displacement chain completeness, 2 pts), C-29 (Stage 5 EXIT SIGNAL names
displacement read chain closure, 2 pts). Six reductions: C-13 (2->1), C-17 (2->1),
C-20 (2->1), C-24 (2->1), C-25 (2->1), C-26 (2->1). New structural pattern:
three-layer synthesis governance (C-17 declaration + C-25 output + C-29 audit record).

### v6 (2026-03-15)

Three new aspirational criteria from R5 excellence signals: C-24 (ROLE A confirms INCUMBENT
ANCHOR binding pre-S0), C-25 (Stage 5 cites all three artifact Displacement reads), C-26
(Invariant D binding note names INCUMBENT ANCHOR sub-section as source). Six reductions:
C-09 (2->1), C-10 (2->1), C-12 (2->1), C-21 (2->1), C-22 (2->1), C-23 (2->1).

### v5 (2026-03-15)

Three new aspirational criteria from R4 excellence signals: C-21 (CAMPAIGN OPEN INCUMBENT
ANCHOR with prohibition), C-22 (Invariant D binding note with literal-use label), C-23
(Stage 5 cites artifact Displacement read by value). Six reductions: C-09 (3->2), C-10
(3->2), C-13 (3->2), C-16 (2->1), C-19 (2->1), C-20 (2->1).

### v4 (2026-03-14)

Three new aspirational criteria from R3 excellence signals: C-18 (Invariant E checkpoint at
handoff schema), C-19 (Invariant D template binding to CAMPAIGN OPEN), C-20 (artifact files
carry Displacement read field). Four reductions: C-09 (5->3), C-10 (5->3), C-11 (3->2),
C-13 (3->2).

### v3 (2026-03-14)

Two new aspirational criteria from R2 excellence signals: C-15 (CAMPAIGN OPEN block
pre-registers displacement context), C-16 (per-stage Displacement read fields). One
reduction: C-12 (3->2). SYNTHESIS DECLARATIONS pattern (C-17) introduced.

### v2 (2026-03-14)

Aspirational tier introduced. C-09 through C-14 added. Scoring formula established.
Essential and recommended tiers consolidated from v1 prototype.

### v1 (2026-03-14)

Initial rubric. Five essential criteria (C-01 through C-05) and three recommended criteria
(C-06 through C-08) defined from first campaign run observations.
