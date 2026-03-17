Now I have all five variations. Let me score them.

---

# Scorecard — flow-conversation — Round 6 (2026-03-14)
**Rubric version:** v5 | **Variations file:** `flow-conversation-variations-R6-2026-03-14.md`

---

## Scoring Key

| Tier | Criteria | Points each | Total |
|------|----------|-------------|-------|
| Essential | C-01 – C-04 | 15 | 60 |
| Recommended | C-05 – C-07 | 10 | 30 |
| Aspirational | C-08 – C-17 | 1 | 10 |

---

## V-01: Phrasing Register (boundary marker isolation)

**Axis:** SHALL/MUST sequencing only — no `=== DEVELOPER ARTIFACT COMPLETE ===`. C-16 + C-17 fully present.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Dialog path traced as turns | **PASS** | Phase 2 table: Turn/User Input/Trigger Phrase/Topic/Nodes Executed/Agent Response — all turns, no skipping. |
| C-02 | All four defect classes | **PASS** | Phase 3 matrix: Dead end, Infinite loop, Trigger phrase collision, Missing fallback — all four rows mandatory, DEFECT_VERDICT enum. |
| C-03 | Session state tracked | **PASS** | Phase 2 table SESSION_VARIABLES column with scope/changed/held/cleared per transition. T-02 shows `var1=cleared (topic exited)`. |
| C-04 | CS framing | **PASS** | CS vocabulary explicitly mandated; 9-term prohibited list; Phase 0-D CS Vocabulary Binding maps generic terms to CS equivalents. |
| C-05 | Defect reproduction steps | **PASS** | Phase 3: FOUND rows require "exact reproduction sequence required (inputs -> failure mode)." Template: `"[input-1]"->"[input-2]"->dead state`. |
| C-06 | Fallback chain coverage | **PASS** | Phase 4: chain from unrecognized input through Step N to terminal. `FALLBACK_QUALITY: COMPLETE \| LOOPS \| TRUNCATED`. |
| C-07 | Collision disambiguation | **PASS** | Phase 3 collision row: "FOUND: phrase, competing topics, scores, disambiguation strategy + rationale." |
| C-08 | Graph coverage metric | **PASS** | Phase 5: Topics and Trigger phrases visited/total/ratio table. |
| C-09 | Adversarial turn injection | **PASS** | Phase 4: adversarial injection with scenario type, injection turn, node path, variable impact, `ADVERSARIAL_OUTCOME` enum. |
| C-10 | Prohibited vocabulary gate | **PASS** | Phase 0-D CS Vocabulary Binding pre-maps term set. Phase 0-A declares prohibited list. Per-turn PROHIBITED_TERM_SCAN. Phase 6 body scan table with YES\|NO per term. Active enforcement. |
| C-11 | Turn-level conformance verdict | **PASS** | Phase 2 table: `SPEC_CONFORMANCE: CONFORMS \| DEVIATES[CS-SPEC-NN: desc]` on every row. |
| C-12 | Role-separated post-production audit | **FAIL** | Prompt explicitly states "No hard boundary separators appear in this prompt." Rubric C-12: "imperative role-switch phrasing without the hard boundary is insufficient." No `=== DEVELOPER ARTIFACT COMPLETE ===`. |
| C-13 | Typed assertion fields with constrained enums | **PASS** | All verdict positions use constrained enums. Phase 0-A explicitly states "Free-text in DEFECT_VERDICT is a contract violation." |
| C-14 | Contract-first schema authorship | **PASS** | Phase 0-A (Auditor) declares complete schema before Phase 1 (Developer trace). "Developer SHALL NOT begin Phase 1 until this contract is complete." |
| C-15 | Table columns as structural enforcement | **PASS** | Phase 2: 3-column mandatory table. "Blank cell = structural violation." |
| C-16 | Developer domain pre-contract | **PASS** | Phase 0-D precedes Phase 0-A. Developer declares agent topology, trigger phrases, vocab binding, topology spec, session variable invariants — all before Auditor writes schema. "Auditor SHALL NOT begin Phase 0-A until this block is complete." |
| C-17 | Gap-closure annotation | **PASS** | Every phase carries `GAP_CLOSURE_VERDICT: CLOSED \| OPEN` with explicit gap tag. Phase 6 gap-closure audit table with Developer verdict + Auditor verification + REGRESSION option. |

**Score: 99 / 100**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 9/10 (C-12 fails)

---

## V-02: Lifecycle Emphasis — Gap-Closure as Primary Structure

**Axis:** Prompt organized around CS Test Bot gaps (Gap-CS-01 through Gap-CS-07). C-17 is the structural backbone.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Dialog path traced as turns | **PASS** | GAP-CS-01 table: Turn/User Input/Trigger Phrase/Topic/Nodes/SESSION_STATE/Agent Response. "Walk every turn. One row per turn." |
| C-02 | All four defect classes | **PASS** | GAP-CS-02: all four rows, DEFECT_VERDICT enum. Free-text = violation. |
| C-03 | Session state tracked | **PASS** | SESSION_STATE column with scope transitions per turn. T-02 shows topic-exit clearing. |
| C-04 | CS framing | **PASS** | CS vocabulary mandatory; prohibited list enforced; GAP-CS-07 Pre-Work declares topology spec CS-SPEC-01 through CS-SPEC-07. |
| C-05 | Defect reproduction steps | **PASS** | GAP-CS-02: "FOUND: reproduction required." Template shows `"[phrase]"->Topic-A+Topic-B`. |
| C-06 | Fallback chain coverage | **PASS** | GAP-CS-03: chain from unrecognized input to terminal. `FALLBACK_QUALITY: COMPLETE \| LOOPS \| TRUNCATED`. TRUNCATED = gap not closed — tight constraint. |
| C-07 | Collision disambiguation | **PASS** | GAP-CS-02 collision: "disambiguation strategy (entity enrichment \| condition ordering \| trigger phrase refactor) + rationale." |
| C-08 | Graph coverage metric | **PASS** | GAP-CS-05: coverage ratios as fractions with percentages for topics and trigger phrases. |
| C-09 | Adversarial turn injection | **PASS** | GAP-CS-04: injection at Turn T-NN, node path traced, session variable impact stated, `ADVERSARIAL_OUTCOME` enum. |
| C-10 | Prohibited vocabulary gate | **PASS** | GAP-CS-07 Pre-Work declares prohibited list. Per-turn PROHIBITED_TERM_SCAN. Phase GAP-CS-07 CLOSURE body scan table. |
| C-11 | Turn-level conformance verdict | **PASS** | SPEC_CONFORMANCE column on every GAP-CS-01 trace row. |
| C-12 | Role-separated post-production audit | **PASS** | Hard boundary present: `=== DEVELOPER ARTIFACT COMPLETE (Gap-CS-06 through Gap-CS-05) ===` and `=== AUDITOR NOW READS THE COMPLETED ARTIFACT ===`. GAP-CS-07 CLOSURE reads Developer artifact as finished document. |
| C-13 | Typed assertion fields with constrained enums | **PASS** | All verdict positions constrained. DEFECT_VERDICT: FOUND \| CONFIRMED_ABSENT. Free-text = violation. GAP_CLOSURE_VERDICT: CLOSED \| OPEN. |
| C-14 | Contract-first schema authorship | **PASS** | GAP-CS-07 Pre-Work (Auditor) declares complete schema — including all field names, enum values, prohibited terms — before any Developer output. |
| C-15 | Table columns as structural enforcement | **PASS** | GAP-CS-01 trace table: 3 mandatory columns, "blank = violation." |
| C-16 | Developer domain pre-contract | **FAIL** | Closing sequence: (A) Auditor asserts schema → (B) Developer declares domain (Gap-CS-06). Auditor writes schema BEFORE Developer domain declaration. C-16 requires Developer declares domain BEFORE Auditor writes schema: "The Auditor's Phase 0 is written against the Developer's declared domain rather than a hypothetical one." V-02 inverts this order. |
| C-17 | Gap-closure annotation | **PASS** | Entire structure IS gap-closure. Each section closes a named CS Test Bot gap. Gap-closure registry audit in GAP-CS-07 CLOSURE with REGRESSION option. C-17 is the organizing principle. |

**Score: 99 / 100**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 9/10 (C-16 fails)

---

## V-03: Role Sequence — Topology Invariants as Explicit C-16 Layer

**Axis:** Developer Phase 0-D pre-commits INVARIANT-TOPO-NN (design-time structural claims). CONFIRMED_ABSENT defect rows must cite invariant ID. Auditor adds INVARIANT_CONFORMANCE as 4th mandatory column. Hard boundary present.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Dialog path traced as turns | **PASS** | Phase 2 table: 4-column mandatory, all turns, no skipping. |
| C-02 | All four defect classes | **PASS** | Phase 3: all four rows with DEFECT_VERDICT enum + INVARIANT-TOPO cross-reference. |
| C-03 | Session state tracked | **PASS** | Phase 2: SESSION_STATE as 3rd mandatory column. Scope transitions shown at every turn. |
| C-04 | CS framing | **PASS** | CS vocabulary mandatory; prohibited terms listed; topology spec CS-SPEC-01 through CS-SPEC-07 pre-committed in Phase 0-D. |
| C-05 | Defect reproduction steps | **PASS** | Phase 3: FOUND rows require reproduction sequence AND which INVARIANT-TOPO-NN is violated. |
| C-06 | Fallback chain coverage | **PASS** | Phase 4: fallback to terminal + INVARIANT-TOPO-02 check inline. `FALLBACK_QUALITY` enum. |
| C-07 | Collision disambiguation | **PASS** | Phase 3 collision row: "disambiguation strategy (entity enrichment \| condition ordering \| trigger phrase refactor) + rationale." |
| C-08 | Graph coverage metric | **PASS** | Phase 5: Topics and Trigger phrases with ratios. |
| C-09 | Adversarial turn injection | **PASS** | Phase 4: adversarial injection with ADVERSARIAL_OUTCOME enum. |
| C-10 | Prohibited vocabulary gate | **PASS** | Phase 0-D vocabulary binding pre-maps CS term set. Phase 0-A declares prohibited list. Per-turn PROHIBITED_TERM_SCAN (4th column). Phase 6 body scan. |
| C-11 | Turn-level conformance verdict | **PASS** | Phase 2: SPEC_CONFORMANCE on every row. |
| C-12 | Role-separated post-production audit | **PASS** | `=== DEVELOPER ARTIFACT COMPLETE (Phases 0-D through 5) ===` + `=== AUDITOR NOW READS THE COMPLETED ARTIFACT ===`. Phase 6 reads Developer artifact as finished. |
| C-13 | Typed assertion fields with constrained enums | **PASS** | Phase 0-A: all fields with constrained enums. "Free-text in DEFECT_VERDICT = contract violation." INVARIANT_CONFORMANCE: HOLDS \| VIOLATED[NN]. |
| C-14 | Contract-first schema authorship | **PASS** | Phase 0-A (Auditor) declares complete schema — incorporating Phase 0-D topology invariants — before Developer begins Phase 1. "Developer SHALL NOT begin Phase 1 until contract complete." |
| C-15 | Table columns as structural enforcement | **PASS** | Phase 2: 4-column mandatory table. "Blank cell = violation." Phase 0-A explicitly lists all four mandatory columns. |
| C-16 | Developer domain pre-contract | **PASS** | Phase 0-D precedes Phase 0-A. Developer declares agent topology + INVARIANT-TOPO-01 through 04 + INVARIANT-SV-01/02 — all before Auditor writes schema. "Auditor SHALL NOT begin Phase 0-A until complete." The Auditor's Phase 0-A incorporates Phase 0-D invariants directly. |
| C-17 | Gap-closure annotation | **PASS** | Every phase carries GAP_CLOSURE_VERDICT + gap tag. Phase 5 gap-closure covers Gap-R4-05 + Gap-R6-01 extended. Phase 6 gap-closure audit table with REGRESSION. |

**Score: 100 / 100**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 10/10

---

## V-04: Full Synthesis — Bidirectional Pre-Contracts + Topology Invariants + Gap-Closure

**Axis:** Maximum density: bidirectional pre-contracts + topology invariants + per-phase gap-closure + hard boundary + 4-column table + SHALL/MUST. Reference implementation.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Dialog path traced as turns | **PASS** | Phase 2 table: 4-column mandatory, all turns. |
| C-02 | All four defect classes | **PASS** | Phase 3: all four rows, DEFECT_VERDICT enum, INVARIANT-TOPO cross-reference per row. |
| C-03 | Session state tracked | **PASS** | Phase 2: SESSION_STATE as mandatory column with scope/change per turn. |
| C-04 | CS framing | **PASS** | CS vocabulary mandatory ("SHALL appear"); prohibited terms ("PROHIBITED") list. TWO STRUCTURAL LAYERS declared in preamble. |
| C-05 | Defect reproduction steps | **PASS** | Phase 3: FOUND rows require reproduction + INVARIANT-TOPO-NN violated. |
| C-06 | Fallback chain coverage | **PASS** | Phase 4: `FALLBACK_QUALITY` + INVARIANT-TOPO-02 inline check. |
| C-07 | Collision disambiguation | **PASS** | Phase 3 collision: disambiguation strategy required for FOUND rows. |
| C-08 | Graph coverage metric | **PASS** | Phase 5: Topics and Trigger phrases ratios. |
| C-09 | Adversarial turn injection | **PASS** | Phase 4: adversarial injection with ADVERSARIAL_OUTCOME. |
| C-10 | Prohibited vocabulary gate | **PASS** | Phase 0-D vocabulary binding. Phase 0-A prohibited list. Per-turn PROHIBITED_TERM_SCAN. Phase 6 body scan. |
| C-11 | Turn-level conformance verdict | **PASS** | Phase 2: SPEC_CONFORMANCE on every row. |
| C-12 | Role-separated post-production audit | **PASS** | `=== DEVELOPER ARTIFACT COMPLETE (Phases 0-D through 5) ===` + `=== AUDITOR NOW READS THE COMPLETED ARTIFACT ===`. Hard phase-gate present. |
| C-13 | Typed assertion fields with constrained enums | **PASS** | All assertion positions use constrained enums. DISCREPANCY: NONE \| FOUND[SPEC_CONFORMANCE] \| FOUND[INVARIANT_CONFORMANCE] \| FOUND[PROHIBITED_TERM] \| FOUND[MULTIPLE]. |
| C-14 | Contract-first schema authorship | **PASS** | Phase 0-A (Auditor) declares complete schema with all four columns + defect matrix + gap-closure contract before Developer Phase 1. "Developer SHALL NOT begin Phase 1 until complete." |
| C-15 | Table columns as structural enforcement | **PASS** | Phase 2: ALL FOUR columns mandatory; "blank = violation." Phase 0-A enumerates all four. |
| C-16 | Developer domain pre-contract | **PASS** | Phase 0-D (Developer) precedes Phase 0-A (Auditor). Developer pre-commits topology + INVARIANT-TOPO-01 through 04 + INVARIANT-SV invariants. Auditor schema binds Phase 0-D declarations. GAP_CLOSURE_VERDICT: CLOSED \| OPEN [Gap-R6-01]. |
| C-17 | Gap-closure annotation | **PASS** | Per-phase GAP_CLOSURE_VERDICT with gap tags across all 7 phases. Phase 5 covers Gap-R4-05 + Gap-R6-01 extended. Phase 6 GAP_CLOSURE_VERDICT [Gap-R6-02]. Gap-closure audit table with REGRESSION. |

**Score: 100 / 100**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 10/10

---

## V-05: Lifecycle Minimal + Phrasing SHALL-Only + C-16 + C-17

**Axis:** R5 V-02 minimal 3-phase extended with C-16 (Phase 1-A) and C-17 (per-sub-section). No hard boundary marker.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Dialog path traced as turns | **PASS** | Phase 1-C: per-turn table with mandatory columns. "All three columns populated. No turns skipped." |
| C-02 | All four defect classes | **PASS** | Phase 1-D: all four rows with DEFECT_VERDICT enum. |
| C-03 | Session state tracked | **PASS** | Phase 1-C: SESSION_STATE column per turn. |
| C-04 | CS framing | **PASS** | CS vocabulary mandatory; prohibited terms listed. |
| C-05 | Defect reproduction steps | **PASS** | Phase 1-D: FOUND rows require reproduction. Disambiguation if COLLISION FOUND. |
| C-06 | Fallback chain coverage | **PASS** | Phase 1-E: fallback to terminal with FALLBACK_QUALITY enum. |
| C-07 | Collision disambiguation | **PASS** | Phase 1-D: "evidence + disambiguation if FOUND." |
| C-08 | Graph coverage metric | **PASS** | Phase 1-F: Topics and Trigger phrases visited/total/ratio table. |
| C-09 | Adversarial turn injection | **PASS** | Phase 1-E: adversarial with injection turn, path, variable impact, ADVERSARIAL_OUTCOME. |
| C-10 | Prohibited vocabulary gate | **PASS** | Phase 0 declares prohibited list. Per-turn PROHIBITED_TERM_SCAN. Phase 2 body scan. |
| C-11 | Turn-level conformance verdict | **PASS** | Phase 1-C: SPEC_CONFORMANCE on every row. |
| C-12 | Role-separated post-production audit | **FAIL** | Prompt explicitly states "No hard boundary separators." Same diagnostic as V-01. "The Auditor SHALL NOT have produced any Phase 2 output before the Developer's completion declaration" — normative only. Rubric: hard boundary is load-bearing, normative phrasing alone is insufficient. |
| C-13 | Typed assertion fields with constrained enums | **PASS** | All verdict positions constrained. Phase 0 declares all enum values. DEFECT_VERDICT: FOUND \| CONFIRMED_ABSENT. Free-text = violation. |
| C-14 | Contract-first schema authorship | **PASS** | Phase 0 (Auditor) declares complete schema before any Developer output. "Developer SHALL begin Phase 1 now." |
| C-15 | Table columns as structural enforcement | **PASS** | Phase 1-C: 3-column mandatory table with "blank = violation." |
| C-16 | Developer domain pre-contract | **FAIL** | Phase 0 (Auditor) declares schema first. Developer domain arrives in Phase 1-A — AFTER Auditor schema. Phase 0 "acknowledges" the Developer WILL declare domain but writes schema "in anticipation." C-16 explicit: "The Auditor's Phase 0 is written against the Developer's declared domain **rather than a hypothetical one**." V-05 Auditor writes against a hypothetical domain. |
| C-17 | Gap-closure annotation | **PASS** | Each sub-section (1-A through 1-F) carries GAP_CLOSURE_VERDICT + gap tag. Phase 2 gap-closure audit table covers all sub-sections with Auditor verification + REGRESSION. |

**Score: 98 / 100**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 8/10 (C-12 and C-16 fail)

---

## Round 6 Summary

| Variation | Score | All Essential Pass | Fails |
|-----------|-------|--------------------|-------|
| **V-03** | **100** | Yes | — |
| **V-04** | **100** | Yes | — |
| V-01 | 99 | Yes | C-12 (no hard boundary) |
| V-02 | 99 | Yes | C-16 (Auditor-first ordering) |
| V-05 | 98 | Yes | C-12 (no hard boundary), C-16 (Auditor-first) |

---

## Diagnostic Bet Resolution

**V-01 vs V-05 (C-12 with/without full phase structure):**
- V-01 (full phase + no hard marker): C-12 FAIL = 99
- V-05 (minimal + no hard marker): C-12 FAIL = 98

**Outcome: Both fail.** Hard boundary marker is always load-bearing regardless of structural complexity. Normative gating alone — whether in full 7-phase or minimal 3-phase architecture — is insufficient for C-12. This resolves the R5 diagnostic bet cleanly: the `=== DEVELOPER ARTIFACT COMPLETE ===` separator is not cosmetic.

**V-01 vs V-05 (C-16 ordering):**
- V-01: C-16 PASS (Phase 0-D Developer domain precedes Phase 0-A Auditor schema)
- V-05: C-16 FAIL (Phase 0 Auditor schema precedes Phase 1-A Developer domain)

This confirms the Auditor-first / Developer-first ordering matters for C-16 regardless of structural depth.

---

## Excellence Signals (from V-03 and V-04)

These patterns appear in the 100-point variations and are not captured by any existing criterion:

**E-01: Topology invariants as falsifiable CONFIRMED_ABSENT evidence**
The Developer pre-commits INVARIANT-TOPO-NN claims in Phase 0-D — design-time structural assertions about the agent graph (e.g., "all condition nodes have a default branch"), distinct from CS-SPEC runtime behavioral rules. The assertion contract (Phase 0-A) requires CONFIRMED_ABSENT defect rows to cite the specific INVARIANT-TOPO-NN that structurally precludes the defect class. A generic scope statement ("no dead ends found") becomes a falsifiable claim ("INVARIANT-TOPO-04 holds: verified exits for all N topics"). This makes absence assertions testable against pre-committed structure rather than just asserted.

**E-02: Invariant testability map before trace**
Phase 1 (before any trace output) maps which INVARIANT-TOPO-NN claims are verifiable within the simulation's coverage scope, with specific turn references. This prevents over-claiming on out-of-scope invariants and gates the per-turn INVARIANT_CONFORMANCE column before rows are written.

**E-03: Topology invariant cross-audit**
Phase 6 (Auditor) produces a separate per-invariant comparison table — Developer Phase 5 summary verdict vs. Auditor Phase 6 independent verdict — with DISCREPANCY column per invariant. Extends the role-separated audit (C-12) from per-turn conformance to the invariant layer specifically. Developer can mis-summarize an invariant as HOLDS when trace evidence shows VIOLATED; the cross-audit table surfaces this.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Topology invariants as falsifiable CONFIRMED_ABSENT evidence: Developer pre-commits INVARIANT-TOPO-NN design-time structural claims; CONFIRMED_ABSENT defect rows must cite the specific invariant that precludes the defect class, making absence assertions testable rather than scope-bounded", "Invariant testability map before trace: Phase 1 explicitly declares which INVARIANT-TOPO-NN are verifiable within coverage scope before any trace output exists, preventing over-claiming on untestable invariants", "Topology invariant cross-audit: Phase 6 Auditor produces per-invariant comparison table (Developer Phase 5 summary vs Auditor Phase 6 independent verdict) with DISCREPANCY column, extending role separation to the invariant layer"]}
```
