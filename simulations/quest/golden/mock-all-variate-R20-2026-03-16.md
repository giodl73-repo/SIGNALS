---
skill: quest-variate
skill_target: mock-all
date: 2026-03-16
round: 20
rubric_version: v20
status: VARIATE
---

# mock-all Variate -- Round 20

**Date:** 2026-03-16
**Skill:** mock-all
**Rubric:** v20 (Essential 5, Recommended 3, Aspirational C-09 through C-40 = 32; formula: (E/5*60) + (R/3*30) + (A/32*10))
**Round:** R20 -- two new criteria (C-39, C-40); R19 V-05 retroactively scores 31/32 under v20 (passes C-39, fails C-40)

---

## What R19 Left Open

v20 adds two criteria extracted from R19 observations:

| Criterion | Source | What it tests |
|-----------|--------|---------------|
| C-39 | V-03 fails C-36: two compliance dimensions (REAL-REQUIRED identifier scope and per-stage firing scope) exist as unlabeled prose but neither is labeled. Once labeled (V-04/V-05), the next structural question is whether the labeled declarations are *architecturally separate* -- each governing exactly one dimension -- or whether one declaration subsumes the other's scope, making the labeling decorative. | The preamble's per-stage firing declaration is formally separate from the REAL-REQUIRED canonical identifier declaration: each governs exactly one compliance dimension, neither subsumes the other. A template passes C-39 only when Declaration A contains no per-stage firing language and Declaration B contains no REAL-REQUIRED identifier language. Cross-contamination (each declaration mentions both dimensions) is C-39 FAIL regardless of whether labels are present. |
| C-40 | V-01/V-02 C-38 progression: V-01 cross-stage delegation → V-02 per-stage gate checks with instruction still in ROLE 2 preamble → V-03 per-stage instruction in stage bodies (C-38 PASS). The next bar after "instruction lives in stage body" is "instruction is semantically stage-specific, not copy-pasted boilerplate." R19 V-03 through V-05 all use `-- specifically, {one phrase naming the topic-specific instance of that gap}` in all three stages -- the same generic placeholder. A model receiving this instruction cannot distinguish Stage 1 artifact expectations from Stage 3 artifact expectations. | Each stage body's inertia instruction names a stage-specific artifact type or domain in its instance phrase, not a generic cross-stage phrase that would be equally valid in any other stage. A HIGH-STRUCTURE stage instruction must name HIGH-STRUCTURE artifact domains (state transitions, boundary contracts, trigger conditions). An EVIDENCE-HEAVY stage instruction must name EVIDENCE-HEAVY artifact domains (study findings, empirical results, adoption measurements). A MIXED stage instruction must name MIXED artifact domains (market signals, design judgments, delivery milestones). |

The denominator rises from 30 to 32. Under v20:
- Each aspirational criterion is worth 10/32 = 0.3125 composite points
- Each Recommended criterion is worth 30/3 = 10 composite points
- C-39 and C-40 are each worth 0.3125 composite points

**R19 V-05 retroactive score under v20:** C-39 PASS (Declaration A governs REAL-REQUIRED identifier exclusively; Declaration B governs per-stage firing exclusively -- no cross-contamination). C-40 FAIL (`{one phrase naming the topic-specific instance of that gap}` is the same placeholder in all three stages -- not stage-specific). Retroactive: 31/32 aspirational, composite 99.688.

---

## Round 20 Primary Hypotheses

**H1 (V-01):** Cross-contaminating declarations (each covers both dimensions) and generic instance phrase. Both C-39 and C-40 fail. This is the regression baseline -- it demonstrates the failure mode targeted by both new criteria. C-39 FAIL is visible from the declaration text (each declaration explicitly governs both REAL-REQUIRED identifier AND per-stage firing). C-40 FAIL is visible from the identical instance phrase placeholder in all three stage bodies.

**H2 (V-02 single axis):** Architecturally separate declarations (C-39 PASS) + generic instance phrase (C-40 FAIL). This is R19 V-05 retroactively annotated. C-39 passes because Declaration A contains no per-stage firing language and Declaration B contains no REAL-REQUIRED identifier language. C-40 still fails because the instance phrase placeholder is identical across all stages.

**H3 (V-03 single axis):** Cross-contaminating declarations (C-39 FAIL) + stage-typed instance phrase (C-40 PASS). C-40 passes because each stage body names its own artifact domain class in the instance placeholder. C-39 still fails because the declarations cross-contaminate. H3 tests that C-39 and C-40 are independent: fixing C-40 alone does not affect C-39.

**H4 (V-04/V-05):** Both C-39 PASS and C-40 PASS. V-04 achieves C-40 via a stage-specific instruction hint (instruction-based; model must follow). V-05 achieves C-40 via pre-seeded example phrases per stage (strongest structural guarantee; model copies, not generates).

---

## Axis-Assignment Plan

| Variation | C-39 | C-40 | All prior (C-09 to C-38) | Aspirational | Predicted composite |
|-----------|------|------|--------------------------|--------------|---------------------|
| V-01 | FAIL | FAIL | 30/30 | 30/32 | 99.375 |
| V-02 | PASS | FAIL | 30/30 | 31/32 | 99.688 |
| V-03 | FAIL | PASS | 30/30 | 31/32 | 99.688 |
| V-04 | PASS | PASS (instruction) | 30/30 | 32/32 | 100.0 |
| V-05 | PASS | PASS (pre-seeded) | 30/30 | 32/32 | 100.0 |

Single-axis chain:
- V-01 → V-02: C-39 axis only (declarations become architecturally separate)
- V-01 → V-03: C-40 axis only (instance phrase becomes stage-specific)
- V-02 → V-04: C-40 axis only (add stage-typed instance instruction)
- V-03 → V-04: C-39 axis only (separate the cross-contaminating declarations)
- V-04 → V-05: C-40 structural guarantee upgrade (pre-seeded examples replace instruction-only)

Score derivations under v20:
- V-01: (5/5 × 60) + (3/3 × 30) + (30/32 × 10) = 60 + 30 + 9.375 = **99.375**
- V-02: (5/5 × 60) + (3/3 × 30) + (31/32 × 10) = 60 + 30 + 9.688 = **99.688**
- V-03: (5/5 × 60) + (3/3 × 30) + (31/32 × 10) = 60 + 30 + 9.688 = **99.688**
- V-04: (5/5 × 60) + (3/3 × 30) + (32/32 × 10) = 60 + 30 + 10.0 = **100.0**
- V-05: (5/5 × 60) + (3/3 × 30) + (32/32 × 10) = 60 + 30 + 10.0 = **100.0**

---

## V-01 -- Cross-Contaminating Declarations + Generic Instance (C-39 FAIL + C-40 FAIL, 99.375)

**axis (primary):** C-39 FAIL: both Declaration A and Declaration B in the preamble cover both compliance dimensions. Declaration A explicitly governs REAL-REQUIRED identifier scope AND per-stage inertia firing. Declaration B explicitly governs per-stage inertia extension AND REAL-REQUIRED rationale copying. Neither declaration governs exactly one compliance dimension; each subsumes the other's scope. C-36 PASS: two labeled declarations are present. C-37 PASS: stage gates cite declarations by label. C-38 PASS: stage bodies contain independent per-stage instructions (referencing Declaration A). C-39 FAIL is entirely a property of declaration body text, not of label presence or gate structure.

**axis (secondary):** C-40 FAIL: the inertia instance phrase `{one phrase naming the topic-specific instance of that gap}` is identical in Stage 1, Stage 2, and Stage 3. The placeholder imposes no stage-specific constraint on the model. A model generating a HIGH-STRUCTURE artifact uses the same instance phrase format as a model generating a MIXED artifact. C-40 is the cross-stage boilerplate failure.

**hypothesis:** V-01 demonstrates that C-39 and C-40 are independent of all prior structural criteria. A template can score 30/30 on C-09 through C-38 while failing both new criteria. The composite drop from R19 V-05 (99.688 retro) to V-01 (99.375) is 2 × 0.3125 = 0.313 composite points -- exactly two aspirational criteria.

**predicted:** C-39: FAIL. C-40: FAIL. C-09 through C-38: all PASS (30/30). Essential: 5/5. Recommended: 3/3. Aspirational: 30/32. Composite: 99.375.

**C-39 failure condition:** PASS if Declaration A contains no per-stage firing language OR Declaration B contains no REAL-REQUIRED identifier language. Diagnostic: scan Declaration A for "fires independently," "per-stage," "inertia extension," "Stage 1, Stage 2, Stage 3" -- presence confirms contamination. Scan Declaration B for "canonical identifier," "REAL-REQUIRED," "copies verbatim," "copies from" -- presence confirms contamination. C-39 fails if either declaration is contaminated.

**C-40 failure condition:** PASS if any stage body's instance phrase placeholder includes stage-specific artifact domain terms (for Stage 1: "state transition" / "boundary contract" / "trigger condition"; for Stage 2: "study finding" / "empirical result" / "adoption measurement"; for Stage 3: "market signal" / "design judgment" / "delivery milestone"). Presence of identical generic placeholder in all three stages confirms C-40 FAIL.

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

**Declaration A -- Compliance framework authority:** "REAL-REQUIRED" is the canonical
identifier for the rationale section in this template. Stage STOP gates and REAL-REQUIRED
blocks reference this identifier per Declaration A. This declaration also governs the
per-stage inertia extension requirement: the inertia extension `-- specifically, {instance}`
fires at every artifact-collection stage, independently within Stage 1, Stage 2, and Stage 3.
Both the REAL-REQUIRED block presence and the per-stage inertia extension are Declaration A
requirements enforced at each stage gate.

**Declaration B -- Extension and rationale authority:** The inertia extension instruction
is a required artifact-prefix in every stage; each stage body invokes it independently per
Declaration B. The REAL-REQUIRED rationale block must also appear for each applicable
namespace; the GENERATOR copies it verbatim from the REAL-REQUIRED Rationale section per
Declaration B. Completing a stage without either requirement is a Declaration B violation.
Declaration B governs both per-artifact inertia extension and rationale section copying.

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

Per Declaration A: extend the inertia skeleton for each artifact in this stage:
> Without this signal, {topic}'s feature story would be missing: {ROLE 1 skeleton phrase}
> -- specifically, {one phrase naming the topic-specific instance of that gap}.

For each namespace (flow, trace):

  #### {namespace} -- {skill name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{skill-name}
  Topic:    {topic}
  Category: HIGH-STRUCTURE
  Date:     {today}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {ROLE 1 skeleton phrase} -- specifically, {topic-specific instance}

  {3-5 sentence body; specification language; state/contract/boundary vocabulary;
  DO NOT use interview language, adoption rates, or study framing}

  [If REAL-REQUIRED = YES (compliance-tagged trace):]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {verbatim text from the REAL-REQUIRED Rationale above for compliance-tagged}

**STAGE 1 STOP -- Do not proceed to Stage 2 until: (1) flow and trace artifact sections are
complete; (2) each has a MOCK ARTIFACT header with all five fields; (3) each has an extended
inertia statement with the skeleton phrase and a topic-specific instance per Declaration A;
(4) each body is 3-5 sentences with HIGH-STRUCTURE vocabulary; (5) any compliance-tagged
namespace has a REAL-REQUIRED block with pre-authored rationale copied verbatim per
Declaration B.**

---

**Stage 2 -- EVIDENCE-HEAVY namespaces (prove, listen)**

Per Declaration A: extend the inertia skeleton for each artifact in this stage:
> Without this signal, {topic}'s feature story would be missing: {ROLE 1 skeleton phrase}
> -- specifically, {one phrase naming the topic-specific instance of that gap}.

For each namespace (prove, listen):

  #### {namespace} -- {skill name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{skill-name}
  Topic:    {topic}
  Category: EVIDENCE-HEAVY
  Date:     {today}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {ROLE 1 skeleton phrase} -- specifically, {topic-specific instance}

  {3-5 sentence body; study/data language; hypothesis-and-result framing;
  DO NOT use specification language or schema definitions}

  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {verbatim text from the REAL-REQUIRED Rationale above for this namespace}

**STAGE 2 STOP -- Do not proceed to Stage 3 until: (1) prove and listen artifact sections
are complete; (2) each has a MOCK ARTIFACT header with all five fields; (3) each has an
extended inertia statement with the skeleton phrase and a topic-specific instance per
Declaration A; (4) each body is 3-5 sentences with EVIDENCE-HEAVY vocabulary; (5) each
has a REAL-REQUIRED block with pre-authored rationale copied verbatim per Declaration B.**

---

**Stage 3 -- MIXED namespaces (scout, draft, review, program, topic)**

Per Declaration A: extend the inertia skeleton for each artifact in this stage:
> Without this signal, {topic}'s feature story would be missing: {ROLE 1 skeleton phrase}
> -- specifically, {one phrase naming the topic-specific instance of that gap}.

For each namespace (scout, draft, review, program, topic):

  #### {namespace} -- {skill name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{skill-name}
  Topic:    {topic}
  Category: MIXED
  Date:     {today}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {ROLE 1 skeleton phrase} -- specifically, {topic-specific instance}

  {3-5 sentence body; discovery/signal language or structural scaffold vocabulary as
  appropriate per ROLE 1; MUST-use vocabulary applied; DO NOT-use vocabulary avoided}

  [If REAL-REQUIRED = YES (compliance-tagged scout):]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {verbatim text from the REAL-REQUIRED Rationale above for compliance-tagged}

**ROLE 2 STOP -- Do not activate ROLE 3 -- SUMMARIZER until: (1) nine artifact sections
present across all three stages; (2) each has a complete MOCK ARTIFACT header with all five
fields (Skill, Topic, Category, Date, Status: MOCK); (3) each has an extended inertia
statement with the skeleton seed phrase and a topic-specific instance -- verified at Stage 1,
Stage 2, and Stage 3 individually per Declaration A; (4) each body is 3-5 sentences,
vocabulary-compliant, register-matched; (5) every REAL-REQUIRED = YES namespace has a
REAL-REQUIRED block with the pre-authored REAL-REQUIRED rationale above copied verbatim
per Declaration B.**

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

---

---

## V-02 -- Architecturally Separate Declarations + Generic Instance (C-39 PASS + C-40 FAIL, 99.688)

**axis (primary):** C-39 PASS: Declaration A contains only REAL-REQUIRED identifier language (canonical name, GENERATOR copy instruction, gate reference mechanism). Declaration A contains no per-stage firing language, no mention of Stage 1/Stage 2/Stage 3, no reference to the inertia extension. Declaration B contains only per-stage inertia extension language (fires independently, stage-local, stage gate enforcement). Declaration B contains no REAL-REQUIRED identifier language, no mention of rationale copying. Each declaration governs exactly one compliance dimension; neither subsumes the other. This is R19 V-05 structure annotated under v20.

**axis (secondary):** C-40 FAIL: the inertia instance phrase `{one phrase naming the topic-specific instance of that gap}` is identical in Stage 1, Stage 2, and Stage 3. No stage-specific artifact domain vocabulary constrains the model's instance phrase generation in any stage.

**hypothesis:** V-02 confirms that R19 V-05 was already C-39 compliant. The 0.3125 composite gain from V-01 (99.375) to V-02 (99.688) is entirely the C-39 fix. The declaration structure in R19 V-05 was clean by inspection; R20 makes this explicit. V-02 is the single-axis C-39 fix, holding C-40 constant.

**predicted:** C-39: PASS. C-40: FAIL. C-09 through C-38: all PASS (30/30). Essential: 5/5. Recommended: 3/3. Aspirational: 31/32. Composite: 99.688.

**failure condition:** C-39 FAIL if Declaration A mentions per-stage firing, inertia extension, or stage-independent execution. C-39 FAIL if Declaration B mentions REAL-REQUIRED identifier, canonical name, or rationale copying. The independence test: read Declaration A alone -- it should fully describe the REAL-REQUIRED compliance mechanism without referencing inertia. Read Declaration B alone -- it should fully describe the per-stage inertia mechanism without referencing REAL-REQUIRED.

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

Per Declaration B: extend the inertia skeleton for each artifact in this stage:
> Without this signal, {topic}'s feature story would be missing: {ROLE 1 skeleton phrase}
> -- specifically, {one phrase naming the topic-specific instance of that gap}.

For each namespace (flow, trace):

  #### {namespace} -- {skill name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{skill-name}
  Topic:    {topic}
  Category: HIGH-STRUCTURE
  Date:     {today}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {ROLE 1 skeleton phrase} -- specifically, {topic-specific instance}

  {3-5 sentence body; specification language; state/contract/boundary vocabulary;
  DO NOT use interview language, adoption rates, or study framing}

  [If REAL-REQUIRED = YES (compliance-tagged trace):]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {verbatim text from the REAL-REQUIRED Rationale above for compliance-tagged}

**STAGE 1 STOP -- Do not proceed to Stage 2 until: (1) flow and trace artifact sections are
complete; (2) each has a MOCK ARTIFACT header with all five fields; (3) each has an extended
inertia statement with the skeleton phrase and a topic-specific instance per Declaration B;
(4) each body is 3-5 sentences with HIGH-STRUCTURE vocabulary; (5) any compliance-tagged
namespace has a REAL-REQUIRED block with pre-authored REAL-REQUIRED rationale copied
verbatim per Declaration A.**

---

**Stage 2 -- EVIDENCE-HEAVY namespaces (prove, listen)**

Per Declaration B: extend the inertia skeleton for each artifact in this stage:
> Without this signal, {topic}'s feature story would be missing: {ROLE 1 skeleton phrase}
> -- specifically, {one phrase naming the topic-specific instance of that gap}.

For each namespace (prove, listen):

  #### {namespace} -- {skill name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{skill-name}
  Topic:    {topic}
  Category: EVIDENCE-HEAVY
  Date:     {today}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {ROLE 1 skeleton phrase} -- specifically, {topic-specific instance}

  {3-5 sentence body; study/data language; hypothesis-and-result framing;
  DO NOT use specification language or schema definitions}

  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {verbatim text from the REAL-REQUIRED Rationale above for this namespace}

**STAGE 2 STOP -- Do not proceed to Stage 3 until: (1) prove and listen artifact sections
are complete; (2) each has a MOCK ARTIFACT header with all five fields; (3) each has an
extended inertia statement with the skeleton phrase and a topic-specific instance per
Declaration B; (4) each body is 3-5 sentences with EVIDENCE-HEAVY vocabulary; (5) each
has a REAL-REQUIRED block with pre-authored REAL-REQUIRED rationale copied verbatim per
Declaration A.**

---

**Stage 3 -- MIXED namespaces (scout, draft, review, program, topic)**

Per Declaration B: extend the inertia skeleton for each artifact in this stage:
> Without this signal, {topic}'s feature story would be missing: {ROLE 1 skeleton phrase}
> -- specifically, {one phrase naming the topic-specific instance of that gap}.

For each namespace (scout, draft, review, program, topic):

  #### {namespace} -- {skill name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{skill-name}
  Topic:    {topic}
  Category: MIXED
  Date:     {today}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {ROLE 1 skeleton phrase} -- specifically, {topic-specific instance}

  {3-5 sentence body; discovery/signal language or structural scaffold vocabulary as
  appropriate per ROLE 1; MUST-use vocabulary applied; DO NOT-use vocabulary avoided}

  [If REAL-REQUIRED = YES (compliance-tagged scout):]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {verbatim text from the REAL-REQUIRED Rationale above for compliance-tagged}

**ROLE 2 STOP -- Do not activate ROLE 3 -- SUMMARIZER until: (1) nine artifact sections
present across all three stages; (2) each has a complete MOCK ARTIFACT header with all five
fields (Skill, Topic, Category, Date, Status: MOCK); (3) each has an extended inertia
statement with the skeleton seed phrase and a topic-specific instance -- verified at Stage 1,
Stage 2, and Stage 3 individually per Declaration B; (4) each body is 3-5 sentences,
vocabulary-compliant, register-matched; (5) every REAL-REQUIRED = YES namespace has a
REAL-REQUIRED block with the pre-authored REAL-REQUIRED rationale above copied verbatim
per Declaration A.**

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

---

---

## V-03 -- Cross-Contaminating Declarations + Stage-Typed Instance (C-39 FAIL + C-40 PASS, 99.688)

**axis (primary):** C-40 PASS: each stage body names a stage-specific artifact domain class in its instance phrase placeholder. Stage 1 (HIGH-STRUCTURE) constrains the instance phrase to state transition, boundary contract, trigger condition, or configuration key vocabulary. Stage 2 (EVIDENCE-HEAVY) constrains the instance phrase to study finding, empirical result, adoption measurement, or hypothesis outcome vocabulary. Stage 3 (MIXED) constrains the instance phrase to market signal, design judgment, delivery milestone, or coverage gap vocabulary. A model generating a Stage 1 instance phrase cannot produce the same phrase as a Stage 2 instance phrase -- the domain vocabularies are disjoint.

**axis (secondary):** C-39 FAIL: same cross-contaminating declarations as V-01. Declaration A governs both REAL-REQUIRED identifier AND per-stage inertia extension. Declaration B governs both per-artifact inertia AND REAL-REQUIRED rationale copying. Neither declaration governs exactly one compliance dimension.

**hypothesis:** V-03 tests that C-39 and C-40 are independent axes. A template can achieve C-40 PASS (stage-specific instance phrases) while failing C-39 (cross-contaminating declarations). The composite score of V-03 (99.688) equals V-02 (99.688) -- confirming that C-39 and C-40 carry equal weight (0.3125 points each) and are not coupled. The sole discriminant between V-02 and V-03 is which new criterion passes.

**predicted:** C-39: FAIL (cross-contaminating declarations). C-40: PASS (stage-typed instance phrase domains). C-09 through C-38: all PASS (30/30). Essential: 5/5. Recommended: 3/3. Aspirational: 31/32. Composite: 99.688.

**failure condition for C-40:** C-40 FAIL if any stage body's instance phrase placeholder lacks stage-specific domain vocabulary. Diagnostic: read Stage 1 instance placeholder -- must mention at least one HIGH-STRUCTURE domain term (state transition, boundary contract, trigger condition, configuration key). Read Stage 2 -- must mention at least one EVIDENCE-HEAVY domain term (study finding, empirical result, adoption measurement, hypothesis outcome). Read Stage 3 -- must mention at least one MIXED domain term (market signal, design judgment, delivery milestone, coverage gap). A placeholder valid for multiple stage categories fails C-40.

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

**Declaration A -- Compliance framework authority:** "REAL-REQUIRED" is the canonical
identifier for the rationale section in this template. Stage STOP gates and REAL-REQUIRED
blocks reference this identifier per Declaration A. This declaration also governs the
per-stage inertia extension requirement: the inertia extension `-- specifically, {instance}`
fires at every artifact-collection stage, independently within Stage 1, Stage 2, and Stage 3.
Both the REAL-REQUIRED block presence and the per-stage inertia extension are Declaration A
requirements enforced at each stage gate.

**Declaration B -- Extension and rationale authority:** The inertia extension instruction
is a required artifact-prefix in every stage; each stage body invokes it independently per
Declaration B. The REAL-REQUIRED rationale block must also appear for each applicable
namespace; the GENERATOR copies it verbatim from the REAL-REQUIRED Rationale section per
Declaration B. Completing a stage without either requirement is a Declaration B violation.
Declaration B governs both per-artifact inertia extension and rationale section copying.

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

Per Declaration A: extend the inertia skeleton for each artifact in this stage:
> Without this signal, {topic}'s feature story would be missing: {ROLE 1 skeleton phrase}
> -- specifically, {one phrase naming a state transition, boundary contract, trigger
>    condition, or configuration key that defines this namespace's HIGH-STRUCTURE
>    contribution to {topic}}.

For each namespace (flow, trace):

  #### {namespace} -- {skill name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{skill-name}
  Topic:    {topic}
  Category: HIGH-STRUCTURE
  Date:     {today}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {ROLE 1 skeleton phrase} -- specifically, {HIGH-STRUCTURE instance: state transition /
  boundary contract / trigger condition / configuration key for {topic}}

  {3-5 sentence body; specification language; state/contract/boundary vocabulary;
  DO NOT use interview language, adoption rates, or study framing}

  [If REAL-REQUIRED = YES (compliance-tagged trace):]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {verbatim text from the REAL-REQUIRED Rationale above for compliance-tagged}

**STAGE 1 STOP -- Do not proceed to Stage 2 until: (1) flow and trace artifact sections are
complete; (2) each has a MOCK ARTIFACT header with all five fields; (3) each has an extended
inertia statement with the skeleton phrase and a HIGH-STRUCTURE instance phrase per
Declaration A; (4) each body is 3-5 sentences with HIGH-STRUCTURE vocabulary; (5) any
compliance-tagged namespace has a REAL-REQUIRED block with pre-authored rationale copied
verbatim per Declaration B.**

---

**Stage 2 -- EVIDENCE-HEAVY namespaces (prove, listen)**

Per Declaration A: extend the inertia skeleton for each artifact in this stage:
> Without this signal, {topic}'s feature story would be missing: {ROLE 1 skeleton phrase}
> -- specifically, {one phrase naming a study finding, empirical result, adoption
>    measurement, or hypothesis outcome that defines this namespace's EVIDENCE-HEAVY
>    contribution to {topic}}.

For each namespace (prove, listen):

  #### {namespace} -- {skill name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{skill-name}
  Topic:    {topic}
  Category: EVIDENCE-HEAVY
  Date:     {today}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {ROLE 1 skeleton phrase} -- specifically, {EVIDENCE-HEAVY instance: study finding /
  empirical result / adoption measurement / hypothesis outcome for {topic}}

  {3-5 sentence body; study/data language; hypothesis-and-result framing;
  DO NOT use specification language or schema definitions}

  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {verbatim text from the REAL-REQUIRED Rationale above for this namespace}

**STAGE 2 STOP -- Do not proceed to Stage 3 until: (1) prove and listen artifact sections
are complete; (2) each has a MOCK ARTIFACT header with all five fields; (3) each has an
extended inertia statement with the skeleton phrase and an EVIDENCE-HEAVY instance phrase
per Declaration A; (4) each body is 3-5 sentences with EVIDENCE-HEAVY vocabulary; (5) each
has a REAL-REQUIRED block with pre-authored rationale copied verbatim per Declaration B.**

---

**Stage 3 -- MIXED namespaces (scout, draft, review, program, topic)**

Per Declaration A: extend the inertia skeleton for each artifact in this stage:
> Without this signal, {topic}'s feature story would be missing: {ROLE 1 skeleton phrase}
> -- specifically, {one phrase naming a market signal, design judgment, delivery milestone,
>    or coverage gap that defines this namespace's MIXED contribution to {topic}}.

For each namespace (scout, draft, review, program, topic):

  #### {namespace} -- {skill name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{skill-name}
  Topic:    {topic}
  Category: MIXED
  Date:     {today}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {ROLE 1 skeleton phrase} -- specifically, {MIXED instance: market signal / design judgment /
  delivery milestone / coverage gap for {topic}}

  {3-5 sentence body; discovery/signal language or structural scaffold vocabulary as
  appropriate per ROLE 1; MUST-use vocabulary applied; DO NOT-use vocabulary avoided}

  [If REAL-REQUIRED = YES (compliance-tagged scout):]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {verbatim text from the REAL-REQUIRED Rationale above for compliance-tagged}

**ROLE 2 STOP -- Do not activate ROLE 3 -- SUMMARIZER until: (1) nine artifact sections
present across all three stages; (2) each has a complete MOCK ARTIFACT header with all five
fields (Skill, Topic, Category, Date, Status: MOCK); (3) each has an extended inertia
statement with the skeleton seed phrase and a stage-category-specific instance phrase --
HIGH-STRUCTURE instance at Stage 1, EVIDENCE-HEAVY instance at Stage 2, MIXED instance at
Stage 3, per Declaration A; (4) each body is 3-5 sentences, vocabulary-compliant,
register-matched; (5) every REAL-REQUIRED = YES namespace has a REAL-REQUIRED block with
the pre-authored REAL-REQUIRED rationale above copied verbatim per Declaration B.**

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

---

---

## V-04 -- Separate Declarations + Stage-Typed Instance via Instruction (C-39 PASS + C-40 PASS, 100.0)

**axis (primary):** C-39 PASS + C-40 PASS. Declaration A governs only REAL-REQUIRED identifier authority (no per-stage firing language). Declaration B governs only per-stage inertia extension authority (no REAL-REQUIRED identifier language). C-39 PASS: architecturally separate. C-40 PASS: each stage body's inertia instruction names the stage's specific artifact domain class. Stage 1 instruction names HIGH-STRUCTURE artifact domains. Stage 2 instruction names EVIDENCE-HEAVY artifact domains. Stage 3 instruction names MIXED artifact domains. The instance phrase cannot be copy-pasted across stages -- each stage's domain vocabulary is disjoint.

**axis (secondary):** C-40 is achieved via instruction (the stage body tells the model which artifact domain class to use for the instance phrase) rather than pre-seeded examples. The model must apply the instruction to generate a domain-appropriate instance phrase. This is instruction-based C-40 compliance -- structurally weaker than V-05's pre-seeded examples because it requires model-side inference, not transcription.

**hypothesis:** V-04 achieves 32/32 aspirational criteria. The composite ceiling (100.0) is reachable with instruction-based C-40 compliance. V-05 tests whether pre-seeded examples provide a stronger structural guarantee for C-40 at identical rubric score.

**predicted:** C-09 through C-40: all PASS (32/32). Essential: 5/5. Recommended: 3/3. Aspirational: 32/32. Composite: 100.0.

**structural risk for C-40:** Instruction-based C-40 compliance depends on model behavior. A model that ignores the artifact-domain constraint and generates a generic instance phrase would fail C-40 in live runs despite the template's rubric-passing structure. V-05 eliminates this risk by pre-seeding an example phrase the model copies rather than generates.

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
The instance phrase must name a HIGH-STRUCTURE artifact domain specific to {topic}:
state transition, boundary contract, trigger condition, or configuration key.
> Without this signal, {topic}'s feature story would be missing: {ROLE 1 skeleton phrase}
> -- specifically, {one phrase: a state transition / boundary contract / trigger condition /
>    configuration key that this HIGH-STRUCTURE namespace contributes to {topic}}.

For each namespace (flow, trace):

  #### {namespace} -- {skill name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{skill-name}
  Topic:    {topic}
  Category: HIGH-STRUCTURE
  Date:     {today}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {ROLE 1 skeleton phrase} -- specifically, {HIGH-STRUCTURE instance for {topic}}

  {3-5 sentence body; specification language; state/contract/boundary vocabulary;
  DO NOT use interview language, adoption rates, or study framing}

  [If REAL-REQUIRED = YES (compliance-tagged trace):]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {verbatim text from the REAL-REQUIRED Rationale above for compliance-tagged}

**STAGE 1 STOP -- Do not proceed to Stage 2 until: (1) flow and trace artifact sections are
complete; (2) each has a MOCK ARTIFACT header with all five fields; (3) each has an extended
inertia statement with the skeleton phrase and a HIGH-STRUCTURE instance phrase per
Declaration B -- the instance phrase names a state transition, boundary contract, trigger
condition, or configuration key for {topic}; (4) each body is 3-5 sentences with
HIGH-STRUCTURE vocabulary; (5) any compliance-tagged namespace has a REAL-REQUIRED block
with pre-authored REAL-REQUIRED rationale copied verbatim per Declaration A.**

---

**Stage 2 -- EVIDENCE-HEAVY namespaces (prove, listen)**

Per Declaration B: extend the inertia skeleton for each artifact in this stage.
The instance phrase must name an EVIDENCE-HEAVY artifact domain specific to {topic}:
study finding, empirical result, adoption measurement, or hypothesis outcome.
> Without this signal, {topic}'s feature story would be missing: {ROLE 1 skeleton phrase}
> -- specifically, {one phrase: a study finding / empirical result / adoption measurement /
>    hypothesis outcome that this EVIDENCE-HEAVY namespace contributes to {topic}}.

For each namespace (prove, listen):

  #### {namespace} -- {skill name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{skill-name}
  Topic:    {topic}
  Category: EVIDENCE-HEAVY
  Date:     {today}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {ROLE 1 skeleton phrase} -- specifically, {EVIDENCE-HEAVY instance for {topic}}

  {3-5 sentence body; study/data language; hypothesis-and-result framing;
  DO NOT use specification language or schema definitions}

  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {verbatim text from the REAL-REQUIRED Rationale above for this namespace}

**STAGE 2 STOP -- Do not proceed to Stage 3 until: (1) prove and listen artifact sections
are complete; (2) each has a MOCK ARTIFACT header with all five fields; (3) each has an
extended inertia statement with the skeleton phrase and an EVIDENCE-HEAVY instance phrase
per Declaration B -- the instance phrase names a study finding, empirical result, adoption
measurement, or hypothesis outcome for {topic}; (4) each body is 3-5 sentences with
EVIDENCE-HEAVY vocabulary; (5) each has a REAL-REQUIRED block with pre-authored REAL-
REQUIRED rationale copied verbatim per Declaration A.**

---

**Stage 3 -- MIXED namespaces (scout, draft, review, program, topic)**

Per Declaration B: extend the inertia skeleton for each artifact in this stage.
The instance phrase must name a MIXED artifact domain specific to {topic}:
market signal, design judgment, delivery milestone, or coverage gap.
> Without this signal, {topic}'s feature story would be missing: {ROLE 1 skeleton phrase}
> -- specifically, {one phrase: a market signal / design judgment / delivery milestone /
>    coverage gap that this MIXED namespace contributes to {topic}}.

For each namespace (scout, draft, review, program, topic):

  #### {namespace} -- {skill name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{skill-name}
  Topic:    {topic}
  Category: MIXED
  Date:     {today}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {ROLE 1 skeleton phrase} -- specifically, {MIXED instance for {topic}}

  {3-5 sentence body; discovery/signal language or structural scaffold vocabulary as
  appropriate per ROLE 1; MUST-use vocabulary applied; DO NOT-use vocabulary avoided}

  [If REAL-REQUIRED = YES (compliance-tagged scout):]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {verbatim text from the REAL-REQUIRED Rationale above for compliance-tagged}

**ROLE 2 STOP -- Do not activate ROLE 3 -- SUMMARIZER until: (1) nine artifact sections
present across all three stages; (2) each has a complete MOCK ARTIFACT header with all five
fields (Skill, Topic, Category, Date, Status: MOCK); (3) each has an extended inertia
statement with the skeleton seed phrase and a stage-category-specific instance phrase per
Declaration B -- HIGH-STRUCTURE domain at Stage 1, EVIDENCE-HEAVY domain at Stage 2, MIXED
domain at Stage 3; (4) each body is 3-5 sentences, vocabulary-compliant, register-matched;
(5) every REAL-REQUIRED = YES namespace has a REAL-REQUIRED block with the pre-authored
REAL-REQUIRED rationale above copied verbatim per Declaration A.**

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

---

---

## V-05 -- Separate Declarations + Pre-Seeded Stage Instance Examples (C-39 PASS + C-40 PASS strongest, 100.0)

**axis (primary):** C-40 PASS via pre-seeded examples (strongest structural guarantee). Each stage body contains not just an instruction but a pre-printed example instance phrase in the correct domain vocabulary. For Stage 1: an example HIGH-STRUCTURE instance phrase is printed in the template (the model copies or adapts it). For Stage 2: an example EVIDENCE-HEAVY instance phrase is printed. For Stage 3: an example MIXED instance phrase is printed. The model cannot produce a cross-stage generic phrase because it is copying or adapting a stage-specific example already on the page.

**axis (secondary):** C-39 PASS: identical to V-04 -- Declaration A governs REAL-REQUIRED identifier exclusively; Declaration B governs per-stage inertia extension exclusively. The structural difference between V-04 and V-05 is entirely in Stage body instruction format: V-04 constrains by instruction (model must generate a domain-appropriate phrase); V-05 constrains by example (model copies or adapts a pre-printed domain-appropriate phrase).

**hypothesis:** V-05 is the 32/32 ceiling with the strongest structural guarantee for C-40. The pre-seeded example eliminates the model-behavior risk in V-04: even a model that ignores the artifact-domain instruction cannot produce a cross-stage generic phrase when an example is already pre-printed. V-05's C-40 guarantee is of the same structural class as V-05's C-13/C-14 guarantee in the scout-feasibility series: the model transcribes rather than generates.

**predicted:** C-09 through C-40: all PASS (32/32). Essential: 5/5. Recommended: 3/3. Aspirational: 32/32. Composite: 100.0.

**V-04 vs V-05 structural guarantee comparison:**

| Property | V-04 (instruction-based C-40) | V-05 (pre-seeded C-40) |
|----------|-------------------------------|------------------------|
| C-40 compliance mechanism | Model must apply domain-constraint instruction | Model copies or adapts pre-seeded example |
| Risk of generic cross-stage phrase | Model may ignore constraint | Pre-seeded example blocks generic phrase |
| Rubric score | 100.0 | 100.0 |
| Structural class | Same as V-03 inertia framing (R3) | Same as V-02/V-05 template-completion (R3) |

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
REAL-REQUIRED block with pre-authored REAL-REQUIRED rationale copied verbatim per
Declaration A.**

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
