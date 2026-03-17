# Quest Score — corps-committee R6

## Criterion-by-Criterion Evaluation

### Baseline Properties (V-01 shown in full — inherited by all variations)

V-01 establishes:  BEFORE YOU START imperative block, Gate 0-B NORM inventory, Phase 0 roster with Designated Challenger (within Phase 0, not pre-Phase-0), Phase 1 discussion grid with Inertia Challenge? column, Decision Check (1.2), Dissent Check (1.3), FAILS entries with C-XX references. Missing: standalone CHAIN CHECK gate, explicit action items section, C-20 pre-Phase-0 Challenger block.

---

### V-01 — NORM Inventory as Phase 0 Structural Backbone

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Committee type instantiated | PASS | BEFORE YOU START block commits type with fail condition per type |
| C-02 | Each participant speaks from role | PASS | Role-voice constraint table hard-enforces domain per role |
| C-03 | Decisions explicitly recorded | PASS | Section 1.2 Decision Check mandates labeled outcome |
| C-04 | Action items with owners | **FAIL** | No dedicated action items section; decision check captures outcomes, not actions+owners |
| C-05 | Dissent represented | PASS | Section 1.3 Dissent Check mandates role-tension identification |
| C-06 | Formal minutes structure | PARTIAL | Phase simulation structure; header/agenda/next-steps not explicitly mandated |
| C-07 | Discussion depth per type | PASS | Grid requires type-specific evidence (metric / risk / trade-off); generic evidence fails |
| C-08 | AMEND honored | PASS | Vacuously satisfied — not invoked |
| C-09 | Pre-mortem outside-in risk | PARTIAL | NORM inventory + Challenger in grid but no dedicated Phase 2 pre-mortem output section |
| C-10 | Charter fidelity traceable | PASS | Section 0.4 names 4 charter constraints before Phase 1 |
| C-11 | Injection as default | PARTIAL | Candidate annotation present in Charter Status column; proof-of-coverage not explicitly required |
| C-12 | Provisional annotation in Phase 0 | PASS | Charter Status column distinguishes Standing / Candidate |
| C-13 | Pre-skeleton imperative block | PASS | BEFORE YOU START block precedes all skeleton filling; per-type fail conditions stated |
| C-14 | FAILS entries cite criterion IDs | PASS | Multiple FAILS entries reference C-XX across all phases |
| C-15 | Phase-gate charter constraints as entry preconditions | PASS | Phase 0 entry requires NORM locked; Phase 1 entry requires Phase 0 complete; charter stated pre-Phase 1 |
| C-16 | Structural table format | PARTIAL | Tables present (roster, discussion grid) but no per-criterion compliance columns; violations require prose reading |
| C-17 | Inertia hypothesis gate | PASS | Gate 0-B poses rubber-stamp question; NORM inventory required before Phase 0 |
| C-18 | NORM-* labeled inventory | PASS | Labeled NORM table with named-belief requirement; at-least-one observable-behavior constraint |
| C-19 | PRE-MORTEM CHAIN CHECK gate | **FAIL** | No standalone CHAIN-1/2/3 block; no Phase 1→2 blocking condition |
| C-20 | Designated Challenger pre-assigned | PARTIAL | Challenger designated in Phase 0 roster with NORM obligation; rationale not committed before Phase 0 begins |

**Essential:** 4/5 → `(4/5)×60 = 48`  
**Recommended:** 2.5/3 → `(2.5/3)×30 = 25`  
**Aspirational:** 9/12 (0.5 for PARTIAL on C-09, C-11, C-16, C-20; 0 for C-19) → `(9/12)×10 = 7.5`  
**Composite: 80.5 — Bronze** (4/5 essential, ≥60)

---

### V-02 — Designated Inertia Challenger Locked Pre-Phase-0

Delta from V-01: Challenger designated as a named pre-Phase-0 block with explicit rationale and NORM label obligation before roster construction. C-20 moves to PASS. All other criteria unchanged.

| Changed | ID | Verdict | Evidence |
|---------|----|---------|---------| 
| ↑ | C-20 | PASS | Pre-Phase-0 block commits specific role, rationale, and NORM obligation before Phase 0 begins |

All others same as V-01.

**Essential:** 4/5 → 48  
**Recommended:** 2.5/3 → 25  
**Aspirational:** 9.5/12 → `(9.5/12)×10 = 7.9`  
**Composite: 80.9 — Bronze**

---

### V-03 — PRE-MORTEM CHAIN CHECK as Hard Blocking Gate

Delta from V-01: Standalone CHAIN-1/2/3 block at Phase 1→2 boundary with DO NOT PROCEED instruction. C-19 → PASS. CHAIN-2 requires non-circular outside-in basis → forces C-09 to PASS.

| Changed | ID | Verdict | Evidence |
|---------|----|---------|---------|
| ↑ | C-19 | PASS | Standalone CHAIN-1/2/3 gate; Phase 2 cannot begin without all three checkpoints confirmed |
| ↑ | C-09 | PASS | CHAIN-2 commits outside-in basis as non-circular precondition; satisfies outside-in risk requirement structurally |

**Essential:** 4/5 → 48  
**Recommended:** 2.5/3 → 25  
**Aspirational:** 10.5/12 → `(10.5/12)×10 = 8.75`  
**Composite: 81.75 — Bronze**

---

### V-04 — Combined: NORM Inventory + Designated Challenger + CHAIN CHECK

Delta from V-01: All three R6 criteria integrated. Challenger pre-Phase-0 (V-02 change) + CHAIN CHECK gate (V-03 change) + existing NORM inventory closes the full inertia traceability loop.

| Changed | ID | Verdict | Evidence |
|---------|----|---------|---------|
| ↑ | C-19 | PASS | CHAIN CHECK gate |
| ↑ | C-20 | PASS | Pre-Phase-0 Challenger block with rationale and NORM obligation |
| ↑ | C-09 | PASS | CHAIN-2 outside-in precondition; Challenger rationale is pre-committed basis |

No action items table → C-04 still FAIL.

**Essential:** 4/5 → 48  
**Recommended:** 2.5/3 → 25  
**Aspirational:** 11/12 → `(11/12)×10 = 9.17`  
**Composite: 82.17 — Bronze**

---

### V-05 — Table Format + NORM Inventory + CHAIN CHECK + Full Criterion Annotation

Delta from V-01: Structural table grammar mandates per-criterion columns throughout. C-16 requires an action items table with Owner column ("missing owner is a missing cell") — directly satisfying C-04. Dissent table with visible rows keeps C-05. Formal section structure enforced by table headers → C-06 PASS. CHAIN CHECK gate → C-19 PASS, C-09 PASS. C-14 already PASS in V-01.

Note: V-05's axis does not include pre-Phase-0 Challenger block; C-20 remains PARTIAL.

| Changed | ID | Verdict | Evidence |
|---------|----|---------|---------|
| ↑ | C-04 | **PASS** | Action items table with Owner column structurally required to satisfy C-16; missing owner = missing cell, not prose gap |
| ↑ | C-06 | PASS | Table headers mandate header / agenda / discussion / decisions / action items / next steps structure |
| ↑ | C-16 | PASS | Per-criterion columns; C-02 detectable per row without reading prose; C-04 visible as missing cell; C-05 visible as missing row |
| ↑ | C-19 | PASS | CHAIN CHECK gate |
| ↑ | C-09 | PASS | CHAIN-2 outside-in precondition |
| — | C-20 | PARTIAL | Challenger in Phase 0 roster only; pre-Phase-0 named block not in V-05 axis |

Full V-05 criterion table:

| ID | Verdict |
|----|---------|
| C-01 | PASS |
| C-02 | PASS |
| C-03 | PASS |
| C-04 | PASS |
| C-05 | PASS |
| C-06 | PASS |
| C-07 | PASS |
| C-08 | PASS (vacuous) |
| C-09 | PASS |
| C-10 | PASS |
| C-11 | PARTIAL |
| C-12 | PASS |
| C-13 | PASS |
| C-14 | PASS |
| C-15 | PASS |
| C-16 | PASS |
| C-17 | PASS |
| C-18 | PASS |
| C-19 | PASS |
| C-20 | PARTIAL |

**Essential:** 5/5 → `(5/5)×60 = 60`  
**Recommended:** 3/3 → `(3/3)×30 = 30`  
**Aspirational:** 11/12 (C-11 PARTIAL, C-20 PARTIAL) → `(11/12)×10 = 9.17`  
**Composite: 99.17 — Gold** (all essential, ≥80)

---

## Summary Scorecard

| Variation | Essential | Recommended | Aspirational | Composite | Tier |
|-----------|-----------|-------------|--------------|-----------|------|
| V-05 | 5/5 (60) | 3/3 (30) | 11/12 (9.2) | **99.2** | Gold |
| V-04 | 4/5 (48) | 2.5/3 (25) | 11/12 (9.2) | 82.2 | Bronze |
| V-03 | 4/5 (48) | 2.5/3 (25) | 10.5/12 (8.8) | 81.8 | Bronze |
| V-02 | 4/5 (48) | 2.5/3 (25) | 9.5/12 (7.9) | 80.9 | Bronze |
| V-01 | 4/5 (48) | 2.5/3 (25) | 9/12 (7.5) | 80.5 | Bronze |

---

## Key Observation: Why V-05 Breaks Away

V-04 closes the full inertia traceability loop (C-18/19/20) — the best structural closure of the three new R6 criteria. But it cannot escape Bronze because C-04 still fails: no action items table means no owners, and prose-level action capture is unreliable.

V-05 solves C-04 as a side effect of C-16. The moment structural table grammar mandates "missing owner is a missing cell," an action items table with an Owner column becomes a structural requirement — not a prose reminder. This is the force multiplier: one investment in output format compliance simultaneously satisfies three essential criteria (C-04 via table mandate, C-02 via per-row role column, C-05 via per-row dissent table). The jump from Bronze to Gold is entirely attributable to this coupling.

---

## Excellence Signals from V-05

**E-01 — Structural table format as essential-criteria force multiplier.** Mandating output tables with per-criterion columns converts C-04 (action items/owners), C-02 (role drift), and C-05 (dissent) from prose-quality checks to structural-gap checks. A single C-16 investment closes three essential criteria simultaneously. Any variation that targets only aspirational inertia criteria while leaving C-04 as a prose check cannot reach Gold.

**E-02 — CHAIN CHECK + criterion-annotated FAILS creates layered self-auditing.** The CHAIN-1/2/3 gate (C-19) blocks Phase 2 until outside-in basis is non-circular. Criterion-ID annotations on FAILS entries (C-14) map each structural gap to the rubric criterion it violates. Combined, these create two independent audit mechanisms — one architectural (gate blocks bad paths), one forensic (FAILS entries identify criterion impact). A skill with both mechanisms is auditable without running the simulation.

**E-03 — Table column presence as rubric proxy.** When output tables include columns for evidence, owner, NORM label, and dissent, a reviewer scanning column headers alone — without reading prose content — can confirm whether C-02, C-04, C-05, C-07, C-17, and C-18 compliance is plausible. This is a structural proxy for rubric compliance: the output format makes violations visible before the prose is read.

---

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["Structural table format as essential-criteria force multiplier: C-16 investment simultaneously closes C-04, C-02, and C-05 by mandating per-criterion table columns where violations appear as missing cells rather than prose gaps", "CHAIN CHECK gate plus criterion-annotated FAILS creates layered self-audit: gate blocks bad paths architecturally, FAILS annotations identify criterion impact forensically — two independent audit mechanisms that do not require running the simulation to validate compliance", "Table column presence as rubric proxy: when output tables include evidence, owner, NORM-label, and dissent columns, a reviewer scanning column headers alone can confirm C-02/C-04/C-05/C-07/C-17/C-18 plausibility without reading prose content"]}
```
