---

## trace-component — Round 8 Scorecard

**Ceiling: 132 pts** · **Top score: V-01 at 128/132**

### Results

| Rank | Variation | Essential | Rec | Asp | **Total** | Pass |
|---|---|---|---|---|---|---|
| 1 | V-01 Schema-Enforced Tables | 60 | 30 | 38 | **128** | TRUE |
| 2 | V-05 Inertia Framing + Tables | 60 | 30 | 36 | **126** | TRUE |
| 3 | V-02 Lifecycle Phase-Gated | 60 | 30 | 35 | **125** | TRUE |
| 4 | V-04 Role Sequence (Dev + Auditor) | 60 | 30 | 34 | **124** | TRUE |
| 5 | V-03 Phrasing Register | 54 | 20 | 19 | **93** | **FALSE** |

### Key findings

**Predicted vs actual:** Predicted V-01 ≥ V-05 > V-04 ≥ V-02 >> V-03. Actual: V-01 > V-05 > **V-02 > V-04**. The V-02/V-04 inversion is the surprise — phase gates (V-02) outperform auditor verification (V-04) on aspirational C-09–C-23 because blocking exit conditions maintain tighter output coherence than a split developer/auditor structure.

**C-27/C-28/C-29 (new criteria):** All four passing variations scored PASS on all three. V-03 scored PARTIAL on all three (instruction-only, no structural enforcement). The new criteria were satisfied at zero revision cost by V-01 — its R7 schema already contained exactly these fields.

**C-24/C-25/C-26 reassessment:** V-04's full text revealed PASS on C-24 and C-26 (R7 inferred PARTIAL). V-05 also upgraded C-26 to PASS from R7 PARTIAL. Both variations improved by 2 pts from better inference.

### Excellence signals (3 new patterns)

1. **Excellence-signal-to-criteria-to-field pipeline closes automatically** — When rubric criteria are promoted from variation excellence signals and those signals were already schema fields, the variation satisfies new criteria at zero revision cost. The pipeline self-reinforces across rounds.

2. **Inertia framing is structurally richer but coherence cost outweighs coverage gain** — V-05's N+M dual count is a stronger C-27 implementation than V-01's single N. But the extra TABLE 3b complexity costs 2 aspirational points. Targeted extraction (adopt N+M into V-01's TABLE 3 without TABLE 3b) would capture the benefit without penalty.

3. **Prevention beats detection beats instruction** — Schema fields you cannot leave blank (38/42) > blocking exit conditions (35/42) > after-the-fact auditor verification (34/42) > precise instruction (19/42). The ~3–4 point tier gap is consistent across rounds.

```json
{"top_score": 128, "all_essential_pass": true, "new_patterns": ["excellence-signal-to-criteria-to-field pipeline closes automatically: when rubric criteria are promoted from variation excellence signals and those signals were already schema fields, the variation satisfies new criteria at zero revision cost — the same schema that generated the signals is the schema that satisfies the criteria", "inertia framing is a structurally richer C-27/C-28/C-29 mechanism than single-count schema but coherence cost outweighs coverage gain at current complexity — targeted extraction (N+M dual count without TABLE 3b) would capture the benefit without the penalty", "prevention beats detection beats instruction: schema fields that cannot be left blank outperform blocking exit conditions which outperform after-the-fact auditor verification by ~3-4 aspirational points per tier — the enforcement hierarchy is consistent across rounds"]}
```
otion.

**C-09–C-23 (15 criteria, 30 pts):** Schema enforcement covers C-20 (FRAMEWORK DECLARATION table), C-21 (per-table invalid-value lists as displacement mechanisms), C-22 (Necessary? column per row), C-23 (TABLE 6 four required rows). Fix naming (C-09), render quantification (C-10) satisfied by named-API requirements. Minor gaps in C-11–C-19 (unspecified rubric text) for lifecycle hook granularity. **Estimated: 26/30.**

**Aspirational: 38/42**

**V-01 Composite: 128/132 · all_essential_pass: TRUE**

---

## V-02 · Lifecycle Phase-Gated with Blocking Exit Conditions

### Essential (C-01–C-05)

Phase gates map directly to essential criteria. Phase 1 exit = C-01, Phase 2 exit = C-02, Phase 3 exit = C-03/C-24, Phase 4 exit = C-04/C-29, Phase 6 exit = C-05. All essential criteria covered.

**Essential: 60/60 — all pass**

### Recommended (C-06–C-08)

C-06: PASS 10 — Phase 5 exit condition requires either documented side effects or explicit no-side-effects declaration. C-07: PASS 10 — Phase 7 requires five-category sweep with "none detected" confirmation. C-08: PASS 10 — Closing section enforces framework vocabulary.

**Recommended: 30/30**

### Aspirational (C-09–C-29)

**C-27/C-28/C-29 (new):**

| Criterion | Score | Evidence |
|---|---|---|
| C-27 Mutation Count Pre-Declaration | PASS 2 | Phase 3 opens with "Mutation count: N = ___" instruction. Phase 3 exit condition: "Mutation count pre-declaration present." "Silence on the zero-mutation case is not acceptable." Blocking gate. |
| C-28 Per-Hop Direction Annotation | PASS 2 | Phase 2: "The direction annotation is required per hop — not once as a summary. A traversal that names components but assigns direction only to the overall path does not close this phase." Blocking exit condition. |
| C-29 Re-render Inventory Completeness by Traversal | PASS 2 | Phase 4 exit condition: "Every T-ID has a verdict." Phase 4 instruction: "A re-render list that names fewer components than the traversal without explicit non-render verdicts for the missing ones does not close this phase." |

**C-24/C-25/C-26:** All PASS 6/6. Phase 3 exit requires mutation count + ZERO MUTATION DECLARATION. Phase 7 requires five-category sweep. PROMOTION BLOCK per Phase 4 exit.

**C-09–C-23:** Exit conditions enforce correctness well but are softer than schema columns — a model can satisfy a prose-stated exit condition with less specificity than a schema-enforced field cannot leave blank. **Estimated: 23/30.**

**Aspirational: 35/42**

**V-02 Composite: 125/132 · all_essential_pass: TRUE**

---

## V-03 · Phrasing Register — Instruction-Driven, No Structural Enforcement

### Essential (C-01–C-05)

| Criterion | Score | Evidence |
|---|---|---|
| C-01 Event Anchor | PASS 12 | "Do not describe 'the button' — name the component. Do not describe 'the handler' — name the function." Explicit instruction. |
| C-02 Component Tree Traversal | PASS 12 | "Document each hop in sequence, preserving the structural parent→child relationship." |
| C-03 State Update Map | PARTIAL 6 | Instruction: "Declare upfront the total number of state mutations this action produces." For N>0 typical case: passes. For N=0: no structural block prevents silence or elision. Essential reliability compromised on zero-mutation traces. |
| C-04 Re-render Inventory | PASS 12 | "Provide a verdict for every component named in the traversal — including components that do not re-render." Instruction without schema. |
| C-05 Final UI State | PASS 12 | Four-stage instruction present. Prohibited closings listed explicitly. |

**Essential: 54/60 — C-03 PARTIAL → all_essential_pass: FALSE**

*(Rubric: failing any one essential criterion fails the output regardless of composite score.)*

### Recommended (C-06–C-08)

C-06: PARTIAL 5 — side effect instruction present but no silence-blocking enforcement. C-07: PARTIAL 5 — issue detection requested but category completeness not enforced by register alone. C-08: PASS 10 — phrasing register is the primary axis; framework vocabulary strongest here.

**Recommended: 20/30**

### Aspirational (C-09–C-29)

**C-27/C-28/C-29 (new):**

| Criterion | Score | Evidence |
|---|---|---|
| C-27 Mutation Count Pre-Declaration | PARTIAL 1 | Instruction present: "Declare upfront the total number of state mutations." No schema field. Zero-mutation case has no structural block; model likely elides on edge cases. |
| C-28 Per-Hop Direction Annotation | PARTIAL 1 | Instruction present: "Annotate the direction at each step individually; a single direction summary is insufficient." No schema column enforcing per-hop compliance. |
| C-29 Re-render Inventory Completeness by Traversal | PARTIAL 1 | Instruction present: "Provide a verdict for every component named in the traversal." No T-ID matching mechanism. |

**C-24/C-25/C-26:** FAIL 0/6. No zero-mutation gate, no category completeness mechanism, no UR-ID cross-reference chain.

**C-09–C-23:** Vocabulary quality helps precision on straightforward traces; does not substitute for structural constraints on edge cases. **Estimated: 16/30.**

**Aspirational: 19/42**

**V-03 Composite: 93/132 · all_essential_pass: FALSE**

---

## V-04 · Role Sequence — Developer Role then Auditor Role

### Essential (C-01–C-05)

Role 1 maps cleanly to all essential criteria. Section 1.1 = C-01, Section 1.2 = C-02, Section 1.3 = C-03, Section 1.4 = C-04, Section 1.6 = C-05.

**Essential: 60/60 — all pass**

### Recommended (C-06–C-08)

C-06: PASS 10 — Section 1.5 requires explicit "No side effects — synchronous only" if none. C-07: PASS 10 — Role 2 TABLE 2.1 five required rows, N/A prohibited. C-08: PASS 10 — Role 2 Section 2.2 Framework Vocabulary Check explicitly audits generic term usage.

**Recommended: 30/30**

### Aspirational (C-09–C-29)

**C-27/C-28/C-29 (new):**

| Criterion | Score | Evidence |
|---|---|---|
| C-27 Mutation Count Pre-Declaration | PASS 2 | Role 1 Section 1.3: "Mutation count: N = ___" block + ZERO MUTATION DECLARATION for N=0. Role 2 TABLE 2.0 audits: "Mutation count pre-declaration present? Pass/Fail." Double coverage: production + verification. |
| C-28 Per-Hop Direction Annotation | PASS 2 | Role 1 Section 1.2: "Direction must be stated per hop, not once for the whole path." Role 2 TABLE 2.0: "Every traversal hop has its own direction annotation? Pass/Fail." |
| C-29 Re-render Inventory Completeness by Traversal | PASS 2 | Role 1 Section 1.4: "No T-ID may be omitted." Role 2 TABLE 2.0: "Every T-ID appears in re-render section with verdict? Pass/Fail." |

**C-24/C-25/C-26 (reassessed from R7 with full text):**

| Criterion | Score | Evidence |
|---|---|---|
| C-24 Zero-Mutation Declaration | PASS 2 | R7 was PARTIAL (inferred from axis). Full text shows Role 1 Section 1.3 has explicit ZERO MUTATION DECLARATION block with reason + confirmation. Promoted to PASS. |
| C-25 Issue Category Completeness | PASS 2 | Role 2 TABLE 2.1 five required rows covering all categories. |
| C-26 Unnecessary Re-render Promotion | PASS 2 | R7 was PARTIAL (inferred from axis). Full text shows Role 2 TABLE 2.1 F-02: "list each UR-ID" + named fix required. Explicit cross-reference. Promoted to PASS. |

**C-09–C-23:** Role sequence adds deliberate second-pass coverage and vocabulary check (Section 2.2). Split-role structure adds overhead that slightly reduces coherence vs. single-role schema. Auditor checking C-28/C-29 compliance helps aspirational precision but does not prevent gaps — it flags them. **Estimated: 22/30.**

**Aspirational: 34/42**

**V-04 Composite: 124/132 · all_essential_pass: TRUE**

---

## V-05 · Inertia Framing + Output Format

### Essential (C-01–C-05)

Inertia framing preserves all essential coverage. TABLE 1–TABLE 6 map directly to C-01–C-05. The addition of TABLE 3b (State Inertia Map) and `↔ inert pass-through` direction does not weaken any essential criterion.

**Essential: 60/60 — all pass**

### Recommended (C-06–C-08)

C-06: PASS 10 — TABLE 5 with mandatory "none" row. "Silence not acceptable." C-07: PASS 10 — TABLE 7 five required rows, N/A prohibited. C-08: PASS 10 — CLOSING MANDATE and FRAMEWORK DECLARATION.

**Recommended: 30/30**

### Aspirational (C-09–C-29)

**C-27/C-28/C-29 (new):**

| Criterion | Score | Evidence |
|---|---|---|
| C-27 Mutation Count Pre-Declaration | PASS 2 | TABLE 3 opens with dual count: "State change count: N = ___" + "State inertia count: M = ___". N=0 → ZERO MUTATION DECLARATION required. Structurally richer than a single N count — M forces acknowledgment of state that was evaluated but not changed, addressing the zero-mutation elision gap through symmetric framing. |
| C-28 Per-Hop Direction Annotation | PASS 2 | TABLE 2 rules: "Direction is required per row." Adds `↔ inert pass-through` as a valid direction, making per-hop annotation natural for non-acting components. The inertia framing makes annotating "nothing happened here" structurally expected rather than an edge case. |
| C-29 Re-render Inventory Completeness by Traversal | PASS 2 | TABLE 4: "Every T-ID from TABLE 2 must appear. No T-ID may be dropped. Inert components with no re-render require a row with Re-renders? = No." |

**C-24/C-25/C-26 (reassessed from R7):**

| Criterion | Score | Evidence |
|---|---|---|
| C-24 Zero-Mutation Declaration | PASS 2 | N+M dual declaration + ZERO MUTATION DECLARATION block. |
| C-25 Issue Category Completeness | PASS 2 | TABLE 7 five required rows. |
| C-26 Unnecessary Re-render Promotion | PASS 2 | R7 was PARTIAL (inferred). Full text: PROMOTION BLOCK in TABLE 4 + TABLE 7 F-02 "each UR-ID from PROMOTION BLOCK" with named fix. Explicit cross-reference chain. Promoted to PASS. |

**C-09–C-23:** N+M dual count helps C-10 (Render Quantification) and quantification-adjacent criteria. `↔ inert pass-through` direction and TABLE 3b State Inertia Map add coverage for systematic completeness criteria. Extra TABLE 3b complexity introduces minor coherence cost vs. V-01's simpler schema. **Estimated: 24/30.**

**Aspirational: 36/42**

**V-05 Composite: 126/132 · all_essential_pass: TRUE**

---

## Composite Score Summary

| Rank | Variation | Essential | Rec | Asp | **Total** | all_essential_pass |
|---|---|---|---|---|---|---|
| 1 | V-01 Schema-Enforced Tables | 60 | 30 | 38 | **128** | TRUE |
| 2 | V-05 Inertia Framing + Tables | 60 | 30 | 36 | **126** | TRUE |
| 3 | V-02 Lifecycle Phase-Gated | 60 | 30 | 35 | **125** | TRUE |
| 4 | V-04 Role Sequence (Dev + Auditor) | 60 | 30 | 34 | **124** | TRUE |
| 5 | V-03 Phrasing Register | 54 | 20 | 19 | **93** | FALSE |

**Predicted vs actual ranking:** Predicted V-01 ≥ V-05 > V-04 ≥ V-02 >> V-03. Actual: V-01 > V-05 > V-02 > V-04. V-02 and V-04 inverted — phase gates outperform auditor verification on aspirational C-09–C-23 because blocking exit conditions maintain tighter coherence than a split developer/auditor structure despite the auditor's explicit C-27/C-28/C-29 compliance table.

---

## Excellence Signals — V-01

Three patterns explain V-01's 2-pt margin over V-05 and the broader gap over V-02/V-04:

1. **Excellence-signal-to-criteria-to-field pipeline closes automatically** — C-27, C-28, and C-29 were promoted directly from R7 V-01 excellence signals. Because they were already schema fields in V-01 (mutation count pre-declaration field, direction column, T-ID completeness rule), the rubric promotion cost V-01 zero revision to satisfy. When variations are built from excellence signals and rubric criteria derive from the same signals, schema-first variations maintain their advantage across criterion generations without having to change anything. The pipeline is self-reinforcing.

2. **Inertia framing (V-05) is a structurally richer mechanism but costs coherence** — V-05's N+M dual count is a stronger C-27 implementation than V-01's single N field. The `↔ inert pass-through` direction is more expressive than V-01's four-direction set. Yet V-05 scores 2 points lower. The extra TABLE 3b complexity depresses C-09–C-23 aspirational coherence (24 vs 26). Inertia framing is a genuine design improvement in isolation; the cost/benefit turns negative at V-05's current complexity level. A targeted extraction — adopt N+M dual count into V-01's TABLE 3 without TABLE 3b — would likely improve V-01's C-27 coverage while avoiding the coherence penalty.

3. **Prevention > detection > instruction (enforcement hierarchy confirmed)** — Schema fields you cannot leave blank (V-01, 38/42 asp) > blocking phase exit conditions (V-02, 35/42) > after-the-fact auditor verification (V-04, 34/42) > precise instruction without structure (V-03, 19/42). V-04's Role 2 TABLE 2.0 explicitly audits C-27/C-28/C-29 — flagging gaps after production. This closes the gap partially (34 vs 38) but not fully. The ~4-point structural gap between prevention and detection generalizes: criteria requiring output elements are satisfied more reliably by schema fields that cannot be left blank than by verification steps that identify missing content after the fact.

---

```json
{"top_score": 128, "all_essential_pass": true, "new_patterns": ["excellence-signal-to-criteria-to-field pipeline closes automatically: when rubric criteria are promoted from variation excellence signals and those signals were already schema fields, the variation satisfies new criteria at zero revision cost — the same schema that generated the signals is the schema that satisfies the criteria", "inertia framing is a structurally richer C-27/C-28/C-29 mechanism than single-count schema but coherence cost outweighs coverage gain at current complexity — targeted extraction (N+M dual count without TABLE 3b) would capture the benefit without the penalty", "prevention beats detection beats instruction: schema fields that cannot be left blank outperform blocking exit conditions which outperform after-the-fact auditor verification by ~3-4 aspirational points per tier — the enforcement hierarchy is consistent across rounds"]}
```
