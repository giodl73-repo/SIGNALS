Written to `simulations/quest/rubrics/prove-topic-rubric-v6-2026-03-16.md`.

---

**Three new criteria from R5 excellence signals:**

| ID | Pts | Signal source | What it captures |
|----|-----|---------------|-----------------|
| C-24 | 2 | V-04 C-21+C-22 | **ROLE A initialization confirms INCUMBENT ANCHOR binding before Stage 0** -- ROLE A explicitly reads CAMPAIGN OPEN INCUMBENT ANCHOR and records the resolved value at campaign start, before any stage fires. Closes the activation gap between declaration (C-21) and enforcement (C-22). Analogous to schema_compliance_confirmed (C-18) for Invariant E. |
| C-25 | 2 | V-05 all-axis | **Stage 5 cites ALL THREE artifact Displacement reads** -- extends C-23's floor (at least one) to all three (websearch + interview + prototype). Completes the four-layer chain: C-16 -> C-20 -> C-23 -> C-25. |
| C-26 | 2 | V-04 C-21+C-22 | **Invariant D binding note names CAMPAIGN OPEN INCUMBENT ANCHOR sub-section as source** -- binding note references "CAMPAIGN OPEN INCUMBENT ANCHOR" (not just "CAMPAIGN OPEN"), cross-wiring the SESSION INVARIANTS chain to the CAMPAIGN OPEN chain at sub-section precision. |

**Rebalancing:** C-09 2→1, C-10 2→1, C-12 2→1, C-21 2→1, C-22 2→1, C-23 2→1. Aspirational pool holds at 26 pts. Total stays 100.

**Structural pattern:** Two parallel chains (SESSION INVARIANTS and CAMPAIGN OPEN) now explicitly connect at sub-section level (C-26), and both are mechanically activated by ROLE A before Stage 0 (C-24). The displacement evidence chain closes fully at Stage 5 when all three artifacts contribute (C-25). The 1-pt floor → 2-pt successor table now has six entries, each pair answering "did it exist" vs. "was the mechanism complete."
ION INVARIANTS Invariant D:
  Stage 2 template ("Does [evidence item] support the displacement of..."), Stage 3
  template ("Does [practitioner account] reveal a viable transition path..."), Stage 4
  template ("Does [prototype result] make a credible case for displacing...").
  Any deviation from registered template wording = FAIL.

### C-04 -- Synthesis Verdict Present

- **Weight**: essential (10 pts)
- **Category**: correctness
- **Text**: Stage 5 produces a well-formed hypothesis verdict with confidence composite.
- **Pass condition**: Stage 5 output contains all three synthesis body fields:
  `hypothesis_verdict` (value is SUPPORTED, PARTIALLY SUPPORTED, or UNSUPPORTED),
  `confidence_composite` (numeric value), and `key_risk` (framed as residual incumbent
  strength). Missing or blank field = FAIL.

### C-05 -- Null Tally Chain Integrity

- **Weight**: essential (10 pts)
- **Category**: correctness
- **Text**: The null tally chain is computed from s2 + s3 + s4 CE verdicts and
  cross-checked at Stage 4 close and Stage 5.
- **Pass condition**: `null_tally_final` is declared at Stage 4 close with explicit
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
- **Pass condition**: Output shows ROLE B execution with `scout_artifact` field populated
  (path named or stated as not found) and `gate_s_cleared` explicitly set to true or
  false. If false, output must show "CAMPAIGN BLOCKED" and record the blocking step.
  Silent omission of ROLE B = FAIL.

### C-07 -- Handoff Table All 11 Fields With Derivation

- **Weight**: recommended (8 pts)
- **Category**: format
- **Text**: Stage 5 HANDOFF TABLE contains all 11 required fields, each with a
  [derived from: X] annotation.
- **Pass condition**: HANDOFF TABLE in Stage 5 contains every field from the
  PRE-COMMITTED HANDOFF SCHEMA: scout_anchor, incumbent_threat_locked, hypothesis,
  counter_hypothesis, s2_ce_verdict, s3_ce_verdict, s4_ce_verdict, null_tally_final,
  co_activation_confirmed, incumbent_defense_closed, confidence_composite (11 total,
  plus schema_compliance_confirmed as confirmation row). Every field carries
  `[derived from: X]` annotation. Any unlabeled field = FAIL.

### C-08 -- Counter-Hypothesis Resolution

- **Weight**: recommended (8 pts)
- **Category**: depth
- **Text**: Stage 5 resolves the counter-hypothesis from Stage 1 with an explicit
  verdict and citation.
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
  `co_activation_confirmed: dual_lock_fired`, names the adversarial_reviewer_type
  registered at campaign open, and applies `confidence_composite -= 2` with the
  hard-cap note. If null_tally_final < 3, criterion is satisfied by
  `co_activation_confirmed: not_triggered`. Fired dual-lock without both Lock 1 and
  Lock 2 = FAIL.
- **v2 signal**: Differentiated output quality at the evidence-ceiling edge case.
- **Reduced from 5 pts to 3 pts in v4**: C-18 covers the Invariant E structural checkpoint
  that makes all dual-lock mechanics architecturally consistent. C-09 remains as the
  output-level check -- did the dual-lock fire when warranted.
- **Reduced from 3 pts to 2 pts in v5**: C-22 (binding resolution note with canonical
  failure label) extends the two-layer enforcement architecture to the binding mechanism
  itself, further narrowing C-09's unique scope to output-level dual-lock firing behavior.
- **Reduced from 2 pts to 1 pt in v6**: C-24 (ROLE A confirms INCUMBENT ANCHOR binding
  before Stage 0) and C-26 (binding note names INCUMBENT ANCHOR sub-section) further
  extend the architectural coverage. C-09 is now the 1-pt floor: did the dual-lock fire
  when warranted.

### C-10 -- Incumbent Displacement Framing Throughout

- **Weight**: aspirational (1 pt)
- **Category**: depth
- **Text**: Every evidence item across all three check tables explicitly argues for
  or against displacement of the incumbent -- not merely describing the topic.
- **Pass condition**: Stage 2, 3, and 4 INCUMBENT CHECK TABLES each contain at least
  one Yes verdict (or a stated reason all are Inconclusive/No), and the Stage 5
  `evidence_summary` cites the Stage 4 displacement verdict explicitly ("Stage 4
  displacement verdict: [Yes/No/Pending]"). Generic summaries without displacement
  framing = FAIL.
- **v3 signal**: V-05 added per-stage "Displacement read:" fields (C-16). C-10 checks
  the framing in outputs; C-16 checks that the structural mechanism to produce it was present.
- **Reduced from 5 pts to 3 pts in v4**: C-20 adds artifact-level displacement read as the
  structural mechanism. C-10 remains as the Stage 5 framing output check; C-16 and C-20
  are its structural predecessors.
- **Reduced from 3 pts to 2 pts in v5**: C-23 (Stage 5 cites artifact Displacement read
  by value) captures the richest dimension of displacement framing -- that Stage 5
  synthesis consumes artifact field values, not just re-states stage verdicts. C-10
  remains as the output-level framing check; C-16, C-20, and C-23 form its structural chain.
- **Reduced from 2 pts to 1 pt in v6**: C-25 (Stage 5 cites all three artifact Displacement
  reads) completes the chain through all three artifact files. C-10 is now the 1-pt floor:
  did Stage 5 cite the Stage 4 displacement verdict at all.

### C-11 -- Invariant Enforcement Language is Mechanical, Not Advisory

- **Weight**: aspirational (1 pt)
- **Category**: correctness
- **Text**: Every SESSION INVARIANT uses explicit hard-failure language at its
  enforcement checkpoint, not advisory phrasing.
- **Pass condition**: At minimum, the enforcement statements for Invariant D (C-03),
  the null tally rule (C-05), and the handoff schema (C-07) use mechanical failure
  language: e.g., "deviation = format error", "mismatch = integrity failure",
  "unlabeled field = FAIL". Soft advisory language ("try to follow", "make sure to",
  "where possible") at any of these three checkpoints = FAIL.
- **Round 1 signal**: V-01 (score 90) kept hard-failure language intact across a format
  change. V-03 (score 62) softened to advisory and lost three essential PARTIALs.
  The enforcement language is the structural mechanism, not incidental style.
- **Reduced from 3 pts to 2 pts in v4**: C-14, C-18, and C-19 together cover the
  full two-layer enforcement architecture across Invariants D and E. C-11 remains as
  the minimum-bar presence check -- mechanical language at all three checkpoints.
- **Reduced from 2 pts to 1 pt in v5**: C-14, C-18, and C-22 now cover the full
  bidirectional enforcement architecture including the binding resolution failure label.
  C-11 is the 1-pt floor: did mechanical language appear at the three checkpoints at all.
  Unchanged in v6.

### C-12 -- SESSION INVARIANTS Registered in Standalone Pre-Stage Block

- **Weight**: aspirational (1 pt)
- **Category**: format
- **Text**: All SESSION INVARIANTS appear in a dedicated named block before Stage 0
  executes, in addition to any inline references within stage bodies.
- **Pass condition**: Output contains a named SESSION INVARIANTS section (TABLE or LIST)
  that appears before Stage 0's `gate_open` EXIT SIGNAL, enumerates all active
  invariants (A through D at minimum), and states each invariant's activation condition.
  Invariants appearing only inline within stage bodies, without a standalone pre-stage
  registration block = FAIL.
- **Round 1 signal**: V-02 (score 76) embedded invariants inline; C-03 and C-05
  degraded to PARTIAL. The standalone pre-stage block is the structural precondition
  for essential compliance.
- **Reduced from 3 pts to 2 pts in v3** to accommodate C-15 (CAMPAIGN OPEN
  pre-registration). Unchanged in v4 and v5.
- **Reduced from 2 pts to 1 pt in v6**: C-14 (two-layer enforcement), C-18 (Invariant E
  checkpoint), C-22 (binding note + failure label), and C-26 (binding note names
  INCUMBENT ANCHOR sub-section) all extend the standalone block with progressively
  richer structural mechanisms. C-12 is now the 1-pt floor: did the standalone block
  exist before Stage 0 at all.

### C-13 -- Stage 5 Synthesis Fields Isolated as Named Declarations

- **Weight**: aspirational (2 pts)
- **Category**: format
- **Text**: `hypothesis_verdict`, `confidence_composite`, and `key_risk` each appear as
  explicitly labeled standalone field declarations in Stage 5 -- not embedded within
  prose paragraphs.
- **Pass condition**: Each of the three fields appears as a labeled key-value pair
  (e.g., `hypothesis_verdict: SUPPORTED`, `confidence_composite: 7`,
  `key_risk: [text]`) that can be extracted by pattern-matching without reading
  surrounding prose. Any field identifiable only by reading prose context = FAIL.
- **Round 1 signal**: V-04 (score 85) showed inertia framing buries fields as
  narrative sub-items. C-04 checks presence; C-13 checks isolation.
- **Round 2 signal**: V-03 and V-05 showed the strongest isolation: a named SYNTHESIS
  DECLARATIONS section with explicit prohibition text (see C-17).
- **Reduced from 3 pts to 2 pts in v4**: C-17 (prohibition instruction) and C-19
  (template binding to CAMPAIGN OPEN) are the upstream mechanisms. Unchanged in v5 and v6.

### C-14 -- Two-Layer Enforcement Architecture

- **Weight**: aspirational (2 pts)
- **Category**: correctness
- **Text**: Failure labels are registered canonically in the SESSION INVARIANTS block
  and echoed verbatim at each inline enforcement checkpoint, creating bidirectional
  enforcement.
- **Pass condition**: The SESSION INVARIANTS TABLE or LIST establishes the canonical
  failure label for each invariant (FORMAT ERROR for Invariant D, INTEGRITY FAILURE for
  null tally, DUAL-LOCK ERROR for dual-lock, ORDER ERROR for Invariant C, FAIL for
  handoff schema). Inline enforcement annotations at each stage checkpoint echo the
  exact label from the registered source -- no divergence. If inline labels diverge
  from registered labels, or if labels appear only inline without canonical registration
  in the SESSION INVARIANTS block = FAIL.
- **Round 2 signal**: V-04 and V-05 used this architecture. Drift at Stage 2 incurs
  FORMAT ERROR from two structural directions simultaneously -- the registered table and
  the inline annotation -- making soft deviation self-incriminating. Extends C-11
  (mechanical language present) with C-14 (bidirectional registration makes it
  structurally self-auditing). Unchanged in v5 and v6.

### C-15 -- CAMPAIGN OPEN Block Pre-Registers Displacement Context

- **Weight**: aspirational (1 pt)
- **Category**: format
- **Text**: A CAMPAIGN OPEN section appears before SESSION INVARIANTS registration,
  recording `incumbent` and `incumbent_strength` so all Invariant D checks operate
  against a named, persistent displacement frame.
- **Pass condition**: Output contains a CAMPAIGN OPEN block (or equivalent named
  section) that appears before the SESSION INVARIANTS block and declares at minimum
  `incumbent` (the tool or practice being displaced) and `incumbent_strength`
  (quantified resistance level). Stages that define displacement context inline,
  re-establishing it per stage rather than carrying it forward = FAIL.
- **Round 2 signal**: V-05 exclusively. Registering `incumbent` and `incumbent_strength`
  before any invariant fires establishes the displacement context that all subsequent
  Invariant D checkpoints rely on. Complements C-12 (SESSION INVARIANTS block): C-15 is
  the upstream context that gives the invariants something to bind to.
- **Reduced from 2 pts to 1 pt in v5**: C-21 captures the richer behavior -- the
  INCUMBENT ANCHOR sub-section with the "Do not re-establish" prohibition. C-15 is now
  the 1-pt floor: did CAMPAIGN OPEN block exist with `incumbent` and `incumbent_strength`.
  Unchanged in v6.

### C-16 -- Per-Stage Displacement Read Fields

- **Weight**: aspirational (1 pt)
- **Category**: depth
- **Text**: Each of Stages 2, 3, and 4 includes a dedicated "Displacement read:"
  synthesis field summarizing the stage's displacement verdict, in addition to the
  INCUMBENT CHECK TABLE.
- **Pass condition**: Each of Stages 2, 3, and 4 contains a labeled "Displacement
  read:" field (or equivalent named displacement synthesis field) that synthesizes
  whether the stage's evidence supports, challenges, or is inconclusive about incumbent
  displacement. This field appears in addition to the INCUMBENT CHECK TABLE rows,
  synthesizing them toward a stage-level displacement conclusion. Stages that carry
  verdict information only in the INCUMBENT CHECK TABLE rows, without a synthesis
  field = FAIL.
- **Round 2 signal**: V-05 only. Giving each stage a "Displacement read:" field makes
  the INCUMBENT CHECK TABLE feel like evidence toward a conclusion rather than a
  compliance checkbox. Extends C-10 with C-16 (structural mechanism for organic framing).
- **Reduced from 2 pts to 1 pt in v5**: C-20 (artifact carries Displacement read field)
  and C-23 (Stage 5 cites artifact Displacement read by value) extend the chain beyond
  stage output. C-16 is now the 1-pt floor: did stages declare Displacement read fields
  at all. C-20 and C-23 capture the richer portability and synthesis behaviors.
  Unchanged in v6.

### C-17 -- SYNTHESIS DECLARATIONS Section With Explicit Prohibition

- **Weight**: aspirational (2 pts)
- **Category**: format
- **Text**: Stage 5 opens with a named SYNTHESIS DECLARATIONS section whose header
  or preamble contains an explicit prohibition against embedding synthesis fields
  in prose sentences.
- **Pass condition**: Stage 5 contains a distinctly named section (SYNTHESIS
  DECLARATIONS or equivalent) that appears before `evidence_summary` and whose header
  or preamble explicitly states that synthesis fields must not appear as prose sub-items.
  Qualifying language: "Do not embed these values in prose sentences. Each on its own
  line, extractable by label match." or equivalent explicit prohibition. A prompt that
  produces isolated fields (passing C-13) without explicit prohibition text in the
  section header = FAIL.
- **Round 2 signal**: V-03 and V-05. Naming the section and stating the prohibition
  eliminates narrative gravity before evidence_summary begins. C-04 (presence) and
  C-13 (isolation) are simultaneously protected by a single structural insertion.
  Unchanged in v5 and v6.

### C-18 -- Invariant E Checkpoint at Handoff Schema

- **Weight**: aspirational (2 pts)
- **Category**: format
- **Text**: The Stage 5 HANDOFF TABLE uses a named Invariant E enforcement checkpoint
  with a canonical failure label registered in SESSION INVARIANTS and echoed inline at
  the schema_compliance_confirmed row.
- **Pass condition**: The SESSION INVARIANTS block registers a canonical label for
  Invariant E (e.g., "Invariant E checkpoint -- FAIL" for any unlabeled or missing
  handoff schema field). The Stage 5 HANDOFF TABLE contains a schema_compliance_confirmed
  row that echoes this exact label (not a paraphrase). Handoff enforcement present but
  using ad-hoc phrasing not registered in SESSION INVARIANTS = FAIL. schema_compliance
  row absent entirely = FAIL.
- **Round 3 signal**: V-01, C-07 evidence: "All 11 fields with [derived from: X];
  Invariant E checkpoint -- FAIL present." Extends C-14 (two-layer enforcement) to
  Invariant E. C-07 checks field presence; C-18 checks that the enforcement mechanism
  governing them is architecturally consistent with the SESSION INVARIANTS system.
  Unchanged in v5 and v6.

### C-19 -- Invariant D Template Binding to CAMPAIGN OPEN

- **Weight**: aspirational (1 pt)
- **Category**: correctness
- **Text**: The displacement-question templates in SESSION INVARIANTS Invariant D
  explicitly interpolate `[incumbent from CAMPAIGN OPEN]`, binding them structurally to
  the pre-registered displacement context rather than restating the incumbent inline.
- **Pass condition**: The SESSION INVARIANTS block's Invariant D entry contains template
  text that references the CAMPAIGN OPEN context by name (e.g.,
  "Does [evidence item] support the displacement of [incumbent from CAMPAIGN OPEN]...").
  Stage tables carry the bound template text -- they do not redefine the incumbent
  independently. Templates that name the incumbent as a literal string, re-establishing
  it per stage, rather than binding to CAMPAIGN OPEN = FAIL.
- **Round 3 signal**: V-02, C-03 evidence: "stage tables reference `[incumbent from
  CAMPAIGN OPEN]`." Bridges C-15 (pre-registration) and C-03 (verbatim use).
- **Reduced from 2 pts to 1 pt in v5**: C-22 (binding resolution note with
  literal-string failure label) captures the richer behavior -- that the binding has a
  registered canonical failure label, not just a bound reference. C-19 is now the
  1-pt floor: does the template use `[incumbent from CAMPAIGN OPEN]` at all.
  Unchanged in v6.

### C-20 -- Artifact Files Carry Displacement Read Field

- **Weight**: aspirational (2 pts)
- **Category**: depth
- **Text**: The websearch, interview, and prototype artifact files written in Stages 2,
  3, and 4 each contain a labeled "Displacement read:" field in their artifact content,
  making displacement evidence portable outside the stage output.
- **Pass condition**: Each of the three write confirmations for `{topic}-websearch-{date}.md`,
  `{topic}-interview-{date}.md`, and `{topic}-prototype-{date}.md` includes, or the
  artifact's described content includes, a labeled "Displacement read:" (or equivalent
  named displacement synthesis field) as part of the artifact body. A "Displacement read:"
  present only in the stage output but not described as part of the artifact file content
  is insufficient for C-20. All three artifacts must carry the field = FAIL if any absent.
- **Round 3 signal**: V-03, C-02 evidence: "websearch, interview, prototype artifacts
  explicitly include Displacement read." Extends C-16 (per-stage Displacement read in
  stage output) to the written artifact files. Makes displacement evidence available to
  downstream skills without re-reading stage output. Unchanged in v5 and v6.

### C-21 -- CAMPAIGN OPEN INCUMBENT ANCHOR With "Do Not Re-Establish" Prohibition

- **Weight**: aspirational (1 pt)
- **Category**: format
- **Text**: The CAMPAIGN OPEN block contains a named INCUMBENT ANCHOR sub-section and
  an explicit prohibition against re-establishing the incumbent per stage.
- **Pass condition**: CAMPAIGN OPEN contains (a) a labeled INCUMBENT ANCHOR sub-section
  (or equivalent named sub-block that isolates `incumbent` and `incumbent_strength` as
  a named unit) and (b) explicit prohibition text stating that the incumbent must not be
  re-established inline at individual stages (e.g., "Do not re-establish the incumbent
  per stage. Carry forward from CAMPAIGN OPEN."). A flat key-value CAMPAIGN OPEN block
  without INCUMBENT ANCHOR labeling or prohibition text -- even if `incumbent` and
  `incumbent_strength` are present (passing C-15) -- = FAIL.
- **Round 4 signal**: V-02, C-15 evidence: "CAMPAIGN OPEN block with INCUMBENT ANCHOR;
  'Do not re-establish the incumbent per stage'." Extends C-15 (CAMPAIGN OPEN block
  pre-registers incumbent + strength) with the structural prohibition that prevents
  per-stage drift. This is the CAMPAIGN OPEN analog of C-17 (SYNTHESIS DECLARATIONS
  with explicit prohibition): C-17 protects synthesis field isolation; C-21 protects
  incumbent name persistence across all six stages. C-15 checks that the context was
  declared; C-21 checks that it is durably locked against re-establishment.
- **Reduced from 2 pts to 1 pt in v6**: C-24 (ROLE A initialization confirms INCUMBENT
  ANCHOR binding before Stage 0) captures the richer behavior -- that ROLE A reads and
  records the resolved incumbent value at campaign start. C-21 is now the 1-pt floor:
  did CAMPAIGN OPEN contain INCUMBENT ANCHOR sub-section + prohibition at all.

### C-22 -- Invariant D Binding Resolution Note With Literal-String Failure Label

- **Weight**: aspirational (1 pt)
- **Category**: correctness
- **Text**: SESSION INVARIANTS Invariant D includes a binding resolution note naming how
  `[incumbent from CAMPAIGN OPEN]` resolves, and registers a canonical failure label
  for using the incumbent as a literal string in the template.
- **Pass condition**: The SESSION INVARIANTS Invariant D entry contains (a) a binding
  resolution note of the form "Binding: [incumbent from CAMPAIGN OPEN] resolves to
  incumbent_name" (or equivalent explicit resolution statement) and (b) a canonical
  failure label for the binding violation (e.g., "naming as literal string = FORMAT ERROR"
  or "literal incumbent use = FORMAT ERROR"). Templates that use `[incumbent from CAMPAIGN
  OPEN]` (passing C-19) without a binding resolution note or without a registered failure
  label for literal-string violation = FAIL.
- **Round 4 signal**: V-02, C-19 evidence: "Invariant D uses `[incumbent from CAMPAIGN
  OPEN]`; 'Binding: [incumbent from CAMPAIGN OPEN] resolves to incumbent_name'; naming
  as literal string = FORMAT ERROR." Extends C-14 (two-layer enforcement) and C-19
  (template uses bound reference) -- C-19 checks that the template is structurally wired
  to CAMPAIGN OPEN; C-22 checks that the binding mechanism itself carries a canonical
  failure label, making literal-string deviation self-incriminating through the two-layer
  architecture. The binding failure label is the C-14-class mechanism for the C-19 binding
  rule.
- **Reduced from 2 pts to 1 pt in v6**: C-26 (Invariant D binding note names CAMPAIGN
  OPEN INCUMBENT ANCHOR sub-section as source) captures the richer behavior -- the binding
  note is explicitly cross-wired to the named sub-section, not just the parent block.
  C-22 is now the 1-pt floor: did Invariant D carry a binding resolution note + failure
  label at all.

### C-23 -- Stage 5 Evidence Summary Cites Artifact Displacement Read by Value

- **Weight**: aspirational (1 pt)
- **Category**: depth
- **Text**: Stage 5 `evidence_summary` references the Displacement read value from at
  least one written artifact directly, confirming that artifact portability (C-20) was
  consumed by Stage 5 synthesis rather than bypassed.
- **Pass condition**: Stage 5 `evidence_summary` or SYNTHESIS DECLARATIONS body includes
  a direct citation of an artifact's Displacement read field by value -- e.g.,
  "websearch Displacement read: [value]", "[artifact]-Displacement read: [value]", or
  equivalent labeled citation that names the artifact file and the read value. Citing
  the Stage 4 displacement verdict (required by C-10) without also citing any artifact
  Displacement read value = FAIL. All three artifacts cited is ideal; at least one
  artifact must be cited.
- **Round 4 signal**: V-03, C-10 evidence: "Per-stage reads; Stage 5 requires 'Stage 4
  displacement verdict: [Yes/No/Pending]' and artifact Displacement read citation."
  Extends C-10 (Stage 5 cites Stage 4 verdict) and C-20 (artifact files carry
  Displacement read field) by verifying that Stage 5 synthesis consumes the artifact's
  field value, not just re-states the stage output verdict. Closes the three-layer chain:
  C-16 (stage output declares Displacement read) -> C-20 (artifact file carries field) ->
  C-23 (Stage 5 synthesis cites artifact field by value). When the chain is intact,
  displacement evidence is traceable from raw stage output through artifact storage
  to final synthesis verdict.
- **Reduced from 2 pts to 1 pt in v6**: C-25 (Stage 5 cites all three artifact
  Displacement reads) captures the complete chain closure. C-23 is now the 1-pt floor:
  did Stage 5 cite at least one artifact Displacement read at all.

### C-24 -- ROLE A Initialization Confirms INCUMBENT ANCHOR Binding Before Stage 0

- **Weight**: aspirational (2 pts)
- **Category**: correctness
- **Text**: ROLE A initialization explicitly reads and records the resolved incumbent
  value from CAMPAIGN OPEN INCUMBENT ANCHOR before Stage 0 gates, creating a pre-stage
  binding confirmation that mechanically enforces the prohibition registered in C-21.
- **Pass condition**: ROLE A initialization output (appearing before Stage 0 `gate_open`)
  contains a labeled confirmation that reads the INCUMBENT ANCHOR value and records
  the resolved binding (e.g., "INCUMBENT ANCHOR read: [resolved_value] confirmed.
  Invariant D binding active." or equivalent). This confirmation must trace the resolved
  value to CAMPAIGN OPEN INCUMBENT ANCHOR by name, not to a stage-level literal
  definition. A CAMPAIGN OPEN INCUMBENT ANCHOR sub-section + prohibition present
  (passing C-21) without ROLE A explicitly reading and recording the binding at
  initialization = FAIL. ROLE A confirmation that states the incumbent as a literal
  string without tracing to CAMPAIGN OPEN INCUMBENT ANCHOR = FAIL.
- **Round 5 signal**: V-04 (C-21 + C-22 combined axis). When both INCUMBENT ANCHOR
  sub-section (C-21) and binding resolution note (C-22) coexist, the optimal variation
  shows ROLE A consuming the binding before Stage 0 fires -- a pre-stage activation
  confirmation analogous to schema_compliance_confirmed (C-18) for Invariant E. C-21
  checks the INCUMBENT ANCHOR sub-section + prohibition was declared; C-22 checks the
  binding note + failure label was registered; C-24 checks ROLE A mechanically consumed
  the registered binding before any stage fired, closing the activation gap between
  declaration and enforcement.

### C-25 -- Stage 5 Evidence Summary Cites All Three Artifact Displacement Reads

- **Weight**: aspirational (2 pts)
- **Category**: depth
- **Text**: Stage 5 `evidence_summary` cites the Displacement read value from all three
  written artifacts (websearch, interview, prototype), completing the Stage 2/3/4
  artifact portability chain through Stage 5 synthesis.
- **Pass condition**: Stage 5 `evidence_summary` or SYNTHESIS DECLARATIONS body includes
  labeled citations of ALL THREE artifact Displacement reads -- from
  `{topic}-websearch-{date}.md`, `{topic}-interview-{date}.md`, and
  `{topic}-prototype-{date}.md` -- each identifying the artifact source and the read
  value (e.g., "websearch Displacement read: [X], interview Displacement read: [Y],
  prototype Displacement read: [Z]"). Citing only one or two artifact Displacement reads
  (passing C-23) without the third = FAIL. A Stage 5 that cites only the Stage 4
  stage-output verdict without any artifact Displacement reads fails both C-23 and C-25.
- **Round 5 signal**: V-05 (all-axis). When C-20 (artifact files carry Displacement read)
  and C-23 (Stage 5 cites at least one artifact) both pass, the optimal all-axis
  variation cites all three artifact reads in Stage 5 synthesis, confirming that the
  full displacement evidence chain is intact. C-23 checks the floor; C-25 checks the
  chain is closed at all three artifact sources. Completes the four-layer chain:
  C-16 (per-stage Displacement read fields) -> C-20 (artifact portability) ->
  C-23 (Stage 5 floor citation) -> C-25 (Stage 5 cites all three).

### C-26 -- Invariant D Binding Note Names CAMPAIGN OPEN INCUMBENT ANCHOR as Source

- **Weight**: aspirational (2 pts)
- **Category**: correctness
- **Text**: The binding resolution note in SESSION INVARIANTS Invariant D explicitly
  names CAMPAIGN OPEN INCUMBENT ANCHOR (the named sub-section) as the binding source,
  not merely CAMPAIGN OPEN (the parent block), cross-wiring the SESSION INVARIANTS
  chain to the CAMPAIGN OPEN chain at sub-section precision.
- **Pass condition**: SESSION INVARIANTS Invariant D binding resolution note uses
  "CAMPAIGN OPEN INCUMBENT ANCHOR" (or the exact name of the INCUMBENT ANCHOR
  sub-section as registered in CAMPAIGN OPEN) as the binding source citation -- e.g.,
  "Binding: [incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR] resolves to incumbent_name."
  A binding note that carries a resolution statement + failure label (passing C-22)
  but references only "CAMPAIGN OPEN" without the INCUMBENT ANCHOR sub-section
  qualifier = FAIL. Templates that name the incumbent as a literal string fail C-19
  and therefore cannot pass C-26.
- **Round 5 signal**: V-04 (C-21 + C-22 combined axis). When CAMPAIGN OPEN
  INCUMBENT ANCHOR sub-section (C-21) and Invariant D binding resolution note (C-22)
  coexist, the optimal variation names the sub-section in the binding note rather than
  the parent block. This is the cross-chain connection: the SESSION INVARIANTS chain
  (C-12 -> C-14 -> C-18 -> C-22) explicitly wired to the CAMPAIGN OPEN chain
  (C-15 -> C-21 -> C-24) at sub-section precision. C-19 checks that the template uses
  a bound reference; C-22 checks that the binding note + failure label exist; C-26
  checks that the binding note names the INCUMBENT ANCHOR sub-section as the canonical
  resolution anchor for both chains simultaneously.

---

## Scoring Summary

| ID   | Text (short)                                         | Weight       | Pts | Category    |
|------|------------------------------------------------------|--------------|-----|-------------|
| C-01 | All 6 EXIT SIGNALs declared in order                | essential    |  10 | correctness |
| C-02 | All 6 artifacts written + confirmed                 | essential    |  10 | behavior    |
| C-03 | Session Invariant D verbatim at S2/3/4              | essential    |  10 | correctness |
| C-04 | Synthesis verdict + confidence present              | essential    |  10 | correctness |
| C-05 | Null tally chain cross-checked                      | essential    |  10 | correctness |
| C-06 | Gate S scout loader executes                        | recommended  |   8 | coverage    |
| C-07 | Handoff table 11 fields + derivations               | recommended  |   8 | format      |
| C-08 | Counter-hypothesis resolved with verdict            | recommended  |   8 | depth       |
| C-09 | Atomic dual-lock fires when warranted               | aspirational |   1 | behavior    |
| C-10 | Incumbent displacement framing throughout           | aspirational |   1 | depth       |
| C-11 | Invariant enforcement language mechanical           | aspirational |   1 | correctness |
| C-12 | SESSION INVARIANTS in standalone block              | aspirational |   1 | format      |
| C-13 | Stage 5 synthesis fields isolated                   | aspirational |   2 | format      |
| C-14 | Two-layer enforcement architecture                  | aspirational |   2 | correctness |
| C-15 | CAMPAIGN OPEN pre-registers displacement            | aspirational |   1 | format      |
| C-16 | Per-stage Displacement read fields                  | aspirational |   1 | depth       |
| C-17 | SYNTHESIS DECLARATIONS explicit prohibition         | aspirational |   2 | format      |
| C-18 | Invariant E checkpoint at handoff schema            | aspirational |   2 | format      |
| C-19 | Invariant D template binding to CAMPAIGN OPEN       | aspirational |   1 | correctness |
| C-20 | Artifact files carry Displacement read field        | aspirational |   2 | depth       |
| C-21 | CAMPAIGN OPEN INCUMBENT ANCHOR + prohibition        | aspirational |   1 | format      |
| C-22 | Invariant D binding note with literal-use label     | aspirational |   1 | correctness |
| C-23 | Stage 5 cites artifact Displacement read value      | aspirational |   1 | depth       |
| C-24 | ROLE A confirms INCUMBENT ANCHOR binding pre-S0     | aspirational |   2 | correctness |
| C-25 | Stage 5 cites all three artifact Displacement reads | aspirational |   2 | depth       |
| C-26 | Invariant D binding note names INCUMBENT ANCHOR     | aspirational |   2 | correctness |
|      | **Total**                                            |              | 100 |             |

**Essential** (50 pts): C-01 through C-05, 10 pts each.
**Recommended** (24 pts): C-06 through C-08, 8 pts each.
**Aspirational** (26 pts): C-09 (1) + C-10 (1) + C-11 (1) + C-12 (1) + C-13 (2)
  + C-14 (2) + C-15 (1) + C-16 (1) + C-17 (2) + C-18 (2) + C-19 (1) + C-20 (2)
  + C-21 (1) + C-22 (1) + C-23 (1) + C-24 (2) + C-25 (2) + C-26 (2) = 26 pts.

**Formula**: sum of individual criterion scores (PASS = full, PARTIAL = half rounded down, FAIL = 0).
**Golden**: all 5 essential PASS + composite >= 80.

---

## Version Notes

### v6 (2026-03-16)

**Three new aspirational criteria from R5 excellence signals**:

- **C-24 (2 pts)** -- ROLE A initialization confirms INCUMBENT ANCHOR binding before Stage 0.
  Signal source: V-04 (C-21 + C-22 combined axis). When INCUMBENT ANCHOR sub-section
  (C-21) and binding resolution note (C-22) coexist, the optimal output shows ROLE A
  consuming the binding before Stage 0 fires -- a pre-stage activation confirmation
  analogous to schema_compliance_confirmed (C-18) for Invariant E. C-21 declares the
  sub-section + prohibition; C-22 registers the binding note + failure label; C-24 checks
  ROLE A mechanically read and recorded the binding before any stage fired, closing the
  activation gap between declaration and enforcement.

- **C-25 (2 pts)** -- Stage 5 cites all three artifact Displacement reads.
  Signal source: V-05 (all-axis). When C-20 (artifact portability) and C-23 (floor
  citation) both pass, the optimal variation cites all three artifact reads in Stage 5
  synthesis. C-23 checks the floor; C-25 checks the Stage 2/3/4 artifact chain is
  closed at all three sources. Completes the four-layer displacement chain:
  C-16 -> C-20 -> C-23 -> C-25.

- **C-26 (2 pts)** -- Invariant D binding note names CAMPAIGN OPEN INCUMBENT ANCHOR as source.
  Signal source: V-04 (C-21 + C-22 combined axis). When both coexist, the optimal output
  names the INCUMBENT ANCHOR sub-section specifically (not just "CAMPAIGN OPEN") in the
  binding note. This is the cross-chain connection: SESSION INVARIANTS chain
  (C-12 -> C-14 -> C-18 -> C-22) explicitly wired to the CAMPAIGN OPEN chain
  (C-15 -> C-21 -> C-24) at sub-section precision. C-22 checks the binding note +
  failure label exist; C-26 checks the note names the sub-section as the canonical
  resolution anchor.

**Point rebalancing** (aspirational pool stays at 26 pts, total stays at 100):
- C-09: 2 pts -> 1 pt. C-24 (ROLE A binding confirmation) and C-26 (binding note names
  INCUMBENT ANCHOR) further narrow C-09's unique scope. C-09 is the 1-pt floor: did
  the dual-lock fire when warranted.
- C-10: 2 pts -> 1 pt. C-25 (all three artifact reads in Stage 5) completes the
  displacement framing chain. C-10 is the 1-pt floor: did Stage 5 cite the Stage 4
  displacement verdict.
- C-12: 2 pts -> 1 pt. C-14, C-18, C-22, and C-26 all extend the standalone block with
  richer structural mechanisms. C-12 is the 1-pt floor: did the standalone block exist
  before Stage 0.
- C-21: 2 pts -> 1 pt. C-24 captures the richer ROLE A activation confirmation. C-21 is
  the 1-pt floor: did CAMPAIGN OPEN contain INCUMBENT ANCHOR sub-section + prohibition.
- C-22: 2 pts -> 1 pt. C-26 captures the richer sub-section cross-reference. C-22 is
  the 1-pt floor: did Invariant D carry a binding resolution note + failure label.
- C-23: 2 pts -> 1 pt. C-25 captures the complete all-three chain. C-23 is the 1-pt
  floor: did Stage 5 cite at least one artifact Displacement read.

**Structural lineage of new criteria**:
- C-24 extends C-21 (INCUMBENT ANCHOR declared) and C-22 (binding registered): the
  binding mechanism gets a ROLE A activation confirmation, parallel to how C-18
  (Invariant E checkpoint at handoff) extended C-14 (two-layer enforcement).
- C-25 extends C-23 (at-least-one artifact cited): the displacement read chain is
  fully closed at Stage 5 synthesis when all three artifacts contribute.
- C-26 extends C-22 (binding note exists): the binding note explicitly cross-wires to
  the CAMPAIGN OPEN INCUMBENT ANCHOR sub-section, connecting the SESSION INVARIANTS
  chain to the CAMPAIGN OPEN chain at sub-section precision.

**1-pt floor criterion progression** (each floor criterion has a 2-pt successor):

| Floor (1 pt) | Richer successor (2 pt) | What the successor adds |
|---|---|---|
| C-15 | C-21 | INCUMBENT ANCHOR sub-section + prohibition |
| C-21 | C-24 | ROLE A reads and records binding before Stage 0 |
| C-19 | C-22 | Binding note + failure label |
| C-22 | C-26 | Binding note names INCUMBENT ANCHOR sub-section |
| C-16 | C-20 | Displacement read portable in artifact files |
| C-23 | C-25 | All three artifact reads cited in Stage 5 |

### v5 (2026-03-16)

Three new aspirational criteria from R4 excellence signals (C-21, C-22, C-23).
C-09 reduced 3->2, C-10 reduced 3->2, C-11 reduced 2->1, C-15 reduced 2->1,
C-16 reduced 2->1, C-19 reduced 2->1.

### v4 (2026-03-16)

Three new aspirational criteria from R3 excellence signals (C-18, C-19, C-20).
C-09 reduced 5->3, C-10 reduced 5->3, C-11 reduced 3->2, C-13 reduced 3->2.

### v3 (2026-03-16)

Four new aspirational criteria from R2 excellence signals (C-14, C-15, C-16, C-17).
C-09 reduced 8->5, C-10 reduced 8->5, C-11 reduced 4->3, C-12 reduced 3->2.

### v2 (2026-03-16)

Three new aspirational criteria from R1 excellence signals (C-11, C-12, C-13).
C-09 and C-10 reduced from 13 pts to 8 pts to make room.
