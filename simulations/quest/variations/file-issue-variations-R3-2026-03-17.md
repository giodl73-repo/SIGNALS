Written to `simulations/quest/golden/file-issue-variate-R3-2026-03-17.md`.

---

## Round 3 Variations — file-issue

**Rubric**: v3 (C-01 through C-13) | All 5 variations predict 100.

---

### Variation axes and hypotheses

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | Phrasing register (conversational imperative) | Conversational "ask" language reduces field-capture friction without sacrificing structural rigor. If V-01 scores the same as formal variations, register is irrelevant to compliance. |
| **V-02** | Role sequence (template-first) | Selecting severity BEFORE collecting other fields turns the template into an input form, not just an output form. This produces architecturally tighter C-12 compliance because template selection drives collection. |
| **V-03** | Inertia framing (workflow blockage as metaphor) | Framing every template around "what workflow is blocked" produces richer C-06 (reproducibility) and C-09 (enrichment) because users anchor on what they were trying to do, not what went wrong. |
| **V-04** | Lifecycle compression (2 macro-phases) | Compressing 4 phases into COLLECT+DRAFT / VALIDATE+WRITE preserves the blocking gate at the phase boundary at half the instruction overhead. Tests whether the gate property lives in the blocking instruction or the four-phase structure. |
| **V-05** | Minimal-token density (all criteria compressed) | The minimum structural token count that satisfies all 13 criteria. If V-05 scores the same as V-04 Round 2, token count is irrelevant. If it fails C-10 or C-12, the structural apparatus is load-bearing. |

---

### Key structural decisions per criterion

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-12** (4 templates) | 4 named `If {severity}` blocks | 4 named `**Form:**` + `**Template:**` pairs | 4 templates with workflow-framing section | 4 named templates in Phase A | 4 `*severity:*` blocks — no prose wrapper |
| **C-13** (--label) | present | present | present | present | present |
| **C-10** (blocking gate) | "check all...do not write until every check passes" | explicit STEP 4 gate | VALIDATE phase with blocking instruction | "DO NOT BEGIN PHASE B" | "STOP. Do not write until all rows pass" |
| **C-11** (remedies) | plain-language remedies in numbered list | corrective-action table in Step 4 | table with "Correction on fail" column | table in Phase B1 | table with "Remedy on fail" column |

---

### Round 2 regression check

V-04 Round 2 had the full four-step TRIAGE/DRAFT/PRE-WRITE GATE/WRITE+OFFER structure and hit all 13 criteria. Round 3 V-04 tests whether compressing that to two macro-phases loses any ground. Round 3 V-02 tests whether template-first ordering (severity → template → collection) is structurally superior to the Round 2 approach (collect all four → then apply template).
