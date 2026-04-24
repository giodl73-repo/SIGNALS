# scout-inertia — Scorecard Round 8

## Scoring Framework

**Rubric v8** | 18 active criteria (15 baseline + C-24/C-25/C-26) | Formula: `N/18 × 100`

**Baseline note**: All five variations inherit R7's 100/100 on the original 15 criteria. Per-variation evaluation below focuses on the three new aspirational criteria; baseline criteria are summarized rather than enumerated.

---

## V-01 — Phrasing Register (Formal/Imperative, C-25 Site Annotations, C-26 Verbatim Identity)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-23 (15 active) | **PASS** | Full R7 structure preserved; all prior sections present and structurally complete |
| **C-24** Exact-text quotation | **PASS** | Step 2 reads: "Do not paraphrase — quote the exact text. Label it: NAMED CLAIM: '[exact text of the claim, verbatim from Step 1]'" + [PAIR REQUIRED] pair explicitly distinguishes verbatim-from-STEELMAN vs paraphrase |
| **C-25** Per-site enforcement annotations | **PASS** | Every structural requirement site carries `[PAIR REQUIRED]` inline: Replication Fidelity (3 sites), Switching Cost Protocol (3 sites), Threat Score (1 site), Loss Condition (2 sites), Failure Mode (3 sites), Forward-Looking Risk (1 site), Anchored Rebuttal (3 sites) — 16 annotation sites total |
| **C-26** Manifest-to-header verbatim alignment | **PASS** | Manifest block opens with explicit directive: "Section headers must reproduce these manifest entries character-for-character — no reformatting, no prefix changes" with entries listed in exact header-text form |

**Score: 18/18 = 100.0**

---

## V-02 — Output Format (Pre-Printed Annotated Template, Verbatim-Aligned Manifest Block)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-23 (15 active) | **PASS** | R7 V-02 scored 100/100 on v7; retroactive v8 analysis confirmed C-24/C-25/C-26 already passing |
| **C-24** Exact-text quotation | **PASS** | R8 adds explicit "do not paraphrase" at NAMED CLAIM step; pre-printed template pins NAMED CLAIM anchor to the STEELMAN block above it, eliminating paraphrase drift |
| **C-25** Per-site enforcement annotations | **PASS** | R7 V-02 originated the `[PAIR REQUIRED]` pattern; R8 tightens coverage at any remaining gap sites identified in retroactive analysis |
| **C-26** Manifest-to-header verbatim alignment | **PASS** | R7 V-02's "Section N:" consistent prefix at both manifest and header sites satisfied C-26 retroactively; R8 adds explicit verbatim-identity constraint instruction to make the requirement declarative rather than implicit |

**Score: 18/18 = 100.0**

---

## V-03 — Inertia Framing (COMPETITOR ZERO Adversarial, C-25/C-26 at Synthesis Step)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-23 (15 active) | **PASS** | Adversarial structure maintains all content sections; R7 V-03 scored 100/100 on v7 |
| **C-24** Exact-text quotation | **PASS** | Description confirms C-24 addressed; adversarial role structure naturally surfaces a STEELMAN that can be quoted verbatim at the rebuttal step |
| **C-25** Per-site enforcement annotations | **PARTIAL** | Design adds `[PAIR REQUIRED]` annotations "to synthesis step" only — prior sections (COMPETITOR ZERO analysis, individual loss conditions, failure mode table) may carry structural requirements without per-site annotation markers; R7 V-03 had structural pairs without annotations throughout the non-synthesis body |
| **C-26** Manifest-to-header verbatim alignment | **PARTIAL** | Verbatim constraint applied "at synthesis" where multi-protocol synthesis manifest lives; the COMPETITOR ZERO analysis header block and sub-section headers before synthesis may diverge from any manifest entries in those sections without the same constraint force |

**Score: 16/18 = 88.9**

---

## V-04 — Combined Role Sequence + Lifecycle Emphasis (PROFILE / THREAT / VERDICT, Co-Located Constraint Sentences)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-23 (15 active) | **PASS** | Three-phase lifecycle structure covers all required content areas; R7 V-04 scored 100/100 retroactively on C-24/C-25/C-26 |
| **C-24** Exact-text quotation | **PASS** | One of the three co-located constraint sentences at the THREAT phase boundary explicitly targets C-24; co-location ensures the model reads all three constraints before entering the sections where they govern |
| **C-25** Per-site enforcement annotations | **PASS** | Constraint sentence for C-25 co-located at THREAT phase boundary applies globally to all requirement sites in the THREAT and VERDICT phases; phase-boundary placement means the rule is read before any site is written |
| **C-26** Manifest-to-header verbatim alignment | **PASS** | Constraint sentence for C-26 co-located at same phase boundary; three-phase lifecycle has a natural manifest-to-header alignment surface at the PROFILE/THREAT phase transition where the PROFILE manifest of sub-protocols maps to THREAT section headers |

**Score: 18/18 = 100.0**

---

## V-05 — Full-Stack Template + Pre-Flight Verification Gate (Extended for C-24/C-25/C-26)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-23 (15 active) | **PASS** | Full-stack template plus pre-flight repair loop; R7 V-05 scored 100/100 on v7 and retroactively on C-24/C-25/C-26 |
| **C-24** Exact-text quotation | **PASS** | Pre-flight gate extended with explicit "verbatim quotation scan": verifies NAMED CLAIM text appears unchanged in STEELMAN above before output is accepted; repair required if scan fails |
| **C-25** Per-site enforcement annotations | **PASS** | Pre-flight gate adds "annotation-site count scan": counts `[PAIR REQUIRED]` markers, counts requirement sites, flags mismatch as mandatory repair target; criterion-ID-labeled check (C-25) makes the obligation machine-readable |
| **C-26** Manifest-to-header verbatim alignment | **PASS** | Pre-flight gate adds "manifest-header identity scan": for each manifest entry, confirms corresponding section header reproduces it character-for-character; explicit repair path if any divergence detected |

**Score: 18/18 = 100.0**

---

## Summary

| Variation | C-24 | C-25 | C-26 | Baseline | Total | Score |
|-----------|------|------|------|----------|-------|-------|
| V-01 | PASS | PASS | PASS | 15/15 | 18/18 | **100.0** |
| V-02 | PASS | PASS | PASS | 15/15 | 18/18 | **100.0** |
| V-03 | PASS | PARTIAL | PARTIAL | 15/15 | 16/18 | **88.9** |
| V-04 | PASS | PASS | PASS | 15/15 | 18/18 | **100.0** |
| V-05 | PASS | PASS | PASS | 15/15 | 18/18 | **100.0** |

**Rank:** V-01 = V-02 = V-04 = V-05 (100.0) > V-03 (88.9)

**V-03 failure analysis**: Adding C-25/C-26 constraints "at the synthesis step" is insufficient when the adversarial base structure has requirement sites throughout the COMPETITOR ZERO analysis body. Synthesis-scoped constraint sentences do not retroactively cover sites written in earlier sections. The gap is structural: the constraint must precede all sites it governs, not only the final synthesis.

---

## Excellence Signals

Three patterns from the top-scoring variations that V-03 missed and that are not yet encoded in C-01 through C-23:

1. **Constraint-before-site placement rule**: In V-04, all three new-criterion constraints are co-located at the phase boundary *preceding* the sections where they govern. In V-01, the verbatim-identity directive appears in the manifest block *before* any sections are written. In V-03, constraints were placed at synthesis *after* requirement sites had already been written. The signal: a constraint placed after its governed sites cannot retroactively repair them. Placement precedes coverage.

2. **Criterion-ID-labeled verification scan** (V-05): Naming `C-24`/`C-25`/`C-26` explicitly in the pre-flight gate converts aspirational criteria from "properties to achieve" into "properties to verify and repair." The difference is structural: criterion-ID labels create an audit path by ID, not by property name, enabling mechanical completeness checking without content review.

3. **Character-for-character identity as a manifest-level directive** (V-01, V-02): Placing the verbatim-alignment instruction in the manifest block itself — "Section headers must reproduce these manifest entries character-for-character" — rather than as a general principle elsewhere, binds the constraint to the specific strings being aligned. The model cannot satisfy the directive without reading the manifest entries it must copy, eliminating the category of failures where the model knows the rule but cannot apply it without the reference text.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["constraint-before-site placement: multi-criterion constraint sentences must precede all sites they govern, not only the final synthesis step", "criterion-ID-labeled verification scans convert aspirational criteria from properties-to-achieve into properties-to-verify-and-repair", "manifest-level character-for-character identity directive binds the verbatim-alignment rule to the specific reference strings, eliminating rule-known-but-reference-absent failure mode"]}
```
