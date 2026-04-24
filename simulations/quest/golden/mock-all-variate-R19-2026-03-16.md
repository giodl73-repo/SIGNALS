---
skill: quest-variate
skill_target: mock-all
date: 2026-03-16
round: 19
rubric_version: v19
status: VARIATE
---

# mock-all Variate -- Round 19

**Date:** 2026-03-16
**Skill:** mock-all
**Rubric:** v19 (Essential 5, Recommended 3, Aspirational C-09 through C-38 = 30; formula: (E/5*60) + (R/3*30) + (A/30*10))
**Round:** R19 -- one new criterion (C-38); R18 V-05 is the reference ceiling (retroactively 30/30 under v19)

---

## What R18 Left Open

v19 adds C-38 extracted from the R18 discrimination inversion:

| Criterion | Source | What it tests |
|-----------|--------|---------------|
| C-38 | R18 actuals: V-01 (26/29) > V-02 (25/29), inverting the prediction V-02 (23/29) > V-01 (16/29). The inversion is driven by V-02's ROLE 2 preamble containing a single cross-stage inertia instruction ("Apply this instruction to all namespaces across all three stages below") while V-01's single-stage structure has no multi-stage delegation failure. C-35 alone could not capture this because C-35 tests whether gates enforce per-stage firing -- not whether the instruction architecturally lives at the stage level. | The template must not delegate stage-local compliance to a cross-stage statement. A multi-stage template satisfies C-38 only when the inertia extension instruction lives independently within each stage body, not in the ROLE 2 preamble as a shared instruction covering all stages. C-38 is an architectural criterion: it tests instruction location, not gate enforcement. A template can pass C-35 (gates enforce per-stage) while failing C-38 (instruction architecturally lives in ROLE 2 preamble). C-38 is a strict refinement: C-38 PASS implies the instruction fires per-stage; C-35 PASS does not imply C-38 PASS. |

The denominator rises from 29 to 30. The scoring formula changes from aspirational-only to three-tier:

```
composite = (essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/30 × 10)
```

Under v19, each Recommended criterion is worth 10 composite points (30 / 3). Each Aspirational criterion is worth 0.33 composite points (10 / 30). This makes R-03 ("each stage STOP gate references a classification-derived condition") the highest-value single criterion in R19 -- a template that fails R-03 loses 10 composite points, while failing C-38 alone loses only 0.33.

---

## Round 19 Primary Hypothesis

Three hypotheses for R19:

**H1 (V-01):** Cross-stage delegation co-occurs with R-03 FAIL. A template that puts the inertia instruction in the ROLE 2 preamble and writes minimal stage STOP gates (artifact count only) will fail R-03. Under v19, this is the bottom of the ladder -- not because C-38 alone scores low but because R-03 FAIL costs 10 composite points.

**H2 (V-02):** C-38 is an independent architectural criterion. A template can fail C-38 (instruction in ROLE 2 preamble, cross-stage) while passing C-35 (stage gates enforce per-stage inertia) and R-03 (stage gates reference classification conditions). The R-03 fix from V-01 to V-02 is worth 10 composite points; the C-38 fix from V-02 to V-03 is worth 0.33 composite points. The v19 formula reveals C-38's relative weight.

**H3 (V-03 through V-05):** The C-38 PASS baseline (V-03), the labeled-declaration intermediate (V-04), and the gate-citation ceiling (V-05) form the same single-axis chain as R18 V-03 through V-05. C-38 PASS is already present in R18 V-03 (per-stage instruction inside each stage body). R19 V-03 through V-05 are R18 V-03 through V-05 with explicit C-38 annotation under the new formula.

---

## Axis-Assignment Plan

| Variation | C-34 | C-35 | C-36 | C-37 | C-38 | R-03 | Primary axis | Predicted composite |
|-----------|------|------|------|------|------|------|--------------|---------------------|
| V-01 | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | Cross-stage delegation; minimal stage gates | 88.0 |
| V-02 | PASS | PASS | FAIL | FAIL | FAIL | PASS | Cross-stage delegation; per-stage gate enforcement; R-03 fixed | 99.0 |
| V-03 | PASS | PASS | FAIL | FAIL | PASS | PASS | Per-stage instruction; canonical declaration; no labels | 99.33 |
| V-04 | PASS | PASS | PASS | FAIL | PASS | PASS | Per-stage; labeled declarations; inline gate restatement | 99.67 |
| V-05 | PASS | PASS | PASS | PASS | PASS | PASS | Per-stage; labeled declarations; gate label citations | 100.0 |

Single-axis chain:
- V-02 → V-03: C-38 axis only (instruction moves from ROLE 2 preamble into each stage body)
- V-03 → V-04: C-36 axis only (add Declaration A / Declaration B labels to template preamble)
- V-04 → V-05: C-37 axis only (gate text changes from inline restatement to label citation)

V-01 → V-02 is a compound step establishing the floor: add canonical REAL-REQUIRED declaration (C-34), add per-stage gate enforcement (C-35), add classification-derived conditions to stage gates (R-03). C-38 remains FAIL in both V-01 and V-02 -- the inertia instruction stays in the ROLE 2 preamble.

Score derivation under v19 formula:
- V-01: (5/5 × 60) + (2/3 × 30) + (24/30 × 10) = 60 + 20 + 8.0 = **88.0**
- V-02: (5/5 × 60) + (3/3 × 30) + (27/30 × 10) = 60 + 30 + 9.0 = **99.0**
- V-03: (5/5 × 60) + (3/3 × 30) + (28/30 × 10) = 60 + 30 + 9.33 = **99.33**
- V-04: (5/5 × 60) + (3/3 × 30) + (29/30 × 10) = 60 + 30 + 9.67 = **99.67**
- V-05: (5/5 × 60) + (3/3 × 30) + (30/30 × 10) = 60 + 30 + 10.0 = **100.0**

---

## V-01 -- Cross-Stage Delegation, Minimal Stage Gates (C-38 FAIL + R-03 FAIL, 88.0)

**axis (primary):** Cross-stage inertia delegation with minimal stage STOP gates. The ROLE 2 body opens with a single inertia instruction before Stage 1 -- architecturally cross-stage (C-38 FAIL, C-35 FAIL). Stage bodies contain no independent inertia instructions. Stage STOP gates check artifact count and section presence only; they do not reference classification-table-derived conditions (vocabulary register, compliance flags, tier conditions). R-03 FAIL: no stage gate contains a classification-derived condition.

**axis (secondary):** No structural authority declarations in template preamble. The preamble contains role-identity and ontological framing only. No sentence of the form `"REAL-REQUIRED" is the canonical identifier` (C-34 FAIL). No Declaration A, no Declaration B (C-36 FAIL). Stage gates are bare: "Do not proceed until Stage N artifact sections are present and complete."

**hypothesis:** V-01 demonstrates that cross-stage delegation and minimal gates are coupled failure modes. A template author who writes the inertia instruction once in ROLE 2 and does not elaborate stage gates will fail both C-38 and R-03. Under v19, R-03 FAIL costs 10 composite points (much more than C-38's 0.33). The v19 formula reframes the diagnosis: the main scoring failure in V-01 is not architectural (C-38) but gate completeness (R-03).

**predicted:** C-34: FAIL. C-35: FAIL. C-36: FAIL. C-37: FAIL. C-38: FAIL. R-03: FAIL. Essential: 5/5. Recommended: 2/3. Aspirational: 24/30. Composite: 88.0.

**failure condition for C-38:** C-38 PASS if any stage body (Stage 1, Stage 2, Stage 3) contains an independent inertia instruction rather than relying on the ROLE 2 preamble instruction. Diagnostic: scan Stage 1 body, Stage 2 body, Stage 3 body for any form of "For each artifact in this stage, extend the inertia skeleton" or equivalent per-stage instruction; absence in all three stages confirms C-38 FAIL.

**failure condition for R-03:** R-03 PASS if any stage STOP gate references a classification-derived condition. Diagnostic: scan all stage gates for "HIGH-STRUCTURE vocabulary," "EVIDENCE-HEAVY vocabulary," "MIXED vocabulary," "compliance-tagged," "REAL-REQUIRED block," or any tier condition; absence confirms R-03 FAIL.

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

You ARE the GENERATOR. Produce nine namespace artifact sections across three collection
stages, ordered by register category. Do not write a coverage summary. You generate.
Nothing else.

Before generating each artifact in this skill, extend the inertia skeleton:
> Without this signal, {topic}'s feature story would be missing: {ROLE 1 skeleton phrase}
> -- specifically, {one phrase naming the topic-specific instance of that gap}.

Apply this instruction to all artifacts across Stage 1, Stage 2, and Stage 3 below.

---

**REAL-REQUIRED Rationale**

For namespaces where REAL-REQUIRED = YES, the following rationale content is pre-authored
here in the skill template body. Copy the matching text verbatim into the REAL-REQUIRED
block for that namespace. Do not substitute, paraphrase, or expand:

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

**STAGE 1 STOP -- Do not proceed to Stage 2 until Stage 1 artifact sections are present
and complete.**

---

**Stage 2 -- EVIDENCE-HEAVY namespaces (prove, listen)**

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

**STAGE 2 STOP -- Do not proceed to Stage 3 until Stage 2 artifact sections are present
and complete.**

---

**Stage 3 -- MIXED namespaces (scout, draft, review, program, topic)**

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
statement with both the skeleton seed phrase and a topic-specific instance; (4) each body is
3-5 sentences, vocabulary-compliant, register-matched; (5) every REAL-REQUIRED = YES
namespace has a REAL-REQUIRED block with pre-authored rationale above copied verbatim.**

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

## V-02 -- Cross-Stage Delegation, Per-Stage Gate Enforcement (C-38 FAIL, C-35 PASS, R-03 PASS, 99.0)

**axis (primary):** Cross-stage inertia delegation (C-38 FAIL) with per-stage gate enforcement (C-35 PASS) and classification-derived gate conditions (R-03 PASS). The ROLE 2 body contains the inertia instruction before Stage 1 -- architecturally cross-stage (C-38 FAIL). Stage bodies do not contain independent inertia instructions; they generate artifacts using the preamble-supplied instruction. However, stage STOP gates DO enforce per-stage inertia independently: each gate explicitly checks that "every artifact in this stage has an extended inertia statement with the skeleton phrase and a topic-specific instance." Stage gates also reference classification-derived conditions: vocabulary register match (HIGH-STRUCTURE / EVIDENCE-HEAVY / MIXED), compliance-tagged namespace check. R-03 PASS.

**axis (secondary):** The template preamble contains a canonical REAL-REQUIRED declaration (C-34 PASS): `"REAL-REQUIRED" is the canonical identifier for the rationale section in this template.` No Declaration A or Declaration B labels assigned (C-36 FAIL). Gate text does not cite declaration labels (C-37 FAIL, trivially).

**hypothesis:** V-02 tests whether C-38 is genuinely independent of C-35 and R-03. The template behaves correctly (gates enforce per-stage inertia, gates reference classification conditions) but the inertia instruction architecturally lives in the ROLE 2 preamble. C-38 should fail on this architecture regardless of gate quality. Under v19, the composite jump from V-01 (88.0) to V-02 (99.0) is entirely R-03 (10 points). The jump from V-02 (99.0) to V-03 (99.33) is C-38 (0.33 points). The v19 formula confirms: C-38 is a correctness criterion, not a high-value scoring criterion.

**predicted:** C-34: PASS. C-35: PASS (gate enforcement per stage). C-36: FAIL. C-37: FAIL. C-38: FAIL (instruction in ROLE 2 preamble, architecturally cross-stage). R-03: PASS. Essential: 5/5. Recommended: 3/3. Aspirational: 27/30. Composite: 99.0.

**failure condition:** C-38 PASS if the ROLE 2 preamble inertia instruction is removed AND each stage body gains an independent instruction. Diagnostic: scan ROLE 2 preamble for "Apply this instruction to all artifacts across Stage 1, Stage 2, and Stage 3" or equivalent; presence confirms C-38 FAIL regardless of gate enforcement quality.

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
stages, ordered by register category. Do not write a coverage summary. You generate.
Nothing else.

For each artifact in this skill, extend the inertia skeleton before the artifact body:
> Without this signal, {topic}'s feature story would be missing: {ROLE 1 skeleton phrase}
> -- specifically, {one phrase naming the topic-specific instance of that gap}.

This inertia extension applies to every artifact across Stage 1, Stage 2, and Stage 3.

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
complete; (2) each has a MOCK ARTIFACT header with all five fields (Skill, Topic, Category,
Date, Status: MOCK); (3) each has an extended inertia statement with the skeleton phrase and
a topic-specific instance; (4) each body is 3-5 sentences with HIGH-STRUCTURE vocabulary
(specification language; state/contract/boundary vocabulary); (5) any compliance-tagged
namespace has a REAL-REQUIRED block with pre-authored rationale copied verbatim.**

---

**Stage 2 -- EVIDENCE-HEAVY namespaces (prove, listen)**

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
extended inertia statement with the skeleton phrase and a topic-specific instance; (4) each
body is 3-5 sentences with EVIDENCE-HEAVY vocabulary (study/data framing; "N of M" form;
hypothesis-and-result language); (5) each has a REAL-REQUIRED block with pre-authored
rationale copied verbatim.**

---

**Stage 3 -- MIXED namespaces (scout, draft, review, program, topic)**

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
statement with the skeleton seed phrase and a topic-specific instance -- confirmed for Stage 1,
Stage 2, and Stage 3 individually; (4) each body is 3-5 sentences, vocabulary-compliant per
ROLE 1 category, register-matched; (5) every REAL-REQUIRED = YES namespace has a
REAL-REQUIRED block with the pre-authored REAL-REQUIRED rationale above copied verbatim.**

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

## V-03 -- Per-Stage Instruction, Canonical Declaration, No Labels (C-38 PASS + C-36 FAIL, 99.33)

**axis (primary):** C-38 PASS + C-35 PASS + C-34 PASS + C-36 FAIL + C-37 FAIL. The template
preamble explicitly declares "REAL-REQUIRED" as the canonical identifier (C-34 PASS). It also
declares that the inertia extension fires independently within Stage 1, Stage 2, and Stage 3
(not as a shared preamble instruction). Stage bodies each contain their own independent inertia
instruction (C-38 PASS, C-35 PASS). Stage STOP gates enforce per-stage inertia and reference
classification-derived conditions (R-03 PASS). No Declaration A or Declaration B labels
assigned -- the declarations exist as unlabeled declarative sentences in the preamble (C-36 FAIL).
Stage STOP gates restate compliance requirements inline (C-37 FAIL, trivially).

**axis (secondary):** This is the C-38 PASS baseline. R18 V-03 was already C-38 PASS; R19 V-03
makes this explicit. The only criteria failing are C-36 and C-37 (the label-and-citation chain
from R18). The C-38 axis (V-02 → V-03) is isolated from the C-36 axis (V-03 → V-04).

**hypothesis:** V-03 confirms that moving the inertia instruction from the ROLE 2 preamble into
each stage body (one line change per stage) is the C-38 fix. The fix costs nothing structurally.
The composite gain is 0.33 points (one aspirational criterion). V-03 is structurally equivalent
to R18 V-03 retroactively annotated as C-38 PASS.

**predicted:** C-34: PASS. C-35: PASS. C-36: FAIL (no labeled declarations). C-37: FAIL
(trivially). C-38: PASS (per-stage instruction in each stage body). R-03: PASS. Essential: 5/5.
Recommended: 3/3. Aspirational: 28/30. Composite: 99.33.

**failure condition:** C-38 FAIL if the per-stage inertia instruction is removed from any stage
body. Diagnostic: confirm Stage 1 body, Stage 2 body, Stage 3 body each independently contain
the instruction; if absent from any stage, C-38 FAIL for that stage.

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

The inertia extension `-- specifically, {instance}` is a required instruction at every
artifact-collection stage. It fires independently within Stage 1, Stage 2, and Stage 3.
Per-stage STOP gates enforce this requirement at each stage boundary.

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
namespace has a REAL-REQUIRED block with pre-authored REAL-REQUIRED rationale copied
verbatim.**

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
has a REAL-REQUIRED block with the pre-authored REAL-REQUIRED rationale above copied
verbatim.**

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
statement with the skeleton seed phrase and a topic-specific instance -- verified at Stage 1,
Stage 2, and Stage 3 individually; (4) each body is 3-5 sentences, vocabulary-compliant,
register-matched; (5) every REAL-REQUIRED = YES namespace has a REAL-REQUIRED block with
the pre-authored REAL-REQUIRED rationale above copied verbatim.**

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

## V-04 -- Labeled Declarations, Per-Stage, Inline Gate Restatement (C-38 PASS + C-36 PASS + C-37 FAIL, 99.67)

**axis (primary):** C-36 PASS + C-37 FAIL + C-38 PASS. The template preamble assigns explicit
reference labels to both structural authority declarations (C-36 PASS): "Declaration A" names
the canonical REAL-REQUIRED identifier authority; "Declaration B" names the per-stage inertia
extension authority. Stage bodies cite "Per Declaration B: extend the inertia skeleton for each
artifact in this stage" -- the label is used as an instruction prefix and the instruction lives
within each stage body (C-38 PASS). Stage STOP gates, however, restate compliance requirements
inline without citing labels (C-37 FAIL): "each has an extended inertia statement with the
skeleton phrase and a topic-specific instance" (not "per Declaration B").

**axis (secondary):** The preamble in V-04 is structurally identical to V-05. Both contain
Declaration A and Declaration B. Stage body instructions in V-04 and V-05 are identical: both
cite "Per Declaration B" before the inertia skeleton. The sole difference between V-04 and V-05
is gate text: V-04 gates restate inline; V-05 gates cite by label. C-37 is the single axis.
C-38 PASS is confirmed for V-04: "Per Declaration B" in Stage 1 body means the instruction
fires within Stage 1 (stage-local), not from a cross-stage preamble.

**hypothesis:** V-04 instantiates C-36 PASS + C-37 FAIL + C-38 PASS. The R18 configuration
(C-36 PASS + C-37 FAIL) is preserved; C-38 is now PASS because Declaration B is in the
template preamble and stage bodies execute it per-stage. Under v19, V-04 scores 29/30
aspirational (0.33 points below ceiling). The C-37 fix (gate citation) is the final step.

**predicted:** C-34: PASS. C-35: PASS. C-36: PASS (Declaration A, Declaration B in preamble).
C-37: FAIL (gates restate inline rather than citing "per Declaration A" / "per Declaration B").
C-38: PASS (stage bodies independently contain per-stage instruction). R-03: PASS. Essential:
5/5. Recommended: 3/3. Aspirational: 29/30. Composite: 99.67.

**failure condition:** C-37 PASS if any stage STOP gate incidentally includes "per Declaration B"
or "per Declaration A". Diagnostic: scan Stage 1 STOP gate, Stage 2 STOP gate, and ROLE 2 STOP
gate for any text of the form "per Declaration A" or "per Declaration B"; absence in all gates
confirms C-37 FAIL.

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
inertia statement with the skeleton phrase and a topic-specific instance; (4) each body is
3-5 sentences with HIGH-STRUCTURE vocabulary; (5) any compliance-tagged namespace has a
REAL-REQUIRED block with pre-authored rationale copied verbatim.**

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
extended inertia statement with the skeleton phrase and a topic-specific instance; (4) each
body is 3-5 sentences with EVIDENCE-HEAVY vocabulary; (5) each has a REAL-REQUIRED block
with pre-authored rationale copied verbatim.**

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
Stage 2, and Stage 3 individually; (4) each body is 3-5 sentences, vocabulary-compliant,
register-matched; (5) every REAL-REQUIRED = YES namespace has a REAL-REQUIRED block with
the pre-authored REAL-REQUIRED rationale above copied verbatim.**

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

## V-05 -- Full Ceiling: Per-Stage + Labeled Declarations + Gate Citations (30/30, 100.0)

**axis (primary):** C-36 PASS + C-37 PASS + C-38 PASS. The structural mechanism is identical
to V-04 in the preamble and stage body instructions. The sole change is the stage STOP gate
text: Stage 1 STOP gate says "per Declaration B" for the inertia requirement and "per
Declaration A" for the REAL-REQUIRED block requirement. Stage 2 STOP gate says "per
Declaration B" and "per Declaration A". The ROLE 2 STOP gate says "per Declaration B --
verified at Stage 1, Stage 2, and Stage 3 individually" and "per Declaration A". This closes
the verification loop: a scorer confirms C-35 compliance by reading Declaration B (preamble)
plus Stage 1 gate ("per Declaration B") alone. A scorer confirms C-34 compliance by reading
Declaration A plus gate clause ("per Declaration A") alone.

**axis (secondary):** V-05 demonstrates that C-37 is a formatting property of gate text, not
a structural property of enforcement. The enforcement is identical between V-04 and V-05.
C-37 concerns whether the gate references the preamble label -- it is a readability and
auditability criterion, not a completeness criterion. V-04 is fully correct in what it
enforces; V-05 is verifiably correct from a shorter reading path. C-38 PASS is confirmed:
"Per Declaration B" in each stage body is a stage-local instruction that references a
template-level authority -- not a delegation to a cross-stage statement in the ROLE 2 body.

**hypothesis:** V-05 is the 30/30 ceiling under v19. All 30 aspirational criteria pass. The
closed reference loop for Declaration A (C-34 mechanism + C-36 label + C-37 gate citation)
and Declaration B (C-35 mechanism + C-38 architecture + C-36 label + C-37 gate citation) is
complete. R18 V-05 retroactively scored 30/30 under v19 because its per-stage stage-body
instructions already satisfied C-38.

**predicted:** C-09 through C-38: PASS. Essential: 5/5. Recommended: 3/3. Aspirational:
30/30. Composite: 100.0.

**failure condition:** C-37 FAIL if any stage STOP gate omits the "per Declaration A" /
"per Declaration B" citation. Diagnostic: verify Stage 1 STOP gate, Stage 2 STOP gate, and
ROLE 2 STOP gate each contain "per Declaration B" for the inertia requirement and "per
Declaration A" for the REAL-REQUIRED block requirement; absence in any gate confirms C-37
FAIL for that gate.

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
has a REAL-REQUIRED block with the pre-authored REAL-REQUIRED rationale above copied
verbatim per Declaration A.**

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

| Variation | C-34 | C-35 | C-36 | C-37 | C-38 | R-03 | Primary axis | Predicted composite |
|-----------|------|------|------|------|------|------|--------------|---------------------|
| V-01 | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | Cross-stage delegation; minimal stage gates (artifact count only) | 88.0 |
| V-02 | PASS | PASS | FAIL | FAIL | FAIL | PASS | Cross-stage delegation; per-stage gate enforcement; R-03 fixed | 99.0 |
| V-03 | PASS | PASS | FAIL | FAIL | PASS | PASS | Per-stage instruction in each stage body; canonical declaration; no labels | 99.33 |
| V-04 | PASS | PASS | PASS | FAIL | PASS | PASS | Per-stage; Declaration A + B labeled; stage bodies cite labels; gates restate inline | 99.67 |
| V-05 | PASS | PASS | PASS | PASS | PASS | PASS | Per-stage; labeled declarations; gates cite "per Declaration A" / "per Declaration B" | 100.0 |

Single-axis chain:
- V-02 vs V-03: C-38 axis only -- move inertia instruction from ROLE 2 preamble into each stage body
- V-03 vs V-04: C-36 axis only -- add "Declaration A" / "Declaration B" labels to template preamble
- V-04 vs V-05: C-37 axis only -- gate text changes from inline restatement to label citation

R19 introduces C-38 as the architectural companion to C-35. C-35 (behavioral: does inertia fire
per stage?) and C-38 (architectural: does inertia live per stage?) are independent: V-02
demonstrates C-35 PASS + C-38 FAIL. V-03 demonstrates the C-38 fix is a pure architectural
change -- move the instruction from the ROLE 2 preamble body into each stage body.

The v19 formula reweights discrimination: R-03 (10 composite points) >> C-38 (0.33 composite
points). The jump V-01 → V-02 (88.0 → 99.0) is the most discriminating step in the R19 ladder
and is entirely driven by R-03, not C-38.

---

## Discrimination Table Under v19

| Variation | C-38 | R-03 | Aspirational | Essential | Recommended | Composite |
|-----------|------|------|-------------|-----------|-------------|-----------|
| V-01 | FAIL | FAIL | 24/30 | 5/5 | 2/3 | 88.0 |
| V-02 | FAIL | PASS | 27/30 | 5/5 | 3/3 | 99.0 |
| V-03 | PASS | PASS | 28/30 | 5/5 | 3/3 | 99.33 |
| V-04 | PASS | PASS | 29/30 | 5/5 | 3/3 | 99.67 |
| V-05 | PASS | PASS | 30/30 | 5/5 | 3/3 | 100.0 |

V-01 → V-02 discrimination: 11.0 points (R-03 fix = 10 pts; C-34+C-35 fix = ~0.67 pts)
V-02 → V-03 discrimination: 0.33 points (C-38 fix only)
V-03 → V-04 discrimination: 0.33 points (C-36 fix only)
V-04 → V-05 discrimination: 0.33 points (C-37 fix only)

The v19 formula collapses V-02 through V-05 into a 1.0-point band (99.0 to 100.0). The
high-value discrimination is entirely below that band: R-03 FAIL produces the only double-digit
composite gap in the ladder.

Next: /mock:review mock-all simulations/quest/golden/mock-all-variate-R19-2026-03-16.md
