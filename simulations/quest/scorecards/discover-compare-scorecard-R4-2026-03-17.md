---

## discover-compare R4 Scorecard

**Written to**: `simulations/quest/scorecards/discover-compare-scorecard-R4-2026-03-17.md`

### Results

| Rank | Variation | Composite | Golden |
|------|-----------|-----------|--------|
| 1 (tie) | V-02 FAULT Label | **100.00** | YES |
| 1 (tie) | V-03 Compressed | **100.00** | YES |
| 1 (tie) | V-04 Inline Phase 0 | **100.00** | YES |
| 4 (tie) | V-01 Template Anchor Slot | **99.44** | YES |
| 4 (tie) | V-05 Combined | **99.44** | YES |

All five Golden. Projections matched exactly.

### The one failure mode: C-13

`"{insert the exact ANCHOR[0] sentence here}"` (V-01, V-05) is **PARTIAL** — not PASS.

The no-paraphrase mandate must be **co-located inside the TOKEN RECALL directive** at point of use in the inertia phase itself. Putting it in a Phase 0 binding rule preamble or inside a template slot instruction is weaker. V-02/V-03/V-04 all use `{reproduce exact sentence from Phase 0 — do not paraphrase}` directly in the recall line — that is what passes.

### Key confirmations

- **C-14 label-flexible**: `FAULT:` = `VIOLATION:` = `SCORING DEFECT:`. Any named class co-located with TOKEN RECALL satisfies it.
- **C-03 compression-safe**: V-03 strips ~50% of words and still hits 9/9. Explanatory prose (rule tables, binding sentences, Print: confirmations) is overhead.
- **C-15 ordering-sufficient**: Inline Phase 0 (V-04) passes — physical REG-before-ANCHOR[0] token ordering is enough. The Part A/Part B split was defensive.
- **V-05 interaction-safe**: All four simplifications combined; C-13 remains the only partial. No adverse interactions.

### Minimal viable 100/100 candidate

V-05 + replace the blockquote template slot with:
```
TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 — do not paraphrase}`
```
Yields: compressed + inline Phase 0 + FAULT label + verbatim recall at point of use. Projected 100.00.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["no-paraphrase mandate must be co-located in the TOKEN RECALL directive at point of use, not in a preamble or template slot", "failure class label is flexible — any named class (FAULT, VIOLATION, SCORING DEFECT) satisfies C-14 when co-located with TOKEN RECALL", "explanatory prose is structural overhead — operative directives alone achieve 9/9 aspirational at ~50% word count", "physical token ordering satisfies register-before-anchor (C-15) without a precondition label or Part A/Part B structural split"]}
```
verbatim anchor recall** | **PARTIAL** | PASS | PASS | PASS | **PARTIAL** |
| C-14 failure class co-located | PASS | PASS | PASS | PASS | PASS |
| C-15 register before anchor | PASS | PASS | PASS | PASS | PASS |
| C-16 blocking ledger gate | PASS | PASS | PASS | PASS | PASS |

---

## Criterion-Level Evidence Notes

### C-08 (Option 0 in matrix)
All: Phase 6 matrix has "Option 0: ANCHOR[0]" as named column header with Inertia row
labeled "this IS the anchor." PASS across all.

### C-09 (audience primary flow)
All: REG token declared in Phase 0. All analysis phases labeled "REG-framed." Phase 8
recalls REG token and applies register-specific recommendation framing. V-03 strips register
rule descriptions but preserves the REG token directive and Phase 8 recall — the operative
mechanism is intact. PASS.

### C-10 (token ledger)
All: Phase 5 LEDGER GATE lists all 10 named tokens with checkboxes. Phase 6 states
"Assemble from LEDGER GATE tokens." Named token cross-reference is structural. PASS.

### C-11 (explicit exclusion rule)
All: Each inertia phase has an explicit "not whether they prefer A over B" prohibition.
V-01/V-03/V-04 use VIOLATION:; V-02/V-05 use FAULT:. All labels are co-located with
TOKEN RECALL. PASS.

### C-12 (named anchor before analysis)
All: ANCHOR[0] token is declared in Phase 0 as a named slot before Phase 1A. Subsequent
phases reference ANCHOR[0] by name. PASS.

### C-13 (verbatim anchor recall) — DISCRIMINATING CRITERION

**V-01 / V-05 — PARTIAL**

Inertia phases use a blockquote template slot:
```
TOKEN RECALL — paste exact text of ANCHOR[0]:
> ANCHOR[0]: "{insert the exact ANCHOR[0] sentence here}"
```
The instruction "insert the exact sentence" is inside a fill-in slot. "Exact" is present
but the no-paraphrase mandate is not co-located with the TOKEN RECALL directive itself:
- In V-01, "do not rephrase or shorten" appears only in Phase 0's binding rule — not at
  the recall step in Phase 2.
- In V-05, even the Phase 0 binding rule is stripped (compressed); "do not paraphrase"
  appears only in Phase 8's TOKEN RECALL, not in Phase 2A/2B.

C-13 pass condition requires that baseline drift be detectable as a token mismatch. A
template slot with "exact" is structurally ambiguous — stronger than a bare name reference,
weaker than a recall directive that says "do not paraphrase." PARTIAL.

**V-02 / V-03 / V-04 — PASS**

TOKEN RECALL at Phase 2A/2B uses:
```
TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 — do not paraphrase}`
```
The no-paraphrase mandate is inside the recall directive at point of use. Any paraphrase is
detectable as a token mismatch against a directive that specified exact reproduction. PASS.

### C-14 (failure class co-located) — LABEL FLEXIBILITY CONFIRMED

**V-01 / V-03 / V-04**: `VIOLATION: ... is an error` — PASS.
**V-02 / V-05**: `FAULT: ... is a fault` — PASS.

C-14 is label-agnostic: VIOLATION:, FAULT:, and SCORING DEFECT: all satisfy the criterion.
The discriminating element is co-location with the TOKEN RECALL step, not the label word.

### C-15 (register before anchor) — ORDERING CONFIRMED SUFFICIENT

**V-01 / V-02 / V-03**: Part A / Part B split with "commit first, before anchor" label. PASS.

**V-04 / V-05**: Inline Phase 0 — single block. REG token slot appears physically before
ANCHOR[0] token slot. "Declare audience register, then commit status quo anchor framed for
that register" implies ordering without a structural precondition label. Physical ordering
alone satisfies C-15. The Part A / Part B split is confirmed defensive. PASS.

### C-16 (blocking ledger gate)
All: Phase 5 ends with "HALT — do not proceed to Phase 6 if any token is absent." PASS.

---

## Scoring Worksheet

| Variation | Essential (4) | Recommended (3) | Aspirational (/9) | Composite | Golden |
|-----------|--------------|-----------------|-------------------|-----------|--------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 8.5/9 = 9.44 | **99.44** | YES |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 9/9 = 10.00 | **100.00** | YES |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 9/9 = 10.00 | **100.00** | YES |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 9/9 = 10.00 | **100.00** | YES |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 8.5/9 = 9.44 | **99.44** | YES |

*Partial = 0.5. Aspirational: passed_count * 10 / 9.*

---

## Key Findings

### Finding 1 — C-13: No-paraphrase mandate must be co-located at the TOKEN RECALL step
Template slot `"{insert the exact ANCHOR[0] sentence here}"` is PARTIAL. The "do not
paraphrase" mandate must be **inside the TOKEN RECALL directive at point of use** in the
inertia phase itself — not in a Phase 0 binding rule preamble and not in a fill-in
template instruction. Moving the constraint upstream weakens enforceability.

### Finding 2 — C-14: Label-flexible; any named failure class satisfies it
FAULT:, VIOLATION:, and SCORING DEFECT: all pass C-14. The label word carries no semantic
weight beyond naming a failure class. Structural requirement: (1) a named label, (2)
co-located with TOKEN RECALL, (3) prohibition stated as a class.

### Finding 3 — C-03/V-03: Explanatory prose is overhead, not load-bearing
Compressed V-05 (~50% word reduction) strips register rule tables, binding sentences,
Print: confirmations, and conditional framing guidance — and achieves 9/9 aspirational.
Load-bearing elements: operative token directives, phase ordering, TOKEN RECALL +
VIOLATION/FAULT pair, HALT instruction. Compressed is the preferred form.

### Finding 4 — C-15/V-04: Physical token ordering satisfies register-before-anchor
Inline Phase 0 (no Part A / Part B split, no "commit first" label) passes C-15. The REG
token slot preceding the ANCHOR[0] token slot in a single phase block is sufficient.
The precondition label was defensive scaffolding, not a structural requirement.

### Finding 5 — V-05 combined: Simplifications are independently safe
In V-05 (all four simplifications at once), C-13 remains the only PARTIAL — identical to
V-01 alone. Label change, compression, and inline Phase 0 do not interact adversely.

---

## Minimal Viable 100/100 Prompt (R4 Conclusion)

**V-05 with one fix**: replace the Phase 2A / 2B template slot with the TOKEN RECALL
directive form:

```
TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 — do not paraphrase}`
FAULT: Comparing Option A against Option B at this phase is a fault — inertia asks whether
teams would keep the status quo recalled above rather than build Option A, not whether they
prefer A over B.
```

This yields: **compressed + inline Phase 0 + FAULT label + verbatim recall mandate at
point of use**. Projected composite: 100.00.

Characteristics vs. R3-V05: ~50% shorter, single Phase 0 block, any named failure class
label acceptable, no binding rule preamble required.

---

## Excellence Signals from Top-Scoring Variations (V-02, V-03, V-04)

1. **No-paraphrase mandate at the TOKEN RECALL directive, not upstream** — the directive
   that produces the reproduction must contain the constraint on that reproduction;
   preamble binding rules and template slot instructions are weaker.

2. **Label flexibility: any named failure class satisfies C-14** — FAULT:, VIOLATION:,
   SCORING DEFECT: are structurally equivalent; co-location with TOKEN RECALL is the
   criterion, not the label word.

3. **Operative directives alone are sufficient; explanatory prose is overhead** — V-03
   proves the register rule table, binding sentences, Print confirmations, and conditional
   framing tables are not load-bearing for 9/9 aspirational coverage.

4. **Physical token ordering satisfies register-before-anchor without a structural split**
   — V-04 proves C-15 is an ordering criterion: REG token must precede ANCHOR[0] token;
   the labeling mechanism that achieves this order is not required.

---

## Projection Accuracy

All five projections matched actuals exactly. Single-axis isolation correctly predicted
that C-13 was the only affected criterion for V-01, that all other simplifications were
independently safe, and that V-05 would carry V-01's C-13 PARTIAL forward without
additional degradation.
