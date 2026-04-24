`scout-stakeholders-rubric-v6-2026-03-14.md` written.

**Two new criteria added:**

**C-20 — Inertia chain prefill-stage binding** (depth, 5 pts)
When C-19's prefill table exists, C-18's third position (`displacement-acknowledgment` mandate) must be stated as an explicit rule *within the prefill step*, not deferred to content-population instructions. V-04 passes C-18 with the mandate inline at Step 6; V-05 moves it upstream to Step 6a rule 3 and gates it with FAIL_MISSING_DISPLACEMENT_PREFILL. Not satisfiable if C-19 is absent.

**C-21 — Amendment example prefill round-trip** (correctness, 5 pts)
The correct-form half of the C-16 before/after pair must demonstrate a prefill table update (Step 6a) alongside the content-row update (Step 6b) — not only content rows. V-05: "Step 6a prefill updated — Keep Satisfied Frame Type reassigned from `value-capture` to `compliance-alignment`; Step 6b row revised accordingly." Not satisfiable if C-16 or C-19 is absent.

**Updated totals**: aspirational 55 → 65 pts; max 145 → 155 pts. Golden threshold (>= 80) unchanged. V-05 scores 155/155 under v6; V-04 stays at 140/155 (fails C-19, C-20, C-21).
 C-16 but its amendment example targets grid/veto/comms updates only; no prefill table exists in V-04, so the round-trip cannot be demonstrated. This is structurally distinct from C-16 (which requires a before/after pair) — it constrains what the correct-form example must demonstrate when C-19 is also present.

Both are first-seen in Round 5; neither appeared in prior rounds. Both require C-19 to be present before they can be satisfied, but are independently failible: a variation could have C-18 + C-19 but place the displacement mandate at the content stage (fails C-20), and could have C-16 + C-19 but show an amendment example that only updates 6b rows (fails C-21).

---

# Rubric — scout-stakeholders — v6

**Version**: v6 (updated from R5 excellence signals)
**Skill**: scout:stakeholders
**Date**: 2026-03-14

---

## Design Rationale

### v5 to v6 changes

Two new aspirational criteria (C-20 and C-21) extracted from Round 5. Both were first-seen in Round 5; neither appeared in prior rounds.

- **C-20** — Inertia chain prefill-stage binding: V-05 established that when C-19's prefill table exists, C-18's third position (the displacement-specific Frame Type requirement) must be stated as an explicit rule *within the prefill step*, not as a note during content population. V-04 passes C-18 with a `displacement-acknowledgment` mandate inline at the communications step — the requirement exists but lives at content-entry time. V-05 moves it upstream: Step 6a rule 3 explicitly assigns `displacement-acknowledgment` to the inertia row *before* any rows are populated, and FAIL_MISSING_DISPLACEMENT_PREFILL fires at that gate. All three inertia positions must be present (C-18), the prefill table must exist (C-19), *and* the displacement assignment must be made in the prefill step — not deferred to content entry. Displacement mandate in content instructions only = FAIL.

- **C-21** — Amendment example prefill round-trip: V-05's C-16 correct-form pair extends through both structural levels. The correct-form amendment example must include at least one case where the prefill table (Step 6a) is updated — not only the content rows (Step 6b). V-05 demonstrates: "Step 6a prefill updated — Keep Satisfied Frame Type reassigned from `value-capture` to `compliance-alignment`; Step 6b row revised accordingly." V-04 passes C-16 but its amendment example targets grid/veto/comms updates only; no prefill table exists in V-04, so the round-trip cannot be demonstrated. C-21 is only satisfiable when C-16 and C-19 are both present; a correct-form example that shows only 6b content updates without a corresponding 6a prefill update = FAIL.

Round 5 also confirms five structural properties:
- V-03 at 120 (not 125) confirms C-15 without C-14 loses 5 points — the reversed sequence is independent but requires FAIL labels to reach the 125-tier.
- V-01 and V-02 each at 125 confirm C-18 and C-19 are stable single-axis additions at the same tier as C-17.
- V-04 at 140 confirms C-18 adds cleanly to the proven C-15 + C-16 + C-17 triple with no interference.
- V-05 at 145/145 confirms all five axes (C-15 through C-19) are independent and compatible simultaneously.
- V-05's patterns for C-20 and C-21 do not alter V-05's score under v5 — they are additive axes targeted by v6.

Point totals updated: aspirational rises from 55 to 65 pts; max score rises from 145 to 155 pts. Golden threshold (>= 80) is unchanged.

### v4 to v5 changes (retained for history)

Two new aspirational criteria (C-18 and C-19) extracted from Round 4. Both were first-seen in Round 4; neither appeared in prior rounds.

- **C-18** — Inertia stakeholder structural elevation: V-02 elevated inertia stakeholders across three structural positions simultaneously — a dedicated sub-step in the strategy phase (Step 1b), a required `[INERTIA]` tag in the Power/Interest grid, and a required `displacement-acknowledgment` Frame Type in the comms table. No prior variation treated inertia as a first-class structural element rather than an incidentally-included grid row. All three requirements must be present; partial presence (e.g., displacement note in comms but no grid tag) = FAIL.

- **C-19** — Frame Type prefill constraint: V-03's diagnostic in v4 explicitly flagged this as a v5 candidate: "The prefill pattern targets C-13 in a different way than the rubric currently measures." C-13 measures output — distinct labels present in the completed table. C-19 measures procedural constraint — a standalone prefill table listing accepted Frame Type values appears as a distinct step *before* the comms table is populated, constraining which values are allowed. Enumerating accepted values inline within instructions (V-01, V-02, V-04 pattern) does not satisfy C-19.

### v3 to v4 changes (retained for history)

One new aspirational criterion (C-17) extracted from V-03's Round 3 pattern. The criterion was explicitly flagged in v3 as a v4 candidate pending confirmation; Round 3 confirmed it. C-17 added: 5 pts. Aspirational rose to 45 pts. Max score rose to 135 pts.

### v2 to v3 changes (retained for history)

Two new aspirational criteria (C-15 and C-16) extracted from V-04's Round 2 perfect score. C-15 enforces analysis-before-synthesis structurally (reversed sequence: Strategy → UX → PM). C-16 requires the amendment anti-pattern shown as an adjacent before/after pair, not just a positive rule.

---

## Essential Criteria (60 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **CODEOWNERS fallback** | correctness | Org context check is the first step. Ask one question if absent. "Never infer silently" or equivalent must be present. |
| C-02 | **Power/Interest grid present** | correctness | Grid has 4+ rows with quadrant labels. Power and Interest values or descriptors present for each row. Prose-only stakeholder list with no grid = FAIL. |
| C-03 | **Veto risks ranked by probability** | correctness | Veto risk list is present, ordered by probability rank. Each entry includes probability + impact. Order must reflect probability rank, not alphabetical or grid order. |
| C-04 | **Champion with concrete action** | correctness | One or more stakeholders labelled champion with a specific action (e.g., "give demo slot", "co-present", "early access"). Generic "engage champion" language = FAIL. |
| C-05 | **Communication strategy per quadrant** | depth | Four quadrant rows are present, each with a distinct message and at least a relative timing signal (e.g., "3 weeks before", "now", "day of"). |

**Essential points**: 12 pts each x 5 = **60 pts**

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Conflict identification** | depth | Two or more distinct conflicts named, each identifying the stakeholder groups in tension and the nature of the conflict. Single-stakeholder risks do not count as conflicts. |
| C-07 | **Role framing** | coverage | All three roles (PM / Strategy / UX) structurally separated into distinct sections or steps. Collapsed into one section = FAIL. Named but not separated (partial) = 5 pts. |
| C-08 | **Critical-path gatekeepers flagged** | correctness | One or more gatekeepers tagged critical-path with a deadline or lead-time note. Generic "important" label without timing = FAIL. |

**Recommended points**: 10 pts each x 3 = **30 pts**

---

## Aspirational Criteria (65 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Amendment phase** | depth | One or more distinct findings not in the initial grid -- adds, splits, or reframes a stakeholder. Absent amendment section = FAIL. |
| C-10 | **"What we are NOT doing" framing** | coverage | One or more sentences or rows describing what the product does not do for a gatekeeper. Generic "out of scope" = FAIL. |
| C-11 | **Source-tracking column in grid** | depth | Grid has a Source column or per-row origin label. Each row has an origin (e.g., "CODEOWNERS", "initial-inventory", "conflict discovery"). Missing = FAIL. |
| C-12 | **Amendment loop with update mandate** | correctness | Amendment section explicitly instructs updating the grid, veto list, or comms table -- not just observing findings. "Note the finding" alone = FAIL. |
| C-13 | **Prefilled frame types in comms table** | coverage | Communication table has a Frame Type column with a distinct label per quadrant row. Same frame on two or more rows = FAIL. |
| C-14 | **Named failure modes inline** | coverage | Two or more inline anti-pattern labels placed at the steps where those failures occur. Generic warnings in a preamble do not count. |
| C-15 | **Reversed sequence (analysis-before-synthesis)** | depth | Steps are explicitly ordered: conflict/strategy analysis first, UX segment analysis second, PM grid construction last. PM must build the grid after conflicts and segments are identified. Grid-first order = FAIL. |
| C-16 | **Amendment anti-pattern as before/after pair** | correctness | Amendment section shows the bad form (observation without revision) immediately adjacent to the correct form (update + note what changed) as a paired example. Positive instruction alone without a bad-form example = FAIL. |
| C-17 | **Anti-pattern saturation at every phase gate** | coverage | Every execution step carries at least one named failure mode inline. A single gate without an inline failure label = FAIL. Two+ labels total (C-14) is necessary but not sufficient; coverage must be complete across all steps. |
| C-18 | **Inertia stakeholder structural elevation** | depth | Three requirements all present: (1) a dedicated sub-step in the strategy phase for inertia stakeholder mapping, (2) a required `[INERTIA]` tag or equivalent in the Power/Interest grid for inertia-classified stakeholders, and (3) a required displacement-specific Frame Type (e.g., `displacement-acknowledgment`) for inertia rows in the comms table. Any one of the three absent = FAIL. |
| C-19 | **Frame Type prefill constraint table** | coverage | A standalone prefill table listing accepted Frame Type values appears as a distinct step before the comms table is populated. The prefill table must function as a constraint -- values not in the prefill table are prohibited. Enumerating accepted values inline within instructions without a separate prefill table = FAIL. |
| C-20 | **Inertia chain prefill-stage binding** | depth | When a prefill table is present (C-19 satisfied), the displacement-specific Frame Type requirement for inertia stakeholders must be stated as an explicit rule *within the prefill step* -- not as a note during content population. The prefill step must mandate the inertia row's Frame Type assignment before any rows are populated, with a corresponding inline failure label (e.g., FAIL_MISSING_DISPLACEMENT_PREFILL) at the prefill gate. Displacement mandate deferred to content-entry instructions = FAIL. Not satisfiable if C-19 is absent. |
| C-21 | **Amendment example prefill round-trip** | correctness | The correct-form half of the C-16 before/after pair must include at least one amendment case where the prefill table is updated -- not only the content rows. The example must show both the prefill table revision (Frame Type reassigned) and the corresponding content-row update as a complete round-trip. A correct-form example that updates only content rows without a corresponding prefill update = FAIL. Not satisfiable if C-16 or C-19 is absent. |

**Aspirational points**: 5 pts each x 13 = **65 pts**

---

## Scoring Reference

| Band | Range | Meaning |
|------|-------|---------|
| Golden | >= 80 | Output suitable as a golden example |
| Pass | 60-79 | Acceptable; essential criteria met |
| Fail | < 60 | Missing one or more essential criteria |

**Max score**: 155 pts (60 essential + 30 recommended + 65 aspirational)

### Round 5 Results Summary (scored under v5 rubric, max 145)

| Variation | Focus | Score (v5) | C-15 | C-16 | C-17 | C-18 | C-19 |
|-----------|-------|------------|------|------|------|------|------|
| V-01 | Inertia elevation (C-18 alone) | 125/145 | FAIL | FAIL | FAIL | PASS | FAIL |
| V-02 | Frame prefill (C-19 alone) | 125/145 | FAIL | FAIL | FAIL | FAIL | PASS |
| V-03 | Reversed sequence (C-15 alone) | 120/145 | PASS | FAIL | FAIL | FAIL | FAIL |
| V-04 | C-15 + C-16 + C-17 + C-18 | 140/145 | PASS | PASS | PASS | PASS | FAIL |
| V-05 | Full five axes | 145/145 | PASS | PASS | PASS | PASS | PASS |

Under the v6 rubric (max 155), V-05 passes C-20 and C-21 and scores 155/155. V-04 fails C-19 and therefore cannot satisfy C-20 or C-21; V-04 scores 140/155. V-01 through V-03 also fail C-19 and score identically to their v5 totals under v6.

The full aspirational target for Round 6 is all thirteen criteria (C-09 through C-21): the v5 complete set plus inertia mandate upstream at the prefill gate (C-20) and amendment example demonstrating the full prefill round-trip (C-21).
