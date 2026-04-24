---
skill: quest-variate
skill_target: prove-topic
round: R3
date: 2026-03-16
rubric: prove-topic-rubric-v3-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [two_layer_enforcement, campaign_open_preregistration, per_stage_displacement_read]
  combined: [V-04 (two_layer + synthesis_declarations), V-05 (all_four_new)]
round_targets: >
  v3 adds C-14/C-15/C-16/C-17 from R2 excellence signals.
  C-14 targets bidirectional enforcement: canonical labels in SESSION INVARIANTS + verbatim echo inline.
  C-15 targets CAMPAIGN OPEN block before SESSION INVARIANTS to give invariant D a persistent named context.
  C-16 targets per-stage displacement synthesis fields that make INCUMBENT CHECK TABLE feel like evidence.
  C-17 targets SYNTHESIS DECLARATIONS prohibition header that pre-empts narrative burial of synthesis fields.
  All five R3 variations maintain all 5 essentials and all 3 recommended criteria from v2.
r2_scores:
  V-01: [tbd]
  V-02: [tbd]
  V-03: [tbd]
  V-04: [tbd]
  V-05: [tbd]
---

## V-01 -- Axis: Two-Layer Enforcement Architecture (C-14)

**Variation axis**: C-14 only -- two-layer enforcement (canonical failure labels in SESSION INVARIANTS block, verbatim echo at every inline checkpoint)

**Hypothesis**: Registering canonical failure labels once in the SESSION INVARIANTS block and requiring every inline checkpoint to echo the exact registered label creates bidirectional self-incrimination: any drift between the registered label and the inline echo is detectable from either direction simultaneously, making enforcement failures visible without requiring external audit.

---

```
You are running the prove-topic Signal skill.

Topic: {topic}
Date: {date}
Status-quo comparator: {status_quo_comparator}

---
CAMPAIGN OPEN

topic: {topic}
date: {date}
status_quo_comparator: {status_quo_comparator}
---
---
INCUMBENT ANCHOR

incumbent_name: [identify the primary incumbent or dominant current approach for {topic}]
incumbent_strength: [assess resistance level: LOW / MEDIUM / HIGH -- with one-sentence justification]
incumbent_vulnerability: [identify the most likely displacement vector]
---
---
SESSION INVARIANTS -- FAILURE LABEL REGISTRY

The following canonical failure labels are registered for this session.
Every inline enforcement checkpoint MUST echo the exact label from this registry.
Any checkpoint that uses a different label is itself a FORMAT ERROR.

  Invariant A -- Write sequencing
    Registered label: ORDER ERROR
    Rule: No artifact write may occur before its stage gate clears.

  Invariant B -- Null tally chain
    Registered label: INTEGRITY FAILURE
    Rule: The running null count carried forward into each stage must match
          the closing count from the prior stage. Cross-check at Stage 4 close.

  Invariant C -- Dual-lock
    Registered label: DUAL-LOCK ERROR
    Rule: Both hypothesis_verdict and confidence_composite must be locked
          before Stage 5 prose begins.

  Invariant D -- Incumbent displacement framing
    Registered label: FORMAT ERROR
    Rule: Every INCUMBENT CHECK TABLE question must use the exact template
          for its stage:
            Stage 2: "Does [evidence item] support the displacement of..."
            Stage 3: "Does [practitioner account] reveal a viable transition path from..."
            Stage 4: "Does [prototype result] make a credible case for displacing..."

  Invariant E -- Handoff schema completeness
    Registered label: FAIL
    Rule: HANDOFF TABLE must contain all 11 fields with [derived from: X]
          annotations. Any missing field triggers FAIL.
---
---
ROLE OWNERSHIP TABLE

| Role   | Owner                        | Runs    | Responsibility                                      |
|--------|------------------------------|---------|-----------------------------------------------------|
| ROLE C | incumbent threat analyst     | first   | Identify incumbent, assess strength + vulnerability |
| ROLE B | scout loader                 | second  | Execute gate_s_cleared check, load prior scout data |
| ROLE A | hypothesis architect         | third   | Lock hypothesis, drive stage sequence               |
---
---
CE VERDICT OWNERSHIP TABLE

| Stage | CE Verdict Owner         | Output                                      |
|-------|--------------------------|---------------------------------------------|
| S0    | ROLE B (scout loader)    | gate_open EXIT SIGNAL                       |
| S1    | ROLE A (hypothesis arch) | hypothesis_locked EXIT SIGNAL               |
| S2    | ROLE A                   | websearch_complete EXIT SIGNAL              |
| S3    | ROLE A                   | interview_complete EXIT SIGNAL              |
| S4    | ROLE A                   | prototype_complete EXIT SIGNAL              |
| S5    | ROLE A                   | synthesis_complete EXIT SIGNAL              |
---
---
PRE-COMMITTED HANDOFF SCHEMA TABLE

The following 11 fields MUST appear in the HANDOFF TABLE at Stage 5.
Any field absent triggers Invariant E: FAIL.
| Field                  | Source stage | Annotation requirement          |
|------------------------|--------------|---------------------------------|
| topic                  | S0           | [derived from: campaign open]   |
| hypothesis_text        | S1           | [derived from: S1 lock]         |
| hypothesis_verdict     | S5           | [derived from: dual-lock]       |
| confidence_composite   | S5           | [derived from: dual-lock]       |
| key_risk               | S5           | [derived from: synthesis body]  |
| null_tally_final       | S4           | [derived from: S4 cross-check]  |
| incumbent_name         | S0           | [derived from: incumbent anchor]|
| incumbent_verdict      | S5           | [derived from: synthesis body]  |
| counter_hypothesis     | S5           | [derived from: counter-hyp res] |
| counter_verdict        | S5           | [derived from: counter-hyp res] |
| next_signal            | S5           | [derived from: synthesis body]  |
---
---
EXIT SIGNALS (declared in order, pre-committed)

  Stage 0: gate_open
  Stage 1: hypothesis_locked
  Stage 2: websearch_complete
  Stage 3: interview_complete
  Stage 4: prototype_complete
  Stage 5: synthesis_complete
---
---
STAGE 0 -- GATE S

ROLE B executes gate_s_cleared check.

| Gate condition                        | Status        |
|---------------------------------------|---------------|
| Topic is scoped and bounded           | [PASS / FAIL] |
|---------------------------------------|---------------|
| Status-quo comparator is named        | [PASS / FAIL] |
| Prior scout data available or waived  | [PASS / FAIL] |
| Incumbent identified                  | [PASS / FAIL] |

All rows must be PASS to proceed.

Invariant A checkpoint -- ORDER ERROR: No Stage 1 artifact write may occur until this gate clears.

If all PASS:
  EXIT SIGNAL: gate_open
  ROLE B hands off to ROLE A.
---
---
STAGE 1 -- HYPOTHESIS

ROLE A locks the hypothesis.

hypothesis_text: [one declarative sentence stating what prove-topic will demonstrate]
null_hypothesis: [one declarative sentence stating what failure looks like]
counter_hypothesis: [one declarative sentence stating the strongest opposing claim]

Invariant A checkpoint -- ORDER ERROR: Artifact write below must not occur before gate_open is confirmed.

Write artifact: {topic}-hypothesis-{date}.md
  Contents: hypothesis_text, null_hypothesis, counter_hypothesis, date, topic

EXIT SIGNAL: hypothesis_locked
---
---
STAGE 2 -- WEB SEARCH

ROLE A drives web search evidence gathering.

Running null tally entering Stage 2: [carry forward from Stage 1 -- initial value is 0]

INCUMBENT CHECK TABLE -- Stage 2
Invariant D checkpoint -- FORMAT ERROR: Every question in this table must match the Stage 2 template exactly:
  "Does [evidence item] support the displacement of [incumbent_name] by {topic}?"

| # | Evidence item             | Invariant D question (Stage 2 template)                            | Answer       | Null? |
|---|---------------------------|----------------------------------------------|--------------|-------|
| 1 | [evidence item 1]         | Does [evidence item 1] support the displacement of [incumbent_name] by {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 2 | [evidence item 2]         | Does [evidence item 2] support the displacement of [incumbent_name] by {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 3 | [evidence item 3]         | Does [evidence item 3] support the displacement of [incumbent_name] by {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 4 | [evidence item 4]         | Does [evidence item 4] support the displacement of [incumbent_name] by {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 5 | [evidence item 5]         | Does [evidence item 5] support the displacement of [incumbent_name] by {topic}?  | [Y/N/PARTIAL]| [0/1] |

Running null tally closing Stage 2: [sum of Null? column]

Invariant B checkpoint -- INTEGRITY FAILURE: Closing tally must equal opening tally plus Stage 2 nulls.

Invariant A checkpoint -- ORDER ERROR: Artifact write below must not occur before websearch stage gate clears.

Write artifact: {topic}-websearch-{date}.md
  Contents: all 5 evidence items, INCUMBENT CHECK TABLE, running null tally, date, topic

EXIT SIGNAL: websearch_complete
---
---
STAGE 3 -- INTERVIEW

ROLE A drives practitioner interview simulation.

Running null tally entering Stage 3: [carry forward closing tally from Stage 2]

INCUMBENT CHECK TABLE -- Stage 3
Invariant D checkpoint -- FORMAT ERROR: Every question in this table must match the Stage 3 template exactly:
  "Does [practitioner account] reveal a viable transition path from [incumbent_name] to {topic}?"

| # | Practitioner account       | Invariant D question (Stage 3 template)                            | Answer       | Null? |
|---|----------------------------|----------------------------------------------|--------------|-------|
| 1 | [practitioner account 1]   | Does [practitioner account 1] reveal a viable transition path from [incumbent_name] to {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 2 | [practitioner account 2]   | Does [practitioner account 2] reveal a viable transition path from [incumbent_name] to {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 3 | [practitioner account 3]   | Does [practitioner account 3] reveal a viable transition path from [incumbent_name] to {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 4 | [practitioner account 4]   | Does [practitioner account 4] reveal a viable transition path from [incumbent_name] to {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 5 | [practitioner account 5]   | Does [practitioner account 5] reveal a viable transition path from [incumbent_name] to {topic}?  | [Y/N/PARTIAL]| [0/1] |

Running null tally closing Stage 3: [opening tally + Stage 3 nulls]

Invariant B checkpoint -- INTEGRITY FAILURE: Closing tally must equal opening tally plus Stage 3 nulls.

Invariant A checkpoint -- ORDER ERROR: Artifact write below must not occur before interview stage gate clears.

Write artifact: {topic}-interview-{date}.md
  Contents: all 5 practitioner accounts, INCUMBENT CHECK TABLE, running null tally, date, topic

EXIT SIGNAL: interview_complete
---
---
STAGE 4 -- PROTOTYPE

ROLE A drives prototype result evaluation.

Running null tally entering Stage 4: [carry forward closing tally from Stage 3]

INCUMBENT CHECK TABLE -- Stage 4
Invariant D checkpoint -- FORMAT ERROR: Every question in this table must match the Stage 4 template exactly:
  "Does [prototype result] make a credible case for displacing [incumbent_name] with {topic}?"

| # | Prototype result           | Invariant D question (Stage 4 template)                            | Answer       | Null? |
|---|----------------------------|----------------------------------------------|--------------|-------|
| 1 | [prototype result 1]       | Does [prototype result 1] make a credible case for displacing [incumbent_name] with {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 2 | [prototype result 2]       | Does [prototype result 2] make a credible case for displacing [incumbent_name] with {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 3 | [prototype result 3]       | Does [prototype result 3] make a credible case for displacing [incumbent_name] with {topic}?  | [Y/N/PARTIAL]| [0/1] |

Running null tally closing Stage 4 (FINAL): [opening tally + Stage 4 nulls]

NULL TALLY CROSS-CHECK:
  Running count entering Stage 3 was [M]. Final count is [N]. Match: [true/false]

Invariant B checkpoint -- INTEGRITY FAILURE: Match must be true. If false, halt and recount.

Invariant A checkpoint -- ORDER ERROR: Artifact write below must not occur before prototype stage gate clears.

Write artifact: {topic}-prototype-{date}.md
  Contents: all 3 prototype results, INCUMBENT CHECK TABLE, final null tally, cross-check, date, topic

EXIT SIGNAL: prototype_complete
---
---
STAGE 5 -- SYNTHESIS

COUNTER-HYPOTHESIS RESOLUTION TABLE

| Counter-hypothesis text              | Evidence against             | Verdict                                        |
|--------------------------------------|------------------------------|------------------------------------------------|
| [counter_hypothesis from Stage 1]    | [evidence items that refute] | [REFUTED / PARTIALLY REFUTED / OPEN RISK]      |

ATOMIC DUAL-LOCK

Invariant C checkpoint -- DUAL-LOCK ERROR: Both values must be locked before any synthesis prose is written.

  hypothesis_verdict: [SUPPORTED / PARTIALLY SUPPORTED / REFUTED]
  confidence_composite: [LOW / MEDIUM / HIGH] -- [one-sentence rationale]

  DUAL-LOCK CONFIRMED: [yes / no -- if no, halt]

SYNTHESIS BODY

[Write synthesis prose here. Minimum 3 sentences. Must reference incumbent by name, address counter-hypothesis verdict, and state key_risk explicitly.]

  key_risk: [one sentence naming the primary remaining risk]
  incumbent_verdict: [DISPLACED / PARTIALLY DISPLACED / NOT DISPLACED] -- [one sentence]
  next_signal: [name the next Signal skill recommended]

HANDOFF TABLE

Invariant E checkpoint -- FAIL: All 11 fields must be present with [derived from: X] annotations.

| Field                | Value                                    | Annotation                      |
|----------------------|------------------------------------------|---------------------------------|
| topic                | {topic}                                  | [derived from: campaign open]   |
| hypothesis_text      | [value from S1]                          | [derived from: S1 lock]         |
| hypothesis_verdict   | [value from dual-lock]                   | [derived from: dual-lock]       |
| confidence_composite | [value from dual-lock]                   | [derived from: dual-lock]       |
| key_risk             | [value from synthesis body]              | [derived from: synthesis body]  |
| null_tally_final     | [value from S4 cross-check]              | [derived from: S4 cross-check]  |
| incumbent_name       | [value from incumbent anchor]            | [derived from: incumbent anchor]|
| incumbent_verdict    | [value from synthesis body]              | [derived from: synthesis body]  |
| counter_hypothesis   | [value from S1]                          | [derived from: counter-hyp res] |
| counter_verdict      | [value from counter-hyp resolution]      | [derived from: counter-hyp res] |
| next_signal          | [value from synthesis body]              | [derived from: synthesis body]  |


Invariant A checkpoint -- ORDER ERROR: Both artifact writes below must not occur before dual-lock is confirmed.

Write artifact: {topic}-synthesis-{date}.md
  Contents: counter-hypothesis resolution table, dual-lock values, synthesis body, date, topic

Write artifact: {topic}-handoff-{date}.md
  Contents: HANDOFF TABLE (all 11 fields with annotations), date, topic

EXIT SIGNAL: synthesis_complete
---
```

---

## V-02 -- Axis: CAMPAIGN OPEN Pre-Registration (C-15)

**Variation axis**: C-15 only -- CAMPAIGN OPEN block appears BEFORE SESSION INVARIANTS and explicitly declares `incumbent` and `incumbent_strength` so all Invariant D checks bind to a persistent named displacement context

**Hypothesis**: Declaring `incumbent` and `incumbent_strength` in CAMPAIGN OPEN before SESSION INVARIANTS are established forces Invariant D to bind to a persistent named entity rather than re-establishing context per stage, eliminating the risk of incumbent drift across stages and making the entire session's displacement framing traceable to a single declared anchor.

---

```
You are running the prove-topic Signal skill.

Topic: {topic}
Date: {date}
Status-quo comparator: {status_quo_comparator}

---
CAMPAIGN OPEN

topic: {topic}
date: {date}
status_quo_comparator: {status_quo_comparator}
incumbent: [full name of the primary incumbent or dominant current approach for {topic}]
incumbent_strength: [LOW / MEDIUM / HIGH: one-sentence quantified justification, e.g., "HIGH: 67% market share, $50K average switching cost"]

NOTE: All Invariant D checks in this session bind to the incumbent named above.
Do not re-establish or rename the incumbent within stage bodies.
---
---
INCUMBENT ANCHOR

incumbent_name: [same value as `incumbent` declared in CAMPAIGN OPEN above]
incumbent_vulnerability: [identify the most likely displacement vector]
---
---
SESSION INVARIANTS

  Invariant A -- Write sequencing:
    No artifact write may occur before its stage gate clears.

  Invariant B -- Null tally chain:
    The running null count carried forward into each stage must match
    the closing count from the prior stage. Cross-check at Stage 4 close.

  Invariant C -- Dual-lock:
    Both hypothesis_verdict and confidence_composite must be locked
    before Stage 5 prose begins.

  Invariant D -- Incumbent displacement framing (bound to CAMPAIGN OPEN incumbent):
    Every INCUMBENT CHECK TABLE question must use the exact template for its stage.
    The incumbent named in CAMPAIGN OPEN is the displacement target throughout.
      Stage 2: "Does [evidence item] support the displacement of [incumbent from CAMPAIGN OPEN] by {topic}?"
      Stage 3: "Does [practitioner account] reveal a viable transition path from [incumbent from CAMPAIGN OPEN] to {topic}?"
      Stage 4: "Does [prototype result] make a credible case for displacing [incumbent from CAMPAIGN OPEN] with {topic}?"

  Invariant E -- Handoff schema completeness:
    HANDOFF TABLE must contain all 11 fields with [derived from: X] annotations.
---
---
ROLE OWNERSHIP TABLE

| Role   | Owner                        | Runs    | Responsibility                                       |
|--------|------------------------------|---------|------------------------------------------------------|
| ROLE C | incumbent threat analyst     | first   | Confirm CAMPAIGN OPEN incumbent, assess vulnerability|
| ROLE B | scout loader                 | second  | Execute gate_s_cleared check, load prior scout data  |
| ROLE A | hypothesis architect         | third   | Lock hypothesis, drive stage sequence                |
---
---
CE VERDICT OWNERSHIP TABLE

| Stage | CE Verdict Owner         | Output                                      |
|-------|--------------------------|---------------------------------------------|
| S0    | ROLE B (scout loader)    | gate_open EXIT SIGNAL                       |
| S1    | ROLE A (hypothesis arch) | hypothesis_locked EXIT SIGNAL               |
| S2    | ROLE A                   | websearch_complete EXIT SIGNAL              |
| S3    | ROLE A                   | interview_complete EXIT SIGNAL              |
| S4    | ROLE A                   | prototype_complete EXIT SIGNAL              |
| S5    | ROLE A                   | synthesis_complete EXIT SIGNAL              |
---
---
PRE-COMMITTED HANDOFF SCHEMA TABLE

The following 11 fields MUST appear in the HANDOFF TABLE at Stage 5.
| Field                  | Source stage | Annotation requirement          |
|------------------------|--------------|---------------------------------|
| topic                  | S0           | [derived from: campaign open]   |
| hypothesis_text        | S1           | [derived from: S1 lock]         |
| hypothesis_verdict     | S5           | [derived from: dual-lock]       |
| confidence_composite   | S5           | [derived from: dual-lock]       |
| key_risk               | S5           | [derived from: synthesis body]  |
| null_tally_final       | S4           | [derived from: S4 cross-check]  |
| incumbent_name         | S0           | [derived from: campaign open]|
| incumbent_verdict      | S5           | [derived from: synthesis body]  |
| counter_hypothesis     | S5           | [derived from: counter-hyp res] |
| counter_verdict        | S5           | [derived from: counter-hyp res] |
| next_signal            | S5           | [derived from: synthesis body]  |
---
---
EXIT SIGNALS (declared in order, pre-committed)

  Stage 0: gate_open
  Stage 1: hypothesis_locked
  Stage 2: websearch_complete
  Stage 3: interview_complete
  Stage 4: prototype_complete
  Stage 5: synthesis_complete
---
---
STAGE 0 -- GATE S

ROLE B executes gate_s_cleared check.

| Gate condition                        | Status        |
|---------------------------------------|---------------|
| Topic is scoped and bounded                 | [PASS / FAIL] |
|---------------------------------------------|---------------|
| Status-quo comparator is named              | [PASS / FAIL] |
| Prior scout data available or waived        | [PASS / FAIL] |
| Incumbent confirmed (matches CAMPAIGN OPEN) | [PASS / FAIL] |

All rows must be PASS to proceed.

If all PASS:
  EXIT SIGNAL: gate_open
  ROLE B hands off to ROLE A.
---
---
STAGE 1 -- HYPOTHESIS

ROLE A locks the hypothesis.

hypothesis_text: [one declarative sentence stating what prove-topic will demonstrate]
null_hypothesis: [one declarative sentence stating what failure looks like]
counter_hypothesis: [one declarative sentence stating the strongest opposing claim]

Write artifact: {topic}-hypothesis-{date}.md
  Contents: hypothesis_text, null_hypothesis, counter_hypothesis, date, topic

EXIT SIGNAL: hypothesis_locked
---
---
STAGE 2 -- WEB SEARCH

ROLE A drives web search evidence gathering.

Running null tally entering Stage 2: [carry forward from Stage 1 -- initial value is 0]

INCUMBENT CHECK TABLE -- Stage 2
Displacement context: incumbent declared in CAMPAIGN OPEN -- do not re-establish.

| # | Evidence item             | Invariant D question (Stage 2 template -- incumbent from CAMPAIGN OPEN) | Answer       | Null? |
|---|---------------------------|----------------------------------------------|--------------|-------|
| 1 | [evidence item 1]         | Does [evidence item 1] support the displacement of [incumbent] by {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 2 | [evidence item 2]         | Does [evidence item 2] support the displacement of [incumbent] by {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 3 | [evidence item 3]         | Does [evidence item 3] support the displacement of [incumbent] by {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 4 | [evidence item 4]         | Does [evidence item 4] support the displacement of [incumbent] by {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 5 | [evidence item 5]         | Does [evidence item 5] support the displacement of [incumbent] by {topic}?  | [Y/N/PARTIAL]| [0/1] |

Running null tally closing Stage 2: [sum of Null? column]

Write artifact: {topic}-websearch-{date}.md
  Contents: all 5 evidence items, INCUMBENT CHECK TABLE, running null tally, date, topic

EXIT SIGNAL: websearch_complete
---
---
STAGE 3 -- INTERVIEW

ROLE A drives practitioner interview simulation.

Running null tally entering Stage 3: [carry forward closing tally from Stage 2]

INCUMBENT CHECK TABLE -- Stage 3
Displacement context: incumbent declared in CAMPAIGN OPEN -- do not re-establish.

| # | Practitioner account       | Invariant D question (Stage 3 template -- incumbent from CAMPAIGN OPEN) | Answer       | Null? |
|---|----------------------------|----------------------------------------------|--------------|-------|
| 1 | [practitioner account 1]   | Does [practitioner account 1] reveal a viable transition path from [incumbent] to {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 2 | [practitioner account 2]   | Does [practitioner account 2] reveal a viable transition path from [incumbent] to {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 3 | [practitioner account 3]   | Does [practitioner account 3] reveal a viable transition path from [incumbent] to {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 4 | [practitioner account 4]   | Does [practitioner account 4] reveal a viable transition path from [incumbent] to {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 5 | [practitioner account 5]   | Does [practitioner account 5] reveal a viable transition path from [incumbent] to {topic}?  | [Y/N/PARTIAL]| [0/1] |

Running null tally closing Stage 3: [opening tally + Stage 3 nulls]

Write artifact: {topic}-interview-{date}.md
  Contents: all 5 practitioner accounts, INCUMBENT CHECK TABLE, running null tally, date, topic

EXIT SIGNAL: interview_complete
---
---
STAGE 4 -- PROTOTYPE

ROLE A drives prototype result evaluation.

Running null tally entering Stage 4: [carry forward closing tally from Stage 3]

INCUMBENT CHECK TABLE -- Stage 4
Displacement context: incumbent declared in CAMPAIGN OPEN -- do not re-establish.

| # | Prototype result           | Invariant D question (Stage 4 template -- incumbent from CAMPAIGN OPEN) | Answer       | Null? |
|---|----------------------------|----------------------------------------------|--------------|-------|
| 1 | [prototype result 1]       | Does [prototype result 1] make a credible case for displacing [incumbent] with {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 2 | [prototype result 2]       | Does [prototype result 2] make a credible case for displacing [incumbent] with {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 3 | [prototype result 3]       | Does [prototype result 3] make a credible case for displacing [incumbent] with {topic}?  | [Y/N/PARTIAL]| [0/1] |

Running null tally closing Stage 4 (FINAL): [opening tally + Stage 4 nulls]

NULL TALLY CROSS-CHECK:
  Running count entering Stage 3 was [M]. Final count is [N]. Match: [true/false]

Write artifact: {topic}-prototype-{date}.md
  Contents: all 3 prototype results, INCUMBENT CHECK TABLE, final null tally, cross-check, date, topic

EXIT SIGNAL: prototype_complete
---
---
STAGE 5 -- SYNTHESIS

COUNTER-HYPOTHESIS RESOLUTION TABLE

| Counter-hypothesis text              | Evidence against             | Verdict                                        |
|--------------------------------------|------------------------------|------------------------------------------------|
| [counter_hypothesis from Stage 1]    | [evidence items that refute] | [REFUTED / PARTIALLY REFUTED / OPEN RISK]      |

ATOMIC DUAL-LOCK

  hypothesis_verdict: [SUPPORTED / PARTIALLY SUPPORTED / REFUTED]
  confidence_composite: [LOW / MEDIUM / HIGH] -- [one-sentence rationale]

  DUAL-LOCK CONFIRMED: [yes / no -- if no, halt]

SYNTHESIS BODY

[Write synthesis prose here. Minimum 3 sentences. Must reference incumbent by the name declared in CAMPAIGN OPEN, address counter-hypothesis verdict, and state key_risk explicitly.]

  key_risk: [one sentence naming the primary remaining risk]
  incumbent_verdict: [DISPLACED / PARTIALLY DISPLACED / NOT DISPLACED] -- [one sentence]
  next_signal: [name the next Signal skill recommended]

HANDOFF TABLE

| Field                | Value                                    | Annotation                      |
|----------------------|------------------------------------------|---------------------------------|
| topic                | {topic}                                  | [derived from: campaign open]   |
| hypothesis_text      | [value from S1]                          | [derived from: S1 lock]         |
| hypothesis_verdict   | [value from dual-lock]                   | [derived from: dual-lock]       |
| confidence_composite | [value from dual-lock]                   | [derived from: dual-lock]       |
| key_risk             | [value from synthesis body]              | [derived from: synthesis body]  |
| null_tally_final     | [value from S4 cross-check]              | [derived from: S4 cross-check]  |
| incumbent_name       | [value from campaign open]               | [derived from: campaign open]|
| incumbent_verdict    | [value from synthesis body]              | [derived from: synthesis body]  |
| counter_hypothesis   | [value from S1]                          | [derived from: counter-hyp res] |
| counter_verdict      | [value from counter-hyp resolution]      | [derived from: counter-hyp res] |
| next_signal          | [value from synthesis body]              | [derived from: synthesis body]  |


Write artifact: {topic}-synthesis-{date}.md
  Contents: counter-hypothesis resolution table, dual-lock values, synthesis body, date, topic

Write artifact: {topic}-handoff-{date}.md
  Contents: HANDOFF TABLE (all 11 fields with annotations), date, topic

EXIT SIGNAL: synthesis_complete
---
```

---

## V-03 -- Axis: Per-Stage Displacement Read Fields (C-16)

**Variation axis**: C-16 only -- each of Stages 2, 3, and 4 has a dedicated "Displacement read:" synthesis field appearing after the INCUMBENT CHECK TABLE rows, summarizing the stage's net displacement verdict

**Hypothesis**: Adding a "Displacement read:" field after each INCUMBENT CHECK TABLE transforms the table from a compliance checkbox into an active displacement test -- each stage is forced to commit to a directional verdict before advancing, making the cumulative displacement argument visible and auditable at each transition point rather than only at Stage 5 synthesis.

---

```
You are running the prove-topic Signal skill.

Topic: {topic}
Date: {date}
Status-quo comparator: {status_quo_comparator}

---
CAMPAIGN OPEN

topic: {topic}
date: {date}
status_quo_comparator: {status_quo_comparator}
---
---
INCUMBENT ANCHOR

incumbent_name: [identify the primary incumbent or dominant current approach for {topic}]
incumbent_strength: [assess resistance level: LOW / MEDIUM / HIGH -- with one-sentence justification]
incumbent_vulnerability: [identify the most likely displacement vector]
---
---
SESSION INVARIANTS

  Invariant A -- Write sequencing:
    No artifact write may occur before its stage gate clears.

  Invariant B -- Null tally chain:
    The running null count carried forward into each stage must match
    the closing count from the prior stage. Cross-check at Stage 4 close.

  Invariant C -- Dual-lock:
    Both hypothesis_verdict and confidence_composite must be locked
    before Stage 5 prose begins.

  Invariant D -- Incumbent displacement framing:
    Every INCUMBENT CHECK TABLE question must use the exact template for its stage:
      Stage 2: "Does [evidence item] support the displacement of..."
      Stage 3: "Does [practitioner account] reveal a viable transition path from..."
      Stage 4: "Does [prototype result] make a credible case for displacing..."

  Invariant E -- Handoff schema completeness:
    HANDOFF TABLE must contain all 11 fields with [derived from: X] annotations.
---
---
ROLE OWNERSHIP TABLE

| Role   | Owner                        | Runs    | Responsibility                                      |
|--------|------------------------------|---------|-----------------------------------------------------|
| ROLE C | incumbent threat analyst     | first   | Identify incumbent, assess strength + vulnerability |
| ROLE B | scout loader                 | second  | Execute gate_s_cleared check, load prior scout data |
| ROLE A | hypothesis architect         | third   | Lock hypothesis, drive stage sequence               |
---
---
CE VERDICT OWNERSHIP TABLE

| Stage | CE Verdict Owner         | Output                                      |
|-------|--------------------------|---------------------------------------------|
| S0    | ROLE B (scout loader)    | gate_open EXIT SIGNAL                       |
| S1    | ROLE A (hypothesis arch) | hypothesis_locked EXIT SIGNAL               |
| S2    | ROLE A                   | websearch_complete EXIT SIGNAL              |
| S3    | ROLE A                   | interview_complete EXIT SIGNAL              |
| S4    | ROLE A                   | prototype_complete EXIT SIGNAL              |
| S5    | ROLE A                   | synthesis_complete EXIT SIGNAL              |
---
---
PRE-COMMITTED HANDOFF SCHEMA TABLE

The following 11 fields MUST appear in the HANDOFF TABLE at Stage 5.
| Field                  | Source stage | Annotation requirement          |
|------------------------|--------------|---------------------------------|
| topic                  | S0           | [derived from: campaign open]   |
| hypothesis_text        | S1           | [derived from: S1 lock]         |
| hypothesis_verdict     | S5           | [derived from: dual-lock]       |
| confidence_composite   | S5           | [derived from: dual-lock]       |
| key_risk               | S5           | [derived from: synthesis body]  |
| null_tally_final       | S4           | [derived from: S4 cross-check]  |
| incumbent_name         | S0           | [derived from: incumbent anchor]|
| incumbent_verdict      | S5           | [derived from: synthesis body]  |
| counter_hypothesis     | S5           | [derived from: counter-hyp res] |
| counter_verdict        | S5           | [derived from: counter-hyp res] |
| next_signal            | S5           | [derived from: synthesis body]  |
---
---
EXIT SIGNALS (declared in order, pre-committed)

  Stage 0: gate_open
  Stage 1: hypothesis_locked
  Stage 2: websearch_complete
  Stage 3: interview_complete
  Stage 4: prototype_complete
  Stage 5: synthesis_complete
---
---
STAGE 0 -- GATE S

ROLE B executes gate_s_cleared check.

| Gate condition                        | Status        |
|---------------------------------------|---------------|
| Topic is scoped and bounded           | [PASS / FAIL] |
|---------------------------------------|---------------|
| Status-quo comparator is named        | [PASS / FAIL] |
| Prior scout data available or waived  | [PASS / FAIL] |
| Incumbent identified                  | [PASS / FAIL] |

All rows must be PASS to proceed.

If all PASS:
  EXIT SIGNAL: gate_open
  ROLE B hands off to ROLE A.
---
---
STAGE 1 -- HYPOTHESIS

ROLE A locks the hypothesis.

hypothesis_text: [one declarative sentence stating what prove-topic will demonstrate]
null_hypothesis: [one declarative sentence stating what failure looks like]
counter_hypothesis: [one declarative sentence stating the strongest opposing claim]

Write artifact: {topic}-hypothesis-{date}.md
  Contents: hypothesis_text, null_hypothesis, counter_hypothesis, date, topic

EXIT SIGNAL: hypothesis_locked
---
---
STAGE 2 -- WEB SEARCH

ROLE A drives web search evidence gathering.

Running null tally entering Stage 2: [carry forward from Stage 1 -- initial value is 0]

INCUMBENT CHECK TABLE -- Stage 2
| # | Evidence item             | Invariant D question (Stage 2 template)                            | Answer       | Null? |
|---|---------------------------|----------------------------------------------|--------------|-------|
| 1 | [evidence item 1]         | Does [evidence item 1] support the displacement of [incumbent_name] by {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 2 | [evidence item 2]         | Does [evidence item 2] support the displacement of [incumbent_name] by {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 3 | [evidence item 3]         | Does [evidence item 3] support the displacement of [incumbent_name] by {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 4 | [evidence item 4]         | Does [evidence item 4] support the displacement of [incumbent_name] by {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 5 | [evidence item 5]         | Does [evidence item 5] support the displacement of [incumbent_name] by {topic}?  | [Y/N/PARTIAL]| [0/1] |

Running null tally closing Stage 2: [sum of Null? column]

Displacement read: Stage 2 evidence NET [SUPPORTS / DOES NOT SUPPORT / IS INCONCLUSIVE ON] displacement of [incumbent_name] by {topic}. Primary supporting dimension: [dimension]. Primary open challenge: [dimension or "none identified"].

Write artifact: {topic}-websearch-{date}.md
  Contents: all 5 evidence items, INCUMBENT CHECK TABLE, running null tally, Displacement read, date, topic

EXIT SIGNAL: websearch_complete
---
---
STAGE 3 -- INTERVIEW

ROLE A drives practitioner interview simulation.

Running null tally entering Stage 3: [carry forward closing tally from Stage 2]

INCUMBENT CHECK TABLE -- Stage 3
| # | Practitioner account       | Invariant D question (Stage 3 template)                            | Answer       | Null? |
|---|----------------------------|----------------------------------------------|--------------|-------|
| 1 | [practitioner account 1]   | Does [practitioner account 1] reveal a viable transition path from [incumbent_name] to {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 2 | [practitioner account 2]   | Does [practitioner account 2] reveal a viable transition path from [incumbent_name] to {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 3 | [practitioner account 3]   | Does [practitioner account 3] reveal a viable transition path from [incumbent_name] to {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 4 | [practitioner account 4]   | Does [practitioner account 4] reveal a viable transition path from [incumbent_name] to {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 5 | [practitioner account 5]   | Does [practitioner account 5] reveal a viable transition path from [incumbent_name] to {topic}?  | [Y/N/PARTIAL]| [0/1] |

Running null tally closing Stage 3: [opening tally + Stage 3 nulls]

Displacement read: Stage 3 practitioner accounts NET [SUPPORT / DO NOT SUPPORT / ARE INCONCLUSIVE ON] viable transition away from [incumbent_name] toward {topic}. Transition confidence signal: [HIGH / MEDIUM / LOW]. Dominant blocker if any: [blocker or "none identified"].

Write artifact: {topic}-interview-{date}.md
  Contents: all 5 practitioner accounts, INCUMBENT CHECK TABLE, running null tally, Displacement read, date, topic

EXIT SIGNAL: interview_complete
---
---
STAGE 4 -- PROTOTYPE

ROLE A drives prototype result evaluation.

Running null tally entering Stage 4: [carry forward closing tally from Stage 3]

INCUMBENT CHECK TABLE -- Stage 4
| # | Prototype result           | Invariant D question (Stage 4 template)                            | Answer       | Null? |
|---|----------------------------|----------------------------------------------|--------------|-------|
| 1 | [prototype result 1]       | Does [prototype result 1] make a credible case for displacing [incumbent_name] with {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 2 | [prototype result 2]       | Does [prototype result 2] make a credible case for displacing [incumbent_name] with {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 3 | [prototype result 3]       | Does [prototype result 3] make a credible case for displacing [incumbent_name] with {topic}?  | [Y/N/PARTIAL]| [0/1] |

Running null tally closing Stage 4 (FINAL): [opening tally + Stage 4 nulls]

NULL TALLY CROSS-CHECK:
  Running count entering Stage 3 was [M]. Final count is [N]. Match: [true/false]

Displacement read: Stage 4 prototype results NET [MAKE / DO NOT MAKE / PARTIALLY MAKE] a credible displacement case against [incumbent_name]. Cumulative displacement signal across S2+S3+S4: [STRONG / MODERATE / WEAK / CONTRADICTORY]. Deciding factor: [factor].

Write artifact: {topic}-prototype-{date}.md
  Contents: all 3 prototype results, INCUMBENT CHECK TABLE, final null tally, cross-check, Displacement read, date, topic

EXIT SIGNAL: prototype_complete
---
---
STAGE 5 -- SYNTHESIS

COUNTER-HYPOTHESIS RESOLUTION TABLE

| Counter-hypothesis text              | Evidence against             | Verdict                                        |
|--------------------------------------|------------------------------|------------------------------------------------|
| [counter_hypothesis from Stage 1]    | [evidence items that refute] | [REFUTED / PARTIALLY REFUTED / OPEN RISK]      |

ATOMIC DUAL-LOCK

  hypothesis_verdict: [SUPPORTED / PARTIALLY SUPPORTED / REFUTED]
  confidence_composite: [LOW / MEDIUM / HIGH] -- [one-sentence rationale]

  DUAL-LOCK CONFIRMED: [yes / no -- if no, halt]

SYNTHESIS BODY

[Write synthesis prose here. Minimum 3 sentences. Must reference incumbent by name, address counter-hypothesis verdict, and state key_risk explicitly. May reference the per-stage Displacement reads from S2, S3, S4 to support the cumulative argument.]

  key_risk: [one sentence naming the primary remaining risk]
  incumbent_verdict: [DISPLACED / PARTIALLY DISPLACED / NOT DISPLACED] -- [one sentence]
  next_signal: [name the next Signal skill recommended]

HANDOFF TABLE

| Field                | Value                                    | Annotation                      |
|----------------------|------------------------------------------|---------------------------------|
| topic                | {topic}                                  | [derived from: campaign open]   |
| hypothesis_text      | [value from S1]                          | [derived from: S1 lock]         |
| hypothesis_verdict   | [value from dual-lock]                   | [derived from: dual-lock]       |
| confidence_composite | [value from dual-lock]                   | [derived from: dual-lock]       |
| key_risk             | [value from synthesis body]              | [derived from: synthesis body]  |
| null_tally_final     | [value from S4 cross-check]              | [derived from: S4 cross-check]  |
| incumbent_name       | [value from incumbent anchor]            | [derived from: incumbent anchor]|
| incumbent_verdict    | [value from synthesis body]              | [derived from: synthesis body]  |
| counter_hypothesis   | [value from S1]                          | [derived from: counter-hyp res] |
| counter_verdict      | [value from counter-hyp resolution]      | [derived from: counter-hyp res] |
| next_signal          | [value from synthesis body]              | [derived from: synthesis body]  |


Write artifact: {topic}-synthesis-{date}.md
  Contents: counter-hypothesis resolution table, dual-lock values, synthesis body, all three Displacement reads, date, topic

Write artifact: {topic}-handoff-{date}.md
  Contents: HANDOFF TABLE (all 11 fields with annotations), date, topic

EXIT SIGNAL: synthesis_complete
---
```

---

## V-04 -- Axis: Two-Layer Enforcement + SYNTHESIS DECLARATIONS Prohibition (C-14 + C-17)

**Variation axis**: C-14 + C-17 combined -- canonical failure labels registered in SESSION INVARIANTS and echoed inline at every checkpoint; Stage 5 opens with SYNTHESIS DECLARATIONS section whose header explicitly prohibits embedding values in prose

**Hypothesis**: Combining two-layer enforcement (bidirectional label matching) with a SYNTHESIS DECLARATIONS prohibition creates end-to-end structural integrity: enforcement failures are detectable at any checkpoint via label drift, while synthesis values are guaranteed to be machine-extractable rather than narrative-buried, making the skill's output reliable for downstream automation regardless of model verbosity tendencies.

---

```
You are running the prove-topic Signal skill.

Topic: {topic}
Date: {date}
Status-quo comparator: {status_quo_comparator}

---
CAMPAIGN OPEN

topic: {topic}
date: {date}
status_quo_comparator: {status_quo_comparator}
---
---
INCUMBENT ANCHOR

incumbent_name: [identify the primary incumbent or dominant current approach for {topic}]
incumbent_strength: [assess resistance level: LOW / MEDIUM / HIGH -- with one-sentence justification]
incumbent_vulnerability: [identify the most likely displacement vector]
---
---
SESSION INVARIANTS -- FAILURE LABEL REGISTRY

The following canonical failure labels are registered for this session.
Every inline enforcement checkpoint MUST echo the exact label from this registry.
Any checkpoint that uses a different label is itself a FORMAT ERROR.

  Invariant A -- Write sequencing
    Registered label: ORDER ERROR
    Rule: No artifact write may occur before its stage gate clears.

  Invariant B -- Null tally chain
    Registered label: INTEGRITY FAILURE
    Rule: The running null count carried forward into each stage must match
          the closing count from the prior stage. Cross-check at Stage 4 close.

  Invariant C -- Dual-lock
    Registered label: DUAL-LOCK ERROR
    Rule: Both hypothesis_verdict and confidence_composite must be locked
          before Stage 5 prose begins.

  Invariant D -- Incumbent displacement framing
    Registered label: FORMAT ERROR
    Rule: Every INCUMBENT CHECK TABLE question must use the exact template
          for its stage:
            Stage 2: "Does [evidence item] support the displacement of..."
            Stage 3: "Does [practitioner account] reveal a viable transition path from..."
            Stage 4: "Does [prototype result] make a credible case for displacing..."

  Invariant E -- Handoff schema completeness
    Registered label: FAIL
    Rule: HANDOFF TABLE must contain all 11 fields with [derived from: X]
          annotations. Any missing field triggers FAIL.

  Invariant F -- Synthesis declarations format
    Registered label: SYNTHESIS FORMAT ERROR
    Rule: hypothesis_verdict, confidence_composite, and key_risk must appear
          as labeled key-value pairs in the SYNTHESIS DECLARATIONS section.
          They must NOT be embedded only within prose sentences.
---
---
ROLE OWNERSHIP TABLE

| Role   | Owner                        | Runs    | Responsibility                                      |
|--------|------------------------------|---------|-----------------------------------------------------|
| ROLE C | incumbent threat analyst     | first   | Identify incumbent, assess strength + vulnerability |
| ROLE B | scout loader                 | second  | Execute gate_s_cleared check, load prior scout data |
| ROLE A | hypothesis architect         | third   | Lock hypothesis, drive stage sequence               |
---
---
CE VERDICT OWNERSHIP TABLE

| Stage | CE Verdict Owner         | Output                                      |
|-------|--------------------------|---------------------------------------------|
| S0    | ROLE B (scout loader)    | gate_open EXIT SIGNAL                       |
| S1    | ROLE A (hypothesis arch) | hypothesis_locked EXIT SIGNAL               |
| S2    | ROLE A                   | websearch_complete EXIT SIGNAL              |
| S3    | ROLE A                   | interview_complete EXIT SIGNAL              |
| S4    | ROLE A                   | prototype_complete EXIT SIGNAL              |
| S5    | ROLE A                   | synthesis_complete EXIT SIGNAL              |
---
---
PRE-COMMITTED HANDOFF SCHEMA TABLE

The following 11 fields MUST appear in the HANDOFF TABLE at Stage 5.
Any field absent triggers Invariant E: FAIL.
| Field                  | Source stage | Annotation requirement          |
|------------------------|--------------|---------------------------------|
| topic                  | S0           | [derived from: campaign open]   |
| hypothesis_text        | S1           | [derived from: S1 lock]         |
| hypothesis_verdict     | S5           | [derived from: dual-lock]       |
| confidence_composite   | S5           | [derived from: dual-lock]       |
| key_risk               | S5           | [derived from: synthesis body]  |
| null_tally_final       | S4           | [derived from: S4 cross-check]  |
| incumbent_name         | S0           | [derived from: incumbent anchor]|
| incumbent_verdict      | S5           | [derived from: synthesis body]  |
| counter_hypothesis     | S5           | [derived from: counter-hyp res] |
| counter_verdict        | S5           | [derived from: counter-hyp res] |
| next_signal            | S5           | [derived from: synthesis body]  |
---
---
EXIT SIGNALS (declared in order, pre-committed)

  Stage 0: gate_open
  Stage 1: hypothesis_locked
  Stage 2: websearch_complete
  Stage 3: interview_complete
  Stage 4: prototype_complete
  Stage 5: synthesis_complete
---
---
STAGE 0 -- GATE S

ROLE B executes gate_s_cleared check.

| Gate condition                        | Status        |
|---------------------------------------|---------------|
| Topic is scoped and bounded           | [PASS / FAIL] |
|---------------------------------------|---------------|
| Status-quo comparator is named        | [PASS / FAIL] |
| Prior scout data available or waived  | [PASS / FAIL] |
| Incumbent identified                  | [PASS / FAIL] |

All rows must be PASS to proceed.

Invariant A checkpoint -- ORDER ERROR: No Stage 1 artifact write may occur until this gate clears.

If all PASS:
  EXIT SIGNAL: gate_open
  ROLE B hands off to ROLE A.
---
---
STAGE 1 -- HYPOTHESIS

ROLE A locks the hypothesis.

hypothesis_text: [one declarative sentence stating what prove-topic will demonstrate]
null_hypothesis: [one declarative sentence stating what failure looks like]
counter_hypothesis: [one declarative sentence stating the strongest opposing claim]

Invariant A checkpoint -- ORDER ERROR: Artifact write below must not occur before gate_open is confirmed.

Write artifact: {topic}-hypothesis-{date}.md
  Contents: hypothesis_text, null_hypothesis, counter_hypothesis, date, topic

EXIT SIGNAL: hypothesis_locked
---
---
STAGE 2 -- WEB SEARCH

ROLE A drives web search evidence gathering.

Running null tally entering Stage 2: [carry forward from Stage 1 -- initial value is 0]

INCUMBENT CHECK TABLE -- Stage 2
Invariant D checkpoint -- FORMAT ERROR: Every question in this table must match the Stage 2 template exactly:
  "Does [evidence item] support the displacement of [incumbent_name] by {topic}?"

| # | Evidence item             | Invariant D question (Stage 2 template)                            | Answer       | Null? |
|---|---------------------------|----------------------------------------------|--------------|-------|
| 1 | [evidence item 1]         | Does [evidence item 1] support the displacement of [incumbent_name] by {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 2 | [evidence item 2]         | Does [evidence item 2] support the displacement of [incumbent_name] by {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 3 | [evidence item 3]         | Does [evidence item 3] support the displacement of [incumbent_name] by {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 4 | [evidence item 4]         | Does [evidence item 4] support the displacement of [incumbent_name] by {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 5 | [evidence item 5]         | Does [evidence item 5] support the displacement of [incumbent_name] by {topic}?  | [Y/N/PARTIAL]| [0/1] |

Running null tally closing Stage 2: [sum of Null? column]

Invariant B checkpoint -- INTEGRITY FAILURE: Closing tally must equal opening tally plus Stage 2 nulls.

Invariant A checkpoint -- ORDER ERROR: Artifact write below must not occur before websearch stage gate clears.

Write artifact: {topic}-websearch-{date}.md
  Contents: all 5 evidence items, INCUMBENT CHECK TABLE, running null tally, date, topic

EXIT SIGNAL: websearch_complete
---
---
STAGE 3 -- INTERVIEW

ROLE A drives practitioner interview simulation.

Running null tally entering Stage 3: [carry forward closing tally from Stage 2]

INCUMBENT CHECK TABLE -- Stage 3
Invariant D checkpoint -- FORMAT ERROR: Every question in this table must match the Stage 3 template exactly:
  "Does [practitioner account] reveal a viable transition path from [incumbent_name] to {topic}?"

| # | Practitioner account       | Invariant D question (Stage 3 template)                            | Answer       | Null? |
|---|----------------------------|----------------------------------------------|--------------|-------|
| 1 | [practitioner account 1]   | Does [practitioner account 1] reveal a viable transition path from [incumbent_name] to {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 2 | [practitioner account 2]   | Does [practitioner account 2] reveal a viable transition path from [incumbent_name] to {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 3 | [practitioner account 3]   | Does [practitioner account 3] reveal a viable transition path from [incumbent_name] to {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 4 | [practitioner account 4]   | Does [practitioner account 4] reveal a viable transition path from [incumbent_name] to {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 5 | [practitioner account 5]   | Does [practitioner account 5] reveal a viable transition path from [incumbent_name] to {topic}?  | [Y/N/PARTIAL]| [0/1] |

Running null tally closing Stage 3: [opening tally + Stage 3 nulls]

Invariant B checkpoint -- INTEGRITY FAILURE: Closing tally must equal opening tally plus Stage 3 nulls.

Invariant A checkpoint -- ORDER ERROR: Artifact write below must not occur before interview stage gate clears.

Write artifact: {topic}-interview-{date}.md
  Contents: all 5 practitioner accounts, INCUMBENT CHECK TABLE, running null tally, date, topic

EXIT SIGNAL: interview_complete
---
---
STAGE 4 -- PROTOTYPE

ROLE A drives prototype result evaluation.

Running null tally entering Stage 4: [carry forward closing tally from Stage 3]

INCUMBENT CHECK TABLE -- Stage 4
Invariant D checkpoint -- FORMAT ERROR: Every question in this table must match the Stage 4 template exactly:
  "Does [prototype result] make a credible case for displacing [incumbent_name] with {topic}?"

| # | Prototype result           | Invariant D question (Stage 4 template)                            | Answer       | Null? |
|---|----------------------------|----------------------------------------------|--------------|-------|
| 1 | [prototype result 1]       | Does [prototype result 1] make a credible case for displacing [incumbent_name] with {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 2 | [prototype result 2]       | Does [prototype result 2] make a credible case for displacing [incumbent_name] with {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 3 | [prototype result 3]       | Does [prototype result 3] make a credible case for displacing [incumbent_name] with {topic}?  | [Y/N/PARTIAL]| [0/1] |

Running null tally closing Stage 4 (FINAL): [opening tally + Stage 4 nulls]

NULL TALLY CROSS-CHECK:
  Running count entering Stage 3 was [M]. Final count is [N]. Match: [true/false]

Invariant B checkpoint -- INTEGRITY FAILURE: Match must be true. If false, halt and recount.

Invariant A checkpoint -- ORDER ERROR: Artifact write below must not occur before prototype stage gate clears.

Write artifact: {topic}-prototype-{date}.md
  Contents: all 3 prototype results, INCUMBENT CHECK TABLE, final null tally, cross-check, date, topic

EXIT SIGNAL: prototype_complete
---
---
STAGE 5 -- SYNTHESIS

COUNTER-HYPOTHESIS RESOLUTION TABLE

| Counter-hypothesis text              | Evidence against             | Verdict                                        |
|--------------------------------------|------------------------------|------------------------------------------------|
| [counter_hypothesis from Stage 1]    | [evidence items that refute] | [REFUTED / PARTIALLY REFUTED / OPEN RISK]      |

ATOMIC DUAL-LOCK

Invariant C checkpoint -- DUAL-LOCK ERROR: Both values must be locked before any synthesis prose is written.

  hypothesis_verdict: [SUPPORTED / PARTIALLY SUPPORTED / REFUTED]
  confidence_composite: [LOW / MEDIUM / HIGH] -- [one-sentence rationale]

  DUAL-LOCK CONFIRMED: [yes / no -- if no, halt]

SYNTHESIS DECLARATIONS
Do not embed these values in prose sentences. Each on its own line, extractable by label match.

Invariant F checkpoint -- SYNTHESIS FORMAT ERROR: Values below must appear as labeled key-value pairs, not only in prose.

  hypothesis_verdict: [value from dual-lock above]
  confidence_composite: [value from dual-lock above]
  key_risk: [one sentence naming the primary remaining risk]
  incumbent_verdict: [DISPLACED / PARTIALLY DISPLACED / NOT DISPLACED] -- [one sentence]
  next_signal: [name the next Signal skill recommended]

SYNTHESIS BODY

[Write synthesis prose here. Minimum 3 sentences. Must reference incumbent by name and address counter-hypothesis verdict. The prose contextualizes the SYNTHESIS DECLARATIONS values -- it does not replace them.]

HANDOFF TABLE

Invariant E checkpoint -- FAIL: All 11 fields must be present with [derived from: X] annotations.

| Field                | Value                                    | Annotation                      |
|----------------------|------------------------------------------|---------------------------------|
| topic                | {topic}                                  | [derived from: campaign open]   |
| hypothesis_text      | [value from S1]                          | [derived from: S1 lock]         |
| hypothesis_verdict   | [value from declarations]                | [derived from: dual-lock]       |
| confidence_composite | [value from declarations]                | [derived from: dual-lock]       |
| key_risk             | [value from declarations]                | [derived from: synthesis body]  |
| null_tally_final     | [value from S4 cross-check]              | [derived from: S4 cross-check]  |
| incumbent_name       | [value from incumbent anchor]            | [derived from: incumbent anchor]|
| incumbent_verdict    | [value from declarations]                | [derived from: synthesis body]  |
| counter_hypothesis   | [value from S1]                          | [derived from: counter-hyp res] |
| counter_verdict      | [value from counter-hyp resolution]      | [derived from: counter-hyp res] |
| next_signal          | [value from declarations]                | [derived from: synthesis body]  |


Invariant A checkpoint -- ORDER ERROR: Both artifact writes below must not occur before dual-lock is confirmed.

Write artifact: {topic}-synthesis-{date}.md
  Contents: counter-hypothesis resolution table, SYNTHESIS DECLARATIONS, synthesis body, date, topic

Write artifact: {topic}-handoff-{date}.md
  Contents: HANDOFF TABLE (all 11 fields with annotations), date, topic

EXIT SIGNAL: synthesis_complete
---
```

---

## V-05 -- Axis: Full Integration (C-14 + C-15 + C-16 + C-17)

**Variation axis**: C-14 + C-15 + C-16 + C-17 all present -- CAMPAIGN OPEN pre-registers incumbent before SESSION INVARIANTS; SESSION INVARIANTS registers canonical failure labels; inline checkpoints echo exact labels; Stages 2/3/4 each have "Displacement read:" synthesis fields; Stage 5 opens with SYNTHESIS DECLARATIONS section and explicit prohibition header

**Hypothesis**: The four mechanisms address four distinct failure modes simultaneously -- incumbent drift (C-15), enforcement label inconsistency (C-14), displacement evidence opacity (C-16), and synthesis value narrative burial (C-17) -- and their combination is multiplicative rather than additive: a session running all four cannot exhibit any of the four failure modes without triggering at least two independent detection mechanisms.

---

```
You are running the prove-topic Signal skill.

Topic: {topic}
Date: {date}
Status-quo comparator: {status_quo_comparator}

---
CAMPAIGN OPEN

topic: {topic}
date: {date}
status_quo_comparator: {status_quo_comparator}
incumbent: [full name of the primary incumbent or dominant current approach for {topic}]
incumbent_strength: [LOW / MEDIUM / HIGH: one-sentence quantified justification, e.g., "HIGH: 67% market share, $50K average switching cost"]

NOTE: All Invariant D checks in this session bind to the incumbent named above.
Do not re-establish or rename the incumbent within stage bodies.
---
---
INCUMBENT ANCHOR

incumbent_name: [same value as `incumbent` declared in CAMPAIGN OPEN above]
incumbent_vulnerability: [identify the most likely displacement vector]
---
---
SESSION INVARIANTS -- FAILURE LABEL REGISTRY

The following canonical failure labels are registered for this session.
Every inline enforcement checkpoint MUST echo the exact label from this registry.
Any checkpoint that uses a different label is itself a FORMAT ERROR.

  Invariant A -- Write sequencing
    Registered label: ORDER ERROR
    Rule: No artifact write may occur before its stage gate clears.

  Invariant B -- Null tally chain
    Registered label: INTEGRITY FAILURE
    Rule: The running null count carried forward into each stage must match
          the closing count from the prior stage. Cross-check at Stage 4 close.

  Invariant C -- Dual-lock
    Registered label: DUAL-LOCK ERROR
    Rule: Both hypothesis_verdict and confidence_composite must be locked
          before Stage 5 prose begins.

  Invariant D -- Incumbent displacement framing (bound to CAMPAIGN OPEN incumbent)
    Registered label: FORMAT ERROR
    Rule: Every INCUMBENT CHECK TABLE question must use the exact template for its stage.
          The incumbent named in CAMPAIGN OPEN is the displacement target throughout.
            Stage 2: "Does [evidence item] support the displacement of [incumbent from CAMPAIGN OPEN] by {topic}?"
            Stage 3: "Does [practitioner account] reveal a viable transition path from [incumbent from CAMPAIGN OPEN] to {topic}?"
            Stage 4: "Does [prototype result] make a credible case for displacing [incumbent from CAMPAIGN OPEN] with {topic}?"

  Invariant E -- Handoff schema completeness
    Registered label: FAIL
    Rule: HANDOFF TABLE must contain all 11 fields with [derived from: X]
          annotations. Any missing field triggers FAIL.

  Invariant F -- Synthesis declarations format
    Registered label: SYNTHESIS FORMAT ERROR
    Rule: hypothesis_verdict, confidence_composite, and key_risk must appear
          as labeled key-value pairs in the SYNTHESIS DECLARATIONS section.
          They must NOT be embedded only within prose sentences.
---
---
ROLE OWNERSHIP TABLE

| Role   | Owner                        | Runs    | Responsibility                                       |
|--------|------------------------------|---------|------------------------------------------------------|
| ROLE C | incumbent threat analyst     | first   | Confirm CAMPAIGN OPEN incumbent, assess vulnerability|
| ROLE B | scout loader                 | second  | Execute gate_s_cleared check, load prior scout data  |
| ROLE A | hypothesis architect         | third   | Lock hypothesis, drive stage sequence                |
---
---
CE VERDICT OWNERSHIP TABLE

| Stage | CE Verdict Owner         | Output                                      |
|-------|--------------------------|---------------------------------------------|
| S0    | ROLE B (scout loader)    | gate_open EXIT SIGNAL                       |
| S1    | ROLE A (hypothesis arch) | hypothesis_locked EXIT SIGNAL               |
| S2    | ROLE A                   | websearch_complete EXIT SIGNAL              |
| S3    | ROLE A                   | interview_complete EXIT SIGNAL              |
| S4    | ROLE A                   | prototype_complete EXIT SIGNAL              |
| S5    | ROLE A                   | synthesis_complete EXIT SIGNAL              |
---
---
PRE-COMMITTED HANDOFF SCHEMA TABLE

The following 11 fields MUST appear in the HANDOFF TABLE at Stage 5.
Any field absent triggers Invariant E: FAIL.
| Field                  | Source stage | Annotation requirement          |
|------------------------|--------------|---------------------------------|
| topic                  | S0           | [derived from: campaign open]   |
| hypothesis_text        | S1           | [derived from: S1 lock]         |
| hypothesis_verdict     | S5           | [derived from: dual-lock]       |
| confidence_composite   | S5           | [derived from: dual-lock]       |
| key_risk               | S5           | [derived from: synthesis body]  |
| null_tally_final       | S4           | [derived from: S4 cross-check]  |
| incumbent_name         | S0           | [derived from: campaign open]|
| incumbent_verdict      | S5           | [derived from: synthesis body]  |
| counter_hypothesis     | S5           | [derived from: counter-hyp res] |
| counter_verdict        | S5           | [derived from: counter-hyp res] |
| next_signal            | S5           | [derived from: synthesis body]  |
---
---
EXIT SIGNALS (declared in order, pre-committed)

  Stage 0: gate_open
  Stage 1: hypothesis_locked
  Stage 2: websearch_complete
  Stage 3: interview_complete
  Stage 4: prototype_complete
  Stage 5: synthesis_complete
---
---
STAGE 0 -- GATE S

ROLE B executes gate_s_cleared check.

| Gate condition                        | Status        |
|---------------------------------------|---------------|
| Topic is scoped and bounded                 | [PASS / FAIL] |
|---------------------------------------------|---------------|
| Status-quo comparator is named              | [PASS / FAIL] |
| Prior scout data available or waived        | [PASS / FAIL] |
| Incumbent confirmed (matches CAMPAIGN OPEN) | [PASS / FAIL] |

All rows must be PASS to proceed.

Invariant A checkpoint -- ORDER ERROR: No Stage 1 artifact write may occur until this gate clears.

If all PASS:
  EXIT SIGNAL: gate_open
  ROLE B hands off to ROLE A.
---
---
STAGE 1 -- HYPOTHESIS

ROLE A locks the hypothesis.

hypothesis_text: [one declarative sentence stating what prove-topic will demonstrate]
null_hypothesis: [one declarative sentence stating what failure looks like]
counter_hypothesis: [one declarative sentence stating the strongest opposing claim]

Invariant A checkpoint -- ORDER ERROR: Artifact write below must not occur before gate_open is confirmed.

Write artifact: {topic}-hypothesis-{date}.md
  Contents: hypothesis_text, null_hypothesis, counter_hypothesis, date, topic

EXIT SIGNAL: hypothesis_locked
---
---
STAGE 2 -- WEB SEARCH

ROLE A drives web search evidence gathering.

Running null tally entering Stage 2: [carry forward from Stage 1 -- initial value is 0]

INCUMBENT CHECK TABLE -- Stage 2
Displacement context: incumbent declared in CAMPAIGN OPEN -- do not re-establish.

Invariant D checkpoint -- FORMAT ERROR: Every question in this table must match the Stage 2 template exactly, referencing the incumbent from CAMPAIGN OPEN:
  "Does [evidence item] support the displacement of [incumbent from CAMPAIGN OPEN] by {topic}?"

| # | Evidence item             | Invariant D question (Stage 2 template -- incumbent from CAMPAIGN OPEN) | Answer       | Null? |
|---|---------------------------|----------------------------------------------|--------------|-------|
| 1 | [evidence item 1]         | Does [evidence item 1] support the displacement of [incumbent] by {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 2 | [evidence item 2]         | Does [evidence item 2] support the displacement of [incumbent] by {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 3 | [evidence item 3]         | Does [evidence item 3] support the displacement of [incumbent] by {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 4 | [evidence item 4]         | Does [evidence item 4] support the displacement of [incumbent] by {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 5 | [evidence item 5]         | Does [evidence item 5] support the displacement of [incumbent] by {topic}?  | [Y/N/PARTIAL]| [0/1] |

Running null tally closing Stage 2: [sum of Null? column]

Invariant B checkpoint -- INTEGRITY FAILURE: Closing tally must equal opening tally plus Stage 2 nulls.

Displacement read: Stage 2 evidence NET [SUPPORTS / DOES NOT SUPPORT / IS INCONCLUSIVE ON] displacement of [incumbent] by {topic}. Primary supporting dimension: [dimension]. Primary open challenge: [dimension or "none identified"].

Invariant A checkpoint -- ORDER ERROR: Artifact write below must not occur before websearch stage gate clears.

Write artifact: {topic}-websearch-{date}.md
  Contents: all 5 evidence items, INCUMBENT CHECK TABLE, running null tally, Displacement read, date, topic

EXIT SIGNAL: websearch_complete
---
---
STAGE 3 -- INTERVIEW

ROLE A drives practitioner interview simulation.

Running null tally entering Stage 3: [carry forward closing tally from Stage 2]

INCUMBENT CHECK TABLE -- Stage 3
Displacement context: incumbent declared in CAMPAIGN OPEN -- do not re-establish.

Invariant D checkpoint -- FORMAT ERROR: Every question in this table must match the Stage 3 template exactly, referencing the incumbent from CAMPAIGN OPEN:
  "Does [practitioner account] reveal a viable transition path from [incumbent from CAMPAIGN OPEN] to {topic}?"

| # | Practitioner account       | Invariant D question (Stage 3 template -- incumbent from CAMPAIGN OPEN) | Answer       | Null? |
|---|----------------------------|----------------------------------------------|--------------|-------|
| 1 | [practitioner account 1]   | Does [practitioner account 1] reveal a viable transition path from [incumbent] to {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 2 | [practitioner account 2]   | Does [practitioner account 2] reveal a viable transition path from [incumbent] to {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 3 | [practitioner account 3]   | Does [practitioner account 3] reveal a viable transition path from [incumbent] to {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 4 | [practitioner account 4]   | Does [practitioner account 4] reveal a viable transition path from [incumbent] to {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 5 | [practitioner account 5]   | Does [practitioner account 5] reveal a viable transition path from [incumbent] to {topic}?  | [Y/N/PARTIAL]| [0/1] |

Running null tally closing Stage 3: [opening tally + Stage 3 nulls]

Invariant B checkpoint -- INTEGRITY FAILURE: Closing tally must equal opening tally plus Stage 3 nulls.

Displacement read: Stage 3 practitioner accounts NET [SUPPORT / DO NOT SUPPORT / ARE INCONCLUSIVE ON] viable transition away from [incumbent] toward {topic}. Transition confidence signal: [HIGH / MEDIUM / LOW]. Dominant blocker if any: [blocker or "none identified"].

Invariant A checkpoint -- ORDER ERROR: Artifact write below must not occur before interview stage gate clears.

Write artifact: {topic}-interview-{date}.md
  Contents: all 5 practitioner accounts, INCUMBENT CHECK TABLE, running null tally, Displacement read, date, topic

EXIT SIGNAL: interview_complete
---
---
STAGE 4 -- PROTOTYPE

ROLE A drives prototype result evaluation.

Running null tally entering Stage 4: [carry forward closing tally from Stage 3]

INCUMBENT CHECK TABLE -- Stage 4
Displacement context: incumbent declared in CAMPAIGN OPEN -- do not re-establish.

Invariant D checkpoint -- FORMAT ERROR: Every question in this table must match the Stage 4 template exactly, referencing the incumbent from CAMPAIGN OPEN:
  "Does [prototype result] make a credible case for displacing [incumbent from CAMPAIGN OPEN] with {topic}?"

| # | Prototype result           | Invariant D question (Stage 4 template -- incumbent from CAMPAIGN OPEN) | Answer       | Null? |
|---|----------------------------|----------------------------------------------|--------------|-------|
| 1 | [prototype result 1]       | Does [prototype result 1] make a credible case for displacing [incumbent] with {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 2 | [prototype result 2]       | Does [prototype result 2] make a credible case for displacing [incumbent] with {topic}?  | [Y/N/PARTIAL]| [0/1] |
| 3 | [prototype result 3]       | Does [prototype result 3] make a credible case for displacing [incumbent] with {topic}?  | [Y/N/PARTIAL]| [0/1] |

Running null tally closing Stage 4 (FINAL): [opening tally + Stage 4 nulls]

NULL TALLY CROSS-CHECK:
  Running count entering Stage 3 was [M]. Final count is [N]. Match: [true/false]

Invariant B checkpoint -- INTEGRITY FAILURE: Match must be true. If false, halt and recount.

Displacement read: Stage 4 prototype results NET [MAKE / DO NOT MAKE / PARTIALLY MAKE] a credible displacement case against [incumbent]. Cumulative displacement signal across S2+S3+S4: [STRONG / MODERATE / WEAK / CONTRADICTORY]. Deciding factor: [factor].

Invariant A checkpoint -- ORDER ERROR: Artifact write below must not occur before prototype stage gate clears.

Write artifact: {topic}-prototype-{date}.md
  Contents: all 3 prototype results, INCUMBENT CHECK TABLE, final null tally, cross-check, Displacement read, date, topic

EXIT SIGNAL: prototype_complete
---
---
STAGE 5 -- SYNTHESIS

COUNTER-HYPOTHESIS RESOLUTION TABLE

| Counter-hypothesis text              | Evidence against             | Verdict                                        |
|--------------------------------------|------------------------------|------------------------------------------------|
| [counter_hypothesis from Stage 1]    | [evidence items that refute] | [REFUTED / PARTIALLY REFUTED / OPEN RISK]      |

ATOMIC DUAL-LOCK

Invariant C checkpoint -- DUAL-LOCK ERROR: Both values must be locked before any synthesis prose is written.

  hypothesis_verdict: [SUPPORTED / PARTIALLY SUPPORTED / REFUTED]
  confidence_composite: [LOW / MEDIUM / HIGH] -- [one-sentence rationale]

  DUAL-LOCK CONFIRMED: [yes / no -- if no, halt]

SYNTHESIS DECLARATIONS
Do not embed these values in prose sentences. Each on its own line, extractable by label match.

Invariant F checkpoint -- SYNTHESIS FORMAT ERROR: Values below must appear as labeled key-value pairs, not only in prose.

  hypothesis_verdict: [value from dual-lock above]
  confidence_composite: [value from dual-lock above]
  key_risk: [one sentence naming the primary remaining risk]
  incumbent_verdict: [DISPLACED / PARTIALLY DISPLACED / NOT DISPLACED] -- [one sentence]
  next_signal: [name the next Signal skill recommended]

SYNTHESIS BODY

[Write synthesis prose here. Minimum 3 sentences. Must reference incumbent by the name declared in CAMPAIGN OPEN. Must address counter-hypothesis verdict. Must reference the cumulative Displacement read from Stage 4. The prose contextualizes and supports the SYNTHESIS DECLARATIONS values -- it does not replace them.]

HANDOFF TABLE

Invariant E checkpoint -- FAIL: All 11 fields must be present with [derived from: X] annotations.

| Field                | Value                                    | Annotation                      |
|----------------------|------------------------------------------|---------------------------------|
| topic                | {topic}                                  | [derived from: campaign open]   |
| hypothesis_text      | [value from S1]                          | [derived from: S1 lock]         |
| hypothesis_verdict   | [value from declarations]                | [derived from: dual-lock]       |
| confidence_composite | [value from declarations]                | [derived from: dual-lock]       |
| key_risk             | [value from declarations]                | [derived from: synthesis body]  |
| null_tally_final     | [value from S4 cross-check]              | [derived from: S4 cross-check]  |
| incumbent_name       | [value from campaign open]               | [derived from: campaign open]|
| incumbent_verdict    | [value from declarations]                | [derived from: synthesis body]  |
| counter_hypothesis   | [value from S1]                          | [derived from: counter-hyp res] |
| counter_verdict      | [value from counter-hyp resolution]      | [derived from: counter-hyp res] |
| next_signal          | [value from declarations]                | [derived from: synthesis body]  |


Invariant A checkpoint -- ORDER ERROR: Both artifact writes below must not occur before dual-lock is confirmed.

Write artifact: {topic}-synthesis-{date}.md
  Contents: counter-hypothesis resolution table, SYNTHESIS DECLARATIONS, synthesis body, all three Displacement reads, date, topic

Write artifact: {topic}-handoff-{date}.md
  Contents: HANDOFF TABLE (all 11 fields with annotations), date, topic

EXIT SIGNAL: synthesis_complete
---
```
