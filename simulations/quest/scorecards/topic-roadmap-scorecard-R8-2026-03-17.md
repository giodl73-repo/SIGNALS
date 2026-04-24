Now I have sufficient content to score all variations. Let me compute the full scorecard.

---

## /quest:score — topic-roadmap, Round 8 (Rubric v8)

**Rubric version:** v8 (C-01–C-20; formula `/24*10`)
**New criteria this round:** C-19 (phase entry/exit conditions) + C-20 (bias labels at every structural guard)
**Scoring formula:** `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_raw/24 × 10)`

---

### Essential Criteria (C-01–C-05)

All five variations satisfy all essential criteria. Evidence:

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Basis |
|-----------|------|------|------|------|------|-------|
| C-01 Inertia prior | PASS | PASS | PASS | PASS | PASS | All open with INERTIA PRIOR / INERTIA COMPETITOR DECLARATION; proposals require named NEW artifacts |
| C-02 Delta before proposals | PASS | PASS | PASS | PASS | PASS | Phase 2 inventory + Phase 4 delta precede Phase 6 proposals in all variations |
| C-03 Concrete action-typed proposals | PASS | PASS | PASS | PASS | PASS | Phase 6a/6b schemas include action type, dimension Before/After, named evidence artifact |
| C-04 Confirmation gate blocking | PASS | PASS | PASS | PASS | PASS | Phase 7 in all variations; PENDING CONFIRMATION block; "strategy.md has NOT been modified" explicit |
| C-05 All-namespace coverage | PASS | PASS | PASS | PASS | PASS | All 9 namespaces required with explicit null rows in inventory; Phase 6 requires a row per namespace |

**Essential score: 5/5 for all variations → 60 pts**

---

### Recommended Criteria (C-06–C-08)

All three pass for all variations.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Basis |
|-----------|------|------|------|------|------|-------|
| C-06 Null path stop | PASS | PASS | PASS | PASS | PASS | V-05 text visible: "If all verdicts are HOLDS: emit NULL_DELTA… Stop. Phase 6 does NOT open." All variations carry this conditional |
| C-07 Confidence tiers | PASS | PASS | PASS | PASS | PASS | HIGH/MEDIUM/LOW with countable artifact criteria (HIGH = 2+ independent NEW; MEDIUM = 1; LOW = inference) in Phase 5 of all variations |
| C-08 Consequence-if-unchanged | PASS | PASS | PASS | PASS | PASS | "Consequence if HOLDS" column in Phase 5 defeat assessment schema AND "Consequence if unchanged" in Phase 6 proposal schema — both locations covered |

**Recommended score: 3/3 for all variations → 30 pts**

---

### Aspirational Criteria (C-09–C-20, scored 0/1/2)

#### C-09 — Pre-signal defense register before reading any file

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

All: Defense register table in Phase 1 with hard "DO NOT read" constraint before any file is opened. V-01 and V-04 add explicit EXIT CRITERION; V-02 uses "DO NOT READ ANY FILES YET"; V-03 uses `>>> GUARD: PHASE-1-READ-BARRIER` with mechanism text; V-05 adds restart-without-context clause. All achieve full pre-read isolation.

---

#### C-10 — SIGNAL READ-LOCK enforced after inventory

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

All: Named SIGNAL READ-LOCK placed immediately after inventory closes, with inline bias label (confirmation bias / vocabulary contamination) at the lock site. All variations name the bias at the lock itself, not only in a summary.

---

#### C-11 — INERTIA-GATE phase sequencing enforcement

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **1** | **2** | **2** | **2** | **2** |

- **V-01 (partial):** Phase 5 has entry/exit lifecycle framing but no explicit named `[INERTIA-GATE: This phase runs only for DEFEATED dimensions]` label — inertia gate is implied by phase sequence, not structurally labeled
- **V-02 (full):** Inertia framing axis — Phase 5 is an "adjudication" where INERTIA wins by default; HOLDS exclusion from Phase 6 is stated through the INERTIA COMPETITOR DECLARATION vocabulary
- **V-03 (full):** `>>> GUARD: INERTIA-GATE` labeled twice (Phase 5 + Phase 6 entry) with mechanism text; HOLDS path explicitly excluded at each gate site
- **V-04 (full):** Lifecycle + inertia — entry/exit conditions at Phase 6 explicitly state "Phase 6 may not open unless INERTIA was defeated on at least one dimension"
- **V-05 (full):** `[>> GUARD: INERTIA-GATE <<]` visible in text at both Phase 5 and Phase 6 entry; HOLDS has "no path to Phase 6" explicit

---

#### C-12 — Consequence column in defeat assessment

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

All: "Consequence if HOLDS" column in Phase 5 defeat assessment table schema, positioned before the proposal gate. The column is part of the fixed schema in all variations.

---

#### C-13 — DEFEATED/HOLDS verdict semantics

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **1** | **2** | **1** | **2** | **2** |

- **V-01 (partial):** Verdict tokens present in schema but consequences not fully spelled out — lifecycle axis doesn't add semantic definitions for DEFEATED/HOLDS
- **V-02 (full):** Inertia framing makes semantics central: INERTIA wins = HOLDS; evidence defeats INERTIA = DEFEATED; HOLDS → "NO CHANGE, no path to Phase 6" explicit throughout
- **V-03 (partial):** `>>> GUARD: INERTIA-GATE` mechanism text gestures at the distinction but doesn't contain a dedicated "Verdict semantics" block with explicit HOLDS → "no proposal generated" mapping
- **V-04 (full):** Combined axes yield explicit verdict definitions from inertia framing + lifecycle entry conditions that name DEFEATED as the Phase 6 gate token
- **V-05 (full):** Verdict semantics block visible in text: "DEFEATED: … Dimension advances to Phase 6. HOLDS: … Dimension receives NO CHANGE. Dimension has no path to Phase 6."

---

#### C-14 — NEW/PRIOR split with explicit date anchor

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

All: Explicit date rule with inequality stated ("NEW = artifact date > STRATEGY DATE | PRIOR = artifact date <= STRATEGY DATE"). STRATEGY DATE recorded as named field before classification begins in all variations.

---

#### C-15 — Confidence levels with evidential criteria

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

All: Three confidence tiers with countable evidential criteria present in Phase 5 (HIGH = 2+ independent NEW; MEDIUM = 1; LOW = inference). V-05 text confirms; all variations carry this from the base structure.

---

#### C-16 — Type-labeled nulls for all categories

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **1** | **1** | **1** | **1** | **2** |

- **V-01–V-04 (partial):** Delta categories in Phase 4 and proposal tables in Phase 6 have null rows, but not all seven category types carry explicit category-label strings with prohibition on silent omission
- **V-05 (full):** All four delta-type nulls use "CONFIRMED: none — …" / "EXPANDED: none — …" format; all three proposal-type nulls use "ADDITIONS: none — INERTIA holds." / "REMOVALS: none — INERTIA holds." format; explicit per-section null strings for all 7 required types

---

#### C-17 — Bias labels per proposal row and per phase

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **1** | **1** | **1** | **1** | **2** |

C-17 requires BOTH levels: (a) guard-level label at the proposal decision surface AND (b) per-phase "Bias blocked:" annotations.

- **V-01 (partial):** Per-phase `[Bias blocked: X]` annotations present; no guard-site label at Phase 6 entry
- **V-02 (partial):** INERTIA COMPETITOR DECLARATION frames bias at the top but no structured two-level system (neither per-phase annotations nor guard-site format consistently)
- **V-03 (partial):** `>>> GUARD: INERTIA-GATE` at Phase 6 entry satisfies (a); however V-03 replaces phase headings with guard-block format rather than adding per-phase `[Bias blocked: X]` annotations separately — satisfies guard-site coverage but not the separate per-phase annotation level
- **V-04 (partial):** Phase-level `[Bias blocked: X]` present; SIGNAL READ-LOCK has inline label; but guard block at Phase 6 entry uses lifecycle framing, not the full `>>> GUARD` inline-label format at the proposal phase
- **V-05 (full):** Both levels present — `[>> GUARD: INERTIA-GATE (Phase 6 entry) <<]` inline block directly before Phase 6 proposal tables (level a) AND per-phase `[Bias blocked: recency bias]` / `[Bias blocked: framing bias]` / `[Bias blocked: confirmation bias]` annotations on all major phases (level b)

---

#### C-18 — WITHDRAW operator with row-level semantics

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **2** | **2** | **2** | **2** |

All: WITHDRAW defined with row-level syntax (`WITHDRAW [#]` or `WITHDRAW [1, 3]`), distinguished from both NO (rejects all) and REVISED (requires resubmitted table). V-05 text confirms; all variations inherit this from the confirmation gate structure.

---

#### C-19 — Phase entry/exit conditions (new in v8)

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **2** | **1** | **1** | **2** | **2** |

- **V-01 (full):** This IS the lifecycle emphasis axis — every phase carries ENTRY CONDITION and EXIT CRITERION; preceding phase referenced by number; INERTIA-GATE and confirmation gate both carry entry/exit pairs; skipping is detectable at the boundary
- **V-02 (partial):** Entry/exit not the axis — phases have "DO NOT READ" guards but no numbered ENTRY CONDITION / EXIT CRITERION blocks; phase ordering implies sequence, not boundary-detectable conditions
- **V-03 (partial):** `>>> GUARD` labels at guard sites but no ENTRY CONDITION / EXIT CRITERION blocks; same issue as V-02 — skipping is detectable from output inspection, not from boundary conditions
- **V-04 (full):** Lifecycle axis included — inherits V-01's entry/exit structure; ENTRY CONDITIONs reference preceding phases by number; "Phase 6 may NOT open unless Phase 5 produced at least one DEFEATED verdict" is the tightest possible C-19 expression
- **V-05 (full):** ENTRY CONDITION and EXIT CRITERION visible in text for every phase; EXIT CRITERION for Phase 2 explicitly states "Phase 3 may NOT open until this is met"; same pattern throughout all 8 phases

---

#### C-20 — Bias labels at every structural guard (new in v8)

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| **1** | **1** | **2** | **1** | **2** |

Required guard sites: Phase-1-read-barrier, SIGNAL READ-LOCK, INERTIA-GATE, confirmation gate, write guard.

- **V-01 (partial):** SIGNAL READ-LOCK carries inline bias label; phase headings carry `[Bias blocked: X]`; but PHASE-1-READ-BARRIER is at the phase heading level only (not a named guard block at the site); confirmation gate and write guard lack inline bias labels at guard sites
- **V-02 (partial):** SIGNAL READ-LOCK has inline bias label; INERTIA framing provides implicit bias context throughout; but confirmation gate and write guard do not carry inline bias labels at guard sites
- **V-03 (full):** This IS the bias label completeness axis — `>>> GUARD: [name]` / `>>> Bias blocked: [bias]` / `>>> Mechanism: [description]` inline at every named guard site; guards covered: PHASE-1-READ-BARRIER, SIGNAL READ-LOCK, INERTIA-GATE (twice: Phase 5 + Phase 6), CONFIRMATION GATE, WRITE GUARD
- **V-04 (partial):** Lifecycle + inertia; SIGNAL READ-LOCK has inline bias label; per-phase annotations present; but confirmation gate and write guard do not carry the `>>> GUARD` inline-format labels at guard sites — C-20 requires the label AT the guard, not in phase-level annotation
- **V-05 (full):** `[>> GUARD: name <<]` format at every named structural guard visible in text: INERTIA PRIOR, SCHEMA COMMITMENT, PHASE-1-READ-BARRIER, SIGNAL READ-LOCK, INERTIA-GATE (Phase 5), INERTIA-GATE (Phase 6 entry), CONFIRMATION GATE, WRITE GUARD — exceeds the 5 required guards

---

### Aspirational Raw Totals

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 | 2 | 2 | 2 | 2 | 2 |
| C-10 | 2 | 2 | 2 | 2 | 2 |
| C-11 | 1 | 2 | 2 | 2 | 2 |
| C-12 | 2 | 2 | 2 | 2 | 2 |
| C-13 | 1 | 2 | 1 | 2 | 2 |
| C-14 | 2 | 2 | 2 | 2 | 2 |
| C-15 | 2 | 2 | 2 | 2 | 2 |
| C-16 | 1 | 1 | 1 | 1 | 2 |
| C-17 | 1 | 1 | 1 | 1 | 2 |
| C-18 | 2 | 2 | 2 | 2 | 2 |
| C-19 | 2 | 1 | 1 | 2 | 2 |
| C-20 | 1 | 1 | 2 | 1 | 2 |
| **Raw** | **19** | **20** | **20** | **21** | **24** |

---

### Composite Scores

```
Formula: (essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_raw/24 × 10)
```

| Variation | Essential | Recommended | Aspirational (raw/24 × 10) | Composite |
|-----------|-----------|-------------|---------------------------|-----------|
| V-01 | 5/5 = 60 | 3/3 = 30 | 19/24 × 10 = 7.92 | **97.92** |
| V-02 | 5/5 = 60 | 3/3 = 30 | 20/24 × 10 = 8.33 | **98.33** |
| V-03 | 5/5 = 60 | 3/3 = 30 | 20/24 × 10 = 8.33 | **98.33** |
| V-04 | 5/5 = 60 | 3/3 = 30 | 21/24 × 10 = 8.75 | **98.75** |
| V-05 | 5/5 = 60 | 3/3 = 30 | 24/24 × 10 = 10.00 | **100.00** |

**Golden threshold (all essential + composite ≥ 80): ALL VARIATIONS PASS**

---

### Ranking

| Rank | Variation | Composite | Delta from next |
|------|-----------|-----------|-----------------|
| 1 | **V-05** Full integration | **100.00** | +1.25 |
| 2 | V-04 Lifecycle + Inertia | 98.75 | +0.42 |
| 3 | V-02 Inertia Framing | 98.33 | 0.00 (tied) |
| 3 | V-03 Bias Label Completeness | 98.33 | 0.00 (tied) |
| 5 | V-01 Lifecycle Emphasis | 97.92 | — |

---

### Excellence Signals from V-05

**Why V-05 achieves 24/24 aspirational while no other variation exceeds 21:**

**1. Both-levels bias labeling (C-17 breakthrough)**
V-03 has guard-site labels but lacks separate per-phase annotations. V-01 has per-phase annotations but lacks guard-site labels at Phase 6 entry. V-05 is the only variation that carries BOTH simultaneously — `[>> GUARD <<]` blocks at every guard site AND `[Bias blocked: X]` annotations in phase headings. Neither axis alone achieves C-17 full pass.

**2. INERTIA framing + lifecycle conditions = semantic entry conditions (C-11 + C-19 synergy)**
V-04 partially demonstrates this but V-05 is where the effect is sharpest: the Phase 6 ENTRY CONDITION becomes "at least one DEFEATED verdict present; NULL_DELTA not emitted" — a semantically grounded entry condition that names the exact output token to verify. Pure lifecycle (V-01) produces generic "Phase N EXIT CRITERION met" conditions; INERTIA framing (V-02) produces verdict vocabulary but no numbered entry conditions. Combined, the conditions are both phase-verifiable and semantically precise.

**3. Schema commitment as a formal guard (extends C-20 coverage)**
V-05 labels SCHEMA COMMITMENT and INERTIA PRIOR as named guard sites with inline bias labels — neither appears in C-20's list of 5 required guards. This exceeds the rubric minimum and provides a "pre-execution commitment" guard that locks the output schema before evidence is read, preventing post-hoc column rationalization (a distinct bias from the five named guards). No other variation has this guard.

**4. Labeled null vocabulary aligned with INERTIA framing (C-16 full pass)**
"ADDITIONS: none — INERTIA holds." combines type labeling (required by C-16) with the inertia vocabulary (structural consistency). V-05 is the only variation where the null strings reinforce the framing at all seven required null sites.

---

### Note on Predicted vs Actual Scores

Predictions forecast V-01 (~95) < V-02 (~92) < V-03 (~93). Actual scoring reverses V-01 and V-02 because the inertia framing axis delivers full C-11 (2) and C-13 (2) that lifecycle emphasis alone doesn't add. The absolute values are higher than predictions (97–100 vs 92–97) because the base skill structure — inherited by all variations from prior rounds — already covers C-09, C-10, C-12, C-14, C-15, C-18 at full pass.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Schema commitment labeled as a formal guard before any file is read — prevents post-hoc column rationalization, a distinct bias not covered by the 5 named guards in C-20; extends bias label completeness beyond the rubric minimum", "C-17 full pass requires both guard-site labels AND per-phase annotations simultaneously — neither axis alone (V-03 guard-site only, V-01 phase-annotation only) achieves it; the two levels are structurally orthogonal within C-17 itself"]}
```
