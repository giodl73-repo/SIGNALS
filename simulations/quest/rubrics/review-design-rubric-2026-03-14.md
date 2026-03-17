Rubric written to `simulations/quest/rubrics/review-design-rubric-2026-03-14.md`.

**Structure:**

| Tier | Criteria | Weight |
|------|----------|--------|
| Essential | C-01 All 6 disciplines present | 60% |
| Essential | C-02 Severity tag on every finding | |
| Essential | C-03 Domain expert selection justified by input signal | |
| Essential | C-04 Consensus block present | |
| Recommended | C-05 Unique catches surfaced | 30% |
| Recommended | C-06 Amend pathway (targeted re-run, not full re-review) | |
| Recommended | C-07 P1/P2 findings traced to specific design sections | |
| Aspirational | C-08 Severity pyramid sanity (P3 >= P2 >= P1) | 10% |
| Aspirational | C-09 Split opinion synthesis (not just contradiction list) | |

The golden bar is all 4 essential criteria passing + composite >= 80. The key design calls: C-03 forces expert selection to be signal-driven (not arbitrary), C-04 requires explicit consensus analysis even when consensus is absent, and C-06 distinguishes targeted amend (re-run affected reviewer only) from naive full re-review.
 a label outside P1/P2/P3) fails this criterion.

### C-03 | Domain Expert Auto-Selection Justified
- **Weight**: essential
- **Category**: behavior
- **Text**: At least one domain expert beyond the 6 stock disciplines is selected, and the selection is traceable to a signal in the input design (e.g., "RBAC mentioned -> security architect added").
- **Pass condition**: Output names 1+ domain expert and includes an explicit signal-to-expert mapping sentence or inline note. An expert added with no stated reason fails this criterion.

### C-04 | Consensus Block Present
- **Weight**: essential
- **Category**: depth
- **Text**: Output contains a consensus analysis section that identifies findings flagged by 2 or more reviewers. Split opinions (reviewers disagree on the same aspect) must be surfaced when present.
- **Pass condition**: A dedicated consensus/agreement section exists. If no consensus exists in the review, the output explicitly states "no consensus findings." Omission of the section entirely fails this criterion.

---

## Recommended Criteria (30% weight — improve quality)

### C-05 | Unique Catches Surfaced
- **Weight**: recommended
- **Category**: depth
- **Text**: Output calls out findings raised by exactly one reviewer that the other reviewers missed -- "unique catches." These are labeled distinctly from consensus findings.
- **Pass condition**: A unique-catches section or inline annotation is present and contains at least one entry, OR the output explicitly states no unique catches were found. A review with 7+ reviewers that omits this section fails.

### C-06 | Amend Pathway Described
- **Weight**: recommended
- **Category**: format
- **Text**: Output includes a structured amend section or instructions explaining how to address a specific finding and re-run the affected reviewer(s) on the changed section only -- not a full re-review.
- **Pass condition**: At least one finding has a corresponding amend action (what to change + which reviewer(s) to re-run). Generic "fix and re-run everything" guidance fails this criterion.

### C-07 | Finding Traceability to Design Section
- **Weight**: recommended
- **Category**: correctness
- **Text**: Each P1 finding and at least 50% of P2 findings reference the specific design section, component, or decision they apply to -- not just "the design" in general.
- **Pass condition**: P1 count with a section reference >= P1 total count. P2 section-referenced count >= 0.5 * P2 total count.

---

## Aspirational Criteria (10% weight — raise the bar)

### C-08 | Severity Distribution Sanity
- **Weight**: aspirational
- **Category**: depth
- **Text**: The finding set has a plausible severity pyramid: more P3 than P2, more P2 than P1. A design with 8 P1s and 1 P3 indicates over-escalation; a design with 8 P3s and no P1s may indicate under-scrutiny.
- **Pass condition**: P3 count >= P2 count >= P1 count, OR the output includes an explicit rationale when this pyramid is inverted (e.g., "this design has unusually high risk concentration at P1 because...").

### C-09 | Expert Disagreement Analysis
- **Weight**: aspirational
- **Category**: depth
- **Text**: Where two or more reviewers reach opposite conclusions on the same design decision (a split opinion), the output provides a synthesis note -- what the disagreement reveals about the design's trade-off space, not just a list of contradicting opinions.
- **Pass condition**: At least one split opinion in the review is accompanied by a 1-3 sentence synthesis explaining the underlying tension. Reviews with no split opinions are exempt.

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: All 4 essential criteria pass AND composite >= 80.

| Outcome    | Condition |
|------------|-----------|
| Golden     | C-01 + C-02 + C-03 + C-04 all pass, composite >= 80 |
| Acceptable | All essential pass, composite >= 70 |
| Needs work | Any essential fails OR composite < 70 |

---

## Failure Mode Reference

| Failure | Likely Criterion | Signal |
|---------|-----------------|--------|
| Missing discipline reviewer | C-01 | Fewer than 6 named discipline sections |
| Finding with no severity | C-02 | Bullet with no P1/P2/P3 tag |
| Domain expert with no stated reason | C-03 | Expert listed without input-signal mapping |
| No consensus section | C-04 | Review ends after per-reviewer blocks |
| All findings are P1 | C-08 | Over-escalation, reviewer calibration issue |
| Split opinions listed but not analyzed | C-09 | "Reviewer A says X; Reviewer B says Y" with no synthesis |
