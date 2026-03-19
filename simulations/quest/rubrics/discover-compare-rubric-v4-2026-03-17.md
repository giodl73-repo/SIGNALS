Done. Here's what changed from v3:

**Two calibrations (existing criteria refined):**

- **C-14** — pass condition now explicitly states label flexibility: FAULT:, VIOLATION:, SCORING DEFECT:, or any named class all pass. Co-location is the criterion, not the label.
- **C-15** — pass condition now explicitly states that physical REG-before-ANCHOR[0] ordering in a single inline phase satisfies it; the Part A/Part B split is sufficient but not required.

**One new criterion:**

- **C-17** (format, aspirational) — *Output is compressed to operative directives only.* Confirmed by V-03 scoring 100/100 at ~50% word count. Explanatory prose (rule tables, binding rationale, Print: confirmations, preamble framing) is overhead, not mechanism. Operative directives alongside explanatory scaffolding = partial. **Denominator bumps from /9 to /10.**

**One new failure mode:** "Operative mechanism with explanatory overhead" — directives all present but wrapped in prose that compression would strip without losing any structural property.
ully-compressed output (all operative criteria met, no explanatory overhead) scores 10/10 aspirational → 10 pts. An output with operative criteria met but explanatory prose present scores 9/10 → 9 pts, placing it at ~99 composite vs. 100 for a compressed equivalent.

**One new failure mode** added to the watch list for C-17.

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
| C-13 | Anchor sentence is reproduced verbatim at each inertia phase | behavior | aspirational | Each inertia phase reproduces the exact anchor sentence — not a paraphrase, not just the anchor name. The no-paraphrase mandate must appear co-located with the TOKEN RECALL directive at point of use (e.g., `{reproduce exact sentence from Phase 0 — do not paraphrase}`), not only in a preamble or template slot instruction. Baseline drift is detectable as a token mismatch rather than requiring prose re-reading. Anchor name reference without the sentence, or "exact" instruction inside a fill-in slot without a co-located no-paraphrase mandate = fail. |
| C-14 | Exclusion prohibition is named as a failure class at point of use | correctness | aspirational | Each inertia phase states the exclusion prohibition as a named failure class co-located with the TOKEN RECALL step — not only in a header or preamble. Any named failure class label satisfies this criterion: FAULT:, VIOLATION:, SCORING DEFECT:, or equivalent. The co-location is the requirement; the specific label is not. Prohibition stated only in framing outside the inertia phase itself = fail. |
| C-15 | Register is declared before the status quo anchor | behavior | aspirational | Audience register is declared as a named token before ANCHOR[0] is committed. The anchor sentence is written in the declared register; the register token is recalled at the recommendation phase. Physical token ordering in a single inline phase satisfies this criterion — a Part A/Part B structural split is sufficient but not required. Register declared after the anchor, or inferred from the anchor framing = fail. |
| C-16 | Token ledger is enforced as a blocking gate | format | aspirational | The ledger check includes an explicit blocking instruction ("do not proceed," "do not assemble," "halt") that makes a missing token a blocked path rather than a checklist item. Ledger check present as a list without a blocking instruction = fail. |
| C-17 | Output is compressed to operative directives only | format | aspirational | All operative mechanisms are present as pure directives — token declarations, recall instructions, exclusion prohibitions, blocking gates, verdict labels. Explanatory prose is absent: no rule description tables, no binding rationale sentences, no Print: confirmations, no preamble framing. Operative directives present alongside explanatory scaffolding = partial. Explanatory prose exceeding operative content in volume = fail. |

---

## Scoring Worksheet

```
Essential passed:    ___ / 4   =>  ___ * 60 / 4  = ___
Recommended passed:  ___ / 3   =>  ___ * 30 / 3  = ___
Aspirational passed: ___ / 10  =>  ___ * 10 / 10 = ___

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
- **No-paraphrase in preamble only** — "do not paraphrase" or "exact" instruction appears only in Phase 0 framing or a template slot, not co-located with the TOKEN RECALL directive at point of use (C-13 fail)
- **Invisible omission** — matrix assembled from prose with no labeled tokens; a missing score is not detectable without re-reading all analysis phases (C-10 fail)
- **Preamble-only prohibition** — exclusion rule stated in framing but absent from the inertia phase itself; the rule is not at the point of use (C-14 fail)
- **Register after anchor** — audience declared after status quo is committed; anchor sentence is written before register is known and cannot be reframed (C-15 fail)
- **Ledger as checklist** — token ledger lists required tokens but includes no blocking instruction; a missing token is a suggestion to fill in, not a halt (C-16 fail)
- **Operative mechanism with explanatory overhead** — all directive mechanisms are present but surrounded by rule descriptions, rationale sentences, or preamble framing; compression to operative-only form would reduce word count by 40%+ without losing any structural property (C-17 partial, not pass)
