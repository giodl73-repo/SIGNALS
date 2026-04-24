## discover-literature -- Round 4 Scorecard

### Scores

| Rank | Variation | Raw | Golden | C-17 | C-18 |
|------|-----------|-----|--------|------|------|
| 1 | **V-05** Full Synthesis | **140** | YES | PASS | PASS (x2) |
| 2 | **V-04** Minimum-Viable 140 | **140** | YES | PASS | PASS |
| 3 | **V-03** C-17 Schema | **135** | YES | PASS | FAIL |
| 4 | **V-01** C-18 via THRESHOLD NOT MET | **135** | YES | PARTIAL | PASS |
| 5 | **V-02** C-18 via RECOVERY NOTE | **135** | YES | PARTIAL | PASS |

**V-04 and V-05 hit the v4 ceiling: 140/140.**

---

### Scoring Logic

All five variations inherit C-01..C-16 PASS from R3 V-05 = 130 base. The only variables are C-17 and C-18 (5 pts each).

**C-17 analysis:**
- V-01/V-02: PARTIAL. OBLIGATION B still uses prose format with `[reason why no sources qualified]` / `[what additional search would address this gap]` in the contract, but Phase 3 RECENT/CONTRARY/METHODOLOGICAL tiers use abbreviated labels (`[reason]`, `[search suggestion]`, `[gap description]`) -- three of four tiers don't match the contract. Same slot-label mismatch as R3 V-05.
- V-03/V-04/V-05: PASS. Typed schema box replaces prose: `Token:` / `Schema:` / `Fields: {why_no_sources_qualified}` / `{search_that_would_address_gap}` declared authoritative. Phase 3 all four tiers use these exact variable names. Contract and output match.

**C-18 analysis:**
- V-01/V-04/V-05: PASS via THRESHOLD NOT MET: annotation. Annotation paragraph names: "satisfies the depth threshold observability gate... and extends template-label checkability by adding a third named gate token alongside INERTIA SCENARIO: and INERTIA RISK:." Token identified, both criteria named (C-09 + C-16), both PASS.
- V-02/V-05: PASS via RECOVERY NOTE: annotation. Annotation names: "satisfies the anti-placeholder recovery gate... and extends template-label checkability by adding a named recovery gate token alongside the tier tokens and inertia tokens." Token identified, both criteria named (C-12 + C-16), both PASS.
- V-03: FAIL. THRESHOLD NOT MET: exists without annotation. Same failure as R3 V-05.

---

### Key findings

**C-18 is a declaration criterion.** The mechanism (THRESHOLD NOT MET: covering C-09 + C-16) was already present in R3 V-05. V-01 single-axis test confirms: one annotation paragraph -- no structural change -- converts C-18 from FAIL to PASS.

**V-04 is the minimum-viable 140/140 path.** V-03 alone (C-17 only) = 135. V-01 alone (C-18 only) = 135. Together in V-04 = 140.

**Multi-criterion annotation generalizes.** V-02 confirms the pattern works for RECOVERY NOTE: (C-12 + C-16), not just for THRESHOLD NOT MET: (C-09 + C-16). V-05 deploys both instances simultaneously.

---

### Excellence signals

1. **Typed contract schema box** -- `Token:` / `Schema:` / `Fields:` / `Required when:` / `Unacceptable:` with authoritative field names eliminates the slot-label mismatch that caused R3 V-05 C-17 PARTIAL. One structural change, zero ambiguity.

2. **C-18 declaration sufficiency** -- multi-criterion token coverage converts from FAIL to PASS with a single annotation paragraph naming both criteria. Pattern generalizes: THRESHOLD NOT MET: covers C-09+C-16; RECOVERY NOTE: covers C-12+C-16.

```json
{"top_score": 140, "all_essential_pass": true, "new_patterns": ["Typed contract schema box: replacing OBLIGATION B prose format with Token/Schema/Fields/Required-when/Unacceptable block makes field names authoritative and eliminates slot-label mismatch between contract and Phase 3 output -- one structural change closes C-17 completely", "C-18 declaration sufficiency: multi-criterion token coverage is a declaration criterion not a mechanism criterion -- a token already satisfying two criteria converts FAIL to PASS with a single annotation paragraph naming both criteria, no structural change required; pattern generalizes to any token (THRESHOLD NOT MET: covers C-09+C-16, RECOVERY NOTE: covers C-12+C-16)"]}
```
 in the body, not only in frontmatter, making it checkable without parsing YAML) and extends template-label checkability by adding a third named gate token alongside INERTIA SCENARIO: and INERTIA RISK:." Token: THRESHOLD NOT MET:. Criterion 1: C-09 (depth threshold observability). Criterion 2: C-16 (template-label checkability). Both C-09 and C-16 PASS. Pass condition satisfied. |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 9/10 = 45
**Raw score: 135** | Composite: 100 (capped) | All essential pass: YES | Golden: YES

**Confirmed hypothesis**: C-18 is a declaration criterion. The mechanism was already present in R3 V-05 -- THRESHOLD NOT MET: covered two criteria but never named them. Adding one annotation paragraph converts C-18 from FAIL to PASS without structural change.

---

### V-02 -- RECOVERY NOTE as Second Multi-Criterion Token

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Claims extracted before search | PASS | Phase 1 identical |
| C-02 | Citation table present | PASS | 7-column table + RECOVERY NOTE: |
| C-03 | Four-tier literature map built | PASS | TIER ENTRY:/TIER EMPTY: tokens on all four tiers |
| C-04 | Gap analysis recommendation issued | PASS | 5 questions + inertia gate |
| C-05 | Artifact written with required frontmatter | PASS | Phase 5 path + 7 fields |
| C-06 | Contrary evidence mapped to claims | PASS | TIER ENTRY: CONTRARY with Claim # + Phase 5 Q2 |
| C-07 | WebSearch evidence visible | PASS | Per-field recovery + 6 search angles |
| C-08 | High-risk claims flagged | PASS | Phase 4 Q4 HIGH RISK gate |
| C-09 | Depth mode source threshold met | PASS | Depth mode + thresholds + THRESHOLD NOT MET: token + mode: in frontmatter |
| C-10 | Methodological precedent chain | PASS | TIER ENTRY: METHODOLOGICAL year confirmation |
| C-11 | Interrogative obligation satisfied | PASS | Per-source 7-Q block + ENFORCEMENT CONTRACT |
| C-12 | Anti-placeholder recovery executed | PASS | OBLIGATION A + per-field recovery + RECOVERY NOTE: |
| C-13 | Empty-tier acknowledgment present | PASS | OBLIGATION B specifies TIER EMPTY: format |
| C-14 | Inertia guard on PROCEED | PASS | INERTIA SCENARIO:/INERTIA RISK: template labels |
| C-15 | Dual-domain obligation preamble | PASS | Formal ENFORCEMENT CONTRACT; OBLIGATION A and OBLIGATION B both non-optional |
| C-16 | Template-label checkability | PASS (full) | TIER ENTRY:/TIER EMPTY: + RECOVERY NOTE: + THRESHOLD NOT MET: + INERTIA SCENARIO:/INERTIA RISK: |
| C-17 | Contract-to-token binding | **PARTIAL** | Same OBLIGATION B prose as V-01 (no typed schema box). Phase 3 RECENT/CONTRARY/METHODOLOGICAL tiers use abbreviated slot labels not matching the contract declaration. PARTIAL: contract names the token but field names are not authoritative. |
| C-18 | Multi-criterion token reuse | **PASS** | Annotation paragraph after RECOVERY NOTE: explicitly names: "it satisfies the anti-placeholder recovery gate (the recovery step is body-visible and auditable without re-running the search) and extends template-label checkability by adding a named recovery gate token alongside the tier tokens and inertia tokens." Token: RECOVERY NOTE:. Criterion 1: C-12 (anti-placeholder recovery executed). Criterion 2: C-16 (template-label checkability). Both C-12 and C-16 PASS. Pass condition satisfied. Note: THRESHOLD NOT MET: also exists in V-02 but without a dual-criterion annotation -- V-02 closes C-18 via RECOVERY NOTE: alone. |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 9/10 = 45
**Raw score: 135** | Composite: 100 (capped) | All essential pass: YES | Golden: YES

**Confirmed hypothesis**: Multi-criterion token annotation generalizes to recovery gates. RECOVERY NOTE: satisfying C-12 + C-16 is a valid C-18 instance independent of THRESHOLD NOT MET:. The pattern is not tied to threshold tokens specifically.

---

### V-03 -- Contract Schema Box (C-17 Hardening)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Claims extracted before search | PASS | Phase 1 identical |
| C-02 | Citation table present | PASS | 7-column table + RECOVERY NOTE: |
| C-03 | Four-tier literature map built | PASS | TIER ENTRY:/TIER EMPTY: tokens; all four tiers use `{why_no_sources_qualified}` / `{search_that_would_address_gap}` per the schema |
| C-04 | Gap analysis recommendation issued | PASS | 5 questions + inertia gate |
| C-05 | Artifact written with required frontmatter | PASS | Phase 5 path + 7 fields |
| C-06 | Contrary evidence mapped to claims | PASS | TIER ENTRY: CONTRARY with Claim # + Phase 5 Q2 |
| C-07 | WebSearch evidence visible | PASS | Per-field recovery + 6 search angles |
| C-08 | High-risk claims flagged | PASS | Phase 4 Q4 HIGH RISK gate |
| C-09 | Depth mode source threshold met | PASS | Depth mode + thresholds + THRESHOLD NOT MET: token + mode: in frontmatter |
| C-10 | Methodological precedent chain | PASS | TIER ENTRY: METHODOLOGICAL year confirmation |
| C-11 | Interrogative obligation satisfied | PASS | Per-source 7-Q block + ENFORCEMENT CONTRACT; "OBLIGATION B governs all four tiers" in Phase 3 header |
| C-12 | Anti-placeholder recovery executed | PASS | OBLIGATION A explicit unacceptable list + per-field recovery + RECOVERY NOTE: |
| C-13 | Empty-tier acknowledgment present | PASS | OBLIGATION B schema mandates TIER EMPTY: for any empty tier with >= 3 fields |
| C-14 | Inertia guard on PROCEED | PASS | INERTIA SCENARIO:/INERTIA RISK: template labels |
| C-15 | Dual-domain obligation preamble | PASS | Formal ENFORCEMENT CONTRACT; OBLIGATION A and OBLIGATION B; schema box declares "This schema is authoritative -- the field names defined here govern what Phase 3 must produce" |
| C-16 | Template-label checkability | PASS (full) | TIER ENTRY:/TIER EMPTY: + RECOVERY NOTE: + THRESHOLD NOT MET: + INERTIA SCENARIO:/INERTIA RISK: |
| C-17 | Contract-to-token binding | **PASS** | OBLIGATION B replaced with typed schema box: `Token: TIER EMPTY:`, `Schema: TIER EMPTY: {tier_name} -- {why_no_sources_qualified} -- {search_that_would_address_gap}`, `Fields:` with explicit field names, `Required when:`, `Unacceptable:`. Schema declared authoritative. Phase 3 all four tiers use the schema field names verbatim: `{why_no_sources_qualified}` and `{search_that_would_address_gap}`. Contract and output tokens match exactly. C-15 PASS (prerequisite met). |
| C-18 | Multi-criterion token reuse | **FAIL** | THRESHOLD NOT MET: token exists without a dual-criterion annotation. No annotation paragraph naming both criteria satisfied. V-03 is the single-axis C-17 test -- THRESHOLD NOT MET: covers two criteria but the variation never declares this. Identical to R3 V-05 failure mode for C-18. |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 9/10 = 45
**Raw score: 135** | Composite: 100 (capped) | All essential pass: YES | Golden: YES

**Confirmed hypothesis**: Typed schema box closes C-17. The slot-label mismatch that caused R3 V-05 C-17 PARTIAL is eliminated by replacing the prose format description with an authoritative schema where field names carry directly into Phase 3 templates.

---

### V-04 -- Combined: THRESHOLD NOT MET Annotation + C-17 Schema

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Claims extracted before search | PASS | Phase 1 identical |
| C-02 | Citation table present | PASS | 7-column table + RECOVERY NOTE: |
| C-03 | Four-tier literature map built | PASS | TIER ENTRY:/TIER EMPTY: tokens; all tiers use authoritative schema field names |
| C-04 | Gap analysis recommendation issued | PASS | 5 questions + inertia gate |
| C-05 | Artifact written with required frontmatter | PASS | Phase 5 path + 7 fields |
| C-06 | Contrary evidence mapped to claims | PASS | TIER ENTRY: CONTRARY with Claim # + Phase 5 Q2 |
| C-07 | WebSearch evidence visible | PASS | Per-field recovery + 6 search angles |
| C-08 | High-risk claims flagged | PASS | Phase 4 Q4 HIGH RISK gate |
| C-09 | Depth mode source threshold met | PASS | Depth mode + thresholds + THRESHOLD NOT MET: token + mode: in frontmatter |
| C-10 | Methodological precedent chain | PASS | TIER ENTRY: METHODOLOGICAL year confirmation |
| C-11 | Interrogative obligation satisfied | PASS | Per-source 7-Q block + ENFORCEMENT CONTRACT; "OBLIGATION B governs all four tiers" in Phase 3 header |
| C-12 | Anti-placeholder recovery executed | PASS | OBLIGATION A + per-field recovery + RECOVERY NOTE: |
| C-13 | Empty-tier acknowledgment present | PASS | OBLIGATION B schema: "Unacceptable: tier heading with no entries and no TIER EMPTY: token; TIER EMPTY: with fewer than three fields" |
| C-14 | Inertia guard on PROCEED | PASS | INERTIA SCENARIO:/INERTIA RISK: template labels |
| C-15 | Dual-domain obligation preamble | PASS | Formal ENFORCEMENT CONTRACT; OBLIGATION A and OBLIGATION B; schema declared authoritative |
| C-16 | Template-label checkability | PASS (full) | TIER ENTRY:/TIER EMPTY: + RECOVERY NOTE: + THRESHOLD NOT MET: + INERTIA SCENARIO:/INERTIA RISK: |
| C-17 | Contract-to-token binding | **PASS** | V-03 typed schema box: `Token:` / `Schema:` / `Fields:` / `Required when:` / `Unacceptable:` format. Schema declared authoritative. Phase 3 all four tiers use `{why_no_sources_qualified}` and `{search_that_would_address_gap}` verbatim. Contract and output tokens match exactly. C-15 PASS. |
| C-18 | Multi-criterion token reuse | **PASS** | V-01 annotation on THRESHOLD NOT MET: explicitly names: "it satisfies the depth threshold observability gate (the source shortfall is recorded in the body, not only in frontmatter, making it checkable without parsing YAML) and extends template-label checkability by adding a third named gate token alongside INERTIA SCENARIO: and INERTIA RISK:." Token: THRESHOLD NOT MET:. Criterion 1: C-09. Criterion 2: C-16. Both PASS. |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 10/10 = 50
**Raw score: 140** | Composite: 100 (capped) | All essential pass: YES | Golden: YES

**V-04 = minimum-viable 140/140.** V-03 (C-17 only) + V-01 (C-18 only) together are necessary and sufficient. Neither single-axis change alone reaches 140.

---

### V-05 -- Full Synthesis (C-17 Schema + Two C-18 Instances)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Claims extracted before search | PASS | Phase 1 identical |
| C-02 | Citation table present | PASS | 7-column table + RECOVERY NOTE: with dual-criterion annotation |
| C-03 | Four-tier literature map built | PASS | TIER ENTRY:/TIER EMPTY: tokens; all tiers use authoritative schema field names |
| C-04 | Gap analysis recommendation issued | PASS | 5 questions + inertia gate |
| C-05 | Artifact written with required frontmatter | PASS | Phase 5 path + 7 fields |
| C-06 | Contrary evidence mapped to claims | PASS | TIER ENTRY: CONTRARY with Claim # + Phase 5 Q2 |
| C-07 | WebSearch evidence visible | PASS | Per-field recovery + 6 search angles |
| C-08 | High-risk claims flagged | PASS | Phase 4 Q4 HIGH RISK gate |
| C-09 | Depth mode source threshold met | PASS | Depth mode + thresholds + THRESHOLD NOT MET: token + mode: in frontmatter |
| C-10 | Methodological precedent chain | PASS | TIER ENTRY: METHODOLOGICAL year confirmation |
| C-11 | Interrogative obligation satisfied | PASS | Per-source 7-Q block + ENFORCEMENT CONTRACT; schema preamble closes "if unknown" / "if none found" escape hatches |
| C-12 | Anti-placeholder recovery executed | PASS | OBLIGATION A + per-field recovery + RECOVERY NOTE: (annotated as recovery gate token) |
| C-13 | Empty-tier acknowledgment present | PASS | OBLIGATION B schema mandates TIER EMPTY: with >= 3 fields for any empty tier |
| C-14 | Inertia guard on PROCEED | PASS | INERTIA SCENARIO:/INERTIA RISK: template labels |
| C-15 | Dual-domain obligation preamble | PASS | Formal ENFORCEMENT CONTRACT; OBLIGATION A and OBLIGATION B; schema declared authoritative with "the field names defined here govern what Phase 3 must produce" |
| C-16 | Template-label checkability | PASS (full) | TIER ENTRY:/TIER EMPTY: + RECOVERY NOTE: + THRESHOLD NOT MET: + INERTIA SCENARIO:/INERTIA RISK: -- four annotated gate tokens; the two C-18 annotations further document each token's dual role |
| C-17 | Contract-to-token binding | **PASS** | V-03 typed schema box inherited. Schema declared authoritative. Phase 3 all four tiers use schema field names verbatim. Contract and output tokens match. C-15 PASS. |
| C-18 | Multi-criterion token reuse | **PASS** | Two independent C-18 instances: (1) THRESHOLD NOT MET: annotation -- "satisfies the depth threshold observability gate... and extends template-label checkability" -- Token: THRESHOLD NOT MET:, Criterion 1: C-09, Criterion 2: C-16, both PASS. (2) RECOVERY NOTE: annotation -- "satisfies the anti-placeholder recovery gate... and extends template-label checkability by adding a fourth named gate token alongside THRESHOLD NOT MET:, INERTIA SCENARIO:, and INERTIA RISK:" -- Token: RECOVERY NOTE:, Criterion 1: C-12, Criterion 2: C-16, both PASS. Two instances: if one were rejected on a technicality, the other independently satisfies C-18. |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 10/10 = 50
**Raw score: 140** | Composite: 100 (capped) | All essential pass: YES | Golden: YES

---

### Ranking

| Rank | Variation | Raw | Composite | Golden | C-17 | C-18 | Differentiator |
|------|-----------|-----|-----------|--------|------|------|----------------|
| 1 | **V-05** Full Synthesis | **140** | 100 | YES | PASS | PASS (x2) | Two C-18 instances confirms pattern is repeatable; RECOVERY NOTE: as fourth annotated gate token extends C-16 documentation |
| 2 | **V-04** Minimum-Viable 140 | **140** | 100 | YES | PASS | PASS | Minimum-change 140/140 path; confirms V-01 + V-03 are necessary and sufficient together |
| 3 | **V-03** C-17 Schema | **135** | 100 | YES | PASS | FAIL | Typed schema box closes C-17; single-axis confirms schema is the correct approach |
| 4 | **V-01** C-18 via THRESHOLD NOT MET | **135** | 100 | YES | PARTIAL | PASS | Canonical C-18 token; single-axis confirms C-18 is a declaration-only criterion |
| 5 | **V-02** C-18 via RECOVERY NOTE | **135** | 100 | YES | PARTIAL | PASS | Secondary C-18 instance; confirms multi-criterion annotation generalizes to recovery gates |

Sub-ranking within 135 group: V-03 ranks above V-01 because C-17 has a harder dependency chain (requires C-15) and the typed schema is a more architecturally significant change than a declaration annotation. V-01 ranks above V-02 because THRESHOLD NOT MET: is the canonical C-18 example cited in the rubric text; RECOVERY NOTE: is a valid second instance but secondary.

Sub-ranking within 140 group: V-05 ranks above V-04 because V-05 demonstrates multi-criterion token design as a repeatable pattern with two independent instances; V-04 has the minimum viable single instance. V-05 also documents RECOVERY NOTE: explicitly as "fourth named gate token" alongside the three from V-04, extending C-16 coverage semantics.

---

### What changed from R3 to R4

| Criterion | R3 winner (V-05 R3) | R4 winner (V-05) | Change |
|-----------|---------------------|-----------------|--------|
| C-17 | PARTIAL (slot-label mismatch in 3 of 4 tiers) | PASS | Typed contract schema box with authoritative field names; Phase 3 templates use schema variables verbatim |
| C-18 | FAIL (mechanism present, never declared) | PASS | Annotation paragraph naming both criteria satisfied by THRESHOLD NOT MET: (+ RECOVERY NOTE: in V-05) |

Score ceiling: 130 (v3 fully satisfied) -> 140 (v4 fully satisfied by V-04 and V-05).

---

### Excellence Signals

**From V-04 and V-05 -- the top scorers:**

1. **Typed contract schema upgrades C-17** -- replacing OBLIGATION B's prose format description with a structured schema box (`Token:` / `Schema:` / `Fields:` / `Required when:` / `Unacceptable:`) eliminates the slot-label mismatch. Schema field names (`{why_no_sources_qualified}`, `{search_that_would_address_gap}`) are declared authoritative and carry verbatim into Phase 3 tier templates. One structural change, zero ambiguity.

2. **C-18 is a declaration criterion** -- the multi-criterion token mechanism was already present in R3 V-05 (THRESHOLD NOT MET: covered C-09 + C-16) but never named. Adding a single annotation paragraph identifying the token and naming both criteria converts C-18 from FAIL to PASS with no structural change. V-01 single-axis test confirms: declaration alone is sufficient. V-02 confirms: the pattern generalizes to recovery gates (RECOVERY NOTE: covering C-12 + C-16).

```json
{"top_score": 140, "all_essential_pass": true, "new_patterns": ["Typed contract schema box: replacing OBLIGATION B prose format with Token/Schema/Fields/Required-when/Unacceptable block makes field names authoritative and eliminates slot-label mismatch between contract and Phase 3 output -- one structural change closes C-17 completely", "C-18 declaration sufficiency: multi-criterion token coverage is a declaration criterion not a mechanism criterion -- a token already satisfying two criteria converts FAIL to PASS with a single annotation paragraph naming both criteria, no structural change required; pattern generalizes to any token (THRESHOLD NOT MET: covers C-09+C-16, RECOVERY NOTE: covers C-12+C-16)"]}
```
