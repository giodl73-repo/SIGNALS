## PHASE 1 — SETUP

### Auto-PASS Conditions

**C-07 auto-PASS** — No prior-round scorecard provided.

**C-05 check** — Deferred until Phase 2 verdict table is complete.

### Formula (v9)
```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 18 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 18.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0.
Each aspirational criterion contributes 10/18 = 0.556 pt.
```

---

## PHASE 2 — Per-Output Scoring

### OUTPUT: V-01 (R9 Full-Stack Baseline)

| Criterion | Evidence Quote | Verdict |
|-----------|---------------|---------|
| C-01 | "1. Write a 25-row scoring table... Rows: C-01 through C-25 in order; no rows skipped or added" | PASS |
| C-02 | "Evidence quote: verbatim or near-verbatim extract from the scored output, clearly tied to the criterion being scored; not a paraphrase of the rubric criterion text" | PASS |
| C-03 | "N_essential = 4, N_recommended = 3, N_aspirational = 18. / An output using N_aspirational=16 (v8 values)... is a C-03 FAIL regardless of other scores" | PASS |
| C-04 | "| Rank | Output | Score | Golden |" with "sorted descending by score" instruction | PASS |
| C-05 | FAILURE PATTERNS section present with structured instructions; no universal FAIL across all 5 variations | PASS (auto) |
| C-06 | EXCELLENCE SIGNALS section present: "For each output-criterion pair where one output outperforms the group by at least one tier... Name the criterion, Name the output, State what the output did differently" | PASS |
| C-07 | No prior-round data provided | PASS (auto) |
| C-08 | C-05 auto-PASS fires | PASS (auto) |
| C-09 | "Score distribution note: State minimum score, maximum score, and spread. State whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread). Note that N_aspirational=18 means each aspirational criterion contributes 10/18 = 0.556 pt" | PASS |
| C-10 | C-05 auto-PASS fires | PASS (auto) |
| C-11 | "Step 1.1 -- Auto-PASS Conditions": C-05, C-07, C-08, C-10, C-21 each named with criterion ID and trigger phrase | PASS |
| C-12 | "Step 1.3 -- Composite Formula: N_essential = 4, N_recommended = 3, N_aspirational = 18" appears in SETUP before Phase 2 | PASS |
| C-13 | "column order is Criterion | Evidence Quote | Verdict... A verdict cell completed before its evidence quote cell violates C-13" — mandate present with named violation | PASS |
| C-14 | 25-row roster (C-01 through C-25) with non-empty diagnostic question for each row; "Step 1.4 -- Criterion Roster with Mechanism-Level Diagnostic Questions" | PASS |
| C-15 | "STOP-4. PHASE 1 complete. Do not open any output file until STOP-4 is passed." | PASS |
| C-16 | "Step 1.1 -- Auto-PASS Conditions" is a dedicated named block separate from "Step 1.4 -- Criterion Roster" | PASS |
| C-17 | C-01: "count exactly 25 verdict rows... A matrix with 23 or 24 rows fails C-01 even if all present rows are correctly scored -- the row count is the falsification test"; C-03: "N_aspirational=16 (v8 values)... is a C-03 FAIL regardless of other scores"; C-20: "Three disqualifying forms: (1) interrogative... (2) conditional... (3) weak-modal..." — all three mechanism-specific | PASS |
| C-18 | "#### REGRESSION SIGNALS" section with "| Criterion | Prior Verdict | Current Verdict | Variation | Mechanism |" table — standalone, 5 columns including all 4 required | PASS |
| C-19 | "C-10 Worked-Example Preservation Rule: The worked example... must be carried forward verbatim from the prior round, or updated to reflect the current round's new axis criterion, whenever the rubric is versioned forward" | PASS |
| C-20 | "The worked example... **must** be carried forward verbatim... The worked example **must** remain in the FAILURE PATTERNS action line" — mandatory verb "must" throughout | PASS |
| C-21 | C-05 auto-PASS fires | PASS (auto) |
| C-22 | "The worked example must remain in the FAILURE PATTERNS action line -- do not relocate it to SETUP, to a roster diagnostic question, or to a preservation checkpoint" — names (a) FAILURE PATTERNS as required location AND (b) "do not relocate it to SETUP" as explicit prohibition | PASS |
| C-23 | C-20 diagnostic: "Three disqualifying forms: (1) interrogative -- 'Has the worked example been carried forward?'...; (2) conditional -- 'If the axis shifts, carry forward the example'...; (3) weak-modal -- 'The worked example should be carried forward'..." — all three named | PASS |
| C-24 | C-22 diagnostic enumerates: "(FAIL) preservation rule is imperative but contains no location language -- e.g., 'must be carried forward verbatim' with no FAILURE PATTERNS reference; (PARTIAL) rule names the required location but omits explicit SETUP exclusion language; (PASS) rule contains both the required location phrase and an explicit SETUP exclusion phrase" — all three verdict levels with structural contrasting examples | PASS |
| C-25 | "Step 1.2 -- Three-Scale Enumeration Principle: **General design rule** (applies to all future criterion authors): Any aspirational criterion whose PARTIAL verdict is defined by having exactly one of two required elements present... must have its diagnostic question enumerate all three verdict cases... Applied in this rubric: C-23 (for C-20), C-24 (for C-22). When authoring a new criterion with a non-trivial PARTIAL threshold, apply this principle before writing the diagnostic question." — standalone named section | PASS |

```
Composite:
- Essential (C-01--C-04): 4/4 x 60 = 60.00 pts
- Recommended (C-05--C-07): 3/3 x 30 = 30.00 pts
- Aspirational (C-08--C-25): 18/18 x 10 = 10.00 pts
- Composite = 100.00/100
- Golden: YES -- all 4 essentials PASS, 100.00 >= 80
```

---

### OUTPUT: V-02 (C-24 PARTIAL Ablation)

| Criterion | Evidence Quote | Verdict |
|-----------|---------------|---------|
| C-01 | Same: "25-row scoring table... Rows: C-01 through C-25 in order; no rows skipped or added" | PASS |
| C-02 | Same mandate | PASS |
| C-03 | "N_aspirational=16 (v8 values)... is a C-03 FAIL" — N_aspirational=18 in formula | PASS |
| C-04 | Leaderboard template present with all 4 columns | PASS |
| C-05 | No universal FAIL across all 5 variations | PASS (auto) |
| C-06 | EXCELLENCE SIGNALS section with instructions present | PASS |
| C-07 | No prior-round data | PASS (auto) |
| C-08 | C-05 auto fires | PASS (auto) |
| C-09 | Distribution note instruction with 0.556 pt per criterion, cluster/discriminate thresholds | PASS |
| C-10 | C-05 auto fires | PASS (auto) |
| C-11 | Step 1.1 — all 5 auto-PASS declarations with criterion ID and trigger | PASS |
| C-12 | Formula N_aspirational=18 in Step 1.3 before Phase 2 | PASS |
| C-13 | Evidence-ordering mandate with named violation "violates C-13" | PASS |
| C-14 | 25-row roster with non-empty diagnostics | PASS |
| C-15 | "STOP-4. PHASE 1 complete. Do not open any output file until STOP-4 is passed." | PASS |
| C-16 | Step 1.1 auto-PASS block separate from Step 1.4 roster | PASS |
| C-17 | C-01/C-03/C-20 diagnostics all mechanism-specific with same content as V-01 | PASS |
| C-18 | REGRESSION SIGNALS section with 5-column table | PASS |
| C-19 | Preservation rule present in Step 1.1 with "must be carried forward verbatim" | PASS |
| C-20 | "must be carried forward verbatim... must remain in the FAILURE PATTERNS action line" — imperative form | PASS |
| C-21 | C-05 auto fires | PASS (auto) |
| C-22 | Same preservation rule: "must remain in the FAILURE PATTERNS action line -- do not relocate it to SETUP" — both required elements | PASS |
| C-23 | C-20 diagnostic: three disqualifying forms enumerated | PASS |
| C-24 | C-22 diagnostic: "(FAIL) preservation rule is imperative but contains no location language; (PARTIAL) rule names the required location but omits explicit SETUP exclusion language. Two-case enumeration earns C-24 PARTIAL. Fewer than two cases earns C-24 FAIL." — **PASS example absent** — exactly two verdict levels illustrated | PARTIAL |
| C-25 | "Step 1.2 -- Three-Scale Enumeration Principle" standalone named section identical to V-01 | PASS |

```
Composite:
- Essential (C-01--C-04): 4/4 x 60 = 60.00 pts
- Recommended (C-05--C-07): 3/3 x 30 = 30.00 pts
- Aspirational (C-08--C-25): 17.5/18 x 10 = 9.72 pts
- Composite = 99.72/100
- Golden: YES -- all 4 essentials PASS, 99.72 >= 80
```

---

### OUTPUT: V-03 (C-24 FAIL Ablation)

| Criterion | Evidence Quote | Verdict |
|-----------|---------------|---------|
| C-01 | 25-row mandate | PASS |
| C-02 | Evidence quote mandate | PASS |
| C-03 | N_aspirational=18 in formula | PASS |
| C-04 | Leaderboard 4-column template | PASS |
| C-05 | No universal FAIL | PASS (auto) |
| C-06 | EXCELLENCE SIGNALS section present | PASS |
| C-07 | No prior-round data | PASS (auto) |
| C-08 | C-05 auto | PASS (auto) |
| C-09 | Distribution note with numeric thresholds and 0.556 contribution | PASS |
| C-10 | C-05 auto | PASS (auto) |
| C-11 | All 5 auto-PASS declarations in Step 1.1 | PASS |
| C-12 | Formula N_aspirational=18 in Step 1.3 | PASS |
| C-13 | Evidence-ordering mandate with "violates C-13" | PASS |
| C-14 | 25-row roster, all non-empty | PASS |
| C-15 | "STOP-4. Do not open any output file..." | PASS |
| C-16 | Standalone auto-PASS block separate from roster | PASS |
| C-17 | C-01/C-03/C-20 diagnostics mechanism-specific | PASS |
| C-18 | REGRESSION SIGNALS section with required columns | PASS |
| C-19 | Preservation rule with "must be carried forward verbatim" | PASS |
| C-20 | "must remain... must be carried forward" — imperative throughout | PASS |
| C-21 | C-05 auto | PASS (auto) |
| C-22 | "must remain in the FAILURE PATTERNS action line -- do not relocate it to SETUP" | PASS |
| C-23 | C-20 three-form enumeration identical to V-01 | PASS |
| C-24 | C-22 diagnostic: "Does the C-22 diagnostic question enumerate verdict cases with structural contrasting examples? A diagnostic question that describes only the FAIL case without illustrating the PARTIAL/PASS boundary earns C-24 FAIL (fewer than two cases)." — **only one case described** (FAIL only; no PARTIAL or PASS illustration) | FAIL |
| C-25 | "Step 1.2 -- Three-Scale Enumeration Principle" standalone named section intact | PASS |

```
Composite:
- Essential (C-01--C-04): 4/4 x 60 = 60.00 pts
- Recommended (C-05--C-07): 3/3 x 30 = 30.00 pts
- Aspirational (C-08--C-25): 17/18 x 10 = 9.44 pts
- Composite = 99.44/100
- Golden: YES -- all 4 essentials PASS, 99.44 >= 80
```

---

### OUTPUT: V-04 (C-25 PARTIAL Ablation)

| Criterion | Evidence Quote | Verdict |
|-----------|---------------|---------|
| C-01 | 25-row mandate | PASS |
| C-02 | Evidence quote mandate | PASS |
| C-03 | N_aspirational=18 in formula | PASS |
| C-04 | Leaderboard template 4 columns | PASS |
| C-05 | No universal FAIL | PASS (auto) |
| C-06 | EXCELLENCE SIGNALS section present | PASS |
| C-07 | No prior-round data | PASS (auto) |
| C-08 | C-05 auto | PASS (auto) |
| C-09 | Distribution note with cluster/discriminate thresholds and 0.556 note | PASS |
| C-10 | C-05 auto | PASS (auto) |
| C-11 | Step 1.1 auto-PASS block with all 5 declarations | PASS |
| C-12 | "Step 1.2 -- Composite Formula: N_essential = 4, N_recommended = 3, N_aspirational = 18" appears before Phase 2 | PASS |
| C-13 | Evidence-ordering mandate with named violation condition | PASS |
| C-14 | 25-row roster, all non-empty including C-24 and C-25 | PASS |
| C-15 | "STOP-4. PHASE 1 complete. Do not open any output file until STOP-4 is passed." | PASS |
| C-16 | Step 1.1 auto-PASS block separate from Step 1.3 roster | PASS |
| C-17 | C-01/C-03/C-20 mechanism-specific diagnostics identical to V-01 | PASS |
| C-18 | REGRESSION SIGNALS section with 5-column table | PASS |
| C-19 | Preservation rule in Step 1.1: "must be carried forward verbatim" | PASS |
| C-20 | "must be carried forward verbatim... must remain in the FAILURE PATTERNS action line" | PASS |
| C-21 | C-05 auto | PASS (auto) |
| C-22 | Preservation rule: "must remain in the FAILURE PATTERNS action line -- do not relocate it to SETUP" | PASS |
| C-23 | C-20 three-form enumeration present | PASS |
| C-24 | C-22 diagnostic: "(FAIL)... 'must be carried forward verbatim' with no FAILURE PATTERNS reference; (PARTIAL) rule names the required location but omits explicit SETUP exclusion language; (PASS) rule contains both the required location phrase and an explicit SETUP exclusion phrase. Note: this criterion applies the three-scale enumeration principle..." — **all three verdict levels** with structural contrasting examples | PASS |
| C-25 | "C-24 | C-22 three-scale enumeration... Note: this criterion applies the three-scale enumeration principle -- any criterion whose PARTIAL is defined by one-of-two-elements-present must have its diagnostic question enumerate FAIL/PARTIAL/PASS with structural contrasts." — principle **embedded in C-24 roster row only**, not a standalone named section; no "Step 1.2 -- Three-Scale Enumeration Principle" exists | PARTIAL |

```
Composite:
- Essential (C-01--C-04): 4/4 x 60 = 60.00 pts
- Recommended (C-05--C-07): 3/3 x 30 = 30.00 pts
- Aspirational (C-08--C-25): 17.5/18 x 10 = 9.72 pts
- Composite = 99.72/100
- Golden: YES -- all 4 essentials PASS, 99.72 >= 80
```

---

### OUTPUT: V-05 (C-24 FAIL + C-25 FAIL Floor)

| Criterion | Evidence Quote | Verdict |
|-----------|---------------|---------|
| C-01 | 25-row mandate | PASS |
| C-02 | Evidence quote mandate | PASS |
| C-03 | N_aspirational=18 in formula | PASS |
| C-04 | Leaderboard 4-column template | PASS |
| C-05 | No universal FAIL | PASS (auto) |
| C-06 | EXCELLENCE SIGNALS section present | PASS |
| C-07 | No prior-round data | PASS (auto) |
| C-08 | C-05 auto | PASS (auto) |
| C-09 | Distribution note with 0.556 and cluster/discriminate thresholds | PASS |
| C-10 | C-05 auto | PASS (auto) |
| C-11 | Step 1.1 with all 5 auto-PASS declarations by criterion ID | PASS |
| C-12 | "Step 1.2 -- Composite Formula: N_aspirational = 18" before Phase 2 | PASS |
| C-13 | Evidence-ordering mandate with "violates C-13" | PASS |
| C-14 | 25-row roster, all non-empty | PASS |
| C-15 | "STOP-4. Do not open any output file until STOP-4 is passed." | PASS |
| C-16 | Step 1.1 auto-PASS block separate from Step 1.3 roster | PASS |
| C-17 | C-01/C-03/C-20 diagnostics: all three mechanism-specific; C-20 names three disqualifying forms | PASS |
| C-18 | REGRESSION SIGNALS section with 5-column table | PASS |
| C-19 | Preservation rule: "must be carried forward verbatim... must remain in the FAILURE PATTERNS action line" | PASS |
| C-20 | "must be carried forward verbatim... must remain" — imperative mandatory verbs | PASS |
| C-21 | C-05 auto | PASS (auto) |
| C-22 | "do not relocate it to SETUP" present; "must remain in the FAILURE PATTERNS action line" present | PASS |
| C-23 | C-20 three-form enumeration present; three forms named | PASS |
| C-24 | C-22 diagnostic: "Does the preservation rule text (in SETUP) explicitly name FAILURE PATTERNS as the required location AND name SETUP as a disqualifying alternative? A rule that is imperative (C-20 PASS) but contains no location language fails C-22. A rule that names the required location but not the SETUP prohibition earns C-22 PARTIAL." — **binary conditional structure**: asks whether rule satisfies C-22 with FAIL/PARTIAL notes but no enumerated FAIL/PARTIAL/PASS verdict-case structure with contrasting examples; C-24 row confirms: "A binary probe ('Does the rule name both required location and SETUP exclusion?') earns C-24 FAIL -- verdict-case enumeration is absent" | FAIL |
| C-25 | C-25 diagnostic: "A roster diagnostic question that references the principle only in passing earns C-25 FAIL -- the principle must appear as a named standalone section, not embedded in a criterion row." No standalone "Three-Scale Enumeration Principle" section in SETUP; Step 1.2 is the composite formula; principle absent from SETUP design notes entirely | FAIL |

```
Composite:
- Essential (C-01--C-04): 4/4 x 60 = 60.00 pts
- Recommended (C-05--C-07): 3/3 x 30 = 30.00 pts
- Aspirational (C-08--C-25): 16/18 x 10 = 8.89 pts
- Composite = 98.89/100
- Golden: YES -- all 4 essentials PASS, 98.89 >= 80
```

---

## PHASE 3 — Synthesis

### FAILURE PATTERNS

Check: Is any criterion FAIL or PARTIAL in ALL 5 variations?

- C-24: PASS / PARTIAL / FAIL / PASS / FAIL — not universal
- C-25: PASS / PASS / PASS / PARTIAL / FAIL — not universal

**C-05 auto-PASS — no universal failures. C-08 auto-PASS. C-10 auto-PASS. C-21 auto-PASS.**

---

### EXCELLENCE SIGNALS

**C-24 — V-01 and V-04 (PASS) vs. group majority (V-02 PARTIAL, V-03 FAIL, V-05 FAIL)**

- V-01 and V-04 enumerate all three verdict levels (FAIL/PARTIAL/PASS) with structural contrasting examples in the C-22 diagnostic question. V-01's FAIL case includes an inline verbatim example ("must be carried forward verbatim" with no FAILURE PATTERNS reference); V-01 and V-04 complete the discrimination triangle so scorers know what to accept, not just what to reject.

**C-25 — V-01, V-02, V-03 (PASS) vs. V-04 (PARTIAL) and V-05 (FAIL)**

- V-01/V-02/V-03 elevate the three-scale enumeration principle to "Step 1.2 -- Three-Scale Enumeration Principle" — a standalone named section encountered before the formula and before the roster. V-04 embeds the principle inside the C-24 criterion row with a note, which satisfies neither standalone nor prior-to-formula positioning. V-05 omits it entirely.

**V-01 exclusive — C-24 PASS + C-25 PASS together (100.00 only variation)**

- V-01 is uniquely top-scored because it satisfies both new R9 criteria simultaneously. Within C-25 PASS, V-01 does two things V-02/V-03 don't emphasize as explicitly: (a) names existing instantiations by criterion ID ("Applied in this rubric: C-23 for C-20, C-24 for C-22"), grounding the abstract rule in concrete current examples; (b) includes an application trigger ("When authoring a new criterion with a non-trivial PARTIAL threshold, apply this principle **before** writing the diagnostic question") that is prescriptive and forward-looking, not merely descriptive. These two properties are not minimum C-25 PASS requirements but distinguish V-01's implementation quality.

---

### REGRESSION SIGNALS

**C-07 auto-PASS — no prior-round scorecard provided.**

---

### LEADERBOARD

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 | V-01 (R9 full-stack baseline) | 100.00 | YES |
| 2 | V-02 (C-24 PARTIAL ablation) | 99.72 | YES |
| 2 | V-04 (C-25 PARTIAL ablation) | 99.72 | YES |
| 4 | V-03 (C-24 FAIL ablation) | 99.44 | YES |
| 5 | V-05 (C-24 FAIL + C-25 FAIL floor) | 98.89 | YES |

Score distribution note: Min = 98.89, Max = 100.00, Spread = 1.11 pts. Scores **cluster** (< 5 pt spread), indicating that C-24 and C-25 are structurally low-weight criteria: each FAIL costs only 0.556 pt, so even the floor variation retains golden status. N_aspirational=18 means each aspirational criterion contributes 10/18 = 0.556 pt to the composite; the two-FAIL floor (V-05) incurs exactly 2 × 0.556 = 1.11 pt total degradation. The rubric's high baseline means golden threshold (80) is never at risk from aspirational-only variations — discrimination between variations is entirely within the 1.11 pt window.

---

## Verdict Summary Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 (E) | PASS | PASS | PASS | PASS | PASS |
| C-02 (E) | PASS | PASS | PASS | PASS | PASS |
| C-03 (E) | PASS | PASS | PASS | PASS | PASS |
| C-04 (E) | PASS | PASS | PASS | PASS | PASS |
| C-05 (R) | PASS | PASS | PASS | PASS | PASS |
| C-06 (R) | PASS | PASS | PASS | PASS | PASS |
| C-07 (R) | PASS | PASS | PASS | PASS | PASS |
| C-08 (A) | PASS | PASS | PASS | PASS | PASS |
| C-09 (A) | PASS | PASS | PASS | PASS | PASS |
| C-10 (A) | PASS | PASS | PASS | PASS | PASS |
| C-11 (A) | PASS | PASS | PASS | PASS | PASS |
| C-12 (A) | PASS | PASS | PASS | PASS | PASS |
| C-13 (A) | PASS | PASS | PASS | PASS | PASS |
| C-14 (A) | PASS | PASS | PASS | PASS | PASS |
| C-15 (A) | PASS | PASS | PASS | PASS | PASS |
| C-16 (A) | PASS | PASS | PASS | PASS | PASS |
| C-17 (A) | PASS | PASS | PASS | PASS | PASS |
| C-18 (A) | PASS | PASS | PASS | PASS | PASS |
| C-19 (A) | PASS | PASS | PASS | PASS | PASS |
| C-20 (A) | PASS | PASS | PASS | PASS | PASS |
| C-21 (A) | PASS | PASS | PASS | PASS | PASS |
| C-22 (A) | PASS | PASS | PASS | PASS | PASS |
| C-23 (A) | PASS | PASS | PASS | PASS | PASS |
| C-24 (A) | **PASS** | **PARTIAL** | **FAIL** | **PASS** | **FAIL** |
| C-25 (A) | **PASS** | **PASS** | **PASS** | **PARTIAL** | **FAIL** |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Standalone Three-Scale Enumeration Principle section cites existing rubric criterion instantiations by ID (e.g., 'Applied in this rubric: C-23 for C-20, C-24 for C-22'), grounding the abstract design rule in concrete current examples so future authors can verify their understanding", "Standalone Three-Scale Enumeration Principle includes an explicit forward application trigger ('when authoring a new criterion with a non-trivial PARTIAL threshold, apply this principle before writing the diagnostic question'), converting the section from a design history note into a prescriptive protocol — the trigger names the decision point, not just the rule"]}
```
