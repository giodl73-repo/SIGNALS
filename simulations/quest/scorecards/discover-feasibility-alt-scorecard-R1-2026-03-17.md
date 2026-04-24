I have all the information needed. Let me now produce the full scorecard.

---

# Scorecard: `discover-feasibility-alt` — Round 1

**Rubric**: v11 | **Date**: 2026-03-17 | **Variations**: V-01 through V-05
**Evaluation basis**: Prompt template structural analysis (no trace artifact; evaluated against skill description and spec)

---

## Evaluation Framework

| Band | Condition |
|------|-----------|
| Golden | All 5 essential PASS (no PARTIAL) + composite ≥ 80 |
| Passing | All essential (PARTIAL allowed) + 60-79 |
| Failing | Any essential fails or PARTIAL |

Formula: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/23 × 10)`
PARTIAL = 0.5. N/A criteria = 0 in numerator; denominator fixed at 23.

---

## Criterion-by-Criterion Evidence

### Essential Criteria (5)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | INFERENCE GATE has all required fields | PASS | PASS | PASS | PASS | PASS |
| C-02 | VERDICT has score + label + conditional prerequisites | PASS | PASS | PASS | PASS | PASS |
| C-03 | ARCHITECT table: traffic-light ratings + RED Blockers | PASS | PASS | PASS | PASS | PASS |
| C-04 | Inertia surfaces all four required locations | PASS | PASS | PASS | PASS | PASS |
| C-05 | Focus content woven into existing sections | PASS | PASS | PASS | PASS | PASS |

**Evidence:**
- **C-01**: All five variations carry Feature/Team/Timeline fields in INFERENCE GATE. Pass structure inherited from V-05-R7.
- **C-02**: VERDICT section in all variations: `Composite score: [N]/100`, label with range, prerequisites conditional on FEASIBLE WITH CAVEATS. Consistent.
- **C-03**: ARCHITECT table specifies GREEN/YELLOW/RED per row; RED Blockers section with blocker statement, Lift condition, Do-nothing cost required. "No RED components" exit phrase provided.
- **C-04**: Four surfaces enforced across all variations: (1) INERTIA Baseline sentence; (2) Do-nothing cost column on every ARCHITECT row; (3) "Not building this means:" in VERDICT; (4) "Inertia saved:" per AMENDMENTS item. V-02/V-05 add INERTIA MANIFEST pre-declaration as a second enforcement layer but baseline per-section enforcement intact in all.
- **C-05**: Item D in all variations: "No section heading matching the focus dimension (e.g., '## COMPLIANCE', '## STAKEHOLDERS') will appear after AMENDMENTS." Propagation Contract routes all focus content to existing sections. Structural prohibition explicit.

---

### Recommended Criteria (3)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | AMENDMENTS traceable to RED/YELLOW with color transition + score delta | PASS | PASS | PASS | PASS | PASS |
| C-07 | Focus integration visibly influences base analysis | PASS | PASS | PASS | PASS | PASS |
| C-08 | STRATEGY covers ≥50% of ARCHITECT components | PASS | PASS | PASS | PASS | PASS |

**Evidence:**
- **C-06**: All variations: "One action per RED or YELLOW component. Include all three lines — do not drop any." Action → color transition → score delta → Inertia saved. Format enforced.
- **C-07**: `focus_adjusted_total = base_cost + focus_adjustment` changes INERTIA cost, ARCHITECT ratings, VERDICT "Not building this means:", AMENDMENTS savings. Demonstrates calculation change vs. no-focus run in all variations.
- **C-08**: V-01/02/03: "Cover at least half the components from ARCHITECT" → ≥50% by instruction. V-04/05: STRATEGY-first with prospective complete list → 100% by construction, which satisfies ≥50%. PASS in all. Note: V-04/05 strengthen this to a structural guarantee, but the criterion requires only ≥50%.

---

### Aspirational Criteria (23)

**C-09 through C-27** — all confirmed in V-05-R7; evaluated here against v11 rubric:

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-09 | Focus constraint propagates to 2+ downstream sections | PASS | PASS | PASS | PASS | PASS |
| C-10 | AMEND selectively re-weaves only affected sections | PASS | PASS | PASS | PASS | PASS |
| C-11 | Explicit constraint routing in pre-section orientation step | PASS | PASS | PASS | PASS | PASS |
| C-12 | Named failure-mode prohibition | PASS | PASS | PASS | PASS | PASS |
| C-13 | Competitive inertia framing reshapes feasibility calculation | PASS | PASS | PASS | PASS | PASS |
| C-14 | AMEND PROTOCOL: 4-step with unaffected-sections declaration | PASS | PASS | PASS | PASS | PASS |
| C-15 | Focus economics as verifiable arithmetic formula | PASS | PASS | PASS | PASS | PASS |
| C-16 | Propagation contract in tabular form before INFERENCE GATE | PASS | PASS | PASS | PASS | PASS |
| C-17 | Propagation contract table precedes lens + economics in Step 0 | PASS | PASS | PASS | PASS | PASS |
| C-18 | Column headers rubric-aligned + back-references for repeated values | PASS | PASS | PASS | PASS | PASS |
| C-19 | Stated Effect cells bind to exact formula variable names | PASS | PASS | PASS | PASS | PASS |
| C-20 | Formula contract check converts binding into generation-time gate | PASS | PASS | PASS | PASS | PASS |
| C-21 | Named-incumbent field anchors ≥2 of 3 downstream references | PASS | PASS | PASS | PASS | PASS |
| C-22 | Dual-assertion gate with per-location repair instructions | PASS | PASS | PASS | PASS | PASS |
| C-23 | 3-anchor propagation list with minimum-count declaration | PASS | PASS | PASS | PASS | PASS |
| C-24 | Sequential stop-token structure with Satisfied/Not-satisfied branching | PASS | PASS | PASS | PASS | PASS |
| C-25 | AMEND PROTOCOL embeds FORMULA CONTRACT RE-CHECK at step 3(b) | PASS | PASS | PASS | PASS | PASS |
| C-26 | Per-anchor Form: labels with worked substitution examples | PASS | PASS | PASS | PASS | PASS |
| C-27 | Three reliability axes at non-overlapping structural positions | PASS | PASS | PASS | PASS | PASS |

**Evidence for C-09–C-27 (all PASS across all variations):**

- **C-09**: Propagation Contract routes to INERTIA, ARCHITECT, VERDICT, AMENDMENTS — 4 sections ≥ 2 required.
- **C-10**: AMEND PROTOCOL step (2) in all variations: "Unaffected sections: [...] Unaffected sections will not be rewritten." Step (3): "Rewrite each affected section... Do not rewrite, summarize, or reference any section listed as unaffected."
- **C-11**: Step 0 Item A table explicitly names which sections receive the focus constraint, appearing before any section is written.
- **C-12**: Item D in all variations names the specific structural failure mode with examples: "No section heading matching the focus dimension (e.g., '## COMPLIANCE', '## STAKEHOLDERS') will appear after AMENDMENTS."
- **C-13**: `focus_adjusted_total = base_cost + focus_adjustment` is the do-nothing cost in INERTIA, ARCHITECT Do-nothing column, VERDICT "Not building this means:", AMENDMENTS "Inertia saved:" — demonstrably different from a base_cost-only run against the named incumbent.
- **C-14**: 4-step AMEND PROTOCOL with step numbers, "Affected/Unaffected sections" declaration, and "Unaffected sections will not be rewritten." All variations.
- **C-15**: Item C formula: `focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]` as labeled arithmetic. Verifiable by subtracting base_cost from total.
- **C-16**: Item A table (3 columns: Constraint / Section / Effect) appears in Step 0, before INFERENCE GATE.
- **C-17**: "complete all four/five items in the order given — Item A first." Item A is the first element, before Item B (lens) and Item C (economics).
- **C-18**: Column headers: "Constraint introduced by focus | Section where it surfaces | Effect on that section" — rubric-aligned. Repeated constraint rows use "[same]" back-reference.
- **C-19**: AMENDMENTS Stated Effect cell: "[Focus-specific inertia savings: base_cost recaptured + focus_adjustment eliminated = `focus_adjusted_total` recaptured per sprint when named incumbent is replaced]" — exact token `focus_adjusted_total` in table cell. Lexical match confirmed.
- **C-20**: Formula Contract Check in Step 0 with CONDITION (i)/(ii) gate — stops generation before Item B until both conditions confirmed. This is a forward-checking gate, not a retrospective note.
- **C-21**: Named incumbent field in INFERENCE GATE includes "Propagation required — this exact name appears in all three downstream anchors." Minimum count: "At least two of these three anchors are required; all three are recommended." Sufficient for ≥2-anchor propagation.
- **C-22**: CONDITION (i) TABLE SIDE with repair: "STOP. Revise the AMENDMENTS row in Item A to include the phrase..." CONDITION (ii) FORMULA SIDE with separate repair: "STOP. Adjust your Item C plan now so the equation label is `focus_adjusted_total`." Two independently named conditions, each with per-location repair.
- **C-23**: INFERENCE GATE named-incumbent field lists all 3 anchors with Form: labels, e.g., Form: "INERTIA: STATUS QUO -- The [Named incumbent] the Feature Must Beat" + worked example for each. Minimum count declared at source.
- **C-24**: Stop-token sequential structure: CONDITION (i) presented first → "Satisfied: proceed to CONDITION (ii). Not satisfied: STOP. [...] Do not write CONDITION (ii) until CONDITION (i) is satisfied." CONDITION (ii) physically follows. Cannot skip CONDITION (i).
- **C-25**: All variations: AMEND PROTOCOL step 3(b) = "FORMULA CONTRACT RE-CHECK — required before writing the updated Item B" with (i)/(ii) conditions and per-condition repair instructions. Block present as named gate in all five.
- **C-26**: Each of 3 anchors in INFERENCE GATE has Form: label ("Form: 'INERTIA: STATUS QUO -- The [Named incumbent] the Feature Must Beat'") + worked example using multi-word incumbent ("manual CSV export + shared Google Sheet"). All three anchors covered.
- **C-27**: Stop-token gate: Step 0 Item A only. RE-CHECK: AMEND step 3(b) only. Worked examples: INFERENCE GATE Named incumbent field only. No mechanism's content appears at a second structural position across any variation.

---

### New Criteria: C-28, C-29, C-30, C-31

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-28 | STRATEGY precedes ARCHITECT | **FAIL** | **FAIL** | **FAIL** | **PASS** | **PASS** |
| C-29 | Ordering constraints carry causal rationale | **FAIL** | **FAIL** | **PASS** | **PARTIAL** | **PASS** |
| C-30 | INERTIA MANIFEST pre-declares all 4 C-04 surfaces | **FAIL** | **PASS** | **FAIL** | **FAIL** | **PASS** |
| C-31 | Combined C-28+C-29+C-30 compose without regression | **N/A** | **N/A** | **N/A** | **N/A** | **PASS** |

**Evidence:**

**C-28:**
- V-01/02/03: Section order is INERTIA → PM:BUDGET → ARCHITECT → STRATEGY. ARCHITECT heading appears before STRATEGY heading. Structural FAIL regardless of content quality.
- V-04: STRATEGY heading appears before ARCHITECT heading. "Write STRATEGY before ARCHITECT. Every component listed here becomes a row in the ARCHITECT table below." ARCHITECT: "Draw components from STRATEGY above." Structural PASS.
- V-05: Same reorder as V-04, with explicit OC-4 rationale added. PASS.

**C-29:**
- V-01: No because-clauses on ordering directives. "Item A first" — directive only, no causal rationale. "Fill this before PM: BUDGET" — directive only. "Do not write any traffic light before you finish this section" — directive only. FAIL.
- V-02: Same ordering structure as V-01 plus Item E INERTIA MANIFEST. No because-clauses added. FAIL.
- V-03: OC-1 ("because the Stated Effect cells in Item A name the formula variable that Item C computes; the contract must define the variable before the formula computes it"), OC-2 ("because the lens definition in Item B must reference the constraint phrase established in Item A"), OC-3 ("because Item B is the first free-text section where the model generates new prose"). Also section-level because-clauses: INERTIA ("because the INERTIA table values drive the rating of components in ARCHITECT"), PM:BUDGET ("because the budget flag is an input to ARCHITECT ratings"), ARCHITECT ("because a component that fits within available hours rates differently"). All ordering constraints in Step 0 carry because-clauses. PASS.
- V-04: Single ordering note: "Section ordering note: STRATEGY precedes ARCHITECT in this analysis — because ARCHITECT ratings draw only from components already named in STRATEGY; writing ARCHITECT before STRATEGY would require inventing component names mid-table without a prior procurement decision to anchor them." This ONE constraint (OC-4 equivalent) has a because-clause. However, the other ordering constraints in Step 0 ("Item A first", Formula Contract Check gate, "Do not write Item B until...") lack because-clauses. Per C-29: "each constraint is accompanied by an explicit causal rationale." Not all constraints covered → PARTIAL.
- V-05: OC-1 through OC-5 all carry because-clauses. Section-level because-clauses on INERTIA, PM:BUDGET, ARCHITECT. All ordering constraints in Step 0 are accompanied by causal rationale naming the downstream dependency. PASS.

**C-30:**
- V-01: Per-section inline enforcement only ("Do-nothing cost column required on every row", "Include all three lines — do not drop any"). No named INERTIA MANIFEST block in Step 0. FAIL.
- V-02: Item E — INERTIA MANIFEST block in Step 0 (before INFERENCE GATE). Lists all four surfaces with location, value type, required form, and checkbox pre-declaration. End-of-AMENDMENTS INERTIA MANIFEST VERIFICATION. PASS.
- V-03: No INERTIA MANIFEST (V-03 only adds because-clauses). FAIL.
- V-04: No INERTIA MANIFEST. FAIL.
- V-05: Item E — INERTIA MANIFEST with OC-5 rationale ("because the manifest pre-declares all four inertia surface locations; declaring surfaces after some sections are already written converts the manifest from a pre-declaration into a retrospective checklist, which fails C-30"). Pre-declaration block + end-of-AMENDMENTS INERTIA MANIFEST VERIFICATION. PASS.

**C-31:**
- V-01 through V-04: At least one of C-28/C-29/C-30 is not PASS (C-28 FAIL in V-01/02/03; C-30 FAIL in V-04). Composability of the combined three improvements cannot be confirmed. N/A per design intent.
- V-05: C-28 PASS, C-29 PASS, C-30 PASS. Composability check: C-01–C-27 stable — V-05 adds Item E and OC-1–OC-5 without touching the Propagation Contract table structure, AMEND PROTOCOL, INFERENCE GATE anchor list, or VERDICT format. C-08 strengthens from ≥50% to 100% by construction (no regression). C-04 gains a second enforcement layer (MANIFEST) alongside the existing per-section enforcement (no regression). PASS.

---

## Scoring Worksheet

| Variation | Essential (5) | Recommended (3) | Aspirational (/23) | Composite | Golden |
|-----------|--------------|-----------------|-------------------|-----------|--------|
| V-01 | 5/5 = 60 | 3/3 = 30 | 19/23 = 8.26 | **98.26** | YES |
| V-02 | 5/5 = 60 | 3/3 = 30 | 20/23 = 8.70 | **98.70** | YES |
| V-03 | 5/5 = 60 | 3/3 = 30 | 20/23 = 8.70 | **98.70** | YES |
| V-04 | 5/5 = 60 | 3/3 = 30 | 20.5/23 = 8.91 | **98.91** | YES |
| V-05 | 5/5 = 60 | 3/3 = 30 | 23/23 = 10.00 | **100.00** | YES |

*Aspirational numerator: PASS=1, PARTIAL=0.5, FAIL/N/A=0. Denominator fixed at 23.*

---

## Variation Rankings

| Rank | Variation | Composite | C-28 | C-29 | C-30 | C-31 | Golden |
|------|-----------|-----------|------|------|------|------|--------|
| 1 | V-05 Combined | **100.00** | PASS | PASS | PASS | PASS | YES |
| 2 | V-04 STRATEGY-first | **98.91** | PASS | PARTIAL | FAIL | N/A | YES |
| 3 | V-02 INERTIA MANIFEST | **98.70** | FAIL | FAIL | PASS | N/A | YES |
| 3 | V-03 Causal rationale | **98.70** | FAIL | PASS | FAIL | N/A | YES |
| 5 | V-01 Baseline confirm | **98.26** | FAIL | FAIL | FAIL | N/A | YES |

---

## Projection Accuracy

| Variation | Projected | Actual | Match | Deviation |
|-----------|-----------|--------|-------|-----------|
| V-01 | ~78 | 98.26 | NO | +20.3 pts |
| V-02 | ~82 | 98.70 | NO | +16.7 pts |
| V-03 | ~82 | 98.70 | NO | +16.7 pts |
| V-04 | ~82 | 98.91 | NO | +16.9 pts |
| V-05 | ~100 | 100.00 | YES | 0 pts |

**Projection miss diagnosis**: The variations doc projected ~78/82 assuming C-24, C-25, C-26, C-27 would fail empirical validation (they were "pending empirical validation in R8+"). All four criteria PASS: V-05-R7's stop-token gate (C-24), AMEND FORMULA CONTRACT RE-CHECK (C-25), per-anchor Form: + worked examples (C-26), and three-axis non-overlapping structure (C-27) are structurally present in the prompt templates and transfer intact to V-01 through V-05. The 19-criteria-passing baseline (C-09 through C-27) was already at the top of the pre-C-28/29/30 ceiling; only the three new criteria differentiate the variations. Projection should have been ~98/99/99/99/100.

---

## Excellence Signals from V-05

V-05 is the only variation achieving 100.0. Four patterns made it better:

**Pattern 1 — Numbered OC block with because-clauses at point of constraint declaration.** V-05 introduces OC-1 through OC-5, each with an explicit causal because-clause naming the downstream element that depends on the ordering. The OC-label is then cross-referenced in the relevant instruction ("see OC-1", "see OC-4") so the connection between declaration and use is maintained. This satisfies C-29 without restructuring any other element.

**Pattern 2 — Prospective STRATEGY list converts C-08 from output-checked to by-construction.** V-04/V-05 flip the coverage model: "List all components you plan to evaluate in ARCHITECT. The ARCHITECT table must contain exactly the components named here — no more, no fewer." ARCHITECT: "Draw components from STRATEGY above — do not introduce component names not listed in STRATEGY." This converts coverage from a retrospective instruction ("cover at least half") into a structural guarantee — components cannot appear in ARCHITECT without a prior STRATEGY entry.

**Pattern 3 — INERTIA MANIFEST as pre-declaration + post-verification dual enforcement.** V-02/V-05 add Item E which names all four C-04 surfaces before any section is written. At end of AMENDMENTS, INERTIA MANIFEST VERIFICATION re-confirms all four are present. This satisfies C-30 without removing or modifying the existing per-section inline enforcement. The dual-layer structure means C-04 has both a pre-declared checklist AND per-section reminders — neither layer depends on the other.

**Pattern 4 — Section-level because-clauses extend OC coverage into the execution phase.** V-03/V-05 add because-clauses directly to section headers: INERTIA ("because the INERTIA table values drive the rating of components in ARCHITECT"), PM:BUDGET ("because the budget flag is an input to ARCHITECT ratings"), ARCHITECT ("because a component... rates differently"). These extend the causal rationale from Step 0 into the output sections, reinforcing the dependency chain at each write point — not only at the ordering declaration.

---

## Key Findings

1. **C-24 through C-27 confirmed PASS at 100.0** across all five variations. The V-05-R7 baseline fully satisfies all four criteria that were pending empirical validation. This is the primary result of R1.

2. **Three structural gaps confirmed at criterion level** (C-28 FAIL in V-01/02/03, C-29 FAIL in V-01/02, C-30 FAIL in V-01/03/04). All three are repaired individually in V-02/V-03/V-04 and jointly in V-05.

3. **V-05 composes without regression (C-31 PASS)**. All C-01 through C-27 remain PASS when C-28, C-29, C-30 are all active. The three structural improvements are non-interfering:
   - Item E occupies Step 0 only
   - Because-clauses are annotations on existing ordering directives only
   - STRATEGY-before-ARCHITECT affects output section order only

4. **C-29 PARTIAL for V-04** confirms the single-axis design prediction: one ordering constraint with a because-clause is not sufficient when other ordering directives in Step 0 lack rationale. V-03's explicit OC-1/2/3 naming pattern is the complete fix.

5. **All five variations are Golden**. The baseline V-05-R7 was already above the 80-point threshold even before the three new improvements. V-05 is the recommended production version.

---

## Recommendation

**Promote V-05 as the v11 production prompt.** It is the only variation where C-28, C-29, C-30, and C-31 all PASS. No prior criterion regresses. The four excellence signals (numbered OC blocks, prospective STRATEGY list, INERTIA MANIFEST dual enforcement, section-level because-clauses) are additive and non-overlapping.

**Next round**: R1 validates the three structural improvements individually and jointly. No further structural gaps identified. The rubric is stable at v11. R2, if run, should focus on adversarial or edge-case variation axes (e.g., no-focus path behavior, AMEND with threshold adjustment) rather than additional structural improvements.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["numbered OC block with because-clauses cross-referenced at point of use converts implicit ordering into documented constraints without restructuring other elements", "prospective STRATEGY component list converts C-08 from output-checked retrospective instruction to by-construction structural guarantee", "INERTIA MANIFEST pre-declaration plus end-of-AMENDMENTS verification creates dual-layer enforcement without removing per-section inline reminders", "section-level because-clauses in INERTIA/PM:BUDGET/ARCHITECT headers extend ordering rationale from Step 0 into execution phase at each write point"]}
```
