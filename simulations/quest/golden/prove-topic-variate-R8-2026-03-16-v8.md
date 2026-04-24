---
skill: quest-variate
skill_target: prove-topic
round: R8
date: 2026-03-16
rubric: prove-topic-rubric-v8-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [stage5_entry_contract_cross_reference, evidence_summary_mandatory_citation, exit_signal_named_provenance]
  combined: [V-04 (C-31+C-30), V-05 (C-30+C-31+C-32 full stack)]
r7_high_scores: >
  V-03 (C-29 PASS -- EXIT SIGNAL chain closure), V-01 (C-27 PASS -- ROLE A contract),
  V-05 (C-27+C-28+C-29 all pass as full stack).
r8_targets: >
  C-30 (evidence_summary instruction mandates all three artifact Displacement reads --
  mandatory language naming websearch/interview/prototype, not conditional),
  C-31 (Stage 5 ENTRY CONDITIONS gate explicitly cross-references ROLE A
  displacement_read_contract by field name -- gate becomes contract-verification step),
  C-32 (Stage 5 EXIT SIGNAL names each artifact type individually in chain closure --
  named-provenance audit trail not count assertion)
severity_stack_gap: >
  R7 V-05 satisfies C-27+C-28+C-29 as full stack but none of the three R8 criteria
  emerge. V-01 isolates C-31. V-02 isolates C-30. V-03 isolates C-32.
  V-04 combines C-31+C-30. V-05 assembles all three on the full structural stack.
---

# prove-topic -- Variation Round R8 (rubric v8)

Five complete, runnable skill body prompts. Each is self-contained -- no diff, no cross-references.

Round 8 targets C-30, C-31, and C-32 -- the three new criteria in rubric v8 derived from R7
excellence signals. These criteria extend the contract-to-synthesis traceability chain:

- **C-31** -- Stage 5 entry gate must explicitly name `displacement_read_contract` by field
  name, converting an independent structural check into a contract-verification step. R7 V-01
  had ROLE A commit the contract; R7 V-02 had Stage 5 gate on chain completeness. No R7
  variation cross-wired them.

- **C-30** -- evidence_summary instruction must be mandatory (naming all three artifact types:
  websearch, interview, prototype), not conditional ("if present"). R7 V-01 failed because
  it mandated only "cite Stage 4 displacement verdict." R7 V-02 failed because instruction
  was conditional. R7 V-03 passed because instruction "explicitly instructs all three reads."

- **C-32** -- Stage 5 EXIT SIGNAL chain closure must name each artifact type individually
  (websearch, interview, prototype) -- not just "all three confirmed." R7 V-03 showed this:
  parenthetical "(websearch, interview, prototype)" converts count assertion to named-provenance.

---

## V-01 -- Axis: Stage 5 Entry Gate Cross-References ROLE A Contract (C-31)

**Variation hypothesis**: Stage 5 ENTRY CONDITIONS displacement chain completeness gate
can be extended to reference `displacement_read_contract` by field name -- without changing
evidence_summary instruction or EXIT SIGNAL wording -- satisfying C-31 as a standalone
structural insertion. C-30 and C-32 do not fire.

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
Do not re-establish the incumbent per stage. Carry forward from CAMPAIGN OPEN.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS TABLE

SESSION INVARIANT D leads. All invariants carry: "cannot be modified or bypassed at
any subsequent stage." Register all four before roles execute.
Canonical failure labels registered here; echoed verbatim at inline enforcement checkpoints.

  ID   | NAME                      | DECLARATION                                               | FAILURE LABEL
  -----|---------------------------|-----------------------------------------------------------|------------------
  D    | INCUMBENT CHECK PHRASING  | Stage 2: "Does [evidence item] support the displacement   | FORMAT ERROR
       | REGISTER                  |   of [incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]      |
       |                           |   by {topic} on [dimension]?                              |
       |                           |   [Yes / No / Inconclusive]"                              |
       |                           | Stage 3: "Does [practitioner account] reveal a viable     |
       |                           |   transition path from [incumbent from CAMPAIGN OPEN      |
       |                           |   INCUMBENT ANCHOR] to {topic} for [use case]?            |
       |                           |   [Yes / No / Inconclusive]"                              |
       |                           | Stage 4: "Does [prototype result] make a credible case    |
       |                           |   for displacing [incumbent from CAMPAIGN OPEN INCUMBENT  |
       |                           |   ANCHOR] with {topic}? [Yes / No / Pending]"             |
       |                           | Binding: [incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]  |
       |                           |   resolves to incumbent_name. Naming as literal string    |
       |                           |   = FORMAT ERROR.                                         |
       |                           | Enforcement: Template deviation = FORMAT ERROR.           |
       |                           | Cannot be modified or bypassed at any stage.              |
  -----|---------------------------|-----------------------------------------------------------|------------------
  A    | ADVERSARIAL REVIEWER      | adversarial_reviewer_type: [role most likely to challenge | DUAL-LOCK ERROR
       | TYPE                      |   the displacement claim]. Activation: null_tally_final   |
       |                           |   >= 3. Cannot be modified or bypassed at synthesis.      |
  -----|---------------------------|-----------------------------------------------------------|------------------
  B    | CONFIDENCE CAP            | null_ce_cap_rule: confidence_composite -= 2 if            | DUAL-LOCK ERROR
       |                           |   null_tally_final >= 3 (hard cap). Cannot be softened.   |
  -----|---------------------------|-----------------------------------------------------------|------------------
  C    | DERIVATION ANNOTATION     | annotation_rule: Every handoff field carries              | FAIL
       |                           |   [derived from: X]. Unlabeled = FAIL.                    |

### ROLE OWNERSHIP TABLE

ROLE C executes first. Roles run in sequence C -> B -> A before Stage 0 begins.
DEPENDENCY column: no role may execute until its listed dependency is satisfied.

  ROLE   | TITLE                    | OWNED FIELD                  | GATE S STEP | EXECUTE | DEPENDENCY
  -------|--------------------------|------------------------------|-------------|---------|------------------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked       | Step 1      | FIRST   | INCUMBENT ANCHOR filled
  ROLE B | SCOUT LOADER             | gate_s_cleared                | Step 2      | SECOND  | ROLE C complete
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed  | Step 3      | THIRD   | ROLE B complete

ROLE C execution (fill now):
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  incumbent_anchor_read:        [INCUMBENT ANCHOR read: resolved incumbent_name confirmed.
                                  Invariant D binding active.]
  displacement_read_contract:   [Stages 2, 3, 4 will write Displacement read field to
                                  artifact bodies. Stage 5 entry will confirm all three.]
  invariant_registry_confirmed: [true when all four invariants registered]

---

## RESUME AUDIT

Run this block before Stage 0. Glob existing artifacts for {topic} on {date}.

  STAGE | ARTIFACT PATTERN                                       | FOUND | DECISION
  ------|--------------------------------------------------------|-------|---------------------
  1     | simulations/prove/{topic}-hypothesis-{date}.md        | [Y/N] | [RESUME-SKIP / RUN]
  2     | simulations/prove/{topic}-websearch-{date}.md         | [Y/N] | [RESUME-SKIP / RUN]
  3     | simulations/prove/{topic}-interview-{date}.md         | [Y/N] | [RESUME-SKIP / RUN]
  4     | simulations/prove/{topic}-prototype-{date}.md         | [Y/N] | [RESUME-SKIP / RUN]
  5     | simulations/prove/{topic}-synthesis-{date}.md         | [Y/N] | [RESUME-SKIP / RUN]

  resume_audit_complete: [true]
  stages_to_run: [list or ALL]

All RESUME-SKIP: "RESUME_AUDIT_EXIT -- Campaign complete." STOP.
Otherwise: "RESUME_AUDIT_PASS -- Stages: [list]. Proceeding to Stage 0."

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] RESUME AUDIT completed -- resume_audit_complete = true
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] SESSION INVARIANTS TABLE complete -- all four rows filled
  [ ] ROLE C executed -- incumbent_threat_locked = true
  [ ] ROLE B executed -- scout_artifact identified and scout_loaded confirmed
  [ ] ROLE A executed -- incumbent_anchor_read confirmed, displacement_read_contract
      committed, invariant_registry_confirmed = true

CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|---------------------------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]

  First BLOCKED step halts campaign. Record step and owning role.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3 all confirmed. SESSION INVARIANT D active.
   ROLE A displacement_read_contract committed. Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] RESUME AUDIT: Stage 1 = RUN
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered

  source_scout_artifact: [path from ROLE B -- copied, not inferred]
  hypothesis:            [falsifiable claim about {topic}]
  counter_hypothesis:    [incumbent's best defense -- grounded in ROLE C analysis]
  confidence_prior:      [1-10 numeric -- initial estimate before evidence]

Write: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked
  "STAGE 1 EXIT: hypothesis_locked -- {topic}-hypothesis-{date}.md written. Stage 2 ready."

---

## STAGE 2 -- WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked
  [ ] RESUME AUDIT: Stage 2 = RUN
  [ ] hypothesis artifact confirmed written
  [ ] SESSION INVARIANT D Stage 2 template active (verbatim from table row D)

Gather minimum 5 external sources.

INCUMBENT CHECK TABLE -- Stage 2 (SESSION INVARIANT D verbatim; DISPLACEMENT DELTA column):

  ITEM | SOURCE              | SUMMARY       | TEMPLATE APPLIED & VERDICT                                              | DISP DELTA
  -----|---------------------|---------------|-------------------------------------------------------------------------|------------
  1    | [source]            | [summary]     | "Does [item] support displacement of [incumbent from CAMPAIGN OPEN      | [delta]
  2    | [source]            | [summary]     |  INCUMBENT ANCHOR] by {topic} on [dim]? [Yes / No / Inconclusive]"     | [delta]
  3    | [source]            | [summary]     | (fill each row verbatim; FORMAT ERROR if template deviates)            | [delta]
  4    | [source]            | [summary]     |                                                                         | [delta]
  5    | [source]            | [summary]     |                                                                         | [delta]

  s2_count:                   [N] -- must be >= 5
  s2_displacement_delta_sum:  [sum of DISP DELTA column]
  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]
  s2_confidence_delta:        [+/- numeric]
  running_confidence:         [confidence_prior + s2_confidence_delta]
  Displacement read:          [one sentence: does Stage 2 evidence support displacement?]

Write: {topic}-websearch-{date}.md. Artifact body includes Displacement read field. Confirm write.
Gate: Do not fire exit signal until s2_count >= 5.

STAGE 2 EXIT SIGNAL: websearch_complete(count=[N], confidence=[running_confidence], momentum=[s2_displacement_delta_sum])
  "STAGE 2 EXIT: websearch_complete -- s2_count = [N] (gate: >= 5 met).
   s2_ce_verdict = [value]. running_confidence = [value]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete(count=N, confidence=C, momentum=M)
  [ ] RESUME AUDIT: Stage 3 = RUN
  [ ] s2_ce_verdict recorded
  [ ] Read {topic}-websearch-{date}.md from disk. Extract running_confidence.
      Validate against signal payload. Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 3 template active

Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D verbatim; DISPLACEMENT DELTA column):

  PRACTITIONER | KEY ACCOUNT       | TEMPLATE APPLIED & VERDICT                                                      | DISP DELTA
  -------------|-------------------|---------------------------------------------------------------------------------|------------
  [type 1]     | [quote/paraphrase]| "Does [account] reveal a viable transition path from [incumbent from CAMPAIGN   | [delta]
  [type 2]     | [quote/paraphrase]|  OPEN INCUMBENT ANCHOR] to {topic} for [use case]? [Yes / No / Inconclusive]"  | [delta]
  [type 3]     | [quote/paraphrase]| (fill each row verbatim; FORMAT ERROR if template deviates)                    | [delta]

  s3_count:                    [N] -- must be >= 3
  s3_displacement_delta_sum:   [sum of DISP DELTA column]
  s3_incumbent_check_summary:  [N support / M counter / P inconclusive]
  s3_ce_verdict:               [null if no CE; cite account if found]
  s3_confidence_delta:         [+/- numeric]
  running_confidence:          [prior + s3_confidence_delta]
  displacement_momentum:       [s2_displacement_delta_sum + s3_displacement_delta_sum]
  Displacement read:           [one sentence: does practitioner evidence support transition?]

Write: {topic}-interview-{date}.md. Artifact body includes Displacement read field. Confirm write.
Gate: Do not fire exit signal until s3_count >= 3.

STAGE 3 EXIT SIGNAL: interview_complete(count=[N], confidence=[running_confidence], momentum=[displacement_momentum])
  "STAGE 3 EXIT: interview_complete -- s3_count = [N] (gate: >= 3 met).
   s3_ce_verdict = [value]. running_confidence = [value]. displacement_momentum = [value].
   Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete(count=N, confidence=C, momentum=M)
  [ ] RESUME AUDIT: Stage 4 = RUN
  [ ] s3_ce_verdict recorded
  [ ] Read {topic}-interview-{date}.md from disk. Extract running_confidence AND
      displacement_momentum. Validate both against signal payload.
      Mismatch on either = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 4 template active

  prototype_design:  [brief description]
  prototype_result:  [what was learned -- 1-3 sentences]

INCUMBENT CHECK TABLE -- Stage 4 (SESSION INVARIANT D verbatim; DISPLACEMENT DELTA column):

  ITEM      | RESULT             | TEMPLATE APPLIED & VERDICT                                                          | DISP DELTA
  ----------|--------------------|-------------------------------------------------------------------------------------|-----------
  prototype | [prototype_result] | "Does [result] make a credible case for displacing [incumbent from CAMPAIGN OPEN    | [delta]
            |                    |  INCUMBENT ANCHOR] with {topic}? [Yes / No / Pending]"                             |

  s4_count:                    [N] -- must be >= 3
  s4_displacement_delta_sum:   [delta for Stage 4]
  s4_displacement_verdict:     [Yes / No / Pending] -- required; omission = format error
  s4_ce_verdict:               [null / description]
  s4_confidence_delta:         [+/- numeric]
  running_confidence:          [prior + s4_confidence_delta]
  displacement_momentum_final: [displacement_momentum + s4_displacement_delta_sum]
  Displacement read:           [one sentence: does prototype make credible displacement case?]

Write: {topic}-prototype-{date}.md. Artifact body includes Displacement read field. Confirm write.
Gate: Do not fire exit signal until s4_count >= 3.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[N], confidence=[running_confidence], momentum_final=[displacement_momentum_final])
  "STAGE 4 EXIT: prototype_complete -- s4_count = [N] (gate: >= 3 met).
   running_confidence = [value]. displacement_momentum_final = [value].
   s4_ce_verdict = [value]. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete(count=N, confidence=C, momentum_final=M)
  [ ] RESUME AUDIT: Stage 5 = RUN
  [ ] Read {topic}-prototype-{date}.md from disk. Extract running_confidence AND
      displacement_momentum_final. Validate both against signal payload.
      Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 present for resolution
  [ ] All four SESSION INVARIANT TABLE rows active
  [ ] All three artifact Displacement read fields confirmed written
      [per ROLE A displacement_read_contract -- websearch, interview, prototype].
      Missing Displacement read in any artifact = CHAIN INTEGRITY FAILURE. Halt.

### BLOCK 1 -- CONFIDENCE CHAIN RESOLUTION

  prior:                [confidence_prior from Stage 1]
  s2_delta:             [s2_confidence_delta]
  s3_delta:             [s3_confidence_delta]
  s4_delta:             [s4_confidence_delta]
  chain_equation:       prior + s2_delta + s3_delta + s4_delta = [final]
  confidence_composite: [final -- before counter-hypothesis and cap adjustments]

### BLOCK 2 -- COUNTER-HYPOTHESIS RESOLUTION

  COUNTER_HYPOTHESIS   | VERDICT                                  | EVIDENCE
  ---------------------|------------------------------------------|------------------
  [from Stage 1]       | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite artifact]

OPEN RISK: reduce confidence_composite one tier before BLOCK 3.

### BLOCK 3 -- DISPLACEMENT INTEGRITY CHECK

NULL TALLY CHAIN:
  S2 -> [s2_ce_verdict]  S3 -> [s3_ce_verdict]  S4 -> [s4_ce_verdict]
  null_tally_final = [N]
  Cross-check: [Match / Mismatch]

If null_tally_final >= 3: dual_lock_fired (Lock 1: adversarial review, Lock 2: -= 2)
Else: co_activation_confirmed: not_triggered

THREE-STAGE DISPLACEMENT CHAIN:
STANCE: SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED. Y/N = FORMAT ERROR.

  STAGE | DISP DELTA SUM | CUMUL MOMENTUM | STANCE                                            | FLAG?
  ------|----------------|----------------|---------------------------------------------------|------
  S2    | [s2_disp_sum]  | [s2_cumul]     | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]
  S3    | [s3_disp_sum]  | [s3_cumul]     | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]
  S4    | [s4_disp_sum]  | [s4_cumul]     | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]

  chain_pattern:            [ACCELERATING / STEADY_BUILD / PLATEAU / LATE_REVERSAL / ...]
  displacement_conclusion:  [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  conclusion_justification: [required if any FLAG = Y]
  incumbent_defense_closed: [true when all flagged rows reconciled]

### SYNTHESIS DECLARATIONS

Do not embed these values in prose sentences. Each on its own line, extractable by label match.

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences integrating Stages 2, 3, 4 -- cite Stage 4
                           displacement verdict explicitly and cite artifact Displacement
                           reads where available]
  confidence_composite:  [final value after all adjustments]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### HANDOFF TABLE

All 11 fields required. Every field: [derived from: X]. Unlabeled = FAIL.

  FIELD                    | VALUE   | DERIVED FROM
  -------------------------|---------|----------------------------------
  scout_anchor             | [value] | [derived from: ROLE B]
  incumbent_threat_locked  | [value] | [derived from: ROLE C]
  hypothesis               | [value] | [derived from: Stage 1]
  counter_hypothesis       | [value] | [derived from: Stage 1]
  s2_ce_verdict            | [value] | [derived from: Stage 2]
  s3_ce_verdict            | [value] | [derived from: Stage 3]
  s4_ce_verdict            | [value] | [derived from: Stage 4]
  null_tally_final         | [value] | [derived from: Stage 4 + Stage 5]
  co_activation_confirmed  | [value] | [derived from: Stage 5 Block 3]
  incumbent_defense_closed | [value] | [derived from: Stage 5 Block 3]
  confidence_composite     | [value] | [derived from: Stage 5 Block 1]
  schema_compliance_confirmed | [true] | [Invariant E checkpoint -- FAIL if any field unlabeled]

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story.
   All three artifact Displacement reads confirmed in evidence_summary."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-02 -- Axis: evidence_summary Instruction Mandates All Three Reads (C-30)

**Variation hypothesis**: Replacing the advisory/Stage-4-only evidence_summary citation
instruction with an explicit mandatory instruction naming all three artifact types
(websearch, interview, prototype) satisfies C-30 as a standalone syntactic change in
Stage 5 SYNTHESIS DECLARATIONS. C-31 does not fire (entry gate does not name
`displacement_read_contract`). C-32 does not fire (EXIT SIGNAL uses count-assertion form).

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
Do not re-establish the incumbent per stage. Carry forward from CAMPAIGN OPEN.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS TABLE

SESSION INVARIANT D leads. All invariants carry: "cannot be modified or bypassed at
any subsequent stage." Register all four before roles execute.
Canonical failure labels registered here; echoed verbatim at inline enforcement checkpoints.

  ID   | NAME                      | DECLARATION                                               | FAILURE LABEL
  -----|---------------------------|-----------------------------------------------------------|------------------
  D    | INCUMBENT CHECK PHRASING  | Stage 2: "Does [evidence item] support the displacement   | FORMAT ERROR
       | REGISTER                  |   of [incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]      |
       |                           |   by {topic} on [dimension]?                              |
       |                           |   [Yes / No / Inconclusive]"                              |
       |                           | Stage 3: "Does [practitioner account] reveal a viable     |
       |                           |   transition path from [incumbent from CAMPAIGN OPEN      |
       |                           |   INCUMBENT ANCHOR] to {topic} for [use case]?            |
       |                           |   [Yes / No / Inconclusive]"                              |
       |                           | Stage 4: "Does [prototype result] make a credible case    |
       |                           |   for displacing [incumbent from CAMPAIGN OPEN INCUMBENT  |
       |                           |   ANCHOR] with {topic}? [Yes / No / Pending]"             |
       |                           | Binding: [incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]  |
       |                           |   resolves to incumbent_name. Literal string = FORMAT ERROR.|
       |                           | Enforcement: Template deviation = FORMAT ERROR.           |
       |                           | Cannot be modified or bypassed at any stage.              |
  -----|---------------------------|-----------------------------------------------------------|------------------
  A    | ADVERSARIAL REVIEWER      | adversarial_reviewer_type: [challenge role].              | DUAL-LOCK ERROR
       | TYPE                      | Activation: null_tally_final >= 3.                        |
  -----|---------------------------|-----------------------------------------------------------|------------------
  B    | CONFIDENCE CAP            | confidence_composite -= 2 if null_tally_final >= 3.       | DUAL-LOCK ERROR
  -----|---------------------------|-----------------------------------------------------------|------------------
  C    | DERIVATION ANNOTATION     | Every handoff field: [derived from: X]. Unlabeled = FAIL. | FAIL

### ROLE OWNERSHIP TABLE

Roles run C -> B -> A. DEPENDENCY column enforced.

  ROLE   | TITLE                    | OWNED FIELD                  | GATE S STEP | EXECUTE | DEPENDENCY
  -------|--------------------------|------------------------------|-------------|---------|------------------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked       | Step 1      | FIRST   | INCUMBENT ANCHOR filled
  ROLE B | SCOUT LOADER             | gate_s_cleared                | Step 2      | SECOND  | ROLE C complete
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed  | Step 3      | THIRD   | ROLE B complete

ROLE C execution (fill now):
  incumbent_threat_locked: [true when name, strength, vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  incumbent_anchor_read:        [INCUMBENT ANCHOR read: resolved incumbent_name confirmed.
                                  Invariant D binding active.]
  displacement_read_contract:   [Stages 2, 3, 4 will write Displacement read field to
                                  artifact bodies. Stage 5 entry will confirm all three.]
  invariant_registry_confirmed: [true when all four invariants registered]

---

## RESUME AUDIT

Glob existing artifacts for {topic} on {date} before Stage 0.

  STAGE | ARTIFACT PATTERN                                | FOUND | DECISION
  ------|-------------------------------------------------|-------|---------------------
  1     | simulations/prove/{topic}-hypothesis-{date}.md | [Y/N] | [RESUME-SKIP / RUN]
  2     | simulations/prove/{topic}-websearch-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  3     | simulations/prove/{topic}-interview-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  4     | simulations/prove/{topic}-prototype-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  5     | simulations/prove/{topic}-synthesis-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]

  resume_audit_complete: [true]  stages_to_run: [list or ALL]

All RESUME-SKIP: "RESUME_AUDIT_EXIT -- Campaign complete." STOP.
Otherwise: "RESUME_AUDIT_PASS -- Stages: [list]. Proceeding to Stage 0."

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] RESUME AUDIT completed  [ ] CAMPAIGN OPEN filled  [ ] INCUMBENT ANCHOR filled
  [ ] SESSION INVARIANTS TABLE complete
  [ ] ROLE C: incumbent_threat_locked = true
  [ ] ROLE B: scout loaded confirmed
  [ ] ROLE A: incumbent_anchor_read confirmed, displacement_read_contract committed,
      invariant_registry_confirmed = true

CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | RESULT
  -----|------------------------------|---------|---------------------
  1    | incumbent_threat_locked      | ROLE C  | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | [confirm or BLOCKED]

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3 confirmed. SESSION INVARIANT D active.
   Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] gate_open received  [ ] Stage 1 = RUN  [ ] scout_artifact available
  [ ] SESSION INVARIANT D templates registered

  source_scout_artifact: [path from ROLE B -- copied, not inferred]
  hypothesis:            [falsifiable claim about {topic}]
  counter_hypothesis:    [incumbent's best defense]
  confidence_prior:      [1-10 numeric]

Write: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked
  "STAGE 1 EXIT: hypothesis_locked -- {topic}-hypothesis-{date}.md written. Stage 2 ready."

---

## STAGE 2 -- WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] hypothesis_locked received  [ ] Stage 2 = RUN  [ ] Invariant D Stage 2 template active

Gather minimum 5 external sources.

INCUMBENT CHECK TABLE -- Stage 2 (SESSION INVARIANT D verbatim; DISP DELTA column):

  ITEM | SOURCE   | SUMMARY   | TEMPLATE APPLIED & VERDICT                                              | DISP DELTA
  -----|----------|-----------|-------------------------------------------------------------------------|------------
  1    | [source] | [summary] | "Does [item] support displacement of [incumbent from CAMPAIGN OPEN      | [delta]
  2    | [source] | [summary] |  INCUMBENT ANCHOR] by {topic} on [dim]? [Yes / No / Inconclusive]"     | [delta]
  3    | [source] | [summary] | (fill each row verbatim; FORMAT ERROR if template deviates)            | [delta]
  4    | [source] | [summary] |                                                                         | [delta]
  5    | [source] | [summary] |                                                                         | [delta]

  s2_count: [N>=5]  s2_displacement_delta_sum: [sum]  s2_ce_verdict: [null/value]
  s2_confidence_delta: [+/-]  running_confidence: [prior+delta]
  Displacement read: [one sentence displacement verdict]

Write: {topic}-websearch-{date}.md. Artifact body includes Displacement read field. Confirm write.
Gate: s2_count >= 5.

STAGE 2 EXIT SIGNAL: websearch_complete(count=[N], confidence=[running_confidence], momentum=[s2_displacement_delta_sum])
  "STAGE 2 EXIT: websearch_complete -- s2_count = [N]. running_confidence = [value]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] websearch_complete received  [ ] Stage 3 = RUN  [ ] s2_ce_verdict recorded
  [ ] Read websearch artifact. Extract running_confidence. Validate vs payload.
      Mismatch = CHAIN INTEGRITY FAILURE.
  [ ] Invariant D Stage 3 template active

Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D verbatim; DISP DELTA column):

  PRACTITIONER | ACCOUNT           | TEMPLATE APPLIED & VERDICT                                                      | DISP DELTA
  -------------|-------------------|---------------------------------------------------------------------------------|------------
  [type 1]     | [quote/paraphrase]| "Does [account] reveal a viable transition path from [incumbent from CAMPAIGN   | [delta]
  [type 2]     | [quote/paraphrase]|  OPEN INCUMBENT ANCHOR] to {topic} for [use case]? [Yes / No / Inconclusive]"  | [delta]
  [type 3]     | [quote/paraphrase]| (verbatim; FORMAT ERROR if deviates)                                           | [delta]

  s3_count: [N>=3]  s3_displacement_delta_sum: [sum]  s3_ce_verdict: [null/value]
  s3_confidence_delta: [+/-]  running_confidence: [prior+delta]
  displacement_momentum: [s2+s3 sums]
  Displacement read: [one sentence]

Write: {topic}-interview-{date}.md. Artifact body includes Displacement read field. Confirm write.
Gate: s3_count >= 3.

STAGE 3 EXIT SIGNAL: interview_complete(count=[N], confidence=[running_confidence], momentum=[displacement_momentum])
  "STAGE 3 EXIT: interview_complete -- s3_count = [N]. running_confidence = [value].
   displacement_momentum = [value]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] interview_complete received  [ ] Stage 4 = RUN  [ ] s3_ce_verdict recorded
  [ ] Read interview artifact. Extract running_confidence AND displacement_momentum.
      Validate both. Mismatch = CHAIN INTEGRITY FAILURE.
  [ ] Invariant D Stage 4 template active

  prototype_design: [description]  prototype_result: [what was learned]

INCUMBENT CHECK TABLE -- Stage 4 (SESSION INVARIANT D verbatim):

  ITEM      | RESULT  | TEMPLATE APPLIED & VERDICT                                                           | DISP DELTA
  ----------|---------|--------------------------------------------------------------------------------------|------------
  prototype | [res]   | "Does [result] make a credible case for displacing [incumbent from CAMPAIGN OPEN    | [delta]
            |         |  INCUMBENT ANCHOR] with {topic}? [Yes / No / Pending]"                             |

  s4_count: [N>=3]  s4_displacement_delta_sum: [delta]  s4_displacement_verdict: [Yes/No/Pending]
  s4_ce_verdict: [null/value]  s4_confidence_delta: [+/-]
  running_confidence: [prior+delta]  displacement_momentum_final: [prior+delta]
  Displacement read: [one sentence]

Write: {topic}-prototype-{date}.md. Artifact body includes Displacement read field. Confirm write.
Gate: s4_count >= 3.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[N], confidence=[running_confidence], momentum_final=[displacement_momentum_final])
  "STAGE 4 EXIT: prototype_complete -- s4_count = [N]. running_confidence = [value].
   displacement_momentum_final = [value]. s4_ce_verdict = [value]. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] prototype_complete received
  [ ] Stage 5 = RUN
  [ ] Read prototype artifact. Extract running_confidence AND displacement_momentum_final.
      Validate both. Mismatch = CHAIN INTEGRITY FAILURE.
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 present
  [ ] All four SESSION INVARIANT TABLE rows active
  [ ] All three artifact Displacement read fields confirmed written (websearch, interview,
      prototype). Stage 5 will consume all three.

### BLOCK 1 -- CONFIDENCE CHAIN RESOLUTION

  prior + s2_delta + s3_delta + s4_delta = confidence_composite: [value]

### BLOCK 2 -- COUNTER-HYPOTHESIS RESOLUTION

  COUNTER_HYPOTHESIS | VERDICT                                  | EVIDENCE
  -------------------|------------------------------------------|--------------------
  [from Stage 1]     | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite artifact]

OPEN RISK: reduce confidence_composite one tier.

### BLOCK 3 -- DISPLACEMENT INTEGRITY CHECK

  S2->[s2_ce_verdict]  S3->[s3_ce_verdict]  S4->[s4_ce_verdict]  null_tally_final=[N]
  Cross-check: [Match / Mismatch]
  >= 3: dual_lock_fired | else: not_triggered

THREE-STAGE DISPLACEMENT CHAIN (STANCE required; Y/N = FORMAT ERROR):

  STAGE | DISP DELTA | CUMUL MOMENTUM | STANCE                                            | FLAG
  ------|------------|----------------|---------------------------------------------------|-----
  S2    | [sum]      | [cumul]        | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]
  S3    | [sum]      | [cumul]        | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]
  S4    | [sum]      | [cumul]        | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]

  chain_pattern: [ACCELERATING / STEADY_BUILD / PLATEAU / LATE_REVERSAL / ...]
  displacement_conclusion: [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  incumbent_defense_closed: [true when flagged rows reconciled]

### SYNTHESIS DECLARATIONS

Do not embed in prose. Each field on its own line, extractable by label match.

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences. Must cite all three artifact Displacement reads
                           (mandatory -- not conditional):
                           websearch Displacement read:  [value from {topic}-websearch-{date}.md]
                           interview Displacement read:  [value from {topic}-interview-{date}.md]
                           prototype Displacement read:  [value from {topic}-prototype-{date}.md]
                           Omission of any artifact Displacement read = FAIL.]
  confidence_composite:  [final value after all adjustments]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### HANDOFF TABLE

All 11 fields required. Every field: [derived from: X]. Unlabeled = FAIL.

  FIELD                    | VALUE   | DERIVED FROM
  -------------------------|---------|----------------------------------
  scout_anchor             | [value] | [derived from: ROLE B]
  incumbent_threat_locked  | [value] | [derived from: ROLE C]
  hypothesis               | [value] | [derived from: Stage 1]
  counter_hypothesis       | [value] | [derived from: Stage 1]
  s2_ce_verdict            | [value] | [derived from: Stage 2]
  s3_ce_verdict            | [value] | [derived from: Stage 3]
  s4_ce_verdict            | [value] | [derived from: Stage 4]
  null_tally_final         | [value] | [derived from: Stage 4 + Stage 5]
  co_activation_confirmed  | [value] | [derived from: Stage 5 Block 3]
  incumbent_defense_closed | [value] | [derived from: Stage 5 Block 3]
  confidence_composite     | [value] | [derived from: Stage 5 Block 1]
  schema_compliance_confirmed | [true] | [Invariant E checkpoint -- FAIL if any field unlabeled]

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story.
   All three artifact Displacement reads cited in evidence_summary."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-03 -- Axis: EXIT SIGNAL Names Each Artifact Type Individually (C-32)

**Variation hypothesis**: Extending Stage 5 EXIT SIGNAL chain closure to enumerate each
artifact type individually by name satisfies C-32 as a standalone one-line change.
C-30 does not fire (evidence_summary instruction is not mandatory-language).
C-31 does not fire (entry gate does not reference `displacement_read_contract`).

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
Do not re-establish the incumbent per stage. Carry forward from CAMPAIGN OPEN.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS TABLE

SESSION INVARIANT D leads. All invariants carry: "cannot be modified or bypassed at
any subsequent stage." Register all four before roles execute.
Canonical failure labels registered here; echoed verbatim at inline enforcement checkpoints.

  ID   | NAME                      | DECLARATION                                               | FAILURE LABEL
  -----|---------------------------|-----------------------------------------------------------|------------------
  D    | INCUMBENT CHECK PHRASING  | Stage 2: "Does [evidence item] support the displacement   | FORMAT ERROR
       | REGISTER                  |   of [incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]      |
       |                           |   by {topic} on [dimension]?                              |
       |                           |   [Yes / No / Inconclusive]"                              |
       |                           | Stage 3: "Does [practitioner account] reveal a viable     |
       |                           |   transition path from [incumbent from CAMPAIGN OPEN      |
       |                           |   INCUMBENT ANCHOR] to {topic} for [use case]?            |
       |                           |   [Yes / No / Inconclusive]"                              |
       |                           | Stage 4: "Does [prototype result] make a credible case    |
       |                           |   for displacing [incumbent from CAMPAIGN OPEN INCUMBENT  |
       |                           |   ANCHOR] with {topic}? [Yes / No / Pending]"             |
       |                           | Binding: [incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]  |
       |                           |   resolves to incumbent_name. Literal string = FORMAT ERROR.|
       |                           | Enforcement: Template deviation = FORMAT ERROR.           |
  -----|---------------------------|-----------------------------------------------------------|------------------
  A    | ADVERSARIAL REVIEWER TYPE | adversarial_reviewer_type: [challenge role].              | DUAL-LOCK ERROR
       |                           | Activation: null_tally_final >= 3.                        |
  -----|---------------------------|-----------------------------------------------------------|------------------
  B    | CONFIDENCE CAP            | confidence_composite -= 2 if null_tally_final >= 3.       | DUAL-LOCK ERROR
  -----|---------------------------|-----------------------------------------------------------|------------------
  C    | DERIVATION ANNOTATION     | Every handoff field: [derived from: X]. Unlabeled = FAIL. | FAIL

### ROLE OWNERSHIP TABLE

Roles run C -> B -> A. DEPENDENCY column enforced.

  ROLE   | TITLE                    | OWNED FIELD                  | EXECUTE | DEPENDENCY
  -------|--------------------------|------------------------------|---------|------------------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked       | FIRST   | INCUMBENT ANCHOR filled
  ROLE B | SCOUT LOADER             | gate_s_cleared                | SECOND  | ROLE C complete
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed  | THIRD   | ROLE B complete

ROLE C execution (fill now):
  incumbent_threat_locked: [true when name, strength, vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  incumbent_anchor_read:        [INCUMBENT ANCHOR read: resolved incumbent_name confirmed.
                                  Invariant D binding active.]
  displacement_read_contract:   [Stages 2, 3, 4 will write Displacement read field to
                                  artifact bodies. Stage 5 entry will confirm all three.]
  invariant_registry_confirmed: [true when all four invariants registered]

---

## RESUME AUDIT

Glob existing artifacts before Stage 0.

  STAGE | ARTIFACT PATTERN                                | FOUND | DECISION
  ------|-------------------------------------------------|-------|---------------------
  1     | simulations/prove/{topic}-hypothesis-{date}.md | [Y/N] | [RESUME-SKIP / RUN]
  2     | simulations/prove/{topic}-websearch-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  3     | simulations/prove/{topic}-interview-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  4     | simulations/prove/{topic}-prototype-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  5     | simulations/prove/{topic}-synthesis-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]

  resume_audit_complete: [true]  stages_to_run: [list or ALL]

All RESUME-SKIP: STOP. Otherwise: proceed to Stage 0.

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] RESUME AUDIT complete  [ ] CAMPAIGN OPEN + INCUMBENT ANCHOR filled
  [ ] SESSION INVARIANTS TABLE complete
  [ ] ROLE C: incumbent_threat_locked = true
  [ ] ROLE B: scout loaded  [ ] ROLE A: all fields confirmed

CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | RESULT
  -----|------------------------------|---------|---------------------
  1    | incumbent_threat_locked      | ROLE C  | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | [confirm or BLOCKED]

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3 confirmed. Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] gate_open received  [ ] Stage 1 = RUN  [ ] scout_artifact available

  source_scout_artifact: [path from ROLE B]
  hypothesis:            [falsifiable claim]
  counter_hypothesis:    [incumbent's best defense]
  confidence_prior:      [1-10]

Write: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked
  "STAGE 1 EXIT: hypothesis_locked -- written. Stage 2 ready."

---

## STAGE 2 -- WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] hypothesis_locked received  [ ] Stage 2 = RUN  [ ] Invariant D Stage 2 template active

Gather minimum 5 sources.

INCUMBENT CHECK TABLE -- Stage 2 (SESSION INVARIANT D verbatim):

  ITEM | SOURCE   | SUMMARY   | TEMPLATE & VERDICT                                                              | DISP DELTA
  -----|----------|-----------|---------------------------------------------------------------------------------|------------
  1    | [src]    | [sum]     | "Does [item] support displacement of [incumbent from CAMPAIGN OPEN INCUMBENT    | [delta]
  2    | [src]    | [sum]     |  ANCHOR] by {topic} on [dim]? [Yes / No / Inconclusive]" (verbatim each row)   | [delta]
  3    | [src]    | [sum]     |                                                                                 | [delta]
  4    | [src]    | [sum]     |                                                                                 | [delta]
  5    | [src]    | [sum]     |                                                                                 | [delta]

  s2_count: [N>=5]  s2_displacement_delta_sum: [sum]  s2_ce_verdict: [null/value]
  s2_confidence_delta: [+/-]  running_confidence: [prior+delta]
  Displacement read: [one sentence]

Write: {topic}-websearch-{date}.md (includes Displacement read). Confirm write.
Gate: s2_count >= 5.

STAGE 2 EXIT SIGNAL: websearch_complete(count=[N], confidence=[running_confidence], momentum=[s2_displacement_delta_sum])
  "STAGE 2 EXIT: websearch_complete -- s2_count=[N]. running_confidence=[value]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] websearch_complete received  [ ] Stage 3 = RUN  [ ] s2_ce_verdict recorded
  [ ] Read websearch artifact. Extract running_confidence. Validate vs payload. Mismatch = CHAIN INTEGRITY FAILURE.
  [ ] Invariant D Stage 3 template active

Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D verbatim):

  PRACTITIONER | ACCOUNT    | TEMPLATE & VERDICT                                                            | DISP DELTA
  -------------|------------|-------------------------------------------------------------------------------|------------
  [type 1]     | [account]  | "Does [account] reveal a viable transition path from [incumbent from CAMPAIGN | [delta]
  [type 2]     | [account]  |  OPEN INCUMBENT ANCHOR] to {topic} for [use case]? [Yes / No / Inconclusive]" | [delta]
  [type 3]     | [account]  |                                                                               | [delta]

  s3_count: [N>=3]  s3_displacement_delta_sum: [sum]  s3_ce_verdict: [null/value]
  s3_confidence_delta: [+/-]  running_confidence: [prior+delta]
  displacement_momentum: [s2+s3]  Displacement read: [one sentence]

Write: {topic}-interview-{date}.md (includes Displacement read). Confirm write.
Gate: s3_count >= 3.

STAGE 3 EXIT SIGNAL: interview_complete(count=[N], confidence=[running_confidence], momentum=[displacement_momentum])
  "STAGE 3 EXIT: interview_complete -- s3_count=[N]. running_confidence=[value].
   displacement_momentum=[value]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] interview_complete received  [ ] Stage 4 = RUN  [ ] s3_ce_verdict recorded
  [ ] Read interview artifact. Extract running_confidence AND displacement_momentum.
      Validate both. Mismatch = CHAIN INTEGRITY FAILURE.
  [ ] Invariant D Stage 4 template active

  prototype_design: [description]  prototype_result: [what was learned]

INCUMBENT CHECK TABLE -- Stage 4:

  ITEM      | RESULT  | TEMPLATE & VERDICT                                                           | DISP DELTA
  ----------|---------|------------------------------------------------------------------------------|------------
  prototype | [res]   | "Does [result] make a credible case for displacing [incumbent from CAMPAIGN  | [delta]
            |         |  OPEN INCUMBENT ANCHOR] with {topic}? [Yes / No / Pending]"                 |

  s4_count: [N>=3]  s4_displacement_delta_sum: [delta]  s4_displacement_verdict: [Yes/No/Pending]
  s4_ce_verdict: [null/value]  s4_confidence_delta: [+/-]
  running_confidence: [prior+delta]  displacement_momentum_final: [prior+delta]
  Displacement read: [one sentence]

Write: {topic}-prototype-{date}.md (includes Displacement read). Confirm write.
Gate: s4_count >= 3.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[N], confidence=[running_confidence], momentum_final=[displacement_momentum_final])
  "STAGE 4 EXIT: prototype_complete -- s4_count=[N]. running_confidence=[value].
   displacement_momentum_final=[value]. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] prototype_complete received
  [ ] Stage 5 = RUN
  [ ] Read prototype artifact. Extract running_confidence AND displacement_momentum_final.
      Validate both. Mismatch = CHAIN INTEGRITY FAILURE.
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 present
  [ ] All four SESSION INVARIANT TABLE rows active
  [ ] All three artifact Displacement read fields confirmed written (websearch, interview,
      prototype). Stage 5 will consume all three.

### BLOCK 1 -- CONFIDENCE CHAIN RESOLUTION

  prior + s2_delta + s3_delta + s4_delta = confidence_composite: [value]

### BLOCK 2 -- COUNTER-HYPOTHESIS RESOLUTION

  COUNTER_HYPOTHESIS | VERDICT                                  | EVIDENCE
  -------------------|------------------------------------------|--------------------
  [from Stage 1]     | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite artifact]

OPEN RISK: reduce confidence_composite one tier.

### BLOCK 3 -- DISPLACEMENT INTEGRITY CHECK

  S2->[s2_ce_verdict]  S3->[s3_ce_verdict]  S4->[s4_ce_verdict]  null_tally_final=[N]
  Cross-check: [Match / Mismatch]
  >= 3: dual_lock_fired | else: not_triggered

THREE-STAGE DISPLACEMENT CHAIN (STANCE required; Y/N = FORMAT ERROR):

  STAGE | DISP DELTA | CUMUL MOMENTUM | STANCE                                            | FLAG
  ------|------------|----------------|---------------------------------------------------|-----
  S2    | [sum]      | [cumul]        | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]
  S3    | [sum]      | [cumul]        | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]
  S4    | [sum]      | [cumul]        | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]

  chain_pattern: [ACCELERATING / STEADY_BUILD / PLATEAU / LATE_REVERSAL / ...]
  displacement_conclusion: [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  incumbent_defense_closed: [true when flagged rows reconciled]

### SYNTHESIS DECLARATIONS

Do not embed in prose. Each field on its own line, extractable by label match.

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences integrating Stages 2, 3, 4 -- cite Stage 4
                           displacement verdict explicitly and cite artifact Displacement
                           reads where available]
  confidence_composite:  [final value after all adjustments]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### HANDOFF TABLE

All 11 fields required. Every field: [derived from: X]. Unlabeled = FAIL.

  FIELD                    | VALUE   | DERIVED FROM
  -------------------------|---------|----------------------------------
  scout_anchor             | [value] | [derived from: ROLE B]
  incumbent_threat_locked  | [value] | [derived from: ROLE C]
  hypothesis               | [value] | [derived from: Stage 1]
  counter_hypothesis       | [value] | [derived from: Stage 1]
  s2_ce_verdict            | [value] | [derived from: Stage 2]
  s3_ce_verdict            | [value] | [derived from: Stage 3]
  s4_ce_verdict            | [value] | [derived from: Stage 4]
  null_tally_final         | [value] | [derived from: Stage 4 + Stage 5]
  co_activation_confirmed  | [value] | [derived from: Stage 5 Block 3]
  incumbent_defense_closed | [value] | [derived from: Stage 5 Block 3]
  confidence_composite     | [value] | [derived from: Stage 5 Block 1]
  schema_compliance_confirmed | [true] | [Invariant E checkpoint -- FAIL if any field unlabeled]

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story.
   Displacement read chain closed: websearch Displacement read, interview Displacement read,
   prototype Displacement read -- all three cited in evidence_summary."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-04 -- Axes: C-31 + C-30 Combined (Entry Gate Contract Reference + Mandatory Citation)

**Variation hypothesis**: Combining C-31 (entry gate names `displacement_read_contract`
by field name) with C-30 (mandatory evidence_summary instruction naming all three artifact
types) creates the contract-to-synthesis traceability pipeline: ROLE A commits the contract,
Stage 5 entry verifies it by name, evidence_summary instruction enforces consumption.
C-32 does not fire (EXIT SIGNAL remains count-assertion form).

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
Do not re-establish the incumbent per stage. Carry forward from CAMPAIGN OPEN.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS TABLE

SESSION INVARIANT D leads. All invariants carry: "cannot be modified or bypassed at
any subsequent stage." Register all four before roles execute.
Canonical failure labels registered here; echoed verbatim at inline enforcement checkpoints.

  ID   | NAME                      | DECLARATION                                               | FAILURE LABEL
  -----|---------------------------|-----------------------------------------------------------|------------------
  D    | INCUMBENT CHECK PHRASING  | Stage 2: "Does [evidence item] support the displacement   | FORMAT ERROR
       | REGISTER                  |   of [incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]      |
       |                           |   by {topic} on [dimension]?                              |
       |                           |   [Yes / No / Inconclusive]"                              |
       |                           | Stage 3: "Does [practitioner account] reveal a viable     |
       |                           |   transition path from [incumbent from CAMPAIGN OPEN      |
       |                           |   INCUMBENT ANCHOR] to {topic} for [use case]?            |
       |                           |   [Yes / No / Inconclusive]"                              |
       |                           | Stage 4: "Does [prototype result] make a credible case    |
       |                           |   for displacing [incumbent from CAMPAIGN OPEN INCUMBENT  |
       |                           |   ANCHOR] with {topic}? [Yes / No / Pending]"             |
       |                           | Binding: [incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]  |
       |                           |   resolves to incumbent_name. Literal string = FORMAT ERROR.|
       |                           | Enforcement: Template deviation = FORMAT ERROR.           |
       |                           | Cannot be modified or bypassed at any stage.              |
  -----|---------------------------|-----------------------------------------------------------|------------------
  A    | ADVERSARIAL REVIEWER TYPE | adversarial_reviewer_type: [challenge role].              | DUAL-LOCK ERROR
       |                           | Activation: null_tally_final >= 3.                        |
  -----|---------------------------|-----------------------------------------------------------|------------------
  B    | CONFIDENCE CAP            | confidence_composite -= 2 if null_tally_final >= 3.       | DUAL-LOCK ERROR
  -----|---------------------------|-----------------------------------------------------------|------------------
  C    | DERIVATION ANNOTATION     | Every handoff field: [derived from: X]. Unlabeled = FAIL. | FAIL

### ROLE OWNERSHIP TABLE

Roles run C -> B -> A. DEPENDENCY column enforced.

  ROLE   | TITLE                    | OWNED FIELD                  | GATE S STEP | EXECUTE | DEPENDENCY
  -------|--------------------------|------------------------------|-------------|---------|------------------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked       | Step 1      | FIRST   | INCUMBENT ANCHOR filled
  ROLE B | SCOUT LOADER             | gate_s_cleared                | Step 2      | SECOND  | ROLE C complete
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed  | Step 3      | THIRD   | ROLE B complete

ROLE C execution (fill now):
  incumbent_threat_locked: [true when name, strength, vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  incumbent_anchor_read:        [INCUMBENT ANCHOR read: resolved incumbent_name confirmed.
                                  Invariant D binding active. Source: CAMPAIGN OPEN
                                  INCUMBENT ANCHOR sub-section.]
  displacement_read_contract:   [Stages 2, 3, 4 will write Displacement read field to
                                  artifact bodies. Stage 5 entry will confirm all three
                                  by verifying this contract before synthesis proceeds.]
  invariant_registry_confirmed: [true when all four invariants registered]

---

## RESUME AUDIT

Glob existing artifacts before Stage 0.

  STAGE | ARTIFACT PATTERN                                | FOUND | DECISION
  ------|-------------------------------------------------|-------|---------------------
  1     | simulations/prove/{topic}-hypothesis-{date}.md | [Y/N] | [RESUME-SKIP / RUN]
  2     | simulations/prove/{topic}-websearch-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  3     | simulations/prove/{topic}-interview-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  4     | simulations/prove/{topic}-prototype-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  5     | simulations/prove/{topic}-synthesis-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]

  resume_audit_complete: [true]  stages_to_run: [list or ALL]

All RESUME-SKIP: STOP. Otherwise: proceed to Stage 0.

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] RESUME AUDIT complete  [ ] CAMPAIGN OPEN + INCUMBENT ANCHOR filled
  [ ] SESSION INVARIANTS TABLE complete
  [ ] ROLE C: incumbent_threat_locked = true
  [ ] ROLE B: scout loaded
  [ ] ROLE A: incumbent_anchor_read confirmed, displacement_read_contract committed,
      invariant_registry_confirmed = true

CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | RESULT
  -----|------------------------------|---------|---------------------
  1    | incumbent_threat_locked      | ROLE C  | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | [confirm or BLOCKED]

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3 confirmed. SESSION INVARIANT D active.
   ROLE A displacement_read_contract committed. Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] gate_open received  [ ] Stage 1 = RUN  [ ] scout_artifact available
  [ ] SESSION INVARIANT D templates registered

  source_scout_artifact: [path from ROLE B -- copied, not inferred]
  hypothesis:            [falsifiable claim about {topic}]
  counter_hypothesis:    [incumbent's best defense]
  confidence_prior:      [1-10 numeric]

Write: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked
  "STAGE 1 EXIT: hypothesis_locked -- {topic}-hypothesis-{date}.md written. Stage 2 ready."

---

## STAGE 2 -- WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] hypothesis_locked received  [ ] Stage 2 = RUN  [ ] Invariant D Stage 2 template active

Gather minimum 5 sources.

INCUMBENT CHECK TABLE -- Stage 2 (SESSION INVARIANT D verbatim; DISP DELTA column):

  ITEM | SOURCE   | SUMMARY   | TEMPLATE & VERDICT                                                              | DISP DELTA
  -----|----------|-----------|---------------------------------------------------------------------------------|------------
  1    | [src]    | [sum]     | "Does [item] support displacement of [incumbent from CAMPAIGN OPEN INCUMBENT    | [delta]
  2    | [src]    | [sum]     |  ANCHOR] by {topic} on [dim]? [Yes / No / Inconclusive]" (verbatim each row)   | [delta]
  3    | [src]    | [sum]     |                                                                                 | [delta]
  4    | [src]    | [sum]     |                                                                                 | [delta]
  5    | [src]    | [sum]     |                                                                                 | [delta]

  s2_count: [N>=5]  s2_displacement_delta_sum: [sum]  s2_ce_verdict: [null/value]
  s2_confidence_delta: [+/-]  running_confidence: [prior+delta]
  Displacement read: [one sentence]

Write: {topic}-websearch-{date}.md (includes Displacement read). Confirm write.
Gate: s2_count >= 5.

STAGE 2 EXIT SIGNAL: websearch_complete(count=[N], confidence=[running_confidence], momentum=[s2_displacement_delta_sum])
  "STAGE 2 EXIT: websearch_complete -- s2_count=[N]. running_confidence=[value]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] websearch_complete received  [ ] Stage 3 = RUN  [ ] s2_ce_verdict recorded
  [ ] Read websearch artifact. Extract running_confidence. Validate vs payload.
      Mismatch = CHAIN INTEGRITY FAILURE.
  [ ] Invariant D Stage 3 template active

Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D verbatim):

  PRACTITIONER | ACCOUNT    | TEMPLATE & VERDICT                                                            | DISP DELTA
  -------------|------------|-------------------------------------------------------------------------------|------------
  [type 1]     | [account]  | "Does [account] reveal a viable transition path from [incumbent from CAMPAIGN | [delta]
  [type 2]     | [account]  |  OPEN INCUMBENT ANCHOR] to {topic} for [use case]? [Yes / No / Inconclusive]" | [delta]
  [type 3]     | [account]  |                                                                               | [delta]

  s3_count: [N>=3]  s3_displacement_delta_sum: [sum]  s3_ce_verdict: [null/value]
  s3_confidence_delta: [+/-]  running_confidence: [prior+delta]
  displacement_momentum: [s2+s3]  Displacement read: [one sentence]

Write: {topic}-interview-{date}.md (includes Displacement read). Confirm write.
Gate: s3_count >= 3.

STAGE 3 EXIT SIGNAL: interview_complete(count=[N], confidence=[running_confidence], momentum=[displacement_momentum])
  "STAGE 3 EXIT: interview_complete -- s3_count=[N]. running_confidence=[value].
   displacement_momentum=[value]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] interview_complete received  [ ] Stage 4 = RUN  [ ] s3_ce_verdict recorded
  [ ] Read interview artifact. Extract running_confidence AND displacement_momentum.
      Validate both. Mismatch = CHAIN INTEGRITY FAILURE.
  [ ] Invariant D Stage 4 template active

  prototype_design: [description]  prototype_result: [what was learned]

INCUMBENT CHECK TABLE -- Stage 4:

  ITEM      | RESULT  | TEMPLATE & VERDICT                                                           | DISP DELTA
  ----------|---------|------------------------------------------------------------------------------|------------
  prototype | [res]   | "Does [result] make a credible case for displacing [incumbent from CAMPAIGN  | [delta]
            |         |  OPEN INCUMBENT ANCHOR] with {topic}? [Yes / No / Pending]"                 |

  s4_count: [N>=3]  s4_displacement_delta_sum: [delta]  s4_displacement_verdict: [Yes/No/Pending]
  s4_ce_verdict: [null/value]  s4_confidence_delta: [+/-]
  running_confidence: [prior+delta]  displacement_momentum_final: [prior+delta]
  Displacement read: [one sentence]

Write: {topic}-prototype-{date}.md (includes Displacement read). Confirm write.
Gate: s4_count >= 3.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[N], confidence=[running_confidence], momentum_final=[displacement_momentum_final])
  "STAGE 4 EXIT: prototype_complete -- s4_count=[N]. running_confidence=[value].
   displacement_momentum_final=[value]. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] prototype_complete received
  [ ] Stage 5 = RUN
  [ ] Read prototype artifact. Extract running_confidence AND displacement_momentum_final.
      Validate both. Mismatch = CHAIN INTEGRITY FAILURE.
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 present
  [ ] All four SESSION INVARIANT TABLE rows active
  [ ] All three artifact Displacement read fields confirmed written
      [per ROLE A displacement_read_contract -- websearch, interview, prototype].
      Missing Displacement read in any artifact = CHAIN INTEGRITY FAILURE. Halt.

### BLOCK 1 -- CONFIDENCE CHAIN RESOLUTION

  prior + s2_delta + s3_delta + s4_delta = confidence_composite: [value]

### BLOCK 2 -- COUNTER-HYPOTHESIS RESOLUTION

  COUNTER_HYPOTHESIS | VERDICT                                  | EVIDENCE
  -------------------|------------------------------------------|--------------------
  [from Stage 1]     | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite artifact]

OPEN RISK: reduce confidence_composite one tier.

### BLOCK 3 -- DISPLACEMENT INTEGRITY CHECK

  S2->[s2_ce_verdict]  S3->[s3_ce_verdict]  S4->[s4_ce_verdict]  null_tally_final=[N]
  Cross-check: [Match / Mismatch]  >= 3: dual_lock_fired | else: not_triggered

THREE-STAGE DISPLACEMENT CHAIN (STANCE required; Y/N = FORMAT ERROR):

  STAGE | DISP DELTA | CUMUL MOMENTUM | STANCE                                            | FLAG
  ------|------------|----------------|---------------------------------------------------|-----
  S2    | [sum]      | [cumul]        | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]
  S3    | [sum]      | [cumul]        | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]
  S4    | [sum]      | [cumul]        | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]

  chain_pattern: [ACCELERATING / STEADY_BUILD / PLATEAU / LATE_REVERSAL / ...]
  displacement_conclusion: [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  incumbent_defense_closed: [true when flagged rows reconciled]

### SYNTHESIS DECLARATIONS

Do not embed in prose. Each field on its own line, extractable by label match.

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences. Must cite all three artifact Displacement reads
                           (mandatory -- not conditional):
                           websearch Displacement read:  [value from {topic}-websearch-{date}.md]
                           interview Displacement read:  [value from {topic}-interview-{date}.md]
                           prototype Displacement read:  [value from {topic}-prototype-{date}.md]
                           Omission of any artifact Displacement read = FAIL.]
  confidence_composite:  [final value after all adjustments]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### HANDOFF TABLE

All 11 fields required. Every field: [derived from: X]. Unlabeled = FAIL.

  FIELD                    | VALUE   | DERIVED FROM
  -------------------------|---------|----------------------------------
  scout_anchor             | [value] | [derived from: ROLE B]
  incumbent_threat_locked  | [value] | [derived from: ROLE C]
  hypothesis               | [value] | [derived from: Stage 1]
  counter_hypothesis       | [value] | [derived from: Stage 1]
  s2_ce_verdict            | [value] | [derived from: Stage 2]
  s3_ce_verdict            | [value] | [derived from: Stage 3]
  s4_ce_verdict            | [value] | [derived from: Stage 4]
  null_tally_final         | [value] | [derived from: Stage 4 + Stage 5]
  co_activation_confirmed  | [value] | [derived from: Stage 5 Block 3]
  incumbent_defense_closed | [value] | [derived from: Stage 5 Block 3]
  confidence_composite     | [value] | [derived from: Stage 5 Block 1]
  schema_compliance_confirmed | [true] | [Invariant E checkpoint -- FAIL if any field unlabeled]

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story.
   All three artifact Displacement reads confirmed in evidence_summary."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-05 -- Axes: C-30 + C-31 + C-32 Full Stack

**Variation hypothesis**: All three R8 targets combined -- mandatory evidence_summary
instruction (C-30), Stage 5 entry gate cross-referencing `displacement_read_contract`
by field name (C-31), Stage 5 EXIT SIGNAL naming each artifact type individually (C-32) --
on the full structural stack achieves all three simultaneously. This is the R8 convergence
candidate: ROLE A commits the contract, Stage 5 entry verifies it by contract field name,
evidence_summary instruction mandates all three reads by name, EXIT SIGNAL names each
artifact type in the chain-closure audit record.

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
Do not re-establish the incumbent per stage. Carry forward from CAMPAIGN OPEN.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS TABLE

SESSION INVARIANT D leads. All invariants carry: "cannot be modified or bypassed at
any subsequent stage." Register all four before roles execute.
Canonical failure labels registered here; echoed verbatim at inline enforcement checkpoints.

  ID   | NAME                      | DECLARATION                                               | FAILURE LABEL
  -----|---------------------------|-----------------------------------------------------------|------------------
  D    | INCUMBENT CHECK PHRASING  | Stage 2: "Does [evidence item] support the displacement   | FORMAT ERROR
       | REGISTER                  |   of [incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]      |
       |                           |   by {topic} on [dimension]?                              |
       |                           |   [Yes / No / Inconclusive]"                              |
       |                           | Stage 3: "Does [practitioner account] reveal a viable     |
       |                           |   transition path from [incumbent from CAMPAIGN OPEN      |
       |                           |   INCUMBENT ANCHOR] to {topic} for [use case]?            |
       |                           |   [Yes / No / Inconclusive]"                              |
       |                           | Stage 4: "Does [prototype result] make a credible case    |
       |                           |   for displacing [incumbent from CAMPAIGN OPEN INCUMBENT  |
       |                           |   ANCHOR] with {topic}? [Yes / No / Pending]"             |
       |                           | Binding: [incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]  |
       |                           |   resolves to incumbent_name. Literal string = FORMAT ERROR.|
       |                           | Enforcement: Template deviation = FORMAT ERROR.           |
       |                           | Cannot be modified or bypassed at any stage.              |
  -----|---------------------------|-----------------------------------------------------------|------------------
  A    | ADVERSARIAL REVIEWER      | adversarial_reviewer_type: [challenge role].              | DUAL-LOCK ERROR
       | TYPE                      | Activation: null_tally_final >= 3.                        |
       |                           | Cannot be modified or bypassed at synthesis.              |
  -----|---------------------------|-----------------------------------------------------------|------------------
  B    | CONFIDENCE CAP            | confidence_composite -= 2 if null_tally_final >= 3.       | DUAL-LOCK ERROR
       |                           | Cannot be softened or overridden.                         |
  -----|---------------------------|-----------------------------------------------------------|------------------
  C    | DERIVATION ANNOTATION     | Every handoff field: [derived from: X]. Unlabeled = FAIL. | FAIL
       |                           | Cannot be modified or bypassed at synthesis.              |

### ROLE OWNERSHIP TABLE

ROLE C executes first. Roles run C -> B -> A before Stage 0 begins.
DEPENDENCY column: no role may execute until its listed dependency is satisfied.

  ROLE   | TITLE                    | OWNED FIELD                  | GATE S STEP | EXECUTE | DEPENDENCY
  -------|--------------------------|------------------------------|-------------|---------|------------------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked       | Step 1      | FIRST   | INCUMBENT ANCHOR filled
  ROLE B | SCOUT LOADER             | gate_s_cleared                | Step 2      | SECOND  | ROLE C complete
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed  | Step 3      | THIRD   | ROLE B complete

ROLE C execution (fill now):
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  incumbent_anchor_read:        [INCUMBENT ANCHOR read: resolved incumbent_name confirmed.
                                  Invariant D binding active. Source: CAMPAIGN OPEN
                                  INCUMBENT ANCHOR sub-section.]
  displacement_read_contract:   [Stages 2, 3, 4 will write Displacement read field to
                                  artifact bodies. Stage 5 entry will confirm all three
                                  by verifying this contract before synthesis proceeds.]
  invariant_registry_confirmed: [true when all four invariants registered]

---

## RESUME AUDIT

Glob existing artifacts for {topic} on {date} before Stage 0.

  STAGE | ARTIFACT PATTERN                                       | FOUND | DECISION
  ------|--------------------------------------------------------|-------|---------------------
  1     | simulations/prove/{topic}-hypothesis-{date}.md        | [Y/N] | [RESUME-SKIP / RUN]
  2     | simulations/prove/{topic}-websearch-{date}.md         | [Y/N] | [RESUME-SKIP / RUN]
  3     | simulations/prove/{topic}-interview-{date}.md         | [Y/N] | [RESUME-SKIP / RUN]
  4     | simulations/prove/{topic}-prototype-{date}.md         | [Y/N] | [RESUME-SKIP / RUN]
  5     | simulations/prove/{topic}-synthesis-{date}.md         | [Y/N] | [RESUME-SKIP / RUN]

  resume_audit_complete: [true]  stages_to_run: [list or ALL]

All RESUME-SKIP: "RESUME_AUDIT_EXIT -- Campaign complete." STOP.
Otherwise: "RESUME_AUDIT_PASS -- Stages: [list]. Proceeding to Stage 0."

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] RESUME AUDIT completed -- resume_audit_complete = true
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] SESSION INVARIANTS TABLE complete -- all four rows filled
  [ ] ROLE C executed -- incumbent_threat_locked = true
  [ ] ROLE B executed -- scout_artifact identified and scout_loaded confirmed
  [ ] ROLE A executed -- incumbent_anchor_read confirmed, displacement_read_contract
      committed, invariant_registry_confirmed = true

CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|---------------------------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]

  First BLOCKED step halts campaign. Record step and owning role.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3 all confirmed. SESSION INVARIANT D active.
   ROLE A displacement_read_contract committed. Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] RESUME AUDIT: Stage 1 = RUN
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered

  source_scout_artifact: [path from ROLE B -- copied, not inferred]
  hypothesis:            [falsifiable claim about {topic}]
  counter_hypothesis:    [incumbent's best defense -- grounded in ROLE C analysis]
  confidence_prior:      [1-10 numeric -- initial estimate before evidence]

Write: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked
  "STAGE 1 EXIT: hypothesis_locked -- {topic}-hypothesis-{date}.md written. Stage 2 ready."

---

## STAGE 2 -- WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked
  [ ] RESUME AUDIT: Stage 2 = RUN
  [ ] hypothesis artifact confirmed written
  [ ] SESSION INVARIANT D Stage 2 template active (verbatim from table row D)

Gather minimum 5 external sources.

INCUMBENT CHECK TABLE -- Stage 2 (SESSION INVARIANT D verbatim; DISPLACEMENT DELTA column):

  ITEM | SOURCE   | SUMMARY   | TEMPLATE APPLIED & VERDICT                                              | DISP DELTA (-2 to +2)
  -----|----------|-----------|-------------------------------------------------------------------------|----------------------
  1    | [source] | [summary] | "Does [item] support displacement of [incumbent from CAMPAIGN OPEN      | [delta]
  2    | [source] | [summary] |  INCUMBENT ANCHOR] by {topic} on [dim]? [Yes / No / Inconclusive]"     | [delta]
  3    | [source] | [summary] | (fill each row verbatim; FORMAT ERROR if template deviates)            | [delta]
  4    | [source] | [summary] |                                                                         | [delta]
  5    | [source] | [summary] |                                                                         | [delta]

  s2_count:                   [N] -- must be >= 5
  s2_displacement_delta_sum:  [sum of DISP DELTA column]
  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]
  s2_confidence_delta:        [+/- numeric]
  running_confidence:         [confidence_prior + s2_confidence_delta]
  Displacement read:          [one sentence: does Stage 2 evidence support displacement?]

Write: {topic}-websearch-{date}.md. Artifact body includes Displacement read field. Confirm write.
Gate: Do not fire exit signal until s2_count >= 5.

STAGE 2 EXIT SIGNAL: websearch_complete(count=[N], confidence=[running_confidence], momentum=[s2_displacement_delta_sum])
  "STAGE 2 EXIT: websearch_complete -- s2_count = [N] (gate: >= 5 met).
   s2_ce_verdict = [value]. running_confidence = [value]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete(count=N, confidence=C, momentum=M)
  [ ] RESUME AUDIT: Stage 3 = RUN
  [ ] s2_ce_verdict recorded
  [ ] Read {topic}-websearch-{date}.md from disk. Extract running_confidence.
      Validate against signal payload. Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 3 template active

Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D verbatim; DISPLACEMENT DELTA column):

  PRACTITIONER | KEY ACCOUNT       | TEMPLATE APPLIED & VERDICT                                                      | DISP DELTA
  -------------|-------------------|---------------------------------------------------------------------------------|------------
  [type 1]     | [quote/paraphrase]| "Does [account] reveal a viable transition path from [incumbent from CAMPAIGN   | [delta]
  [type 2]     | [quote/paraphrase]|  OPEN INCUMBENT ANCHOR] to {topic} for [use case]? [Yes / No / Inconclusive]"  | [delta]
  [type 3]     | [quote/paraphrase]| (fill each row verbatim; FORMAT ERROR if template deviates)                    | [delta]

  s3_count:                    [N] -- must be >= 3
  s3_displacement_delta_sum:   [sum of DISP DELTA column]
  s3_incumbent_check_summary:  [N support / M counter / P inconclusive]
  s3_ce_verdict:               [null if no CE; cite account if found]
  s3_confidence_delta:         [+/- numeric]
  running_confidence:          [prior + s3_confidence_delta]
  displacement_momentum:       [s2_displacement_delta_sum + s3_displacement_delta_sum]
  Displacement read:           [one sentence: does practitioner evidence support transition?]

Write: {topic}-interview-{date}.md. Artifact body includes Displacement read field. Confirm write.
Gate: Do not fire exit signal until s3_count >= 3.

STAGE 3 EXIT SIGNAL: interview_complete(count=[N], confidence=[running_confidence], momentum=[displacement_momentum])
  "STAGE 3 EXIT: interview_complete -- s3_count = [N] (gate: >= 3 met).
   s3_ce_verdict = [value]. running_confidence = [value]. displacement_momentum = [value].
   Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete(count=N, confidence=C, momentum=M)
  [ ] RESUME AUDIT: Stage 4 = RUN
  [ ] s3_ce_verdict recorded
  [ ] Read {topic}-interview-{date}.md from disk. Extract running_confidence AND
      displacement_momentum. Validate both against signal payload.
      Mismatch on either = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 4 template active

  prototype_design:   [brief description]
  prototype_result:   [what was learned -- 1-3 sentences]

INCUMBENT CHECK TABLE -- Stage 4 (SESSION INVARIANT D verbatim; DISPLACEMENT DELTA column):

  ITEM      | RESULT             | TEMPLATE APPLIED & VERDICT                                                          | DISP DELTA
  ----------|--------------------|-------------------------------------------------------------------------------------|-----------
  prototype | [prototype_result] | "Does [result] make a credible case for displacing [incumbent from CAMPAIGN OPEN    | [delta]
            |                    |  INCUMBENT ANCHOR] with {topic}? [Yes / No / Pending]"                             |

  s4_count:                    [N] -- must be >= 3
  s4_displacement_delta_sum:   [delta for Stage 4]
  s4_displacement_verdict:     [Yes / No / Pending] -- required; omission = format error
  s4_ce_verdict:               [null / description]
  s4_confidence_delta:         [+/- numeric]
  running_confidence:          [prior + s4_confidence_delta]
  displacement_momentum_final: [displacement_momentum + s4_displacement_delta_sum]
  Displacement read:           [one sentence: does prototype make credible displacement case?]

Write: {topic}-prototype-{date}.md. Artifact body includes Displacement read field. Confirm write.
Gate: Do not fire exit signal until s4_count >= 3.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[N], confidence=[running_confidence], momentum_final=[displacement_momentum_final])
  "STAGE 4 EXIT: prototype_complete -- s4_count = [N] (gate: >= 3 met).
   running_confidence = [value]. displacement_momentum_final = [value].
   s4_ce_verdict = [value]. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete(count=N, confidence=C, momentum_final=M)
  [ ] RESUME AUDIT: Stage 5 = RUN
  [ ] Read {topic}-prototype-{date}.md from disk. Extract running_confidence AND
      displacement_momentum_final. Validate both against signal payload.
      Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 present for resolution
  [ ] All four SESSION INVARIANT TABLE rows active
  [ ] All three artifact Displacement read fields confirmed written
      [per ROLE A displacement_read_contract -- websearch, interview, prototype].
      Stage 5 will consume all three. Missing Displacement read in any artifact =
      CHAIN INTEGRITY FAILURE. Halt.

### BLOCK 1 -- CONFIDENCE CHAIN RESOLUTION

  prior:                [confidence_prior from Stage 1]
  s2_delta:             [s2_confidence_delta]
  s3_delta:             [s3_confidence_delta]
  s4_delta:             [s4_confidence_delta]
  chain_equation:       prior + s2_delta + s3_delta + s4_delta = [final]
  confidence_composite: [final -- before counter-hypothesis and cap adjustments]

### BLOCK 2 -- COUNTER-HYPOTHESIS RESOLUTION

  COUNTER_HYPOTHESIS   | VERDICT                                  | EVIDENCE
  ---------------------|------------------------------------------|------------------
  [from Stage 1]       | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite artifact]

OPEN RISK: reduce confidence_composite one tier before BLOCK 3.

### BLOCK 3 -- DISPLACEMENT INTEGRITY CHECK

NULL TALLY CHAIN:
  S2 -> [s2_ce_verdict]  S3 -> [s3_ce_verdict]  S4 -> [s4_ce_verdict]
  null_tally_final = [N]
  Cross-check vs Stage 4 exit count: [Match / Mismatch]

If null_tally_final >= 3:
  Lock 1 (SESSION INVARIANT A): adversarial review by [adversarial_reviewer_type]. BLOCKED.
  Lock 2 (SESSION INVARIANT B): confidence_composite -= 2 (hard cap, cannot be softened).
  co_activation_confirmed: dual_lock_fired
Else:
  co_activation_confirmed: not_triggered

THREE-STAGE DISPLACEMENT CHAIN (STANCE required per row; Y/N = FORMAT ERROR):

  STAGE | DISP DELTA SUM | CUMULATIVE MOMENTUM | STANCE                                            | FLAG?
  ------|----------------|---------------------|---------------------------------------------------|------
  S2    | [s2_disp_sum]  | [s2_cumul]          | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]
  S3    | [s3_disp_sum]  | [s3_cumul]          | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]
  S4    | [s4_disp_sum]  | [s4_cumul]          | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]

  chain_pattern:            [ACCELERATING / STEADY_BUILD / PLATEAU / LATE_REVERSAL / ...]
  FLAG rule: adjacent-stage STANCE divergence = FLAG = Y; requires conclusion_justification.
  displacement_conclusion:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  conclusion_justification:   [required if any FLAG = Y]
  incumbent_defense_closed:   [true when all flagged rows reconciled]

### SYNTHESIS DECLARATIONS

Do not embed these values in prose sentences. Each on its own line, extractable by label match.

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences. Must cite all three artifact Displacement reads
                           (mandatory -- not conditional):
                           websearch Displacement read:  [value from {topic}-websearch-{date}.md]
                           interview Displacement read:  [value from {topic}-interview-{date}.md]
                           prototype Displacement read:  [value from {topic}-prototype-{date}.md]
                           Omission of any artifact Displacement read = FAIL.]
  confidence_composite:  [final value after all adjustments]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### HANDOFF TABLE

All 11 fields required. Every field: [derived from: X] annotation. Unlabeled = FAIL.
schema_compliance_confirmed echoes registered failure label from SESSION INVARIANTS.

  FIELD                    | VALUE   | DERIVED FROM
  -------------------------|---------|----------------------------------
  scout_anchor             | [value] | [derived from: ROLE B]
  incumbent_threat_locked  | [value] | [derived from: ROLE C]
  hypothesis               | [value] | [derived from: Stage 1]
  counter_hypothesis       | [value] | [derived from: Stage 1]
  s2_ce_verdict            | [value] | [derived from: Stage 2]
  s3_ce_verdict            | [value] | [derived from: Stage 3]
  s4_ce_verdict            | [value] | [derived from: Stage 4]
  null_tally_final         | [value] | [derived from: Stage 4 + Stage 5]
  co_activation_confirmed  | [value] | [derived from: Stage 5 Block 3]
  incumbent_defense_closed | [value] | [derived from: Stage 5 Block 3]
  confidence_composite     | [value] | [derived from: Stage 5 Block 1]
  schema_compliance_confirmed | [true] | [Invariant E checkpoint -- FAIL if any field unlabeled]

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story.
   Displacement read chain closed: websearch Displacement read, interview Displacement read,
   prototype Displacement read -- all three cited in evidence_summary. Chain closed."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## R8 Variation Matrix

| Variation | C-27 | C-28 | C-29 | C-30 | C-31 | C-32 | Axis |
|-----------|------|------|------|------|------|------|------|
| V-01 | PASS | PASS | PASS | FAIL | **PASS** | FAIL | C-31 isolation (entry gate names contract) |
| V-02 | PASS | PASS | PASS | **PASS** | FAIL | FAIL | C-30 isolation (mandatory citation instruction) |
| V-03 | PASS | PASS | PASS | FAIL | FAIL | **PASS** | C-32 isolation (EXIT SIGNAL named provenance) |
| V-04 | PASS | PASS | PASS | **PASS** | **PASS** | FAIL | C-31+C-30 combined |
| V-05 | PASS | PASS | PASS | **PASS** | **PASS** | **PASS** | Full stack convergence candidate |

**C-30 key distinction**:
- V-01/V-03 evidence_summary: advisory or Stage-4-verdict-only -- FAIL
- V-02/V-04/V-05: `Must cite all three... Mandatory -- not conditional. Omission = FAIL.` -- PASS

**C-31 key distinction**:
- V-02/V-03 Stage 5 entry: `All three artifact Displacement read fields confirmed written
  (websearch, interview, prototype)` -- no contract field name reference -- FAIL
- V-01/V-04/V-05: `[per ROLE A displacement_read_contract -- ...]` -- PASS

**C-32 key distinction**:
- V-01/V-02/V-04 EXIT SIGNAL: `All three artifact Displacement reads confirmed` -- count
  assertion -- FAIL
- V-03/V-05: `websearch Displacement read, interview Displacement read, prototype
  Displacement read -- chain closed` -- individually named -- PASS

**R9 open target**: C-10 (displacement loop role anchor at Stage 3 -- no variation yet
names a ROLE 2 displacement anchor established at Stage 3 to close the three-point loop).
