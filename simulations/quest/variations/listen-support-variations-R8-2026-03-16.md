title-preceding-verb | ___ | ___ |
| Three named gap sections [C-04: SUSPENDERS] | C-04 | Doc/Design/Operational, each >= 1 artifact | ___ | ___ |
| TABLE CHECK with halt [C-05: SUSPENDERS] | C-05 | TABLE CHECK present; halt names STEP 6 | ___ | ___ |
| Phase 1 discovery register [C-14: SUSPENDERS] | C-14 | >= 3 Phase 1 bodies use VM-xxx-P1 | ___ | ___ |
| Phase 3 operational register [C-14: SUSPENDERS] | C-14 | >= 1 Phase 3 body uses VM-xxx-P3 | ___ | ___ |
| VM Row IDs in STEP 3B [C-16: SUSPENDERS] | C-16 | = total ticket count | ___ | ___ |
| Gate minimum >= 7 [C-18: SUSPENDERS] | C-18 | TABLE CHECK minimum >= 7 | ___ | ___ |
| Halt instruction names STEP 6 [C-19: SUSPENDERS] | C-19 | "Do not proceed to STEP 6" explicit | ___ | ___ |
| ## headlines with VM Row ID [C-20: SUSPENDERS] | C-20 | = total ticket count; inline on ## | ___ | ___ |
| Gate items (a)-(e) all PASS [C-21: SUSPENDERS] | C-21 | 5 items; item (e) = inter-role differentiation | ___ | ___ |
| Belt-and-suspenders labels [C-23: SUSPENDERS] | C-23 | [C-NN: BELT] at generation; [C-NN: SUSPENDERS] at verification | ___ | ___ |
| Materialization with orphan check [C-24: SUSPENDERS] | C-24 | VOCABULARY MATERIALIZATION present; both checks complete | ___ | ___ |

---

### SOLE GATE DECLARATION [C-27: BELT confirmed]

**The CRITERION VERIFICATION SPINE in STEP 10 is the sole final verification gate for this output.**

- The PRE-SPINE PROPERTY TRACE above is a precursor trace. It is not a gate.
- A scorer reading only the PRE-SPINE PROPERTY TRACE has NOT completed verification.
- If the PRE-SPINE PROPERTY TRACE and the CRITERION VERIFICATION SPINE disagree on any criterion, the CRITERION VERIFICATION SPINE governs.
- No other check in this output -- TABLE CHECK, VOCABULARY PRE-FLIGHT GATE, or GAP COVERAGE TRACE -- substitutes for the spine verdict on rubric criterion compliance.

---

### STEP 10 -- CRITERION VERIFICATION SPINE

**SPINE COMPLETENESS PRE-CHECK [C-26: BELT confirmed]:**
Before filling any row, complete this pre-check:
1. List all 27 criterion IDs you must cover: C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-18, C-19, C-20, C-21, C-22, C-23, C-24, C-25, C-26, C-27.
2. Confirm 27 row slots exist in the table below -- one per C-ID.
3. Fill rows C-01 through C-25 and C-27 first. Fill C-26 last (it grades the spine after all other rows are complete).

**[C-25: SUSPENDERS] -- A scorer reading only this table must determine PASS/PARTIAL/FAIL for every criterion without consulting earlier sections. [C-27: SUSPENDERS] -- SOLE GATE DECLARATION above designates this spine as the sole final gate.**

| C-ID | Criterion name | Required condition | Actual value | PASS/PARTIAL/FAIL |
|------|---------------|--------------------|--------------|-------------------|
| C-01 | Title field on each card | Title: field present, descriptive, on every card body (not only in ## heading) | ___ | ___ |
| C-02 | Controlled vocabulary declared and enforced | VOCABULARY MANIFEST present; all card Category/Volume/Severity match declared options | ___ | ___ |
| C-03 | First-person voice throughout | All bodies first-person; constraint stated in prompt; no role-title-preceding-verb | ___ | ___ |
| C-04 | Gap analysis with three named sections | Doc Gaps / Design Gaps / Operational Gaps present; each names >= 1 artifact | ___ | ___ |
| C-05 | Minimum ticket count with structural gate | TABLE CHECK with halt instruction naming STEP 6; gate minimum sums to >= 7 | ___ | ___ |
| C-06 | [Recommended criterion name] | [Required condition] | ___ | ___ |
| C-07 | [Recommended criterion name] | [Required condition] | ___ | ___ |
| C-08 | [Recommended criterion name] | [Required condition] | ___ | ___ |
| C-09 | [Aspirational criterion name] | [Required condition] | ___ | ___ |
| C-10 | [Aspirational criterion name] | [Required condition] | ___ | ___ |
| C-11 | Phase as named card field | Phase: field present on every card | ___ | ___ |
| C-12 | Fallback-grounded severity | Phase 1 = P2/P3; Phase 3 = P0/P1; no Phase 1 P0/P1 non-outage | ___ | ___ |
| C-13 | Mid-output verification block | Audit block between ticket generation and gap analysis | ___ | ___ |
| C-14 | Phase-differentiated body register | Phase 1 bodies use discovery vocabulary; Phase 3 use operational | ___ | ___ |
| C-15 | Temporal adoption window in severity reasoning | Severity tied explicitly to adoption phase window | ___ | ___ |
| C-16 | Prior-tool coverage in verification | Inertia competitor name appears in verification manifest check | ___ | ___ |
| C-17 | Phase-as-severity-key declaration | Phase severity norms stated as inference rule before ticket table | ___ | ___ |
| C-18 | Gate minimum correct at >= 7 | TABLE CHECK minimum sums to >= 7 (not < 7) | ___ | ___ |
| C-19 | TABLE CHECK halt instruction names next step | "Do not proceed to STEP 6" explicit | ___ | ___ |
| C-20 | VM Row ID in ## headline (Compliance Contract) | All ## ticket headlines carry *(VM: VM-xxx-P#)* inline | ___ | ___ |
| C-21 | Five-item gate all present with item (e) | Gate items (a)-(e) all present; item (e) = inter-role differentiation cited by VM Row ID | ___ | ___ |
| C-22 | Prohibited sentinel language on consequence fields | Consequence fields (Adoption cost, Day-90 scenario) free of generic sentinel phrases | ___ | ___ |
| C-23 | Belt-and-suspenders criterion satisfaction | [C-NN: BELT] labels at generation steps; [C-NN: SUSPENDERS] at verification checks | ___ | ___ |
| C-24 | Materialized-view traceability instruction | VOCABULARY MATERIALIZATION table present; orphan type A and type B checks both complete | ___ | ___ |
| C-25 | Criterion-ID-named final verification spine | This table present; one row per criterion; C-IDs in column 1; required condition named | ___ | ___ |
| C-26 | Self-referential criterion enforcement | Count the rows in this table. Are all C-IDs C-01 through C-26 present with Required condition, Actual value, and PASS/PARTIAL/FAIL populated? If yes: write "All 26 C-IDs present; all three columns populated for each." and PASS. If any C-ID is missing or any cell is blank: list the missing C-IDs and FAIL. SPINE COMPLETENESS PRE-CHECK at top of this section confirmed 27 slots before filling began. This row grades itself -- execute the count before writing the Actual value. [C-26: BELT triple-confirmed: obligation in COMPLIANCE CONTRACT + pre-check + this inline instruction] | ___ | ___ |
| C-27 | Spine-as-sole-suspenders declaration | SOLE GATE DECLARATION block present before this spine (YES). PRE-SPINE PROPERTY TRACE explicitly demoted to non-gate trace (YES). This spine declared sole final gate in COMPLIANCE CONTRACT [C-27: BELT] and in SOLE GATE DECLARATION block (YES). No other check substitutes for this spine verdict (YES). | SOLE GATE DECLARATION present; PRE-SPINE PROPERTY TRACE demoted; [C-27: BELT] in COMPLIANCE CONTRACT | PASS |

**SPINE RESULT:** [ ALL ESSENTIAL PASS ] / [ ESSENTIAL FAILURES: C-___ ]
**COMPOSITE ESTIMATE:** ___/185

---

## Variation Summary

| Variation | Axis | C-26 mechanism | C-27 mechanism | Predicted C-26 | Predicted C-27 | Delta vs R7 V-05 |
|-----------|------|---------------|----------------|----------------|----------------|------------------|
| V-01 | Lifecycle emphasis | SPINE COMPLETENESS PRE-CHECK block; C-26 filled last | Row present; no declaration | PASS | FAIL | +5 pts |
| V-02 | Output format | Row present; no pre-check | PRE-SPINE PROPERTY TRACE demotion + SOLE GATE DECLARATION | PARTIAL | PASS | +5 pts |
| V-03 | Phrasing register | Inline self-check instruction in Required condition column | Row present; no declaration | PASS | FAIL | +5 pts |
| V-04 | V-01 + V-02 | SPINE COMPLETENESS PRE-CHECK block | PRE-SPINE PROPERTY TRACE demotion + SOLE GATE DECLARATION | PASS | PASS | +10 pts |
| V-05 | Full synthesis | Pre-check + inline instruction + [C-26: BELT] in COMPLIANCE CONTRACT | SOLE GATE DECLARATION + [C-27: BELT] in COMPLIANCE CONTRACT | PASS | PASS | +10 pts candidate |

**Key scoring question for quest-score:** Does V-03's inline instruction outperform V-01's pre-check block for C-26 reliability? V-05 stacks both -- if the inline instruction is the stronger mechanism, the V-03 approach warrants extraction into the R9 base regardless of V-05's overall score.
