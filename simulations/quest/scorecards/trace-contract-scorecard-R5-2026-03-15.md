## trace-contract Round 5 — Scoring Report

### Rubric v5 Criteria Reference

| ID | Tier | Category | Key Pass Condition |
|----|------|----------|--------------------|
| C-01 | Essential | integrity | Expected before actual |
| C-02 | Essential | correctness | Explicit diff (before/after per element) |
| C-03 | Essential | correctness | Severity label per finding |
| C-04 | Essential | depth | Root cause hypothesis per finding |
| C-05 | Essential | coverage | Spec reference per finding |
| C-06 | Recommended | depth | Integration-level impact callout (at-least-one) |
| C-07 | Recommended | format | Summary verdict with severity counts + PASS/FAIL |
| C-08 | Recommended | behavior | Affirmative confirmation when no findings |
| C-09 | Aspirational | depth | Amendment suggestion for every breaking finding |
| C-10 | Aspirational | coverage | Pattern recognition when N findings ≥ 2 |
| C-11 | Aspirational | format | Structural template (missing field = visible gap) |
| C-12 | Aspirational | behavior | Explicit phase-gate checkpoint |
| C-13 | Aspirational | behavior | Machine-readable gate token `[EXPECTED SEALED]` |
| C-14 | Aspirational | depth | connector-impact slot in **every** finding block (not at-least-one) |
| C-15 | Aspirational | depth | recommended-action as pre-printed slot in breaking template |
| C-16 | Aspirational | format | Three distinct templates, one per severity tier, no conditional fields |
| C-17 | Aspirational | depth | recommended-action = vocabulary choice + rationale sentence (both required) |
| C-18 | Aspirational | behavior | Full token contract: placement + non-substitutability + verification |
| C-19 | Aspirational | behavior | Token contract in named preamble section **before Phase 1** |

---

## V-01 — Preamble-First Behavioral Protocol

**Structural signature:** `## Behavioral Contract` before Phase 1 → unified single finding template → breaking gets conditional sixth field.

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | Phase 1 writes Expected from spec; Phase 2 role begins "after `[EXPECTED SEALED]`" |
| C-02 | PASS | Phase 3 enumerates every element as `check` or `F-NN` |
| C-03 | PASS | Template: `severity: [exactly one of: breaking \| degraded \| cosmetic]` |
| C-04 | PASS | Template: `hypothesis: [one sentence naming the causal mechanism]` |
| C-05 | PASS | Template: `spec: [clause identifier — must match a cited clause; no paraphrase]` |
| C-06 | PASS | `connector-impact:` slot in unified template → present on all findings |
| C-07 | PASS | Phase 5 Summary: counts + "Contract violated / Contract satisfied" |
| C-08 | PASS | "If no deviations: write `## Diff — Contract satisfied.`" |
| C-09 | PASS | "For every `breaking` finding, add a sixth field: `recommended-action`" includes vocabulary + rationale |
| C-10 | PASS | Phase 5 Pattern note: "If two or more findings share a root cause… `Pattern: F-NN and F-MM share [mechanism] — single fix resolves both`" |
| C-11 | PASS | Template block with labeled fields; missing field is a visible gap |
| C-12 | PASS | "Do not run the operation before this section is complete" + gate token instruction |
| C-13 | PASS | Exact string `[EXPECTED SEALED]` specified |
| C-14 | PASS | `connector-impact:` in the unified template → structurally present on all findings |
| C-15 | **FAIL** | `recommended-action` is instructional ("add a sixth field") not a pre-printed slot; the template as shown has five fields — the sixth must be added by instruction, not revealed as visibly empty when missing |
| C-16 | **FAIL** | Single unified template; C-16 requires three distinct templates one per severity tier |
| C-17 | PASS | `recommended-action: [amend-spec \| fix-impl \| needs-discussion] — [one sentence rationale: which side of the contract is wrong and why]` — both parts present |
| C-18 | PASS | Behavioral Contract section states placement rule, non-substitutability (with five negative examples), and verification mechanism |
| C-19 | PASS | `## Behavioral Contract` appears before any `### ROLE:` heading and before Phase 1 instructions |

**Essential:** 5/5 (60 pts) | **Recommended:** 3/3 (30 pts) | **Aspirational:** 9/11 (9 pts)
**Composite: 99** | Golden: yes

---

## V-02 — Severity-Stratified Templates

**Structural signature:** No Behavioral Contract preamble → `[EXPECTED SEALED]` inline instruction only → three distinct templates (Breaking 6-slot / Degraded 5-slot / Cosmetic 4-slot).

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | "Write `## Expected Output`… Do not run the operation before completing this section" |
| C-02 | PASS | Step 4 Diff: check or F-NN per element |
| C-03 | PASS | Severity hard-coded per template tier |
| C-04 | PASS | `hypothesis:` in all three templates |
| C-05 | PASS | `spec:` in all three templates |
| C-06 | PASS | Breaking and Degraded templates include `connector-impact:` → at-least-one satisfied |
| C-07 | PASS | Step 6 Summary block with counts + Verdict |
| C-08 | PASS | "If no deviations: write `## Diff — Contract satisfied.` and enumerate all elements as `check satisfied`" |
| C-09 | PASS | Breaking template has `recommended-action:` as labeled slot |
| C-10 | **FAIL** | No pattern note in V-02 Summary block |
| C-11 | PASS | Three separate template blocks; missing slot is visually empty |
| C-12 | PASS | "Do not run the operation before completing this section. When done, write: `[EXPECTED SEALED]`" |
| C-13 | PASS | Token `[EXPECTED SEALED]` specified |
| C-14 | **FAIL** | Cosmetic template has no `connector-impact:` slot — four fields: deviation, severity, spec, hypothesis only |
| C-15 | PASS | Breaking template pre-prints `recommended-action:` as a required labeled slot; "All six slots are required. A breaking finding with any slot unfilled is incomplete." |
| C-16 | PASS | Three distinct templates, one per tier; all fields within each template unconditionally required; no conditional language |
| C-17 | PASS | Breaking template: `recommended-action: [amend-spec \| fix-impl \| needs-discussion] — [one sentence rationale: which side of the contract is wrong and why]` |
| C-18 | **FAIL** | No Behavioral Contract section; token mentioned only as "when done, write `[EXPECTED SEALED]`" — placement, non-substitutability, and verification mechanism are absent |
| C-19 | **FAIL** | No named preamble section containing token contract before Phase 1 |

**Essential:** 5/5 (60 pts) | **Recommended:** 3/3 (30 pts) | **Aspirational:** 7/11 (7 pts)
**Composite: 97** | Golden: yes

---

## V-03 — Integration-First, Collaborative Frame

**Structural signature:** `## Integration Lens` preamble (no token contract) → single unified template with connector-impact for all findings → breaking gets instructional add-on.

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | "Write `## Expected Output` from the spec alone… Do not run the operation before this section is complete" |
| C-02 | PASS | Phase 4 Diff: check or F-NN per element |
| C-03 | PASS | `severity: [breaking \| degraded \| cosmetic]` in unified template |
| C-04 | PASS | `hypothesis:` in template |
| C-05 | PASS | `spec:` in template |
| C-06 | PASS | `connector-impact:` in unified template → at-least-one satisfied; framing amplifies it |
| C-07 | PASS | Phase 6 Summary: counts + verdict |
| C-08 | PASS | "If nothing deviates: write `## Diff — Contract satisfied.` and list every element as `check satisfied`" |
| C-09 | PASS | "For every `breaking` finding, add a recommendation: `recommended-action: [vocabulary] — [one sentence]`" |
| C-10 | PASS | Phase 6 Summary: "If two or more findings share a root cause: `Pattern: F-NN and F-MM share [mechanism] — single fix resolves both`" |
| C-11 | PASS | Template block with labeled fields |
| C-12 | PASS | "Do not run the operation before this section is complete. When done, write: `[EXPECTED SEALED]`" |
| C-13 | PASS | Token `[EXPECTED SEALED]` specified |
| C-14 | PASS | `connector-impact:` in unified template → structurally present on every finding block; Integration Lens reinforces substance |
| C-15 | **FAIL** | `recommended-action` is instructional ("add a recommendation") — no pre-printed slot in a breaking-specific template; a breaking finding can be written without the recommendation being visibly absent |
| C-16 | **FAIL** | Single unified template |
| C-17 | PASS | `recommended-action: [vocabulary] — [one sentence: which side is wrong and why]` — vocabulary + rationale both present |
| C-18 | **FAIL** | No Behavioral Contract section; `## Integration Lens` preamble describes the audience frame, not the token contract; placement, non-substitutability, and verification are absent |
| C-19 | **FAIL** | `## Integration Lens` does not contain the gate token behavioral rules; C-19 requires the token contract specifically to appear in the preamble |

**Essential:** 5/5 (60 pts) | **Recommended:** 3/3 (30 pts) | **Aspirational:** 7/11 (7 pts)
**Composite: 97** | Golden: yes

---

## V-04 — Preamble + Stratified + Rationale-Anchored

**Structural signature:** `## Behavioral Contract` before Phase 1 → three severity-stratified templates → breaking template has `recommended-action` slot with rationale constraint.

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | Phase 1 writes Expected from spec; gate seals before Phase 2 begins |
| C-02 | PASS | Phase 3 Diff enumerates every element |
| C-03 | PASS | Severity hard-coded in each template |
| C-04 | PASS | `hypothesis:` in all three templates |
| C-05 | PASS | `spec:` in all three templates |
| C-06 | PASS | Breaking and Degraded templates include `connector-impact:` |
| C-07 | PASS | Phase 5 Summary with counts + verdict |
| C-08 | PASS | "If no deviations: write `## Diff — Contract satisfied.` and enumerate each element as `check satisfied`" |
| C-09 | PASS | Breaking template has `recommended-action:` as required slot |
| C-10 | PASS | Phase 5 Pattern note: "If two or more findings share a root cause: `Pattern: F-NN and F-MM — [mechanism] — single fix resolves both`" |
| C-11 | PASS | Three template blocks; any missing slot is visibly empty |
| C-12 | PASS | Gate instruction in Phase 1 Step 2: "write on its own line: `[EXPECTED SEALED]`"; role boundary enforces the gate |
| C-13 | PASS | Token `[EXPECTED SEALED]` specified |
| C-14 | **FAIL** | Cosmetic template has four fields (deviation, severity, spec, hypothesis) — no `connector-impact:` slot; C-14 requires every finding block, not just Breaking and Degraded |
| C-15 | PASS | Breaking template pre-prints `recommended-action:` as a labeled slot; "All six slots are unconditionally required" |
| C-16 | PASS | Three distinct templates, one per tier; all fields within each template unconditionally required |
| C-17 | PASS | Breaking template: `recommended-action: [vocabulary] — [one sentence rationale identifying which side of the contract is wrong and why, grounded in the hypothesis above]`; "A vocabulary choice without a rationale sentence does not complete this slot" |
| C-18 | PASS | `## Behavioral Contract` specifies placement rule, non-substitutability (examples of invalid variants), and verification mechanism |
| C-19 | PASS | `## Behavioral Contract` appears before `### ROLE: Connectors Contract Expert` and before any Phase 1 instructions |

**Essential:** 5/5 (60 pts) | **Recommended:** 3/3 (30 pts) | **Aspirational:** 10/11 (10 pts)
**Composite: 100** | Golden: yes

---

## V-05 — All Axes Full Synthesis

**Structural signature:** `## Behavioral Contract` + `## Integration Lens` both before Phase 1 → three stratified templates → inertia framing at each phase boundary → pattern analysis with mandatory "no patterns" affirmation.

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | Phase 1 writes Expected from spec; inertia framing underscores why |
| C-02 | PASS | Phase 3 Diff: `check` or `F-NN` per element; "silent gap" warning reinforced |
| C-03 | PASS | Severity hard-coded per template tier |
| C-04 | PASS | `hypothesis:` in all three templates |
| C-05 | PASS | `spec:` in all three templates |
| C-06 | PASS | Breaking and Degraded templates include `connector-impact:` |
| C-07 | PASS | Phase 5 Summary block with counts + verdict |
| C-08 | PASS | "If no deviations: write `## Diff — Contract satisfied.` and enumerate each element as `check satisfied`" |
| C-09 | PASS | Breaking template has `recommended-action:` as required slot |
| C-10 | PASS | Phase 5: "**Pattern analysis:** If two or more findings share a root cause… If no pattern exists: `No patterns detected — findings have independent root causes`" — mandatory affirmation both ways |
| C-11 | PASS | Three template blocks; missing field is a visible gap |
| C-12 | PASS | Gate token instruction in Phase 1 Step 2; Behavioral Contract governs |
| C-13 | PASS | Token `[EXPECTED SEALED]` specified |
| C-14 | **FAIL** | Cosmetic template: deviation, severity, spec, hypothesis — no `connector-impact:` slot; Integration Lens framing provides integration-awareness prose but does not structurally enforce the slot |
| C-15 | PASS | Breaking template pre-prints `recommended-action:` as unconditionally required slot |
| C-16 | PASS | Three distinct templates, unconditionally required fields per tier |
| C-17 | PASS | Breaking template: vocabulary choice + "rationale sentence grounded in the hypothesis above" — both enforced in the slot description |
| C-18 | PASS | `## Behavioral Contract` states placement rule, non-substitutability (with examples), and verification mechanism |
| C-19 | PASS | `## Behavioral Contract` and `## Integration Lens` both appear before `### ROLE: Connectors Contract Expert` and before Phase 1 |

**Essential:** 5/5 (60 pts) | **Recommended:** 3/3 (30 pts) | **Aspirational:** 10/11 (10 pts)
**Composite: 100** | Golden: yes

---

## Variation Ranking

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Fails |
|------|-----------|-----------|-------------|--------------|-----------|-------|
| 1 (tie) | V-04 | 5/5 | 3/3 | 10/11 | **100** | C-14 |
| 1 (tie) | V-05 | 5/5 | 3/3 | 10/11 | **100** | C-14 |
| 3 | V-01 | 5/5 | 3/3 | 9/11 | **99** | C-15, C-16 |
| 4 (tie) | V-02 | 5/5 | 3/3 | 7/11 | **97** | C-10, C-14, C-18, C-19 |
| 4 (tie) | V-03 | 5/5 | 3/3 | 7/11 | **97** | C-15, C-16, C-18, C-19 |

All five variations are golden (≥ 80 + all essential pass).

---

## Excellence Signals from Top-Scoring Variations (V-04 / V-05)

**Signal 1 — Preamble-first is a structural fix, not a content fix.**
V-01 through R4 already contained complete token contracts (C-18 satisfying content). The single change in V-04/V-05 that earned C-19 was document placement: moving the `## Behavioral Contract` section to appear before any `### ROLE:` heading. The model reads behavioral rules before phase instructions begin — no paraphrase, no re-statement, just a named section at the top.

**Signal 2 — Stratified templates eliminate the conditional field problem.**
The R4 breaking-finding template had `recommended-action` marked "required if breaking" — conditional language embedded in a unified template. That conditional is exactly what fails C-16. Three distinct templates, one per tier, each with only unconditionally required fields, resolve C-15 and C-16 together: the breaking template always has `recommended-action` because it is a pre-printed slot; you cannot complete the template without filling it.

**Signal 3 — The C-14 / C-16 structural tradeoff is now fully diagnosed.**
Unified template → `connector-impact:` on every finding (C-14 passes) but requires conditional fields (C-15, C-16 fail). Stratified templates → unconditional fields per tier (C-15, C-16 pass) but cosmetic tier systematically omits `connector-impact:` (C-14 fails). The R6 synthesis target: stratified templates where **all three** templates include `connector-impact:` — even the cosmetic template, which would carry a constrained affirmation like `connector-impact: none — cosmetic only; no integration behavior affected`. This resolves C-14 without reintroducing conditional field logic.

**Signal 4 — Mandatory pattern affirmation is better than conditional pattern note.**
V-05's Phase 5 requires either a grouping statement OR `No patterns detected — findings have independent root causes.` Forcing the author to write one or the other prevents silent omission. V-04's pattern note ("if two or more…") is also sufficient for C-10, but V-05's unconditional form is more robust as a forcing function.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Stratified templates create a C-14/C-16 tradeoff: unified template passes C-14 (connector-impact on all findings) but fails C-15/C-16 (conditional fields); stratified templates pass C-15/C-16 but cosmetic tier systematically omits connector-impact, failing C-14 — R6 target is connector-impact in all three templates", "Mandatory pattern affirmation (one of two required statements) prevents silent C-10 omission better than a conditional pattern note"]}
```
