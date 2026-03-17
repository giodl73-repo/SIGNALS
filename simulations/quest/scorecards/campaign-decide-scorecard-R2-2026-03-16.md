## Scorecard — campaign-decide / Round 2

### Rubric v2 Summary
- **Essential (60 pts):** C-01 through C-05, 12 pts each
- **Recommended (30 pts):** C-06 through C-08, 10 pts each
- **Aspirational (10 pts):** C-09 through C-12, 2.5 pts each
- **Formula:** `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/4 × 10)`
- **Gold threshold:** all 5 essential pass AND composite ≥ 80

---

### V-01 — Per-phase named-field schema

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|---------------|
| C-01 | Recommendation stated | **PASS** | Phase 6: `Recommendation: [COMMIT/PAUSE/PIVOT/ABANDON]` required field |
| C-02 | Confidence level stated | **PASS** | Phase 6: `Confidence: [High/Medium/Low]` required field |
| C-03 | All six domains represented | **PASS** | Phases 1–6 map to competitors / feasibility / market / hypothesis / websearch / synthesis in canonical order |
| C-04 | Inertia-first competitor framing | **PASS** | Explicit ordering rule: "all Inertia fields must appear before any Rival fields" — enforced by field sequence |
| C-05 | Evidence-to-recommendation traceability | **PASS** | Phase 6 requires `Because (required, cite by Phase and field): [claim] because Phase N, [field]` |
| C-06 | Structured decision brief format | **PASS** | `##` section header per phase, titled synthesis block |
| C-07 | Risk and counter-evidence acknowledged | **PASS** | Phase 6: `Counter-evidence: [one risk or caveat...]` is a required field |
| C-08 | Hypothesis disposition explicit | **PASS** | Phase 6: `Hypothesis outcome: [Confirmed/Refuted/Inconclusive]` required field |
| C-09 | Confidence calibration narrative | **PASS** | Phase 6: `Confidence rationale: [name the specific findings or gaps that drove the rating — not just the label]` |
| C-10 | Actionable next steps conditioned | **PASS** | Phase 6: `Next step: [COMMIT → concrete action, not "do more research" \| no-build → exit condition or revisit trigger]` |
| C-11 | Per-phase required-field schema | **PASS** | Each phase lists required labeled fields; all 6 phases have distinct named-row schemas. Risk: named-field format vs table rows — rubric says "named rows," not "table rows"; intent satisfied. |
| C-12 | Templated citation syntax | **PASS** | `[claim] because Phase N, [field name]` matches the rubric's `because Phase [N], [section reference]` example closely — same Phase+field structure |

**Essential:** 5/5 → 60 pts | **Recommended:** 3/3 → 30 pts | **Aspirational:** 4/4 → 10 pts

**Composite: 100 — Gold**

Residual risk: A strict C-11 scorer expecting markdown table rows (not labeled fields) might score C-11 as partial. No other risk paths.

---

### V-02 — Role sequence (hypothesis-first)

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|---------------|
| C-01 | Recommendation stated | **PASS** | Phase 6 table: `Recommendation` field |
| C-02 | Confidence level stated | **PASS** | Phase 6 table: `Confidence` field |
| C-03 | All six domains represented | **PASS** | All six skills present across phases; rubric says "represented" not "in canonical order" — low-risk interpretation |
| C-04 | Inertia-first competitor framing | **PASS** | Phase 2 table: inertia rows (Inertia/status quo, Switching cost) listed before named rival rows; rule stated in parenthetical |
| C-05 | Evidence-to-recommendation traceability | **PASS** | Phase 6 `Because (cite by Phase):` block with `[claim] because Phase N, [field/row]` for all 5 phases |
| C-06 | Structured decision brief format | **PASS** | `##` per-phase headers, Phase 6 table + citation block |
| C-07 | Risk and counter-evidence acknowledged | **PASS** | Phase 6 table: `Counter-evidence` row required |
| C-08 | Hypothesis disposition explicit | **PASS+** | Phase 6 table: `Hypothesis outcome` row. **Depth advantage**: hypothesis committed as Phase 1 anchor — evidence tests a prior belief, not post-hoc framing. Disposition is a genuine experimental result. |
| C-09 | Confidence calibration narrative | **PASS** | Phase 6 table: `Confidence rationale: [name specific evidence gaps or strengths — not just the label]` |
| C-10 | Actionable next steps conditioned | **PASS** | Phase 6 table: `Next step: [COMMIT: concrete action \| no-build: exit condition or revisit trigger]` |
| C-11 | Per-phase required-field schema | **PASS** | Every phase has a full markdown table schema with named columns; strongest table coverage in round |
| C-12 | Templated citation syntax | **PASS** | `because Phase N, [field/row]` across all 5 phases — matches rubric example format |

**Essential:** 5/5 → 60 pts | **Recommended:** 3/3 → 30 pts | **Aspirational:** 4/4 → 10 pts

**Composite: 100 — Gold**

Quality edge: C-08 is deeper than standard pass — hypothesis-anchor pattern ensures synthesis reports a true experimental outcome, not post-hoc confirmation. C-03 canonical-order risk is low: rubric says "represented," not "in order."

---

### V-03 — Citation anchor (finding-ID system)

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|---------------|
| C-01 | Recommendation stated | **PASS** | Phase 6: `Recommendation: [COMMIT/PAUSE/PIVOT/ABANDON]` field |
| C-02 | Confidence level stated | **PASS** | Phase 6: `Confidence: [High/Medium/Low]` field |
| C-03 | All six domains represented | **PASS** | Phases 1–6: competitors / feasibility / market / hypothesis / websearch / synthesis — all present |
| C-04 | Inertia-first competitor framing | **PASS** | Phase 1 table: F1-01/F1-02 are inertia rows, precede F1-03/F1-04 named rivals; rule stated explicitly |
| C-05 | Evidence-to-recommendation traceability | **PASS** | Phase 6: `Because (required, cite by FID): [claim] because [FID]` — FID pinning is traceable by lookup |
| C-06 | Structured decision brief format | **PASS** | `##` per-phase section headers |
| C-07 | Risk and counter-evidence acknowledged | **PASS** | Phase 6: `Counter-evidence: [one risk or caveat — cite the finding it qualifies, by FID]` — counter-evidence is FID-pinned |
| C-08 | Hypothesis disposition explicit | **PASS** | Phase 6: `Hypothesis outcome: [Confirmed/Refuted/Inconclusive]` required field |
| C-09 | Confidence calibration narrative | **PASS** | Phase 6: `Confidence rationale: [name the specific findings — cite by FID — that drove this rating]` — FID citations make "specific" concrete |
| C-10 | Actionable next steps conditioned | **PASS** | Phase 6: `Next step: [COMMIT: concrete action \| no-build: exit condition or revisit trigger]` |
| C-11 | Per-phase required-field schema | **PASS** | Each phase has FID-prefixed rows; Phases 1-3, 5 use tables; Phase 4 uses FID-labeled named fields; Phase 6 uses named fields. Mixed format but all phases have a per-phase schema. |
| C-12 | Templated citation syntax | **PASS** | `because [FID]` is a prescribed format and is mechanically auditable at a glance. Rubric says "e.g." — FID satisfies "mechanically auditable" even if different syntax. Note: a strict scorer requiring `Phase N, [section]` syntax would fail this. |

**Essential:** 5/5 → 60 pts | **Recommended:** 3/3 → 30 pts | **Aspirational:** 4/4 → 10 pts

**Composite: 100 — Gold**

C-12 interpretive risk is the only gap — FID format satisfies the spirit but differs from the rubric's example syntax. Lenient scorer: PASS. Strict scorer: FAIL C-12 → composite drops to 97.5. Mixed-format phases (Phase 4 uses labeled fields, not tables) creates mild C-11 inconsistency compared to V-02/V-05.

---

### V-04 — Named fields + finding-IDs (combined)

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|---------------|
| C-01 | Recommendation stated | **PASS** | `F6-02 Recommendation: [COMMIT/PAUSE/PIVOT/ABANDON]` |
| C-02 | Confidence level stated | **PASS** | `F6-03 Confidence: [High/Medium/Low]` |
| C-03 | All six domains represented | **PASS** | Phases 1–6: all six domains in canonical order |
| C-04 | Inertia-first competitor framing | **PASS** | "Ordering rule: F1-01 through F1-03 (inertia) must be populated before F1-04+ (named rivals)" — explicit and FID-enforced |
| C-05 | Evidence-to-recommendation traceability | **PASS** | Phase 6: `Because (required, cite by FID — minimum 4 citations spanning at least 3 phases):` |
| C-06 | Structured decision brief format | **PASS** | `##` per-phase headers, FID-labeled synthesis block |
| C-07 | Risk and counter-evidence acknowledged | **PASS** | `F6-05 Counter-evidence: [one risk or caveat — cite the finding it qualifies, by FID]` |
| C-08 | Hypothesis disposition explicit | **PASS** | `F6-01 Hypothesis outcome: [Confirmed/Refuted/Inconclusive]` |
| C-09 | Confidence calibration narrative | **PASS** | `F6-04 Confidence rationale: [cite by FID the specific findings that drove the rating]` — FID grounding makes "specific" concrete |
| C-10 | Actionable next steps conditioned | **PASS** | `F6-06 Next step: [COMMIT: concrete action \| no-build: exit condition or revisit trigger]` |
| C-11 | Per-phase required-field schema | **PASS** | Every phase has FID-labeled named fields (F1-01 through F6-06). Most rendering-robust implementation of C-11 — named fields survive markdown degradation that breaks table alignment. |
| C-12 | Templated citation syntax | **PASS** | `because F[phase]-[seq]` is prescribed and mechanically auditable. Same interpretive risk as V-03: strict Phase+section scorer would fail this. |

**Essential:** 5/5 → 60 pts | **Recommended:** 3/3 → 30 pts | **Aspirational:** 4/4 → 10 pts

**Composite: 100 — Gold**

C-12 FID risk same as V-03. However, C-11 is the most rendering-robust implementation in the round — FID-labeled named fields survive context pressure better than markdown tables. Minimum-4-citations constraint in Phase 6 is a novel enforcement not in the rubric; may produce over-cited synthesis blocks but doesn't hurt scoring.

---

### V-05 — Hypothesis-first + V-02 R1 tables (best-of synthesis)

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|---------------|
| C-01 | Recommendation stated | **PASS** | Phase 6 table: `Recommendation` field |
| C-02 | Confidence level stated | **PASS** | Phase 6 table: `Confidence` field |
| C-03 | All six domains represented | **PASS** | All six skills present; rubric says "represented" not "in canonical order." Low-risk — same as V-02. |
| C-04 | Inertia-first competitor framing | **PASS** | Phase 2 table: inertia rows precede named rival rows; parenthetical rule enforces ordering |
| C-05 | Evidence-to-recommendation traceability | **PASS** | Phase 6 `Because (cite by Phase):` block spans all 5 evidence phases — complete cross-phase traceability by construction |
| C-06 | Structured decision brief format | **PASS** | `##` per-phase headers; Phase 6 table + citation block |
| C-07 | Risk and counter-evidence acknowledged | **PASS** | Phase 6 table: `Counter-evidence` row required |
| C-08 | Hypothesis disposition explicit | **PASS+** | Phase 6: `Hypothesis outcome: [Confirmed / Refuted / Inconclusive — must match Phase 1 claim]`. Anchor linkage is strongest in the round — disposition is structurally required to reconcile with Phase 1 commitment, not merely report a label. |
| C-09 | Confidence calibration narrative | **PASS** | Phase 6 table: `Confidence rationale: [name specific evidence gaps or strengths — not just the label]` |
| C-10 | Actionable next steps conditioned | **PASS** | Phase 6 table: `Next step: [COMMIT: concrete action \| no-build: exit condition or revisit trigger]` |
| C-11 | Per-phase required-field schema | **PASS** | Every phase has a complete table schema: Phase 1 (Field/Value, 6 rows), Phase 2 (Force/Type/Strength/Notes), Phase 3 (Dimension/Rating/Notes), Phase 4 (Segment/Size/Fit/Priority), Phase 5 (Source/Quote/Strength/Verdict), Phase 6 (Field/Value, 6 rows). Proven V-02 R1 structure — highest table coverage fidelity in round. |
| C-12 | Templated citation syntax | **PASS** | `because Phase N, [field/row]` across all 5 evidence phases — exact rubric example syntax, no interpretive risk. Strongest C-12 signal in round. |

**Essential:** 5/5 → 60 pts | **Recommended:** 3/3 → 30 pts | **Aspirational:** 4/4 → 10 pts

**Composite: 100 — Gold**

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational | Composite | Band |
|-----------|-----------|-------------|--------------|-----------|------|
| V-01 | 60 | 30 | 10 | **100** | Gold |
| V-02 | 60 | 30 | 10 | **100** | Gold |
| V-03 | 60 | 30 | 10 | **100** | Gold* |
| V-04 | 60 | 30 | 10 | **100** | Gold* |
| V-05 | 60 | 30 | 10 | **100** | Gold |

*Gold under lenient C-12 interpretation. Under strict Phase+section-only scoring: C-12 FAIL → V-03 and V-04 drop to **97.5**.

---

### Ranking

**Tie at 100 — broken by criterion-level quality signals:**

1. **V-05** — Strongest C-08 (anchor linkage "must match Phase 1 claim"), strongest C-11 (proven V-02 table structure), strongest C-12 (exact rubric syntax, no interpretive risk). Best-of synthesis delivers maximum structural guarantees.
2. **V-02** — Second-strongest C-08 (anchor ordering without explicit linkage requirement), strong C-11 and C-12. Only risk: C-03 canonical-order interpretation (low probability).
3. **V-01** — All 12 criteria met. Phase+section citation format (no C-12 risk). Named-field format is lighter than tables; slight C-11 scoring variance possible.
4. **V-04** — FID citation risk on C-12 under strict scoring. C-11 is rendering-robust but not table-based. Minimum-4-citations constraint adds enforcement rigor.
5. **V-03** — FID citation risk on C-12 same as V-04. Phase 4 uses non-table format, creating minor per-phase inconsistency vs Phases 1–3, 5.

---

### Excellence Signals from V-05 (Top Variation)

**Signal 1 — Anchor linkage in synthesis disposition**: `Hypothesis outcome: [Confirmed / Refuted / Inconclusive — must match Phase 1 claim]` is structurally stronger than a plain disposition label. The parenthetical "must match Phase 1 claim" forces reconciliation between the prior commitment and the outcome — it cannot be filled in without consulting Phase 1. This is mechanically superior to V-02 R1's standard outcome row.

**Signal 2 — Prior rationale field in Phase 1**: V-05 adds `Prior rationale: [why you hold this prior before seeing evidence — name the assumption]` beyond the standard hypothesis fields. This captures the epistemic state before evidence collection, making C-09 (confidence calibration) traceable across the full belief-update arc: prior → evidence → posterior.

**Signal 3 — Complete Phase+section citation coverage for all 5 evidence phases**: The citation block in Phase 6 explicitly maps `because Phase 1` through `because Phase 5` with domain-specific field names. By construction, the model cannot write the synthesis without anchoring to all 5 evidence phases — zero traceability gaps are possible.

**Signal 4 — Consistent table format across all phases**: All 6 phases use markdown tables (never labeled fields), making C-11 auditable at a glance with no format-switching. This is the most consistent rendering surface in the round.

**Signal 5 — Zero interpretive risk**: Phase+section citation format matches the rubric example exactly; all six domains are present; inertia-first is enforced by row ordering; hypothesis disposition is explicitly tied to Phase 1. No criterion requires scorer interpretation to pass.

---

### Round 2 Verdict

All five R2 variations reach Gold — the targeted intervention (making C-11 and C-12 commitments explicit in every variation) succeeded completely. The R1 failure modes (C-11/C-12 absent) are fully resolved. The round is now a quality contest rather than a pass/fail contest.

The one remaining structural risk is the C-12 FID-vs-Phase+section ambiguity (V-03, V-04). If a future rubric version makes this explicit, FID format is worth preserving — it is strictly more precise than Phase+section. A potential R3 direction: prescribe FID as an additional citation format option, removing the interpretive risk while gaining FID's per-row precision.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Anchor linkage in synthesis: 'Hypothesis outcome — must match Phase N claim' forces reconciliation with the prior commitment rather than free-form disposition labeling", "Prior rationale field captures epistemic state before evidence collection, making confidence calibration traceable across the full belief-update arc", "Phase+section citation coverage mapped to all 5 evidence phases by construction — synthesis cannot be written without anchoring to every domain", "FID citation format (V-03, V-04) is strictly more precise than Phase+section but carries interpretive risk; future rubric should explicitly permit both formats"]}
```
