# Quest Score — quest-rubric / Round 4

**Rubric version**: v4 | **Date**: 2026-03-16
**Note**: V-03 through V-05 described in variation map but not drafted — scoring V-01 and V-02 only.
**Trace artifact**: placeholder (no ground truth artifact — scoring prompt structure against rubric criteria)

**v4 criteria active**:
- Essential (5): C-01–C-05 (unchanged)
- Recommended (3): C-06–C-08 (unchanged)
- Aspirational (8): C-09–C-11 (v2), C-12–C-14 (v3), C-15 DEFINED HERE (specificity → scoreable criterion), C-16 NEW (required field structural home)

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 8 * 10)
```

PARTIAL = 0.5 credit (consistent with R3 convention).
Golden threshold: all essential criteria PASS AND composite >= 80.

---

## V-01 — Output Format (Schema-First Declaration Block)

### Essential Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | Skill identity declared | PASS | Phase 4 output template has `skill: {skill}` in frontmatter — structurally required before write |
| C-02 | Criteria are testable | PASS | Phase 3 bans "is clear," "seems appropriate," "adequately covers," "is comprehensive" from pass conditions; requires "observable anchors only — count thresholds, named fields, structural patterns, explicit enumerations" |
| C-03 | Pass condition enforced | PASS | Prohibited phrase list in Phase 3 is a named, enumerated checklist; SCHEMA gate prevents undeclared fields entering Phase 2 |
| C-04 | Scoring formula explicit | PASS | Phase 4 shows exact formula with denominators: `(essential_pass / N_essential * 60) + ...` |
| C-05 | Tier structure present | PASS | Phase 3 defines three tiers (Essential 3–5, Recommended 2–3, Aspirational 1–2) with sequential C-NN numbering |

**Essential gate**: PASS (5/5)

### Recommended Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-06 | Failure modes cataloged | PASS | Phase 2 requires minimum 3 failure modes with FAIL-NN format before criteria are drafted; each must name a concrete property, not a generic quality observation |
| C-07 | Specificity test included | PARTIAL | Phase 3's prohibited phrase list prevents generic pass conditions, but no criterion in the output rubric tests that output is specific to the input — the mechanism is a prohibition, not a scoreable criterion |
| C-08 | Version and date stamped | PASS | SCHEMA frontmatter_block declares `date` and `version` as required fields; output template shows both fields |

**Recommended**: (1 + 0.5 + 1) = 2.5 / 3 → **25 pts**

### Aspirational Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-09 | Coverage of all output sections | PARTIAL | Phase 2 extracts "required output fields, structural shape of a complete correct output" — section awareness present; but no rule mandates at least one criterion per named output section |
| C-10 | Scoring formula includes partial credit | FAIL | Phase 4 formula is binary (pass/fail counts); no PARTIAL distinction defined for recommended or aspirational tiers |
| C-11 | External enforcement gate | PASS | Phase 3 contains a named, enumerated prohibition checklist (4 banned phrases); SCHEMA gate ("A field not in SCHEMA before Phase 2 is a structural error") is a named rejection constraint |
| C-12 | Failure-first derivation | PASS | Phase 2 extracts failure modes before Phase 3 drafts criteria; structural phase sequencing prevents criteria from being written before FAIL-NN entries exist |
| C-13 | Generic-vs-specific foil pair | FAIL | No before/after contrast example illustrating what a generic vs. specific criterion looks like; prohibition list states what to avoid but does not model the alternative |
| C-14 | Explicit category enumeration | FAIL | SCHEMA criterion_block declares `category` as a required field but provides no closed enumeration; evaluators must invent values at scoring time |
| C-15 | Specificity mechanism → scoreable criterion | FAIL | V-01's design note explicitly names this as the risk: the SCHEMA BLOCK prevents unanchored fields but does not include a conversion phase; specificity enforcement remains a prohibition ("must not appear"), not a criterion in the output rubric |
| C-16 | Required fields have structural home | PASS | SCHEMA BLOCK maps every required field to a named structural location (frontmatter_block, purpose_statement, criterion_block, scoring_section) before Phase 2 begins; a required field absent from SCHEMA is a structural error detectable before content is written |

**Aspirational**: (0.5 + 0 + 1 + 1 + 0 + 0 + 0 + 1) = 3.5 / 8 → **4.375 pts**

### V-01 Composite

```
composite = (5/5 * 60) + (2.5/3 * 30) + (3.5/8 * 10)
          = 60 + 25 + 4.375
          = 89.375
```

**Score: 89.4 / 100 — GOLDEN** (all essential pass, composite >= 80)

---

## V-02 — Lifecycle Emphasis (Specificity-Conversion Phase)

### Essential Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | Skill identity declared | PARTIAL | No frontmatter template in Phase 4 — write path `{skill}-rubric-{date}.md` names the skill in the filename but the rubric header is unanchored; skill identity is builder-inferred, not structurally required |
| C-02 | Criteria are testable | PASS | CONVERSION-MAP's `is_prohibition` and `is_input_analysis` boolean checks enforce testability for specificity criteria; Phase 1 failure modes require "a concrete property of the skill's output — not a generic quality observation" |
| C-03 | Pass condition enforced | PARTIAL | CONVERSION-MAP enforces testability for criteria derived from SPEC-INVENTORY but no prohibition checklist applies to failure-mode-derived criteria in Phase 3; advisory language remains possible in the essential tier |
| C-04 | Scoring formula explicit | PASS | Phase 4 shows exact formula with denominators |
| C-05 | Tier structure present | PASS | Phase 3 defines Essential (3–5), Recommended (2–3), Aspirational (1–2) tiers with C-NN numbering |

**Essential gate**: FAIL (C-01 PARTIAL, C-03 PARTIAL — essential not all PASS)

### Recommended Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-06 | Failure modes cataloged | PASS | Phase 1 requires FAIL-NN format, minimum 3, each naming a concrete property and explaining why the output is non-functional |
| C-07 | Specificity test included | PASS | CONVERSION-MAP produces a named criterion for each specificity element with a testable pass condition (not a prohibition or input-analysis gate); CONVERSION TRACE verifies all SPEC-INVENTORY elements map to a criterion ID; `unmapped: must be empty` is a hard gate |
| C-08 | Version and date stamped | FAIL | No frontmatter template defined; Phase 4 write path uses date in filename but no `version:` or `date:` field is declared as required in the output schema |

**Recommended**: (1 + 1 + 0) = 2 / 3 → **20 pts**

### Aspirational Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-09 | Coverage of all output sections | PARTIAL | Phase 1 extracts "required output fields, structural shape of a complete correct output" — sections are surfaced but no rule mandates one criterion per section |
| C-10 | Scoring formula includes partial credit | FAIL | Phase 4 formula is binary; CONVERSION-MAP distinguishes FAIL/PARTIAL/PASS within the build step but this is not the scoring formula — the output rubric's formula collapses to pass/fail counts |
| C-11 | External enforcement gate | PASS | "DO NOT proceed to Phase 3 unless every CONVERSION-MAP entry has conversion_complete: yes" and "DO NOT proceed to Phase 4 unless unmapped is empty" are named rejection gates preventing advancement without quality checks |
| C-12 | Failure-first derivation | PASS | Phase 1 (failure enumeration) structurally precedes Phase 3 (criterion drafting); FAIL-NN IDs are required before any criterion block is written |
| C-13 | Generic-vs-specific foil pair | PASS | CONVERSION-MAP includes concrete contrast: "**A prohibition is not a criterion.** [example]" vs. "**An input-analysis step is not a criterion.** [example]" vs. "**A scoreable criterion** names a testable property of the output: [example]" — three-way contrast model present |
| C-14 | Explicit category enumeration | FAIL | SPEC-INVENTORY and CONVERSION-MAP use open labels; no closed enumeration `one of: correctness / depth / format / coverage / behavior` defined anywhere |
| C-15 | Specificity mechanism → scoreable criterion | PASS | SPECIFICITY-CONVERSION phase explicitly converts each SPEC-INVENTORY element into a criterion whose pass_condition is a testable property of the output artifact; `is_prohibition: yes/no` and `conversion_complete: yes/no` booleans block prohibition-form pass conditions from advancing; "DO NOT proceed" gate enforces 100% conversion before Phase 3 |
| C-16 | Required fields have structural home | FAIL | No SCHEMA block; required criterion fields (id, text, category, pass_condition) are stated as obligations in phase instructions but have no named structural location in an output template — unanchored declarations |

**Aspirational**: (0.5 + 0 + 1 + 1 + 1 + 0 + 1 + 0) = 4.5 / 8 → **5.625 pts**

### V-02 Composite

```
composite = (4/5 * 60) + (2/3 * 30) + (4.5/8 * 10)
          = 48 + 20 + 5.625
          = 73.625
```

**Score: 73.6 / 100 — NOT GOLDEN** (C-01 and C-03 not full PASS; composite < 80)

---

## Ranking

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Golden? |
|------|-----------|-----------|-------------|--------------|-----------|---------|
| 1 | V-01 (Schema-First) | 5/5 PASS | 2.5/3 | 3.5/8 | **89.4** | YES |
| 2 | V-02 (Specificity-Conversion) | 4/5 (partials) | 2/3 | 4.5/8 | **73.6** | NO |
| — | V-03–V-05 | not drafted | — | — | — | — |

---

## Criterion Cross-Reference

| Criterion | V-01 | V-02 | Pattern |
|-----------|------|------|---------|
| C-01 | PASS | PARTIAL | V-01 frontmatter template anchors skill identity; V-02 has none |
| C-02 | PASS | PASS | Both enforce testability; different mechanisms |
| C-03 | PASS | PARTIAL | V-01 prohibition checklist; V-02 partial (specificity only) |
| C-04 | PASS | PASS | Both show exact formula |
| C-05 | PASS | PASS | Both define three tiers |
| C-06 | PASS | PASS | Both require failure mode enumeration |
| C-07 | PARTIAL | PASS | V-02's CONVERSION PHASE is the only mechanism that produces a C-07 PASS |
| C-08 | PASS | FAIL | V-01 SCHEMA declares date/version; V-02 has no frontmatter template |
| C-09 | PARTIAL | PARTIAL | Universal miss — no per-section criterion mandate in either |
| C-10 | FAIL | FAIL | Universal miss — binary formula in both |
| C-11 | PASS | PASS | Different mechanisms: prohibition checklist (V-01), rejection gates (V-02) |
| C-12 | PASS | PASS | Both sequence failure modes before criteria |
| C-13 | FAIL | PASS | V-02 CONVERSION-MAP three-way contrast passes; V-01 has no foil pair |
| C-14 | FAIL | FAIL | Universal miss — closed enumeration absent in both |
| C-15 | FAIL | PASS | V-02's axis directly targets this criterion; V-01 does not address it |
| C-16 | PASS | FAIL | V-01's axis directly targets this criterion; V-02 does not address it |

---

## Excellence Signals — Round 4

### E-1: SCHEMA BLOCK converts C-16 from audit to structural pre-condition (V-01)

V-01 demonstrates that requiring a SCHEMA BLOCK as the *first section of the artifact* — before Phase 2 begins — makes unanchored field declarations structurally impossible rather than detectable only at audit time. The key mechanism: "A field that will appear in the final output must have an entry in SCHEMA before you begin Phase 2." This converts C-16 from "did the evaluator notice the field had no home?" to "is the SCHEMA entry present or absent?" — a binary structural check available by inspection.

### E-2: CONVERSION-MAP boolean triplet converts specificity prohibitions to output-testable criteria (V-02)

V-02 demonstrates that three self-referential boolean fields — `is_prohibition`, `is_input_analysis`, `conversion_complete` — force a builder to reclassify each specificity element until it satisfies the definition of a scoreable criterion. The `DO NOT proceed` gate before Phase 3 makes conversion completeness a structural dependency rather than an intention. The CONVERSION TRACE (`unmapped: must be empty`) closes the loop. This is the only mechanism across all rounds that achieves C-15 PASS.

### E-3: C-15 and C-16 are orthogonal — V-01 and V-02 solve different failure modes

V-01 targets C-16 (structural homes) and fails C-15 (specificity conversion). V-02 targets C-15 (specificity conversion) and fails C-16 (structural homes). Both reach the same aspirational score on their respective target criterion. No interaction between the failure modes was observed — combining SCHEMA BLOCK (V-01) with CONVERSION-MAP (V-02) is the V-04 hypothesis and is structurally predictable to achieve both PASS.

### Persistent Gaps

**C-10 (universal miss)**: Neither variation distinguishes PARTIAL from PASS in the scoring formula. V-02's CONVERSION-MAP does use PARTIAL semantics internally (three-way conversion assessment), but this is a build-step judgment — it does not propagate into the output rubric's scoring formula structure. A formula variant like `composite = (essential_pass + 0.5 * essential_partial) / 5 * 60 + ...` would pass C-10.

**C-14 (universal miss)**: Neither variation provides a closed enumeration for the `category` field. Both allow arbitrary prose labels, which leaves the evaluator to invent enumeration members at scoring time.

**C-13 (V-01 miss)**: V-01 has a prohibition list but no before/after contrast model. V-02 passes C-13 via the three-way CONVERSION-MAP contrast. The foil pair pattern (E-3 from R3) consistently converts C-07 from PARTIAL to PASS when present.

---

## Round 4 Findings

### F-01: V-01 achieves golden despite C-15 FAIL; V-02 fails golden despite C-15 PASS

The discovery: C-16 (structural home) contributes more to total composite than C-15 (specificity conversion) because fixing C-16 also unlocks essential-tier stability. V-02's C-01 and C-03 PARTIAL scores (both caused by absent structural templates — the root cause C-16 captures) cost 12 essential points, which outweighs V-02's advantages on C-07, C-13, and C-15. This confirms C-16 is load-bearing at the essential tier level, not just aspirational.

### F-02: Frontmatter template absence is a cascading failure

In V-02, absent frontmatter template causes C-01 PARTIAL (skill identity unanchored), C-08 FAIL (no date/version), and contributes to C-16 FAIL (no structural home for required fields). Three criteria fail or partial from one missing output template. The SCHEMA BLOCK in V-01 prevents all three simultaneously — it is a multiplier pattern.

### F-03: V-04 (combined schema-first + conversion phase) is strongly predicted to be the highest-scoring unscored variation

From the criterion cross-reference: V-04 would inherit V-01's PASS on C-01, C-03, C-08, C-16 and V-02's PASS on C-07, C-13, C-15. Combined essential = 5/5. Combined recommended = 3/3 (C-06, C-07, C-08). Combined aspirational gains C-11, C-12, C-13, C-15, C-16. Universal misses C-10 and C-14 remain. Predicted score: 60 + 30 + (6/8 * 10) = 97.5.

---

```json
{"top_score": 89.4, "all_essential_pass": true, "new_patterns": ["SCHEMA BLOCK converts required-field anchoring from post-hoc audit to pre-Phase structural declaration: unanchored field absence is a structural error visible before content is written, eliminating C-16 failures cascading into C-01 and C-08", "CONVERSION-MAP boolean triplet (is_prohibition / is_input_analysis / conversion_complete) with DO NOT proceed gate is the only mechanism that converts specificity prohibitions into output-testable criteria, achieving C-15 PASS"]}
```
