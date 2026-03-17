---
skill: quest-variate
skill_target: org-roles
date: 2026-03-16
round: R14
rubric_version: v13
status: variate
---

# org-roles Variate — Round 14

**Date:** 2026-03-16
**Skill:** org-roles
**Rubric:** v13 (C-01 through C-55; denominator /47)
**Round:** R14 — single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

**Context:** R13 V-05 closed the v13 frontier at 100.00 (47/47) carrying all three R13
mechanisms: VERIFY-MAP (Chain E, C-53), SIMPLIFY-DOMAIN GATE (C-54), and CHALLENGE-COVERAGE
MAP (Chain F, C-55), plus 6-chain PROVENANCE-CHAIN DECLARATION and anchor → stock → experts
YAML write order. R14 inherits R13 V-05's full mechanism set as the base for all five
variations and adds three new candidate patterns for v14.

**Post-ceiling framing:** Three candidate strengthening patterns identified from R13 V-05
analysis:

1. **Simplify-rule vocabulary-anchor provenance as Chain G** — C-54 requires each
   simplify_rule to contain at least one named domain term. But no provenance requirement
   governs where that term comes from. A simplify_rule could satisfy C-54 with a
   domain-sounding term that does not appear in any GAP-{slug} Domain vocabulary from Phase 2.
   A SIMPLIFY-VOCABULARY ANCHOR step in the SIMPLIFY-DOMAIN CHECK — requiring each named
   domain term to trace to a specific GAP-{slug} Domain vocabulary entry, with a VOCABULARY
   TRACE citation ("term '{term}' from GAP-{slug} Domain: {vocabulary-source}") — creates the
   same provenance guarantee for simplify_rule vocabulary that POSITIVE SOURCING creates for
   role names. Introduces Chain G in the PROVENANCE-CHAIN DECLARATION.

2. **ROLE-MANIFEST pre-Diagnosis Card forward declaration** — Phase 5 PREPARE confirms inputs
   but does not enumerate the expected set of Diagnosis Cards by name. The ORTHOGONALITY
   COMPLETENESS TABLE is a post-hoc check (after all cards are written) that verifies every
   non-anchor role appears. A ROLE-MANIFEST written after PREPARE and before the first
   Diagnosis Card — listing every expected card name, type (stock/domain-expert/anchor), and
   Phase source — converts the completeness check from post-hoc validation to pre-writing
   forward declaration. The GATE after ROLE-MANIFEST confirms all expected cards are declared
   before writing begins; the ORTHOGONALITY TABLE gate confirms the manifest count matches
   the table row count.

3. **VERIFY-MAP CITATION verbatim in Diagnosis Cards** — Each expert Diagnosis Card currently
   records "VERIFY-MAP check: Chain E confirmed" as a status assertion. But the Diagnosis Card
   does not reproduce the VERIFY-MAP's "Interrogates gap because" text verbatim, meaning the
   Chain E transit is attested by status only (not by content). A VERIFY-MAP CITATION block in
   each expert Diagnosis Card — reproducing the source gap, verify focus, and "Interrogates
   gap because" text verbatim from the Phase 2 VERIFY-MAP — makes the Chain E transit fully
   auditable at the card level, parallel to how Diagnosis Cards reproduce inertia gap verbatim
   for Chain A.

---

## Round 14 Variation Map

| V | Axis | Primary new pattern | Hypothesis |
|---|------|---------------------|------------|
| V-01 | lifecycle emphasis | SIMPLIFY-VOCABULARY ANCHOR — simplify_rule domain terms must trace to GAP-{slug} Domain vocabulary; VOCABULARY TRACE citation per rule; Chain G in PROVENANCE-CHAIN DECLARATION | C-54 tests that a named domain term is present; V-01 tests that the term derives from Phase 2 gap vocabulary — if vocabulary provenance is structurally distinct from term presence, a new C-56 criterion emerges |
| V-02 | output format | ROLE-MANIFEST forward declaration — after PREPARE, before first Diagnosis Card, enumerate all expected cards by name/type/source; GATE confirms declared count before writing begins | ORTHOGONALITY TABLE is post-hoc completeness checking; ROLE-MANIFEST is pre-writing forward declaration — if forward declaration of the expected card set is structurally distinct from post-hoc table verification, a new C-56 criterion emerges |
| V-03 | phrasing register | VERIFY-MAP CITATION verbatim in Diagnosis Cards — each expert card reproduces source gap, verify focus, and "Interrogates gap because" text from Phase 2 VERIFY-MAP verbatim, not just Chain E status | Chain E transit is currently status-attested ("confirmed") rather than content-reproduced; V-03 requires verbatim reproduction parallel to how Chain A transit reproduces inertia gap verbatim — if content-level transit auditing is distinct from status-level attestation, a new C-56 criterion emerges |
| V-04 | V-01+V-02 combined | SIMPLIFY-VOCABULARY ANCHOR + ROLE-MANIFEST | Both pre-writing gate artifacts: vocabulary provenance and forward card manifest |
| V-05 | V-01+V-02+V-03 combined | All three + role sequence unchanged (anchor → stock → experts) | Full combined: vocabulary provenance, forward manifest, and verbatim Chain E transit citation |

---

## V-01 — Single-Axis: SIMPLIFY-VOCABULARY ANCHOR

**axis:** lifecycle emphasis
**hypothesis:** R13 V-05 satisfies C-54 by requiring each simplify_rule to contain at least
one named domain artifact, mechanism, field name, or vocabulary term (SIMPLIFY-DOMAIN
REQUIREMENT in [FC-5], per-role SIMPLIFY-DOMAIN CHECK before YAML). But no provenance
obligation governs where the named term comes from. A rule like "Skip state-machine
transitions unless async boundaries apply" satisfies C-54 if this domain has state machines,
even if "state-machine transitions" appears nowhere in Phase 2 INERTIA-GAP ANALYSIS. This
variate adds a SIMPLIFY-VOCABULARY ANCHOR step inside the SIMPLIFY-DOMAIN CHECK: each rule's
named domain term must trace to a specific GAP-{slug} Domain vocabulary entry via a
VOCABULARY TRACE citation. The citation is written per rule as: "term '{term}' from
GAP-{slug} Domain: {vocabulary-source}". Chain G in the PROVENANCE-CHAIN DECLARATION
formalizes this: Source = Phase 2 INERTIA-GAP ANALYSIS Domain vocabularies; Transit =
SIMPLIFY-DOMAIN CHECK VOCABULARY TRACE; Destination = simplify_rules named terms in YAML.
Falsifiable: if the evaluator treats VOCABULARY TRACE as a restatement of what POSITIVE
SOURCING already does for names (gap vocabulary → role names) applied to a different field,
no new criterion emerges and V-01 equals R13 V-05 under v13. If vocabulary provenance for
simplify_rules is structurally distinct from term presence (C-54) — requiring a named chain
back to Phase 2 rather than merely a domain-sounding word — a new C-56 criterion emerges.

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
          SIMPLIFY-DOMAIN REQUIREMENT: each simplify_rule must contain at least one
            named domain artifact, mechanism, field name, or vocabulary term specific
            to this domain — generic exclusion terms alone fail this requirement
          SIMPLIFY-VOCABULARY ANCHOR (new): each named domain term must trace to a
            GAP-{slug} Domain vocabulary entry from Phase 2 INERTIA-GAP ANALYSIS;
            cite via VOCABULARY TRACE: "term '{term}' from GAP-{slug} Domain: {source}"
          BAD: "Skip obvious things" (no domain term)
          BAD-ANCHOR: "Skip retry loops" where "retry loops" does not appear in any
            GAP-{slug} Domain vocabulary (named term, no provenance)
          GOOD: "Skip {domain-term} handling unless {condition}" where {domain-term}
            cites a GAP-{slug} Domain vocabulary entry

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
    Integrity:   copy verbatim; cite GAP-{slug} by name; positional reference breaks A

  Chain B — Orthogonality provenance:
    Source:      Phase 5 CROSS-CARD UNIQUENESS SCAN + ANCHOR-CARD primary question
    Transit:     Phase 5 Diagnosis Card — field: Orthogonality to ANCHOR-CARD
    Destination: Phase 5 YAML role file — field: orthogonality [FC-11]
    Integrity:   copy verbatim from Diagnosis Card to YAML; named contrast axis required;
      generic assertion breaks B

  Chain C — Inertia surface provenance:
    Source:      Phase 1 INERTIA-SURFACE — field: Status-quo claim
    Transit:     Phase 5 ANCHOR-CARD Frame — rephrased as epistemic stance
    Destination: Phase 6 REGISTRY.md — field: inertia_surface
    Integrity:   inertia_surface uses exact words of Status-quo claim; fulfills
      EXTENSION-COMMITMENT

  Chain D — Anchor name provenance:
    Source:      Phase 1 INERTIA-SURFACE — Status-quo claim vocabulary
    Transit:     Phase 5 ANCHOR-CARD Diagnosis Card — ANCHOR-SOURCING statement
    Destination: Phase 5 ANCHOR-CARD YAML — field: name
    Integrity:   anchor name contains term traceable to INERTIA-SURFACE vocabulary;
      generic anchor name breaks D

  Chain E — Verify-question-to-gap traceability:
    Source:      Phase 2 INERTIA-GAP ANALYSIS — field: GAP-{slug}.Failure mode
    Transit:     Phase 2 VERIFY-MAP — field: Interrogates gap because
    Destination: Phase 5 YAML role file — field: lens.verify_questions[0]
    Integrity:   primary verify_question interrogates GAP Failure mode; disconnected
      verify focus breaks E; shared vocabulary without interrogating failure mode breaks E

  Chain F — Challenge coverage:
    Source:      Phase 1 INERTIA-SURFACE — Challenge questions
    Transit:     Phase 5 CHALLENGE-COVERAGE MAP — coverage mapping rows
    Destination: Phase 5 ANCHOR-CARD YAML — field: lens.verify_questions
    Integrity:   all Phase 1 challenge questions represented; uncovered questions
      added before MAP closes; unresolved question breaks F

  Chain G — Simplify-rule vocabulary provenance (new):
    Source:      Phase 2 INERTIA-GAP ANALYSIS — field: GAP-{slug}.Domain vocabulary
    Transit:     Phase 5 SIMPLIFY-DOMAIN CHECK — VOCABULARY TRACE per rule
    Destination: Phase 5 YAML role file — field: lens.simplify_rules named terms
    Integrity:   each named domain term in a simplify_rule traces to a GAP-{slug}
      Domain vocabulary entry via VOCABULARY TRACE citation; domain-sounding term
      with no provenance citation breaks G
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT written with all three elements [C-23/C-30]
2. FIELD-CONTRACT [FC-1] through [FC-12] written [C-26]
3. [FC-1]: PROHIBITED NAMES + POSITIVE SOURCING REQUIRED + ANCHOR-SOURCING REQUIRED [C-28/C-31]
4. [FC-4] and [FC-5] EXACT IDENTIFIER labels displayed [C-24/C-07]
5. [FC-5] SIMPLIFY-DOMAIN REQUIREMENT + SIMPLIFY-VOCABULARY ANCHOR with BAD/BAD-ANCHOR/GOOD
   examples present [C-54/new]
6. [FC-10] CONTRACT VIOLATION (type 1) and (type 2) labels present [C-29]
7. [FC-11] REQUIRED FORMAT + YAML persistence stated [C-46]
8. [FC-12] REQUIRED FORMAT + positional failure stated + YAML persistence stated [C-47]
9. PROVENANCE-CHAIN DECLARATION written with all seven chains (A through G); each chain
   names Source, Transit, Destination, and Integrity rule [C-52/new]

---

PHASE 1 — INERTIA SURFACE

Read `{topic}` context. Write an INERTIA-SURFACE block:

```
INERTIA-SURFACE for {topic}:

  Status-quo claim: [the strongest argument that {topic} is unnecessary — grounded
    in context; name the specific existing capability relied upon]

  Challenge questions (at minimum three; each uses vocabulary from `{topic}` context):
    Q1: What specific failure does the status quo produce that this feature resolves?
    Q2: [what does the existing mechanism already handle?]
    Q3: [what is the minimum status-quo fix, and why is it insufficient?]
```

Do not name domain experts in Phase 1.
Status-quo claim is Chain C + D source. Note specific vocabulary terms for anchor name.
Challenge questions are Chain F source — CHALLENGE-COVERAGE MAP will verify coverage.

**GATE** — Phase 1 complete when ALL of the following are TRUE:
1. INERTIA-SURFACE written with status-quo claim naming a specific capability [C-02]
2. At least three challenge questions using `{topic}` vocabulary
3. No domain expert names appear [C-39 precondition]

---

PHASE 2 — DOMAIN ANALYSIS (gap-first, with verify-question traceability)

**Step 1 — INERTIA-GAP ANALYSIS** (before any expert naming):

```
INERTIA-GAP ANALYSIS for {topic}:

  GAP-{domain-slug-1}:
    Domain: [named vocabulary domain for this gap]
    Failure mode: [specific failure the status quo cannot prevent]
    Inertia resistance: [what the Phase 1 inertia claim overlooks from this domain]

  GAP-{domain-slug-2}: ...
  GAP-{domain-slug-3}: ...
  (minimum three; GAP-{slug} identifier derives from Domain vocabulary)
```

**Step 2 — EXPERT DERIVATION** (POSITIVE SOURCING per expert; no stock roles):

```
DOMAIN-ANALYSIS for {topic}:

  Domain experts derived from INERTIA-GAP ANALYSIS:
    - Expert name: [slug from GAP-{slug} Domain vocabulary]
      POSITIVE SOURCING: "this name derives from GAP-{slug} Domain vocabulary:
        [specific term from that vocabulary used in the name]"
      Named gap source: GAP-{slug}
      Inertia gap: [GAP-{slug} inertia resistance — copied verbatim]
      Domain-vocabulary frame: [per [FC-2] using GAP-{slug} vocabulary]
      Verify focus: [what artifact or behavior this expert checks first]
```

**Step 3 — VERIFY-MAP** (Chain E transit; resolve all FLAGs before Phase 3):

```
VERIFY-MAP for /org-roles {topic}:

  For each domain expert from DOMAIN-ANALYSIS:

    Expert: {expert-name}
      Source gap: GAP-{slug}
      Verify focus (from DOMAIN-ANALYSIS): [text from Verify focus field]
      Interrogates gap because: [explicit connection between verify focus and
        GAP-{slug} Failure mode — name the failure mode; state why the verify focus
        surfaces or prevents that failure]
      Chain E status: PASS | FLAG
        (FLAG: verify focus does not interrogate GAP-{slug} Failure mode by name;
         PASS: verify focus interrogates GAP-{slug} Failure mode by name)
```

Resolve all FLAGs before proceeding. A flagged entry must be rewritten with revised focus
and reason it now interrogates the GAP Failure mode.
VERIFY-MAP is the Chain E transit artifact — produced in Phase 2, consumed in Phase 5.

**GATE** — Phase 2 complete when ALL of the following are TRUE:
1. INERTIA-GAP ANALYSIS before DOMAIN-ANALYSIS; at least three GAP-{slug} entries; all
   fields (Domain, Failure mode, Inertia resistance) present per entry [C-39/C-44]
2. GAP-{slug} identifiers derive from their Domain vocabularies [C-44]
3. Each derived expert includes all five attributes with POSITIVE SOURCING statement [C-45]
4. POSITIVE SOURCING cites specific GAP-{slug} and domain vocabulary term [C-45/C-40]
5. No placeholder or stock role names [C-28/C-31] — checkpoint 2 of 3
6. VERIFY-MAP written for all domain experts; all Chain E statuses PASS;
   all FLAGs resolved before this GATE confirmed [C-53]

---

PHASE 3 — STOCK ROLES

```
STOCK-ROLES:
  - inertia-advocate  (ANCHOR-CARD; frame from Phase 1 status-quo claim; written FIRST
                       in Phase 5; carries anchor: true; CHALLENGE-COVERAGE MAP written
                       after ANCHOR-CARD Diagnosis Card before subsequent cards)
  - pm                (product value and user outcome lens)
  - architect         (technical structure and system boundary lens)
  - strategy          (business model and competitive position lens)
```

All non-anchor roles carry `orthogonality` per [FC-11] (Chain B destination).
Domain expert roles carry `inertia_gap_inherited` per [FC-12] (Chain A destination).

**WRITE ORDER NOTE:** In Phase 5, YAML files are written: inertia-advocate (ANCHOR-CARD)
first, then stock roles (pm, architect, strategy), then domain experts.

**GATE** — Phase 3 complete when [C-03/C-37/C-46/C-47] confirmed; write order noted.

---

PHASE 4 — OUTPUT AREA

```
OUTPUT-AREA: .craft/roles/{area}/
```

Area slug uses Phase 2 GAP-{slug} Domain vocabulary. NOT: `default`, `generic`, `roles`.

**GATE** — Phase 4 complete when [C-04] confirmed.

---

PHASE 5 — DIAGNOSIS CARDS, CHALLENGE-COVERAGE MAP, SIMPLIFY-DOMAIN CHECK, ROLE FILES

**PREPARE:** Confirm all inputs before writing any Diagnosis Card:
- Phase 0 [FC-4] exact identifier: `verify_questions` (retrieve verbatim) [C-07/C-24]
- Phase 0 [FC-5] exact identifier: `simplify_rules` (retrieve verbatim) [C-07/C-24]
- Phase 0 [FC-5] SIMPLIFY-VOCABULARY ANCHOR requirement confirmed [new/C-54]
- Phase 0 [FC-11] REQUIRED FORMAT for `orthogonality` (retrieve verbatim) [C-46]
- Phase 0 [FC-12] REQUIRED FORMAT for `inertia_gap_inherited` (retrieve verbatim) [C-47]
- Phase 0 PROVENANCE-CHAIN DECLARATION: all seven chains (A-G) confirmed [C-52/new]
- Phase 1 INERTIA-SURFACE: status-quo claim and challenge questions confirmed [C-02/Chain F]
- Phase 2 INERTIA-GAP ANALYSIS: all GAP-{slug} entries with Domain vocabularies confirmed [C-39/C-44]
- Phase 2 DOMAIN-ANALYSIS: expert names with POSITIVE SOURCING confirmed [C-40/C-45]
- Phase 2 VERIFY-MAP: all experts PASS Chain E status confirmed [C-53]
- Phase 3 STOCK-ROLES: four names; inertia-advocate ANCHOR-CARD confirmed; write order noted [C-03/C-37]
- Phase 4 OUTPUT-AREA path confirmed [C-04]

PREPARE complete when all twelve inputs confirmed. Do not begin Diagnosis Cards until confirmed.

**ANCHOR-CARD (write first):**

```
ANCHOR-CARD for inertia-advocate:

  name: {term from Phase 1 INERTIA-SURFACE status-quo claim vocabulary}
  ANCHOR-SOURCING: "this name derives from INERTIA-SURFACE: [specific term from
    status-quo claim vocabulary used in this name]" — Chain D transit
  [FC-1] name check: traces to INERTIA-SURFACE vocabulary; NOT placeholder; confirmed

  frame (one sentence): {Phase 1 status-quo claim as epistemic stance — Chain C transit}
  serves (one sentence): {beneficiary — NOT a frame restatement}

  primary_verify_question: {most adversarial "why is the status quo sufficient?" —
    Chain B source; Phase 5 scan reference axis}
  verify_questions planned: [{all planned verify_questions for ANCHOR-CARD — used in
    CHALLENGE-COVERAGE MAP below}]
  uniqueness argument: uniquely attributable to inertia-advocate because [reason]; confirmed
  anchor status: ANCHOR-CARD

  collaborates_with draft: [{names}]; phantom check: confirmed

  SIMPLIFY-DOMAIN PLAN:
    Rule 1: [planned text] — domain term: [{term}] — PASS/FLAG
    (one entry per planned simplify_rule; resolve FLAGs before YAML)
```

**CHALLENGE-COVERAGE MAP (immediately after ANCHOR-CARD; before all other Diagnosis Cards):**

```
CHALLENGE-COVERAGE MAP for /org-roles {topic}:

  Phase 1 challenge questions (complete list from INERTIA-SURFACE):
    Q1: [verbatim]
    Q2: [verbatim]
    Q3: [verbatim]
    (all challenge questions — copy verbatim from Phase 1)

  Coverage mapping:
  | Phase 1 Challenge Question | In ANCHOR-CARD verify_questions? | Evidence |
  |----------------------------|----------------------------------|----------|
  | Q1 | YES/NO | [covering question text or "absent"] |
  | Q2 | YES/NO | [evidence] |
  | Q3 | YES/NO | [evidence] |

  Covered: {count YES}; Uncovered: {count NO}

  CHALLENGE-COVERAGE GATE:
    - [ ] Every Phase 1 challenge question appears in this table [new/Chain F]
    - [ ] All rows YES, or add missing question to anchor verify_questions before closing

Chain F transit confirmed. Proceed to subsequent Diagnosis Cards.
```

**SUBSEQUENT DIAGNOSIS CARDS (after CHALLENGE-COVERAGE MAP):**

```
DIAGNOSIS-CARD for {role-name}:

  name: {for domain experts: from GAP-{slug} Domain vocabulary with POSITIVE SOURCING
         confirmed; for stock roles: standard name; confirmed against [FC-1]}
  [FC-1] name check: [experts: GAP-{slug} trace and term; stock: standard]; confirmed

  frame (one sentence): {for domain experts: from GAP-{slug} vocabulary per [FC-2];
    for stock roles: standard lens}
  serves (one sentence): {beneficiary — NOT a frame restatement per [FC-3]}

  inertia gap inherited: {for domain experts: "GAP-{slug}: [inertia resistance copied
    verbatim]" — Chain A transit; for stock roles: N/A}
  orthogonality to ANCHOR-CARD: {per [FC-11] REQUIRED FORMAT — Chain B transit —
    named contrast axis; copy verbatim to YAML orthogonality field}

  primary_verify_question: {most role-specific question for this frame}
  VERIFY-MAP check (domain experts only): confirm primary_verify_question interrogates
    GAP-{slug} Failure mode per Phase 2 VERIFY-MAP — Chain E consumed here [C-53]
  uniqueness argument: [reason]; confirmed distinct

  collaborates_with draft: [{names}]; phantom check: confirmed

  SIMPLIFY-DOMAIN PLAN:
    Rule 1: [planned text] — domain term: [{term}] — PASS/FLAG
    (resolve all FLAGs before YAML)
```

After all Diagnosis Cards, produce **ORTHOGONALITY COMPLETENESS TABLE**:

```
ORTHOGONALITY COMPLETENESS TABLE for /org-roles {topic}:

  ANCHOR primary question: "[anchor's primary_verify_question from Diagnosis Card]"

  Non-anchor roles:
  | Role | Named contrast axis | Axis distinct from anchor | Axis distinct from all prior rows | Status |
  |------|---------------------|---------------------------|-----------------------------------|--------|
  | {role-1} | {axis text} | YES/NO | N/A (first row) | PASS/FLAG |
  | {role-2} | {axis text} | YES/NO | YES/NO          | PASS/FLAG |

  ORTHOGONALITY COMPLETENESS GATE:
  - [ ] Every non-anchor role appears in table [C-35]
  - [ ] Every contrast axis names the ANCHOR primary question scope [C-35]
  - [ ] No two non-anchor roles share the same named contrast axis [C-35]
  - [ ] All rows PASS

TABLE complete when all rows filled and GATE confirmed. Do not run scan until complete.
```

After TABLE, run **CROSS-CARD UNIQUENESS SCAN**:

```
CROSS-CARD UNIQUENESS SCAN (ANCHOR-CARD as reference axis):

  Phase 1 — Enumerate All Verify Questions:
    List every primary_verify_question from every Diagnosis Card (ANCHOR-CARD first).
    Format: [role-name]: "[question text]"
    Scope: enumeration only — no checking, no flagging in this phase.

  Phase 2 — Anchor-Orthogonality Check:
    State ANCHOR primary question. For each non-anchor role: test whether its question
    and the anchor question could be asked by the same role. Mark PASS or FLAG.
    Resolve all flags before Phase 3.

  Phase 3 — Non-Anchor Pairwise Check:
    For each pair of non-anchor roles: compare primary_verify_questions.
    Flag any pair where both questions serve the same epistemic purpose.
    Record PASS or FLAG per pair. Do not begin Phase 4 until Phase 3 records written.

  Phase 4 — Revision and Resolution:
    Collect all flags from Phase 2 and Phase 3. Rewrite flagged questions; record reason
    each revision now achieves distinctness. Do not write any YAML until Phase 4 complete.
```

**SCAN ORDERING GATE** — confirm before writing any YAML:
- [ ] CHALLENGE-COVERAGE MAP complete; all questions covered [C-55/Chain F]
- [ ] ORTHOGONALITY COMPLETENESS TABLE complete; all rows PASS [C-35]
- [ ] Phase 1 (Enumerate) executed first; no checking in Phase 1 [C-42]
- [ ] Phase 2 (Anchor-Orthogonality) after Phase 1 complete; before Phase 3 [C-50]
- [ ] Phase 3 (Non-Anchor Pairwise) after Phase 2 complete; before Phase 4 [C-50]
- [ ] Phase 4 (Revision) executed last; flags from Phase 2 AND Phase 3 collected [C-43]
- [ ] No phases merged; canonical sequence: CCM → Table → P1 → P2 → P3 → P4 [C-48]

**WRITE:** YAML files in order: inertia-advocate (ANCHOR-CARD) first, then stock roles
(pm, architect, strategy), then domain experts.

**SIMPLIFY-DOMAIN CHECK with VOCABULARY ANCHOR** — before each role's YAML (in write
order: anchor → stock → experts):

```
SIMPLIFY-DOMAIN CHECK for {role-name}:

  Planned simplify_rules (from Diagnosis Card SIMPLIFY-DOMAIN PLAN):
    Rule 1: "{rule text}"
      Named domain term: [{term}]
      VOCABULARY TRACE (new): "term '{term}' from GAP-{slug} Domain: {vocabulary-source}"
        (cite the specific GAP-{slug} whose Domain vocabulary contains this term;
         if term appears in multiple gaps, cite the primary sourcing gap)
      Domain term present: PASS | FLAG
      Vocabulary provenance confirmed: PASS | FLAG
        (FLAG if term does not appear in any GAP-{slug} Domain vocabulary)
    Rule N: "{text}" — term: [{term}] — trace: [{GAP-{slug}}] — PASS/FLAG

  SIMPLIFY-DOMAIN GATE:
    - [ ] All rules contain a named domain term [C-54/FC-5 SIMPLIFY-DOMAIN REQUIREMENT]
    - [ ] All named terms trace to a GAP-{slug} Domain vocabulary entry [new/FC-5
          SIMPLIFY-VOCABULARY ANCHOR]
    - [ ] No rule relies solely on generic exclusion language [FC-5]

Resolve all FLAGs before writing YAML. Do not proceed to YAML until gate confirmed.
```

```yaml
---
name: {per Diagnosis Card — [FC-1] positive/anchor sourcing confirmed}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

anchor: true   # ANCHOR-CARD only; omit from all other roles

orthogonality: "{Chain B — per [FC-11] REQUIRED FORMAT; verbatim from TABLE contrast
  axis; named; not generic}"   # non-anchor roles only; omit from ANCHOR-CARD

inertia_gap_inherited: "{Chain A — GAP-{slug}: [verbatim inertia resistance];
  not positional}"   # domain expert roles only; omit from stock and anchor

orientation:
  frame: |
    {Per [FC-2]. FAILURE MODE: task-list frame.}
  serves: |
    {Per [FC-3]. NOT a frame restatement.}

lens:
  verify_questions:
    - "{Primary — Chain E dest (experts): interrogates GAP Failure mode per VERIFY-MAP;
       Chain F dest (anchor): covers Phase 1 challenge question}"
    - "{Additional per [FC-4] minimum two}"
  simplify_rules:
    - "{Per [FC-5] SIMPLIFY-DOMAIN REQUIREMENT + VOCABULARY ANCHOR:
       named domain term present; term traces to GAP-{slug} Domain vocabulary}"

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
  # CONTRACT VIOLATION (type 1) — PHANTOM: a role name absent from this registry [C-29]
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent [C-29]
```

Checklist before writing each file [C-51: each item names its governing criterion]:
- [ ] `verify_questions` spelled exactly as in [FC-4] EXACT IDENTIFIER [C-07/FC-4]
- [ ] `simplify_rules` spelled exactly as in [FC-5] EXACT IDENTIFIER [C-07/FC-5]
- [ ] `orthogonality` present per [FC-11] for all non-anchor roles; absent from ANCHOR-CARD [C-46]
- [ ] `orthogonality` value matches ORTHOGONALITY TABLE contrast axis verbatim [C-35]
- [ ] `inertia_gap_inherited` present per [FC-12] for domain experts; absent from stock/anchor [C-47]
- [ ] `anchor: true` in inertia-advocate file only [C-37]
- [ ] No PHANTOM names — CONTRACT VIOLATION (type 1) [C-29/C-33]
- [ ] No UNIVERSALIST listing — CONTRACT VIOLATION (type 2) [C-29/C-33]
- [ ] ANCHOR-CARD verify_questions cover all Phase 1 challenge questions [C-55/Chain F]
- [ ] Domain expert verify_questions[0] interrogates GAP Failure mode per VERIFY-MAP [C-53/Chain E]
- [ ] All simplify_rules contain named domain terms [C-54/FC-5]
- [ ] All simplify_rule domain terms trace to GAP-{slug} Domain vocabulary [new/Chain G]
- [ ] Write order confirmed: anchor → stock → experts [C-37]

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. ANCHOR-CARD Diagnosis Card written first; CHALLENGE-COVERAGE MAP written immediately
   after; all subsequent cards written after MAP [C-37/C-55]
2. All non-anchor Diagnosis Cards include `orthogonality to ANCHOR-CARD` per [FC-11] [C-35]
3. All domain expert Diagnosis Cards include `inertia gap inherited` citing GAP-{slug} [C-41]
4. VERIFY-MAP consulted per expert Diagnosis Card; Chain E status confirmed [C-53]
5. SIMPLIFY-DOMAIN CHECK with VOCABULARY TRACE run per role (write order: anchor → stock →
   experts); all domain terms present and all vocabulary traces confirmed PASS [C-54/new]
6. ORTHOGONALITY COMPLETENESS TABLE complete; all rows PASS before scan [C-35]
7. CROSS-CARD UNIQUENESS SCAN: all four phases run; SCAN ORDERING GATE confirmed
   (seven items) [C-42/C-43/C-48/C-50]
8. YAML written: anchor first, then stock, then experts [C-37]
9. ANCHOR-CARD YAML: `anchor: true`; NO `orthogonality`; NO `inertia_gap_inherited` [C-37]
10. Non-anchor YAML: `orthogonality` per [FC-11] REQUIRED FORMAT; not generic [C-46]
11. Domain expert YAML: `inertia_gap_inherited` per [FC-12] citing GAP-{slug} verbatim [C-47]
12. All YAML files use exact identifiers `verify_questions` and `simplify_rules` [C-07]
13. No prohibited names; no collaborates_with CONTRACT VIOLATION; labels mirrored [C-28/C-29/C-33]
14. Chains A-G each traceable through transit artifacts to YAML destinations [C-52/new]
15. Per-file checklist items carry criterion-ID annotations [C-51]

---

PHASE 6 — REGISTRY SUMMARY

**COVERAGE-GATE** — before writing REGISTRY.md:

```
COVERAGE-GATE for /org-roles {topic}:

  Walk each GAP-{slug} from Phase 2 INERTIA-GAP ANALYSIS:

    GAP-{slug-1}:
      Expert derived: {name from Phase 2, or "none"}
      Expert file written in Phase 5: {filename, or "none written"}
      Coverage status: COVERED | GAP

    GAP-{slug-2}: ...

  Coverage summary:
    Covered gaps: {count} — {GAP-{slug} list}
    Uncovered gaps: {count} — {list or "none"}
```

COVERAGE-GATE complete when all Phase 2 gaps enumerated. Do not write REGISTRY.md until
COVERAGE-GATE complete.

**PREPARE:** Enumerate `.md` files written in Phase 5; record as `PHASE5_COUNT`.
Count from Phase 5 enumeration only — not from prior-phase planned counts.

**WRITE:** `.craft/roles/{area}/REGISTRY.md`:

```
---
area: {Phase 2 GAP Domain vocabulary}
generated: {date}
---

## Registry Summary

total_roles: {PHASE5_COUNT — from Phase 5 enumeration}

stock_roles:
  - inertia-advocate  (ANCHOR-CARD — derived Phase 1; written first in Phase 5)
  - pm
  - architect
  - strategy

domain_experts:
  - name: {expert-name}
    gap_source: GAP-{slug}
    inertia_gap: {verbatim inertia resistance}

coverage_gaps: |
  {from COVERAGE-GATE Uncovered gaps — not from memory; or "none detected"}

inertia_surface: |
  {Phase 1 status-quo claim verbatim — Chain C destination}

Generated by: /org-roles {topic} — {date}
```

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. COVERAGE-GATE written; every Phase 2 GAP-{slug} enumerated [C-10/C-22 parallel]
2. `coverage_gaps` from COVERAGE-GATE Uncovered gaps — not memory
3. `REGISTRY.md` at `.craft/roles/{area}/REGISTRY.md` [C-04]
4. `total_roles` equals `PHASE5_COUNT` from Phase 5 [C-22/C-27]
5. `domain_experts` lists each expert with `name`, `gap_source`, `inertia_gap` verbatim [C-10]
6. `inertia_surface` contains Phase 1 claim verbatim — Chain C verified [C-20/C-23]
7. No heading stubs [C-15]
8. Chains A-G traceable [C-52/new]

---

**Final checklist — confirm before declaring done:**

Simplify vocabulary provenance (new/Chain G): SIMPLIFY-DOMAIN CHECK with VOCABULARY TRACE
run per role in write order; all simplify_rule domain terms trace to GAP-{slug} Domain
vocabulary; Chain G confirmed from Phase 2 → SIMPLIFY-DOMAIN CHECK → YAML simplify_rules

Challenge coverage (C-55/Chain F): CHALLENGE-COVERAGE MAP after ANCHOR-CARD; every Phase 1
challenge question mapped and represented; Chain F confirmed

Verify-question traceability (C-53/Chain E): VERIFY-MAP in Phase 2; all experts PASS;
primary verify_questions interrogate GAP Failure modes

Scan structure (C-42/C-43/C-48/C-50): CROSS-CARD UNIQUENESS SCAN four phases; SCAN
ORDERING GATE confirmed (seven items); Phase 4 before any YAML

Orthogonality completeness (C-35): TABLE after all Diagnosis Cards; distinct axes; all PASS

Phase output (C-37/C-46/C-47): anchor `anchor: true`; non-anchor `orthogonality` from TABLE;
expert `inertia_gap_inherited` verbatim

Provenance chains (C-52): seven chains declared (A-G); all traceable

Gap/sourcing (C-39/C-44/C-40/C-45): INERTIA-GAP ANALYSIS before naming; POSITIVE SOURCING
per expert; ANCHOR-SOURCING per anchor (Chain D)

Contract violations (C-29/C-33): labels in YAML template and per-file checklist

Pipeline criterion annotations (C-51): all gate items and checklist items carry [C-NN]

Coverage gate: COVERAGE-GATE enumerated every Phase 2 GAP-{slug}; `coverage_gaps`
populated from enumeration not memory

---

## V-02 — Single-Axis: ROLE-MANIFEST

**axis:** output format
**hypothesis:** R13 V-05 Phase 5 PREPARE confirms inputs from Phases 0-4 but does not
enumerate the expected set of Diagnosis Cards by name. The ORTHOGONALITY COMPLETENESS TABLE
provides a post-hoc completeness check (after all cards are written), verifying that every
non-anchor role has an entry. But a card could be omitted before the TABLE is produced and
only discovered then — the TABLE is corrective, not preventive. This variate adds a
ROLE-MANIFEST block written after PREPARE and before the first Diagnosis Card. The manifest
lists every expected card by name, type (anchor/stock/domain-expert), and source phase.
A MANIFEST GATE confirms the expected count and card names before any Diagnosis Card is
written. The ORTHOGONALITY TABLE gate subsequently confirms that the table row count matches
the ROLE-MANIFEST non-anchor count. This makes completeness a declared pre-writing invariant
rather than a post-hoc verification.
Falsifiable: if the evaluator treats ROLE-MANIFEST as a restatement of what PREPARE already
does (listing Phase 3 STOCK-ROLES and Phase 2 experts before writing begins), no new
criterion emerges. If forward declaration of the expected card set as a named manifest is
structurally distinct from PREPARE's input confirmation — because it enumerates every
expected card name in an artifact before writing, enabling the TABLE to verify against a
named source rather than an implicit "all non-anchor roles" clause — a new C-56 criterion
emerges.

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

  [FC-1]  name — domain-vocabulary slug; PROHIBITED: placeholder names
          Experts: POSITIVE SOURCING REQUIRED ("this name derives from GAP-{slug}: [term]")
          Anchor: ANCHOR-SOURCING REQUIRED ("this name derives from INERTIA-SURFACE: [term]")
          BAD: "domain-expert"; GOOD (expert): slug from GAP Domain vocabulary; GOOD (anchor):
            slug from INERTIA-SURFACE claim vocabulary

  [FC-2]  orientation.frame — epistemic viewpoint; FAILURE MODE: task list

  [FC-3]  orientation.serves — beneficiary; NOT a frame restatement

  [FC-4]  lens.verify_questions
          EXACT IDENTIFIER: verify_questions
          PROHIBITED: verify | questions | checks | verify_list
          minimum two items; uniqueness argument required

  [FC-5]  lens.simplify_rules
          EXACT IDENTIFIER: simplify_rules
          PROHIBITED: simplify | rules | constraints | guidelines
          minimum one item; opinionated exclusion — NOT a scope description
          SIMPLIFY-DOMAIN REQUIREMENT: each rule contains at least one named domain
            artifact, mechanism, field, or vocabulary term; generic terms alone fail

  [FC-6]  expertise.depth — enum: expert | practitioner | senior | principal

  [FC-7]  expertise.relevance — domain-specific; not a role-name restatement

  [FC-8]  scope.primary — main concern; one sentence

  [FC-9]  scope.boundary — explicit exclusion; one sentence

  [FC-10] collaborates_with — registry members only
          CONTRACT VIOLATION (type 1) — PHANTOM: absent from registry
          CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent

  [FC-11] orthogonality — non-anchor YAML only
          REQUIRED FORMAT: "[axis] — this role's lens diverges from ANCHOR-CARD because
            [specific reason naming anchor's question and how concern falls outside]"
          REQUIRED: in YAML file; not only in Diagnosis Card

  [FC-12] inertia_gap_inherited — domain expert YAML only
          REQUIRED FORMAT: "GAP-{slug}: [verbatim inertia resistance]"
          Positional reference ("Gap 1:") fails; REQUIRED: in YAML file
```

**PROVENANCE-CHAIN DECLARATION:**

```
PROVENANCE-CHAIN DECLARATION for /org-roles {topic}:

  Chain A — Inertia gap:
    Source: Phase 2 INERTIA-GAP ANALYSIS — GAP-{slug}.Inertia resistance
    Transit: Phase 5 Diagnosis Card — inertia gap inherited
    Destination: Phase 5 YAML — inertia_gap_inherited
    Integrity: verbatim; GAP-{slug} named; positional breaks A

  Chain B — Orthogonality:
    Source: Phase 5 SCAN + ANCHOR primary question
    Transit: Phase 5 Diagnosis Card — Orthogonality to ANCHOR-CARD
    Destination: Phase 5 YAML — orthogonality
    Integrity: verbatim; named contrast axis; generic breaks B

  Chain C — Inertia surface:
    Source: Phase 1 Status-quo claim
    Transit: Phase 5 ANCHOR-CARD Frame
    Destination: Phase 6 REGISTRY.md inertia_surface
    Integrity: exact words at destination; fulfills EXTENSION-COMMITMENT

  Chain D — Anchor name:
    Source: Phase 1 INERTIA-SURFACE vocabulary
    Transit: Phase 5 ANCHOR-CARD ANCHOR-SOURCING
    Destination: Phase 5 ANCHOR-CARD YAML name
    Integrity: term traceable to INERTIA-SURFACE; generic breaks D

  Chain E — Verify-question-to-gap:
    Source: Phase 2 INERTIA-GAP ANALYSIS — GAP-{slug}.Failure mode
    Transit: Phase 2 VERIFY-MAP — Interrogates gap because
    Destination: Phase 5 YAML — lens.verify_questions[0]
    Integrity: primary verify_question interrogates GAP Failure mode; disconnected breaks E

  Chain F — Challenge coverage:
    Source: Phase 1 INERTIA-SURFACE — Challenge questions
    Transit: Phase 5 CHALLENGE-COVERAGE MAP — coverage mapping rows
    Destination: Phase 5 ANCHOR-CARD YAML — lens.verify_questions
    Integrity: all challenge questions represented; unresolved breaks F
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT written [C-23/C-30]
2. FIELD-CONTRACT [FC-1]-[FC-12] written [C-26]
3. [FC-1]: PROHIBITED NAMES + POSITIVE SOURCING + ANCHOR-SOURCING clauses [C-28/C-31]
4. [FC-4]/[FC-5] EXACT IDENTIFIER labels [C-24/C-07]
5. [FC-5] SIMPLIFY-DOMAIN REQUIREMENT + BAD/GOOD examples [C-54]
6. [FC-10] CONTRACT VIOLATION (type 1) and (type 2) labels [C-29]
7. [FC-11] REQUIRED FORMAT + YAML persistence [C-46]
8. [FC-12] REQUIRED FORMAT + positional-reference failure + YAML persistence [C-47]
9. PROVENANCE-CHAIN DECLARATION with six chains (A-F); each with Source/Transit/
   Destination/Integrity rule [C-52]

---

PHASE 1 — INERTIA SURFACE

```
INERTIA-SURFACE for {topic}:
  Status-quo claim: [specific capability; Chain C + D vocabulary; note terms]
  Challenge questions (minimum three; {topic} vocabulary):
    Q1: [failure produced by status quo]
    Q2: [what existing mechanism handles]
    Q3: [minimum fix and why insufficient]
```

Chain C + D source. Challenge questions are Chain F source.

**GATE:** [C-02]; three questions; no expert names.

---

PHASE 2 — DOMAIN ANALYSIS (with VERIFY-MAP)

**Step 1 — INERTIA-GAP ANALYSIS** (before expert naming; minimum three GAP-{slug} entries):

```
INERTIA-GAP ANALYSIS for {topic}:
  GAP-{slug-1}: Domain: [...]; Failure mode: [...]; Inertia resistance: [...]
  GAP-{slug-2}: ...
  GAP-{slug-3}: ...
```

**Step 2 — EXPERT DERIVATION** (POSITIVE SOURCING per expert; no stock roles):

```
DOMAIN-ANALYSIS for {topic}:
  - Expert name: [slug from GAP-{slug} Domain vocabulary]
    POSITIVE SOURCING: "this name derives from GAP-{slug}: [term]"
    Named gap source: GAP-{slug}
    Inertia gap: [verbatim]
    Domain-vocabulary frame: [per [FC-2]]
    Verify focus: [first-check artifact]
```

**Step 3 — VERIFY-MAP** (Chain E transit; PASS/FLAG per expert; resolve before Phase 3):

```
VERIFY-MAP for /org-roles {topic}:
  {expert-name}:
    Source gap: GAP-{slug}
    Verify focus: [from DOMAIN-ANALYSIS]
    Interrogates gap because: [connection to GAP-{slug} Failure mode — name it]
    Chain E status: PASS | FLAG
```

**GATE:** [C-39/C-44/C-45/C-40/C-28/C-31]; VERIFY-MAP all PASS [C-53].

---

PHASE 3 — STOCK ROLES

```
STOCK-ROLES:
  - inertia-advocate  (ANCHOR-CARD; Phase 1 frame; written first; anchor: true;
                       CHALLENGE-COVERAGE MAP after ANCHOR-CARD Diagnosis Card)
  - pm; architect; strategy
```

Write order in Phase 5: anchor → stock (pm, architect, strategy) → domain experts.

**GATE:** [C-03/C-37/C-46/C-47] confirmed; write order noted.

---

PHASE 4 — OUTPUT AREA

```
OUTPUT-AREA: .craft/roles/{area}/
```

Area from Phase 2 GAP Domain vocabulary. NOT: `default`, `generic`, `roles`.

**GATE:** [C-04] confirmed.

---

PHASE 5 — DIAGNOSIS CARDS, ROLE-MANIFEST, CHALLENGE-COVERAGE MAP, SIMPLIFY-DOMAIN CHECK, ROLE FILES

**PREPARE:** Confirm twelve inputs (Phase 0 identifiers/formats/six chains; Phase 1
INERTIA-SURFACE challenge questions for Chain F; Phase 2 INERTIA-GAP + DOMAIN-ANALYSIS +
VERIFY-MAP all PASS; Phase 3 STOCK-ROLES + write order; Phase 4 OUTPUT-AREA).
[C-07/C-24/C-46/C-47/C-52/C-02/C-39/C-44/C-40/C-45/C-03/C-37/C-04]

PREPARE complete when all twelve confirmed.

**ROLE-MANIFEST (after PREPARE; before first Diagnosis Card; new):**

```
ROLE-MANIFEST for /org-roles {topic}:

  Expected Diagnosis Cards (from Phase 2 DOMAIN-ANALYSIS + Phase 3 STOCK-ROLES):

  | Card name | Type | Source phase |
  |-----------|------|-------------|
  | inertia-advocate | anchor/stock | Phase 3 |
  | pm | stock | Phase 3 |
  | architect | stock | Phase 3 |
  | strategy | stock | Phase 3 |
  | {expert-name-1} | domain-expert | Phase 2 / GAP-{slug} |
  | {expert-name-N} | domain-expert | Phase 2 / GAP-{slug} |

  Manifest totals:
    Anchor cards: 1
    Non-anchor stock: 3
    Domain experts: {count from Phase 2}
    Total expected: {sum}

  MANIFEST GATE:
    - [ ] All Phase 2 experts listed with their GAP-{slug} source [new]
    - [ ] All Phase 3 stock roles listed [new]
    - [ ] Total matches Phase 2 expert count + 4 stock roles [new]
    - [ ] No names absent from DOMAIN-ANALYSIS or STOCK-ROLES [new]

Manifest confirmed. Proceed to ANCHOR-CARD Diagnosis Card.
```

**ANCHOR-CARD (write first):**

```
ANCHOR-CARD for inertia-advocate:
  name: {INERTIA-SURFACE vocabulary; ANCHOR-SOURCING: "this name derives from
    INERTIA-SURFACE: [term]" — Chain D transit; [FC-1] confirmed}
  MANIFEST CHECK: card name matches ROLE-MANIFEST row 1 [new]
  frame: {Phase 1 status-quo claim — Chain C transit}
  serves: {beneficiary}
  primary_verify_question: {adversarial sufficiency — Chain B source; scan axis}
  verify_questions planned: [{all planned anchor verify_questions — for CCM}]
  uniqueness: confirmed distinct; anchor status: ANCHOR-CARD
  collaborates_with: [{registry names}]; phantom check: confirmed
  SIMPLIFY-DOMAIN PLAN: Rule N: [text] — domain term: [{term}] — PASS/FLAG
```

**CHALLENGE-COVERAGE MAP (immediately after ANCHOR-CARD; before all other Diagnosis Cards):**

```
CHALLENGE-COVERAGE MAP for /org-roles {topic}:
  Phase 1 challenge questions (complete list):
    Q1: [verbatim]; Q2: [verbatim]; Q3: [verbatim]
  Coverage mapping:
  | Phase 1 Challenge | In ANCHOR-CARD verify_questions? | Evidence |
  |-------------------|----------------------------------|----------|
  | Q1 | YES/NO | [covering question or "absent"] |
  | Q2/Q3 | YES/NO | [...] |
  Covered: {n}; Uncovered: {n}
  CHALLENGE-COVERAGE GATE:
    - [ ] Every Phase 1 question in table [C-55/Chain F]
    - [ ] All YES or add missing question before closing
Chain F transit confirmed.
```

**SUBSEQUENT DIAGNOSIS CARDS (after CHALLENGE-COVERAGE MAP):**

```
DIAGNOSIS-CARD for {role-name}:
  MANIFEST CHECK: card name matches ROLE-MANIFEST entry [new]
  name: {[FC-1] confirmed per type}
  frame / serves (per role type)
  inertia gap inherited: {"GAP-{slug}: [verbatim]" (experts) / N/A — Chain A transit}
  orthogonality to ANCHOR-CARD: {[FC-11] — Chain B transit — verbatim to YAML}
  primary_verify_question: {role-specific}
  VERIFY-MAP check (experts): Chain E confirmed [C-53]
  uniqueness: confirmed
  collaborates_with: [{registry names}]; phantom check: confirmed
  SIMPLIFY-DOMAIN PLAN: Rule N: [text] — domain term: [{term}] — PASS/FLAG
```

After all Diagnosis Cards, **ORTHOGONALITY COMPLETENESS TABLE** (same structure as V-01;
GATE adds: [ ] table row count matches ROLE-MANIFEST non-anchor count [new]).

After TABLE, **CROSS-CARD UNIQUENESS SCAN** (Phase 1 Enumerate → Phase 2
Anchor-Orthogonality → Phase 3 Non-Anchor Pairwise → Phase 4 Revision-Resolution).

**SCAN ORDERING GATE:**
- [ ] ROLE-MANIFEST confirmed; MANIFEST GATE closed [new]
- [ ] CHALLENGE-COVERAGE MAP complete; all questions covered [C-55/Chain F]
- [ ] ORTHOGONALITY TABLE complete; all rows PASS; row count matches manifest [C-35/new]
- [ ] Phase 1 first; no checking [C-42]
- [ ] Phase 2 after Phase 1; before Phase 3 [C-50]
- [ ] Phase 3 after Phase 2; before Phase 4 [C-50]
- [ ] Phase 4 last; flags from Phase 2 AND Phase 3 [C-43]
- [ ] No phases merged; canonical sequence [C-48]

**WRITE:** YAML in order: anchor → stock → experts.

**SIMPLIFY-DOMAIN CHECK** (before each role's YAML; same structure as R13 V-05):

```
SIMPLIFY-DOMAIN CHECK for {role-name}:
  Rule N: [{text}] — domain term: [{term}] — PASS | FLAG
  GATE:
    - [ ] All rules contain named domain terms [C-54/FC-5]
    - [ ] No generic-only exclusion [FC-5]
```

YAML template same as V-01 (without Chain G annotation on simplify_rules).

Checklist [C-51: criterion per item]:
- [ ] `verify_questions` exact [C-07/FC-4]
- [ ] `simplify_rules` exact [C-07/FC-5]
- [ ] `orthogonality` per [FC-11]; non-anchor only [C-46]; matches TABLE [C-35]
- [ ] `inertia_gap_inherited` per [FC-12]; experts only [C-47]
- [ ] `anchor: true`; anchor only [C-37]
- [ ] ANCHOR-CARD verify_questions cover all Phase 1 challenge questions [C-55/Chain F]
- [ ] Expert verify_questions[0] interrogates GAP Failure mode per VERIFY-MAP [C-53/Chain E]
- [ ] All simplify_rules contain named domain terms [C-54/FC-5]
- [ ] No PHANTOM [C-29/C-33]; no UNIVERSALIST [C-29/C-33]
- [ ] Card name matched against ROLE-MANIFEST [new]
- [ ] Write order: anchor → stock → experts [C-37]

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. ROLE-MANIFEST written; MANIFEST GATE closed [new]
2. ANCHOR-CARD first; CHALLENGE-COVERAGE MAP immediately after [C-37/C-55]
3. Each Diagnosis Card includes MANIFEST CHECK [new]
4. VERIFY-MAP consulted per expert Diagnosis Card; Chain E confirmed [C-53]
5. SIMPLIFY-DOMAIN CHECK per role; all gates confirmed [C-54]
6. ORTHOGONALITY TABLE complete; row count matches ROLE-MANIFEST non-anchor count [C-35/new]
7. SCAN four phases; SCAN ORDERING GATE confirmed (eight items) [C-42/C-43/C-48/C-50]
8. YAML written in order; correct per-role fields [C-37/C-46/C-47]
9. Chains A-F traceable [C-52]; criterion annotations on all items [C-51]

---

PHASE 6 — REGISTRY SUMMARY

(Identical structure to V-01 Phase 6. COVERAGE-GATE before REGISTRY.md; PHASE5_COUNT from
Phase 5 enumeration; REGISTRY.md fields as specified; GATE [C-04/C-22/C-27/C-10/C-20/C-23/C-15/C-52].)

**REGISTRY.md note:** `total_roles` must equal PHASE5_COUNT AND match ROLE-MANIFEST total.

---

**Final checklist — confirm before declaring done:**

ROLE-MANIFEST forward declaration (new): manifest written after PREPARE; every expected card
listed by name/type/source; MANIFEST GATE closed; each Diagnosis Card carries MANIFEST CHECK;
ORTHOGONALITY TABLE row count confirmed against manifest non-anchor count

Challenge coverage (C-55): CHALLENGE-COVERAGE MAP complete; all questions covered

Verify-question traceability (C-53): VERIFY-MAP in Phase 2; all PASS

Simplify-domain specificity (C-54): SIMPLIFY-DOMAIN CHECK per role; all named domain terms

Scan structure (C-42/C-43/C-48/C-50): four phases; ORDERING GATE (eight items); Phase 4 first

Phase output (C-37/C-46/C-47): correct fields per role type

Chains A-F declared and traceable (C-52)

---

## V-03 — Single-Axis: VERIFY-MAP CITATION in Diagnosis Cards

**axis:** phrasing register
**hypothesis:** R13 V-05 establishes Chain E through the Phase 2 VERIFY-MAP (which records
Source gap, Verify focus, Interrogates gap because, Chain E status per expert). In Phase 5,
each expert Diagnosis Card carries a "VERIFY-MAP check: Chain E confirmed" annotation. But
this is a status assertion, not content reproduction — the Diagnosis Card attests that Chain
E is satisfied without reproducing the Chain E transit content (the "Interrogates gap because"
text verbatim). Compare to Chain A: each expert Diagnosis Card reproduces the inertia gap
resistance verbatim ("GAP-{slug}: [resistance copied verbatim]"), making Chain A fully
auditable at the card level. Chain E lacks this parallel. This variate replaces the
"VERIFY-MAP check: Chain E confirmed" annotation in each expert Diagnosis Card with a
VERIFY-MAP CITATION block that reproduces the Phase 2 VERIFY-MAP entry's source gap,
verify focus, and "Interrogates gap because" text verbatim. The citation makes the Chain E
transit content-reproducible at the Diagnosis Card level, parallel to Chain A's verbatim
inertia-gap reproduction. The per-file checklist gains a new item requiring this citation.
Falsifiable: if the evaluator treats VERIFY-MAP CITATION as a mechanical restatement of
information the Diagnosis Card already carries in other fields (the primary_verify_question
and the VERIFY-MAP check status), no new criterion emerges. If verbatim content reproduction
at the Chain E transit level is structurally distinct from status attestation — because it
enables Chain E to be audited at the card level without consulting Phase 2 (parallel to how
Chain A verbatim reproduction enables Chain A to be audited without consulting Phase 2) — a
new C-56 criterion emerges.

---

You are running `/org-roles {topic}`.

---

PHASE 0 — FIELD CONTRACT, EXTENSION COMMITMENT, AND PROVENANCE CHAINS

**EXTENSION-COMMITMENT:** (identical to V-01)

```
EXTENSION-COMMITMENT:
  field_name: inertia_surface
  population_source: Phase 1, INERTIA-SURFACE block, status-quo claim field
  purpose: answers the Phase 0 diagnostic question — "what is the strongest
    existing-system argument that makes {topic} premature?"
```

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
          SIMPLIFY-DOMAIN REQUIREMENT: each rule contains at least one named domain
            artifact, mechanism, field, or vocabulary term; generic terms alone fail

  [FC-6]  expertise.depth — enum: expert | practitioner | senior | principal

  [FC-7]  expertise.relevance — domain-specific justification

  [FC-8]  scope.primary — one sentence

  [FC-9]  scope.boundary — explicit exclusion; one sentence

  [FC-10] collaborates_with — registry members only
          CONTRACT VIOLATION (type 1) — PHANTOM: absent from registry
          CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent

  [FC-11] orthogonality — non-anchor YAML only
          REQUIRED FORMAT: "[axis] — this role's lens diverges from ANCHOR-CARD because
            [specific reason naming anchor's question and how concern falls outside]"
          REQUIRED: in YAML file; not only in Diagnosis Card

  [FC-12] inertia_gap_inherited — domain expert YAML only
          REQUIRED FORMAT: "GAP-{slug}: [verbatim inertia resistance]"
          Positional reference fails; REQUIRED: in YAML file
```

**PROVENANCE-CHAIN DECLARATION:**

```
PROVENANCE-CHAIN DECLARATION for /org-roles {topic}:

  Chain A — Inertia gap:
    Source:      Phase 2 INERTIA-GAP ANALYSIS — GAP-{slug}.Inertia resistance
    Transit:     Phase 5 Diagnosis Card — inertia gap inherited (verbatim reproduction)
    Destination: Phase 5 YAML — inertia_gap_inherited
    Integrity:   verbatim at transit and destination; GAP-{slug} named; positional breaks A

  Chain B — Orthogonality:
    Source:      Phase 5 SCAN + ANCHOR primary question
    Transit:     Phase 5 Diagnosis Card — Orthogonality to ANCHOR-CARD
    Destination: Phase 5 YAML — orthogonality
    Integrity:   verbatim; named contrast axis; generic breaks B

  Chain C — Inertia surface:
    Source:      Phase 1 Status-quo claim
    Transit:     Phase 5 ANCHOR-CARD Frame
    Destination: Phase 6 REGISTRY.md inertia_surface
    Integrity:   exact words at destination; fulfills EXTENSION-COMMITMENT

  Chain D — Anchor name:
    Source:      Phase 1 INERTIA-SURFACE vocabulary
    Transit:     Phase 5 ANCHOR-CARD ANCHOR-SOURCING
    Destination: Phase 5 ANCHOR-CARD YAML name
    Integrity:   term traceable to INERTIA-SURFACE claim vocabulary

  Chain E — Verify-question-to-gap (content-reproduced transit):
    Source:      Phase 2 INERTIA-GAP ANALYSIS — GAP-{slug}.Failure mode
    Transit:     Phase 2 VERIFY-MAP — Interrogates gap because;
                 Phase 5 Diagnosis Card — VERIFY-MAP CITATION (verbatim reproduction)
    Destination: Phase 5 YAML — lens.verify_questions[0]
    Integrity:   primary verify_question interrogates GAP Failure mode;
      Diagnosis Card CITATION reproduces VERIFY-MAP "Interrogates gap because" text
      verbatim — status-only attestation ("Chain E confirmed") without reproduction
      is insufficient and breaks the transit audit trail

  Chain F — Challenge coverage:
    Source:      Phase 1 INERTIA-SURFACE — Challenge questions
    Transit:     Phase 5 CHALLENGE-COVERAGE MAP — coverage rows
    Destination: Phase 5 ANCHOR-CARD YAML — lens.verify_questions
    Integrity:   all questions represented; unresolved breaks F
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT written [C-23/C-30]
2. FIELD-CONTRACT [FC-1]-[FC-12] [C-26]
3. [FC-1] PROHIBITED NAMES + POSITIVE SOURCING + ANCHOR-SOURCING [C-28/C-31]
4. [FC-4]/[FC-5] EXACT IDENTIFIER labels [C-24/C-07]
5. [FC-5] SIMPLIFY-DOMAIN REQUIREMENT + BAD/GOOD examples [C-54]
6. [FC-10] CONTRACT VIOLATION labels [C-29]
7. [FC-11] REQUIRED FORMAT + YAML persistence [C-46]
8. [FC-12] REQUIRED FORMAT + positional failure + YAML persistence [C-47]
9. PROVENANCE-CHAIN DECLARATION six chains (A-F); Chain E explicitly describes two-transit
   path (VERIFY-MAP + Diagnosis Card CITATION); content-reproduction requirement stated [C-52/new]

---

PHASE 1 — INERTIA SURFACE

```
INERTIA-SURFACE for {topic}:
  Status-quo claim: [specific capability; Chain C + D source; note terms]
  Challenge questions (min three; {topic} vocabulary):
    Q1: [failure]; Q2: [existing handling]; Q3: [minimum fix + why insufficient]
```

Chain F source. **GATE:** [C-02]; three questions; no expert names.

---

PHASE 2 — DOMAIN ANALYSIS (with VERIFY-MAP)

**Step 1 — INERTIA-GAP ANALYSIS** (min three; GAP-{slug} from Domain vocabulary):

```
INERTIA-GAP ANALYSIS for {topic}:
  GAP-{slug-1}: Domain: [...]; Failure mode: [...]; Inertia resistance: [...]
  ...
```

**Step 2 — EXPERT DERIVATION** (POSITIVE SOURCING per expert):

```
DOMAIN-ANALYSIS for {topic}:
  - Expert name: [GAP vocabulary slug]
    POSITIVE SOURCING: "this name derives from GAP-{slug}: [term]"
    Named gap source: GAP-{slug}
    Inertia gap: [verbatim]
    Domain-vocabulary frame: [per [FC-2]]
    Verify focus: [first-check artifact]
```

**Step 3 — VERIFY-MAP** (Chain E first transit; PASS/FLAG; resolve before Phase 3):

```
VERIFY-MAP for /org-roles {topic}:
  {expert-name}:
    Source gap: GAP-{slug}
    Verify focus: [from DOMAIN-ANALYSIS]
    Interrogates gap because: [connection to GAP-{slug} Failure mode — name it]
      (this text is the Chain E first-transit content; copied verbatim to Diagnosis Card)
    Chain E status: PASS | FLAG
```

**GATE:** [C-39/C-44/C-45/C-40/C-28/C-31]; VERIFY-MAP all PASS [C-53].

---

PHASE 3, 4 — (identical to V-01)

---

PHASE 5 — DIAGNOSIS CARDS, CHALLENGE-COVERAGE MAP, SIMPLIFY-DOMAIN CHECK, ROLE FILES

**PREPARE:** Confirm twelve inputs (same as V-01 except Chain E PREPARE note):
- Phase 2 VERIFY-MAP: all PASS; "Interrogates gap because" text available for CITATION [C-53/new]
[All other inputs same as V-01.]

**ANCHOR-CARD (write first):** (same structure as V-01; no VERIFY-MAP CITATION needed for anchor)

**CHALLENGE-COVERAGE MAP:** (immediately after ANCHOR-CARD; identical to V-01)

**SUBSEQUENT DIAGNOSIS CARDS (after CCM) — modified for VERIFY-MAP CITATION:**

```
DIAGNOSIS-CARD for {role-name}:

  name: {[FC-1] confirmed per role type}
  frame / serves (per role type)
  inertia gap inherited: {"GAP-{slug}: [verbatim]" (experts) / N/A — Chain A transit}
  orthogonality to ANCHOR-CARD: {[FC-11] format — Chain B transit — verbatim to YAML}

  primary_verify_question: {role-specific question}
  uniqueness argument: [reason]; confirmed distinct

  VERIFY-MAP CITATION (domain experts only; replaces "VERIFY-MAP check: Chain E confirmed"):
    Source gap: GAP-{slug}  [from Phase 2 VERIFY-MAP entry for this expert]
    Verify focus: [verbatim from Phase 2 VERIFY-MAP Verify focus field]
    Interrogates gap because: [verbatim from Phase 2 VERIFY-MAP "Interrogates gap because"
      field — copy exactly; this is the Chain E second transit (Diagnosis Card level)]
    Chain E status: PASS (confirmed from Phase 2 VERIFY-MAP; content reproduced above)
  [new: Chain E is now auditable at card level without consulting Phase 2]

  collaborates_with draft: [{names}]; phantom check: confirmed
  SIMPLIFY-DOMAIN PLAN: Rule N: [text] — domain term: [{term}] — PASS/FLAG
```

For stock roles (pm, architect, strategy): no VERIFY-MAP CITATION (only domain experts
require it; stock roles do not have a sourcing GAP or VERIFY-MAP entry).

After all Diagnosis Cards: **ORTHOGONALITY COMPLETENESS TABLE** (identical to V-01).

After TABLE: **CROSS-CARD UNIQUENESS SCAN** (identical four-phase structure).

**SCAN ORDERING GATE** (identical to V-01):
- [ ] CHALLENGE-COVERAGE MAP complete [C-55]
- [ ] TABLE complete; all rows PASS [C-35]
- [ ] Phase 1 first [C-42]; Phase 2 after Phase 1 [C-50]; Phase 3 after Phase 2 [C-50]
- [ ] Phase 4 last; flags from P2 and P3 [C-43]; no phases merged [C-48]
- [ ] Canonical sequence: CCM → Table → P1 → P2 → P3 → P4

**WRITE:** anchor → stock → experts.

**SIMPLIFY-DOMAIN CHECK** (identical to R13 V-05; no vocabulary anchor):

```
SIMPLIFY-DOMAIN CHECK for {role-name}:
  Rule N: [{text}] — domain term: [{term}] — PASS | FLAG
  GATE: all rules contain domain terms [C-54]; no generic-only exclusion [FC-5]
```

```yaml
---
name: {[FC-1] confirmed}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}
anchor: true                    # ANCHOR-CARD only
orthogonality: "{[FC-11] verbatim from TABLE}"   # non-anchor
inertia_gap_inherited: "{[FC-12] GAP-{slug}: verbatim}"   # experts
orientation:
  frame: |
    {[FC-2]}
  serves: |
    {[FC-3]}
lens:
  verify_questions:
    - "{primary — Chain E: interrogates GAP Failure mode (per VERIFY-MAP CITATION verbatim)}"
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
  - {phantom check confirmed}
  # CONTRACT VIOLATION (type 1) — PHANTOM [C-29]
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST [C-29]
```

Checklist [C-51: criterion per item]:
- [ ] `verify_questions` exact [C-07/FC-4]
- [ ] `simplify_rules` exact [C-07/FC-5]
- [ ] `orthogonality` per [FC-11]; non-anchor only [C-46]; matches TABLE [C-35]
- [ ] `inertia_gap_inherited` per [FC-12]; experts only [C-47]
- [ ] `anchor: true`; anchor only [C-37]
- [ ] ANCHOR-CARD verify_questions cover all Phase 1 challenge questions [C-55/Chain F]
- [ ] Expert verify_questions[0] interrogates GAP Failure mode (per VERIFY-MAP CITATION) [C-53/Chain E/new]
- [ ] VERIFY-MAP CITATION present in each expert Diagnosis Card with verbatim text [new/Chain E]
- [ ] All simplify_rules contain named domain terms [C-54/FC-5]
- [ ] No PHANTOM [C-29/C-33]; no UNIVERSALIST [C-29/C-33]

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. ANCHOR-CARD first; CCM immediately after [C-37/C-55]
2. Each expert Diagnosis Card contains VERIFY-MAP CITATION with verbatim "Interrogates gap
   because" text from Phase 2 VERIFY-MAP [new/Chain E transit]
3. SIMPLIFY-DOMAIN CHECK per role; all domain terms confirmed [C-54]
4. ORTHOGONALITY TABLE complete; all rows PASS [C-35]
5. SCAN four phases; ORDERING GATE confirmed [C-42/C-43/C-48/C-50]
6. YAML in write order (anchor → stock → experts) [C-37]
7. Chains A-F traceable; Chain E audit trail confirmed at Diagnosis Card level [C-52/new]
8. Criterion annotations on all checklist items [C-51]

---

PHASE 6 — (identical to V-01; GATE [C-04/C-22/C-27/C-10/C-20/C-23/C-15/C-52])

---

**Final checklist:**

VERIFY-MAP CITATION (new/Chain E): each expert Diagnosis Card contains verbatim
"Interrogates gap because" text from Phase 2 VERIFY-MAP; Chain E auditable at card level
without consulting Phase 2; status-only annotation absent from expert cards

Challenge coverage (C-55/Chain F): CCM complete; all questions covered

Simplify-domain specificity (C-54): CHECK per role; all domain terms present

Scan structure (C-42/C-43/C-48/C-50): four phases; ORDERING GATE (seven items)

Phase output (C-37/C-46/C-47): correct fields per role type

Chains A-F declared and traceable (C-52)

---

## V-04 — Combined: SIMPLIFY-VOCABULARY ANCHOR + ROLE-MANIFEST

**axis:** lifecycle emphasis + output format (V-01 + V-02)
**hypothesis:** V-01 adds vocabulary provenance for simplify_rule domain terms (Chain G);
V-02 adds a ROLE-MANIFEST forward declaration before Diagnosis Cards begin. These two
mechanisms address orthogonal structural gaps: Chain G concerns provenance traceability of
simplify_rule content; ROLE-MANIFEST concerns completeness assurance for card writing.
Neither depends on the other. V-04 tests whether both can coexist in the formal Phase
register without interaction effects that regress existing criteria.

---

You are running `/org-roles {topic}`.

---

PHASE 0 — FIELD CONTRACT, EXTENSION COMMITMENT, AND PROVENANCE CHAINS

**EXTENSION-COMMITMENT:** (same as V-01)

**FIELD CONTRACT:** (same as V-01 — includes [FC-1] through [FC-12] with V-01's
SIMPLIFY-VOCABULARY ANCHOR added to [FC-5])

**PROVENANCE-CHAIN DECLARATION:**

```
PROVENANCE-CHAIN DECLARATION for /org-roles {topic}:

  Chain A — Inertia gap:
    Source: Phase 2 INERTIA-GAP ANALYSIS — GAP-{slug}.Inertia resistance
    Transit: Phase 5 Diagnosis Card — inertia gap inherited
    Destination: Phase 5 YAML — inertia_gap_inherited
    Integrity: verbatim; GAP-{slug} named; positional breaks A

  Chain B — Orthogonality:
    Source: Phase 5 SCAN + ANCHOR primary question
    Transit: Phase 5 Diagnosis Card — Orthogonality to ANCHOR-CARD
    Destination: Phase 5 YAML — orthogonality
    Integrity: verbatim; named contrast axis; generic breaks B

  Chain C — Inertia surface:
    Source: Phase 1 Status-quo claim
    Transit: Phase 5 ANCHOR-CARD Frame
    Destination: Phase 6 REGISTRY.md inertia_surface
    Integrity: exact words at destination; fulfills EXTENSION-COMMITMENT

  Chain D — Anchor name:
    Source: Phase 1 INERTIA-SURFACE vocabulary
    Transit: Phase 5 ANCHOR-CARD ANCHOR-SOURCING
    Destination: Phase 5 ANCHOR-CARD YAML name
    Integrity: term from INERTIA-SURFACE vocabulary; generic breaks D

  Chain E — Verify-question-to-gap:
    Source: Phase 2 INERTIA-GAP ANALYSIS — GAP-{slug}.Failure mode
    Transit: Phase 2 VERIFY-MAP — Interrogates gap because
    Destination: Phase 5 YAML — lens.verify_questions[0]
    Integrity: primary verify_question interrogates GAP Failure mode

  Chain F — Challenge coverage:
    Source: Phase 1 INERTIA-SURFACE — Challenge questions
    Transit: Phase 5 CHALLENGE-COVERAGE MAP — coverage rows
    Destination: Phase 5 ANCHOR-CARD YAML — verify_questions
    Integrity: all questions represented; unresolved breaks F

  Chain G — Simplify-rule vocabulary provenance (V-01):
    Source: Phase 2 INERTIA-GAP ANALYSIS — GAP-{slug}.Domain vocabulary
    Transit: Phase 5 SIMPLIFY-DOMAIN CHECK — VOCABULARY TRACE per rule
    Destination: Phase 5 YAML — simplify_rules named terms
    Integrity: each named term traces to GAP Domain vocabulary; unprovenance breaks G
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT [C-23/C-30]
2. FIELD-CONTRACT [FC-1]-[FC-12]; [FC-5] includes SIMPLIFY-DOMAIN REQUIREMENT +
   SIMPLIFY-VOCABULARY ANCHOR with BAD/BAD-ANCHOR/GOOD examples [C-26/C-54/new]
3. [FC-1] PROHIBITED NAMES + POSITIVE SOURCING + ANCHOR-SOURCING [C-28/C-31]
4. [FC-4]/[FC-5] EXACT IDENTIFIER labels [C-24/C-07]
5. [FC-10] CONTRACT VIOLATION labels [C-29]
6. [FC-11] REQUIRED FORMAT + YAML persistence [C-46]
7. [FC-12] REQUIRED FORMAT + positional failure + YAML persistence [C-47]
8. PROVENANCE-CHAIN DECLARATION seven chains (A-G); each Source/Transit/Destination/Integrity [C-52/new]

---

PHASES 1-4 — (identical to V-01)

---

PHASE 5 — DIAGNOSIS CARDS, ROLE-MANIFEST, CHALLENGE-COVERAGE MAP, SIMPLIFY-DOMAIN CHECK, ROLE FILES

**PREPARE:** Thirteen inputs — Phase 0 (identifiers/formats/seven chains including Chain G);
Phase 1 INERTIA-SURFACE challenge questions for Chain F; Phase 2 INERTIA-GAP ANALYSIS
(Domain vocabularies available for Chain G) + DOMAIN-ANALYSIS + VERIFY-MAP all PASS;
Phase 3 STOCK-ROLES + write order; Phase 4 OUTPUT-AREA.
[C-07/C-24/C-46/C-47/C-52/C-02/C-39/C-44/C-40/C-45/C-03/C-37/C-04]

**ROLE-MANIFEST (after PREPARE; before first Diagnosis Card; V-02):**

```
ROLE-MANIFEST for /org-roles {topic}:
  | Card name | Type | Source |
  |-----------|------|--------|
  | inertia-advocate | anchor/stock | Phase 3 |
  | pm; architect; strategy | stock | Phase 3 |
  | {expert-1} | domain-expert | Phase 2 / GAP-{slug} |
  ...
  Total expected: {n}
  MANIFEST GATE:
    - [ ] All Phase 2 experts listed [new]
    - [ ] All stock roles listed [new]
    - [ ] Total = experts + 4 stock [new]
```

**ANCHOR-CARD (write first):** (same as V-01; includes SIMPLIFY-DOMAIN PLAN)

**CHALLENGE-COVERAGE MAP:** (immediately after ANCHOR-CARD; identical to V-01)

**SUBSEQUENT DIAGNOSIS CARDS:** (same as V-02; includes MANIFEST CHECK per card and
SIMPLIFY-DOMAIN PLAN per card)

**ORTHOGONALITY TABLE:** (same as V-02; GATE: row count matches ROLE-MANIFEST non-anchor)

**CROSS-CARD UNIQUENESS SCAN:** (four phases; canonical)

**SCAN ORDERING GATE:**
- [ ] ROLE-MANIFEST confirmed [new/V-02]
- [ ] CHALLENGE-COVERAGE MAP complete [C-55]
- [ ] TABLE complete; rows PASS; count matches manifest [C-35/new]
- [ ] Phase 1 first [C-42]; Phase 2 after 1 [C-50]; Phase 3 after 2 [C-50]
- [ ] Phase 4 last; flags from P2+P3 [C-43]; no merges [C-48]
- [ ] Canonical: Manifest → CCM → Table → P1 → P2 → P3 → P4

**WRITE:** anchor → stock → experts.

**SIMPLIFY-DOMAIN CHECK with VOCABULARY ANCHOR** (V-01; before each role's YAML):

```
SIMPLIFY-DOMAIN CHECK for {role-name}:
  Rule N: [{text}]
    Named domain term: [{term}]
    VOCABULARY TRACE: "term '{term}' from GAP-{slug} Domain: {vocabulary-source}"
    Term present: PASS|FLAG; Provenance confirmed: PASS|FLAG
  GATE:
    - [ ] Named term present [C-54]
    - [ ] Vocabulary trace confirmed [new/Chain G]
    - [ ] No generic-only exclusion [FC-5]
```

YAML template same as V-01 (Chain G annotation on simplify_rules).

Checklist [C-51: criterion per item]:
- [ ] `verify_questions` exact [C-07/FC-4]
- [ ] `simplify_rules` exact [C-07/FC-5]
- [ ] `orthogonality` per [FC-11]; non-anchor [C-46]; matches TABLE [C-35]
- [ ] `inertia_gap_inherited` per [FC-12]; experts only [C-47]
- [ ] `anchor: true`; anchor only [C-37]
- [ ] ANCHOR verify_questions cover all challenge questions [C-55/Chain F]
- [ ] Expert verify_questions[0] interrogates GAP Failure mode [C-53/Chain E]
- [ ] All simplify_rules contain named domain terms [C-54/FC-5]
- [ ] All simplify_rule terms trace to GAP Domain vocabulary [new/Chain G]
- [ ] Card name matched against ROLE-MANIFEST [new/V-02]
- [ ] No PHANTOM [C-29/C-33]; no UNIVERSALIST [C-29/C-33]

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. ROLE-MANIFEST written; MANIFEST GATE closed [new/V-02]
2. ANCHOR-CARD first; CCM immediately after [C-37/C-55]
3. Each Diagnosis Card: MANIFEST CHECK [new]; VERIFY-MAP check (experts) [C-53]
4. SIMPLIFY-DOMAIN CHECK with VOCABULARY TRACE per role; all PASS [C-54/new/Chain G]
5. ORTHOGONALITY TABLE complete; row count matches manifest [C-35/new]
6. SCAN four phases; ORDERING GATE (eight items) [C-42/C-43/C-48/C-50]
7. YAML in order; correct per-role fields [C-37/C-46/C-47]
8. Chains A-G traceable [C-52/new]; criterion annotations [C-51]

---

PHASE 6 — (identical to V-01 with total_roles matching ROLE-MANIFEST total)

---

## V-05 — Combined: All Three Axes

**axis:** lifecycle emphasis + output format + phrasing register (V-01 + V-02 + V-03)
**hypothesis:** V-04 carries SIMPLIFY-VOCABULARY ANCHOR (Chain G) and ROLE-MANIFEST. V-05
adds V-03's VERIFY-MAP CITATION verbatim in Diagnosis Cards. The YAML write order remains
anchor → stock → experts (confirmed non-load-bearing in R13 V-05). The three mechanisms
address three distinct structural properties: Chain G tests vocabulary provenance of
simplify_rule content; ROLE-MANIFEST tests forward completeness declaration of the expected
card set; VERIFY-MAP CITATION tests content-level auditability of the Chain E transit.

---

You are running `/org-roles {topic}`.

---

PHASE 0 — FIELD CONTRACT, EXTENSION COMMITMENT, AND PROVENANCE CHAINS

**EXTENSION-COMMITMENT:**

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
          minimum one; opinionated exclusion — NOT scope description
          SIMPLIFY-DOMAIN REQUIREMENT: each rule contains at least one named domain
            artifact, mechanism, field, or vocabulary term; generic terms alone fail
          SIMPLIFY-VOCABULARY ANCHOR (V-01): each named domain term must trace to a
            GAP-{slug} Domain vocabulary entry; cite via VOCABULARY TRACE in CHECK
          BAD: "Skip obvious things"
          BAD-ANCHOR: domain-sounding term with no provenance to Phase 2 vocabulary
          GOOD: named term cites specific GAP-{slug} Domain vocabulary entry

  [FC-6]  expertise.depth — enum: expert | practitioner | senior | principal

  [FC-7]  expertise.relevance — domain-specific; not a role-name restatement

  [FC-8]  scope.primary — one sentence

  [FC-9]  scope.boundary — explicit exclusion; one sentence

  [FC-10] collaborates_with — registry members only
          CONTRACT VIOLATION (type 1) — PHANTOM: absent from registry
          CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent

  [FC-11] orthogonality — non-anchor YAML only
          REQUIRED FORMAT: "[axis] — this role's lens diverges from ANCHOR-CARD because
            [specific reason naming anchor's question and how concern falls outside]"
          REQUIRED: in YAML file; not only in Diagnosis Card

  [FC-12] inertia_gap_inherited — domain expert YAML only
          REQUIRED FORMAT: "GAP-{slug}: [verbatim inertia resistance]"
          Positional reference fails; REQUIRED: in YAML file
```

**PROVENANCE-CHAIN DECLARATION:**

```
PROVENANCE-CHAIN DECLARATION for /org-roles {topic}:

  Chain A — Inertia gap:
    Source:      Phase 2 INERTIA-GAP ANALYSIS — GAP-{slug}.Inertia resistance
    Transit:     Phase 5 Diagnosis Card — inertia gap inherited (verbatim)
    Destination: Phase 5 YAML — inertia_gap_inherited
    Integrity:   verbatim; GAP-{slug} named; positional breaks A

  Chain B — Orthogonality:
    Source:      Phase 5 SCAN + ANCHOR primary question
    Transit:     Phase 5 Diagnosis Card — Orthogonality to ANCHOR-CARD
    Destination: Phase 5 YAML — orthogonality
    Integrity:   verbatim; named axis; generic breaks B

  Chain C — Inertia surface:
    Source:      Phase 1 Status-quo claim
    Transit:     Phase 5 ANCHOR-CARD Frame
    Destination: Phase 6 REGISTRY.md inertia_surface
    Integrity:   exact words at destination; fulfills EXTENSION-COMMITMENT

  Chain D — Anchor name:
    Source:      Phase 1 INERTIA-SURFACE vocabulary
    Transit:     Phase 5 ANCHOR-CARD ANCHOR-SOURCING
    Destination: Phase 5 ANCHOR-CARD YAML name
    Integrity:   term traceable to INERTIA-SURFACE vocabulary

  Chain E — Verify-question-to-gap (two-transit):
    Source:      Phase 2 INERTIA-GAP ANALYSIS — GAP-{slug}.Failure mode
    Transit 1:   Phase 2 VERIFY-MAP — Interrogates gap because
    Transit 2:   Phase 5 Diagnosis Card — VERIFY-MAP CITATION (verbatim reproduction)
    Destination: Phase 5 YAML — lens.verify_questions[0]
    Integrity:   verify_question interrogates GAP Failure mode; Diagnosis Card CITATION
      reproduces Transit 1 verbatim; status-only assertion without content breaks E at T2

  Chain F — Challenge coverage:
    Source:      Phase 1 INERTIA-SURFACE — Challenge questions
    Transit:     Phase 5 CHALLENGE-COVERAGE MAP — coverage rows
    Destination: Phase 5 ANCHOR-CARD YAML — verify_questions
    Integrity:   all questions represented; unresolved breaks F

  Chain G — Simplify-rule vocabulary provenance (V-01):
    Source:      Phase 2 INERTIA-GAP ANALYSIS — GAP-{slug}.Domain vocabulary
    Transit:     Phase 5 SIMPLIFY-DOMAIN CHECK — VOCABULARY TRACE per rule
    Destination: Phase 5 YAML — simplify_rules named terms
    Integrity:   each term traces to GAP Domain vocabulary; unprovenanced term breaks G
```

**GATE** — Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT [C-23/C-30]
2. FIELD-CONTRACT [FC-1]-[FC-12]; [FC-5] includes SIMPLIFY-DOMAIN REQUIREMENT +
   SIMPLIFY-VOCABULARY ANCHOR [C-26/C-54/new]
3. [FC-1] PROHIBITED NAMES + POSITIVE SOURCING + ANCHOR-SOURCING [C-28/C-31]
4. [FC-4]/[FC-5] EXACT IDENTIFIER labels [C-24/C-07]
5. [FC-10] CONTRACT VIOLATION labels [C-29]
6. [FC-11] REQUIRED + YAML persistence [C-46]
7. [FC-12] REQUIRED + positional failure + YAML persistence [C-47]
8. PROVENANCE-CHAIN DECLARATION seven chains (A-G); Chain E states two-transit path with
   content-reproduction requirement at Transit 2 [C-52/new]

---

PHASE 1 — INERTIA SURFACE

```
INERTIA-SURFACE for {topic}:
  Status-quo claim: [specific capability; Chain C + D vocabulary; note terms]
  Challenge questions (min three; {topic} vocabulary):
    Q1: [failure]; Q2: [handling]; Q3: [minimum fix + why insufficient]
```

All challenge questions are Chain F source.
**GATE:** [C-02]; three questions; no expert names.

---

PHASE 2 — DOMAIN ANALYSIS (with VERIFY-MAP)

**Step 1 — INERTIA-GAP ANALYSIS** (min three; GAP-{slug} from Domain vocabulary):

```
INERTIA-GAP ANALYSIS for {topic}:
  GAP-{slug-1}: Domain: [...]; Failure mode: [...]; Inertia resistance: [...]
  GAP-{slug-2}: ...
  GAP-{slug-3}: ...
```

**Step 2 — EXPERT DERIVATION** (POSITIVE SOURCING per expert; no stock roles):

```
DOMAIN-ANALYSIS for {topic}:
  - Expert name: [GAP-{slug} vocabulary slug]
    POSITIVE SOURCING: "this name derives from GAP-{slug}: [term]"
    Named gap source: GAP-{slug}
    Inertia gap: [verbatim]
    Domain-vocabulary frame: [per [FC-2]]
    Verify focus: [first-check artifact]
```

**Step 3 — VERIFY-MAP** (Chain E Transit 1; PASS/FLAG; resolve before Phase 3):

```
VERIFY-MAP for /org-roles {topic}:
  {expert-name}:
    Source gap: GAP-{slug}
    Verify focus: [from DOMAIN-ANALYSIS]
    Interrogates gap because: [connection to GAP-{slug} Failure mode — name it;
      this text will be reproduced verbatim in Phase 5 Diagnosis Card CITATION (Chain E T2)]
    Chain E status: PASS | FLAG
```

**GATE:** [C-39/C-44/C-45/C-40/C-28/C-31]; VERIFY-MAP all PASS [C-53].

---

PHASE 3 — STOCK ROLES

```
STOCK-ROLES:
  - inertia-advocate  (ANCHOR-CARD; Phase 1 frame; written first; anchor: true;
                       CHALLENGE-COVERAGE MAP after ANCHOR-CARD Diagnosis Card)
  - pm; architect; strategy
```

**WRITE ORDER NOTE:** YAML files: inertia-advocate first, then pm/architect/strategy, then
domain experts. [confirmed non-load-bearing from R13 V-05; C-37 satisfied]

**GATE:** [C-03/C-37/C-46/C-47]; write order noted.

---

PHASE 4 — OUTPUT AREA

```
OUTPUT-AREA: .craft/roles/{area}/
```

Area from Phase 2 GAP Domain vocabulary. NOT: `default`, `generic`, `roles`.
**GATE:** [C-04].

---

PHASE 5 — DIAGNOSIS CARDS, ROLE-MANIFEST, CCM, SIMPLIFY-DOMAIN CHECK, ROLE FILES

**PREPARE:** Thirteen inputs:
- Phase 0 [FC-4] `verify_questions` exact identifier [C-07/C-24]
- Phase 0 [FC-5] `simplify_rules` exact identifier + SIMPLIFY-VOCABULARY ANCHOR [C-07/C-24/new]
- Phase 0 [FC-11] REQUIRED FORMAT for `orthogonality` [C-46]
- Phase 0 [FC-12] REQUIRED FORMAT for `inertia_gap_inherited` [C-47]
- Phase 0 PROVENANCE-CHAIN DECLARATION seven chains (A-G) confirmed; Chain E two-transit
  path noted; Chain G vocabulary provenance requirement noted [C-52/new]
- Phase 1 INERTIA-SURFACE: claim + challenge questions for Chain F [C-02]
- Phase 2 INERTIA-GAP ANALYSIS: GAP-{slug} entries with Domain vocabularies for Chain G [C-39/C-44]
- Phase 2 DOMAIN-ANALYSIS: expert names with POSITIVE SOURCING [C-40/C-45]
- Phase 2 VERIFY-MAP: all PASS; "Interrogates gap because" text available for CITATION [C-53/new]
- Phase 3 STOCK-ROLES: four names; anchor designated; write order anchor→stock→experts [C-03/C-37]
- Phase 4 OUTPUT-AREA path [C-04]

PREPARE complete when all thirteen confirmed.

**ROLE-MANIFEST (after PREPARE; before first Diagnosis Card; V-02):**

```
ROLE-MANIFEST for /org-roles {topic}:

  Expected Diagnosis Cards:
  | Card name | Type | Source |
  |-----------|------|--------|
  | inertia-advocate | anchor/stock | Phase 3 |
  | pm | stock | Phase 3 |
  | architect | stock | Phase 3 |
  | strategy | stock | Phase 3 |
  | {expert-1} | domain-expert | Phase 2 / GAP-{slug} |
  | {expert-N} | domain-expert | Phase 2 / GAP-{slug} |

  Manifest totals: Anchor: 1; Non-anchor stock: 3; Experts: {n}; Total: {n+4}

  MANIFEST GATE:
    - [ ] All Phase 2 experts listed with GAP-{slug} source [new]
    - [ ] All Phase 3 stock roles listed [new]
    - [ ] Total = Phase 2 expert count + 4 [new]
```

**ANCHOR-CARD (write first):**

```
ANCHOR-CARD for inertia-advocate:
  name: {INERTIA-SURFACE vocabulary; ANCHOR-SOURCING: "this name derives from
    INERTIA-SURFACE: [term]" — Chain D transit}
  MANIFEST CHECK: confirms row 1 of ROLE-MANIFEST [new/V-02]
  [FC-1] name check: INERTIA-SURFACE trace; NOT placeholder; confirmed

  frame: {Phase 1 status-quo claim — Chain C transit}
  serves: {beneficiary — NOT frame restatement}

  primary_verify_question: {adversarial sufficiency — Chain B source; scan axis}
  verify_questions planned: [{all planned — for CCM below}]
  uniqueness: confirmed distinct; anchor status: ANCHOR-CARD

  collaborates_with: [{registry names}]; phantom check: confirmed

  SIMPLIFY-DOMAIN PLAN:
    Rule N: [text] — domain term: [{term}] — PASS/FLAG
```

**CHALLENGE-COVERAGE MAP (immediately after ANCHOR-CARD; before all other Diagnosis Cards):**

```
CHALLENGE-COVERAGE MAP for /org-roles {topic}:

  Phase 1 challenge questions (complete list):
    Q1: [verbatim]; Q2: [verbatim]; Q3: [verbatim]

  Coverage mapping:
  | Phase 1 Challenge | In ANCHOR-CARD verify_questions? | Evidence |
  |-------------------|----------------------------------|----------|
  | Q1 | YES/NO | [covering question or "absent"] |
  | Q2 | YES/NO | [evidence] |
  | Q3 | YES/NO | [evidence] |

  Covered: {n}; Uncovered: {n}

  CHALLENGE-COVERAGE GATE:
    - [ ] Every Phase 1 question in table [C-55/Chain F]
    - [ ] All YES or add missing question before closing

Chain F transit confirmed. Proceed to subsequent Diagnosis Cards.
```

**SUBSEQUENT DIAGNOSIS CARDS (after CCM):**

```
DIAGNOSIS-CARD for {role-name}:

  MANIFEST CHECK: name matches ROLE-MANIFEST entry [new/V-02]

  name: {[FC-1] confirmed per type}
  [FC-1] name check: [experts: GAP-{slug} trace + term; stock: standard]

  frame: {per role type per [FC-2]}
  serves: {per [FC-3] — NOT restatement}

  inertia gap inherited: {"GAP-{slug}: [verbatim]" (experts) / N/A — Chain A transit}
  orthogonality to ANCHOR-CARD: {[FC-11] — Chain B transit — verbatim to YAML}

  primary_verify_question: {role-specific}
  uniqueness argument: [reason]; confirmed

  VERIFY-MAP CITATION (domain experts only; V-03):
    Source gap: GAP-{slug}
    Verify focus: [verbatim from Phase 2 VERIFY-MAP]
    Interrogates gap because: [verbatim from Phase 2 VERIFY-MAP "Interrogates gap because" —
      this is Chain E Transit 2; copy exactly]
    Chain E status: PASS (content confirmed from Phase 2; reproduced above)

  collaborates_with: [{registry names}]; phantom check: confirmed

  SIMPLIFY-DOMAIN PLAN:
    Rule N: [text] — domain term: [{term}] — PASS/FLAG
```

For stock roles: MANIFEST CHECK present; VERIFY-MAP CITATION absent (not applicable).

After all Diagnosis Cards, **ORTHOGONALITY COMPLETENESS TABLE**:

```
ORTHOGONALITY COMPLETENESS TABLE for /org-roles {topic}:

  ANCHOR primary question: "[anchor primary_verify_question]"

  | Role | Named contrast axis | Distinct from anchor | Distinct from prior rows | Status |
  |------|---------------------|---------------------|--------------------------|--------|
  | {r1} | {axis} | YES/NO | N/A | PASS/FLAG |
  | {r2} | {axis} | YES/NO | YES/NO | PASS/FLAG |

  ORTHOGONALITY COMPLETENESS GATE:
    - [ ] Every non-anchor role in table [C-35]
    - [ ] Every axis names ANCHOR question scope [C-35]
    - [ ] No two rows share named axis [C-35]
    - [ ] Row count matches ROLE-MANIFEST non-anchor total [new/V-02]
    - [ ] All rows PASS
```

After TABLE, **CROSS-CARD UNIQUENESS SCAN** (Phase 1 Enumerate → Phase 2
Anchor-Orthogonality → Phase 3 Non-Anchor Pairwise → Phase 4 Revision-Resolution).

**SCAN ORDERING GATE:**
- [ ] ROLE-MANIFEST confirmed; MANIFEST GATE closed [new/V-02]
- [ ] CHALLENGE-COVERAGE MAP complete; all questions covered [C-55/Chain F]
- [ ] ORTHOGONALITY TABLE complete; all rows PASS; count matches manifest [C-35/new]
- [ ] Phase 1 (Enumerate) first; no checking [C-42]
- [ ] Phase 2 (Anchor-Orthogonality) after Phase 1; before Phase 3 [C-50]
- [ ] Phase 3 (Non-Anchor Pairwise) after Phase 2; before Phase 4 [C-50]
- [ ] Phase 4 (Revision) last; flags from P2 AND P3 collected [C-43]
- [ ] No phases merged; canonical: Manifest → CCM → Table → P1 → P2 → P3 → P4 [C-48]

**WRITE:** YAML files in write order: inertia-advocate FIRST, then pm/architect/strategy,
then domain experts. [C-37]

**SIMPLIFY-DOMAIN CHECK with VOCABULARY ANCHOR** (before each role's YAML, in write order
anchor → stock → experts; V-01):

```
SIMPLIFY-DOMAIN CHECK for {role-name}:
  Rule N: "{rule text}"
    Named domain term: [{term}]
    VOCABULARY TRACE: "term '{term}' from GAP-{slug} Domain: {vocabulary-source}"
    Term present: PASS | FLAG
    Vocabulary provenance confirmed: PASS | FLAG

  SIMPLIFY-DOMAIN GATE:
    - [ ] All rules contain named domain term [C-54/FC-5]
    - [ ] All named terms trace to GAP-{slug} Domain vocabulary [new/Chain G]
    - [ ] No generic-only exclusion [FC-5]
```

```yaml
---
name: {[FC-1] confirmed}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

anchor: true   # ANCHOR-CARD only

orthogonality: "{Chain B — [FC-11] REQUIRED FORMAT; verbatim from TABLE contrast axis}"
               # non-anchor only

inertia_gap_inherited: "{Chain A — GAP-{slug}: [verbatim resistance]; not positional}"
                       # domain experts only

orientation:
  frame: |
    {[FC-2]. FAILURE MODE: task list.}
  serves: |
    {[FC-3]. NOT frame restatement.}

lens:
  verify_questions:
    - "{primary — Chain E T2 dest (experts): interrogates GAP Failure mode per CITATION;
       Chain F dest (anchor): covers Phase 1 challenge question}"
    - "{additional per [FC-4]}"
  simplify_rules:
    - "{[FC-5] SIMPLIFY-DOMAIN REQUIREMENT + VOCABULARY ANCHOR: named term present;
       term traces to GAP-{slug} Domain vocabulary per VOCABULARY TRACE}"

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
  # CONTRACT VIOLATION (type 1) — PHANTOM: absent from registry [C-29]
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent [C-29]
```

Checklist before writing each file [C-51: criterion per item]:
- [ ] `verify_questions` exact as [FC-4] EXACT IDENTIFIER [C-07/FC-4]
- [ ] `simplify_rules` exact as [FC-5] EXACT IDENTIFIER [C-07/FC-5]
- [ ] `orthogonality` per [FC-11]; non-anchor only [C-46]; matches TABLE verbatim [C-35]
- [ ] `inertia_gap_inherited` per [FC-12]; experts only [C-47]
- [ ] `anchor: true`; anchor only [C-37]
- [ ] ANCHOR-CARD verify_questions cover all Phase 1 challenge questions [C-55/Chain F]
- [ ] Expert verify_questions[0] interrogates GAP Failure mode per VERIFY-MAP CITATION [C-53/Chain E/new]
- [ ] VERIFY-MAP CITATION present in each expert card with verbatim Transit-1 text [new/V-03/Chain E T2]
- [ ] All simplify_rules contain named domain terms [C-54/FC-5]
- [ ] All simplify_rule terms trace to GAP Domain vocabulary [new/Chain G]
- [ ] Card name matched against ROLE-MANIFEST [new/V-02]
- [ ] No PHANTOM [C-29/C-33]; no UNIVERSALIST [C-29/C-33]
- [ ] Write order confirmed: anchor → stock → experts [C-37]

**GATE** — Phase 5 complete when ALL of the following are TRUE:
1. ROLE-MANIFEST written after PREPARE; MANIFEST GATE closed [new/V-02]
2. ANCHOR-CARD written first; CCM written immediately after ANCHOR-CARD [C-37/C-55]
3. Each Diagnosis Card carries MANIFEST CHECK [new/V-02]
4. Each expert Diagnosis Card carries VERIFY-MAP CITATION with verbatim "Interrogates gap
   because" text from Phase 2 VERIFY-MAP; Chain E T2 auditable at card level [new/V-03]
5. SIMPLIFY-DOMAIN CHECK with VOCABULARY TRACE run per role (write order anchor → stock →
   experts); all terms present and provenance confirmed [C-54/new/Chain G]
6. ORTHOGONALITY TABLE complete; row count matches manifest non-anchor total [C-35/new]
7. CROSS-CARD UNIQUENESS SCAN four phases; SCAN ORDERING GATE confirmed (eight items)
   [C-42/C-43/C-48/C-50]
8. YAML written: anchor first, then pm/architect/strategy, then domain experts [C-37]
9. ANCHOR-CARD YAML: `anchor: true`; NO `orthogonality`; NO `inertia_gap_inherited` [C-37]
10. Non-anchor YAML: `orthogonality` per [FC-11] REQUIRED FORMAT from TABLE [C-46]
11. Domain expert YAML: `inertia_gap_inherited` per [FC-12] GAP-{slug} verbatim [C-47]
12. All YAML: exact `verify_questions` and `simplify_rules` identifiers [C-07]
13. No prohibited names; no collaborates_with CONTRACT VIOLATION [C-28/C-29/C-33]
14. Chains A-G traceable through transit artifacts to destinations [C-52/new]
15. Per-file checklist items carry criterion-ID annotations [C-51]

---

PHASE 6 — REGISTRY SUMMARY

**COVERAGE-GATE** — before writing REGISTRY.md:

```
COVERAGE-GATE for /org-roles {topic}:
  Walk each GAP-{slug} from Phase 2 INERTIA-GAP ANALYSIS:
    GAP-{slug-1}: Expert derived: {name}; File written: {filename}; Status: COVERED|GAP
    GAP-{slug-2}: ...
  Coverage summary:
    Covered: {n} — {GAP-{slug} list}
    Uncovered: {n} — {list or "none"}
```

Do not write REGISTRY.md until COVERAGE-GATE complete.

**PREPARE:** Enumerate Phase 5 `.md` files; record `PHASE5_COUNT`. Count from Phase 5 only.

**WRITE:** `.craft/roles/{area}/REGISTRY.md`:

```
---
area: {Phase 2 GAP Domain vocabulary}
generated: {date}
---

## Registry Summary

total_roles: {PHASE5_COUNT — must match ROLE-MANIFEST total from Phase 5 manifest}

stock_roles:
  - inertia-advocate  (ANCHOR-CARD — Phase 1; written first)
  - pm
  - architect
  - strategy

domain_experts:
  - name: {expert-name}
    gap_source: GAP-{slug}
    inertia_gap: {verbatim resistance}

coverage_gaps: |
  {from COVERAGE-GATE Uncovered gaps; or "none detected"}

inertia_surface: |
  {Phase 1 status-quo claim verbatim — Chain C destination}

Generated by: /org-roles {topic} — {date}
```

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. COVERAGE-GATE complete; every Phase 2 gap enumerated [C-10]
2. `coverage_gaps` from COVERAGE-GATE; not memory
3. `REGISTRY.md` at correct path [C-04]
4. `total_roles` = PHASE5_COUNT AND matches ROLE-MANIFEST total [C-22/C-27/new]
5. `domain_experts` with name/gap_source/inertia_gap verbatim [C-10]
6. `inertia_surface` verbatim — Chain C confirmed [C-20/C-23]
7. No heading stubs [C-15]
8. Chains A-G traceable [C-52/new]

---

**Final checklist — confirm before declaring done:**

VERIFY-MAP CITATION (new/V-03/Chain E T2): every expert Diagnosis Card contains VERIFY-MAP
CITATION block with verbatim "Interrogates gap because" text from Phase 2; Chain E T2
confirmed at card level; status-only annotation absent from expert cards

Simplify vocabulary provenance (new/V-01/Chain G): SIMPLIFY-DOMAIN CHECK with VOCABULARY
TRACE run per role; every simplify_rule domain term traces to GAP-{slug} Domain vocabulary;
VOCABULARY TRACE citations written; Chain G confirmed

ROLE-MANIFEST forward declaration (new/V-02): manifest written after PREPARE; all expected
cards listed; MANIFEST GATE closed; each card carries MANIFEST CHECK; TABLE row count
confirmed against manifest; total_roles matches manifest total

Challenge coverage (C-55/Chain F): CHALLENGE-COVERAGE MAP after ANCHOR-CARD; every Phase 1
challenge question represented; Chain F confirmed

Verify-question traceability (C-53/Chain E T1): VERIFY-MAP in Phase 2; all experts PASS;
primary verify_questions interrogate GAP Failure modes

Simplify-domain specificity (C-54): SIMPLIFY-DOMAIN CHECK per role; named domain terms present

Write order confirmed: anchor → pm → architect → strategy → domain experts [C-37]

Scan structure (C-42/C-43/C-48/C-50): SCAN ORDERING GATE confirmed (eight items:
Manifest → CCM → Table → P1 → P2 → P3 → P4)

Orthogonality completeness (C-35): TABLE after all Diagnosis Cards; axes distinct; all PASS

Phase output (C-37/C-46/C-47): `anchor: true` in anchor; `orthogonality` in non-anchor;
`inertia_gap_inherited` in experts

Provenance chains (C-52): seven chains (A-G) declared in Phase 0; all traceable

Gap/sourcing (C-39/C-44/C-40/C-45): INERTIA-GAP before naming; POSITIVE SOURCING per expert;
ANCHOR-SOURCING per anchor

Contract violations (C-29/C-33): labels in YAML template and per-file checklist

Pipeline annotations (C-51): all gate items and checklist items carry [C-NN]

Coverage gate: COVERAGE-GATE complete; `coverage_gaps` from enumeration not memory
