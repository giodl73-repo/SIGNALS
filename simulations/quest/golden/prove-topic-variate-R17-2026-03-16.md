---
skill: quest-variate
skill_target: prove-topic
round: R17
date: 2026-03-16
rubric: prove-topic-rubric-v16-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [exact_value_lockdown, open_risk_confidence_chain, displacement_loop_integrity_check]
  combined: [V-04 (exact_value_lockdown + open_risk_confidence_chain), V-05 (all_three + full_structural_stack)]
r16_anchor: >
  R16 V-05 (100/100 against v15 rubric) introduced: three-role pre-stage (SCOUT LOADER,
  INERTIA ANALYST, CAMPAIGN DIRECTOR), numeric confidence chain, compound dual-value exit
  signals (count + running_confidence), count-gated stage thresholds, resume audit,
  three-point displacement loop (INERTIA ANALYST anchor -> Stage 4 aggregate verdict ->
  Stage 5 displacement_conclusion), and Stage 5 dual-block structure. The v16 rubric
  extracted two of these excellence patterns as new aspirational criteria: C-13 (live
  payload chaining) and C-14 (Stage 5 dual-block CONFIDENCE CHAIN RESOLUTION +
  COUNTER-HYPOTHESIS RESOLUTION). Denominator updates to 6.
r17_context: >
  R16 V-05 already satisfies C-13 and C-14. R17 treats all patterns in R16 V-05 as the
  mandatory baseline (carried in all 5 variations), then explores NEW single-axis
  improvements that probe the edges of C-13 and C-14 and adjacent structural patterns:

  V-01 (single: exact_value_lockdown): The R16 V-05 payload chain uses N as a placeholder
  in entry conditions ("confidence_prior = N") rather than specifying the EXACT expected
  value. V-01 makes entry conditions READ the prior artifact to extract the concrete value,
  then validates received signal payload against that value ("confidence_prior = 7 — read
  from Stage 1 artifact field confidence_prior; mismatch = INTEGRITY FAILURE"). Tests
  whether first-principles value reconstruction (not just named-payload receipt) produces
  a truly tamper-resistant chain distinct from tamper-evident C-13.

  V-02 (single: open_risk_confidence_chain): When COUNTER-HYPOTHESIS RESOLUTION produces
  OPEN RISK, the verdict is currently noted in key_risk informally. V-02 gives OPEN RISK
  a named confidence delta (cr_delta = -1 per OPEN RISK item), adds it to the chain
  equation as an explicit term, and makes the final confidence derivation show ALL five
  contributing deltas: "[prior] + [s2] + [s3] + [s4] + [cr] = [final]". Tests whether
  formalizing counter-hypothesis resolution as a chain contributor produces a more
  defensible confidence derivation and a richer chain_equation.

  V-03 (single: displacement_loop_integrity_check): Stage 5 currently has CONFIDENCE CHAIN
  RESOLUTION and COUNTER-HYPOTHESIS RESOLUTION as two named blocks. V-03 adds a third
  named block: DISPLACEMENT INTEGRITY CHECK, which cross-references displacement_conclusion
  with s4_aggregate_displacement_verdict and flags structural inconsistency before synthesis
  closes. This extends Stage 5 from a dual-block to a triple-block structure. Tests whether
  a named consistency gate between the Stage 4 displacement anchor and the Stage 5
  displacement_conclusion produces a tighter three-point displacement loop than the current
  informal version.

  V-04 (combined: exact_value_lockdown + open_risk_confidence_chain): V-01 + V-02. The
  payload chain is first-principles validated at every stage AND counter-hypothesis
  resolution feeds a named delta into the final confidence equation.

  V-05 (full: all three + full structural stack): V-01 + V-02 + V-03 on top of the complete
  R16 V-05 structural stack. Tests whether all three new axes simultaneously applied produce
  a 6/6 aspirational score against the v16 rubric.
---

# prove-topic Variations — Round 17 (rubric v16)

**Skill**: prove-topic
**Rubric**: v16 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-14 aspirational)
**Date**: 2026-03-16
**Round**: R17

---

## Context: what informed this round

R16 V-05 (100/100 against v15) established the structural stack now used as the R17
baseline. The v16 rubric extracted two patterns from R16 as new aspirational criteria:

| Change | R16 V-05 | R17 target | Design consequence |
|--------|----------|------------|-------------------|
| C-13 (live payload chaining) | signals carry count + running_confidence; entry conditions check `count >= N, running_confidence = N` | All R17 variations carry this baseline | V-01 tightens C-13 by making entry conditions reconstruct the expected value from the prior artifact (exact-value validation vs placeholder N) |
| C-14 (Stage 5 dual-block) | CONFIDENCE CHAIN RESOLUTION -> COUNTER-HYPOTHESIS RESOLUTION, two named sequential blocks | All R17 variations carry this baseline | V-03 extends to triple-block: adds DISPLACEMENT INTEGRITY CHECK as third named block |

All five R17 variations carry the full R16 V-05 structural stack as their floor. Each
variation then applies exactly one new axis (V-01–V-03) or a combination (V-04–V-05).

---

## V-01 — Exact Value Lockdown

**Axis**: exact_value_lockdown (single)
**Hypothesis**: R16 V-05 exit signals carry payloads like `hypothesis_locked(confidence_prior=N)`
and entry conditions check `confidence_prior = N` — but N is a placeholder, not a value.
If the actual value at Stage 1 was 7, the entry condition for Stage 2 should say
`confidence_prior = 7 (read from Stage 1 artifact)`, not `confidence_prior = N`. Making
entry conditions READ the prior artifact, extract the concrete value, and validate the
received signal against it makes the chain tamper-resistant rather than merely tamper-evident.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for a topic. Three named roles execute pre-stage.
Five evidence stages in strict sequence: prove-hypothesis -> prove-websearch ->
prove-intelligence -> prove-analysis -> prove-synthesize. Scout artifact named before
Stage 1. Resumable: pre-run audit marks completed stages RESUME-SKIP. Evidence stages
enforce minimum counts. Confidence flows numerically 1-10 through a chain. Each stage
fires a named EXIT SIGNAL carrying live numeric payload. The NEXT stage's ENTRY CONDITIONS
read the prior artifact, extract the concrete value, and validate received payload against
it — mismatch = CHAIN INTEGRITY FAILURE. Stage 5 synthesizes in two named blocks:
CONFIDENCE CHAIN RESOLUTION, then COUNTER-HYPOTHESIS RESOLUTION. Final output: evidence
brief ready for /topic-story.

---

## CAMPAIGN OPEN

  topic:  {topic}
  date:   {date}

---

### PRE-STAGE: NAMED ROLE EXECUTION (Steps 1-3)

All three roles execute before Stage 1. A later role cannot run until the prior role
confirms its field.

---

**ROLE 1 — SCOUT LOADER** (Step 1 of 3 — executes first)

Locate and confirm the scout artifact.

  scout_artifact:  [{topic}-scout-record-{date}.md — or most recent scout signal for {topic}]
  scout_loaded:    [true / false]
  ROLE 1 STATUS:   [CONFIRMED] or [BLOCKED — record search path, halt campaign]

If scout_loaded = false: CAMPAIGN BLOCKED. Do not advance to ROLE 2.

---

**ROLE 2 — INERTIA ANALYST** (Step 2 of 3 — requires ROLE 1 CONFIRMED)

Name the incumbent and decompose its position.

  status_quo_comparator:    [incumbent approach {topic} must displace]
  comparator_strength:      [one sentence: why the incumbent wins today]
  comparator_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]
  ROLE 2 STATUS:            [CONFIRMED]

---

**ROLE 3 — CAMPAIGN DIRECTOR** (Step 3 of 3 — requires ROLES 1 + 2 CONFIRMED)

Initialize confidence chain register.

CONFIDENCE CHAIN REGISTER:
  confidence_prior:  [to be set in Stage 1]
  s2_delta:          [to be set in Stage 2]
  s3_delta:          [to be set in Stage 3]
  s4_delta:          [to be set in Stage 4]
  confidence_final:  [to be computed in Stage 5]

  CAMPAIGN STATUS:   OPEN

PRE-STAGE EXIT: campaign_open
  "PRE-STAGE COMPLETE — Roles 1, 2, 3 confirmed. Advancing to Stage 1."
Do not begin Stage 1 until PRE-STAGE EXIT is printed.

---

## RESUME AUDIT

Glob for existing artifacts.

  Stage 1: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  Stage 2: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  Stage 3: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  Stage 4: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  Stage 5: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md

Mark each DONE or MISSING. Resume from first MISSING stage.

  s1_status: [RESUME-SKIP / RUN]   s2_status: [RESUME-SKIP / RUN]
  s3_status: [RESUME-SKIP / RUN]   s4_status: [RESUME-SKIP / RUN]
  s5_status: [RESUME-SKIP / RUN]

RESUME AUDIT EXIT: resume_audit_complete
  "RESUME AUDIT COMPLETE — resuming from Stage [N]."

---

## STAGE 1 — HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] EXIT SIGNAL received: resume_audit_complete
  [ ] s1_status = RUN (if RESUME-SKIP: read confidence_prior from Stage 1 artifact and carry
      it as the validated value for Stage 2 entry)
  [ ] scout_artifact confirmed from ROLE 1

STAGE 1 BODY:
Load scout_artifact. Frame hypothesis grounded in its signals.

  source_artifact:    [path — from ROLE 1, not re-inferred]
  hypothesis:         [falsifiable claim derived from scout signals]
  counter_hypothesis: [strongest argument that {topic} fails to displace the incumbent —
                       grounded in ROLE 2 comparator_strength]

CONFIDENCE PRIOR:
  confidence_prior:     [1-10 integer — prior before gathering evidence]
  confidence_reasoning: [one sentence: why this prior, based on scout signals]

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked(confidence_prior={confidence_prior})
  "STAGE 1 EXIT: hypothesis_locked — confidence_prior = [N].
   Stage 2 entry conditions must read this value from the artifact and validate."

---

## STAGE 2 — WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] EXIT SIGNAL received: hypothesis_locked(confidence_prior = ?)
  [ ] EXACT VALUE VALIDATION — read simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md,
      extract field confidence_prior = [V]. Signal must carry [V]. If signal carries a
      different value: CHAIN INTEGRITY FAILURE — record received value vs expected value,
      halt campaign.
  [ ] s2_status = RUN (if RESUME-SKIP: read s2_delta and running_confidence from Stage 2 artifact)

STAGE 2 MINIMUM THRESHOLD: 5 external sources. Do not fire exit until count >= 5.

STAGE 2 BODY:
Gather external sources. Apply displacement check and confidence impact to each row.

  # | SOURCE (URL or citation) | KEY FINDING (1 sentence) | STRENGTH | SUPPORTS? | CONFIDENCE IMPACT
  1 | [source]                 | [finding]                | S/M/W    | Y/N/P     | +N / -N / 0
  2 | [source]                 | [finding]                | S/M/W    | Y/N/P     | +N / -N / 0
  3 | [source]                 | [finding]                | S/M/W    | Y/N/P     | +N / -N / 0
  4 | [source]                 | [finding]                | S/M/W    | Y/N/P     | +N / -N / 0
  5 | [source]                 | [finding]                | S/M/W    | Y/N/P     | +N / -N / 0
  + | add if found             |                          |          |           |

  s2_evidence_count:   [N — verify >= 5]
  s2_delta:            [sum of confidence impact column]
  s2_support_tally:    [Y: N, N: M, Partial: P]
  s2_key_gap:          [what external evidence does not cover]
  running_confidence:  [confidence_prior + s2_delta — capped 1-10]

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete(count={s2_evidence_count}, running_confidence={running_confidence})
  "STAGE 2 EXIT: websearch_complete — count = [N], running_confidence = [N].
   Stage 3 must read these values from artifact and validate."

---

## STAGE 3 — INTELLIGENCE

STAGE 3 ENTRY CONDITIONS:
  [ ] EXIT SIGNAL received: websearch_complete(count = ?, running_confidence = ?)
  [ ] EXACT VALUE VALIDATION — read Stage 2 artifact, extract s2_evidence_count = [V1] and
      running_confidence = [V2]. Signal must carry count >= 5 AND running_confidence = [V2].
      If count < 5: MINIMUM THRESHOLD FAILURE. If running_confidence mismatch: CHAIN
      INTEGRITY FAILURE. Record and halt on either violation.
  [ ] s3_status = RUN (if RESUME-SKIP: read s3_delta and running_confidence from Stage 3 artifact)

STAGE 3 MINIMUM THRESHOLD: 3 internal sources. Do not fire exit until count >= 3.

STAGE 3 BODY:
Search internal sources: codebase, specs, docs, prior signal artifacts.

  # | FILE PATH    | SECTION     | FINDING (1 sentence) | ALIGNS WITH WEB?    | CONFIDENCE IMPACT
  1 | [path]       | [section]   | [finding]            | Y / N / Contradicts | +N / -N / 0
  2 | [path]       | [section]   | [finding]            | Y / N / Contradicts | +N / -N / 0
  3 | [path]       | [section]   | [finding]            | Y / N / Contradicts | +N / -N / 0
  + | add rows     |             |                      |                     |

  s3_sources_found:    [N — verify >= 3]
  s3_delta:            [sum of confidence impact column]
  s3_alignment:        [ALIGNED / CONTRADICTS / MIXED — vs Stage 2]
  s3_key_gap:          [what internal sources do not address]
  running_confidence:  [prev running_confidence + s3_delta — capped 1-10]

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Confirm write.

STAGE 3 EXIT SIGNAL: intelligence_complete(count={s3_sources_found}, running_confidence={running_confidence})
  "STAGE 3 EXIT: intelligence_complete — count = [N], running_confidence = [N].
   Stage 4 must read these values from artifact and validate."

---

## STAGE 4 — ANALYSIS

STAGE 4 ENTRY CONDITIONS:
  [ ] EXIT SIGNAL received: intelligence_complete(count = ?, running_confidence = ?)
  [ ] EXACT VALUE VALIDATION — read Stage 3 artifact, extract s3_sources_found = [V1] and
      running_confidence = [V2]. Signal must carry count >= 3 AND running_confidence = [V2].
      Violation = CHAIN INTEGRITY FAILURE. Record and halt.
  [ ] s4_status = RUN (if RESUME-SKIP: read s4_delta and running_confidence from Stage 4 artifact)

STAGE 4 MINIMUM THRESHOLD: 3 distinct patterns. Do not fire exit until count >= 3.

STAGE 4 BODY:
Analyze patterns across Stages 2 + 3.

  # | PATTERN      | SOURCES (S2-# / S3-filepath) | CAUSAL?        | CONFIDENCE IMPACT
  1 | [pattern]    | [sources]                    | Yes/No/Unknown | +N / -N / 0
  2 | [pattern]    | [sources]                    | Yes/No/Unknown | +N / -N / 0
  3 | [pattern]    | [sources]                    | Yes/No/Unknown | +N / -N / 0
  + | add rows     |                              |                |

Aggregate displacement verdict:
  "Does the aggregate pattern support the displacement of {status_quo_comparator}
   by {topic}? [Yes / No / Inconclusive]"
  s4_aggregate_displacement_verdict: [Yes / No / Inconclusive]

  s4_pattern_count:    [N — verify >= 3]
  s4_delta:            [sum of confidence impact column]
  s4_primary_finding:  [dominant pattern, 1-2 sentences]
  s4_counter_evidence: [strongest evidence against hypothesis — cite artifact + section]
  running_confidence:  [prev running_confidence + s4_delta — capped 1-10]

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Confirm write.

STAGE 4 EXIT SIGNAL: analysis_complete(patterns={s4_pattern_count}, running_confidence={running_confidence})
  "STAGE 4 EXIT: analysis_complete — patterns = [N], running_confidence = [N].
   Stage 5 must read these values from artifact and validate."

---

## STAGE 5 — SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] EXIT SIGNAL received: analysis_complete(patterns = ?, running_confidence = ?)
  [ ] EXACT VALUE VALIDATION — read Stage 4 artifact, extract s4_pattern_count = [V1] and
      running_confidence = [V2]. Signal must carry patterns >= 3 AND running_confidence = [V2].
      Violation = CHAIN INTEGRITY FAILURE. Record and halt.
  [ ] s5_status = RUN
  [ ] counter_hypothesis available (read Stage 1 artifact if s1 was RESUME-SKIP)
  [ ] full confidence chain available: prior, s2_delta, s3_delta, s4_delta

### BLOCK 1: CONFIDENCE CHAIN RESOLUTION

  confidence_prior:  [from Stage 1 artifact — re-read to confirm]
  s2_delta:          [from Stage 2 artifact]
  s3_delta:          [from Stage 3 artifact]
  s4_delta:          [from Stage 4 artifact]
  confidence_final:  [confidence_prior + s2_delta + s3_delta + s4_delta — capped 1-10]
  chain_equation:    "[prior] + [s2] + [s3] + [s4] = [final]"

### BLOCK 2: COUNTER-HYPOTHESIS RESOLUTION

  counter_hypothesis:  [from Stage 1 artifact]
  resolution_verdict:  [REFUTED / PARTIALLY REFUTED / OPEN RISK]
  resolution_evidence: [cite the stage artifact and section that resolves it]

If resolution_verdict = OPEN RISK: note the unresolved claim explicitly in key_risk below.

### SYNTHESIS

  hypothesis_verdict:        [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  displacement_conclusion:   [Does the evidence support replacing {status_quo_comparator}
                               with {topic}? Yes / No / Conditional — one sentence.]
  confidence_final:          [1-10 from chain equation in Block 1]
  evidence_summary:          [2-3 sentences: integrate S2 (N sources), S3 (N files),
                               S4 (N patterns), cite chain equation]
  key_risk:                  [primary risk remaining; include OPEN RISK item if applicable]

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Confirm write.

STAGE 5 EXIT SIGNAL: synthesis_complete(confidence_final={confidence_final})
  "STAGE 5 EXIT: synthesis_complete — confidence_final = [N]. Ready for /topic-story."

CAMPAIGN COMPLETE.
```

---

## V-02 — Open Risk Confidence Chain

**Axis**: open_risk_confidence_chain (single)
**Hypothesis**: When COUNTER-HYPOTHESIS RESOLUTION produces OPEN RISK, the current V-05
structure notes it informally in key_risk. The confidence reduction is implied but not
chained. Adding a named `cr_delta` field (-1 per OPEN RISK item) and incorporating it
as an explicit fifth term in the chain_equation ("[prior] + [s2] + [s3] + [s4] + [cr]
= [final]") makes the counter-hypothesis verdict a traceable contributor to the final
confidence, not a footnote. This tests whether the chain_equation — and therefore the
entire confidence derivation — becomes more defensible when ALL adjustments are visible
in one expression.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for a topic. Three named roles execute pre-stage.
Five evidence stages in strict sequence: prove-hypothesis -> prove-websearch ->
prove-intelligence -> prove-analysis -> prove-synthesize. Scout artifact named before
Stage 1. Resumable. Evidence stages enforce minimum counts. Confidence flows numerically
1-10 through a chain. Each stage fires a named EXIT SIGNAL with live payload. Stage 5
synthesizes in two named blocks: BLOCK 1 is CONFIDENCE CHAIN RESOLUTION (five-term
equation including counter-hypothesis delta), BLOCK 2 is COUNTER-HYPOTHESIS RESOLUTION.
Final output: evidence brief ready for /topic-story.

---

## CAMPAIGN OPEN

  topic:  {topic}
  date:   {date}

---

### PRE-STAGE: NAMED ROLE EXECUTION (Steps 1-3)

---

**ROLE 1 — SCOUT LOADER** (Step 1 of 3 — executes first)

  scout_artifact:  [{topic}-scout-record-{date}.md — or most recent scout signal for {topic}]
  scout_loaded:    [true / false]
  ROLE 1 STATUS:   [CONFIRMED] or [BLOCKED — record search path, halt campaign]

If scout_loaded = false: CAMPAIGN BLOCKED. Do not advance to ROLE 2.

---

**ROLE 2 — INERTIA ANALYST** (Step 2 of 3 — requires ROLE 1 CONFIRMED)

  status_quo_comparator:    [incumbent approach {topic} must displace]
  comparator_strength:      [one sentence: why the incumbent wins today]
  comparator_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]
  ROLE 2 STATUS:            [CONFIRMED]

---

**ROLE 3 — CAMPAIGN DIRECTOR** (Step 3 of 3 — requires ROLES 1 + 2 CONFIRMED)

CONFIDENCE CHAIN REGISTER (five-term):
  confidence_prior:  [to be set in Stage 1]
  s2_delta:          [to be set in Stage 2]
  s3_delta:          [to be set in Stage 3]
  s4_delta:          [to be set in Stage 4]
  cr_delta:          [to be set in Stage 5 Block 2 — counter-hypothesis resolution delta;
                       -1 per OPEN RISK item; 0 if REFUTED or PARTIALLY REFUTED]
  confidence_final:  [to be computed after all five terms known]

  Note: cr_delta is the fifth chain term. chain_equation in Block 1 cannot be written
  until Block 2 completes and cr_delta is set.

  CAMPAIGN STATUS:   OPEN

PRE-STAGE EXIT: campaign_open
  "PRE-STAGE COMPLETE — Roles 1, 2, 3 confirmed. Five-term chain initialized."
Do not begin Stage 1 until PRE-STAGE EXIT is printed.

---

## RESUME AUDIT

Glob for existing artifacts.

  Stage 1: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  Stage 2: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  Stage 3: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  Stage 4: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  Stage 5: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md

Mark each DONE or MISSING. Resume from first MISSING stage.

  s1_status: [RESUME-SKIP / RUN]   s2_status: [RESUME-SKIP / RUN]
  s3_status: [RESUME-SKIP / RUN]   s4_status: [RESUME-SKIP / RUN]
  s5_status: [RESUME-SKIP / RUN]

RESUME AUDIT EXIT: resume_audit_complete
  "RESUME AUDIT COMPLETE — resuming from Stage [N]."

---

## STAGE 1 — HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] EXIT SIGNAL received: resume_audit_complete
  [ ] s1_status = RUN (if RESUME-SKIP: carry confidence_prior from Stage 1 artifact)
  [ ] scout_artifact confirmed from ROLE 1

STAGE 1 BODY:
Load scout_artifact. Frame hypothesis.

  source_artifact:    [path — from ROLE 1]
  hypothesis:         [falsifiable claim derived from scout signals]
  counter_hypothesis: [strongest argument that {topic} fails to displace the incumbent —
                       grounded in ROLE 2 comparator_strength]

  confidence_prior:     [1-10 integer]
  confidence_reasoning: [one sentence: why this prior]

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked(confidence_prior={confidence_prior})
  "STAGE 1 EXIT: hypothesis_locked — confidence_prior = [N]. Stage 2 ready."

---

## STAGE 2 — WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] EXIT SIGNAL received: hypothesis_locked(confidence_prior = N)
  [ ] s2_status = RUN (if RESUME-SKIP: carry s2_delta and running_confidence from Stage 2 artifact)

STAGE 2 MINIMUM THRESHOLD: 5 external sources.

STAGE 2 BODY:

  # | SOURCE (URL or citation) | KEY FINDING (1 sentence) | STRENGTH | SUPPORTS? | CONFIDENCE IMPACT
  1 | [source]                 | [finding]                | S/M/W    | Y/N/P     | +N / -N / 0
  2 | [source]                 | [finding]                | S/M/W    | Y/N/P     | +N / -N / 0
  3 | [source]                 | [finding]                | S/M/W    | Y/N/P     | +N / -N / 0
  4 | [source]                 | [finding]                | S/M/W    | Y/N/P     | +N / -N / 0
  5 | [source]                 | [finding]                | S/M/W    | Y/N/P     | +N / -N / 0
  + | add if found             |                          |          |           |

  s2_evidence_count:   [N — verify >= 5]
  s2_delta:            [sum of confidence impact column]
  s2_support_tally:    [Y: N, N: M, Partial: P]
  s2_key_gap:          [what external evidence does not cover]
  running_confidence:  [confidence_prior + s2_delta — capped 1-10]

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete(count={s2_evidence_count}, running_confidence={running_confidence})
  "STAGE 2 EXIT: websearch_complete — count = [N], running_confidence = [N]. Stage 3 ready."

---

## STAGE 3 — INTELLIGENCE

STAGE 3 ENTRY CONDITIONS:
  [ ] EXIT SIGNAL received: websearch_complete(count >= 5, running_confidence = N)
  [ ] s3_status = RUN (if RESUME-SKIP: carry s3_delta and running_confidence from Stage 3 artifact)

STAGE 3 MINIMUM THRESHOLD: 3 internal sources.

STAGE 3 BODY:

  # | FILE PATH    | SECTION     | FINDING (1 sentence) | ALIGNS WITH WEB?    | CONFIDENCE IMPACT
  1 | [path]       | [section]   | [finding]            | Y / N / Contradicts | +N / -N / 0
  2 | [path]       | [section]   | [finding]            | Y / N / Contradicts | +N / -N / 0
  3 | [path]       | [section]   | [finding]            | Y / N / Contradicts | +N / -N / 0
  + | add rows     |             |                      |                     |

  s3_sources_found:    [N — verify >= 3]
  s3_delta:            [sum of confidence impact column]
  s3_alignment:        [ALIGNED / CONTRADICTS / MIXED]
  s3_key_gap:          [what internal sources do not address]
  running_confidence:  [prev running_confidence + s3_delta — capped 1-10]

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Confirm write.

STAGE 3 EXIT SIGNAL: intelligence_complete(count={s3_sources_found}, running_confidence={running_confidence})
  "STAGE 3 EXIT: intelligence_complete — count = [N], running_confidence = [N]. Stage 4 ready."

---

## STAGE 4 — ANALYSIS

STAGE 4 ENTRY CONDITIONS:
  [ ] EXIT SIGNAL received: intelligence_complete(count >= 3, running_confidence = N)
  [ ] s4_status = RUN (if RESUME-SKIP: carry s4_delta and running_confidence from Stage 4 artifact)

STAGE 4 MINIMUM THRESHOLD: 3 distinct patterns.

STAGE 4 BODY:

  # | PATTERN      | SOURCES (S2-# / S3-filepath) | CAUSAL?        | CONFIDENCE IMPACT
  1 | [pattern]    | [sources]                    | Yes/No/Unknown | +N / -N / 0
  2 | [pattern]    | [sources]                    | Yes/No/Unknown | +N / -N / 0
  3 | [pattern]    | [sources]                    | Yes/No/Unknown | +N / -N / 0
  + | add rows     |                              |                |

  s4_aggregate_displacement_verdict: [Yes / No / Inconclusive]
    ("Does the aggregate pattern support the displacement of {status_quo_comparator}
      by {topic}? [Yes / No / Inconclusive]")

  s4_pattern_count:    [N — verify >= 3]
  s4_delta:            [sum of confidence impact column]
  s4_primary_finding:  [dominant pattern, 1-2 sentences]
  s4_counter_evidence: [strongest evidence against hypothesis — cite artifact + section]
  running_confidence:  [prev running_confidence + s4_delta — capped 1-10]

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Confirm write.

STAGE 4 EXIT SIGNAL: analysis_complete(patterns={s4_pattern_count}, running_confidence={running_confidence})
  "STAGE 4 EXIT: analysis_complete — patterns = [N], running_confidence = [N]. Stage 5 ready."

---

## STAGE 5 — SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] EXIT SIGNAL received: analysis_complete(patterns >= 3, running_confidence = N)
  [ ] s5_status = RUN
  [ ] counter_hypothesis available (read Stage 1 artifact if s1 was RESUME-SKIP)
  [ ] full confidence chain available: prior, s2_delta, s3_delta, s4_delta

ORDER CONSTRAINT: BLOCK 2 executes BEFORE BLOCK 1. cr_delta is set in Block 2 and
required for Block 1's chain_equation. Do not write chain_equation until cr_delta is known.

### BLOCK 2: COUNTER-HYPOTHESIS RESOLUTION

Execute first to determine cr_delta.

  counter_hypothesis:  [from Stage 1 artifact]
  resolution_verdict:  [REFUTED / PARTIALLY REFUTED / OPEN RISK]
  resolution_evidence: [cite the stage artifact and section that resolves it]
  open_risk_count:     [number of OPEN RISK items — 0 if REFUTED or PARTIALLY REFUTED]
  cr_delta:            [-(open_risk_count) — e.g., 0 if REFUTED, -1 if one OPEN RISK item]

### BLOCK 1: CONFIDENCE CHAIN RESOLUTION

Executed after Block 2 so cr_delta is available.

  confidence_prior:  [from Stage 1]
  s2_delta:          [from Stage 2]
  s3_delta:          [from Stage 3]
  s4_delta:          [from Stage 4]
  cr_delta:          [from Block 2 — counter-hypothesis resolution delta]
  confidence_final:  [confidence_prior + s2_delta + s3_delta + s4_delta + cr_delta — capped 1-10]
  chain_equation:    "[prior] + [s2] + [s3] + [s4] + [cr] = [final]"

### SYNTHESIS

  hypothesis_verdict:        [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  displacement_conclusion:   [Does the evidence support replacing {status_quo_comparator}
                               with {topic}? Yes / No / Conditional — one sentence.]
  confidence_final:          [1-10 from chain equation]
  evidence_summary:          [2-3 sentences: integrate S2 (N sources), S3 (N files),
                               S4 (N patterns), cite chain equation with all five terms]
  key_risk:                  [primary risk remaining; note each OPEN RISK item from Block 2]

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Confirm write.

STAGE 5 EXIT SIGNAL: synthesis_complete(confidence_final={confidence_final})
  "STAGE 5 EXIT: synthesis_complete — confidence_final = [N]. Ready for /topic-story."

CAMPAIGN COMPLETE.
```

---

## V-03 — Displacement Loop Integrity Check

**Axis**: displacement_loop_integrity_check (single)
**Hypothesis**: Stage 5 currently has two named blocks (CONFIDENCE CHAIN RESOLUTION ->
COUNTER-HYPOTHESIS RESOLUTION) that satisfy C-14. The three-point displacement loop
(ROLE 2 anchor -> Stage 4 aggregate verdict -> Stage 5 displacement_conclusion) is
present (C-10) but the consistency relationship between s4_aggregate_displacement_verdict
and displacement_conclusion is never formally checked — they could contradict silently.
Adding a third named block DISPLACEMENT INTEGRITY CHECK that explicitly cross-references
the two fields before synthesis closes produces a triple-block Stage 5 structure and
makes the displacement loop tamper-evident in the same way C-13 makes the confidence
chain tamper-evident.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for a topic. Three named roles execute pre-stage.
Five evidence stages in strict sequence: prove-hypothesis -> prove-websearch ->
prove-intelligence -> prove-analysis -> prove-synthesize. Scout artifact named before
Stage 1. Resumable. Evidence stages enforce minimum counts. Confidence flows numerically
1-10 through a chain. Each stage fires a named EXIT SIGNAL with live payload. Stage 5
synthesizes in THREE named blocks: BLOCK 1 CONFIDENCE CHAIN RESOLUTION (chain_equation),
BLOCK 2 COUNTER-HYPOTHESIS RESOLUTION (verdict vocabulary), BLOCK 3 DISPLACEMENT
INTEGRITY CHECK (cross-references Stage 4 aggregate verdict against displacement_conclusion;
inconsistency = synthesis integrity error). Final output: evidence brief for /topic-story.

---

## CAMPAIGN OPEN

  topic:  {topic}
  date:   {date}

---

### PRE-STAGE: NAMED ROLE EXECUTION (Steps 1-3)

---

**ROLE 1 — SCOUT LOADER** (Step 1 of 3 — executes first)

  scout_artifact:  [{topic}-scout-record-{date}.md — or most recent scout signal for {topic}]
  scout_loaded:    [true / false]
  ROLE 1 STATUS:   [CONFIRMED] or [BLOCKED — record search path, halt campaign]

If scout_loaded = false: CAMPAIGN BLOCKED. Do not advance to ROLE 2.

---

**ROLE 2 — INERTIA ANALYST** (Step 2 of 3 — requires ROLE 1 CONFIRMED)

  status_quo_comparator:    [incumbent approach {topic} must displace]
  comparator_strength:      [one sentence: why the incumbent wins today]
  comparator_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]
  ROLE 2 STATUS:            [CONFIRMED]

---

**ROLE 3 — CAMPAIGN DIRECTOR** (Step 3 of 3 — requires ROLES 1 + 2 CONFIRMED)

CONFIDENCE CHAIN REGISTER:
  confidence_prior:  [to be set in Stage 1]
  s2_delta:          [to be set in Stage 2]
  s3_delta:          [to be set in Stage 3]
  s4_delta:          [to be set in Stage 4]
  confidence_final:  [to be computed in Stage 5]

DISPLACEMENT ANCHOR (from ROLE 2 — referenced in Stage 5 Block 3):
  displacement_anchor: {status_quo_comparator} vs {topic}
  anchor_strength:     [comparator_strength from ROLE 2]

  CAMPAIGN STATUS:   OPEN

PRE-STAGE EXIT: campaign_open
  "PRE-STAGE COMPLETE — Roles 1, 2, 3 confirmed. Displacement anchor registered."
Do not begin Stage 1 until PRE-STAGE EXIT is printed.

---

## RESUME AUDIT

Glob for existing artifacts.

  Stage 1: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  Stage 2: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  Stage 3: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  Stage 4: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  Stage 5: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md

Mark each DONE or MISSING. Resume from first MISSING stage.

  s1_status: [RESUME-SKIP / RUN]   s2_status: [RESUME-SKIP / RUN]
  s3_status: [RESUME-SKIP / RUN]   s4_status: [RESUME-SKIP / RUN]
  s5_status: [RESUME-SKIP / RUN]

RESUME AUDIT EXIT: resume_audit_complete
  "RESUME AUDIT COMPLETE — resuming from Stage [N]."

---

## STAGE 1 — HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] EXIT SIGNAL received: resume_audit_complete
  [ ] s1_status = RUN (if RESUME-SKIP: carry confidence_prior from Stage 1 artifact)
  [ ] scout_artifact confirmed from ROLE 1

STAGE 1 BODY:

  source_artifact:    [path — from ROLE 1]
  hypothesis:         [falsifiable claim derived from scout signals]
  counter_hypothesis: [strongest argument that {topic} fails to displace the incumbent —
                       grounded in ROLE 2 comparator_strength]

  confidence_prior:     [1-10 integer]
  confidence_reasoning: [one sentence: why this prior]

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked(confidence_prior={confidence_prior})
  "STAGE 1 EXIT: hypothesis_locked — confidence_prior = [N]. Stage 2 ready."

---

## STAGE 2 — WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] EXIT SIGNAL received: hypothesis_locked(confidence_prior = N)
  [ ] s2_status = RUN (if RESUME-SKIP: carry s2_delta and running_confidence from Stage 2 artifact)

STAGE 2 MINIMUM THRESHOLD: 5 external sources.

STAGE 2 BODY:

  # | SOURCE (URL or citation) | KEY FINDING (1 sentence) | STRENGTH | SUPPORTS? | CONFIDENCE IMPACT
  1 | [source]                 | [finding]                | S/M/W    | Y/N/P     | +N / -N / 0
  2 | [source]                 | [finding]                | S/M/W    | Y/N/P     | +N / -N / 0
  3 | [source]                 | [finding]                | S/M/W    | Y/N/P     | +N / -N / 0
  4 | [source]                 | [finding]                | S/M/W    | Y/N/P     | +N / -N / 0
  5 | [source]                 | [finding]                | S/M/W    | Y/N/P     | +N / -N / 0
  + | add if found             |                          |          |           |

  s2_evidence_count:   [N — verify >= 5]
  s2_delta:            [sum of confidence impact column]
  s2_support_tally:    [Y: N, N: M, Partial: P]
  s2_key_gap:          [what external evidence does not cover]
  running_confidence:  [confidence_prior + s2_delta — capped 1-10]

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete(count={s2_evidence_count}, running_confidence={running_confidence})
  "STAGE 2 EXIT: websearch_complete — count = [N], running_confidence = [N]. Stage 3 ready."

---

## STAGE 3 — INTELLIGENCE

STAGE 3 ENTRY CONDITIONS:
  [ ] EXIT SIGNAL received: websearch_complete(count >= 5, running_confidence = N)
  [ ] s3_status = RUN (if RESUME-SKIP: carry s3_delta and running_confidence from Stage 3 artifact)

STAGE 3 MINIMUM THRESHOLD: 3 internal sources.

STAGE 3 BODY:

  # | FILE PATH    | SECTION     | FINDING (1 sentence) | ALIGNS WITH WEB?    | CONFIDENCE IMPACT
  1 | [path]       | [section]   | [finding]            | Y / N / Contradicts | +N / -N / 0
  2 | [path]       | [section]   | [finding]            | Y / N / Contradicts | +N / -N / 0
  3 | [path]       | [section]   | [finding]            | Y / N / Contradicts | +N / -N / 0
  + | add rows     |             |                      |                     |

  s3_sources_found:    [N — verify >= 3]
  s3_delta:            [sum of confidence impact column]
  s3_alignment:        [ALIGNED / CONTRADICTS / MIXED]
  s3_key_gap:          [what internal sources do not address]
  running_confidence:  [prev running_confidence + s3_delta — capped 1-10]

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Confirm write.

STAGE 3 EXIT SIGNAL: intelligence_complete(count={s3_sources_found}, running_confidence={running_confidence})
  "STAGE 3 EXIT: intelligence_complete — count = [N], running_confidence = [N]. Stage 4 ready."

---

## STAGE 4 — ANALYSIS

STAGE 4 ENTRY CONDITIONS:
  [ ] EXIT SIGNAL received: intelligence_complete(count >= 3, running_confidence = N)
  [ ] s4_status = RUN (if RESUME-SKIP: carry s4_delta and running_confidence from Stage 4 artifact)

STAGE 4 MINIMUM THRESHOLD: 3 distinct patterns.

STAGE 4 BODY:

  # | PATTERN      | SOURCES (S2-# / S3-filepath) | CAUSAL?        | CONFIDENCE IMPACT
  1 | [pattern]    | [sources]                    | Yes/No/Unknown | +N / -N / 0
  2 | [pattern]    | [sources]                    | Yes/No/Unknown | +N / -N / 0
  3 | [pattern]    | [sources]                    | Yes/No/Unknown | +N / -N / 0
  + | add rows     |                              |                |

Aggregate displacement verdict:
  "Does the aggregate pattern support the displacement of {status_quo_comparator}
   by {topic}? [Yes / No / Inconclusive]"
  s4_aggregate_displacement_verdict: [Yes / No / Inconclusive]

  s4_pattern_count:    [N — verify >= 3]
  s4_delta:            [sum of confidence impact column]
  s4_primary_finding:  [dominant pattern, 1-2 sentences]
  s4_counter_evidence: [strongest evidence against hypothesis — cite artifact + section]
  running_confidence:  [prev running_confidence + s4_delta — capped 1-10]

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Confirm write.

STAGE 4 EXIT SIGNAL: analysis_complete(patterns={s4_pattern_count}, running_confidence={running_confidence})
  "STAGE 4 EXIT: analysis_complete — patterns = [N], running_confidence = [N]. Stage 5 ready."

---

## STAGE 5 — SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] EXIT SIGNAL received: analysis_complete(patterns >= 3, running_confidence = N)
  [ ] s5_status = RUN
  [ ] counter_hypothesis available (read Stage 1 artifact if s1 was RESUME-SKIP)
  [ ] full confidence chain: prior, s2_delta, s3_delta, s4_delta
  [ ] s4_aggregate_displacement_verdict available from Stage 4 artifact

Execute blocks in order: BLOCK 1 -> BLOCK 2 -> BLOCK 3 -> SYNTHESIS. Block 3 gates synthesis.

### BLOCK 1: CONFIDENCE CHAIN RESOLUTION

  confidence_prior:  [from Stage 1]
  s2_delta:          [from Stage 2]
  s3_delta:          [from Stage 3]
  s4_delta:          [from Stage 4]
  confidence_final:  [confidence_prior + s2_delta + s3_delta + s4_delta — capped 1-10]
  chain_equation:    "[prior] + [s2] + [s3] + [s4] = [final]"

### BLOCK 2: COUNTER-HYPOTHESIS RESOLUTION

  counter_hypothesis:  [from Stage 1 artifact]
  resolution_verdict:  [REFUTED / PARTIALLY REFUTED / OPEN RISK]
  resolution_evidence: [cite the stage artifact and section that resolves it]

If resolution_verdict = OPEN RISK: note in key_risk below.

### BLOCK 3: DISPLACEMENT INTEGRITY CHECK

Cross-reference Stage 4 aggregate verdict against proposed displacement_conclusion.
Inconsistency must be named before synthesis closes.

  s4_aggregate_displacement_verdict:   [read from Stage 4 artifact — Yes / No / Inconclusive]
  proposed_displacement_conclusion:    [draft: does the evidence support replacing
                                         {status_quo_comparator} with {topic}?
                                         Yes / No / Conditional]
  consistency_check:                   [CONSISTENT — s4 verdict and proposed conclusion align]
                                       [INCONSISTENT — state the discrepancy and resolve it]
  displacement_conclusion:             [final value after consistency check; must be consistent
                                         with s4_aggregate_displacement_verdict or discrepancy
                                         explicitly explained]

If INCONSISTENT: do not close synthesis until discrepancy is explained.

### SYNTHESIS

  hypothesis_verdict:      [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  displacement_conclusion: [from Block 3]
  confidence_final:        [1-10 from Block 1]
  evidence_summary:        [2-3 sentences: integrate S2 (N sources), S3 (N files),
                             S4 (N patterns), cite chain equation]
  key_risk:                [primary risk; include OPEN RISK from Block 2 if applicable]

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Confirm write.

STAGE 5 EXIT SIGNAL: synthesis_complete(confidence_final={confidence_final})
  "STAGE 5 EXIT: synthesis_complete — confidence_final = [N]. Ready for /topic-story."

CAMPAIGN COMPLETE.
```

---

## V-04 — Exact Value Lockdown + Open Risk Confidence Chain

**Axes**: exact_value_lockdown + open_risk_confidence_chain (combined)
**Hypothesis**: V-01 (exact-value payload validation at every entry condition) and V-02
(cr_delta as fifth chain term from counter-hypothesis resolution) address orthogonal
weak spots in the confidence derivation: V-01 prevents silent payload corruption between
stages, V-02 prevents silent confidence inflation from unresolved counter-hypotheses.
Together they form a closed-loop confidence audit: every value entering the chain is
verified on arrival, and every downward adjustment to confidence is named and visible
in the chain_equation.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for a topic. Three named roles execute pre-stage.
Five evidence stages in strict sequence: prove-hypothesis -> prove-websearch ->
prove-intelligence -> prove-analysis -> prove-synthesize. Scout artifact named before
Stage 1. Resumable. Evidence stages enforce minimum counts. Confidence flows numerically
1-10 through a VERIFIED chain: each entry condition reads the prior artifact, extracts
the concrete value, and validates received payload against it (mismatch = CHAIN INTEGRITY
FAILURE). Stage 5 synthesizes in two named blocks: BLOCK 2 COUNTER-HYPOTHESIS RESOLUTION
executes first to determine cr_delta (-1 per OPEN RISK item), then BLOCK 1 CONFIDENCE
CHAIN RESOLUTION writes the five-term chain_equation including cr_delta. Final output:
evidence brief for /topic-story.

---

## CAMPAIGN OPEN

  topic:  {topic}
  date:   {date}

---

### PRE-STAGE: NAMED ROLE EXECUTION (Steps 1-3)

---

**ROLE 1 — SCOUT LOADER** (Step 1 of 3)

  scout_artifact:  [{topic}-scout-record-{date}.md — or most recent scout signal for {topic}]
  scout_loaded:    [true / false]
  ROLE 1 STATUS:   [CONFIRMED] or [BLOCKED — halt campaign]

If scout_loaded = false: CAMPAIGN BLOCKED. Do not advance to ROLE 2.

---

**ROLE 2 — INERTIA ANALYST** (Step 2 of 3 — requires ROLE 1 CONFIRMED)

  status_quo_comparator:    [incumbent approach {topic} must displace]
  comparator_strength:      [one sentence: why the incumbent wins today]
  comparator_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]
  ROLE 2 STATUS:            [CONFIRMED]

---

**ROLE 3 — CAMPAIGN DIRECTOR** (Step 3 of 3 — requires ROLES 1 + 2 CONFIRMED)

CONFIDENCE CHAIN REGISTER (five-term — cr_delta populated in Stage 5 Block 2):
  confidence_prior:  [Stage 1]
  s2_delta:          [Stage 2]
  s3_delta:          [Stage 3]
  s4_delta:          [Stage 4]
  cr_delta:          [Stage 5 Block 2 — counter-hypothesis delta; -1 per OPEN RISK; 0 otherwise]
  confidence_final:  [all five terms summed — capped 1-10]

  CAMPAIGN STATUS:   OPEN

PRE-STAGE EXIT: campaign_open
  "PRE-STAGE COMPLETE — Roles 1, 2, 3 confirmed. Five-term chain initialized."

---

## RESUME AUDIT

  Stage 1: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  Stage 2: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  Stage 3: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  Stage 4: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  Stage 5: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md

  s1_status: [RESUME-SKIP / RUN]   s2_status: [RESUME-SKIP / RUN]
  s3_status: [RESUME-SKIP / RUN]   s4_status: [RESUME-SKIP / RUN]
  s5_status: [RESUME-SKIP / RUN]

RESUME AUDIT EXIT: resume_audit_complete

---

## STAGE 1 — HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] EXIT SIGNAL received: resume_audit_complete
  [ ] s1_status = RUN (if RESUME-SKIP: read confidence_prior from artifact as validated value)
  [ ] scout_artifact from ROLE 1

STAGE 1 BODY:

  source_artifact:      [from ROLE 1]
  hypothesis:           [falsifiable claim from scout signals]
  counter_hypothesis:   [incumbent's best defense — grounded in ROLE 2 comparator_strength]
  confidence_prior:     [1-10]
  confidence_reasoning: [one sentence]

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked(confidence_prior={confidence_prior})
  "STAGE 1 EXIT: hypothesis_locked — confidence_prior = [N].
   Stage 2 must read this value from artifact and validate."

---

## STAGE 2 — WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] EXIT SIGNAL received: hypothesis_locked(confidence_prior = ?)
  [ ] EXACT VALUE VALIDATION — read Stage 1 artifact, extract confidence_prior = [V].
      Signal must carry [V]. If signal carries a different value: CHAIN INTEGRITY FAILURE —
      record received vs expected, halt campaign.
  [ ] s2_status = RUN (if RESUME-SKIP: read s2_delta and running_confidence from artifact)

STAGE 2 MINIMUM THRESHOLD: 5 external sources.

  # | SOURCE | KEY FINDING | STRENGTH | SUPPORTS? | CONFIDENCE IMPACT
  1 | [src]  | [finding]   | S/M/W    | Y/N/P     | +N / -N / 0
  2 | [src]  | [finding]   | S/M/W    | Y/N/P     | +N / -N / 0
  3 | [src]  | [finding]   | S/M/W    | Y/N/P     | +N / -N / 0
  4 | [src]  | [finding]   | S/M/W    | Y/N/P     | +N / -N / 0
  5 | [src]  | [finding]   | S/M/W    | Y/N/P     | +N / -N / 0
  + | add    |             |          |           |

  s2_evidence_count:  [N — verify >= 5]
  s2_delta:           [sum of confidence impact]
  s2_key_gap:         [what is not covered]
  running_confidence: [confidence_prior + s2_delta — capped 1-10]

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md. Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete(count={s2_evidence_count}, running_confidence={running_confidence})
  "STAGE 2 EXIT: websearch_complete — count = [N], running_confidence = [N].
   Stage 3 must read both values from artifact and validate."

---

## STAGE 3 — INTELLIGENCE

STAGE 3 ENTRY CONDITIONS:
  [ ] EXIT SIGNAL received: websearch_complete(count = ?, running_confidence = ?)
  [ ] EXACT VALUE VALIDATION — read Stage 2 artifact: s2_evidence_count = [V1],
      running_confidence = [V2]. Signal must carry count >= 5 AND running_confidence = [V2].
      count < 5: MINIMUM THRESHOLD FAILURE. running_confidence mismatch: CHAIN INTEGRITY FAILURE.
  [ ] s3_status = RUN

STAGE 3 MINIMUM THRESHOLD: 3 internal sources.

  # | FILE PATH | SECTION | FINDING | ALIGNS WITH WEB?    | CONFIDENCE IMPACT
  1 | [path]    | [sec]   | [find]  | Y / N / Contradicts | +N / -N / 0
  2 | [path]    | [sec]   | [find]  | Y / N / Contradicts | +N / -N / 0
  3 | [path]    | [sec]   | [find]  | Y / N / Contradicts | +N / -N / 0
  + | add       |         |         |                     |

  s3_sources_found:   [N — verify >= 3]
  s3_delta:           [sum of confidence impact]
  s3_alignment:       [ALIGNED / CONTRADICTS / MIXED]
  running_confidence: [prev + s3_delta — capped 1-10]

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md. Confirm write.

STAGE 3 EXIT SIGNAL: intelligence_complete(count={s3_sources_found}, running_confidence={running_confidence})
  "STAGE 3 EXIT: intelligence_complete — count = [N], running_confidence = [N].
   Stage 4 must read both values from artifact and validate."

---

## STAGE 4 — ANALYSIS

STAGE 4 ENTRY CONDITIONS:
  [ ] EXIT SIGNAL received: intelligence_complete(count = ?, running_confidence = ?)
  [ ] EXACT VALUE VALIDATION — read Stage 3 artifact: s3_sources_found = [V1],
      running_confidence = [V2]. Validate count >= 3 AND running_confidence = [V2].
      Violation = CHAIN INTEGRITY FAILURE.
  [ ] s4_status = RUN

STAGE 4 MINIMUM THRESHOLD: 3 distinct patterns.

  # | PATTERN   | SOURCES (S2-# / S3-path) | CAUSAL?        | CONFIDENCE IMPACT
  1 | [pattern] | [sources]                | Yes/No/Unknown | +N / -N / 0
  2 | [pattern] | [sources]                | Yes/No/Unknown | +N / -N / 0
  3 | [pattern] | [sources]                | Yes/No/Unknown | +N / -N / 0
  + | add       |                          |                |

  s4_aggregate_displacement_verdict: [Yes / No / Inconclusive]
    ("Does the aggregate pattern support displacement of {status_quo_comparator} by {topic}?")

  s4_pattern_count:    [N — verify >= 3]
  s4_delta:            [sum of confidence impact]
  s4_primary_finding:  [dominant pattern, 1-2 sentences]
  s4_counter_evidence: [strongest counter-evidence with citation]
  running_confidence:  [prev + s4_delta — capped 1-10]

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md. Confirm write.

STAGE 4 EXIT SIGNAL: analysis_complete(patterns={s4_pattern_count}, running_confidence={running_confidence})
  "STAGE 4 EXIT: analysis_complete — patterns = [N], running_confidence = [N].
   Stage 5 must read both values from artifact and validate."

---

## STAGE 5 — SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] EXIT SIGNAL received: analysis_complete(patterns = ?, running_confidence = ?)
  [ ] EXACT VALUE VALIDATION — read Stage 4 artifact: s4_pattern_count = [V1],
      running_confidence = [V2]. Validate patterns >= 3 AND running_confidence = [V2].
      Violation = CHAIN INTEGRITY FAILURE.
  [ ] s5_status = RUN
  [ ] counter_hypothesis from Stage 1 artifact
  [ ] full chain: prior, s2_delta, s3_delta, s4_delta

ORDER: BLOCK 2 executes before BLOCK 1 (cr_delta needed for chain_equation).

### BLOCK 2: COUNTER-HYPOTHESIS RESOLUTION

  counter_hypothesis:  [from Stage 1 artifact]
  resolution_verdict:  [REFUTED / PARTIALLY REFUTED / OPEN RISK]
  resolution_evidence: [cite stage artifact + section]
  open_risk_count:     [count of OPEN RISK items — 0 if REFUTED or PARTIALLY REFUTED]
  cr_delta:            [-(open_risk_count)]

### BLOCK 1: CONFIDENCE CHAIN RESOLUTION

  confidence_prior:  [Stage 1]
  s2_delta:          [Stage 2]
  s3_delta:          [Stage 3]
  s4_delta:          [Stage 4]
  cr_delta:          [from Block 2]
  confidence_final:  [sum of all five terms — capped 1-10]
  chain_equation:    "[prior] + [s2] + [s3] + [s4] + [cr] = [final]"

### SYNTHESIS

  hypothesis_verdict:        [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  displacement_conclusion:   [Does evidence support replacing {status_quo_comparator}
                               with {topic}? Yes / No / Conditional]
  confidence_final:          [from Block 1]
  evidence_summary:          [2-3 sentences: integrate S2 (N sources), S3 (N files),
                               S4 (N patterns); cite five-term chain equation]
  key_risk:                  [primary risk; list each OPEN RISK item from Block 2]

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md. Confirm write.

STAGE 5 EXIT SIGNAL: synthesis_complete(confidence_final={confidence_final})
  "STAGE 5 EXIT: synthesis_complete — confidence_final = [N]. Ready for /topic-story."

CAMPAIGN COMPLETE.
```

---

## V-05 — All Three Axes + Full Structural Stack

**Axes**: exact_value_lockdown + open_risk_confidence_chain + displacement_loop_integrity_check
**Hypothesis**: All three new R17 axes address different integrity gaps in the R16 champion:
V-01 seals payload corruption between stages, V-02 names counter-hypothesis resolution as
a confidence chain contributor, V-03 cross-validates the Stage 4 displacement verdict
against Stage 5 displacement_conclusion before synthesis closes. Together on top of the
full R16 V-05 structural stack (three-role pre-stage, displacement loop, compound exit
signals, count-gated thresholds, resume audit), this variation should satisfy all six
aspirational criteria (C-09 through C-14) while also probing whether two new excellence
patterns emerge: tamper-resistant chain (V-01) and triple-block Stage 5 (V-03).

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for a topic. Three named roles execute pre-stage.
Five evidence stages in strict sequence: prove-hypothesis -> prove-websearch ->
prove-intelligence -> prove-analysis -> prove-synthesize. Scout artifact named before
Stage 1. Resumable: pre-run audit marks completed stages RESUME-SKIP. Evidence stages
enforce minimum counts. Confidence flows numerically 1-10 through a VERIFIED five-term
chain: each entry condition reads the prior artifact, extracts the concrete value, and
validates received payload (mismatch = CHAIN INTEGRITY FAILURE). Stage 5 synthesizes in
THREE named blocks in order: BLOCK 2 COUNTER-HYPOTHESIS RESOLUTION (sets cr_delta: -1
per OPEN RISK item), BLOCK 1 CONFIDENCE CHAIN RESOLUTION (five-term chain_equation
including cr_delta), BLOCK 3 DISPLACEMENT INTEGRITY CHECK (cross-validates Stage 4
aggregate displacement verdict vs displacement_conclusion before synthesis closes;
inconsistency = synthesis integrity error). Final output: evidence brief for /topic-story.

---

## CAMPAIGN OPEN

  topic:  {topic}
  date:   {date}

---

### PRE-STAGE: NAMED ROLE EXECUTION (Steps 1-3)

All three roles execute before Stage 1. Each role requires the prior to confirm.

---

**ROLE 1 — SCOUT LOADER** (Step 1 of 3 — executes first)

  scout_artifact:  [{topic}-scout-record-{date}.md — or most recent scout signal for {topic}]
  scout_loaded:    [true / false]
  ROLE 1 STATUS:   [CONFIRMED] or [BLOCKED — record search path, halt campaign]

If scout_loaded = false: CAMPAIGN BLOCKED. Do not advance to ROLE 2.

---

**ROLE 2 — INERTIA ANALYST** (Step 2 of 3 — requires ROLE 1 CONFIRMED)

Name the incumbent and decompose its position. Grounds counter_hypothesis, displacement
framing, and Stage 5 Block 3.

  status_quo_comparator:    [incumbent approach {topic} must displace]
  comparator_strength:      [one sentence: why the incumbent wins today]
  comparator_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]
  ROLE 2 STATUS:            [CONFIRMED]

---

**ROLE 3 — CAMPAIGN DIRECTOR** (Step 3 of 3 — requires ROLES 1 + 2 CONFIRMED)

Initialize five-term confidence chain and displacement anchor.

CONFIDENCE CHAIN REGISTER (five terms — cr_delta populated in Stage 5 Block 2):
  confidence_prior:  [Stage 1]
  s2_delta:          [Stage 2]
  s3_delta:          [Stage 3]
  s4_delta:          [Stage 4]
  cr_delta:          [Stage 5 Block 2 — -1 per OPEN RISK; 0 if REFUTED or PARTIALLY REFUTED]
  confidence_final:  [all five terms — capped 1-10]

DISPLACEMENT ANCHOR (from ROLE 2 — referenced in Stage 5 Block 3):
  displacement_anchor: {status_quo_comparator} to be displaced by {topic}

  role_1_confirmed:  true
  role_2_confirmed:  true
  chain_initialized: true
  CAMPAIGN STATUS:   OPEN

PRE-STAGE EXIT: campaign_open
  "PRE-STAGE COMPLETE — Roles 1, 2, 3 confirmed. Five-term chain and displacement anchor
   initialized. Advancing to Resume Audit."
Do not begin Resume Audit until PRE-STAGE EXIT is printed.

---

## RESUME AUDIT

Glob for existing artifacts.

  Stage 1: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  Stage 2: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  Stage 3: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  Stage 4: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  Stage 5: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md

Mark each DONE or MISSING. Resume from first MISSING stage. For RESUME-SKIP stages:
read the artifact and carry the relevant chain values as validated inputs for the next
running stage's entry conditions.

  s1_status: [RESUME-SKIP / RUN]   s2_status: [RESUME-SKIP / RUN]
  s3_status: [RESUME-SKIP / RUN]   s4_status: [RESUME-SKIP / RUN]
  s5_status: [RESUME-SKIP / RUN]

RESUME AUDIT EXIT: resume_audit_complete
  "RESUME AUDIT COMPLETE — resuming from Stage [N]. Advancing."

---

## STAGE 1 — HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] EXIT SIGNAL received: resume_audit_complete
  [ ] s1_status = RUN (if RESUME-SKIP: read confidence_prior from artifact — this is the
      VALIDATED value to use for Stage 2 entry)
  [ ] scout_artifact confirmed from ROLE 1

STAGE 1 BODY:
Load scout_artifact. Read its signals. Frame hypothesis grounded in those signals.

  source_artifact:    [path — from ROLE 1, not re-inferred]
  hypothesis:         [falsifiable claim derived from scout signals]
  counter_hypothesis: [strongest argument that {topic} fails to displace the incumbent —
                       grounded in ROLE 2 comparator_strength]

CONFIDENCE PRIOR:
  confidence_prior:     [1-10 integer — prior before gathering evidence]
  confidence_reasoning: [one sentence: why this prior, based on scout signals]

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked(confidence_prior={confidence_prior})
  "STAGE 1 EXIT: hypothesis_locked — confidence_prior = [N].
   Stage 2 entry conditions must read this value from the artifact and validate."

---

## STAGE 2 — WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] EXIT SIGNAL received: hypothesis_locked(confidence_prior = ?)
  [ ] EXACT VALUE VALIDATION — read simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md,
      extract confidence_prior = [V]. Signal must carry [V]. If values differ:
      CHAIN INTEGRITY FAILURE — record "received [X], expected [V]", halt campaign.
      (If s1_status = RESUME-SKIP: V is already read from artifact in Resume Audit.)
  [ ] s2_status = RUN (if RESUME-SKIP: read s2_delta and running_confidence from artifact)

STAGE 2 MINIMUM THRESHOLD: 5 external sources. Do not fire exit until count >= 5.

STAGE 2 BODY:
Gather external sources. Apply displacement check and confidence impact per row.

  # | SOURCE (URL or citation) | KEY FINDING (1 sentence) | STRENGTH | SUPPORTS? | CONFIDENCE IMPACT
  1 | [source]                 | [finding]                | S/M/W    | Y/N/P     | +N / -N / 0
  2 | [source]                 | [finding]                | S/M/W    | Y/N/P     | +N / -N / 0
  3 | [source]                 | [finding]                | S/M/W    | Y/N/P     | +N / -N / 0
  4 | [source]                 | [finding]                | S/M/W    | Y/N/P     | +N / -N / 0
  5 | [source]                 | [finding]                | S/M/W    | Y/N/P     | +N / -N / 0
  + | add if found             |                          |          |           |

  s2_evidence_count:   [N — verify >= 5]
  s2_delta:            [sum of confidence impact column]
  s2_support_tally:    [Y: N, N: M, Partial: P]
  s2_key_gap:          [what external evidence does not cover]
  running_confidence:  [confidence_prior + s2_delta — capped 1-10]

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete(count={s2_evidence_count}, running_confidence={running_confidence})
  "STAGE 2 EXIT: websearch_complete — count = [N], running_confidence = [N].
   Stage 3 must read both values from artifact and validate."

---

## STAGE 3 — INTELLIGENCE

STAGE 3 ENTRY CONDITIONS:
  [ ] EXIT SIGNAL received: websearch_complete(count = ?, running_confidence = ?)
  [ ] EXACT VALUE VALIDATION — read Stage 2 artifact, extract s2_evidence_count = [V1]
      and running_confidence = [V2]. Validate: count >= 5 AND running_confidence = [V2].
      count < 5: MINIMUM THRESHOLD FAILURE. running_confidence mismatch: CHAIN INTEGRITY
      FAILURE. Record and halt on either violation.
  [ ] s3_status = RUN (if RESUME-SKIP: read s3_delta and running_confidence from artifact)

STAGE 3 MINIMUM THRESHOLD: 3 internal sources. Do not fire exit until count >= 3.

STAGE 3 BODY:
Search internal sources: codebase, specs, docs, prior signal artifacts.

  # | FILE PATH    | SECTION     | FINDING (1 sentence) | ALIGNS WITH WEB?    | CONFIDENCE IMPACT
  1 | [path]       | [section]   | [finding]            | Y / N / Contradicts | +N / -N / 0
  2 | [path]       | [section]   | [finding]            | Y / N / Contradicts | +N / -N / 0
  3 | [path]       | [section]   | [finding]            | Y / N / Contradicts | +N / -N / 0
  + | add rows     |             |                      |                     |

  s3_sources_found:    [N — verify >= 3]
  s3_delta:            [sum of confidence impact column]
  s3_alignment:        [ALIGNED / CONTRADICTS / MIXED — vs Stage 2]
  s3_key_gap:          [what internal sources do not address]
  running_confidence:  [prev running_confidence + s3_delta — capped 1-10]

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Confirm write.

STAGE 3 EXIT SIGNAL: intelligence_complete(count={s3_sources_found}, running_confidence={running_confidence})
  "STAGE 3 EXIT: intelligence_complete — count = [N], running_confidence = [N].
   Stage 4 must read both values from artifact and validate."

---

## STAGE 4 — ANALYSIS

STAGE 4 ENTRY CONDITIONS:
  [ ] EXIT SIGNAL received: intelligence_complete(count = ?, running_confidence = ?)
  [ ] EXACT VALUE VALIDATION — read Stage 3 artifact, extract s3_sources_found = [V1]
      and running_confidence = [V2]. Validate: count >= 3 AND running_confidence = [V2].
      Violation = CHAIN INTEGRITY FAILURE. Record and halt.
  [ ] s4_status = RUN (if RESUME-SKIP: read s4_delta and running_confidence from artifact)

STAGE 4 MINIMUM THRESHOLD: 3 distinct patterns. Do not fire exit until count >= 3.

STAGE 4 BODY:
Analyze patterns across Stages 2 + 3. Distinguish causation from correlation.

  # | PATTERN      | SOURCES (S2-# / S3-filepath) | CAUSAL?        | CONFIDENCE IMPACT
  1 | [pattern]    | [sources]                    | Yes/No/Unknown | +N / -N / 0
  2 | [pattern]    | [sources]                    | Yes/No/Unknown | +N / -N / 0
  3 | [pattern]    | [sources]                    | Yes/No/Unknown | +N / -N / 0
  + | add rows     |                              |                |

Aggregate displacement verdict:
  "Does the aggregate pattern support the displacement of {status_quo_comparator}
   by {topic}? [Yes / No / Inconclusive]"
  s4_aggregate_displacement_verdict: [Yes / No / Inconclusive]

  s4_pattern_count:    [N — verify >= 3]
  s4_delta:            [sum of confidence impact column]
  s4_primary_finding:  [dominant pattern, 1-2 sentences]
  s4_counter_evidence: [strongest evidence against hypothesis — cite artifact + section]
  running_confidence:  [prev running_confidence + s4_delta — capped 1-10]

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Confirm write.

STAGE 4 EXIT SIGNAL: analysis_complete(patterns={s4_pattern_count}, running_confidence={running_confidence})
  "STAGE 4 EXIT: analysis_complete — patterns = [N], running_confidence = [N].
   Stage 5 must read both values from artifact and validate."

---

## STAGE 5 — SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] EXIT SIGNAL received: analysis_complete(patterns = ?, running_confidence = ?)
  [ ] EXACT VALUE VALIDATION — read Stage 4 artifact, extract s4_pattern_count = [V1]
      and running_confidence = [V2]. Validate: patterns >= 3 AND running_confidence = [V2].
      Violation = CHAIN INTEGRITY FAILURE. Record and halt.
  [ ] s5_status = RUN
  [ ] counter_hypothesis available (read Stage 1 artifact if s1 was RESUME-SKIP)
  [ ] full confidence chain available: prior, s2_delta, s3_delta, s4_delta
  [ ] s4_aggregate_displacement_verdict available from Stage 4 artifact

EXECUTION ORDER (enforced): BLOCK 2 -> BLOCK 1 -> BLOCK 3 -> SYNTHESIS.
BLOCK 2 must complete before BLOCK 1 (cr_delta dependency).
BLOCK 3 must complete before SYNTHESIS (displacement_conclusion dependency).

### BLOCK 2: COUNTER-HYPOTHESIS RESOLUTION

Execute first. Sets cr_delta needed for BLOCK 1 chain_equation.

  counter_hypothesis:  [from Stage 1 artifact]
  resolution_verdict:  [REFUTED / PARTIALLY REFUTED / OPEN RISK]
  resolution_evidence: [cite stage artifact and section]
  open_risk_count:     [number of distinct OPEN RISK items — 0 if REFUTED or PARTIALLY REFUTED]
  cr_delta:            [-(open_risk_count) — e.g., 0 if REFUTED; -1 if one item unresolved]

### BLOCK 1: CONFIDENCE CHAIN RESOLUTION

Execute after BLOCK 2 so cr_delta is known.

  confidence_prior:  [from Stage 1 — re-read from artifact to confirm]
  s2_delta:          [from Stage 2 artifact]
  s3_delta:          [from Stage 3 artifact]
  s4_delta:          [from Stage 4 artifact]
  cr_delta:          [from BLOCK 2]
  confidence_final:  [sum of all five terms — capped 1-10]
  chain_equation:    "[prior] + [s2] + [s3] + [s4] + [cr] = [final]"

### BLOCK 3: DISPLACEMENT INTEGRITY CHECK

Execute after BLOCK 1. Cross-validate Stage 4 verdict vs proposed conclusion.
Do not write displacement_conclusion into SYNTHESIS until this block completes.

  s4_aggregate_displacement_verdict:  [re-read from Stage 4 artifact]
  proposed_displacement_conclusion:   [Does evidence support replacing
                                        {status_quo_comparator} with {topic}?
                                        Yes / No / Conditional]
  consistency_check:                  [CONSISTENT] or [INCONSISTENT — state discrepancy]
  displacement_conclusion:            [final — must align with s4 verdict or discrepancy
                                        explicitly explained before closing]

If INCONSISTENT: resolve before advancing to SYNTHESIS. Do not suppress the discrepancy.

### SYNTHESIS

  hypothesis_verdict:        [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  displacement_conclusion:   [from BLOCK 3]
  confidence_final:          [from BLOCK 1 chain equation]
  evidence_summary:          [2-3 sentences: integrate S2 (N sources), S3 (N files),
                               S4 (N patterns); cite five-term chain equation]
  key_risk:                  [primary risk; list each OPEN RISK item from BLOCK 2;
                               note any displacement inconsistency resolved in BLOCK 3]

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Confirm write.

STAGE 5 EXIT SIGNAL: synthesis_complete(confidence_final={confidence_final})
  "STAGE 5 EXIT: synthesis_complete — confidence_final = [N]. Ready for /topic-story."

CAMPAIGN COMPLETE.
```
