## Round 2 Scoring — quest-golden vs. rubric v2

**Rubric v2 structure:** E=5 (C-01–C-05), R=3 (C-06–C-08), A=4 (C-09–C-12)
**Formula:** `(E_pass/5 * 60) + (R_pass/3 * 30) + (A_pass/4 * 10)`

---

### SCORECARD: V-01 — Output Format (Formula-Anchored COMPOSITE Row)

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|---------|
| C-01 | E | PASS | Steps 1–4 present: generate, score, identify patterns, propose criteria. All 4 phases labeled in order. |
| C-02 | E | PASS | Per-variation SCORECARD table with 12 criterion rows before COMPOSITE. "Complete each variation's full scorecard before starting the next." |
| C-03 | E | PASS | GATE 1 and GATE 2 as separate labeled sections. "DO NOT proceed to Gate 2 until Gate 1 is declared." Each gate has its own state declaration format. |
| C-04 | E | PASS | "Write the full prompt body to: simulations/quest/golden/... Body: complete, verbatim, runnable. Not a summary. Not a description." |
| C-05 | E | PASS | "Write the accumulated rubric to: simulations/quest/rubrics/... All criteria from all rounds, all five fields per criterion, round of addition noted." |
| C-06 | R | PASS | Step 3 requires: Pattern name, Mechanism (structural property), Principle (transferable rule — "not 'V-02 scored higher' but the design choice that caused it"), Scope. |
| C-07 | R | PASS | Step 4 has all five fields: ID, Text, Weight, Category, Pass condition. |
| C-08 | R | PASS | Gate 2: "Name the current round by label … Name the immediately preceding round by label … Do not write 'the last two rounds.'" |
| C-09 | A | PASS | "Before writing any variation, assign axes and verify at least two variations will diverge on at least one criterion." Active spread-design instruction prior to any scoring. |
| C-10 | A | PASS | "Rounds where all variations produce identical composite scores generate no excellence patterns — no patterns means the round does not count toward the two consecutive zero-pattern rounds required for plateau detection." Causal chain stated. |
| C-11 | A | PASS | COMPOSITE row template: `Count criteria from active rubric: E=[n], R=[n], A=[n]. Compute: (E_pass/[E] * 60) + ... Do not use N_essential, N_recommended, or N_aspirational as denominators.` Formula anchored at point of use with resolved-count placeholders. |
| C-12 | A | FAIL | Convergence section has two labeled gates and a DUAL CONVERGENCE RULE, but contains no explicit anti-conflation guard. No "DO NOT conflate," no IS:/IS NOT: pair. Gate labeling alone present; prohibition absent. |
| **COMPOSITE** | — | **97.5** | E=[5], R=[3], A=[4]. All E pass, all R pass, 3/4 A pass (C-12 fails). `(5/5 * 60) + (3/3 * 30) + (3/4 * 10)` = 60 + 30 + 7.5 = **97.5** |

---

### SCORECARD: V-02 — Phrasing Register (IS:/IS NOT: Anti-Conflation Constitutive Pair)

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|---------|
| C-01 | E | PASS | Steps 1–4 labeled and present with substantive instructions in each. |
| C-02 | E | PASS | Cross-variation table with all 12 criteria as rows and all variations as columns. "DO NOT proceed to Step 3 until all cells have per-criterion results with evidence." |
| C-03 | E | PASS | GATE 1 and GATE 2 separately labeled; IS:/IS NOT: definitions precede them. Each gate has its own state declaration format. |
| C-04 | E | PASS | Golden artifact instructions: full prompt body, verbatim, runnable. |
| C-05 | E | PASS | Rubric artifact instructions: all criteria accumulated, all five fields, round of addition. |
| C-06 | R | PASS | Step 3: pattern name, mechanism (structural property present in passing/absent in failing), principle (design choice not comparison), scope. |
| C-07 | R | PASS | Step 4: all five fields listed. |
| C-08 | R | PASS | Gate 2 names current and preceding rounds by label; prohibits "the previous two rounds." |
| C-09 | A | PASS | "Before writing any variation, assign axes. Verify at least two variations target different criteria." Round 1/Round 2+ axis instruction present. |
| C-10 | A | PASS | "identical scores produce no spread, no spread produces no patterns, and no patterns cannot count toward the two-round plateau requirement." Full causal chain. |
| C-11 | A | FAIL | Step 2 COMPOSITE row is a bare empty cell in the cross-variation table. No formula template with resolved denominators. No instruction to count criteria or produce integer denominators before writing composite. |
| C-12 | A | PASS | Convergence section opens with: `**INDEPENDENT GATES IS:** two separately labeled sections … **INDEPENDENT GATES IS NOT:** a merged paragraph that combines criterion pass-rates with pattern-discovery history into a single verdict.` Explicit IS:/IS NOT: constitutive pair naming the forbidden form. |
| **COMPOSITE** | — | **97.5** | E=[5], R=[3], A=[4]. All E pass, all R pass, 3/4 A pass (C-11 fails). `(5/5 * 60) + (3/3 * 30) + (3/4 * 10)` = 60 + 30 + 7.5 = **97.5** |

---

### SCORECARD: V-03 — Lifecycle Emphasis (Denominator-Resolution Sub-Step)

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|---------|
| C-01 | E | PASS | Steps 1–4 all present with full instructions. Sub-steps within Step 2 do not split the phase structure. |
| C-02 | E | PASS | Sub-step 2a: per-criterion table for each variation with 12 rows before composite. "DO NOT proceed to Step 3 until all variations have completed all three sub-steps." |
| C-03 | E | PASS | "CONVERGENCE CHECK — TWO INDEPENDENT GATES. Execute both gates fully and separately." GATE 1 and GATE 2 with separate declarations. |
| C-04 | E | PASS | Golden artifact: full, verbatim, runnable. |
| C-05 | E | PASS | Rubric artifact: all criteria, all rounds, all five fields. |
| C-06 | R | PASS | Step 3 pattern format: name, mechanism, principle (transferable rule), scope. |
| C-07 | R | PASS | Step 4: all five fields. |
| C-08 | R | PASS | Gate 2 names current and preceding rounds by label; prohibits "the last two rounds." |
| C-09 | A | PASS | "Active spread-design: before writing any variation, assign axes and verify divergence. A round where all variations produce identical composite scores cannot advance plateau detection." Round 1/2+ axis instruction included. |
| C-10 | A | PASS | "Identical scores → no spread → no patterns → round does not count toward the two-round plateau requirement." Full causal chain with arrow notation. |
| C-11 | A | PASS | Sub-step 2b forces `E = [count]`, `R = [count]`, `A = [count]` as integer counts before COMPOSITE. "DO NOT proceed to sub-step 2c until this block is written with integer counts." Sub-step 2c: `COMPOSITE = (E_pass/[E] * 60) + ...` uses the resolved counts. |
| C-12 | A | PASS | Convergence section: "Execute both gates fully and separately. Do not conflate them. Do not write a single paragraph covering both. The two gates ask different questions … require different evidence, and must be declared separately." Explicit imperative anti-conflation guard. |
| **COMPOSITE** | — | **100** | E=[5], R=[3], A=[4]. All pass. `(5/5 * 60) + (3/3 * 30) + (4/4 * 10)` = 60 + 30 + 10 = **100** |

---

### SCORECARD: V-04 — Output Format × Phrasing Register (COMPOSITE Template + IS:/IS NOT: Anti-Conflation Guard)

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|---------|
| C-01 | E | PASS | All four steps present: generate (Step 1), score (Step 2), identify patterns (Step 3), propose criteria (Step 4). |
| C-02 | E | PASS | Per-variation SCORECARD table, 12 criterion rows before COMPOSITE. "DO NOT proceed to Step 3 until all scorecards have evidence in every row." |
| C-03 | E | PASS | GATE 1 and GATE 2 as separate labeled sections. CONFLATION IS/IS NOT pair defines the required two-section form before the gates. |
| C-04 | E | PASS | "Body: complete, verbatim, runnable. Not a summary. Not a description." |
| C-05 | E | PASS | Rubric artifact: all criteria from all rounds, all five fields. |
| C-06 | R | PASS | Step 3: pattern name, mechanism, principle (transferable rule), scope. |
| C-07 | R | PASS | Step 4: all five fields. |
| C-08 | R | PASS | Gate 2 names rounds by label; prohibits "the last two rounds" and "the previous two rounds." |
| C-09 | A | PASS | "Active spread-design: assign axes before writing. Verify at least two variations target different criteria." Round 1/2+ instruction present. |
| C-10 | A | PASS | "identical scores produce no excellence patterns, and no new patterns cannot count toward the two-round plateau gate." Causal chain explicit. |
| C-11 | A | PASS | COMPOSITE row template: `Count from {rubric-content}: E=[n], R=[n], A=[n]. Formula: (E_pass/[E] * 60) + (R_pass/[R] * 30) + (A_pass/[A] * 10) = [result]`. Explicit: "Do not use N_essential, N_recommended, or N_aspirational." Formula anchored at point of use with concrete-count requirement. |
| C-12 | A | PASS | Convergence section: `**CONFLATION IS:** writing a single paragraph that addresses both … **CONFLATION IS NOT:** two separately labeled sections, each with its own question, its own evidence, and its own state declaration. This is the only acceptable form.` IS:/IS NOT: constitutive pair explicitly naming merged-paragraph as forbidden. |
| **COMPOSITE** | — | **100** | E=[5], R=[3], A=[4]. All pass. `(5/5 * 60) + (3/3 * 30) + (4/4 * 10)` = 60 + 30 + 10 = **100** |

---

### SCORECARD: V-05 — Inertia Framing × Lifecycle Emphasis (Status-Quo Golden Competitor + Denominator Audit)

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|---------|
| C-01 | E | PASS | Steps 1–4 all present with full instructions; sub-steps internal to Step 2 don't break the phase structure. |
| C-02 | E | PASS | Sub-step 2a: per-criterion table with all 12 rows. "DO NOT proceed to sub-step 2b until this block is written." Per-criterion scoring precedes composite for every variation. |
| C-03 | E | PASS | "CONVERGENCE CHECK — TWO INDEPENDENT GATES." Section header explicitly labels intent. GATE 1 and GATE 2 separately declared with own state formats. |
| C-04 | E | PASS | Golden artifact: full prompt body, verbatim, runnable. |
| C-05 | E | PASS | Rubric artifact: all criteria, all rounds, all five fields. |
| C-06 | R | PASS | Step 3: pattern name, mechanism, principle (transferable rule), scope. |
| C-07 | R | PASS | Step 4: all five fields. |
| C-08 | R | PASS | Gate 2 names current and preceding rounds by label; prohibits "the last two rounds." |
| C-09 | A | PASS | "Before writing each variation, state: a. Which failure mode(s) this variation closes; b. The structural mechanism." Per-variation accountability label forces divergent design before writing. Round 1/2+ axis instruction included. |
| C-10 | A | PASS | "Identical scores produce no spread; no spread produces no new patterns; no new patterns means the round does not count toward the two-round plateau gate." Full causal chain. |
| C-11 | A | PASS | Sub-step 2b: `E = [count] — verify by listing C-IDs in this tier`. Integer counts with verification. "DO NOT fill the COMPOSITE row until this block contains integer counts (not N_essential, not N_recommended, not N_aspirational)." Sub-step 2c uses resolved formula. |
| C-12 | A | PASS | Convergence section: "This section closes Status-Quo Failure 2. Two labeled sections, each fully executed." Status-Quo Golden section at top explicitly names Failure 2 as "one paragraph, two gates, zero auditability." Two-pronged: motivational at generation time + structural at gate section. |
| **COMPOSITE** | — | **100** | E=[5], R=[3], A=[4]. All pass. `(5/5 * 60) + (3/3 * 30) + (4/4 * 10)` = 60 + 30 + 10 = **100** |

---

### Round 2 Summary

| V | COMPOSITE | RANK | Essential failures |
|---|-----------|------|--------------------|
| V-03 | 100 | 1 (tied) | none |
| V-04 | 100 | 1 (tied, preferred — minimal structure) | none |
| V-05 | 100 | 1 (tied) | none |
| V-01 | 97.5 | 4 (tied) | none |
| V-02 | 97.5 | 4 (tied) | none |

**Tiebreak (V-03/V-04/V-05):** V-04 preferred. Uses per-variation scorecards (V-01 style, no sub-step overhead) plus IS:/IS NOT pair in convergence — the simplest prompt body achieving 100.

---

### Excellence Patterns — Round 2

**Criterion spread observed:**

**C-11 (aspirational):** V-01, V-03, V-04, V-05 PASS; V-02 FAIL.
- Pattern name: Formula-at-point-of-use
- Mechanism: V-02 uses a cross-variation summary table where the COMPOSITE cell is empty — no formula template is provided at scoring time, and no sub-step forces denominator resolution. V-01/V-04 anchor the resolved formula in the COMPOSITE row template at the moment the operator writes scores. V-03/V-05 add a denominator-resolution sub-step that must complete before the COMPOSITE row can be filled.
- Principle: An empty COMPOSITE row provides no compliance guarantee; the formula must appear either as a pre-filled template that the operator fills in by counting, or as a blocking sub-step that forces the count as a named lifecycle action.
- Scope: transferable

**C-12 (aspirational):** V-02, V-03, V-04, V-05 PASS; V-01 FAIL.
- Pattern name: Explicit anti-conflation guard
- Mechanism: V-01 has two labeled gates and "DO NOT proceed to Gate 2 until Gate 1 is declared" — but no explicit prohibition against merging them into a single paragraph. V-02/V-04 use IS:/IS NOT: constitutive pairs. V-03 uses imperative prohibitions ("Do not conflate them. Do not write a single paragraph covering both."). V-05 motivates the prohibition by naming the merged-paragraph failure mode at the top of the skill.
- Principle: Gate labels without an explicit prohibition leave a compliance gap; an operator can satisfy the label requirement while still merging the evidence into a compound paragraph. The anti-conflation guard must be stated as a prohibition (imperative or constitutive), not implied by structure.
- Scope: transferable

**Are these new patterns?** Both C-11 and C-12 were absorbed into the v2 rubric from Round 1 signals. Round 2's spread is entirely on these two criteria — no new axis of divergence appeared. The mechanisms above confirm and refine the criteria but generate no new proposed criteria beyond C-01–C-12. **Round 2 finds zero new excellence patterns.**

**All-fail criteria:** None. All criteria passed by at least one variation.

---

### Convergence Check

**GATE 1 — TRIAL CONVERGENCE**

Essential criteria C-01–C-05 against all 5 variations:

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| C-01 | PASS | PASS | PASS | PASS | PASS |
| C-02 | PASS | PASS | PASS | PASS | PASS |
| C-03 | PASS | PASS | PASS | PASS | PASS |
| C-04 | PASS | PASS | PASS | PASS | PASS |
| C-05 | PASS | PASS | PASS | PASS | PASS |

**TRIAL CONVERGED:** all 5 variations pass all essential criteria this round.

---

**GATE 2 — PLATEAU DETECTION**

Round 2 (current): Step 3 found zero new excellence patterns — the C-11 and C-12 spread confirms criteria already in rubric v2; no new proposed criteria generated.

Round 1 (preceding): Step 3 found two new excellence patterns — C-11 (composite formula with concrete denominators) and C-12 (anti-conflation guard) — which were absorbed into rubric v2.

**QUEST NOT PLATEAUED:** Round 1 found new excellence patterns (C-11, C-12). Two consecutive zero-pattern rounds not yet achieved. Round 3 required.

---

**DUAL CONVERGENCE:** TRIAL CONVERGED but QUEST NOT PLATEAUED. Not golden this round. Proceed to Round 3 with V-04 as anchor.

---

### Round 3 Design Note

V-04 achieves 100 in Round 2. For Round 3, variations must be designed around V-04's structure and probe for any remaining axes of divergence. Since all criteria now pass in V-04, Round 3 variations need to test whether V-04's mechanisms are stable across rubric versions and skill types (axis: transferability), or whether any existing criteria can be strengthened (axis: scoring-granularity). If Round 3 also finds zero new patterns, plateau is declared and V-04 is golden.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": []}
```
