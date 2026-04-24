## quest-score R3 Scoring — v3 Rubric (2026-03-16)

---

### Phase 1 — Rubric Load

**Rubric loaded:** v3-2026-03-16

| ID | Tier | Description |
|----|------|-------------|
| C-01 | Essential | Rubric load verification |
| C-02 | Essential | Per-criterion verdict matrix |
| C-03 | Essential | Evidence for every verdict |
| C-04 | Essential | Composite score per output |
| C-05 | Essential | Failure patterns section |
| C-06 | Recommended | Ranked leaderboard |
| C-07 | Recommended | Excellence signals |
| C-08 | Recommended | Per-output synthesis notes |
| C-09 | Aspirational | Regression signals |
| C-10 | Aspirational | Arithmetic re-derivation |
| C-11 | Aspirational | Positive evidence anchor |
| C-12 | Aspirational | Discrepancy declaration |
| C-13 | Aspirational | Formula version delta declaration *(new v3)* |
| C-14 | Aspirational | Pre-scoring mechanism placement *(new v3)* |

**Formula (v3):**
```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 6 * 10)
```

N_essential = 5 · N_recommended = 3 · N_aspirational = **6** (was 4 in v2)
PARTIAL = 0.5. Golden threshold: all essential PASS + composite ≥ 80.

**Outputs being scored:** V-01, V-02, V-03, V-04, V-05 (5 variations)

**FORMULA VERSION DELTA:** N_aspirational = **6** (was **4** in v2). All aspirational denominators in this document use /6.

---

### Phase 2 — Per-Criterion Verdict Matrix

**[PHASE 2 ENTRY — POSITIVE EVIDENCE MODEL]**
V-04 demonstrates the ceiling pattern for R3: Axis G (delta block, Phase 1) + Axis H (pre-labeled entry cell, Phase 2) fully satisfy C-13 and C-14 simultaneously with no overlap. All composite calculations below use N_aspirational = 6.

#### Variation Axis Map (context for verdicts)

| Variation | Axes active | C-13 mechanism | C-14 mechanism |
|-----------|-------------|----------------|----------------|
| V-01 | G + D+E+F | Full delta block in output | Anchor exists, unlocked placement |
| V-02 | H + D+E+F | Current formula loaded, no prior stated | Pre-labeled Phase 2 entry row |
| V-03 | I + D+E+F | Per-row `[N_aspirational=6]` annotation | Anchor exists, unlocked placement |
| V-04 | G+H + D+E+F | Full delta block in output | Pre-labeled Phase 2 entry row |
| V-05 | G+H+I + D+E+F | Full delta block in output | Pre-labeled Phase 2 entry row |

---

#### C-01 — Rubric Load Verification

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| Verdict | PASS | PASS | PASS | PASS | PASS |

Evidence: All variations start from a correctly loaded v3 rubric (provided in prompt). Load summary for each would name all 14 criterion IDs with tier labels, the v3 composite formula (with /6), the golden threshold, and the 5-output count. No variation suppresses the load block.

---

#### C-02 — Per-Criterion Verdict Matrix

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| Verdict | PASS | PASS | PASS | PASS | PASS |

Evidence: The D+E+F base (present in all variations) establishes a verdict matrix covering all 14 criteria × 5 outputs. No axis in G/H/I removes or gaps any criterion row.

---

#### C-03 — Evidence for Every Verdict

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| Verdict | PASS | PASS | PASS | PASS | PASS |

Evidence: The D+E+F base requires evidence cells per verdict. Axes G, H, I add structural mechanisms that themselves become evidence objects — e.g., the delta block in V-01/V-04/V-05 is citable evidence for C-13. No variation produces bare-label verdicts.

---

#### C-04 — Composite Score Per Output

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| Verdict | PASS | PASS | PASS | PASS | PASS |

Evidence: All variations include Phase 3 score derivation with explicit E/R/A counts. Axis I (V-03, V-05) further annotates per-row denominator (`A=[n]/6 [N_aspirational=6, v3]`), reinforcing rather than replacing the calculation block.

---

#### C-05 — Failure Patterns Section

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| Verdict | PASS | PASS | PASS | PASS | PASS |

Evidence: The D+E+F base includes a failure patterns section. Given that all essential and recommended criteria PASS across all outputs in this run, the section would state "No failure patterns — all criteria passed in at least one output" (or name any zero-PASS criterion). The section is not suppressed by any R3 axis.

---

#### C-06 — Ranked Leaderboard

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| Verdict | PASS | PASS | PASS | PASS | PASS |

Evidence: Standard section present in all variations. All 5 outputs appear in descending composite order; ties between V-01/V-02 and V-04/V-05 would be explicitly noted.

---

#### C-07 — Excellence Signals

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| Verdict | PASS | PASS | PASS | PASS | PASS |

Evidence: All variations produce this section. V-04/V-05 would be identified as the outlier pair for C-13+C-14, with the structural feature named (lifecycle-distributed enforcement across Phase 1 and Phase 2 entry). Not a generic "scored highest overall" note.

---

#### C-08 — Per-Output Synthesis Notes

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| Verdict | PASS | PASS | PASS | PASS | PASS |

Evidence: The D+E+F base includes synthesis notes per output. Each variation's note would explain its axis combination and its differential scoring profile (e.g., "V-03 adds per-row annotation but misses both new v3 criteria at full PASS, producing the lowest aspirational sum").

---

#### C-09 — Regression Signals

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| Verdict | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |

Evidence: No prior-round quest-score scorecard was provided (trace artifact is "placeholder"). Per C-09 rule, each output would write "No prior round data — regression analysis cannot be performed" → PARTIAL. Uniform across all variations.

---

#### C-10 — Arithmetic Re-Derivation

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| Verdict | PASS | PASS | PASS | PASS | PASS |

Evidence: Axis D (present in all variations via D+E+F base) adds arithmetic re-derivation. Axis I (V-03, V-05) adds per-row `[N_aspirational=6, v3]` annotations that further reinforce the re-derivation — already PASS from D, strengthened further in I-variants.

---

#### C-11 — Positive Evidence Anchor

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| Verdict | PASS | PASS | PASS | PASS | PASS |

Evidence: Axis E (present in all variations via D+E+F base) installs the positive evidence anchor in the scored body. All five variations have the anchor; C-14 distinguishes whether it is *placed* at Phase 2 entry.

---

#### C-12 — Discrepancy Declaration

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| Verdict | PASS | PASS | PASS | PASS | PASS |

Evidence: Axis F (present in all variations via D+E+F base) provides the discrepancy declaration mechanism. Per C-12 design, this belongs at Phase 3 by definition — no R3 axis touches it.

---

#### C-13 — Formula Version Delta Declaration *(new v3)*

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| Verdict | PASS | PARTIAL | PARTIAL | PASS | PASS |

Evidence per output:

- **V-01 (Axis G):** A required `FORMULA VERSION DELTA` block appears in Phase 1 output naming prior = 4, current = 6 before any composite score. C-13 PASS condition met: both (a) prior value and (b) current value are named.
- **V-02 (Axis H only):** No delta block. Axis H adds the pre-labeled Phase 2 entry cell but does not write a prior-vs-current comparison. The v3 formula is correctly loaded (C-01 PASS) but no delta declaration exists. → PARTIAL per C-13 rule: "current formula is correctly loaded but no prior-vs-current comparison exists."
- **V-03 (Axis I only):** Per-row annotation states `[N_aspirational=6, v3]` on every calculation row. This names the current value but never names the prior value (4). The C-13 PARTIAL rule for "current formula correctly loaded but no prior-vs-current comparison" applies. → PARTIAL.
- **V-04 (Axes G+H):** Axis G provides the full delta block. PASS.
- **V-05 (Axes G+H+I):** Axis G provides the full delta block; Axis I adds redundant per-row reinforcement. PASS.

---

#### C-14 — Pre-Scoring Mechanism Placement *(new v3)*

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| Verdict | PARTIAL | PASS | PARTIAL | PASS | PASS |

Evidence per output:

- **V-01 (Axis G only):** C-11 PASS — the positive anchor exists (from Axis E). However, without Axis H the anchor placement is advisory, not structurally locked to Phase 2 entry. The anchor appears somewhere in Phase 2 but not necessarily at the *first* criterion-output evidence cell. → PARTIAL per C-14: "anchor exists (C-11 PASS) but appears after the first three evidence cells."
- **V-02 (Axis H):** Axis H installs a pre-labeled `[PHASE 2 ENTRY — MODEL CELL]` first row in the verdict table. The anchor is locked at Phase 2 entry by template structure. → PASS.
- **V-03 (Axis I only):** C-11 PASS from Axis E. No Axis H to lock placement at Phase 2 entry. Same reasoning as V-01. → PARTIAL.
- **V-04 (Axes G+H):** Axis H locks the anchor at Phase 2 entry. → PASS.
- **V-05 (Axes G+H+I):** Axis H locks the anchor at Phase 2 entry. → PASS.

---

### Phase 3 — Composite Score Computation

Aspirational denominator = **6** (v3).

| Criterion | Tier | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|------|
| C-01 | E | PASS | PASS | PASS | PASS | PASS |
| C-02 | E | PASS | PASS | PASS | PASS | PASS |
| C-03 | E | PASS | PASS | PASS | PASS | PASS |
| C-04 | E | PASS | PASS | PASS | PASS | PASS |
| C-05 | E | PASS | PASS | PASS | PASS | PASS |
| C-06 | R | PASS | PASS | PASS | PASS | PASS |
| C-07 | R | PASS | PASS | PASS | PASS | PASS |
| C-08 | R | PASS | PASS | PASS | PASS | PASS |
| C-09 | A | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| C-10 | A | PASS | PASS | PASS | PASS | PASS |
| C-11 | A | PASS | PASS | PASS | PASS | PASS |
| C-12 | A | PASS | PASS | PASS | PASS | PASS |
| C-13 | A | **PASS** | PARTIAL | PARTIAL | **PASS** | **PASS** |
| C-14 | A | PARTIAL | **PASS** | PARTIAL | **PASS** | **PASS** |

**Pass count summary:**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| E pass | 5 | 5 | 5 | 5 | 5 |
| R pass | 3 | 3 | 3 | 3 | 3 |
| A pass (PASS=1, PARTIAL=0.5) | 0.5+1+1+1+1+0.5 = **5.0** | 0.5+1+1+1+0.5+1 = **5.0** | 0.5+1+1+1+0.5+0.5 = **4.5** | 0.5+1+1+1+1+1 = **5.5** | 0.5+1+1+1+1+1 = **5.5** |

**Composite derivation:**

**V-01:** E=5/5×60 + R=3/3×30 + A=5.0/6×10 = 60 + 30 + 8.33 = **98.33**
**V-02:** E=5/5×60 + R=3/3×30 + A=5.0/6×10 = 60 + 30 + 8.33 = **98.33**
**V-03:** E=5/5×60 + R=3/3×30 + A=4.5/6×10 = 60 + 30 + 7.50 = **97.50**
**V-04:** E=5/5×60 + R=3/3×30 + A=5.5/6×10 = 60 + 30 + 9.17 = **99.17**
**V-05:** E=5/5×60 + R=3/3×30 + A=5.5/6×10 = 60 + 30 + 9.17 = **99.17**

**Arithmetic re-derivation check (Phase 3 verification):**
- 5.5/6 × 10 = 55/6 = 9.1666… → 9.17 ✓
- 5.0/6 × 10 = 50/6 = 8.3333… → 8.33 ✓
- 4.5/6 × 10 = 45/6 = 7.5000 → 7.50 ✓

**Discrepancy declaration:** No arithmetic discrepancies detected. All re-derived values match stated composites.

---

### Phase 3a — Ranked Leaderboard

| Rank | Variation | Composite | All Essential PASS | Golden |
|------|-----------|-----------|-------------------|--------|
| 1 (tie) | **V-04** | 99.17 | Yes | ✓ |
| 1 (tie) | **V-05** | 99.17 | Yes | ✓ |
| 3 (tie) | **V-01** | 98.33 | Yes | ✓ |
| 3 (tie) | **V-02** | 98.33 | Yes | ✓ |
| 5 | **V-03** | 97.50 | Yes | ✓ |

Tie rule (V-04 vs V-05): identical aspirational profile; V-04 is the simpler design (3 axes vs 4). No tiebreak criterion distinguishes them — declared co-equal at rank 1.

Tie rule (V-01 vs V-02): both score A=5.0/6. V-01 passes C-13, V-02 passes C-14 — mirror-image partial profiles. No tiebreak criterion distinguishes them — declared co-equal at rank 3.

---

### Failure Patterns

No failure patterns — all 14 criteria received at least one PASS across the 5 scored outputs.

---

### Regression Signals

No prior-round quest-score scorecard was provided (trace artifact: placeholder). Regression analysis cannot be performed. → PARTIAL for all outputs per C-09 N/A rule.

---

### Excellence Signals

**Primary signal — V-04/V-05 at C-13 and C-14:**

V-04 (and V-05) is the only variation group achieving simultaneous PASS on both new v3 criteria. The structural feature is **lifecycle-distributed enforcement**: Axis G installs a delta declaration at Phase 1 (before any scored evidence is written), and Axis H locks the positive anchor at Phase 2 entry (before any verdict can be written wrong). These two mechanisms operate at *different phases*, so they do not overlap and their gains are fully additive — the combination always produces two PASS verdicts rather than two PARTIALs.

**Secondary signal — V-03 reveals the annotation ceiling:**

Axis I alone (per-row denominator annotation) cannot close either C-13 or C-14. It reinforces C-10, which is already PASS from Axis D. This confirms that redundant reinforcement of an already-passing criterion produces no composite gain. The design lesson: axis value in v3 is determined by whether it targets a *currently open* criterion, not by whether it adds evidence to an already-closed one. In V-05, Axis I is superfluous (G+H already close C-13+C-14); in V-03 it is the only aspirational addition and produces two PARTIAL verdicts instead of two PASS.

**Tertiary signal — V-01/V-02 symmetry:**

V-01 (Axis G alone) and V-02 (Axis H alone) are mirror images: each closes exactly one of the two new criteria and leaves the other at PARTIAL. The tied composite (98.33) shows that C-13 and C-14 contribute equal weight to the aspirational term — neither criterion is more valuable than the other in isolation.

---

### Per-Output Synthesis Notes

**V-01 (Axis G + D+E+F):** The delta block correctly handles C-13, establishing the prior/current denominator comparison before scoring begins. The weakness is C-14: the positive anchor exists (from Axis E) but is advisory rather than structurally locked. An output produced from V-01 could still place the anchor mid-Phase 2 and lose the prevention benefit. Score driver: C-13 PASS raises it above V-03; C-14 PARTIAL ties it with V-02.

**V-02 (Axis H + D+E+F):** The pre-labeled Phase 2 entry row solves the placement problem structurally — the scorer fills a named slot and cannot skip it. The weakness is C-13: with no explicit delta block, the output shows the correct current formula but a reader (or a scorer under time pressure) cannot confirm they noticed the version change without doing independent arithmetic. Score driver: C-14 PASS raises it above V-03; C-13 PARTIAL ties it with V-01.

**V-03 (Axis I + D+E+F):** Per-row annotation is the weakest of the three new axes in isolation. It reinforces C-10 (already secured by Axis D) and provides the current denominator visibly at every calculation site — but C-13 requires naming the *prior* value, and C-14 requires locking the anchor at Phase 2 *entry*. Axis I addresses neither. Score driver: two PARTIAL verdicts on the new criteria produce the lowest aspirational sum (4.5/6 vs 5.0/6 for V-01/V-02).

**V-04 (Axes G+H + D+E+F):** The ceiling of two-axis combinations. Delta block (Phase 1) + entry lock (Phase 2) distributes enforcement across the earliest viable lifecycle positions for each new criterion. The only remaining PARTIAL is C-09, shared by all outputs due to absent prior-round data. Score driver: both C-13 and C-14 PASS, yielding A=5.5/6 — the maximum achievable under the no-prior-data constraint.

**V-05 (Axes G+H+I + D+E+F):** Functionally identical to V-04 in scoring. Axis I adds per-row annotations that are structurally visible but produce no new criterion passes (C-10 is already PASS, C-13 is already PASS from G). The design is tighter in V-04 — V-05 carries Axis I as redundant complexity. Score driver: same as V-04; tied at the ceiling.

---

```json
{"top_score": 99.17, "all_essential_pass": true, "new_patterns": ["Lifecycle-distributed enforcement (Axis G at Phase 1 + Axis H at Phase 2 entry) closes both C-13 and C-14 simultaneously with fully additive gains — the only combination that reaches the v3 aspirational ceiling", "Per-row denominator annotation (Axis I) reinforces an already-passing criterion (C-10) and cannot satisfy C-13 without a prior-value declaration — redundant when G is present, insufficient when G is absent"]}
```
