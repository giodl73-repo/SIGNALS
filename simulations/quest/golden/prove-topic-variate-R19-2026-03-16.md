---
skill: quest-variate
skill_target: prove-topic
round: R19
date: 2026-03-16
rubric: prove-topic-rubric-v18-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [resume_audit_gate, count_gated_exit_language, trajectory_compute_step]
  combined: [V-04 (resume_audit_gate + count_gated_exit_language), V-05 (all_three + full_structural_stack)]
r18_anchor: >
  R18 V-05 established three new excellence patterns now codified as aspirational criteria:
  C-18 (multi-field inter-stage validation — S3/S4 entry conditions validate both
  running_confidence AND displacement_momentum simultaneously from disk), C-19 (momentum
  trajectory as conclusion ceiling — DECELERATING forces displacement_conclusion <=
  PARTIALLY SUPPORTED), C-20 (per-stage delta column in BLOCK 3 with arc naming —
  THREE-STAGE DISPLACEMENT CHAIN table with INCUMBENT DELTA SUM and chain_pattern).
  Denominator updates to 12 in v18.
r19_context: >
  R18 V-05 achieves C-15 through C-20 but C-08 (resume audit) and C-12 (count-gated
  exit language) remain consistent fails across all R18 variations. R19 treats the full
  R18 V-05 structural stack as the mandatory baseline, then explores NEW axes that
  close the C-08 and C-12 ceiling gaps and probe adjacent territory:

  V-01 (single: resume_audit_gate): C-08 requires a Glob pre-scan before Stage 1 that
  emits RESUME-SKIP or RUN per stage and fires RESUME_AUDIT_EXIT if all stages are already
  complete. The current baseline has no such gate — Stage 0 GATE S is an entry pre-check
  but not a resume check. V-01 inserts a RESUME AUDIT block between CAMPAIGN OPEN and
  Stage 0, with per-artifact glob decisions and an explicit exit path if all artifacts
  are already on disk.

  V-02 (single: count_gated_exit_language): C-12 requires "Do not fire exit signal until
  count >= N" as a hard constraint inside each evidence stage, not a prose suggestion.
  The current baseline states count gates in the stage overview but the gate is not
  embedded in the exit signal instruction. V-02 adds an explicit GATE INSTRUCTION at the
  end of each evidence stage body: "Do not fire exit signal until count >= N. If count
  < N, gather additional [sources/accounts/experiments] before proceeding."

  V-03 (single: trajectory_compute_step): C-19 states momentum trajectory is a conclusion
  ceiling. The current baseline annotates this as a rule in BLOCK 3 but does not compute
  an intermediate trajectory_direction variable explicitly before applying the ceiling.
  V-03 adds a named TRAJECTORY COMPUTE STEP to BLOCK 3 that derives trajectory_direction
  (ACCELERATING / DECELERATING / FLAT) from the per-stage delta sequence before
  displacement_conclusion is set, then applies the ceiling rule as a typed conditional
  with the intermediate variable. This converts C-19 from a constraint annotation to a
  mandatory compute step with an auditable intermediate output.

  V-04 (combined: resume_audit_gate + count_gated_exit_language): V-01 + V-02.
  RESUME AUDIT block + count-gated exit language in all evidence stages. Tests whether
  fixing both consistent ceiling fails together (without the trajectory step change)
  achieves PASS on C-08 and C-12 while maintaining all other criteria.

  V-05 (full: all three + complete R18 V-05 structural stack): V-01 + V-02 + V-03 on
  top of the complete R18 V-05 baseline (DEPENDENCY column in ROLE OWNERSHIP TABLE for
  C-17, C-15 tamper-resistant reads, C-16 three-block Stage 5, C-18 dual-field validation,
  C-19 trajectory ceiling, C-20 per-stage delta chain, ATOMIC DUAL-LOCK, compound exit
  signals). Tests whether all three new axes simultaneously achieve PASS on C-08, C-12,
  and an enhanced C-19 while preserving C-18/C-20 PASS+ patterns.
---

# prove-topic Variations — Round 19 (rubric v18)

**Skill**: prove-topic
**Rubric**: v18 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-20 aspirational)
**Date**: 2026-03-16
**Round**: R19

---

## Context: what informed this round

R18 V-05 is the structural floor for all R19 variations. The v18 rubric codified three
new criteria C-18/C-19/C-20 from R18 excellence patterns. Two recommended/aspirational
criteria remain consistent fails:

| Criterion | Failure mode | R19 target |
|-----------|-------------|-----------|
| C-08 (resume audit) | No glob pre-scan before Stage 1; no RESUME-SKIP/RUN decisions emitted | V-01, V-04, V-05 |
| C-12 (count-gated exit) | Count gates appear in prose/overview, not embedded as hard gate in stage exit instruction | V-02, V-04, V-05 |

V-03 explores a deeper C-19 expression: trajectory as an explicit compute step with an
intermediate variable, not just a ceiling annotation.

---

## V-01 — Resume Audit Gate

**Axis**: resume_audit_gate (single)
**Hypothesis**: C-08 fails because the current baseline has no Glob pre-scan step. GATE S
verifies roles and invariants but does not check whether prior artifacts from a partial
campaign run already exist on disk. If a RESUME AUDIT block is inserted between CAMPAIGN
OPEN and Stage 0, with per-stage artifact glob decisions (RESUME-SKIP or RUN) and an
explicit RESUME_AUDIT_EXIT path when all stages are complete, C-08 will pass without
disturbing any other structural criteria.

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

---

## RESUME AUDIT

Run this block before Stage 0. Glob existing artifacts for {topic} on {date}.

ARTIFACT SCAN:
  STAGE | ARTIFACT PATTERN                    | FOUND (Y/N) | DECISION
  ------|-------------------------------------|-------------|------------------
  1     | simulations/prove/{topic}-hypothesis-{date}.md   | [Y/N] | [RESUME-SKIP / RUN]
  2     | simulations/prove/{topic}-websearch-{date}.md    | [Y/N] | [RESUME-SKIP / RUN]
  3     | simulations/prove/{topic}-interview-{date}.md    | [Y/N] | [RESUME-SKIP / RUN]
  4     | simulations/prove/{topic}-prototype-{date}.md    | [Y/N] | [RESUME-SKIP / RUN]
  5     | simulations/prove/{topic}-synthesis-{date}.md    | [Y/N] | [RESUME-SKIP / RUN]

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
  [ ] RESUME AUDIT: Stage 1 decision = RUN (skip if RESUME-SKIP)
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered

STAGE 1 BODY:
Load scout artifact. Read signals. Frame hypothesis.

  source_scout_artifact:        [path from ROLE B — copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense — grounded in ROLE C analysis]
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
  [ ] RESUME AUDIT: Stage 2 decision = RUN (skip if RESUME-SKIP)
  [ ] hypothesis artifact confirmed written
  [ ] SESSION INVARIANT D Stage 2 template active

STAGE 2 BODY:
Gather minimum 5 external sources.

INCUMBENT CHECK TABLE — Stage 2 (SESSION INVARIANT D, Stage 2 template applied verbatim):

  ITEM | SOURCE (URL or citation) | SUMMARY (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----|--------------------------|----------------------|------------------------------
  1    | [source]                 | [summary]            | "Does [item] support displacement
  2    | [source]                 | [summary]            |  of [comparator] by [topic] on
  3    | [source]                 | [summary]            |  [dim]? [verdict]"
  4    | [source]                 | [summary]            | (fill each row verbatim)
  5    | [source]                 | [summary]            |

  s2_count:                   [N] — must be >= 5
  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]
  running_confidence:         [prior + s2_delta = new value]

GATE INSTRUCTION: Do not fire exit signal until s2_count >= 5. If s2_count < 5,
gather additional sources before proceeding.

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."
Write artifact: {topic}-websearch-{date}.md. Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete — s2_ce_verdict = [value]. s2_count = [N] (gate: >= 5 met).
   running_confidence = [value]. Stage 3 ready."

---

## STAGE 3 — INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete
  [ ] RESUME AUDIT: Stage 3 decision = RUN (skip if RESUME-SKIP)
  [ ] s2_ce_verdict recorded (null or value — not blank)
  [ ] SESSION INVARIANT D Stage 3 template active

STAGE 3 BODY:
Simulate minimum 3 practitioner interviews.

INCUMBENT CHECK TABLE — Stage 3 (SESSION INVARIANT D, Stage 3 template applied verbatim):

  PRACTITIONER     | KEY ACCOUNT (1 sentence)     | TEMPLATE APPLIED & VERDICT
  -----------------|------------------------------|------------------------------
  [type 1]         | [quote or paraphrase]        | "Does [account] reveal a viable
  [type 2]         | [quote or paraphrase]        |  transition path from [comparator]
  [type 3]         | [quote or paraphrase]        |  to [topic] for [use case]? [verdict]"

  s3_count:                   [N] — must be >= 3
  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no CE; cite account if found]
  running_confidence:         [prior + s3_delta = new value]

GATE INSTRUCTION: Do not fire exit signal until s3_count >= 3. If s3_count < 3,
simulate additional practitioner interviews before proceeding.

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."
Write artifact: {topic}-interview-{date}.md. Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete
  "STAGE 3 EXIT: interview_complete — s3_ce_verdict = [value]. s3_count = [N] (gate: >= 3 met).
   running_confidence = [value]. Stage 4 ready."

---

## STAGE 4 — PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete
  [ ] RESUME AUDIT: Stage 4 decision = RUN (skip if RESUME-SKIP)
  [ ] s3_ce_verdict recorded (null or value — not blank)
  [ ] SESSION INVARIANT D Stage 4 template active

STAGE 4 BODY:
Design and assess minimum 3 prototype experiments.

  prototype_design:   [brief description]
  prototype_result:   [what was learned — 1-3 sentences]

INCUMBENT CHECK TABLE — Stage 4 (SESSION INVARIANT D, Stage 4 template applied verbatim):

  ITEM       | PROTOTYPE RESULT (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----------|-------------------------------|-------------------------------
  prototype  | [prototype_result]            | "Does [result] make a credible case
             |                               |  for displacing [comparator] with
             |                               |  [topic]? [Yes / No / Pending]"

  s4_count:                   [N] — must be >= 3
  s4_displacement_verdict:    [Yes / No / Pending] — required; omission = format error
  s4_ce_verdict:              [null if no CE; description if found]
  running_confidence:         [prior + s4_delta = new value]

GATE INSTRUCTION: Do not fire exit signal until s4_count >= 3. If s4_count < 3,
design additional prototype experiments before proceeding.

Final null tally:
  null_tally_final = [N]
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

Write artifact: {topic}-prototype-{date}.md. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete
  "STAGE 4 EXIT: prototype_complete — s4_ce_verdict = [value]. s4_count = [N] (gate: >= 3 met).
   null_tally_final = [N]. Stage 5 ready."

---

## STAGE 5 — SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete
  [ ] RESUME AUDIT: Stage 5 decision = RUN (skip if RESUME-SKIP)
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 present for resolution
  [ ] All four SESSION INVARIANT TABLE rows active

STAGE 5 BODY:

### BLOCK 1 — CONFIDENCE CHAIN RESOLUTION

  prior:           [value at Stage 1 close]
  s2_delta:        [+/- value from Stage 2 evidence]
  s3_delta:        [+/- value from Stage 3 evidence]
  s4_delta:        [+/- value from Stage 4 evidence]
  chain_equation:  prior + s2_delta + s3_delta + s4_delta = [final]
  confidence_composite: [final — before cap check]

### BLOCK 2 — COUNTER-HYPOTHESIS RESOLUTION

  COUNTER_HYPOTHESIS     | VERDICT                                  | EVIDENCE
  -----------------------|------------------------------------------|-------------------
  [from Stage 1]         | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite stage artifact]

OPEN RISK: reduce confidence_composite one tier before ATOMIC DUAL-LOCK.

### BLOCK 3 — DISPLACEMENT INTEGRITY CHECK

ATOMIC DUAL-LOCK:
  S2 -> [s2_ce_verdict: null or value]
  S3 -> [s3_ce_verdict: null or value]
  S4 -> [s4_ce_verdict: null or value]
  null_tally_final = [N]
  Cross-check vs Stage 4 exit count: [Match / Mismatch]

If null_tally_final >= 3:
  Lock 1 (SESSION INVARIANT A): adversarial review by [adversarial_reviewer_type]. BLOCKED.
  Lock 2 (SESSION INVARIANT B): confidence_composite -= 2 (hard cap).
  co_activation_confirmed: dual_lock_fired
Else:
  co_activation_confirmed: not_triggered

DISPLACEMENT INTEGRITY:
  s4_displacement_verdict: [from Stage 4]
  displacement_conclusion: [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  Consistency check: displacement_conclusion aligns with s4_displacement_verdict and
  confidence_composite. Mismatch requires justification before synthesis closes.

### SYNTHESIS BODY

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences integrating Stages 2, 3, 4]
  confidence_composite:  [final value after all adjustments]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### HANDOFF TABLE

SESSION INVARIANT C enforced. All fields carry [derived from: X]. Unlabeled = format error.

  FIELD                      | VALUE   | DERIVATION                          | IND. CHAIN
  ---------------------------|---------|-------------------------------------|------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]   | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]     | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]    | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]    | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]    | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]    | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]    | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4 verdicts]   | not through co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]    | not through incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct]     | not through co_activation
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]   | capped by INV B
  schema_compliance_confirmed| [true]  | [all 11 fields, sources match]      | n/a

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete — Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-02 — Count-Gated Exit Language

**Axis**: count_gated_exit_language (single)
**Hypothesis**: C-12 fails because count thresholds in the current baseline appear in stage
overview lines ("Gather minimum 5 external sources") but are not embedded as hard gate
constraints inside the stage exit instruction block. If each evidence stage gains an
explicit GATE INSTRUCTION ("Do not fire exit signal until count >= N") immediately before
the exit signal, the constraint moves from aspirational prose to a structural guard that
must be satisfied before the exit fires. This satisfies C-12 without altering any other
structural elements of the baseline.

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
  A    | ADVERSARIAL REVIEWER      | adversarial_reviewer_type: [role].
       | TYPE                      | Activation: null_tally_final >= 3.
  -----|---------------------------|------------------------------------------------------
  B    | CONFIDENCE CAP            | null_ce_cap_rule: confidence_composite -= 2 if
       |                           |   null_tally_final >= 3 (hard cap).
  -----|---------------------------|------------------------------------------------------
  C    | DERIVATION ANNOTATION     | annotation_rule: Every handoff field carries
       |                           |   [derived from: X]. Unlabeled = format error.

### ROLE OWNERSHIP TABLE

  ROLE   | TITLE                    | OWNED FIELD               | GATE S STEP | EXECUTE
  -------|--------------------------|---------------------------|-------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | Step 1      | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared            | Step 2      | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3   | THIRD

ROLE C: incumbent_threat_locked = [true when anchor complete]
ROLE B: scout_artifact = [{topic}-scout-record-{date}.md]; gate_s_cleared = [true/false]
ROLE A: invariant_registry_confirmed = [true when all four rows registered]

---

## STAGE 0 — GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN fields filled
  [ ] INCUMBENT ANCHOR filled
  [ ] SESSION INVARIANTS TABLE complete
  [ ] ROLE C executed — incumbent_threat_locked = true
  [ ] ROLE B executed — gate_s_cleared = true
  [ ] ROLE A executed — invariant_registry_confirmed = true

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|--------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open — Steps 1, 2, 3 confirmed. Advancing to Stage 1."

---

## STAGE 1 — HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered

STAGE 1 BODY:

  source_scout_artifact:        [path from ROLE B — copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense — grounded in ROLE C analysis]
  gate_s_cleared:               [true — from GATE S Step 2]
  invariant_registry_confirmed: [true — from GATE S Step 3]
  incumbent_threat_locked:      [true — from GATE S Step 1]
  prior_confidence:             [numeric 1-10 baseline before evidence begins]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked
  "STAGE 1 EXIT: hypothesis_locked — {topic}-hypothesis-{date}.md written. Stage 2 ready."

---

## STAGE 2 — WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked
  [ ] hypothesis artifact confirmed written
  [ ] SESSION INVARIANT D Stage 2 template active

STAGE 2 BODY:
Gather external sources. Minimum threshold: count >= 5.

INCUMBENT CHECK TABLE — Stage 2:

  ITEM | SOURCE (URL or citation) | SUMMARY (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----|--------------------------|----------------------|------------------------------
  1    | [source]                 | [summary]            | "Does [item] support displacement
  2    | [source]                 | [summary]            |  of [comparator] by [topic] on
  3    | [source]                 | [summary]            |  [dim]? [verdict]"
  4    | [source]                 | [summary]            | (fill each row verbatim)
  5    | [source]                 | [summary]            |

  s2_count:                   [N]
  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]
  s2_delta:                   [+/- numeric confidence delta]
  running_confidence:         [prior + s2_delta = new value]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."

GATE INSTRUCTION: Do not fire exit signal until s2_count >= 5.
If s2_count < 5, gather additional sources before proceeding.

Write artifact: {topic}-websearch-{date}.md. Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete — s2_count = [N] (gate: >= 5 met). s2_ce_verdict = [value].
   running_confidence = [value]. Stage 3 ready."

---

## STAGE 3 — INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete
  [ ] s2_ce_verdict recorded
  [ ] SESSION INVARIANT D Stage 3 template active

STAGE 3 BODY:
Simulate practitioner interviews. Minimum threshold: count >= 3.

INCUMBENT CHECK TABLE — Stage 3:

  PRACTITIONER     | KEY ACCOUNT (1 sentence)     | TEMPLATE APPLIED & VERDICT
  -----------------|------------------------------|------------------------------
  [type 1]         | [quote or paraphrase]        | "Does [account] reveal a viable
  [type 2]         | [quote or paraphrase]        |  transition path from [comparator]
  [type 3]         | [quote or paraphrase]        |  to [topic] for [use case]? [verdict]"

  s3_count:                   [N]
  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no CE; cite account if found]
  s3_delta:                   [+/- numeric confidence delta]
  running_confidence:         [prior + s3_delta = new value]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."

GATE INSTRUCTION: Do not fire exit signal until s3_count >= 3.
If s3_count < 3, simulate additional practitioner interviews before proceeding.

Write artifact: {topic}-interview-{date}.md. Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete
  "STAGE 3 EXIT: interview_complete — s3_count = [N] (gate: >= 3 met). s3_ce_verdict = [value].
   running_confidence = [value]. Stage 4 ready."

---

## STAGE 4 — PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete
  [ ] s3_ce_verdict recorded
  [ ] SESSION INVARIANT D Stage 4 template active

STAGE 4 BODY:
Design and assess prototype experiments. Minimum threshold: count >= 3.

  prototype_design:   [brief description]
  prototype_result:   [what was learned — 1-3 sentences]

INCUMBENT CHECK TABLE — Stage 4:

  ITEM       | PROTOTYPE RESULT (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----------|-------------------------------|-------------------------------
  prototype  | [prototype_result]            | "Does [result] make a credible
             |                               |  case for displacing [comparator]
             |                               |  with [topic]? [Yes / No / Pending]"

  s4_count:                [N]
  s4_displacement_verdict: [Yes / No / Pending] — required
  s4_ce_verdict:           [null if no CE; description if found]
  s4_delta:                [+/- numeric confidence delta]
  running_confidence:      [prior + s4_delta = new value]

Final null tally:
  null_tally_final = [N]
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

GATE INSTRUCTION: Do not fire exit signal until s4_count >= 3.
If s4_count < 3, design additional prototype experiments before proceeding.

Write artifact: {topic}-prototype-{date}.md. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete
  "STAGE 4 EXIT: prototype_complete — s4_count = [N] (gate: >= 3 met). s4_ce_verdict = [value].
   null_tally_final = [N]. Stage 5 ready."

---

## STAGE 5 — SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 present
  [ ] All four SESSION INVARIANT TABLE rows active

STAGE 5 BODY:

### BLOCK 1 — CONFIDENCE CHAIN RESOLUTION

  prior:           [value at Stage 1 close]
  s2_delta:        [from Stage 2]
  s3_delta:        [from Stage 3]
  s4_delta:        [from Stage 4]
  chain_equation:  prior + s2_delta + s3_delta + s4_delta = [final]
  confidence_composite: [final]

### BLOCK 2 — COUNTER-HYPOTHESIS RESOLUTION

  COUNTER_HYPOTHESIS     | VERDICT                                  | EVIDENCE
  -----------------------|------------------------------------------|-------------------
  [from Stage 1]         | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite stage artifact]

OPEN RISK: reduce confidence_composite one tier.

### BLOCK 3 — DISPLACEMENT INTEGRITY CHECK

  S2 -> [s2_ce_verdict]
  S3 -> [s3_ce_verdict]
  S4 -> [s4_ce_verdict]
  null_tally_final = [N]; Cross-check vs Stage 4: [Match / Mismatch]

If null_tally_final >= 3:
  co_activation_confirmed: dual_lock_fired
  confidence_composite -= 2 (hard cap, INV B)
Else:
  co_activation_confirmed: not_triggered

  s4_displacement_verdict: [from Stage 4]
  displacement_conclusion: [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  Consistency with confidence_composite: [aligned / justification required]

### SYNTHESIS BODY

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences integrating Stages 2, 3, 4]
  confidence_composite:  [final]
  key_risk:              [primary adoption risk]

### HANDOFF TABLE

  FIELD                      | VALUE   | DERIVATION                          | IND. CHAIN
  ---------------------------|---------|-------------------------------------|------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]   | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]     | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]    | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]    | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]    | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]    | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]    | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4 verdicts]   | not through co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]    | not through incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct]     | not through co_activation
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]   | capped by INV B
  schema_compliance_confirmed| [true]  | [all 11 fields, sources match]      | n/a

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete — Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-03 — Trajectory Compute Step

**Axis**: trajectory_compute_step (single)
**Hypothesis**: C-19 requires trajectory direction to be computed explicitly (not inferred from
the final momentum value alone) and its ceiling effect stated as a rule, not an editorial note.
The current baseline names the ceiling in BLOCK 3 but does not define trajectory_direction
as a separate intermediate variable derived from the delta sequence before displacement_conclusion
is set. If BLOCK 3 adds a named TRAJECTORY COMPUTE STEP that resolves trajectory_direction
from the S2/S3/S4 delta sequence (ACCELERATING if deltas grow, DECELERATING if deltas shrink,
FLAT if stable), then applies the ceiling as a typed conditional ("IF trajectory_direction =
DECELERATING THEN displacement_conclusion <= PARTIALLY SUPPORTED"), the computation path is
auditable and C-19 moves from annotation to enforced rule.

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
  D    | INCUMBENT CHECK PHRASING  | Stage 2/3/4 templates as defined above.
       | REGISTER                  | Cannot be modified or bypassed at any stage.
  -----|---------------------------|------------------------------------------------------
  A    | ADVERSARIAL REVIEWER      | adversarial_reviewer_type: [role].
       | TYPE                      | Activation: null_tally_final >= 3.
  -----|---------------------------|------------------------------------------------------
  B    | CONFIDENCE CAP            | confidence_composite -= 2 if null_tally_final >= 3.
  -----|---------------------------|------------------------------------------------------
  C    | DERIVATION ANNOTATION     | Every handoff field carries [derived from: X].

### ROLE OWNERSHIP TABLE

  ROLE   | TITLE                    | OWNED FIELD               | EXECUTE
  -------|--------------------------|---------------------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared            | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | THIRD

ROLE C: incumbent_threat_locked = [true when anchor complete]
ROLE B: scout_artifact = [{topic}-scout-record-{date}.md]; gate_s_cleared = [true/false]
ROLE A: invariant_registry_confirmed = [true]

---

## STAGE 0 — GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN fields filled
  [ ] INCUMBENT ANCHOR filled
  [ ] SESSION INVARIANTS TABLE complete
  [ ] All three roles executed

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|--------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open — Steps 1, 2, 3 confirmed. Advancing to Stage 1."

---

## STAGE 1 — HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] scout_artifact path available

STAGE 1 BODY:

  source_scout_artifact:        [path from ROLE B]
  hypothesis:                   [falsifiable claim]
  counter_hypothesis:           [incumbent's best defense]
  prior_confidence:             [numeric 1-10 baseline]
  displacement_delta_s1:        [0 — baseline stage, no displacement evidence yet]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked
  "STAGE 1 EXIT: hypothesis_locked — artifact written. Stage 2 ready."

---

## STAGE 2 — WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked
  [ ] SESSION INVARIANT D Stage 2 template active

STAGE 2 BODY:
Gather minimum 5 external sources.

INCUMBENT CHECK TABLE — Stage 2 (with DISPLACEMENT DELTA):

  ITEM | SOURCE       | SUMMARY      | VERDICT       | DISPLACEMENT DELTA (-2 to +2)
  -----|--------------|--------------|---------------|------------------------------
  1    | [source]     | [summary]    | [Y/N/Inc]     | [delta]
  2    | [source]     | [summary]    | [Y/N/Inc]     | [delta]
  3    | [source]     | [summary]    | [Y/N/Inc]     | [delta]
  4    | [source]     | [summary]    | [Y/N/Inc]     | [delta]
  5    | [source]     | [summary]    | [Y/N/Inc]     | [delta]

  s2_count:                    [N >= 5]
  s2_displacement_delta_sum:   [sum of DISPLACEMENT DELTA column]
  s2_incumbent_check_summary:  [N support / M counter / P inconclusive]
  s2_ce_verdict:               [null / citation]
  s2_confidence_delta:         [+/- numeric]
  running_confidence:          [prior + s2_confidence_delta]
  displacement_momentum:       [cumulative: s2_displacement_delta_sum]

Write artifact: {topic}-websearch-{date}.md. Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete — s2_count = [N]. displacement_momentum = [value].
   running_confidence = [value]. Stage 3 ready."

---

## STAGE 3 — INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete
  [ ] s2_ce_verdict recorded
  [ ] SESSION INVARIANT D Stage 3 template active

STAGE 3 BODY:
Simulate minimum 3 practitioner interviews.

INCUMBENT CHECK TABLE — Stage 3 (with DISPLACEMENT DELTA):

  PRACTITIONER | KEY ACCOUNT  | VERDICT       | DISPLACEMENT DELTA (-2 to +2)
  -------------|--------------|---------------|------------------------------
  [type 1]     | [account]    | [Y/N/Inc]     | [delta]
  [type 2]     | [account]    | [Y/N/Inc]     | [delta]
  [type 3]     | [account]    | [Y/N/Inc]     | [delta]

  s3_count:                    [N >= 3]
  s3_displacement_delta_sum:   [sum of DISPLACEMENT DELTA column]
  s3_incumbent_check_summary:  [N support / M counter / P inconclusive]
  s3_ce_verdict:               [null / citation]
  s3_confidence_delta:         [+/- numeric]
  running_confidence:          [prior + s3_confidence_delta]
  displacement_momentum:       [cumulative: prior + s3_displacement_delta_sum]

Write artifact: {topic}-interview-{date}.md. Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete
  "STAGE 3 EXIT: interview_complete — s3_count = [N]. displacement_momentum = [value].
   running_confidence = [value]. Stage 4 ready."

---

## STAGE 4 — PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete
  [ ] s3_ce_verdict recorded
  [ ] SESSION INVARIANT D Stage 4 template active

STAGE 4 BODY:
Design minimum 3 prototype experiments.

  prototype_design:   [brief description]
  prototype_result:   [what was learned]

INCUMBENT CHECK TABLE — Stage 4 (with DISPLACEMENT DELTA):

  ITEM       | RESULT       | VERDICT              | DISPLACEMENT DELTA (-2 to +2)
  -----------|--------------|----------------------|------------------------------
  prototype  | [result]     | [Yes / No / Pending] | [delta]

  s4_count:                    [N >= 3]
  s4_displacement_delta_sum:   [delta for Stage 4]
  s4_displacement_verdict:     [Yes / No / Pending] — required
  s4_ce_verdict:               [null / description]
  s4_confidence_delta:         [+/- numeric]
  running_confidence:          [prior + s4_confidence_delta]
  displacement_momentum_final: [cumulative: prior + s4_displacement_delta_sum]

Final null tally:
  null_tally_final = [N]
  Cross-check vs Stage 3 tally: [Match / Mismatch]

Write artifact: {topic}-prototype-{date}.md. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete
  "STAGE 4 EXIT: prototype_complete — s4_count = [N]. displacement_momentum_final = [value].
   null_tally_final = [N]. Stage 5 ready."

---

## STAGE 5 — SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete
  [ ] null_tally_final recorded
  [ ] counter_hypothesis present for resolution
  [ ] All four SESSION INVARIANT TABLE rows active

STAGE 5 BODY:

### BLOCK 1 — CONFIDENCE CHAIN RESOLUTION

  prior:           [value at Stage 1 close]
  s2_delta:        [from Stage 2]
  s3_delta:        [from Stage 3]
  s4_delta:        [from Stage 4]
  chain_equation:  prior + s2_delta + s3_delta + s4_delta = [final]
  confidence_composite: [final]

### BLOCK 2 — COUNTER-HYPOTHESIS RESOLUTION

  COUNTER_HYPOTHESIS     | VERDICT                                  | EVIDENCE
  -----------------------|------------------------------------------|-------------------
  [from Stage 1]         | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite artifact]

OPEN RISK: reduce confidence_composite one tier.

### BLOCK 3 — DISPLACEMENT INTEGRITY CHECK

TRAJECTORY COMPUTE STEP (execute before displacement_conclusion is set):

  STAGE | DISPLACEMENT DELTA SUM | CUMULATIVE MOMENTUM | DIRECTION SIGNAL
  ------|------------------------|---------------------|-------------------
  S2    | [s2_displacement_delta_sum]  | [s2 cumulative]   | [+/-/0]
  S3    | [s3_displacement_delta_sum]  | [s3 cumulative]   | [+/-/0 vs S2]
  S4    | [s4_displacement_delta_sum]  | [s4 cumulative]   | [+/-/0 vs S3]

  trajectory_direction: [ACCELERATING / DECELERATING / FLAT]
    ACCELERATING: each stage delta >= prior stage delta (momentum growing)
    DECELERATING: at least one later stage delta < prior stage delta (momentum shrinking)
    FLAT:         all stage deltas within +/- 0.5 of each other

  chain_pattern: [name the arc — e.g., STEADY_BUILD / LATE_REVERSAL / PEAK_THEN_DROP]

CEILING RULE (applied as hard constraint, not editorial note):
  IF trajectory_direction = DECELERATING:
    displacement_conclusion <= PARTIALLY SUPPORTED
    (hard ceiling — even if displacement_momentum_final > 0)
  IF trajectory_direction = ACCELERATING:
    displacement_conclusion may reach SUPPORTED if evidence warrants
  IF trajectory_direction = FLAT:
    displacement_conclusion ceiling = displacement_momentum_final direction

  trajectory_ceiling_applied: [true / false]
  displacement_conclusion:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
    Note: must not exceed ceiling set by trajectory_direction

NULL TALLY CROSS-CHECK:
  S2 -> [s2_ce_verdict]; S3 -> [s3_ce_verdict]; S4 -> [s4_ce_verdict]
  null_tally_final = [N]; Cross-check: [Match / Mismatch]

If null_tally_final >= 3:
  co_activation_confirmed: dual_lock_fired; confidence_composite -= 2
Else:
  co_activation_confirmed: not_triggered

Consistency: displacement_conclusion aligns with confidence_composite and
trajectory_ceiling. Any deviation requires conclusion_justification before synthesis closes.

### SYNTHESIS BODY

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences integrating Stages 2, 3, 4]
  confidence_composite:  [final]
  key_risk:              [primary adoption risk]

### HANDOFF TABLE

  FIELD                      | VALUE   | DERIVATION                          | IND. CHAIN
  ---------------------------|---------|-------------------------------------|------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]   | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]     | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]    | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]    | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]    | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]    | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]    | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4 verdicts]   | not through co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]    | not through incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct]     | not through co_activation
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]   | capped by INV B
  schema_compliance_confirmed| [true]  | [all 11 fields, sources match]      | n/a

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete — Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-04 — Resume Audit Gate + Count-Gated Exit Language

**Axes**: resume_audit_gate + count_gated_exit_language (combined)
**Hypothesis**: C-08 and C-12 are the two consistent ceiling fails in R18 and are structurally
independent — one is a pre-execution scan, the other is an in-stage gate instruction. V-04
combines both fixes to test whether they co-exist cleanly without either masking the other
or requiring trade-offs, while making no changes to the R18 V-05 displacement momentum or
trajectory machinery.

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
  D    | INCUMBENT CHECK PHRASING  | Stage 2/3/4 displacement templates (see stage bodies).
       | REGISTER                  | Cannot be modified or bypassed at any stage.
  -----|---------------------------|------------------------------------------------------
  A    | ADVERSARIAL REVIEWER      | adversarial_reviewer_type: [role].
       | TYPE                      | Activation: null_tally_final >= 3.
  -----|---------------------------|------------------------------------------------------
  B    | CONFIDENCE CAP            | confidence_composite -= 2 if null_tally_final >= 3.
  -----|---------------------------|------------------------------------------------------
  C    | DERIVATION ANNOTATION     | Every handoff field carries [derived from: X].

### ROLE OWNERSHIP TABLE

  ROLE   | TITLE                    | OWNED FIELD               | GATE S STEP | EXECUTE
  -------|--------------------------|---------------------------|-------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | Step 1      | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared            | Step 2      | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3   | THIRD

ROLE C: incumbent_threat_locked = [true when anchor complete]
ROLE B: scout_artifact = [{topic}-scout-record-{date}.md]; gate_s_cleared = [true/false]
ROLE A: invariant_registry_confirmed = [true]

---

## RESUME AUDIT

Run before Stage 0. Glob {topic} artifacts for {date}.

ARTIFACT SCAN:
  STAGE | ARTIFACT PATTERN                                       | FOUND | DECISION
  ------|--------------------------------------------------------|-------|------------------
  1     | simulations/prove/{topic}-hypothesis-{date}.md        | [Y/N] | [RESUME-SKIP / RUN]
  2     | simulations/prove/{topic}-websearch-{date}.md         | [Y/N] | [RESUME-SKIP / RUN]
  3     | simulations/prove/{topic}-interview-{date}.md         | [Y/N] | [RESUME-SKIP / RUN]
  4     | simulations/prove/{topic}-prototype-{date}.md         | [Y/N] | [RESUME-SKIP / RUN]
  5     | simulations/prove/{topic}-synthesis-{date}.md         | [Y/N] | [RESUME-SKIP / RUN]

  resume_audit_complete: true
  stages_to_run:         [list RUN stages, or ALL if none found]

RESUME AUDIT EXIT:
  If all five = RESUME-SKIP: "RESUME_AUDIT_EXIT — All artifacts present. Campaign complete."
  Otherwise: "RESUME_AUDIT_PASS — Stages to run: [list]. Proceeding to Stage 0."

---

## STAGE 0 — GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] RESUME AUDIT complete — resume_audit_complete = true
  [ ] CAMPAIGN OPEN fields filled
  [ ] INCUMBENT ANCHOR filled
  [ ] SESSION INVARIANTS TABLE complete
  [ ] ROLE C: incumbent_threat_locked = true
  [ ] ROLE B: gate_s_cleared = true
  [ ] ROLE A: invariant_registry_confirmed = true

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|--------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open — Steps 1, 2, 3 confirmed. Advancing to Stage 1."

---

## STAGE 1 — HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT: gate_open
  [ ] RESUME AUDIT: Stage 1 = RUN
  [ ] scout_artifact available

STAGE 1 BODY:

  source_scout_artifact:        [path from ROLE B — copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense]
  prior_confidence:             [numeric 1-10 baseline]
  gate_s_cleared:               true
  invariant_registry_confirmed: true
  incumbent_threat_locked:      true

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked
  "STAGE 1 EXIT: hypothesis_locked — artifact written. Stage 2 ready."

---

## STAGE 2 — WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT: hypothesis_locked
  [ ] RESUME AUDIT: Stage 2 = RUN
  [ ] SESSION INVARIANT D Stage 2 template active

STAGE 2 BODY:
Gather external sources.

INCUMBENT CHECK TABLE — Stage 2:

  ITEM | SOURCE       | SUMMARY      | TEMPLATE APPLIED & VERDICT
  -----|--------------|--------------|------------------------------
  1    | [source]     | [summary]    | "Does [item] support displacement
  2    | [source]     | [summary]    |  of [comparator] by [topic] on
  3    | [source]     | [summary]    |  [dim]? [verdict]"
  4    | [source]     | [summary]    | (verbatim for each row)
  5    | [source]     | [summary]    |

  s2_count:                   [N]
  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null / citation]
  s2_delta:                   [+/- confidence delta]
  running_confidence:         [prior + s2_delta]

Running null tally: "[N] null across 1 stage. 2 stages remain."

GATE INSTRUCTION: Do not fire exit signal until s2_count >= 5.
If s2_count < 5, gather additional sources before proceeding.

Write artifact: {topic}-websearch-{date}.md. Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete — s2_count = [N] (gate: >= 5 met). s2_ce_verdict = [value].
   running_confidence = [value]. Stage 3 ready."

---

## STAGE 3 — INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT: websearch_complete
  [ ] RESUME AUDIT: Stage 3 = RUN
  [ ] s2_ce_verdict recorded
  [ ] SESSION INVARIANT D Stage 3 template active

STAGE 3 BODY:
Simulate practitioner interviews.

INCUMBENT CHECK TABLE — Stage 3:

  PRACTITIONER | KEY ACCOUNT  | TEMPLATE APPLIED & VERDICT
  -------------|--------------|------------------------------
  [type 1]     | [account]    | "Does [account] reveal a viable
  [type 2]     | [account]    |  transition path from [comparator]
  [type 3]     | [account]    |  to [topic] for [use case]? [verdict]"

  s3_count:                   [N]
  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null / citation]
  s3_delta:                   [+/- confidence delta]
  running_confidence:         [prior + s3_delta]

Running null tally: "[N] null across 2 stages. 1 stage remains."

GATE INSTRUCTION: Do not fire exit signal until s3_count >= 3.
If s3_count < 3, simulate additional interviews before proceeding.

Write artifact: {topic}-interview-{date}.md. Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete
  "STAGE 3 EXIT: interview_complete — s3_count = [N] (gate: >= 3 met). s3_ce_verdict = [value].
   running_confidence = [value]. Stage 4 ready."

---

## STAGE 4 — PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT: interview_complete
  [ ] RESUME AUDIT: Stage 4 = RUN
  [ ] s3_ce_verdict recorded
  [ ] SESSION INVARIANT D Stage 4 template active

STAGE 4 BODY:

  prototype_design:  [brief description]
  prototype_result:  [what was learned]

INCUMBENT CHECK TABLE — Stage 4:

  ITEM       | RESULT       | TEMPLATE APPLIED & VERDICT
  -----------|--------------|-------------------------------
  prototype  | [result]     | "Does [result] make a credible
             |              |  case for displacing [comparator]
             |              |  with [topic]? [Yes / No / Pending]"

  s4_count:                [N]
  s4_displacement_verdict: [Yes / No / Pending] — required
  s4_ce_verdict:           [null / description]
  s4_delta:                [+/- confidence delta]
  running_confidence:      [prior + s4_delta]

Final null tally:
  null_tally_final = [N]
  Cross-check vs Stage 3: [Match / Mismatch]

GATE INSTRUCTION: Do not fire exit signal until s4_count >= 3.
If s4_count < 3, design additional prototype experiments before proceeding.

Write artifact: {topic}-prototype-{date}.md. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete
  "STAGE 4 EXIT: prototype_complete — s4_count = [N] (gate: >= 3 met). s4_ce_verdict = [value].
   null_tally_final = [N]. Stage 5 ready."

---

## STAGE 5 — SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT: prototype_complete
  [ ] RESUME AUDIT: Stage 5 = RUN
  [ ] null_tally_final recorded
  [ ] counter_hypothesis present
  [ ] All SESSION INVARIANTS active

STAGE 5 BODY:

### BLOCK 1 — CONFIDENCE CHAIN RESOLUTION

  prior:           [value at Stage 1]
  s2_delta:        [from Stage 2]
  s3_delta:        [from Stage 3]
  s4_delta:        [from Stage 4]
  chain_equation:  prior + s2_delta + s3_delta + s4_delta = [final]
  confidence_composite: [final]

### BLOCK 2 — COUNTER-HYPOTHESIS RESOLUTION

  COUNTER_HYPOTHESIS     | VERDICT                                  | EVIDENCE
  -----------------------|------------------------------------------|-------------------
  [from Stage 1]         | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite artifact]

OPEN RISK: reduce confidence_composite one tier.

### BLOCK 3 — DISPLACEMENT INTEGRITY CHECK

  S2 -> [s2_ce_verdict]; S3 -> [s3_ce_verdict]; S4 -> [s4_ce_verdict]
  null_tally_final = [N]; Cross-check: [Match / Mismatch]

If null_tally_final >= 3:
  co_activation_confirmed: dual_lock_fired; confidence_composite -= 2
Else:
  co_activation_confirmed: not_triggered

  s4_displacement_verdict: [from Stage 4]
  displacement_conclusion: [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  Consistency with confidence_composite: [aligned / justification required]

### SYNTHESIS BODY

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences integrating Stages 2, 3, 4]
  confidence_composite:  [final]
  key_risk:              [primary adoption risk]

### HANDOFF TABLE

  FIELD                      | VALUE   | DERIVATION                          | IND. CHAIN
  ---------------------------|---------|-------------------------------------|------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]   | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]     | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]    | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]    | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]    | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]    | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]    | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4 verdicts]   | not through co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]    | not through incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct]     | not through co_activation
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]   | capped by INV B
  schema_compliance_confirmed| [true]  | [all 11 fields, sources match]      | n/a

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete — Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-05 — Full Integration

**Axes**: resume_audit_gate + count_gated_exit_language + trajectory_compute_step +
complete R18 V-05 structural stack (single)
**Hypothesis**: V-01, V-02, V-03 each address one ceiling gap. V-05 assembles all three on
the full R18 V-05 floor (DEPENDENCY column in ROLE OWNERSHIP TABLE for C-17, C-15
tamper-resistant artifact reads at every inter-stage boundary, C-16 three-block Stage 5,
C-18 dual-field momentum+confidence validation, C-20 per-stage delta table in BLOCK 3 with
arc naming) to test whether the full stack simultaneously passes C-08, C-12, and a
strengthened C-19 without sacrificing any existing PASS criteria.

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

ROLE C executes first. Execution order is dependency-driven (C-17).
ORDER CONSTRAINT: ROLE A depends on incumbent_threat_locked from ROLE C;
ROLE A must execute after ROLE C even if declared third. Inversion is causal, not arbitrary.

  ROLE   | TITLE                    | OWNED FIELD               | DEPENDS ON            | EXECUTE
  -------|--------------------------|---------------------------|-----------------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | INCUMBENT ANCHOR      | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared            | scout_artifact glob   | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | incumbent_threat_locked (ROLE C) | THIRD

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

Run before Stage 0. Glob existing artifacts for {topic} on {date}.

ARTIFACT SCAN:
  STAGE | ARTIFACT PATTERN                                       | FOUND | DECISION
  ------|--------------------------------------------------------|-------|------------------
  1     | simulations/prove/{topic}-hypothesis-{date}.md        | [Y/N] | [RESUME-SKIP / RUN]
  2     | simulations/prove/{topic}-websearch-{date}.md         | [Y/N] | [RESUME-SKIP / RUN]
  3     | simulations/prove/{topic}-interview-{date}.md         | [Y/N] | [RESUME-SKIP / RUN]
  4     | simulations/prove/{topic}-prototype-{date}.md         | [Y/N] | [RESUME-SKIP / RUN]
  5     | simulations/prove/{topic}-synthesis-{date}.md         | [Y/N] | [RESUME-SKIP / RUN]

  resume_audit_complete: true
  stages_to_run:         [list RUN stages, or ALL if none found]

RESUME AUDIT EXIT:
  If all five = RESUME-SKIP: "RESUME_AUDIT_EXIT — All artifacts present. Campaign complete."
  Otherwise: "RESUME_AUDIT_PASS — Stages to run: [list]. Proceeding to Stage 0."

---

## STAGE 0 — GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] RESUME AUDIT complete — resume_audit_complete = true
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] SESSION INVARIANTS TABLE complete — all four rows filled, SESSION INVARIANT D
      displacement-question templates registered
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
  [ ] RESUME AUDIT: Stage 1 = RUN (skip body if RESUME-SKIP, advance exit signal)
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered (confirmed by ROLE A)

STAGE 1 BODY:
Load scout artifact. Read signals. Frame hypothesis.

  source_scout_artifact:        [path from ROLE B — copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense — grounded in ROLE C analysis]
  prior_confidence:             [numeric 1-10 baseline before evidence begins]
  gate_s_cleared:               [true — from GATE S Step 2]
  invariant_registry_confirmed: [true — from GATE S Step 3]
  incumbent_threat_locked:      [true — from GATE S Step 1]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked(confidence_prior=[prior_confidence])
  "STAGE 1 EXIT: hypothesis_locked — {topic}-hypothesis-{date}.md written.
   confidence_prior = [value]. Stage 2 ready."

---

## STAGE 2 — WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked(confidence_prior=N)
  [ ] RESUME AUDIT: Stage 2 = RUN
  [ ] hypothesis artifact confirmed written
  [ ] ARTIFACT EXTRACTION: Read {topic}-hypothesis-{date}.md from disk.
      Extract confidence_prior. Validate: signal value = extracted value.
      Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 2 template active

STAGE 2 BODY:
Gather external sources.

INCUMBENT CHECK TABLE — Stage 2 (SESSION INVARIANT D verbatim; DISPLACEMENT DELTA column):

  ITEM | SOURCE       | SUMMARY      | TEMPLATE APPLIED & VERDICT | DISP DELTA (-2 to +2)
  -----|--------------|--------------|----------------------------|----------------------
  1    | [source]     | [summary]    | "Does [item] support        | [delta]
  2    | [source]     | [summary]    |  displacement of [comp]    | [delta]
  3    | [source]     | [summary]    |  by [topic] on [dim]?      | [delta]
  4    | [source]     | [summary]    |  [Yes/No/Inc]"             | [delta]
  5    | [source]     | [summary]    | (verbatim each row)        | [delta]

  s2_count:                    [N]
  s2_displacement_delta_sum:   [sum DISP DELTA column]
  s2_incumbent_check_summary:  [N support / M counter / P inconclusive]
  s2_ce_verdict:               [null / citation]
  s2_confidence_delta:         [+/- numeric]
  running_confidence:          [confidence_prior + s2_confidence_delta]
  displacement_momentum:       [cumulative: s2_displacement_delta_sum]

DUAL-FIELD VALIDATION (C-18):
  Carry both fields forward in exit payload.
  running_confidence and displacement_momentum are independent tamper-resistant chains.

Running null tally: "[N] null across 1 stage. 2 stages remain."

GATE INSTRUCTION: Do not fire exit signal until s2_count >= 5.
If s2_count < 5, gather additional sources before proceeding.

Write artifact: {topic}-websearch-{date}.md. Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete(count=[N], confidence=[running_confidence], momentum=[displacement_momentum])
  "STAGE 2 EXIT: websearch_complete — s2_count = [N] (gate: >= 5 met).
   s2_ce_verdict = [value]. running_confidence = [value]. displacement_momentum = [value].
   Stage 3 ready."

---

## STAGE 3 — INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete(count=N, confidence=C, momentum=M)
  [ ] RESUME AUDIT: Stage 3 = RUN
  [ ] s2_ce_verdict recorded
  [ ] ARTIFACT EXTRACTION (C-15 + C-18): Read {topic}-websearch-{date}.md from disk.
      Extract running_confidence AND displacement_momentum.
      Validate both against signal payload.
      Mismatch on either = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 3 template active

STAGE 3 BODY:
Simulate practitioner interviews.

INCUMBENT CHECK TABLE — Stage 3 (SESSION INVARIANT D verbatim; DISPLACEMENT DELTA column):

  PRACTITIONER | KEY ACCOUNT  | TEMPLATE APPLIED & VERDICT | DISP DELTA (-2 to +2)
  -------------|--------------|----------------------------|----------------------
  [type 1]     | [account]    | "Does [account] reveal a   | [delta]
  [type 2]     | [account]    |  viable transition path    | [delta]
  [type 3]     | [account]    |  from [comp] to [topic]    | [delta]
               |              |  for [use case]? [verdict]"|

  s3_count:                    [N]
  s3_displacement_delta_sum:   [sum DISP DELTA column]
  s3_incumbent_check_summary:  [N support / M counter / P inconclusive]
  s3_ce_verdict:               [null / citation]
  s3_confidence_delta:         [+/- numeric]
  running_confidence:          [prior + s3_confidence_delta]
  displacement_momentum:       [prior + s3_displacement_delta_sum]

DUAL-FIELD VALIDATION: Both running_confidence and displacement_momentum updated and
carried independently. Neither passes through the other.

Running null tally: "[N] null across 2 stages. 1 stage remains."

GATE INSTRUCTION: Do not fire exit signal until s3_count >= 3.
If s3_count < 3, simulate additional practitioner interviews before proceeding.

Write artifact: {topic}-interview-{date}.md. Confirm write.

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

INCUMBENT CHECK TABLE — Stage 4 (SESSION INVARIANT D verbatim; DISPLACEMENT DELTA column):

  ITEM       | RESULT       | TEMPLATE APPLIED & VERDICT           | DISP DELTA (-2 to +2)
  -----------|--------------|--------------------------------------|----------------------
  prototype  | [result]     | "Does [result] make a credible case  | [delta]
             |              |  for displacing [comp] with [topic]? |
             |              |  [Yes / No / Pending]"               |

  s4_count:                    [N]
  s4_displacement_delta_sum:   [delta for Stage 4]
  s4_displacement_verdict:     [Yes / No / Pending] — required; omission = format error
  s4_ce_verdict:               [null / description]
  s4_confidence_delta:         [+/- numeric]
  running_confidence:          [prior + s4_confidence_delta]
  displacement_momentum_final: [prior + s4_displacement_delta_sum]

Final null tally:
  null_tally_final = [N]
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

GATE INSTRUCTION: Do not fire exit signal until s4_count >= 3.
If s4_count < 3, design additional prototype experiments before proceeding.

Write artifact: {topic}-prototype-{date}.md. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[N], confidence=[running_confidence], momentum_final=[displacement_momentum_final])
  "STAGE 4 EXIT: prototype_complete — s4_count = [N] (gate: >= 3 met).
   s4_ce_verdict = [value]. null_tally_final = [N].
   displacement_momentum_final = [value]. Stage 5 ready."

---

## STAGE 5 — SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete(count=N, confidence=C, momentum_final=M)
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

  prior:           [confidence_prior from Stage 1]
  s2_delta:        [s2_confidence_delta]
  s3_delta:        [s3_confidence_delta]
  s4_delta:        [s4_confidence_delta]
  chain_equation:  prior + s2_delta + s3_delta + s4_delta = [final]
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

## Variation Summary

| Variation | Axis | New vs R18 V-05 | C-08 | C-12 | C-19 enhance |
|-----------|------|----------------|------|------|-------------|
| V-01 | resume_audit_gate | RESUME AUDIT block + per-stage RESUME-SKIP/RUN + RESUME_AUDIT_EXIT path | target PASS | baseline | baseline |
| V-02 | count_gated_exit_language | GATE INSTRUCTION in each evidence stage body | baseline | target PASS | baseline |
| V-03 | trajectory_compute_step | TRAJECTORY COMPUTE STEP with trajectory_direction intermediate variable + typed ceiling rule | baseline | baseline | target PASS |
| V-04 | resume_audit_gate + count_gated_exit | V-01 + V-02 combined | target PASS | target PASS | baseline |
| V-05 | all three + full R18 V-05 stack | V-01 + V-02 + V-03 + DEPENDENCY column + C-15/C-18 dual reads + C-20 three-stage chain | target PASS | target PASS | target PASS |

**Primary target**: V-05 closes all three ceiling gaps simultaneously on the full structural baseline.
