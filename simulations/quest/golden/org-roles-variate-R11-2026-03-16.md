---
skill: quest-variate
skill_target: org-roles
date: 2026-03-16
round: R11
rubric_version: v11
status: variate
---

# org-roles Variate — Round 11

**Date:** 2026-03-16
**Skill:** org-roles
**Rubric:** v11 (C-01 through C-49; new in v11: C-48 canonical 4-phase scan ordering,
C-49 per-file checklist criterion cross-referencing — both derived from R10 excellence signals)
**Round:** R11 — single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

**Context:** R10 V-05 closed the v11 frontier at 100.00 — the first perfect score in the
series. The v11 ceiling is 41/41. R11 variates all inherit R10 V-05's imperative register
and 4-phase scan as the base, and explore structural patterns beyond C-48/C-49 that could
surface as C-50+ in v12. All five variations must maintain 100.00 under v11 while discovering
new forcing mechanisms.

**Post-ceiling framing:** When the rubric ceiling is closed, variate exploration shifts from
"find missing mechanisms" to "strengthen existing mechanisms." Three candidate strengthening
patterns identified from R10 V-05 analysis:

1. **Gate-encoded canonical ordering** — C-48 is satisfied by structural position of scan
   phases. A variate that additionally declares the ordering as an explicit gate condition
   (verified, not just arranged) would surface a new structural property: ordering as a
   formally asserted constraint rather than an inferred artifact.

2. **Criterion ID propagation to all gates** — C-49 is satisfied by criterion-ID annotations
   in the per-file checklist. Propagating [C-NN] annotations to every gate checkpoint across
   the pipeline generalizes the C-49 mechanism from file-writing to the full pipeline.

3. **Provenance chain declaration** — the three artifact chains (gap→card→YAML,
   ortho→card→YAML, status-quo→registry) are enforced structurally but never declared as
   named artifacts. Declaring them explicitly before writing begins creates a formal
   self-auditing structure.

---

## Round 11 Variation Map

| V | Axis | Primary new pattern | Hypothesis |
|---|------|---------------------|------------|
| V-01 | lifecycle emphasis | SCAN ORDERING GATE — canonical sequence declared as explicit gate condition after scan block | C-48 currently satisfied by structure; a gate that asserts "Phase 1 executed before Phase 2, Phase 2 before Phase 3, Phase 3 before Phase 4; no phases merged" turns ordering into a formally verified constraint rather than inferred arrangement — potential C-50 |
| V-02 | output format | Criterion ID propagation — [C-NN] annotations on every gate item throughout the pipeline, not just the per-file checklist | C-49 satisfied by per-file checklist; propagating criterion IDs to step-end gate items creates a fully cross-referenced pipeline where every checkpoint names the criterion it enforces — potential C-50 |
| V-03 | inertia framing | PROVENANCE-CHAIN DECLARATION — named artifact block in Step 6 PREPARE declaring all three artifact chains before cards are written | The three provenance chains (inertia gap, orthogonality, inertia surface) exist structurally but are never declared as a named artifact; making them explicit and gated creates a new structural mechanism for pipeline self-auditing — potential C-50 |
| V-04 | V-01+V-02 combined | SCAN ORDERING GATE + criterion ID propagation to all gates | Full synthesis of V-01 and V-02: canonical ordering asserted as gate condition AND full pipeline criterion cross-referencing |
| V-05 | V-01+V-02+V-03 + register | All three patterns + formal Phase-based register (vs imperative Steps) | Tests whether all three new mechanisms survive a register change; R10 V-04 (formal register) achieved 99.76 vs V-05 (imperative) 100.00 — V-05 R11 restores formal register WITH all V-05 R10 mechanisms to test register robustness at the ceiling |

---

## V-01 — Single-Axis: SCAN ORDERING GATE

**axis:** lifecycle emphasis
**hypothesis:** R10 V-05 achieves C-48 because its four scan phases appear in canonical
sequence (Phase 1 Enumerate → Phase 2 Anchor-Orthogonality → Phase 3 Non-Anchor Pairwise
→ Phase 4 Revision-Resolution). The current gate in Step 7 only confirms that "all four
phases pass" without explicitly asserting the ordering as a verified constraint. This
variate adds a SCAN ORDERING GATE checklist after the scan block — six items that
individually verify: Phase 1 ran before Phase 2, Phase 2 before Phase 3, Phase 3 before
Phase 4, no two consecutive phases share a label, no phase was merged with an adjacent
phase, and the canonical sequence is confirmed. The final checklist extends the
scan-structure item to reference SCAN ORDERING GATE confirmation. All other elements
identical to R10 V-05.
Falsifiable: if the evaluator treats the SCAN ORDERING GATE as a C-48 paraphrase (not a
distinct mechanism), the gate items score no new criteria and V-01 equals V-04 R10 under
v11. If the gate asserts something structurally distinct from C-48's positional test, a
new C-50 criterion emerges for v12.

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

For each gap the Step 2 status-quo claim leaves uncovered, assign a formal identifier
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

**SCAN ORDERING GATE** — confirm before writing any YAML:
- [ ] Phase 1 (Enumerate) executed first; no checking or flagging occurred in Phase 1
- [ ] Phase 2 (Anchor-Orthogonality) executed after Phase 1 was complete and before Phase 3 began
- [ ] Phase 3 (Non-Anchor Pairwise) executed after Phase 2 was complete and before Phase 4 began
- [ ] Phase 4 (Revision and Resolution) executed last; collected flags from Phase 2 AND Phase 3
- [ ] No two consecutive phases share a label; no phase was merged with an adjacent phase
- [ ] Canonical sequence confirmed: Phase 1 (Enumerate) → Phase 2 (Anchor-Orthogonality) →
     Phase 3 (Non-Anchor Pairwise) → Phase 4 (Revision-Resolution)

SCAN ORDERING GATE complete when all six items checked. Do not write any YAML until GATE passes.

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

Scan structure (C-38/C-42/C-43/C-48): CROSS-CARD UNIQUENESS SCAN ran four named phases in
canonical sequence — Phase 1 (Enumerate All Verify Questions), Phase 2 (Anchor-Orthogonality),
Phase 3 (Non-Anchor Pairwise), Phase 4 (Revision and Resolution); SCAN ORDERING GATE
confirmed: all six ordering items checked, canonical sequence Phase 1→2→3→4 verified,
no phases merged; Phase 4 complete before any YAML was written

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

---

## V-02 — Single-Axis: Criterion ID Propagation to All Gate Items

**axis:** output format
**hypothesis:** R10 V-05 earns C-49 because its per-file Step 8 checklist carries
CONTRACT VIOLATION criterion-ID annotations (C-29/C-33), and the final checklist labels
each group with C-NN identifiers. But gate items in Steps 2, 3, 4, 6, 7, and 9 carry no
criterion annotations — the evaluator must externally map each rule to its rubric criterion.
This variate propagates [C-NN] annotations to a "Criterion check:" line at the end of each
step's rule block, and annotates every per-file checklist item with its governing criterion
ID. The per-file checklist becomes fully self-auditing: any single item names the criterion
it enforces without reference to other sections. All other elements identical to R10 V-05.
Falsifiable: if the evaluator scores C-49 on per-file checklist annotations only (C-29/C-33
as in R10 V-05) and treats gate-level criterion annotations as redundant, V-02 scores
identically to R10 V-05 under v11. If gate-level annotation is a distinct mechanism, a new
C-50 criterion emerges for v12.

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

Criterion check: [C-28] BANNED list named above; [C-31] prohibition appears at Step 1 (checkpoint 1 of 3);
[C-40] positive sourcing constraint established before any expert is named

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

Criterion check: [C-02] status-quo claim present with specific capability named; [C-39 precondition]
no expert names appear — gap analysis has not started; [C-23] EXTENSION-COMMITMENT written
before this step

---

**Step 3 — Gap analysis with named identifiers (before naming any expert):**

For each gap the Step 2 status-quo claim leaves uncovered, assign a formal identifier
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

Criterion check: [C-44] GAP-{slug} identifiers derive from Domain vocabulary, not positional;
[C-39] this block precedes expert naming — artifact order enforced; [C-28/C-31] prohibited
names absent (checkpoint 2 of 3 for C-31 is Step 4)

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

Criterion check: [C-45] POSITIVE SOURCING field present inline per expert record, not only at gate;
[C-40] expert names derive from GAP-{slug} vocabulary confirmed per record; [C-28/C-31]
BANNED names absent from every expert name (checkpoint 3 of 3 for C-31); [C-34] inertia gap
per expert in derivation record

---

**Step 5 — Confirm output area:**

Write:
```
OUTPUT-AREA: .craft/roles/{area}/
```

Use GAP Domain vocabulary for the area slug. Not: `default`, `generic`, `roles`.

Criterion check: [C-04] output area path in `.craft/roles/{area}/` format; area slug from
GAP Domain vocabulary

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

Criterion check (after all cards written): [C-37] ANCHOR-CARD written first; all subsequent
cards written after; [C-41] Inertia gap inherited present in every domain expert card citing
"GAP-{slug}: [resistance verbatim]"; [C-35] Orthogonality to ANCHOR-CARD present in every
non-anchor card; [C-21] uniqueness argument present per card before YAML writing

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

Criterion check: [C-42] Phase 1 is enumerate-only — no checking began until Phase 2;
[C-43] Phase 4 is named revision phase — separate label from Phase 3; [C-48] four phases
in canonical sequence: enumerate → anchor-ortho → pairwise → revision-resolution, no two
consecutive phases share a label; [C-38] scan has at least three named phases with
anchor-orthogonality separated from pairwise; [C-36] cross-set scan gate between Diagnosis
Cards and YAML writing

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
  # CONTRACT VIOLATION (type 1) — PHANTOM: a name absent from this registry [C-29]
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent [C-29]
```

Checklist before writing each file [C-49: each item names its governing criterion]:
- [ ] `verify_questions` spelled exactly as committed [C-07/FC-4] (PROHIBITED: verify, questions, checks)
- [ ] `simplify_rules` spelled exactly as committed [C-07/FC-5] (PROHIBITED: simplify, rules, guidelines)
- [ ] `orthogonality` present for all non-anchor roles; absent from ANCHOR-CARD file [C-46]
- [ ] `inertia_gap_inherited` present for domain expert files; absent from stock/anchor files [C-47]
- [ ] `anchor: true` present in inertia-advocate file only [C-37]
- [ ] No PHANTOM names in `collaborates_with` — CONTRACT VIOLATION (type 1) [C-29/C-33]
- [ ] No UNIVERSALIST listing in `collaborates_with` — CONTRACT VIOLATION (type 2) [C-29/C-33]

Criterion check: [C-01] all six required schema fields and sub-fields present; [C-07] exact
field identifiers used; [C-29] CONTRACT VIOLATION framing in collaborates_with annotation;
[C-33] CONTRACT VIOLATION labels mirrored in YAML template at write site; [C-49] per-file
checklist items annotated with criterion IDs above

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

Criterion check: [C-10] all five registry fields present with substantive content; [C-22]
total_roles derived from PHASE5_COUNT enumeration, not a computed sum; [C-27] PHASE5_COUNT
declared from Step 8 enumeration before WRITE; [C-20] inertia_surface extension field
present fulfilling EXTENSION-COMMITMENT

---

**Final checklist — confirm before declaring done:**

Phase output (C-37/C-46): inertia-advocate YAML has `anchor: true`; all other YAML files
have `orthogonality` field with named contrast axis tracing to ANCHOR-CARD primary question

Scan structure (C-38/C-42/C-43/C-48): CROSS-CARD UNIQUENESS SCAN ran four named phases —
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

---

## V-03 — Single-Axis: Provenance Chain Declaration

**axis:** inertia framing
**hypothesis:** R10 V-05 enforces three artifact provenance chains structurally (inertia gap
flows GAP-ANALYSIS → Diagnosis Card → YAML; orthogonality flows Diagnosis Card → YAML;
status-quo claim flows INERTIA-SURFACE → REGISTRY.md), but never declares these chains as
a named artifact. A model following the pipeline can populate each field correctly without
ever stating "Chain A carries X from source Y to destination Z." This variate adds a
PROVENANCE-CHAIN DECLARATION block inside Step 6 PREPARE — three named chains with
explicit source, transit, destination, and integrity rules — that must be written before
any Diagnosis Card is produced. The final checklist adds a provenance chain verification
item. All other elements identical to R10 V-05.
Falsifiable: if the PROVENANCE-CHAIN DECLARATION produces no scoring delta under v11
(because all chains are already structurally enforced), the mechanism has no independent
criterion signal. If declaring chains as a formal artifact enables a new verification
pattern, a C-50 criterion emerges for v12.

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

For each gap the Step 2 status-quo claim leaves uncovered, assign a formal identifier
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

**PREPARE — Provenance chains and inputs:**

Before writing any Diagnosis Card, declare the three provenance chains that this pipeline
must maintain. Write this block verbatim, filling in the source names from your context:

```
PROVENANCE-CHAIN DECLARATION for /org-roles {topic}:

  Chain A — Inertia gap provenance:
    Source:      INERTIA-GAP ANALYSIS (Step 3) — field: GAP-{slug}.Inertia resistance
    Transit:     Diagnosis Card (Step 6) — field: Inertia gap inherited
    Destination: YAML role file (Step 8) — field: inertia_gap_inherited
    Integrity rule: copy verbatim at each transit; cite GAP-{slug} identifier throughout;
      positional reference ("Gap 1") breaks Chain A at destination

  Chain B — Orthogonality provenance:
    Source:      CROSS-CARD UNIQUENESS SCAN (Step 7) + ANCHOR-CARD primary question
    Transit:     Diagnosis Card (Step 6) — field: Orthogonality to ANCHOR-CARD
    Destination: YAML role file (Step 8) — field: orthogonality
    Integrity rule: copy verbatim from Diagnosis Card to YAML; must name contrast axis
      tracing to ANCHOR-CARD primary question; generic assertion breaks Chain B

  Chain C — Inertia surface provenance:
    Source:      INERTIA-SURFACE (Step 2) — field: Status-quo claim
    Transit:     ANCHOR-CARD Frame (Step 6) — rephrased as epistemic stance
    Destination: REGISTRY.md (Step 9) — field: inertia_surface
    Integrity rule: inertia_surface in REGISTRY.md uses exact words of Status-quo claim;
      ANCHOR-CARD Frame may rephrase but must trace to same claim

PROVENANCE-CHAIN DECLARATION complete when all three chains written.
Do not begin Diagnosis Cards until PROVENANCE-CHAIN DECLARATION is complete.
```

Also confirm these inputs before beginning:
- Step 0 `verify_questions` exact identifier confirmed
- Step 0 `simplify_rules` exact identifier confirmed
- Step 0 `orthogonality` REQUIRED FORMAT confirmed
- Step 0 `inertia_gap_inherited` REQUIRED FORMAT confirmed
- Step 2 INERTIA-SURFACE status-quo claim confirmed
- Step 3 INERTIA-GAP ANALYSIS all GAP-{slug} entries confirmed
- Step 4 DOMAIN-ANALYSIS expert names with POSITIVE SOURCING confirmed

PREPARE complete when PROVENANCE-CHAIN DECLARATION written and all inputs confirmed.

**ANCHOR-CARD (write first):**
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
  Inertia gap inherited: [for experts: "GAP-{slug}: [resistance verbatim]" — Chain A transit;
    for stock: N/A]
  Orthogonality to ANCHOR-CARD: [named contrast axis — Chain B transit; per REQUIRED FORMAT
    in Commit 2; this exact value is copied to YAML `orthogonality` field]
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
orthogonality: "{Chain B destination — copy verbatim from Diagnosis Card 'Orthogonality
  to ANCHOR-CARD'; must name contrast axis tracing to ANCHOR-CARD primary question}"

# Domain expert roles ONLY — present in expert files, absent from stock and anchor:
inertia_gap_inherited: "{Chain A destination — GAP-{slug}: [inertia resistance verbatim
  from INERTIA-GAP ANALYSIS]; not positional}"

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
- [ ] `orthogonality` present for all non-anchor roles; absent from ANCHOR-CARD file [Chain B]
- [ ] `inertia_gap_inherited` present for domain expert files; absent from stock/anchor [Chain A]
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
  {Step 2 status-quo claim — exact words; Chain C destination; fulfills EXTENSION-COMMITMENT}

Generated by: /org-roles {topic} — {date}
```

HEADING STUB RULE: Every field must contain substantive content. A section header with no
real value beneath it fails C-10.

---

**Final checklist — confirm before declaring done:**

Phase output (C-37/C-46): inertia-advocate YAML has `anchor: true`; all other YAML files
have `orthogonality` field with named contrast axis tracing to ANCHOR-CARD primary question

Scan structure (C-38/C-42/C-43/C-48): CROSS-CARD UNIQUENESS SCAN ran four named phases —
Phase 1 (Enumerate All Verify Questions), Phase 2 (Anchor-Orthogonality), Phase 3
(Non-Anchor Pairwise), Phase 4 (Revision and Resolution) — per-role records written,
Phase 4 complete before any YAML was written

Gap artifact (C-39/C-44): INERTIA-GAP ANALYSIS block with formal GAP-{slug} identifiers
written before any expert was named in Step 4

Expert sourcing (C-40/C-45): every expert has a POSITIVE SOURCING statement citing the
specific GAP-{slug} identifier and domain vocabulary term used in the name, embedded inline
in the derivation record

Provenance chains declared and verified: PROVENANCE-CHAIN DECLARATION written before first
Diagnosis Card; Chain A (inertia gap: GAP-ANALYSIS → Diagnosis Card → YAML) verified by
checking inertia_gap_inherited in every domain expert YAML; Chain B (orthogonality:
Diagnosis Card → YAML orthogonality) verified by checking verbatim copy per non-anchor file;
Chain C (inertia surface: INERTIA-SURFACE → REGISTRY.md) verified by checking inertia_surface
field contains Step 2 status-quo claim verbatim

Contract violations (C-29/C-33): `collaborates_with` section in every YAML file includes
CONTRACT VIOLATION (type 1) — PHANTOM comment and CONTRACT VIOLATION (type 2) —
UNIVERSALIST comment; phantom check confirmed for every collaborates_with list written

---

## V-04 — Combined: SCAN ORDERING GATE + Criterion ID Propagation

**axis:** lifecycle emphasis + output format (V-01 + V-02 combined)
**hypothesis:** V-01 and V-02 explore independent structural mechanisms. V-04 combines them:
the SCAN ORDERING GATE from V-01 makes canonical ordering a formally verified gate condition;
criterion-ID annotations from V-02 propagate [C-NN] to every gate/criterion-check block
throughout the pipeline. Together, these create a prompt where every structural requirement
is both named by its criterion ID at the point of enforcement AND verified as an explicit
gate condition. Expected outcome: 41/41 = 100.00 under v11; potential discovery of two
independent C-50 candidates for v12 evaluation. Falsifiable: if the evaluator treats
SCAN ORDERING GATE and criterion-ID propagation as C-48/C-49 paraphrases respectively, V-04
scores identically to R10 V-05 — demonstrating no new distinguishable structural property.

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

Criterion check: [C-28] BANNED list named; [C-31] prohibition at Step 1 (location 1 of 3);
[C-40] positive sourcing constraint established before any expert is named

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

Criterion check: [C-02] status-quo claim present; [C-39 precondition] no expert names appear;
[C-23] EXTENSION-COMMITMENT written at Commit 1 before this step

---

**Step 3 — Gap analysis with named identifiers (before naming any expert):**

For each gap the Step 2 status-quo claim leaves uncovered, assign a formal identifier
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

Criterion check: [C-44] GAP-{slug} identifiers derive from Domain vocabulary; [C-39] artifact
precedes expert naming in Step 4; [C-31] prohibition absent here (location 2 is Step 4)

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

Criterion check: [C-45] POSITIVE SOURCING field inline per expert record; [C-40] names derive
from GAP vocabulary per record; [C-28/C-31] BANNED names absent — checkpoint 2 of 3 for C-31;
[C-34] inertia gap per expert record present

---

**Step 5 — Confirm output area:**

Write:
```
OUTPUT-AREA: .craft/roles/{area}/
```

Use GAP Domain vocabulary for the area slug. Not: `default`, `generic`, `roles`.

Criterion check: [C-04] output area path correct; area slug from GAP Domain vocabulary

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
  Orthogonality to ANCHOR-CARD: [named contrast axis — per REQUIRED FORMAT in Commit 2;
    this exact value is copied to YAML `orthogonality` field]
  Primary question: [most role-specific question for this Frame]
  Uniqueness: [why no other role asks this first]; confirmed distinct
  Collaborates with: [{name-1}, {name-2}]; phantom check: confirmed
```

Criterion check: [C-37] ANCHOR-CARD written first; all subsequent cards written after;
[C-41] Inertia gap inherited present in every domain expert card with GAP-{slug} citation;
[C-35] Orthogonality to ANCHOR-CARD present per non-anchor card; [C-21] uniqueness argument
per card; [C-31] BANNED names absent from all card names — checkpoint 3 of 3 for C-31

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

Criterion check: [C-42] Phase 1 enumerate-only; [C-43] Phase 4 named revision phase; [C-48]
four phases in canonical sequence: no consecutive phases share a label; [C-38] at least three
named phases with anchor-ortho separate from pairwise; [C-36] cross-set gate between cards
and YAML

**SCAN ORDERING GATE** — confirm before writing any YAML:
- [ ] Phase 1 (Enumerate) executed first; no checking occurred in Phase 1 [C-42]
- [ ] Phase 2 (Anchor-Orthogonality) executed after Phase 1 and before Phase 3 [C-48]
- [ ] Phase 3 (Non-Anchor Pairwise) executed after Phase 2 and before Phase 4 [C-48]
- [ ] Phase 4 (Revision and Resolution) executed last; collected flags from Phase 2 AND Phase 3 [C-43]
- [ ] No two consecutive phases share a label; no phase was merged with adjacent phase [C-48]
- [ ] Canonical sequence confirmed: Phase 1 → Phase 2 → Phase 3 → Phase 4 [C-48]

SCAN ORDERING GATE complete when all six items checked. Do not write YAML until GATE passes.

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
  # CONTRACT VIOLATION (type 1) — PHANTOM: a name absent from this registry [C-29]
  # CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent [C-29]
```

Checklist before writing each file [C-49: each item names its governing criterion]:
- [ ] `verify_questions` spelled exactly as committed [C-07/FC-4] (PROHIBITED: verify, questions, checks)
- [ ] `simplify_rules` spelled exactly as committed [C-07/FC-5] (PROHIBITED: simplify, rules, guidelines)
- [ ] `orthogonality` present for all non-anchor roles; absent from ANCHOR-CARD file [C-46]
- [ ] `inertia_gap_inherited` present for domain expert files; absent from stock/anchor [C-47]
- [ ] `anchor: true` present in inertia-advocate file only [C-37]
- [ ] No PHANTOM names in `collaborates_with` — CONTRACT VIOLATION (type 1) [C-29/C-33]
- [ ] No UNIVERSALIST listing in `collaborates_with` — CONTRACT VIOLATION (type 2) [C-29/C-33]

Criterion check: [C-01] all six schema fields present; [C-07] exact identifiers used; [C-29]
CONTRACT VIOLATION framing at collaborates_with write site; [C-33] labels mirrored in template;
[C-49] per-file checklist items carry criterion-ID annotations

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

Criterion check: [C-10] all five fields present with substantive content; [C-22] total_roles
from PHASE5_COUNT enumeration; [C-27] PHASE5_COUNT declared before WRITE; [C-20] inertia_surface
extension field present

---

**Final checklist — confirm before declaring done:**

Phase output (C-37/C-46): inertia-advocate YAML has `anchor: true`; all other YAML files
have `orthogonality` field with named contrast axis tracing to ANCHOR-CARD primary question

Scan structure (C-38/C-42/C-43/C-48): CROSS-CARD UNIQUENESS SCAN ran four named phases in
canonical sequence — Phase 1 (Enumerate All Verify Questions), Phase 2 (Anchor-Orthogonality),
Phase 3 (Non-Anchor Pairwise), Phase 4 (Revision and Resolution); SCAN ORDERING GATE
confirmed: all six criterion-annotated ordering items checked, canonical sequence verified,
no phases merged; Phase 4 complete before any YAML was written

Gap artifact (C-39/C-44): INERTIA-GAP ANALYSIS block with formal GAP-{slug} identifiers
written before any expert was named in Step 4

Expert sourcing (C-40/C-45): every expert has a POSITIVE SOURCING statement citing the
specific GAP-{slug} identifier and domain vocabulary term used in the name, embedded inline
in the derivation record

Provenance (C-41/C-47): every domain expert Diagnosis Card has `Inertia gap inherited`
citing "GAP-{slug}: [resistance verbatim]"; same value persisted into YAML
`inertia_gap_inherited` field — not positional ("Gap 1")

Contract violations (C-29/C-33): `collaborates_with` section in every YAML file includes
CONTRACT VIOLATION (type 1) — PHANTOM comment [C-29] and CONTRACT VIOLATION (type 2) —
UNIVERSALIST comment [C-29]; labels mirrored in template [C-33]; phantom check confirmed

---

## V-05 — Combined: All Three Axes + Formal Phase Register

**axis:** lifecycle emphasis + output format + inertia framing + phrasing register
(V-01 + V-02 + V-03 + register change)
**hypothesis:** V-04 carries all R10 V-05 mechanisms (4-phase scan, criterion IDs in
per-file checklist) plus V-01's SCAN ORDERING GATE and V-02's criterion-ID propagation, all
in the imperative Step register. V-05 adds V-03's PROVENANCE-CHAIN DECLARATION and switches
to the formal Phase-based register (Phase 0 through Phase 6 with named GATE blocks) used by
R10 V-03/V-04, which scored 99.76 (failing only C-49). V-05 R11 thus takes the formal
register + adds all three new mechanisms — testing whether formal register + SCAN ORDERING
GATE + criterion-ID gates + PROVENANCE-CHAIN DECLARATION preserves 100.00 under v11 or
whether the register change creates edge-case regressions in any of the new mechanisms.
Falsifiable: if formal register re-introduces the C-29/C-33 regressions seen in R9 V-04
and R10 V-03/V-04, the per-file checklist criterion annotations are insufficient to protect
them — demonstrating that the imperative register's inline checklist is more reliable than
the formal register's GATE block for contract violation enforcement.

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
   Transit, Destination, and Integrity rule

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
- Phase 0 PROVENANCE-CHAIN DECLARATION: all three chains confirmed [C-41/C-46/C-47]
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
- [ ] Phase 2 (Anchor-Orthogonality) executed after Phase 1 and before Phase 3 [C-48]
- [ ] Phase 3 (Non-Anchor Pairwise) executed after Phase 2 and before Phase 4 [C-48]
- [ ] Phase 4 (Revision and Resolution) executed last; collected flags from Phase 2 AND Phase 3 [C-43]
- [ ] No two consecutive phases share a label; no phase merged with an adjacent phase [C-48]
- [ ] Canonical sequence confirmed: Phase 1 → Phase 2 → Phase 3 → Phase 4 [C-48]

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

Checklist before writing each file [C-49: each item names its governing criterion]:
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
   confirmed with all six items checked; Phase 4 complete before YAML writing began [C-42/C-43/C-48]
5. One `.md` file per role; inertia-advocate (ANCHOR-CARD) written first [C-37]
6. ANCHOR-CARD YAML: `anchor: true`; NO `orthogonality`; NO `inertia_gap_inherited` [C-37]
7. Non-anchor YAML: `orthogonality` field per [FC-11] REQUIRED FORMAT — not generic [C-46]
8. Domain expert YAML: `inertia_gap_inherited` per [FC-12] citing GAP-{slug} — not positional [C-47]
9. All YAML files use exact identifiers `verify_questions` and `simplify_rules` verbatim [C-07]
10. No prohibited names per [FC-1]; no collaborates_with CONTRACT VIOLATION; labels mirrored
    in template annotation per [C-33] [C-28/C-29/C-33]
11. PROVENANCE-CHAIN DECLARATION Chain A, B, C each traceable through Diagnosis Cards to YAML

---

PHASE 6 — REGISTRY SUMMARY

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
  {Phase 2 gaps not addressed by any derived expert; or "none detected."}

inertia_surface: |
  {Phase 1 status-quo claim verbatim — Chain C destination; fulfills EXTENSION-COMMITMENT}

Generated by: /org-roles {topic} — {date}
```

HEADING STUB FAIL CONDITION: Section headers with empty or omitted values beneath them
fail C-10. Every field must contain substantive content.

**GATE** — Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.craft/roles/{area}/REGISTRY.md` [C-04]
2. `total_roles` equals `PHASE5_COUNT` from Phase 5 enumeration [C-22/C-27]
3. `domain_experts` lists each expert with `name`, `gap_source` (GAP-{slug}),
   `inertia_gap` (verbatim) [C-10]
4. `inertia_surface` contains Phase 1 status-quo claim verbatim [C-20/C-23] — Chain C
   destination integrity verified
5. No heading stubs; HEADING STUB FAIL CONDITION was read before writing began [C-15]
6. PROVENANCE-CHAIN DECLARATION Chain C integrity confirmed: inertia_surface exact words
   match Phase 1 Status-quo claim

---

**Final checklist — confirm before declaring done:**

Phase output (C-37/C-46): inertia-advocate YAML has `anchor: true`; all other YAML files
have `orthogonality` field with named contrast axis tracing to ANCHOR-CARD primary question

Scan structure (C-38/C-42/C-43/C-48): CROSS-CARD UNIQUENESS SCAN ran four named phases in
canonical sequence — Phase 1 (Enumerate All Verify Questions), Phase 2 (Anchor-Orthogonality),
Phase 3 (Non-Anchor Pairwise), Phase 4 (Revision and Resolution); SCAN ORDERING GATE
confirmed (all six criterion-annotated items checked); canonical sequence Phase 1→2→3→4
verified; no phases merged; Phase 4 complete before any YAML written

Gap artifact (C-39/C-44): INERTIA-GAP ANALYSIS block with formal GAP-{slug} identifiers
written before any expert was named in Phase 2

Expert sourcing (C-40/C-45): every expert has a POSITIVE SOURCING statement citing the
specific GAP-{slug} identifier and domain vocabulary term used in the name, embedded inline
in the derivation record

Provenance chains declared and verified (new): PROVENANCE-CHAIN DECLARATION written in Phase 0
with all three chains; Chain A (inertia gap: GAP-ANALYSIS → Diagnosis Card → YAML field)
traced per domain expert; Chain B (orthogonality: scan + anchor → Diagnosis Card → YAML
field) traced per non-anchor role; Chain C (status-quo claim → ANCHOR-CARD frame →
REGISTRY.md inertia_surface) traced to Phase 6 output

Contract violations (C-29/C-33): `collaborates_with` section in every YAML file includes
CONTRACT VIOLATION (type 1) — PHANTOM comment [C-29] and CONTRACT VIOLATION (type 2) —
UNIVERSALIST comment [C-29]; labels mirrored in template at write site [C-33]; phantom
check confirmed for every collaborates_with list; per-file checklist items carry [C-29/C-33]
criterion-ID annotations [C-49]
