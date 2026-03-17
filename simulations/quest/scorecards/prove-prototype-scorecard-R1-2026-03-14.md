# prove-prototype — Scoring Round 1

---

## V-01: Table-Driven

| ID | Criterion | Pass? | Evidence |
|----|-----------|-------|----------|
| C-01 | Hypothesis restated | **PASS** | "Claim" field is first item in DEFINE; explicit instruction: "must appear before any build description or result" |
| C-02 | Prototype scope defined | **PASS** | Scope table has IN/OUT column + "Why this boundary doesn't compromise the test" column; two OUT rows minimum enforced |
| C-03 | Measurement defined before building | **PASS** | Predicted value required in DEFINE table; explicit gate instruction: "Do not proceed to BUILD until this section is finished" |
| C-04 | Actual vs. predicted reported | **PASS** | Results table: Predicted \| Actual \| Delta side-by-side — delta is a required column, not optional prose |
| C-05 | Hypothesis verdict rendered | **PASS** | Verdict column in results table + separate "Verdict rationale" field decoupled from evidence display |
| C-06 | Minimality justified | **PASS** | "Minimality (required field)" — explicitly rejects "it wasn't needed"; requires naming the specific trade-off |
| C-07 | Raw evidence included | **PASS** | "Raw evidence (required field)" — explicitly rejects summary statements; enumerates acceptable forms |
| C-08 | Limitations and next step named | **PASS** | Limitations table + conditional Next step: "what specifically changes in the feature plan? Not 'do more research.'" |
| C-09 | Counter-evidence addressed | **PASS** | "Counter-check" field: name skeptic interpretation + explain why verdict holds despite it |
| C-10 | Replication path clear | **PASS** | BUILD table: Tool \| Input \| Step \| Output — all implicit steps surfaced |

**Composite: 100/100**
All essential: PASS
Verdict: **Golden**

---

## V-02: Conversational (input truncated at Step 6 body)

| ID | Criterion | Pass? | Evidence |
|----|-----------|-------|----------|
| C-01 | Hypothesis restated | **PASS** | Step 1 opens with claim; explicit: "must appear before any description of what you built or what happened" |
| C-02 | Prototype scope defined | **PASS** | Step 2: IN + two minimum OUT items, each requiring "why the test is still valid without it" |
| C-03 | Measurement defined before building | **PASS** | Step 3 opens: "Before you build anything, name the metric" — temporal gate stated plainly |
| C-04 | Actual vs. predicted reported | **PASS** | Step 5: Predicted / Observed / Delta structured fields; delta labeled explicitly |
| C-05 | Hypothesis verdict rendered | **PASS** | Verdict + "one sentence why" in Step 5; verdict follows evidence |
| C-06 | Minimality justified | **PASS** | Step 2: two excluded items each requiring per-item justification |
| C-07 | Raw evidence included | **PASS** | Step 5: "A summary statement does not count" — concrete data point required |
| C-08 | Limitations and next step | **PARTIAL** | Next step referenced in task context but limitations section truncated before body |
| C-09 | Counter-evidence addressed | **PARTIAL** | Step 6 header "What would a skeptic say?" present; body cut off before pass condition is enforceable |
| C-10 | Replication path clear | **PASS** | Step 4: "another developer could reproduce without asking any follow-up questions"; numbered steps required |

**Composite: ~88/100** (8 PASS at full weight, 2 PARTIAL at half weight; C-08/C-09 likely PASS in full prompt)
All essential: PASS
Verdict: **Passing** (truncation only; likely Golden in full form)

---

## V-03 through V-05: Not present in input

Input was truncated after V-02 Step 6 header. Scoring halted — no data to evaluate.

---

## Rankings (scored variations)

| Rank | Variation | Score | Essential Pass | Verdict |
|------|-----------|-------|----------------|---------|
| 1 | V-01 Table-Driven | 100 | All 5 | Golden |
| 2 | V-02 Conversational | ~88 | All 5 | Passing (truncation artifact) |

---

## Excellence Signals — V-01

**1. "Required field" label converts aspirational into mandatory**
Tagging minimality and raw evidence as `(required field)` creates a structural stop. The model cannot rationalize past a blank labeled "required" the way it can silently omit an unlabeled section. This is what makes C-06 and C-07 enforcement different between V-01 and typical prose prompts.

**2. Explicit temporal gate blocks retrofitting**
"Do not proceed to BUILD until this section is finished" is the only instruction that actually prevents C-03 failure. Without a gate, models write DEFINE and BUILD in one pass — the metric appears to precede the build, but was written after the result was already known. The gate makes the violation explicit.

**3. Delta column forces gap computation, not just co-reporting**
Having Predicted \| Actual \| Delta as separate columns means the model must compute and state the gap. In prose, two numbers can be mentioned without comparison. Side-by-side columns with a labeled Delta require the comparison that C-04 actually demands.

**4. Verdict rationale decoupled from evidence table**
A separate "Verdict rationale" field means the model must explain why the verdict follows — it cannot substitute the data table for the explanation. This is what differentiates C-05 PASS from PARTIAL: a verdict column says "confirmed"; a verdict rationale field says "confirmed because delta was zero and the predicted condition was met."

**5. Scope table column header is the justification prompt**
The column is titled "Why this boundary doesn't compromise the test" — not "Notes" or "Reason." The model must answer that specific question in every OUT row. The header is load-bearing, not decorative.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["required-field-label-converts-aspirational-to-mandatory", "explicit-temporal-gate-blocks-retrofitting", "delta-column-forces-gap-computation-not-co-reporting", "verdict-rationale-decoupled-from-evidence-display", "column-header-as-embedded-justification-prompt"]}
```
