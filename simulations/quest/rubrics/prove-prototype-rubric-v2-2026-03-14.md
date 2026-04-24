Here is the complete updated rubric:

---

# Rubric: prove-prototype (v2)

**Updated**: 2026-03-14
**Changes from v1**: Added C-11 through C-15 (Excellence tier) derived from Round 1 scorecard patterns. Aspirational tier expanded from 2 to 7 criteria. Total points raised from 100 to 110.

---

## Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01 through C-05 | 60 |
| Recommended | C-06 through C-08 | 30 |
| Aspirational | C-09 through C-10 | 10 |
| Excellence | C-11 through C-15 | 10 |
| **Total** | | **110** |

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

## Aspirational Criteria (10 points)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Counter-evidence addressed** | depth | aspirational | A specific counter-interpretation is named and rebutted with reasoning grounded in the evidence |
| C-10 | **Replication path clear** | behavior | aspirational | All tools, inputs, commands, or steps needed to reproduce are either stated inline or referenced by name; no implicit steps |

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
| Golden | All 5 essential pass + composite >= 80 |
| Passing | All 5 essential pass + composite 60-79 |
| Needs work | 4 essential pass |
| Failing | 3 or fewer essential pass |

### Essential failure modes

- **C-01 missing**: output does not reference the hypothesis at all
- **C-03 missing**: measurement criteria defined only after results are known (confirmation bias)
- **C-04 missing**: no comparison between prediction and observation (not a test -- just a build)
- **C-05 missing**: no verdict on the hypothesis (output ends without answering the question)

---

**Mapping from scorecard patterns to new criteria:**

| Pattern | Criterion |
|---------|-----------|
| required-field-label-converts-aspirational-to-mandatory | C-11 |
| explicit-temporal-gate-blocks-retrofitting | C-12 |
| delta-column-forces-gap-computation-not-co-reporting | C-13 |
| verdict-rationale-decoupled-from-evidence-display | C-14 |
| column-header-as-embedded-justification-prompt | C-15 |
is condition |

---

## Scoring Guide

| Result | Threshold |
|--------|-----------|
| Golden | All 5 essential pass + composite >= 80 |
| Passing | All 5 essential pass + composite 60-79 |
| Needs work | 4 essential pass |
| Failing | 3 or fewer essential pass |

### Essential failure modes (automatic fail regardless of composite)

- **C-01 missing**: output does not reference the hypothesis at all
- **C-03 missing**: measurement criteria defined only after results are known (confirmation bias)
- **C-04 missing**: no comparison between prediction and observation (not a test -- just a build)
- **C-05 missing**: no verdict on the hypothesis (output ends without answering the question)

---

## Design Notes

**C-03** (measure before build) is the discipline criterion -- it separates a controlled test from a build-then-rationalize. An output that retroactively invents measurement criteria is not a prototype report; it is a rationalization.

**C-04 + C-05** together distinguish a prototype *report* from a prototype *log* -- the comparison and the verdict are what make it a signal. C-13 (v2) raises the bar further: co-reporting two numbers is not the same as computing the gap.

**C-11 through C-15** (v2 additions) capture a structural discipline that goes beyond content presence. They test whether the output *enforces* its own completeness -- whether each section answers its specific question rather than merely existing. A prompt template that uses required-field labels, explicit temporal gates, and per-row justification columns produces outputs that satisfy these criteria naturally; outputs that satisfy them without such scaffolding demonstrate deeper internalization of the test discipline.
