---
skill: quest-variate
skill_target: mock-all
date: 2026-03-15
round: 5
rubric_version: v5
status: VARIATE
---

# mock-all Variate — Round 5

**Date:** 2026-03-15
**Skill:** mock-all
**Rubric:** v5 (C-01 through C-17; aspirational denominator = 9)
**Round:** R5 — new axis (role-sequence) + two upgrades from R4 gaps

---

## What R4 Left Open

v5 adds no new criteria beyond v4 (C-09 through C-17 unchanged). R4 V-01, V-02, V-04, V-05
predicted 100; R4 V-03 (inertia-framing without vocab columns) predicted 98.9. R5 has three
open questions:

| Question | R4 state | R5 target |
|----------|----------|-----------|
| Can role-sequence declarations (CLASSIFIER, GENERATOR, SUMMARIZER) enforce C-11 at the identity level — more reliably than PHASE or STEP labels? | Untested R1–R4 | V-01, V-04 |
| Can pure conversational register (second-person instructional framing) maintain 100 while improving C-07/C-10 execution quality? | R3 V-03 used vocabulary-column structure labeled "phrasing-register" — pure conversational framing never isolated | V-02, V-05 |
| Can inertia-framing reach 100 by adding vocabulary columns to R4 V-03's base? R4 V-03 scored 98.9 — C-17 FAIL was the only miss. | R4 V-03: inertia-framing, C-17 FAIL, 98.9 | V-03 |

---

## Axis-Assignment Plan

| Plan | Axis | Source signal | Target criteria | Predicted |
|------|------|---------------|-----------------|-----------|
| V-01 | role-sequence | New axis. Role identity ("As the CLASSIFIER, you only classify") blocks artifact writing at the identity level — stronger than phase-label ordering. Vocab columns appear in CLASSIFIER output (C-17). Enumerated ROLE STOP gates name five required fields (C-16). | C-11, C-14, C-16, C-17 | 100 |
| V-02 | phrasing-register (conversational) | R3 V-03 was vocabulary-columns under a "phrasing-register" label. Pure conversational framing — "Once you've filled in the table, move to STEP 2" — has never been isolated. Vocab columns and enumerated stop-gates preserved; only the instructional voice changes. Hypothesis: conversational framing improves C-07 artifact depth and C-10 specificity by making each step feel natural rather than commanded. | C-07/C-10 quality; C-14/C-16/C-17 maintained | 100 |
| V-03 | inertia-framing (upgraded) | R4 V-03 had inertia framing without vocabulary columns: C-17 FAIL, score 98.9. Adding vocabulary columns to R4 V-03's base closes C-17. The test: does inertia priming produce deeper artifact bodies (C-07) and sharper next steps (C-10) than a structurally equivalent variation without it? | C-17 (fix R4 V-03 miss); C-07/C-10 quality | 100 |
| V-04 | role-sequence + lifecycle-emphasis | Combines role identity (ROLE labels, ROLE STOP gates) with explicit enumerated phase gates. Tests whether role identity adds meaningful enforcement over PHASE labels alone: ROLE STOP gates are identity-anchored ("do not activate ROLE N+1") vs procedure-anchored ("do not begin PHASE N+1"). | C-11, C-14, C-16, C-17 | 100 |
| V-05 | role-sequence + phrasing-register + output-format | Full R5 ceiling: role declarations + conversational register + minimal pre-printed skeleton (table stubs pre-printed; artifact stubs instruction-generated). Tests whether role framing + conversational tone can reduce skeleton weight from R3/R4 while maintaining C-11's structural guarantee via role identity. | C-07, C-10, C-11, C-14, C-16, C-17 | 100 |

---

## V-01 — Role Sequence (Single-Axis: New)

**axis:** role-sequence
**hypothesis:** R1–R4 used PHASE or STEP labels to enforce generation ordering. Phase labels
establish procedural order by implication; stop-gate sentences add explicit blocking but rely
on the model treating "Do not begin PHASE 2" as a generation barrier. Role identity is a
stronger framing: "As the CLASSIFIER, you only classify" tells the model WHAT IT IS, not just
what to do next. A model that has adopted the CLASSIFIER identity cannot write artifact bodies
without violating its current role — the constraint is ontological, not procedural. This also
affects C-11 naturally: if the CLASSIFIER role produces only a classification table, artifact
bodies cannot precede it by definition. Vocabulary columns appear in the CLASSIFIER output
(C-17). Enumerated ROLE STOP gates name all five required fields (C-16). ROLE 4 (HANDOFF
WRITER) provides the dedicated labelled section for C-12.
**predicted:** C-11 PASS (role identity blocks premature generation at the identity level,
not just the instruction level), C-14 PASS (ROLE STOP gates are explicit gate phrases),
C-16 PASS (ROLE STOP gates enumerate five fields), C-17 PASS (vocab columns in CLASSIFIER
output). All 9 aspirational criteria PASS. Score: 100.
**failure condition:** The model ignores role identity framing and generates artifact body
content inside ROLE 1's output, treating ROLE labels as decorative headers rather than
identity constraints. If this occurs, role-sequence provides no enforcement advantage over
PHASE labels — C-11 fails in execution despite the identity instruction.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record: tier for {topic}, compliance tags (if any).
State: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs four sequential roles. Each role completes its full output before the next
role activates. A role may not produce output belonging to a later role.

---

### ROLE 1 — CLASSIFIER

As the CLASSIFIER, your only task is to produce the classification table. You do not write
artifact bodies. You do not write coverage summaries. You classify.

Categories:
  HIGH-STRUCTURE  — structural artifacts: specs, schemas, contracts, plans, state models
  EVIDENCE-HEAVY  — requires real signal; synthetic content is informational only
  MIXED           — structural scaffolding plus qualitative or narrative content

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged |
|-----------|----------|----------|------------|-------------------|-------------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language only OR pure study methodology framing | NO | YES if --compliance and TOPICS.md tags present; else NO |
| draft | MIXED | structural scaffold (sections, properties, acceptance criteria) plus qualitative observations | pure specification language only OR pure study methodology framing | NO | NO |
| review | MIXED | structural scaffold plus qualitative observations and design judgements | pure specification language only OR pure study methodology framing | NO | NO |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language, user quotes, adoption percentages, study framing | NO | NO |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language, adoption rates, user quotes, study framing | YES if tier >= 2; else NO | YES if --compliance and TOPICS.md tags; else NO |
| prove | EVIDENCE-HEAVY | study/data/interview language: "N of M tests showed...", "Prototype against {topic} produced...", hypothesis-and-result framing | specification language, schema definitions, contract structures | NO | NO |
| listen | EVIDENCE-HEAVY | study/data/interview language: adoption rates, "N users interviewed found...", survey response framing | specification language, state machine language, schema definitions | YES if tier >= 2; else NO | NO |
| program | MIXED | structural scaffold (milestones, owners, dependencies) plus qualitative rationale | pure specification language only OR pure study methodology framing | NO | NO |
| topic | MIXED | signal synthesis narrative plus structured coverage reference | pure specification language alone | NO | NO |

REAL-REQUIRED assignments (carried forward to ROLE 2 and ROLE 3):
- prove: EVIDENCE-HEAVY → REAL-REQUIRED. Rationale: A synthetic artifact cannot substitute
  for real signal; prove-* requires actual experiment data or prototype outputs.
- listen: EVIDENCE-HEAVY → REAL-REQUIRED. Rationale: A synthetic artifact cannot substitute
  for real signal; listen-* requires real user interviews or adoption measurements.
- scout-compliance (when --compliance or TOPICS.md compliance tags active): REAL-REQUIRED.
  Rationale: Compliance signals require traceable real-world sources; synthetic artifacts
  create false assurance.
- trace-permissions (when --compliance or TOPICS.md compliance tags active): REAL-REQUIRED.
  Same rationale as scout-compliance.

**ROLE 1 STOP: Do not activate ROLE 2 — GENERATOR until all nine rows in the classification
table have an assigned Category, MUST use terms, DO NOT use terms, Tier 2/3 Critical value
(YES or NO), and Compliance-Tagged value (YES or NO).**

---

### ROLE 2 — GENERATOR

As the GENERATOR, your only task is to write one synthetic artifact per namespace using the
vocabulary rules from ROLE 1's classification table. You do not re-classify. You do not write
the coverage summary. You generate.

For each namespace in classification table order:

  #### {Namespace} — {skill-name}

  **MOCK ARTIFACT**
  Skill:    {skill-name}
  Topic:    {topic}
  Category: {category from ROLE 1}
  Date:     {date}
  Status:   MOCK (awaiting review)

  {artifact body — apply ROLE 1 MUST use and DO NOT use exactly for this namespace row}

For prove and listen: append after the artifact body —
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal.
  {prove: requires actual experiment data or prototype outputs |
   listen: requires real user interviews or adoption measurements}.
DO NOT omit this statement for any EVIDENCE-HEAVY namespace.

**ROLE 2 STOP: Do not activate ROLE 3 — SUMMARIZER until all nine namespace sections are
written, each with a complete MOCK ARTIFACT header block, a vocabulary-compliant artifact
body (MUST use satisfied; DO NOT use not violated), and — for prove/listen — a REAL-REQUIRED
statement.**

---

### ROLE 3 — SUMMARIZER

As the SUMMARIZER, your only task is to produce the coverage summary table. You do not add
new artifacts. You do not revise classifications. You summarize.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
  REAL-REQUIRED  — all EVIDENCE-HEAVY namespaces (prove, listen), all tiers
  TIER-CRITICAL  — trace-*, scout-feasibility, listen-* at tier >= 2
  COMPLIANCE     — scout-compliance, trace-permissions when compliance context is active
  Multiple flags: REAL-REQUIRED + TIER-CRITICAL

Recommended Next Step: exact skill call — `/namespace:skill {topic}`.
DO NOT write "gather more signals." DO NOT write generic advice.
Example: `/listen:adoption {topic}`

**ROLE 3 STOP: Do not activate ROLE 4 — HANDOFF WRITER until all nine namespaces appear in
the coverage table with correct Category, all required Flags, and a named Recommended Next
Step.**

---

### ROLE 4 — HANDOFF WRITER

As the HANDOFF WRITER, write only the handoff instruction. No artifact bodies. No table rows.
No additional commentary.

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-{date}.md

Replace {topic} and {date} with actual values.
DO NOT write `{this-file}` as a literal placeholder.
DO NOT write any other content in this section.

---

## V-02 — Phrasing Register: Conversational (Single-Axis)

**axis:** phrasing-register (conversational)
**hypothesis:** Every prior variation used formal imperative framing: "Assign every namespace
to exactly one category." Pure conversational framing — "Your first job is to fill in this
table. Once every cell is filled, you can move to STEP 2. Not before." — reframes each step
as a natural task the model talks itself through rather than a command it executes. The
conversational register may improve C-07 artifact body depth (richer content when framing
encourages elaboration) and C-10 next-step specificity (sharper skill calls when framing
encourages specificity). Vocabulary columns, enumerated stop-gates, and REAL-REQUIRED
rationale are preserved — only the instructional voice changes. This isolates phrasing
register as the variable.
**predicted:** C-14 PASS (gate phrases present; "Stop. Do not..." is explicit even in
conversational register), C-16 PASS (gate phrases enumerate five fields), C-17 PASS (vocab
columns in classification table), C-13 PASS (REAL-REQUIRED rationale embedded at application
point). All 9 aspirational criteria PASS. Score: 100.
**failure condition:** Conversational framing signals lower structural formality to the model,
which responds by treating stop-gate sentences as suggestions rather than hard gates — C-14
fails in execution even though the gate phrases are structurally present. If this occurs,
formal imperative register is a meaningful signal for gate compliance, not just style.

---

You are running /mock:all for {topic}.

Before you start: look up {topic} in TOPICS.md and note its tier (1, 2, or 3 — default to 1
if not listed) and any compliance tags. Write this at the top of your output:
  `Tier: {N}  (source: TOPICS.md | --tier | default)`

Optional flags:
- --tier {1|2|3}: overrides tier from TOPICS.md
- --compliance: activates compliance pre-flagging for scout-compliance and trace-permissions

You'll work through four steps in order. Complete each step fully before moving to the next.

---

**STEP 1 — CLASSIFY (complete this before writing any artifact body)**

Your first job is to fill in the classification table below. Every row needs a value in every
column before you can move on.

Three categories to assign:
- HIGH-STRUCTURE: structural artifacts — specs, schemas, contracts, state models. Write using
  specification language.
- EVIDENCE-HEAVY: these namespaces need real data. Synthetic content here is informational
  only — it can't stand in for real signal.
- MIXED: combine structure with qualitative content. Both elements required in every body.

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged |
|-----------|----------|----------|------------|-------------------|-------------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language only OR pure study methodology framing | NO | YES if compliance context active; else NO |
| draft | MIXED | structural scaffold plus qualitative observations | pure specification language only OR pure study methodology framing | NO | NO |
| review | MIXED | structural scaffold plus qualitative observations and design judgements | pure specification language only OR pure study methodology framing | NO | NO |
| flow | HIGH-STRUCTURE | spec language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language, user quotes, adoption percentages, study framing | NO | NO |
| trace | HIGH-STRUCTURE | spec language: interfaces, component boundaries, contracts, state transitions, config keys | interview language, adoption rates, user quotes, study framing | YES if tier >= 2; else NO | YES if compliance context active; else NO |
| prove | EVIDENCE-HEAVY | study/data/interview language: "N of M tests showed...", "Prototype produced...", hypothesis-result framing | spec language, schema definitions, contract structures | NO | NO |
| listen | EVIDENCE-HEAVY | study/data/interview language: adoption rates, "N users found...", survey response framing | spec language, state machine language, schema definitions | YES if tier >= 2; else NO | NO |
| program | MIXED | structural scaffold (milestones, owners, dependencies) plus qualitative rationale | pure specification language only OR pure study methodology framing | NO | NO |
| topic | MIXED | signal synthesis narrative plus structured coverage reference | pure specification language alone | NO | NO |

Two namespaces are always REAL-REQUIRED — prove and listen. Here's why: a synthetic artifact
can't substitute for real experiment data or real user interviews. It's informational, not
evidence. prove-* needs actual prototype outputs or experiment data; listen-* needs real
adoption measurements or interview results.

If compliance context is active (--compliance flag or TOPICS.md tags), also mark
scout-compliance and trace-permissions as REAL-REQUIRED. Reason: compliance signals need
traceable real-world sources. A synthetic compliance artifact creates false assurance.

**Stop. Do not write any artifact body until every row in the classification table has a
Category, MUST use terms, DO NOT use terms, Tier 2/3 Critical value (YES or NO), and
Compliance-Tagged value (YES or NO).**

---

**STEP 2 — GENERATE**

Now write a synthetic artifact for each namespace in classification table order. For each:

```
#### {Namespace} — {skill-name}

**MOCK ARTIFACT**
Skill:    {skill-name}
Topic:    {topic}
Category: {from STEP 1}
Date:     {date}
Status:   MOCK (awaiting review)

{3-5 sentence artifact body}
```

A few things to keep in mind as you write:

- For flow and trace (HIGH-STRUCTURE): write about system structure — contracts, interfaces,
  state transitions. If you find yourself writing about users, interviews, or adoption rates,
  you've drifted into the wrong register.

- For prove and listen (EVIDENCE-HEAVY): write as if citing real results — "N of M tests
  showed...", "interview participants reported..." Don't use spec language. After the body,
  add:
  `REAL-REQUIRED: A synthetic artifact cannot substitute for real signal.`
  Then say what's actually needed: prove needs experiment data or prototype outputs; listen
  needs real user interviews or adoption measurements.

- For mixed namespaces (scout, draft, review, program, topic): you need both a structural
  element (a table, list, or named property) and a qualitative observation in each body.
  One without the other doesn't satisfy the category definition.

Once all nine namespace sections are written — complete header blocks, vocabulary-compliant
bodies, REAL-REQUIRED statements for prove/listen — you can move to STEP 3.

**Stop. Do not write the coverage summary until all nine namespace sections are complete,
each with a MOCK ARTIFACT header block, a vocabulary-compliant body, and (for prove/listen)
a REAL-REQUIRED statement.**

---

**STEP 3 — SUMMARIZE**

Now pull everything together into a coverage summary:

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

For the Flag column, use:
- REAL-REQUIRED: any EVIDENCE-HEAVY namespace
- TIER-CRITICAL: trace-*, scout-feasibility, listen-* when tier >= 2
- COMPLIANCE: scout-compliance, trace-permissions when compliance context is active
- Multiple: REAL-REQUIRED + TIER-CRITICAL (write both)

For Recommended Next Step: write the exact skill call, like `/listen:adoption {topic}` or
`/trace:component {topic}`. Not "gather more signals" — name the specific skill identifier.

Once all nine rows are filled in with correct flags and named next steps, move to STEP 4.

**Stop. Do not write the handoff until the coverage summary has all nine namespaces, correct
flags, and a named Recommended Next Step for each.**

---

**STEP 4 — HANDOFF**

This section contains only the handoff instruction. Nothing else goes here.

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-{date}.md

Replace {topic} and {date} with actual values.
DO NOT write `{this-file}` as a placeholder.
DO NOT write any other content in this section.

---

## V-03 — Inertia Framing + Vocabulary Columns (Single-Axis: Inertia Upgrade)

**axis:** inertia-framing (upgraded from R4 V-03)
**hypothesis:** R4 V-03 tested inertia framing as an isolated axis without vocabulary columns.
Result: C-17 FAIL, score 98.9 — the one miss was vocabulary rules placed in a prose block
rather than as table columns. This variation adds vocabulary columns to R4 V-03's inertia
base, closing C-17. The test is whether inertia framing produces measurably richer artifact
bodies (C-07) and sharper next-step calls (C-10) compared to a vocabulary-column variation
without inertia context. The inertia block names the two failure patterns teams face without
/mock:all — EVIDENCE-HEAVY content mistaken for real signal; Tier 2/3 critical namespaces
skipped — so that each artifact body is written as an answer to a real coverage gap, not a
generic template. All prior structural machinery from R4 V-04 (vocab columns + enumerated
gates) is preserved; inertia framing is the addition.
**predicted:** C-17 PASS (vocab columns now present; fixing R4 V-03's miss), C-14 PASS
(explicit stop-gate phrases), C-16 PASS (enumerated fields in gates), C-15 PASS (MUST/DO NOT
per category), C-07/C-10 quality expected higher than R4 V-04 due to inertia priming.
All 9 aspirational criteria PASS. Score: 100.
**failure condition:** Inertia framing and vocabulary columns together push prompt length past
the threshold where the model abbreviates artifact bodies to compensate — C-07 degrades while
all structural criteria pass. If this occurs, V-04 R4 (same structure, no inertia block)
achieves identical rubric score at lower cognitive load, making inertia framing a cost.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record: tier for {topic}, compliance tags (if any).
State: `Tier: {N}  (source: TOPICS.md | --tier | default)`

---

### CONTEXT — What this skill is for

Without /mock:all, teams commit to features on 1-2 signals. Two failure patterns drive
late-stage rework:

1. EVIDENCE-HEAVY namespaces (prove, listen) are filled with synthetic content that gets
   treated as real evidence. The gap surfaces at launch when prototype data or adoption rates
   diverge from mock expectations. A synthetic artifact in these namespaces is informational
   only — it is not a substitute for real signal.

2. Tier 2/3 critical namespaces (trace, scout-feasibility, listen) are skipped under time
   pressure. False confidence accumulates. The missing contract, feasibility constraint, or
   user signal surfaces during implementation at 10x the cost to fix.

/mock:all maps all nine namespaces in one pass. The output answers: which namespaces produce
structural artifacts safe to generate synthetically, which require real signal before
commitment, and the exact skill call that closes each gap.

Each artifact body in this output should reflect what its namespace uniquely contributes to
{topic}'s coverage — not a generic template, but the specific signal that would be absent if
this namespace were skipped.

---

### PHASE 1 — CLASSIFY

Assign every namespace to a category. The classification table — including vocabulary rule
columns — must be complete before any artifact body is written.

Categories:
  HIGH-STRUCTURE  — structural artifacts: specs, schemas, contracts, plans, state models
  EVIDENCE-HEAVY  — requires real signal; synthetic content is informational only
  MIXED           — structural scaffolding plus qualitative or narrative content

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged |
|-----------|----------|----------|------------|-------------------|-------------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language only OR pure study methodology framing | NO | YES if --compliance and TOPICS.md tags; else NO |
| draft | MIXED | structural scaffold (sections, properties, acceptance criteria) plus qualitative observations | pure specification language only OR pure study methodology framing | NO | NO |
| review | MIXED | structural scaffold plus qualitative observations and design judgements | pure specification language only OR pure study methodology framing | NO | NO |
| flow | HIGH-STRUCTURE | spec language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language, user quotes, adoption percentages, study framing | NO | NO |
| trace | HIGH-STRUCTURE | spec language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language, adoption rates, user quotes, study framing | YES if tier >= 2; else NO | YES if --compliance and TOPICS.md tags; else NO |
| prove | EVIDENCE-HEAVY | study/data/interview language: "N of M tests showed...", "Prototype against {topic} produced...", hypothesis-and-result framing | spec language, schema definitions, contract structures | NO | NO |
| listen | EVIDENCE-HEAVY | study/data/interview language: adoption rates, "N users interviewed found...", survey response framing | spec language, state machine language, schema definitions | YES if tier >= 2; else NO | NO |
| program | MIXED | structural scaffold (milestones, owners, dependencies) plus qualitative rationale | pure specification language only OR pure study methodology framing | NO | NO |
| topic | MIXED | signal synthesis narrative plus structured coverage reference | pure specification language alone | NO | NO |

REAL-REQUIRED rule (embedded at classification step):
  prove and listen are EVIDENCE-HEAVY. A synthetic artifact cannot substitute for real signal.
  prove-* requires actual experiment data or prototype outputs.
  listen-* requires real user interviews or adoption measurements.
  DO NOT apply any flag other than REAL-REQUIRED to EVIDENCE-HEAVY namespaces.

If {topic} has compliance tags in TOPICS.md: scout-compliance and trace-permissions are
Compliance-Tagged = YES regardless of structural quality.

**Do not begin PHASE 2 until all nine rows in the classification table are filled: each
namespace has an assigned Category, MUST use terms, DO NOT use terms, Tier 2/3 Critical value
(YES or NO), and Compliance-Tagged value (YES or NO).**

---

### PHASE 2 — GENERATE

For each namespace in table order, write a namespace section. Apply the MUST use and DO NOT
use rules from the Phase 1 row exactly. The artifact body should reflect the specific blind
spot this namespace fills for {topic} — what would be missing if this signal were absent.

  #### {Namespace} — {skill-name}

  **MOCK ARTIFACT**
  Skill:    {skill-name}
  Topic:    {topic}
  Category: {category from Phase 1}
  Date:     {date}
  Status:   MOCK (awaiting review)

  {artifact body — apply Phase 1 MUST use / DO NOT use; reflect what this namespace
   contributes to {topic}'s coverage and what would be absent without it}

For prove and listen: append after artifact body —
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal.
  {prove: requires actual experiment data or prototype outputs |
   listen: requires real user interviews or adoption measurements}.
DO NOT omit this statement for any EVIDENCE-HEAVY namespace.

**Do not begin PHASE 3 until all nine namespace sections are written, each with a complete
MOCK ARTIFACT header block, a vocabulary-compliant artifact body (MUST use satisfied; DO NOT
use not violated), and — for prove/listen — a REAL-REQUIRED statement.**

---

### PHASE 3 — SUMMARIZE

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
  REAL-REQUIRED  — all EVIDENCE-HEAVY namespaces, all tiers
  TIER-CRITICAL  — trace-*, scout-feasibility, listen-* at tier >= 2
  COMPLIANCE     — scout-compliance, trace-permissions when compliance context is active
  Multiple flags: REAL-REQUIRED + TIER-CRITICAL

Recommended Next Step: exact skill call that closes the specific blind spot this namespace
fills. DO NOT write "gather more signals." Write the exact skill identifier.
Example: `/scout:feasibility {topic}`

**Do not begin PHASE 4 until the coverage summary table is complete: all nine namespaces
appear with correct Category, all required Flags, and a named Recommended Next Step.**

---

### PHASE 4 — HANDOFF

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-{date}.md

Replace {topic} and {date} with actual values.
DO NOT write the placeholder string `{this-file}`.
DO NOT write any other content in this section.

---

## V-04 — Role Sequence + Lifecycle Emphasis (Combined)

**axes:** role-sequence + lifecycle-emphasis
**hypothesis:** V-01 tests role-sequence in isolation; R4 V-01/V-04 tested lifecycle-emphasis
(PHASE labels + enumerated gates) without role identity framing. V-04 combines both: PHASE
labels AND role identity declarations are present at each boundary. The hypothesis is that
role identity + phase labels are stronger together than either alone: the model is told both
WHAT IT IS (CLASSIFIER) and WHEN TO STOP (enumerated phase gate). This creates dual-channel
enforcement — identity and procedure — reducing the probability of premature artifact body
generation. The combination also tests whether role framing affects artifact body register
(C-15): a model that has adopted the CLASSIFIER identity in PHASE 1 may write more
specification-appropriate bodies in PHASE 2 when it adopts the GENERATOR identity.
**predicted:** C-11 PASS (dual enforcement: role identity + phase gate), C-14 PASS (explicit
gate phrases at all boundaries), C-16 PASS (gates enumerate five fields), C-17 PASS (vocab
columns in CLASSIFIER output), C-15 PASS (role identity reinforces vocabulary compliance
during generation). All 9 aspirational criteria PASS. Score: 100.
**failure condition:** Role labels and phase labels together produce cognitive redundancy
without additive structural enforcement — the model either ignores the role framing entirely
(role labels are ignored as decorative) or ignores the phase gates as redundant. If both
signals are present but neither adds beyond the other, the combined variation scores
identically to V-01 or R4 V-01 — correct, but offering no evidence of interaction effects.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record: tier for {topic}, compliance tags (if any).
State: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs four sequential phases, each with a named role. The role defines what you
produce in that phase. A phase may not produce output belonging to a later phase.

---

### PHASE 1 — CLASSIFY  [ROLE: CLASSIFIER]

As the CLASSIFIER, produce the classification table. You do not write artifact bodies.
You do not write coverage summaries. Classify only.

Categories:
  HIGH-STRUCTURE  — structural artifacts: specs, schemas, contracts, plans, state models
  EVIDENCE-HEAVY  — requires real signal; synthetic content is informational only
  MIXED           — structural scaffolding plus qualitative or narrative content

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged |
|-----------|----------|----------|------------|-------------------|-------------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language only OR pure study methodology framing | NO | YES if --compliance and TOPICS.md tags present; else NO |
| draft | MIXED | structural scaffold (sections, properties, acceptance criteria) plus qualitative observations | pure specification language only OR pure study methodology framing | NO | NO |
| review | MIXED | structural scaffold plus qualitative observations and design judgements | pure specification language only OR pure study methodology framing | NO | NO |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language, user quotes, adoption percentages, study framing | NO | NO |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language, adoption rates, user quotes, study framing | YES if tier >= 2; else NO | YES if --compliance and TOPICS.md tags; else NO |
| prove | EVIDENCE-HEAVY | study/data/interview language: "N of M tests showed...", "Prototype against {topic} produced...", hypothesis-and-result framing | specification language, schema definitions, contract structures | NO | NO |
| listen | EVIDENCE-HEAVY | study/data/interview language: adoption rates, "N users interviewed found...", survey response framing | specification language, state machine language, schema definitions | YES if tier >= 2; else NO | NO |
| program | MIXED | structural scaffold (milestones, owners, dependencies) plus qualitative rationale | pure specification language only OR pure study methodology framing | NO | NO |
| topic | MIXED | signal synthesis narrative plus structured coverage reference | pure specification language alone | NO | NO |

REAL-REQUIRED assignments:
- prove: EVIDENCE-HEAVY → REAL-REQUIRED. Rationale: A synthetic artifact cannot substitute
  for real signal; prove-* requires actual experiment data or prototype outputs.
- listen: EVIDENCE-HEAVY → REAL-REQUIRED. Rationale: A synthetic artifact cannot substitute
  for real signal; listen-* requires real user interviews or adoption measurements.
- scout-compliance (when compliance context active): REAL-REQUIRED. Compliance signals require
  traceable real-world sources; synthetic artifacts create false assurance.
- trace-permissions (when compliance context active): REAL-REQUIRED. Same rationale.

**PHASE 1 GATE: Do not begin PHASE 2 — GENERATE [ROLE: GENERATOR] until all nine rows in the
classification table have an assigned Category, MUST use terms, DO NOT use terms, Tier 2/3
Critical value (YES or NO), and Compliance-Tagged value (YES or NO).**

---

### PHASE 2 — GENERATE  [ROLE: GENERATOR]

As the GENERATOR, produce one synthetic artifact per namespace using the vocabulary rules
from PHASE 1's classification table. You do not re-classify. You do not write the coverage
summary. Generate only.

For each namespace in classification table order:

  #### {Namespace} — {skill-name}

  **MOCK ARTIFACT**
  Skill:    {skill-name}
  Topic:    {topic}
  Category: {category from PHASE 1}
  Date:     {date}
  Status:   MOCK (awaiting review)

  {artifact body — apply PHASE 1 MUST use and DO NOT use exactly for this namespace row}

For prove and listen: append after the artifact body —
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal.
  {prove: requires actual experiment data or prototype outputs |
   listen: requires real user interviews or adoption measurements}.
DO NOT omit this statement for any EVIDENCE-HEAVY namespace.

**PHASE 2 GATE: Do not begin PHASE 3 — SUMMARIZE [ROLE: SUMMARIZER] until all nine namespace
sections are written, each with a complete MOCK ARTIFACT header block, a vocabulary-compliant
artifact body (MUST use satisfied; DO NOT use not violated), and — for prove/listen — a
REAL-REQUIRED statement.**

---

### PHASE 3 — SUMMARIZE  [ROLE: SUMMARIZER]

As the SUMMARIZER, produce the coverage summary table. You do not add new artifacts. You do
not revise classifications. Summarize only.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
  REAL-REQUIRED  — all EVIDENCE-HEAVY namespaces (prove, listen), all tiers
  TIER-CRITICAL  — trace-*, scout-feasibility, listen-* at tier >= 2
  COMPLIANCE     — scout-compliance, trace-permissions when compliance context is active
  Multiple flags: REAL-REQUIRED + TIER-CRITICAL

Recommended Next Step: exact skill call — `/namespace:skill {topic}`.
DO NOT write "gather more signals" or generic advice.

**PHASE 3 GATE: Do not begin PHASE 4 — HANDOFF [ROLE: HANDOFF WRITER] until all nine
namespaces appear in the coverage table with correct Category, all required Flags, and a
named Recommended Next Step.**

---

### PHASE 4 — HANDOFF  [ROLE: HANDOFF WRITER]

As the HANDOFF WRITER, write only the handoff instruction. No artifact bodies. No table rows.
No additional commentary.

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-{date}.md

Replace {topic} and {date} with actual values.
DO NOT write `{this-file}` as a literal placeholder.
DO NOT write any other content in this section.

---

## V-05 — Role Sequence + Phrasing Register + Output Format (Combined)

**axes:** role-sequence + phrasing-register (conversational) + output-format (minimal skeleton)
**hypothesis:** This is the R5 full-ceiling combination. V-01 tests role-sequence (new axis).
V-02 tests conversational register (new isolation). V-05 combines both with minimal pre-printed
skeleton structure: the classification table stubs are pre-printed (enforcing C-11 via
structure), but artifact section stubs are instruction-generated not pre-printed (reducing
skeleton length vs R3 V-05). The conversational register makes each role feel like a natural
handoff: "You've just finished classifying. Now, as the GENERATOR, here's what you do next."
The role identity + conversational bridge + pre-printed table creates three concurrent C-11
enforcement mechanisms: structural (table precedes artifact sections), identity (role cannot
produce out-of-role content), and procedural (gate phrases). This tests whether the
combination of all three converges on stronger C-11 compliance than any single mechanism while
remaining leaner than full pre-printed skeleton (R3 V-05 / R4 V-05).
**predicted:** C-11 PASS (three concurrent mechanisms), C-14 PASS (explicit gate phrases
embedded in conversational transitions), C-16 PASS (gates enumerate five fields), C-17 PASS
(vocab columns in pre-printed table), C-07/C-10 quality expected improved by conversational
framing. All 9 aspirational criteria PASS. Score: 100.
**failure condition:** Three concurrent mechanisms produce conflicting signals. The model
interprets role identity, conversational bridges, and gate phrases as three overlapping
instructions for the same constraint, producing confusion about precedence and omitting one
mechanism's output. Artifact bodies may be shorter under combined cognitive load. If this
occurs, single-mechanism variations (V-01, V-02) are more reliable at the same rubric score.

---

You are running /mock:all for {topic}.

First, look up {topic} in TOPICS.md. Note its tier (1, 2, or 3 — default to 1 if not listed)
and any compliance tags. Write at the top of your output:
  `Tier: {N}  (source: TOPICS.md | --tier | default)`

Optional flags:
- --tier {1|2|3}: overrides tier from TOPICS.md
- --compliance: activates compliance pre-flagging

This skill runs four sequential roles. Each role has one job. Complete that job fully before
the next role takes over.

---

### PHASE 1  [ROLE: CLASSIFIER]

As the CLASSIFIER, your one job is to fill in the classification table. You are not the
GENERATOR yet — artifact bodies are not your concern. Classify all nine namespaces, then
hand off.

Fill this table completely. Every cell needs a value before you can move on.

Three categories:
- HIGH-STRUCTURE: structural artifacts — specs, schemas, contracts, state models
- EVIDENCE-HEAVY: requires real data; synthetic content here is informational only
- MIXED: combine structure with qualitative content; both elements required in every body

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged |
|-----------|----------|----------|------------|-------------------|-------------------|
| scout     | [assign] | [discovery language: signals, findings, open questions — fill in] | [pure spec only OR pure study only — fill in] | [YES / NO] | [YES / NO] |
| draft     | [assign] | [fill in] | [fill in] | [YES / NO] | [YES / NO] |
| review    | [assign] | [fill in] | [fill in] | [YES / NO] | [YES / NO] |
| flow      | [assign] | [fill in] | [fill in] | [YES / NO] | [YES / NO] |
| trace     | [assign] | [fill in] | [fill in] | [YES / NO] | [YES / NO] |
| prove     | [assign] | [fill in] | [fill in] | [YES / NO] | [YES / NO] |
| listen    | [assign] | [fill in] | [fill in] | [YES / NO] | [YES / NO] |
| program   | [assign] | [fill in] | [fill in] | [YES / NO] | [YES / NO] |
| topic     | [assign] | [fill in] | [fill in] | [YES / NO] | [YES / NO] |

Category reference (use this when filling in the table):
- scout, draft, review, program, topic: MIXED
- flow, trace: HIGH-STRUCTURE
- prove, listen: EVIDENCE-HEAVY

Vocabulary reference (use this when filling in MUST use / DO NOT use):
- MIXED MUST: discovery language (signals, findings, open questions) + structural scaffold.
  DO NOT: pure specification language only OR pure study methodology framing.
- HIGH-STRUCTURE MUST: specification language (interfaces, contracts, state transitions,
  schema shapes, config keys). DO NOT: interview language, user quotes, adoption rates,
  study framing.
- EVIDENCE-HEAVY MUST: study/data/interview language ("N of M tests showed...", adoption
  rates, "N users interviewed found..."). DO NOT: specification language, schema definitions,
  contract structures.

Tier 2/3 Critical (YES when tier >= 2): trace-*, scout-feasibility, listen-*
Compliance-Tagged (YES when --compliance or TOPICS.md tags active): scout-compliance,
trace-permissions

REAL-REQUIRED applies to prove and listen — always. Rationale: A synthetic artifact cannot
substitute for real signal. prove-* needs actual experiment data; listen-* needs real user
interviews or adoption measurements. If compliance context is active, also apply to
scout-compliance and trace-permissions.

Once every cell in that table is filled — all nine rows, all six columns — you're ready to
hand off to the GENERATOR. Not before.

**Stop. Do not write any artifact body until all nine rows in the classification table have
a Category, MUST use terms, DO NOT use terms, Tier 2/3 Critical value, and Compliance-Tagged
value.**

---

### PHASE 2  [ROLE: GENERATOR]

You've just finished classifying. Now, as the GENERATOR, your one job is to write a synthetic
artifact for each namespace using the vocabulary rules you just filled in. You're not the
SUMMARIZER yet — the coverage table is not your concern.

For each namespace in table order, write:

  #### {Namespace} — {skill-name}

  **MOCK ARTIFACT**
  Skill:    {skill-name}
  Topic:    {topic}
  Category: {from PHASE 1}
  Date:     {date}
  Status:   MOCK (awaiting review)

  {3-5 sentence artifact body — use only the MUST vocabulary from your PHASE 1 row; do not
   use anything in the DO NOT column}

A reminder of what each category needs:
- HIGH-STRUCTURE: stay in specification language. No user quotes, no adoption numbers.
- EVIDENCE-HEAVY: stay in study/interview language. No spec language, no contracts.
- MIXED: include at least one structural element (table, list, named property) AND at least
  one qualitative observation.

For prove and listen, add this after the body:
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal.
  {prove: actual experiment data or prototype outputs |
   listen: real user interviews or adoption measurements}.

Once all nine sections are written — complete headers, vocabulary-compliant bodies,
REAL-REQUIRED statements for prove/listen — hand off to the SUMMARIZER.

**Stop. Do not write the coverage summary until all nine namespace sections are complete,
each with a full MOCK ARTIFACT header block, a vocabulary-compliant body, and (for
prove/listen) a REAL-REQUIRED statement.**

---

### PHASE 3  [ROLE: SUMMARIZER]

You've generated all nine artifacts. Now, as the SUMMARIZER, your one job is to produce the
coverage summary. Don't add new artifacts or revise anything. Summarize.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

For Flag:
- REAL-REQUIRED: prove, listen (all tiers)
- TIER-CRITICAL: trace-*, scout-feasibility, listen-* when tier >= 2
- COMPLIANCE: scout-compliance, trace-permissions when compliance context is active
- Multiple: REAL-REQUIRED + TIER-CRITICAL

For Recommended Next Step: write the exact skill call, like `/trace:component {topic}` or
`/prove:prototype {topic}`. Not "gather more signals" — the exact skill identifier.

Once all nine rows are in the summary with correct flags and named next steps, hand off to
the HANDOFF WRITER.

**Stop. Do not write the handoff until the coverage summary has all nine namespaces, correct
flags, and a named Recommended Next Step for each.**

---

### PHASE 4  [ROLE: HANDOFF WRITER]

You've summarized the coverage picture. Now, as the HANDOFF WRITER, your one job is to write
the handoff instruction. Nothing else goes in this section.

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-{date}.md

Replace {topic} and {date} with actual values.
DO NOT write `{this-file}` as a placeholder.
DO NOT write any other content in this section.
