---

## R8 Scorecard: discover-causal

**Rubric:** v8 (29 criteria, 195 pts max)
**Base:** R7 V-05 (195/195 -- ceiling)

### Results

| Variation | C-27 | C-28 | C-29 | Score | Tier |
|-----------|------|------|------|-------|------|
| V-01 (inline prohibition) | PASS | PASS | PASS | **195** | Golden (ceiling) |
| V-02 (back-reference stripped) | PASS | **FAIL** | PASS | **190** | Golden |
| V-03 (field-level C-29 stripped) | PASS | PASS | PASS | **195** | Golden (ceiling) |
| V-04 (V-01 + V-02 combined) | PASS | **FAIL** | PASS | **190** | Golden |
| V-05 (ceiling + anchor-update) | PASS | PASS | PASS | **195** | Golden (ceiling) |

All 4 hypotheses confirmed. C-28 is the sole differentiating criterion in R8.

### Hypothesis Outcomes

**V-01 confirmed (195):** The `PROHIBITED FORM:` block label is NOT required for C-27. Inline "does not pass" in the sub-step header is the load-bearing element -- the phrase closes the escape hatch regardless of whether it appears in a labeled block or inline parenthetical.

**V-02 confirmed (190):** The "already on record from Phase 1 SUB-STEP 2" phrase IS required for C-28. "Confirm and extend the preliminary anchor from Phase 1" references Phase 1 but does not acknowledge the anchor as prior record -- it reads as instruction to produce rather than instruction to confirm. The back-reference is load-bearing.

**V-03 confirmed (195):** Any Phase 6 position satisfies C-29. The integration rules list bullet alone suffices; the Falsification field description annotation is a second site, not a required site.

**V-04 confirmed (190):** V-01 and V-02 effects are independent -- C-27 PASS carries through and C-28 FAIL carries through with no interaction.

### V9 Candidate Signal (from V-05)

**C-30 (proposed): Phase 6 Falsification tracks Phase 3 anchor update.** When Phase 3 updates the preliminary anchor to a higher-confidence step, Phase 6 must carry the updated step -- not the Phase 1 anchor verbatim. V-05 closes this stale-anchor propagation gap with an integration rule and adds `anchor_updated_from_phase1: true | false | n/a` to the ARTIFACT frontmatter. V-01 through V-04 do not have this rule and would fail C-30 if it were added.

```json
{"top_score": 195, "all_essential_pass": true, "new_patterns": ["C-27 phrase is load-bearing not the block label: inline 'does not pass' in the sub-step header satisfies C-27", "C-28 back-reference 'already on record from Phase 1 SUB-STEP 2' is load-bearing: 'confirm and extend from Phase 1' without explicit prior-record acknowledgment does not pass", "C-29 is satisfied by any Phase 6 position: integration rules list bullet alone satisfies the synthesis-phase integrity requirement", "V9 candidate C-30: Phase 6 Falsification must track Phase 3 anchor update -- stale-anchor propagation failure detectable via ARTIFACT field anchor_updated_from_phase1"]}
```
used only for C-26
through C-29.

| ID | Criterion | All Variations | Evidence Note |
|----|-----------|---------------|---------------|
| C-09 | Evidence quality rated | **PASS** | Phase 4 defines T1/T2/T3/none tiers; Aggregate evidence tier is a required output |
| C-10 | Multiple pathways considered | **PASS** | Phase 2 explicitly asks for secondary pathway; complementary/competing/nested/singular required |
| C-11 | Incompleteness acknowledged | **PASS** | Phase 1 readiness gate requires self-assessment; fabricating thin steps explicitly named as failure |
| C-12 | Break anchored to named step | **PASS** | Phase 3 requires "Step [N] -- [Name]" format; UNCERTAIN step still anchors |
| C-13 | Evidence gap localized | **PASS** | Phase 4 requires per-step evidence accounting; gap field required even when value is "none" |
| C-14 | AMEND conditioned on inertia | **PASS** | Phase 6 AMEND requires inertia incorporation; all three verdict values covered with required forms |
| C-15 | AMEND synthesizes all phases | **PASS** | Phase 6 requires named fields from every prior phase; omitting any does not pass |
| C-16 | Pathway steps formally labeled | **PASS** | Phase 2 STEP LABELING REQUIREMENT is structural prerequisite; positional references do not pass |
| C-17 | Confounder distinguished from inertia | **PASS** | Phase 5 explicitly excludes inertia case; required to acknowledge the exclusion explicitly |
| C-18 | Incomplete pathway still anchors | **PASS** | Phase 3 CONDITIONAL BRANCH requires BEST-TRACEABLE ANCHOR; metric deferral named as failure |
| C-19 | Evidence gap and tier are separate fields | **PASS** | Phase 4 FIELD INDEPENDENCE NOTE; two named entries explicitly required; merging named as failure |
| C-20 | AMEND inertia is unconditional | **PASS** | Phase 6 names all three verdict forms; no verdict makes incorporation optional |
| C-21 | Null-gap counterexample proven | **PASS** | Phase 4 NULL-GAP COUNTEREXAMPLE explicitly instantiates "gap: none, tier: T1" state |
| C-22 | Inertia conditional form excluded | **PASS** | Phase 0 PROHIBITED FORM names "conditioning on Competing or Unclear does not pass" |
| C-23 | Mechanism completeness is named AMEND field | **PASS** | Phase 6 Mechanism completeness is a standalone named field; embedding in clause text does not pass |
| C-24 | Falsification deferral form excluded | **PASS** | Phase 3 PROHIBITED FORM (C-24) names "deferring or omitting step-level falsification does not pass" |
| C-25 | Evidence gap is standalone AMEND field | **PASS** | Phase 6 Evidence gap is a distinct named field; PROPAGATION REQUIREMENT names this explicitly |
| C-26 | Anchor co-located with declaration | **PASS** | Phase 1 SUB-STEP 2 requires preliminary anchor before Phase 2 in all five variations; Phase 3 confirms/extends |

**C-26 is PASS in all five variations.** C-27/C-28/C-29 are gradeable for all five.

---

### C-27, C-28, C-29 -- Per-Variation

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| **C-27** | C-26 prohibition co-located at Phase 1 | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |
| **C-28** | Phase 3 frames anchor as confirmation | **PASS** | **FAIL** | **PASS** | **FAIL** | **PASS** |
| **C-29** | C-26 integrity rule named at synthesis | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |

**C-27 evidence per variation:**

- **V-01 PASS**: Phase 1 SUB-STEP 2 header reads "(required here before Phase 2; proceeding to
  Phase 2 without producing this anchor does not pass):" -- "does not pass" language is present
  at Phase 1. Body adds: "Deferring this anchor to Phase 3 does not pass." No PROHIBITED FORM
  block label, but the phrase is present at the declaration point. C-27 requires the "does not
  pass" language at Phase 1 -- satisfied. The block label is not required; the phrase is
  load-bearing.

- **V-02 PASS**: Phase 1 has separate PROHIBITED FORM block: "Declaring incompleteness and
  proceeding to Phase 2 without producing this preliminary anchor in SUB-STEP 2 does not pass."
  Named at Phase 1. Full C-27 pass.

- **V-03 PASS**: Phase 1 PROHIBITED FORM block preserved identically from R7 V-05. Full C-27 pass.

- **V-04 PASS**: Same inline mechanism as V-01 -- "(required here before Phase 2; proceeding to
  Phase 2 without producing this anchor does not pass):" plus body "Deferring this anchor to
  Phase 3 does not pass." Language present at Phase 1. PASS.

- **V-05 PASS**: Phase 1 PROHIBITED FORM block preserved identically from R7 V-05. Full C-27 pass.

**C-28 evidence per variation:**

- **V-01 PASS**: Phase 3 CONDITIONAL BRANCH preserved from R7 V-05: "If PATHWAY INCOMPLETE was
  declared in Phase 1, a PRELIMINARY ANCHOR is already on record from Phase 1 SUB-STEP 2. This
  branch confirms and extends it." Both explicit prior-record acknowledgment ("already on record")
  and confirmation framing ("This branch confirms and extends it.") are present.

- **V-02 FAIL**: Phase 3 CONDITIONAL BRANCH reads: "If PATHWAY INCOMPLETE was declared in Phase 1,
  confirm and extend the preliminary anchor from Phase 1." The "already on record from Phase 1
  SUB-STEP 2" phrase is removed. The standalone sentence "This branch confirms and extends it."
  is removed. "Confirm and extend from Phase 1" references Phase 1 but does not acknowledge the
  Phase 1 anchor as prior record -- it reads as instruction rather than acknowledgment. C-28
  requires Phase 3 to "explicitly reference the Phase 1 anchor as prior record" -- the stripped
  form omits that explicit acknowledgment. FAIL.

- **V-03 PASS**: Phase 3 CONDITIONAL BRANCH preserved from R7 V-05. "Already on record from
  Phase 1 SUB-STEP 2. This branch confirms and extends it." present. PASS.

- **V-04 FAIL**: Same stripped Phase 3 as V-02 -- "confirm and extend the preliminary anchor from
  Phase 1" without "already on record" acknowledgment. FAIL for the same reason as V-02.

- **V-05 PASS**: Phase 3 CONDITIONAL BRANCH preserved from R7 V-05. Full C-28 pass.

**C-29 evidence per variation:**

- **V-01 PASS**: Phase 6 Falsification field description includes "a Falsification field that
  first names the anchor here without a corresponding Phase 1 PRELIMINARY ANCHOR does not pass
  C-26." Integration rules also include the same detection. Both sites present.

- **V-02 PASS**: Phase 6 Falsification field description preserved with C-29 rule. Integration
  rules preserved. Both sites present.

- **V-03 PASS**: Phase 6 Falsification field description C-29 sentence removed. Integration rules
  C-29 bullet preserved: "For incomplete pathways, the Falsification field must carry an anchor
  that was first produced in Phase 1 -- not first introduced here. A response where Phase 1
  contains no PRELIMINARY ANCHOR and Phase 6 Falsification carries the first anchor does not
  pass C-26." C-29 criterion requires "the synthesis/AMEND phase includes an integration rule
  that explicitly detects the C-26 cross-phase violation" -- integration rules bullet satisfies
  this. Any Phase 6 position passes. PASS.

- **V-04 PASS**: Phase 6 Falsification field description C-29 rule preserved. Integration rules
  C-29 bullet preserved. Both sites present.

- **V-05 PASS**: Phase 6 preserved from R7 V-05 at both C-29 sites. Anchor-update propagation
  rule also present. Full C-29 pass.

---

## Score Summary

### Per-Criterion Points (aspirational tier -- 5 pts each)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-09 | 5 | 5 | 5 | 5 | 5 |
| C-10 | 5 | 5 | 5 | 5 | 5 |
| C-11 | 5 | 5 | 5 | 5 | 5 |
| C-12 | 5 | 5 | 5 | 5 | 5 |
| C-13 | 5 | 5 | 5 | 5 | 5 |
| C-14 | 5 | 5 | 5 | 5 | 5 |
| C-15 | 5 | 5 | 5 | 5 | 5 |
| C-16 | 5 | 5 | 5 | 5 | 5 |
| C-17 | 5 | 5 | 5 | 5 | 5 |
| C-18 | 5 | 5 | 5 | 5 | 5 |
| C-19 | 5 | 5 | 5 | 5 | 5 |
| C-20 | 5 | 5 | 5 | 5 | 5 |
| C-21 | 5 | 5 | 5 | 5 | 5 |
| C-22 | 5 | 5 | 5 | 5 | 5 |
| C-23 | 5 | 5 | 5 | 5 | 5 |
| C-24 | 5 | 5 | 5 | 5 | 5 |
| C-25 | 5 | 5 | 5 | 5 | 5 |
| C-26 | 5 | 5 | 5 | 5 | 5 |
| C-27 | 5 | 5 | 5 | 5 | 5 |
| C-28 | 5 | **0** | 5 | **0** | 5 |
| C-29 | 5 | 5 | 5 | 5 | 5 |

### Composite Scores

| Section | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| Essential (60 pts) | 60 | 60 | 60 | 60 | 60 |
| Recommended (30 pts) | 30 | 30 | 30 | 30 | 30 |
| Aspirational (105 pts) | 105 | 100 | 105 | 100 | 105 |
| **Total (195 pts)** | **195** | **190** | **195** | **190** | **195** |
| Tier | Golden (ceiling) | Golden | Golden (ceiling) | Golden | Golden (ceiling) |

All essential criteria pass in all five variations.

---

## Ranking

1. **V-01, V-03, V-05** -- 195/195 (tied at ceiling)
2. **V-02, V-04** -- 190/195 (C-28 FAIL)

---

## Hypothesis Outcomes

| Variation | Hypothesis | Result | Confirmed? |
|-----------|-----------|--------|-----------|
| V-01 | Inline "does not pass" in sub-step header satisfies C-27 (block label not required) | 195 -- C-27 PASS | YES |
| V-02 | "confirm and extend from Phase 1" alone is NOT sufficient for C-28 (back-reference required) | 190 -- C-28 FAIL | YES |
| V-03 | Integration rules list position alone satisfies C-29 (field-level annotation not required) | 195 -- C-29 PASS | YES |
| V-04 | V-01 + V-02 effects are independent: C-27 PASS + C-28 FAIL = 190 | 190 -- C-28 FAIL | YES |
| V-05 | R7 V-05 ceiling preserved; anchor-update propagation is a v9 signal | 195 -- all pass | YES |

All four hypotheses confirmed. No unexpected interaction effects.

---

## Excellence Signals

**From V-01 (195 -- C-27 inline mechanism):**
The labeled "PROHIBITED FORM:" block is not required for C-27. The phrase "does not pass" at
the Phase 1 declaration point is the load-bearing element. An inline parenthetical in the
sub-step header satisfies C-27 as effectively as a standalone block. C-27 can be satisfied by
a lighter syntactic form; the block structure is one path, not the only path.

**From V-02 (190 -- C-28 FAIL establishes back-reference as load-bearing):**
"Confirm and extend the preliminary anchor from Phase 1" is NOT sufficient for C-28. The explicit
acknowledgment "a PRELIMINARY ANCHOR is already on record from Phase 1 SUB-STEP 2" is the
mechanism by which Phase 3 frames its work as confirmation rather than origination. Without the
prior-record acknowledgment, Phase 3 reads as instruction to produce an anchor (which could be
first origination) rather than instruction to confirm one that already exists. The "already on
record" phrase is the C-28 load-bearing element.

**From V-03 (195 -- C-29 any Phase 6 site):**
C-29 is satisfied by any Phase 6 enforcement site. The integration rules list bullet alone
satisfies the synthesis-phase integrity requirement. The Falsification field description
annotation is a second site, not a required site. Either a Falsification field note or an
integration rules bullet is sufficient for C-29.

**From V-05 (195 -- anchor-update propagation as v9 signal):**
V-05 closes a gap not yet captured by any criterion: stale-anchor propagation. A model can pass
C-26/C-27/C-28/C-29 while still carrying the Phase 1 preliminary anchor verbatim in Phase 6
when Phase 3 updated to a higher-confidence step. V-05 adds an explicit integration rule and
the ARTIFACT field `anchor_updated_from_phase1` to make this observable. This is the v9
candidate criterion.

---

## V9 Candidate Criterion

**C-30 (proposed): Phase 6 Falsification tracks Phase 3 anchor update**

When Phase 3 updates the preliminary anchor to a higher-confidence step, Phase 6 Falsification
must carry the updated step -- not the Phase 1 preliminary anchor verbatim. Carrying the Phase 1
anchor unchanged when Phase 3 identified a better step is a stale-anchor propagation failure.
If Phase 3 confirmed without updating, Phase 6 carrying the Phase 1 anchor verbatim is correct.

Gradeability: requires C-26 PASS and C-28 PASS. Scored only when PATHWAY INCOMPLETE triggers.
Observable via ARTIFACT field `anchor_updated_from_phase1: true | false | n/a`.

V-01 through V-04 do not have this rule. V-05 has it. V-05 is the baseline for C-30.

---

## Criteria Summary (v8)

| Tier | IDs | Max pts | All-variation result |
|------|-----|---------|---------------------|
| Essential | C-01 through C-05 | 60 | All PASS (60/60) |
| Recommended | C-06 through C-08 | 30 | All PASS (30/30) |
| Aspirational | C-09 through C-29 | 105 | C-28 varies (V-02, V-04 FAIL) |

**C-28 is the sole differentiating criterion in R8.** V-02 and V-04 fail it (-5 pts each).
All other criteria pass in all five variations.

---

```json
{"top_score": 195, "all_essential_pass": true, "new_patterns": ["C-27 phrase is load-bearing not the block label: inline 'does not pass' in the sub-step header satisfies C-27", "C-28 back-reference 'already on record from Phase 1 SUB-STEP 2' is load-bearing: 'confirm and extend from Phase 1' without explicit prior-record acknowledgment does not pass", "C-29 is satisfied by any Phase 6 position: integration rules list bullet alone satisfies the synthesis-phase integrity requirement", "V9 candidate C-30: Phase 6 Falsification must track Phase 3 anchor update -- stale-anchor propagation failure detectable via ARTIFACT field anchor_updated_from_phase1"]}
```
