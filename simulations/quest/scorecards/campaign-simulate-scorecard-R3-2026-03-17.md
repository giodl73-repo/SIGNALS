---

# campaign-simulate — Round 3 Scorecard

**Rubric**: v3 (2026-03-17) | **Variations**: V-01 through V-05  
**Evaluator note**: No trace artifact available; scoring evaluates prompt design reliability — how confidently each variation's structure produces rubric-compliant output.

---

## Essential Criteria (C-01 through C-05, 12 pts each)

All five variations PASS all essential criteria. Each variation includes five labeled sub-skill sections (C-01), a RANKED FINDINGS section with explicit blast-radius sort and Rank column (C-02), a 10-column unified schema declaring System Boundary and Severity per row (C-03), trace-contract and trace-state instructions that explicitly target divergence and unenforced invariants (C-04), and a single unified findings table structure rather than five disconnected outputs (C-05).

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 All five sub-skills | PASS | PASS | PASS | PASS | PASS |
| C-02 Ranked by blast radius | PASS | PASS | PASS | PASS | PASS |
| C-03 Boundary + severity per finding | PASS | PASS | PASS | PASS | PASS |
| C-04 Spec gap or contract violation | PASS | PASS | PASS | PASS | PASS |
| C-05 Single synthesized report | PASS | PASS | PASS | PASS | PASS |
| **Essential subtotal** | **60** | **60** | **60** | **60** | **60** |

---

## Recommended Criteria (C-06 through C-08, 10 pts each)

All five variations PASS all recommended criteria. Every variation's flow-lifecycle section names exception paths without recovery and undeclared terminal states (C-06); flow-conversation probes dead ends and loops (C-06). The Sub-Skill column in the unified schema guarantees >= 80% attribution by construction (C-07). trace-state instructions explicitly call for exit-less states, early-firing transitions, unenforced invariants, and unreachable states (C-08).

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Exception paths + edge cases | PASS | PASS | PASS | PASS | PASS |
| C-07 Cross-reference source sub-skill | PASS | PASS | PASS | PASS | PASS |
| C-08 State machine anomalies | PASS | PASS | PASS | PASS | PASS |
| **Recommended subtotal** | **30** | **30** | **30** | **30** | **30** |

---

## Aspirational Criteria (C-09 through C-18, 1 pt each)

This tier is where Round 3's variation axes differentiate. C-09 through C-13 are uniform across all variations; C-14 through C-18 are the five targeted criteria.

### C-09 through C-13 — Uniform Aspirational

All five variations include a TEST SCENARIO BASELINE section (C-09), F-ID column in the schema (C-10), severity budget >= 1 CRITICAL/HIGH per trace sub-skill (C-11), 10-column structured table with no-blank-cell contract (C-12), and explicit "at least one flow-lifecycle finding must carry a non-'none' Trace Link" instruction (C-13).

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 Test scenario baseline | PASS | PASS | PASS | PASS | PASS |
| C-10 F-NN IDs | PASS | PASS | PASS | PASS | PASS |
| C-11 CRITICAL/HIGH budget per trace sub-skill | PASS | PASS | PASS | PASS | PASS |
| C-12 Structured table, no blank cells | PASS | PASS | PASS | PASS | PASS |
| C-13 Flow findings reference trace context | PASS | PASS | PASS | PASS | PASS |

---

### C-14: System Boundary Vocabulary Pre-Assigned

- **V-01**: PASS — dedicated two-column vocabulary lookup table at the very top of the prompt, before any sub-skill instruction; "copy verbatim, do not infer" is explicit.
- **V-02**: PASS — boundary labels carried in the Sentinel Manifest with "copy from the Sentinel Manifest -- never infer or substitute." The manifest is the vocabulary source.
- **V-03**: PASS — boundary labels explicitly stated per sub-skill in the execution order ("System Boundary = 'state machine'") and in each sub-skill section. Labels are pre-assigned per sub-skill, making boundary entry a copy, not an inference. Weaker mechanism than V-01 (no dedicated lookup table) but the pass condition targets output correctness, which is met.
- **V-04**: PASS — schema contract vocabulary map at top + manifest both carry the labels; double-enforcement.
- **V-05**: PASS — schema contract vocabulary map (dedicated two-column table) + manifest; identical to V-04 plus the gate validates them.

| C-14 | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| | PASS | PASS | PASS | PASS | PASS |

---

### C-15: Universal Sentinel Rule Across All Columns

All five variations include "optional fields that do not apply: 'N/A -- [reason]' -- not blank, not a dash" in their no-blank-cell contract. V-02 adds the demonstration: manifest rows show fully-populated cells including optional fields. V-05 adds the gate as post-execution enforcement.

| C-15 | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| | PASS | PASS | PASS | PASS | PASS |

---

### C-16: No-Findings Sentinel Rows for Clean Sub-Skills

The critical differentiator between the single-axis and combined variations.

- **V-01**: FAIL — sentinel row rule is stated inside the FINDINGS TABLE section ("A sub-skill with no findings must still appear in the table as a sentinel row") but there is no pre-written manifest. Compliance requires the author to recall and apply the rule at clean-run time. Recall-based — the failure mode C-16 was designed to close.
- **V-02**: PASS — SENTINEL MANIFEST (Step 0) pre-writes all five sentinel rows before any sub-skill executes. "If a sub-skill produces 0 findings: copy its manifest row verbatim." Copy-paste is structurally more reliable than recall.
- **V-03**: FAIL — sentinel row rule appears inline in the flow-conversation section only ("A sub-skill with no findings gets a sentinel row"). Positioned in sub-skill 5's instructions; not a pre-written manifest; not visibly scoped to all sub-skills. Recall-based, same failure mode as V-01.
- **V-04**: PASS — Sentinel Manifest pre-writes all five rows; "zero findings = copy sentinel verbatim; sub-skill absent from table = execution gap."
- **V-05**: PASS — Sentinel Manifest pre-writes all five rows; "absence is never evidence of a clean run."

| C-16 | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| | FAIL | PASS | FAIL | PASS | PASS |

---

### C-17: Pre-Output Blank-Cell Verification Gate

The critical differentiator between the gate-axis and non-gate variations.

- **V-01**: FAIL — "Before writing: run blank-cell check. Every row, every column." This is an instruction to run the check, not a named section that must appear in the output. The required output sections list does not include a gate. The output would show clean cells but no inspectable audit record.
- **V-02**: FAIL — "Before writing: confirm every sub-skill has at least one row. Confirm no blank cells." Same pattern as V-01: an instruction, not a named section in the output structure. No per-column audit table.
- **V-03**: PASS — BLANK-CELL VERIFICATION GATE is a named section in the required output (position 8 of 10). Produces a per-column audit table with "Blank Cells Found / Action Taken / Status (PASS/FAIL)" per column and Overall status. "Do not write the output file until Overall = PASS."
- **V-04**: FAIL — "Before writing: confirm every sub-skill has at least one row. Verify all boundary labels match the schema contract vocabulary map. No blank cells." An inline instruction — does not appear in the required output sections list as a named section. No per-column audit table.
- **V-05**: PASS — BLANK-CELL VERIFICATION GATE is a named section (position 10 of 12 in required output). Per-column audit table, Overall = PASS required before file is written.

| C-17 | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| | FAIL | FAIL | PASS | FAIL | PASS |

---

### C-18: Unified Schema Closes C-03/C-07/C-10/C-13

All five variations declare a single 10-column unified table (F-ID, Sub-Skill, System Boundary, Type, Spec Location, Summary, Severity, Blast Radius, Trace Link, Remediation) that satisfies all four criteria by inspection of one artifact. No variation uses a multi-table design.

| C-18 | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| | PASS | PASS | PASS | PASS | PASS |

---

## Full Aspirational Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 | 1 | 1 | 1 | 1 | 1 |
| C-10 | 1 | 1 | 1 | 1 | 1 |
| C-11 | 1 | 1 | 1 | 1 | 1 |
| C-12 | 1 | 1 | 1 | 1 | 1 |
| C-13 | 1 | 1 | 1 | 1 | 1 |
| C-14 | 1 | 1 | 1 | 1 | 1 |
| C-15 | 1 | 1 | 1 | 1 | 1 |
| C-16 | **0** | 1 | **0** | 1 | 1 |
| C-17 | **0** | **0** | 1 | **0** | 1 |
| C-18 | 1 | 1 | 1 | 1 | 1 |
| **Aspirational subtotal** | **8** | **9** | **9** | **9** | **10** |

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 60 | 30 | 8 | **98** |
| V-02 | 60 | 30 | 9 | **99** |
| V-03 | 60 | 30 | 9 | **99** |
| V-04 | 60 | 30 | 9 | **99** |
| V-05 | 60 | 30 | 10 | **100** |

**Rank**: V-05 (100) > V-02 = V-03 = V-04 (99) > V-01 (98)

---

## Ranking Analysis

**V-05 wins by closing the specific gap that separates 99 from 100**: C-17, the pre-output blank-cell verification gate.

V-02, V-03, and V-04 each miss exactly one of the two C-16/C-17 objectives:
- V-02 and V-04 close C-16 (sentinel manifest) but miss C-17 (no named gate section in output)
- V-03 closes C-17 (named gate section) but misses C-16 (no pre-written manifest; recall-based sentinel)

V-01 misses both — it is the prompt that closest resembles the baseline (all-in-one execution flow with no pre-execution artifacts), and it loses exactly on the two criteria that pre-execution artifacts were designed to close.

The single-axis variations (V-01, V-02, V-03) each solve one dimension. The combined variations (V-04, V-05) solve two and three dimensions respectively.

---

## Excellence Signals from V-05

**Signal 1: Three-layer enforcement architecture**
Schema contract (vocabulary source, read before finding #1) → Sentinel Manifest (sentinel content, written before execution #1) → Verification Gate (completeness proof, written before file #1). Each layer targets a different compliance failure mode: hallucinated labels, forgotten sentinel rows, and invisible blank cells. No compliance requirement depends on author recall during the finding-writing phase.

**Signal 2: Setup artifacts are mandatory output sections, not preamble**
V-05's required output sections list includes Schema Contract (section 1), Sentinel Manifest (section 2), and Blank-Cell Verification Gate (section 10). These artifacts are not prompt scaffolding that disappears — they must appear in the artifact itself. An output missing any of these three sections is structurally incomplete regardless of finding quality.

**Signal 3: Verification gate produces evidence, not assertion**
The gate section contains a per-column audit table with "Blank Cells Found / Action Taken / Status" per column. The gate cannot be satisfied by marking it "PASS" without data — blank cell counts must be written, making any compliance failure visible as a cell in the gate table rather than inferred from absence of blanks.

**Signal 4: Sentinel manifest carries vocabulary, eliminating redundant recall**
In V-04 and V-05, the sentinel manifest rows contain the boundary vocabulary (e.g., `trace-state | state machine | ...`). An author copying a manifest row verbatim gets the correct boundary label for free — they do not need to cross-reference the vocabulary map separately. Two compliance requirements (C-14 and C-16) are satisfied by a single copy operation.

**Signal 5: Absence is named as a failure mode, not just empty space**
V-05's manifest includes "A sub-skill absent from the findings table = execution gap. Absence is never evidence of a clean run." This transforms the missing-row problem from an invisible gap (silent failure) into a labeled failure category. The gate section cannot pass with a missing sub-skill row — the PASS condition requires all sub-skills to appear.

---

## Round 3 Conclusion

Round 3's hypothesis was confirmed: single-axis variations (V-01, V-02, V-03) each close one of the three new mechanisms but cannot close all five new criteria simultaneously. The combination in V-05 is not merely additive — the three artifacts (schema contract, sentinel manifest, verification gate) form an interlocking enforcement chain where each artifact reinforces the others. R2 V-05 already scored 100 on this rubric; R3 V-05 confirms the same architecture holds when the rubric criteria are explicit rather than post-hoc observations.

No new patterns beyond those formalized in the v3 rubric. The rubric has caught up to the gold standard.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": []}
```
