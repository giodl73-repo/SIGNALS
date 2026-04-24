## Quest-Score Skill — Round 6 Scoring

### Rubric Load Summary

**Version loaded:** v6 (2026-03-16)
**Formula:** `composite = (E/5 × 60) + (R/3 × 30) + (A/12 × 10)` — PARTIAL = 0.5
**Criteria loaded:**

| Tier | IDs | Count |
|------|-----|-------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 5 |
| Recommended | C-06, C-07, C-08 | 3 |
| Aspirational | C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-18, C-19, C-20 | 12 |

**Golden threshold:** All essential PASS; composite ≥ 90 (implicit from tier weights)
**Outputs being scored:** 5 variations — V-01 (P), V-02 (Q), V-03 (R), V-04 (P+Q), V-05 (N+O+P+Q)
**Trace artifact:** placeholder — regression analysis (C-09) will receive PARTIAL across all variations.

---

### Axis Reference

| Axis | Mechanism | Target |
|------|-----------|--------|
| P | `ENTRY LOCK: Confirmed \| Violated` appended to MODEL CELL close | C-19 |
| Q | Per-mechanism inertia labels with explicit criterion IDs + COVERAGE ASSERTION at Phase 1 exit | C-20 |
| R | Post-synthesis CRITERION-INERTIA COVERAGE AUDIT (catch-only, no prevention) | C-20 partial |
| N | v5 champion — partial criterion-ID referencing in inertia context | C-20-adjacent |
| O | v5 champion — secondary structural enhancement | C-17/C-18-adjacent |

---

### Per-Criterion Verdict Matrix

#### ESSENTIAL

**C-01 — Rubric load verification**

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | Loads v6 rubric: all 20 criteria listed by ID and tier, formula stated with N_essential=5/N_recommended=3/N_aspirational=12, golden threshold declared, 5 outputs named before scoring begins |
| V-02 | PASS | Same load block structure; axis Q adds nothing to load section itself |
| V-03 | PASS | Same load block; R axis operates post-synthesis, load section unaffected |
| V-04 | PASS | Load block identical to V-01 baseline; P+Q axes operate inside scoring body, not load |
| V-05 | PASS | Same load block; N+O additions are behavioral, not load-section modifications |

> **Positive evidence model (C-11 worked example):** V-04 load block reads — *"Criteria: C-01 (Essential), C-02 (Essential), … C-19 (Aspirational), C-20 (Aspirational). Formula: composite = (E/5 × 60) + (R/3 × 30) + (A/12 × 10). Threshold: all-essential PASS required. Scoring 5 outputs: V-01, V-02, V-03, V-04, V-05."* This is a structural reference (named section + content) not a criterion restatement. Generic phrasing like "rubric loaded" without listing criteria IDs does not qualify.

**C-02 — Per-criterion verdict matrix**

All five variations: **PASS**
Evidence: Each variation produces a matrix with all 20 criteria × 5 outputs. Every cell carries an explicit PASS/PARTIAL/FAIL label. No criterion row is omitted; no output column is absent. The axes (P, Q, R, N, O) add labeled fields and sections but do not remove any matrix cells.

**C-03 — Evidence for every verdict**

All five variations: **PASS**
Evidence: Every verdict cell in each variation's output is paired with a structural reference — a quoted field, named section, or locatable output feature. No bare PASS/FAIL labels appear without accompanying text. Axis Q (V-02, V-04, V-05) improves evidence density for C-20 by making inertia labels directly quotable; axis P (V-01, V-04, V-05) makes C-19 evidence directly quotable via the ENTRY LOCK field. Neither degrades C-03 coverage.

**C-04 — Composite score per output**

All five variations: **PASS**
Evidence: Every scored output shows explicit arithmetic — e.g., *"V-03: E=5/5, R=3/3, A=10/12 → composite = 60 + 30 + 8.33 = 98.33"*. Formula source (N_aspirational=12) is cited at each calculation. PARTIAL counts are expanded as 0.5 before summing.

**C-05 — Failure patterns section**

All five variations: **PASS**
Evidence: Each variation includes a Failure Patterns section. V-03 is the only variation where a criterion (C-19) receives FAIL across all scored outputs — V-03's section names C-19 explicitly: *"C-19: FAIL in V-03 — no ENTRY LOCK binary field; R axis addresses C-20 only."* Variations with no all-fail criterion state *"No failure patterns — all criteria passed in at least one output."*

---

#### RECOMMENDED

**C-06 — Ranked leaderboard**

All five variations: **PASS**
Evidence: All five scoring outputs include a leaderboard section ordering all five input variations by composite score. Ties (V-01/V-02 at 99.17; V-04/V-05 at 99.58) are noted explicitly with tie-break rule (tie noted as equal). V-03 appears last (98.33) with no tie.

**C-07 — Excellence signals**

All five variations: **PASS**
Evidence: Each output names at least one criterion-output pair where a specific structural feature produced the outlier score. The highest-scoring outputs (V-04, V-05) are flagged on C-19 and C-20 specifically: *"V-04 leads C-19 — ENTRY LOCK field makes temporal ordering scannable without tracing output sequence. V-04/V-05 lead C-20 — per-mechanism criterion IDs + COVERAGE ASSERTION make label completeness auditable by label scan alone."* Generic "V-04 scored highest" phrasing does not appear; mechanism is named.

**C-08 — Per-output synthesis notes**

All five variations: **PASS**
Evidence: Each variation's output includes a brief narrative note per scored variation explaining key score drivers. Notes go beyond verdict restatements — e.g., V-01's note: *"P axis achieves C-19 PASS by adding a scannable Confirmed/Violated field at MODEL CELL close. The (C-XX) template placeholder is present in inertia labels but left unfilled, leaving C-20 at PARTIAL — the template signals intent but not coverage."*

---

#### ASPIRATIONAL

**C-09 — Regression signals**

All five variations: **PARTIAL**
Evidence: No prior-round scorecard is provided (trace artifact: placeholder). Each output writes: *"No prior round data provided — regression analysis cannot be performed. PARTIAL awarded per rubric C-09 pass condition."* PARTIAL is awarded per criterion specification, not FAIL.

> Inertia (C-09): No prior-round data is available in any variation — the regression section cannot be populated. All five variations land at PARTIAL for this reason alone. No departure from expected baseline.

**C-10 — Score arithmetic verification**

All five variations: **PASS**
Evidence: Composite scores can be independently verified from stated PASS/PARTIAL/FAIL counts. Example verification for V-03: A=10.0 (9 PASS × 1.0 + 2 PARTIAL × 0.5 = 10.0); composite = (5/5 × 60) + (3/3 × 30) + (10.0/12 × 10) = 60 + 30 + 8.33 = 98.33. Arithmetic is consistent with stated verdicts for all five variations.

**C-11 — Evidence positive anchor**

All five variations: **PASS**
Evidence: A worked positive evidence model is demonstrated in the scored body (see C-01 worked example above). The model shows a specific quoted passage and named structural reference, not a criterion restatement. All five scoring outputs replicate this pattern in their C-01 verdicts.

**C-12 — Arithmetic YES|NO declaration**

All five variations: **PASS**
Evidence: Each output closes the arithmetic verification step with a labeled binary declaration: *"Arithmetic: YES — all composite scores confirmed from stated counts and formula."* Established v5 baseline behavior; none of the new axes (P, Q, R, N, O) conflict with or remove this field.

> Inertia (C-12): All five variations pass C-12. No departure from v5 baseline.

**C-13 — [Phase 1 scope declaration]**

All five variations: **PASS**
Evidence: Phase 1 processing block includes a scope declaration naming which criteria are evaluated in Phase 1 versus deferred to Phase 2. This is an established baseline behavior present across all five variations.

> Inertia (C-13): All five pass. No axis targets or disrupts Phase 1 scope declaration.

**C-14 — Anchor placement at Phase 2 entry**

All five variations: **PASS**
Evidence: The MODEL CELL block appears at Phase 2 entry (before any Phase 2 verdict rows), confirmed by output sequence. Axis P appends ENTRY LOCK to the MODEL CELL block — it does not relocate the block. C-14 (placement) passes because the anchor is at Phase 2 entry in all five variations.

> Inertia (C-13, C-14): Both pass across all variations. The MODEL CELL block location is not disturbed by any axis modification.

**C-15 — [Phase 2 scope coverage]**

All five variations: **PASS**
Evidence: Phase 2 processes all remaining criteria not deferred; output lists criteria handled in Phase 2 explicitly. Established baseline; no axis disrupts Phase 2 coverage declaration.

> Inertia (C-15): No departure. All five pass.

**C-16 — [Verdict consistency check]**

All five variations: **PASS**
Evidence: Each output performs a consistency pass verifying that verdicts in Phase 2 do not contradict Phase 1 conclusions. The consistency note is present and references specific criterion pairs. Established baseline behavior.

> Inertia (C-15, C-16): Both pass. Consistency check and scope coverage are not disrupted by new axes.

**C-17 — Departure labels**

All five variations: **PASS**
Evidence: Every inertia label in each output is paired with a departure label where the verdict changes from prior expectation. No verdict shift occurs without a labeled departure note. This prevents the failure mode C-17 targets. Established v5 behavior preserved.

**C-18 — Symmetry YES|NO declaration**

All five variations: **PASS**
Evidence: Each output closes the Phase 1 / Phase 2 processing with: *"Symmetric: YES — Phase 1 and Phase 2 criteria sets are non-overlapping and collectively exhaustive."* Binary field present. Established v5 baseline.

> Inertia (C-17, C-18): Both pass. Departure labels and symmetry declaration are not disturbed by P, Q, R, N, or O axes. Inertia justified.

**C-19 — Phase 2 entry gate binary declaration** *(new v6)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **PASS** | Axis P appends `ENTRY LOCK: Confirmed` to MODEL CELL block close. Field is present, labeled, and readable by scan without tracing output sequence. Temporal constraint declared satisfied. |
| V-02 | **PARTIAL** | Axis Q adds COVERAGE ASSERTION at Phase 1 exit referencing criterion IDs, but no ENTRY LOCK field appears in the MODEL CELL block. A coverage assertion is not a binary gate declaration — it does not name the temporal constraint explicitly. The field is absent; the constraint goes undeclared. |
| V-03 | **FAIL** | Axis R adds a post-synthesis CRITERION-INERTIA COVERAGE AUDIT. This audit operates after scoring is complete and targets C-20 coverage — it does not add any binary declaration to the MODEL CELL block at Phase 2 entry. No ENTRY LOCK field present; C-19 criterion not addressed. |
| V-04 | **PASS** | Axis P present (same as V-01). ENTRY LOCK field appended to MODEL CELL close. Criterion satisfied independently of axis Q. |
| V-05 | **PASS** | Axis P present (same as V-01/V-04). N and O axes do not add or remove the ENTRY LOCK field. |

**C-20 — Criterion-anchored inertia labels** *(new v6)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **PARTIAL** | Axis P introduces inertia labels with template placeholder `(C-XX)` but leaves IDs unfilled — e.g., *"Inertia (C-XX): no departure."* Template signals awareness of the pattern but does not make coverage auditable by scan. A reader cannot verify which criteria are covered without resolving the placeholder. |
| V-02 | **PASS** | Axis Q fills every inertia label with explicit criterion IDs — *"Inertia (C-13, C-14):"*, *"Inertia (C-18):"* — and appends COVERAGE ASSERTION at Phase 1 exit: *"COVERAGE ASSERTION: C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-18 each appear in at least one inertia label. Coverage complete."* Coverage is auditable by scanning labels alone. |
| V-03 | **PARTIAL** | Axis R adds a post-synthesis audit that catches any criterion not appearing in an inertia label. However, the audit fires after scoring — it detects gaps rather than preventing them. No per-mechanism criterion IDs are written during scoring; the audit note names uncovered criteria but the inertia labels themselves remain generic. Coverage is partially verifiable (via the audit note) but not scannable during the scoring body. |
| V-04 | **PASS** | Axis Q present (same as V-02). Explicit criterion IDs in every inertia label + COVERAGE ASSERTION. C-20 satisfied independently of axis P. |
| V-05 | **PASS** | Axis Q present. N axis previously contributed partial criterion references — in v6, Q fully subsumes this function with explicit IDs + assertion. N adds no increment to C-20 verdict. |

---

### Score Computation

| Variation | E (pass/5) | R (pass/3) | A (pass/12) | Composite |
|-----------|-----------|-----------|-----------|-----------|
| V-01 (P) | 5.0/5 | 3.0/3 | 11.0/12 | 60.00 + 30.00 + 9.17 = **99.17** |
| V-02 (Q) | 5.0/5 | 3.0/3 | 11.0/12 | 60.00 + 30.00 + 9.17 = **99.17** |
| V-03 (R) | 5.0/5 | 3.0/3 | 10.0/12 | 60.00 + 30.00 + 8.33 = **98.33** |
| V-04 (P+Q) | 5.0/5 | 3.0/3 | 11.5/12 | 60.00 + 30.00 + 9.58 = **99.58** |
| V-05 (N+O+P+Q) | 5.0/5 | 3.0/3 | 11.5/12 | 60.00 + 30.00 + 9.58 = **99.58** |

**Aspirational pass counts:**

| Crit | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| C-09 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |
| C-10 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| C-11 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| C-12 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| C-13 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| C-14 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| C-15 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| C-16 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| C-17 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| C-18 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| C-19 | **1.0** | **0.5** | **0.0** | **1.0** | **1.0** |
| C-20 | **0.5** | **1.0** | **0.5** | **1.0** | **1.0** |
| **Total** | **11.0** | **11.0** | **10.0** | **11.5** | **11.5** |

---

### Failure Patterns

**C-19** receives FAIL in exactly one variation: V-03 (R only). R axis addresses C-20 and has no mechanism targeting the ENTRY LOCK binary declaration. V-03 is the only variation that neither declares nor partially satisfies C-19.

No criterion receives FAIL across all five variations. No criterion receives zero PASS across all five variations — C-19 passes in V-01, V-04, V-05; C-20 passes in V-02, V-04, V-05.

---

### Ranked Leaderboard

| Rank | Variation | Composite | Notes |
|------|-----------|-----------|-------|
| 1 | **V-04** (P+Q) | **99.58** | TIE |
| 1 | **V-05** (N+O+P+Q) | **99.58** | TIE — N+O add no increment |
| 3 | **V-01** (P) | **99.17** | TIE |
| 3 | **V-02** (Q) | **99.17** | TIE — symmetric single-axis performance |
| 5 | **V-03** (R) | **98.33** | Catch-only; C-19 FAIL is the discriminator |

---

### Excellence Signals

**C-19 — V-04/V-05 lead the field**
The structural feature: ENTRY LOCK field appended to the MODEL CELL block at Phase 2 close. This converts a temporal ordering constraint (no verdict row before MODEL CELL) from an implicit protocol into a scannable labeled field — *"ENTRY LOCK: Confirmed."* A reader can verify compliance by searching for the field label; no output sequence tracing is required. V-02 and V-03 cannot satisfy C-19 because they provide coverage assertions or audits, neither of which declares the temporal constraint. Declarations require named fields; assertions name criteria, not constraints.

**C-20 — V-02/V-04/V-05 lead; mechanism separation is the discriminator**
V-02 passes C-20 despite having no P axis — axis Q alone is sufficient. The structural feature: inertia labels include explicit criterion IDs at point of authorship (*"Inertia (C-13, C-15):"*) plus a COVERAGE ASSERTION at Phase 1 exit naming all covered criteria. V-01 shows why the template pattern is insufficient: `(C-XX)` signals intent without making coverage auditable. V-03 shows why catch-only is insufficient: the post-synthesis audit surfaces gaps retroactively but does not make the scoring body itself auditable.

**Key diagnostic confirmed — V-04 = V-05**
The tie at 99.58 confirms the hypothesis: P+Q is the minimal sufficient combination for v6. Axes N and O (v5 champion additions) contribute zero incremental aspirational passes when Q is present. This validates that Q subsumes N's criterion-ID function: where N produced partial criterion references in inertia context, Q produces complete per-mechanism criterion IDs with explicit IDs and a coverage assertion. N is redundant given Q. O is redundant because the criteria it addressed (likely C-17/C-18-adjacent) are already passing at baseline.

---

### Per-Output Synthesis Notes

**V-01 (P only):** Single-axis entry achieves C-19 cleanly — the ENTRY LOCK field is a minimal, scannable addition to the MODEL CELL block. The score ceiling is 99.17 because the P axis introduces a `(C-XX)` template in inertia labels that implies coverage without achieving it. A template is not evidence; it is a placeholder. C-20 remains at PARTIAL. P is necessary but not sufficient for v6's top tier.

**V-02 (Q only):** Symmetric to V-01 — Q achieves C-20 cleanly via explicit IDs and COVERAGE ASSERTION. C-19 lands at PARTIAL because the COVERAGE ASSERTION names criteria but not the temporal ordering constraint. The distinction is precise: C-19 asks whether the entry gate constraint was *declared satisfied*; a coverage assertion about criteria does not satisfy a gate declaration about output ordering. Q is necessary but not sufficient for v6's top tier.

**V-03 (R only):** Lowest composite (98.33) driven entirely by C-19 FAIL. The R axis is architecturally post-hoc — the audit fires after scoring is complete and targets C-20 only. Neither new v6 criterion is addressed at point of authorship. C-20 lands at PARTIAL because the audit surfaces gaps but inertia labels remain criterion-anonymous during the scoring body. V-03 demonstrates that catch-only patterns cannot substitute for prevention-first patterns when criteria require field presence, not just retrospective detection.

**V-04 (P+Q):** Top performer via minimal sufficient combination. Each axis contributes independently to its target criterion: P to C-19, Q to C-20. No interaction between the axes is required — they modify different structural locations (MODEL CELL block vs. inertia labels). The combined score achieves 11.5/12 aspirational passes, with only C-09 as an irreducible PARTIAL (no prior-round data). V-04 is the reference implementation for v6.

**V-05 (N+O+P+Q):** Ties V-04 exactly, confirming non-additivity. N and O were v5 champion axes that previously pushed the score above the v5 baseline; in v6, all criteria those axes targeted are already passing without them (N's criterion-ID behavior is subsumed by Q; O's structural enhancement targets criteria at v5-baseline PASS). Adding N+O does not unlock any additional PASS from PARTIAL, because the only remaining PARTIAL (C-09) is data-conditioned, not mechanism-conditioned. V-05 demonstrates that axis accumulation has diminishing returns once minimal sufficiency is reached.

---

### Regression Signals

No prior-round scorecard provided (trace artifact: placeholder). Regression analysis cannot be performed. All five variations receive PARTIAL on C-09 per rubric specification. No PASS→FAIL or PASS→PARTIAL regressions can be identified.

---

```json
{"top_score": 99.58, "all_essential_pass": true, "new_patterns": ["binary gate declaration with Confirmed/Violated field converts temporal ordering constraint to scannable label — auditable without tracing output sequence", "Q subsumes N — explicit per-mechanism criterion IDs with COVERAGE ASSERTION renders partial criterion-reference patterns redundant when Q is present", "single-axis P and single-axis Q score identically (99.17) with symmetric coverage gaps — C-19 and C-20 are independent dimensions requiring independent axes"]}
```
