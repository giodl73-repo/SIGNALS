---
skill: quest-variate
skill_target: mock-all
date: 2026-03-16
round: 17
rubric_version: v17
status: VARIATE
---

# mock-all Variate -- Round 17

**Date:** 2026-03-16
**Skill:** mock-all
**Rubric:** v17 (C-01 through C-35; aspirational denominator = 27)
**Round:** R17 -- two new criteria (C-34, C-35); R16 V-05 is the reference ceiling at 25/25 on v16 criteria

---

## What R16 Left Open

v17 adds two new aspirational criteria extracted from Round 16 structural gaps:

| Criterion | Source | What it tests |
|-----------|--------|---------------|
| C-34 | V-05 R16 -- preamble to the REAL-REQUIRED Rationale section declared: '"REAL-REQUIRED" is the semantic identifier for this section'; V-01--V-04 R16 all fail: none contain a template preamble statement that explicitly declares "REAL-REQUIRED" as the canonical authoritative identifier before any gate references it | The template preamble explicitly declares the semantic role identifier "REAL-REQUIRED" as the canonical authoritative label, establishing document-scope identifier authority before any gate references it. C-34 is a strict refinement of C-33: C-34 pass implies C-33 pass; C-33 pass does not imply C-34 pass. A gate using "REAL-REQUIRED" in its provenance reference clause (C-33 PASS) without a preamble declaration satisfies C-33 but fails C-34 -- the identifier's authority is implicit in C-33 (derivable by matching gate label to section header) and explicit in C-34 (stated before any gate references it). |
| C-35 | V-05 R16 -- the Inertia Deepening Protocol instantiated `-- specifically, {instance}` at Stage 1+2+3 individually; V-01--V-04 R16 all present the inertia extension at a single composite or preamble-level point without per-stage instantiation | The inertia extension `-- specifically, {instance}` instruction is instantiated at every artifact-collection stage of the skill template, not only at a single composite or terminal instruction point. C-35 is a strict refinement of C-17 for multi-stage templates: in a single-stage template C-35 = C-17 (one stage, one application); in a multi-stage template C-35 requires per-stage instantiation. The discriminating test: a multi-stage template where the instruction appears only in a shared opening preamble passes C-17 (instruction present) but fails C-35 (absent at intermediate stages). |

The denominator rises from 25 to 27. R16 V-05 retroactively scores C-34 PASS (preamble line '"REAL-REQUIRED" is the semantic identifier for this section' is a document-scope canonical-authority declaration preceding the gate) and C-35 PASS (three-stage deepening protocol: each stage carries its own binding instruction; Stage 2 is the designated `-- specifically, {instance}` extension stage, with Stage 1 carrying verbatim-seed binding and Stage 3 carrying action-anchor binding, each instantiated independently within its stage).

---

## Round 17 Primary Hypothesis

Confirm the C-34 two-way discrimination and the C-35 stage-isolation:

| Case | C-33 | C-34 | Mechanism |
|------|------|------|-----------|
| Bottom | PASS | FAIL | Gate uses "REAL-REQUIRED" semantic identifier (C-33 PASS); template preamble contains no declaration of canonical identifier authority; authority derivable by body traversal only |
| Ceiling | PASS | PASS | Preamble explicitly declares "REAL-REQUIRED" as canonical authoritative label; gate cites an already-declared name |

| Case | C-17 | C-35 | Mechanism |
|------|------|------|-----------|
| Single-stage | PASS | PASS (trivial) | One artifact-collection stage; C-35 = C-17; no multi-stage test possible |
| Multi-stage + terminal | PASS | FAIL | Multiple stages; `-- specifically` stated once in shared ROLE 2 preamble; absent from intermediate stage bodies; C-17 PASS, C-35 FAIL |
| Multi-stage + per-stage | PASS | PASS | Multiple stages; `-- specifically` instantiated within each stage individually; per-stage gates enforce it |

C-34 FAIL cases isolated in V-01 and V-02 (single-stage; no preamble declaration / passive description).
C-35 FAIL case isolated in V-03 (multi-stage; terminal-only instruction).
C-34 PASS + C-35 PASS ceiling in V-04 and V-05.

---

## Axis-Assignment Plan

| Variation | C-34 | C-35 | Secondary axis | Predicted |
|-----------|------|------|----------------|-----------|
| V-01 | FAIL | PASS (trivial) | Standard 4-role; no preamble declaration; gate uses "REAL-REQUIRED" semantic identifier | 26/27 |
| V-02 | FAIL | PASS (trivial) | Passive-descriptive preamble (locative reference to section, not canonical declaration); phase-boundary annotations | 26/27 |
| V-03 | PASS | FAIL | Multi-stage ROLE 2 (HIGH-STRUCTURE / EVIDENCE-HEAVY / MIXED); `-- specifically` in ROLE 2 opening preamble only, absent from stage bodies | 26/27 |
| V-04 | PASS | PASS | Multi-stage ROLE 2; `-- specifically` within each stage individually; per-stage STOP gates enforce it | 27/27 |
| V-05 | PASS | PASS | Multi-stage ROLE 2; preamble unifies C-34 + C-35 via Declaration A + Declaration B before any role activates | 27/27 |

C-34 discrimination: V-01/V-02 (Bottom) vs V-03/V-04/V-05 (Ceiling).
C-35 discrimination: V-01/V-02 (trivial single-stage) vs V-03 (multi-stage FAIL) vs V-04/V-05 (multi-stage PASS).
Three distinct 26/27 failure paths: V-01 (C-34 FAIL only), V-02 (C-34 FAIL only, different register), V-03 (C-35 FAIL only).

---

## V-01 -- No-Preamble Semantic-Gate (C-34 FAIL)

**axis (primary):** C-33 PASS + C-34 FAIL. The ROLE 2 section is labeled "REAL-REQUIRED Rationale" and the ROLE 2 STOP gate says "with the pre-authored REAL-REQUIRED rationale above copied verbatim" (C-33 PASS: gate names block by semantic identifier and directs verbatim copy). The template preamble -- the role-framing section before ROLE 1 -- contains no statement declaring "REAL-REQUIRED" as the canonical authoritative identifier. Authority is implicit: a reader must traverse to ROLE 2's section header and match it against the gate label. C-34 FAIL.

**axis (secondary):** Standard 4-role structure without phase-boundary annotations. Single-stage inertia extension in ROLE 2 (C-35 = C-17 trivially PASS). Full prior-round criteria at ceiling: seed chain (C-29 PASS: seeds authored; C-31 PASS: gate cites list, prohibits paraphrase); table-coupling cluster (C-27 PASS: column names verbatim; C-28 PASS: gate self-annotates required field names); identity staircase at ceiling (C-22 PASS: ontological framing; C-23 PASS: per-activation affirmation).

**hypothesis:** V-01 isolates the no-preamble register for C-34 FAIL. Everything at the gate level is correct -- C-33 PASS is confirmed. The only absent element is the document-scope declaration that establishes "REAL-REQUIRED" as the canonical name before the gate references it. The absence is structural: no template preamble sentence, no role-framing declaration, no pre-role authority statement. A reader of the template preamble cannot determine from it that "REAL-REQUIRED" is the canonical identifier; they must search the ROLE 2 body.

**predicted:** C-01 through C-33: PASS. C-34: FAIL (no preamble declaration of canonical identifier authority). C-35: PASS (single-stage; C-35 = C-17). Score: 26/27.

**failure condition:** C-34 PASS if the role-framing preamble incidentally contains a sentence explicitly declaring "REAL-REQUIRED" as the canonical identifier. Diagnostic: scan the template section before ROLE 1 for any sentence of the form '"REAL-REQUIRED" is the canonical/authoritative/semantic identifier for...' or equivalent declarative form; absence confirms C-34 FAIL.

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

You ARE the GENERATOR. Produce nine namespace artifact sections, one per ROLE 1 row, in
table order. Writing a coverage summary here means you have become the SUMMARIZER, which
you are not yet. You generate. Nothing else.

---

**REAL-REQUIRED Rationale**

For namespaces where REAL-REQUIRED = YES, the following rationale content is pre-authored
here in the skill template body. Copy the matching text verbatim into the REAL-REQUIRED
block for that namespace. Do not substitute, paraphrase, or expand. The template is the
author; the GENERATOR copies:

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

Before each artifact body, extend the inertia skeleton:
> Without this signal, {topic}'s feature story would be missing: {ROLE 1 skeleton phrase}
> -- specifically, {one phrase naming the topic-specific instance of that gap}.

For each namespace:

  #### {namespace} -- {skill name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{skill-name}
  Topic:    {topic}
  Category: {from ROLE 1}
  Date:     {today}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {ROLE 1 skeleton phrase} -- specifically, {topic-specific instance}

  {3-5 sentence body; register matches Category; MUST-use vocabulary applied; DO NOT-use
  vocabulary avoided; body grounded in the extended inertia statement}

  [If REAL-REQUIRED = YES:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {verbatim text from the REAL-REQUIRED Rationale above for this namespace}

**ROLE 2 STOP -- Do not activate ROLE 3 -- SUMMARIZER until: (1) nine artifact sections
present; (2) each has a complete MOCK ARTIFACT header with all five fields (Skill, Topic,
Category, Date, Status: MOCK); (3) each has an extended inertia statement with both the
skeleton seed phrase and a topic-specific instance; (4) each body is 3-5 sentences,
vocabulary-compliant, register-matched, grounded in the inertia statement; (5) every
REAL-REQUIRED = YES namespace has a REAL-REQUIRED block with the pre-authored REAL-REQUIRED
rationale above copied verbatim.**

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

## V-02 -- Passive-Preamble with Phase Annotations (C-34 FAIL)

**axis (primary):** C-33 PASS + C-34 FAIL. The ROLE 2 section is labeled "REAL-REQUIRED
Rationale" and the gate uses "REAL-REQUIRED" in the provenance reference clause (C-33 PASS).
The template preamble contains a reference to the section by name -- but it is a
locative/procedural description, not a canonical-authority declaration. The preamble says
"The REAL-REQUIRED Rationale section in ROLE 2 contains pre-authored rationale for
REAL-REQUIRED = YES namespaces. Copy the matching entry verbatim when generating a
REAL-REQUIRED block." This tells the GENERATOR where to find the content (procedural) and
names the section (locative), but does not assert that "REAL-REQUIRED" is THE canonical
identifier with document-scope authority. C-34 FAIL: naming a section in passing is not
the same as declaring its identifier as canonical.

**axis (secondary):** Phase-boundary annotations between each role. Between ROLE 1 and
ROLE 2, and between ROLE 2 and ROLE 3, an explicit boundary declaration states which role
just completed and which scope is active next. This tests whether C-34 FAIL is stable when
the template contains structural padding that could superficially resemble a preamble
declaration. Single-stage inertia (C-35 = C-17 trivially PASS).

**hypothesis:** V-02 tests the passive-preamble register for C-34 FAIL. A procedural
instruction that references the section by name ("copy from the REAL-REQUIRED Rationale
section") is not a canonical-authority declaration. The distinction: a canonical-authority
declaration establishes the identifier as authoritative ("this is the canonical name");
a procedural instruction uses the name as a locator ("look here"). A reader of the preamble
in V-02 learns the section exists and where it is, but does not receive an explicit assertion
that "REAL-REQUIRED" is the canonical identifier to be used when referencing it in gates.
C-34 FAIL. Phase annotations confirm that structural padding does not rescue C-34.

**predicted:** C-01 through C-33: PASS. C-34: FAIL (preamble describes section procedurally,
does not declare identifier canonical authority). C-35: PASS (single-stage). Score: 26/27.

**failure condition:** C-34 PASS if the procedural preamble sentence is interpreted as an
authority declaration. Diagnostic: the discriminating test is whether the preamble uses
declarative form ("is the canonical identifier") vs. locative/procedural form ("contains"
or "see...for"); only declarative form satisfies C-34.

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

The REAL-REQUIRED Rationale section in ROLE 2 below contains pre-authored rationale
sentences for all namespaces where REAL-REQUIRED = YES. When generating a REAL-REQUIRED
block, copy the matching entry from that section verbatim into the Rationale field.

---

PHASE BOUNDARY: Pre-classification.
Nothing from ROLE 2, 3, or 4 may appear in ROLE 1 output.
ROLE 1 scope: classification table only.

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

PHASE BOUNDARY: Classification complete.
ROLE 1 table verified. Proceed to ROLE 2.
ROLE 2 scope: artifact bodies only. No coverage summary. No handoff.

### ROLE 2 -- GENERATOR

You ARE the GENERATOR. Produce nine namespace artifact sections, one per ROLE 1 row, in
table order. Writing a coverage summary here means you have become the SUMMARIZER, which
you are not yet. You generate. Nothing else.

---

**REAL-REQUIRED Rationale**

For namespaces where REAL-REQUIRED = YES, the following rationale content is pre-authored
here in the skill template body. Copy the matching text verbatim into the REAL-REQUIRED
block for that namespace. Do not substitute, paraphrase, or expand. The template is the
author; the GENERATOR copies:

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

Before each artifact body, extend the inertia skeleton:
> Without this signal, {topic}'s feature story would be missing: {ROLE 1 skeleton phrase}
> -- specifically, {one phrase naming the topic-specific instance of that gap}.

For each namespace:

  #### {namespace} -- {skill name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{skill-name}
  Topic:    {topic}
  Category: {from ROLE 1}
  Date:     {today}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {ROLE 1 skeleton phrase} -- specifically, {topic-specific instance}

  {3-5 sentence body; register matches Category; MUST-use vocabulary applied; DO NOT-use
  vocabulary avoided; body grounded in the extended inertia statement}

  [If REAL-REQUIRED = YES:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {verbatim text from the REAL-REQUIRED Rationale above for this namespace}

**ROLE 2 STOP -- Do not activate ROLE 3 -- SUMMARIZER until: (1) nine artifact sections
present; (2) each has a complete MOCK ARTIFACT header with all five fields (Skill, Topic,
Category, Date, Status: MOCK); (3) each has an extended inertia statement with both the
skeleton seed phrase and a topic-specific instance; (4) each body is 3-5 sentences,
vocabulary-compliant, register-matched, grounded in the inertia statement; (5) every
REAL-REQUIRED = YES namespace has a REAL-REQUIRED block with the pre-authored REAL-REQUIRED
rationale above copied verbatim.**

---

PHASE BOUNDARY: Generation complete.
ROLE 2 output verified. Proceed to ROLE 3.
ROLE 3 scope: coverage summary table only. No handoff.

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

PHASE BOUNDARY: Summarization complete.
ROLE 3 output verified. Proceed to ROLE 4.
ROLE 4 scope: handoff section only.

### ROLE 4 -- HANDOFF WRITER

You ARE the HANDOFF WRITER. Write only the handoff section.

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

---

---

## V-03 -- Multi-Stage Terminal Inertia (C-34 PASS + C-35 FAIL)

**axis (primary):** C-35 FAIL with C-34 PASS. The template preamble explicitly declares
"REAL-REQUIRED" as the canonical identifier (C-34 PASS). ROLE 2 is structured as three
artifact-collection stages by register category: Stage 1 (HIGH-STRUCTURE: flow, trace),
Stage 2 (EVIDENCE-HEAVY: prove, listen), Stage 3 (MIXED: scout, draft, review, program,
topic). The `-- specifically, {instance}` instruction appears once in the ROLE 2 opening
preamble, before Stage 1 -- not within each stage individually. The stage STOP gates do not
verify that the instruction fired within that stage; they check artifact completeness only.
A model completing Stage 1 without the `-- specifically` extension would pass the Stage 1
STOP gate. C-17 PASS (instruction present in the skill); C-35 FAIL (absent at Stage 1 and
Stage 2 boundaries; present only at the terminal/composite level of the ROLE 2 preamble).

**axis (secondary):** Collection-stage structure by register category. The three stages are
ordered by register: HIGH-STRUCTURE (tight contract language) -> EVIDENCE-HEAVY (study/data
framing) -> MIXED (discovery/signal language). This ordering tests whether the stage
structure itself holds when category-ordered rather than alphabetically ordered, and confirms
that per-stage vs. preamble-only distinction is the sole C-35 discriminant.

**hypothesis:** V-03 isolates the multi-stage template with terminal-only instruction -- the
C-35 FAIL case that cannot arise in single-stage templates. A model executing V-03 reads the
`-- specifically` instruction once in the ROLE 2 preamble, generates all artifacts, and
passes the ROLE 2 STOP gate. Whether it applied the instruction at each stage or only at the
terminal stage is not checked by the intermediate STOP gates. C-35 requires the instruction
to be present at each collection stage so that the binding occurs at the moment of
collection, not deferred. V-03 defers; V-03 fails C-35.

**predicted:** C-01 through C-34: PASS (C-34 PASS: preamble declares canonical authority).
C-35: FAIL (multi-stage template; `-- specifically` stated in ROLE 2 preamble only, not
within Stage 1, Stage 2, or Stage 3 individually). Score: 26/27.

**failure condition:** C-35 PASS if the stage body text incidentally re-states the inertia
extension instruction within each stage. Diagnostic: scan Stage 1 body text and Stage 2 body
text for any `-- specifically` instruction separate from the ROLE 2 opening preamble; their
absence confirms C-35 FAIL.

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

"REAL-REQUIRED" is the canonical identifier for the rationale section in this template.
The ROLE 2 STOP gate references this section by its canonical identifier. The GENERATOR
copies from the REAL-REQUIRED Rationale section by canonical name.

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
stages, ordered by register category. Do not write a coverage summary -- that is ROLE 3.
You generate. Nothing else.

Before each artifact body in this skill, extend the inertia skeleton:
> Without this signal, {topic}'s feature story would be missing: {ROLE 1 skeleton phrase}
> -- specifically, {one phrase naming the topic-specific instance of that gap}.

Apply this instruction to all namespaces across all three stages below.

---

**REAL-REQUIRED Rationale**

For namespaces where REAL-REQUIRED = YES, the following rationale content is pre-authored
here in the skill template body. Copy the matching text verbatim into the REAL-REQUIRED
block for that namespace. Do not substitute, paraphrase, or expand. The template is the
author; the GENERATOR copies:

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

**Stage 1 -- HIGH-STRUCTURE namespaces**

Generate artifact sections for the HIGH-STRUCTURE category (flow, trace) in ROLE 1 table order.

For each namespace:

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
complete; (2) each has a MOCK ARTIFACT header with all five fields; (3) each body is 3-5
sentences with HIGH-STRUCTURE vocabulary; (4) any compliance-tagged namespace has a
REAL-REQUIRED block with pre-authored rationale copied verbatim.**

---

**Stage 2 -- EVIDENCE-HEAVY namespaces**

Generate artifact sections for the EVIDENCE-HEAVY category (prove, listen) in ROLE 1 table order.

For each namespace:

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
are complete; (2) each has a MOCK ARTIFACT header with all five fields; (3) each body is 3-5
sentences with EVIDENCE-HEAVY vocabulary; (4) each has a REAL-REQUIRED block with
pre-authored rationale copied verbatim.**

---

**Stage 3 -- MIXED namespaces**

Generate artifact sections for the MIXED category (scout, draft, review, program, topic) in
ROLE 1 table order.

For each namespace:

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
  appropriate; vocabulary-compliant per ROLE 1 MUST use / DO NOT use}

  [If REAL-REQUIRED = YES (compliance-tagged scout):]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {verbatim text from the REAL-REQUIRED Rationale above for compliance-tagged}

**ROLE 2 STOP -- Do not activate ROLE 3 -- SUMMARIZER until: (1) nine artifact sections
present across all three stages; (2) each has a complete MOCK ARTIFACT header with all five
fields (Skill, Topic, Category, Date, Status: MOCK); (3) each has an extended inertia
statement with both the skeleton seed phrase and a topic-specific instance; (4) each body is
3-5 sentences, vocabulary-compliant, register-matched, grounded in the inertia statement;
(5) every REAL-REQUIRED = YES namespace has a REAL-REQUIRED block with the pre-authored
REAL-REQUIRED rationale above copied verbatim.**

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

## V-04 -- Multi-Stage Per-Stage Ceiling (C-34 PASS + C-35 PASS)

**axis (primary):** C-34 PASS + C-35 PASS. The preamble declares "REAL-REQUIRED" as the
canonical identifier (C-34 PASS). ROLE 2 has three artifact-collection stages (HIGH-STRUCTURE,
EVIDENCE-HEAVY, MIXED). Each stage individually contains the `-- specifically, {instance}`
instruction before the artifact format, and each stage's STOP gate verifies that the instruction
fired within that stage. C-35 PASS: the instruction is instantiated at Stage 1, Stage 2, and
Stage 3 independently -- not deferred to a shared preamble.

**axis (secondary):** Per-stage STOP gate enforcement. The stage STOP gates explicitly name
"a topic-specific instance via '-- specifically'" as a gate condition. This makes C-35
mechanically checkable at each stage boundary: a model that generates Stage 1 artifacts
without the `-- specifically` extension cannot pass the Stage 1 STOP gate. The per-stage
gate enforcement is the structural mechanism that distinguishes V-04 from V-03.

**hypothesis:** V-04 confirms the C-35 PASS ceiling for multi-stage templates. The
`-- specifically` instruction fires independently within each stage because each stage
contains its own copy of the instruction and its own gate verifying compliance. This prevents
a model from deferring the extension to a terminal pass; each collection event carries its
own binding. C-35 PASS is mechanically enforced, not merely instructed.

**predicted:** C-01 through C-35: PASS. Score: 27/27.

**failure condition:** C-35 FAIL if the per-stage instruction is accidentally omitted from
Stage 1 or Stage 2. Diagnostic: scan Stage 1 body and Stage 2 body for the `-- specifically`
instruction independent of the ROLE 2 preamble; presence in each stage body confirms C-35 PASS.

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

"REAL-REQUIRED" is the canonical identifier for the rationale section in this template.
The ROLE 2 STOP gate references this section by its canonical identifier. The GENERATOR
copies from the REAL-REQUIRED Rationale section by canonical name.

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
stages, ordered by register category. Do not write a coverage summary -- that is ROLE 3.
You generate. Nothing else.

---

**REAL-REQUIRED Rationale**

"REAL-REQUIRED" is the canonical identifier for this section. For namespaces where
REAL-REQUIRED = YES, the following rationale content is pre-authored here in the skill
template body. The GENERATOR copies verbatim from this REAL-REQUIRED Rationale section
into each applicable namespace block. Do not substitute, paraphrase, or expand:

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

For each artifact in this stage, extend the inertia skeleton before the artifact body:
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
inertia statement with the skeleton phrase and a topic-specific instance via '-- specifically';
(4) each body is 3-5 sentences with HIGH-STRUCTURE vocabulary; (5) any compliance-tagged
namespace has a REAL-REQUIRED block with pre-authored rationale copied verbatim.**

---

**Stage 2 -- EVIDENCE-HEAVY namespaces (prove, listen)**

For each artifact in this stage, extend the inertia skeleton before the artifact body:
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
extended inertia statement with the skeleton phrase and a topic-specific instance via
'-- specifically'; (4) each body is 3-5 sentences with EVIDENCE-HEAVY vocabulary; (5) each
has a REAL-REQUIRED block with the pre-authored REAL-REQUIRED rationale above copied verbatim.**

---

**Stage 3 -- MIXED namespaces (scout, draft, review, program, topic)**

For each artifact in this stage, extend the inertia skeleton before the artifact body:
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
statement with the skeleton seed phrase and a topic-specific instance per its collection
stage; (4) each body is 3-5 sentences, vocabulary-compliant, register-matched; (5) every
REAL-REQUIRED = YES namespace has a REAL-REQUIRED block with the pre-authored REAL-REQUIRED
rationale above copied verbatim.**

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

## V-05 -- Multi-Stage Per-Stage with Unified Preamble Declarations (C-34 PASS + C-35 PASS)

**axis (primary):** C-34 PASS + C-35 PASS, elevated. The preamble before ROLE 1 contains
two explicit structural authority declarations: Declaration A (canonical identifier authority
for "REAL-REQUIRED") and Declaration B (per-stage inertia extension authority). These
declarations make both C-34 and C-35 machine-readable from the preamble alone, without
requiring a reader to traverse ROLE 2's body. In V-04, the C-34 and C-35 requirements are
enforced within ROLE 2 (per-stage instructions + REAL-REQUIRED Rationale section header)
but are not unified in the preamble. In V-05, the preamble explicitly establishes both
structural rules as canonical before any role activates, and the ROLE 2 body implements
them by reference to the declared names.

**axis (secondary):** The ROLE 2 STOP gate for each stage refers back to the Declaration B
constraint by name ("per Declaration B"). This creates a closed reference loop: the preamble
declares Declaration B; the stage STOP gates enforce it by citing Declaration B. A reader
can verify C-35 compliance from the preamble (where the rule is stated) + the gate (where
it is enforced) without reading every stage instruction individually. This is structurally
parallel to the C-27/C-28 analogy and C-33/C-34 analogy: the declaration makes the
structural dependency explicit at the broadest scope.

**hypothesis:** V-05 is the 27/27 ceiling candidate with elevated preamble authority. The
multi-stage per-stage mechanism is identical to V-04 (confirming stability). The unified
preamble declarations test whether binding C-34 and C-35 together in a single pre-role
authority section improves mechanical readability -- a scorer can confirm both criteria
from the preamble alone without traversing stage bodies. V-05 is to C-35 what C-34 is to
C-33: the preamble-scope declaration that makes the existing gate-scope requirement
explicit at document scope.

**predicted:** C-01 through C-35: PASS. Score: 27/27.

**failure condition:** C-35 FAIL if per-stage STOP gates do not cite Declaration B or if
stage bodies omit the per-stage instruction. Diagnostic: verify that (a) the preamble
contains Declaration B, (b) each stage body contains the `-- specifically` instruction,
and (c) each stage STOP gate references the per-stage extension requirement.

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
stages, ordered by register category. Do not write a coverage summary -- that is ROLE 3.
You generate. Nothing else.

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
inertia statement with the skeleton phrase and a topic-specific instance via '-- specifically'
per Declaration B; (4) each body is 3-5 sentences with HIGH-STRUCTURE vocabulary; (5) any
compliance-tagged namespace has a REAL-REQUIRED block with pre-authored REAL-REQUIRED
rationale copied verbatim per Declaration A.**

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
extended inertia statement with the skeleton phrase and a topic-specific instance via
'-- specifically' per Declaration B; (4) each body is 3-5 sentences with EVIDENCE-HEAVY
vocabulary; (5) each has a REAL-REQUIRED block with the pre-authored REAL-REQUIRED
rationale above copied verbatim per Declaration A.**

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
statement with the skeleton seed phrase and a topic-specific instance per Declaration B --
verified at Stage 1, Stage 2, and Stage 3 individually; (4) each body is 3-5 sentences,
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

You ARE the HANDOFF WRITER. Write only the handoff section. Nothing else.

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

---

---

## Variation Summary

| Variation | C-33 | C-34 | C-35 | C-34 case | C-35 case | Secondary axis | Predicted |
|-----------|------|------|------|-----------|-----------|----------------|-----------|
| V-01 | PASS | FAIL | PASS (trivial) | Bottom -- no preamble declaration | Single-stage | Standard 4-role; no phase annotations | 26/27 |
| V-02 | PASS | FAIL | PASS (trivial) | Bottom -- passive preamble (locative, not declarative) | Single-stage | Phase-boundary annotations | 26/27 |
| V-03 | PASS | PASS | FAIL | Ceiling | Multi-stage + terminal-only `-- specifically` | Collection ordered HIGH-STRUCTURE > EVIDENCE-HEAVY > MIXED; preamble declares canonical | 26/27 |
| V-04 | PASS | PASS | PASS | Ceiling | Multi-stage + per-stage | Per-stage STOP gates enforce `-- specifically`; preamble declares canonical | 27/27 |
| V-05 | PASS | PASS | PASS | Ceiling | Multi-stage + per-stage | Unified Declaration A + B in preamble; stage gates cite Declaration B | 27/27 |

**C-34 discrimination:** V-01/V-02 (Bottom, no canonical-authority declaration) vs V-03/V-04/V-05 (Ceiling, preamble declares canonical authority).
**C-35 discrimination:** V-01/V-02 (trivial single-stage) vs V-03 (multi-stage FAIL: terminal-only) vs V-04/V-05 (multi-stage PASS: per-stage).
**Three distinct 26/27 failure paths:** V-01 (C-34 FAIL only), V-02 (C-34 FAIL only, passive-preamble register), V-03 (C-35 FAIL only, multi-stage terminal).

Gate-text audit (C-34 discriminant -- preamble declaration):
- V-01: No preamble declaration. Section header "REAL-REQUIRED Rationale" exists in ROLE 2. Gate uses "REAL-REQUIRED" (C-33 PASS). No document-scope declaration (C-34 FAIL).
- V-02: Preamble says "The REAL-REQUIRED Rationale section in ROLE 2 below contains pre-authored rationale...copy the matching entry from that section verbatim." Locative/procedural. Not a canonical-authority declaration (C-34 FAIL).
- V-03: Preamble says '"REAL-REQUIRED" is the canonical identifier for the rationale section in this template.' Explicit declarative form (C-34 PASS).
- V-04: Same preamble as V-03. C-34 PASS.
- V-05: Preamble contains Declaration A: '"REAL-REQUIRED" is the canonical identifier for the rationale section in this template...per Declaration A.' Explicit declarative form with named authority (C-34 PASS).

Gate-text audit (C-35 discriminant -- per-stage vs terminal `-- specifically`):
- V-01: Single ROLE 2 instruction block. One stage. C-35 = C-17 (trivially PASS).
- V-02: Single ROLE 2 instruction block. One stage. C-35 = C-17 (trivially PASS).
- V-03: ROLE 2 preamble says "Apply this instruction to all namespaces across all three stages." Instruction stated once; stage bodies do not individually re-state it; stage STOP gates do not check for it (C-35 FAIL).
- V-04: Each stage body individually says "For each artifact in this stage, extend the inertia skeleton... -- specifically, ..."; each stage STOP gate checks for it (C-35 PASS).
- V-05: Each stage body says "Per Declaration B: extend the inertia skeleton...-- specifically, ..."; each stage STOP gate checks for it citing "per Declaration B" (C-35 PASS).
