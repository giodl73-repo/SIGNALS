---
skill: quest-variate
skill_target: mock-ns
round: 8
rubric_version: 8
date: 2026-03-15
---

# mock-ns -- Round 8 Variations

Rubric: v8 (C-01 through C-26, aspirational denominator 18).

New criteria in v8:
- **C-25** -- Guarantee-break framing in the compute-site failure-consequence statement (depends on C-23)
- **C-26** -- Cross-site consequence reference in the compute-site failure-consequence statement (depends on C-23, requires C-20)

R7 V-05 carried C-23 in extended form -- "If any path modifies FLAG after this point, the
guarantee stated above is broken: A-1 will inherit a corrupted value that cannot be
distinguished from a correctly-computed one, producing the same silent category mismatch
described at the consumption site." -- and C-24 ("Every instruction in this step -- named or
unnamed -- is governed by this rule. No instruction in this step is exempt."). R8 isolates and
formalizes the two compute-site refinements that appeared in R7's excellence signals.

C-25 requires the consequence statement to frame the violation as explicitly breaking the
affirmative closure guarantee stated in C-21 -- the phrase "the guarantee stated above is
broken" is the required causal bridge. C-26 requires the consequence statement to cross-
reference the consumption-site failure consequence (C-20) by naming the shared failure
mechanism -- "producing the same silent category mismatch described at the consumption site"
is the reference pattern.

The compute-site escalation chain now reads six levels:

  C-14 prohibit
  C-16 run-scoped
  C-18 named path classes
  C-21 affirmative closure (positive obligation + no-exemption statement)
  C-23 failure consequence (mechanism + downstream effect)
  C-25 guarantee-break framing (violation breaks the C-21 commitment)
  C-26 cross-site reference (names C-20 consequence at the consumption site)

Each variation is a **complete, runnable skill body prompt**. Single-axis variation first
(V-01 through V-03), then combined axes (V-04, V-05).

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Inertia framing (C-25 only, guarantee-break as primary addition) | C-25 is the higher-leverage R8 criterion. The affirmative closure (C-21) states a positive commitment: every path carries this value, no path is exempt. C-23 then names the contamination consequence. But without explicit framing that the violation *breaks the guarantee just stated*, an executor under pressure may read C-23 as an independent warning rather than as the cost of a stated obligation. "The guarantee stated above is broken" is a backward-pointing connective -- it makes C-23's consequence logically dependent on C-21's closure at the point of the consequence, not merely adjacent to it. C-26 adds a navigation link to C-20 but does not change what the executor understands about why the violation is serious. |
| V-02 | Phrasing register (C-26 only, cross-site reference as primary addition) | C-26 is the higher-leverage R8 criterion. The guarantee-break framing of C-25 is implicit once C-21 and C-23 are both present -- an executor who reads "every path carries this value, no path is exempt; if any path modifies it, A-1 inherits a corrupted value indistinguishable from a correct one" can reconstruct the logical connection to the guarantee. What C-26 adds is not reconstructable: it tells the reader there is a companion consequence statement at the other prohibition site, and it names the shared mechanism. This is new navigational information that collapses the structural symmetry between the two escalation chains from implicit to explicit. C-25 adds a logical connective over information already present; C-26 adds a pointer to information that would otherwise require search. |
| V-03 | Lifecycle emphasis (R7 full convergence -- neither C-25 nor C-26) | R7 full convergence (C-01 through C-24) is already sufficient. C-23 names the contamination mechanism (FLAG modified after the compute step) and the downstream effect (A-1 inherits a corrupted value indistinguishable from a correctly-computed one). C-24 converts the consumption-site catch-all from a negative bound to a positive assertion of coverage. An executor who reads both sites has the information needed to treat the prohibitions as serious. C-25 adds a logical connective that tightens the causal chain but introduces no new information. C-26 reduces navigation effort but does not change the executor's understanding. Regression baseline for scoring comparison against V-01, V-02, and V-04/V-05. |
| V-04 | Output format + role sequence (C-25 + C-26, minimal form, table-structured S-3) | C-25 and C-26 are independent structural completions at the compute site and do not require extended elaboration to satisfy their pass conditions. C-25 requires only the guarantee-break framing phrase: "the guarantee stated above is broken" as a causal bridge before the consequence description. C-26 requires only the cross-reference phrase: "producing the same silent category mismatch described at the consumption site" appended to the consequence. Both fit within the existing C-23 sentence without adding a new sentence. Table-structuring the flag-case decision in S-3 reduces cognitive overhead at the decision node without compressing the prohibition block. |
| V-05 | Role sequence (full convergence -- all 26 criteria, prose emphasis) | C-25 and C-26 are mutually reinforcing with all prior layers and neither is redundant. C-25 makes the consequence logically dependent on the guarantee -- a reader at the compute step sees not just "a bad thing happens" but "the specific commitment just stated is violated." C-26 makes the structural symmetry between both prohibition sites explicit and navigable -- a reader at either site is directed to the companion consequence without needing to search the other step. Together they complete the six-level compute-site chain, matching the five-level consumption-site chain completed by C-24 in R7. Full convergence is the only variant that predicts 100 on v8 aspirational. |

---

## V-01 -- Guarantee-Break Framing (C-25 only)

**Axis**: Inertia framing -- guarantee-break causal bridge added at the compute-site
consequence only. C-26 cross-site reference intentionally absent.
**Hypothesis**: C-25 is the stronger R8 addition. C-21 stakes a positive commitment and C-23
names the consequence of violating it, but the connection between the commitment and the
consequence is left implicit. An executor under pressure who skims C-23 may treat "A-1 will
inherit a corrupted value" as a standalone risk statement, not as the cost of violating the
specific positive obligation just asserted. The phrase "the guarantee stated above is broken"
forces a backward reference: the consequence is now logically anchored to C-21, not merely
sequential with it. C-26 provides useful navigation but the consequence's credibility does
not depend on a link to C-20.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 C-12 C-13
C-14 C-15 C-16 C-17 C-18 C-19 C-20 C-21 C-22 C-23 C-24 C-25. Missing: C-26.
**Expected composite**: 17/18 aspirational ~= 99.4

---

```
You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required -- scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional -- default: representative skill per namespace)
  --tier     1 | 2 | 3        (optional -- default: 1)

SINGLE-PASS. NO PROMPTS. Write artifact. Emit next-step line. Done.

---

STEP S-1 -- SETUP

Read TOPICS.md. Emit a dedicated line:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Select the skill to mock:
  - If --skill is provided, use it.
  - Otherwise use the representative skill for the namespace:

  | Namespace | Default skill       | Exclusion constraint                                      |
  |-----------|---------------------|-----------------------------------------------------------|
  | scout     | scout-feasibility   |                                                           |
  | draft     | draft-spec          |                                                           |
  | review    | review-design       |                                                           |
  | flow      | flow-resilience     |                                                           |
  | trace     | trace-request       |                                                           |
  | prove     | prove-hypothesis    |                                                           |
  | listen    | listen-support      |                                                           |
  | program   | program-plan        |                                                           |
  | topic     | topic-plan          | topic-status is EXCLUDED -- meta-structural, never default |

Emit:
  > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- DETERMINE CATEGORY

Assign CATEGORY for the selected skill:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,
    flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

CATEGORY is now assigned. Do not modify it.

---

STEP S-3 -- COMPUTE FLAG

FLAG is computed exactly once in this step. It is a named variable.

FLAG MUST NOT be recomputed anywhere in this run -- not in any step, any conditional
branch, any fallback path, any regeneration sequence, or any other execution context,
including paths that do not pass through prior steps in normal order. Every execution
path that reaches A-1 carries the FLAG value emitted here. No path is exempt. If any
path modifies FLAG after this point, the guarantee stated above is broken: A-1 will
inherit a corrupted value that cannot be distinguished from a correctly-computed one.

Compute FLAG from CATEGORY and tier:

  Case 1 -- CATEGORY = HIGH-STRUCTURE AND skill is critical (trace-*, scout-feasibility,
            any listen-*) AND tier >= 2:
    FLAG = "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"

  Case 2 -- CATEGORY = HIGH-STRUCTURE (all other cases):
    FLAG = "none (structural coverage reliable)"

  Case 3 -- CATEGORY = EVIDENCE-HEAVY:
    FLAG = "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)"

  Case 4 -- CATEGORY = MIXED:
    FLAG = "REVIEW-FOR-PLAUSIBILITY"

  Compliance override -- check last, applied regardless of case above:
    If compliance tags are present in TOPICS.md AND skill is scout-compliance or
    trace-permissions (any tier, any category):
    FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

The first rule of this step is: copy FLAG from S-3 verbatim. Do not rederive it.
This rule is first -- it applies before any field is listed, before any category
lookup, before any formatting instruction, or any other instruction in this step.
No instruction in A-1 precedes this rule. Every instruction in this step -- named or
unnamed -- is governed by this rule. No instruction in this step is exempt.
Inertia risk: re-deriving FLAG here produces a category mismatch that is invisible
to downstream tooling and silently corrupts the artifact's trust tier. The artifact
will carry an incorrect Flag field, downstream mock-review will flag the wrong
namespaces as REAL-REQUIRED, and the corruption is undetectable without manual
header inspection.

Assemble the header block:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- copied verbatim, not rederived}

The header appears immediately after any frontmatter. All six fields are present.
The header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning as the first section of the artifact body. Position it
before any mock content. Separate from the header and from the body with ---
delimiters.

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. The sections are right; the contents are invented. A real
    {skill-id} run is required before any evidence-based decision can be made
    from this namespace.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
    mechanisms) are reliable. Specific claims (competitor names, market data,
    research findings) may be partially accurate or partially fabricated. Review
    for plausibility before accepting coverage.

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
    mechanisms are reliable. Content is synthetically generated but structurally
    representative. Adequate for structural planning at Tier 1. REAL-REQUIRED at
    Tier 2+ for critical namespaces (trace, scout-feasibility, listen).

---

STEP A-3 -- GENERATE ARTIFACT BODY

Generate the mock body following the golden rubric structure for the selected skill.
The body must include:
  - All required section headings for the skill
  - Required tables or lists in the expected positions
  - Gate or verdict line where the skill produces one
  - Enforcement mechanisms in the expected positions

A reader familiar with the real skill must be able to identify which skill was mocked.
Generic prose without skill-specific structure fails.

---

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

The final line of the artifact is:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit only if this skill was called from within a mock-review session to regenerate
a thin namespace.
```

---

## V-02 -- Cross-Site Reference (C-26 only)

**Axis**: Phrasing register -- cross-site consequence reference added at the compute-site
consequence only. C-25 guarantee-break framing intentionally absent.
**Hypothesis**: C-26 is the stronger R8 addition. The guarantee-break framing of C-25 is
recoverable by an attentive executor: if C-21 states the commitment and C-23 names the
consequence, the logical connection is inferrable. The cross-reference in C-26 is not
recoverable by inference -- it provides a navigation signal to C-20 at the consumption site
that does not exist elsewhere in the procedure. An executor reading the compute-site
consequence learns not only what goes wrong at A-1, but that there is a companion description
of the same failure mechanism at the other prohibition site. This collapses the structural
symmetry between the two escalation chains from implicit to explicit. C-25 tightens a
logical connective; C-26 opens a new navigational path.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 C-12 C-13
C-14 C-15 C-16 C-17 C-18 C-19 C-20 C-21 C-22 C-23 C-24 C-26. Missing: C-25.
**Expected composite**: 17/18 aspirational ~= 99.4

---

```
You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required -- scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional -- default: representative skill per namespace)
  --tier     1 | 2 | 3        (optional -- default: 1)

Single-pass. No prompts.

---

STEP S-1 -- SETUP

Read TOPICS.md. Emit:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Select the skill to mock. If --skill is provided, use it. Otherwise use the
representative default:

  | Namespace | Default skill       | Exclusion constraint                                      |
  |-----------|---------------------|-----------------------------------------------------------|
  | scout     | scout-feasibility   |                                                           |
  | draft     | draft-spec          |                                                           |
  | review    | review-design       |                                                           |
  | flow      | flow-resilience     |                                                           |
  | trace     | trace-request       |                                                           |
  | prove     | prove-hypothesis    |                                                           |
  | listen    | listen-support      |                                                           |
  | program   | program-plan        |                                                           |
  | topic     | topic-plan          | topic-status is EXCLUDED -- meta-structural, never default |

Emit:
  > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- DETERMINE CATEGORY

Assign CATEGORY for the selected skill:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,
    flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

CATEGORY is now assigned. Do not modify it.

---

STEP S-3 -- COMPUTE FLAG

FLAG is computed exactly once in this step. It is a named variable.

FLAG MUST NOT be recomputed anywhere in this run -- not in any step, any conditional
branch, any fallback path, any regeneration sequence, or any other execution context,
including paths that do not pass through prior steps in normal order. Every execution
path that reaches A-1 carries the FLAG value emitted here. No path is exempt. If any
path modifies FLAG after this point, A-1 will inherit a corrupted value that cannot
be distinguished from a correctly-computed one, producing the same silent category
mismatch described at the consumption site.

Compute FLAG from CATEGORY and tier:

  Case 1 -- CATEGORY = HIGH-STRUCTURE AND skill is critical (trace-*, scout-feasibility,
            any listen-*) AND tier >= 2:
    FLAG = "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"

  Case 2 -- CATEGORY = HIGH-STRUCTURE (all other cases):
    FLAG = "none (structural coverage reliable)"

  Case 3 -- CATEGORY = EVIDENCE-HEAVY:
    FLAG = "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)"

  Case 4 -- CATEGORY = MIXED:
    FLAG = "REVIEW-FOR-PLAUSIBILITY"

  Compliance override -- check last, applied regardless of case above:
    If compliance tags are present in TOPICS.md AND skill is scout-compliance or
    trace-permissions (any tier, any category):
    FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

The first rule of this step is: copy FLAG from S-3 verbatim. Do not rederive it.
This rule is first -- it applies before any field is listed, before any category
lookup, before any formatting instruction, or any other instruction in this step.
No instruction in A-1 precedes this rule. Every instruction in this step -- named or
unnamed -- is governed by this rule. No instruction in this step is exempt.
Inertia risk: re-deriving FLAG here produces a category mismatch that is invisible
to downstream tooling and silently corrupts the artifact's trust tier. The artifact
will carry an incorrect Flag field, downstream mock-review will flag the wrong
namespaces as REAL-REQUIRED, and the corruption is undetectable without manual
header inspection.

Assemble the header block:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- copied verbatim, not rederived}

The header appears immediately after any frontmatter. All six fields are present.
The header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning as the first section of the artifact body. Position it
before any mock content. Separate from the header and from the body with ---
delimiters.

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. The sections are right; the contents are invented. A real
    {skill-id} run is required before any evidence-based decision can be made
    from this namespace.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
    mechanisms) are reliable. Specific claims (competitor names, market data,
    research findings) may be partially accurate or partially fabricated. Review
    for plausibility before accepting coverage.

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
    mechanisms are reliable. Content is synthetically generated but structurally
    representative. Adequate for structural planning at Tier 1. REAL-REQUIRED at
    Tier 2+ for critical namespaces (trace, scout-feasibility, listen).

---

STEP A-3 -- GENERATE ARTIFACT BODY

Generate the mock body following the golden rubric structure for the selected skill.
The body must include:
  - All required section headings for the skill
  - Required tables or lists in the expected positions
  - Gate or verdict line where the skill produces one
  - Enforcement mechanisms in the expected positions

A reader familiar with the real skill must be able to identify which skill was mocked.
Generic prose without skill-specific structure fails.

---

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

The final line of the artifact is:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit only if this skill was called from within a mock-review session to regenerate
a thin namespace.
```

---

## V-03 -- R7 Full Convergence (neither C-25 nor C-26)

**Axis**: Lifecycle emphasis -- R7 full convergence as regression baseline. No new R8
criteria introduced.
**Hypothesis**: R7 full convergence (C-01 through C-24) is already sufficient. The compute-
site escalation chain through C-23 names both the upstream contamination mechanism ("FLAG
modified after the compute step") and the downstream effect ("A-1 inherits a corrupted value
indistinguishable from a correctly-computed one"). The consumption-site chain through C-24
asserts positive coverage: every instruction in the step is governed by the rule, no
instruction is exempt. An executor with both sites fully instrumented has the information
needed to treat the prohibitions as serious. C-25 adds a logical connective that tightens
causality but introduces no new information. C-26 adds a navigation shortcut but the reader
can locate C-20 via the step structure. Baseline for scoring regression comparison against
V-01, V-02, and V-04/V-05.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 C-12 C-13
C-14 C-15 C-16 C-17 C-18 C-19 C-20 C-21 C-22 C-23 C-24. Missing: C-25, C-26.
**Expected composite**: 16/18 aspirational ~= 98.9

---

```
You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}
  Namespace: {namespace}   (scout | draft | review | flow | trace | prove |
                            listen | program | topic)
  --skill    {skill-id}    (optional)
  --tier     1 | 2 | 3     (default: 1)

Execute in one pass. No prompts. Write artifact. Done.

---

S-1. SETUP

Read TOPICS.md. Emit:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Determine the skill to mock.
  If --skill is specified, use it.
  Otherwise, apply the namespace default:

  | Namespace | Default skill       | Exclusion constraint                                      |
  |-----------|---------------------|-----------------------------------------------------------|
  | scout     | scout-feasibility   |                                                           |
  | draft     | draft-spec          |                                                           |
  | review    | review-design       |                                                           |
  | flow      | flow-resilience     |                                                           |
  | trace     | trace-request       |                                                           |
  | prove     | prove-hypothesis    |                                                           |
  | listen    | listen-support      |                                                           |
  | program   | program-plan        |                                                           |
  | topic     | topic-plan          | topic-status is EXCLUDED -- meta-structural, never default |

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

S-2. CATEGORY

Look up the skill in the category table:

  HIGH-STRUCTURE
    scout-feasibility, scout-stakeholders, scout-requirements, scout-naming,
    scout-compliance, scout-market, draft-spec, draft-proposal, draft-pitch,
    review-design, review-code, trace-request, trace-component, trace-contract,
    trace-state, trace-skill, trace-migration, trace-deployment, flow-resilience,
    flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle, flow-trigger,
    flow-integration, program-plan

  EVIDENCE-HEAVY
    prove-websearch, prove-interview, prove-prototype, listen-feedback,
    listen-support, listen-adoption

  MIXED
    scout-competitors, prove-hypothesis, review-customers, review-users

CATEGORY = the value from this table. No other value is valid.

---

S-3. COMPUTE FLAG

FLAG is a named variable computed in this step. Compute it once.

FLAG MUST NOT be recomputed anywhere in this run -- not in any step, any conditional
branch, any fallback path, any regeneration sequence, or any other execution context,
including paths that do not pass through prior steps in normal order. Every execution
path that reaches A-1 carries the FLAG value emitted here. No path is exempt. If any
path modifies FLAG after this point, A-1 will inherit a corrupted value that cannot
be distinguished from a correctly-computed one.

  CATEGORY = HIGH-STRUCTURE, critical namespace (trace-*, scout-feasibility,
             listen-*), tier >= 2:
    FLAG = "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"
  CATEGORY = HIGH-STRUCTURE (all other cases):
    FLAG = "none (structural coverage reliable)"
  CATEGORY = EVIDENCE-HEAVY:
    FLAG = "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)"
  CATEGORY = MIXED:
    FLAG = "REVIEW-FOR-PLAUSIBILITY"
  Compliance override (compliance tags in TOPICS.md AND skill is scout-compliance
  or trace-permissions):
    FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not modify FLAG after this step.

---

A-1. ASSEMBLE HEADER

The first rule of this step is: copy FLAG from S-3 verbatim. Do not rederive it.
This rule is first -- it applies before any field is listed, before any category
lookup, before any formatting instruction, or any other instruction in this step.
No instruction in A-1 precedes this rule. Every instruction in this step -- named or
unnamed -- is governed by this rule. No instruction in this step is exempt.
Inertia risk: re-deriving FLAG here produces a category mismatch that is invisible
to downstream tooling and silently corrupts the artifact's trust tier. The artifact
will carry an incorrect Flag field, downstream mock-review will flag the wrong
namespaces as REAL-REQUIRED, and the corruption is undetectable without manual
header inspection.

Build the header block:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- do not rederive}

Place immediately after frontmatter, before all body content.

---

A-2. FIDELITY WARNING

Write the fidelity warning as the lead section of the artifact body, before mock
content, delimited by ---:

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. Structure is correct; content is
    fabricated. Do not use for conclusions about {topic}. Real {skill-id} run
    required before evidence-based decisions.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements are reliable. Specific
    claims may be fabricated. Review for plausibility before accepting coverage.

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. Structure and enforcement mechanisms are
    reliable. Content is synthetically generated. Adequate for structural planning
    at Tier 1. REAL-REQUIRED at Tier 2+ for critical namespaces (trace,
    scout-feasibility, listen).

---

A-3. ARTIFACT BODY

Generate the mock body following the golden rubric structure for the selected skill.
All required sections, tables, gates, and enforcement mechanisms must be present in
the expected positions. Generic prose fails.

---

A-4. WRITE

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md
Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

A-5. NEXT STEP

Final artifact line:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit if regenerating from within a mock-review session.
```

---

## V-04 -- C-25 + C-26 Minimal, Table-Structured

**Axis**: Output format + role sequence -- both C-25 and C-26 in minimal form, with the
S-3 flag-case decision expressed as a table rather than prose cases.
**Hypothesis**: C-25 and C-26 are both satisfied by minimal additions to the existing C-23
sentence. C-25 requires only the phrase "the guarantee stated above is broken" inserted as
a causal bridge before the consequence description. C-26 requires only the phrase "producing
the same silent category mismatch described at the consumption site" appended to the
consequence. Both fit within the single consequence sentence without requiring a new sentence
or extended elaboration. The minimal form tests whether the rubric's pass conditions are
satisfied by precision rather than verbosity. Table-structuring the S-3 flag-case decision
reduces cognitive overhead at the multi-case branching node without compressing the
prohibition block that follows it.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 C-12 C-13
C-14 C-15 C-16 C-17 C-18 C-19 C-20 C-21 C-22 C-23 C-24 C-25 C-26.
**Expected composite**: 100 (all 26 criteria).

---

```
You are running /mock:ns for Signal.

INPUTS

| Input     | Value                                                                      |
|-----------|----------------------------------------------------------------------------|
| Topic     | {topic} (required)                                                         |
| Namespace | {namespace} (required): scout | draft | review | flow | trace | prove |    |
|           | listen | program | topic                                                |
| --skill   | {skill-id} (optional -- default: representative skill)                     |
| --tier    | 1 | 2 | 3 (optional -- default: 1)                                    |

Single-pass. No prompts.

---

PROCEDURE

S-1  SETUP
     Read TOPICS.md. Emit:
       > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

     Select the skill:

     | Namespace | Default skill       | Exclusion constraint                                      |
     |-----------|---------------------|-----------------------------------------------------------|
     | scout     | scout-feasibility   |                                                           |
     | draft     | draft-spec          |                                                           |
     | review    | review-design       |                                                           |
     | flow      | flow-resilience     |                                                           |
     | trace     | trace-request       |                                                           |
     | prove     | prove-hypothesis    |                                                           |
     | listen    | listen-support      |                                                           |
     | program   | program-plan        |                                                           |
     | topic     | topic-plan          | topic-status is EXCLUDED -- meta-structural, never default |

     Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

S-2  CATEGORY
     Assign CATEGORY:
       HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
         scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
         draft-pitch, review-design, review-code, trace-request, trace-component,
         trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
         flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle,
         flow-throttle, flow-trigger, flow-integration, program-plan
       EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
         listen-feedback, listen-support, listen-adoption
       MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

S-3  COMPUTE FLAG
     Compute FLAG as a named variable before header assembly.

     | CATEGORY                         | FLAG value                                                     |
     |----------------------------------|----------------------------------------------------------------|
     | HIGH-STRUCTURE (critical + T2+)  | "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"|
     | HIGH-STRUCTURE (all other)       | "none (structural coverage reliable)"                          |
     | EVIDENCE-HEAVY                   | "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)" |
     | MIXED                            | "REVIEW-FOR-PLAUSIBILITY"                                      |
     | Compliance override (any cat.)   | "REAL-REQUIRED (compliance-sensitive)"                         |

     Critical namespaces: trace-*, scout-feasibility, listen-*. Compliance override
     applies when compliance tags are present in TOPICS.md AND skill is
     scout-compliance or trace-permissions; override takes precedence over all other
     cases.

     FLAG MUST NOT be recomputed anywhere in this run -- not in any step, any
     conditional branch, any fallback path, any regeneration sequence, or any other
     execution context, including paths that do not pass through prior steps in
     normal order. Every execution path that reaches A-1 carries the FLAG value
     emitted here. No path is exempt. If any path modifies FLAG after this point,
     the guarantee stated above is broken: A-1 will inherit a corrupted value that
     cannot be distinguished from a correctly-computed one, producing the same
     silent category mismatch described at the consumption site.

     FLAG is resolved. Do not re-evaluate or modify it anywhere in this run.

A-1  HEADER
     The first rule of this step: copy FLAG from S-3 verbatim. Do not rederive it.
     This rule is first -- it applies before any field is listed, before any category
     lookup, before any formatting instruction, or any other instruction in this step.
     No instruction in A-1 precedes this rule. Every instruction in this step -- named
     or unnamed -- is governed by this rule. No instruction in this step is exempt.
     Inertia risk: re-deriving FLAG here produces a category mismatch that is invisible
     to downstream tooling and silently corrupts the artifact's trust tier. The artifact
     will carry an incorrect Flag field, downstream mock-review will flag the wrong
     namespaces as REAL-REQUIRED, and the corruption is undetectable without manual
     header inspection.

     [MOCK ARTIFACT -- NOT VERIFIED]
     Skill: {skill-id}
     Topic: {topic}
     Category: {CATEGORY}
     Date: {today's date}
     Status: MOCK (awaiting review)
     Flag: {FLAG from S-3}

A-2  FIDELITY WARNING
     Write as the lead section of the artifact body (before mock content, after ---):

     | CATEGORY       | Block    | Required content                                       |
     |----------------|----------|--------------------------------------------------------|
     | EVIDENCE-HEAVY | WARNING  | Content fabricated; real run required                  |
     | MIXED          | CAUTION  | Structural reliable; specific claims may be wrong      |
     | HIGH-STRUCTURE | NOTE     | Structure reliable; Tier 1 adequate; REAL-REQUIRED     |
     |                |          | at Tier 2+ for critical namespaces                     |

A-3  ARTIFACT BODY
     Generate mock body following the golden rubric structure for the selected skill.
     All required sections, tables, gates, and enforcement mechanisms must be present.
     Generic prose fails.

A-4  WRITE
     Path: simulations/mock/{topic}-{namespace}-mock-{date}.md
     Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

A-5  NEXT STEP
     Final line: Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
     (Omit if called from within a mock-review session.)
```

---

## V-05 -- Full Convergence (all 26 criteria, prose emphasis)

**Axis**: Role sequence -- convergent execution with all six compute-site protection layers
and all five consumption-site protection layers active simultaneously. Prose emphasis.
**Hypothesis**: C-25 and C-26 are mutually reinforcing with all prior layers and neither is
redundant. C-25 makes the consequence statement at S-3 logically dependent on the affirmative
closure commitment stated immediately above it: a reader encounters "Every path carries this
value. No path is exempt." and then "If any path modifies it, the guarantee stated above is
broken" -- the backward reference forecloses the reading of C-23 as a standalone risk
statement. C-26 makes the structural symmetry between both prohibition sites explicit and
navigable: a reader at the compute site is directed to the consumption-site consequence (C-20)
without needing to search, and vice versa. Together they complete the six-level compute-site
chain, which now mirrors the five-level consumption-site chain extended by C-24. Full
convergence is the only variant that predicts 100 on v8 aspirational.
**Predicts**: All 26 criteria -- C-01 through C-26.
**Expected composite**: 100.

---

```
You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}         (required)
  Namespace: {namespace}     (required -- scout | draft | review | flow | trace |
                              prove | listen | program | topic)
  --skill    {skill-id}      (optional)
  --tier     1 | 2 | 3       (default: 1)

Single-pass. No prompts. One artifact. One next-step line.

---

STEP S-1 -- SETUP

Read TOPICS.md. Emit a dedicated line for the TOPICS.md result:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Select the skill to mock:
  - If --skill is specified: use it.
  - Otherwise, use the representative default from this table:

  | Namespace | Default skill       | Exclusion constraint                                      |
  |-----------|---------------------|-----------------------------------------------------------|
  | scout     | scout-feasibility   |                                                           |
  | draft     | draft-spec          |                                                           |
  | review    | review-design       |                                                           |
  | flow      | flow-resilience     |                                                           |
  | trace     | trace-request       |                                                           |
  | prove     | prove-hypothesis    |                                                           |
  | listen    | listen-support      |                                                           |
  | program   | program-plan        |                                                           |
  | topic     | topic-plan          | topic-status is EXCLUDED -- meta-structural, never default |

Emit:
  > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- DETERMINE CATEGORY

Assign CATEGORY for the selected skill:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,
    flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

CATEGORY is now assigned. Do not modify it.

---

STEP S-3 -- COMPUTE FLAG

FLAG is computed exactly once in this step. It is a named variable.

FLAG MUST NOT be recomputed anywhere in this run -- not in any step, any conditional
branch, any fallback path, any regeneration sequence, or any other execution context,
including paths that do not pass through prior steps in normal order. Every execution
path that reaches A-1 carries the FLAG value emitted here. No path is exempt. If any
path modifies FLAG after this point, the guarantee stated above is broken: A-1 will
inherit a corrupted value that cannot be distinguished from a correctly-computed one,
producing the same silent category mismatch described at the consumption site.

Compute FLAG from CATEGORY and tier:

  Case 1 -- CATEGORY = HIGH-STRUCTURE AND skill is critical (trace-*, scout-feasibility,
            any listen-*) AND tier >= 2:
    FLAG = "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"

  Case 2 -- CATEGORY = HIGH-STRUCTURE (all other cases):
    FLAG = "none (structural coverage reliable)"

  Case 3 -- CATEGORY = EVIDENCE-HEAVY:
    FLAG = "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)"

  Case 4 -- CATEGORY = MIXED:
    FLAG = "REVIEW-FOR-PLAUSIBILITY"

  Compliance override -- check last, applied regardless of case above:
    If compliance tags are present in TOPICS.md AND skill is scout-compliance or
    trace-permissions (any tier, any category):
    FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

The first rule of this step is: copy FLAG from S-3 verbatim. Do not rederive it.
This rule is first -- it applies before any field is listed, before any category
lookup, before any formatting instruction, or any other instruction in this step.
No instruction in A-1 precedes this rule. Every instruction in this step -- named or
unnamed -- is governed by this rule. No instruction in this step is exempt.
Inertia risk: re-deriving FLAG here produces a category mismatch that is invisible
to downstream tooling and silently corrupts the artifact's trust tier. The artifact
will carry an incorrect Flag field, downstream mock-review will flag the wrong
namespaces as REAL-REQUIRED, and the corruption is undetectable without manual
header inspection.

Assemble the header block:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- copied verbatim, not rederived}

The header appears immediately after any frontmatter. All six fields are present.
The header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning as the first section of the artifact body. Position it
before any mock content. Separate from the header and from the body with ---
delimiters.

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. The sections are right; the contents are invented. A real
    {skill-id} run is required before any evidence-based decision can be made
    from this namespace.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
    mechanisms) are reliable. Specific claims (competitor names, market data,
    research findings) may be partially accurate or partially fabricated. Review
    for plausibility before accepting coverage.

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
    mechanisms are reliable. Content is synthetically generated but structurally
    representative. Adequate for structural planning and coverage orientation at
    Tier 1. REAL-REQUIRED at Tier 2+ for critical namespaces (trace,
    scout-feasibility, listen).

---

STEP A-3 -- GENERATE ARTIFACT BODY

Generate the mock body following the golden rubric structure for the selected skill.
The body must include:
  - All required section headings for the skill
  - Required tables or lists in the expected positions
  - Gate or verdict line where the skill produces one
  - Enforcement mechanisms in the expected positions

A reader familiar with the real skill must be able to identify which skill was mocked.
Generic prose without skill-specific structure fails.

---

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

The final line of the artifact is:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit only if this skill was called from within a mock-review session to regenerate
a thin namespace.
```

---

## Scoring prediction summary

| Variant | Axis | New criteria targeted | Denominator | Expected composite |
|---------|------|-----------------------|-------------|-------------------|
| V-01 | Inertia framing (guarantee-break) | C-25 only | 18 | ~99.4 |
| V-02 | Phrasing register (cross-site reference) | C-26 only | 18 | ~99.4 |
| V-03 | Lifecycle emphasis (R7 baseline) | none | 18 | ~98.9 |
| V-04 | Output format + role sequence (C-25 + C-26 minimal, table S-3) | C-25 + C-26 | 18 | 100 |
| V-05 | Role sequence (full convergence, prose) | C-25 + C-26 | 18 | 100 |

**Key discriminants**:
- V-01 vs V-02: Isolates whether guarantee-break framing (C-25) or cross-site reference
  (C-26) is the stronger standalone addition. Both target the same sentence in S-3 but
  from opposite directions -- C-25 points backward to the commitment; C-26 points across
  to the mirrored site.
- V-04 vs V-05: Tests whether minimal form ("the guarantee stated above is broken: ...
  producing the same silent category mismatch described at the consumption site") within
  the existing C-23 sentence satisfies both C-25 and C-26, or whether the prose-emphasis
  layout of V-05 produces meaningfully different execution behavior. If both score 100,
  the criteria are form-neutral.
- V-03 vs V-01/V-02: Confirms that C-25 and C-26 each add a measurable increment over the
  R7 baseline. If V-03 scores 98.9, each single-criterion addition should add ~0.28 points
  at the aspirational layer (1/18 * 10 * 0.5 for the partial slot freed).
- V-01 vs V-02 vs V-04/V-05: The interesting question for R8 is whether C-25 or C-26 is
  the load-bearing addition. R7's pattern had C-23 as the stronger single addition over
  C-24. R8's two new criteria are structurally different: C-25 is a logical connective
  (backward-pointing to C-21), C-26 is a navigational pointer (sideways to C-20). The
  relative strength between a logical connective and a navigational pointer under execution
  pressure is the primary empirical question this round introduces.
