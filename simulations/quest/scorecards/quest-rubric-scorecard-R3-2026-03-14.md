```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["labeled-gate-headers-unlock-c16: three-gate amend requires distinct subheader labels (Gate 1/Gate 2/Gate 3), not inline prose numbering -- formatting is the gate", "named-banned-qualifier-list-unlocks-c12: explicitly listing banned terms (good/sufficient/appropriate/clear) triggers C-12 OR path and produces PASS; instruction-only approach produces PARTIAL", "c15-mechanism-agnostic: auditor-calibration route, interrogative-question route, and self-application gate route all satisfy C-15 literal pass condition -- any mechanism placing criterion-ID-for-poor-output plus named-rejected-generic in same design rationale section passes"]}
```

---

**R3 result**: V-04 = V-05 (100), V-01 = V-03 (98.75), V-02 (88.75).

Key finding: V-01 and V-03 both reached 98.75 rather than the projected ~97/~98 — the C-15 co-presence requirement is satisfied by auditor calibration and interrogative routes, not only by V-05's self-application gate. The 100 barrier required two specific structural choices: labeled gate headers in amend (C-16) and a named banned-qualifier list (C-12).
 | PASS | PASS | PASS | PASS | PASS |
| C-08 Distinct failure modes | PASS | PARTIAL | PASS | PASS | PASS |
| C-09 Rubric is calibrated | PASS | FAIL | PASS | PASS | PASS |
| C-10 Evolution hook present | PASS | PASS | PASS | PASS | PASS |
| C-11 Inertia framing in design rationale | PASS | FAIL | PASS | PASS | PASS |
| C-12 Pass conditions closed-world gates | PARTIAL | PARTIAL | PARTIAL | PASS | PASS |
| C-13 Rejection log proves filter ran | PASS | PASS | PASS | PASS | PASS |
| C-14 Design rationale precedes tables | PASS | FAIL | PASS | PASS | PASS |
| C-15 Self-application + rejection log co-present | PASS | FAIL | PASS | PASS | PASS |
| C-16 Amend covers three distinct gates | PARTIAL | PARTIAL | PARTIAL | PASS | PASS |

---

## Evidence Notes

### C-01 All 5 fields present
- V-01: Auditor question 1 explicitly checks every row for all five fields.
- V-02: Phase 3 extract-to-table uses five-field format; no explicit audit step.
- V-03: Table format specified; no explicit audit step.
- V-04: Phase 3 Validate question 1 explicitly checks "Every criterion row has all five fields, no field blank?"
- V-05: Template clear; self-application gate checks criteria against their own pass conditions.

### C-02 Weight distribution
- All: Distribution specified in constructor/execute section; V-04 also checks in Phase 3 Validate.

### C-03 Formula + threshold
- All: Findings template includes explicit Composite Score section with 60/30/10 formula and >= 80 / all-essential-pass threshold.

### C-04 Criteria are skill-specific
- V-01: Failure log requires each entry "specific to this skill"; every essential must trace to a failure ID.
- V-02: Every prose sentence must answer "what specific behavior unique to this skill would fail"; Phase 2 skill-specificity filter applied.
- V-03: Interrogative questions force concrete answers; "What makes an output genuinely unusable?" requires skill-specific defects.
- V-04: Every criterion traces to failure log (skill-specific by construction) or spec constraints; failure log itself enforces specificity.
- V-05: Skill-specificity test on every candidate; Step 0 rejection log actively filters generics during construction.

### C-05 Pass conditions binary/testable
- V-01: Constructor bans bare subjective qualifiers without measurable anchors.
- V-02: Phase 2 binary-test filter; rewrite required if not observable.
- V-03: Explicit instruction: no bare subjective qualifiers without count/threshold/presence anchor.
- V-04: Constructor names 8 banned terms explicitly: "good / sufficient / appropriate / thorough / complete / clear / comprehensive / adequate."
- V-05: Names 6 banned terms: "sufficient, appropriate, good, thorough, complete, clear."

### C-06 Ordered by tier
- V-01, V-03, V-04, V-05: Design Rationale, then Essential, Recommended, Aspirational in order with distinct headers.
- V-02: Essential, Recommended, Aspirational in order (each with distinct header/table), then Composite Score, then Design Rationale. The tier sections are in spec order. PASS.

### C-07 Categories from allowed set
- All: Allowed category values (correctness / depth / format / coverage / behavior) explicitly listed with "no other values."

### C-08 Distinct failure modes
- V-01: Failure log produces distinct failures; Auditor question 5 checks for overlap and requires merge/remove.
- V-02 PARTIAL: Prose approach helps specificity but no explicit distinct-failure-modes check or overlap detection mechanism.
- V-03: "What makes an output genuinely unusable?" forces 3-5 distinct defects; mediocre/strong calibration provides implicit overlap check.
- V-04: Failure log produces >= 5 distinct failures; Phase 3 checks "Two essential criteria that catch the same failure? Merge or remove."
- V-05: Skill-specificity test + self-application gate together catch overlap.

### C-09 Rubric is calibrated
- V-01 PASS: Auditor question 4 requires mediocre output + criterion ID AND strong output + criterion ID. Result placed in Design Rationale.
- V-02 FAIL: No calibration step anywhere in the prompt.
- V-03: Question 7 "Describe a mediocre output and a strong output" with explicit criterion ID requirement; goes in design rationale.
- V-04: Phase 2 calibration with specific criterion IDs; placed in design rationale.
- V-05: Self-application gate questions 2 and 3 produce poor-output criterion ID and strong-output criterion ID; placed in design rationale.

### C-10 Evolution hook
- All: Notes section: "Version 1. Grows as /quest:golden discovers excellence patterns."

### C-11 Inertia framing in design rationale
- V-01: Design Rationale "[First sentence: the dominant failure mode for this skill, from the failure log]" appears before criteria tables. PASS.
- V-02 FAIL: Design Rationale contains dominant failure mode but appears AFTER criteria tables in the output template.
- V-03: Question 2 says "State this as one sentence. Write it here, before answering any other question. It will be the first sentence of the design rationale." Design rationale precedes tables. PASS.
- V-04: "First sentence: the dominant failure mode for this skill, from the failure log." Design rationale precedes tables. PASS.
- V-05: "This sentence appears before the first criteria table." PASS.

### C-12 Pass conditions closed-world gates
- V-01 PARTIAL: Instruction bans bare qualifiers but no explicit named banned-terms list or demonstration of the pattern.
- V-02 PARTIAL: Phase 2 filter checks observability but no banned-terms list.
- V-03 PARTIAL: Instruction present; no explicit banned-terms list or demonstration.
- V-04 PASS: Names 8 banned terms explicitly. Triggers the "explicitly lists banned subjective terms" path in C-12 pass condition.
- V-05 PASS: Names 6 banned terms explicitly. Same path as V-04.

### C-13 Rejection log proves filter ran
- V-01: Rejection log (G-01..G-05, >= 3 entries) required and placed verbatim in Design Rationale.
- V-02: Phase 2 produces rejection log; design rationale template includes discarded criteria with reasons.
- V-03: Question 3 produces "Rejected generics" list (>= 3 entries) placed verbatim in Design Rationale.
- V-04: Phase 1 rejection log (>= 3 entries) placed verbatim in Design Rationale.
- V-05: Step 0 rejection log (5 entries) placed verbatim in Design Rationale, plus additional rejected criteria.

### C-14 Design rationale precedes criteria tables
- V-01: Template has "## Design Rationale" before "## Essential Criteria." PASS.
- V-02 FAIL: Template order: Essential Criteria -> Recommended -> Aspirational -> Composite Score -> Design Rationale -> Notes. Design rationale is last.
- V-03: Template has "## Design Rationale" as first section. PASS.
- V-04: "The file must be structured in this exact order" begins with Design Rationale. PASS.
- V-05: "The file must be structured in this exact order" begins with Design Rationale. PASS.

### C-15 Self-application and rejection log co-present in design rationale
- V-01 PASS: (1) Auditor question 4 result -- "criterion ID a mediocre output fails first" -- placed in Design Rationale. (2) Rejection log (G-01..G-05) placed verbatim in Design Rationale. Both co-present. Pass condition met: "at least one essential criterion ID cited as the failure point for a described poor output" is satisfied by auditor calibration.
- V-02 FAIL: (1) No criterion ID for a poor output anywhere. (2) Rejection log present. Only slot 2 populated.
- V-03 PASS: (1) Question 7 mediocre-output calibration with criterion ID placed in Design Rationale. (2) Rejected generics from question 3 placed verbatim in Design Rationale. Both co-present in same section.
- V-04: (1) Phase 2 calibration (criterion ID + poor output) in Design Rationale. (2) Rejection log from Phase 1 in Design Rationale. Both co-present.
- V-05: (1) Self-application results with criterion ID in Design Rationale. (2) Step 0 rejection log (5 entries) in Design Rationale. Both co-present.

### C-16 Amend covers three distinct gates
- V-01 PARTIAL: "(1) Is it specific to this skill? (2) Is the pass condition binary? (3) Does it catch a failure mode not already covered?" All three failure modes present but formatted as inline prose in a single sentence with parenthetical numbering. Not labeled as distinct gate headers.
- V-02 PARTIAL: Three questions present but as flowing paragraph with no numbering or labeled gates.
- V-03 PARTIAL: Three questions present as paragraph. No labeled gate structure.
- V-04 PASS: "**Gate 1 -- Specificity**:" / "**Gate 2 -- Testability**:" / "**Gate 3 -- Distinctness**:" as distinct labeled subheaders. All three failure modes, each as a distinct explicit question.
- V-05 PASS: Same three-gate labeled structure as V-04.

---

## Projection Divergences

Two criteria resolved differently from pre-scoring projections:

**V-01 C-15: projected PARTIAL -> actual PASS.**
The auditor question 4 result ("criterion ID a mediocre output fails first") is explicitly placed in the Design Rationale. The C-15 pass condition requires "at least one essential criterion ID cited as the failure point for a described poor output" -- not a full self-application gate. The auditor calibration satisfies this literally. The projection over-read "self-application" as requiring a formal self-application gate; the pass condition does not require that.

**V-03 C-15: projected PARTIAL -> actual PASS.**
Same logic: question 7 (mediocre/strong calibration with criterion ID) goes in Design Rationale alongside the rejected generics from question 3. Both C-15 slots are co-present in the same section. The interrogative question route satisfies C-15's literal pass condition.

Effect: V-01 and V-03 tie at 98.75 rather than being separated by ~1 point. C-12 (closed-world gates) and C-16 (labeled gate headers) are the only differentiators between the 98.75 group and the 100 group.

---

## Excellence Signals

Patterns from V-04 and V-05 (the 100-scoring variations) that explain their advantage over V-01 and V-03:

**ES-01: Labeled gate headers in amend, not inline prose.**
The difference between PARTIAL and PASS on C-16 is structural. `**Gate 1 -- Specificity**:` / `**Gate 2 -- Testability**:` / `**Gate 3 -- Distinctness**:` as distinct labeled subheaders satisfies "distinct" and "none merged." Inline prose with `(1)... (2)... (3)...` in a single sentence, or three questions as a paragraph, does not. The formatting is the gate -- not the presence of three questions.

**ES-02: Named banned-qualifier list is the path to C-12 PASS.**
Instructions like "no bare subjective qualifiers" produce PARTIAL. Naming the banned terms explicitly ("good / sufficient / appropriate / thorough / complete / clear") triggers C-12's OR path ("the rubric explicitly lists banned subjective terms") and produces PASS. Any variation targeting C-12 must include the named list.

**ES-03: C-15 is mechanism-agnostic; three routes satisfy it.**
The auditor-calibration route (V-01), the interrogative-question route (V-03), and the self-application gate route (V-05) all satisfy C-15's literal pass condition. Any mechanism that places (a) a criterion ID for a poor output AND (b) a named rejected generic into the same design rationale section passes. The self-application gate framing is sufficient but not necessary for C-15.

---

## Top Variation

V-04 and V-05 tied at 100. V-04's mechanism (critic-first failure log + three-phase lifecycle + three-gate amend) and V-05's mechanism (inertia framing + pre-spec rejection log + self-application gate + three-gate amend) both produce complete coverage. V-04 takes a different path to C-15 (Phase 2 calibration route) while V-05 uses the explicit self-application gate. Either can serve as the golden prompt.

V-05 has one structural advantage: the pre-spec Step 0 rejection log provides rejection evidence before reading the spec, meaning the filter is active during construction rather than retrospective. This makes C-13 evidence stronger in spirit even though both score identically against the formal pass condition.
