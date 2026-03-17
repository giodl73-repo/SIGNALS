---
skill: quest-rubric
skill_target: discover-feasibility-alt
date: 2026-03-17
version: 9
---

# Rubric: discover-feasibility-alt

**Skill description**: UNIFIED VERSION (A/B test against discover-feasibility). Single prompt handles base feasibility AND optional focus dimensions woven together, not appended. Produces a richer, more coherent output when focus is active. Test whether unified > parameterized. AMEND: shift focus, adjust confidence thresholds.

**Key diagnostic**: C-05 is the A/B test gate. If focus content is appended rather than woven, the alt version fails its central hypothesis regardless of other scores.

---

## Essential Criteria

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | INFERENCE GATE has all required fields | completeness | essential | Feature, Team, and Timeline are all present and non-empty in the INFERENCE GATE section before any analysis begins. Focus is optional; its absence does not fail C-01. |
| C-02 | VERDICT has score + label consistent with range, prerequisites iff FEASIBLE WITH CAVEATS + RED | correctness | essential | VERDICT contains a numeric score (0-100) and a label (NOT FEASIBLE, FEASIBLE WITH CAVEATS, or FEASIBLE) both present. Label is consistent with score range: <50 = NOT FEASIBLE, 50-74 = FEASIBLE WITH CAVEATS, >=75 = FEASIBLE. Prerequisites listed iff label is FEASIBLE WITH CAVEATS and at least one RED component exists. |
| C-03 | ARCHITECT table has traffic-light ratings with RED Blockers | correctness | essential | Every component row in the ARCHITECT table carries GREEN, YELLOW, or RED. Every RED-rated component has a corresponding RED Blockers entry with all three sub-fields: blocker statement, Lift condition, and Do-nothing cost. "No RED components." is acceptable iff no RED rows exist. |
| C-04 | Inertia surfaces in all four required locations | coverage | essential | All four inertia surfaces present: (1) INERTIA: STATUS QUO section with Baseline sentence, (2) Do-nothing cost column in ARCHITECT table with a value on every row, (3) "Not building this means:" line in VERDICT, (4) "Inertia saved:" line on every amendment in AMENDMENTS. Any surface omitted fails this criterion. |
| C-05 | When focus is active, focus content is woven into existing sections | behavior | essential | If a focus value is provided (compliance, stakeholders, requirements, naming, size, or other), the focus-specific content appears integrated within the relevant existing sections — not appended as a new standalone section after AMENDMENTS. Fails if focus content is additive-only (appended block). Passes automatically (N/A) if no focus is active. |

---

## Recommended Criteria

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | AMENDMENTS are traceable to RED or YELLOW components | depth | recommended | Every amendment names the specific component it addresses, states the color transition, and includes a score-delta estimate. Amendments not tied to a rated component, or missing the color transition, fail this criterion. |
| C-07 | Focus integration visibly influences the base analysis | depth | recommended | When focus is active, the focus content demonstrably changes the base analysis — not just accompanies it. Passes automatically (N/A) if no focus is active. |
| C-08 | STRATEGY: BUILD-VS-BUY covers at least half of components | coverage | recommended | At least 50% of the components listed in the ARCHITECT table carry an explicit Build / Buy / Use existing recommendation in the STRATEGY section. |

---

## Aspirational Criteria

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | Focus constraint propagates to 2+ downstream sections | coverage | aspirational | When focus is active, the focus-introduced constraint must appear in at least two distinct downstream sections (e.g., ARCHITECT, INERTIA, VERDICT, AMENDMENTS). Presence in only one section fails C-09. Passes N/A if no focus is active. |
| C-10 | AMEND selectively re-weaves only affected sections | behavior | aspirational | When AMEND is invoked, the response re-weaves only the sections directly affected by the focus change or threshold shift, leaving unaffected sections unchanged in content. A full rewrite of all sections fails C-10. Passes N/A if AMEND is never invoked. |
| C-11 | Explicit constraint routing in pre-section orientation step | coverage | aspirational | When focus is active, the response includes an explicit pre-section orientation step that identifies which sections the focus constraint will affect and how, before any section is written. A response that weaves focus content correctly (C-09 PASS) without an explicit routing step fails C-11. Passes N/A if no focus is active. |
| C-12 | Named failure-mode prohibition | behavior | aspirational | When focus is active, the pre-section orientation step (C-11) explicitly names the structural failure mode being avoided — e.g., "Do not append a standalone ## COMPLIANCE section after AMENDMENTS." An output that weaves focus content correctly without naming the forbidden pattern fails C-12. The criterion tests failure-mode specificity, not correctness alone. Passes N/A if no focus is active. |
| C-13 | Competitive inertia framing reshapes feasibility calculation | depth | aspirational | When focus is active and the INERTIA section frames the status quo as a named competing alternative (not generic "not building"), the focus lens demonstrably shifts the competitive calculation: the status quo's do-nothing cost or the feature's inertia-saved value changes because of the focus dimension — not only because of technical complexity. If the competitive calculation is identical to a no-focus run, this criterion fails. Passes N/A if no focus is active or if no competitive inertia framing is used. |
| C-14 | AMEND PROTOCOL uses explicit 4-step structure with named unaffected-sections declaration | behavior | aspirational | When AMEND is invoked, the response follows a named 4-step protocol: (1) parse the focus shift or threshold change, (2) identify affected sections, (3) re-weave only affected sections, (4) update VERDICT. Additionally, the protocol must explicitly declare a named list of unaffected sections — e.g., "Unaffected sections: INFERENCE GATE, ARCHITECT, STRATEGY. These will not be rewritten." A response that passes C-10 (correct selective re-weave output) without this explicit protocol structure and unaffected-sections declaration fails C-14. Passes N/A if AMEND is never invoked. |
| C-15 | Focus economics expressed as verifiable arithmetic formula | depth | aspirational | When focus is active and competitive inertia framing is used, the do-nothing cost in INERTIA and AMENDMENTS is expressed as a decomposable arithmetic formula: base_cost (no-focus run value) + focus_adjustment (explicit unit rate by focus type) = focus-adjusted total. The formula must be verifiable by inspection — not a prose statement that focus raises cost. A response that passes C-13 via prose but cannot be verified arithmetically fails C-15. Passes N/A if no focus is active or if no competitive inertia framing is used. |
| C-16 | Propagation contract takes tabular form before INFERENCE GATE | depth | aspirational | When focus is active, the pre-section orientation step expresses the constraint-to-section routing as a table with at least three columns: Constraint, Downstream Section(s), and Stated Effect. A prose-based routing does not satisfy C-16 even if it satisfies C-11. The table must appear before any section heading. Passes N/A if no focus is active. |
| C-17 | Propagation contract table precedes focus-lens interpretation and economics within Step 0 | depth | aspirational | When focus is active and a propagation contract table is present (C-16 PASS), the table appears as the first element within the pre-section orientation step — before any prose focus-lens interpretation and before the economics formula. A C-16-compliant table that appears after lens prose or economics text fails C-17. Passes N/A if no focus is active. |
| C-18 | Propagation contract column headers use rubric-aligned language with back-references for repeated constraint values | depth | aspirational | When focus is active and a propagation contract table is present (C-16 PASS), two conditions must both hold: (1) column headers use vocabulary aligned with the rubric's terminology — e.g., "Constraint introduced by focus," "Section where it surfaces," "Effect on that section"; and (2) when the same constraint applies to multiple rows, `[same]` or an equivalent back-reference is used instead of verbatim repetition. A table that uses generic headers or repeats the constraint phrase verbatim on all rows fails C-18. Passes N/A if no focus is active. |
| C-19 | Propagation contract Stated Effect cells bind to exact formula variable names | depth | aspirational | When focus is active and a propagation contract table is present (C-16 PASS) and a focus economics formula is present (C-15 PASS), at least one Stated Effect cell references by exact name the formula variable computed in the economics section. A Stated Effect cell that describes the effect only in prose without naming the formula variable fails C-19. Passes N/A if no focus is active, or if C-16 is N/A, or if C-15 is N/A. |
| C-20 | Formula contract check assertion converts C-19 binding into generation-time enforcement | behavior | aspirational | When C-19 conditions are present (C-15 PASS + C-16 PASS), the pre-section orientation step (Step 0) includes an explicit named verification gate stating that the formula variable must be confirmed to appear in both the propagation contract table Stated Effect cells and the Item C formula before any section beyond Step 0 is written. The assertion must appear as a forward-checking gate within Step 0, not as a retrospective note. Passes N/A if C-19 conditions are N/A. |
| C-21 | Named-incumbent field in INFERENCE GATE anchors all downstream competitive references | depth | aspirational | When competitive inertia framing is used, the INFERENCE GATE includes a dedicated named-incumbent field that records the specific workaround, tool, or process the team currently uses. This field then propagates as the referent in at least two of three downstream anchors: (1) INERTIA section heading renamed to reflect the named incumbent; (2) INERTIA table incumbent identification column uses the named entity; (3) do-nothing cost language in AMENDMENTS framed relative to the named incumbent. A competitive-framing response that omits the field entirely fails C-21. A response where the field exists but propagates to fewer than two anchors also fails C-21. Passes N/A if no competitive inertia framing is used. |
| C-22 | Formula contract gate uses dual-assertion checklist with independent per-location repair instructions | behavior | aspirational | When C-19 conditions are present, the Step 0 forward gate takes the form of a dual-assertion checklist with two independently named conditions: (i) the formula variable appears by exact name in at least one Stated Effect cell — with an explicit repair instruction for failure at this location; and (ii) the formula variable will appear as the left-hand side label of the arithmetic equation in Item C — with a separate explicit repair instruction for failure at this location. A single-statement gate naming only the table-side location fails C-22. Passes N/A if C-19 conditions are N/A. |
| C-23 | Named-incumbent INFERENCE GATE field includes explicit 3-anchor propagation list with minimum-count declaration | depth | aspirational | When competitive inertia framing is used, the named-incumbent field in INFERENCE GATE includes an explicit anchor propagation list that: (1) names all three downstream anchors by location and form; and (2) explicitly states a minimum count (e.g., "At least two of these three anchors are required; all three are recommended"). C-21 passes when the field exists and the downstream anchor count reaches two (verifiable only by scanning downstream sections); C-23 additionally requires the propagation contract to be declared at the source field, making it checkable at declaration time. Passes N/A if no competitive inertia framing is used. |
| C-24 | Dual-assertion gate uses sequential stop-token structure with Satisfied/Not-satisfied branching | behavior | aspirational | When C-22 conditions are present, the dual-assertion gate takes a sequential stop-token form: CONDITION (i) is presented first with an explicit Satisfied/Not-satisfied status marker; a stop-token explicitly prevents writing CONDITION (ii) until CONDITION (i) is marked Satisfied; CONDITION (ii) then follows the same structure. A dual-assertion checklist (C-22 PASS via inline list form) that presents both conditions simultaneously without stop-token sequencing fails C-24. Passes N/A if C-22 conditions are N/A. |
| C-25 | AMEND PROTOCOL embeds FORMULA CONTRACT RE-CHECK block at step (3)(b) before updated Item B | behavior | aspirational | When AMEND is invoked and C-22 conditions are present, the AMEND PROTOCOL step (3)(b) contains an explicit FORMULA CONTRACT RE-CHECK block that re-verifies both C-22 conditions against the post-amendment state, with per-condition repair instructions, before writing the updated Item B. A prompt that satisfies C-22 at first invocation but lacks this RE-CHECK block in the AMEND PROTOCOL fails C-25. Passes N/A if AMEND is never invoked or if C-22 conditions are N/A. |
| C-26 | Named-incumbent anchor list includes per-anchor Form: label with worked substitution example | depth | aspirational | When competitive inertia framing is used and C-23 is active, each of the three downstream anchors in the named-incumbent propagation list includes both: (1) an explicit Form: label naming the exact output form for that anchor; and (2) a worked substitution example using a representative multi-word incumbent name demonstrating the anchor's rendered form. An anchor list that uses only abstract placeholders without Form: labels and worked examples fails C-26 even when C-23 PASS. Passes N/A if C-23 is N/A. |
| C-27 | Three reliability axes occupy non-overlapping structural positions without cross-interference | behavior | aspirational | When C-24, C-25, and C-26 are all active, each mechanism appears exclusively at its designated structural position and no mechanism's content is duplicated at another axis's position: stop-token gate at Step 0 Item A only; RE-CHECK block at AMEND step (3)(b) only; worked examples at INFERENCE GATE Named incumbent field only. A combined implementation that duplicates gate content across positions fails C-27. Passes N/A if any of C-24, C-25, or C-26 is N/A. |

---

## Scoring

```
Composite = (essential_pass    / 5  * 60)
          + (recommended_pass  / 3  * 30)
          + (aspirational_pass / 19 * 10)
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

- **C-05 is the diagnostic criterion for the A/B test**: the entire point of the alt version is that focus is woven in, not appended. Score C-05 strictly — a new section added after AMENDMENTS is a structural failure even if the content is correct.
- **C-07 and C-05 are complementary**: C-05 checks structure (where focus content lives), C-07 checks effect (whether it changed the analysis). An output can pass C-05 (focus is woven in) but fail C-07 (the base sections are unchanged). The alt version wins the A/B test only if both pass.
- **C-04 partial pattern**: the golden baseline revealed Do-nothing cost in the ARCHITECT table is the most frequently omitted inertia surface. Score each row independently — one blank cell in a multi-row table is a PARTIAL.
- **C-04 and named-incumbent renaming**: when C-21 is active and the INERTIA section is renamed, this satisfies the section-order requirement for C-04 as an equivalent heading.
- **C-09 is a propagation test, not a presence test**: the focus-introduced constraint must appear in at least two downstream sections. Identify the constraint, trace it forward; if it does not recur, score FAIL.
- **C-11 is the propagation anchor**: C-11 operationalizes what C-09 requires but cannot enforce alone. Score C-11 first; use its result to calibrate C-09 strictness.
- **C-12 requires naming, not just correctness**: an output that cleanly weaves focus content with zero meta-commentary fails C-12, even if C-05 passes.
- **C-13 is a calculation test, not a framing test**: compare the do-nothing costs and inertia-saved values to what a no-focus run would produce. If they are the same, the focus lens decorated rather than reshaped.
- **C-14 upgrades C-10**: score C-10 first. A C-10 PASS via selective re-weave without a named protocol or unaffected-sections declaration is C-14 FAIL.
- **C-15 upgrades C-13**: score C-13 first. C-13 PASS via prose does not satisfy C-15. C-15 requires arithmetic separability.
- **C-16 upgrades C-11**: score C-11 first. Prose routing satisfies C-11; only tabular form satisfies C-16. Score C-16 FAIL (not PARTIAL) when prose routing is used.
- **C-17 upgrades C-16**: score C-16 first. Table-first ordering anchors the economics derivation. Score C-17 FAIL (not PARTIAL) when the table follows other Step 0 content.
- **C-18 upgrades C-16**: score C-16 first. Two independent sub-conditions must both hold — generic headers alone fail; verbatim row repetition alone fails.
- **C-17 and C-18 are independent**: a table can have rubric-aligned headers (C-18 PASS) but appear after lens prose (C-17 FAIL), or vice versa. Score each independently after confirming C-16 PASS.
- **C-19 upgrades C-15 and C-18**: score C-15 and C-16 first. C-19 test is lexical: can you grep the variable name and find it in both locations?
- **C-20 upgrades C-19**: C-20 asks "did the output require itself to produce the binding before proceeding?" — not merely whether the binding is present. Score C-20 FAIL (not PARTIAL) when the gate is absent or appears after sections are already written.
- **C-21 upgrades C-13**: count propagation anchors explicitly. Two of three required for PASS; one anchor alone is FAIL.
- **C-22 upgrades C-20**: C-22 asks a structural question — does the gate enumerate two independent, named conditions with per-location repair instructions? Score C-22 FAIL (not PARTIAL) when either condition is absent or when repair instructions are missing from either condition.
- **C-23 upgrades C-21**: the diagnostic — can an evaluator confirm the contract is satisfied by reading only the INFERENCE GATE field, without scanning downstream sections? If yes, C-23 PASS. Score C-23 FAIL when the anchor list is absent from the field even if C-21 PASS.
- **C-24 upgrades C-22**: the test is whether the model is structurally blocked from skipping CONDITION (i), not merely instructed to check both. Score C-24 FAIL (not PARTIAL) when stop-token sequencing is absent.
- **C-25 upgrades C-22 in the amendment-cycle dimension**: C-22 tests Step 0 first-invocation; C-25 tests AMEND step (3)(b) re-invocation. Score C-25 FAIL when the RE-CHECK block is absent from step (3)(b) even if the amendment output happens to satisfy C-22 by luck.
- **C-26 upgrades C-23**: the diagnostic — could an evaluator confirm what the anchor looks like in a real output by reading only the INFERENCE GATE field, without imagining the substitution? Score C-26 FAIL (not PARTIAL) when either the Form: label or the worked example is absent from any anchor.
- **C-27 upgrades C-24+C-25+C-26**: locate each mechanism's content. If any mechanism appears at a second position, score C-27 FAIL.
- **N/A handling**: C-05, C-07, C-09 through C-27 pass as N/A when no focus is active. C-13/C-15/C-21/C-22/C-23/C-24/C-25/C-26 additionally pass N/A if no competitive inertia framing is used. C-14/C-25 pass N/A if AMEND is never invoked. C-17 and C-18 pass N/A if C-16 is N/A. C-19 passes N/A if C-16 is N/A or C-15 is N/A. C-20 passes N/A if C-19 conditions are N/A. C-22/C-24/C-25 pass N/A if C-19 conditions are N/A. C-23/C-26 pass N/A if no competitive inertia framing is used. C-27 passes N/A if any of C-24, C-25, or C-26 is N/A.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-17 | Initial rubric: C-01 through C-10, 5 essential / 3 recommended / 2 aspirational; aspirational denominator /2 |
| v2 | 2026-03-17 | Added C-11 (pre-section routing), C-12 (named failure-mode prohibition), C-13 (competitive inertia calculation); aspirational denominator /2 -> /5 |
| v3 | 2026-03-17 | Added C-14 (4-step AMEND PROTOCOL), C-15 (focus economics arithmetic formula), C-16 (tabular propagation contract); aspirational denominator /5 -> /8 |
| v4 | 2026-03-17 | Added C-17 (table-first ordering within Step 0), C-18 (rubric-aligned column headers + back-references); aspirational denominator /8 -> /10 |
| v5 | 2026-03-17 | Added C-19 (Stated Effect cells bind to exact formula variable names); aspirational denominator /10 -> /11 |
| v6 | 2026-03-17 | Added C-20 (formula contract self-check assertion), C-21 (named-incumbent field anchors downstream refs); aspirational denominator /11 -> /13 |
| v7 | 2026-03-17 | Added C-22 (dual-assertion gate with per-location repair instructions), C-23 (explicit 3-anchor propagation list with minimum-count declaration); aspirational denominator /13 -> /15 |
| v8 | 2026-03-17 | Added C-24 (sequential stop-token gate), C-25 (AMEND PROTOCOL FORMULA CONTRACT RE-CHECK), C-26 (per-anchor Form: labels with worked substitution examples), C-27 (three-axis composability); aspirational denominator /15 -> /19 |
| **v9** | **2026-03-17** | **No new criteria (R8 variations empty). Clean reissue with consolidated evaluation notes and consistent formatting throughout. Production rubric — all 27 criteria confirmed stable at 100.0 in R7.** |
