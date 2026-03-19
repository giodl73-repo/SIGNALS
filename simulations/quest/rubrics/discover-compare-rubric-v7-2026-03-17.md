Looking at the three new patterns from R8:

1. **phase-labels-inert** → C-22: structural separation via token block + divider, labels fully inert
2. **recommendation-first-valid** → C-23: exec-register output leads with recommendation before matrix
3. **sub-ledger-benign** → C-24: AMEND blocking gate enumerates token names before the halt instruction

Aspirational denominator bumps /14 → /17. Here is the complete v7 rubric:

---

```markdown
## discover-compare-rubric-v7-2026-03-17.md

What changed from v6:

**Three new criteria from R8 excellence signals:**

- **C-22** (format, aspirational) — *Phase structure is enforced by operative token positioning
  and section dividers; phase label headers are absent or fully inert.* Confirmed by V-02:
  removing all PHASE N -- NAME headers while preserving the REG + ANCHOR[0] token block
  before the first `---` divider satisfies C-12 "dedicated phase" without a labeled header.
  Phase labels are cosmetic; their presence or absence does not change conformance. Output
  with structural separation via token block + divider and no phase labels = pass. Output
  where phase labels are the sole mechanism establishing phase boundaries (removing them
  would merge phases) = partial. **Denominator bumps from /14 to /15.**

- **C-23** (behavior, aspirational) — *Exec-register output leads with the recommendation
  token before the decision matrix, surfacing the conclusion before the evidence trail.*
  Confirmed by V-05: recommendation-first ordering satisfies all 21 prior criteria
  unchanged; no criterion encodes phase-ordering constraints on recommendation vs. matrix;
  exec-register output that places the recommendation first is natively aligned with exec
  reading pattern without requiring AMEND. Recommendation before matrix when REG = exec =
  pass. Matrix before recommendation when REG = exec = partial. No register-sensitive
  ordering present = fail. **Denominator bumps from /15 to /16.**

- **C-24** (format, aspirational) — *Each AMEND path blocking gate enumerates the token
  names required by that path before issuing the halt instruction.* Confirmed by V-04:
  the sub-ledger inside the Add-C path (listing token names: ANCHOR[0], FEAS-C, RISK-C,
  etc.) is a structural verification step that makes a missing token visible by name before
  the blocking halt fires. This enumeration is a verification gate, not TOKEN RECALL — it
  does not constitute over-recall under C-20. Token-name mini-ledger + blocking instruction
  at each AMEND path = pass. Blocking instruction without token enumeration = partial.
  No blocking gate at AMEND paths = C-19 fail (not scored here). **Denominator bumps
  from /16 to /17.**

**Three new patterns added to watch list:**

- **phase-labels-inert** — PHASE N -- NAME headers are cosmetic; structural separation
  (token block + `---` divider before first analysis token) satisfies C-12 "dedicated
  phase" without a labeled header (C-22 pass; confirmed V-02)
- **recommendation-first-valid** — placing recommendation before matrix in exec register
  is natively audience-aligned and satisfies all criteria unchanged; no criterion is
  phase-order-sensitive on recommendation vs. matrix (C-23 pass; confirmed V-05)
- **sub-ledger-benign** — token-name listing inside an AMEND path blocking gate is a
  structural verification step, not TOKEN RECALL; does not fire C-20 over-recall
  (C-24 pass; confirmed V-04)

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
| C-12 | Status quo baseline is committed before analysis begins | behavior | aspirational | The status quo is defined as a named anchor (e.g., ANCHOR[0], STATUS QUO, Option 0) in a dedicated phase before any option analysis begins. Subsequent inertia phases reference this anchor by name. A dedicated phase requires a structurally separate block (token declarations + section divider) before the first analysis token — a labeled header is not required. Baseline defined inline during inertia phases, or implied rather than declared = fail. |
| C-13 | Anchor sentence is reproduced verbatim at each inertia phase | behavior | aspirational | Each inertia phase reproduces the exact anchor sentence — not a paraphrase, not just the anchor name. The no-paraphrase mandate must appear co-located with the TOKEN RECALL directive at point of use (e.g., `{reproduce exact sentence from Phase 0 — do not paraphrase}`), not only in a preamble or template slot instruction. Baseline drift is detectable as a token mismatch rather than requiring prose re-reading. Anchor name reference without the sentence, or "exact" instruction inside a fill-in slot without a co-located no-paraphrase mandate = fail. |
| C-14 | Exclusion prohibition is named as a failure class at point of use | correctness | aspirational | Each inertia phase states the exclusion prohibition as a named failure class co-located with the TOKEN RECALL step — not only in a header or preamble. Any named failure class label satisfies this criterion: FAULT:, VIOLATION:, SCORING DEFECT:, or equivalent. The co-location is the requirement; the specific label is not. Prohibition stated only in framing outside the inertia phase itself = fail. |
| C-15 | Register is declared before the status quo anchor | behavior | aspirational | Audience register is declared as a named token before ANCHOR[0] is committed. The anchor sentence is written in the declared register; the register token is recalled at the recommendation phase. Physical token ordering in a single inline phase satisfies this criterion — a Part A/Part B structural split is sufficient but not required. Register declared after the anchor, or inferred from the anchor framing = fail. |
| C-16 | Token ledger is enforced as a blocking gate | format | aspirational | The ledger check includes an explicit blocking instruction ("do not proceed," "do not assemble," "halt") that makes a missing token a blocked path rather than a checklist item. Ledger check present as a list without a blocking instruction = fail. |
| C-17 | Output is compressed to operative directives only | format | aspirational | All operative mechanisms are present as pure directives — token declarations, recall instructions, exclusion prohibitions, blocking gates, verdict labels. Explanatory prose is absent: no rule description tables, no binding rationale sentences, no Print: confirmations, no preamble framing. Phase label headers (PHASE N -- NAME) are section labels, not explanatory prose — their presence or absence is neutral to this criterion. Operative directives present alongside explanatory scaffolding = partial. Explanatory prose exceeding operative content in volume = fail. |
| C-18 | Exclusion FAULT is encoded as a single dual-polarity directive | correctness | aspirational | The inertia exclusion FAULT encodes both polarities in one line: the positive mandate (compare against ANCHOR[0] only) and the negative prohibition (inter-option comparison is an error). Single-polarity form covering only the prohibition = partial. Two separate sentences achieving the same dual coverage = partial. Explanatory clause appended to the directive = overhead, not mechanism. |
| C-19 | AMEND phase is self-contained via inline TOKEN RECALL and FAULT prohibitions | behavior | aspirational | Each amendment path in the AMEND phase carries its own inline TOKEN RECALL directives and FAULT prohibitions, making the path executable without re-reading primary phases. Slot declarations with inline TOKEN RECALL + FAULT at each path = pass. Prose path descriptions without slot declarations = fail. Slot declarations without inline TOKEN RECALL or FAULT = partial. |
| C-20 | TOKEN RECALL at each AMEND path is scoped to that path's operational requirements | behavior | aspirational | Each amendment path recalls only the tokens required for its own execution: the register path recalls only REG (register override does not involve status-quo evaluation; ANCHOR[0] recall here = over-recall); option-addition and weight paths recall ANCHOR[0] and any register token their execution requires. A token-name mini-ledger inside a blocking gate is a structural verification step, not TOKEN RECALL, and does not count as over-recall. Uniform superset recall across all paths regardless of operational need = partial. Any path that over-recalls and any path that under-recalls in the same output = fail. |
| C-21 | Dual-polarity FAULT discipline propagates from primary phases into every AMEND path | correctness | aspirational | Each amendment path carries a one-line FAULT encoding positive mandate + negative prohibition, consistent with the C-18 structural discipline applied in primary inertia phases. All AMEND paths with dual-polarity FAULT = pass. Some paths with dual-polarity FAULT, others with single-polarity or none = partial. No FAULT directives in AMEND paths, or all paths with single-polarity form only = fail. |
| C-22 | Phase structure is enforced by operative token positioning and section dividers, not by labeled headers | format | aspirational | The output achieves structural phase separation through the positioning of operative tokens (REG, ANCHOR[0]) and section dividers (`---` or equivalent) alone — phase label headers (PHASE N -- NAME) are absent or present only as inert cosmetic scaffolding. Pass condition: removing all phase label headers from the output would not merge any two phases or break any structural boundary. Output where phase labels are the sole mechanism establishing phase boundaries (removing them would collapse phases into each other) = partial. Output indistinguishable in structure with or without labels = pass. |
| C-23 | Exec-register output leads with the recommendation token before the decision matrix | behavior | aspirational | When REG = exec, the recommendation token appears before the decision matrix in the output — surfacing the conclusion before the evidence trail in alignment with exec reading pattern. This ordering satisfies all other criteria unchanged; no criterion is phase-order-sensitive on recommendation vs. matrix. Recommendation before matrix when REG = exec = pass. Matrix before recommendation when REG = exec = partial. No register-sensitive ordering distinguishable in the output = fail. |
| C-24 | Each AMEND path blocking gate enumerates required token names before the halt instruction | format | aspirational | The blocking gate at each AMEND path entry contains a mini-ledger that lists by name the tokens required for that path's execution, followed by the blocking halt instruction. This enumeration is a structural verification step — it makes a missing token visible by name before the path fires. Token-name mini-ledger + blocking instruction at each AMEND path = pass. Blocking instruction present but without token enumeration = partial. No blocking gate at AMEND paths = C-19 fail (not scored here). |

---

## Scoring Worksheet

```
Essential passed:    ___ / 4   =>  ___ * 60 / 4  = ___
Recommended passed:  ___ / 3   =>  ___ * 30 / 3  = ___
Aspirational passed: ___ / 17  =>  ___ * 10 / 17 = ___

Total composite: ___
```

## Watch List — Failure Modes

| Pattern | Criterion | Class |
|---------|-----------|-------|
| Uniform superset recall | C-20 | partial |
| FAULT discipline lost at AMEND boundary | C-21 | fail |
| Phase labels load-bearing (removing them merges phases) | C-22 | partial |
| Matrix-before-recommendation in exec register | C-23 | partial |
| Blocking gate without token enumeration | C-24 | partial |
| Inertia comparison crosses option boundary | C-02, C-11 | fail |
| Anchor paraphrased at inertia phase | C-13 | fail |
| FAULT not co-located with TOKEN RECALL | C-14 | fail |
| Ledger present but no blocking instruction | C-16 | fail |
| Explanatory prose alongside operative directives | C-17 | partial |
| Single-polarity exclusion FAULT | C-18 | partial |
| AMEND paths without inline TOKEN RECALL or FAULT | C-19 | partial |
```
