Looking at V-04's excellence signals, two patterns are genuinely new (not yet captured by C-11–C-14):

1. **Reversed sequence** (Strategy → UX → PM) — structural analysis-before-synthesis; PM builds the grid last so Source labels are native to the first draft, not retroactively audited
2. **Amendment before/after pair** — bad-form example immediately adjacent to correct-form example; more directive than a positive rule alone

The other two signals (anti-pattern at every gate, Source column as audit artifact) are refinements of C-14 and C-11 respectively — already in v2.

Adding C-15 and C-16 at 5 pts each: aspirational rises from 30 to 40 pts, max score from 120 to 130.

---

# Rubric -- scout-stakeholders -- v3

**Version**: v3 (updated from R2 excellence signals)
**Skill**: scout:stakeholders
**Date**: 2026-03-14

---

## Design Rationale

### v2 to v3 changes

Two new aspirational criteria (C-15 and C-16) extracted from V-04's Round 2 perfect score. Both patterns were present in V-04 (120/120) and absent in every 115-point output.

- **C-15** -- Reversed sequence (Strategy → UX → PM): enforces analysis-before-synthesis structurally rather than instructionally. PM builds the grid last, after conflicts and segments are already identified, making Source column differentiation native to the first draft instead of retroactively audited. No other Round 2 variation had this ordering.
- **C-16** -- Amendment anti-pattern as before/after pair: the bad form (observation without revision) shown immediately adjacent to the correct form (make the update, note what changed) is more directive than stating a positive rule alone. The bad form is recognizable as an actual common failure mode; proximity at the point of execution closes the gap that preamble warnings leave open.

The two patterns in V-04 that are *not* new criteria:
- Anti-pattern at every phase gate is a higher-bar variant of C-14 (two+ labels). Raising C-14's threshold would retroactively penalize Round 2 outputs; capturing the distinction as a separate criterion is deferred to v4 if Round 3 confirms it as a reliable differentiator.
- Source column with "initial-inventory" as visibly suspicious label is a specific implementation of C-11. Already scoreable under C-11 pass condition.

Point totals updated: aspirational rises from 30 to 40 pts; max score rises from 120 to 130 pts. Golden threshold (>= 80) is unchanged.

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

## Aspirational Criteria (40 pts total)

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

**Aspirational points**: 5 pts each × 8 = **40 pts**

---

## Scoring Reference

| Result | Meaning |
|--------|---------|
| All C-01..C-05 pass | Essential gate cleared |
| Composite >= 80 | Golden threshold met |
| Any essential fails | Not golden regardless of total |
| Max score | **130 pts** |

---

## Version History

| Version | Max Score | Aspirational Criteria | Change Summary |
|---------|-----------|----------------------|----------------|
| v1 | 100 | C-09, C-10 (10 pts) | Initial rubric |
| v2 | 120 | C-09 through C-14 (30 pts) | R1 signals: source column, amendment mandate, frame types, inline failure modes |
| v3 | 130 | C-09 through C-16 (40 pts) | R2 signals: reversed sequence structural enforcement, amendment before/after pair |

**Golden threshold (>= 80) is unchanged across all versions** -- all previously golden outputs remain golden.
