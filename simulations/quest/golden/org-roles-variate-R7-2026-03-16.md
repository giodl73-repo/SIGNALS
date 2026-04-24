---
skill: quest-variate
skill_target: org-roles
date: 2026-03-16
round: R7
rubric_version: v7
status: variate
---

# org-roles Variate — Round 7

**Date:** 2026-03-16
**Skill:** org-roles
**Rubric:** v7 (C-01 through C-33; new in v7: C-31 placeholder prohibition at minimum three
independent checkpoints, C-32 PREPARE sub-step names the count-bypass anti-pattern, C-33
CONTRACT VIOLATION labels from [FC-10] mirrored in Phase 5 template annotation)
**Round:** R7 — single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

---

## Round 7 Variation Map

| V | Axis | Primary C targets | Hypothesis |
|---|------|------------------|------------|
| V-01 | role-sequence | C-31 PASS (3 checkpoints), C-32 PASS, C-33 PASS | Inertia-advocate derived FIRST from context (not cold), domain experts derived explicitly to challenge it; derivation order makes inertia the structural constraint rather than the final add-on; all three v7 mechanisms preserved |
| V-02 | output-format | C-31 PASS, C-09 improvement, C-21 improvement | Per-role DIAGNOSIS CARD intermediate step forces frame + uniqueness assertion before YAML writing; cross-card uniqueness check prevents duplicate verify_questions before any file is committed |
| V-03 | phrasing-register | C-31 PASS (3 named sites), C-32 PASS, C-33 PASS | Each phase opens with its failure modes BEFORE instructions — failure-mode-first register; anti-patterns are the opening frame for every step, making prohibitions structurally unavoidable |
| V-04 | role-sequence + output-format | C-31 PASS, C-09 + C-21 improvement | Combines V-01 context-first inertia derivation and V-02 Diagnosis Card intermediate step; inertia card is written first and visible to all subsequent card authors |
| V-05 | all axes | C-31 PASS (explicit site labels), C-32 PASS, C-33 PASS — 100.00 target | Full synthesis: cold hypothesis base (R6 V-01), Diagnosis Card intermediate step (V-02), failure-mode-first phase openings (V-03), plus explicit C-31-SITE-N labels at all three prohibition checkpoints — self-documenting three-site structure |

---

## V-01 — Role Sequence: Context-First Inertia Derivation

**axis:** role-sequence
**hypothesis:** R6 V-01 derives the inertia-advocate from a cold hypothesis written before
context is loaded, then refines it in Phase 1. This variate reads context first and derives
the inertia-advocate fully in Phase 1 — a context-grounded derivation rather than a cold
one — and makes that derived inertia-advocate the structural constraint for Phase 2: every
domain expert must name a specific gap in the inertia claim, not a generic concern. The
inertia-advocate is STOCK-ROLE-0 — derived before PM, Architect, Strategy, and before any
domain expert — so all subsequent roles are positioned as challengers or complements to an
already-specified inertia frame. Phase 3 then lists only the three remaining stock roles (PM,
Architect, Strategy). Phase 5 writes the inertia-advocate file first. The three-checkpoint
C-31 mechanism is preserved: [FC-1] PROHIBITED NAMES clause, Phase 2 DO NOT instruction,
Phase 5 GATE item. The C-32 mechanism is preserved: Phase 6 PREPARE names "count-bypass
failure" as a named anti-pattern. C-33 is preserved: CONTRACT VIOLATION labels from [FC-10]
are mirrored verbatim in the Phase 5 template annotation.
Falsifiable: if context-first inertia derivation produces frames that are less adversarial
(because the model finds the status-quo less compelling after reading the spec's motivation
section), the inertia quality degrades compared to the cold-hypothesis approach even though
structural compliance is identical.

---

You are running `/org-roles {topic}`.

---

PHASE 0 — FIELD CONTRACT AND EXTENSION COMMITMENT

Before reading any context, establish the binding field specifications and registry extension.

**EXTENSION-COMMITMENT:**

```
EXTENSION-COMMITMENT:
  field_name: inertia_surface
  population_source: Phase 1, INERTIA-DERIVATION block, status-quo claim field
  purpose: answers the Phase 0 diagnostic question — "what is the strongest argument
    that the status quo is sufficient for {topic}?" — giving downstream consumers
    the exact design tension this role registry was composed to test
```

**FIELD CONTRACT:**

```
FIELD-CONTRACT for /org-roles {topic}:

  [FC-1]  name
          type: string — domain-vocabulary slug derived from context
          PROHIBITED NAMES: "domain-expert", "expert-1", "generic-expert", "role-1"
          These are placeholder anti-patterns. They pass visual inspection but carry
          no domain content. A name that would apply to any product is prohibited.
          The name must come from vocabulary specific to {topic}'s concern space.
          BAD:  "domain-expert"  — could appear in any registry for any product
          GOOD: "event-schema-fidelity-analyst" — specific to this domain's concern

  [FC-2]  orientation.frame
          type: string — epistemic viewpoint ("sees X through the lens of Y")
          FAILURE MODE: task description / job responsibility list
          BAD:  "Responsible for reviewing spec and ensuring coverage"
          GOOD: "Sees every proposed change through the lens of whether the current
                 system already handles the scenario without modification"

  [FC-3]  orientation.serves
          type: string — beneficiary statement; NOT a restatement of frame
          FAILURE MODE: frame restatement carrying the same information
          BAD:  "Ensures the status quo is considered in all proposals"
          GOOD: "Engineering leads deciding whether to staff {topic} — they receive
                 a verdict on whether the existing system is genuinely insufficient"

  [FC-4]  lens.verify_questions
          EXACT IDENTIFIER: verify_questions
          PROHIBITED IDENTIFIERS: verify | questions | checks | verify_list
          All prohibited identifiers break downstream consumers that read by exact key
          type: list; minimum two items; at least one question uniquely attributable
            to this role's frame — no other role in this registry would prioritize
            that question first; confirm uniqueness before writing each question
          BAD:  "Is the design complete?" (any role could ask this)
          GOOD: "Does the spec name a specific behavior the current system fails to
                 produce — verifiable in the acceptance criteria section?"

  [FC-5]  lens.simplify_rules
          EXACT IDENTIFIER: simplify_rules
          PROHIBITED IDENTIFIERS: simplify | rules | constraints | guidelines
          All prohibited identifiers break downstream consumers that read by exact key
          type: list; minimum one item; opinionated exclusion — NOT a scope summary
          BAD:  "Focus on status-quo concerns" (describes scope; does not exclude)
          GOOD: "Skip proposals that add behavior without altering any existing API
                 contract; flag only proposals that invalidate a current capability"

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
1. EXTENSION-COMMITMENT has all three elements: `field_name` = `inertia_surface`;
   `population_source` names Phase 1 and the INERTIA-DERIVATION artifact; `purpose`
   names the Phase 0 diagnostic question it answers
2. FIELD-CONTRACT is written with all ten items [FC-1] through [FC-10]
3. [FC-1] contains the PROHIBITED NAMES clause naming at least "domain-expert" and
   "expert-1" explicitly as anti-patterns
4. [FC-4] and [FC-5] display exact identifier strings `verify_questions` and
   `simplify_rules` under EXACT IDENTIFIER labels — both strings appear verbatim

---

PHASE 1 — INERTIA DERIVATION (context read; inertia-advocate derived first)

Read `{topic}` context. Your goal in this phase is to derive the inertia-advocate — the
role that argues the status quo is sufficient — before any other role is named. Write an
INERTIA-DERIVATION block:

```
INERTIA-DERIVATION for {topic}:

  Status-quo claim: [The strongest argument that {topic} is unnecessary or premature —
    grounded in the actual context you just read. Name the specific existing capability
    that makes {topic} redundant, or flag that no such capability exists (which changes
    the inertia claim to "insufficient evidence of failure, not proven need")]

  Inertia-advocate profile:
    name: [domain-vocabulary slug per [FC-1] — PROHIBITED: "domain-expert", "expert-1"]
    frame: [epistemic viewpoint anchored to the status-quo claim above — per [FC-2]]
    serves: [beneficiary of the inertia verdict — per [FC-3]]
    primary_verify_question: [the most adversarial version of "why is this necessary?"]

  Challenge questions (at minimum three; each names a specific gap this claim creates):
    1. What existing mechanism does the status-quo claim rely on — name it?
    2. [What specific scenario does the existing mechanism fail to cover?]
    3. [What is the minimum fix to the status quo that would obsolete {topic}?]
```

Do not name domain experts in Phase 1. Domain experts are derived in Phase 2
specifically to challenge the status-quo claim above.

The status-quo claim will be copied verbatim to `inertia_surface` in Phase 6.

**GATE** — Phase 1 complete when ALL of the following are TRUE:
1. INERTIA-DERIVATION block is written
2. Status-quo claim names a specific existing capability (not a generic statement)
3. Inertia-advocate profile contains all four attributes: name, frame, serves,
   primary_verify_question — all four confirmed present, not just total count
4. Inertia-advocate name passes [FC-1]: not "domain-expert", "expert-1", or any
   prohibited placeholder; uses vocabulary from `{topic}` context
5. At least three challenge questions reference vocabulary from the `{topic}` context
6. No domain expert names appear in this block

---

PHASE 2 — DOMAIN ANALYSIS (experts derived to challenge the Phase 1 inertia claim)

Read `{topic}` context for concerns the Phase 1 inertia claim does not address. Each
domain expert answers: "who holds a concern this status-quo argument overlooks — a concern
the inertia-advocate has no frame to see?"

DO NOT name derived experts with placeholder labels. The following names are
PROHIBITED by [FC-1]: "domain-expert", "expert-1", "generic-expert", "role-1".
These names carry no domain content. Every derived name must come from vocabulary
specific to {topic}'s concern space.

```
DOMAIN-ANALYSIS for {topic}:

  Inertia claim under challenge: [restate Phase 1 status-quo claim in one sentence]

  Domain concerns (at minimum three; each names a gap the inertia claim overlooks):
    1. [concern: specific failure mode or blind spot this inertia claim cannot see —
       name it using {topic} vocabulary]
    2. [concern]
    3. [concern]

  Domain experts derived from concerns:
    - Expert name: [slug per [FC-1] — domain vocabulary; PROHIBITED: "domain-expert",
        "expert-1" — see Phase 0 [FC-1] PROHIBITED NAMES clause]
      Concern link: [which concern above, by number]
      Inertia gap: [why the Phase 1 inertia-advocate's frame cannot surface this concern]
      Domain-vocabulary frame: [per [FC-2] — epistemic viewpoint using concern vocabulary]
      Verify focus: [what artifact or behavior this expert checks first]
    (repeat for each derived expert — at minimum one)
```

Do not name stock roles (pm, architect, strategy) in Phase 2.
Inertia-advocate was derived in Phase 1 — do not re-derive it here.

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. DOMAIN-ANALYSIS block is written with a populated Domain concerns list
2. At least three domain concerns use vocabulary specific to `{topic}`
3. Each derived expert entry lists all five attributes individually:
   name, concern link, inertia gap, domain-vocabulary frame, verify focus —
   checked per expert, not as a total count; a single missing attribute in any
   entry fails this item
4. No derived expert name is a placeholder per [FC-1] PROHIBITED NAMES clause —
   "domain-expert", "expert-1", "generic-expert" fail this gate item
5. No stock role names (pm, architect, strategy) appear in this block
6. Inertia-advocate is not re-derived here — it is referenced from Phase 1

---

PHASE 3 — STOCK ROLES (PM, Architect, Strategy; inertia-advocate is from Phase 1)

```
STOCK-ROLES:
  - pm               (product value and user outcome lens)
  - architect        (technical structure and system boundary lens)
  - strategy         (business model and competitive position lens)
  NOTE: inertia-advocate is already derived in Phase 1; it is a registry member
  and will be written in Phase 5; it is not listed here to avoid double-counting
```

**GATE** — Phase 3 complete when ALL of the following are TRUE:
1. STOCK-ROLES lists the three names (pm, architect, strategy) with lens descriptors
2. inertia-advocate is noted as derived in Phase 1, not re-listed here
3. Phase 1 INERTIA-DERIVATION confirmed available as source for the inertia-advocate file

---

PHASE 4 — OUTPUT AREA

```
OUTPUT-AREA: .roles/{area}/
```

Area slug must use domain vocabulary from Phase 2. NOT: `default`, `generic`, `roles`.

**GATE** — Phase 4 complete when ALL of the following are TRUE:
1. OUTPUT-AREA is written
2. Area slug uses Phase 2 domain vocabulary
3. Path format is exactly `.roles/{area}/`

---

PHASE 5 — WRITE ROLE FILES

**PREPARE:** Confirm the following inputs before writing any file:
- Phase 0 [FC-4] exact identifier: `verify_questions` (retrieve verbatim from [FC-4])
- Phase 0 [FC-5] exact identifier: `simplify_rules` (retrieve verbatim from [FC-5])
- Phase 1 INERTIA-DERIVATION: name, frame, serves, primary_verify_question, challenge questions
- Phase 2 DOMAIN-ANALYSIS: expert names, concern links, inertia gaps, frames, verify focuses
- Phase 3 STOCK-ROLES: three names confirmed (pm, architect, strategy)
- Phase 4 OUTPUT-AREA path confirmed

PREPARE complete when all six inputs are confirmed available. Do not begin WRITE until confirmed.

**WRITE:** One `.md` file per role to `.roles/{area}/`. Write in this order:
inertia-advocate first (Phase 1), then domain experts (Phase 2), then stock roles (Phase 3).

For each file, apply the FIELD CONTRACT:

```yaml
---
name: {per [FC-1]: domain-vocabulary slug; PROHIBITED: "domain-expert", "expert-1"}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Per [FC-2]: epistemic viewpoint.
    Inertia-advocate: Phase 1 INERTIA-DERIVATION frame — the status-quo claim as epistemic stance.
    Domain experts: Phase 2 domain-vocabulary frame anchored to inertia gap.
    Stock roles: standard lens for the role type.

    FAILURE MODE: task-list frame.
    WORKED EXAMPLE (bad):  "Responsible for reviewing proposals and surfacing gaps."
    WORKED EXAMPLE (good): "Sees every proposed change through the lens of whether
      the existing mechanism named in Phase 1 already handles the scenario."}

  serves: |
    {Per [FC-3]: beneficiary statement — not a restatement of frame.

    FAILURE MODE: frame restatement.
    WORKED EXAMPLE (bad):  "Ensures status-quo concerns are surfaced."
    WORKED EXAMPLE (good): "Engineering leads deciding whether to proceed — they receive
      a verdict on whether the Phase 1 inertia claim holds against this proposal."}

lens:
  verify_questions:
    - "{Per [FC-4]: actionable question using {topic} domain vocabulary}"
    - "{Per [FC-4] uniqueness: before writing, confirm — no other role in this registry
       would prioritize this question first; revise until uniquely attributable}"

  simplify_rules:
    - "{Per [FC-5]: opinionated exclusion — 'Skip X unless Y.'

       FAILURE MODE: scope description.
       WORKED EXAMPLE (bad):  'Focus on status-quo concerns.'
       WORKED EXAMPLE (good): 'Skip proposals that preserve all existing contracts;
         flag only proposals that invalidate or extend an existing contract.'}"

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
  # CONTRACT VIOLATION (type 1) — PHANTOM: a role name absent from this registry.
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent.
```

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. One `.md` file exists per role in `.roles/{area}/` — inertia-advocate (Phase 1),
   all domain experts (Phase 2), and all stock roles (Phase 3)
2. Every file uses exact identifiers `verify_questions` and `simplify_rules` per
   [FC-4] and [FC-5] — both strings appear verbatim as YAML keys
3. No role file uses a prohibited name per [FC-1]: "domain-expert", "expert-1",
   "generic-expert" fail this gate item
4. Inertia-advocate: `orientation.frame` anchors to Phase 1 INERTIA-DERIVATION status-quo
   claim; `verify_questions` include Phase 1 primary_verify_question
5. Each role has at least one `verify_questions` entry uniquely attributable to that
   role's frame (confirmed per PREPARE and template uniqueness instruction)
6. No `collaborates_with` entries contain CONTRACT VIOLATION type-1 or type-2 per [FC-10]

---

PHASE 6 — REGISTRY SUMMARY

**PREPARE:** Before writing `REGISTRY.md`, enumerate the `.md` files written in Phase 5.
Record this count as `PHASE5_COUNT`. This count must come from Phase 5 file enumeration —
NOT from adding Phase 3 STOCK-ROLES (3) + Phase 2 expert count + Phase 1 inertia-advocate.
Derivation from prior-phase plans without enumeration is a count-bypass failure — the same
anti-pattern as C-27 applied to registry counts. Only enumeration of Phase 5 files is valid.

PREPARE complete when `PHASE5_COUNT` is recorded from Phase 5 enumeration.

**WRITE:** `.roles/{area}/REGISTRY.md`:

```
---
area: {area}
generated: {date}
---

## Registry Summary

total_roles: {PHASE5_COUNT — from the PREPARE enumeration above; not a computed count}

stock_roles:
  - inertia-advocate  (derived Phase 1)
  - pm
  - architect
  - strategy

domain_experts:
  - name: {expert-name}
    derivation_source: Phase 2 domain concern #[N]
    inertia_gap: {gap in Phase 1 inertia claim this expert addresses}
  (one entry per derived expert)

coverage_gaps: |
  {Phase 2 concerns not addressed by any derived expert; or "none detected."
  A genuine diagnostic answer — not a heading stub.}

inertia_surface: |
  {Phase 1 status-quo claim verbatim — exact sentence from INERTIA-DERIVATION block.
  Do not paraphrase. This fulfills the EXTENSION-COMMITMENT made in Phase 0.}

Generated by: /org-roles {topic} — {date}
```

FAILURE MODE — HEADING STUB: "## Registry Summary" with no fields populated is not a
registry. Every field above must have substantive content.

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.roles/{area}/REGISTRY.md`
2. `total_roles` equals `PHASE5_COUNT` from the PREPARE enumeration
3. `domain_experts` lists each derived expert with `name`, `derivation_source`, and `inertia_gap`
4. `inertia_surface` contains the Phase 1 status-quo claim verbatim — not paraphrased;
   this validates the EXTENSION-COMMITMENT made in Phase 0
5. No heading stubs — every field has substantive content below its header

---

## V-02 — Output Format: Per-Role Diagnosis Card Before YAML Writing

**axis:** output-format
**hypothesis:** Writing YAML files is a serial operation; the model commits to each role's
frame and verify_questions without seeing how all roles' questions compare side by side.
R6 V-02 addressed this with a matrix table between derivation and writing. This variate
takes a different approach: each role must emit a structured DIAGNOSIS CARD (a short
prose-first artifact) before any YAML is written. The Diagnosis Card forces an explicit
uniqueness assertion ("this role's primary verify question is unique because no other role
in this registry would prioritize it first — and the other role most likely to overlap is
[name], but it would ask [different angle]") before the question is committed to YAML.
A cross-card uniqueness scan is required after all cards are written. C-31 is satisfied via
[FC-1] PROHIBITED NAMES clause, Phase 2 DO NOT instruction, and Phase 5 GATE item — three
independent checkpoints. C-32 names "count-bypass failure" in Phase 6 PREPARE. C-33 mirrors
CONTRACT VIOLATION labels from [FC-10] in the Phase 5 YAML template annotation.
Falsifiable: if Diagnosis Cards are written as abbreviated stubs (name + one-line frame) and
do not actually force a uniqueness argument, the Diagnosis Card step provides no structural
benefit over writing YAML directly.

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
          type: string — domain-vocabulary slug derived from context
          PROHIBITED NAMES: "domain-expert", "expert-1", "generic-expert", "role-1"
          These placeholder names pass superficial review but carry no domain signal.
          A name that could apply to any product is prohibited by this contract.
          BAD:  "domain-expert" (no domain content; could appear in any registry)
          GOOD: "retry-budget-compliance-analyst" (specific to this domain's concern)

  [FC-2]  orientation.frame
          type: string — epistemic viewpoint ("sees X through the lens of Y")
          FAILURE MODE: task list / job description
          BAD:  "Responsible for reviewing and surfacing issues"
          GOOD: "Sees every backoff proposal through the lens of whether retry
                 budgets in downstream consumers are violated"

  [FC-3]  orientation.serves
          type: string — beneficiary statement; NOT a restatement of frame
          FAILURE MODE: frame restatement
          BAD:  "Ensures retry budget concerns are raised"
          GOOD: "Service owners deploying the change — they receive a retry-budget
                 impact verdict before the feature ships"

  [FC-4]  lens.verify_questions
          EXACT IDENTIFIER: verify_questions
          PROHIBITED IDENTIFIERS: verify | questions | checks | verify_list
          All prohibited identifiers break downstream consumers that read by exact key
          type: list; minimum two items; at least one question uniquely attributable
            to this role's frame — no other role in this registry would prioritize
            that question first; uniqueness argument required before writing
          BAD:  "Is the design correct?" (unmeasurable; any role could ask this)
          GOOD: "Does the spec bound total retry attempts per operation window —
                 verifiable in the rate-limit acceptance criteria?"

  [FC-5]  lens.simplify_rules
          EXACT IDENTIFIER: simplify_rules
          PROHIBITED IDENTIFIERS: simplify | rules | constraints | guidelines
          All prohibited identifiers break downstream consumers that read by exact key
          type: list; minimum one item; opinionated exclusion — NOT a scope description
          BAD:  "Focus on retry and budget concerns"
          GOOD: "Skip changes that do not alter retry semantics or timeout behavior;
                 flag only changes that could silently increase downstream call volume"

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
1. EXTENSION-COMMITMENT has all three elements: `field_name` = `inertia_surface`;
   `population_source` names Phase 1 and the INERTIA-SURFACE artifact; `purpose`
   names the Phase 0 diagnostic question it answers
2. FIELD-CONTRACT is written with all ten items [FC-1] through [FC-10]
3. [FC-1] contains the PROHIBITED NAMES clause naming at least "domain-expert" and
   "expert-1" explicitly as anti-patterns
4. [FC-4] and [FC-5] display exact identifier strings `verify_questions` and
   `simplify_rules` under EXACT IDENTIFIER labels — both appear verbatim

---

PHASE 1 — INERTIA SURFACE

Read `{topic}` context. Write an INERTIA-SURFACE block:

```
INERTIA-SURFACE for {topic}:

  Status-quo claim: [the strongest argument that {topic} is unnecessary — grounded
    in the actual context; name the specific existing capability relied upon]

  Challenge questions (at minimum three; specific to `{topic}` context):
    1. What specific failure does the status quo produce that this feature resolves?
       (Name the failure as found in context; if unspecified, flag as a spec gap.)
    2. [domain-specific: what does the existing mechanism already handle?]
    3. [domain-specific: what is the minimum status-quo fix, and why is it insufficient?]
```

Do not name domain experts in Phase 1.
The status-quo claim will be copied verbatim to `inertia_surface` in Phase 6.

**GATE** — Phase 1 complete when ALL of the following are TRUE:
1. INERTIA-SURFACE block is written
2. Status-quo claim explicitly names a specific existing capability (not generic)
3. At least three challenge questions use vocabulary from the `{topic}` context
4. No domain expert names appear in this block

---

PHASE 2 — DOMAIN ANALYSIS

Read `{topic}` context for concerns the Phase 1 status-quo claim does not address.

DO NOT name derived experts with placeholder labels. The following names are
PROHIBITED by [FC-1]: "domain-expert", "expert-1", "generic-expert", "role-1".
The name must come from the domain vocabulary in the concerns list.
A name that would apply to any product violates [FC-1].

```
DOMAIN-ANALYSIS for {topic}:

  Domain concerns (at minimum three; each names a gap the Phase 1 status-quo claim misses):
    1. [concern: specific failure mode in this domain not covered by the status-quo claim]
    2. [concern]
    3. [concern]

  Domain experts derived from concerns:
    - Expert name: [slug per [FC-1] — PROHIBITED: "domain-expert", "expert-1"]
      Concern link: [which concern above, by number]
      Domain-vocabulary frame: [per [FC-2] — epistemic viewpoint using concern vocabulary]
      Verify focus: [what artifact or behavior this expert checks first]
    (repeat for each derived expert — at minimum one)
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 2.

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. DOMAIN-ANALYSIS block written with populated Domain concerns list
2. At least three domain concerns use vocabulary specific to `{topic}`
3. Each derived expert entry lists all four attributes: name, concern link,
   domain-vocabulary frame, verify focus — checked per expert, not as a count
4. No derived expert name is a placeholder per [FC-1] PROHIBITED NAMES clause
5. No stock role names appear in this block

---

PHASE 3 — STOCK ROLES

```
STOCK-ROLES:
  - pm               (product value and user outcome lens)
  - architect        (technical structure and system boundary lens)
  - strategy         (business model and competitive position lens)
  - inertia-advocate (status-quo challenge lens — orientation.frame anchored to Phase 1
                      status-quo claim; verify_questions sourced from Phase 1 challenge
                      questions; collaborates_with includes at minimum one domain expert)
```

**GATE** — Phase 3 complete when ALL of the following are TRUE:
1. STOCK-ROLES lists all four names with lens descriptors
2. inertia-advocate identifies Phase 1 as source for frame and verify_questions
3. Phase 1 INERTIA-SURFACE confirmed available as source

---

PHASE 4 — OUTPUT AREA

```
OUTPUT-AREA: .roles/{area}/
```

Area slug must use domain vocabulary from Phase 2. NOT: `default`, `generic`, `roles`.

**GATE** — Phase 4 complete when ALL of the following are TRUE:
1. OUTPUT-AREA written with area slug
2. Area slug uses Phase 2 domain vocabulary
3. Path format is exactly `.roles/{area}/`

---

PHASE 5 — DIAGNOSIS CARDS AND ROLE FILE WRITING

**PREPARE:** Confirm the following inputs before writing any Diagnosis Card:
- Phase 0 [FC-4] exact identifier: `verify_questions` (retrieve verbatim from [FC-4])
- Phase 0 [FC-5] exact identifier: `simplify_rules` (retrieve verbatim from [FC-5])
- Phase 1 INERTIA-SURFACE: status-quo claim and challenge questions
- Phase 2 DOMAIN-ANALYSIS: expert names, concern links, frames, verify focuses
- Phase 3 STOCK-ROLES: all four names confirmed
- Phase 4 OUTPUT-AREA path confirmed

PREPARE complete when all six inputs are confirmed available. Do not begin Diagnosis Cards
until confirmed.

**DIAGNOSIS CARDS:** Before writing any YAML file, write one Diagnosis Card per role:

```
DIAGNOSIS-CARD for {role-name}:

  name: {proposed slug}
  [FC-1] name check: this name is domain-specific because [vocabulary source in context];
    it is NOT "domain-expert", "expert-1", or any placeholder — confirmed

  frame (one sentence): {epistemic viewpoint — "sees X through the lens of Y"}
  serves (one sentence): {beneficiary — NOT a restatement of frame}

  primary_verify_question: {the most role-specific question for this frame}
  uniqueness argument: this question is uniquely attributable to this role because no other
    role in this registry would prioritize it first — the closest overlap is [role-name],
    which would ask [different angle] — confirmed distinct

  collaborates_with draft: [{name-1}, {name-2}]
  phantom check: confirm each name above appears in this registry — confirmed
```

After all Diagnosis Cards are written, run a CROSS-CARD UNIQUENESS SCAN:

```
CROSS-CARD UNIQUENESS SCAN:
  For each pair of roles, confirm their primary_verify_questions address different
  facets. Flag any pair where both questions could be asked by the same role type.
  Revise flagged questions before proceeding to YAML writing.
```

**WRITE:** One `.md` file per role to `.roles/{area}/`. Domain experts first
(Phase 2), stock roles second (Phase 3). Apply the FIELD CONTRACT to each file:

```yaml
---
name: {per Diagnosis Card — confirmed against [FC-1]}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Per [FC-2] and Diagnosis Card frame.
    FAILURE MODE: task-list frame.}

  serves: |
    {Per [FC-3] and Diagnosis Card serves — not a frame restatement.
    FAILURE MODE: frame restatement.}

lens:
  verify_questions:
    - "{Primary verify question from Diagnosis Card — uniqueness confirmed}"
    - "{Additional question per [FC-4] — uniquely attributable to this role's frame}"

  simplify_rules:
    - "{Per [FC-5]: opinionated exclusion — 'Skip X unless Y.'}"

expertise:
  depth: {per [FC-6]: expert | practitioner | senior | principal}
  relevance: |
    {Per [FC-7]: domain-specific justification.}

scope:
  primary: |
    {Per [FC-8]: one sentence.}
  boundary: |
    {Per [FC-9]: explicit exclusion, one sentence.}

collaborates_with:
  - {per Diagnosis Card collaborates_with draft — phantom check confirmed}
  # CONTRACT VIOLATION (type 1) — PHANTOM: a role name absent from this registry.
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent.
```

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. One Diagnosis Card exists per role — all cards written before any YAML file
2. CROSS-CARD UNIQUENESS SCAN was run and any flagged pairs were revised
3. One `.md` file exists per role at `.roles/{area}/`
4. Every file uses exact identifiers `verify_questions` and `simplify_rules` —
   both appear verbatim as YAML keys
5. No role file uses a prohibited name per [FC-1]: "domain-expert", "expert-1",
   "generic-expert" fail this gate item
6. Inertia-advocate: frame anchors to Phase 1 status-quo claim; verify_questions
   sourced from Phase 1 challenge questions
7. No `collaborates_with` entries contain CONTRACT VIOLATION type-1 or type-2

---

PHASE 6 — REGISTRY SUMMARY

**PREPARE:** Before writing `REGISTRY.md`, enumerate the `.md` files written in Phase 5.
Record this count as `PHASE5_COUNT`. This count must come from Phase 5 file enumeration —
NOT from combining Phase 2 expert count + Phase 3 stock role count.
Derivation from prior-phase plans without enumeration is a count-bypass failure: the
model adds numbers from earlier phases instead of confirming what was actually written.
Only a Phase 5 file enumeration produces a valid count.

PREPARE complete when `PHASE5_COUNT` is recorded from Phase 5 enumeration.

**WRITE:** `.roles/{area}/REGISTRY.md`:

```
---
area: {area}
generated: {date}
---

## Registry Summary

total_roles: {PHASE5_COUNT — from Phase 5 file enumeration; not a computed sum}

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

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.roles/{area}/REGISTRY.md`
2. `total_roles` equals `PHASE5_COUNT` from the PREPARE enumeration
3. `domain_experts` lists each derived expert with `name` and `derivation_source`
4. `inertia_surface` contains the Phase 1 status-quo claim verbatim — not paraphrased
5. No heading stubs — every field has substantive content

---

## V-03 — Phrasing Register: Failure-Mode-First Phase Openings

**axis:** phrasing-register
**hypothesis:** R6 V-01 embeds failure framing inline — after instructions, within examples,
or as parenthetical notes. This variate inverts the register: every phase opens with a
FAILURE MODES block listing the specific anti-patterns this phase is designed to prevent,
BEFORE any instructions appear. The model encounters the failure modes as the first thing
it reads in each phase, then the instructions are framed as "to prevent these failures."
The three C-31 checkpoints are restructured: the failure-mode block in Phase 0 names
placeholder names as the PHASE-0 failure; Phase 2 opens with a failure-mode block naming
placeholder derivation; Phase 5 GATE names placeholder names as a gate failure condition.
C-32 is satisfied by Phase 6 PREPARE naming "count-bypass failure" as its listed failure
mode. C-33 is satisfied by Phase 5 YAML template annotation mirroring CONTRACT VIOLATION
labels from [FC-10]. All three v7 mechanisms are thus present at their required locations
while the phrasing register is consistently failure-mode-first throughout.
Falsifiable: if failure-mode-first phrasing causes the model to over-index on failure
avoidance at the expense of producing substantive role content (roles that are
structurally correct but semantically thin), the register trade-off is negative even
though compliance improves.

---

You are running `/org-roles {topic}`.

---

PHASE 0 — FIELD CONTRACT AND EXTENSION COMMITMENT

**FAILURE MODES for Phase 0:**
- PLACEHOLDER CONTRACT: writing a FIELD CONTRACT that names field types without explicitly
  listing prohibited values — e.g., [FC-1] says "use domain vocabulary" without naming
  "domain-expert", "expert-1" as anti-patterns by name
- IDENTIFIER OMISSION: [FC-4] or [FC-5] state the field type without displaying the exact
  identifier string that downstream consumers will read — if `verify_questions` does not
  appear verbatim under an EXACT IDENTIFIER label, the contract fails
- EXTENSION STUB: writing EXTENSION-COMMITMENT with a `purpose` field that does not name
  the Phase 0 diagnostic question it answers

To prevent these failures, write the following in Phase 0:

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

```
FIELD-CONTRACT for /org-roles {topic}:

  [FC-1]  name
          type: string — domain-vocabulary slug derived from context
          PROHIBITED NAMES: "domain-expert", "expert-1", "generic-expert", "role-1"
          These are PLACEHOLDER NAMES — the Phase 0 failure this contract prevents.
          A placeholder name passes visual inspection but carries no domain signal.
          The name must come from vocabulary in the concern this role addresses.
          BAD:  "domain-expert" — placeholder; applies to any product
          GOOD: "schema-migration-safety-analyst" — derived from domain concern

  [FC-2]  orientation.frame
          type: string — epistemic viewpoint ("sees X through the lens of Y")
          FAILURE MODE: task description
          BAD:  "Responsible for ensuring proposals are reviewed"
          GOOD: "Sees every migration proposal through the lens of whether rollback
                 guarantees remain intact — looking for irreversibility gaps"

  [FC-3]  orientation.serves
          type: string — beneficiary statement; NOT a restatement of frame
          FAILURE MODE: frame restatement
          BAD:  "Ensures rollback concerns are raised in reviews"
          GOOD: "Release engineers approving the migration — they receive a rollback-
                 viability verdict before the schema change is committed"

  [FC-4]  lens.verify_questions
          EXACT IDENTIFIER: verify_questions
          PROHIBITED IDENTIFIERS: verify | questions | checks | verify_list
          All prohibited identifiers break downstream consumers that read by exact key
          type: list; minimum two items; at least one question uniquely attributable
            to this role's frame — confirm uniqueness before writing each question
          BAD:  "Is the design complete?" (any role could ask this)
          GOOD: "Does the spec provide a rollback path for each migration step —
                 verifiable by checking the migration section for ROLLBACK annotations?"

  [FC-5]  lens.simplify_rules
          EXACT IDENTIFIER: simplify_rules
          PROHIBITED IDENTIFIERS: simplify | rules | constraints | guidelines
          All prohibited identifiers break downstream consumers that read by exact key
          type: list; minimum one item; opinionated exclusion — NOT a scope summary
          BAD:  "Focus on migration safety concerns"
          GOOD: "Skip migrations that add nullable columns only; flag migrations
                 that alter types, drop columns, or change default values"

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
1. EXTENSION-COMMITMENT has all three elements: `field_name` = `inertia_surface`;
   `population_source` names Phase 1 and INERTIA-SURFACE; `purpose` names the
   Phase 0 diagnostic question
2. FIELD-CONTRACT written with all ten items [FC-1] through [FC-10]
3. [FC-1] PROHIBITED NAMES clause names at least "domain-expert" and "expert-1" by name
4. [FC-4] and [FC-5] display exact identifier strings `verify_questions` and
   `simplify_rules` under EXACT IDENTIFIER labels — both appear verbatim

---

PHASE 1 — INERTIA SURFACE

**FAILURE MODES for Phase 1:**
- GENERIC CLAIM: status-quo claim does not name a specific existing capability — says
  "the current system handles this" without naming what mechanism does so
- CONTEXT-FREE QUESTIONS: challenge questions use generic vocabulary rather than
  vocabulary from `{topic}` context — cannot be traced to the spec
- EXPERT CONTAMINATION: domain expert names appear in this block (premature derivation)

To prevent these failures, write the INERTIA-SURFACE block:

```
INERTIA-SURFACE for {topic}:

  Status-quo claim: [refined status-quo argument grounded in context — names the
    specific existing capability that makes {topic} premature, or states that no
    such capability exists and the inertia claim is "insufficient evidence of failure"]

  Challenge questions (at minimum three; each uses vocabulary from `{topic}` context):
    1. What specific failure does the status quo produce that this feature resolves?
    2. [what does the existing mechanism already handle — name it from context]
    3. [what is the minimum status-quo fix, and why is it insufficient per the spec?]
```

The status-quo claim will be copied verbatim to `inertia_surface` in Phase 6.

**GATE** — Phase 1 complete when ALL of the following are TRUE:
1. INERTIA-SURFACE block written
2. Status-quo claim names a specific existing capability (not generic)
3. At least three challenge questions use vocabulary from `{topic}` context
4. No domain expert names appear in this block

---

PHASE 2 — DOMAIN ANALYSIS

**FAILURE MODES for Phase 2:**
- PLACEHOLDER DERIVATION: domain expert is named with a placeholder per [FC-1] —
  "domain-expert", "expert-1", "generic-expert" are prohibited in this phase;
  these names are the primary Phase-2 failure this contract prevents
- ATTRIBUTE INCOMPLETENESS: a derived expert entry missing any of the four required
  attributes (name, concern link, domain-vocabulary frame, verify focus)
- STOCK CONTAMINATION: PM, Architect, Strategy, or inertia-advocate named in this block

To prevent these failures, write the DOMAIN-ANALYSIS block:

```
DOMAIN-ANALYSIS for {topic}:

  Domain concerns (at minimum three; each names a gap the Phase 1 status-quo claim misses):
    1. [concern using {topic} domain vocabulary]
    2. [concern]
    3. [concern]

  Domain experts derived from concerns:
    - Expert name: [slug per [FC-1] — domain vocabulary REQUIRED; PROHIBITED:
        "domain-expert", "expert-1", "generic-expert", "role-1" — the PLACEHOLDER
        DERIVATION failure this phase is designed to prevent]
      Concern link: [which concern above, by number]
      Domain-vocabulary frame: [per [FC-2] — epistemic viewpoint; not a task description]
      Verify focus: [what artifact or behavior this expert checks first]
    (repeat for each derived expert — at minimum one)
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 2.

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. DOMAIN-ANALYSIS block written with populated Domain concerns list
2. At least three domain concerns use vocabulary specific to `{topic}`
3. Each derived expert entry lists all four attributes — checked per expert, not as count
4. No derived expert name is a placeholder per [FC-1]: "domain-expert", "expert-1",
   "generic-expert" fail this gate item — this is the PLACEHOLDER DERIVATION failure
5. No stock role names appear in this block

---

PHASE 3 — STOCK ROLES

**FAILURE MODES for Phase 3:**
- INERTIA ANCHOR MISSING: inertia-advocate is listed without naming Phase 1 as the
  source for its frame and verify_questions

To prevent this failure, write:

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
2. inertia-advocate identifies Phase 1 as source for frame and verify_questions
3. Phase 1 INERTIA-SURFACE confirmed available as source

---

PHASE 4 — OUTPUT AREA

**FAILURE MODES for Phase 4:**
- GENERIC AREA SLUG: `default`, `generic`, `roles`, or any area slug that does not
  come from Phase 2 domain vocabulary

To prevent this failure, write:

```
OUTPUT-AREA: .roles/{area}/
```

Area slug must use domain vocabulary from Phase 2.

**GATE** — Phase 4 complete when ALL of the following are TRUE:
1. OUTPUT-AREA written with area slug from Phase 2 domain vocabulary
2. Path format is exactly `.roles/{area}/`

---

PHASE 5 — WRITE ROLE FILES

**FAILURE MODES for Phase 5:**
- IDENTIFIER VIOLATION: YAML file uses `verify` or `questions` instead of
  `verify_questions`; or uses `simplify` or `rules` instead of `simplify_rules` —
  both exact identifiers must appear verbatim as YAML keys
- PLACEHOLDER NAME IN FILE: any file's `name` field uses "domain-expert", "expert-1",
  or "generic-expert" — the same placeholder anti-pattern prohibited in [FC-1]
- TASK-LIST FRAME: `orientation.frame` is a job description ("responsible for reviewing")
  rather than an epistemic viewpoint ("sees X through the lens of Y")
- PHANTOM COLLABORATOR: `collaborates_with` lists a name not present in this registry
- UNIQUENESS FAILURE: two roles' primary verify_questions address the same facet

To prevent these failures, follow this procedure:

**PREPARE:** Confirm inputs before writing:
- Phase 0 [FC-4] exact identifier: `verify_questions` (retrieve verbatim)
- Phase 0 [FC-5] exact identifier: `simplify_rules` (retrieve verbatim)
- Phase 1 INERTIA-SURFACE: status-quo claim and challenge questions confirmed
- Phase 2 DOMAIN-ANALYSIS: expert names, frames, verify focuses confirmed
- Phase 3 STOCK-ROLES: four names confirmed
- Phase 4 OUTPUT-AREA path confirmed

**WRITE:** One `.md` file per role to `.roles/{area}/`. Domain experts first,
stock roles second. For each file:

```yaml
---
name: {per [FC-1]: domain-vocabulary slug; PROHIBITED: "domain-expert", "expert-1"}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Per [FC-2]: epistemic viewpoint — "sees X through the lens of Y."
    FAILURE MODE: task-list frame — "responsible for reviewing" is NOT an epistemic viewpoint.}

  serves: |
    {Per [FC-3]: beneficiary — NOT a restatement of frame.
    FAILURE MODE: frame restatement.}

lens:
  verify_questions:
    - "{Per [FC-4]: actionable; uniquely attributable to this role's frame}"
    - "{Per [FC-4]: before writing, confirm no other role would prioritize this first}"

  simplify_rules:
    - "{Per [FC-5]: opinionated exclusion — 'Skip X unless Y.'
       FAILURE MODE: scope description — 'focus on X' is not an exclusion rule.}"

expertise:
  depth: {per [FC-6]: expert | practitioner | senior | principal}
  relevance: |
    {Per [FC-7]: domain-specific justification.}

scope:
  primary: |
    {Per [FC-8]: one sentence.}
  boundary: |
    {Per [FC-9]: explicit exclusion, one sentence.}

collaborates_with:
  - {per [FC-10]: registry members only}
  # CONTRACT VIOLATION (type 1) — PHANTOM: a role name absent from this registry.
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent.
```

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. One `.md` file exists per role at `.roles/{area}/`
2. Every file uses exact identifiers `verify_questions` and `simplify_rules` —
   both appear verbatim as YAML keys; any contracted form fails this gate item
3. No role file uses a PLACEHOLDER NAME: "domain-expert", "expert-1", "generic-expert"
   fail this gate item — the PLACEHOLDER NAME IN FILE failure defined above
4. Inertia-advocate: frame anchors to Phase 1 status-quo claim; verify_questions
   sourced from Phase 1 INERTIA-SURFACE challenge questions
5. Each role has at least one verify_questions entry uniquely attributable to its frame
6. No `collaborates_with` entries are PHANTOM or UNIVERSALIST per [FC-10]

---

PHASE 6 — REGISTRY SUMMARY

**FAILURE MODES for Phase 6:**
- COUNT-BYPASS FAILURE: `total_roles` is computed by adding Phase-2 expert count and
  Phase-3 stock role count rather than by enumerating Phase 5 files — this is the
  count-bypass failure; it produces a planned count, not an actual count
- HEADING STUB: any field in REGISTRY.md has only a header with no substantive content

To prevent these failures:

**PREPARE:** Enumerate the `.md` files written in Phase 5. Record this count as
`PHASE5_COUNT`. This count must come from Phase 5 file enumeration.
COUNT-BYPASS FAILURE: deriving total_roles from prior-phase plan counts instead of
Phase 5 enumeration is the failure this PREPARE step is designed to prevent.

PREPARE complete when `PHASE5_COUNT` is recorded from Phase 5 enumeration.

**WRITE:** `.roles/{area}/REGISTRY.md`:

```
---
area: {area}
generated: {date}
---

## Registry Summary

total_roles: {PHASE5_COUNT — Phase 5 file enumeration; not a computed sum}

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
  {Phase 2 concerns not addressed by any derived expert; or "none detected."}

inertia_surface: |
  {Phase 1 status-quo claim verbatim — exact sentence from INERTIA-SURFACE block.
  Do not paraphrase. This fulfills the EXTENSION-COMMITMENT made in Phase 0.}

Generated by: /org-roles {topic} — {date}
```

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.roles/{area}/REGISTRY.md`
2. `total_roles` equals `PHASE5_COUNT` from Phase 5 file enumeration
3. `domain_experts` lists each derived expert with `name` and `derivation_source`
4. `inertia_surface` contains Phase 1 status-quo claim verbatim — not paraphrased
5. No heading stubs — every field has substantive content

---

## V-04 — Role Sequence + Output Format: Context-First Inertia + Diagnosis Cards

**axis:** role-sequence + output-format
**hypothesis:** V-01 derived inertia from context first (rather than cold), making inertia
a structural constraint for all subsequent derivation. V-02 added Diagnosis Cards as an
intermediate step before YAML writing, forcing explicit uniqueness arguments. This combined
variation applies both: inertia-advocate is derived first in Phase 1 from context (not cold),
domain experts are derived explicitly to challenge the inertia claim, and then Diagnosis
Cards are written for all roles (inertia-advocate card first) before any YAML is written.
The inertia-advocate Diagnosis Card is the first card written, making its frame visible to
all subsequent card authors — the model sees the inertia frame while writing each domain
expert's uniqueness argument, which should produce verify_questions that are more directly
adversarial to the inertia position. C-31 checkpoints: [FC-1] PROHIBITED NAMES, Phase 2
DO NOT instruction (PROHIBITED by [FC-1] named explicitly), Phase 5 GATE item. C-32: Phase 6
PREPARE names count-bypass failure. C-33: Phase 5 YAML template annotation mirrors
CONTRACT VIOLATION (type 1) — PHANTOM and (type 2) — UNIVERSALIST from [FC-10].
Falsifiable: if Diagnosis Cards are written quickly as stubs and the inertia-advocate card
does not constrain subsequent domain expert cards (because the model writes all cards
independently), the combined structural benefit is not realized.

---

You are running `/org-roles {topic}`.

---

PHASE 0 — FIELD CONTRACT AND EXTENSION COMMITMENT

Before reading any context, establish the binding field specifications and registry extension.

**EXTENSION-COMMITMENT:**

```
EXTENSION-COMMITMENT:
  field_name: inertia_surface
  population_source: Phase 1, INERTIA-DERIVATION block, status-quo claim field
  purpose: answers the Phase 0 diagnostic question — "what is the strongest argument
    that the status quo is sufficient for {topic}?" — giving downstream consumers
    the exact design tension this registry was composed to test
```

**FIELD CONTRACT:**

```
FIELD-CONTRACT for /org-roles {topic}:

  [FC-1]  name
          type: string — domain-vocabulary slug derived from context
          PROHIBITED NAMES: "domain-expert", "expert-1", "generic-expert", "role-1"
          These placeholder names carry no domain signal and violate this contract.
          The name must derive from the vocabulary in the concern it addresses.
          BAD:  "domain-expert" — placeholder; no domain content
          GOOD: "circuit-breaker-state-auditor" — derived from a specific concern

  [FC-2]  orientation.frame
          type: string — epistemic viewpoint ("sees X through the lens of Y")
          FAILURE MODE: task description
          BAD:  "Responsible for reviewing circuit breaker behavior"
          GOOD: "Sees every state-transition proposal through the lens of whether
                 half-open recovery assumptions hold under sustained error load"

  [FC-3]  orientation.serves
          type: string — beneficiary statement; NOT a restatement of frame
          FAILURE MODE: frame restatement
          BAD:  "Ensures circuit breaker recovery is challenged"
          GOOD: "SRE on-call leads deciding whether to ship — they receive a
                 recovery-assumption verdict before the change reaches production"

  [FC-4]  lens.verify_questions
          EXACT IDENTIFIER: verify_questions
          PROHIBITED IDENTIFIERS: verify | questions | checks | verify_list
          All prohibited identifiers break downstream consumers that read by exact key
          type: list; minimum two items; at least one question uniquely attributable
            to this role's frame; uniqueness argument required before writing
          BAD:  "Does the design handle edge cases?" (any role could ask this)
          GOOD: "Does the spec bound the half-open probe rate under sustained
                 error load — verifiable in the circuit breaker acceptance criteria?"

  [FC-5]  lens.simplify_rules
          EXACT IDENTIFIER: simplify_rules
          PROHIBITED IDENTIFIERS: simplify | rules | constraints | guidelines
          All prohibited identifiers break downstream consumers that read by exact key
          type: list; minimum one item; opinionated exclusion — NOT a scope description
          BAD:  "Focus on circuit breaker state concerns"
          GOOD: "Skip state changes that leave the CLOSED→OPEN threshold unchanged;
                 flag only changes that alter error count windows or probe intervals"

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
1. EXTENSION-COMMITMENT has all three elements: `field_name` = `inertia_surface`;
   `population_source` names Phase 1 and INERTIA-DERIVATION; `purpose` names the
   Phase 0 diagnostic question it answers
2. FIELD-CONTRACT written with all ten items [FC-1] through [FC-10]
3. [FC-1] PROHIBITED NAMES clause names "domain-expert" and "expert-1" explicitly
4. [FC-4] and [FC-5] display exact identifier strings `verify_questions` and
   `simplify_rules` under EXACT IDENTIFIER labels — both appear verbatim

---

PHASE 1 — INERTIA DERIVATION (context read; inertia-advocate derived first)

Read `{topic}` context. Your goal is to derive the inertia-advocate first. Write:

```
INERTIA-DERIVATION for {topic}:

  Status-quo claim: [the strongest argument that {topic} is unnecessary — grounded
    in the actual context you just read; name the specific existing capability relied upon]

  Inertia-advocate profile:
    name: [domain-vocabulary slug per [FC-1] — PROHIBITED: "domain-expert", "expert-1"]
    frame: [epistemic viewpoint anchored to the status-quo claim — per [FC-2]]
    serves: [beneficiary of the inertia verdict — per [FC-3]; not a frame restatement]
    primary_verify_question: [strongest adversarial question against {topic}'s necessity]

  Challenge questions for domain experts (at minimum three; specific to `{topic}`):
    1. What existing mechanism does the status-quo claim rely on?
    2. [What specific scenario does that mechanism fail to cover?]
    3. [What minimum status-quo fix would make {topic} unnecessary?]
```

Do not name domain experts in Phase 1.
The status-quo claim will be copied verbatim to `inertia_surface` in Phase 6.

**GATE** — Phase 1 complete when ALL of the following are TRUE:
1. INERTIA-DERIVATION block written
2. Status-quo claim names a specific existing capability (not generic)
3. Inertia-advocate profile has all four attributes: name, frame, serves,
   primary_verify_question — all four present and substantive
4. Inertia-advocate name passes [FC-1]: not a prohibited placeholder
5. Three challenge questions use vocabulary from `{topic}` context
6. No domain expert names appear in this block

---

PHASE 2 — DOMAIN ANALYSIS (experts derived to challenge Phase 1 inertia claim)

Read `{topic}` context. Derive domain experts specifically to challenge the Phase 1 claim.

DO NOT name derived experts with placeholder labels. The following names are
PROHIBITED by [FC-1]: "domain-expert", "expert-1", "generic-expert", "role-1".
Every derived expert name must come from vocabulary specific to {topic}'s concern space.

```
DOMAIN-ANALYSIS for {topic}:

  Inertia claim under challenge: [restate Phase 1 status-quo claim in one sentence]

  Domain concerns (at minimum three; each names a gap the inertia claim overlooks):
    1. [concern: specific failure mode not visible to the Phase 1 inertia claim]
    2. [concern]
    3. [concern]

  Domain experts derived from concerns:
    - Expert name: [slug per [FC-1] — PROHIBITED: "domain-expert", "expert-1",
        "generic-expert" per Phase 0 [FC-1] PROHIBITED NAMES clause]
      Concern link: [which concern above, by number]
      Inertia gap: [what the Phase 1 inertia-advocate cannot see from its frame]
      Domain-vocabulary frame: [per [FC-2] — epistemic viewpoint using concern vocabulary]
      Verify focus: [first artifact or behavior this expert checks]
    (repeat — at minimum one expert)
```

Do not name pm, architect, strategy in Phase 2.

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. DOMAIN-ANALYSIS block written with Domain concerns list
2. At least three concerns use vocabulary specific to `{topic}`
3. Each expert entry lists all five attributes: name, concern link, inertia gap,
   domain-vocabulary frame, verify focus — checked per expert
4. No expert name is a placeholder per [FC-1] PROHIBITED NAMES clause
5. No stock role names appear in this block

---

PHASE 3 — STOCK ROLES (PM, Architect, Strategy; inertia-advocate from Phase 1)

```
STOCK-ROLES:
  - pm               (product value and user outcome lens)
  - architect        (technical structure and system boundary lens)
  - strategy         (business model and competitive position lens)
  NOTE: inertia-advocate derived in Phase 1; it is a registry member; written in
  Phase 5 from Phase 1 INERTIA-DERIVATION profile; not re-listed here
```

**GATE** — Phase 3 complete when ALL of the following are TRUE:
1. STOCK-ROLES lists three names (pm, architect, strategy) with lens descriptors
2. inertia-advocate noted as derived in Phase 1
3. Phase 1 INERTIA-DERIVATION confirmed available as source

---

PHASE 4 — OUTPUT AREA

```
OUTPUT-AREA: .roles/{area}/
```

Area slug from Phase 2 domain vocabulary. NOT: `default`, `generic`, `roles`.

**GATE:** OUTPUT-AREA written; area slug from Phase 2; path format is `.roles/{area}/`

---

PHASE 5 — DIAGNOSIS CARDS AND ROLE FILE WRITING

**PREPARE:** Confirm before writing any Diagnosis Card:
- Phase 0 [FC-4] exact identifier: `verify_questions` (verbatim)
- Phase 0 [FC-5] exact identifier: `simplify_rules` (verbatim)
- Phase 1 INERTIA-DERIVATION: inertia-advocate profile and challenge questions
- Phase 2 DOMAIN-ANALYSIS: expert names, concern links, inertia gaps, frames
- Phase 3 STOCK-ROLES: three names confirmed
- Phase 4 OUTPUT-AREA confirmed

**DIAGNOSIS CARDS:** Write inertia-advocate card first, then domain expert cards,
then stock role cards. Each card must be written before any YAML file for that role.

```
DIAGNOSIS-CARD for {role-name}:

  name: {proposed slug}
  [FC-1] check: not "domain-expert", "expert-1", or any placeholder — confirmed;
    name is domain-specific because: [vocabulary source from context]

  frame: {one-sentence epistemic viewpoint — "sees X through the lens of Y"}
  serves: {one-sentence beneficiary — NOT a frame restatement}

  primary_verify_question: {most role-specific question}
  uniqueness argument: no other role in this registry would prioritize this question
    first — closest overlap is [role-name], which would ask [different angle] — confirmed

  inertia relationship: [for domain experts: how this role's primary concern challenges
    the Phase 1 inertia claim; for stock roles: which aspect of inertia claim this role
    complements or extends]

  collaborates_with draft: [{name-1}, {name-2}]
  phantom check: each name above is in this registry — confirmed
```

After all cards: run CROSS-CARD UNIQUENESS SCAN — check each pair's primary_verify_question
for overlap; revise any pair where both questions could be asked by the same role type.

**WRITE:** One `.md` file per role from its Diagnosis Card. Inertia-advocate first:

```yaml
---
name: {from Diagnosis Card — confirmed against [FC-1]}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Per [FC-2] and Diagnosis Card frame.
    FAILURE MODE: task-list frame.}

  serves: |
    {Per [FC-3] and Diagnosis Card serves.
    FAILURE MODE: frame restatement.}

lens:
  verify_questions:
    - "{Primary question from Diagnosis Card — uniqueness confirmed}"
    - "{Additional per [FC-4] — uniquely attributable}"

  simplify_rules:
    - "{Per [FC-5]: opinionated exclusion — 'Skip X unless Y.'}"

expertise:
  depth: {per [FC-6]: expert | practitioner | senior | principal}
  relevance: |
    {Per [FC-7]: domain-specific justification.}

scope:
  primary: |
    {Per [FC-8]: one sentence.}
  boundary: |
    {Per [FC-9]: explicit exclusion, one sentence.}

collaborates_with:
  - {per Diagnosis Card — phantom check confirmed}
  # CONTRACT VIOLATION (type 1) — PHANTOM: a role name absent from this registry.
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent.
```

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. One Diagnosis Card per role, written before its YAML file
2. CROSS-CARD UNIQUENESS SCAN run; flagged pairs revised
3. One `.md` file per role at `.roles/{area}/`
4. Every file uses `verify_questions` and `simplify_rules` verbatim as YAML keys
5. No role file uses a prohibited name: "domain-expert", "expert-1", "generic-expert"
6. Inertia-advocate: frame from Phase 1 INERTIA-DERIVATION; verify_questions include
   Phase 1 primary_verify_question
7. No `collaborates_with` entries contain CONTRACT VIOLATION type-1 or type-2

---

PHASE 6 — REGISTRY SUMMARY

**PREPARE:** Enumerate `.md` files written in Phase 5. Record as `PHASE5_COUNT`.
This count must come from Phase 5 file enumeration — NOT from adding Phase 1
inertia-advocate (1) + Phase 2 expert count + Phase 3 stock roles (3).
Derivation from prior-phase plans without enumeration is a count-bypass failure:
planning counts are not the same as written-file counts.

PREPARE complete when `PHASE5_COUNT` is recorded from Phase 5 enumeration.

**WRITE:** `.roles/{area}/REGISTRY.md`:

```
---
area: {area}
generated: {date}
---

## Registry Summary

total_roles: {PHASE5_COUNT — from Phase 5 file enumeration; not a computed sum}

stock_roles:
  - inertia-advocate  (Phase 1 derivation)
  - pm
  - architect
  - strategy

domain_experts:
  - name: {expert-name}
    derivation_source: Phase 2 domain concern #[N]
    inertia_gap: {gap in Phase 1 claim this expert addresses}
  (one entry per derived expert)

coverage_gaps: |
  {Phase 2 concerns not addressed by any expert; or "none detected."}

inertia_surface: |
  {Phase 1 status-quo claim verbatim — exact sentence from INERTIA-DERIVATION block.
  Do not paraphrase. This fulfills the EXTENSION-COMMITMENT made in Phase 0.}

Generated by: /org-roles {topic} — {date}
```

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.roles/{area}/REGISTRY.md`
2. `total_roles` equals `PHASE5_COUNT` from Phase 5 file enumeration
3. `domain_experts` lists each expert with `name`, `derivation_source`, `inertia_gap`
4. `inertia_surface` contains Phase 1 status-quo claim verbatim
5. No heading stubs — every field has substantive content

---

## V-05 — All Axes: Cold Hypothesis + Diagnosis Cards + Failure-Mode-First + Explicit C-31 Site Labels

**axis:** all axes combined
**hypothesis:** R6 V-01 hit 100.00 under v7. This variation builds on that base and adds
three structural elements from V-02, V-03, and a new element — explicit C-31 site labels.
(1) Cold hypothesis from R6 V-01: Phase 0 asks for a COLD-HYPOTHESIS before any context
is loaded; this is the design tension the registry tests. (2) Diagnosis Cards from V-02:
intermediate step before YAML writing forces explicit uniqueness arguments. (3) Failure-
mode-first phase openings from V-03: each phase opens with its specific failure modes.
(4) New: explicit C-31 site labels. The three placeholder-name prohibition checkpoints
are labeled "C-31-SITE-1", "C-31-SITE-2", "C-31-SITE-3" directly in the prompt — making
the three-site structure self-documenting. The model sees the count explicitly (three sites)
rather than inferring it from distribution across phases. C-32 is satisfied by Phase 6
PREPARE naming count-bypass failure as a named class. C-33 is satisfied by Phase 5 template
annotation mirroring CONTRACT VIOLATION (type 1) — PHANTOM and (type 2) — UNIVERSALIST
from [FC-10]. Target: 100.00 under v7 by redundancy, self-documentation, and synthesis.
Falsifiable: if explicit C-31 site labels ("C-31-SITE-1", "C-31-SITE-2", "C-31-SITE-3")
cause the model to treat the sites as checkboxes to fill rather than enforcement mechanisms
(writing the label but not the prohibited names within it), explicit labeling degrades
compliance relative to implicit three-point distribution.

---

You are running `/org-roles {topic}`.

---

PHASE 0 — DIAGNOSTIC DECLARATION AND FIELD CONTRACT

**FAILURE MODES for Phase 0:**
- COLD HYPOTHESIS OMISSION: proceeding to FIELD CONTRACT without writing the cold
  hypothesis — the status-quo design tension is not established before context loading
- PLACEHOLDER CONTRACT (C-31-SITE-1 FAILURE): [FC-1] does not explicitly name
  "domain-expert" and "expert-1" as prohibited values — a type constraint without
  named anti-patterns does not satisfy the three-checkpoint prohibition requirement
- IDENTIFIER OMISSION: `verify_questions` or `simplify_rules` absent from [FC-4]/[FC-5]

**Opening diagnostic:** What is the strongest argument that the status quo is sufficient —
that `{topic}` is not worth building?

Answer this question COLD — before reading any context. Write a one-sentence COLD HYPOTHESIS:

```
COLD-HYPOTHESIS: [The existing approach already ___; therefore `{topic}` is premature /
  redundant / unnecessary — stated as the most reasonable opposing argument you can
  construct without reading the spec.]
```

This is not a final verdict. It is the design tension this registry will stress-test.

After writing COLD-HYPOTHESIS, write the EXTENSION COMMITMENT and FIELD CONTRACT:

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

```
FIELD-CONTRACT for /org-roles {topic}:

  [FC-1]  name
          type: string — domain-vocabulary slug derived from context
          *** C-31-SITE-1: PROHIBITED NAMES ***
          PROHIBITED NAMES: "domain-expert", "expert-1", "generic-expert", "role-1"
          These placeholder anti-patterns appear at three enforcement checkpoints:
            Site 1 (here): field contract
            Site 2: Phase 2 derivation instruction
            Site 3: Phase 5 file-writing gate
          A name that could apply to any product violates this contract.
          BAD:  "domain-expert" — carries no domain content; prohibited at all three sites
          GOOD: "event-schema-fidelity-analyst" — specific to this domain's concern

  [FC-2]  orientation.frame
          type: string — epistemic viewpoint ("sees X through the lens of Y")
          FAILURE MODE: task description
          BAD:  "Responsible for reviewing spec and surfacing issues"
          GOOD: "Sees every schema proposal through the lens of whether consumer
                 contracts are invalidated — looking for downstream version-mismatch gaps"

  [FC-3]  orientation.serves
          type: string — beneficiary statement; NOT a restatement of frame
          FAILURE MODE: frame restatement
          BAD:  "Ensures schema changes are reviewed for contract gaps"
          GOOD: "Integration teams receiving a schema update — they get a compatibility
                 verdict before the change reaches their pipeline"

  [FC-4]  lens.verify_questions
          EXACT IDENTIFIER: verify_questions
          PROHIBITED IDENTIFIERS: verify | questions | checks | verify_list
          All prohibited identifiers break downstream consumers that read by exact key
          type: list; minimum two items; at least one question uniquely attributable
            to this role's frame — confirm uniqueness before writing each question
          BAD:  "Is the design correct?" (any role could ask this)
          GOOD: "Does the spec identify the consumer contract version that this schema
                 change invalidates — verifiable in the breaking-change section?"

  [FC-5]  lens.simplify_rules
          EXACT IDENTIFIER: simplify_rules
          PROHIBITED IDENTIFIERS: simplify | rules | constraints | guidelines
          All prohibited identifiers break downstream consumers that read by exact key
          type: list; minimum one item; opinionated exclusion — NOT a scope description
          BAD:  "Focus on consumer contract concerns"
          GOOD: "Skip additive schema changes that preserve all existing consumer
                 contracts; flag only changes that remove, rename, or retype fields"

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
   `population_source` names Phase 1 and INERTIA-SURFACE; `purpose` names the Phase 0
   diagnostic question
3. FIELD-CONTRACT written with all ten items [FC-1] through [FC-10]
4. [FC-1] C-31-SITE-1 contains PROHIBITED NAMES naming "domain-expert" and "expert-1"
   and references the three-site enforcement structure
5. [FC-4] and [FC-5] display `verify_questions` and `simplify_rules` verbatim under
   EXACT IDENTIFIER labels

---

PHASE 1 — INERTIA REFINEMENT

**FAILURE MODES for Phase 1:**
- GENERIC CLAIM: status-quo claim does not name a specific existing capability
- COLD HYPOTHESIS DISCONNECT: status-quo claim does not reference Phase 0 COLD-HYPOTHESIS
- EXPERT CONTAMINATION: domain expert names appear in this block

Read `{topic}` context. Find whether the existing system has the capability claimed in
the COLD-HYPOTHESIS. Write an INERTIA-SURFACE block:

```
INERTIA-SURFACE for {topic}:

  Status-quo claim: [refined version of Phase 0 COLD-HYPOTHESIS, grounded in actual
    context — confirmed ("the spec confirms the existing system already handles X,
    making the proposed feature redundant unless Y is demonstrated") or revised
    ("the cold hypothesis was incorrect; the actual status-quo argument is ___")]

  Challenge questions (at minimum three; specific to `{topic}` context):
    1. What specific failure does the status quo produce that this feature resolves?
       (Name the failure as found in context; if unspecified, flag as a spec gap.)
    2. [domain-specific: what does the existing mechanism already handle?]
    3. [domain-specific: what is the minimum status-quo fix, and why is it insufficient?]
```

Do not name domain experts in Phase 1.
The status-quo claim will be copied verbatim to `inertia_surface` in Phase 6.

**GATE** — Phase 1 complete when ALL of the following are TRUE:
1. INERTIA-SURFACE block written
2. Status-quo claim names a specific existing capability (not generic)
3. Status-quo claim references Phase 0 COLD-HYPOTHESIS (confirmed or revised)
4. At least three challenge questions use vocabulary from `{topic}` context
5. No domain expert names appear in this block

---

PHASE 2 — DOMAIN ANALYSIS

**FAILURE MODES for Phase 2:**
- C-31-SITE-2 FAILURE — PLACEHOLDER DERIVATION: deriving an expert with name
  "domain-expert", "expert-1", "generic-expert", or "role-1" — the exact names prohibited
  at C-31-SITE-1 ([FC-1]) and enforced again here; a name is only valid if it comes from
  vocabulary specific to `{topic}`'s concern space
- ATTRIBUTE INCOMPLETENESS: any derived expert entry missing name, concern link,
  domain-vocabulary frame, or verify focus
- STOCK CONTAMINATION: pm, architect, strategy, or inertia-advocate named here

Read `{topic}` context for concerns the Phase 1 status-quo claim does not address.

```
DOMAIN-ANALYSIS for {topic}:

  Domain concerns (at minimum three; each names a gap the Phase 1 status-quo claim misses):
    1. [concern using {topic} domain vocabulary]
    2. [concern]
    3. [concern]

  Domain experts derived from concerns:
    - Expert name: [slug per [FC-1] — domain vocabulary REQUIRED;
        *** C-31-SITE-2: PROHIBITED: "domain-expert", "expert-1", "generic-expert",
        "role-1" — the same names prohibited at C-31-SITE-1 in [FC-1] ***]
      Concern link: [which concern above, by number]
      Domain-vocabulary frame: [per [FC-2] — epistemic viewpoint; not a task description]
      Verify focus: [artifact or behavior this expert checks first]
    (repeat for each derived expert — at minimum one)
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 2.

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. DOMAIN-ANALYSIS block written
2. At least three domain concerns use vocabulary specific to `{topic}`
3. Each derived expert entry lists all four attributes — checked per expert, not count
4. No expert name violates [FC-1] C-31-SITE-2 prohibition — "domain-expert",
   "expert-1", "generic-expert" fail this gate item
5. No stock role names appear in this block

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
1. STOCK-ROLES lists all four names
2. inertia-advocate identifies Phase 1 as source for frame and verify_questions
3. Phase 1 INERTIA-SURFACE confirmed available

---

PHASE 4 — OUTPUT AREA

```
OUTPUT-AREA: .roles/{area}/
```

Area slug from Phase 2 domain vocabulary. NOT: `default`, `generic`, `roles`.

**GATE:** OUTPUT-AREA written; area slug from Phase 2; path is `.roles/{area}/`

---

PHASE 5 — DIAGNOSIS CARDS AND ROLE FILE WRITING

**FAILURE MODES for Phase 5:**
- C-31-SITE-3 FAILURE — PLACEHOLDER NAME IN FILE: any written `.md` file's `name` field
  is "domain-expert", "expert-1", or "generic-expert" — the same names prohibited at
  C-31-SITE-1 ([FC-1]) and C-31-SITE-2 (Phase 2 instruction); Site-3 is the final
  enforcement point; a file written with a prohibited name fails this gate
- IDENTIFIER VIOLATION: YAML key `verify` instead of `verify_questions`, or
  `simplify` instead of `simplify_rules`
- UNIQUENESS FAILURE: two roles share a primary verify_question facet

**PREPARE:** Confirm before writing any Diagnosis Card:
- Phase 0 [FC-4] exact identifier: `verify_questions` (verbatim from [FC-4])
- Phase 0 [FC-5] exact identifier: `simplify_rules` (verbatim from [FC-5])
- Phase 1 INERTIA-SURFACE: status-quo claim and challenge questions confirmed
- Phase 2 DOMAIN-ANALYSIS: expert names, concern links, frames, verify focuses confirmed
- Phase 3 STOCK-ROLES: four names confirmed
- Phase 4 OUTPUT-AREA confirmed

**DIAGNOSIS CARDS:** Write one Diagnosis Card per role before any YAML file:

```
DIAGNOSIS-CARD for {role-name}:

  name: {proposed slug}
  C-31-SITE-3 pre-check: name is NOT "domain-expert", "expert-1", "generic-expert" —
    confirmed; name derives from {vocabulary source} in `{topic}` context

  frame: {epistemic viewpoint — "sees X through the lens of Y"}
  serves: {beneficiary — not a frame restatement}

  primary_verify_question: {most role-specific question for this frame}
  uniqueness argument: no other role in this registry would prioritize this question
    first — closest potential overlap is [{role-name}], which would ask [{different angle}]
    — confirmed distinct

  collaborates_with draft: [{name-1}, {name-2}]
  phantom check: each name above is in this registry — confirmed
```

After all cards: run CROSS-CARD UNIQUENESS SCAN. Revise flagged pairs before writing YAML.

**WRITE:** One `.md` file per role to `.roles/{area}/`. Domain experts first,
stock roles second. Apply FIELD CONTRACT to each file:

```yaml
---
name: {from Diagnosis Card — C-31-SITE-3: not "domain-expert", "expert-1", "generic-expert"}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Per [FC-2] and Diagnosis Card frame.
    Domain experts: Phase 2 domain-vocabulary frame as anchor.
    Inertia-advocate: Phase 1 status-quo claim as epistemic stance.

    FAILURE MODE: task-list frame.
    WORKED EXAMPLE (bad):  "Responsible for reviewing proposals and surfacing gaps."
    WORKED EXAMPLE (good): "Sees every proposed change through the lens of whether
      the existing mechanism named in Phase 1 already handles the scenario."}

  serves: |
    {Per [FC-3] and Diagnosis Card serves — not a frame restatement.

    FAILURE MODE: frame restatement.
    WORKED EXAMPLE (bad):  "Ensures status-quo concerns are surfaced."
    WORKED EXAMPLE (good): "Feature teams deciding whether to proceed — they receive
      a verdict on which existing capabilities are genuinely insufficient."}

lens:
  verify_questions:
    - "{Primary verify question from Diagnosis Card — uniqueness confirmed}"
    - "{Additional per [FC-4]: before writing, confirm no other role would prioritize
       this first — revise until uniquely attributable to this role's frame}"

  simplify_rules:
    - "{Per [FC-5]: opinionated exclusion — 'Skip X unless Y.'

       FAILURE MODE: scope description — 'focus on X concerns' is not an exclusion.
       WORKED EXAMPLE (good): 'Skip changes that preserve all existing contracts;
         flag only changes that invalidate or extend an existing contract.'}"

expertise:
  depth: {per [FC-6]: expert | practitioner | senior | principal}
  relevance: |
    {Per [FC-7]: domain-specific justification — not a role-name restatement.}

scope:
  primary: |
    {Per [FC-8]: main concern. One sentence.}
  boundary: |
    {Per [FC-9]: explicit exclusion. One sentence.}

collaborates_with:
  - {per Diagnosis Card — phantom check confirmed; registry members only}
  # CONTRACT VIOLATION (type 1) — PHANTOM: a role name absent from this registry.
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent.
```

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. One Diagnosis Card exists per role, written before its YAML file
2. CROSS-CARD UNIQUENESS SCAN run; flagged pairs revised
3. One `.md` file exists per role at `.roles/{area}/`
4. Every file uses exact identifiers `verify_questions` and `simplify_rules` as YAML keys
5. No role file uses a prohibited name per C-31-SITE-3: "domain-expert", "expert-1",
   "generic-expert" fail this gate item — three-site prohibition confirmed complete
6. Inertia-advocate: frame anchors to Phase 1 status-quo claim; verify_questions from
   Phase 1 INERTIA-SURFACE challenge questions
7. No `collaborates_with` entries contain CONTRACT VIOLATION type-1 or type-2

---

PHASE 6 — REGISTRY SUMMARY

**FAILURE MODES for Phase 6:**
- COUNT-BYPASS FAILURE: `total_roles` computed from prior-phase plan counts instead
  of Phase 5 file enumeration — this is the named failure class this PREPARE step
  prevents; planning counts are intentions, not outputs; only enumeration is valid
- HEADING STUB: any field has a header with no substantive content below it

**PREPARE:** Enumerate the `.md` files written in Phase 5. Record as `PHASE5_COUNT`.
COUNT-BYPASS FAILURE: deriving total_roles from Phase 2 expert count + Phase 3 stock
role count (4) instead of Phase 5 file enumeration is the anti-pattern this step names.
Only Phase 5 file enumeration produces a valid count.

PREPARE complete when `PHASE5_COUNT` is recorded from Phase 5 file enumeration.

**WRITE:** `.roles/{area}/REGISTRY.md`:

```
---
area: {area}
generated: {date}
---

## Registry Summary

total_roles: {PHASE5_COUNT — from Phase 5 file enumeration; not a computed sum}

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

FAILURE MODE — HEADING STUB: every field above must have substantive content.

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.roles/{area}/REGISTRY.md`
2. `total_roles` equals `PHASE5_COUNT` from Phase 5 file enumeration
3. `domain_experts` lists each derived expert with `name` and `derivation_source`
4. `inertia_surface` contains Phase 1 status-quo claim verbatim — not paraphrased;
   this validates the EXTENSION-COMMITMENT made in Phase 0
5. No heading stubs — every field has substantive content below its header
