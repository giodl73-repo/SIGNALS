**Round 5 scorecard written.** Here is the summary:

---

## discover-literature R5 -- Results

| Rank | Variation | Raw | C-19 | C-20 |
|------|-----------|-----|------|------|
| 1 | **V-05** Full Synthesis | **150** | PASS (x2) | PASS |
| 1 | **V-03** C-20 Full Declaration | **150** | PASS | PASS |
| 3 | **V-02** C-20 Partial | 145 | PASS | FAIL |
| 3 | **V-04** Dual Typed Schemas | 145 | PASS | FAIL |
| 5 | **V-01** C-19 Baseline | 140 | PASS | FAIL |

**Top score: 150/150. All essential PASS across all variations. v5 ceiling reached.**

### Key findings

**C-19 confirmed PASS** -- The typed schema block (OBLIGATION B) already present in R4 V-03 earns C-19 immediately. No additional work needed. V-01 proves this is independent of C-18/C-20 infrastructure.

**C-20 is a declaration criterion** -- exact parallel to C-18 in R4. The dual-token mechanism existed in R4 V-05; the gap was that neither annotation explicitly stated "C-NN PASS". Adding those tags to both annotations closes C-20 without structural change. V-02 confirms C-20 is symmetric: one annotation explicit + one implicit = FAIL.

**Minimum-viable 150 = V-03** -- No OBLIGATION A typed schema required. Just "C-09 PASS" / "C-16 PASS" and "C-12 PASS" / "C-16 PASS" appended to existing annotation paragraphs.

**Maximum infrastructure = V-05** -- Dual typed schemas (both obligations) + explicit PASS confirmation = holistic, symmetric enforcement contract. Same score as V-03, superior design.

```json
{"top_score": 150, "all_essential_pass": true, "new_patterns": ["C-20 is a declaration criterion: the dual-token multi-criterion mechanism existed in R4 V-05 but never confirmed PASS status per condition (c); adding 'C-NN PASS' tags to both annotation paragraphs closes the gap without structural change -- exact parallel to how C-18 moved from FAIL to PASS in R4", "Symmetric enforcement contract: extending typed schema block pattern to OBLIGATION A creates Token/Schema/Fields/Required-when/Unacceptable structure for RECOVERY NOTE: in parallel to OBLIGATION B's TIER EMPTY: schema, making the contract holistically self-documenting across both obligations -- design quality upgrade independent of scoring"]}
```
SK: |
| C-17 | Contract-to-token binding | **PASS** | OBLIGATION B typed schema box: `Token: TIER EMPTY:` / `Schema:` / `Fields: {tier_name}, {why_no_sources_qualified}, {search_that_would_address_gap}` / `Required when:` / `Unacceptable:` declared authoritative; Phase 3 uses field names verbatim. Inherited from R4 V-03. |
| C-18 | Multi-criterion token reuse | **FAIL** | No annotation paragraph on any token naming multiple criteria. V-01 is R4 V-03 base -- THRESHOLD NOT MET: exists but no dual-criterion annotation. C-18 requires declaration. |
| C-19 | Typed token schema block | **PASS** | OBLIGATION B has full typed schema block: Token/Schema/Fields/Required when/Unacceptable. Field names `{why_no_sources_qualified}` and `{search_that_would_address_gap}` appear verbatim in all four Phase 3 tier instructions. C-17 PASS (prerequisite met). C-19 is earned by schema precision alone, independent of C-18 annotation infrastructure. |
| C-20 | Dual multi-criterion token synthesis | **FAIL** | Blocked by C-18 FAIL. |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: C-09..C-17 PASS + C-19 PASS, C-18/C-20 FAIL = 9x5 = 45
**Raw score: 140** | Composite: 100 (capped) | All essential pass: YES | Golden: YES

**Confirmed hypothesis**: C-19 is earned by the typed schema block alone, independent of the C-18/C-20 annotation infrastructure. V-01 = R4 V-03 + 5 pts for C-19 = 140. Same ceiling as R4 winner despite FAIL on C-18.

---

### V-02 -- C-20 Partial: One Annotation Explicit (THRESHOLD NOT MET Only)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01..C-16 | (same as R4 V-05) | PASS | Inherited |
| C-17 | Contract-to-token binding | **PASS** | Inherited from R4 V-05 |
| C-18 | Multi-criterion token reuse | **PASS** | THRESHOLD NOT MET: annotation: "satisfies the depth threshold observability gate... -- C-09 PASS) and extends template-label checkability... (C-16 PASS)." Token identified, C-09 + C-16 named and confirmed PASS. Independently sufficient. |
| C-19 | Typed token schema block | **PASS** | OBLIGATION B typed schema block inherited. Field names verbatim in Phase 3. C-17 PASS. |
| C-20 | Dual multi-criterion token synthesis | **FAIL** | C-18 PASS (prerequisite met). THRESHOLD NOT MET: annotation: (a) token named implicitly, (b) C-09+C-16 listed, (c) "C-09 PASS. C-16 PASS." confirmed -- all three conditions met. RECOVERY NOTE: annotation: (a) "This token" names it implicitly, (b) describes C-12+C-16, (c) NO explicit "C-12 PASS" or "C-16 PASS" confirmation -- condition (c) fails. C-20 requires both tokens to satisfy all three conditions. One annotation explicit + one implicit = FAIL. |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: C-09..C-19 all PASS (10x5=50), C-20 FAIL
**Raw score: 145** | Composite: 100 (capped) | All essential pass: YES | Golden: YES

**Key finding**: C-20 is symmetric -- both annotations must explicitly confirm PASS. Partial coverage (one explicit, one implicit) does not satisfy condition (c). V-02 FAIL on C-20 confirms V-03 is necessary.

---

### V-03 -- C-20 Full: Both Annotations Explicit

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01..C-16 | (same as R4 V-05) | PASS | Inherited |
| C-17 | Contract-to-token binding | **PASS** | Inherited from R4 V-05 |
| C-18 | Multi-criterion token reuse | **PASS** | THRESHOLD NOT MET: annotation names C-09 + C-16, both confirmed PASS. Sufficient independently. |
| C-19 | Typed token schema block | **PASS** | OBLIGATION B typed schema block inherited. Field names verbatim in Phase 3. C-17 PASS. |
| C-20 | Dual multi-criterion token synthesis | **PASS** | C-18 PASS (prerequisite met). THRESHOLD NOT MET: annotation: "This token" (contextually THRESHOLD NOT MET:) + C-09 + C-16 + "C-09 PASS. C-16 PASS." -- (a)(b)(c) all satisfied. RECOVERY NOTE: annotation: "This token" (contextually RECOVERY NOTE:) + C-12 + C-16 + "C-12 PASS. C-16 PASS." -- (a)(b)(c) all satisfied. Two distinct tokens. Three distinct criteria: C-09, C-12, C-16. C-20 pass condition fully satisfied. |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: all 12 criteria PASS = 12x5 = 60
**Raw score: 150** | Composite: 100 (capped) | All essential pass: YES | Golden: YES

**Confirmed hypothesis**: C-20 is a declaration criterion. The mechanism (two annotated dual-criterion tokens) existed in R4 V-05. The gap was explicit PASS confirmation per condition (c). Adding "C-NN PASS" tags to both annotations closes C-20 without structural change. V-03 = minimum-viable 150/150 with no OBLIGATION A typed schema needed.

---

### V-04 -- C-19 Extended: Dual Typed Schema Blocks

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01..C-16 | (same as R4 V-05) | PASS | Inherited |
| C-17 | Contract-to-token binding | **PASS** | Now both OBLIGATION A and OBLIGATION B declare typed schema blocks. OBLIGATION A: `Token: RECOVERY NOTE:` / `Schema: RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}` / `Fields:` / `Required when:` / `Unacceptable:`. OBLIGATION B: same as R4 V-05. Both authoritative. C-17 strengthened (names two contract tokens). |
| C-18 | Multi-criterion token reuse | **PASS** | THRESHOLD NOT MET: annotation: "satisfies the depth threshold observability gate... and extends template-label checkability..." Token: THRESHOLD NOT MET:, C-09 + C-16, both PASS. Criteria named by description (same form as R4 V-05 which scored PASS). |
| C-19 | Typed token schema block | **PASS** | Two typed schema blocks. OBLIGATION A: Token/Schema/Fields/Required when/Unacceptable for RECOVERY NOTE:; `{field_name}`, `{title_fragment}`, `{outcome}` appear verbatim in Phase 2 instructions. OBLIGATION B: same as before with TIER EMPTY: schema variables verbatim in Phase 3. C-19 requires at least one -- V-04 has two. Full schema symmetry across both obligations. |
| C-20 | Dual multi-criterion token synthesis | **FAIL** | C-18 PASS (prerequisite met). THRESHOLD NOT MET: annotation: describes C-09+C-16 but no "C-09 PASS" / "C-16 PASS" confirmation -- condition (c) fails. RECOVERY NOTE: annotation: describes C-12+C-16 but no "C-12 PASS" / "C-16 PASS" confirmation -- condition (c) fails. V-04's change is schema structure (V-04 axis), not declaration (V-03 axis). C-20 is declaration-gated; adding a second typed schema does not satisfy condition (c). |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: C-09..C-19 all PASS (10x5=50), C-20 FAIL
**Raw score: 145** | Composite: 100 (capped) | All essential pass: YES | Golden: YES

**Key finding**: Dual typed schemas do not push C-20 past FAIL. C-20 is declaration-gated, not structure-gated. V-04 demonstrates dual schema is a valid design upgrade (symmetric enforcement contract) but independent of the C-20 declaration gap. C-20 requires V-03's PASS confirmation, not V-04's schema extension.

---

### V-05 -- Full Synthesis (Dual Typed Schemas + Explicit PASS Confirmation)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01..C-16 | (same as R4 V-05) | PASS | Inherited |
| C-17 | Contract-to-token binding | **PASS** | Both OBLIGATION A and OBLIGATION B declare typed schema blocks. OBLIGATION A: `Token: RECOVERY NOTE:` with `{field_name}`, `{title_fragment}`, `{outcome}` authoritative. OBLIGATION B: `Token: TIER EMPTY:` with `{tier_name}`, `{why_no_sources_qualified}`, `{search_that_would_address_gap}` authoritative. Maximum contract-to-token precision. |
| C-18 | Multi-criterion token reuse | **PASS** | Two independent C-18 instances: (1) THRESHOLD NOT MET: annotation -- "C-09 PASS" + "C-16 PASS" explicitly confirmed. (2) RECOVERY NOTE: annotation -- "C-12 PASS" + "C-16 PASS" explicitly confirmed. Both instances independently satisfy C-18. |
| C-19 | Typed token schema block | **PASS** | Dual typed schema blocks (from V-04). Both OBLIGATION A and OBLIGATION B use Token/Schema/Fields/Required when/Unacceptable format. Authoritative field names appear verbatim in Phase 2 (RECOVERY NOTE:) and Phase 3 (TIER EMPTY:) output. Strongest possible C-19 coverage. |
| C-20 | Dual multi-criterion token synthesis | **PASS** | C-18 PASS (prerequisite met). THRESHOLD NOT MET: annotation: (a) contextually named, (b) C-09+C-16, (c) "C-09 PASS. C-16 PASS." -- (a)(b)(c) all satisfied. RECOVERY NOTE: annotation: (a) contextually named, (b) C-12+C-16, (c) "C-12 PASS. C-16 PASS." -- (a)(b)(c) all satisfied. Two distinct tokens. Three distinct criteria (C-09, C-12, C-16). C-20 fully satisfied. |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: all 12 criteria PASS = 12x5 = 60
**Raw score: 150** | Composite: 100 (capped) | All essential pass: YES | Golden: YES

**V-05 = maximum v5 infrastructure.** Dual typed schemas (V-04) + explicit PASS confirmation (V-03) are orthogonal improvements. V-03 is the minimum-viable 150; V-05 is the holistically designed 150 with symmetric enforcement across both obligations.

---

### Ranking

| Rank | Variation | Raw | C-17 | C-18 | C-19 | C-20 | Differentiator |
|------|-----------|-----|------|------|------|------|----------------|
| 1 | **V-05** Full Synthesis | **150** | PASS | PASS (x2) | PASS (x2) | PASS | Dual typed schemas + explicit PASS on both annotations; symmetric enforcement contract; holistic design over minimum-viable |
| 1 | **V-03** C-20 Full Declaration | **150** | PASS | PASS | PASS | PASS | Minimum-viable 150; confirms C-20 is a declaration criterion; no OBLIGATION A schema needed for ceiling |
| 3 | **V-02** C-20 Partial | **145** | PASS | PASS | PASS | FAIL | One annotation explicit, one implicit; confirms C-20 is symmetric (both must declare) |
| 3 | **V-04** Dual Typed Schemas | **145** | PASS | PASS | PASS | FAIL | Dual schemas without explicit PASS; confirms C-20 is declaration-gated not structure-gated |
| 5 | **V-01** C-19 Baseline | **140** | PASS | FAIL | PASS | FAIL | Confirms C-19 earns 5 pts independent of C-18/C-20; same ceiling as R4 winner despite FAIL on C-18 |

Sub-ranking at 150: V-05 edges V-03 on design quality (symmetric contract infrastructure, two C-18 instances), though both score identically. V-05 is the recommended reference implementation.
Sub-ranking at 145: V-02 and V-04 equal by score. V-04 ranks slightly higher as a design advance (dual typed schemas) that compounds if future rubric versions reward dual-obligation schema coverage.

---

### What changed from R4 to R5

| Criterion | R4 winner (V-05 R4) | R5 winner (V-05 R5) | Change |
|-----------|---------------------|---------------------|--------|
| C-19 | Unconfirmed (earned, not measured) | PASS | Typed schema block already present in OBLIGATION B; C-19 formalizes the reward |
| C-20 | FAIL (mechanism present, PASS never declared) | PASS | Adding "C-NN PASS" to both annotation paragraphs closes the declaration gap; exact parallel to how C-18 moved from FAIL to PASS in R4 |

Score ceiling: 140 (v4 fully satisfied) -> 150 (v5 fully satisfied by V-03 and V-05).

---

### Excellence Signals

**From V-03 and V-05 -- the top scorers:**

1. **C-20 is a declaration criterion** -- the multi-criterion token infrastructure (two annotated tokens, three distinct criteria) existed in R4 V-05 but never explicitly confirmed PASS status. Adding "C-NN PASS" tags within existing annotation paragraphs converts C-20 from FAIL to PASS without structural change. Exact parallel to C-18's R4 breakthrough.

2. **Symmetric enforcement contract** (V-05) -- extending the typed schema block pattern to OBLIGATION A creates a parallel Token/Schema/Fields/Required when/Unacceptable structure for RECOVERY NOTE: alongside OBLIGATION B's TIER EMPTY: schema. The enforcement contract is now self-documenting for both obligations with identical precision. Design quality upgrade: V-05 scores the same as V-03, but the infrastructure is holistic rather than asymmetric.

```json
{"top_score": 150, "all_essential_pass": true, "new_patterns": ["C-20 is a declaration criterion: the dual-token multi-criterion mechanism existed in R4 V-05 but never confirmed PASS status per condition (c); adding 'C-NN PASS' tags to both annotation paragraphs closes the gap without structural change -- exact parallel to how C-18 moved from FAIL to PASS in R4", "Symmetric enforcement contract: extending typed schema block pattern to OBLIGATION A creates Token/Schema/Fields/Required-when/Unacceptable structure for RECOVERY NOTE: in parallel to OBLIGATION B's TIER EMPTY: schema, making the contract holistically self-documenting across both obligations -- design quality upgrade independent of scoring"]}
```
