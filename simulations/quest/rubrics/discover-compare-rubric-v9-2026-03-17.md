v9 rubric written. Here's what was extracted from R10 and how each pattern was resolved:

---

**c23-positional-independence → C-26 (new criterion) + C-23 update**

R10 V-03 confirmed: C-23 fires on effective output position, not routing construct presence. Engineering-only routing leaves exec ordering determined by body section position, which satisfies C-23 independently. This revealed a design principle worth rewarding explicitly:

**C-26 — Body section order is exec-safe without routing**: RECOMMENDATION precedes DECISION MATRIX in body by design. Routing block serves as a deviation mechanism for non-exec registers, not the source of exec correctness. Body-first recommendation = pass; matrix-first body (exec depends on routing firing) = partial; ambiguous ordering = fail.

C-23's pass condition updated to state routing-construct-independence explicitly and note that C-25 PARTIAL does not create a C-23 gap.

---

**c25-partial-form-agnostic → scoring clarification in C-25 (no new criterion)**

Three structurally distinct partial forms (exec-only, engineering-only, two-branch prose) score identically within the PARTIAL band. Following the same treatment as c24-partial-path-agnostic from R9: this is a scoring boundary, not a new output excellence behavior. Incorporated into C-25's pass condition text with a PARTIAL flat-band statement.

---

**Structural corollary → C-27 (new criterion)**

Since routing depends on REG, it must appear after the LEDGER GATE that verifies REG is present. A routing block before the gate fires without protection — absent REG reaches routing logic unguarded.

**C-27 — Routing block is positioned within LEDGER GATE scope**: Routing after gate = pass; routing before gate = partial; no routing block = fail (C-25 scores independently).

---

**Denominator: /18 → /20**. Two new watch list entries added for both R10 patterns.
as been verified present. A routing block positioned before the LEDGER GATE fires without gate protection -- an absent REG reaches routing logic unguarded. Routing block after LEDGER GATE = pass. Routing block before LEDGER GATE = partial. No routing block = fail (C-25 scoring applies independently). Denominator bumps /19 → /20.

**Two scoring clarifications applied:**

- **c23-positional-independence** -- C-23 reads effective exec output position, not routing construct presence or completeness. Positional ordering (RECOMMENDATION precedes DECISION MATRIX in body) satisfies C-23 independently. C-25 PARTIAL does not create a C-23 gap; the two criteria are orthogonal. Incorporated into C-23's pass condition text.

- **c25-partial-form-agnostic** -- C-25 PARTIAL is a flat discrete state regardless of which partial form is present. Exec-only routing, engineering-only routing, and two-branch prose all score identically within the PARTIAL band. No sub-grades within PARTIAL -- form variation does not move the score. The only path to C-25 PASS is both branches in a unified conditional construct. Incorporated into C-25's pass condition text; no new criterion generated; no denominator change from this pattern.

**Two new patterns added to watch list:**

- **c23-positional-independence** -- C-23 is routing-construct-independent; effective exec output position (body section order when no exec-branch routing override is present) satisfies C-23; C-25 PARTIAL does not create a C-23 gap (confirmed V-03)
- **c25-partial-form-agnostic** -- C-25 PARTIAL is a flat band; exec-only routing, engineering-only routing, and two-branch prose all score identically; no sub-grades within PARTIAL; both branches in a single conditional construct is the only PASS path (confirmed V-02 = V-03 = V-04)

---

## Essential Criteria (60%)

Output fails if any of these are missing.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | All four dimensions are covered for both options | coverage | essential | Output addresses feasibility, risk, competitive positioning, and inertia for Option A AND Option B. Missing any dimension for either option = fail. |
| C-02 | Inertia check is applied independently to both options | correctness | essential | The output asks "would teams do nothing instead of THIS option?" for Option A separately and Option B separately -- not as a relative A-vs-B comparison. Each option has its own inertia verdict. A single combined inertia statement = fail. |
| C-03 | A decision matrix is present | format | essential | Output contains a structured matrix (table or equivalent scored grid) placing both options side-by-side across dimensions. Prose-only comparison without any structured layout = fail. |
| C-04 | A concrete recommendation is made | correctness | essential | Output concludes with a stated recommendation: A, B, neither, or conditional. The recommendation must be explicit. Ending with "it depends" without resolution, or implying a preference without stating it = fail. |

---

## Recommended Criteria (30%)

Output is better with these.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | Build/no-build gate is surfaced when both options fail inertia | behavior | recommended | If both options score weak on inertia (teams would do nothing), the output explicitly raises "build neither" as a possible recommendation. May still conclude build, but must surface the question. Outputs that treat A-vs-B as the only valid frame = fail. |
| C-06 | Risk factors are meaningfully differentiated between options | depth | recommended | Risks listed for Option A and Option B are distinct -- not symmetric or copy-pasted. At least one risk is unique to each option, or the output explains why risks are identical. |
| C-07 | AMEND section is actionable | coverage | recommended | Output includes an AMEND section (or equivalent) that provides concrete instructions for at least one of: adding a third option, weighting a specific dimension, adjusting for exec vs engineering audience. Generic "you could amend this" without a concrete prompt or slot structure = fail. |

---

## Aspirational Criteria (10%)

Raise the bar once essential and recommended are stable.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | "Do nothing" (Option 0) is a named column in the matrix | behavior | aspirational | The status quo is represented as Option 0 in the comparison matrix -- not just mentioned in prose. Both build options are scored against the status quo simultaneously, making it visible when A and B both lose to inertia rather than only when they tie each other. |
| C-09 | Audience register is calibrated in the primary flow | depth | aspirational | When audience is specified or can be inferred, language and emphasis shift appropriately in the main output -- not deferred to AMEND. Exec output leads with recommendation and business risk; engineering output leads with feasibility and implementation complexity. Audience handling available only as an AMEND slot = partial, not pass. One-size framing with no audience signal = fail. |
| C-10 | Labeled output tokens are cross-checked at matrix assembly | format | aspirational | Each analysis phase produces a labeled output token (e.g., FEASIBILITY-A:, VERDICT-B:) that is explicitly recalled or cross-checked when assembling the matrix. Missing scores are structurally visible rather than requiring prose review. Matrix assembled from free prose without named token references = fail. |
| C-11 | Inertia independence is stated as an explicit exclusion rule | correctness | aspirational | Each option's inertia phase contains an explicit "compare against status quo, not against Option [X]" prohibition -- not just physical separation into different sections. The exclusion is stated as a rule that prevents relative comparison, making violations detectable. Separation without the explicit prohibition = fail. |
| C-12 | Status quo baseline is committed before analysis begins | behavior | aspirational | The status quo is defined as a named anchor (e.g., ANCHOR[0], STATUS QUO, Option 0) in a dedicated phase before any option analysis begins. Subsequent inertia phases reference this anchor by name. A dedicated phase requires a structurally separate block (token declarations + section divider) before the first analysis token -- a labeled header is not required. Baseline defined inline during inertia phases, or implied rather than declared = fail. |
| C-13 | Anchor sentence is reproduced verbatim at each inertia phase | behavior | aspirational | Each inertia phase reproduces the exact anchor sentence -- not a paraphrase, not just the anchor name. The no-paraphrase mandate must appear co-located with the TOKEN RECALL directive at point of use (e.g., `{reproduce exact sentence from Phase 0 -- do not paraphrase}`), not only in a preamble or template slot instruction. Baseline drift is detectable as a token mismatch rather than requiring prose re-reading. Anchor name reference without the sentence, or "exact" instruction inside a fill-in slot without a co-located no-paraphrase mandate = fail. |
| C-14 | Exclusion prohibition is named as a failure class at point of use | correctness | aspirational | Each inertia phase states the exclusion prohibition as a named failure class co-located with the TOKEN RECALL step -- not only in a header or preamble. Any named failure class label satisfies this criterion: FAULT:, VIOLATION:, SCORING DEFECT:, or equivalent. The co-location is the requirement; the specific label is not. Prohibition stated only in framing outside the inertia phase itself = fail. |
| C-15 | Register is declared before the status quo anchor | behavior | aspirational | Audience register is declared as a named token before ANCHOR[0] is committed. The anchor sentence is written in the declared register; the register token is recalled at the recommendation phase. Physical token ordering in a single inline phase satisfies this criterion -- a Part A/Part B structural split is sufficient but not required. Register declared after the anchor, or inferred from the anchor framing = fail. |
| C-16 | Token ledger is enforced as a blocking gate | format | aspirational | The ledger check includes an explicit blocking instruction ("do not proceed," "do not assemble," "halt") that makes a missing token a blocked path rather than a checklist item. Ledger check present as a list without a blocking instruction = fail. |
| C-17 | Output is compressed to operative directives only | format | aspirational | All operative mechanisms are present as pure directives -- token declarations, recall instructions, exclusion prohibitions, blocking gates, verdict labels. Explanatory prose is absent: no rule description tables, no binding rationale sentences, no Print: confirmations, no preamble framing. Phase label headers (PHASE N -- NAME) are section labels, not explanatory prose -- their presence or absence is neutral to this criterion. Operative directives present alongside explanatory scaffolding = partial. Explanatory prose exceeding operative content in volume = fail. |
| C-18 | Exclusion FAULT is encoded as a single dual-polarity directive | correctness | aspirational | The inertia exclusion FAULT encodes both polarities in one line: the positive mandate (compare against ANCHOR[0] only) and the negative prohibition (inter-option comparison is an error). Single-polarity form covering only the prohibition = partial. Two separate sentences achieving the same dual coverage = partial. Explanatory clause appended to the directive = overhead, not mechanism. |
| C-19 | AMEND phase is self-contained via inline TOKEN RECALL and FAULT prohibitions | behavior | aspirational | Each amendment path in the AMEND phase carries its own inline TOKEN RECALL directives and FAULT prohibitions, making the path executable without re-reading primary phases. Slot declarations with inline TOKEN RECALL + FAULT at each path = pass. Prose path descriptions without slot declarations = fail. Slot declarations without inline TOKEN RECALL or FAULT = partial. |
| C-20 | TOKEN RECALL at each AMEND path is scoped to that path's operational requirements | behavior | aspirational | Each amendment path recalls only the tokens required for its own execution: the register path recalls only REG (register override does not involve status-quo evaluation; ANCHOR[0] recall here = over-recall); option-addition and weight paths recall ANCHOR[0] and any register token their execution requires. A token-name mini-ledger inside a blocking gate is a structural verification step, not TOKEN RECALL, and does not count as over-recall. Uniform superset recall across all paths regardless of operational need = partial. Any path that over-recalls and any path that under-recalls in the same output = fail. |
| C-21 | Dual-polarity FAULT discipline propagates from primary phases into every AMEND path | correctness | aspirational | Each amendment path carries a one-line FAULT encoding positive mandate + negative prohibition, consistent with the C-18 structural discipline applied in primary inertia phases. All AMEND paths with dual-polarity FAULT = pass. Some paths with dual-polarity FAULT, others with single-polarity or none = partial. No FAULT directives in AMEND paths, or all paths with single-polarity form only = fail. |
| C-22 | Phase structure is enforced by operative token positioning and section dividers, not by labeled headers | format | aspirational | The output achieves structural phase separation through the positioning of operative tokens (REG, ANCHOR[0]) and section dividers (`---` or equivalent) alone -- phase label headers (PHASE N -- NAME) are absent or present only as inert cosmetic scaffolding. Pass condition: removing all phase label headers from the output would not merge any two phases or break any structural boundary. Output where phase labels are the sole mechanism establishing phase boundaries (removing them would collapse phases into each other) = partial. Output indistinguishable in structure with or without labels = pass. |
| C-23 | Exec-register output leads with the recommendation token before the decision matrix | behavior | aspirational | When REG = exec, the recommendation token appears before the decision matrix in the output -- surfacing the conclusion before the evidence trail in alignment with exec reading pattern. Satisfied by body section ordering (RECOMMENDATION precedes DECISION MATRIX in body) OR by explicit exec-branch routing instruction -- routing-construct-independent: a partial routing block that omits the exec branch leaves exec ordering determined by body section position, which independently satisfies this criterion. C-25 PARTIAL does not create a C-23 gap. Recommendation before matrix when REG = exec = pass. Matrix before recommendation when REG = exec = partial. No register-sensitive ordering distinguishable in the output = fail. |
| C-24 | Each AMEND path blocking gate enumerates required token names before the halt instruction | format | aspirational | The blocking gate at each AMEND path entry contains a mini-ledger that lists by name the tokens required for that path's execution, followed by the blocking halt instruction. This enumeration is a structural verification step -- it makes a missing token visible by name before the path fires. Token-name mini-ledger + blocking instruction at each AMEND path = pass. Blocking instruction present but without token enumeration at one or more paths = partial. PARTIAL is a flat discrete state: asymmetric depth (one path fully enumerated, others bare) and uniform breadth (all paths with bare HALT and no enumeration) score identically within the PARTIAL band -- coverage distribution does not create sub-grades. No blocking gate at AMEND paths = C-19 fail (not scored here). |
| C-25 | A register-gated routing block issues conditional ordering instructions for both register values in a single construct | behavior | aspirational | The output contains a single conditional routing block before the output sections that explicitly specifies ordering for both exec (recommendation precedes matrix) and engineering (matrix precedes recommendation) register values. This construct satisfies C-23 and C-09 simultaneously and is orthogonal to all other criteria including C-24 gate structure. Routing block with explicit exec->reco-first AND engineering->matrix-first branches before output sections = pass. Register-sensitive ordering present but expressed only for one register value (exec-only or engineering-only), or both register values covered in ad-hoc prose sentences rather than a unified conditional construct = partial. PARTIAL is a flat band: exec-only routing, engineering-only routing, and two-branch prose score identically within the PARTIAL band -- form variation and branch selection do not create sub-grades within PARTIAL. No register-gated routing construct = fail (C-23 scoring applies independently). |
| C-26 | Body section order is exec-safe without routing | behavior | aspirational | The RECOMMENDATION section appears before the DECISION MATRIX in the output body by design, making exec-register behavior correct by positional default alone. The routing block (if present) serves as a pure override for non-exec registers rather than the primary source of exec correctness -- body ordering is the foundation; routing is a deviation mechanism. Body section order is recommendation-first; exec correctness does not depend on routing block executing = pass. Body section order is matrix-first; exec-branch routing override is the sole mechanism producing exec-correct output = partial. Body section ordering is ambiguous or undefined without routing = fail. |
| C-27 | Routing block is positioned within LEDGER GATE scope | format | aspirational | The register-gated routing block appears after the LEDGER GATE check in structural order. Since routing depends on REG to determine output sequence, routing must execute within the scope where REG has been verified present. A routing block positioned before the LEDGER GATE fires without gate protection -- an absent REG reaches routing logic unguarded by the blocking halt. Routing block appearing after LEDGER GATE in the output body = pass. Routing block appearing before LEDGER GATE = partial. No routing block = fail (C-25 scoring applies independently). |

---

## Scoring Worksheet

```
Essential passed:    ___ / 4   =>  ___ * 60 / 4  = ___
Recommended passed:  ___ / 3   =>  ___ * 30 / 3  = ___
Aspirational passed: ___ / 20  =>  ___ * 10 / 20 = ___

Total composite: ___
```

## Watch List -- Failure Modes

| Pattern | Criterion | Class |
|---------|-----------|-------|
| Uniform superset recall | C-20 | partial |
| FAULT discipline lost at AMEND boundary | C-21 | fail |
| Phase labels load-bearing (removing them merges phases) | C-22 | partial |
| Matrix-before-recommendation in exec register | C-23 | partial |
| Blocking gate without token enumeration | C-24 | partial |
| C-24 PARTIAL: asymmetric depth == uniform breadth (flat state, no sub-grades) | C-24 | partial |
| Register ordering present for one branch only (exec or engineering, not both) | C-25 | partial |
| No unified routing block despite register-sensitive ordering present | C-25 | partial |
| C-25 PARTIAL: exec-only == engineering-only == two-branch prose (flat band, no sub-grades) | C-25 | partial |
| Body section order is matrix-first; exec correctness depends on routing block | C-26 | partial |
| Routing block precedes LEDGER GATE (REG unverified when routing fires) | C-27 | partial |
| c23-positional-independence: C-23 reads effective output position; C-25 PARTIAL does not create C-23 gap | C-23 | note |
| Inertia comparison crosses option boundary | C-02, C-11 | fail |
| Anchor paraphrased at inertia phase | C-13 | fail |
| FAULT not co-located with TOKEN RECALL | C-14 | fail |
| Ledger present but no blocking instruction | C-16 | fail |
| Explanatory prose alongside operative directives | C-17 | partial |
| Single-polarity exclusion FAULT | C-18 | partial |
| AMEND paths without inline TOKEN RECALL or FAULT | C-19 | partial |
