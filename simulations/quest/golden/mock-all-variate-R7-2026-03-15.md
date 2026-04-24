---
skill: quest-variate
skill_target: mock-all
date: 2026-03-15
round: 7
rubric_version: v7
status: VARIATE
---

# mock-all Variate — Round 7

**Date:** 2026-03-15
**Skill:** mock-all
**Rubric:** v7 (C-01 through C-20; aspirational denominator = 12)
**Round:** R7 — C-19 and C-20 added to rubric from R7 evidence targets

---

## What R6 Left Open

v7 adds C-19 and C-20 to the aspirational tier. R6 V-01/V-03/V-04 all scored 100 against v6
(12/12 aspirational). R6 V-02 and V-05 deliberately tested whether in-template vocabulary
placement is equivalent to table-column placement for C-17, scoring ~91.7 (11/12). The
remaining open question entering R7:

| Question | R6 state | R7 target |
|----------|----------|-----------|
| Does a **minimal** inline depth anchor — `{3-5 sentence artifact body}` as the placeholder token itself, referencing the vocabulary table rather than repeating it — enforce C-07 depth compliance? R6 V-02 put the depth anchor first inside a large in-placeholder vocabulary block. C-19 requires the anchor to be the placeholder name, not the first line of a block. | Partial — depth cue present in V-02/V-05 but buried in multi-line block; placeholder form ≠ minimal inline anchor | V-02: isolate the minimal-anchor form — placeholder is `{3-5 sentence artifact body — [register]; refer to MUST vocabulary from table}`, no vocabulary duplication inside `{}` |
| Does explicit inertia-to-next-step derivation — ROLE 3 instructed to derive each Recommended Next Step from the inertia answer produced in ROLE 2, not from generic coverage logic — elevate C-10 quality above V-03-class performance? R6 V-03 added "The next step should address the specific gap named in the inertia statement" as trailing guidance. C-20 requires the derivation to be the primary instruction, not a qualifier. | Partial — V-03 tied next-step to inertia statement via trailing guidance; C-20 requires the derivation to be primary and explicit at the placeholder level | V-03: make the inertia-to-next-step derivation the structural mechanism — ROLE 3 template references the inertia answer directly as the input to next-step generation |

---

## Axis-Assignment Plan

| Variation | Axis | Source signal | Target criteria | Predicted score |
|-----------|------|---------------|-----------------|-----------------|
| V-01 | role-sequence (identity constraint baseline) | R6 V-01 achieved 12/12 against v6. v7 adds C-19 and C-20 to the denominator. V-01 is the clean baseline: same identity-constraint framing, vocabulary columns, enumerated stop-gate fields — but standard placeholder (no inline depth anchor) and no explicit inertia-to-next-step derivation. Establishes the marginal gain C-19 and C-20 represent. | C-18 (PASS), C-19 (FAIL — standard placeholder), C-20 (FAIL — no derivation bridge); all other criteria PASS | 10/12 aspirational → score ~98.3 |
| V-02 | output-format (minimal inline depth anchor — C-19 evidence) | R6 V-02 had depth anchor as first line of a multi-line vocabulary block inside `{}`. C-19 requires the placeholder to be the anchor: `{3-5 sentence artifact body — [CATEGORY] register; apply MUST vocabulary from classification table}`. The vocabulary rules stay in the classification table (C-17 ✓). The placeholder is short, self-referencing, and contains only the depth cue. This separates depth enforcement (placeholder) from vocabulary enforcement (table). | C-17 (PASS — vocab in table), C-18 (PASS — role identity), C-19 (PASS — minimal inline anchor) | 11/12 aspirational → score ~99.2 |
| V-03 | inertia-framing (explicit inertia-to-next-step bridge — C-20 evidence) | R6 V-03 added a trailing instruction: "next step should address the specific gap named in the inertia statement." C-20 requires the inertia-to-derivation connection to be structural: ROLE 3's Recommended Next Step placeholder must reference the inertia answer as its input. "Derive from the inertia answer — not generic coverage logic. A recommendation that would be valid for any namespace is not valid here." C-07 quality also elevated because body must be provably grounded in the inertia answer. | C-18 (PASS), C-19 (FAIL — standard placeholder), C-20 (PASS — derivation bridge is primary instruction in ROLE 3 template) | 11/12 aspirational → score ~99.2 |
| V-04 | role-sequence + output-format (V-01 + V-02) | Adds V-02's minimal inline depth anchor to V-01's full enumerated stop-gate fields. Classification table has vocabulary columns (C-17). Placeholder is minimal inline anchor (C-19). No inertia framing. Tests whether C-17 + C-19 co-present at both classification and generation time produces cleaner C-07 compliance than either alone. | C-17 PASS, C-18 PASS, C-19 PASS, C-20 FAIL | 11/12 aspirational → score ~99.2 |
| V-05 | role-sequence + output-format + inertia-framing (full combination) | All three axes active. V-01 identity constraint + V-02 minimal inline anchor + V-03 inertia-to-next-step derivation. The minimal placeholder carries the depth cue; the table carries vocabulary; the inertia statement carries relevance. ROLE 3 derives next steps from inertia answers. This is the ceiling variation — all 12 aspirational criteria active simultaneously. | C-17 PASS, C-18 PASS, C-19 PASS, C-20 PASS — 12/12 aspirational → score 100 |

---

## V-01 — Role Sequence: Identity Constraint Baseline (Single Axis)

**axis:** role-sequence (identity constraint)
**hypothesis:** R6 V-01 achieved 12/12 aspirational against the v6 rubric. Against v7, the
same variation scores 10/12 because C-19 (minimal inline depth anchor) and C-20 (explicit
inertia-to-next-step derivation) are new criteria the baseline does not address. V-01 isolates
the R6 baseline to establish the marginal contribution of the two new mechanisms. If V-01
scores 10/12 as predicted, V-02 and V-03 each add exactly one aspirational criterion at the
cost of no other criterion — confirming the mechanisms are independent.
**predicted:** C-01 through C-18: all PASS. C-19 FAIL (placeholder does not contain inline
depth anchor; depth guidance in prose around placeholder). C-20 FAIL (no explicit
inertia-to-next-step derivation; next-step instruction is generic "exact skill call").
Score: 10/12 aspirational, composite ~98.3.
**failure condition:** V-01 fails a criterion previously PASS in R6, indicating a regression
in the baseline. If this occurs, compare V-01 to R6 V-01 line-by-line to isolate the
structural change.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier for {topic} and any compliance tags.
State at top of output: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs four sequential roles. Each role has a distinct identity. You ARE that role
while it is active. Producing output that belongs to a later role during an earlier role is
an identity violation — not a process error, an identity error.

---

### ROLE 1 — CLASSIFIER

You are the CLASSIFIER. Your sole output is the classification table below, fully populated.
Writing an artifact body here means you are ROLE 2 — GENERATOR, which you are not yet.
Writing a coverage summary means you are ROLE 3 — SUMMARIZER, which you are not yet.
You classify. Nothing else.

Classification rules:
- EVIDENCE-HEAVY: prove, listen
- HIGH-STRUCTURE: trace, flow
- MIXED: scout, draft, review, program, topic

REAL-REQUIRED rationale (applies to all EVIDENCE-HEAVY and compliance-active namespaces):
A synthetic artifact cannot substitute for real signal. prove-* requires actual experiment
data or prototype outputs. listen-* requires real user interviews or adoption measurements.
Compliance-active namespaces (scout-compliance, trace-permissions) require traceable
real-world sources — synthetic artifacts here create false assurance regardless of
structural quality.

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED |
|-----------|----------|----------|------------|-------------------|-------------------|---------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language only; pure study methodology framing only | NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES |
| draft | MIXED | structural scaffold: sections, properties, acceptance criteria; qualitative observations | pure specification language only; pure study methodology framing only | NO | NO | NO |
| review | MIXED | structural scaffold; qualitative observations; design judgements | pure specification language only; pure study methodology framing only | NO | NO | NO |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language; user quotes; adoption percentages; study framing | NO | NO | NO |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language; adoption rates; user quotes; study framing | YES if tier >= 2; else NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES |
| prove | EVIDENCE-HEAVY | study/data framing: "N of M tests showed…", "prototype against {topic} produced…", hypothesis-and-result | specification language; schema definitions; contract structures | NO | NO | YES |
| listen | EVIDENCE-HEAVY | study/data framing: adoption rates, "N users found…", survey response framing | specification language; state machine language; schema definitions | YES if tier >= 2; else NO | NO | YES |
| program | MIXED | structural scaffold: milestones, owners, dependencies; qualitative rationale | pure specification language only; pure study methodology framing only | NO | NO | NO |
| topic | MIXED | signal synthesis narrative; structured coverage reference | pure specification language alone | NO | NO | NO |

**ROLE 1 STOP — Do not activate ROLE 2 — GENERATOR until all nine namespaces have all seven
fields populated: (1) Category assigned as HIGH-STRUCTURE, EVIDENCE-HEAVY, or MIXED;
(2) MUST-use vocabulary present; (3) DO NOT-use vocabulary present; (4) Tier 2/3 Critical
set to YES or NO; (5) Compliance-Tagged set to YES or NO; (6) REAL-REQUIRED set to YES or NO.
Any empty cell fails this gate.**

---

### ROLE 2 — GENERATOR

You are the GENERATOR. Your sole output is nine namespace artifact sections, one per ROLE 1
row, in table order.

Writing a coverage summary means you are ROLE 3 — SUMMARIZER, which you are not yet.
Writing a handoff line means you are ROLE 4 — HANDOFF WRITER, which you are not yet.
You generate. Nothing else.

Apply MUST-use and DO NOT-use vocabulary from the ROLE 1 table exactly. An artifact body
that uses DO NOT-use vocabulary is a generation error and must be corrected before this role
ends.

For each namespace:

  #### {Namespace} — {representative-skill-name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{representative-skill-name}
  Topic:    {topic}
  Category: {from ROLE 1 table}
  Date:     {current date}
  Status:   MOCK

  {artifact body — vocabulary-compliant with ROLE 1 MUST-use and DO NOT-use for this row}

  [If REAL-REQUIRED = YES in ROLE 1 table:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {one sentence specific to this namespace — prove: requires actual experiment
  data or prototype outputs; listen: requires real user interviews or adoption measurements;
  compliance namespace: requires traceable real-world sources.}

**ROLE 2 STOP — Do not activate ROLE 3 — SUMMARIZER until: (1) all nine namespaces are
present as artifact sections; (2) each section has a complete MOCK ARTIFACT header block
with all five fields (Skill, Topic, Category, Date, Status); (3) each artifact body uses
MUST-use vocabulary and does not use DO NOT-use vocabulary from its ROLE 1 row; (4) every
namespace with REAL-REQUIRED = YES has a REAL-REQUIRED statement with a one-sentence
rationale. Any missing field, vocabulary violation, or absent rationale fails this gate.**

---

### ROLE 3 — SUMMARIZER

You are the SUMMARIZER. Your sole output is the coverage summary table. Writing new artifact
sections means you are ROLE 2, which is no longer active. Writing the handoff line means you
are ROLE 4, which you are not yet. You summarize. Nothing else.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
- REAL-REQUIRED: all EVIDENCE-HEAVY namespaces; all compliance-active namespaces
- TIER-CRITICAL: trace-* at tier >= 2; scout-feasibility at tier >= 2; listen-* at tier >= 2
- Multiple flags: REAL-REQUIRED, TIER-CRITICAL (comma-separated)
- No applicable flag: —

Recommended Next Step: exact skill invocation — `/namespace:skill {topic}`. Not generic
advice. Each step must name the specific skill that produces the most needed signal for this
namespace. "Gather more signals" is not a valid recommendation.

**ROLE 3 STOP — Do not activate ROLE 4 — HANDOFF WRITER until: (1) all nine namespaces
appear in the coverage table; (2) each row has a Category matching the ROLE 1 table; (3) each
row has all applicable Flags assigned; (4) each row has a Recommended Next Step naming a
specific skill call. Any missing row, absent Flag, or generic next step fails this gate.**

---

### ROLE 4 — HANDOFF WRITER

You are the HANDOFF WRITER. Your sole output is the handoff section below. You write the
handoff. Nothing else.

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

Replace {topic} and {date} with actual values before writing this section.
DO NOT write `{this-file}` as a literal placeholder.
DO NOT write any other content in this section.

---

---

## V-02 — Output Format: Minimal Inline Depth Anchor (Single Axis — C-19 Evidence)

**axis:** output-format (minimal inline depth anchor)
**hypothesis:** R6 V-02 placed `3-5 sentence` as the first line of a large multi-line
vocabulary block inside `{}`. The depth anchor was present but embedded — the placeholder
was structurally a vocabulary instruction block with a sentence count at the top.
C-19 requires the placeholder to be the anchor: `{3-5 sentence artifact body — [CATEGORY]
register; apply MUST vocabulary from classification table}`. The vocabulary rules remain in
the classification table columns (C-17 ✓). The placeholder is short, self-referencing, and
carries only the depth cue and a register tag that points back to the table. This separates
the two enforcement mechanisms: table = what vocabulary; placeholder = how much content.
When the model fills the placeholder, it sees the depth requirement inline — not below a
colon, not inside a block, but as the label of the thing it is filling.
**predicted:** C-17 PASS (vocabulary rules in classification table columns, not in
placeholder). C-18 PASS (role identity present). C-19 PASS (depth anchor is the placeholder
token itself — `{3-5 sentence artifact body — …}` is the entire placeholder). C-20 FAIL (no
inertia-to-next-step derivation). Score: 11/12 aspirational, composite ~99.2.
**failure condition:** Minimal placeholder produces shorter bodies than R6 V-02's verbose
in-placeholder block — the sentence count alone is insufficient without the vocabulary
examples co-located. If this occurs, the R6 in-placeholder vocabulary block was doing two
jobs (depth anchor + vocabulary guidance), and C-19's minimal form requires supplementation
from a different enforcement mechanism.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier for {topic} and any compliance tags.
State at top of output: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs four sequential roles. Each role has a distinct identity. You ARE that role
while it is active. Producing output that belongs to a later role during an earlier role is
an identity violation.

---

### ROLE 1 — CLASSIFIER

You are the CLASSIFIER. Your sole output is the classification table below, fully populated.
Writing an artifact body here is a role violation — you are not yet ROLE 2 — GENERATOR.
You classify. Nothing else.

Classification rules:
- EVIDENCE-HEAVY: prove, listen
- HIGH-STRUCTURE: trace, flow
- MIXED: scout, draft, review, program, topic

REAL-REQUIRED rationale: A synthetic artifact cannot substitute for real signal in
EVIDENCE-HEAVY namespaces. prove-* requires actual experiment data or prototype outputs.
listen-* requires real user interviews or adoption measurements. Compliance-active namespaces
require traceable real-world sources — synthetic artifacts here create false assurance.

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED |
|-----------|----------|----------|------------|-------------------|-------------------|---------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language only; pure study methodology framing only | NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES |
| draft | MIXED | structural scaffold: sections, properties, acceptance criteria; qualitative observations | pure specification language only; pure study methodology framing only | NO | NO | NO |
| review | MIXED | structural scaffold; qualitative observations; design judgements | pure specification language only; pure study methodology framing only | NO | NO | NO |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language; user quotes; adoption percentages; study framing | NO | NO | NO |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language; adoption rates; user quotes; study framing | YES if tier >= 2; else NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES |
| prove | EVIDENCE-HEAVY | study/data framing: "N of M tests showed…", "prototype against {topic} produced…", hypothesis-and-result | specification language; schema definitions; contract structures | NO | NO | YES |
| listen | EVIDENCE-HEAVY | study/data framing: adoption rates, "N users found…", survey response framing | specification language; state machine language; schema definitions | YES if tier >= 2; else NO | NO | YES |
| program | MIXED | structural scaffold: milestones, owners, dependencies; qualitative rationale | pure specification language only; pure study methodology framing only | NO | NO | NO |
| topic | MIXED | signal synthesis narrative; structured coverage reference | pure specification language alone | NO | NO | NO |

**ROLE 1 STOP — Do not activate ROLE 2 until all nine namespaces have all seven fields
populated: (1) Category; (2) MUST-use vocabulary; (3) DO NOT-use vocabulary; (4) Tier 2/3
Critical (YES/NO); (5) Compliance-Tagged (YES/NO); (6) REAL-REQUIRED (YES/NO). Any empty
cell fails this gate.**

---

### ROLE 2 — GENERATOR

You are the GENERATOR. Your sole output is nine namespace artifact sections, one per ROLE 1
row, in table order.

Do not re-classify. Do not write the coverage summary. Writing a coverage summary row means
you are ROLE 3 — SUMMARIZER, which you are not yet.

For each namespace, fill in the template below. The body placeholder carries the depth
requirement inline as its token text — fill it with content of exactly that form. Do not copy
the placeholder text into the output.

  #### {Namespace} — {representative-skill-name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{representative-skill-name}
  Topic:    {topic}
  Category: {from ROLE 1 table}
  Date:     {current date}
  Status:   MOCK

  {3-5 sentence artifact body — register matches Category from ROLE 1 table: HIGH-STRUCTURE
  uses contract/specification language; EVIDENCE-HEAVY uses study/data language; MIXED uses
  discovery/signal language; apply MUST-use vocabulary and do not use DO NOT-use vocabulary
  from the ROLE 1 classification table for this namespace}

  [If REAL-REQUIRED = YES in ROLE 1 table:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {one sentence — prove: requires actual experiment data or prototype outputs;
  listen: requires real user interviews or adoption measurements; compliance namespace:
  requires traceable real-world sources.}

**ROLE 2 STOP — Do not activate ROLE 3 until all nine namespaces have: a complete MOCK
ARTIFACT header block (all five fields), a 3-5 sentence vocabulary-compliant body with
register matching the ROLE 1 Category, and — for every REAL-REQUIRED namespace — a
rationale-accompanied REAL-REQUIRED statement. Any vocabulary violation or absent rationale
fails this gate.**

---

### ROLE 3 — SUMMARIZER

You are the SUMMARIZER. Produce the coverage summary table only. Writing new artifact
sections or the handoff line is a role violation. You summarize. Nothing else.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
- REAL-REQUIRED: all EVIDENCE-HEAVY namespaces; all compliance-active namespaces
- TIER-CRITICAL: trace-* at tier >= 2; scout-feasibility at tier >= 2; listen-* at tier >= 2
- Multiple flags: REAL-REQUIRED, TIER-CRITICAL
- No applicable flag: —

Recommended Next Step: exact skill invocation — `/namespace:skill {topic}`. Not generic advice.

**ROLE 3 STOP — Do not activate ROLE 4 until all nine rows have Category, all applicable
Flags, and a Recommended Next Step naming a specific skill call.**

---

### ROLE 4 — HANDOFF WRITER

You are the HANDOFF WRITER. Write only the handoff section.

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

Replace {topic} and {date} with actual values.
DO NOT write `{this-file}` as a literal placeholder.
DO NOT write any other content in this section.

---

---

## V-03 — Inertia Framing: Explicit Derivation Bridge (Single Axis — C-20 Evidence)

**axis:** inertia-framing (explicit inertia-to-next-step derivation)
**hypothesis:** R6 V-03 tied the Recommended Next Step to the inertia answer via trailing
guidance: "The next step should address the specific gap named in the inertia statement for
this namespace." C-20 requires the derivation to be the primary structural mechanism — not
a modifier on a generic instruction. V-03's ROLE 3 template names the inertia statement as
the INPUT to next-step generation: "the skill call that closes the gap named in this
namespace's inertia statement from ROLE 2." A next step that would be identical regardless
of the inertia answer fails the gate. This change elevates C-10 quality from "namespace-
specific" to "inertia-grounded" — the recommendation can only be produced by someone who
read the inertia answer, not by someone who knows the namespace alone.
**predicted:** C-17 PASS (vocabulary columns in table). C-18 PASS (role identity). C-19
FAIL (standard placeholder — no inline depth anchor in token text). C-20 PASS (ROLE 3
template explicitly names inertia answer as derivation input; gate rejects next steps that
would be valid without the inertia answer). Score: 11/12 aspirational, composite ~99.2.
**failure condition:** Inertia statements are too generic ("without this signal, the story
would be missing evidence") to ground next steps — the derivation bridge carries no
information. If this occurs, inertia framing requires a grounding instruction in ROLE 2 that
forces topic-specificity before the bridge can function in ROLE 3.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier for {topic} and any compliance tags.
State at top of output: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill generates synthetic signal artifacts across all nine namespaces. Every artifact
answers the inertia question: "Without this signal, {topic}'s feature story would be missing
[what, specifically?]." That answer is the input to both the artifact body (ROLE 2) and the
Recommended Next Step (ROLE 3). A body that could exist without the inertia answer is too
generic. A next step that would be identical regardless of the inertia answer does not close
the named gap.

This skill runs four sequential roles. You ARE the named role while it is active. Producing
output belonging to a later role is a role violation.

---

### ROLE 1 — CLASSIFIER

You are the CLASSIFIER. Produce the classification table. Do not write artifact bodies.
Writing an artifact body here is a role violation — you are not yet ROLE 2. You classify.

Classification rules:
- EVIDENCE-HEAVY: prove, listen
- HIGH-STRUCTURE: trace, flow
- MIXED: scout, draft, review, program, topic

REAL-REQUIRED rationale: A synthetic artifact cannot substitute for real signal in
EVIDENCE-HEAVY namespaces. prove-* requires actual experiment data or prototype outputs.
listen-* requires real user interviews or adoption measurements. Compliance-active namespaces
require traceable real-world sources; synthetic artifacts create false assurance.

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED |
|-----------|----------|----------|------------|-------------------|-------------------|---------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language only; pure study methodology framing only | NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES |
| draft | MIXED | structural scaffold: sections, properties, acceptance criteria; qualitative observations | pure specification language only; pure study methodology framing only | NO | NO | NO |
| review | MIXED | structural scaffold; qualitative observations; design judgements | pure specification language only; pure study methodology framing only | NO | NO | NO |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language; user quotes; adoption percentages; study framing | NO | NO | NO |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language; adoption rates; user quotes; study framing | YES if tier >= 2; else NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES |
| prove | EVIDENCE-HEAVY | study/data framing: "N of M tests showed…", "prototype against {topic} produced…", hypothesis-and-result | specification language; schema definitions; contract structures | NO | NO | YES |
| listen | EVIDENCE-HEAVY | study/data framing: adoption rates, "N users found…", survey response framing | specification language; state machine language; schema definitions | YES if tier >= 2; else NO | NO | YES |
| program | MIXED | structural scaffold: milestones, owners, dependencies; qualitative rationale | pure specification language only; pure study methodology framing only | NO | NO | NO |
| topic | MIXED | signal synthesis narrative; structured coverage reference | pure specification language alone | NO | NO | NO |

**ROLE 1 STOP — Do not activate ROLE 2 until all nine namespaces have all seven fields
populated: (1) Category; (2) MUST-use vocabulary; (3) DO NOT-use vocabulary; (4) Tier 2/3
Critical (YES/NO); (5) Compliance-Tagged (YES/NO); (6) REAL-REQUIRED (YES/NO). Any empty
cell fails this gate.**

---

### ROLE 2 — GENERATOR

You are the GENERATOR. For each namespace: answer the inertia question first, then write the
artifact body grounded in that answer. A body that could exist without the inertia answer is
too generic and must be revised before this role ends.

Apply MUST-use and DO NOT-use vocabulary from the ROLE 1 table. Do not re-classify. Do not
write the coverage summary.

For each namespace:

  #### {Namespace} — {representative-skill-name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{representative-skill-name}
  Topic:    {topic}
  Category: {from ROLE 1 table}
  Date:     {current date}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {one sentence — the specific gap this namespace closes for {topic}; not a generic gap
  statement; must name what is absent without this namespace's signal}

  {artifact body — vocabulary-compliant with ROLE 1 MUST-use and DO NOT-use for this row;
  grounded in the inertia statement above; a body that could exist without the inertia
  answer must be revised}

  [If REAL-REQUIRED = YES in ROLE 1 table:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {one sentence — prove: requires actual experiment data or prototype outputs;
  listen: requires real user interviews or adoption measurements; compliance namespace:
  requires traceable real-world sources.}

**ROLE 2 STOP — Do not activate ROLE 3 until all nine namespaces have: a complete MOCK
ARTIFACT header block (all five fields), a non-generic inertia statement ("Without this
signal, {topic}'s feature story would be missing: [specific gap]"), a vocabulary-compliant
artifact body grounded in the inertia statement, and — for every REAL-REQUIRED namespace —
a rationale-accompanied REAL-REQUIRED statement. A generic inertia statement or a body not
grounded in the inertia answer fails this gate.**

---

### ROLE 3 — SUMMARIZER

You are the SUMMARIZER. Produce the coverage summary table only. Do not write new artifact
sections. Do not write the handoff line. You summarize.

For each namespace row, the Recommended Next Step is derived from the inertia statement that
namespace produced in ROLE 2. The step must close the specific gap named in that inertia
statement. A recommendation that would be identical regardless of the inertia answer does not
close the named gap and must be revised.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
- REAL-REQUIRED: all EVIDENCE-HEAVY namespaces; all compliance-active namespaces
- TIER-CRITICAL: trace-* at tier >= 2; scout-feasibility at tier >= 2; listen-* at tier >= 2
- Multiple flags: REAL-REQUIRED, TIER-CRITICAL
- No applicable flag: —

Recommended Next Step: the skill call that closes the specific gap named in this namespace's
inertia statement from ROLE 2 — `/namespace:skill {topic}`. A recommendation valid for any
topic or any namespace without reference to the inertia answer is not valid here.

**ROLE 3 STOP — Do not activate ROLE 4 until all nine namespaces appear in the coverage
table with correct Category, all applicable Flags, and a Recommended Next Step that closes
the specific gap named in that namespace's inertia statement. A generic next step fails this
gate.**

---

### ROLE 4 — HANDOFF WRITER

You are the HANDOFF WRITER. Write only the handoff section.

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

Replace {topic} and {date} with actual values.
DO NOT write `{this-file}` as a literal placeholder.
DO NOT write any other content in this section.

---

---

## V-04 — Role Sequence + Output Format (Combination: V-01 + V-02)

**axes:** role-sequence + output-format (minimal inline depth anchor)
**hypothesis:** V-01 has vocabulary columns (C-17) and full enumerated stop-gate fields
(C-16) but a standard placeholder. V-02 has the minimal inline depth anchor (C-19) but
stop-gates are compact. V-04 combines both: vocabulary columns in the classification table
(C-17 ✓) + minimal inline depth anchor in the placeholder (C-19 ✓) + V-01's full field-
level gate enumeration (C-16 fully satisfied). The test: does the combination of table-level
vocabulary enforcement and placeholder-level depth enforcement produce strictly better C-07
compliance than either alone? The co-location principle — depth cue at the moment the body
is filled — should reinforce the table's vocabulary rules without duplicating them.
**predicted:** C-17 PASS (vocab in table columns). C-18 PASS (role identity). C-19 PASS
(minimal inline anchor in placeholder token). C-20 FAIL (no inertia-to-next-step derivation).
Score: 11/12 aspirational, composite ~99.2.
**failure condition:** Combination produces longer prompts that cause the model to skim
phase headers — role-identity framing degrades. If this occurs, there is a length-versus-
enforcement trade-off between V-01 (compact gates, standard placeholder) and V-04 (full
gates, inline anchor).

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier for {topic} and any compliance tags.
State at top of output: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs four sequential roles. Each role has a distinct identity. You ARE that role
while it is active. Producing output that belongs to a later role during an earlier role is
an identity violation — not a process error, an identity error.

---

### ROLE 1 — CLASSIFIER

You are the CLASSIFIER. Your sole output is the classification table below, fully populated.
Writing an artifact body here means you are ROLE 2 — GENERATOR, which you are not yet.
Writing a coverage summary means you are ROLE 3 — SUMMARIZER, which you are not yet.
You classify. Nothing else.

Classification rules:
- EVIDENCE-HEAVY: prove, listen
- HIGH-STRUCTURE: trace, flow
- MIXED: scout, draft, review, program, topic

REAL-REQUIRED rationale: A synthetic artifact cannot substitute for real signal in
EVIDENCE-HEAVY namespaces. prove-* requires actual experiment data or prototype outputs.
listen-* requires real user interviews or adoption measurements. Compliance-active namespaces
require traceable real-world sources — synthetic artifacts here create false assurance
regardless of structural quality.

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED |
|-----------|----------|----------|------------|-------------------|-------------------|---------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language only; pure study methodology framing only | NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES |
| draft | MIXED | structural scaffold: sections, properties, acceptance criteria; qualitative observations | pure specification language only; pure study methodology framing only | NO | NO | NO |
| review | MIXED | structural scaffold; qualitative observations; design judgements | pure specification language only; pure study methodology framing only | NO | NO | NO |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language; user quotes; adoption percentages; study framing | NO | NO | NO |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language; adoption rates; user quotes; study framing | YES if tier >= 2; else NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES |
| prove | EVIDENCE-HEAVY | study/data framing: "N of M tests showed…", "prototype against {topic} produced…", hypothesis-and-result | specification language; schema definitions; contract structures | NO | NO | YES |
| listen | EVIDENCE-HEAVY | study/data framing: adoption rates, "N users found…", survey response framing | specification language; state machine language; schema definitions | YES if tier >= 2; else NO | NO | YES |
| program | MIXED | structural scaffold: milestones, owners, dependencies; qualitative rationale | pure specification language only; pure study methodology framing only | NO | NO | NO |
| topic | MIXED | signal synthesis narrative; structured coverage reference | pure specification language alone | NO | NO | NO |

**ROLE 1 STOP — Do not activate ROLE 2 — GENERATOR until you have verified that all nine
namespaces are present AND each namespace has all seven fields populated:
(1) Category assigned as HIGH-STRUCTURE, EVIDENCE-HEAVY, or MIXED;
(2) MUST-use vocabulary terms present;
(3) DO NOT-use vocabulary terms present;
(4) Tier 2/3 Critical set to YES or NO;
(5) Compliance-Tagged set to YES or NO;
(6) REAL-REQUIRED set to YES or NO.
Any empty cell fails this gate.**

---

### ROLE 2 — GENERATOR

You are the GENERATOR. Your sole output is nine namespace artifact sections, one per ROLE 1
row, in table order.

Writing a coverage summary means you are ROLE 3 — SUMMARIZER, which you are not yet.
Writing a handoff line means you are ROLE 4 — HANDOFF WRITER, which you are not yet.
You generate. Nothing else.

For each namespace, fill in the template below. The body placeholder carries the depth
requirement inline as its token text — fill it with content of that form; do not copy
placeholder text into the output.

  #### {Namespace} — {representative-skill-name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{representative-skill-name}
  Topic:    {topic}
  Category: {from ROLE 1 table}
  Date:     {current date}
  Status:   MOCK

  {3-5 sentence artifact body — register matches Category from ROLE 1: HIGH-STRUCTURE uses
  contract/specification language; EVIDENCE-HEAVY uses study/data language; MIXED uses
  discovery/signal language; apply MUST-use vocabulary and do not use DO NOT-use vocabulary
  from the ROLE 1 classification table row for this namespace}

  [If REAL-REQUIRED = YES in ROLE 1 table:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {one sentence specific to this namespace — prove: requires actual experiment
  data or prototype outputs; listen: requires real user interviews or adoption measurements;
  compliance namespace: requires traceable real-world sources.}

**ROLE 2 STOP — Do not activate ROLE 3 — SUMMARIZER until you have verified:
(1) all nine namespaces are present as artifact sections;
(2) each section has a complete MOCK ARTIFACT header block with all five fields
    (Skill, Topic, Category, Date, Status);
(3) each artifact body is 3-5 sentences, uses MUST-use vocabulary, and does not use
    DO NOT-use vocabulary from the ROLE 1 row, with register matching the Category;
(4) every namespace with REAL-REQUIRED = YES has a REAL-REQUIRED statement followed by
    a one-sentence rationale.
Any missing field, vocabulary violation, register mismatch, or absent rationale fails
this gate.**

---

### ROLE 3 — SUMMARIZER

You are the SUMMARIZER. Your sole output is the coverage summary table. Writing new artifact
sections means you are ROLE 2, which is no longer active. Writing the handoff line means you
are ROLE 4, which you are not yet. You summarize. Nothing else.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
- REAL-REQUIRED: all EVIDENCE-HEAVY namespaces; all compliance-active namespaces
- TIER-CRITICAL: trace-* at tier >= 2; scout-feasibility at tier >= 2; listen-* at tier >= 2
- Multiple flags: REAL-REQUIRED, TIER-CRITICAL (comma-separated)
- No applicable flag: —

Recommended Next Step: exact skill invocation — `/namespace:skill {topic}`. Not generic
advice. Must name the specific skill that produces the most needed signal.

**ROLE 3 STOP — Do not activate ROLE 4 — HANDOFF WRITER until:
(1) all nine namespaces appear in the coverage table;
(2) each row has a Category matching the ROLE 1 table;
(3) each row has all applicable Flags assigned (REAL-REQUIRED, TIER-CRITICAL);
(4) each row has a Recommended Next Step naming a specific skill call.
Any missing row, incorrect Category, absent Flag, or generic next step fails this gate.**

---

### ROLE 4 — HANDOFF WRITER

You are the HANDOFF WRITER. Your sole output is the handoff section below. You write the
handoff. Nothing else.

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

Replace {topic} and {date} with actual values.
DO NOT write `{this-file}` as a literal placeholder.
DO NOT write any other content in this section.

---

---

## V-05 — Full Combination: Role Sequence + Output Format + Inertia Framing

**axes:** role-sequence + output-format (minimal inline depth anchor) + inertia-framing
(explicit derivation bridge)
**hypothesis:** All three axes active. V-01 identity constraint (C-18) prevents cross-role
contamination at the ontological level. V-02 minimal inline depth anchor (C-19) enforces
sentence-count depth at the moment the model fills the body placeholder, without duplicating
vocabulary rules. V-03 inertia-to-next-step derivation (C-20) grounds both the artifact body
and the coverage summary recommendation in the same gap analysis. The three mechanisms target
independent enforcement layers: who you are (identity) + how much you write (depth anchor) +
why it matters (inertia). Combined, a body that is short, register-wrong, and inertia-
disconnected is blocked at three independent checkpoints rather than one. The coverage
summary's next steps derive from inertia answers that are themselves grounded in the artifact
body — the full chain closes.
**predicted:** C-17 PASS (vocab columns in table). C-18 PASS (role identity). C-19 PASS
(minimal inline depth anchor in placeholder token). C-20 PASS (ROLE 3 derives next steps
from inertia answers as primary mechanism). Score: 12/12 aspirational, composite 100.
**failure condition:** Three axes in one prompt increase length to the point where role
identity framing becomes decorative — the model begins generating before classification is
complete. If this occurs, the ceiling for single-session prompts is V-04 (role + depth
anchor), with inertia framing better suited to a two-pass structure.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier for {topic} and any compliance tags.
State at top of output: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill generates synthetic signal artifacts across all nine namespaces. Every artifact
answers the inertia question: "Without this signal, {topic}'s feature story would be missing
[what, specifically?]." That answer is the input to the artifact body (ROLE 2) and the
Recommended Next Step (ROLE 3). A body that could exist without the inertia answer is too
generic. A next step that would be identical regardless of the inertia answer does not close
the named gap.

This skill runs four sequential roles. Each role has a distinct identity. You ARE that role
while it is active. Producing output that belongs to a later role during an earlier role is
an identity violation — not a process error, an identity error.

---

### ROLE 1 — CLASSIFIER

You are the CLASSIFIER. Your sole output is the classification table below, fully populated.
Writing an artifact body here means you are ROLE 2 — GENERATOR, which you are not yet.
Writing a coverage summary means you are ROLE 3 — SUMMARIZER, which you are not yet.
You classify. Nothing else.

Classification rules:
- EVIDENCE-HEAVY: prove, listen
- HIGH-STRUCTURE: trace, flow
- MIXED: scout, draft, review, program, topic

REAL-REQUIRED rationale: A synthetic artifact cannot substitute for real signal in
EVIDENCE-HEAVY namespaces. prove-* requires actual experiment data or prototype outputs.
listen-* requires real user interviews or adoption measurements. Compliance-active namespaces
require traceable real-world sources — synthetic artifacts here create false assurance
regardless of structural quality.

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED |
|-----------|----------|----------|------------|-------------------|-------------------|---------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language only; pure study methodology framing only | NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES |
| draft | MIXED | structural scaffold: sections, properties, acceptance criteria; qualitative observations | pure specification language only; pure study methodology framing only | NO | NO | NO |
| review | MIXED | structural scaffold; qualitative observations; design judgements | pure specification language only; pure study methodology framing only | NO | NO | NO |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language; user quotes; adoption percentages; study framing | NO | NO | NO |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language; adoption rates; user quotes; study framing | YES if tier >= 2; else NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES |
| prove | EVIDENCE-HEAVY | study/data framing: "N of M tests showed…", "prototype against {topic} produced…", hypothesis-and-result | specification language; schema definitions; contract structures | NO | NO | YES |
| listen | EVIDENCE-HEAVY | study/data framing: adoption rates, "N users found…", survey response framing | specification language; state machine language; schema definitions | YES if tier >= 2; else NO | NO | YES |
| program | MIXED | structural scaffold: milestones, owners, dependencies; qualitative rationale | pure specification language only; pure study methodology framing only | NO | NO | NO |
| topic | MIXED | signal synthesis narrative; structured coverage reference | pure specification language alone | NO | NO | NO |

**ROLE 1 STOP — Do not activate ROLE 2 — GENERATOR until you have verified that all nine
namespaces are present AND each namespace has all seven fields populated:
(1) Category assigned as HIGH-STRUCTURE, EVIDENCE-HEAVY, or MIXED;
(2) MUST-use vocabulary terms present;
(3) DO NOT-use vocabulary terms present;
(4) Tier 2/3 Critical set to YES or NO;
(5) Compliance-Tagged set to YES or NO;
(6) REAL-REQUIRED set to YES or NO.
Any empty cell fails this gate.**

---

### ROLE 2 — GENERATOR

You are the GENERATOR. For each namespace: answer the inertia question first, then write the
artifact body grounded in that answer. The body placeholder carries the depth requirement
inline as its token text — fill it with content of that form; do not copy placeholder text
into the output. A body that could exist without the inertia answer must be revised.

Writing a coverage summary means you are ROLE 3 — SUMMARIZER, which you are not yet.
You generate. Nothing else.

Apply MUST-use and DO NOT-use vocabulary from the ROLE 1 table exactly. For each namespace,
in ROLE 1 table order:

  #### {Namespace} — {representative-skill-name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{representative-skill-name}
  Topic:    {topic}
  Category: {from ROLE 1 table}
  Date:     {current date}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {one sentence — the specific gap this namespace closes for {topic}; must name what is
  absent without this namespace's signal; not a generic gap statement}

  {3-5 sentence artifact body — register matches Category from ROLE 1: HIGH-STRUCTURE uses
  contract/specification language; EVIDENCE-HEAVY uses study/data language; MIXED uses
  discovery/signal language; apply MUST-use vocabulary and do not use DO NOT-use vocabulary
  from the ROLE 1 classification table row for this namespace; body must be grounded in the
  inertia statement above — a body that could exist without the inertia answer must be
  revised before this role ends}

  [If REAL-REQUIRED = YES in ROLE 1 table:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {one sentence — prove: requires actual experiment data or prototype outputs;
  listen: requires real user interviews or adoption measurements; compliance namespace:
  requires traceable real-world sources.}

**ROLE 2 STOP — Do not activate ROLE 3 — SUMMARIZER until you have verified:
(1) all nine namespaces are present as artifact sections;
(2) each section has a complete MOCK ARTIFACT header block with all five fields
    (Skill, Topic, Category, Date, Status);
(3) each section has a non-generic inertia statement naming the specific gap for {topic};
(4) each artifact body is 3-5 sentences, vocabulary-compliant, grounded in the inertia
    statement, with register matching the Category;
(5) every namespace with REAL-REQUIRED = YES has a rationale-accompanied statement.
Any missing field, generic inertia answer, vocabulary violation, or absent rationale fails
this gate.**

---

### ROLE 3 — SUMMARIZER

You are the SUMMARIZER. Your sole output is the coverage summary table. Writing new artifact
sections means you are ROLE 2, which is no longer active. Writing the handoff line means you
are ROLE 4, which you are not yet. You summarize. Nothing else.

For each namespace row, the Recommended Next Step derives from the inertia statement that
namespace produced in ROLE 2. A recommendation that would be identical regardless of the
inertia answer does not close the named gap and must be revised.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
- REAL-REQUIRED: all EVIDENCE-HEAVY namespaces; all compliance-active namespaces
- TIER-CRITICAL: trace-* at tier >= 2; scout-feasibility at tier >= 2; listen-* at tier >= 2
- Multiple flags: REAL-REQUIRED, TIER-CRITICAL
- No applicable flag: —

Recommended Next Step: the skill call that closes the specific gap named in this namespace's
inertia statement from ROLE 2 — `/namespace:skill {topic}`. Derive from the inertia answer.
A recommendation valid for any topic or any namespace without reference to the inertia answer
is not valid here.

**ROLE 3 STOP — Do not activate ROLE 4 — HANDOFF WRITER until:
(1) all nine namespaces appear in the coverage table;
(2) each row has a Category matching the ROLE 1 table;
(3) each row has all applicable Flags assigned;
(4) each row has a Recommended Next Step derived from the inertia statement (not generic
    advice; must close the specific gap named).
Any missing row, incorrect Category, absent Flag, or inertia-disconnected next step fails
this gate.**

---

### ROLE 4 — HANDOFF WRITER

You are the HANDOFF WRITER. Your sole output is the handoff section below. You write the
handoff. Nothing else.

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

Replace {topic} and {date} with actual values.
DO NOT write `{this-file}` as a literal placeholder.
DO NOT write any other content in this section.

---

---

## Scorecard Preview

| Variation | Primary Axes | C-17 | C-18 | C-19 | C-20 | Aspirational Pass | Predicted Score |
|-----------|-------------|------|------|------|------|-------------------|-----------------|
| V-01 | role-sequence (baseline) | PASS | PASS | FAIL (standard placeholder, no depth anchor in token) | FAIL (no derivation bridge) | 10/12 | ~98.3 |
| V-02 | output-format (minimal inline anchor) | PASS | PASS | PASS (placeholder is the anchor token) | FAIL | 11/12 | ~99.2 |
| V-03 | inertia-framing (derivation bridge) | PASS | PASS | FAIL | PASS (inertia answer is ROLE 3 derivation input) | 11/12 | ~99.2 |
| V-04 | role-sequence + output-format | PASS | PASS | PASS | FAIL | 11/12 | ~99.2 |
| V-05 | role-sequence + output-format + inertia-framing | PASS | PASS | PASS | PASS | 12/12 | 100 |

**C-19 discriminator between V-01 and V-02:**
V-01 placeholder: `{artifact body — vocabulary-compliant with ROLE 1 MUST-use and DO NOT-use for this row}`
V-02 placeholder: `{3-5 sentence artifact body — register matches Category from ROLE 1: HIGH-STRUCTURE uses contract/specification language; …; apply MUST-use vocabulary…}`
The depth cue (`3-5 sentence`) is inside the placeholder token text in V-02, not in prose around it.

**C-20 discriminator between V-01/V-02 and V-03/V-05:**
V-01/V-02 ROLE 3: "exact skill invocation — `/namespace:skill {topic}`. Not generic advice."
V-03/V-05 ROLE 3: "the skill call that closes the specific gap named in this namespace's inertia statement from ROLE 2 — `/namespace:skill {topic}`. Derive from the inertia answer. A recommendation valid for any topic or any namespace without reference to the inertia answer is not valid here."
The inertia answer is explicitly named as the derivation input in V-03/V-05.

**Open questions for scorecard:**
1. Does C-19 require the depth anchor to be the only content in the placeholder, or can it
   be the first element of a longer token text? V-02 and V-04 use longer token text that
   includes register cues after the sentence count — are these still "minimal inline anchors"
   or do they reintroduce the R6 V-02 pattern?
2. Does C-20 require the inertia answer to appear as a named field in the coverage table
   (e.g., a fifth column "Inertia Gap"), or is explicit ROLE 3 derivation instruction
   sufficient evidence?

Next: /mock:review {topic} simulations/quest/golden/mock-all-variate-R7-2026-03-15.md
