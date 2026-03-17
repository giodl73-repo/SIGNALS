---
skill: quest-variate
skill_target: org-roles
date: 2026-03-16
round: R5
rubric_version: v5
status: variate
---

# org-roles Variate — Round 5

**Date:** 2026-03-16
**Skill:** org-roles
**Rubric:** v5 (C-01 through C-25; new in v5: C-21 uniqueness mandate by construction, C-22 cross-step
count integrity, C-23 extension field commitment block with provenance, C-24 schema field name precision
gate, C-25 per-expert attribute gate in domain derivation)
**Round:** R5 — single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

---

## Round 5 Variation Map

| V | Axis | Primary C targets | Hypothesis |
|---|------|------------------|------------|
| V-01 | role sequence | C-21 PASS, C-22 PASS, C-23 PASS, C-24 PASS, C-25 PASS | Inertia-first role sequence — Phase 1 derives the status-quo claim from a first-pass context read before any domain expert is named; domain experts are then derived in Phase 2 explicitly in response to the Phase 1 challenge; the Phase 0 extension commitment names the Phase 1 artifact as its population source, grounding C-23's provenance requirement by construction |
| V-02 | output format | C-21 PASS, C-22 PASS, C-23 PASS, C-24 PASS, C-25 PASS | Field Contract document in Phase 0 names all six schema field identifiers as string-literal contract terms; C-24's identifier precision becomes a structural consequence of the contract rather than a gate assertion; the role-writing gate checks fields by referencing contract item numbers, making identifier precision load-bearing at every step |
| V-03 | lifecycle emphasis | C-21 PASS, C-22 PASS, C-23 PASS, C-24 PASS, C-25 PASS | PREPARE / WRITE / GATE triad at every output-producing step; the PREPARE sub-step of Phase 6 names "count Phase 5 output files" as a required input before registry writing begins — grounding C-22 in the lifecycle structure rather than a gate assertion; the PREPARE sub-step of Phase 5 names Phase 0 field identifiers as required inputs, making C-24 a pre-write condition |
| V-04 | phrasing register + inertia framing | C-21 PASS, C-22 PASS, C-23 PASS, C-24 PASS, C-25 PASS | Diagnostic-question framing for each phase (the model must answer a framing question before producing structured output) combined with a dedicated inertia specification phase; the Phase 0 diagnostic question is "What domain-specific tension will this registry expose?" — forcing declaration of the extension commitment in the answer before any context is read |
| V-05 | all four axes | C-21 PASS, C-22 PASS, C-23 PASS, C-24 PASS, C-25 PASS | Maximum integration: inertia-first role sequence (V-01) + Field Contract in Phase 0 (V-02) + PREPARE/WRITE/GATE triad (V-03) + diagnostic-question framing (V-04); all five new criteria satisfied by structural construction, not gate assertions alone |

**R5 thesis:** All four R4 golden variates failed at least one of C-23 and C-24. R5 adds Phase 0 (extension commitment with all three required elements) and field-identifier precision to the role-writing gate across all five variations. The variation axes test whether structural approaches (field contract, lifecycle triad, role sequence) produce stronger C-21–C-25 coverage than assertion-based approaches (gate items alone). Falsifiable: if all five variations score GOLDEN and the gap between best and worst is less than 2 points, the five new criteria are satisfied adequately by any structural approach and the axes are equally valid. If the spread exceeds 2 points, structural integration order matters.

---

## V-01 — Role Sequence: Inertia-First

**axis:** role sequence
**hypothesis:** In R4 variates (V-01 through V-04), the status-quo claim was derived in Phase 2
or Phase 3 — after domain experts were already named in Phase 1. This variate reverses that
sequence: Phase 1 makes a first-pass context read to identify only the existing system's
claimed sufficiency, then Phase 2 derives domain experts explicitly in response to that
challenge. Each domain expert must include an inertia-response question that directly
falsifies the Phase 1 status-quo claim for their concern. The Phase 0 extension commitment
names "Phase 1, INERTIA-SURFACE block, status-quo claim" as its population source — a
provenance reference that satisfies C-23 before Phase 1 is run.
Falsifiable: if domain expert frames still default to generic concerns rather than
domain-specific opposition to the Phase 1 challenge, inertia-first sequencing adds
structural layers without changing the quality of derived expert frames.

---

You are running `/org-roles {topic}`.

---

PHASE 0 — EXTENSION COMMITMENT

Before reading any context, declare the registry extension this skill will produce.

```
EXTENSION-COMMITMENT:
  field_name: inertia_surface
  population_source: Phase 1, INERTIA-SURFACE block, status-quo claim field
  purpose: Preserves the domain-specific status-quo argument this registry was composed
    to challenge; enables downstream skills (org-review, org-chart) to reconstruct the
    design tension the role set was built to surface — why the feature might not be
    necessary, stated in domain vocabulary before any role was written
```

GATE — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT block is written
2. All three elements present: field_name (a single identifier), population_source (names
   a specific step and artifact), purpose (states the domain concern it captures)
3. population_source names Phase 1 as the origin step — not a future phase

---

PHASE 1 — INERTIA SPECIFICATION (first-pass context read; domain experts not yet named)

Read `{topic}` context for existing system capabilities only. Do not derive domain experts.
Write an INERTIA-SURFACE block:

```
INERTIA-SURFACE for {topic}:

  Status-quo claim: [one sentence stating what the existing system already provides that
    makes the proposed feature redundant; use vocabulary specific to `{topic}` context;
    not a generic "the current approach is sufficient" — name the specific capability]

  Why-not-build questions (at minimum three; domain-specific; each asks what the current
  system already handles):
    1. What does the existing system already do that makes this feature redundant?
       (Name the specific existing mechanism; do not assume it is absent.)
    2. [domain-specific question derived from a second existing capability]
    3. [domain-specific question derived from a third existing capability]
```

The status-quo claim will be copied verbatim to the `inertia_surface` extension field in
Phase 6. It must be a complete sentence in `{topic}` domain vocabulary.

GATE — Phase 1 complete when ALL of the following are TRUE:
1. INERTIA-SURFACE block is written
2. Status-quo claim is a complete sentence using vocabulary specific to `{topic}` context
   (not "the existing approach is sufficient" without naming the specific capability)
3. At least three why-not-build questions are listed, each naming a current system capability
4. No domain expert names appear in this block — derivation happens in Phase 2

---

PHASE 2 — CONTEXT ANALYSIS (domain experts; derived in response to Phase 1 challenge)

Read full `{topic}` context. Write a DOMAIN-ANALYSIS block. Domain experts must be
derived in explicit response to the Phase 1 status-quo challenge — each expert exists
because the status-quo claim, if left unchallenged, would miss a real concern.

```
DOMAIN-ANALYSIS for {topic}:

  Domain concerns (at minimum three; drawn from context; each is a failure mode, blind
  spot, or risk the Phase 1 status-quo claim does not acknowledge):
    1. [concern: specific failure the existing system produces that the status-quo claim
       omits or understates]
    2. [concern]
    3. [concern]

  Domain experts derived from concerns:
    - Expert name: [slug in domain vocabulary — not "domain-expert" or "expert-1"]
      Concern link: [which concern above, by number]
      Domain-vocabulary frame: [one sentence using vocabulary from that concern]
      Verify focus: [what artifact or behavior this expert checks first]
      Inertia-response question: [exact question form: "What evidence shows that
        [Phase 1 status-quo claim] fails for [this expert's concern]?"]
    (repeat for each derived expert — at minimum one)
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 2.

GATE — Phase 2 complete when ALL of the following are TRUE:
1. DOMAIN-ANALYSIS block is written with a populated Domain concerns list
2. At least three domain concerns are present using vocabulary specific to `{topic}`
3. Each derived expert entry lists all five attributes individually:
   name, concern link, domain-vocabulary frame, verify focus, inertia-response question
   — checked per expert, not as a total count; each attribute must be substantive
4. Each inertia-response question references the Phase 1 status-quo claim by content
5. No stock role names (pm, architect, strategy, inertia-advocate) appear in this block

---

PHASE 3 — STOCK ROLES

After Phase 2 GATE passes, declare the four stock roles:

```
STOCK-ROLES:
  - pm
  - architect
  - strategy
  - inertia-advocate (orientation and verify_questions sourced from Phase 1 INERTIA-SURFACE)
```

The inertia-advocate's role file (written in Phase 5) must use Phase 1's why-not-build
questions as its `verify_questions`. Its `orientation.frame` must anchor to the Phase 1
status-quo claim as its epistemic viewpoint — not a generic "challenges every proposal."

GATE — Phase 3 complete when ALL of the following are TRUE:
1. STOCK-ROLES block lists all four names
2. inertia-advocate entry references Phase 1 as source for orientation and verify_questions
3. Phase 1 INERTIA-SURFACE block is confirmed available for Phase 5 role-file authoring

---

PHASE 4 — OUTPUT AREA

Derive the area slug from `{topic}` context. Write:

```
OUTPUT-AREA: .craft/roles/{area}/
```

GATE — Phase 4 complete when ALL of the following are TRUE:
1. OUTPUT-AREA line is written
2. Area slug uses domain vocabulary from `{topic}` (not `default`, `generic`, `roles`)
3. Path format is exactly `.craft/roles/{area}/`

---

PHASE 5 — WRITE ROLE FILES

Write one `.md` file per role to `.craft/roles/{area}/`.
Order: domain-expert roles (Phase 2) first, then stock roles (Phase 3).
For the inertia-advocate: source `orientation.frame` and `verify_questions` from Phase 1.

Read each FAILURE MODE and WORKED EXAMPLE pair before filling in the annotated field:

```yaml
---
name: {role-name}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Perspective statement — how this role sees work in this domain.
    Phrased as an epistemic viewpoint: "Sees every X through the lens of Y."
    Domain experts: use vocabulary from Phase 2 domain-vocabulary frame.
    Inertia-advocate: use the Phase 1 status-quo claim as the perspective anchor.

    FAILURE MODE: task-list frame — frame becomes a job description.
    WORKED EXAMPLE (bad):  "Responsible for reviewing spec artifacts and ensuring
      requirements are captured before engineering handoff."
    WORKED EXAMPLE (good): "Sees every spec artifact through the lens of whether
      the stated requirements survive contact with the actual system boundary —
      scanning for the gap between what the spec assumes and what the system enforces."}

  serves: |
    {Beneficiary statement — who depends on this role's signal and what they receive.
    Must name a beneficiary. Must not restate frame.

    FAILURE MODE: frame restatement — serves carries the same information as frame.
    WORKED EXAMPLE (bad):  "Ensures specs are evaluated for boundary correctness."
      (restates frame in different words — zero new signal)
    WORKED EXAMPLE (good): "Engineers receiving the spec as a handoff artifact —
      they get a boundary-gap verdict before the spec becomes load-bearing in
      implementation."}

lens:
  verify_questions:
    - "{Actionable question answerable by reading an artifact, running code, or
       inspecting a measurable outcome — references a specific artifact type,
       behavior, or outcome}"
    - "{Second question: must be one that no other role in this registry would
       prioritize first — confirm before writing: if any other role would ask
       this question first, revise until this question is uniquely attributable
       to this role's frame}"
    - "{Domain experts only: inertia-response question sourced from Phase 2 —
       'What evidence shows that [Phase 1 status-quo claim] fails for this
       concern?' — copy from the Phase 2 DOMAIN-ANALYSIS inertia-response
       question for this expert}"

  simplify_rules:
    - "{Opinionated constraint that reduces scope or removes ambiguity — phrased
       as a prohibition or elimination ('Skip X unless Y', 'Do not include Z
       when W'), not a description of what the role does.

       FAILURE MODE: scope description — rule names a priority area without
       excluding anything.
       WORKED EXAMPLE (bad):  'Focus on boundary correctness and constraint-gap
         concerns relevant to this role.' (names priority, excludes nothing)
       WORKED EXAMPLE (good): 'Skip boundary analysis for internal-only components;
         flag only surfaces exposed to external callers or cross-service consumers.'}"

expertise:
  depth: {expert | practitioner | senior | principal}
  relevance: |
    {Why this depth level is calibrated to this domain — not a restatement of
    the role name. Must reference a domain-specific constraint or artifact type
    that justifies the seniority level.}

scope:
  primary: |
    {The main concern this role surfaces in reviews and decisions. One sentence,
    domain-specific.}
  boundary: |
    {What this role explicitly does NOT own or evaluate. One sentence that
    excludes something specific.}

collaborates_with:
  - {role-name}
  # List only roles present in this registry output (Phase 2 experts + Phase 3 stock).
  # FAILURE MODE (type 1) — PHANTOM ROLE: naming a role absent from the output set.
  # FAILURE MODE (type 2) — UNIVERSALIST LISTING: "works with all roles" or equivalent.
  # Both failure modes invalidate the collaborates_with field.
```

GATE — Phase 5 complete when ALL of the following are TRUE:
1. One `.md` file exists per role in `.craft/roles/{area}/`
2. Every role file uses exact field identifiers `verify_questions` and `simplify_rules`
   — not shortened forms (`verify`, `simplify`, `questions`, `rules`) — the identifier
   strings appear verbatim as YAML keys in each file
3. Inertia-advocate `orientation.frame` anchors to the Phase 1 status-quo claim;
   `verify_questions` sourced from Phase 1 why-not-build questions
4. Each domain expert's `verify_questions` includes a Phase 2 inertia-response question
5. `collaborates_with` lists only roles present in Phase 5 output (no phantom names,
   no universalist entries)

---

PHASE 6 — REGISTRY SUMMARY

Write `.craft/roles/{area}/REGISTRY.md`:

```
---
area: {area}
generated: {date}
---

## Registry Summary

total_roles: [COUNT — count the .md files written in Phase 5 before writing this
  number; do not carry forward the planned count from Phase 3 — verify against
  actual Phase 5 output]

stock_roles:
  - pm
  - architect
  - strategy
  - inertia-advocate

domain_experts:
  - name: {expert-name}
    derivation_source: Phase 2 domain concern #[N]
  (one entry per derived expert — name and derivation_source both required)

coverage_gaps: |
  {Any Phase 2 concern not addressed by any derived expert; or "none detected."
  Not a stub — write the finding explicitly.}

inertia_surface: |
  {The Phase 1 status-quo claim verbatim — copy the exact sentence from the
  INERTIA-SURFACE block. Do not paraphrase.}

Generated by: /org-roles {topic} — {date}
```

FAILURE MODE — HEADING STUB: a section header with no content below it is not a
complete registry entry. "## Registry Summary" with no populated fields beneath it
fails this step unconditionally.

GATE — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.craft/roles/{area}/REGISTRY.md`
2. `total_roles` equals the count of `.md` files written in Phase 5 (count Phase 5
   output; do not estimate or self-report from prior phases)
3. `domain_experts` lists each derived expert with both `name` and `derivation_source`
4. `inertia_surface` contains the Phase 1 status-quo claim verbatim — not paraphrased
5. No heading stubs: every section has substantive content below its header

---

## V-02 — Output Format: Field Contract Document

**axis:** output format
**hypothesis:** In R4 variates, C-24's field identifier precision requirement was
expressed as a gate assertion ("every role file uses exact identifiers `verify_questions`
and `simplify_rules`"). The gate works, but the model generates output first and checks
identifiers second. This variate moves identifier precision to Phase 0: the FIELD CONTRACT
names all six top-level schema fields and their exact sub-field identifiers as string-literal
contract terms. The role-writing gate in Phase 5 checks fields by referencing contract
item numbers — making precision a structural consequence of the contract, not a
post-generation gate. C-18 contrastive pairs appear in the contract, not inside the YAML
template annotations, keeping the template scannable.
Falsifiable: if the model generates role files that quote contract terms verbatim but
still produces shortened identifiers in actual YAML output, the contract structure
positions but does not enforce identifier precision — a gate-only assertion would
have been equivalent.

---

You are running `/org-roles {topic}`.

---

PHASE 0 — EXTENSION COMMITMENT + FIELD CONTRACT

**PART A — EXTENSION COMMITMENT**

```
EXTENSION-COMMITMENT:
  field_name: inertia_surface
  population_source: Phase 2, INERTIA-SURFACE block, status-quo claim field
  purpose: Preserves the domain-specific argument for why the proposed feature may be
    unnecessary; provides downstream consumers of this registry a design-level tension
    anchor — the status-quo position this role set was assembled to stress-test
```

**PART B — FIELD CONTRACT**

All role files must conform to this contract. Field identifiers are binding string
literals — any shortened or paraphrased variant is a contract violation that breaks
downstream consumers.

```
FIELD-CONTRACT for /org-roles:

  [FC-1]  name
          type: string
          constraint: domain-vocabulary slug; not "domain-expert", "expert-1", or generic labels

  [FC-2]  orientation.frame
          type: string
          constraint: epistemic viewpoint — "sees X through the lens of Y"; NOT a task list
          BAD:  "Responsible for reviewing spec artifacts and ensuring requirements are captured"
          GOOD: "Sees every spec draft through the lens of whether stated requirements survive
                 contact with the actual system boundary — scanning for spec-to-enforcement gaps"

  [FC-3]  orientation.serves
          type: string
          constraint: beneficiary statement; NOT a restatement of frame
          BAD:  "Ensures specs are evaluated for boundary correctness" (restates [FC-2])
          GOOD: "Engineers receiving the spec as a handoff — they get a gap verdict before
                 the spec becomes load-bearing in implementation"

  [FC-4]  lens.verify_questions
          type: list (minimum two items)
          EXACT IDENTIFIER: verify_questions
          VIOLATION: `verify`, `questions`, `verify_list`, `checks` — all are contract violations
          constraint: each question answerable by reading an artifact, running code, or
            inspecting a measurable outcome; at least one question must be uniquely
            attributable to this role's frame — no other role in this registry would
            prioritize that question first; confirm this before writing the question
          BAD:  "Is the design correct?" (unmeasurable; any role could ask this)
          GOOD: "Does the emitted event schema match the consumer's declared schema version,
                 verifiable in the integration test suite?"

  [FC-5]  lens.simplify_rules
          type: list (minimum one item)
          EXACT IDENTIFIER: simplify_rules
          VIOLATION: `simplify`, `rules`, `constraints`, `guidelines` — all are contract violations
          constraint: opinionated exclusion or scope reduction — "Skip X unless Y"; NOT a
            description of what the role does
          BAD:  "Focus on boundary correctness and constraint-gap concerns" (describes, not excludes)
          GOOD: "Skip boundary analysis for internal-only components; flag only external surfaces"

  [FC-6]  expertise.depth
          type: enum: expert | practitioner | senior | principal

  [FC-7]  expertise.relevance
          type: string
          constraint: justification referencing a domain-specific constraint, not a role restatement

  [FC-8]  scope.primary
          type: string
          constraint: the main concern this role surfaces; one sentence; domain-specific

  [FC-9]  scope.boundary
          type: string
          constraint: what this role does NOT own; must exclude something specific

  [FC-10] collaborates_with
          type: list
          constraint: only roles present in this registry's output
          CONTRACT VIOLATION (type 1) — PHANTOM: a role name absent from the output set
          CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent
          Both violations are gate failures
```

GATE — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT has all three elements: `field_name`, `population_source`, `purpose`
2. FIELD-CONTRACT is written with all ten contract items [FC-1] through [FC-10]
3. Items [FC-4] and [FC-5] display their exact identifiers — the strings `verify_questions`
   and `simplify_rules` appear verbatim as the EXACT IDENTIFIER values

---

PHASE 1 — CONTEXT ANALYSIS (domain experts only — stock roles not yet named)

Read `{topic}` context. Write a DOMAIN-ANALYSIS block:

```
DOMAIN-ANALYSIS for {topic}:

  Domain concerns (at minimum three; drawn from actual context, not generic templates):
    1. [concern: specific failure mode, blind spot, or risk unique to this domain]
    2. [concern]
    3. [concern]

  Domain experts derived from concerns:
    - Expert name: [slug per FIELD-CONTRACT [FC-1] — domain vocabulary, not generic]
      Concern link: [which concern above, by number]
      Domain-vocabulary frame: [one sentence using vocabulary from that concern]
      Verify focus: [what artifact or behavior this expert checks first]
    (repeat for each derived expert — at minimum one)
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 1.

GATE — Phase 1 complete when ALL of the following are TRUE:
1. DOMAIN-ANALYSIS block is written with a populated Domain concerns list
2. At least three domain concerns are listed using vocabulary specific to `{topic}`
3. Each derived expert entry lists all four attributes individually:
   name, concern link, domain-vocabulary frame, verify focus
   — checked per expert, not as a total count; each attribute must be substantive
4. No stock role names (pm, architect, strategy, inertia-advocate) appear in this block

---

PHASE 2 — INERTIA SPECIFICATION

Use Phase 1 domain concerns to write a domain-specific status-quo claim. Write an
INERTIA-SURFACE block:

```
INERTIA-SURFACE for {topic}:

  Status-quo claim: [one sentence stating what the existing approach already provides
    that makes the proposed feature redundant — derived from Phase 1 concerns, using
    Phase 1 vocabulary; not a generic "it works fine"]

  Challenge questions (at minimum three; domain-specific):
    1. Why is the current approach insufficient — what specific failure does the status
       quo produce that this feature resolves? (Name the failure; do not assume it.)
    2. [domain-specific challenge derived from Phase 1 concern 2]
    3. [domain-specific challenge derived from Phase 1 concern 3]
```

The status-quo claim will be written verbatim to the `inertia_surface` field in Phase 6.

GATE — Phase 2 complete when ALL of the following are TRUE:
1. INERTIA-SURFACE block is written
2. Status-quo claim is a complete sentence using Phase 1 domain vocabulary
3. At least three challenge questions reference specific Phase 1 concerns

---

PHASE 3 — STOCK ROLES

```
STOCK-ROLES:
  - pm
  - architect
  - strategy
  - inertia-advocate (verify_questions sourced from Phase 2 challenge questions)
```

GATE — Phase 3 complete when ALL of the following are TRUE:
1. STOCK-ROLES block lists all four names
2. inertia-advocate is listed with Phase 2 as source for `verify_questions`
3. Phase 2 INERTIA-SURFACE block is confirmed available

---

PHASE 4 — OUTPUT AREA

```
OUTPUT-AREA: .craft/roles/{area}/
```

GATE — Phase 4 complete when ALL of the following are TRUE:
1. OUTPUT-AREA is written
2. Area slug uses domain vocabulary (not `default`, `generic`, `roles`)
3. Path format is exactly `.craft/roles/{area}/`

---

PHASE 5 — WRITE ROLE FILES (per FIELD CONTRACT)

Read FIELD-CONTRACT [FC-1] through [FC-10] before writing. Write one `.md` file per role.
Domain-expert roles first (Phase 1), then stock roles (Phase 3).

Template — fill every field per the FIELD CONTRACT items above:

```yaml
---
name: {role-name per [FC-1]}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Per [FC-2]: epistemic viewpoint. Domain experts: use Phase 1 domain-vocabulary frame.
    Inertia-advocate: anchor to Phase 2 status-quo claim as epistemic stance.}
  serves: |
    {Per [FC-3]: beneficiary statement — not a restatement of frame.}

lens:
  verify_questions:
    - "{Per [FC-4]: actionable, artifact-specific question}"
    - "{Per [FC-4] uniqueness requirement: no other role in this registry would
       prioritize this question first — confirm before writing; revise if any other
       role would ask this question first}"
  simplify_rules:
    - "{Per [FC-5]: opinionated exclusion or scope reduction — not a description}"

expertise:
  depth: {per [FC-6]}
  relevance: |
    {Per [FC-7]: domain-specific justification for depth level}

scope:
  primary: |
    {Per [FC-8]: main concern, one sentence}
  boundary: |
    {Per [FC-9]: explicit exclusion, one sentence}

collaborates_with:
  - {role-name per [FC-10]: registry members only}
```

GATE — Phase 5 complete when ALL of the following are TRUE:
1. One `.md` file exists per role in `.craft/roles/{area}/`
2. Every file uses exact identifiers `verify_questions` and `simplify_rules` per
   FIELD-CONTRACT [FC-4] and [FC-5] — the identifier strings appear verbatim as YAML
   keys; not `verify`, `simplify`, or any variant
3. Inertia-advocate `verify_questions` sourced from Phase 2 challenge questions;
   `orientation.frame` anchors to Phase 2 status-quo claim
4. Each role's `verify_questions` includes at least one question uniquely attributable
   to that role's frame per [FC-4] uniqueness requirement
5. `collaborates_with` contains no CONTRACT VIOLATIONS (type 1 phantom or type 2
   universalist) per [FC-10]

---

PHASE 6 — REGISTRY SUMMARY

Write `.craft/roles/{area}/REGISTRY.md`:

```
---
area: {area}
generated: {date}
---

## Registry Summary

total_roles: [COUNT — before writing this number, count the .md files written in Phase 5;
  do not carry forward a planned count — verify against actual Phase 5 output]

stock_roles:
  - pm
  - architect
  - strategy
  - inertia-advocate

domain_experts:
  - name: {expert-name}
    derivation_source: Phase 1 domain concern #[N]
  (one entry per derived expert)

coverage_gaps: |
  {Phase 1 concerns not addressed by any derived expert; or "none detected."}

inertia_surface: |
  {Phase 2 status-quo claim verbatim — exact sentence from INERTIA-SURFACE block.
  Do not paraphrase.}

Generated by: /org-roles {topic} — {date}
```

FAILURE MODE — HEADING STUB: "## Registry Summary" with no populated fields is not a
registry. Every field above must contain substantive content.

GATE — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.craft/roles/{area}/REGISTRY.md`
2. `total_roles` equals the count of `.md` files written in Phase 5 (count Phase 5
   output; do not estimate)
3. `domain_experts` lists each expert with `name` and `derivation_source`
4. `inertia_surface` contains the Phase 2 status-quo claim verbatim
5. No heading stubs — every field has substantive content

---

## V-03 — Lifecycle Emphasis: PREPARE / WRITE / GATE Triad

**axis:** lifecycle emphasis
**hypothesis:** In R4 variates, C-22's count cross-reference requirement was satisfied
by a gate assertion in Phase 6 ("total_roles equals the count from Phase 5 output").
But the gate runs after the registry is already partially written — the model may have
already committed a self-reported count before checking. This variate adds a PREPARE
sub-step to every output-producing phase. Phase 6's PREPARE sub-step names "count
Phase 5 output files" as a required input before the first word of REGISTRY.md is
written — making C-22 a pre-write input requirement, not a post-write gate assertion.
Phase 5's PREPARE sub-step names "Phase 0 field identifiers" as required inputs —
making C-24 a pre-write dependency check. Both shifts move the compliance burden from
gate assertion (after generation) to preparation (before generation).
Falsifiable: if PREPARE sub-steps are treated as nominal headers and the model still
generates output without performing the named pre-write checks, lifecycle structure
alone does not prevent post-hoc rationalization.

---

You are running `/org-roles {topic}`.

---

PHASE 0 — EXTENSION COMMITMENT

**PREPARE:** Nothing required from prior phases.

**WRITE:**

```
EXTENSION-COMMITMENT:
  field_name: inertia_surface
  population_source: Phase 2, INERTIA-SURFACE block, status-quo claim field
  purpose: Records the domain-specific case for the status quo that this registry's
    inertia-advocate is built to mount; gives downstream consumers the design-level
    tension the role set was composed to stress-test
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT block is written
2. All three required elements present: `field_name` (single identifier with no spaces),
   `population_source` (names a specific step and artifact from this skill's phases),
   `purpose` (states what domain concern the extension field captures)
3. `population_source` names Phase 2 as the origin step

---

PHASE 1 — CONTEXT ANALYSIS (domain experts only — stock roles not yet named)

**PREPARE:** Read `{topic}` context. Do not name stock roles in this phase.

**WRITE:** Produce a DOMAIN-ANALYSIS block:

```
DOMAIN-ANALYSIS for {topic}:

  Domain concerns (at minimum three; drawn from actual context, not generic templates):
    1. [concern: specific failure mode, blind spot, or risk unique to this domain]
    2. [concern]
    3. [concern]

  Domain experts derived from concerns:
    - Expert name: [slug in domain vocabulary — not "domain-expert" or "expert-1"]
      Concern link: [which concern above, by number]
      Domain-vocabulary frame: [one sentence using vocabulary from that concern]
      Verify focus: [what artifact or behavior this expert checks first]
    (repeat for each derived expert — at minimum one)
```

**GATE** — Phase 1 complete when ALL of the following are TRUE:
1. DOMAIN-ANALYSIS block is written with a populated Domain concerns list
2. At least three domain concerns are listed using vocabulary specific to `{topic}`
3. Each derived expert entry lists all four attributes checked per expert individually —
   name, concern link, domain-vocabulary frame, verify focus — each entry is complete;
   a partial entry (name only, or name + concern link only) does not satisfy this item
4. No stock role names (pm, architect, strategy, inertia-advocate) appear in this block

---

PHASE 2 — INERTIA SPECIFICATION

**PREPARE:** Retrieve Phase 1 DOMAIN-ANALYSIS domain concerns. The status-quo claim
must be derivable from Phase 1 vocabulary — do not invent concerns not in Phase 1.

**WRITE:**

```
INERTIA-SURFACE for {topic}:

  Status-quo claim: [one sentence arguing the existing approach is sufficient; derived
    from Phase 1 domain concerns vocabulary; not a generic "it works fine"]

  Challenge questions (at minimum three; domain-specific; each derived from a Phase 1
  concern):
    1. Why is the current approach insufficient — what specific failure does the status
       quo produce that this feature resolves? (Name the failure; do not assume it.)
    2. [domain-specific challenge derived from Phase 1 concern 2]
    3. [domain-specific challenge derived from Phase 1 concern 3]
```

The status-quo claim will be copied verbatim to `inertia_surface` in Phase 6.

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. INERTIA-SURFACE block is written
2. Status-quo claim is a complete sentence using Phase 1 domain vocabulary
3. At least three challenge questions reference Phase 1 concerns by content

---

PHASE 3 — STOCK ROLES

**PREPARE:** Retrieve Phase 2 INERTIA-SURFACE challenge questions for inertia-advocate.

**WRITE:**

```
STOCK-ROLES:
  - pm
  - architect
  - strategy
  - inertia-advocate (verify_questions: Phase 2 INERTIA-SURFACE challenge questions)
```

**GATE** — Phase 3 complete when ALL of the following are TRUE:
1. STOCK-ROLES block lists all four names
2. inertia-advocate entry identifies Phase 2 as source
3. Phase 2 challenge questions confirmed available

---

PHASE 4 — OUTPUT AREA

**PREPARE:** Derive area slug from `{topic}` context.

**WRITE:**

```
OUTPUT-AREA: .craft/roles/{area}/
```

**GATE** — Phase 4 complete when ALL of the following are TRUE:
1. OUTPUT-AREA is written
2. Area slug uses domain vocabulary (not `default`, `generic`, `roles`)
3. Path is exactly `.craft/roles/{area}/`

---

PHASE 5 — WRITE ROLE FILES

**PREPARE:** Before writing any role file, confirm all of the following inputs are available:
- Phase 0 EXTENSION-COMMITMENT: `field_name` = `inertia_surface`
- Phase 0 field identifiers: `verify_questions` and `simplify_rules` (exact strings;
  retrieve and confirm spelling before beginning Phase 5 output)
- Phase 1 DOMAIN-ANALYSIS: domain expert names, frames, verify focuses
- Phase 2 INERTIA-SURFACE: status-quo claim, challenge questions
- Phase 3 STOCK-ROLES: pm, architect, strategy, inertia-advocate
- Phase 4 OUTPUT-AREA path

PREPARE is complete when all six inputs are confirmed available. Do not begin WRITE
until PREPARE is confirmed.

**WRITE:** One `.md` file per role to `.craft/roles/{area}/`. Domain experts first,
then stock roles.

Use this template. Read each FAILURE MODE annotation before filling in the field:

```yaml
---
name: {role-name}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Epistemic viewpoint — "Sees every X through the lens of Y."
    Domain experts: Phase 1 domain-vocabulary frame as anchor.
    Inertia-advocate: Phase 2 status-quo claim as epistemic stance.

    FAILURE MODE: task-list frame.
    WORKED EXAMPLE (bad):  "Responsible for reviewing artifacts and ensuring
      requirements are captured."
    WORKED EXAMPLE (good): "Sees every artifact through the lens of whether
      the stated contract matches the enforced boundary — gap-first reading."}

  serves: |
    {Beneficiary statement. Must name a beneficiary. Must not restate frame.

    FAILURE MODE: frame restatement.
    WORKED EXAMPLE (bad):  "Ensures artifacts are evaluated for contract
      correctness." (same information as frame)
    WORKED EXAMPLE (good): "Engineers receiving the artifact as a handoff —
      they get a contract-gap verdict before the artifact is load-bearing."}

lens:
  verify_questions:
    - "{Actionable question answerable by artifact-read, code-run, or measurable
       outcome — references a specific artifact type or behavior}"
    - "{Second question: must be one that no other role in this registry would
       prioritize first — confirm this claim before writing; if any other role
       would ask it first, revise until it is uniquely attributable to this
       role's frame}"

  simplify_rules:
    - "{Opinionated exclusion or scope reduction. 'Skip X unless Y.'
       FAILURE MODE: scope description without exclusion.
       WORKED EXAMPLE (bad):  'Focus on contract correctness concerns.'
       WORKED EXAMPLE (good): 'Skip internal component analysis; flag only
         externally exposed interfaces.'}"

expertise:
  depth: {expert | practitioner | senior | principal}
  relevance: |
    {Domain-specific justification for depth level — not a restatement of role name.}

scope:
  primary: |
    {Main concern this role surfaces. One sentence.}
  boundary: |
    {What this role explicitly does NOT own. One sentence.}

collaborates_with:
  - {role-name — registry members only}
  # FAILURE MODE (type 1): PHANTOM ROLE — name absent from this registry output.
  # FAILURE MODE (type 2): UNIVERSALIST LISTING — "all roles" or equivalent.
```

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. One `.md` file exists per role in `.craft/roles/{area}/`
2. Every role file uses exact field identifiers `verify_questions` and `simplify_rules`
   — the identifier strings appear verbatim as YAML keys; not `verify`, `simplify`,
   `questions`, `rules`, or any other variant
3. Inertia-advocate: `orientation.frame` anchors to Phase 2 status-quo claim;
   `verify_questions` sourced from Phase 2 challenge questions
4. Each role has at least one `verify_questions` entry uniquely attributable to
   that role's frame
5. No `collaborates_with` entries contain phantom role names or universalist statements

---

PHASE 6 — REGISTRY SUMMARY

**PREPARE:** Before writing `REGISTRY.md`, perform this count:
- List all `.md` files written in Phase 5 (enumerate them)
- Record the count as `PHASE5_COUNT`
- This count will be written as `total_roles` — do not derive it from Phase 3 STOCK-ROLES
  plus Phase 1 domain expert counts; verify against actual Phase 5 file output

PREPARE is complete when `PHASE5_COUNT` is recorded from Phase 5 file enumeration.

**WRITE:** `.craft/roles/{area}/REGISTRY.md`:

```
---
area: {area}
generated: {date}
---

## Registry Summary

total_roles: {PHASE5_COUNT — the count from the PREPARE enumeration above}

stock_roles:
  - pm
  - architect
  - strategy
  - inertia-advocate

domain_experts:
  - name: {expert-name}
    derivation_source: Phase 1 domain concern #[N]
  (one entry per derived expert)

coverage_gaps: |
  {Phase 1 concerns not addressed by any derived expert; or "none detected."}

inertia_surface: |
  {Phase 2 status-quo claim verbatim — exact sentence from INERTIA-SURFACE block.
  Do not paraphrase.}

Generated by: /org-roles {topic} — {date}
```

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.craft/roles/{area}/REGISTRY.md`
2. `total_roles` equals `PHASE5_COUNT` from the PREPARE enumeration (not a planned count)
3. `domain_experts` lists each derived expert with `name` and `derivation_source`
4. `inertia_surface` contains the Phase 2 status-quo claim verbatim
5. No heading stubs — every section contains substantive content below its header

---

## V-04 — Phrasing Register + Inertia Framing: Diagnostic Question Mode

**axis:** phrasing register (diagnostic questions) + inertia framing (dedicated inertia phase)
**hypothesis:** In R4 variates, each phase opens with an imperative: "Write a DOMAIN-ANALYSIS
block," "Add the four stock roles." The model interprets the imperative as a format instruction
and generates the output block immediately. This variate replaces phase imperatives with
diagnostic questions — each phase opens with a question the model must answer before
producing structured output. Phase 0's question is "What domain-specific tension will this
registry expose?" — forcing the model to state the design-level gap (the extension commitment)
before reading any context. Combined with a dedicated inertia phase positioned before domain
expert derivation, this creates a diagnostic chain: the model names the design tension, then
challenges it, then derives experts to defend it. The inertia framing and diagnostic register
reinforce each other: the challenge is more specific when the model has already stated what
tension the registry exists to expose.
Falsifiable: if the model's domain expert derivation quality (frame specificity, verify-question
precision) is unchanged from imperative-mode variants, the diagnostic framing changes
generation surface without changing generation depth.

---

You are running `/org-roles {topic}`.

---

PHASE 0 — REGISTRY TENSION DECLARATION

**Diagnostic question:** What domain-specific tension will this registry expose — what is
the design-level gap between what teams currently assume and what this feature will require?

Answer this question by writing an EXTENSION-COMMITMENT block. The answer commits the
registry to a named extension field that captures this tension:

```
EXTENSION-COMMITMENT:
  field_name: inertia_surface
  population_source: Phase 2, INERTIA-SURFACE block, status-quo claim field
  purpose: [your answer to the diagnostic question — what domain-specific tension does
    this registry expose? One sentence naming the gap between the current assumption
    and what the feature requires — this becomes the registry's design anchor]
```

GATE — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT block is written with all three elements
2. `field_name` is a single identifier: `inertia_surface`
3. `purpose` answers the diagnostic question: it names a domain-specific tension, not
   a generic statement about role registries

---

PHASE 1 — INERTIA SPECIFICATION

**Diagnostic question:** What does the existing system already provide, and why would a
reasonable stakeholder argue this feature is unnecessary?

Answer this question by writing an INERTIA-SURFACE block. The answer becomes the
basis for the inertia-advocate role:

```
INERTIA-SURFACE for {topic}:

  Status-quo claim: [your answer to the diagnostic question — one sentence using
    vocabulary from `{topic}` context that states what the existing approach already
    handles; this is the strongest reasonable argument against building the feature]

  Challenge questions (at minimum three; each challenges the feature's necessity from
  a different angle):
    1. What specific failure does the status quo produce that this feature resolves?
       (Name the actual failure; if you cannot name it, the status-quo claim may be
       correct — flag this as a coverage gap.)
    2. [second challenge: what does the existing system already do that addresses the
       most important stated use case?]
    3. [third challenge: what would the minimum viable status-quo fix look like, and
       why isn't it sufficient?]
```

The status-quo claim will be copied verbatim to the `inertia_surface` field in Phase 6.

Do not name domain experts in Phase 1. The inertia surface shapes what domain experts
will need to argue against in Phase 2.

GATE — Phase 1 complete when ALL of the following are TRUE:
1. INERTIA-SURFACE block is written
2. Status-quo claim is a complete sentence using `{topic}` domain vocabulary
3. At least three challenge questions are present, each naming a specific capability or
   argument, not a generic "is this necessary?"
4. No domain expert names appear in this block

---

PHASE 2 — CONTEXT ANALYSIS (domain experts; each must answer a Phase 1 challenge)

**Diagnostic question:** Given the Phase 1 status-quo claim, what concerns in this domain
does the existing system fail to handle — and who holds each concern?

Answer by writing a DOMAIN-ANALYSIS block. Each domain expert is your answer to a
specific Phase 1 challenge: the expert exists because the status-quo claim misses their
concern.

```
DOMAIN-ANALYSIS for {topic}:

  Domain concerns (at minimum three; each a failure the Phase 1 status-quo claim
  does not address):
    1. [concern: specific failure mode this domain produces that the status quo omits]
    2. [concern]
    3. [concern]

  Domain experts derived from concerns:
    - Expert name: [slug in domain vocabulary — not "domain-expert" or "expert-1"]
      Concern link: [which concern above, by number]
      Domain-vocabulary frame: [one sentence using vocabulary from that concern —
        how this expert sees the world through their concern's lens]
      Verify focus: [what artifact or behavior this expert checks first to detect
        their concern]
    (repeat for each derived expert — at minimum one)
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 2.

GATE — Phase 2 complete when ALL of the following are TRUE:
1. DOMAIN-ANALYSIS block is written
2. At least three domain concerns are listed using vocabulary specific to `{topic}`
3. Each derived expert entry lists all four attributes checked per expert individually:
   name, concern link, domain-vocabulary frame, verify focus
   — a missing attribute in any single expert entry fails this item
4. No stock role names (pm, architect, strategy, inertia-advocate) appear in this block

---

PHASE 3 — STOCK ROLES

**Diagnostic question:** Which standing perspectives are always needed regardless of domain?

Answer:

```
STOCK-ROLES:
  - pm              (product value and user outcome lens)
  - architect       (technical structure and system boundary lens)
  - strategy        (business model and competitive position lens)
  - inertia-advocate (status-quo sufficiency lens — verify_questions from Phase 1
                      INERTIA-SURFACE challenge questions; orientation.frame anchored
                      to Phase 1 status-quo claim)
```

GATE — Phase 3 complete when ALL of the following are TRUE:
1. STOCK-ROLES lists all four names with their lens descriptors
2. inertia-advocate identifies Phase 1 as source for orientation and verify_questions
3. Phase 1 INERTIA-SURFACE is confirmed available for role-file authoring in Phase 5

---

PHASE 4 — OUTPUT AREA

**Diagnostic question:** What area slug reflects this domain's identity in vocabulary
that downstream skills will recognize?

Answer:

```
OUTPUT-AREA: .craft/roles/{area}/
```

GATE — Phase 4 complete when ALL of the following are TRUE:
1. OUTPUT-AREA is written
2. Area slug uses domain vocabulary (not `default`, `generic`, `roles`)
3. Path is exactly `.craft/roles/{area}/`

---

PHASE 5 — WRITE ROLE FILES

**Diagnostic question:** What does each role see, serve, verify, and simplify — and
which of their verify questions is uniquely theirs?

Answer by writing one `.md` file per role. Domain experts first, then stock roles.
Read each FAILURE MODE annotation before filling in the field:

```yaml
---
name: {role-name}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {How does this role see the world? Phrased as an epistemic viewpoint:
    "Sees every X through the lens of Y — looking for Z."
    Domain experts: use Phase 2 domain-vocabulary frame.
    Inertia-advocate: Phase 1 status-quo claim is this role's epistemic anchor.

    FAILURE MODE: task list. A frame that lists responsibilities rather than
    naming a viewpoint is not an epistemic orientation.
    WORKED EXAMPLE (bad):  "Responsible for reviewing all artifacts and
      coordinating with stakeholders to capture requirements."
    WORKED EXAMPLE (good): "Sees every proposed feature through the lens of
      whether it changes the competitive positioning surface — asking whether
      this is a differentiator, a table-stake, or a distraction."}

  serves: |
    {Who depends on this role's signal? Name the beneficiary and what they receive.
    Must not restate frame.

    FAILURE MODE: frame restatement — serves says the same thing as frame.
    WORKED EXAMPLE (bad):  "Ensures competitive positioning is analyzed for
      each feature." (restates what the frame already says)
    WORKED EXAMPLE (good): "Product leadership deciding whether to fund the
      feature — they receive a signal on whether this is a differentiator or a
      competitive catch-up move before investment is committed."}

lens:
  verify_questions:
    - "{Answerable by artifact-read, code-run, or measurable-outcome inspection}"
    - "{This question is uniquely mine: no other role in this registry would
       prioritize this question first. Before writing, confirm that no other
       derived or stock role would naturally lead with this question — if they
       would, revise until this question could only come from this role's frame.}"

  simplify_rules:
    - "{An opinionated exclusion: 'Skip X unless Y.' Names what is out of scope.
       FAILURE MODE: scope description — names an area of focus without excluding anything.
       WORKED EXAMPLE (bad):  'Focus on competitive positioning and market signal.'
       WORKED EXAMPLE (good): 'Skip competitive analysis for features scoped to internal
         tooling only; flag only user-facing or API-surface changes.'}"

expertise:
  depth: {expert | practitioner | senior | principal}
  relevance: |
    {Why this depth level fits this domain — reference a domain constraint or artifact type.}

scope:
  primary: |
    {Main concern. One sentence.}
  boundary: |
    {Explicit exclusion. One sentence.}

collaborates_with:
  - {role-name — registry members only}
  # FAILURE MODE (type 1): PHANTOM ROLE — name absent from this registry.
  # FAILURE MODE (type 2): UNIVERSALIST LISTING — "all roles" or equivalent.
```

GATE — Phase 5 complete when ALL of the following are TRUE:
1. One `.md` file exists per role in `.craft/roles/{area}/`
2. Every file uses exact identifiers `verify_questions` and `simplify_rules` as YAML
   keys — not shortened or paraphrased variants; the identifier strings appear verbatim
3. Inertia-advocate `orientation.frame` anchors to Phase 1 status-quo claim;
   `verify_questions` sourced from Phase 1 challenge questions
4. Each role has at least one `verify_questions` entry uniquely attributable to that
   role's frame (per the template's uniqueness confirmation instruction)
5. `collaborates_with` contains no phantom role names and no universalist entries

---

PHASE 6 — REGISTRY SUMMARY

**Diagnostic question:** What does this registry as a whole commit to — what design
tension does it hold, what coverage does it provide, and what gaps does it acknowledge?

Answer by writing `.craft/roles/{area}/REGISTRY.md`. Before writing, count the `.md`
files produced in Phase 5 — this count is `total_roles`:

```
---
area: {area}
generated: {date}
---

## Registry Summary

total_roles: [COUNT — enumerate Phase 5 output files; this number must equal the
  actual file count from Phase 5, not the planned count from Phase 3]

stock_roles:
  - pm
  - architect
  - strategy
  - inertia-advocate

domain_experts:
  - name: {expert-name}
    derivation_source: Phase 2 domain concern #[N]
  (one entry per derived expert)

coverage_gaps: |
  {Phase 2 concerns not addressed by any derived expert; or "none detected."
  A genuine diagnostic answer — not a stub.}

inertia_surface: |
  {Phase 1 status-quo claim verbatim — exact sentence from INERTIA-SURFACE.
  Do not paraphrase. This is the design tension this registry was built to hold.}

Generated by: /org-roles {topic} — {date}
```

FAILURE MODE — HEADING STUB: writing "## Registry Summary" with no fields populated
is not an answer to the diagnostic question. The answer requires all fields to have
substantive content.

GATE — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.craft/roles/{area}/REGISTRY.md`
2. `total_roles` equals the count of `.md` files written in Phase 5 (enumerated from
   Phase 5 output, not derived from prior-phase plans)
3. `domain_experts` lists each derived expert with `name` and `derivation_source`
4. `inertia_surface` contains the Phase 1 status-quo claim verbatim
5. No heading stubs — every field has substantive content

---

## V-05 — Combined: All Four Axes

**axis:** role sequence + output format + lifecycle emphasis + phrasing register + inertia framing
**hypothesis:** R4's highest-scoring variate (V-01 at 98.82 retroactive) failed C-23 (no Phase 0
commitment block) and C-24 (gate did not quote field identifiers). The five new R5 criteria
form a dependency chain: C-23 requires Phase 0 → C-20 (extension named before role writing)
is satisfied → C-22 requires Phase 6 PREPARE → count integrity is structural → C-24 requires
Phase 5 PREPARE or FIELD CONTRACT → field identifiers are verified pre-write → C-21 requires
the template's verify_questions annotation → uniqueness is construction-time, not evaluator-time
→ C-25 requires Phase 1 gate to enumerate per-expert attributes → completeness is
per-entry, not aggregate. This variate integrates all four axes to satisfy the chain by
construction at every step: Phase 0 commits the extension with formal provenance (C-23, V-02),
Phase 1 runs inertia-first to ground the challenge before domain experts (V-01), Phase 5 uses
PREPARE/WRITE/GATE with the FIELD CONTRACT identifiers as required inputs (V-03), diagnostic
framing at each phase forces answers before outputs (V-04). The inertia-advocate is the
structural counterweight that connects Phase 0 to Phase 6: the commitment made in Phase 0
is validated at Phase 6 by requiring the status-quo claim verbatim.
Falsifiable: if V-05 scores lower than V-03 on aspirational criteria, lifecycle-only
structure is more reliable than multi-axis integration, and the axes are not mutually
reinforcing for these specific criteria.

---

You are running `/org-roles {topic}`.

---

PHASE 0 — REGISTRY DESIGN DECLARATION

**Diagnostic question:** What design-level tension will this role registry hold — what
assumption is currently unchallenged in this domain that this registry must expose?

Answer by writing a FIELD CONTRACT and EXTENSION COMMITMENT before reading any context.

**PART A — EXTENSION COMMITMENT**

```
EXTENSION-COMMITMENT:
  field_name: inertia_surface
  population_source: Phase 1, INERTIA-SURFACE block, status-quo claim field
  purpose: [answer to the diagnostic question — the domain-specific assumption this
    registry exists to stress-test; one sentence naming the unchallenged assumption]
```

**PART B — FIELD CONTRACT**

All role files must conform to this contract. Field identifiers are binding.

```
FIELD-CONTRACT for /org-roles {topic}:

  [FC-1]  name
          type: string — domain-vocabulary slug; not "domain-expert", "expert-1"

  [FC-2]  orientation.frame
          type: string — epistemic viewpoint ("sees X through the lens of Y")
          BAD:  task list / job description
          GOOD: "Sees every [artifact] through the lens of [concern] — looking for [gap]"

  [FC-3]  orientation.serves
          type: string — beneficiary statement; NOT a restatement of frame
          BAD:  restates frame in different words
          GOOD: names a beneficiary and what signal they receive from this role

  [FC-4]  lens.verify_questions
          EXACT IDENTIFIER: verify_questions
          VIOLATIONS: verify | questions | checks | verify_list — all break downstream
          type: list; minimum two items; at least one question uniquely attributable to
            this role's frame — no other role in this registry would prioritize that
            question first; confirm uniqueness before writing each question
          BAD:  "Is the design correct?" (unmeasurable; non-unique)
          GOOD: "Does [specific artifact] satisfy [specific measurable constraint] as
                 verifiable in [specific test or inspection]?"

  [FC-5]  lens.simplify_rules
          EXACT IDENTIFIER: simplify_rules
          VIOLATIONS: simplify | rules | constraints | guidelines — all break downstream
          type: list; minimum one item; opinionated exclusion, not a scope description
          BAD:  "Focus on [concern area]" (describes priority, excludes nothing)
          GOOD: "Skip [X] unless [condition]; flag only [Y]"

  [FC-6]  expertise.depth   — enum: expert | practitioner | senior | principal

  [FC-7]  expertise.relevance — domain-specific justification; not a role-name restatement

  [FC-8]  scope.primary     — main concern this role surfaces; one sentence

  [FC-9]  scope.boundary    — what this role does NOT own; explicit exclusion

  [FC-10] collaborates_with
          type: list — registry members only
          CONTRACT VIOLATION (type 1) — PHANTOM: name absent from registry output
          CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT has all three elements: `field_name` = `inertia_surface`;
   `population_source` names Phase 1 and the INERTIA-SURFACE artifact; `purpose`
   answers the diagnostic question with a domain-specific tension statement
2. FIELD-CONTRACT is written with all ten items [FC-1] through [FC-10]
3. Items [FC-4] and [FC-5] display exact identifier strings `verify_questions` and
   `simplify_rules` under their EXACT IDENTIFIER labels — both strings appear verbatim

---

PHASE 1 — INERTIA SPECIFICATION (first-pass context read; domain experts not yet named)

**Diagnostic question:** What does the existing approach already solve, and why would
a rational stakeholder argue this feature is premature or unnecessary?

Read `{topic}` context for existing system capabilities. Do not derive domain experts.
Answer the diagnostic question by writing an INERTIA-SURFACE block:

```
INERTIA-SURFACE for {topic}:

  Status-quo claim: [your answer — one sentence in `{topic}` domain vocabulary;
    the strongest reasonable argument against building the feature; names the specific
    existing capability that makes the feature redundant]

  Challenge questions (at minimum three; each challenges the feature's necessity):
    1. What specific failure does the status quo produce that this feature resolves?
       (Name the failure; if you cannot name it, flag as gap — the status quo may be right.)
    2. [domain-specific challenge: what does the existing mechanism already do that
       addresses the most important proposed use case?]
    3. [domain-specific challenge: what is the minimum viable status-quo fix, and
       why is it insufficient?]
```

The status-quo claim will be copied verbatim to `inertia_surface` in Phase 6.
Do not name domain experts in Phase 1. Domain experts are derived in Phase 2
in explicit response to this challenge surface.

**GATE** — Phase 1 complete when ALL of the following are TRUE:
1. INERTIA-SURFACE block is written
2. Status-quo claim is a complete sentence using `{topic}` domain vocabulary
3. At least three challenge questions are present, each naming a specific capability
   or argument (not a generic "is this needed?")
4. No domain expert names appear in this block

---

PHASE 2 — CONTEXT ANALYSIS (domain experts; derived to challenge the Phase 1 surface)

**Diagnostic question:** What concerns in this domain does the Phase 1 status-quo claim
fail to acknowledge — and who holds each unacknowledged concern?

Read full `{topic}` context. Each domain expert is your answer to this question for one
specific concern that the status-quo claim misses.

```
DOMAIN-ANALYSIS for {topic}:

  Domain concerns (at minimum three; each a failure the Phase 1 status-quo claim omits):
    1. [concern: what the status quo claim overlooks about this domain]
    2. [concern]
    3. [concern]

  Domain experts derived from concerns:
    - Expert name: [slug per FIELD-CONTRACT [FC-1] — domain vocabulary, not generic]
      Concern link: [which concern above, by number]
      Domain-vocabulary frame: [per [FC-2] — epistemic viewpoint using concern vocabulary]
      Verify focus: [what artifact or behavior this expert checks first to surface concern]
    (repeat for each derived expert — at minimum one)
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 2.

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. DOMAIN-ANALYSIS block is written with a populated Domain concerns list
2. At least three domain concerns are listed using vocabulary specific to `{topic}`
3. Each derived expert entry lists all four attributes checked per expert individually:
   name, concern link, domain-vocabulary frame, verify focus — checked per expert,
   not as a total count; a single missing attribute in any entry fails this item
4. Each derived expert's concern link names a concern the Phase 1 status-quo claim omits
5. No stock role names (pm, architect, strategy, inertia-advocate) appear in this block

---

PHASE 3 — STOCK ROLES

**Diagnostic question:** Which standing perspectives ensure the registry covers value,
structure, strategy, and design tension regardless of domain?

```
STOCK-ROLES:
  - pm              (product value and user outcome lens)
  - architect       (technical structure and system boundary lens)
  - strategy        (business model and competitive position lens)
  - inertia-advocate (status-quo challenge lens — orientation.frame anchored to Phase 1
                      status-quo claim; verify_questions sourced from Phase 1
                      INERTIA-SURFACE challenge questions)
```

**GATE** — Phase 3 complete when ALL of the following are TRUE:
1. STOCK-ROLES lists all four names with lens descriptors
2. inertia-advocate identifies Phase 1 as source for orientation and verify_questions
3. Phase 1 INERTIA-SURFACE confirmed available

---

PHASE 4 — OUTPUT AREA

**Diagnostic question:** What area slug identifies this domain unambiguously to downstream
skills?

```
OUTPUT-AREA: .craft/roles/{area}/
```

**GATE** — Phase 4 complete when ALL of the following are TRUE:
1. OUTPUT-AREA is written
2. Area slug uses domain vocabulary (not `default`, `generic`, `roles`)
3. Path is exactly `.craft/roles/{area}/`

---

PHASE 5 — WRITE ROLE FILES

**PREPARE:** Confirm the following inputs are available before writing any file:
- Phase 0 FIELD-CONTRACT items [FC-4] and [FC-5]: exact identifiers `verify_questions`
  and `simplify_rules` (retrieve and confirm spelling from Phase 0 before proceeding)
- Phase 1 INERTIA-SURFACE: status-quo claim, challenge questions (for inertia-advocate)
- Phase 2 DOMAIN-ANALYSIS: expert names, frames, verify focuses
- Phase 3 STOCK-ROLES: four names confirmed
- Phase 4 OUTPUT-AREA path confirmed

PREPARE complete when all five inputs are confirmed available. Do not begin WRITE until confirmed.

**Diagnostic question (per role):** What does this role see, serve, verify, and simplify
— and which of its verify questions is so specific to its frame that no other role would
ask it first?

**WRITE:** One `.md` file per role to `.craft/roles/{area}/`. Domain experts first, stock
roles second. For each file, answer the diagnostic question using the FIELD CONTRACT:

```yaml
---
name: {per [FC-1]: domain-vocabulary slug}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Per [FC-2]: epistemic viewpoint.
    Domain experts: Phase 2 domain-vocabulary frame as anchor.
    Inertia-advocate: Phase 1 status-quo claim as epistemic stance.

    FAILURE MODE: task-list frame.
    WORKED EXAMPLE (bad):  "Responsible for reviewing artifacts and ensuring
      requirements are captured before handoff."
    WORKED EXAMPLE (good): "Sees every proposal through the lens of whether the
      claimed benefit justifies the cost of the change — looking for cases where
      the status quo handles the use case adequately without new infrastructure."}

  serves: |
    {Per [FC-3]: beneficiary statement — not a restatement of frame.

    FAILURE MODE: frame restatement.
    WORKED EXAMPLE (bad):  "Ensures proposals are evaluated for cost-benefit
      ratio." (same information as frame, different words)
    WORKED EXAMPLE (good): "Engineering leads deciding whether to staff the
      feature — they get a cost-benefit verdict before roadmap commitment."}

lens:
  verify_questions:
    - "{Per [FC-4]: actionable; answerable by artifact-read, code-run, or
       measurable outcome}"
    - "{Per [FC-4] uniqueness requirement: before writing, confirm — no other
       role in this registry would prioritize this question first; if any would,
       revise until this question is uniquely attributable to this role's frame.
       The question must be answerable from an artifact, not from an interview.}"

  simplify_rules:
    - "{Per [FC-5]: opinionated exclusion — 'Skip X unless Y.'

       FAILURE MODE: scope description.
       WORKED EXAMPLE (bad):  'Focus on cost-benefit and change-risk concerns.'
       WORKED EXAMPLE (good): 'Skip analysis of features scoped to internal teams;
         flag only changes that reach external integrators or end users.'}"

expertise:
  depth: {per [FC-6]: expert | practitioner | senior | principal}
  relevance: |
    {Per [FC-7]: domain-specific justification — not a restatement of role name.}

scope:
  primary: |
    {Per [FC-8]: main concern. One sentence.}
  boundary: |
    {Per [FC-9]: explicit exclusion. One sentence.}

collaborates_with:
  - {per [FC-10]: role-name — registry members only}
  # CONTRACT VIOLATION (type 1): PHANTOM — name absent from this registry.
  # CONTRACT VIOLATION (type 2): UNIVERSALIST — "all roles" or equivalent.
```

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. One `.md` file exists per role in `.craft/roles/{area}/`
2. Every file uses exact field identifiers `verify_questions` and `simplify_rules`
   per FIELD-CONTRACT [FC-4] and [FC-5] — the identifier strings appear verbatim
   as YAML keys; not `verify`, `simplify`, or any contracted form
3. Inertia-advocate: `orientation.frame` anchors to Phase 1 status-quo claim;
   `verify_questions` from Phase 1 challenge questions
4. Each role has at least one `verify_questions` entry uniquely attributable to that
   role's frame (per the PREPARE diagnostic question and template instruction)
5. No `collaborates_with` entries contain type-1 phantom or type-2 universalist
   violations per FIELD-CONTRACT [FC-10]

---

PHASE 6 — REGISTRY SUMMARY

**PREPARE:** Before writing `REGISTRY.md`, enumerate the `.md` files written in Phase 5.
Record this as `PHASE5_COUNT`. This count must come from Phase 5 file enumeration —
not from adding Phase 3 STOCK-ROLES count to Phase 2 expert count. Derivation from
prior-phase plans without verification is a C-22 failure.

PREPARE complete when `PHASE5_COUNT` is recorded.

**Diagnostic question:** What does this registry as a whole commit to — what design
tension does it hold, what coverage does it provide, and what does it explicitly not claim?

Answer by writing `.craft/roles/{area}/REGISTRY.md`:

```
---
area: {area}
generated: {date}
---

## Registry Summary

total_roles: {PHASE5_COUNT — from the PREPARE enumeration above; not a planned count}

stock_roles:
  - pm
  - architect
  - strategy
  - inertia-advocate

domain_experts:
  - name: {expert-name}
    derivation_source: Phase 2 domain concern #[N]
  (one entry per derived expert)

coverage_gaps: |
  {Phase 2 concerns not addressed by any derived expert; or "none detected."
  A genuine diagnostic answer — not a heading stub.}

inertia_surface: |
  {Phase 1 status-quo claim verbatim — exact sentence from INERTIA-SURFACE block.
  Do not paraphrase. This fulfills the EXTENSION-COMMITMENT made in Phase 0.}

Generated by: /org-roles {topic} — {date}
```

FAILURE MODE — HEADING STUB: "## Registry Summary" with no fields populated is not an
answer to the diagnostic question. Every field above must contain substantive content
that could not have been written without running all prior phases.

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.craft/roles/{area}/REGISTRY.md`
2. `total_roles` equals `PHASE5_COUNT` from the PREPARE enumeration (not a planned count)
3. `domain_experts` lists each derived expert with both `name` and `derivation_source`
4. `inertia_surface` contains the Phase 1 status-quo claim verbatim — not paraphrased;
   this validates the EXTENSION-COMMITMENT made in Phase 0
5. No heading stubs — every field has substantive content below its header

---

## Round 5 Criterion Coverage Map

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-23** Phase 0 commitment block (3 elements) | Phase 0 structural commitment before Phase 1 | Phase 0 PART A, named before FIELD CONTRACT | Phase 0 WRITE sub-step, 3-element gate | Phase 0 diagnostic answer forms commitment | Phase 0 PART A + diagnostic question |
| **C-21** Uniqueness mandate by construction | Template: "no other role would prioritize first" | FIELD CONTRACT [FC-4] uniqueness requirement | Template: "confirm uniqueness before writing" | Template: "no other role would ask it first" | [FC-4] + template diagnostic instruction |
| **C-22** Cross-step count integrity | Phase 6 gate: "count Phase 5 before writing" | Phase 6 gate: "enumerate Phase 5 output" | Phase 6 PREPARE names count as required input | Phase 6: "enumerate Phase 5 output files" | Phase 6 PREPARE + gate both require enumeration |
| **C-24** Field identifier precision gate | Gate item 2 quotes `verify_questions`, `simplify_rules` | Gate references [FC-4] and [FC-5] with exact identifiers in contract | Phase 5 PREPARE names identifiers from Phase 0 | Gate item 2 quotes exact identifier strings | Phase 5 PREPARE + gate + contract all quote identifiers |
| **C-25** Per-expert attribute gate | Gate item 3: four attributes per expert individually | Gate item 3: four attributes per expert individually | Gate item 3: four attributes per expert individually | Gate item 3: four attributes per expert individually | Gate item 3: four attributes per expert individually |
| **C-02** Devil-advocate role | Phase 3 sourced from Phase 1 inertia spec | Phase 2 challenge questions as verify_questions | Phase 2 challenge questions as verify_questions | Phase 1 shapes inertia-advocate orientation | Phase 1 shapes orientation + Phase 0 grounds design tension |
| **C-08/C-14** Collaborates_with dual prohibition | Type 1 + Type 2 labeled in template | Type 1 + Type 2 labeled in [FC-10] | Type 1 + Type 2 labeled in template | Type 1 + Type 2 labeled in template | Type 1 + Type 2 labeled in [FC-10] + template |
| **C-11** Context-first ordering | Phase 1 inertia → Phase 2 domain experts → Phase 3 stock | Phase 1 domain experts → Phase 2 inertia → Phase 3 stock | Phase 1 domain experts → Phase 2 inertia → Phase 3 stock | Phase 1 inertia → Phase 2 domain experts → Phase 3 stock | Phase 1 inertia → Phase 2 domain experts → Phase 3 stock |
| **C-18** Contrastive worked example pairs | frame, serves, simplify_rules (3 pairs) | frame, serves, verify_questions, simplify_rules in FIELD CONTRACT | frame, serves, simplify_rules (3 pairs) | frame, serves, verify_questions, simplify_rules (4 pairs) | frame, serves, simplify_rules + FC-2, FC-3, FC-4, FC-5 |
| **C-19** Multi-item completion gate | All phases: 3–5 items per gate | All phases: 3–5 items per gate | All phases: 3–5 items per PREPARE/WRITE/GATE | All phases: 3–5 items per gate | All phases: 3–5 items per PREPARE/WRITE/GATE |
| **C-20** Domain-specific registry extension | inertia_surface grounded in Phase 1 | inertia_surface grounded in Phase 2 | inertia_surface grounded in Phase 2 | inertia_surface grounded in Phase 1 | inertia_surface grounded in Phase 1, committed Phase 0 |

**Predicted scores against v5 rubric:**

```
V-01: (5/5)*60 + (3/3)*30 + (17/17)*10  =  60 + 30 + 10  =  100.0  (if all aspirational pass)
      Key risks: C-20 requires extension named before role writing — Phase 1 INERTIA-SURFACE
      appears before Phase 5 role writing, but Phase 0 commitment names Phase 1 as source:
      C-20 requires "named in step output spec before role writing begins" — Phase 0 names
      it before Phase 1 runs. C-20 PASS predicted.

V-02: same structure; C-11 at risk — Phase 1 derives domain experts, Phase 2 is inertia spec;
      stock roles in Phase 3; this satisfies C-11 (context-first) because domain experts
      precede stock roles. C-11 PASS predicted.

V-03: PREPARE/WRITE/GATE triad makes C-16, C-19 structurally guaranteed. C-23 PASS via Phase 0.
      C-24 PASS via Phase 5 PREPARE. C-22 PASS via Phase 6 PREPARE.

V-04: Diagnostic framing does not weaken any criterion — all gates are equivalent to V-01/V-02.
      C-11 at risk for same inertia-first reason as V-01. PASS predicted.

V-05: Maximum integration; all five new criteria satisfied by two mechanisms each (structural
      + gate). Highest ceiling — ceiling risk is execution depth on C-17/C-18 worked examples.
```
