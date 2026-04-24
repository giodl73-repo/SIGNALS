# trace-state — Round 11 Scorecard

## V-01 Evaluation

**Variation axis**: Standards Registry (sealed pre-game) + fully expanded Phase 3E peer template + mandatory negative-path step in trace

---

### Essential Criteria (60 pts, 12 pts each)

| ID | Verdict | Evidence Note |
|----|---------|---------------|
| C-01 | **PASS** | Part 2 step template explicitly requires `Before state: [S-ID] [State] — {field: value}` and `After state:` for every step. |
| C-02 | **PASS** | Step template requires `Preconditions checked: [list each, verdict: MET / NOT MET]` and `Postconditions verified: [list each, verdict: HOLDS / VIOLATED]`. |
| C-03 | **PASS** | INV-ID registry in 1C, minimum 2 invariants with scope and falsifiable threshold. |
| C-04 | **PASS** | Five-phase sweep (3A–3E) mandated; each phase targets a named anomaly class. |
| C-05 | **PASS** | Opening line: "You are a domain expert in one of three domains: Sales, Customer Service, or Finance." |

**Essential subtotal: 60 / 60**

---

### Recommended Criteria (30 pts, 10 pts each)

| ID | Verdict | Evidence Note |
|----|---------|---------------|
| C-06 | **PASS** | Part 2 explicitly requires "at least one negative-path step: a `[REJECTED]` operation where the guard condition fires, the before-state is shown, and the rejection reason is stated. The entity must remain in its before-state after rejection." — direct V-01 closure. |
| C-07 | **PASS** | `Step N: [OP-ID] [Operation Name]` numbered format with structured sub-fields enforces mechanical replayability. |
| C-08 | **PASS** | Phase 3D targets race conditions with explicit dual-pass sweep and phase exit gate. |

**Recommended subtotal: 30 / 30**

---

### Aspirational Criteria (10 pts, 0.345 pts each, 29 criteria)

| ID | Verdict | Evidence Note |
|----|---------|---------------|
| C-09 | **PASS** | All four anomaly types in dedicated phases (3A–3D), plus undeclared references (3E). |
| C-10 | **PASS** | Multiple structured tables: state registry, op registry, invariant registry, finding tables per phase. |
| C-11 | **PASS** | Each phase has a sweep table with mandatory Finding-ID rows; no entry = no finding. |
| C-12 | **PASS** | `OP-ID / S-ID affected` column appears in every finding table; IDs declared in 1B/1A and cross-referenced throughout. |
| C-13 | **PASS** | 1A State Registry has `Entry Condition` and `Exit Condition` columns explicitly. |
| C-14 | **PASS** | Evidence Strength exit gate ("at least one finding at strength ≥ 2") functions as minimum-found threshold per phase. |
| C-15 | **PASS** | S-IDs, OP-IDs, INV-IDs all declared in registries and referenced in finding tables and trace steps. |
| C-16 | **PASS** | Phase 3E exists as a named phase targeting undeclared references. |
| C-17 | **PARTIAL** | Column is `OP-ID / S-ID affected` (combined), not three separate columns; no standalone INV-ID column in finding tables. Blank-cell detection partially enabled. |
| C-18 | **PASS** | Part 3 pre-sweep hypothesis table with Predicted Count, Confidence (L/M/H), and Specific Predicted Scenario per phase. |
| C-19 | **PASS** | Exit gate checkbox: "Evidence Strength gate — at least one finding at strength ≥ 2, OR Gap Record explicitly explains why no finding met the threshold." |
| C-20 | **PASS** | INV-ID registry requires "at least one must be numeric or temporal with a precise threshold (e.g., 'any decrease > $0.00 is a violation')." |
| C-21 | **FAIL** | No post-sweep reconciliation table present; Part 3 hypothesis table has no Surprise column pairing prediction outcomes to actuals. |
| C-22 | **PASS** | "THE SCORING PROTOCOL: Assign evidence strength the moment you record a finding." Explicit point-of-discovery instruction. |
| C-23 | **PASS** | `THE SCORING PROTOCOL` is a named discipline with verbal instruction (`Say: "I am scoring this [1/2/3] because..."`), self-correction gate ("If you cannot complete the sentence, the evidence is insufficient — do not record the finding"), and placement at detection entry point, not end-of-sweep. |
| C-24 | **PASS** | Three explicit exit gate checkboxes (Findings List, Evidence Strength, Gap Record) in Phase 3A exit certification; Phases 3B–3E inherit same structure. |
| C-25 | **FAIL** | No C/FP/FN three-value taxonomy; no computed calibration score; reconciliation table absent entirely. |
| C-26 | **PASS** | Phases 3A–3E are top-level numbered phases with LOCKED/OPEN status; sequential commitment enforced by explicit COMPLETE declarations as unlock signals. |
| C-27 | **PASS** | Pass 1 and Pass 2 both include: "If no finding in this pass: name the specific [declaration-table values / trace steps and state conditions] that would need to exist to produce a finding." |
| C-28 | **PASS** | Pass 1 (Declaration-Only) and Pass 2 (Trace-Diff) are structurally separate named passes per phase; declaration-present-but-trace-absent is explicitly a finding type. |
| C-29 | **PASS** | C-29's function subsumed and exceeded by C-32 (unconditional Role B Gap Record); Role B fires on every phase regardless of finding count, which satisfies the gap-documentation requirement at higher rigor. |
| C-30 | **PASS** | Phase 3A has separate `Declaration-Only Finding` and `Trace-Diff Finding` column headers in the finding table; each has its own "if no finding, name what would need to exist" inline gap requirement. |
| C-31 | **PASS** | All phases carry explicit `[STATUS: LOCKED until PHASE N-1: COMPLETE]` and emit `PHASE N: COMPLETE [Unlocks Phase N+1]` as the named unlock signal. |
| C-32 | **PASS** | `Role B: GAP RECORD [UNCONDITIONAL — fires regardless of finding count]` stated explicitly in Phase 3A template. |
| C-33 | **PASS** | Every phase emits `{findings list} + {Gap Record}` as the structurally mandatory pair; absence of either is a detectable error. |
| C-34 | **PASS** | Phase 3A explicitly states: "*The Gap Record is the unlock signal for the Phase 3A exit gate.*" |
| C-35 | **PASS** | PART 0 Standards Registry sealed before Part 1 opens; every phase restates its row verbatim before detection runs; standard cannot be revised after findings are known. |
| C-36 | **PARTIAL** | Phase 3E is declared "a full structural peer of Phases 3A–3D" with the correct components listed; Role B restatement prompt is present. But the full Phase 3E sweep table, dual-column detection, and three-gate exit certification are not expanded in the template body (cuts off at "Trace artifact: placeholder"). Intent clear, template incomplete. |
| C-37 | **PASS** | Evidence Strength gate is a named checkbox in exit certification; blocks PHASE N: COMPLETE until satisfied; creates the three-gate model (Findings + Evidence Strength + Gap Record). |

**Aspirational subtotal**:
- PASS: 25 × 0.345 = **8.625**
- PARTIAL: 2 × 0.172 = **0.344**
- FAIL: 2 × 0.000 = **0.000**
- Total: **8.969 / 10.000**

---

### V-01 Composite Score

| Category | Score | Max |
|----------|-------|-----|
| Essential | 60.000 | 60 |
| Recommended | 30.000 | 30 |
| Aspirational | 8.969 | 10 |
| **Total** | **98.969** | **100** |

**Improvement over R10 (93.62)**: C-06 moved from PARTIAL (5/10) to PASS (10/10) → +5.0 pts. C-36 remains PARTIAL (same as R10's truncated Phase 3E). Net gain: +5.35 pts accounting for rounding.

---

### Ranking

| Variation | Score | All Essential Pass |
|-----------|-------|--------------------|
| V-01 | **98.97** | Yes |

*(Only V-01 submitted.)*

---

### Excellence Signals

**Signal 1 — Standards Registry as meta-preamble unlock artifact**
PART 0 is not just a "fill out the table before proceeding" instruction. It emits `STANDARDS REGISTRY: SEALED → PART 1 now OPEN` as an explicit state transition signal — the registry *itself* follows the same lock/unlock mechanics as the phases. This creates a zero-level gate before any declaration work begins, making the entire protocol governed by the same artifact-driven model from the registry through Phase 3E.

**Signal 2 — Role B identity shift from reactive to proactive**
Renaming Role B "Evidence Steward" (vs. "Acquittal Advocate") and defining it in the opening preamble as "locks all evidence standards *before detection begins*" reframes the role's primary identity. The name signals forward-looking commitment, not post-hoc gap-filling. This is not cosmetic: combined with the Standards Registry sealing before Part 1 opens, the role's first action is pre-game standard-locking, not detection-phase response. The identity frames C-35 as a first-class Role B responsibility.

**Remaining gaps after V-01** (for R12 targeting):
- C-17 (separate OP-ID / S-ID / INV-ID columns)
- C-21 (Surprise column in reconciliation table)
- C-25 (C/FP/FN three-value taxonomy)
- C-36 (Phase 3E template body fully expanded)

---

```json
{"top_score": 98.97, "all_essential_pass": true, "new_patterns": ["Standards Registry as meta-preamble unlock artifact: registry completion emits an explicit SEALED→OPEN state transition signal, making the registry-to-Phase-1 handoff a first-class mechanical gate governed by the same lock/unlock model as all other phases", "Role B identity shift at preamble: naming Role B 'Evidence Steward' and defining its primary responsibility as locking evidence standards before detection begins reframes the role from reactive acquittal-documenter to proactive standard-setter, making C-35's pre-detection commitment the role's first-class identity rather than a phase-header formality"]}
```
