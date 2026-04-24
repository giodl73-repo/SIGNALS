---
skill: quest-variate
skill_target: org-roles
date: 2026-03-16
round: R9
rubric_version: v9
status: variate
---

# org-roles Variate — Round 9

**Date:** 2026-03-16
**Skill:** org-roles
**Rubric:** v9 (C-01 through C-41; new in v9: C-37 ANCHOR-CARD per-YAML orthogonality field,
C-38 phase-decomposed cross-set scan, C-39 INERTIA-GAP ANALYSIS artifact before expert naming,
C-40 expert names from Gap Domain vocabulary, C-41 Diagnosis Card provenance traces to named entry)
**Round:** R9 — single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

---

## Round 9 Variation Map

| V | Axis | Primary C targets | Hypothesis |
|---|------|------------------|------------|
| V-01 | inertia-framing | C-37 PASS, C-38 PASS | Add ANCHOR-CARD designation to Phase 3, `anchor: true` and `orthogonality` fields to YAML schema, and explicitly phase-labeled cross-set scan (Phase 1 Anchor-Orthogonality + Phase 2 Non-Anchor Pairwise) over R8 V-03 gap-first base |
| V-02 | role-sequence | C-40 strengthened, C-41 strengthened | Assign formal named identifiers (GAP-{slug}) to each gap in INERTIA-GAP ANALYSIS; require expert name tracing to cite the GAP identifier by name; require Diagnosis Card provenance field to cite the named gap entry rather than the gap number |
| V-03 | output-format | C-37 partial, C-41 at YAML level | Persist `orthogonality` and `inertia_gap_inherited` in the YAML output files (not only in Diagnosis Cards); add [FC-11] and [FC-12] to Field Contract; gate confirms both fields appear in the written files |
| V-04 | inertia-framing + role-sequence + output-format | C-37 PASS, C-38 PASS, C-39 PASS, C-40 PASS, C-41 PASS | Full synthesis: ANCHOR-CARD first + phase-decomposed scan (V-01) + named GAP identifiers + positive sourcing (V-02) + YAML field persistence (V-03) — all five new criteria simultaneously |
| V-05 | all axes, conversational register | C-37–C-41 PASS, 100.00 target | V-04 content recast in imperative/checklist register; shorter gate conditions; direct imperative phrasing replaces procedural block format; tests whether register affects edge-case criterion satisfaction |

---

## V-01 — Inertia Framing: ANCHOR-CARD + Per-YAML Orthogonality + Phase-Decomposed Scan

**axis:** inertia-framing
**hypothesis:** R8 V-03 leads at 99.39 under v9 with the gap-first pipeline (C-39 + C-40 + C-41)
but lacks the ANCHOR-CARD mechanism: Phase 3 does not designate the inertia-advocate as
ANCHOR-CARD, YAML files carry no `orthogonality` field referencing the anchor, and the cross-set
scan is a flat "for each pair" check without phase-decomposition. This variate adds three
structures over R8 V-03: (1) explicit ANCHOR-CARD designation and write-first mandate in Phase 3
and Phase 5, (2) [FC-11] `orthogonality` field in the YAML schema applied to all non-anchor roles,
and (3) a cross-set scan with explicitly named Phase 1 (Anchor-Orthogonality) and Phase 2
(Non-Anchor Pairwise) — satisfying C-37 + C-38. The gap-first pipeline from R8 V-03
(INERTIA-GAP ANALYSIS sub-step, gap-vocab names, inherited inertia gap in Diagnosis Card)
is preserved unchanged. Falsifiable: if ANCHOR-CARD write-first ordering causes subsequent
domain expert frames to define themselves negatively against the anchor rather than positively
from their concern vocabulary, Role Differentiation (C-09) degrades even as structural
compliance improves.

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
          The name must derive from the inertia gap vocabulary identified in Phase 2.
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
            to this role's frame — uniqueness argument required before writing

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
          type: string — named contrast to the ANCHOR-CARD primary verify question
          REQUIRED FORMAT: "[Named contrast axis] — this role's lens diverges from the
            ANCHOR-CARD because [specific reason naming the anchor's question and why
            this role's concern falls outside that question's scope]"
          FAILURE MODE: generic assertion not tied to the anchor question
          BAD:  "This role thinks about performance"
          GOOD: "Retry-budget boundary — this role's lens diverges from the ANCHOR-CARD
                 because while the anchor asks whether the status quo already handles the
                 scenario, this role asks whether retry semantics produce silent call-volume
                 violations the anchor's sufficiency test cannot see"
          NOTE: the inertia-advocate ANCHOR-CARD does NOT carry this field.
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT: `field_name` = `inertia_surface`; `population_source` names Phase 1
   and INERTIA-SURFACE artifact; `purpose` names the Phase 0 diagnostic question
2. FIELD-CONTRACT written with all eleven items [FC-1] through [FC-11]
3. [FC-1] PROHIBITED NAMES clause names "domain-expert" and "expert-1" explicitly
4. [FC-4] and [FC-5] display exact identifier strings `verify_questions` and
   `simplify_rules` under EXACT IDENTIFIER labels — both appear verbatim
5. [FC-11] written with REQUIRED FORMAT clause and FAILURE MODE; applies to non-anchor only

---

PHASE 1 — INERTIA SURFACE

Read `{topic}` context. Write an INERTIA-SURFACE block:

```
INERTIA-SURFACE for {topic}:

  Status-quo claim: [the strongest argument that {topic} is unnecessary — grounded
    in the actual context; name the specific existing capability relied upon]

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

PHASE 2 — DOMAIN ANALYSIS (gap-first derivation)

Read `{topic}` context for concerns the Phase 1 status-quo claim does not address.

**Step 1 — INERTIA-GAP ANALYSIS:** Before naming any domain expert, identify the gaps
the Phase 1 status-quo claim leaves uncovered. DO NOT name experts in this step.

```
INERTIA-GAP ANALYSIS for {topic}:

  Gap 1:
    Domain: [the named vocabulary domain this failure belongs to — e.g., "retry semantics",
             "schema migration", "backpressure propagation"]
    Failure mode: [the specific failure the status quo cannot prevent in this domain]
    Inertia resistance: [the status-quo argument an expert from this domain exposes
      as insufficient — what the Phase 1 inertia-advocate's claim overlooks]

  Gap 2:
    Domain: [...]
    Failure mode: [...]
    Inertia resistance: [...]

  Gap 3:
    Domain: [...]
    Failure mode: [...]
    Inertia resistance: [...]

  (minimum three gaps; each must have a named Domain, Failure mode, Inertia resistance)
```

Expert names must derive from the Gap Domain vocabulary above.
PROHIBITED by [FC-1]: "domain-expert", "expert-1", "generic-expert", "role-1".

**Step 2 — EXPERT DERIVATION:** From each gap, derive an expert whose name comes from
that gap's Domain vocabulary:

```
DOMAIN-ANALYSIS for {topic}:

  Domain experts derived from INERTIA-GAP ANALYSIS:
    - Expert name: [slug from Gap N Domain vocabulary — PROHIBITED: "domain-expert",
        "expert-1"; name must be derivable from the Domain field above]
      Concern link: Gap N from INERTIA-GAP ANALYSIS
      Inertia gap: [Gap N inertia resistance — copied from INERTIA-GAP ANALYSIS;
        not paraphrased; this is what this expert's domain sees that the inertia-advocate
        overlooks]
      Domain-vocabulary frame: [per [FC-2] — epistemic viewpoint using Gap N vocabulary]
      Verify focus: [what artifact or behavior this expert checks first]
    (one entry per gap — at minimum one expert)
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 2.

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. INERTIA-GAP ANALYSIS written before DOMAIN-ANALYSIS; at least three gaps, each with
   named Domain, Failure mode, and Inertia resistance
2. At least three gaps use vocabulary specific to `{topic}`
3. Each derived expert entry lists all five attributes: name, concern link, inertia gap,
   domain-vocabulary frame, verify focus — checked per expert, not as a total count
4. Expert names derive from INERTIA-GAP ANALYSIS Domain vocabulary — no placeholder per [FC-1]
5. No stock role names appear in this block

---

PHASE 3 — STOCK ROLES

```
STOCK-ROLES:
  - inertia-advocate  (status-quo challenge lens — ANCHOR-CARD for this registry;
                       orientation.frame anchors to Phase 1 status-quo claim;
                       verify_questions sourced from Phase 1 challenge questions;
                       Diagnosis Card written FIRST in Phase 5, YAML written FIRST;
                       carries `anchor: true` in YAML; does NOT carry `orthogonality`)
  - pm                (product value and user outcome lens)
  - architect         (technical structure and system boundary lens)
  - strategy          (business model and competitive position lens)
```

All non-anchor roles carry `orthogonality` per [FC-11] in their YAML files.

**GATE** — Phase 3 complete when ALL of the following are TRUE:
1. STOCK-ROLES lists all four names with lens descriptors
2. inertia-advocate is explicitly designated ANCHOR-CARD
3. Phase 5 ANCHOR-CARD write-first mandate is stated
4. Phase 1 INERTIA-SURFACE confirmed available as source for frame and verify_questions

---

PHASE 4 — OUTPUT AREA

```
OUTPUT-AREA: .roles/{area}/
```

Area slug must use Gap Domain vocabulary from Phase 2 INERTIA-GAP ANALYSIS. NOT: `default`,
`generic`, `roles`.

**GATE** — Phase 4 complete when ALL of the following are TRUE:
1. OUTPUT-AREA written with area slug from Phase 2 Gap Domain vocabulary
2. Path format is exactly `.roles/{area}/`

---

PHASE 5 — DIAGNOSIS CARDS AND ROLE FILE WRITING

**PREPARE:** Confirm inputs before writing any Diagnosis Card:
- Phase 0 [FC-4] exact identifier: `verify_questions` (retrieve verbatim from [FC-4])
- Phase 0 [FC-5] exact identifier: `simplify_rules` (retrieve verbatim from [FC-5])
- Phase 0 [FC-11] orthogonality: REQUIRED FORMAT and applies to non-anchor roles (confirm)
- Phase 1 INERTIA-SURFACE: status-quo claim and challenge questions confirmed
- Phase 2 INERTIA-GAP ANALYSIS: all gaps, Domains, Failure modes, Inertia resistances confirmed
- Phase 2 DOMAIN-ANALYSIS: expert names (gap-derived), concern links, inertia gaps confirmed
- Phase 3 STOCK-ROLES: four names; inertia-advocate flagged ANCHOR-CARD confirmed
- Phase 4 OUTPUT-AREA path confirmed

PREPARE complete when all eight inputs are confirmed. Do not begin Diagnosis Cards until confirmed.

**ANCHOR-CARD (write this Diagnosis Card first, before all others):**

```
ANCHOR-CARD for inertia-advocate:

  name: {domain-vocabulary slug — derived from Phase 1 context; confirmed against [FC-1]}
  [FC-1] name check: this name is domain-specific because [vocabulary source]; NOT a
    placeholder; confirmed

  frame (one sentence): {Phase 1 status-quo claim cast as epistemic stance}
  serves (one sentence): {beneficiary of the inertia verdict — NOT a frame restatement}

  primary_verify_question: {the most adversarial form of "why is the status quo
    sufficient?" — this question is the reference axis for Phase 1 of the cross-set scan;
    all subsequent Diagnosis Cards must show orthogonality to this question}
  uniqueness argument: this question is uniquely attributable to the inertia-advocate
    because no other role challenges the sufficiency of the status quo as its primary
    concern — the closest overlap is [role-name], which would ask [different angle] —
    confirmed distinct
  anchor status: ANCHOR-CARD — this role's primary question is the Phase 1 reference
    axis; all subsequent non-anchor YAML files carry `orthogonality` to this question

  collaborates_with draft: [{name-1}, {name-2}]
  phantom check: confirm each name appears in this registry — confirmed
```

**SUBSEQUENT DIAGNOSIS CARDS (written after ANCHOR-CARD, one per remaining role):**

```
DIAGNOSIS-CARD for {role-name}:

  name: {proposed slug — for domain experts: derived from Phase 2 INERTIA-GAP ANALYSIS
         Gap Domain vocabulary; confirmed against [FC-1]}
  [FC-1] name check: this name derives from [Gap N Domain vocabulary]; NOT a placeholder;
    confirmed

  frame (one sentence): {for domain experts: anchored to Phase 2 inertia gap vocabulary;
    for stock roles: standard lens framing}
  serves (one sentence): {beneficiary — NOT a frame restatement}

  inertia gap inherited: {for domain experts: Gap N inertia resistance from Phase 2
    INERTIA-GAP ANALYSIS — copied verbatim, not paraphrased; for stock roles: N/A}

  primary_verify_question: {the most role-specific question for this frame}
  uniqueness argument: this question is uniquely attributable to this role because no
    other role would prioritize it first — closest overlap is [role-name], which would
    ask [different angle] — confirmed distinct
  orthogonality to ANCHOR-CARD: {per [FC-11] REQUIRED FORMAT — named contrast axis
    explaining how this role's concern falls outside the anchor's sufficiency question;
    this value is copied verbatim to the `orthogonality` YAML field}

  collaborates_with draft: [{name-1}, {name-2}]
  phantom check: confirm each name appears in this registry — confirmed
```

After all Diagnosis Cards are written, run the **CROSS-CARD UNIQUENESS SCAN**:

```
CROSS-CARD UNIQUENESS SCAN (ANCHOR-CARD as reference axis):

  Phase 1 — Anchor-Orthogonality Check:
    List the ANCHOR-CARD primary_verify_question.
    For each non-anchor role, state its primary_verify_question.
    Test per non-anchor role: could this role's question and the anchor question both
      be asked by the same role? If yes, flag and revise the non-anchor question.
    Record PASS/FAIL per non-anchor role before proceeding to Phase 2.

  Phase 2 — Non-Anchor Pairwise Check:
    For each pair of non-anchor roles, compare their primary_verify_questions.
    Test per pair: could both questions be asked by the same role type?
    Flag any pair where both questions serve the same epistemic purpose.
    Revise flagged questions before proceeding to YAML writing.

  Resolution: all Phase 1 and Phase 2 flags resolved before YAML writing begins.
```

**WRITE:** One `.md` file per role to `.roles/{area}/`. Write order: inertia-advocate
(ANCHOR-CARD) first, then domain experts (Phase 2 order), then remaining stock roles.

```yaml
---
name: {per Diagnosis Card — confirmed against [FC-1]}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

# For inertia-advocate ANCHOR-CARD only:
anchor: true

# For all non-anchor roles only (omit from ANCHOR-CARD):
orthogonality: "{per [FC-11] REQUIRED FORMAT — copied from Diagnosis Card orthogonality
  field; named contrast axis tracing to ANCHOR-CARD primary question}"

orientation:
  frame: |
    {Per [FC-2] and Diagnosis Card frame. FAILURE MODE: task-list frame.}
  serves: |
    {Per [FC-3] — NOT a frame restatement.}

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
  # CONTRACT VIOLATION (type 1) — PHANTOM: name absent from this registry
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent
```

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. ANCHOR-CARD Diagnosis Card was written before all other Diagnosis Cards
2. All subsequent (non-anchor) Diagnosis Cards include `orthogonality to ANCHOR-CARD` field
3. CROSS-CARD UNIQUENESS SCAN run with two explicitly named phases — Phase 1
   (Anchor-Orthogonality) and Phase 2 (Non-Anchor Pairwise) — both phases documented
4. One `.md` file per role at `.roles/{area}/`; inertia-advocate written first
5. ANCHOR-CARD YAML file contains `anchor: true`; does NOT contain `orthogonality` field
6. All non-anchor YAML files contain `orthogonality` field per [FC-11] REQUIRED FORMAT;
   field is not generic — names a contrast axis tracing to the ANCHOR-CARD question
7. Every file uses exact identifiers `verify_questions` and `simplify_rules` verbatim
8. No prohibited names per [FC-1]; no collaborates_with CONTRACT VIOLATION type-1 or type-2

---

PHASE 6 — REGISTRY SUMMARY

**PREPARE:** Enumerate the `.md` files written in Phase 5. Record as `PHASE5_COUNT`.
This count must come from Phase 5 enumeration — NOT from adding prior-phase planned counts.
Deriving total_roles by adding Phase 2 expert count + Phase 3 stock role count instead of
enumerating Phase 5 output files is a count-bypass failure.

PREPARE complete when `PHASE5_COUNT` is recorded from Phase 5 enumeration.

**WRITE:** `.roles/{area}/REGISTRY.md`:

```
---
area: {area — from Phase 2 Gap Domain vocabulary}
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
    derivation_source: Phase 2 Gap N — {Gap Domain vocabulary}
    inertia_gap: {Gap N inertia resistance copied from Phase 2 — not paraphrased}
  (one entry per derived expert)

coverage_gaps: |
  {Phase 2 gaps not addressed by any derived expert; or "none detected."}

inertia_surface: |
  {Phase 1 status-quo claim verbatim — exact sentence from INERTIA-SURFACE block.
  Do not paraphrase. This fulfills the EXTENSION-COMMITMENT from Phase 0.}

Generated by: /org-roles {topic} — {date}
```

HEADING STUB FAIL CONDITION: A `## Registry Summary` heading with empty or omitted fields
beneath it is an explicit C-10 failure. Every field must contain substantive content; a header
with an empty value below it fails this gate.

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.roles/{area}/REGISTRY.md`
2. `total_roles` equals `PHASE5_COUNT` from Phase 5 enumeration
3. `domain_experts` lists each expert with name, derivation_source, and inertia_gap
4. `inertia_surface` contains Phase 1 status-quo claim verbatim — not paraphrased
5. No heading stubs; HEADING STUB FAIL CONDITION was read before writing began

---

## V-02 — Role Sequence: Named Gap Identifiers + Positive Sourcing + Named Diagnosis Card Provenance

**axis:** role-sequence
**hypothesis:** R8 V-03's INERTIA-GAP ANALYSIS uses anonymous gap numbers ("Gap 1", "Gap 2")
and the `inertia gap inherited` field in Diagnosis Cards cites "Gap N inertia resistance from
Phase 2" — a positional reference rather than a named-entry reference. C-40 requires a positive
sourcing constraint ("names must derive from Gap Domain vocabulary" — a gate, not a fence)
and C-41 requires the Diagnosis Card provenance field to trace "to a named entry in the gap
analysis artifact." This variate gives each gap a formal slug identifier (GAP-{domain-slug})
at write-time, requires expert name derivation to cite the GAP-{slug} identifier by name,
and requires the Diagnosis Card `inertia gap inherited` field to cite the named GAP-{slug}
entry rather than a positional number. The ANCHOR-CARD mechanism and phase-decomposed scan
are not changed from R8 V-03 (the ANCHOR-CARD is not yet introduced, preserving the
single-axis constraint). Falsifiable: if named gap identifiers cause experts to be named
too literally (e.g., "GAP-retry-semantics-expert" rather than "retry-budget-compliance-analyst"),
expert name quality (C-28 specificity) may degrade even as sourcing compliance improves.

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
          The name must derive from the vocabulary of the named GAP identifier assigned
          in Phase 2 INERTIA-GAP ANALYSIS. The derivation must be traceable: the name
          must be justifiable by citing a specific GAP-{slug} entry.
          BAD:  "domain-expert" (no domain content; applies to any registry)
          GOOD: "retry-budget-compliance-analyst" (derived from GAP-retry-semantics vocabulary)

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
          type: list; minimum two items; at least one uniquely attributable to this role's
            frame — uniqueness argument required before writing

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
1. EXTENSION-COMMITMENT: `field_name` = `inertia_surface`; `population_source` names Phase 1
   and INERTIA-SURFACE; `purpose` names the Phase 0 diagnostic question
2. FIELD-CONTRACT written with all ten items [FC-1] through [FC-10]
3. [FC-1] contains PROHIBITED NAMES clause AND the positive sourcing requirement naming
   GAP-{slug} as the derivation source — both clauses present verbatim
4. [FC-4] and [FC-5] display exact identifier strings `verify_questions` and
   `simplify_rules` under EXACT IDENTIFIER labels

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

PHASE 2 — DOMAIN ANALYSIS (named-identifier gap-first derivation)

Read `{topic}` context for concerns the Phase 1 status-quo claim does not address.

**Step 1 — INERTIA-GAP ANALYSIS with named identifiers:** Before naming any domain expert,
identify the gaps the Phase 1 status-quo claim leaves uncovered. Assign each gap a formal
named identifier of the form `GAP-{domain-slug}`. DO NOT name experts in this step.

```
INERTIA-GAP ANALYSIS for {topic}:

  GAP-{domain-slug-1}:
    Domain: [the named vocabulary domain this failure belongs to]
    Failure mode: [the specific failure the status quo cannot prevent]
    Inertia resistance: [what the inertia-advocate's Phase 1 claim overlooks from
      this domain's perspective]

  GAP-{domain-slug-2}:
    Domain: [...]
    Failure mode: [...]
    Inertia resistance: [...]

  GAP-{domain-slug-3}:
    Domain: [...]
    Failure mode: [...]
    Inertia resistance: [...]

  (minimum three named gaps; each identifier must derive from its Domain vocabulary)
```

Expert names must derive from the Gap Domain vocabulary above.
PROHIBITED by [FC-1]: "domain-expert", "expert-1", "generic-expert", "role-1".

**Step 2 — EXPERT DERIVATION with positive sourcing:** From each named gap, derive an
expert whose name and frame are traceable to that gap's identifier:

```
DOMAIN-ANALYSIS for {topic}:

  Domain experts derived from INERTIA-GAP ANALYSIS:
    - Expert name: [slug derived from GAP-{identifier} Domain vocabulary —
        PROHIBITED: "domain-expert", "expert-1";
        POSITIVE SOURCING REQUIRED: state "this name derives from GAP-{identifier}
        Domain vocabulary: [specific term from that vocabulary used in the name]"]
      Named gap source: GAP-{identifier} from INERTIA-GAP ANALYSIS
      Inertia gap: [GAP-{identifier} inertia resistance — copied from INERTIA-GAP
        ANALYSIS; not paraphrased]
      Domain-vocabulary frame: [per [FC-2] — epistemic viewpoint using GAP-{identifier}
        Domain vocabulary]
      Verify focus: [what artifact or behavior this expert checks first]
    (one entry per named gap — at minimum one expert)
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 2.

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. INERTIA-GAP ANALYSIS written before DOMAIN-ANALYSIS; at least three named gaps
   (GAP-{slug} format), each with Domain, Failure mode, and Inertia resistance
2. Each GAP-{slug} identifier derives from its own Domain vocabulary
3. Each derived expert entry lists all five attributes: name, named gap source (GAP-{slug}),
   inertia gap, domain-vocabulary frame, verify focus — checked per expert
4. Each expert entry includes POSITIVE SOURCING statement tracing the name to GAP-{slug}
   vocabulary — absent sourcing statement fails this item even if the name is specific
5. No placeholder names per [FC-1]; no stock role names

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
3. Phase 1 INERTIA-SURFACE confirmed available

---

PHASE 4 — OUTPUT AREA

```
OUTPUT-AREA: .roles/{area}/
```

Area slug must use Gap Domain vocabulary from Phase 2 INERTIA-GAP ANALYSIS. NOT: `default`,
`generic`, `roles`.

**GATE** — Phase 4 complete when ALL of the following are TRUE:
1. OUTPUT-AREA written with area slug from Phase 2 Domain vocabulary
2. Path format is exactly `.roles/{area}/`

---

PHASE 5 — DIAGNOSIS CARDS AND ROLE FILE WRITING

**PREPARE:** Confirm inputs before writing any Diagnosis Card:
- Phase 0 [FC-4] exact identifier: `verify_questions` (retrieve verbatim)
- Phase 0 [FC-5] exact identifier: `simplify_rules` (retrieve verbatim)
- Phase 1 INERTIA-SURFACE: status-quo claim and challenge questions confirmed
- Phase 2 INERTIA-GAP ANALYSIS: all named gaps (GAP-{slug}) with Domain, Failure mode,
  Inertia resistance confirmed
- Phase 2 DOMAIN-ANALYSIS: expert names (with GAP-{slug} sourcing), inertia gaps confirmed
- Phase 3 STOCK-ROLES: four names confirmed
- Phase 4 OUTPUT-AREA path confirmed

PREPARE complete when all seven inputs confirmed. Do not begin Diagnosis Cards until confirmed.

**DIAGNOSIS CARDS:** Before writing any YAML, write one Diagnosis Card per role.
For domain expert cards, the `inertia gap inherited` field must cite the GAP-{slug} identifier
by name — not a positional reference ("Gap 1") but the named identifier ("GAP-retry-semantics").

```
DIAGNOSIS-CARD for {role-name}:

  name: {proposed slug — for domain experts: derived from GAP-{slug} Domain vocabulary;
         confirmed against [FC-1] positive sourcing requirement}
  [FC-1] name check: this name derives from GAP-{slug} Domain vocabulary: [specific term
    used in the name]; NOT a placeholder; confirmed

  frame (one sentence): {for domain experts: anchored to GAP-{slug} inertia gap vocabulary;
    for inertia-advocate: Phase 1 status-quo claim; for stock roles: standard lens}
  serves (one sentence): {beneficiary — NOT a frame restatement}

  inertia gap inherited: {for domain experts: GAP-{slug} inertia resistance from Phase 2
    INERTIA-GAP ANALYSIS — cite by named identifier "GAP-{slug}", not by position;
    example: "GAP-retry-semantics: [resistance text copied verbatim]";
    for inertia-advocate: Phase 1 status-quo claim;
    for stock roles: N/A}

  primary_verify_question: {the most role-specific question for this frame}
  uniqueness argument: this question is uniquely attributable to this role because no
    other role would prioritize it first — closest overlap is [role-name], which would
    ask [different angle] — confirmed distinct

  collaborates_with draft: [{name-1}, {name-2}]
  phantom check: confirm each name appears in this registry — confirmed
```

After all Diagnosis Cards are written, run a CROSS-CARD UNIQUENESS SCAN:

```
CROSS-CARD UNIQUENESS SCAN:
  For each pair of roles, confirm their primary_verify_questions address different facets.
  Flag any pair where both questions could be asked by the same role type.
  Revise flagged questions before proceeding to YAML writing.
```

**WRITE:** One `.md` file per role to `.roles/{area}/`. Domain experts first (Phase 2),
stock roles second (Phase 3). Apply the FIELD CONTRACT to each file.

```yaml
---
name: {per Diagnosis Card — confirmed against [FC-1] positive sourcing}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Per [FC-2] and Diagnosis Card frame. FAILURE MODE: task-list frame.}
  serves: |
    {Per [FC-3] — NOT a frame restatement.}

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
  # CONTRACT VIOLATION (type 1) — PHANTOM: name absent from this registry
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent
```

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. One Diagnosis Card per role — all cards written before any YAML file
2. Domain expert Diagnosis Cards include `inertia gap inherited` citing named GAP-{slug}
   identifier — positional reference ("Gap 1") fails this item
3. CROSS-CARD UNIQUENESS SCAN was run; flagged pairs revised
4. One `.md` file per role at `.roles/{area}/`
5. Every file uses exact identifiers `verify_questions` and `simplify_rules` verbatim
6. No prohibited names per [FC-1] positive sourcing requirement
7. No collaborates_with CONTRACT VIOLATION type-1 or type-2

---

PHASE 6 — REGISTRY SUMMARY

**PREPARE:** Enumerate `.md` files written in Phase 5. Record as `PHASE5_COUNT`.
Count must come from Phase 5 enumeration — not from adding prior-phase planned counts.

PREPARE complete when `PHASE5_COUNT` recorded from Phase 5 enumeration.

**WRITE:** `.roles/{area}/REGISTRY.md`:

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
    gap_source: GAP-{slug} from INERTIA-GAP ANALYSIS
    inertia_gap: {GAP-{slug} inertia resistance — copied verbatim from Phase 2}
  (one entry per derived expert)

coverage_gaps: |
  {Phase 2 gaps not addressed by any derived expert; or "none detected."}

inertia_surface: |
  {Phase 1 status-quo claim verbatim — exact sentence from INERTIA-SURFACE block.
  Do not paraphrase. This fulfills the EXTENSION-COMMITMENT from Phase 0.}

Generated by: /org-roles {topic} — {date}
```

HEADING STUB FAIL CONDITION: Section headers with empty or omitted values beneath them
fail C-10. Every field must contain substantive content.

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.roles/{area}/REGISTRY.md`
2. `total_roles` equals `PHASE5_COUNT` from Phase 5 enumeration
3. `domain_experts` lists each expert with `name`, `gap_source` (GAP-{slug}), `inertia_gap`
4. `inertia_surface` contains Phase 1 status-quo claim verbatim
5. No heading stubs; HEADING STUB FAIL CONDITION was read before writing began

---

## V-03 — Output Format: YAML Persistence of Orthogonality + Inertia Gap Provenance

**axis:** output-format
**hypothesis:** C-37 requires "every subsequent card carries a named orthogonality field
referencing the anchor." R8 V-02 places this field in the Diagnosis Card (pre-YAML) but not
in the YAML output file. C-41 requires the Diagnosis Card to carry a provenance field, but the
provenance information is not preserved in the final YAML file, making it inaccessible to
downstream consumers that read only the YAML. This variate adds two new schema fields to the
YAML output: `orthogonality` (for all non-anchor roles) and `inertia_gap_inherited` (for
domain expert roles). Both fields must contain substantive values traceable to Phase 2 named
entries. The ANCHOR-CARD mechanism, gap-first pipeline, and phase-decomposed scan are not
added (single-axis: output format only). Falsifiable: if adding `inertia_gap_inherited` to
YAML files causes domain expert frames to over-anchor to their gap description rather than
to their concern's positive signal, frame quality (C-05) may degrade as persistence compliance
improves.

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
          The name must derive from the inertia gap vocabulary in Phase 2.
          BAD:  "domain-expert" (no domain content)
          GOOD: "backpressure-propagation-verifier" (derived from gap vocabulary)

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
          Applies to: all non-anchor YAML files
          type: string — named contrast axis explaining how this role's concern falls
            outside the inertia-advocate's status-quo sufficiency framing
          FAILURE MODE: generic assertion ("this role thinks about X")
          REQUIRED: must appear in the YAML output file, not only in the Diagnosis Card
          BAD:  "This role focuses on technical concerns"
          GOOD: "Backpressure-signal coverage — this role's concern (whether upstream
                 producers receive correct backpressure signals) falls outside the
                 inertia-advocate's sufficiency test, which evaluates only whether
                 existing rate-limit behavior covers the nominal path"

  [FC-12] inertia_gap_inherited
          Applies to: domain expert YAML files only (not stock roles, not inertia-advocate)
          type: string — provenance field tracing this role's inertia gap to a named entry
            in the Phase 2 INERTIA-GAP ANALYSIS artifact
          REQUIRED: must appear in the YAML output file, not only in the Diagnosis Card
          REQUIRED FORMAT: "Gap N — [Gap Domain name]: [inertia resistance copied verbatim]"
          FAILURE MODE: positional reference without domain name ("Gap 1: ...")
          BAD:  "Gap 1: retry loops are not bounded by the existing mechanism"
          GOOD: "Gap 3 — retry-semantics: the existing rate-limit mechanism does not bound
                 total retry attempts per operation window, only per-request latency"
          NOTE: the inertia_gap_inherited field must cite the Gap Domain name by name,
          not only by number; a number-only reference fails this contract.
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT: `field_name` = `inertia_surface`; `population_source` names Phase 1
   and INERTIA-SURFACE; `purpose` names the Phase 0 diagnostic question
2. FIELD-CONTRACT written with all twelve items [FC-1] through [FC-12]
3. [FC-1] PROHIBITED NAMES clause names "domain-expert" and "expert-1"
4. [FC-4] and [FC-5] display exact identifier strings `verify_questions` and
   `simplify_rules` under EXACT IDENTIFIER labels — both appear verbatim
5. [FC-11] written with REQUIRED and FAILURE MODE; states field appears in YAML output
6. [FC-12] written with REQUIRED FORMAT; states Gap Domain name required (not number only)

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

PHASE 2 — DOMAIN ANALYSIS (gap-first derivation)

Read `{topic}` context for concerns the Phase 1 status-quo claim does not address.

**Step 1 — INERTIA-GAP ANALYSIS:** Before naming any domain expert, identify the gaps
the Phase 1 status-quo claim leaves uncovered. DO NOT name experts in this step.

```
INERTIA-GAP ANALYSIS for {topic}:

  Gap 1:
    Domain: [named vocabulary domain — e.g., "retry semantics", "schema migration"]
    Failure mode: [specific failure the status quo cannot prevent]
    Inertia resistance: [what the Phase 1 inertia claim overlooks from this domain]

  Gap 2:
    Domain: [...]
    Failure mode: [...]
    Inertia resistance: [...]

  Gap 3:
    Domain: [...]
    Failure mode: [...]
    Inertia resistance: [...]

  (minimum three gaps; each must have named Domain, Failure mode, Inertia resistance)
```

Expert names must derive from Gap Domain vocabulary.
PROHIBITED by [FC-1]: "domain-expert", "expert-1", "generic-expert", "role-1".

**Step 2 — EXPERT DERIVATION:**

```
DOMAIN-ANALYSIS for {topic}:

  Domain experts derived from INERTIA-GAP ANALYSIS:
    - Expert name: [slug from Gap N Domain vocabulary — PROHIBITED: "domain-expert",
        "expert-1"]
      Concern link: Gap N from INERTIA-GAP ANALYSIS
      Inertia gap: [Gap N inertia resistance — copied from INERTIA-GAP ANALYSIS]
      Domain-vocabulary frame: [per [FC-2] — epistemic viewpoint using Gap N vocabulary]
      Verify focus: [what artifact or behavior this expert checks first]
    (one entry per gap — at minimum one)
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 2.

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. INERTIA-GAP ANALYSIS written before DOMAIN-ANALYSIS; at least three gaps each with
   named Domain, Failure mode, Inertia resistance
2. Each derived expert lists all five attributes; names from Domain vocabulary
3. No placeholder names per [FC-1]; no stock role names

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
OUTPUT-AREA: .roles/{area}/
```

Area slug uses Gap Domain vocabulary from Phase 2. NOT: `default`, `generic`, `roles`.

**GATE** — Phase 4 complete when ALL of the following are TRUE:
1. OUTPUT-AREA written with area slug from Phase 2 Domain vocabulary
2. Path format is exactly `.roles/{area}/`

---

PHASE 5 — DIAGNOSIS CARDS AND ROLE FILE WRITING

**PREPARE:** Confirm inputs before writing any Diagnosis Card:
- Phase 0 [FC-4] exact identifier: `verify_questions` (retrieve verbatim)
- Phase 0 [FC-5] exact identifier: `simplify_rules` (retrieve verbatim)
- Phase 0 [FC-11] orthogonality REQUIRED FORMAT (confirm applies to non-anchor YAML)
- Phase 0 [FC-12] inertia_gap_inherited REQUIRED FORMAT (confirm cites Gap Domain name)
- Phase 1 INERTIA-SURFACE: status-quo claim and challenge questions confirmed
- Phase 2 INERTIA-GAP ANALYSIS: gaps with Domain names and inertia resistances confirmed
- Phase 2 DOMAIN-ANALYSIS: expert names, inertia gaps confirmed
- Phase 3 STOCK-ROLES: four names confirmed
- Phase 4 OUTPUT-AREA path confirmed

PREPARE complete when all nine inputs confirmed. Do not begin Diagnosis Cards until confirmed.

**DIAGNOSIS CARDS:** Before writing any YAML, write one Diagnosis Card per role.

```
DIAGNOSIS-CARD for {role-name}:

  name: {proposed slug — domain experts: from Phase 2 Gap Domain vocabulary;
         confirmed against [FC-1]}
  [FC-1] name check: this name derives from [Gap Domain vocabulary]; NOT a placeholder;
    confirmed

  frame (one sentence): {for domain experts: anchored to Gap vocabulary; for
    inertia-advocate: Phase 1 status-quo claim; for stock roles: standard lens}
  serves (one sentence): {beneficiary — NOT a frame restatement}

  inertia gap inherited: {for domain experts: "Gap N — [Gap Domain name]:
    [inertia resistance copied verbatim]" — cite by Gap Domain NAME per [FC-12];
    for inertia-advocate: Phase 1 status-quo claim; for stock roles: N/A}
  orthogonality: {for non-inertia-advocate roles: named contrast axis per [FC-11] —
    explains how this role's concern falls outside the inertia-advocate's sufficiency
    framing; this value will be copied verbatim to the YAML `orthogonality` field}

  primary_verify_question: {most role-specific question for this frame}
  uniqueness argument: this question is uniquely attributable because [reason] —
    confirmed distinct

  collaborates_with draft: [{name-1}, {name-2}]
  phantom check: confirmed
```

After all Diagnosis Cards are written, run a CROSS-CARD UNIQUENESS SCAN:

```
CROSS-CARD UNIQUENESS SCAN:
  For each pair of roles, confirm their primary_verify_questions address different facets.
  Flag any pair where both questions could be asked by the same role type.
  Revise flagged questions before proceeding to YAML writing.
```

**WRITE:** One `.md` file per role to `.roles/{area}/`. Domain experts first, then
stock roles. The YAML schema includes two new fields specified in [FC-11] and [FC-12]:

```yaml
---
name: {per Diagnosis Card — confirmed against [FC-1]}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

# orthogonality — all non-inertia-advocate roles; omit from inertia-advocate file
orthogonality: "{per [FC-11]: named contrast axis copied from Diagnosis Card;
  not generic; traces to inertia-advocate sufficiency framing}"

# inertia_gap_inherited — domain expert roles only; omit from stock roles
inertia_gap_inherited: "{per [FC-12]: Gap N — [Gap Domain name]: [resistance verbatim];
  Domain name required; positional-only reference fails [FC-12]}"

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
    {Per [FC-7]: domain-specific justification.}

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
1. One Diagnosis Card per role — all cards written before any YAML file
2. Domain expert Diagnosis Cards include `inertia gap inherited` citing Gap Domain NAME
   per [FC-12] — positional-only reference fails this item
3. Non-inertia-advocate Diagnosis Cards include `orthogonality` field per [FC-11]
4. CROSS-CARD UNIQUENESS SCAN run; flagged pairs revised
5. One `.md` file per role at `.roles/{area}/`
6. Non-inertia-advocate YAML files contain `orthogonality` field with substantive value
7. Domain expert YAML files contain `inertia_gap_inherited` field citing Gap Domain NAME
8. Every file uses exact identifiers `verify_questions` and `simplify_rules` verbatim
9. No prohibited names per [FC-1]; no collaborates_with CONTRACT VIOLATION

---

PHASE 6 — REGISTRY SUMMARY

**PREPARE:** Enumerate `.md` files written in Phase 5. Record as `PHASE5_COUNT`.
Counting from prior-phase plans instead of Phase 5 enumeration is a count-bypass failure.

**WRITE:** `.roles/{area}/REGISTRY.md`:

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
    derivation_source: Phase 2 Gap N — {Gap Domain name}
    inertia_gap: {Gap N inertia resistance — copied verbatim}
  (one entry per derived expert)

coverage_gaps: |
  {Phase 2 gaps not addressed by any derived expert; or "none detected."}

inertia_surface: |
  {Phase 1 status-quo claim verbatim. This fulfills the EXTENSION-COMMITMENT from Phase 0.}

Generated by: /org-roles {topic} — {date}
```

HEADING STUB FAIL CONDITION: Headers with empty fields beneath them fail C-10. Every field
must contain substantive content.

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.roles/{area}/REGISTRY.md`
2. `total_roles` equals `PHASE5_COUNT` from Phase 5 enumeration
3. `domain_experts` lists each expert with name, derivation_source (Gap N — [Domain name]),
   inertia_gap
4. `inertia_surface` contains Phase 1 status-quo claim verbatim
5. No heading stubs; HEADING STUB FAIL CONDITION was read before writing began

---

## V-04 — Combined: ANCHOR-CARD + Named Gaps + Phase-Decomposed Scan + YAML Persistence

**axis:** inertia-framing + role-sequence + output-format
**hypothesis:** V-01 satisfies C-37 + C-38 by adding ANCHOR-CARD designation, per-YAML
`orthogonality`, and the two-phase scan. V-02 satisfies C-40 + C-41 by assigning formal
GAP-{slug} identifiers and requiring named-entry Diagnosis Card provenance. V-03 satisfies
C-37 (YAML) + C-41 (YAML level) by persisting both `orthogonality` and `inertia_gap_inherited`
in the YAML output files. This variate combines all three: the inertia-advocate is ANCHOR-CARD
(Phase 3, Phase 5 write-first), all non-anchor YAML files carry `orthogonality` per [FC-11],
each gap has a formal GAP-{slug} identifier, expert names trace to the named gap by positive
sourcing, Diagnosis Cards cite provenance by GAP-{slug} name, YAML files persist
`inertia_gap_inherited` by named gap, and the cross-set scan is explicitly phase-labeled.
All five new criteria are targeted simultaneously. Falsifiable: if the combination of
constraints (named gaps + ANCHOR-CARD ordering + YAML persistence) produces over-specified
expert frames that collapse into variations of the inertia-advocate's concern rather than
expressing independent epistemic viewpoints, the Role Differentiation criterion (C-09) will
degrade — an accuracy cost for a compliance gain.

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
OUTPUT-AREA: .roles/{area}/
```

Area slug uses GAP-{slug} Domain vocabulary from Phase 2. NOT: `default`, `generic`, `roles`.

**GATE** — Phase 4 complete when ALL of the following are TRUE:
1. OUTPUT-AREA written with area slug from Phase 2 GAP Domain vocabulary
2. Path format is exactly `.roles/{area}/`

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
      role? If yes, flag and revise the non-anchor question.
    Record PASS or FLAG per non-anchor role. Resolve all flags before Phase 2.

  Phase 2 — Non-Anchor Pairwise Check:
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
3. CROSS-CARD UNIQUENESS SCAN run with Phase 1 (Anchor-Orthogonality) and Phase 2
   (Non-Anchor Pairwise) — both phases documented with per-role records
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

**WRITE:** `.roles/{area}/REGISTRY.md`:

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
1. `REGISTRY.md` exists at `.roles/{area}/REGISTRY.md`
2. `total_roles` equals `PHASE5_COUNT` from Phase 5 enumeration
3. `domain_experts` lists each expert with `name`, `gap_source` (GAP-{slug}),
   `inertia_gap` (verbatim)
4. `inertia_surface` contains Phase 1 status-quo claim verbatim
5. No heading stubs; HEADING STUB FAIL CONDITION was read before writing began

---

## V-05 — Combined (Conversational Register): All Axes, Imperative Checklist Format

**axis:** all axes, phrasing register
**hypothesis:** V-04 satisfies all five new criteria but uses a procedural block format
(GATE conditions, PREPARE sequences) that may introduce ambiguity at the edges of each
gate check. This variate reframes V-04's pipeline in a direct imperative register: phases
open with the action, requirements are numbered checklists rather than GATE blocks,
inter-phase references use active verbs ("carry", "cite", "confirm") rather than passive
noun phrases ("must appear in"). The substantive requirements are identical to V-04.
Falsifiable: if the more conversational format causes less precise adherence to field
format requirements (e.g., the [FC-12] GAP-{slug} name citation), the format-driven
criteria (C-37, C-38, C-41) may degrade even if the structural pipeline (C-39, C-40) is
preserved.

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
- `verify_questions` — the YAML key for the verify list (PROHIBITED: verify, questions, checks)
- `simplify_rules` — the YAML key for the simplify list (PROHIBITED: simplify, rules, guidelines)
- `orthogonality` — appears in all non-anchor YAML files; names contrast to ANCHOR-CARD
- `inertia_gap_inherited` — appears in domain expert YAML files; cites GAP-{slug} by name
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
OUTPUT-AREA: .roles/{area}/
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
    the Phase 1 reference axis for the scan in Step 7]
  Uniqueness: [why no other role asks this first]; confirmed distinct
  anchor: ANCHOR-CARD — primary question is the Step 7 Phase 1 reference axis
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
    for inertia-advocate: Step 2 status-quo claim; for stock: N/A]
  Orthogonality to ANCHOR-CARD: [named contrast axis — "this role's lens diverges from
    the ANCHOR-CARD because [specific reason naming the anchor's question and what this
    role's concern sees that the anchor's sufficiency test cannot]";
    this value will be copied to the YAML `orthogonality` field]
  Primary question: [most role-specific question for this Frame]
  Uniqueness: [why no other role asks this first]; confirmed distinct
  Collaborates with: [{name-1}, {name-2}]; phantom check: confirmed
```

---

**Step 7 — Cross-card scan before writing any YAML:**

Run this scan in two named phases. Do not write any YAML file until both phases pass.

```
CROSS-CARD UNIQUENESS SCAN:

  Phase 1 — Anchor-Orthogonality:
    List the ANCHOR-CARD primary question.
    For each non-anchor role: write its primary question.
    For each non-anchor role: could this question and the anchor question both be asked
      by the same role? Mark PASS or FLAG.
    Revise all flagged non-anchor questions before starting Phase 2.

  Phase 2 — Non-Anchor Pairwise:
    For each pair of non-anchor roles: could both questions be asked by the same role type?
    Mark PASS or FLAG per pair.
    Revise all flagged questions before writing any YAML.
```

---

**Step 8 — Write YAML files (inertia-advocate first):**

Write in order: inertia-advocate, then domain experts, then remaining stock roles.

```yaml
---
name: {from Diagnosis Card; sourcing confirmed}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

# Inertia-advocate ONLY:
anchor: true

# All non-inertia-advocate roles ONLY:
orthogonality: "{from Diagnosis Card 'Orthogonality to ANCHOR-CARD' — copy verbatim;
  must name a contrast axis, not be generic}"

# Domain expert roles ONLY:
inertia_gap_inherited: "{GAP-{slug}: [inertia resistance verbatim from INERTIA-GAP ANALYSIS]}"

orientation:
  frame: |
    {from Diagnosis Card Frame — epistemic viewpoint, not a task list}
  serves: |
    {from Diagnosis Card Serves — beneficiary, not a frame restatement}

lens:
  verify_questions:
    - "{primary question from Diagnosis Card}"
    - "{second question — uniquely attributable to this role's frame}"

  simplify_rules:
    - "{opinionated exclusion: 'Skip X unless Y.'}"

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
  - {registry members only — no phantom names, no "all roles"}
```

Checklist before writing each file:
- [ ] `verify_questions` and `simplify_rules` spelled exactly as committed in Step 1
- [ ] `orthogonality` present for all non-anchor roles; absent from ANCHOR-CARD
- [ ] `inertia_gap_inherited` present for domain expert roles; absent from stock/anchor
- [ ] No PHANTOM names in collaborates_with
- [ ] No UNIVERSALIST listing in collaborates_with

---

**Step 9 — Write REGISTRY.md:**

Count the files written in Step 8. Record this as PHASE5_COUNT. Do not add up prior-phase
counts — enumerate the actual files written.

Write `.roles/{area}/REGISTRY.md`:

```
---
area: {area}
generated: {date}
---

## Registry Summary

total_roles: {PHASE5_COUNT}

stock_roles:
  - inertia-advocate  (ANCHOR-CARD — written first; source: Phase 2 / Step 2)
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
  {Step 2 status-quo claim — exact words, not paraphrased; fulfills EXTENSION-COMMITMENT}

Generated by: /org-roles {topic} — {date}
```

HEADING STUB RULE: If any field in this template is empty or a placeholder, stop and fill it.
A section header with nothing real below it is a C-10 failure.

---

**Final checklist — confirm before declaring done:**

Phase output (C-37): inertia-advocate YAML has `anchor: true`; all other YAML files have
`orthogonality` field with a named contrast axis tracing to the anchor's primary question

Scan structure (C-38): CROSS-CARD UNIQUENESS SCAN ran two named phases — Phase 1
(Anchor-Orthogonality) and Phase 2 (Non-Anchor Pairwise) — per-role records written

Gap artifact (C-39): INERTIA-GAP ANALYSIS block with named GAP-{slug} identifiers was
written before any expert was named in Step 4

Expert sourcing (C-40): every expert name has a POSITIVE SOURCING statement citing the
specific GAP-{slug} identifier and domain vocabulary term used in the name

Provenance (C-41): every domain expert Diagnosis Card has `inertia gap inherited` citing
"GAP-{slug}: [resistance verbatim]" — not a positional reference ("Gap 1")
