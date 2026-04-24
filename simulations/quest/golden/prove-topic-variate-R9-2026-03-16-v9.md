---
skill: quest-variate
skill_target: prove-topic
round: R9
date: 2026-03-16
rubric: prove-topic-rubric-v9-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [campaign_closure_canonical_form, synthesis_invariant_e, stage0_precommit]
  combined: [V-04 (V-01+V-02), V-05 (V-01+V-02+V-03+dual_lock_precision)]
r8_baseline: >
  V-05 R8 = 98/100 under v8. Under v9 rubric V-05 R8 converts to 99/100:
  C-18 reduced 2->1 (-1), C-33 new (+1, Chain closed. present in R8 V-05),
  C-34 new (+1, Omission = FAIL present in R8 V-05). R9 goal: identify the 100th point
  and generate structural patterns that extend C-14 architecture to C-33 and C-34.
r9_targets: >
  C-33 (terminal closure assertion in Stage 5 EXIT SIGNAL -- all five R9 variations
  must pass by design). C-34 (evidence_summary instruction registers omission failure
  label -- all five R9 variations must pass by design).
  R9 exploration: what structural extension yields the first new excellence signal?
  Three axes: pre-registered closure canonical form (two-layer enforcement for C-33),
  Invariant E synthesis mandate (two-layer enforcement for C-34), Stage 0 forward
  pre-commitment of closure form + synthesis mandate.
r9_note: >
  The existing prove-topic-variate-R9-2026-03-16.md was written against rubric v14,
  a different architectural generation of the skill. This file targets rubric v9
  (displacement evidence campaign architecture: SESSION INVARIANTS, ROLE C/B/A,
  INCUMBENT ANCHOR, null tally, HANDOFF TABLE, SYNTHESIS DECLARATIONS).
---

# prove-topic -- Variation Round R9 (rubric v9)

Five complete, runnable skill body prompts. Each is self-contained -- no diff, no cross-references.

Round 9 targets C-33 and C-34 -- the two new aspirational criteria in rubric v9 derived from
R8 V-05 excellence signals. Both were present in R8 V-05 but not in R8 V-01 through V-04.

- **C-33** (1 pt): Stage 5 EXIT SIGNAL appends "Chain closed." as a distinct terminal assertion
  after the named-artifact enumeration. Requires C-32 to pass.

- **C-34** (1 pt): The Stage 5 evidence_summary mandatory instruction includes a canonical
  failure label for omission ("Omission = FAIL" or equivalent). Requires C-30 to pass.

All five R9 variations include the R8 V-05 full stack (C-30+C-31+C-32+C-33+C-34) and vary
one structural axis per single-axis variation. The goal is to discover structural improvements
that could yield new excellence signals (potential C-35+) while confirming C-33 and C-34 as
universal across all variations.

Axes explored:
- **V-01**: Pre-register the terminal closure form as a CAMPAIGN CLOSURE CANONICAL FORM block
  (C-14-style two-layer enforcement for C-33: registered source + Stage 5 echo).
- **V-02**: Elevate evidence_summary mandate to SESSION INVARIANTS Invariant E (two-layer
  enforcement for C-34: registered invariant + inline echo at SYNTHESIS DECLARATIONS).
- **V-03**: Stage 0 EXIT SIGNAL pre-commits closure form and synthesis mandate as forward
  declarations, creating a Stage 0 -> Stage 5 closure chain.

---

## V-01 -- Axis: CAMPAIGN CLOSURE CANONICAL FORM Pre-Registered in SESSION INVARIANTS

**Variation hypothesis**: Pre-registering the Stage 5 EXIT SIGNAL terminal closure form in a
CAMPAIGN CLOSURE CANONICAL FORM block (before roles execute) creates two-layer enforcement for
C-33: registered canonical form at session open -> Stage 5 EXIT SIGNAL echoes it verbatim.
Extends C-14's bidirectional label architecture to the terminal closure assertion. Axes V-02
and V-03 do not fire: Invariant E absent, Stage 0 EXIT SIGNAL standard.

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
  A    | ADVERSARIAL REVIEWER TYPE | adversarial_reviewer_type: [role most likely to challenge | DUAL-LOCK ERROR
       |                           |   the displacement claim]. Activation: null_tally_final   |
       |                           |   >= 3. Cannot be modified or bypassed at synthesis.      |
  -----|---------------------------|-----------------------------------------------------------|------------------
  B    | CONFIDENCE CAP            | null_ce_cap_rule: confidence_composite -= 2 if            | DUAL-LOCK ERROR
       |                           |   null_tally_final >= 3 (hard cap). Cannot be softened.   |
  -----|---------------------------|-----------------------------------------------------------|------------------
  C    | DERIVATION ANNOTATION     | annotation_rule: Every handoff field carries              | FAIL
       |                           |   [derived from: X]. Unlabeled = FAIL.                    |
       |                           | Cannot be modified or bypassed at synthesis.              |

### CAMPAIGN CLOSURE CANONICAL FORM

Register before roles execute. Stage 5 EXIT SIGNAL must echo this form verbatim.
Deviation from registered form = CLOSURE FORMAT ERROR.

  SIGNAL             | CANONICAL TERMINAL FORM
  -------------------|----------------------------------------------------------------------
  synthesis_complete | "Displacement read chain closed: websearch Displacement read,
                     |  interview Displacement read, prototype Displacement read --
                     |  all three cited in evidence_summary. Chain closed."

### ROLE OWNERSHIP TABLE

ROLE C executes first. Roles run C -> B -> A before Stage 0 begins.

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
  [ ] RESUME AUDIT completed -- resume_audit_complete = true
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] SESSION INVARIANTS TABLE complete -- all four rows filled
  [ ] CAMPAIGN CLOSURE CANONICAL FORM registered -- synthesis_complete terminal form on record
  [ ] ROLE C executed -- incumbent_threat_locked = true
  [ ] ROLE B executed -- scout_artifact identified, scout_loaded confirmed
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
   ROLE A displacement_read_contract committed. CAMPAIGN CLOSURE CANONICAL FORM registered.
   Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] gate_open received  [ ] Stage 1 = RUN
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered

  source_scout_artifact: [path from ROLE B -- copied, not inferred]
  hypothesis:            [falsifiable claim about {topic}]
  counter_hypothesis:    [incumbent's best defense -- grounded in ROLE C analysis]
  confidence_prior:      [1-10 numeric]

Write: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked
  "STAGE 1 EXIT: hypothesis_locked -- {topic}-hypothesis-{date}.md written. Stage 2 ready."

---

## STAGE 2 -- WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] hypothesis_locked received  [ ] Stage 2 = RUN
  [ ] hypothesis artifact confirmed written
  [ ] SESSION INVARIANT D Stage 2 template active (verbatim from table row D)

Gather minimum 5 external sources.

INCUMBENT CHECK TABLE -- Stage 2 (SESSION INVARIANT D verbatim; DISP DELTA column):

  ITEM | SOURCE   | SUMMARY   | TEMPLATE APPLIED & VERDICT                                              | DISP DELTA
  -----|----------|-----------|-------------------------------------------------------------------------|------------
  1    | [source] | [summary] | "Does [item] support the displacement of [incumbent from CAMPAIGN OPEN  | [delta]
  2    | [source] | [summary] |  INCUMBENT ANCHOR] by {topic} on [dimension]?                          | [delta]
  3    | [source] | [summary] |  [Yes / No / Inconclusive]" (fill each row verbatim;                   | [delta]
  4    | [source] | [summary] |  FORMAT ERROR if template deviates)                                    | [delta]
  5    | [source] | [summary] |                                                                         | [delta]

  s2_count:                  [N -- must be >= 5]
  s2_displacement_delta_sum: [sum of DISP DELTA column]
  s2_ce_verdict:             [null if no CE; cite item if found]
  s2_confidence_delta:       [+/- numeric]
  running_confidence:        [confidence_prior + s2_confidence_delta]
  Displacement read:         [one sentence: does Stage 2 evidence support displacement?]

Write: {topic}-websearch-{date}.md. Artifact body includes Displacement read field. Confirm write.
Gate: Do not fire exit signal until s2_count >= 5.

STAGE 2 EXIT SIGNAL: websearch_complete(count=[N], confidence=[running_confidence], momentum=[s2_displacement_delta_sum])
  "STAGE 2 EXIT: websearch_complete -- s2_count = [N]. s2_ce_verdict = [value].
   running_confidence = [value]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] websearch_complete received  [ ] Stage 3 = RUN  [ ] s2_ce_verdict recorded
  [ ] Read {topic}-websearch-{date}.md. Extract running_confidence.
      Validate against payload. Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 3 template active

Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D verbatim; DISP DELTA column):

  PRACTITIONER | KEY ACCOUNT       | TEMPLATE APPLIED & VERDICT                                                      | DISP DELTA
  -------------|-------------------|---------------------------------------------------------------------------------|------------
  [type 1]     | [quote/paraphrase]| "Does [account] reveal a viable transition path from [incumbent from CAMPAIGN   | [delta]
  [type 2]     | [quote/paraphrase]|  OPEN INCUMBENT ANCHOR] to {topic} for [use case]?                             | [delta]
  [type 3]     | [quote/paraphrase]|  [Yes / No / Inconclusive]" (verbatim; FORMAT ERROR if deviates)                | [delta]

  s3_count:                  [N -- must be >= 3]
  s3_displacement_delta_sum: [sum of DISP DELTA column]
  s3_ce_verdict:             [null if no CE; cite account if found]
  s3_confidence_delta:       [+/- numeric]
  running_confidence:        [prior + s3_confidence_delta]
  displacement_momentum:     [s2_displacement_delta_sum + s3_displacement_delta_sum]
  Displacement read:         [one sentence: does practitioner evidence support transition?]

Write: {topic}-interview-{date}.md. Artifact body includes Displacement read field. Confirm write.
Gate: Do not fire exit signal until s3_count >= 3.

STAGE 3 EXIT SIGNAL: interview_complete(count=[N], confidence=[running_confidence], momentum=[displacement_momentum])
  "STAGE 3 EXIT: interview_complete -- s3_count = [N]. s3_ce_verdict = [value].
   running_confidence = [value]. displacement_momentum = [value]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] interview_complete received  [ ] Stage 4 = RUN  [ ] s3_ce_verdict recorded
  [ ] Read {topic}-interview-{date}.md. Extract running_confidence AND displacement_momentum.
      Validate both. Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 4 template active

  prototype_design: [brief description]
  prototype_result: [what was learned -- 1-3 sentences]

INCUMBENT CHECK TABLE -- Stage 4 (SESSION INVARIANT D verbatim; DISP DELTA column):

  ITEM      | RESULT             | TEMPLATE APPLIED & VERDICT                                                          | DISP DELTA
  ----------|--------------------|-------------------------------------------------------------------------------------|-----------
  prototype | [prototype_result] | "Does [result] make a credible case for displacing [incumbent from CAMPAIGN OPEN    | [delta]
            |                    |  INCUMBENT ANCHOR] with {topic}? [Yes / No / Pending]"                             |

  s4_count:                    [N -- must be >= 3]
  s4_displacement_delta_sum:   [delta for Stage 4]
  s4_displacement_verdict:     [Yes / No / Pending] -- required; omission = FORMAT ERROR
  s4_ce_verdict:               [null / description]
  s4_confidence_delta:         [+/- numeric]
  running_confidence:          [prior + s4_confidence_delta]
  displacement_momentum_final: [displacement_momentum + s4_displacement_delta_sum]
  Displacement read:           [one sentence: does prototype make credible displacement case?]

  null_tally_running:     [S2 null + S3 null + S4 null CE verdicts = N]
  null_tally_final:       [N -- freeze here at Stage 4 close]
  null_tally_cross_check: Running count from Stage 3 was [M]. Final is [N]. Match: [true/false].

Write: {topic}-prototype-{date}.md. Artifact body includes Displacement read field. Confirm write.
Gate: Do not fire exit signal until s4_count >= 3.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[N], confidence=[running_confidence], momentum_final=[displacement_momentum_final], null_tally=[null_tally_final])
  "STAGE 4 EXIT: prototype_complete -- s4_count = [N]. running_confidence = [value].
   displacement_momentum_final = [value]. s4_ce_verdict = [value].
   null_tally_final = [N]. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] prototype_complete received  [ ] Stage 5 = RUN
  [ ] Read {topic}-prototype-{date}.md. Extract running_confidence AND
      displacement_momentum_final. Validate both. Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] null_tally_final recorded (from Stage 4 close)
  [ ] counter_hypothesis from Stage 1 present
  [ ] All four SESSION INVARIANT TABLE rows active
  [ ] All three artifact Displacement read fields confirmed written
      [per ROLE A displacement_read_contract -- websearch, interview, prototype].
      Stage 5 will consume all three. Missing Displacement read = CHAIN INTEGRITY FAILURE. Halt.

### BLOCK 1 -- CONFIDENCE CHAIN RESOLUTION

  prior:                [confidence_prior from Stage 1]
  s2_delta / s3_delta / s4_delta: [each confidence delta]
  chain_equation:       prior + s2_delta + s3_delta + s4_delta = [final]
  confidence_composite: [final -- before counter-hypothesis and cap adjustments]

### BLOCK 2 -- COUNTER-HYPOTHESIS RESOLUTION

  COUNTER_HYPOTHESIS   | VERDICT                                  | EVIDENCE
  ---------------------|------------------------------------------|------------------
  [from Stage 1]       | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite artifact]

OPEN RISK: reduce confidence_composite one tier before BLOCK 3.

### BLOCK 3 -- DISPLACEMENT INTEGRITY CHECK

NULL TALLY CHAIN (Stage 5 reconstruction):
  S2: s2_ce_verdict = [value], null contribution = [0/1]
  S3: s3_ce_verdict = [value], null contribution = [0/1]
  S4: s4_ce_verdict = [value], null contribution = [0/1]
  null_tally_reconstructed = [sum]
  Cross-check vs Stage 4 null_tally_final: [Match / Mismatch]
  Mismatch = INTEGRITY FAILURE. Halt.

If null_tally_final >= 3:
  Lock 1 (SESSION INVARIANT A): adversarial review by [adversarial_reviewer_type]. BLOCKED.
  Lock 2 (SESSION INVARIANT B): confidence_composite -= 2 (hard cap, cannot be softened).
  co_activation_confirmed: dual_lock_fired
Else:
  co_activation_confirmed: not_triggered

THREE-STAGE DISPLACEMENT CHAIN (STANCE required per row; Y/N = FORMAT ERROR):

  STAGE | DISP DELTA SUM | CUMUL MOMENTUM | STANCE                                            | FLAG?
  ------|----------------|----------------|---------------------------------------------------|------
  S2    | [s2_disp_sum]  | [s2_cumul]     | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]
  S3    | [s3_disp_sum]  | [s3_cumul]     | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]
  S4    | [s4_disp_sum]  | [s4_cumul]     | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]

  chain_pattern:            [ACCELERATING / STEADY_BUILD / PLATEAU / LATE_REVERSAL / ...]
  displacement_conclusion:  [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  incumbent_defense_closed: [true when flagged rows reconciled]

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

  FIELD                       | VALUE   | DERIVED FROM
  ----------------------------|---------|----------------------------------
  scout_anchor                | [value] | [derived from: ROLE B]
  incumbent_threat_locked     | [value] | [derived from: ROLE C]
  hypothesis                  | [value] | [derived from: Stage 1]
  counter_hypothesis          | [value] | [derived from: Stage 1]
  s2_ce_verdict               | [value] | [derived from: Stage 2]
  s3_ce_verdict               | [value] | [derived from: Stage 3]
  s4_ce_verdict               | [value] | [derived from: Stage 4]
  null_tally_final            | [value] | [derived from: Stage 4 + Stage 5]
  co_activation_confirmed     | [value] | [derived from: Stage 5 Block 3]
  incumbent_defense_closed    | [value] | [derived from: Stage 5 Block 3]
  confidence_composite        | [value] | [derived from: Stage 5 Block 1]
  schema_compliance_confirmed | [true]  | [Invariant E checkpoint -- FAIL if any field unlabeled]

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story.
   Echoing registered CAMPAIGN CLOSURE CANONICAL FORM:
   Displacement read chain closed: websearch Displacement read, interview Displacement read,
   prototype Displacement read -- all three cited in evidence_summary. Chain closed."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-02 -- Axis: Synthesis Evidence Mandate as Invariant E in SESSION INVARIANTS TABLE

**Variation hypothesis**: Elevating the evidence_summary omission failure label from an inline
instruction to a pre-registered SESSION INVARIANTS Invariant E (SYNTHESIS EVIDENCE MANDATE,
failure label SYNTHESIS-FAIL) creates full two-layer enforcement for C-34: registered as
canonical source in SESSION INVARIANTS TABLE, echoed at SYNTHESIS DECLARATIONS inline. Extends
the C-14 bidirectional enforcement architecture into the Stage 5 synthesis instruction layer
as a named, registered invariant. Axes V-01 and V-03 do not fire.

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
any subsequent stage." Register all five before roles execute.
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
  A    | ADVERSARIAL REVIEWER TYPE | adversarial_reviewer_type: [challenge role].              | DUAL-LOCK ERROR
       |                           | Activation: null_tally_final >= 3.                        |
       |                           | Cannot be modified or bypassed at synthesis.              |
  -----|---------------------------|-----------------------------------------------------------|------------------
  B    | CONFIDENCE CAP            | null_ce_cap_rule: confidence_composite -= 2 if            | DUAL-LOCK ERROR
       |                           |   null_tally_final >= 3 (hard cap). Cannot be softened.   |
  -----|---------------------------|-----------------------------------------------------------|------------------
  C    | DERIVATION ANNOTATION     | annotation_rule: Every handoff field carries              | FAIL
       |                           |   [derived from: X]. Unlabeled = FAIL.                    |
       |                           | Cannot be modified or bypassed at synthesis.              |
  -----|---------------------------|-----------------------------------------------------------|------------------
  E    | SYNTHESIS EVIDENCE        | evidence_summary must cite all three artifact             | SYNTHESIS-FAIL
       | MANDATE                   |   Displacement reads: websearch Displacement read,        |
       |                           |   interview Displacement read, prototype Displacement     |
       |                           |   read. Omission of any artifact Displacement read =      |
       |                           |   SYNTHESIS-FAIL. Cannot be modified or bypassed.         |

### ROLE OWNERSHIP TABLE

ROLE C executes first. Roles run C -> B -> A before Stage 0 begins.

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
  invariant_registry_confirmed: [true when all five invariants registered (D, A, B, C, E)]

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
  [ ] SESSION INVARIANTS TABLE complete -- all five rows filled (D, A, B, C, E)
  [ ] ROLE C: incumbent_threat_locked = true
  [ ] ROLE B: scout loaded confirmed
  [ ] ROLE A: incumbent_anchor_read confirmed, displacement_read_contract committed,
      invariant_registry_confirmed = true (five invariants)

CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | RESULT
  -----|------------------------------|---------|---------------------
  1    | incumbent_threat_locked      | ROLE C  | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | [confirm or BLOCKED]

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3 confirmed. SESSION INVARIANT D active.
   SESSION INVARIANT E (SYNTHESIS EVIDENCE MANDATE, failure: SYNTHESIS-FAIL) registered.
   ROLE A displacement_read_contract committed. Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] gate_open received  [ ] Stage 1 = RUN
  [ ] scout_artifact available from ROLE B  [ ] SESSION INVARIANT D templates registered

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
  [ ] hypothesis_locked received  [ ] Stage 2 = RUN
  [ ] SESSION INVARIANT D Stage 2 template active (verbatim from table row D)

Gather minimum 5 external sources.

INCUMBENT CHECK TABLE -- Stage 2 (SESSION INVARIANT D verbatim; DISP DELTA column):

  ITEM | SOURCE   | SUMMARY   | TEMPLATE APPLIED & VERDICT                                              | DISP DELTA
  -----|----------|-----------|-------------------------------------------------------------------------|------------
  1    | [source] | [summary] | "Does [item] support the displacement of [incumbent from CAMPAIGN OPEN  | [delta]
  2    | [source] | [summary] |  INCUMBENT ANCHOR] by {topic} on [dimension]?                          | [delta]
  3    | [source] | [summary] |  [Yes / No / Inconclusive]" (verbatim; FORMAT ERROR if deviates)        | [delta]
  4    | [source] | [summary] |                                                                         | [delta]
  5    | [source] | [summary] |                                                                         | [delta]

  s2_count: [N>=5]  s2_displacement_delta_sum: [sum]  s2_ce_verdict: [null/value]
  s2_confidence_delta: [+/-]  running_confidence: [prior+delta]
  Displacement read: [one sentence]

Write: {topic}-websearch-{date}.md. Artifact body includes Displacement read field. Confirm write.
Gate: s2_count >= 5.

STAGE 2 EXIT SIGNAL: websearch_complete(count=[N], confidence=[running_confidence], momentum=[s2_displacement_delta_sum])
  "STAGE 2 EXIT: websearch_complete -- s2_count = [N]. running_confidence = [value]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] websearch_complete received  [ ] Stage 3 = RUN  [ ] s2_ce_verdict recorded
  [ ] Read {topic}-websearch-{date}.md. Extract running_confidence. Validate.
      Mismatch = CHAIN INTEGRITY FAILURE.
  [ ] SESSION INVARIANT D Stage 3 template active

Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D verbatim; DISP DELTA column):

  PRACTITIONER | ACCOUNT    | TEMPLATE APPLIED & VERDICT                                                            | DISP DELTA
  -------------|------------|----------------------------------------------------------------------------------------|------------
  [type 1]     | [account]  | "Does [account] reveal a viable transition path from [incumbent from CAMPAIGN OPEN    | [delta]
  [type 2]     | [account]  |  INCUMBENT ANCHOR] to {topic} for [use case]? [Yes / No / Inconclusive]" (verbatim)  | [delta]
  [type 3]     | [account]  |                                                                                       | [delta]

  s3_count: [N>=3]  s3_displacement_delta_sum: [sum]  s3_ce_verdict: [null/value]
  s3_confidence_delta: [+/-]  running_confidence: [prior+delta]
  displacement_momentum: [s2+s3]  Displacement read: [one sentence]

Write: {topic}-interview-{date}.md. Artifact body includes Displacement read field. Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete(count=[N], confidence=[running_confidence], momentum=[displacement_momentum])
  "STAGE 3 EXIT: interview_complete -- s3_count = [N]. running_confidence = [value].
   displacement_momentum = [value]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] interview_complete received  [ ] Stage 4 = RUN  [ ] s3_ce_verdict recorded
  [ ] Read {topic}-interview-{date}.md. Extract running_confidence AND displacement_momentum.
      Validate both. Mismatch = CHAIN INTEGRITY FAILURE.
  [ ] SESSION INVARIANT D Stage 4 template active

INCUMBENT CHECK TABLE -- Stage 4 (SESSION INVARIANT D verbatim; DISP DELTA column):

  ITEM      | RESULT  | TEMPLATE APPLIED & VERDICT                                                           | DISP DELTA
  ----------|---------|--------------------------------------------------------------------------------------|------------
  prototype | [res]   | "Does [result] make a credible case for displacing [incumbent from CAMPAIGN OPEN    | [delta]
            |         |  INCUMBENT ANCHOR] with {topic}? [Yes / No / Pending]"                             |

  s4_count: [N>=3]  s4_displacement_delta_sum: [delta]  s4_displacement_verdict: [Yes/No/Pending]
  s4_ce_verdict: [null/value]  s4_confidence_delta: [+/-]
  running_confidence: [prior+delta]  displacement_momentum_final: [prior+delta]
  Displacement read: [one sentence]

  null_tally_running:     [S2+S3+S4 null CE verdicts = N]
  null_tally_final:       [N -- freeze here]
  null_tally_cross_check: Running count from Stage 3 was [M]. Final is [N]. Match: [true/false].

Write: {topic}-prototype-{date}.md. Artifact body includes Displacement read field. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[N], confidence=[running_confidence], momentum_final=[displacement_momentum_final], null_tally=[null_tally_final])
  "STAGE 4 EXIT: prototype_complete -- s4_count = [N]. running_confidence = [value].
   null_tally_final = [N]. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] prototype_complete received  [ ] Stage 5 = RUN
  [ ] Read {topic}-prototype-{date}.md. Validate running_confidence AND displacement_momentum_final.
      Mismatch = CHAIN INTEGRITY FAILURE.
  [ ] null_tally_final recorded  [ ] counter_hypothesis from Stage 1 present
  [ ] All five SESSION INVARIANT TABLE rows active (D, A, B, C, E)
  [ ] All three artifact Displacement read fields confirmed written
      [per ROLE A displacement_read_contract -- websearch, interview, prototype].
      Stage 5 will consume all three. Missing = CHAIN INTEGRITY FAILURE. Halt.

### BLOCK 1 -- CONFIDENCE CHAIN RESOLUTION

  prior + s2_delta + s3_delta + s4_delta = confidence_composite: [value]

### BLOCK 2 -- COUNTER-HYPOTHESIS RESOLUTION

  COUNTER_HYPOTHESIS | VERDICT                                  | EVIDENCE
  -------------------|------------------------------------------|--------------------
  [from Stage 1]     | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite artifact]

OPEN RISK: reduce confidence_composite one tier.

### BLOCK 3 -- DISPLACEMENT INTEGRITY CHECK

NULL TALLY CHAIN:
  S2: [s2_ce_verdict, 0/1]  S3: [s3_ce_verdict, 0/1]  S4: [s4_ce_verdict, 0/1]
  null_tally_reconstructed = [sum]
  Cross-check vs Stage 4 null_tally_final: [Match / Mismatch]
  Mismatch = INTEGRITY FAILURE. Halt.

  >= 3: dual_lock_fired (Lock 1: adversarial review, Lock 2: -= 2 cap)
  < 3: not_triggered
  co_activation_confirmed: [dual_lock_fired / not_triggered]

THREE-STAGE DISPLACEMENT CHAIN (STANCE required per row; Y/N = FORMAT ERROR):

  STAGE | DISP DELTA SUM | CUMUL MOMENTUM | STANCE                                            | FLAG?
  ------|----------------|----------------|---------------------------------------------------|------
  S2    | [sum]          | [cumul]        | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]
  S3    | [sum]          | [cumul]        | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]
  S4    | [sum]          | [cumul]        | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]

  chain_pattern: [...]  displacement_conclusion: [...]  incumbent_defense_closed: [true/false]

### SYNTHESIS DECLARATIONS

Do not embed these values in prose sentences. Each on its own line, extractable by label match.

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences. SESSION INVARIANT E (SYNTHESIS EVIDENCE MANDATE)
                           active. Must cite all three artifact Displacement reads
                           (mandatory -- not conditional):
                           websearch Displacement read:  [value from {topic}-websearch-{date}.md]
                           interview Displacement read:  [value from {topic}-interview-{date}.md]
                           prototype Displacement read:  [value from {topic}-prototype-{date}.md]
                           Omission of any artifact Displacement read = SYNTHESIS-FAIL.
                           (echoes SESSION INVARIANTS Invariant E registered failure label)]
  confidence_composite:  [final value after all adjustments]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### HANDOFF TABLE

All 11 fields required. Every field: [derived from: X]. Unlabeled = FAIL.

  FIELD                       | VALUE   | DERIVED FROM
  ----------------------------|---------|----------------------------------
  scout_anchor                | [value] | [derived from: ROLE B]
  incumbent_threat_locked     | [value] | [derived from: ROLE C]
  hypothesis                  | [value] | [derived from: Stage 1]
  counter_hypothesis          | [value] | [derived from: Stage 1]
  s2_ce_verdict               | [value] | [derived from: Stage 2]
  s3_ce_verdict               | [value] | [derived from: Stage 3]
  s4_ce_verdict               | [value] | [derived from: Stage 4]
  null_tally_final            | [value] | [derived from: Stage 4 + Stage 5]
  co_activation_confirmed     | [value] | [derived from: Stage 5 Block 3]
  incumbent_defense_closed    | [value] | [derived from: Stage 5 Block 3]
  confidence_composite        | [value] | [derived from: Stage 5 Block 1]
  schema_compliance_confirmed | [true]  | [Invariant E checkpoint -- FAIL if any field unlabeled]

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story.
   Displacement read chain closed: websearch Displacement read, interview Displacement read,
   prototype Displacement read -- all three cited in evidence_summary. Chain closed."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-03 -- Axis: Stage 0 EXIT SIGNAL Pre-Commits Stage 5 Closure Form and Synthesis Mandate

**Variation hypothesis**: Stage 0 gate_open EXIT SIGNAL explicitly pre-commits both (a) the
terminal closure form ("Chain closed.") and (b) the synthesis omission mandate ("Omission =
FAIL") as named forward-commitments, creating a Stage 0 -> Stage 5 closure chain. This is
structurally analogous to ROLE A displacement_read_contract -> Stage 5 entry verification:
just as ROLE A pre-commits the evidence chain and Stage 5 entry verifies it, Stage 0 can
pre-commit the closure and synthesis mandate forms and Stage 5 can reference them as
registered pre-commitments. Axes V-01 and V-02 do not fire.

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
  A    | ADVERSARIAL REVIEWER TYPE | adversarial_reviewer_type: [challenge role].              | DUAL-LOCK ERROR
       |                           | Activation: null_tally_final >= 3.                        |
  -----|---------------------------|-----------------------------------------------------------|------------------
  B    | CONFIDENCE CAP            | confidence_composite -= 2 if null_tally_final >= 3.       | DUAL-LOCK ERROR
  -----|---------------------------|-----------------------------------------------------------|------------------
  C    | DERIVATION ANNOTATION     | Every handoff field: [derived from: X]. Unlabeled = FAIL. | FAIL

### ROLE OWNERSHIP TABLE

Roles run C -> B -> A before Stage 0 begins.

  ROLE   | TITLE                    | OWNED FIELD                  | GATE S STEP | EXECUTE | DEPENDENCY
  -------|--------------------------|------------------------------|-------------|---------|------------------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked       | Step 1      | FIRST   | INCUMBENT ANCHOR filled
  ROLE B | SCOUT LOADER             | gate_s_cleared                | Step 2      | SECOND  | ROLE C complete
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed  | Step 3      | THIRD   | ROLE B complete

ROLE C execution (fill now):
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact: [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:   [true / false]
  gate_s_cleared: [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

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
  [ ] RESUME AUDIT completed  [ ] CAMPAIGN OPEN + INCUMBENT ANCHOR filled
  [ ] SESSION INVARIANTS TABLE complete -- all four rows filled
  [ ] ROLE C: incumbent_threat_locked = true
  [ ] ROLE B: scout loaded
  [ ] ROLE A: all fields confirmed

CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | RESULT
  -----|------------------------------|---------|---------------------
  1    | incumbent_threat_locked      | ROLE C  | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | [confirm or BLOCKED]

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3 confirmed. SESSION INVARIANT D active.
   ROLE A displacement_read_contract committed.
   Stage 5 pre-commitments registered:
     synthesis_closure_form: 'Chain closed.' (terminal assertion after named-artifact enumeration)
     synthesis_mandate_label: Omission of any artifact Displacement read = FAIL.
   Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] gate_open received  [ ] Stage 1 = RUN
  [ ] scout_artifact available  [ ] SESSION INVARIANT D templates registered

  source_scout_artifact: [path from ROLE B]
  hypothesis:            [falsifiable claim about {topic}]
  counter_hypothesis:    [incumbent's best defense]
  confidence_prior:      [1-10 numeric]

Write: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked
  "STAGE 1 EXIT: hypothesis_locked -- {topic}-hypothesis-{date}.md written. Stage 2 ready."

---

## STAGE 2 -- WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] hypothesis_locked received  [ ] Stage 2 = RUN
  [ ] SESSION INVARIANT D Stage 2 template active

Gather minimum 5 external sources.

INCUMBENT CHECK TABLE -- Stage 2 (SESSION INVARIANT D verbatim; DISP DELTA column):

  ITEM | SOURCE   | SUMMARY   | TEMPLATE APPLIED & VERDICT                                              | DISP DELTA
  -----|----------|-----------|-------------------------------------------------------------------------|------------
  1    | [source] | [summary] | "Does [item] support the displacement of [incumbent from CAMPAIGN OPEN  | [delta]
  2    | [source] | [summary] |  INCUMBENT ANCHOR] by {topic} on [dimension]?                          | [delta]
  3    | [source] | [summary] |  [Yes / No / Inconclusive]" (verbatim; FORMAT ERROR if deviates)        | [delta]
  4    | [source] | [summary] |                                                                         | [delta]
  5    | [source] | [summary] |                                                                         | [delta]

  s2_count: [N>=5]  s2_displacement_delta_sum: [sum]  s2_ce_verdict: [null/value]
  s2_confidence_delta: [+/-]  running_confidence: [prior+delta]
  Displacement read: [one sentence]

Write: {topic}-websearch-{date}.md. Artifact body includes Displacement read field. Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete(count=[N], confidence=[running_confidence], momentum=[s2_displacement_delta_sum])
  "STAGE 2 EXIT: websearch_complete -- s2_count = [N]. running_confidence = [value]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] websearch_complete received  [ ] Stage 3 = RUN  [ ] s2_ce_verdict recorded
  [ ] Read {topic}-websearch-{date}.md. Validate running_confidence.
      Mismatch = CHAIN INTEGRITY FAILURE.
  [ ] SESSION INVARIANT D Stage 3 template active

Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D verbatim; DISP DELTA column):

  PRACTITIONER | ACCOUNT    | TEMPLATE APPLIED & VERDICT                                                            | DISP DELTA
  -------------|------------|----------------------------------------------------------------------------------------|------------
  [type 1]     | [account]  | "Does [account] reveal a viable transition path from [incumbent from CAMPAIGN OPEN    | [delta]
  [type 2]     | [account]  |  INCUMBENT ANCHOR] to {topic} for [use case]? [Yes / No / Inconclusive]" (verbatim)  | [delta]
  [type 3]     | [account]  |                                                                                       | [delta]

  s3_count: [N>=3]  s3_displacement_delta_sum: [sum]  s3_ce_verdict: [null/value]
  s3_confidence_delta: [+/-]  running_confidence: [prior+delta]
  displacement_momentum: [s2+s3]  Displacement read: [one sentence]

Write: {topic}-interview-{date}.md. Artifact body includes Displacement read field. Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete(count=[N], confidence=[running_confidence], momentum=[displacement_momentum])
  "STAGE 3 EXIT: interview_complete -- s3_count = [N]. running_confidence = [value].
   displacement_momentum = [value]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] interview_complete received  [ ] Stage 4 = RUN  [ ] s3_ce_verdict recorded
  [ ] Read {topic}-interview-{date}.md. Validate running_confidence AND displacement_momentum.
      Mismatch = CHAIN INTEGRITY FAILURE.
  [ ] SESSION INVARIANT D Stage 4 template active

INCUMBENT CHECK TABLE -- Stage 4 (SESSION INVARIANT D verbatim; DISP DELTA column):

  ITEM      | RESULT  | TEMPLATE APPLIED & VERDICT                                                           | DISP DELTA
  ----------|---------|--------------------------------------------------------------------------------------|------------
  prototype | [res]   | "Does [result] make a credible case for displacing [incumbent from CAMPAIGN OPEN    | [delta]
            |         |  INCUMBENT ANCHOR] with {topic}? [Yes / No / Pending]"                             |

  s4_count: [N>=3]  s4_displacement_delta_sum: [delta]  s4_displacement_verdict: [Yes/No/Pending]
  s4_ce_verdict: [null/value]  s4_confidence_delta: [+/-]
  running_confidence: [prior+delta]  displacement_momentum_final: [prior+delta]
  Displacement read: [one sentence]

  null_tally_running:     [S2+S3+S4 null CE verdicts = N]
  null_tally_final:       [N -- freeze here]
  null_tally_cross_check: Running count from Stage 3 was [M]. Final is [N]. Match: [true/false].

Write: {topic}-prototype-{date}.md. Artifact body includes Displacement read field. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[N], confidence=[running_confidence], momentum_final=[displacement_momentum_final], null_tally=[null_tally_final])
  "STAGE 4 EXIT: prototype_complete -- s4_count = [N]. running_confidence = [value].
   null_tally_final = [N]. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] prototype_complete received  [ ] Stage 5 = RUN
  [ ] Validate running_confidence AND displacement_momentum_final from prototype artifact.
      Mismatch = CHAIN INTEGRITY FAILURE.
  [ ] null_tally_final recorded  [ ] counter_hypothesis present
  [ ] All four SESSION INVARIANT TABLE rows active
  [ ] All three artifact Displacement read fields confirmed written
      [per ROLE A displacement_read_contract -- websearch, interview, prototype].
      Stage 5 will consume all three. Missing = CHAIN INTEGRITY FAILURE. Halt.
  [ ] Stage 0 pre-commitments active:
      synthesis_closure_form: 'Chain closed.'
      synthesis_mandate_label: Omission of any artifact Displacement read = FAIL.

### BLOCK 1 -- CONFIDENCE CHAIN RESOLUTION

  prior + s2_delta + s3_delta + s4_delta = confidence_composite: [value]

### BLOCK 2 -- COUNTER-HYPOTHESIS RESOLUTION

  COUNTER_HYPOTHESIS | VERDICT                                  | EVIDENCE
  -------------------|------------------------------------------|--------------------
  [from Stage 1]     | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite artifact]

OPEN RISK: reduce confidence_composite one tier.

### BLOCK 3 -- DISPLACEMENT INTEGRITY CHECK

NULL TALLY CHAIN:
  S2: [s2_ce_verdict, 0/1]  S3: [s3_ce_verdict, 0/1]  S4: [s4_ce_verdict, 0/1]
  null_tally_reconstructed = [sum]
  Cross-check vs Stage 4 null_tally_final: [Match / Mismatch]
  Mismatch = INTEGRITY FAILURE. Halt.

  >= 3: dual_lock_fired (Lock 1: adversarial review, Lock 2: -= 2 cap)
  < 3: not_triggered
  co_activation_confirmed: [dual_lock_fired / not_triggered]

THREE-STAGE DISPLACEMENT CHAIN (STANCE required per row; Y/N = FORMAT ERROR):

  STAGE | DISP DELTA SUM | CUMUL MOMENTUM | STANCE                                            | FLAG?
  ------|----------------|----------------|---------------------------------------------------|------
  S2    | [sum]          | [cumul]        | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]
  S3    | [sum]          | [cumul]        | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]
  S4    | [sum]          | [cumul]        | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]

  chain_pattern: [...]  displacement_conclusion: [...]  incumbent_defense_closed: [true/false]

### SYNTHESIS DECLARATIONS

Do not embed these values in prose sentences. Each on its own line, extractable by label match.

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences. Stage 0 synthesis_mandate_label active.
                           Must cite all three artifact Displacement reads
                           (mandatory -- not conditional):
                           websearch Displacement read:  [value from {topic}-websearch-{date}.md]
                           interview Displacement read:  [value from {topic}-interview-{date}.md]
                           prototype Displacement read:  [value from {topic}-prototype-{date}.md]
                           Omission of any artifact Displacement read = FAIL.
                           (per Stage 0 pre-committed synthesis_mandate_label)]
  confidence_composite:  [final value after all adjustments]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### HANDOFF TABLE

All 11 fields required. Every field: [derived from: X]. Unlabeled = FAIL.

  FIELD                       | VALUE   | DERIVED FROM
  ----------------------------|---------|----------------------------------
  scout_anchor                | [value] | [derived from: ROLE B]
  incumbent_threat_locked     | [value] | [derived from: ROLE C]
  hypothesis                  | [value] | [derived from: Stage 1]
  counter_hypothesis          | [value] | [derived from: Stage 1]
  s2_ce_verdict               | [value] | [derived from: Stage 2]
  s3_ce_verdict               | [value] | [derived from: Stage 3]
  s4_ce_verdict               | [value] | [derived from: Stage 4]
  null_tally_final            | [value] | [derived from: Stage 4 + Stage 5]
  co_activation_confirmed     | [value] | [derived from: Stage 5 Block 3]
  incumbent_defense_closed    | [value] | [derived from: Stage 5 Block 3]
  confidence_composite        | [value] | [derived from: Stage 5 Block 1]
  schema_compliance_confirmed | [true]  | [Invariant E checkpoint -- FAIL if any field unlabeled]

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story.
   Displacement read chain closed: websearch Displacement read, interview Displacement read,
   prototype Displacement read -- all three cited in evidence_summary.
   [Per Stage 0 synthesis_closure_form] Chain closed."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-04 -- Axes: V-01 + V-02 Combined (Registered Closure Form + Invariant E)

**Variation hypothesis**: Combining V-01 (CAMPAIGN CLOSURE CANONICAL FORM pre-registered) with
V-02 (Invariant E SYNTHESIS EVIDENCE MANDATE in SESSION INVARIANTS TABLE) creates a fully
registered twin-enforcement architecture: the terminal closure form is pre-registered as a
named canonical block; the synthesis evidence mandate is pre-registered as a named SESSION
INVARIANT. Both have two-layer enforcement (registered source + Stage 5 inline echo). Axis
V-03 does not fire: Stage 0 EXIT SIGNAL uses standard form.

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
any subsequent stage." Register all five before roles execute.
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
  A    | ADVERSARIAL REVIEWER TYPE | adversarial_reviewer_type: [challenge role].              | DUAL-LOCK ERROR
       |                           | Activation: null_tally_final >= 3.                        |
  -----|---------------------------|-----------------------------------------------------------|------------------
  B    | CONFIDENCE CAP            | confidence_composite -= 2 if null_tally_final >= 3.       | DUAL-LOCK ERROR
  -----|---------------------------|-----------------------------------------------------------|------------------
  C    | DERIVATION ANNOTATION     | Every handoff field: [derived from: X]. Unlabeled = FAIL. | FAIL
  -----|---------------------------|-----------------------------------------------------------|------------------
  E    | SYNTHESIS EVIDENCE        | evidence_summary must cite all three artifact             | SYNTHESIS-FAIL
       | MANDATE                   |   Displacement reads: websearch Displacement read,        |
       |                           |   interview Displacement read, prototype Displacement     |
       |                           |   read. Omission of any artifact Displacement read =      |
       |                           |   SYNTHESIS-FAIL. Cannot be modified or bypassed.         |

### CAMPAIGN CLOSURE CANONICAL FORM

Register before roles execute. Stage 5 EXIT SIGNAL must echo this form verbatim.
Deviation from registered form = CLOSURE FORMAT ERROR.

  SIGNAL             | CANONICAL TERMINAL FORM
  -------------------|----------------------------------------------------------------------
  synthesis_complete | "Displacement read chain closed: websearch Displacement read,
                     |  interview Displacement read, prototype Displacement read --
                     |  all three cited in evidence_summary. Chain closed."

### ROLE OWNERSHIP TABLE

Roles run C -> B -> A before Stage 0 begins.

  ROLE   | TITLE                    | OWNED FIELD                  | GATE S STEP | EXECUTE | DEPENDENCY
  -------|--------------------------|------------------------------|-------------|---------|------------------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked       | Step 1      | FIRST   | INCUMBENT ANCHOR filled
  ROLE B | SCOUT LOADER             | gate_s_cleared                | Step 2      | SECOND  | ROLE C complete
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed  | Step 3      | THIRD   | ROLE B complete

ROLE C execution (fill now):
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact: [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:   [true / false]
  gate_s_cleared: [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  incumbent_anchor_read:        [INCUMBENT ANCHOR read: resolved incumbent_name confirmed.
                                  Invariant D binding active. Source: CAMPAIGN OPEN
                                  INCUMBENT ANCHOR sub-section.]
  displacement_read_contract:   [Stages 2, 3, 4 will write Displacement read field to
                                  artifact bodies. Stage 5 entry will confirm all three.]
  invariant_registry_confirmed: [true when all five invariants registered (D, A, B, C, E)]

---

## RESUME AUDIT

  STAGE | ARTIFACT PATTERN                                | FOUND | DECISION
  ------|-------------------------------------------------|-------|---------------------
  1     | simulations/prove/{topic}-hypothesis-{date}.md | [Y/N] | [RESUME-SKIP / RUN]
  2     | simulations/prove/{topic}-websearch-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  3     | simulations/prove/{topic}-interview-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  4     | simulations/prove/{topic}-prototype-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  5     | simulations/prove/{topic}-synthesis-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]

  resume_audit_complete: [true]  stages_to_run: [list or ALL]

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] RESUME AUDIT completed  [ ] CAMPAIGN OPEN + INCUMBENT ANCHOR filled
  [ ] SESSION INVARIANTS TABLE complete -- all five rows (D, A, B, C, E)
  [ ] CAMPAIGN CLOSURE CANONICAL FORM registered
  [ ] ROLE C/B/A all confirmed with displacement_read_contract committed

CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | RESULT
  -----|------------------------------|---------|---------------------
  1    | incumbent_threat_locked      | ROLE C  | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | [confirm or BLOCKED]

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3 confirmed. SESSION INVARIANT D active.
   SESSION INVARIANT E (SYNTHESIS-FAIL) registered. CAMPAIGN CLOSURE CANONICAL FORM on record.
   ROLE A displacement_read_contract committed. Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

  source_scout_artifact: [path from ROLE B]
  hypothesis:            [falsifiable claim about {topic}]
  counter_hypothesis:    [incumbent's best defense]
  confidence_prior:      [1-10]

Write: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked
  "STAGE 1 EXIT: hypothesis_locked -- written. Stage 2 ready."

---

## STAGE 2 -- WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] hypothesis_locked  [ ] Stage 2 = RUN  [ ] SESSION INVARIANT D Stage 2 active

INCUMBENT CHECK TABLE -- Stage 2 (SESSION INVARIANT D verbatim):

  ITEM | SOURCE   | SUMMARY   | TEMPLATE APPLIED & VERDICT                                              | DISP DELTA
  -----|----------|-----------|-------------------------------------------------------------------------|------------
  1-5  | [source] | [summary] | "Does [item] support displacement of [incumbent from CAMPAIGN OPEN      | [delta]
       |          |           |  INCUMBENT ANCHOR] by {topic} on [dim]? [Yes/No/Inconclusive]"         |

  s2_count: [N>=5]  s2_ce_verdict: [null/value]  running_confidence: [prior+delta]
  Displacement read: [one sentence]

Write: {topic}-websearch-{date}.md (includes Displacement read). Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete -- s2_count=[N]. running_confidence=[val]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] websearch_complete  [ ] s2_ce_verdict recorded
  [ ] Validate running_confidence from websearch artifact. Mismatch = CHAIN INTEGRITY FAILURE.
  [ ] SESSION INVARIANT D Stage 3 active

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D verbatim):

  PRACTITIONER | ACCOUNT   | TEMPLATE APPLIED & VERDICT                                                       | DISP DELTA
  -------------|-----------|----------------------------------------------------------------------------------|------------
  [type 1-3]   | [account] | "Does [account] reveal a viable transition path from [incumbent from CAMPAIGN   | [delta]
               |           |  OPEN INCUMBENT ANCHOR] to {topic} for [use case]? [Yes/No/Inconclusive]"      |

  s3_count: [N>=3]  s3_ce_verdict: [null/value]  running_confidence: [prior+delta]
  displacement_momentum: [s2+s3]  Displacement read: [one sentence]

Write: {topic}-interview-{date}.md (includes Displacement read). Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete
  "STAGE 3 EXIT: interview_complete -- s3_count=[N]. displacement_momentum=[val]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] interview_complete  [ ] Validate running_confidence AND displacement_momentum.
      Mismatch = CHAIN INTEGRITY FAILURE.  [ ] SESSION INVARIANT D Stage 4 active

INCUMBENT CHECK TABLE -- Stage 4:

  ITEM      | RESULT | TEMPLATE APPLIED & VERDICT                                                          | DISP DELTA
  ----------|--------|-------------------------------------------------------------------------------------|-----------
  prototype | [res]  | "Does [result] make a credible case for displacing [incumbent from CAMPAIGN OPEN    | [delta]
            |        |  INCUMBENT ANCHOR] with {topic}? [Yes / No / Pending]"                             |

  s4_displacement_verdict: [Yes/No/Pending]  s4_ce_verdict: [null/value]
  running_confidence: [prior+delta]  displacement_momentum_final: [prior+delta]
  Displacement read: [one sentence]

  null_tally_final:       [S2+S3+S4 null CE verdicts = N]
  null_tally_cross_check: Running count from Stage 3 was [M]. Final is [N]. Match: [true/false].

Write: {topic}-prototype-{date}.md (includes Displacement read). Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete(null_tally=[N])
  "STAGE 4 EXIT: prototype_complete -- null_tally_final=[N]. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] prototype_complete  [ ] Validate running_confidence AND displacement_momentum_final.
      Mismatch = CHAIN INTEGRITY FAILURE.
  [ ] null_tally_final recorded  [ ] counter_hypothesis present
  [ ] All five SESSION INVARIANT TABLE rows active (D, A, B, C, E)
  [ ] All three artifact Displacement read fields confirmed written
      [per ROLE A displacement_read_contract -- websearch, interview, prototype].
      Stage 5 will consume all three. Missing = CHAIN INTEGRITY FAILURE. Halt.

### BLOCK 1 -- CONFIDENCE CHAIN RESOLUTION

  prior + s2_delta + s3_delta + s4_delta = confidence_composite: [value]

### BLOCK 2 -- COUNTER-HYPOTHESIS RESOLUTION

  COUNTER_HYPOTHESIS | VERDICT                                  | EVIDENCE
  -------------------|------------------------------------------|--------------------
  [from Stage 1]     | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite artifact]

OPEN RISK: reduce confidence_composite one tier.

### BLOCK 3 -- DISPLACEMENT INTEGRITY CHECK

NULL TALLY:
  S2/S3/S4 null contributions -> null_tally_reconstructed = [sum]
  Cross-check vs Stage 4: [Match / Mismatch]  Mismatch = INTEGRITY FAILURE. Halt.
  >= 3: dual_lock_fired (Lock 1 + Lock 2)  < 3: not_triggered
  co_activation_confirmed: [value]

THREE-STAGE DISPLACEMENT CHAIN:

  STAGE | DISP DELTA | CUMUL MOMENTUM | STANCE                                            | FLAG?
  ------|------------|----------------|---------------------------------------------------|------
  S2    | [sum]      | [cumul]        | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]
  S3    | [sum]      | [cumul]        | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]
  S4    | [sum]      | [cumul]        | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]

  displacement_conclusion: [...]  incumbent_defense_closed: [true/false]

### SYNTHESIS DECLARATIONS

Do not embed these values in prose sentences. Each on its own line, extractable by label match.

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences. SESSION INVARIANT E (SYNTHESIS EVIDENCE MANDATE)
                           active -- SYNTHESIS-FAIL if any artifact Displacement read omitted.
                           Must cite all three artifact Displacement reads (mandatory):
                           websearch Displacement read:  [value from {topic}-websearch-{date}.md]
                           interview Displacement read:  [value from {topic}-interview-{date}.md]
                           prototype Displacement read:  [value from {topic}-prototype-{date}.md]
                           Omission of any artifact Displacement read = SYNTHESIS-FAIL.
                           (echoes SESSION INVARIANTS Invariant E registered failure label)]
  confidence_composite:  [final value after all adjustments]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### HANDOFF TABLE

All 11 fields + schema_compliance_confirmed. Every field: [derived from: X]. Unlabeled = FAIL.

  FIELD                       | VALUE   | DERIVED FROM
  ----------------------------|---------|----------------------------------
  scout_anchor                | [value] | [derived from: ROLE B]
  incumbent_threat_locked     | [value] | [derived from: ROLE C]
  hypothesis                  | [value] | [derived from: Stage 1]
  counter_hypothesis          | [value] | [derived from: Stage 1]
  s2_ce_verdict               | [value] | [derived from: Stage 2]
  s3_ce_verdict               | [value] | [derived from: Stage 3]
  s4_ce_verdict               | [value] | [derived from: Stage 4]
  null_tally_final            | [value] | [derived from: Stage 4 + Stage 5]
  co_activation_confirmed     | [value] | [derived from: Stage 5 Block 3]
  incumbent_defense_closed    | [value] | [derived from: Stage 5 Block 3]
  confidence_composite        | [value] | [derived from: Stage 5 Block 1]
  schema_compliance_confirmed | [true]  | [Invariant E checkpoint -- FAIL if any field unlabeled]

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story.
   Echoing registered CAMPAIGN CLOSURE CANONICAL FORM:
   Displacement read chain closed: websearch Displacement read, interview Displacement read,
   prototype Displacement read -- all three cited in evidence_summary. Chain closed."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-05 -- Full Integration: V-01 + V-02 + V-03 + C-14 Dual-Lock Label Precision

**Variation hypothesis**: All three single-axis improvements combined, plus the dual-lock
inline label precision fix. C-14 in R8 was universally PARTIAL because Block 3 dual-lock
inline used "dual_lock_fired / BLOCKED" rather than echoing the registered "DUAL-LOCK ERROR"
label from SESSION INVARIANTS. Under v9 C-14 is 1 pt with a lower pass bar, but the precise
echo ("DUAL-LOCK ERROR if bypassed" at each lock step) creates cleaner two-layer enforcement
and could yield a new excellence signal. V-05 is the R9 convergence candidate.

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
any subsequent stage." Register all five before roles execute.
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
  A    | ADVERSARIAL REVIEWER TYPE | adversarial_reviewer_type: [challenge role]. Activation:  | DUAL-LOCK ERROR
       |                           |   null_tally_final >= 3. Cannot be bypassed at synthesis. |
  -----|---------------------------|-----------------------------------------------------------|------------------
  B    | CONFIDENCE CAP            | confidence_composite -= 2 if null_tally_final >= 3.       | DUAL-LOCK ERROR
       |                           |   Hard cap. Cannot be softened or overridden.             |
  -----|---------------------------|-----------------------------------------------------------|------------------
  C    | DERIVATION ANNOTATION     | Every handoff field: [derived from: X]. Unlabeled = FAIL. | FAIL
       |                           | Cannot be modified or bypassed at synthesis.              |
  -----|---------------------------|-----------------------------------------------------------|------------------
  E    | SYNTHESIS EVIDENCE        | evidence_summary must cite all three artifact             | SYNTHESIS-FAIL
       | MANDATE                   |   Displacement reads: websearch Displacement read,        |
       |                           |   interview Displacement read, prototype Displacement     |
       |                           |   read. Omission of any artifact Displacement read =      |
       |                           |   SYNTHESIS-FAIL. Cannot be modified or bypassed.         |

### CAMPAIGN CLOSURE CANONICAL FORM

Register before roles execute. Stage 5 EXIT SIGNAL must echo this form verbatim.
Deviation from registered form = CLOSURE FORMAT ERROR.

  SIGNAL             | CANONICAL TERMINAL FORM
  -------------------|----------------------------------------------------------------------
  synthesis_complete | "Displacement read chain closed: websearch Displacement read,
                     |  interview Displacement read, prototype Displacement read --
                     |  all three cited in evidence_summary. Chain closed."

### ROLE OWNERSHIP TABLE

ROLE C executes first. Roles run C -> B -> A before Stage 0 begins.

  ROLE   | TITLE                    | OWNED FIELD                  | GATE S STEP | EXECUTE | DEPENDENCY
  -------|--------------------------|------------------------------|-------------|---------|------------------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked       | Step 1      | FIRST   | INCUMBENT ANCHOR filled
  ROLE B | SCOUT LOADER             | gate_s_cleared                | Step 2      | SECOND  | ROLE C complete
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed  | Step 3      | THIRD   | ROLE B complete

ROLE C execution (fill now):
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact: [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:   [true / false]
  gate_s_cleared: [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  incumbent_anchor_read:        [INCUMBENT ANCHOR read: resolved incumbent_name confirmed.
                                  Invariant D binding active. Source: CAMPAIGN OPEN
                                  INCUMBENT ANCHOR sub-section.]
  displacement_read_contract:   [Stages 2, 3, 4 will write Displacement read field to
                                  artifact bodies. Stage 5 entry will confirm all three
                                  by verifying this contract before synthesis proceeds.]
  invariant_registry_confirmed: [true when all five invariants registered (D, A, B, C, E)]

---

## RESUME AUDIT

  STAGE | ARTIFACT PATTERN                                | FOUND | DECISION
  ------|-------------------------------------------------|-------|---------------------
  1     | simulations/prove/{topic}-hypothesis-{date}.md | [Y/N] | [RESUME-SKIP / RUN]
  2     | simulations/prove/{topic}-websearch-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  3     | simulations/prove/{topic}-interview-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  4     | simulations/prove/{topic}-prototype-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  5     | simulations/prove/{topic}-synthesis-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]

  resume_audit_complete: [true]  stages_to_run: [list or ALL]

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] RESUME AUDIT completed  [ ] CAMPAIGN OPEN + INCUMBENT ANCHOR filled
  [ ] SESSION INVARIANTS TABLE complete -- all five rows (D, A, B, C, E)
  [ ] CAMPAIGN CLOSURE CANONICAL FORM registered
  [ ] ROLE C: incumbent_threat_locked = true
  [ ] ROLE B: scout loaded  [ ] ROLE A: all fields confirmed, five invariants registered

CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|---------------------------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3 all confirmed. SESSION INVARIANT D active.
   SESSION INVARIANT E (SYNTHESIS-FAIL) registered. CAMPAIGN CLOSURE CANONICAL FORM on record.
   ROLE A displacement_read_contract committed.
   Stage 5 pre-commitments registered:
     synthesis_closure_form: 'Chain closed.' (terminal assertion after named-artifact enumeration)
     synthesis_mandate_label: Omission of any artifact Displacement read = FAIL.
   Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] gate_open received  [ ] Stage 1 = RUN
  [ ] scout_artifact available  [ ] SESSION INVARIANT D templates registered

  source_scout_artifact: [path from ROLE B -- copied, not inferred]
  hypothesis:            [falsifiable claim about {topic}]
  counter_hypothesis:    [incumbent's best defense -- grounded in ROLE C analysis]
  confidence_prior:      [1-10 numeric]

Write: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked
  "STAGE 1 EXIT: hypothesis_locked -- {topic}-hypothesis-{date}.md written. Stage 2 ready."

---

## STAGE 2 -- WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] hypothesis_locked received  [ ] Stage 2 = RUN
  [ ] SESSION INVARIANT D Stage 2 template active (verbatim from table row D)

Gather minimum 5 external sources.

INCUMBENT CHECK TABLE -- Stage 2 (SESSION INVARIANT D verbatim; DISP DELTA column):

  ITEM | SOURCE   | SUMMARY   | TEMPLATE APPLIED & VERDICT                                              | DISP DELTA
  -----|----------|-----------|-------------------------------------------------------------------------|------------
  1    | [source] | [summary] | "Does [item] support the displacement of [incumbent from CAMPAIGN OPEN  | [delta]
  2    | [source] | [summary] |  INCUMBENT ANCHOR] by {topic} on [dimension]?                          | [delta]
  3    | [source] | [summary] |  [Yes / No / Inconclusive]" (verbatim; FORMAT ERROR if deviates)        | [delta]
  4    | [source] | [summary] |                                                                         | [delta]
  5    | [source] | [summary] |                                                                         | [delta]

  s2_count: [N>=5]  s2_displacement_delta_sum: [sum]  s2_ce_verdict: [null/value]
  s2_confidence_delta: [+/-]  running_confidence: [prior+delta]
  Displacement read: [one sentence]

Write: {topic}-websearch-{date}.md. Artifact body includes Displacement read field. Confirm write.
Gate: s2_count >= 5.

STAGE 2 EXIT SIGNAL: websearch_complete(count=[N], confidence=[running_confidence], momentum=[s2_displacement_delta_sum])
  "STAGE 2 EXIT: websearch_complete -- s2_count = [N]. running_confidence = [value]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] websearch_complete received  [ ] Stage 3 = RUN  [ ] s2_ce_verdict recorded
  [ ] Read {topic}-websearch-{date}.md. Validate running_confidence.
      Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 3 template active

Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D verbatim; DISP DELTA column):

  PRACTITIONER | ACCOUNT    | TEMPLATE APPLIED & VERDICT                                                            | DISP DELTA
  -------------|------------|----------------------------------------------------------------------------------------|------------
  [type 1]     | [account]  | "Does [account] reveal a viable transition path from [incumbent from CAMPAIGN OPEN    | [delta]
  [type 2]     | [account]  |  INCUMBENT ANCHOR] to {topic} for [use case]? [Yes / No / Inconclusive]" (verbatim)  | [delta]
  [type 3]     | [account]  |                                                                                       | [delta]

  s3_count: [N>=3]  s3_displacement_delta_sum: [sum]  s3_ce_verdict: [null/value]
  s3_confidence_delta: [+/-]  running_confidence: [prior+delta]
  displacement_momentum: [s2+s3]  Displacement read: [one sentence]

Write: {topic}-interview-{date}.md. Artifact body includes Displacement read field. Confirm write.
Gate: s3_count >= 3.

STAGE 3 EXIT SIGNAL: interview_complete(count=[N], confidence=[running_confidence], momentum=[displacement_momentum])
  "STAGE 3 EXIT: interview_complete -- s3_count = [N]. running_confidence = [value].
   displacement_momentum = [value]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] interview_complete received  [ ] Stage 4 = RUN  [ ] s3_ce_verdict recorded
  [ ] Read {topic}-interview-{date}.md. Validate running_confidence AND displacement_momentum.
      Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 4 template active

  prototype_design: [brief description]  prototype_result: [what was learned]

INCUMBENT CHECK TABLE -- Stage 4 (SESSION INVARIANT D verbatim; DISP DELTA column):

  ITEM      | RESULT  | TEMPLATE APPLIED & VERDICT                                                           | DISP DELTA
  ----------|---------|--------------------------------------------------------------------------------------|------------
  prototype | [res]   | "Does [result] make a credible case for displacing [incumbent from CAMPAIGN OPEN    | [delta]
            |         |  INCUMBENT ANCHOR] with {topic}? [Yes / No / Pending]"                             |

  s4_count: [N>=3]  s4_displacement_delta_sum: [delta]  s4_displacement_verdict: [Yes/No/Pending]
  s4_ce_verdict: [null/value]  s4_confidence_delta: [+/-]
  running_confidence: [prior+delta]  displacement_momentum_final: [prior+delta]
  Displacement read: [one sentence]

  null_tally_running:     [S2+S3+S4 null CE verdicts = N]
  null_tally_final:       [N -- freeze here at Stage 4 close]
  null_tally_cross_check: Running count from Stage 3 was [M]. Final is [N]. Match: [true/false].

Write: {topic}-prototype-{date}.md. Artifact body includes Displacement read field. Confirm write.
Gate: s4_count >= 3.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[N], confidence=[running_confidence], momentum_final=[displacement_momentum_final], null_tally=[null_tally_final])
  "STAGE 4 EXIT: prototype_complete -- s4_count = [N]. running_confidence = [value].
   displacement_momentum_final = [value]. s4_ce_verdict = [value].
   null_tally_final = [N]. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] prototype_complete received  [ ] Stage 5 = RUN
  [ ] Read {topic}-prototype-{date}.md. Validate running_confidence AND
      displacement_momentum_final. Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] null_tally_final recorded (from Stage 4 close)
  [ ] counter_hypothesis from Stage 1 present
  [ ] All five SESSION INVARIANT TABLE rows active (D, A, B, C, E)
  [ ] All three artifact Displacement read fields confirmed written
      [per ROLE A displacement_read_contract -- websearch, interview, prototype].
      Stage 5 will consume all three. Missing = CHAIN INTEGRITY FAILURE. Halt.
  [ ] Stage 0 pre-commitments active:
      synthesis_closure_form: 'Chain closed.'
      synthesis_mandate_label: Omission of any artifact Displacement read = FAIL.

### BLOCK 1 -- CONFIDENCE CHAIN RESOLUTION

  prior:                [confidence_prior from Stage 1]
  s2_delta / s3_delta / s4_delta: [each delta]
  chain_equation:       prior + s2_delta + s3_delta + s4_delta = [final]
  confidence_composite: [final -- before counter-hypothesis and cap adjustments]

### BLOCK 2 -- COUNTER-HYPOTHESIS RESOLUTION

  COUNTER_HYPOTHESIS   | VERDICT                                  | EVIDENCE
  ---------------------|------------------------------------------|------------------
  [from Stage 1]       | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite artifact]

OPEN RISK: reduce confidence_composite one tier before BLOCK 3.

### BLOCK 3 -- DISPLACEMENT INTEGRITY CHECK

NULL TALLY CHAIN (Stage 5 reconstruction):
  S2: s2_ce_verdict = [value], null contribution = [0/1]
  S3: s3_ce_verdict = [value], null contribution = [0/1]
  S4: s4_ce_verdict = [value], null contribution = [0/1]
  null_tally_reconstructed = [sum]
  Cross-check vs Stage 4 null_tally_final: [Match / Mismatch]
  Mismatch = INTEGRITY FAILURE. Halt.

If null_tally_final >= 3:
  co_activation_confirmed: dual_lock_fired
  Lock 1 (SESSION INVARIANT A): adversarial review by [adversarial_reviewer_type] mandatory.
    Bypassing adversarial review = DUAL-LOCK ERROR. (echoes registered SESSION INVARIANT A label)
  Lock 2 (SESSION INVARIANT B): confidence_composite -= 2 applied (hard cap).
    Softening or overriding cap = DUAL-LOCK ERROR. (echoes registered SESSION INVARIANT B label)
Else:
  co_activation_confirmed: not_triggered

THREE-STAGE DISPLACEMENT CHAIN (STANCE required per row; Y/N = FORMAT ERROR):

  STAGE | DISP DELTA SUM | CUMUL MOMENTUM | STANCE                                            | FLAG?
  ------|----------------|----------------|---------------------------------------------------|------
  S2    | [s2_disp_sum]  | [s2_cumul]     | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]
  S3    | [s3_disp_sum]  | [s3_cumul]     | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]
  S4    | [s4_disp_sum]  | [s4_cumul]     | [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED] | [Y/N]

  chain_pattern:            [ACCELERATING / STEADY_BUILD / PLATEAU / LATE_REVERSAL / ...]
  displacement_conclusion:  [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  incumbent_defense_closed: [true when flagged rows reconciled]

### SYNTHESIS DECLARATIONS

Do not embed these values in prose sentences. Each on its own line, extractable by label match.

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences. SESSION INVARIANT E (SYNTHESIS EVIDENCE MANDATE)
                           active. Stage 0 synthesis_mandate_label active.
                           Must cite all three artifact Displacement reads (mandatory):
                           websearch Displacement read:  [value from {topic}-websearch-{date}.md]
                           interview Displacement read:  [value from {topic}-interview-{date}.md]
                           prototype Displacement read:  [value from {topic}-prototype-{date}.md]
                           Omission of any artifact Displacement read = SYNTHESIS-FAIL.
                           (echoes SESSION INVARIANTS Invariant E + Stage 0 synthesis_mandate_label)]
  confidence_composite:  [final value after all adjustments]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### HANDOFF TABLE

All 11 fields required. Every field: [derived from: X] annotation. Unlabeled = FAIL.
schema_compliance_confirmed echoes registered failure label from SESSION INVARIANTS.

  FIELD                       | VALUE   | DERIVED FROM
  ----------------------------|---------|----------------------------------
  scout_anchor                | [value] | [derived from: ROLE B]
  incumbent_threat_locked     | [value] | [derived from: ROLE C]
  hypothesis                  | [value] | [derived from: Stage 1]
  counter_hypothesis          | [value] | [derived from: Stage 1]
  s2_ce_verdict               | [value] | [derived from: Stage 2]
  s3_ce_verdict               | [value] | [derived from: Stage 3]
  s4_ce_verdict               | [value] | [derived from: Stage 4]
  null_tally_final            | [value] | [derived from: Stage 4 + Stage 5]
  co_activation_confirmed     | [value] | [derived from: Stage 5 Block 3]
  incumbent_defense_closed    | [value] | [derived from: Stage 5 Block 3]
  confidence_composite        | [value] | [derived from: Stage 5 Block 1]
  schema_compliance_confirmed | [true]  | [Invariant E checkpoint -- FAIL if any field unlabeled]

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story.
   Echoing registered CAMPAIGN CLOSURE CANONICAL FORM:
   Displacement read chain closed: websearch Displacement read, interview Displacement read,
   prototype Displacement read -- all three cited in evidence_summary. Chain closed."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## R9 Variation Matrix

| Variation | Axis | CLOSURE CANONICAL FORM | Invariant E | S0 Pre-commit | Dual-lock precision | C-33 | C-34 |
|-----------|------|------------------------|-------------|---------------|---------------------|------|------|
| V-01 | CAMPAIGN CLOSURE CANONICAL FORM | **YES** | no | no | no | PASS | PASS |
| V-02 | Synthesis Invariant E | no | **YES** | no | no | PASS | PASS |
| V-03 | Stage 0 pre-commit | no | no | **YES** | no | PASS | PASS |
| V-04 | V-01 + V-02 | **YES** | **YES** | no | no | PASS | PASS |
| V-05 | V-01 + V-02 + V-03 + dual-lock | **YES** | **YES** | **YES** | **YES** | PASS | PASS |

**All five variations pass C-33 and C-34 by design** -- C-33 "Chain closed." terminal
assertion and C-34 "Omission = FAIL" label are present in every variation.

**New potential excellence signals in R9:**

| Signal | Variation | Description |
|--------|-----------|-------------|
| CLOSURE CANONICAL echo | V-01/V-04/V-05 | Stage 5 EXIT SIGNAL cites "registered CAMPAIGN CLOSURE CANONICAL FORM" by name -- extends two-layer enforcement to C-33 terminal closure |
| Invariant E dual-layer | V-02/V-04/V-05 | SYNTHESIS DECLARATIONS evidence_summary echoes "SESSION INVARIANTS Invariant E" by name -- two-layer enforcement for C-34 omission label |
| Stage 0 closure chain | V-03/V-05 | Stage 0 EXIT SIGNAL registers synthesis_closure_form + synthesis_mandate_label as named forward-commitments; Stage 5 entry conditions verify them |
| Dual-lock DUAL-LOCK ERROR precision | V-05 | Block 3 Lock 1 + Lock 2 each append "(echoes registered SESSION INVARIANT A/B label) = DUAL-LOCK ERROR if bypassed" -- fixes C-14 partial from R8 |

**R9 scoring note**: Under rubric v9, V-05 from R8 converts to 99/100. All five R9
variations are designed to pass C-33 and C-34 as baseline (targeting 99). The new excellence
signals above are candidates for C-35+ criteria in rubric v10, dependent on scoring results.
