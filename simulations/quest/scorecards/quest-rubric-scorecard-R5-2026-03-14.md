---

## Round 5 Scorecard — quest-rubric

| Rank | Variation | Essential | Recommended | Aspirational | Score | Golden? |
|------|-----------|-----------|-------------|--------------|-------|---------|
| 1 | V-02 Front-loaded contract | 5/5 | 3/3 | 11/12 | **99.17** | YES |
| 1 | V-05 Canonical path | 5/5 | 3/3 | 11/12 | **99.17** | YES |
| 3 | V-01 Phase 4 audit | 5/5 | 3/3 | 9.5/12 | **97.92** | YES |
| 4 | V-03 Lifecycle emphasis | 5/5 | 2.5/3 | 9/12 | **92.50** | YES |
| 5 | V-04 Inertia framing | 4.5/5 | 3/3 | 9.5/12 | **91.92** | NO |

**The breakthrough**: R4 top was 77.56 with universal C-03 failure (all variations stripped out the Scoring section). R5 adds mandatory Scoring to all but V-04, resolving the joint C-03/C-09/C-10 failure pattern. Four of five variations reach golden.

---

## Criterion Scores

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 All 5 fields | PASS | PASS | PASS | PASS | PASS |
| C-02 Weight distribution | PASS | PASS | PASS | PASS | PASS |
| C-03 Formula + threshold | PASS | PASS | PASS | **PARTIAL** | PASS |
| C-04 Skill-specific | PASS | PASS | PASS | PASS | PASS |
| C-05 Binary+testable | PASS | PASS | PASS | PASS | PASS |
| C-06 Ordered by tier | PASS | PASS | PASS | PASS | PASS |
| C-07 Categories | PASS | PASS | PASS | PASS | PASS |
| C-08 Distinct failure modes | PASS | PASS | **PARTIAL** | PASS | PASS |
| C-09 Calibrated | PASS | PASS | PASS | **PARTIAL** | PASS |
| C-10 Evolution hook | PASS | PASS | PASS | **PARTIAL** | PASS |
| C-11 Inertia framing | PASS | PASS | **FAIL** | PASS | PASS |
| C-12 Closed-world gates | PASS | PASS | PASS | PASS | PASS |
| C-13 Rejection log | **FAIL** | PASS | PASS | PASS | PASS |
| C-14 DR precedes tables | PASS | PASS | **FAIL** | PASS | PASS |
| C-15 Self-application | **FAIL** | PARTIAL | **FAIL** | Partial | **FAIL** |
| C-18 Banned-qualifier list | PASS | PASS | PASS | PASS | PASS |
| C-19 Co-presence agnostic | PASS | PASS | PASS | PASS | PASS |
| C-20 Output contract: Scoring | PASS | PASS | PASS | PASS | PASS |
| C-21 Failure inventory route | PARTIAL | PARTIAL | **FAIL** | Partial | **PASS** |
| C-22 Construction-time filter | **FAIL** | PASS | PASS | Partial | PASS |

---

## Key Evidence

**C-03 — V-04 PARTIAL**: Phase 4 includes the Scoring Section and formula, but the falsifiability check explicitly predicts "Scoring section present/absent varies across V-04 runs" due to dense Generic Rubric test applications at every phase boundary consuming output token budget. Structural inclusion is present; reliability is not.

**C-11/C-14 — V-03 FAIL**: V-03's output order is `1. Rubric Table, 2. Rejection Log, 3. Scoring`. The Phase 1 Failure Analysis is explicitly a construction artifact: *"they do not appear in the final artifact unless you choose to include them."* No pre-criteria DR or equivalent block is guaranteed. The lifecycle emphasis fix (expanded Rejection Phase) correctly resolves C-13/C-22 but the output ordering decision breaks C-11 and C-14.

**C-13 — V-01 FAIL**: Phase 4 Output Contract Architect checklist has three items: Failure Inventory, Rubric Table, Scoring Section. Rejection Log is absent from the checklist; it is absent from the output. The checklist covers exactly what it names.

**C-21 — V-05 PASS only**: Role description explicitly uses the phrase `"or equivalent block"` and names the failure inventory as satisfying the DR requirement: *"this block satisfies the Design Rationale 'or equivalent block' requirement."* V-01 achieves structural equivalence but not label equivalence; C-21 requires the explicit phrase.

**C-22 — V-01 FAIL, V-04 PARTIAL**: V-01 has no rejection log at all. V-04 mandates the Rejection Log in the output but does not include the explicit "construction-time filter activity alone does not satisfy this requirement" disqualification statement.

**C-15 — universal near-miss**: V-02 and V-04 reach PARTIAL (slot 2 — rejected criterion — is in the DR; slot 1 — calibration criterion ID + poor output — is in Scoring, a different section). All others FAIL. The calibration example consistently lands in Scoring, not in the DR phase. C-15 requires co-presence in the same section.

---

## Excellence Signals

**ES-01: Output Contract Architect covers only what its checklist names** — V-01 resolves C-03 by adding Scoring to the Phase 4 checklist but C-13 (Rejection Log) remains FAIL because it was never added to the checklist. A retroactive audit is as comprehensive as its checklist.

**ES-02: Front-loading beats retroactive auditing for section completeness** — V-02's five-section contract (named before any phase instruction) achieves C-13/C-20/C-22 simultaneously. V-01's Phase 4 audit achieves only C-20. Obligations set at t=0 are more complete than obligations added retroactively.

**ES-03: Output ordering is a structural C-11/C-14 determinant** — V-03 demonstrates that the output ordering instruction, not phase framing quality, determines C-11/C-14 compliance. Strong phase framing cannot compensate for an output ordering that places the Rubric Table before any pre-criteria section.

**ES-04: "or equivalent block" phrase in role definition is the C-21 mechanism** — V-05 is the only variation with C-21 PASS because it is the only variation to use the phrase explicitly in the role definition. Structural equivalence (V-01) registers as PARTIAL.

**ES-05: C-15 path identified** — Add a self-application gate (criterion ID + poor output) to the Design Rationale/Failure Inventory phase, co-located with the rejected criterion already present there. Calibration currently lands only in Scoring; C-15 requires both slots in the same section.

---

```json
{"top_score": 99.17, "all_essential_pass": true, "new_patterns": ["c15-calibration-must-be-in-dr-block-not-only-scoring: calibration example (criterion ID + poor output) consistently lands in the Scoring section across all R5 variations; C-15 requires it co-present with the rejected generic criterion in the same Design Rationale section; no variation achieves C-15 PASS because no variation moves the calibration from the Scoring phase to the DR/Failure Inventory phase; path to C-15 PASS: add an explicit self-application gate to the DR phase instruction requiring both a criterion ID + poor output statement and a named rejected criterion in the same block", "output-contract-completeness-gate-confirmed: V-01 retroactive audit achieves only the three sections named in its checklist (Failure Inventory, Rubric Table, Scoring); V-02 front-loaded five-section contract achieves all five simultaneously; confirms the v5 output-contract-completeness-gate v6 candidate with a specific failure mode: a retroactive checklist that omits a required section (Rejection Log) produces a rubric that omits that section; front-loading is structurally more complete than retroactive auditing for section compliance", "role-identity-explicit-equivalence-language-is-the-mechanism-for-c21: V-05 is the only R5 variation to achieve C-21 PASS by using the phrase 'or equivalent block' explicitly in the role definition; V-01 achieves the same structural outcome (failure inventory before criteria) but without the phrase, registering PARTIAL; criteria requiring explicit naming of a non-canonical route are satisfied by including the exact phrase in the role definition, not by structural demonstration alone"]}
```
ct: "they do not appear in the final artifact unless you choose to include them as a pre-table notes section." Inclusion is optional, not mandated; Rubric Table appears first. No pre-criteria equivalent block guaranteed in output. FAIL.
- V-04: Output section 1 is Design Rationale, which requires naming the dominant failure mode. DR precedes Rubric Table. PASS.
- V-05: Section 1 is Failure Inventory, labeled "this section serves as the Design Rationale equivalent block... satisfies the requirement that the dominant failure mode be named before criteria are constructed." Phase 1 requires at least one entry marked *(dominant)*. PASS.

### C-12 Closed-world gates
All 5 variations: explicit 8-term banned-qualifier list triggers the C-12 OR path. PASS across the board.

### C-13 Rejection log proves filter ran
- V-01: Phase 4 checklist items: Failure Inventory, Rubric Table, Scoring Section. Rejection Log absent from checklist and absent from output order. The failure inventory documents failure modes, not rejected criteria. FAIL.
- V-02: Phase 4 Rejection Log is a named output phase: "This is a named output section. Recording deletions only in your reasoning does not satisfy this requirement — the log must appear in the artifact." Required Output Sections names Rejection Log as section 3. PASS.
- V-03: Phase 3 Rejection Log: "The Rejection Log is a named section in your output document... Construction-time filter activity alone does not satisfy this requirement." Minimum 2 entries, STOP CONDITION enforced. Output order item 2. PASS.
- V-04: Phase 3 Step A Rejection Log is mandated in the output (output item 2). STOP CONDITION requires >= 1 entry with named rejected criterion. PASS.
- V-05: Phase 3: "This is Section 2 of the four-section canonical output. It must appear as a named section in the artifact... Construction-time filter activity alone does not satisfy this section." Minimum 1 entry. PASS.

### C-14 Design rationale precedes criteria tables
- V-01: Output order: 1. Failure Inventory (DR equivalent block), 2. Derivation Notes, 3. Rubric Table. Failure Inventory precedes Rubric Table. PASS.
- V-02: Output order: Design Rationale -> Failure Inventory -> Rejection Log -> Rubric Table -> Scoring. DR is first. PASS.
- V-03: Output order: 1. Rubric Table, 2. Rejection Log, 3. Scoring Section. Rubric Table is first; no DR or equivalent block precedes it. FAIL.
- V-04: Output order: 1. Design Rationale, 2. Rejection Log, 3. Rubric Table, 4. Scoring. DR first. PASS.
- V-05: Output order: Section 1 Failure Inventory (DR equivalent block), Section 2 Rejection Log, Section 3 Rubric Table, Section 4 Scoring. Failure Inventory precedes Rubric Table. PASS.

### C-15 Self-application and rejection log co-present
- V-01: Calibration example (criterion ID + poor output) is in Scoring Section (section 4). Failure Inventory (section 1) contains failure modes, not rejected criteria. Both slots absent from the DR equivalent block. FAIL.
- V-02: Design Rationale (Phase 1) requires "at least one criterion that was considered and rejected" — slot (2) present in DR. Calibration example (slot 1) is in Phase 5 Scoring, not in DR. Not co-present. PARTIAL.
- V-03: No DR section in output. Calibration in Scoring; rejected criteria in Rejection Log. Items distributed across output, no co-presence in a single DR section. FAIL.
- V-04: Design Rationale (Phase 3 Step B) requires "at least one criterion from the Rejection Log by text and explains the rejection" — slot (2) in DR. Calibration example (slot 1) is in Phase 4 Scoring Section, separate from DR. Not co-present. PARTIAL.
- V-05: Failure Inventory (Section 1, DR equivalent block) contains failure modes but not a criterion ID + poor output (slot 1). Rejected criteria (slot 2) are in Rejection Log (Section 2), separate from Section 1. Calibration (slot 1) is in Section 4 Scoring. Both slots distributed across three sections, not co-present in DR equivalent block. FAIL.

### C-16, C-17 Amend step
All N/A: no R5 variation includes an amend or revision phase.

### C-18 Banned-qualifier list explicit and enumerated
All 5 variations: construction section contains explicit list of 8 banned terms individually named. PASS across the board.

### C-19 Co-presence pass conditions mechanism-agnostic
All 5 variations: output-state checks (presence/absence, counts, named sections) without mandating construction route. PASS across the board.

### C-20 Output contract explicitly names Scoring section
- V-01: Phase 4 Output Contract Architect checklist explicitly includes Scoring Section as a required element with joint-failure warning: "Omitting the Scoring section is a structural gap that causes C-03, C-09, and C-10 to fail simultaneously." PASS.
- V-02: Required Output Sections front-matter names "5. Scoring" as required section with explicit joint-failure warning. PASS.
- V-03: Output instruction names Scoring Section as item 3 in the emit order. PASS.
- V-04: Phase 4 STOP CONDITION includes "Scoring section present." PASS.
- V-05: Phase 4 labels Scoring Section as "*required; omitting this section causes C-03, C-09, and C-10 to fail simultaneously*." PASS.

### C-21 Failure inventory route named as equivalent block
- V-01: Phase 4 output contract names "Failure Inventory" as the required pre-table output, structurally treating it as DR equivalent. However, the phrase "or equivalent block" is absent; the prompt does not explicitly state the failure-inventory route as an acceptable substitute in pass-condition terms. PARTIAL.
- V-02: Has both Design Rationale and Failure Inventory as separate named sections. Does not use "or equivalent block" language or name the failure-inventory route as equivalent to DR. PARTIAL.
- V-03: No pre-criteria DR section or equivalent block in output; prompt makes no acknowledgment of failure-inventory equivalence. FAIL.
- V-04: Uses Design Rationale section explicitly; does not name failure-inventory route as an acceptable DR substitute. PARTIAL.
- V-05: Role description explicitly states: "the failure inventory is explicitly named as satisfying the Design Rationale 'or equivalent block' requirement." Phase 1 says "this section serves as the Design Rationale equivalent block" and "this block satisfies the Design Rationale 'or equivalent block' requirement." The phrase "or equivalent block" appears explicitly in the role definition. PASS.

### C-22 Construction-time filter named insufficient
- V-01: No rejection log in output contract. No "construction-time filter insufficient" statement anywhere. FAIL.
- V-02: Required Output Sections for Rejection Log states: "construction-time filtering alone does not satisfy this requirement — the log must appear as a named section in your output document." Explicit disqualification. PASS.
- V-03: Phase 3 states: "Construction-time filter activity alone does not satisfy this requirement. A rubric that ran the filter during Phase 2 but produces no Rejection Log section in the output fails C-13 regardless of the quality of the filtering activity." PASS.
- V-04: Phase 3 Step A mandates the Rejection Log as output item 2 and enforces STOP CONDITION, but the explicit "construction-time filter activity alone is insufficient" disqualification is absent. Rejection Log is required but the disqualification rationale is not stated. PARTIAL.
- V-05: Phase 3: "Construction-time filter activity alone does not satisfy this section. A rubric that applied the inline specificity filter during Phase 2 but produces no named Rejection Log section in the output fails C-13 regardless of how actively the filter ran." Global Constraints reinforce: "not implied by construction activity." PASS.

---

## Composite Scores

| Band | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| Essential (x60) | 5/5 = **60.0** | 5/5 = **60.0** | 5/5 = **60.0** | 4.5/5 = **54.0** | 5/5 = **60.0** |
| Recommended (x30) | 3/3 = **30.0** | 3/3 = **30.0** | 2.5/3 = **25.0** | 3/3 = **30.0** | 3/3 = **30.0** |
| Aspirational (x10) | 9.5/12 = **7.92** | 11/12 = **9.17** | 9/12 = **7.50** | 9.5/12 = **7.92** | 11/12 = **9.17** |
| **Total** | **97.92** | **99.17** | **92.50** | **91.92** | **99.17** |
| All essential pass? | YES | YES | YES | NO (C-03 PARTIAL) | YES |
| Golden? | YES | YES | YES | NO | YES |

PARTIAL on an essential criterion counts as 0.5 pass for score computation but does not satisfy the all-essential-pass precondition.

---

## Projection Divergences

**V-01 C-13 remains FAIL after Phase 4 audit addition.** The falsifiability check predicted C-13 FAIL for V-01; confirmed. The Phase 4 checklist covers three items (Failure Inventory, Rubric Table, Scoring Section) but not the Rejection Log. An Output Contract Architect covers exactly what its checklist names.

**V-02 and V-05 tie at 99.17 via different mechanisms.** V-02 achieves C-13/C-22 via front-loaded section contract; V-05 achieves C-21/C-22 via explicit role-definition language. V-02 scores C-15 PARTIAL; V-05 scores C-21 PASS. Net aspirational sum equal (11/12 each), total tied.

**V-03 achieves C-13/C-22 but loses C-11/C-14 due to output ordering.** The lifecycle emphasis fix resolves C-13 and C-22 as predicted. The C-11/C-14 regression was not predicted by the falsifiability check but is directly caused by V-03's output ordering instruction (Rubric Table first). Phase framing quality cannot compensate for a missing pre-criteria output section.

**V-04 cannot reliably produce the Scoring section.** Dense inertia-check prose competes with the Scoring Section for output token budget. C-03 PARTIAL; without all-essential-pass, golden threshold not reached regardless of composite score (91.92).

---

## Excellence Signals

**ES-01: Output Contract Architect covers only what its checklist names.**
V-01 resolves R4/universal C-03 failure by adding Scoring Section to the Phase 4 checklist. But C-13 (rejection log) remains FAIL because the checklist has three items, not four. A retroactive audit is as comprehensive as its checklist — it covers exactly what it names and nothing else. The structural implication: an output contract checklist must enumerate all required sections to be a complete gate.

**ES-02: Front-loaded output contract achieves C-13/C-20/C-22 jointly where retroactive audit covers only one.**
V-02's five-section contract (named before any phase instruction) produces C-13 PASS, C-20 PASS, and C-22 PASS simultaneously. V-01's Phase 4 audit produces C-20 PASS but fails C-13 and C-22 because they weren't in the checklist. Front-loading creates structural obligations at t=0 that persist through all subsequent phases; retroactive auditing catches only what was explicitly planned for.

**ES-03: Output ordering is a structural C-11/C-14 determinant that cannot be patched by phase framing.**
V-03 demonstrates that the output ordering instruction — not the phase framing quality — determines C-11/C-14 compliance. V-03 has strong phase framing (6 failures, inline filter, explicit rejection log enforcement) but fails C-11 and C-14 because the output instruction places Rubric Table first. C-11 and C-14 are output-state gates; only the output order specification satisfies them.

**ES-04: Explicit label-equivalence language in role definition achieves C-21; structural equivalence alone does not.**
V-05 is the only variation to achieve C-21 PASS. The mechanism: the role description explicitly uses "or equivalent block" language and names the failure inventory as satisfying the DR requirement. V-01 achieves the same structural outcome (failure inventory before criteria table) but without the phrase. C-21 requires explicit naming of the equivalence path; implicit structural equivalence registers as PARTIAL.

**ES-05: C-15 is the last unachieved criterion — path identified.**
No R5 variation achieves C-15 PASS. Calibration example (criterion ID + poor output, slot 1) consistently lands in the Scoring section; rejected generic criterion (slot 2) lands in DR or Rejection Log. They are never co-present. The path to C-15 PASS: add a self-application gate to the Design Rationale phase itself — name one criterion ID and describe a poor output that fails it in the DR block, alongside the rejected criterion already required there.

---

## Top Variation

V-02 and V-05 tied at 99.17.

**V-02 strength profile**: Front-loaded contract achieves section completeness most reliably — no retroactive audit required. Weakness: C-21 PARTIAL (no "or equivalent block" language), C-15 PARTIAL (calibration not in DR).

**V-05 strength profile**: Canonical path formalization achieves C-20/C-21/C-22 simultaneously as predicted. Weakness: C-15 FAIL (calibration/rejection not co-present in DR equivalent block).

**Path to 100**: Add a self-application gate (criterion ID + poor output description) to the Design Rationale or Failure Inventory phase instruction in both V-02 and V-05. This co-locates slot 1 with slot 2 in the DR section, resolving C-15. All other criteria already pass in both.

---

## New Patterns (v6 Candidates)

**P-01: c15-calibration-must-be-in-dr-block-not-only-scoring** — No R5 variation achieves C-15 PASS because the calibration example (criterion ID + poor output) is consistently placed in the Scoring section while the rejected criterion is in the DR or Rejection Log. C-15 requires co-presence in the same DR section. The path: a Design Rationale phase instruction that explicitly requires both (1) a self-application statement naming a criterion ID and a poor output that fails it, AND (2) at least one rejected generic criterion by text, in the same section. This is not a new criterion — C-15's existing pass condition already captures it — but V-06 variation designs must move calibration from Scoring to the DR/Failure Inventory phase.

**P-02: output-contract-completeness-gate-confirmed-with-failure-mode** — V-01's retroactive Output Contract Architect audit achieves only the three sections in its checklist; Rejection Log is absent from the checklist and absent from the output. V-02's front-loaded five-section contract achieves all five simultaneously. This confirms the v5 output-contract-completeness-gate v6 candidate and adds a specific failure mode: a retroactive audit checklist that is incomplete produces a rubric that is incomplete in exactly the sections omitted from the checklist. A criterion: "the output contract (whether front-loaded or retroactive checklist) names Failure Inventory/DR, Rejection Log, Rubric Table, and Scoring as required sections; any section absent from the contract is absent from the output."

**P-03: role-identity-framing-is-the-mechanism-for-explicit-equivalence-language** — V-05's RubricArchitect role definition is the only R5 mechanism that achieves C-21 PASS by explicitly using "or equivalent block" language. V-01 achieves structural equivalence (failure inventory before criteria) but not label equivalence. The lesson: criteria that require explicit naming of a non-canonical route (C-21, and potentially C-22's disqualification statement) are best satisfied by including the exact phrase in the role definition or role description, not in a phase instruction alone. A candidate criterion: "the prompt's role definition explicitly names at least one non-canonical construction route as an acceptable substitute for a formally-labeled required section, using 'or equivalent block' or equivalent language."
