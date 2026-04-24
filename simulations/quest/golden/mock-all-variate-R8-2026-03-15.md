---
skill: quest-variate
skill_target: mock-all
date: 2026-03-15
round: 8
rubric_version: v8
status: VARIATE
---

# mock-all Variate — Round 8

**Date:** 2026-03-15
**Skill:** mock-all
**Rubric:** v8 (C-01 through C-20; aspirational denominator = 12)
**Round:** R8 — rubric frozen; V-05 R7 is the documented reference implementation at 100%

---

## What R7 Left Open

v8 adds no new criteria. Both open questions from R7 are resolved by v8's confirmation
notes:

| Question | R7 state | v8 resolution |
|----------|----------|---------------|
| Does C-19 require the depth anchor to be the *only* content in the placeholder, or can it be the first element of a longer token? R7 V-02/V-04 used longer token text with register cues after the sentence count. | Unresolved — "minimal inline anchor" was ambiguous about token length | RESOLVED: PASS form is `{3-5 sentence artifact body -- register matches Category...}` — sentence count as first token element. Longer token text is permitted; count must be first. |
| Does C-20 require the inertia answer to appear as a named column in the coverage table, or is explicit ROLE 3 derivation instruction sufficient? | Unresolved — V-03/V-05 both used ROLE 3 derivation instruction, neither used a table column | RESOLVED: V-05's ROLE 3 derivation bridge is the confirmed passing form. No coverage table column required. |

With both open questions resolved and the rubric frozen, R8 shifts to structural robustness
questions: can 100% be achieved with meaningfully different structural choices, and does any
axis expose a quality dimension that a potential v9 criterion might target?

---

## Axis-Assignment Plan

| Variation | Axis | Source signal | Target criteria | Predicted score |
|-----------|------|---------------|-----------------|-----------------|
| V-01 | role-sequence (consolidated preamble — remove per-role violation warnings) | R7 V-05 repeats identity-violation warnings in each role header. V-01 consolidates all identity-constraint language into a single preamble, strips per-role repetition, and keeps only the role name + stop-gate per phase. Tests if per-role violation warnings are structurally necessary for C-18 or decorative. | C-18 (PASS if role name + single-preamble constraint satisfy "identity violation"; FAIL if per-role enforcement is structurally required) | 12/12 aspirational; failure would reveal C-18 requires per-role framing |
| V-02 | output-format (inertia skeleton pre-classified in ROLE 1 table as 8th column) | R7 V-05 has ROLE 2 free-form the inertia question per namespace. V-02 adds an "Inertia gap skeleton" column to the ROLE 1 classification table — namespace-specific skeleton phrases (e.g., "which market signals are visible before building") that ROLE 2 extends with {topic}-specific content. Tests if pre-seeding the inertia skeleton in ROLE 1 improves C-20 output quality (consistently topic-grounded answers) and constitutes additional C-17 co-location. | C-17 PASS (vocabulary in table columns), C-18 PASS, C-19 PASS, C-20 PASS + improved quality | 12/12 aspirational → score 100 with measurably better C-20 output |
| V-03 | phrasing-register (prohibition-forward — no "You ARE" identity framing) | R7 V-05 uses ontological "You ARE the CLASSIFIER" framing. C-18 requires "the model knows it *is* the CLASSIFIER, not merely *is in step 1*." V-03 tests whether prohibition-forward framing ("CLASSIFIER: generate the classification table only. Generating artifact bodies is prohibited.") satisfies C-18 without the "You ARE" construct. If the criterion requires ontological framing specifically, prohibition-forward is analogous to "is in step 1" and fails C-18. | C-18 UNCERTAIN — prohibition-forward may not make wrong-phase output an *identity* violation, only a *rule* violation | 11/12 if C-18 requires ontological framing; 12/12 if prohibition-forward satisfies the identity-violation test |
| V-04 | lifecycle-emphasis (checklist stop-gates — one field per checkbox) | R7 V-05 uses prose stop-gate phrases with parenthesized field enumerations. V-04 converts all stop-gate phrases to markdown checkbox lists: one checkbox per required field, with "ROLE N STOP — do not activate ROLE N+1 until all boxes above are checked" as the gate phrase. Tests if checklist format improves C-16 (one checkbox = one enumerated field) while satisfying C-14 (explicit stop-gate phrase preserved at list header). | C-14 PASS (gate phrase at checklist header), C-16 PASS (one checkbox = one enumerated field) | 12/12 aspirational → score 100 |
| V-05 | combination: V-02 (inertia skeleton table) + V-04 (checklist gates) + V-01 (consolidated preamble) | All three single-axis changes active. ROLE 1 classification table has 8 columns including inertia gap skeleton. Stop-gates are checklist format. Identity framing is consolidated to preamble. The ceiling variant for R8 — all three structural changes together. If each individual variation scores 12/12, the combination also scores 12/12 with the cleanest output. | C-17 PASS, C-18 PASS (consolidated preamble), C-19 PASS, C-20 PASS (skeleton + derivation bridge) | 12/12 aspirational → score 100 |

---

## V-01 — Role Sequence: Consolidated Preamble (Single Axis)

**axis:** role-sequence (consolidated preamble; per-role identity-violation warnings removed)
**hypothesis:** R7 V-05 embeds identity-violation warnings in every role header: "Writing an
artifact body here means you are ROLE 2 — GENERATOR, which you are not yet." These warnings
make wrong-phase output a named violation at the point of potential transgression. V-01
removes per-role repetition and consolidates all identity-constraint language into a single
preamble: "Wrong-phase output is an identity violation in all phases — the wrong entity
acting." The role names remain. The stop-gates remain. The violation framing is present once.
If C-18 requires per-role enforcement at each role boundary, V-01 fails C-18. If C-18 is
satisfied by named roles + preamble constraint, V-01 scores 12/12 and establishes that the
per-role violation warnings in V-05 are quality repetition, not structural requirement.
**predicted:** C-01 through C-17: all PASS (unchanged from V-05 R7). C-18: PASS if preamble
+ named roles satisfy; FAIL if per-role violation warnings are structurally required. C-19
PASS (placeholder form unchanged from V-05 R7). C-20 PASS (inertia derivation bridge
unchanged from V-05 R7). Score: 12/12 aspirational if C-18 passes; 11/12 if C-18 fails.
**failure condition:** V-01 fails C-18 — the role names appear but the absence of per-role
violation language means the model does not treat wrong-phase output as an *identity*
violation, only as a generic error. If this occurs, C-18 requires not just naming the role
but repeating the identity-violation consequence at each role boundary.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier for {topic} and any compliance tags.
State at top of output: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs four sequential roles: CLASSIFIER, GENERATOR, SUMMARIZER, HANDOFF WRITER.
Each role has a distinct identity. You ARE that role while it is active. Wrong-phase output
is an identity violation in all phases — the wrong entity acting, not a process error.
Every role boundary has a stop-gate. Do not cross a stop-gate until its conditions are met.

---

### ROLE 1 — CLASSIFIER

You are the CLASSIFIER. Produce the classification table below, fully populated.
You classify. Nothing else.

Classification rules:
- EVIDENCE-HEAVY: prove, listen
- HIGH-STRUCTURE: trace, flow
- MIXED: scout, draft, review, program, topic

REAL-REQUIRED rationale (global — applies to all REAL-REQUIRED = YES entries):
A synthetic artifact cannot substitute for real signal. prove-* requires actual experiment
data or prototype outputs. listen-* requires real user interviews or adoption measurements.
Compliance-active namespaces require traceable real-world sources — synthetic artifacts
create false assurance regardless of structural quality.

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED |
|-----------|----------|----------|------------|-------------------|-------------------|---------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language only; pure study methodology framing only | NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES |
| draft | MIXED | structural scaffold: sections, properties, acceptance criteria; qualitative observations | pure specification language only; pure study methodology framing only | NO | NO | NO |
| review | MIXED | structural scaffold; qualitative observations; design judgements | pure specification language only; pure study methodology framing only | NO | NO | NO |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language; user quotes; adoption percentages; study framing | NO | NO | NO |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language; adoption rates; user quotes; study framing | YES if tier >= 2; else NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES |
| prove | EVIDENCE-HEAVY | study/data framing: "N of M tests showed...", "prototype against {topic} produced...", hypothesis-and-result | specification language; schema definitions; contract structures | NO | NO | YES |
| listen | EVIDENCE-HEAVY | study/data framing: adoption rates, "N users found...", survey response framing | specification language; state machine language; schema definitions | YES if tier >= 2; else NO | NO | YES |
| program | MIXED | structural scaffold: milestones, owners, dependencies; qualitative rationale | pure specification language only; pure study methodology framing only | NO | NO | NO |
| topic | MIXED | signal synthesis narrative; structured coverage reference | pure specification language alone | NO | NO | NO |

**ROLE 1 STOP — Do not activate ROLE 2 — GENERATOR until all nine namespaces have all
seven fields populated: (1) Category assigned as HIGH-STRUCTURE, EVIDENCE-HEAVY, or MIXED;
(2) MUST-use vocabulary present; (3) DO NOT-use vocabulary present; (4) Tier 2/3 Critical
set to YES or NO; (5) Compliance-Tagged set to YES or NO; (6) REAL-REQUIRED set to YES or
NO. Any empty cell fails this gate.**

---

### ROLE 2 — GENERATOR

You are the GENERATOR. Produce nine namespace artifact sections, one per ROLE 1 row, in
table order. You generate. Nothing else.

Before writing each artifact body, answer the inertia question for that namespace:
> Without this signal, {topic}'s feature story would be missing: ___

Write the inertia answer (one sentence) immediately before the artifact body. The body must
be grounded in the inertia answer — a body that could have been written without reading the
answer is too generic and must be revised.

For each namespace:

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

  {3-5 sentence artifact body -- register matches Category from ROLE 1: HIGH-STRUCTURE uses
  contract/specification language; EVIDENCE-HEAVY uses study/data language; MIXED uses
  discovery/signal language; apply MUST-use vocabulary and do not use DO NOT-use vocabulary
  from the ROLE 1 classification table for this namespace; body must be grounded in the
  inertia statement above -- a body that could exist without the inertia answer must be
  revised before this role ends}

  [If REAL-REQUIRED = YES in ROLE 1 table:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {one sentence -- prove: requires actual experiment data or prototype outputs;
  listen: requires real user interviews or adoption measurements; compliance namespace:
  requires traceable real-world sources.}

**ROLE 2 STOP — Do not activate ROLE 3 — SUMMARIZER until: (1) all nine namespaces are
present as artifact sections; (2) each section has a complete MOCK ARTIFACT header block
with all five fields (Skill, Topic, Category, Date, Status); (3) each section has a
non-generic inertia statement naming the specific gap for {topic}; (4) each artifact body
is 3-5 sentences, vocabulary-compliant, with register matching the Category, grounded in
the inertia statement; (5) every namespace with REAL-REQUIRED = YES has a REAL-REQUIRED
statement with a one-sentence rationale. Any missing field, generic inertia answer,
vocabulary violation, or absent rationale fails this gate.**

---

### ROLE 3 — SUMMARIZER

You are the SUMMARIZER. Produce the coverage summary table only. You summarize.
Nothing else.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
- REAL-REQUIRED: all EVIDENCE-HEAVY namespaces; all compliance-active namespaces
- TIER-CRITICAL: trace-* at tier >= 2; scout-feasibility at tier >= 2; listen-* at tier >= 2
- Multiple flags: REAL-REQUIRED, TIER-CRITICAL (comma-separated)
- No applicable flag: —

Recommended Next Step: the skill call that closes the specific gap named in this namespace's
inertia statement from ROLE 2. Derive from the inertia answer. A recommendation valid for
any topic or any namespace without reference to the inertia answer is not valid here.
Inertia-disconnected next step fails this gate. Format: `/namespace:skill {topic}`.

**ROLE 3 STOP — Do not activate ROLE 4 — HANDOFF WRITER until: (1) all nine namespaces
appear in the coverage table; (2) each row has a Category matching the ROLE 1 table; (3)
each row has all applicable Flags assigned; (4) each row has a Recommended Next Step derived
from the ROLE 2 inertia statement. Any missing row, absent Flag, or inertia-disconnected
recommendation fails this gate.**

---

### ROLE 4 — HANDOFF WRITER

You are the HANDOFF WRITER. Write only the handoff section. You write the handoff.
Nothing else.

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

Replace {topic} and {date} with actual values before writing this section.
DO NOT write `{this-file}` as a literal placeholder.
DO NOT write any other content in this section.

---

---

## V-02 — Output Format: Inertia Skeleton as ROLE 1 Table Column (Single Axis)

**axis:** output-format (inertia gap skeleton pre-classified in ROLE 1 as 8th table column)
**hypothesis:** R7 V-05 has ROLE 2 free-form the inertia question per namespace. The quality
of the inertia answer depends on the model's unprompted ability to identify the
namespace-specific epistemic gap for {topic}. V-02 moves the inertia skeleton into the ROLE
1 classification table as an 8th column: a namespace-specific gap phrase that names what
this namespace's signal provides, independent of any topic (e.g., scout: "which market
signals are visible before building"; prove: "whether the core assumption survives empirical
test"). ROLE 2 extends the skeleton with {topic}-specific content. The skeleton constrains
the inertia answer to the namespace's epistemic function before the topic is applied,
preventing generic "missing signal" answers. This also tests whether a skeleton that is
co-located in the ROLE 1 table constitutes additional C-17 satisfaction (vocabulary + inertia
co-located) versus a separate enforcement mechanism.
**predicted:** C-17 PASS (vocabulary rules in MUST/DO NOT columns; inertia skeleton is a
separate column that does not displace vocabulary). C-18 PASS (role identity unchanged).
C-19 PASS (placeholder form unchanged from V-05). C-20 PASS with improved quality (skeleton
forces namespace-specific framing; ROLE 2 extends rather than invents). Score: 12/12
aspirational; improved C-20 output quality. If the skeleton column produces materially better
artifact bodies, this is the R8 excellence signal.
**failure condition:** Skeleton phrases are too abstract to ground topic-specific answers —
ROLE 2 appends "{topic}" to a generic skeleton and produces the same quality as free-form.
If this occurs, the skeleton needs to be more prescriptive (naming the specific signal type
rather than the epistemic function) or scoped to a narrower namespace characterization.

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
Compliance-active namespaces require traceable real-world sources — synthetic artifacts
create false assurance regardless of structural quality.

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED | Inertia gap skeleton |
|-----------|----------|----------|------------|-------------------|-------------------|---------------|----------------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language only; pure study methodology framing only | NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES | "which market signals are visible before building" |
| draft | MIXED | structural scaffold: sections, properties, acceptance criteria; qualitative observations | pure specification language only; pure study methodology framing only | NO | NO | NO | "what structural shape the feature takes" |
| review | MIXED | structural scaffold; qualitative observations; design judgements | pure specification language only; pure study methodology framing only | NO | NO | NO | "whether the design holds up under expert scrutiny" |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language; user quotes; adoption percentages; study framing | NO | NO | NO | "how data moves through the system at runtime" |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language; adoption rates; user quotes; study framing | YES if tier >= 2; else NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES | "which components own which boundaries" |
| prove | EVIDENCE-HEAVY | study/data framing: "N of M tests showed...", "prototype against {topic} produced...", hypothesis-and-result | specification language; schema definitions; contract structures | NO | NO | YES | "whether the core assumption survives empirical test" |
| listen | EVIDENCE-HEAVY | study/data framing: adoption rates, "N users found...", survey response framing | specification language; state machine language; schema definitions | YES if tier >= 2; else NO | NO | YES | "how real users respond to the feature in practice" |
| program | MIXED | structural scaffold: milestones, owners, dependencies; qualitative rationale | pure specification language only; pure study methodology framing only | NO | NO | NO | "what the delivery plan looks like and who owns what" |
| topic | MIXED | signal synthesis narrative; structured coverage reference | pure specification language alone | NO | NO | NO | "whether enough signals exist to commit to the feature" |

**ROLE 1 STOP — Do not activate ROLE 2 — GENERATOR until all nine namespaces have all
eight fields populated: (1) Category assigned as HIGH-STRUCTURE, EVIDENCE-HEAVY, or MIXED;
(2) MUST-use vocabulary present; (3) DO NOT-use vocabulary present; (4) Tier 2/3 Critical
set to YES or NO; (5) Compliance-Tagged set to YES or NO; (6) REAL-REQUIRED set to YES or
NO; (7) Inertia gap skeleton present as a quoted phrase. Any empty cell fails this gate.**

---

### ROLE 2 — GENERATOR

You are the GENERATOR. Your sole output is nine namespace artifact sections, one per ROLE 1
row, in table order.

Writing a coverage summary means you are ROLE 3 — SUMMARIZER, which you are not yet.
Writing a handoff line means you are ROLE 4 — HANDOFF WRITER, which you are not yet.
You generate. Nothing else.

For each namespace, extend the ROLE 1 inertia gap skeleton with {topic}-specific content
to form the inertia answer:
> Without this signal, {topic}'s feature story would be missing: {extend the ROLE 1
> skeleton for this namespace with {topic}-specific content — one sentence}

Write the inertia answer before the artifact body. The body must be traceable to the
inertia answer — a body that could have been written without reading the answer, or one that
merely restates the skeleton without topic extension, is too generic and must be revised.

Apply MUST-use and DO NOT-use vocabulary from the ROLE 1 table exactly. For each namespace:

  #### {Namespace} — {representative-skill-name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{representative-skill-name}
  Topic:    {topic}
  Category: {from ROLE 1 table}
  Date:     {current date}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {extend the ROLE 1 inertia gap skeleton for this namespace with {topic}-specific content;
  must name what is absent without this namespace's signal; "the signal" alone does not pass}

  {3-5 sentence artifact body -- register matches Category from ROLE 1: HIGH-STRUCTURE uses
  contract/specification language; EVIDENCE-HEAVY uses study/data language; MIXED uses
  discovery/signal language; apply MUST-use vocabulary and do not use DO NOT-use vocabulary
  from the ROLE 1 classification table for this namespace; body must be grounded in the
  inertia answer above -- a body that could exist without the inertia answer must be revised}

  [If REAL-REQUIRED = YES in ROLE 1 table:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {one sentence -- prove: requires actual experiment data or prototype outputs;
  listen: requires real user interviews or adoption measurements; compliance namespace:
  requires traceable real-world sources.}

**ROLE 2 STOP — Do not activate ROLE 3 — SUMMARIZER until: (1) all nine namespaces are
present as artifact sections; (2) each section has a complete MOCK ARTIFACT header block
with all five fields (Skill, Topic, Category, Date, Status); (3) each inertia answer extends
the ROLE 1 skeleton with {topic}-specific content — not a restatement of the skeleton alone;
(4) each artifact body is 3-5 sentences, vocabulary-compliant, register-matched, grounded in
the inertia answer; (5) every namespace with REAL-REQUIRED = YES has a rationale-accompanied
statement. Any missing field, skeleton-restatement inertia answer, vocabulary violation, or
absent rationale fails this gate.**

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

Recommended Next Step: the skill call that closes the specific gap named in this namespace's
inertia answer from ROLE 2 — not the ROLE 1 skeleton, but the topic-extended answer.
Derive from the inertia answer. A recommendation valid for any topic or namespace without
reference to the inertia answer is not valid here. Inertia-disconnected next step fails this
gate. Format: `/namespace:skill {topic}`.

**ROLE 3 STOP — Do not activate ROLE 4 — HANDOFF WRITER until: (1) all nine namespaces
appear in the coverage table; (2) each row has a Category matching the ROLE 1 table; (3)
each row has all applicable Flags assigned; (4) each row has a Recommended Next Step derived
from the ROLE 2 inertia answer (not the ROLE 1 skeleton). Any missing row, absent Flag, or
inertia-disconnected recommendation fails this gate.**

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

## V-03 — Phrasing Register: Prohibition-Forward (Single Axis)

**axis:** phrasing-register (prohibition-forward framing; "You ARE" identity construct removed)
**hypothesis:** R7 V-05 uses ontological identity framing throughout: "You ARE the CLASSIFIER.
Writing an artifact body here means you are ROLE 2 — GENERATOR, which you are not yet." C-18
specifies: "the role name must make wrong-phase behavior an identity violation — the model
knows it *is* the CLASSIFIER, not merely *is in step 1*." V-03 tests the boundary of this
criterion by replacing the "You ARE" construct with prohibition-forward framing: the role
name is stated as a phase label ("CLASSIFIER:"), permitted output is enumerated, and
prohibited output is explicitly named. Wrong-phase output is framed as a "classification-
phase violation" rather than an identity violation. The model knows it is in the CLASSIFIER
phase; it may not know it *is* the CLASSIFIER as an entity. If C-18 requires the ontological
framing specifically — the model must identify *as* the CLASSIFIER rather than operate *in*
the CLASSIFIER phase — V-03 fails C-18 and provides clear evidence that "You ARE" is
structurally required, not just stylistically preferred.
**predicted:** C-18 UNCERTAIN. If prohibition-forward + named role label satisfy C-18:
score 12/12. If C-18 requires ontological "You ARE" construct: C-18 FAIL, score 11/12.
All other criteria unchanged from V-05 R7. C-19 PASS (placeholder form unchanged). C-20
PASS (inertia derivation bridge unchanged).
**failure condition:** V-03 fails C-18 — the prohibition language creates a rule violation,
not an identity violation. The model generates artifact bodies mid-classification and
treats this as an error to correct rather than as a category error (wrong entity acting).
If this occurs, the "You ARE" ontological framing is load-bearing for C-18, and subsequent
variations must preserve it.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier for {topic} and any compliance tags.
State at top of output: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs four sequential phases. Each phase has a named role. Generating output that
belongs to a later phase is a phase violation. Every phase has a stop-gate; do not cross it
until its conditions are met.

---

### CLASSIFIER

**CLASSIFIER: generate the classification table only.**

Permitted output: the classification table with all nine namespaces and all seven fields
populated. Nothing else.
Prohibited output: artifact bodies, coverage summaries, handoff lines.
Generating any prohibited output in this phase is a classification-phase violation.

Classification rules:
- EVIDENCE-HEAVY: prove, listen
- HIGH-STRUCTURE: trace, flow
- MIXED: scout, draft, review, program, topic

REAL-REQUIRED rationale (applies to all EVIDENCE-HEAVY and compliance-active namespaces):
A synthetic artifact cannot substitute for real signal. prove-* requires actual experiment
data or prototype outputs. listen-* requires real user interviews or adoption measurements.
Compliance-active namespaces require traceable real-world sources — synthetic artifacts
create false assurance regardless of structural quality.

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED |
|-----------|----------|----------|------------|-------------------|-------------------|---------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language only; pure study methodology framing only | NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES |
| draft | MIXED | structural scaffold: sections, properties, acceptance criteria; qualitative observations | pure specification language only; pure study methodology framing only | NO | NO | NO |
| review | MIXED | structural scaffold; qualitative observations; design judgements | pure specification language only; pure study methodology framing only | NO | NO | NO |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language; user quotes; adoption percentages; study framing | NO | NO | NO |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language; adoption rates; user quotes; study framing | YES if tier >= 2; else NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES |
| prove | EVIDENCE-HEAVY | study/data framing: "N of M tests showed...", "prototype against {topic} produced...", hypothesis-and-result | specification language; schema definitions; contract structures | NO | NO | YES |
| listen | EVIDENCE-HEAVY | study/data framing: adoption rates, "N users found...", survey response framing | specification language; state machine language; schema definitions | YES if tier >= 2; else NO | NO | YES |
| program | MIXED | structural scaffold: milestones, owners, dependencies; qualitative rationale | pure specification language only; pure study methodology framing only | NO | NO | NO |
| topic | MIXED | signal synthesis narrative; structured coverage reference | pure specification language alone | NO | NO | NO |

**CLASSIFIER STOP — Do not enter GENERATOR phase until all nine namespaces have all seven
fields populated: (1) Category assigned as HIGH-STRUCTURE, EVIDENCE-HEAVY, or MIXED;
(2) MUST-use vocabulary present; (3) DO NOT-use vocabulary present; (4) Tier 2/3 Critical
set to YES or NO; (5) Compliance-Tagged set to YES or NO; (6) REAL-REQUIRED set to YES or
NO. Any empty cell is a classification-phase violation — return to the table.**

---

### GENERATOR

**GENERATOR: generate nine namespace artifact sections only.**

Permitted output: nine namespace artifact sections, one per CLASSIFIER row, in table order.
Prohibited output: coverage summary rows, handoff lines, re-classification.
Generating any prohibited output in this phase is a generation-phase violation.

Before writing each artifact body, answer the inertia question for that namespace:
> Without this signal, {topic}'s feature story would be missing: ___

Write the inertia answer (one sentence) immediately before the artifact body. The body must
be grounded in the inertia answer — a body that could have been written without reading the
answer is too generic and must be revised.

For each namespace:

  #### {Namespace} — {representative-skill-name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{representative-skill-name}
  Topic:    {topic}
  Category: {from CLASSIFIER table}
  Date:     {current date}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {one sentence -- the specific gap this namespace closes for {topic}; must name what is
  absent without this namespace's signal; not a generic gap statement}

  {3-5 sentence artifact body -- register matches Category from CLASSIFIER table:
  HIGH-STRUCTURE uses contract/specification language; EVIDENCE-HEAVY uses study/data
  language; MIXED uses discovery/signal language; apply MUST-use vocabulary and do not use
  DO NOT-use vocabulary from the CLASSIFIER table for this namespace; body must be grounded
  in the inertia statement above -- a body that could exist without the inertia answer must
  be revised before this phase ends}

  [If REAL-REQUIRED = YES in CLASSIFIER table:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {one sentence -- prove: requires actual experiment data or prototype outputs;
  listen: requires real user interviews or adoption measurements; compliance namespace:
  requires traceable real-world sources.}

**GENERATOR STOP — Do not enter SUMMARIZER phase until: (1) all nine namespaces are present
as artifact sections; (2) each section has a complete MOCK ARTIFACT header block with all
five fields (Skill, Topic, Category, Date, Status); (3) each section has a non-generic
inertia statement naming the specific gap for {topic}; (4) each artifact body is 3-5
sentences, vocabulary-compliant, register-matched, grounded in the inertia statement; (5)
every namespace with REAL-REQUIRED = YES has a rationale-accompanied statement. Any missing
field or violation is a generation-phase violation — return to the section and fix it.**

---

### SUMMARIZER

**SUMMARIZER: generate the coverage summary table only.**

Permitted output: the coverage summary table. Nothing else.
Prohibited output: new artifact sections, handoff lines.
Generating any prohibited output in this phase is a summarization-phase violation.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
- REAL-REQUIRED: all EVIDENCE-HEAVY namespaces; all compliance-active namespaces
- TIER-CRITICAL: trace-* at tier >= 2; scout-feasibility at tier >= 2; listen-* at tier >= 2
- Multiple flags: REAL-REQUIRED, TIER-CRITICAL (comma-separated)
- No applicable flag: —

Recommended Next Step: the skill call that closes the specific gap named in this namespace's
inertia statement from GENERATOR. Derive from the inertia answer. A recommendation valid for
any topic or namespace without reference to the inertia answer is not valid here. Inertia-
disconnected next step is a summarization-phase violation. Format: `/namespace:skill {topic}`.

**SUMMARIZER STOP — Do not enter HANDOFF WRITER phase until: (1) all nine namespaces appear
in the coverage table; (2) each row has a Category matching the CLASSIFIER table; (3) each
row has all applicable Flags assigned; (4) each row has a Recommended Next Step derived from
the GENERATOR inertia statement. Any missing row, absent Flag, or inertia-disconnected
recommendation is a summarization-phase violation.**

---

### HANDOFF WRITER

**HANDOFF WRITER: write the handoff section only.**

Permitted output: the handoff section below. Nothing else.
Generating any other content in this phase is a handoff-phase violation.

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

Replace {topic} and {date} with actual values before writing this section.
DO NOT write `{this-file}` as a literal placeholder.
DO NOT write any other content in this section.

---

---

## V-04 — Lifecycle Emphasis: Checklist Stop-Gates (Single Axis)

**axis:** lifecycle-emphasis (checklist stop-gates — one checkbox per required field)
**hypothesis:** R7 V-05 uses prose stop-gate phrases with parenthesized field enumerations:
"Do not activate ROLE N until: (1) field A; (2) field B; (3) field C." C-14 requires an
explicit stop-gate phrase; C-16 requires that phrase to name specific required output fields.
V-04 converts all stop-gate phrases to markdown checkbox lists: one checkbox per required
field, with "ROLE N STOP — do not activate ROLE N+1 until all boxes above are checked" as
the gate header. The gate header satisfies C-14's explicit stop-gate phrase. The checkboxes
satisfy C-16's field enumeration (each checkbox is exactly one field). The question is
whether checklist format *improves* model compliance with gate conditions — the model sees
each field as a discrete checkbox rather than a clause in a parenthesized list. If models
are more likely to satisfy checkbox lists than prose enumerations, V-04 raises gate
enforcement quality above V-05 without changing rubric compliance.
**predicted:** C-14 PASS (gate header contains explicit stop-gate phrase). C-16 PASS (each
checkbox = one enumerated required field). C-18 PASS (role identity unchanged). C-19 PASS
(placeholder form unchanged). C-20 PASS (inertia derivation bridge unchanged). Score: 12/12
aspirational. If C-14 requires the field enumeration to appear inline with the stop-gate
phrase (as in the prose parenthesized form), checklist format might fail C-14 — the phrase
and the enumeration are structurally separated (header + list vs single prose block).
**failure condition:** C-14 fails because the checklist separates the stop-gate phrase
(header) from the field enumeration (list body) — the criterion reads "stop-gate phrase must
name specific fields" as requiring co-location in a single statement. If this occurs,
checklist format requires the fields to be in the header line itself to satisfy C-14+C-16
simultaneously.

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
Compliance-active namespaces require traceable real-world sources — synthetic artifacts
create false assurance regardless of structural quality.

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED |
|-----------|----------|----------|------------|-------------------|-------------------|---------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language only; pure study methodology framing only | NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES |
| draft | MIXED | structural scaffold: sections, properties, acceptance criteria; qualitative observations | pure specification language only; pure study methodology framing only | NO | NO | NO |
| review | MIXED | structural scaffold; qualitative observations; design judgements | pure specification language only; pure study methodology framing only | NO | NO | NO |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language; user quotes; adoption percentages; study framing | NO | NO | NO |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language; adoption rates; user quotes; study framing | YES if tier >= 2; else NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES |
| prove | EVIDENCE-HEAVY | study/data framing: "N of M tests showed...", "prototype against {topic} produced...", hypothesis-and-result | specification language; schema definitions; contract structures | NO | NO | YES |
| listen | EVIDENCE-HEAVY | study/data framing: adoption rates, "N users found...", survey response framing | specification language; state machine language; schema definitions | YES if tier >= 2; else NO | NO | YES |
| program | MIXED | structural scaffold: milestones, owners, dependencies; qualitative rationale | pure specification language only; pure study methodology framing only | NO | NO | NO |
| topic | MIXED | signal synthesis narrative; structured coverage reference | pure specification language alone | NO | NO | NO |

**ROLE 1 STOP — Do not activate ROLE 2 — GENERATOR until all boxes below are checked:**

- [ ] All nine namespaces present in the table
- [ ] Each namespace has Category assigned (HIGH-STRUCTURE, EVIDENCE-HEAVY, or MIXED)
- [ ] Each namespace has MUST-use vocabulary terms present
- [ ] Each namespace has DO NOT-use vocabulary terms present
- [ ] Each namespace has Tier 2/3 Critical set to YES or NO
- [ ] Each namespace has Compliance-Tagged set to YES or NO
- [ ] Each namespace has REAL-REQUIRED set to YES or NO

Any unchecked box fails this gate.

---

### ROLE 2 — GENERATOR

You are the GENERATOR. Your sole output is nine namespace artifact sections, one per ROLE 1
row, in table order.

Writing a coverage summary means you are ROLE 3 — SUMMARIZER, which you are not yet.
Writing a handoff line means you are ROLE 4 — HANDOFF WRITER, which you are not yet.
You generate. Nothing else.

Before writing each artifact body, answer the inertia question for that namespace:
> Without this signal, {topic}'s feature story would be missing: ___

Write the inertia answer (one sentence) immediately before the artifact body. The body must
be grounded in the inertia answer — a body that could have been written without reading the
answer is too generic and must be revised.

Apply MUST-use and DO NOT-use vocabulary from the ROLE 1 table exactly. For each namespace:

  #### {Namespace} — {representative-skill-name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{representative-skill-name}
  Topic:    {topic}
  Category: {from ROLE 1 table}
  Date:     {current date}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {one sentence -- the specific gap this namespace closes for {topic}; must name what is
  absent without this namespace's signal; not a generic gap statement}

  {3-5 sentence artifact body -- register matches Category from ROLE 1: HIGH-STRUCTURE uses
  contract/specification language; EVIDENCE-HEAVY uses study/data language; MIXED uses
  discovery/signal language; apply MUST-use vocabulary and do not use DO NOT-use vocabulary
  from the ROLE 1 classification table for this namespace; body must be grounded in the
  inertia statement above -- a body that could exist without the inertia answer must be
  revised before this role ends}

  [If REAL-REQUIRED = YES in ROLE 1 table:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {one sentence -- prove: requires actual experiment data or prototype outputs;
  listen: requires real user interviews or adoption measurements; compliance namespace:
  requires traceable real-world sources.}

**ROLE 2 STOP — Do not activate ROLE 3 — SUMMARIZER until all boxes below are checked:**

- [ ] All nine namespaces present as artifact sections
- [ ] Each section has a complete MOCK ARTIFACT header block (Skill, Topic, Category, Date, Status — all five fields present)
- [ ] Each section has an inertia statement that names the specific gap for {topic} (not a generic "missing signal" statement)
- [ ] Each artifact body is 3-5 sentences, with register matching the ROLE 1 Category
- [ ] Each artifact body uses MUST-use vocabulary from the ROLE 1 table for that namespace
- [ ] Each artifact body does not use DO NOT-use vocabulary from the ROLE 1 table for that namespace
- [ ] Each artifact body is grounded in the inertia statement (not writable without reading the inertia answer)
- [ ] Every namespace with REAL-REQUIRED = YES has a REAL-REQUIRED statement with a one-sentence rationale

Any unchecked box fails this gate.

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

Recommended Next Step: the skill call that closes the specific gap named in this namespace's
inertia statement from ROLE 2. Derive from the inertia answer. A recommendation valid for
any topic or namespace without reference to the inertia answer is not valid here. Inertia-
disconnected next step fails this gate. Format: `/namespace:skill {topic}`.

**ROLE 3 STOP — Do not activate ROLE 4 — HANDOFF WRITER until all boxes below are checked:**

- [ ] All nine namespaces present in the coverage table
- [ ] Each row has a Category matching the ROLE 1 table
- [ ] Each row has all applicable Flags assigned (REAL-REQUIRED where applicable, TIER-CRITICAL where applicable)
- [ ] Each row has a Recommended Next Step naming a specific skill call derived from the ROLE 2 inertia statement

Any unchecked box fails this gate.

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

## V-05 — Full Combination: Consolidated Preamble + Inertia Skeleton Table + Checklist Gates

**axes:** role-sequence (consolidated preamble) + output-format (inertia skeleton table) +
lifecycle-emphasis (checklist gates)
**hypothesis:** All three single-axis changes active simultaneously. V-01's consolidated
preamble removes per-role violation warning repetition while preserving named roles and
stop-gates. V-02's inertia skeleton column in ROLE 1 pre-seeds namespace-specific gap
framing so ROLE 2 extends rather than invents. V-04's checklist gates make each required
field a discrete checkbox, giving the model a self-verification mechanism at each role
boundary. The combination produces the most compact skill body that still carries all three
enforcement layers: identity (consolidated preamble + named roles), depth (inline placeholder
anchor), inertia (skeleton pre-classified in ROLE 1, extended in ROLE 2, derived in ROLE 3),
and field completeness (checklist gates). If V-01, V-02, and V-04 all individually score
12/12, V-05 also scores 12/12 — and if the inertia skeleton materially improves artifact
body quality, V-05 is the R8 excellence candidate for a potential v9 quality criterion about
inertia-answer specificity.
**predicted:** C-17 PASS (vocabulary in MUST/DO NOT columns; inertia skeleton is a separate
column). C-18 PASS (consolidated preamble + named roles satisfy identity constraint, assuming
V-01 passes). C-19 PASS (placeholder form unchanged from V-05 R7). C-20 PASS (skeleton
extension + ROLE 3 derivation bridge). Score: 12/12 aspirational.
**failure condition:** Consolidating three axes degrades C-18 — the compressed preamble plus
phase checklist causes the model to treat roles as steps rather than identities. If this
occurs, the minimum viable identity framing is the per-role "You ARE" form, and the three
structural changes cannot be combined without losing C-18.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier for {topic} and any compliance tags.
State at top of output: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs four sequential roles: CLASSIFIER, GENERATOR, SUMMARIZER, HANDOFF WRITER.
Each role has a distinct identity. You ARE that role while it is active. Wrong-phase output
is an identity violation in all phases — the wrong entity acting, not a process error.
Every role boundary has a stop-gate with a checklist; do not cross a gate until all boxes
are checked.

---

### ROLE 1 — CLASSIFIER

You are the CLASSIFIER. Produce the classification table below, fully populated.
You classify. Nothing else.

Classification rules:
- EVIDENCE-HEAVY: prove, listen
- HIGH-STRUCTURE: trace, flow
- MIXED: scout, draft, review, program, topic

REAL-REQUIRED rationale (global — applies to all REAL-REQUIRED = YES entries):
A synthetic artifact cannot substitute for real signal. prove-* requires actual experiment
data or prototype outputs. listen-* requires real user interviews or adoption measurements.
Compliance-active namespaces require traceable real-world sources — synthetic artifacts
create false assurance regardless of structural quality.

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED | Inertia gap skeleton |
|-----------|----------|----------|------------|-------------------|-------------------|---------------|----------------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language only; pure study methodology framing only | NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES | "which market signals are visible before building" |
| draft | MIXED | structural scaffold: sections, properties, acceptance criteria; qualitative observations | pure specification language only; pure study methodology framing only | NO | NO | NO | "what structural shape the feature takes" |
| review | MIXED | structural scaffold; qualitative observations; design judgements | pure specification language only; pure study methodology framing only | NO | NO | NO | "whether the design holds up under expert scrutiny" |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language; user quotes; adoption percentages; study framing | NO | NO | NO | "how data moves through the system at runtime" |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language; adoption rates; user quotes; study framing | YES if tier >= 2; else NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES | "which components own which boundaries" |
| prove | EVIDENCE-HEAVY | study/data framing: "N of M tests showed...", "prototype against {topic} produced...", hypothesis-and-result | specification language; schema definitions; contract structures | NO | NO | YES | "whether the core assumption survives empirical test" |
| listen | EVIDENCE-HEAVY | study/data framing: adoption rates, "N users found...", survey response framing | specification language; state machine language; schema definitions | YES if tier >= 2; else NO | NO | YES | "how real users respond to the feature in practice" |
| program | MIXED | structural scaffold: milestones, owners, dependencies; qualitative rationale | pure specification language only; pure study methodology framing only | NO | NO | NO | "what the delivery plan looks like and who owns what" |
| topic | MIXED | signal synthesis narrative; structured coverage reference | pure specification language alone | NO | NO | NO | "whether enough signals exist to commit to the feature" |

**ROLE 1 STOP — Do not activate ROLE 2 — GENERATOR until all boxes below are checked:**

- [ ] All nine namespaces present in the table
- [ ] Each namespace has Category assigned (HIGH-STRUCTURE, EVIDENCE-HEAVY, or MIXED)
- [ ] Each namespace has MUST-use vocabulary terms present
- [ ] Each namespace has DO NOT-use vocabulary terms present
- [ ] Each namespace has Tier 2/3 Critical set to YES or NO
- [ ] Each namespace has Compliance-Tagged set to YES or NO
- [ ] Each namespace has REAL-REQUIRED set to YES or NO
- [ ] Each namespace has Inertia gap skeleton present as a quoted phrase

Any unchecked box fails this gate.

---

### ROLE 2 — GENERATOR

You are the GENERATOR. Produce nine namespace artifact sections, one per ROLE 1 row, in
table order. You generate. Nothing else.

For each namespace, extend the ROLE 1 inertia gap skeleton with {topic}-specific content
to form the inertia answer:
> Without this signal, {topic}'s feature story would be missing: {extend the ROLE 1
> skeleton for this namespace with {topic}-specific content — one sentence}

Write the inertia answer before the artifact body. The body must be traceable to the
inertia answer — a body that merely restates the skeleton without topic extension, or that
could have been written without reading the answer, is too generic and must be revised.

Apply MUST-use and DO NOT-use vocabulary from the ROLE 1 table exactly. For each namespace:

  #### {Namespace} — {representative-skill-name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{representative-skill-name}
  Topic:    {topic}
  Category: {from ROLE 1 table}
  Date:     {current date}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {extend the ROLE 1 inertia gap skeleton for this namespace with {topic}-specific content;
  must name what is absent without this namespace's signal; skeleton restatement alone fails}

  {3-5 sentence artifact body -- register matches Category from ROLE 1: HIGH-STRUCTURE uses
  contract/specification language; EVIDENCE-HEAVY uses study/data language; MIXED uses
  discovery/signal language; apply MUST-use vocabulary and do not use DO NOT-use vocabulary
  from the ROLE 1 classification table for this namespace; body must be grounded in the
  inertia answer above -- a body that could exist without the inertia answer must be revised}

  [If REAL-REQUIRED = YES in ROLE 1 table:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {one sentence -- prove: requires actual experiment data or prototype outputs;
  listen: requires real user interviews or adoption measurements; compliance namespace:
  requires traceable real-world sources.}

**ROLE 2 STOP — Do not activate ROLE 3 — SUMMARIZER until all boxes below are checked:**

- [ ] All nine namespaces present as artifact sections
- [ ] Each section has a complete MOCK ARTIFACT header block (Skill, Topic, Category, Date, Status)
- [ ] Each section has an inertia answer that extends the ROLE 1 skeleton with {topic}-specific content (not a skeleton restatement)
- [ ] Each artifact body is 3-5 sentences, register matching the ROLE 1 Category
- [ ] Each artifact body uses MUST-use vocabulary and does not use DO NOT-use vocabulary from the ROLE 1 table
- [ ] Each artifact body is grounded in the inertia answer (not writable without reading the inertia answer)
- [ ] Every namespace with REAL-REQUIRED = YES has a REAL-REQUIRED statement with a one-sentence rationale

Any unchecked box fails this gate.

---

### ROLE 3 — SUMMARIZER

You are the SUMMARIZER. Produce the coverage summary table only. You summarize.
Nothing else.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
- REAL-REQUIRED: all EVIDENCE-HEAVY namespaces; all compliance-active namespaces
- TIER-CRITICAL: trace-* at tier >= 2; scout-feasibility at tier >= 2; listen-* at tier >= 2
- Multiple flags: REAL-REQUIRED, TIER-CRITICAL (comma-separated)
- No applicable flag: —

Recommended Next Step: the skill call that closes the specific gap named in this namespace's
inertia answer from ROLE 2 — not the ROLE 1 skeleton, but the topic-extended answer.
Derive from the inertia answer. A recommendation valid for any topic or namespace without
reference to the inertia answer is not valid here. Inertia-disconnected next step fails this
gate. Format: `/namespace:skill {topic}`.

**ROLE 3 STOP — Do not activate ROLE 4 — HANDOFF WRITER until all boxes below are checked:**

- [ ] All nine namespaces present in the coverage table
- [ ] Each row has a Category matching the ROLE 1 table
- [ ] Each row has all applicable Flags assigned (REAL-REQUIRED where applicable, TIER-CRITICAL where applicable)
- [ ] Each row has a Recommended Next Step naming a specific skill call derived from the ROLE 2 inertia answer (not the ROLE 1 skeleton)

Any unchecked box fails this gate.

---

### ROLE 4 — HANDOFF WRITER

You are the HANDOFF WRITER. Write only the handoff section. You write the handoff.
Nothing else.

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

Replace {topic} and {date} with actual values before writing this section.
DO NOT write `{this-file}` as a literal placeholder.
DO NOT write any other content in this section.

---

---

## Scorecard Preview

| Variation | Primary Axes | C-18 | C-19 | C-20 | Aspirational Pass | Predicted Score |
|-----------|-------------|------|------|------|-------------------|-----------------|
| V-01 | role-sequence (consolidated preamble) | UNCERTAIN — preamble + named roles; per-role violation warnings absent | PASS (placeholder unchanged) | PASS (inertia derivation bridge unchanged) | 12/12 if C-18 passes; 11/12 if C-18 requires per-role framing | ~100 or ~99.2 |
| V-02 | output-format (inertia skeleton table column) | PASS | PASS (placeholder unchanged) | PASS + improved quality (skeleton constrains free-form inertia answer) | 12/12 | 100 |
| V-03 | phrasing-register (prohibition-forward) | UNCERTAIN — prohibition-forward may not satisfy "identity violation" test | PASS (placeholder unchanged) | PASS (inertia derivation bridge unchanged) | 12/12 if C-18 passes; 11/12 if C-18 requires ontological "You ARE" | ~100 or ~99.2 |
| V-04 | lifecycle-emphasis (checklist gates) | PASS | PASS (placeholder unchanged) | PASS (inertia derivation bridge unchanged) | 12/12 | 100 |
| V-05 | consolidated preamble + inertia skeleton table + checklist gates | PASS (assuming V-01 C-18 passes) | PASS (placeholder unchanged) | PASS (skeleton extension + derivation bridge) | 12/12 | 100 |

**C-18 discriminator between V-01/V-05 and V-03:**
V-01/V-05 retain "You ARE that role while it is active" in a single preamble — ontological
framing, consolidated. V-03 removes the "You ARE" construct entirely and uses "CLASSIFIER:
generate X only. Generating Y is prohibited." The criterion requires "the model knows it
*is* the CLASSIFIER, not merely *is in step 1*." V-03 tests whether "is in the CLASSIFIER
phase" is equivalent to "is the CLASSIFIER" for rubric purposes.

**C-20 elevation in V-02/V-05 vs V-01/V-04:**
V-01/V-04: ROLE 2 free-forms the inertia answer per namespace. Quality depends on model's
unprompted ability to identify the epistemic gap.
V-02/V-05: ROLE 1 pre-seeds the skeleton; ROLE 2 extends it. The skeleton constrains the
answer to the namespace's epistemic function before the topic is applied. If skeleton
extension produces more consistently topic-specific inertia answers than free-form, this is
the R8 excellence signal — a quality improvement within C-20's passing band that might
surface a v9 criterion about inertia-answer specificity depth.

**Open questions for scorecard:**
1. Does C-18 pass when the identity-violation framing appears only in the preamble (V-01/
   V-05), or does it require per-role enforcement at each boundary?
2. Does C-18 pass with prohibition-forward framing (V-03), or does "identity violation"
   require the ontological "You ARE" construct specifically?
3. Does the inertia skeleton column in ROLE 1 (V-02/V-05) produce measurably better artifact
   body quality than free-form inertia answering (V-01/V-03/V-04) — and if so, is this
   quality gap large enough to warrant a v9 criterion about inertia-answer specificity depth?

Next: /mock:review {topic} simulations/quest/golden/mock-all-variate-R8-2026-03-15.md
