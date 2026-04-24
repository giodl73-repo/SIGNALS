Written to `simulations/quest/rubrics/discover-compare-rubric-v3-2026-03-17.md`.

---

**What changed from v2:**

Four new aspirational criteria, each targeting a structural enforcement pattern that V-05 demonstrated but the v2 rubric couldn't distinguish:

| ID | Tightens | From PARTIAL/FAIL to PASS requires |
|----|----------|-------------------------------------|
| C-13 | C-12 | Verbatim anchor sentence at each inertia phase, not just name reference — drift becomes a token mismatch |
| C-14 | C-11 | "is an error" failure class co-located inside the inertia phase alongside TOKEN RECALL — not only in preamble |
| C-15 | C-09 | Register declared before ANCHOR[0] — register is a precondition for the anchor sentence, not just for the recommendation |
| C-16 | C-10 | "Do not proceed with gaps" blocking instruction in the ledger check — missing token halts assembly, not just flags it |

**Scoring worksheet:** aspirational denominator bumped from `/5` to `/9` (still normalized to 10 points). A V-05-class output scores 9/9 aspirational → 10 pts; a V-04 (C-12 PASS but not verbatim recall) scores ~6/9 → ~6.7 pts, placing it ~94.7 composite vs. 100 for V-05.

**Four new failure modes** added to the watch list, one per criterion.
Essential Criteria (60%)

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
| C-13 | Anchor sentence is reproduced verbatim at each inertia phase | behavior | aspirational | Each inertia phase reproduces the exact anchor sentence — not a paraphrase, not just the anchor name. Baseline drift is detectable as a token mismatch rather than requiring prose re-reading. Referencing the anchor by name without quoting the sentence = fail. |
| C-14 | Exclusion prohibition is named as a failure class at point of use | correctness | aspirational | Each inertia phase states the exclusion prohibition as a named failure class ("is an error", "is a scoring defect", etc.) co-located with the TOKEN RECALL step — not only in a header or preamble. Prohibition stated only in framing outside the inertia phase itself = fail. |
| C-15 | Register is declared before the status quo anchor | behavior | aspirational | Audience register is declared as a named token before ANCHOR[0] is committed. The anchor sentence is written in the declared register; the register token is recalled at the recommendation phase. Register declared after the anchor, or inferred from the anchor framing = fail. |
| C-16 | Token ledger is enforced as a blocking gate | format | aspirational | The ledger check includes an explicit blocking instruction ("do not proceed," "do not assemble," "halt") that makes a missing token a blocked path rather than a checklist item. Ledger check present as a list without a blocking instruction = fail. |

---

## Scoring Worksheet

```
Essential passed:    ___ / 4   =>  ___ * 60 / 4  = ___
Recommended passed:  ___ / 3   =>  ___ * 30 / 3  = ___
Aspirational passed: ___ / 9   =>  ___ * 10 / 9  = ___

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
- **Anchor name without anchor sentence** — inertia phase references ANCHOR[0] by name but does not reproduce the sentence; drift is invisible at the token level (C-13 fail)
- **Invisible omission** — matrix assembled from prose with no labeled tokens; a missing score is not detectable without re-reading all analysis phases (C-10 fail)
- **Preamble-only prohibition** — exclusion rule stated in framing but absent from the inertia phase itself; the rule is not at the point of use (C-14 fail)
- **Register after anchor** — audience declared after status quo is committed; anchor sentence is written before register is known and cannot be reframed (C-15 fail)
- **Ledger as checklist** — token ledger lists required tokens but includes no blocking instruction; a missing token is a suggestion to fill in, not a halt (C-16 fail)
