Reading the Round 3 scorecard carefully before writing.

The scorecard reveals one new excellence pattern not yet captured, and confirms the v3 design rationale's deferred candidate:

**New pattern — Anti-pattern saturation at every phase gate (V-03):**
V-03 placed a FAIL_ label at *every* execution step (14 labels total), not just two+ labels anywhere in the document. The v3 rationale explicitly deferred this as a v4 candidate pending Round 3 confirmation. Round 3 confirms it: V-03 achieves this consistently and it is independent of C-14 (which only requires two+ total). No other Round 3 variation targeted this axis.

No other patterns in the scorecard are genuinely new. The V-04 `amendment` source label refinement is a specific implementation of C-11, already scoreable. V-01 and V-02's distinctive behaviors (structural prohibition language, "read both forms before proceeding") are pass-condition implementations of C-15 and C-16 respectively.

**C-17 added: 5 pts. Aspirational rises to 45 pts. Max score rises to 135 pts.**

---

# Rubric — scout-stakeholders — v4

**Version**: v4 (updated from R3 excellence signals)
**Skill**: scout:stakeholders
**Date**: 2026-03-14

---

## Design Rationale

### v3 to v4 changes

One new aspirational criterion (C-17) extracted from V-03's Round 3 pattern. The criterion was explicitly flagged in v3 as a v4 candidate pending confirmation; Round 3 confirms it.

- **C-17** — Anti-pattern saturation at every phase gate: every execution step carries at least one named failure mode inline, not just two+ labels anywhere in the document. V-03 placed 14 FAIL\_ labels at every step (FAIL\_SILENT\_INFERENCE, FAIL\_ONE\_PARTY, FAIL\_NO\_INERTIA, FAIL\_NO\_SOURCE, FAIL\_PROSE\_ONLY, FAIL\_MONOLITH\_ASSUMPTION, FAIL\_NO\_NOT\_DOING, FAIL\_WRONG\_ORDER, FAIL\_NO\_MITIGATION, FAIL\_GENERIC\_CHAMPION, FAIL\_SAME\_FRAME, FAIL\_VAGUE\_TIMING, FAIL\_NO\_TIMING, FAIL\_OBSERVATION\_ONLY). No other Round 3 variation targeted this axis. C-14 remains unchanged at two+ labels total; C-17 is the higher-bar variant requiring every gate to be covered.

Round 3 also confirmed two structural properties of v3:
- C-15 and C-16 are genuinely independent axes. V-01 passes C-15 and fails C-16; V-02 passes C-16 and fails C-15. Neither incidentally produces the other.
- C-16's pass condition requires an adjacent paired example, not merely a named failure label. V-03's FAIL\_OBSERVATION\_ONLY label at the amendment gate does not satisfy C-16. The distinction is confirmed and load-bearing.

Point totals updated: aspirational rises from 40 to 45 pts; max score rises from 130 to 135 pts. Golden threshold (>= 80) is unchanged.

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

## Aspirational Criteria (45 pts total)

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

**Aspirational points**: 5 pts each × 9 = **45 pts**

---

## Scoring Reference

| Band | Range | Meaning |
|------|-------|---------|
| Golden | >= 80 | Output suitable as a golden example |
| Pass | 60–79 | Acceptable; essential criteria met |
| Fail | < 60 | Missing one or more essential criteria |

**Max score**: 135 pts (60 essential + 30 recommended + 45 aspirational)

### Round 3 Results Summary

| Variation | Focus | Score | C-15 | C-16 | C-17 |
|-----------|-------|-------|------|------|------|
| V-01 | Reversed sequence via structural phase headers | 125/130 → 125/135 | PASS | FAIL | FAIL |
| V-02 | Before/after amendment pair | 125/130 → 125/135 | FAIL | PASS | FAIL |
| V-03 | Anti-pattern saturation at every phase gate | 120/130 → 125/135 | FAIL | FAIL | PASS |
| V-04 | Minimal combo (C-15 + C-16) | 130/130 → 130/135 | PASS | PASS | FAIL |

No Round 3 output achieves 135/135. The full aspirational set (C-15 + C-16 + C-17) has not yet been demonstrated in a single output. That combination — reversed sequence, adjacent before/after pair at the amendment gate, and failure-mode coverage at every execution step — is the v4 target for Round 4.
