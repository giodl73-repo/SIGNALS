Now I have the complete picture. The R3 scorecard resolves the key discrepancy: R3-V-01 scored 117.5 because C-17 **failed** under rubric v3's stricter definition (interrogative form was not enough). Rubric v4 **relaxed C-17 to a floor** (peer-comparison structure present in any form) and added C-19/C-20 as the ceiling. This means the R4 base for V-01/V-02 is 120 under rubric v4 (not 117.5), so adding C-19 or C-20 gives 122.5.

---

## R4 Scoring — draft-brainstorm

### Framework Recap

| Tier | Criteria | Pts each | Max |
|------|----------|----------|-----|
| Essential | C-01..C-05 | 12 | 60 |
| Recommended | C-06..C-08 | 10 | 30 |
| Aspirational | C-09..C-10 | 5 | 10 |
| R2 extended | C-11..C-14 | 2.5 | 10 |
| R3 aspirational | C-15..C-18 | 2.5 | 10 |
| R4 aspirational | C-19..C-20 | 2.5 | 5 |
| **Max** | | | **125** |

Rubric v4 key change: C-17 is now the **floor** (peer-comparison structure present in any form passes). C-19 (imperative + materialization) and C-20 (consequence clause) are the ceiling. R3-V-01 retroactively scores 120 under rubric v4 (C-17 now passes at floor), not 117.5.

---

## V-01 — Phrasing Register: Imperative Peer Test (C-19 isolation)

**Base**: R3-V-01 — C-15 PASS, C-16 PASS, C-17 PASS (floor), C-18 PASS → 120 under rubric v4.
**Axis**: Convert Check B from interrogative to imperative with output-materialization. No consequence clause (intentional isolation).

| Tier | C-01 | C-02 | C-03 | C-04 | C-05 | Result |
|------|------|------|------|------|------|--------|
| Essential | PASS | PASS | PASS | PASS | PASS | 60 |

| C-06 | C-07 | C-08 | Result |
|------|------|------|--------|
| PASS | PASS | PASS | 30 |

| C-09 | C-10 | Result |
|------|------|--------|
| PASS | PASS | 10 |

| C-11 | C-12 | C-13 | C-14 | Result |
|------|------|------|------|--------|
| PASS | PASS | PASS | PASS | 10 |

**R3 criteria:**

| ID | Result | Evidence |
|----|--------|----------|
| C-15 | PASS | "These are **not suggestions or scaffolding** -- each dimension is a required `##` section… Do not collapse… Do not omit." 6 mandated structural positions. |
| C-16 | PASS | "**Do not mark top-5 yet.**" in Phase 1b (generation block), imperative. |
| C-17 | PASS | Check B: "complete this sentence: 'I chose [Idea Name] over [name one specific unmarked idea in the same section] because ___'" — sentence-completion structure named, peer named. Floor pass. |
| C-18 | PASS | Phase 2 has 4 checks; Phase 3 explicitly "informed by Check A and B" and "Update AMEND items if Check C required changes" — review-to-output links named. |

**R4 criteria:**

| ID | Result | Evidence |
|----|--------|----------|
| C-19 | **PASS** | Check B: "complete this sentence **and write it in your output**" + "Write all five completed sentences **before moving to Check C**." Imperative form. Explicit output-materialization requirement. Cannot be answered silently. |
| C-20 | **FAIL** | No consequence clause present. After requiring the sentence, no named action follows if the test cannot be satisfied. Intentional isolation to test C-19 alone. |

**Score: 60 + 30 + 10 + 10 + 10 + 2.5 = 122.5**
Golden: YES (≥80, no essential failures)

Note: Variate file projects 120 based on R3's v3 score (117.5 + 2.5). Under rubric v4's relaxed C-17 definition, the base is 120, making V-01 = **122.5**.

---

## V-02 — Lifecycle Emphasis: Consequence Gate (C-20 isolation)

**Base**: R3-V-01 — same base as V-01. C-15 PASS, C-16 PASS, C-17 PASS (floor), C-18 PASS → 120 under rubric v4.
**Axis**: Add mandatory replacement consequence to Check B. Interrogative form preserved (intentional isolation for C-20).

Essential, Recommended, Aspirational, R2: identical pass pattern to V-01 → 110.

**R3 criteria:**

| ID | Result | Evidence |
|----|--------|----------|
| C-15 | PASS | Same as V-01 — 6 required dimensions as mandatory `##` sections. |
| C-16 | PASS | "**Do not mark top-5 yet.**" in Phase 1b, imperative. |
| C-17 | PASS | Check B: "can you complete this sentence: 'I chose this over [name one specific unmarked idea in the same section] because ___'?" — peer-comparison structure named. Interrogative form is the C-19 failure, not C-17 floor. |
| C-18 | PASS | Phase 2 with 4 checks; Phase 3 "informed by Check A and B" / "Update AMEND if Check C required changes." |

**R4 criteria:**

| ID | Result | Evidence |
|----|--------|----------|
| C-19 | **FAIL** | Check B asks "can you complete this sentence" — interrogative form preserved intentionally. Model can answer "yes" silently without writing the sentence. No output-materialization requirement. |
| C-20 | **PASS** | "If you cannot name a specific peer or state a specific reason for any marked idea, **that idea must be replaced with the specific peer you attempted to name**. Do not revise the idea's rationale to manufacture a distinction… **if the distinction does not hold on inspection, the replacement is mandatory.**" Named action: replace. Hard gate. |

**Score: 60 + 30 + 10 + 10 + 10 + 2.5 = 122.5**
Golden: YES

Note: Same base-calculation issue as V-01. Variate projects 120; rubric v4 correct score is **122.5**.

---

## V-03 — Output Format: Peer Justification Table (C-19+C-20 via schema)

**Base**: R3-V-05 — table format. C-15 PASS, C-16 PASS, C-17 PASS (floor), C-18 PASS → 120 under rubric v4.
**Axis**: Encode both C-19 and C-20 into a required output table schema (Peer Justification Table at Step 3b).

Essential, Recommended, Aspirational, R2: all pass → 110.

**R3 criteria:**

| ID | Result | Evidence |
|----|--------|----------|
| C-15 | PASS | Category View (Step 4): "required structural output… must contain a section for every Dimension present in the table. A flat list fails." + 7 required dimension types mandated in idea table. |
| C-16 | PASS | Step 1: "Leave this column **blank during Step 1.** Do not fill in Top-5? values as you build the table… Marking during construction introduces sequential bias." Generation-phase imperative with bias explanation. |
| C-17 | PASS | Review B requires identifying "one specific unmarked row in the same Dimension" + Peer Justification Table schema requires completing the sentence as a table row. Peer-comparison structure explicitly named and structurally materialized. |
| C-18 | PASS | Self-Review Phase labels each review with downstream target: "Review A (determines top-5 marking in Step 3)", "Review B (determines top-5 marking in Step 3b)", "Review C (determines AMEND content in Step 5)", "Review D (determines Category View completeness in Step 4)." Every link auditable. |

**R4 criteria:**

| ID | Result | Evidence |
|----|--------|----------|
| C-19 | **PASS** | Step 3b: "For each of the 5 marked rows, produce one row in this table: \| Marked Idea \| Peer (same Dimension, unmarked) \| Because (specific reason) \|" + "All 5 rows must be filled before proceeding." Table row = materialized sentence. Cannot be answered silently — the table row IS the output. Schema structure enforces materialization by construction, not by instruction compliance. |
| C-20 | **PASS** | "**If you cannot fill the Peer or Because field for any row**: remove the `**YES**` mark from that row and move the mark to the idea named in the Peer column. Do not revise the original row's rationale to manufacture a distinction -- if the comparison cannot be stated, the substitution is mandatory." Named action: remove mark + move. Encoded as a column rule, not prose instruction. |

**Score: 60 + 30 + 10 + 10 + 10 + 5 = 125**
Golden: YES

---

## V-04 — Combination: Phrasing Register + Lifecycle Emphasis (C-19+C-20 prose)

**Base**: R3-V-01. C-15 PASS, C-16 PASS, C-17 PASS, C-18 PASS → 120 under rubric v4.
**Axis**: Check B carries imperative form + output-materialization (C-19) AND mandatory replacement (C-20) in a single instruction block.

Essential, Recommended, Aspirational, R2: all pass → 110.

**R3 criteria:**

| ID | Result | Evidence |
|----|--------|----------|
| C-15 | PASS | Same as V-01 — 6 required dimensions as mandatory `##` sections. |
| C-16 | PASS | "**Do not mark top-5 yet.**" in Phase 1b, imperative. |
| C-17 | PASS | Check B: "complete this sentence: 'I chose [Idea Name] over [name one specific unmarked idea in the same section] because ___'" — sentence-completion structure with named peer. |
| C-18 | PASS | Phase 2 with 4 checks; Phase 3 "informed by Check A and B" and "Update AMEND items if Check C required changes." |

**R4 criteria:**

| ID | Result | Evidence |
|----|--------|----------|
| C-19 | **PASS** | Check B: "complete this sentence **and write it in your output**: 'I chose [Idea Name] over [name one specific unmarked idea in the same section] because ___.' … **Write all five completed sentences in your output before proceeding to Check C.**" Imperative form. Explicit output-materialization. Sequencing gate. |
| C-20 | **PASS** | Check B continuation: "If you cannot complete the sentence for any pick -- no specific peer comes to mind or no specific reason holds -- **that pick must be replaced with the specific peer you named**. Do not revise the pick's rationale to manufacture a distinction; if the distinction is not already present in the pool, **the replacement is mandatory.**" Named action: replace. No softening language. |

**Score: 60 + 30 + 10 + 10 + 10 + 5 = 125**
Golden: YES

Variate file self-correction confirmed: both C-19 and C-20 pass, correcting the initial 122.5 projection to **125**.

---

## V-05 — Full Stack: All Six R3+R4 Criteria

**Base**: R3-V-04 (multi-phase self-review architecture). C-15 PASS, C-16 PASS, C-17 PASS, C-18 PASS → 120 under rubric v4.
**Axis**: Convert Review B from "Why [Name] and not [peer]?" question form to explicit sentence-completion + materialization gate + mandatory replacement.

Essential, Recommended, Aspirational, R2: all pass → 110.

**R3 criteria:**

| ID | Result | Evidence |
|----|--------|----------|
| C-15 | PASS | 7 dimensions each mandated as `##` header in Axis Map. "Do not mark any idea with `**` in this section." Structural enforcement. |
| C-16 | PASS | Axis Map: "**Do not mark any idea with `**` in this section.** Selection happens after the full pool is complete. Marking ideas as you generate them introduces sequential bias -- the first ideas written are the most available, not the best." Generation-phase, imperative, with bias explanation. |
| C-17 | PASS | Review B: "complete this sentence and write it in your output: 'I chose [Idea Name] over [name one specific unmarked idea in the same Dimension] because ___'" — named sentence-completion structure with peer. |
| C-18 | PASS | Self-Review Phase with four reviews labeled by downstream target: "Review A (determines which candidates proceed to Review B)", "Review B (determines final top-5 marks)", "Review C (determines AMEND finalization)", "Review D (gates the final write)". Top-5 Selection section labeled "(output of Review A and B)". |

**R4 criteria:**

| ID | Result | Evidence |
|----|--------|----------|
| C-19 | **PASS** | Review B: "complete this sentence **and write it in your output**: 'I chose [Idea Name] over [name one specific unmarked idea in the same Dimension] because ___.' … **Write all five completed sentences in your output before proceeding to Review C. Do not advance to the Top-5 Selection step until all five sentences are written.**" Imperative. Output-materialization. Double-reinforced phase gate. |
| C-20 | **PASS** | Review B continuation: "If you cannot complete the sentence for any candidate -- no specific peer comes to mind or no specific reason holds -- **that candidate must be replaced with the specific peer you named**. Do not revise the candidate's rationale to manufacture a distinction; if the comparison does not hold on inspection, **the replacement is mandatory.**" Named action: replace. No escape clause. |

**Score: 60 + 30 + 10 + 10 + 10 + 5 = 125**
Golden: YES

---

## Composite Scores and Ranking

| Rank | Variation | C-15 | C-16 | C-17 | C-18 | C-19 | C-20 | Score | Delta vs projected |
|------|-----------|------|------|------|------|------|------|-------|--------------------|
| 1 | **V-03** (table schema) | PASS | PASS | PASS | PASS | PASS | PASS | **125** | +0 |
| 1 | **V-04** (prose combo) | PASS | PASS | PASS | PASS | PASS | PASS | **125** | +2.5 (corrected) |
| 1 | **V-05** (full stack) | PASS | PASS | PASS | PASS | PASS | PASS | **125** | +0 |
| 4 | V-01 (C-19 isolation) | PASS | PASS | PASS | PASS | PASS | FAIL | **122.5** | +2.5 (base correction) |
| 4 | V-02 (C-20 isolation) | PASS | PASS | PASS | PASS | FAIL | PASS | **122.5** | +2.5 (base correction) |

All 5 variations: all essential criteria PASS. All 5 are golden.

---

## Projection Correction Note

The variate file projected V-01=120, V-02=120, V-04=122.5 (then self-corrected to 125). The root cause: projected scores used R3's v3 score (117.5) as the base, but rubric v4 relaxed C-17's definition. Under rubric v4, the peer-comparison structure in R3-V-01's Check B ("can you complete this sentence: 'I chose this over [peer] because ___'?") now passes C-17 at floor — the floor only requires the structure to be named. Interrogative form is a C-19 failure, not a C-17 failure. Correct base = 120. Hence V-01 = 120 + 2.5 (C-19) = 122.5, V-02 = 120 + 2.5 (C-20) = 122.5.

---

## Excellence Signals — Patterns from the 125-Scoring Variations

### Signal 1: Schema-encoded compliance vs. prose-instruction compliance (V-03)

V-03 achieves C-19 and C-20 not through prose instructions but through output table schema. The Peer Justification Table makes materialization **structurally mandatory** — there is no way to "silently affirm" when the completed sentence is a required table row. The consequence clause is a **column rule** ("if you cannot fill the Peer or Because field, remove mark and move it to the Peer column") rather than a prose instruction. Schema-level encoding is immune to the interrogative-vs-imperative failure mode entirely: the question of form is irrelevant when output structure forces the sentence to be written.

### Signal 2: Unified imperative-consequence block in minimal footprint (V-04/V-05)

V-04 achieves 125 from the same two-phase prose architecture as V-01/V-02, by combining three requirements into a single Check B block without degradation: (1) "complete this sentence and write it in your output" (imperative + materialization), (2) "Write all five completed sentences before proceeding" (phase gate), (3) "if you cannot complete it, that pick must be replaced… the replacement is mandatory" (named consequence). The combination test passed: a single instruction can carry all three without becoming internally contradictory or too cluttered for model compliance.

### Signal 3: Double-reinforced phase gate (V-05 ceiling pattern)

V-05 adds a second gate phrase not present in V-04: "**Do not advance to the Top-5 Selection step until all five sentences are written.**" This upgrades the completion requirement from an instruction ("write before proceeding") to a **named phase boundary**. The gate is tied to a named downstream step (Top-5 Selection), making the consequence of skipping concrete rather than implicit. V-04 relies on sequencing ("before proceeding to Check C"). V-05 names the blocked step. Both score 125 under rubric v4, but V-05's double gate is structurally more durable if the prompt is compressed or reordered.

---

```json
{"top_score": 125, "all_essential_pass": true, "new_patterns": ["schema-encoded consequence: encoding C-19+C-20 as required output table column rules makes materialization structurally mandatory rather than instruction-compliance-dependent, bypassing the interrogative-vs-imperative failure mode entirely", "unified imperative-consequence block: single Check B carrying imperative completion + output-materialization + named replacement in one coherent instruction achieves both C-19 and C-20 without bloat or degradation", "double-reinforced phase gate: naming the blocked downstream step ('do not advance to Top-5 Selection until all five sentences are written') upgrades the completion requirement from a sequencing instruction to a structural phase boundary"]}
```
