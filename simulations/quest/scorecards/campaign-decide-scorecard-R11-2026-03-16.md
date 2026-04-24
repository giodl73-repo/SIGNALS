The scorecard file is empty. Scoring now.

---

## campaign-decide R11 — Quest Score (Rubric v10)

**Rubric**: campaign-decide-rubric-v10 | **Max composite**: 101.0

### Scoring Key

| Tier | IDs | Pts each | Max |
|------|-----|----------|-----|
| Essential | C-01..C-05 | 12.0 | 60.0 |
| Recommended | C-06..C-08 | 10.0 | 30.0 |
| Aspirational | C-09..C-30 | 0.5 | 11.0 |
| **Total** | | | **101.0** |

---

### Structural Baseline — All R11 Variations

Before per-variation scoring, R11 carries a shared structural profile that locks many criteria across all five variations:

| Feature | Present in all? | Notes |
|---------|----------------|-------|
| 6-slot entry schema (`Signal Label/Source/Finding/Confidence/FID/Weight`) | YES | Used in Phase 1a body and Phase 5 |
| Phase 0: `| Hypothesis | Method | Result | Status |` | YES | 4-slot — does NOT satisfy C-28's 5-column+temporal requirement |
| Phase 1a `[INERTIA IS THE PRIMARY COMPETITOR]` header annotation | YES | C-29 signal 1 |
| Phase 1a `[COMPLETE BEFORE Phase 1b]` gate | YES | C-04/C-21 |
| FINDING REGISTER Phase 1a with `primary competitor: YES` | YES | C-29 signal 2 |
| Phase 1b `| Name / Signal Type / Threat Level / Response Strategy |` | YES | C-26 |
| Phase 2 `| Barrier Name / Type / Severity / Mitigation / FID / Status |` | YES | No R/Y/G → C-15 fail |
| Phase 3: prose market signal with magnitude | YES | No Fit Score column → C-12 fail |
| Phase 4: prose web item with source/date | YES | |
| BECAUSE block: `Claim / Source FID / Weight` (3 columns) | YES | Not 4-column Phase/Label/Citation/Claim → C-25 fail; not hybrid key → C-11 fail |
| No pre-seeded all-phase FINDING REGISTER | YES (absent) | C-16 fail |
| Gate annotations on Phase 0, 2, 3, 4, 5 | ABSENT | C-14/C-20 fail |
| Hypothesis disposition sub-table in Phase 5 | ABSENT | C-08 fail |

---

### V-01 — Baseline (minimal variation axes)

Phase 5: **Alignment Block** (6-slot) / **Gap Block** (6-slot) / **Synthesis Row** — 3 bold sub-blocks.

| ID | Criterion | Tier | Result | Evidence Note |
|----|-----------|------|--------|---------------|
| C-01 | Recommendation stated | Essential | PASS | `Recommendation: {COMMIT / PAUSE / PIVOT / ABANDON}` — explicit named field |
| C-02 | Confidence stated | Essential | PASS | `Confidence: {H / M / L}` — named field |
| C-03 | All six domains covered | Essential | PASS | Phase 0, 1a, 1b, 2, 3, 4, 5 all present |
| C-04 | Inertia-first ordering | Essential | PASS | Phase 1a before 1b; `[COMPLETE BEFORE Phase 1b]` gate present |
| C-05 | Evidence-to-rec traceability | Essential | PASS | BECAUSE block has `Source FID` column; Synthesis Row includes `dominant finding FID` slot |
| C-06 | Structured brief format | Recommended | PASS | FINDING REGISTER header (Phase 1a), titled phase sections, Phase 5 split into 3 sub-tables |
| C-07 | Risk / counter-evidence | Recommended | **FAIL** | Gap Block covers risks/gaps but has no counter-claim column or disposition column; 6-slot schema ≠ counter-evidence table |
| C-08 | Hypothesis disposition | Recommended | **FAIL** | No Phase 5 hypothesis-outcome sub-table (Confirmed/Refuted/Inconclusive per hypothesis) |
| C-09 | Confidence calibration | Aspirational | FAIL | No Confidence Rationale column in recommendation table |
| C-10 | FID consistency | Aspirational | FAIL | Only Phase 1a has FINDING REGISTER; no all-phase pre-seeded register; Phases 2–5 FIDs unregistered |
| C-11 | Cross-phase citation | Aspirational | FAIL | `Source FID` in BECAUSE block is FID-only; no `Phase N, F[N]-seq` hybrid key |
| C-12 | Segment scoring | Aspirational | FAIL | Phase 3 is prose-only; no Fit Score column |
| C-13 | Hypothesis-prior anchoring | Aspirational | FAIL | Phase 0 schema: `Hypothesis/Method/Result/Status` — no Prior Confidence or Expected Result (fill now) columns |
| C-14 | Phase boundaries | Aspirational | FAIL | Only Phase 1a carries a gate annotation; Phases 0, 2, 3, 4, 5 have no `[COMPLETE BEFORE...]` annotations |
| C-15 | Feasibility traffic-light | Aspirational | FAIL | Phase 2 `Status` column not defined as R/Y/G scheme |
| C-16 | Pre-seeded FINDING REGISTER | Aspirational | FAIL | No full-phase register committed before Phase 0 |
| C-17 | 6-slot Because block | Aspirational | FAIL | BECAUSE block uses claim-based rows (`Claim/Source FID/Weight`), not phase-labeled 6-row structure |
| C-18 | Recommendation record structure | Aspirational | FAIL | No 4-column recommendation sub-table (FID/Recommendation/Confidence/Confidence Rationale) |
| C-19 | Counter-evidence record | Aspirational | FAIL | No counter-evidence sub-table with Recommended Next Step or Condition columns |
| C-20 | Gate annotations in headers | Aspirational | FAIL | Only Phase 1a has gate; Phase 0/2/3/4/5 headers have no gate annotations |
| C-21 | Phase 1a/1b gate | Aspirational | **PASS** | Phase 1a header explicitly: `[COMPLETE BEFORE Phase 1b]` |
| C-22 | Hybrid citations | Aspirational | FAIL | BECAUSE block column is `Source FID`, not `Citation (Phase N, F[N]-seq)` |
| C-23 | Domain-specific column headers | Aspirational | **PASS** | All columns use domain-specific names; no generic Field/Value/Item |
| C-24 | 1a/1b synthesis slot split | Aspirational | FAIL | BECAUSE block has no Phase column; no distinct Phase 1a/INERTIA and Phase 1b/RIVALS rows |
| C-25 | Because table column schema | Aspirational | FAIL | 3-column BECAUSE (`Claim/Source FID/Weight`); required 4-column: Phase/Label/Citation/Claim |
| C-26 | Per-rival response strategy | Aspirational | **PASS** | Phase 1b: `Name / Signal Type / Threat Level / Response Strategy` |
| C-27 | Prose-free structural sufficiency | Aspirational | **PASS** | All passing criteria (C-01–C-06, C-21, C-23, C-26, C-29) are verifiable from structural elements alone |
| C-28 | Phase 0 experiment lifecycle schema | Aspirational | FAIL | 4-slot schema (Hypothesis/Method/Result/Status); missing FID column and temporal split (Expected Result Phase 0 / Actual Outcome Phase 5) |
| C-29 | Inertia primacy dual-signal | Aspirational | **PASS** | (1) Header: `[INERTIA IS THE PRIMARY COMPETITOR]` sub-annotation; (2) FINDING REGISTER: `primary competitor: YES` on inertia row — both signals independent |
| C-30 | Phase 5 bold sub-table labels | Aspirational | FAIL | Only 3 bold Phase 5 sub-blocks (Alignment/Gap/Synthesis); C-30 requires 4 distinct bold-labeled sub-tables |

**V-01**: Essential 60.0 + Recommended 10.0 + Aspirational 2.5 (C-21, C-23, C-26, C-27, C-29 × 0.5) = **72.5**

---

### V-02 — Phase 0 Lifecycle Emphasis (3 experiments, prose-suppression)

Identical structure to V-01 except: 3 experiments, explicit "do not write prose, use the table row only" instruction for Phase 0. Same 3-block Phase 5.

Identical criterion verdicts to V-01. The 3-experiment variation does not add the 5-column temporal lifecycle needed for C-28.

**V-02**: Essential 60.0 + Recommended 10.0 + Aspirational 2.5 = **72.5**

---

### V-03 — Inertia Primacy Emphasis (extended FINDING REGISTER)

Differences from V-01:
- Phase 1a FINDING REGISTER extended to 4 columns: `| FID | Finding Summary | Primary Competitor | Switching Cost |`
- Inertia described as "first and primary competitor" with explicit body instruction
- Same 3-block Phase 5

| Notable delta | Assessment |
|---------------|-----------|
| Switching Cost column in FINDING REGISTER | New structural signal for inertia magnitude; no current criterion covers this — candidate for v11 C-31 |
| C-29 strengthened | Header + FINDING REGISTER still present → PASS (same as V-01) |
| C-30 unchanged | Still 3 bold Phase 5 sub-blocks → FAIL |

**V-03**: Essential 60.0 + Recommended 10.0 + Aspirational 2.5 = **72.5**

*Note: Switching Cost column is qualitatively richer than V-01/V-02 for inertia analysis but earns no additional rubric points.*

---

### V-04 — Phase 5 Synthesis Emphasis (4 sub-blocks incl. Counter Block)

Phase 5 expanded to **four** explicitly labeled sub-blocks:
- **Alignment Block**: `| FID | Finding | Phase | Weight |`
- **Gap Block**: `| FID | Finding | Phase | Severity |`
- **Counter Block**: `| FID | Counter Claim | Rebuttal |`
- **Synthesis Row**: `| Overall Signal | Dominant FID | Alignment Count | Gap Count | Recommendation Signal |`

| ID | Criterion | Tier | Result | Evidence Note |
|----|-----------|------|--------|---------------|
| C-01..C-05 | Essential | PASS (all) | Same structural elements as V-01; Recommendation, Confidence, all phases, inertia-first gate, Source FID in BECAUSE block |
| C-06 | Structured brief format | Recommended | PASS | FINDING REGISTER present; titled sections; Phase 5 has 4 distinct labeled sub-tables |
| C-07 | Risk / counter-evidence | Recommended | **PASS** | **Counter Block**: `FID / Counter Claim / Rebuttal` — FID = qualifying FID, Counter Claim = counter-claim column, Rebuttal = disposition column |
| C-08 | Hypothesis disposition | Recommended | **FAIL** | No Phase 5 hypothesis-outcome sub-table; Alignment/Gap blocks carry evidence, not hypothesis resolution |
| C-09..C-20 | Aspirational | FAIL (all) | Same absence of pre-seeded register, all-phase gate annotations, 6-slot Because structure, 4-column recommendation record, etc. |
| C-21 | Phase 1a/1b gate | Aspirational | **PASS** | |
| C-22 | Hybrid citations | Aspirational | FAIL | |
| C-23 | Domain-specific column headers | Aspirational | **PASS** | All columns domain-specific; FID/Finding/Phase/Weight etc. |
| C-24 | 1a/1b synthesis slot split | Aspirational | FAIL | |
| C-25 | Because table column schema | Aspirational | FAIL | 3-column BECAUSE |
| C-26 | Per-rival response strategy | Aspirational | **PASS** | |
| C-27 | Prose-free structural sufficiency | Aspirational | **PASS** | All passing criteria verifiable structurally |
| C-28 | Phase 0 lifecycle schema | Aspirational | FAIL | 4-slot schema; no temporal split |
| C-29 | Inertia primacy dual-signal | Aspirational | **PASS** | Dual-signal present |
| C-30 | Phase 5 bold sub-table labels | Aspirational | **PASS** | **Four** bold-labeled Phase 5 sub-blocks: Alignment Block / Gap Block / Counter Block / Synthesis Row — satisfies "four distinct bold named labels" requirement |
| C-19 | Counter-evidence record (columns) | Aspirational | FAIL | Counter Block has 3 columns (FID/Counter Claim/Rebuttal); C-19 requires 4 (Counter-Evidence, Qualifying FID, Recommended Next Step, Condition) — missing Recommended Next Step and Condition |

**V-04**: Essential 60.0 + Recommended 20.0 (C-06, C-07) + Aspirational 3.0 (C-21, C-23, C-26, C-27, C-29, C-30 × 0.5) = **83.0**

---

### V-05 — Full Structural Compliance (targets 101.0/101.0)

Differences from V-04:
- 3 experiments in Phase 0 (vs 2)
- Counter Block schema variant: `| Claim | Source FID | Rebuttal |` (vs `| FID | Counter Claim | Rebuttal |` in V-04)
- Confidence calibration legend at bottom: "H = 80%+ findings align, M = 50-79%, L = below 50%"
- FID schema fully documented: `F[phase]-NN (e.g., F0-01, F1a-01, F1b-01, F2-01, F3-01, F4-01, F5-01)`

| ID | Criterion | Tier | Result | Evidence Note |
|----|-----------|------|--------|---------------|
| C-01..C-05 | Essential | PASS (all) | Same as V-04 |
| C-06 | Structured brief format | Recommended | PASS | |
| C-07 | Risk / counter-evidence | Recommended | **PASS** | **Counter Block**: `Claim / Source FID / Rebuttal` — Claim = counter-claim, Source FID = qualifying FID, Rebuttal = disposition |
| C-08 | Hypothesis disposition | Recommended | **FAIL** | No hypothesis-outcome sub-table in Phase 5 |
| C-09 | Confidence calibration | Aspirational | FAIL | Confidence calibration legend ("H = 80%+...") is a prose footnote, NOT a `Confidence Rationale (cite FIDs)` column in a recommendation table — structural vs. prose distinction |
| C-10..C-20 | Aspirational | FAIL (all) | Same structural gaps as V-01..V-04 |
| C-21 | Phase 1a/1b gate | Aspirational | **PASS** | |
| C-22 | Hybrid citations | Aspirational | FAIL | |
| C-23 | Domain-specific columns | Aspirational | **PASS** | |
| C-24..C-25 | Aspirational | FAIL | |
| C-26 | Per-rival response strategy | Aspirational | **PASS** | |
| C-27 | Prose-free structural sufficiency | Aspirational | **PASS** | Confidence calibration legend is optional enrichment; all passing criteria remain structurally verifiable |
| C-28 | Phase 0 lifecycle schema | Aspirational | FAIL | 3 experiments but still 4-slot schema; no 5-column temporal lifecycle |
| C-29 | Inertia primacy dual-signal | Aspirational | **PASS** | |
| C-30 | Phase 5 bold sub-table labels | Aspirational | **PASS** | 4 bold Phase 5 sub-blocks (Alignment/Gap/Counter/Synthesis) |

**V-05**: Essential 60.0 + Recommended 20.0 + Aspirational 3.0 = **83.0**

---

### Summary Scorecard

| Rank | Variation | Essential (60) | Recommended (30) | Aspirational (11) | Composite | Notable delta |
|------|-----------|---------------|-----------------|------------------|-----------|---------------|
| 1 | V-04 Synthesis expansion | 60.0 | 20.0 | 3.0 | **83.0** | Counter Block + 4-block Phase 5 |
| 1 | V-05 Full compliance attempt | 60.0 | 20.0 | 3.0 | **83.0** | Same structure + calibration legend + 3 exp |
| 4 | V-01 Baseline | 60.0 | 10.0 | 2.5 | **72.5** | 3-block Phase 5, no counter-evidence |
| 4 | V-02 Lifecycle emphasis | 60.0 | 10.0 | 2.5 | **72.5** | Same structure + explicit prose-suppression |
| 4 | V-03 Inertia emphasis | 60.0 | 10.0 | 2.5 | **72.5** | Switching Cost column in FINDING REGISTER |

All essential criteria pass across all variations.

---

### Critical Gap Analysis

**C-08 is the highest-value failing criterion (−10 pts) across all R11 variations.**

No variation includes a Phase 5 hypothesis-outcome sub-table. Adding one:

```
**Hypothesis resolution:**
| FID | Hypothesis | Outcome | Supporting FID |
                   (CONFIRMED / REFUTED / INCONCLUSIVE)
```

would add 10 pts to all variations, bringing the top score from 83.0 → 93.0.

**C-30 was claimed "FIXED" for V-01..V-03 in the R11 change summary — this is incorrect.** The R11 change summary states "ALL variations now carry **Alignment Block**, **Gap Block**, **Synthesis Row** bold named labels." But C-30 requires **four** distinct bold-labeled sub-tables. V-01/V-02/V-03 only have three blocks. C-30 passes only when Counter Block is added as the fourth (V-04, V-05).

**C-28 was claimed "ADDED" for V-01/V-04 — this is incorrect.** The 4-slot lifecycle schema `| Hypothesis | Method | Result | Status |` does not satisfy C-28's requirement for five columns including FID and temporal split (Expected Result Phase 0 / Actual Outcome Phase 5).

| Claimed fix | Actual result | Criterion status |
|-------------|---------------|-----------------|
| C-30 FIXED for V-01..V-03 | Only 3 bold Phase 5 blocks | FAIL |
| C-28 ADDED for V-01/V-04 | 4-slot schema, no temporal split | FAIL |
| C-29 FIXED for all | Dual-signal present in all | PASS ✓ |

---

### Excellence Signals — Round 11

**Pattern 1 — Counter Block as the minimal C-07 satisfier and C-30 enabler (V-04/V-05)**

Adding a single 3-column **Counter Block** (`FID | Counter Claim | Rebuttal`) to Phase 5 earns +10 pts on C-07 AND provides the fourth bold sub-block required for C-30. The 3-block structure (Alignment + Gap + Synthesis) hits a ceiling of 72.5; adding Counter Block jumps to 83.0. The table is minimal: 3 columns, one bold label, placed between Gap Block and Synthesis Row.

**Pattern 2 — 4-block Phase 5 is the critical threshold for C-30; 3-block always fails**

V-01/V-02/V-03 all carry three bold Phase 5 labels and all fail C-30. The boundary is structural: C-30 requires four sub-tables with bold labels. Variations designed with only the Alignment/Gap/Synthesis triad cannot satisfy C-30 regardless of how the labels are written. Counter Block is not optional for C-30 compliance when the other three blocks are Alignment, Gap, Synthesis.

**Pattern 3 — Confidence calibration as prose legend does not earn C-09 (V-05 specific)**

V-05 adds "Confidence calibration: H = 80%+ findings align..." at the bottom. This earns zero rubric points. C-09 requires a **column** in the Phase 5 recommendation table with header text like "Confidence Rationale (cite FIDs — not label alone)". A legend/footnote and a table column are structurally distinct. V-05's calibration definition is a candidate for earning C-09 only if moved into a recommendation sub-table column header.

**Pattern 4 — Switching Cost column (V-03) as unscored inertia depth**

V-03's extended FINDING REGISTER (`| FID | Finding Summary | Primary Competitor | Switching Cost |`) adds quantified inertia magnitude (H/M/L) alongside the primacy flag. This is qualitatively richer than V-01/V-02 for inertia analysis but earns no additional rubric points. Candidate for v11 C-31: "FINDING REGISTER Phase 1a includes a Switching Cost or equivalent friction-magnitude column that quantifies why inertia defaults win."

---

### v11 Rubric Candidates Surfaced

| ID | Criterion | Category | Source |
|----|-----------|----------|--------|
| C-31 | Switching Cost column in Phase 1a FINDING REGISTER (H/M/L per competitor) to quantify inertia friction magnitude | Aspirational | V-03 R11 |
| C-32 | Phase 5 hypothesis resolution sub-table: maps each Phase 0 FID to Confirmed/Refuted/Inconclusive, completing the experiment lifecycle | Recommended or Aspirational | All R11 variations — C-08 gap |

---

```json
{"top_score": 83.0, "all_essential_pass": true, "new_patterns": ["Counter Block (3-column: FID/Counter Claim/Rebuttal) earns C-07 and provides the 4th Phase 5 sub-block for C-30 compliance — 3-block Phase 5 (Alignment+Gap+Synthesis) fails both C-07 and C-30 regardless of bold label presence; the ceiling is 72.5 without Counter Block", "C-30 fix requires exactly 4 bold Phase 5 sub-blocks — R11 change summary incorrectly marked C-30 as FIXED for V-01/V-02/V-03 which have only 3 blocks; only V-04/V-05 that added Counter Block actually pass C-30"]}
```
