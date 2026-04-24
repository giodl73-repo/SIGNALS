Here is the complete updated rubric:

---

# Rubric -- scout-stakeholders -- v2

**Version**: v2 (updated from R1 excellence signals)
**Skill**: scout:stakeholders
**Date**: 2026-03-14

---

## Design Rationale

### v1 to v2 changes

Four new aspirational criteria (C-11 through C-14) extracted from Round 1 top-scoring variations. All four patterns appeared in at least one V-04/V-01/V-05 100-point output and were absent or partial in the 95-point outputs.

- **C-11** -- Source-tracking column (seen in V-04): makes the amendment phase a traceable audit instead of a free-form observation block.
- **C-12** -- Amendment update mandate (seen in V-04): converts amendment phase from observation register to revision loop.
- **C-13** -- Prefilled frame types in comms table (seen in V-05): structurally prevents same-frame repetition across quadrants.
- **C-14** -- Named failure modes inline (seen in V-01/V-04/V-05): naming the anti-pattern is more effective than positive instruction alone.

Point totals updated: aspirational rises from 10 to 30 pts; max score rises from 100 to 120 pts. Golden threshold (>= 80) is unchanged.

---

## Essential Criteria (60 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **CODEOWNERS fallback** | correctness | Org context check is the first step. Ask one question if absent. "Never infer silently" or equivalent must be present. |
| C-02 | **Power/Interest grid present** | correctness | Grid has 4+ rows with quadrant labels. Power and Interest values present for each row. |
| C-03 | **Veto risks ranked by probability** | correctness | List ordered by probability rank. Each entry includes probability + impact. |
| C-04 | **Champion with concrete action** | correctness | One+ stakeholders labelled champion with a specific action. Generic "engage champion" = FAIL. |
| C-05 | **Communication strategy per quadrant** | depth | Four quadrant rows, each with distinct message and relative timing signal. |

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Conflict identification** | depth | Two+ distinct conflicts named, each identifying both parties in tension. |
| C-07 | **Role framing** | coverage | All three roles (PM/Strategy/UX) structurally separated. Collapsed = FAIL. Partial (named but not separated) = 5 pts. |
| C-08 | **Critical-path gatekeepers flagged** | correctness | One+ gatekeeper tagged critical-path with deadline or lead-time note. |

## Aspirational Criteria (30 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Amendment phase** | depth | One+ distinct finding not in the initial grid -- adds, splits, or reframes. |
| C-10 | **"What we are NOT doing" framing** | coverage | One+ sentence/row describing what the product does not do for a gatekeeper. |
| C-11 | **Source-tracking column in grid** | depth | Grid has Source column or per-row origin label. Each row has an origin. Missing = FAIL. |
| C-12 | **Amendment loop with update mandate** | correctness | Amendment section says to update the grid, not just observe. "Note the finding" alone = FAIL. |
| C-13 | **Prefilled frame types in comms table** | coverage | Communication table has Frame Type column with distinct label per quadrant row. Same frame on all rows = FAIL. |
| C-14 | **Named failure modes inline** | coverage | Two+ inline anti-pattern labels at the steps where they occur. Generic "be specific" = does not count. |

## Scoring Reference

| Result | Meaning |
|--------|---------|
| All C-01..C-05 pass | Essential gate cleared |
| Composite >= 80 | Golden threshold met |
| Any essential fails | Not golden regardless of total |
| Max score | **120 pts** |

---

**What changed:** 4 new aspirational criteria (C-11--C-14), aspirational section grows from 10 to 30 pts, max score from 100 to 120. The golden threshold (>= 80) is unchanged -- existing golden outputs remain golden.
ower and Interest values or descriptors present for each row. Prose-only stakeholder list with no grid = FAIL. |
| C-03 | **Veto risks ranked by probability** -- Output lists veto risks in probability-ranked order, not alphabetical or grid order, with each risk stating both probability and impact. | correctness | Veto risk list is present, ordered by probability rank. Each entry includes probability + impact. Order must reflect probability rank, not alphabetical or grid order. |
| C-04 | **Champion identified with concrete action** -- At least one stakeholder is explicitly designated as champion, with a concrete activation action (not just "engage"). | correctness | One or more stakeholders labelled champion with a specific action (e.g., "give demo slot", "co-present", "early access"). Generic "engage champion" language = FAIL. |
| C-05 | **Communication strategy per quadrant** -- Output maps a communication approach to each quadrant (keep satisfied / engage / inform / champion), including message framing and timing. | depth | Four quadrant rows are present in the strategy, each with a distinct message and at least a relative timing signal (e.g., "3 weeks before", "now", "day of"). |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Conflict identification** -- Output surfaces at least two conflicts between stakeholder groups (e.g., exec framing vs. user framing, gatekeeper inertia vs. event deadline). | depth | Two or more distinct conflicts named, each identifying the stakeholder groups in tension and the nature of the conflict. Single-stakeholder risks do not count as conflicts. |
| C-07 | **Role framing** -- PM, Strategy, and UX stock roles are applied: PM owns power/interest mapping, Strategy surfaces conflicts, UX identifies journey implications or experience-path concerns. | coverage | All three roles are invoked or their perspective is traceable in the output. May be implicit if the output structure clearly separates these concerns. Roles absent or collapsed = FAIL. |
| C-08 | **Critical-path gatekeepers flagged** -- Any stakeholder whose scheduling or approval constrains the launch timeline is called out on the critical path, not just placed in the keep-satisfied quadrant. | correctness | At least one gatekeeper explicitly tagged as critical-path with a deadline or lead-time note (e.g., "Security Review must start 2 weeks before slot confirmation"). |

---

## Aspirational Criteria (30 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Amendment phase** -- Output includes at least one finding that was not evident from the initial stakeholder list, discovered through analysis (e.g., a downstream segment within a bulk group, a missing actor, a reframe of the message for a gatekeeper). | depth | A distinct amendment, finding, or "what we missed" item that adds a stakeholder, splits an existing group, or reframes an action based on analysis -- not restating something already in the grid. |
| C-10 | **"What we are NOT doing" framing** -- For compliance or security gatekeepers, output provides a concise negative-space summary: what data the tool does not collect, what it does not do, to reduce review friction. | coverage | At least one sentence or table row explicitly addresses a gatekeeper concern by describing what the product does not do. Absence = partial credit not awarded. |
| C-11 | **Source-tracking column in grid** -- The Power/Interest grid includes a Source column (or equivalent per-row annotation) recording the origin of each row: initial inventory, conflict discovery (Strategy phase), or segment analysis (UX phase). | depth | Grid has a Source column or per-row origin label. Each row has an origin. Rows missing source label = FAIL. Benefit: rows sourced from initial inventory that should have been conflict-discovered become visible as gaps during the amendment audit. |
| C-12 | **Amendment loop with update mandate** -- Amendment section instructs acting on findings, not just observing them. If analysis reveals a new stakeholder, segment split, or re-ranking, the grid is updated and the change is noted inline. | correctness | Amendment section explicitly states to update the grid (or output) when a finding changes it. "Note the finding" alone = FAIL. "Make the change and note it" (or equivalent) = PASS. Observation-only register = FAIL. |
| C-13 | **Prefilled frame types in comms table** -- Communication strategy table pre-seeds each quadrant row with a distinct named message frame (e.g., Risk frame, Value frame, Motivating frame), making it structurally impossible to repeat the same frame across quadrants. | coverage | Communication table has a Frame Type column or equivalent, with a distinct label per quadrant row. All rows carrying the same frame type = FAIL. Missing frame type column = FAIL. |
| C-14 | **Named failure modes inline** -- Output instructions name at least two specific anti-patterns by label at the steps where they are most likely to occur (e.g., "Not 'engage the dev lead' -- give a specific action", "Do not alphabetize -- rank by probability", "Do not guess org context -- ask one question"). | coverage | At least two inline failure-mode labels appear in the output instructions, each naming a specific anti-pattern. Generic "be specific" or "be thorough" guidance without naming the failure = does not count. |

---

## Scoring Reference

| Result | Meaning |
|--------|---------|
| All C-01..C-05 pass | Essential gate cleared |
| Composite >= 80 | Golden threshold met |
| Any essential fails | Output not useful regardless of total score |
| Max score | 120 pts (60 essential + 30 recommended + 30 aspirational) |

```
Example: C-01..C-05 pass (60), C-06+C-07 pass (20), C-09 pass (5) = 85 -> GOLDEN
Example: C-03 fails = essential gate broken -> NOT GOLDEN even if composite is high
Example: C-01..C-05 (60) + all recommended (30) + all aspirational (30) = 120 -> GOLDEN + EXCELLENCE
```

### C-07 partial credit note

C-07 awards 5 pts (partial) when all three roles are named but UX has no structurally distinct section -- i.e., UX concerns are folded into another section rather than separated. Full 10 pts requires output structure to clearly separate PM, Strategy, and UX analytical sections.
