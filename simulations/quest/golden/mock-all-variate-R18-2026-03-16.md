---
skill: quest-variate
skill_target: mock-all
date: 2026-03-16
round: 18
rubric_version: v18
status: VARIATE
---

# mock-all Variate -- Round 18

**Date:** 2026-03-16
**Skill:** mock-all
**Rubric:** v18 (C-01 through C-37; aspirational denominator = 29)
**Round:** R18 -- two new criteria (C-36, C-37); R17 V-05 is the reference ceiling at 29/29

---

## What R17 Left Open

v18 adds two new aspirational criteria from the gate-citation sub-chain:

| Criterion | Source | What it tests |
|-----------|--------|---------------|
| C-36 | R17 V-05 -- preamble assigned "Declaration A" and "Declaration B" labels to structural authority statements; V-01--V-04 R17 all fail: none of them assign explicit reference labels to their preamble declarations | The template preamble assigns explicit reference labels (e.g., "Declaration A", "Declaration B") to its structural authority declarations, enabling stage STOP gates to cite each by name. C-36 is a strict refinement of C-34 and C-35: C-36 pass implies both C-34 pass and C-35 pass. Neither C-34 pass nor C-35 pass implies C-36 pass. |
| C-37 | R17 V-05 -- stage STOP gates said "per Declaration B" and "per Declaration A" rather than restating rules inline; V-01--V-04 R17 all fail: gates restate the compliance requirements inline without citing the preamble label | The stage-level STOP gates cite the preamble's structural authority declarations by reference label (e.g., "per Declaration A", "per Declaration B"), forming a closed verification loop checkable from preamble + gate alone. C-37 is a strict refinement of C-36: C-37 pass requires labeled declarations (C-36 pass) plus gate citation of those labels. |

The denominator rises from 27 to 29. R17 V-05 retroactively scores C-36 PASS (Declaration A
and Declaration B labeled in preamble) and C-37 PASS (stage gates cite "per Declaration A"
and "per Declaration B"). R17 V-04 scores C-36 FAIL (rules stated without labels) and
C-37 FAIL (gates restate inline).

---

## Round 18 Primary Hypothesis

Instantiate the C-36 PASS + C-37 FAIL intermediate case -- the one case absent from R17:

| Case | C-36 | C-37 | Mechanism |
|------|------|------|-----------|
| Bottom (V-03) | FAIL | FAIL | Multi-stage; per-stage inertia; canonical declaration; no labels; gates restate inline |
| Intermediate (V-04) | PASS | FAIL | Multi-stage; labeled declarations (Declaration A, Declaration B) in preamble; stage bodies cite "Per Declaration B"; stage STOP gates restate compliance requirement inline -- not by label |
| Ceiling (V-05) | PASS | PASS | Multi-stage; labeled declarations in preamble; stage bodies cite "Per Declaration B"; stage STOP gates cite "per Declaration A" and "per Declaration B" |

The discriminating axis between V-04 and V-05 is entirely in the gate text. Stage body
instructions in both cases say "Per Declaration B: extend the inertia skeleton...". The V-04
stage STOP gate says "each has an extended inertia statement with the skeleton phrase and a
topic-specific instance" (inline). The V-05 stage STOP gate says the same clause ending
"per Declaration B" (label citation). The preamble content is identical between V-04 and V-05.

C-37 FAIL is possible even when Declaration A and Declaration B labels are present in the
preamble. The label exists; the gate simply does not reference it. A scorer verifying
compliance must traverse the stage instruction body to confirm the requirement holds
rather than confirming from preamble-declaration + gate-citation alone.

---

## Axis-Assignment Plan

| Variation | C-34 | C-35 | C-36 | C-37 | Primary axis | Predicted |
|-----------|------|------|------|------|-------------|-----------|
| V-01 | FAIL | PASS (trivial) | FAIL | FAIL | Single-stage; no preamble declaration; no labels | 16/29 |
| V-02 | FAIL | FAIL | FAIL | FAIL | Multi-stage; procedural preamble; terminal inertia only | 23/29 |
| V-03 | PASS | PASS | FAIL | FAIL | Multi-stage; canonical declaration; per-stage inertia; no labels | 27/29 |
| V-04 | PASS | PASS | PASS | FAIL | Multi-stage; labeled declarations; stage bodies cite labels; gates restate inline | 28/29 |
| V-05 | PASS | PASS | PASS | PASS | Multi-stage; labeled declarations; gates cite by label | 29/29 |

Single-axis chain:
- V-03 --> V-04: C-36 axis (add labeled declarations; no other change to compliance)
- V-04 --> V-05: C-37 axis (gate citation vs inline restatement; no other change)

V-01 and V-02 establish the bottom of the discrimination ladder. V-01/V-02 fail multiple
aspirational criteria below C-34 that are not the focus of this round.

---

## V-01 -- No-Preamble Single-Stage (C-36 FAIL + C-37 FAIL, 16/29)

**axis (primary):** Single-stage ROLE 2; no preamble declaration; no labeled structural
authority. The ROLE 2 section is labeled "REAL-REQUIRED Rationale" and the ROLE 2 STOP
gate names it by that label (C-33 PASS), but the template preamble contains no statement
asserting "REAL-REQUIRED" as the canonical authoritative identifier (C-34 FAIL). The
preamble is purely role-framing prose. No Declaration A, no Declaration B (C-36 FAIL).
Single-stage ROLE 2 means C-35 is trivially PASS (one stage).

**axis (secondary):** Standard 4-role structure with no phase-boundary annotations and no
sub-stage ordering. ROLE 2 generates all nine namespaces in a single sequential pass.
The inertia extension appears once in the ROLE 2 opening before all artifacts.

**hypothesis:** V-01 isolates the no-preamble, no-label case as the bottom of the ladder.
A reader of the template preamble receives only role identity framing -- no structural
authority declarations of any kind. C-34 FAIL, C-36 FAIL, C-37 FAIL. Many lower aspirational
criteria also fail: the ROLE 2 STOP gate does not name the REAL-REQUIRED section by
canonical identifier in the provenance reference clause; the seed-phrase column binding
instruction is present but the gate does not enforce verbatim compliance by name.

**predicted:** C-34: FAIL. C-35: PASS (trivial). C-36: FAIL. C-37: FAIL. Score: ~16/29.

**failure condition:** C-34 PASS if the role-framing preamble incidentally contains any
declarative sentence asserting "REAL-REQUIRED" as the canonical identifier. Diagnostic:
scan preamble for any form of '"REAL-REQUIRED" is the canonical/authoritative identifier';
absence confirms C-34 FAIL.

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
REAL-REQUIRED = YES namespace has a REAL-REQUIRED block with pre-authored rationale
above copied verbatim.**

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

## V-02 -- Multi-Stage Terminal Inertia, Procedural Preamble (C-36 FAIL + C-37 FAIL, 23/29)

**axis (primary):** Multi-stage ROLE 2 with terminal inertia instruction (C-35 FAIL) and
procedural preamble reference to REAL-REQUIRED (C-34 FAIL). The preamble says: "The
REAL-REQUIRED Rationale section in ROLE 2 contains pre-authored rationale for
REAL-REQUIRED = YES namespaces. When generating a REAL-REQUIRED block, copy the matching
entry from that section verbatim." This is a locative/procedural description (where to look
and what to do) -- not a canonical-authority declaration (this IS the canonical name). C-34
FAIL. The inertia extension `-- specifically, {instance}` appears once in the ROLE 2 opening
instruction before Stage 1, not within each stage body. A model can complete Stage 1
artifacts and pass the Stage 1 STOP gate without having applied the per-artifact extension.
C-35 FAIL. No labeled declarations (C-36 FAIL).

**axis (secondary):** Three-stage ROLE 2 ordered by register category: Stage 1
(HIGH-STRUCTURE: flow, trace), Stage 2 (EVIDENCE-HEAVY: prove, listen), Stage 3 (MIXED:
scout, draft, review, program, topic). Stage STOP gates verify artifact completeness but
do not check for the inertia extension. This confirms that stage structure alone does not
produce C-35 PASS -- per-stage gate enforcement is required.

**hypothesis:** V-02 isolates the multi-stage template with procedural preamble and terminal
inertia. Adding stage structure without upgrading the preamble to canonical declaration or
adding per-stage inertia binding raises the aspirational score from V-01 (better structure,
better coverage table mechanics, better seed-phrase gate) but leaves C-34, C-35, C-36, C-37
all failing. Score rises to ~23/29 from V-01's ~16/29 via structural improvements unrelated
to the C-34/C-35/C-36/C-37 chain.

**predicted:** C-34: FAIL (procedural preamble, not canonical declaration). C-35: FAIL
(terminal inertia instruction; stage gates do not enforce per-artifact extension). C-36: FAIL
(no labeled declarations). C-37: FAIL. Score: ~23/29.

**failure condition:** C-34 PASS if the procedural preamble sentence is interpreted as a
canonical-authority declaration. Diagnostic: the discriminating test is declarative form
("is the canonical identifier") vs. locative form ("contains" / "section in ROLE 2"); only
declarative form satisfies C-34.

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

The REAL-REQUIRED Rationale section in ROLE 2 contains pre-authored rationale for
REAL-REQUIRED = YES namespaces. When generating a REAL-REQUIRED block, copy the matching
entry from that section verbatim into the Rationale field.

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
Date, Status: MOCK); (3) each body is 3-5 sentences with HIGH-STRUCTURE vocabulary; (4) any
compliance-tagged namespace has a REAL-REQUIRED block with pre-authored rationale copied
verbatim.**

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
are complete; (2) each has a MOCK ARTIFACT header with all five fields; (3) each body is 3-5
sentences with EVIDENCE-HEAVY vocabulary; (4) each has a REAL-REQUIRED block with
pre-authored rationale copied verbatim.**

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

## V-03 -- Multi-Stage Per-Stage, Canonical Declaration, No Labels (C-36 FAIL + C-37 FAIL, 27/29)

**axis (primary):** C-34 PASS + C-35 PASS + C-36 FAIL + C-37 FAIL. The template preamble
explicitly declares "REAL-REQUIRED" as the canonical identifier (C-34 PASS): '"REAL-REQUIRED"
is the canonical identifier for the rationale section in this template. The ROLE 2 STOP gate
references this section by its canonical identifier. The GENERATOR copies from the
REAL-REQUIRED Rationale section by canonical name.' The inertia extension `-- specifically,
{instance}` is instantiated within each stage body independently (C-35 PASS). But neither
the canonical declaration nor the per-stage inertia requirement is assigned a reference label
("Declaration A", "Declaration B"). They exist as declarative sentences and per-stage
instructions, not as named contracts that gates can cite by label. C-36 FAIL.

**axis (secondary):** This is the structural ceiling below the new R18 axes -- the equivalent
of R17 V-04. All prior-round criteria at ceiling (C-01 through C-35): PASS. The only failing
criteria are C-36 (no labeled declarations) and C-37 (trivially FAIL: C-36 FAIL means no
labels exist to cite). Stage STOP gates enforce C-35 by verifying the per-artifact inertia
extension inline -- they name the requirement in gate text without citing a preamble label.

**hypothesis:** V-03 confirms the C-35 PASS + C-36 FAIL configuration. The discriminating
test between V-03 and V-04 is purely whether the preamble assigns "Declaration A" /
"Declaration B" labels. The per-stage inertia mechanism, the canonical REAL-REQUIRED
declaration, and all other structural properties are identical between V-03 and V-04. The
label assignment in V-04 costs nothing in structural complexity; it is an identifier
assigned to existing declarations. V-04 has C-36 PASS from V-03 baseline; V-03 has C-36 FAIL.

**predicted:** C-01 through C-35: PASS. C-36: FAIL (preamble declarations present but
unlabeled). C-37: FAIL (trivially; no labels to cite). Score: 27/29.

**failure condition:** C-36 PASS if the preamble incidentally assigns a label to either
declaration. Diagnostic: scan preamble for any form of "Declaration A" or "Declaration B"
or equivalent reference-label assignment; absence confirms C-36 FAIL.

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

## V-04 -- Labeled Declarations, Inline-Restatement Gates (C-36 PASS + C-37 FAIL, 28/29)

**axis (primary):** C-36 PASS + C-37 FAIL. This is the new intermediate case instantiated
for the first time in R18. The preamble assigns explicit reference labels to both structural
authority declarations (C-36 PASS): "Declaration A" names the canonical REAL-REQUIRED
identifier authority; "Declaration B" names the per-stage inertia extension authority.
Stage bodies cite "Per Declaration B: extend the inertia skeleton..." -- the label is
used as an instruction prefix. The stage STOP gates, however, restate the compliance
requirement inline: they say "each has an extended inertia statement with the skeleton
phrase and a topic-specific instance" (not "per Declaration B") and "each has a
REAL-REQUIRED block with pre-authored rationale copied verbatim" (not "per Declaration A").
C-37 FAIL: the gate text does not cite the preamble labels; it restates the requirements
independently. A scorer verifying C-35 compliance at Stage 1 must read the stage body
instruction ("Per Declaration B...") -- the gate does not close the loop by citing the
label.

**axis (secondary):** The preamble in V-04 is structurally identical to V-05. Both contain
Declaration A and Declaration B. The stage body instructions in V-04 and V-05 are identical:
both cite "Per Declaration B" before the inertia skeleton. The only structural difference
between V-04 and V-05 is in the stage STOP gate text. V-04 gates restate inline; V-05
gates cite by label. This single-axis isolation makes C-37 the discrimination criterion
between V-04 and V-05.

**hypothesis:** V-04 instantiates the C-36 PASS + C-37 FAIL case. The label exists in the
preamble (Declaration A, Declaration B). The stage body cites the label. But the gate
completes the check without referencing the label -- it uses inline description instead.
A reader verifying gate compliance has all the information needed, but must know to look
back at "Declaration B" to confirm the gate's inline text is a complete restatement.
The closed verification loop in V-05 -- where preamble declaration + gate citation is
sufficient -- is absent in V-04. Gate text "per Declaration B" would close the loop; the
absence of those three words is the sole difference from the ceiling.

**predicted:** C-01 through C-36: PASS. C-37: FAIL (stage STOP gates restate inline
rather than citing "per Declaration A" / "per Declaration B"). Score: 28/29.

**failure condition:** C-37 PASS if any stage STOP gate incidentally includes a reference
to "Declaration A" or "Declaration B". Diagnostic: scan Stage 1 STOP gate, Stage 2 STOP
gate, and Stage 3 / ROLE 2 STOP gate for any text of the form "per Declaration A" or
"per Declaration B"; absence in all gates confirms C-37 FAIL.

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

## V-05 -- Labeled Declarations, Gate-Citation Ceiling (C-36 PASS + C-37 PASS, 29/29)

**axis (primary):** C-36 PASS + C-37 PASS. The structural mechanism is identical to V-04
in the preamble and stage body instructions. The sole change is the stage STOP gate text:
Stage 1 STOP gate says "per Declaration B" for the inertia requirement and "per Declaration A"
for the REAL-REQUIRED block requirement. Stage 2 STOP gate says "per Declaration B" and
"per Declaration A". The ROLE 2 STOP gate says "per Declaration B -- verified at Stage 1,
Stage 2, and Stage 3 individually" and "per Declaration A". This closes the verification
loop: a scorer confirms C-35 compliance by reading Declaration B (preamble) + Stage 1 gate
("per Declaration B") alone, without reading the stage body. A scorer confirms C-34
compliance by reading Declaration A (preamble) + gate clause ("per Declaration A") alone.

**axis (secondary):** V-05 demonstrates that C-37 is a formatting property of gate text,
not a structural property of the template's enforcement mechanism. The enforcement is
identical between V-04 and V-05: both have per-stage inertia firing independently, both
have REAL-REQUIRED rationale copied verbatim. C-37 concerns only whether the gate
references the preamble label -- it is a readability and auditability criterion, not a
completeness criterion. V-04 is fully correct in what it enforces; V-05 is verifiably
correct from a shorter reading path.

**hypothesis:** V-05 is the 29/29 ceiling. All 29 aspirational criteria pass. The closed
reference loop for both Declaration A (C-34 mechanism + C-36 label + C-37 gate citation)
and Declaration B (C-35 mechanism + C-36 label + C-37 gate citation) is complete. A scorer
with access to the preamble section and the gate text alone -- without the stage body
instructions -- can confirm compliance with both structural constraints.

**predicted:** C-01 through C-37: PASS. Score: 29/29.

**failure condition:** C-37 FAIL if any stage STOP gate omits the "per Declaration A" /
"per Declaration B" citation. Diagnostic: verify Stage 1 STOP gate, Stage 2 STOP gate,
and ROLE 2 STOP gate each contain "per Declaration B" for the inertia requirement and
"per Declaration A" for the REAL-REQUIRED block requirement; absence in any gate confirms
C-37 FAIL for that gate.

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

| Variation | C-34 | C-35 | C-36 | C-37 | Primary axis | Predicted |
|-----------|------|------|------|------|-------------|-----------|
| V-01 | FAIL | PASS (trivial) | FAIL | FAIL | Single-stage; no preamble declaration; no labels | 16/29 |
| V-02 | FAIL | FAIL | FAIL | FAIL | Multi-stage; procedural preamble; terminal inertia; stage gates check completeness only | 23/29 |
| V-03 | PASS | PASS | FAIL | FAIL | Multi-stage; canonical declaration; per-stage inertia; no labels; gates restate inline | 27/29 |
| V-04 | PASS | PASS | PASS | FAIL | Multi-stage; labeled declarations (Dec A, Dec B); stage bodies cite labels; gates restate inline | 28/29 |
| V-05 | PASS | PASS | PASS | PASS | Multi-stage; labeled declarations; gates cite "per Declaration A" / "per Declaration B" | 29/29 |

Single-axis discrimination chain:
- V-03 vs V-04: C-36 axis only -- add "Declaration A" / "Declaration B" labels to preamble
- V-04 vs V-05: C-37 axis only -- gate text changes from inline restatement to label citation

R18 instantiates the C-36 PASS + C-37 FAIL intermediate case (V-04, 28/29) that was
absent from R17. V-04 demonstrates that labeled declarations are necessary but not sufficient
for C-37: the label must appear in the gate text, not only in the preamble and stage body.

Discrimination table under v18:

| Variation | C-36 | C-37 | Aspirational | Composite |
|-----------|------|------|-------------|-----------|
| V-01 | FAIL | FAIL | 16/29 | 95.5 |
| V-02 | FAIL | FAIL | 23/29 | 97.9 |
| V-03 | FAIL | FAIL | 27/29 | 99.3 |
| V-04 | PASS | FAIL | 28/29 | 99.7 |
| V-05 | PASS | PASS | 29/29 | 100.0 |

Next: /mock:review mock-all simulations/quest/golden/mock-all-variate-R18-2026-03-16.md
