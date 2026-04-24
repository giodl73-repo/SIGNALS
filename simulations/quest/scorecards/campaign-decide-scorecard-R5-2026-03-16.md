Now I have everything I need to score all five variations. Let me evaluate each against all 20 criteria.

---

# Quest Score — campaign-decide / Round 5

**Rubric**: v5 (20 criteria: 5 essential / 3 recommended / 12 aspirational)
**Denominator change**: /9 → /12 aspirational, each worth 0.83 pts
**Formula**: `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/12 × 10)`

---

## V-01 — C-12 hybrid citation format

Base: R4 V-01 with single-axis change to Because block citation ("because Phase N, F[N]-[seq]").

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Recommendation stated | **PASS** | F5-02 labeled field `[COMMIT/PAUSE/PIVOT/ABANDON]` |
| C-02 | Confidence level stated | **PASS** | F5-03 labeled field `[High/Medium/Low]` |
| C-03 | Six domains represented | **PASS** | Phase 0 (hypothesis), 1 (competitors), 2 (feasibility), 3 (market), 4 (websearch), 5 (synthesis) |
| C-04 | Inertia-first framing | **PASS** | F1-01–F1-03 inertia fields precede F1-04+ rivals by field position; ordering rule stated |
| C-05 | Evidence traceability | **PASS** | Five-slot Because block with one FID citation per phase |
| C-06 | Structured brief format | **PASS** | Section headers per phase + labeled FID rows |
| C-07 | Risk/counter-evidence | **PASS** | F5-05 field with required FID reference |
| C-08 | Hypothesis disposition | **PASS** | F5-01: "resolves F0-01" |
| C-09 | Confidence calibration | **PASS** | F5-04: "cite the specific FIDs that drove this rating" |
| C-10 | Actionable next step | **PASS** | F5-06: COMMIT/no-build conditioned branches |
| C-11 | Per-phase required schema | **PASS** | FID-labeled required rows in every phase section |
| C-12 | Templated citation syntax | **PASS** | "because Phase N, F[N]-[seq]" — Phase prefix satisfies rubric example; FID key provides unique auditable reference. Zero strict-scorer risk. |
| C-13 | Hypothesis-prior anchoring | **PASS** | Phase 0 precedes Phase 1–4 by document position |
| C-14 | Cross-phase citation span | **PASS** | 5 labeled slots enforce 5 distinct phases by construction |
| C-15 | Per-finding unique keys | **PASS** | FINDING REGISTER pre-assigns F0-01..F5-06 |
| C-16 | Register pre-seeded | **PASS** | Standalone FINDING REGISTER with "—" skeleton rows appears before Phase 0 — strict and liberal |
| C-17 | Per-phase Because slot | **PASS** | Exactly 5 labeled slots for 5 evidence phases |
| C-18 | Counter-evidence FID-pinned | **PASS** | F5-05: "cite the FID it qualifies" |
| C-19 | Hypothesis resolution FID-anchored | **PASS** | F5-01: "resolves F0-01" — FID citation present |
| C-20 | Phase gate in section headers | **PASS** | `[COMPLETE BEFORE PHASE 1]` in Phase 0 header; `[COMPLETE BEFORE PHASE 0]` in FINDING REGISTER header |

**Essential**: 5/5 × 60 = **60.0**
**Recommended**: 3/3 × 30 = **30.0**
**Aspirational**: 12/12 × 10 = **10.0**
**Composite: 100.0** — no residual strict risk. R5 axis (hybrid citation) eliminates the only remaining ambiguity from R4 V-01.

---

## V-02 — Inertia elevation (Phase 1a/1b sub-section structure)

Base: R4 V-01. Single axis: Phase 1 split into Phase 1a (Inertia) gated before Phase 1b (Rivals). Because block retains FID-only citation `because F[N]-[seq]` (no Phase prefix).

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Recommendation stated | **PASS** | F5-02 labeled |
| C-02 | Confidence level stated | **PASS** | F5-03 labeled |
| C-03 | Six domains represented | **PASS** | Phases 0–5 cover all six |
| C-04 | Inertia-first framing | **PASS** | Phase 1a section header precedes Phase 1b at section boundary — structural enforcement, stronger than V-01's field-order rule |
| C-05 | Evidence traceability | **PASS** | Five-slot Because block with FID citations |
| C-06 | Structured brief format | **PASS** | Section + sub-section headers + FID rows |
| C-07 | Risk/counter-evidence | **PASS** | F5-05 with FID reference |
| C-08 | Hypothesis disposition | **PASS** | F5-01 with "resolves F0-01" |
| C-09 | Confidence calibration | **PASS** | F5-04 FID-driven |
| C-10 | Actionable next step | **PASS** | F5-06 conditioned |
| C-11 | Per-phase required schema | **PASS** | FID rows per phase |
| C-12 | Templated citation syntax | **PASS (liberal)** / **RISK (strict)** | "because F[N]-[seq]" — FID satisfies "mechanically auditable"; Phase prefix absent. Liberal scorers accept; strict scorers may require the Phase token. Low-to-moderate risk. |
| C-13 | Hypothesis-prior anchoring | **PASS** | Phase 0 before Phase 1 by document position |
| C-14 | Cross-phase citation span | **PASS** | 5 slots × 5 phases |
| C-15 | Per-finding unique keys | **PASS** | FINDING REGISTER with 1a/1b sub-labels |
| C-16 | Register pre-seeded | **PASS** | Skeleton rows before Phase 0 |
| C-17 | Per-phase Because slot | **PASS** | 5 slots for 5 phases (Phase 1 = one slot covering 1a+1b; slot count unchanged) |
| C-18 | Counter-evidence FID-pinned | **PASS** | F5-05 FID required |
| C-19 | Hypothesis resolution FID-anchored | **PASS** | F5-01 "resolves F0-01" |
| C-20 | Phase gate in section headers | **PASS** | Three gate annotations: FINDING REGISTER, Phase 0, Phase 1a (`[COMPLETE BEFORE PHASE 1b]`) — reinforced pattern |

**Essential**: 5/5 × 60 = **60.0**
**Recommended**: 3/3 × 30 = **30.0**
**Aspirational (liberal)**: 12/12 × 10 = **10.0** → Composite: **100.0**
**Aspirational (strict C-12)**: 11/12 × 10 = **9.17** → Composite: **99.2**

---

## V-03 — C-20 graft on non-FID template (boundary test)

Base: R4 V-02 (table-per-phase, no FIDs, hypothesis Phase 4 after scouting). Single axis: `[COMPLETE BEFORE PHASE N]` added to all section headers.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Recommendation stated | **PASS** | Recommendation table row |
| C-02 | Confidence level stated | **PASS** | Confidence table row |
| C-03 | Six domains represented | **PASS** | Phases 1–6 cover competitors, feasibility, market, hypothesis, websearch, synthesis |
| C-04 | Inertia-first framing | **PASS** | Inertia rows (status-quo, switching cost, good-enough threshold) appear before named rival rows in table; "(Inertia rows must precede named rival rows.)" instruction present |
| C-05 | Evidence traceability | **PASS** | Because block with five phase+row citations |
| C-06 | Structured brief format | **PASS** | Section headers + table per phase |
| C-07 | Risk/counter-evidence | **PASS** | Counter-evidence row in synthesis table |
| C-08 | Hypothesis disposition | **PASS** | Hypothesis outcome row |
| C-09 | Confidence calibration | **PASS** | Confidence rationale: "name specific evidence gaps or strengths — not just the label" |
| C-10 | Actionable next step | **PASS** | Conditioned next step row |
| C-11 | Per-phase required schema | **PASS** | Table schema per phase |
| C-12 | Templated citation syntax | **PASS** | "because Phase N, [row reference]" — exact rubric example format |
| C-13 | Hypothesis-prior anchoring | **FAIL** | Hypothesis is Phase 4, after Phase 1 (competitors), 2 (feasibility), 3 (market) — not a genuine prior |
| C-14 | Cross-phase citation span | **PASS** | 5 labeled slots × 5 phases |
| C-15 | Per-finding unique keys | **FAIL** | No FID system — table rows have no unique identifiers |
| C-16 | Register pre-seeded | **FAIL** | No FID system, no register |
| C-17 | Per-phase Because slot | **PASS** | "SLOT COUNT (5) = PHASE COUNT (5)" formula declared |
| C-18 | Counter-evidence FID-pinned | **FAIL** | C-15 prerequisite absent — no keys to cite |
| C-19 | Hypothesis resolution FID-anchored | **FAIL** | C-15 prerequisite absent — disposition label only |
| C-20 | Phase gate in section headers | **PASS** | All 5 evidence phase headers carry `[COMPLETE BEFORE PHASE N]`. Gates present at structural boundaries. C-20 passes independently of C-13 — the criterion measures co-location of gate with boundary, not whether the gate enforces the correct ordering. |

Aspirational passes: C-09, C-10, C-11, C-12, C-14, C-17, C-20 = **7/12**
Fails: C-13, C-15, C-16, C-18, C-19

**Essential**: 5/5 × 60 = **60.0**
**Recommended**: 3/3 × 30 = **30.0**
**Aspirational**: 7/12 × 10 = **5.83**
**Composite: 95.83** (+0.83 from R4 V-02's 95.0 — exactly one criterion gained via C-20 graft)

> Boundary test confirmed: C-20 PASS + C-13 FAIL simultaneously. C-20 is a structural format criterion, not an ordering correctness criterion. The graft yields only 0.83 pts. Adding a full FID system (C-15 → C-16, C-18, C-19 = +4 criteria, +3.33 pts) is 4× higher yield.

---

## V-04 — Combined: C-12 hybrid + Phase 1a/1b inertia elevation

Both R5 axes applied to R4 V-01 base. Hybrid citation eliminates C-12 strict risk; Phase 1a/1b section split elevates C-04 to structural enforcement.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Recommendation stated | **PASS** | F5-02 labeled |
| C-02 | Confidence level stated | **PASS** | F5-03 labeled |
| C-03 | Six domains represented | **PASS** | All six covered |
| C-04 | Inertia-first framing | **PASS** | Phase 1a (Inertia Analysis) is a complete, gated section before Phase 1b (Named Rivals) — structural at the section level, not instructional |
| C-05 | Evidence traceability | **PASS** | Five-slot Because block, hybrid citations |
| C-06 | Structured brief format | **PASS** | Section + sub-section hierarchy |
| C-07 | Risk/counter-evidence | **PASS** | F5-05 with FID required |
| C-08 | Hypothesis disposition | **PASS** | F5-01 "resolves F0-01" |
| C-09 | Confidence calibration | **PASS** | F5-04 FID-driven rationale |
| C-10 | Actionable next step | **PASS** | F5-06 conditioned |
| C-11 | Per-phase required schema | **PASS** | FID rows per phase including 1a/1b sub-labels |
| C-12 | Templated citation syntax | **PASS** | "because Phase N, F[N]-[seq]" — dual-token: Phase prefix satisfies rubric example; FID key satisfies mechanical auditability. No residual risk under any interpretation. |
| C-13 | Hypothesis-prior anchoring | **PASS** | Phase 0 before Phase 1 by document position |
| C-14 | Cross-phase citation span | **PASS** | 5 slots × 5 phases by construction |
| C-15 | Per-finding unique keys | **PASS** | Full FINDING REGISTER with Phase 1a/1b sub-labels |
| C-16 | Register pre-seeded | **PASS** | Skeleton rows before Phase 0 — strict and liberal |
| C-17 | Per-phase Because slot | **PASS** | 5 slots for 5 phases (Phase 1 = one slot covering 1a+1b) |
| C-18 | Counter-evidence FID-pinned | **PASS** | F5-05 FID required |
| C-19 | Hypothesis resolution FID-anchored | **PASS** | F5-01 "resolves F0-01" |
| C-20 | Phase gate in section headers | **PASS** | Three gate points: FINDING REGISTER, Phase 0, Phase 1a — deepest annotation chain of all variants |

**Essential**: 5/5 × 60 = **60.0**
**Recommended**: 3/3 × 30 = **30.0**
**Aspirational**: 12/12 × 10 = **10.0**
**Composite: 100.0** — zero residual risks under strict or liberal interpretation.

---

## V-05 — Combined: all R5 axes + conversational phrasing register

V-04 structure with conversational prose replacing imperative headers. FINDING REGISTER retains `[COMPLETE BEFORE PHASE 0]`. Phase 0 and Phase 1a headers drop bracket annotations in favor of prose body instructions.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Recommendation stated | **PASS** | F5-02 labeled |
| C-02 | Confidence level stated | **PASS** | F5-03 labeled |
| C-03 | Six domains represented | **PASS** | All six covered |
| C-04 | Inertia-first framing | **PASS** | Phase 1a section still named "Inertia Analysis" and appears before Phase 1b; prose body says "Start here" and "Complete Phase 1a before filling Phase 1b." |
| C-05 | Evidence traceability | **PASS** | Five-slot Because block with hybrid citations |
| C-06 | Structured brief format | **PASS** | Section hierarchy preserved |
| C-07 | Risk/counter-evidence | **PASS** | F5-05 with FID reference |
| C-08 | Hypothesis disposition | **PASS** | F5-01 "resolves F0-01" |
| C-09 | Confidence calibration | **PASS** | F5-04 FID-driven |
| C-10 | Actionable next step | **PASS** | F5-06 conditioned |
| C-11 | Per-phase required schema | **PASS** | FID rows per phase |
| C-12 | Templated citation syntax | **PASS** | "because Phase N, F[N]-[seq]" — hybrid format retained, no strict risk |
| C-13 | Hypothesis-prior anchoring | **PASS** | Phase 0 before Phase 1 by document position |
| C-14 | Cross-phase citation span | **PASS** | 5 slots × 5 phases |
| C-15 | Per-finding unique keys | **PASS** | FINDING REGISTER present |
| C-16 | Register pre-seeded | **PASS** | Skeleton rows before Phase 0 |
| C-17 | Per-phase Because slot | **PASS** | 5 slots for 5 phases |
| C-18 | Counter-evidence FID-pinned | **PASS** | F5-05 FID required |
| C-19 | Hypothesis resolution FID-anchored | **PASS** | F5-01 "resolves F0-01" |
| C-20 | Phase gate in section headers | **CONDITIONAL** | FINDING REGISTER header retains `[COMPLETE BEFORE PHASE 0]`. Phase 0 header: prose preamble only, no bracket annotation. Phase 1a header: prose body only ("Complete Phase 1a before filling Phase 1b"), no bracket annotation. **Liberal**: one annotated header at a structural boundary = PASS. **Strict**: the criterion requires gates to appear at the boundary they govern — Phase 0's gate (which governs Phase 1 entry) is in a prose body, not the Phase 0 header itself = FAIL. |

**Essential**: 5/5 × 60 = **60.0**
**Recommended**: 3/3 × 30 = **30.0**
**Aspirational (liberal C-20)**: 12/12 × 10 = **10.0** → Composite: **100.0**
**Aspirational (strict C-20)**: 11/12 × 10 = **9.17** → Composite: **99.2**

---

## Composite Score Table

| Variation | Essential | Recommended | Aspirational (liberal) | **Composite (liberal)** | Composite (strict) |
|-----------|-----------|-------------|----------------------|-------------------------|--------------------|
| V-01 | 60.0 | 30.0 | 10.0 (12/12) | **100.0** | 100.0 |
| V-02 | 60.0 | 30.0 | 10.0 (12/12) | **100.0** | 99.2 (C-12 risk) |
| V-03 | 60.0 | 30.0 | 5.83 (7/12) | **95.83** | 95.83 |
| V-04 | 60.0 | 30.0 | 10.0 (12/12) | **100.0** | **100.0** |
| V-05 | 60.0 | 30.0 | 10.0 (12/12) | **100.0** | 99.2 (C-20 risk) |

---

## Ranking

1. **V-04** — 100.0 (zero residual risk under all interpretations)
2. **V-01** — 100.0 (zero residual risk — C-12 hybrid closes R4's only remaining ambiguity)
3. **V-02** — 100.0 liberal / 99.2 strict (C-12 FID-only risk retained)
4. **V-05** — 100.0 liberal / 99.2 strict (C-20 partial-annotation risk)
5. **V-03** — 95.83 (FID system absent, C-13/C-15/C-16/C-18/C-19 all fail; C-20 graft yields only 0.83 pts)

**Predicted ranking confirmed**: V-04 >= V-01 > V-02 = V-05 >> V-03.

V-04 is the unambiguous R5 winner because it combines both axes: hybrid citation eliminates C-12 strict risk, and Phase 1a/1b section split elevates C-04 to structural enforcement without any scoring trade-offs.

---

## Excellence Signals (from V-04)

**Signal 1 — Dual-token citation as interpreter-proof traceability.**
The hybrid "because Phase N, F[N]-[seq]" format contains both tokens that any scorer might require: the Phase prefix satisfies the rubric's prose example ("because Phase [N], [section reference]"); the FID key satisfies the mechanical auditability requirement without positional prose lookup. A citation that satisfies two competing interpretations simultaneously eliminates the strict/liberal split entirely. This is a general principle: when rubric example syntax and structural requirement diverge, the winning format includes both tokens rather than choosing one.

**Signal 2 — Section-boundary inertia gating makes correctness structural.**
Splitting Phase 1 into Phase 1a (Inertia Analysis) `[COMPLETE BEFORE PHASE 1b]` and Phase 1b (Named Rivals) moves C-04 compliance from instructional to structural. In V-01, inertia-first is enforced by a field-ordering rule in prose — a model can misread it. In V-04, the document structure names inertia first at the section level; filling Phase 1b content before Phase 1a requires actively skipping a labeled section heading. The pattern generalizes: any ordering requirement that is expressible as a section sequence is better enforced by section structure than by instructions within a section.

**Signal 3 — Multi-level gate chain creates a machine-readable sequencing contract.**
V-04 carries three gate annotations at distinct structural levels: `[COMPLETE BEFORE PHASE 0]` on the FINDING REGISTER (register-level), `[COMPLETE BEFORE PHASE 1]` on Phase 0 (phase-level), `[COMPLETE BEFORE PHASE 1b]` on Phase 1a (sub-phase-level). Each annotation governs the boundary it is attached to. The chain makes the entire execution order readable by scanning only section headers — no prose parsing required. This is the machine-readability property C-20 was designed to measure.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["dual-token citation format (Phase N + FID key) eliminates strict/liberal C-12 split by satisfying both interpretations simultaneously", "section-boundary inertia gating (Phase 1a/1b sub-section split with gate header) moves C-04 compliance from instructional to structural enforcement"]}
```
