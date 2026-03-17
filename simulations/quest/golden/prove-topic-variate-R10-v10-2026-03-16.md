---
skill: quest-variate
skill_target: prove-topic
round: R10
date: 2026-03-16
rubric: prove-topic-rubric-v10-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [five_invariant_coverage_declaration, stage0_precommit_role_a_crosscheck, closure_canonical_form_consistency_check]
  combined: [V-04 (V-01+V-02), V-05 (V-01+V-02+V-03)]
r9_baseline: >
  V-05 R9 = 103/104 under v10. Aspirational = 29/30. One aspirational criterion from C-09
  through C-34 fails universally across all R9 variations. All four v10 criteria
  (C-35/C-36/C-37/C-38) pass for V-05 R9.
r10_targets: >
  Three candidate C-39+ axes from rubric v10 Excellence Signals section:
  (1) Unified five-invariant SESSION INVARIANTS coverage declaration with COVERAGE FAIL label;
  (2) Stage 0 pre-commit chain cross-verified at ROLE A initialization (three-anchor chain);
  (3) CAMPAIGN CLOSURE CANONICAL FORM consistency check at Stage 0 EXIT SIGNAL.
  All R10 variations inherit full V-05 R9 base. Single-axis variations isolate one new
  structural pattern each. V-05 integrates all three.
---

# prove-topic -- Variation Round R10 (rubric v10)

Five complete, runnable skill body prompts. Each is self-contained -- no diff, no cross-references.
All start from V-05 R9 (103/104) as base and add one new structural axis per single-axis variation.

R10 axes:
- **V-01**: Five-invariant unified SESSION INVARIANTS coverage declaration.
  Named FIVE-INVARIANT ARCHITECTURE COMPLETE block. COVERAGE FAIL canonical label.
  ROLE A initialization echoes five_invariant_coverage_confirmed by block name.
  Stage 5 ENTRY CONDITIONS verify the block is active.
- **V-02**: Stage 0 pre-commit chain cross-verified at ROLE A initialization.
  ROLE A commits stage0_precommit_verification_plan naming Stage 0's two forward-commitment
  fields. Stage 5 ENTRY CONDITIONS cross-reference both fields per ROLE A plan by field name.
  Three-anchor chain: ROLE A plan -> Stage 0 commit -> Stage 5 verify.
- **V-03**: CAMPAIGN CLOSURE CANONICAL FORM consistency check at Stage 0 EXIT SIGNAL.
  Stage 0 EXIT SIGNAL explicitly cross-verifies canonical form against synthesis_closure_form.
  Mismatch = CLOSURE FORMAT ERROR. Closes registration-to-commitment loop at Stage 0.
- **V-04**: V-01 + V-02 combined.
- **V-05**: V-01 + V-02 + V-03 (full integration, R10 convergence candidate).

---

## V-01 -- Axis: Five-Invariant Unified SESSION INVARIANTS Coverage Declaration

**Variation hypothesis**: A named FIVE-INVARIANT ARCHITECTURE COMPLETE block registered
after SESSION INVARIANTS TABLE (before roles execute) creates a coverage-level structural
gate above the per-invariant level. ROLE A initialization echoes five_invariant_coverage_confirmed
by block name, producing two-layer enforcement: registered coverage block -> ROLE A echo.
Stage 5 ENTRY CONDITIONS verify the block was active. Axes V-02 and V-03 absent.

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
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
       |                           |   by {topic} on [dimension]? [Yes / No / Inconclusive]"   |
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

### FIVE-INVARIANT ARCHITECTURE COMPLETE

Register immediately after SESSION INVARIANTS TABLE, before roles execute.
ROLE A initialization must echo five_invariant_coverage_confirmed by this block name.
Any SESSION INVARIANT unregistered at campaign open = COVERAGE FAIL. Cannot be waived.

  INVARIANTS REGISTERED | COVERAGE DECLARATION                                       | FAILURE LABEL
  ----------------------|------------------------------------------------------------|------------------
  D / A / B / C / E     | All five SESSION INVARIANTS registered and active.         | COVERAGE FAIL
                        | Two-layer enforcement architecture complete:                |
                        |   D = FORMAT ERROR, A = DUAL-LOCK ERROR,                   |
                        |   B = DUAL-LOCK ERROR, C = FAIL, E = SYNTHESIS-FAIL.       |
                        | Any SESSION INVARIANT unregistered at campaign open        |
                        |   = COVERAGE FAIL. Cannot be waived.                       |

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

  ROLE   | TITLE                    | OWNED FIELD                  | GATE S STEP | EXECUTE
  -------|--------------------------|------------------------------|-------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked       | Step 1      | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared                | Step 2      | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed  | Step 3      | THIRD

ROLE C execution (fill now):
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact: [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:   [true / false]
  gate_s_cleared: [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  incumbent_anchor_read:             [INCUMBENT ANCHOR read: resolved incumbent_name confirmed.
                                       Invariant D binding active. Source: CAMPAIGN OPEN
                                       INCUMBENT ANCHOR sub-section.]
  displacement_read_contract:        [Stages 2, 3, 4 will write Displacement read field to
                                       artifact bodies. Stage 5 entry will confirm all three
                                       by verifying this contract before synthesis proceeds.]
  five_invariant_coverage_confirmed: [Echoing registered FIVE-INVARIANT ARCHITECTURE COMPLETE
                                       block: All five SESSION INVARIANTS registered (D/A/B/C/E).
                                       Two-layer enforcement architecture complete for all five.
                                       COVERAGE FAIL if any SESSION INVARIANT unregistered.
                                       Source: SESSION INVARIANTS TABLE + FIVE-INVARIANT
                                       ARCHITECTURE COMPLETE block.]
  invariant_registry_confirmed:      [true when all five invariants registered (D, A, B, C, E)
                                       and five_invariant_coverage_confirmed echoed above]

---

## RESUME AUDIT

  STAGE | ARTIFACT PATTERN                                | FOUND | DECISION
  ------|-------------------------------------------------|-------|--------------------
  1     | simulations/prove/{topic}-hypothesis-{date}.md | [Y/N] | [RESUME-SKIP / RUN]
  2     | simulations/prove/{topic}-websearch-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  3     | simulations/prove/{topic}-interview-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  4     | simulations/prove/{topic}-prototype-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  5     | simulations/prove/{topic}-synthesis-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]

  resume_audit_complete: [true]  stages_to_run: [list or ALL]

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] RESUME AUDIT completed
  [ ] CAMPAIGN OPEN + INCUMBENT ANCHOR filled
  [ ] SESSION INVARIANTS TABLE complete -- all five rows (D, A, B, C, E)
  [ ] FIVE-INVARIANT ARCHITECTURE COMPLETE block registered
  [ ] CAMPAIGN CLOSURE CANONICAL FORM registered
  [ ] ROLE C: incumbent_threat_locked = true
  [ ] ROLE B: scout loaded
  [ ] ROLE A: five_invariant_coverage_confirmed echoed, invariant_registry_confirmed = true

CLEARANCE TABLE:
  STEP | FIELD                             | OWNER   | REQUIRED | RESULT
  -----|-----------------------------------|---------|----------|---------------------------
  1    | incumbent_threat_locked           | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared                    | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed      | ROLE A  | true     | [confirm or BLOCKED]
  4    | five_invariant_coverage_confirmed | ROLE A  | echoed   | [confirm or COVERAGE FAIL]

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1-4 all confirmed. SESSION INVARIANT D active.
   SESSION INVARIANT E (SYNTHESIS-FAIL) registered. FIVE-INVARIANT ARCHITECTURE COMPLETE
   confirmed (D/A/B/C/E). CAMPAIGN CLOSURE CANONICAL FORM on record.
   ROLE A displacement_read_contract committed.
   Stage 5 pre-commitments registered:
     synthesis_closure_form: 'Chain closed.'
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

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete -- s2_count=[N]. running_confidence=[value]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] websearch_complete received  [ ] Stage 3 = RUN  [ ] s2_ce_verdict recorded
  [ ] Read {topic}-websearch-{date}.md. Validate running_confidence.
      Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 3 template active

Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D verbatim; DISP DELTA column):

  PRACTITIONER | ACCOUNT   | TEMPLATE APPLIED & VERDICT                                                           | DISP DELTA
  -------------|-----------|--------------------------------------------------------------------------------------|------------
  [type 1]     | [account] | "Does [account] reveal a viable transition path from [incumbent from CAMPAIGN OPEN  | [delta]
  [type 2]     | [account] |  INCUMBENT ANCHOR] to {topic} for [use case]? [Yes / No / Inconclusive]"           | [delta]
  [type 3]     | [account] |  (verbatim; FORMAT ERROR if deviates)                                               | [delta]

  s3_count: [N>=3]  s3_displacement_delta_sum: [sum]  s3_ce_verdict: [null/value]
  s3_confidence_delta: [+/-]  running_confidence: [prior+delta]
  displacement_momentum: [s2+s3]  Displacement read: [one sentence]

Write: {topic}-interview-{date}.md. Artifact body includes Displacement read field. Confirm write.
Gate: s3_count >= 3.

STAGE 3 EXIT SIGNAL: interview_complete
  "STAGE 3 EXIT: interview_complete -- s3_count=[N]. running_confidence=[value].
   displacement_momentum=[value]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] interview_complete received  [ ] Stage 4 = RUN  [ ] s3_ce_verdict recorded
  [ ] Read {topic}-interview-{date}.md. Validate running_confidence AND displacement_momentum.
      Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 4 template active

  prototype_design: [brief description]  prototype_result: [what was learned]

INCUMBENT CHECK TABLE -- Stage 4 (SESSION INVARIANT D verbatim; DISP DELTA column):

  ITEM      | RESULT | TEMPLATE APPLIED & VERDICT                                                          | DISP DELTA
  ----------|--------|--------------------------------------------------------------------------------------|------------
  prototype | [res]  | "Does [result] make a credible case for displacing [incumbent from CAMPAIGN OPEN   | [delta]
            |        |  INCUMBENT ANCHOR] with {topic}? [Yes / No / Pending]" (verbatim)                  |

  s4_displacement_verdict: [Yes/No/Pending]  s4_ce_verdict: [null/value]
  s4_confidence_delta: [+/-]  running_confidence: [prior+delta]
  displacement_momentum_final: [prior+delta]  Displacement read: [one sentence]

  null_tally_final:       [count of null CE verdicts across S2+S3+S4]
  null_tally_cross_check: Running count from Stage 3 was [M]. Final is [N]. Match: [true/false].

Write: {topic}-prototype-{date}.md. Artifact body includes Displacement read field. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete
  "STAGE 4 EXIT: prototype_complete -- running_confidence=[value].
   displacement_momentum_final=[value]. s4_ce_verdict=[value]. null_tally_final=[N]. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] prototype_complete received  [ ] Stage 5 = RUN
  [ ] Read {topic}-prototype-{date}.md. Validate running_confidence AND displacement_momentum_final.
      Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] null_tally_final recorded (from Stage 4 close)
  [ ] counter_hypothesis from Stage 1 present
  [ ] All five SESSION INVARIANT TABLE rows active (D, A, B, C, E)
  [ ] FIVE-INVARIANT ARCHITECTURE COMPLETE verified active (five_invariant_coverage_confirmed
      echoed at ROLE A -- COVERAGE FAIL if missing)
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
  Cross-check vs Stage 4 null_tally_final: [Match / Mismatch -- INTEGRITY FAILURE if mismatch]

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

## V-02 -- Axis: Stage 0 Pre-Commit Chain Cross-Verified at ROLE A Initialization

**Variation hypothesis**: ROLE A initialization (before Stage 0 runs) explicitly names the
Stage 0 forward-commitment fields and commits a verification plan. Stage 5 ENTRY CONDITIONS
cross-reference both Stage 0 committed values AND ROLE A's stage0_precommit_verification_plan
by field name. Three-anchor chain: ROLE A declares -> Stage 0 commits -> Stage 5 verifies
per ROLE A plan. Structural parallel to C-27/C-31. Axes V-01 and V-03 absent.

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
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
       |                           |   by {topic} on [dimension]? [Yes / No / Inconclusive]"   |
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
       | MANDATE                   |   Displacement reads: websearch, interview, prototype.    |
       |                           |   Omission of any = SYNTHESIS-FAIL. Cannot be bypassed.  |

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

  ROLE   | TITLE                    | OWNED FIELD                  | GATE S STEP | EXECUTE
  -------|--------------------------|------------------------------|-------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked       | Step 1      | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared                | Step 2      | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed  | Step 3      | THIRD

ROLE C execution (fill now):
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact: [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:   [true / false]
  gate_s_cleared: [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  incumbent_anchor_read:               [INCUMBENT ANCHOR read: resolved incumbent_name confirmed.
                                         Invariant D binding active. Source: CAMPAIGN OPEN
                                         INCUMBENT ANCHOR sub-section.]
  displacement_read_contract:          [Stages 2, 3, 4 will write Displacement read field to
                                         artifact bodies. Stage 5 entry will confirm all three
                                         by verifying this contract before synthesis proceeds.]
  stage0_precommit_verification_plan:  [Stage 0 EXIT SIGNAL will commit two forward-declaration
                                         fields before Stage 1 begins. ROLE A verification plan:
                                           synthesis_closure_form: expected 'Chain closed.'
                                             (must match CAMPAIGN CLOSURE CANONICAL FORM entry)
                                           synthesis_mandate_label: expected 'Omission of any
                                             artifact Displacement read = FAIL'
                                             (must match SESSION INVARIANTS Invariant E)
                                         Stage 5 ENTRY CONDITIONS will verify both committed
                                         values by field name, cross-referencing this
                                         stage0_precommit_verification_plan. Mismatch from
                                         expected values = CHAIN INTEGRITY FAILURE.]
  invariant_registry_confirmed:        [true when all five invariants registered (D, A, B, C, E)
                                         and stage0_precommit_verification_plan committed above]

---

## RESUME AUDIT

  STAGE | ARTIFACT PATTERN                                | FOUND | DECISION
  ------|-------------------------------------------------|-------|--------------------
  1     | simulations/prove/{topic}-hypothesis-{date}.md | [Y/N] | [RESUME-SKIP / RUN]
  2     | simulations/prove/{topic}-websearch-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  3     | simulations/prove/{topic}-interview-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  4     | simulations/prove/{topic}-prototype-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  5     | simulations/prove/{topic}-synthesis-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]

  resume_audit_complete: [true]  stages_to_run: [list or ALL]

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] RESUME AUDIT completed
  [ ] CAMPAIGN OPEN + INCUMBENT ANCHOR filled
  [ ] SESSION INVARIANTS TABLE complete -- all five rows (D, A, B, C, E)
  [ ] CAMPAIGN CLOSURE CANONICAL FORM registered
  [ ] ROLE C: incumbent_threat_locked = true
  [ ] ROLE B: scout loaded
  [ ] ROLE A: stage0_precommit_verification_plan committed, invariant_registry_confirmed = true

CLEARANCE TABLE:
  STEP | FIELD                              | OWNER   | REQUIRED  | RESULT
  -----|------------------------------------|---------|-----------|---------------------------
  1    | incumbent_threat_locked            | ROLE C  | true      | [confirm or BLOCKED]
  2    | gate_s_cleared                     | ROLE B  | true      | [confirm or BLOCKED]
  3    | invariant_registry_confirmed       | ROLE A  | true      | [confirm or BLOCKED]
  4    | stage0_precommit_verification_plan | ROLE A  | committed | [confirm or BLOCKED]

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1-4 all confirmed. SESSION INVARIANT D active.
   SESSION INVARIANT E (SYNTHESIS-FAIL) registered. CAMPAIGN CLOSURE CANONICAL FORM on record.
   ROLE A displacement_read_contract committed.
   ROLE A stage0_precommit_verification_plan committed.
   Stage 5 pre-commitments registered:
     synthesis_closure_form: 'Chain closed.'
     synthesis_mandate_label: Omission of any artifact Displacement read = FAIL.
   Stage 5 ENTRY CONDITIONS will verify both fields per ROLE A stage0_precommit_verification_plan.
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

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete -- s2_count=[N]. running_confidence=[value]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] websearch_complete received  [ ] Stage 3 = RUN  [ ] s2_ce_verdict recorded
  [ ] Read {topic}-websearch-{date}.md. Validate running_confidence.
      Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 3 template active

Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D verbatim; DISP DELTA column):

  PRACTITIONER | ACCOUNT   | TEMPLATE APPLIED & VERDICT                                                           | DISP DELTA
  -------------|-----------|--------------------------------------------------------------------------------------|------------
  [type 1]     | [account] | "Does [account] reveal a viable transition path from [incumbent from CAMPAIGN OPEN  | [delta]
  [type 2]     | [account] |  INCUMBENT ANCHOR] to {topic} for [use case]? [Yes / No / Inconclusive]"           | [delta]
  [type 3]     | [account] |  (verbatim; FORMAT ERROR if deviates)                                               | [delta]

  s3_count: [N>=3]  s3_displacement_delta_sum: [sum]  s3_ce_verdict: [null/value]
  s3_confidence_delta: [+/-]  running_confidence: [prior+delta]
  displacement_momentum: [s2+s3]  Displacement read: [one sentence]

Write: {topic}-interview-{date}.md. Artifact body includes Displacement read field. Confirm write.
Gate: s3_count >= 3.

STAGE 3 EXIT SIGNAL: interview_complete
  "STAGE 3 EXIT: interview_complete -- s3_count=[N]. running_confidence=[value].
   displacement_momentum=[value]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] interview_complete received  [ ] Stage 4 = RUN  [ ] s3_ce_verdict recorded
  [ ] Read {topic}-interview-{date}.md. Validate running_confidence AND displacement_momentum.
      Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 4 template active

  prototype_design: [brief description]  prototype_result: [what was learned]

INCUMBENT CHECK TABLE -- Stage 4 (SESSION INVARIANT D verbatim; DISP DELTA column):

  ITEM      | RESULT | TEMPLATE APPLIED & VERDICT                                                          | DISP DELTA
  ----------|--------|--------------------------------------------------------------------------------------|------------
  prototype | [res]  | "Does [result] make a credible case for displacing [incumbent from CAMPAIGN OPEN   | [delta]
            |        |  INCUMBENT ANCHOR] with {topic}? [Yes / No / Pending]" (verbatim)                  |

  s4_displacement_verdict: [Yes/No/Pending]  s4_ce_verdict: [null/value]
  s4_confidence_delta: [+/-]  running_confidence: [prior+delta]
  displacement_momentum_final: [prior+delta]  Displacement read: [one sentence]

  null_tally_final:       [count of null CE verdicts across S2+S3+S4]
  null_tally_cross_check: Running count from Stage 3 was [M]. Final is [N]. Match: [true/false].

Write: {topic}-prototype-{date}.md. Artifact body includes Displacement read field. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete
  "STAGE 4 EXIT: prototype_complete -- running_confidence=[value].
   displacement_momentum_final=[value]. s4_ce_verdict=[value]. null_tally_final=[N]. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] prototype_complete received  [ ] Stage 5 = RUN
  [ ] Read {topic}-prototype-{date}.md. Validate running_confidence AND displacement_momentum_final.
      Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] null_tally_final recorded (from Stage 4 close)
  [ ] counter_hypothesis from Stage 1 present
  [ ] All five SESSION INVARIANT TABLE rows active (D, A, B, C, E)
  [ ] All three artifact Displacement read fields confirmed written
      [per ROLE A displacement_read_contract -- websearch, interview, prototype].
      Stage 5 will consume all three. Missing = CHAIN INTEGRITY FAILURE. Halt.
  [ ] Stage 0 pre-commitments verified [per ROLE A stage0_precommit_verification_plan]:
        synthesis_closure_form: 'Chain closed.' -- confirm matches Stage 0 committed value.
        synthesis_mandate_label: 'Omission of any artifact Displacement read = FAIL' --
          confirm matches Stage 0 committed value.
        Both fields verified per stage0_precommit_verification_plan by field name.
        Mismatch from Stage 0 committed values = CHAIN INTEGRITY FAILURE. Halt.

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
  Cross-check vs Stage 4 null_tally_final: [Match / Mismatch -- INTEGRITY FAILURE if mismatch]

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
                           active. Stage 0 synthesis_mandate_label active
                           [per ROLE A stage0_precommit_verification_plan].
                           Must cite all three artifact Displacement reads (mandatory):
                           websearch Displacement read:  [value from {topic}-websearch-{date}.md]
                           interview Displacement read:  [value from {topic}-interview-{date}.md]
                           prototype Displacement read:  [value from {topic}-prototype-{date}.md]
                           Omission of any artifact Displacement read = SYNTHESIS-FAIL.
                           (echoes SESSION INVARIANTS Invariant E + Stage 0 synthesis_mandate_label
                           + ROLE A stage0_precommit_verification_plan)]
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

## V-03 -- Axis: CAMPAIGN CLOSURE CANONICAL FORM Consistency Check at Stage 0 EXIT SIGNAL

**Variation hypothesis**: Stage 0 EXIT SIGNAL explicitly cross-verifies that
synthesis_closure_form (the forward-commitment value) matches the registered CAMPAIGN
CLOSURE CANONICAL FORM terminal form, emitting CLOSURE FORMAT ERROR on mismatch. Closes
the registration-to-commitment loop at Stage 0 before Stage 1 begins -- preventing a
desynced canonical form and commitment from propagating silently to Stage 5. Axes V-01
and V-02 absent.

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
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
       |                           |   by {topic} on [dimension]? [Yes / No / Inconclusive]"   |
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
       | MANDATE                   |   Displacement reads: websearch, interview, prototype.    |
       |                           |   Omission of any = SYNTHESIS-FAIL. Cannot be bypassed.  |

### CAMPAIGN CLOSURE CANONICAL FORM

Register before roles execute. Stage 5 EXIT SIGNAL must echo this form verbatim.
Stage 0 EXIT SIGNAL must verify synthesis_closure_form matches this registered entry.
Deviation = CLOSURE FORMAT ERROR.

  SIGNAL             | CANONICAL TERMINAL FORM
  -------------------|----------------------------------------------------------------------
  synthesis_complete | "Displacement read chain closed: websearch Displacement read,
                     |  interview Displacement read, prototype Displacement read --
                     |  all three cited in evidence_summary. Chain closed."

### ROLE OWNERSHIP TABLE

ROLE C executes first. Roles run C -> B -> A before Stage 0 begins.

  ROLE   | TITLE                    | OWNED FIELD                  | GATE S STEP | EXECUTE
  -------|--------------------------|------------------------------|-------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked       | Step 1      | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared                | Step 2      | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed  | Step 3      | THIRD

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
  ------|-------------------------------------------------|-------|--------------------
  1     | simulations/prove/{topic}-hypothesis-{date}.md | [Y/N] | [RESUME-SKIP / RUN]
  2     | simulations/prove/{topic}-websearch-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  3     | simulations/prove/{topic}-interview-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  4     | simulations/prove/{topic}-prototype-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  5     | simulations/prove/{topic}-synthesis-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]

  resume_audit_complete: [true]  stages_to_run: [list or ALL]

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] RESUME AUDIT completed
  [ ] CAMPAIGN OPEN + INCUMBENT ANCHOR filled
  [ ] SESSION INVARIANTS TABLE complete -- all five rows (D, A, B, C, E)
  [ ] CAMPAIGN CLOSURE CANONICAL FORM registered
  [ ] ROLE C: incumbent_threat_locked = true
  [ ] ROLE B: scout loaded
  [ ] ROLE A: invariant_registry_confirmed = true

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
   CAMPAIGN CLOSURE CANONICAL FORM consistency check:
     Registered canonical form (from CAMPAIGN CLOSURE CANONICAL FORM table):
       'Chain closed.' (terminal assertion)
     synthesis_closure_form pre-committed: 'Chain closed.'
     Consistency: [MATCH -- proceed / MISMATCH -- CLOSURE FORMAT ERROR. Halt.]
   Stage 5 pre-commitments registered:
     synthesis_closure_form: 'Chain closed.' (verified consistent with CAMPAIGN CLOSURE
       CANONICAL FORM registered entry above)
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

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete -- s2_count=[N]. running_confidence=[value]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] websearch_complete received  [ ] Stage 3 = RUN  [ ] s2_ce_verdict recorded
  [ ] Read {topic}-websearch-{date}.md. Validate running_confidence.
      Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 3 template active

Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D verbatim; DISP DELTA column):

  PRACTITIONER | ACCOUNT   | TEMPLATE APPLIED & VERDICT                                                           | DISP DELTA
  -------------|-----------|--------------------------------------------------------------------------------------|------------
  [type 1]     | [account] | "Does [account] reveal a viable transition path from [incumbent from CAMPAIGN OPEN  | [delta]
  [type 2]     | [account] |  INCUMBENT ANCHOR] to {topic} for [use case]? [Yes / No / Inconclusive]"           | [delta]
  [type 3]     | [account] |  (verbatim; FORMAT ERROR if deviates)                                               | [delta]

  s3_count: [N>=3]  s3_displacement_delta_sum: [sum]  s3_ce_verdict: [null/value]
  s3_confidence_delta: [+/-]  running_confidence: [prior+delta]
  displacement_momentum: [s2+s3]  Displacement read: [one sentence]

Write: {topic}-interview-{date}.md. Artifact body includes Displacement read field. Confirm write.
Gate: s3_count >= 3.

STAGE 3 EXIT SIGNAL: interview_complete
  "STAGE 3 EXIT: interview_complete -- s3_count=[N]. running_confidence=[value].
   displacement_momentum=[value]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] interview_complete received  [ ] Stage 4 = RUN  [ ] s3_ce_verdict recorded
  [ ] Read {topic}-interview-{date}.md. Validate running_confidence AND displacement_momentum.
      Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 4 template active

  prototype_design: [brief description]  prototype_result: [what was learned]

INCUMBENT CHECK TABLE -- Stage 4 (SESSION INVARIANT D verbatim; DISP DELTA column):

  ITEM      | RESULT | TEMPLATE APPLIED & VERDICT                                                          | DISP DELTA
  ----------|--------|--------------------------------------------------------------------------------------|------------
  prototype | [res]  | "Does [result] make a credible case for displacing [incumbent from CAMPAIGN OPEN   | [delta]
            |        |  INCUMBENT ANCHOR] with {topic}? [Yes / No / Pending]" (verbatim)                  |

  s4_displacement_verdict: [Yes/No/Pending]  s4_ce_verdict: [null/value]
  s4_confidence_delta: [+/-]  running_confidence: [prior+delta]
  displacement_momentum_final: [prior+delta]  Displacement read: [one sentence]

  null_tally_final:       [count of null CE verdicts across S2+S3+S4]
  null_tally_cross_check: Running count from Stage 3 was [M]. Final is [N]. Match: [true/false].

Write: {topic}-prototype-{date}.md. Artifact body includes Displacement read field. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete
  "STAGE 4 EXIT: prototype_complete -- running_confidence=[value].
   displacement_momentum_final=[value]. s4_ce_verdict=[value]. null_tally_final=[N]. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] prototype_complete received  [ ] Stage 5 = RUN
  [ ] Read {topic}-prototype-{date}.md. Validate running_confidence AND displacement_momentum_final.
      Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] null_tally_final recorded (from Stage 4 close)
  [ ] counter_hypothesis from Stage 1 present
  [ ] All five SESSION INVARIANT TABLE rows active (D, A, B, C, E)
  [ ] All three artifact Displacement read fields confirmed written
      [per ROLE A displacement_read_contract -- websearch, interview, prototype].
      Stage 5 will consume all three. Missing = CHAIN INTEGRITY FAILURE. Halt.
  [ ] Stage 0 pre-commitments active (consistency-verified at Stage 0 EXIT SIGNAL):
      synthesis_closure_form: 'Chain closed.' (verified consistent with CAMPAIGN CLOSURE
        CANONICAL FORM at Stage 0 EXIT)
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
  Cross-check vs Stage 4 null_tally_final: [Match / Mismatch -- INTEGRITY FAILURE if mismatch]

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
                           active. Stage 0 synthesis_mandate_label active (consistency-verified
                           at Stage 0 EXIT SIGNAL against CAMPAIGN CLOSURE CANONICAL FORM).
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

## V-04 -- Combined: V-01 + V-02 (Five-Invariant Coverage + Stage 0 Three-Anchor Chain)

**Variation hypothesis**: FIVE-INVARIANT ARCHITECTURE COMPLETE block (V-01) combined with
stage0_precommit_verification_plan at ROLE A initialization (V-02). Two orthogonal structural
axes: V-01 adds a coverage-level gate at campaign-open time; V-02 adds a pre-commitment
verification chain across ROLE A -> Stage 0 -> Stage 5. Together they close two independent
gaps: V-01 prevents a missing SESSION INVARIANT from going undetected; V-02 prevents
synthesis_closure_form and synthesis_mandate_label from becoming desynced between Stage 0
commitment and Stage 5 verification without ROLE A awareness. Axis V-03 absent.

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
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
       |                           |   by {topic} on [dimension]? [Yes / No / Inconclusive]"   |
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
       | MANDATE                   |   Displacement reads: websearch, interview, prototype.    |
       |                           |   Omission of any = SYNTHESIS-FAIL. Cannot be bypassed.  |

### FIVE-INVARIANT ARCHITECTURE COMPLETE

Register immediately after SESSION INVARIANTS TABLE, before roles execute.
ROLE A initialization must echo five_invariant_coverage_confirmed by this block name.
Any SESSION INVARIANT unregistered at campaign open = COVERAGE FAIL. Cannot be waived.

  INVARIANTS REGISTERED | COVERAGE DECLARATION                                       | FAILURE LABEL
  ----------------------|------------------------------------------------------------|------------------
  D / A / B / C / E     | All five SESSION INVARIANTS registered and active.         | COVERAGE FAIL
                        | Two-layer enforcement architecture complete:                |
                        |   D = FORMAT ERROR, A = DUAL-LOCK ERROR,                   |
                        |   B = DUAL-LOCK ERROR, C = FAIL, E = SYNTHESIS-FAIL.       |
                        | Any SESSION INVARIANT unregistered at campaign open        |
                        |   = COVERAGE FAIL. Cannot be waived.                       |

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

  ROLE   | TITLE                    | OWNED FIELD                  | GATE S STEP | EXECUTE
  -------|--------------------------|------------------------------|-------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked       | Step 1      | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared                | Step 2      | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed  | Step 3      | THIRD

ROLE C execution (fill now):
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact: [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:   [true / false]
  gate_s_cleared: [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  incumbent_anchor_read:               [INCUMBENT ANCHOR read: resolved incumbent_name confirmed.
                                         Invariant D binding active. Source: CAMPAIGN OPEN
                                         INCUMBENT ANCHOR sub-section.]
  displacement_read_contract:          [Stages 2, 3, 4 will write Displacement read field to
                                         artifact bodies. Stage 5 entry will confirm all three
                                         by verifying this contract before synthesis proceeds.]
  five_invariant_coverage_confirmed:   [Echoing registered FIVE-INVARIANT ARCHITECTURE COMPLETE
                                         block: All five SESSION INVARIANTS registered (D/A/B/C/E).
                                         Two-layer enforcement architecture complete for all five.
                                         COVERAGE FAIL if any SESSION INVARIANT unregistered.
                                         Source: SESSION INVARIANTS TABLE + FIVE-INVARIANT
                                         ARCHITECTURE COMPLETE block.]
  stage0_precommit_verification_plan:  [Stage 0 EXIT SIGNAL will commit two forward-declaration
                                         fields before Stage 1 begins. ROLE A verification plan:
                                           synthesis_closure_form: expected 'Chain closed.'
                                           synthesis_mandate_label: expected 'Omission of any
                                             artifact Displacement read = FAIL'
                                         Stage 5 ENTRY CONDITIONS will verify both values by
                                         field name, cross-referencing this plan. Mismatch
                                         = CHAIN INTEGRITY FAILURE.]
  invariant_registry_confirmed:        [true when all five invariants registered,
                                         five_invariant_coverage_confirmed echoed, and
                                         stage0_precommit_verification_plan committed above]

---

## RESUME AUDIT

  STAGE | ARTIFACT PATTERN                                | FOUND | DECISION
  ------|-------------------------------------------------|-------|--------------------
  1     | simulations/prove/{topic}-hypothesis-{date}.md | [Y/N] | [RESUME-SKIP / RUN]
  2     | simulations/prove/{topic}-websearch-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  3     | simulations/prove/{topic}-interview-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  4     | simulations/prove/{topic}-prototype-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  5     | simulations/prove/{topic}-synthesis-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]

  resume_audit_complete: [true]  stages_to_run: [list or ALL]

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] RESUME AUDIT completed
  [ ] CAMPAIGN OPEN + INCUMBENT ANCHOR filled
  [ ] SESSION INVARIANTS TABLE complete -- all five rows (D, A, B, C, E)
  [ ] FIVE-INVARIANT ARCHITECTURE COMPLETE block registered
  [ ] CAMPAIGN CLOSURE CANONICAL FORM registered
  [ ] ROLE C: incumbent_threat_locked = true
  [ ] ROLE B: scout loaded
  [ ] ROLE A: five_invariant_coverage_confirmed echoed, stage0_precommit_verification_plan
      committed, invariant_registry_confirmed = true

CLEARANCE TABLE:
  STEP | FIELD                             | OWNER   | REQUIRED  | RESULT
  -----|-----------------------------------|---------|-----------|---------------------------
  1    | incumbent_threat_locked           | ROLE C  | true      | [confirm or BLOCKED]
  2    | gate_s_cleared                    | ROLE B  | true      | [confirm or BLOCKED]
  3    | invariant_registry_confirmed      | ROLE A  | true      | [confirm or BLOCKED]
  4    | five_invariant_coverage_confirmed | ROLE A  | echoed    | [confirm or COVERAGE FAIL]
  5    | stage0_precommit_verification_plan | ROLE A | committed | [confirm or BLOCKED]

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1-5 all confirmed. SESSION INVARIANT D active.
   SESSION INVARIANT E (SYNTHESIS-FAIL) registered. FIVE-INVARIANT ARCHITECTURE COMPLETE
   confirmed (D/A/B/C/E). CAMPAIGN CLOSURE CANONICAL FORM on record.
   ROLE A displacement_read_contract committed.
   ROLE A stage0_precommit_verification_plan committed.
   Stage 5 pre-commitments registered:
     synthesis_closure_form: 'Chain closed.'
     synthesis_mandate_label: Omission of any artifact Displacement read = FAIL.
   Stage 5 ENTRY CONDITIONS will verify both fields per ROLE A stage0_precommit_verification_plan.
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

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete -- s2_count=[N]. running_confidence=[value]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] websearch_complete received  [ ] Stage 3 = RUN  [ ] s2_ce_verdict recorded
  [ ] Read {topic}-websearch-{date}.md. Validate running_confidence.
      Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 3 template active

Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D verbatim; DISP DELTA column):

  PRACTITIONER | ACCOUNT   | TEMPLATE APPLIED & VERDICT                                                           | DISP DELTA
  -------------|-----------|--------------------------------------------------------------------------------------|------------
  [type 1]     | [account] | "Does [account] reveal a viable transition path from [incumbent from CAMPAIGN OPEN  | [delta]
  [type 2]     | [account] |  INCUMBENT ANCHOR] to {topic} for [use case]? [Yes / No / Inconclusive]"           | [delta]
  [type 3]     | [account] |  (verbatim; FORMAT ERROR if deviates)                                               | [delta]

  s3_count: [N>=3]  s3_displacement_delta_sum: [sum]  s3_ce_verdict: [null/value]
  s3_confidence_delta: [+/-]  running_confidence: [prior+delta]
  displacement_momentum: [s2+s3]  Displacement read: [one sentence]

Write: {topic}-interview-{date}.md. Artifact body includes Displacement read field. Confirm write.
Gate: s3_count >= 3.

STAGE 3 EXIT SIGNAL: interview_complete
  "STAGE 3 EXIT: interview_complete -- s3_count=[N]. running_confidence=[value].
   displacement_momentum=[value]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] interview_complete received  [ ] Stage 4 = RUN  [ ] s3_ce_verdict recorded
  [ ] Read {topic}-interview-{date}.md. Validate running_confidence AND displacement_momentum.
      Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 4 template active

  prototype_design: [brief description]  prototype_result: [what was learned]

INCUMBENT CHECK TABLE -- Stage 4 (SESSION INVARIANT D verbatim; DISP DELTA column):

  ITEM      | RESULT | TEMPLATE APPLIED & VERDICT                                                          | DISP DELTA
  ----------|--------|--------------------------------------------------------------------------------------|------------
  prototype | [res]  | "Does [result] make a credible case for displacing [incumbent from CAMPAIGN OPEN   | [delta]
            |        |  INCUMBENT ANCHOR] with {topic}? [Yes / No / Pending]" (verbatim)                  |

  s4_displacement_verdict: [Yes/No/Pending]  s4_ce_verdict: [null/value]
  s4_confidence_delta: [+/-]  running_confidence: [prior+delta]
  displacement_momentum_final: [prior+delta]  Displacement read: [one sentence]

  null_tally_final:       [count of null CE verdicts across S2+S3+S4]
  null_tally_cross_check: Running count from Stage 3 was [M]. Final is [N]. Match: [true/false].

Write: {topic}-prototype-{date}.md. Artifact body includes Displacement read field. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete
  "STAGE 4 EXIT: prototype_complete -- running_confidence=[value].
   displacement_momentum_final=[value]. s4_ce_verdict=[value]. null_tally_final=[N]. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] prototype_complete received  [ ] Stage 5 = RUN
  [ ] Read {topic}-prototype-{date}.md. Validate running_confidence AND displacement_momentum_final.
      Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] null_tally_final recorded (from Stage 4 close)
  [ ] counter_hypothesis from Stage 1 present
  [ ] All five SESSION INVARIANT TABLE rows active (D, A, B, C, E)
  [ ] FIVE-INVARIANT ARCHITECTURE COMPLETE verified active (five_invariant_coverage_confirmed
      echoed at ROLE A -- COVERAGE FAIL if missing)
  [ ] All three artifact Displacement read fields confirmed written
      [per ROLE A displacement_read_contract -- websearch, interview, prototype].
      Stage 5 will consume all three. Missing = CHAIN INTEGRITY FAILURE. Halt.
  [ ] Stage 0 pre-commitments verified [per ROLE A stage0_precommit_verification_plan]:
        synthesis_closure_form: 'Chain closed.' -- confirm matches Stage 0 committed value.
        synthesis_mandate_label: 'Omission of any artifact Displacement read = FAIL' --
          confirm matches Stage 0 committed value.
        Both fields verified by field name per stage0_precommit_verification_plan.
        Mismatch = CHAIN INTEGRITY FAILURE. Halt.

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
  Cross-check vs Stage 4 null_tally_final: [Match / Mismatch -- INTEGRITY FAILURE if mismatch]

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
                           active. Stage 0 synthesis_mandate_label active
                           [per ROLE A stage0_precommit_verification_plan].
                           Must cite all three artifact Displacement reads (mandatory):
                           websearch Displacement read:  [value from {topic}-websearch-{date}.md]
                           interview Displacement read:  [value from {topic}-interview-{date}.md]
                           prototype Displacement read:  [value from {topic}-prototype-{date}.md]
                           Omission of any artifact Displacement read = SYNTHESIS-FAIL.
                           (echoes SESSION INVARIANTS Invariant E + Stage 0 synthesis_mandate_label
                           + ROLE A stage0_precommit_verification_plan)]
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

## V-05 -- Full Integration: V-01 + V-02 + V-03 (R10 Convergence Candidate)

**Variation hypothesis**: All three R10 structural axes combined.
- FIVE-INVARIANT ARCHITECTURE COMPLETE block (V-01): coverage-level gate with COVERAGE FAIL
  label, echoed at ROLE A by block name.
- stage0_precommit_verification_plan at ROLE A (V-02): three-anchor chain ROLE A -> Stage 0
  -> Stage 5, Stage 5 verifies both fields by name cross-referencing ROLE A plan.
- CAMPAIGN CLOSURE CANONICAL FORM consistency check at Stage 0 EXIT (V-03): explicit
  cross-verification that synthesis_closure_form matches registered canonical form, CLOSURE
  FORMAT ERROR if mismatch.
All three axes are non-competing: V-01 operates at campaign-open coverage level, V-02 operates
at ROLE A pre-stage commitment level, V-03 operates at Stage 0 EXIT commitment-registration
consistency level. Together they close three independent structural gaps in the governance layer
above C-35/C-36/C-37/C-38.

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
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
       |                           |   by {topic} on [dimension]? [Yes / No / Inconclusive]"   |
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

### FIVE-INVARIANT ARCHITECTURE COMPLETE

Register immediately after SESSION INVARIANTS TABLE, before roles execute.
ROLE A initialization must echo five_invariant_coverage_confirmed by this block name.
Any SESSION INVARIANT unregistered at campaign open = COVERAGE FAIL. Cannot be waived.

  INVARIANTS REGISTERED | COVERAGE DECLARATION                                       | FAILURE LABEL
  ----------------------|------------------------------------------------------------|------------------
  D / A / B / C / E     | All five SESSION INVARIANTS registered and active.         | COVERAGE FAIL
                        | Two-layer enforcement architecture complete:                |
                        |   D = FORMAT ERROR, A = DUAL-LOCK ERROR,                   |
                        |   B = DUAL-LOCK ERROR, C = FAIL, E = SYNTHESIS-FAIL.       |
                        | Any SESSION INVARIANT unregistered at campaign open        |
                        |   = COVERAGE FAIL. Cannot be waived.                       |

### CAMPAIGN CLOSURE CANONICAL FORM

Register before roles execute. Stage 5 EXIT SIGNAL must echo this form verbatim.
Stage 0 EXIT SIGNAL must verify synthesis_closure_form is consistent with this entry.
Deviation or consistency mismatch = CLOSURE FORMAT ERROR.

  SIGNAL             | CANONICAL TERMINAL FORM
  -------------------|----------------------------------------------------------------------
  synthesis_complete | "Displacement read chain closed: websearch Displacement read,
                     |  interview Displacement read, prototype Displacement read --
                     |  all three cited in evidence_summary. Chain closed."

### ROLE OWNERSHIP TABLE

ROLE C executes first. Roles run C -> B -> A before Stage 0 begins.

  ROLE   | TITLE                    | OWNED FIELD                  | GATE S STEP | EXECUTE
  -------|--------------------------|------------------------------|-------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked       | Step 1      | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared                | Step 2      | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed  | Step 3      | THIRD

ROLE C execution (fill now):
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled]

ROLE B execution (fill now):
  scout_artifact: [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:   [true / false]
  gate_s_cleared: [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  incumbent_anchor_read:               [INCUMBENT ANCHOR read: resolved incumbent_name confirmed.
                                         Invariant D binding active. Source: CAMPAIGN OPEN
                                         INCUMBENT ANCHOR sub-section.]
  displacement_read_contract:          [Stages 2, 3, 4 will write Displacement read field to
                                         artifact bodies. Stage 5 entry will confirm all three
                                         by verifying this contract before synthesis proceeds.]
  five_invariant_coverage_confirmed:   [Echoing registered FIVE-INVARIANT ARCHITECTURE COMPLETE
                                         block: All five SESSION INVARIANTS registered (D/A/B/C/E).
                                         Two-layer enforcement architecture complete for all five.
                                         COVERAGE FAIL if any SESSION INVARIANT unregistered.
                                         Source: SESSION INVARIANTS TABLE + FIVE-INVARIANT
                                         ARCHITECTURE COMPLETE block.]
  stage0_precommit_verification_plan:  [Stage 0 EXIT SIGNAL will commit two forward-declaration
                                         fields before Stage 1 begins. ROLE A verification plan:
                                           synthesis_closure_form: expected 'Chain closed.'
                                             (must match CAMPAIGN CLOSURE CANONICAL FORM entry;
                                             Stage 0 will run consistency check before committing)
                                           synthesis_mandate_label: expected 'Omission of any
                                             artifact Displacement read = FAIL'
                                             (must match SESSION INVARIANTS Invariant E)
                                         Stage 5 ENTRY CONDITIONS will verify both committed
                                         values by field name, cross-referencing this plan.
                                         Mismatch from expected values = CHAIN INTEGRITY FAILURE.]
  invariant_registry_confirmed:        [true when all five invariants registered,
                                         five_invariant_coverage_confirmed echoed,
                                         and stage0_precommit_verification_plan committed]

---

## RESUME AUDIT

  STAGE | ARTIFACT PATTERN                                | FOUND | DECISION
  ------|-------------------------------------------------|-------|--------------------
  1     | simulations/prove/{topic}-hypothesis-{date}.md | [Y/N] | [RESUME-SKIP / RUN]
  2     | simulations/prove/{topic}-websearch-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  3     | simulations/prove/{topic}-interview-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  4     | simulations/prove/{topic}-prototype-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]
  5     | simulations/prove/{topic}-synthesis-{date}.md  | [Y/N] | [RESUME-SKIP / RUN]

  resume_audit_complete: [true]  stages_to_run: [list or ALL]

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] RESUME AUDIT completed
  [ ] CAMPAIGN OPEN + INCUMBENT ANCHOR filled
  [ ] SESSION INVARIANTS TABLE complete -- all five rows (D, A, B, C, E)
  [ ] FIVE-INVARIANT ARCHITECTURE COMPLETE block registered
  [ ] CAMPAIGN CLOSURE CANONICAL FORM registered
  [ ] ROLE C: incumbent_threat_locked = true
  [ ] ROLE B: scout loaded
  [ ] ROLE A: five_invariant_coverage_confirmed echoed, stage0_precommit_verification_plan
      committed, invariant_registry_confirmed = true

CLEARANCE TABLE:
  STEP | FIELD                              | OWNER   | REQUIRED  | RESULT
  -----|------------------------------------|---------|-----------|---------------------------
  1    | incumbent_threat_locked            | ROLE C  | true      | [confirm or BLOCKED]
  2    | gate_s_cleared                     | ROLE B  | true      | [confirm or BLOCKED]
  3    | invariant_registry_confirmed       | ROLE A  | true      | [confirm or BLOCKED]
  4    | five_invariant_coverage_confirmed  | ROLE A  | echoed    | [confirm or COVERAGE FAIL]
  5    | stage0_precommit_verification_plan | ROLE A  | committed | [confirm or BLOCKED]

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1-5 all confirmed. SESSION INVARIANT D active.
   SESSION INVARIANT E (SYNTHESIS-FAIL) registered. FIVE-INVARIANT ARCHITECTURE COMPLETE
   confirmed (D/A/B/C/E). CAMPAIGN CLOSURE CANONICAL FORM on record.
   ROLE A displacement_read_contract committed.
   ROLE A stage0_precommit_verification_plan committed.
   CAMPAIGN CLOSURE CANONICAL FORM consistency check:
     Registered canonical form: 'Chain closed.' (from CAMPAIGN CLOSURE CANONICAL FORM table)
     synthesis_closure_form pre-committed: 'Chain closed.'
     Consistency: [MATCH -- proceed / MISMATCH -- CLOSURE FORMAT ERROR. Halt.]
   Stage 5 pre-commitments registered:
     synthesis_closure_form: 'Chain closed.' (verified consistent with CAMPAIGN CLOSURE
       CANONICAL FORM registered entry)
     synthesis_mandate_label: Omission of any artifact Displacement read = FAIL.
   Stage 5 ENTRY CONDITIONS will verify both fields per ROLE A stage0_precommit_verification_plan.
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

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete -- s2_count=[N]. running_confidence=[value]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] websearch_complete received  [ ] Stage 3 = RUN  [ ] s2_ce_verdict recorded
  [ ] Read {topic}-websearch-{date}.md. Validate running_confidence.
      Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 3 template active

Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE -- Stage 3 (SESSION INVARIANT D verbatim; DISP DELTA column):

  PRACTITIONER | ACCOUNT   | TEMPLATE APPLIED & VERDICT                                                           | DISP DELTA
  -------------|-----------|--------------------------------------------------------------------------------------|------------
  [type 1]     | [account] | "Does [account] reveal a viable transition path from [incumbent from CAMPAIGN OPEN  | [delta]
  [type 2]     | [account] |  INCUMBENT ANCHOR] to {topic} for [use case]? [Yes / No / Inconclusive]"           | [delta]
  [type 3]     | [account] |  (verbatim; FORMAT ERROR if deviates)                                               | [delta]

  s3_count: [N>=3]  s3_displacement_delta_sum: [sum]  s3_ce_verdict: [null/value]
  s3_confidence_delta: [+/-]  running_confidence: [prior+delta]
  displacement_momentum: [s2+s3]  Displacement read: [one sentence]

Write: {topic}-interview-{date}.md. Artifact body includes Displacement read field. Confirm write.
Gate: s3_count >= 3.

STAGE 3 EXIT SIGNAL: interview_complete
  "STAGE 3 EXIT: interview_complete -- s3_count=[N]. running_confidence=[value].
   displacement_momentum=[value]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] interview_complete received  [ ] Stage 4 = RUN  [ ] s3_ce_verdict recorded
  [ ] Read {topic}-interview-{date}.md. Validate running_confidence AND displacement_momentum.
      Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] SESSION INVARIANT D Stage 4 template active

  prototype_design: [brief description]  prototype_result: [what was learned]

INCUMBENT CHECK TABLE -- Stage 4 (SESSION INVARIANT D verbatim; DISP DELTA column):

  ITEM      | RESULT | TEMPLATE APPLIED & VERDICT                                                          | DISP DELTA
  ----------|--------|--------------------------------------------------------------------------------------|------------
  prototype | [res]  | "Does [result] make a credible case for displacing [incumbent from CAMPAIGN OPEN   | [delta]
            |        |  INCUMBENT ANCHOR] with {topic}? [Yes / No / Pending]" (verbatim)                  |

  s4_displacement_verdict: [Yes/No/Pending]  s4_ce_verdict: [null/value]
  s4_confidence_delta: [+/-]  running_confidence: [prior+delta]
  displacement_momentum_final: [prior+delta]  Displacement read: [one sentence]

  null_tally_final:       [count of null CE verdicts across S2+S3+S4]
  null_tally_cross_check: Running count from Stage 3 was [M]. Final is [N]. Match: [true/false].

Write: {topic}-prototype-{date}.md. Artifact body includes Displacement read field. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete
  "STAGE 4 EXIT: prototype_complete -- running_confidence=[value].
   displacement_momentum_final=[value]. s4_ce_verdict=[value]. null_tally_final=[N]. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] prototype_complete received  [ ] Stage 5 = RUN
  [ ] Read {topic}-prototype-{date}.md. Validate running_confidence AND displacement_momentum_final.
      Mismatch = CHAIN INTEGRITY FAILURE. Halt.
  [ ] null_tally_final recorded (from Stage 4 close)
  [ ] counter_hypothesis from Stage 1 present
  [ ] All five SESSION INVARIANT TABLE rows active (D, A, B, C, E)
  [ ] FIVE-INVARIANT ARCHITECTURE COMPLETE verified active (five_invariant_coverage_confirmed
      echoed at ROLE A -- COVERAGE FAIL if missing)
  [ ] All three artifact Displacement read fields confirmed written
      [per ROLE A displacement_read_contract -- websearch, interview, prototype].
      Stage 5 will consume all three. Missing = CHAIN INTEGRITY FAILURE. Halt.
  [ ] Stage 0 pre-commitments verified [per ROLE A stage0_precommit_verification_plan]:
        synthesis_closure_form: 'Chain closed.' -- confirm matches Stage 0 committed value
          (verified consistent with CAMPAIGN CLOSURE CANONICAL FORM at Stage 0 EXIT).
        synthesis_mandate_label: 'Omission of any artifact Displacement read = FAIL' --
          confirm matches Stage 0 committed value.
        Both fields verified by field name per stage0_precommit_verification_plan.
        Mismatch = CHAIN INTEGRITY FAILURE. Halt.

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
  Cross-check vs Stage 4 null_tally_final: [Match / Mismatch -- INTEGRITY FAILURE if mismatch]

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
                           active. Stage 0 synthesis_mandate_label active (consistency-verified
                           at Stage 0 EXIT SIGNAL against CAMPAIGN CLOSURE CANONICAL FORM;
                           per ROLE A stage0_precommit_verification_plan).
                           Must cite all three artifact Displacement reads (mandatory):
                           websearch Displacement read:  [value from {topic}-websearch-{date}.md]
                           interview Displacement read:  [value from {topic}-interview-{date}.md]
                           prototype Displacement read:  [value from {topic}-prototype-{date}.md]
                           Omission of any artifact Displacement read = SYNTHESIS-FAIL.
                           (echoes SESSION INVARIANTS Invariant E + Stage 0 synthesis_mandate_label
                           + ROLE A stage0_precommit_verification_plan)]
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

## R10 Variation Matrix

| Variation | FIVE-INVARIANT COVERAGE | S0 PRECOMMIT ROLE A CHAIN | CLOSURE FORM CONSISTENCY CHECK | C-39? | C-40? | C-41? |
|-----------|------------------------|--------------------------|-------------------------------|-------|-------|-------|
| V-01 | **YES** | no | no | candidate | -- | -- |
| V-02 | no | **YES** | no | -- | candidate | -- |
| V-03 | no | no | **YES** | -- | -- | candidate |
| V-04 | **YES** | **YES** | no | candidate | candidate | -- |
| V-05 | **YES** | **YES** | **YES** | candidate | candidate | candidate |

All five R10 variations carry full V-05 R9 base (103/104 under v10).
V-05 is the R10 convergence candidate: all three new structural axes present
and mutually reinforcing. The three new axes operate at non-competing levels:
V-01 at campaign-open coverage level, V-02 at ROLE A pre-stage commitment level,
V-03 at Stage 0 EXIT registration-consistency level.
