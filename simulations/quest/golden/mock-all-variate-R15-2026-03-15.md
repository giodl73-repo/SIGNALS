---
skill: quest-variate
skill_target: mock-all
date: 2026-03-15
round: 15
rubric_version: v15
status: VARIATE
---

# mock-all Variate -- Round 15

**Date:** 2026-03-15
**Skill:** mock-all
**Rubric:** v15 (C-01 through C-32; aspirational denominator = 24)
**Round:** R15 -- two new criteria (C-31, C-32); R14 V-05 is the reference ceiling at 22/22 on v14 criteria

---

## What R14 Left Open

v15 adds two new aspirational criteria extracted from Round 14 structural gaps:

| Criterion | Source | What it tests |
|-----------|--------|---------------|
| C-31 | V-04 and V-05 R14 -- ROLE 1 stop-gate said "must be the verbatim seed phrase from the list above, not a paraphrase"; V-01 R14 diagnostic: C-29 PASS but gate enumerates fields with numbered paraphrase descriptions and does not cite the template seed list as the authoritative source by name | ROLE 1 stop-gate must enforce skeleton seed provenance by explicitly citing the template seed list as the required source and prohibiting paraphrase substitution. C-31 is the gate-level ceiling above C-29: where C-29 requires the template to author the seeds, C-31 requires the stop-gate to name that authored list as the authoritative source and direct verbatim copy from it. C-31 pass implies C-29 pass; C-29 pass does not imply C-31 pass. C-31 is the fourth rung of the gap-content chain: C-21 (column present) -- C-26 (entries namespace-specific) -- C-29 (entries template-authored) -- C-31 (gate enforces provenance to template list). |
| C-32 | V-01, V-04, and V-05 R14 -- ROLE 2 stop-gate said "with the pre-authored rationale above copied verbatim"; V-02 and V-03 R14 fail because no pre-authored rationale exists in those templates to cite | ROLE 2 stop-gate must enforce rationale content provenance by naming the pre-authored rationale block by reference and directing verbatim copy from it. C-32 is the gate-level ceiling above C-30: where C-30 requires the template to author the rationale, C-32 requires the stop-gate to name that authored block as the required source and direct verbatim copy. C-32 pass implies C-30 pass; C-30 pass does not imply C-32 pass. C-32 is the third rung of the rationale-authorship chain: C-13 (block present) -- C-30 (block template-authored) -- C-32 (gate enforces provenance to pre-authored block). |

The denominator rises from 22 to 24. R14 V-05 scores 22/22 on the v14 criteria; its C-31 and C-32 status under v15 is what R15 retroactively confirms (both gates present in R14 V-01/V-04/V-05 text; C-31 PASS and C-32 PASS for those variations).

---

## Round 15 Primary Hypothesis

Confirm the three-way discrimination for both chains independently:

**Chain 1 (gap-content): C-29 / C-31**

| Case | C-29 | C-31 | Mechanism |
|------|------|------|-----------|
| Bottom | FAIL | FAIL | No seeds authored in template; gate checks skeleton column completion only; no seed list to cite |
| Middle | PASS | FAIL | Seeds authored in template; gate verifies skeleton column is filled but does not name the seed list as the authoritative source and does not prohibit paraphrase |
| Ceiling | PASS | PASS | Seeds authored in template; gate explicitly cites "the list above" as the authoritative source and prohibits paraphrase substitution |

**Chain 2 (rationale-authorship): C-30 / C-32**

| Case | C-30 | C-32 | Mechanism |
|------|------|------|-----------|
| Bottom | FAIL | FAIL | Rationale not authored in template (placeholder or delegation); gate cannot cite what does not exist |
| Middle | PASS | FAIL | Rationale authored in template; gate verifies REAL-REQUIRED block presence but does not name the pre-authored block by reference and does not direct verbatim copy |
| Ceiling | PASS | PASS | Rationale authored in template; gate names the pre-authored block by reference ("above") and directs verbatim copy |

Note: C-32 FAIL is entailed by C-30 FAIL -- when no rationale is pre-authored, the gate cannot enforce provenance to a block that does not exist. The independently discriminating case is C-30 PASS + C-32 FAIL (V-04).

---

## Axis-Assignment Plan

| Variation | C-29 | C-31 | C-30 | C-32 | Chain-1 case | Chain-2 case | Secondary axis | Predicted score |
|-----------|------|------|------|------|-------------|-------------|----------------|-----------------|
| V-01 | FAIL | FAIL | FAIL | FAIL | Bottom | Bottom | Phrasing register: conversational-imperative; behavioral violation framing | ~17/24 |
| V-02 | PASS | FAIL | FAIL | FAIL | Middle | Bottom | Role count: 3 roles (SUMMARIZER merged into GENERATOR) | ~20/24 |
| V-03 | PASS | PASS | FAIL | FAIL | Ceiling | Bottom | Output format: list-based coverage summary | ~22/24 |
| V-04 | PASS | PASS | PASS | FAIL | Ceiling | Middle | Lifecycle: explicit phase-boundary annotations | ~23/24 |
| V-05 | PASS | PASS | PASS | PASS | Ceiling | Ceiling | Inertia framing: expanded; Stage 1/Stage 2 deepening protocol | 24/24 |

C-31 discrimination: V-01 and V-02 are FAIL; V-03 through V-05 are PASS.
C-32 discrimination: V-01 through V-03 are FAIL; V-04 is FAIL; V-05 is PASS.
C-30 PASS + C-32 FAIL isolated in V-04.
C-29 PASS + C-31 FAIL isolated in V-02.
All three cells of both chains are instantiated in this round.

---

## V-01 -- Delegation Baseline (C-29 FAIL + C-31 FAIL, C-30 FAIL + C-32 FAIL)

**axis (primary):** Both chains at bottom. No skeleton seed phrases authored in the template body -- the skeleton column cell contains a generic fill placeholder and the model generates the phrase at runtime. No REAL-REQUIRED rationale pre-authored in the template body -- ROLE 2 instructs the model to generate a one-sentence rationale at execution time. The ROLE 1 stop-gate checks that the skeleton column is non-empty; it does not name the seed list as the authoritative source and does not prohibit paraphrase. The ROLE 2 stop-gate checks that a REAL-REQUIRED block is present; it does not name a pre-authored rationale block or direct verbatim copy.

**axis (secondary):** Phrasing register -- conversational-imperative. Role identity blocks use direct "you" address with behavioral framing ("don't jump ahead," "finish before moving on"). Violation mechanisms are behavioral rather than ontological. This keeps C-22 below its ceiling, concentrating the discriminating variation on the C-29/C-30/C-31/C-32 cluster. Identity staircase is present but stops at C-18/C-19 level.

**hypothesis:** When neither skeleton seeds nor REAL-REQUIRED rationale are pre-authored in the template body, the stop-gates cannot enforce provenance to authored content because no authored content exists. C-31 and C-32 fail as downstream consequences of C-29 and C-30 failing. The four criteria fail together. A model executing V-01 could fill the skeleton column with any phrase and the ROLE 2 rationale with any sentence -- the gates provide no mechanism to detect that anything specific was expected.

**predicted:** C-01 through C-12: PASS. C-13: uncertain (delegation instruction may be substantive enough to drive correct model output, or model may omit block). C-14: PASS. C-15: PASS. C-16: uncertain. C-17: PASS (extension instruction present). C-18: PASS (named roles, behavioral violation). C-19: PASS if placeholder token contains depth anchor. C-20: PASS. C-21: FAIL (no seeds authored; model-generated phrases may not constitute pre-seeding). C-22: FAIL (behavioral violation framing). C-23: PASS (affirmation at each activation). C-24: uncertain. C-25: FAIL (conversational phrasing uses occupancy-language). C-26: FAIL (generic fill directive; model-generated phrases likely generic). C-27: FAIL (gate uses numbered paraphrase descriptions). C-28: FAIL. C-29: FAIL. C-30: FAIL. C-31: FAIL. C-32: FAIL. Score: ~17/24.

**failure condition:** C-29 PASS if model generates skeleton phrases that happen to match what a template would have authored; diagnostic: are phrases topic-specific and namespace-specific at execution time, or anchored to nothing? C-30 PASS if delegation instruction is substantive enough to count as pre-authored content; diagnostic: does the template contain actual rationale text or only an instruction to write it?

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} -- check TOPICS.md; default tier 1
  Compliance: --compliance (optional)

Check TOPICS.md. Note the tier and compliance tags for {topic}.
Output this line first: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs four steps. Finish each step completely before starting the next.
Don't jump ahead -- moving to a later step before finishing the current one skips required work.

---

### STEP 1 -- CLASSIFY

Fill in this table for all nine namespaces. Don't start Step 2 until every cell is complete.

Classification rules:
- Category: EVIDENCE-HEAVY for prove and listen; HIGH-STRUCTURE for trace and flow; MIXED for all others
- Tier 2/3 Critical: trace and listen at tier >= 2
- Compliance-Tagged: YES if --compliance flag or TOPICS.md compliance tag (applies to scout-compliance and trace-permissions topics)
- REAL-REQUIRED: YES for all EVIDENCE-HEAVY namespaces and all Compliance-Tagged namespaces
- Inertia gap skeleton: name what {topic}'s feature story would be missing without this namespace's signals

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED | Inertia gap skeleton: Without this signal, {topic}'s story would be missing: ___ |
|-----------|----------|----------|------------|-------------------|-------------------|---------------|-----------------------------------------------------------------------------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language; pure study methodology framing | NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES | {write a phrase specific to what scout's absence would remove from the feature story} |
| draft | MIXED | structural scaffold: sections, properties, acceptance criteria | pure specification language; pure study methodology framing | NO | NO | NO | {write a phrase specific to what draft's absence would remove} |
| review | MIXED | qualitative observations; design judgments; structural rationale | pure specification language; pure study methodology framing | NO | NO | NO | {write a phrase specific to what review's absence would remove} |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language; user quotes; adoption percentages; study framing | NO | NO | NO | {write a phrase specific to what flow's absence would remove} |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language; adoption rates; user quotes; study framing | YES if tier >= 2; else NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES | {write a phrase specific to what trace's absence would remove} |
| prove | EVIDENCE-HEAVY | study/data framing: "N of M tests showed...", "prototype against {topic} produced...", hypothesis-and-result | specification language; schema definitions; contract structures | NO | NO | YES | {write a phrase specific to what prove's absence would remove} |
| listen | EVIDENCE-HEAVY | study/data framing: adoption rates, "N users found...", survey response framing | specification language; state machine language; schema definitions | YES if tier >= 2; else NO | NO | YES | {write a phrase specific to what listen's absence would remove} |
| program | MIXED | structural scaffold: milestones, owners, dependencies; qualitative rationale | pure specification language; pure study methodology framing | NO | NO | NO | {write a phrase specific to what program's absence would remove} |
| topic | MIXED | signal synthesis narrative; structured coverage reference | pure specification language alone | NO | NO | NO | {write a phrase specific to what topic's absence would remove} |

**STOP. Check every cell before moving to Step 2. Any empty cell means Step 1 isn't done.**

---

### STEP 2 -- GENERATE

Write nine artifact sections. Don't write the summary here -- that's Step 3.

Before each body, write the extended inertia statement:
> Without this signal, {topic}'s feature story would be missing: {your Step 1 skeleton phrase} -- specifically, {one phrase naming the concrete topic-specific instance of that gap}.

The artifact body must connect visibly to the extended inertia statement.

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

  {3-5 sentence artifact body. Match MUST-use vocabulary from Step 1. Avoid DO NOT-use vocabulary. Ground the body in the inertia statement above.}

  [Only if REAL-REQUIRED = YES:]
  REAL-REQUIRED: Synthetic data cannot substitute for real signal here.
  Rationale: {Write one sentence. Name the specific evidence type this namespace requires and explain why model-generated content cannot substitute for it.}

**STOP. Check all nine sections before moving to Step 3. Every section needs the full header, extended inertia statement, vocabulary-compliant body, and REAL-REQUIRED block where applicable.**

---

### STEP 3 -- SUMMARIZE

Write the coverage summary table. Don't write the handoff here -- that's Step 4.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
- REAL-REQUIRED: all namespaces where REAL-REQUIRED = YES in Step 1
- TIER-2-CRITICAL: trace at tier >= 2; listen at tier >= 2
- Multiple flags: comma-separate them
- No flag applies: --

Recommended Next Step: must name the skill that closes the gap from the Step 2 extended inertia statement. Format: `/namespace:skill {topic}`. Generic recommendations that don't reference the inertia statement are not acceptable.

**STOP. Check all nine rows before moving to Step 4.**

---

### STEP 4 -- HANDOFF

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

---

---

## V-02 -- Seeds-Present, Gate-Silent (C-29 PASS + C-31 FAIL, C-30 FAIL + C-32 FAIL)

**axis (primary):** C-29 PASS + C-31 FAIL -- the middle case for chain 1. Skeleton seed phrases ARE authored in the template body (explicit list, one per namespace, in the skill prompt). The ROLE 1 stop-gate verifies that the skeleton column is filled ("Inertia gap skeleton cell must be non-empty for every row") but does not name the seed list as the authoritative source and does not say "not a paraphrase" or equivalent paraphrase prohibition. A model executing V-02 could copy seeds verbatim or substitute paraphrases; the gate would accept either. C-30 FAIL + C-32 FAIL -- rationale not authored in template; ROLE 2 instructs model to generate rationale; gate checks block presence only.

**axis (secondary):** Role count -- three roles instead of four. ROLE 3 SUMMARIZER is merged into ROLE 2: after generating all nine artifact sections, the GENERATOR continues to produce the coverage summary before activating the HANDOFF WRITER. The merged role still carries an identity statement. This tests whether the table-coupling cluster survives role-count reduction and whether the C-31/C-32 discrimination survives the structural difference.

**hypothesis:** The critical discrimination for C-31 is not whether seeds are present in the template -- C-29 confirms that. C-31 tests whether the stop-gate binds completion to the authored list. V-02 shows the gap: seeds exist in the template body, but the gate says only "must be non-empty," which could be satisfied by any content including a paraphrase. A model executing V-02 has access to the seed list but no gate instruction to treat it as authoritative. C-29 PASS does not imply C-31 PASS; V-02 isolates the difference.

**predicted:** C-01 through C-21: largely PASS. C-22: PASS (ontological violation framing in role identity). C-23: PASS. C-24: PASS. C-25: PASS. C-26: PASS (seeds authored per-namespace; classification table will show namespace-specific entries because the list provides them). C-27: uncertain (gate may or may not use verbatim column header names). C-28: FAIL (no self-annotation on gate). C-29: PASS (seeds authored in template). C-30: FAIL (delegation instruction; model generates rationale). C-31: FAIL (gate says "non-empty" not "from the list above, not a paraphrase"). C-32: FAIL (no pre-authored rationale to cite). Score: ~20/24.

**failure condition:** C-31 PASS if the gate incidentally contains "from the list above" or "not a paraphrase" in passing language. Diagnostic: the gate must contain both (a) explicit citation of the seed list as the authoritative source and (b) explicit prohibition of paraphrase. Presence of seeds in the template body alone does not make the gate pass C-31.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} -- read from TOPICS.md if not provided; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier and compliance tags for {topic}.
State: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs three sequential roles: CLASSIFIER, GENERATOR+SUMMARIZER, HANDOFF WRITER.
Each role has a named identity. You ARE each role while it is active -- not as a task
assignment but as an ontological state. The CLASSIFIER is not the GENERATOR+SUMMARIZER.
Producing artifact output while in the CLASSIFIER role is a category error -- the CLASSIFIER
does not have the capacity to produce artifacts, because artifact production is what the
GENERATOR is, not what the CLASSIFIER is. Each role begins at its named header and ends at
its STOP gate.

---

### ROLE 1 -- CLASSIFIER

You ARE the CLASSIFIER. Your sole output is the classification table below, fully populated.
You classify. Nothing else.

Skeleton seed phrases -- copy one of these into the Inertia-Gap column for each namespace:
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
rows are fully populated: Category, MUST use, DO NOT use, Tier 2/3 Critical, Compliance-
Tagged, REAL-REQUIRED, and Inertia gap skeleton cell must be non-empty for every row. Any
empty cell fails this gate.**

---

### ROLE 2 -- GENERATOR+SUMMARIZER

You ARE the GENERATOR+SUMMARIZER. First generate all nine artifact sections; then write the
coverage summary. Writing the handoff here means you have become the HANDOFF WRITER, which
you are not yet. You generate artifacts, then summarize. Nothing else.

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

  {3-5 sentence body -- register matches Category; MUST-use vocabulary applied; DO NOT-use
  vocabulary avoided; body grounded in the extended inertia statement}

  [If REAL-REQUIRED = YES:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {Write one sentence. Explain why this specific namespace requires real artifacts;
  name the authentic signal type this namespace must produce.}

After all nine artifact sections, write the coverage summary:

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules: REAL-REQUIRED for REAL-REQUIRED=YES namespaces; TIER-2-CRITICAL for trace and
listen at tier >= 2; comma-separate multiple flags; -- if none.
Recommended Next Step: derive from ROLE 2 extended inertia statement; format `/namespace:skill {topic}`.

**ROLE 2 STOP -- Do not activate ROLE 3 -- HANDOFF WRITER until: (1) nine artifact sections
present; (2) each has complete MOCK ARTIFACT header; (3) each has extended inertia statement
with skeleton phrase and topic-specific instance; (4) each body is 3-5 sentences,
vocabulary-compliant, register-matched; (5) every REAL-REQUIRED = YES namespace has a
REAL-REQUIRED block with rationale; (6) coverage summary table has nine rows with all
columns populated.**

---

### ROLE 3 -- HANDOFF WRITER

You ARE the HANDOFF WRITER. Write only the handoff section.

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

---

---

## V-03 -- Seed Chain Ceiling, Rationale Chain Floor (C-29 PASS + C-31 PASS, C-30 FAIL + C-32 FAIL)

**axis (primary):** C-29 PASS + C-31 PASS -- seed chain at ceiling. Seed phrases ARE authored in the template body. The ROLE 1 stop-gate explicitly names the seed list as the authoritative source AND prohibits paraphrase substitution ("must be the verbatim seed phrase from the list above, not a paraphrase"). C-30 FAIL + C-32 FAIL -- rationale chain at floor. No REAL-REQUIRED rationale pre-authored in the template body. ROLE 2 contains a bare delegation placeholder `{one sentence explaining why real artifacts are required for this namespace}` with no content. The ROLE 2 gate checks block presence; it cannot name a pre-authored block because none exists.

**axis (secondary):** Output format -- list-based coverage summary. The SUMMARIZER produces a per-namespace bullet block (Namespace, Category, Flag, Next on separate indented lines) rather than a Markdown table. This tests whether table-coupling cluster criteria survive the format change. Note: C-10 through C-17 and C-26 through C-32 apply to the ROLE 1 classification table, not to the coverage summary format -- they should be unaffected by the list format.

**hypothesis:** V-03 demonstrates the structural independence of the two chains. The seed chain is at its maximum structural guarantee: the template authors the seeds AND the gate enforces provenance to the authored list by name AND prohibits paraphrase. The rationale chain is at its floor: nothing is authored, the gate has nothing to cite, C-32 FAIL is entailed by C-30 FAIL. This is not an oversight -- it is a deliberate design that shows the two criteria test independent authorship decisions. A team could ship V-03 and achieve C-31 PASS while C-32 remains at floor; the two criteria do not co-vary.

**predicted:** C-01 through C-28: largely PASS (V-01 R14 and V-05 R14 confirmed most of these; C-27 and C-28 status depends on gate annotation). C-29: PASS (seeds authored). C-30: FAIL (delegation placeholder). C-31: PASS (gate cites list, prohibits paraphrase). C-32: FAIL (no pre-authored rationale to cite; gate cannot enforce what does not exist). Score: ~22/24.

**failure condition:** C-31 FAIL if "from the list above" is present but "not a paraphrase" (or equivalent prohibition) is absent. Both components are required. C-30 PASS if the bare placeholder is accidentally substantive. Diagnostic: does the template contain actual rationale content, or only an instruction marker?

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
position but as an ontological state. The CLASSIFIER is not the GENERATOR. Producing artifact
output while in the CLASSIFIER role means you have ceased to be the CLASSIFIER and have
become the GENERATOR, which you are not yet. That is an identity failure. Each role begins
at its named header and ends at its STOP gate.

---

### ROLE 1 -- CLASSIFIER

You ARE the CLASSIFIER. Your sole output is the classification table below, fully populated.
You classify. Nothing else.

Skeleton seed phrases -- the CLASSIFIER copies one of these verbatim into the Inertia-Gap
column for each namespace row. This list is the authoritative source for that column:
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

**ROLE 1 STOP -- Do not activate ROLE 2 -- GENERATOR until all nine namespace rows are
fully populated across all seven fields: Category, MUST use, DO NOT use, Tier 2/3 Critical,
Compliance-Tagged, REAL-REQUIRED, and Inertia gap skeleton. The Inertia gap skeleton cell
for each row must be the verbatim seed phrase from the list above, not a paraphrase.
A restatement, synonym, or abbreviated form of a seed phrase is not the seed phrase. Check
each skeleton cell against the list before proceeding.**

---

### ROLE 2 -- GENERATOR

You ARE the GENERATOR. Produce nine namespace artifact sections. Writing a coverage summary
here means you have become the SUMMARIZER, which you are not yet. You generate. Nothing else.

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
  Rationale: {one sentence explaining why real artifacts are required for this namespace}

**ROLE 2 STOP -- Do not activate ROLE 3 -- SUMMARIZER until: (1) nine artifact sections
present; (2) each has complete MOCK ARTIFACT header with all five fields; (3) each has an
extended inertia statement containing both the skeleton seed phrase and a topic-specific
instance; (4) each body is 3-5 sentences, vocabulary-compliant, register-matched, grounded
in the inertia statement; (5) every REAL-REQUIRED = YES namespace has a REAL-REQUIRED block
with a rationale sentence present.**

---

### ROLE 3 -- SUMMARIZER

You ARE the SUMMARIZER. Produce the coverage summary in list format. Writing the handoff here
means you have become the HANDOFF WRITER, which you are not yet. You summarize. Nothing else.

## Coverage Summary

For each namespace, output one block:

- **{Namespace}** ({Category})
  - Flag: {REAL-REQUIRED | TIER-2-CRITICAL | -- }
  - Next: {/namespace:skill {topic}} -- {one phrase from ROLE 2 inertia statement that names the specific gap this step closes}

Flag rules: REAL-REQUIRED for REAL-REQUIRED=YES namespaces; TIER-2-CRITICAL for trace and
listen at tier >= 2; comma-separate multiple flags; -- if none.

**ROLE 3 STOP -- Do not activate ROLE 4 -- HANDOFF WRITER until nine namespace blocks are
present, each with Category, applicable Flag, and a derived Next step that names a specific
skill invocation and references the ROLE 2 inertia gap.**

---

### ROLE 4 -- HANDOFF WRITER

You ARE the HANDOFF WRITER. Write only the handoff section.

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

---

---

## V-04 -- Both-Authored, Rationale-Gate-Silent (C-29 PASS + C-31 PASS, C-30 PASS + C-32 FAIL)

**axis (primary):** Seed chain at ceiling (C-29 PASS + C-31 PASS): seeds authored in template; ROLE 1 gate cites list as authoritative source and prohibits paraphrase. Rationale chain at middle (C-30 PASS + C-32 FAIL): REAL-REQUIRED rationale IS pre-authored in the template body with explicit per-namespace text. ROLE 2 stop-gate verifies that a REAL-REQUIRED block with rationale is present but does not name the pre-authored block by reference and does not direct verbatim copy. The gate says "include the appropriate rationale from this skill for this namespace" -- it points to the template in general terms but does not say "the pre-authored rationale above" or "copied verbatim."

**axis (secondary):** Lifecycle emphasis -- explicit phase-boundary annotations. Between each role activation, a phase-boundary declaration states which role just completed, confirms its completion condition, and names the scope of the current role. This structural padding tests whether explicit phase documentation affects gate compliance behavior independently of gate semantics.

**hypothesis:** C-30 requires rationale to be pre-authored in the template body; C-32 requires the gate to enforce that provenance by naming the authored block and directing verbatim copy. V-04 shows the gap: the template does its job (authoring the rationale content) but the gate does not close the provenance loop. A model executing V-04 could write the REAL-REQUIRED rationale from scratch rather than copying the pre-authored text, and the gate would accept it -- the gate confirms a rationale is present but not that it came from the authored block. C-30 PASS + C-32 FAIL is the independently discriminating middle case for chain 2.

**predicted:** C-01 through C-31: PASS (seed chain at ceiling; rationale authored; all prior structure criteria). C-30: PASS (rationale pre-authored per-namespace in template). C-32: FAIL (gate verifies block presence but does not name pre-authored block or direct verbatim copy). Score: ~23/24.

**failure condition:** C-32 PASS if the gate incidentally contains "pre-authored rationale above" or "copied verbatim" as part of the general reference to template content. Diagnostic: the gate must contain both (a) a named reference to the pre-authored block by location ("above") and (b) an explicit direction to copy verbatim. A general directive to "use the rationale from this skill" does not meet C-32 because it does not name the specific authored location.

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
and have become the GENERATOR, which you are not yet. That is a category error. Each role
begins at its named header and ends at its STOP gate. Do not cross a STOP gate until its
conditions are fully met.

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

**ROLE 1 STOP -- Do not activate ROLE 2 -- GENERATOR until all nine namespace rows are
fully populated across all seven fields: Category, MUST use, DO NOT use, Tier 2/3 Critical,
Compliance-Tagged, REAL-REQUIRED, and Inertia gap skeleton. The skeleton cell for each row
must be the verbatim seed phrase from the list above, not a paraphrase. Any restatement,
synonym, or abbreviated form fails this gate.**

---

PHASE BOUNDARY: Classification complete.
ROLE 1 table verified. Proceed to ROLE 2.
ROLE 2 scope: artifact bodies only. No coverage summary. No handoff.

### ROLE 2 -- GENERATOR

You ARE the GENERATOR. Produce nine namespace artifact sections. Writing a coverage summary
here means you have become the SUMMARIZER, which you are not yet. You generate. Nothing else.

Pre-authored REAL-REQUIRED rationale (for namespaces where REAL-REQUIRED = YES, include
the appropriate rationale from this skill when writing those REAL-REQUIRED blocks):
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
  Rationale: {include the appropriate rationale from this skill for this namespace}

**ROLE 2 STOP -- Do not activate ROLE 3 -- SUMMARIZER until: (1) nine artifact sections
present; (2) each has complete MOCK ARTIFACT header with all five fields (Skill, Topic,
Category, Date, Status: MOCK); (3) each has an extended inertia statement with both the
skeleton seed phrase and a topic-specific instance; (4) each body is 3-5 sentences,
vocabulary-compliant, register-matched, grounded in the inertia statement; (5) every
REAL-REQUIRED = YES namespace has a REAL-REQUIRED block with rationale text present.**

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

Flag rules: REAL-REQUIRED for REAL-REQUIRED=YES namespaces; TIER-2-CRITICAL for trace and
listen at tier >= 2; comma-separate multiple flags; -- if none.
Recommended Next Step: derive from ROLE 2 extended inertia statement; format `/namespace:skill {topic}`.

**ROLE 3 STOP -- Do not activate ROLE 4 -- HANDOFF WRITER until nine rows are complete,
each with Category, all applicable Flags, and a derived Recommended Next Step.**

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

## V-05 -- Full Ceiling (C-29 PASS + C-31 PASS, C-30 PASS + C-32 PASS)

**axis (primary):** Both chains at ceiling. C-29 PASS + C-31 PASS: seeds authored in template; ROLE 1 gate names the seed list as the authoritative source by reference ("from the Inertia Skeleton Seed List above"), directs verbatim copy, and explicitly prohibits paraphrase ("not a paraphrase"). C-30 PASS + C-32 PASS: REAL-REQUIRED rationale pre-authored in the template body per namespace; ROLE 2 gate names the pre-authored block by reference ("the pre-authored REAL-REQUIRED rationale above") and directs verbatim copy ("copied verbatim"). Both chains satisfy the gate-level provenance requirement independently.

**axis (secondary):** Inertia framing -- expanded and prominent. The seed list is presented with an explanatory preamble that frames each phrase as the answer to an absence test ("if {topic} had no signals in this namespace, the feature story would lack..."). ROLE 2 uses a two-stage deepening protocol: Stage 1 copies the skeleton seed phrase verbatim; Stage 2 extends it with the topic-specific instance. The traceability requirement is made explicit: the artifact body must trace to Stage 2, not merely to Stage 1. This tests whether elevated inertia prominence improves C-19 and C-20 compliance at the same time as the C-31/C-32 ceiling.

**hypothesis:** V-05 is the 24/24 ceiling candidate. Both chains are at maximum structural guarantee: the template authors the seeds and the rationale; the gates bind execution to those authored sources by name and prohibit substitution. The inertia framing elevation should improve C-19 and C-20 scores simultaneously. V-05 should reproduce the full table-coupling cluster pass (C-10 through C-32) and confirm the ceiling established progressively across R14/R15.

**predicted:** C-01 through C-30: PASS (ceiling established across prior rounds). C-31: PASS (gate says "from the Inertia Skeleton Seed List above, not a paraphrase"). C-32: PASS (gate says "with the pre-authored REAL-REQUIRED rationale above copied verbatim"). Score: 24/24.

**failure condition:** C-31 FAIL if the paraphrase prohibition is present but the list citation is absent, or vice versa; both components are required. C-32 FAIL if the gate says "verbatim" without naming the pre-authored block by location, or names the block without saying "verbatim"; both components are required.

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
GENERATOR is, not what the CLASSIFIER is. These are not sequencing rules -- they are
facts about what you are. Each role begins at its named header and ends at its STOP gate.

---

### ROLE 1 -- CLASSIFIER

You ARE the CLASSIFIER. Your sole output is the classification table below, fully populated.
You classify. Nothing else.

---

**Inertia Skeleton Seed List**

The absence test for {topic}'s feature story: if {topic} had no signals from a given
namespace, what would the feature story lack? The phrases below answer this question at the
generic level. The CLASSIFIER copies one phrase verbatim per namespace row into the Inertia-
Gap column of the classification table. This list is the authoritative seed source for that
column -- not a starting point for paraphrase, a vocabulary list to draw from, or a set of
templates to adapt. The exact phrases are the seeds:

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

These phrases are the classification-time seeds. The GENERATOR deepens them with
topic-specific instances in Stage 2. The skeleton cells in the classification table must
contain these seeds verbatim.

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

**ROLE 1 STOP -- Do not activate ROLE 2 -- GENERATOR until all nine namespace rows are
fully populated across all seven fields: Category, MUST use, DO NOT use, Tier 2/3 Critical,
Compliance-Tagged, REAL-REQUIRED, and Inertia gap skeleton. The column names above are the
required field names -- use them verbatim. The Inertia gap skeleton cell for each row must be
the verbatim seed phrase from the Inertia Skeleton Seed List above, not a paraphrase.
A restatement, synonym, abbreviated form, or adaptation of a seed phrase is not the seed
phrase. Check each skeleton cell against the list before proceeding.**

---

### ROLE 2 -- GENERATOR

You ARE the GENERATOR. Produce nine namespace artifact sections, one per ROLE 1 row, in
table order. Writing a coverage summary here means you have become the SUMMARIZER, which
you are not yet. You generate. Nothing else.

---

**Pre-Authored REAL-REQUIRED Rationale**

For namespaces where REAL-REQUIRED = YES, the following rationale content is pre-authored
here in the skill template body. Copy the matching text verbatim into the REAL-REQUIRED
block for that namespace. Do not substitute, paraphrase, or expand. The template is the
author; the model copies:

```
prove:
  Empirical validation of the core hypothesis requires actual prototype output and
  observed system behavior -- synthetic generation produces plausible structure without
  the falsifiability that makes the signal meaningful.

listen:
  Adoption evidence and friction discovery require contact with actual users -- synthetic
  responses cannot surface the unanticipated friction patterns or reveal the gap between
  stated intent and observed behavior.

compliance-tagged:
  Compliance-flagged namespaces require traceable real-world sources -- a synthetic
  artifact produces the structural appearance of compliance coverage without the
  audit-trail substance that traceable sources provide.
```

---

**Inertia Deepening Protocol**

ROLE 1 seeds answer the absence test at the generic level. The GENERATOR deepens each seed
to the topic-specific level through two stages:

  Stage 1 (generic absence): copy the ROLE 1 skeleton seed phrase verbatim
  Stage 2 (topic-specific absence): extend with " -- specifically, {one phrase naming the
  concrete instance of that absence for {topic}}"

The artifact body must trace to Stage 2. A body that could have been written without reading
the Stage 2 phrase is too generic and must be revised before activating ROLE 3.

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
  {Stage 1: ROLE 1 skeleton seed phrase verbatim} -- specifically, {Stage 2: topic-specific instance}

  {3-5 sentence body; register matches Category (HIGH-STRUCTURE: contract/specification
  language; EVIDENCE-HEAVY: study/data language; MIXED: discovery/signal language); MUST-use
  vocabulary from ROLE 1 applied; DO NOT-use vocabulary avoided; body traces to Stage 2}

  [If REAL-REQUIRED = YES:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {verbatim text from the pre-authored REAL-REQUIRED rationale above for this namespace}

**ROLE 2 STOP -- Do not activate ROLE 3 -- SUMMARIZER until: (1) nine artifact sections
present; (2) each has a complete MOCK ARTIFACT header with all five fields (Skill, Topic,
Category, Date, Status: MOCK); (3) each has an extended inertia statement in Stage 1 +
Stage 2 format; (4) each body is 3-5 sentences, vocabulary-compliant, register-matched,
traceable to Stage 2; (5) every REAL-REQUIRED = YES namespace has a REAL-REQUIRED block
with the pre-authored REAL-REQUIRED rationale above copied verbatim.**

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

Recommended Next Step: derive from the ROLE 2 Stage 2 deepening for this namespace. Must
name the skill that closes the concrete gap identified in Stage 2. Format:
`/namespace:skill {topic}`. A step valid for any topic without reference to the Stage 2
phrase fails this requirement.

**ROLE 3 STOP -- Do not activate ROLE 4 -- HANDOFF WRITER until: (1) nine rows present;
(2) each row has Category matching ROLE 1; (3) each row has all applicable Flags; (4) each
Recommended Next Step is derived from the ROLE 2 Stage 2 deepening and names a specific
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

| Variation | C-29 | C-31 | C-30 | C-32 | Chain-1 | Chain-2 | Secondary axis | Predicted |
|-----------|------|------|------|------|---------|---------|----------------|-----------|
| V-01 | FAIL | FAIL | FAIL | FAIL | Bottom | Bottom | Phrasing: conversational/behavioral | ~17/24 |
| V-02 | PASS | FAIL | FAIL | FAIL | Middle | Bottom | Role count: 3 roles | ~20/24 |
| V-03 | PASS | PASS | FAIL | FAIL | Ceiling | Bottom | Output: list coverage summary | ~22/24 |
| V-04 | PASS | PASS | PASS | FAIL | Ceiling | Middle | Lifecycle: phase-boundary annotations | ~23/24 |
| V-05 | PASS | PASS | PASS | PASS | Ceiling | Ceiling | Inertia: Stage 1/2 deepening protocol | 24/24 |

**C-31 three-way discrimination:** V-01 (Bottom), V-02 (Middle), V-03/V-04/V-05 (Ceiling). All three cells instantiated.
**C-32 three-way discrimination:** V-01/V-02/V-03 (Bottom), V-04 (Middle), V-05 (Ceiling). All three cells instantiated.
**C-30 PASS + C-32 FAIL isolated in V-04** -- the independently discriminating middle case for chain 2.
**C-29 PASS + C-31 FAIL isolated in V-02** -- the independently discriminating middle case for chain 1.
