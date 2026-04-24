Written to `simulations/quest/rubrics/discover-feasibility-alt-rubric-v7-2026-03-17.md`.

---

**Two new criteria extracted from R6 excellence signals:**

| ID | Source | Upgrades | Core distinction |
|----|--------|----------|-----------------|
| C-22 | V-02 R6 dual-assertion checklist | C-20 | Converts C-20 from a single-location forward gate into a two-condition checklist, each with independent repair instructions. C-20 passes when a gate names the table-side location; C-22 additionally requires an explicit named condition confirming the formula-side location (Item C equation label), eliminating the ambiguity where a model could satisfy C-20 on table evidence alone while leaving the formula label unchecked. |
| C-23 | V-03 R6 explicit 3-anchor propagation list | C-21 | Converts C-21 from a field-existence + downstream-count check into a source-level contract declaration. C-21 passes when the named-incumbent field exists and propagates to 2+ downstream anchors (verifiable only by scanning downstream sections); C-23 additionally requires the field itself to list all three anchors by location and form with a minimum-count declaration, making the propagation contract checkable at the declaration point. |

**Key design decisions:**
- C-22 prerequisites: same as C-20 (C-15 PASS + C-16 PASS); binary FAIL when dual-assertion form is absent or when condition (ii) (formula-side location) is not named as an independent check
- C-23 passes N/A when no competitive framing is used; C-21 PASS without the explicit anchor list is C-23 FAIL
- Aspirational denominator `/13` → `/15`; all-pass composite remains 100
- N/A handling extended: C-22 passes N/A if C-19 conditions are N/A; C-23 passes N/A if no competitive inertia framing is used

---

## Essential Criteria

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | INFERENCE GATE has all required fields | completeness | essential | Feature, Team, and Timeline are all present and non-empty in the INFERENCE GATE section before any analysis begins. Focus is optional; its absence does not fail C-01. |
| C-02 | VERDICT has score + label consistent with range, prerequisites iff FEASIBLE WITH CAVEATS + RED | correctness | essential | VERDICT contains a numeric score (0-100) and a label (NOT FEASIBLE, FEASIBLE WITH CAVEATS, or FEASIBLE) both present. Label is consistent with score range: <50 = NOT FEASIBLE, 50-74 = FEASIBLE WITH CAVEATS, >=75 = FEASIBLE. Prerequisites listed iff label is FEASIBLE WITH CAVEATS and at least one RED component exists. |
| C-03 | ARCHITECT table has traffic-light ratings with RED Blockers | correctness | essential | Every component row in the ARCHITECT table carries GREEN, YELLOW, or RED. Every RED-rated component has a corresponding RED Blockers entry with all three sub-fields: blocker statement, Lift condition, and Do-nothing cost. "No RED components." is acceptable iff no RED rows exist. |
| C-04 | Inertia surfaces in all four required locations | coverage | essential | All four inertia surfaces present: (1) INERTIA: STATUS QUO section with Baseline sentence, (2) Do-nothing cost column in ARCHITECT table with a value on every row, (3) "Not building this means:" line in VERDICT, (4) "Inertia saved:" line on every amendment in AMENDMENTS. Any surface omitted fails this criterion. |
| C-05 | When focus is active, focus content is woven into existing sections | behavior | essential | If a focus value is provided (compliance, stakeholders, requirements, naming, size, or other), the focus-specific content appears integrated within the relevant existing sections -- not appended as a new standalone section after AMENDMENTS. Fails if focus content is additive-only (appended block). Passes automatically (N/A) if no focus is active. |

---

## Recommended Criteria

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | AMENDMENTS are traceable to RED or YELLOW components | depth | recommended | Every amendment names the specific component it addresses, states the color transition, and includes a score-delta estimate. Amendments not tied to a rated component, or missing the color transition, fail this criterion. |
| C-07 | Focus integration visibly influences the base analysis | depth | recommended | When focus is active, the focus content demonstrably changes the base analysis -- not just accompanies it. Passes automatically (N/A) if no focus is active. |
| C-08 | STRATEGY: BUILD-VS-BUY covers at least half of components | coverage | recommended | At least 50% of the components listed in the ARCHITECT table carry an explicit Build / Buy / Use existing recommendation in the STRATEGY section. |

---

## Aspirational Criteria (C-09 through C-23)

*(C-09 through C-21 unchanged from v6; C-22 and C-23 are new)*

**C-22** | Formula contract gate uses dual-assertion checklist with independent per-location repair instructions | behavior | aspirational

> When C-19 conditions are present (C-15 PASS + C-16 PASS), the Step 0 forward gate takes the form of a dual-assertion checklist with two independently named conditions: (i) the formula variable appears by exact name in at least one Stated Effect cell -- with an explicit repair instruction for failure at this location; and (ii) the formula variable will appear as the left-hand side label of the arithmetic equation in Item C -- with a separate explicit repair instruction for failure at this location. Both conditions must be satisfied before writing any section beyond Step 0. A single-statement C-20-compliant gate that names only the table-side location fails C-22 even if the output ultimately satisfies C-19 for both locations. Passes N/A if C-19 conditions are N/A.

**C-23** | Named-incumbent INFERENCE GATE field includes explicit 3-anchor propagation list with minimum-count declaration | depth | aspirational

> When competitive inertia framing is used (C-21 active scope), the named-incumbent field in INFERENCE GATE includes an explicit anchor propagation list naming all three downstream anchors by location and form, and explicitly states a minimum count (e.g., "At least two of these three anchors are required; all three are recommended"). C-21 passes when the field exists and 2+ anchors appear in output (verifiable only retrospectively); C-23 additionally requires the contract to be declared at the source field, making it checkable at declaration time. A named-incumbent field without this list fails C-23 even when C-21 PASS. Passes N/A if no competitive inertia framing is used.

---

## Scoring

```
Composite = (essential_pass    / 5  * 60)
          + (recommended_pass  / 3  * 30)
          + (aspirational_pass / 15 * 10)
```

PARTIAL counts as 0.5. PARTIAL on any essential fails Golden regardless of composite.

**Golden threshold**: all 5 essential pass (no PARTIALs) AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Golden | all essential (no PARTIAL) + >= 80 | Ship-ready |
| Passing | all essential (PARTIAL allowed) + 60-79 | Usable, gaps noted |
| Failing | any essential fails or PARTIAL | Not useful as a feasibility artifact |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-17 | Initial: C-01 through C-10, aspirational /2 |
| v2 | 2026-03-17 | Added C-11, C-12, C-13; /2 -> /5 |
| v3 | 2026-03-17 | Added C-14, C-15, C-16; /5 -> /8 |
| v4 | 2026-03-17 | Added C-17, C-18; /8 -> /10 |
| v5 | 2026-03-17 | Added C-19; /10 -> /11 |
| v6 | 2026-03-17 | Added C-20, C-21; /11 -> /13 |
| **v7** | **2026-03-17** | **Added C-22 (dual-assertion gate, upgrades C-20), C-23 (explicit 3-anchor list in named-incumbent field, upgrades C-21); /13 -> /15** |
 the specific error. Passes N/A if no focus is active. |
| C-13 | Competitive inertia framing makes the focus lens reshape the feasibility calculation | depth | aspirational | When focus is active and the INERTIA section frames the status quo as a named competing alternative (not generic "not building"), the focus lens demonstrably shifts the competitive calculation: the status quo's do-nothing cost or the feature's inertia-saved value changes because of the focus dimension -- not only because of technical complexity. Example: a compliance focus raises the status quo's do-nothing cost because the current workaround carries an ongoing compliance liability. If the competitive calculation is identical to a no-focus run (same costs, same competitor identity, same VERDICT score), this criterion fails. Passes N/A if no focus is active or if no competitive inertia framing is used. |
| C-14 | AMEND PROTOCOL uses explicit 4-step structure with named unaffected-sections declaration | behavior | aspirational | When AMEND is invoked, the response follows a named 4-step protocol: (1) parse the focus shift or threshold change, (2) identify affected sections, (3) re-weave only affected sections, (4) update VERDICT. Additionally, the protocol must explicitly declare a named list of unaffected sections that will not be rewritten -- e.g., "Unaffected sections: INFERENCE GATE, ARCHITECT, STRATEGY. These will not be rewritten." A response that passes C-10 (correct selective re-weave output) without this explicit protocol structure and unaffected-sections declaration fails C-14. Passes N/A if AMEND is never invoked. |
| C-15 | Focus economics expressed as verifiable arithmetic formula | depth | aspirational | When focus is active and competitive inertia framing is used, the do-nothing cost in INERTIA and AMENDMENTS is expressed as a decomposable arithmetic formula: base_cost (no-focus run value) + focus_adjustment (explicit unit rate by focus type, e.g., "compliance: +$X/yr per open gap; stakeholders: +N weeks per approval cycle") = focus-adjusted total. The formula must be verifiable by inspection -- not a prose statement that focus raises cost. A response that passes C-13 (economics shift exists) via prose but cannot be verified arithmetically fails C-15. Passes N/A if no focus is active or if no competitive inertia framing is used. |
| C-16 | Propagation contract takes tabular form before INFERENCE GATE | depth | aspirational | When focus is active, the pre-section orientation step (the same step that satisfies C-11) expresses the constraint-to-section routing as a table with at least three columns: Constraint, Downstream Section(s), and Stated Effect. A prose-based routing (e.g., "SOC 2 gap surfaces in ARCHITECT and VERDICT") does not satisfy C-16 even if it satisfies C-11. The table must appear before any section heading. Passes N/A if no focus is active. |
| C-17 | Propagation contract table precedes focus-lens interpretation and economics within Step 0 | depth | aspirational | When focus is active and a propagation contract table is present (C-16 PASS), the table appears as the first element within the pre-section orientation step -- before any prose focus-lens interpretation and before the economics formula (C-15). The ordering enforces "name the contract before computing the economics": constraints are declared before their costs are derived, making the causal chain explicit. A C-16-compliant table that appears after lens prose or economics text fails C-17. Passes N/A if no focus is active. |
| C-18 | Propagation contract column headers use rubric-aligned language with back-references for repeated constraint values | depth | aspirational | When focus is active and a propagation contract table is present (C-16 PASS), two conditions must both hold: (1) column headers use vocabulary aligned with the rubric's terminology -- e.g., "Constraint introduced by focus," "Section where it surfaces," "Effect on that section" -- rather than bare generic labels (e.g., "Constraint," "Section," "Effect"); and (2) when the same constraint applies to multiple rows, `[same]` or an equivalent back-reference is used instead of verbatim repetition, reducing redundancy while maintaining traceability. A table that uses generic headers or repeats the constraint phrase verbatim on all rows fails C-18. Passes N/A if no focus is active. |
| C-19 | Propagation contract Stated Effect cells bind to exact formula variable names | depth | aspirational | When focus is active and a propagation contract table is present (C-16 PASS) and a focus economics formula is present (C-15 PASS), at least one Stated Effect cell in the propagation contract table references by exact name the formula variable that the economics section computes -- e.g., a cell reads "increases `focus_adjustment` term in `focus_adjusted_total`" or "contributes to `focus_adjusted_total = base_cost + focus_adjustment`." A Stated Effect cell that describes the effect only in prose ("raises do-nothing cost") without naming the formula variable fails C-19. This creates a closed contract-to-formula loop: the routing table and the arithmetic formula share a token, eliminating the prose-drift gap where effects are described in one vocabulary in the table and a different vocabulary in the formula. Passes N/A if no focus is active, or if C-16 is N/A, or if C-15 is N/A. |
| C-20 | Formula contract check assertion converts C-19 binding into generation-time enforcement | behavior | aspirational | When C-19 conditions are present (C-15 PASS + C-16 PASS), the pre-section orientation step (Step 0) includes an explicit named verification gate stating that the formula variable (`focus_adjusted_total` or the variable defined in Item C) must be confirmed to appear in both the propagation contract table Stated Effect cells and the Item C formula before any section beyond Step 0 is written -- e.g., "Verify this is true before writing Item B: grep `focus_adjusted_total` finds hits in both the table and the formula section." The assertion must appear as a forward-checking gate within Step 0, not as a retrospective note appended after sections are already written. A response that satisfies C-19 (correct lexical binding in the output) but without this explicit generation-time self-check fails C-20. C-19 tests whether the binding exists; C-20 tests whether the output actively required itself to produce that binding. Passes N/A if C-19 conditions are N/A (i.e., C-15 is N/A or C-16 is N/A). |
| C-21 | Named-incumbent field in INFERENCE GATE anchors all downstream competitive references | depth | aspirational | When competitive inertia framing is used (C-13 active scope), the INFERENCE GATE includes a dedicated named-incumbent field that records the specific workaround, tool, or process the team currently uses -- e.g., "Named incumbent: manual CSV export + shared Google Sheet for deduplication." This field then propagates as the referent in at least two of the following three downstream anchors: (1) the INERTIA section heading (renamed to reflect the named incumbent, e.g., "The Named Incumbent the Feature Must Beat"); (2) the INERTIA table's incumbent identification column (replacing a generic "what the team does instead" label with the named entity); (3) the do-nothing cost language in AMENDMENTS (costs framed relative to the named incumbent, not an abstract "workaround"). A competitive-framing response that omits the named-incumbent field in INFERENCE GATE entirely fails C-21. A response where the field exists but propagates to fewer than two of the three downstream anchors also fails C-21. Passes N/A if no competitive inertia framing is used. |
| C-22 | Formula contract gate uses dual-assertion checklist with independent per-location repair instructions | behavior | aspirational | When C-19 conditions are present (C-15 PASS + C-16 PASS), the Step 0 forward gate (from C-20) takes the form of a dual-assertion checklist with two independently named conditions: (i) the formula variable (e.g., `focus_adjusted_total`) appears by exact name in at least one Stated Effect cell in the propagation contract table -- with an explicit repair instruction for failure at this location (e.g., "If not satisfied: revise the Stated Effect rows now before continuing"); and (ii) the formula variable will appear as the left-hand side label of the arithmetic equation in Item C -- with a separate explicit repair instruction for failure at this location (e.g., "If not satisfied: revise Item C now before continuing"). Both conditions must be satisfied before writing any section beyond Step 0. A single-statement gate (C-20 PASS) that names only the table-side location and leaves the formula-side location as an implicit consequence of correct formula design fails C-22, even if the output ultimately satisfies C-19 (both token locations correct). The test is whether the gate structure itself makes each location independently checkable and repairable. Passes N/A if C-19 conditions are N/A (i.e., C-15 is N/A or C-16 is N/A). |
| C-23 | Named-incumbent INFERENCE GATE field includes explicit 3-anchor propagation list with minimum-count declaration | depth | aspirational | When competitive inertia framing is used (C-21 active scope), the named-incumbent field in INFERENCE GATE includes an explicit anchor propagation list that: (1) names all three downstream anchors by location and form -- e.g., "(1) INERTIA section heading: rename to 'INERTIA: STATUS QUO -- The [Named incumbent] the Feature Must Beat'; (2) INERTIA table: first column header reads '[Named incumbent]' not 'What the team does instead'; (3) AMENDMENTS: savings framed as 'recaptured from [Named incumbent]' not 'workaround eliminated'" -- and (2) explicitly states a minimum count (e.g., "At least two of these three anchors are required; all three are recommended"). C-21 passes when the named-incumbent field exists and the downstream anchor count reaches two (verifiable only by scanning downstream sections after the fact); C-23 additionally requires the propagation contract to be declared at the source field, making it checkable at the declaration point rather than only verifiable retrospectively. A named-incumbent field that omits this explicit list fails C-23 even when C-21 PASS (field present, 2+ anchors in output). Passes N/A if no competitive inertia framing is used. |

---

## Scoring

```
Composite = (essential_pass    / 5  * 60)
          + (recommended_pass  / 3  * 30)
          + (aspirational_pass / 15 * 10)
```

PARTIAL scores count as 0.5 for the formula. PARTIAL on any essential criterion fails the Golden threshold regardless of composite score.

**Golden threshold**: all 5 essential criteria pass (no PARTIALs) AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Golden | all essential (no PARTIAL) + >= 80 | Ship-ready; alt version validates the unified hypothesis |
| Passing | all essential (PARTIAL allowed) + 60-79 | Usable, recommended gaps noted |
| Failing | any essential fails or PARTIAL | Not useful as a feasibility artifact |

---

## Evaluation Notes

- **C-05 is the diagnostic criterion for the A/B test**: the entire point of the alt version is that focus is woven in, not appended. Score C-05 strictly -- a new section added after AMENDMENTS is a structural failure even if the content is correct.
- **C-07 and C-05 are complementary**: C-05 checks structure (where focus content lives), C-07 checks effect (whether it changed the analysis). An output can pass C-05 (focus is woven in) but fail C-07 (the base sections are unchanged). The alt version wins the A/B test only if both pass.
- **C-04 partial pattern**: the golden baseline revealed Do-nothing cost in the ARCHITECT table is the most frequently omitted inertia surface. Score each row independently -- one blank cell in a multi-row table is a PARTIAL.
- **C-04 and named-incumbent renaming**: when C-21 is active and the INERTIA section is renamed (e.g., "The Named Incumbent the Feature Must Beat"), this satisfies the section-order requirement for C-04 as an equivalent heading. The renamed heading does not fail C-04.
- **C-09 is a propagation test, not a presence test**: the focus-introduced constraint must appear in at least two downstream sections. Identify the constraint, trace it forward; if it does not recur, score FAIL.
- **C-11 is the propagation anchor**: C-11 operationalizes what C-09 requires but cannot enforce alone. When C-11 passes (explicit routing in pre-section step), C-09 is far more likely to pass. When C-11 is absent, C-09 typically lands at PARTIAL (multi-section presence structurally implied but not explicitly chained). Score C-11 first; use its result to calibrate C-09 strictness.
- **C-12 requires naming, not just correctness**: an output that cleanly weaves focus content with zero meta-commentary fails C-12, even if C-05 passes. The criterion tests failure-mode specificity -- did the output actively name the error it was avoiding? This is a higher bar than structural compliance.
- **C-13 is a calculation test, not a framing test**: scoring C-13 requires identifying whether competitive framing exists (is there a named status quo competitor?) and then asking whether the focus lens changed the *economics* of that competition -- not just the section labels. Compare the do-nothing costs and inertia-saved values to what a no-focus run would produce. If they are the same, the focus lens decorated rather than reshaped.
- **C-14 upgrades C-10**: score C-10 first. A C-10 PASS via selective re-weave without a named protocol or unaffected-sections declaration is C-14 FAIL. The 4-step AMEND PROTOCOL block with explicit "Unaffected sections: [list]" is the only pattern that produced C-10 PASS reliably across tested R2 variations; treat its absence as a structural gap even when the output is correct.
- **C-15 upgrades C-13**: score C-13 first. C-13 PASS via prose (model states the focus raises do-nothing cost plausibly) does not satisfy C-15. C-15 requires arithmetic separability: a reader must be able to verify the delta by subtracting base from focus-adjusted total and matching the unit rate. V-01 R2 C-13 PASS is prose-based (C-15 FAIL); V-03/V-05 R2 C-13 PASS is arithmetic (C-15 PASS). When both C-13 and C-15 are present, V-05's selection preference stands: arithmetic is more reliable in production than prose.
- **C-16 upgrades C-11**: score C-11 first. Prose routing satisfies C-11; only tabular form (table with Constraint / Section / Effect columns appearing before any section heading) satisfies C-16. V-05 R2 prose Step 0 = C-11 PASS, C-16 FAIL. V-02/V-04 R2 tabular routing = C-11 PASS, C-16 PASS. Score C-16 FAIL (not PARTIAL) when prose routing is used -- the distinction is binary.
- **C-17 upgrades C-16**: score C-16 first. A table that satisfies C-16 (correct structure, before any section heading) but appears after lens prose or economics text within Step 0 fails C-17. Table-first ordering is what V-02 R3 demonstrated: the propagation contract is written before the lens is interpreted, anchoring the economics derivation in named constraints rather than the reverse. Score C-17 FAIL (not PARTIAL) when the table follows other Step 0 content.
- **C-18 upgrades C-16**: score C-16 first. Two independent sub-conditions must both hold -- generic headers alone fail even if back-references are used; verbatim row repetition alone fails even if headers are rubric-aligned. V-03 R3 demonstrated that rubric-aligned headers reduce evaluator interpretation ambiguity, and `[same]` back-references maintain traceability without inflating table size. Either sub-condition failing alone scores C-18 FAIL.
- **C-17 and C-18 are independent of each other**: a table can have rubric-aligned headers (C-18 PASS) but appear after lens prose (C-17 FAIL), or appear first (C-17 PASS) but with generic headers (C-18 FAIL). Score each independently after confirming C-16 PASS.
- **C-19 upgrades C-15 and C-18**: score C-15 and C-16 first -- both are prerequisites. C-19 then asks: does the Stated Effect column in the table share a variable token with the formula? V-05 R4 demonstrated this pattern: a table cell such as "increases `focus_adjustment` term in `focus_adjusted_total = base_cost + focus_adjustment`" creates a closed loop -- the exact variable name appears in both the routing contract and the arithmetic section. The test is lexical, not semantic: can you grep the variable name and find it in both locations? Generic prose about "raising cost" in the table does not satisfy C-19 even if the arithmetic formula is correct.
- **C-20 upgrades C-19**: score C-19 first. C-20 asks a different question than C-19: not "is the binding present?" but "did the output require itself to produce the binding before proceeding?" The assertion must appear inside Step 0 as a forward gate -- a sentence or note that explicitly states the variable name must be confirmed in both locations before writing the next section. A response where C-19 passes (correct binding in output) but contains no such forward gate fails C-20. V-03 R5 demonstrated this: the formula contract check converts a wiring property into a model self-check. Score C-20 FAIL (not PARTIAL) when the gate is absent or when it appears after sections are already written.
- **C-21 upgrades C-13**: score C-13 first. C-21 asks whether the competitive entity is named and anchored at the gate rather than improvised during analysis. The INFERENCE GATE field is the anchor: if absent, all downstream competitive references are floating -- the model may use a consistent label, but nothing enforces consistency across invocations. Count propagation anchors explicitly: (1) INERTIA heading rename, (2) INERTIA table column label, (3) AMENDMENTS framing language. Two of three required for PASS; one anchor alone is FAIL. V-04 R5 demonstrated all three propagating from the INFERENCE GATE anchor; the strongest C-13 evidence of any R5 variation came from this structure.
- **C-22 upgrades C-20**: score C-20 first. C-22 asks a structural question about the gate, not a content question: does the gate enumerate two independent, named conditions with per-location repair instructions? A single-statement gate that names the table-side location (C-20 PASS) but leaves the formula-side location implicit fails C-22, even when the output ultimately satisfies C-19 for both locations. The gap C-22 closes: a model that produces a C-20-compliant gate ("verify `focus_adjusted_total` appears in both locations") could satisfy C-20 by reasoning about the table location only and treating correct formula design as a given; C-22's explicit condition (ii) with repair instruction requires the model to treat the formula label as a separately checkable gate condition. V-02 R6 demonstrated this: dual-assertion form with "If not satisfied: revise Item C" makes the formula-side location independently enforceable. Score C-22 FAIL (not PARTIAL) when either condition is absent or when repair instructions are missing from either condition.
- **C-23 upgrades C-21**: score C-21 first. C-23 asks whether the propagation contract is declared at the source or only verifiable after the fact. A named-incumbent field that says "Named incumbent: [entity]" without listing the downstream anchors passes C-21 (if the output reaches 2+ anchors) but fails C-23. The diagnostic: can an evaluator confirm the contract is satisfied by reading only the INFERENCE GATE field, without scanning downstream sections? If yes, C-23 PASS. If not, C-23 FAIL. V-03 R6 demonstrated this: the explicit propagation list with minimum-count declaration made the contract checkable at declaration time, not just verifiable retrospectively. Score C-23 FAIL when the anchor list is absent from the field even if C-21 PASS.
- **N/A handling**: C-05, C-07, C-09, C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-18, C-19, C-20, C-21, C-22, and C-23 all pass as N/A when no focus is active. A degenerate or empty no-focus run fails C-01 regardless. C-13/C-15/C-21/C-22/C-23 additionally pass N/A if no competitive inertia framing is used. C-14 passes N/A if AMEND is never invoked. C-17 and C-18 additionally pass N/A if C-16 is N/A. C-19 additionally passes N/A if C-16 is N/A or C-15 is N/A. C-20 additionally passes N/A if C-19 conditions are N/A (i.e., C-15 is N/A or C-16 is N/A). C-22 additionally passes N/A if C-19 conditions are N/A (same prerequisites as C-20). C-23 additionally passes N/A if no competitive inertia framing is used (same scope as C-21).

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-17 | Initial rubric: C-01 through C-10, 5 essential / 3 recommended / 2 aspirational |
| v2 | 2026-03-17 | Added C-11 (pre-section routing), C-12 (named failure-mode prohibition), C-13 (competitive inertia calculation); aspirational denominator /2 -> /5; extended evaluation notes |
| v3 | 2026-03-17 | Added C-14 (4-step AMEND PROTOCOL with unaffected-sections declaration), C-15 (focus economics arithmetic formula), C-16 (tabular propagation contract); aspirational denominator /5 -> /8; added C-14/C-15/C-16 upgrade notes |
| v4 | 2026-03-17 | Added C-17 (table-first ordering within Step 0), C-18 (rubric-aligned column headers + back-references); aspirational denominator /8 -> /10; added C-17/C-18 upgrade notes and independence note |
| v5 | 2026-03-17 | Added C-19 (Stated Effect cells bind to exact formula variable names, closing contract-to-formula loop); aspirational denominator /10 -> /11; added C-19 upgrade note and extended N/A handling |
| v6 | 2026-03-17 | Added C-20 (formula contract self-check assertion converts C-19 into generation-time enforcement gate), C-21 (named-incumbent field in INFERENCE GATE anchors downstream competitive references); aspirational denominator /11 -> /13; added C-20/C-21 upgrade notes, C-04 named-incumbent heading note, extended N/A handling |
| v7 | 2026-03-17 | Added C-22 (dual-assertion gate with independent per-location repair instructions, upgrades C-20), C-23 (explicit 3-anchor propagation list declared in named-incumbent field, upgrades C-21); aspirational denominator /13 -> /15; added C-22/C-23 upgrade notes and extended N/A handling |
