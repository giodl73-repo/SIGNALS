Written to `simulations/quest/rubrics/prove-prototype-rubric-2026-03-14.md`.

---

**Rubric summary: prove-prototype**

**5 Essential (60 pts)**
- C-01 Hypothesis restated — must appear before prototype description
- C-02 Prototype scope defined — what it does, what it doesn't, why the boundary
- C-03 Measurement defined before building — success/failure criteria stated upfront, not retrofitted
- C-04 Actual vs. predicted reported — explicit delta between prediction and observation
- C-05 Hypothesis verdict rendered — confirmed / refuted / inconclusive with evidence backing

**3 Recommended (30 pts)**
- C-06 Minimality justified — what was left out and why that's still a valid test
- C-07 Raw evidence included — at least one concrete data point, not just summary prose
- C-08 Limitations and next step named — specific, not vague

**2 Aspirational (10 pts)**
- C-09 Counter-evidence addressed — names a possible counter-interpretation and rebuts it
- C-10 Replication path clear — someone else could reproduce the prototype without follow-up questions

**Design note**: C-03 (measure before build) is the discipline criterion — it's what separates a controlled test from a build-then-rationalize. C-04 + C-05 together are what distinguish a prototype *report* from a prototype *log* — the comparison and the verdict are what make it a signal.
e construction, not retrofitted after results | correctness | essential | A "what to measure" section appears logically before the results section; success and failure conditions are stated explicitly |
| C-04 | **Actual vs. predicted reported** -- Output explicitly compares what was predicted to happen with what actually happened | correctness | essential | Both a prediction and an observation are present; the delta (match or mismatch) is called out directly |
| C-05 | **Hypothesis verdict rendered** -- Output states whether the hypothesis is confirmed, refuted, or inconclusive based on the measurements | correctness | essential | A verdict is stated in plain language; it follows from the evidence rather than being asserted without support |

---

## Recommended Criteria (30 points)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Minimality justified** -- Output explains why this was the smallest sufficient prototype (not over-built, not under-built) | depth | recommended | Output addresses at least one explicit trade-off: what was left out and why that omission still allows the hypothesis to be tested |
| C-07 | **Raw evidence included** -- Output includes actual measurements, logs, counts, or observations -- not just summary conclusions | coverage | recommended | At least one concrete data point (number, log excerpt, screenshot reference, or enumerated list of observed behaviors) appears in the results section |
| C-08 | **Limitations and next step named** -- Output acknowledges at least one limitation of the prototype and names a concrete next action | depth | recommended | One limitation and one next step are stated; next step is specific (not "do more research") |

---

## Aspirational Criteria (10 points)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Counter-evidence addressed** -- Output identifies at least one result or observation that could be interpreted as contradicting the conclusion, and explains why the conclusion still holds | depth | aspirational | A specific counter-interpretation is named and rebutted with reasoning grounded in the evidence |
| C-10 | **Replication path clear** -- Output is written such that another developer could independently reproduce the prototype and re-run the measurement without asking any follow-up questions | behavior | aspirational | All tools, inputs, commands, or steps needed to reproduce are either stated inline or referenced by name; no implicit steps |

---

## Scoring Guide

| Result | Score |
|--------|-------|
| All 5 essential pass + composite >= 80 | Golden |
| All 5 essential pass + composite 60-79 | Passing |
| 4 essential pass | Needs work |
| 3 or fewer essential pass | Failing |

### Essential failure modes (automatic fail regardless of composite)

- C-01 missing: output does not reference the hypothesis at all
- C-03 missing: measurement criteria defined only after results are known (confirmation bias)
- C-04 missing: no comparison between prediction and observation (not a test -- just a build)
- C-05 missing: no verdict on the hypothesis (output ends without answering the question)
