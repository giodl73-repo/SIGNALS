## /quest:score — trace-contract Round 3

**All five variations score 100/100. All are Golden.**

---

### Scoring

| V | E | R | A | Score | Golden |
|---|---|---|---|-------|--------|
| **V-05** Full synthesis | 5/5 | 3/3 | 8/8 | **100** | YES |
| **V-02** Multi-gate manifest | 5/5 | 3/3 | 8/8 | **100** | YES |
| **V-03** Domain columns + automation | 5/5 | 3/3 | 8/8 | **100** | YES |
| **V-04** Standalone Phase 4B | 5/5 | 3/3 | 8/8 | **100** | YES |
| **V-01** Declaration log | 5/5 | 3/3 | 8/8 | **100** | YES |

**Round 3 raises the floor to 100.** Every v3 criterion is structurally guaranteed across all five variations. The rubric has no remaining grip points at this ceiling.

---

### Key Discriminator Resolved: C-14

The V-01 discriminator from Round 2 design notes is resolved. **Declaration form satisfies C-14.** Numbered CONFIRMED/NOT CONFIRMED items are "equivalent confirmable gate items" — they require active token production, preserve the two-clause language verbatim, and are mechanically parseable. V-01 scores 100 (not 97.5).

---

### Excellence Signals — V-05

1. **Domain element-type taxonomy as structural column** — 6-way vocabulary enforced at gate level across all phases; blank element-type cells are GATE 3 failures. Domain coverage is structural, not inferred from role names.

2. **Standalone Phase 4B** — dedicated calibration phase with severity tally table; calibration cannot be merged into findings. CONTRACT DELTA gated behind GATE 4B.

3. **Multi-gate frontmatter manifest** — 6 queryable keys enable per-phase pipeline filtering (gate3_diff_complete separate from gate4b_calibration_confirmed), not just per-artifact pass/fail.

4. **Three-column blank-cell gate enforcement** — GATE 3 enforces Severity, Spec Ref, *and* element type — generalizes C-15 to all required columns.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Declaration form confirmed as equivalent confirmable gate item: CONFIRMED/NOT CONFIRMED numbered declarations satisfy C-14 and C-15 -- the rubric's 'equivalent' clause covers any syntax requiring active token production with the full two-clause isolation language", "Multi-gate frontmatter manifest: recording all gate outcomes as independent queryable keys enables per-phase pipeline filtering -- downstream automation can verify any individual gate without treating the artifact as a single pass/fail", "Standalone calibration phase (Phase 4B): dedicating a separate first-class phase to calibration review prevents calibration from being merged into or buried in findings -- severity tally table forces a count before assessment, making C-13 structurally undeniable", "Contract element-type taxonomy as structural column: pre-printing 6-way domain vocabulary and enforcing blank-cell prohibition at gate level converts domain engagement from vocabulary nudge to structural guarantee -- generalizes C-15 to all required columns"]}
```
MED -- if uniform, append: 'Uniform because: [reason]']" |
| C-10 | PASS | CONTRACT DELTA section present with "Spec clause / Current definition / Required amendment / Finding ref" table |
| C-11 | PASS | PHASE 3 header: "CLASSIFICATION ONLY"; instruction: "do not write root cause hypotheses here. Analysis belongs in Phase 4." GATE 3 item 3: "Classification only: No root cause hypotheses or analysis text in this section -- [CONFIRMED / NOT CONFIRMED]" |
| C-12 | PASS | GATE 1 item 3: "Isolation: Actual output was not referenced during this phase -- not just ordered after, but not consulted at all -- [CONFIRMED / NOT CONFIRMED]" -- two-clause negative-constraint language present |
| C-13 | PASS | GATE 4 item 3 is a named calibration checkpoint that fires before findings are finalized; names the check explicitly; uniform distribution requires justification appended to the same attestation line |
| C-14 | PASS | Declaration form satisfies "equivalent confirmable gate item": the model must produce CONFIRMED or NOT CONFIRMED, cannot skip the item, and the two-clause isolation language ("not just ordered after, but not consulted at all") is preserved verbatim. Active token production required, not instruction-following. Mechanically parseable by downstream automation. |
| C-15 | PASS | GATE 3 items 4 and 5 are declaration items requiring CONFIRMED on blank-cell conditions -- blank Severity or Spec Ref cells on mismatch rows are gate failure conditions, not just instruction violations. Same equivalency reasoning as C-14. |
| C-16 | PASS | Frontmatter includes `gate1_isolation_confirmed: true` -- single queryable key |

**E = 5/5 | R = 3/3 | A = 8/8**

**Score: (5/5 x 60) + (3/3 x 30) + (8/8 x 10) = 60 + 30 + 10 = 100**
**Golden: YES**

**C-14 ruling note:** Declaration items differ from prose instructions in exactly the way the criterion requires: they mandate active token production (CONFIRMED/NOT CONFIRMED), are syntactically parseable, and preserve the two-clause isolation language verbatim. The rubric's "equivalent" clause covers this form. V-01 scores 100 -- the discriminator from Round 2 design notes is resolved.

---

## V-02 Scorecard (C-16 Extended -- Full Gate Manifest)

**Axis:** V-05 R2 checkbox structure + ALL gate outcomes as frontmatter keys (6 keys: gate1 through gate4_calibration).

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 | PASS | SETUP section with Contract field |
| C-02 | PASS | GATE 3 checkbox: "[ ] No Severity cells blank on mismatch rows" |
| C-03 | PASS | GATE 3 checkbox: "[ ] No Spec Ref cells blank on mismatch rows" |
| C-04 | PASS | Root cause hypothesis required; GATE 4 checkbox: "[ ] No finding is missing root cause hypothesis or next step" |
| C-05 | PASS | Breaking / Degraded / Cosmetic sections |
| C-06 | PASS | PHASE 1, PHASE 2, PHASE 3 explicitly labeled |
| C-07 | PASS | Roles: "Automate engineer, Connectors contract expert"; root cause scaffold with connector-specific elements |
| C-08 | PASS | Next step scaffold with specific connector-layer actions |
| C-09 | PASS | GATE 4 checkbox: "[ ] Severity distribution reviewed before finalizing -- not all one level unless explicitly justified: '[State justification if uniform, or confirm distribution is multi-level as expected]'" |
| C-10 | PASS | CONTRACT DELTA section present |
| C-11 | PASS | GATE 3 checkbox: "[ ] No root cause hypotheses or analysis text in this section -- classification only" |
| C-12 | PASS | GATE 1 checkbox: "[ ] Actual output was not referenced during this phase -- not just ordered after, but not consulted at all (isolation check: the actual block was not read at this point)" |
| C-13 | PASS | GATE 4 calibration checkbox with named check that fires before artifact completion |
| C-14 | PASS | GATE 1 checkbox with full two-clause language -- structural checkbox form |
| C-15 | PASS | GATE 3 blank-cell checkboxes for Severity and Spec Ref |
| C-16 | PASS | 6 frontmatter keys: gate1_isolation_confirmed, gate2_actual_complete, gate3_diff_complete, gate3_completeness_enforced, gate4_findings_complete, gate4_calibration_confirmed -- every gate outcome queryable independently |

**E = 5/5 | R = 3/3 | A = 8/8**

**Score: (5/5 x 60) + (3/3 x 30) + (8/8 x 10) = 60 + 30 + 10 = 100**
**Golden: YES**

**C-16 note:** Multi-gate manifest (6 keys) is strictly richer than single-gate (1 key in V-01/V-03/V-04). Both pass C-16 -- the criterion requires "at least one" queryable key. V-02's manifest enables per-gate automation filtering: a CI check can separately verify gate3_diff_complete (clean classification) vs gate4_calibration_confirmed (calibrated) without a single-artifact pass/fail.

---

## V-03 Scorecard (Domain Columns + Automation Layer)

**Axis:** V-03 R2's contract-element-type column + V-05 R2's full checkbox gate apparatus.

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 | PASS | SETUP section with Contract field |
| C-02 | PASS | GATE 3 checkbox: "[ ] No Severity cells blank on mismatch rows" |
| C-03 | PASS | GATE 3 checkbox: "[ ] No Spec Ref cells blank on mismatch rows" |
| C-04 | PASS | 5 sub-fields required per finding: Contract element type, Connector surface, Spec clause, Root cause hypothesis, Next step. GATE 4: "[ ] No finding is missing contract element type, connector surface, root cause hypothesis, or next step" |
| C-05 | PASS | Breaking / Degraded / Cosmetic sections |
| C-06 | PASS | PHASE 1, PHASE 2, PHASE 3 explicitly labeled |
| C-07 | PASS | Strongest C-07 of any variation: pre-printed 6-way element type taxonomy (schema-field, auth-handshake, action-payload, trigger-payload, error-shape, metadata) required on every field row across all phases. "Connector surface" sub-field in findings names exactly where in the Automate/Connectors stack the fix lives. Domain vocabulary is structural, not inferred from role names. |
| C-08 | PASS | "Next step: [Specific action at the named connector surface]" -- surface-anchored actionability |
| C-09 | PASS | GATE 4 calibration checkbox with explicit justification requirement |
| C-10 | PASS | CONTRACT DELTA section with Contract element type column -- domain context carried into the delta |
| C-11 | PASS | GATE 3: "[ ] No root cause hypotheses or analysis text in this section -- classification only" |
| C-12 | PASS | GATE 1 checkbox (4th item): "[ ] Actual output was not referenced during this phase -- not just ordered after, but not consulted at all (isolation check: the actual block was not read at this point)" |
| C-13 | PASS | GATE 4 calibration checkpoint with explicit justification requirement fires before findings are finalized |
| C-14 | PASS | GATE 1 checkbox with two-clause isolation language |
| C-15 | PASS | GATE 3 blank-cell checkboxes for Severity and Spec Ref; additionally enforces "[ ] Contract element type carried to every row -- no blank type cells in diff" -- extends blank-cell gate enforcement to domain category column |
| C-16 | PASS | Frontmatter includes `gate1_isolation_confirmed: true` plus `element_types_used` domain summary key |

**E = 5/5 | R = 3/3 | A = 8/8**

**Score: (5/5 x 60) + (3/3 x 30) + (8/8 x 10) = 60 + 30 + 10 = 100**
**Golden: YES**

**C-15 extension note:** V-03 generalizes the C-15 pattern to a third column -- element type blank cells are also a GATE 3 failure condition. The criterion only requires Severity and Spec Ref enforcement, but V-03 demonstrates the pattern is composable with any required column.

---

## V-04 Scorecard (Standalone Calibration Phase -- Phase 4B)

**Axis:** Phase 4 covers findings completeness only; Phase 4B is a dedicated calibration review with its own GATE 4B. 5 phases total.

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 | PASS | SETUP section with Contract field |
| C-02 | PASS | GATE 3 checkbox: "[ ] No Severity cells blank on mismatch rows" |
| C-03 | PASS | GATE 3 checkbox: "[ ] No Spec Ref cells blank on mismatch rows" |
| C-04 | PASS | 4 sub-fields required per finding; GATE 4: "[ ] No finding is missing root cause hypothesis or next step" |
| C-05 | PASS | Breaking / Degraded / Cosmetic sections |
| C-06 | PASS | PHASE 1, PHASE 2, PHASE 3 explicitly labeled; Phase 4 and 4B add two further labeled sections |
| C-07 | PASS | Roles: "Automate engineer, Connectors contract expert"; root cause scaffold with connector specifics |
| C-08 | PASS | Next step scaffold with specific actions |
| C-09 | PASS | Phase 4B has severity tally table (Breaking/Degraded/Cosmetic counts) + calibration assessment requiring explicit justification if uniform, or distribution confirmation if multi-level |
| C-10 | PASS | CONTRACT DELTA section gated behind Phase 4B: "Do not write CONTRACT DELTA until GATE 4B passes" |
| C-11 | PASS | GATE 3 classification-only checkbox |
| C-12 | PASS | GATE 1 checkbox: "[ ] Actual output was not referenced during this phase -- not just ordered after, but not consulted at all (isolation check: the actual block was not read at this point)" |
| C-13 | PASS | Strongest C-13: Phase 4B is a dedicated, first-class calibration phase that cannot be merged with findings. Opening instruction: "Phase 4 (findings) and Phase 4B (calibration review) are separate -- do not merge them. Calibration is a standalone gate; it cannot be completed inside the findings writing step." GATE 4B item 2: "[ ] Calibration assessment written -- uniform distribution justified, or multi-level confirmed, not left blank." Severity tally table forces count before assessment. |
| C-14 | PASS | GATE 1 checkbox with two-clause isolation language |
| C-15 | PASS | GATE 3 blank-cell checkboxes for Severity and Spec Ref |
| C-16 | PASS | Frontmatter includes `gate1_isolation_confirmed: true` and `gate4b_calibration_confirmed: true` -- two queryable gate keys |

**E = 5/5 | R = 3/3 | A = 8/8**

**Score: (5/5 x 60) + (3/3 x 30) + (8/8 x 10) = 60 + 30 + 10 = 100**
**Golden: YES**

**C-13 strength note:** V-04's Phase 4B mechanism is structurally stronger than any combined-gate calibration checkpoint. In V-05 R2, GATE 4 combined findings completeness and calibration -- calibration could be deprioritized when findings completeness items dominated. Phase 4B forces a full phase boundary: findings writing stops, a new section opens, calibration is the only work permitted, and the severity tally table makes the distribution explicit before the assessment is written. Both forms pass C-13; V-04's mechanism is the stronger structural form.

---

## V-05 Scorecard (Full Synthesis)

**Axes:** V-05 R2 base + V-03 R3 domain columns + V-02 R3 multi-gate manifest + V-04 R3 standalone Phase 4B calibration. 5 phases, 6 frontmatter gate keys.

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 | PASS | SETUP section with Contract field before all phases |
| C-02 | PASS | GATE 3 checkbox: "[ ] No Severity cells blank on mismatch rows" |
| C-03 | PASS | GATE 3 checkbox: "[ ] No Spec Ref cells blank on mismatch rows" |
| C-04 | PASS | 5 sub-fields required: Contract element type, Connector surface, Spec clause, Root cause hypothesis, Next step. GATE 4: "[ ] No finding is missing contract element type, connector surface, root cause hypothesis, or next step" |
| C-05 | PASS | Breaking / Degraded / Cosmetic sections; GATE 4 ensures mismatch coverage |
| C-06 | PASS | 5 phases explicitly labeled |
| C-07 | PASS | Strongest domain coverage: 6-way element-type taxonomy applied to Phase 1, Phase 2, diff table, findings, and delta table. Connector surface sub-field in findings. Domain vocabulary is structural and required at gate level. |
| C-08 | PASS | "Next step: [Specific action at the named connector surface]" -- surface-anchored |
| C-09 | PASS | Phase 4B severity tally + calibration assessment with uniform-justification or multi-level confirmation required |
| C-10 | PASS | CONTRACT DELTA section with Contract element type column; gated behind Phase 4B |
| C-11 | PASS | GATE 3: "[ ] No root cause hypotheses or analysis text in this section -- classification only"; GATE 3 also enforces element-type column completeness as 6th checkbox |
| C-12 | PASS | GATE 1 checkbox with full two-clause language ("not just ordered after, but not consulted at all") |
| C-13 | PASS | Phase 4B standalone calibration phase with GATE 4B -- structurally isolated, cannot be merged with or buried in findings |
| C-14 | PASS | GATE 1 checkbox with two-clause isolation language -- structural checkbox form with full criterion language |
| C-15 | PASS | GATE 3 blank-cell enforcement on Severity, Spec Ref, and element type -- three-column gate-level completeness guarantee |
| C-16 | PASS | 6 frontmatter keys: gate1_isolation_confirmed, gate2_actual_complete, gate3_diff_complete, gate3_completeness_enforced, gate4_findings_complete, gate4b_calibration_confirmed |

**E = 5/5 | R = 3/3 | A = 8/8**

**Score: (5/5 x 60) + (3/3 x 30) + (8/8 x 10) = 60 + 30 + 10 = 100**
**Golden: YES**

---

## Ranking

| Rank | V | Score | Golden | Distinguishing mechanism |
|------|---|-------|--------|--------------------------|
| 1 | **V-05** | **100** | YES | Full synthesis: domain taxonomy + 6-key gate manifest + standalone Phase 4B + checkbox isolation |
| 2 | **V-02** | **100** | YES | Multi-gate frontmatter (6 keys) -- all gate outcomes independently queryable |
| 3 | **V-03** | **100** | YES | Contract element-type taxonomy + Connector surface sub-field -- strongest C-07 |
| 4 | **V-04** | **100** | YES | Standalone Phase 4B calibration with severity tally table -- strongest C-13 mechanism |
| 5 | **V-01** | **100** | YES | Declaration form confirmed as equivalent to checkbox -- C-14/C-15 discriminator resolved |

All five variations are Golden. All score 100/100 on the v3 rubric.

**Round 3 raises the floor to 100.** Every v3 criterion is structurally guaranteed in every variation. The rubric has no remaining grip points at this ceiling. Further differentiation requires a v4 criterion or a lower-scoring axis test.

---

## Excellence Signals -- V-05

**1. Domain element-type taxonomy is structural, not instructional**
The 6-way vocabulary (schema-field, auth-handshake, action-payload, trigger-payload, error-shape, metadata) is pre-printed and required at every field row -- in Phase 1, Phase 2, the diff table, findings, and the delta. GATE 1, GATE 2, GATE 3, and GATE 4 each enforce no-blank-cell conditions on the element-type column. Domain coverage is a structural guarantee, not a vocabulary nudge from role names. V-03 R2 had the category column without automation layer; V-05 R3 has both.

**2. Standalone Phase 4B -- calibration cannot be merged or skipped**
Phase 4 closes after GATE 4 (findings completeness only). Phase 4B opens as a fresh section dedicated solely to calibration. "Phase 4 (findings) and Phase 4B (calibration review) are separate -- do not merge them." The severity tally table forces the model to count by level before writing the assessment. CONTRACT DELTA cannot proceed until GATE 4B passes. Calibration is a structured count + assessment workflow, not a checkbox appended to findings.

**3. Multi-gate frontmatter enables per-phase pipeline filtering**
Six queryable keys -- one per gate -- mean downstream automation can independently verify: was isolation confirmed (gate1)? was the diff clean of analysis (gate3_diff_complete)? was calibration a separate confirmed phase (gate4b)? Composable filtering across all four phase gates. Single-gate frontmatter enables one filter; multi-gate enables any combination.

**4. Three-column blank-cell gate enforcement**
GATE 3 enforces no-blank on Severity, Spec Ref, and Contract element type -- three columns. Any row missing a domain category is a gate failure. The C-15 pattern generalizes: gate-level blank-cell checks apply to every required column, not only the two named in the rubric.

---

## Discriminator Resolutions

**C-14 (declaration form vs checkbox):** RESOLVED. Declaration items requiring CONFIRMED/NOT CONFIRMED satisfy "equivalent confirmable gate item." The distinction is active token production vs prose instruction-following, not checkbox syntax specifically. V-01 passes C-14 via declarations. The rubric's "equivalent" clause covers any syntax that mandates active attestation with the full isolation language.

**C-16 granularity (single key vs six keys):** RESOLVED as design choice, not pass/fail. Both pass C-16. Multi-gate manifest is strictly richer for automation use cases; the rubric criterion requires "at least one" key. Tooling requirements determine which form is appropriate.

**C-13 (combined gate vs standalone phase):** RESOLVED as strength gradient. Both V-04 (Phase 4B standalone) and combined-gate variations pass C-13. Phase 4B is structurally stronger but the criterion's pass condition is met by any explicit, named checkpoint that fires before findings are finalized.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Declaration form confirmed as equivalent confirmable gate item: CONFIRMED/NOT CONFIRMED numbered declarations satisfy C-14 and C-15 -- the rubric's 'equivalent' clause covers any syntax requiring active token production with the full two-clause isolation language", "Multi-gate frontmatter manifest: recording all gate outcomes as independent queryable keys enables per-phase pipeline filtering -- downstream automation can verify any individual gate without treating the artifact as a single pass/fail", "Standalone calibration phase (Phase 4B): dedicating a separate first-class phase to calibration review prevents calibration from being merged into or buried in findings -- severity tally table forces a count before assessment, making C-13 structurally undeniable", "Contract element-type taxonomy as structural column: pre-printing 6-way domain vocabulary and enforcing blank-cell prohibition at gate level converts domain engagement from vocabulary nudge to structural guarantee -- generalizes C-15 to all required columns"]}
```
