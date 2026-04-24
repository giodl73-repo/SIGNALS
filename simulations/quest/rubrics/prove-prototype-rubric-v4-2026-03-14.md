Reading the three new patterns from the scorecard:

1. **`explicit-two-path-closure-enforces-c16`** — binary disposition generalizes beyond counter-evidence to any optional section
2. **`phase-execute-marker-as-inline-temporal-lock`** — ordering gate co-located with the action it constrains, not only in a separate output contract
3. **`labeled-pair-block-achieves-c17-without-tables`** — already absorbed by C-17's existing pass condition ("labeled pair"); confirmatory, not a new criterion; C-17 pass condition gets a clarifying note instead

That yields C-18 and C-19 as new aspirational criteria, and a minor clarification to C-17.

---

# Rubric: prove-prototype (v4)

**Updated**: 2026-03-15
**Changes from v3**: Added C-18 and C-19 (Aspirational tier) derived from Round 3 scorecard patterns. C-18 generalizes the two-path closure mechanism beyond counter-evidence to any optional section. C-19 captures the inline temporal-lock pattern from V-02's Phase Gates architecture, distinguishing point-of-construction enforcement from end-of-document output contracts. C-17 pass condition clarified to explicitly name labeled-pair blocks as a valid co-location format (confirmed by V-02 Round 3 assessment). Aspirational points raised from 20 to 30. Total raised from 120 to 130.

---

## Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01 through C-05 | 60 |
| Recommended | C-06 through C-08 | 30 |
| Aspirational | C-09, C-10, C-16 through C-19 | 30 |
| Excellence | C-11 through C-15 | 10 |
| **Total** | | **130** |

---

## Essential Criteria (60 points)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Hypothesis restated** — Output opens with an explicit restatement of the hypothesis being tested, before any description of what was built or what happened | correctness | essential | Hypothesis appears as the first substantive element; it must precede any prototype description or result |
| C-02 | **Prototype scope defined** — Output specifies what the prototype does and does not do, and states why the boundary does not invalidate the test | correctness | essential | At least two explicit exclusions are named; each exclusion is paired with a reason why the test remains valid without it |
| C-03 | **Measurement defined before building** — Output shows that success and failure criteria were established before construction, not retrofitted after results | correctness | essential | A "what to measure" section appears logically before the results section; success and failure conditions are stated explicitly |
| C-04 | **Actual vs. predicted reported** — Output explicitly compares what was predicted to happen with what actually happened | correctness | essential | Both a prediction and an observation are present; the delta (match or mismatch) is called out directly |
| C-05 | **Hypothesis verdict rendered** — Output states whether the hypothesis is confirmed, refuted, or inconclusive based on the measurements | correctness | essential | A verdict is stated in plain language; it follows from the evidence rather than being asserted without support |

---

## Recommended Criteria (30 points)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Minimality justified** | depth | recommended | Output addresses at least one explicit trade-off: what was left out and why that omission still allows the hypothesis to be tested |
| C-07 | **Raw evidence included** | coverage | recommended | At least one concrete data point appears in the results section |
| C-08 | **Limitations and next step named** | depth | recommended | One limitation and one specific next step are stated |

---

## Aspirational Criteria (30 points)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Counter-evidence addressed** | depth | aspirational | A specific counter-interpretation is named and rebutted with reasoning grounded in the evidence |
| C-10 | **Replication path clear** | behavior | aspirational | All tools, inputs, commands, or steps needed to reproduce are either stated inline or referenced by name; no implicit steps |
| C-16 | **Counter-evidence question explicitly closed** — The output resolves whether any counter-interpretation exists, not just whether one was found | depth | aspirational | The counter-evidence section terminates with one of two explicit dispositions: (a) a named counter-interpretation with a grounded rebuttal, or (b) an explicit statement that no plausible counter-interpretation exists, with a reason. A missing counter-evidence section, or one that ends with the rebuttal case only and leaves the no-counter case unaddressed, does not pass |
| C-17 | **Rationale co-located with its anchor** — Each rationale element appears in the same structural unit as the item it explains | structure | aspirational | For every rationale required by the output — scope exclusion validity, delta explanation, verdict reasoning, counter-rebuttal — the rationale appears in the same table row, labeled pair, or immediately adjacent labeled element as its anchor item. A labeled-pair block (e.g., `**Why the delta is what it is**: [explanation]` in the same block as `**Delta**`) satisfies this criterion without requiring tabular format. A rationale that requires the reader to cross-reference a distant or generic section does not pass |
| C-18 | **Optional sections terminated with explicit binary disposition** — Any section that could be empty, skipped, or produce no findings must terminate with one of exactly two explicit dispositions: findings exist plus a substantive response, or findings absent plus an explicit reason | structure | aspirational | Every section whose content depends on what was found closes with one of the two permitted dispositions. Silence, a missing section, or a section structured to handle only the affirmative case does not pass. The disposition must appear as a terminal element of the section, not as a preamble or general instruction |
| C-19 | **Ordering gate co-located with the construction action** — Each temporal ordering requirement appears as an inline execution marker at the point where the constrained action occurs, not only in a separate structural-rules section or output contract | structure | aspirational | Every phase, section, or step that must precede a later action carries its own inline gate label (e.g., *Execute before Phase N*, *Establish before any build activity*) at the point of that action. A requirement stated only in a preamble or end-of-document contract, without a co-located inline marker, does not pass |

---

## Excellence Criteria (10 points)

Derived from Round 1 scorecard patterns. These criteria distinguish outputs that *enforce* their own completeness from outputs that merely permit it.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-11 | **No sections left blank** — Every named section is populated with substantive content; no heading exists without a body | structure | excellence | Zero blank or placeholder sections; each heading is followed by content that directly addresses the section's purpose |
| C-12 | **Measurement ordering made explicit** — The temporal sequence is structurally visible; metric definition and success condition are explicitly positioned before any build or result content | structure | excellence | Section ordering or explicit labeling makes the temporal gate legible without inference |
| C-13 | **Delta computed, not co-reported** — The gap between predicted and actual is stated as its own labeled element, not merely co-located with two numbers | correctness | excellence | A dedicated delta element (column, field, or labeled sentence) states the gap explicitly; reader does not have to compute it |
| C-14 | **Verdict rationale is a distinct explanation** — The rationale explains *why* the evidence supports the verdict rather than restating the evidence | depth | excellence | A verdict rationale passage is present and distinct from the results section; it connects the observed delta to the verdict in at least one sentence of reasoning |
| C-15 | **Each scope exclusion answers the test-validity question** — For every excluded item, the output explains why the test remains valid without it | depth | excellence | Each exclusion entry answers "why does leaving this out still permit a valid test?"; bare labels or "it wasn't needed" do not pass |

---

## Scoring Guide

| Result | Threshold |
|--------|-----------|
