---
skill: quest-variate
skill_target: org-roles
date: 2026-03-16
round: R8
rubric_version: v8
status: variate
---

# org-roles Variate — Round 8

**Date:** 2026-03-16
**Skill:** org-roles
**Rubric:** v8 (C-01 through C-36; new in v8: C-34 inertia-gap as fifth per-expert attribute
in derivation gate, C-35 pre-YAML Diagnosis Card with named-overlap uniqueness argument,
C-36 cross-set pre-YAML uniqueness scan gate)
**Round:** R8 — single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

---

## Round 8 Variation Map

| V | Axis | Primary C targets | Hypothesis |
|---|------|------------------|------------|
| V-01 | output-format | C-34 PASS, C-35 PASS, C-36 PASS, C-15 PASS | Merge R7 V-01's 5-attribute derivation gate (inertia gap per expert) into R7 V-02's Diagnosis Card pipeline; fix C-15 by naming heading stub as explicit FAIL condition referencing C-10; first variation to hold all four open criteria simultaneously |
| V-02 | role-sequence | C-34 PASS, C-35 PASS, C-36 PASS, C-15 PASS | Inertia-advocate's Diagnosis Card written FIRST as anchor card; domain expert cards each include an explicit "inertia card orthogonality" field showing how their primary verify question addresses a facet the inertia card cannot see; the cross-set scan treats the inertia card as the comparison axis |
| V-03 | lifecycle-emphasis | C-34 PASS, C-35 PASS, C-36 PASS, C-15 PASS | Phase 2 gains a dedicated INERTIA-GAP ANALYSIS sub-step where each domain expert's inertia gap is derived BEFORE their name is written — gap-first expert naming; Phase 5 Diagnosis Cards inherit the inertia gap from Phase 2, reducing duplication; lifecycle weight shifts toward derivation |
| V-04 | role-sequence + output-format | C-34 PASS, C-35 PASS, C-36 PASS, C-15 PASS | Combines V-01's 5-attribute format and C-15 fix with V-02's inertia-card-first Diagnosis Card sequence; the inertia card's gap analysis is the cross-set scan's reference point |
| V-05 | all axes | C-34 PASS, C-35 PASS, C-36 PASS, C-15 PASS — 100.00 target | Full synthesis: failure-mode-first phase openings (R7 V-03), context-first inertia derivation (R7 V-01), 5-attribute gate with inertia gap (V-01), Diagnosis Cards with inertia-card-first sequence (V-02), gap-first expert naming (V-03), explicit C-15 stub FAIL condition, explicit C-31-SITE labels at all three prohibition checkpoints |

---

## V-01 — Output Format: Unified Five-Attribute Derivation + Diagnosis Card Pipeline

**axis:** output-format
**hypothesis:** R7 V-01 captured C-34 (inertia gap as fifth per-expert derivation attribute)
but lacked C-35/C-36. R7 V-02 captured C-35+C-36 (Diagnosis Card + cross-set scan) but
lacked C-34. The criteria operate at different phases (Phase 2 derivation gate vs. Phase 5
pre-YAML artifacts) and are fully combinable. This variate adds the `inertia_gap` field to
the Phase 2 DOMAIN-ANALYSIS record and updates the derivation gate to check five attributes
per expert. The Diagnosis Card mechanism (C-35) and CROSS-CARD UNIQUENESS SCAN (C-36) from
R7 V-02 are preserved unchanged. C-15 is fixed from PARTIAL to PASS by adding an explicit
HEADING STUB FAIL CONDITION to Phase 6 that names the stub failure by reference to its
C-10 consequence. No other axes change — this is a pure output-format variation.
Falsifiable: if the inertia gap attribute in Phase 2 produces over-specified expert records
whose frames are constrained by inertia reasoning rather than concern reasoning, the Phase 2
output quality degrades even though the gate compliance improves.

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
      Inertia gap: [what status-quo resistance this expert's domain would name —
        the specific Phase 1 claim this expert's concern challenges or exposes as
        insufficient; name the mechanism the Phase 1 inertia-advocate relies on
        and why this expert's concern falls outside its coverage]
      Domain-vocabulary frame: [per [FC-2] — epistemic viewpoint using concern vocabulary]
      Verify focus: [what artifact or behavior this expert checks first]
    (repeat for each derived expert — at minimum one)
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 2.

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. DOMAIN-ANALYSIS block written with populated Domain concerns list
2. At least three domain concerns use vocabulary specific to `{topic}`
3. Each derived expert entry lists all five attributes individually:
   name, concern link, inertia gap, domain-vocabulary frame, verify focus —
   checked per expert, not as a total count; a single missing attribute in any
   entry fails this item
4. No derived expert name is a placeholder per [FC-1] PROHIBITED NAMES clause —
   "domain-expert", "expert-1", "generic-expert" fail this gate item
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
OUTPUT-AREA: .craft/roles/{area}/
```

Area slug must use domain vocabulary from Phase 2. NOT: `default`, `generic`, `roles`.

**GATE** — Phase 4 complete when ALL of the following are TRUE:
1. OUTPUT-AREA written with area slug
2. Area slug uses Phase 2 domain vocabulary
3. Path format is exactly `.craft/roles/{area}/`

---

PHASE 5 — DIAGNOSIS CARDS AND ROLE FILE WRITING

**PREPARE:** Confirm the following inputs before writing any Diagnosis Card:
- Phase 0 [FC-4] exact identifier: `verify_questions` (retrieve verbatim from [FC-4])
- Phase 0 [FC-5] exact identifier: `simplify_rules` (retrieve verbatim from [FC-5])
- Phase 1 INERTIA-SURFACE: status-quo claim and challenge questions
- Phase 2 DOMAIN-ANALYSIS: expert names, concern links, inertia gaps, frames, verify focuses
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

For domain expert roles, the Diagnosis Card PREPARE confirms the Phase 2 `inertia gap`
attribute is available and used to anchor the `frame`: the expert's frame should address
the gap the inertia-advocate's claim cannot cover, as identified in Phase 2.

After all Diagnosis Cards are written, run a CROSS-CARD UNIQUENESS SCAN:

```
CROSS-CARD UNIQUENESS SCAN:
  For each pair of roles, confirm their primary_verify_questions address different
  facets. Flag any pair where both questions could be asked by the same role type.
  Revise flagged questions before proceeding to YAML writing.
```

**WRITE:** One `.md` file per role to `.craft/roles/{area}/`. Domain experts first
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
3. One `.md` file exists per role at `.craft/roles/{area}/`
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

**WRITE:** `.craft/roles/{area}/REGISTRY.md`:

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
    inertia_gap: {the status-quo resistance this expert's domain names — from Phase 2
      inertia gap attribute; not a paraphrase of the expert name}
  (one entry per derived expert)

coverage_gaps: |
  {Phase 2 concerns not addressed by any derived expert; or "none detected."
  A genuine diagnostic answer — not a heading stub.}

inertia_surface: |
  {Phase 1 status-quo claim verbatim — exact sentence from INERTIA-SURFACE block.
  Do not paraphrase. This fulfills the EXTENSION-COMMITMENT made in Phase 0.}

Generated by: /org-roles {topic} — {date}
```

HEADING STUB FAIL CONDITION: A `## Registry Summary` section with no required fields
populated beneath it is not a registry and fails this step's completion gate. A heading
stub — where section headers are present but field values are empty strings, omitted, or
placeholder text — is not a partial registry; it is an explicit C-10 failure (registry
content completeness). Every field in the template above must contain substantive content.

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.craft/roles/{area}/REGISTRY.md`
2. `total_roles` equals `PHASE5_COUNT` from the PREPARE enumeration
3. `domain_experts` lists each derived expert with `name`, `derivation_source`, and `inertia_gap`
4. `inertia_surface` contains the Phase 1 status-quo claim verbatim — not paraphrased
5. No heading stubs — every field has substantive content below its header
6. HEADING STUB FAIL CONDITION was read before writing began

---

## V-02 — Role Sequence: Inertia Card Anchor in Diagnosis Pipeline

**axis:** role-sequence
**hypothesis:** R7 V-01 made the inertia-advocate the structural constraint for Phase 2
by deriving it FIRST in context, before domain experts. R7 V-02 introduced the Diagnosis
Card mechanism but wrote cards in domain-expert-first order. This variate extends the
inertia-first sequence into Phase 5: the inertia-advocate's Diagnosis Card is written
FIRST (ANCHOR-CARD), before any domain expert or stock role card. Each subsequent Diagnosis
Card includes a required "inertia card orthogonality" field confirming how its primary
verify question addresses a facet the anchor card cannot cover. The CROSS-CARD UNIQUENESS
SCAN then uses the anchor card's primary question as the comparison axis. C-34 is satisfied
by the Phase 2 gate with five per-expert attributes including inertia gap. C-35 and C-36
are satisfied by the Diagnosis Card pipeline and scan. C-15 is fixed from PARTIAL to PASS.
Falsifiable: if inertia-card-first Diagnosis Card ordering causes domain expert cards to
define their uniqueness negatively ("not what the inertia card asks") rather than
positively from their own concern, the frames become inertia-derived rather than
concern-derived, degrading expert quality even as compliance improves.

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
          BAD:  "domain-expert" (no domain content)
          GOOD: "event-schema-fidelity-analyst" (specific to this domain's concern)

  [FC-2]  orientation.frame
          type: string — epistemic viewpoint ("sees X through the lens of Y")
          FAILURE MODE: task list / job description

  [FC-3]  orientation.serves
          type: string — beneficiary statement; NOT a restatement of frame
          FAILURE MODE: frame restatement

  [FC-4]  lens.verify_questions
          EXACT IDENTIFIER: verify_questions
          PROHIBITED IDENTIFIERS: verify | questions | checks | verify_list
          All prohibited identifiers break downstream consumers that read by exact key
          type: list; minimum two items; at least one question uniquely attributable
            to this role's frame — no other role in this registry would prioritize
            that question first; uniqueness argument required before writing

  [FC-5]  lens.simplify_rules
          EXACT IDENTIFIER: simplify_rules
          PROHIBITED IDENTIFIERS: simplify | rules | constraints | guidelines
          All prohibited identifiers break downstream consumers that read by exact key
          type: list; minimum one item; opinionated exclusion — NOT a scope description

  [FC-6]  expertise.depth   — enum: expert | practitioner | senior | principal

  [FC-7]  expertise.relevance — domain-specific justification; not a role-name restatement

  [FC-8]  scope.primary     — main concern this role surfaces; one sentence

  [FC-9]  scope.boundary    — what this role does NOT own; explicit exclusion; one sentence

  [FC-10] collaborates_with
          type: list — registry members only
          CONTRACT VIOLATION (type 1) — PHANTOM: a role name absent from this registry's
            output
          CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT: `field_name` = `inertia_surface`; `population_source` names
   Phase 1 and INERTIA-SURFACE artifact; `purpose` names the Phase 0 diagnostic question
2. FIELD-CONTRACT written with all ten items [FC-1] through [FC-10]
3. [FC-1] contains PROHIBITED NAMES clause naming "domain-expert" and "expert-1"
4. [FC-4] and [FC-5] display exact identifier strings `verify_questions` and
   `simplify_rules` under EXACT IDENTIFIER labels — both appear verbatim

---

PHASE 1 — INERTIA SURFACE

Read `{topic}` context. Write an INERTIA-SURFACE block:

```
INERTIA-SURFACE for {topic}:

  Status-quo claim: [the strongest argument that {topic} is unnecessary — grounded
    in the actual context; name the specific existing capability relied upon]

  Inertia-advocate profile:
    name: [domain-vocabulary slug per [FC-1] — PROHIBITED: "domain-expert", "expert-1"]
    primary_verify_question: [the most adversarial version of "why is this necessary?"]

  Challenge questions (at minimum three; specific to `{topic}` context):
    1. What specific failure does the status quo produce that this feature resolves?
    2. [what does the existing mechanism already handle?]
    3. [what is the minimum status-quo fix, and why is it insufficient?]
```

Do not name domain experts in Phase 1.
The status-quo claim will be copied verbatim to `inertia_surface` in Phase 6.

**GATE** — Phase 1 complete when ALL of the following are TRUE:
1. INERTIA-SURFACE block is written
2. Status-quo claim names a specific existing capability (not generic)
3. Inertia-advocate profile has name and primary_verify_question
4. At least three challenge questions use vocabulary from `{topic}` context
5. No domain expert names appear in this block

---

PHASE 2 — DOMAIN ANALYSIS

Read `{topic}` context for concerns the Phase 1 status-quo claim does not address.

DO NOT name derived experts with placeholder labels. The following names are
PROHIBITED by [FC-1]: "domain-expert", "expert-1", "generic-expert", "role-1".
The name must come from the domain vocabulary in the concerns list.

```
DOMAIN-ANALYSIS for {topic}:

  Domain concerns (at minimum three; each names a gap the Phase 1 status-quo claim misses):
    1. [concern: specific failure mode not covered by the status-quo claim]
    2. [concern]
    3. [concern]

  Domain experts derived from concerns:
    - Expert name: [slug per [FC-1] — PROHIBITED: "domain-expert", "expert-1"]
      Concern link: [which concern above, by number]
      Inertia gap: [what status-quo resistance this expert's domain would name —
        the specific claim the inertia-advocate makes that this expert's concern
        falls outside; this attribute is the expert's answer to: "what does the
        inertia-advocate overlook that your domain sees?"]
      Domain-vocabulary frame: [per [FC-2] — epistemic viewpoint using concern vocabulary]
      Verify focus: [what artifact or behavior this expert checks first]
    (repeat for each derived expert — at minimum one)
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 2.

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. DOMAIN-ANALYSIS block written with populated Domain concerns list
2. At least three domain concerns use vocabulary specific to `{topic}`
3. Each derived expert entry lists all five attributes individually:
   name, concern link, inertia gap, domain-vocabulary frame, verify focus —
   checked per expert, not as a total count
4. No derived expert name is a placeholder per [FC-1]: "domain-expert", "expert-1",
   "generic-expert" fail this gate item
5. No stock role names appear in this block

---

PHASE 3 — STOCK ROLES

```
STOCK-ROLES:
  - pm               (product value and user outcome lens)
  - architect        (technical structure and system boundary lens)
  - strategy         (business model and competitive position lens)
  - inertia-advocate (status-quo challenge lens — ANCHOR-CARD role;
                      Phase 1 INERTIA-SURFACE is its Diagnosis Card source;
                      Diagnosis Card is written FIRST in Phase 5 before all others)
```

**GATE** — Phase 3 complete when ALL of the following are TRUE:
1. STOCK-ROLES lists all four names with lens descriptors
2. inertia-advocate is flagged as ANCHOR-CARD role for Phase 5 ordering
3. Phase 1 INERTIA-SURFACE confirmed available as source

---

PHASE 4 — OUTPUT AREA

```
OUTPUT-AREA: .craft/roles/{area}/
```

Area slug must use domain vocabulary from Phase 2. NOT: `default`, `generic`, `roles`.

**GATE** — Phase 4 complete when ALL of the following are TRUE:
1. OUTPUT-AREA written with area slug using Phase 2 domain vocabulary
2. Path format is exactly `.craft/roles/{area}/`

---

PHASE 5 — DIAGNOSIS CARDS AND ROLE FILE WRITING

**PREPARE:** Confirm the following inputs before writing any Diagnosis Card:
- Phase 0 [FC-4] exact identifier: `verify_questions` (retrieve verbatim from [FC-4])
- Phase 0 [FC-5] exact identifier: `simplify_rules` (retrieve verbatim from [FC-5])
- Phase 1 INERTIA-SURFACE: status-quo claim, inertia-advocate profile, challenge questions
- Phase 2 DOMAIN-ANALYSIS: expert names, concern links, inertia gaps, frames, verify focuses
- Phase 3 STOCK-ROLES: four names; inertia-advocate flagged as ANCHOR-CARD
- Phase 4 OUTPUT-AREA path confirmed

PREPARE complete when all six inputs are confirmed. Do not begin Diagnosis Cards until confirmed.

**ANCHOR-CARD (write first, before all other Diagnosis Cards):**

```
ANCHOR-CARD (inertia-advocate):

  name: {Phase 1 inertia-advocate name — confirmed against [FC-1]}
  [FC-1] name check: this name is domain-specific because [vocabulary source]; confirmed

  frame (one sentence): {Phase 1 status-quo claim as epistemic stance}
  serves (one sentence): {beneficiary of the inertia verdict — NOT a frame restatement}

  primary_verify_question: {Phase 1 primary_verify_question — the anchor question
    for the cross-set scan; all subsequent cards must show orthogonality to this question}
  uniqueness argument: this question is uniquely attributable to the inertia-advocate
    because no other role challenges sufficiency of the status quo first — the closest
    overlap is [role-name], which would ask about [performance/design/etc.], but this
    role asks specifically whether the current system already handles the scenario —
    confirmed distinct

  collaborates_with draft: [{name-1}, {name-2}]
  phantom check: confirm each name appears in this registry — confirmed
```

**SUBSEQUENT DIAGNOSIS CARDS (domain experts and stock roles, after ANCHOR-CARD):**

```
DIAGNOSIS-CARD for {role-name}:

  name: {proposed slug}
  [FC-1] name check: this name is domain-specific because [vocabulary source]; confirmed

  frame (one sentence): {epistemic viewpoint — "sees X through the lens of Y"}
  serves (one sentence): {beneficiary — NOT a restatement of frame}

  primary_verify_question: {the most role-specific question for this frame}
  uniqueness argument: this question is uniquely attributable to this role because no other
    role in this registry would prioritize it first — the closest overlap is [role-name],
    which would ask [different angle] — confirmed distinct
  inertia card orthogonality: this question addresses a facet the ANCHOR-CARD cannot cover
    because [the inertia-advocate's primary_verify_question asks about status-quo
    sufficiency, while this question asks about {specific domain concern}] — confirmed
    orthogonal to ANCHOR-CARD primary question

  collaborates_with draft: [{name-1}, {name-2}]
  phantom check: confirm each name appears in this registry — confirmed
```

After all Diagnosis Cards are written, run a CROSS-CARD UNIQUENESS SCAN:

```
CROSS-CARD UNIQUENESS SCAN (ANCHOR-CARD as reference axis):
  Step 1: List all primary_verify_questions alongside their role names.
  Step 2: For each non-anchor card, confirm its primary question is orthogonal to the
    ANCHOR-CARD question (status-quo sufficiency) — check: could these two questions
    be asked by the same role? If yes, revise.
  Step 3: For each pair of non-anchor cards, confirm their primary questions address
    different facets. Flag any pair where both questions could be asked by the same role.
  Step 4: Revise all flagged questions before proceeding to YAML writing.
```

**WRITE:** One `.md` file per role to `.craft/roles/{area}/`. Write in this order:
inertia-advocate first (ANCHOR-CARD), then domain experts, then remaining stock roles.
Apply the FIELD CONTRACT to each file per the Phase 5 YAML template.

```yaml
---
name: {per Diagnosis Card — confirmed against [FC-1]}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Per [FC-2] and Diagnosis Card frame. FAILURE MODE: task-list frame.}
  serves: |
    {Per [FC-3] and Diagnosis Card serves — not a frame restatement.}

lens:
  verify_questions:
    - "{Primary verify question from Diagnosis Card — uniqueness confirmed}"
    - "{Additional question per [FC-4]}"

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
1. ANCHOR-CARD (inertia-advocate) was written before all other Diagnosis Cards
2. All subsequent Diagnosis Cards include inertia card orthogonality field
3. CROSS-CARD UNIQUENESS SCAN was run with ANCHOR-CARD as reference axis
4. One `.md` file per role at `.craft/roles/{area}/`; inertia-advocate written first
5. Every file uses exact identifiers `verify_questions` and `simplify_rules` verbatim
6. No role file uses a prohibited name per [FC-1]
7. No `collaborates_with` entries contain CONTRACT VIOLATION type-1 or type-2

---

PHASE 6 — REGISTRY SUMMARY

**PREPARE:** Enumerate the `.md` files written in Phase 5. Record as `PHASE5_COUNT`.
This count must come from Phase 5 file enumeration — NOT from adding prior-phase planned
counts. Deriving total_roles from "Phase 2 N experts + Phase 3 4 stock roles" instead of
enumerating Phase 5 output files is a count-bypass failure and invalidates this gate.

PREPARE complete when `PHASE5_COUNT` is recorded from Phase 5 enumeration.

**WRITE:** `.craft/roles/{area}/REGISTRY.md`:

```
---
area: {area}
generated: {date}
---

## Registry Summary

total_roles: {PHASE5_COUNT — from Phase 5 enumeration; not a computed sum}

stock_roles:
  - inertia-advocate  (ANCHOR-CARD — derived Phase 1; written first in Phase 5)
  - pm
  - architect
  - strategy

domain_experts:
  - name: {expert-name}
    derivation_source: Phase 2 domain concern #[N]
    inertia_gap: {from Phase 2 inertia gap attribute — the status-quo resistance
      this expert's domain names}
  (one entry per derived expert)

coverage_gaps: |
  {Phase 2 concerns not addressed by any derived expert; or "none detected."}

inertia_surface: |
  {Phase 1 status-quo claim verbatim — exact sentence from INERTIA-SURFACE block.
  Do not paraphrase. This fulfills the EXTENSION-COMMITMENT made in Phase 0.}

Generated by: /org-roles {topic} — {date}
```

HEADING STUB FAIL CONDITION: A `## Registry Summary` heading with no fields populated
beneath it is not a registry — this is the explicit C-10 failure condition. Every field
in the template above must contain substantive content; a section header with an empty
string or omitted value below it fails this step's completion gate.

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.craft/roles/{area}/REGISTRY.md`
2. `total_roles` equals `PHASE5_COUNT` from Phase 5 enumeration
3. `domain_experts` lists each derived expert with `name`, `derivation_source`, `inertia_gap`
4. `inertia_surface` contains Phase 1 status-quo claim verbatim — not paraphrased
5. No heading stubs — every field has substantive content; HEADING STUB FAIL CONDITION was read

---

## V-03 — Lifecycle Emphasis: Gap-First Expert Naming in Phase 2

**axis:** lifecycle-emphasis
**hypothesis:** R7 V-01 and V-02 both derive the domain expert name first, then link it
to a concern. This produces a name-first derivation that may select generic names before
the concern vocabulary is fully engaged. This variate shifts lifecycle emphasis: Phase 2
runs a dedicated INERTIA-GAP ANALYSIS sub-step that identifies each expert's inertia gap
BEFORE the expert name is written — gap-first derivation forces domain vocabulary to come
from the gap, not the concern heading. Phase 5 Diagnosis Cards inherit the inertia gap
from Phase 2's INERTIA-GAP ANALYSIS, so the uniqueness argument is built on an already-
specified gap rather than reconstructed at card-writing time. The Diagnosis Card and
cross-set scan mechanisms (C-35, C-36) are preserved. C-34 is satisfied via the Phase 2
gate which checks five attributes including the gap. C-15 is fixed to PASS.
Falsifiable: if gap-first naming produces expert names that are so tightly bound to their
inertia-gap framing that their frames become redundant with the inertia-advocate's frame,
the role differentiation (C-09) degrades even though structural compliance improves.

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
          The name must derive from the inertia gap vocabulary — not the concern heading.
          BAD:  "domain-expert" (no domain content; applies to any registry)
          GOOD: "backpressure-propagation-verifier" (derived from gap vocabulary)

  [FC-2]  orientation.frame
          type: string — epistemic viewpoint ("sees X through the lens of Y")
          FAILURE MODE: task list / job description
          BAD:  "Responsible for reviewing and surfacing issues"
          GOOD: "Sees every proposed change through the lens of whether backpressure
                 signals propagate correctly to upstream producers"

  [FC-3]  orientation.serves
          type: string — beneficiary statement; NOT a restatement of frame
          FAILURE MODE: frame restatement

  [FC-4]  lens.verify_questions
          EXACT IDENTIFIER: verify_questions
          PROHIBITED IDENTIFIERS: verify | questions | checks | verify_list
          All prohibited identifiers break downstream consumers that read by exact key
          type: list; minimum two items; at least one question uniquely attributable
            to this role's frame; uniqueness argument required before writing

  [FC-5]  lens.simplify_rules
          EXACT IDENTIFIER: simplify_rules
          PROHIBITED IDENTIFIERS: simplify | rules | constraints | guidelines
          All prohibited identifiers break downstream consumers that read by exact key
          type: list; minimum one item; opinionated exclusion — NOT a scope description

  [FC-6]  expertise.depth   — enum: expert | practitioner | senior | principal

  [FC-7]  expertise.relevance — domain-specific justification; not a role-name restatement

  [FC-8]  scope.primary     — main concern this role surfaces; one sentence

  [FC-9]  scope.boundary    — what this role does NOT own; explicit exclusion; one sentence

  [FC-10] collaborates_with
          type: list — registry members only
          CONTRACT VIOLATION (type 1) — PHANTOM: a role name absent from this registry
          CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT: `field_name` = `inertia_surface`; `population_source` names
   Phase 1 and INERTIA-SURFACE; `purpose` names the Phase 0 diagnostic question
2. FIELD-CONTRACT written with all ten items [FC-1] through [FC-10]
3. [FC-1] PROHIBITED NAMES clause names "domain-expert" and "expert-1"
4. [FC-4] and [FC-5] display exact identifier strings `verify_questions` and
   `simplify_rules` under EXACT IDENTIFIER labels — both appear verbatim

---

PHASE 1 — INERTIA SURFACE

Read `{topic}` context. Write an INERTIA-SURFACE block:

```
INERTIA-SURFACE for {topic}:

  Status-quo claim: [the strongest argument that {topic} is unnecessary — grounded
    in context; name the specific existing capability relied upon]

  Challenge questions (at minimum three; each uses vocabulary from `{topic}` context):
    1. What specific failure does the status quo produce that this feature resolves?
    2. [what does the existing mechanism already handle?]
    3. [what is the minimum status-quo fix, and why is it insufficient?]
```

Do not name domain experts in Phase 1.
The status-quo claim is copied verbatim to `inertia_surface` in Phase 6.

**GATE** — Phase 1 complete when ALL of the following are TRUE:
1. INERTIA-SURFACE block written
2. Status-quo claim names a specific existing capability (not generic)
3. At least three challenge questions use vocabulary from `{topic}` context
4. No domain expert names appear in this block

---

PHASE 2 — DOMAIN ANALYSIS (gap-first expert derivation)

Read `{topic}` context for concerns the Phase 1 status-quo claim does not address.

**Step 1 — INERTIA-GAP ANALYSIS:** Before naming any domain expert, identify the gaps
the Phase 1 status-quo claim leaves uncovered. For each gap, name:
- The specific failure mode the status quo cannot prevent
- The vocabulary domain this failure mode belongs to
- What status-quo resistance an expert from this domain would deploy

DO NOT name experts in Step 1. The gap analysis drives the name derivation in Step 2.

```
INERTIA-GAP ANALYSIS for {topic}:

  Gap 1: [description of what the Phase 1 inertia claim fails to address]
    Domain: [the vocabulary domain this gap belongs to — e.g., "retry semantics",
             "schema migration", "backpressure propagation"]
    Inertia resistance: [the status-quo argument an expert in this domain would make —
      the specific claim the inertia-advocate overlooks from this domain's perspective]

  Gap 2: [...]
    Domain: [...]
    Inertia resistance: [...]

  Gap 3: [...]
    Domain: [...]
    Inertia resistance: [...]

  (minimum three gaps)
```

DO NOT name derived experts with placeholder labels. The following names are
PROHIBITED by [FC-1]: "domain-expert", "expert-1", "generic-expert", "role-1".
Names must derive from the Gap Domain vocabulary above.

**Step 2 — EXPERT DERIVATION:** From each gap, derive an expert whose name comes from
the Gap Domain vocabulary:

```
DOMAIN-ANALYSIS for {topic}:

  Domain experts derived from INERTIA-GAP ANALYSIS:
    - Expert name: [slug from Gap N Domain vocabulary — PROHIBITED: "domain-expert", "expert-1"]
      Concern link: Gap [N] from INERTIA-GAP ANALYSIS
      Inertia gap: [Gap N inertia resistance — copied from INERTIA-GAP ANALYSIS;
        this is what this expert's domain sees that the inertia-advocate's frame misses]
      Domain-vocabulary frame: [per [FC-2] — epistemic viewpoint using Gap N Domain vocabulary]
      Verify focus: [what artifact or behavior this expert checks first]
    (one entry per gap — at minimum one expert)
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 2.

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. INERTIA-GAP ANALYSIS written with at least three gaps, each having Domain and
   Inertia resistance fields
2. At least three gaps use vocabulary specific to `{topic}`
3. Each derived expert entry lists all five attributes individually:
   name, concern link, inertia gap, domain-vocabulary frame, verify focus —
   checked per expert, not as a total count
4. Expert names derive from INERTIA-GAP ANALYSIS Domain vocabulary — not from
   concern headings alone; no placeholder per [FC-1]: "domain-expert", "expert-1",
   "generic-expert" fail this gate item
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
                      questions)
```

**GATE** — Phase 3 complete when ALL of the following are TRUE:
1. STOCK-ROLES lists all four names with lens descriptors
2. inertia-advocate identifies Phase 1 as source for frame and verify_questions
3. Phase 1 INERTIA-SURFACE confirmed available

---

PHASE 4 — OUTPUT AREA

```
OUTPUT-AREA: .craft/roles/{area}/
```

Area slug must use INERTIA-GAP ANALYSIS Domain vocabulary from Phase 2 (not generic).

**GATE** — Phase 4 complete when ALL of the following are TRUE:
1. OUTPUT-AREA written with area slug from Phase 2 Domain vocabulary
2. Path format is exactly `.craft/roles/{area}/`

---

PHASE 5 — DIAGNOSIS CARDS AND ROLE FILE WRITING

**PREPARE:** Confirm inputs before writing any Diagnosis Card:
- Phase 0 [FC-4] exact identifier: `verify_questions` (retrieve verbatim)
- Phase 0 [FC-5] exact identifier: `simplify_rules` (retrieve verbatim)
- Phase 1 INERTIA-SURFACE: status-quo claim and challenge questions confirmed
- Phase 2 INERTIA-GAP ANALYSIS: all gaps, domains, inertia resistances confirmed
- Phase 2 DOMAIN-ANALYSIS: expert names, concern links, inertia gaps, frames confirmed
- Phase 3 STOCK-ROLES: four names confirmed
- Phase 4 OUTPUT-AREA path confirmed

PREPARE complete when all seven inputs confirmed. Do not begin Diagnosis Cards until confirmed.

**DIAGNOSIS CARDS:** Before writing any YAML, write one Diagnosis Card per role. For domain
expert cards, the Diagnosis Card inherits the inertia gap from Phase 2 — do not re-derive it.

```
DIAGNOSIS-CARD for {role-name}:

  name: {proposed slug — for domain experts, derived from Phase 2 INERTIA-GAP ANALYSIS
         Domain vocabulary; confirmed against [FC-1]}
  [FC-1] name check: this name derives from [Gap N Domain vocabulary]; NOT a placeholder;
    confirmed

  frame (one sentence): {epistemic viewpoint — anchored to Phase 2 inertia gap for
    domain experts; to Phase 1 status-quo claim for inertia-advocate; standard lens
    for stock roles}
  serves (one sentence): {beneficiary — NOT a frame restatement}

  inertia gap inherited: {for domain experts: Gap N inertia resistance from Phase 2
    INERTIA-GAP ANALYSIS; for inertia-advocate: Phase 1 status-quo claim; for stock
    roles: N/A — stock role frames are not inertia-derived}

  primary_verify_question: {the most role-specific question for this frame}
  uniqueness argument: this question is uniquely attributable to this role because no other
    role in this registry would prioritize it first — the closest overlap is [role-name],
    which would ask [different angle] — confirmed distinct

  collaborates_with draft: [{name-1}, {name-2}]
  phantom check: confirm each name appears in this registry — confirmed
```

After all Diagnosis Cards are written, run a CROSS-CARD UNIQUENESS SCAN:

```
CROSS-CARD UNIQUENESS SCAN:
  For each pair of roles, confirm their primary_verify_questions address different
  facets. Flag any pair where both questions could be asked by the same role type.
  Revise flagged questions before proceeding to YAML writing.
```

**WRITE:** One `.md` file per role. Apply the FIELD CONTRACT to each file:

```yaml
---
name: {per Diagnosis Card — from Domain vocabulary per [FC-1]}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Per [FC-2] and Diagnosis Card frame. FAILURE MODE: task-list frame.}
  serves: |
    {Per [FC-3] and Diagnosis Card serves — not a frame restatement.}

lens:
  verify_questions:
    - "{Primary verify question from Diagnosis Card — uniqueness confirmed}"
    - "{Additional question per [FC-4]}"

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
1. One Diagnosis Card per role — all cards written before any YAML file
2. Domain expert cards show `inertia gap inherited` from Phase 2 INERTIA-GAP ANALYSIS
3. CROSS-CARD UNIQUENESS SCAN run; flagged pairs revised
4. One `.md` file per role at `.craft/roles/{area}/`
5. Every file uses exact identifiers `verify_questions` and `simplify_rules` verbatim
6. No role file uses a prohibited name per [FC-1]
7. No `collaborates_with` entries contain CONTRACT VIOLATION type-1 or type-2

---

PHASE 6 — REGISTRY SUMMARY

**PREPARE:** Enumerate `.md` files written in Phase 5. Record as `PHASE5_COUNT`.
Count must come from Phase 5 enumeration — NOT from adding prior-phase planned counts.
Deriving total_roles from INERTIA-GAP ANALYSIS gap count or Phase 3 stock role count
instead of enumerating Phase 5 output files is a count-bypass failure.

PREPARE complete when `PHASE5_COUNT` recorded from Phase 5 enumeration.

**WRITE:** `.craft/roles/{area}/REGISTRY.md`:

```
---
area: {area}
generated: {date}
---

## Registry Summary

total_roles: {PHASE5_COUNT — from Phase 5 enumeration; not a computed sum}

stock_roles:
  - pm
  - architect
  - strategy
  - inertia-advocate

domain_experts:
  - name: {expert-name}
    derivation_source: Phase 2 Gap [N] — {gap domain vocabulary}
    inertia_gap: {Phase 2 Gap N inertia resistance — the status-quo resistance
      this expert's domain names}
  (one entry per derived expert)

coverage_gaps: |
  {Phase 2 gaps not addressed by any derived expert; or "none detected."}

inertia_surface: |
  {Phase 1 status-quo claim verbatim — exact sentence from INERTIA-SURFACE block.
  Do not paraphrase. Fulfills EXTENSION-COMMITMENT from Phase 0.}

Generated by: /org-roles {topic} — {date}
```

HEADING STUB FAIL CONDITION: A `## Registry Summary` heading with no required fields
populated beneath it is not a registry and fails C-10 (registry content completeness).
A section header with empty or omitted field values is a structural omission, not a
partial registry. Every field in the template above must have substantive content.

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.craft/roles/{area}/REGISTRY.md`
2. `total_roles` equals `PHASE5_COUNT` from Phase 5 enumeration
3. `domain_experts` lists each expert with `name`, `derivation_source`, `inertia_gap`
4. `inertia_surface` contains Phase 1 status-quo claim verbatim
5. No heading stubs — every field has substantive content; HEADING STUB FAIL CONDITION read

---

## V-04 — Role Sequence + Output Format: Inertia-First Derivation + Five-Attribute + Diagnosis Pipeline

**axis:** role-sequence + output-format
**hypothesis:** V-01 unified the 5-attribute derivation format (C-34) with the Diagnosis
Card pipeline (C-35/C-36) in a single output-format axis. V-02 extended the inertia-first
sequence into Phase 5 via the ANCHOR-CARD mechanism. This combined variation takes both:
the Phase 2 five-attribute derivation record (including inertia gap) and the Phase 5
ANCHOR-CARD-first Diagnosis Card sequence. The combination tests whether inertia-first
derivation in Phase 2 (concern gap explicitly linked to the Phase 1 claim per expert)
combined with inertia-first Diagnosis Card authoring in Phase 5 produces stronger
structural coherence across the full pipeline — the inertia claim is the organizing
axis at both derivation time (Phase 2 gate) and card-authoring time (Phase 5 sequence).
C-15 is fixed to PASS. All other axes are held constant.
Falsifiable: if the dual inertia-first enforcement (Phase 2 + Phase 5) over-constrains the
registry toward status-quo framing and away from forward-looking domain concerns, the
role quality (C-05, C-09) degrades relative to the single-axis variants.

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
          BAD:  "domain-expert" (no domain content; applies to any registry)
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
            to this role's frame; uniqueness argument required before writing
          BAD:  "Is the design correct?" (unmeasurable; any role could ask this)
          GOOD: "Does the spec bound total retry attempts per operation window?"

  [FC-5]  lens.simplify_rules
          EXACT IDENTIFIER: simplify_rules
          PROHIBITED IDENTIFIERS: simplify | rules | constraints | guidelines
          All prohibited identifiers break downstream consumers that read by exact key
          type: list; minimum one item; opinionated exclusion — NOT a scope description
          BAD:  "Focus on retry and budget concerns"
          GOOD: "Skip changes that do not alter retry semantics or timeout behavior"

  [FC-6]  expertise.depth   — enum: expert | practitioner | senior | principal

  [FC-7]  expertise.relevance — domain-specific justification; not a role-name restatement

  [FC-8]  scope.primary     — main concern this role surfaces; one sentence

  [FC-9]  scope.boundary    — what this role does NOT own; explicit exclusion; one sentence

  [FC-10] collaborates_with
          type: list — registry members only
          CONTRACT VIOLATION (type 1) — PHANTOM: a role name absent from this registry's
            output; phantom names silently break all downstream skills
          CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent;
            prevents directed graph reasoning over collaborations
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT: `field_name` = `inertia_surface`; `population_source` names
   Phase 1 and INERTIA-SURFACE; `purpose` names the Phase 0 diagnostic question
2. FIELD-CONTRACT written with all ten items [FC-1] through [FC-10]
3. [FC-1] PROHIBITED NAMES clause names "domain-expert" and "expert-1"
4. [FC-4] and [FC-5] display exact identifier strings `verify_questions` and
   `simplify_rules` under EXACT IDENTIFIER labels — both appear verbatim

---

PHASE 1 — INERTIA SURFACE

Read `{topic}` context. Write an INERTIA-SURFACE block:

```
INERTIA-SURFACE for {topic}:

  Status-quo claim: [the strongest argument that {topic} is unnecessary — names
    the specific existing capability relied upon]

  Inertia-advocate profile:
    name: [domain-vocabulary slug per [FC-1] — PROHIBITED: "domain-expert", "expert-1"]
    primary_verify_question: [the most adversarial "why is this necessary?"]

  Challenge questions (at minimum three; `{topic}` vocabulary):
    1. What specific failure does the status quo produce that this feature resolves?
    2. [what does the existing mechanism already handle?]
    3. [what is the minimum status-quo fix, and why is it insufficient?]
```

Do not name domain experts in Phase 1.
The status-quo claim will be copied verbatim to `inertia_surface` in Phase 6.
The inertia-advocate profile provides the ANCHOR-CARD source for Phase 5.

**GATE** — Phase 1 complete when ALL of the following are TRUE:
1. INERTIA-SURFACE block written
2. Status-quo claim names a specific existing capability (not generic)
3. Inertia-advocate profile has name and primary_verify_question
4. At least three challenge questions use vocabulary from `{topic}` context
5. No domain expert names appear in this block

---

PHASE 2 — DOMAIN ANALYSIS

Read `{topic}` context for concerns the Phase 1 status-quo claim does not address.

DO NOT name derived experts with placeholder labels. PROHIBITED by [FC-1]:
"domain-expert", "expert-1", "generic-expert", "role-1". Names must come from
the domain vocabulary in the concerns list.

```
DOMAIN-ANALYSIS for {topic}:

  Inertia claim under challenge: [restate Phase 1 status-quo claim in one sentence]

  Domain concerns (at minimum three; each names a gap the inertia claim overlooks):
    1. [concern: specific failure mode not covered by the status-quo claim]
    2. [concern]
    3. [concern]

  Domain experts derived from concerns:
    - Expert name: [slug per [FC-1] — PROHIBITED: "domain-expert", "expert-1"]
      Concern link: [which concern above, by number]
      Inertia gap: [the specific Phase 1 claim this expert's concern challenges —
        name the mechanism the inertia-advocate relies on and why this expert's
        concern falls outside its coverage frame]
      Domain-vocabulary frame: [per [FC-2] — epistemic viewpoint]
      Verify focus: [what artifact or behavior this expert checks first]
    (repeat for each derived expert — at minimum one)
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 2.

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. DOMAIN-ANALYSIS block written with Inertia claim under challenge and concerns list
2. At least three domain concerns use vocabulary specific to `{topic}`
3. Each derived expert entry lists all five attributes individually:
   name, concern link, inertia gap, domain-vocabulary frame, verify focus —
   checked per expert, not as a total count; a single missing attribute fails this item
4. No derived expert name is a placeholder per [FC-1]: "domain-expert", "expert-1",
   "generic-expert" fail this gate item
5. No stock role names appear in this block

---

PHASE 3 — STOCK ROLES

```
STOCK-ROLES:
  - pm               (product value and user outcome lens)
  - architect        (technical structure and system boundary lens)
  - strategy         (business model and competitive position lens)
  - inertia-advocate (status-quo challenge lens — ANCHOR-CARD for Phase 5;
                      Phase 1 INERTIA-SURFACE is source for frame and verify_questions;
                      Diagnosis Card written FIRST before all other cards in Phase 5)
```

**GATE** — Phase 3 complete when ALL of the following are TRUE:
1. STOCK-ROLES lists all four names
2. inertia-advocate flagged as ANCHOR-CARD; Phase 1 named as source
3. Phase 1 INERTIA-SURFACE confirmed available

---

PHASE 4 — OUTPUT AREA

```
OUTPUT-AREA: .craft/roles/{area}/
```

Area slug uses domain vocabulary from Phase 2. NOT: `default`, `generic`, `roles`.

**GATE** — Phase 4 complete when ALL of the following are TRUE:
1. OUTPUT-AREA written with Phase 2 domain vocabulary area slug
2. Path format is exactly `.craft/roles/{area}/`

---

PHASE 5 — DIAGNOSIS CARDS AND ROLE FILE WRITING

**PREPARE:** Confirm all inputs before writing any Diagnosis Card:
- Phase 0 [FC-4] exact identifier: `verify_questions` (retrieve verbatim)
- Phase 0 [FC-5] exact identifier: `simplify_rules` (retrieve verbatim)
- Phase 1 INERTIA-SURFACE: status-quo claim, inertia-advocate name, primary_verify_question
- Phase 2 DOMAIN-ANALYSIS: expert names, concern links, inertia gaps, frames, verify focuses
- Phase 3 STOCK-ROLES: four names; inertia-advocate flagged as ANCHOR-CARD
- Phase 4 OUTPUT-AREA path confirmed

PREPARE complete when all six inputs confirmed. Do not begin Diagnosis Cards until confirmed.

**ANCHOR-CARD (write first):** The inertia-advocate's Diagnosis Card is written before all
other cards. It is the structural reference for subsequent cards' uniqueness arguments.

```
ANCHOR-CARD (inertia-advocate):

  name: {Phase 1 inertia-advocate name — confirmed against [FC-1]}
  [FC-1] name check: domain-specific vocabulary source confirmed; NOT a placeholder

  frame: {Phase 1 status-quo claim as epistemic stance — "sees every proposal through
    the lens of whether the existing mechanism named in Phase 1 already handles it"}
  serves: {beneficiary — NOT a frame restatement — the stakeholder who receives the
    inertia verdict}

  primary_verify_question: {Phase 1 primary_verify_question — this question is the
    ANCHOR for cross-set uniqueness; all subsequent cards must show they ask something
    this question cannot subsume}
  uniqueness argument: this question is uniquely attributable to the inertia-advocate
    because it challenges necessity at the feature level — no domain expert, stock PM,
    architect, or strategy role prioritizes necessity-of-the-whole first; the closest
    overlap is [role-name], which asks about [specific concern], not sufficiency of the
    status quo — confirmed distinct

  collaborates_with draft: [{name-1}, {name-2}]
  phantom check: each name confirmed in registry — confirmed
```

**SUBSEQUENT DIAGNOSIS CARDS (for all other roles, after ANCHOR-CARD):**

```
DIAGNOSIS-CARD for {role-name}:

  name: {slug — for domain experts, from Phase 2 derivation; confirmed against [FC-1]}
  [FC-1] name check: domain-specific vocabulary confirmed; NOT a placeholder

  frame: {epistemic viewpoint — "sees X through the lens of Y"}
  serves: {beneficiary — NOT a frame restatement}

  inertia gap source: {for domain experts: Phase 2 inertia gap attribute — the specific
    claim the inertia-advocate makes that this role's domain falls outside of; for stock
    roles: N/A — their frames are not inertia-derived}

  primary_verify_question: {the most role-specific question for this frame}
  uniqueness argument: this question is uniquely attributable to this role because no
    other role in this registry would prioritize it first — the closest overlap is
    [role-name], which would ask [different angle] — confirmed distinct
  ANCHOR-CARD orthogonality: this question is orthogonal to the ANCHOR-CARD's
    primary_verify_question because [the ANCHOR-CARD asks about status-quo sufficiency,
    while this question asks about {specific concern this role owns}] — confirmed

  collaborates_with draft: [{name-1}, {name-2}]
  phantom check: each name confirmed in registry — confirmed
```

After all Diagnosis Cards are written, run a CROSS-CARD UNIQUENESS SCAN:

```
CROSS-CARD UNIQUENESS SCAN:
  Reference: ANCHOR-CARD primary_verify_question = [{inertia-advocate question}]

  For each non-anchor card:
    - Confirm its primary question is orthogonal to the ANCHOR-CARD question
    - Confirm it cannot be subsumed by the ANCHOR-CARD's framing

  For each pair of non-anchor cards:
    - Confirm their primary questions address different facets
    - Flag any pair where both questions could be asked by the same role type

  Revise all flagged questions before proceeding to YAML writing.
```

**WRITE:** One `.md` file per role. Write inertia-advocate first, then domain experts,
then remaining stock roles. Apply the FIELD CONTRACT:

```yaml
---
name: {per Diagnosis Card — confirmed against [FC-1]}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Per [FC-2] and Diagnosis Card frame.
    FAILURE MODE: task-list frame — "responsible for X" is NOT an epistemic viewpoint.
    WORKED EXAMPLE (bad):  "Responsible for reviewing proposals and surfacing gaps."
    WORKED EXAMPLE (good): "Sees every proposed change through the lens of whether
      the existing mechanism named in Phase 1 already handles the scenario."}

  serves: |
    {Per [FC-3] and Diagnosis Card serves — not a frame restatement.
    FAILURE MODE: frame restatement.}

lens:
  verify_questions:
    - "{Primary verify question from Diagnosis Card — uniqueness confirmed}"
    - "{Additional question per [FC-4] — uniquely attributable to this role's frame}"

  simplify_rules:
    - "{Per [FC-5]: opinionated exclusion — 'Skip X unless Y.'
       FAILURE MODE: scope description — 'focus on X' is not an exclusion.}"

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
  - {per Diagnosis Card — ANCHOR-CARD orthogonality and phantom check confirmed}
  # CONTRACT VIOLATION (type 1) — PHANTOM: a role name absent from this registry.
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent.
```

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. ANCHOR-CARD (inertia-advocate) was written before all other Diagnosis Cards
2. All subsequent cards include inertia gap source and ANCHOR-CARD orthogonality fields
3. CROSS-CARD UNIQUENESS SCAN run with ANCHOR-CARD as reference; flagged pairs revised
4. One `.md` file per role at `.craft/roles/{area}/`; inertia-advocate file written first
5. Every file uses exact identifiers `verify_questions` and `simplify_rules` verbatim
6. No role file uses a prohibited name per [FC-1]: "domain-expert", "expert-1" fail
7. No `collaborates_with` entries contain CONTRACT VIOLATION type-1 or type-2

---

PHASE 6 — REGISTRY SUMMARY

**PREPARE:** Enumerate `.md` files written in Phase 5. Record as `PHASE5_COUNT`.
This count must come from Phase 5 file enumeration — NOT from adding prior-phase counts.
Deriving total_roles by adding "Phase 2 expert count + Phase 3 stock role count" instead
of enumerating Phase 5 output files is a count-bypass failure; the sum may differ from
what was actually written.

PREPARE complete when `PHASE5_COUNT` recorded from Phase 5 enumeration.

**WRITE:** `.craft/roles/{area}/REGISTRY.md`:

```
---
area: {area}
generated: {date}
---

## Registry Summary

total_roles: {PHASE5_COUNT — from Phase 5 enumeration; not a computed sum}

stock_roles:
  - inertia-advocate  (ANCHOR-CARD — derived Phase 1; written first)
  - pm
  - architect
  - strategy

domain_experts:
  - name: {expert-name}
    derivation_source: Phase 2 domain concern #[N]
    inertia_gap: {Phase 2 inertia gap attribute — the status-quo resistance
      this expert's domain names; not a paraphrase of the role name}
  (one entry per derived expert)

coverage_gaps: |
  {Phase 2 concerns not addressed by any derived expert; or "none detected."}

inertia_surface: |
  {Phase 1 status-quo claim verbatim — exact sentence. Do not paraphrase.
  Fulfills EXTENSION-COMMITMENT from Phase 0.}

Generated by: /org-roles {topic} — {date}
```

HEADING STUB FAIL CONDITION: A `## Registry Summary` heading with no fields populated
beneath it fails C-10 (registry content completeness). Every field must contain
substantive content — a section header with empty or omitted values is a structural
omission, not a partial registry.

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.craft/roles/{area}/REGISTRY.md`
2. `total_roles` equals `PHASE5_COUNT` from Phase 5 enumeration
3. `domain_experts` lists each expert with `name`, `derivation_source`, `inertia_gap`
4. `inertia_surface` contains Phase 1 status-quo claim verbatim
5. No heading stubs — HEADING STUB FAIL CONDITION was read; every field is populated

---

## V-05 — All Axes: Failure-Mode-First + Inertia-First + Five-Attribute + Diagnosis Pipeline

**axis:** all axes (phrasing-register + role-sequence + output-format + lifecycle-emphasis + inertia-framing)
**hypothesis:** V-01 through V-04 test individual axes or two-axis combinations. V-05
synthesizes all signals: (1) failure-mode-first phase openings from R7 V-03 — every phase
names its anti-patterns before instructions appear; (2) context-first inertia derivation
from R7 V-01 — inertia-advocate derived first in Phase 1 before domain experts; (3) the
five-attribute derivation gate from V-01 — inertia gap as fifth per-expert attribute in
Phase 2; (4) ANCHOR-CARD-first Diagnosis Card sequence from V-02 — inertia card is the
reference axis for cross-set uniqueness; (5) gap-first expert naming discipline from V-03
— expert names derive from inertia gap vocabulary; (6) explicit C-15 HEADING STUB FAIL
CONDITION naming the C-10 consequence; (7) self-labeling C-31 site markers at all three
placeholder prohibition checkpoints. The full synthesis tests whether all axes reinforce
each other or create structural tension where one axis's constraint conflicts with another.
Falsifiable: if the failure-mode-first openings combined with inertia-first derivation
and gap-first naming over-constrain the model's attention toward failure detection and
inertia analysis, leaving insufficient attention for building substantively differentiated
role frames (C-09), the all-axes synthesis underperforms the targeted single-axis variants.

---

You are running `/org-roles {topic}`.

---

PHASE 0 — FIELD CONTRACT AND EXTENSION COMMITMENT

**FAILURE MODES for Phase 0:**
- EXTENSION STUB: EXTENSION-COMMITMENT has `purpose` field that does not name the Phase 0
  diagnostic question it answers — stores what the field contains rather than what question
  it resolves
- PLACEHOLDER CONTRACT: FIELD-CONTRACT does not name "domain-expert", "expert-1" as
  anti-patterns by name under [FC-1] — states positive requirement only
- IDENTIFIER OMISSION: [FC-4] or [FC-5] do not display the exact identifier string that
  downstream consumers will read — if `verify_questions` does not appear verbatim under
  EXACT IDENTIFIER, the contract fails

To prevent these failures, write the following:

**EXTENSION-COMMITMENT:**

```
EXTENSION-COMMITMENT:
  field_name: inertia_surface
  population_source: Phase 1, INERTIA-SURFACE block, status-quo claim field
  purpose: answers the Phase 0 diagnostic question — "what is the strongest
    existing-system argument that makes {topic} premature?" — giving downstream
    consumers the exact design tension this role registry was built to hold
```

**FIELD CONTRACT:**

```
FIELD-CONTRACT for /org-roles {topic}:

  [FC-1]  name                                           [C-31-SITE-1: PROHIBITED NAMES]
          type: string — domain-vocabulary slug derived from context
          PROHIBITED NAMES: "domain-expert", "expert-1", "generic-expert", "role-1"
          These are PLACEHOLDER NAMES — the Phase 0 failure this contract prevents.
          A placeholder name passes visual inspection but carries no domain signal.
          The name must come from vocabulary in the concern or inertia gap it addresses.
          BAD:  "domain-expert" — placeholder; applies to any product
          GOOD: "backpressure-propagation-verifier" — derived from domain concern

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
            to this role's frame — no other role in this registry would prioritize
            that question first; uniqueness argument required before writing
          BAD:  "Is the design complete?" (any role could ask this)
          GOOD: "Does the spec provide a rollback path for each migration step —
                 verifiable by checking for ROLLBACK annotations in the migration section?"

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
            output; phantom names silently break all downstream skills
          CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent;
            prevents directed graph reasoning over collaborations
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT: `field_name` = `inertia_surface`; `population_source` names
   Phase 1 and INERTIA-SURFACE; `purpose` names the Phase 0 diagnostic question
2. FIELD-CONTRACT written with all ten items [FC-1] through [FC-10]
3. [FC-1] contains PROHIBITED NAMES clause naming "domain-expert" and "expert-1" —
   this is C-31-SITE-1; the clause name appears in [FC-1] header
4. [FC-4] and [FC-5] display exact identifier strings `verify_questions` and
   `simplify_rules` under EXACT IDENTIFIER labels — both appear verbatim

---

PHASE 1 — INERTIA DERIVATION (context-first; inertia-advocate derived before domain experts)

**FAILURE MODES for Phase 1:**
- GENERIC CLAIM: status-quo claim does not name a specific existing capability — says
  "the current system handles this" without naming what mechanism does so
- CONTEXT-FREE QUESTIONS: challenge questions use generic vocabulary rather than
  vocabulary from `{topic}` context
- EXPERT CONTAMINATION: domain expert names appear in this block (premature derivation)
- ANCHOR OMISSION: inertia-advocate profile missing name or primary_verify_question —
  the ANCHOR-CARD in Phase 5 cannot be written without both attributes from Phase 1

To prevent these failures, read `{topic}` context and write the INERTIA-DERIVATION block:

```
INERTIA-DERIVATION for {topic}:

  Status-quo claim: [the strongest argument that {topic} is unnecessary — grounded
    in the actual context; name the specific existing capability relied upon, or state
    "insufficient evidence of failure" if no capability is named in context]

  Inertia-advocate profile:
    name: [domain-vocabulary slug per [FC-1] — PROHIBITED: "domain-expert", "expert-1"]
    frame: [Phase 1 status-quo claim as epistemic stance — the ANCHOR-CARD frame source]
    primary_verify_question: [the most adversarial "why is this necessary?" — the
      ANCHOR question for Phase 5 cross-set uniqueness scan]

  Challenge questions (at minimum three; each uses vocabulary from `{topic}` context):
    1. What specific failure does the status quo produce that this feature resolves?
       (Name the failure from context; if unspecified, flag as a spec gap.)
    2. [what does the existing mechanism already handle — name it from context?]
    3. [what is the minimum status-quo fix, and why is it insufficient per the spec?]
```

Do not name domain experts in Phase 1. Domain experts are derived in Phase 2 to challenge
the status-quo claim. The status-quo claim will be copied verbatim to `inertia_surface`
in Phase 6.

**GATE** — Phase 1 complete when ALL of the following are TRUE:
1. INERTIA-DERIVATION block written
2. Status-quo claim names a specific existing capability (not generic)
3. Inertia-advocate profile contains all three attributes: name, frame, primary_verify_question
4. Inertia-advocate name passes [FC-1]: not "domain-expert", "expert-1", or any
   prohibited placeholder; uses vocabulary from `{topic}` context
5. At least three challenge questions use vocabulary from `{topic}` context
6. No domain expert names appear in this block

---

PHASE 2 — DOMAIN ANALYSIS (gap-first derivation; inertia gap as fifth per-expert attribute)

**FAILURE MODES for Phase 2:**
- PLACEHOLDER DERIVATION: domain expert named with a placeholder per [FC-1] —
  "domain-expert", "expert-1", "generic-expert" are prohibited;          [C-31-SITE-2]
  the name must derive from the inertia gap vocabulary, not the concern heading
- INERTIA GAP OMISSION: a derived expert entry missing the inertia gap attribute —
  the five-attribute gate requires name, concern link, inertia gap, domain-vocabulary
  frame, verify focus; missing the inertia gap is an INERTIA GAP OMISSION failure
- ATTRIBUTE INCOMPLETENESS: any entry missing any of the five required attributes
- STOCK CONTAMINATION: PM, Architect, Strategy, or inertia-advocate named in this block

To prevent these failures, run INERTIA-GAP ANALYSIS before naming any expert, then
derive experts from gaps:

**Step 1 — INERTIA-GAP ANALYSIS:**

```
INERTIA-GAP ANALYSIS for {topic}:

  Inertia claim under challenge: [restate Phase 1 status-quo claim in one sentence]

  Gap 1: [what the Phase 1 claim fails to address — uses {topic} domain vocabulary]
    Domain: [vocabulary domain of this gap]
    Inertia resistance: [the status-quo argument an expert from this domain would make]

  Gap 2: [...]
    Domain: [...]
    Inertia resistance: [...]

  Gap 3: [...]
    Domain: [...]
    Inertia resistance: [...]
  (minimum three gaps)
```

**Step 2 — EXPERT DERIVATION:** Names derive from Gap Domain vocabulary.

```
DOMAIN-ANALYSIS for {topic}:

  Domain experts derived from INERTIA-GAP ANALYSIS:
    - Expert name: [slug from Gap N Domain vocabulary —                [C-31-SITE-2 prose]
        PROHIBITED: "domain-expert", "expert-1", "generic-expert" — PLACEHOLDER DERIVATION
        failure prevented here; name must use Gap N Domain vocabulary specifically]
      Concern link: Gap [N] from INERTIA-GAP ANALYSIS
      Inertia gap: [Gap N inertia resistance — the status-quo claim this expert's
        domain exposes as insufficient; copied from INERTIA-GAP ANALYSIS Step 1]
      Domain-vocabulary frame: [per [FC-2] — epistemic viewpoint from Gap Domain vocab]
      Verify focus: [what artifact or behavior this expert checks first]
    (one entry per gap — at minimum one expert)
```

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. INERTIA-GAP ANALYSIS written with at minimum three gaps; each has Domain and
   Inertia resistance fields using vocabulary from `{topic}`
2. DOMAIN-ANALYSIS written; expert names derive from INERTIA-GAP ANALYSIS Domain vocab
3. Each derived expert lists all five attributes individually:
   name, concern link, inertia gap, domain-vocabulary frame, verify focus —
   checked per expert, not as a total count; INERTIA GAP OMISSION fails this item
4. No placeholder per [FC-1] C-31-SITE-2: "domain-expert", "expert-1", "generic-expert"
   fail this gate item — PLACEHOLDER DERIVATION failure
5. No stock role names appear in this block

---

PHASE 3 — STOCK ROLES

**FAILURE MODES for Phase 3:**
- ANCHOR OMISSION: inertia-advocate listed without flagging it as ANCHOR-CARD for Phase 5

To prevent this failure, write:

```
STOCK-ROLES:
  - pm               (product value and user outcome lens)
  - architect        (technical structure and system boundary lens)
  - strategy         (business model and competitive position lens)
  - inertia-advocate (status-quo challenge lens — ANCHOR-CARD for Phase 5;
                      Phase 1 INERTIA-DERIVATION is source for name, frame,
                      primary_verify_question, and challenge questions;
                      Diagnosis Card written FIRST before all other cards in Phase 5)
```

**GATE** — Phase 3 complete when ALL of the following are TRUE:
1. STOCK-ROLES lists all four names with lens descriptors
2. inertia-advocate flagged as ANCHOR-CARD; Phase 1 named as source for all attributes
3. Phase 1 INERTIA-DERIVATION confirmed available

---

PHASE 4 — OUTPUT AREA

**FAILURE MODES for Phase 4:**
- GENERIC AREA SLUG: `default`, `generic`, `roles`, or any slug not from Phase 2
  INERTIA-GAP ANALYSIS Domain vocabulary

To prevent this failure, write:

```
OUTPUT-AREA: .craft/roles/{area}/
```

Area slug must come from Phase 2 INERTIA-GAP ANALYSIS Domain vocabulary.

**GATE** — Phase 4 complete when ALL of the following are TRUE:
1. OUTPUT-AREA written with area slug from Phase 2 Domain vocabulary
2. Path format is exactly `.craft/roles/{area}/`

---

PHASE 5 — DIAGNOSIS CARDS AND ROLE FILE WRITING

**FAILURE MODES for Phase 5:**
- IDENTIFIER VIOLATION: YAML uses `verify` or `questions` instead of `verify_questions`,
  or `simplify` or `rules` instead of `simplify_rules` — exact identifiers required
- PLACEHOLDER NAME IN FILE: any file's `name` field uses "domain-expert", "expert-1",
  or "generic-expert" — the PLACEHOLDER DERIVATION failure at write time [C-31-SITE-3]
- TASK-LIST FRAME: `orientation.frame` is a job description, not an epistemic viewpoint
- PHANTOM COLLABORATOR: `collaborates_with` lists a name not present in this registry
- UNIQUENESS FAILURE: two roles' primary verify_questions address the same facet
- ANCHOR BYPASS: domain expert Diagnosis Cards written before the ANCHOR-CARD is complete

To prevent these failures, follow this procedure:

**PREPARE:** Confirm inputs before writing any Diagnosis Card:
- Phase 0 [FC-4] exact identifier: `verify_questions` (retrieve verbatim)
- Phase 0 [FC-5] exact identifier: `simplify_rules` (retrieve verbatim)
- Phase 1 INERTIA-DERIVATION: name, frame, primary_verify_question, challenge questions
- Phase 2 INERTIA-GAP ANALYSIS and DOMAIN-ANALYSIS: all five attributes per expert
- Phase 3 STOCK-ROLES: four names; inertia-advocate flagged as ANCHOR-CARD
- Phase 4 OUTPUT-AREA path confirmed

PREPARE complete when all six inputs confirmed. Do not begin Diagnosis Cards until confirmed.

**ANCHOR-CARD (write first — before all other Diagnosis Cards):**

```
ANCHOR-CARD (inertia-advocate):

  name: {Phase 1 INERTIA-DERIVATION name — confirmed against [FC-1]; not a placeholder}
  [FC-1] C-31-SITE-3 name check: this name derives from {topic} domain vocabulary;
    NOT "domain-expert", "expert-1", or any placeholder — confirmed

  frame: {Phase 1 status-quo claim as epistemic stance}
  serves: {beneficiary of the inertia verdict — NOT a frame restatement}

  primary_verify_question: {Phase 1 primary_verify_question}
  ANCHOR note: this is the cross-set uniqueness reference; all subsequent cards must
    show their primary question is orthogonal to this question
  uniqueness argument: this question is uniquely attributable to the inertia-advocate
    because it challenges feature necessity at the level of status-quo sufficiency —
    the closest overlap is [role-name], which would ask [different angle], but this
    role asks specifically whether the current system already handles the scenario —
    confirmed distinct

  collaborates_with draft: [{name-1}, {name-2}]
  phantom check: each name confirmed in registry — confirmed
```

**SUBSEQUENT DIAGNOSIS CARDS (domain experts and stock roles; after ANCHOR-CARD):**

```
DIAGNOSIS-CARD for {role-name}:

  name: {slug — for domain experts, from Phase 2 INERTIA-GAP ANALYSIS Domain vocabulary;
         confirmed against [FC-1]; NOT a placeholder — C-31-SITE-3}
  [FC-1] name check: domain vocabulary source confirmed; NOT "domain-expert", "expert-1" —
    confirmed

  frame: {epistemic viewpoint — "sees X through the lens of Y"}
  serves: {beneficiary — NOT a frame restatement}

  inertia gap: {for domain experts: Phase 2 inertia gap attribute; for stock roles: N/A}

  primary_verify_question: {the most role-specific question for this frame}
  uniqueness argument: this question is uniquely attributable to this role because no
    other role in this registry would prioritize it first — the closest overlap is
    [role-name], which would ask [different angle] — confirmed distinct
  ANCHOR-CARD orthogonality: this question is orthogonal to the ANCHOR-CARD question
    because [ANCHOR asks about status-quo sufficiency; this role asks about {specific
    domain concern}] — confirmed they address different facets

  collaborates_with draft: [{name-1}, {name-2}]
  phantom check: each name confirmed in registry — confirmed
```

After all Diagnosis Cards are written, run a CROSS-CARD UNIQUENESS SCAN:

```
CROSS-CARD UNIQUENESS SCAN:
  ANCHOR reference: [{inertia-advocate primary_verify_question}]

  Step 1: For each non-anchor card, confirm primary question is orthogonal to ANCHOR.
  Step 2: For each non-anchor pair, confirm primary questions address different facets.
  Step 3: Flag any pair where both questions could be asked by the same role type.
  Step 4: Revise all flagged questions. Do not begin YAML writing until scan is clean.
```

**WRITE:** One `.md` file per role. Inertia-advocate first, then domain experts,
then remaining stock roles. Apply the FIELD CONTRACT:

```yaml
---
name: {per Diagnosis Card — confirmed against [FC-1]; C-31-SITE-3 check}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Per [FC-2] and Diagnosis Card frame.
    FAILURE MODE: task-list frame — "responsible for reviewing" is NOT epistemic.
    WORKED EXAMPLE (bad):  "Responsible for reviewing proposals and surfacing gaps."
    WORKED EXAMPLE (good): "Sees every proposed change through the lens of whether
      the existing mechanism named in Phase 1 already handles the scenario."}

  serves: |
    {Per [FC-3] and Diagnosis Card serves — not a frame restatement.
    FAILURE MODE: frame restatement.
    WORKED EXAMPLE (bad):  "Ensures status-quo concerns are surfaced."
    WORKED EXAMPLE (good): "Engineering leads deciding whether to proceed — they
      receive a verdict on whether the Phase 1 inertia claim holds."}

lens:
  verify_questions:
    - "{Primary verify question from Diagnosis Card — uniqueness confirmed}"
    - "{Additional question per [FC-4] — uniquely attributable to this role's frame}"

  simplify_rules:
    - "{Per [FC-5]: opinionated exclusion — 'Skip X unless Y.'
       FAILURE MODE: scope description — 'focus on X' is NOT an exclusion rule.}"

expertise:
  depth: {per [FC-6]: expert | practitioner | senior | principal}
  relevance: |
    {Per [FC-7]: domain-specific justification — not a restatement of role name.}

scope:
  primary: |
    {Per [FC-8]: one sentence.}
  boundary: |
    {Per [FC-9]: explicit exclusion, one sentence.}

collaborates_with:
  - {per Diagnosis Card — ANCHOR-CARD orthogonality and phantom check confirmed}
  # CONTRACT VIOLATION (type 1) — PHANTOM: a role name absent from this registry.
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent.
```

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. ANCHOR-CARD (inertia-advocate) written before all other Diagnosis Cards
2. All subsequent Diagnosis Cards include inertia gap and ANCHOR-CARD orthogonality
3. CROSS-CARD UNIQUENESS SCAN run; flagged pairs revised; scan confirmed clean
4. One `.md` file per role at `.craft/roles/{area}/`; inertia-advocate written first
5. Every file uses exact identifiers `verify_questions` and `simplify_rules` verbatim —
   both strings appear as YAML keys; C-31-SITE-3 placeholder check passed for all files
6. Inertia-advocate: frame from Phase 1 status-quo claim; verify_questions include
   Phase 1 primary_verify_question
7. No `collaborates_with` entries contain CONTRACT VIOLATION type-1 or type-2

---

PHASE 6 — REGISTRY SUMMARY

**FAILURE MODES for Phase 6:**
- COUNT BYPASS: deriving total_roles from prior-phase planned counts (e.g., "I listed
  N roles in Phase 3 so total_roles = N") instead of enumerating Phase 5 output files
- HEADING STUB: `## Registry Summary` present with no fields populated — the Phase 6
  failure that invalidates C-10 (registry content completeness)
- INERTIA SURFACE PARAPHRASE: `inertia_surface` field contains a summary rather than
  the exact verbatim sentence from Phase 1 INERTIA-DERIVATION

To prevent these failures:

**PREPARE:** Enumerate `.md` files written in Phase 5. Record as `PHASE5_COUNT`.
COUNT BYPASS failure: deriving total_roles from "Phase 2 expert count + Phase 3 stock
role count" instead of enumerating Phase 5 output files is a named failure class —
the sum may differ from what was actually written; only Phase 5 enumeration is valid.

PREPARE complete when `PHASE5_COUNT` recorded from Phase 5 enumeration.

**WRITE:** `.craft/roles/{area}/REGISTRY.md`:

```
---
area: {area}
generated: {date}
---

## Registry Summary

total_roles: {PHASE5_COUNT — from Phase 5 enumeration; not a computed sum;
  COUNT BYPASS failure if derived from prior-phase counts}

stock_roles:
  - inertia-advocate  (ANCHOR-CARD — Phase 1 INERTIA-DERIVATION source; written first)
  - pm
  - architect
  - strategy

domain_experts:
  - name: {expert-name}
    derivation_source: Phase 2 Gap [N] — {domain vocabulary}
    inertia_gap: {Phase 2 INERTIA-GAP ANALYSIS gap N inertia resistance — verbatim
      from Phase 2; not paraphrased; the status-quo resistance this expert's domain
      names against the Phase 1 claim}
  (one entry per derived expert)

coverage_gaps: |
  {Phase 2 gaps not addressed by any derived expert; or "none detected."
  A genuine diagnostic answer — not a heading stub.}

inertia_surface: |
  {Phase 1 status-quo claim — EXACT VERBATIM sentence from INERTIA-DERIVATION block.
  INERTIA SURFACE PARAPHRASE failure if summarized or reworded.
  Fulfills EXTENSION-COMMITMENT from Phase 0.}

Generated by: /org-roles {topic} — {date}
```

HEADING STUB FAIL CONDITION: A `## Registry Summary` heading with no required fields
populated beneath it is not a registry — this is the explicit C-10 failure condition
(registry content completeness). A section header with empty or omitted field values
is a structural omission. Every field in the template above must contain substantive
content before this step's gate can pass.

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.craft/roles/{area}/REGISTRY.md`
2. `total_roles` equals `PHASE5_COUNT` from Phase 5 enumeration; COUNT BYPASS confirmed absent
3. `domain_experts` lists each expert with `name`, `derivation_source`, `inertia_gap`
4. `inertia_surface` contains Phase 1 status-quo claim verbatim — INERTIA SURFACE
   PARAPHRASE confirmed absent
5. No heading stubs — HEADING STUB FAIL CONDITION read; every field has substantive
   content below its header; C-10 failure condition explicitly checked
