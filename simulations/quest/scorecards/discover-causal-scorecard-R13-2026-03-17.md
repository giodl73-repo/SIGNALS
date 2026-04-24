---

## discover-causal Scorecard — Round 13

**R13 Results**

| Variation | Score | Tier |
|-----------|-------|------|
| V-01 (C-35 element-1 only) | **220** | Golden |
| V-02 (C-35 element-2 only) | **220** | Golden |
| V-03 (C-35 wrong location) | **220** | Golden |
| V-04 (C-35 paraphrase) | **220** | Golden |
| V-05 (Full C-35 ceiling) | **225** | Golden (ceiling) |

**All four isolation questions confirmed.** All variations start from the R12 V-05 ceiling (225/225 under v13). The only modification in each variation is the C-35 handling. C-27 and C-34 are PASS across all R13 variations (Phase 1 PROHIBITED FORM and ARTIFACT field both preserved from R12 V-05), making C-35 gradeable in all cases.

---

**C-35 fail analysis per variation:**

- **V-01:** Element-1 present (`"absent fails C-34 separately from any C-27 outcome"`) but element-2 absent — no `false`-vs-absent E-02 clause. Partial naming → FAIL.
- **V-02:** Element-2 present (`"false vs absent is the E-02 gradeability distinction"`) but element-1 absent — `"fails C-34 independently"` without naming the C-27 fail counterpart. Independence of the two failure modes not named. Partial naming → FAIL.
- **V-03:** Both elements placed in Phase 1 ARTIFACT NOTE; Phase 6 carries no C-35 rule. Wrong location → FAIL.
- **V-04:** Phase 6 paraphrase (`"record the field as false — do not leave it out"`) without naming `"fails C-34 separately from the C-27 fail"` or `"E-02 gradeability distinction"` explicitly. Paraphrase → FAIL.
- **V-05:** Both elements explicit in Phase 6. PASS → 225/225.

**Key structural confirmation:** V-01 vs V-02 symmetry (both 220) confirms the conjunctive two-element requirement — neither element alone satisfies C-35. The synthesis-point naming chain is now fully closed and confirmed.

```json
{"top_score": 225, "all_essential_pass": true, "new_patterns": []}
```
Questions

| Q | Test | Degraded var | Score | V-05 | Finding |
|---|------|-------------|-------|------|---------|
| Q1 | Element (2) (`false`-vs-absent E-02 clause) independently required? | V-01 | 220 | 225 | YES -- element (2) independently required |
| Q2 | Element (1) ("separately from C-27 fail") independently required? | V-02 | 220 | 225 | YES -- element (1) independently required |
| Q3 | Phase 6 location binding (vs Phase 1)? | V-03 | 220 | 225 | YES -- Phase 1 placement fails |
| Q4 | Explicit structural naming required (vs paraphrase)? | V-04 | 220 | 225 | YES -- paraphrase fails |
| Q5 | Elements (1) and (2) symmetric? | V-01 vs V-02 | 220 / 220 | -- | YES -- both independently required, same 5-pt delta |

---

### Excellence Signals (V-05)

**Pattern E-01 (carried, complete):** The symmetric ARTIFACT audit table is closed. Every enforcement chain criterion has a paired machine-readable ARTIFACT frontmatter field:

| Production point | Criterion | ARTIFACT field |
|-----------------|-----------|----------------|
| Phase 1 | C-26 (preliminary anchor) | `preliminary_anchor_declared` |
| Phase 1 | C-27 (prohibition phrase) | `phase1_anchor_prohibition_stated` |
| Phase 3 | C-31 (prohibited form) | `phase3_anchor_update_prohibited_form` |
| Phase 6 | C-30 (stale-anchor rule) | `anchor_updated_from_phase1` |

**Pattern E-02 (carried, confirmed):** Field gradeability under criterion-fail states. When C-27 fails, field `false` gives C-34 PASS; field absent fails C-34 separately. Three states: (a) C-27 PASS + field `true` -- fully compliant; (b) C-27 FAIL + field `false` -- behavioral fail, correct audit, C-34 PASS; (c) C-27 FAIL + field absent -- behavioral fail, missing audit, C-34 FAIL.

**Pattern E-03 (carried, now codified as C-35):** Phase 6 synthesis-point naming of the C-34 structural requirement. R13 confirms the conjunctive two-element structure: both elements are independently required (V-01 vs V-02 symmetric fail), Phase 6 location is binding (V-03 fail), and explicit structural language is required over paraphrase (V-04 fail). No new E-0N pattern emerges -- R13 closes structural analysis of C-35.

**Synthesis-point naming chain -- complete:**

| Criterion named | Named at Phase 6 by |
|----------------|---------------------|
| C-26 (Phase 1 anchor co-location) | C-29 |
| C-31 (Phase 3 prohibited form) | C-32 |
| C-34 (ARTIFACT field required) | C-35 |
| C-30 (stale-anchor rule) | self (is at Phase 6) |

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

#### Aspirational Criteria -- 135 pts (C-09 through C-35, 5 pts each)

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
| C-27 | PASS | PASS | PASS | PASS | PASS | Phase 1 PROHIBITED FORM present in all variations (inherited from R12 V-05 base): "does not pass" language co-located with anchor requirement at Phase 1 |
| C-28 | PASS | PASS | PASS | PASS | PASS | Phase 3 "a PRELIMINARY ANCHOR is already on record from Phase 1 SUB-STEP 2" -- explicit prior-record acknowledgment present |
| C-29 | PASS | PASS | PASS | PASS | PASS | Phase 6 integration rule: "a Falsification field that first names the anchor here without a corresponding Phase 1 PRELIMINARY ANCHOR does not pass C-26" |
| C-30 | PASS | PASS | PASS | PASS | PASS | Phase 6 integration rule names stale-anchor failure mode; `anchor_updated_from_phase1: true | false | n/a` ARTIFACT field present |
| C-31 | PASS | PASS | PASS | PASS | PASS | Phase 3 ANCHOR-UPDATE PROHIBITED FORM: "recording the updated BEST-TRACEABLE ANCHOR here does not complete the propagation requirement" |
| C-32 | PASS | PASS | PASS | PASS | PASS | Phase 6 integration rule names C-31 structural requirement: "A Phase 3 CONDITIONAL BRANCH that carries only a positive update instruction...does not pass C-31" |
| C-33 | PASS | PASS | PASS | PASS | PASS | `phase3_anchor_update_prohibited_form: true | false | n/a` ARTIFACT frontmatter field present in all variations |
| C-34 | PASS | PASS | PASS | PASS | PASS | `phase1_anchor_prohibition_stated: true` in all ARTIFACT frontmatters; C-27 PASS in all variations -- field value `true` -- C-34 PASS |
| C-35 | FAIL | FAIL | FAIL | FAIL | PASS | V-01: element-1 present ("absent fails C-34 separately from any C-27 outcome") but element-2 absent (no `false`-vs-absent E-02 clause) -- partial naming FAIL; V-02: element-2 present ("`false` vs absent is the E-02 gradeability distinction") but element-1 absent ("fails C-34 independently" without naming the C-27 fail counterpart -- independence of two failure modes not named) -- partial naming FAIL; V-03: both elements placed in Phase 1 ARTIFACT NOTE; Phase 6 carries no C-35 rule -- wrong location FAIL; V-04: Phase 6 paraphrase ("record the field as `false` -- do not leave it out") without naming "fails C-34 separately from the C-27 fail" or "E-02 gradeability distinction" explicitly -- paraphrase FAIL; V-05: Phase 6 carries both elements verbatim: (1) "absence of the field fails C-34 separately from the C-27 fail" and (2) "`false` -- not absent; absence of the field fails C-34 separately from the C-27 fail" -- PASS |

**Aspirational subtotals:**
- V-01: 26 PASS x 5 = 130 pts (C-35 FAIL = -5 from 135 ceiling)
- V-02: 26 PASS x 5 = 130 pts (C-35 FAIL = -5 from 135 ceiling)
- V-03: 26 PASS x 5 = 130 pts (C-35 FAIL = -5 from 135 ceiling)
- V-04: 26 PASS x 5 = 130 pts (C-35 FAIL = -5 from 135 ceiling)
- V-05: 27 PASS x 5 = 135 pts (full aspirational ceiling)

---

### Final Score Table

| Variation | Essential | Recommended | Aspirational | **Total** | Tier |
|-----------|-----------|-------------|--------------|-----------|------|
| V-01 (element-1 only) | 60 | 30 | 130 | **220** | Golden |
| V-02 (element-2 only) | 60 | 30 | 130 | **220** | Golden |
| V-03 (wrong location) | 60 | 30 | 130 | **220** | Golden |
| V-04 (paraphrase) | 60 | 30 | 130 | **220** | Golden |
| V-05 (full ceiling) | 60 | 30 | 135 | **225** | Golden (ceiling) |

---

### Isolation Analysis

**Q1 (V-01 vs V-05):** Element (2) (`false`-vs-absent E-02 clause) is independently required. V-01 names field-absence as a C-34 fail mode but omits the `false`-vs-absent distinction. A model reading V-01 knows field absence is bad but does not have the rule that `false` (not absent) is the correct value for a behavioral-fail case. 5-pt delta confirms element (2) as independently load-bearing.

**Q2 (V-02 vs V-05):** Element (1) ("separately from C-27 fail" naming) is independently required. V-02 names the `false`-vs-absent E-02 distinction but uses "fails C-34 independently" without naming C-27 as the counterfactual. The independence claim requires naming both sides of the two-mode distinction. 5-pt delta confirms element (1) as independently load-bearing.

**Q3 (V-03 vs V-05):** Phase 6 location is binding. Both elements present at Phase 1 ARTIFACT NOTE does not satisfy C-35 -- synthesis-point naming requires the rule to appear in Phase 6 where all enforcement chains converge. Placement at Phase 1 is informational but does not constitute synthesis-point enforcement. Parallel to C-32 requiring Phase 6 over Phase 3 for C-31 structural naming.

**Q4 (V-04 vs V-05):** Explicit structural naming is required. V-04's paraphrase conveys the behavioral instruction but omits the structural framing: it does not name that field absence fails C-34 separately from the C-27 fail, and does not name the E-02 gradeability distinction. Conceptual coverage alone does not close the escape hatch -- the exact structural terms are load-bearing.

**Q5 (V-01 vs V-02):** Elements (1) and (2) are symmetric. Both score 220 under C-35 FAIL. The two-element conjunctive requirement is confirmed: neither element alone satisfies C-35. A response must name both the independence of failure modes and the `false`-vs-absent gradeability distinction.

---

```json
{"top_score": 225, "all_essential_pass": true, "new_patterns": []}
```
