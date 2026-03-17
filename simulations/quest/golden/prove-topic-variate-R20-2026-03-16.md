---
skill: quest-variate
skill_target: prove-topic
round: R20
date: 2026-03-16
rubric: prove-topic-rubric-v19-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [stage4_body_confidence_echo, chain_table_verdict_vocabulary, dual_chain_bridge_declaration]
  combined: [V-04 (stage4_body_confidence_echo + chain_table_verdict_vocabulary), V-05 (all_three + full_R19_V05_stack)]
r19_anchor: >
  R19 V-05 established three patterns now codified as C-21 and C-22 in v19:
  C-21 (Stage 4 tri-value exit — count + running_confidence + displacement_momentum_final
  simultaneously; the only stage where both chains have resolved final values),
  C-22 (per-row VERDICT in THREE-STAGE DISPLACEMENT CHAIN with SUPPORTED / PARTIALLY
  SUPPORTED / NOT SUPPORTED vocabulary, not Y/N/Inc shorthand).
  Denominator updates to 14 in v19. V-03 under v19 scores 83.55.
r20_context: >
  R19 V-05 achieves C-08, C-12, C-19 (full), C-20 (partial) but C-21 and C-22 remain
  fails. Exact failure modes:

  C-21 fails because running_confidence appears in the exit signal parameter syntax
  (prototype_complete(count=N, confidence=C, momentum_final=M)) but drops out of the
  body text. The body line reads "s4_count = [N]. s4_ce_verdict = [value].
  null_tally_final = [N]. displacement_momentum_final = [value]." — running_confidence
  is absent from the prose. The rubric requires all three values to appear simultaneously
  in the exit signal body, bridging both chains in one signal.

  C-22 fails because the THREE-STAGE DISPLACEMENT CHAIN VERDICT column uses [Y/N/Inc]
  shorthand. The rubric requires SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED per row.
  chain_pattern names the arc but does not substitute for the per-stage stance.

  V-01 (single: stage4_body_confidence_echo): Add running_confidence = [value] to Stage 4
  EXIT SIGNAL body text between count and displacement_momentum_final. One-line addition to
  the body prose. Does not disturb any other structural criteria.

  V-02 (single: chain_table_verdict_vocabulary): Rename THREE-STAGE DISPLACEMENT CHAIN
  VERDICT column to STANCE. Change [Y/N/Inc] to [SUPPORTED / PARTIALLY SUPPORTED / NOT
  SUPPORTED]. Add enforcement note: "Valid STANCE values: SUPPORTED / PARTIALLY SUPPORTED /
  NOT SUPPORTED. Y/N shorthand = format error." chain_pattern naming stays unchanged.

  V-03 (single: dual_chain_bridge_declaration): C-21 also requires Stage 4 to be declared
  as the only stage where both chains reach final. V-03 adds a CHAIN BRIDGE block inside
  Stage 4 body (after displacement_momentum_final computation) that explicitly marks
  confidence_chain_final and displacement_chain_final as resolved, and adds bridge_declared
  to the Stage 4 exit signal. This converts C-21 from a value-listing pass to a structural
  declaration pass.

  V-04 (combined: stage4_body_confidence_echo + chain_table_verdict_vocabulary): V-01 + V-02.
  Tests whether closing both C-21 and C-22 simultaneously (without bridge declaration) is
  sufficient for PASS on both criteria.

  V-05 (full: all three + complete R19 V-05 stack): V-01 + V-02 + V-03 on top of the full
  R19 V-05 baseline — RESUME AUDIT, count-gated exits, dual-field entry validation (C-18),
  TRAJECTORY COMPUTE STEP (C-19), THREE-STAGE DISPLACEMENT CHAIN (C-20), DEPENDENCY column
  (C-17), ATOMIC DUAL-LOCK, three-block Stage 5.
---

# prove-topic Variations — Round 20 (rubric v19)

**Skill**: prove-topic
**Rubric**: v19 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-22 aspirational)
**Date**: 2026-03-16
**Round**: R20

---

## Context: what informed this round

R19 V-05 is the structural floor for all R20 variations. The v19 rubric codified two new
criteria from R19 excellence patterns. Both remain fails in R19 V-05:

| Criterion | Failure mode | R20 target |
|-----------|-------------|-----------|
| C-21 (Stage 4 tri-value exit) | running_confidence present in exit signal params but absent from body text | V-01, V-03, V-04, V-05 |
| C-22 (per-row STANCE in DISPLACEMENT CHAIN) | VERDICT column uses Y/N/Inc shorthand, not SUPPORTED vocabulary | V-02, V-04, V-05 |

V-03 explores a deeper C-21 expression: a structural CHAIN BRIDGE declaration that marks
Stage 4 as the convergence point of both chains, not just a value-listing fix.

---

## V-01 — Stage 4 Body Confidence Echo

**Axis**: stage4_body_confidence_echo (single)
**Hypothesis**: C-21 fails because running_confidence appears in the exit signal parameter
syntax but is absent from the body text. The body line only carries count, ce_verdict,
null_tally_final, and displacement_momentum_final. Adding one explicit
`running_confidence = [value].` line to the Stage 4 exit signal body — positioned between
count and displacement_momentum_final — will achieve C-21 PASS without disturbing any
other structural criterion. The parameter syntax already names it; the body just needs to
echo it.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---
depth: standard
confidence: standard
for: {value}
iterations: 1

Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign builds the case for displacing {status_quo_comparator} with {topic}.
Six stages (Stage 0 = gate, Stages 1-5 = evidence + synthesis). Each stage has numbered
ENTRY CONDITIONS and a named EXIT SIGNAL. No stage body begins until entry conditions confirm.

---

## CAMPAIGN OPEN

  topic:                 {topic}
  date:                  {date}
  status_quo_comparator: [name the incumbent approach this topic must displace]

### INCUMBENT ANCHOR

Fill before any role or invariant registration.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS TABLE

SESSION INVARIANT D leads. All invariants carry: "cannot be modified or bypassed at
any subsequent stage." Register all four before roles execute.

  ID   | NAME                      | DECLARATION
  -----|---------------------------|------------------------------------------------------
  D    | INCUMBENT CHECK PHRASING  | Stage 2: "Does [evidence item] support the displacement
       | REGISTER                  |   of {status_quo_comparator} by {topic} on [dimension]?
       |                           |   [Yes / No / Inconclusive]"
       |                           | Stage 3: "Does [practitioner account] reveal a viable
       |                           |   transition path from {status_quo_comparator} to
       |                           |   {topic} for [use case]? [Yes / No / Inconclusive]"
       |                           | Stage 4: "Does [prototype result] make a credible case
       |                           |   for displacing {status_quo_comparator} with {topic}?
       |                           |   [Yes / No / Pending]"
       |                           | Enforcement: Template deviation = format error.
       |                           | Cannot be modified or bypassed at any stage.
  -----|---------------------------|------------------------------------------------------
  A    | ADVERSARIAL REVIEWER      | adversarial_reviewer_type: [role most likely to
       | TYPE                      |   challenge the displacement claim].
       |                           | Activation: null_tally_final >= 3.
       |                           | Cannot be modified or bypassed at synthesis.
  -----|---------------------------|------------------------------------------------------
  B    | CONFIDENCE CAP            | null_ce_cap_rule: confidence_composite -= 2 if
       |                           |   null_tally_final >= 3 (hard cap).
       |                           | Cannot be softened or overridden at synthesis.
  -----|---------------------------|------------------------------------------------------
  C    | DERIVATION ANNOTATION     | annotation_rule: Every handoff field carries
       |                           |   [derived from: X]. Unlabeled = format error.
       |                           | Cannot be modified or bypassed at synthesis.

### ROLE OWNERSHIP TABLE

ROLE C executes first. Roles run in sequence C -> B -> A before Stage 0 begins.

  ROLE   | TITLE                    | OWNED FIELD               | GATE S STEP | EXECUTE
  -------|--------------------------|---------------------------|-------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | Step 1      | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared            | Step 2      | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3   | THIRD

ROLE C execution (fill now):
  Reads INCUMBENT ANCHOR above. Confirms analysis complete.
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  Confirms all four SESSION INVARIANT TABLE rows filled and active.
  invariant_registry_confirmed: [true when all four invariants registered]

### CE VERDICT OWNERSHIP TABLE

  FIELD            | OWNED BY      | FORMULA
  -----------------|---------------|-----------------------------------------------------
  s2_ce_verdict    | Stage 2       | null if no CE; citation if CE found
  s3_ce_verdict    | Stage 3       | null if no CE; citation if CE found
  s4_ce_verdict    | Stage 4       | null if no CE; description if CE found
  null_tally_final | Stage 4 close | count(null) across s2 + s3 + s4

NULL TALLY CHAIN RULE (locked): Running tally from Stage 2. Stage 4 close reconstructs
full chain. ATOMIC DUAL-LOCK cross-checks at synthesis. Mismatch = integrity failure.

### PRE-COMMITTED HANDOFF SCHEMA TABLE

  FIELD                      | DERIVATION SOURCE                         | IND. CHAIN
  ---------------------------|-------------------------------------------|------------------
  scout_anchor               | ROLE B scout load                         | n/a
  incumbent_threat_locked    | ROLE C analysis                           | n/a
  hypothesis                 | Stage 1 artifact                          | n/a
  counter_hypothesis         | Stage 1 artifact                          | n/a
  s2_ce_verdict              | Stage 2 artifact                          | n/a
  s3_ce_verdict              | Stage 3 artifact                          | n/a
  s4_ce_verdict              | Stage 4 artifact                          | n/a
  null_tally_final           | s2+s3+s4 CE verdicts                      | not through co_activation
  co_activation_confirmed    | ATOMIC DUAL-LOCK                          | not through incumbent_defense
  incumbent_defense_closed   | s2+s3+s4 direct chain                     | not through co_activation
  confidence_composite       | Stage 5 minus reductions                  | capped by B

---

## RESUME AUDIT

Run this block before Stage 0. Glob existing artifacts for {topic} on {date}.

ARTIFACT SCAN:
  STAGE | ARTIFACT PATTERN                                       | FOUND (Y/N) | DECISION
  ------|--------------------------------------------------------|-------------|------------------
  1     | simulations/prove/{topic}-hypothesis-{date}.md        | [Y/N]       | [RESUME-SKIP / RUN]
  2     | simulations/prove/{topic}-websearch-{date}.md         | [Y/N]       | [RESUME-SKIP / RUN]
  3     | simulations/prove/{topic}-interview-{date}.md         | [Y/N]       | [RESUME-SKIP / RUN]
  4     | simulations/prove/{topic}-prototype-{date}.md         | [Y/N]       | [RESUME-SKIP / RUN]
  5     | simulations/prove/{topic}-synthesis-{date}.md         | [Y/N]       | [RESUME-SKIP / RUN]

  resume_audit_complete: [true]
  stages_to_run:         [list of stages with RUN decision, or ALL if none found]

RESUME AUDIT EXIT:
  If all five stages are RESUME-SKIP: emit "RESUME_AUDIT_EXIT — All stage artifacts
  already present on disk. Campaign complete. No stages will re-run." and STOP.
  Otherwise: "RESUME_AUDIT_PASS — Stages to run: [list]. Proceeding to Stage 0."

---

## STAGE 0 — GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] RESUME AUDIT completed — resume_audit_complete = true
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] SESSION INVARIANTS TABLE complete — all four rows filled
  [ ] ROLE C executed — incumbent_threat_locked = true
  [ ] ROLE B executed — scout_artifact identified and scout_loaded confirmed
  [ ] ROLE A executed — invariant_registry_confirmed = true

STAGE 0 BODY:

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|--------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]

  First BLOCKED step halts campaign. Record step and owning role.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open — Steps 1, 2, 3 all confirmed. SESSION INVARIANT D active.
   Advancing to Stage 1."

---

## STAGE 1 — HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] RESUME AUDIT: Stage 1 = RUN
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered

STAGE 1 BODY:
Load scout artifact. Read signals. Frame hypothesis.

  source_scout_artifact:        [path from ROLE B — copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense — grounded in ROLE C analysis]
  confidence_prior:             [1-10 numeric — initial estimate before evidence]
  gate_s_cleared:               [true — from GATE S Step 2]
  invariant_registry_confirmed: [true — from GATE S Step 3]
  incumbent_threat_locked:      [true — from GATE S Step 1]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked
  "STAGE 1 EXIT: hypothesis_locked — {topic}-hypothesis-{date}.md written. Stage 2 ready."

---

## STAGE 2 — WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked
  [ ] RESUME AUDIT: Stage 2 = RUN
  [ ] hypothesis artifact confirmed written
  [ ] SESSION INVARIANT D Stage 2 template active

STAGE 2 BODY:
Gather minimum 5 external sources.

INCUMBENT CHECK TABLE — Stage 2 (SESSION INVARIANT D verbatim; DISPLACEMENT DELTA column):

  ITEM | SOURCE (URL or citation) | SUMMARY (1 sentence) | TEMPLATE APPLIED & VERDICT        | DISP DELTA (-2 to +2)
  -----|--------------------------|----------------------|-----------------------------------|-----------------------
  1    | [source]                 | [summary]            | "Does [item] support displacement | [delta]
  2    | [source]                 | [summary]            |  of [comp] by [topic] on [dim]?   | [delta]
  3    | [source]                 | [summary]            |  [Yes / No / Inconclusive]"       | [delta]
  4    | [source]                 | [summary]            | (fill each row verbatim)          | [delta]
  5    | [source]                 | [summary]            |                                   | [delta]

  s2_count:                   [N] — must be >= 5
  s2_displacement_delta_sum:  [sum of DISP DELTA column]
  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]
  s2_confidence_delta:        [+/- numeric]
  running_confidence:         [confidence_prior + s2_confidence_delta]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."
SCHEMA INTEGRITY: handoff fields populated per PRE-COMMITTED HANDOFF SCHEMA TABLE.
Write artifact: {topic}-websearch-{date}.md. Confirm write.

GATE INSTRUCTION: Do not fire exit signal until s2_count >= 5.
If s2_count < 5, gather additional external sources before proceeding.

STAGE 2 EXIT SIGNAL: websearch_complete(count=[N], confidence=[running_confidence], momentum=[displacement_momentum])
  "STAGE 2 EXIT: websearch_complete — s2_count = [N] (gate: >= 5 met).
   s2_ce_verdict = [value]. running_confidence = [value]. Stage 3 ready."

---

## STAGE 3 — INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete
  [ ] RESUME AUDIT: Stage 3 = RUN
  [ ] s2_ce_verdict recorded
  [ ] Read {topic}-websearch-{date}.md from disk. Extract running_confidence.
      Validate against signal payload. Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 3 template active

STAGE 3 BODY:
Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE — Stage 3 (SESSION INVARIANT D verbatim; DISPLACEMENT DELTA column):

  PRACTITIONER | KEY ACCOUNT (1 sentence)  | TEMPLATE APPLIED & VERDICT                    | DISP DELTA
  -------------|---------------------------|-----------------------------------------------|-----------
  [type 1]     | [quote or paraphrase]     | "Does [account] reveal a viable transition     | [delta]
  [type 2]     | [quote or paraphrase]     |  path from [comp] to [topic] for [use case]?  | [delta]
  [type 3]     | [quote or paraphrase]     |  [Yes / No / Inconclusive]"                   | [delta]

  s3_count:                    [N] — must be >= 3
  s3_displacement_delta_sum:   [sum of DISP DELTA column]
  s3_incumbent_check_summary:  [N support / M counter / P inconclusive]
  s3_ce_verdict:               [null if no CE; cite account if found]
  s3_confidence_delta:         [+/- numeric]
  running_confidence:          [prior + s3_confidence_delta]
  displacement_momentum:       [s2_displacement_delta_sum + s3_displacement_delta_sum]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."
Write artifact: {topic}-interview-{date}.md. Confirm write.

GATE INSTRUCTION: Do not fire exit signal until s3_count >= 3.
If s3_count < 3, simulate additional practitioner interviews before proceeding.

STAGE 3 EXIT SIGNAL: interview_complete(count=[N], confidence=[running_confidence], momentum=[displacement_momentum])
  "STAGE 3 EXIT: interview_complete — s3_count = [N] (gate: >= 3 met).
   s3_ce_verdict = [value]. running_confidence = [value]. Stage 4 ready."

---

## STAGE 4 — PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete(count=N, confidence=C, momentum=M)
  [ ] RESUME AUDIT: Stage 4 = RUN
  [ ] s3_ce_verdict recorded
  [ ] Read {topic}-interview-{date}.md from disk. Extract running_confidence AND
      displacement_momentum. Validate both against signal payload.
      Mismatch on either = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 4 template active

STAGE 4 BODY:
Design and assess prototype experiments.

  prototype_design:   [brief description]
  prototype_result:   [what was learned — 1-3 sentences]

INCUMBENT CHECK TABLE — Stage 4 (SESSION INVARIANT D verbatim; DISPLACEMENT DELTA column):

  ITEM       | RESULT           | TEMPLATE APPLIED & VERDICT                    | DISP DELTA
  -----------|------------------|-----------------------------------------------|-----------
  prototype  | [prototype_result] | "Does [result] make a credible case for     | [delta]
             |                  |  displacing [comp] with [topic]?              |
             |                  |  [Yes / No / Pending]"                        |

  s4_count:                    [N] — must be >= 3
  s4_displacement_delta_sum:   [delta for Stage 4]
  s4_displacement_verdict:     [Yes / No / Pending] — required; omission = format error
  s4_ce_verdict:               [null / description]
  s4_confidence_delta:         [+/- numeric]
  running_confidence:          [prior + s4_confidence_delta]
  displacement_momentum_final: [displacement_momentum + s4_displacement_delta_sum]

Final null tally:
  null_tally_final = [N]
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

GATE INSTRUCTION: Do not fire exit signal until s4_count >= 3.
If s4_count < 3, design additional prototype experiments before proceeding.

Write artifact: {topic}-prototype-{date}.md. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[N], confidence=[running_confidence], momentum_final=[displacement_momentum_final])
  "STAGE 4 EXIT: prototype_complete — s4_count = [N] (gate: >= 3 met).
   running_confidence = [value]. s4_ce_verdict = [value]. null_tally_final = [N].
   displacement_momentum_final = [value]. Stage 5 ready."

---

## STAGE 5 — SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete(count=N, confidence=C, momentum_final=M)
  [ ] RESUME AUDIT: Stage 5 = RUN
  [ ] Read {topic}-prototype-{date}.md from disk. Extract running_confidence AND
      displacement_momentum_final. Validate both against signal payload.
      Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 present for resolution
  [ ] All four SESSION INVARIANT TABLE rows active

STAGE 5 BODY:

### BLOCK 1 — CONFIDENCE CHAIN RESOLUTION

  prior:            [confidence_prior from Stage 1]
  s2_delta:         [s2_confidence_delta]
  s3_delta:         [s3_confidence_delta]
  s4_delta:         [s4_confidence_delta]
  chain_equation:   prior + s2_delta + s3_delta + s4_delta = [final]
  confidence_composite: [final — before counter-hypothesis and cap adjustments]

### BLOCK 2 — COUNTER-HYPOTHESIS RESOLUTION

  COUNTER_HYPOTHESIS     | VERDICT                                  | EVIDENCE
  -----------------------|------------------------------------------|-------------------
  [from Stage 1]         | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite stage artifact]
  [add rows as needed]   |                                          |

OPEN RISK: reduce confidence_composite one tier before BLOCK 3.

ORDER CONSTRAINT (C-17): If BLOCK 1 requires cr_delta produced by BLOCK 2 resolution,
execute BLOCK 2 before BLOCK 1 and annotate inversion with this ORDER CONSTRAINT statement.

### BLOCK 3 — DISPLACEMENT INTEGRITY CHECK

NULL TALLY CHAIN reconstruction:
  S2 -> [s2_ce_verdict: null or value]
  S3 -> [s3_ce_verdict: null or value]
  S4 -> [s4_ce_verdict: null or value]
  null_tally_final = [N]
  Cross-check vs Stage 4 exit count: [Match / Mismatch — record mismatch before continuing]

If null_tally_final >= 3:
  Lock 1 (SESSION INVARIANT A): adversarial review by [adversarial_reviewer_type]. BLOCKED.
  Lock 2 (SESSION INVARIANT B): confidence_composite -= 2 (hard cap, cannot be softened).
  co_activation_confirmed: dual_lock_fired
Else:
  co_activation_confirmed: not_triggered

THREE-STAGE DISPLACEMENT CHAIN (C-20):

  STAGE | DISP DELTA SUM | CUMULATIVE MOMENTUM | INCUMBENT DELTA SUM | VERDICT     | FLAG?
  ------|----------------|---------------------|---------------------|-------------|------
  S2    | [s2_disp_sum]  | [s2_cumul]          | [running sum at S2] | [Y/N/Inc]   | [Y/N]
  S3    | [s3_disp_sum]  | [s3_cumul]          | [running sum at S3] | [Y/N/Inc]   | [Y/N]
  S4    | [s4_disp_sum]  | [s4_cumul]          | [running sum at S4] | [Y/N/Inc]   | [Y/N]

  chain_pattern: [ACCELERATING / STEADY_BUILD / PLATEAU / LATE_REVERSAL / PEAK_THEN_DROP / ...]
  FLAG rule: any stage where verdict runs counter to adjacent stage verdicts = FLAG = Y.
  Each FLAG requires conclusion_justification before synthesis closes.

TRAJECTORY COMPUTE STEP (C-19 — execute before displacement_conclusion is set):

  Delta sequence: S2=[s2_disp_sum], S3=[s3_disp_sum], S4=[s4_disp_sum]
  trajectory_direction computation:
    IF S3_delta >= S2_delta AND S4_delta >= S3_delta: ACCELERATING
    IF S3_delta < S2_delta OR S4_delta < S3_delta:    DECELERATING
    ELSE (all deltas within +/- 0.5):                 FLAT

  trajectory_direction: [ACCELERATING / DECELERATING / FLAT]

CEILING RULE (hard constraint — not editorial note):
  IF trajectory_direction = DECELERATING:
    displacement_conclusion <= PARTIALLY SUPPORTED
    (ceiling holds even if displacement_momentum_final > 0)
  IF trajectory_direction = ACCELERATING:
    displacement_conclusion may reach SUPPORTED if evidence warrants
  IF trajectory_direction = FLAT:
    displacement_conclusion ceiling = direction of displacement_momentum_final

  trajectory_ceiling_applied: [true / false]
  displacement_conclusion:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
    Cannot exceed ceiling set by trajectory_direction.

  conclusion_justification: [required if any FLAG = Y or trajectory ceiling applied]
  incumbent_defense_closed: [true when all flagged rows reconciled]

### SYNTHESIS BODY

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences integrating Stages 2, 3, 4 — with explicit
                           incumbent displacement verdict from Stage 4 check]
  confidence_composite:  [final value after all adjustments]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### HANDOFF TABLE

SESSION INVARIANT C enforced. All fields carry [derived from: X]. Unlabeled = format error.

  FIELD                      | VALUE   | DERIVATION                                  | IND. CHAIN
  ---------------------------|---------|---------------------------------------------|------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]           | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]             | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]            | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]            | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]            | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]            | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]            | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4 CE verdicts]        | not through co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]            | not through incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct chain]       | not through co_activation
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]           | capped by INV B
  schema_compliance_confirmed| [true]  | [all 11 fields, sources match]              | n/a

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete — Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-02 — Chain Table Verdict Vocabulary

**Axis**: chain_table_verdict_vocabulary (single)
**Hypothesis**: C-22 fails because the THREE-STAGE DISPLACEMENT CHAIN table VERDICT column
uses [Y/N/Inc] shorthand. The rubric requires SUPPORTED / PARTIALLY SUPPORTED / NOT
SUPPORTED per row, with chain_pattern naming the arc but not substituting for the per-stage
stance. V-02 renames the column STANCE and replaces the shorthand values with the required
vocabulary. An enforcement note is added: "Valid STANCE values: SUPPORTED / PARTIALLY
SUPPORTED / NOT SUPPORTED. Y/N shorthand = format error." All other structure is unchanged
from R19 V-05.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---
depth: standard
confidence: standard
for: {value}
iterations: 1

Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign builds the case for displacing {status_quo_comparator} with {topic}.
Six stages (Stage 0 = gate, Stages 1-5 = evidence + synthesis). Each stage has numbered
ENTRY CONDITIONS and a named EXIT SIGNAL. No stage body begins until entry conditions confirm.

---

## CAMPAIGN OPEN

  topic:                 {topic}
  date:                  {date}
  status_quo_comparator: [name the incumbent approach this topic must displace]

### INCUMBENT ANCHOR

Fill before any role or invariant registration.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS TABLE

SESSION INVARIANT D leads. All invariants carry: "cannot be modified or bypassed at
any subsequent stage." Register all four before roles execute.

  ID   | NAME                      | DECLARATION
  -----|---------------------------|------------------------------------------------------
  D    | INCUMBENT CHECK PHRASING  | Stage 2: "Does [evidence item] support the displacement
       | REGISTER                  |   of {status_quo_comparator} by {topic} on [dimension]?
       |                           |   [Yes / No / Inconclusive]"
       |                           | Stage 3: "Does [practitioner account] reveal a viable
       |                           |   transition path from {status_quo_comparator} to
       |                           |   {topic} for [use case]? [Yes / No / Inconclusive]"
       |                           | Stage 4: "Does [prototype result] make a credible case
       |                           |   for displacing {status_quo_comparator} with {topic}?
       |                           |   [Yes / No / Pending]"
       |                           | Enforcement: Template deviation = format error.
       |                           | Cannot be modified or bypassed at any stage.
  -----|---------------------------|------------------------------------------------------
  A    | ADVERSARIAL REVIEWER      | adversarial_reviewer_type: [role most likely to
       | TYPE                      |   challenge the displacement claim].
       |                           | Activation: null_tally_final >= 3.
       |                           | Cannot be modified or bypassed at synthesis.
  -----|---------------------------|------------------------------------------------------
  B    | CONFIDENCE CAP            | null_ce_cap_rule: confidence_composite -= 2 if
       |                           |   null_tally_final >= 3 (hard cap).
       |                           | Cannot be softened or overridden at synthesis.
  -----|---------------------------|------------------------------------------------------
  C    | DERIVATION ANNOTATION     | annotation_rule: Every handoff field carries
       |                           |   [derived from: X]. Unlabeled = format error.
       |                           | Cannot be modified or bypassed at synthesis.

### ROLE OWNERSHIP TABLE

ROLE C executes first. Roles run in sequence C -> B -> A before Stage 0 begins.

  ROLE   | TITLE                    | OWNED FIELD               | GATE S STEP | EXECUTE
  -------|--------------------------|---------------------------|-------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | Step 1      | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared            | Step 2      | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3   | THIRD

ROLE C execution (fill now):
  Reads INCUMBENT ANCHOR above. Confirms analysis complete.
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  Confirms all four SESSION INVARIANT TABLE rows filled and active.
  invariant_registry_confirmed: [true when all four invariants registered]

### CE VERDICT OWNERSHIP TABLE

  FIELD            | OWNED BY      | FORMULA
  -----------------|---------------|-----------------------------------------------------
  s2_ce_verdict    | Stage 2       | null if no CE; citation if CE found
  s3_ce_verdict    | Stage 3       | null if no CE; citation if CE found
  s4_ce_verdict    | Stage 4       | null if no CE; description if CE found
  null_tally_final | Stage 4 close | count(null) across s2 + s3 + s4

NULL TALLY CHAIN RULE (locked): Running tally from Stage 2. Stage 4 close reconstructs
full chain. ATOMIC DUAL-LOCK cross-checks at synthesis. Mismatch = integrity failure.

---

## RESUME AUDIT

Run this block before Stage 0. Glob existing artifacts for {topic} on {date}.

ARTIFACT SCAN:
  STAGE | ARTIFACT PATTERN                                       | FOUND (Y/N) | DECISION
  ------|--------------------------------------------------------|-------------|------------------
  1     | simulations/prove/{topic}-hypothesis-{date}.md        | [Y/N]       | [RESUME-SKIP / RUN]
  2     | simulations/prove/{topic}-websearch-{date}.md         | [Y/N]       | [RESUME-SKIP / RUN]
  3     | simulations/prove/{topic}-interview-{date}.md         | [Y/N]       | [RESUME-SKIP / RUN]
  4     | simulations/prove/{topic}-prototype-{date}.md         | [Y/N]       | [RESUME-SKIP / RUN]
  5     | simulations/prove/{topic}-synthesis-{date}.md         | [Y/N]       | [RESUME-SKIP / RUN]

  resume_audit_complete: [true]
  stages_to_run:         [list of stages with RUN decision, or ALL if none found]

RESUME AUDIT EXIT:
  If all five stages are RESUME-SKIP: emit "RESUME_AUDIT_EXIT — All stage artifacts
  already present on disk. Campaign complete. No stages will re-run." and STOP.
  Otherwise: "RESUME_AUDIT_PASS — Stages to run: [list]. Proceeding to Stage 0."

---

## STAGE 0 — GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] RESUME AUDIT completed — resume_audit_complete = true
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] SESSION INVARIANTS TABLE complete — all four rows filled
  [ ] ROLE C executed — incumbent_threat_locked = true
  [ ] ROLE B executed — scout_artifact identified and scout_loaded confirmed
  [ ] ROLE A executed — invariant_registry_confirmed = true

STAGE 0 BODY:

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|--------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]

  First BLOCKED step halts campaign. Record step and owning role.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open — Steps 1, 2, 3 all confirmed. SESSION INVARIANT D active.
   Advancing to Stage 1."

---

## STAGE 1 — HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] RESUME AUDIT: Stage 1 = RUN
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered

STAGE 1 BODY:
Load scout artifact. Read signals. Frame hypothesis.

  source_scout_artifact:        [path from ROLE B — copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense — grounded in ROLE C analysis]
  confidence_prior:             [1-10 numeric]
  gate_s_cleared:               [true — from GATE S Step 2]
  invariant_registry_confirmed: [true — from GATE S Step 3]
  incumbent_threat_locked:      [true — from GATE S Step 1]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked
  "STAGE 1 EXIT: hypothesis_locked — {topic}-hypothesis-{date}.md written. Stage 2 ready."

---

## STAGE 2 — WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked
  [ ] RESUME AUDIT: Stage 2 = RUN
  [ ] hypothesis artifact confirmed written
  [ ] SESSION INVARIANT D Stage 2 template active

STAGE 2 BODY:
Gather minimum 5 external sources.

INCUMBENT CHECK TABLE — Stage 2 (SESSION INVARIANT D verbatim; DISPLACEMENT DELTA column):

  ITEM | SOURCE | SUMMARY | TEMPLATE APPLIED & VERDICT | DISP DELTA
  -----|--------|---------|----------------------------|-----------
  1    | [src]  | [sum]   | "Does [item] support displacement of [comp] by [topic] on [dim]? [Yes/No/Inc]" | [d]
  2    | [src]  | [sum]   | (fill each row verbatim) | [d]
  3+   | ...    | ...     |                            | [d]

  s2_count:                   [N] — must be >= 5
  s2_displacement_delta_sum:  [sum of DISP DELTA column]
  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]
  s2_confidence_delta:        [+/- numeric]
  running_confidence:         [confidence_prior + s2_confidence_delta]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."
Write artifact: {topic}-websearch-{date}.md. Confirm write.

GATE INSTRUCTION: Do not fire exit signal until s2_count >= 5.
If s2_count < 5, gather additional external sources before proceeding.

STAGE 2 EXIT SIGNAL: websearch_complete(count=[N], confidence=[running_confidence])
  "STAGE 2 EXIT: websearch_complete — s2_count = [N] (gate: >= 5 met).
   s2_ce_verdict = [value]. running_confidence = [value]. Stage 3 ready."

---

## STAGE 3 — INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete
  [ ] RESUME AUDIT: Stage 3 = RUN
  [ ] s2_ce_verdict recorded
  [ ] Read {topic}-websearch-{date}.md from disk. Extract running_confidence.
      Validate against signal payload. Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 3 template active

STAGE 3 BODY:
Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE — Stage 3 (SESSION INVARIANT D verbatim; DISPLACEMENT DELTA column):

  PRACTITIONER | KEY ACCOUNT | TEMPLATE APPLIED & VERDICT | DISP DELTA
  -------------|-------------|----------------------------|-----------
  [type 1]     | [account]   | "Does [account] reveal a viable transition path from [comp] to [topic] for [use case]? [Yes/No/Inc]" | [d]
  [type 2]     | [account]   | (fill each row verbatim) | [d]
  [type 3]     | [account]   |  | [d]

  s3_count:                    [N] — must be >= 3
  s3_displacement_delta_sum:   [sum of DISP DELTA column]
  s3_incumbent_check_summary:  [N support / M counter / P inconclusive]
  s3_ce_verdict:               [null if no CE; cite account if found]
  s3_confidence_delta:         [+/- numeric]
  running_confidence:          [prior + s3_confidence_delta]
  displacement_momentum:       [s2_displacement_delta_sum + s3_displacement_delta_sum]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."
Write artifact: {topic}-interview-{date}.md. Confirm write.

GATE INSTRUCTION: Do not fire exit signal until s3_count >= 3.
If s3_count < 3, simulate additional practitioner interviews before proceeding.

STAGE 3 EXIT SIGNAL: interview_complete(count=[N], confidence=[running_confidence])
  "STAGE 3 EXIT: interview_complete — s3_count = [N] (gate: >= 3 met).
   s3_ce_verdict = [value]. running_confidence = [value]. Stage 4 ready."

---

## STAGE 4 — PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete
  [ ] RESUME AUDIT: Stage 4 = RUN
  [ ] s3_ce_verdict recorded
  [ ] Read {topic}-interview-{date}.md from disk. Extract running_confidence AND
      displacement_momentum. Validate both against signal payload.
      Mismatch on either = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 4 template active

STAGE 4 BODY:
Design and assess prototype experiments.

  prototype_design:            [brief description]
  prototype_result:            [what was learned — 1-3 sentences]

INCUMBENT CHECK TABLE — Stage 4 (SESSION INVARIANT D verbatim; DISPLACEMENT DELTA column):

  ITEM       | RESULT             | TEMPLATE APPLIED & VERDICT | DISP DELTA
  -----------|--------------------|----------------------------|-----------
  prototype  | [prototype_result] | "Does [result] make a credible case for displacing [comp] with [topic]? [Yes/No/Pending]" | [delta]

  s4_count:                    [N] — must be >= 3
  s4_displacement_delta_sum:   [delta for Stage 4]
  s4_displacement_verdict:     [Yes / No / Pending] — required; omission = format error
  s4_ce_verdict:               [null / description]
  s4_confidence_delta:         [+/- numeric]
  running_confidence:          [prior + s4_confidence_delta]
  displacement_momentum_final: [displacement_momentum + s4_displacement_delta_sum]

Final null tally:
  null_tally_final = [N]
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

GATE INSTRUCTION: Do not fire exit signal until s4_count >= 3.
If s4_count < 3, design additional prototype experiments before proceeding.

Write artifact: {topic}-prototype-{date}.md. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[N], momentum_final=[displacement_momentum_final])
  "STAGE 4 EXIT: prototype_complete — s4_count = [N] (gate: >= 3 met).
   s4_ce_verdict = [value]. null_tally_final = [N].
   displacement_momentum_final = [value]. Stage 5 ready."

---

## STAGE 5 — SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete
  [ ] RESUME AUDIT: Stage 5 = RUN
  [ ] Read {topic}-prototype-{date}.md from disk. Extract running_confidence AND
      displacement_momentum_final. Validate both against signal payload.
      Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 present for resolution
  [ ] All four SESSION INVARIANT TABLE rows active

STAGE 5 BODY:

### BLOCK 1 — CONFIDENCE CHAIN RESOLUTION

  prior:            [confidence_prior from Stage 1]
  s2_delta:         [s2_confidence_delta]
  s3_delta:         [s3_confidence_delta]
  s4_delta:         [s4_confidence_delta]
  chain_equation:   prior + s2_delta + s3_delta + s4_delta = [final]
  confidence_composite: [final — before counter-hypothesis and cap adjustments]

### BLOCK 2 — COUNTER-HYPOTHESIS RESOLUTION

  COUNTER_HYPOTHESIS     | VERDICT                                  | EVIDENCE
  -----------------------|------------------------------------------|-------------------
  [from Stage 1]         | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite stage artifact]

OPEN RISK: reduce confidence_composite one tier before BLOCK 3.

ORDER CONSTRAINT (C-17): If BLOCK 1 requires cr_delta produced by BLOCK 2 resolution,
execute BLOCK 2 before BLOCK 1 and annotate inversion with this ORDER CONSTRAINT statement.

### BLOCK 3 — DISPLACEMENT INTEGRITY CHECK

NULL TALLY CHAIN reconstruction:
  S2 -> [s2_ce_verdict: null or value]
  S3 -> [s3_ce_verdict: null or value]
  S4 -> [s4_ce_verdict: null or value]
  null_tally_final = [N]
  Cross-check vs Stage 4 exit count: [Match / Mismatch]

If null_tally_final >= 3: dual_lock_fired (INV A + INV B). co_activation_confirmed: dual_lock_fired
Else: co_activation_confirmed: not_triggered

THREE-STAGE DISPLACEMENT CHAIN (C-20 + C-22):
Valid STANCE values: SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED.
Y/N shorthand = format error. chain_pattern names the arc; it does not substitute for STANCE.

  STAGE | DISP DELTA SUM | CUMULATIVE MOMENTUM | INCUMBENT DELTA SUM | STANCE                | FLAG?
  ------|----------------|---------------------|---------------------|-----------------------|------
  S2    | [s2_disp_sum]  | [s2_cumul]          | [running sum at S2] | [SUPPORTED /          | [Y/N]
        |                |                     |                     |  PARTIALLY SUPPORTED / |
        |                |                     |                     |  NOT SUPPORTED]        |
  S3    | [s3_disp_sum]  | [s3_cumul]          | [running sum at S3] | [SUPPORTED /          | [Y/N]
        |                |                     |                     |  PARTIALLY SUPPORTED / |
        |                |                     |                     |  NOT SUPPORTED]        |
  S4    | [s4_disp_sum]  | [s4_cumul]          | [running sum at S4] | [SUPPORTED /          | [Y/N]
        |                |                     |                     |  PARTIALLY SUPPORTED / |
        |                |                     |                     |  NOT SUPPORTED]        |

  chain_pattern: [ACCELERATING / STEADY_BUILD / PLATEAU / LATE_REVERSAL / PEAK_THEN_DROP / ...]
  FLAG rule: any stage where STANCE runs counter to adjacent stage stances = FLAG = Y.
  Each FLAG requires conclusion_justification before synthesis closes.

TRAJECTORY COMPUTE STEP (C-19 — execute before displacement_conclusion is set):

  Delta sequence: S2=[s2_disp_sum], S3=[s3_disp_sum], S4=[s4_disp_sum]
  trajectory_direction computation:
    IF S3_delta >= S2_delta AND S4_delta >= S3_delta: ACCELERATING
    IF S3_delta < S2_delta OR S4_delta < S3_delta:    DECELERATING
    ELSE (all deltas within +/- 0.5):                 FLAT

  trajectory_direction: [ACCELERATING / DECELERATING / FLAT]

CEILING RULE (hard constraint):
  IF trajectory_direction = DECELERATING: displacement_conclusion <= PARTIALLY SUPPORTED
  IF trajectory_direction = ACCELERATING: displacement_conclusion may reach SUPPORTED
  IF trajectory_direction = FLAT:         displacement_conclusion ceiling = direction of displacement_momentum_final

  trajectory_ceiling_applied: [true / false]
  displacement_conclusion:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  conclusion_justification:   [required if any FLAG = Y or ceiling applied]
  incumbent_defense_closed:   [true when all flagged rows reconciled]

### SYNTHESIS BODY

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences integrating Stages 2, 3, 4]
  confidence_composite:  [final value after all adjustments]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### HANDOFF TABLE

SESSION INVARIANT C enforced. All fields carry [derived from: X]. Unlabeled = format error.

  FIELD                      | VALUE   | DERIVATION                                  | IND. CHAIN
  ---------------------------|---------|---------------------------------------------|------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]           | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]             | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]            | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]            | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]            | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]            | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]            | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4 CE verdicts]        | not through co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]            | not through incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct chain]       | not through co_activation
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]           | capped by INV B
  schema_compliance_confirmed| [true]  | [all 11 fields, sources match]              | n/a

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete — Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-03 — Dual Chain Bridge Declaration

**Axis**: dual_chain_bridge_declaration (single)
**Hypothesis**: C-21 has a structural dimension beyond value-listing: Stage 4 is the *only*
stage where both chains (confidence and displacement) reach their final values simultaneously.
If this convergence is made explicit via a CHAIN BRIDGE block inside Stage 4 body — naming
confidence_chain_final and displacement_chain_final as resolved, and adding bridge_declared
to the exit signal — C-21 will register as a structural pass, not just a value pass. This
axis tests whether the declaration framing matters for C-21 or whether V-01's body echo
is sufficient alone.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---
depth: standard
confidence: standard
for: {value}
iterations: 1

Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign builds the case for displacing {status_quo_comparator} with {topic}.
Six stages (Stage 0 = gate, Stages 1-5 = evidence + synthesis). Each stage has numbered
ENTRY CONDITIONS and a named EXIT SIGNAL. No stage body begins until entry conditions confirm.

---

## CAMPAIGN OPEN

  topic:                 {topic}
  date:                  {date}
  status_quo_comparator: [name the incumbent approach this topic must displace]

### INCUMBENT ANCHOR

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS TABLE

  ID   | NAME                      | DECLARATION
  -----|---------------------------|------------------------------------------------------
  D    | INCUMBENT CHECK PHRASING  | Stage 2: "Does [evidence item] support the displacement
       | REGISTER                  |   of {status_quo_comparator} by {topic} on [dimension]?
       |                           |   [Yes / No / Inconclusive]"
       |                           | Stage 3: "Does [practitioner account] reveal a viable
       |                           |   transition path from {status_quo_comparator} to
       |                           |   {topic} for [use case]? [Yes / No / Inconclusive]"
       |                           | Stage 4: "Does [prototype result] make a credible case
       |                           |   for displacing {status_quo_comparator} with {topic}?
       |                           |   [Yes / No / Pending]"
       |                           | Cannot be modified or bypassed at any stage.
  -----|---------------------------|------------------------------------------------------
  A    | ADVERSARIAL REVIEWER TYPE | adversarial_reviewer_type: [challenging role]. Activation: null_tally_final >= 3.
  -----|---------------------------|------------------------------------------------------
  B    | CONFIDENCE CAP            | confidence_composite -= 2 if null_tally_final >= 3. Cannot be softened.
  -----|---------------------------|------------------------------------------------------
  C    | DERIVATION ANNOTATION     | Every handoff field carries [derived from: X]. Unlabeled = format error.

### ROLE OWNERSHIP TABLE

  ROLE   | TITLE                    | OWNED FIELD               | GATE S STEP | EXECUTE
  -------|--------------------------|---------------------------|-------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | Step 1      | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared            | Step 2      | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3   | THIRD

ROLE C: incumbent_threat_locked: [true when anchor fields filled]
ROLE B: scout_artifact: [{topic}-scout-record-{date}.md or equivalent]
        scout_loaded: [true/false]  gate_s_cleared: [true if loaded; BLOCKED otherwise]
ROLE A: invariant_registry_confirmed: [true when all four invariants registered]

---

## RESUME AUDIT

  STAGE | ARTIFACT PATTERN                                  | FOUND | DECISION
  ------|---------------------------------------------------|-------|------------------
  1     | simulations/prove/{topic}-hypothesis-{date}.md   | [Y/N] | [RESUME-SKIP / RUN]
  2     | simulations/prove/{topic}-websearch-{date}.md    | [Y/N] | [RESUME-SKIP / RUN]
  3     | simulations/prove/{topic}-interview-{date}.md    | [Y/N] | [RESUME-SKIP / RUN]
  4     | simulations/prove/{topic}-prototype-{date}.md    | [Y/N] | [RESUME-SKIP / RUN]
  5     | simulations/prove/{topic}-synthesis-{date}.md    | [Y/N] | [RESUME-SKIP / RUN]

If all RESUME-SKIP: "RESUME_AUDIT_EXIT — All artifacts present. Campaign complete." STOP.
Otherwise: "RESUME_AUDIT_PASS — Stages to run: [list]. Proceeding to Stage 0."

---

## STAGE 0 — GATE S

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]

STAGE 0 EXIT SIGNAL: gate_open — "Steps 1, 2, 3 confirmed. SESSION INVARIANT D active. Stage 1 ready."

---

## STAGE 1 — HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] gate_open received  [ ] Stage 1 = RUN  [ ] scout_artifact available

  source_scout_artifact:        [path from ROLE B — copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense — grounded in ROLE C analysis]
  confidence_prior:             [1-10 numeric]

Write: {topic}-hypothesis-{date}.md. Confirm.

STAGE 1 EXIT SIGNAL: hypothesis_locked — "{topic}-hypothesis-{date}.md written. Stage 2 ready."

---

## STAGE 2 — WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] hypothesis_locked  [ ] Stage 2 = RUN  [ ] SESSION INVARIANT D Stage 2 template active

  s2_count:                   [N] — must be >= 5
  s2_displacement_delta_sum:  [sum of DISP DELTA]
  s2_ce_verdict:              [null / citation]
  s2_confidence_delta:        [+/- numeric]
  running_confidence:         [confidence_prior + s2_confidence_delta]

GATE INSTRUCTION: Do not fire exit signal until s2_count >= 5.

Write: {topic}-websearch-{date}.md. Confirm.

STAGE 2 EXIT: websearch_complete — s2_count=[N] (gate met). s2_ce_verdict=[v]. running_confidence=[v]. Stage 3 ready.

---

## STAGE 3 — INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] websearch_complete  [ ] Stage 3 = RUN
  [ ] Read {topic}-websearch-{date}.md. Extract running_confidence. Validate. Mismatch = HALT.

  s3_count:                    [N] — must be >= 3
  s3_displacement_delta_sum:   [sum]
  s3_ce_verdict:               [null / citation]
  s3_confidence_delta:         [+/- numeric]
  running_confidence:          [prior + s3_delta]
  displacement_momentum:       [s2_sum + s3_sum]

GATE INSTRUCTION: Do not fire exit signal until s3_count >= 3.

Write: {topic}-interview-{date}.md. Confirm.

STAGE 3 EXIT: interview_complete — s3_count=[N] (gate met). s3_ce_verdict=[v]. running_confidence=[v]. Stage 4 ready.

---

## STAGE 4 — PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] interview_complete  [ ] Stage 4 = RUN
  [ ] Read {topic}-interview-{date}.md. Extract running_confidence AND displacement_momentum.
      Validate both. Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 4 template active

STAGE 4 BODY:

  prototype_design:            [brief description]
  prototype_result:            [what was learned — 1-3 sentences]

INCUMBENT CHECK TABLE — Stage 4:

  ITEM       | RESULT             | TEMPLATE APPLIED & VERDICT                                                    | DISP DELTA
  -----------|--------------------|-------------------------------------------------------------------------------|-----------
  prototype  | [prototype_result] | "Does [result] make a credible case for displacing [comp] with [topic]? [Yes/No/Pending]" | [delta]

  s4_count:                    [N] — must be >= 3
  s4_displacement_delta_sum:   [delta for Stage 4]
  s4_displacement_verdict:     [Yes / No / Pending] — required
  s4_ce_verdict:               [null / description]
  s4_confidence_delta:         [+/- numeric]
  running_confidence:          [prior + s4_confidence_delta]
  displacement_momentum_final: [displacement_momentum + s4_displacement_delta_sum]

CHAIN BRIDGE (Stage 4 only):
Both the confidence chain and the displacement chain reach their final values at this stage.
No further updates to either field occur after Stage 4 exit.

  confidence_chain_final:   running_confidence = [value]
                            (final — no further updates after Stage 4 exit)
  displacement_chain_final: displacement_momentum_final = [value]
                            (final — no further updates after Stage 4 exit)
  bridge_declared:          true — both chains resolved simultaneously at Stage 4

Final null tally:
  null_tally_final = [N]
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

GATE INSTRUCTION: Do not fire exit signal until s4_count >= 3.

Write: {topic}-prototype-{date}.md. Confirm.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[N], confidence=[running_confidence], momentum_final=[displacement_momentum_final], bridge_declared=true)
  "STAGE 4 EXIT: prototype_complete — s4_count = [N] (gate: >= 3 met).
   running_confidence = [value]. displacement_momentum_final = [value].
   bridge_declared = true (both chains final at Stage 4). null_tally_final = [N].
   s4_ce_verdict = [value]. Stage 5 ready."

---

## STAGE 5 — SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] prototype_complete received (with bridge_declared = true)
  [ ] Stage 5 = RUN
  [ ] Read {topic}-prototype-{date}.md. Extract running_confidence AND displacement_momentum_final.
      Validate both. Mismatch = CHAIN INTEGRITY FAILURE. Halt.

### BLOCK 1 — CONFIDENCE CHAIN RESOLUTION

  prior + s2_delta + s3_delta + s4_delta = confidence_composite [before adjustments]

### BLOCK 2 — COUNTER-HYPOTHESIS RESOLUTION

  COUNTER_HYPOTHESIS | VERDICT (REFUTED / PARTIALLY REFUTED / OPEN RISK) | EVIDENCE
  OPEN RISK: reduce confidence_composite one tier.

ORDER CONSTRAINT (C-17): execute BLOCK 2 before BLOCK 1 if cr_delta required; annotate.

### BLOCK 3 — DISPLACEMENT INTEGRITY CHECK

NULL TALLY CHAIN: S2=[s2_ce_verdict], S3=[s3_ce_verdict], S4=[s4_ce_verdict].
null_tally_final=[N]. Cross-check vs Stage 4 exit.

If null_tally_final >= 3: dual_lock_fired (INV A + INV B). Else: not_triggered.

THREE-STAGE DISPLACEMENT CHAIN (C-20):

  STAGE | DISP DELTA SUM | CUMULATIVE MOMENTUM | INCUMBENT DELTA SUM | VERDICT   | FLAG?
  S2    | [s2_disp_sum]  | [s2_cumul]          | [sum S2]            | [Y/N/Inc] | [Y/N]
  S3    | [s3_disp_sum]  | [s3_cumul]          | [sum S3]            | [Y/N/Inc] | [Y/N]
  S4    | [s4_disp_sum]  | [s4_cumul]          | [sum S4]            | [Y/N/Inc] | [Y/N]

  chain_pattern: [named arc]
  Each FLAG requires conclusion_justification.

TRAJECTORY COMPUTE STEP (C-19):
  trajectory_direction: [ACCELERATING / DECELERATING / FLAT]
  CEILING RULE: DECELERATING -> displacement_conclusion <= PARTIALLY SUPPORTED.
  trajectory_ceiling_applied: [true/false]
  displacement_conclusion: [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]

### SYNTHESIS BODY

  hypothesis_verdict: [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:   [2-3 sentences from Stages 2, 3, 4]
  confidence_composite: [final]
  key_risk: [residual incumbent strength]

### HANDOFF TABLE (SESSION INVARIANT C — all fields labeled [derived from: X])

  scout_anchor, incumbent_threat_locked, hypothesis, counter_hypothesis,
  s2_ce_verdict, s3_ce_verdict, s4_ce_verdict, null_tally_final,
  co_activation_confirmed, incumbent_defense_closed, confidence_composite,
  schema_compliance_confirmed

STAGE 5 EXIT: synthesis_complete — Evidence brief ready for topic-story.

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both. Campaign complete.
```

---

## V-04 — Stage 4 Body Confidence Echo + Chain Table Verdict Vocabulary

**Axis**: stage4_body_confidence_echo + chain_table_verdict_vocabulary (combined)
**Hypothesis**: C-21 and C-22 are independent fixes that do not conflict. Combining V-01
(running_confidence in Stage 4 exit body) and V-02 (SUPPORTED vocabulary in THREE-STAGE
DISPLACEMENT CHAIN) will achieve PASS on both simultaneously while preserving all other
R19 V-05 criteria. This tests whether the minimal two-fix combination is sufficient for
both new criteria without the bridge declaration overhead of V-03.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---
depth: standard
confidence: standard
for: {value}
iterations: 1

Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign builds the case for displacing {status_quo_comparator} with {topic}.
Six stages (Stage 0 = gate, Stages 1-5 = evidence + synthesis). Each stage has numbered
ENTRY CONDITIONS and a named EXIT SIGNAL. No stage body begins until entry conditions confirm.

---

## CAMPAIGN OPEN

  topic:                 {topic}
  date:                  {date}
  status_quo_comparator: [name the incumbent approach this topic must displace]

### INCUMBENT ANCHOR

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS TABLE

  ID   | NAME                      | DECLARATION
  D    | INCUMBENT CHECK PHRASING REGISTER | [Stage 2/3/4 templates verbatim. Cannot be modified.]
  A    | ADVERSARIAL REVIEWER TYPE         | [activates if null_tally_final >= 3]
  B    | CONFIDENCE CAP                    | [confidence_composite -= 2 if null_tally_final >= 3]
  C    | DERIVATION ANNOTATION             | [every handoff field carries derived from: X]

### ROLE OWNERSHIP TABLE

  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked | Step 1 | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared          | Step 2 | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3 | THIRD

ROLE C: incumbent_threat_locked: [true when anchor filled]
ROLE B: scout_artifact: [{topic}-scout-record-{date}.md or equivalent]
        gate_s_cleared: [true / CAMPAIGN BLOCKED]
ROLE A: invariant_registry_confirmed: [true when all four invariants registered]

---

## RESUME AUDIT

  STAGE | ARTIFACT PATTERN | FOUND | DECISION
  1 | simulations/prove/{topic}-hypothesis-{date}.md | [Y/N] | [RESUME-SKIP / RUN]
  2 | simulations/prove/{topic}-websearch-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  3 | simulations/prove/{topic}-interview-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  4 | simulations/prove/{topic}-prototype-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  5 | simulations/prove/{topic}-synthesis-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]

All RESUME-SKIP -> RESUME_AUDIT_EXIT. Otherwise -> RESUME_AUDIT_PASS. Proceed to Stage 0.

---

## STAGE 0 — GATE S

  Step 1: incumbent_threat_locked = true (ROLE C)
  Step 2: gate_s_cleared = true (ROLE B)
  Step 3: invariant_registry_confirmed = true (ROLE A)
  First BLOCKED halts campaign.

EXIT: gate_open — all three confirmed. Stage 1 ready.

---

## STAGE 1 — HYPOTHESIS

  [ ] gate_open  [ ] Stage 1 = RUN  [ ] scout_artifact available

  source_scout_artifact: [path from ROLE B — copied]
  hypothesis:            [falsifiable claim]
  counter_hypothesis:    [incumbent's best defense]
  confidence_prior:      [1-10]

Write: {topic}-hypothesis-{date}.md. Confirm.
EXIT: hypothesis_locked.

---

## STAGE 2 — WEB SEARCH

  [ ] hypothesis_locked  [ ] Stage 2 = RUN  [ ] INV D Stage 2 template active

INCUMBENT CHECK TABLE — Stage 2:

  ITEM | SOURCE | SUMMARY | TEMPLATE APPLIED & VERDICT | DISP DELTA
  -----|--------|---------|----------------------------|-----------
  1    | [src]  | [sum]   | "Does [item] support displacement of [comp] by [topic] on [dim]? [Y/N/Inc]" | [d]
  (min 5 rows)

  s2_count: [N] >= 5  |  s2_displacement_delta_sum: [sum]  |  s2_ce_verdict: [null/cite]
  s2_confidence_delta: [+/-]  |  running_confidence: [prior + delta]

Running null tally. Write: {topic}-websearch-{date}.md. Confirm.
GATE INSTRUCTION: Do not fire exit signal until s2_count >= 5.

EXIT: websearch_complete(count=[N], confidence=[running_confidence]) —
  "s2_count=[N] (gate met). s2_ce_verdict=[v]. running_confidence=[v]. Stage 3 ready."

---

## STAGE 3 — INTERVIEW

  [ ] websearch_complete  [ ] Stage 3 = RUN
  [ ] Read {topic}-websearch-{date}.md. Extract running_confidence. Validate. Mismatch = HALT.
  [ ] INV D Stage 3 template active

INCUMBENT CHECK TABLE — Stage 3:

  PRACTITIONER | KEY ACCOUNT | TEMPLATE APPLIED & VERDICT | DISP DELTA
  (min 3 rows)
  "Does [account] reveal a viable transition path from [comp] to [topic] for [use case]? [Y/N/Inc]"

  s3_count: [N] >= 3  |  s3_displacement_delta_sum: [sum]  |  s3_ce_verdict: [null/cite]
  s3_confidence_delta: [+/-]  |  running_confidence: [prior + delta]
  displacement_momentum: [s2_sum + s3_sum]

Running null tally. Write: {topic}-interview-{date}.md. Confirm.
GATE INSTRUCTION: Do not fire exit signal until s3_count >= 3.

EXIT: interview_complete(count=[N], confidence=[running_confidence]) —
  "s3_count=[N] (gate met). s3_ce_verdict=[v]. running_confidence=[v]. Stage 4 ready."

---

## STAGE 4 — PROTOTYPE

  [ ] interview_complete  [ ] Stage 4 = RUN
  [ ] Read {topic}-interview-{date}.md. Extract running_confidence AND displacement_momentum.
      Validate both. Mismatch on either = CHAIN INTEGRITY FAILURE. Halt.
  [ ] INV D Stage 4 template active

INCUMBENT CHECK TABLE — Stage 4:

  ITEM      | RESULT             | TEMPLATE APPLIED & VERDICT                                                    | DISP DELTA
  prototype | [prototype_result] | "Does [result] make a credible case for displacing [comp] with [topic]? [Yes/No/Pending]" | [delta]

  s4_count: [N] >= 3  |  s4_displacement_delta_sum: [delta]
  s4_displacement_verdict: [Yes/No/Pending] — required
  s4_ce_verdict: [null/description]
  s4_confidence_delta: [+/-]
  running_confidence: [prior + s4_delta]
  displacement_momentum_final: [displacement_momentum + s4_displacement_delta_sum]

null_tally_final = [N]. Cross-check with Stage 3 running count.

GATE INSTRUCTION: Do not fire exit signal until s4_count >= 3.
Write: {topic}-prototype-{date}.md. Confirm.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[N], confidence=[running_confidence], momentum_final=[displacement_momentum_final])
  "STAGE 4 EXIT: prototype_complete — s4_count = [N] (gate: >= 3 met).
   running_confidence = [value]. s4_ce_verdict = [value]. null_tally_final = [N].
   displacement_momentum_final = [value]. Stage 5 ready."

---

## STAGE 5 — SYNTHESIS

  [ ] prototype_complete(count=N, confidence=C, momentum_final=M)
  [ ] Stage 5 = RUN
  [ ] Read {topic}-prototype-{date}.md. Extract running_confidence AND displacement_momentum_final.
      Validate both. Mismatch = CHAIN INTEGRITY FAILURE. Halt.

### BLOCK 1 — CONFIDENCE CHAIN RESOLUTION

  prior + s2_delta + s3_delta + s4_delta = confidence_composite [before adjustments]

### BLOCK 2 — COUNTER-HYPOTHESIS RESOLUTION

  COUNTER_HYPOTHESIS | VERDICT (REFUTED / PARTIALLY REFUTED / OPEN RISK) | EVIDENCE (cite artifact)
  OPEN RISK -> reduce confidence_composite one tier before BLOCK 3.

ORDER CONSTRAINT (C-17): execute BLOCK 2 before BLOCK 1 if cr_delta required; annotate.

### BLOCK 3 — DISPLACEMENT INTEGRITY CHECK

NULL TALLY CHAIN: S2=[s2_ce], S3=[s3_ce], S4=[s4_ce]. null_tally_final=[N]. Cross-check.
null_tally_final >= 3 -> dual_lock_fired. Else -> not_triggered.

THREE-STAGE DISPLACEMENT CHAIN (C-20 + C-22):
STANCE column required per row. Valid values: SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED.
Y/N shorthand = format error. chain_pattern names the arc; it does not substitute for STANCE.

  STAGE | DISP DELTA SUM | CUMULATIVE MOMENTUM | INCUMBENT DELTA SUM | STANCE                                           | FLAG?
  ------|----------------|---------------------|---------------------|--------------------------------------------------|------
  S2    | [s2_disp_sum]  | [s2_cumul]          | [sum at S2]         | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]
  S3    | [s3_disp_sum]  | [s3_cumul]          | [sum at S3]         | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]
  S4    | [s4_disp_sum]  | [s4_cumul]          | [sum at S4]         | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]

  chain_pattern: [named arc]
  Each FLAG = Y requires conclusion_justification.

TRAJECTORY COMPUTE STEP (C-19):

  Delta sequence: S2=[s2_disp_sum], S3=[s3_disp_sum], S4=[s4_disp_sum]
  IF S3>=S2 AND S4>=S3: ACCELERATING
  IF S3<S2 OR S4<S3:   DECELERATING
  ELSE:                 FLAT

  trajectory_direction: [ACCELERATING / DECELERATING / FLAT]

CEILING RULE:
  DECELERATING -> displacement_conclusion <= PARTIALLY SUPPORTED (holds even if momentum_final > 0)
  ACCELERATING -> may reach SUPPORTED
  FLAT         -> ceiling = direction of displacement_momentum_final

  trajectory_ceiling_applied: [true/false]
  displacement_conclusion:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  conclusion_justification:   [required if FLAG=Y or ceiling applied]
  incumbent_defense_closed:   [true when all flags reconciled]

### SYNTHESIS BODY

  hypothesis_verdict:   [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:     [2-3 sentences integrating Stages 2, 3, 4]
  confidence_composite: [final after all adjustments]
  key_risk:             [residual incumbent strength]

### HANDOFF TABLE (SESSION INVARIANT C)

All 11 fields carry [derived from: X]:
  scout_anchor, incumbent_threat_locked, hypothesis, counter_hypothesis,
  s2_ce_verdict, s3_ce_verdict, s4_ce_verdict, null_tally_final,
  co_activation_confirmed, incumbent_defense_closed, confidence_composite,
  + schema_compliance_confirmed

EXIT: synthesis_complete — Evidence brief ready for topic-story.
Write: {topic}-synthesis-{date}.md + {topic}-handoff-{date}.md. Confirm both.
```

---

## V-05 — Full Integration (all three + complete R19 V-05 stack)

**Axis**: stage4_body_confidence_echo + chain_table_verdict_vocabulary + dual_chain_bridge_declaration (combined, on full R19 V-05 baseline)
**Hypothesis**: All three axes together — running_confidence in Stage 4 exit body (C-21
value pass), SUPPORTED vocabulary in THREE-STAGE DISPLACEMENT CHAIN (C-22), and CHAIN
BRIDGE declaration in Stage 4 body (C-21 structural pass) — will achieve PASS on both
C-21 and C-22 simultaneously on the full R19 V-05 structural stack, while preserving
C-08 (RESUME AUDIT), C-12 (count-gated exits), C-17 (DEPENDENCY ORDER CONSTRAINT),
C-18 (dual-field entry validation), C-19 (TRAJECTORY COMPUTE STEP), C-20 (THREE-STAGE
DISPLACEMENT CHAIN), and all essential/recommended criteria.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---
depth: standard
confidence: standard
for: {value}
iterations: 1

Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign builds the case for displacing {status_quo_comparator} with {topic}.
Six stages (Stage 0 = gate, Stages 1-5 = evidence + synthesis). Each stage has numbered
ENTRY CONDITIONS and a named EXIT SIGNAL. No stage body begins until entry conditions confirm.

---

## CAMPAIGN OPEN

  topic:                 {topic}
  date:                  {date}
  status_quo_comparator: [name the incumbent approach this topic must displace]

### INCUMBENT ANCHOR

Fill before any role or invariant registration.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS TABLE

SESSION INVARIANT D leads. All invariants carry: "cannot be modified or bypassed at
any subsequent stage." Register all four before roles execute.

  ID   | NAME                      | DECLARATION
  -----|---------------------------|------------------------------------------------------
  D    | INCUMBENT CHECK PHRASING  | Stage 2: "Does [evidence item] support the displacement
       | REGISTER                  |   of {status_quo_comparator} by {topic} on [dimension]?
       |                           |   [Yes / No / Inconclusive]"
       |                           | Stage 3: "Does [practitioner account] reveal a viable
       |                           |   transition path from {status_quo_comparator} to
       |                           |   {topic} for [use case]? [Yes / No / Inconclusive]"
       |                           | Stage 4: "Does [prototype result] make a credible case
       |                           |   for displacing {status_quo_comparator} with {topic}?
       |                           |   [Yes / No / Pending]"
       |                           | Enforcement: Template deviation = format error.
       |                           | Cannot be modified or bypassed at any stage.
  -----|---------------------------|------------------------------------------------------
  A    | ADVERSARIAL REVIEWER      | adversarial_reviewer_type: [role most likely to
       | TYPE                      |   challenge the displacement claim].
       |                           | Activation: null_tally_final >= 3.
       |                           | Cannot be modified or bypassed at synthesis.
  -----|---------------------------|------------------------------------------------------
  B    | CONFIDENCE CAP            | null_ce_cap_rule: confidence_composite -= 2 if
       |                           |   null_tally_final >= 3 (hard cap).
       |                           | Cannot be softened or overridden at synthesis.
  -----|---------------------------|------------------------------------------------------
  C    | DERIVATION ANNOTATION     | annotation_rule: Every handoff field carries
       |                           |   [derived from: X]. Unlabeled = format error.
       |                           | Cannot be modified or bypassed at synthesis.

### ROLE OWNERSHIP TABLE

ROLE C executes first. Roles run in sequence C -> B -> A before Stage 0 begins.
DEPENDENCY column: no role may execute until its listed dependency is satisfied.

  ROLE   | TITLE                    | OWNED FIELD               | GATE S STEP | EXECUTE | DEPENDENCY
  -------|--------------------------|---------------------------|-------------|---------|------------------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | Step 1      | FIRST   | INCUMBENT ANCHOR filled
  ROLE B | SCOUT LOADER             | gate_s_cleared            | Step 2      | SECOND  | ROLE C complete
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3   | THIRD   | ROLE B complete

ROLE C execution (fill now):
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  invariant_registry_confirmed: [true when all four invariants registered]

### CE VERDICT OWNERSHIP TABLE

  FIELD            | OWNED BY      | FORMULA
  -----------------|---------------|-----------------------------------------------------
  s2_ce_verdict    | Stage 2       | null if no CE; citation if CE found
  s3_ce_verdict    | Stage 3       | null if no CE; citation if CE found
  s4_ce_verdict    | Stage 4       | null if no CE; description if CE found
  null_tally_final | Stage 4 close | count(null) across s2 + s3 + s4

NULL TALLY CHAIN RULE (locked): Running tally from Stage 2. Stage 4 close reconstructs
full chain. ATOMIC DUAL-LOCK cross-checks at synthesis. Mismatch = integrity failure.

### PRE-COMMITTED HANDOFF SCHEMA TABLE

  FIELD                      | DERIVATION SOURCE                     | IND. CHAIN
  ---------------------------|---------------------------------------|------------------
  scout_anchor               | ROLE B scout load                     | n/a
  incumbent_threat_locked    | ROLE C analysis                       | n/a
  hypothesis                 | Stage 1 artifact                      | n/a
  counter_hypothesis         | Stage 1 artifact                      | n/a
  s2_ce_verdict              | Stage 2 artifact                      | n/a
  s3_ce_verdict              | Stage 3 artifact                      | n/a
  s4_ce_verdict              | Stage 4 artifact                      | n/a
  null_tally_final           | s2+s3+s4 CE verdicts                  | not through co_activation
  co_activation_confirmed    | ATOMIC DUAL-LOCK                      | not through incumbent_defense
  incumbent_defense_closed   | s2+s3+s4 direct chain                 | not through co_activation
  confidence_composite       | Stage 5 minus reductions              | capped by B

---

## RESUME AUDIT

Run this block before Stage 0. Glob existing artifacts for {topic} on {date}.

ARTIFACT SCAN:
  STAGE | ARTIFACT PATTERN                                       | FOUND (Y/N) | DECISION
  ------|--------------------------------------------------------|-------------|------------------
  1     | simulations/prove/{topic}-hypothesis-{date}.md        | [Y/N]       | [RESUME-SKIP / RUN]
  2     | simulations/prove/{topic}-websearch-{date}.md         | [Y/N]       | [RESUME-SKIP / RUN]
  3     | simulations/prove/{topic}-interview-{date}.md         | [Y/N]       | [RESUME-SKIP / RUN]
  4     | simulations/prove/{topic}-prototype-{date}.md         | [Y/N]       | [RESUME-SKIP / RUN]
  5     | simulations/prove/{topic}-synthesis-{date}.md         | [Y/N]       | [RESUME-SKIP / RUN]

  resume_audit_complete: [true]
  stages_to_run:         [list of stages with RUN decision, or ALL if none found]

RESUME AUDIT EXIT:
  If all five stages are RESUME-SKIP: emit "RESUME_AUDIT_EXIT — All stage artifacts
  already present on disk. Campaign complete. No stages will re-run." and STOP.
  Otherwise: "RESUME_AUDIT_PASS — Stages to run: [list]. Proceeding to Stage 0."

---

## STAGE 0 — GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] RESUME AUDIT completed — resume_audit_complete = true
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] SESSION INVARIANTS TABLE complete — all four rows filled
  [ ] ROLE C executed — incumbent_threat_locked = true
  [ ] ROLE B executed — scout_artifact identified and scout_loaded confirmed
  [ ] ROLE A executed — invariant_registry_confirmed = true

STAGE 0 BODY:

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|--------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]

  First BLOCKED step halts campaign. Record step and owning role.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open — Steps 1, 2, 3 all confirmed. SESSION INVARIANT D active.
   Advancing to Stage 1."

---

## STAGE 1 — HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] RESUME AUDIT: Stage 1 = RUN
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered

STAGE 1 BODY:
Load scout artifact from disk (C-15: tamper-resistant — read file, do not reconstruct from memory).
Read signals. Frame hypothesis.

  source_scout_artifact:        [path from ROLE B — copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense — grounded in ROLE C analysis]
  confidence_prior:             [1-10 numeric — initial estimate before evidence]
  gate_s_cleared:               [true — from GATE S Step 2]
  invariant_registry_confirmed: [true — from GATE S Step 3]
  incumbent_threat_locked:      [true — from GATE S Step 1]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked
  "STAGE 1 EXIT: hypothesis_locked — {topic}-hypothesis-{date}.md written. Stage 2 ready."

---

## STAGE 2 — WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked
  [ ] RESUME AUDIT: Stage 2 = RUN
  [ ] hypothesis artifact confirmed written
  [ ] SESSION INVARIANT D Stage 2 template active (verbatim from table row D)

STAGE 2 BODY:
Gather minimum 5 external sources.

INCUMBENT CHECK TABLE — Stage 2 (SESSION INVARIANT D, Stage 2 template applied verbatim;
DISPLACEMENT DELTA column for momentum tracking):

  ITEM | SOURCE (URL or citation) | SUMMARY (1 sentence) | TEMPLATE APPLIED & VERDICT                        | DISP DELTA (-2 to +2)
  -----|--------------------------|----------------------|---------------------------------------------------|-----------------------
  1    | [source]                 | [summary]            | "Does [item] support displacement of [comp]       | [delta]
  2    | [source]                 | [summary]            |  by [topic] on [dim]? [Yes / No / Inconclusive]" | [delta]
  3    | [source]                 | [summary]            | (fill each row verbatim)                          | [delta]
  4    | [source]                 | [summary]            |                                                   | [delta]
  5    | [source]                 | [summary]            |                                                   | [delta]

  s2_count:                   [N] — must be >= 5
  s2_displacement_delta_sum:  [sum of DISP DELTA column]
  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]
  s2_confidence_delta:        [+/- numeric]
  running_confidence:         [confidence_prior + s2_confidence_delta]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."
SCHEMA INTEGRITY: handoff fields populated per PRE-COMMITTED HANDOFF SCHEMA TABLE.
Write artifact: {topic}-websearch-{date}.md. Confirm write.

GATE INSTRUCTION: Do not fire exit signal until s2_count >= 5.
If s2_count < 5, gather additional external sources before proceeding.

STAGE 2 EXIT SIGNAL: websearch_complete(count=[N], confidence=[running_confidence], momentum=[s2_displacement_delta_sum])
  "STAGE 2 EXIT: websearch_complete — s2_count = [N] (gate: >= 5 met).
   s2_ce_verdict = [value]. running_confidence = [value]. Stage 3 ready."

---

## STAGE 3 — INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete(count=N, confidence=C, momentum=M)
  [ ] RESUME AUDIT: Stage 3 = RUN
  [ ] s2_ce_verdict recorded
  [ ] ARTIFACT EXTRACTION (C-15 + C-18): Read {topic}-websearch-{date}.md from disk.
      Extract running_confidence. Validate against signal payload.
      Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 3 template active

STAGE 3 BODY:
Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE — Stage 3 (SESSION INVARIANT D, Stage 3 template applied verbatim;
DISPLACEMENT DELTA column):

  PRACTITIONER     | KEY ACCOUNT (1 sentence)     | TEMPLATE APPLIED & VERDICT                                                          | DISP DELTA
  -----------------|------------------------------|-------------------------------------------------------------------------------------|------------
  [type 1]         | [quote or paraphrase]        | "Does [account] reveal a viable transition path from [comp] to [topic]              | [delta]
  [type 2]         | [quote or paraphrase]        |  for [use case]? [Yes / No / Inconclusive]"                                         | [delta]
  [type 3]         | [quote or paraphrase]        | (fill each row verbatim)                                                            | [delta]

  s3_count:                    [N] — must be >= 3
  s3_displacement_delta_sum:   [sum of DISP DELTA column]
  s3_incumbent_check_summary:  [N support / M counter / P inconclusive]
  s3_ce_verdict:               [null if no CE; cite account if found]
  s3_confidence_delta:         [+/- numeric]
  running_confidence:          [prior + s3_confidence_delta]
  displacement_momentum:       [s2_displacement_delta_sum + s3_displacement_delta_sum]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."
SCHEMA INTEGRITY: handoff fields populated per PRE-COMMITTED HANDOFF SCHEMA TABLE.
Write artifact: {topic}-interview-{date}.md. Confirm write.

GATE INSTRUCTION: Do not fire exit signal until s3_count >= 3.
If s3_count < 3, simulate additional practitioner interviews before proceeding.

STAGE 3 EXIT SIGNAL: interview_complete(count=[N], confidence=[running_confidence], momentum=[displacement_momentum])
  "STAGE 3 EXIT: interview_complete — s3_count = [N] (gate: >= 3 met).
   s3_ce_verdict = [value]. running_confidence = [value]. displacement_momentum = [value].
   Stage 4 ready."

---

## STAGE 4 — PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete(count=N, confidence=C, momentum=M)
  [ ] RESUME AUDIT: Stage 4 = RUN
  [ ] s3_ce_verdict recorded
  [ ] ARTIFACT EXTRACTION (C-15 + C-18): Read {topic}-interview-{date}.md from disk.
      Extract running_confidence AND displacement_momentum.
      Validate both against signal payload.
      Mismatch on either = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 4 template active

STAGE 4 BODY:
Design and assess prototype experiments.

  prototype_design:   [brief description]
  prototype_result:   [what was learned — 1-3 sentences]

INCUMBENT CHECK TABLE — Stage 4 (SESSION INVARIANT D, Stage 4 template applied verbatim;
DISPLACEMENT DELTA column):

  ITEM       | RESULT             | TEMPLATE APPLIED & VERDICT                                                    | DISP DELTA
  -----------|--------------------|-------------------------------------------------------------------------------|-----------
  prototype  | [prototype_result] | "Does [result] make a credible case for displacing [comp] with [topic]?       | [delta]
             |                    |  [Yes / No / Pending]"                                                        |

  s4_count:                    [N] — must be >= 3
  s4_displacement_delta_sum:   [delta for Stage 4]
  s4_displacement_verdict:     [Yes / No / Pending] — required; omission = format error
  s4_ce_verdict:               [null / description]
  s4_confidence_delta:         [+/- numeric]
  running_confidence:          [prior + s4_confidence_delta]
  displacement_momentum_final: [displacement_momentum + s4_displacement_delta_sum]

CHAIN BRIDGE (Stage 4 only — both chains reach final here):
Stage 4 is the only stage where both the confidence chain and the displacement chain
simultaneously resolve to their final values. No further updates to either chain after
Stage 4 exit.

  confidence_chain_final:   running_confidence = [value]
                            (no further updates to running_confidence after Stage 4 exit)
  displacement_chain_final: displacement_momentum_final = [value]
                            (no further updates to displacement_momentum_final after Stage 4 exit)
  bridge_declared:          true — both chains resolved at Stage 4 exit simultaneously

Final null tally:
  null_tally_final = [N]
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

GATE INSTRUCTION: Do not fire exit signal until s4_count >= 3.
If s4_count < 3, design additional prototype experiments before proceeding.

Write artifact: {topic}-prototype-{date}.md. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[N], confidence=[running_confidence], momentum_final=[displacement_momentum_final], bridge_declared=true)
  "STAGE 4 EXIT: prototype_complete — s4_count = [N] (gate: >= 3 met).
   running_confidence = [value]. displacement_momentum_final = [value].
   bridge_declared = true (both chains final at Stage 4). null_tally_final = [N].
   s4_ce_verdict = [value]. Stage 5 ready."

---

## STAGE 5 — SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete(count=N, confidence=C, momentum_final=M, bridge_declared=true)
  [ ] RESUME AUDIT: Stage 5 = RUN
  [ ] ARTIFACT EXTRACTION: Read {topic}-prototype-{date}.md from disk.
      Extract running_confidence AND displacement_momentum_final.
      Validate both against signal payload.
      Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 present for resolution
  [ ] All four SESSION INVARIANT TABLE rows active

STAGE 5 BODY:

### BLOCK 1 — CONFIDENCE CHAIN RESOLUTION

  prior:            [confidence_prior from Stage 1]
  s2_delta:         [s2_confidence_delta]
  s3_delta:         [s3_confidence_delta]
  s4_delta:         [s4_confidence_delta]
  chain_equation:   prior + s2_delta + s3_delta + s4_delta = [final]
  confidence_composite: [final — before counter-hypothesis and cap adjustments]

### BLOCK 2 — COUNTER-HYPOTHESIS RESOLUTION

  COUNTER_HYPOTHESIS     | VERDICT                                  | EVIDENCE
  -----------------------|------------------------------------------|-------------------
  [from Stage 1]         | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite stage artifact]
  [add rows as needed]   |                                          |

OPEN RISK: reduce confidence_composite one tier before BLOCK 3.

ORDER CONSTRAINT (C-17): If BLOCK 1 requires cr_delta produced by BLOCK 2 resolution
(counter-hypothesis reduction applied before chain_equation final), execute BLOCK 2
before BLOCK 1 and annotate inversion with this ORDER CONSTRAINT statement.

### BLOCK 3 — DISPLACEMENT INTEGRITY CHECK

NULL TALLY CHAIN reconstruction:
  S2 -> [s2_ce_verdict: null or value]
  S3 -> [s3_ce_verdict: null or value]
  S4 -> [s4_ce_verdict: null or value]
  null_tally_final = [N]
  Cross-check vs Stage 4 exit count: [Match / Mismatch — record mismatch before continuing]

If null_tally_final >= 3:
  Lock 1 (SESSION INVARIANT A): adversarial review by [adversarial_reviewer_type]. BLOCKED.
  Lock 2 (SESSION INVARIANT B): confidence_composite -= 2 (hard cap, cannot be softened).
  co_activation_confirmed: dual_lock_fired
Else:
  co_activation_confirmed: not_triggered

THREE-STAGE DISPLACEMENT CHAIN (C-20 + C-22):
STANCE column required per row. Valid STANCE values: SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED.
Y/N shorthand = format error. chain_pattern names the arc but does not substitute for per-stage STANCE.

  STAGE | DISP DELTA SUM | CUMULATIVE MOMENTUM | INCUMBENT DELTA SUM | STANCE                                            | FLAG?
  ------|----------------|---------------------|---------------------|---------------------------------------------------|------
  S2    | [s2_disp_sum]  | [s2_cumul]          | [running sum at S2] | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]
  S3    | [s3_disp_sum]  | [s3_cumul]          | [running sum at S3] | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]
  S4    | [s4_disp_sum]  | [s4_cumul]          | [running sum at S4] | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]

  chain_pattern: [ACCELERATING / STEADY_BUILD / PLATEAU / LATE_REVERSAL / PEAK_THEN_DROP / ...]
  FLAG rule: any stage where STANCE runs counter to adjacent stage stances = FLAG = Y.
  Each FLAG requires conclusion_justification before synthesis closes.

TRAJECTORY COMPUTE STEP (C-19 — execute before displacement_conclusion is set):

  Delta sequence: S2=[s2_disp_sum], S3=[s3_disp_sum], S4=[s4_disp_sum]
  trajectory_direction computation:
    IF S3_delta >= S2_delta AND S4_delta >= S3_delta: ACCELERATING
    IF S3_delta < S2_delta OR S4_delta < S3_delta:    DECELERATING
    ELSE (all deltas within +/- 0.5):                 FLAT

  trajectory_direction: [ACCELERATING / DECELERATING / FLAT]

CEILING RULE (hard constraint — not editorial note):
  IF trajectory_direction = DECELERATING:
    displacement_conclusion <= PARTIALLY SUPPORTED
    (ceiling holds even if displacement_momentum_final > 0)
  IF trajectory_direction = ACCELERATING:
    displacement_conclusion may reach SUPPORTED if evidence warrants
  IF trajectory_direction = FLAT:
    displacement_conclusion ceiling = direction of displacement_momentum_final

  trajectory_ceiling_applied: [true / false]
  displacement_conclusion:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
    Cannot exceed ceiling set by trajectory_direction.

  conclusion_justification: [required if any FLAG = Y or trajectory ceiling applied]
  incumbent_defense_closed: [true when all flagged rows reconciled]

### SYNTHESIS BODY

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences integrating Stages 2, 3, 4 — with explicit
                           incumbent displacement verdict from Stage 4 check]
  confidence_composite:  [final value after all adjustments]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### HANDOFF TABLE

SESSION INVARIANT C enforced. All fields carry [derived from: X]. Unlabeled = format error.

  FIELD                      | VALUE   | DERIVATION                                  | IND. CHAIN
  ---------------------------|---------|---------------------------------------------|------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]           | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]             | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]            | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]            | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]            | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]            | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]            | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4 CE verdicts]        | not through co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]            | not through incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct chain]       | not through co_activation
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]           | capped by INV B
  schema_compliance_confirmed| [true]  | [all 11 fields, sources match]              | n/a

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete — Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## Variation Summary

| Variation | Axis | Key change from R19 V-05 | C-21 | C-22 | Bridge |
|-----------|------|--------------------------|------|------|--------|
| V-01 | stage4_body_confidence_echo | running_confidence added to Stage 4 exit body text | target PASS | baseline | no |
| V-02 | chain_table_verdict_vocabulary | THREE-STAGE CHAIN STANCE column uses SUPPORTED vocabulary; enforcement note added | baseline | target PASS | no |
| V-03 | dual_chain_bridge_declaration | CHAIN BRIDGE block in Stage 4 + bridge_declared in exit signal | target PASS (structural) | baseline | yes |
| V-04 | echo + vocabulary | V-01 + V-02 combined | target PASS | target PASS | no |
| V-05 | all three + full stack | V-01 + V-02 + V-03 on complete R19 V-05 baseline | target PASS | target PASS | yes |

**Primary target**: V-05 closes both ceiling gaps (C-21, C-22) simultaneously with the bridge
declaration as the structural anchor for C-21. V-04 tests whether value-listing alone suffices.
