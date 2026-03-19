import os
os.chdir('C:/src/sim')

content = """\
---
skill: quest-rubric
skill_target: prove-topic
date: 2026-03-16
version: 2
prior_version: v1-2026-03-16
---

# Scoring Rubric -- prove-topic (v2)

**Scoring weights**: Essential C-01--C-05 = 10 pts each (50 total) | Recommended C-06--C-08 = 8 pts each (24 total) | Aspirational C-09--C-13 = 26 pts total (see table) | **Grand total = 100**

Golden threshold: all essential pass + composite >= 80.

**v2 changes**: Added C-11, C-12, C-13 from Round 1 excellence signals. Redistributed aspirational weights from 13/13 to 8/8/4/3/3.

---

## Essential Criteria (50 pts total -- must all pass)

### C-01 -- Stage Execution Completeness
- **Weight**: essential (10 pts)
- **Category**: correctness
- **Text**: All six campaign phases execute and declare their named EXIT SIGNAL.
- **Pass condition**: Output contains all six named EXIT SIGNALs in order:
  `gate_open` (Stage 0), `hypothesis_locked` (Stage 1), `websearch_complete` (Stage 2),
  `interview_complete` (Stage 3), `prototype_complete` (Stage 4), `synthesis_complete` (Stage 5).
  Missing or reordered signal = FAIL.

### C-02 -- Artifact Write Confirmation
- **Weight**: essential (10 pts)
- **Category**: behavior
- **Text**: Every required artifact is written to disk and confirmed.
- **Pass condition**: Output contains explicit write confirmations for all six artifacts:
  `{topic}-hypothesis-{date}.md`, `{topic}-websearch-{date}.md`, `{topic}-interview-{date}.md`,
  `{topic}-prototype-{date}.md`, `{topic}-synthesis-{date}.md`, `{topic}-handoff-{date}.md`.
  Any missing confirmation = FAIL.

### C-03 -- Session Invariant D Compliance
- **Weight**: essential (10 pts)
- **Category**: correctness
- **Text**: The displacement-question template is applied verbatim at every incumbent check table in Stages 2, 3, and 4.
- **Pass condition**: Each stage's INCUMBENT CHECK TABLE uses the exact template registered in the SESSION INVARIANTS TABLE:
  Stage 2 template ("Does [evidence item] support the displacement of..."), Stage 3 template
  ("Does [practitioner account] reveal a viable transition path..."), Stage 4 template
  ("Does [prototype result] make a credible case for displacing...").
  Any deviation from registered template wording = FAIL.

### C-04 -- Synthesis Verdict Present
- **Weight**: essential (10 pts)
- **Category**: correctness
- **Text**: Stage 5 produces a well-formed hypothesis verdict with confidence composite.
- **Pass condition**: Stage 5 output contains all three synthesis body fields:
  `hypothesis_verdict` (value is SUPPORTED, PARTIALLY SUPPORTED, or UNSUPPORTED),
  `confidence_composite` (numeric value), and `key_risk` (framed as residual incumbent strength).
  Missing or blank field = FAIL.

### C-05 -- Null Tally Chain Integrity
- **Weight**: essential (10 pts)
- **Category**: correctness
- **Text**: The null tally chain is computed from s2 + s3 + s4 CE verdicts and cross-checked at Stage 4 close and Stage 5.
- **Pass condition**: `null_tally_final` is declared at Stage 4 close with explicit cross-check
  ("Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]").
  Stage 5 reconstructs the chain (S2 -> S3 -> S4 -> null_tally_final) and confirms match.
  Missing cross-check or mismatch without integrity-failure flag = FAIL.

---

## Recommended Criteria (24 pts total -- output is better with these)

### C-06 -- Gate S Scout Loader Executes
- **Weight**: recommended (8 pts)
- **Category**: coverage
- **Text**: ROLE B executes and either confirms scout_loaded = true or halts campaign with CAMPAIGN BLOCKED.
- **Pass condition**: Output shows ROLE B execution with `scout_artifact` field populated (path named or
  stated as not found) and `gate_s_cleared` explicitly set to true or false.
  If false, output must show "CAMPAIGN BLOCKED" and record the blocking step.
  Silent omission of ROLE B = FAIL.

### C-07 -- Handoff Table All 11 Fields With Derivation
- **Weight**: recommended (8 pts)
- **Category**: format
- **Text**: Stage 5 HANDOFF TABLE contains all 11 required fields, each with a [derived from: X] annotation.
- **Pass condition**: HANDOFF TABLE in Stage 5 contains every field from the PRE-COMMITTED HANDOFF SCHEMA:
  scout_anchor, incumbent_threat_locked, hypothesis, counter_hypothesis, s2_ce_verdict, s3_ce_verdict,
  s4_ce_verdict, null_tally_final, co_activation_confirmed, incumbent_defense_closed,
  confidence_composite (11 total, plus schema_compliance_confirmed as confirmation row).
  Every field carries `[derived from: X]` annotation. Any unlabeled field = FAIL.

### C-08 -- Counter-Hypothesis Resolution
- **Weight**: recommended (8 pts)
- **Category**: depth
- **Text**: Stage 5 resolves the counter-hypothesis from Stage 1 with an explicit verdict and citation.
- **Pass condition**: Stage 5 COUNTER-HYPOTHESIS RESOLUTION TABLE contains the counter-hypothesis value
  carried from Stage 1 and assigns a verdict of REFUTED, PARTIALLY REFUTED, or OPEN RISK.
  OPEN RISK triggers one-tier confidence reduction (stated in output).
  Missing table or verdict without citation = FAIL.

---

## Aspirational Criteria (26 pts total -- raise the bar)

### C-09 -- Atomic Dual-Lock Fires When Warranted
- **Weight**: aspirational (8 pts)
- **Category**: behavior
- **Text**: When null_tally_final >= 3, the ATOMIC DUAL-LOCK activates both SESSION INVARIANT A
  (adversarial review) and SESSION INVARIANT B (confidence cap) explicitly.
- **Pass condition**: If null_tally_final >= 3 in the output, Stage 5 declares:
  `co_activation_confirmed: dual_lock_fired`, names the adversarial_reviewer_type registered at
  campaign open, and applies `confidence_composite -= 2` with the hard-cap note.
  If null_tally_final < 3, criterion is satisfied by `co_activation_confirmed: not_triggered`.
  Fired dual-lock without both Lock 1 and Lock 2 = FAIL.

### C-10 -- Incumbent Displacement Framing Throughout
- **Weight**: aspirational (8 pts)
- **Category**: depth
- **Text**: Every evidence item across all three check tables explicitly argues for or against
  displacement of the incumbent -- not merely describing the topic.
- **Pass condition**: Stage 2, 3, and 4 INCUMBENT CHECK TABLES each contain at least one Yes verdict
  (or a stated reason all are Inconclusive/No), and the Stage 5 `evidence_summary` cites the
  Stage 4 displacement verdict explicitly ("Stage 4 displacement verdict: [Yes/No/Pending]").
  Generic summaries without displacement framing = FAIL.

### C-11 -- Invariant Enforcement Language is Mechanical, Not Advisory
- **Weight**: aspirational (4 pts)
- **Category**: correctness
- **Text**: Every SESSION INVARIANT uses explicit hard-failure language at its enforcement checkpoint,
  not advisory phrasing.
- **Pass condition**: At minimum, the enforcement statements for Invariant D (C-03), the null tally
  rule (C-05), and the handoff schema (C-07) use mechanical failure language:
  e.g., "deviation = format error", "mismatch = integrity failure", "unlabeled field = FAIL".
  Soft advisory language ("try to follow", "make sure to", "where possible") at any of these three
  checkpoints = FAIL.
- **Round 1 signal**: V-01 (score 90) kept "Template deviation = format error" and "Mismatch =
  integrity failure" intact across a format change. V-03 (score 62) softened these to advisory
  phrasing and lost three essential PARTIALs. The enforcement language is the structural mechanism
  -- not incidental style.

### C-12 -- SESSION INVARIANTS Registered in Standalone Pre-Stage Block
- **Weight**: aspirational (3 pts)
- **Category**: format
- **Text**: All SESSION INVARIANTS appear in a dedicated named block before Stage 0 executes, in
  addition to any inline references within stage bodies.
- **Pass condition**: Output contains a named SESSION INVARIANTS section (TABLE or LIST) that appears
  before Stage 0s `gate_open` EXIT SIGNAL, enumerates all active invariants (A through D at minimum),
  and states each invariants activation condition. Invariants appearing only inline within stage
  bodies, without a standalone pre-stage registration block = FAIL.
- **Round 1 signal**: V-02 (score 76) compressed the preamble and embedded invariants inline,
  causing C-03 and C-05 to degrade to PARTIAL. The standalone pre-stage block forces verbatim
  attention before execution begins and is the structural precondition for essential compliance.

### C-13 -- Stage 5 Synthesis Fields Isolated as Named Declarations
- **Weight**: aspirational (3 pts)
- **Category**: format
- **Text**: `hypothesis_verdict`, `confidence_composite`, and `key_risk` each appear as explicitly
  labeled standalone field declarations in Stage 5 -- not embedded within prose paragraphs.
- **Pass condition**: Each of the three fields appears as a labeled key-value pair
  (e.g., `hypothesis_verdict: SUPPORTED`, `confidence_composite: 7`, `key_risk: [text]`)
  that can be extracted by pattern-matching without reading surrounding prose.
  Any field identifiable only by reading prose context = FAIL.
- **Round 1 signal**: V-04 (score 85) showed inertia framing can bury `confidence_composite` and
  `key_risk` as sub-items of a narrative frame. C-04 checks presence; C-13 checks isolation.
  An output can pass C-04 (fields present) while failing C-13 (fields not extractable).

---

## Scoring Summary

| ID   | Text (short)                               | Weight       | Pts | Category    |
|------|--------------------------------------------|--------------|-----|-------------|
| C-01 | All 6 EXIT SIGNALs declared in order      | essential    |  10 | correctness |
| C-02 | All 6 artifacts written + confirmed       | essential    |  10 | behavior    |
| C-03 | Session Invariant D verbatim at S2/3/4    | essential    |  10 | correctness |
| C-04 | Synthesis verdict + confidence present    | essential    |  10 | correctness |
| C-05 | Null tally chain cross-checked            | essential    |  10 | correctness |
| C-06 | Gate S scout loader executes              | recommended  |   8 | coverage    |
| C-07 | Handoff table 11 fields + derivations     | recommended  |   8 | format      |
| C-08 | Counter-hypothesis resolved with verdict  | recommended  |   8 | depth       |
| C-09 | Atomic dual-lock fires when warranted     | aspirational |   8 | behavior    |
| C-10 | Incumbent displacement framing throughout | aspirational |   8 | depth       |
| C-11 | Invariant enforcement language mechanical | aspirational |   4 | correctness |
| C-12 | SESSION INVARIANTS in standalone block    | aspirational |   3 | format      |
| C-13 | Stage 5 synthesis fields isolated         | aspirational |   3 | format      |
|      | **Total**                                  |              | 100 |             |

**Formula**: (essential_pass/5 x 50) + (recommended_pass/3 x 24) + (aspirational_pass/5 x 26)
**Golden**: all 5 essential pass + composite >= 80

**v2 notes**:
- C-09 and C-10 reduced from 13 pts to 8 pts to accommodate three new criteria.
- C-11 is the enforcement-language criterion: the mechanism that makes C-03 and C-05 structurally
  robust across format and tone variations. The key differentiator between V-01 (90) and V-03 (62).
- C-12 is the preamble-block criterion: the structural precondition protecting C-03 and C-05 when
  setup is compressed. The failure mode exposed by V-02 (76).
- C-13 separates field isolation from field presence (C-04), targeting the narrative-burial
  failure mode observed in V-04 (85) inertia framing.
"""

out = 'simulations/quest/rubrics/prove-topic-rubric-v2-2026-03-16.md'
with open(out, 'w') as f:
    f.write(content)
print('Written:', out)
