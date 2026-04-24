Two genuinely new patterns emerge from Round 4:

1. **V-02's inertia structural elevation** — not captured by any existing criterion. Three simultaneous requirements: dedicated strategy sub-step for inertia mapping, `[INERTIA]` tag required in the grid, `displacement-acknowledgment` required Frame Type. This is structural, not incidental.

2. **V-03's prefill-before-execute for Frame Types** — explicitly flagged in v4's diagnostic as "a confirmed v5 candidate axis." The rubric currently measures output (distinct labels present via C-13); this measures procedural constraint (prefill table shown before population).

V-04 introduces no new axes: `amendment` as Source label is a C-11 implementation (v4 rationale already ruled this out); the post-pass inventory audit is a stronger implementation of C-09/C-12, not an independent axis.

---

# Rubric — scout-stakeholders — v5

**Version**: v5 (updated from R4 excellence signals)
**Skill**: scout:stakeholders
**Date**: 2026-03-14

---

## Design Rationale

### v4 to v5 changes

Two new aspirational criteria (C-18 and C-19) extracted from Round 4. Both were first-seen in Round 4; neither appeared in prior rounds.

- **C-18** — Inertia stakeholder structural elevation: V-02 elevated inertia stakeholders across three structural positions simultaneously — a dedicated sub-step in the strategy phase (Step 1b), a required `[INERTIA]` tag in the Power/Interest grid, and a required `displacement-acknowledgment` Frame Type in the comms table. No prior variation treated inertia as a first-class structural element rather than an incidentally-included grid row. All three requirements must be present; partial presence (e.g., displacement note in comms but no grid tag) = FAIL.

- **C-19** — Frame Type prefill constraint: V-03's diagnostic in v4 explicitly flagged this as a v5 candidate: "The prefill pattern targets C-13 in a different way than the rubric currently measures." C-13 measures output — distinct labels present in the completed table. C-19 measures procedural constraint — a standalone prefill table listing accepted Frame Type values appears as a distinct step *before* the comms table is populated, constraining which values are allowed. Enumerating accepted values inline within instructions (V-01, V-02, V-04 pattern) does not satisfy C-19. V-03 is the only Round 4 variation that introduces this structure.

Round 4 also confirms three structural properties:
- V-04 demonstrates that C-15 + C-16 + C-17 can co-exist in a single output at 135/145 under the new rubric, completing the Round 4 target set in v4.
- V-01, V-02, and V-03 each pass exactly one of {C-17, C-18, C-19} at 125/145, confirming these three axes are genuinely independent.
- V-04 does not pass C-18 or C-19: its inertia treatment is a row-level displacement note (not a structural sub-step + grid tag + frame requirement), and its Frame Type values are enumerated inline rather than in a prefill table.

Point totals updated: aspirational rises from 45 to 55 pts; max score rises from 135 to 145 pts. Golden threshold (>= 80) is unchanged.

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

**Essential points**: 12 pts each × 5 = **60 pts**

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Conflict identification** | depth | Two or more distinct conflicts named, each identifying the stakeholder groups in tension and the nature of the conflict. Single-stakeholder risks do not count as conflicts. |
| C-07 | **Role framing** | coverage | All three roles (PM / Strategy / UX) structurally separated into distinct sections or steps. Collapsed into one section = FAIL. Named but not separated (partial) = 5 pts. |
| C-08 | **Critical-path gatekeepers flagged** | correctness | One or more gatekeepers tagged critical-path with a deadline or lead-time note. Generic "important" label without timing = FAIL. |

**Recommended points**: 10 pts each × 3 = **30 pts**

---

## Aspirational Criteria (55 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Amendment phase** | depth | One or more distinct findings not in the initial grid — adds, splits, or reframes a stakeholder. Absent amendment section = FAIL. |
| C-10 | **"What we are NOT doing" framing** | coverage | One or more sentences or rows describing what the product does not do for a gatekeeper. Generic "out of scope" = FAIL. |
| C-11 | **Source-tracking column in grid** | depth | Grid has a Source column or per-row origin label. Each row has an origin (e.g., "CODEOWNERS", "initial-inventory", "conflict discovery"). Missing = FAIL. |
| C-12 | **Amendment loop with update mandate** | correctness | Amendment section explicitly instructs updating the grid, veto list, or comms table — not just observing findings. "Note the finding" alone = FAIL. |
| C-13 | **Prefilled frame types in comms table** | coverage | Communication table has a Frame Type column with a distinct label per quadrant row. Same frame on two or more rows = FAIL. |
| C-14 | **Named failure modes inline** | coverage | Two or more inline anti-pattern labels placed at the steps where those failures occur. Generic warnings in a preamble do not count. |
| C-15 | **Reversed sequence (analysis-before-synthesis)** | depth | Steps are explicitly ordered: conflict/strategy analysis first, UX segment analysis second, PM grid construction last. PM must build the grid after conflicts and segments are identified. Grid-first order = FAIL. |
| C-16 | **Amendment anti-pattern as before/after pair** | correctness | Amendment section shows the bad form (observation without revision) immediately adjacent to the correct form (update + note what changed) as a paired example. Positive instruction alone without a bad-form example = FAIL. |
| C-17 | **Anti-pattern saturation at every phase gate** | coverage | Every execution step carries at least one named failure mode inline. A single gate without an inline failure label = FAIL. Two+ labels total (C-14) is necessary but not sufficient; coverage must be complete across all steps. |
| C-18 | **Inertia stakeholder structural elevation** | depth | Three requirements all present: (1) a dedicated sub-step in the strategy phase for inertia stakeholder mapping, (2) a required `[INERTIA]` tag or equivalent in the Power/Interest grid for inertia-classified stakeholders, and (3) a required displacement-specific Frame Type (e.g., `displacement-acknowledgment`) for inertia rows in the comms table. Any one of the three absent = FAIL. |
| C-19 | **Frame Type prefill constraint table** | coverage | A standalone prefill table listing accepted Frame Type values appears as a distinct step before the comms table is populated. The prefill table must function as a constraint — values not in the prefill table are prohibited. Enumerating accepted values inline within instructions without a separate prefill table = FAIL. |

**Aspirational points**: 5 pts each × 11 = **55 pts**

---

## Scoring Reference

| Band | Range | Meaning |
|------|-------|---------|
| Golden | >= 80 | Output suitable as a golden example |
| Pass | 60–79 | Acceptable; essential criteria met |
| Fail | < 60 | Missing one or more essential criteria |

**Max score**: 145 pts (60 essential + 30 recommended + 55 aspirational)

### Round 4 Results Summary

| Variation | Focus | Score | C-15 | C-16 | C-17 | C-18 | C-19 |
|-----------|-------|-------|------|------|------|------|------|
| V-01 | Anti-pattern saturation (single axis) | 125/145 | FAIL | FAIL | PASS | FAIL | FAIL |
| V-02 | Inertia prominence as structural section | 125/145 | FAIL | FAIL | FAIL | PASS | FAIL |
| V-03 | Prefill-before-execute for frame types | 125/145 | FAIL | FAIL | FAIL | FAIL | PASS |
| V-04 | Minimal triple combo (C-15 + C-16 + C-17) | 135/145 | PASS | PASS | PASS | FAIL | FAIL |

No Round 4 output achieves 145/145. V-01, V-02, and V-03 score identically at 125/145, each passing exactly one of the three new aspirational axes. V-04 achieves the Round 4 target (C-15 + C-16 + C-17) but does not reach the new aspirational criteria. The full aspirational set (C-15 + C-16 + C-17 + C-18 + C-19) — reversed sequence, adjacent before/after pair, failure-mode coverage at every gate, inertia structurally elevated across three positions, and Frame Type values constrained by a prefill table — is the v5 target for Round 5.
