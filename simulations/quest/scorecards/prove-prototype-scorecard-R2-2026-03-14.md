# Quest Score — prove-prototype (Round 2)

**Rubric**: v2 (110 pts) | **Variations**: V-01, V-02, V-03 (partial), V-04 and V-05 not provided
**Note**: Trace artifact is placeholder; scoring reflects each prompt's structural enforcement power — the probability that a model following this variation produces output satisfying each criterion.

---

## V-01 — Table-Dominant Format

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Hypothesis restated | **PASS** | "Restate it...as the first line of your output...This line must appear before any other content." Direct structural requirement. |
| C-02 | Prototype scope defined | **PASS** | Table requires ≥2 rows; third column header is literally "Why the test remains valid without the excluded item" — "it wasn't needed" explicitly rejected. |
| C-03 | Measurement defined before building | **PASS** | "This table must appear in the output before any description of building or results. If you find yourself writing build steps...stop and complete this table first." Double enforcement. |
| C-04 | Actual vs. predicted reported | **PASS** | Step 5 table has explicit Predicted value and Actual value columns. Delta column structurally forces the comparison. |
| C-05 | Verdict rendered | **PASS** | Step 6: labeled verdict field + distinct rationale paragraph required. |
| C-06 | Minimality justified | **PASS** | Third column in scope table covers each exclusion's test-validity rationale; ≥2 rows enforced. |
| C-07 | Raw evidence included | **PASS** | "Include at least one concrete data point in the Actual value column (a number, a count, a measured duration, or a direct quote from output)." |
| C-08 | Limitations and next step | **PASS** | Step 7 table with "One row minimum. The next step must be specific enough to act on in the next session." |
| C-09 | Counter-evidence addressed | **PASS** | Step 8 requires either a rebutted counter-interpretation or an explicit statement that none exists with rationale. |
| C-10 | Replication path clear | **PASS** | "Every tool, input, and command must be named explicitly so someone else can replicate the build from this description alone." |
| C-11 | No sections left blank | **PASS** | Header declaration: "Every table cell must be populated. No cell may be left blank or contain a placeholder." Structural enforcement strongest of any variation. |
| C-12 | Measurement ordering explicit | **PASS** | "Output contract: All eight steps must appear in order." + in-step gate: "stop and complete this table first." |
| C-13 | Delta computed, not co-reported | **PASS** | Column header "Delta (predicted − actual)" + "The Delta column must be computed explicitly — do not leave it for the reader to infer." |
| C-14 | Verdict rationale distinct | **PASS** | "This rationale must be a new explanation, not a restatement of the results table." |
| C-15 | Each exclusion answers test-validity | **PASS** | Table column header directly asks the question; row-level enforcement via ≥2 row requirement. |

**Composite: 110 / 110 — Golden**

---

## V-02 — Conversational / Imperative

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Hypothesis restated | **PASS** | "restate it right now, before you write anything else. Put it at the top. Label it 'Hypothesis.'" |
| C-02 | Prototype scope defined | **PASS** | "List at least two things your prototype will leave out. For each one, answer this question..." Test-validity question asked per exclusion. |
| C-03 | Measurement defined before building | **PASS** | "Label it 'Measurement protocol.' Do not move on to building until this section exists." + final rule restated at end. |
| C-04 | Actual vs. predicted reported | **PASS** | "Put your prediction next to your result. Then compute the gap. Don't just show two numbers — name the gap." |
| C-05 | Verdict rendered | **PASS** | "Confirmed? Refuted? Inconclusive? Say it plainly." |
| C-06 | Minimality justified | **PASS** | Test-validity framing ("Does leaving this out mean the test is invalid?") covers this; not labeled "trade-off" but functionally equivalent. |
| C-07 | Raw evidence included | **PASS** | "At least one of your results must be a concrete data point: a number, a measured output, a direct quote from what ran." |
| C-08 | Limitations and next step | **PASS** | "One limitation. One next step specific enough to act on. Not 'do more testing.' Something concrete." |
| C-09 | Counter-evidence addressed | **PASS** | "Name that argument. Then rebut it using the evidence you already have. If there is genuinely no counter-interpretation, say so and say why." |
| C-10 | Replication path clear | **PASS** | "write down every step you take in enough detail that someone else could replicate it: what tool, what input, what command, what you observed." |
| C-11 | No sections left blank | **PARTIAL** | "Do not skip steps" enforces section presence but not cell-level population depth. No structural mechanism (table) prevents thin section bodies. Prose imperative alone is weaker. |
| C-12 | Measurement ordering explicit | **PASS** | Final rule: "One rule above all: the measurement protocol (step 3) must appear in your output before the build output (step 4)." |
| C-13 | Delta computed, not co-reported | **PASS** | "'I predicted X. I observed Y. The difference is Z.'" Template pattern explicitly shown. |
| C-14 | Verdict rationale distinct | **PASS** | "This explanation is not the results again. It is the reasoning that bridges the evidence to the conclusion." |
| C-15 | Each exclusion answers test-validity | **PASS** | Per-exclusion question: "Does leaving this out mean the test is invalid? If the answer is no, write down why not." |

**Composite: 109 / 110 — Golden**
*(C-11 scored at 1/2 pts: PARTIAL = 50% credit)*

---

## V-03 — Phase Gates (PARTIAL PROMPT — cutoff after Phase 3 Task line)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Hypothesis restated | **PASS** | Phase 1: "Restate the hypothesis being tested. This restatement must be the first substantive element of your output." Gate 1 enforces it. |
| C-02 | Prototype scope defined | **PASS** | Phase 2: "name at least two items it excludes. For each exclusion, answer the test-validity question." Gate 2 checklist verifies. |
| C-03 | Measurement defined before building | **PASS** | Phase 3: "Commit to measurement criteria before any build output exists. This phase exists entirely to prevent post-hoc retrofitting." |
| C-04 | Actual vs. predicted reported | **UNKNOWN** | Phase 4+ not visible due to cutoff. Cannot confirm coverage. |
| C-05 | Verdict rendered | **UNKNOWN** | Phase 5+ not visible. Cannot confirm. |
| C-06 | Minimality justified | **PASS** | Phase 2 explicitly requires "at least one minimality trade-off...something you could have included that you chose not to, and why." Strongest explicit minimality coverage of any variation. |
| C-07 | Raw evidence | **UNKNOWN** | Not visible in truncated text. |
| C-08 | Limitations and next step | **UNKNOWN** | Not visible. |
| C-09 | Counter-evidence | **UNKNOWN** | Not visible. |
| C-10 | Replication path | **UNKNOWN** | Not visible. |
| C-11 | No blank sections | **PASS** (visible phases) | Gate checks require explicit "yes/no + fulfill" at each phase boundary. Strong structural enforcement where visible. |
| C-12 | Measurement ordering explicit | **PASS** | Phase 3 is titled "Measure-First" and gate structure enforces phases cannot be skipped. |
| C-13 | Delta computed | **UNKNOWN** | Not visible. |
| C-14 | Verdict rationale distinct | **UNKNOWN** | Not visible. |
| C-15 | Each exclusion answers test-validity | **PASS** | Phase 2: "An exclusion without a test-validity answer does not satisfy this phase." Per-exclusion gate enforcement. |

**Composite: Cannot compute (prompt incomplete)**
**Confirmed essential passes: C-01, C-02, C-03 (3/5). C-04, C-05 unconfirmed.)**
*V-03 is unrankable due to cutoff. Phase 1–3 quality is strongest structural design in the set.*

---

## V-04, V-05

**Not provided.** Cannot score.

---

## Ranking (scorable variations)

| Rank | Variation | Score | Result |
|------|-----------|-------|--------|
| 1 | V-01 (Table-Dominant) | 110 / 110 | Golden |
| 2 | V-02 (Conversational/Imperative) | 109 / 110 | Golden |
| — | V-03 (Phase Gates) | incomplete | Not ranked |

---

## Excellence Signals from V-01

**Signal 1 — Column header as criterion enforcer**
V-01's third scope column header is verbatim the rubric question: "Why the test remains valid without the excluded item." The model reads the column header as it writes, which makes skipping the test-validity reasoning structurally awkward. Prose prompts ask the question once; table headers repeat it per row.

**Signal 2 — Output contract block**
V-01 appends a final "Output contract" paragraph that restates ordering requirements after all step instructions. This functions as a closing gate: the model verifies completeness against the contract after generating all content, not just at the point of each step.

**Signal 3 — Explicit "do not infer" language on Delta**
"The Delta column must be computed explicitly — do not leave it for the reader to infer." The phrase "do not leave it for the reader to infer" targets the exact failure mode the C-13 criterion was written to prevent. V-02 handles this with a template ("I predicted X. I observed Y.") but V-01's column structure plus the explicit anti-inference instruction is stronger structural coverage.

**Signal 4 — Header declaration scoping the entire output**
"Every table cell must be populated. No cell may be left blank or contain a placeholder." appears at the very top before any steps. This means the model internalizes the population constraint before it begins structuring output — not after seeing a blank cell.

---

```json
{"top_score": 110, "all_essential_pass": true, "new_patterns": ["column-header-as-criterion-enforcer", "output-contract-closing-block", "anti-inference-language-on-delta"]}
```
