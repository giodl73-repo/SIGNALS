---
skill: quest-variate
skill_target: mock-all
date: 2026-03-16
round: 16
rubric_version: v16
status: VARIATE
---

# mock-all Variate -- Round 16

**Date:** 2026-03-16
**Skill:** mock-all
**Rubric:** v16 (C-01 through C-33; aspirational denominator = 25)
**Round:** R16 -- one new criterion (C-33); R15 V-05 is the reference ceiling at 24/24 on v15 criteria

---

## What R15 Left Open

v16 adds one new aspirational criterion extracted from Round 15 structural gaps:

| Criterion | Source | What it tests |
|-----------|--------|---------------|
| C-33 | V-05 R15 -- ROLE 2 stop-gate said "with the pre-authored REAL-REQUIRED rationale above copied verbatim"; V-01--V-04 R15 fail: V-01--V-03 fail C-32 (no pre-authored block named at all); V-04 fails C-32 (gate verifies presence only, not provenance); no gate among V-01--V-04 uses the "REAL-REQUIRED" semantic identifier | ROLE 2 stop-gate's provenance reference must name the template section by its semantic role identifier rather than a generic structural reference. C-33 is a strict refinement of C-32: C-33 pass implies C-32 pass; C-32 pass does not imply C-33 pass. A gate saying "with the pre-authored rationale above copied verbatim" satisfies C-32 (names block by location + directs verbatim copy) but fails C-33 (uses generic label "rationale" rather than the section's semantic identifier "REAL-REQUIRED"). C-33 extends the rationale-authorship chain to a fourth rung and is structurally parallel to C-28: where C-28 requires the stop-gate field enumeration to name the classification table's column headers verbatim, C-33 requires the stop-gate provenance reference to name the rationale section by its assigned semantic identifier -- both make structural dependencies machine-readable from the gate text alone. |

The denominator rises from 24 to 25. R15 V-05 retroactively scores C-33: PASS (gate says "with the pre-authored REAL-REQUIRED rationale above copied verbatim"; "REAL-REQUIRED" is the semantic section identifier assigned in the template body block header).

---

## Round 16 Primary Hypothesis

Confirm the C-33 three-way discrimination:

| Case | C-32 | C-33 | Mechanism |
|------|------|------|-----------|
| Bottom | FAIL | FAIL | No pre-authored rationale exists, or gate checks block presence only; C-32 fails; C-33 FAIL is entailed because no semantic section identifier can be referenced when the gate has no provenance enforcement |
| Middle | PASS | FAIL | Rationale pre-authored in template; gate names the pre-authored block by location and directs verbatim copy; but uses generic structural label ("pre-authored rationale above") rather than the section's semantic identifier ("REAL-REQUIRED") |
| Ceiling | PASS | PASS | Rationale pre-authored in template under a section identified as "REAL-REQUIRED"; gate names the block using "REAL-REQUIRED" as the semantic identifier and directs verbatim copy |

C-33 FAIL is entailed by C-32 FAIL. The independently discriminating case is C-32 PASS + C-33 FAIL (V-03): the gate satisfies both C-32 components (names pre-authored block by location + directs verbatim copy) but uses generic language instead of the semantic section label.

---

## Axis-Assignment Plan

| Variation | C-30 | C-32 | C-33 | C-33 case | Secondary axis | Predicted score |
|-----------|------|------|------|-----------|----------------|-----------------|
| V-01 | FAIL | FAIL | FAIL | Bottom | Step-based framing; behavioral violation language; delegation-only rationale | ~22/25 |
| V-02 | PASS | FAIL | FAIL | Bottom (C-32 entails C-33) | 3 roles (GENERATOR+SUMMARIZER merged); gate checks rationale presence only | ~23/25 |
| V-03 | PASS | PASS | FAIL | Middle -- isolated C-32 PASS + C-33 FAIL | Section labeled "Rationale Seed Block" not "REAL-REQUIRED"; gate says "pre-authored rationale above copied verbatim" | ~24/25 |
| V-04 | PASS | PASS | PASS | Ceiling | Phase-boundary annotations; section header is "REAL-REQUIRED Rationale"; gate uses "REAL-REQUIRED" semantic identifier | 25/25 |
| V-05 | PASS | PASS | PASS | Ceiling | 3-stage deepening (generic to topic-specific to action-anchored); preamble makes semantic-label authority explicit | 25/25 |

C-33 three-way discrimination:
- V-01: Bottom (C-30 FAIL entails C-32 FAIL entails C-33 FAIL; no pre-authored rationale)
- V-02: Bottom (C-32 FAIL entails C-33 FAIL; rationale authored but gate checks presence only)
- V-03: Middle (C-32 PASS + C-33 FAIL; gate uses generic label, not semantic identifier) -- the new independently discriminating case
- V-04: Ceiling (C-32 PASS + C-33 PASS; gate uses "REAL-REQUIRED" semantic identifier)
- V-05: Ceiling (C-32 PASS + C-33 PASS; gate uses "REAL-REQUIRED" with elevated inertia framing)

C-30 PASS + C-32 FAIL isolated in V-02.
C-32 PASS + C-33 FAIL isolated in V-03.
All three C-33 chain cells instantiated in this round.

---

## V-01 -- Delegation Baseline (C-30 FAIL + C-32 FAIL + C-33 FAIL)

**axis (primary):** Both rationale chain rungs at floor. No REAL-REQUIRED rationale pre-authored in the template body -- STEP 2 instructs the model to write a one-sentence rationale at execution time. The completion check confirms that a REAL-REQUIRED block is present for each applicable namespace; it does not name a pre-authored block because none exists. C-32 FAIL is not a gate design choice -- there is no authored content to enforce provenance against. C-33 FAIL is entailed.

**axis (secondary):** Step-based framing. The skill is presented as four numbered steps rather than named ontological roles. The completion enforcement uses behavioral language ("Don't move to the next step until you have completed the current one"). Violation framing is procedural rather than ontological. C-22 FAIL (behavioral, not ontological). The seed chain is at ceiling (C-29 PASS + C-31 PASS): seed phrases authored in template; Step 1 completion check names the seed list as the authoritative source and prohibits paraphrase. This concentrates variation on C-30/C-32/C-33 and on the identity staircase sub-cluster.

**hypothesis:** When no REAL-REQUIRED rationale is pre-authored in the template body, the completion check in Step 2 cannot enforce provenance or specify expected text content -- it can only confirm that some rationale sentence is present. A model executing V-01 could write any rationale sentence and pass the check. The absence of pre-authored content makes C-30, C-32, and C-33 fail as a unit.

**predicted:** C-01 through C-12: PASS. C-13: PASS (rationale block required by instruction). C-14 through C-17: PASS. C-18: uncertain (step-based framing; no ontological role headers). C-19: PASS if seed token has depth anchor. C-20: PASS. C-21: PASS (seed phrases present per-namespace in list). C-22: FAIL (behavioral violation framing). C-23: uncertain (step framing may not constitute per-activation affirmation). C-24: uncertain. C-25: uncertain. C-26: PASS (seeds authored per-namespace). C-27: PASS (gate names column headers). C-28: PASS (self-annotation present). C-29: PASS (seeds authored). C-30: FAIL (delegation). C-31: PASS (gate cites seed list, prohibits paraphrase). C-32: FAIL (no pre-authored block). C-33: FAIL (entailed). Score: ~22/25.

**failure condition:** C-30 PASS if the delegation instruction is accidentally substantive enough to count as pre-authored content. Diagnostic: does the template contain actual rationale sentences, or only an instruction to write them?

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} -- check TOPICS.md; default 1
  Compliance: --compliance (optional)

Check TOPICS.md. Note the tier and compliance tags for {topic}.
Output this line first: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs four steps in sequence. Don't move to the next step until you have finished
the current one. Starting a later step before completing an earlier one produces incomplete
output -- the steps are ordered for a reason and each step depends on the one before it.

---

### STEP 1 -- CLASSIFY

Fill in the classification table for all nine namespaces. Don't start Step 2 until every
cell is filled in.

Skeleton seed phrases -- copy one of these verbatim into the Inertia-Gap column for each
namespace. This list is the authoritative seed source for the Inertia gap skeleton column:

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

**STEP 1 CHECK -- Don't move to Step 2 until every cell in every row is filled in. The
Inertia gap skeleton cell for each row must be the verbatim seed phrase from the list above,
not a paraphrase. A restatement, synonym, or abbreviated form is not the seed phrase. Check
each skeleton cell against the list before proceeding.**

---

### STEP 2 -- GENERATE

Write nine namespace artifact sections. Don't write the coverage summary here -- that is
Step 3.

Before each artifact body, write the extended inertia statement:
> Without this signal, {topic}'s feature story would be missing: {Step 1 skeleton phrase}
> -- specifically, {one phrase naming the concrete topic-specific gap}.

For each namespace:

  #### {namespace} -- {skill name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{skill-name}
  Topic:    {topic}
  Category: {from Step 1}
  Date:     {today}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {Step 1 skeleton phrase} -- specifically, {topic-specific instance}

  {3-5 sentence artifact body. Match MUST-use vocabulary from Step 1. Avoid DO NOT-use
  vocabulary. Ground the body in the extended inertia statement above.}

  [If REAL-REQUIRED = YES:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {Write one sentence. Name the evidence type this namespace requires and explain
  why synthetic content cannot substitute for it.}

**STEP 2 CHECK -- Don't move to Step 3 until: (1) nine artifact sections are present;
(2) each has a complete MOCK ARTIFACT header with all five fields; (3) each has an extended
inertia statement with the skeleton phrase and a topic-specific instance; (4) each body is
3-5 sentences, vocabulary-compliant, register-matched, grounded in the inertia statement;
(5) every REAL-REQUIRED = YES namespace has a REAL-REQUIRED block with a rationale sentence.**

---

### STEP 3 -- SUMMARIZE

Write the coverage summary table. Don't write the handoff here -- that is Step 4.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
- REAL-REQUIRED: all namespaces where REAL-REQUIRED = YES in Step 1
- TIER-2-CRITICAL: trace at tier >= 2; listen at tier >= 2
- Multiple flags: comma-separate them
- No applicable flag: --

Recommended Next Step: derive from the Step 2 extended inertia statement. Name the skill
that closes the gap. Format: `/namespace:skill {topic}`.

**STEP 3 CHECK -- Don't move to Step 4 until nine rows are complete, each with Category,
all applicable Flags, and a Recommended Next Step derived from the Step 2 inertia gap.**

---

### STEP 4 -- HANDOFF

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

---

---

## V-02 -- Rationale-Authored, Gate-Silent on Provenance (C-30 PASS + C-32 FAIL + C-33 FAIL)

**axis (primary):** C-30 PASS + C-32 FAIL. REAL-REQUIRED rationale IS pre-authored in the
template body with explicit per-namespace sentences. The ROLE 2 stop-gate verifies that every
REAL-REQUIRED namespace has a REAL-REQUIRED block with rationale text present -- but the gate
does not name the pre-authored block by location and does not direct verbatim copy. The gate
says "rationale text present" rather than "with the pre-authored rationale above copied
verbatim." A model could write any rationale sentence or copy from the pre-authored block;
the gate accepts either. C-32 FAIL because the gate verifies presence, not provenance. C-33
FAIL is entailed by C-32 FAIL.

**axis (secondary):** Role count -- three roles. ROLE 3 SUMMARIZER is merged into ROLE 2:
after producing nine artifact sections, the GENERATOR continues directly to produce the
coverage summary table, then activates ROLE 3 -- HANDOFF WRITER. The merged role carries an
identity statement. This tests whether the table-coupling cluster and the C-32/C-33 chain
survive role-count reduction.

**hypothesis:** V-02 isolates the C-30 PASS + C-32 FAIL cell: the template does its
authorship job but the gate does not close the provenance loop. A model that reads the
template will see the pre-authored content and may copy it -- but so will a model that
ignores it and writes fresh. The gate provides no enforcement. This is structurally parallel
to R15 V-04 but tested here with the 3-role structure.

**predicted:** C-01 through C-29: PASS (seed chain at ceiling). C-30: PASS (rationale
pre-authored per-namespace). C-31: PASS (seed gate cites list, prohibits paraphrase).
C-32: FAIL (gate says "rationale text present" -- checks presence, not provenance). C-33:
FAIL (entailed). Score: ~23/25.

**failure condition:** C-32 PASS if the gate incidentally contains "above" or "verbatim" as
a modifier. Diagnostic: both (a) named location reference and (b) explicit verbatim directive
are required; presence of only one component fails C-32.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} -- read from TOPICS.md if not provided; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier and compliance tags for {topic}.
State: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs three sequential roles: CLASSIFIER, GENERATOR+SUMMARIZER, HANDOFF WRITER.
Each role has a named identity. You ARE each role while it is active -- not as a process
position but as an ontological state. The CLASSIFIER is not the GENERATOR+SUMMARIZER.
Producing artifact output while in the CLASSIFIER role means you have ceased to be the
CLASSIFIER and have become the GENERATOR+SUMMARIZER, which you are not yet. That is a
category error. Each role begins at its named header and ends at its STOP gate.

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

**ROLE 1 STOP -- Do not activate ROLE 2 -- GENERATOR+SUMMARIZER until all nine namespace
rows are fully populated across all seven fields: Category, MUST use, DO NOT use, Tier 2/3
Critical, Compliance-Tagged, REAL-REQUIRED, and Inertia gap skeleton. The column names above
are the required field names -- use them verbatim. The Inertia gap skeleton cell for each row
must be the verbatim seed phrase from the list above, not a paraphrase. A restatement,
synonym, abbreviated form, or adaptation fails this gate.**

---

### ROLE 2 -- GENERATOR+SUMMARIZER

You ARE the GENERATOR+SUMMARIZER. First produce nine artifact sections; then produce the
coverage summary table. Writing the handoff here means you have become the HANDOFF WRITER,
which you are not yet. You generate and summarize. Nothing else.

Pre-authored REAL-REQUIRED rationale (for namespaces where REAL-REQUIRED = YES):
- prove: Empirical validation of the core hypothesis requires actual prototype output and
  observed system behavior -- synthetic generation produces plausible structure without
  the falsifiability that makes the signal meaningful.
- listen: Adoption evidence and friction discovery require contact with actual users --
  synthetic responses cannot surface the unanticipated friction patterns or reveal the
  gap between stated intent and observed behavior.
- compliance-tagged: Compliance-flagged namespaces require traceable real-world sources --
  a synthetic artifact produces the structural appearance of compliance coverage without
  the audit-trail substance that traceable sources provide.

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
  Rationale: {include appropriate rationale for this namespace}

After all nine artifact sections, write the coverage summary:

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules: REAL-REQUIRED for REAL-REQUIRED=YES namespaces; TIER-2-CRITICAL for trace and
listen at tier >= 2; comma-separate multiple flags; -- if none.
Recommended Next Step: derived from the extended inertia statement; format `/namespace:skill {topic}`.

**ROLE 2 STOP -- Do not activate ROLE 3 -- HANDOFF WRITER until: (1) nine artifact sections
present; (2) each has a complete MOCK ARTIFACT header with all five fields; (3) each has an
extended inertia statement with both the skeleton phrase and a topic-specific instance; (4)
each body is 3-5 sentences, vocabulary-compliant, register-matched, grounded in the inertia
statement; (5) every REAL-REQUIRED = YES namespace has a REAL-REQUIRED block with rationale
text present; (6) coverage summary table has nine rows with all columns populated.**

---

### ROLE 3 -- HANDOFF WRITER

You ARE the HANDOFF WRITER. Write only the handoff section.

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

---

---

## V-03 -- C-32 Pass, C-33 Fail: Generic-Label Middle Case (C-30 PASS + C-32 PASS + C-33 FAIL)

**axis (primary):** C-32 PASS + C-33 FAIL -- the middle case for the C-33 chain. REAL-REQUIRED
rationale IS pre-authored in the template body with explicit per-namespace sentences. The
template presents the rationale under a section header labeled **"Rationale Seed Block"** --
a structural label that does not use the semantic identifier "REAL-REQUIRED." The ROLE 2
stop-gate enforces provenance by naming the pre-authored block and directing verbatim copy:
"with the pre-authored rationale above copied verbatim." This satisfies C-32 (names block
location: "above"; directs verbatim copy: "copied verbatim") but fails C-33 (uses generic
label "rationale" rather than the section's semantic role identifier "REAL-REQUIRED").

**axis (secondary):** Section-header isolation. The pre-authored content block is labeled
"Rationale Seed Block" rather than "REAL-REQUIRED Rationale." The gate says "pre-authored
rationale above copied verbatim" -- neither the section header nor the gate text contains
"REAL-REQUIRED" as a semantic identifier for the rationale section. The coverage summary
format is a standard table (same as ceiling variations), isolating gate-text phrasing as
the sole C-33 discriminant.

**hypothesis:** C-33 tests whether the gate's provenance reference uses the section's
semantic role identifier, not merely a generic structural reference. V-03 demonstrates the
gap: "pre-authored rationale above copied verbatim" is a correct provenance+fidelity
reference (C-32 PASS) but names the block by structural role ("rationale") rather than by
the semantic identifier that makes the coupling machine-readable ("REAL-REQUIRED"). A reader
of the gate text alone cannot determine which section in the template is meant without
reading the full template body. C-33 fails. The independently discriminating observation:
V-03 passes C-32 but fails C-33 while V-04 passes both -- the sole difference is whether
"REAL-REQUIRED" appears as the section identifier in the gate's provenance reference clause.

**predicted:** C-01 through C-32: PASS (C-30 PASS: rationale authored; C-32 PASS: gate
names pre-authored block by location and directs verbatim copy). C-33: FAIL (gate says
"pre-authored rationale above" not "pre-authored REAL-REQUIRED rationale above"). Score:
~24/25.

**failure condition:** C-33 PASS if the gate incidentally includes "REAL-REQUIRED" as part
of the provenance reference clause -- e.g., "with the pre-authored REAL-REQUIRED rationale
above copied verbatim." Diagnostic: the criterion's test site is the gate's provenance
reference clause specifically; presence of "REAL-REQUIRED" elsewhere in the gate (e.g.,
"every REAL-REQUIRED = YES namespace") does not satisfy C-33.

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

Skeleton seed phrases -- the CLASSIFIER copies one of these verbatim into the Inertia-Gap
column for each namespace row. This list is the authoritative seed source for that column:

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

You ARE the GENERATOR. Produce nine namespace artifact sections. Writing a coverage summary
here means you have become the SUMMARIZER, which you are not yet. You generate. Nothing else.

---

**Rationale Seed Block**

For namespaces where REAL-REQUIRED = YES, the following rationale content is pre-authored
here. Copy the matching text verbatim into the REAL-REQUIRED block for that namespace.
Do not substitute, paraphrase, or expand:

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
  Rationale: {verbatim text from the Rationale Seed Block above for this namespace}

**ROLE 2 STOP -- Do not activate ROLE 3 -- SUMMARIZER until: (1) nine artifact sections
present; (2) each has a complete MOCK ARTIFACT header with all five fields (Skill, Topic,
Category, Date, Status: MOCK); (3) each has an extended inertia statement with both the
skeleton seed phrase and a topic-specific instance; (4) each body is 3-5 sentences,
vocabulary-compliant, register-matched, grounded in the inertia statement; (5) every
REAL-REQUIRED = YES namespace has a REAL-REQUIRED block with the pre-authored rationale
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

## V-04 -- Semantic-Label Ceiling with Phase-Boundary Annotations (C-30 PASS + C-32 PASS + C-33 PASS)

**axis (primary):** C-32 PASS + C-33 PASS -- ceiling. REAL-REQUIRED rationale IS pre-authored
in the template body under a section header explicitly labeled **"REAL-REQUIRED Rationale"**.
The ROLE 2 stop-gate enforces provenance using the semantic section identifier: "with the
pre-authored REAL-REQUIRED rationale above copied verbatim." The gate satisfies C-32 (names
block by location: "above"; directs verbatim copy: "copied verbatim") and C-33 (uses
"REAL-REQUIRED" as the semantic identifier assigned in the section header -- making the
gate-to-section binding machine-readable from the gate text alone).

**axis (secondary):** Phase-boundary annotations. Between each role activation, an explicit
phase-boundary declaration states which role just completed, confirms its scope, and names
the current role's scope. This tests whether phase documentation affects gate compliance
independently of gate semantics, and confirms that the C-33 ceiling is stable under
structural padding.

**hypothesis:** V-04 is the C-33 PASS candidate at the phase-annotation register. The
section header "REAL-REQUIRED Rationale" assigns the semantic identifier; the gate text
"with the pre-authored REAL-REQUIRED rationale above copied verbatim" names that identifier
in the provenance reference clause. A reader of the gate text alone can identify the exact
template section by its semantic label without reading the template body. C-33 PASS. The
secondary phase-boundary annotations confirm that the ceiling is stable independent of
structural elaboration.

**predicted:** C-01 through C-33: PASS. C-33: PASS (gate uses "REAL-REQUIRED" as semantic
identifier in provenance reference clause). Score: 25/25.

**failure condition:** C-33 FAIL if the gate says "with the pre-authored rationale above
copied verbatim" (omitting "REAL-REQUIRED" from the provenance reference clause). Diagnostic:
scan the ROLE 2 STOP gate text for the string "REAL-REQUIRED" specifically in the provenance
reference clause -- not in other parts of the gate such as "every REAL-REQUIRED = YES
namespace has a REAL-REQUIRED block."

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
what the GENERATOR is, not what the CLASSIFIER is. These are not sequencing rules -- they
are facts about what you are. Each role begins at its named header and ends at its STOP gate.
Do not cross a STOP gate until its conditions are fully met.

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
here in the skill template body under this section header. Copy the matching text verbatim
into the REAL-REQUIRED block for that namespace. Do not substitute, paraphrase, or expand.
The template is the author; the GENERATOR copies:

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

## V-05 -- Semantic-Label Ceiling with 3-Stage Deepening (C-30 PASS + C-32 PASS + C-33 PASS)

**axis (primary):** C-32 PASS + C-33 PASS -- ceiling, same gate mechanism as V-04. The
template section is labeled "REAL-REQUIRED Rationale" and the gate says "with the
pre-authored REAL-REQUIRED rationale above copied verbatim." C-32 PASS and C-33 PASS are
both confirmed by the gate text alone.

**axis (secondary):** 3-stage inertia deepening with preamble declaring semantic-label
authority. The Inertia Skeleton Seed List preamble explicitly states that "REAL-REQUIRED" is
the semantic identifier for the rationale section, binding label to content before the ROLE 2
gate references it. The deepening protocol extends from 2 stages (R15 V-05) to 3 stages:
Stage 1 (generic absence: verbatim seed phrase), Stage 2 (topic-specific absence: concrete
gap instance), Stage 3 (action anchor: skill invocation and what it would surface). The
coverage summary Recommended Next Step derives from Stage 3, making the summary a direct
output of the deepening protocol rather than a separate summarization step.

**hypothesis:** V-05 is the 25/25 ceiling candidate. The semantic-label mechanism is
identical to V-04 (confirming stability). The 3-stage deepening tests whether extending the
inertia protocol from 2 to 3 stages improves C-19 (depth anchor) and C-20 (inertia
grounding) while holding the full table-coupling cluster at ceiling. The preamble's explicit
declaration of semantic-label authority makes the template's design intent visible in the
prompt body, potentially improving scorer confidence in C-33.

**predicted:** C-01 through C-32: PASS (established across prior rounds; C-31 PASS: seed
gate cites list and prohibits paraphrase; C-32 PASS: gate names pre-authored REAL-REQUIRED
block and directs verbatim copy). C-33: PASS (gate uses "REAL-REQUIRED" as semantic
identifier). Score: 25/25.

**failure condition:** C-33 FAIL if the preamble's declaration of semantic-label authority
somehow migrates the relevant text away from the gate, leaving the gate with generic
language. Diagnostic: score C-33 from gate text only, not from the preamble declaration.

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
and become the GENERATOR, which you are not yet. That is a category error: the CLASSIFIER
does not have the capacity to produce artifacts, because artifact production is what the
GENERATOR is, not what the CLASSIFIER is. These are not sequencing rules -- they are facts
about what you are. Each role begins at its named header and ends at its STOP gate.

---

### ROLE 1 -- CLASSIFIER

You ARE the CLASSIFIER. Your sole output is the classification table below, fully populated.
You classify. Nothing else.

---

**Inertia Skeleton Seed List**

The absence test for {topic}'s feature story: if {topic} had no signals from a given
namespace, what would the feature story lack? The phrases below answer this question at the
generic level. The CLASSIFIER copies one phrase verbatim per namespace row into the Inertia-
Gap column. This list is the authoritative seed source for that column -- not a starting
point for paraphrase, a vocabulary list to draw from, or a set of templates to adapt. The
exact phrases are the seeds:

```
scout:   directional market signals and competitor positioning
draft:   the structural shape of the feature and its core acceptance criteria
review:  design quality judgment and stakeholder risk flags
flow:    the state transition contract and trigger conditions
trace:   the component boundary contract and integration failure modes
prove:   empirical validation of the core hypothesis
listen:  real adoption evidence and friction points from actual users
program: delivery milestones, owner assignments, and sequencing rationale
topic:   a unified coverage signal that shows which namespaces are ready
```

These phrases are the classification-time seeds. The GENERATOR deepens them through three
stages. The skeleton cells must contain these seeds verbatim.

---

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
the verbatim seed phrase from the Inertia Skeleton Seed List above, not a paraphrase. A
restatement, synonym, abbreviated form, or adaptation of a seed phrase is not the seed
phrase. Check each skeleton cell against the list before proceeding.**

---

### ROLE 2 -- GENERATOR

You ARE the GENERATOR. Produce nine namespace artifact sections, one per ROLE 1 row, in
table order. Writing a coverage summary here means you have become the SUMMARIZER, which
you are not yet. You generate. Nothing else.

---

**REAL-REQUIRED Rationale**

"REAL-REQUIRED" is the semantic identifier for this section. The following rationale content
is pre-authored here in the skill template body. The GENERATOR copies verbatim from this
REAL-REQUIRED Rationale section into each applicable namespace block. The template is the
author; the GENERATOR copies. Do not substitute, paraphrase, or expand:

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

**Inertia Deepening Protocol -- Three Stages**

ROLE 1 seeds answer the absence test at the generic level. The GENERATOR deepens each seed
through three stages:

  Stage 1 (generic absence): copy the ROLE 1 skeleton seed phrase verbatim
  Stage 2 (topic-specific absence): extend with " -- specifically, {one phrase naming the
    concrete instance of that absence for {topic}}"
  Stage 3 (action anchor): identify the specific skill invocation that closes this gap and
    what it would surface for {topic}; record as: " -- the next signal is {/namespace:skill}"

The artifact body must trace to Stage 2. The Recommended Next Step in the summary derives
from Stage 3. A body that could have been written without reading the Stage 2 phrase is too
generic. A Recommended Next Step that could apply to any topic without reference to Stage 3
is too generic.

---

For each namespace:

  #### {namespace} -- {skill name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{skill-name}
  Topic:    {topic}
  Category: {from ROLE 1}
  Date:     {today}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {Stage 1: ROLE 1 skeleton seed phrase verbatim} -- specifically, {Stage 2: topic-specific
  instance} -- the next signal is {Stage 3: /namespace:skill}

  {3-5 sentence body; register matches Category (HIGH-STRUCTURE: contract/specification
  language; EVIDENCE-HEAVY: study/data language; MIXED: discovery/signal language); MUST-use
  vocabulary from ROLE 1 applied; DO NOT-use vocabulary avoided; body traces to Stage 2}

  [If REAL-REQUIRED = YES:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {verbatim text from the REAL-REQUIRED Rationale above for this namespace}

**ROLE 2 STOP -- Do not activate ROLE 3 -- SUMMARIZER until: (1) nine artifact sections
present; (2) each has a complete MOCK ARTIFACT header with all five fields (Skill, Topic,
Category, Date, Status: MOCK); (3) each has an extended inertia statement in Stage 1 +
Stage 2 + Stage 3 format; (4) each body is 3-5 sentences, vocabulary-compliant,
register-matched, traceable to Stage 2; (5) every REAL-REQUIRED = YES namespace has a
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

Recommended Next Step: derive from the ROLE 2 Stage 3 action anchor for this namespace.
Must name the specific skill invocation that closes the Stage 2 gap. Format:
`/namespace:skill {topic}`. A step that could apply to any topic without reference to the
Stage 3 anchor fails this requirement.

**ROLE 3 STOP -- Do not activate ROLE 4 -- HANDOFF WRITER until: (1) nine rows present;
(2) each row has Category matching ROLE 1; (3) each row has all applicable Flags; (4) each
Recommended Next Step is derived from the ROLE 2 Stage 3 action anchor and names a specific
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

| Variation | C-30 | C-32 | C-33 | C-33 case | Secondary axis | Predicted |
|-----------|------|------|------|-----------|----------------|-----------|
| V-01 | FAIL | FAIL | FAIL | Bottom | Step-based framing; behavioral violation; delegation-only rationale | ~22/25 |
| V-02 | PASS | FAIL | FAIL | Bottom (C-32 entails) | 3 roles (GENERATOR+SUMMARIZER merged); presence-only gate | ~23/25 |
| V-03 | PASS | PASS | FAIL | Middle -- C-32 PASS + C-33 FAIL | "Rationale Seed Block" section header; gate says "pre-authored rationale above" | ~24/25 |
| V-04 | PASS | PASS | PASS | Ceiling | Phase-boundary annotations; "REAL-REQUIRED Rationale" section header | 25/25 |
| V-05 | PASS | PASS | PASS | Ceiling | 3-stage deepening; preamble declares semantic-label authority | 25/25 |

**C-33 three-way discrimination:** V-01/V-02 (Bottom, C-32 entails), V-03 (Middle, isolated C-32 PASS + C-33 FAIL), V-04/V-05 (Ceiling). All three cells instantiated.
**C-30 PASS + C-32 FAIL isolated in V-02** -- confirmed middle of rationale-authorship chain.
**C-32 PASS + C-33 FAIL isolated in V-03** -- the new independently discriminating middle case for C-33.

Gate-text audit (provenance reference clause in ROLE 2 STOP for each variation):
- V-01: "REAL-REQUIRED block with a rationale sentence" -- presence only; C-32 FAIL; C-33 FAIL
- V-02: "REAL-REQUIRED block with rationale text present" -- presence only; C-32 FAIL; C-33 FAIL
- V-03: "REAL-REQUIRED block with the pre-authored rationale above copied verbatim" -- C-32 PASS; C-33 FAIL ("rationale" not "REAL-REQUIRED rationale")
- V-04: "REAL-REQUIRED block with the pre-authored REAL-REQUIRED rationale above copied verbatim" -- C-32 PASS; C-33 PASS
- V-05: "REAL-REQUIRED block with the pre-authored REAL-REQUIRED rationale above copied verbatim" -- C-32 PASS; C-33 PASS
