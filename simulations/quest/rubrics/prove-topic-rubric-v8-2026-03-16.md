Written to `simulations/quest/rubrics/prove-topic-rubric-v8-2026-03-16.md`.

---

**v8 summary:**

**Three new aspirational criteria** from R7 excellence signals:

| ID | Pts | Signal | What it captures |
|----|-----|--------|-----------------|
| C-30 | 1 | V-03 Signal 1 | evidence_summary carries a mandatory (not conditional) citation instruction for all three artifact Displacement reads — instruction-level mandate makes C-25 structurally enforced rather than emergent |
| C-31 | 1 | V-01/V-02 gap | Stage 5 ENTRY CONDITIONS gate explicitly cross-references ROLE A `displacement_read_contract` by field name — gate becomes contract-verification step, not independent structural check |
| C-32 | 1 | V-03 Signal 2 | Stage 5 EXIT SIGNAL chain closure names each artifact type individually (websearch, interview, prototype) — named-provenance audit trail, not count assertion |

**Three reductions** (aspirational pool holds at 26 pts): C-27 (2→1), C-28 (2→1), C-29 (2→1).

**New structural pattern — contract-to-synthesis traceability chain**:
- C-27: ROLE A commits `displacement_read_contract`
- C-31: Stage 5 entry gate names the contract → contract-verification step
- C-30: evidence_summary instruction mandates all three citations → C-25 structurally enforced
- C-32: EXIT SIGNAL names artifact types individually → named-provenance record

The V-01 cascading gap is now captured: ROLE A committing the contract without the entry gate naming it (C-31) and evidence_summary mandating it (C-30) left Stage 5 free to bypass the artifact citation chain entirely.
ontract (C-27) without the entry gate naming it (C-31) and evidence_summary
mandating it (C-30) left Stage 5 synthesis free to bypass the chain.

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

## Aspirational Criteria (26 pts total -- raise the bar)

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
  C-09 is the 1-pt floor: did the dual-lock fire when warranted. Unchanged in v7 and v8.

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
  verdict at all. Unchanged in v7 and v8.

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
  mechanical language appear at the three checkpoints at all. Unchanged in v6, v7, v8.

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
  standalone block exist before Stage 0 at all. Unchanged in v7 and v8.

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
  did Stage 5 synthesis fields appear as labeled key-value pairs at all. Unchanged in v8.

### C-14 -- Two-Layer Enforcement Architecture

- **Weight**: aspirational (2 pts)
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
  Unchanged in v5, v6, v7, and v8.

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
  Unchanged in v6, v7, and v8.

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
  did stages declare Displacement read fields at all. Unchanged in v6, v7, and v8.

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
  DECLARATIONS section with explicit prohibition text exist at all. Unchanged in v8.

### C-18 -- Invariant E Checkpoint at Handoff Schema

- **Weight**: aspirational (2 pts)
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
  Unchanged in v6, v7, and v8.

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
  floor: did artifact files carry Displacement read field at all. Unchanged in v8.

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
  Unchanged in v7 and v8.

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
  Unchanged in v7 and v8.

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
  Unchanged in v7 and v8.

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
  before Stage 0. Unchanged in v8.

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
  5 evidence_summary cite all three artifact Displacement reads. Unchanged in v8.

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
  OPEN INCUMBENT ANCHOR sub-section as the binding source at all. Unchanged in v8.

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
- **Reduced from 2 pts to 1 pt in v8**: C-31 (Stage 5 entry gate cross-references ROLE A
  displacement_read_contract) captures the richer contract-to-gate traceability behavior.
  The pre-stage contract is not only committed by ROLE A (C-27) but explicitly verified by
  field name at Stage 5 entry (C-31). C-27 is now the 1-pt floor: did ROLE A pre-stage
  initialization commit both incumbent_anchor_read AND displacement_read_contract in a
  single block. C-31 checks that Stage 5 also explicitly cross-wired its entry gate to
  that contract by field name.

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
- **Reduced from 2 pts to 1 pt in v8**: C-31 (Stage 5 entry gate cross-references ROLE A
  displacement_read_contract) captures the richer contract-verification behavior. The entry
  gate is not only present (C-28) but explicitly traces to the ROLE A pre-stage commitment
  by field name, making it a contract-verification step. C-28 is now the 1-pt floor: did
  Stage 5 ENTRY CONDITIONS include an explicit displacement chain completeness gate at all.
  C-31 checks that the gate is explicitly cross-wired to the ROLE A contract.

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
- **Reduced from 2 pts to 1 pt in v8**: C-32 (Stage 5 EXIT SIGNAL names each artifact type
  individually) captures the richer named-provenance behavior. The chain closure declaration
  explicitly names websearch, interview, and prototype, converting the EXIT SIGNAL from a
  count assertion to a named-provenance audit trail. C-29 is now the 1-pt floor: did Stage
  5 EXIT SIGNAL declare displacement read chain closure at all. C-32 checks that the
  declaration individually names each artifact type.

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
  Displacement reads if present" as in V-02) = FAIL. A Stage 4-verdict-only instruction
  ("cite Stage 4 displacement verdict explicitly" as in V-01) without any artifact read
  citation mandate = FAIL. The mandate must name all three artifact types or equivalent
  enumeration.
- **Round 7 signal**: V-01 passes C-27 but fails C-25 because evidence_summary mandates
  only "cite Stage 4 displacement verdict explicitly" -- no artifact reads. V-02 passes C-28
  but fails C-25 because evidence_summary says "Cite artifact Displacement reads if present"
  -- conditional, not required. V-03 passes both C-23 and C-25 because evidence_summary
  "explicitly instructs all three artifact reads." The instruction-level mandate is the
  mechanism that makes C-25 structurally enforced rather than left to synthesis quality.
  This closes the V-01 cascading gap: ROLE A committing displacement_read_contract (C-27)
  without a mandatory evidence_summary instruction (C-30) leaves Stage 5 free to bypass the
  artifact citation chain in synthesis. C-25 checks the output; C-30 checks the instruction
  constraining the output is mandatory.

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
- **Round 7 signal**: V-01 has C-27 (ROLE A contract) but no C-28 (entry gate). V-02 has
  C-28 (entry gate) but no C-27 (contract). No R7 variation showed them cross-wired. When
  both coexist, the optimal pattern explicitly names displacement_read_contract in the entry
  gate, making the gate a contract-verification step rather than an independently conceived
  structural check. This closes the V-01/V-02 axis isolation gap. C-28 checks the gate
  exists; C-31 checks the gate is explicitly traced to the ROLE A contract by field name.

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
- **Round 7 signal**: V-03 EXIT SIGNAL states "All three artifact Displacement reads cited
  in evidence_summary (websearch, interview, prototype). Displacement read chain closed." --
  explicitly naming each artifact type in parenthetical enumeration. This converts the chain
  closure from "all three confirmed" (count assertion) to "websearch, interview, prototype
  confirmed" (named-provenance record), making the campaign audit log a full artifact-
  resolution trace allowing downstream verification without re-reading evidence_summary.
  C-29 checks chain closure declared; C-32 checks each artifact type is individually named.

---

## Scoring Summary

| ID   | Text (short)                                               | Weight       | Pts | Category    |
|------|------------------------------------------------------------|--------------|-----|-------------|
| C-01 | All 6 EXIT SIGNALs declared in order                      | essential    |  10 | correctness |
| C-02 | All 6 artifacts written + confirmed                       | essential    |  10 | behavior    |
| C-03 | Session Invariant D verbatim at S2/3/4                    | essential    |  10 | correctness |
| C-04 | Synthesis verdict + confidence present                    | essential    |  10 | correctness |
| C-05 | Null tally chain cross-checked                            | essential    |  10 | correctness |
| C-06 | Gate S scout loader executes                              | recommended  |   8 | coverage    |
| C-07 | Handoff table 11 fields + derivations                     | recommended  |   8 | format      |
| C-08 | Counter-hypothesis resolved with verdict                  | recommended  |   8 | depth       |
| C-09 | Atomic dual-lock fires when warranted                     | aspirational |   1 | behavior    |
| C-10 | Incumbent displacement framing throughout                 | aspirational |   1 | depth       |
| C-11 | Invariant enforcement language mechanical                 | aspirational |   1 | correctness |
| C-12 | SESSION INVARIANTS in standalone block                    | aspirational |   1 | format      |
| C-13 | Stage 5 synthesis fields isolated                         | aspirational |   1 | format      |
| C-14 | Two-layer enforcement architecture                        | aspirational |   2 | correctness |
| C-15 | CAMPAIGN OPEN pre-registers displacement                  | aspirational |   1 | format      |
| C-16 | Per-stage Displacement read fields                        | aspirational |   1 | depth       |
| C-17 | SYNTHESIS DECLARATIONS explicit prohibition               | aspirational |   1 | format      |
| C-18 | Invariant E checkpoint at handoff schema                  | aspirational |   2 | format      |
| C-19 | Invariant D template binding to CAMPAIGN OPEN             | aspirational |   1 | correctness |
| C-20 | Artifact files carry Displacement read field              | aspirational |   1 | depth       |
| C-21 | CAMPAIGN OPEN INCUMBENT ANCHOR + prohibition              | aspirational |   1 | format      |
| C-22 | Invariant D binding note with literal-use label           | aspirational |   1 | correctness |
| C-23 | Stage 5 cites artifact Displacement read value            | aspirational |   1 | depth       |
| C-24 | ROLE A confirms INCUMBENT ANCHOR binding pre-S0           | aspirational |   1 | correctness |
| C-25 | Stage 5 cites all three artifact Displacement reads       | aspirational |   1 | depth       |
| C-26 | Invariant D binding note names INCUMBENT ANCHOR           | aspirational |   1 | correctness |
| C-27 | ROLE A initialization commits displacement evidence chain | aspirational |   1 | correctness |
| C-28 | Stage 5 entry conditions gate on chain completeness       | aspirational |   1 | format      |
| C-29 | Stage 5 EXIT SIGNAL names displacement read chain closure | aspirational |   1 | correctness |
| C-30 | evidence_summary instruction mandates all three reads     | aspirational |   1 | depth       |
| C-31 | Stage 5 entry gate cross-references ROLE A contract       | aspirational |   1 | format      |
| C-32 | Stage 5 EXIT SIGNAL names artifact types individually     | aspirational |   1 | correctness |
|      | **Total**                                                  |              | 100 |             |

**Essential** (50 pts): C-01 through C-05, 10 pts each.
**Recommended** (24 pts): C-06 through C-08, 8 pts each.
**Aspirational** (26 pts): C-09 (1) + C-10 (1) + C-11 (1) + C-12 (1) + C-13 (1)
  + C-14 (2) + C-15 (1) + C-16 (1) + C-17 (1) + C-18 (2) + C-19 (1) + C-20 (1)
  + C-21 (1) + C-22 (1) + C-23 (1) + C-24 (1) + C-25 (1) + C-26 (1)
  + C-27 (1) + C-28 (1) + C-29 (1) + C-30 (1) + C-31 (1) + C-32 (1) = 26 pts.

**Formula**: sum of individual criterion scores (PASS = full, PARTIAL = half rounded down, FAIL = 0).
**Golden**: all 5 essential PASS + composite >= 80.

---

## Version Notes

### v8 (2026-03-16)

**Three new aspirational criteria from R7 excellence signals**:

- **C-30 (1 pt)** -- evidence_summary instruction mandates all three artifact reads.
  Signal source: V-03 (Signal 1). V-01 passes C-27 but fails C-25 because evidence_summary
  mandates only "cite Stage 4 displacement verdict explicitly" -- no artifact reads. V-02
  passes C-28 but fails C-25 because evidence_summary says "Cite artifact Displacement reads
  if present" -- conditional. V-03 passes both C-23 and C-25 because evidence_summary
  "explicitly instructs all three artifact reads." The instruction-level mandate is the
  mechanism that makes C-25 structurally enforced rather than emergent. C-25 checks the
  output; C-30 checks the instruction constraining the output is mandatory and names all
  three artifact types.

- **C-31 (1 pt)** -- Stage 5 entry gate cross-references ROLE A displacement read contract.
  Signal source: V-01/V-02 axis isolation gap. V-01 has C-27 (ROLE A contract) but no C-28
  (entry gate); V-02 has C-28 (entry gate) but no C-27 (contract). No R7 variation showed
  the gate explicitly cross-wired to the contract. When both coexist, the optimal pattern
  names displacement_read_contract in the entry gate, making the gate a contract-verification
  step. C-28 checks the gate exists; C-31 checks the gate is explicitly traced to the ROLE A
  contract by field name.

- **C-32 (1 pt)** -- Stage 5 EXIT SIGNAL names each artifact type individually in chain
  closure. Signal source: V-03 (Signal 2). V-03 EXIT SIGNAL states "All three artifact
  Displacement reads cited in evidence_summary (websearch, interview, prototype). Displacement
  read chain closed." -- naming each artifact type individually. Converts the chain closure
  from "all three confirmed" (count assertion) to "websearch, interview, prototype confirmed"
  (named-provenance record). C-29 checks chain closure declared; C-32 checks each artifact
  type is individually named.

**Three reductions** (aspirational pool holds at 26 pts):

- **C-27 (2->1)**: C-31 captures the richer contract-to-gate traceability. The pre-stage
  contract is not only committed by ROLE A (C-27) but explicitly verified by name at Stage
  5 entry (C-31). C-27 is the 1-pt floor: did ROLE A commit both incumbent_anchor_read AND
  displacement_read_contract in a single pre-stage block.

- **C-28 (2->1)**: C-31 captures the richer contract-verification behavior. The entry gate
  is not only present (C-28) but explicitly traces to the ROLE A pre-stage commitment by
  field name, making it a contract-verification step. C-28 is the 1-pt floor: did Stage 5
  ENTRY CONDITIONS include an explicit displacement chain completeness gate at all.

- **C-29 (2->1)**: C-32 captures the richer named-provenance behavior. The chain closure
  declaration explicitly names websearch, interview, and prototype, converting the EXIT
  SIGNAL from a count assertion to a named-provenance audit trail. C-29 is the 1-pt floor:
  did Stage 5 EXIT SIGNAL declare displacement read chain closure at all.

**Structural pattern -- contract-to-synthesis traceability chain**: C-27 (ROLE A commits
displacement_read_contract pre-stage) + C-31 (Stage 5 entry gate names the contract,
making it a contract-verification step) + C-30 (evidence_summary instruction mandates all
three artifact citations, making C-25 structurally enforced) + C-32 (EXIT SIGNAL names each
artifact type individually, making the audit log a named-provenance record). The displacement
evidence chain is now fully traced from pre-stage commitment through structural entry gate
through synthesis instruction to named-artifact exit audit -- closing the V-01 cascading gap
where ROLE A contract commitment left Stage 5 free to bypass the artifact citation chain.

---

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
