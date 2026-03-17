Written to `simulations/quest/rubrics/prove-topic-rubric-v3-2026-03-16.md`.

---

**Four new aspirational criteria added from R2 excellence signals:**

| ID | Pts | Signal source | What it captures |
|----|-----|---------------|-----------------|
| C-14 | 2 | V-04, V-05 | **Two-layer enforcement** — SESSION INVARIANTS block registers canonical failure labels; inline checkpoints echo them verbatim. Drift is self-incriminating from two directions simultaneously. |
| C-15 | 2 | V-05 | **CAMPAIGN OPEN pre-registration** — `incumbent` and `incumbent_strength` declared before SESSION INVARIANTS block. All Invariant D checks bind to a persistent named context rather than re-establishing it per stage. |
| C-16 | 2 | V-05 | **Per-stage Displacement read fields** — each of Stages 2/3/4 has a dedicated "Displacement read:" synthesis field. Makes INCUMBENT CHECK TABLE feel like evidence toward a conclusion, reducing template-softening pressure. |
| C-17 | 2 | V-03, V-05 | **SYNTHESIS DECLARATIONS prohibition** — Stage 5 section header explicitly states "Do not embed these values in prose sentences." Extends C-13 (isolation in output) to C-17 (instruction that pre-empts narrative burial). |

**Rebalancing:** C-09 8→5, C-10 8→5, C-11 4→3, C-12 3→2. Aspirational pool holds at 26 pts. Total stays 100.

**Structural relationships captured in the notes:** C-14 extends C-11, C-15 complements C-12, C-16 extends C-10, C-17 extends C-13 — each new criterion is the mechanism behind an existing output-level check.
*Category**: behavior
- **Text**: All 6 prove-topic artifacts are written with explicit per-artifact write
  confirmations before the skill closes.
- **Pass condition**: Output confirms file writes for all six artifacts:
  `{topic}-hypothesis-{date}.md`, `{topic}-websearch-{date}.md`,
  `{topic}-interview-{date}.md`, `{topic}-prototype-{date}.md`,
  `{topic}-synthesis-{date}.md`, `{topic}-handoff-{date}.md`.
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

- **Weight**: aspirational (5 pts)
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
  Reduced from 8 pts to 5 pts in v3 as newer criteria (C-14, C-15) capture the
  upstream structural conditions that make dual-lock execution reliable.

### C-10 -- Incumbent Displacement Framing Throughout

- **Weight**: aspirational (5 pts)
- **Category**: depth
- **Text**: Every evidence item across all three check tables explicitly argues for
  or against displacement of the incumbent -- not merely describing the topic.
- **Pass condition**: Stage 2, 3, and 4 INCUMBENT CHECK TABLES each contain at least
  one Yes verdict (or a stated reason all are Inconclusive/No), and the Stage 5
  `evidence_summary` cites the Stage 4 displacement verdict explicitly ("Stage 4
  displacement verdict: [Yes/No/Pending]"). Generic summaries without displacement
  framing = FAIL.
- **v2 signal**: V-05 (richest implementation) added per-stage "Displacement read:"
  fields (now C-16). C-10 checks the framing in outputs; C-16 checks that the
  structural mechanism to produce it was present. Reduced from 8 pts to 5 pts in v3.

### C-11 -- Invariant Enforcement Language is Mechanical, Not Advisory

- **Weight**: aspirational (3 pts)
- **Category**: correctness
- **Text**: Every SESSION INVARIANT uses explicit hard-failure language at its
  enforcement checkpoint, not advisory phrasing.
- **Pass condition**: At minimum, the enforcement statements for Invariant D (C-03),
  the null tally rule (C-05), and the handoff schema (C-07) use mechanical failure
  language: e.g., "deviation = format error", "mismatch = integrity failure",
  "unlabeled field = FAIL". Soft advisory language ("try to follow", "make sure to",
  "where possible") at any of these three checkpoints = FAIL.
- **Round 1 signal**: V-01 (score 90) kept hard-failure language intact across a
  format change. V-03 (score 62) softened to advisory and lost three essential
  PARTIALs. The enforcement language is the structural mechanism, not incidental style.
- **Reduced from 4 pts to 3 pts in v3** to accommodate C-14 (two-layer architecture),
  which captures the stronger form: enforcement labels registered canonically and
  echoed bidirectionally.

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
  standalone invariants block depends on.

### C-13 -- Stage 5 Synthesis Fields Isolated as Named Declarations

- **Weight**: aspirational (3 pts)
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
- **Round 2 signal**: V-04 and V-05 used this architecture. "Two-layer architecture --
  SESSION INVARIANTS TABLE holds failure labels; inline checkpoints echo the exact label
  from the table. Drift at Stage 2 incurs FORMAT ERROR from two structural directions
  simultaneously -- the table and the inline annotation -- making soft deviation
  self-incriminating." Extends C-11 (mechanical language present) with C-14
  (bidirectional registration makes it structurally self-auditing).

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
- **Round 2 signal**: V-05 exclusively. "Registering `incumbent` and
  `incumbent_strength` before any invariant fires establishes the displacement context
  that all subsequent Invariant D checkpoints rely on. Stages then feel like
  displacement tests rather than checkbox tables." Complements C-12 (SESSION INVARIANTS
  block): C-15 is the upstream context that gives the invariants something to bind to.

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
- **Round 2 signal**: V-05 only. "Giving each stage a 'Displacement read:' synthesis
  field makes the INCUMBENT CHECK TABLE feel like evidence toward a conclusion rather
  than a compliance checkbox. Reduces the temptation to soften template wording to
  match a prose-narrative tone." Extends C-10 (displacement framing in output) with
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
- **Round 2 signal**: V-03 and V-05. "Naming the section and stating 'Do not embed
  these values in prose sentences. Each on its own line, extractable by label match.'
  eliminates narrative gravity before evidence_summary begins. C-04 (presence) and
  C-13 (isolation) are simultaneously protected by a single structural insertion."
  Extends C-13 (isolation in output) with C-17 (prohibition instruction that prevents
  narrative burial before it occurs).

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
| C-09 | Atomic dual-lock fires when warranted      | aspirational |   5 | behavior    |
| C-10 | Incumbent displacement framing throughout  | aspirational |   5 | depth       |
| C-11 | Invariant enforcement language mechanical  | aspirational |   3 | correctness |
| C-12 | SESSION INVARIANTS in standalone block     | aspirational |   2 | format      |
| C-13 | Stage 5 synthesis fields isolated          | aspirational |   3 | format      |
| C-14 | Two-layer enforcement architecture         | aspirational |   2 | correctness |
| C-15 | CAMPAIGN OPEN pre-registers displacement   | aspirational |   2 | format      |
| C-16 | Per-stage Displacement read fields         | aspirational |   2 | depth       |
| C-17 | SYNTHESIS DECLARATIONS explicit prohibition| aspirational |   2 | format      |
|      | **Total**                                    |              | 100 |             |

**Essential** (50 pts): C-01 through C-05, 10 pts each.
**Recommended** (24 pts): C-06 through C-08, 8 pts each.
**Aspirational** (26 pts): C-09 (5) + C-10 (5) + C-11 (3) + C-12 (2) + C-13 (3)
  + C-14 (2) + C-15 (2) + C-16 (2) + C-17 (2) = 26 pts across 9 criteria.

**Formula**: sum of individual criterion scores (PASS = full, PARTIAL = half rounded down, FAIL = 0).
**Golden**: all 5 essential PASS + composite >= 80.

---

## Version Notes

### v3 (2026-03-16)

**Four new aspirational criteria from R2 excellence signals**:

- **C-14 (2 pts)** -- Two-layer enforcement architecture. Extends C-11: where C-11
  requires mechanical language, C-14 requires that the canonical labels are registered
  in the SESSION INVARIANTS block AND echoed verbatim inline -- making any label drift
  self-incriminating from two directions. Signal: V-04 and V-05 both used this;
  neither reached below 100.

- **C-15 (2 pts)** -- CAMPAIGN OPEN pre-registers displacement context. Complements
  C-12: where C-12 requires a standalone SESSION INVARIANTS block, C-15 requires a
  CAMPAIGN OPEN block that comes before it, establishing `incumbent` and
  `incumbent_strength` as a persistent named context. Signal: V-05 exclusively; the
  only variation with organic-feeling displacement tests rather than checkbox tables.

- **C-16 (2 pts)** -- Per-stage Displacement read fields. Extends C-10: where C-10
  checks displacement framing appears in the Stage 5 summary, C-16 checks that each
  of Stages 2/3/4 has a dedicated synthesis field summarizing its displacement verdict.
  The structural mechanism that reduces Invariant D template-softening pressure.
  Signal: V-05 only.

- **C-17 (2 pts)** -- SYNTHESIS DECLARATIONS explicit prohibition. Extends C-13: where
  C-13 checks that synthesis fields are isolated in the output, C-17 checks that the
  prompt contains an explicit prohibition against prose embedding. Protects both C-04
  (presence) and C-13 (isolation) via a single pre-emptive instruction. Signal:
  V-03 and V-05; strongest C-13 implementations across R1 and R2.

**Point rebalancing** (aspirational pool stays at 26 pts, total stays at 100):
- C-09: 8 pts -> 5 pts (two-layer architecture and CAMPAIGN OPEN are the upstream
  conditions; dual-lock execution flows from them when they are present).
- C-10: 8 pts -> 5 pts (per-stage Displacement read fields, now C-16, is the
  structural mechanism; C-10 checks the output framing it produces).
- C-11: 4 pts -> 3 pts (C-14 captures the stronger form; C-11 remains as the
  minimum-bar check).
- C-12: 3 pts -> 2 pts (C-15 captures the complementary upstream block; C-12 remains
  as the standalone-registration check).
- C-13: unchanged at 3 pts (C-17 extends it rather than replacing it).

### v2 (2026-03-16)

Three new aspirational criteria from R1 excellence signals (C-11, C-12, C-13).
C-09 and C-10 reduced from 13 pts to 8 pts to make room.
