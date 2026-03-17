# trace-migration — Round 11 Scoring (v10 rubric, 220 max)

---

## Shared Baseline

All five variations share the same structural backbone: STEP REGISTRY + CONSTRAINT TYPE REGISTRY (BINDING MANIFEST) + PARITY ENFORCEMENT BLOCK + PARSE PHASE with encapsulated exit gate + Phase A three-section structure + Phase B (B1 EXECUTION SEQUENCE with MANIFEST COLUMN AUDIT + B2 DOMAIN SYNTHESIS + B3 VERIFY CHECKS + B4 RECOMMENDATIONS + VERDICT) + pre-seeded inertia examples (Commerce: order_status ENUM; Finance: decimal precision) + Phase B pre-seeded inertia example (reserved_qty DEFAULT).

---

## V-01 — Named BOUNDARY CHECKPOINT Sections

| ID | PASS/PARTIAL/FAIL | Evidence | Points |
|----|-------------------|----------|--------|
| C-01 | PASS | STEP REGISTRY carries Before/After columns; B1 repeats them | 12 |
| C-02 | PASS | DATA LOSS PATH (BINARY FIELD): YES / NO in CONSTRAINT TRACE + B2 | 12 |
| C-03 | PASS | Four constraint-type manifest rows, all with binary fields in CONSTRAINT TRACE | 12 |
| C-04 | PASS | PARITY ENFORCEMENT BLOCK item 2: DEFAULT check for ALL new NOT NULL columns | 12 |
| C-05 | PASS | Explicit "C-05 is satisfied here, not by any Phase A section" in Phase B header | 12 |
| C-06 | PASS | Operations Lens: performance cliff detection (full-table rewrite, index rebuild, row-scan) | 10 |
| C-07 | PASS | Fixed rollback taxonomy FULL DOWN MIGRATION / BACKUP ONLY / IRREVERSIBLE in PARITY BLOCK + B1 | 10 |
| C-08 | PASS | Commerce: 50,000 orders/day; Finance: $9,999,999.99 cap — numeric domain framing | 10 |
| C-09 | PASS | PARITY ENFORCEMENT BLOCK item 1: zero-downtime viability in ALL roles | 5 |
| C-10 | PASS | IDEMPOTENCY (BINARY FIELD): SAFE / UNSAFE in CONSTRAINT TRACE + B1 | 5 |
| C-11 | PASS | STEP REGISTRY named; CONSTRAINT TRACE cites "Step N from STEP REGISTRY"; B-sections cite "Step N from B1" | 5 |
| C-12 | PASS | DOMAIN IMPACT carries "(POSITIONED BEFORE B2 DOMAIN SYNTHESIS — complete before writing B2)" | 5 |
| C-13 | PASS | Binary fields throughout: YES/NO/PARTIAL for all critical items; free-form omission structurally visible | 5 |
| C-14 | PASS | "(BINARY FIELD)" annotation on all critical field labels | 5 |
| C-15 | PASS | PARSE GATE (BINARY FIELD): OPEN / BLOCKED gates CONSTRAINT TRACE entry | 5 |
| C-16 | PASS | Phase A — INTERROGATIVE / Phase B — CANONICAL MIGRATION TRACE explicit separation | 5 |
| C-17 | PASS | "PARSE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)" — compound annotation at gate definition | 5 |
| C-18 | PASS | "Step N from STEP REGISTRY" and "Step N from B1" named artifact citations | 5 |
| C-19 | **PARTIAL** | PARSE PHASE carries global "All downstream sections cite as…"; CONSTRAINT TRACE and DOMAIN IMPACT repeat per-section, but Phase B relies on B1-header global "All step references in Phase B cite as…" — B4 carries no citation instruction; unlabeled inline style (not named "CITATION ANCHOR") | **2.5** |
| C-20 | PASS | "(POSITIONED BEFORE B2 DOMAIN SYNTHESIS — complete before writing B2)" names the forward-completion target | 5 |
| C-21 | PASS | PARSE→CONSTRAINT, CONSTRAINT→DOMAIN, DOMAIN→PHASE B, B2→B3, B3→B4, B4→VERDICT all gated | 5 |
| C-22 | PASS | Pre-seeded Commerce and Finance worked examples with step, type change, and numeric threshold | 5 |
| C-23 | PASS | STEP REGISTRY within PARSE PHASE section; PARSE PHASE EXIT BLOCK; CONSTRAINT TRACE ENTRY REFERENCE names PARSE GATE | 5 |
| C-24 | PASS | B2→B3 gate (DOMAIN SYNTHESIS GATE) + B3→B4 gate (VERIFY COMPLETION GATE); each succeeding section names prerequisite | 5 |
| C-25 | PASS | Phase B header: "C-05 is satisfied here, not by any Phase A section" | 5 |
| C-26 | PASS | B4→VERDICT gate; VERDICT header names RECOMMENDATIONS GATE as entry prerequisite | 5 |
| C-27 | PASS | Pre-seeded inertia examples carry all three parts: before-state condition, migration breaks it, numeric consequence | 5 |
| C-28 | PASS | Four dedicated binary slots per constraint type in CONSTRAINT TRACE (not merged into free-form) | 5 |
| C-29 | PASS | PARITY ENFORCEMENT BLOCK applied to ALL THREE lenses; scoping prohibitions enforce checklist parity | 5 |
| C-30 | **PARTIAL** | B2 instructs "Seed a NEW inertia-contrast example — different step, table, consequence" with pre-seeded model example; but no structural INERTIA-SEED-B artifact or distinctness checklist — behavioral instruction only; model output could re-use Phase A example without triggering a mechanical failure | **2.5** |
| C-31 | PASS | CONSTRAINT TYPE REGISTRY (BINDING MANIFEST) in PARSE PHASE; fills all four rows before analysis | 5 |
| C-32 | PASS | MANIFEST COLUMN AUDIT in B1 pre-populates all four column names in manifest row order | 5 |
| C-33 | PASS | PARITY ENFORCEMENT BLOCK positioned before first domain-role section; all six items with scoping prohibitions ("DO NOT SCOPE OR SHORTEN," "apply to ALL roles," "not only financial columns") | 5 |
| C-34 | PASS | Named BOUNDARY CHECKPOINT sections at both positions — EXIT BLOCK at preceding phase bottom + ENTRY REFERENCE at succeeding phase top, both "(BINARY FIELD)" — absence detectable as missing named section | 5 |

**V-01 Total: 60 + 30 + 125 = 215 / 220** (C-19: −2.5, C-30: −2.5)

---

## V-02 — 2-Row Boundary Gate Table

All criteria identical to V-01 except:

| ID | PASS/PARTIAL/FAIL | Evidence vs V-01 | Points |
|----|-------------------|-----------------|--------|
| C-19 | **PASS** | CONSTRAINT TRACE, DOMAIN IMPACT, B1, B2, B3 each carry explicit "CITATION ANCHOR: All step references in this section cite as…" — labeled structural marker, not inline instruction | 5 |
| C-30 | **PASS** | B2 contains named **INERTIA-SEED-B** artifact (3-column distinctness checklist: Step ≠, Table ≠, Consequence ≠) that must be filled before synthesis prose; mechanical gate, not behavioral instruction | 5 |
| C-34 | PASS | 2-row boundary gate table at every boundary — Row 1 EXIT (preceding phase bottom) + Row 2 ENTRY (succeeding phase top), both carrying "(BINARY FIELD)" in the Type column; incomplete boundary = single-row table, detectable by row count without annotation inspection | 5 |

**V-02 Total: 60 + 30 + 130 = 220 / 220**

---

## V-03 — Imperative → PROPAGATE / ← RECEIVED FROM Directives

All criteria identical to V-01:

| ID | PASS/PARTIAL/FAIL | Evidence | Points |
|----|-------------------|----------|--------|
| C-19 | **PARTIAL** | PARSE PHASE global "All downstream sections cite as…"; CONSTRAINT TRACE and DOMAIN IMPACT have per-section repetition; Phase B B1 uses "All step references in Phase B cite as…" (Phase B global, not per sub-section); B4 carries no per-section instruction | **2.5** |
| C-30 | **PARTIAL** | B2 behavioral "Seed a NEW inertia-contrast example" with pre-seeded example — no structural INERTIA-SEED-B checklist artifact; same gap as V-01 | **2.5** |
| C-34 | PASS | EXIT BLOCK carries "→ PROPAGATE: write ENTRY REFERENCE at top of [successor] with (BINARY FIELD)…"; ENTRY REFERENCE carries "← RECEIVED FROM: [predecessor] EXIT BLOCK (BINARY FIELD)" — broken reference chain detectable as unexecuted PROPAGATE or missing source declaration | 5 |

**V-03 Total: 60 + 30 + 125 = 215 / 220** (C-19: −2.5, C-30: −2.5)

---

## V-04 — Combined V-01 + V-03 + INERTIA-SEED-B + Per-Section CITATION ANCHORs

All criteria identical to V-02:

| ID | PASS/PARTIAL/FAIL | Evidence | Points |
|----|-------------------|----------|--------|
| C-19 | **PASS** | Explicit "CITATION ANCHOR:" labeled markers in CONSTRAINT TRACE, DOMAIN IMPACT, B1, B2, B3, B4 — every step-referencing section carries the anchor | 5 |
| C-30 | **PASS** | Named INERTIA-SEED-B artifact (3-column checklist) in B2; same structural gate as V-02 | 5 |
| C-34 | PASS | Named BOUNDARY CHECKPOINT sections (V-01 axis) AND imperative cross-reference directives (V-03 axis) at every boundary — dual-detection surface: missing section is structural gap; unexecuted PROPAGATE is instruction non-compliance | 5 |

**V-04 Total: 60 + 30 + 130 = 220 / 220**

---

## V-05 — All Three C-34 Axes on Full R10 Backbone

All criteria identical to V-04:

| ID | PASS/PARTIAL/FAIL | Evidence | Points |
|----|-------------------|----------|--------|
| C-19 | **PASS** | CITATION ANCHOR labeled markers in every step-referencing section (CONSTRAINT TRACE, DOMAIN IMPACT, B1, B2, B3, B4) | 5 |
| C-30 | **PASS** | Named INERTIA-SEED-B artifact with 3-column distinctness checklist | 5 |
| C-34 | PASS | Three simultaneous enforcement surfaces: named BOUNDARY CHECKPOINT sections (structural presence) + 2-row table (row-count) + → PROPAGATE / ← RECEIVED FROM directives (reference chain) — a C-34 violation must evade all three surfaces | 5 |

**V-05 Total: 60 + 30 + 130 = 220 / 220**

---

## Composite Score Table

| V | Essential (60) | Recommended (30) | Aspirational (130) | Total (220) | Golden? | C-19 | C-30 | C-34 |
|---|----------------|------------------|--------------------|-------------|---------|------|------|------|
| V-01 | 60 | 30 | 125 | **215** | YES | PARTIAL | PARTIAL | PASS |
| V-02 | 60 | 30 | 130 | **220** | YES | PASS | PASS | PASS |
| V-03 | 60 | 30 | 125 | **215** | YES | PARTIAL | PARTIAL | PASS |
| V-04 | 60 | 30 | 130 | **220** | YES | PASS | PASS | PASS |
| V-05 | 60 | 30 | 130 | **220** | YES | PASS | PASS | PASS |

**All essential criteria (C-01–C-05): PASS in all five variations.**
**Golden threshold (176 pts, 80%): All five exceed. All GOLDEN.**

---

## Ranking

1. **V-02, V-04, V-05 — 220/220 (tied at max)**
   - V-02 achieves 220 with the simplest C-34 mechanism (2-row table, single axis) plus per-section CITATION ANCHORs and INERTIA-SEED-B
   - V-04 achieves 220 with dual-axis C-34 (named sections + cross-references) plus full C-19/C-30 backbone
   - V-05 achieves 220 with triple-axis C-34 plus full C-19/C-30 backbone — maximum detection redundancy at maximum structural cost
2. **V-01, V-03 — 215/220 (tied)** — both lose 2.5 pts each on C-19 and C-30 from using global citation instruction and behavioral B2 seeding without structural artifacts

**Design observation:** V-02 achieves the same max score as V-04 and V-05 with minimal overhead. Additional C-34 axes beyond the first add robustness (fault surfaces), not score. Score ceiling is determined by C-19 and C-30 enforcement quality, not C-34 complexity.

---

## Excellence Signals from Top-Scoring Variations

### Signal 1 — Row-count verification as parse-mechanical C-34 compliance check (V-02)

The 2-row boundary gate table converts C-34 compliance from annotation-position inspection ("find the compound annotation at both structural positions") into a mechanical row-count check ("count rows; two required; type column must carry '(BINARY FIELD)' in both"). This is qualitatively different from the V-01 mechanism (named section presence) and V-03 mechanism (reference chain). A row count is computable without semantic understanding of the boundary context.

**Structural detail:** The Row 2 ENTRY cell carries "*(propagate from Row 1)*" as its State placeholder — propagation direction is recorded in-cell rather than in surrounding prose. A boundary table where Row 2 State is unfilled is detectable at cell level without prose inspection.

### Signal 2 — CITATION ANCHOR as labeled section-entry marker (V-02, V-04, V-05)

Naming the per-section citation instruction "CITATION ANCHOR:" creates a scannable structural label at section entry rather than an inline sentence. This distinguishes a structural compliance element from prose instruction. Consequence: C-19 compliance is verifiable by searching for "CITATION ANCHOR" in each section header zone rather than scanning all section prose for citation mentions.

V-01/V-03 have the same citation information embedded in section-opening sentences but without the labeled marker — scannable only by prose reading, not structural token matching.

### Signal 3 — INERTIA-SEED-B as pre-execution distinctness gate (V-02, V-04, V-05)

The INERTIA-SEED-B artifact forces distinctness verification before synthesis prose is permitted: three checklist rows (Step ≠, Table ≠, Consequence ≠) must be filled before writing B2 synthesis content. This converts C-30 from a post-hoc check ("did the final output contain a distinct Phase B example?") to a pre-execution gate ("is the planned B2 example provably distinct before it is written?"). The artifact fails explicitly (unfilled checklist cell) rather than silently (prose that superficially satisfies the instruction but re-uses Phase A content).

V-01/V-03 pre-seed a B2 example that IS distinct (reserved_qty DEFAULT ≠ order_status/payment_amount), but the instruction is behavioral — a model output that narrows to a prior example violates spirit without triggering a structural failure surface.

### Signal 4 — Efficiency of single-axis C-34 enforcement (V-02)

V-02 achieves 220 with one C-34 mechanism (row-count table). V-04 uses two, V-05 uses three — same score. This establishes that any single structurally complete C-34 mechanism is sufficient for max score. Multiple axes add fault-surface redundancy (a violation must evade more checks), not additional score. Future variation design should prefer structural simplicity unless robustness against model error is the explicit goal.

---

```json
{"top_score": 220, "all_essential_pass": true, "new_patterns": ["2-row boundary gate table converts C-34 gate compliance to row-count verification — Row 2 ENTRY state propagated in-cell, detectable without annotation inspection", "INERTIA-SEED-B pre-execution checklist converts C-30 from behavioral instruction to structural pre-flight gate — distinctness verified before synthesis prose is permitted"]}
```
