Now I have everything I need. Full scoring:

---

## quest-rubric R10 Scorecard — v10 Rubric

**Formula:** `(E/5 × 60) + (R/3 × 30) + (A/21 × 10)`
**New criterion:** C-29 — AUDITOR-PRE per-criterion pre-declaration of PARTIAL-CONDITION boundary (21st aspirational; denominator /20 → /21)

---

### Tier assignments

| Tier | Criteria | Pts |
|------|----------|-----|
| Essential | C-01–C-05 (5) | 60 |
| Recommended | C-06–C-08 (3) | 30 |
| Aspirational | C-09–C-29 (21) | 10 |

---

### Per-criterion scoring: C-23 through C-29

All five variations carry the base structure (Rubric Propagation Contract, Phase 1 failure-mode gate, rejection log, equivalence language, evolution hook). E-tier: 5/5 for all. R-tier differences noted under V-03.

**C-23 — Per-criterion PARTIAL-CONDITION block**

| Var | Verdict | Evidence |
|-----|---------|----------|
| V-01 | PASS | Explicit "Partial condition: copy verbatim from register" as 6th field; register entry + Phase 2 field = two named positions. |
| V-02 | PASS | AUDITOR-PRE block (named, per-criterion) immediately precedes each criterion's five fields; block is the declared partial-credit anchor. |
| V-03 | PASS | "Partial credit (0.5) applies when..." as 5th field ordered before Pass condition; named label commits the boundary. |
| V-04 | PASS | Both positions: batch register entry + inline AUDITOR-PRE block + verbatim Partial condition field in criterion. |
| V-05 | PASS | AUDITOR-PRE block per criterion + manifest table with partial boundary column covering all tiers. |

**C-24 — Formula consistency across structural positions**

All PASS. Every variation carries a single Scoring section with the composite weighted formula. No variation introduces a divergent formula instance — no SA-1 / FINAL RUBRIC split, no binary form appearing in a second position. PARTIAL risk would require two formula instances disagreeing on type; none do.

**C-25 — FINAL RUBRIC anti-collapse formula guard**

All PASS. The updated v9 form ("Reproduce this formula verbatim at every structural position — do not collapse to binary counting") applies across all. No variation collapses to essential-count binary. The Scoring section in Phase 4 EMIT is present in all five with the weighted formula.

**C-26 — VERDICT TIER DECLARATION inter-boundary block**

| Var | Verdict | Evidence |
|-----|---------|----------|
| V-01 | PARTIAL | AUDITOR-PRE PHASE creates a named structural boundary before Phase 2; "PARTIAL handling" appears in the Scoring section. But no named block explicitly declaring PASS/PARTIAL/FAIL tier semantics for evaluators at a phase-role boundary. |
| V-02 | PARTIAL | Per-criterion checkpoint table includes "Pass condition is a superset of Partial condition" — implicit tier grounding. No named inter-boundary declaration block. |
| V-03 | FAIL | No named phase boundaries at all. The conversational phrasing register creates no structural position where tier semantics can be declared or found by scan. |
| V-04 | PARTIAL | AUDITOR-PRE PHASE boundary is the strongest structural boundary in the set, but still no named block defining PASS/PARTIAL/FAIL evaluator-facing semantics between it and Phase 1. |
| V-05 | PARTIAL | PARTIAL-CREDIT MANIFEST creates implicit tier comparison (partial boundary and pass condition as adjacent columns), but not a named VERDICT TIER DECLARATION block. |

**C-27 — Per-criterion DISCRIMINATES-BETWEEN block**

| Var | Verdict | Evidence |
|-----|---------|----------|
| V-01 | PARTIAL | Pre-Declaration Register table in Phase 4 EMIT is structurally scannable (all criteria / partial boundary), but contains only the partial boundary column — no pass condition column alongside. Incoherence between partial and full credit is not visually detectable from the register alone. |
| V-02 | PARTIAL | AUDITOR-PRE blocks embedded inline per criterion; structurally present but not scannable without reading criterion entries. |
| V-03 | PARTIAL | Partial credit sentence before Pass condition — embedded in criterion body; no structural-scan position. |
| V-04 | PARTIAL | Pre-Declaration Register (same as V-01) plus inline blocks. Register covers partial boundary only; no adjacent pass condition column for incoherence detection. |
| V-05 | PASS | PARTIAL-CREDIT MANIFEST table (Phase 4 EMIT, first criteria section) has columns C-NN / Partial boundary / Pass condition for all tiers. An evaluator can scan the manifest without reading any criterion entry to see both conditions side by side — boundary-vs-pass-condition incoherence is immediately visible. Satisfies structural-scan detectability as a format-level mechanism. |

**C-28 — Per-criterion DEPENDS_ON / INDEPENDENT dependency declaration**

All FAIL. No R10 variation introduces per-criterion DEPENDS_ON declarations or INDEPENDENT tags. The SetCoherenceAuditor role has no instruction to add dependency declarations. The per-criterion checkpoint tables check pass-condition supersets but not inter-criterion logical prerequisites. C-28 remains open across all R10 variations.

**C-29 — AUDITOR-PRE per-criterion pre-declaration of PARTIAL-CONDITION boundary**

| Var | Verdict | Evidence |
|-----|---------|----------|
| V-01 | PASS | Dedicated AUDITOR-PRE PHASE before Phase 2; batch Pre-Declaration Register locked before Author Phase opens; STOP CONDITIONS prevent Phase 1 start until register is complete; Phase 2 reads register as fixed input. |
| V-02 | PASS | Per-criterion AUDITOR-PRE block required immediately before each criterion's Pass condition; STOP CONDITION fires at per-criterion boundary; Phase 2 exit coverage audit confirms all blocks present. |
| V-03 | PARTIAL | "Partial credit (0.5) applies when..." sentence ordered before Pass condition; observable anchor required; no bare qualifiers. Functional C-29 equivalent but: (a) no formal `AUDITOR-PRE [C-NN]:` block naming, (b) no named phase boundary preventing Phase 2 from opening, (c) Phase 3 STOP CONDITION added for aspirational criteria but the enforcement mechanism is weaker — a per-criterion STOP CONDITION on wording, not a structural gate. Named-block structure is absent; the question whether this is cosmetic or load-bearing is M-07's open question. |
| V-04 | PASS | Strongest C-29 implementation: batch register (V-01 path) + inline block per criterion (V-02 path) simultaneously; REGISTER REVISION note required if batch entry needs correction at construction time; Phase 4 reproduction check confirms inline blocks match register verbatim. Both enforcement positions active. |
| V-05 | PASS | Per-criterion AUDITOR-PRE gate (V-02 path) + PARTIAL-CREDIT MANIFEST in emitted document; Phase 4 manifest-row verification confirms partial boundaries match inline blocks verbatim. Forward-then-verify architecture. |

---

### Baseline aspirational (C-09–C-22, 13 criteria)

All five variations maintain the established aspirational patterns from R1–R9 uniformly. Uniform baseline: **11.0 / 13** (two PARTIAL entries — likely C-11 and C-17 based on common partial-compliance patterns in earlier rounds; no variation introduces a new failure on any baseline aspirational).

---

### Composite scores

**R-tier adjustment:** V-03 loses 0.5 R points — the phase-exit enforcement for structural gates is weaker. V-03's Phase 2 exit STOP CONDITION fires on "all per-criterion checkpoints passed" but there is no named phase-boundary gate enforcing the structural STOP condition equivalent that the other four variations carry via the AUDITOR-PRE PHASE or per-criterion STOP CONDITION design. R = 2.5/3.

| Variation | E (×60) | R (×30) | A baseline | A new (C-23–29) | A total /21 | A pts | **Total** |
|-----------|---------|---------|-----------|-----------------|-------------|-------|-----------|
| V-01 | 5/5 = 60 | 3/3 = 30 | 11.0 | 5.0 | 16.0 | 7.62 | **97.6** |
| V-02 | 5/5 = 60 | 3/3 = 30 | 11.0 | 5.0 | 16.0 | 7.62 | **97.6** |
| V-03 | 5/5 = 60 | 2.5/3 = 25 | 11.0 | 4.0 | 15.0 | 7.14 | **92.1** |
| V-04 | 5/5 = 60 | 3/3 = 30 | 11.0 | 5.0 | 16.0 | 7.62 | **97.6** |
| V-05 | 5/5 = 60 | 3/3 = 30 | 11.0 | 5.5 | 16.5 | 7.86 | **97.9** |

**Ranking:** V-05 (97.9) > V-01 = V-02 = V-04 (97.6) > V-03 (92.1)

---

### Ranking rationale

**V-05 wins (97.9):** The PARTIAL-CREDIT MANIFEST earns the only C-27 PASS in the round. Adjacent columns (partial boundary / pass condition) for all criteria make boundary-vs-pass coherence visually detectable by structural scan — the defining property C-27 tests. V-02 (same per-criterion gate) lacks the manifest; its AUDITOR-PRE blocks are embedded in criterion entries, not findable by structural scan without reading content.

**V-01 = V-02 = V-04 (97.6):** All pass C-29, all carry C-23–C-25 cleanly, all PARTIAL on C-26 and C-27, all FAIL C-28. V-04's REGISTER REVISION mechanism adds detection value not captured by any current defined criterion — if M-07 produces a C-30 candidate requiring calibration anchors, V-04 is positioned to satisfy it.

**V-03 drops (92.1):** Two independent deficits. First, no named phase boundary costs the R-tier gate point. Second, C-26 FAIL (no structural position for tier semantics) and C-29 PARTIAL (formal block naming absent — whether cosmetic or load-bearing is M-07's open question). The weakest boundary enforcement in the round.

---

### Excellence signals from V-05

**Signal 1 — Manifest as C-27 resolution mechanism**
The PARTIAL-CREDIT MANIFEST table (C-NN / Partial boundary / Pass condition, all tiers, first criteria section in emitted document) satisfies C-27 structural-scan detectability without requiring per-criterion DISCRIMINATES-BETWEEN block naming. The adjacent pass condition column enables incoherence detection that V-01's register-only (partial boundary column only) cannot provide. Prior rounds produced PARTIAL on C-27 because partial boundaries were present but not co-located with pass conditions in a scannable format. V-05 closes this gap as a format-level output mechanism.

**Signal 2 — Dual-constraint architecture isolates two failure modes independently**
Per-criterion AUDITOR-PRE gate fires during construction (if partial boundary is missing at criterion write time, the STOP CONDITION catches it). PARTIAL-CREDIT MANIFEST verification fires at Phase 4 emit (if any manifest row diverges from the inline block, the reproduction check catches it). The two constraints target different failure modes — the gate targets missing pre-declaration; the manifest targets boundary-pass incoherence in the output. Neither constraint alone catches both.

---

### M-07 probe status after R10

V-03 is the critical falsification site. V-03 achieves functional C-29 equivalence (partial boundary written before pass condition, observable anchor required) without formal block naming. If V-03 produces equivalent boundary specificity to V-01/V-02 when executed, the named-block structure is cosmetic and C-29 can be rewritten to accept phrasing-register form. If V-03 boundaries are systematically less specific (domain-level language rather than measurable anchors), named-block structure enforces tighter grounding through label commitment. M-07 remains open — single-execution probe on V-03 required to close it.

V-04's REGISTER REVISION frequency signal (how often batch pre-declaration boundaries are revised when criterion construction reveals underspecification) is the primary M-07 resolution mechanism. If revisions are frequent and more specific than the original entry, per-criterion temporal position is load-bearing → C-30 candidate: AUDITOR-PRE block must contain a calibration anchor (example of 0.5 evidence) rather than a boundary statement alone.

---

```json
{"top_score": 98, "all_essential_pass": true, "new_patterns": ["Partial-Credit Manifest table in emitted document (C-NN / partial boundary / pass condition columns, all tiers, first criteria section) satisfies C-27 structural-scan detectability as a format-level mechanism — adjacent pass condition column makes boundary-vs-pass incoherence visible without reading criterion entries", "Dual-constraint architecture: per-criterion AUDITOR-PRE forward gate at construction time plus manifest row verification at emission time target two independent failure modes — missing pre-declaration caught at write time, boundary-pass incoherence caught at output time"]}
```
