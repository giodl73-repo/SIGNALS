Scorecard written to `simulations/quest/scorecards/discover-causal-scorecard-R12-2026-03-17.md`.

---

**R12 Results**

| Variation | Score | Tier |
|-----------|-------|------|
| V-01 (C-34 stripped) | **215** | Golden |
| V-02 (C-34 body-placement) | **215** | Golden |
| V-03 (C-27 stripped + field false) | **215** | Golden |
| V-04 (C-27 stripped + field absent) | **210** | Golden (floor) |
| V-05 (Full ceiling + v13 scout) | **220** | Golden (ceiling) |

**All four isolation questions confirmed:**

1. C-34 is independently required -- C-27 PASS does not make the field redundant (V-01 FAIL)
2. Frontmatter placement specifically required -- prose body fails machine-readability (V-02 FAIL)
3. E-02 state (b) confirmed -- C-27 FAIL + field `false` = C-34 PASS (V-03 PASS)
4. E-02 state (c) confirmed -- C-27 FAIL + field absent = C-34 FAIL independently (V-04 FAIL)

**V-03 vs V-04 is the key comparison:** `false` vs absent is the load-bearing distinction. The `false` value signals behavioral failure with correct audit; absence signals behavioral failure with missing audit -- two separately graded failure modes.

**v13 signal (E-03 / C-35):** Phase 6 integration rule naming the C-34 structural requirement and E-02 value semantics. V-05 demonstrates the pattern. Closes the synthesis-point naming chain: C-29 names C-26, C-32 names C-31, C-35 names C-34.

```json
{"top_score": 220, "all_essential_pass": true, "new_patterns": ["Phase 6 synthesis-point naming of C-34 structural requirement: a Phase 6 integration rule explicitly stating that absence of phase1_anchor_prohibition_stated from ARTIFACT frontmatter fails C-34 separately from the C-27 fail, and that false vs absent is the gradeability distinction under E-02 -- closes the synthesis-point naming chain for C-34, parallel to C-29 closing for C-26 and C-32 closing for C-31 (C-35 candidate)"]}
```
cation. Prose body placement is not machine-parseable as structured key-value data. Parallel to R11 V-04 (C-33 body-placement): same structure, same result. C-34 FAIL confirmed.

**Q3 (V-03):** E-02 state (b) confirmed: C-27 FAIL + field `false` = C-34 PASS. When the prohibition phrase is absent at Phase 1, the field with value `false` constitutes a behavioral failure with correct audit. The field is present and accurately reports the C-27 state. C-34 is independently gradeable from C-27 -- it can pass when C-27 fails, provided the field is present with the correct value. C-34 PASS confirmed.

**Q4 (V-04):** E-02 state (c) confirmed: C-27 FAIL + field absent = C-34 FAIL independently. Two distinct failures: C-27 (behavioral -- prohibition phrase absent) and C-34 (audit -- field absent from ARTIFACT). V-03 vs V-04 comparison isolates the load-bearing element: `false` vs absent. The `false` value is what gives C-34 PASS under behavioral failure; absence gives C-34 FAIL independently. C-34 FAIL confirmed, separately from C-27 FAIL.

---

### Excellence Signals (V-05)

**Pattern E-01 (carried, now complete):** The symmetric ARTIFACT audit table is now closed. Every enforcement chain criterion has a paired machine-readable ARTIFACT frontmatter field:

| Production point | Criterion | ARTIFACT field |
|-----------------|-----------|----------------|
| Phase 1 | C-26 (preliminary anchor) | `preliminary_anchor_declared` |
| Phase 1 | C-27 (prohibition phrase) | `phase1_anchor_prohibition_stated` |
| Phase 3 | C-31 (prohibited form) | `phase3_anchor_update_prohibited_form` |
| Phase 6 | C-30 (stale-anchor rule) | `anchor_updated_from_phase1` |

**Pattern E-02 (carried, confirmed):** Field gradeability under criterion-fail states: when C-27 fails (prohibition phrase absent), field `false` gives C-34 PASS; field absent fails C-34 separately. Three distinct states: (a) C-27 PASS + field `true` -- fully compliant; (b) C-27 FAIL + field `false` -- behavioral fail, correct audit, C-34 PASS; (c) C-27 FAIL + field absent -- behavioral fail, missing audit, C-34 FAIL. V-03 demonstrates (b); V-04 demonstrates (c).

**Pattern E-03 (new -- v13 signal):** V-05 adds a Phase 6 integration rule naming the C-34 structural requirement explicitly: absence of `phase1_anchor_prohibition_stated` from ARTIFACT frontmatter fails C-34 separately from the C-27 fail; when C-27 fails the correct field value is `false` not absent. This closes the synthesis-point naming gap for C-34, parallel to C-29 (Phase 6 names C-26) and C-32 (Phase 6 names C-31). No earlier variation carries this Phase 6 rule -- it is the C-35 candidate.

---

**v13 signal:** C-35 -- Phase 6 integration rule naming the C-34 structural requirement with E-02 value semantics. V-05 demonstrates the pattern: a single Phase 6 integration rules entry naming that field absence fails C-34 independently, and that `false` vs absent is the gradeability distinction, closes the synthesis-point naming chain. Under a v13 rubric targeting C-35, V-05 would score above 220 while V-01 through V-04 would not.

---

```json
{"top_score": 220, "all_essential_pass": true, "new_patterns": ["Phase 6 synthesis-point naming of C-34 structural requirement: a Phase 6 integration rule explicitly stating that absence of phase1_anchor_prohibition_stated from ARTIFACT frontmatter fails C-34 separately from the C-27 fail, and that false vs absent is the gradeability distinction under E-02 -- closes the synthesis-point naming chain for C-34, parallel to C-29 closing for C-26 and C-32 closing for C-31 (C-35 candidate)"]}
```

---

### Detailed Criteria Table

#### Essential Criteria -- 60 pts (C-01 through C-05, 12 pts each)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence note |
|----|------|------|------|------|------|---------------|
| C-01 | PASS | PASS | PASS | PASS | PASS | Phase 2 MECHANISM PATHWAY requires step-by-step trace with named agent and observable indicator per step |
| C-02 | PASS | PASS | PASS | PASS | PASS | Phase 3 format "The mechanism fails if Step [N] -- [Name] -- does not occur" requires mechanism break, not metric threshold |
| C-03 | PASS | PASS | PASS | PASS | PASS | Phase 0 INERTIA GATE is mandatory before mechanism work; verdict required before Phase 2 |
| C-04 | PASS | PASS | PASS | PASS | PASS | Phase 6 AMEND produces narrowed claim with mechanism qualifier and scope condition |
| C-05 | PASS | PASS | PASS | PASS | PASS | Phase 4 CONTEXT EVIDENCE assesses evidence per pathway step; "no evidence" is a valid value |

**Essential subtotal: 60/60 all variations**

---

#### Recommended Criteria -- 30 pts (C-06 through C-08, 10 pts each)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence note |
|----|------|------|------|------|------|---------------|
| C-06 | PASS | PASS | PASS | PASS | PASS | Step format ("What changes. Who acts. Observable indicator.") produces testable pathway by construction |
| C-07 | PASS | PASS | PASS | PASS | PASS | Phase 5 CONFOUNDER CHECK requires at least one named alternative cause; silence is not acceptable |
| C-08 | PASS | PASS | PASS | PASS | PASS | Phase 6 AMEND requires bounded scope: mechanism qualifier + population/context/timeframe |

**Recommended subtotal: 30/30 all variations**

---

#### Aspirational Criteria -- 130 pts (C-09 through C-34, 5 pts each)

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
| C-21 | PASS | PASS | PASS | PASS | PASS | Phase 4 NULL-GAP COUNTEREXAMPLE demonstrates "gap: none, tier: T1" as a valid state |
| C-22 | PASS | PASS | PASS | PASS | PASS | Phase 6 PROHIBITED FORM: "Conditioning inertia incorporation on the verdict being Competing or Unclear does not pass" |
| C-23 | PASS | PASS | PASS | PASS | PASS | Phase 6 Mechanism completeness is a standalone named field; embedding in amended clause text does not satisfy |
| C-24 | PASS | PASS | PASS | PASS | PASS | Phase 3 PROHIBITED FORM (C-24): "declaring incompleteness and deferring or omitting step-level falsification does not pass" |
| C-25 | PASS | PASS | PASS | PASS | PASS | Phase 4 PROPAGATION REQUIREMENT: evidence gap propagates to Phase 6 AMEND as standalone named entry |
| C-26 | PASS | PASS | PASS | PASS | PASS | Phase 1 SUB-STEP 2 produces PRELIMINARY ANCHOR at declaration point before Phase 2 tracing |
| C-27 | PASS | PASS | FAIL | FAIL | PASS | V-01/V-02/V-05: "does not pass" prohibition phrase present in SUB-STEP 2. V-03/V-04: SUB-STEP 2 retains required format and anchor instruction but carries no "does not pass" language -- prohibition phrase absent |
| C-28 | PASS | PASS | PASS | PASS | PASS | Phase 3 "a PRELIMINARY ANCHOR is already on record from Phase 1 SUB-STEP 2" -- explicit prior-record acknowledgment present |
| C-29 | PASS | PASS | PASS | PASS | PASS | Phase 6 integration rule: "a Falsification field that first names the anchor here without a corresponding Phase 1 PRELIMINARY ANCHOR does not pass C-26" |
| C-30 | PASS | PASS | PASS | PASS | PASS | Phase 6 integration rule names stale-anchor failure mode; `anchor_updated_from_phase1: true | false | n/a` ARTIFACT field present |
| C-31 | PASS | PASS | PASS | PASS | PASS | Phase 3 ANCHOR-UPDATE PROHIBITED FORM: "recording the updated BEST-TRACEABLE ANCHOR here does not complete the propagation requirement" |
| C-32 | PASS | PASS | PASS | PASS | PASS | Phase 6 integration rule names C-31 structural requirement: "A Phase 3 CONDITIONAL BRANCH that carries only a positive update instruction...does not pass C-31" |
| C-33 | PASS | PASS | PASS | PASS | PASS | `phase3_anchor_update_prohibited_form: true | false | n/a` ARTIFACT frontmatter field present in all variations |
| C-34 | FAIL | FAIL | PASS | FAIL | PASS | V-01: field absent from ARTIFACT frontmatter (C-27 PASS, machine-readability gap). V-02: field in prose body not frontmatter (location spec violated). V-03: C-27 FAIL + field `false` = E-02 state (b) = C-34 PASS. V-04: C-27 FAIL + field absent = E-02 state (c) = C-34 FAIL. V-05: C-27 PASS + field `true` = fully compliant |

**Aspirational subtotals:**
- V-01: 25 PASS x 5 = 125 pts (C-34 FAIL = -5 from 130 ceiling)
- V-02: 25 PASS x 5 = 125 pts (C-34 FAIL = -5 from 130 ceiling)
- V-03: 25 PASS x 5 = 125 pts (C-27 FAIL = -5 from 130 ceiling; C-34 PASS offsets)
- V-04: 24 PASS x 5 = 120 pts (C-27 FAIL -5, C-34 FAIL -5 from 130 ceiling)
- V-05: 26 PASS x 5 = 130 pts (full aspirational ceiling)

---

### Final Score Table

| Variation | Essential | Recommended | Aspirational | **Total** | Tier |
|-----------|-----------|-------------|--------------|-----------|------|
| V-01 (C-34 stripped) | 60 | 30 | 125 | **215** | Golden |
| V-02 (C-34 body-placement) | 60 | 30 | 125 | **215** | Golden |
| V-03 (C-27 stripped + field false) | 60 | 30 | 125 | **215** | Golden |
| V-04 (C-27 stripped + field absent) | 60 | 30 | 120 | **210** | Golden (floor) |
| V-05 (Full ceiling + v13 scout) | 60 | 30 | 130 | **220** | Golden (ceiling) |
