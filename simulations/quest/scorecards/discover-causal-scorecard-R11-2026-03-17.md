## discover-causal R11 Scorecard (Rubric v11)

**Base:** R10 V-05 -- 215/215 (ceiling)
**Criteria under test:** C-32, C-33

---

### Score Summary

| Variation | C-01..C-31 | C-32 | C-33 | Total | Tier |
|-----------|------------|------|------|-------|------|
| V-01 (C-32 stripped) | 205 | FAIL | PASS | **210** | Golden |
| V-02 (C-32 softened) | 205 | FAIL | PASS | **210** | Golden |
| V-03 (C-33 stripped) | 205 | PASS | FAIL | **210** | Golden |
| V-04 (C-33 body-placement) | 205 | PASS | FAIL | **210** | Golden |
| V-05 (Full ceiling + v12 scout) | 205 | PASS | PASS | **215** | Golden (ceiling) |

All essential pass: YES. All recommended pass: YES. C-01 through C-31 PASS in all variations (inherited from R10 V-05 base).

---

### Isolation Question Verdicts

**Q1 (V-01):** C-32 is independently required. C-29 names the C-26 violation; C-30 names the stale-anchor failure; neither names the C-31 structural requirement at Phase 6. Silence on C-31 at synthesis leaves the Phase 3 co-location requirement unnamed at the convergence point. C-32 FAIL confirmed.

**Q2 (V-02):** Explicit "does not pass" failure-mode language is required for C-32. By the C-22/C-24/C-27 precedent, positive structural description without naming the failure mode does not close the escape hatch. C-32 FAIL confirmed.

**Q3 (V-03):** ARTIFACT field independently required. C-31 (behavior at Phase 3) and C-32 (named at Phase 6) enforce the behavioral requirement; C-33 enforces the machine-readability requirement. Neither substitutes for the other. C-33 FAIL confirmed.

**Q4 (V-04):** Frontmatter placement specifically required. "ARTIFACT frontmatter includes" is the location specification. Prose body is not machine-parseable in the same structured way. C-33 FAIL confirmed.

---

### Excellence Signals (V-05)

**Pattern E-01 -- Symmetric ARTIFACT audit:** For every enforcement chain criterion, pair with a machine-readable frontmatter field tracking compliance. V-05 adds `phase1_anchor_prohibition_stated: true | false | n/a` completing the four-position ARTIFACT table: `preliminary_anchor_declared` (C-26), `phase1_anchor_prohibition_stated` (C-27, v12 candidate), `anchor_updated_from_phase1` (C-30), `phase3_anchor_update_prohibited_form` (C-33).

**Pattern E-02 -- Field gradeability for criterion-fail states:** When the prohibited form is absent (C-31 FAIL), the correct ARTIFACT field value is `false`, not absent. This distinguishes behavioral failure with correct audit (field `false`) from missing audit (field absent, C-33 FAIL).

---

**v12 signal:** `phase1_anchor_prohibition_stated` tracks C-27 compliance machine-readably. Under v12, V-05 scores 220 (new ceiling); V-01..V-04 drop to 205 (Golden floor).

```json
{"top_score": 215, "all_essential_pass": true, "new_patterns": ["Symmetric ARTIFACT audit: for every enforcement chain criterion, pair with a machine-readable frontmatter field tracking compliance at that production point -- one field per criterion, same N/A condition as the criterion, independently gradeable", "Field gradeability design: when the prohibited form is absent (criterion fails), the correct ARTIFACT field value is 'false' not absent -- absence of the field fails C-33 separately from the criterion fail; this distinguishes behavioral failure with correct audit from behavioral failure with missing audit"]}
```
-specific grounding; "no evidence" is a valid value |

**Essential subtotal: 60/60 all variations**

---

#### Recommended Criteria -- 30 pts (C-06 through C-08, 10 pts each)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence note |
|----|------|------|------|------|------|---------------|
| C-06 | PASS | PASS | PASS | PASS | PASS | Step format ("What changes. Who acts. Observable indicator.") produces testable pathway by construction |
| C-07 | PASS | PASS | PASS | PASS | PASS | Phase 5 CONFOUNDER CHECK requires at least one named alternative cause; silence is not acceptable |
| C-08 | PASS | PASS | PASS | PASS | PASS | Phase 6 AMEND produces bounded scope (mechanism qualifier + population/context/timeframe) |

**Recommended subtotal: 30/30 all variations**

---

#### Aspirational Criteria -- 125 pts (C-09 through C-33, 5 pts each)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence note |
|----|------|------|------|------|------|---------------|
| C-09 | PASS | PASS | PASS | PASS | PASS | Phase 4 T1/T2/T3 tier schema present; aggregate evidence tier is a named output |
| C-10 | PASS | PASS | PASS | PASS | PASS | Phase 2 asks "more than one plausible causal pathway?" with complementary/competing/nested classification |
| C-11 | PASS | PASS | PASS | PASS | PASS | Phase 1 incompleteness gate: "if no: complete both sub-steps below" triggers only on genuine incompleteness |
| C-12 | PASS | PASS | PASS | PASS | PASS | Phase 3 format "The mechanism fails if Step [N] -- [Name]" requires step number and name matching Phase 2 |
| C-13 | PASS | PASS | PASS | PASS | PASS | Phase 4 "Evidence gap steps" named output lists step labels lacking evidence; "none" is a valid value |
| C-14 | PASS | PASS | PASS | PASS | PASS | Phase 6 Amended clause (c) requires inertia incorporation for all three verdict values |
| C-15 | PASS | PASS | PASS | PASS | PASS | Phase 6 requires named fields for inertia verdict, mechanism completeness, evidence tier, evidence gap, confounder finding, falsification |
| C-16 | PASS | PASS | PASS | PASS | PASS | Phase 2 STEP LABELING REQUIREMENT names "Step N -- [Name]:" as structural prerequisite, not presentational preference |
| C-17 | PASS | PASS | PASS | PASS | PASS | Phase 5 CONFOUNDER CHECK explicitly excludes inertia case with required acknowledgment phrase |
| C-18 | PASS | PASS | PASS | PASS | PASS | Phase 3 CONDITIONAL BRANCH format "BEST-TRACEABLE ANCHOR" enforces step-anchored falsification even when incomplete |
| C-19 | PASS | PASS | PASS | PASS | PASS | Phase 4 FIELD INDEPENDENCE NOTE produces "Evidence gap steps" and "Aggregate evidence tier" as two separate named entries |
| C-20 | PASS | PASS | PASS | PASS | PASS | Phase 6 integration rules: "no verdict value makes inertia incorporation optional" |
| C-21 | PASS | PASS | PASS | PASS | PASS | Phase 4 NULL-GAP COUNTEREXAMPLE demonstrates gap:none + tier:T1 as valid co-existing state |
| C-22 | PASS | PASS | PASS | PASS | PASS | Phase 0 PROHIBITED FORM names "conditioning inertia incorporation on the verdict being Competing or Unclear does not pass" |
| C-23 | PASS | PASS | PASS | PASS | PASS | Phase 6 "Mechanism completeness:" is a standalone named AMEND field with explicit embed-in-clause exclusion |
| C-24 | PASS | PASS | PASS | PASS | PASS | Phase 3 PROHIBITED FORM (C-24): "declaring incompleteness and deferring or omitting step-level falsification does not pass" |
| C-25 | PASS | PASS | PASS | PASS | PASS | Phase 4 PROPAGATION REQUIREMENT explicitly mandates Evidence gap steps appear in Phase 6 AMEND as standalone named entry |
| C-26 | PASS | PASS | PASS | PASS | PASS | Phase 1 SUB-STEP 2 produces PRELIMINARY ANCHOR at declaration point before Phase 2 begins |
| C-27 | PASS | PASS | PASS | PASS | PASS | Phase 1 PROHIBITED FORM: "Declaring incompleteness and proceeding to Phase 2 without producing this preliminary anchor in SUB-STEP 2 does not pass" |
| C-28 | PASS | PASS | PASS | PASS | PASS | Phase 3 CONDITIONAL BRANCH: "a PRELIMINARY ANCHOR is already on record from Phase 1 SUB-STEP 2 -- This branch confirms and extends it" |
| C-29 | PASS | PASS | PASS | PASS | PASS | Phase 6 integration rules include C-26 cross-phase integrity detection: "a Falsification field that first names the anchor here without a corresponding Phase 1 PRELIMINARY ANCHOR does not pass C-26" |
| C-30 | PASS | PASS | PASS | PASS | PASS | Phase 6 stale-anchor rule + `anchor_updated_from_phase1: true | false | n/a` in ARTIFACT frontmatter present in all variations |
| C-31 | PASS | PASS | PASS | PASS | PASS | Phase 3 ANCHOR-UPDATE PROHIBITED FORM: "recording the updated BEST-TRACEABLE ANCHOR here does not complete the propagation requirement. Phase 6 Falsification must also carry the updated step -- correctly recording the update here does not close the Phase 6 propagation requirement." Self-referential form intact in all variations. |
| **C-32** | **FAIL** | **FAIL** | PASS | PASS | PASS | See per-variation analysis below |
| **C-33** | PASS | PASS | **FAIL** | **FAIL** | PASS | See per-variation analysis below |

---

### Per-Variation C-32 and C-33 Analysis

#### C-32 -- Phase 6 names C-31 structural requirement (requires C-31 PASS; gradeable in all)

**V-01 -- FAIL:** Phase 6 integration rules preserve the C-30 stale-anchor rule and the C-29 C-26 cross-phase integrity rule, but the C-32 integration rule is removed entirely. Phase 6 never names the C-31 structural requirement -- that the Phase 3 CONDITIONAL BRANCH must carry a PROHIBITED FORM alongside the update record. C-29 (C-26 violation detection) and the C-30 stale-anchor rule both PASS and address distinct failure modes; neither names that Phase 3 must carry the co-located prohibited form. The C-31 requirement is met at Phase 3 but invisible at the synthesis point. **FAIL (-5 pts).**

**V-02 -- FAIL:** Phase 6 names the C-31 structural requirement positively -- "a positive Phase 3 instruction satisfies the recording requirement but not the co-located enforcement requirement" -- but does not include explicit "does not pass" failure-mode language for the Phase 3-positive-instruction-only case. By the C-22/C-20, C-24/C-18, and C-27/C-26 precedent, positive rules are not self-enforcing. The escape hatch (a model treating Phase 3 as the terminal requirement) is named in positive structural terms but not closed by an explicit failure-mode phrase. The load-bearing element for C-32 is the "does not pass" phrase for the Phase 3-only case, parallel to C-27's "does not pass" for the Phase 1-omission case. **FAIL (-5 pts).**

**V-03 -- PASS:** Phase 6 integration rules include: "A Phase 3 CONDITIONAL BRANCH that carries only a positive update instruction -- 'record the updated BEST-TRACEABLE ANCHOR and carry it to Phase 6' -- without a PROHIBITED FORM explicitly naming that recording the update at Phase 3 does not close this Phase 6 propagation requirement does not pass C-31." This names the C-31 structural requirement with explicit failure-mode language at the synthesis point. Satisfies C-32 regardless of C-33 status. **PASS.**

**V-04 -- PASS:** Same Phase 6 C-32 integration rule as V-03, preserved intact. **PASS.**

**V-05 -- PASS:** All R10 V-05 elements intact, including the Phase 6 C-32 integration rule. **PASS.**

---

#### C-33 -- ARTIFACT frontmatter includes `phase3_anchor_update_prohibited_form` field (requires C-30 PASS; gradeable in all)

**V-01 -- PASS:** `phase3_anchor_update_prohibited_form: true | false | n/a` present in ARTIFACT frontmatter alongside `anchor_updated_from_phase1: true | false | n/a`. C-30 PASS and C-31 PASS; correct value is `true`. Field present with correct semantics. **PASS.**

**V-02 -- PASS:** Same ARTIFACT frontmatter as V-01. Field present. **PASS.**

**V-03 -- FAIL:** `phase3_anchor_update_prohibited_form: true | false | n/a` removed from ARTIFACT frontmatter entirely. `anchor_updated_from_phase1` remains. C-31 and C-32 both PASS (narrative enforcement intact), but the machine-readable ARTIFACT-layer tracking of Phase 3 co-location status is absent. Narrative enforcement at Phase 3 and Phase 6 addresses behavior; ARTIFACT field tracking is an independent machine-readability requirement. Parallel to C-30: both the integration rule and the ARTIFACT field are required; narrative alone does not substitute for the field. **FAIL (-5 pts).**

**V-04 -- FAIL:** `phase3_anchor_update_prohibited_form` appears as a prose note in the artifact body ("Phase 3 compliance note: phase3_anchor_update_prohibited_form: [true | false | n/a] -- true if..."), not in the ARTIFACT YAML frontmatter. C-33 specifies "ARTIFACT frontmatter includes" -- the location specification is frontmatter, not body. YAML frontmatter is machine-parseable in a structured, predictable way; prose body notes require natural language parsing. Body placement is the location-omission variant. Parallel to C-30's `anchor_updated_from_phase1` frontmatter requirement. **FAIL (-5 pts).**

**V-05 -- PASS:** `phase3_anchor_update_prohibited_form: true | false | n/a` in ARTIFACT frontmatter, same as R10 V-05 base. **PASS.**

---

### Score Summary

| Variation | C-01..C-31 | C-32 (5 pts) | C-33 (5 pts) | Total | Tier |
|-----------|------------|--------------|--------------|-------|------|
| V-01 (C-32 stripped) | 205 | FAIL (+0) | PASS (+5) | **210** | Golden |
| V-02 (C-32 softened) | 205 | FAIL (+0) | PASS (+5) | **210** | Golden |
| V-03 (C-33 stripped) | 205 | PASS (+5) | FAIL (+0) | **210** | Golden |
| V-04 (C-33 body-placement) | 205 | PASS (+5) | FAIL (+0) | **210** | Golden |
| V-05 (Full ceiling + v12 scout) | 205 | PASS (+5) | PASS (+5) | **215** | Golden (ceiling) |

**All essential pass: YES (all variations)**
**All recommended pass: YES (all variations)**
**C-01 through C-31 pass: YES (all variations) -- inherited from R10 V-05 base**

**Composite breakdown:**
- Essential: 60/60 across all
- Recommended: 30/30 across all
- Aspirational C-09..C-31: 115/115 across all
- C-32: V-01/V-02 = 0; V-03/V-04/V-05 = 5
- C-33: V-01/V-02/V-05 = 5; V-03/V-04 = 0

---

### Ranking

1. **V-05** -- 215 pts (Golden, ceiling) -- All C-32/C-33 PASS; adds v12 scout field `phase1_anchor_prohibition_stated` (not yet scored)
2. **V-01, V-02, V-03, V-04** -- 210 pts each (Golden) -- Single-criterion loss at C-32 or C-33

**Tie-break note:** V-01 and V-02 are structurally differentiated: V-01 tests presence/absence of the C-32 rule; V-02 tests whether the specific failure-mode phrasing ("does not pass") is required within the rule. V-03 and V-04 are also differentiated: V-03 tests field presence/absence; V-04 tests frontmatter vs body placement. All four resolve to 210 -- the single-axis isolation is clean.

---

### Isolation Question Verdicts

**Q1 (V-01): Is C-32 independently required, or do C-29 + C-30 together cover C-31 enforcement at Phase 6?**
VERDICT: C-32 is independently required. C-29 names the C-26 first-appearance-at-synthesis violation; the C-30 stale-anchor rule names the Phase 6 propagation failure. Neither names the C-31 structural requirement -- that Phase 3 must carry a co-located PROHIBITED FORM alongside the update record. Silence on the C-31 requirement at Phase 6 leaves the Phase 3 co-location requirement unnamed at the synthesis convergence point. V-01 FAIL confirms: C-29 + C-30 in place, C-32 absent, C-32 FAIL.

**Q2 (V-02): Does C-32 require explicit "does not pass" failure-mode language, or does positive structural description suffice?**
VERDICT: Explicit failure-mode language is required. Parallel to C-22 (C-20 escape hatch), C-24 (C-18 escape hatch), C-27 (C-26 escape hatch): positive rules are not self-enforcing. Naming what must be present without naming its absence as a failure mode leaves the escape hatch open for a model that reads Phase 3 as the terminal requirement. The "does not pass" phrase (or equivalent) for the Phase 3-positive-instruction-only case is the load-bearing element. V-02 FAIL confirms.

**Q3 (V-03): Is the ARTIFACT field independently required for C-33, or does narrative enforcement (C-31 + C-32) substitute?**
VERDICT: The ARTIFACT field is independently required. C-31 at Phase 3 and C-32 at Phase 6 enforce the behavioral requirement that the prohibited form be present. C-33 enforces the machine-readability requirement that Phase 3 co-location status be tracked in ARTIFACT frontmatter. These are distinct requirements: behavioral enforcement (Phase 3 carries the form) vs machine-readable audit (ARTIFACT records whether the form was carried). Parallel to C-30: integration rule + ARTIFACT field both required; neither alone satisfies both criteria. V-03 FAIL confirms.

**Q4 (V-04): Does C-33 require frontmatter placement specifically, or does prose body satisfy machine-readability?**
VERDICT: Frontmatter placement is specifically required. C-33 specifies "ARTIFACT frontmatter includes" -- the location specification is the criterion's load-bearing element. YAML frontmatter is machine-parseable in a structured, predictable way; prose body notes require natural language parsing and are not machine-parseable in the same structured sense. The machine-readability purpose motivating C-33 depends on frontmatter structure. Parallel to C-30's `anchor_updated_from_phase1` frontmatter requirement. V-04 FAIL confirms.

---

### Excellence Signals (V-05)

V-05 achieves the 215/215 ceiling under v11 and advances a v12 scout pattern:

**Pattern E-01: Symmetric ARTIFACT audit for every enforcement chain position**
V-05 adds `phase1_anchor_prohibition_stated: true | false | n/a` to the ARTIFACT frontmatter. With this field, the ARTIFACT audit table covers all four enforcement chain positions:

| ARTIFACT field | Tracks | Criterion |
|----------------|--------|-----------|
| `preliminary_anchor_declared` | Phase 1 anchor co-location | C-26 |
| `phase1_anchor_prohibition_stated` | Phase 1 prohibition phrase | C-27 (v12 candidate) |
| `anchor_updated_from_phase1` | Phase 6 anchor provenance | C-30 |
| `phase3_anchor_update_prohibited_form` | Phase 3 prohibited form | C-33 |

The pattern: for every criterion that places a structural requirement at a production point, pair it with a machine-readable ARTIFACT frontmatter field tracking compliance at that point. One field per enforcement chain criterion; each field is independently gradeable with the same N/A condition as its criterion.

**Pattern E-02: Field gradeability semantics for criterion-fail states**
When the prohibited form is absent (C-31 FAIL), the correct ARTIFACT field value is `false` -- not absent. Absence of the field fails C-33 independently of whether C-31 passed. This design distinguishes: (a) behavioral failure with correct audit (field present, value `false`); (b) behavioral failure with missing audit (field absent, C-33 FAIL). The field is gradeable even when the criterion it tracks fails -- which enables scorecards to distinguish degrees of compliance at the ARTIFACT layer.

---

### v12 Signal

**Candidate criterion:** `phase1_anchor_prohibition_stated: true | false | n/a` in ARTIFACT frontmatter (parallel to C-33 / `phase3_anchor_update_prohibited_form`).

**What it would add:** Machine-readable tracking of C-27 compliance -- whether "does not pass" language was present at Phase 1 for the preliminary anchor requirement. Currently ARTIFACT has `preliminary_anchor_declared` (C-26 tracking) but no field for C-27. The new field completes the ARTIFACT-layer audit of the Phase 1 enforcement chain.

**Value semantics:** `true` when Phase 1 SUB-STEP 2 carries "does not pass" language (C-27 pass); `false` when Phase 1 produces the anchor but no "does not pass" phrase appears (C-27 fail); `n/a` when PATHWAY INCOMPLETE was not declared (same N/A condition as C-26/C-27).

**Expected behavior under v12 scoring:**
- V-05 (R11): PASS (field present in frontmatter) -- 215 + 5 = 220 (new ceiling)
- V-01 through V-04 (R11): FAIL (field absent) -- 210 - 5 = 205 (Golden floor)
- R10 V-01 through V-04 (retro): field absent -- 190 - 5 = 185 (Passing tier)

**Isolation test for v12:** Predicted V-02-equivalent (field present but value semantics only described positively without failure-mode phrase) would produce ~215 under v12, leaving the C-27 phase1_prohibition_stated escape hatch in prose-only form open at the ARTIFACT layer -- a potential v13 signal.

---

```json
{"top_score": 215, "all_essential_pass": true, "new_patterns": ["Symmetric ARTIFACT audit: for every enforcement chain criterion, pair with a machine-readable frontmatter field tracking compliance at that production point -- one field per criterion, same N/A condition as the criterion, independently gradeable", "Field gradeability design: when the prohibited form is absent (criterion fails), the correct ARTIFACT field value is 'false' not absent -- absence of the field fails C-33 separately from the criterion fail; this distinguishes behavioral failure with correct audit from behavioral failure with missing audit"]}
```
