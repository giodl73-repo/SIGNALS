---
skill: quest-variate
skill_target: mock-all
date: 2026-03-15
round: 12
rubric_version: v12
status: VARIATE
---

# mock-all Variate -- Round 12

**Date:** 2026-03-15
**Skill:** mock-all
**Rubric:** v12 (C-01 through C-27; aspirational denominator = 19)
**Round:** R12 -- two new criteria; R11 V-02 is the reference ceiling at 17/17

---

## What R11 Left Open

v12 adds two new aspirational criteria extracted from Round 11 structural gaps:

| Criterion | Source | What it tests |
|-----------|--------|---------------|
| C-26 | V-05 Pattern 1 -- skeleton column existed but cells contained TBD; C-21 required non-empty but C-26 requires namespace-specific content at table construction time | The inertia gap skeleton column cells must be filled with namespace-specific gap phrases at the point the table is written, not deferred to ROLE 2 artifact bodies. A cell that writes "TBD" or "namespace-level gap" passes C-21 (non-empty) but fails C-26 (not namespace-specific). The coupling: C-10 and C-17 can only derive next steps and vocabulary from the skeleton if the cell is specific enough to read directly. |
| C-27 | V-05 Pattern 2 -- stop-gate enumerated fields by description ("six required fields"), not by verbatim column names; structural self-reference missing | The ROLE 1 stop-gate must name the classification table's actual column headers verbatim as its required fields. A gate that says "(1) Category; (2) MUST-use vocabulary; (3) REAL-REQUIRED" passes C-16 (enumerated fields) but fails C-27 if the table headers use different labels (e.g., "MUST use" vs "MUST-use vocabulary"). Verbatim match is the load-bearing condition. Side effect: a gate written to name verbatim column headers cannot be written before the columns are declared, so C-11 and C-14 pass automatically. |

The denominator rises from 17 to 19. The R11 reference (V-02) scores 17/17 on the old
criteria. Its C-26 and C-27 status under v12 is what R12 determines.

The three-criteria coupling that C-26 enables: when the skeleton cell is namespace-specific
at table construction time, C-10 (next steps actionable/namespace-specific) and C-17
(vocabulary anchored as table columns) have content to derive from directly. The chain:
ROLE 1 skeleton cell -> ROLE 2 topic-specific extension -> ROLE 3 next step grounded in
inertia answer. If the skeleton cell is generic, the chain breaks at the first link.

---

## Axis-Assignment Plan

| Variation | Axis | Source signal | Target criteria | Predicted score |
|-----------|------|---------------|-----------------|-----------------|
| V-01 | role-sequence (skill pre-seeds skeleton cells in template; model reads, not invents) | C-26 requires cells authored at classification time. If the skill provides namespace-level skeleton phrases in the template body, the model is reading them into the table rather than inventing them free-form -- this is the strongest form of "authored at classification time." | C-26: PASS (seed phrases in template, copied into table during ROLE 1); C-27: UNCERTAIN (stop-gate uses paraphrase, not verbatim headers) | 18/19 |
| V-02 | output-format (ROLE 1 stop-gate enumerates verbatim column header names) | C-27 requires verbatim column names in the gate. V-02 declares all column headers explicitly and then writes the gate using those exact labels. This is the direct C-27 test. | C-26: UNCERTAIN (skeleton cells written by model without pre-seeded phrases -- may be specific or generic); C-27: PASS (gate text is verbatim match to declared column headers) | 18/19 |
| V-03 | phrasing-register (conversational, first-person descriptive rather than imperative-block) | Tests whether register affects C-26 and C-27. A conversational skill that says "I'll pre-fill the skeleton column with the gap each namespace owns by default" is semantically equivalent but structurally different. | C-26: PARTIAL (conversational pre-fill instruction may lead to generic phrases); C-27: FAIL (conversational gate descriptions rarely match verbatim column names) | 15/19 |
| V-04 | combination: V-01 template-seeded skeleton + V-02 verbatim stop-gate (C-26 + C-27 maximum form) | Both new criteria at ceiling simultaneously. Template provides seed phrases; stop-gate names columns verbatim. Tests whether the two criteria reinforce each other structurally. | C-26: PASS; C-27: PASS; all C-01 through C-25: PASS | 19/19 aspirational -- ceiling confidence variant |
| V-05 | combination: V-02 verbatim gate + lifecycle emphasis (explicit column-declaration step before ROLE 1 fills the table) | C-27's self-reference cascade requires columns to be declared before the gate references them. V-05 makes this explicit by adding a column-declaration step before ROLE 1 table generation -- the model first commits to column names, then fills the table, then the gate names those columns verbatim. | C-26: UNCERTAIN (explicit column step may improve specificity but does not guarantee namespace-specific seed phrases); C-27: PASS (column names committed before gate written) | 18-19/19 |

---

## V-01 -- Role Sequence: Skill Pre-Seeds Skeleton Cells in Template (Single Axis)

**axis:** role-sequence (skill template body provides namespace-level skeleton phrases for
the inertia gap skeleton column; model reads these into the table during ROLE 1 rather than
inventing them free-form; no change to any other structural element)
**hypothesis:** C-26 requires skeleton cells to be "authored at classification time" with
"namespace-specific gap content." The ambiguity in prior rounds was whether the model,
instructed to fill a skeleton column, would produce namespace-specific phrases or generic
fillers. V-01 eliminates this ambiguity by providing the seed phrases in the skill prompt
itself. The model reads the phrases into the table; it does not originate them. This is
the strongest form of "authored at classification time" -- the skill is the author, not
the model. C-27 is not targeted: the stop-gate continues to use paraphrase descriptions
rather than verbatim column labels.
**predicted:** C-01 through C-25: PASS (structure unchanged from R11 ceiling V-02). C-26:
PASS (seed phrases are in the template, namespace-specific, authored before ROLE 1 executes).
C-27: FAIL (stop-gate uses enumerated descriptions, not verbatim column labels). Score: 18/19.
**failure condition:** C-26 PARTIAL if the model treats the seed phrases as examples and
substitutes its own generic phrases rather than using the provided seeds verbatim. The
diagnostic test: do the skeleton cells in the output match the phrases provided in the
skill template? A mismatch indicates the model is re-inventing rather than reading.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} -- read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier for {topic} and any compliance tags.
State at top of output: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs four sequential roles: CLASSIFIER, GENERATOR, SUMMARIZER, HANDOFF WRITER.
Each role has a named identity. You ARE each role while it is active. This is an identity
statement, not a process instruction. The CLASSIFIER and the GENERATOR are distinct entities.
A CLASSIFIER that writes artifact bodies has ceased to be the CLASSIFIER -- it has become
the GENERATOR, which it is not yet. Wrong-phase output is an identity failure, not a
sequencing error. Each role begins at its named header and ends at its STOP gate. Do not
cross a STOP gate until its conditions are fully met.

---

### ROLE 1 -- CLASSIFIER

You ARE the CLASSIFIER. Your sole output is the classification table below, fully populated.
Writing an artifact body here means you have become the GENERATOR, which you are not yet.
Writing a coverage summary here means you have become the SUMMARIZER, which you are not yet.
You classify. Nothing else.

Classification rules:
- EVIDENCE-HEAVY: prove, listen
- HIGH-STRUCTURE: trace, flow
- MIXED: scout, draft, review, program, topic

REAL-REQUIRED rationale (applies to all EVIDENCE-HEAVY and compliance-active namespaces):
A synthetic artifact cannot substitute for real signal. prove-* requires actual experiment
data or prototype outputs. listen-* requires real user interviews or adoption measurements.
Compliance-active namespaces require traceable real-world sources -- synthetic artifacts
create false assurance regardless of structural quality.

Skeleton seed phrases (use these verbatim in the "Inertia gap skeleton" column):
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
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language; pure study methodology framing | NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES | directional market signals and competitor positioning |
| draft | MIXED | structural scaffold: sections, properties, acceptance criteria; qualitative observations | pure specification language; pure study methodology framing | NO | NO | NO | the structural shape of the feature and its core acceptance criteria |
| review | MIXED | qualitative observations; design judgments; structural rationale | pure specification language; pure study methodology framing | NO | NO | NO | design quality judgment and stakeholder risk flags |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language; user quotes; adoption percentages; study framing | NO | NO | NO | the state transition contract and trigger conditions |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language; adoption rates; user quotes; study framing | YES if tier >= 2; else NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES | the component boundary contract and integration failure modes |
| prove | EVIDENCE-HEAVY | study/data framing: "N of M tests showed...", "prototype against {topic} produced...", hypothesis-and-result | specification language; schema definitions; contract structures | NO | NO | YES | empirical validation of the core hypothesis |
| listen | EVIDENCE-HEAVY | study/data framing: adoption rates, "N users found...", survey response framing | specification language; state machine language; schema definitions | YES if tier >= 2; else NO | NO | YES | real adoption evidence and friction points from actual users |
| program | MIXED | structural scaffold: milestones, owners, dependencies; qualitative rationale | pure specification language; pure study methodology framing | NO | NO | NO | delivery milestones, owner assignments, and sequencing rationale |
| topic | MIXED | signal synthesis narrative; structured coverage reference | pure specification language alone | NO | NO | NO | a unified coverage signal that shows which namespaces are ready |

**ROLE 1 STOP -- Do not activate ROLE 2 -- GENERATOR until all nine namespaces have all
eight fields populated: (1) Category; (2) MUST-use vocabulary; (3) DO NOT-use vocabulary;
(4) Tier 2/3 Critical; (5) Compliance-Tagged; (6) REAL-REQUIRED; (7) Inertia gap skeleton
with the provided seed phrase (not a generic substitute). Any empty cell or substituted
phrase fails this gate.**

---

### ROLE 2 -- GENERATOR

You ARE the GENERATOR. Produce nine namespace artifact sections, one per ROLE 1 row, in
table order. Writing a coverage summary here means you have become the SUMMARIZER, which
you are not yet. You generate. Nothing else.

Before writing each artifact body, extend the inertia skeleton for this namespace with
topic-specific content:

> Without this signal, {topic}'s feature story would be missing: {skeleton phrase from
> ROLE 1 table} -- specifically, {one phrase naming the topic-specific instance of that gap}.

Write the completed inertia statement immediately before the body. The body must be
traceable to the completed inertia statement -- a body that could have been written without
reading the statement is too generic and must be revised.

For each namespace:

  #### {Namespace} -- {representative-skill-name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{representative-skill-name}
  Topic:    {topic}
  Category: {from ROLE 1 table}
  Date:     {current date}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {skeleton phrase from ROLE 1 table} -- specifically, {topic-specific instance}

  {3-5 sentence artifact body -- register matches Category: HIGH-STRUCTURE uses
  contract/specification language; EVIDENCE-HEAVY uses study/data language; MIXED uses
  discovery/signal language; apply MUST-use vocabulary from ROLE 1, avoid DO NOT-use
  vocabulary; body must be grounded in the completed inertia statement above, not generically
  valid for any topic}

  [If REAL-REQUIRED = YES in ROLE 1 table:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {one sentence -- prove: requires actual experiment data; listen: requires real
  user feedback; compliance namespace: requires traceable real-world sources.}

**ROLE 2 STOP -- Do not activate ROLE 3 -- SUMMARIZER until: (1) nine artifact sections
present; (2) each has a complete MOCK ARTIFACT header (Skill, Topic, Category, Date,
Status: MOCK); (3) each has an extended inertia statement that names both the skeleton
phrase and a topic-specific instance; (4) each body is 3-5 sentences, vocabulary-compliant,
register-matched, grounded in the extended inertia statement; (5) every REAL-REQUIRED = YES
namespace has a REAL-REQUIRED statement with rationale.**

---

### ROLE 3 -- SUMMARIZER

You ARE the SUMMARIZER. Produce the coverage summary table only. Writing a handoff section
here means you have become the HANDOFF WRITER, which you are not yet. You summarize.
Nothing else.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
- REAL-REQUIRED: all EVIDENCE-HEAVY namespaces; all compliance-active namespaces
- TIER-2-CRITICAL: trace at tier >= 2; scout-feasibility at tier >= 2
- TIER-3-CRITICAL: listen at tier >= 2
- Multiple flags: comma-separated
- No applicable flag: --

Recommended Next Step: derive from the extended inertia statement for this namespace from
ROLE 2. The step must name the skill that closes the specific gap identified in that
statement. Format: `/namespace:skill {topic}`. A recommendation valid for any topic without
reference to the inertia statement is not valid here -- inertia-disconnected next step
fails this gate.

**ROLE 3 STOP -- Do not activate ROLE 4 -- HANDOFF WRITER until: (1) nine rows present;
(2) each row has Category matching ROLE 1; (3) each row has all applicable Flags;
(4) each Recommended Next Step is derived from the ROLE 2 extended inertia statement and
names a specific skill invocation.**

---

### ROLE 4 -- HANDOFF WRITER

You ARE the HANDOFF WRITER. Write only the handoff section below. You write the handoff.
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

## V-02 -- Output Format: Verbatim Column Headers in ROLE 1 Stop-Gate (Single Axis)

**axis:** output-format (ROLE 1 stop-gate enumerates the classification table's own column
headers verbatim as its required completeness fields; column headers are declared in the
table definition before the gate references them; no other structural change)
**hypothesis:** C-27 requires the stop-gate to name the table's own column headers verbatim.
This creates structural self-reference: the gate text must match the column text. V-02
tests whether writing the column headers explicitly at table declaration time, then writing
the ROLE 1 stop-gate to reference those exact names, produces a C-27 pass. The column
declaration approach also satisfies C-11 and C-14 as a side effect (columns committed
before bodies; explicit gate phrase). C-26 is not structurally targeted -- the skeleton
cells are written by the model during ROLE 1 with a fill instruction, not pre-seeded in
the template; whether they are namespace-specific depends on model execution.
**predicted:** C-01 through C-25: PASS (structure matches R11 ceiling V-02). C-26: UNCERTAIN
(skeleton cells instructed but not pre-seeded; cells may be generic or specific depending
on model output). C-27: PASS (stop-gate names verbatim column headers). Score: 18/19 if
C-26 uncertain resolves to PASS; 17/19 if C-26 resolves to PARTIAL.
**failure condition:** C-27 FAIL if the stop-gate paraphrases rather than quotes the column
headers. Diagnostic test: copy the gate field names and compare character-by-character to
the declared column headers. Any synonym or abbreviation is a fail.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} -- read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier for {topic} and any compliance tags.
State at top of output: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs four sequential roles: CLASSIFIER, GENERATOR, SUMMARIZER, HANDOFF WRITER.
Each role has a named identity. You ARE each role while it is active -- not as a process
position but as an ontological state. Producing output belonging to a different role is
an identity failure: you have ceased to be who you are and have become something you are
not yet. Each role begins at its named header and ends at its STOP gate. Do not cross a
STOP gate until its conditions are fully met.

---

### ROLE 1 -- CLASSIFIER

You ARE the CLASSIFIER. Your sole output is the classification table below, fully populated.
Writing an artifact body here means you are no longer the CLASSIFIER -- you have become the
GENERATOR, which you are not yet.
You classify. Nothing else.

Classification rules:
- EVIDENCE-HEAVY: prove, listen
- HIGH-STRUCTURE: trace, flow
- MIXED: scout, draft, review, program, topic

REAL-REQUIRED rationale (applies to all EVIDENCE-HEAVY and compliance-active namespaces):
A synthetic artifact cannot substitute for real signal. prove-* requires actual experiment
data or prototype outputs. listen-* requires real user interviews or adoption measurements.
Compliance-active namespaces require traceable real-world sources.

The classification table has exactly these columns, in this order:
  Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED | Inertia gap skeleton

Fill each cell according to the rules above. For "Inertia gap skeleton," write a
namespace-specific phrase of the form "Without this signal, {topic}'s story would be
missing: [namespace-specific gap phrase]" with the blank filled at the namespace level
(topic-independent; topic specificity is added in ROLE 2).

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED | Inertia gap skeleton |
|-----------|----------|----------|------------|-------------------|-------------------|---------------|----------------------|
| scout | ... | ... | ... | ... | ... | ... | ... |
| draft | ... | ... | ... | ... | ... | ... | ... |
| review | ... | ... | ... | ... | ... | ... | ... |
| flow | ... | ... | ... | ... | ... | ... | ... |
| trace | ... | ... | ... | ... | ... | ... | ... |
| prove | ... | ... | ... | ... | ... | ... | ... |
| listen | ... | ... | ... | ... | ... | ... | ... |
| program | ... | ... | ... | ... | ... | ... | ... |
| topic | ... | ... | ... | ... | ... | ... | ... |

**ROLE 1 STOP -- Do not activate ROLE 2 -- GENERATOR until all nine rows have values in
every one of the following columns: Namespace, Category, MUST use, DO NOT use,
Tier 2/3 Critical, Compliance-Tagged, REAL-REQUIRED, Inertia gap skeleton. Any cell
containing "..." or left empty fails this gate. The column names above are the required
field names -- use them verbatim when assessing completeness.**

---

### ROLE 2 -- GENERATOR

You ARE the GENERATOR. Produce nine namespace artifact sections, one per ROLE 1 row, in
table order. Writing a coverage summary here means you are no longer the GENERATOR -- you
have become the SUMMARIZER, which you are not yet.
You generate. Nothing else.

Before writing each artifact body, answer the inertia question for that namespace by
extending the skeleton phrase from the ROLE 1 "Inertia gap skeleton" column:

> Without this signal, {topic}'s feature story would be missing: {skeleton phrase from
> ROLE 1} -- specifically, {one clause naming the topic-specific instance of that gap}.

Write the completed inertia statement immediately before the body. The body must be
traceable to this statement -- a body that could have been written without reading the
statement is too generic and must be revised.

For each namespace:

  #### {Namespace} -- {representative-skill-name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{representative-skill-name}
  Topic:    {topic}
  Category: {from ROLE 1 table -- column: Category}
  Date:     {current date}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {skeleton phrase from ROLE 1 Inertia gap skeleton column} -- specifically,
  {topic-specific clause}

  {3-5 sentence artifact body -- register matches Category column from ROLE 1;
  HIGH-STRUCTURE: contract/specification language; EVIDENCE-HEAVY: study/data language;
  MIXED: discovery/signal language; apply MUST use vocabulary, avoid DO NOT use vocabulary;
  body grounded in the extended inertia statement above}

  [If REAL-REQUIRED column = YES:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {one sentence -- prove: requires actual experiment data; listen: requires real
  user feedback; compliance namespace: requires traceable real-world sources.}

**ROLE 2 STOP -- Do not activate ROLE 3 -- SUMMARIZER until: (1) nine artifact sections
present; (2) each has a complete MOCK ARTIFACT header; (3) each has a completed inertia
statement extending the ROLE 1 skeleton phrase; (4) each body is 3-5 sentences,
vocabulary-compliant per ROLE 1 columns, register-matched; (5) every REAL-REQUIRED YES row
has its REAL-REQUIRED statement.**

---

### ROLE 3 -- SUMMARIZER

You ARE the SUMMARIZER. Produce the coverage summary table only. Writing a handoff section
here means you are no longer the SUMMARIZER -- you have become the HANDOFF WRITER, which
you are not yet.
You summarize. Nothing else.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
- REAL-REQUIRED: all EVIDENCE-HEAVY namespaces; all compliance-active namespaces
- TIER-2-CRITICAL: trace at tier >= 2; scout-feasibility at tier >= 2
- TIER-3-CRITICAL: listen at tier >= 2
- Multiple flags: comma-separated
- No applicable flag: --

Recommended Next Step: derive from the ROLE 2 extended inertia statement for this
namespace. The step must name the skill that closes the specific gap. Format:
`/namespace:skill {topic}`. A recommendation valid for any topic without reference to the
inertia statement fails this gate.

**ROLE 3 STOP -- Do not activate ROLE 4 -- HANDOFF WRITER until: (1) nine rows present;
(2) each row's Category matches the ROLE 1 Category column value; (3) each row has all
applicable Flags; (4) each Recommended Next Step is derived from the ROLE 2 inertia
statement for that namespace.**

---

### ROLE 4 -- HANDOFF WRITER

You ARE the HANDOFF WRITER. Write only the handoff section below. You write the handoff.
Nothing else.

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

Replace {topic} and {date} with actual values.
DO NOT write `{this-file}` as a literal placeholder.
DO NOT write any other content in this section.

---

---

## V-03 -- Phrasing Register: Conversational Descriptive (Single Axis)

**axis:** phrasing-register (conversational first-person descriptive framing throughout;
imperative command blocks replaced with narrative explanation; stop-gates phrased as
"before I proceed" rather than "Do not activate"; role identity expressed as "my job is"
rather than "You ARE")
**hypothesis:** C-26 and C-27 are structural criteria, not register criteria -- a
conversational skill that provides the same structural elements should pass both. The
question is whether conversational framing tends to lose the structural specificity that
C-26 and C-27 require. Specifically: (1) C-26 requires namespace-specific skeleton cells
at construction time -- conversational framing may produce vaguer filler since no explicit
seed phrases are provided and the instruction is softer; (2) C-27 requires verbatim column
names in the gate -- conversational framing naturally paraphrases ("all eight fields") rather
than quoting. V-03 tests the ceiling for conversational register on these two criteria.
**predicted:** C-01 through C-25: most PASS (structure preserved). C-24 and C-25: PARTIAL --
"my job is" and "I am acting as" are occupancy-language; being-language requires "I AM the
CLASSIFIER" not "my role here is classifier." C-26: PARTIAL (conversational fill instruction
likely produces generic phrases rather than namespace-specific seeds). C-27: FAIL
(conversational gates almost never quote verbatim column names). Score: ~15/19.
**failure condition:** The conversational register diagnoses the floor: a skill that does not
pass C-24, C-25, C-26, or C-27 in conversational form confirms that all four criteria
require specific structural choices beyond what natural prose produces.

---

You are running /mock:all.

I'll use this topic with all nine namespaces to produce a complete mock coverage picture.

First, let me check TOPICS.md to find the tier and compliance tags for {topic}, then note
this at the top of my output.

Here's how I'll approach this in four passes:

---

**Pass 1 -- Classify**

My job in this pass is to assign each namespace its category, vocabulary rules, tier
criticality, compliance status, and inertia skeleton. I'm not writing artifact content yet.

Categories I use:
- EVIDENCE-HEAVY for prove and listen (these get flagged REAL-REQUIRED automatically)
- HIGH-STRUCTURE for trace and flow
- MIXED for scout, draft, review, program, topic

Let me fill in the classification table before moving on:

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED | What's missing without it |
|-----------|----------|----------|------------|-------------------|-------------------|---------------|---------------------------|
| scout | MIXED | discovery language, signals, directional hypotheses | pure spec language only | no | yes if --compliance active | no unless compliance-tagged | ... |
| draft | MIXED | structural scaffold, acceptance criteria | pure spec language only | no | no | no | ... |
| review | MIXED | qualitative observations, design judgments | pure spec language only | no | no | no | ... |
| flow | HIGH-STRUCTURE | state transitions, trigger conditions, data flow contracts | interview language, user quotes | no | no | no | ... |
| trace | HIGH-STRUCTURE | interfaces, component boundaries, contracts | interview language, adoption rates | yes if tier >= 2 | yes if --compliance active | no unless compliance-tagged | ... |
| prove | EVIDENCE-HEAVY | study framing, hypothesis-and-result, N-of-M | spec language, schema definitions | no | no | yes | ... |
| listen | EVIDENCE-HEAVY | adoption rates, user interview framing | spec language, state machine language | yes if tier >= 2 | no | yes | ... |
| program | MIXED | milestones, owners, dependencies, qualitative rationale | pure spec language only | no | no | no | ... |
| topic | MIXED | signal synthesis, coverage reference | pure spec language alone | no | no | no | ... |

Before I write any artifact content, I need all eight fields filled for all nine rows,
including a specific phrase in the "What's missing without it" column that describes what
each namespace uniquely contributes at the namespace level.

---

**Pass 2 -- Generate**

My job here is to write one artifact section per namespace. For each one I'll extend the
skeleton phrase from Pass 1 with a topic-specific clause, then write the artifact body
grounded in that answer. 3-5 sentences per body, vocabulary-compliant, register-matched.

For each namespace:

  #### {Namespace} -- {representative-skill-name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{representative-skill-name}
  Topic:    {topic}
  Category: {from Pass 1}
  Date:     {current date}
  Status:   MOCK

  **Without this signal, {topic}'s story would be missing:**
  {skeleton phrase extended with topic-specific clause}

  {3-5 sentence artifact body, grounded in the inertia statement above, vocabulary-compliant}

  [if REAL-REQUIRED = yes] REAL-REQUIRED: A synthetic artifact cannot substitute for real
  signal here. Rationale: {one sentence specific to this namespace type}.

I won't move to Pass 3 until all nine sections are written and each body is traceable to
its inertia statement.

---

**Pass 3 -- Summarize**

My job here is to produce the coverage summary table. Each row gets its Flag and a
recommended next step derived from the Pass 2 inertia statement for that namespace.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

I won't write the handoff section in this pass.

---

**Pass 4 -- Handoff**

My job here is only the handoff line.

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

Replace {topic} and {date} with actual values.
DO NOT write `{this-file}` literally.

---

---

## V-04 -- Combination: Template-Seeded Skeleton + Verbatim Stop-Gate (C-26 + C-27 Ceiling)

**axis:** combination (V-01 template-seeded skeleton cells + V-02 verbatim stop-gate column
reference; both new v12 criteria targeted simultaneously at maximum structural strength)
**hypothesis:** C-26 and C-27 can be satisfied independently (V-01 targets C-26; V-02 targets
C-27). V-04 tests whether satisfying both simultaneously creates any structural tension or
whether they compose cleanly. The template-seed approach (V-01) provides the skeleton cells
before ROLE 1 executes, ensuring namespace-specific content at construction time. The
verbatim-gate approach (V-02) requires the ROLE 1 stop-gate to name the declared column
headers exactly as written. The two approaches reinforce the same structural chain: columns
declared -> cells seeded with specific content -> gate names those columns verbatim -> ROLE 2
extends topic-specifically -> ROLE 3 derives next steps from extended inertia.
**predicted:** C-01 through C-25: PASS (structure includes all prior ceiling elements including
C-24 and C-25 being-language). C-26: PASS (template provides seed phrases; model reads them
into table). C-27: PASS (gate names table column headers verbatim). Score: 19/19 aspirational.
**failure condition:** C-26 PARTIAL if the model replaces the provided seed phrases with its
own generic version. C-27 FAIL if the gate text drifts from the declared column header names
(e.g., "Inertia gap skeleton" in the table but "skeleton column" in the gate).

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} -- read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier for {topic} and any compliance tags.
State at top of output: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs four sequential roles: CLASSIFIER, GENERATOR, SUMMARIZER, HANDOFF WRITER.
You ARE each role while it is active. This is an identity statement. Each role is a distinct
entity. The CLASSIFIER cannot generate artifact bodies because generating artifact bodies
means the CLASSIFIER has ceased to exist and the GENERATOR has taken its place -- and the
GENERATOR does not yet exist at ROLE 1 time. Wrong-phase output is not a sequencing error:
it is an ontological contradiction. Each role begins at its named header and ends at its
STOP gate. Do not cross a STOP gate until its conditions are fully met.

---

### ROLE 1 -- CLASSIFIER

You ARE the CLASSIFIER. Your sole output is the classification table below, fully populated.
Writing an artifact body here means you are no longer the CLASSIFIER -- you have become the
GENERATOR, which you are not yet. Writing a coverage summary means you have become the
SUMMARIZER, which you are not yet. Writing a handoff means you have become the HANDOFF
WRITER, which you are not yet.
You classify. Nothing else.

Classification rules:
- EVIDENCE-HEAVY: prove, listen
- HIGH-STRUCTURE: trace, flow
- MIXED: scout, draft, review, program, topic

REAL-REQUIRED rationale (applies to all EVIDENCE-HEAVY and compliance-active namespaces):
A synthetic artifact cannot substitute for real signal. prove-* requires actual experiment
data or prototype outputs. listen-* requires real user interviews or adoption measurements.
Compliance-active namespaces require traceable real-world sources -- synthetic artifacts
create false assurance regardless of structural quality.

The classification table has exactly these columns, in this order:
  Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED | Inertia gap skeleton

Inertia gap skeleton column: use the seed phrase provided below for each namespace.
DO NOT substitute a generic phrase. DO NOT write "TBD." Copy the seed phrase verbatim.
ROLE 2 will extend it with topic-specific content.

Seed phrases (copy verbatim into the "Inertia gap skeleton" column):
- scout:   directional market signals and competitor positioning
- draft:   the structural shape of the feature and its core acceptance criteria
- review:  design quality judgment and stakeholder risk flags
- flow:    the state transition contract and trigger conditions
- trace:   the component boundary contract and integration failure modes
- prove:   empirical validation of the core hypothesis
- listen:  real adoption evidence and friction points from actual users
- program: delivery milestones, owner assignments, and sequencing rationale
- topic:   a unified coverage signal that shows which namespaces are ready

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED | Inertia gap skeleton |
|-----------|----------|----------|------------|-------------------|-------------------|---------------|----------------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language only; pure study methodology framing only | NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES | directional market signals and competitor positioning |
| draft | MIXED | structural scaffold: sections, properties, acceptance criteria; qualitative observations | pure specification language only; pure study methodology framing only | NO | NO | NO | the structural shape of the feature and its core acceptance criteria |
| review | MIXED | qualitative observations; design judgments; structural rationale | pure specification language only; pure study methodology framing only | NO | NO | NO | design quality judgment and stakeholder risk flags |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language; user quotes; adoption percentages; study framing | NO | NO | NO | the state transition contract and trigger conditions |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language; adoption rates; user quotes; study framing | YES if tier >= 2; else NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES | the component boundary contract and integration failure modes |
| prove | EVIDENCE-HEAVY | study/data framing: "N of M tests showed...", "prototype against {topic} produced...", hypothesis-and-result | specification language; schema definitions; contract structures | NO | NO | YES | empirical validation of the core hypothesis |
| listen | EVIDENCE-HEAVY | study/data framing: adoption rates, "N users found...", survey response framing | specification language; state machine language; schema definitions | YES if tier >= 2; else NO | NO | YES | real adoption evidence and friction points from actual users |
| program | MIXED | structural scaffold: milestones, owners, dependencies; qualitative rationale | pure specification language only; pure study methodology framing only | NO | NO | NO | delivery milestones, owner assignments, and sequencing rationale |
| topic | MIXED | signal synthesis narrative; structured coverage reference | pure specification language alone | NO | NO | NO | a unified coverage signal that shows which namespaces are ready |

**ROLE 1 STOP -- Do not activate ROLE 2 -- GENERATOR until all nine rows have values in
every one of the following columns (column names are verbatim from the table above):
Namespace, Category, MUST use, DO NOT use, Tier 2/3 Critical, Compliance-Tagged,
REAL-REQUIRED, Inertia gap skeleton. Any cell containing "..." or left empty fails this
gate. Any "Inertia gap skeleton" cell that does not match the seed phrase provided above
fails this gate.**

---

### ROLE 2 -- GENERATOR

You ARE the GENERATOR. Produce nine namespace artifact sections, one per ROLE 1 row, in
table order. Writing a coverage summary here means you are no longer the GENERATOR -- you
have become the SUMMARIZER, which you are not yet.
You generate. Nothing else.

Before writing each artifact body, extend the ROLE 1 inertia skeleton for this namespace:

> Without this signal, {topic}'s feature story would be missing: {Inertia gap skeleton cell
> from ROLE 1} -- specifically, {one clause naming the topic-specific instance of that gap}.

Write the completed inertia statement immediately before the body. The body must be
traceable to the completed statement -- a body that could have been written without reading
the statement is too generic and must be revised.

For each namespace:

  #### {Namespace} -- {representative-skill-name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{representative-skill-name}
  Topic:    {topic}
  Category: {from ROLE 1 -- Inertia gap skeleton column}
  Date:     {current date}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {Inertia gap skeleton cell from ROLE 1} -- specifically, {topic-specific clause}

  {3-5 sentence artifact body -- register matches Category from ROLE 1:
  HIGH-STRUCTURE uses contract/specification language;
  EVIDENCE-HEAVY uses study/data language;
  MIXED uses discovery/signal language;
  apply MUST use vocabulary from ROLE 1, avoid DO NOT use vocabulary from ROLE 1;
  body must be grounded in the completed inertia statement above; a body valid for any
  topic without using the inertia statement fails this gate}

  [If REAL-REQUIRED column = YES in ROLE 1:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {one sentence -- prove: requires actual experiment data; listen: requires real
  user feedback; compliance namespace: requires traceable real-world sources.}

**ROLE 2 STOP -- Do not activate ROLE 3 -- SUMMARIZER until: (1) nine artifact sections
present; (2) each has a complete MOCK ARTIFACT header with Skill, Topic, Category, Date,
Status: MOCK; (3) each has a completed inertia statement that extends the ROLE 1
Inertia gap skeleton cell with a topic-specific clause; (4) each body is 3-5 sentences,
vocabulary-compliant per ROLE 1 MUST use and DO NOT use columns, register-matched to
the Category column; (5) every row where REAL-REQUIRED = YES has a REAL-REQUIRED statement
with rationale.**

---

### ROLE 3 -- SUMMARIZER

You ARE the SUMMARIZER. Produce the coverage summary table only. Writing a handoff here
means you are no longer the SUMMARIZER -- you have become the HANDOFF WRITER, which you
are not yet.
You summarize. Nothing else.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
- REAL-REQUIRED: all EVIDENCE-HEAVY namespaces; all compliance-active namespaces
- TIER-2-CRITICAL: trace at tier >= 2; scout-feasibility at tier >= 2
- TIER-3-CRITICAL: listen at tier >= 2
- Multiple flags: comma-separated
- No applicable flag: --

Recommended Next Step: derive from the ROLE 2 completed inertia statement for this
namespace -- the skill call that closes the specific gap named in that statement.
Format: `/namespace:skill {topic}`. A recommendation that does not name a skill derived
from the inertia statement is not valid here. Inertia-disconnected next step fails this gate.

**ROLE 3 STOP -- Do not activate ROLE 4 -- HANDOFF WRITER until: (1) nine rows present;
(2) each row's Category value matches the Category column value in ROLE 1; (3) each row
has all applicable Flags per the flag rules above; (4) each Recommended Next Step names
a specific skill call derived from the ROLE 2 inertia statement for that row's namespace.**

---

### ROLE 4 -- HANDOFF WRITER

You ARE the HANDOFF WRITER. Write only the handoff section below. You write the handoff.
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

## V-05 -- Combination: Verbatim Gate + Lifecycle Emphasis (Explicit Column Declaration Step)

**axis:** combination (V-02 verbatim stop-gate + lifecycle emphasis; an explicit
column-declaration step precedes ROLE 1 table generation; the model commits to column
names before filling cells and before writing the gate; this creates the C-27 structural
self-reference cascade as a side effect of lifecycle ordering)
**hypothesis:** C-27's side-effect cascade -- that a gate naming verbatim columns cannot be
written before those columns are declared -- can be operationalized directly by adding an
explicit column-declaration step at the start of ROLE 1. The model first outputs the column
list (making column names canonical), then fills the table using those canonical names, then
the gate references those names verbatim. This is distinct from V-02 (which pre-declares
columns in the skill template) and from V-04 (which combines template seeds with verbatim
gate). V-05 tests whether making column commitment an explicit runtime step, rather than a
template-design choice, is sufficient for C-27. C-26 is secondary: without template-seeded
phrases (V-01 and V-04), the skeleton cells are model-generated and may or may not be
namespace-specific.
**predicted:** C-01 through C-25: PASS (all prior ceiling elements preserved including C-24
and C-25 being-language). C-26: UNCERTAIN (no template seeds; model fills skeleton during
ROLE 1 declaration step; quality depends on how specific the model-generated phrases are).
C-27: PASS (column-declaration step makes column names canonical before gate is written;
gate references those names verbatim). Score: 18-19/19 depending on C-26 resolution.
**failure condition:** C-26 PARTIAL if the explicit column-declaration step does not constrain
skeleton cell content to be namespace-specific -- the model may treat "fill the skeleton
column" as permission to write generic phrases. C-27 FAIL if the gate text drifts from
the column names established in the declaration step.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} -- read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier for {topic} and any compliance tags.
State at top of output: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs four sequential roles: CLASSIFIER, GENERATOR, SUMMARIZER, HANDOFF WRITER.
You ARE each role while it is active. This is an identity statement, not a process position.
Each role is a distinct entity; wrong-phase output means the current entity has ceased to
exist and a future entity has taken its place before being activated. Do not cross a STOP
gate until its conditions are fully met.

---

### ROLE 1 -- CLASSIFIER

You ARE the CLASSIFIER. Writing an artifact body here means you are no longer the CLASSIFIER
-- you have become the GENERATOR, which you are not yet. Writing a coverage summary means
you are no longer the CLASSIFIER -- you have become the SUMMARIZER, which you are not yet.
You classify. Nothing else.

**Step 1a -- Declare column names.**

Before filling the classification table, output the following column name commitment block
exactly as shown. This commits the canonical column names that the ROLE 1 STOP gate will
reference verbatim:

```
COLUMN NAMES (canonical -- referenced verbatim by ROLE 1 STOP gate):
  1. Namespace
  2. Category
  3. MUST use
  4. DO NOT use
  5. Tier 2/3 Critical
  6. Compliance-Tagged
  7. REAL-REQUIRED
  8. Inertia gap skeleton
```

Do not proceed to Step 1b until this block is written.

**Step 1b -- Fill the classification table.**

Classification rules:
- EVIDENCE-HEAVY: prove, listen
- HIGH-STRUCTURE: trace, flow
- MIXED: scout, draft, review, program, topic

REAL-REQUIRED rationale (applies to all EVIDENCE-HEAVY and compliance-active namespaces):
A synthetic artifact cannot substitute for real signal. prove-* requires actual experiment
data or prototype outputs. listen-* requires real user interviews or adoption measurements.
Compliance-active namespaces require traceable real-world sources.

For the "Inertia gap skeleton" column: write a namespace-specific phrase of the form
"Without this signal, {topic}'s story would be missing: [namespace gap phrase]" where
the gap phrase characterizes what this namespace uniquely contributes at the namespace
level, independent of any specific topic. ROLE 2 will extend this phrase with topic-specific
content. DO NOT write "TBD" or a generic filler -- a namespace-specific gap phrase is required.

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED | Inertia gap skeleton |
|-----------|----------|----------|------------|-------------------|-------------------|---------------|----------------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language only; pure study methodology framing only | NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES | {namespace-specific gap phrase -- see instruction above} |
| draft | MIXED | structural scaffold: sections, properties, acceptance criteria; qualitative observations | pure specification language only; pure study methodology framing only | NO | NO | NO | {namespace-specific gap phrase} |
| review | MIXED | qualitative observations; design judgments; structural rationale | pure specification language only; pure study methodology framing only | NO | NO | NO | {namespace-specific gap phrase} |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language; user quotes; adoption percentages; study framing | NO | NO | NO | {namespace-specific gap phrase} |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language; adoption rates; user quotes; study framing | YES if tier >= 2; else NO | YES if --compliance or TOPICS.md tag; else NO | NO unless Compliance-Tagged YES | {namespace-specific gap phrase} |
| prove | EVIDENCE-HEAVY | study/data framing: "N of M tests showed...", "prototype against {topic} produced...", hypothesis-and-result | specification language; schema definitions; contract structures | NO | NO | YES | {namespace-specific gap phrase} |
| listen | EVIDENCE-HEAVY | study/data framing: adoption rates, "N users found...", survey response framing | specification language; state machine language; schema definitions | YES if tier >= 2; else NO | NO | YES | {namespace-specific gap phrase} |
| program | MIXED | structural scaffold: milestones, owners, dependencies; qualitative rationale | pure specification language only; pure study methodology framing only | NO | NO | NO | {namespace-specific gap phrase} |
| topic | MIXED | signal synthesis narrative; structured coverage reference | pure specification language alone | NO | NO | NO | {namespace-specific gap phrase} |

**ROLE 1 STOP -- Do not activate ROLE 2 -- GENERATOR until all nine rows have values in
every one of the following columns (names taken verbatim from the Step 1a column name
commitment block): Namespace, Category, MUST use, DO NOT use, Tier 2/3 Critical,
Compliance-Tagged, REAL-REQUIRED, Inertia gap skeleton. Any cell containing
"{namespace-specific gap phrase}" as a literal or left empty fails this gate. Any
Inertia gap skeleton cell that does not name a namespace-level gap characterization
(topic-independent) fails this gate.**

---

### ROLE 2 -- GENERATOR

You ARE the GENERATOR. Produce nine namespace artifact sections, one per ROLE 1 row, in
table order. Writing a coverage summary here means you are no longer the GENERATOR -- you
have become the SUMMARIZER, which you are not yet.
You generate. Nothing else.

Before writing each artifact body, extend the ROLE 1 Inertia gap skeleton value for this
namespace with a topic-specific clause:

> Without this signal, {topic}'s feature story would be missing: {Inertia gap skeleton
> from ROLE 1} -- specifically, {one clause naming the topic-specific instance of that gap}.

Write this completed statement immediately before the artifact body. The body must be
traceable to this statement -- a body that could have been written without reading the
completed statement is too generic and must be revised.

For each namespace:

  #### {Namespace} -- {representative-skill-name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{representative-skill-name}
  Topic:    {topic}
  Category: {from ROLE 1 Category column}
  Date:     {current date}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {Inertia gap skeleton from ROLE 1} -- specifically, {topic-specific clause}

  {3-5 sentence artifact body -- register matches Category column from ROLE 1:
  HIGH-STRUCTURE uses contract/specification language;
  EVIDENCE-HEAVY uses study/data language;
  MIXED uses discovery/signal language;
  apply MUST use vocabulary, avoid DO NOT use vocabulary;
  body grounded in the completed inertia statement; cannot be valid for any topic
  without using the inertia answer}

  [If REAL-REQUIRED = YES:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {one sentence -- prove: requires actual experiment data; listen: requires real
  user feedback; compliance namespace: requires traceable real-world sources.}

**ROLE 2 STOP -- Do not activate ROLE 3 -- SUMMARIZER until: (1) nine artifact sections
present; (2) each has a complete MOCK ARTIFACT header; (3) each has a completed inertia
statement extending the ROLE 1 Inertia gap skeleton with a topic-specific clause; (4) each
body is 3-5 sentences, vocabulary-compliant per ROLE 1 columns, register-matched to the
Category column; (5) every REAL-REQUIRED YES row has its REAL-REQUIRED statement.**

---

### ROLE 3 -- SUMMARIZER

You ARE the SUMMARIZER. Produce the coverage summary table only. Writing a handoff here
means you are no longer the SUMMARIZER -- you have become the HANDOFF WRITER, which you
are not yet.
You summarize. Nothing else.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
- REAL-REQUIRED: all EVIDENCE-HEAVY namespaces; all compliance-active namespaces
- TIER-2-CRITICAL: trace at tier >= 2; scout-feasibility at tier >= 2
- TIER-3-CRITICAL: listen at tier >= 2
- Multiple flags: comma-separated
- No applicable flag: --

Recommended Next Step: derive from the ROLE 2 completed inertia statement for this
namespace -- specifically the skill that closes the gap named in the topic-specific clause.
Format: `/namespace:skill {topic}`. Inertia-disconnected next step fails this gate.

**ROLE 3 STOP -- Do not activate ROLE 4 -- HANDOFF WRITER until: (1) nine rows present;
(2) each row's Category matches the ROLE 1 Category column; (3) each row has all applicable
Flags; (4) each Recommended Next Step derives from the ROLE 2 inertia statement for that
namespace and names a specific skill call.**

---

### ROLE 4 -- HANDOFF WRITER

You ARE the HANDOFF WRITER. Write only the handoff section below. You write the handoff.
Nothing else.

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

Replace {topic} and {date} with actual values before writing this section.
DO NOT write `{this-file}` as a literal placeholder.
DO NOT write any other content in this section.

---
