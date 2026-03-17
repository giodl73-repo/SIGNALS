## Round 6 Scorecard — `discover-feasibility-alt` (v6 Rubric)

---

### V-01 — V-05-R5 Baseline (100.000 under v6 confirm)

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 | essential | PASS | INFERENCE GATE has Feature, Team, Timeline, Named incumbent — all required fields. |
| C-02 | essential | PASS | VERDICT has score/100, label, prerequisite block conditioned on FEASIBLE WITH CAVEATS. |
| C-03 | essential | PASS | ARCHITECT table has GREEN/YELLOW/RED per row; RED Blockers require all three sub-fields. |
| C-04 | essential | PASS | All four inertia surfaces: INERTIA Baseline, ARCHITECT Do-nothing cost column, "Not building this means:", "Inertia saved:" per amendment. |
| C-05 | essential | PASS | Item D prohibits "## COMPLIANCE"/"## STAKEHOLDERS" headings by name; preamble reinforces. |
| C-06 | recommended | PASS | AMENDMENTS requires component name, color-transition, score-delta estimate per entry. |
| C-07 | recommended | PASS | Propagation contract routes focus constraint to ARCHITECT ratings via focus_adjusted_total; ratings can change color due to focus-adjusted economics. |
| C-08 | recommended | PASS | "Cover at least half the components from ARCHITECT" explicit instruction. |
| C-09 | aspirational | PASS | Item A table routes constraint through INERTIA → ARCHITECT → VERDICT → AMENDMENTS; multi-section propagation structurally enforced. |
| C-10 | aspirational | N/A | AMEND PROTOCOL present and complete; AMEND not invoked in this scoring run. |
| C-11 | aspirational | PASS | Item A table names all four downstream sections as routing targets with effect descriptions per row. |
| C-12 | aspirational | PASS | Item D names "## COMPLIANCE", "## STAKEHOLDERS" as the exact failure-mode headings to avoid. |
| C-13 | aspirational | PASS | focus_adjusted_total separates base_cost from focus_adjustment; ARCHITECT ratings can change because of focus-adjusted do-nothing cost; named incumbent anchors the competitive entity. |
| C-14 | aspirational | N/A | AMEND PROTOCOL has 4-step structure + "Unaffected sections will not be rewritten"; AMEND not invoked. |
| C-15 | aspirational | PASS | Item C: `focus_adjusted_total = base_cost + focus_adjustment = [TOTAL]` — labeled arithmetic equation verifiable by inspection. |
| C-16 | aspirational | PASS | Item A table (Constraint / Section / Effect) appears in Step 0 before INFERENCE GATE. |
| C-17 | aspirational | PASS | Item A (table) is first in Step 0; Item B (lens) and Item C (economics) follow. Sequence explicit. |
| C-18 | aspirational | PASS | Headers: "Constraint introduced by focus" / "Section where it surfaces" / "Effect on that section" — rubric-aligned. Rows 2–4 use `[same]`. |
| C-19 | aspirational | PASS | All four Stated Effect rows name `focus_adjusted_total` explicitly. Item C defines `focus_adjusted_total = base_cost + focus_adjustment`. Lexical test passes both locations. |
| C-20 | aspirational | PASS | Single-sentence forward gate between Item A and Item B: "The variable `focus_adjusted_total = base_cost + focus_adjustment` from Item C must appear by exact name in at least one Stated Effect cell above. Verify this is true before writing Item B." Positioned before Item B, names the variable, is a forward check. |
| C-21 | aspirational | PASS | Named incumbent field present. All three downstream anchors covered in template body: (1) INERTIA heading "The Named Incumbent the Feature Must Beat" matches C-21 example form; (2) INERTIA table "Named incumbent" column; (3) AMENDMENTS "Frame savings as 'recaptured from [Named incumbent]'". Field + 3/3 anchors = PASS. |

**Essential all-pass:** YES (no PARTIALs) | **Aspirational pass count:** 13/13 (C-10, C-14 N/A = PASS)

```
Composite = (5/5 × 60) + (3/3 × 30) + (13/13 × 10)
          = 60 + 30 + 10.000
          = 100.000
```

**Band: Golden**

> **v6 confirm:** V-05-R5 scores 100.000 under v6 as predicted. C-20 satisfies via single-sentence forward gate. C-21 satisfies because the named-incumbent field is present and all three downstream anchors are covered in the template body. Baseline confirmed before testing new axes.

---

### V-02 — C-20 Dual-Assertion Gate

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 through C-19 | — | all PASS | Identical to V-01. Only C-20 gate form changes. |
| C-20 | aspirational | PASS | **Dual-assertion checklist**: "(i) `focus_adjusted_total` appears by exact name in at least one Stated Effect cell. If not satisfied: revise the AMENDMENTS row now. (ii) `focus_adjusted_total` will appear as the left-hand side label of the arithmetic equation in Item C. If not satisfied: revise Item C. Both conditions must hold. Do not write Item B until both are confirmed." **Stronger than V-01**: two independent conditions with repair instructions per failure location vs. V-01's single instruction that covers only the table-side location. The formula-side location is now an explicitly named gate condition, not an implicit consequence of formula design. |
| C-21 | aspirational | PASS | Same as V-01 — field present, 3/3 anchors in template body. |

**Essential all-pass:** YES | **Aspirational pass count:** 13/13

```
Composite = (5/5 × 60) + (3/3 × 30) + (13/13 × 10) = 100.000
```

**Band: Golden**

> **C-20 axis finding:** V-01's single gate enforces the table-side location only ("at least one Stated Effect cell"). V-02 closes the gap: condition (ii) explicitly requires `focus_adjusted_total` as the Item C equation label. A model that passes C-19 (both locations have the token) but has not been explicitly prompted to check the formula label would pass V-01's gate on table evidence alone. V-02 removes that ambiguity.

---

### V-03 — C-21 Explicit 3-Anchor Propagation List

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 through C-19 | — | all PASS | Identical to V-01. |
| C-20 | aspirational | PASS | Same single-sentence gate as V-01. |
| C-21 | aspirational | PASS | **Explicit 3-anchor propagation list** added to INFERENCE GATE Named incumbent field: "Propagation required — use this exact name in all three downstream anchors: (1) INERTIA section heading: rename to 'INERTIA: STATUS QUO — The [Named incumbent] the Feature Must Beat'; (2) INERTIA table: first column header reads '[Named incumbent]' not 'What the team does instead'; (3) AMENDMENTS: savings framed as 'recaptured from [Named incumbent]' not 'workaround eliminated'. At least two of these three anchors are required; all three are recommended." **Stronger than V-01**: V-01's implicit "use this name throughout" leaves the model to infer which sections qualify. V-03 names each anchor by location and form, sets a minimum count, and makes the propagation contract checkable at the declaration point. |

**Essential all-pass:** YES | **Aspirational pass count:** 13/13

```
Composite = (5/5 × 60) + (3/3 × 30) + (13/13 × 10) = 100.000
```

**Band: Golden**

> **C-21 axis finding:** V-01 passes C-21 because the template body already enforces the anchors. V-03 makes the contract visible at the declaration point (INFERENCE GATE) rather than implied by the downstream templates. Propagation drift in production — model writes the field but uses generic labels in 1-of-3 downstream anchors — is harder to mask when the minimum count is explicitly stated at the source.

---

### V-04 — Combined: C-20 Dual-Assertion Gate + C-21 Explicit 3-Anchor Propagation

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 through C-19 | — | all PASS | Identical to V-01. |
| C-20 | aspirational | PASS | Dual-assertion checklist (same as V-02). |
| C-21 | aspirational | PASS | Explicit 3-anchor propagation list (same as V-03). |

**Essential all-pass:** YES | **Aspirational pass count:** 13/13

```
Composite = (5/5 × 60) + (3/3 × 30) + (13/13 × 10) = 100.000
```

**Band: Golden**

> **Combined axis finding:** The two reliability mechanisms are structurally orthogonal — the formula gate lives in Step 0 Item A; the anchor list lives in INFERENCE GATE. Combining them introduces no interaction. V-04 carries both reliability improvements without noise.

---

### V-05 — Incumbent-First Phrasing Register + C-20 Dual-Assert + C-21 Explicit 3-Anchor

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 through C-19 | — | all PASS | Identical to V-04 on all criteria. |
| C-20 | aspirational | PASS | Dual-assertion checklist (same as V-02/V-04). |
| C-21 | aspirational | PASS | Explicit 3-anchor propagation list (same as V-03/V-04). INFERENCE GATE field adds "Establish this first — it is the competitive reference for every downstream section." Opening block leads with: "**First, establish who the incumbent is.** Before analysis begins, you will record in INFERENCE GATE the specific workaround, tool, or process the team uses today. This name becomes the competitive reference for the entire output." The **incumbent-first phrasing** positions the naming act as the first instruction before competitive framing — treating the incumbent as a first-class input parallel to Topic/Focus rather than a value inferred from the competitive argument. C-21: field present + 3/3 anchors propagated. |

**Essential all-pass:** YES | **Aspirational pass count:** 13/13

```
Composite = (5/5 × 60) + (3/3 × 30) + (13/13 × 10) = 100.000
```

**Band: Golden**

> **Phrasing axis finding:** V-04 introduces the incumbent mid-paragraph within competitive framing ("The status quo is your real competitor. You will name the incumbent in INFERENCE GATE"). V-05 names the incumbent as the first act before competitive framing exists. The practical consequence: when the model encounters V-04's incumbent field, it arrives having already processed competitive context. When it encounters V-05's field, the incumbent is declared before any competitive interpretation has begun — reducing the risk of the model conflating "the named incumbent" with "whatever my competitive framing suggests."

---

## Rankings

| Rank | Variation | Score | C-20 Gate Form | C-21 Anchor Form | Phrasing |
|------|-----------|-------|----------------|------------------|----------|
| 1 | V-05 | 100.000 | Dual-assert checklist | Explicit 3-anchor list | Incumbent-first |
| 2 | V-04 | 100.000 | Dual-assert checklist | Explicit 3-anchor list | Competitive-frame-first |
| 3 | V-02 | 100.000 | Dual-assert checklist | Implicit "use throughout" | Competitive-frame-first |
| 4 | V-03 | 100.000 | Single-sentence gate | Explicit 3-anchor list | Competitive-frame-first |
| 5 | V-01 | 100.000 | Single-sentence gate | Implicit "use throughout" | Competitive-frame-first |

All five variations score 100.000. Ranking reflects production reliability:

- **V-05** recommended: incumbent-first phrasing pre-commits the naming act before analysis; dual-assert gate enforces formula variable in both locations independently; explicit 3-anchor list makes C-21 propagation checkable at the declaration point.
- **V-04** is the fallback if incumbent-first phrasing causes premature inference (model attempts to fill in the incumbent name before reaching INFERENCE GATE).
- **V-02 vs. V-03**: The C-21 explicit anchor list (V-03) closes a gap V-01 left open (propagation drift). The dual-assert gate (V-02) closes a gap V-01 addressed less explicitly (formula-label verification). V-03 addresses a higher-probability production failure.

---

## Excellence Signals

**Signal 1 — Dual-assertion checklist converts a prose reminder into two independent enforcement points**
V-02 demonstrates that splitting a single compound gate into two named conditions with per-condition repair instructions changes the semantic load. A single "verify this is true" instruction can be treated as advisory; a numbered checklist with an explicit repair path per failure location creates two discrete steps each with a defined correction action.

**Signal 2 — Explicit anchor enumeration at the declaration point closes propagation drift**
V-03 demonstrates that naming all three downstream anchors by exact location and form in the INFERENCE GATE field — the same location where the value is declared — creates a closed propagation contract at the source. V-01's implicit "use this name throughout" leaves the inference step to the model. The explicit list eliminates it: locations are named, required forms specified, minimum count stated.

---

```json
{"top_score": 100.000, "all_essential_pass": true, "new_patterns": ["Dual-assertion checklist splits a single compound condition into two named independent verification points with explicit repair instructions per failure location -- a numbered checklist with per-condition repair paths reduces the probability that one location is verified while the other is assumed", "Explicit anchor enumeration at the declaration point closes propagation drift -- naming all three downstream propagation anchors by exact location and required form in the same INFERENCE GATE field where the value is declared creates a closed contract at the source, eliminating the inference step that implicit propagation instructions require"]}
```
st | Implicit "use throughout" | Competitive-frame-first |
| 4 | V-03 | 100.000 | Single-sentence gate | Explicit 3-anchor list | Competitive-frame-first |
| 5 | V-01 | 100.000 | Single-sentence gate | Implicit "use throughout" | Competitive-frame-first |

All five variations score 100.000 under v6 rubric. Ranking reflects production reliability (expected PASS rate across topic variation), not static template score:

- **V-05** is the production recommendation: incumbent-first phrasing pre-commits the naming act before analysis, dual-assert gate enforces formula variable in both locations independently, explicit 3-anchor list makes C-21 propagation checkable at the declaration point.
- **V-04** is the fallback if incumbent-first phrasing introduces inference errors in production (model attempts to fill in the incumbent name before reaching INFERENCE GATE). Same reliability on C-20 and C-21.
- **V-02 vs. V-03**: If only one axis can be chosen, the dual-assert C-20 gate (V-02) targets a failure mode (formula-label missing) that V-01's gate already caught in R5. The explicit C-21 anchor list (V-03) targets a failure mode (propagation drift to fewer than 2 anchors) that V-01's implicit instruction left unaddressed. V-03 closes a gap V-01 left open; V-02 closes a gap V-01 closed less explicitly.

---

## Excellence Signals (from R6 top-scoring variations)

**Signal 1 — Dual-assertion checklist converts a prose reminder into two independent enforcement points**
V-02 demonstrates that splitting a single compound condition ("variable must appear in at least one table cell") into two named conditions with independent repair instructions changes the semantic load. A prose reminder ("verify this is true") can be skipped by a model treating the gate as advisory. A numbered checklist with explicit repair actions per condition makes each verification a discrete step with a defined correction path, reducing the probability that one location is checked while the other is assumed.

**Signal 2 — Explicit anchor enumeration at the declaration point closes propagation drift**
V-03 demonstrates that naming all three downstream anchors by exact location and form in the INFERENCE GATE field itself — the same location where the value is declared — creates a closed propagation contract at the source. V-01's equivalent instruction ("use this name throughout") is a general instruction that leaves the model to determine where "throughout" applies. The explicit list reduces ambiguity by eliminating the inference step: the three locations are named, their required forms are specified, and the minimum count is stated.

**Signal 3 — Incumbent-first phrasing treats naming as a first-class input act**
V-05 demonstrates that positioning the naming act as the first instruction before any competitive framing changes the model's relationship to the named incumbent field. When competitive framing precedes the naming act (V-04: "The status quo is your real competitor → you will name the incumbent"), the incumbent is introduced as a variable within the competitive argument. When the naming act precedes competitive framing (V-05: "First, establish who the incumbent is → then frame the competitive question"), the incumbent is treated as a declaration parallel to Topic and Focus — something established before analysis begins, not derived from it.

---

```json
{"top_score": 100.000, "all_essential_pass": true, "new_patterns": ["Dual-assertion checklist splits a single compound condition into two named independent verification points with explicit repair instructions per failure location -- a numbered checklist with per-condition repair paths reduces the probability that one location is verified while the other is assumed", "Explicit anchor enumeration at the declaration point closes propagation drift -- naming all three downstream propagation anchors by exact location and required form in the same INFERENCE GATE field where the value is declared creates a closed contract at the source, eliminating the inference step that implicit propagation instructions require"]}
```
