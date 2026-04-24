Looking at the Round 2 scorecard, two new patterns emerge that aren't captured in any current criterion:

1. **Counter-evidence closure** — V-01 requires either a rebuttal *or* an explicit "none exists + rationale." C-09 only covers the rebuttal case; it leaves the question open when no counter-interpretation applies.

2. **Rationale co-location** — V-01's tables structurally pair each rationale with its anchor (same row: exclusion + validity reason; same row: predicted + actual + delta). The existing criteria require the rationale to *exist* but not to be *co-located*. V-02's PARTIAL on C-11 traces directly to absence of this structural pairing.

Here is the complete v3 rubric:

---

# Rubric: prove-prototype (v3)

**Updated**: 2026-03-14
**Changes from v2**: Added C-16 and C-17 (Aspirational tier) derived from Round 2 scorecard patterns. C-16 closes the counter-evidence gap exposed by C-09 when no counter-interpretation exists. C-17 captures the structural co-location pattern that distinguished V-01 from V-02 on C-11. Aspirational points raised from 10 to 20. Total raised from 110 to 120.

---

## Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01 through C-05 | 60 |
| Recommended | C-06 through C-08 | 30 |
| Aspirational | C-09 through C-10, C-16 through C-17 | 20 |
| Excellence | C-11 through C-15 | 10 |
| **Total** | | **120** |

---

## Essential Criteria (60 points)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Hypothesis restated** -- Output opens with an explicit restatement of the hypothesis being tested, before any description of what was built or what happened | correctness | essential | Hypothesis appears as the first substantive element; it must precede any prototype description or result |
| C-02 | **Prototype scope defined** -- Output specifies what the prototype does and does not do, and states why the boundary does not invalidate the test | correctness | essential | At least two explicit exclusions are named; each exclusion is paired with a reason why the test remains valid without it |
| C-03 | **Measurement defined before building** -- Output shows that success and failure criteria were established before construction, not retrofitted after results | correctness | essential | A "what to measure" section appears logically before the results section; success and failure conditions are stated explicitly |
| C-04 | **Actual vs. predicted reported** -- Output explicitly compares what was predicted to happen with what actually happened | correctness | essential | Both a prediction and an observation are present; the delta (match or mismatch) is called out directly |
| C-05 | **Hypothesis verdict rendered** -- Output states whether the hypothesis is confirmed, refuted, or inconclusive based on the measurements | correctness | essential | A verdict is stated in plain language; it follows from the evidence rather than being asserted without support |

---

## Recommended Criteria (30 points)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Minimality justified** | depth | recommended | Output addresses at least one explicit trade-off: what was left out and why that omission still allows the hypothesis to be tested |
| C-07 | **Raw evidence included** | coverage | recommended | At least one concrete data point appears in the results section |
| C-08 | **Limitations and next step named** | depth | recommended | One limitation and one specific next step are stated |

---

## Aspirational Criteria (20 points)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Counter-evidence addressed** | depth | aspirational | A specific counter-interpretation is named and rebutted with reasoning grounded in the evidence |
| C-10 | **Replication path clear** | behavior | aspirational | All tools, inputs, commands, or steps needed to reproduce are either stated inline or referenced by name; no implicit steps |
| C-16 | **Counter-evidence question explicitly closed** -- The output resolves whether any counter-interpretation exists, not just whether one was found | depth | aspirational | The counter-evidence section terminates with one of two explicit dispositions: (a) a named counter-interpretation with a grounded rebuttal, or (b) an explicit statement that no plausible counter-interpretation exists, with a reason. A missing counter-evidence section, or one that ends with the rebuttal case only and leaves the no-counter case unaddressed, does not pass |
| C-17 | **Rationale co-located with its anchor** -- Each rationale element appears in the same structural unit as the item it explains | structure | aspirational | For every rationale required by the output — scope exclusion validity, delta explanation, verdict reasoning, counter-rebuttal — the rationale appears in the same table row, labeled pair, or immediately adjacent labeled element as its anchor item. A rationale that requires the reader to cross-reference a distant or generic section does not pass |

---

## Excellence Criteria (10 points)

Derived from Round 1 scorecard patterns. These criteria distinguish outputs that *enforce* their own completeness from outputs that merely permit it.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-11 | **No sections left blank** -- Every named section is populated with substantive content; no heading exists without a body | structure | excellence | Zero blank or placeholder sections; each heading is followed by content that directly addresses the section's purpose |
| C-12 | **Measurement ordering made explicit** -- The temporal sequence is structurally visible; metric definition and success condition are explicitly positioned before any build or result content | structure | excellence | Section ordering or explicit labeling makes the temporal gate legible without inference |
| C-13 | **Delta computed, not co-reported** -- The gap between predicted and actual is stated as its own labeled element, not merely co-located with two numbers | correctness | excellence | A dedicated delta element (column, field, or labeled sentence) states the gap explicitly; reader does not have to compute it |
| C-14 | **Verdict rationale is a distinct explanation** -- The rationale explains *why* the evidence supports the verdict rather than restating the evidence | depth | excellence | A verdict rationale passage is present and distinct from the results section; it connects the observed delta to the verdict in at least one sentence of reasoning |
| C-15 | **Each scope exclusion answers the test-validity question** -- For every excluded item, the output explains why the test remains valid without it | depth | excellence | Each exclusion entry answers "why does leaving this out still permit a valid test?"; bare labels or "it wasn't needed" do not pass |

---

## Scoring Guide

| Result | Threshold |
|--------|-----------|
| Golden | All 5 essential pass + composite >= 90 |
| Passing | All 5 essential pass + composite 60-89 |
| Needs work | 4 essential pass |
| Failing | 3 or fewer essential pass |

### Essential failure modes

- **C-01 missing**: output does not reference the hypothesis at all
- **C-02 missing**: scope boundaries are absent or unnamed
- **C-03 missing**: measurement criteria appear after or alongside results
- **C-04 missing**: prediction is absent; only result is stated
- **C-05 missing**: no verdict is rendered; output ends on results alone

---

**Note on C-16 vs C-09**: C-09 passes when a counter-interpretation is named and rebutted. C-16 passes only when the counter-evidence question is *closed* — either by rebuttal or by explicit dismissal with reason. An output can pass C-09 while failing C-16 if no counter-interpretation applied and the output simply omitted the section. V-02's approach ("If there is genuinely no counter-interpretation, say so and say why") satisfies both; outputs that silently skip the section when no counter applies satisfy neither.
