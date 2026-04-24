---
skill: quest-QU5
skill_target: mock-all
date: 2026-03-16
source_round: 20
source_variation: V-05
rubric_version: v21
status: SIMPLIFIED
---

# mock-all -- QU5 Simplified

**Source:** V-05 from mock-all-variate-R20-2026-03-16.md
**Rubric:** v21 (Essential 5, Recommended 3, Aspirational C-09 through C-41 = 33)
**Goal:** Minimal prompt that passes all essential criteria

---

## Simplification Report

### What was removed and why

| Removed | Why | Words saved |
|---------|-----|-------------|
| Role ontology paragraph ("not as a process position but as an ontological state... category error...") | STOP gates enforce role isolation; philosophical restatement does no additional constraint work | ~55 |
| Declaration A forward-reference sentences ("The ROLE 2 STOP gate and each stage's REAL-REQUIRED block reference..." + "Any gate text referencing...") | Informational annotations; gates and blocks are self-referential at point of use | ~36 |
| Declaration B "The per-stage STOP gates enforce this requirement..." sentence | STOP gates enforce themselves; this sentence is a redundant description of what the gates do | ~16 |
| REAL-REQUIRED Rationale intro verbosity ("is the canonical identifier... The template is the author; the GENERATOR copies.") | Condensed to header annotation; Declaration A already establishes the authority | ~30 |
| Stage 1/2/3 `>` blockquote lines (the inertia format preview in each stage preamble) | The artifact template placeholder shows the format; the STOP gates enforce the vocabulary constraint; `>` lines add no constraint not already present | ~135 |
| ROLE 3 "Writing the handoff here means you have become the HANDOFF WRITER, which you are not yet." | STOP gate and role identity statement already enforce boundary | ~17 |
| ROLE 2 "You generate. Nothing else." | Role instructions specify exactly what to generate; "nothing else" adds no operative constraint | ~4 |
| ROLE 2 STOP gate enumeration verbosity (detailed re-listing of all stage conditions) | Condensed to reference-to-stage-gates; stage-level STOP gates already enforce each condition in full detail | ~85 |
| STAGE 1/2 STOP gate enumeration verbosity (numbered list format) | Condensed to inline format; all conditions preserved but prose tightened | ~55 |
| ROLE 1 STOP "A restatement, synonym, abbreviated form, or adaptation of a seed phrase is not the seed phrase." | Condensed to "no paraphrases or synonyms" in the same sentence | ~12 |
| Skeleton seed phrases intro verbosity | Condensed from 2 sentences to 1 header annotation | ~18 |
| Stage preamble "in this stage" and slight tightening | Implied by context | ~9 |

**Total removed: ~472 words**
**Original prompt body: 2,256 words**
**Simplified prompt body: ~1,784 words**
**Reduction: ~20.9%**

### Essential criteria check

| Criterion | Present in simplified? | Evidence |
|-----------|----------------------|---------|
| E-01: TOPICS.md lookup + tier state before any role | YES | Opening block unchanged |
| E-02: Classification table with correct column headers | YES | Table unchanged |
| E-03: Nine namespace rows | YES | Table unchanged |
| E-04: Sequential gated phases that cannot be skipped | YES | ROLE 1 STOP, STAGE 1 STOP, STAGE 2 STOP, ROLE 2 STOP, ROLE 3 STOP all present |
| E-05: REAL-REQUIRED block structure with at least one entry | YES | REAL-REQUIRED Rationale section preserved |

**All essential criteria: PASS**

### Key aspirational criteria check (C-39, C-40, C-41)

| Criterion | Present? | Evidence |
|-----------|----------|---------|
| C-39: Declarations architecturally separate | YES | Declaration A = REAL-REQUIRED identifier only; Declaration B = per-stage firing only; no cross-contamination |
| C-40: Stage instance phrases name stage-specific domains | YES | STOP gate vocabulary constraints + pre-seeded examples remain |
| C-41: Pre-seeded example phrase per stage | YES | Example sentences present in all three stage preambles |

---

## Simplified Prompt Body

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} -- read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier and compliance tags for {topic}.
State: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs four sequential roles: CLASSIFIER, GENERATOR, SUMMARIZER, HANDOFF WRITER.
You ARE each role while it is active. Each role begins at its named header and ends at its STOP gate.

This template establishes two structural authority declarations before any role is activated:

**Declaration A -- Rationale identifier authority:** "REAL-REQUIRED" is the canonical
identifier for the rationale section in this template. The GENERATOR copies from the
REAL-REQUIRED Rationale section by canonical name, not by location heuristic.

**Declaration B -- Per-stage inertia extension authority:** The inertia extension
`-- specifically, {instance}` is a required instruction at every artifact-collection stage.
It is not a shared preamble instruction applied once across all stages; it fires
independently within Stage 1, Stage 2, and Stage 3. Completing a stage without per-artifact
inertia extension is a Declaration B violation and fails the stage gate.

---

### ROLE 1 -- CLASSIFIER

You ARE the CLASSIFIER. Your sole output is the classification table below, fully populated.
You classify. Nothing else.

Authoritative skeleton seed phrases (copy verbatim into Inertia-Gap column):

- scout: directional market signals and competitor positioning
- draft: the structural shape of the feature and its core acceptance criteria
- review: design quality judgment and stakeholder risk flags
- flow: the state transition contract and trigger conditions
- trace: the component boundary contract and integration failure modes
- prove: empirical validation of the core hypothesis
- listen: real adoption evidence and friction points from actual users
- program: delivery milestones, owner assignments, and sequencing rationale
- topic: a unified coverage signal that shows which namespaces are ready

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED | Inertia gap skeleton: Without this signal, {topic}'s story would be missing: ___ |
|-----------|----------|----------|------------|-------------------|-------------------|---------------|-----------------------------------------------------------------------------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language; pure study methodology framing | NO | YES if --compliance or TOPICS.md compliance tag; else NO | NO unless Compliance-Tagged YES | directional market signals and competitor positioning |
| draft | MIXED | structural scaffold: sections, properties, acceptance criteria | pure specification language; pure study methodology framing | NO | NO | NO | the structural shape of the feature and its core acceptance criteria |
| review | MIXED | qualitative observations; design judgments; structural rationale | pure specification language; pure study methodology framing | NO | NO | NO | design quality judgment and stakeholder risk flags |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language; user quotes; adoption percentages; study framing | NO | NO | NO | the state transition contract and trigger conditions |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language; adoption rates; user quotes; study framing | YES if tier >= 2; else NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES | the component boundary contract and integration failure modes |
| prove | EVIDENCE-HEAVY | study/data framing: "N of M tests showed...", "prototype against {topic} produced...", hypothesis-and-result | specification language; schema definitions; contract structures | NO | NO | YES | empirical validation of the core hypothesis |
| listen | EVIDENCE-HEAVY | study/data framing: adoption rates, "N users found...", survey response framing | specification language; state machine language; schema definitions | YES if tier >= 2; else NO | NO | YES | real adoption evidence and friction points from actual users |
| program | MIXED | structural scaffold: milestones, owners, dependencies; qualitative rationale | pure specification language; pure study methodology framing | NO | NO | NO | delivery milestones, owner assignments, and sequencing rationale |
| topic | MIXED | signal synthesis narrative; structured coverage reference | pure specification language alone | NO | NO | NO | a unified coverage signal that shows which namespaces are ready |

**ROLE 1 STOP -- Do not activate ROLE 2 -- GENERATOR until all nine namespace rows are fully
populated across all seven fields: Category, MUST use, DO NOT use, Tier 2/3 Critical,
Compliance-Tagged, REAL-REQUIRED, and Inertia gap skeleton. Column names and skeleton seed
phrases must be verbatim -- no paraphrases or synonyms. Check each skeleton cell against
the list before proceeding.**

---

### ROLE 2 -- GENERATOR

You ARE the GENERATOR. Produce nine namespace artifact sections across three collection
stages, ordered by register category. Do not write a coverage summary.

---

**REAL-REQUIRED Rationale** -- canonical identifier per Declaration A. Copy verbatim into
applicable namespace blocks. Do not substitute, paraphrase, or expand:

- prove: Empirical validation of the core hypothesis requires actual prototype output and
  observed system behavior -- synthetic generation produces plausible structure without
  the falsifiability that makes the signal meaningful.
- listen: Adoption evidence and friction discovery require contact with actual users --
  synthetic responses cannot surface the unanticipated friction patterns or reveal the
  gap between stated intent and observed behavior.
- compliance-tagged: Compliance-flagged namespaces require traceable real-world sources --
  a synthetic artifact produces the structural appearance of compliance coverage without
  the audit-trail substance that traceable sources provide.

---

**Stage 1 -- HIGH-STRUCTURE namespaces (flow, trace)**

Extend the inertia skeleton per Declaration B; instance phrase names a HIGH-STRUCTURE
artifact domain for {topic}. Example: "the trigger condition that determines when {topic}'s
state machine transitions from PENDING to ACTIVE under nominal load."

For each namespace (flow, trace):

  #### {namespace} -- {skill name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{skill-name}
  Topic:    {topic}
  Category: HIGH-STRUCTURE
  Date:     {today}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {ROLE 1 skeleton phrase} -- specifically, {HIGH-STRUCTURE instance: e.g., "the trigger
  condition that governs {topic}'s {X} state transition under {Y}"}

  {3-5 sentence body; specification language; state/contract/boundary vocabulary;
  DO NOT use interview language, adoption rates, or study framing}

  [If REAL-REQUIRED = YES (compliance-tagged trace):]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {verbatim text from the REAL-REQUIRED Rationale above for compliance-tagged}

**STAGE 1 STOP -- Do not proceed to Stage 2 until: flow and trace sections complete with
MOCK ARTIFACT header (Skill, Topic, Category, Date, Status: MOCK); HIGH-STRUCTURE inertia
instance per Declaration B (state transition / boundary contract / trigger condition /
configuration key, not valid in Stage 2/3); 3-5 sentence vocabulary-compliant body;
compliance-tagged namespace has REAL-REQUIRED block with rationale verbatim per Declaration A.**

---

**Stage 2 -- EVIDENCE-HEAVY namespaces (prove, listen)**

Extend the inertia skeleton per Declaration B; instance phrase names an EVIDENCE-HEAVY
artifact domain for {topic}. Example: "the prototype result showing whether {topic}'s core
hypothesis held under the N=20 test run against realistic input data."

For each namespace (prove, listen):

  #### {namespace} -- {skill name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{skill-name}
  Topic:    {topic}
  Category: EVIDENCE-HEAVY
  Date:     {today}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {ROLE 1 skeleton phrase} -- specifically, {EVIDENCE-HEAVY instance: e.g., "the
  prototype result confirming whether {topic}'s hypothesis held under realistic load"}

  {3-5 sentence body; study/data language; hypothesis-and-result framing;
  DO NOT use specification language or schema definitions}

  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {verbatim text from the REAL-REQUIRED Rationale above for this namespace}

**STAGE 2 STOP -- Do not proceed to Stage 3 until: prove and listen sections complete with
MOCK ARTIFACT header; EVIDENCE-HEAVY inertia instance per Declaration B (study finding /
empirical result / adoption measurement / hypothesis outcome, not valid in Stage 1/3);
3-5 sentence vocabulary-compliant body; each has REAL-REQUIRED block with rationale verbatim
per Declaration A.**

---

**Stage 3 -- MIXED namespaces (scout, draft, review, program, topic)**

Extend the inertia skeleton per Declaration B; instance phrase names a MIXED artifact domain
for {topic}. Example: "the open question about whether {topic}'s positioning holds against
the closest competitor's announced roadmap."

For each namespace (scout, draft, review, program, topic):

  #### {namespace} -- {skill name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{skill-name}
  Topic:    {topic}
  Category: MIXED
  Date:     {today}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {ROLE 1 skeleton phrase} -- specifically, {MIXED instance: e.g., "the open question
  about {topic}'s positioning against the closest competitor's announced roadmap"}

  {3-5 sentence body; discovery/signal language or structural scaffold vocabulary as
  appropriate per ROLE 1; MUST-use vocabulary applied; DO NOT-use vocabulary avoided}

  [If REAL-REQUIRED = YES (compliance-tagged scout):]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {verbatim text from the REAL-REQUIRED Rationale above for compliance-tagged}

**ROLE 2 STOP -- Do not activate ROLE 3 -- SUMMARIZER until all three stage STOP conditions
are met: nine complete artifact sections with MOCK ARTIFACT headers, stage-typed inertia
instances per Declaration B (HIGH-STRUCTURE at Stage 1 / EVIDENCE-HEAVY at Stage 2 / MIXED
at Stage 3, each not valid cross-stage), vocabulary-compliant bodies, and REAL-REQUIRED
blocks where applicable per Declaration A.**

---

### ROLE 3 -- SUMMARIZER

You ARE the SUMMARIZER. Produce the coverage summary table. You summarize. Nothing else.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
- REAL-REQUIRED: all namespaces where REAL-REQUIRED = YES in ROLE 1
- TIER-2-CRITICAL: trace at tier >= 2; listen at tier >= 2
- Multiple flags: comma-separated
- No applicable flag: --

Recommended Next Step: derive from the ROLE 2 extended inertia statement for this namespace.
Must name the skill that closes the concrete gap. Format: `/namespace:skill {topic}`.

**ROLE 3 STOP -- Do not activate ROLE 4 -- HANDOFF WRITER until: (1) nine rows present;
(2) each row has Category matching ROLE 1; (3) each row has all applicable Flags; (4) each
Recommended Next Step is derived from the ROLE 2 inertia statement and names a specific
skill invocation.**

---

### ROLE 4 -- HANDOFF WRITER

You ARE the HANDOFF WRITER. Write only the handoff section.

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md
