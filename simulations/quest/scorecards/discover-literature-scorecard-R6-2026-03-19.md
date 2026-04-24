**Round 6 scorecard written.** Here is the summary:

---

## discover-literature R6 -- Results

| Rank | Variation | Raw | C-20 | C-21 |
|------|-----------|-----|------|------|
| 1 | **V-04** Lifecycle Tokens | **155** | PASS | PASS |
| 1 | **V-05** Full Synthesis | **155** | PASS | PASS |
| 3 | **V-01** Baseline | 150 | FAIL | PASS |
| 3 | **V-02** Conversational | 150 | FAIL | PASS |
| 3 | **V-03** Inertia Front-Loading | 150 | FAIL | PASS |

**Top score: 155/155. All essential PASS. v6 ceiling reached.**

### Key findings

**C-21 PASS across all five variations** -- All R6 variations inherit the dual typed schema design from R5 V-04/V-05. v6 simply formalizes the +5 pts reward. Minimum score floor jumps from 145 (R5) to 150 (R6).

**C-20 is token-agnostic (V-04 -- the critical experiment PASSES)** -- `PHASE 2 COMPLETE: (C-09+C-16)` + `PHASE 3 COMPLETE: (C-13+C-16)` satisfies C-20 without the canonical `THRESHOLD NOT MET:` + `RECOVERY NOTE:` pair. Any two tokens with explicit condition-(c) PASS annotations covering 3 distinct criteria qualifies. The rubric has no implicit token constraint.

**Lifecycle tokens are a design improvement** -- `THRESHOLD NOT MET:` instruments only the failure path; `PHASE 2 COMPLETE:` fires unconditionally at the phase boundary, making threshold compliance checkable in both the success and failure cases. Superior observability design over the canonical token.

**C-21 is structure-dependent, not label-dependent (V-02)** -- Renaming `OBLIGATION A/B` to `RULE 1/2` does not break C-21. The `Token/Schema/Fields/Required when/Unacceptable` block structure and verbatim field name propagation are what C-21 measures.

```json
{"top_score": 155, "all_essential_pass": true, "new_patterns": ["C-20 is token-agnostic: any two named tokens each carrying explicit condition-(c) PASS annotations covering 3 distinct aspirational criteria satisfies C-20 -- the canonical THRESHOLD NOT MET:/RECOVERY NOTE: pair is not required; PHASE 2 COMPLETE:/PHASE 3 COMPLETE: is an independent valid path confirmed by V-04", "Lifecycle completion tokens as superior observability: PHASE N COMPLETE: tokens fire unconditionally at phase boundaries regardless of success/failure state, making compliance checkable in the happy path as well as the failure path -- structural improvement over THRESHOLD NOT MET: which instruments only the failure case"]}
```
Typed token schema block | **PASS** | OBLIGATION B: full Token/Schema/Fields/Required when/Unacceptable for TIER EMPTY:; {why_no_sources_qualified} and {search_that_would_address_gap} appear verbatim in all four Phase 3 tier instructions. C-17 PASS (prerequisite met). |
| C-20 | Dual multi-criterion token synthesis | **FAIL** | C-18 PASS (prerequisite met). THRESHOLD NOT MET: annotation describes C-09+C-16 without explicit "C-09 PASS. C-16 PASS." Condition (c) fails. RECOVERY NOTE: annotation same pattern. Same as R5 V-04 FAIL on C-20. |
| C-21 | Symmetric dual-obligation typed schema | **PASS** | OBLIGATION A: full typed schema (Token/Schema/Fields/Required when/Unacceptable) for RECOVERY NOTE:; {field_name}, {title_fragment}, {outcome} verbatim in Phase 2. OBLIGATION B: full typed schema for TIER EMPTY:; {tier_name}, {why_no_sources_qualified}, {search_that_would_address_gap} verbatim in Phase 3 tier instructions. Symmetric dual-schema contract confirmed. C-19 PASS (prerequisite met). |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: C-09..C-19 PASS (11 x 5 = 55) + C-20 FAIL + C-21 PASS (5)
**Raw score: 150/155** | Composite: 100 (capped) | All essential pass: YES | Golden: YES

---

### V-02 -- Conversational Register With Dual Schemas

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01..C-08 | Essential + Recommended | **PASS** | Conversational phrasing does not affect structural completeness |
| C-09..C-17 | (same structural profile as V-01) | **PASS** | RULE 1 / RULE 2 = OBLIGATION A / B renamed; schema blocks structurally identical; Phase 2/3 enforcement identical |
| C-18 | Multi-criterion token reuse | **PASS** | THRESHOLD NOT MET: annotation: "it makes the threshold shortfall visible in the body without requiring YAML parsing, and it adds a third named gate token" -- dual function described. RECOVERY NOTE: annotation: "it makes your recovery step auditable in the body without re-running the search, and it adds a fourth named gate token" -- dual function described. Description-based naming accepted per R5 precedent. |
| C-19 | Typed token schema block | **PASS** | RULE 2 (OBLIGATION B) has full Token/Schema/Fields/Required when/Unacceptable for TIER EMPTY:; {why_no_sources_qualified}, {search_that_would_address_gap} verbatim in all four Phase 3 TIER EMPTY: templates. C-17 PASS. |
| C-20 | Dual multi-criterion token synthesis | **FAIL** | Annotation paragraphs describe dual purpose but do not state "C-NN PASS". Condition (c) fails for both tokens. Same gap as V-01. |
| C-21 | Symmetric dual-obligation typed schema | **PASS** | RULE 1 (OBLIGATION A) typed schema for RECOVERY NOTE:; {field_name}, {title_fragment}, {outcome} verbatim in Phase 2. RULE 2 (OBLIGATION B) typed schema for TIER EMPTY:; variables verbatim in Phase 3. C-21 is a structural criterion -- phrasing register (RULE 1/2 vs. OBLIGATION A/B) is irrelevant. Schema blocks present and symmetric regardless of surrounding prose voice. C-19 PASS (prerequisite met). |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: C-09..C-19 PASS (11 x 5 = 55) + C-20 FAIL + C-21 PASS (5)
**Raw score: 150/155** | Composite: 100 (capped) | All essential pass: YES | Golden: YES

**Confirmed hypothesis**: C-21 is structure-dependent, not register-dependent. Schema blocks in conversational voice earn C-21 without change.

---

### V-03 -- Inertia Front-Loading

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01..C-08 | Essential + Recommended | **PASS** | Front-loading inertia to Phase 1 adds structure; all required outputs preserved |
| C-09..C-17 | (same structural profile as V-01) | **PASS** | Contract section identical to V-01; Phase 2/3 enforcement identical |
| C-14 | Inertia guard on PROCEED | **PASS** | Inertia scenario committed before any search (Phase 1 INERTIA COMMITMENT). Phase 4 becomes verification against the commitment. INERTIA SCENARIO: and INERTIA RISK: tokens present in Phase 4. C-14 satisfied by both gate and verification block. |
| C-16 | Template-label checkability | **PASS** | INERTIA SCENARIO: appears in two places (Phase 1 + Phase 4). Additional named token strengthens C-16. |
| C-18 | Multi-criterion token reuse | **PASS** | Same THRESHOLD NOT MET: + RECOVERY NOTE: annotations as V-01. |
| C-19 | Typed token schema block | **PASS** | Identical OBLIGATION A + OBLIGATION B typed schemas as V-01. |
| C-20 | Dual multi-criterion token synthesis | **FAIL** | Same gap as V-01 -- description-based without explicit "C-NN PASS". Condition (c) fails. |
| C-21 | Symmetric dual-obligation typed schema | **PASS** | Contract section identical to V-01: both OBLIGATION A and OBLIGATION B full typed schema blocks. Field names verbatim in Phase 2 and Phase 3. Inertia front-loading is orthogonal to contract schema structure. C-19 PASS (prerequisite met). |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: C-09..C-19 PASS (11 x 5 = 55) + C-20 FAIL + C-21 PASS (5)
**Raw score: 150/155** | Composite: 100 (capped) | All essential pass: YES | Golden: YES

---

### V-04 -- Lifecycle Emphasis: Phase Completion Tokens (CRITICAL EXPERIMENT)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01..C-08 | Essential + Recommended | **PASS** | Phase completion tokens add structure; all required outputs preserved |
| C-09..C-17 | (same structural profile as V-01) | **PASS** | Contract section identical to V-01; Phase 2/3 enforcement identical |
| C-18 | Multi-criterion token reuse | **PASS** | Three independent paths: (1) THRESHOLD NOT MET: annotation names C-09+C-16 by description (R5 precedent). (2) PHASE 2 COMPLETE: annotation: "source count and threshold are co-located and checkable without parsing frontmatter (C-09 PASS), and it adds a fifth named gate token for template-label checkability (C-16 PASS)" -- explicit. (3) PHASE 3 COMPLETE: annotation: "(C-13 PASS), and it adds a sixth named gate token for template-label checkability (C-16 PASS)" -- explicit. C-18 satisfied by multiple independent tokens. |
| C-19 | Typed token schema block | **PASS** | Both OBLIGATION A and OBLIGATION B typed schemas present, identical to V-01. |
| C-20 | Dual multi-criterion token synthesis | **PASS** | C-18 PASS (prerequisite met). PHASE 2 COMPLETE: annotation: (a) contextually names PHASE 2 COMPLETE:, (b) lists C-09 + C-16, (c) explicitly confirms "C-09 PASS... C-16 PASS" -- all three conditions met. PHASE 3 COMPLETE: annotation: (a) contextually names PHASE 3 COMPLETE:, (b) lists C-13 + C-16, (c) explicitly confirms "C-13 PASS... C-16 PASS" -- all three conditions met. Two distinct tokens. Three distinct criteria total: C-09, C-13, C-16. C-20 pass condition fully satisfied. C-20 is confirmed token-agnostic: THRESHOLD NOT MET: + RECOVERY NOTE: canonical pair is not required. |
| C-21 | Symmetric dual-obligation typed schema | **PASS** | Contract section identical to V-01: both OBLIGATION A and OBLIGATION B full typed schema blocks. {field_name}, {title_fragment}, {outcome} verbatim in Phase 2; {tier_name}, {why_no_sources_qualified}, {search_that_would_address_gap} verbatim in Phase 3. Lifecycle tokens are orthogonal to contract schema structure. C-19 PASS (prerequisite met). |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: C-09..C-21 all PASS (13 x 5 = 65)
**Raw score: 155/155** | Composite: 100 (capped) | All essential pass: YES | Golden: YES

**Critical experiment result: C-20 PASS. C-20 is confirmed token-agnostic.**

---

### V-05 -- Full Synthesis (Dual Typed Schemas + C-20 Explicit PASS + Lifecycle Tokens)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01..C-08 | Essential + Recommended | **PASS** | Inherited from R5 V-05 |
| C-09..C-20 | All aspirational through C-20 | **PASS** | Inherited from R5 V-05 (scored 150/150 -- all 12 v5 criteria PASS). THRESHOLD NOT MET: explicit "C-09 PASS. C-16 PASS." RECOVERY NOTE: explicit "C-12 PASS. C-16 PASS." Dual typed schemas for both obligations. Lifecycle tokens add a second independent C-20 path (PHASE 2 COMPLETE: + PHASE 3 COMPLETE:). |
| C-21 | Symmetric dual-obligation typed schema | **PASS** | Both OBLIGATION A and OBLIGATION B retain full typed schema blocks from R5 V-05. {field_name}, {title_fragment}, {outcome} verbatim in Phase 2; {tier_name}, {why_no_sources_qualified}, {search_that_would_address_gap} verbatim in Phase 3. C-21 is the additive R6 gain (+5 pts over R5 V-05 score of 150). C-19 PASS (prerequisite met). |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: C-09..C-21 all PASS (13 x 5 = 65)
**Raw score: 155/155** | Composite: 100 (capped) | All essential pass: YES | Golden: YES

---

### Ranking

| Rank | Variation | Raw | C-18 | C-19 | C-20 | C-21 | Differentiator |
|------|-----------|-----|------|------|------|------|----------------|
| 1 | **V-04** Lifecycle Tokens | **155** | PASS | PASS | PASS | PASS | Proves C-20 is token-agnostic; PHASE N COMPLETE: tokens fire unconditionally at phase boundary -- superior observability to THRESHOLD NOT MET: which instruments only failure |
| 1 | **V-05** Full Synthesis | **155** | PASS | PASS | PASS | PASS | Two independent C-20 paths (canonical pair + lifecycle pair); maximum redundancy and holistic design |
| 3 | **V-01** Baseline | **150** | PASS | PASS | FAIL | PASS | C-21 confirmed on R5 V-04 base; minimum change for +5 pts over R5 |
| 3 | **V-02** Conversational | **150** | PASS | PASS | FAIL | PASS | Confirms C-21 is structure-dependent not register-dependent; survives complete header relabeling |
| 3 | **V-03** Inertia Front-Loading | **150** | PASS | PASS | FAIL | PASS | Confirms C-21 orthogonal to inertia framing axis |

Sub-ranking at 155: V-04 is the cleaner diagnostic (proves C-20 token-agnosticism without canonical annotations). V-05 has greater coverage redundancy. Both are valid reference implementations.
Sub-ranking at 150: V-02 is most informative -- schema blocks surviving complete header relabeling confirms C-21 is a schema-structure criterion, not a label criterion.

---

### What changed from R5 to R6

| Criterion | R5 winners (V-03/V-05 R5) | R6 winners (V-04/V-05 R6) | Change |
|-----------|---------------------------|---------------------------|--------|
| C-21 | Not in v5 rubric | PASS | Both OBLIGATION A and OBLIGATION B typed schema blocks confirmed; dual schemas close asymmetric enforcement surface (+5 pts for all R6 variations) |
| C-20 path | Canonical only (THRESHOLD NOT MET: + RECOVERY NOTE:) | Token-agnostic confirmed | PHASE 2 COMPLETE: + PHASE 3 COMPLETE: is a valid independent C-20 path; C-20 requires explicit condition-(c) confirmation on any two tokens covering 3 distinct criteria |

Score ceiling: 150 (v5 fully satisfied) -> 155 (v6 fully satisfied by V-04 and V-05).

---

### Key findings

**C-21 PASS across all five variations** -- All have dual typed schemas inherited from R5 V-04/V-05 design. v6 formalized the reward for infrastructure already present. All variations reach at least 150/155.

**C-20 is token-agnostic (V-04)** -- PHASE 2 COMPLETE: + PHASE 3 COMPLETE: is a valid independent path. C-20's pass condition specifies structure (two distinct tokens, explicit PASS annotations, 3 distinct criteria) without restricting which tokens qualify. V-04 PASS on C-20 without the canonical pair confirms no implicit token constraint in the rubric.

**Lifecycle tokens are a design improvement** -- THRESHOLD NOT MET: instruments the failure path only; PHASE 2 COMPLETE: instruments both paths unconditionally. The phase boundary is always checkable, not only when the threshold was missed.

**C-21 is structure-dependent, not label-dependent (V-02)** -- Renaming OBLIGATION A/B to RULE 1/2 does not break C-21. The Token/Schema/Fields/Required when/Unacceptable block structure and verbatim field name propagation are what C-21 measures.

```json
{"top_score": 155, "all_essential_pass": true, "new_patterns": ["C-20 is token-agnostic: any two named tokens each carrying explicit condition-(c) PASS annotations covering 3 distinct aspirational criteria satisfies C-20 -- the canonical THRESHOLD NOT MET:/RECOVERY NOTE: pair is not required; PHASE 2 COMPLETE:/PHASE 3 COMPLETE: is an independent valid path confirmed by V-04", "Lifecycle completion tokens as superior observability: PHASE N COMPLETE: tokens fire unconditionally at phase boundaries regardless of success/failure state, making compliance checkable in the happy path as well as the failure path -- structural improvement over THRESHOLD NOT MET: which instruments only the failure case"]}
```
