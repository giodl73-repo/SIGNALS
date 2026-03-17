Written to `simulations/quest/rubrics/discover-compare-rubric-v2-2026-03-17.md`.

---

**Three new aspirational criteria extracted from R1:**

| ID | Signal source | What it captures |
|----|---------------|-----------------|
| C-10 | V-03 phase labels, V-05 TOKEN RECALL | Labeled output tokens cross-checked at matrix assembly — missing scores structurally visible, not prose-detectable |
| C-11 | V-02 "Do not score relative to Option A", V-05 VERDICT independence constraints | Inertia independence stated as explicit exclusion prohibition at the sentence level, not just physical separation |
| C-12 | V-01 ANCHOR[0] pattern, V-05 Phase 0 dual-purpose | Status quo baseline committed as named anchor before any option analysis — prevents baseline drift |

**Scoring worksheet updated:** aspirational now `/5`, each worth `2 points` (10/5).

**C-09 tightened:** PARTIAL (audience only in AMEND) is now explicitly called out as a non-pass in the pass condition — previously the distinction was implicit.

**Two new failure modes added:** "Audience deferred to AMEND" and "Invisible omission" (untokenized matrix), "Baseline drift."
 — but the output should at least have raised the question
- C-10/C-11/C-12 are aspirational because they represent structural enforcement of already-essential behaviors; outputs can pass C-01 and C-02 without them, but these patterns make violations structurally visible rather than requiring human review

---

## Essential Criteria (60%)

Output fails if any of these are missing.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | All four dimensions are covered for both options | coverage | essential | Output addresses feasibility, risk, competitive positioning, and inertia for Option A AND Option B. Missing any dimension for either option = fail. |
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
| C-09 | Audience register is calibrated in the primary flow | depth | aspirational | When audience is specified or can be inferred, language and emphasis shift appropriately in the main output — not deferred to AMEND. Exec output leads with recommendation and business risk; engineering output leads with feasibility and implementation complexity. Audience handling available only as an AMEND slot = partial, not pass. One-size framing with no audience signal = fail. |
| C-10 | Labeled output tokens are cross-checked at matrix assembly | format | aspirational | Each analysis phase produces a labeled output token (e.g., FEASIBILITY-A:, VERDICT-B:) that is explicitly recalled or cross-checked when assembling the matrix. Missing scores are structurally visible rather than requiring prose review. Matrix assembled from free prose without named token references = fail. |
| C-11 | Inertia independence is stated as an explicit exclusion rule | correctness | aspirational | Each option's inertia phase contains an explicit "compare against status quo, not against Option [X]" prohibition — not just physical separation into different sections. The exclusion is stated as a rule that prevents relative comparison, making violations detectable. Separation without the explicit prohibition = fail. |
| C-12 | Status quo baseline is committed before analysis begins | behavior | aspirational | The status quo is defined as a named anchor (e.g., ANCHOR[0], STATUS QUO, Option 0) in a dedicated phase before any option analysis begins. Subsequent inertia phases reference this anchor by name. Baseline defined inline during inertia phases, or implied rather than declared = fail. |

---

## Scoring Worksheet

```
Essential passed:    ___ / 4   =>  ___ * 60 / 4  = ___
Recommended passed:  ___ / 3   =>  ___ * 30 / 3  = ___
Aspirational passed: ___ / 5   =>  ___ * 10 / 5  = ___

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
- **Audience deferred to AMEND** — audience register available only as an amendment slot; primary output is single-register (C-09 partial, not pass)
- **Baseline drift** — inertia phases each define their own implied status quo rather than referencing a shared anchor declared before analysis (C-12 fail)
- **Invisible omission** — matrix assembled from prose with no labeled tokens; a missing score is not detectable without re-reading all analysis phases (C-10 fail)
