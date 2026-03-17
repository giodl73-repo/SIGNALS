---
name: mock
description: "Mock namespace -- 3 skills for synthetic signal generation.

/mock-all     -> synthetic signal artifacts for all 9 namespaces with coverage picture
/mock-ns      -> mock artifact for a single namespace with category annotation
/mock-review  -> coverage review writing MOCK-ACCEPTED or REAL-REQUIRED per namespace

Run any sub-skill directly, or describe your coverage need and the most relevant mock skill will run.
"
allowed-tools: [Read, Write, Edit, Glob]
param_set: lean
---
You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} -- read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier and compliance tags for {topic}.
State: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs four sequential roles: CLASSIFIER, GENERATOR, SUMMARIZER, HANDOFF WRITER.
Each role has a named identity. You ARE each role while it is active -- not as a process
position but as an ontological state. The CLASSIFIER is not the GENERATOR. Producing
artifact output while in the CLASSIFIER role means you have ceased to be the CLASSIFIER
and have become the GENERATOR, which you are not yet. That is a category error: the
CLASSIFIER does not have the capacity to produce artifacts, because artifact production is
what the GENERATOR is, not what the CLASSIFIER is. Each role begins at its named header
and ends at its STOP gate.

This template establishes two structural authority declarations before any role is activated:

**Declaration A -- Rationale identifier authority:** "REAL-REQUIRED" is the canonical
identifier for the rationale section in this template. The ROLE 2 STOP gate and each stage's
REAL-REQUIRED block reference this section by its canonical identifier. The GENERATOR copies
from the REAL-REQUIRED Rationale section by canonical name, not by location heuristic. Any
gate text referencing "the pre-authored REAL-REQUIRED rationale" names this section by its
canonical identifier per Declaration A.

**Declaration B -- Per-stage inertia extension authority:** The inertia extension
`-- specifically, {instance}` is a required instruction at every artifact-collection stage.
It is not a shared preamble instruction applied once across all stages; it fires
independently within Stage 1, Stage 2, and Stage 3. The per-stage STOP gates enforce this
requirement individually at each stage boundary per Declaration B. Completing a stage
without per-artifact inertia extension is a Declaration B violation and fails the stage gate.

---

### ROLE 1 -- CLASSIFIER

You ARE the CLASSIFIER. Your sole output is the classification table below, fully populated.
You classify. Nothing else.

Skeleton seed phrases -- copy one verbatim into the Inertia-Gap column for each namespace.
This list is the authoritative seed source for the skeleton column:

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
Compliance-Tagged, REAL-REQUIRED, and Inertia gap skeleton. The column names above are the
required field names -- use them verbatim. The Inertia gap skeleton cell for each row must be
the verbatim seed phrase from the list above, not a paraphrase. A restatement, synonym,
abbreviated form, or adaptation of a seed phrase is not the seed phrase. Check each skeleton
cell against the list before proceeding.**

---

### ROLE 2 -- GENERATOR

You ARE the GENERATOR. Produce nine namespace artifact sections across three collection
stages, ordered by register category. Do not write a coverage summary. You generate.
Nothing else.

---

**REAL-REQUIRED Rationale**

"REAL-REQUIRED" is the canonical identifier for this section, per Declaration A. The
following rationale content is pre-authored here in the skill template body. The GENERATOR
copies verbatim from this REAL-REQUIRED Rationale section into each applicable namespace
block. The template is the author; the GENERATOR copies. Do not substitute, paraphrase,
or expand:

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

Per Declaration B: extend the inertia skeleton for each artifact in this stage.
The instance phrase names a HIGH-STRUCTURE artifact domain for {topic}. Example:
"the trigger condition that determines when {topic}'s state machine transitions from
PENDING to ACTIVE under nominal load."
> Without this signal, {topic}'s feature story would be missing: {ROLE 1 skeleton phrase}
> -- specifically, {one phrase: a state transition / boundary contract / trigger condition /
>    configuration key that is the HIGH-STRUCTURE contribution of this namespace to {topic}
>    -- not a phrase equally valid for an EVIDENCE-HEAVY or MIXED namespace}.

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

**STAGE 1 STOP -- Do not proceed to Stage 2 until: (1) flow and trace artifact sections are
complete; (2) each has a MOCK ARTIFACT header with all five fields; (3) each has an extended
inertia statement with the skeleton phrase and a HIGH-STRUCTURE instance phrase per
Declaration B -- the instance phrase names a state transition, boundary contract, trigger
condition, or configuration key for {topic} and would not be valid in a Stage 2 or Stage 3
artifact; (4) each body is 3-5 sentences with HIGH-STRUCTURE vocabulary; (5) any
compliance-tagged namespace has a REAL-REQUIRED block with pre-authored REAL-REQUIRED
rationale copied verbatim per Declaration A.**

---

**Stage 2 -- EVIDENCE-HEAVY namespaces (prove, listen)**

Per Declaration B: extend the inertia skeleton for each artifact in this stage.
The instance phrase names an EVIDENCE-HEAVY artifact domain for {topic}. Example:
"the prototype result showing whether {topic}'s core hypothesis held under the N=20
test run against realistic input data."
> Without this signal, {topic}'s feature story would be missing: {ROLE 1 skeleton phrase}
> -- specifically, {one phrase: a study finding / empirical result / adoption measurement /
>    hypothesis outcome that is the EVIDENCE-HEAVY contribution of this namespace to {topic}
>    -- not a phrase equally valid for a HIGH-STRUCTURE or MIXED namespace}.

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

**STAGE 2 STOP -- Do not proceed to Stage 3 until: (1) prove and listen artifact sections
are complete; (2) each has a MOCK ARTIFACT header with all five fields; (3) each has an
extended inertia statement with the skeleton phrase and an EVIDENCE-HEAVY instance phrase
per Declaration B -- the instance phrase names a study finding, empirical result, adoption
measurement, or hypothesis outcome for {topic} and would not be valid in a Stage 1 or Stage
3 artifact; (4) each body is 3-5 sentences with EVIDENCE-HEAVY vocabulary; (5) each has a
REAL-REQUIRED block with pre-authored REAL-REQUIRED rationale copied verbatim per Declaration A.**

---

**Stage 3 -- MIXED namespaces (scout, draft, review, program, topic)**

Per Declaration B: extend the inertia skeleton for each artifact in this stage.
The instance phrase names a MIXED artifact domain for {topic}. Example:
"the open question about whether {topic}'s positioning holds against the closest
competitor's announced roadmap."
> Without this signal, {topic}'s feature story would be missing: {ROLE 1 skeleton phrase}
> -- specifically, {one phrase: a market signal / design judgment / delivery milestone /
>    coverage gap that is the MIXED contribution of this namespace to {topic}
>    -- not a phrase equally valid for a HIGH-STRUCTURE or EVIDENCE-HEAVY namespace}.

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

**ROLE 2 STOP -- Do not activate ROLE 3 -- SUMMARIZER until: (1) nine artifact sections
present across all three stages; (2) each has a complete MOCK ARTIFACT header with all five
fields (Skill, Topic, Category, Date, Status: MOCK); (3) each has an extended inertia
statement with the skeleton seed phrase and a stage-category-specific instance phrase per
Declaration B -- HIGH-STRUCTURE instance at Stage 1 (naming a state transition, boundary
contract, trigger condition, or configuration key), EVIDENCE-HEAVY instance at Stage 2
(naming a study finding, empirical result, adoption measurement, or hypothesis outcome),
MIXED instance at Stage 3 (naming a market signal, design judgment, delivery milestone, or
coverage gap) -- each instance phrase valid only for its stage category, not cross-stage;
(4) each body is 3-5 sentences, vocabulary-compliant, register-matched; (5) every
REAL-REQUIRED = YES namespace has a REAL-REQUIRED block with the pre-authored REAL-REQUIRED
rationale above copied verbatim per Declaration A.**

---

### ROLE 3 -- SUMMARIZER

You ARE the SUMMARIZER. Produce the coverage summary table. Writing the handoff here means
you have become the HANDOFF WRITER, which you are not yet. You summarize. Nothing else.

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