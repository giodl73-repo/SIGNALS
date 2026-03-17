---
skill: quest-variate
skill_target: org-roles
date: 2026-03-16
round: R10
rubric_version: v10
status: variate
---

# org-roles Variate — Round 10

**Date:** 2026-03-16
**Skill:** org-roles
**Rubric:** v10 (C-01 through C-47; new in v10: C-42 standalone enumeration phase, C-43 named
revision phase — both close the C-38 PARTIAL gap from R9 V-04)
**Round:** R10 — single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

---

## Round 10 Variation Map

| V | Axis | Primary C targets | Hypothesis |
|---|------|------------------|------------|
| V-01 | lifecycle emphasis | C-42 PASS (C-38 still PARTIAL) | Add Phase 0 — Enumerate as standalone list-only phase before Phase 1 Anchor-Orthogonality; keep resolution as trailing instruction; isolates C-42 without C-43 |
| V-02 | lifecycle emphasis | C-43 PASS (C-38 still PARTIAL) | Promote revision to Phase 3 — Revision and Resolution as top-level named phase at same level as checking phases; keep enumeration merged into Phase 1; isolates C-43 without C-42 |
| V-03 | lifecycle emphasis | C-42 PASS + C-43 PASS → C-38 PASS | Restructure scan into four explicitly named phases (Enumerate / Anchor-Orthogonality / Pairwise / Revision-Resolution); both C-42 and C-43 addressed simultaneously; rest of prompt identical to V-04 R9 |
| V-04 | all axes combined | C-42 PASS + C-43 PASS + all C-37 through C-47 PASS | Full synthesis: R9 V-04 pipeline + 4-phase scan; target 39/39 = 100.00 |
| V-05 | all axes + phrasing register | C-42 PASS + C-43 PASS + C-29/C-33 regression recovery | R9 V-05 imperative/checklist register + 4-phase scan + restored CONTRACT VIOLATION framing to recover C-29/C-33 PARTIAL regressions |

---

## V-01 — Single-Axis: Standalone Enumeration Phase (C-42 target)

**axis:** lifecycle emphasis
**hypothesis:** R9 V-04 fails C-42 because its "Phase 1 — Anchor-Orthogonality Check" subsumes
both listing and checking under one phase header. This variate adds "Phase 0 — Enumerate All
Verify Questions" as a list-only phase before Phase 1. The resolution step remains a trailing
instruction (no separate phase label) to isolate the C-42 fix without C-43. Expected outcome:
C-42 PASS, C-43 FAIL, C-38 PARTIAL (two checking phases + enumeration = three named phases but
resolution not a labeled phase). All other R9 V-04 criteria unchanged.
Falsifiable: if the evaluator treats "Phase 0" as a non-canonical label and requires "Phase 1"
for the enumeration, C-42 may score PARTIAL rather than PASS. Testing whether ordinal labeling
is required or whether any standalone phase header suffices.

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
          The name must derive from the vocabulary of the named GAP-{slug} entry in Phase 2.
          POSITIVE SOURCING REQUIRED: each expert name must cite the specific GAP-{slug}
            identifier and the Domain vocabulary term used in the name.
          BAD:  "domain-expert" (no domain content; no traceable gap source)
          GOOD: "retry-budget-compliance-analyst" — derived from GAP-retry-semantics,
                term "retry-budget" from Domain vocabulary

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
          type: list; minimum two items; uniqueness argument required before writing

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

  [FC-11] orthogonality
          Applies to: all non-anchor YAML files (omit from inertia-advocate ANCHOR-CARD)
          type: string — named contrast axis tracing this role's concern to its
            divergence from the ANCHOR-CARD primary verify question
          REQUIRED: must appear in the YAML output file, not only in the Diagnosis Card
          REQUIRED FORMAT: "[Named contrast axis] — this role's lens diverges from the
            ANCHOR-CARD because [specific reason naming the anchor's question and how
            this role's concern falls outside that question's scope]"
          FAILURE MODE: generic assertion not tracing to the anchor question

  [FC-12] inertia_gap_inherited
          Applies to: domain expert YAML files only
          type: string — provenance field tracing this role's inertia gap to a named
            GAP-{slug} entry in Phase 2 INERTIA-GAP ANALYSIS
          REQUIRED: must appear in the YAML output file, not only in the Diagnosis Card
          REQUIRED FORMAT: "GAP-{slug}: [inertia resistance copied verbatim from
            INERTIA-GAP ANALYSIS]"
          FAILURE MODE: positional reference only ("Gap 1: ...") — fails [FC-12]
          NOTE: GAP-{slug} identifier must match exactly the identifier assigned in Phase 2
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT: all three elements present; `field_name` = `inertia_surface`
2. FIELD-CONTRACT written with all twelve items [FC-1] through [FC-12]
3. [FC-1] contains both PROHIBITED NAMES clause and POSITIVE SOURCING REQUIRED clause
4. [FC-4] and [FC-5] display exact identifier strings `verify_questions` and
   `simplify_rules` under EXACT IDENTIFIER labels — both appear verbatim
5. [FC-11] written with REQUIRED and REQUIRED FORMAT; states YAML persistence
6. [FC-12] written with REQUIRED and REQUIRED FORMAT citing GAP-{slug}; states YAML
   persistence and that positional-only reference fails

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
1. INERTIA-SURFACE block written with status-quo claim naming a specific capability
2. At least three challenge questions using `{topic}` vocabulary
3. No domain expert names appear

---

PHASE 2 — DOMAIN ANALYSIS (named-identifier gap-first derivation)

Read `{topic}` context for concerns the Phase 1 status-quo claim does not address.

**Step 1 — INERTIA-GAP ANALYSIS with formal named identifiers:**
Before naming any domain expert, identify gaps and assign each a formal GAP-{slug}
identifier derived from that gap's Domain vocabulary. DO NOT name experts in Step 1.

```
INERTIA-GAP ANALYSIS for {topic}:

  GAP-{domain-slug-1}:
    Domain: [named vocabulary domain for this gap]
    Failure mode: [specific failure the status quo cannot prevent]
    Inertia resistance: [what the Phase 1 inertia claim overlooks from this domain]

  GAP-{domain-slug-2}:
    Domain: [...]
    Failure mode: [...]
    Inertia resistance: [...]

  GAP-{domain-slug-3}:
    Domain: [...]
    Failure mode: [...]
    Inertia resistance: [...]

  (minimum three named gaps; GAP-{slug} identifier must derive from Domain vocabulary)
```

Expert names must derive from GAP-{slug} Domain vocabulary. PROHIBITED by [FC-1]:
"domain-expert", "expert-1", "generic-expert", "role-1".

**Step 2 — EXPERT DERIVATION with positive sourcing:**

```
DOMAIN-ANALYSIS for {topic}:

  Domain experts derived from INERTIA-GAP ANALYSIS:
    - Expert name: [slug from GAP-{slug} Domain vocabulary]
      POSITIVE SOURCING: "this name derives from GAP-{slug} Domain vocabulary:
        [specific term from that vocabulary used in the name]"
      Named gap source: GAP-{slug} from INERTIA-GAP ANALYSIS
      Inertia gap: [GAP-{slug} inertia resistance — copied verbatim]
      Domain-vocabulary frame: [per [FC-2] using GAP-{slug} vocabulary]
      Verify focus: [what artifact or behavior this expert checks first]
    (one entry per named gap — at minimum one)
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 2.

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. INERTIA-GAP ANALYSIS written before DOMAIN-ANALYSIS; at least three named gaps
   in GAP-{slug} format, each with Domain, Failure mode, Inertia resistance
2. GAP-{slug} identifiers derive from their respective Domain vocabularies
3. Each derived expert lists all five attributes including POSITIVE SOURCING statement
4. POSITIVE SOURCING statement cites specific GAP-{slug} and domain vocabulary term used
5. No placeholder names; no stock role names

---

PHASE 3 — STOCK ROLES

```
STOCK-ROLES:
  - inertia-advocate  (status-quo challenge lens — ANCHOR-CARD for this registry;
                       orientation.frame anchors to Phase 1 status-quo claim;
                       verify_questions sourced from Phase 1 challenge questions;
                       Diagnosis Card written FIRST in Phase 5; YAML written FIRST;
                       carries `anchor: true`; does NOT carry `orthogonality` or
                       `inertia_gap_inherited`)
  - pm                (product value and user outcome lens)
  - architect         (technical structure and system boundary lens)
  - strategy          (business model and competitive position lens)
```

All non-anchor roles carry `orthogonality` per [FC-11] in their YAML files.
Domain expert roles carry `inertia_gap_inherited` per [FC-12] in their YAML files.

**GATE** — Phase 3 complete when ALL of the following are TRUE:
1. STOCK-ROLES lists all four names with lens descriptors
2. inertia-advocate explicitly designated ANCHOR-CARD with write-first mandate for Phase 5
3. [FC-11] and [FC-12] field assignments confirmed for respective role types
4. Phase 1 INERTIA-SURFACE confirmed available as source

---

PHASE 4 — OUTPUT AREA

```
OUTPUT-AREA: .craft/roles/{area}/
```

Area slug uses GAP-{slug} Domain vocabulary from Phase 2. NOT: `default`, `generic`, `roles`.

**GATE** — Phase 4 complete when ALL of the following are TRUE:
1. OUTPUT-AREA written with area slug from Phase 2 GAP Domain vocabulary
2. Path format is exactly `.craft/roles/{area}/`

---

PHASE 5 — DIAGNOSIS CARDS AND ROLE FILE WRITING

**PREPARE:** Confirm inputs before writing any Diagnosis Card:
- Phase 0 [FC-4] exact identifier: `verify_questions` (retrieve verbatim)
- Phase 0 [FC-5] exact identifier: `simplify_rules` (retrieve verbatim)
- Phase 0 [FC-11] REQUIRED FORMAT for `orthogonality` YAML field (retrieve verbatim)
- Phase 0 [FC-12] REQUIRED FORMAT for `inertia_gap_inherited` YAML field (retrieve verbatim)
- Phase 1 INERTIA-SURFACE: status-quo claim and challenge questions confirmed
- Phase 2 INERTIA-GAP ANALYSIS: all GAP-{slug} entries with Domain and Inertia resistance
- Phase 2 DOMAIN-ANALYSIS: expert names with POSITIVE SOURCING confirmed
- Phase 3 STOCK-ROLES: four names; inertia-advocate ANCHOR-CARD confirmed
- Phase 4 OUTPUT-AREA path confirmed

PREPARE complete when all nine inputs confirmed. Do not begin Diagnosis Cards until confirmed.

**ANCHOR-CARD (write first):**

```
ANCHOR-CARD for inertia-advocate:

  name: {domain-vocabulary slug — confirmed against [FC-1]}
  [FC-1] name check: domain-specific because [vocabulary source]; NOT placeholder; confirmed

  frame (one sentence): {Phase 1 status-quo claim as epistemic stance}
  serves (one sentence): {beneficiary — NOT a frame restatement}

  primary_verify_question: {most adversarial "why is the status quo sufficient?" —
    this is the Phase 1 reference axis for the CROSS-CARD UNIQUENESS SCAN}
  uniqueness argument: uniquely attributable to inertia-advocate because [reason];
    confirmed distinct
  anchor status: ANCHOR-CARD — primary question is Phase 1 scan reference axis;
    all non-anchor YAML files carry `orthogonality` tracing to this question

  collaborates_with draft: [{name-1}, {name-2}]; phantom check: confirmed
```

**SUBSEQUENT DIAGNOSIS CARDS (after ANCHOR-CARD):**

```
DIAGNOSIS-CARD for {role-name}:

  name: {for domain experts: from GAP-{slug} Domain vocabulary, POSITIVE SOURCING
         confirmed; confirmed against [FC-1]}
  [FC-1] name check: derives from GAP-{slug} vocabulary: [term used]; NOT placeholder;
    confirmed

  frame (one sentence): {for domain experts: from GAP-{slug} vocabulary;
    for stock roles: standard lens}
  serves (one sentence): {beneficiary — NOT a restatement}

  inertia gap inherited: {for domain experts: "GAP-{slug}: [inertia resistance copied
    verbatim]" — cite by GAP-{slug} name per [FC-12]; for stock roles: N/A}
  orthogonality to ANCHOR-CARD: {per [FC-11] REQUIRED FORMAT — named contrast axis
    tracing how this role's concern falls outside the anchor's sufficiency question;
    this value copied verbatim to YAML `orthogonality` field}

  primary_verify_question: {most role-specific question for this frame}
  uniqueness argument: [reason]; confirmed distinct

  collaborates_with draft: [{name-1}, {name-2}]; phantom check: confirmed
```

After all Diagnosis Cards, run **CROSS-CARD UNIQUENESS SCAN**:

```
CROSS-CARD UNIQUENESS SCAN (ANCHOR-CARD as reference axis):

  Phase 0 — Enumerate All Verify Questions:
    List every primary_verify_question from every Diagnosis Card written above.
    Format: [role-name]: "[question text]"
    Scope: enumeration only — no checking, no flagging in this phase.
    Enumeration complete when every card's primary question appears exactly once.

  Phase 1 — Anchor-Orthogonality Check:
    Using the enumerated questions from Phase 0 as the reference list:
    State the ANCHOR-CARD primary_verify_question (from Phase 0).
    For each non-anchor role: retrieve its question from Phase 0.
    Test: could this role's question and the anchor question both be asked by the
      same role? If yes, flag and revise the non-anchor question.
    Record PASS or FLAG per non-anchor role. Resolve all flags before Phase 2.

  Phase 2 — Non-Anchor Pairwise Check:
    Using Phase 0 enumeration (non-anchor entries only) as reference:
    For each pair of non-anchor roles: compare primary_verify_questions.
    Test: could both questions be asked by the same role type?
    Flag any pair where both questions serve the same epistemic purpose.
    Revise all flagged questions. Record resolution before YAML writing begins.
```

**WRITE:** One `.md` file per role. Order: inertia-advocate (ANCHOR-CARD) first, then
domain experts, then remaining stock roles.

```yaml
---
name: {per Diagnosis Card — [FC-1] positive sourcing confirmed}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

# ANCHOR-CARD field (inertia-advocate only):
anchor: true   # omit from non-anchor roles

# Non-anchor roles only (omit from inertia-advocate):
orthogonality: "{per [FC-11] REQUIRED FORMAT — named contrast axis from Diagnosis Card;
  not generic; traces to ANCHOR-CARD primary question}"

# Domain expert roles only (omit from stock roles and inertia-advocate):
inertia_gap_inherited: "{per [FC-12] REQUIRED FORMAT: GAP-{slug}: [resistance verbatim]}"

orientation:
  frame: |
    {Per [FC-2]. FAILURE MODE: task-list frame.}
  serves: |
    {Per [FC-3] — NOT a frame restatement.}

lens:
  verify_questions:
    - "{Primary verify question — uniqueness confirmed}"
    - "{Additional question per [FC-4]}"

  simplify_rules:
    - "{Per [FC-5]: opinionated exclusion — 'Skip X unless Y.'}"

expertise:
  depth: {per [FC-6]}
  relevance: |
    {Per [FC-7]: domain-specific.}

scope:
  primary: |
    {Per [FC-8]: one sentence.}
  boundary: |
    {Per [FC-9]: explicit exclusion, one sentence.}

collaborates_with:
  - {per Diagnosis Card — phantom check confirmed}
  # CONTRACT VIOLATION (type 1) — PHANTOM
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST
```

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. ANCHOR-CARD Diagnosis Card written first; all subsequent cards written after
2. All subsequent Diagnosis Cards include `inertia gap inherited` (domain experts, citing
   GAP-{slug} by name) and `orthogonality to ANCHOR-CARD` fields
3. CROSS-CARD UNIQUENESS SCAN run with Phase 0 (Enumerate All Verify Questions),
   Phase 1 (Anchor-Orthogonality), and Phase 2 (Non-Anchor Pairwise) — per-role records
   written for Phase 1 and Phase 2
4. One `.md` file per role; inertia-advocate (ANCHOR-CARD) written first
5. ANCHOR-CARD YAML: `anchor: true`; NO `orthogonality`; NO `inertia_gap_inherited`
6. Non-anchor YAML: `orthogonality` field per [FC-11] REQUIRED FORMAT — not generic
7. Domain expert YAML: `inertia_gap_inherited` field per [FC-12] citing GAP-{slug} — not
   positional-only
8. All YAML files use exact identifiers `verify_questions` and `simplify_rules` verbatim
9. No prohibited names per [FC-1]; no collaborates_with CONTRACT VIOLATION

---

PHASE 6 — REGISTRY SUMMARY

**PREPARE:** Enumerate `.md` files written in Phase 5. Record as `PHASE5_COUNT`.
This count must come from Phase 5 enumeration only — not from adding prior-phase
planned counts. Count-bypass failure applies.

PREPARE complete when `PHASE5_COUNT` recorded from Phase 5 enumeration.

**WRITE:** `.craft/roles/{area}/REGISTRY.md`:

```
---
area: {area — from Phase 2 GAP Domain vocabulary}
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
    gap_source: GAP-{slug} from INERTIA-GAP ANALYSIS
    inertia_gap: {GAP-{slug} inertia resistance — copied verbatim}
  (one entry per derived expert)

coverage_gaps: |
  {Phase 2 gaps not addressed by any derived expert; or "none detected."}

inertia_surface: |
  {Phase 1 status-quo claim verbatim. This fulfills the EXTENSION-COMMITMENT from Phase 0.}

Generated by: /org-roles {topic} — {date}
```

HEADING STUB FAIL CONDITION: Section headers with empty or omitted values beneath them
fail C-10. Every field must contain substantive content.

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.craft/roles/{area}/REGISTRY.md`
2. `total_roles` equals `PHASE5_COUNT` from Phase 5 enumeration
3. `domain_experts` lists each expert with `name`, `gap_source` (GAP-{slug}),
   `inertia_gap` (verbatim)
4. `inertia_surface` contains Phase 1 status-quo claim verbatim
5. No heading stubs; HEADING STUB FAIL CONDITION was read before writing began

---

## V-02 — Single-Axis: Named Revision Phase (C-43 target)

**axis:** lifecycle emphasis
**hypothesis:** R9 V-04 fails C-43 because the resolution instruction ("Revise all flagged
questions. Record resolution before YAML writing begins") is embedded inside Phase 2 —
Non-Anchor Pairwise Check as a trailing sentence, not a separately labeled phase. This variate
keeps the Phase 1/Phase 2 split from V-04 exactly (enumeration remains inside Phase 1), but
promotes the revision step to "Phase 3 — Revision and Resolution" at the same structural level
as Phase 1 and Phase 2. Isolates C-43 without C-42. Expected outcome: C-43 PASS, C-42 FAIL
(Phase 1 still subsumes enumeration and anchor-orthogonality under one header), C-38 PARTIAL
(has three named phases including revision but enumeration is not standalone). All other R9
V-04 criteria unchanged.
Falsifiable: if the evaluator scores C-38 as PASS when any three phases are named (including
a revision phase), the C-38 PARTIAL may not hold — but the primary test is C-43 isolation.

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
          The name must derive from the vocabulary of the named GAP-{slug} entry in Phase 2.
          POSITIVE SOURCING REQUIRED: each expert name must cite the specific GAP-{slug}
            identifier and the Domain vocabulary term used in the name.
          BAD:  "domain-expert" (no domain content; no traceable gap source)
          GOOD: "retry-budget-compliance-analyst" — derived from GAP-retry-semantics,
                term "retry-budget" from Domain vocabulary

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
          type: list; minimum two items; uniqueness argument required before writing

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

  [FC-11] orthogonality
          Applies to: all non-anchor YAML files (omit from inertia-advocate ANCHOR-CARD)
          type: string — named contrast axis tracing this role's concern to its
            divergence from the ANCHOR-CARD primary verify question
          REQUIRED: must appear in the YAML output file, not only in the Diagnosis Card
          REQUIRED FORMAT: "[Named contrast axis] — this role's lens diverges from the
            ANCHOR-CARD because [specific reason naming the anchor's question and how
            this role's concern falls outside that question's scope]"
          FAILURE MODE: generic assertion not tracing to the anchor question

  [FC-12] inertia_gap_inherited
          Applies to: domain expert YAML files only
          type: string — provenance field tracing this role's inertia gap to a named
            GAP-{slug} entry in Phase 2 INERTIA-GAP ANALYSIS
          REQUIRED: must appear in the YAML output file, not only in the Diagnosis Card
          REQUIRED FORMAT: "GAP-{slug}: [inertia resistance copied verbatim from
            INERTIA-GAP ANALYSIS]"
          FAILURE MODE: positional reference only ("Gap 1: ...") — fails [FC-12]
          NOTE: GAP-{slug} identifier must match exactly the identifier assigned in Phase 2
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT: all three elements present; `field_name` = `inertia_surface`
2. FIELD-CONTRACT written with all twelve items [FC-1] through [FC-12]
3. [FC-1] contains both PROHIBITED NAMES clause and POSITIVE SOURCING REQUIRED clause
4. [FC-4] and [FC-5] display exact identifier strings `verify_questions` and
   `simplify_rules` under EXACT IDENTIFIER labels — both appear verbatim
5. [FC-11] written with REQUIRED and REQUIRED FORMAT; states YAML persistence
6. [FC-12] written with REQUIRED and REQUIRED FORMAT citing GAP-{slug}; states YAML
   persistence and that positional-only reference fails

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
1. INERTIA-SURFACE block written with status-quo claim naming a specific capability
2. At least three challenge questions using `{topic}` vocabulary
3. No domain expert names appear

---

PHASE 2 — DOMAIN ANALYSIS (named-identifier gap-first derivation)

Read `{topic}` context for concerns the Phase 1 status-quo claim does not address.

**Step 1 — INERTIA-GAP ANALYSIS with formal named identifiers:**
Before naming any domain expert, identify gaps and assign each a formal GAP-{slug}
identifier derived from that gap's Domain vocabulary. DO NOT name experts in Step 1.

```
INERTIA-GAP ANALYSIS for {topic}:

  GAP-{domain-slug-1}:
    Domain: [named vocabulary domain for this gap]
    Failure mode: [specific failure the status quo cannot prevent]
    Inertia resistance: [what the Phase 1 inertia claim overlooks from this domain]

  GAP-{domain-slug-2}:
    Domain: [...]
    Failure mode: [...]
    Inertia resistance: [...]

  GAP-{domain-slug-3}:
    Domain: [...]
    Failure mode: [...]
    Inertia resistance: [...]

  (minimum three named gaps; GAP-{slug} identifier must derive from Domain vocabulary)
```

Expert names must derive from GAP-{slug} Domain vocabulary. PROHIBITED by [FC-1]:
"domain-expert", "expert-1", "generic-expert", "role-1".

**Step 2 — EXPERT DERIVATION with positive sourcing:**

```
DOMAIN-ANALYSIS for {topic}:

  Domain experts derived from INERTIA-GAP ANALYSIS:
    - Expert name: [slug from GAP-{slug} Domain vocabulary]
      POSITIVE SOURCING: "this name derives from GAP-{slug} Domain vocabulary:
        [specific term from that vocabulary used in the name]"
      Named gap source: GAP-{slug} from INERTIA-GAP ANALYSIS
      Inertia gap: [GAP-{slug} inertia resistance — copied verbatim]
      Domain-vocabulary frame: [per [FC-2] using GAP-{slug} vocabulary]
      Verify focus: [what artifact or behavior this expert checks first]
    (one entry per named gap — at minimum one)
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 2.

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. INERTIA-GAP ANALYSIS written before DOMAIN-ANALYSIS; at least three named gaps
   in GAP-{slug} format, each with Domain, Failure mode, Inertia resistance
2. GAP-{slug} identifiers derive from their respective Domain vocabularies
3. Each derived expert lists all five attributes including POSITIVE SOURCING statement
4. POSITIVE SOURCING statement cites specific GAP-{slug} and domain vocabulary term used
5. No placeholder names; no stock role names

---

PHASE 3 — STOCK ROLES

```
STOCK-ROLES:
  - inertia-advocate  (status-quo challenge lens — ANCHOR-CARD for this registry;
                       orientation.frame anchors to Phase 1 status-quo claim;
                       verify_questions sourced from Phase 1 challenge questions;
                       Diagnosis Card written FIRST in Phase 5; YAML written FIRST;
                       carries `anchor: true`; does NOT carry `orthogonality` or
                       `inertia_gap_inherited`)
  - pm                (product value and user outcome lens)
  - architect         (technical structure and system boundary lens)
  - strategy          (business model and competitive position lens)
```

All non-anchor roles carry `orthogonality` per [FC-11] in their YAML files.
Domain expert roles carry `inertia_gap_inherited` per [FC-12] in their YAML files.

**GATE** — Phase 3 complete when ALL of the following are TRUE:
1. STOCK-ROLES lists all four names with lens descriptors
2. inertia-advocate explicitly designated ANCHOR-CARD with write-first mandate for Phase 5
3. [FC-11] and [FC-12] field assignments confirmed for respective role types
4. Phase 1 INERTIA-SURFACE confirmed available as source

---

PHASE 4 — OUTPUT AREA

```
OUTPUT-AREA: .craft/roles/{area}/
```

Area slug uses GAP-{slug} Domain vocabulary from Phase 2. NOT: `default`, `generic`, `roles`.

**GATE** — Phase 4 complete when ALL of the following are TRUE:
1. OUTPUT-AREA written with area slug from Phase 2 GAP Domain vocabulary
2. Path format is exactly `.craft/roles/{area}/`

---

PHASE 5 — DIAGNOSIS CARDS AND ROLE FILE WRITING

**PREPARE:** Confirm inputs before writing any Diagnosis Card:
- Phase 0 [FC-4] exact identifier: `verify_questions` (retrieve verbatim)
- Phase 0 [FC-5] exact identifier: `simplify_rules` (retrieve verbatim)
- Phase 0 [FC-11] REQUIRED FORMAT for `orthogonality` YAML field (retrieve verbatim)
- Phase 0 [FC-12] REQUIRED FORMAT for `inertia_gap_inherited` YAML field (retrieve verbatim)
- Phase 1 INERTIA-SURFACE: status-quo claim and challenge questions confirmed
- Phase 2 INERTIA-GAP ANALYSIS: all GAP-{slug} entries with Domain and Inertia resistance
- Phase 2 DOMAIN-ANALYSIS: expert names with POSITIVE SOURCING confirmed
- Phase 3 STOCK-ROLES: four names; inertia-advocate ANCHOR-CARD confirmed
- Phase 4 OUTPUT-AREA path confirmed

PREPARE complete when all nine inputs confirmed. Do not begin Diagnosis Cards until confirmed.

**ANCHOR-CARD (write first):**

```
ANCHOR-CARD for inertia-advocate:

  name: {domain-vocabulary slug — confirmed against [FC-1]}
  [FC-1] name check: domain-specific because [vocabulary source]; NOT placeholder; confirmed

  frame (one sentence): {Phase 1 status-quo claim as epistemic stance}
  serves (one sentence): {beneficiary — NOT a frame restatement}

  primary_verify_question: {most adversarial "why is the status quo sufficient?" —
    this is the Phase 1 reference axis for the CROSS-CARD UNIQUENESS SCAN}
  uniqueness argument: uniquely attributable to inertia-advocate because [reason];
    confirmed distinct
  anchor status: ANCHOR-CARD — primary question is Phase 1 scan reference axis;
    all non-anchor YAML files carry `orthogonality` tracing to this question

  collaborates_with draft: [{name-1}, {name-2}]; phantom check: confirmed
```

**SUBSEQUENT DIAGNOSIS CARDS (after ANCHOR-CARD):**

```
DIAGNOSIS-CARD for {role-name}:

  name: {for domain experts: from GAP-{slug} Domain vocabulary, POSITIVE SOURCING
         confirmed; confirmed against [FC-1]}
  [FC-1] name check: derives from GAP-{slug} vocabulary: [term used]; NOT placeholder;
    confirmed

  frame (one sentence): {for domain experts: from GAP-{slug} vocabulary;
    for stock roles: standard lens}
  serves (one sentence): {beneficiary — NOT a restatement}

  inertia gap inherited: {for domain experts: "GAP-{slug}: [inertia resistance copied
    verbatim]" — cite by GAP-{slug} name per [FC-12]; for stock roles: N/A}
  orthogonality to ANCHOR-CARD: {per [FC-11] REQUIRED FORMAT — named contrast axis
    tracing how this role's concern falls outside the anchor's sufficiency question;
    this value copied verbatim to YAML `orthogonality` field}

  primary_verify_question: {most role-specific question for this frame}
  uniqueness argument: [reason]; confirmed distinct

  collaborates_with draft: [{name-1}, {name-2}]; phantom check: confirmed
```

After all Diagnosis Cards, run **CROSS-CARD UNIQUENESS SCAN**:

```
CROSS-CARD UNIQUENESS SCAN (ANCHOR-CARD as reference axis):

  Phase 1 — Anchor-Orthogonality Check:
    List ANCHOR-CARD primary_verify_question.
    For each non-anchor role: state its primary_verify_question.
    Test: could this role's question and the anchor question both be asked by the same
      role? If yes, flag.
    Record PASS or FLAG per non-anchor role.

  Phase 2 — Non-Anchor Pairwise Check:
    For each pair of non-anchor roles: compare primary_verify_questions.
    Test: could both questions be asked by the same role type?
    Flag any pair where both questions serve the same epistemic purpose.
    Record PASS or FLAG per pair.

  Phase 3 — Revision and Resolution:
    Collect all flags from Phase 1 and Phase 2.
    For each flagged role or pair:
      Rewrite the flagged primary_verify_question to remove the overlap.
      Record the revised question and the reason it is now distinct.
    Phase 3 complete when all flags are resolved and revisions are recorded.
    Do not write any YAML file until Phase 3 is complete.
```

**WRITE:** One `.md` file per role. Order: inertia-advocate (ANCHOR-CARD) first, then
domain experts, then remaining stock roles.

```yaml
---
name: {per Diagnosis Card — [FC-1] positive sourcing confirmed}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

# ANCHOR-CARD field (inertia-advocate only):
anchor: true   # omit from non-anchor roles

# Non-anchor roles only (omit from inertia-advocate):
orthogonality: "{per [FC-11] REQUIRED FORMAT — named contrast axis from Diagnosis Card;
  not generic; traces to ANCHOR-CARD primary question}"

# Domain expert roles only (omit from stock roles and inertia-advocate):
inertia_gap_inherited: "{per [FC-12] REQUIRED FORMAT: GAP-{slug}: [resistance verbatim]}"

orientation:
  frame: |
    {Per [FC-2]. FAILURE MODE: task-list frame.}
  serves: |
    {Per [FC-3] — NOT a frame restatement.}

lens:
  verify_questions:
    - "{Primary verify question — uniqueness confirmed}"
    - "{Additional question per [FC-4]}"

  simplify_rules:
    - "{Per [FC-5]: opinionated exclusion — 'Skip X unless Y.'}"

expertise:
  depth: {per [FC-6]}
  relevance: |
    {Per [FC-7]: domain-specific.}

scope:
  primary: |
    {Per [FC-8]: one sentence.}
  boundary: |
    {Per [FC-9]: explicit exclusion, one sentence.}

collaborates_with:
  - {per Diagnosis Card — phantom check confirmed}
  # CONTRACT VIOLATION (type 1) — PHANTOM
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST
```

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. ANCHOR-CARD Diagnosis Card written first; all subsequent cards written after
2. All subsequent Diagnosis Cards include `inertia gap inherited` (domain experts, citing
   GAP-{slug} by name) and `orthogonality to ANCHOR-CARD` fields
3. CROSS-CARD UNIQUENESS SCAN run with Phase 1 (Anchor-Orthogonality), Phase 2
   (Non-Anchor Pairwise), and Phase 3 (Revision and Resolution) — per-role records
   written; Phase 3 confirmed complete before YAML writing began
4. One `.md` file per role; inertia-advocate (ANCHOR-CARD) written first
5. ANCHOR-CARD YAML: `anchor: true`; NO `orthogonality`; NO `inertia_gap_inherited`
6. Non-anchor YAML: `orthogonality` field per [FC-11] REQUIRED FORMAT — not generic
7. Domain expert YAML: `inertia_gap_inherited` field per [FC-12] citing GAP-{slug} — not
   positional-only
8. All YAML files use exact identifiers `verify_questions` and `simplify_rules` verbatim
9. No prohibited names per [FC-1]; no collaborates_with CONTRACT VIOLATION

---

PHASE 6 — REGISTRY SUMMARY

**PREPARE:** Enumerate `.md` files written in Phase 5. Record as `PHASE5_COUNT`.
This count must come from Phase 5 enumeration only — not from adding prior-phase
planned counts. Count-bypass failure applies.

PREPARE complete when `PHASE5_COUNT` recorded from Phase 5 enumeration.

**WRITE:** `.craft/roles/{area}/REGISTRY.md`:

```
---
area: {area — from Phase 2 GAP Domain vocabulary}
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
    gap_source: GAP-{slug} from INERTIA-GAP ANALYSIS
    inertia_gap: {GAP-{slug} inertia resistance — copied verbatim}
  (one entry per derived expert)

coverage_gaps: |
  {Phase 2 gaps not addressed by any derived expert; or "none detected."}

inertia_surface: |
  {Phase 1 status-quo claim verbatim. This fulfills the EXTENSION-COMMITMENT from Phase 0.}

Generated by: /org-roles {topic} — {date}
```

HEADING STUB FAIL CONDITION: Section headers with empty or omitted values beneath them
fail C-10. Every field must contain substantive content.

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.craft/roles/{area}/REGISTRY.md`
2. `total_roles` equals `PHASE5_COUNT` from Phase 5 enumeration
3. `domain_experts` lists each expert with `name`, `gap_source` (GAP-{slug}),
   `inertia_gap` (verbatim)
4. `inertia_surface` contains Phase 1 status-quo claim verbatim
5. No heading stubs; HEADING STUB FAIL CONDITION was read before writing began

---

## V-03 — Single-Axis: Four-Phase Scan (C-42 + C-43 combined, minimal surrounding change)

**axis:** lifecycle emphasis
**hypothesis:** V-01 and V-02 isolate C-42 and C-43 respectively. V-03 combines both in the
scan section — restructuring into four named phases (Enumerate / Anchor-Orthogonality /
Non-Anchor Pairwise / Revision-Resolution) — while keeping every other aspect of the prompt
identical to R9 V-04. This should deliver C-42 PASS, C-43 PASS, C-38 PASS (now four named
phases including standalone enumeration and standalone revision), while all other criteria
remain at R9 V-04 levels. Expected score: 38/39 or 39/39 depending on whether C-38 PASS
requires exactly "three" phases or "at least three". The minimal change isolates the scan
restructuring as the only variable; no Phase 0 label change (enumeration is Phase 1 of the
scan, not Phase 0 of the outer pipeline), preserving the outer phase numbering.
Falsifiable: if C-38 still reads PARTIAL (rubric wording says "at least three named phases"
— four named phases should PASS), the rubric's PARTIAL condition for C-38 is reading
something else.

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
          The name must derive from the vocabulary of the named GAP-{slug} entry in Phase 2.
          POSITIVE SOURCING REQUIRED: each expert name must cite the specific GAP-{slug}
            identifier and the Domain vocabulary term used in the name.
          BAD:  "domain-expert" (no domain content; no traceable gap source)
          GOOD: "retry-budget-compliance-analyst" — derived from GAP-retry-semantics,
                term "retry-budget" from Domain vocabulary

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
          type: list; minimum two items; uniqueness argument required before writing

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

  [FC-11] orthogonality
          Applies to: all non-anchor YAML files (omit from inertia-advocate ANCHOR-CARD)
          type: string — named contrast axis tracing this role's concern to its
            divergence from the ANCHOR-CARD primary verify question
          REQUIRED: must appear in the YAML output file, not only in the Diagnosis Card
          REQUIRED FORMAT: "[Named contrast axis] — this role's lens diverges from the
            ANCHOR-CARD because [specific reason naming the anchor's question and how
            this role's concern falls outside that question's scope]"
          FAILURE MODE: generic assertion not tracing to the anchor question

  [FC-12] inertia_gap_inherited
          Applies to: domain expert YAML files only
          type: string — provenance field tracing this role's inertia gap to a named
            GAP-{slug} entry in Phase 2 INERTIA-GAP ANALYSIS
          REQUIRED: must appear in the YAML output file, not only in the Diagnosis Card
          REQUIRED FORMAT: "GAP-{slug}: [inertia resistance copied verbatim from
            INERTIA-GAP ANALYSIS]"
          FAILURE MODE: positional reference only ("Gap 1: ...") — fails [FC-12]
          NOTE: GAP-{slug} identifier must match exactly the identifier assigned in Phase 2
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT: all three elements present; `field_name` = `inertia_surface`
2. FIELD-CONTRACT written with all twelve items [FC-1] through [FC-12]
3. [FC-1] contains both PROHIBITED NAMES clause and POSITIVE SOURCING REQUIRED clause
4. [FC-4] and [FC-5] display exact identifier strings `verify_questions` and
   `simplify_rules` under EXACT IDENTIFIER labels — both appear verbatim
5. [FC-11] written with REQUIRED and REQUIRED FORMAT; states YAML persistence
6. [FC-12] written with REQUIRED and REQUIRED FORMAT citing GAP-{slug}; states YAML
   persistence and that positional-only reference fails

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
1. INERTIA-SURFACE block written with status-quo claim naming a specific capability
2. At least three challenge questions using `{topic}` vocabulary
3. No domain expert names appear

---

PHASE 2 — DOMAIN ANALYSIS (named-identifier gap-first derivation)

Read `{topic}` context for concerns the Phase 1 status-quo claim does not address.

**Step 1 — INERTIA-GAP ANALYSIS with formal named identifiers:**
Before naming any domain expert, identify gaps and assign each a formal GAP-{slug}
identifier derived from that gap's Domain vocabulary. DO NOT name experts in Step 1.

```
INERTIA-GAP ANALYSIS for {topic}:

  GAP-{domain-slug-1}:
    Domain: [named vocabulary domain for this gap]
    Failure mode: [specific failure the status quo cannot prevent]
    Inertia resistance: [what the Phase 1 inertia claim overlooks from this domain]

  GAP-{domain-slug-2}:
    Domain: [...]
    Failure mode: [...]
    Inertia resistance: [...]

  GAP-{domain-slug-3}:
    Domain: [...]
    Failure mode: [...]
    Inertia resistance: [...]

  (minimum three named gaps; GAP-{slug} identifier must derive from Domain vocabulary)
```

Expert names must derive from GAP-{slug} Domain vocabulary. PROHIBITED by [FC-1]:
"domain-expert", "expert-1", "generic-expert", "role-1".

**Step 2 — EXPERT DERIVATION with positive sourcing:**

```
DOMAIN-ANALYSIS for {topic}:

  Domain experts derived from INERTIA-GAP ANALYSIS:
    - Expert name: [slug from GAP-{slug} Domain vocabulary]
      POSITIVE SOURCING: "this name derives from GAP-{slug} Domain vocabulary:
        [specific term from that vocabulary used in the name]"
      Named gap source: GAP-{slug} from INERTIA-GAP ANALYSIS
      Inertia gap: [GAP-{slug} inertia resistance — copied verbatim]
      Domain-vocabulary frame: [per [FC-2] using GAP-{slug} vocabulary]
      Verify focus: [what artifact or behavior this expert checks first]
    (one entry per named gap — at minimum one)
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 2.

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. INERTIA-GAP ANALYSIS written before DOMAIN-ANALYSIS; at least three named gaps
   in GAP-{slug} format, each with Domain, Failure mode, Inertia resistance
2. GAP-{slug} identifiers derive from their respective Domain vocabularies
3. Each derived expert lists all five attributes including POSITIVE SOURCING statement
4. POSITIVE SOURCING statement cites specific GAP-{slug} and domain vocabulary term used
5. No placeholder names; no stock role names

---

PHASE 3 — STOCK ROLES

```
STOCK-ROLES:
  - inertia-advocate  (status-quo challenge lens — ANCHOR-CARD for this registry;
                       orientation.frame anchors to Phase 1 status-quo claim;
                       verify_questions sourced from Phase 1 challenge questions;
                       Diagnosis Card written FIRST in Phase 5; YAML written FIRST;
                       carries `anchor: true`; does NOT carry `orthogonality` or
                       `inertia_gap_inherited`)
  - pm                (product value and user outcome lens)
  - architect         (technical structure and system boundary lens)
  - strategy          (business model and competitive position lens)
```

All non-anchor roles carry `orthogonality` per [FC-11] in their YAML files.
Domain expert roles carry `inertia_gap_inherited` per [FC-12] in their YAML files.

**GATE** — Phase 3 complete when ALL of the following are TRUE:
1. STOCK-ROLES lists all four names with lens descriptors
2. inertia-advocate explicitly designated ANCHOR-CARD with write-first mandate for Phase 5
3. [FC-11] and [FC-12] field assignments confirmed for respective role types
4. Phase 1 INERTIA-SURFACE confirmed available as source

---

PHASE 4 — OUTPUT AREA

```
OUTPUT-AREA: .craft/roles/{area}/
```

Area slug uses GAP-{slug} Domain vocabulary from Phase 2. NOT: `default`, `generic`, `roles`.

**GATE** — Phase 4 complete when ALL of the following are TRUE:
1. OUTPUT-AREA written with area slug from Phase 2 GAP Domain vocabulary
2. Path format is exactly `.craft/roles/{area}/`

---

PHASE 5 — DIAGNOSIS CARDS AND ROLE FILE WRITING

**PREPARE:** Confirm inputs before writing any Diagnosis Card:
- Phase 0 [FC-4] exact identifier: `verify_questions` (retrieve verbatim)
- Phase 0 [FC-5] exact identifier: `simplify_rules` (retrieve verbatim)
- Phase 0 [FC-11] REQUIRED FORMAT for `orthogonality` YAML field (retrieve verbatim)
- Phase 0 [FC-12] REQUIRED FORMAT for `inertia_gap_inherited` YAML field (retrieve verbatim)
- Phase 1 INERTIA-SURFACE: status-quo claim and challenge questions confirmed
- Phase 2 INERTIA-GAP ANALYSIS: all GAP-{slug} entries with Domain and Inertia resistance
- Phase 2 DOMAIN-ANALYSIS: expert names with POSITIVE SOURCING confirmed
- Phase 3 STOCK-ROLES: four names; inertia-advocate ANCHOR-CARD confirmed
- Phase 4 OUTPUT-AREA path confirmed

PREPARE complete when all nine inputs confirmed. Do not begin Diagnosis Cards until confirmed.

**ANCHOR-CARD (write first):**

```
ANCHOR-CARD for inertia-advocate:

  name: {domain-vocabulary slug — confirmed against [FC-1]}
  [FC-1] name check: domain-specific because [vocabulary source]; NOT placeholder; confirmed

  frame (one sentence): {Phase 1 status-quo claim as epistemic stance}
  serves (one sentence): {beneficiary — NOT a frame restatement}

  primary_verify_question: {most adversarial "why is the status quo sufficient?" —
    this is the Phase 1 reference axis for the CROSS-CARD UNIQUENESS SCAN}
  uniqueness argument: uniquely attributable to inertia-advocate because [reason];
    confirmed distinct
  anchor status: ANCHOR-CARD — primary question is Phase 1 scan reference axis;
    all non-anchor YAML files carry `orthogonality` tracing to this question

  collaborates_with draft: [{name-1}, {name-2}]; phantom check: confirmed
```

**SUBSEQUENT DIAGNOSIS CARDS (after ANCHOR-CARD):**

```
DIAGNOSIS-CARD for {role-name}:

  name: {for domain experts: from GAP-{slug} Domain vocabulary, POSITIVE SOURCING
         confirmed; confirmed against [FC-1]}
  [FC-1] name check: derives from GAP-{slug} vocabulary: [term used]; NOT placeholder;
    confirmed

  frame (one sentence): {for domain experts: from GAP-{slug} vocabulary;
    for stock roles: standard lens}
  serves (one sentence): {beneficiary — NOT a restatement}

  inertia gap inherited: {for domain experts: "GAP-{slug}: [inertia resistance copied
    verbatim]" — cite by GAP-{slug} name per [FC-12]; for stock roles: N/A}
  orthogonality to ANCHOR-CARD: {per [FC-11] REQUIRED FORMAT — named contrast axis
    tracing how this role's concern falls outside the anchor's sufficiency question;
    this value copied verbatim to YAML `orthogonality` field}

  primary_verify_question: {most role-specific question for this frame}
  uniqueness argument: [reason]; confirmed distinct

  collaborates_with draft: [{name-1}, {name-2}]; phantom check: confirmed
```

After all Diagnosis Cards, run **CROSS-CARD UNIQUENESS SCAN**:

```
CROSS-CARD UNIQUENESS SCAN (ANCHOR-CARD as reference axis):

  Phase 1 — Enumerate All Verify Questions:
    List every primary_verify_question from every Diagnosis Card (ANCHOR-CARD first,
      then non-anchor cards in the order they were written).
    Format: [role-name]: "[question text]"
    Scope: enumeration only — no checking, no flagging in this phase.
    Phase 1 complete when every card's primary question appears exactly once in the list.

  Phase 2 — Anchor-Orthogonality Check:
    Using Phase 1 enumeration as the reference list:
    State the ANCHOR-CARD primary_verify_question (from Phase 1).
    For each non-anchor role: retrieve its question from Phase 1.
    Test: could this role's question and the anchor question both be asked by the same
      role? If yes, flag.
    Record PASS or FLAG per non-anchor role.
    Do not begin Phase 3 until all Phase 2 records are written.

  Phase 3 — Non-Anchor Pairwise Check:
    Using Phase 1 enumeration (non-anchor entries only) as reference:
    For each pair of non-anchor roles: compare primary_verify_questions.
    Test: could both questions be asked by the same role type?
    Flag any pair where both questions serve the same epistemic purpose.
    Record PASS or FLAG per pair.
    Do not begin Phase 4 until all Phase 3 records are written.

  Phase 4 — Revision and Resolution:
    Collect all flags from Phase 2 and Phase 3.
    For each flagged role or pair:
      Rewrite the flagged primary_verify_question to remove the overlap.
      Record the revised question and the reason it is now distinct.
    Phase 4 complete when all flags are resolved and revisions are recorded.
    Do not write any YAML file until Phase 4 is complete.
```

**WRITE:** One `.md` file per role. Order: inertia-advocate (ANCHOR-CARD) first, then
domain experts, then remaining stock roles.

```yaml
---
name: {per Diagnosis Card — [FC-1] positive sourcing confirmed}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

# ANCHOR-CARD field (inertia-advocate only):
anchor: true   # omit from non-anchor roles

# Non-anchor roles only (omit from inertia-advocate):
orthogonality: "{per [FC-11] REQUIRED FORMAT — named contrast axis from Diagnosis Card;
  not generic; traces to ANCHOR-CARD primary question}"

# Domain expert roles only (omit from stock roles and inertia-advocate):
inertia_gap_inherited: "{per [FC-12] REQUIRED FORMAT: GAP-{slug}: [resistance verbatim]}"

orientation:
  frame: |
    {Per [FC-2]. FAILURE MODE: task-list frame.}
  serves: |
    {Per [FC-3] — NOT a frame restatement.}

lens:
  verify_questions:
    - "{Primary verify question — uniqueness confirmed}"
    - "{Additional question per [FC-4]}"

  simplify_rules:
    - "{Per [FC-5]: opinionated exclusion — 'Skip X unless Y.'}"

expertise:
  depth: {per [FC-6]}
  relevance: |
    {Per [FC-7]: domain-specific.}

scope:
  primary: |
    {Per [FC-8]: one sentence.}
  boundary: |
    {Per [FC-9]: explicit exclusion, one sentence.}

collaborates_with:
  - {per Diagnosis Card — phantom check confirmed}
  # CONTRACT VIOLATION (type 1) — PHANTOM
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST
```

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. ANCHOR-CARD Diagnosis Card written first; all subsequent cards written after
2. All subsequent Diagnosis Cards include `inertia gap inherited` (domain experts, citing
   GAP-{slug} by name) and `orthogonality to ANCHOR-CARD` fields
3. CROSS-CARD UNIQUENESS SCAN run with Phase 1 (Enumerate All Verify Questions),
   Phase 2 (Anchor-Orthogonality), Phase 3 (Non-Anchor Pairwise), and Phase 4
   (Revision and Resolution) — per-role records written; Phase 4 confirmed complete
   before YAML writing began
4. One `.md` file per role; inertia-advocate (ANCHOR-CARD) written first
5. ANCHOR-CARD YAML: `anchor: true`; NO `orthogonality`; NO `inertia_gap_inherited`
6. Non-anchor YAML: `orthogonality` field per [FC-11] REQUIRED FORMAT — not generic
7. Domain expert YAML: `inertia_gap_inherited` field per [FC-12] citing GAP-{slug} — not
   positional-only
8. All YAML files use exact identifiers `verify_questions` and `simplify_rules` verbatim
9. No prohibited names per [FC-1]; no collaborates_with CONTRACT VIOLATION

---

PHASE 6 — REGISTRY SUMMARY

**PREPARE:** Enumerate `.md` files written in Phase 5. Record as `PHASE5_COUNT`.
This count must come from Phase 5 enumeration only — not from adding prior-phase
planned counts. Count-bypass failure applies.

PREPARE complete when `PHASE5_COUNT` recorded from Phase 5 enumeration.

**WRITE:** `.craft/roles/{area}/REGISTRY.md`:

```
---
area: {area — from Phase 2 GAP Domain vocabulary}
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
    gap_source: GAP-{slug} from INERTIA-GAP ANALYSIS
    inertia_gap: {GAP-{slug} inertia resistance — copied verbatim}
  (one entry per derived expert)

coverage_gaps: |
  {Phase 2 gaps not addressed by any derived expert; or "none detected."}

inertia_surface: |
  {Phase 1 status-quo claim verbatim. This fulfills the EXTENSION-COMMITMENT from Phase 0.}

Generated by: /org-roles {topic} — {date}
```

HEADING STUB FAIL CONDITION: Section headers with empty or omitted values beneath them
fail C-10. Every field must contain substantive content.

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.craft/roles/{area}/REGISTRY.md`
2. `total_roles` equals `PHASE5_COUNT` from Phase 5 enumeration
3. `domain_experts` lists each expert with `name`, `gap_source` (GAP-{slug}),
   `inertia_gap` (verbatim)
4. `inertia_surface` contains Phase 1 status-quo claim verbatim
5. No heading stubs; HEADING STUB FAIL CONDITION was read before writing began

---

## V-04 — Combined: Full Pipeline + Four-Phase Scan (target 39/39 = 100.00)

**axis:** all axes combined (inertia-framing + role-sequence + output-format + lifecycle emphasis)
**hypothesis:** R9 V-04 scores 99.36 under v10. It fails only C-42 (enumeration embedded in
Phase 1 Anchor-Orthogonality Check) and C-43 (resolution not labeled as a named phase). V-03
demonstrated the 4-phase scan in isolation. This variate applies the identical 4-phase scan
to V-04's complete pipeline: ANCHOR-CARD designation + phase-decomposed scan with ANCHOR-CARD
as reference axis + named GAP-{slug} identifiers + per-expert POSITIVE SOURCING inline records
+ YAML `orthogonality` persistence + YAML `inertia_gap_inherited` persistence. The 4-phase scan
additionally upgrades C-38 from PARTIAL to PASS (rubric requires "at least three named phases"
including enumeration and a revision step — four phases satisfies both conditions). Expected
score: 39/39 = 100.00. Falsifiable: if C-09 (role differentiation) degrades because the
combination of ANCHOR-CARD ordering + named-gap tracing + YAML persistence produces over-
specified expert frames that converge toward the inertia-advocate's concern rather than
expressing independent epistemic viewpoints, the full-pipeline compliance gain comes at a
role-differentiation accuracy cost.

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
          The name must derive from the vocabulary of the named GAP-{slug} entry in Phase 2.
          POSITIVE SOURCING REQUIRED: each expert name must cite the specific GAP-{slug}
            identifier and the Domain vocabulary term used in the name.
          BAD:  "domain-expert" (no domain content; no traceable gap source)
          GOOD: "retry-budget-compliance-analyst" — derived from GAP-retry-semantics,
                term "retry-budget" from Domain vocabulary

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
          type: list; minimum two items; uniqueness argument required before writing

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

  [FC-11] orthogonality
          Applies to: all non-anchor YAML files (omit from inertia-advocate ANCHOR-CARD)
          type: string — named contrast axis tracing this role's concern to its
            divergence from the ANCHOR-CARD primary verify question
          REQUIRED: must appear in the YAML output file, not only in the Diagnosis Card
          REQUIRED FORMAT: "[Named contrast axis] — this role's lens diverges from the
            ANCHOR-CARD because [specific reason naming the anchor's question and how
            this role's concern falls outside that question's scope]"
          FAILURE MODE: generic assertion not tracing to the anchor question

  [FC-12] inertia_gap_inherited
          Applies to: domain expert YAML files only
          type: string — provenance field tracing this role's inertia gap to a named
            GAP-{slug} entry in Phase 2 INERTIA-GAP ANALYSIS
          REQUIRED: must appear in the YAML output file, not only in the Diagnosis Card
          REQUIRED FORMAT: "GAP-{slug}: [inertia resistance copied verbatim from
            INERTIA-GAP ANALYSIS]"
          FAILURE MODE: positional reference only ("Gap 1: ...") — fails [FC-12]
          NOTE: GAP-{slug} identifier must match exactly the identifier assigned in Phase 2
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT: all three elements present; `field_name` = `inertia_surface`
2. FIELD-CONTRACT written with all twelve items [FC-1] through [FC-12]
3. [FC-1] contains both PROHIBITED NAMES clause and POSITIVE SOURCING REQUIRED clause
4. [FC-4] and [FC-5] display exact identifier strings `verify_questions` and
   `simplify_rules` under EXACT IDENTIFIER labels — both appear verbatim
5. [FC-11] written with REQUIRED and REQUIRED FORMAT; states YAML persistence
6. [FC-12] written with REQUIRED and REQUIRED FORMAT citing GAP-{slug}; states YAML
   persistence and that positional-only reference fails

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
1. INERTIA-SURFACE block written with status-quo claim naming a specific capability
2. At least three challenge questions using `{topic}` vocabulary
3. No domain expert names appear

---

PHASE 2 — DOMAIN ANALYSIS (named-identifier gap-first derivation)

Read `{topic}` context for concerns the Phase 1 status-quo claim does not address.

**Step 1 — INERTIA-GAP ANALYSIS with formal named identifiers:**
Before naming any domain expert, identify gaps and assign each a formal GAP-{slug}
identifier derived from that gap's Domain vocabulary. DO NOT name experts in Step 1.

```
INERTIA-GAP ANALYSIS for {topic}:

  GAP-{domain-slug-1}:
    Domain: [named vocabulary domain for this gap]
    Failure mode: [specific failure the status quo cannot prevent]
    Inertia resistance: [what the Phase 1 inertia claim overlooks from this domain]

  GAP-{domain-slug-2}:
    Domain: [...]
    Failure mode: [...]
    Inertia resistance: [...]

  GAP-{domain-slug-3}:
    Domain: [...]
    Failure mode: [...]
    Inertia resistance: [...]

  (minimum three named gaps; GAP-{slug} identifier must derive from Domain vocabulary)
```

Expert names must derive from GAP-{slug} Domain vocabulary. PROHIBITED by [FC-1]:
"domain-expert", "expert-1", "generic-expert", "role-1".

**Step 2 — EXPERT DERIVATION with positive sourcing:**

```
DOMAIN-ANALYSIS for {topic}:

  Domain experts derived from INERTIA-GAP ANALYSIS:
    - Expert name: [slug from GAP-{slug} Domain vocabulary]
      POSITIVE SOURCING: "this name derives from GAP-{slug} Domain vocabulary:
        [specific term from that vocabulary used in the name]"
      Named gap source: GAP-{slug} from INERTIA-GAP ANALYSIS
      Inertia gap: [GAP-{slug} inertia resistance — copied verbatim]
      Domain-vocabulary frame: [per [FC-2] using GAP-{slug} vocabulary]
      Verify focus: [what artifact or behavior this expert checks first]
    (one entry per named gap — at minimum one)
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 2.

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. INERTIA-GAP ANALYSIS written before DOMAIN-ANALYSIS; at least three named gaps
   in GAP-{slug} format, each with Domain, Failure mode, Inertia resistance
2. GAP-{slug} identifiers derive from their respective Domain vocabularies
3. Each derived expert lists all five attributes including POSITIVE SOURCING statement
4. POSITIVE SOURCING statement cites specific GAP-{slug} and domain vocabulary term used
5. No placeholder names; no stock role names

---

PHASE 3 — STOCK ROLES

```
STOCK-ROLES:
  - inertia-advocate  (status-quo challenge lens — ANCHOR-CARD for this registry;
                       orientation.frame anchors to Phase 1 status-quo claim;
                       verify_questions sourced from Phase 1 challenge questions;
                       Diagnosis Card written FIRST in Phase 5; YAML written FIRST;
                       carries `anchor: true`; does NOT carry `orthogonality` or
                       `inertia_gap_inherited`)
  - pm                (product value and user outcome lens)
  - architect         (technical structure and system boundary lens)
  - strategy          (business model and competitive position lens)
```

All non-anchor roles carry `orthogonality` per [FC-11] in their YAML files.
Domain expert roles carry `inertia_gap_inherited` per [FC-12] in their YAML files.

**GATE** — Phase 3 complete when ALL of the following are TRUE:
1. STOCK-ROLES lists all four names with lens descriptors
2. inertia-advocate explicitly designated ANCHOR-CARD with write-first mandate for Phase 5
3. [FC-11] and [FC-12] field assignments confirmed for respective role types
4. Phase 1 INERTIA-SURFACE confirmed available as source

---

PHASE 4 — OUTPUT AREA

```
OUTPUT-AREA: .craft/roles/{area}/
```

Area slug uses GAP-{slug} Domain vocabulary from Phase 2. NOT: `default`, `generic`, `roles`.

**GATE** — Phase 4 complete when ALL of the following are TRUE:
1. OUTPUT-AREA written with area slug from Phase 2 GAP Domain vocabulary
2. Path format is exactly `.craft/roles/{area}/`

---

PHASE 5 — DIAGNOSIS CARDS AND ROLE FILE WRITING

**PREPARE:** Confirm inputs before writing any Diagnosis Card:
- Phase 0 [FC-4] exact identifier: `verify_questions` (retrieve verbatim)
- Phase 0 [FC-5] exact identifier: `simplify_rules` (retrieve verbatim)
- Phase 0 [FC-11] REQUIRED FORMAT for `orthogonality` YAML field (retrieve verbatim)
- Phase 0 [FC-12] REQUIRED FORMAT for `inertia_gap_inherited` YAML field (retrieve verbatim)
- Phase 1 INERTIA-SURFACE: status-quo claim and challenge questions confirmed
- Phase 2 INERTIA-GAP ANALYSIS: all GAP-{slug} entries with Domain and Inertia resistance
- Phase 2 DOMAIN-ANALYSIS: expert names with POSITIVE SOURCING confirmed
- Phase 3 STOCK-ROLES: four names; inertia-advocate ANCHOR-CARD confirmed
- Phase 4 OUTPUT-AREA path confirmed

PREPARE complete when all nine inputs confirmed. Do not begin Diagnosis Cards until confirmed.

**ANCHOR-CARD (write first):**

```
ANCHOR-CARD for inertia-advocate:

  name: {domain-vocabulary slug — confirmed against [FC-1]}
  [FC-1] name check: domain-specific because [vocabulary source]; NOT placeholder; confirmed

  frame (one sentence): {Phase 1 status-quo claim as epistemic stance}
  serves (one sentence): {beneficiary — NOT a frame restatement}

  primary_verify_question: {most adversarial "why is the status quo sufficient?" —
    this is the Phase 1 reference axis for the CROSS-CARD UNIQUENESS SCAN}
  uniqueness argument: uniquely attributable to inertia-advocate because [reason];
    confirmed distinct
  anchor status: ANCHOR-CARD — primary question is Phase 1 scan reference axis;
    all non-anchor YAML files carry `orthogonality` tracing to this question

  collaborates_with draft: [{name-1}, {name-2}]; phantom check: confirmed
```

**SUBSEQUENT DIAGNOSIS CARDS (after ANCHOR-CARD):**

```
DIAGNOSIS-CARD for {role-name}:

  name: {for domain experts: from GAP-{slug} Domain vocabulary, POSITIVE SOURCING
         confirmed; confirmed against [FC-1]}
  [FC-1] name check: derives from GAP-{slug} vocabulary: [term used]; NOT placeholder;
    confirmed

  frame (one sentence): {for domain experts: from GAP-{slug} vocabulary;
    for stock roles: standard lens}
  serves (one sentence): {beneficiary — NOT a restatement}

  inertia gap inherited: {for domain experts: "GAP-{slug}: [inertia resistance copied
    verbatim]" — cite by GAP-{slug} name per [FC-12]; for stock roles: N/A}
  orthogonality to ANCHOR-CARD: {per [FC-11] REQUIRED FORMAT — named contrast axis
    tracing how this role's concern falls outside the anchor's sufficiency question;
    this value copied verbatim to YAML `orthogonality` field}

  primary_verify_question: {most role-specific question for this frame}
  uniqueness argument: [reason]; confirmed distinct

  collaborates_with draft: [{name-1}, {name-2}]; phantom check: confirmed
```

After all Diagnosis Cards, run **CROSS-CARD UNIQUENESS SCAN**:

```
CROSS-CARD UNIQUENESS SCAN (ANCHOR-CARD as reference axis):

  Phase 1 — Enumerate All Verify Questions:
    List every primary_verify_question from every Diagnosis Card (ANCHOR-CARD first,
      then non-anchor cards in the order written).
    Format: [role-name]: "[question text]"
    Scope: enumeration only — no checking, no flagging in this phase.
    Phase 1 complete when every card's primary question appears exactly once in the list.

  Phase 2 — Anchor-Orthogonality Check:
    Using Phase 1 enumeration as the reference list:
    State the ANCHOR-CARD primary_verify_question (from Phase 1).
    For each non-anchor role: retrieve its question from Phase 1.
    Test: could this role's question and the anchor question both be asked by the
      same role? If yes, flag.
    Record PASS or FLAG per non-anchor role.
    Do not begin Phase 3 until all Phase 2 records are written.

  Phase 3 — Non-Anchor Pairwise Check:
    Using Phase 1 enumeration (non-anchor entries only):
    For each pair of non-anchor roles: compare primary_verify_questions.
    Test: could both questions be asked by the same role type?
    Flag any pair where both questions serve the same epistemic purpose.
    Record PASS or FLAG per pair.
    Do not begin Phase 4 until all Phase 3 records are written.

  Phase 4 — Revision and Resolution:
    Collect all flags from Phase 2 and Phase 3.
    For each flagged role or pair:
      Rewrite the flagged primary_verify_question to remove the overlap.
      Record the revised question and the reason it is now distinct.
    Phase 4 complete when all flags are resolved and revisions are recorded.
    Do not write any YAML file until Phase 4 is complete and all revisions confirmed.
```

**WRITE:** One `.md` file per role. Order: inertia-advocate (ANCHOR-CARD) first, then
domain experts, then remaining stock roles.

```yaml
---
name: {per Diagnosis Card — [FC-1] positive sourcing confirmed}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

# ANCHOR-CARD field (inertia-advocate only):
anchor: true   # omit from non-anchor roles

# Non-anchor roles only (omit from inertia-advocate):
orthogonality: "{per [FC-11] REQUIRED FORMAT — named contrast axis from Diagnosis Card;
  not generic; traces to ANCHOR-CARD primary question}"

# Domain expert roles only (omit from stock roles and inertia-advocate):
inertia_gap_inherited: "{per [FC-12] REQUIRED FORMAT: GAP-{slug}: [resistance verbatim]}"

orientation:
  frame: |
    {Per [FC-2]. FAILURE MODE: task-list frame.}
  serves: |
    {Per [FC-3] — NOT a frame restatement.}

lens:
  verify_questions:
    - "{Primary verify question — uniqueness confirmed}"
    - "{Additional question per [FC-4]}"

  simplify_rules:
    - "{Per [FC-5]: opinionated exclusion — 'Skip X unless Y.'}"

expertise:
  depth: {per [FC-6]}
  relevance: |
    {Per [FC-7]: domain-specific.}

scope:
  primary: |
    {Per [FC-8]: one sentence.}
  boundary: |
    {Per [FC-9]: explicit exclusion, one sentence.}

collaborates_with:
  - {per Diagnosis Card — phantom check confirmed}
  # CONTRACT VIOLATION (type 1) — PHANTOM
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST
```

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. ANCHOR-CARD Diagnosis Card written first; all subsequent cards written after
2. All subsequent Diagnosis Cards include `inertia gap inherited` (domain experts, citing
   GAP-{slug} by name) and `orthogonality to ANCHOR-CARD` fields
3. CROSS-CARD UNIQUENESS SCAN run with Phase 1 (Enumerate All Verify Questions),
   Phase 2 (Anchor-Orthogonality), Phase 3 (Non-Anchor Pairwise), and Phase 4
   (Revision and Resolution) — per-role records written for Phases 2 and 3; Phase 4
   confirmed complete with all revisions recorded before YAML writing began
4. One `.md` file per role; inertia-advocate (ANCHOR-CARD) written first
5. ANCHOR-CARD YAML: `anchor: true`; NO `orthogonality`; NO `inertia_gap_inherited`
6. Non-anchor YAML: `orthogonality` field per [FC-11] REQUIRED FORMAT — not generic
7. Domain expert YAML: `inertia_gap_inherited` field per [FC-12] citing GAP-{slug} — not
   positional-only
8. All YAML files use exact identifiers `verify_questions` and `simplify_rules` verbatim
9. No prohibited names per [FC-1]; no collaborates_with CONTRACT VIOLATION

---

PHASE 6 — REGISTRY SUMMARY

**PREPARE:** Enumerate `.md` files written in Phase 5. Record as `PHASE5_COUNT`.
This count must come from Phase 5 enumeration only — not from adding prior-phase
planned counts. Count-bypass failure applies.

PREPARE complete when `PHASE5_COUNT` recorded from Phase 5 enumeration.

**WRITE:** `.craft/roles/{area}/REGISTRY.md`:

```
---
area: {area — from Phase 2 GAP Domain vocabulary}
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
    gap_source: GAP-{slug} from INERTIA-GAP ANALYSIS
    inertia_gap: {GAP-{slug} inertia resistance — copied verbatim}
  (one entry per derived expert)

coverage_gaps: |
  {Phase 2 gaps not addressed by any derived expert; or "none detected."}

inertia_surface: |
  {Phase 1 status-quo claim verbatim. This fulfills the EXTENSION-COMMITMENT from Phase 0.}

Generated by: /org-roles {topic} — {date}
```

HEADING STUB FAIL CONDITION: Section headers with empty or omitted values beneath them
fail C-10. Every field must contain substantive content.

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.craft/roles/{area}/REGISTRY.md`
2. `total_roles` equals `PHASE5_COUNT` from Phase 5 enumeration
3. `domain_experts` lists each expert with `name`, `gap_source` (GAP-{slug}),
   `inertia_gap` (verbatim)
4. `inertia_surface` contains Phase 1 status-quo claim verbatim
5. No heading stubs; HEADING STUB FAIL CONDITION was read before writing began

---

## V-05 — Combined (Imperative Register + Regression Recovery): All Axes + Four-Phase Scan

**axis:** all axes, phrasing register
**hypothesis:** R9 V-05 used an imperative/checklist register and scored 99.10 under v10 —
lower than V-04 (99.36) due to two regressions: C-29 PARTIAL (CONTRACT VIOLATION framing
stripped from collaborates_with section in checklist format) and C-33 PARTIAL (same). This
variate takes R9 V-05's imperative structure, adds the 4-phase scan (C-42 + C-43), and
restores the CONTRACT VIOLATION comments explicitly in the per-file write checklist to
recover C-29 and C-33. Expected score: 39/39 = 100.00. Secondary test: whether the
imperative register's per-step checklist produces more reliable gate adherence than V-04's
procedural-block format, or introduces edge-case degradation on field-format criteria
(C-37, C-46, C-47) by replacing extended REQUIRED FORMAT blocks with shorter imperative phrases.
Falsifiable: if checklist brevity re-introduces the C-29/C-33 regression despite the explicit
CONTRACT VIOLATION restoration, the register itself is the cause rather than the framing omission.

---

You are running `/org-roles {topic}`.

Before doing anything else, commit to two things in writing:

**Commit 1 — Extension field:**
Write this block verbatim:
```
EXTENSION-COMMITMENT:
  field_name: inertia_surface
  population_source: Phase 1, INERTIA-SURFACE block, status-quo claim field
  purpose: answers "what is the strongest existing-system argument that makes
    {topic} premature?" for downstream consumers
```

**Commit 2 — Field identifiers:**
Write these identifiers verbatim and confirm you will use them exactly:
- `verify_questions` — the YAML key for the verify list
  (PROHIBITED identifiers that break downstream consumers: verify, questions, checks)
- `simplify_rules` — the YAML key for the simplify list
  (PROHIBITED identifiers that break downstream consumers: simplify, rules, guidelines)
- `orthogonality` — appears in all non-anchor YAML files; names contrast to ANCHOR-CARD;
  REQUIRED FORMAT: "[Named contrast axis] — this role's lens diverges from the ANCHOR-CARD
  because [specific reason naming the anchor's question and how this role's concern falls
  outside that question's scope]"; populate from Diagnosis Card verbatim
- `inertia_gap_inherited` — appears in domain expert YAML files; cites GAP-{slug} by name;
  REQUIRED FORMAT: "GAP-{slug}: [inertia resistance verbatim]"; positional-only ("Gap 1:")
  is a failure
- `anchor: true` — appears in inertia-advocate YAML file only

---

**Step 1 — Name constraints (read before writing any names):**

Every expert name must:
1. Come from the vocabulary of a named GAP-{slug} entry you produce in Step 3
2. Include a positive sourcing statement: "this name derives from GAP-{slug}: [term used]"
3. Be specific enough that it could only appear in this domain's registry

BANNED names that will fail review: "domain-expert", "expert-1", "generic-expert", "role-1"

---

**Step 2 — Inertia surface (read context, no expert naming yet):**

Read `{topic}`. Write:
```
INERTIA-SURFACE for {topic}:
  Status-quo claim: [strongest argument {topic} is unnecessary; name the specific capability]
  Challenge questions:
    Q1: What specific failure does the status quo produce that this resolves?
    Q2: [what does the existing mechanism already handle?]
    Q3: [minimum status-quo fix, and why is it insufficient?]
```

Rules: status-quo claim must name a specific capability. Write at least three questions using
`{topic}` vocabulary. Write no expert names here.

---

**Step 3 — Gap analysis with named identifiers (before naming any expert):**

For each gap the Phase 2 status-quo claim leaves uncovered, assign a formal identifier
`GAP-{domain-slug}` derived from that gap's vocabulary. Write at least three.

```
INERTIA-GAP ANALYSIS for {topic}:
  GAP-{slug-1}:
    Domain: [named vocabulary domain]
    Failure mode: [what the status quo cannot prevent]
    Inertia resistance: [what the inertia-advocate overlooks from this domain]

  GAP-{slug-2}: ...
  GAP-{slug-3}: ...
```

Rules: assign the GAP-{slug} identifier before writing the Domain field. Each slug must
be derivable from its own Domain vocabulary. Write no expert names until this block is done.

---

**Step 4 — Expert derivation from named gaps:**

For each named gap, derive one expert. Write:
```
DOMAIN-ANALYSIS for {topic}:
  - Expert name: [slug from GAP-{slug} vocabulary]
    POSITIVE SOURCING: "this name derives from GAP-{slug}: [specific term used in name]"
    Named gap source: GAP-{slug}
    Inertia gap: [GAP-{slug} inertia resistance — copy verbatim, do not paraphrase]
    Frame: [epistemic viewpoint using GAP-{slug} vocabulary — "sees X through the lens of Y"]
    Verify focus: [what artifact or behavior this expert checks first]
```

Rules: one expert per gap minimum. No PM, Architect, Strategy, or inertia-advocate here.

---

**Step 5 — Confirm output area:**

Write:
```
OUTPUT-AREA: .craft/roles/{area}/
```

Use GAP Domain vocabulary for the area slug. Not: `default`, `generic`, `roles`.

---

**Step 6 — Diagnosis Cards, ANCHOR-CARD first:**

Before writing any YAML file, write one Diagnosis Card per role. Write the inertia-advocate
Diagnosis Card FIRST — it is the ANCHOR-CARD.

**ANCHOR-CARD:**
```
ANCHOR-CARD (inertia-advocate):
  name: [domain-specific slug from Step 2 vocabulary; BANNED: placeholder names]
  Sourcing check: specific because [vocabulary source]; confirmed
  Frame: [Phase 2 status-quo claim as "sees X through the lens of Y"]
  Serves: [beneficiary of the inertia verdict — NOT a restatement of Frame]
  Primary question: [most adversarial "why is the status quo sufficient?" — this is
    the Step 7 Phase 2 reference axis for the CROSS-CARD UNIQUENESS SCAN]
  Uniqueness: [why no other role asks this first]; confirmed distinct
  anchor: ANCHOR-CARD — primary question is the Step 7 Phase 2 reference axis
  Collaborates with: [{name-1}, {name-2}]; phantom check: confirmed
```

**All other Diagnosis Cards** (domain experts and stock roles, written after ANCHOR-CARD):
```
DIAGNOSIS-CARD ({role-name}):
  name: [for experts: from GAP-{slug} vocabulary with POSITIVE SOURCING; for stock: standard]
  Sourcing check: [for experts: "derives from GAP-{slug}: [term]"; for stock: standard]
  Frame: [for experts: from GAP-{slug} vocabulary; for stock: standard lens]
  Serves: [beneficiary — NOT a restatement of Frame]
  Inertia gap inherited: [for experts: "GAP-{slug}: [resistance verbatim]";
    for stock: N/A]
  Orthogonality to ANCHOR-CARD: [named contrast axis — per REQUIRED FORMAT in Commit 2:
    "[Named contrast axis] — this role's lens diverges from the ANCHOR-CARD because
    [specific reason naming the anchor's question and what this role sees that the anchor
    cannot]"; this exact value is copied to YAML `orthogonality` field]
  Primary question: [most role-specific question for this Frame]
  Uniqueness: [why no other role asks this first]; confirmed distinct
  Collaborates with: [{name-1}, {name-2}]; phantom check: confirmed
```

---

**Step 7 — Cross-card scan, four phases, before writing any YAML:**

Run this scan in four named phases. Do not write any YAML file until all four phases pass.

```
CROSS-CARD UNIQUENESS SCAN (ANCHOR-CARD as reference axis):

  Phase 1 — Enumerate All Verify Questions:
    List every primary question from every Diagnosis Card (ANCHOR-CARD first).
    Format: [role-name]: "[question text]"
    Scope: listing only — no checking, no flagging in this phase.
    Complete when every card's primary question appears exactly once.

  Phase 2 — Anchor-Orthogonality Check:
    Using Phase 1 list as reference:
    State the ANCHOR-CARD primary question.
    For each non-anchor role: retrieve its question from Phase 1.
    Could this role's question and the anchor question both be asked by the same role?
    Mark PASS or FLAG per non-anchor role.
    Do not start Phase 3 until Phase 2 is complete.

  Phase 3 — Non-Anchor Pairwise Check:
    Using Phase 1 list (non-anchor entries only):
    For each pair of non-anchor roles: could both questions be asked by the same role type?
    Mark PASS or FLAG per pair.
    Do not start Phase 4 until Phase 3 is complete.

  Phase 4 — Revision and Resolution:
    List all flags from Phase 2 and Phase 3.
    For each flag: rewrite the question; record the revision and why it is now distinct.
    Phase 4 complete when all flags resolved.
    No YAML writing until Phase 4 is complete.
```

---

**Step 8 — Write YAML files (inertia-advocate first):**

Write in order: inertia-advocate, then domain experts, then remaining stock roles.

```yaml
---
name: {from Diagnosis Card; sourcing confirmed}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

# Inertia-advocate ONLY — present only in this file:
anchor: true

# All non-inertia-advocate roles ONLY — present in every other file:
orthogonality: "{from Diagnosis Card 'Orthogonality to ANCHOR-CARD' — copy verbatim;
  must name a contrast axis tracing to ANCHOR-CARD primary question, not be generic}"

# Domain expert roles ONLY — present in expert files, absent from stock and anchor:
inertia_gap_inherited: "{GAP-{slug}: [inertia resistance verbatim from INERTIA-GAP ANALYSIS]}"

orientation:
  frame: |
    {epistemic viewpoint — "sees X through the lens of Y"; not a task list}
  serves: |
    {beneficiary — not a restatement of frame}

lens:
  verify_questions:
    - "{primary question from Diagnosis Card}"
    - "{second question — uniquely attributable to this role's frame}"

  simplify_rules:
    - "{opinionated exclusion: 'Skip X unless Y.' — not a scope description}"

expertise:
  depth: {expert | practitioner | senior | principal}
  relevance: |
    {domain-specific justification — not a restatement of the role name}

scope:
  primary: |
    {main concern, one sentence}
  boundary: |
    {what this role does NOT own, one sentence}

collaborates_with:
  - {registry members only}
  # CONTRACT VIOLATION (type 1) — PHANTOM: a name absent from this registry
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent
```

Checklist before writing each file:
- [ ] `verify_questions` spelled exactly as committed (PROHIBITED: verify, questions, checks)
- [ ] `simplify_rules` spelled exactly as committed (PROHIBITED: simplify, rules, guidelines)
- [ ] `orthogonality` present for all non-anchor roles; absent from ANCHOR-CARD file
- [ ] `inertia_gap_inherited` present for domain expert files; absent from stock/anchor files
- [ ] `anchor: true` present in inertia-advocate file only
- [ ] No PHANTOM names in `collaborates_with` (CONTRACT VIOLATION type 1)
- [ ] No UNIVERSALIST listing in `collaborates_with` (CONTRACT VIOLATION type 2)

---

**Step 9 — Write REGISTRY.md:**

Count the files written in Step 8. Record this as PHASE5_COUNT. Enumerate the actual files
written — do not add up prior-phase counts.

Write `.craft/roles/{area}/REGISTRY.md`:

```
---
area: {area}
generated: {date}
---

## Registry Summary

total_roles: {PHASE5_COUNT}

stock_roles:
  - inertia-advocate  (ANCHOR-CARD — written first; source: Step 2)
  - pm
  - architect
  - strategy

domain_experts:
  - name: {expert-name}
    gap_source: GAP-{slug}
    inertia_gap: {GAP-{slug} inertia resistance — copied verbatim}
  (one entry per expert)

coverage_gaps: |
  {gaps from Step 3 not addressed by any expert; or "none detected"}

inertia_surface: |
  {Step 2 status-quo claim — exact words; fulfills EXTENSION-COMMITMENT}

Generated by: /org-roles {topic} — {date}
```

HEADING STUB RULE: Every field must contain substantive content. A section header with no
real value beneath it fails C-10.

---

**Final checklist — confirm before declaring done:**

Phase output (C-37/C-46): inertia-advocate YAML has `anchor: true`; all other YAML files
have `orthogonality` field with named contrast axis tracing to ANCHOR-CARD primary question

Scan structure (C-38/C-42/C-43): CROSS-CARD UNIQUENESS SCAN ran four named phases —
Phase 1 (Enumerate All Verify Questions), Phase 2 (Anchor-Orthogonality), Phase 3
(Non-Anchor Pairwise), Phase 4 (Revision and Resolution) — per-role records written,
Phase 4 complete before any YAML was written

Gap artifact (C-39/C-44): INERTIA-GAP ANALYSIS block with formal GAP-{slug} identifiers
written before any expert was named in Step 4

Expert sourcing (C-40/C-45): every expert has a POSITIVE SOURCING statement citing the
specific GAP-{slug} identifier and domain vocabulary term used in the name, embedded inline
in the derivation record

Provenance (C-41/C-47): every domain expert Diagnosis Card has `Inertia gap inherited`
citing "GAP-{slug}: [resistance verbatim]"; same value persisted into YAML
`inertia_gap_inherited` field — not positional ("Gap 1")

Contract violations (C-29/C-33): `collaborates_with` section in every YAML file includes
CONTRACT VIOLATION (type 1) — PHANTOM comment and CONTRACT VIOLATION (type 2) —
UNIVERSALIST comment; phantom check confirmed for every collaborates_with list written
