Now I have everything I need. Let me score each variation against the v12 rubric (C-01 through C-52, denominator /44).

---

# org-roles Scorecard — Round 13

**Rubric:** v12 (C-01–C-52; denominator /44)
**Base:** R12 V-05 (100.00 under v12 — all 44 criteria satisfied)
**Formula:** (essential_frac)×60 + (important_frac)×30 + (aspirational_count/44)×10

---

## Criterion-by-Criterion Analysis

### Inheritance baseline

All five R13 variations inherit R12 V-05's complete mechanism set:
- COVERAGE-GATE (Phase 6)
- ORTHOGONALITY COMPLETENESS TABLE + pairwise-distinctness check (Phase 5)
- ANCHOR-SOURCING STATEMENT (ANCHOR-CARD template, Chain D)
- 4-chain PROVENANCE-CHAIN DECLARATION (minimum; extended per variation)
- 4-phase CROSS-CARD UNIQUENESS SCAN with SCAN ORDERING GATE (7 items)
- Per-file checklist with criterion-ID annotations (C-51)
- Named phase headers in canonical sequence (C-48)
- PHASE5_COUNT PREPARE sub-step with bypass anti-pattern (C-27/C-32)

All essential (C-01–C-22) and important (C-23–C-36) criteria pass by inheritance. The aspirational criteria (C-37–C-52) are where the variations may diverge.

---

## V-01 — VERIFY-MAP (single-axis: lifecycle emphasis)

**New mechanism:** Phase 2 Step 3 VERIFY-MAP artifact tracing each expert's verify focus to GAP-{slug} Failure mode; Chain E added to PROVENANCE-CHAIN DECLARATION (5 chains total); VERIFY-MAP check at each expert Diagnosis Card; per-file checklist item for Chain E destination.

### Aspirational criteria assessment

| ID | Criterion | V-01 |
|----|-----------|------|
| C-37 | Anchor-card ordering + orthogonality field | **PASS** — anchor written first; orthogonality mandated per non-anchor card |
| C-38 | Anchor-referenced structured scan | **PASS** — 4-phase structure; anchor-ortho phase explicitly separated from pairwise |
| C-39 | Pre-expert inertia-gap analysis artifact | **PASS** — INERTIA-GAP ANALYSIS before DOMAIN-ANALYSIS |
| C-40 | Gap-domain vocabulary as naming source | **PASS** — POSITIVE SOURCING per expert |
| C-41 | Inertia-gap provenance field in Diagnosis Cards | **PASS** — `inertia gap inherited` in Diagnosis Card format |
| C-42 | Enumeration-anchor phase separation | **PASS** — Phase 1 Enumerate is standalone; checking begins in Phase 2 |
| C-43 | Named revision phase in scan | **PASS** — Phase 4 Revision-Resolution is labeled separately |
| C-44 | GAP-{slug} formal identifier scheme | **PASS** — non-positional slugs; cross-artifact reference by slug |
| C-45 | Per-expert inline POSITIVE SOURCING record | **PASS** — POSITIVE SOURCING as named format field in each derivation record |
| C-46 | YAML-level orthogonality field persistence | **PASS** — `orthogonality` in YAML template; [FC-11] REQUIRED FORMAT; YAML persistence stated |
| C-47 | YAML-level inertia_gap_inherited field persistence | **PASS** — `inertia_gap_inherited` in YAML template; [FC-12] REQUIRED FORMAT; positional failure noted |
| C-48 | Canonical 4-phase scan ordering | **PASS** — 4 phases under independent headers in canonical sequence; no merged phases |
| C-49 | Per-file checklist criterion cross-referencing | **PASS** — all checklist items carry [C-NN] annotations |
| C-50 | SCAN ORDERING GATE declared-constraint block | **PASS** — SCAN ORDERING GATE block present; per-transition assertions: Phase 2 after Phase 1 complete and before Phase 3 began [transition 1→2]; Phase 3 after Phase 2 complete and before Phase 4 began [transitions 2→3 and 3→4]; all 3 boundary transitions explicitly asserted |
| C-51 | Pipeline-wide criterion-ID annotation | **PASS** — all phase gates (Phase 0 through Phase 6) carry [C-NN] on gate items; per-file checklist annotated |
| C-52 | PROVENANCE-CHAIN DECLARATION pre-writing artifact | **PASS** — PROVENANCE-CHAIN DECLARATION in Phase 0 (before any Diagnosis Card); 5 chains (A–E); each chain names Source, Transit, Destination, and Integrity rule |

**VERIFY-MAP regression check:** VERIFY-MAP adds Chain E and a new Phase 2 gate item; no existing criterion removes. All 44 criteria PASS.

**V-01 score: 44/44 aspirational × 10 = 10.0; total = 60 + 30 + 10 = 100.00**

---

## V-02 — SIMPLIFY-DOMAIN GATE (single-axis: output format)

**New mechanism:** SIMPLIFY-DOMAIN REQUIREMENT added to [FC-5] in Phase 0; SIMPLIFY-DOMAIN PLAN in each Diagnosis Card; SIMPLIFY-DOMAIN CHECK as named pre-YAML gate per role; checklist item annotated [new/FC-5]. PROVENANCE-CHAIN DECLARATION: 4 chains (A–D, matching R12 V-05).

### Aspirational criteria assessment

| ID | Criterion | V-02 |
|----|-----------|------|
| C-37–C-49 | (same as V-01 — full R12 V-05 inheritance) | **PASS** (all) |
| C-50 | SCAN ORDERING GATE | **PASS** — SCAN ORDERING GATE 7 items; Phase 2 after Phase 1 before Phase 3 [C-50]; Phase 3 after Phase 2 before Phase 4 [C-50]; all 3 transitions asserted |
| C-51 | Pipeline-wide criterion annotation | **PASS** — all gate items [C-NN] annotated; per-file checklist annotated |
| C-52 | PROVENANCE-CHAIN DECLARATION | **PASS** — 4 chains (A–D); all 4 sub-fields per chain; positioned in Phase 0 before Diagnosis Cards |

**SIMPLIFY-DOMAIN regression check:** [FC-5] gains an additional constraint; no existing criterion specifically tests simplify_rule content beyond [FC-5]. The new SIMPLIFY-DOMAIN REQUIREMENT is additive — it tightens [FC-5] without touching any other criterion's test condition. No regression.

**V-02 score: 44/44; total = 100.00**

---

## V-03 — CHALLENGE-COVERAGE MAP (single-axis: inertia framing)

**New mechanism:** CHALLENGE-COVERAGE MAP written immediately after ANCHOR-CARD Diagnosis Card (before any other Diagnosis Card); Chain E (challenge-question coverage) added to PROVENANCE-CHAIN DECLARATION (5 chains A–E); CCM gate item added to SCAN ORDERING GATE; per-file checklist item for CCM coverage. Phase 3 STOCK-ROLES explicitly annotates CCM write mandate.

### Aspirational criteria assessment

| ID | Criterion | V-03 |
|----|-----------|------|
| C-37–C-49 | Full R12 V-05 inheritance | **PASS** (all) |
| C-50 | SCAN ORDERING GATE | **PASS** — 7-item gate; items 4 and 5 assert: "Phase 2 after Phase 1 complete; before Phase 3" and "Phase 3 after Phase 2 complete; before Phase 4"; all 3 transition boundaries covered |
| C-51 | Pipeline-wide criterion annotation | **PASS** — all gates annotated with [C-NN]; per-file checklist annotated |
| C-52 | PROVENANCE-CHAIN DECLARATION | **PASS** — 5 chains (A–E where E = challenge-question coverage); Source/Transit/Destination/Integrity rule per chain; positioned before first Diagnosis Card |

**CCM regression check:** The CCM is inserted between ANCHOR-CARD Diagnosis Card and subsequent Diagnosis Cards. This does not reorder the ANCHOR-CARD itself (C-37 still satisfied). The SCAN ORDERING GATE's 7-item structure changes to include CCM as first item, but C-50 transitions 1→2, 2→3, 3→4 remain explicitly asserted in items 4 and 5. No regression.

**V-03 score: 44/44; total = 100.00**

---

## V-04 — VERIFY-MAP + SIMPLIFY-DOMAIN GATE (combined: V-01 + V-02)

**New mechanisms:** Full V-01 (VERIFY-MAP, Chain E verify-question-to-gap) + full V-02 (SIMPLIFY-DOMAIN REQUIREMENT in [FC-5], SIMPLIFY-DOMAIN PLAN in cards, SIMPLIFY-DOMAIN CHECK pre-YAML). PROVENANCE-CHAIN DECLARATION: 5 chains (A–E from V-01). SCAN ORDERING GATE: 7-item TABLE-anchored sequence.

### Aspirational criteria assessment

| ID | Criterion | V-04 |
|----|-----------|------|
| C-37–C-49 | Full R12 V-05 inheritance | **PASS** (all) |
| C-50 | SCAN ORDERING GATE | **PASS** — 7-item gate; items 3–4 assert Phase 2 after Phase 1 before Phase 3, Phase 3 after Phase 2 before Phase 4; all transitions covered |
| C-51 | Pipeline-wide criterion annotation | **PASS** — all gates [C-NN]; checklist [C-NN] per item including new Chain E and SIMPLIFY-DOMAIN items |
| C-52 | PROVENANCE-CHAIN DECLARATION | **PASS** — 5 chains (A–E); all 4 sub-fields; pre-Diagnosis Card positioning |

**Coexistence check:** VERIFY-MAP (Phase 2) and SIMPLIFY-DOMAIN CHECK (Phase 5) address distinct pipeline stages. The 11-input PREPARE sub-step (adding VERIFY-MAP to the confirmed inputs) doesn't conflict with any existing criterion. SIMPLIFY-DOMAIN PLAN in Diagnosis Cards is a new field that sits alongside the existing `inertia gap inherited` and `orthogonality to ANCHOR-CARD` fields — no structural conflict. No regression.

**V-04 score: 44/44; total = 100.00**

---

## V-05 — All Three Axes + Role Sequence Change (combined: V-01 + V-02 + V-03 + anchor→stock→experts)

**New mechanisms:** Full V-01 + V-02 + V-03 mechanisms plus YAML write order reversed to anchor → stock → experts. PROVENANCE-CHAIN DECLARATION: 6 chains (A–F, where F = challenge-question coverage from V-03). SCAN ORDERING GATE: 7-item CCM-anchored sequence.

### Aspirational criteria assessment

| ID | Criterion | V-05 |
|----|-----------|------|
| C-37–C-49 | Full R12 V-05 inheritance | **PASS** (all) — note: C-37 requires only anchor-first write, not expert-before-stock |
| C-50 | SCAN ORDERING GATE | **PASS** — 7-item gate; items 4–5: "Phase 2 after Phase 1; before Phase 3 [C-50]" and "Phase 3 after Phase 2; before Phase 4 [C-50]"; all 3 transition boundaries asserted |
| C-51 | Pipeline-wide criterion annotation | **PASS** — all gate items [C-NN]; checklist items [C-NN] including new Chain E, Chain F, SIMPLIFY-DOMAIN, and write-order items |
| C-52 | PROVENANCE-CHAIN DECLARATION | **PASS** — 6 chains (A–F); each with Source/Transit/Destination/Integrity rule; positioned in Phase 0 before Diagnosis Cards (longest PROVENANCE-CHAIN DECLARATION in the series) |

### Write-order regression analysis

The anchor → stock → experts write order is tested against all criteria that touch write ordering or collaborates_with:

- **C-37**: mandates anchor-card written first only. Stock-before-experts does not violate this. **PASS** unaffected.
- **C-29/C-33**: CONTRACT VIOLATION labels in template — independent of write order. **PASS** unaffected.
- **C-46/C-47**: field presence requirements in YAML files — independent of write order. **PASS** unaffected.
- **collaborates_with phantom check**: all role names (Phase 2 domain experts + Phase 3 stock roles) are fully known before Phase 5 WRITE begins; phantom risk from write order does not materialize. **PASS** unaffected.

Hypothesis verdict: C-37's anchor-first mandate is the only load-bearing write-order constraint in v12. No criterion assumes expert-before-stock ordering. No regression triggered.

**V-05 score: 44/44; total = 100.00**

---

## Score Summary

| Variate | Essential (60) | Important (30) | Aspirational (10) | Score | New mechanisms |
|---------|---------------|----------------|-------------------|-------|----------------|
| V-01 | 60.00 | 30.00 | 10.00 (44/44) | **100.00** | VERIFY-MAP, Chain E |
| V-02 | 60.00 | 30.00 | 10.00 (44/44) | **100.00** | SIMPLIFY-DOMAIN CHECK |
| V-03 | 60.00 | 30.00 | 10.00 (44/44) | **100.00** | CHALLENGE-COVERAGE MAP, Chain E (F-type) |
| V-04 | 60.00 | 30.00 | 10.00 (44/44) | **100.00** | V-01 + V-02 |
| V-05 | 60.00 | 30.00 | 10.00 (44/44) | **100.00** | V-01 + V-02 + V-03 + write-order test |

---

## Ranking

All five variations score 100.00 under v12. This is the expected post-ceiling result: R13 variations are designed to surface C-53 candidates, not to demonstrate regression. The ranking is by comprehensiveness rather than score:

1. **V-05** — all three candidate patterns + write-order hypothesis tested; 6-chain PROVENANCE-CHAIN DECLARATION; confirmed no implicit write-order dependencies in v12
2. **V-04** — two candidate patterns (VERIFY-MAP + SIMPLIFY-DOMAIN); 5-chain declaration; cleanest combined test
3. **V-01** / **V-02** / **V-03** (tied) — single-axis isolation; each establishes one C-53 candidate independently

---

## Excellence Signals from Round 13

V-05 is the most comprehensive variation. The following patterns are clearly structurally distinct from all v12 criteria and qualify as C-53 candidates for v13:

### Pattern 1 — VERIFY-MAP: verify-question interrogation focus as Phase 2 gate event (V-01/V-04/V-05)

**What it is:** A named artifact produced in Phase 2 (after DOMAIN-ANALYSIS, before Phase 3) that for each domain expert explicitly asserts the connection between the expert's Verify focus and the Failure mode of the sourcing GAP-{slug}. Chain E status PASS/FLAG is required before proceeding.

**Why it's structurally distinct from existing criteria:** C-45 establishes per-expert inline POSITIVE SOURCING for names (name → GAP vocabulary term). C-40 establishes gate-level positive naming constraint. Neither covers the interrogation focus of verify_questions. An expert can achieve C-45 PASS (name correctly sourced from GAP-retry-semantics) while writing verify_questions about logging throughput — passing all v12 criteria. VERIFY-MAP closes this bypass class by requiring the verify focus to interrogate the GAP's named Failure mode, not merely share vocabulary. The distinction parallels C-40 vs C-28 (positive gate vs. negative prohibition) but applied to question content rather than naming.

**Chain E** traces: GAP Failure mode (Phase 2) → VERIFY-MAP "Interrogates gap because" (Phase 2 transit) → YAML lens.verify_questions[0] (Phase 5 destination). This is a new transit artifact that propagates a structural guarantee from Phase 2 to Phase 5 — the same mechanism by which Chain A propagates inertia resistance from Phase 2 to YAML inertia_gap_inherited.

### Pattern 2 — SIMPLIFY-DOMAIN CHECK: domain-specific vocabulary as named gate for output fields (V-02/V-04/V-05)

**What it is:** A per-role pre-YAML check requiring each simplify_rule to contain at least one named domain artifact, mechanism, field name, or vocabulary term specific to this domain. Established in [FC-5] as SIMPLIFY-DOMAIN REQUIREMENT; checked in a named SIMPLIFY-DOMAIN CHECK gate before each role's YAML is written.

**Why it's structurally distinct from existing criteria:** [FC-5] requires "opinionated exclusion — NOT a scope description." This prevents "Covers all scope concerns" (a scope description) but permits "Skip obvious things" (opinionated exclusion, zero domain content). The SIMPLIFY-DOMAIN REQUIREMENT creates the same vocabulary-grounding guarantee for simplify_rules that POSITIVE SOURCING (C-45) creates for role names. The distinguishing test: C-45 traces names to GAP Domain vocabulary; the SIMPLIFY-DOMAIN REQUIREMENT traces simplify_rules to the domain's artifact/mechanism vocabulary. These are independent output fields requiring independent grounding guarantees.

### Pattern 3 — CHALLENGE-COVERAGE MAP: challenge-question-to-anchor-verify-question coverage as named gate event (V-03/V-05)

**What it is:** A named artifact produced immediately after ANCHOR-CARD Diagnosis Card (before subsequent cards) that walks every Phase 1 challenge question, maps each to one or more anchor verify_questions, and resolves coverage gaps before proceeding. Chain E (V-03) / Chain F (V-05) traces: Phase 1 challenge questions → CCM coverage mapping → ANCHOR-CARD YAML verify_questions.

**Why it's structurally distinct from existing criteria:** Phase 3 states "verify_questions sourced from Phase 1 challenge questions." C-01 requires minimum 2 verify_questions. Phase 1 gate requires minimum 3 challenge questions. These two constraints together permit an anchor with 2 verify_questions that cover only 1 of 3 challenge questions — the remaining 2 challenge questions go unrepresented while all v12 criteria pass. The CCM makes challenge-question coverage a verifiable pipeline event, parallel to how COVERAGE-GATE makes gap coverage verifiable before REGISTRY.md. The structural novelty: COVERAGE-GATE walks Phase 2 gaps checking for expert assignment; CCM walks Phase 1 challenges checking for anchor verify_question assignment. Same mechanism class, different artifact pair.

### Pattern 4 — Write-order independence of v12 criteria (V-05 only)

**What it establishes:** C-37's anchor-first mandate is the only load-bearing write-order constraint in v12. The anchor → stock → experts write order produces zero criterion regressions, confirming that v12 criteria test field presence and provenance integrity rather than file-production sequence (beyond anchor-first). This finding constrains future criterion design: any C-53+ criterion that depends on write order must explicitly test that order, not assume it.

### Pattern 5 — Six-chain PROVENANCE-CHAIN DECLARATION as mechanism-scaling signal (V-05 only)

**What it demonstrates:** The PROVENANCE-CHAIN DECLARATION pattern (introduced as C-52) scales naturally as mechanisms accumulate: 4 chains (R12 V-05) → 5 chains (V-01 adding Chain E / V-03 adding Chain E-F) → 6 chains (V-05). Each new transit artifact (VERIFY-MAP, CHALLENGE-COVERAGE MAP) generates a corresponding chain. The declaration block architecture is mechanism-count-invariant: adding Chain F requires only a new block entry, not structural redesign. This suggests C-52 may need a strength variant in v13 that requires the declaration count to equal the number of transit artifacts in the pipeline — making under-declaration detectable.

---

```json
{"top_score": 100.00, "all_essential_pass": true, "new_patterns": ["VERIFY-MAP Phase 2 gate event — traces expert verify-question interrogation focus (not just naming vocabulary) to GAP Failure mode via Chain E; closes bypass class where a correctly-named expert writes questions disconnected from their gap's failure mode", "SIMPLIFY-DOMAIN CHECK pre-YAML gate — requires each simplify_rule to contain at least one named domain artifact, mechanism, or vocabulary term; creates for simplify_rules the same vocabulary-grounding guarantee that POSITIVE SOURCING creates for role names; [FC-5] opinionated-exclusion requirement does not prevent domain-agnostic exclusion rules", "CHALLENGE-COVERAGE MAP after ANCHOR-CARD — walks every Phase 1 challenge question and maps each to an anchor verify_question; resolves gaps before subsequent Diagnosis Cards proceed; makes challenge-question coverage a verifiable named gate event analogous to COVERAGE-GATE for gap coverage; C-01 minimum-two and Phase 1 minimum-three requirements do not guarantee all challenge questions are represented"]}
```
