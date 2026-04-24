Now I have everything needed. Let me score all five variations against the v8 rubric.

---

# Quest Score — prove-prototype Round 8 (v8 rubric, 204 pts)

**Date**: 2026-03-15
**Rubric version**: v8 (added C-27, C-28)
**Scoring basis**: Template design enforceability — R7 V-04 (180/190) is the forward-projected baseline

---

## Point Weights

| Tier | Criteria | Pts/criterion | Total |
|------|----------|--------------|-------|
| Essential | C-01–C-05 | 12 | 60 |
| Recommended | C-06–C-08 | 10 | 30 |
| Aspirational | C-09, C-10, C-16–C-25 | 7 | 84 |
| Aspirational | C-26 | 6 | 6 |
| Aspirational | C-27, C-28 | 7 each | 14 |
| Excellence | C-11–C-15 | 2 | 10 |
| **Total** | | | **204** |

---

## Baseline Projection: R7 V-04 on v8 Rubric

R7 V-04 scored 180/190 — all essential, recommended, and aspirational criteria passing (C-01 through C-26), zero excellence. Mapped to v8: 180/204. C-27 and C-28 are not achievable by that template; 24 pts remain (14 new aspirational + 10 excellence ceiling).

---

## V-01 — Completion-Grade Encoding (R7 V-04 verbatim + FULL|PARTIAL tokens)

**Container**: SETUP(THINKER + ANCHOR) / BUILD(MAKER + WATCHER) / CLOSE
**Axis**: Inline `FULL|PARTIAL` grade token as first word after dash in every PHASE N COMPLETE line. Zero structural change from R7 V-04.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** 12 | THINKER in SETUP writes hypothesis first — identical to R7 V-04 |
| C-02 | **PASS** 12 | Two exclusions with co-located validity rationale — inherited |
| C-03 | **PASS** 12 | Measurement criteria frozen in SETUP before BUILD — inherited |
| C-04 | **PASS** 12 | CLOSE comparison phase — inherited |
| C-05 | **PASS** 12 | CLOSE verdict phase — inherited |
| C-06 | **PASS** 10 | MAKER minimality trade-off in BUILD — inherited |
| C-07 | **PASS** 10 | WATCHER raw observations in BUILD — inherited |
| C-08 | **PASS** 10 | CLOSE limitations + next step — inherited |
| C-09 | **PASS** 7 | CLOSE counter-evidence — inherited |
| C-10 | **PASS** 7 | MAKER replication steps in BUILD — inherited; FULL|PARTIAL grade now makes partial replication visible at scan level |
| C-16 | **PASS** 7 | CLOSE binary counter-evidence disposition — inherited |
| C-17 | **PASS** 7 | Prose co-location in conversational register — inherited |
| C-18 | **PASS** 7 | Binary closures throughout — inherited |
| C-19 | **PASS** 7 | Inline gate markers per phase — inherited |
| C-20 | **PASS** 7 | PHASE N COMPLETE lines with named outcomes — inherited |
| C-21 | **PASS** 7 | CLOSE absorbs all trailing sections explicitly — inherited from R7 V-04 |
| C-22 | **PASS** 7 | Completion lines carry result values — inherited; C-27 tokens extend C-22 automatically |
| C-23 | **PASS** 7 | SETUP and BUILD role headers carry explicit prohibitions — inherited |
| C-24 | **PASS** 7 | Three containers (SETUP, BUILD, CLOSE) map to distinct lifecycle stages — inherited |
| C-25 | **PASS** 7 | SETUP(2 roles) + BUILD(2 roles); container scan (3 headers) ≠ role scan (4 labels) — inherited |
| C-26 | **PASS** 6 | ANCHOR writes B-00 in SETUP; CLOSE completion: "observed [X] vs. B-00 [Y], delta [Z]" — inherited |
| C-27 | **PASS** 7 | `FULL|PARTIAL` grade token is first word after dash in PHASE N COMPLETE line — satisfies "labeled token in the completion line" |
| C-28 | **FAIL** 0 | SETUP holds both THINKER (scope/hypothesis) and ANCHOR (calibration) — mixed scope; baseline container not exclusively pre-build. Container scan cannot distinguish pre-build from scope-definition within SETUP |
| C-11–C-15 | **FAIL** 0 | Not addressed |

**V-01 Total: 60 + 30 + 90 + 7 + 0 + 0 = 187 / 204**

---

## V-02 — Alt C-27 Encoding (co-located labeled pair instead of inline token)

**Container**: SETUP(THINKER + ANCHOR) / BUILD(MAKER + WATCHER) / CLOSE
**Axis**: Grade expressed as `**Completeness**: FULL | PARTIAL — reason` in a labeled pair block adjacent to the PHASE N COMPLETE line, not embedded inside the line itself.

| ID | Result | Evidence |
|----|--------|----------|
| C-01–C-26 | **Same as V-01** | Structure is identical to V-01; only the C-27 encoding differs |
| C-27 | **FAIL** 0 | Pass condition requires "an explicit grade as a labeled token in the completion line." The labeled pair is adjacent to `PHASE N COMPLETE —` but separate from it — the completion line itself still omits the grade. A scan of completion lines alone cannot recover the grade without reading the labeled pair block. C-22 is still satisfied (result values are in the PHASE N COMPLETE line), but the grade is not |
| C-28 | **FAIL** 0 | Same SETUP mixing as V-01 |
| C-11–C-15 | **FAIL** 0 | Not addressed |

**V-02 Total: 60 + 30 + 90 + 0 + 0 + 0 = 180 / 204**

**C-27 finding**: The distinction between "grade in the completion line" and "grade adjacent to the completion line" is the discriminator between 187 and 180. A labeled pair co-located at the same structural level but in a separate block breaks the scan-only auditability property that C-27 requires. The token must be inside the `PHASE N COMPLETE —` line.

---

## V-03 — CALIBRATE Isolation (DESIGN first, dedicated CALIBRATE container)

**Container**: DESIGN(FRAMER + ANCHOR scope-phase) / CALIBRATE(ANCHOR calibration-phase only) / BUILD(MAKER + WATCHER) / CLOSE
**Axis**: SETUP split into DESIGN (hypothesis + scope + measurement) preceding CALIBRATE (B-00 only). Hypothesis first in DESIGN preserves C-01. No FULL|PARTIAL grade tokens.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** 12 | DESIGN opens with hypothesis — DESIGN precedes CALIBRATE in container order; C-01 is unambiguous |
| C-02 | **PASS** 12 | DESIGN scope phase — exclusions + co-located validity |
| C-03 | **PASS** 12 | DESIGN measurement criteria precede BUILD at container level |
| C-04 | **PASS** 12 | CLOSE comparison — inherited pattern |
| C-05 | **PASS** 12 | CLOSE verdict — inherited |
| C-06 | **PASS** 10 | MAKER minimality in BUILD — inherited |
| C-07 | **PASS** 10 | WATCHER raw observations in BUILD — inherited |
| C-08 | **PASS** 10 | CLOSE limitations + next step — inherited |
| C-09 | **PASS** 7 | CLOSE counter-evidence — inherited |
| C-10 | **PASS** 7 | MAKER replication steps in BUILD — inherited |
| C-16 | **PASS** 7 | CLOSE binary counter-evidence disposition — inherited |
| C-17 | **PASS** 7 | Co-location enforced per phase — inherited |
| C-18 | **PASS** 7 | Binary closures — inherited |
| C-19 | **PASS** 7 | Inline gate markers per phase — inherited |
| C-20 | **PASS** 7 | Completion lines per phase — inherited |
| C-21 | **PASS** 7 | CLOSE absorbs all trailing sections — inherited from CLOSE-container pattern |
| C-22 | **PASS** 7 | Completion lines carry result values — inherited |
| C-23 | **PASS** 7 | Role prohibitions per role header — inherited |
| C-24 | **PASS** 7 | Four containers (DESIGN, CALIBRATE, BUILD, CLOSE) map to distinct stages — each container single-stage |
| C-25 | **PASS** 7 | DESIGN(1+ roles) + BUILD(2 roles); 4 containers vs. 4+ roles; container scan ≠ role scan — BUILD still multi-role ensuring orthogonality |
| C-26 | **PASS** 6 | CALIBRATE establishes B-00 before BUILD; CLOSE completion carries B-00 delta |
| C-27 | **FAIL** 0 | No FULL|PARTIAL grade tokens in completion lines |
| C-28 | **PASS** 7 | CALIBRATE holds only B-00 calibration activity — no hypothesis framing, no scope definition, no build. A container scan reveals that all content within CALIBRATE is exclusively pre-build. Pass condition met |
| C-11–C-15 | **FAIL** 0 | Not addressed |

**V-03 Total: 60 + 30 + 90 + 0 + 7 + 0 = 187 / 204**

---

## V-04 — Combined: Grade + CALIBRATE Isolation

**Container**: DESIGN / CALIBRATE / BUILD / CLOSE (identical structure to V-03)
**Axis**: Both V-01 and V-03 interventions applied simultaneously. Grade tokens in every completion line (C-27 target) AND dedicated CALIBRATE container (C-28 target). Two interventions on orthogonal structural dimensions.

| ID | Result | Evidence |
|----|--------|----------|
| C-01–C-26 | **All PASS** | V-03 structure with hypothesis first in DESIGN — all inherited from V-03 analysis |
| C-27 | **PASS** 7 | Inline `FULL|PARTIAL` grade token in every PHASE N COMPLETE line — from V-01 intervention. C-28's CALIBRATE container does not interfere; the grade applies to all phases including the CALIBRATE completion line (e.g., `CALIBRATE COMPLETE — FULL: B-00 measured = [value], no build activity in container`) |
| C-28 | **PASS** 7 | CALIBRATE holds B-00 only — from V-03 intervention. C-27's grade token appears on the CALIBRATE completion line without contaminating the container's single-function scope |
| C-11–C-15 | **FAIL** 0 | Not addressed |

**Interaction check**: C-27 operates at line-level encoding; C-28 operates at container-level scoping. The grade token added to a completion line is a lexical addition — it neither adds phases to CALIBRATE nor changes what CALIBRATE contains. The two mechanisms are structurally independent and stack without interference.

**V-04 Total: 60 + 30 + 90 + 7 + 7 + 0 = 194 / 204**

---

## V-05 — Combined + Inertia Framing

**Container**: DESIGN / CALIBRATE / BUILD / CLOSE (identical to V-04)
**Axis**: V-04 base + (a) B-00 named explicitly as the inertia competitor in CALIBRATE, (b) Phase 7 three-column results table (predicted / observed / B-00), (c) primary inertia counter-interpretation seeded in Phase 9.

| ID | Result | Evidence |
|----|--------|----------|
| C-01–C-26 | **All PASS** | Same as V-04 — container structure identical |
| C-27 | **PASS** 7 | Grade tokens inherited from V-04 |
| C-28 | **PASS** 7 | CALIBRATE isolation inherited from V-04 |
| C-09 | **PASS** 7 (quality enriched) | Inertia counter-interpretation seeded in Phase 9 strengthens the named counter-interpretation; C-09 was already PASS — no additional points, higher quality |
| C-16 | **PASS** 7 (quality enriched) | Inertia framing makes the null counter-evidence case more grounded; still a PASS, not a new scoring dimension |
| C-26 | **PASS** 6 (quality enriched) | Three-column table (predicted / observed / B-00) is the strongest C-26 expression yet — baseline comparison is structurally unavoidable, not just instructed. Still 6 pts; inertia depth is subsumed into existing pass |
| C-11–C-15 | **FAIL** 0 | Inertia framing enriches C-12 candidates (three-column table naturally produces quantified deltas) but the template does not explicitly require failure mode identification (C-11) or boundary condition testing (C-13). No excellence criteria crossed |

**V-05 Total: 60 + 30 + 90 + 7 + 7 + 0 = 194 / 204**

V-05 matches V-04 on rubric score. The inertia framing produces measurable quality gains on C-09, C-16, and C-26 that are not resolved into distinct scoring by the v8 rubric — and the three-column table structure is the strongest C-12 candidate surfaced to date without yet crossing the excellence threshold.

---

## Composite Scores and Ranking

| Rank | Variation | Essential | Recommended | Aspirational | Excellence | Total | % |
|------|-----------|-----------|-------------|-------------|------------|-------|---|
| 1 | **V-04** Combined | 60/60 | 30/30 | 104/104 | 0/10 | **194** | 95.1% |
| 1 | **V-05** Combined + inertia | 60/60 | 30/30 | 104/104 | 0/10 | **194** | 95.1% |
| 3 | **V-01** Grade tokens only | 60/60 | 30/30 | 97/104 | 0/10 | **187** | 91.7% |
| 3 | **V-03** CALIBRATE only | 60/60 | 30/30 | 97/104 | 0/10 | **187** | 91.7% |
| 5 | **V-02** Alt encoding | 60/60 | 30/30 | 90/104 | 0/10 | **180** | 88.2% |

All five variations: all essential pass. All variations achieve 88%+ composite.

---

## Criterion Analysis

### C-27 vs C-28: Independent dimensions confirmed

The clean arithmetic confirms the orthogonality design claim:
- V-01 (grade only): 180 + 7 = 187
- V-03 (CALIBRATE only): 180 + 7 = 187
- V-04 (both): 180 + 7 + 7 = 194

No interaction penalty. No interaction bonus. C-27 (line-level lexical encoding) and C-28 (container-level scoping boundary) are structurally independent — they can be scored on different structural passes of the same document without one mechanism affecting the other.

### C-27: Token location is non-negotiable

V-02 confirms the pass condition boundary precisely. The labeled pair `**Completeness**: FULL` placed adjacent to the `PHASE N COMPLETE —` line satisfies C-22 (result values in completion line) but not C-27. The auditability property C-27 encodes — "scan completion lines alone to detect degradation" — requires the grade to reside inside the `PHASE N COMPLETE —` string. An adjacent block requires two lines to be read. The 7-point gap between V-02 (180) and V-01 (187) is entirely attributable to this single location constraint.

### C-28: DESIGN-before-CALIBRATE is the correct container order

The R7 V-05 analysis identified that B-00-first ordering caused C-01 failure. R8 V-03 resolves this by placing DESIGN before CALIBRATE — hypothesis is first in DESIGN; B-00 measurement follows in a dedicated downstream container. This is the correct ordering: `hypothesis → scope → measurement criteria → baseline measurement → build → evaluate`. CALIBRATE's single-function guarantee remains intact because the DESIGN container absorbs all non-measurement setup activity.

### V-05 inertia framing: quality ceiling not yet captured

The three-column table (predicted / observed / B-00) is the strongest C-26 enforcement mechanism in any round — the delta against baseline is structurally embedded in a column the model must populate, not an inline instruction. This likely crosses the C-12 (effect size estimated) threshold in live runs: a three-column comparison table with populated cells is an effect size by construction. A v9 round should test this with C-12 targeted explicitly as a live model run rather than template design scoring.

---

## Excellence Signals — Round 8

### E-1: Token-in-line vs. adjacent-token is a detectable design boundary (V-02 finding)

The C-27 fail evidence from V-02 defines a clean binary: the grade token must be part of the same string that begins `PHASE N COMPLETE —`. Any format that requires the reader to move off that line — including a well-structured labeled pair immediately below — breaks the scan-only auditability that C-27 encodes. This is a sharper pass condition than the rubric text made obvious and should be reflected in rubric wording for v9.

### E-2: CALIBRATE isolation plus grade encoding is the additive ceiling for R8

V-04 and V-05 demonstrate that the two new criteria are the complete surface for R8. No excellence criteria are reachable through structural template design alone at this stage — C-11 through C-15 require explicit template prompting for failure mode, effect size, boundary conditions, and negative result treatment. The R8 ceiling of 194/204 (95.1%) represents complete aspirational coverage under v8 criteria.

### E-3: Inertia framing enriches C-09, C-16, and C-26 without new rubric points — candidate for v9 criterion (V-05 axis)

V-05's B-00-as-inertia-competitor pattern adds:
- **C-09 depth**: counter-interpretation is not a generic alternative but the status-quo approach, named and quantified in CALIBRATE before any build activity
- **C-26 strength**: the three-column comparison (predicted / observed / B-00) makes baseline comparison structurally unavoidable — the column must be populated
- **C-12 proximity**: a populated three-column table is functionally an effect size measurement

The rubric score is identical to V-04, but V-05's inertia framing is the strongest C-12 candidate in eight rounds without an explicit C-12 prompt. This is the correct signal for a v9 excellence-to-aspirational promotion of C-12, or a dedicated C-29 for "baseline named as inertia competitor in CALIBRATE phase."

---

```json
{"top_score": 194, "all_essential_pass": true, "new_patterns": ["Completion-grade token must reside inside the PHASE-N-COMPLETE line itself — an adjacent labeled pair breaks scan-only auditability even when co-located at the same structural level; V-02 defines this boundary cleanly", "Three-column results table (predicted / observed / B-00) structurally enforces effect-size comparison without an explicit prompt, making it the strongest C-12 candidate in eight rounds and a candidate for v9 C-12 elevation from Excellence to Aspirational"]}
```
