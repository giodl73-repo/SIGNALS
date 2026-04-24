## Scoring: campaign-specify Round 3

Evaluating five variations against the v3 rubric. No trace artifact available; scoring against skill prompt structure.

---

### V-01 — Inertia Framing (loss-first Phase 0 ordering)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Three artifacts produced | **PASS** | Phases 1-3 each save to disk; completion check requires active write if any missing |
| C-02 | Spec six required sections | **PASS** | Phase 1 names all six explicitly with no-skip rule |
| C-03 | Proposal 3+ options + Do Nothing | **PASS** | "Option 1 MUST be named Do Nothing"; description/pros/cons/risk/effort required; recommendation section included |
| C-04 | Pitch three audience versions | **PASS** | Exec, Dev, Maker versions + Anti-Positioning as separate section |
| C-05 | Cross-artifact consistency | **PASS** | Phase 0 inertia costs flow by reference into spec (User Problem), proposal (options), pitch (hooks) — consistency by construction |
| C-06 | Self-review flags gaps | **PASS** | "Cite at least one specific gap. 'No gaps found' fails this section." |
| C-07 | Anti-positioning section | **PASS** | Phase 3 explicitly requires Anti-Positioning as separate section with 3-5 "This is not..." statements |
| C-08 | Proposal recommendation cites trade-off | **PASS** | Template requires "over [other rejected option] because [cite specific trade-off traceable to options analysis]" |
| C-09 | Scout signal pull-through | **PASS** | Phase 0c globs scout/**/*.md; per-phase targeted re-pulls in Phases 1-3 |
| C-10 | Audience voice differentiation | **PASS** | Each phase-3 version opens with the audience-specific Phase 0 inertia cost; exec=ROI, dev=capability, maker=plain-language workflow |
| C-11 | Completion check fail-safe | **PASS** | "Write it now. Do not emit a completion summary until all three files exist on disk. A warning... is not a substitute." Active write gate with explicit prohibition on warnings. |
| C-12 | Phase 0 audience framing pre-write | **PASS** | Step 0a (inertia costs) → Step 0b (voice contracts) → Step 0c (scout) — all precede Phase 1 |
| C-13 | Namespace-targeted per-phase scout pull | **PASS** | Phase 0c: scout/**; Phase 1: scout/ broadly; Phase 2: scout-feasibility/; Phase 3: scout-positioning/ |
| C-14 | Per-audience inertia cost in Phase 0 | **PASS** | Step 0a requires named loss for each audience with explicit required form; gate: "Do not advance to Step 0b until all three inertia costs are complete." Strongest structural enforcement of any variation. |
| C-15 | Do Nothing as named falsifiable baseline | **PASS** | Template: "over **Do Nothing** because [cite the exact Phase 0 inertia cost]." Explicitly references C-15 by name; "implicit defeat... fails." |

**Essential**: 5/5 **Recommended**: 3/3 **Aspirational**: 7/7
**Composite**: 60 + 30 + 10 = **100.0**

---

### V-02 — Output Format (tabular Do Nothing comparison)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Three artifacts | **PASS** | Phases 1-3 save to disk; completion check active write gate |
| C-02 | Spec six sections | **PASS** | Phase 1 lists all six with explicit names; no-skip rule |
| C-03 | Proposal 3+ options + Do Nothing | **PASS** | "Do Nothing as the first row"; minimum three rows; recommendation section required |
| C-04 | Pitch three audience versions | **PASS** | Exec, Dev, Maker versions + Anti-Positioning as fourth named section |
| C-05 | Cross-artifact consistency | **PASS** | Step 0b inertia costs routed into proposal Audience impact column and pitch opening hooks — consistent by table reference |
| C-06 | Self-review flags gaps | **PASS** | "'No gaps' fails" |
| C-07 | Anti-positioning section | **PASS** | Explicit fourth section in Phase 3 |
| C-08 | Trade-off rationale | **PASS** | "cite specific Risk or Cons difference — traceable to the table above" |
| C-09 | Scout signal pull-through | **PASS** | Three targeted scout pulls across phases |
| C-10 | Audience voice differentiation | **PASS** | Per-version opening instructions with "Do not open with..." guards; distinct voice registers from Phase 0 |
| C-11 | Completion check fail-safe | **PASS** | "If any file is missing: write it now. Do not stop until all three files exist." |
| C-12 | Phase 0 audience framing pre-write | **PASS** | Step 0a voice contracts, Step 0b inertia costs — both in Phase 0, preceding Phase 1 |
| C-13 | Namespace-targeted per-phase scout pull | **PASS** | Phase 0c: scout/**; Phase 1: broadly; Phase 2: scout-feasibility/; Phase 3: scout-positioning/ |
| C-14 | Per-audience inertia cost in Phase 0 | **PASS** | Step 0b tabular format: three rows (Exec/Dev/Maker) each requiring "[specific ...]" cost. Structural table enforcement slightly weaker than V-01 gate but broader scope. _Note: risk of model inventing rather than referencing Phase 0 in proposal table cells._ |
| C-15 | Do Nothing named falsifiable baseline | **PASS** | "We reject **Do Nothing** because [cite specific Audience impact cell — name which cost is decisive and why it cannot be absorbed]." Cell citation grounds defeat in table. |

**Essential**: 5/5 **Recommended**: 3/3 **Aspirational**: 7/7
**Composite**: 60 + 30 + 10 = **100.0**

---

### V-03 — Lifecycle Emphasis (Phase 0 heavy, phases 1-3 lean)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Three artifacts | **PASS** | Phases 1-3 save to disk; completion check with write gate |
| C-02 | Spec six sections | **PASS** | Phase 1 names all six |
| C-03 | Proposal 3+ options + Do Nothing | **PASS** | "minimum three, one must be **Do Nothing**"; recommendation template included |
| C-04 | Pitch three audience versions | **PASS** | Four sections including Anti-Positioning |
| C-05 | Cross-artifact consistency | **PASS** | Phase 0d voice contracts feed Phase 3; Phase 0c inertia costs feed Phase 1 and 2 by reference |
| C-06 | Self-review flags gaps | **PASS** | "(one named gap; 'no gaps' fails)" |
| C-07 | Anti-positioning section | **PASS** | Explicit fourth section with 3-5 statements |
| C-08 | Trade-off rationale | **PASS** | "name the specific trade-off from the options analysis" |
| C-09 | Scout signal pull-through | **PASS** | Phase 0a scout inventory with per-phase routing; targeted re-queries in Phases 1-3 |
| C-10 | Audience voice differentiation | **PASS** | "Each version must open from a distinct Phase 0d voice contract — not the same frame reworded. Exec leads with outcomes. Dev leads with capability. Maker leads with workflow." |
| C-11 | Completion check fail-safe | **PASS** | "If any is missing: write it now before stopping." Active gate. |
| C-12 | Phase 0 audience framing pre-write | **PASS** | Five full steps (0a-0e) including voice contracts (0d) precede Phase 1 |
| C-13 | Namespace-targeted per-phase scout pull | **PASS** | Phase 0a: scout/**; Phase 1: broadly; Phase 2: scout-feasibility/; Phase 3: scout-positioning/ |
| C-14 | Per-audience inertia cost in Phase 0 | **PARTIAL** | Step 0c has three explicit fields with "Vague answers fail this step" — but this is advisory, not a structural gate. No equivalent of V-01's "Do not advance until all three complete." A model under context pressure can produce shallow entries and proceed. The fields exist; the enforcement does not. |
| C-15 | Do Nothing named falsifiable baseline | **PASS** | Template: "over **Do Nothing** because [cite the Phase 0e Do Nothing baseline — name which cost is decisive]." Explicit named defeat; cross-reference to Phase 0e slightly vulnerable to context decay but requirement is unambiguous. |

**Essential**: 5/5 **Recommended**: 3/3 **Aspirational**: 6/7 (C-14 PARTIAL → FAIL under strict scoring)
**Composite**: 60 + 30 + (6/7 × 10) = 60 + 30 + 8.57 = **98.6**

---

### V-04 — Combined: Inertia framing + Do Nothing as named competitor

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Three artifacts | **PASS** | Per-artifact write gate: "exists? If not: write now" × 3 |
| C-02 | Spec six sections | **PASS** | "Six required sections. Do not skip or merge." |
| C-03 | Proposal 3+ options + Do Nothing | **PASS** | "Do Nothing must be Option 1"; description/pros/cons/risk/effort required; "Against Do Nothing" + "Against [other]" recommendation blocks |
| C-04 | Pitch three audience versions | **PASS** | Exec, Dev, Maker + Anti-Positioning; voice differentiation check enforced at end |
| C-05 | Cross-artifact consistency | **PASS** | Phase 0c inertia costs flow into spec (User Problem), proposal (Option 1 risk entry), pitch (hooks) — competitor profile established once, referenced throughout |
| C-06 | Self-review flags gaps | **PASS** | "At least one named gap. Cite which section. 'No gaps found' fails." |
| C-07 | Anti-positioning section | **PASS** | "3-5 'This is not...' statements. Separate from the three versions above." |
| C-08 | Trade-off rationale | **PASS** | "Against [other option]" block: "cite specific trade-off traceable to risk or effort above" |
| C-09 | Scout signal pull-through | **PASS** | Phase 0a globs with relevance routing; per-phase targeted pulls in Phases 1-3 |
| C-10 | Audience voice differentiation | **PASS** | Per-version opening instructions; voice differentiation check: "If all three open with the same frame, rewrite until distinct." |
| C-11 | Completion check fail-safe | **PASS** | Per-artifact: "exists? If not: write now" — three explicit write gates |
| C-12 | Phase 0 audience framing pre-write | **PASS** | Phase 0 includes Do Nothing profile (0b) + inertia costs (0c) + voice contracts (0d) — all before Phase 1 |
| C-13 | Namespace-targeted per-phase scout pull | **PASS** | Phase 0a: scout/**; Phase 1: broadly; Phase 2: scout-feasibility/; Phase 3: scout-positioning/ |
| C-14 | Per-audience inertia cost in Phase 0 | **PASS** | Step 0c: three fields with "concrete and specific to that audience's context"; "Quantity or specific scenario preferred" raises bar. The Do Nothing profile in Step 0b makes costs necessary to characterize the competitor — structural pressure beyond just a field label. |
| C-15 | Do Nothing named falsifiable baseline | **PASS** | "Against Do Nothing" block: "Do Nothing perpetuates [cite most decisive Phase 0c inertia cost — name audience and specific cost]. This cost is not absorbed; it compounds." Strongest C-15 structure: named block, cited cost, stability argument. Explicit prohibition on implicit defeat. |

**Essential**: 5/5 **Recommended**: 3/3 **Aspirational**: 7/7
**Composite**: 60 + 30 + 10 = **100.0**

Distinguishing strength: Do Nothing introduced as a **named competitor with a profile** (current state, hidden cost, good-enough threshold, breaking triggers) in Step 0b — this changes the cognitive frame for all subsequent phases. C-15 becomes structurally unavoidable when the competitor was introduced and characterized before any artifact was written.

---

### V-05 — Combined: All axes (full armoring)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Three artifacts | **PASS** | Tabular completion check: per-row "Exists? → write now" gate; "A missing artifact is not a completion state." |
| C-02 | Spec six sections | **PASS** | All six named; no-skip rule |
| C-03 | Proposal 3+ options + Do Nothing | **PASS** | "Do Nothing must be row 1"; tabular options; "Defeating Do Nothing" block in recommendation |
| C-04 | Pitch three audience versions | **PASS** | Three versions + Anti-Positioning; voice differentiation check before saving |
| C-05 | Cross-artifact consistency | **PASS** | Step 0c costs flow into spec (User Problem), proposal (Do Nothing row Audience impact), pitch (opening hooks) — triple reference path, consistency by construction |
| C-06 | Self-review flags gaps | **PASS** | "'No gaps found' fails." |
| C-07 | Anti-positioning section | **PASS** | Explicit named section with 3-5 statements |
| C-08 | Trade-off rationale | **PASS** | "cite specific Risk or Effort difference traceable to the table above — not a preference statement" |
| C-09 | Scout signal pull-through | **PASS** | Step 0a routing table assigns files to phases; per-phase targeted pulls; final index requires listing scout files used per phase |
| C-10 | Audience voice differentiation | **PASS** | Per-version opening instructions + explicit voice differentiation check pre-save |
| C-11 | Completion check fail-safe | **PASS** | Tabular format: Artifact/Path/Exists? → "For any row where 'Exists?' is No: write the artifact now." Most structurally explicit completion enforcement of any variation. |
| C-12 | Phase 0 audience framing pre-write | **PASS** | Five steps (0a-0e) including voice contracts (0d) before Phase 1; full Do Nothing baseline (0e) before proposal writing |
| C-13 | Namespace-targeted per-phase scout pull | **PASS** | Step 0a file list with phase routing; Phase 1: broadly; Phase 2: scout-feasibility/; Phase 3: scout-positioning/; final index confirms scout files used per phase |
| C-14 | Per-audience inertia cost in Phase 0 | **PASS** | Triple enforcement: (1) Step 0c table with per-row cost fields + "Vague answers fail"; (2) Do Nothing row in proposal table with Audience impact column referencing Step 0c; (3) Phase 3 opening hooks require Step 0c costs. Single mechanism failure does not cascade. |
| C-15 | Do Nothing named falsifiable baseline | **PASS** | "Defeating Do Nothing" block: "reject Do Nothing because [specific Audience impact cell — name whose cost is decisive and why it cannot continue to be absorbed]. Do Nothing is not stable: [cite Step 0b stability assessment]." Multi-path defeat: table cell + named block + stability argument. |

**Essential**: 5/5 **Recommended**: 3/3 **Aspirational**: 7/7
**Composite**: 60 + 30 + 10 = **100.0**

Distinguishing strength: redundant independent mechanisms for C-14 and C-15. No single path failure cascades to criterion failure.

---

## Composite Scores

| Variation | Essential | Rec | Asp | Composite | Rank |
|-----------|-----------|-----|-----|-----------|------|
| V-01 | 5/5 | 3/3 | 7/7 | 100.0 | 3 |
| V-02 | 5/5 | 3/3 | 7/7 | 100.0 | 4 |
| V-03 | 5/5 | 3/3 | 6/7 | 98.6 | 5 |
| V-04 | 5/5 | 3/3 | 7/7 | 100.0 | 2 |
| **V-05** | **5/5** | **3/3** | **7/7** | **100.0** | **1** |

**Strength-ordered ranking within the 100s**: V-05 > V-04 > V-01 = V-02 > V-03

All-essential-pass: **all five variations** (100% essential pass rate at the structural level — all R3 variations correctly targeted the v3 criteria).

---

## Excellence Signals from Top Scorers (V-04, V-05)

### Signal 1: Do Nothing as named competitor with a profile
V-04 introduces Do Nothing not as an option to be considered, but as "the one competitor that is always present and never goes away." Phase 0b builds a full profile: current state, hidden cost, good-enough threshold, and when it breaks. This changes the model's cognitive frame — every subsequent artifact is implicitly testing whether the feature defeats this competitor. C-15 becomes structurally unavoidable because the competitor was characterized before any writing began.

### Signal 2: Stability argument in the Do Nothing defeat
V-04 and V-05 add a sentence to the defeat block: "This cost is not absorbed; it compounds." This converts the inertia cost from a static fact into a growing risk — making the time dimension explicit. The rubric's C-15 minimum form doesn't require this, but its presence strengthens the falsification beyond bare preference.

### Signal 3: Redundant per-criterion enforcement paths (V-05)
V-05 satisfies C-14 and C-15 through three independent mechanisms each. C-14: Step 0c table + proposal Do Nothing row Audience impact column + pitch opening hooks. C-15: proposal table cell citation + named "Defeating Do Nothing" block + Step 0b stability assessment. A single path failure cannot cascade to criterion failure. This is an armoring pattern worth formalizing.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Do Nothing introduced as a named competitor with a full profile in Phase 0 (current state, hidden cost, good-enough threshold, breaking triggers) — not just an option, changes cognitive frame for all subsequent phases", "Stability argument in Do Nothing defeat: 'this cost is not absorbed; it compounds' converts static inertia cost into growing risk, strengthens C-15 beyond minimum required form"]}
```
