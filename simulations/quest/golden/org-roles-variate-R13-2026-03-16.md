---
skill: quest-variate
skill_target: org-roles
date: 2026-03-16
round: R13
rubric_version: v12
status: variate
---

# org-roles Variate — Round 13

**Date:** 2026-03-16
**Skill:** org-roles
**Rubric:** v12 (C-01 through C-52; denominator /44)
**Round:** R13 — single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

**Context:** R12 V-05 closed the v12 frontier at 100.00 (44/44) in the formal Phase
register with all three R12 mechanisms: COVERAGE-GATE (Phase 6), ORTHOGONALITY COMPLETENESS
TABLE (Phase 5), ANCHOR-SOURCING STATEMENT (ANCHOR-CARD template), and 4-chain
PROVENANCE-CHAIN DECLARATION (Phase 0). R13 inherits R12 V-05's full mechanism set as the
base for all five variations and adds three new candidate patterns for v13.

**Post-ceiling framing:** Three candidate strengthening patterns identified from R12 V-05
analysis:

1. **Verify-question-to-gap traceability as Phase 2 gate event** — [FC-1] POSITIVE SOURCING
   traces each domain expert's *name* to GAP-{slug} vocabulary. But expert verify_questions
   may interrogate concerns disconnected from the sourcing gap. A VERIFY-MAP artifact
   produced in Phase 2 (after DOMAIN-ANALYSIS) that explicitly traces each expert's
   intended verify focus to the GAP Failure mode turns verify-question grounding into a
   verifiable pipeline event before Phase 5 begins — parallel to how INERTIA-GAP ANALYSIS
   establishes gap vocabulary before expert naming proceeds.

2. **Simplify-rule domain specificity as per-role pre-YAML gate** — [FC-5] requires
   "opinionated exclusion — NOT a scope description" but no domain-specificity requirement.
   A simplify_rule like "Skip obvious things" passes [FC-5] while carrying zero domain
   content. A SIMPLIFY-DOMAIN CHECK before each role's YAML writing — requiring every
   simplify_rule to contain at least one named domain artifact, mechanism, or vocabulary
   term — creates the same grounding guarantee for simplify_rules that POSITIVE SOURCING
   creates for role names.

3. **Challenge-question coverage as anchor completeness gate** — Phase 3 STOCK-ROLES
   states "verify_questions sourced from Phase 1 challenge questions" but no formal
   enumeration confirms all Phase 1 challenge questions are represented in the anchor's
   verify_questions. A CHALLENGE-COVERAGE MAP produced after ANCHOR-CARD Diagnosis Card
   (before subsequent cards) that walks each Phase 1 challenge question and maps it to an
   anchor verify_question makes challenge coverage a verifiable gate event before the rest
   of Phase 5 proceeds.

---

## Round 13 Variation Map

| V | Axis | Primary new pattern | Hypothesis |
|---|------|---------------------|------------|
| V-01 | lifecycle emphasis | VERIFY-MAP — verify-question-to-gap traceability as Phase 2 artifact after DOMAIN-ANALYSIS | [FC-1] POSITIVE SOURCING traces expert *names* to GAP vocabulary; VERIFY-MAP traces expert *verify_questions* to GAP Failure mode — if these are structurally distinct (name sourcing ≠ question sourcing), potential C-53 |
| V-02 | output format | SIMPLIFY-DOMAIN GATE — named-domain-term requirement per simplify_rule, checked per-role before YAML | [FC-5] "opinionated exclusion" prevents generic scope descriptions; SIMPLIFY-DOMAIN CHECK prevents domain-agnostic exclusion rules — if domain-term requirement is structurally distinct from [FC-5]'s anti-scope-description requirement, potential C-53 |
| V-03 | inertia framing | CHALLENGE-COVERAGE MAP — all Phase 1 challenge questions mapped to anchor verify_questions, written after ANCHOR-CARD Diagnosis Card | Phase 3 implies anchor verify_questions sourced from Phase 1 challenges; CHALLENGE-COVERAGE MAP makes that coverage formally verifiable as a named gate event — if coverage is a structural property distinct from C-01 (minimum two verify_questions) and C-02 (status-quo claim), potential C-53 |
| V-04 | V-01+V-02 combined | VERIFY-MAP + SIMPLIFY-DOMAIN GATE | Both Phase 2 and Phase 5 domain-grounding mechanisms in formal Phase register |
| V-05 | V-01+V-02+V-03 + role sequence | All three + YAML write order: anchor → stock → domain experts | Tests whether C-37 (anchor-first mandate) is sufficient when YAML write order is anchor → stock → experts; all current criteria pass with anchor-first; this order tests whether any criterion implicitly assumes expert-before-stock ordering |

---

## V-01 — Single-Axis: VERIFY-MAP

**axis:** lifecycle emphasis
**hypothesis:** R12 V-05 achieves [FC-1] POSITIVE SOURCING by requiring each domain expert
name to trace to a specific GAP-{slug} and vocabulary term. But the verify_questions in
those same roles carry no parallel traceability requirement — an expert sourced from
GAP-retry-semantics could write a verify_question about logging throughput and pass all
v12 criteria. This variate adds a VERIFY-MAP block to Phase 2 (Step 3 of the analysis
phase), produced immediately after DOMAIN-ANALYSIS, that for each derived expert states the
sourcing GAP-{slug}, the intended verify focus (from the DOMAIN-ANALYSIS Verify focus
field), and a explicit reasoning statement connecting that focus to the GAP Failure mode or
Inertia resistance. VERIFY-MAP is added to the Phase 5 PREPARE list and to the per-file
checklist. A new Chain E in the Phase 0 PROVENANCE-CHAIN DECLARATION traces verify_questions
back to GAP Failure modes through the VERIFY-MAP.
Falsifiable: if the evaluator treats VERIFY-MAP as a paraphrase of POSITIVE SOURCING (the
same gap-traceability mechanism applied to a different field), no new criterion emerges and
V-01 equals R12 V-05 under v12. If verify-question grounding is structurally distinct from
name sourcing — requiring the *interrogation focus* of a question to connect to the gap's
named failure mode rather than merely sharing vocabulary — a new C-53 criterion emerges for
v13.

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
          Inertia-advocate: ANCHOR-SOURCING REQUIRED — "this name derives from
            INERTIA-SURFACE: [term from status-quo claim vocabulary used in name]"
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

  Chain D — Anchor name provenance:
    Source:      Phase 1 INERTIA-SURFACE — Status-quo claim vocabulary
    Transit:     Phase 5 ANCHOR-CARD Diagnosis Card — ANCHOR-SOURCING statement
    Destination: Phase 5 ANCHOR-CARD YAML — field: name
    Integrity rule: anchor name contains term traceable to INERTIA-SURFACE claim
      vocabulary; ANCHOR-SOURCING cites the specific term; generic anchor name breaks D

  Chain E — Verify-question-to-gap traceability (new in V-01):
    Source:      Phase 2 INERTIA-GAP ANALYSIS — field: GAP-{slug}.Failure mode
    Transit:     Phase 2 VERIFY-MAP — field: Interrogates gap because
    Destination: Phase 5 YAML role file — field: lens.verify_questions[0]
    Integrity rule: primary verify_question interrogates the sourcing gap's Failure
      mode; verify focus disconnected from GAP Failure mode breaks Chain E;
      verify focus referencing only GAP vocabulary without interrogating the failure
      mode is insufficient and breaks Chain E
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT written with all three elements; `field_name` = `inertia_surface`;
   purpose references Phase 0 diagnostic question [C-23/C-30]
2. FIELD-CONTRACT written with all twelve items [FC-1] through [FC-12] [C-26]
3. [FC-1] contains PROHIBITED NAMES clause, POSITIVE SOURCING REQUIRED clause, and
   ANCHOR-SOURCING REQUIRED clause [C-28/C-31]
4. [FC-4] and [FC-5] display exact identifier strings `verify_questions` and `simplify_rules`
   under EXACT IDENTIFIER labels [C-24/C-07]
5. [FC-10] carries CONTRACT VIOLATION (type 1) and (type 2) labels [C-29]
6. [FC-11] written with REQUIRED and REQUIRED FORMAT; states YAML persistence [C-46]
7. [FC-12] written with REQUIRED and REQUIRED FORMAT citing GAP-{slug}; states YAML
   persistence and that positional-only reference fails [C-47]
8. PROVENANCE-CHAIN DECLARATION written with all five chains (A through E); each chain
   names Source, Transit, Destination, and Integrity rule [C-52]

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
Note one or two specific vocabulary terms from the status-quo claim for anchor name use
(Chain D source).

**GATE** — Phase 1 complete when ALL of the following are TRUE:
1. INERTIA-SURFACE block written with status-quo claim naming a specific capability [C-02]
2. At least three challenge questions using `{topic}` vocabulary
3. No domain expert names appear [C-39 precondition]

---

PHASE 2 — DOMAIN ANALYSIS (gap-first, with verify-question traceability)

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

**Step 3 — VERIFY-MAP (verify-question-to-gap traceability):**
After DOMAIN-ANALYSIS, write a VERIFY-MAP tracing each expert's intended verify focus
to the Failure mode of its sourcing GAP-{slug}. Produce this artifact before Phase 3.

```
VERIFY-MAP for /org-roles {topic}:

  For each domain expert from DOMAIN-ANALYSIS:

    Expert: {expert-name}
      Source gap: GAP-{slug}
      Verify focus (from DOMAIN-ANALYSIS): [text from Verify focus field]
      Interrogates gap because: [explicit connection between the verify focus and
        GAP-{slug} Failure mode — name the failure mode; state why the verify focus
        surfaces or prevents that failure]
      Chain E status: PASS | FLAG
        (FLAG: verify focus does not interrogate GAP-{slug} Failure mode;
         PASS: verify focus interrogates GAP-{slug} Failure mode by name)
```

Resolve all FLAGs before proceeding to Phase 3. A flagged verify focus must be
rewritten in the DOMAIN-ANALYSIS record and in this VERIFY-MAP with the revised
focus and the reason it now interrogates the GAP Failure mode.
VERIFY-MAP is the Chain E transit artifact — produced in Phase 2, consumed in Phase 5.

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. INERTIA-GAP ANALYSIS written before DOMAIN-ANALYSIS; at least three named gaps in
   GAP-{slug} format, each with Domain, Failure mode, Inertia resistance [C-39/C-44]
2. GAP-{slug} identifiers derive from their respective Domain vocabularies [C-44]
3. Each derived expert lists all five attributes including POSITIVE SOURCING statement [C-45]
4. POSITIVE SOURCING statement cites specific GAP-{slug} and domain vocabulary term [C-45/C-40]
5. No placeholder names per [FC-1]; no stock role names [C-28/C-31] — checkpoint 2 of 3
6. VERIFY-MAP written for all domain experts; all entries have Chain E status PASS;
   all FLAGs resolved before this GATE confirmed [new]

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
OUTPUT-AREA: .roles/{area}/
```

Area slug uses GAP-{slug} Domain vocabulary from Phase 2. NOT: `default`, `generic`, `roles`.

**GATE** — Phase 4 complete when ALL of the following are TRUE:
1. OUTPUT-AREA written with area slug from Phase 2 GAP Domain vocabulary [C-04]
2. Path format is exactly `.roles/{area}/`

---

PHASE 5 — DIAGNOSIS CARDS AND ROLE FILE WRITING

**PREPARE:** Confirm inputs before writing any Diagnosis Card:
- Phase 0 [FC-4] exact identifier: `verify_questions` (retrieve verbatim) [C-07/C-24]
- Phase 0 [FC-5] exact identifier: `simplify_rules` (retrieve verbatim) [C-07/C-24]
- Phase 0 [FC-11] REQUIRED FORMAT for `orthogonality` YAML field (retrieve verbatim) [C-46]
- Phase 0 [FC-12] REQUIRED FORMAT for `inertia_gap_inherited` YAML field (retrieve verbatim) [C-47]
- Phase 0 PROVENANCE-CHAIN DECLARATION: all five chains (A-E) confirmed [C-41/C-46/C-47/C-52]
- Phase 1 INERTIA-SURFACE: status-quo claim and challenge questions confirmed [C-02]
- Phase 2 INERTIA-GAP ANALYSIS: all GAP-{slug} entries confirmed [C-39/C-44]
- Phase 2 DOMAIN-ANALYSIS: expert names with POSITIVE SOURCING confirmed [C-40/C-45]
- Phase 2 VERIFY-MAP: all experts PASS Chain E status confirmed [new]
- Phase 3 STOCK-ROLES: four names; inertia-advocate ANCHOR-CARD confirmed [C-03/C-37]
- Phase 4 OUTPUT-AREA path confirmed [C-04]

PREPARE complete when all eleven inputs confirmed. Do not begin Diagnosis Cards until confirmed.

**ANCHOR-CARD (write first):**

```
ANCHOR-CARD for inertia-advocate:

  name: {term from Phase 1 INERTIA-SURFACE status-quo claim vocabulary — confirmed
         against [FC-1]; NOT placeholder}
  ANCHOR-SOURCING: "this name derives from INERTIA-SURFACE: [specific term from
    status-quo claim vocabulary used in this name]" — Chain D transit
  [FC-1] name check: traces to INERTIA-SURFACE vocabulary via ANCHOR-SOURCING;
    NOT placeholder; confirmed

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
  VERIFY-MAP check (experts only): confirm primary_verify_question interrogates
    GAP-{slug} Failure mode per VERIFY-MAP — Chain E consumed here [new]
  uniqueness argument: [reason]; confirmed distinct

  collaborates_with draft: [{name-1}, {name-2}]; phantom check: confirmed
```

After all Diagnosis Cards, produce an **ORTHOGONALITY COMPLETENESS TABLE**:

```
ORTHOGONALITY COMPLETENESS TABLE for /org-roles {topic}:

  ANCHOR primary question: "[anchor's primary_verify_question from Diagnosis Card]"

  Non-anchor roles:
  | Role | Named contrast axis (from Orthogonality to ANCHOR-CARD) | Axis distinct from anchor | Axis distinct from all prior rows | Status |
  |------|----------------------------------------------------------|---------------------------|-----------------------------------|--------|
  | {role-1} | {contrast axis text} | YES/NO | YES/NO (first row: N/A) | PASS/FLAG |
  | {role-2} | {contrast axis text} | YES/NO | YES/NO                  | PASS/FLAG |
  | ...  | ...                                                      | ...       | ...                               | ...    |

  ORTHOGONALITY COMPLETENESS GATE:
  - [ ] Every non-anchor role appears in the table [C-35]
  - [ ] Every contrast axis explicitly names the ANCHOR primary question scope [C-35]
  - [ ] No two non-anchor roles share the same named contrast axis [new]
  - [ ] All rows PASS

TABLE complete when all rows filled and GATE confirmed. Resolve all FLAGs before scan.
Do not run the CROSS-CARD UNIQUENESS SCAN until TABLE is complete.
```

After ORTHOGONALITY COMPLETENESS TABLE, run **CROSS-CARD UNIQUENESS SCAN**:

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
- [ ] ORTHOGONALITY COMPLETENESS TABLE complete; all rows PASS; before scan began [C-35/new]
- [ ] Phase 1 (Enumerate) executed first; no checking occurred in Phase 1 [C-42]
- [ ] Phase 2 (Anchor-Orthogonality) executed after Phase 1 was complete and before Phase 3 began [C-50]
- [ ] Phase 3 (Non-Anchor Pairwise) executed after Phase 2 was complete and before Phase 4 began [C-50]
- [ ] Phase 4 (Revision and Resolution) executed last; collected flags from Phase 2 AND Phase 3 [C-43]
- [ ] No two consecutive phases share a label; no phase merged with an adjacent phase [C-48]
- [ ] Canonical sequence confirmed: Table → Phase 1 → Phase 2 → Phase 3 → Phase 4 [C-48]

**WRITE:** One `.md` file per role. Order: inertia-advocate (ANCHOR-CARD) first, then
domain experts, then remaining stock roles.

```yaml
---
name: {per Diagnosis Card — [FC-1] positive/anchor sourcing confirmed}
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
    - "{Primary verify question — uniqueness confirmed in scan; Chain E destination
       for domain experts: interrogates GAP Failure mode per VERIFY-MAP}"
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
- [ ] `orthogonality` value matches ORTHOGONALITY COMPLETENESS TABLE contrast axis [C-35]
- [ ] `inertia_gap_inherited` present per [FC-12] for domain experts; absent from stock/anchor [C-47]
- [ ] `anchor: true` in inertia-advocate file only [C-37]
- [ ] No PHANTOM names in `collaborates_with` — CONTRACT VIOLATION (type 1) [C-29/C-33]
- [ ] No UNIVERSALIST listing in `collaborates_with` — CONTRACT VIOLATION (type 2) [C-29/C-33]
- [ ] Domain expert verify_questions[0] interrogates sourcing GAP Failure mode per VERIFY-MAP [new/Chain E]

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. ANCHOR-CARD Diagnosis Card written first; all subsequent cards written after [C-37]
2. All non-anchor Diagnosis Cards include `orthogonality to ANCHOR-CARD` per [FC-11] [C-35]
3. All domain expert Diagnosis Cards include `inertia gap inherited` citing GAP-{slug} [C-41]
4. VERIFY-MAP consulted per expert Diagnosis Card; Chain E status confirmed [new]
5. ORTHOGONALITY COMPLETENESS TABLE complete; all rows PASS before scan began [C-35/new]
6. CROSS-CARD UNIQUENESS SCAN: all four phases run; SCAN ORDERING GATE confirmed (seven items
   checked) [C-42/C-43/C-48/C-50]
7. One `.md` file per role; inertia-advocate (ANCHOR-CARD) written first [C-37]
8. ANCHOR-CARD YAML: `anchor: true`; NO `orthogonality`; NO `inertia_gap_inherited` [C-37]
9. Non-anchor YAML: `orthogonality` field per [FC-11] REQUIRED FORMAT — not generic [C-46]
10. Domain expert YAML: `inertia_gap_inherited` per [FC-12] citing GAP-{slug} — not positional [C-47]
11. All YAML files use exact identifiers `verify_questions` and `simplify_rules` verbatim [C-07]
12. No prohibited names per [FC-1]; no collaborates_with CONTRACT VIOLATION; labels mirrored [C-28/C-29/C-33]
13. PROVENANCE-CHAIN DECLARATION Chains A-E each traceable through Diagnosis Cards to YAML [C-52]
14. Per-file checklist items carry criterion-ID annotations [C-51]

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
  than from this enumeration fails [C-22 parallel].
```

COVERAGE-GATE complete when all Phase 2 gaps enumerated and coverage status recorded.
Do not write REGISTRY.md until COVERAGE-GATE is complete.

**PREPARE:** Enumerate `.md` files written in Phase 5. Record as `PHASE5_COUNT`.
This count must come from Phase 5 enumeration only — not from prior-phase planned counts.
Count-bypass failure class applies: deriving the count from plans fails [C-27/C-32].

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
  {from COVERAGE-GATE "Uncovered gaps" enumeration — not from memory;
   or "none detected" if COVERAGE-GATE confirmed zero uncovered gaps}

inertia_surface: |
  {Phase 1 status-quo claim verbatim — Chain C destination; fulfills EXTENSION-COMMITMENT}

Generated by: /org-roles {topic} — {date}
```

HEADING STUB FAIL CONDITION: Section headers with empty or omitted values beneath them
fail C-10. Every field must contain substantive content.

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. COVERAGE-GATE written and complete; every Phase 2 GAP-{slug} enumerated [C-10/C-22 parallel]
2. `coverage_gaps` populated from COVERAGE-GATE "Uncovered gaps" — not memory
3. `REGISTRY.md` exists at `.roles/{area}/REGISTRY.md` [C-04]
4. `total_roles` equals `PHASE5_COUNT` from Phase 5 enumeration [C-22/C-27]
5. `domain_experts` lists each expert with `name`, `gap_source`, `inertia_gap` verbatim [C-10]
6. `inertia_surface` contains Phase 1 status-quo claim verbatim [C-20/C-23] — Chain C verified
7. No heading stubs [C-15]
8. PROVENANCE-CHAIN DECLARATION Chain C integrity confirmed [C-52]

---

**Final checklist — confirm before declaring done:**

Phase output (C-37/C-46): inertia-advocate YAML has `anchor: true`; all non-anchor YAML have
`orthogonality` with named contrast axis matching ORTHOGONALITY TABLE; domain expert YAML
have `inertia_gap_inherited` citing GAP-{slug} verbatim

Scan structure (C-38/C-42/C-43/C-48/C-50): CROSS-CARD UNIQUENESS SCAN ran four named phases
in canonical sequence; SCAN ORDERING GATE confirmed (seven items including TABLE gate);
Phase 4 complete before any YAML written

Orthogonality completeness: ORTHOGONALITY COMPLETENESS TABLE written after all Diagnosis
Cards and before scan; every non-anchor role appears; all contrast axes pairwise distinct;
all rows PASS

Verify-question traceability (new): VERIFY-MAP written in Phase 2 after DOMAIN-ANALYSIS;
all domain expert primary verify_questions interrogate sourcing GAP Failure mode per
VERIFY-MAP; Chain E confirmed; VERIFY-MAP check notation present in each expert Diagnosis
Card; YAML verify_questions[0] annotation references Chain E and VERIFY-MAP

Gap/sourcing (C-39/C-44/C-40/C-45): INERTIA-GAP ANALYSIS before expert naming; POSITIVE
SOURCING per expert; ANCHOR-SOURCING per ANCHOR-CARD (Chain D transit)

Provenance chains (C-52): PROVENANCE-CHAIN DECLARATION in Phase 0 with five chains (A-E);
Chain A/B/C/D/E each traceable through transit artifacts to destinations

Contract violations (C-29/C-33): labels in YAML template and per-file checklist

Pipeline criterion annotations (C-51): all gate items and checklist items carry [C-NN]

Coverage gate: COVERAGE-GATE enumerated every Phase 2 GAP-{slug}; coverage_gaps in
REGISTRY.md populated from enumeration, not memory

---

## V-02 — Single-Axis: SIMPLIFY-DOMAIN GATE

**axis:** output format
**hypothesis:** R12 V-05 requires [FC-5] "opinionated exclusion — NOT a scope description"
for every simplify_rule. This prevents rules like "Covers all scope concerns" (a scope
description) but does not prevent domain-agnostic exclusion rules like "Skip obvious things"
or "Defer non-critical items" — which pass [FC-5] while carrying zero domain content. This
variate adds a SIMPLIFY-DOMAIN CHECK before each role's YAML is written in Phase 5. The
check requires every simplify_rule to contain at least one named domain artifact, mechanism,
field name, or vocabulary term specific to this domain — the same grounding guarantee that
POSITIVE SOURCING creates for role names. The check is added to the per-file checklist
as a new criterion-annotated item. All other elements identical to R12 V-05.
Falsifiable: if the evaluator treats SIMPLIFY-DOMAIN CHECK as a subset of [FC-5]'s
anti-scope requirement (the same "be specific" obligation in different words), no new
criterion emerges and V-02 equals R12 V-05 under v12. If naming a domain term creates a
structural property distinct from excluding generic scope descriptions — specifically, that
simplify_rules are traceable to the domain's vocabulary just as names are — a new C-53
criterion emerges for v13.

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
          Inertia-advocate: ANCHOR-SOURCING REQUIRED — "this name derives from
            INERTIA-SURFACE: [term from status-quo claim vocabulary used in name]"
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
          SIMPLIFY-DOMAIN REQUIREMENT (new): each simplify_rule must contain at least one
            named domain artifact, mechanism, field name, or vocabulary term specific to
            this domain — generic exclusion terms ("obvious things", "non-critical items",
            "implementation details") without a named domain term fail this requirement
          BAD: "Skip obvious things unless performance matters"
          GOOD: "Skip {domain-artifact} validation unless {domain-condition} applies"

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

  Chain D — Anchor name provenance:
    Source:      Phase 1 INERTIA-SURFACE — Status-quo claim vocabulary
    Transit:     Phase 5 ANCHOR-CARD Diagnosis Card — ANCHOR-SOURCING statement
    Destination: Phase 5 ANCHOR-CARD YAML — field: name
    Integrity rule: anchor name contains term traceable to INERTIA-SURFACE claim
      vocabulary; ANCHOR-SOURCING cites the specific term; generic anchor name breaks D
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT written with all three elements [C-23/C-30]
2. FIELD-CONTRACT written with all twelve items [FC-1] through [FC-12] [C-26]
3. [FC-1] contains PROHIBITED NAMES clause, POSITIVE SOURCING REQUIRED clause, and
   ANCHOR-SOURCING REQUIRED clause [C-28/C-31]
4. [FC-4] and [FC-5] display exact identifier strings under EXACT IDENTIFIER labels [C-24/C-07]
5. [FC-5] contains SIMPLIFY-DOMAIN REQUIREMENT with BAD/GOOD examples [new]
6. [FC-10] carries CONTRACT VIOLATION (type 1) and (type 2) labels [C-29]
7. [FC-11] written with REQUIRED and REQUIRED FORMAT [C-46]
8. [FC-12] written with REQUIRED and REQUIRED FORMAT; positional-reference failure noted [C-47]
9. PROVENANCE-CHAIN DECLARATION written with all four chains; each chain names Source,
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
Note one or two specific vocabulary terms from the status-quo claim for anchor name use.

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
  (minimum three; GAP-{slug} from Domain vocabulary)
```

**Step 2 — EXPERT DERIVATION:**

```
DOMAIN-ANALYSIS for {topic}:

  Domain experts derived from INERTIA-GAP ANALYSIS:
    - Expert name: [slug from GAP-{slug} Domain vocabulary]
      POSITIVE SOURCING: "this name derives from GAP-{slug}: [term used]"
      Named gap source: GAP-{slug}
      Inertia gap: [GAP-{slug} inertia resistance — copied verbatim]
      Domain-vocabulary frame: [per [FC-2]]
      Verify focus: [artifact or behavior checked first]
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 2.

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. INERTIA-GAP ANALYSIS before DOMAIN-ANALYSIS; minimum three gaps; all fields present [C-39/C-44]
2. GAP-{slug} identifiers from Domain vocabularies [C-44]
3. Each expert: POSITIVE SOURCING citing GAP-{slug} and vocabulary term [C-45/C-40]
4. No placeholder or stock names [C-28/C-31] — checkpoint 2 of 3

---

PHASE 3 — STOCK ROLES

```
STOCK-ROLES:
  - inertia-advocate  (ANCHOR-CARD; frame from Phase 1; written first; anchor: true)
  - pm                (product value and user outcome lens)
  - architect         (technical structure and system boundary lens)
  - strategy          (business model and competitive position lens)
```

All non-anchor roles carry `orthogonality` per [FC-11]. Domain experts carry
`inertia_gap_inherited` per [FC-12].

**GATE** — Phase 3 complete when [C-03/C-37/C-46/C-47] confirmed.

---

PHASE 4 — OUTPUT AREA

```
OUTPUT-AREA: .roles/{area}/
```

Area slug from Phase 2 GAP Domain vocabulary. NOT: `default`, `generic`, `roles`.

**GATE** — Phase 4 complete when [C-04] confirmed.

---

PHASE 5 — DIAGNOSIS CARDS AND ROLE FILE WRITING

**PREPARE:** Confirm Phase 0-4 inputs before writing any Diagnosis Card:
Phase 0 [FC-4]/[FC-5] exact identifiers; [FC-11]/[FC-12] REQUIRED FORMATs; PROVENANCE-CHAIN
DECLARATION four chains; Phase 1 INERTIA-SURFACE; Phase 2 INERTIA-GAP ANALYSIS + DOMAIN-ANALYSIS;
Phase 3 STOCK-ROLES; Phase 4 OUTPUT-AREA.
[C-07/C-24/C-46/C-47/C-52/C-02/C-39/C-44/C-40/C-45/C-03/C-37/C-04]

PREPARE complete when all ten inputs confirmed.

**ANCHOR-CARD (write first):**

```
ANCHOR-CARD for inertia-advocate:
  name: {INERTIA-SURFACE vocabulary slug; ANCHOR-SOURCING: "this name derives from
    INERTIA-SURFACE: [term]" — Chain D transit; [FC-1] confirmed; NOT placeholder}
  frame: {Phase 1 status-quo claim as epistemic stance — Chain C transit}
  serves: {beneficiary — NOT frame restatement}
  primary_verify_question: {adversarial sufficiency question — Chain B source; scan
    reference axis}
  uniqueness argument: [reason]; confirmed distinct
  anchor status: ANCHOR-CARD
  collaborates_with draft: [{names}]; phantom check: confirmed
```

**SUBSEQUENT DIAGNOSIS CARDS (after ANCHOR-CARD):**

```
DIAGNOSIS-CARD for {role-name}:
  name: {experts: GAP-{slug} vocabulary with POSITIVE SOURCING; stock: standard; confirmed}
  [FC-1] name check: [experts: GAP-{slug} trace; stock: standard]
  frame: {GAP-{slug} vocabulary (experts) / standard lens (stock)}
  serves: {beneficiary — NOT restatement}
  inertia gap inherited: {"GAP-{slug}: [verbatim]" (experts) / N/A (stock) — Chain A transit}
  orthogonality to ANCHOR-CARD: {per [FC-11] — Chain B transit; verbatim to YAML}
  primary_verify_question: {role-specific}
  uniqueness argument: [reason]; confirmed distinct
  collaborates_with draft: [{names}]; phantom check: confirmed

  SIMPLIFY-DOMAIN PLAN (new): before writing YAML, list planned simplify_rules and
    confirm each contains at least one named domain term:
    Rule 1: [planned text] — domain term: [{term}] — PASS/FLAG
    Rule 2: [planned text] — domain term: [{term}] — PASS/FLAG
    Resolve all FLAGs before writing YAML for this role.
```

After all Diagnosis Cards, produce **ORTHOGONALITY COMPLETENESS TABLE**:

```
ORTHOGONALITY COMPLETENESS TABLE for /org-roles {topic}:

  ANCHOR primary question: "[anchor primary_verify_question]"

  | Role | Named contrast axis | Axis distinct from anchor | Axis distinct from prior rows | Status |
  |------|---------------------|---------------------------|-------------------------------|--------|
  | {role-1} | {axis} | YES/NO | N/A (first) | PASS/FLAG |
  | {role-2} | {axis} | YES/NO | YES/NO      | PASS/FLAG |

  ORTHOGONALITY COMPLETENESS GATE:
  - [ ] Every non-anchor role in table [C-35]
  - [ ] Every axis names ANCHOR question scope [C-35]
  - [ ] No two rows share same named axis [new]
  - [ ] All rows PASS

Do not run CROSS-CARD UNIQUENESS SCAN until TABLE complete.
```

After TABLE, run **CROSS-CARD UNIQUENESS SCAN** (same four-phase structure as all R12/R13
variations: Phase 1 Enumerate → Phase 2 Anchor-Orthogonality → Phase 3 Non-Anchor Pairwise
→ Phase 4 Revision-Resolution; each phase in canonical sequence; no phase merged).

**SCAN ORDERING GATE** — confirm before writing any YAML:
- [ ] ORTHOGONALITY COMPLETENESS TABLE complete; all rows PASS [new]
- [ ] Phase 1 executed first; no checking in Phase 1 [C-42]
- [ ] Phase 2 after Phase 1 complete and before Phase 3 [C-50]
- [ ] Phase 3 after Phase 2 complete and before Phase 4 [C-50]
- [ ] Phase 4 executed last; flags from Phase 2 AND Phase 3 collected [C-43]
- [ ] No phases merged; no consecutive phases share label [C-48]
- [ ] Canonical sequence: Table → Phase 1 → Phase 2 → Phase 3 → Phase 4 [C-48]

**WRITE:** One `.md` per role; anchor first, then experts, then stock.

**SIMPLIFY-DOMAIN CHECK** — before writing each role's YAML file:

```
SIMPLIFY-DOMAIN CHECK for {role-name}:

  Planned simplify_rules (from Diagnosis Card SIMPLIFY-DOMAIN PLAN):
    Rule 1: "{rule text}"
      Named domain term: [{term} — must be an artifact, mechanism, field, or vocab term
        specific to this domain; generic terms: "obvious", "non-critical", "details" alone
        are insufficient]
      Status: PASS | FLAG
    Rule 2: "{rule text}" (if present)
      Named domain term: [{term}]
      Status: PASS | FLAG

  SIMPLIFY-DOMAIN GATE:
    - [ ] All rules PASS — each contains a named domain term [new/FC-5 SIMPLIFY-DOMAIN REQUIREMENT]
    - [ ] No rule relies solely on generic exclusion language [FC-5]

Resolve all FLAGs before writing YAML. Do not proceed to YAML until gate confirmed.
```

```yaml
---
name: {[FC-1] confirmed}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}
anchor: true   # ANCHOR-CARD only
orthogonality: "{Chain B — per [FC-11]; verbatim from TABLE; not generic}"   # non-anchor
inertia_gap_inherited: "{Chain A — GAP-{slug}: [verbatim]; not positional}"   # experts
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
    - "{Per [FC-5] + SIMPLIFY-DOMAIN REQUIREMENT: contains named domain term}"
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
- [ ] `verify_questions` exact as [FC-4] EXACT IDENTIFIER [C-07/FC-4]
- [ ] `simplify_rules` exact as [FC-5] EXACT IDENTIFIER [C-07/FC-5]
- [ ] `orthogonality` per [FC-11] for non-anchor; absent from ANCHOR-CARD [C-46]
- [ ] `orthogonality` matches TABLE contrast axis [C-35]
- [ ] `inertia_gap_inherited` per [FC-12] for experts; absent from stock/anchor [C-47]
- [ ] `anchor: true` in inertia-advocate only [C-37]
- [ ] No PHANTOM — CONTRACT VIOLATION (type 1) [C-29/C-33]
- [ ] No UNIVERSALIST — CONTRACT VIOLATION (type 2) [C-29/C-33]
- [ ] SIMPLIFY-DOMAIN CHECK run; all simplify_rules contain named domain terms [new/FC-5]

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. ANCHOR-CARD first [C-37]
2. All non-anchor cards: `orthogonality to ANCHOR-CARD` [C-35]
3. All expert cards: `inertia gap inherited` citing GAP-{slug} [C-41]
4. SIMPLIFY-DOMAIN CHECK run per role; all gates confirmed; all FLAGs resolved [new]
5. ORTHOGONALITY COMPLETENESS TABLE complete; all rows PASS [new]
6. CROSS-CARD UNIQUENESS SCAN: four phases; SCAN ORDERING GATE confirmed (seven items) [C-42/C-43/C-48/C-50]
7. YAML written; anchor first; correct per-role field presence [C-37/C-46/C-47]
8. Criterion annotations on checklist items [C-51]
9. Provenance chains A-D traceable to YAML [C-52]

---

PHASE 6 — REGISTRY SUMMARY

(Identical to V-01 Phase 6: COVERAGE-GATE before REGISTRY.md; PHASE5_COUNT from enumeration;
REGISTRY.md fields as specified; GATE items as specified.)

**COVERAGE-GATE** — walk each Phase 2 GAP-{slug}; record COVERED/GAP; populate
`coverage_gaps` from enumeration not memory. GATE: complete before REGISTRY.md written.

**PREPARE:** Enumerate Phase 5 `.md` files; record `PHASE5_COUNT` from Phase 5 only.

**WRITE:** `.roles/{area}/REGISTRY.md` with `total_roles`, `stock_roles`,
`domain_experts` (name/gap_source/inertia_gap verbatim), `coverage_gaps` from COVERAGE-GATE,
`inertia_surface` verbatim from Phase 1.

**GATE** — [C-04/C-22/C-27/C-10/C-20/C-23/C-15/C-52] all confirmed.

---

**Final checklist — confirm before declaring done:**

Phase output (C-37/C-46): anchor YAML has `anchor: true`; non-anchor YAML have
`orthogonality` matching TABLE; expert YAML have `inertia_gap_inherited` verbatim

Scan structure (C-38/C-42/C-43/C-48/C-50): four-phase scan; SCAN ORDERING GATE confirmed
(seven items); Phase 4 before any YAML

Orthogonality completeness: TABLE after all Diagnosis Cards; all axes distinct; all PASS

Simplify-rule domain specificity (new): SIMPLIFY-DOMAIN CHECK run per role in Diagnosis
Card planning and pre-YAML gate; all simplify_rules contain named domain terms;
SIMPLIFY-DOMAIN REQUIREMENT in [FC-5] established in Phase 0

Gap/sourcing (C-39/C-44/C-40/C-45): INERTIA-GAP ANALYSIS before naming; POSITIVE SOURCING
per expert; ANCHOR-SOURCING per anchor

Provenance chains (C-52): four chains declared; A/B/C/D traceable

Contract violations (C-29/C-33): labels in template and checklist

Pipeline annotations (C-51): all gate and checklist items carry [C-NN]

Coverage gate: COVERAGE-GATE enumerated all gaps; coverage_gaps from enumeration

---

## V-03 — Single-Axis: CHALLENGE-COVERAGE MAP

**axis:** inertia framing
**hypothesis:** R12 V-05 Phase 3 STOCK-ROLES states that the inertia-advocate's
`verify_questions` are "sourced from Phase 1 challenge questions." But no formal
enumeration confirms that all Phase 1 challenge questions are represented in the anchor's
verify_questions. The anchor must have minimum two verify_questions (C-01); Phase 1 must
have minimum three challenge questions (Phase 1 GATE). These two requirements together do
not guarantee coverage — the anchor could carry two verify_questions that cover only one
of the three Phase 1 challenge questions and pass all v12 criteria. This variate adds a
CHALLENGE-COVERAGE MAP immediately after the ANCHOR-CARD Diagnosis Card (before any
subsequent Diagnosis Card). The MAP walks every Phase 1 challenge question and maps it to
the anchor's planned verify_questions, producing a coverage assessment. Any Phase 1
challenge question not represented must be added to the anchor's verify_questions before
the MAP is closed. All other elements identical to R12 V-05.
Falsifiable: if the evaluator treats CHALLENGE-COVERAGE MAP as a restatement of the
existing coverage already implied by Phase 3's "sourced from Phase 1" annotation, no new
criterion emerges. If the MAP establishes a structural property distinct from C-01/C-02 —
that all Phase 1 challenge questions are explicitly verified as represented in anchor
verify_questions before Phase 5 proceeds — a new C-53 criterion emerges for v13.

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
          GOOD (anchor): "integration-sufficiency-advocate" — INERTIA-SURFACE, term
                "integration sufficiency"

  [FC-2]  orientation.frame
          type: string — epistemic viewpoint; FAILURE MODE: task list

  [FC-3]  orientation.serves
          type: string — beneficiary; NOT a frame restatement

  [FC-4]  lens.verify_questions
          EXACT IDENTIFIER: verify_questions
          PROHIBITED IDENTIFIERS: verify | questions | checks | verify_list
          type: list; minimum two items; uniqueness argument required before writing

  [FC-5]  lens.simplify_rules
          EXACT IDENTIFIER: simplify_rules
          PROHIBITED IDENTIFIERS: simplify | rules | constraints | guidelines
          type: list; minimum one item; opinionated exclusion — NOT a scope description

  [FC-6]  expertise.depth   — enum: expert | practitioner | senior | principal

  [FC-7]  expertise.relevance — domain-specific justification

  [FC-8]  scope.primary     — main concern; one sentence

  [FC-9]  scope.boundary    — explicit exclusion; one sentence

  [FC-10] collaborates_with
          type: list — registry members only
          CONTRACT VIOLATION (type 1) — PHANTOM: absent from registry
          CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent

  [FC-11] orthogonality
          Applies to: all non-anchor YAML files
          REQUIRED FORMAT: "[Named contrast axis] — this role's lens diverges from the
            ANCHOR-CARD because [specific reason]"
          FAILURE MODE: generic assertion not tracing to anchor question

  [FC-12] inertia_gap_inherited
          Applies to: domain expert YAML files only
          REQUIRED FORMAT: "GAP-{slug}: [inertia resistance copied verbatim]"
          FAILURE MODE: positional reference ("Gap 1:") fails [FC-12]
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
    Source:      Phase 5 SCAN + ANCHOR-CARD primary question
    Transit:     Phase 5 Diagnosis Card — Orthogonality to ANCHOR-CARD
    Destination: Phase 5 YAML — orthogonality [FC-11]
    Integrity rule: verbatim copy; named contrast axis; generic assertion breaks B

  Chain C — Inertia surface provenance:
    Source:      Phase 1 INERTIA-SURFACE — Status-quo claim
    Transit:     Phase 5 ANCHOR-CARD Frame
    Destination: Phase 6 REGISTRY.md — inertia_surface
    Integrity rule: exact words at destination; fulfills EXTENSION-COMMITMENT

  Chain D — Anchor name provenance:
    Source:      Phase 1 INERTIA-SURFACE — Status-quo claim vocabulary
    Transit:     Phase 5 ANCHOR-CARD — ANCHOR-SOURCING statement
    Destination: Phase 5 ANCHOR-CARD YAML — name field
    Integrity rule: anchor name term traceable to INERTIA-SURFACE; generic breaks D

  Chain E — Challenge-question coverage (new in V-03):
    Source:      Phase 1 INERTIA-SURFACE — Challenge questions (minimum three)
    Transit:     Phase 5 CHALLENGE-COVERAGE MAP — coverage mapping rows
    Destination: Phase 5 ANCHOR-CARD YAML — lens.verify_questions (all challenge
                 questions represented)
    Integrity rule: every Phase 1 challenge question maps to at least one anchor
      verify_question; gaps detected in MAP must be resolved before MAP is closed;
      an anchor whose verify_questions leave any Phase 1 challenge question uncovered
      breaks Chain E
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT written [C-23/C-30]
2. FIELD-CONTRACT written [FC-1] through [FC-12] [C-26]
3. [FC-1] contains PROHIBITED NAMES, POSITIVE SOURCING REQUIRED, ANCHOR-SOURCING REQUIRED [C-28/C-31]
4. [FC-4]/[FC-5] EXACT IDENTIFIER labels [C-24/C-07]
5. [FC-10] CONTRACT VIOLATION labels [C-29]
6. [FC-11] REQUIRED FORMAT [C-46]
7. [FC-12] REQUIRED FORMAT; positional failure [C-47]
8. PROVENANCE-CHAIN DECLARATION with five chains (A-E); Source/Transit/Destination/Integrity
   rule per chain [C-52]

---

PHASE 1 — INERTIA SURFACE

```
INERTIA-SURFACE for {topic}:
  Status-quo claim: [strongest argument {topic} is premature; specific capability]
  Challenge questions (minimum three; {topic} vocabulary):
    Q1: What specific failure does the status quo produce?
    Q2: [what existing mechanism handles?]
    Q3: [minimum fix and why insufficient?]
```

Note: Phase 1 challenge questions are the Chain E source — the CHALLENGE-COVERAGE MAP
in Phase 5 will walk each question and confirm anchor verify_question coverage.

**GATE:** status-quo claim with named capability; minimum three challenge questions;
no expert names. [C-02/C-39 precondition]

---

PHASE 2 — DOMAIN ANALYSIS

**Step 1 — INERTIA-GAP ANALYSIS** (minimum three named gaps; each with Domain, Failure mode,
Inertia resistance; GAP-{slug} from Domain vocabulary; no expert names):

```
INERTIA-GAP ANALYSIS for {topic}:
  GAP-{slug-1}: Domain: [...]; Failure mode: [...]; Inertia resistance: [...]
  GAP-{slug-2}: ...
  GAP-{slug-3}: ...
```

**Step 2 — EXPERT DERIVATION** (one entry per gap; POSITIVE SOURCING per expert;
no PM/Architect/Strategy/inertia-advocate):

```
DOMAIN-ANALYSIS for {topic}:
  - Expert name: [from GAP-{slug} vocabulary]
    POSITIVE SOURCING: "this name derives from GAP-{slug}: [term]"
    Named gap source: GAP-{slug}
    Inertia gap: [verbatim]
    Domain-vocabulary frame: [per [FC-2]]
    Verify focus: [first-check artifact]
```

**GATE:** INERTIA-GAP ANALYSIS before DOMAIN-ANALYSIS; three gaps; POSITIVE SOURCING per
expert; no placeholders [C-39/C-44/C-45/C-40/C-28/C-31].

---

PHASE 3 — STOCK ROLES

```
STOCK-ROLES:
  - inertia-advocate  (ANCHOR-CARD; Phase 1 frame; written first; anchor: true;
                       verify_questions sourced from Phase 1 challenge questions;
                       CHALLENGE-COVERAGE MAP written after ANCHOR-CARD before other cards)
  - pm
  - architect
  - strategy
```

**GATE:** [C-03/C-37/C-46/C-47] confirmed; CHALLENGE-COVERAGE MAP mandate noted.

---

PHASE 4 — OUTPUT AREA

```
OUTPUT-AREA: .roles/{area}/
```

Area slug from Phase 2 GAP Domain vocabulary. NOT: `default`, `generic`, `roles`.
**GATE:** [C-04] confirmed.

---

PHASE 5 — DIAGNOSIS CARDS AND ROLE FILE WRITING

**PREPARE:** Confirm ten inputs (Phase 0 identifiers/formats/chains; Phase 1 INERTIA-SURFACE;
Phase 2 INERTIA-GAP ANALYSIS + DOMAIN-ANALYSIS; Phase 3 STOCK-ROLES; Phase 4 OUTPUT-AREA).
[C-07/C-24/C-46/C-47/C-52/C-02/C-39/C-44/C-40/C-45/C-03/C-37/C-04]

**ANCHOR-CARD (write first):**

```
ANCHOR-CARD for inertia-advocate:
  name: {INERTIA-SURFACE vocabulary; ANCHOR-SOURCING: "this name derives from
    INERTIA-SURFACE: [term]" — Chain D transit; [FC-1] confirmed}
  frame: {Phase 1 status-quo claim as epistemic stance — Chain C transit}
  serves: {beneficiary — NOT restatement}
  primary_verify_question: {adversarial sufficiency — Chain B source; scan reference}
  verify_questions planned: [{list all planned verify_questions for anchor}]
    (list here to enable CHALLENGE-COVERAGE MAP below)
  uniqueness argument: confirmed distinct
  anchor status: ANCHOR-CARD
  collaborates_with: [{names}]; phantom check: confirmed
```

**CHALLENGE-COVERAGE MAP (write immediately after ANCHOR-CARD Diagnosis Card; before any
other Diagnosis Card):**

```
CHALLENGE-COVERAGE MAP for /org-roles {topic}:

  Phase 1 challenge questions (from INERTIA-SURFACE — complete list):
    Q1: [verbatim text]
    Q2: [verbatim text]
    Q3: [verbatim text]
    (continue for all challenge questions)

  Coverage mapping:
  | Phase 1 Challenge Question | Represented in ANCHOR-CARD verify_questions? | Evidence |
  |----------------------------|----------------------------------------------|----------|
  | Q1: [text] | YES / NO | [which anchor verify_question covers this; or "absent"] |
  | Q2: [text] | YES / NO | [evidence] |
  | Q3: [text] | YES / NO | [evidence] |

  Coverage assessment:
    Covered: {count YES}
    Uncovered: {count NO} — {list question texts}

  CHALLENGE-COVERAGE GATE:
    - [ ] Every Phase 1 challenge question appears in the mapping table [new/Chain E]
    - [ ] All questions marked YES (PASS) or gap resolution recorded (see below)

  Gap resolution (if any questions marked NO):
    For each uncovered question: add a corresponding verify_question to the ANCHOR-CARD
    planned list and mark question as RESOLVED.
    Do not proceed to subsequent Diagnosis Cards until all questions are covered or resolved.
```

Chain E transit confirmed: CHALLENGE-COVERAGE MAP complete; all Phase 1 challenge questions
represented in ANCHOR-CARD verify_questions.

Do not write subsequent Diagnosis Cards until CHALLENGE-COVERAGE MAP gate is confirmed.

**SUBSEQUENT DIAGNOSIS CARDS (after CHALLENGE-COVERAGE MAP):**

```
DIAGNOSIS-CARD for {role-name}:
  name: {experts: GAP-{slug} vocabulary + POSITIVE SOURCING; stock: standard; confirmed}
  frame: {GAP vocabulary (experts) / standard (stock)}
  serves: {beneficiary — NOT restatement}
  inertia gap inherited: {"GAP-{slug}: [verbatim]" (experts) / N/A (stock) — Chain A}
  orthogonality to ANCHOR-CARD: {per [FC-11] — Chain B transit; verbatim to YAML}
  primary_verify_question: {role-specific}
  uniqueness argument: [reason]; confirmed distinct
  collaborates_with: [{names}]; phantom check: confirmed
```

After all Diagnosis Cards, produce **ORTHOGONALITY COMPLETENESS TABLE** (same structure as
V-01/V-02: ANCHOR primary question + non-anchor table with contrast axes + pairwise
distinctness check + gate).

After TABLE, run **CROSS-CARD UNIQUENESS SCAN** (Phase 1 Enumerate → Phase 2
Anchor-Orthogonality → Phase 3 Non-Anchor Pairwise → Phase 4 Revision-Resolution).

**SCAN ORDERING GATE** — confirm before writing any YAML:
- [ ] CHALLENGE-COVERAGE MAP complete; all Phase 1 challenge questions represented [new/Chain E]
- [ ] ORTHOGONALITY COMPLETENESS TABLE complete; all rows PASS [new]
- [ ] Phase 1 (Enumerate) executed first; no checking in Phase 1 [C-42]
- [ ] Phase 2 after Phase 1 complete; before Phase 3 [C-50]
- [ ] Phase 3 after Phase 2 complete; before Phase 4 [C-50]
- [ ] Phase 4 last; flags from Phase 2 AND Phase 3 [C-43]
- [ ] No phases merged; canonical sequence: CCM → Table → P1 → P2 → P3 → P4 [C-48]

**WRITE:** anchor first, then experts, then stock. YAML template (same structure as all
R13 variations): name/version/archetype/anchor (anchor only)/orthogonality (non-anchor)/
inertia_gap_inherited (experts)/orientation/lens/expertise/scope/collaborates_with with
CONTRACT VIOLATION labels.

Checklist [C-51: criterion-ID per item]:
- [ ] `verify_questions` exact [C-07/FC-4]
- [ ] `simplify_rules` exact [C-07/FC-5]
- [ ] `orthogonality` per [FC-11] for non-anchor [C-46]
- [ ] `orthogonality` matches TABLE axis [C-35]
- [ ] `inertia_gap_inherited` per [FC-12] for experts [C-47]
- [ ] `anchor: true` in anchor only [C-37]
- [ ] ANCHOR-CARD verify_questions cover all Phase 1 challenge questions per CCM [new/Chain E]
- [ ] No PHANTOM [C-29/C-33]
- [ ] No UNIVERSALIST [C-29/C-33]

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. ANCHOR-CARD written first [C-37]
2. CHALLENGE-COVERAGE MAP written after ANCHOR-CARD; before subsequent cards; gate confirmed [new]
3. All Phase 1 challenge questions represented in ANCHOR-CARD verify_questions [new/Chain E]
4. ORTHOGONALITY COMPLETENESS TABLE complete; all rows PASS [new]
5. CROSS-CARD UNIQUENESS SCAN four phases; SCAN ORDERING GATE confirmed (seven items) [C-42/C-43/C-48/C-50]
6. YAML written; anchor first; correct field presence per role type [C-37/C-46/C-47]
7. Chains A-E traceable through transit artifacts to YAML [C-52]
8. Checklist items carry [C-NN] annotations [C-51]

---

PHASE 6 — REGISTRY SUMMARY

(Identical to V-01/V-02 Phase 6.)

**COVERAGE-GATE:** walk each Phase 2 GAP-{slug}; COVERED/GAP status; `coverage_gaps` from
enumeration not memory.

**PREPARE:** `PHASE5_COUNT` from Phase 5 enumeration only.

**WRITE:** `.roles/{area}/REGISTRY.md` per standard template.

**GATE:** [C-04/C-22/C-27/C-10/C-20/C-23/C-15/C-52] confirmed.

---

**Final checklist — confirm before declaring done:**

Challenge coverage (new): CHALLENGE-COVERAGE MAP written after ANCHOR-CARD Diagnosis Card;
every Phase 1 challenge question mapped; all represented in anchor verify_questions;
Chain E traceable from Phase 1 questions through MAP to ANCHOR-CARD YAML verify_questions

Phase output (C-37/C-46): anchor YAML `anchor: true`; non-anchor `orthogonality` matching
TABLE; expert `inertia_gap_inherited` verbatim

Scan structure (C-42/C-43/C-48/C-50): SCAN ORDERING GATE seven items confirmed (CCM first,
TABLE second, then four-phase scan)

Orthogonality completeness: TABLE; distinct axes; all PASS

Gap/sourcing (C-39/C-44/C-40/C-45): INERTIA-GAP ANALYSIS before naming; POSITIVE SOURCING;
ANCHOR-SOURCING

Provenance chains (C-52): five chains (A-E); all traceable

Contract violations (C-29/C-33): labels present

Pipeline annotations (C-51): [C-NN] on all items

Coverage gate: COVERAGE-GATE; coverage_gaps from enumeration

---

## V-04 — Combined: VERIFY-MAP + SIMPLIFY-DOMAIN GATE

**axis:** lifecycle emphasis + output format (V-01 + V-02)
**hypothesis:** V-01 adds VERIFY-MAP to Phase 2 to trace verify_question interrogation focus
to GAP Failure modes. V-02 adds SIMPLIFY-DOMAIN CHECK to Phase 5 to confirm domain-term
presence in simplify_rules. These mechanisms target distinct bypass classes: VERIFY-MAP
prevents verify-focus drift (question vocabulary matches gap but question doesn't interrogate
the failure mode), and SIMPLIFY-DOMAIN CHECK prevents simplify-rule genericness (exclusion
is opinionated but domain-agnostic). V-04 tests that both mechanisms coexist in the formal
Phase register without structural conflict and that both maintain 100.00 under v12.

---

You are running `/org-roles {topic}`.

---

PHASE 0 — FIELD CONTRACT, EXTENSION COMMITMENT, AND PROVENANCE CHAINS

**EXTENSION-COMMITMENT:** (same as V-01)

**FIELD CONTRACT:**

```
FIELD-CONTRACT for /org-roles {topic}:

  [FC-1]  name — domain-vocabulary slug
          PROHIBITED NAMES: "domain-expert", "expert-1", "generic-expert", "role-1"
          Experts: POSITIVE SOURCING REQUIRED ("this name derives from GAP-{slug}: [term]")
          Anchor: ANCHOR-SOURCING REQUIRED ("this name derives from INERTIA-SURFACE: [term]")

  [FC-2]  orientation.frame — epistemic viewpoint; FAILURE MODE: task list

  [FC-3]  orientation.serves — beneficiary; NOT frame restatement

  [FC-4]  lens.verify_questions
          EXACT IDENTIFIER: verify_questions
          PROHIBITED: verify | questions | checks | verify_list
          minimum two; uniqueness argument required

  [FC-5]  lens.simplify_rules
          EXACT IDENTIFIER: simplify_rules
          PROHIBITED: simplify | rules | constraints | guidelines
          minimum one; opinionated exclusion — NOT scope description
          SIMPLIFY-DOMAIN REQUIREMENT: each rule must contain at least one named domain
            artifact, mechanism, field, or vocabulary term specific to this domain
          BAD: "Skip obvious things"; GOOD: "Skip {domain-artifact} unless {condition}"

  [FC-6]  expertise.depth — enum: expert | practitioner | senior | principal

  [FC-7]  expertise.relevance — domain-specific; not role-name restatement

  [FC-8]  scope.primary — main concern; one sentence

  [FC-9]  scope.boundary — explicit exclusion; one sentence

  [FC-10] collaborates_with — registry members only
          CONTRACT VIOLATION (type 1) — PHANTOM: absent from registry
          CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent

  [FC-11] orthogonality — non-anchor YAML; REQUIRED FORMAT: "[axis] — diverges from
          ANCHOR-CARD because [specific reason]"; YAML persistence required

  [FC-12] inertia_gap_inherited — expert YAML; REQUIRED FORMAT: "GAP-{slug}: [verbatim]";
          positional reference fails; YAML persistence required
```

**PROVENANCE-CHAIN DECLARATION:**

```
PROVENANCE-CHAIN DECLARATION for /org-roles {topic}:

  Chain A: Source: Phase 2 GAP-{slug}.Inertia resistance | Transit: Phase 5 Diagnosis Card
    inertia gap inherited | Destination: Phase 5 YAML inertia_gap_inherited
    Integrity: verbatim; GAP-{slug} by name; positional breaks A

  Chain B: Source: Phase 5 SCAN + ANCHOR primary question | Transit: Phase 5 Diagnosis Card
    Orthogonality to ANCHOR-CARD | Destination: Phase 5 YAML orthogonality
    Integrity: verbatim; named contrast axis; generic breaks B

  Chain C: Source: Phase 1 Status-quo claim | Transit: Phase 5 ANCHOR-CARD Frame
    Destination: Phase 6 REGISTRY.md inertia_surface
    Integrity: exact words at destination; fulfills EXTENSION-COMMITMENT

  Chain D: Source: Phase 1 INERTIA-SURFACE vocabulary | Transit: Phase 5 ANCHOR-CARD
    ANCHOR-SOURCING statement | Destination: Phase 5 ANCHOR-CARD YAML name
    Integrity: anchor name term from INERTIA-SURFACE; generic breaks D

  Chain E: Source: Phase 2 INERTIA-GAP ANALYSIS GAP-{slug}.Failure mode
    Transit: Phase 2 VERIFY-MAP Interrogates gap because
    Destination: Phase 5 YAML lens.verify_questions[0]
    Integrity: primary verify_question interrogates GAP Failure mode; disconnected
      focus breaks E; vocabulary match alone insufficient
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT written [C-23/C-30]
2. FIELD-CONTRACT items [FC-1] through [FC-12] all written [C-26]
3. [FC-1] PROHIBITED NAMES + POSITIVE SOURCING + ANCHOR-SOURCING [C-28/C-31]
4. [FC-4]/[FC-5] EXACT IDENTIFIER labels [C-24/C-07]
5. [FC-5] SIMPLIFY-DOMAIN REQUIREMENT with BAD/GOOD examples [new]
6. [FC-10] CONTRACT VIOLATION labels [C-29]
7. [FC-11] REQUIRED FORMAT + YAML persistence [C-46]
8. [FC-12] REQUIRED FORMAT + positional failure + YAML persistence [C-47]
9. PROVENANCE-CHAIN DECLARATION with five chains (A-E) [C-52]

---

PHASE 1 — INERTIA SURFACE

```
INERTIA-SURFACE for {topic}:
  Status-quo claim: [specific capability; Chain C source; Chain D vocabulary source]
  Challenge questions (minimum three; {topic} vocabulary):
    Q1: [failure produced]; Q2: [existing handling]; Q3: [minimum fix and why insufficient]
```

**GATE:** status-quo claim; three challenge questions; no expert names. [C-02/C-39]

---

PHASE 2 — DOMAIN ANALYSIS (with VERIFY-MAP)

**Step 1 — INERTIA-GAP ANALYSIS** (minimum three; GAP-{slug} from Domain vocabulary):

```
INERTIA-GAP ANALYSIS for {topic}:
  GAP-{slug-1}: Domain: [...]; Failure mode: [...]; Inertia resistance: [...]
  GAP-{slug-2}: ...
  GAP-{slug-3}: ...
```

**Step 2 — EXPERT DERIVATION:**

```
DOMAIN-ANALYSIS for {topic}:
  - Expert name: [GAP vocabulary slug]
    POSITIVE SOURCING: "this name derives from GAP-{slug}: [term]"
    Named gap source: GAP-{slug}
    Inertia gap: [verbatim]
    Domain-vocabulary frame: [per [FC-2]]
    Verify focus: [first-check artifact or behavior]
```

**Step 3 — VERIFY-MAP (new):**

```
VERIFY-MAP for /org-roles {topic}:

  {expert-name}:
    Source gap: GAP-{slug}
    Verify focus (from DOMAIN-ANALYSIS): [text]
    Interrogates gap because: [connection to GAP-{slug} Failure mode — name the failure;
      state why the verify focus surfaces or prevents it]
    Chain E status: PASS | FLAG

  (one entry per domain expert)

Resolve all FLAGs before Phase 3. Rewrite flagged verify focuses in DOMAIN-ANALYSIS
and VERIFY-MAP with revised focus and explanation.
```

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. INERTIA-GAP ANALYSIS before DOMAIN-ANALYSIS; minimum three gaps [C-39/C-44]
2. GAP-{slug} from Domain vocabularies [C-44]
3. POSITIVE SOURCING per expert; GAP-{slug} and term cited [C-45/C-40]
4. No placeholders [C-28/C-31] — checkpoint 2 of 3
5. VERIFY-MAP written; all experts PASS Chain E status; FLAGs resolved [new]

---

PHASE 3 — STOCK ROLES

```
STOCK-ROLES:
  - inertia-advocate  (ANCHOR-CARD; Phase 1 frame; written first; anchor: true)
  - pm; architect; strategy
```

**GATE:** [C-03/C-37/C-46/C-47] confirmed.

---

PHASE 4 — OUTPUT AREA

```
OUTPUT-AREA: .roles/{area}/
```

**GATE:** [C-04] confirmed.

---

PHASE 5 — DIAGNOSIS CARDS, SIMPLIFY-DOMAIN CHECK, AND ROLE FILE WRITING

**PREPARE:** eleven inputs — Phase 0 identifiers/formats; PROVENANCE-CHAIN five chains;
Phase 1 INERTIA-SURFACE; Phase 2 INERTIA-GAP ANALYSIS + DOMAIN-ANALYSIS + VERIFY-MAP
(all PASS); Phase 3 STOCK-ROLES; Phase 4 OUTPUT-AREA.
[C-07/C-24/C-46/C-47/C-52/C-02/C-39/C-44/C-40/C-45/C-03/C-37/C-04]

**ANCHOR-CARD (write first):**

```
ANCHOR-CARD for inertia-advocate:
  name: {INERTIA-SURFACE vocabulary; ANCHOR-SOURCING: "this name derives from
    INERTIA-SURFACE: [term]" — Chain D transit; NOT placeholder}
  frame: {Phase 1 status-quo claim — Chain C transit}
  serves: {beneficiary}
  primary_verify_question: {adversarial sufficiency — Chain B source; scan reference}
  uniqueness: confirmed distinct
  anchor status: ANCHOR-CARD
  collaborates_with: [{names}]; phantom check: confirmed
  SIMPLIFY-DOMAIN PLAN: list planned simplify_rules; domain term per rule; PASS/FLAG
```

**SUBSEQUENT DIAGNOSIS CARDS:**

```
DIAGNOSIS-CARD for {role-name}:
  name: {GAP vocabulary + POSITIVE SOURCING (experts) / standard (stock)}
  frame / serves / inertia gap inherited / orthogonality to ANCHOR-CARD (per standard)
  primary_verify_question: {role-specific}
  VERIFY-MAP check (experts): confirm verify_question interrogates GAP Failure mode [new]
  collaborates_with: [{names}]; phantom check: confirmed
  SIMPLIFY-DOMAIN PLAN: Rule N: [text] — domain term: [{term}] — PASS/FLAG
```

After all Diagnosis Cards, **ORTHOGONALITY COMPLETENESS TABLE** (ANCHOR primary question +
non-anchor table; contrast axis pairwise distinctness; all rows PASS before scan).

After TABLE, **CROSS-CARD UNIQUENESS SCAN** (Phase 1 Enumerate → Phase 2
Anchor-Orthogonality → Phase 3 Non-Anchor Pairwise → Phase 4 Revision-Resolution).

**SCAN ORDERING GATE:**
- [ ] ORTHOGONALITY COMPLETENESS TABLE complete; all rows PASS [new]
- [ ] Phase 1 first; no checking [C-42]
- [ ] Phase 2 after Phase 1; before Phase 3 [C-50]
- [ ] Phase 3 after Phase 2; before Phase 4 [C-50]
- [ ] Phase 4 last; flags from 2 AND 3 [C-43]
- [ ] No phases merged [C-48]
- [ ] Canonical sequence: Table → P1 → P2 → P3 → P4 [C-48]

**SIMPLIFY-DOMAIN CHECK** (before each role's YAML):

```
SIMPLIFY-DOMAIN CHECK for {role-name}:
  Rule 1: [{text}] — domain term: [{term}] — PASS | FLAG
  Rule 2: [{text}] — domain term: [{term}] — PASS | FLAG
  GATE: all rules PASS [new/FC-5]
```

```yaml
---
name: {[FC-1] confirmed}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}
anchor: true            # ANCHOR-CARD only
orthogonality: "{[FC-11] — from TABLE; verbatim; named axis}"  # non-anchor
inertia_gap_inherited: "{[FC-12] — GAP-{slug}: [verbatim]}"   # experts
orientation:
  frame: |
    {[FC-2]}
  serves: |
    {[FC-3]}
lens:
  verify_questions:
    - "{primary — Chain E destination for experts: interrogates GAP Failure mode}"
    - "{additional}"
  simplify_rules:
    - "{[FC-5] + SIMPLIFY-DOMAIN REQUIREMENT: contains named domain term}"
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
  - {phantom confirmed}
  # CONTRACT VIOLATION (type 1) — PHANTOM [C-29]
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST [C-29]
```

Checklist [C-51]:
- [ ] `verify_questions` exact [C-07/FC-4]
- [ ] `simplify_rules` exact [C-07/FC-5]
- [ ] `orthogonality` per [FC-11]; non-anchor only [C-46]; matches TABLE [C-35]
- [ ] `inertia_gap_inherited` per [FC-12]; experts only [C-47]
- [ ] `anchor: true`; anchor only [C-37]
- [ ] Expert verify_questions[0] interrogates GAP Failure mode per VERIFY-MAP [new/Chain E]
- [ ] All simplify_rules contain named domain terms per SIMPLIFY-DOMAIN CHECK [new/FC-5]
- [ ] No PHANTOM [C-29/C-33]; no UNIVERSALIST [C-29/C-33]

**GATE** — Phase 5 complete when ALL TRUE:
1. ANCHOR-CARD first [C-37]; chains A-E traceable [C-52]
2. VERIFY-MAP checked per expert; Chain E confirmed [new]
3. SIMPLIFY-DOMAIN CHECK per role; all PASS [new]
4. TABLE complete; all rows PASS [new]
5. SCAN four phases; ORDERING GATE seven items [C-42/C-43/C-48/C-50]
6. YAML correct per role type [C-37/C-46/C-47]; criterion annotations [C-51]

---

PHASE 6 — REGISTRY SUMMARY

COVERAGE-GATE (Phase 2 GAP-{slug} walk; COVERED/GAP; coverage_gaps from enumeration).
PHASE5_COUNT from Phase 5 enumeration only.
REGISTRY.md: total_roles/stock_roles/domain_experts/coverage_gaps/inertia_surface verbatim.
**GATE:** [C-04/C-22/C-27/C-10/C-20/C-23/C-15/C-52].

---

**Final checklist:**

Verify-question traceability (new): VERIFY-MAP in Phase 2; all experts Chain E PASS;
primary verify_questions interrogate GAP Failure modes; Chain E traceable to YAML

Simplify-rule domain specificity (new): SIMPLIFY-DOMAIN CHECK per role before YAML;
SIMPLIFY-DOMAIN REQUIREMENT in [FC-5]; all rules contain named domain terms

Scan/orthogonality: TABLE before scan; SCAN ORDERING GATE seven items; four-phase scan

Phase output (C-37/C-46/C-47): anchor YAML/non-anchor YAML/expert YAML correct

Provenance chains (C-52): five chains declared; A-E traceable

Coverage gate: COVERAGE-GATE; coverage_gaps from enumeration

Pipeline annotations (C-51): all [C-NN]

---

## V-05 — Combined: All Three Axes + Role Sequence Change

**axis:** lifecycle emphasis + output format + inertia framing + role sequence
(V-01 + V-02 + V-03 + YAML write order: anchor → stock → experts)
**hypothesis:** V-04 carries VERIFY-MAP (V-01) and SIMPLIFY-DOMAIN GATE (V-02) in the
formal Phase register. V-05 adds V-03's CHALLENGE-COVERAGE MAP and switches the YAML
write order from anchor → experts → stock to anchor → stock → experts. C-37 mandates
anchor-first but is silent on expert-vs-stock order. Current R12/R13 V-01-V-04 all write
experts before stock because Phase 2 produces expert names before Phase 3 produces stock
names. V-05 tests whether any criterion implicitly assumes expert-before-stock ordering
(e.g., a criterion checking collaborates_with could produce a phantom if the stock role
YAML is written before expert names are confirmed — though all names are known from
DOMAIN-ANALYSIS and STOCK-ROLES before writing begins). Falsifiable: if all criteria pass
with anchor → stock → experts order, the ordering assumption is not load-bearing. If a
criterion regresses, the implicit ordering dependency is surfaced as a structural finding.

---

You are running `/org-roles {topic}`.

---

PHASE 0 — FIELD CONTRACT, EXTENSION COMMITMENT, AND PROVENANCE CHAINS

**EXTENSION-COMMITMENT:** (same as all R13 variations)

```
EXTENSION-COMMITMENT:
  field_name: inertia_surface
  population_source: Phase 1, INERTIA-SURFACE block, status-quo claim field
  purpose: answers Phase 0 diagnostic question — "what is the strongest existing-system
    argument that makes {topic} premature?"
```

**FIELD CONTRACT:**

```
FIELD-CONTRACT for /org-roles {topic}:

  [FC-1]  name — domain-vocabulary slug
          PROHIBITED NAMES: "domain-expert", "expert-1", "generic-expert", "role-1"
          Experts: POSITIVE SOURCING REQUIRED ("this name derives from GAP-{slug}: [term]")
          Anchor: ANCHOR-SOURCING REQUIRED ("this name derives from INERTIA-SURFACE: [term]")
          BAD: placeholder; GOOD (expert): from GAP vocabulary; GOOD (anchor): from
            INERTIA-SURFACE claim vocabulary

  [FC-2]  orientation.frame — epistemic viewpoint; FAILURE MODE: task list

  [FC-3]  orientation.serves — beneficiary; NOT frame restatement

  [FC-4]  lens.verify_questions
          EXACT IDENTIFIER: verify_questions
          PROHIBITED: verify | questions | checks | verify_list
          minimum two; uniqueness argument required

  [FC-5]  lens.simplify_rules
          EXACT IDENTIFIER: simplify_rules
          PROHIBITED: simplify | rules | constraints | guidelines
          minimum one; opinionated exclusion; NOT scope description
          SIMPLIFY-DOMAIN REQUIREMENT: each rule contains at least one named domain
            artifact, mechanism, field, or vocabulary term; generic terms alone fail

  [FC-6]  expertise.depth — enum: expert | practitioner | senior | principal

  [FC-7]  expertise.relevance — domain-specific

  [FC-8]  scope.primary — main concern; one sentence

  [FC-9]  scope.boundary — explicit exclusion; one sentence

  [FC-10] collaborates_with — registry members only
          CONTRACT VIOLATION (type 1) — PHANTOM: absent from registry
          CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent

  [FC-11] orthogonality — non-anchor YAML only
          REQUIRED FORMAT: "[axis] — this role's lens diverges from ANCHOR-CARD because
            [specific reason naming anchor's question and how this concern falls outside]"
          YAML persistence required; not only in Diagnosis Card

  [FC-12] inertia_gap_inherited — expert YAML only
          REQUIRED FORMAT: "GAP-{slug}: [verbatim resistance]"
          Positional reference ("Gap 1:") fails; YAML persistence required
```

**PROVENANCE-CHAIN DECLARATION:**

```
PROVENANCE-CHAIN DECLARATION for /org-roles {topic}:

  Chain A — Inertia gap:
    Source:      Phase 2 INERTIA-GAP ANALYSIS — GAP-{slug}.Inertia resistance
    Transit:     Phase 5 Diagnosis Card — inertia gap inherited
    Destination: Phase 5 YAML — inertia_gap_inherited
    Integrity:   verbatim; GAP-{slug} named; positional breaks A

  Chain B — Orthogonality:
    Source:      Phase 5 SCAN + ANCHOR primary question
    Transit:     Phase 5 Diagnosis Card — Orthogonality to ANCHOR-CARD
    Destination: Phase 5 YAML — orthogonality
    Integrity:   verbatim; named contrast axis; generic breaks B

  Chain C — Inertia surface:
    Source:      Phase 1 Status-quo claim
    Transit:     Phase 5 ANCHOR-CARD Frame
    Destination: Phase 6 REGISTRY.md inertia_surface
    Integrity:   exact words at destination

  Chain D — Anchor name:
    Source:      Phase 1 INERTIA-SURFACE vocabulary
    Transit:     Phase 5 ANCHOR-CARD ANCHOR-SOURCING
    Destination: Phase 5 ANCHOR-CARD YAML name
    Integrity:   term traceable to INERTIA-SURFACE; generic breaks D

  Chain E — Verify-question-to-gap:
    Source:      Phase 2 INERTIA-GAP ANALYSIS — GAP-{slug}.Failure mode
    Transit:     Phase 2 VERIFY-MAP — Interrogates gap because
    Destination: Phase 5 YAML — lens.verify_questions[0]
    Integrity:   primary verify_question interrogates GAP Failure mode; disconnected breaks E

  Chain F — Challenge coverage:
    Source:      Phase 1 INERTIA-SURFACE — Challenge questions
    Transit:     Phase 5 CHALLENGE-COVERAGE MAP — coverage mapping rows
    Destination: Phase 5 ANCHOR-CARD YAML — lens.verify_questions
    Integrity:   all Phase 1 challenge questions represented; uncovered questions
                 added before MAP closes; unresolved breaks F
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT written [C-23/C-30]
2. FIELD-CONTRACT [FC-1] through [FC-12] [C-26]
3. [FC-1]: PROHIBITED NAMES + POSITIVE SOURCING + ANCHOR-SOURCING [C-28/C-31]
4. [FC-4]/[FC-5] EXACT IDENTIFIER labels [C-24/C-07]
5. [FC-5] SIMPLIFY-DOMAIN REQUIREMENT + BAD/GOOD examples [new]
6. [FC-10] CONTRACT VIOLATION labels [C-29]
7. [FC-11] REQUIRED FORMAT + YAML persistence [C-46]
8. [FC-12] REQUIRED FORMAT + positional failure + YAML persistence [C-47]
9. PROVENANCE-CHAIN DECLARATION with six chains (A-F); each with Source/Transit/
   Destination/Integrity rule [C-52]

---

PHASE 1 — INERTIA SURFACE

```
INERTIA-SURFACE for {topic}:
  Status-quo claim: [specific capability; Chain C + D source vocabulary; note terms]
  Challenge questions (minimum three; {topic} vocabulary):
    Q1: [failure produced]
    Q2: [existing handling]
    Q3: [minimum fix and why insufficient]
```

Note the specific vocabulary terms from the status-quo claim for anchor name (Chain D).
All challenge questions are Chain F source — CHALLENGE-COVERAGE MAP will verify coverage.
**GATE:** [C-02/C-39 precondition] — claim + three questions + no expert names.

---

PHASE 2 — DOMAIN ANALYSIS (with VERIFY-MAP)

**Step 1 — INERTIA-GAP ANALYSIS** (minimum three; GAP-{slug} from Domain vocabulary;
Domain/Failure mode/Inertia resistance per entry; no expert names):

```
INERTIA-GAP ANALYSIS for {topic}:
  GAP-{slug-1}: Domain: [...]; Failure mode: [...]; Inertia resistance: [...]
  GAP-{slug-2}: ...
  GAP-{slug-3}: ...
```

**Step 2 — EXPERT DERIVATION** (POSITIVE SOURCING per expert; no stock roles):

```
DOMAIN-ANALYSIS for {topic}:
  - Expert name: [GAP vocabulary slug]
    POSITIVE SOURCING: "this name derives from GAP-{slug}: [term]"
    Named gap source: GAP-{slug}
    Inertia gap: [verbatim]
    Domain-vocabulary frame: [per [FC-2]]
    Verify focus: [first-check artifact]
```

**Step 3 — VERIFY-MAP** (Chain E transit; one entry per expert; PASS/FLAG; resolve before
Phase 3):

```
VERIFY-MAP for /org-roles {topic}:
  {expert-name}:
    Source gap: GAP-{slug}
    Verify focus: [from DOMAIN-ANALYSIS]
    Interrogates gap because: [connection to GAP-{slug} Failure mode — name it]
    Chain E status: PASS | FLAG
```

**GATE:** [C-39/C-44/C-45/C-40/C-28/C-31]; VERIFY-MAP all PASS [new].

---

PHASE 3 — STOCK ROLES

```
STOCK-ROLES:
  - inertia-advocate  (ANCHOR-CARD; Phase 1 frame; written first; anchor: true;
                       CHALLENGE-COVERAGE MAP after ANCHOR-CARD)
  - pm; architect; strategy
```

**WRITE ORDER NOTE:** In Phase 5, YAML files are written: inertia-advocate (ANCHOR-CARD)
first, then stock roles (pm, architect, strategy), then domain experts. This order reverses
the expert-before-stock convention used in R12 and R13 V-01-V-04. All names are known from
Phase 2 and Phase 3 before writing begins; phantom checks are unaffected.

**GATE:** [C-03/C-37/C-46/C-47] confirmed; write-order noted.

---

PHASE 4 — OUTPUT AREA

```
OUTPUT-AREA: .roles/{area}/
```

**GATE:** [C-04] confirmed.

---

PHASE 5 — DIAGNOSIS CARDS, CHALLENGE-COVERAGE MAP, SIMPLIFY-DOMAIN CHECK, ROLE FILES

**PREPARE:** twelve inputs — Phase 0 (identifiers/formats/six chains); Phase 1 INERTIA-SURFACE
(challenge questions confirmed for Chain F); Phase 2 INERTIA-GAP ANALYSIS + DOMAIN-ANALYSIS
+ VERIFY-MAP (all PASS); Phase 3 STOCK-ROLES (write order: anchor → stock → experts noted);
Phase 4 OUTPUT-AREA.
[C-07/C-24/C-46/C-47/C-52/C-02/C-39/C-44/C-40/C-45/C-03/C-37/C-04]

**ANCHOR-CARD (write first):**

```
ANCHOR-CARD for inertia-advocate:
  name: {INERTIA-SURFACE vocabulary; ANCHOR-SOURCING: "this name derives from
    INERTIA-SURFACE: [term]" — Chain D transit}
  [FC-1] name check: INERTIA-SURFACE trace; NOT placeholder; confirmed
  frame: {Phase 1 status-quo claim — Chain C transit}
  serves: {beneficiary}
  primary_verify_question: {adversarial sufficiency — Chain B source; scan reference}
  verify_questions planned: [{all planned verify_questions for anchor — for CCM below}]
  uniqueness: confirmed distinct
  anchor status: ANCHOR-CARD
  collaborates_with: [{names — all from registry}]; phantom check: confirmed
  SIMPLIFY-DOMAIN PLAN: Rule 1: [text] — term: [{domain term}] — PASS/FLAG
```

**CHALLENGE-COVERAGE MAP (immediately after ANCHOR-CARD; before all other Diagnosis Cards):**

```
CHALLENGE-COVERAGE MAP for /org-roles {topic}:

  Phase 1 challenge questions (complete list from INERTIA-SURFACE):
    Q1: [verbatim]; Q2: [verbatim]; Q3: [verbatim]; (all questions)

  Coverage mapping:
  | Phase 1 Challenge Question | In ANCHOR-CARD verify_questions? | Evidence |
  |----------------------------|----------------------------------|----------|
  | Q1 | YES/NO | [covering question or "absent"] |
  | Q2 | YES/NO | [evidence] |
  | Q3 | YES/NO | [evidence] |

  Covered: {count YES}; Uncovered: {count NO}

  CHALLENGE-COVERAGE GATE:
    - [ ] Every Phase 1 question in table [new/Chain F]
    - [ ] All YES or gap resolved (add missing verify_question to anchor before closing)

Chain F transit confirmed. Proceed to subsequent Diagnosis Cards.
```

**SUBSEQUENT DIAGNOSIS CARDS (after CHALLENGE-COVERAGE MAP):**

```
DIAGNOSIS-CARD for {role-name}:
  name: {GAP vocabulary + POSITIVE SOURCING (experts) / standard (stock)}
  frame / serves (standard per role type)
  inertia gap inherited: {"GAP-{slug}: [verbatim]" (experts) / N/A — Chain A transit}
  orthogonality to ANCHOR-CARD: {[FC-11] format — Chain B transit; verbatim to YAML}
  primary_verify_question: {role-specific}
  VERIFY-MAP check (experts): Chain E confirmed — interrogates GAP Failure mode [new]
  collaborates_with: [{registry names}]; phantom check: confirmed
  SIMPLIFY-DOMAIN PLAN: Rule N: [text] — domain term: [{term}] — PASS/FLAG
```

After all Diagnosis Cards, **ORTHOGONALITY COMPLETENESS TABLE** (ANCHOR primary question +
non-anchor rows with contrast axes; pairwise distinctness check; all rows PASS before scan).

After TABLE, **CROSS-CARD UNIQUENESS SCAN** (Phase 1 Enumerate → Phase 2
Anchor-Orthogonality → Phase 3 Non-Anchor Pairwise → Phase 4 Revision-Resolution).

**SCAN ORDERING GATE:**
- [ ] CHALLENGE-COVERAGE MAP complete; all questions covered [new/Chain F]
- [ ] ORTHOGONALITY COMPLETENESS TABLE complete; all rows PASS [new]
- [ ] Phase 1 (Enumerate) first; no checking [C-42]
- [ ] Phase 2 after Phase 1; before Phase 3 [C-50]
- [ ] Phase 3 after Phase 2; before Phase 4 [C-50]
- [ ] Phase 4 last; flags from Phase 2 AND Phase 3 [C-43]
- [ ] No phases merged; canonical sequence: CCM → Table → P1 → P2 → P3 → P4 [C-48]

**WRITE:** YAML files in this order: inertia-advocate (ANCHOR-CARD) FIRST, then stock roles
(pm, architect, strategy), then domain experts. [C-37: anchor first — confirmed]

**SIMPLIFY-DOMAIN CHECK** (before each role's YAML, in write order: anchor → stock → experts):

```
SIMPLIFY-DOMAIN CHECK for {role-name}:
  Rule N: [{text}] — domain term: [{term}] — PASS | FLAG
  GATE: all rules PASS [new/FC-5 SIMPLIFY-DOMAIN REQUIREMENT]
```

```yaml
---
name: {[FC-1] confirmed}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}
anchor: true            # ANCHOR-CARD only
orthogonality: "{[FC-11] — verbatim from TABLE contrast axis}"   # non-anchor
inertia_gap_inherited: "{[FC-12] — GAP-{slug}: [verbatim]}"     # experts
orientation:
  frame: |
    {[FC-2]}
  serves: |
    {[FC-3]}
lens:
  verify_questions:
    - "{primary — Chain E dest (experts): GAP Failure mode; Chain F dest (anchor): covers Q}"
    - "{additional}"
  simplify_rules:
    - "{[FC-5] + SIMPLIFY-DOMAIN REQUIREMENT: named domain term present}"
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
  - {phantom check confirmed — all names from registry}
  # CONTRACT VIOLATION (type 1) — PHANTOM [C-29]
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST [C-29]
```

Checklist [C-51: criterion-ID per item]:
- [ ] `verify_questions` exact [C-07/FC-4]
- [ ] `simplify_rules` exact [C-07/FC-5]
- [ ] `orthogonality` per [FC-11]; non-anchor only [C-46]; matches TABLE [C-35]
- [ ] `inertia_gap_inherited` per [FC-12]; experts only [C-47]
- [ ] `anchor: true`; anchor only [C-37]
- [ ] ANCHOR-CARD verify_questions cover all Phase 1 challenge questions [new/Chain F]
- [ ] Expert verify_questions[0] interrogates GAP Failure mode per VERIFY-MAP [new/Chain E]
- [ ] All simplify_rules contain named domain terms [new/FC-5]
- [ ] No PHANTOM [C-29/C-33]; no UNIVERSALIST [C-29/C-33]
- [ ] Write order confirmed: anchor → stock → experts [new — role sequence]

**GATE** — Phase 5 complete when ALL TRUE:
1. ANCHOR-CARD Diagnosis Card first [C-37]
2. CHALLENGE-COVERAGE MAP after ANCHOR-CARD; gate confirmed; Chain F traced [new]
3. VERIFY-MAP checked per expert Diagnosis Card; Chain E confirmed [new]
4. SIMPLIFY-DOMAIN CHECK per role (in write order: anchor → stock → experts); all PASS [new]
5. ORTHOGONALITY COMPLETENESS TABLE complete; all rows PASS [new]
6. CROSS-CARD UNIQUENESS SCAN four phases; ORDERING GATE confirmed (seven items) [C-42/C-43/C-48/C-50]
7. YAML written: anchor first, then stock (pm/architect/strategy), then experts [C-37/new]
8. Chains A-F each traceable from transit artifacts to YAML destinations [C-52]
9. Checklist items carry [C-NN] annotations [C-51]

---

PHASE 6 — REGISTRY SUMMARY

**COVERAGE-GATE:** walk each Phase 2 GAP-{slug}; COVERED/GAP status; `coverage_gaps` from
enumeration not memory. All FLAGs resolved before REGISTRY.md.

**PREPARE:** `PHASE5_COUNT` from Phase 5 enumeration only (count-bypass fails [C-27]).

**WRITE:** `.roles/{area}/REGISTRY.md`:

```
---
area: {Phase 2 GAP Domain vocabulary}
generated: {date}
---

## Registry Summary

total_roles: {PHASE5_COUNT}

stock_roles:
  - inertia-advocate  (ANCHOR-CARD — Phase 1 source; written first)
  - pm
  - architect
  - strategy

domain_experts:
  - name: {expert-name}
    gap_source: GAP-{slug}
    inertia_gap: {verbatim}

coverage_gaps: |
  {from COVERAGE-GATE Uncovered gaps; or "none detected"}

inertia_surface: |
  {Phase 1 status-quo claim verbatim — Chain C destination}

Generated by: /org-roles {topic} — {date}
```

**GATE:** [C-04/C-22/C-27/C-10/C-20/C-23/C-15/C-52] all confirmed; Chain C verbatim
integrity verified; no heading stubs.

---

**Final checklist — confirm before declaring done:**

Challenge coverage (new/Chain F): CHALLENGE-COVERAGE MAP written after ANCHOR-CARD
Diagnosis Card; every Phase 1 challenge question mapped; all represented in anchor
verify_questions; Chain F traceable from Phase 1 → CCM → ANCHOR-CARD YAML

Verify-question traceability (new/Chain E): VERIFY-MAP in Phase 2; all experts PASS;
primary verify_questions interrogate GAP Failure modes; Chain E to YAML

Simplify-rule domain specificity (new): SIMPLIFY-DOMAIN CHECK per role in write order
(anchor → stock → experts); all simplify_rules contain named domain terms

Write order confirmed: anchor YAML first, then pm/architect/strategy, then domain experts
[C-37 satisfied; role sequence hypothesis tested]

Scan structure (C-42/C-43/C-48/C-50): SCAN ORDERING GATE confirmed (seven items: CCM →
Table → P1 → P2 → P3 → P4)

Orthogonality completeness: TABLE; distinct axes; all PASS

Phase output (C-37/C-46/C-47): anchor `anchor: true`; non-anchor `orthogonality` from TABLE;
expert `inertia_gap_inherited` verbatim

Provenance chains (C-52): six chains (A-F) declared in Phase 0; all traceable

Gap/sourcing (C-39/C-44/C-40/C-45): INERTIA-GAP ANALYSIS before naming; POSITIVE SOURCING;
ANCHOR-SOURCING (Chain D)

Contract violations (C-29/C-33): labels in template and checklist

Pipeline annotations (C-51): all gate and checklist items carry [C-NN]

Coverage gate: COVERAGE-GATE enumerated all Phase 2 gaps; coverage_gaps from enumeration
