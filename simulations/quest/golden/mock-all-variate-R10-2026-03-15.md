---
skill: quest-variate
skill_target: mock-all
date: 2026-03-15
round: 10
rubric_version: v10
status: VARIATE
---

# mock-all Variate — Round 10

**Date:** 2026-03-15
**Skill:** mock-all
**Rubric:** v10 (C-01 through C-23; aspirational denominator = 15)
**Round:** R10 — one new criterion; R9 V-04 is the reference ceiling at 14/14

---

## What R9 Left Open

v10 adds one new aspirational criterion extracted from the structural gap between R9 V-02 and
R9 V-04:

| Criterion | Source | What it tests |
|-----------|--------|---------------|
| C-23 | R9 V-04 ceiling — per-role header combines positive identity affirmation ("You ARE the CLASSIFIER") with entity-transition violation ("you have become the GENERATOR, which you are not yet"); R9 V-02 had only entity-transition (naming wrong entity) with positive identity deferred to preamble | Each per-role activation header must carry both elements: (1) `You ARE the [SPECIFIC ROLE]` as first element, and (2) entity-transition violation statement. Preamble-level identity + per-role violation satisfies C-22 but not C-23. The diagnostic test: does each role-activation header contain `You ARE the [SPECIFIC ROLE]` as its first element? |

The denominator rises from 14 to 15. R9 V-04 (14/14) is re-scored under v10: if V-04 already
carries the two-part per-role header at all four role activations, it scores 15/15. R10 confirms
this and explores the C-23 boundary systematically.

The three-rung staircase that v10 makes explicit:
- C-18: named role at each boundary + any identity-violation mechanism in the skill (minimum)
- C-22: identity-violation mechanism must be ontological self-contradiction, not prohibition
- C-23: positive identity affirmation must appear at each per-role activation header, not only preamble

---

## Axis-Assignment Plan

| Variation | Axis | Source signal | Target criteria | Predicted score |
|-----------|------|---------------|-----------------|-----------------|
| V-01 | phrasing-register (conditional positive identity: "In the CLASSIFIER role" instead of "You ARE the CLASSIFIER") | C-23 specifies "You ARE the [SPECIFIC ROLE]" as first element; conditional phrasing ("In the X role") does not satisfy positive affirmation | C-22: PASS (entity-transition preserved); C-23: FAIL (no "You ARE" positive affirmation at activation) | 14/15 aspirational |
| V-02 | ceiling form — R9 V-04 base with all four role activations carrying two-part C-23 header | R9 V-04 demonstrated C-23 passability; V-02 is the positive control confirming 15/15 against v10 | C-23: PASS; all other criteria: PASS (inherited from R9 V-04) | 15/15 aspirational |
| V-03 | lifecycle-emphasis (preamble-deferred positive identity: "You ARE each role while it is active" in preamble; per-role headers carry entity-transition only) | C-22 passes via per-role entity-transition (naming no longer CLASSIFIER); C-23 fails because positive "You ARE the CLASSIFIER" does not appear at activation point | C-22: PASS (entity-transition in per-role header); C-23: FAIL (positive affirmation deferred to preamble) | 14/15 aspirational |
| V-04 | combination: phrasing-register (formal) + output-format (role-launch block at each activation carrying both C-23 elements in structured key-value form) | Tests whether structured block format can carry C-23 when both "You ARE: CLASSIFIER" and the violation statement appear as adjacent block fields at each activation | C-22: PASS; C-23: PASS (if block format carries both elements at activation point) | 15/15 aspirational |
| V-05 | regression: R9 V-02 baseline tested against v10 rubric | R9 V-02 used "You are the CLASSIFIER" (lowercase "are") and "Writing an artifact body here means you are ROLE 2 — GENERATOR, which you are not yet" — positive affirmation was lowercase and did not use the full entity-departure form | C-22: PASS (entity named in violation); C-23: FAIL (lowercase "are", no "no longer the CLASSIFIER" departure) | 14/15 aspirational |

---

## V-01 — Phrasing Register: Conditional Positive Identity (Single Axis)

**axis:** phrasing-register — conditional role framing ("In the CLASSIFIER role, ...") instead of
affirmative identity claim ("You ARE the CLASSIFIER") at each role activation header

**hypothesis:** C-23 diagnostic test requires "You ARE the [SPECIFIC ROLE]" as the first element
of each per-role header. A conditional role framing ("In the CLASSIFIER role") denotes incumbency
without asserting identity — the model is described as occupying a role, not *being* it. This
preserves C-22 (entity-transition statement and ontological mechanism are unchanged) but removes
the positive affirmation C-23 requires. Predicted: C-22 PASS (entity-transition present at each
boundary: "you are no longer the CLASSIFIER — you have become the GENERATOR, which you are not
yet"), C-23 FAIL (no "You ARE" first element at any activation). All criteria C-01 through C-22:
PASS. Score: 14/15 aspirational.

**failure condition:** C-22 also fails — if the grader treats conditional framing as weakening
the ontological mechanism (not just the positive affirmation), both C-22 and C-23 fail and the
score drops to 13/15. Watch for this: V-01 is designed to isolate C-23 from C-22, so if C-22
also fails, that exposes an over-coupling in the criteria boundary.

**predicted:** 14/15. Expected composite: 60 (essential) + 30 (recommended) + 10*(14/15) = 99.3

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier for {topic} and any compliance tags.
State at top of output: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs four sequential roles. Each role has a distinct identity. Each role is
exclusively active during its phase. Activating the wrong role is a categorical error: the
wrong entity acting. Each role begins at its header. Each role ends at its STOP gate.
Do not cross a STOP gate until its conditions are met.

---

### ROLE 1 — CLASSIFIER

In the CLASSIFIER role, your output is the classification table below, fully populated.
Writing an artifact body here means you are no longer the CLASSIFIER — you have become the
GENERATOR, which you are not yet. Writing a coverage summary means you are no longer the
CLASSIFIER — you have become the SUMMARIZER, which you are not yet.
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

The "Inertia gap skeleton" column contains a namespace-level phrase characterizing what each
namespace's signal provides, independently of any topic. ROLE 2 — the GENERATOR — extends
each skeleton phrase with {topic}-specific content, making topic specificity additive rather
than originating.

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED | Inertia gap skeleton |
|-----------|----------|----------|------------|-------------------|-------------------|---------------|----------------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language only; pure study methodology framing only | NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES | "which market signals and open directional hypotheses existed before any build decision" |
| draft | MIXED | structural scaffold: sections, properties, acceptance criteria; qualitative observations | pure specification language only; pure study methodology framing only | NO | NO | NO | "what structural constraints and acceptance criteria bounded the design space before implementation" |
| review | MIXED | qualitative observations; design judgments; structural rationale | pure specification language only; pure study methodology framing only | NO | NO | NO | "what design judgments and expert assessments surrounded the structural decisions" |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language; user quotes; adoption percentages; study framing | NO | NO | NO | "what state-transition contracts and trigger conditions define the runtime behavior envelope" |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language; adoption rates; user quotes; study framing | YES if tier >= 2; else NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES | "what component boundaries, interface contracts, and permission grants are formally specified" |
| prove | EVIDENCE-HEAVY | study/data framing: "N of M tests showed...", "prototype against {topic} produced...", hypothesis-and-result | specification language; schema definitions; contract structures | NO | NO | YES | "whether the core technical assumption survives empirical test against real conditions" |
| listen | EVIDENCE-HEAVY | study/data framing: adoption rates, "N users found...", survey response framing | specification language; state machine language; schema definitions | YES if tier >= 2; else NO | NO | YES | "what actual users reported about adoption friction and workflow fit" |
| program | MIXED | structural scaffold: milestones, owners, dependencies; qualitative rationale | pure specification language only; pure study methodology framing only | NO | NO | NO | "what milestone sequencing, ownership assignments, and dependency constraints were planned" |
| topic | MIXED | signal synthesis narrative; structured coverage reference | pure specification language alone | NO | NO | NO | "what the combined signal picture says about coverage completeness and next-step priority" |

**ROLE 1 STOP — Do not activate ROLE 2 — GENERATOR until all nine namespaces have all eight
fields populated: (1) Category; (2) MUST-use vocabulary; (3) DO NOT-use vocabulary; (4) Tier
2/3 Critical; (5) Compliance-Tagged; (6) REAL-REQUIRED; (7) Inertia gap skeleton as a quoted
phrase filling the namespace-level blank. Any empty cell means you are still the CLASSIFIER —
do not become the GENERATOR until all eight fields are present.**

---

### ROLE 2 — GENERATOR

In the GENERATOR role, your output is nine namespace artifact sections. Writing a
classification table here means you are no longer the GENERATOR — you have become the
CLASSIFIER, which is no longer active. Writing a coverage summary means you are no longer the
GENERATOR — you have become the SUMMARIZER, which you are not yet.
You generate. Nothing else.

For each namespace, extend the ROLE 1 inertia gap skeleton with {topic}-specific content:
> Without this signal, {topic}'s feature story would be missing: {extend the ROLE 1 skeleton
> for this namespace — add what is specifically absent for {topic}; one sentence total}

Write the inertia answer immediately before the artifact body. A body that merely appends
"{topic}" to the ROLE 1 skeleton without substantive extension, or that could exist without
reading the skeleton, must be revised before this role ends.

For each namespace:

  #### {Namespace} — {representative-skill-name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{representative-skill-name}
  Topic:    {topic}
  Category: {from ROLE 1 table}
  Date:     {current date}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {extend the ROLE 1 skeleton with {topic}-specific content — one sentence total; the
  skeleton sets the namespace's epistemic function; this sentence names what is specifically
  absent for {topic}; "the signal" alone or skeleton-echo fails this field}

  {3-5 sentence artifact body — register matches Category: HIGH-STRUCTURE uses
  contract/specification language; EVIDENCE-HEAVY uses study/data language; MIXED uses
  discovery/signal language; apply MUST-use vocabulary, avoid DO NOT-use vocabulary;
  body must be traceable to the extended inertia answer above}

  [If REAL-REQUIRED = YES in ROLE 1 table:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {one sentence — prove: requires actual experiment data; listen: requires real
  user feedback; compliance namespace: requires traceable real-world sources.}

**ROLE 2 STOP — Do not activate ROLE 3 — SUMMARIZER until: (1) nine sections present; (2)
each has a complete MOCK ARTIFACT header (Skill, Topic, Category, Date, Status: MOCK); (3)
each inertia answer extends the ROLE 1 skeleton with topic-specific content — skeleton-echo
alone fails; (4) each body is 3-5 sentences, vocabulary-compliant, register-matched, grounded
in the extended inertia answer; (5) every REAL-REQUIRED = YES namespace has a rationale
statement. If any condition is unmet, you are still the GENERATOR — do not become the
SUMMARIZER until all five conditions pass.**

---

### ROLE 3 — SUMMARIZER

In the SUMMARIZER role, your output is the coverage summary table. Writing new artifact
bodies here means you are no longer the SUMMARIZER — you have become the GENERATOR, which
is no longer active. Writing the handoff line means you are no longer the SUMMARIZER — you
have become the HANDOFF WRITER, which you are not yet.
You summarize. Nothing else.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
- REAL-REQUIRED: all EVIDENCE-HEAVY namespaces; all compliance-active namespaces
- TIER-2-CRITICAL: trace at tier >= 2; scout-feasibility at tier >= 2
- TIER-3-CRITICAL: listen at tier >= 2
- Multiple flags: comma-separated
- No applicable flag: —

Recommended Next Step: derive from the ROLE 2 extended inertia answer — the topic-specific
extension, not the ROLE 1 skeleton alone. Format: `/namespace:skill {topic}`. An inertia-
disconnected next step fails this gate.

**ROLE 3 STOP — Do not activate ROLE 4 — HANDOFF WRITER until: (1) nine rows present; (2)
each row has Category matching ROLE 1; (3) each row has all applicable Flags; (4) each
Recommended Next Step is derived from the ROLE 2 inertia answer. If any condition is unmet,
you are still the SUMMARIZER — do not become the HANDOFF WRITER until all four conditions pass.**

---

### ROLE 4 — HANDOFF WRITER

In the HANDOFF WRITER role, your output is the handoff section only. Writing a coverage
table here means you are no longer the HANDOFF WRITER — you have become the SUMMARIZER,
which is no longer active. You write the handoff. Nothing else.

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

Replace {topic} and {date} with actual values before writing this section.
DO NOT write `{this-file}` as a literal placeholder.
DO NOT write any other content in this section.

---

---

## V-02 — Ceiling Form: Two-Part Per-Role Header at All Four Activations (Single Axis)

**axis:** phrasing-register — explicit positive identity affirmation ("You ARE the [ROLE]") as
first element of every per-role activation header, combined with full entity-departure transition
("you are no longer the [ROLE] — you have become the [OTHER ROLE], which you are not yet")

**hypothesis:** C-23 requires both elements at each per-role activation: (1) "You ARE the
[SPECIFIC ROLE]" as first element, and (2) entity-transition naming the departure from current
role and arrival at wrong role. R9 V-04 demonstrated this form at ROLE 1 and ROLE 2; V-02
confirms C-23 at all four role boundaries (ROLE 1 through ROLE 4). All other criteria inherited
from R9 V-04. Predicted: C-23 PASS at all four activations. Score: 15/15 aspirational.

**failure condition:** An unexpected criterion fails outside C-23 — most likely C-19 (depth
anchor form — sentence count as first token inside placeholder) or C-20 (inertia answer
topic-specificity — ROLE 2 appends "{topic}" to skeleton without substantive extension). The
skeleton extension instruction must produce additive topic content, not skeleton-echo. If either
fails, the score drops to 14/15 and the criterion gap is not C-23 but one of the content-quality
criteria.

**predicted:** 15/15. Expected composite: 60 + 30 + 10*(15/15) = 100

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier for {topic} and any compliance tags.
State at top of output: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs four sequential roles. Each role has a distinct identity. You ARE that role
while it is active. Activating the wrong role is not a procedural error — it is a categorical
error: the wrong entity acting. Each role begins at its header. Each role ends at its STOP gate.
Do not cross a STOP gate until its conditions are met.

---

### ROLE 1 — CLASSIFIER

You ARE the CLASSIFIER. Writing an artifact body here means you are no longer the CLASSIFIER
— you have become the GENERATOR, which you are not yet. Writing a coverage summary means you
are no longer the CLASSIFIER — you have become the SUMMARIZER, which you are not yet.
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

The "Inertia gap skeleton" column contains a namespace-level phrase characterizing what each
namespace's signal provides, independently of any topic. ROLE 2 — the GENERATOR — extends
each skeleton phrase with {topic}-specific content, making topic specificity additive rather
than originating.

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED | Inertia gap skeleton |
|-----------|----------|----------|------------|-------------------|-------------------|---------------|----------------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language only; pure study methodology framing only | NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES | "which market signals and open directional hypotheses existed before any build decision" |
| draft | MIXED | structural scaffold: sections, properties, acceptance criteria; qualitative observations | pure specification language only; pure study methodology framing only | NO | NO | NO | "what structural constraints and acceptance criteria bounded the design space before implementation" |
| review | MIXED | qualitative observations; design judgments; structural rationale | pure specification language only; pure study methodology framing only | NO | NO | NO | "what design judgments and expert assessments surrounded the structural decisions" |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language; user quotes; adoption percentages; study framing | NO | NO | NO | "what state-transition contracts and trigger conditions define the runtime behavior envelope" |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language; adoption rates; user quotes; study framing | YES if tier >= 2; else NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES | "what component boundaries, interface contracts, and permission grants are formally specified" |
| prove | EVIDENCE-HEAVY | study/data framing: "N of M tests showed...", "prototype against {topic} produced...", hypothesis-and-result | specification language; schema definitions; contract structures | NO | NO | YES | "whether the core technical assumption survives empirical test against real conditions" |
| listen | EVIDENCE-HEAVY | study/data framing: adoption rates, "N users found...", survey response framing | specification language; state machine language; schema definitions | YES if tier >= 2; else NO | NO | YES | "what actual users reported about adoption friction and workflow fit" |
| program | MIXED | structural scaffold: milestones, owners, dependencies; qualitative rationale | pure specification language only; pure study methodology framing only | NO | NO | NO | "what milestone sequencing, ownership assignments, and dependency constraints were planned" |
| topic | MIXED | signal synthesis narrative; structured coverage reference | pure specification language alone | NO | NO | NO | "what the combined signal picture says about coverage completeness and next-step priority" |

**ROLE 1 STOP — Do not activate ROLE 2 — GENERATOR until all nine namespaces have all eight
fields populated: (1) Category; (2) MUST-use vocabulary; (3) DO NOT-use vocabulary; (4) Tier
2/3 Critical; (5) Compliance-Tagged; (6) REAL-REQUIRED; (7) Inertia gap skeleton as a quoted
phrase filling the namespace-level blank. Any empty cell means you are still the CLASSIFIER —
do not become the GENERATOR until all eight fields are present.**

---

### ROLE 2 — GENERATOR

You ARE the GENERATOR. Writing a classification table here means you are no longer the
GENERATOR — you have become the CLASSIFIER, which is no longer active. Writing a coverage
summary here means you are no longer the GENERATOR — you have become the SUMMARIZER, which
you are not yet. You generate. Nothing else.

For each namespace, extend the ROLE 1 inertia gap skeleton with {topic}-specific content:
> Without this signal, {topic}'s feature story would be missing: {extend the ROLE 1 skeleton
> for this namespace — add what is specifically absent for {topic}; one sentence total}

Write the inertia answer immediately before the artifact body. A body that merely appends
"{topic}" to the ROLE 1 skeleton without substantive extension, or that could exist without
reading the skeleton, must be revised before this role ends.

For each namespace:

  #### {Namespace} — {representative-skill-name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{representative-skill-name}
  Topic:    {topic}
  Category: {from ROLE 1 table}
  Date:     {current date}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {extend the ROLE 1 skeleton with {topic}-specific content — one sentence total; the
  skeleton sets the namespace's epistemic function; this sentence names what is specifically
  absent for {topic}; "the signal" alone or skeleton-echo fails this field}

  {3-5 sentence artifact body — register matches Category: HIGH-STRUCTURE uses
  contract/specification language; EVIDENCE-HEAVY uses study/data language; MIXED uses
  discovery/signal language; apply MUST-use vocabulary, avoid DO NOT-use vocabulary;
  body must be traceable to the extended inertia answer above}

  [If REAL-REQUIRED = YES in ROLE 1 table:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {one sentence — prove: requires actual experiment data; listen: requires real
  user feedback; compliance namespace: requires traceable real-world sources.}

**ROLE 2 STOP — Do not activate ROLE 3 — SUMMARIZER until: (1) nine sections present; (2)
each has a complete MOCK ARTIFACT header (Skill, Topic, Category, Date, Status: MOCK); (3)
each inertia answer extends the ROLE 1 skeleton with topic-specific content — skeleton-echo
alone fails; (4) each body is 3-5 sentences, vocabulary-compliant, register-matched, grounded
in the extended inertia answer; (5) every REAL-REQUIRED = YES namespace has a rationale
statement. If any condition is unmet, you are still the GENERATOR — do not become the
SUMMARIZER until all five conditions pass.**

---

### ROLE 3 — SUMMARIZER

You ARE the SUMMARIZER. Writing new artifact bodies here means you are no longer the
SUMMARIZER — you have become the GENERATOR, which is no longer active. Writing the handoff
line here means you are no longer the SUMMARIZER — you have become the HANDOFF WRITER, which
you are not yet. You summarize. Nothing else.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
- REAL-REQUIRED: all EVIDENCE-HEAVY namespaces; all compliance-active namespaces
- TIER-2-CRITICAL: trace at tier >= 2; scout-feasibility at tier >= 2
- TIER-3-CRITICAL: listen at tier >= 2
- Multiple flags: comma-separated
- No applicable flag: —

Recommended Next Step: derive from the ROLE 2 extended inertia answer — the topic-specific
extension, not the ROLE 1 skeleton alone. Format: `/namespace:skill {topic}`. An inertia-
disconnected next step fails this gate.

**ROLE 3 STOP — Do not activate ROLE 4 — HANDOFF WRITER until: (1) nine rows present; (2)
each row has Category matching ROLE 1; (3) each row has all applicable Flags; (4) each
Recommended Next Step is derived from the ROLE 2 inertia answer. If any condition is unmet,
you are still the SUMMARIZER — do not become the HANDOFF WRITER until all four conditions pass.**

---

### ROLE 4 — HANDOFF WRITER

You ARE the HANDOFF WRITER. Writing a coverage table here means you are no longer the
HANDOFF WRITER — you have become the SUMMARIZER, which is no longer active. You write the
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

## V-03 — Lifecycle Emphasis: Preamble-Deferred Positive Identity (Single Axis, C-23 Negative Control)

**axis:** lifecycle-emphasis — positive identity affirmation moved to a single preamble
statement ("You ARE each role while it is active") rather than firing at each per-role
activation header; per-role headers carry entity-transition statement only

**hypothesis:** This is the documented negative control for C-23. The preamble establishes
generic identity ("you are that role while active"). Per-role headers carry the ontological
entity-transition ("you are no longer the CLASSIFIER — you have become the GENERATOR, which
you are not yet") but do not begin with "You ARE the CLASSIFIER." C-22 passes because each
per-role header contains the ontological self-contradiction mechanism. C-23 fails because the
per-role activation header does not contain "You ARE the [SPECIFIC ROLE]" as its first
element — positive identity lives only in the preamble. This variation explicitly traces the
C-22 / C-23 boundary: same entity-transition form, different placement of the positive
affirmation.

**predicted:** C-22 PASS; C-23 FAIL. Score: 14/15. Expected composite: 60 + 30 + 10*(14/15) = 99.3

**failure condition:** C-22 also fails — if the grader treats the absence of per-role
"You ARE" as weakening the ontological mechanism, both criteria fail. This is the same
failure mode as V-01 and would indicate the criteria are less separable than the rubric
claims. Scorecard should distinguish: C-22 tests the *mechanism type* (ontological vs
prohibition); C-23 tests the *placement* (preamble vs per-role header).

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier for {topic} and any compliance tags.
State at top of output: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs four sequential roles. You ARE each role while it is active — exclusively
that role, no other. Activating the wrong role is a categorical error: the wrong entity
acting. Each role begins at its header. Each role ends at its STOP gate. Do not cross a
STOP gate until its conditions are met.

---

### ROLE 1 — CLASSIFIER

Your sole output is the classification table below, fully populated. Writing an artifact
body here means you are no longer the CLASSIFIER — you have become the GENERATOR, which
you are not yet. Writing a coverage summary means you are no longer the CLASSIFIER — you
have become the SUMMARIZER, which you are not yet. You classify. Nothing else.

Classification rules:
- EVIDENCE-HEAVY: prove, listen
- HIGH-STRUCTURE: trace, flow
- MIXED: scout, draft, review, program, topic

REAL-REQUIRED rationale (applies to all EVIDENCE-HEAVY and compliance-active namespaces):
A synthetic artifact cannot substitute for real signal. prove-* requires actual experiment
data or prototype outputs. listen-* requires real user interviews or adoption measurements.
Compliance-active namespaces require traceable real-world sources — synthetic artifacts
create false assurance regardless of structural quality.

The "Inertia gap skeleton" column contains a namespace-level phrase characterizing what each
namespace's signal provides, independently of any topic. ROLE 2 — the GENERATOR — extends
each skeleton phrase with {topic}-specific content, making topic specificity additive rather
than originating.

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED | Inertia gap skeleton |
|-----------|----------|----------|------------|-------------------|-------------------|---------------|----------------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language only; pure study methodology framing only | NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES | "which market signals and open directional hypotheses existed before any build decision" |
| draft | MIXED | structural scaffold: sections, properties, acceptance criteria; qualitative observations | pure specification language only; pure study methodology framing only | NO | NO | NO | "what structural constraints and acceptance criteria bounded the design space before implementation" |
| review | MIXED | qualitative observations; design judgments; structural rationale | pure specification language only; pure study methodology framing only | NO | NO | NO | "what design judgments and expert assessments surrounded the structural decisions" |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language; user quotes; adoption percentages; study framing | NO | NO | NO | "what state-transition contracts and trigger conditions define the runtime behavior envelope" |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language; adoption rates; user quotes; study framing | YES if tier >= 2; else NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES | "what component boundaries, interface contracts, and permission grants are formally specified" |
| prove | EVIDENCE-HEAVY | study/data framing: "N of M tests showed...", "prototype against {topic} produced...", hypothesis-and-result | specification language; schema definitions; contract structures | NO | NO | YES | "whether the core technical assumption survives empirical test against real conditions" |
| listen | EVIDENCE-HEAVY | study/data framing: adoption rates, "N users found...", survey response framing | specification language; state machine language; schema definitions | YES if tier >= 2; else NO | NO | YES | "what actual users reported about adoption friction and workflow fit" |
| program | MIXED | structural scaffold: milestones, owners, dependencies; qualitative rationale | pure specification language only; pure study methodology framing only | NO | NO | NO | "what milestone sequencing, ownership assignments, and dependency constraints were planned" |
| topic | MIXED | signal synthesis narrative; structured coverage reference | pure specification language alone | NO | NO | NO | "what the combined signal picture says about coverage completeness and next-step priority" |

**ROLE 1 STOP — Do not activate ROLE 2 — GENERATOR until all nine namespaces have all eight
fields populated: (1) Category; (2) MUST-use vocabulary; (3) DO NOT-use vocabulary; (4) Tier
2/3 Critical; (5) Compliance-Tagged; (6) REAL-REQUIRED; (7) Inertia gap skeleton as a quoted
phrase filling the namespace-level blank. Any empty cell means you are still the CLASSIFIER —
do not become the GENERATOR until all eight fields are present.**

---

### ROLE 2 — GENERATOR

Your sole output is nine namespace artifact sections, one per ROLE 1 row, in table order.
Writing a classification table here means you are no longer the GENERATOR — you have become
the CLASSIFIER, which is no longer active. Writing a coverage summary means you are no longer
the GENERATOR — you have become the SUMMARIZER, which you are not yet. You generate. Nothing
else.

For each namespace, extend the ROLE 1 inertia gap skeleton with {topic}-specific content:
> Without this signal, {topic}'s feature story would be missing: {extend the ROLE 1 skeleton
> for this namespace — add what is specifically absent for {topic}; one sentence total}

Write the inertia answer immediately before the artifact body. A body that merely appends
"{topic}" to the ROLE 1 skeleton without substantive extension, or that could exist without
reading the skeleton, must be revised before this role ends.

For each namespace:

  #### {Namespace} — {representative-skill-name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{representative-skill-name}
  Topic:    {topic}
  Category: {from ROLE 1 table}
  Date:     {current date}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {extend the ROLE 1 skeleton with {topic}-specific content — one sentence total; the
  skeleton sets the namespace's epistemic function; this sentence names what is specifically
  absent for {topic}; "the signal" alone or skeleton-echo fails this field}

  {3-5 sentence artifact body — register matches Category: HIGH-STRUCTURE uses
  contract/specification language; EVIDENCE-HEAVY uses study/data language; MIXED uses
  discovery/signal language; apply MUST-use vocabulary, avoid DO NOT-use vocabulary;
  body must be traceable to the extended inertia answer above}

  [If REAL-REQUIRED = YES in ROLE 1 table:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {one sentence — prove: requires actual experiment data; listen: requires real
  user feedback; compliance namespace: requires traceable real-world sources.}

**ROLE 2 STOP — Do not activate ROLE 3 — SUMMARIZER until: (1) nine sections present; (2)
each has a complete MOCK ARTIFACT header (Skill, Topic, Category, Date, Status: MOCK); (3)
each inertia answer extends the ROLE 1 skeleton with topic-specific content — skeleton-echo
alone fails; (4) each body is 3-5 sentences, vocabulary-compliant, register-matched, grounded
in the extended inertia answer; (5) every REAL-REQUIRED = YES namespace has a rationale
statement. If any condition is unmet, you are still the GENERATOR — do not become the
SUMMARIZER until all five conditions pass.**

---

### ROLE 3 — SUMMARIZER

Your sole output is the coverage summary table. Writing artifact bodies here means you are
no longer the SUMMARIZER — you have become the GENERATOR, which is no longer active. Writing
the handoff line means you are no longer the SUMMARIZER — you have become the HANDOFF WRITER,
which you are not yet. You summarize. Nothing else.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
- REAL-REQUIRED: all EVIDENCE-HEAVY namespaces; all compliance-active namespaces
- TIER-2-CRITICAL: trace at tier >= 2; scout-feasibility at tier >= 2
- TIER-3-CRITICAL: listen at tier >= 2
- Multiple flags: comma-separated
- No applicable flag: —

Recommended Next Step: derive from the ROLE 2 extended inertia answer — the topic-specific
extension, not the ROLE 1 skeleton alone. Format: `/namespace:skill {topic}`. An inertia-
disconnected next step fails this gate.

**ROLE 3 STOP — Do not activate ROLE 4 — HANDOFF WRITER until: (1) nine rows present; (2)
each row has Category matching ROLE 1; (3) each row has all applicable Flags; (4) each
Recommended Next Step is derived from the ROLE 2 inertia answer. If any condition is unmet,
you are still the SUMMARIZER — do not become the HANDOFF WRITER until all four conditions pass.**

---

### ROLE 4 — HANDOFF WRITER

Your sole output is the handoff section. Writing a coverage table here means you are no
longer the HANDOFF WRITER — you have become the SUMMARIZER, which is no longer active. You
write the handoff. Nothing else.

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

Replace {topic} and {date} with actual values before writing this section.
DO NOT write `{this-file}` as a literal placeholder.
DO NOT write any other content in this section.

---

---

## V-04 — Combination: Output Format (Role-Launch Block) + Phrasing Register (C-23 at Block Level)

**axis:** combination: output-format (role activation expressed as a structured key-value
block instead of inline prose) + phrasing-register (C-23 two-part identity within the block:
"You ARE:" + "Violation:" as adjacent fields)

**hypothesis:** C-23 requires "You ARE the [SPECIFIC ROLE]" as the first element of the
per-role activation header. This variation tests whether a structured key-value block can
carry C-23 when "You ARE: the CLASSIFIER" appears as the first field and "Violation: Writing
artifact bodies means you are no longer the CLASSIFIER — you have become the GENERATOR, which
you are not yet" appears as the second field in the same block. The two C-23 elements are
present; the question is whether co-presence in a structured block counts as the "per-role
activation header" form. If block format passes C-23, it establishes an alternative structural
path to the ceiling. If it fails, C-23 requires inline prose specifically — a finding worth
capturing.

**predicted:** C-23 PASS (if block co-presence satisfies the criterion); C-22 PASS; all
other criteria PASS. Score: 15/15. If C-23 fails via block format, score: 14/15, and the
finding is that C-23 requires inline prose (not block fields).

**failure condition:** C-23 PARTIAL — grader accepts the block "You ARE:" field as positive
affirmation but requires the two elements to appear in a single prose sentence. Block format
satisfies the content requirement but not the structural co-location requirement.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier for {topic} and any compliance tags.
State at top of output: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs four sequential roles. Each role activation begins with a ROLE LAUNCH block
that declares the active identity. You ARE the role named in that block. Activating the wrong
role is not a procedural error — it is a categorical error: the wrong entity acting. Each role
ends at its STOP gate. Do not cross a STOP gate until its conditions are met.

---

### ROLE 1 — CLASSIFIER

```
ROLE LAUNCH
You ARE:    the CLASSIFIER
Violation:  Writing an artifact body here means you are no longer the CLASSIFIER —
            you have become the GENERATOR, which you are not yet.
            Writing a coverage summary means you are no longer the CLASSIFIER —
            you have become the SUMMARIZER, which you are not yet.
Mandate:    You classify. Nothing else.
```

Classification rules:
- EVIDENCE-HEAVY: prove, listen
- HIGH-STRUCTURE: trace, flow
- MIXED: scout, draft, review, program, topic

REAL-REQUIRED rationale (applies to all EVIDENCE-HEAVY and compliance-active namespaces):
A synthetic artifact cannot substitute for real signal. prove-* requires actual experiment
data or prototype outputs. listen-* requires real user interviews or adoption measurements.
Compliance-active namespaces require traceable real-world sources — synthetic artifacts
create false assurance regardless of structural quality.

The "Inertia gap skeleton" column contains a namespace-level phrase characterizing what each
namespace's signal provides, independently of any topic. ROLE 2 — the GENERATOR — extends
each skeleton phrase with {topic}-specific content, making topic specificity additive rather
than originating.

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED | Inertia gap skeleton |
|-----------|----------|----------|------------|-------------------|-------------------|---------------|----------------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language only; pure study methodology framing only | NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES | "which market signals and open directional hypotheses existed before any build decision" |
| draft | MIXED | structural scaffold: sections, properties, acceptance criteria; qualitative observations | pure specification language only; pure study methodology framing only | NO | NO | NO | "what structural constraints and acceptance criteria bounded the design space before implementation" |
| review | MIXED | qualitative observations; design judgments; structural rationale | pure specification language only; pure study methodology framing only | NO | NO | NO | "what design judgments and expert assessments surrounded the structural decisions" |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language; user quotes; adoption percentages; study framing | NO | NO | NO | "what state-transition contracts and trigger conditions define the runtime behavior envelope" |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language; adoption rates; user quotes; study framing | YES if tier >= 2; else NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES | "what component boundaries, interface contracts, and permission grants are formally specified" |
| prove | EVIDENCE-HEAVY | study/data framing: "N of M tests showed...", "prototype against {topic} produced...", hypothesis-and-result | specification language; schema definitions; contract structures | NO | NO | YES | "whether the core technical assumption survives empirical test against real conditions" |
| listen | EVIDENCE-HEAVY | study/data framing: adoption rates, "N users found...", survey response framing | specification language; state machine language; schema definitions | YES if tier >= 2; else NO | NO | YES | "what actual users reported about adoption friction and workflow fit" |
| program | MIXED | structural scaffold: milestones, owners, dependencies; qualitative rationale | pure specification language only; pure study methodology framing only | NO | NO | NO | "what milestone sequencing, ownership assignments, and dependency constraints were planned" |
| topic | MIXED | signal synthesis narrative; structured coverage reference | pure specification language alone | NO | NO | NO | "what the combined signal picture says about coverage completeness and next-step priority" |

**ROLE 1 STOP — Do not activate ROLE 2 — GENERATOR until all nine namespaces have all eight
fields populated: (1) Category; (2) MUST-use vocabulary; (3) DO NOT-use vocabulary; (4) Tier
2/3 Critical; (5) Compliance-Tagged; (6) REAL-REQUIRED; (7) Inertia gap skeleton as a quoted
phrase filling the namespace-level blank. Any empty cell means you are still the CLASSIFIER —
do not become the GENERATOR until all eight fields are present.**

---

### ROLE 2 — GENERATOR

```
ROLE LAUNCH
You ARE:    the GENERATOR
Violation:  Writing a classification table here means you are no longer the GENERATOR —
            you have become the CLASSIFIER, which is no longer active.
            Writing a coverage summary means you are no longer the GENERATOR —
            you have become the SUMMARIZER, which you are not yet.
Mandate:    You generate. Nothing else.
```

For each namespace, extend the ROLE 1 inertia gap skeleton with {topic}-specific content:
> Without this signal, {topic}'s feature story would be missing: {extend the ROLE 1 skeleton
> for this namespace — add what is specifically absent for {topic}; one sentence total}

Write the inertia answer immediately before the artifact body. A body that merely appends
"{topic}" to the ROLE 1 skeleton without substantive extension, or that could exist without
reading the skeleton, must be revised before this role ends.

For each namespace:

  #### {Namespace} — {representative-skill-name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{representative-skill-name}
  Topic:    {topic}
  Category: {from ROLE 1 table}
  Date:     {current date}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {extend the ROLE 1 skeleton with {topic}-specific content — one sentence total; the
  skeleton sets the namespace's epistemic function; this sentence names what is specifically
  absent for {topic}; "the signal" alone or skeleton-echo fails this field}

  {3-5 sentence artifact body — register matches Category: HIGH-STRUCTURE uses
  contract/specification language; EVIDENCE-HEAVY uses study/data language; MIXED uses
  discovery/signal language; apply MUST-use vocabulary, avoid DO NOT-use vocabulary;
  body must be traceable to the extended inertia answer above}

  [If REAL-REQUIRED = YES in ROLE 1 table:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {one sentence — prove: requires actual experiment data; listen: requires real
  user feedback; compliance namespace: requires traceable real-world sources.}

**ROLE 2 STOP — Do not activate ROLE 3 — SUMMARIZER until: (1) nine sections present; (2)
each has a complete MOCK ARTIFACT header (Skill, Topic, Category, Date, Status: MOCK); (3)
each inertia answer extends the ROLE 1 skeleton with topic-specific content — skeleton-echo
alone fails; (4) each body is 3-5 sentences, vocabulary-compliant, register-matched, grounded
in the extended inertia answer; (5) every REAL-REQUIRED = YES namespace has a rationale
statement. If any condition is unmet, you are still the GENERATOR — do not become the
SUMMARIZER until all five conditions pass.**

---

### ROLE 3 — SUMMARIZER

```
ROLE LAUNCH
You ARE:    the SUMMARIZER
Violation:  Writing new artifact bodies here means you are no longer the SUMMARIZER —
            you have become the GENERATOR, which is no longer active.
            Writing the handoff line means you are no longer the SUMMARIZER —
            you have become the HANDOFF WRITER, which you are not yet.
Mandate:    You summarize. Nothing else.
```

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
- REAL-REQUIRED: all EVIDENCE-HEAVY namespaces; all compliance-active namespaces
- TIER-2-CRITICAL: trace at tier >= 2; scout-feasibility at tier >= 2
- TIER-3-CRITICAL: listen at tier >= 2
- Multiple flags: comma-separated
- No applicable flag: —

Recommended Next Step: derive from the ROLE 2 extended inertia answer — the topic-specific
extension, not the ROLE 1 skeleton alone. Format: `/namespace:skill {topic}`. An inertia-
disconnected next step fails this gate.

**ROLE 3 STOP — Do not activate ROLE 4 — HANDOFF WRITER until: (1) nine rows present; (2)
each row has Category matching ROLE 1; (3) each row has all applicable Flags; (4) each
Recommended Next Step is derived from the ROLE 2 inertia answer. If any condition is unmet,
you are still the SUMMARIZER — do not become the HANDOFF WRITER until all four conditions pass.**

---

### ROLE 4 — HANDOFF WRITER

```
ROLE LAUNCH
You ARE:    the HANDOFF WRITER
Violation:  Writing a coverage table here means you are no longer the HANDOFF WRITER —
            you have become the SUMMARIZER, which is no longer active.
Mandate:    You write the handoff. Nothing else.
```

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

Replace {topic} and {date} with actual values before writing this section.
DO NOT write `{this-file}` as a literal placeholder.
DO NOT write any other content in this section.

---

---

## V-05 — Regression: R9 V-02 Baseline Against v10 Rubric

**axis:** regression — R9 V-02 baseline (lowercase "are" + ROLE N designation in violation
statement) retested under v10 to confirm C-23 scoring and document the exact form that fails

**hypothesis:** R9 V-02 scored 14/14 under v9. Under v10, C-23 diagnostic test: does each
role-activation header contain "You ARE the [SPECIFIC ROLE]" as its first element? R9 V-02
has "You are the CLASSIFIER" (lowercase "are") at per-role headers, and the violation
statement says "you are ROLE 2 — GENERATOR, which you are not yet" (not "you are no longer
the CLASSIFIER — you have become the GENERATOR"). Two differences from V-02 (ceiling): (1)
lowercase "are" vs emphatic "ARE", and (2) violation names destination role-number + name
("ROLE 2 — GENERATOR") rather than naming departure from current role ("no longer the
CLASSIFIER"). C-23 is expected to fail: the positive affirmation element is weakened by
lowercase "are" (emphasis absent) and the entity-transition form uses destination-naming
rather than departure+destination naming. Score under v10: 14/15.

**predicted:** C-22 PASS (entity-transition naming present, names wrong entity); C-23 FAIL
(lowercase "are", entity-transition does not use departure form "no longer the CLASSIFIER").
Score: 14/15. If C-23 PASS (grader accepts lowercase "are" as equivalent), then R9 V-02
already achieved the ceiling and C-23 was redundant with C-22 — a finding to escalate.

**failure condition:** C-23 PASS — the grader accepts "You are the CLASSIFIER" as satisfying
"You ARE the [SPECIFIC ROLE]". This would mean the distinction between V-02 (ceiling) and
V-05 (regression) is the entity-transition form only, not the emphasis. Escalate to criteria
review: is capital ARE load-bearing or is the first-element requirement the structural test?

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

The "Inertia gap skeleton" column contains namespace-level phrases that characterize what
each namespace's signal provides, independently of any topic. ROLE 2 will extend each
skeleton with {topic}-specific content. The skeleton is the namespace-level seed; the
topic-specific extension is ROLE 2's additive contribution.

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED | Inertia gap skeleton |
|-----------|----------|----------|------------|-------------------|-------------------|---------------|----------------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language only; pure study methodology framing only | NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES | "which market signals and open directional hypotheses existed before any build decision" |
| draft | MIXED | structural scaffold: sections, properties, acceptance criteria; qualitative observations | pure specification language only; pure study methodology framing only | NO | NO | NO | "what structural constraints and acceptance criteria bounded the design space before implementation" |
| review | MIXED | qualitative observations; design judgments; structural rationale | pure specification language only; pure study methodology framing only | NO | NO | NO | "what design judgments and expert assessments surrounded the structural decisions" |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language; user quotes; adoption percentages; study framing | NO | NO | NO | "what state-transition contracts and trigger conditions define the runtime behavior envelope" |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language; adoption rates; user quotes; study framing | YES if tier >= 2; else NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES | "what component boundaries, interface contracts, and permission grants are formally specified" |
| prove | EVIDENCE-HEAVY | study/data framing: "N of M tests showed...", "prototype against {topic} produced...", hypothesis-and-result | specification language; schema definitions; contract structures | NO | NO | YES | "whether the core technical assumption survives empirical test against real conditions" |
| listen | EVIDENCE-HEAVY | study/data framing: adoption rates, "N users found...", survey response framing | specification language; state machine language; schema definitions | YES if tier >= 2; else NO | NO | YES | "what actual users reported about adoption friction and workflow fit" |
| program | MIXED | structural scaffold: milestones, owners, dependencies; qualitative rationale | pure specification language only; pure study methodology framing only | NO | NO | NO | "what milestone sequencing, ownership assignments, and dependency constraints were planned" |
| topic | MIXED | signal synthesis narrative; structured coverage reference | pure specification language alone | NO | NO | NO | "what the combined signal picture says about coverage completeness and next-step priority" |

**ROLE 1 STOP — Do not activate ROLE 2 — GENERATOR until all nine namespaces have all eight
fields populated: (1) Category; (2) MUST-use vocabulary; (3) DO NOT-use vocabulary; (4) Tier
2/3 Critical; (5) Compliance-Tagged; (6) REAL-REQUIRED; (7) Inertia gap skeleton as a
quoted phrase characterizing the namespace's epistemic function. Any empty cell fails this gate.**

---

### ROLE 2 — GENERATOR

You are the GENERATOR. Your sole output is nine namespace artifact sections, one per ROLE 1
row, in table order. Writing a coverage summary means you are ROLE 3 — SUMMARIZER, which you
are not yet. Writing a handoff line means you are ROLE 4 — HANDOFF WRITER, which you are not
yet. You generate. Nothing else.

For each namespace, extend the ROLE 1 inertia gap skeleton with {topic}-specific content:
> Without this signal, {topic}'s feature story would be missing: {extend the ROLE 1 skeleton
> for this namespace with content specific to {topic} — one sentence}

Write the inertia answer before the artifact body. The body must be traceable to the extended
inertia answer. A body that merely restates the ROLE 1 skeleton without topic extension, or
that could exist without the skeleton, must be revised before this role ends.

For each namespace:

  #### {Namespace} — {representative-skill-name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{representative-skill-name}
  Topic:    {topic}
  Category: {from ROLE 1 table}
  Date:     {current date}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {extend the ROLE 1 inertia gap skeleton for this namespace with {topic}-specific content;
  the ROLE 1 skeleton names the namespace's epistemic function; this sentence extends it
  with what is specifically absent for {topic} without this namespace's signal}

  {3-5 sentence artifact body — register matches Category: HIGH-STRUCTURE uses
  contract/specification language; EVIDENCE-HEAVY uses study/data language; MIXED uses
  discovery/signal language; apply MUST-use vocabulary, avoid DO NOT-use vocabulary;
  body must be grounded in the extended inertia answer above}

  [If REAL-REQUIRED = YES in ROLE 1 table:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {one sentence — prove: requires actual experiment data; listen: requires real
  user feedback; compliance namespace: requires traceable real-world sources.}

**ROLE 2 STOP — Do not activate ROLE 3 — SUMMARIZER until: (1) nine artifact sections present;
(2) each has a complete MOCK ARTIFACT header (Skill, Topic, Category, Date, Status: MOCK);
(3) each inertia answer extends the ROLE 1 skeleton with {topic}-specific content — restatement
of the skeleton alone fails this gate; (4) each body is 3-5 sentences, vocabulary-compliant,
register-matched, grounded in the extended inertia answer; (5) every REAL-REQUIRED = YES
namespace has a REAL-REQUIRED statement with rationale.**

---

### ROLE 3 — SUMMARIZER

You are the SUMMARIZER. Your sole output is the coverage summary table. Writing artifact
sections means you are ROLE 2, which is no longer active. Writing the handoff line means you
are ROLE 4, which you are not yet. You summarize. Nothing else.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
- REAL-REQUIRED: all EVIDENCE-HEAVY namespaces; all compliance-active namespaces
- TIER-2-CRITICAL: trace at tier >= 2; scout-feasibility at tier >= 2
- TIER-3-CRITICAL: listen at tier >= 2
- Multiple flags: comma-separated
- No applicable flag: —

Recommended Next Step: derive from the ROLE 2 extended inertia answer for this namespace —
not the ROLE 1 skeleton, but the topic-specific extension. Format: `/namespace:skill {topic}`.

**ROLE 3 STOP — Do not activate ROLE 4 — HANDOFF WRITER until: (1) nine rows present; (2)
each row has Category matching ROLE 1; (3) each row has all applicable Flags; (4) each
Recommended Next Step is derived from the ROLE 2 inertia answer (topic-extended, not ROLE 1
skeleton alone).**

---

### ROLE 4 — HANDOFF WRITER

You are the HANDOFF WRITER. Your sole output is the handoff section. You write the handoff.
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

## Scoring Summary

| Variation | Axis | C-22 | C-23 | Aspirational predicted | Notes |
|-----------|------|------|------|------------------------|-------|
| V-01 | Phrasing register: conditional ("In the X role") | PASS | FAIL | 14/15 | Tests whether conditional phrasing satisfies C-23; expected negative |
| V-02 | Ceiling form: "You ARE the X" + entity-departure at all 4 activations | PASS | PASS | 15/15 | R9 V-04 confirmed ceiling; v10 positive control |
| V-03 | Lifecycle: preamble-deferred positive identity; per-role entity-transition only | PASS | FAIL | 14/15 | C-23 negative control; isolates placement from mechanism |
| V-04 | Combination: block format + C-23 elements as adjacent block fields | PASS | PASS (predicted) | 15/15 | Tests whether block format can carry C-23 |
| V-05 | Regression: R9 V-02 baseline (lowercase "are", ROLE N designation) | PASS | FAIL | 14/15 | Documents exact form that misses C-23 |

**Expected ceiling:** V-02 and V-04 at 15/15. If V-04 fails C-23, finding: C-23 requires
inline prose, not block fields. If V-01 passes C-23, finding: conditional phrasing satisfies
positive affirmation — escalate C-23 criterion to require more specific form. If V-05 passes
C-23, finding: capital ARE is not load-bearing — C-23 is met by lowercase "are" + ROLE N form.
