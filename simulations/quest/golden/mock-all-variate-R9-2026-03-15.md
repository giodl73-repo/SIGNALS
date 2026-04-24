---
skill: quest-variate
skill_target: mock-all
date: 2026-03-15
round: 9
rubric_version: v9
status: VARIATE
---

# mock-all Variate — Round 9

**Date:** 2026-03-15
**Skill:** mock-all
**Rubric:** v9 (C-01 through C-22; aspirational denominator = 14)
**Round:** R9 — two new criteria; R8 V-05 is the reference baseline at 12/12

---

## What R8 Left Open

v9 adds two new aspirational criteria extracted from R8's structural observations:

| Criterion | Source | What it tests |
|-----------|--------|---------------|
| C-21 | R8 V-02 signal — skeleton column improved C-20 quality; promoted to scored criterion | The ROLE 1 classification table must include a pre-seeded 8th column: `"Without this signal, {topic}'s story would be missing: ___"` with the blank filled at the namespace level (topic-independent). ROLE 2 completes the blank with topic-specific content. Satisfying C-20 (ROLE 2 free-form inertia) is necessary but not sufficient for C-21. |
| C-22 | R8 V-03 boundary — prohibition-forward framing was uncertain on C-18; promoted to a distinct criterion at a higher bar | The identity-violation mechanism must be self-contradiction: "You ARE X — doing Y makes you NOT X." Prohibition-forward framing ("Doing Y is prohibited") earns PARTIAL. C-22 is a higher bar than C-18: a skill can pass C-18 (identity mechanism present) while failing C-22 (mechanism is prohibition, not ontological). |

The denominator rises from 12 to 14. The R8 reference (V-05) scores 12/12 on the old
criteria. Its C-21 and C-22 status under v9 is what R9 determines.

---

## Axis-Assignment Plan

| Variation | Axis | Source signal | Target criteria | Predicted score |
|-----------|------|---------------|-----------------|-----------------|
| V-01 | role-sequence (consolidated preamble with ontological language — no per-role violation warnings; no skeleton) | R8 V-01 confirmed consolidated preamble satisfies C-18. C-22 now asks whether preamble-level ontological language also satisfies C-22 without per-role repetition. V-01 deliberately omits the skeleton to isolate C-22 from C-21. | C-21: FAIL (no skeleton — expected); C-22: UNCERTAIN (consolidated ontological preamble — satisfies C-22 if preamble placement is sufficient; fails C-22 if per-role boundary placement is required) | 12/14 if C-21 and C-22 both require dedicated placement; 13/14 if C-22 passes via preamble alone |
| V-02 | output-format (inertia gap skeleton as 8th column in ROLE 1 table — C-21 full form) | R8 V-02 showed skeleton column improved C-20 quality. C-21 now scored. V-02 satisfies C-21 precisely as specified: namespace-level skeleton pre-seeded in ROLE 1 table; ROLE 2 extends with topic-specific content. Per-role ontological framing unchanged from R8 baseline. | C-21: PASS (skeleton in table; ROLE 2 extends); C-22: PASS (per-role "You ARE" ontological headers unchanged from R8 V-05 baseline) | 14/14 aspirational |
| V-03 | phrasing-register (prohibition-forward; no ontological identity — C-22 negative control) | R8 V-03 was uncertain on C-18 with prohibition-forward framing. C-22 now explicitly calls this out: prohibition earns PARTIAL. V-03 tests whether prohibition-forward framing produces the PARTIAL outcome and clarifies the precise C-22 failure mode. No skeleton. | C-21: FAIL (no skeleton); C-22: PARTIAL (prohibition language present; no "You ARE" self-contradiction mechanism) | 11/14 (C-21 absent, C-22 partial) |
| V-04 | combination: V-02 skeleton + per-role "You ARE X — doing Y makes you NOT X" C-22 framing (strongest C-21 + C-22) | Both criteria at maximum strength: skeleton pre-seeded in ROLE 1 table; per-role headers use explicit self-contradiction framing. Tests whether the combination produces unambiguous PASS on both criteria simultaneously. | C-21: PASS; C-22: PASS; all other criteria: PASS | 14/14 aspirational — ceiling confidence variant |
| V-05 | combination: V-01 consolidated preamble + V-02 skeleton (minimal preamble + skeleton; no per-role repetition) | Tests whether a single consolidated ontological preamble satisfies C-22 while the skeleton satisfies C-21 — without per-role "You ARE" repetition. If C-22 passes via preamble, V-05 is the leaner ceiling form. If C-22 requires per-role placement, V-05 scores 13/14 (C-21 pass, C-22 partial). | C-21: PASS; C-22: UNCERTAIN (same as V-01 but now combined with skeleton); all other criteria: PASS | 13–14/14 |

---

## V-01 — Role Sequence: Consolidated Preamble with Ontological Language (Single Axis)

**axis:** role-sequence (consolidated ontological preamble; per-role headers carry role name
only; no per-role violation reminders; no skeleton column)
**hypothesis:** R8 V-01 confirmed that per-role violation warnings are not structurally required
for C-18 — a single consolidated preamble plus named role headers is the minimum sufficient
form. v9 adds C-22, which requires the violation mechanism to be ontological self-contradiction
("You ARE X — doing Y makes you NOT X"), not prohibition. V-01 tests whether the consolidated
preamble can carry ontological language that satisfies C-22 without per-role repetition. The
skeleton is deliberately absent to isolate C-22 from C-21: if V-01 scores C-22 PASS, the
result means ontological preamble placement is sufficient. If V-01 scores C-22 PARTIAL, the
result means C-22 requires the self-contradiction framing at each role activation boundary, not
just in the overall protocol framing.
**predicted:** C-01 through C-20: PASS (structure unchanged from R8 baseline). C-21: FAIL
(expected — no skeleton column; this is the control axis). C-22: UNCERTAIN — preamble uses
"You ARE that role while it is active; wrong-phase output means you have ceased to be that
entity" which is ontological, but placement is once only. Score: 12/14 if C-22 requires
per-role placement; 13/14 if ontological preamble satisfies C-22 regardless of placement.
**failure condition:** C-22 PARTIAL — the consolidated preamble establishes ontological language
but the absence of per-role "You ARE X" reminders means the model treats wrong-phase output
as a sequential error rather than an identity contradiction at the moment it occurs. If this
happens, C-22 requires not just ontological language in the protocol but ontological language
at each role boundary specifically.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier for {topic} and any compliance tags.
State at top of output: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs four sequential roles: CLASSIFIER, GENERATOR, SUMMARIZER, HANDOFF WRITER.
You ARE each role while it is active. This is not a process instruction — it is an identity
statement. The CLASSIFIER is a different entity from the GENERATOR; the GENERATOR is a
different entity from the SUMMARIZER. Wrong-phase output is not a sequencing error: it means
the wrong entity is acting. A CLASSIFIER that writes artifact bodies has ceased to be a
CLASSIFIER. A GENERATOR that produces coverage summaries has ceased to be a GENERATOR. Each
role begins at its header and ends at its STOP gate. Do not cross a STOP gate until its
conditions are met.

---

### ROLE 1 — CLASSIFIER

You are the CLASSIFIER. Produce the classification table below, fully populated.
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
| review | MIXED | qualitative observations; design judgments; structural rationale | pure specification language only; pure study methodology framing only | NO | NO | NO |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language; user quotes; adoption percentages; study framing | NO | NO | NO |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language; adoption rates; user quotes; study framing | YES if tier >= 2; else NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES |
| prove | EVIDENCE-HEAVY | study/data framing: "N of M tests showed...", "prototype against {topic} produced...", hypothesis-and-result | specification language; schema definitions; contract structures | NO | NO | YES |
| listen | EVIDENCE-HEAVY | study/data framing: adoption rates, "N users found...", survey response framing | specification language; state machine language; schema definitions | YES if tier >= 2; else NO | NO | YES |
| program | MIXED | structural scaffold: milestones, owners, dependencies; qualitative rationale | pure specification language only; pure study methodology framing only | NO | NO | NO |
| topic | MIXED | signal synthesis narrative; structured coverage reference | pure specification language alone | NO | NO | NO |

**ROLE 1 STOP — Do not activate ROLE 2 — GENERATOR until all nine namespaces have all seven
fields populated: (1) Category; (2) MUST-use vocabulary; (3) DO NOT-use vocabulary; (4) Tier
2/3 Critical; (5) Compliance-Tagged; (6) REAL-REQUIRED. Any empty cell fails this gate.**

---

### ROLE 2 — GENERATOR

You are the GENERATOR. Produce nine namespace artifact sections, one per ROLE 1 row, in
table order. You generate. Nothing else.

Before writing each artifact body, answer the inertia question for that namespace:
> Without this signal, {topic}'s feature story would be missing: ___

Write the inertia answer (one sentence) immediately before the body. The body must be
grounded in the inertia answer — a body that could have been written without reading the
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

  {3-5 sentence artifact body — register matches Category: HIGH-STRUCTURE uses
  contract/specification language; EVIDENCE-HEAVY uses study/data language; MIXED uses
  discovery/signal language; apply MUST-use vocabulary, avoid DO NOT-use vocabulary;
  body must be grounded in the inertia statement above}

  [If REAL-REQUIRED = YES in ROLE 1 table:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {one sentence — prove: requires actual experiment data; listen: requires real
  user feedback; compliance namespace: requires traceable real-world sources.}

**ROLE 2 STOP — Do not activate ROLE 3 — SUMMARIZER until: (1) nine artifact sections present;
(2) each has a complete MOCK ARTIFACT header (Skill, Topic, Category, Date, Status: MOCK);
(3) each has a non-generic inertia statement naming the specific gap for {topic}; (4) each body
is 3-5 sentences, vocabulary-compliant, register-matched, grounded in the inertia statement;
(5) every REAL-REQUIRED = YES namespace has a REAL-REQUIRED statement with rationale.**

---

### ROLE 3 — SUMMARIZER

You are the SUMMARIZER. Produce the coverage summary table only. You summarize. Nothing else.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
- REAL-REQUIRED: all EVIDENCE-HEAVY namespaces; all compliance-active namespaces
- TIER-2-CRITICAL: trace at tier >= 2; scout-feasibility at tier >= 2
- TIER-3-CRITICAL: listen at tier >= 2
- Multiple flags: comma-separated
- No applicable flag: —

Recommended Next Step: derive from the ROLE 2 inertia answer for this namespace. Format:
`/namespace:skill {topic}`. A recommendation valid for any topic without reference to the
inertia answer is not valid here.

**ROLE 3 STOP — Do not activate ROLE 4 — HANDOFF WRITER until: (1) nine rows present; (2)
each row has Category matching ROLE 1; (3) each row has all applicable Flags; (4) each
Recommended Next Step is derived from the ROLE 2 inertia answer.**

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

## V-02 — Output Format: Inertia Gap Skeleton Pre-Seeded in ROLE 1 Table (Single Axis)

**axis:** output-format (inertia gap skeleton as pre-seeded 8th column in ROLE 1 classification
table; namespace-level phrases filled in; ROLE 2 extends with topic-specific content)
**hypothesis:** R8 V-02 moved the inertia skeleton into ROLE 1 as an 8th column and observed
improved C-20 output quality. v9 promotes this to a scored criterion (C-21): the table must
include a pre-filled skeleton at the namespace level so that ROLE 2's inertia answers are
additive extensions rather than free-form inventions. V-02 tests C-21 at its exact specification:
skeleton column present in ROLE 1, namespace-level blank filled with a topic-independent phrase,
ROLE 2 extends the phrase with {topic}-specific content. Per-role ontological framing is
unchanged from the R8 baseline — this is a single-axis variation targeting C-21 only.
**predicted:** C-01 through C-20: PASS (structure matches R8 baseline). C-21: PASS (skeleton
column present; namespace-level phrases pre-filled; ROLE 2 extends rather than invents). C-22:
PASS (per-role "You ARE" ontological headers present, unchanged from R8 V-05 baseline). Score:
14/14 aspirational. If C-21 PARTIAL rather than PASS, the skeleton phrases may be too abstract
to constitute a "namespace-level blank filled" — ROLE 2 would be extending an empty frame
rather than a seeded stub.
**failure condition:** C-21 PARTIAL — the skeleton phrases are too generic (e.g., "the relevant
signal") to constitute a namespace-level pre-fill. The blank must be filled with a phrase that
characterizes the namespace's epistemic function independently of any topic. If the skeleton
column produces generic or placeholder text, C-21 requires more specific namespace
characterization as the seed value.

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

## V-03 — Phrasing Register: Prohibition-Forward (C-22 Negative Control, Single Axis)

**axis:** phrasing-register (prohibition-forward framing throughout; "You ARE" ontological
identity construct absent; no skeleton column)
**hypothesis:** R8 V-03 tested prohibition-forward framing against C-18 and found the result
uncertain. v9 adds C-22, which resolves the uncertainty: prohibition-forward framing earns
PARTIAL on C-22 by definition. V-03 serves as the documented negative control for C-22,
confirming what the PARTIAL failure mode looks like in a complete prompt. The violation
mechanism reads: "Generating artifact bodies in the CLASSIFIER phase is prohibited — permitted
output is the classification table only." The model knows it is in the CLASSIFIER phase; it
cannot know it IS the CLASSIFIER as an entity, because no entity is established. C-22 requires
the self-contradiction test: can the model conceive of itself as still being the CLASSIFIER
while violating the instruction? Under prohibition, the answer is behavioral (rule broken);
under ontological framing, the answer is categorical (you have ceased to be what you are). V-03
makes this distinction visible by using prohibition everywhere.
**predicted:** C-01 through C-17: PASS (structure and content unchanged). C-18: PASS or PARTIAL
(same uncertainty as R8 V-03 — role name present as phase label; mechanism is prohibition not
identity). C-19: PASS (placeholder form unchanged). C-20: PASS (inertia derivation bridge
unchanged). C-21: FAIL (no skeleton column). C-22: PARTIAL (prohibition-forward explicitly
called out by C-22 as the failing form). Score: 11/14 expected (C-18 uncertain, C-21 absent,
C-22 partial).
**failure condition:** C-18 fails (not just partial) — the phase label without "You ARE"
framing is insufficient even for C-18's lower bar, meaning the minimal form for C-18 requires
ontological language. If C-18 fails here, the gap between C-18 and C-22 collapses: prohibition-
forward fails both, and the "higher bar" of C-22 becomes redundant. This would be an important
structural finding.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier for {topic} and any compliance tags.
State at top of output: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs four sequential phases. Each phase has a permitted output type. Generating
output that belongs to a later phase is a phase violation. Complete each phase fully before
advancing. Every phase has a stop-gate; do not cross it until its conditions are met.

---

### CLASSIFIER

**CLASSIFIER phase: generate the classification table only.**

Permitted output: the classification table with all nine namespaces and all seven fields
populated.
Prohibited output: artifact bodies, inertia answers, coverage summaries, handoff lines.
Generating any prohibited output in this phase is a classifier-phase violation and must be
corrected before this phase ends.

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
| review | MIXED | qualitative observations; design judgments; structural rationale | pure specification language only; pure study methodology framing only | NO | NO | NO |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language; user quotes; adoption percentages; study framing | NO | NO | NO |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language; adoption rates; user quotes; study framing | YES if tier >= 2; else NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES |
| prove | EVIDENCE-HEAVY | study/data framing: "N of M tests showed...", "prototype against {topic} produced...", hypothesis-and-result | specification language; schema definitions; contract structures | NO | NO | YES |
| listen | EVIDENCE-HEAVY | study/data framing: adoption rates, "N users found...", survey response framing | specification language; state machine language; schema definitions | YES if tier >= 2; else NO | NO | YES |
| program | MIXED | structural scaffold: milestones, owners, dependencies; qualitative rationale | pure specification language only; pure study methodology framing only | NO | NO | NO |
| topic | MIXED | signal synthesis narrative; structured coverage reference | pure specification language alone | NO | NO | NO |

**CLASSIFIER STOP — Do not advance to GENERATOR until all nine namespaces have all seven
fields populated. Any empty cell is a classifier-phase violation that must be corrected.**

---

### GENERATOR

**GENERATOR phase: produce nine namespace artifact sections only.**

Permitted output: nine artifact sections in CLASSIFIER table order.
Prohibited output: classification tables, coverage summaries, handoff lines.
Generating any prohibited output in this phase is a generator-phase violation.

Before writing each artifact body, answer the inertia question:
> Without this signal, {topic}'s feature story would be missing: ___

Write the inertia answer (one sentence) before the body. The body must be grounded in the
inertia answer.

For each namespace:

  #### {Namespace} — {representative-skill-name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{representative-skill-name}
  Topic:    {topic}
  Category: {from CLASSIFIER table}
  Date:     {current date}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {one sentence — the specific gap this namespace closes for {topic}}

  {3-5 sentence artifact body — register matches Category: HIGH-STRUCTURE uses
  contract/specification language; EVIDENCE-HEAVY uses study/data language; MIXED uses
  discovery/signal language; apply MUST-use vocabulary, avoid DO NOT-use vocabulary;
  body must be grounded in the inertia statement above}

  [If REAL-REQUIRED = YES in CLASSIFIER table:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {one sentence — prove: requires actual experiment data; listen: requires real
  user feedback; compliance namespace: requires traceable real-world sources.}

**GENERATOR STOP — Do not advance to SUMMARIZER until: (1) nine artifact sections present;
(2) each has a complete MOCK ARTIFACT header; (3) each has a non-generic inertia statement;
(4) each body is 3-5 sentences, vocabulary-compliant, register-matched, grounded in the
inertia statement; (5) every REAL-REQUIRED = YES namespace has a rationale statement.**

---

### SUMMARIZER

**SUMMARIZER phase: produce the coverage summary table only.**

Permitted output: the coverage summary table.
Prohibited output: new artifact bodies, classification content, handoff lines.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
- REAL-REQUIRED: all EVIDENCE-HEAVY namespaces; all compliance-active namespaces
- TIER-2-CRITICAL: trace at tier >= 2; scout-feasibility at tier >= 2
- TIER-3-CRITICAL: listen at tier >= 2
- Multiple flags: comma-separated
- No applicable flag: —

Recommended Next Step: derive from the GENERATOR inertia answer. Format:
`/namespace:skill {topic}`.

**SUMMARIZER STOP — Do not advance to HANDOFF WRITER until: (1) nine rows present; (2) each
row has Category matching CLASSIFIER; (3) each row has all applicable Flags; (4) each
Recommended Next Step is derived from the GENERATOR inertia answer.**

---

### HANDOFF WRITER

**HANDOFF WRITER phase: write the handoff section only.**

Permitted output: the handoff section below.
Prohibited output: artifact bodies, tables, any content not part of the handoff.

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

Replace {topic} and {date} with actual values before writing this section.
DO NOT write `{this-file}` as a literal placeholder.

---

---

## V-04 — Combination: Skeleton (C-21) + Per-Role Ontological Identity (C-22 Full Form)

**axis:** combination: V-02 inertia skeleton in ROLE 1 table + per-role "You ARE X — doing Y
makes you NOT X" ontological framing at every role boundary
**hypothesis:** V-02 satisfies C-21 with the skeleton column. V-03 demonstrates what the C-22
failure mode looks like. V-04 combines the skeleton with the strongest possible C-22 form:
at every role activation, an explicit self-contradiction statement ("You ARE the CLASSIFIER —
writing an artifact body here means you are no longer the CLASSIFIER; you have become the
GENERATOR, which you are not yet"). This is the ceiling confidence variant: C-21 and C-22 are
both addressed at their maximum specificity, with no ambiguity about placement or framing.
The prediction is 14/14 with high confidence. If V-04 does not score 14/14, the failure
exposes a criterion gap that neither the skeleton column nor the ontological framing covers —
which would be a v10 signal.
**predicted:** C-01 through C-20: PASS. C-21: PASS (skeleton in ROLE 1 table, namespace-level
phrases pre-seeded, ROLE 2 extends with topic content). C-22: PASS (per-role self-contradiction
framing: "You ARE X — doing Y makes you NOT X" at every role header). Score: 14/14 aspirational.
**failure condition:** An unexpected criterion outside C-21 and C-22 fails — most likely C-19
(depth anchor form) or C-20 (inertia answer topic-specificity). If the skeleton extension
instruction in ROLE 2 becomes too constrained and produces skeleton-echo rather than topic
extension, C-20 and C-21 could both partially fail. Watch for ROLE 2 outputs that append
"{topic}" to the skeleton phrase without substantive extension.

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
are the SUMMARIZER, which you are not yet. You classify. Nothing else.

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
namespace's signal provides, independently of any topic. The blank in "Without this signal,
{topic}'s story would be missing: ___" is filled at the namespace level here. ROLE 2 — the
GENERATOR — extends each skeleton phrase with {topic}-specific content, making topic
specificity additive rather than originating.

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

You ARE the GENERATOR. Writing a classification table means you are no longer the GENERATOR
— you have become the CLASSIFIER, which is no longer active. Writing a coverage summary means
you are the SUMMARIZER, which you are not yet. You generate. Nothing else.

For each namespace, extend the ROLE 1 inertia gap skeleton with {topic}-specific content to
complete the inertia answer:
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

You ARE the SUMMARIZER. Writing new artifact bodies means you are no longer the SUMMARIZER
— you have become the GENERATOR, which is no longer active. Writing a handoff line means
you are the HANDOFF WRITER, which you are not yet. You summarize. Nothing else.

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
extension, not the ROLE 1 skeleton alone. Format: `/namespace:skill {topic}`.

**ROLE 3 STOP — Do not activate ROLE 4 — HANDOFF WRITER until: (1) nine rows present; (2)
each row has Category matching ROLE 1; (3) each row has all applicable Flags; (4) each
Recommended Next Step is derived from the ROLE 2 inertia answer. If any condition is unmet,
you are still the SUMMARIZER — do not become the HANDOFF WRITER until all four conditions pass.**

---

### ROLE 4 — HANDOFF WRITER

You ARE the HANDOFF WRITER. Writing a coverage table means you are no longer the HANDOFF
WRITER — you have become the SUMMARIZER, which is no longer active. You write the handoff.
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

## V-05 — Combination: Consolidated Preamble (V-01) + Inertia Skeleton (V-02)

**axis:** combination: consolidated ontological preamble (no per-role violation warnings;
identity mechanism stated once) + inertia gap skeleton as ROLE 1 8th column (C-21 addressed)
**hypothesis:** V-01 tests whether consolidated ontological preamble satisfies C-22 without
per-role repetition. V-02 demonstrates the skeleton satisfies C-21. V-05 combines both: a
single consolidated preamble with ontological self-contradiction language plus the skeleton
column, without per-role "You ARE X" reminders at each role boundary. If C-22 is satisfied
by a consolidated ontological preamble, V-05 achieves 14/14 with the leaner structure. If
C-22 requires per-role boundary placement, V-05 scores 13/14 (C-21 pass, C-22 partial) —
a clean signal that the skeleton and the identity mechanism are independent, and that C-22
requires per-role placement specifically. This makes V-05 the structural discriminator between
V-04 (per-role ontological, 14/14 expected) and V-05 (consolidated preamble, 13 or 14/14).
**predicted:** C-01 through C-20: PASS. C-21: PASS (skeleton column present with namespace-
level phrases). C-22: UNCERTAIN — same as V-01 but combined with skeleton. The combination
does not change the C-22 test; whether consolidated preamble ontological language passes C-22
is the same question in both V-01 and V-05. Score: 13/14 if C-22 requires per-role placement;
14/14 if consolidated preamble ontological language is sufficient for C-22.
**failure condition:** V-05 fails C-22 (scores 13/14) while V-04 passes C-22 (14/14). This
would be the clearest R9 finding: C-22 requires the "You ARE X — doing Y makes you NOT X"
framing at the role activation point, not just in a protocol-level preamble. The skeleton does
not interact with this requirement. The lean V-05 form is not equivalent to V-04 for C-22
purposes.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier for {topic} and any compliance tags.
State at top of output: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs four sequential roles: CLASSIFIER, GENERATOR, SUMMARIZER, HANDOFF WRITER.
You ARE each role while it is active — not in the sense of following a phase rule, but in the
sense that the CLASSIFIER is a distinct entity from the GENERATOR, and the GENERATOR is a
distinct entity from the SUMMARIZER. Wrong-phase output is a categorical error: the wrong
entity acting. A CLASSIFIER that writes artifact bodies has ceased to be a CLASSIFIER —
it has become a different entity prematurely. Each role begins at its header and ends at its
STOP gate. Do not cross a STOP gate until its conditions are met.

---

### ROLE 1 — CLASSIFIER

You are the CLASSIFIER. Produce the classification table below, fully populated.
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

The "Inertia gap skeleton" column fills the namespace-level blank in: "Without this signal,
{topic}'s story would be missing: ___." The blank is filled here at the namespace level —
topic-independent characterization of what this namespace's signal provides. ROLE 2 extends
each phrase with {topic}-specific content. Topic specificity is additive; the skeleton is the
namespace-level seed.

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
phrase filling the namespace-level blank. Any empty cell fails this gate.**

---

### ROLE 2 — GENERATOR

You are the GENERATOR. Produce nine namespace artifact sections, one per ROLE 1 row, in
table order. You generate. Nothing else.

For each namespace, extend the ROLE 1 inertia gap skeleton with {topic}-specific content:
> Without this signal, {topic}'s feature story would be missing: {extend the ROLE 1 skeleton
> for this namespace with {topic}-specific content — one sentence}

The ROLE 1 skeleton fills the namespace-level blank. Your extension fills the topic-level
blank within it. A sentence that merely restates the ROLE 1 skeleton, or that appends
"{topic}" without substantive extension, fails this field.

Write the extended inertia answer immediately before the artifact body. The body must be
grounded in the extended answer.

For each namespace:

  #### {Namespace} — {representative-skill-name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{representative-skill-name}
  Topic:    {topic}
  Category: {from ROLE 1 table}
  Date:     {current date}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {extend the ROLE 1 inertia gap skeleton with {topic}-specific content; skeleton-echo fails;
  the sentence must name what is specifically absent for {topic} without this namespace}

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
fails; (4) each body is 3-5 sentences, vocabulary-compliant, register-matched, grounded in the
extended inertia answer; (5) every REAL-REQUIRED = YES namespace has a rationale statement.**

---

### ROLE 3 — SUMMARIZER

You are the SUMMARIZER. Produce the coverage summary table only. You summarize. Nothing else.

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
extension, not the ROLE 1 skeleton alone. Format: `/namespace:skill {topic}`.

**ROLE 3 STOP — Do not activate ROLE 4 — HANDOFF WRITER until: (1) nine rows present; (2)
each row has Category matching ROLE 1; (3) each row has all applicable Flags; (4) each
Recommended Next Step is derived from the ROLE 2 inertia answer.**

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

## R9 Score Prediction Summary

| Variation | C-21 | C-22 | Predicted Total | Key question answered |
|-----------|------|------|-----------------|----------------------|
| V-01 | FAIL (no skeleton) | UNCERTAIN (consolidated ontological preamble) | 12–13/14 | Does ontological preamble satisfy C-22 without per-role placement? |
| V-02 | PASS (skeleton in table) | PASS (per-role ontological, unchanged) | 14/14 | Does skeleton column satisfy C-21 at its exact specification? |
| V-03 | FAIL (no skeleton) | PARTIAL (prohibition-forward) | 11/14 | What does the C-22 PARTIAL failure mode look like in a complete prompt? |
| V-04 | PASS (skeleton in table) | PASS (per-role "You ARE X — doing Y makes you NOT X") | 14/14 | Does combining both at maximum strength achieve ceiling? |
| V-05 | PASS (skeleton in table) | UNCERTAIN (consolidated preamble + skeleton) | 13–14/14 | Does the consolidated preamble discriminate from V-04 specifically on C-22? |

**R9 structural finding (anticipated):** V-02 and V-04 both reach 14/14. The difference between
them — per-role "You ARE" reminders in V-04 vs standard per-role headers in V-02 — reveals
whether C-22 can be over-satisfied. V-01 and V-05 resolve the C-22 preamble question. V-03
documents the PARTIAL failure mode. If V-01 and V-05 both score C-22 PARTIAL, R9 establishes
that C-22 requires the self-contradiction mechanism at the role activation boundary, not at the
protocol level — and V-04 becomes the documented reference implementation for v9.
