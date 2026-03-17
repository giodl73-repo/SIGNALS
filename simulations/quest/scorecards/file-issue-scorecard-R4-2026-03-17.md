## file-issue — Round 4 Scorecard

**Rubric**: v4 (C-01 through C-15)
**Date**: 2026-03-17
**Variations scored**: V-01 through V-05

---

### V-01 — Role Sequence: Severity-First Isolation

#### Essential (60%)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Required fields captured | PASS | Step 1 collects severity alone; Step 2 forms collect skill/expected/actual per severity. All four fields required. |
| C-02 | Severity vocabulary enforcement | PASS | Four-value enum only. Explicit rejection: "Not a valid severity. Choose from: crash, wrong-output, missing-feature, improvement." |
| C-03 | GitHub issue format | PASS | Four templates with `[{severity}] {skill}: {description}` title pattern plus Expected / Actual / Steps / Context sections. |
| C-04 | Artifact path | PASS | `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md` — unambiguous. |

Essential: **4/4 → 60**

#### Recommended (30%)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-05 | Actionable, specific title | PASS | Templates specify `[wrong-output] {skill}: {section} — expected {X}, got {Y}` etc. Skill name + symptom required. |
| C-06 | Sufficient reproducibility context | PASS | Step 4 gate row: "Invocation, input, topic, or event sequence in body." Forms also prompt for invocation, topic, chain. |
| C-07 | Repo open offer presented | PASS | OFFER block includes `gh issue create --title ... --label "{severity}" --body-file ...` |

Recommended: **3/3 → 30**

#### Aspirational (10%)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-08 | Severity-appropriate framing | PASS | crash: "Priority: HIGH — skill non-functional" + Impact field. improvement: Acceptance condition + Rationale fields. Gate checks tone match. |
| C-09 | Skill context enrichment | PASS | Forms collect topic, invocation, chain, version/date. Gate row: "At least one item beyond the 4 required fields present." |
| C-10 | Pre-write validation gate | PASS | Step 4 PRE-WRITE GATE — 6-row check table, separate from drafting. "Do not write the artifact until every row shows PASS." Blocks write step. |
| C-11 | Corrective actions per validation check | PASS | Each gate row has explicit "Correction on fail" column: "Ask user for the missing field(s) by name", "Rewrite: …", "Add Topic + Invocation", etc. |
| C-12 | Per-severity body templates | PASS | Four distinct templates structurally differentiated: crash has Priority/Impact; improvement has Acceptance condition/Rationale. Template selection determines structure. |
| C-13 | Severity-labeled issue creation | PASS | `--label "{severity}"` in OFFER command. |
| C-14 | Severity-first field sequencing | **PASS** | Step 1 is severity alone — one question, no other fields. "Do not collect any other field until a valid severity value is confirmed." Severity then loads the matching form (Step 2) and output template (Step 3). Strongest single-step isolation implementation. |
| C-15 | Macro-phase hard boundary | **FAIL** | Five sequential steps (1–5), not two named macro-phases. No "DO NOT BEGIN PHASE X UNTIL PHASE Y IS COMPLETE" instruction. The step structure does not qualify — the gate must be a phase transition. |

Aspirational: **7/8 → 8.75**

**V-01 Composite: 60 + 30 + 8.75 = 98.75** | Golden

---

### V-02 — Lifecycle Emphasis: Symmetric Macro-Phase

#### Essential (60%)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Required fields captured | PASS | A1 asks for Skill, Expected, Actual, Severity — all four. |
| C-02 | Severity vocabulary enforcement | PASS | "must be exactly one of the four values… reject it and re-prompt." |
| C-03 | GitHub issue format | PASS | Four templates in A2 with title pattern and structured sections. |
| C-04 | Artifact path | PASS | `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md` |

Essential: **4/4 → 60**

#### Recommended (30%)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-05 | Actionable, specific title | PASS | Per-severity title patterns require skill name + symptom. |
| C-06 | Sufficient reproducibility context | PASS | B1 validates reproducibility; A1 collects invocation, topic, chain. |
| C-07 | Repo open offer presented | PASS | B3 OFFER with `gh issue create --label "{severity}"`. |

Recommended: **3/3 → 30**

#### Aspirational (10%)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-08 | Severity-appropriate framing | PASS | crash: Priority HIGH; improvement: Acceptance condition + Rationale. B1 checks "Tone matches template." |
| C-09 | Skill context enrichment | PASS | A1 collects topic, invocation, chain, version/date. B1 checks "Context enriched." |
| C-10 | Pre-write validation gate | PASS | B1 VALIDATE is a named phase with "Do not begin B2 until all rows pass." The gate is within a phase, blocking the write sub-operation. |
| C-11 | Corrective actions per validation check | PASS | B1 table has "Correction on fail" column with explicit remedies. |
| C-12 | Per-severity body templates | PASS | Four distinct templates in A2 with severity-differentiated structure. |
| C-13 | Severity-labeled issue creation | PASS | `--label "{severity}"` in B3 OFFER. |
| C-14 | Severity-first field sequencing | **FAIL** | A1 asks for all four fields together: "Ask the user for all four required fields" — Skill, Expected, Actual, Severity listed in that order. Severity is fourth. No explicit severity-first sequencing statement. |
| C-15 | Macro-phase hard boundary | **PASS** | Two named macro-phases: PHASE A (A1: collect + A2: draft) and PHASE B (B1: validate + B2: write + B3: offer). Explicit instruction: "DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE." Completion condition defined. |

Aspirational: **7/8 → 8.75**

**V-02 Composite: 60 + 30 + 8.75 = 98.75** | Golden

---

### V-03 — Output Format: Table-Driven Collection

#### Essential (60%)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Required fields captured | PASS | Intake table marks Skill, Severity, Expected, Actual as required. |
| C-02 | Severity vocabulary enforcement | PASS | "Severity must be exactly one of the four values... Reject any other value and re-prompt before accepting other fields." |
| C-03 | GitHub issue format | PASS | Four templates with proper title pattern and structured sections. |
| C-04 | Artifact path | PASS | `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md` |

Essential: **4/4 → 60**

#### Recommended (30%)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-05 | Actionable, specific title | PASS | Per-severity title patterns. |
| C-06 | Sufficient reproducibility context | PASS | PRE-WRITE GATE checks reproducibility. Table includes invocation, topic, related skill. |
| C-07 | Repo open offer presented | PASS | OFFER with `gh issue create --label "{severity}"`. |

Recommended: **3/3 → 30**

#### Aspirational (10%)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-08 | Severity-appropriate framing | PASS | crash: Priority HIGH; improvement: Acceptance condition. Gate checks tone match. |
| C-09 | Skill context enrichment | PASS | Table has topic, invocation, related skill/rubric ref, version/date as recommended fields. Gate checks context enrichment. |
| C-10 | Pre-write validation gate | PASS | PRE-WRITE GATE — 6-row structured check, "Do not write the artifact until every row shows PASS." Separate from DRAFT step. |
| C-11 | Corrective actions per validation check | PASS | Gate table has "Correction on fail" column with explicit corrective actions per row. |
| C-12 | Per-severity body templates | PASS | Four distinct templates with severity-differentiated structure (crash/improvement structurally different). |
| C-13 | Severity-labeled issue creation | PASS | `--label "{severity}"` in OFFER. |
| C-14 | Severity-first field sequencing | **FAIL** | Intake table presents all fields simultaneously — Skill, Severity, Expected, Actual in same table. Severity is not the first field collected; all are collected together. "Reject and re-prompt before accepting other fields" is rejection behavior on invalid input, not severity-first sequencing. |
| C-15 | Macro-phase hard boundary | **FAIL** | No named macro-phases. Structure is: INTAKE → DRAFT → PRE-WRITE GATE → WRITE → OFFER. Sequential steps, not two macro-phases with a cross-phase blocking instruction. |

Aspirational: **6/8 → 7.5**

**V-03 Composite: 60 + 30 + 7.5 = 97.5** | Golden

---

### V-04 — Combined: Severity-First + Macro-Phase

#### Essential (60%)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Required fields captured | PASS | A1: severity. A2: skill/expected/actual per severity-appropriate form. All four collected. |
| C-02 | Severity vocabulary enforcement | PASS | Four-value enum; "Reject any other value and re-prompt." |
| C-03 | GitHub issue format | PASS | Four distinct templates in A3 with title pattern and structured sections. |
| C-04 | Artifact path | PASS | `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md` |

Essential: **4/4 → 60**

#### Recommended (30%)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-05 | Actionable, specific title | PASS | Per-severity title patterns require skill name + symptom. |
| C-06 | Sufficient reproducibility context | PASS | B1 validates reproducibility; forms collect invocation, topic, chain. |
| C-07 | Repo open offer presented | PASS | B3 OFFER with `gh issue create --label "{severity}"`. |

Recommended: **3/3 → 30**

#### Aspirational (10%)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-08 | Severity-appropriate framing | PASS | crash: Priority HIGH + Impact field. improvement: Acceptance condition + Rationale. B1 checks tone match. |
| C-09 | Skill context enrichment | PASS | A2 forms collect invocation, topic, chain, version/date. B1 checks "Context enriched." |
| C-10 | Pre-write validation gate | PASS | B1 VALIDATE — named gate operation within Phase B. "Do not begin B2 until all rows pass." |
| C-11 | Corrective actions per validation check | PASS | B1 table has "Correction on fail" column — including "Return to A1" and "Return to A2" (cross-phase correction). Stronger than V-01/V-02/V-03. |
| C-12 | Per-severity body templates | PASS | Four distinct A3 templates with severity-differentiated sections (crash: Priority/Impact; improvement: Acceptance condition/Rationale; missing-feature: Scope/References). |
| C-13 | Severity-labeled issue creation | PASS | `--label "{severity}"` in B3 OFFER. |
| C-14 | Severity-first field sequencing | **PASS** | A1 asks severity alone — "What kind of issue is this?" — with no other fields. "Do not collect any other field until a valid severity value is confirmed." Severity then loads the matching collection form (A2) and output template (A3). Single event triggers both. Strongest implementation. |
| C-15 | Macro-phase hard boundary | **PASS** | PHASE A (A1+A2+A3) and PHASE B (B1+B2+B3), each with multiple named sub-operations. "DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE." Explicit completion condition. |

Aspirational: **8/8 → 10**

**V-04 Composite: 60 + 30 + 10 = 100** | Golden

---

### V-05 — Combined: Severity-First + Macro-Phase + Table Format

#### Essential (60%)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Required fields captured | PASS | A1: severity. A2: per-severity intake table with Skill/Expected/Actual marked required. All four fields collected. |
| C-02 | Severity vocabulary enforcement | PASS | Four-value enum; "Do not load the intake table or collect any other field until severity is confirmed." |
| C-03 | GitHub issue format | PASS | Four A3 templates with title pattern and structured sections. |
| C-04 | Artifact path | PASS | `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md` |

Essential: **4/4 → 60**

#### Recommended (30%)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-05 | Actionable, specific title | PASS | Per-severity title patterns require specific skill name + symptom. |
| C-06 | Sufficient reproducibility context | PASS | B1 validates reproducibility; A2 tables include invocation, topic, chain as recommended fields. |
| C-07 | Repo open offer presented | PASS | B3 OFFER with `gh issue create --label "{severity}"`. |

Recommended: **3/3 → 30**

#### Aspirational (10%)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-08 | Severity-appropriate framing | PASS | crash: Priority HIGH + Impact; improvement: Acceptance condition + Rationale. B1 checks "Tone matches severity." |
| C-09 | Skill context enrichment | PASS | A2 per-severity tables include topic, invocation, chain/related, version/date as recommended fields. B1 checks "Context enriched." |
| C-10 | Pre-write validation gate | PASS | B1 VALIDATE — structured gate, "Do not begin B2 until every row shows PASS." 8-row check table. |
| C-11 | Corrective actions per validation check | PASS | B1 table has "Correction on fail" column with return-to-phase instructions ("Return to A1", "Return to A2"). |
| C-12 | Per-severity body templates | PASS | Four distinct A3 templates. Also four distinct A2 intake tables — symmetric dual-table architecture. |
| C-13 | Severity-labeled issue creation | PASS | `--label "{severity}"` in B3 OFFER. |
| C-14 | Severity-first field sequencing | **PASS** | A1 asks severity alone. "Do not load the intake table or collect any other field until severity is confirmed." Severity gates intake table load itself — the table does not exist until severity is confirmed. Severity selects both the intake table (A2) and the output template (A3). Strongest expression of C-14: severity confirmation is simultaneously the collection gate and the table/template selector. |
| C-15 | Macro-phase hard boundary | **PASS** | PHASE A (A1+A2+A3) and PHASE B (B1+B2+B3). "DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE." Explicit completion condition defined. |

Aspirational: **8/8 → 10**

**V-05 Composite: 60 + 30 + 10 = 100** | Golden

---

### Summary Table

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Composite | C-14 | C-15 |
|-----------|---------------|------------------|-------------------|-----------|------|------|
| V-01 | 60 | 30 | 8.75 (7/8) | **98.75** | PASS | FAIL |
| V-02 | 60 | 30 | 8.75 (7/8) | **98.75** | FAIL | PASS |
| V-03 | 60 | 30 | 7.5 (6/8) | **97.5** | FAIL | FAIL |
| V-04 | 60 | 30 | 10 (8/8) | **100** | PASS | PASS |
| V-05 | 60 | 30 | 10 (8/8) | **100** | PASS | PASS |

**Top score**: 100 (V-04 and V-05)
**All-essential pass**: Yes, all five variations.

---

### Excellence Signals

Patterns from V-04 and V-05 that closed the gap from 98.75 to 100:

**1. Single severity-confirmation event with dual consequence (C-14 at full strength)**
The rubric's C-14 definition notes "template selection driven by severity confirmation" as the strongest implementation. V-04 and V-05 both achieve this: severity confirmation in A1 loads the collection form in A2 *and* determines the output template in A3 — one event with two downstream effects. V-05 makes this even more explicit: "Do not load the intake table…" — the intake table itself is not pre-shown; it is loaded as a consequence of severity confirmation.

**2. Dual-level blocking: phase boundary + row-level write gate**
Both V-04 and V-05 have blocking at two levels: the cross-phase "DO NOT BEGIN PHASE B" instruction and the within-phase "Do not begin B2 until all rows pass" instruction. This creates defense in depth — an implementer cannot skip validation by either ignoring the phase boundary or jumping within Phase B.

**3. Return-to-phase corrective actions**
V-04 and V-05 B1 corrections say "Return to A1, re-collect severity" and "Return to A2, ask for the missing field(s)" — the correction on failure specifies the exact return point in the other phase. V-01/V-02/V-03 corrections only say "ask user" or "rewrite." The cross-phase return instruction is a stronger corrective action pattern.

**4. Per-severity intake tables mirroring output templates (V-05)**
V-05 introduces symmetric dual-table architecture: a per-severity A2 intake table for collection and a per-severity A3 output template for drafting, both indexed by severity. C-12 required per-severity output templates; V-05 adds per-severity intake tables as a structural mirror. The table format in V-05 reinforces C-14 rather than undermining it, proving the three axes are mutually compatible.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["return-to-phase corrective actions: B1 corrections specify the exact phase+operation to return to (Return to A1, Return to A2) rather than generic re-ask instructions", "dual-level blocking: phase-boundary DO-NOT-BEGIN instruction plus row-level pre-write gate within Phase B creates defense in depth against skipping validation", "severity confirmation as table load gate: intake table does not pre-exist but is loaded as a consequence of severity confirmation, making the sequencing visually and structurally unavoidable"]}
```
