Now I have everything needed. Let me score all five variations.

---

# scout-size R8 — Quest Score

**Rubric**: v8 (27 criteria) | **Scoring model**: essential 5/5 × 60 + recommended 3/3 × 30 + aspirational N/19 × 10

---

## Per-Variation Evaluation

### V-01 — Structural AMEND directive only (C-26)

Base: R7 V-03 (passes C-01–C-25) + STRUCTURAL AMEND RE-EVALUATION DIRECTIVE in SYNTHESIS. OPEN UNKNOWNS retains inline "A generic placeholder like 'dependencies may exist' fails"; SYNTHESIS retains `> **Anti-pattern**:` blockquote.

| ID | Result | Evidence |
|----|--------|----------|
| **C-01** | PASS | Tier field: `[LOW / MEDIUM / HIGH / XL]` — enforced vocabulary |
| **C-02** | PASS | Timeline field: sprint range "N–M sprints" with failing calendar example |
| **C-03** | PASS | SURFACE AREA table with `**Total**` row required |
| **C-04** | PASS | INERTIA CHECK: Workaround / Maintenance cost / Cost direction fields present |
| **C-05** | PASS | CONFIDENCE: level + Basis with "what IS known" |
| **C-06** | PASS | "specialist disciplines + FTE fractions + implementation ownership per role"; failing "2 engineers" example |
| **C-07** | PASS | "Primary driver: [one or two factors most responsible]" in COMPLEXITY section |
| **C-08** | PASS (default) | No AMEND invoked in template — STRUCTURAL AMEND RE-EVALUATION DIRECTIVE provides re-evaluation behavior but C-08 defaults pass |
| **C-09** | PASS | PRE-FLIGHT GATE "Out-of-scope boundary:" field with "TBD or blank fails" |
| **C-10** | PASS | PRE-FLIGHT GATE "Break-even signal:" field with "Cannot assess — [reason]" fallback |
| **C-11** | PASS | Team signal template: "(owns event schema + storage layer)" example enforces ownership |
| **C-12** | PASS | OPEN UNKNOWNS: Unknown/Impact/Movement typed fields; generic placeholder explicitly fails |
| **C-13** | PASS | SYNTHESIS: "combine at least two signal dimensions...to produce a decision-relevant recommendation" |
| **C-14** | PASS | OPEN UNKNOWNS is separate section with typed fields; CONFIDENCE carries "Do not list unknowns here" |
| **C-15** | PASS | Preliminary hypothesis in PRE-FLIGHT GATE; SYNTHESIS: "State whether the analysis confirms, revises, or partially revises the commitment made in PRE-FLIGHT GATE" |
| **C-16** | PASS (default) | No AMEND invoked in template run |
| **C-17** | PASS | SYNTHESIS: `> **Anti-pattern**: Restating sections...is juxtaposition`; OPEN UNKNOWNS: "A generic placeholder like 'dependencies may exist' fails" |
| **C-18** | PASS | PRE-FLIGHT GATE before all analysis sections; contains scope / break-even / hypothesis; STOP instruction present |
| **C-19** | PASS | CONFIDENCE: "Do not list unknowns here"; SURFACE AREA, COMPLEXITY, INERTIA CHECK all carry scope prohibition rules |
| **C-20** | PASS | Full mesh: INERTIA CHECK, SURFACE AREA, COMPLEXITY, SYNTHESIS each prohibit scope content; COMPLEXITY, CONFIDENCE, SYNTHESIS, OPEN UNKNOWNS prohibit unknowns content |
| **C-21** | PASS | Preliminary hypothesis is a field INSIDE PRE-FLIGHT GATE; SYNTHESIS names "PRE-FLIGHT GATE" and confirms/revises it |
| **C-22** | PASS | Anchor: "look back at PRE-FLIGHT GATE — it committed a preliminary hypothesis"; Verdict close: "committed in PRE-FLIGHT GATE" required phrase in verdict template |
| **C-23** | PASS | Guards say "scope was resolved in PRE-FLIGHT GATE, not in analysis steps" — names the canonical home, not bare exclusion |
| **C-24** | PASS | Commitment chain block with labeled lines: `Gate commitment:` / `Analysis:` / `Verdict:` — "A prose paragraph that folds the same information into a single sentence fails C-24" |
| **C-25** | PASS | PRE-FLIGHT GATE: "This gate's commitments are enforced downstream: — Scope exclusions: held in INERTIA CHECK, SURFACE AREA, COMPLEXITY TIER AND DRIVER, and SYNTHESIS — Hypothesis: confirmed or revised in SYNTHESIS" |
| **C-26** | PASS | STRUCTURAL AMEND RE-EVALUATION DIRECTIVE: "applies on every invocation, independent of whether an AMEND directive is present...This requirement is a structural property of this section's template, not a conditional check. Leaving this conclusion unchanged...is a structural failure of this section's integrity" — unconditional scope + structural framing, both C-26 disqualifiers absent |
| **C-27** | **FAIL** | SYNTHESIS: `> **Anti-pattern**: Restating sections...` — embedded in instruction prose, not a dedicated `> **FAILURE MODE FOR THIS SECTION**:` block. OPEN UNKNOWNS: "A generic placeholder like 'dependencies may exist' fails" — inline trailing requirement sentence, not a standalone labeled block |

**V-01: Essential 5/5 | Recommended 3/3 | Aspirational 18/19**
`Composite = 60 + 30 + (18/19 × 10) = 60 + 30 + 9.47 = **99.47**`

---

### V-02 — Dedicated FAILURE MODE blocks only (C-27)

Base: R7 V-03 + dedicated `> **FAILURE MODE FOR THIS SECTION**:` blockquotes in OPEN UNKNOWNS and SYNTHESIS. No STRUCTURAL AMEND RE-EVALUATION DIRECTIVE.

| ID | Result | Evidence |
|----|--------|----------|
| **C-01–C-25** | PASS (all) | Same base structure as V-01; PRE-FLIGHT GATE forward references, bilateral closure mesh, commitment chain trace all present |
| **C-26** | **FAIL** | SYNTHESIS ends after cross-signal directional observation — no AMEND directive of any form present. C-26 requires a written structural directive; absence = fail |
| **C-27** | PASS | OPEN UNKNOWNS: `> **FAILURE MODE FOR THIS SECTION**: "Dependencies may exist" is a placeholder, not an unknown...` — dedicated labeled blockquote, structurally separate from field requirements. SYNTHESIS: `> **FAILURE MODE FOR THIS SECTION**: Restating sections in sequence...is juxtaposition...` — dedicated labeled blockquote. Both sections carry standalone blocks whose absence would be a visible structural gap |

**V-02: Essential 5/5 | Recommended 3/3 | Aspirational 18/19**
`Composite = 60 + 30 + (18/19 × 10) = 60 + 30 + 9.47 = **99.47**`

---

### V-03 — Minimal combination: C-26 + C-27 (no self-check)

Base: R7 V-03 + STRUCTURAL AMEND RE-EVALUATION DIRECTIVE in SYNTHESIS + dedicated `> **FAILURE MODE FOR THIS SECTION**:` blocks in OPEN UNKNOWNS and SYNTHESIS.

| ID | Result | Evidence |
|----|--------|----------|
| **C-01–C-25** | PASS (all) | PRE-FLIGHT GATE with forward references; bilateral closure mesh; commitment chain with labeled lines; navigational guards naming canonical home; preliminary hypothesis inside gate |
| **C-26** | PASS | SYNTHESIS: `**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: This synthesis section carries a written re-evaluation requirement that applies on every invocation, independent of whether an AMEND directive is present...a structural property of this section's template, not a conditional check...a structural failure of this section's integrity` — both required discriminators present, both disqualifying forms absent |
| **C-27** | PASS | OPEN UNKNOWNS: dedicated `> **FAILURE MODE FOR THIS SECTION**:` blockquote before field requirements. SYNTHESIS: dedicated `> **FAILURE MODE FOR THIS SECTION**:` blockquote before commitment chain. Both sections covered; standalone labeled blocks, not inline prose |

**V-03: Essential 5/5 | Recommended 3/3 | Aspirational 19/19**
`Composite = 60 + 30 + (19/19 × 10) = 60 + 30 + 10 = **100**`

---

### V-04 — All R8 mechanisms + 27-criterion self-check

Base: R7 V-04 step-labeled structure + STRUCTURAL AMEND RE-EVALUATION DIRECTIVE (replaces conditional AMEND INSTRUCTION) + FAILURE MODE blocks retained + self-check extended to 27 criteria with definition-level C-26/C-27 items.

| ID | Result | Evidence |
|----|--------|----------|
| **C-01–C-25** | PASS (all) | Step-labeled structure (STEP 1–7 + PRE-FLIGHT GATE), WRONG/CORRECT examples, failing forms table, bilateral closure mesh, forward-reference enforcement contract, structured commitment chain, navigational guards naming canonical homes |
| **C-26** | PASS | STEP 7 SYNTHESIS: `**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**:` — identical text to V-03: unconditional scope ("every invocation, independent of whether an AMEND directive is present"), structural framing ("structural property of this section's template"), structural failure language ("structural failure of this section's integrity"). Self-check C-26 item adds definition: "a directive ending 'it fails C-16' fails C-26 even if present in synthesis" |
| **C-27** | PASS | STEP 6: `> **FAILURE MODE FOR THIS SECTION**:` dedicated block. STEP 7: `> **FAILURE MODE FOR THIS SECTION**:` dedicated block. Self-check C-27 item distinguishes inline anti-pattern from dedicated block: "an inline anti-pattern sentence embedded in a prose blockquote fails C-27" |

**V-04: Essential 5/5 | Recommended 3/3 | Aspirational 19/19**
`Composite = 60 + 30 + (19/19 × 10) = 60 + 30 + 10 = **100**`

---

### V-05 — Full integration + structural disqualifying forms for C-26/C-27

Base: R7 V-05 structure + all R8 V-04 mechanisms + C-26/C-27 self-check items extended with exact structural disqualifying conditions.

| ID | Result | Evidence |
|----|--------|----------|
| **C-01–C-25** | PASS (all) | Identical structural mechanisms to V-04; enforcement contract in PRE-FLIGHT GATE names STEP 1/2/3/7 for scope and STEP 7 for hypothesis |
| **C-26** | PASS | STEP 7: identical STRUCTURAL AMEND RE-EVALUATION DIRECTIVE. Self-check C-26 item names both disqualifying forms: "'in this invocation' makes it conditional" + "'it fails C-16' makes it criterion-referenced rather than a structural property" — both must be absent for PASS |
| **C-27** | PASS | STEP 6 and STEP 7 both carry `> **FAILURE MODE FOR THIS SECTION**:` dedicated blocks. Self-check C-27 item names both disqualifying forms: (1) `> **Anti-pattern**: Restating sections in sequence is juxtaposition` in SYNTHESIS "is a structural annotation embedded in the section's instruction prose, not a dedicated block"; (2) `A generic placeholder fails` as a trailing sentence in OPEN UNKNOWNS "is embedded in the requirements prose, not a standalone labeled block" |

**V-05: Essential 5/5 | Recommended 3/3 | Aspirational 19/19**
`Composite = 60 + 30 + (19/19 × 10) = 60 + 30 + 10 = **100**`

---

## Composite Score Summary

| Variation | Essential (×60) | Recommended (×30) | Aspirational (/19 ×10) | Composite | Band |
|-----------|----------------|-------------------|------------------------|-----------|------|
| **V-01** | 5/5 → 60 | 3/3 → 30 | 18/19 → 9.47 | **99.47** | Gold |
| **V-02** | 5/5 → 60 | 3/3 → 30 | 18/19 → 9.47 | **99.47** | Gold |
| **V-03** | 5/5 → 60 | 3/3 → 30 | 19/19 → 10.00 | **100.00** | Gold |
| **V-04** | 5/5 → 60 | 3/3 → 30 | 19/19 → 10.00 | **100.00** | Gold |
| **V-05** | 5/5 → 60 | 3/3 → 30 | 19/19 → 10.00 | **100.00** | Gold |

**Ranking**: V-03 = V-04 = V-05 (100) > V-01 = V-02 (99.47)

All five variations are Gold-band. All five pass all essential criteria.

---

## Excellence Signals

**Top-scoring variations**: V-03, V-04, V-05 (first round achieving 19/19 on v8 rubric)

### Signal 1 — Unconditional scope + structural framing are the two discriminating properties of C-26

The R7 conditional AMEND INSTRUCTION ("If an AMEND directive is present in this invocation...it fails C-16") fails C-26 on two counts simultaneously: "in this invocation" scopes the directive to AMEND-present runs only; "it fails C-16" frames non-compliance as a criterion failure rather than a section integrity violation. R8 V-01/V-03/V-04/V-05 replace both: the STRUCTURAL AMEND RE-EVALUATION DIRECTIVE applies "on every invocation, independent of whether an AMEND directive is present" (unconditional scope) and frames non-compliance as "a structural failure of this section's integrity" (structural framing). Both discriminators must be present for C-26 to pass.

### Signal 2 — Dedicated FAILURE MODE blocks must be placed before field requirements as independent structural elements

R7 had two forms of failure-mode language that pass C-17 but fail C-27: (1) `> **Anti-pattern**:` embedded inside instruction prose in SYNTHESIS — the reader cannot distinguish it from a section annotation; (2) "A generic placeholder fails" as a trailing sentence in OPEN UNKNOWNS — absorbed into the requirements list. R8 V-02/V-03/V-04/V-05 position `> **FAILURE MODE FOR THIS SECTION**:` as the first element in each section, before the field requirements, so that the block is structurally prior to the content it governs and its absence creates an immediately visible structural gap.

### Signal 3 — C-26 and C-27 are orthogonally addable; V-03 achieves 100 without self-check

V-01 proves C-26 is achievable by adding only the STRUCTURAL AMEND RE-EVALUATION DIRECTIVE to SYNTHESIS (no other section changes needed). V-02 proves C-27 is achievable by adding only the FAILURE MODE blocks to OPEN UNKNOWNS and SYNTHESIS (no AMEND handling changes needed). V-03 confirms both can be added together to any C-01–C-25 base and achieve 100 without any self-check machinery — the structural properties are section-level invariants, not procedural requirements.

### Signal 4 — Self-check items with exact disqualifying forms (V-05) provide the highest pre-write reliability

V-04 adds C-26/C-27 to the self-check with definition-level descriptions. V-05 extends these with the exact textual form that fails each criterion: for C-26, naming the phrase "in this invocation" as the conditional disqualifier and "it fails C-16" as the criterion-reference disqualifier; for C-27, naming `> **Anti-pattern**: Restating sections` and the trailing "A generic placeholder fails" sentence as the disqualifying inline forms. This pattern (naming the exact string that fails) has been the primary driver of execution reliability since R5 — it enables pre-write violation detection rather than post-score discovery.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Unconditional scope + structural framing are the two discriminating properties of C-26: directive must state 'applies on every invocation, independent of whether AMEND is present' (unconditional) and frame non-compliance as 'a structural failure of this section's integrity' (structural) — both disqualifiers 'in this invocation' and 'it fails C-16' must be absent", "Dedicated FAILURE MODE labeled blocks must be placed before field requirements as independent structural elements — their absence creates a visible structural gap, unlike inline anti-pattern text in instruction prose or trailing requirement sentences", "C-26 and C-27 are orthogonally addable: C-26 lives entirely in SYNTHESIS; C-27 lives in OPEN UNKNOWNS and SYNTHESIS; minimal combination (V-03) achieves 19/19 without self-check machinery, confirming these are structural invariants not procedural requirements", "Self-check items with exact disqualifying textual forms enable pre-write violation detection: naming the specific failing string ('in this invocation' for C-26; Anti-pattern blockquote for C-27) is stronger than naming the passing condition alone — this pattern has been the primary reliability driver since R5"]}
```
