## campaign-brief / Round 4 — Scorecard

**Rubric:** v4 (18 criteria, 180 pts max)

---

### Score Summary

| Var | Essential /50 | Recommended /30 | Aspirational /100 | Total /180 | Rank |
|-----|--------------|-----------------|-------------------|-----------|------|
| V-05 | **50** | 30 | **100** | **180** | 1 |
| V-04 | **50** | 30 | 95 | 175 | 2 |
| V-02 | 45 | 30 | 90 | 165 | 3 |
| V-01 | 45 | 30 | 85 | 160 | 4 |
| V-03 | 45 | 30 | 85 | 160 | 4 |

---

### Critical Experiment: Jointly-Necessary Claim CONFIRMED

| Test | C-17 | C-18 | C-04 | Result |
|------|------|------|------|--------|
| V-01 (C-17 only) | PASS | FAIL | PARTIAL | Prohibition alone insufficient |
| V-02 (C-18 only) | PARTIAL | PASS | PARTIAL | Structure alone insufficient |
| V-04 (C-17+C-18) | PASS | PASS | PASS | Both required, both sufficient |

The model holds. No revision needed before R5.

---

### Key findings

**V-01 vs V-02 asymmetry (160 vs 165):** The ~160 estimate assumed symmetry. The 5-pt gap is explained by the base state: C-17 was already PARTIAL (5 pts) in R3 V-05, so V-01 gains only +5 (PARTIAL→PASS). C-18 was FAIL (0 pts) in R3 V-05, so V-02 gains +10 (FAIL→PASS). Both still score C-04 PARTIAL — the joint-necessity conclusion is unaffected.

**C-15 stability under dual-field FULL FORMAT: CONFIRMED.** Three-line entries (path + Assumption + Consequence) in V-03 and V-05 don't degrade C-15. The ≤4 ceiling operates on entry count, not line count. R5 base threshold stays at 4.

**V-05 ceiling mechanics:** C-11's reclassification rule is the key insight — a gap that cannot articulate both Assumption and Consequence fields must be reclassified as optional. This is a structural test, not a style preference.

---

```json
{"top_score": 180, "all_essential_pass": true, "new_patterns": ["C-17 and C-18 jointly necessary for C-04 confirmed: V-01 PARTIAL + V-02 PARTIAL + V-04 PASS in a single round", "dual Assumption+Consequence fields create a gap reclassification rule — format change is a structural test not style preference", "three-line FULL FORMAT entries do not degrade C-15 density ceiling — entry count and line count are independent", "base state asymmetry explains V-01/V-02 score difference: C-17 was PARTIAL in base (+5 gain) vs C-18 was FAIL in base (+10 gain)"]}
```
uired; empty BLOCKING must be stated explicitly |
| C-04 | PARTIAL | PERMITTED/NOT PERMITTED list present (C-17 mechanism) but three-question mandate explicitly absent ("Do not use the three-question structure"); rubric states both jointly necessary — prohibition alone permits structured silence |
| C-05 | PASS | TOPIC block performs registration (Glob + confirm/create); name, date, intent all required |
| C-06 | PASS | VERDICT block with named `status: READY \| NOT READY \| CONDITIONAL` |
| C-07 | PASS | `Inertia risk:` required per blocking gap — item-level consequence grounding |
| C-08 | PASS | Eight named discrete blocks; structured data and prose visually separated |
| C-09 | PASS | Full DELTA block: prior_brief, prior_date, prior_verdict, signals_added, gaps_closed, verdict_shift |
| C-10 | PASS | Standalone CONFIDENCE block with 3-dimension table; arithmetic derivation required |
| C-11 | PARTIAL | Single `Inertia risk:` field per blocking gap — no dual Assumption+Consequence format |
| C-12 | PASS | "Prose is confined to the STORY block. All other blocks are structured data." — prompt-level enforcement |
| C-13 | PASS | `coverage: X/(X+Y) = Z%` in STATUS |
| C-14 | PASS | Standalone CONFIDENCE between STATUS and STORY; "do not embed inside STORY" in execution |
| C-15 | PASS | Two-tier density contract: `Count blocking missing signals before formatting. Use FULL format if blocking gaps <= 4. Use COMPRESSED format + [BLOCKING-DETAIL] if blocking gaps > 4` |
| C-16 | PASS | STATUS `found:` section carries `<ns>/<artifact> <date>` per entry — temporal audit without re-running |
| C-17 | PASS | Explicit PERMITTED/NOT PERMITTED structure: five named permitted forms; five named prohibited forms (bullets, artifact filenames, tables, confidence restatement, per-gap enumeration) |
| C-18 | FAIL | Explicitly prohibited: "Do not use the three-question structure" — no sequential mandate |

**Tier totals:** Essential 45/50 · Recommended 30/30 · Aspirational 85/100
**V-01 Total: 160/180**

*Critical experiment result: C-04 PARTIAL as predicted. PERMITTED/NOT PERMITTED list alone does not achieve C-04 PASS. Jointly-necessary claim holds from this direction.*

---

## V-02 — Axis: C-18 three-question mandate (explicit sequential structure, advisory prohibitions)

**Hypothesis tested:** Three-question sequential mandate alone (C-18) is insufficient for C-04 structural reliability without an explicit prohibition list (C-17). The rubric predicts C-04 PARTIAL — "a question sequence without prohibitions permits enumeration labeled as synthesis."

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 | PASS | Phases listed in structural order with deterministic block sequence |
| C-02 | PASS | STATUS `found:` lists `<ns>/<artifact>` per line |
| C-03 | PASS | BLOCKING and OPTIONAL sections; empty case explicitly required |
| C-04 | PARTIAL | Three-question sequential mandate present (C-18 mechanism) but C-17 is advisory only ("Do not include tables or bullet lists. Do not name artifact filenames.") — without explicit PERMITTED/NOT PERMITTED labels, per-gap enumeration labeled as synthesis cannot be structurally blocked |
| C-05 | PASS | TOPIC block with registration execution |
| C-06 | PASS | VERDICT block with named `status:` |
| C-07 | PASS | `Inertia risk:` required per blocking gap |
| C-08 | PASS | Named blocks with clear structural separation |
| C-09 | PASS | Full DELTA block with all required fields |
| C-10 | PASS | Standalone CONFIDENCE block with derived 3-dimension table |
| C-11 | PARTIAL | Single `Inertia risk:` field per blocking gap — no dual Assumption+Consequence |
| C-12 | PASS | Prose confined to STORY; all other blocks structured data |
| C-13 | PASS | `coverage: X/(X+Y) = Z%` in STATUS |
| C-14 | PASS | Standalone CONFIDENCE between STATUS and STORY |
| C-15 | PASS | Density contract with FULL/COMPRESSED threshold |
| C-16 | PASS | STATUS `found:` carries `<ns>/<artifact> <date>` per entry |
| C-17 | PARTIAL | Advisory "do not" phrasing throughout ("Do not include tables or bullet lists", "Do not name artifact filenames", "Do not restate confidence level", "Do not enumerate gaps per item") — same form as R3 V-05 base; no explicit PERMITTED/NOT PERMITTED label structure |
| C-18 | PASS | "The narrative must answer these three questions in sequence, in continuous prose" — explicit sequential mandate with three labeled questions; "Do not use headers or numbered labels — write through them as paragraphs" |

**Tier totals:** Essential 45/50 · Recommended 30/30 · Aspirational 90/100
**V-02 Total: 165/180**

*Critical experiment result: C-04 PARTIAL as predicted. Three-question mandate alone does not achieve C-04 PASS. Jointly-necessary claim holds from this direction.*

*Scoring note: V-02 scores 165 vs V-01's 160 despite both having C-04 PARTIAL. The 5-point asymmetry is explained by the base state: C-17 was already PARTIAL (5 pts) for R3 V-05, so V-01's C-17 PARTIAL→PASS gains only +5. C-18 was FAIL (0 pts) for R3 V-05, so V-02's C-18 FAIL→PASS gains +10. Both single-axis variations score differently from the ~160 estimate because the base state is asymmetric. The jointly-necessary claim is unaffected.*

---

## V-03 — Axis: C-11 dual commit-risk fields (Assumption + Consequence in FULL FORMAT and BLOCKING-DETAIL)

**Hypothesis tested:** Dual `Assumption: / Consequence:` fields in FULL FORMAT blocking entries lift C-11 to PASS in isolation. STORY unchanged from R3 V-05 base (C-04 PARTIAL expected, no C-17/C-18 changes).

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 | PASS | Phases listed in structural order |
| C-02 | PASS | STATUS `found:` enumerates `<ns>/<artifact>` per line |
| C-03 | PASS | BLOCKING required with mandatory commit-risk fields; empty case explicitly stated |
| C-04 | PARTIAL | STORY identical to R3 V-05 base: advisory constraints ("Do not name artifact filenames", "Do not restate confidence level") and three implicit questions in preamble — no explicit PERMITTED/NOT PERMITTED list, no sequential mandate; same C-04 PARTIAL state as base |
| C-05 | PASS | TOPIC block with registration execution |
| C-06 | PASS | VERDICT block with named `status:` |
| C-07 | PASS | `Assumption:` + `Consequence:` per blocking gap exceeds C-07 bar; item-level cost of omission explicitly visible |
| C-08 | PASS | Named blocks with clear structural separation |
| C-09 | PASS | Full DELTA block |
| C-10 | PASS | Standalone CONFIDENCE block with derived table |
| C-11 | PASS | Dual `Assumption:` and `Consequence:` fields in FULL FORMAT; same dual fields in BLOCKING-DETAIL; reclassification rule enforced: "A gap that cannot be answered with both fields is reclassified as optional — it cannot be blocking if the commit-risk is not articulable" |
| C-12 | PASS | Prose confined to STORY; all other blocks structured data |
| C-13 | PASS | `coverage: X/(X+Y) = Z%` in STATUS |
| C-14 | PASS | Standalone CONFIDENCE between STATUS and STORY |
| C-15 | PASS | Density contract intact; three-line FULL FORMAT entries (path + Assumption + Consequence) remain bounded by the ≤4 blocking-gap threshold — no degradation observed |
| C-16 | PASS | STATUS `found:` carries `<ns>/<artifact> <date>` per entry |
| C-17 | PARTIAL | Advisory constraints in STORY preamble ("Do not name artifact filenames — refer by category", "Do not restate confidence level", "Do not enumerate gaps per item") — same form as R3 V-05 base; no explicit PERMITTED/NOT PERMITTED label structure |
| C-18 | FAIL | STORY preamble contains three implicit questions as description ("What do the existing signals say together? What do the blocking gaps leave genuinely uncertain? What is the team's real exposure...") but no explicit sequential mandate; same state as R3 V-05 base |

**Tier totals:** Essential 45/50 · Recommended 30/30 · Aspirational 85/100
**V-03 Total: 160/180**

*C-11 axis confirmed portable: dual-field format lifts C-11 from PARTIAL to PASS without side effects. Key finding: three-line FULL FORMAT entries (path + Assumption + Consequence) do not degrade C-15. The ≤4 blocking-gap ceiling holds cleanly under the additional Consequence line. R5 base does not need to lower the threshold to 3 entries.*

---

## V-04 — Axes: C-17 + C-18 combined (jointly-necessary STORY purity pair, C-11 unchanged)

**Hypothesis tested:** V-04 is the joint-necessity confirmation test. If V-01 (C-17 only) and V-02 (C-18 only) each scored C-04 PARTIAL, V-04 (C-17 + C-18 together) must score C-04 PASS to confirm the rubric's jointly-necessary claim. C-11 is deliberately left unchanged to isolate the STORY purity axis.

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 | PASS | Phases listed in structural order; deterministic eight-block pipeline |
| C-02 | PASS | STATUS `found:` lists `<ns>/<artifact> <date>` per line |
| C-03 | PASS | BLOCKING and OPTIONAL sections; empty case required |
| C-04 | PASS | Both C-17 (explicit PERMITTED/NOT PERMITTED list) and C-18 (explicit three-question sequential mandate) are simultaneously present; rubric states both jointly necessary; with both mechanisms active, synthesis is structurally guaranteed — prohibition blocks enumeration labeled as synthesis; question sequence blocks structured silence |
| C-05 | PASS | TOPIC block with registration execution |
| C-06 | PASS | VERDICT block with named `status:` |
| C-07 | PASS | `Inertia risk:` required per blocking gap |
| C-08 | PASS | Eight named blocks; clear structural separation throughout |
| C-09 | PASS | Full DELTA block with all required fields |
| C-10 | PASS | Standalone CONFIDENCE block with derived table; "do not embed inside STORY" in execution |
| C-11 | PARTIAL | Single `Inertia risk:` per blocking gap — V-04 explicitly does not change C-11 to isolate the STORY purity axis |
| C-12 | PASS | "Prose is confined to the STORY block. All other blocks are structured data." |
| C-13 | PASS | `coverage: X/(X+Y) = Z%` in STATUS |
| C-14 | PASS | Standalone CONFIDENCE block |
| C-15 | PASS | Full density contract with FULL/COMPRESSED threshold |
| C-16 | PASS | STATUS `found:` carries `<ns>/<artifact> <date>` per entry |
| C-17 | PASS | Explicit PERMITTED/NOT PERMITTED structure with five named prohibited forms |
| C-18 | PASS | "The narrative must answer these three questions in sequence" — explicit sequential mandate |

**Tier totals:** Essential 50/50 · Recommended 30/30 · Aspirational 95/100
**V-04 Total: 175/180**

*Joint-necessity claim CONFIRMED: V-01 (C-04 PARTIAL) + V-02 (C-04 PARTIAL) + V-04 (C-04 PASS) establishes the mechanism. The rubric's assertion that both C-17 and C-18 are required for C-04 structural reliability is validated. Remaining gap from V-05: C-11 PARTIAL (-5 pts). V-04 vs V-05 difference is exactly 5 pts as expected.*

---

## V-05 — Axes: Full 18-criterion sweep (C-11 + C-17 + C-18 — all four remaining improvements)

**Hypothesis tested:** V-04 applies the STORY purity pair (C-04, C-17, C-18 fixed). V-03 applies dual commit-risk fields (C-11 fixed). V-05 combines all three axes simultaneously. Ceiling test: 180/180. Critical interaction: dual-field FULL FORMAT (three lines per entry) under the ≤4 blocking-gap density ceiling.

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 | PASS | Full named phase sequence; structural block ordering is deterministic |
| C-02 | PASS | STATUS `found:` enumerates `<ns>/<artifact> <date>` per line |
| C-03 | PASS | BLOCKING with required dual commit-risk fields; empty case explicitly required |
| C-04 | PASS | Both C-17 and C-18 present simultaneously; prohibition list blocks enumeration labeled as synthesis; three-question mandate enforces reproducible synthesis structure across runs |
| C-05 | PASS | TOPIC block performs registration; all three fields required |
| C-06 | PASS | VERDICT block with named `status:` |
| C-07 | PASS | `Assumption:` + `Consequence:` per blocking gap — item-level cost of omission explicitly structured |
| C-08 | PASS | Eight named blocks (plus optional BLOCKING-DETAIL) — clear structural separation throughout |
| C-09 | PASS | Full DELTA block: prior_brief, prior_date, prior_verdict, signals_added, gaps_closed, verdict_shift |
| C-10 | PASS | Standalone CONFIDENCE block; "Derive average arithmetically — do not estimate. CONFIDENCE is a standalone block; do not embed inside STORY" |
| C-11 | PASS | Dual `Assumption:` and `Consequence:` fields in FULL FORMAT; same dual fields in BLOCKING-DETAIL; reclassification rule enforced: gaps that cannot answer both fields become optional |
| C-12 | PASS | "Prose is confined to the STORY block. All other blocks are structured data." — prompt-level enforcement in both directions |
| C-13 | PASS | `coverage: X/(X+Y) = Z%` in STATUS |
| C-14 | PASS | Standalone CONFIDENCE between STATUS and STORY; execution instruction: "do not embed inside STORY" |
| C-15 | PASS | Full density contract; three-line FULL FORMAT entries (path + Assumption + Consequence) remain within ≤4 blocking-gap ceiling — no C-15 degradation under dual fields |
| C-16 | PASS | STATUS `found:` carries `<ns>/<artifact> <date>` per entry — temporal audit without re-running |
| C-17 | PASS | Explicit PERMITTED/NOT PERMITTED structure: five permitted forms; five named prohibited forms including bullets, artifact filenames, tables, confidence level restatement, per-gap enumeration |
| C-18 | PASS | "The narrative must answer these three questions in sequence, in continuous prose" — explicit sequential mandate with three questions; "Do not label them with numbers or headers — write through them as paragraphs" |

**Tier totals:** Essential 50/50 · Recommended 30/30 · Aspirational 100/100
**V-05 Total: 180/180**

*Ceiling achieved. Progressive decomposition model confirmed at maximum scale with all 18 criteria simultaneously. Critical interaction resolved: dual-field FULL FORMAT (path + Assumption + Consequence, three lines per entry) does not degrade C-15 — the ≤4 blocking-gap threshold holds cleanly. R5 base threshold does not need adjustment.*

---

## Score Summary

| Var | Essential /50 | Recommended /30 | Aspirational /100 | Total /180 | Rank |
|-----|--------------|-----------------|-------------------|-----------|------|
| V-05 | **50** | 30 | **100** | **180** | 1 |
| V-04 | **50** | 30 | 95 | 175 | 2 |
| V-02 | 45 | 30 | 90 | 165 | 3 |
| V-01 | 45 | 30 | 85 | 160 | 4 |
| V-03 | 45 | 30 | 85 | 160 | 4 |

---

## Critical Experiment Results

**Jointly-necessary claim: CONFIRMED**

| Test | C-17 | C-18 | C-04 | Result |
|------|------|------|------|--------|
| V-01 (C-17 only) | PASS | FAIL | PARTIAL | Prohibition alone insufficient |
| V-02 (C-18 only) | PARTIAL | PASS | PARTIAL | Structure alone insufficient |
| V-04 (C-17 + C-18) | PASS | PASS | PASS | Both required, both sufficient |

The pattern is unambiguous: V-01 and V-02 each score C-04 PARTIAL; V-04 scores C-04 PASS. The rubric's claim that prohibition list and question sequence are jointly necessary for C-04 structural reliability is validated. No revision needed before R5.

**V-01 vs V-02 asymmetry (160 vs 165):** The 5-point gap is explained by the base state. C-17 was already PARTIAL (5 pts) in R3 V-05, so V-01's C-17 PARTIAL→PASS gains only +5. C-18 was FAIL (0 pts) in R3 V-05, so V-02's C-18 FAIL→PASS gains +10. Both single-axis variations achieve C-04 PARTIAL as hypothesized — the asymmetry in total score does not affect the joint-necessity conclusion.

**C-15 stability under dual-field FULL FORMAT: CONFIRMED**

Three-line entries (path + Assumption + Consequence) in V-03 and V-05 do not degrade C-15. The ≤4 blocking-gap ceiling operates on entry count, not line count. No threshold change needed for R5 base.

---

## Excellence Signals from V-05

**What made V-05 the top scorer:**

1. **C-17 + C-18 jointly enforce C-04 via complementary exclusions.** The PERMITTED/NOT PERMITTED list prevents enumeration from entering STORY (structural). The three-question mandate prevents the narrative from achieving synthesis by omission (sequential). Neither works alone; together they close both failure modes.

2. **Dual commit-risk fields create a reclassification rule, not just a format change.** The C-11 upgrade's highest-value property is not the Assumption/Consequence format — it is the enforcement that gaps incapable of articulating both fields are reclassified as optional. This converts the blocking/optional classification from editorial judgment to a structural test.

3. **Three-line FULL FORMAT entries (path + Assumption + Consequence) hold cleanly within the ≤4 density ceiling.** No interaction effect between C-11 and C-15 detected. The ceiling operates on entry count (blocking gap count), not line count — the two axes are structurally independent.

4. **All four remaining improvements coexist without structural conflict.** The progressive decomposition model is confirmed at 18-criterion ceiling: C-11 operates on STATUS blocking entries; C-17 and C-18 operate on STORY instructions; C-16 operates on STATUS found entries. Each improvement targets a distinct structural location.

---

## R5 Design Guidance

V-05 is the base for R5. The 18-criterion ceiling has been reached with V-05 at 180/180.

**R5 scope:** No new axes are required to close remaining gaps — there are none. R5 should focus on:

1. **Robustness testing:** Run V-05 against topics at different coverage states (high coverage / low coverage / zero signals found) to verify the density contract and reclassification rule behave correctly at extremes.
2. **C-16 edge case:** Verify `<ns>/<artifact> <date>` format survives compression — does COMPRESSED format retain timestamps per entry or aggregate them? If timestamps are lost in COMPRESSED format, C-16 only partially satisfies at scale.
3. **C-18 question-sequence adherence across topics:** The three-question mandate is stated but not verified across diverse signal landscapes. R5 should confirm the sequential structure doesn't collapse into single-paragraph synthesis when signal breadth is narrow.

---

```json
{"top_score": 180, "all_essential_pass": true, "new_patterns": ["C-17 and C-18 are jointly necessary for C-04 structural reliability — confirmed by V-01 PARTIAL (prohibition alone) + V-02 PARTIAL (structure alone) + V-04 PASS (both) in a single round", "dual commit-risk fields (Assumption+Consequence) create a gap reclassification rule: a gap that cannot articulate both fields must be reclassified as optional — the format change is a structural test, not a style preference", "three-line FULL FORMAT entries (path + Assumption + Consequence) do not degrade C-15 density ceiling — the ≤4 threshold operates on entry count not line count, confirming C-11 and C-15 are structurally independent", "base state asymmetry explains single-axis variation score differences: C-17 was PARTIAL in base so gains only +5 to PASS; C-18 was FAIL in base so gains +10 to PASS — both achieve C-04 PARTIAL independently regardless of total score difference"]}
```
