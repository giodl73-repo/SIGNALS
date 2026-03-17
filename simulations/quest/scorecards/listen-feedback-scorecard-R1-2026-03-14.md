Scorecard written to `simulations/quest/scorecards/listen-feedback-scorecard-R1-2026-03-14.md`.

**Results:**

| Rank | Variation | Score |
|------|-----------|-------|
| 1 | V-05 (Combined) | 100 |
| 2 | V-02 (Scorecard-first) | 95 |
| 2 | V-03 (Phase gates) | 95 |
| 2 | V-04 (Conversational) | 95 |
| 5 | V-01 (Baseline) | 90 |

**All 5 essential criteria pass across all variations.** The only differentiation is at the aspirational tier:

- **A-01** (revision recs for NPS < 6): V-01 fails — it never prompts them. V-02 through V-05 all pass.
- **A-02** (NPS sensitivity analysis): Only V-05 passes — it's the only variation that names the section and prescribes the format.

**Key finding:** This rubric is well-matched to the prompt designs. All recommended criteria (R-01 through R-03) are reliably closed by all variations because the rubric was written with explicit zero-result guidance in mind. The interesting variance is concentrated in the aspirational tier.

**New patterns from V-05:** inline `[BLOCKING]` flags turning escalation into a verification pass; ascending-NPS ordering to surface highest-risk personas first; two-pass revision recs (inline + summary) for completeness enforcement.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["inline-blocking-flags-for-verification-escalation", "ascending-nps-priority-ordering", "two-pass-revision-recs-inline-then-summary"]}
```
le template with each persona pre-filled; "All 12 rows required."
- V-03: Phase 2 "All 12 must be scored before Phase 3 begins." Phase 3 "All 12 cards required before Phase 4."
- V-04: "Do this for all twelve people. Do not skip anyone." Conversational but explicit.
- V-05: Ascending-order list forces all 12 to be scored in Phase 1 before Phase 2 begins.

No FAIL risk across variations -- all enforce completeness structurally.

---

### C-02: Every feedback item has a severity tag -- PASS all

- V-01: Format specifies `[severity: blocking | major | minor | cosmetic]` per item.
- V-02: Same severity tag format in feedback card template.
- V-03: Phase 3 feedback format uses `[severity: blocking | major | minor | cosmetic]`.
- V-04: Defines all four levels and instructs "Tag the severity honestly." Open-ended format but explicit.
- V-05: Severity tag format in Phase 2 card template; `[BLOCKING]` inline flag adds a second enforcement layer for the most severe tier.

V-04 is the weakest -- conversational tone and open-ended format mean a model could write prose rather than a tagged list. Reliability lower than structural variations but pass condition still met by prompt intent.

---

### C-03: NPS per persona with justification -- PASS all

- V-01: `NPS: [1-10] -- [1-2 sentences connecting persona context to score]` in card header.
- V-02: One-sentence rationale in scorecard table row; brief but present.
- V-03: Phase 2 NPS-only cards: `NPS: [1-10] -- [1-2 sentences grounded in role, workflow, or priorities]`. Clean separation from feedback items.
- V-04: NPS placed AFTER feedback items. Inverted order vs. other variations. Score required + explanation required. Pass condition met but ordering difference may affect output structure.
- V-05: Phase 1 one-sentence rationale per score; NPS fixed before feedback is written.

V-04's inversion (feedback before NPS) is the main differentiator -- not a failure, but worth noting.

---

### C-04: Aggregate NPS computed and threshold applied -- PASS all

Threshold placement is the primary structural bet across variations:

- V-01: End of document. Both branches scripted. Risk: buried after substantial prose.
- V-02: AGG row in scorecard table, completed before any feedback is written. If FAIL, table header marked "REVISION REQUIRED." Strongest front-loading of C-04.
- V-03: Phase 2 gate -- threshold must be stated before Phase 3 begins. Clean separation from feedback.
- V-04: "WOULD THE PANEL RECOMMEND IT?" section. Both branches scripted. Placed after all 12 cards.
- V-05: End of Phase 1. "REVISION REQUIRED" appended on FAIL. Phase gate -- cannot proceed to Phase 2 without stating this.

All pass. V-02 and V-05 enforce it before feedback is written; V-01 and V-04 enforce it after.

---

### C-05: Cross-persona theme matrix present -- PASS all

All five variations include an explicit theme matrix section with a table template and "minimum one theme required." Placement varies (V-01/V-04 before blocking section; V-02/V-03/V-05 in synthesis phase). No variation omits it.

---

### R-01: Blocking items escalated to dedicated section -- PASS all

All five include a dedicated blocking items section with explicit zero-result guidance.

- V-01: "BLOCKING ITEMS:" section. "If no blocking items exist across all cards, state: 'No blocking items.'"
- V-02: STEP 4 with explicit zero-result.
- V-03: Phase 4 ESCALATE is a named mandatory phase. Two required outputs, both with explicit zero-result.
- V-04: "DID ANYONE FLAG A SHOWSTOPPER?" with explicit zero-result.
- V-05: Phase 3 ESCALATE collects [BLOCKING]-tagged lines from Phase 2. Inline flags make Phase 3 a verification pass, not first-pass discovery. Explicit zero-result.

V-03 and V-05 are strongest -- named phases with mandatory completion before the next phase.

---

### R-02: PM and UX lens reads -- PASS all

All five include both reads. V-02 and V-03 explicitly note that PM/UX reads do not affect aggregate NPS. All others imply this by placement.

---

### R-03: Theme matrix annotated with highest severity -- PASS all

All five include a "Highest Severity" (or equivalent) column.

- V-04 uses "Most serious severity" -- different label, equivalent meaning. PASS.
- V-03 instructs "annotate each theme with its highest severity" -- template-enforced.

---

### A-01: Revision recs for NPS < 6 -- FAIL V-01, PASS V-02/V-03/V-04/V-05

- V-01: No mention of revision recommendations for low-NPS personas. FAIL.
- V-02: "For any persona with NPS < 6: include at least one revision recommendation." Specificity requirement explicit: "Name the section, decision, or design choice that is the problem." PASS.
- V-03: Phase 4 LOW-NPS REVISION RECOMMENDATIONS section. Zero-result option provided. PASS.
- V-04: "WHAT SHOULD CHANGE?" section. Anti-pattern excluded: "'Improve clarity' is not a recommendation." PASS.
- V-05: Phase 2 REVISION REC inline per NPS < 6 persona; Phase 3 REVISION RECS SUMMARY collects and verifies all of them. Two-pass enforcement. PASS.

---

### A-02: NPS sensitivity analysis -- FAIL V-01/V-02/V-03/V-04, PASS V-05

- V-01 through V-04: No mention of sensitivity analysis, leverage personas, or highest-ROI change. FAIL.
- V-05: Phase 4 NPS SENSITIVITY ANALYSIS section. Prescribed format: leverage persona identification, why each is a leverage point, highest-ROI change per persona, and a final "Single highest-ROI change" statement with estimated aggregate lift. PASS.

A-02 is only reachable via V-05 in this rubric round.

---

## Ranking

| Rank | Variation | Score | Differentiator |
|------|-----------|-------|----------------|
| 1 | V-05 | 100 | Only variation to prompt A-02; A-01 inline + summarized in two phases |
| 2 | V-02 | 95 | Scorecard-first forces C-04 before any feedback prose; A-01 explicit |
| 2 | V-03 | 95 | Named phase gates most reliable for C-04 and R-01; A-01 in ESCALATE phase |
| 2 | V-04 | 95 | Conversational register produces richer rationale; A-01 in own section; NPS inverted |
| 5 | V-01 | 90 | Baseline; misses both aspirational; threshold at end |

---

## Excellence Signals (from V-05)

1. **Inline [BLOCKING] tags during the card loop** -- makes escalation a verification pass in Phase 3, not first-pass discovery. Reduces the chance of blocking items being missed.

2. **Ascending NPS order** -- lowest scorer first anchors revision priority before higher-scoring cards can dilute attention. Structurally biases the output toward what matters most.

3. **Phase gates as hard stops** -- "Do not proceed to Phase 2 until all 12 scores, their ascending-order list, and the aggregate result are stated." Cannot skip ahead and lose required outputs.

4. **Two-pass revision recs** -- inline during card loop (Phase 2) plus summarized in Phase 3. The summary is a completeness check; harder to silently drop a rec when it must appear in two places.

5. **Named sensitivity analysis with prescribed format** -- section name, per-persona fields, and final "single highest-ROI change" statement all specified. A vague observation cannot pass as a sensitivity analysis.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["inline-blocking-flags-for-verification-escalation", "ascending-nps-priority-ordering", "two-pass-revision-recs-inline-then-summary"]}
```
