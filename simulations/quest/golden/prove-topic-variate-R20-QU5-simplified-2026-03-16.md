---
skill: quest-variate
skill_target: prove-topic
round: R20-QU5
date: 2026-03-16
source: V-05
simplification: QU5 minimal golden — essential criteria only
---

# prove-topic — QU5 Simplified Golden (R20 V-05 base)

**Source**: R20 V-05 (full integration)
**Date**: 2026-03-16

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
---

Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign builds the case for displacing {status_quo_comparator} with {topic}.
Each stage has numbered ENTRY CONDITIONS and a named EXIT SIGNAL. No stage body begins
until entry conditions confirm.

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
Load scout artifact from disk. Read signals. Frame hypothesis.

  source_scout_artifact:        [path from ROLE B — copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense — grounded in ROLE C analysis]
  confidence_prior:             [1-10 numeric — initial estimate before evidence]

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
  [ ] Read {topic}-websearch-{date}.md from disk. Extract running_confidence.
      Validate against signal payload. Mismatch = CHAIN INTEGRITY FAILURE. Halt.
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
  [ ] Read {topic}-interview-{date}.md from disk. Extract running_confidence AND
      displacement_momentum. Validate both against signal payload.
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

Write artifact: {topic}-prototype-{date}.md. Confirm write.

GATE INSTRUCTION: Do not fire exit signal until s4_count >= 3.
If s4_count < 3, design additional prototype experiments before proceeding.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[N], confidence=[running_confidence], momentum_final=[displacement_momentum_final])
  "STAGE 4 EXIT: prototype_complete — s4_count = [N] (gate: >= 3 met).
   running_confidence = [value]. displacement_momentum_final = [value].
   s4_ce_verdict = [value]. Stage 5 ready."

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

  displacement_conclusion:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  conclusion_justification:   [required if any FLAG = Y]
  incumbent_defense_closed:   [true when all flagged rows reconciled]

### SYNTHESIS BODY

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences integrating Stages 2, 3, 4 — with explicit
                           incumbent displacement verdict from Stage 4 check]
  confidence_composite:  [final value after all adjustments]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete — Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```
