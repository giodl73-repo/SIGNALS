---
skill: quest-variate
skill_target: mock-all
date: 2026-03-15
round: 4
rubric_version: v4
status: VARIATE
---

# mock-all Variate — Round 4

**Date:** 2026-03-15
**Skill:** mock-all
**Rubric:** v4 (C-01 through C-17; aspirational denominator = 9)
**Round:** R4 — targeting v4 new criteria (C-16, C-17)

---

## What R3 Left Open

R3 five variations all scored GOLDEN (97.9–100) under v3 rubric. V-01 and V-05 tied at the
ceiling. The v4 rubric adds two new aspirational criteria derived from R3's new patterns:

| Criterion | R3 best coverage | Gap under v4 |
|-----------|-----------------|--------------|
| C-16 — Stop-gate completeness specification | V-01/V-04/V-05: gates enumerate named fields (Category, Tier 2/3 Critical, Compliance-Tagged). V-02/V-03: no gate sentences. | V-01 PASS; V-05 PASS (enumerates vocabulary columns too); V-02/V-03 FAIL; V-04 PASS. |
| C-17 — Vocabulary-column anchoring | V-05: MUST/DO NOT as table columns. V-03: MUST/DO NOT as table columns (instruction-based). Others: vocabulary rules in separate blocks. | V-05 PASS; V-03 PASS; V-01/V-02/V-04 FAIL. |

Applying v4 retroactively to R3 variations:

| Variation | C-14 | C-15 | C-16 | C-17 | v4 Score |
|-----------|------|------|------|------|----------|
| R3 V-01 | PASS | PASS | PASS | FAIL | 98.9 |
| R3 V-02 | FAIL | PARTIAL | FAIL | FAIL | 96.7 |
| R3 V-03 | FAIL | PASS | FAIL | PASS | 97.8 |
| R3 V-04 | PASS | PARTIAL | PASS | FAIL | 98.9 |
| R3 V-05 | PASS | PASS | PASS | PASS | 100.0 |

R3 V-05 already achieves 100 under v4 by design. R4 targets three open questions:

1. Can a leaner instruction-based path (no pre-printed skeleton) close C-17 via vocabulary
   columns and also satisfy C-16 via enumerated stop-gates?
2. Does inertia framing (new axis, untested in R1–R3) improve C-07 artifact body depth or
   C-10 next-step specificity?
3. Is the instruction-based path (V-01/V-02 R4) as structurally reliable as V-05's pre-printed
   skeleton for achieving C-16 + C-17 simultaneously?

---

## Axis-Assignment Plan

| Variation | Axis | Source signal | Target criteria | Predicted |
|-----------|------|---------------|-----------------|-----------|
| V-01 | output-format | C-17 gap: R3 V-01 had vocabulary in a separate PHASE 2 block, not table columns; adding MUST/DO NOT as table columns with enumerated stop-gate closes C-17 without skeleton weight | C-17, C-16 (enumerated gate) | 100 — vocabulary columns close C-17; enumerated gate with five named fields closes C-16 |
| V-02 | lifecycle-emphasis | C-16 + C-17 gap: R3 V-03 had vocabulary columns (C-17 PASS) but step-label ordering without gate sentences (C-14/C-16 FAIL); adding explicit "Do not begin STEP N+1 until [enumerated fields]" sentences closes C-14 and C-16 while preserving C-17 | C-14, C-16, C-17 | 100 — adds enumerated gate sentences to V-03 R3's vocabulary-column structure |
| V-03 | inertia-framing | New axis untested in R1–R3: opening "status quo" block describes what teams do without /mock:all (commit on 1-2 signals, miss blind spots), priming richer artifact bodies and sharper next-step calls. No vocabulary columns — C-17 not targeted. | C-07 (deeper), C-10 (sharper) | 98.9 — inertia framing does not close C-17; vocabulary rules stay in prose block |
| V-04 | output-format + lifecycle-emphasis | Combine V-01 vocabulary columns (C-17) with V-02 enumerated stop-gates (C-16) using instruction-based structure — leaner than V-05's pre-printed skeleton. Minimal path to v4 ceiling. | C-16, C-17 | 100 — both new criteria closed at minimal skeleton weight |
| V-05 | output-format + lifecycle-emphasis + inertia-framing | Full ceiling: vocabulary columns + enumerated stop-gates + inertia framing. Tests whether inertia framing improves C-07/C-10 output quality on top of a 100-scoring base without degrading any criterion. | C-16, C-17, C-07, C-10 | 100 — all new criteria pass; inertia framing may improve unmeasured execution quality |

---

## V-01 — Vocabulary-Column Anchoring (Single-Axis: Output Format)

**axis:** output-format
**hypothesis:** R3 V-01 embedded vocabulary rules in a PHASE 2 prose block — visible during
generation but not co-located with category assignment. C-17 requires MUST/DO NOT rules as
columns in the classification table, co-located with the category assignment step. Adding
vocabulary columns to V-01's existing instruction-based structure (with enumerated stop-gate
sentences already present) closes C-17 without adding pre-printed skeleton weight. The C-16
gate is upgraded to enumerate all five column types (Category, MUST use, DO NOT use, Tier 2/3
Critical, Compliance-Tagged), making the completeness check self-verifiable per column.
**predicted:** C-16 PASS (five-field enumeration), C-17 PASS (vocabulary columns in table),
C-14/C-15 maintained. Score: 100.
**failure condition:** Model fills vocabulary columns with [per-category] placeholders rather
than actual terms, producing a table that satisfies C-17 structurally but fails C-15 in
execution because the per-namespace vocabulary rules are too generic to enforce register.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier for {topic} and any compliance tags.
State: `Tier: {N}  (source: TOPICS.md | --tier | default)`

---

### PHASE 1 — CLASSIFY

Assign every namespace to exactly one category. Output the classification table — including
vocabulary rule columns — before writing any artifact body.

Categories:
  HIGH-STRUCTURE  — structural artifacts: specs, schemas, contracts, plans, state models
  EVIDENCE-HEAVY  — requires real signal; synthetic content is informational only
  MIXED           — structural scaffolding plus qualitative or narrative content

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged |
|-----------|----------|----------|------------|-------------------|-------------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language only OR pure study methodology framing | NO | YES if --compliance and TOPICS.md tags present; else NO |
| draft | MIXED | structural scaffold plus qualitative observations | pure specification language only OR pure study methodology framing | NO | NO |
| review | MIXED | structural scaffold plus qualitative observations and judgements | pure specification language only OR pure study methodology framing | NO | NO |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language, user quotes, adoption percentages, study framing | NO | NO |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language, adoption rates, user quotes, study framing | YES if tier >= 2; else NO | YES if --compliance and TOPICS.md tags present; else NO |
| prove | EVIDENCE-HEAVY | study/data/interview language: "N of M tests showed...", "Prototype against {topic} produced...", hypothesis-and-result framing | specification language, schema definitions, contract structures | NO | NO |
| listen | EVIDENCE-HEAVY | study/data/interview language: adoption rates, "N users interviewed found...", survey response framing | specification language, state machine language, schema definitions | YES if tier >= 2; else NO | NO |
| program | MIXED | structural scaffold (milestones, owners, dependencies) plus qualitative rationale | pure specification language only OR pure study methodology framing | NO | NO |
| topic | MIXED | signal synthesis narrative plus structured coverage reference | pure specification language | NO | NO |

REAL-REQUIRED rule: every EVIDENCE-HEAVY namespace (prove, listen) receives the REAL-REQUIRED
flag. A synthetic artifact cannot substitute for real signal in EVIDENCE-HEAVY namespaces.
prove-* requires actual experiment data or prototype outputs.
listen-* requires real user interviews or adoption measurements.
DO NOT assign any flag other than REAL-REQUIRED to EVIDENCE-HEAVY namespaces.

If {topic} has compliance tags in TOPICS.md, set scout-compliance and trace-permissions rows
to Compliance-Tagged = YES regardless of structural quality.

**Do not begin PHASE 2 until every cell in the classification table is filled: all nine
namespaces have an assigned Category, MUST use terms, DO NOT use terms, Tier 2/3 Critical
value (YES or NO), and Compliance-Tagged value (YES or NO).**

---

### PHASE 2 — GENERATE

For each namespace in classification table order, write a namespace section. Apply the MUST use
and DO NOT use rules from the Phase 1 table row exactly.

  ### {Namespace} — {skill-name}

  **MOCK ARTIFACT**
  Skill:    {skill-name}
  Topic:    {topic}
  Category: {category from Phase 1}
  Date:     {date}
  Status:   MOCK (awaiting review)

  {artifact body — vocabulary-compliant per Phase 1 MUST use / DO NOT use columns}

For prove and listen: append after the artifact body —
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal.
  prove-*: requires actual experiment data or prototype outputs.
  listen-*: requires real user interviews or adoption measurements.

**Do not begin PHASE 3 until all nine namespace sections are written, each with a complete
MOCK ARTIFACT header block, a vocabulary-compliant artifact body (MUST use satisfied, DO NOT
use not violated), and — for prove and listen — a REAL-REQUIRED statement.**

---

### PHASE 3 — SUMMARIZE

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
  REAL-REQUIRED  — every EVIDENCE-HEAVY namespace, all tiers
  TIER-CRITICAL  — trace-*, scout-feasibility, listen-* at tier >= 2
  COMPLIANCE     — scout-compliance, trace-permissions when compliance context is active
  Multiple flags: REAL-REQUIRED + TIER-CRITICAL

Recommended Next Step: exact skill call. DO NOT write "gather more signals."
Example: `/trace:component {topic}`

**Do not begin PHASE 4 until the coverage summary table is complete: all nine namespaces appear
with correct Category, all required Flags, and a named Recommended Next Step.**

---

### PHASE 4 — HANDOFF

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-{date}.md

Replace {topic} and {date} with actual values.
DO NOT write the literal placeholder string `{this-file}`.
DO NOT write any other content in this section.

---

## V-02 — Enumerated Stop-Gates on Vocabulary-Column Table (Single-Axis: Lifecycle Emphasis)

**axis:** lifecycle-emphasis
**hypothesis:** R3 V-03 had MUST/DO NOT vocabulary as table columns (C-17 PASS) but used
step-label ordering without gate sentences — C-14 FAIL, C-16 FAIL. Adding explicit "Do not
begin STEP N+1 until [named fields] are complete" sentences at every STEP boundary upgrades
V-03 R3 to satisfy C-14 and C-16 while preserving C-17. The gate at STEP 1→2 enumerates all
five column types: "assigned category, MUST use terms, DO NOT use terms, Tier 2/3 Critical
value, Compliance-Tagged value" — making the gate field-specific per C-16. Uses STEP labeling
(V-03 R3's register) rather than PHASE labeling to test whether label style affects compliance.
**predicted:** C-14 PASS (gate sentences at all step boundaries), C-16 PASS (five-field gate
enumeration), C-17 PASS (vocabulary columns in table), C-15 maintained. Score: 100.
**failure condition:** STEP labels (vs PHASE labels) weaken the model's association with
procedural ordering; model treats STEP boundaries as advisory rather than sequential gates
even with explicit sentences — C-14 fails in execution while the gate sentences are present in
the prompt. If this occurs, PHASE labeling (V-01/V-04 R4) is a stronger signal than STEP.

---

You are running /mock:all.

INPUTS:
  topic:      {topic}
  tier:       {1|2|3} — from TOPICS.md, --tier flag, or default 1
  compliance: --compliance (if provided)

Read TOPICS.md. Record: tier for {topic}, compliance tags (if any).
State: `Tier: {N}  (source: TOPICS.md | --tier | default)`

---

STEP 1 — CLASSIFY ALL NAMESPACES

Before writing any artifact body, assign every namespace to a category.
Output the classification table with vocabulary rule columns:

Categories:
  HIGH-STRUCTURE — structural artifacts: specs, schemas, contracts, plans, state models
  EVIDENCE-HEAVY — requires real signal; synthetic content cannot substitute
  MIXED          — structural scaffolding plus qualitative or narrative content

| Namespace | Assigned Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged |
|-----------|-------------------|----------|------------|-------------------|-------------------|
| scout | MIXED | discovery language: signals, findings, open questions | pure specification only OR pure study methodology | NO | YES if compliance context; else NO |
| draft | MIXED | structural scaffold plus qualitative observations | pure specification only OR pure study methodology | NO | NO |
| review | MIXED | structural scaffold plus qualitative observations and judgements | pure specification only OR pure study methodology | NO | NO |
| flow | HIGH-STRUCTURE | spec language: state transitions, trigger conditions, data flow contracts | interview language, user quotes, adoption rates | NO | NO |
| trace | HIGH-STRUCTURE | spec language: interfaces, component boundaries, contracts, state transitions | interview language, study framing, adoption percentages | YES if tier >= 2; else NO | YES if compliance context; else NO |
| prove | EVIDENCE-HEAVY | study/data/interview language: "N of M tests showed...", prototype results, hypothesis framing | specification language, contract structures, schema definitions | NO | NO |
| listen | EVIDENCE-HEAVY | study/data/interview language: adoption rates, interview quotes, survey response framing | specification language, state machine language | YES if tier >= 2; else NO | NO |
| program | MIXED | structural scaffold (milestones, owners, dependencies) plus qualitative rationale | pure specification only OR pure study methodology | NO | NO |
| topic | MIXED | signal synthesis narrative plus structured coverage reference | pure specification language | NO | NO |

REAL-REQUIRED rule: every EVIDENCE-HEAVY namespace receives the REAL-REQUIRED flag.
  A synthetic artifact cannot substitute for real signal in EVIDENCE-HEAVY namespaces.
  prove-* requires actual experiment data or prototype outputs.
  listen-* requires real user interviews or adoption measurements.
  DO NOT assign any flag other than REAL-REQUIRED to EVIDENCE-HEAVY namespaces.

If {topic} has compliance tags in TOPICS.md: set scout-compliance and trace-permissions to
Compliance-Tagged = YES regardless of structural quality.

**Do not begin STEP 2 until all nine namespaces in the classification table have an assigned
category, MUST use terms, DO NOT use terms, Tier 2/3 Critical value (YES or NO), and
Compliance-Tagged value (YES or NO).**

---

STEP 2 — GENERATE ARTIFACT BODIES

For each namespace, write a namespace section. Apply the MUST use and DO NOT use rules from
Step 1 exactly. Every artifact body MUST comply with both vocabulary columns for its row.

Section format:

  ### {Namespace} — {skill-name}

  **MOCK ARTIFACT**
  Skill:    {skill-name}
  Topic:    {topic}
  Category: {category from Step 1}
  Date:     {date}
  Status:   MOCK (awaiting review)

  {artifact body — vocabulary-compliant per Step 1 MUST use / DO NOT use columns}

For prove and listen: append after the artifact body —
  REAL-REQUIRED applied: EVIDENCE-HEAVY — A synthetic artifact cannot substitute for real
  signal. {prove: actual experiment data or prototype outputs | listen: real user interviews
  or adoption measurements}.
DO NOT omit this statement for any EVIDENCE-HEAVY namespace.
DO NOT use specification language in any EVIDENCE-HEAVY artifact body.

**Do not begin STEP 3 until all nine namespace sections are written, each with a complete
MOCK ARTIFACT header block, a vocabulary-compliant artifact body, and — for prove/listen — a
REAL-REQUIRED applied statement.**

---

STEP 3 — WRITE COVERAGE SUMMARY

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
  REAL-REQUIRED  — every EVIDENCE-HEAVY namespace, all tiers
  TIER-CRITICAL  — trace-*, scout-feasibility, listen-* at tier >= 2
  COMPLIANCE     — scout-compliance, trace-permissions when compliance context active
  Multiple flags: REAL-REQUIRED + TIER-CRITICAL

Recommended Next Step: exact skill call — `/skill:subskill {topic}`
DO NOT write "run the real skill." DO NOT write generic advice.

**Do not begin STEP 4 until the coverage summary table is complete: all nine namespaces appear
with correct Category, all required Flags, and a named Recommended Next Step.**

---

STEP 4 — HANDOFF

Write this section only. No artifact bodies, no table rows, no other content.

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-{date}.md

MUST replace {topic} and {date} with actual values.
DO NOT write the placeholder string `{this-file}`.
DO NOT write any other content in this section.

---

## V-03 — Inertia Framing (Single-Axis: New Axis)

**axis:** inertia-framing
**hypothesis:** New axis untested in R1–R3. Adding a "status quo" block before Phase 1 —
describing what teams do without /mock:all (commit on 1-2 signals, miss blind spots in
EVIDENCE-HEAVY and Tier 2/3 namespaces, mistake synthetic content for real evidence) — primes
richer artifact bodies (C-07) and sharper Recommended Next Step calls (C-10). The mechanism:
the model writes artifact bodies not as generic templates but as explicit answers to "what
blind spot does this namespace fill?" This variation does NOT add vocabulary columns to the
classification table — C-17 is intentionally not targeted, isolating the inertia framing
effect. C-14 and C-15 are maintained via standard stop-gate sentences and prose vocabulary
rules. The variation tests whether inertia framing alone can improve observable output quality
without structural changes.
**predicted:** C-14 PASS, C-15 PASS, C-16 PASS (gate enumerates Category, Tier 2/3 Critical,
Compliance-Tagged), C-17 FAIL (no vocabulary columns in table). Score: 98.9.
**failure condition:** Inertia framing adds prompt length without changing artifact body depth
— C-07 does not improve, making the inertia framing a cost with no measured benefit. If this
occurs, the finding is that context-setting does not improve generation quality under rubric
criteria; structural mechanisms (V-01/V-04 R4) are the only reliable path to higher scores.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier for {topic} and any compliance tags.
State: `Tier: {N}  (source: TOPICS.md | --tier | default)`

---

### STATUS QUO — What happens without this skill

Teams typically commit to features on 1-2 signals: a draft proposal and a design review.
The blind spots that cause late-stage rework cluster in two places:

1. EVIDENCE-HEAVY namespaces (prove, listen) — synthetic content is generated and treated as
   real evidence. The gap surfaces at launch when adoption or prototype results diverge from
   mock expectations.
2. Tier 2/3 critical namespaces (trace, scout-feasibility, listen) — underweighted at early
   stages, producing false confidence that collapses when implementation surfaces the missing
   contract, feasibility constraint, or user signal.

/mock:all maps the full 9-namespace coverage picture before any real signal investment. The
output answers: which namespaces have structural artifacts that are safe to generate
synthetically, which require real signal before commitment, and what the specific next action
is for each gap.

Each artifact body in this output should reflect what this namespace uniquely contributes to
{topic}'s coverage — what would be missing if this signal were absent.

---

### PHASE 1 — CLASSIFY

Assign every namespace to exactly one category before writing any artifact body.

Categories:
  HIGH-STRUCTURE  — structural artifacts: specs, schemas, contracts, plans, state models
  EVIDENCE-HEAVY  — requires real signal; synthetic content is informational only
  MIXED           — structural scaffolding plus qualitative or narrative content

Namespaces: scout, draft, review, flow, trace, prove, listen, program, topic

Output the classification table:

| Namespace | Category | Tier 2/3 Critical | Compliance-Tagged |
|-----------|----------|-------------------|-------------------|

Tier 2/3 critical (YES when tier >= 2): trace-*, scout-feasibility, listen-*
Compliance-tagged (YES when --compliance or TOPICS.md tags): scout-compliance, trace-permissions

Vocabulary rules by category (applied during Phase 2):
  HIGH-STRUCTURE: MUST use specification language (interfaces, data contracts, state
    transitions, configuration keys, schema fields, deployment constraints). DO NOT use
    interview language, user quotes, adoption percentages, or study framing.
  EVIDENCE-HEAVY: MUST use study/data/interview language ("N of M interviews showed...",
    "Prototype against {topic} produced...", "Week-1 adoption rate was [N]%"). DO NOT use
    specification language, contract structures, or schema definitions.
  MIXED: MUST include at least one structural element (table, list, or named property) AND at
    least one qualitative observation. DO NOT use pure specification language alone OR pure
    study framing alone.

REAL-REQUIRED rule: every EVIDENCE-HEAVY namespace receives the REAL-REQUIRED flag.
  Rationale: A synthetic artifact cannot substitute for real signal. prove-* requires actual
  experiment data or prototype outputs. listen-* requires real user interviews or adoption
  measurements.

**Do not begin PHASE 2 until the classification table is complete and all nine namespaces have
an assigned Category, a Tier 2/3 Critical value (YES or NO), and a Compliance-Tagged value
(YES or NO).**

---

### PHASE 2 — GENERATE

For each namespace in classification table order, write a namespace section. Apply vocabulary
rules from Phase 1. The artifact body should address the specific blind spot this namespace
fills for {topic} — not a generic template.

  ### {Namespace} — {skill-name}

  **MOCK ARTIFACT**
  Skill:    {skill-name}
  Topic:    {topic}
  Category: {category from Phase 1}
  Date:     {date}
  Status:   MOCK (awaiting review)

  {artifact body — vocabulary-compliant per Phase 1; reflects what this namespace contributes
   to {topic}'s coverage and what would be missing without it}

Vocabulary compliance:
- HIGH-STRUCTURE (flow, trace): DO NOT use interview language, user quotes, or adoption rates.
- EVIDENCE-HEAVY (prove, listen): DO NOT use specification language, schema definitions, or
  contract structures.
- MIXED: include both a structural element and a qualitative observation. Both required.
- prove and listen: append — REAL-REQUIRED: A synthetic artifact cannot substitute for real
  signal. {prove: actual experiment data | listen: real user interviews or adoption measurements}.

**Do not begin PHASE 3 until all nine namespace sections are written with complete MOCK ARTIFACT
header blocks and category-appropriate artifact bodies.**

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

Recommended Next Step: exact skill call that turns this mock into real signal for {topic}.
The next step should close the specific blind spot this namespace covers.
DO NOT write "gather more signals." Write the exact skill identifier.
Example: `/listen:adoption {topic}`

**Do not begin PHASE 4 until the coverage summary table is complete and all nine namespaces
appear with correct Flags and named Recommended Next Steps.**

---

### PHASE 4 — HANDOFF

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-{date}.md

Replace {topic} and {date} with actual values.
DO NOT write the placeholder string `{this-file}`.

---

## V-04 — Vocabulary Columns + Enumerated Gates (Combined: Output Format + Lifecycle)

**axes:** output-format + lifecycle-emphasis
**hypothesis:** V-01 R4 closes C-17 via vocabulary columns with enumerated stop-gate (C-16).
V-02 R4 closes C-14/C-16 via enumerated gates on V-03 R3's vocabulary-column table. V-04
combines both mechanisms in a unified instruction-based structure — the minimal path to the v4
ceiling without pre-printed skeleton. The classification table has MUST/DO NOT columns (C-17);
the gate at CLASSIFY→GENERATE enumerates all five column types (C-16); stop-gate sentences
appear at all three phase boundaries (C-14). This is a leaner path than R3 V-05's pre-printed
skeleton, testing whether instruction-based enforcement achieves the same structural guarantee.
**predicted:** C-14 PASS, C-15 PASS, C-16 PASS, C-17 PASS. Score: 100.
**failure condition:** Without structural pre-printing, the model may generate artifact body
content before completing the vocabulary columns in the classification table — C-11 passes at
the instruction level but fails in execution. The instruction "Do not write artifact body
content before completing PHASE 1" must suppress generation reliably; if it does not, R3 V-05's
pre-printed skeleton is still the stronger structural guarantee.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier for {topic} and any compliance tags.
State: `Tier: {N}  (source: TOPICS.md | --tier | default)`

---

### PHASE 1 — CLASSIFY

Assign every namespace to a category. The classification table — with vocabulary rule columns —
must be fully completed before any artifact body is written.

Categories:
  HIGH-STRUCTURE  — structural artifacts: specs, schemas, contracts, plans, state models
  EVIDENCE-HEAVY  — requires real signal; synthetic content is informational only
  MIXED           — structural scaffolding plus qualitative or narrative content

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged |
|-----------|----------|----------|------------|-------------------|-------------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure-spec language only OR pure study methodology framing | NO | YES if compliance context; else NO |
| draft | MIXED | structural scaffold plus qualitative observations | pure-spec language only OR pure study methodology framing | NO | NO |
| review | MIXED | structural scaffold plus qualitative observations | pure-spec language only OR pure study methodology framing | NO | NO |
| flow | HIGH-STRUCTURE | spec language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language, user quotes, adoption percentages, study framing | NO | NO |
| trace | HIGH-STRUCTURE | spec language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language, adoption rates, user quotes, study framing | YES if tier >= 2; else NO | YES if compliance context; else NO |
| prove | EVIDENCE-HEAVY | study/data/interview language: "N of M tests showed...", "Prototype against {topic} produced...", hypothesis-and-result framing | spec language, schema definitions, contract structures | NO | NO |
| listen | EVIDENCE-HEAVY | study/data/interview language: adoption rates, interview quotes, survey response framing | spec language, state machine language, schema definitions | YES if tier >= 2; else NO | NO |
| program | MIXED | structural scaffold (milestones, owners, dependencies) plus qualitative rationale | pure-spec language only OR pure study methodology framing | NO | NO |
| topic | MIXED | signal synthesis narrative plus structured coverage reference | pure specification language | NO | NO |

REAL-REQUIRED rule (embedded at classification step, applied throughout):
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

For each namespace in table order, write a namespace section. Apply the MUST use and DO NOT use
rules from the Phase 1 row exactly.

  ### {Namespace} — {skill-name}

  **MOCK ARTIFACT**
  Skill:    {skill-name}
  Topic:    {topic}
  Category: {category from Phase 1}
  Date:     {date}
  Status:   MOCK (awaiting review)

  {artifact body — apply Phase 1 MUST use / DO NOT use for this namespace row}

For prove and listen: append after body —
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal.
  prove-*: requires actual experiment data or prototype outputs.
  listen-*: requires real user interviews or adoption measurements.

**Do not begin PHASE 3 until all nine namespace sections are written, each with a complete
MOCK ARTIFACT header block, a vocabulary-compliant artifact body (MUST use satisfied, DO NOT
use not violated), and — for prove/listen — a REAL-REQUIRED statement.**

---

### PHASE 3 — SUMMARIZE

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
  REAL-REQUIRED  — every EVIDENCE-HEAVY namespace, all tiers
  TIER-CRITICAL  — trace-*, scout-feasibility, listen-* at tier >= 2
  COMPLIANCE     — scout-compliance, trace-permissions when compliance context is active
  Multiple flags: REAL-REQUIRED + TIER-CRITICAL

Recommended Next Step: exact skill call — `/skill:subskill {topic}`
DO NOT write "gather more signals" or "run the real skill." Write the exact identifier.

**Do not begin PHASE 4 until the coverage summary table is complete: all nine namespaces appear
with a Category, all required Flags (REAL-REQUIRED for EVIDENCE-HEAVY; TIER-CRITICAL where
applicable; COMPLIANCE where active), and a named Recommended Next Step.**

---

### PHASE 4 — HANDOFF

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-{date}.md

Replace {topic} and {date} with actual values.
DO NOT write the literal placeholder string `{this-file}`.
DO NOT write any other content in this section.

---

## V-05 — Vocabulary Columns + Enumerated Gates + Inertia Framing (Combined: All Three Axes)

**axes:** output-format + lifecycle-emphasis + inertia-framing
**hypothesis:** V-04 R4 achieves 100 under v4 via vocabulary columns (C-17) and enumerated
stop-gates (C-16). V-05 adds inertia framing — a status-quo context block that primes the
model to produce artifact bodies that address specific blind spots rather than generic template
content. The three axes are orthogonal: output-format governs table structure, lifecycle
governs phase sequencing, inertia-framing governs semantic priming. Combining them tests
whether inertia framing improves C-07 depth and C-10 specificity on top of a base that already
scores 100. The inertia block names the two failure patterns teams face without /mock:all
(EVIDENCE-HEAVY content mistaken for real signal; Tier 2/3 namespaces skipped) so artifact
body generation is anchored to what each namespace distinctively contributes.
**predicted:** All 9 aspirational criteria PASS. Score: 100. C-07 and C-10 may show
improvement in execution vs V-04 due to inertia priming — but unmeasurable under current
rubric criteria.
**failure condition:** Inertia framing and vocabulary columns together push prompt length past
the threshold where the model abbreviates artifact bodies to compensate. C-07 degrades
(shorter, shallower bodies) while all structural criteria pass. If this occurs, V-04 achieves
the same rubric score at less cognitive load — inertia framing is a cost.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier for {topic} and any compliance tags.
State: `Tier: {N}  (source: TOPICS.md | --tier | default)`

---

### CONTEXT — What this skill replaces

Without /mock:all, teams commit to features on 1-2 signals. Two failure patterns cause late
rework:

1. EVIDENCE-HEAVY namespaces (prove, listen) are filled with synthetic content treated as real
   evidence. The gap surfaces at launch when prototype data or adoption rates diverge from mock
   expectations. Synthetic content in these namespaces is informational only — not a substitute
   for the real signal.

2. Tier 2/3 critical namespaces (trace, scout-feasibility, listen) are skipped under time
   pressure, creating false confidence. The missing contract, feasibility constraint, or user
   signal surfaces during implementation at much higher cost to fix.

/mock:all maps all nine namespaces in one pass. The output shows: which namespaces produce
structural artifacts safe to generate synthetically, which require real signal before commitment,
and the exact skill call that closes each gap. Each artifact body in this output should reflect
the specific blind spot its namespace fills — not generic template content.

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
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes, boundary conditions | interview language, user quotes, adoption percentages, study framing | NO | NO |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys, deployment constraints | interview language, adoption rates, user quotes, study framing | YES if tier >= 2; else NO | YES if --compliance and TOPICS.md tags; else NO |
| prove | EVIDENCE-HEAVY | study/data/interview language: "N of M tests showed...", "Prototype against {topic} produced...", hypothesis-and-result framing | specification language, schema definitions, contract structures | NO | NO |
| listen | EVIDENCE-HEAVY | study/data/interview language: adoption rates, "N users interviewed found...", survey response framing | specification language, state machine language, schema definitions | YES if tier >= 2; else NO | NO |
| program | MIXED | structural scaffold (milestones, owners, dependencies) plus qualitative rationale | pure specification language only OR pure study methodology framing | NO | NO |
| topic | MIXED | signal synthesis narrative plus structured coverage reference (which namespaces have real vs mock signal) | pure specification language | NO | NO |

REAL-REQUIRED rule (embedded at classification step, enforced at generation and summary):
  prove and listen are EVIDENCE-HEAVY. A synthetic artifact cannot substitute for real signal.
  prove-* requires actual experiment data or prototype outputs.
  listen-* requires real user interviews or adoption measurements.
  DO NOT apply any flag other than REAL-REQUIRED to EVIDENCE-HEAVY namespaces.
  DO NOT use specification language in any EVIDENCE-HEAVY artifact body — this violates the
  DO NOT use rule for that category.

If {topic} has compliance tags in TOPICS.md: set scout-compliance and trace-permissions to
Compliance-Tagged = YES regardless of structural quality.

**Do not begin PHASE 2 until all nine rows in the classification table are filled: each
namespace has an assigned Category, MUST use terms, DO NOT use terms, Tier 2/3 Critical value
(YES or NO), and Compliance-Tagged value (YES or NO).**

---

### PHASE 2 — GENERATE

For each namespace in table order, write a namespace section. Apply the MUST use and DO NOT
use rules from the Phase 1 row. The artifact body should reflect the specific blind spot this
namespace fills for {topic}: what would be missing from the coverage picture without it?

  ### {Namespace} — {skill-name}

  **MOCK ARTIFACT**
  Skill:    {skill-name}
  Topic:    {topic}
  Category: {category from Phase 1}
  Date:     {date}
  Status:   MOCK (awaiting review)

  {artifact body — vocabulary-compliant per Phase 1 table row; addresses the specific coverage
   gap this namespace fills for {topic}}

Vocabulary compliance:
- HIGH-STRUCTURE (flow, trace): DO NOT use interview language, user quotes, adoption rates,
  or study framing. Specification language required.
- EVIDENCE-HEAVY (prove, listen): DO NOT use specification language, schema definitions, or
  contract structures. Study/data/interview framing required.
- MIXED: include at least one structural element AND at least one qualitative observation.
  Both required — DO NOT use pure specification or pure narrative alone.
- prove and listen: append after body —
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal.
  prove-*: requires actual experiment data or prototype outputs.
  listen-*: requires real user interviews or adoption measurements.

**Do not begin PHASE 3 until all nine namespace sections are written, each with a complete
MOCK ARTIFACT header block, a vocabulary-compliant artifact body (MUST use satisfied, DO NOT
use not violated), and — for prove and listen — a REAL-REQUIRED statement.**

---

### PHASE 3 — SUMMARIZE

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
  REAL-REQUIRED  — every EVIDENCE-HEAVY namespace, all tiers
  TIER-CRITICAL  — trace-*, scout-feasibility, listen-* at tier >= 2
  COMPLIANCE     — scout-compliance, trace-permissions when compliance context is active
  Multiple flags: REAL-REQUIRED + TIER-CRITICAL

Recommended Next Step: exact skill call that closes this namespace's coverage gap for {topic}.
Name the specific skill that turns this mock into real signal.
DO NOT write "gather more signals." Write the exact skill identifier.
Example: `/listen:adoption {topic}` not "run a listen skill."

**Do not begin PHASE 4 until the coverage summary table is complete: all nine namespaces appear
with a Category, all required Flags (REAL-REQUIRED for EVIDENCE-HEAVY; TIER-CRITICAL where
applicable; COMPLIANCE where active), and a named Recommended Next Step.**

---

### PHASE 4 — HANDOFF

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-{date}.md

Replace {topic} and {date} with actual values.
DO NOT write the literal placeholder string `{this-file}`.
DO NOT write any other content in this section.

---

## Predicted Scores (v4 rubric)

| Variation | C-14 | C-15 | C-16 | C-17 | Asp (9) | Score | Delta vs R3 ceiling |
|-----------|------|------|------|------|---------|-------|---------------------|
| V-01 output-format | PASS | PASS | PASS | PASS | 9/9 | 100 | 0 (matches R3 V-05) |
| V-02 lifecycle-emphasis | PASS | PASS | PASS | PASS | 9/9 | 100 | 0 |
| V-03 inertia-framing | PASS | PASS | PASS | FAIL | 8/9 | 98.9 | -1.1 |
| V-04 output+lifecycle | PASS | PASS | PASS | PASS | 9/9 | 100 | 0 |
| V-05 all three axes | PASS | PASS | PASS | PASS | 9/9 | 100 | 0 |

Discriminator: C-17. Only V-03 (inertia framing alone) fails — vocabulary rules remain in a
prose block rather than table columns. All other variations close both C-16 and C-17 via
instruction-based enforcement. V-04 and V-05 are the leaner path alternatives to R3 V-05's
pre-printed skeleton.

**Round 4 question for Round 5:** Do V-01/V-02/V-04/V-05 (instruction-based) achieve the same
execution reliability as R3 V-05 (pre-printed skeleton) when run against a live model? If
instruction-based vocabulary columns produce C-17 compliance less reliably than pre-printed
columns, the structural guarantee difference justifies R3 V-05's skeleton overhead.

Next: /mock:review mock-all simulations/quest/golden/mock-all-variate-R4-2026-03-15.md
