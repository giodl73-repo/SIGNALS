---
skill: quest-variate
skill_target: org-roles
date: 2026-03-16
round: R6
rubric_version: v6
status: variate
---

# org-roles Variate — Round 6

**Date:** 2026-03-16
**Skill:** org-roles
**Rubric:** v6 (C-01 through C-30; new in v6: C-26 named FC-N contract block, C-27 PREPARE sub-step
with named count variable, C-28 explicit placeholder name prohibition, C-29 CONTRACT VIOLATION
framing, C-30 extension purpose tied to Phase 0 diagnostic question)
**Round:** R6 — single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

---

## Round 6 Variation Map

| V | Axis | Primary C targets | Hypothesis |
|---|------|------------------|------------|
| V-01 | inertia framing | C-28 PASS (contract + gate), C-30 natural anchor | Status-quo hypothesis written cold in Phase 0 before any context is read; EXTENSION-COMMITMENT answers the Phase 0 diagnostic by construction; domain experts are derived in Phase 2 specifically to challenge the cold hypothesis, making inertia the design lens rather than a final add-on role |
| V-02 | output format | C-28 PASS (contract + derivation gate), C-09 improvement | Role matrix table inserted between derivation and file writing forces the model to see all roles' frames and verify questions simultaneously — uniqueness violations become visible at the matrix stage rather than per-file; C-28 is prohibitied at two points: [FC-1] and derivation gate |
| V-03 | phrasing register | C-28 PASS — surgical addition to R5 V-05 structure | R5 V-05 scores 99.55/100, failing only C-28; [FC-1] in R5 V-05 states `not "domain-expert", "expert-1"` as a type constraint but without an explicit PROHIBITED class label; R6 V-03 adds a standalone PROHIBITED NAMES block in [FC-1], a DO NOT prohibition in Phase 2, and a gate item — three reinforcing points — and changes nothing else |
| V-04 | inertia framing + output format | C-28 PASS, C-09 + C-30 both improved | Combines V-01 (cold inertia hypothesis as Phase 0 diagnostic) and V-02 (matrix table before file writing); status-quo claim is hardened by context in Phase 1, then domain experts challenge it in Phase 2, then all roles are reviewed in the matrix before files are written |
| V-05 | all axes | C-28 PASS, 100.00 target | Full synthesis: cold inertia hypothesis (Phase 0 diagnostic), FC-N contract with standalone PROHIBITED NAMES clause, role matrix table, DO/DO NOT phrasing throughout, PREPARE/WRITE/GATE lifecycle at every phase, and all R5 V-05 mechanisms preserved — targets first 100.00 under the v6 rubric |

---

## V-01 — Inertia Framing: Status-Quo Hypothesis as Phase 0 Diagnostic

**axis:** inertia-framing
**hypothesis:** In R5 V-05, the inertia-advocate's status-quo claim is derived in Phase 1
after a context read. This variate makes the status-quo claim the opening act: Phase 0 asks
the model to write a COLD HYPOTHESIS of the strongest argument against building `{topic}` —
before any context is loaded. The cold hypothesis becomes the Phase 0 diagnostic answer that
the EXTENSION-COMMITMENT captures, satisfying C-30 by construction (the purpose IS the
answer to the Phase 0 question). Context is then read in Phase 1 to either confirm or revise
the cold hypothesis; domain experts are derived in Phase 2 specifically to challenge whichever
form the hypothesis took. The inertia-advocate's frame is anchored to the Phase 0/1 hybrid
rather than a post-hoc characterization. The FIELD CONTRACT in Phase 0 contains a standalone
PROHIBITED NAMES clause in [FC-1], not a type constraint inline, making C-28 a named
anti-pattern prohibition rather than a positive-only naming requirement.
Falsifiable: if domain experts derived to challenge a cold hypothesis are less
domain-specific than those derived from context, cold-first ordering reduces expert quality
despite improving structural compliance.

---

You are running `/org-roles {topic}`.

---

PHASE 0 — DIAGNOSTIC DECLARATION

**Opening diagnostic:** What is the strongest argument that the status quo is sufficient —
that `{topic}` is not worth building?

Answer this question COLD — before reading any context. Write a one-sentence COLD HYPOTHESIS:

```
COLD-HYPOTHESIS: [The existing approach already ___; therefore `{topic}` is premature / redundant
/ unnecessary — stated as the most reasonable opposing argument you can construct without
reading the spec.]
```

This is not a final verdict. It is the design tension this registry will stress-test.

After writing COLD-HYPOTHESIS, write the FIELD CONTRACT and EXTENSION COMMITMENT:

**EXTENSION-COMMITMENT:**

```
EXTENSION-COMMITMENT:
  field_name: inertia_surface
  population_source: Phase 1, INERTIA-SURFACE block, status-quo claim field
  purpose: answers the Phase 0 diagnostic question — "what is the strongest argument
    that the status quo is sufficient for {topic}?" — giving downstream consumers
    the exact design tension this registry was composed to hold
```

**FIELD CONTRACT:**

All role files must conform to this contract. Field identifiers are binding.

```
FIELD-CONTRACT for /org-roles {topic}:

  [FC-1]  name
          type: string — domain-vocabulary slug derived from context
          PROHIBITED NAMES: "domain-expert", "expert-1", "generic-expert", "role-1"
          These placeholder names pass superficial review but carry no domain signal.
          A name that could apply to any product is prohibited.
          BAD:  "domain-expert" (could be used in any registry)
          GOOD: "event-schema-fidelity-analyst" (specific to this domain's concern)

  [FC-2]  orientation.frame
          type: string — epistemic viewpoint ("sees X through the lens of Y")
          FAILURE MODE: task list / job description ("responsible for reviewing artifacts")
          BAD:  "Responsible for reviewing spec and ensuring requirements are captured"
          GOOD: "Sees every proposal through the lens of whether the status-quo capability
                 named in Phase 1 actually fails — looking for the specific gap the
                 feature is meant to close"

  [FC-3]  orientation.serves
          type: string — beneficiary statement; NOT a restatement of frame
          FAILURE MODE: frame restatement (serves carries the same information as frame)
          BAD:  "Ensures proposals are challenged against the status quo"
          GOOD: "Engineering leads deciding whether to staff the feature — they receive
                 a verdict on whether the status quo is genuinely insufficient"

  [FC-4]  lens.verify_questions
          EXACT IDENTIFIER: verify_questions
          PROHIBITED IDENTIFIERS: verify | questions | checks | verify_list
          All prohibited identifiers break downstream consumers that read by exact key
          type: list; minimum two items; at least one question uniquely attributable to
            this role's frame — no other role in this registry would prioritize that
            question first; confirm uniqueness before writing each question
          BAD:  "Is the design correct?" (unmeasurable; any role could ask this)
          GOOD: "Does the spec name a specific failure the status quo produces that
                 existing error handling cannot prevent — verifiable in the acceptance
                 criteria section?"

  [FC-5]  lens.simplify_rules
          EXACT IDENTIFIER: simplify_rules
          PROHIBITED IDENTIFIERS: simplify | rules | constraints | guidelines
          All prohibited identifiers break downstream consumers that read by exact key
          type: list; minimum one item; opinionated exclusion — NOT a scope description
          BAD:  "Focus on status-quo challenge concerns" (describes, does not exclude)
          GOOD: "Skip analysis of changes that do not alter any existing user-facing
                 behavior; flag only changes that invalidate a current capability claim"

  [FC-6]  expertise.depth   — enum: expert | practitioner | senior | principal

  [FC-7]  expertise.relevance — domain-specific justification; not a role-name restatement

  [FC-8]  scope.primary     — main concern this role surfaces; one sentence

  [FC-9]  scope.boundary    — what this role does NOT own; explicit exclusion; one sentence

  [FC-10] collaborates_with
          type: list — registry members only
          CONTRACT VIOLATION (type 1) — PHANTOM: a role name absent from this registry's
            output; phantom names silently break all downstream skills that resolve
            collaboration links by exact name
          CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent;
            universalist listing carries no structural information and prevents directed
            graph reasoning over collaborations
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. COLD-HYPOTHESIS is written as a complete sentence with the status-quo claim
2. EXTENSION-COMMITMENT has all three elements: `field_name` = `inertia_surface`;
   `population_source` names Phase 1 and the INERTIA-SURFACE artifact; `purpose`
   explicitly names the Phase 0 diagnostic question it answers
3. FIELD-CONTRACT is written with all ten items [FC-1] through [FC-10]
4. [FC-1] contains the PROHIBITED NAMES clause naming at least "domain-expert" and
   "expert-1" explicitly as anti-patterns
5. [FC-4] and [FC-5] display exact identifier strings `verify_questions` and
   `simplify_rules` under EXACT IDENTIFIER labels — both strings appear verbatim

---

PHASE 1 — INERTIA REFINEMENT (context read; cold hypothesis confirmed or revised)

Read `{topic}` context. Your goal is to find whether the existing system actually has the
capability claimed in the COLD-HYPOTHESIS. Write an INERTIA-SURFACE block:

```
INERTIA-SURFACE for {topic}:

  Status-quo claim: [refined version of Phase 0 COLD-HYPOTHESIS, now grounded in actual
    context — either confirmed ("the spec confirms the existing system already handles X,
    making the proposed feature redundant unless Y is demonstrated") or revised ("the
    cold hypothesis was incorrect; the actual status-quo argument is ___")]

  Challenge questions (at minimum three; specific to `{topic}` context):
    1. What specific failure does the status quo produce that this feature resolves?
       (Name the failure as found in context; if unspecified, flag as a spec gap.)
    2. [domain-specific challenge: what does the existing mechanism already handle?]
    3. [domain-specific challenge: what is the minimum status-quo fix, and why
       is it insufficient according to the context?]
```

Do not name domain experts in Phase 1. Domain experts are derived in Phase 2
specifically to challenge the status-quo claim above.

The status-quo claim will be copied verbatim to `inertia_surface` in Phase 6.

**GATE** — Phase 1 complete when ALL of the following are TRUE:
1. INERTIA-SURFACE block is written
2. Status-quo claim explicitly names a specific existing capability (not generic)
3. Status-quo claim references Phase 0 COLD-HYPOTHESIS (confirmed or revised)
4. At least three challenge questions use vocabulary from the `{topic}` context
5. No domain expert names appear in this block

---

PHASE 2 — CONTEXT ANALYSIS (domain experts derived to challenge the Phase 1 surface)

Read `{topic}` context for concerns the Phase 1 status-quo claim does not address.
Each domain expert you derive is your answer to: "who holds a concern this status-quo
argument overlooks?"

DO NOT name derived experts with placeholder labels. The following names are
PROHIBITED by [FC-1]: "domain-expert", "expert-1", "generic-expert", "role-1".
The name must come from the domain vocabulary in the concerns list below.
A name that would apply to any product violates [FC-1].

```
DOMAIN-ANALYSIS for {topic}:

  Domain concerns (at minimum three; each names a gap the Phase 1 status-quo claim misses):
    1. [concern: specific failure mode or blind spot in this domain not covered by the
       status-quo claim — use {topic} vocabulary]
    2. [concern]
    3. [concern]

  Domain experts derived from concerns:
    - Expert name: [slug per [FC-1] — domain vocabulary; PROHIBITED: "domain-expert",
        "expert-1" — see Phase 0 [FC-1] PROHIBITED NAMES clause]
      Concern link: [which concern above, by number]
      Domain-vocabulary frame: [per [FC-2] — epistemic viewpoint using concern vocabulary;
        not a task description]
      Verify focus: [what artifact or behavior this expert checks first to surface concern]
    (repeat for each derived expert — at minimum one)
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 2.

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. DOMAIN-ANALYSIS block is written with a populated Domain concerns list
2. At least three domain concerns use vocabulary specific to `{topic}`
3. Each derived expert entry lists all four attributes individually:
   name, concern link, domain-vocabulary frame, verify focus —
   checked per expert, not as a total count; a single missing attribute in any
   entry fails this item
4. No derived expert name is a placeholder per [FC-1] PROHIBITED NAMES clause —
   "domain-expert", "expert-1", "generic-expert" fail this gate item
5. No stock role names (pm, architect, strategy, inertia-advocate) appear in this block

---

PHASE 3 — STOCK ROLES

```
STOCK-ROLES:
  - pm               (product value and user outcome lens)
  - architect        (technical structure and system boundary lens)
  - strategy         (business model and competitive position lens)
  - inertia-advocate (status-quo challenge lens — orientation.frame anchored to Phase 1
                      status-quo claim; verify_questions sourced from Phase 1
                      INERTIA-SURFACE challenge questions)
```

**GATE** — Phase 3 complete when ALL of the following are TRUE:
1. STOCK-ROLES lists all four names with lens descriptors
2. inertia-advocate identifies Phase 1 as source for `orientation.frame` and
   `verify_questions`
3. Phase 1 INERTIA-SURFACE confirmed available as source

---

PHASE 4 — OUTPUT AREA

```
OUTPUT-AREA: .craft/roles/{area}/
```

Area slug must use domain vocabulary from Phase 2. NOT: `default`, `generic`, `roles`.

**GATE** — Phase 4 complete when ALL of the following are TRUE:
1. OUTPUT-AREA is written
2. Area slug uses Phase 2 domain vocabulary
3. Path format is exactly `.craft/roles/{area}/`

---

PHASE 5 — WRITE ROLE FILES

**PREPARE:** Confirm the following inputs before writing any file:
- Phase 0 [FC-4] exact identifier: `verify_questions` (retrieve verbatim from [FC-4])
- Phase 0 [FC-5] exact identifier: `simplify_rules` (retrieve verbatim from [FC-5])
- Phase 1 INERTIA-SURFACE: status-quo claim and challenge questions
- Phase 2 DOMAIN-ANALYSIS: expert names, concern links, frames, verify focuses
- Phase 3 STOCK-ROLES: all four names confirmed
- Phase 4 OUTPUT-AREA path confirmed

PREPARE complete when all six inputs are confirmed available. Do not begin WRITE until confirmed.

**WRITE:** One `.md` file per role to `.craft/roles/{area}/`. Domain experts first (Phase 2),
stock roles second (Phase 3). For each file, apply the FIELD CONTRACT:

```yaml
---
name: {per [FC-1]: domain-vocabulary slug; PROHIBITED: "domain-expert", "expert-1"}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Per [FC-2]: epistemic viewpoint.
    Domain experts: Phase 2 domain-vocabulary frame as anchor.
    Inertia-advocate: Phase 1 status-quo claim as epistemic stance.

    FAILURE MODE: task-list frame.
    WORKED EXAMPLE (bad):  "Responsible for reviewing proposals and surfacing gaps."
    WORKED EXAMPLE (good): "Sees every spec change through the lens of whether
      the existing system already handles the proposed scenario — looking for
      cases where a simpler status-quo fix would avoid the new complexity."}

  serves: |
    {Per [FC-3]: beneficiary statement — not a restatement of frame.

    FAILURE MODE: frame restatement.
    WORKED EXAMPLE (bad):  "Ensures proposals are challenged against the status quo."
    WORKED EXAMPLE (good): "Feature teams deciding whether to proceed — they receive
      a verdict on which existing capabilities are genuinely insufficient."}

lens:
  verify_questions:
    - "{Per [FC-4]: actionable; answerable by artifact-read, code-run, or
       measurable outcome; uses {topic} domain vocabulary}"
    - "{Per [FC-4] uniqueness requirement: before writing, confirm — no other role
       in this registry would prioritize this question first; if any would, revise
       until the question is uniquely attributable to this role's frame}"

  simplify_rules:
    - "{Per [FC-5]: opinionated exclusion — 'Skip X unless Y.'

       FAILURE MODE: scope description.
       WORKED EXAMPLE (bad):  'Focus on status-quo challenge concerns.'
       WORKED EXAMPLE (good): 'Skip changes that preserve all existing API contracts;
         flag only changes that invalidate or extend an existing contract.'}"

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
  # CONTRACT VIOLATION (type 1) — PHANTOM: name absent from this registry.
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent.
```

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. One `.md` file exists per role in `.craft/roles/{area}/`
2. Every file uses exact identifiers `verify_questions` and `simplify_rules` per
   [FC-4] and [FC-5] — both strings appear verbatim as YAML keys; `verify`, `simplify`,
   or any contracted form fails this gate item
3. No role file uses a prohibited name per [FC-1]: "domain-expert", "expert-1",
   "generic-expert" fail this gate item
4. Inertia-advocate: `orientation.frame` anchors to Phase 1 status-quo claim;
   `verify_questions` sourced from Phase 1 challenge questions
5. Each role has at least one `verify_questions` entry uniquely attributable to that
   role's frame (confirmed per PREPARE diagnostic and template instruction)
6. No `collaborates_with` entries contain CONTRACT VIOLATION type-1 or type-2
   per [FC-10]

---

PHASE 6 — REGISTRY SUMMARY

**PREPARE:** Before writing `REGISTRY.md`, enumerate the `.md` files written in Phase 5.
Record this count as `PHASE5_COUNT`. This count must come from Phase 5 file enumeration —
NOT from adding Phase 3 STOCK-ROLES (4) to Phase 2 expert count.
Derivation from prior-phase plans without enumeration is a C-27 failure.

PREPARE complete when `PHASE5_COUNT` is recorded from Phase 5 enumeration.

**WRITE:** `.craft/roles/{area}/REGISTRY.md`:

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

FAILURE MODE — HEADING STUB: "## Registry Summary" with no fields populated is not a
registry. Every field above must have substantive content.

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.craft/roles/{area}/REGISTRY.md`
2. `total_roles` equals `PHASE5_COUNT` from the PREPARE enumeration
3. `domain_experts` lists each derived expert with both `name` and `derivation_source`
4. `inertia_surface` contains the Phase 1 status-quo claim verbatim — not paraphrased;
   this validates the EXTENSION-COMMITMENT made in Phase 0
5. No heading stubs — every field has substantive content below its header

---

## V-02 — Output Format: Role Matrix Table Before File Expansion

**axis:** output-format
**hypothesis:** Writing individual role files is a serial operation; the model commits to
each role's frame and verify questions without seeing how other roles' questions compare.
This variate adds a ROLE MATRIX TABLE step between domain derivation and file writing.
The matrix shows all roles in a single table — name, frame (one sentence), key verify
question, collaborates_with (two to four names) — and requires a uniqueness check
across all verify questions before any file is written. C-09 and C-21 become structural
outputs of the matrix step rather than post-hoc verification criteria. C-28 is addressed
at two reinforcing locations: [FC-1] PROHIBITED NAMES clause and a dedicated DO NOT
instruction in Phase 2. Matrix-first format also reduces type-1 phantom violations (C-08)
because collaboration names are visible across all roles simultaneously before any file
commits them.
Falsifiable: if the matrix step is treated as a heading-only stub and files are written
without calibrating against the matrix, output-format structure alone does not enforce
role differentiation at execution time.

---

You are running `/org-roles {topic}`.

---

PHASE 0 — FIELD CONTRACT AND EXTENSION COMMITMENT

Before reading any context, establish the binding field specifications and registry extension.

**EXTENSION-COMMITMENT:**

```
EXTENSION-COMMITMENT:
  field_name: inertia_surface
  population_source: Phase 1, INERTIA-SURFACE block, status-quo claim field
  purpose: answers the Phase 0 diagnostic question — "what is the strongest
    existing-system argument that makes {topic} premature?" — giving downstream
    consumers the design tension this role registry was built to hold
```

**FIELD CONTRACT:**

```
FIELD-CONTRACT for /org-roles {topic}:

  [FC-1]  name
          type: string — domain-vocabulary slug
          PROHIBITED NAMES: "domain-expert", "expert-1", "generic-expert", "role-1"
          These are placeholder anti-patterns: they pass visual review but carry no
          domain content and violate C-05 by construction. The name must derive
          from the domain vocabulary in the concern it addresses.
          BAD:  "domain-expert"  — applies to any product; no domain signal
          GOOD: "pipeline-fault-isolation-engineer" — derived from a specific concern

  [FC-2]  orientation.frame
          type: string — epistemic viewpoint ("sees X through the lens of Y")
          FAILURE MODE: task list / job description
          BAD:  "Responsible for reviewing artifacts and surfacing issues"
          GOOD: "Sees every schema change through the lens of whether the consumer
                 contract is invalidated — looking for version-mismatch gaps"

  [FC-3]  orientation.serves
          type: string — beneficiary statement; NOT a restatement of frame
          FAILURE MODE: frame restatement
          BAD:  "Ensures schema changes are reviewed for contract gaps"
          GOOD: "Integration teams receiving a schema update — they get a contract-
                 compatibility verdict before the change reaches their pipeline"

  [FC-4]  lens.verify_questions
          EXACT IDENTIFIER: verify_questions
          PROHIBITED IDENTIFIERS: verify | questions | checks | verify_list
          type: list; minimum two items; at least one question uniquely attributable
            to this role's frame — "a question no other role in this registry would
            prioritize first"; confirm uniqueness before writing each question
          BAD:  "Is the design consistent?" (generic; non-unique; unmeasurable)
          GOOD: "Does the published event schema match the consumer's declared version
                 constraint, as verifiable in the integration contract fixture?"

  [FC-5]  lens.simplify_rules
          EXACT IDENTIFIER: simplify_rules
          PROHIBITED IDENTIFIERS: simplify | rules | constraints | guidelines
          type: list; minimum one item; opinionated exclusion — NOT a scope description
          BAD:  "Focus on contract fidelity concerns" (describes priority, excludes nothing)
          GOOD: "Skip schema fields not referenced by any declared consumer; flag
                 only fields in active use that change type or drop a required key"

  [FC-6]  expertise.depth   — enum: expert | practitioner | senior | principal

  [FC-7]  expertise.relevance — domain-specific justification; not a role-name restatement

  [FC-8]  scope.primary     — main concern this role surfaces; one sentence

  [FC-9]  scope.boundary    — what this role does NOT own; explicit exclusion; one sentence

  [FC-10] collaborates_with
          type: list — registry members only
          CONTRACT VIOLATION (type 1) — PHANTOM: role name absent from this registry's
            output; phantom names silently break downstream skill resolution
          CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent;
            universalist listing conveys no structural dependency
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT has all three elements: `field_name` = `inertia_surface`;
   `population_source` names Phase 1 and the INERTIA-SURFACE artifact; `purpose`
   explicitly names the Phase 0 diagnostic question it answers
2. FIELD-CONTRACT has all ten items [FC-1] through [FC-10]
3. [FC-1] contains the PROHIBITED NAMES clause naming "domain-expert" and
   "expert-1" explicitly as prohibited anti-patterns
4. [FC-4] and [FC-5] display exact identifier strings `verify_questions` and
   `simplify_rules` under their EXACT IDENTIFIER labels

---

PHASE 1 — INERTIA SURFACE

Read `{topic}` context for existing system capabilities. Write an INERTIA-SURFACE block:

```
INERTIA-SURFACE for {topic}:

  Status-quo claim: [one sentence naming the existing capability that makes {topic}
    appear redundant — the strongest reasonable argument against building it]

  Challenge questions (at minimum three; domain-specific):
    1. What specific failure does the status quo produce that this feature resolves?
    2. [challenge derived from context: what does the existing mechanism handle?]
    3. [challenge derived from context: minimum viable status-quo fix, and why insufficient?]
```

**GATE** — Phase 1 complete when ALL of the following are TRUE:
1. INERTIA-SURFACE is written
2. Status-quo claim names a specific existing capability using `{topic}` vocabulary
3. At least three challenge questions name specific context-derived concerns
4. No domain expert names appear in this block

---

PHASE 2 — CONTEXT ANALYSIS (domain experts only)

Read full `{topic}` context. Derive domain experts from concerns the Phase 1 status-quo
claim fails to address.

DO NOT name derived experts with placeholder labels.
PROHIBITED by [FC-1]: "domain-expert", "expert-1", "generic-expert", "role-1"
A name that could apply to any product is a [FC-1] violation regardless of the
surrounding context — the name itself must carry domain signal.

```
DOMAIN-ANALYSIS for {topic}:

  Domain concerns (at minimum three; each a gap the Phase 1 status-quo claim misses):
    1. [concern specific to {topic} — use domain vocabulary]
    2. [concern]
    3. [concern]

  Domain experts derived from concerns:
    - Expert name: [per [FC-1] — domain slug; NOT "domain-expert" or "expert-1"]
      Concern link: [which concern above, by number]
      Domain-vocabulary frame: [per [FC-2] — epistemic viewpoint, not a task description]
      Verify focus: [what artifact or behavior this expert checks first]
    (repeat for each derived expert — at minimum one)
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 2.

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. DOMAIN-ANALYSIS block is written with a populated concerns list
2. At least three concerns use vocabulary specific to `{topic}`
3. Each derived expert lists all four attributes individually:
   name, concern link, domain-vocabulary frame, verify focus —
   checked per expert; a missing attribute in any single entry fails this item
4. No derived expert name is a [FC-1] placeholder — "domain-expert", "expert-1",
   "generic-expert" all fail this gate item
5. No stock role names appear in this block

---

PHASE 3 — STOCK ROLES

```
STOCK-ROLES:
  - pm               (product value lens)
  - architect        (technical structure lens)
  - strategy         (business and competitive lens)
  - inertia-advocate (status-quo challenge lens — frame anchored to Phase 1
                      status-quo claim; verify_questions from Phase 1 challenges)
```

**GATE** — Phase 3 complete when all four names are listed.

---

PHASE 4 — ROLE MATRIX TABLE

Before writing any role file, assemble all roles into a matrix. The matrix lets you verify
uniqueness across all roles' verify questions and detect collaboration phantoms before
any file is committed.

Write ROLE-MATRIX:

```
ROLE-MATRIX for {area}:

| role | frame (one sentence) | key unique verify question | collaborates_with |
|------|---------------------|---------------------------|-------------------|
| {domain-expert-1} | [frame] | [question only this role would ask first] | [2-4 registry names] |
| ... | ... | ... | ... |
| pm | [frame] | [question only pm would ask first] | [2-4 names] |
| architect | [frame] | [question] | [2-4 names] |
| strategy | [frame] | [question] | [2-4 names] |
| inertia-advocate | [frame anchored to Phase 1 status-quo claim] | [question from Phase 1] | [2-4 names] |
```

After writing the matrix, review across all rows:
- Uniqueness check: each "key unique verify question" must be different in substance
  from every other role's question; if two roles share the same question, revise
  until each row has a question uniquely owned by that role's frame
- Phantom check: each name in `collaborates_with` must appear in the `role` column;
  a name absent from the role column is a [FC-10] CONTRACT VIOLATION (type 1)
- Universalist check: no `collaborates_with` cell contains "all roles" or equivalent

**GATE** — Phase 4 complete when ALL of the following are TRUE:
1. ROLE-MATRIX has one row per role (all Phase 2 experts + all Phase 3 stock roles)
2. Each row's "key unique verify question" is substantively different from all other rows
3. All `collaborates_with` names appear in the `role` column — no phantoms
4. No `collaborates_with` cell contains "all roles" or equivalent universalist entry

---

PHASE 5 — WRITE ROLE FILES

**PREPARE:** Confirm the following inputs before writing any file:
- Phase 0 [FC-4] exact identifier: `verify_questions`
- Phase 0 [FC-5] exact identifier: `simplify_rules`
- Phase 4 ROLE-MATRIX confirmed complete (uniqueness and phantom checks passed)
- Phase 1 INERTIA-SURFACE available for inertia-advocate

PREPARE complete when all four inputs confirmed. Do not begin WRITE until confirmed.

**WRITE:** One `.md` file per role to `.craft/roles/{area}/`. Domain experts first
(Phase 2 order), then stock roles (Phase 3 order).

Use this template for every file:

```yaml
---
name: {per [FC-1]: domain slug; PROHIBITED: "domain-expert", "expert-1"}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Per [FC-2]: epistemic viewpoint — use Phase 4 matrix frame as anchor.
    FAILURE MODE: task list.
    WORKED EXAMPLE (bad):  "Handles reviewing artifacts for domain concerns."
    WORKED EXAMPLE (good): "Sees every schema change through the lens of whether
      the consumer contract survives the update — looking for silent breakage."}

  serves: |
    {Per [FC-3]: beneficiary statement — not a restatement of frame.
    FAILURE MODE: frame restatement.
    WORKED EXAMPLE (bad):  "Ensures schema changes are reviewed for breakage."
    WORKED EXAMPLE (good): "Consumer teams receiving a schema update — they get a
      compatibility verdict before the update reaches their integration."}

lens:
  verify_questions:
    - "{Per [FC-4]: actionable; artifact-specific; use Phase 4 matrix row as anchor}"
    - "{Per [FC-4] uniqueness: confirmed in Phase 4 matrix — no other role in this
       registry would prioritize this question first}"

  simplify_rules:
    - "{Per [FC-5]: opinionated exclusion — 'Skip X unless Y.'
       FAILURE MODE: scope description.
       WORKED EXAMPLE (bad):  'Focus on contract fidelity.'
       WORKED EXAMPLE (good): 'Skip unchanged fields; flag only fields that drop
         a required key or change type in a way a consumer cannot negotiate.'}"

expertise:
  depth: {per [FC-6]}
  relevance: |
    {Per [FC-7]: domain-specific justification.}

scope:
  primary: |
    {Per [FC-8]: main concern. One sentence.}
  boundary: |
    {Per [FC-9]: explicit exclusion. One sentence.}

collaborates_with:
  - {per [FC-10]: Phase 4 matrix collaborates_with entry — registry members only}
  # CONTRACT VIOLATION (type 1) — PHANTOM: name absent from this registry.
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent.
```

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. One `.md` file per role in `.craft/roles/{area}/`
2. Every file uses exact identifiers `verify_questions` and `simplify_rules` per
   [FC-4] and [FC-5]; no contracted or alternate forms
3. No role name violates [FC-1] PROHIBITED NAMES clause
4. Each role's `verify_questions` is consistent with Phase 4 matrix uniqueness check
5. No `collaborates_with` entry contains a type-1 or type-2 CONTRACT VIOLATION per [FC-10]

---

PHASE 6 — REGISTRY SUMMARY

**PREPARE:** Enumerate the `.md` files written in Phase 5. Record as `PHASE5_COUNT`.
Do NOT derive from Phase 3 STOCK-ROLES (4) + Phase 2 expert count. Derivation from
prior-phase plans is a C-27 failure — enumeration from Phase 5 output is required.

PREPARE complete when `PHASE5_COUNT` is recorded.

**WRITE:** `.craft/roles/{area}/REGISTRY.md`:

```
---
area: {area}
generated: {date}
---

## Registry Summary

total_roles: {PHASE5_COUNT — from PREPARE enumeration}

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
  {Phase 2 concerns not addressed by any role; or "none detected."}

inertia_surface: |
  {Phase 1 status-quo claim verbatim — exact sentence. Do not paraphrase.
  Fulfills the EXTENSION-COMMITMENT made in Phase 0.}

Generated by: /org-roles {topic} — {date}
```

FAILURE MODE — HEADING STUB: "## Registry Summary" with no fields populated is not a
complete registry entry; every field listed above must contain substantive content.

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.craft/roles/{area}/REGISTRY.md`
2. `total_roles` equals `PHASE5_COUNT` from the PREPARE enumeration
3. `domain_experts` has one entry per derived expert with `name` and `derivation_source`
4. `inertia_surface` contains Phase 1 status-quo claim verbatim
5. No heading stubs — every field has substantive content

---

## V-03 — Phrasing Register: Surgical C-28 Addition to R5 V-05

**axis:** phrasing-register
**hypothesis:** R5 V-05 scores 99.55/100 under v6, failing only C-28. Examining [FC-1] in
R5 V-05 reveals: `type: string — domain-vocabulary slug; not "domain-expert", "expert-1"`.
This states the prohibition as a type constraint inline — the evaluator reads it as a
positive naming requirement with a parenthetical exception rather than as a named anti-pattern
class. C-28 requires the instruction to "explicitly name at least one class of generic
placeholder name by example." The surgical fix: (1) expand [FC-1] with a standalone
PROHIBITED NAMES sub-clause that names the anti-pattern class explicitly; (2) add a
prominent DO NOT instruction in Phase 2 naming the same anti-patterns; (3) add a gate
item in Phase 2 that checks for placeholder names by name. Three reinforcing points
eliminate the C-28 ambiguity without restructuring any other phase. If this variation
scores 100.00, the R5 V-05 structure is sufficient and the single gap was a presentation
issue in [FC-1], not a structural one.
Falsifiable: if C-28 still fails despite three reinforcing prohibitions, the evaluator
requires a prohibition in the domain derivation BODY (not gate or contract), and a
fourth location must be added.

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
  purpose: answers the Phase 0 diagnostic question — "what is the design-level assumption
    about {topic} that this registry exists to stress-test?" — giving downstream consumers
    the unchallenged assumption the inertia-advocate is built to surface
```

**PART B — FIELD CONTRACT**

All role files must conform to this contract. Field identifiers are binding.

```
FIELD-CONTRACT for /org-roles {topic}:

  [FC-1]  name
          type: string — domain-vocabulary slug
          PROHIBITED NAMES (name any of these and the contract is violated):
            "domain-expert"   — placeholder; applies to any product; no domain signal
            "expert-1"        — placeholder; numeric suffix carries no domain content
            "generic-expert"  — placeholder; explicitly generic
            "role-1"          — placeholder; positional, not semantic
          A compliant name is derived from the domain concern it addresses.
          BAD:  "domain-expert" (prohibited by this contract)
          GOOD: "auth-boundary-verifier" (derived from the concern: auth surface leakage)

  [FC-2]  orientation.frame
          type: string — epistemic viewpoint ("sees X through the lens of Y")
          FAILURE MODE: task list / job description
          BAD:  "Responsible for reviewing artifacts and ensuring requirements are
                 captured before handoff."
          GOOD: "Sees every proposal through the lens of whether the claimed benefit
                 justifies the cost of the change — looking for cases where the status
                 quo handles the use case adequately without new infrastructure."

  [FC-3]  orientation.serves
          type: string — beneficiary statement; NOT a restatement of frame
          FAILURE MODE: frame restatement
          BAD:  "Ensures proposals are evaluated for cost-benefit ratio."
                (same information as frame, different words)
          GOOD: "Engineering leads deciding whether to staff the feature — they get a
                 cost-benefit verdict before roadmap commitment."

  [FC-4]  lens.verify_questions
          EXACT IDENTIFIER: verify_questions
          VIOLATIONS: `verify`, `questions`, `verify_list`, `checks` — all are contract
            violations that break downstream consumers reading by exact key
          type: list (minimum two items); at least one question must be uniquely
            attributable to this role's frame — no other role in this registry would
            prioritize that question first; confirm this before writing the question
          BAD:  "Is the design correct?" (unmeasurable; any role could ask this)
          GOOD: "Does the emitted event schema match the consumer's declared schema
                 version, verifiable in the integration test suite?"

  [FC-5]  lens.simplify_rules
          EXACT IDENTIFIER: simplify_rules
          VIOLATIONS: `simplify`, `rules`, `constraints`, `guidelines` — all are contract
            violations that break downstream consumers reading by exact key
          type: list (minimum one item); opinionated exclusion or scope reduction —
            NOT a description of what the role does
          BAD:  "Focus on boundary correctness and constraint-gap concerns"
                (describes, not excludes)
          GOOD: "Skip boundary analysis for internal-only components; flag only
                 external surfaces"

  [FC-6]  expertise.depth   — enum: expert | practitioner | senior | principal

  [FC-7]  expertise.relevance — domain-specific justification; not a role-name restatement

  [FC-8]  scope.primary     — main concern this role surfaces; one sentence; domain-specific

  [FC-9]  scope.boundary    — what this role does NOT own; must exclude something specific;
                               one sentence

  [FC-10] collaborates_with
          type: list — only roles present in this registry's output
          CONTRACT VIOLATION (type 1) — PHANTOM: a role name absent from the output set;
            phantom names silently break integration with downstream skills
          CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent;
            universalist listing is structurally inert and breaks dependency reasoning
          Both violations are gate failures
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT has all three elements: `field_name` = `inertia_surface`;
   `population_source` names Phase 1 and the INERTIA-SURFACE artifact; `purpose`
   answers the diagnostic question with a domain-specific tension statement
2. FIELD-CONTRACT is written with all ten items [FC-1] through [FC-10]
3. [FC-1] contains a PROHIBITED NAMES sub-clause that names at least "domain-expert"
   and "expert-1" explicitly — not as inline type constraints but as named anti-patterns
4. Items [FC-4] and [FC-5] display exact identifier strings `verify_questions` and
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
    existing capability that makes the feature appear redundant]

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

DO NOT use placeholder names for derived experts.
The following names are PROHIBITED by FIELD-CONTRACT [FC-1]:
  "domain-expert", "expert-1", "generic-expert", "role-1"
These placeholder names pass visual inspection but violate [FC-1] by construction.
Every derived expert's name must come from the vocabulary of the concern it addresses.

```
DOMAIN-ANALYSIS for {topic}:

  Domain concerns (at minimum three; each a failure the Phase 1 status-quo claim omits):
    1. [concern: what the status quo claim overlooks about this domain]
    2. [concern]
    3. [concern]

  Domain experts derived from concerns:
    - Expert name: [slug per FIELD-CONTRACT [FC-1] — domain vocabulary, not generic;
        PROHIBITED: "domain-expert", "expert-1" — these names violate [FC-1]]
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
5. No derived expert name is a placeholder: "domain-expert", "expert-1", "generic-expert"
   all fail this gate item by name — check the exact string, not just the general character
6. No stock role names (pm, architect, strategy, inertia-advocate) appear in this block

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
      # PROHIBITED: "domain-expert", "expert-1", "generic-expert", "role-1"
      # These names violate [FC-1] and fail the Phase 5 gate
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
2. Every file uses exact identifiers `verify_questions` and `simplify_rules` per
   FIELD-CONTRACT [FC-4] and [FC-5] — the identifier strings appear verbatim
   as YAML keys; not `verify`, `simplify`, or any contracted form
3. No role file uses a name from the [FC-1] PROHIBITED NAMES list: "domain-expert",
   "expert-1", "generic-expert", "role-1" all fail this gate item
4. Inertia-advocate: `orientation.frame` anchors to Phase 1 status-quo claim;
   `verify_questions` from Phase 1 challenge questions
5. Each role has at least one `verify_questions` entry uniquely attributable to that
   role's frame (per the PREPARE diagnostic question and template instruction)
6. No `collaborates_with` entries contain type-1 phantom or type-2 universalist
   violations per FIELD-CONTRACT [FC-10]

---

PHASE 6 — REGISTRY SUMMARY

**PREPARE:** Before writing `REGISTRY.md`, enumerate the `.md` files written in Phase 5.
Record this as `PHASE5_COUNT`. This count must come from Phase 5 file enumeration —
not from adding Phase 3 STOCK-ROLES count to Phase 2 expert count. Derivation from
prior-phase plans without verification is a C-27 failure.

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

## V-04 — Combined: Inertia Framing + Role Matrix Table

**axes:** inertia-framing + output-format
**hypothesis:** V-01 makes the status-quo claim the Phase 0 diagnostic anchor, grounding
C-30 by construction and hardening the inertia-advocate's frame before any domain expert
is derived. V-02 adds a ROLE MATRIX TABLE between derivation and file writing, enabling
cross-role uniqueness verification before commitment. This combination targets two
independent failure modes: C-30 (extension purpose disconnected from skill opening) and
C-09/C-21 (verify-question uniqueness verified too late or not at all). The cold hypothesis
in Phase 0 provides the inertia-advocate's stance; Phase 1 refines it from context;
domain experts in Phase 2 respond to the refined hypothesis; the matrix in Phase 4 surfaces
uniqueness violations before any file is written. C-28 is present at [FC-1] PROHIBITED
NAMES and Phase 2 DO NOT instruction.
Falsifiable: if the matrix step is skipped or treated nominally (every row has the same
question), the combination adds no uniqueness benefit over V-01 alone.

---

You are running `/org-roles {topic}`.

---

PHASE 0 — COLD HYPOTHESIS, FIELD CONTRACT, EXTENSION COMMITMENT

**Opening diagnostic:** What is the strongest argument that the status quo is sufficient —
that `{topic}` is not worth building?

Write a COLD HYPOTHESIS before reading any context:

```
COLD-HYPOTHESIS: [one sentence — the most reasonable argument that the existing system
  already handles the primary use case of {topic}, making the feature premature or
  unnecessary]
```

This hypothesis will be refined in Phase 1 from actual context.

**EXTENSION-COMMITMENT:**

```
EXTENSION-COMMITMENT:
  field_name: inertia_surface
  population_source: Phase 1, INERTIA-SURFACE block, status-quo claim field
  purpose: answers the Phase 0 opening diagnostic — "what is the strongest argument
    that the status quo is sufficient for {topic}?" — the refined claim this registry
    is designed to stress-test through all role perspectives
```

**FIELD CONTRACT:**

```
FIELD-CONTRACT for /org-roles {topic}:

  [FC-1]  name
          type: string — domain-vocabulary slug
          PROHIBITED NAMES:
            "domain-expert" — no domain signal; prohibited
            "expert-1"      — numeric placeholder; prohibited
            "generic-expert"— explicitly generic; prohibited
            "role-1"        — positional, not semantic; prohibited
          The name must derive from the vocabulary of the concern it addresses.
          BAD:  "domain-expert" (prohibited)
          GOOD: "signal-fidelity-analyst" (derived from signal accuracy concern)

  [FC-2]  orientation.frame
          type: string — epistemic viewpoint ("sees X through the lens of Y")
          FAILURE MODE: task list
          BAD:  "Reviews proposals for completeness."
          GOOD: "Sees every event schema change through the lens of consumer contract
                 survival — looking for breaking changes that downstream pipelines
                 cannot renegotiate at runtime."

  [FC-3]  orientation.serves
          type: string — beneficiary statement; NOT a restatement of frame
          FAILURE MODE: frame restatement
          BAD:  "Ensures schema changes are reviewed for contract survival."
          GOOD: "Downstream teams receiving schema updates — they get a contract-
                 breakage verdict before the change enters production pipelines."

  [FC-4]  lens.verify_questions
          EXACT IDENTIFIER: verify_questions
          PROHIBITED: verify | questions | checks | verify_list (all break downstream)
          type: list; minimum two items; at least one question uniquely attributable
            to this role's frame — "no other role in this registry would prioritize
            this question first"; confirm uniqueness before writing
          BAD:  "Does the design meet requirements?" (unmeasurable; non-unique)
          GOOD: "Are all consumer-declared version constraints satisfied by the
                 proposed schema, verifiable against the contract fixture files?"

  [FC-5]  lens.simplify_rules
          EXACT IDENTIFIER: simplify_rules
          PROHIBITED: simplify | rules | constraints | guidelines (all break downstream)
          type: list; minimum one item; opinionated exclusion — NOT a scope description
          BAD:  "Focus on schema contract concerns."
          GOOD: "Skip unchanged fields; flag only fields that add a required key,
                 drop an existing key, or change a field type."

  [FC-6]  expertise.depth   — enum: expert | practitioner | senior | principal

  [FC-7]  expertise.relevance — domain-specific justification

  [FC-8]  scope.primary     — main concern; one sentence

  [FC-9]  scope.boundary    — explicit exclusion; one sentence

  [FC-10] collaborates_with
          type: list — registry members only
          CONTRACT VIOLATION (type 1) — PHANTOM: role absent from this registry
          CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. COLD-HYPOTHESIS written as a complete sentence
2. EXTENSION-COMMITMENT has all three elements; purpose explicitly names the Phase 0
   diagnostic question it answers
3. [FC-1] contains PROHIBITED NAMES with "domain-expert" and "expert-1" named explicitly
4. [FC-4] and [FC-5] display exact identifier strings verbatim

---

PHASE 1 — INERTIA REFINEMENT (context read; cold hypothesis confirmed or revised)

Read `{topic}` context. Confirm or revise the COLD-HYPOTHESIS:

```
INERTIA-SURFACE for {topic}:

  Status-quo claim: [refined from COLD-HYPOTHESIS — grounded in actual context;
    the strongest reasonable argument against building {topic}; references specific
    existing capabilities by name]

  Challenge questions (at minimum three; derived from context):
    1. What specific failure does the status quo produce that this feature resolves?
    2. [context-derived challenge: what does the existing mechanism already handle?]
    3. [context-derived challenge: minimum viable status-quo fix, and why insufficient?]
```

Do not name domain experts in Phase 1.

**GATE** — Phase 1 complete when ALL of the following are TRUE:
1. INERTIA-SURFACE is written
2. Status-quo claim names a specific existing capability (not generic)
3. Three challenge questions present, each citing a specific context-derived concern
4. No domain expert names appear in this block

---

PHASE 2 — CONTEXT ANALYSIS (domain experts derived to challenge Phase 1 surface)

DO NOT use placeholder names: "domain-expert", "expert-1", "generic-expert", "role-1"
are all prohibited by [FC-1]. Every derived expert's name must come from the vocabulary
of the concern it addresses.

```
DOMAIN-ANALYSIS for {topic}:

  Domain concerns (at minimum three; each names a gap the Phase 1 claim misses):
    1. [concern — {topic} vocabulary]
    2. [concern]
    3. [concern]

  Domain experts derived from concerns:
    - Expert name: [per [FC-1]; PROHIBITED: "domain-expert", "expert-1"]
      Concern link: [which concern, by number]
      Domain-vocabulary frame: [per [FC-2]; not a task description]
      Verify focus: [specific artifact or behavior this expert checks first]
    (at minimum one)
```

Do not name stock roles in Phase 2.

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. At least three domain concerns listed in `{topic}` vocabulary
2. Each derived expert has all four attributes: name, concern link, frame, verify focus —
   per expert, not as a total
3. No derived expert name is a [FC-1] placeholder
4. No stock role names appear in this block

---

PHASE 3 — STOCK ROLES

```
STOCK-ROLES:
  - pm               (product value lens)
  - architect        (technical structure lens)
  - strategy         (business and competitive lens)
  - inertia-advocate (status-quo challenge lens — frame anchored to Phase 1
                      status-quo claim; verify_questions from Phase 1 challenges)
```

**GATE** — Phase 3 complete when all four names listed and inertia-advocate names Phase 1
as source.

---

PHASE 4 — ROLE MATRIX TABLE

Write ROLE-MATRIX showing all roles before writing any file. Each row must include
the role's key unique verify question — the question no other role would ask first.

```
ROLE-MATRIX for {area}:

| role | frame (one sentence) | key unique verify question | collaborates_with (2-4) |
|------|---------------------|--------------------------|------------------------|
| {expert-1-name} | ... | ... | {name1}, {name2} |
| ... | ... | ... | ... |
| pm | ... | ... | ... |
| architect | ... | ... | ... |
| strategy | ... | ... | ... |
| inertia-advocate | Phase 1 status-quo claim as frame | Phase 1 challenge Q1 | ... |
```

After writing the matrix:
- Uniqueness review: scan the "key unique verify question" column; if any two rows have
  the same question in substance, revise until each question is unique to its row's frame
- Phantom review: every name in "collaborates_with" must appear in the "role" column;
  names absent from the role column are [FC-10] CONTRACT VIOLATION (type 1)

**GATE** — Phase 4 complete when ALL of the following are TRUE:
1. ROLE-MATRIX has one row per role (Phase 2 experts + Phase 3 stock)
2. Each row's unique verify question is substantively different from all other rows
3. All collaborates_with names appear in the role column — no phantoms
4. No universalist entries in collaborates_with column

---

PHASE 5 — WRITE ROLE FILES

**PREPARE:** Confirm before writing:
- [FC-4] exact identifier: `verify_questions` (from Phase 0)
- [FC-5] exact identifier: `simplify_rules` (from Phase 0)
- Phase 4 ROLE-MATRIX uniqueness and phantom checks confirmed complete
- Phase 1 INERTIA-SURFACE available for inertia-advocate

PREPARE complete when all four inputs confirmed.

**WRITE:** One `.md` file per role to `.craft/roles/{area}/`. Domain experts first, then
stock roles. Template for every file:

```yaml
---
name: {per [FC-1]; PROHIBITED: "domain-expert", "expert-1", "generic-expert", "role-1"}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Per [FC-2]. Domain experts: Phase 2 frame. Inertia-advocate: Phase 1 claim.
    FAILURE MODE: task list.
    WORKED EXAMPLE (bad):  "Reviews artifacts for domain concerns."
    WORKED EXAMPLE (good): "Sees every [artifact] through the lens of [specific concern]
      — looking for [specific gap]."}

  serves: |
    {Per [FC-3]: beneficiary. NOT a restatement of frame.
    FAILURE MODE: frame restatement.
    WORKED EXAMPLE (bad):  "Ensures [concern] is reviewed." (same as frame)
    WORKED EXAMPLE (good): "[Stakeholder] deciding [decision] — they get [signal]."}

lens:
  verify_questions:
    - "{Per [FC-4]: artifact-specific; use Phase 4 matrix row as anchor}"
    - "{Per [FC-4] uniqueness: confirmed unique in Phase 4 matrix — no other role
       asks this first}"

  simplify_rules:
    - "{Per [FC-5]: opinionated exclusion — 'Skip X unless Y.'
       FAILURE MODE: scope description.
       WORKED EXAMPLE (bad):  'Focus on [concern area].'
       WORKED EXAMPLE (good): 'Skip [X]; flag only [Y with condition Z].'}"

expertise:
  depth: {per [FC-6]}
  relevance: |
    {Per [FC-7]: domain-specific justification.}

scope:
  primary: |
    {Per [FC-8]: main concern. One sentence.}
  boundary: |
    {Per [FC-9]: explicit exclusion. One sentence.}

collaborates_with:
  - {per [FC-10]; Phase 4 matrix value — registry members only}
  # CONTRACT VIOLATION (type 1) — PHANTOM: name absent from this registry.
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent.
```

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. One `.md` file per role in `.craft/roles/{area}/`
2. Exact identifiers `verify_questions` and `simplify_rules` used in every file
3. No role name is a [FC-1] PROHIBITED NAME
4. Each role's verify_questions consistent with Phase 4 uniqueness check
5. No [FC-10] CONTRACT VIOLATIONS in any collaborates_with field

---

PHASE 6 — REGISTRY SUMMARY

**PREPARE:** Enumerate `.md` files from Phase 5. Record as `PHASE5_COUNT`.
Do NOT derive from Phase 3 + Phase 2 counts — enumerate Phase 5 output directly.

PREPARE complete when `PHASE5_COUNT` recorded.

**WRITE:** `.craft/roles/{area}/REGISTRY.md`:

```
---
area: {area}
generated: {date}
---

## Registry Summary

total_roles: {PHASE5_COUNT — from PREPARE enumeration; not a planned count}

stock_roles:
  - pm
  - architect
  - strategy
  - inertia-advocate

domain_experts:
  - name: {expert-name}
    derivation_source: Phase 2 domain concern #[N]

coverage_gaps: |
  {Phase 2 concerns not covered by any role; or "none detected."}

inertia_surface: |
  {Phase 1 status-quo claim verbatim. Fulfills EXTENSION-COMMITMENT from Phase 0.}

Generated by: /org-roles {topic} — {date}
```

FAILURE MODE — HEADING STUB: "## Registry Summary" with no content below it fails
the registry completeness requirement unconditionally.

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` at `.craft/roles/{area}/REGISTRY.md`
2. `total_roles` = `PHASE5_COUNT` from PREPARE
3. `domain_experts` lists each expert with `name` and `derivation_source`
4. `inertia_surface` contains Phase 1 status-quo claim verbatim
5. No heading stubs

---

## V-05 — Full Synthesis: All Axes

**axes:** inertia-framing + output-format + phrasing-register + lifecycle-emphasis + role-sequence
**hypothesis:** Combines all five innovations: (1) cold inertia hypothesis as Phase 0 diagnostic
anchor — the extension commitment purpose names the opening question explicitly (C-30 by
construction); (2) FC-N contract block with standalone PROHIBITED NAMES clause in [FC-1]
naming "domain-expert" and "expert-1" as anti-pattern class (C-28 as a named contract term);
(3) role matrix table in Phase 4 for cross-role uniqueness verification before file commitment
(C-09/C-21 enforced at matrix stage); (4) DO/DO NOT phrasing register with WORKED EXAMPLE
(bad) + WORKED EXAMPLE (good) pairs in every schema field instruction (C-17, C-18 by
construction); (5) PREPARE/WRITE/GATE lifecycle triad at every output-producing phase
(C-13, C-16, C-19 by construction). Domain experts are derived AFTER the cold inertia
hypothesis (Phase 2) to ensure they respond to the design tension rather than generating
it; stock roles loaded last (Phase 3). The role-sequence innovation is that inertia-advocate
is the first named role (Phase 0 cold hypothesis), domain experts second (Phase 2), and
stock PM/Architect/Strategy third (Phase 3) — the inertia-advocate's stance is independent
of domain-expert framing, which prevents inertia from being softened by domain expertise.
This variation targets the first 100.00 under the v6 rubric by satisfying all thirty
criteria, with the five new v6 criteria (C-26 through C-30) each addressed at two
reinforcing structural locations.
Falsifiable: if integration of all five axes produces prompt length that degrades execution
quality on C-07 (lens depth) or C-09 (uniqueness), a shorter V-03 is preferable despite
lower theoretical ceiling. Score V-05 against V-03 on C-07 and C-09 first.

---

You are running `/org-roles {topic}`.

---

PHASE 0 — REGISTRY DESIGN DECLARATION

**Opening diagnostic:** What is the strongest status-quo argument that `{topic}` is not
worth building — and what design tension must this registry hold to stress-test that argument?

**STEP A — COLD HYPOTHESIS (write before reading any context)**

```
COLD-HYPOTHESIS: [one sentence — the most reasonable argument that the existing system
  already handles the primary value of {topic}, making the feature premature or
  unnecessary; write this without reading the spec — it will be refined in Phase 1]
```

**STEP B — EXTENSION COMMITMENT**

```
EXTENSION-COMMITMENT:
  field_name: inertia_surface
  population_source: Phase 1, INERTIA-SURFACE block, status-quo claim field
  purpose: answers the Phase 0 opening diagnostic — "what is the strongest status-quo
    argument that {topic} is not worth building?" — giving downstream consumers the
    specific design tension this registry was composed to hold
```

**STEP C — FIELD CONTRACT**

All role files must conform to this contract. Identifiers are binding terms.

```
FIELD-CONTRACT for /org-roles {topic}:

  [FC-1]  name
          type: string — domain-vocabulary slug
          PROHIBITED NAMES (any of these is a [FC-1] CONTRACT VIOLATION):
            "domain-expert"  — generic placeholder; no domain signal by construction
            "expert-1"       — numeric placeholder; no semantic content
            "generic-expert" — explicitly generic; prohibited
            "role-1"         — positional label; prohibited
          A compliant name derives from the vocabulary of the concern it addresses.
          BAD:  "domain-expert" (prohibited — [FC-1] CONTRACT VIOLATION)
          GOOD: "event-schema-fidelity-analyst" (derived from schema-accuracy concern)

  [FC-2]  orientation.frame
          type: string — epistemic viewpoint ("sees X through the lens of Y")
          FAILURE MODE: task list / job description
          WORKED EXAMPLE (bad):  "Responsible for reviewing artifacts and ensuring
            requirements are captured before handoff."
          WORKED EXAMPLE (good): "Sees every proposal through the lens of whether
            the claimed benefit justifies the cost of the change — looking for cases
            where the status quo handles the use case adequately without new
            infrastructure."

  [FC-3]  orientation.serves
          type: string — beneficiary statement; NOT a restatement of frame
          FAILURE MODE: frame restatement (same information, different words)
          WORKED EXAMPLE (bad):  "Ensures proposals are evaluated for cost-benefit
            ratio." (restates frame)
          WORKED EXAMPLE (good): "Engineering leads deciding whether to staff the
            feature — they get a cost-benefit verdict before roadmap commitment."

  [FC-4]  lens.verify_questions
          EXACT IDENTIFIER: verify_questions
          CONTRACT VIOLATIONS: `verify` | `questions` | `verify_list` | `checks`
            — any contracted form breaks downstream consumers by key-lookup failure
          type: list; minimum two items; at least one question uniquely attributable
            to this role's frame — "a question no other role in this registry would
            prioritize first"; confirm uniqueness before writing each question
          WORKED EXAMPLE (bad):  "Is the design correct?" (unmeasurable; any role
            could ask this; fails both actionability and uniqueness)
          WORKED EXAMPLE (good): "Does the emitted event schema satisfy the consumer's
            declared version constraint, verifiable in the integration contract
            fixture files?"

  [FC-5]  lens.simplify_rules
          EXACT IDENTIFIER: simplify_rules
          CONTRACT VIOLATIONS: `simplify` | `rules` | `constraints` | `guidelines`
            — any alternate form breaks downstream consumers by key-lookup failure
          type: list; minimum one item; opinionated exclusion or scope reduction —
            NOT a description of what the role values
          WORKED EXAMPLE (bad):  "Focus on schema contract and fidelity concerns."
            (describes priority; excludes nothing — not a simplify rule)
          WORKED EXAMPLE (good): "Skip unchanged fields entirely; flag only fields
            that add a required key, drop an existing key, or change a type in a
            way a consumer cannot negotiate."

  [FC-6]  expertise.depth   — enum: expert | practitioner | senior | principal

  [FC-7]  expertise.relevance — domain-specific justification referencing a constraint
                                 from context; not a restatement of role name

  [FC-8]  scope.primary     — main concern this role surfaces; one sentence;
                               uses domain vocabulary

  [FC-9]  scope.boundary    — what this role does NOT own; explicit exclusion;
                               one sentence; names something specific

  [FC-10] collaborates_with
          type: list — registry members only
          CONTRACT VIOLATION (type 1) — PHANTOM: a role name absent from this
            registry's output set; phantom names silently break all downstream
            skills that resolve collaboration links by exact name lookup
          CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or "everyone"
            or equivalent; universalist listing is structurally inert and prevents
            directed dependency reasoning over the collaboration graph
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. COLD-HYPOTHESIS written as a complete one-sentence claim
2. EXTENSION-COMMITMENT has all three elements: `field_name` = `inertia_surface`;
   `population_source` names Phase 1 and the INERTIA-SURFACE artifact; `purpose`
   explicitly names the Phase 0 opening diagnostic question it answers
3. [FC-1] contains PROHIBITED NAMES sub-clause naming "domain-expert" and "expert-1"
   explicitly as contract violations — not inline type constraints
4. [FC-4] and [FC-5] display exact identifier strings `verify_questions` and
   `simplify_rules` verbatim under their EXACT IDENTIFIER labels
5. [FC-10] labels both prohibitions as CONTRACT VIOLATION (type 1) and
   CONTRACT VIOLATION (type 2)

---

PHASE 1 — INERTIA REFINEMENT (first context read; cold hypothesis confirmed or revised)

**DO** read `{topic}` context for existing system capabilities.
**DO** confirm or revise the Phase 0 COLD-HYPOTHESIS based on what the context actually says.
**DO** write INERTIA-SURFACE:

```
INERTIA-SURFACE for {topic}:

  Status-quo claim: [refined from COLD-HYPOTHESIS using actual context; the strongest
    reasonable argument against building {topic}; names a specific existing capability]

  Challenge questions (at minimum three; each domain-specific):
    1. What specific failure does the status quo produce that this feature resolves?
       (Name the failure from context; if unspecified, flag as a spec gap.)
    2. [context-derived: what does the existing mechanism already handle for the
       primary use case?]
    3. [context-derived: what is the minimum viable status-quo fix, and why is it
       insufficient according to context?]
```

**DO NOT** name domain experts in Phase 1. Domain experts are derived in Phase 2
to challenge this surface.

The status-quo claim will be copied verbatim to `inertia_surface` in Phase 6.

**GATE** — Phase 1 complete when ALL of the following are TRUE:
1. INERTIA-SURFACE written with status-quo claim and three challenge questions
2. Status-quo claim explicitly names a specific existing capability in `{topic}` vocabulary
3. Status-quo claim references Phase 0 COLD-HYPOTHESIS (confirmed or revised with reason)
4. At least three challenge questions cite specific context-derived concerns
5. No domain expert names appear in this block

---

PHASE 2 — CONTEXT ANALYSIS (domain experts; derived to challenge the Phase 1 surface)

**DO** read full `{topic}` context. Derive domain experts from concerns the Phase 1
status-quo claim fails to address.
**DO** treat each derived expert as your answer to: "who holds a concern this status-quo
argument overlooks?"
**DO NOT** use placeholder names.

PROHIBITED by [FC-1] — naming any of these is a contract violation:
  "domain-expert", "expert-1", "generic-expert", "role-1"
These patterns pass visual inspection but carry no domain signal and violate [FC-1] by
construction. The name must come from the vocabulary of the concern it addresses.

```
DOMAIN-ANALYSIS for {topic}:

  Domain concerns (at minimum three; each names a gap the Phase 1 claim misses):
    1. [concern: what the status quo overlooks — {topic} vocabulary]
    2. [concern]
    3. [concern]

  Domain experts derived from concerns:
    - Expert name: [per [FC-1] — PROHIBITED: "domain-expert", "expert-1",
        "generic-expert", "role-1" — see Phase 0 [FC-1] PROHIBITED NAMES]
      Concern link: [which concern above, by number]
      Domain-vocabulary frame: [per [FC-2] — epistemic viewpoint;
        DO NOT write a task description]
      Verify focus: [artifact or behavior this expert checks first]
    (at minimum one)
```

**DO NOT** name PM, Architect, Strategy, or inertia-advocate in Phase 2.

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. DOMAIN-ANALYSIS written with populated concerns list
2. At least three concerns use vocabulary specific to `{topic}`
3. Each derived expert lists all four attributes individually:
   name, concern link, domain-vocabulary frame, verify focus —
   per expert; a single missing attribute in any entry fails this item
4. Each expert's concern link names a gap the Phase 1 status-quo claim misses
5. No derived expert name is a [FC-1] placeholder:
   "domain-expert", "expert-1", "generic-expert", "role-1" all fail this item by name
6. No stock role names appear in this block

---

PHASE 3 — STOCK ROLES

**DO** write STOCK-ROLES after Phase 2 is complete:

```
STOCK-ROLES:
  - pm               (product value and user outcome lens)
  - architect        (technical structure and system boundary lens)
  - strategy         (business model and competitive position lens)
  - inertia-advocate (status-quo challenge lens — orientation.frame anchored to
                      Phase 1 status-quo claim; verify_questions sourced from
                      Phase 1 challenge questions)
```

**DO NOT** introduce domain experts in Phase 3. Domain derivation is complete after Phase 2.

**GATE** — Phase 3 complete when ALL of the following are TRUE:
1. All four stock role names listed with lens descriptors
2. inertia-advocate identifies Phase 1 as source for frame and verify_questions
3. Phase 1 INERTIA-SURFACE confirmed available

---

PHASE 4 — OUTPUT AREA AND ROLE MATRIX TABLE

**Step A — Output Area:**

```
OUTPUT-AREA: .craft/roles/{area}/
```

Area slug uses domain vocabulary from Phase 2. NOT: `default`, `generic`, `roles`.

**Step B — Role Matrix Table (all roles visible before any file is written):**

Write ROLE-MATRIX. Include every role from Phase 2 and Phase 3:

```
ROLE-MATRIX for {area}:

| role | frame (one sentence) | key unique verify question | collaborates_with |
|------|---------------------|--------------------------|-------------------|
| {expert-1} | ... | [question only this role asks first] | {name}, {name} |
| ... | ... | ... | ... |
| pm | ... | ... | ... |
| architect | ... | ... | ... |
| strategy | ... | ... | ... |
| inertia-advocate | [Phase 1 status-quo claim as epistemic stance] | [Phase 1 Q1] | ... |
```

After writing the matrix, perform two checks before proceeding:
- **Uniqueness check:** scan the "key unique verify question" column; if any two rows share
  the same question in substance, revise the lower-uniqueness row until every question is
  distinctly owned by that row's frame. A question owned by no other role is the target.
- **Phantom check:** every name in "collaborates_with" must appear in the "role" column;
  absent names are [FC-10] CONTRACT VIOLATION (type 1). Correct before proceeding.

**GATE** — Phase 4 complete when ALL of the following are TRUE:
1. OUTPUT-AREA written with domain-vocabulary area slug
2. ROLE-MATRIX has one row per role
3. Each "key unique verify question" is substantively different from all other rows
4. All collaborates_with names appear in the role column — no phantoms
5. No universalist entries in collaborates_with column

---

PHASE 5 — WRITE ROLE FILES

**PREPARE:** Confirm the following before writing any file:
- Phase 0 [FC-4] exact identifier: `verify_questions` (retrieve verbatim from [FC-4])
- Phase 0 [FC-5] exact identifier: `simplify_rules` (retrieve verbatim from [FC-5])
- Phase 1 INERTIA-SURFACE: status-quo claim and challenge questions confirmed available
- Phase 2 DOMAIN-ANALYSIS: expert names, frames, verify focuses confirmed available
- Phase 3 STOCK-ROLES: all four names confirmed
- Phase 4 ROLE-MATRIX uniqueness and phantom checks confirmed complete

PREPARE complete when all six inputs confirmed. **DO NOT begin WRITE until PREPARE is complete.**

**Diagnostic question (per role):** What does this role see, serve, verify, and simplify —
and which of its verify questions is so specific to its frame that no other role would
ask it first?

**WRITE:** One `.md` file per role to `.craft/roles/{area}/`. Domain experts first (Phase 2),
stock roles second (Phase 3). For each file, answer the diagnostic question:

```yaml
---
name: {per [FC-1]: domain-vocabulary slug}
  # DO NOT use: "domain-expert", "expert-1", "generic-expert", "role-1"
  # These names are [FC-1] CONTRACT VIOLATIONS — they fail Phase 5 gate item 3
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Per [FC-2]: epistemic viewpoint — use Phase 4 matrix frame as anchor.
    Domain experts: Phase 2 domain-vocabulary frame.
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
    WORKED EXAMPLE (bad):  "Ensures proposals are evaluated for cost-benefit ratio."
      (same information as frame, different words)
    WORKED EXAMPLE (good): "Engineering leads deciding whether to staff the feature
      — they get a cost-benefit verdict before roadmap commitment."}

lens:
  verify_questions:
    - "{Per [FC-4]: actionable; answerable by artifact-read, code-run, or measurable
       outcome; uses {topic} domain vocabulary}"
    - "{Per [FC-4] uniqueness: before writing, confirm — no other role in this registry
       would prioritize this question first (check against Phase 4 matrix); if any
       other role would ask it first, revise until uniquely attributable to this
       frame. The question must be answerable from an artifact, not an interview.}"

  simplify_rules:
    - "{Per [FC-5]: opinionated exclusion — 'Skip X unless Y.'

       FAILURE MODE: scope description.
       WORKED EXAMPLE (bad):  'Focus on cost-benefit and change-risk concerns.'
       WORKED EXAMPLE (good): 'Skip analysis of changes scoped to internal teams;
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
  - {per [FC-10]: role-name — registry members only; Phase 4 matrix value}
  # CONTRACT VIOLATION (type 1) — PHANTOM: name absent from this registry.
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent.
```

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. One `.md` file exists per role in `.craft/roles/{area}/`
2. Every file uses exact identifiers `verify_questions` and `simplify_rules` per
   [FC-4] and [FC-5] — verbatim as YAML keys; `verify`, `simplify`, or any contracted
   form is a contract violation that fails this item
3. No role file uses a name from the [FC-1] PROHIBITED NAMES list:
   "domain-expert", "expert-1", "generic-expert", "role-1" all fail this item
4. Inertia-advocate: `orientation.frame` anchors to Phase 1 status-quo claim;
   `verify_questions` sourced from Phase 1 INERTIA-SURFACE challenge questions
5. Each role has at least one `verify_questions` entry uniquely attributable to that
   role's frame — confirmed against Phase 4 ROLE-MATRIX
6. No `collaborates_with` entries contain type-1 PHANTOM or type-2 UNIVERSALIST
   violations per [FC-10]

---

PHASE 6 — REGISTRY SUMMARY

**PREPARE:** Before writing `REGISTRY.md`:
1. Enumerate the `.md` files written in Phase 5 — list them explicitly
2. Record the count as `PHASE5_COUNT`
3. **DO NOT** derive this count by adding Phase 3 STOCK-ROLES (4) to Phase 2 expert count
   — that derivation is a C-27 failure; it uses a plan rather than enumerating the actual
   Phase 5 output

PREPARE complete when `PHASE5_COUNT` is confirmed from Phase 5 file enumeration.

**Diagnostic question:** What does this registry as a whole commit to — what design tension
does it hold, what coverage does it provide, and what gaps does it explicitly acknowledge?

**WRITE:** `.craft/roles/{area}/REGISTRY.md`:

```
---
area: {area}
generated: {date}
---

## Registry Summary

total_roles: {PHASE5_COUNT — from PREPARE enumeration; NOT a planned count from prior phases}

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
  A genuine diagnostic answer — not a heading stub or generic statement.}

inertia_surface: |
  {Phase 1 status-quo claim verbatim — exact sentence from INERTIA-SURFACE block.
  DO NOT paraphrase. This fulfills the EXTENSION-COMMITMENT made in Phase 0.}

Generated by: /org-roles {topic} — {date}
```

**FAILURE MODE — HEADING STUB:** Writing "## Registry Summary" with no fields populated
below it is not a registry. Every field above must contain substantive content that could
not have been written without running all prior phases. A heading with an empty body fails
the registry completeness requirement unconditionally.

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.craft/roles/{area}/REGISTRY.md`
2. `total_roles` equals `PHASE5_COUNT` from PREPARE enumeration — not a planned count
3. `domain_experts` lists each derived expert with `name` and `derivation_source`
4. `inertia_surface` contains the Phase 1 status-quo claim verbatim — not paraphrased;
   this validates the EXTENSION-COMMITMENT made in Phase 0
5. No heading stubs — every field has substantive content below its identifier

---

## Round 6 Criterion Coverage Map

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-26** FC-N contract block | Phase 0 FIELD CONTRACT [FC-1]–[FC-10] | Phase 0 FIELD CONTRACT [FC-1]–[FC-10] | Phase 0 FIELD CONTRACT [FC-1]–[FC-10] | Phase 0 FIELD CONTRACT [FC-1]–[FC-10] | Phase 0 FIELD CONTRACT [FC-1]–[FC-10] |
| **C-27** PREPARE sub-step + PHASE5_COUNT | Phase 6 PREPARE; PHASE5_COUNT; derivation failure named | Phase 6 PREPARE; PHASE5_COUNT; derivation failure named | Phase 6 PREPARE; PHASE5_COUNT; derivation failure named | Phase 6 PREPARE; PHASE5_COUNT; derivation failure named | Phase 6 PREPARE; PHASE5_COUNT; derivation failure named explicitly |
| **C-28** Placeholder name prohibition | [FC-1] PROHIBITED NAMES clause (standalone); Phase 2 DO NOT; Phase 2 gate item 4; Phase 5 gate item 3 | [FC-1] PROHIBITED NAMES clause; Phase 2 DO NOT; Phase 2 gate item 4 | [FC-1] PROHIBITED NAMES sub-clause; Phase 2 DO NOT (explicit); Phase 2 gate item 5; Phase 5 gate item 3 | [FC-1] PROHIBITED NAMES; Phase 2 DO NOT; Phase 2 gate item 3; Phase 5 gate item 3 | [FC-1] PROHIBITED NAMES (standalone contract violation label); Phase 2 DO NOT; Phase 2 gate item 5; Phase 5 gate item 3 — four locations |
| **C-29** CONTRACT VIOLATION framing | [FC-10]: CONTRACT VIOLATION (type 1) PHANTOM + (type 2) UNIVERSALIST | [FC-10]: CONTRACT VIOLATION (type 1) + (type 2) | [FC-10]: CONTRACT VIOLATION (type 1) + (type 2) + template annotation | [FC-10]: CONTRACT VIOLATION (type 1) + (type 2) + template | [FC-10]: CONTRACT VIOLATION (type 1) + (type 2) + template + gate item 6 |
| **C-30** Extension purpose tied to diagnostic | EXTENSION-COMMITMENT purpose: "answers the Phase 0 diagnostic question — 'what is the strongest argument...'" | EXTENSION-COMMITMENT purpose: "answers the Phase 0 diagnostic question — 'what is the strongest existing-system argument...'" | EXTENSION-COMMITMENT purpose: "answers the Phase 0 diagnostic question — 'what is the design-level assumption...'" | EXTENSION-COMMITMENT purpose: "answers the Phase 0 opening diagnostic — 'what is the strongest argument...'" | EXTENSION-COMMITMENT purpose: "answers the Phase 0 opening diagnostic — 'what is the strongest status-quo argument...'" |
| **C-11** Context-first ordering | inertia (Phase 0 cold, Phase 1 context) → domain experts (Phase 2) → stock roles (Phase 3) | domain experts (Phase 2) after inertia (Phase 1); stock roles (Phase 3) | inertia (Phase 1) → domain experts (Phase 2) → stock roles (Phase 3) | inertia (Phase 0 cold, Phase 1 refined) → domain experts (Phase 2) → stock roles (Phase 3) | inertia (Phase 0 cold, Phase 1 refined) → domain experts (Phase 2) → stock roles (Phase 3) |
| **C-21** Uniqueness mandate by construction | [FC-4] uniqueness requirement in contract; template annotation requiring pre-write confirmation | [FC-4] uniqueness requirement; template annotation; Phase 4 matrix uniqueness check pre-write | [FC-4] uniqueness requirement in contract; template annotation with pre-write confirmation | [FC-4] uniqueness requirement; Phase 4 matrix uniqueness check | [FC-4] uniqueness requirement; Phase 4 matrix uniqueness check; template annotation with Phase 4 cross-reference |
| **C-09** Role differentiation (output) | uniqueness mandate by construction + inertia-advocate frame anchored distinctly | Phase 4 matrix forces cross-role comparison before file writing | uniqueness mandate by construction | Phase 4 matrix + uniqueness mandate | Phase 4 matrix + uniqueness mandate + DO NOT "write universal questions" |
| **C-18** Contrastive worked example pairs | frame, serves, simplify_rules in template; FC-2, FC-3 in contract | frame, serves, verify_questions, simplify_rules (contract + template) | frame, serves, verify_questions, simplify_rules (contract + template) | frame, serves, simplify_rules in template; FC-2, FC-3, FC-4, FC-5 in contract | frame, serves, verify_questions, simplify_rules in template + contract — maximum coverage |
| **C-19** Multi-item completion gate | All phases: 4–6 gate items per phase | All phases: 3–5 gate items per phase | All phases: 4–6 gate items per phase | All phases: 3–5 gate items per phase | All phases: 5–6 gate items per phase |

**Predicted scores against v6 rubric (all five previous essential and recommended criteria pass by construction):**

```
V-01: (5/5)*60 + (3/3)*30 + (22/22)*10  =  60.0 + 30.0 + 10.0  =  100.00  GOLDEN (predicted)
      C-28 PASS: [FC-1] PROHIBITED NAMES standalone clause + Phase 2 gate item + Phase 5 gate item
      C-30 PASS: EXTENSION-COMMITMENT purpose explicitly names Phase 0 diagnostic question
      C-26 PASS: FIELD-CONTRACT [FC-1]–[FC-10] is standalone referenced block
      C-27 PASS: Phase 6 PREPARE sub-step declares PHASE5_COUNT before WRITE
      C-29 PASS: [FC-10] CONTRACT VIOLATION (type 1) and (type 2)

V-02: (5/5)*60 + (3/3)*30 + (22/22)*10  =  60.0 + 30.0 + 10.0  =  100.00  GOLDEN (predicted)
      C-28 PASS: [FC-1] PROHIBITED NAMES + Phase 2 DO NOT + Phase 2 gate item 4
      C-11 risk: domain experts (Phase 2) precede stock roles (Phase 3); Phase 1 is inertia.
      C-11 PASS predicted — domain experts load before stock roles satisfies context-first.

V-03: (5/5)*60 + (3/3)*30 + (22/22)*10  =  60.0 + 30.0 + 10.0  =  100.00  GOLDEN (predicted)
      C-28 PASS: [FC-1] PROHIBITED NAMES sub-clause (standalone, not inline type constraint);
      Phase 2 DO NOT prohibition; Phase 2 gate item 5; Phase 5 gate item 3 — four locations.
      All other criteria preserved from R5 V-05 which scored 21/22.

V-04: (5/5)*60 + (3/3)*30 + (22/22)*10  =  60.0 + 30.0 + 10.0  =  100.00  GOLDEN (predicted)
      All five new criteria addressed. Matrix table adds no risk to prior passing criteria.

V-05: (5/5)*60 + (3/3)*30 + (22/22)*10  =  60.0 + 30.0 + 10.0  =  100.00  GOLDEN (predicted)
      Full synthesis. Risk: prompt length. C-07 execution depth is the most likely execution
      failure if length degrades attention on verify_questions quality.
      Hedge: V-03 is the minimal-change 100.00 candidate; V-05 is the maximum-structure candidate.
```
