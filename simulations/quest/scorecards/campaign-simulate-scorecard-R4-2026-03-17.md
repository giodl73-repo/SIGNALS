Now I have all the data I need. Let me score all five variations against the rubric.

---

# campaign-simulate — Round 4 Scorecard

**Rubric**: v3 (18 criteria, max 100 pts)
**Date**: 2026-03-17
**Variations scored**: V-01 through V-05

---

## Scoring Key

| Result | Points Applied |
|--------|---------------|
| PASS | Full points |
| PARTIAL | Half points |
| FAIL | 0 |

---

## Essential Criteria (60 pts)

### C-01 · All Five Sub-Skills Execute (12 pts)

All five variations include labeled execution sections for all five sub-skills (trace-state, trace-contract, trace-permissions, flow-lifecycle, flow-conversation) with distinct instructions per sub-skill.

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| **Result** | PASS | PASS | PASS | PASS | PASS |
| **Evidence** | Explicit 5-sub-skill execution order | Explicit 5-sub-skill execution sequence | Explicit 5-sub-skill sequence | Explicit trace-first then flow | Explicit trace-first then flow |

---

### C-02 · Findings Ranked by Blast Radius (12 pts)

All five variations include a UNIFIED FINDINGS REPORT with blast radius as the sort key (system-wide first) and an explicit Blast Radius column in the ranked table.

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| **Result** | PASS | PASS | PASS | PASS | PASS |
| **Evidence** | "Rank by blast radius (system-wide first)" + Blast Radius column | Same | Same | Ranked Findings step + Blast Radius column | Same + blast radius rationale required for top-tier findings |

---

### C-03 · System Boundary and Severity per Finding (12 pts)

All five variations pre-assign system boundary labels per sub-skill (state machine, contract surface, permission check, lifecycle phase, conversation state) and include Severity as a required field in each finding block or table row.

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| **Result** | PASS | PASS | PASS | PASS | PASS |
| **Evidence** | Boundaries hardcoded in finding block schemas; Severity field required | Type Vocabulary Map table includes System Boundary column; Severity field required | Boundaries hardcoded per sub-skill schema; Severity field required | Type Vocabulary Map + unified 10-column schema; explicit copy-from-map instruction | Same as V-04; "System Boundary and Type must be copied from this table" |

---

### C-04 · At Least One Spec Gap or Contract Violation (12 pts)

All five variations have sub-skill instructions that explicitly target spec gaps (trace-contract finds "undocumented edge case behaviors," type vocabulary includes `spec-gap`, `contract-violation`, `caller-callee-mismatch`). PASS for all.

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| **Result** | PASS | PASS | PASS | PASS | PASS |

---

### C-05 · Single Synthesized Report (12 pts)

All five variations include a UNIFIED FINDINGS REPORT section that collects and integrates findings from all five sub-skills into one table or report structure. None require raw concatenation.

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| **Result** | PASS | PASS | PASS | PASS | PASS |

**Essential total (all variations): 60/60**

---

## Recommended Criteria (30 pts)

### C-06 · Exception Paths and Edge Cases (10 pts)

All variations instruct flow-lifecycle to find missing exit states, undefined phase contracts, and phases with no recovery path; flow-conversation to find dead ends, loops, and ambiguous transitions. V-01's entity manifest makes exception paths more systematic (Entity List 4 requires explicit Exception Path column).

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| **Result** | PASS | PASS | PASS | PASS | PASS |

---

### C-07 · Findings Cross-Reference Source Sub-Skill (10 pts)

All variations include `Sub-skill:` in the finding block schema and `Sub-Skill` as a column in the unified table.

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| **Result** | PASS | PASS | PASS | PASS | PASS |

---

### C-08 · State Machine Anomalies Called Out (10 pts)

All variations instruct trace-state to find: exit-less states, early-firing transitions, unenforced invariants, and unreachable states. V-01/V-04/V-05 also walk a pre-enumerated Entity List 1 of all states, making coverage more complete.

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| **Result** | PASS | PASS | PASS | PASS | PASS |

**Recommended total (all variations): 30/30**

---

## Aspirational Criteria (10 pts)

### C-09 · Test Scenario Baseline Derived from Findings (1 pt)

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| **Result** | PASS | PASS | PASS | PASS | PASS |
| **Evidence** | TEST SCENARIO BASELINE section with 4-column table for CRITICAL/HIGH findings | Same + Type column | Same + Remediation Form column | Same + Severity and Acceptance Condition columns | Same; baseline must contain >= count of CRITICAL/HIGH findings |

---

### C-10 · Finding IDs Assigned F-NN Pattern (1 pt)

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| **Result** | PASS | PASS | PASS | PASS | PASS |
| **Evidence** | F-ID in each finding block + unified table | Same | Same | F-ID as first column in unified 10-column schema | Same |

---

### C-11 · CRITICAL/HIGH Budget per Trace Sub-Skill (1 pt)

V-01, V-02, and V-03 have no severity budget gate — trace sub-skills are instructed to find anomalies but not required to meet a minimum HIGH/CRITICAL floor. V-04 and V-05 introduce an explicit "severity budget: >= 1 CRITICAL or HIGH" per trace sub-skill, with a named SEVERITY BUDGET GATE table that must show all three MET before flow sub-skills run.

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| **Result** | FAIL | FAIL | FAIL | PASS | PASS |
| **Evidence** | No budget gate | No budget gate | No budget gate | Explicit budget per trace sub-skill; gate blocks flow until MET | Same; "campaign halts" if NOT MET without rationale |

---

### C-12 · Structured Findings Table, No Blank Cells (1 pt)

V-01, V-02, V-03: Unified findings table exists with required columns, but no explicit no-blank-cell contract or N/A sentinel instruction — a blank cell could pass undetected.
V-04, V-05: Explicit instruction: "No blank cells. If a field does not apply: 'N/A -- [reason]'." Per-column rules stated.

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| **Result** | PARTIAL | PARTIAL | PARTIAL | PASS | PASS |
| **Evidence** | Table exists; no sentinel instruction | Table exists; no sentinel instruction | Table exists; no sentinel instruction | Explicit N/A sentinel; per-column enforcement | Same + "not blank, not a dash" specification |

---

### C-13 · Flow Findings Reference Trace Context (1 pt)

V-02 and V-03: Use flow-first execution order — flow sub-skills run before trace. Trace Link for flow findings is "N/A -- pre-trace execution" by design. C-13 is structurally impossible in these variations.
V-01: Trace-first ordering means flow runs after trace; Trace Link field present with "F-ID of related trace finding or 'none'." No explicit requirement for at least one non-"none" link. Structural possibility, no mandate.
V-04, V-05: Trace-first + Trace Findings Brief fed into flow sub-skills + explicit mandate: "At least one flow-lifecycle finding must carry a non-'none' Trace Link."

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| **Result** | PARTIAL | FAIL | FAIL | PASS | PASS |
| **Evidence** | Trace-first order + Trace Link field; no mandate | Flow-first: trace runs after flow; links impossible | Flow-first: same structural impossibility | Trace Findings Brief + explicit non-"none" mandate for flow sub-skills | Same mandate; also CROSS-SKILL PATTERNS section reinforces linkage |

---

### C-14 · System Boundary Vocabulary Pre-Assigned (1 pt)

All five variations pre-assign the five vocabulary labels to their owning sub-skills. V-01/V-02/V-03 do this via hardcoded values in per-sub-skill finding schemas. V-04/V-05 consolidate this into the Type Vocabulary Map table with a System Boundary column.

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| **Result** | PASS | PASS | PASS | PASS | PASS |
| **Evidence** | Hardcoded in finding blocks per sub-skill | Type Vocabulary Map includes System Boundary column | Hardcoded in per-sub-skill schemas | Unified vocabulary map; "copy from this table, do not invent alternate labels" | Same; "Both are copy operations, not model judgments" |

---

### C-15 · Universal Sentinel Rule Across All Columns (1 pt)

V-01, V-02, V-03: No universal sentinel rule — optional columns can be left blank.
V-04: "No blank cells. If a field does not apply: 'N/A -- [reason]'" applies to all columns in the unified table. Universal rule.
V-05: Same + enumerated per-column rules make the universal contract explicit for every column by name.

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| **Result** | FAIL | FAIL | FAIL | PASS | PASS |
| **Evidence** | No sentinel rule | No sentinel rule | No sentinel rule | "No blank cells" + "N/A -- [reason]" escape applies table-wide | Same + "not blank, not a dash" + per-column enumeration |

---

### C-16 · No-Findings Sentinel Rows for Clean Sub-Skills (1 pt)

V-01, V-02, V-03: Execution Log records "executed / no findings" status, but no instruction to add a sentinel row to the findings table. An absent sub-skill in the table is indistinguishable from a skip.
V-04, V-05: Explicit instruction: "A sub-skill with no findings must add a sentinel row: Summary = 'No findings detected', Remediation = 'None required -- [reason]', all other cells populated."

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| **Result** | FAIL | FAIL | FAIL | PASS | PASS |
| **Evidence** | Execution log only; no sentinel row instruction | Same | Same | Explicit sentinel row instruction in Execution Log | Same; reinforced in verification checklist |

---

### C-17 · Pre-Output Blank-Cell Verification Gate (1 pt)

V-01, V-02, V-03: No named verification gate with visible PASSED/FAILED outcome.
V-04: Inline parenthetical instruction "[Verify: no blank cells...]" in the Findings Table section — a hint, not a named gate with an output status.
V-05: Explicit 8-item numbered checklist with `**Verification gate**: PASSED ... OR FAILED ...` and "Do not write the unified report until the verification gate shows PASSED."

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| **Result** | FAIL | FAIL | FAIL | FAIL | PASS |
| **Evidence** | No gate | Type Vocabulary Verification exists (different purpose) | Remediation Template Verification exists (different purpose) | Inline hint only; no PASSED/FAILED status label | Explicit 8-check numbered gate with PASSED/FAILED output; execution blocked until PASSED |

---

### C-18 · Unified Schema Closes C-03, C-07, C-10, C-13 Simultaneously (1 pt)

All five variations use a single findings table at synthesis with columns that include F-ID, Sub-Skill, System Boundary, Severity, Blast Radius, Trace Link, and Remediation. No multi-table design; all criteria can be verified in one artifact.

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| **Result** | PASS | PASS | PASS | PASS | PASS |
| **Evidence** | 11-column unified table with Rank prepended | Same 11-column schema | Same | Explicit "FINDINGS TABLE SCHEMA (unified, all sub-skills)" with 10 required columns | Same schema; schema declared at top before execution begins |

---

## Composite Scores

| Criterion | Pts | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-----|------|------|------|------|------|
| C-01 | 12 | 12 | 12 | 12 | 12 | 12 |
| C-02 | 12 | 12 | 12 | 12 | 12 | 12 |
| C-03 | 12 | 12 | 12 | 12 | 12 | 12 |
| C-04 | 12 | 12 | 12 | 12 | 12 | 12 |
| C-05 | 12 | 12 | 12 | 12 | 12 | 12 |
| C-06 | 10 | 10 | 10 | 10 | 10 | 10 |
| C-07 | 10 | 10 | 10 | 10 | 10 | 10 |
| C-08 | 10 | 10 | 10 | 10 | 10 | 10 |
| C-09 | 1 | 1 | 1 | 1 | 1 | 1 |
| C-10 | 1 | 1 | 1 | 1 | 1 | 1 |
| C-11 | 1 | 0 | 0 | 0 | 1 | 1 |
| C-12 | 1 | 0.5 | 0.5 | 0.5 | 1 | 1 |
| C-13 | 1 | 0.5 | 0 | 0 | 1 | 1 |
| C-14 | 1 | 1 | 1 | 1 | 1 | 1 |
| C-15 | 1 | 0 | 0 | 0 | 1 | 1 |
| C-16 | 1 | 0 | 0 | 0 | 1 | 1 |
| C-17 | 1 | 0 | 0 | 0 | 0 | 1 |
| C-18 | 1 | 1 | 1 | 1 | 1 | 1 |
| **TOTAL** | **100** | **95** | **94.5** | **94.5** | **99** | **100** |

---

## Rankings

| Rank | Variation | Score | Delta from #1 | Key Gap |
|------|-----------|-------|--------------|---------|
| 1 | **V-05** | 100 | — | None |
| 2 | **V-04** | 99 | -1 | C-17 only (verification gate is a hint, not a named gate) |
| 3 | **V-01** | 95 | -5 | C-11, C-13 (partial), C-15, C-16, C-17 |
| 4 | **V-02** | 94.5 | -5.5 | C-11, C-13 (structural fail), C-15, C-16, C-17 |
| 4 | **V-03** | 94.5 | -5.5 | C-11, C-13 (structural fail), C-15, C-16, C-17 |

**V-02 vs V-03 tie note**: Both lose C-13 structurally due to flow-first execution order. Both add a specialized verification gate (type vocabulary and remediation template respectively) but neither closes the blank-cell gate (C-17). Equal score is correct.

**V-01 vs V-02/V-03**: V-01 uses trace-first order, allowing C-13 partial credit. V-02/V-03 use flow-first, making C-13 impossible. V-01's single-axis improvement (entity manifest) does more for total score than V-02's or V-03's single-axis improvements because trace-first ordering preserves C-13 eligibility.

---

## Excellence Signals from V-05

V-05 is the maximum-structure variant. Three patterns from the three new R4 axes account for its advantages over all prior rounds:

### Pattern 1: Finding type vocabulary pre-assigned per sub-skill (Type column as copy operation)

R4 V-05 declares a TYPE VOCABULARY MAP with 4–5 allowed type values per sub-skill before execution begins. The Type column instruction is "copy from map for the sub-skill." A finding from trace-permissions must have one of: `privilege-escalation`, `missing-denial`, `cross-role-conflict`, `spec-gap`. Any other value is a finding error.

This closes the same judgment gap that C-14 closed for System Boundary labels: free-text type fields produce inconsistent, meaningless, or hallucinated values (`"issue"`, `"problem"`, `"gap"`) that obscure finding categorization. Pre-assigned vocabulary makes type classification verifiable by inspection. The `spec-gap` escape type prevents the map from straining under genuinely novel findings.

**Rubric impact**: This pattern is not captured by any v3 criterion. It would be a candidate for C-19 in rubric v4: "Type column vocabulary pre-assigned per sub-skill; all Type values in findings table must match the sub-skill's allowed type list."

---

### Pattern 2: Topic entity manifest as pre-execution scope contract

R4 V-05 (and V-01/V-04) introduces a Phase 0 that decomposes the topic into five typed entity lists before any sub-skill fires. Each sub-skill walks its list rather than re-interpreting the raw topic spec. The manifest has a named completeness gate: any empty list is a pre-simulation spec gap, recorded as sentinel finding F-00.

This eliminates interpretation variance at sub-skill setup: five independent sub-skill calls on the same prose can model different states, different boundaries, or different role sets. Pre-extraction in one pass means every sub-skill works from the same ground truth. It also makes coverage auditable: the Execution Log records "Entity List Rows Used" per sub-skill, so reviewers can see whether the state walk covered all extracted states.

**Rubric impact**: This pattern is not captured by any v3 criterion. It would be a candidate for C-20 in rubric v4: "A Topic Entity Manifest is produced in Phase 0 before any sub-skill runs, with completeness gate; each sub-skill cites entity list row count in the Execution Log."

---

### Pattern 3: Remediation template contract with research-item escape

R4 V-05 requires every Remediation cell to match one of two templates:
- **Action form**: `[VERB] [TARGET] AT [LOCATION] TO [SPEC]`
- **Research form**: `INVESTIGATE [specific question] BEFORE specifying remediation`

"Fix the spec", "clarify", "add validation" are named template violations. The pre-output verification checklist explicitly checks "All Remediation entries match action form or research form template."

This closes the last free-text column in the 10-column schema. Combined with C-14 (boundary vocabulary) and the new Type vocabulary, every column now has a mechanical compliance path. The research-item escape is particularly valuable: it surfaces findings that are not yet actionable as a distinct visible category rather than hiding them behind vague prose. A developer reading the findings report can distinguish "act now" (action form) from "investigate first" (research form) without re-reading the sub-skill narrative.

**Rubric impact**: This pattern is not captured by any v3 criterion. It would be a candidate for C-21 in rubric v4: "All Remediation cells match action form (`VERB TARGET AT LOCATION TO SPEC`) or research form (`INVESTIGATE question BEFORE specifying`); findings with neither form are named template violations and must be corrected before output."

---

## All-Essential-Pass Status

All five variations pass C-01 through C-05. All meet the golden threshold condition (all essentials pass AND composite >= 80).

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Finding type vocabulary pre-assigned per sub-skill — Type column closed as copy operation from a named per-sub-skill vocabulary map (parallel to C-14 for System Boundary); type classification is verifiable by inspection; spec-gap escape prevents over-constraint", "Topic entity manifest as pre-execution scope contract — five typed entity lists extracted in Phase 0 before any sub-skill fires; manifest completeness gate surfaces spec gaps before execution; entity list row counts in Execution Log make coverage auditable", "Remediation template contract with research-item escape — every Remediation cell must match VERB+TARGET+AT+LOCATION or INVESTIGATE form; vague entries become named template violations; research form surfaces non-actionable findings as a distinct visible category"]}
```
