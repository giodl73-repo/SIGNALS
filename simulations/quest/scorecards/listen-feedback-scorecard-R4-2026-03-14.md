## listen-feedback R4 Scorecard — Summary

**Top score: 135/135 (V-05)**

| Rank | Variation | Score | Key axis |
|------|-----------|-------|----------|
| 1 | V-05 Combined ceiling | **135** | Both A-08+A-09 fixes in phase structure |
| 2 | V-03 A-09 fix only | **130** | `Current approach:` before NPS; no dominant Detractor field |
| 2 | V-04 A-08 fix only | **130** | Dominant Detractor field in Phase 1; NPS still in header |
| 4 | V-02 Non-phased A-08+A-09 | **120** | Lightweight ceiling; no A-02/A-04/A-05 |
| 5 | V-01 Non-phased A-08 only | **115** | No `Current approach:` field |

**All predictions matched.** V-04 settled the A-09 ambiguity: **strict reading applies** — `Current approach:` must precede NPS, not just feedback items.

**Two new R4 patterns confirmed:**

1. **`dominant-detractor-objection-labeled-field-in-aggregate`** — Phase 1 aggregate gets a `Dominant Detractor objection:` labeled field naming the specific inertia concern pattern (not a prose paragraph). Extended to the Phase 1 gate: Phase 2 blocked until the field is populated.

2. **`current-approach-before-nps-card-field-ordering`** — Card header contains id/name/role only (no scored data). Card body fields: `Current approach:` → `NPS:` → feedback. Keeps NPS out of the header line entirely, making A-09 structurally guaranteed regardless of model tendency to front-load scores.

Written to `simulations/quest/scorecards/listen-feedback-scorecard-R4-2026-03-14.md`.

```json
{"top_score": 135, "all_essential_pass": true, "new_patterns": ["dominant-detractor-objection-labeled-field-in-aggregate", "current-approach-before-nps-card-field-ordering"]}
```
(130): +5, exactly A-09. This confirms that card field ordering was the only A-09 blocker in V-05 R3.

**V-04 confirms A-08 is the sole gap in V-05 R3.** V-04 is V-05 R3 with one change: `Dominant Detractor objection:` labeled field added to Phase 1 aggregate. Score: 130. Gap: +5, exactly A-08. The labeled field forces a specific pattern name rather than a prose paragraph — structurally consistent with A-09's field format in the card body.

**V-01 vs. V-02 confirms A-08+A-09 are additive in lightweight format.** V-01 (A-08 only) = 115; V-02 (A-08+A-09) = 120. No interference between the two new structural fields. The `Current approach:` labeled field in cards makes the `Dominant Detractor objection:` in the aggregate more specific — each persona's current behavior is named explicitly, giving the aggregate section concrete inertia data to synthesize.

**Non-phased ceiling confirmed at 120.** V-02 achieves 120 without phase structure. A-02 (sensitivity analysis), A-04 (ascending NPS order), and A-05 (two-pass revision recs) require Phase 1 pre-scoring and Phase 3 bundled collection — structurally inaccessible in lightweight format. The four-phase structure adds 15 points above the lightweight ceiling.

---

### A-08 scoring

**Pass condition:** All 12 NPS scores carry a band label; aggregate section includes Detractor/Passive/Promoter counts; band definitions encode inertia framing; aggregate names dominant Detractor objection as a specific pattern.

- **V-01**: NPS band definitions encode inertia framing. CATEGORY SUMMARY has counts + `Dominant Detractor objection:` labeled field with specific-pattern instruction. Per-card band label via template. **PASS.**
- **V-02**: Same band definitions + per-card band label + `Dominant Detractor objection:` in CATEGORY SUMMARY with instruction to draw on `Current approach:` fields. **PASS.**
- **V-03**: Band definitions at top encode inertia framing. Phase 1 has category breakdown with counts. Per-card band label in Phase 2. **No `Dominant Detractor objection:` field in Phase 1 aggregate** — Phase 1 ends at counts and threshold. **FAIL.**
- **V-04**: Phase 1 aggregate has counts + `Dominant Detractor objection:` labeled field ("one phrase naming the specific switching-cost or inertia concern... Not a restatement of the band definition"). **PASS.**
- **V-05**: Phase 1 aggregate has counts + `Dominant Detractor objection:` labeled field with instruction to draw on Phase 1 rationale sentences. Band definitions at top with inertia framing. Per-card band label in Phase 2. **PASS.**

---

### A-09 scoring

**Pass condition (strict reading):** `Current approach:` labeled field must appear before NPS score and before feedback items within the card. Card header (id/name/role) may precede it; requirement is that `Current approach:` is the first card body field.

- **V-01**: No `Current approach:` field. NPS is first card field. **FAIL.**
- **V-02**: Card template: header → `Current approach:` → `NPS:` → feedback. `Current approach:` explicitly before NPS. **PASS.**
- **V-03**: Phase 2 card template: header → `Current approach:` → `NPS:` → feedback. `Current approach:` before NPS. **PASS.**
- **V-04**: Phase 2 card template: `[C-NN] [Name] ([Role]) | NPS: [score]` → `Current approach:` → feedback. NPS is in the header line before `Current approach:`. Strict reading: **FAIL.**
- **V-05**: Phase 2 card template: header only (`[C-NN] [Name] ([Role])`) → `Current approach:` → `NPS:` → feedback. Card header contains no scored data; `Current approach:` is first labeled card field, before `NPS:`. **PASS — unambiguous.**

---

### Full Scoring Table

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01 All 12 personas | 12 | PASS | PASS | PASS | PASS | PASS |
| C-02 Severity tags | 12 | PASS | PASS | PASS | PASS | PASS |
| C-03 NPS + justification | 12 | PASS | PASS | PASS | PASS | PASS |
| C-04 Aggregate NPS + threshold | 12 | PASS | PASS | PASS | PASS | PASS |
| C-05 Theme matrix | 12 | PASS | PASS | PASS | PASS | PASS |
| R-01 Blocking escalated | 10 | PASS | PASS | PASS | PASS | PASS |
| R-02 PM + UX reads | 10 | PASS | PASS | PASS | PASS | PASS |
| R-03 Theme matrix severity | 10 | PASS | PASS | PASS | PASS | PASS |
| A-01 Revision recs NPS < 6 | 5 | PASS | PASS | PASS | PASS | PASS |
| A-02 NPS sensitivity | 5 | FAIL | FAIL | PASS | PASS | PASS |
| A-03 Inline [BLOCKING] | 5 | PASS | PASS | PASS | PASS | PASS |
| A-04 Ascending NPS order | 5 | FAIL | FAIL | PASS | PASS | PASS |
| A-05 Two-pass recs | 5 | FAIL | FAIL | PASS | PASS | PASS |
| A-06 Inertia baseline NPS | 5 | PASS | PASS | PASS | PASS | PASS |
| A-07 Severity-first within card | 5 | PASS | PASS | PASS | PASS | PASS |
| A-08 Category bands + dominant | 5 | PASS | PASS | FAIL | PASS | PASS |
| A-09 `Current approach:` before NPS | 5 | FAIL | PASS | PASS | FAIL | PASS |
| **Score** | | **115** | **120** | **130** | **130** | **135** |

---

### Ranking

| Rank | Variation | Score | Key finding |
|------|-----------|-------|-------------|
| 1 | V-05 | 135 | First 135/135; both new R4 patterns confirmed; NPS-in-header-only enables unambiguous A-09 |
| 2 | V-03 | 130 | A-09 fix confirmed; A-08 absent — dominant Detractor field is the sole remaining gap |
| 2 | V-04 | 130 | A-08 fix confirmed; A-09 fails strict reading — NPS-in-header is the sole remaining gap |
| 4 | V-02 | 120 | Non-phased ceiling; A-08+A-09 additive (+10 over V-01); A-02/A-04/A-05 inaccessible |
| 5 | V-01 | 115 | Non-phased A-08 baseline; no `Current approach:` field |

---

### Excellence Signals (from V-05)

Patterns from V-05 that explain 135 vs. 130 for V-03/V-04:

1. **`current-approach-before-nps-card-field-ordering`** — Separating the card header (id/name/role only) from card body fields (`Current approach:` first, then `NPS:`) makes A-09 compliance structurally guaranteed. Any template that includes NPS in the header line risks placing it before `Current approach:` regardless of what follows in the card body. V-05 eliminates this risk: the header carries no scored data; the card body leads with the inertia baseline before the score.

2. **`dominant-detractor-objection-labeled-field-in-aggregate`** — Adding `Dominant Detractor objection:` as a labeled field (not prose instruction) in the Phase 1 aggregate section forces a specific, named inertia concern pattern. The label+colon format is structurally parallel to `Current approach:` in the card body — same format discipline, complementary scopes (aggregate pattern vs. per-persona behavior). The Phase 1 gate is extended to include the field: "Do not proceed to Phase 2 until all 12 scores, their ascending-order list, the category breakdown, the dominant Detractor objection, and the aggregate result are stated."

3. **Structural consistency between card fields and aggregate field** — Both `Current approach:` (per-card) and `Dominant Detractor objection:` (aggregate) use label+colon format. The aggregate field instruction ("draw on the Phase 1 rationale sentences above to identify the common pattern") makes the synthesis relationship explicit — the aggregate field is the convergence of 12 per-persona inertia comparisons, not a separately invented summary.

4. **Phase 1 gate now includes A-08 field** — V-05 Phase 1 gate blocks Phase 2 until all 12 scores, ascending-order list, category breakdown, dominant Detractor objection, and aggregate result are stated. Any partial Phase 1 (counts without named objection) is blocked from proceeding. A-08 structural completeness enforced at the gate.

---

### Prediction accuracy

| Variation | Predicted | Actual | Match |
|-----------|-----------|--------|-------|
| V-01 | 115 | 115 | Yes |
| V-02 | 120 | 120 | Yes |
| V-03 | 130 | 130 | Yes |
| V-04 | 130 (strict) / 135 (lenient) | 130 | Yes — strict reading confirmed |
| V-05 | 135 | 135 | Yes |

All five predictions matched. Single-axis tests (V-03/V-04) isolated each new criterion independently; V-05 confirmed their conjunction.

---

### New R4 patterns

1. **`dominant-detractor-objection-labeled-field-in-aggregate`** — A labeled `Dominant Detractor objection:` field in the aggregate section names the specific inertia concern pattern driving the most Detractor scores. Field uses label+colon format. Content must be a specific pattern name (e.g., "setup complexity blocks initial adoption") — not a restatement of the Detractor band definition. If no Detractors, field value is "No Detractors." Structurally parallel to `Current approach:` in card body: both are label+colon named fields synthesizing inertia data at different scopes (aggregate vs. per-persona).

2. **`current-approach-before-nps-card-field-ordering`** — The card body begins with `Current approach:` as the first labeled field, before `NPS:`, before feedback items. The card header contains only persona id, name, and role — no scored data. This ordering is structurally guaranteed by template sequence: once the card header is id/name/role-only, the template forces `Current approach:` before any NPS value appears in the card body. Any template that embeds NPS in the card header risks A-09 failure regardless of what fields follow.

---

```json
{"top_score": 135, "all_essential_pass": true, "new_patterns": ["dominant-detractor-objection-labeled-field-in-aggregate", "current-approach-before-nps-card-field-ordering"]}
```
