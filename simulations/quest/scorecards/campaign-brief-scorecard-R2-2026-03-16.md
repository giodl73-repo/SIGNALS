# Quest Scorecard — campaign-brief — Round 2
**Date:** 2026-03-16
**Variations:** V-01 through V-05
**Rubric:** v2 (13 criteria, 130 points max)

---

## Scoring Table

| Criterion | Tier | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|------|
| C-01 Sub-skills invoked in order | E | PASS | PASS | PASS | PASS | PASS |
| C-02 Signals enumerated by namespace | E | PASS | PASS | PASS | PASS | PASS |
| C-03 Missing signals explicitly named | E | PASS | PASS | PASS | PASS | PASS |
| C-04 Narrative arc synthesizes signals | E | PASS | PASS | PASS | PASS | PASS |
| C-05 Topic registered name/date/intent | E | PASS | PASS | PASS | PASS | PASS |
| C-06 Explicit readiness verdict | R | PASS | PASS | PASS | PASS | PASS |
| C-07 Gap prioritization / inertia framing | R | PARTIAL | PASS | PARTIAL | PASS | PASS |
| C-08 Visual hierarchy / structural blocks | R | PASS | PASS | PASS | PASS | PASS |
| C-09 Session delta block | A | PASS | FAIL | FAIL | FAIL | PASS |
| C-10 Confidence metric (derived, auditable) | A | FAIL | FAIL | PASS | PARTIAL | PASS |
| C-11 Per-gap commit-risk fields | A | FAIL | PASS | FAIL | PASS | PASS |
| C-12 Prose confined to STORY section | A | PASS | PASS | PARTIAL | PASS | PARTIAL |
| C-13 Silence-breaking structural enforcement | A | PASS | PASS | PASS | PASS | PASS |

---

## Evidence Notes

### V-01 — Session delta
- **C-07 PARTIAL:** V-05 base uses blocking/optional labels but no inertia cost framing — labeling without consequence grounding.
- **C-09 PASS:** DELTA block is the sole axis; mandatory even on first run ("prior_brief: NONE") — cleanest structural enforcement in the round.
- **C-10 FAIL:** No confidence mechanism added.
- **C-11 FAIL:** No per-gap inertia or consequence fields.
- **C-12 PASS:** V-05 base confines prose to STORY; DELTA block is structured data only.

### V-02 — Commit-risk grounding per gap
- **C-07 PASS:** `Assumption:` + `Consequence:` per blocking entry is item-level inertia framing — stronger than R1 V-04's thematic framing because the reclassification rule is structural.
- **C-09 FAIL:** No DELTA block.
- **C-10 FAIL:** No confidence table or derived score.
- **C-11 PASS:** Two-field mandatory structure forces reclassification when Consequence is absent — strongest C-11 mechanism in the round.
- **C-12 PASS:** STORY prose is unaffected; STATUS verbosity stays within STATUS block boundary.

### V-03 — Confidence dimension rubric
- **C-07 PARTIAL:** V-05 base gap labeling present; no inertia framing axis added.
- **C-09 FAIL:** No DELTA block.
- **C-10 PASS:** Three-dimension scoring (breadth 1-3 × depth 1-3 × gap severity 1-3) with derived average and defined thresholds — deterministic and auditable. First structural C-10 PASS in the round.
- **C-11 FAIL:** No per-gap inertia fields.
- **C-12 PARTIAL:** Confidence table inserted *into* STORY section — structured data in a prose-designated section blurs the confinement boundary. Not a FAIL (table is structured, not prose) but enforcement is weakened.

### V-04 — R1 structural winner + R1 content winner
- **C-07 PASS:** `Inertia risk:` per blocking gap in STATUS + `inertia_cost:` in VERDICT — the R1 excellence signal operationalized at item level.
- **C-09 FAIL:** No DELTA block by design ("safe combination" test).
- **C-10 PARTIAL:** `inertia_cost:` in VERDICT implies a confidence dimension but is prose-qualified, not derived from a scoring table. Not auditable in isolation — PARTIAL is the ceiling.
- **C-11 PASS:** `Inertia risk:` per blocking gap is the R1 pattern that defined this criterion.
- **C-12 PASS:** All prose confined to STORY; VERDICT carries structured fields only.

### V-05 — Full aspirational sweep
- **C-07 PASS:** Per-gap inertia fields in STATUS inherited from V-04 axis.
- **C-09 PASS:** DELTA block present; mandatory on first run.
- **C-10 PASS:** Confidence dimension table in STORY — derived, auditable, three dimensions.
- **C-11 PASS:** Per-gap inertia fields from V-04 axis + V-02 Consequence structure.
- **C-12 PARTIAL:** Confidence table inserted into STORY creates the same pressure as V-03 — structured data competes with narrative prose for the section's designated role. The six-block structure holds, but STORY is the overload point.
- **C-13 PASS:** Silence-breaking enforcement structural in V-05 base.
- **C-01 note:** Six-block structure adds orchestration overhead but sequence remains structurally defined — PASS holds. Execution fidelity is the risk to watch in simulation, not a scoring downgrade here.

---

## Score Summary

| Variation | Essential (50) | Recommended (30) | Aspirational (50) | Total (130) |
|-----------|---------------|-----------------|-------------------|-------------|
| V-01 | 50 | 25 | 30 | **105** |
| V-02 | 50 | 30 | 30 | **110** |
| V-03 | 50 | 25 | 25 | **100** |
| V-04 | 50 | 30 | 35 | **115** |
| V-05 | 50 | 30 | 45 | **125** |

**Ranking:** V-05 > V-04 > V-02 > V-01 > V-03

---

## Excellence Signals from V-05

**1. All-essential base holds under load.** Adding DELTA + confidence table + per-gap inertia fields to the V-05 terminal block structure doesn't degrade any Essential criterion. The only degradation is C-12 PARTIAL — one aspirational criterion — from STORY section inflation. The combination is viable at 125/130.

**2. STORY is the structural pressure point.** When two aspirational features (confidence table from V-03 + narrative synthesis from C-04) must share a single section, the "prose confined to STORY" invariant weakens. This is not a prompt-writing failure — it is a structural conflict between C-10 and C-12. The natural resolution is a dedicated CONFIDENCE block, separate from STORY.

**3. Per-gap fields scale with blocking gap count.** V-02's Assumption/Consequence structure and V-04's Inertia risk field both contribute to STATUS verbosity in V-05. At low gap counts the section is clean; the density problem is a function of gap count, not structure. A maximum fields-per-gap entry threshold is not currently captured.

---

## New Patterns for Rubric v3

**Pattern A — Confidence block isolation.** Derived confidence scores (C-10) should occupy a dedicated named block, not STORY. STORY is for narrative cross-signal synthesis (C-04); embedding a scoring table there creates a structural conflict. No criterion currently enforces block separation for confidence output.

**Pattern B — STATUS density ceiling.** Mandatory per-gap fields multiply with blocking gap count. A readability threshold — e.g., "blocking gap entries remain scannable at N gaps" — is not captured by C-11 (which measures presence of the fields) or C-12 (which measures STORY discipline).

---

```json
{"top_score": 125, "all_essential_pass": true, "new_patterns": ["Confidence block isolation — derived confidence scores (C-10) placed inside STORY create a C-10/C-12 structural conflict; a dedicated CONFIDENCE block resolves this without inflating the narrative section", "STATUS density ceiling — mandatory per-gap inertia fields scale with blocking gap count; a readability threshold for STATUS entry count is not captured by C-11 or C-12"]}
```
