Written to `simulations/quest/rubrics/prove-topic-rubric-v4-2026-03-16.md`.

---

**Three new aspirational criteria from R3 excellence signals:**

| ID | Pts | Signal source | What it captures |
|----|-----|---------------|-----------------|
| C-18 | 2 | V-01 C-07 | **Invariant E checkpoint at handoff schema** — Stage 5 HANDOFF TABLE has a canonical "Invariant E checkpoint -- FAIL" label registered in SESSION INVARIANTS and echoed at the schema_compliance_confirmed row. Extends C-14 (Invariant D two-layer enforcement) to Invariant E. |
| C-19 | 2 | V-02 C-03 | **Invariant D template binding to CAMPAIGN OPEN** — The template text in SESSION INVARIANTS Invariant D explicitly interpolates `[incumbent from CAMPAIGN OPEN]`, making the binding structural rather than coincidental. Bridges C-15 (pre-registration) and C-03 (verbatim use). |
| C-20 | 2 | V-03 C-02 | **Artifact files carry Displacement read field** — websearch, interview, and prototype artifacts each contain a labeled "Displacement read:" in their file content, making displacement evidence portable to downstream skills. Extends C-16 from stage output to written artifact. |

**Rebalancing:** C-09 5→3, C-10 5→3, C-11 3→2, C-13 3→2. Aspirational pool holds at 26 pts. Total stays 100.

**Structural lineage:** C-18 extends C-14 | C-19 bridges C-15 + C-03 | C-20 extends C-16 — each new criterion is the artifact-level or cross-invariant mechanism behind an existing check.
c}-prototype-{date}.md`, `{topic}-synthesis-{date}.md`, `{topic}-handoff-{date}.md`.
  Any missing confirmation = FAIL.

### C-03 -- Session Invariant D Compliance

- **Weight**: essential (10 pts)
- **Category**: correctness
- **Text**: The displacement-question template is applied verbatim at every incumbent
  check table in Stages 2, 3, and 4.
- **Pass condition**: Each stage's INCUMBENT CHECK TABLE uses the exact template
  registered in the SESSION INVARIANTS block:
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

- **Weight**: aspirational (3 pts)
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

### C-10 -- Incumbent Displacement Framing Throughout

- **Weight**: aspirational (3 pts)
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
  deeper structural mechanism. C-10 remains as the Stage 5 framing output check; C-16
  (stage output) and C-20 (artifact content) are its structural predecessors.

### C-11 -- Invariant Enforcement Language is Mechanical, Not Advisory

- **Weight**: aspirational (2 pts)
- **Category**: correctness
- **Text**: Every SESSION INVARIANT uses explicit hard-failure language at its
  enforcement checkpoint, not advisory phrasing.
- **Pass condition**: At minimum, the enforcement statements for Invariant D (C-03),
  the null tally rule (C-05), and the handoff schema (C-07) use mechanical failure
  language: e.g., "deviation = format error", "mismatch = integrity failure",
  "unlabeled field = FAIL". Soft advisory language ("try to follow", "make sure to",
  "where possible") at any of these three checkpoints = FAIL.
- **Round 1 signal**: V-01 (score 90) kept hard-failure language intact across a
  format change. V-03 (score 62) softened to advisory and lost three essential PARTIALs.
  The enforcement language is the structural mechanism, not incidental style.
- **Reduced from 3 pts to 2 pts in v4**: C-14, C-18, and C-19 together now cover the
  full two-layer enforcement architecture across Invariants D and E. C-11 remains as
  the minimum-bar presence check -- mechanical language at all three checkpoints.

### C-12 -- SESSION INVARIANTS Registered in Standalone Pre-Stage Block

- **Weight**: aspirational (2 pts)
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
  pre-registration), which captures the complementary upstream context that the
  standalone invariants block depends on. Unchanged in v4.

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
  narrative sub-items. C-04 checks presence; C-13 checks isolation. An output can
  pass C-04 while failing C-13.
- **Round 2 signal**: V-03 and V-05 showed the strongest isolation: a named SYNTHESIS
  DECLARATIONS section with explicit prohibition text (see C-17 for the structural
  mechanism that protects C-13).
- **Reduced from 3 pts to 2 pts in v4**: C-17 (prohibition instruction) and C-19
  (template binding to CAMPAIGN OPEN) are the upstream mechanisms; C-13 remains as
  the output-level isolation check.

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
  structurally self-auditing).

### C-15 -- CAMPAIGN OPEN Block Pre-Registers Displacement Context

- **Weight**: aspirational (2 pts)
- **Category**: format
- **Text**: A CAMPAIGN OPEN section appears before SESSION INVARIANTS registration,
  recording `incumbent` and `incumbent_strength` so all Invariant D checks operate
  against a named, persistent displacement frame.
- **Pass condition**: Output contains a CAMPAIGN OPEN block (or equivalent named
  section) that appears before the SESSION INVARIANTS block and declares at minimum
  `incumbent` (the tool or practice being displaced) and `incumbent_strength`
  (quantified resistance level). All subsequent Invariant D check tables reference
  this pre-registered incumbent by name. Stages that define displacement context
  inline, re-establishing it per stage rather than carrying it forward = FAIL.
- **Round 2 signal**: V-05 exclusively. Registering `incumbent` and `incumbent_strength`
  before any invariant fires establishes the displacement context that all subsequent
  Invariant D checkpoints rely on. Complements C-12 (SESSION INVARIANTS block): C-15 is
  the upstream context that gives the invariants something to bind to.

### C-16 -- Per-Stage Displacement Read Fields

- **Weight**: aspirational (2 pts)
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
- **Round 2 signal**: V-05 only. Giving each stage a "Displacement read:" synthesis
  field makes the INCUMBENT CHECK TABLE feel like evidence toward a conclusion rather
  than a compliance checkbox. Reduces the temptation to soften template wording to
  match a prose-narrative tone. Extends C-10 (displacement framing in output) with
  C-16 (structural mechanism that makes framing organic to each stage).

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
  Extends C-13 (isolation in output) with C-17 (prohibition instruction that prevents
  narrative burial before it occurs).

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
  Invariant E checkpoint -- FAIL present." Extends C-14 (Invariant D two-layer
  enforcement) to cover Invariant E (handoff schema). C-07 checks that all 11 fields
  and derivations are present; C-18 checks that the enforcement mechanism governing
  them is architecturally consistent with the rest of the SESSION INVARIANTS system.

### C-19 -- Invariant D Template Binding to CAMPAIGN OPEN

- **Weight**: aspirational (2 pts)
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
- **Round 3 signal**: V-02, C-03 evidence: "Templates registered in SESSION INVARIANTS D;
  stage tables reference `[incumbent from CAMPAIGN OPEN]`." Bridges C-15 (CAMPAIGN OPEN
  pre-registration) and C-03 (verbatim template use). C-15 establishes the named context;
  C-19 verifies that the template text is structurally wired to it, making the
  binding architectural rather than coincidental.

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
- **Round 3 signal**: V-03, C-02 evidence: "All 6 artifact writes; websearch, interview,
  prototype artifacts explicitly include Displacement read." Extends C-16 (per-stage
  Displacement read fields in stage output) to the written artifact files. C-16 checks
  that the stage declares a displacement synthesis; C-20 checks that this synthesis
  travels into the artifact on disk, making displacement evidence available to downstream
  skills (topic-story, scout handoff) without re-reading stage output.

---

## Scoring Summary

| ID   | Text (short)                                 | Weight       | Pts | Category    |
|------|----------------------------------------------|--------------|-----|-------------|
| C-01 | All 6 EXIT SIGNALs declared in order        | essential    |  10 | correctness |
| C-02 | All 6 artifacts written + confirmed         | essential    |  10 | behavior    |
| C-03 | Session Invariant D verbatim at S2/3/4      | essential    |  10 | correctness |
| C-04 | Synthesis verdict + confidence present      | essential    |  10 | correctness |
| C-05 | Null tally chain cross-checked              | essential    |  10 | correctness |
| C-06 | Gate S scout loader executes               | recommended  |   8 | coverage    |
| C-07 | Handoff table 11 fields + derivations       | recommended  |   8 | format      |
| C-08 | Counter-hypothesis resolved with verdict   | recommended  |   8 | depth       |
| C-09 | Atomic dual-lock fires when warranted      | aspirational |   3 | behavior    |
| C-10 | Incumbent displacement framing throughout  | aspirational |   3 | depth       |
| C-11 | Invariant enforcement language mechanical  | aspirational |   2 | correctness |
| C-12 | SESSION INVARIANTS in standalone block     | aspirational |   2 | format      |
| C-13 | Stage 5 synthesis fields isolated          | aspirational |   2 | format      |
| C-14 | Two-layer enforcement architecture         | aspirational |   2 | correctness |
| C-15 | CAMPAIGN OPEN pre-registers displacement   | aspirational |   2 | format      |
| C-16 | Per-stage Displacement read fields         | aspirational |   2 | depth       |
| C-17 | SYNTHESIS DECLARATIONS explicit prohibition| aspirational |   2 | format      |
| C-18 | Invariant E checkpoint at handoff schema   | aspirational |   2 | format      |
| C-19 | Invariant D template binding to CAMPAIGN OPEN | aspirational | 2 | correctness |
| C-20 | Artifact files carry Displacement read field | aspirational | 2 | depth       |
|      | **Total**                                    |              | 100 |             |

**Essential** (50 pts): C-01 through C-05, 10 pts each.
**Recommended** (24 pts): C-06 through C-08, 8 pts each.
**Aspirational** (26 pts): C-09 (3) + C-10 (3) + C-11 (2) + C-12 (2) + C-13 (2)
  + C-14 (2) + C-15 (2) + C-16 (2) + C-17 (2) + C-18 (2) + C-19 (2) + C-20 (2) = 26 pts.

**Formula**: sum of individual criterion scores (PASS = full, PARTIAL = half rounded down, FAIL = 0).
**Golden**: all 5 essential PASS + composite >= 80.

---

## Version Notes

### v4 (2026-03-16)

**Three new aspirational criteria from R3 excellence signals**:

- **C-18 (2 pts)** -- Invariant E checkpoint at handoff schema. Extends C-14 (Invariant D
  two-layer enforcement) to Invariant E (handoff schema). Where C-14 ensures Invariant D
  failure labels are registered and echoed bidirectionally, C-18 applies the same
  architectural requirement to the Stage 5 HANDOFF TABLE enforcement row. C-07 checks
  field presence; C-18 checks that the mechanism governing those fields is part of the
  SESSION INVARIANTS system. Signal: V-01, C-07 evidence ("Invariant E checkpoint -- FAIL
  present").

- **C-19 (2 pts)** -- Invariant D template binding to CAMPAIGN OPEN. Bridges C-15
  (CAMPAIGN OPEN pre-registers incumbent) and C-03 (verbatim template use) by verifying
  that the template text in SESSION INVARIANTS Invariant D explicitly interpolates
  `[incumbent from CAMPAIGN OPEN]`. C-15 establishes the named context; C-03 checks
  verbatim use; C-19 checks that the template is structurally wired to C-15's declaration,
  making the binding architectural rather than coincidental. Signal: V-02, C-03 evidence
  ("stage tables reference `[incumbent from CAMPAIGN OPEN]`").

- **C-20 (2 pts)** -- Artifact files carry Displacement read field. Extends C-16
  (per-stage Displacement read fields in stage output) to the written artifact files.
  C-16 checks that each stage declares a displacement synthesis in its output; C-20 checks
  that this synthesis travels into the artifact on disk. Makes displacement evidence
  available to downstream skills without re-reading stage output. Signal: V-03, C-02
  evidence ("websearch, interview, prototype artifacts explicitly include Displacement read").

**Point rebalancing** (aspirational pool stays at 26 pts, total stays at 100):
- C-09: 5 pts -> 3 pts. C-18 covers the Invariant E structural checkpoint that makes
  all dual-lock mechanics architecturally consistent. C-09 remains as the output-level
  check -- did the dual-lock fire when warranted.
- C-10: 5 pts -> 3 pts. C-20 adds artifact-level displacement read as the structural
  mechanism. C-10 remains as the Stage 5 framing output check; C-16 and C-20 are its
  structural predecessors.
- C-11: 3 pts -> 2 pts. C-14, C-18, and C-19 together cover the full two-layer enforcement
  architecture across Invariants D and E and the template binding. C-11 remains as the
  minimum-bar check -- mechanical language at all three checkpoints.
- C-13: 3 pts -> 2 pts. C-17 (prohibition instruction) and C-19 (template binding to
  CAMPAIGN OPEN) are the upstream mechanisms that protect field isolation. C-13 remains
  as the output-level isolation check.

**Structural lineage of new criteria**:
- C-18 extends C-14 (two-layer enforcement) and complements C-07 (11-field handoff table).
- C-19 bridges C-15 (CAMPAIGN OPEN pre-registration) and C-03 (verbatim Invariant D template).
- C-20 extends C-16 (per-stage Displacement read in stage output) toward artifact portability.

### v3 (2026-03-16)

Four new aspirational criteria from R2 excellence signals (C-14, C-15, C-16, C-17).
C-09 reduced 8->5, C-10 reduced 8->5, C-11 reduced 4->3, C-12 reduced 3->2.

### v2 (2026-03-16)

Three new aspirational criteria from R1 excellence signals (C-11, C-12, C-13).
C-09 and C-10 reduced from 13 pts to 8 pts to make room.
