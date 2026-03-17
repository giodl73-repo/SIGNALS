---
skill: quest-variate
skill_target: mock-all
date: 2026-03-15
round: 6
rubric_version: v6
status: VARIATE
---

# mock-all Variate — Round 6

**Date:** 2026-03-15
**Skill:** mock-all
**Rubric:** v6 (C-01 through C-18; aspirational denominator = 12)
**Round:** R6 — C-18 formalized from R5 evidence; three new single axes isolated

---

## What R5 Left Open

v6 adds C-18 (named role-identity per phase). R5 V-01/V-04/V-05 demonstrated the behavior
C-18 captures: role label as identity constraint, not step label. R5 V-02 demonstrated a
co-located template depth anchor solving C-07 PARTIAL. R5 V-03 demonstrated inertia framing
as a semantic quality anchor — but failed C-17 (vocab rules in prose, not table columns).

Three new axes enter R6 as single-axis variations, now that their behavior is rubric-encoded:

| Question | R5 state | R6 target |
|----------|----------|-----------|
| Does "You ARE the CLASSIFIER" (identity constraint) reliably prevent artifact-body production in ROLE 1, beyond what stop-gate sentences alone enforce? | R5 V-01 demonstrated this; C-18 formalizes it | V-01 — minimal identity framing, isolate the C-18 mechanism |
| Does a `{3-5 sentence body using [CATEGORY] register}` placeholder — co-located inside the template — force C-07 compliance more reliably than vocab rules in a prose block or classification table? | R5 V-02 demonstrated this; never combined with role-identity | V-02 — role-identity + co-located template anchor |
| Does inertia framing ("without this signal, {topic}'s story is missing...") elevate C-07/C-10 quality above what structural vocabulary rules alone produce? | R5 V-03 tested this but failed C-17; fixed here by adding vocab columns | V-03 — role-identity + inertia framing + vocab columns (closed C-17 miss) |

---

## Axis-Assignment Plan

| Plan | Axis | Source signal | Target criteria | Predicted |
|------|------|---------------|-----------------|-----------|
| V-01 | role-sequence (identity constraint) | C-18 formalizes what R5 V-01 demonstrated: role label must make wrong-phase output an identity violation, not a procedure violation. Variation from R5: the identity framing is made even more explicit — "The moment you write an artifact body here, you are acting as ROLE 2, which you are not" — to isolate whether identity constraint language adds enforcement over stop-gate phrases alone. Vocab columns in table (C-17). Enumerated but compact stop-gate fields (C-16). | C-18 (primary), C-14, C-16, C-17 | 100 |
| V-02 | output-format (co-located template depth anchor) | R5 V-02 showed `{3-5 sentence body}` inside the template placeholder enforces C-07 depth at generation time; prose-level depth guidance does not. R5 V-02 used conversational register, not role-identity — the co-location effect was confounded with register. R6 V-02 isolates the template axis: role-identity is present (C-18 passes), vocabulary rules move from table columns into the template placeholder itself. Tests whether in-template vocabulary enforcement is equivalent to or stronger than table-column enforcement for C-07/C-15 compliance. | C-07 (primary), C-15, C-18 | 100 |
| V-03 | inertia-framing (upgraded) | R5 V-03 tested inertia framing without vocabulary columns: C-17 FAIL, score 98.9. R6 V-03 adds vocabulary columns to close C-17, keeping inertia framing as the isolate. The test: does "without this signal, the feature story for {topic} would be missing: [X]" produce richer C-07 bodies and sharper C-10 next steps than a structurally equivalent variation (V-01) without inertia priming? | C-17 (fix R5 V-03 miss), C-07/C-10 quality, C-18 | 100 |
| V-04 | role-sequence + lifecycle-emphasis | Combines V-01's identity constraint framing with stop-gate phrases that enumerate every specific output field. The ROLE STOP language names all required fields: "all nine namespaces must have Category, MUST-use vocabulary, DO NOT-use vocabulary, Tier 2/3 Critical (YES/NO), Compliance-Tagged (YES/NO), and REAL-REQUIRED (YES/NO) before ROLE 2 activates." Tests whether field-level enumeration adds measurable enforcement over V-01's role-identity gates alone. | C-16 (primary), C-18, C-14, C-17 | 100 |
| V-05 | role-sequence + output-format + inertia-framing | Full synthesis: V-01 role-identity + V-02 co-located template + V-03 inertia framing. The GENERATOR role uses a template where the body placeholder carries both the inertia question and the vocabulary register cue co-located. Tests the ceiling behavior when all three axes are active simultaneously: identity prevents cross-role contamination; template anchor enforces depth at generation time; inertia framing ensures semantic weight. | C-07, C-10, C-15, C-18 ceiling | 100 |

---

## V-01 — Role Sequence: Identity Constraint Framing (Single Axis)

**axis:** role-sequence (identity constraint)
**hypothesis:** R5 V-01 demonstrated that CLASSIFIER/GENERATOR/SUMMARIZER/HANDOFF WRITER
labels prevent cross-phase contamination. C-18 formalizes this. The R6 variation isolates the
mechanism: explicit identity violation framing ("the moment you write an artifact body here,
you are acting as ROLE 2, which you are not yet") makes wrong-phase output an identity
contradiction, not a procedure violation. Stop-gate phrases are present (C-14) but compact —
the identity frame is the primary enforcement mechanism. Vocabulary rules anchor as table
columns (C-17). Stop-gate fields enumerated (C-16).
**predicted:** C-18 PASS (explicit role identity + violation framing), C-14 PASS (stop-gate
phrases at each boundary), C-16 PASS (fields enumerated in gates), C-17 PASS (vocab columns
in classification table), C-13 PASS (REAL-REQUIRED rationale at each application). All 12
criteria PASS. Score: 100.
**failure condition:** Identity constraint language is treated as decoration rather than a
genuine constraint — the model generates artifact bodies inside ROLE 1's output without
registering the identity violation. If this occurs, stop-gate phrases are the load-bearing
mechanism and identity framing adds no enforcement.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record tier for {topic} and any compliance tags.
State at top of output: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs four sequential roles. Each role has a distinct identity. You ARE that role
while it is active. Output that belongs to a later role produced during an earlier role is an
identity violation — you are not yet that role.

---

### ROLE 1 — CLASSIFIER

You are the CLASSIFIER. Your sole output is the classification table below, fully populated.

The moment you write an artifact body in this section, you are acting as ROLE 2 — GENERATOR,
which you are not yet. The moment you write a coverage summary, you are acting as ROLE 3 —
SUMMARIZER, which you are not yet. You classify. Nothing else.

Classification rules:
- EVIDENCE-HEAVY: prove, listen
- HIGH-STRUCTURE: trace, flow
- MIXED: scout, draft, review, program, topic

REAL-REQUIRED rationale (applies to all EVIDENCE-HEAVY namespaces):
A synthetic artifact cannot substitute for real signal. prove-* requires actual experiment
data or prototype outputs. listen-* requires real user interviews or adoption measurements.
When --compliance is active or TOPICS.md tags are present: scout-compliance and
trace-permissions are REAL-REQUIRED regardless of structural quality — compliance signals
require traceable real-world sources; synthetic artifacts here create false assurance.

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED |
|-----------|----------|----------|------------|-------------------|-------------------|---------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language only OR pure study methodology framing | NO | YES if compliance context active; else NO | NO (unless Compliance-Tagged YES) |
| draft | MIXED | structural scaffold (sections, properties, acceptance criteria) plus qualitative observations | pure specification language only OR pure study methodology framing | NO | NO | NO |
| review | MIXED | structural scaffold plus qualitative observations and design judgements | pure specification language only OR pure study methodology framing | NO | NO | NO |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language, user quotes, adoption percentages, study framing | NO | NO | NO |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language, adoption rates, user quotes, study framing | YES if tier >= 2; else NO | YES if compliance context active; else NO | NO (unless Compliance-Tagged YES) |
| prove | EVIDENCE-HEAVY | study/data/interview language: "N of M tests showed…", "Prototype against {topic} produced…", hypothesis-and-result framing | specification language, schema definitions, contract structures | NO | NO | YES |
| listen | EVIDENCE-HEAVY | study/data/interview language: adoption rates, "N users interviewed found…", survey response framing | specification language, state machine language, schema definitions | YES if tier >= 2; else NO | NO | YES |
| program | MIXED | structural scaffold (milestones, owners, dependencies) plus qualitative rationale | pure specification language only OR pure study methodology framing | NO | NO | NO |
| topic | MIXED | signal synthesis narrative plus structured coverage reference | pure specification language alone | NO | NO | NO |

**ROLE 1 STOP — Do not activate ROLE 2 until all nine namespaces have: Category,
MUST-use vocabulary, DO NOT-use vocabulary, Tier 2/3 Critical (YES/NO), Compliance-Tagged
(YES/NO), and REAL-REQUIRED (YES/NO) in the table above.**

---

### ROLE 2 — GENERATOR

You are the GENERATOR. Your sole output is nine namespace sections, one per row of the ROLE 1
table, in table order.

The moment you write a coverage summary here, you are acting as ROLE 3 — SUMMARIZER, which
you are not yet. The moment you write a handoff line, you are acting as ROLE 4 — HANDOFF
WRITER, which you are not yet. You generate. Nothing else.

Apply MUST-use and DO NOT-use vocabulary from the ROLE 1 table exactly. An artifact body
that uses DO NOT-use vocabulary is invalid and must be corrected before proceeding.

For each namespace:

  #### {Namespace} — {representative-skill-name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{representative-skill-name}
  Topic:    {topic}
  Category: {from ROLE 1 table}
  Date:     {current date}
  Status:   MOCK

  {artifact body — vocabulary-compliant with ROLE 1 MUST-use and DO NOT-use for this row}

  [If REAL-REQUIRED = YES in ROLE 1 table:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {one sentence specific to this namespace — prove: requires actual experiment
  data or prototype outputs; listen: requires real user interviews or adoption measurements;
  compliance namespace: requires traceable real-world compliance sources.}

**ROLE 2 STOP — Do not activate ROLE 3 until all nine namespaces have: a complete MOCK
ARTIFACT header block (all five fields), a vocabulary-compliant artifact body, and — for
every REAL-REQUIRED namespace — a rationale-accompanied REAL-REQUIRED statement.**

---

### ROLE 3 — SUMMARIZER

You are the SUMMARIZER. Your sole output is the coverage summary table. You do not write
additional artifact bodies. You do not write the handoff line. You summarize.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
- REAL-REQUIRED: all EVIDENCE-HEAVY namespaces; all compliance-context namespaces
- TIER-CRITICAL: trace-*, scout-feasibility, listen-* at tier >= 2
- Multiple flags: comma-separate (REAL-REQUIRED, TIER-CRITICAL)

Recommended Next Step: exact skill invocation — `/namespace:skill {topic}`. Not generic
advice ("gather signals"). Name the specific skill identifier.

**ROLE 3 STOP — Do not activate ROLE 4 until all nine namespaces appear in the coverage
table with correct Category, all applicable Flags, and a named Recommended Next Step.**

---

### ROLE 4 — HANDOFF WRITER

You are the HANDOFF WRITER. Your sole output is the handoff section. No artifact bodies.
No table rows. No other content.

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

Replace {topic} and {date} with actual values.
DO NOT write `{this-file}` as a literal placeholder.
DO NOT write any other content in this section.

---

---

## V-02 — Output Format: Co-located Template Depth Anchor (Single Axis)

**axis:** output-format (co-located template depth anchor)
**hypothesis:** R5 V-02 showed that vocabulary register and depth guidance co-located inside
the template placeholder (`{3-5 sentence body using…}`) produce better C-07 compliance than
the same guidance placed elsewhere. R5 V-02 confounded this with conversational phrasing
register. R6 V-02 isolates the axis: role-identity is present (C-18), stop-gates enumerate
fields (C-16), but vocabulary rules live inside the template body placeholder rather than as
table columns. The classification table is structurally simpler (no MUST/DO NOT columns) —
the model encounters vocabulary rules only at the moment it fills in the body placeholder.
**predicted:** C-18 PASS (role identity explicit), C-14 PASS (stop-gate phrases present),
C-16 PASS (fields enumerated), C-07 PASS (depth anchor in template), C-15 PASS (MUST/DO NOT
at generation point), C-17 PARTIAL-FAIL (vocabulary rules are in template, not in table
columns). Score: ~91.7 (11/12). Deliberate trade-off: tests whether in-template vocabulary
enforcement is a viable alternative to table-column enforcement for C-07 even at C-17 cost.
**failure condition:** Moving vocabulary rules out of the table into the template placeholder
causes the model to lose the category-to-vocabulary mapping — artifacts drift register because
the lookup is no longer pre-computed at classification time. If this occurs, table-column
enforcement (V-01) is structurally superior regardless of generation-time co-location.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record: tier for {topic}, compliance tags (if any).
State: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs four sequential roles. Each role holds a distinct identity. You ARE that
role while it is active. Producing output that belongs to a later role is a role violation.

---

### ROLE 1 — CLASSIFIER

You are the CLASSIFIER. Produce the classification table. Do not write artifact bodies.

Categories:
- EVIDENCE-HEAVY: prove, listen
- HIGH-STRUCTURE: trace, flow
- MIXED: scout, draft, review, program, topic

REAL-REQUIRED rationale: A synthetic artifact cannot substitute for real signal in
EVIDENCE-HEAVY namespaces. prove-* requires actual experiment data or prototype outputs.
listen-* requires real user interviews or adoption measurements. Compliance-active
namespaces (scout-compliance, trace-permissions) require traceable real-world sources.

| Namespace | Category | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED |
|-----------|----------|-------------------|-------------------|---------------|
| scout | MIXED | NO | YES if compliance context; else NO | NO (unless Compliance-Tagged YES) |
| draft | MIXED | NO | NO | NO |
| review | MIXED | NO | NO | NO |
| flow | HIGH-STRUCTURE | NO | NO | NO |
| trace | HIGH-STRUCTURE | YES if tier >= 2; else NO | YES if compliance context; else NO | NO (unless Compliance-Tagged YES) |
| prove | EVIDENCE-HEAVY | NO | NO | YES |
| listen | EVIDENCE-HEAVY | YES if tier >= 2; else NO | NO | YES |
| program | MIXED | NO | NO | NO |
| topic | MIXED | NO | NO | NO |

**ROLE 1 STOP — Do not activate ROLE 2 until all nine rows have Category, Tier 2/3 Critical
(YES/NO), Compliance-Tagged (YES/NO), and REAL-REQUIRED (YES/NO).**

---

### ROLE 2 — GENERATOR

You are the GENERATOR. Produce one artifact per namespace. Do not re-classify. Do not write
the coverage summary.

For each namespace, fill in the template below exactly as written. The placeholder text in the
body field shows the required form — replace it with actual content of that form. Do not copy
placeholder text into the output.

```
---
MOCK ARTIFACT
Skill:    {namespace}:{representative-skill-name}
Topic:    {topic}
Category: {Category from ROLE 1 — HIGH-STRUCTURE | EVIDENCE-HEAVY | MIXED}
Date:     {current date}
Status:   MOCK
---

{3-5 sentence artifact body. Register MUST match Category:
  HIGH-STRUCTURE  → MUST use: specification/contract framing —
                    "the component contract requires…", "the interface exposes…",
                    "schema defines field X as…", "state transition fires when…"
                    DO NOT use: user quotes, interview data, adoption rates, study framing
  EVIDENCE-HEAVY  → MUST use: study/experiment framing —
                    "N of M tests showed…", "prototype against {topic} produced…",
                    "interview participants reported…", "adoption rate of X%…"
                    DO NOT use: specification language, contract structures, schema definitions
  MIXED           → MUST use: discovery/signal language plus one structural element —
                    "signals suggest…", "three sources converge on…", "early indicators…"
                    DO NOT use: pure specification language; pure study methodology framing}

{If REAL-REQUIRED in ROLE 1 table:
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: [one sentence — prove: requires actual experiment data or prototype outputs;
  listen: requires real user interviews or adoption measurements;
  compliance namespace: requires traceable real-world sources]}
```

**ROLE 2 STOP — Do not activate ROLE 3 until all nine namespaces have: a complete MOCK
ARTIFACT header block (all five fields), a 3-5 sentence vocabulary-compliant body, and — for
every REAL-REQUIRED namespace — a rationale-accompanied REAL-REQUIRED statement.**

---

### ROLE 3 — SUMMARIZER

You are the SUMMARIZER. Produce the coverage summary table only.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flags: REAL-REQUIRED | TIER-CRITICAL | (both) | —
Recommended Next Step: specific skill call — `/namespace:skill {topic}`. Not generic.

**ROLE 3 STOP — Do not activate ROLE 4 until all nine rows have Flag and Recommended Next
Step values.**

---

### ROLE 4 — HANDOFF WRITER

You are the HANDOFF WRITER.

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

Replace {topic} and {date} with actual values.
DO NOT leave any placeholder as a literal string.

---

---

## V-03 — Inertia Framing Upgraded (Single Axis)

**axis:** inertia-framing (upgraded from R5 V-03)
**hypothesis:** R5 V-03 failed C-17 — inertia framing without vocabulary table columns.
R6 V-03 adds vocabulary columns (closing C-17) and keeps inertia framing as the isolated
axis. The inertia question — "Without this signal, {topic}'s feature story would be missing:"
— forces the artifact body to carry genuine evidential weight: the model must identify the
specific gap this namespace closes, then produce a body that fills it. A body that could be
written without answering the inertia question is too generic. This provides a semantic
quality anchor that vocabulary register rules alone cannot enforce.
**predicted:** C-17 PASS (vocab columns added, fixing R5 V-03 miss), C-18 PASS (role
identity explicit), C-07/C-10 quality expected higher than V-01 due to inertia priming.
All 12 criteria PASS. Score: 100.
**failure condition:** The inertia question is answered with a generic gap statement ("the
feature story would be missing evidence") rather than a {topic}-specific one, and the body
does not reflect the specific gap named. If this occurs, inertia framing produces no quality
advantage over V-01 — the semantic anchor is hollow.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record: tier for {topic}, compliance tags (if any).
State: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill generates a synthetic coverage map for {topic} across all nine namespaces. Each
artifact answers: what would be missing from {topic}'s feature story if this signal were
absent? That question should shape each body — not as a template phrase, but as a genuine
constraint on what the body is allowed to say.

This skill runs four sequential roles. You ARE the named role while it is active. Producing
output belonging to a later role is a role violation.

---

### ROLE 1 — CLASSIFIER

You are the CLASSIFIER. Produce the classification table below. Do not write artifact bodies.
Writing an artifact body here means you are ROLE 2 — GENERATOR, which you are not yet.

Classification rules:
- EVIDENCE-HEAVY: prove, listen
- HIGH-STRUCTURE: trace, flow
- MIXED: scout, draft, review, program, topic

REAL-REQUIRED rationale (applies at classification time; carried forward to ROLE 2 and
ROLE 3): A synthetic artifact cannot substitute for real signal in EVIDENCE-HEAVY namespaces.
prove-* requires actual experiment data or prototype outputs. listen-* requires real user
interviews or adoption measurements. Compliance-active namespaces (scout-compliance,
trace-permissions) require traceable real-world sources; synthetic content here creates
false assurance.

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED |
|-----------|----------|----------|------------|-------------------|-------------------|---------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language only OR pure study methodology framing | NO | YES if compliance context; else NO | NO (unless Compliance-Tagged YES) |
| draft | MIXED | structural scaffold (sections, properties, acceptance criteria) plus qualitative observations | pure specification language only OR pure study methodology framing | NO | NO | NO |
| review | MIXED | structural scaffold plus qualitative observations and design judgements | pure specification language only OR pure study methodology framing | NO | NO | NO |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language, user quotes, adoption percentages, study framing | NO | NO | NO |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language, adoption rates, user quotes, study framing | YES if tier >= 2; else NO | YES if compliance context; else NO | NO (unless Compliance-Tagged YES) |
| prove | EVIDENCE-HEAVY | study/data/interview language: "N of M tests showed…", "Prototype produced…", hypothesis-and-result framing | specification language, schema definitions, contract structures | NO | NO | YES |
| listen | EVIDENCE-HEAVY | study/data/interview language: adoption rates, "N users found…", survey response framing | specification language, state machine language, schema definitions | YES if tier >= 2; else NO | NO | YES |
| program | MIXED | structural scaffold (milestones, owners, dependencies) plus qualitative rationale | pure specification language only OR pure study methodology framing | NO | NO | NO |
| topic | MIXED | signal synthesis narrative plus structured coverage reference | pure specification language alone | NO | NO | NO |

**ROLE 1 STOP — Do not activate ROLE 2 until all nine namespaces have: Category, MUST-use
vocabulary, DO NOT-use vocabulary, Tier 2/3 Critical (YES/NO), Compliance-Tagged (YES/NO),
and REAL-REQUIRED (YES/NO) in the table.**

---

### ROLE 2 — GENERATOR

You are the GENERATOR. For each namespace, answer the inertia question first, then write the
artifact body. The body must make the inertia answer concrete — a body that could have been
written without the inertia answer is too generic and must be revised before proceeding.

Apply MUST-use and DO NOT-use vocabulary from the ROLE 1 table. Do not re-classify. Do not
write the coverage summary.

For each namespace:

  #### {Namespace} — {representative-skill-name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{representative-skill-name}
  Topic:    {topic}
  Category: {from ROLE 1}
  Date:     {current date}
  Status:   MOCK

  **Without this signal, {topic}'s feature story would be missing:**
  {one sentence — the specific gap this namespace closes for {topic}, not generic}

  **Signal body:**
  {3-5 sentences — vocabulary-compliant with ROLE 1 MUST-use and DO NOT-use for this row;
   body must be grounded in the inertia statement above}

  [If REAL-REQUIRED = YES:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {one sentence — prove: requires actual experiment data or prototype outputs;
  listen: requires real user interviews or adoption measurements;
  compliance namespace: requires traceable real-world sources.}

**ROLE 2 STOP — Do not activate ROLE 3 until all nine namespaces have: a complete MOCK
ARTIFACT header block, an inertia statement ("Without this signal…"), a vocabulary-compliant
signal body, and — for every REAL-REQUIRED namespace — a rationale-accompanied statement.**

---

### ROLE 3 — SUMMARIZER

You are the SUMMARIZER. Produce the coverage summary table only. Do not add new artifact
sections. Do not write the handoff line.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
- REAL-REQUIRED: all EVIDENCE-HEAVY namespaces; compliance-active namespaces
- TIER-CRITICAL: trace-*, scout-feasibility, listen-* at tier >= 2
- Multiple flags: REAL-REQUIRED, TIER-CRITICAL

Recommended Next Step: exact skill call — `/namespace:skill {topic}`. Not "gather signals."
The next step should address the specific gap named in the inertia statement for this namespace.

**ROLE 3 STOP — Do not activate ROLE 4 until all nine namespaces appear in the coverage table
with correct Category, all applicable Flags, and a named Recommended Next Step.**

---

### ROLE 4 — HANDOFF WRITER

You are the HANDOFF WRITER. Write only the handoff section.

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

Replace {topic} and {date} with actual values.
DO NOT write `{this-file}` as a literal placeholder.
DO NOT write any other content in this section.

---

---

## V-04 — Role Sequence + Lifecycle Emphasis (Combination)

**axes:** role-sequence + lifecycle-emphasis
**hypothesis:** V-01 uses identity constraint framing as the primary enforcement mechanism;
stop-gate fields are enumerated but the gates are compact. V-04 adds lifecycle emphasis:
each ROLE STOP enumerates every specific required output field by name, making the gate
conditions unambiguous. "Do not activate ROLE 2 until all nine namespaces have Category,
MUST-use vocabulary, DO NOT-use vocabulary, Tier 2/3 Critical (YES/NO), Compliance-Tagged
(YES/NO), and REAL-REQUIRED (YES/NO)" cannot be satisfied by a partially-filled table.
The combination tests whether field-level gate enumeration adds meaningful enforcement over
V-01's identity constraint framing alone, or whether role identity is already sufficient.
**predicted:** C-18 PASS (role identity), C-14 PASS (explicit stop-gate phrases), C-16 PASS
(field-level gate enumeration, more complete than V-01), C-17 PASS (vocab columns), C-13
PASS (rationale at each REAL-REQUIRED). All 12 criteria PASS. Score: 100.
**failure condition:** Longer, more elaborate stop-gate text trains the model to skim gate
conditions — the model satisfies the gate label without verifying each named field. If this
occurs, compact identity-constraint gates (V-01) are more reliable than verbose field-
enumeration gates at the same role-identity foundation.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record: tier for {topic}, compliance tags (if any).
State: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill runs four sequential roles. Each role holds a distinct identity. You ARE that role
while it is active. Output that belongs to a later role produced during an earlier role is
an identity violation — you are not yet that role. Each role must produce complete output
before the next role activates.

---

### ROLE 1 — CLASSIFIER

You are the CLASSIFIER. Your only output is the classification table below, fully populated.
Writing an artifact body in this section means you are ROLE 2 — GENERATOR, which you are not
yet. Writing a coverage summary means you are ROLE 3 — SUMMARIZER, which you are not yet.
You are the CLASSIFIER. You classify.

Classification rules:
- EVIDENCE-HEAVY: prove, listen
- HIGH-STRUCTURE: trace, flow
- MIXED: scout, draft, review, program, topic

REAL-REQUIRED rationale: A synthetic artifact cannot substitute for real signal in
EVIDENCE-HEAVY namespaces. prove-* requires actual experiment data or prototype outputs.
listen-* requires real user interviews or adoption measurements. When compliance context is
active: scout-compliance and trace-permissions are REAL-REQUIRED regardless of structural
quality — compliance signals require traceable real-world sources; synthetic artifacts create
false assurance.

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED |
|-----------|----------|----------|------------|-------------------|-------------------|---------------|
| scout | MIXED | discovery language: signals, findings, open questions, directional hypotheses | pure specification language only OR pure study methodology framing | NO | YES if compliance context; else NO | NO (unless Compliance-Tagged YES) |
| draft | MIXED | structural scaffold (sections, properties, acceptance criteria) plus qualitative observations | pure specification language only OR pure study methodology framing | NO | NO | NO |
| review | MIXED | structural scaffold plus qualitative observations and design judgements | pure specification language only OR pure study methodology framing | NO | NO | NO |
| flow | HIGH-STRUCTURE | specification language: state transitions, trigger conditions, data flow contracts, schema shapes | interview language, user quotes, adoption percentages, study framing | NO | NO | NO |
| trace | HIGH-STRUCTURE | specification language: interfaces, component boundaries, contracts, state transitions, configuration keys | interview language, adoption rates, user quotes, study framing | YES if tier >= 2; else NO | YES if compliance context; else NO | NO (unless Compliance-Tagged YES) |
| prove | EVIDENCE-HEAVY | study/data/interview language: "N of M tests showed…", "Prototype produced…", hypothesis-and-result framing | specification language, schema definitions, contract structures | NO | NO | YES |
| listen | EVIDENCE-HEAVY | study/data/interview language: adoption rates, "N users found…", survey response framing | specification language, state machine language, schema definitions | YES if tier >= 2; else NO | NO | YES |
| program | MIXED | structural scaffold (milestones, owners, dependencies) plus qualitative rationale | pure specification language only OR pure study methodology framing | NO | NO | NO |
| topic | MIXED | signal synthesis narrative plus structured coverage reference | pure specification language alone | NO | NO | NO |

**ROLE 1 STOP — Do not activate ROLE 2 — GENERATOR until you have verified that all nine
namespaces are present in the table AND each namespace has all six fields populated: (1)
Category assigned as HIGH-STRUCTURE, EVIDENCE-HEAVY, or MIXED; (2) MUST-use vocabulary
terms present; (3) DO NOT-use vocabulary terms present; (4) Tier 2/3 Critical set to YES or
NO; (5) Compliance-Tagged set to YES or NO; (6) REAL-REQUIRED set to YES or NO. A table with
any empty cell does not satisfy this gate.**

---

### ROLE 2 — GENERATOR

You are the GENERATOR. Your only output is nine namespace sections. Apply MUST-use and DO
NOT-use vocabulary from the ROLE 1 table exactly. An artifact body that uses DO NOT-use
vocabulary is invalid.

Writing a coverage summary means you are ROLE 3 — SUMMARIZER, which you are not yet.
You are the GENERATOR. You generate.

For each namespace in table order:

  #### {Namespace} — {representative-skill-name}

  **MOCK ARTIFACT**
  Skill:    {namespace}:{representative-skill-name}
  Topic:    {topic}
  Category: {from ROLE 1 table}
  Date:     {current date}
  Status:   MOCK

  {artifact body — vocabulary-compliant with ROLE 1 MUST-use and DO NOT-use for this row}

  [If REAL-REQUIRED = YES in ROLE 1 table:]
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: {one sentence specific to this namespace — prove: requires actual experiment
  data or prototype outputs; listen: requires real user interviews or adoption measurements;
  compliance namespace: requires traceable real-world sources.}

**ROLE 2 STOP — Do not activate ROLE 3 — SUMMARIZER until you have verified: (1) all nine
namespaces are present as artifact sections; (2) each section contains a complete MOCK
ARTIFACT header block with all five fields (Skill, Topic, Category, Date, Status); (3) each
artifact body uses MUST-use vocabulary and does not use DO NOT-use vocabulary for its row's
category; (4) every namespace with REAL-REQUIRED = YES has a REAL-REQUIRED statement
followed by a one-sentence rationale. An artifact section missing any of these four
conditions does not satisfy this gate.**

---

### ROLE 3 — SUMMARIZER

You are the SUMMARIZER. Your only output is the coverage summary table. You are the
SUMMARIZER — writing additional artifact bodies or the handoff line here is a role violation.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
- REAL-REQUIRED: all EVIDENCE-HEAVY namespaces; all compliance-active namespaces
- TIER-CRITICAL: trace-*, scout-feasibility, listen-* at tier >= 2
- Multiple flags: list all applicable (REAL-REQUIRED, TIER-CRITICAL)

Recommended Next Step: exact skill invocation only — `/namespace:skill {topic}`. DO NOT
write generic advice. DO NOT write "gather more signals." Name the specific skill identifier.

**ROLE 3 STOP — Do not activate ROLE 4 — HANDOFF WRITER until you have verified: (1) all
nine namespaces appear in the coverage table; (2) each row has a Category that matches the
ROLE 1 table; (3) each row has all applicable Flags assigned; (4) each row has a Recommended
Next Step that names a specific skill call — not generic advice. A table row with an empty
Flag cell or a generic next step does not satisfy this gate.**

---

### ROLE 4 — HANDOFF WRITER

You are the HANDOFF WRITER. Your only output is the handoff section below.

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

Replace {topic} and {date} with actual values.
DO NOT write `{this-file}` as a literal placeholder.
DO NOT write any other content in this section.

---

---

## V-05 — Role Sequence + Output Format + Inertia Framing (Full Combination)

**axes:** role-sequence + output-format (co-located template) + inertia-framing
**hypothesis:** All three R5-derived axes active simultaneously. Role identity (C-18) prevents
cross-role contamination at the ontological level. Co-located template depth anchor (from V-02)
delivers vocabulary register cues at the exact generation moment, inside the placeholder the
model is filling. Inertia framing (from V-03) ensures the body carries semantic weight, not
just syntactic vocabulary compliance. The three mechanisms are independent: identity prevents
wrong-phase output; template anchor enforces depth and register at generation time; inertia
framing enforces relevance to {topic}'s actual coverage gap. This combination should produce
the ceiling for C-07 and C-10 execution quality.
**predicted:** C-18 PASS, C-07 ceiling (template anchor + inertia forces depth + relevance),
C-10 ceiling (inertia-derived next steps are gap-specific), C-15 PASS (DO NOT vocabulary
co-located in template), C-17 PARTIAL — vocabulary rules are in the template placeholder
rather than as classification table columns. Score: ~91.7 (11/12) if C-17 requires table
columns strictly; 100 if co-located template satisfies C-17 intent. Deliberate test of
whether C-17's "co-located with the category assignment row" can be satisfied by the
generation-time template or strictly requires the classification table.
**failure condition:** Three axes in one prompt produce length that degrades C-07 execution —
the model abbreviates bodies to process more steps. If this occurs, V-04's two-axis
combination (role + lifecycle) is the practical ceiling, and inertia framing adds cognitive
overhead without quality gain.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record: tier for {topic}, compliance tags (if any).
State: `Tier: {N}  (source: TOPICS.md | --tier | default)`

This skill generates a synthetic coverage map for all nine namespaces. Each artifact answers:
what would be missing from {topic}'s feature story if this signal were absent? That question
constrains every artifact body — a body that could exist without the answer is too generic.

This skill runs four sequential roles. You ARE the named role while it is active. Output that
belongs to a later role produced during an earlier role is an identity violation.

---

### ROLE 1 — CLASSIFIER

You are the CLASSIFIER. Produce the classification table only. Writing an artifact body here
is a role violation — you are not yet ROLE 2. You classify.

Classification rules:
- EVIDENCE-HEAVY: prove, listen
- HIGH-STRUCTURE: trace, flow
- MIXED: scout, draft, review, program, topic

REAL-REQUIRED rationale: A synthetic artifact cannot substitute for real signal in
EVIDENCE-HEAVY namespaces. prove-* requires actual experiment data or prototype outputs.
listen-* requires real user interviews or adoption measurements. Compliance-active namespaces
(scout-compliance, trace-permissions) require traceable real-world sources.

| Namespace | Category | Tier 2/3 Critical | Compliance-Tagged | REAL-REQUIRED |
|-----------|----------|-------------------|-------------------|---------------|
| scout | MIXED | NO | YES if compliance context; else NO | NO (unless Compliance-Tagged YES) |
| draft | MIXED | NO | NO | NO |
| review | MIXED | NO | NO | NO |
| flow | HIGH-STRUCTURE | NO | NO | NO |
| trace | HIGH-STRUCTURE | YES if tier >= 2; else NO | YES if compliance context; else NO | NO (unless Compliance-Tagged YES) |
| prove | EVIDENCE-HEAVY | NO | NO | YES |
| listen | EVIDENCE-HEAVY | YES if tier >= 2; else NO | NO | YES |
| program | MIXED | NO | NO | NO |
| topic | MIXED | NO | NO | NO |

**ROLE 1 STOP — Do not activate ROLE 2 until all nine rows have Category, Tier 2/3 Critical
(YES/NO), Compliance-Tagged (YES/NO), and REAL-REQUIRED (YES/NO).**

---

### ROLE 2 — GENERATOR

You are the GENERATOR. For each namespace, fill in the template below exactly. The body
placeholder contains all vocabulary and depth guidance — do not read vocabulary rules from
anywhere else. Replace placeholder text with actual content; do not copy placeholder text
into the output.

For each namespace, in ROLE 1 table order:

```
---
MOCK ARTIFACT
Skill:    {namespace}:{representative-skill-name}
Topic:    {topic}
Category: {Category from ROLE 1 — HIGH-STRUCTURE | EVIDENCE-HEAVY | MIXED}
Date:     {current date}
Status:   MOCK
---

Without this signal, {topic}'s feature story would be missing:
{one sentence — the specific gap this namespace closes for {topic}}

Signal body:
{3-5 sentences. Match register to Category from ROLE 1:

  HIGH-STRUCTURE  → MUST use: specification/contract framing —
                    "the component contract requires…", "the interface exposes…",
                    "schema defines field X as…", "state transition fires when…"
                    DO NOT use: user quotes, interview data, adoption rates, study framing
  EVIDENCE-HEAVY  → MUST use: study/experiment framing —
                    "N of M tests showed…", "prototype against {topic} produced…",
                    "interview participants reported…", "adoption rate of X%…"
                    DO NOT use: specification language, contract structures, schema definitions
  MIXED           → MUST use: discovery/signal language plus one structural element —
                    "signals suggest…", "three sources converge on…", "early indicators…"
                    DO NOT use: pure specification language; pure study methodology framing

  The body must be grounded in the inertia statement above — a body that could exist
  without the inertia answer is too generic and must be revised.}

{If REAL-REQUIRED = YES in ROLE 1 table:
  REAL-REQUIRED: A synthetic artifact cannot substitute for real signal here.
  Rationale: [one sentence — prove: requires actual experiment data or prototype outputs;
  listen: requires real user interviews or adoption measurements;
  compliance namespace: requires traceable real-world sources]}
```

**ROLE 2 STOP — Do not activate ROLE 3 until all nine namespaces have: a complete MOCK
ARTIFACT header block (all five fields), a non-generic inertia statement, a 3-5 sentence
vocabulary-compliant signal body grounded in the inertia statement, and — for every
REAL-REQUIRED namespace — a rationale-accompanied REAL-REQUIRED statement.**

---

### ROLE 3 — SUMMARIZER

You are the SUMMARIZER. Produce the coverage summary table. Do not write additional artifact
sections. Do not write the handoff line. You are the SUMMARIZER.

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag rules:
- REAL-REQUIRED: all EVIDENCE-HEAVY namespaces; compliance-active namespaces
- TIER-CRITICAL: trace-*, scout-feasibility, listen-* at tier >= 2
- Multiple flags: REAL-REQUIRED, TIER-CRITICAL

Recommended Next Step: exact skill call — `/namespace:skill {topic}`. The next step should
address the specific gap named in the inertia statement for this namespace. Not generic advice.

**ROLE 3 STOP — Do not activate ROLE 4 until all nine namespaces appear in the coverage table
with correct Category, all applicable Flags, and a named Recommended Next Step.**

---

### ROLE 4 — HANDOFF WRITER

You are the HANDOFF WRITER. Write only the handoff section.

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-all-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md

Replace {topic} and {date} with actual values.
DO NOT write `{this-file}` as a literal placeholder.
DO NOT write any other content in this section.

---

---

## Scorecard Preview

| Variation | Primary Axis | C-17 | C-18 | C-07 | Predicted |
|-----------|-------------|------|------|------|-----------|
| V-01 | role-sequence (identity constraint) | PASS (vocab columns) | PASS (explicit identity framing) | PASS | 100 |
| V-02 | output-format (co-located template) | PARTIAL (vocab in template, not table) | PASS | PASS (in-template anchor) | ~91.7 |
| V-03 | inertia-framing (upgraded) | PASS (vocab columns added) | PASS | PASS (inertia grounds body) | 100 |
| V-04 | role-sequence + lifecycle-emphasis | PASS | PASS | PASS | 100 |
| V-05 | role-sequence + output-format + inertia | PARTIAL (vocab in template) | PASS | CEILING | ~91.7–100 |

**Open question for scorecard:** Does C-17's "co-located with the category assignment row"
require table columns specifically, or does co-location in the generation-time template
satisfy the criterion? V-02 and V-05 are the deliberate test cases.

Next: /mock:review {topic} simulations/quest/golden/mock-all-variate-R6-2026-03-15.md
