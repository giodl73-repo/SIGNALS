Scorecard written to `simulations/quest/scorecards/scout-market-scorecard-R1-2026-03-14.md`.

---

## Results

**Top score: 95** (V-03 and V-05 tied)
**All essential pass: true** (all 5 variations, 5/5)
**Golden: true**

**Ranking:**

| Rank | Variation | Score |
|------|-----------|-------|
| 1 (tie) | V-03: Inertia framing | 95 |
| 1 (tie) | V-05: Full synthesis | 95 |
| 3 (tie) | V-01, V-02, V-04 | 90 |

**What separated the 95s:** STATUS QUO section + mandatory inertia anchor column. That's the structural path to C-09 — without it, the high-WTP-killed-by-GTM flip depends on model discretion. All three 90-point variations prompt the comparison but don't scaffold it.

**Key finding vs. prediction:** The predicted ceiling (V-05) confirmed, but the surprise is V-03 ties it at the same score. Inertia framing alone achieves what the full synthesis achieves — per-segment cards and Strategy-first ordering add structural reliability for C-03, not additional criteria coverage.

**Persistent gap:** C-10 fails in all five variations. No template includes a revenue model field. The ground truth trace produced revenue models naturally (the PM surfaced them in Phase 2), but none of the skill prompts elicit them. This is the single addition needed for Round 2 to reach 100.

```json
{"top_score": 95, "all_essential_pass": true, "new_patterns": ["STATUS QUO inertia section alone achieves the same C-09 score as the full synthesis -- it is the single highest-value variation axis", "All 5 variations pass all 5 essentials -- explicit column labels and arithmetic instructions are sufficient for essential coverage; structural enforcement raises reliability not criteria count", "C-10 is absent from all variations -- no template includes a revenue model field, creating a consistent aspirational gap that only an explicit field can close"]}
```
5 x 60) + (3/3 x 30) + (0/2 x 10) = 90 -- Exemplary**

---

### V-02: Per-segment scoring ledger

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Segment IDs | PASS | Segment count declared; card headers S1/S2/S3; COMPOSITE RANKING table mirrors IDs |
| C-02 | TAM/SAM/SOM table | PASS | TAM/SAM/SOM fields pre-printed per card |
| C-03 | 3-dimension fit scoring | PASS | Pain/WTP/Accessibility are pre-printed fields in each card; arithmetic formula pre-printed: `([pain] + [WTP] + [accessibility]) / 3`; no column-drop omission path |
| C-04 | Composite rank formula | PASS | Rank score field pre-printed per card: `[fit score] + (10 - [GTM difficulty]) = [total]`; values copied to COMPOSITE RANKING table |
| C-05 | Beachhead + rationale | PASS | BEACHHEAD RECOMMENDATION has pre-printed `Highest-WTP segment:` + `Deferred because:` fields; rationale must address fit and GTM |
| C-06 | Unit consistency | PASS | Unit declared per card at point of declaration ("tooling use devs; platform/enterprise use $") |
| C-07 | Sequencing path | PASS | SEQUENCING PATH section with Y1/Y2+/Defer structure |
| C-08 | At least one amendment | PASS | AMENDMENTS section |
| C-09 | Non-obvious insight | PARTIAL | WTP score visible per card; BEACHHEAD contrast is a direct lookup -- but no inertia framing; GTM-difficulty flip not structurally scaffolded |
| C-10 | Revenue model per segment | FAIL | No revenue model field in cards or template |

**essential_pass = 5 | recommended_pass = 3 | aspirational_pass = 0**
**Composite = 60 + 30 + 0 = 90 -- Exemplary**

---

### V-03: Inertia framing (STATUS QUO first)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Segment IDs | PASS | Segment ID column in table |
| C-02 | TAM/SAM/SOM table | PASS | TAM/SAM/SOM section, one row per segment |
| C-03 | 3-dimension fit scoring | PASS | FIT SCORING table with Pain/WTP/Accessibility; pain anchored to STATUS QUO do-nothing cost; WTP anchored to switching trigger; "All three columns required. Composite = arithmetic mean." |
| C-04 | Composite rank formula | PASS | COMPOSITE RANK table with full arithmetic pre-printed |
| C-05 | Beachhead + rationale | PASS | Pre-printed highest-WTP field + "Deferred because: [reference inertia anchor or GTM difficulty]" + dedicated "Inertia note:" field |
| C-06 | Unit consistency | PASS | "Do not mix units within the same column" instruction; Unit Type column |
| C-07 | Sequencing path | PASS | SEQUENCING PATH with inertia-anchored Y1/Y2+/Defer |
| C-08 | At least one amendment | PASS | AMENDMENTS section |
| C-09 | Non-obvious insight | PASS | STATUS QUO section names do-nothing cost before any scoring; GTM table has mandatory "Inertia anchor" column; segments with high WTP but strong inertia anchors structurally receive high GTM difficulty, producing rank reversal; BEACHHEAD "Inertia note:" forces the insight to be stated explicitly |
| C-10 | Revenue model per segment | FAIL | No revenue model column |

**essential_pass = 5 | recommended_pass = 3 | aspirational_pass = 1**
**Composite = 60 + 30 + 5 = 95 -- Exemplary**

---

### V-04: Strategy-first + per-segment cards

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Segment IDs | PASS | Segment table + card headers |
| C-02 | TAM/SAM/SOM table | PASS | Strategy-first TAM/SAM/SOM section completes before scoring cards ("This section must complete before scoring cards begin") |
| C-03 | 3-dimension fit scoring | PASS | PM fields pre-printed per card: Pain/WTP/Accessibility + fit score formula; no omission path |
| C-04 | Composite rank formula | PASS | Rank score pre-printed per card; COMPOSITE RANK table copies from cards |
| C-05 | Beachhead + rationale | PASS | PM: BEACHHEAD RECOMMENDATION with pre-printed "Highest-WTP segment:" + "Deferred because:" |
| C-06 | Unit consistency | PASS | Unit Type column in segment table; "Do not mix units" instruction |
| C-07 | Sequencing path | PASS | GTM: SEQUENCING PATH section |
| C-08 | At least one amendment | PASS | AMENDMENTS section |
| C-09 | Non-obvious insight | PARTIAL | Per-segment cards make WTP visible per card; BEACHHEAD prompts highest-WTP comparison -- no STATUS QUO, no inertia anchor column; flip depends on model |
| C-10 | Revenue model per segment | FAIL | No revenue model field |

**essential_pass = 5 | recommended_pass = 3 | aspirational_pass = 0**
**Composite = 60 + 30 + 0 = 90 -- Exemplary**

---

### V-05: Full synthesis (all axes)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Segment IDs | PASS | Segment table with IDs; cards S1/S2/S3+ |
| C-02 | TAM/SAM/SOM table | PASS | TAM/SAM/SOM table required to complete before cards begin |
| C-03 | 3-dimension fit scoring | PASS | PM fields pre-printed per card: Pain/WTP/Accessibility + fit score formula; STATUS QUO references for pain and WTP anchoring; no omission path |
| C-04 | Composite rank formula | PASS | Rank score pre-printed per card: `[fit] + (10 - [gtm]) = [total]`; COMPOSITE RANK table copies from cards |
| C-05 | Beachhead + rationale | PASS | Pre-printed fit/GTM/rank score header fields; "Highest-WTP segment:"; "Not building this means:" pre-printed line requiring STATUS QUO reference; 4-point rationale structure |
| C-06 | Unit consistency | PASS | Strongest enforcement across all variations: "UNIT RULE" at declaration with "Carry this unit through all cards and tables -- do not change mid-table" |
| C-07 | Sequencing path | PASS | GTM: SEQUENCING PATH with inertia-aware Y1/Y2+/Defer |
| C-08 | At least one amendment | PASS | AMENDMENTS section |
| C-09 | Non-obvious insight | PASS | Three structural surfaces: STATUS QUO section before segmentation + per-card GTM field requires naming inertia anchor ("Do not leave blank") + "Not building this means:" at BEACHHEAD ties back to STATUS QUO do-nothing cost |
| C-10 | Revenue model per segment | FAIL | No revenue model field in any card or table |

**essential_pass = 5 | recommended_pass = 3 | aspirational_pass = 1**
**Composite = 60 + 30 + 5 = 95 -- Exemplary**

---

## Summary Rankings

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Label |
|------|-----------|-----------|-------------|--------------|-----------|-------|
| 1 (tie) | V-03: Inertia framing | 5/5 | 3/3 | 1/2 | **95** | Exemplary |
| 1 (tie) | V-05: Full synthesis | 5/5 | 3/3 | 1/2 | **95** | Exemplary |
| 3 (tie) | V-01: Strategy-first | 5/5 | 3/3 | 0/2 | **90** | Exemplary |
| 3 (tie) | V-02: Per-segment ledger | 5/5 | 3/3 | 0/2 | **90** | Exemplary |
| 3 (tie) | V-04: Strategy-first + ledger | 5/5 | 3/3 | 0/2 | **90** | Exemplary |

---

## Excellence Signals (from V-03 and V-05)

**What made the 95-point variations better:**

1. **STATUS QUO section creates the condition for C-09 structurally.** Naming the do-nothing competitor before any scoring forces pain and WTP to be grounded in observable behavior. Once inertia is named at the top, GTM difficulty scores naturally flow from it -- which produces the rank reversal without relying on model discretion.

2. **Inertia anchor as a required column/field.** V-03's "Inertia anchor" column in the GTM table and V-05's mandatory per-card GTM inertia field convert C-09 from an optional insight into a structural output. High-WTP segments with strong inertia anchors mechanically receive high GTM difficulty, reversing their rank.

3. **BEACHHEAD doubles as a C-09 surface.** V-05's "Not building this means:" pre-printed line forces the STATUS QUO cost to resurface at the decision point -- the insight is restated where it matters most.

**What V-05 adds over V-03 (without changing the score):**

- Per-segment cards eliminate the C-03 column-drop omission path that V-03's consolidated table leaves open -- V-05 is more structurally reliable at the same score.
- "UNIT RULE" at declaration is the strongest C-06 enforcement language across all variations.
- Three inertia surfaces (STATUS QUO -> card GTM field -> BEACHHEAD) vs. V-03's two (STATUS QUO -> GTM table column + inertia note).

**Persistent gap across all variations -- C-10:**

No variation includes a revenue model field. The ground truth trace produced a revenue model column in its TAM table (free/freemium/seat/enterprise with concrete ARR target). None of the five templates provide a field or instruction to elicit per-segment revenue model. This is the single highest-leverage addition for Round 2.

---

## New Patterns

1. **STATUS QUO inertia section is the single highest-value variation axis.** It alone achieves the same C-09 score as the full synthesis -- adding per-segment cards and Strategy-first ordering does not increase criteria coverage beyond what V-03 achieves.

2. **All 5 variations pass all 5 essentials.** Even V-01's consolidated table with instruction-based enforcement is sufficient. Explicit column labels and arithmetic instructions are enough for essential coverage; structural enforcement (per-segment cards) raises reliability not criteria count.

3. **C-10 is absent from all variations.** No template includes a revenue model field, creating a consistent aspirational gap. The only way to close it is an explicit per-segment field -- the ground truth trace produced revenue models because Phase 2 naturally surfaced them, not because the spec prompted them.

---

## Round 2 Recommendation

**V-golden candidate: V-05 + revenue model field.**

Add one field per segment card:
```
Revenue model: [free / freemium / seat license / enterprise / other]
Price point or ARR target (if known): [$ or defer]
```

This closes C-10 and, if V-05 is confirmed structurally reliable in live runs, reaches 100.

**Open question for R2:** Does V-05's triple inertia surface produce measurably better C-09 outputs in live runs vs. V-03's single GTM column? If not, V-03 + revenue model field is the simpler path to 100.
