## scout-inertia — Round 5 Scorecard

**Rubric**: v5 (18 criteria: 5 essential / 3 recommended / 10 aspirational)
**New in v5**: C-18 per-table column manifest
**Formula**: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/10 * 10)`

---

### Criterion Reference

| ID | Weight | Category |
|----|--------|----------|
| C-01 | essential | Workaround described concretely |
| C-02 | essential | Switching costs quantified |
| C-03 | essential | Inertia threat score = HIGH |
| C-04 | essential | "Why inertia loses" answered |
| C-05 | essential | Workaround failure modes identified |
| C-06 | recommended | Switching cost dimensions treated separately |
| C-07 | recommended | Inertia-loss conditions threshold-based |
| C-08 | recommended | Long-term risk of staying |
| C-09 | aspirational | Failure modes ranked by severity |
| C-10 | aspirational | Steelman rebutted |
| C-11 | aspirational | Loss conditions include verification method |
| C-12 | aspirational | Rebuttal anchored to named claim |
| C-13 | aspirational | Workaround at replication fidelity |
| C-14 | aspirational | Labeled analytical sections |
| C-15 | aspirational | Trigger/impact decomposed |
| C-16 | aspirational | Dedicated Trigger/Impact columns |
| C-17 | aspirational | Synthesis step declares section manifest |
| C-18 | aspirational | Per-table column manifest (NEW in v5) |

---

### V-01 — Phrasing Register (Minimal Inline C-18)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | "Specific tools, manual steps, conventions, scripts, or habits" + "reader must be able to picture the workflow" |
| C-02 | PASS | Three line items with numeric estimates required; adjectives rejected |
| C-03 | PASS | "Assign: HIGH (default and required). Absence = automatic analysis failure." |
| C-04 | PASS | Why Inertia Loses table with ≥2 rows, conditions column required |
| C-05 | PASS | Failure Modes table with ≥2 rows, "Two or more required" |
| C-06 | PASS | Time / Training / Disruption as separate line items |
| C-07 | PASS | Observable Threshold dedicated column in loss table |
| C-08 | PASS | Section 6: "next 6-12 months... specific compounding cost... with a time horizon" |
| C-09 | PASS | Severity column in failure mode table with HIGH/MED/LOW scale |
| C-10 | PASS | Section 7: "strongest possible argument... label it explicitly... rebut it specifically" |
| C-11 | PASS | Verification Command format with `[Tool]: [Action] → [Result]` spec |
| C-12 | **FAIL** | No NAMED CLAIM extraction or word-for-word copy requirement; "rebut it specifically" insufficient to anchor rebuttal to specific claim |
| C-13 | **PARTIAL** | Asks for "specific tools, manual steps" but no requirement to name tools by product (vs. category), no numbered-step enumeration, no institutional knowledge flag |
| C-14 | PASS | Sections 1–7 labeled with descriptive headings; heading manifest declares all 7 |
| C-15 | PASS | "Trigger and Impact are separate columns — do not merge" |
| C-16 | PASS | Table template shows distinct Trigger and Impact column headers |
| C-17 | PASS | "This output must contain the following sections: [7-item list]" before content |
| C-18 | PASS | "Required columns for this table: # \| Condition \| Observable Threshold \| Verification Command" before Why Inertia Loses; "Required columns for this table: # \| Failure Mode \| Trigger \| Impact \| Severity" before Failure Modes |

**Essential**: 5/5 → 60 pts
**Recommended**: 3/3 → 30 pts
**Aspirational**: C-12 FAIL (0), C-13 PARTIAL (0.5), rest PASS (8.5/10) → **8.5 pts**

**V-01 Composite: 98.5 · Gold · All essential pass**

---

### V-02 — Output Format (Schema Block)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | "Name the workaround. Describe the concrete workflow... tools, manual steps, conventions, scripts, or habits. Do not use 'manual processes' without specifics." |
| C-02 | PASS | Table requires numeric ranges; "Significant is not an estimate" |
| C-03 | PASS | Fenced code block `Threat: HIGH` + "Omitting this field fails the analysis" |
| C-04 | PASS | Why Inertia Loses table with falsifiable conditions required |
| C-05 | PASS | Failure Modes table ≥2 rows required |
| C-06 | PASS | Switching Cost Table: Time / Training / Disruption as separate rows |
| C-07 | PASS | Observable Threshold column |
| C-08 | PASS | Section 6: "6-12 months... at least one compounding cost or accumulating risk with a time horizon" |
| C-09 | PASS | Severity column: HIGH / MED / LOW |
| C-10 | PASS | Section 7: "The strongest argument for staying. Then the specific rebuttal." |
| C-11 | PASS | Verification Command format with passing/failing examples |
| C-12 | **FAIL** | Section 7 says "specific rebuttal" but no NAMED CLAIM extraction or word-for-word anchor step; rebuttal can address steelman category rather than the strongest specific claim |
| C-13 | **PARTIAL** | "Describe the concrete workflow... tools, manual steps" — no product-level naming requirement, no numbered steps, no institutional knowledge flag |
| C-14 | PASS | Sections 1–7 under "### Required Output Structure" with descriptive labels |
| C-15 | PASS | "Trigger and Impact are separate columns — do not merge into a single cell" |
| C-16 | PASS | Schema block shows Trigger and Impact as separate column headers |
| C-17 | PASS | "### Required Output Structure" lists Sections 1–7 before any content |
| C-18 | PASS | `> Schema: # \| Condition \| Observable Threshold \| Verification Command` before Section 4; `> Schema: # \| Failure Mode \| Trigger \| Impact \| Severity` before Section 5; block format visually separates declaration from table header |

**Essential**: 5/5 → 60 pts
**Recommended**: 3/3 → 30 pts
**Aspirational**: C-12 FAIL (0), C-13 PARTIAL (0.5), rest PASS (8.5/10) → **8.5 pts**

**V-02 Composite: 98.5 · Gold · All essential pass**

---

### V-03 — Role Sequence (Procedural Column Manifests)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | ROLE 1 Step 1: "Name it. Describe the exact workflow: tools, commands, conventions, manual steps." |
| C-02 | PASS | ROLE 2 Step 2: "Numbers or ranges required. Do not use adjectives alone." |
| C-03 | PASS | ROLE 2 Step 1: "Inertia threat is HIGH by default. Only downgrade with written justification. State the score explicitly." |
| C-04 | PASS | ROLE 2 Step 4: inertia-loss table with ≥2 rows and conditions required |
| C-05 | PASS | ROLE 2 Step 3: failure mode table with ≥2 rows required |
| C-06 | PASS | Three dimensions (Time / Training / Disruption) in Step 2 |
| C-07 | PASS | Observable Threshold column in Step 4 table |
| C-08 | PASS | ROLE 2 Step 5: "What happens in 6-12 months for teams that stay?" |
| C-09 | PASS | Severity column; "Rank by severity" instruction |
| C-10 | PASS | ROLE 1 produces steelman; ROLE 2 Step 6 rebuts it |
| C-11 | PASS | Verification Command format in Step 4 with `[Tool: Action → Result]` spec |
| C-12 | PASS | Step 6a: "Copy the STRONGEST CLAIM from the Advocate Brief word-for-word. Label it: NAMED CLAIM: '[exact text from Advocate Brief]'" + "do not address a weaker point instead" |
| C-13 | **PARTIAL** | "Be specific enough that someone else could follow the same process" implies replication fidelity but no explicit product-naming requirement, no numbered steps enumeration, no institutional knowledge flag |
| C-14 | PASS | Role structure produces labeled ADVOCATE BRIEF + ANALYST VERDICT with labeled sub-sections; synthesis preserves section labels; ≥5 descriptive headings guaranteed by role template |
| C-15 | PASS | "Trigger and Impact are separate columns" |
| C-16 | PASS | Distinct Trigger and Impact columns in Step 3 table |
| C-17 | **FAIL** | No section heading manifest in synthesis step; "Synthesize both outputs into the final artifact" declares no explicit list of required section headings before content begins |
| C-18 | PASS | Step 3: "Before writing the table, write this line: Required columns for this table: # \| Failure Mode \| Trigger \| Impact \| Severity"; Step 4: same mechanism for loss table — procedural generation reliably produces pre-commitment |

**Essential**: 5/5 → 60 pts
**Recommended**: 3/3 → 30 pts
**Aspirational**: C-13 PARTIAL (0.5), C-17 FAIL (0), rest PASS (8.5/10) → **8.5 pts**

**V-03 Composite: 98.5 · Gold · All essential pass**

*Note: C-17 is structurally absent from the synthesis step. The rubric notes indicate R4 V-03 proved C-17 is a synthesis-step constraint orthogonal to role structure — but the R5 V-03 synthesis step ("Synthesize both outputs into the final artifact") carries no manifest. This is a carry-forward gap from the axis isolation; V-03 picks up C-12 (NAMED CLAIM) but loses C-17.*

---

### V-04 — Combined: Lifecycle + Output Format

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | "Name the workaround. Describe it concretely: tools, manual steps, conventions, scripts, habits." + "Fail condition: 'teams use manual processes' with no specifics." |
| C-02 | PASS | Three dimensions with "numeric estimate or explicit N/A"; adjective-only fail condition |
| C-03 | PASS | "Threat score: HIGH. Required. Do not omit." |
| C-04 | PASS | Phase 4A: Why Inertia Loses table, ≥2 rows |
| C-05 | PASS | Phase 3: Failure Mode table, ≥2 rows |
| C-06 | PASS | Time / Training / Disruption as separate Phase 2 items |
| C-07 | PASS | Observable Threshold column in Phase 4A |
| C-08 | PASS | Phase 4C: "What accumulates over 6-12 months... specific compounding cost or divergence risk with a time horizon." |
| C-09 | PASS | Severity column with HIGH/MED/LOW definition |
| C-10 | PASS | Phase 4B: Steelman and Anchored Rebuttal, three-step sequence |
| C-11 | PASS | Verification Command format with `[Tool]: [Action] → [Result]` and fail conditions |
| C-12 | PASS | Phase 4B Step 2: "Extract the single strongest specific claim... Label it: NAMED CLAIM: '[exact text]'" + "Rebut only that named claim" |
| C-13 | **PARTIAL** | Phase 1: "Name the workaround. Describe it concretely: tools, manual steps, conventions, scripts, habits." No product-level naming requirement, no numbered step enumeration, no institutional knowledge flag |
| C-14 | PASS | 6 labeled phases (Phase 1, 2, 3, 4A, 4B, 4C) with descriptive names |
| C-15 | PASS | "Trigger and Impact are separate columns — do not merge." |
| C-16 | PASS | Dedicated Trigger / Impact columns in Phase 3 table |
| C-17 | PASS | "This output must contain the following sections: Phase 1… Phase 4C" declared before phases begin |
| C-18 | PASS | "Required columns for this table: # \| Failure Mode \| Trigger \| Impact \| Severity" at top of Phase 3; "Required columns for this table: # \| Condition \| Observable Threshold \| Verification Command" at top of Phase 4A |

**Essential**: 5/5 → 60 pts
**Recommended**: 3/3 → 30 pts
**Aspirational**: C-13 PARTIAL (0.5), rest PASS (9.5/10) → **9.5 pts**

**V-04 Composite: 99.5 · Gold · All essential pass**

---

### V-05 — All Axes Combined

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | STEP 1 Workaround Profile: "Describe the workaround so that another team with no prior context could reproduce it independently" |
| C-02 | PASS | Switching Cost Table: "Numeric or range-based estimates required. 'Significant' is not an estimate." |
| C-03 | PASS | Section B fenced block `Inertia Threat: HIGH` + "Omitting this field = analysis failure" |
| C-04 | PASS | Section D: Why Inertia Loses table, ≥2 rows, each condition must be falsifiable |
| C-05 | PASS | Section C: Workaround Failure Mode Table, ≥2 rows, specific failure required |
| C-06 | PASS | Three rows (Time / Training / Disruption) with separate Estimate and What Drives This columns |
| C-07 | PASS | Observable Threshold column in Section D |
| C-08 | PASS | Section E: "What accumulates over 6-12 months... specific compounding cost, growing debt, or divergence risk with a time horizon." |
| C-09 | PASS | Severity column in Section C; HIGH/MED/LOW required; "Does not scale without a scale limit does not pass." |
| C-10 | PASS | Section F: three-step Anchored Rebuttal sequence |
| C-11 | PASS | Verification Command format with passing and failing examples explicitly contrasted |
| C-12 | PASS | Section F Step 1: "Copy the STRONGEST CLAIM from the Advocate Pass word-for-word. Label it: NAMED CLAIM: '[exact text from Advocate Pass]'" + "Constraint: do not redirect to a different benefit. The rebuttal must be traceable to the named claim." |
| C-13 | **PASS** | Replication Fidelity Standard with three operationalized requirements: (1) "Name each tool by product, not by category. 'GitHub Actions' not 'CI system.'" (2) "Enumerate the major steps in numbered sequence." (3) "Flag institutional knowledge: any step requiring tribal context, undocumented conventions, or shared credentials." |
| C-14 | PASS | 7 labeled sections (WORKAROUND PROFILE, A–F) with descriptive labels |
| C-15 | PASS | "Trigger and Impact are separate columns — do not merge." |
| C-16 | PASS | Dedicated Trigger / Impact columns in Section C table |
| C-17 | PASS | "This output must contain the following sections: WORKAROUND PROFILE… F. Anchored Rebuttal" declared before STEP 1 begins |
| C-18 | PASS | "Required columns for this table: # \| Failure Mode \| Trigger \| Impact \| Severity" immediately before Section C; "Required columns for this table: # \| Condition \| Observable Threshold \| Verification Command" immediately before Section D — both table sites covered |

**Essential**: 5/5 → 60 pts
**Recommended**: 3/3 → 30 pts
**Aspirational**: 10/10 → **10 pts**

**V-05 Composite: 100 · Gold · All essential pass**

---

### Summary Scorecard

| Variation | Essential | Recommended | Aspirational | Composite | Band | C-12 | C-13 | C-17 | C-18 |
|-----------|-----------|-------------|--------------|-----------|------|------|------|------|------|
| V-01 | 5/5 | 3/3 | 8.5/10 | **98.5** | Gold | FAIL | PARTIAL | PASS | PASS |
| V-02 | 5/5 | 3/3 | 8.5/10 | **98.5** | Gold | FAIL | PARTIAL | PASS | PASS |
| V-03 | 5/5 | 3/3 | 8.5/10 | **98.5** | Gold | PASS | PARTIAL | **FAIL** | PASS |
| V-04 | 5/5 | 3/3 | 9.5/10 | **99.5** | Gold | PASS | PARTIAL | PASS | PASS |
| V-05 | 5/5 | 3/3 | 10/10 | **100** | Gold | PASS | **PASS** | PASS | PASS |

**Rank**: V-05 > V-04 > V-01 = V-02 = V-03

---

### Findings Against Predicted Scores

The variation document predicted all-100 for R5. Three deviations found:

1. **V-01, V-02: C-12 FAIL** — "Rebut it specifically" / "The specific rebuttal" does not reliably produce a NAMED CLAIM anchor. The rebuttal can address the steelman category rather than a single extracted claim. Fixing either: add "Extract the strongest specific claim. Label it: NAMED CLAIM: '...'. Rebut only that claim."

2. **V-03: C-17 FAIL** — The synthesis step ("Synthesize both outputs into the final artifact") carries no section heading manifest. R4 V-03 demonstrated that C-17 is a synthesis-step constraint independent of role structure — but R5 V-03 omits the manifest from the synthesis step. One addition fixes it: a "This output must contain the following sections:" list before the synthesis instruction.

3. **V-01 through V-04: C-13 PARTIAL** — All four single-axis and pair-axis variations ask for "specific tools" or "concrete detail" but none operationalize replication fidelity the way V-05 does. V-05's Replication Fidelity Standard explicitly requires product-level tool names, numbered steps, and institutional knowledge flagging — the three sub-requirements that make the workaround reproducible by a new team.

---

### Excellence Signals (V-05)

**Signal 1 — Replication Fidelity Standard as a named, operationalized sub-protocol**
V-05 is the only variation that converts C-13 from PARTIAL to PASS. The mechanism: naming the sub-protocol ("Replication Fidelity Standard"), then providing three numbered, independently checkable requirements with counter-examples inline ("GitHub Actions" not "CI system"). The named standard pattern makes the requirement memorable, the inline counter-examples make it enforceable. Variations that ask for "specifics" without operationalizing what specificity means produce PARTIAL results.

**Signal 2 — Triple-layer structural enforcement stack fully assembled**
V-05 is the only variation where C-16, C-17, and C-18 all PASS together. C-16 ensures dedicated Trigger/Impact columns exist. C-17 pre-commits to section headings globally before content begins. C-18 pre-commits to column structure locally at each table site. Each layer catches a different class of omission without reading cell content. The three layers are pairwise independent — V-03 passes C-16 and C-18 but fails C-17; V-01/V-02 pass C-16, C-17, and C-18 but fail C-12. Only V-05 assembles all three simultaneously.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Replication Fidelity Standard as a named sub-protocol with three operationalized requirements (product-level tool naming, numbered steps, institutional knowledge flag) converts C-13 from PARTIAL to PASS — present only in V-05", "Triple-layer structural enforcement stack (C-16 dedicated columns + C-17 global section manifest + C-18 per-table column manifests) fully assembled only in V-05 — each layer independently detectable without reading cell content"]}
```
