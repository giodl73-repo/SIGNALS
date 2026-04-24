Rubric written to `simulations/quest/rubrics/discover-compare-rubric-2026-03-17.md`.

**Structure:**
- **4 Essential** (60%): four-dimension coverage on both options, independent inertia check per option, decision matrix present, explicit recommendation
- **3 Recommended** (30%): build/no-build gate when both fail inertia, differentiated risk per option, actionable AMEND section
- **2 Aspirational** (10%): Option 0 as a named matrix column, audience register calibration

**Key design decisions:**
- C-02 (independent inertia) is essential because the skill's defining insight — that neither option may be worth building — depends on checking each option against "do nothing" separately, not just against each other
- C-04 requires an explicit recommendation; "it depends" without resolution is a fail
- C-05 (neither surfaced) is recommended rather than essential because an output can still be useful if the author's context makes "neither" implausible — but the output should at least have raised the question
n A AND Option B. Missing any dimension for either option = fail. |
| C-02 | Inertia check is applied independently to both options | correctness | essential | The output asks "would teams do nothing instead of THIS option?" for Option A separately and Option B separately — not as a relative A-vs-B comparison. Each option has its own inertia verdict. A single combined inertia statement = fail. |
| C-03 | A decision matrix is present | format | essential | Output contains a structured matrix (table or equivalent scored grid) placing both options side-by-side across dimensions. Prose-only comparison without any structured layout = fail. |
| C-04 | A concrete recommendation is made | correctness | essential | Output concludes with a stated recommendation: A, B, neither, or conditional. The recommendation must be explicit. Ending with "it depends" without resolution, or implying a preference without stating it = fail. |

---

## Recommended Criteria (30%)

Output is better with these.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | Build/no-build gate is surfaced when both options fail inertia | behavior | recommended | If both options score weak on inertia (teams would do nothing), the output explicitly raises "build neither" as a possible recommendation. May still conclude build, but must surface the question. Outputs that treat A-vs-B as the only valid frame = fail. |
| C-06 | Risk factors are meaningfully differentiated between options | depth | recommended | Risks listed for Option A and Option B are distinct — not symmetric or copy-pasted. At least one risk is unique to each option, or the output explains why risks are identical. |
| C-07 | AMEND section is actionable | coverage | recommended | Output includes an AMEND section (or equivalent) that provides concrete instructions for at least one of: adding a third option, weighting a specific dimension, adjusting for exec vs engineering audience. Generic "you could amend this" without a concrete prompt or slot structure = fail. |

---

## Aspirational Criteria (10%)

Raise the bar once essential and recommended are stable.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | "Do nothing" (Option 0) is a named column in the matrix | behavior | aspirational | The status quo is represented as Option 0 in the comparison matrix — not just mentioned in prose. Both build options are scored against the status quo simultaneously, making it visible when A and B both lose to inertia rather than only when they tie each other. |
| C-09 | Audience register is calibrated | depth | aspirational | When audience is specified or can be inferred, language and emphasis shift appropriately. Exec output leads with recommendation and business risk; engineering output leads with feasibility and implementation complexity. One-size framing with no audience signal = fail. |

---

## Scoring Worksheet

```
Essential passed:    ___ / 4   =>  ___ * 60 / 4  = ___
Recommended passed:  ___ / 3   =>  ___ * 30 / 3  = ___
Aspirational passed: ___ / 2   =>  ___ * 10 / 2  = ___

Composite score: ___

Golden: all 4 essential pass AND composite >= 80
```

| Band | Score | Meaning |
|------|-------|---------|
| Golden | all essential + >= 80 | Ship-ready comparison artifact |
| Passing | all essential + 60-79 | Usable; recommended gaps noted |
| Failing | any essential fails | Not useful as a comparison artifact |

---

## Failure Modes to Watch

- **Symmetric inertia** — both options get identical inertia commentary; suggests the check was not applied independently
- **Matrix without assessments** — decision matrix lists dimensions but provides no values or ratings, making comparison impossible
- **Implied recommendation** — output clearly leans toward one option but never states it
- **Missing dimension** — feasibility and risk covered but competitive positioning omitted entirely
- **AMEND as afterthought** — AMEND section present but contains only meta-commentary without a concrete prompt or structure
