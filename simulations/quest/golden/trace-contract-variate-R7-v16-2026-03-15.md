# trace-contract Variate — Round 7 (rubric v16)

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v16 (C-01–C-10; essential C-01–C-05; golden threshold: all essential pass + composite >= 80)
**Round:** R7 — 2 new single-axis + 3 combination passes from R6 candidates

---

## Round 7 Variation Map

| Variation | Axis | Primary Targets | Hypothesis |
|-----------|------|-----------------|------------|
| V-01 | phrasing-register (question-driven) | C-05 | Framing each phase as a question Automate must answer in writing forces reasoning rather than compliance; "What caused this?" cannot be answered by symptom restatement |
| V-02 | output-format (hypothesis example gallery) | C-05 | Embedding 3 accepted + 3 rejected hypothesis examples at the point of the hypothesis instruction gives operators an instant calibration model; the boundary between mechanism and symptom is concrete, not abstract |
| V-03 | preflight + summary-first + Skeptic (R6 P1) | C-01, C-05, C-09, C-10 | Triple-mechanism: preflight names all criteria before writing begins; summary shell creates forward-looking C-09/C-10 obligations; Skeptic enforces C-05 semantic quality after findings are drafted |
| V-04 | three-directory headings + preflight (R6 P2) | C-07, C-02, C-09, C-10 | Directory headings enforce C-07 structurally; preflight ensures all other criteria are named before the first word is written; tests whether checklist adds value beyond what the directory skeleton already provides |
| V-05 | DO NOT gates + summary-first (R6 P3) | C-01, C-05, C-09, C-10 | DO NOT language targets the precise failure form of C-01 and C-05 linguistically; summary-first targets C-09/C-10 structurally; the two axes operate on orthogonal criterion sets — no overlap, clean combined effect |

---

## V-01 — Phrasing Register: Question-Driven Self-Interview

**axis:** phrasing-register
**hypothesis:** Standard imperative prompts frame each phase as an obligation ("Write the expected output before running anything"). The operator reads the obligation, acknowledges it, and proceeds — often without fully reasoning through the criterion. Replacing imperatives with questions the operator must answer in writing forces a different cognitive posture. "What does the spec require for this operation?" cannot be answered by copying a boilerplate structure; it requires engagement with the spec. "For each deviation, what caused the difference? Not what differed — what caused it?" cannot be answered by "the output did not match" because that restates the question rather than answering it. C-05 is the primary target: phrasing the hypothesis step as a question forces Automate to produce an answer, and an answer to "what caused this?" is definitionally a mechanism, not a symptom.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

Answer each question below in writing. The question is the section header; your answer is the section body. Do not skip a question. An unanswered question is an incomplete trace.

---

### Q1 — What is the exact scope of this trace?

Write a `## Contract Scope` section. Your answer must let a reader determine the scope without opening another file:
- What operation and HTTP method (or equivalent) is under test?
- What connector or Automate context and environment?
- What is the input fixture? (Paste or describe inline — no file references.)
- What spec version and section governs this operation's output contract?

---

### Q2 — What does the spec require?

Write a `## Expected Output` section. Answer this question from the spec alone — do not run the operation first, do not rely on memory of observed behavior.

For each required element, your answer has two parts:
1. What the spec requires (the element)
2. Where in the spec it says so (the clause citation)

Answer for all contract surfaces the spec defines:
- **Success path** — nominal input: what must the output contain?
- **Error path** — invalid or missing input: what must the response contain?
- **At least one edge case** — what does the spec require for an empty collection, null required field, rate-limit trigger, or auth expiry?

If the spec does not define a surface for this operation, answer: `[surface]: not specified in spec`.

When you have answered this question completely, write:

`[CONTRACT COMMITTED — Q2 answered from spec; Q3 begins here]`

Do not run the operation before writing this line.

---

### Q3 — What did the operation actually produce?

Write a `## Actual Output` section. Run or simulate the operation against the input fixture. Your answer is the full captured response: status code, response body, all relevant headers, observable side effects.

---

### Q4 — Where did actual differ from expected?

Write a `## Diff` section. For each element in Q2's answer, answer one of:
- `✓ {element} — satisfied` (actual matches what Q2 required)
- `F-NN — {element} — deviation (see Q5)`

Every element from Q2 must appear in your answer. An element you skip is a question you did not answer — the trace fails C-02.

If no deviations: write `## Diff — Q4 answer: no deviations; contract satisfied.` and skip to Q6.

---

### Q5 — For each deviation, what caused it?

Write a `## Findings` section. For each deviation from Q4, answer four sub-questions:

```
Finding F-NN
Q4 deviation: [what was expected; what was actual — both sides]
Q5a. How severe is this? [breaking | degraded | cosmetic]
Q5b. Which spec clause does this violate? [cite the clause from Q2]
Q5c. What caused the difference? [name the mechanism — what process, mapping, serialization path, or condition produced this output instead of the expected one]
```

Sub-question definitions:
- Q5a `breaking` — a consumer relying on the contract cannot function correctly
- Q5a `degraded` — the operation runs but a guarantee is violated; silent failure or data loss possible
- Q5a `cosmetic` — differs from contract without affecting correctness or consumer behavior

Q5c must answer "what caused the difference?" — not restate what differed. An answer that begins "The output did not match" is restating Q4, not answering Q5c.

For every `breaking` or `degraded` finding, add a fifth sub-question:
```
Q5d. Should the spec be amended or the implementation fixed?
     [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
```

---

### Q6 — What is the verdict and how much of the contract was covered?

Write a `## Summary` section. Answer:

```
| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

Verdict: Contract violated / Contract satisfied

Recommendations (from Q5d):
[F-NN: amend-spec / fix-impl / needs-discussion — rationale]

Coverage: {N} / {total elements in Q2} contract clauses answered in Q4, {N} deviations found
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Output Format: Hypothesis Example Gallery Embedded

**axis:** output-format
**hypothesis:** C-05 fails in a predictable way: the hypothesis field is populated, syntactically complete, and entirely useless — "The output did not match the expected value." The failure is not that operators don't know the criterion; the failure is that they have no calibrated model of where the boundary falls between mechanism and symptom restatement. Abstract instruction ("name a mechanism, not a symptom") does not give operators that model. A concrete gallery of three accepted and three rejected hypothesis examples, placed at the exact point of the hypothesis instruction, provides the calibration at the moment it is needed. The operator can compare their candidate hypothesis to six concrete examples before committing. This is a format change: the gallery is embedded in the prompt template, not stated once in the preamble.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### Step 1 — Contract Scope

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline — no external file references)
- Spec version and section governing this operation's output contract

Self-contained: a reader must determine scope from this section alone.

---

### Step 2 — Expected Output (the contract)

Write the `## Expected Output` section from the spec before running anything. For each required element:
- State the element
- Cite the spec clause that requires it

Cover all contract surfaces the spec defines:
- **Success path** — nominal input → nominal output
- **Error path** — invalid or missing input → error response
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not in the spec, write: `[surface]: not specified in spec`.

Write: `[CONTRACT COMMITTED]`

---

### Step 3 — Actual Output

Run or simulate the operation. Write the `## Actual Output` section: status code, response body, headers, observable side effects.

---

### Step 4 — Diff

Write the `## Diff` section. For every element in the Expected Output, write:
- `✓ {element} — satisfied`, or
- `F-NN — {element} — deviation (see findings)`

Every element must appear. If no deviations: write `## Diff — Contract satisfied. No findings.` and skip to Step 6.

---

### Step 5 — Findings

For each deviation, write a finding entry:

```
Finding F-NN
deviation: [expected X; actual Y — state both sides]
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated — same clause cited in Expected Output]
hypothesis: [see gallery below]
```

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness or consumer behavior

---

**Hypothesis calibration gallery**

Before writing your hypothesis, compare it against these examples.

**Accepted — these name a mechanism:**

| Example | Why it passes |
|---------|---------------|
| "The OData normalizer strips null-valued fields during response shaping; the spec requires the field present with a null value to signal absence rather than omitting it." | Names the specific process (OData normalizer response shaping) that produced the deviation. |
| "The `items` array returns `null` on an empty result set because the collection adapter short-circuits before the outer wrapper is applied; the spec requires `[]`." | Names the code path (collection adapter short-circuit) that produces the wrong value. |
| "The `X-RateLimit-Reset` header is absent because the throttle middleware only injects it when the rate limit is actively exceeded; the spec requires it on every response regardless of throttle state." | Names the condition (rate limit not exceeded) under which the middleware fails to inject, explaining why the header is missing. |

**Rejected — these restate what differed:**

| Example | Why it fails |
|---------|--------------|
| "The output did not match the expected value." | States that there is a deviation. Does not name what produced it. |
| "There is a mismatch between the actual and expected response." | Same failure in different words. |
| "The field was returned with an incorrect value." | Describes the observation. Any reviewer reading the deviation line already knows this. |

**Rule:** If your hypothesis could be written without knowing anything about the system under test — only from reading the deviation line — it is a symptom restatement. A mechanism-naming hypothesis requires knowledge of why.

---

After every `breaking` or `degraded` finding, add:
```
recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
```

---

### Step 6 — Summary

Write a `## Summary` section:

```
| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

Verdict: Contract violated / Contract satisfied

Recommendations:
[F-NN: amend-spec / fix-impl / needs-discussion — rationale — one line per breaking/degraded finding]

Coverage: {N} / {total in Expected Output} clauses verified, {N} deviations found
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Triple Combination: Preflight + Summary-First + Contract Skeptic

**axes:** output-format + lifecycle-emphasis + role-sequence (R6 Priority 1)
**hypothesis:** Three independent mechanisms target three different failure points in the trace lifecycle. The preflight checklist (from R6-V-01) targets the point before writing begins: all ten criteria are named as obligations before the first word of the artifact is written. The summary shell (from R6-V-03) targets C-09 and C-10 structurally: writing the shell first makes the counts and coverage ratio forward-looking obligations — blank cells are visible debts. The Contract Skeptic (from R6-V-02) targets C-05 at the semantic level after findings are drafted: no hypothesis can pass without surviving "What caused this?" These three mechanisms have no overlap. Preflight is a pre-write structural gate. The summary shell is a forward-looking data commitment. The Skeptic is a post-write semantic review. Together they cover the full span of C-01–C-10 failure modes without redundancy.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate + Contract Skeptic.

---

### Step 0 — Preflight Checklist

Write the following block at the top of your output artifact. Do not proceed until this checklist is written. Tick each item as you complete the corresponding section.

```
## Preflight Checklist

- [ ] C-01  Expected Output written from spec before any actual output was observed
- [ ] C-02  Every expected element appears in the diff with an explicit result (pass or finding)
- [ ] C-03  Every finding carries exactly one severity label: breaking / degraded / cosmetic
- [ ] C-04  Every finding cites a specific spec clause
- [ ] C-05  Every finding hypothesis names a mechanism (Skeptic review required — do not tick until Skeptic accepts)
- [ ] C-06  Contract scope declared upfront (operation, context, input fixture, spec source)
- [ ] C-07  Three-directory layers (Input / Expected / Actual) explicitly labeled in the artifact
- [ ] C-08  Every breaking/degraded finding carries amend-spec / fix-impl / needs-discussion + rationale
- [ ] C-09  Summary table with per-severity counts and a verdict
- [ ] C-10  Coverage ratio stated (clauses verified / total / deviations found)
```

C-05 may only be ticked by the Contract Skeptic.

---

### Step 1 — Summary Shell (write before any findings)

Before writing any expected output or running the operation, write the `## Summary` section as an empty shell:

```
## Summary (shell — fill in as trace proceeds)

| Severity | Count |
|----------|-------|
| breaking |   ?   |
| degraded |   ?   |
| cosmetic |   ?   |
| total    |   ?   |

Verdict: [fill after diff is complete]

Recommendations:
[F-NN: amend-spec / fix-impl / needs-discussion — rationale — one per breaking/degraded finding]

Coverage: ? / ? clauses verified, ? deviations found
```

Every `?` is a debt this trace must repay before the artifact is complete.

---

### ROLE: Connectors Contract Expert

You are the Connectors contract expert. You write the expected output from the spec alone. You have not run the operation. You have not observed any implementation output.

**Step 2 — Contract Scope**

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline — no file references)
- Spec version and section governing this operation's output contract

Tick `C-06` in the preflight checklist.

**Step 3 — Expected Output**

Write the `## 20-Expected Layer` section from the spec alone. For each required element, state the element and cite the spec clause.

Cover all contract surfaces:
- **Success path** — nominal input → nominal output
- **Error path** — invalid or missing input → error response
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not in the spec: `[surface]: not specified in spec`.

As you write expected elements, update the coverage denominator in the Summary shell: `? / {count so far}`.

Tick `C-01` and `C-07 (Expected layer)`.

Write: `[CONTRACT COMMITTED — Automate begins here]`

Your role ends at this line.

---

### ROLE: Automate

You begin after `[CONTRACT COMMITTED]`. Do not modify the Expected Output section.

**Step 4 — Actual Output**

Run or simulate the operation. Write the `## 30-Actual Layer` section: status code, response body, headers, observable side effects.

Tick `C-07 (Actual layer)`.

**Step 5 — Input Layer (backfill)**

Write the `## 10-Input Layer` section: the setup record — what was fed in, what environment, what spec version.

Tick `C-07 (Input layer)`.

**Step 6 — Diff**

Write the `## Diff` section. For every element in the `20-Expected Layer`:
- `✓ {element} — satisfied`, or
- `F-NN — {element} — deviation (see findings)`

Every element must appear. Tick `C-02`.

If no deviations: write `## Diff — Contract satisfied. No findings.` Update summary shell: fill in counts (all zero), verdict (`Contract satisfied`), coverage. Tick `C-08`, `C-09`, `C-10`. Skip to Step 9.

**Step 7 — Draft Findings**

For each deviation:

```
Finding F-NN [DRAFT — awaiting Skeptic review]
deviation: [expected X; actual Y — state both sides]
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated — same clause cited in 20-Expected Layer]
hypothesis: [your best hypothesis — name the mechanism, not the symptom]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]
(include recommendation for breaking or degraded; omit for cosmetic)
```

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness or consumer behavior

Tick `C-03`, `C-04`, `C-08` after writing all findings.

Do not tick `C-05`. Write: `[FINDINGS SUBMITTED TO SKEPTIC]`

As you write findings, update the severity counts in the Summary shell.

---

### ROLE: Contract Skeptic

You are the Contract Skeptic. You read the draft findings above. For each finding, ask exactly one question: **"What caused this?"**

If the hypothesis names a causal mechanism — a process, a mapping failure, a serialization path, a wrong default, a missing condition, a code path that produces the wrong value — mark:

```
F-NN hypothesis: ACCEPTED — [one sentence confirming the mechanism is named]
```

If the hypothesis describes what differed without naming what caused it — "the output did not match", "there is a mismatch", "the value is incorrect" — mark:

```
F-NN hypothesis: REJECTED — symptom restatement
Skeptic note: "{quoted hypothesis}" states what differed. What process or condition caused it?
```

For each REJECTED finding, Automate rewrites the hypothesis. Skeptic reviews the rewrite. If still rejected after one rewrite: `F-NN hypothesis: UNRESOLVED — mechanism unknown`.

When all hypotheses are ACCEPTED or UNRESOLVED, tick `C-05`.

**Step 8 — Fill in the Summary**

Return to the `## Summary` shell. Replace every `?` with the actual value:
- Severity counts from Step 7
- Verdict: `Contract violated` or `Contract satisfied`
- Recommendations already written in Step 7 (copy here)
- Coverage ratio: `{clauses verified in Diff} / {total in 20-Expected Layer} clauses verified, {N} deviations found`

If any hypotheses are UNRESOLVED: note `F-NN hypothesis gap: mechanism unknown — further investigation required`.

Tick `C-09` and `C-10`.

**Step 9 — Final Preflight Review**

Review the preflight checklist. Every box must be checked. Any unchecked box is a named gap.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Three-Directory Headings + Preflight Checklist

**axes:** lifecycle-emphasis + output-format (R6 Priority 2)
**hypothesis:** R1-V-03 established that naming the three-directory layers as section headings (10-Input, 20-Expected, 30-Actual) enforces C-07 structurally — the mapping from phase to directory is self-evident without reading the instructions. R6-V-01 established that a preflight checklist names all criteria before writing begins, making omissions visible rather than silently absent. The combination tests a specific question: when the directory structure already gives the artifact a rigid three-layer skeleton, does the preflight checklist add value for criteria beyond C-07? The hypothesis is yes — the skeleton enforces C-07 but cannot enforce C-01 (expected before actual), C-05 (hypothesis quality), C-09 (summary table), or C-10 (coverage ratio). The checklist adds these four as named obligations that the directory structure alone does not provide.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### Step 0 — Preflight Checklist

Write the following block at the top of your artifact before writing any section. Tick each item as you complete the corresponding section.

```
## Preflight Checklist

- [ ] C-01  20-Expected Layer written from spec before 30-Actual Layer was run or observed
- [ ] C-02  Every element in 20-Expected Layer appears in the Diff with an explicit result
- [ ] C-03  Every finding carries exactly one severity label: breaking / degraded / cosmetic
- [ ] C-04  Every finding cites a specific spec clause from 20-Expected Layer
- [ ] C-05  Every finding hypothesis names a mechanism, not a symptom restatement
- [ ] C-06  10-Input Layer declares operation, context, input fixture, spec source
- [ ] C-07  All three directory layers labeled: 10-Input / 20-Expected / 30-Actual
- [ ] C-08  Every breaking/degraded finding carries amend-spec / fix-impl / needs-discussion + rationale
- [ ] C-09  Summary table with per-severity counts and a verdict
- [ ] C-10  Coverage ratio: clauses verified / total / deviations
```

---

### `## 10-Input Layer`

Write this section first. It is the setup record.

Contents:
- Operation name and HTTP method (or equivalent)
- Connector or Automate context and environment
- Input fixture — paste or describe inline; no external file references
- Spec source version and section

This answers: "What are we testing and against what spec?"

Tick `C-06` and `C-07 (Input layer)`.

---

### `## 20-Expected Layer` (the contract)

Write this section from the spec alone, before running anything. This is the contract. Every element is a claim the spec makes about what the operation must produce.

For each required element:
- State the element
- Cite the spec clause that requires it

Cover all contract surfaces defined by the spec:
- **Success path** — nominal input, nominal output per spec
- **Error path** — invalid or missing input, error response per spec
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

If the spec does not define a surface, write: `[surface]: not specified in spec`.

**Do not run the operation before this section is complete.**

Write: `[CONTRACT COMMITTED]`

Tick `C-01` and `C-07 (Expected layer)`.

---

### `## 30-Actual Layer` (observed output)

Run or simulate the operation against the input fixture. Capture the full response.

Contents:
- Status code
- Response body (full or representative)
- All relevant headers
- Observable side effects

Tick `C-07 (Actual layer)`.

---

### `## Diff`

For every element in `20-Expected Layer`:
- `✓ {element} — satisfied`
- `F-NN — {element} — deviation (see findings)`

Every element must appear. Elements in 20-Expected that are absent from the Diff are silent omissions — the trace fails C-02 regardless of finding quality.

If no deviations: write `## Diff — Contract satisfied. No findings.` and skip to Summary.

Tick `C-02`.

---

### `## Findings`

For each deviation from the Diff:

```
Finding F-NN
deviation: [expected X; actual Y — state both sides explicitly]
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated — must match a clause cited in 20-Expected Layer]
hypothesis: [mechanism, not symptom — name the causal process, not the observed difference]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]
(include recommendation for breaking or degraded; omit for cosmetic)
```

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness or consumer behavior

Tick `C-03`, `C-04`, `C-05`, `C-08` after writing all findings.

---

### `## Summary`

```
| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

Verdict: Contract violated / Contract satisfied

Recommendations:
[F-NN: amend-spec / fix-impl / needs-discussion — rationale — one line per breaking/degraded finding]

Coverage: {N} / {total in 20-Expected Layer} clauses verified, {N} deviations found
```

Tick `C-09` and `C-10`.

**Final step:** Review the preflight checklist. Every box must be checked.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — DO NOT Gates + Summary-First

**axes:** phrasing-register + lifecycle-emphasis (R6 Priority 3)
**hypothesis:** R1-V-04 established that explicit DO NOT gates targeting the precise failure forms of C-01 ("DO NOT run the operation before completing this section") and C-05 ("DO NOT begin a hypothesis with 'The output did not'") operate at the language level — they block the path of least resistance for the two most common essential failures. R6-V-03 established that writing the summary shell first makes C-09 and C-10 forward-looking structural obligations rather than trailing aspirational additions. These two axes operate on orthogonal criterion sets: DO NOT gates target C-01 and C-05; summary-first targets C-09 and C-10. Neither axis helps with the other's targets. The combination isolates each mechanism's contribution cleanly, and together they cover the four criteria most commonly failing or aspirational in contract traces.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

**Write your output in this exact order. Do not reorder the steps.**

---

### Step 1 — Write the Summary Shell (before any findings)

Before writing any expected output, before running the operation, write the `## Summary` section with all values empty. This is your forward-looking plan.

```
## Summary (shell — fill in as trace proceeds)

| Severity | Count |
|----------|-------|
| breaking |   ?   |
| degraded |   ?   |
| cosmetic |   ?   |
| total    |   ?   |

Verdict: [fill after diff is complete]

Recommendations:
[F-NN: amend-spec / fix-impl / needs-discussion — rationale — one per breaking/degraded finding]

Coverage: ? / ? clauses verified, ? deviations found
```

The shell states what the completed trace must contain. Every `?` is a gap that must be filled before the artifact is complete.

---

### ROLE: Connectors Contract Expert

You are the Connectors contract expert. You write the expected output from the spec alone. You have not run the operation. You have not observed any implementation output.

**Step 2 — Contract Scope**

REQUIRED. Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture — state inline; DO NOT reference external files
- Spec version and section governing this operation's output contract

A scope section that requires the reader to open another file fails this step.

**Step 3 — Expected Output**

REQUIRED. Write the `## Expected Output` section from the spec alone.

DO NOT run the operation before completing this section.
DO NOT infer expected values from a previous run, from memory of observed behavior, or from knowledge of the current implementation.
DO NOT mark this section complete until every contract surface has at least one expected element with a spec citation.

For each required element:
- State the element
- Cite the spec clause that requires it

Cover all contract surfaces:
- **Success path** — nominal input → nominal output
- **Error path** — invalid or missing input → error response
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not defined in the spec: `[surface]: not specified in spec`.

As you write expected elements, update the coverage denominator in the Summary shell: `? / {count so far}`.

When complete, write: `[CONTRACT COMMITTED]`

DO NOT proceed to Step 4 before writing this line.

---

### ROLE: Automate

You begin after `[CONTRACT COMMITTED]`. DO NOT revise the Expected Output section. Any belief that an Expected entry is wrong is a finding, not a license to edit.

**Step 4 — Actual Output**

REQUIRED. Run or simulate the operation against the input fixture. Write the `## Actual Output` section: status code, full response body, headers, observable side effects.

DO NOT edit the Expected Output section after this step begins.

**Step 5 — Diff**

REQUIRED. Write the `## Diff` section. For every element in the Expected Output:
- `✓ {element} — satisfied`, or
- `F-NN — {element} — deviation`

Every element must appear. Silent omissions fail C-02.

As you complete each clause, update the coverage numerator in the Summary shell.

If no deviations: write `## Diff — Contract satisfied. No findings.` Fill in the Summary shell (all counts zero, verdict `Contract satisfied`, coverage complete). Skip to Step 7.

**Step 6 — Findings**

REQUIRED. For every deviation, write a finding entry with all four fields:

```
Finding F-NN
deviation: [expected X; actual Y — state both sides explicitly]
severity: [EXACTLY ONE OF: breaking | degraded | cosmetic]
spec: [spec clause violated — must match a clause from Expected Output]
hypothesis: [one sentence on the cause — a mechanism, not a symptom]
```

DO NOT write a finding without a severity label.
DO NOT write a finding without a spec clause reference.
DO NOT begin a hypothesis with "The output did not" — that describes what differed, not what caused it.
DO NOT begin a hypothesis with "There is a mismatch" or "The value is incorrect" — same failure.

A valid hypothesis names a causal mechanism: the field mapping is not applied after the auth upgrade; the enum is serialized as an integer instead of a string; the empty-collection short-circuit returns null rather than applying the wrapper; the middleware condition check excludes the success path.

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness or consumer behavior

For every `breaking` or `degraded` finding, add:
```
recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
```

DO NOT omit a recommendation for any `breaking` or `degraded` finding.

As you write findings, update the severity counts in the Summary shell.

**Step 7 — Fill in the Summary**

Return to the `## Summary` shell written in Step 1. Replace every `?` with the actual value:
- Severity counts from Step 6
- Verdict: `Contract violated` or `Contract satisfied`
- Recommendations: copy from Step 6 (one line per breaking/degraded finding)
- Coverage: `{clauses verified in Diff} / {total in Expected Output} clauses verified, {N} deviations found`

The artifact is complete when no `?` remains in the Summary section.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## Combination Candidates for Round 8

| Priority | Axis Combination | Primary Targets | Rationale |
|----------|-----------------|-----------------|-----------|
| 1 | DO NOT gates + summary-first + hypothesis gallery (V-05 + V-02 mechanism) | C-01, C-05, C-09, C-10 | V-05 uses DO NOT to block C-01/C-05 failures linguistically; the hypothesis gallery from V-02 adds a positive model alongside the prohibitions. Prohibitions block the wrong path; gallery illuminates the right one. Together they address C-05 from both directions. |
| 2 | question-driven + Skeptic (V-01 + R6-V-02) | C-05 | Two different cognitive interventions targeting C-05: questions force reasoning before writing (V-01); Skeptic challenges quality after writing (R6-V-02). Test whether pre-write reasoning combines with post-write review to produce reliably strong hypotheses. |
| 3 | triple combination + hypothesis gallery (V-03 + V-02 mechanism) | C-01, C-05, C-09, C-10 | V-03's triple combination already targets most criteria; adding the hypothesis gallery is a targeted C-05 reinforcement inside the Skeptic phase — the gallery gives Automate the calibration model before the Skeptic reviews. Minimal addition, addresses the one failure mode V-03 already targets through the Skeptic role. |

## Evaluation Order Guidance

| Priority | Variation | Rationale |
|----------|-----------|-----------|
| 1 | V-02 (hypothesis gallery) | Isolates C-05. The gallery is the simplest possible C-05 intervention — a format change with no structural overhead. Establishes whether positive modeling (examples) suffices or whether prohibitions and/or a Skeptic role are still needed. |
| 2 | V-01 (question-driven) | Isolates C-05 from a different angle — cognitive framing vs. format. If both V-02 and V-01 improve C-05 in isolation, the combination (candidate R8 priority 2) is worth testing. |
| 3 | V-05 (DO NOT + summary-first) | Tests C-01/C-05/C-09/C-10 across two axes. Evaluate after V-02 to determine whether prohibitions add C-05 value beyond what the gallery already provides. |
| 4 | V-04 (directory headings + preflight) | Tests whether the checklist adds value when the directory structure is already enforced. If V-04 reaches golden and V-01 (preflight alone from R6) already reached golden, the delta is pure C-07 structural enforcement. |
| 5 | V-03 (triple combination) | Evaluates the maximum-mechanism combination from R6. Run last — if V-02 and V-01 reliably deliver C-05, V-03 tests whether the Skeptic role adds value beyond what the gallery and question framing already provide. |
