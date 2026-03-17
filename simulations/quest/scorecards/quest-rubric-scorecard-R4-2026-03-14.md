```json
{"top_score": 77.56, "all_essential_pass": false, "new_patterns": ["output-contract-missing-scoring-section-fails-c03-c09-c10-jointly: rubric construction prompts that omit a mandatory Scoring section from the output contract fail C-03 (formula+threshold), C-09 (calibration), and C-10 (evolution hook) simultaneously -- these three criteria are jointly satisfied or jointly failed based on whether the output contract includes an explicit scoring/notes section; no content-level refinement can compensate for a structural omission in the output contract", "failure-inventory-satisfies-c11-c14-as-equivalent-design-rationale-block: a Failure Analyst phase (Phase 1 enumerating the top N silent failures for the target skill) satisfies C-11 (dominant failure mode stated before criteria) and C-14 (design rationale precedes criteria table) through the failure inventory alone, without requiring a formally-labeled Design Rationale section; the 'or equivalent block describing dominant failure mode' language in C-14 and 'or notes section' language in C-11 accommodate this route", "construction-time-filter-without-output-slot-fails-c13: V-03's Generic Rubric Filter actively deletes generic criteria during Phase 1 (YES result → delete, with named reason) but C-13 scores only PARTIAL because the deletion evidence is not mandated to appear as a named rejection log in the output document; construction-time filter activity is insufficient for C-13; the evidence must be explicitly slotted into the output"]}
```

---

**R4 result**: V-01 (77.56) > V-02 (70.33) > V-03 (60.00). No variation reaches golden threshold.

Key finding: **C-03 fails universally** — all R4 variations stripped out the scoring section that R3 variations carried. This produces a joint failure on C-03 + C-09 + C-10, capping V-01 at 77.56 regardless of its strong criteria quality. V-01's failure-analyst route is the structural winner: it passes C-11 and C-14 via the failure inventory (mechanism-agnostic equivalent block), passes C-08 via distinct labeled failure modes, and passes C-12/C-18 via explicit banned-qualifier list. The path to V-05 (golden) requires adding a scoring section + calibration + evolution hook + rejection log slot + self-application result to V-01's failure-analyst skeleton.
| V-02 | V-03 |
|-----------|------|------|------|
| C-01 All 5 fields present | PASS | PASS | PARTIAL |
| C-02 Weight distribution | PARTIAL | PARTIAL | FAIL |
| C-03 Formula + threshold | FAIL | FAIL | FAIL |
| C-04 Criteria skill-specific | PASS | PASS | PASS |
| C-05 Pass conditions binary | PASS | PASS | PASS |
| C-06 Ordered by tier | PASS | PASS | PASS |
| C-07 Categories from set | PASS | PASS | PASS |
| C-08 Distinct failure modes | PASS | PARTIAL | PARTIAL |
| C-09 Rubric calibrated | FAIL | FAIL | FAIL |
| C-10 Evolution hook present | FAIL | FAIL | FAIL |
| C-11 Inertia framing in DR | PASS | FAIL | PARTIAL |
| C-12 Closed-world gates | PASS | PASS | PASS |
| C-13 Rejection log | FAIL | FAIL | PARTIAL |
| C-14 DR precedes tables | PASS | FAIL | PARTIAL |
| C-15 Self-application + rejection co-present | FAIL | FAIL | FAIL |
| C-16 Amend three gates | N/A | N/A | N/A |
| C-17 Amend gate labels | N/A | N/A | N/A |
| C-18 Banned-qualifier list | PASS | PASS | PASS |
| C-19 Co-presence agnostic | PASS | PASS | PASS |

---

## Evidence Notes

### C-01 All 5 fields present
- V-01: Phase 3 Rubric Assembler explicitly specifies "| ID | Text | Weight | Category | Pass Condition |" as the output table format with weight values and category values enumerated. PASS.
- V-02: Criterion paragraph format block requires "(Weight: essential/recommended/aspirational | Category: correctness/depth/format/coverage/behavior)" plus pass condition. Summary table specifies "| ID | Criterion Name | Weight | Category | Pass Condition (one line) |" — 5 columns. PASS.
- V-03: Phase 2 assigns weight and category per criterion; Phase 3 adds pass condition. No explicit 5-column table template. A model running V-03 might not produce a table with all 5 fields named. PARTIAL.

### C-02 Weight distribution
- V-01: "Total criteria: 7–12. The first 3–5 must be essential." Essential range correct [3,5]; no constraint on recommended [2,3] or aspirational [1,2]. Remaining 2–9 criteria could be any split. PARTIAL.
- V-02: "3–5 essential. Then 2–4 recommended. Then 1–2 aspirational if warranted." Essential [3,5] ✓, Aspirational [1,2] ✓, but recommended upper bound is 4 (spec says 3 max). A rubric produced by V-02 with 4 recommended criteria would fail C-02. PARTIAL.
- V-03: No distribution constraint stated anywhere. FAIL.

### C-03 Formula + threshold
- V-01: Output contract: 1. Failure inventory, 2. Derivation notes, 3. Rubric table. No scoring section. FAIL.
- V-02: "Output: Prose criteria (numbered), then summary table. No other sections." FAIL.
- V-03: No explicit output format. No scoring section referenced. FAIL.

### C-04 Criteria skill-specific
- V-01: Failure Analyst phase requires naming "the top 5 ways this skill can fail silently" with explicit "why it would not be caught by a generic quality check." Every essential criterion traces to a distinct failure ID. PASS.
- V-02: "Every criterion you write must answer... what specific behavior unique to this skill would fail if this criterion were not tested?" Inertia Check: "Would 'the output is well-structured and complete' score equally well? If yes, revise." PASS.
- V-03: Generic Rubric Filter applied per-criterion: "Would 'the output is well-structured, clear, and complete' catch this failure? YES → delete." Active real-time filter throughout Phase 1. PASS.

### C-05 Pass conditions binary/testable
- V-01: "Pass Condition: a binary gate — observable, measurable, no banned qualifiers" + explicit list of 8 banned terms. PASS.
- V-02: "A single binary gate. No banned qualifiers." + explicit list of 8 banned terms including "good / sufficient / appropriate / clear / complete / thorough / comprehensive / adequate." PASS.
- V-03: Phase 3 rules: "Observable", "Measurable: counts, presence/absence, enumerated values", "No banned qualifiers without anchors: good / sufficient / appropriate / clear / complete / thorough / comprehensive / adequate." PASS.

### C-06 Ordered by tier
- V-01: "Start with all essential criteria, then recommended, then aspirational." PASS.
- V-02: "Write 3–5 essential first. Then 2–4 recommended. Then 1–2 aspirational." PASS.
- V-03: Phase 2: "Reorder: essential first, then recommended, then aspirational." PASS.

### C-07 Categories from allowed set
- V-01: "Category values: correctness / depth / format / coverage / behavior" listed explicitly in Phase 3. PASS.
- V-02: Criterion format includes the 5 canonical categories in the template. PASS.
- V-03: Phase 2 lists "correctness / depth / format / coverage / behavior." PASS.

### C-08 Distinct failure modes
- V-01 PASS: Five distinct labeled failures (F-01...F-05) each traced to a unique silent failure mode; each essential criterion derives from a distinct failure ID; structural isolation enforced by the failure log.
- V-02 PARTIAL: Prose-per-criterion approach encourages distinctness and the inertia filter removes generics, but no explicit overlap detection mechanism is present.
- V-03 PARTIAL: Generic Rubric Filter removes generic criteria but does not check overlap between surviving criteria — two distinct-sounding criteria could catch the same underlying failure mode.

### C-09 Rubric calibrated
- All FAIL: No variation includes a calibration step (poor output + criterion ID / strong output + criteria pass count) in the output contract.

### C-10 Evolution hook present
- All FAIL: No variation includes a version field or evolution note in the output template.

### C-11 Inertia framing in design rationale
- V-01 PASS: Output section 1 (failure inventory) enumerates the top 5 silent failures for the skill with explicit "why generics miss it" statements — this is an equivalent block stating the dominant failure modes before the criteria table (section 3). Per C-14's "or equivalent block" language, C-11's "or notes section" accommodates this route.
- V-02 FAIL: The Inertia Check ("Before finalizing, ask: would...") is a prompt instruction, not an output element. Output is: prose criteria then summary table. No pre-criteria design framing in the output document.
- V-03 PARTIAL: "## The Problem This Rubric Must Solve" is prominently framed in the prompt and names the Generic Rubric as the dominant failure mode. However, V-03 has no explicit output format specification — the section appears in the prompt template but is not mandated to appear in the output rubric. Construction-time framing is not the same as output-state co-presence.

### C-12 Pass conditions closed-world gates
- V-01 PASS: 8 banned terms listed explicitly ("good / sufficient / appropriate / clear / complete / thorough / comprehensive / adequate") in Phase 3. Triggers C-12 OR path.
- V-02 PASS: Same 8-term list in construction section. Triggers C-12 OR path.
- V-03 PASS: Same 8-term list in Phase 3 rules. Triggers C-12 OR path.

### C-13 Rejection log proves filter ran
- V-01 FAIL: Three output sections (failure inventory, derivation notes, rubric table). Failure inventory documents why failures are not caught by generics but does not explicitly name and reject a generic criterion by text. No rejection log slot.
- V-02 FAIL: "No other sections" in output contract. Inertia Check tells model to revise, but doesn't produce a rejection log. FAIL.
- V-03 PARTIAL: Phase 1 explicitly produces YES/NO filter results with "→ Keep / Delete" labels per criterion. Deleted criteria are named during Phase 1 with reasons. However, no explicit "Rejection log" section is mandated in the output — the deletion evidence appears in Phase 1 work but is not explicitly required to be preserved as a named section in the final document.

### C-14 Design rationale precedes criteria tables
- V-01 PASS: Output order: 1. Failure inventory (equivalent block, precedes tables), 2. Derivation notes, 3. Rubric table. Failure inventory = "equivalent block describing dominant failure mode" per C-14 pass condition language.
- V-02 FAIL: Output order: prose criteria, then summary table. Criteria appear immediately — no preceding design rationale or equivalent block.
- V-03 PARTIAL: No explicit output ordering specified. "The Problem" section in the prompt framing could correspond to a pre-criteria output section, but the output format is unspecified. PARTIAL — the mechanism is present in the prompt but not guaranteed in the output.

### C-15 Self-application and rejection log co-present
- All FAIL: Slot (1) — a criterion ID cited as the failure point for a described poor output — is absent in all three variations (no calibration step, no self-application gate). Slot (2) — named rejected generic criterion in design rationale — is absent in V-01 and V-02; PARTIAL in V-03 (deletion evidence but no explicit output slot). Both slots must be co-present; none of the variations achieve this.

### C-16, C-17 Amend step
- All N/A: None of the three variations include an amend or revision phase.

### C-18 Banned-qualifier list explicit and enumerated
- V-01 PASS: Phase 3 construction section contains explicit list of 8 terms named individually.
- V-02 PASS: Construction section contains same explicit 8-term list.
- V-03 PASS: Phase 3 rules contain same explicit 8-term list.

### C-19 Co-presence pass conditions mechanism-agnostic
- V-01 PASS: Pass condition instructions — "binary gate, observable, measurable" — specify output state without naming construction route.
- V-02 PASS: Pass condition format specifies state: "If the condition requires counting, state the minimum count. If it requires presence, name the exact item to find." Output-state gates, no mechanism specified.
- V-03 PASS: Phase 3 rules: "Observable: a human with the output in front of them can determine PASS/FAIL in under 30 seconds." Output-state focused, no construction mechanism named.

---

## Composite Scores

| Band | V-01 | V-02 | V-03 |
|------|------|------|------|
| Essential (×60) | 3.5/5 = 42.0 | 3.5/5 = 42.0 | 2.5/5 = 30.0 |
| Recommended (×30) | 3/3 = 30.0 | 2.5/3 = 25.0 | 2.5/3 = 25.0 |
| Aspirational (×10) | 5/9 = 5.56 | 3/9 = 3.33 | 4.5/9 = 5.00 |
| **Total** | **77.56** | **70.33** | **60.00** |
| All essential pass? | NO (C-03 FAIL) | NO (C-03 FAIL) | NO (C-02, C-03 FAIL) |

---

## Projection Divergences

**All three fail C-03 (formula + threshold).** This was not the case in R3 (where all variations included an explicit Findings/Scoring template). R4 variations are stripped-down single-phase construction prompts that focus on criteria quality without scaffolding the output document structure. The formula and threshold cannot be present in the output rubric if the output contract doesn't mandate a scoring section.

**V-01 C-11 and C-14 both PASS via failure inventory.** The failure-analyst route satisfies both criteria through an equivalent block, confirming the mechanism-agnostic reading that C-14's "or equivalent block" language established in R3. This is not a divergence — it validates the prior finding's generalization.

---

## Excellence Signals

**ES-01: Universal C-03 failure exposes the scoring-section gap.**
Every R4 variation omits a mandatory Scoring section from its output contract. This produces simultaneous FAIL on C-03, C-09, and C-10 — three criteria that can only pass if the output contract explicitly slots them. No level of criteria construction quality can compensate for this structural omission. The R4 variations are efficient at producing well-structured criteria (C-04, C-05, C-07 all pass) but produce structurally incomplete rubrics.

**ES-02: Failure-analyst route satisfies C-11 and C-14 without a Design Rationale section.**
V-01's Phase 1 (failure inventory) is an "equivalent block" for both C-11 and C-14 purposes, placing dominant failure modes before the criteria table without requiring a formally-labeled Design Rationale section. V-02 and V-03 fail C-11/C-14 because their inertia framing is embedded in the construction prompt, not mandated as pre-criteria output content. This is a structural advantage unique to the failure-analyst route.

**ES-03: Construction-time filter without output slot fails C-13.**
V-03's Generic Rubric Filter actively deletes generic criteria during Phase 1 — the filtering activity clearly ran. But C-13 is about evidence in the output document, not about whether the filter ran. V-03 passes C-04 (criteria are skill-specific, filter was active) but fails C-13 (rejection log absent from output). The distinction is output-state vs. construction-state: C-13 requires the evidence to be preserved and placed, not merely generated and discarded.

---

## Top Variation

V-01 at 77.56. V-01's failure-analyst route provides the strongest structural coverage: failure inventory satisfies C-11/C-14, distinct failure log satisfies C-08, and explicit banned-qualifier list satisfies C-12/C-18. To reach the golden threshold, V-01 needs: a Scoring section in the output contract (C-03), a calibration example (C-09), an evolution hook (C-10), a named rejection log (C-13), and a self-application result (C-15).
