---
skill: quest-variate
skill_target: org-roles
date: 2026-03-16
round: R12
rubric_version: v12
status: variate
---

# org-roles Variate — Round 12

**Date:** 2026-03-16
**Skill:** org-roles
**Rubric:** v12 (C-01 through C-52; new in v12: C-50 SCAN ORDERING GATE declared-constraint
block, C-51 pipeline-wide criterion-ID annotation, C-52 PROVENANCE-CHAIN DECLARATION
pre-writing artifact — all derived from R11 excellence signals)
**Round:** R12 — single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

**Context:** R11 V-05 closed the v12 frontier at 100.00 (44/44) — all three new criteria
pass. The v12 ceiling is 44/44. R12 variates all inherit R11 V-05's formal Phase register and
its three mechanisms (SCAN ORDERING GATE, criterion-ID propagation, PROVENANCE-CHAIN
DECLARATION in Phase 0) as the base. All five variations must maintain 100.00 under v12 while
discovering new forcing mechanisms that could surface as C-53+ in v13.

**Post-ceiling framing:** Three candidate strengthening patterns identified from R11 V-05
analysis:

1. **Gap coverage as formally verified gate event** — C-22 prevents count-bypass by requiring
   PHASE5_COUNT from Phase 5 enumeration, not prior-phase plans. The `coverage_gaps` field in
   REGISTRY.md has a parallel bypass class: deriving coverage_gaps from memory of the plan
   rather than from a formal per-gap enumeration. A COVERAGE-GATE that walks each GAP-{slug}
   before writing REGISTRY.md — confirming each gap is either covered by a named expert file
   or recorded as a formal gap entry — turns coverage assurance into a verifiable pipeline
   event, parallel to count-bypass prevention.

2. **Orthogonality completeness as standalone table artifact** — C-35 is satisfied by presence
   of the `Orthogonality to ANCHOR-CARD` field in each Diagnosis Card. But orthogonality axes
   across the full registry are currently verifiable only by reading every card individually.
   An ORTHOGONALITY COMPLETENESS TABLE produced after all Diagnosis Cards — listing every
   non-anchor role's named contrast axis against the ANCHOR primary question, with
   PASS/FLAG per axis — makes the full set of orthogonality claims navigable as a single
   cross-role artifact, parallel to how the Phase 1 enumeration makes verify questions
   navigable before the scan runs.

3. **Anchor sourcing parity with domain experts** — C-40/C-45 require domain experts to carry
   explicit POSITIVE SOURCING statements tracing their names to specific GAP-{slug} vocabulary.
   The ANCHOR-CARD name requires a domain-specific slug from Step 2 vocabulary, but there is
   no explicit positive-sourcing statement in the ANCHOR-CARD template — only a "sourcing
   check" narrative. Elevating the anchor to carry a formal ANCHOR-SOURCING statement
   ("this name derives from INERTIA-SURFACE: [specific term from status-quo claim vocabulary]")
   creates sourcing parity: every named role in the registry, including the anchor, carries an
   explicit named-source declaration with the same structural format.

---

## Round 12 Variation Map

| V | Axis | Primary new pattern | Hypothesis |
|---|------|---------------------|------------|
| V-01 | lifecycle emphasis | COVERAGE-GATE — formal per-gap coverage verification before REGISTRY write | C-22 prevents count-bypass; COVERAGE-GATE prevents the parallel coverage-bypass by requiring per-GAP-{slug} enumeration before `coverage_gaps` is populated — potential C-53 |
| V-02 | output format | ORTHOGONALITY COMPLETENESS TABLE — cross-role table of all contrast axes after Diagnosis Cards, before YAML | C-35 satisfied by per-card orthogonality field; a table that presents all contrast axes against the anchor as a single navigable artifact generalizes the mechanism to pipeline level — potential C-53 |
| V-03 | inertia framing | ANCHOR-SOURCING STATEMENT — explicit positive-sourcing declaration for the inertia-advocate name, parallel to domain expert pattern | C-40/C-45 require explicit sourcing for domain experts; a symmetric ANCHOR-SOURCING statement that traces the anchor name to INERTIA-SURFACE vocabulary creates sourcing parity across all registry roles — potential C-53 |
| V-04 | V-01+V-02 combined | COVERAGE-GATE + ORTHOGONALITY COMPLETENESS TABLE | Full synthesis: gap coverage as formal gate event AND cross-role orthogonality table before YAML |
| V-05 | V-01+V-02+V-03 + register | All three patterns + imperative Step register (vs formal Phase) | Tests whether all three new mechanisms survive a register change back to imperative Steps; R11 V-05 used formal Phase register — V-05 R12 takes all new mechanisms back into imperative register to test robustness |

---

## V-01 — Single-Axis: COVERAGE-GATE

**axis:** lifecycle emphasis
**hypothesis:** R11 V-05 achieves C-22 and C-27 by requiring PHASE5_COUNT from Phase 5
actual enumeration, explicitly forbidding derivation from prior-phase plans. An identical
bypass class exists for `coverage_gaps` in REGISTRY.md: the current pipeline writes
coverage_gaps from memory of what was and wasn't done, with no formal per-gap verification
step. This variate adds a COVERAGE-GATE before writing REGISTRY.md — a block that walks
each GAP-{slug} from Phase 2 INERTIA-GAP ANALYSIS, confirms whether a domain expert file
was written for it in Phase 5, and explicitly marks each gap COVERED or GAP. The
`coverage_gaps` field in REGISTRY.md is then populated from this enumeration, not from
memory. All other elements identical to R11 V-05.
Falsifiable: if the evaluator treats COVERAGE-GATE as a paraphrase of C-22/C-27 (the same
count-bypass prevention at a different field), no new criterion emerges and V-01 equals R11
V-05 under v12. If the gate asserts something structurally distinct — a per-artifact coverage
enumeration rather than a per-file count — a new C-53 criterion emerges for v13.

---

You are running `/org-roles {topic}`.

---

PHASE 0 — FIELD CONTRACT, EXTENSION COMMITMENT, AND PROVENANCE CHAINS

Before reading any context, establish all binding specifications.

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

**PROVENANCE-CHAIN DECLARATION:**

```
PROVENANCE-CHAIN DECLARATION for /org-roles {topic}:

  Chain A — Inertia gap provenance:
    Source:      Phase 2 INERTIA-GAP ANALYSIS — field: GAP-{slug}.Inertia resistance
    Transit:     Phase 5 Diagnosis Card — field: inertia gap inherited
    Destination: Phase 5 YAML role file — field: inertia_gap_inherited [FC-12]
    Integrity rule: copy verbatim at each transit; cite GAP-{slug} by name throughout;
      positional reference ("Gap 1") at destination breaks Chain A and fails [FC-12]

  Chain B — Orthogonality provenance:
    Source:      Phase 5 CROSS-CARD UNIQUENESS SCAN + ANCHOR-CARD primary question
    Transit:     Phase 5 Diagnosis Card — field: Orthogonality to ANCHOR-CARD
    Destination: Phase 5 YAML role file — field: orthogonality [FC-11]
    Integrity rule: copy verbatim from Diagnosis Card to YAML; must name contrast axis
      tracing to ANCHOR-CARD primary question; generic assertion breaks Chain B

  Chain C — Inertia surface provenance:
    Source:      Phase 1 INERTIA-SURFACE — field: Status-quo claim
    Transit:     Phase 5 ANCHOR-CARD Frame — rephrased as epistemic stance
    Destination: Phase 6 REGISTRY.md — field: inertia_surface
    Integrity rule: inertia_surface uses exact words of Status-quo claim; ANCHOR-CARD
      Frame may rephrase but traces to same claim; fulfills EXTENSION-COMMITMENT
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT written with all three elements; `field_name` = `inertia_surface`;
   purpose references Phase 0 diagnostic question [C-23/C-30]
2. FIELD-CONTRACT written with all twelve items [FC-1] through [FC-12] [C-26]
3. [FC-1] contains both PROHIBITED NAMES clause and POSITIVE SOURCING REQUIRED clause [C-28/C-31]
4. [FC-4] and [FC-5] display exact identifier strings `verify_questions` and `simplify_rules`
   under EXACT IDENTIFIER labels [C-24/C-07]
5. [FC-10] carries CONTRACT VIOLATION (type 1) and (type 2) labels [C-29]
6. [FC-11] written with REQUIRED and REQUIRED FORMAT; states YAML persistence [C-46]
7. [FC-12] written with REQUIRED and REQUIRED FORMAT citing GAP-{slug}; states YAML
   persistence and that positional-only reference fails [C-47]
8. PROVENANCE-CHAIN DECLARATION written with all three chains; each chain names Source,
   Transit, Destination, and Integrity rule [C-52]

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
The status-quo claim is copied verbatim to `inertia_surface` in Phase 6 (Chain C source).

**GATE** — Phase 1 complete when ALL of the following are TRUE:
1. INERTIA-SURFACE block written with status-quo claim naming a specific capability [C-02]
2. At least three challenge questions using `{topic}` vocabulary
3. No domain expert names appear [C-39 precondition]

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

  GAP-{domain-slug-2}: ...
  GAP-{domain-slug-3}: ...

  (minimum three named gaps; GAP-{slug} identifier must derive from Domain vocabulary)
```

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
1. INERTIA-GAP ANALYSIS written before DOMAIN-ANALYSIS; at least three named gaps in
   GAP-{slug} format, each with Domain, Failure mode, Inertia resistance [C-39/C-44]
2. GAP-{slug} identifiers derive from their respective Domain vocabularies [C-44]
3. Each derived expert lists all five attributes including POSITIVE SOURCING statement [C-45]
4. POSITIVE SOURCING statement cites specific GAP-{slug} and domain vocabulary term [C-45/C-40]
5. No placeholder names per [FC-1]; no stock role names [C-28/C-31] — checkpoint 2 of 3

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

All non-anchor roles carry `orthogonality` per [FC-11] in their YAML files (Chain B destination).
Domain expert roles carry `inertia_gap_inherited` per [FC-12] in their YAML files (Chain A destination).

**GATE** — Phase 3 complete when ALL of the following are TRUE:
1. STOCK-ROLES lists all four names with lens descriptors [C-03]
2. inertia-advocate explicitly designated ANCHOR-CARD with write-first mandate for Phase 5 [C-37]
3. [FC-11] and [FC-12] field assignments confirmed for respective role types [C-46/C-47]
4. Phase 1 INERTIA-SURFACE confirmed available as Chain C source

---

PHASE 4 — OUTPUT AREA

```
OUTPUT-AREA: .craft/roles/{area}/
```

Area slug uses GAP-{slug} Domain vocabulary from Phase 2. NOT: `default`, `generic`, `roles`.

**GATE** — Phase 4 complete when ALL of the following are TRUE:
1. OUTPUT-AREA written with area slug from Phase 2 GAP Domain vocabulary [C-04]
2. Path format is exactly `.craft/roles/{area}/`

---

PHASE 5 — DIAGNOSIS CARDS AND ROLE FILE WRITING

**PREPARE:** Confirm inputs before writing any Diagnosis Card:
- Phase 0 [FC-4] exact identifier: `verify_questions` (retrieve verbatim) [C-07/C-24]
- Phase 0 [FC-5] exact identifier: `simplify_rules` (retrieve verbatim) [C-07/C-24]
- Phase 0 [FC-11] REQUIRED FORMAT for `orthogonality` YAML field (retrieve verbatim) [C-46]
- Phase 0 [FC-12] REQUIRED FORMAT for `inertia_gap_inherited` YAML field (retrieve verbatim) [C-47]
- Phase 0 PROVENANCE-CHAIN DECLARATION: all three chains confirmed [C-41/C-46/C-47/C-52]
- Phase 1 INERTIA-SURFACE: status-quo claim and challenge questions confirmed [C-02]
- Phase 2 INERTIA-GAP ANALYSIS: all GAP-{slug} entries confirmed [C-39/C-44]
- Phase 2 DOMAIN-ANALYSIS: expert names with POSITIVE SOURCING confirmed [C-40/C-45]
- Phase 3 STOCK-ROLES: four names; inertia-advocate ANCHOR-CARD confirmed [C-03/C-37]
- Phase 4 OUTPUT-AREA path confirmed [C-04]

PREPARE complete when all ten inputs confirmed. Do not begin Diagnosis Cards until confirmed.

**ANCHOR-CARD (write first):**

```
ANCHOR-CARD for inertia-advocate:

  name: {domain-vocabulary slug — confirmed against [FC-1]}
  [FC-1] name check: domain-specific because [vocabulary source]; NOT placeholder; confirmed

  frame (one sentence): {Phase 1 status-quo claim as epistemic stance — Chain C transit}
  serves (one sentence): {beneficiary — NOT a frame restatement}

  primary_verify_question: {most adversarial "why is the status quo sufficient?" —
    this is the Phase 5 reference axis for the CROSS-CARD UNIQUENESS SCAN;
    this is Chain B source for all non-anchor orthogonality fields}
  uniqueness argument: uniquely attributable to inertia-advocate because [reason];
    confirmed distinct
  anchor status: ANCHOR-CARD — primary question is Phase 5 scan reference axis;
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
    verbatim]" — Chain A transit, cite by GAP-{slug} name per [FC-12]; for stock: N/A}
  orthogonality to ANCHOR-CARD: {per [FC-11] REQUIRED FORMAT — Chain B transit — named
    contrast axis tracing how this role's concern falls outside the anchor's sufficiency
    question; this value copied verbatim to YAML `orthogonality` field}

  primary_verify_question: {most role-specific question for this frame}
  uniqueness argument: [reason]; confirmed distinct

  collaborates_with draft: [{name-1}, {name-2}]; phantom check: confirmed
```

After all Diagnosis Cards, run **CROSS-CARD UNIQUENESS SCAN**:

```
CROSS-CARD UNIQUENESS SCAN (ANCHOR-CARD as reference axis):

  Phase 1 — Enumerate All Verify Questions:
    List every primary_verify_question from every Diagnosis Card (ANCHOR-CARD first).
    Format: [role-name]: "[question text]"
    Scope: enumeration only — no checking, no flagging in this phase.
    Enumeration complete when every card's primary question appears exactly once.

  Phase 2 — Anchor-Orthogonality Check:
    Using the Phase 1 enumeration as reference list:
    State the ANCHOR-CARD primary_verify_question (from Phase 1).
    For each non-anchor role: retrieve its question from Phase 1.
    Test: could this role's question and the anchor question both be asked by the same role?
    Mark PASS or FLAG per non-anchor role. Resolve all flags before Phase 3.

  Phase 3 — Non-Anchor Pairwise Check:
    Using Phase 1 enumeration (non-anchor entries only) as reference:
    For each pair of non-anchor roles: compare primary_verify_questions.
    Test: could both questions be asked by the same role type?
    Flag any pair where both questions serve the same epistemic purpose.
    Record PASS or FLAG per pair. Do not begin Phase 4 until Phase 3 records are written.

  Phase 4 — Revision and Resolution:
    Collect all flags from Phase 2 and Phase 3.
    For each flagged role or pair: rewrite the flagged primary_verify_question to remove
      the overlap. Record the revised question and the reason it is now distinct.
    Phase 4 complete when all flags resolved and revisions recorded.
    Do not write any YAML file until Phase 4 is complete.
```

**SCAN ORDERING GATE** — confirm before writing any YAML:
- [ ] Phase 1 (Enumerate) executed first; no checking occurred in Phase 1 [C-42]
- [ ] Phase 2 (Anchor-Orthogonality) executed after Phase 1 was complete and before Phase 3 began [C-50]
- [ ] Phase 3 (Non-Anchor Pairwise) executed after Phase 2 was complete and before Phase 4 began [C-50]
- [ ] Phase 4 (Revision and Resolution) executed last; collected flags from Phase 2 AND Phase 3 [C-43]
- [ ] No two consecutive phases share a label; no phase merged with an adjacent phase [C-48]
- [ ] Canonical sequence confirmed: Phase 1 (Enumerate) → Phase 2 (Anchor-Orthogonality) →
     Phase 3 (Non-Anchor Pairwise) → Phase 4 (Revision-Resolution) [C-48]

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
orthogonality: "{Chain B destination — per [FC-11] REQUIRED FORMAT — named contrast axis
  from Diagnosis Card verbatim; traces to ANCHOR-CARD primary question, not generic}"

# Domain expert roles only (omit from stock roles and inertia-advocate):
inertia_gap_inherited: "{Chain A destination — per [FC-12] REQUIRED FORMAT:
  GAP-{slug}: [resistance verbatim]; not positional}"

orientation:
  frame: |
    {Per [FC-2]. FAILURE MODE: task-list frame.}
  serves: |
    {Per [FC-3] — NOT a frame restatement.}

lens:
  verify_questions:
    - "{Primary verify question — uniqueness confirmed in scan}"
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
  # CONTRACT VIOLATION (type 1) — PHANTOM: a name absent from this registry [C-29]
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent [C-29]
```

Checklist before writing each file [C-51: each item names its governing criterion]:
- [ ] `verify_questions` spelled exactly as in [FC-4] EXACT IDENTIFIER [C-07/FC-4]
- [ ] `simplify_rules` spelled exactly as in [FC-5] EXACT IDENTIFIER [C-07/FC-5]
- [ ] `orthogonality` present per [FC-11] for all non-anchor roles; absent from ANCHOR-CARD [C-46]
- [ ] `inertia_gap_inherited` present per [FC-12] for domain experts; absent from stock/anchor [C-47]
- [ ] `anchor: true` in inertia-advocate file only [C-37]
- [ ] No PHANTOM names in `collaborates_with` — CONTRACT VIOLATION (type 1) [C-29/C-33]
- [ ] No UNIVERSALIST listing in `collaborates_with` — CONTRACT VIOLATION (type 2) [C-29/C-33]

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. ANCHOR-CARD Diagnosis Card written first; all subsequent cards written after [C-37]
2. All non-anchor Diagnosis Cards include `orthogonality to ANCHOR-CARD` per [FC-11] [C-35]
3. All domain expert Diagnosis Cards include `inertia gap inherited` citing GAP-{slug} [C-41]
4. CROSS-CARD UNIQUENESS SCAN run with Phase 1 (Enumerate), Phase 2 (Anchor-Orthogonality),
   Phase 3 (Non-Anchor Pairwise), Phase 4 (Revision and Resolution); SCAN ORDERING GATE
   confirmed with all six items checked; Phase 4 complete before YAML writing began [C-42/C-43/C-48/C-50]
5. One `.md` file per role; inertia-advocate (ANCHOR-CARD) written first [C-37]
6. ANCHOR-CARD YAML: `anchor: true`; NO `orthogonality`; NO `inertia_gap_inherited` [C-37]
7. Non-anchor YAML: `orthogonality` field per [FC-11] REQUIRED FORMAT — not generic [C-46]
8. Domain expert YAML: `inertia_gap_inherited` per [FC-12] citing GAP-{slug} — not positional [C-47]
9. All YAML files use exact identifiers `verify_questions` and `simplify_rules` verbatim [C-07]
10. No prohibited names per [FC-1]; no collaborates_with CONTRACT VIOLATION; labels mirrored
    in template annotation per [C-33] [C-28/C-29/C-33]
11. PROVENANCE-CHAIN DECLARATION Chain A, B, C each traceable through Diagnosis Cards to YAML [C-52]
12. Per-file checklist items carry criterion-ID annotations [C-51]

---

PHASE 6 — REGISTRY SUMMARY

**COVERAGE-GATE** — before writing REGISTRY.md, verify gap coverage from Phase 2 enumeration:

```
COVERAGE-GATE for /org-roles {topic}:

  Walk each GAP-{slug} from Phase 2 INERTIA-GAP ANALYSIS:

    GAP-{slug-1}:
      Expert derived: {expert name from Phase 2 DOMAIN-ANALYSIS, or "none"}
      Expert file written in Phase 5: {filename, or "none written"}
      Coverage status: COVERED | GAP
      If GAP: record as coverage gap entry below

    GAP-{slug-2}: ...
    GAP-{slug-3}: ...

  Coverage summary:
    Covered gaps: {count} — {list of GAP-{slug} identifiers}
    Uncovered gaps: {count} — {list of GAP-{slug} identifiers; or "none"}

  NOTE: `coverage_gaps` in REGISTRY.md is populated from "Uncovered gaps" above.
  Coverage-bypass failure class applies: deriving coverage_gaps from memory rather
  than from this enumeration is a bypass that fails [C-22 parallel].
```

COVERAGE-GATE complete when all Phase 2 gaps enumerated and coverage status recorded.
Do not write REGISTRY.md until COVERAGE-GATE is complete.

**PREPARE:** Enumerate `.md` files written in Phase 5. Record as `PHASE5_COUNT`.
This count must come from Phase 5 enumeration only — not from adding prior-phase planned
counts. Count-bypass failure class applies: deriving the count from prior-phase plans
rather than Phase 5 actual output is a bypass that fails [C-27/C-32].

PREPARE complete when `PHASE5_COUNT` recorded from Phase 5 actual enumeration.

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
  {from COVERAGE-GATE "Uncovered gaps" enumeration — not from memory;
   or "none detected" if COVERAGE-GATE confirmed zero uncovered gaps}

inertia_surface: |
  {Phase 1 status-quo claim verbatim — Chain C destination; fulfills EXTENSION-COMMITMENT}

Generated by: /org-roles {topic} — {date}
```

HEADING STUB FAIL CONDITION: Section headers with empty or omitted values beneath them
fail C-10. Every field must contain substantive content.

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. COVERAGE-GATE written and complete; every Phase 2 GAP-{slug} enumerated with
   coverage status [C-10/C-22 parallel]
2. `coverage_gaps` populated from COVERAGE-GATE "Uncovered gaps" enumeration — not memory
3. `REGISTRY.md` exists at `.craft/roles/{area}/REGISTRY.md` [C-04]
4. `total_roles` equals `PHASE5_COUNT` from Phase 5 enumeration [C-22/C-27]
5. `domain_experts` lists each expert with `name`, `gap_source` (GAP-{slug}),
   `inertia_gap` (verbatim) [C-10]
6. `inertia_surface` contains Phase 1 status-quo claim verbatim [C-20/C-23] — Chain C
   destination integrity verified
7. No heading stubs; HEADING STUB FAIL CONDITION was read before writing began [C-15]
8. PROVENANCE-CHAIN DECLARATION Chain C integrity confirmed: inertia_surface exact words
   match Phase 1 Status-quo claim [C-52]

---

**Final checklist — confirm before declaring done:**

Phase output (C-37/C-46): inertia-advocate YAML has `anchor: true`; all other YAML files
have `orthogonality` field with named contrast axis tracing to ANCHOR-CARD primary question

Scan structure (C-38/C-42/C-43/C-48/C-50): CROSS-CARD UNIQUENESS SCAN ran four named phases
in canonical sequence; SCAN ORDERING GATE confirmed (all six per-transition assertions
checked); canonical sequence Phase 1→2→3→4 verified; no phases merged; Phase 4 complete
before any YAML written

Gap artifact (C-39/C-44): INERTIA-GAP ANALYSIS block with formal GAP-{slug} identifiers
written before any expert was named in Phase 2

Expert sourcing (C-40/C-45): every expert has a POSITIVE SOURCING statement citing the
specific GAP-{slug} identifier and domain vocabulary term used in the name, embedded inline
in the derivation record

Provenance chains declared and verified (C-52): PROVENANCE-CHAIN DECLARATION written in
Phase 0 with all three chains; Chain A traced per domain expert to YAML; Chain B traced per
non-anchor role to YAML orthogonality field; Chain C traced to Phase 6 REGISTRY.md
inertia_surface (verbatim from Phase 1)

Contract violations (C-29/C-33): `collaborates_with` in every YAML file includes CONTRACT
VIOLATION (type 1) — PHANTOM [C-29] and CONTRACT VIOLATION (type 2) — UNIVERSALIST [C-29]
comments; labels mirrored in template [C-33]; phantom check confirmed per file

Pipeline criterion annotations (C-51): every gate item and per-file checklist item carries
[C-NN] annotation naming its governing criterion

Coverage gate (new): COVERAGE-GATE enumerated every Phase 2 GAP-{slug}; coverage_gaps in
REGISTRY.md populated from enumeration, not memory

---

## V-02 — Single-Axis: ORTHOGONALITY COMPLETENESS TABLE

**axis:** output format
**hypothesis:** R11 V-05 achieves C-35 because every non-anchor Diagnosis Card carries an
`Orthogonality to ANCHOR-CARD` field with a named contrast axis. But the full set of
contrast axes across the registry is only verifiable by reading every card individually —
there is no single cross-role artifact that makes orthogonality completeness navigable at a
glance. This variate adds an ORTHOGONALITY COMPLETENESS TABLE after all Diagnosis Cards and
before the CROSS-CARD UNIQUENESS SCAN. The table lists every non-anchor role with its named
contrast axis and a PASS/FLAG per axis — asserting not only that each axis is present, but
that the axes themselves are pairwise distinct (no two non-anchor roles claim the same named
contrast axis against the anchor). The SCAN ORDERING GATE is then extended to include an
ORTHOGONALITY TABLE item. All other elements identical to R11 V-05.
Falsifiable: if the evaluator treats the ORTHOGONALITY COMPLETENESS TABLE as a paraphrase of
C-35 (same orthogonality check reformatted), no new criterion emerges and V-02 equals R11
V-05 under v12. If the table asserts a cross-role property (axis pairwise distinctness) not
captured by per-card orthogonality fields alone, a new C-53 criterion emerges for v13.

---

You are running `/org-roles {topic}`.

---

PHASE 0 — FIELD CONTRACT, EXTENSION COMMITMENT, AND PROVENANCE CHAINS

Before reading any context, establish all binding specifications.

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

**PROVENANCE-CHAIN DECLARATION:**

```
PROVENANCE-CHAIN DECLARATION for /org-roles {topic}:

  Chain A — Inertia gap provenance:
    Source:      Phase 2 INERTIA-GAP ANALYSIS — field: GAP-{slug}.Inertia resistance
    Transit:     Phase 5 Diagnosis Card — field: inertia gap inherited
    Destination: Phase 5 YAML role file — field: inertia_gap_inherited [FC-12]
    Integrity rule: copy verbatim at each transit; cite GAP-{slug} by name throughout;
      positional reference ("Gap 1") at destination breaks Chain A and fails [FC-12]

  Chain B — Orthogonality provenance:
    Source:      Phase 5 CROSS-CARD UNIQUENESS SCAN + ANCHOR-CARD primary question
    Transit:     Phase 5 Diagnosis Card — field: Orthogonality to ANCHOR-CARD
    Destination: Phase 5 YAML role file — field: orthogonality [FC-11]
    Integrity rule: copy verbatim from Diagnosis Card to YAML; must name contrast axis
      tracing to ANCHOR-CARD primary question; generic assertion breaks Chain B

  Chain C — Inertia surface provenance:
    Source:      Phase 1 INERTIA-SURFACE — field: Status-quo claim
    Transit:     Phase 5 ANCHOR-CARD Frame — rephrased as epistemic stance
    Destination: Phase 6 REGISTRY.md — field: inertia_surface
    Integrity rule: inertia_surface uses exact words of Status-quo claim; ANCHOR-CARD
      Frame may rephrase but traces to same claim; fulfills EXTENSION-COMMITMENT
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT written with all three elements [C-23/C-30]
2. FIELD-CONTRACT written with all twelve items [FC-1] through [FC-12] [C-26]
3. [FC-1] contains PROHIBITED NAMES and POSITIVE SOURCING REQUIRED [C-28/C-31]
4. [FC-4]/[FC-5] display exact identifiers under EXACT IDENTIFIER labels [C-24/C-07]
5. [FC-10] carries CONTRACT VIOLATION (type 1) and (type 2) labels [C-29]
6. [FC-11] written with REQUIRED and REQUIRED FORMAT [C-46]
7. [FC-12] written with REQUIRED, REQUIRED FORMAT, and positional-reference failure [C-47]
8. PROVENANCE-CHAIN DECLARATION written with all three chains (Source/Transit/Destination/
   Integrity rule per chain) [C-52]

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
The status-quo claim is copied verbatim to `inertia_surface` in Phase 6 (Chain C source).

**GATE** — Phase 1 complete when ALL of the following are TRUE:
1. INERTIA-SURFACE block written with status-quo claim naming a specific capability [C-02]
2. At least three challenge questions using `{topic}` vocabulary
3. No domain expert names appear [C-39 precondition]

---

PHASE 2 — DOMAIN ANALYSIS

**Step 1 — INERTIA-GAP ANALYSIS:**

```
INERTIA-GAP ANALYSIS for {topic}:

  GAP-{domain-slug-1}:
    Domain: [named vocabulary domain for this gap]
    Failure mode: [specific failure the status quo cannot prevent]
    Inertia resistance: [what the Phase 1 inertia claim overlooks from this domain]

  GAP-{domain-slug-2}: ...
  GAP-{domain-slug-3}: ...
```

**Step 2 — EXPERT DERIVATION:**

```
DOMAIN-ANALYSIS for {topic}:
    - Expert name: [slug from GAP-{slug} Domain vocabulary]
      POSITIVE SOURCING: "this name derives from GAP-{slug} Domain vocabulary:
        [specific term from that vocabulary used in the name]"
      Named gap source: GAP-{slug}
      Inertia gap: [GAP-{slug} inertia resistance — copied verbatim]
      Domain-vocabulary frame: [per [FC-2]]
      Verify focus: [what artifact or behavior this expert checks first]
```

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. INERTIA-GAP ANALYSIS before DOMAIN-ANALYSIS; minimum three named gaps [C-39/C-44]
2. GAP-{slug} identifiers from Domain vocabularies [C-44]
3. Each expert: POSITIVE SOURCING citing GAP-{slug} and vocabulary term [C-45/C-40]
4. No placeholder or stock names [C-28/C-31] — checkpoint 2 of 3

---

PHASE 3 — STOCK ROLES

```
STOCK-ROLES:
  - inertia-advocate  (ANCHOR-CARD; frame from Phase 1; written first; anchor: true)
  - pm
  - architect
  - strategy
```

**GATE** — Phase 3 complete when [C-03/C-37/C-46/C-47] confirmed.

---

PHASE 4 — OUTPUT AREA

```
OUTPUT-AREA: .craft/roles/{area}/
```

Area slug from Phase 2 GAP Domain vocabulary. NOT: `default`, `generic`, `roles`.

**GATE** — Phase 4 complete when [C-04] confirmed.

---

PHASE 5 — DIAGNOSIS CARDS, ORTHOGONALITY TABLE, SCAN, AND ROLE FILES

**PREPARE:** Confirm Phase 0-4 inputs (ten items) before writing any Diagnosis Card.
[C-07/C-24/C-46/C-47/C-52/C-02/C-39/C-44/C-40/C-45/C-03/C-37/C-04]

**ANCHOR-CARD (write first):**

```
ANCHOR-CARD for inertia-advocate:
  name: {domain-vocabulary slug — [FC-1] confirmed}
  [FC-1] name check: domain-specific because [source]; NOT placeholder; confirmed
  frame: {Phase 1 status-quo claim as epistemic stance — Chain C transit}
  serves: {beneficiary — NOT frame restatement}
  primary_verify_question: {adversarial sufficiency question — Chain B source for all
    non-anchor orthogonality fields; Phase 5 scan reference axis}
  uniqueness argument: [reason]; confirmed distinct
  anchor status: ANCHOR-CARD
  collaborates_with draft: [{name-1}, {name-2}]; phantom check: confirmed
```

**SUBSEQUENT DIAGNOSIS CARDS (after ANCHOR-CARD):**

```
DIAGNOSIS-CARD for {role-name}:
  name: {from GAP-{slug} vocabulary (experts) or standard (stock); [FC-1] confirmed}
  [FC-1] name check: derives from GAP-{slug}: [term] (experts) / standard (stock)
  frame: {GAP-{slug} vocabulary (experts) / standard lens (stock)}
  serves: {beneficiary — NOT frame restatement}
  inertia gap inherited: {"GAP-{slug}: [verbatim]" — Chain A transit (experts); N/A (stock)}
  orthogonality to ANCHOR-CARD: {per [FC-11] REQUIRED FORMAT — Chain B transit;
    copied verbatim to YAML `orthogonality`}
  primary_verify_question: {role-specific question}
  uniqueness argument: [reason]; confirmed distinct
  collaborates_with draft: [{names}]; phantom check: confirmed
```

After all Diagnosis Cards, produce an **ORTHOGONALITY COMPLETENESS TABLE**:

```
ORTHOGONALITY COMPLETENESS TABLE for /org-roles {topic}:

  ANCHOR primary question: "[anchor's primary_verify_question from Diagnosis Card]"

  Non-anchor roles:
  | Role | Named contrast axis (from Orthogonality to ANCHOR-CARD) | Axis distinct from anchor | Axis distinct from all prior rows | Status |
  |------|----------------------------------------------------------|---------------------------|-----------------------------------|--------|
  | {role-1} | {contrast axis text} | YES/NO | YES/NO (first row: N/A) | PASS/FLAG |
  | {role-2} | {contrast axis text} | YES/NO | YES/NO | PASS/FLAG |
  | ...  | ...                  | ...    | ...                               | ...    |

  ORTHOGONALITY COMPLETENESS GATE:
  - [ ] Every non-anchor role appears in the table
  - [ ] Every contrast axis explicitly names the ANCHOR primary question scope
  - [ ] No two non-anchor roles share the same named contrast axis
  - [ ] All rows PASS

TABLE complete when all rows filled and GATE confirmed. Flag any duplicate or generic axes
and resolve by rewriting the Orthogonality to ANCHOR-CARD field in the relevant Diagnosis Card
before proceeding. Do not run the CROSS-CARD UNIQUENESS SCAN until TABLE is complete.
```

After ORTHOGONALITY COMPLETENESS TABLE, run **CROSS-CARD UNIQUENESS SCAN**:

```
CROSS-CARD UNIQUENESS SCAN (ANCHOR-CARD as reference axis):

  Phase 1 — Enumerate All Verify Questions:
    List every primary_verify_question (ANCHOR-CARD first). No checking in this phase.

  Phase 2 — Anchor-Orthogonality Check:
    State ANCHOR-CARD question. For each non-anchor: could both questions be asked by
    the same role? Mark PASS or FLAG per non-anchor role.

  Phase 3 — Non-Anchor Pairwise Check:
    For each pair of non-anchor roles: could both questions serve the same epistemic
    purpose? Mark PASS or FLAG per pair.

  Phase 4 — Revision and Resolution:
    Collect all flags from Phase 2 and Phase 3. Rewrite each flagged question.
    Record revision and reason. Phase 4 complete when all flags resolved.
```

**SCAN ORDERING GATE** — confirm before writing any YAML:
- [ ] ORTHOGONALITY COMPLETENESS TABLE written and all rows PASS before scan began [new]
- [ ] Phase 1 (Enumerate) executed first; no checking occurred in Phase 1 [C-42]
- [ ] Phase 2 (Anchor-Orthogonality) executed after Phase 1 was complete and before Phase 3 began [C-50]
- [ ] Phase 3 (Non-Anchor Pairwise) executed after Phase 2 was complete and before Phase 4 began [C-50]
- [ ] Phase 4 (Revision and Resolution) executed last; collected flags from Phase 2 AND Phase 3 [C-43]
- [ ] No two consecutive phases share a label; no phase merged with an adjacent phase [C-48]
- [ ] Canonical sequence confirmed: Table → Phase 1 → Phase 2 → Phase 3 → Phase 4 [C-48]

**WRITE:** One `.md` file per role. Order: anchor first, then experts, then stock.

```yaml
---
name: {[FC-1] confirmed}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}
anchor: true   # ANCHOR-CARD only
orthogonality: "{Chain B — per [FC-11]; verbatim from ORTHOGONALITY COMPLETENESS TABLE
  contrast axis; not generic}"   # non-anchor only
inertia_gap_inherited: "{Chain A — GAP-{slug}: [verbatim]; not positional}"   # experts only
orientation:
  frame: |
    {Per [FC-2].}
  serves: |
    {Per [FC-3].}
lens:
  verify_questions:
    - "{primary question}"
    - "{additional}"
  simplify_rules:
    - "{Per [FC-5]: 'Skip X unless Y.'}"
expertise:
  depth: {per [FC-6]}
  relevance: |
    {Per [FC-7].}
scope:
  primary: |
    {Per [FC-8].}
  boundary: |
    {Per [FC-9].}
collaborates_with:
  - {phantom check confirmed}
  # CONTRACT VIOLATION (type 1) — PHANTOM: a name absent from this registry [C-29]
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent [C-29]
```

Checklist before writing each file [C-51: each item names its governing criterion]:
- [ ] `verify_questions` exact as [FC-4] [C-07/FC-4]
- [ ] `simplify_rules` exact as [FC-5] [C-07/FC-5]
- [ ] `orthogonality` present per [FC-11] for non-anchor; absent from ANCHOR-CARD [C-46]
- [ ] `orthogonality` value matches ORTHOGONALITY COMPLETENESS TABLE contrast axis [C-35/new]
- [ ] `inertia_gap_inherited` per [FC-12] for experts; absent from stock/anchor [C-47]
- [ ] `anchor: true` in inertia-advocate only [C-37]
- [ ] No PHANTOM names — CONTRACT VIOLATION (type 1) [C-29/C-33]
- [ ] No UNIVERSALIST — CONTRACT VIOLATION (type 2) [C-29/C-33]

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. ANCHOR-CARD Diagnosis Card written first [C-37]
2. ORTHOGONALITY COMPLETENESS TABLE complete; all rows PASS; no duplicate axes [new]
3. CROSS-CARD UNIQUENESS SCAN: all four phases; SCAN ORDERING GATE confirmed [C-42/C-43/C-48/C-50]
4. Inertia gap inherited in all domain expert Diagnosis Cards [C-41]
5. YAML files written in correct order; anchor YAML first [C-37]
6. Chain A, B, C traceable from Diagnosis Cards to YAML output [C-52]
7. Per-file checklist criterion annotations present [C-51]

---

PHASE 6 — REGISTRY SUMMARY

**PREPARE:** Enumerate Phase 5 `.md` files. Record as `PHASE5_COUNT`.

**WRITE:** `.craft/roles/{area}/REGISTRY.md`

```
---
area: {area}
generated: {date}
---

## Registry Summary

total_roles: {PHASE5_COUNT}

stock_roles:
  - inertia-advocate  (ANCHOR-CARD)
  - pm
  - architect
  - strategy

domain_experts:
  - name: {expert-name}
    gap_source: GAP-{slug}
    inertia_gap: {verbatim}

coverage_gaps: |
  {Phase 2 gaps not covered by derived experts; or "none detected."}

inertia_surface: |
  {Phase 1 status-quo claim verbatim — Chain C destination}

Generated by: /org-roles {topic} — {date}
```

**GATE** — Phase 6 complete when [C-04/C-22/C-27/C-10/C-20/C-23/C-15/C-52] confirmed.

---

**Final checklist — confirm before declaring done:**

Phase output (C-37/C-46): anchor YAML has `anchor: true`; all non-anchor YAML have
`orthogonality` with named contrast axis; orthogonality values match ORTHOGONALITY TABLE

Scan structure (C-38/C-42/C-43/C-48/C-50): CROSS-CARD UNIQUENESS SCAN four named phases;
SCAN ORDERING GATE confirmed (seven items including TABLE gate)

Orthogonality completeness (new): ORTHOGONALITY COMPLETENESS TABLE written after all
Diagnosis Cards; every non-anchor role appears; all contrast axes distinct; all rows PASS

Gap/sourcing (C-39/C-44/C-40/C-45): INERTIA-GAP ANALYSIS before expert naming;
POSITIVE SOURCING per expert

Provenance chains (C-52): PROVENANCE-CHAIN DECLARATION in Phase 0; Chain A/B/C traced

Contract violations (C-29/C-33): labels in YAML template and per-file checklist

Pipeline criterion annotations (C-51): all gate items and checklist items carry [C-NN]

---

## V-03 — Single-Axis: ANCHOR-SOURCING STATEMENT

**axis:** inertia framing
**hypothesis:** R11 V-05 requires domain experts to carry a formal POSITIVE SOURCING
statement (inline in the derivation record, citing the specific GAP-{slug} identifier
and domain vocabulary term used in the name). This elevates expert names to formally
traced artifacts. The ANCHOR-CARD name, however, carries only a "sourcing check" narrative
("domain-specific because [vocabulary source]; confirmed") — structurally weaker than the
explicit POSITIVE SOURCING format applied to domain experts. This variate adds an explicit
ANCHOR-SOURCING statement to the ANCHOR-CARD template, with the same format used for domain
experts: "this name derives from INERTIA-SURFACE: [specific term from status-quo claim
vocabulary used in name]". The ANCHOR-SOURCING statement is added to both the Diagnosis
Card template and the pre-file checklist. All other elements identical to R11 V-05.
Falsifiable: if the evaluator treats ANCHOR-SOURCING as a paraphrase of the existing
sourcing check (same information in different format), no new criterion emerges and V-03
equals R11 V-05 under v12. If the explicit POSITIVE SOURCING format applied to the anchor
creates a structural property distinct from the narrative sourcing check — specifically,
that all named roles carry explicit named-source citations with vocabulary traceable to
named artifacts — a new C-53 criterion emerges for v13.

---

You are running `/org-roles {topic}`.

---

PHASE 0 — FIELD CONTRACT, EXTENSION COMMITMENT, AND PROVENANCE CHAINS

Before reading any context, establish all binding specifications.

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
          Domain experts: derive from GAP-{slug} vocabulary; POSITIVE SOURCING REQUIRED.
          Inertia-advocate: derive from INERTIA-SURFACE vocabulary; ANCHOR-SOURCING REQUIRED.
          POSITIVE SOURCING format: "this name derives from GAP-{slug}: [term used]"
          ANCHOR-SOURCING format: "this name derives from INERTIA-SURFACE: [term used]"
          BAD:  "domain-expert"; "status-quo-reviewer" with no named vocabulary source
          GOOD (expert): "retry-budget-compliance-analyst" — GAP-retry-semantics, term
                "retry-budget"
          GOOD (anchor): "integration-sufficiency-advocate" — INERTIA-SURFACE claim,
                term "integration sufficiency"

  [FC-2]  orientation.frame
          type: string — epistemic viewpoint ("sees X through the lens of Y")
          FAILURE MODE: task list / job description

  [FC-3]  orientation.serves
          type: string — beneficiary statement; NOT a restatement of frame
          FAILURE MODE: frame restatement

  [FC-4]  lens.verify_questions
          EXACT IDENTIFIER: verify_questions
          PROHIBITED IDENTIFIERS: verify | questions | checks | verify_list
          type: list; minimum two items; uniqueness argument required before writing

  [FC-5]  lens.simplify_rules
          EXACT IDENTIFIER: simplify_rules
          PROHIBITED IDENTIFIERS: simplify | rules | constraints | guidelines
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
          REQUIRED FORMAT: "[Named contrast axis] — this role's lens diverges from the
            ANCHOR-CARD because [specific reason naming the anchor's question and how
            this role's concern falls outside that question's scope]"

  [FC-12] inertia_gap_inherited
          Applies to: domain expert YAML files only
          REQUIRED FORMAT: "GAP-{slug}: [inertia resistance verbatim]"
          FAILURE MODE: positional reference ("Gap 1: ...")
```

**PROVENANCE-CHAIN DECLARATION:**

```
PROVENANCE-CHAIN DECLARATION for /org-roles {topic}:

  Chain A — Inertia gap provenance:
    Source:      Phase 2 INERTIA-GAP ANALYSIS — GAP-{slug}.Inertia resistance
    Transit:     Phase 5 Diagnosis Card — inertia gap inherited
    Destination: Phase 5 YAML — inertia_gap_inherited [FC-12]
    Integrity rule: verbatim at each transit; GAP-{slug} cited by name; positional breaks A

  Chain B — Orthogonality provenance:
    Source:      Phase 5 CROSS-CARD UNIQUENESS SCAN + ANCHOR-CARD primary question
    Transit:     Phase 5 Diagnosis Card — Orthogonality to ANCHOR-CARD
    Destination: Phase 5 YAML — orthogonality [FC-11]
    Integrity rule: verbatim copy; named contrast axis tracing to anchor question

  Chain C — Inertia surface provenance:
    Source:      Phase 1 INERTIA-SURFACE — Status-quo claim
    Transit:     Phase 5 ANCHOR-CARD Frame — rephrased as epistemic stance
    Destination: Phase 6 REGISTRY.md — inertia_surface
    Integrity rule: exact words at destination; ANCHOR-CARD Frame may rephrase

  Chain D — Anchor name provenance (new):
    Source:      Phase 1 INERTIA-SURFACE — Status-quo claim vocabulary
    Transit:     Phase 5 ANCHOR-CARD — ANCHOR-SOURCING statement
    Destination: Phase 5 ANCHOR-CARD YAML — name field [FC-1]
    Integrity rule: anchor name must contain a term traceable to INERTIA-SURFACE vocabulary;
      ANCHOR-SOURCING statement must cite the specific term used; generic anchor name breaks D
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT written [C-23/C-30]
2. FIELD-CONTRACT with all twelve items; [FC-1] includes ANCHOR-SOURCING format [C-26/C-28/C-31]
3. [FC-4]/[FC-5] exact identifiers under EXACT IDENTIFIER labels [C-24/C-07]
4. [FC-10] CONTRACT VIOLATION labels [C-29]
5. [FC-11] with REQUIRED FORMAT [C-46]; [FC-12] with REQUIRED FORMAT and positional failure [C-47]
6. PROVENANCE-CHAIN DECLARATION with all four chains (A, B, C, D); each with Source/Transit/
   Destination/Integrity rule [C-52/new]

---

PHASE 1 — INERTIA SURFACE

```
INERTIA-SURFACE for {topic}:
  Status-quo claim: [strongest argument {topic} is unnecessary; name specific capability]
  Challenge questions (minimum three; {topic} vocabulary):
    1. What specific failure does the status quo produce that this resolves?
    2. [what does existing mechanism already handle?]
    3. [minimum status-quo fix, and why insufficient?]
```

The status-quo claim vocabulary is the source for Chain D — anchor name must contain a term
traceable to this claim.

**GATE** — Phase 1 complete: status-quo claim names specific capability [C-02]; no expert
names appear [C-39 precondition]; at least three questions.

---

PHASE 2 — DOMAIN ANALYSIS

**Step 1 — INERTIA-GAP ANALYSIS:**

```
INERTIA-GAP ANALYSIS for {topic}:
  GAP-{slug}: Domain / Failure mode / Inertia resistance
  (minimum three; slugs from Domain vocabulary)
```

**Step 2 — EXPERT DERIVATION:**

```
DOMAIN-ANALYSIS for {topic}:
  - Expert name: [from GAP-{slug} vocabulary]
    POSITIVE SOURCING: "this name derives from GAP-{slug}: [term]"
    Named gap source: GAP-{slug}
    Inertia gap: [verbatim]
    Domain-vocabulary frame: [FC-2]
    Verify focus: [artifact or behavior checked first]
```

**GATE** — Phase 2 complete [C-39/C-44/C-45/C-40/C-28/C-31].

---

PHASE 3 — STOCK ROLES

```
STOCK-ROLES:
  - inertia-advocate  (ANCHOR-CARD; Chain C+D transit; written first; anchor: true)
  - pm / architect / strategy
```

**GATE** — Phase 3 complete [C-03/C-37/C-46/C-47].

---

PHASE 4 — OUTPUT AREA

```OUTPUT-AREA: .craft/roles/{area}/```

**GATE** — Phase 4 complete [C-04].

---

PHASE 5 — DIAGNOSIS CARDS, CROSS-CARD SCAN, AND ROLE FILE WRITING

**PREPARE:** Confirm all Phase 0-4 inputs before writing any Diagnosis Card.
Also confirm: Phase 1 INERTIA-SURFACE status-quo claim vocabulary available as Chain D source.

**ANCHOR-CARD (write first):**

```
ANCHOR-CARD for inertia-advocate:

  name: {slug containing a term from Phase 1 INERTIA-SURFACE vocabulary}
  ANCHOR-SOURCING: "this name derives from INERTIA-SURFACE: [specific term from
    status-quo claim vocabulary used in this name]"
    — Chain D transit; parallel to domain expert POSITIVE SOURCING format
  [FC-1] name check: traces to INERTIA-SURFACE vocabulary via ANCHOR-SOURCING; confirmed

  frame: {Phase 1 status-quo claim as epistemic stance — Chain C transit}
  serves: {beneficiary — NOT frame restatement}

  primary_verify_question: {adversarial sufficiency question — Chain B source;
    scan reference axis}
  uniqueness argument: confirmed distinct
  anchor status: ANCHOR-CARD

  collaborates_with draft: [{names}]; phantom check: confirmed
```

**SUBSEQUENT DIAGNOSIS CARDS (after ANCHOR-CARD):**

```
DIAGNOSIS-CARD for {role-name}:

  name: {from GAP-{slug} vocabulary (experts) / standard (stock)}
  POSITIVE SOURCING (experts): "this name derives from GAP-{slug}: [term]"
  [FC-1] name check: confirmed

  frame / serves / inertia gap inherited / orthogonality to ANCHOR-CARD /
  primary_verify_question / uniqueness argument / collaborates_with draft
  (per R11 V-05 template)
```

After all Diagnosis Cards, run **CROSS-CARD UNIQUENESS SCAN** (four phases):

```
Phase 1 — Enumerate All Verify Questions (no checking)
Phase 2 — Anchor-Orthogonality Check (PASS/FLAG per non-anchor)
Phase 3 — Non-Anchor Pairwise Check (PASS/FLAG per pair)
Phase 4 — Revision and Resolution (resolve all flags before YAML)
```

**SCAN ORDERING GATE** — confirm before writing any YAML:
- [ ] Phase 1 (Enumerate) executed first; no checking in Phase 1 [C-42]
- [ ] Phase 2 (Anchor-Orthogonality) after Phase 1 complete and before Phase 3 [C-50]
- [ ] Phase 3 (Non-Anchor Pairwise) after Phase 2 complete and before Phase 4 [C-50]
- [ ] Phase 4 (Revision) executed last; collected Phase 2 AND Phase 3 flags [C-43]
- [ ] No consecutive phases share a label; no phase merged [C-48]
- [ ] Canonical sequence Phase 1→2→3→4 confirmed [C-48]

**WRITE:** Anchor first, then experts, then stock.

```yaml
---
name: {[FC-1] sourcing confirmed}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}
anchor: true          # ANCHOR-CARD only; name traces to INERTIA-SURFACE via Chain D
orthogonality: "..."  # non-anchor only; Chain B destination [FC-11]
inertia_gap_inherited: "..."  # domain experts only; Chain A destination [FC-12]
orientation:
  frame: |
    {[FC-2]}
  serves: |
    {[FC-3]}
lens:
  verify_questions:
    - "{primary question}"
    - "{additional}"
  simplify_rules:
    - "{'Skip X unless Y.'}"
expertise:
  depth: {[FC-6]}
  relevance: |
    {[FC-7]}
scope:
  primary: |
    {[FC-8]}
  boundary: |
    {[FC-9]}
collaborates_with:
  - {phantom check confirmed}
  # CONTRACT VIOLATION (type 1) — PHANTOM: a name absent from this registry [C-29]
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent [C-29]
```

Checklist before writing each file [C-51: each item names its governing criterion]:
- [ ] `verify_questions` exact as [FC-4] [C-07/FC-4]
- [ ] `simplify_rules` exact as [FC-5] [C-07/FC-5]
- [ ] ANCHOR-CARD: `anchor: true`; ANCHOR-SOURCING in Diagnosis Card names INERTIA-SURFACE
      vocabulary term [FC-1/new]
- [ ] Non-anchor: `orthogonality` per [FC-11]; absent from ANCHOR-CARD [C-46]
- [ ] Domain experts: `inertia_gap_inherited` per [FC-12] [C-47]
- [ ] No PHANTOM names [C-29/C-33]; no UNIVERSALIST [C-29/C-33]

**GATE** — Phase 5 complete: ANCHOR-SOURCING present in ANCHOR-CARD Diagnosis Card;
Chain D traceable from INERTIA-SURFACE vocabulary to anchor name; all other Phase 5
conditions from R11 V-05 [C-37/C-35/C-41/C-42/C-43/C-48/C-50/C-52/C-51].

---

PHASE 6 — REGISTRY SUMMARY

PREPARE + WRITE REGISTRY.md (per R11 V-05 structure).

The `inertia_surface` field in REGISTRY.md is Chain C AND Chain D adjacent: the
status-quo claim that both provides the anchor name vocabulary (Chain D) and populates
the extension field (Chain C) appears verbatim here.

**GATE** — Phase 6 complete [C-04/C-22/C-27/C-10/C-20/C-23/C-15/C-52].

---

**Final checklist — confirm before declaring done:**

Phase output (C-37/C-46): anchor YAML has `anchor: true`; non-anchor YAML have `orthogonality`

Anchor sourcing (new): ANCHOR-CARD carries ANCHOR-SOURCING statement citing INERTIA-SURFACE
vocabulary; Chain D traces from status-quo claim vocabulary to anchor name in Diagnosis Card
to anchor YAML name field; anchor sourcing format mirrors domain expert POSITIVE SOURCING

Scan structure (C-38/C-42/C-43/C-48/C-50): four named phases; SCAN ORDERING GATE confirmed

Gap artifact (C-39/C-44): INERTIA-GAP ANALYSIS before expert naming

Expert sourcing (C-40/C-45): POSITIVE SOURCING per expert

Provenance chains (C-52): PROVENANCE-CHAIN DECLARATION with all four chains (A, B, C, D)

Contract violations (C-29/C-33): labels in YAML template and per-file checklist

Pipeline criterion annotations (C-51): all gate and checklist items carry [C-NN]

---

## V-04 — Combined: COVERAGE-GATE + ORTHOGONALITY COMPLETENESS TABLE

**axis:** lifecycle emphasis + output format (V-01 + V-02 combined)
**hypothesis:** V-01 and V-02 explore independent structural mechanisms at different pipeline
stages. V-01's COVERAGE-GATE operates in Phase 6 (before REGISTRY.md write), asserting gap
coverage as a formally enumerated fact rather than a recalled plan. V-02's ORTHOGONALITY
COMPLETENESS TABLE operates in Phase 5 (after Diagnosis Cards, before the CROSS-CARD
UNIQUENESS SCAN), asserting contrast-axis uniqueness as a cross-role navigable artifact.
Together these two gates close two distinct bypass vectors: coverage-bypass (populating
coverage_gaps from memory) and orthogonality-bypass (writing redundant contrast axes without
cross-role comparison). Expected outcome: 44/44 = 100.00 under v12; potential discovery of
two independent C-53 candidates. Falsifiable: if the evaluator treats COVERAGE-GATE as a
C-22/C-27 paraphrase and ORTHOGONALITY TABLE as a C-35 paraphrase, V-04 scores identically
to R11 V-05 — demonstrating no new distinguishable structural properties.

---

You are running `/org-roles {topic}`.

---

PHASE 0 — FIELD CONTRACT, EXTENSION COMMITMENT, AND PROVENANCE CHAINS

[Identical to V-01 Phase 0 — EXTENSION-COMMITMENT, FIELD-CONTRACT [FC-1] through [FC-12],
PROVENANCE-CHAIN DECLARATION with Chains A/B/C, GATE confirming all eight items including
PROVENANCE-CHAIN DECLARATION with Source/Transit/Destination/Integrity rule per chain [C-52]]

**EXTENSION-COMMITMENT:**
```
EXTENSION-COMMITMENT:
  field_name: inertia_surface
  population_source: Phase 1, INERTIA-SURFACE block, status-quo claim field
  purpose: answers "what is the strongest existing-system argument that makes
    {topic} premature?" for downstream consumers
```

**FIELD CONTRACT:** [FC-1] through [FC-12] as in V-01. [FC-1] includes PROHIBITED NAMES and
POSITIVE SOURCING REQUIRED. [FC-4]/[FC-5] EXACT IDENTIFIER labels. [FC-10] CONTRACT
VIOLATION labels. [FC-11] REQUIRED FORMAT. [FC-12] REQUIRED FORMAT + positional failure.

**PROVENANCE-CHAIN DECLARATION:** Chains A, B, C with Source/Transit/Destination/Integrity
rule per chain (as V-01).

**GATE** — Phase 0 complete when ALL eight gate items confirmed [C-23/C-30/C-26/C-28/C-31/
C-24/C-07/C-29/C-46/C-47/C-52].

---

PHASE 1 — INERTIA SURFACE

[As V-01. Status-quo claim names specific capability; minimum three challenge questions;
no domain expert names. GATE [C-02/C-39 precondition].]

---

PHASE 2 — DOMAIN ANALYSIS

[As V-01. INERTIA-GAP ANALYSIS (minimum three GAP-{slug} entries from Domain vocabulary)
before EXPERT DERIVATION (POSITIVE SOURCING per expert). GATE [C-39/C-44/C-45/C-40/C-28/C-31].]

---

PHASE 3 — STOCK ROLES

[As V-01. STOCK-ROLES: inertia-advocate (ANCHOR-CARD), pm, architect, strategy.
GATE [C-03/C-37/C-46/C-47].]

---

PHASE 4 — OUTPUT AREA

[As V-01. OUTPUT-AREA: `.craft/roles/{area}/` from Phase 2 GAP Domain vocabulary.
GATE [C-04].]

---

PHASE 5 — DIAGNOSIS CARDS, ORTHOGONALITY TABLE, CROSS-CARD SCAN, AND ROLE FILES

**PREPARE:** Confirm Phase 0-4 inputs (ten items) before writing any Diagnosis Card.
[C-07/C-24/C-46/C-47/C-52/C-02/C-39/C-44/C-40/C-45/C-03/C-37/C-04]

**ANCHOR-CARD (write first):**

```
ANCHOR-CARD for inertia-advocate:
  name: {domain-vocabulary slug — [FC-1] confirmed; NOT placeholder}
  [FC-1] name check: domain-specific because [source]; confirmed
  frame: {Phase 1 status-quo claim as epistemic stance — Chain C transit}
  serves: {beneficiary — NOT frame restatement}
  primary_verify_question: {adversarial sufficiency question — Chain B source; scan axis}
  uniqueness argument: confirmed distinct
  anchor status: ANCHOR-CARD
  collaborates_with draft: [{names}]; phantom check: confirmed
```

**SUBSEQUENT DIAGNOSIS CARDS (after ANCHOR-CARD):**

```
DIAGNOSIS-CARD for {role-name}:
  name / [FC-1] check / frame / serves / inertia gap inherited /
  orthogonality to ANCHOR-CARD / primary_verify_question /
  uniqueness argument / collaborates_with draft
  (per R11 V-05 template; Chain A and Chain B transits as applicable)
```

After all Diagnosis Cards, produce **ORTHOGONALITY COMPLETENESS TABLE**:

```
ORTHOGONALITY COMPLETENESS TABLE for /org-roles {topic}:

  ANCHOR primary question: "[anchor's primary_verify_question]"

  Non-anchor roles:
  | Role | Named contrast axis | Distinct from anchor scope | Distinct from prior rows | Status |
  |------|--------------------|-----------------------------|---------------------------|--------|
  | {role-1} | {axis} | YES/NO | N/A (first) | PASS/FLAG |
  | {role-2} | {axis} | YES/NO | YES/NO | PASS/FLAG |
  | ...  |         |        |        | ... |

  ORTHOGONALITY COMPLETENESS GATE:
  - [ ] Every non-anchor role appears
  - [ ] Every axis names the ANCHOR primary question scope explicitly
  - [ ] No two non-anchor roles share the same named contrast axis
  - [ ] All rows PASS
```

Resolve any FLAGs by rewriting the relevant Orthogonality to ANCHOR-CARD field before
running the CROSS-CARD UNIQUENESS SCAN.

After TABLE, run **CROSS-CARD UNIQUENESS SCAN**:

```
Phase 1 — Enumerate All Verify Questions (no checking)
Phase 2 — Anchor-Orthogonality Check (PASS/FLAG per non-anchor)
Phase 3 — Non-Anchor Pairwise Check (PASS/FLAG per pair)
Phase 4 — Revision and Resolution (resolve flags; no YAML until complete)
```

**SCAN ORDERING GATE** — confirm before writing any YAML:
- [ ] ORTHOGONALITY COMPLETENESS TABLE written and all rows PASS before Phase 1 scan began [new]
- [ ] Phase 1 (Enumerate) executed first; no checking occurred in Phase 1 [C-42]
- [ ] Phase 2 (Anchor-Orthogonality) after Phase 1 complete and before Phase 3 began [C-50]
- [ ] Phase 3 (Non-Anchor Pairwise) after Phase 2 complete and before Phase 4 began [C-50]
- [ ] Phase 4 (Revision) last; flags from Phase 2 AND Phase 3 [C-43]
- [ ] No consecutive phases share label; no phase merged [C-48]
- [ ] Canonical sequence: Table → Phase 1 → Phase 2 → Phase 3 → Phase 4 confirmed [C-48]

**WRITE:** One `.md` file per role. Anchor first, then experts, then stock.

[YAML template as V-02 including Chain B destination note for orthogonality.]

Checklist before writing each file [C-51: each item names its governing criterion]:
- [ ] `verify_questions` exact as [FC-4] [C-07/FC-4]
- [ ] `simplify_rules` exact as [FC-5] [C-07/FC-5]
- [ ] `orthogonality` per [FC-11] for non-anchor; absent from ANCHOR-CARD [C-46]
- [ ] `orthogonality` value matches ORTHOGONALITY TABLE contrast axis (verbatim) [C-35/new]
- [ ] `inertia_gap_inherited` per [FC-12] for domain experts [C-47]
- [ ] `anchor: true` in anchor only [C-37]
- [ ] No PHANTOM [C-29/C-33]; no UNIVERSALIST [C-29/C-33]

**GATE** — Phase 5 complete [C-37/C-35/C-41/C-42/C-43/C-48/C-50/C-52/C-51 + TABLE gate].

---

PHASE 6 — REGISTRY SUMMARY

**COVERAGE-GATE** — before writing REGISTRY.md:

```
COVERAGE-GATE for /org-roles {topic}:

  Walk each GAP-{slug} from Phase 2 INERTIA-GAP ANALYSIS:
    GAP-{slug-N}: Expert derived / File written in Phase 5 / Coverage status: COVERED | GAP

  Coverage summary:
    Covered: {count} — {GAP-{slug} list}
    Uncovered: {count} — {GAP-{slug} list or "none"}

  NOTE: `coverage_gaps` in REGISTRY.md comes from Uncovered list above.
  Coverage-bypass failure class: populating coverage_gaps from memory fails.
```

**PREPARE:** Enumerate Phase 5 files → `PHASE5_COUNT`.

**WRITE REGISTRY.md** (as V-01 Phase 6 structure, with `coverage_gaps` from COVERAGE-GATE).

**GATE** — Phase 6 complete [C-04/C-22/C-27/C-10/C-20/C-23/C-15/C-52 + COVERAGE-GATE].

---

**Final checklist — confirm before declaring done:**

Phase output (C-37/C-46) / Scan structure (C-38/C-42/C-43/C-48/C-50) /
Gap artifact (C-39/C-44) / Expert sourcing (C-40/C-45) / Provenance chains (C-52) /
Contract violations (C-29/C-33) / Pipeline criterion annotations (C-51):
[All per R11 V-05 with additions below]

ORTHOGONALITY COMPLETENESS TABLE (new): all non-anchor roles present; all contrast axes
distinct from each other and from anchor; all rows PASS; written before scan

COVERAGE GATE (new): all Phase 2 GAP-{slug} entries enumerated; COVERED/GAP status per
gap; coverage_gaps in REGISTRY.md from enumeration, not memory

---

## V-05 — Combined: All Three Axes + Imperative Step Register

**axis:** lifecycle emphasis + output format + inertia framing + phrasing register
(V-01 + V-02 + V-03 + register change)
**hypothesis:** V-04 carries V-01's COVERAGE-GATE and V-02's ORTHOGONALITY COMPLETENESS
TABLE in the formal Phase register inherited from R11 V-05. V-05 adds V-03's ANCHOR-SOURCING
STATEMENT and switches to the imperative Step register (Steps 1-9) used by R10 V-05 and
R11 V-01-V-04. The formal Phase register (Phase 0-6) scored 100.00 in R11 V-05 with the
PROVENANCE-CHAIN DECLARATION in Phase 0 and per-gate criterion annotations. V-05 R12 tests
whether all three new mechanisms (COVERAGE-GATE, ORTHOGONALITY TABLE, ANCHOR-SOURCING) plus
all inherited mechanisms (C-50, C-51, C-52) survive the register switch to imperative Steps.
Falsifiable: if the imperative register re-introduces regressions in any of C-50/C-51/C-52
(as the formal Phase register's inline GATE structure was the mechanism enabling them), V-05
scores below 100.00 under v12 — demonstrating that the formal Phase register is load-bearing
for the new criteria and cannot be safely replaced by the imperative Step register.

---

You are running `/org-roles {topic}`.

Before doing anything else, commit to three things in writing:

**Commit 1 — Extension field:**
```
EXTENSION-COMMITMENT:
  field_name: inertia_surface
  population_source: Step 2, INERTIA-SURFACE block, status-quo claim field
  purpose: answers "what is the strongest existing-system argument that makes
    {topic} premature?" for downstream consumers
```

**Commit 2 — Field identifiers:**
Write these identifiers verbatim and confirm you will use them exactly:
- `verify_questions` — YAML key for verify list
  (PROHIBITED: verify, questions, checks, verify_list)
- `simplify_rules` — YAML key for simplify list
  (PROHIBITED: simplify, rules, constraints, guidelines)
- `orthogonality` — all non-anchor YAML files; names contrast to ANCHOR-CARD;
  REQUIRED FORMAT: "[Named contrast axis] — this role's lens diverges from the ANCHOR-CARD
  because [specific reason naming the anchor's question and how this role's concern falls
  outside that question's scope]"; copy from Diagnosis Card verbatim
- `inertia_gap_inherited` — domain expert YAML files only;
  REQUIRED FORMAT: "GAP-{slug}: [inertia resistance verbatim]"; positional ("Gap 1:") fails
- `anchor: true` — inertia-advocate YAML file only

**Commit 3 — Provenance chains:**
Write this block verbatim before writing any Diagnosis Card:
```
PROVENANCE-CHAIN DECLARATION for /org-roles {topic}:

  Chain A — Inertia gap provenance:
    Source:      Step 3 INERTIA-GAP ANALYSIS — GAP-{slug}.Inertia resistance
    Transit:     Step 6 Diagnosis Card — Inertia gap inherited
    Destination: Step 8 YAML — inertia_gap_inherited
    Integrity rule: verbatim at each step; GAP-{slug} cited by name; positional breaks A

  Chain B — Orthogonality provenance:
    Source:      Step 7 CROSS-CARD UNIQUENESS SCAN + ANCHOR-CARD primary question
    Transit:     Step 6 Diagnosis Card — Orthogonality to ANCHOR-CARD
    Destination: Step 8 YAML — orthogonality
    Integrity rule: verbatim copy; named contrast axis from ORTHOGONALITY TABLE; traces
      to ANCHOR-CARD primary question; generic assertion breaks B

  Chain C — Inertia surface provenance:
    Source:      Step 2 INERTIA-SURFACE — Status-quo claim
    Transit:     Step 6 ANCHOR-CARD Frame — rephrased as epistemic stance
    Destination: Step 9 REGISTRY.md — inertia_surface
    Integrity rule: exact words at destination; fulfills EXTENSION-COMMITMENT

  Chain D — Anchor name provenance:
    Source:      Step 2 INERTIA-SURFACE — Status-quo claim vocabulary
    Transit:     Step 6 ANCHOR-CARD — ANCHOR-SOURCING statement
    Destination: Step 8 ANCHOR-CARD YAML — name field
    Integrity rule: anchor name contains term traceable to INERTIA-SURFACE vocabulary;
      ANCHOR-SOURCING cites the specific term; generic anchor name breaks D
```

Criterion check (Commit 3): [C-52] PROVENANCE-CHAIN DECLARATION with four chains written
before any Diagnosis Card; each chain names Source/Transit/Destination/Integrity rule

---

**Step 1 — Name constraints (read before writing any names):**

Every expert name must:
1. Come from the vocabulary of a named GAP-{slug} entry you produce in Step 3
2. Include a positive sourcing statement: "this name derives from GAP-{slug}: [term used]"
3. Be specific enough that it could only appear in this domain's registry

The inertia-advocate name must:
1. Come from the vocabulary of the Step 2 INERTIA-SURFACE status-quo claim
2. Include an ANCHOR-SOURCING statement: "this name derives from INERTIA-SURFACE: [term used]"
3. Be specific enough that it could only describe this domain's status-quo position

BANNED names that will fail review: "domain-expert", "expert-1", "generic-expert", "role-1",
"status-quo-reviewer", "inertia-checker"

Criterion check: [C-28] BANNED list named; [C-31] prohibition at Step 1 (location 1 of 3);
[C-40] positive sourcing constraint established before any expert named; [FC-1/new]
ANCHOR-SOURCING requirement established before ANCHOR-CARD name chosen

---

**Step 2 — Inertia surface (read context, no expert naming yet):**

Read `{topic}`. Write:
```
INERTIA-SURFACE for {topic}:
  Status-quo claim: [strongest argument {topic} is unnecessary; name specific capability]
  Challenge questions (minimum three; {topic} vocabulary):
    Q1: What specific failure does the status quo produce that this resolves?
    Q2: [what does existing mechanism already handle?]
    Q3: [minimum status-quo fix, and why insufficient?]
```

Rules: status-quo claim must name a specific capability. Write no expert names here.
The status-quo claim vocabulary is the Chain D source — note one or two specific terms
you will use in the anchor name.

Criterion check: [C-02] status-quo claim present; [C-39 precondition] no expert names;
[C-23] EXTENSION-COMMITMENT written at Commit 1; [C-52/Chain D] vocabulary source identified

---

**Step 3 — Gap analysis with named identifiers (before naming any expert):**

```
INERTIA-GAP ANALYSIS for {topic}:
  GAP-{slug-1}:
    Domain: [named vocabulary domain]
    Failure mode: [what status quo cannot prevent]
    Inertia resistance: [what inertia-advocate overlooks]
  GAP-{slug-2}: ...
  GAP-{slug-3}: ...
```

Rules: assign GAP-{slug} before writing Domain field. Each slug from its Domain vocabulary.
Write no expert names until this block is done.

Criterion check: [C-44] GAP-{slug} identifiers from Domain vocabulary; [C-39] artifact
precedes expert naming; [C-31] prohibition absent here (location 2 is Step 4)

---

**Step 4 — Expert derivation from named gaps:**

```
DOMAIN-ANALYSIS for {topic}:
  - Expert name: [slug from GAP-{slug} vocabulary]
    POSITIVE SOURCING: "this name derives from GAP-{slug}: [term used]"
    Named gap source: GAP-{slug}
    Inertia gap: [GAP-{slug} inertia resistance — verbatim, do not paraphrase]
    Frame: [epistemic viewpoint from GAP-{slug} vocabulary — "sees X through lens of Y"]
    Verify focus: [artifact or behavior checked first]
```

Rules: one expert per gap minimum. No PM, Architect, Strategy, or inertia-advocate here.

Criterion check: [C-45] POSITIVE SOURCING inline per expert; [C-40] names from GAP vocabulary;
[C-28/C-31] BANNED names absent — checkpoint 3 of 3; [C-34] inertia gap per record

---

**Step 5 — Confirm output area:**

```
OUTPUT-AREA: .craft/roles/{area}/
```

Use GAP Domain vocabulary. Not: `default`, `generic`, `roles`.

Criterion check: [C-04] path format correct; area slug from GAP Domain vocabulary

---

**Step 6 — Diagnosis Cards, ANCHOR-CARD first:**

Before writing any YAML file, write one Diagnosis Card per role. Write ANCHOR-CARD FIRST.

**ANCHOR-CARD:**
```
ANCHOR-CARD (inertia-advocate):
  name: [term from Step 2 INERTIA-SURFACE status-quo claim vocabulary; BANNED: placeholders]
  ANCHOR-SOURCING: "this name derives from INERTIA-SURFACE: [specific term from status-quo
    claim vocabulary used in this name]" — Chain D transit
  [FC-1] name check: traces to INERTIA-SURFACE vocabulary; NOT placeholder; confirmed
  Frame: [Step 2 status-quo claim as epistemic stance — Chain C transit]
  Serves: [beneficiary — NOT a restatement of Frame]
  Primary question: [most adversarial "why is status quo sufficient?" — CROSS-CARD UNIQUENESS
    SCAN Phase 2 reference axis; Chain B source for all non-anchor orthogonality fields]
  Uniqueness: confirmed distinct
  anchor: ANCHOR-CARD — primary question is scan reference axis
  Collaborates with: [{names}]; phantom check: confirmed
```

**All other Diagnosis Cards (after ANCHOR-CARD):**
```
DIAGNOSIS-CARD ({role-name}):
  name: [experts: from GAP-{slug} vocabulary with POSITIVE SOURCING; stock: standard]
  [FC-1] name check: [experts: "derives from GAP-{slug}: [term]"; stock: standard]
  Frame: [experts: GAP-{slug} vocabulary; stock: standard lens]
  Serves: [beneficiary — NOT Frame restatement]
  Inertia gap inherited: [experts: "GAP-{slug}: [verbatim]" — Chain A transit; stock: N/A]
  Orthogonality to ANCHOR-CARD: [named contrast axis per REQUIRED FORMAT in Commit 2 —
    Chain B transit; this value copied verbatim to YAML `orthogonality` field]
  Primary question: [most role-specific question for this Frame]
  Uniqueness: confirmed distinct
  Collaborates with: [{names}]; phantom check: confirmed
```

After all Diagnosis Cards, produce **ORTHOGONALITY COMPLETENESS TABLE**:

```
ORTHOGONALITY COMPLETENESS TABLE for /org-roles {topic}:

  ANCHOR primary question: "[anchor's Primary question from Diagnosis Card above]"

  Non-anchor roles:
  | Role | Named contrast axis | Distinct from anchor | Distinct from prior rows | Status |
  |------|---------------------|----------------------|--------------------------|--------|
  | {role-1} | {contrast axis verbatim from card} | YES/NO | N/A (first) | PASS/FLAG |
  | {role-2} | {axis} | YES/NO | YES/NO | PASS/FLAG |
  | ...  |         |        |        | ... |

  ORTHOGONALITY COMPLETENESS GATE:
  - [ ] Every non-anchor role appears in the table [C-35]
  - [ ] Every axis explicitly names the ANCHOR primary question scope [C-35]
  - [ ] No two non-anchor roles share the same named contrast axis [new]
  - [ ] All rows PASS

TABLE complete when GATE confirmed. Resolve any FLAGs before Step 7.
```

---

**Step 7 — Cross-card scan, four phases, before writing any YAML:**

Run after ORTHOGONALITY COMPLETENESS TABLE is complete and all rows PASS.

```
CROSS-CARD UNIQUENESS SCAN (ANCHOR-CARD as reference axis):

  Phase 1 — Enumerate All Verify Questions:
    List every primary question from every Diagnosis Card (ANCHOR-CARD first).
    Format: [role-name]: "[question text]"
    Scope: enumeration only — no checking, no flagging in this phase.
    Complete when every card's primary question appears exactly once.

  Phase 2 — Anchor-Orthogonality Check:
    Using Phase 1 list as reference:
    State ANCHOR-CARD primary question. For each non-anchor: could this role's question
    and the anchor question both be asked by the same role? Mark PASS or FLAG per role.
    Do not start Phase 3 until Phase 2 is complete.

  Phase 3 — Non-Anchor Pairwise Check:
    Using Phase 1 list (non-anchor entries only):
    For each pair: could both questions be asked by the same role type?
    Mark PASS or FLAG per pair. Do not start Phase 4 until Phase 3 complete.

  Phase 4 — Revision and Resolution:
    List all flags from Phase 2 and Phase 3.
    For each flag: rewrite question; record revision and why now distinct.
    Phase 4 complete when all flags resolved. No YAML until Phase 4 complete.
```

**SCAN ORDERING GATE** — confirm before writing any YAML:
- [ ] ORTHOGONALITY COMPLETENESS TABLE complete and all rows PASS before Phase 1 began [new]
- [ ] Phase 1 (Enumerate) executed first; no checking in Phase 1 [C-42]
- [ ] Phase 2 (Anchor-Orthogonality) executed after Phase 1 complete and before Phase 3 began [C-50]
- [ ] Phase 3 (Non-Anchor Pairwise) executed after Phase 2 complete and before Phase 4 began [C-50]
- [ ] Phase 4 (Revision) executed last; collected flags from Phase 2 AND Phase 3 [C-43]
- [ ] No consecutive phases share label; no phase merged with adjacent phase [C-48]
- [ ] Canonical sequence: Table → Phase 1 → Phase 2 → Phase 3 → Phase 4 confirmed [C-48]

SCAN ORDERING GATE complete when all seven items checked. Do not write YAML until GATE passes.

Criterion check: [C-42] Phase 1 enumerate-only; [C-43] Phase 4 named revision; [C-48/C-50]
four phases canonical sequence with per-transition assertions; [C-38] anchor-ortho separate
from pairwise; [C-36] cross-set gate before YAML

---

**Step 8 — Write YAML files (inertia-advocate first):**

Write in order: inertia-advocate (ANCHOR-CARD), then domain experts, then remaining stock.

```yaml
---
name: {from Diagnosis Card — [FC-1] sourcing confirmed; anchor name traces to INERTIA-SURFACE}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

# ANCHOR-CARD only:
anchor: true

# Non-anchor roles only:
orthogonality: "{Chain B destination — verbatim from ORTHOGONALITY TABLE contrast axis;
  per [FC-11] REQUIRED FORMAT; traces to ANCHOR-CARD primary question; not generic}"

# Domain expert roles only:
inertia_gap_inherited: "{Chain A destination — GAP-{slug}: [verbatim]; not positional}"

orientation:
  frame: |
    {Per [FC-2] — epistemic viewpoint, not task list}
  serves: |
    {Per [FC-3] — NOT frame restatement}

lens:
  verify_questions:
    - "{primary question from Diagnosis Card}"
    - "{additional per [FC-4]}"

  simplify_rules:
    - "{Per [FC-5]: 'Skip X unless Y.' — not scope description}"

expertise:
  depth: {per [FC-6]}
  relevance: |
    {Per [FC-7]: domain-specific}

scope:
  primary: |
    {Per [FC-8]: one sentence}
  boundary: |
    {Per [FC-9]: explicit exclusion, one sentence}

collaborates_with:
  - {registry members only; phantom check confirmed}
  # CONTRACT VIOLATION (type 1) — PHANTOM: a name absent from this registry [C-29]
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent [C-29]
```

Checklist before writing each file [C-51: each item names its governing criterion]:
- [ ] `verify_questions` exact as in Commit 2 EXACT IDENTIFIER [C-07/FC-4]
- [ ] `simplify_rules` exact as in Commit 2 EXACT IDENTIFIER [C-07/FC-5]
- [ ] ANCHOR-CARD: `anchor: true`; name traces to INERTIA-SURFACE via ANCHOR-SOURCING [FC-1/new]
- [ ] Non-anchor: `orthogonality` per [FC-11]; verbatim from ORTHOGONALITY TABLE [C-46/new]
- [ ] Domain experts: `inertia_gap_inherited` per [FC-12]; absent from stock/anchor [C-47]
- [ ] No PHANTOM names in `collaborates_with` — CONTRACT VIOLATION (type 1) [C-29/C-33]
- [ ] No UNIVERSALIST in `collaborates_with` — CONTRACT VIOLATION (type 2) [C-29/C-33]

Criterion check: [C-01] schema fields; [C-07] exact identifiers; [C-29/C-33] CONTRACT
VIOLATION framing; [C-46/C-47] field presence/absence; [C-51] criterion annotations on
every checklist item

---

**Step 9 — Write REGISTRY.md:**

**COVERAGE-GATE** — run before writing REGISTRY.md:

```
COVERAGE-GATE for /org-roles {topic}:

  Walk each GAP-{slug} from Step 3 INERTIA-GAP ANALYSIS:

    GAP-{slug-1}:
      Expert derived: {name from Step 4, or "none"}
      Expert file written in Step 8: {filename, or "none written"}
      Coverage status: COVERED | GAP

    GAP-{slug-2}: ...

  Coverage summary:
    Covered gaps: {count} — {list}
    Uncovered gaps: {count} — {list or "none"}

  `coverage_gaps` in REGISTRY.md is populated from "Uncovered gaps" above.
  Coverage-bypass failure class: populating coverage_gaps from memory fails.
```

COVERAGE-GATE complete when all Step 3 gaps enumerated. Do not write REGISTRY.md until done.

Count the files written in Step 8. Record as PHASE5_COUNT from actual enumeration — not
from prior-step plans. Count-bypass failure class applies [C-27/C-32].

Write `.craft/roles/{area}/REGISTRY.md`:

```
---
area: {area}
generated: {date}
---

## Registry Summary

total_roles: {PHASE5_COUNT — from Step 8 enumeration}

stock_roles:
  - inertia-advocate  (ANCHOR-CARD — Step 2 derived; written first; Chain D: name
                       traces to INERTIA-SURFACE vocabulary)
  - pm
  - architect
  - strategy

domain_experts:
  - name: {expert-name}
    gap_source: GAP-{slug}
    inertia_gap: {GAP-{slug} inertia resistance — verbatim}
  (one entry per derived expert)

coverage_gaps: |
  {from COVERAGE-GATE "Uncovered gaps" enumeration — not memory;
   or "none detected" if zero uncovered gaps}

inertia_surface: |
  {Step 2 status-quo claim verbatim — Chain C destination; Chain D vocabulary source;
   fulfills EXTENSION-COMMITMENT}

Generated by: /org-roles {topic} — {date}
```

HEADING STUB RULE: Every field must contain substantive content. A header with no value fails C-10.

Criterion check: [C-10] all five fields substantive; [C-22] total_roles from PHASE5_COUNT;
[C-27] PHASE5_COUNT declared before REGISTRY write; [C-20] inertia_surface present;
[C-15] HEADING STUB RULE read before writing

---

**Final checklist — confirm before declaring done:**

Phase output (C-37/C-46): anchor YAML has `anchor: true`; all non-anchor YAML have
`orthogonality` per [FC-11]; values verbatim from ORTHOGONALITY COMPLETENESS TABLE axes

Scan structure (C-38/C-42/C-43/C-48/C-50): CROSS-CARD UNIQUENESS SCAN four phases;
SCAN ORDERING GATE confirmed (seven items including TABLE gate and per-transition assertions);
canonical sequence Table→Phase 1→2→3→4; no phases merged; Phase 4 before YAML

Orthogonality completeness (new): ORTHOGONALITY TABLE written after all Diagnosis Cards;
every non-anchor present; all contrast axes distinct from each other and anchor; all PASS

Anchor sourcing (new): ANCHOR-CARD carries ANCHOR-SOURCING statement citing INERTIA-SURFACE
vocabulary term; Chain D traces from status-quo claim vocabulary through Diagnosis Card to
anchor YAML name; symmetric with domain expert POSITIVE SOURCING

Coverage gate (new): COVERAGE-GATE enumerated every Step 3 GAP-{slug}; COVERED/GAP per gap;
coverage_gaps from enumeration, not memory

Gap artifact (C-39/C-44): INERTIA-GAP ANALYSIS before expert naming

Expert sourcing (C-40/C-45): POSITIVE SOURCING per expert in derivation record

Provenance chains (C-52): PROVENANCE-CHAIN DECLARATION in Commit 3 with all four chains
(A, B, C, D); Chain A traced per expert to YAML; Chain B traced per non-anchor through
ORTHOGONALITY TABLE to YAML; Chain C traced to REGISTRY.md inertia_surface (verbatim);
Chain D traced from status-quo claim vocabulary to anchor name

Contract violations (C-29/C-33): CONTRACT VIOLATION (type 1) PHANTOM and (type 2)
UNIVERSALIST comments in every YAML file; labels mirrored in template [C-33]; phantom
check per file

Pipeline criterion annotations (C-51): every step-end criterion check and per-file
checklist item carries [C-NN] annotation naming its governing criterion
