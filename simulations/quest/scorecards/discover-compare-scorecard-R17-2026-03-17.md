## discover-compare R17 Scorecard

**Rubric v15 | Denominator: /29**

| Variation | Axis | Composite | Golden |
|-----------|------|-----------|--------|
| V-01 | Baseline (R16 carry) | **99.31** | No |
| V-02 | C-35 only — positional HALT | **99.66** | No |
| V-03 | C-36 only — DEVIATION: marker | **99.66** | No |
| V-04 | C-35 + C-36 combined | **100.00** | YES |
| V-05 | Form variant — "any listed" + OVERRIDE: | **100.00** | YES |

**All essential pass: YES** (C-01 to C-04, all variations)

**Key criterion verdicts:**

**C-35** (positional reference HALT):
- V-01/V-03 FAIL — "any Add-C token is absent" (category) and "ledger incomplete" (completeness state) are semantic references, not positional anchors
- V-02/V-04 PASS — "any of the above tokens is absent" uses "above" as positional anchor to the preceding fenced-code block
- V-05 PASS — "any listed token is absent" is rubric-cited equivalent form; confirmed form-neutral

**C-36** (deviation marker at branch-instruction level):
- V-01/V-02 FAIL — routing branch has no DEVIATION:/OVERRIDE: prefix; role only recoverable from C-32 scope header
- V-03/V-04 PASS — `DEVIATION: if REG = engineering or general...` marker present at branch line; orthogonal to C-31 ("precedes") and C-32 scope
- V-05 PASS — OVERRIDE: confirmed equivalent to DEVIATION:

**Excellence signals:**
1. `positional-reference-halt-makes-enumeration-block-revisable-c35` — "any of the above" / "any listed" decouples HALT from token identity; enumeration block and HALT become independently revisable components
2. `deviation-marker-at-branch-instruction-level-orthogonal-to-positional-vocabulary-c36` — DEVIATION:/OVERRIDE: identifies branch role at the branch line; orthogonal to C-31 ordering vocabulary and C-32 scope declaration; additive, not substitutive

```json
{"top_score": 100.00, "all_essential_pass": true, "new_patterns": ["positional-reference-halt-makes-enumeration-block-revisable-c35", "deviation-marker-at-branch-instruction-level-orthogonal-to-positional-vocabulary-c36"]}
```
istinct from RISK-A or explain overlap. REG-framed." at RISK-B |
| C-07 actionable AMEND | PASS | PASS | PASS | PASS | PASS | Three concrete amendment paths: Add Option C, Weight {dimension}, Override register |

**Recommended subtotal: 3/3 = 30.00 (all variations)**

---

## Aspirational Criteria -- Stable across all variations (C-08 to C-34)

These 27 criteria are structurally identical across all five variations. All PASS.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-08 Option 0 in matrix | PASS | Column header: "Option 0: ANCHOR[0]" in decision matrix |
| C-09 audience register in primary flow | PASS | ROUTING block handles engineering register in main flow; "Apply REG column-label overrides if exec or engineering" in output body; REG-framed throughout |
| C-10 token ledger cross-check | PASS | RECOMMENDATION: TOKEN RECALL x2 (ANCHOR[0], REG); "Assemble from LEDGER GATE tokens" at matrix assembly |
| C-11 explicit exclusion rule | PASS | "FAULT: compare against ANCHOR[0] only -- Option A vs Option B comparison is an error." at each inertia site |
| C-12 named anchor before analysis | PASS | ANCHOR[0] declared as named token + section divider before first analysis token (FEAS-A) |
| C-13 verbatim anchor recall | PASS | "TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from above -- do not paraphrase}`" co-located at each inertia site; no-paraphrase mandate inline at point of use |
| C-14 failure class co-located | PASS | FAULT: label co-located with TOKEN RECALL at each inertia site |
| C-15 register before anchor | PASS | REG token declared before ANCHOR[0] in structural order |
| C-16 blocking ledger gate | PASS | "HALT -- do not proceed if any token is absent." in LEDGER GATE |
| C-17 output compressed | PASS | All directives operative: token declarations, recall instructions, FAULT prohibitions, blocking gates. No binding rationale tables or preamble framing |
| C-18 dual-polarity FAULT | PASS | "FAULT: compare against ANCHOR[0] only -- Option A vs Option B comparison is an error." -- positive mandate + negative prohibition in one line |
| C-19 AMEND self-contained | PASS | All three AMEND paths carry TOKEN RECALL + FAULT inline |
| C-20 path-scoped TOKEN RECALL | PASS | Add-C and Weight recall ANCHOR[0] only; Override recalls REG only (correct exclusion -- register path does not involve status-quo evaluation) |
| C-21 dual-polarity FAULT in AMEND | PASS | Add-C: "compare against ANCHOR[0] only -- Option C vs A or B comparison is an error." Weight: "apply multiplier to dimension scores only -- do not revise token values." Override: "register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0]." All dual-polarity |
| C-22 phase structure via tokens + dividers | PASS | Phase separation via --- dividers and operative token positioning; no phase label headers whose removal would collapse boundaries |
| C-23 exec leads with recommendation | PASS | RECOMMENDATION before DECISION MATRIX in body; exec correctness by positional default |
| C-24 AMEND path token enumeration | PASS | All three paths: fenced-code block with named tokens precedes HALT |
| C-25 register-gated routing block | PASS | Engineering/general branch in routing block (established R16 forward; exec handled by body order) |
| C-26 body section order exec-safe | PASS | RECOMMENDATION precedes DECISION MATRIX in body; exec correctness does not depend on routing |
| C-27 routing block within LEDGER GATE scope | PASS | Routing block appears after LEDGER GATE in structural order |
| C-28 body-order and routing-scope isolated | PASS | BODY ORDER directive and routing block structurally separate; neither references the other |
| C-29 BODY ORDER unconditional | PASS | "BODY ORDER: RECOMMENDATION precedes DECISION MATRIX in all outputs." -- unconditional single-clause directive |
| C-30 routing handles only deviation | PASS | Routing block contains only engineering deviation branch; no exec branch; BODY ORDER handles exec independently |
| C-31 routing vocabulary positionally descriptive | PASS | "DECISION MATRIX precedes RECOMMENDATION" -- positional vocabulary only; no structural layer names |
| C-32 routing scope declared deviation-only | PASS | "ROUTING: deviation from BODY ORDER only." scope header present and structurally distinct from branch instruction |
| C-33 BODY-ORDER-LAYER activation token | PASS | "Token: `BODY-ORDER-LAYER: active`" as discrete standalone declaration |
| C-34 AMEND enumeration in separable block | PASS | All three paths: fenced-code block precedes HALT; HALT sentence does not embed token names inline |

**C-34 per-path detail:**
- Add-C: `Add-C ledger: FEAS-C [ ]  INERT-C [ ]  RISK-C [ ]  COMP-C [ ]` (fenced-code) → HALT "do not extend matrix if any Add-C token is absent." Category reference in HALT but block is separable. C-34 PASS.
- Weight: `Weight ledger: ANCHOR[0] [ ]  WEIGHT [ ]` (fenced-code) → HALT "do not re-score if ledger incomplete." Completeness reference; block separable. C-34 PASS.
- Override: `Override ledger: REG [ ]  REG-override [ ]` (fenced-code) → HALT "do not re-render if ledger incomplete." Completeness reference; block separable. C-34 PASS.

---

## Aspirational Criteria -- Discriminating (C-35 and C-36)

### C-35: HALT uses positional reference to enumeration block

**V-01 -- FAIL**
- Add-C HALT: "do not extend matrix if any **Add-C token** is absent." -- category name inline; not positional reference
- Weight HALT: "do not re-score if **ledger incomplete**." -- completeness state; no positional anchor
- Override HALT: "do not re-render if **ledger incomplete**." -- completeness state; no positional anchor
- All three HALTs use semantic references (what tokens mean / their completion state), not positional anchors to the preceding block.

**V-02 -- PASS**
- Add-C HALT: "do not extend matrix if any **of the above tokens** is absent." -- "above" is positional anchor to preceding fenced-code block
- Weight HALT: "do not re-score if any **of the above tokens** is absent." -- positional anchor
- Override HALT: "do not re-render if any **of the above tokens** is absent." -- positional anchor
- All three HALTs use "any of the above tokens" -- positional reference, no inline token names.

**V-03 -- FAIL**
- AMEND HALTs unchanged from V-01. "any Add-C token is absent." / "ledger incomplete." -- no positional reference.

**V-04 -- PASS**
- All three HALTs: "do not [action] if any of the above tokens is absent." -- positional anchor in all three paths.

**V-05 -- PASS**
- Add-C HALT: "do not extend matrix if any **listed token** is absent." -- "listed" references the enumeration as a listing artifact (rubric explicitly cites "any listed token is missing" as equivalent form)
- Weight HALT: "do not re-score if any **listed token** is absent." -- positional anchor
- Override HALT: "do not re-render if any **listed token** is absent." -- positional anchor
- All three use "any listed token" -- rubric-cited equivalent form satisfies C-35.

---

### C-36: Engineering routing branch carries a named deviation marker

**Gate condition**: C-32 is PASS for all variations (scope declaration present). C-36 is scored for all.

**V-01 -- FAIL**
- Routing: `if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.`
- No deviation marker at branch-instruction level. Branch role legible only from C-32 scope declaration header, not from branch line itself.

**V-02 -- FAIL**
- Routing unchanged from V-01. No DEVIATION:/OVERRIDE: marker.

**V-03 -- PASS**
- Routing: `DEVIATION: if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.`
- DEVIATION: marker present at branch-instruction level, preceding the conditional clause.
- C-31 preserved: "precedes" is positional vocabulary; DEVIATION: is a role label, not a structural layer name.
- C-32 preserved: scope declaration "ROUTING: deviation from BODY ORDER only." unchanged.
- C-30 preserved: no exec branch added.

**V-04 -- PASS**
- Routing: `DEVIATION: if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.` -- same DEVIATION: marker as V-03. All preservation checks pass.

**V-05 -- PASS**
- Routing: `OVERRIDE: if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.`
- OVERRIDE: is listed as explicit equivalent to DEVIATION: in the C-36 rubric ("DEVIATION:, OVERRIDE:, EXCEPTION:, or equivalent label").
- C-31 preserved: "precedes" is positional vocabulary; OVERRIDE: is a role label.
- C-32 preserved: scope declaration unchanged.

---

## Aspirational subtotals

| Variation | C-35 | C-36 | Passing / Denom | Aspirational % |
|-----------|------|------|-----------------|---------------|
| V-01 | FAIL | FAIL | 27 / 29 | 9.310 |
| V-02 | PASS | FAIL | 28 / 29 | 9.655 |
| V-03 | FAIL | PASS | 28 / 29 | 9.655 |
| V-04 | PASS | PASS | 29 / 29 | 10.000 |
| V-05 | PASS | PASS | 29 / 29 | 10.000 |

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | Composite |
|-----------|-----------|-------------|-------------|-----------|
| V-01 | 60.00 | 30.00 | 9.310 | **99.31** |
| V-02 | 60.00 | 30.00 | 9.655 | **99.66** |
| V-03 | 60.00 | 30.00 | 9.655 | **99.66** |
| V-04 | 60.00 | 30.00 | 10.000 | **100.00** |
| V-05 | 60.00 | 30.00 | 10.000 | **100.00** |

---

## Variation ranking

1. V-04 -- 100.00 (golden, primary)
1. V-05 -- 100.00 (golden, form-neutrality confirmed)
3. V-02 -- 99.66 (C-35 established independently)
3. V-03 -- 99.66 (C-36 established independently)
5. V-01 -- 99.31 (baseline; R16 golden body does not satisfy v15 ceiling)

---

## Golden variations

**V-04** (primary golden -- DEVIATION: + "any of the above"):
Confirms C-35 and C-36 are the complete and sufficient delta between R16 ceiling (99.31 under v15) and v15 ceiling (100.00). Both additions are structurally independent -- AMEND HALT changes and routing branch changes operate in different sections with no overlap.

**V-05** (form-neutrality golden -- OVERRIDE: + "any listed token"):
Confirms rubric form-neutrality claims for both new criteria. "any listed token is absent" satisfies C-35 equivalently to "any of the above tokens is absent" -- "listed" is a positional anchor to the enumeration as a listing artifact. OVERRIDE: satisfies C-36 equivalently to DEVIATION: -- both are valid marker labels per rubric. No boundary narrowing at either criterion.

---

## Excellence signals

### Signal 1: `positional-reference-halt-makes-enumeration-block-revisable-c35`

The HALT instruction in each AMEND path uses "any of the above tokens is absent" or "any listed token is absent" -- a positional anchor that references the preceding enumeration block as a unit rather than naming specific tokens. This decouples the HALT sentence from token identity: the enumeration block can be revised (tokens added, removed, renamed) without touching the HALT text. The fenced-code block and the HALT become independently revisable components.

Contrast with V-01: "any Add-C token is absent" names a category; "ledger incomplete" names a completion state. Both are semantic references (what tokens mean / their state) rather than positional references (where they are listed). When token names change, the HALT must be rewritten. The C-34 block is present and separable, but the HALT is not yet the structural complement to the block.

**Diagnostic**: HALT with category/completeness reference: C-24 PASS + C-34 PASS + C-35 FAIL. C-35 is the tier above C-34 -- C-34 establishes that block and HALT are separable; C-35 establishes that the HALT actively links to the block via positional language.

### Signal 2: `deviation-marker-at-branch-instruction-level-orthogonal-to-positional-vocabulary-c36`

The engineering routing branch in V-04/V-05 carries DEVIATION: or OVERRIDE: as a prefix to the conditional clause. This makes the branch's non-default role legible at branch-instruction level: a reader scanning the routing block sees "DEVIATION:" immediately, without needing to consult the C-32 scope declaration header. The marker identifies branch role; positional vocabulary ("precedes") identifies section ordering. The two are orthogonal and non-interfering.

Contrast with V-01/V-02: `if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.` -- the branch's deviation status is implied by C-32 scope but not visible at the branch line itself.

**Orthogonality confirmed by V-03**: Adding DEVIATION: to routing carries all 27 prior criteria at PASS. DEVIATION: is additive at the branch-instruction level -- it does not modify C-31 ordering vocabulary, C-32 scope declaration, or C-30 deviation-only constraint.

---

## Discriminating question resolutions

**v15 gap above R16 ceiling confirmed**: V-01 carries R16 golden body verbatim. Under v15: C-35 FAIL + C-36 FAIL = 27/29 = 99.31. The R16 golden body does not satisfy v15 ceiling.

**C-35 independently achievable (V-02)**: Changing only the three AMEND HALTs to positional reference form produces 28/29 = 99.66. No other criterion affected. C-35 mechanism is isolated to HALT text.

**C-36 independently achievable (V-03)**: Adding only DEVIATION: to the routing branch produces 28/29 = 99.66. C-31, C-32, C-30 all preserved -- orthogonality confirmed.

**C-35 + C-36 complete the delta (V-04)**: Both changes together produce 29/29 = 100.00. No other criterion affected. Two mechanisms operate in different sections of the skill body -- no structural overlap.

**C-35 form-neutrality confirmed (V-05 "any listed token")**: Scores equivalently to "any of the above tokens is absent." No boundary narrowing -- "listed" as positional anchor satisfies C-35 as specified.

**C-36 marker-label neutrality confirmed (V-05 OVERRIDE:)**: Scores equivalently to DEVIATION:. No boundary narrowing.

---

## Watch list carried forward

| Entry | Description |
|-------|-------------|
| `c35-positional-reference-halt` | "any of the above tokens is absent" / "any listed token is absent" satisfy C-35; category references ("any Add-C token") and completeness references ("ledger incomplete") do not |
| `c35-c34-tier-relationship` | C-34 (separable block) is prerequisite for C-35 (positional reference in HALT); C-35 is the tier above C-34 -- C-24 PASS + C-34 PARTIAL gates out C-35 |
| `c36-deviation-marker-at-branch-level` | DEVIATION: / OVERRIDE: / EXCEPTION: at branch-instruction line; C-32 scope-level declaration is necessary but not sufficient for C-36 |
| `c36-orthogonal-to-c31-and-c32` | DEVIATION: marker is a role label; "precedes" is positional vocabulary; "ROUTING: deviation..." is scope declaration -- three independent mechanisms, no interaction |
| `c36-c32-gate-relationship` | C-36 only scored when C-32 PASS; C-32 N/S excludes C-36 |
| `c34-form-agnostic-confirmed` | fenced-code = indented-list for C-34; separability is the mechanism (confirmed R16) |
| `inline-within-halt-c24-pass-c34-partial-boundary` | Token names embedded inside HALT sentence: C-24 PASS + C-34 PARTIAL + C-35 not scored |
