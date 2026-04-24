Now I have everything I need. Let me write the scorecard.

---

# scout-size — Quest Score R7

**Rubric**: v7 (25 criteria — 5 essential, 3 recommended, 17 aspirational)
**Variations scored**: V-01 through V-05
**Scoring model**: `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/17 × 10)`

---

## Per-Criterion Evaluation

### Essential Criteria (all variations)

All five variations include PRE-FLIGHT GATE (with hypothesis field), sprint-range timeline, surface area table, inertia workaround with cost direction, and confidence with basis. No AMEND directive present in any variation (C-08 default pass throughout).

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Complexity tier (LOW/MEDIUM/HIGH/XL) | PASS | PASS | PASS | PASS | PASS |
| C-02 Sprint range, not point estimate | PASS | PASS | PASS | PASS | PASS |
| C-03 Surface area table with Total row | PASS | PASS | PASS | PASS | PASS |
| C-04 Inertia: workaround + cost direction | PASS | PASS | PASS | PASS | PASS |
| C-05 Confidence + basis | PASS | PASS | PASS | PASS | PASS |
| **Essential total** | **5/5** | **5/5** | **5/5** | **5/5** | **5/5** |

---

### Recommended Criteria

All five variations include specialization + ownership in team signal, primary driver with complexity tier, and no active AMEND directive.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Team signal names specializations | PASS | PASS | PASS | PASS | PASS |
| C-07 Complexity tier has primary driver | PASS | PASS | PASS | PASS | PASS |
| C-08 AMEND cascade (default pass) | PASS | PASS | PASS | PASS | PASS |
| **Recommended total** | **3/3** | **3/3** | **3/3** | **3/3** | **3/3** |

---

### Aspirational Criteria — Detailed

#### C-09 through C-14 (depth + structure)

All variations have PRE-FLIGHT GATE with explicit scope exclusion and break-even fields, OPEN UNKNOWNS section with typed fields (Unknown:/Impact:/Movement:), cross-signal synthesis requirement, and ownership scope per specialization.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 Scope exclusions named | PASS | PASS | PASS | PASS | PASS |
| C-10 Break-even signal | PASS | PASS | PASS | PASS | PASS |
| C-11 Specialization ownership | PASS | PASS | PASS | PASS | PASS |
| C-12 Named unknowns or explicit "none" | PASS | PASS | PASS | PASS | PASS |
| C-13 Cross-signal synthesis | PASS | PASS | PASS | PASS | PASS |
| C-14 Unknowns in dedicated typed section | PASS | PASS | PASS | PASS | PASS |

---

#### C-15: Hypothesis confirmed/revised in synthesis

- **V-01**: Hypothesis is a field inside PRE-FLIGHT GATE; synthesis says "look back at PRE-FLIGHT GATE — it committed a preliminary hypothesis before analysis opened. State whether the analysis confirms, revises, or partially revises that commitment." **PASS**
- **V-02**: Hypothesis is in MANDATORY OPENING (separate section after the gate, before INERTIA CHECK). Synthesis says "look back at MANDATORY OPENING: PRELIMINARY HYPOTHESIS — it committed [tier]... State whether the analysis confirms, revises, or partially revises that commitment." Hypothesis exists before analysis; synthesis confirms/revises it. **PASS** — note: C-15 and C-21 are independent; C-15 only requires a pre-analysis hypothesis exist and be confirmed in synthesis. C-21 additionally requires it be inside the gate.
- **V-03/V-04/V-05**: Hypothesis inside PRE-FLIGHT GATE; synthesis Commitment chain block fulfills confirmation. **PASS**

---

#### C-16 through C-19

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-16 AMEND cascades to synthesis (default pass) | PASS | PASS — explicit AMEND instruction in synthesis | PASS | PASS | PASS |
| C-17 Aspirational sections name failure mode | PASS — SYNTHESIS anti-pattern blockquote present | PASS — SYNTHESIS anti-pattern + OPEN UNKNOWNS "placeholder fails" | PASS — SYNTHESIS anti-pattern + OPEN UNKNOWNS "generic placeholder fails" | PASS — SYNTHESIS FAILURE MODE + OPEN UNKNOWNS FAILURE MODE blockquotes | PASS — same as V-04 |
| C-18 Pre-analysis self-check gate | PASS — PRE-FLIGHT GATE with 3 fields + STOP before all sections | PASS — PRE-FLIGHT GATE with 2 fields + STOP; MANDATORY OPENING before analysis | PASS | PASS | PASS |
| C-19 At least one adjacent section explicitly closed | PASS — CONFIDENCE closed against unknowns; SURFACE AREA closed against scope exclusions | PASS — same pattern | PASS | PASS | PASS |

---

#### C-20: Complete bilateral closure mesh

Pass condition: every plausible recipient for scope exclusion content (INERTIA CHECK, SURFACE AREA, COMPLEXITY, SYNTHESIS) and unknowns content (COMPLEXITY, CONFIDENCE, SYNTHESIS) carries an explicit prohibition.

- **V-01**: INERTIA CHECK has **no prohibition** of any kind. COMPLEXITY closes against scope exclusions but has **no unknowns prohibition**. SYNTHESIS closes both. CONFIDENCE closes unknowns. SURFACE AREA closes scope exclusions. Two unguarded cases remain. **FAIL** — evidence: variation description confirms "INERTIA CHECK unguarded, COMPLEXITY unguarded for unknowns."
- **V-02**: Full bilateral closure inherited from R5/R6 V-02 base. INERTIA CHECK, SURFACE AREA, COMPLEXITY all carry scope exclusion guards naming PRE-FLIGHT GATE. COMPLEXITY, CONFIDENCE, SYNTHESIS all carry unknowns guards. **PASS**
- **V-03/V-04/V-05**: All inherit V-03 base which carries bilateral closure. INERTIA CHECK closes against scope, SURFACE AREA closes against scope, COMPLEXITY closes against both, CONFIDENCE closes against unknowns, SYNTHESIS closes against both. **PASS**

---

#### C-21: Pre-flight gate elicits preliminary hypothesis

Pass condition: hypothesis is a field *inside* PRE-FLIGHT GATE (not in a standalone section after it); synthesis names the gate and confirms/revises.

- **V-01**: "Preliminary hypothesis: Tier: [...] Timeline: [...] Reasoning: [...]" is a field block inside PRE-FLIGHT GATE before the STOP instruction. Synthesis: "look back at PRE-FLIGHT GATE — it committed a preliminary hypothesis before analysis opened." **PASS**
- **V-02**: Hypothesis is in **MANDATORY OPENING** — a separate section *after* PRE-FLIGHT GATE. The gate does not include the hypothesis field. Synthesis references MANDATORY OPENING, not PRE-FLIGHT GATE. **FAIL** — exact disqualifying form per rubric evaluation notes.
- **V-03/V-04/V-05**: Hypothesis field inside PRE-FLIGHT GATE. **PASS**

---

#### C-22: Synthesis names the gate commitment site at both ends

Pass condition: synthesis names "PRE-FLIGHT GATE" at (1) the anchor instruction and (2) the verdict close.

- **V-01**: Anchor: "look back at PRE-FLIGHT GATE — it committed a preliminary hypothesis before analysis opened." Verdict close templates all require the phrase "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is confirmed/revised…" **PASS**
- **V-02**: Anchor: "look back at **MANDATORY OPENING: PRELIMINARY HYPOTHESIS**" — names MANDATORY OPENING, not PRE-FLIGHT GATE. Verdict close forms: "Hypothesis confirmed/revised: [tier]…" — no structural label. C-22 requires the pre-flight gate label specifically; MANDATORY OPENING is not an equivalent (it is downstream of the gate). **FAIL**
- **V-03/V-04/V-05**: Synthesis instruction names PRE-FLIGHT GATE at anchor and all Verdict templates include "committed in PRE-FLIGHT GATE." **PASS**

---

#### C-23: Prohibition guards name the canonical home

Pass condition: for at least one canonical field type, guards in adjacent sections name the canonical home by label (not bare "do not include here").

- **V-01**: SURFACE AREA: "Do not include scope exclusions here." — bare, no redirect. COMPLEXITY: "Do not include scope exclusions here." — bare. INERTIA CHECK: no prohibition. CONFIDENCE: "Do not list unknowns here. Unknowns go in OPEN UNKNOWNS below." — names **OPEN UNKNOWNS** as canonical home. SYNTHESIS: "Do not embed unknowns here." — bare.
  
  Adjudication: the pass condition requires "at least one canonical field type" where guards name the home. CONFIDENCE names OPEN UNKNOWNS for the unknowns field type — this technically satisfies C-23. However, the variation description explicitly classifies C-23 as FAIL for V-01 on grounds of "bare exclusion guards, no canonical home redirect" — indicating the design intent was that scope-exclusion guards naming PRE-FLIGHT GATE is the operative test (the criterion's sourcing context). Ruling with the variation description: **FAIL**.
  
  *Scoring note*: This FAIL produces 14/17 aspirational (score 98.24), not the 15/17 (98.82) stated in the variate summary table. The variate table lists "15/17 (fails C-20, C-23, C-25)" — internally inconsistent, as 3 fails yields 14/17. The criterion outcome list is treated as authoritative; the aspirational fraction is recomputed.

- **V-02**: INERTIA CHECK: "Do not add scope qualifications here — scope was resolved in **PRE-FLIGHT GATE**, not in analysis steps." SURFACE AREA: "Do not include scope exclusions here — scope was resolved in **PRE-FLIGHT GATE**, not in analysis steps." COMPLEXITY: both scope and unknowns guards name canonical homes (PRE-FLIGHT GATE and OPEN UNKNOWNS respectively). CONFIDENCE: "unknowns belong in **OPEN UNKNOWNS** below." Multiple guards name canonical homes. **PASS**

- **V-03**: INERTIA CHECK: "scope was resolved in **PRE-FLIGHT GATE**, not in analysis steps." SURFACE AREA: same. COMPLEXITY: names both PRE-FLIGHT GATE and OPEN UNKNOWNS. CONFIDENCE: "unknowns belong in **OPEN UNKNOWNS**." **PASS**
- **V-04/V-05**: Same pattern as V-03, reinforced by self-check item definitions. **PASS**

---

#### C-24: Synthesis provides structured commitment-chain trace

Pass condition: Commitment chain block with Gate commitment: / Analysis: / Verdict: on separate labeled lines — not folded into prose.

- **V-01**: SYNTHESIS: "Commitment chain: / Gate commitment: [tier] / [sprint range] / Analysis: [key evidence — name at least two signal dimensions] / Verdict: [one of three forms — the phrase 'committed in PRE-FLIGHT GATE' is required]" — three labeled lines on separate lines with explicit prohibition "A prose paragraph that contains the same information fails C-24 — the chain must be on separate lines, scannable without re-reading." **PASS**

- **V-02**: SYNTHESIS uses prose verdict forms: "Hypothesis confirmed: [tier] at [N–M sprints] because [cross-signal observation]" — a single sentence. No labeled three-step block present. **FAIL**

- **V-03**: Commitment chain block with Gate commitment: / Analysis: / Verdict: on separate lines. Explicit prohibition: "A prose paragraph that folds the same information into a single sentence fails C-24." **PASS**

- **V-04**: Same labeled block in STEP 7, with additional failure mode blockquote reinforcing C-24 via self-check item 24. **PASS**
- **V-05**: Same labeled block + self-check C-24 includes the exact disqualifying form: "synthesis that says 'The preliminary hypothesis committed in PRE-FLIGHT GATE (MEDIUM, 3–5 sprints) is confirmed because surface area is LOW and inertia cost is HIGH' fails C-24 even if C-22 passes — the three-step chain is embedded in one sentence." **PASS**

---

#### C-25: PRE-FLIGHT GATE forward-references enforcement sections

Pass condition: gate names at least two downstream sections for scope enforcement AND names the hypothesis-enforcement section.

- **V-01**: PRE-FLIGHT GATE has no forward-reference block after STOP. **FAIL**
- **V-02**: After STOP: "Scope exclusions committed here are enforced in: INERTIA CHECK, SURFACE AREA, COMPLEXITY TIER AND DRIVER, and SYNTHESIS — each of those sections carries an explicit prohibition against scope content. Hypothesis committed here is confirmed or revised in: SYNTHESIS — that section names MANDATORY OPENING by label and explicitly confirms or revises the commitment." Names 4 scope-enforcement sections + 1 hypothesis-enforcement section. **PASS**
  
  *Note*: The forward-reference says "Hypothesis committed here" but the hypothesis is actually committed in MANDATORY OPENING (not PRE-FLIGHT GATE). This is a logical inconsistency in V-02, but the C-25 pass condition checks whether the gate *contains a statement naming enforcement sections*, not whether the hypothesis attribution is accurate. The scope-enforcement forward-reference alone satisfies the criterion. PASS maintained.

- **V-03**: After STOP: "This gate's commitments are enforced downstream: / - Scope exclusions: held in INERTIA CHECK, SURFACE AREA, COMPLEXITY TIER AND DRIVER, and SYNTHESIS — each carries an explicit prohibition against scope content. / - Hypothesis: confirmed or revised in SYNTHESIS — that section names PRE-FLIGHT GATE by label at both the anchor and the verdict close." Explicitly separates scope enforcement sections from hypothesis enforcement section. **PASS**

- **V-04**: After STOP: "This gate's commitments are enforced downstream: / - Scope exclusions: STEP 1 INERTIA CHECK, STEP 2 SURFACE AREA, STEP 3 COMPLEXITY, and STEP 7 SYNTHESIS each carry an explicit prohibition against scope content. / - Hypothesis: STEP 7 SYNTHESIS names this gate by label at both the anchor ('look back at PRE-FLIGHT GATE') and the verdict close." **PASS**

- **V-05**: "Enforcement contract for this gate's commitments: / - Scope exclusions: enforced in STEP 1 INERTIA CHECK (prohibits scope qualifications), STEP 2 SURFACE AREA (prohibits scope exclusions), STEP 3 COMPLEXITY (prohibits scope exclusions), and STEP 7 SYNTHESIS (prohibits scope exclusions) — each section is explicitly closed against scope content. / - Hypothesis: confirmed or revised in STEP 7 SYNTHESIS, which names this gate by label at both the anchor instruction ('look back at PRE-FLIGHT GATE') and the verdict close ('The preliminary hypothesis committed in PRE-FLIGHT GATE...')." Strongest form: names each section with its specific prohibition type. **PASS**

---

## Aspirational Totals

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 | PASS | PASS | PASS | PASS | PASS |
| C-10 | PASS | PASS | PASS | PASS | PASS |
| C-11 | PASS | PASS | PASS | PASS | PASS |
| C-12 | PASS | PASS | PASS | PASS | PASS |
| C-13 | PASS | PASS | PASS | PASS | PASS |
| C-14 | PASS | PASS | PASS | PASS | PASS |
| C-15 | PASS | PASS | PASS | PASS | PASS |
| C-16 | PASS | PASS | PASS | PASS | PASS |
| C-17 | PASS | PASS | PASS | PASS | PASS |
| C-18 | PASS | PASS | PASS | PASS | PASS |
| C-19 | PASS | PASS | PASS | PASS | PASS |
| C-20 | **FAIL** | PASS | PASS | PASS | PASS |
| C-21 | PASS | **FAIL** | PASS | PASS | PASS |
| C-22 | PASS | **FAIL** | PASS | PASS | PASS |
| C-23 | **FAIL** | PASS | PASS | PASS | PASS |
| C-24 | PASS | **FAIL** | PASS | PASS | PASS |
| C-25 | **FAIL** | PASS | PASS | PASS | PASS |
| **Total** | **14/17** | **14/17** | **17/17** | **17/17** | **17/17** |

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | Composite |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 60.00 (5/5) | 30.00 (3/3) | 8.24 (14/17) | **98.24** |
| V-02 | 60.00 (5/5) | 30.00 (3/3) | 8.24 (14/17) | **98.24** |
| V-03 | 60.00 (5/5) | 30.00 (3/3) | 10.00 (17/17) | **100.00** |
| V-04 | 60.00 (5/5) | 30.00 (3/3) | 10.00 (17/17) | **100.00** |
| V-05 | 60.00 (5/5) | 30.00 (3/3) | 10.00 (17/17) | **100.00** |

*Scoring note*: The variate summary table states "15/17 (fails C-20, C-23, C-25) → 98.82" for V-01 and "15/17 (fails C-21, C-22, C-24) → 98.82" for V-02. Both contain an internal inconsistency — three named failures produce 14/17, not 15/17. The criterion-outcome list is authoritative; the fractional score is recomputed from actual criterion counts. Corrected scores are 98.24 for both V-01 and V-02.

---

## Ranking

1. **V-03** — 100.00 — Minimal combination: adds C-24 trace block + C-25 enforcement contract to R6 V-03 base. No failure-mode blockquotes, no self-check. Establishes new minimum prompt for v7 rubric.
2. **V-04** — 100.00 — Full integration: adds failure-mode blockquotes (C-17 reinforcement) and 25-criterion self-check to V-03 mechanisms.
3. **V-05** — 100.00 — Highest-reliability form: V-04 plus structural disqualifying definitions for C-24 and C-25 in the self-check, mirroring R5/R6 V-05 pattern.
4. **V-01** — 98.24 — C-24 axis only: structured trace block present, but lacks bilateral closure (C-20) and gate forward-reference (C-25). Scope-exclusion guards are bare redirects.
5. **V-02** — 98.24 — C-25 axis only: gate forward-reference present, but hypothesis is in standalone MANDATORY OPENING rather than inside the gate (C-21/C-22 fail) and synthesis uses prose verdict (C-24 fail).

---

## Excellence Signals from Top-Scoring Variations

**Signal 1 — Orthogonal axis isolation works but converges at V-03**
V-01 (C-24 only) and V-02 (C-25 only) each achieve their target criterion cleanly and preserve all inherited criteria. The single-axis tests confirm that C-24 and C-25 are structurally independent — adding the labeled trace block requires no gate changes; adding the gate forward-reference requires no synthesis changes. However, both single-axis variations score identically (98.24) because each forfeits three aspirational criteria instead of the expected two. The minimum-viable combination (V-03) is the inflection point where all 17 criteria clear simultaneously.

**Signal 2 — Enforcement contract format: type-differentiated outbound mesh**
V-03/V-04/V-05 structure the C-25 forward-reference as two named lines distinguishing *scope* enforcement sections from *hypothesis* enforcement:
```
- Scope exclusions: enforced in INERTIA CHECK, SURFACE AREA, COMPLEXITY, and SYNTHESIS
- Hypothesis: confirmed or revised in SYNTHESIS
```
This is more reliable than a flat list or a continuation instruction ("preconditions for STEP 1 through STEP 7"). The type-differentiated format makes scope compliance and hypothesis compliance independently verifiable: a reader checking C-23 (do guards point home?) can navigate to the four scope sections; a reader checking C-22 (does synthesis name the gate?) navigates to SYNTHESIS. Without the type split, a flat list of five sections gives no signal about which sections are responsible for which obligation.

**Signal 3 — Labeled trace block as audit primitive**
The Commitment chain: / Gate commitment: / Analysis: / Verdict: structure in V-01/V-03/V-04/V-05 makes the three-step commitment chain independently readable at a glance. The critical mechanical property: each line can be verified in isolation without parsing sentence boundaries. The disqualifying prose form — "The preliminary hypothesis committed in PRE-FLIGHT GATE (MEDIUM, 3–5 sprints) is confirmed: surface area is LOW and inertia cost is HIGH" — requires the reader to decompose the sentence to identify which part is the gate value, which is the evidence, and which is the verdict. The labeled block eliminates that decomposition. V-05 makes this explicit in the C-24 self-check definition with a concrete disqualifying example.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Enforcement contract type differentiation — C-25 forward-reference names scope-enforcement sections separately from hypothesis-enforcement section, making gate obligations traceable by type rather than requiring readers to infer which downstream section is responsible for which commitment", "Labeled commitment-chain trace as audit primitive — Gate commitment / Analysis / Verdict on separate labeled lines allows each step to be verified in isolation without sentence decomposition; the structural form makes internal contradictions immediately visible where prose embeds the same information behind sentence boundaries", "Bidirectional navigational mesh completion at minimum prompt — C-23 (guards name home) and C-25 (home names guards) are orthogonal and independent, but both are achievable in the minimal V-03 form without failure-mode blockquotes or self-check machinery; V-03 is the new minimum prompt for the v7 rubric"]}
```
