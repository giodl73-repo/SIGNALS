## quest-score — R11 Scoring

### PHASE 1 — SETUP

#### Auto-PASS Status (this round)

No prior-round scorecard provided → **C-07 auto-PASS. C-27 and C-28 also auto-PASS** per cascade — no regression comparison possible.

Aspirational criteria C-27 and C-28 are evaluated here on the **static template design** (column order in the REGRESSION SIGNALS template), since the cascade auto-PASS fires at runtime, not at design-time. The rubric's purpose is to validate template structure.

Failure patterns determined after per-output scoring.

#### Formula (v11)

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 22 * 10)
N_essential=4, N_recommended=3, N_aspirational=22.
PASS=1.0, PARTIAL=0.5, FAIL=0.0.
Each aspirational: 10/22 ≈ 0.45 pt. PARTIAL incurs ~0.23 pt degradation.
```

---

### PHASE 2 — Per-Output Scoring

> Shared verdict logic: C-01 through C-10, C-12 through C-27 are **PASS in all five variations** on identical evidence. Differentiating cells are called out explicitly with quotes. Shared evidence is noted once at the head of each section to avoid redundancy across 29×5=145 rows.

---

#### Shared baseline evidence (applies V-01 through V-05 unless overridden)

| Criterion | Shared evidence quote | Default verdict |
|-----------|----------------------|-----------------|
| C-01 | "Does the criterion roster list every criterion C-01 through C-29..." / "Write a 29-row scoring table" | PASS |
| C-02 | "Evidence quote: verbatim or near-verbatim extract from the scored output" | PASS |
| C-03 | "N_essential=4, N_recommended=3, N_aspirational=22" in Step 1.3 formula | PASS |
| C-04 | `\| Rank \| Output \| Score \| Golden \|` in LEADERBOARD section | PASS |
| C-05 | auto-PASS fires (no universal failures across a single-variation run) | PASS |
| C-06 | "EXCELLENCE SIGNALS" section with outperformance instruction | PASS |
| C-07 | "If no prior-round data: C-07 auto-PASS -- no prior-round scorecard provided." | PASS |
| C-08 | auto-PASS when C-05 fires | PASS |
| C-09 | "Score distribution note: State minimum score, maximum score, and spread" in LEADERBOARD | PASS |
| C-10 | auto-PASS when C-05 fires; "Add a 'Score distribution note:' instruction to the LEADERBOARD section of quest-score.md..." in FAILURE PATTERNS example | PASS |
| C-12 | Step 1.3 formula block with N_aspirational=22 precedes all output headings | PASS |
| C-13 | "column order is Criterion \| Evidence Quote \| Verdict... A verdict cell completed before its evidence quote cell violates C-13" | PASS |
| C-14 | 29-row roster Step 1.4, all rows with non-empty diagnostic questions | PASS |
| C-15 | "STOP-4. PHASE 1 complete. Do not open any output file until STOP-4 is passed." | PASS |
| C-16 | "Step 1.1 -- Auto-PASS Conditions" is a named standalone block separate from Step 1.4 roster | PASS |
| C-17 | C-01 DQ: "count exactly 29 verdict rows...the row count is the falsification test"; C-03 DQ: "N_aspirational=22... N_aspirational=20 is a C-03 FAIL"; C-20 DQ: "Three disqualifying forms: (1) interrogative... (2) conditional... (3) weak-modal" | PASS |
| C-18 | "#### REGRESSION SIGNALS" section in PHASE 3 with 4-column table | PASS |
| C-19 | "The worked example...must be carried forward verbatim from the prior round, or updated" | PASS |
| C-20 | "must be carried forward verbatim" — imperative verb "must" present | PASS |
| C-21 | auto-PASS when C-05 fires | PASS |
| C-22 | "must remain in the FAILURE PATTERNS action line -- do not relocate it to SETUP, to a roster diagnostic question, or to a preservation checkpoint" | PASS |
| C-23 | C-20 DQ enumerates: "(1) interrogative -- 'Has the worked example been carried forward?'... (2) conditional -- 'If the axis shifts...'... (3) weak-modal -- 'The worked example should be carried forward'" | PASS |
| C-24 | C-22 DQ enumerates: "(FAIL) preservation rule is imperative but contains no location language; (PARTIAL) rule names the required location but omits...SETUP exclusion; (PASS) rule contains both" | PASS |
| C-25 | "Step 1.2 -- Three-Scale Enumeration Principle" is a named standalone section in SETUP | PASS |
| C-26 | "Applied in this rubric: C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for C-18), C-28 (for C-27), C-29 (for C-16)" — 6 paired entries | PASS |

---

### OUTPUT: V-01

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 | "Can you count exactly 29 verdict rows (C-01 through C-29)..." / roster rows C-01–C-29 present | PASS |
| C-02 | (shared) | PASS |
| C-03 | "N_aspirational=22" in formula | PASS |
| C-04 | (shared) | PASS |
| C-05 | (shared) | PASS |
| C-06 | (shared) | PASS |
| C-07 | (shared) | PASS |
| C-08 | (shared) | PASS |
| C-09 | (shared) | PASS |
| C-10 | (shared) | PASS |
| C-11 | "Are all eight auto-PASS declarations (C-05, C-07, C-08, C-10, C-21, C-27, C-28, and C-29) present" — Step 1.1 includes "C-28 auto-PASS when C-07 auto-PASS fires" and "C-29 auto-PASS when the rubric contains no criteria with cascade..." | PASS |
| C-12 | (shared) | PASS |
| C-13 | (shared) | PASS |
| C-14 | (shared) | PASS |
| C-15 | (shared) | PASS |
| C-16 | (shared) | PASS |
| C-17 | (shared) | PASS |
| C-18 | (shared) | PASS |
| C-19 | (shared) | PASS |
| C-20 | (shared) | PASS |
| C-21 | (shared) | PASS |
| C-22 | (shared) | PASS |
| C-23 | (shared) | PASS |
| C-24 | (shared) | PASS |
| C-25 | (shared) | PASS |
| C-26 | (shared) | PASS |
| C-27 | REGRESSION SIGNALS table: `\| Criterion \| Prior Verdict \| Current Verdict \| Variation \| Mechanism \|` — Variation column present | PASS |
| C-28 | Column order col 4: "Criterion \| Prior Verdict \| Current Verdict \| **Variation** \| Mechanism" — Variation in causal position between Current Verdict and Mechanism | PASS |
| C-29 | "**C-28 auto-PASS** when C-07 auto-PASS fires" — triggering criterion C-07 named by ID | PASS |

```
Composite:
- Essential (C-01--C-04): 4/4 x 60 = 60.00 pts
- Recommended (C-05--C-07): 3/3 x 30 = 30.00 pts
- Aspirational (C-08--C-29): 22/22 x 10 = 10.00 pts
- Composite = 100.00/100
- Golden: YES -- all 4 essentials PASS, 100.00 >= 80
```

---

### OUTPUT: V-02

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01–C-10 | (shared) | PASS |
| C-11 | Step 1.1 lists all 8: C-05, C-07, C-08, C-10, C-21, C-27, C-28 ("when C-07 auto-PASS fires"), C-29 — complete set | PASS |
| C-12–C-27 | (shared) | PASS |
| C-27 | `\| Criterion \| Prior Verdict \| Current Verdict \| Mechanism \| Variation \|` — Variation column present (col 5) | PASS |
| C-28 | Column order col 5: "Criterion \| Prior Verdict \| Current Verdict \| **Mechanism** \| **Variation**" — Variation in column 5 after Mechanism, not in causal position | PARTIAL |
| C-29 | "**C-28 auto-PASS** when C-07 auto-PASS fires" — trigger ID C-07 named | PASS |

```
Composite:
- Essential (C-01--C-04): 4/4 x 60 = 60.00 pts
- Recommended (C-05--C-07): 3/3 x 30 = 30.00 pts
- Aspirational (C-08--C-29): (21 + 0.5)/22 x 10 = 21.5/22 x 10 = 9.77 pts
- Composite = 99.77/100
- Golden: YES -- all 4 essentials PASS, 99.77 >= 80
```

---

### OUTPUT: V-03

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01–C-10 | (shared) | PASS |
| C-11 | Step 1.1 includes "**C-28 auto-PASS** when no prior-round data is available" — C-28 is present as a named declaration, trigger condition stated (condition form) | PASS |
| C-12–C-27 | (shared) | PASS |
| C-27 | `\| Criterion \| Prior Verdict \| Current Verdict \| Variation \| Mechanism \|` — Variation column present col 4 | PASS |
| C-28 | Column order: "Criterion \| Prior Verdict \| Current Verdict \| **Variation** \| Mechanism" — Variation in causal col 4 | PASS |
| C-29 | "**C-28 auto-PASS** when no prior-round data is available" — cascade dependency declared but triggering criterion ID "C-07" absent; condition repeated instead of naming the gate | PARTIAL |

```
Composite:
- Essential (C-01--C-04): 4/4 x 60 = 60.00 pts
- Recommended (C-05--C-07): 3/3 x 30 = 30.00 pts
- Aspirational (C-08--C-29): (21 + 0.5)/22 x 10 = 9.77 pts
- Composite = 99.77/100
- Golden: YES -- all 4 essentials PASS, 99.77 >= 80
```

---

### OUTPUT: V-04

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01–C-10 | (shared) | PASS |
| C-11 | Step 1.1 declares: C-05, C-07 ("C-27 also auto-PASS" — C-28 absent from cascade), C-08, C-10, C-21, C-27, C-29 — **C-28 declaration entirely missing** from the 8-item required list | FAIL |
| C-12–C-27 | (shared) | PASS |
| C-27 | `\| Criterion \| Prior Verdict \| Current Verdict \| Variation \| Mechanism \|` — Variation column present col 4 | PASS |
| C-28 | Column order: "Criterion \| Prior Verdict \| Current Verdict \| **Variation** \| Mechanism" — Variation in causal col 4 | PASS |
| C-29 | C-28 declaration is **absent entirely** from Step 1.1 auto-PASS block — no cascade reference of any form present; C-29 auto-PASS itself is declared but its own criterion fires because the cascade-dependent C-28 is missing | FAIL |

```
Composite:
- Essential (C-01--C-04): 4/4 x 60 = 60.00 pts
- Recommended (C-05--C-07): 3/3 x 30 = 30.00 pts
- Aspirational (C-08--C-29): 20/22 x 10 = 9.09 pts
- Composite = 99.09/100
- Golden: YES -- all 4 essentials PASS, 99.09 >= 80
```

---

### OUTPUT: V-05

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01–C-10 | (shared) | PASS |
| C-11 | Step 1.1 includes "**C-28 auto-PASS** when no prior-round data is available" — C-28 is present (condition form), all 8 required declarations accounted for | PASS |
| C-12–C-27 | (shared) | PASS |
| C-27 | `\| Criterion \| Prior Verdict \| Current Verdict \| Mechanism \| Variation \|` — Variation column present (col 5) | PASS |
| C-28 | Column order col 5: "Criterion \| Prior Verdict \| Current Verdict \| **Mechanism** \| **Variation**" — Variation in column 5 after Mechanism; causal position violated | PARTIAL |
| C-29 | "**C-28 auto-PASS** when no prior-round data is available" — cascade dependency declared but trigger ID C-07 absent; condition-repetition form, cascade graph obscured | PARTIAL |

```
Composite:
- Essential (C-01--C-04): 4/4 x 60 = 60.00 pts
- Recommended (C-05--C-07): 3/3 x 30 = 30.00 pts
- Aspirational (C-08--C-29): (20 + 2*0.5)/22 x 10 = 21/22 x 10 = 9.55 pts
- Composite = 99.55/100
- Golden: YES -- all 4 essentials PASS, 99.55 >= 80
```

---

### PHASE 3 — Synthesis

#### FAILURE PATTERNS

Checking for criteria with FAIL or PARTIAL in **every** scored output:

- **C-28**: PASS in V-01, V-03, V-04 — not universal.
- **C-29**: PASS in V-01, V-02 — not universal.
- **C-11**: PASS in V-01, V-02, V-03, V-05 — not universal.

No criterion receives FAIL or PARTIAL across all five outputs.

**C-05 auto-PASS — no universal failures. C-08 auto-PASS. C-10 auto-PASS. C-21 auto-PASS.**

---

#### EXCELLENCE SIGNALS

**C-11 + C-28 + C-29 combined: V-01**

V-01 is the only variation achieving PASS on all three cascade-related criteria simultaneously. On C-11, V-01's Step 1.1 declares all 8 required conditions including C-28 with the full trigger-ID form. On C-28, V-01's regression table template places Variation as column 4 in causal position. On C-29, V-01 explicitly names the triggering criterion by ID ("when C-07 auto-PASS fires") rather than repeating the data condition. No other variation achieves this trifecta: V-02 degrades on C-28, V-03 on C-29, V-04 on both C-11 and C-29, V-05 on both C-28 and C-29.

**C-29: V-01 and V-02 (PASS) vs. V-03 and V-05 (PARTIAL) vs. V-04 (FAIL)**

V-01 and V-02 both name the triggering criterion ID in the cascade declaration ("C-28 auto-PASS when C-07 auto-PASS fires"), making the cascade graph readable without cross-referencing. V-03 and V-05 present only the data condition ("no prior-round data"), and V-04 omits the declaration entirely.

---

#### REGRESSION SIGNALS

Prior-round scorecard not provided. **C-07 auto-PASS — no regression comparison possible.**

---

#### LEADERBOARD

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 | V-01 | 100.00 | YES |
| 2 | V-02 | 99.77 | YES |
| 2 | V-03 | 99.77 | YES |
| 4 | V-05 | 99.55 | YES |
| 5 | V-04 | 99.09 | YES |

Score distribution note: min=99.09, max=100.00, spread=0.91 pt. Scores **cluster** (< 5 pt spread) — expected at this rubric maturity level where all essential and recommended criteria are structurally stable and only aspirational fine-grained criteria discriminate. Each aspirational criterion contributes 10/22 ≈ 0.45 pt; V-04's two FAILs (C-11 + C-29) account for its full 0.91 pt gap from the ceiling. V-02/V-03's single PARTIAL accounts for 0.23 pt each. V-05's two PARTIALs (additive, non-interacting) accounts for 0.45 pt — confirming structural independence of C-28 and C-29 mechanisms.

---

### R11 Summary

| V | C-11 | C-28 | C-29 | Score | Delta from V-01 |
|---|------|------|------|-------|-----------------|
| V-01 | PASS | PASS | PASS | 100.00 | — |
| V-02 | PASS | PARTIAL | PASS | 99.77 | -0.23 |
| V-03 | PASS | PASS | PARTIAL | 99.77 | -0.23 |
| V-05 | PASS | PARTIAL | PARTIAL | 99.55 | -0.45 |
| V-04 | FAIL | PASS | FAIL | 99.09 | -0.91 |

**Hypotheses confirmed:**
- C-28 and C-29 are structurally independent: V-05 = V-02 + V-03 degradation exactly (additive, ~0.45 pt total).
- V-04 controlled co-failure: one structural decision (absent C-28 declaration) causes C-11 FAIL + C-29 FAIL simultaneously (~0.91 pt gap).
- Evidence ladders validated: C-28 FAIL→PARTIAL→PASS from col-absent → col-5 → col-4; C-29 FAIL→PARTIAL→PASS from absent → condition-only → trigger-ID.

**Excellence signals from V-01 for R12 candidate criteria:**

1. **Gate cascade declarations enumerate all downstream beneficiaries**: V-01's C-07 declaration reads "C-27 and C-28 also auto-PASS" — explicitly covering both cascade dependents. When a gate criterion has multiple downstream cascades, the gate declaration should name all of them to prevent partial cascade graphs from accumulating across versions.

2. **Column position as causal contract**: The regression table's 5-column order (criterion → prior → current → variation → mechanism) encodes a complete diagnostic chain where each column answers a distinct causal question. Template designs where column order encodes causality are more resistant to versioner drift than designs where columns are appended arbitrarily.

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Gate cascade declarations enumerate all downstream beneficiaries: when a gating criterion (e.g., C-07) cascades to multiple downstream auto-PASSes, the gate declaration must list all beneficiaries explicitly (C-27 and C-28), not just the first-added one", "Column position as causal contract: regression table 5-column order (criterion | prior | current | variation | mechanism) encodes a complete diagnostic chain where each position answers a distinct causal question; appending columns after Mechanism breaks this contract even when the column content is correct"]}
```
