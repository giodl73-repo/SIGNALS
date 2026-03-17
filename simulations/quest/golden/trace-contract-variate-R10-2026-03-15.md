# trace-contract Variate — Round 10

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v16 (C-01–C-10; essential C-01–C-05; golden threshold: all essential pass + composite >= 80)
**Round:** R10 — 3 new single-axis explorations + 2 priority combinations from R9

---

## Round 10 Variation Map

| Variation | Axis | Primary Targets | Hypothesis |
|-----------|------|-----------------|------------|
| V-01 | output-format (parallel contract table) | C-02, C-03, C-04, C-07 | A two-column Expected/Actual table per clause makes C-02 omissions visible as blank rows and C-03/C-04 failures visible as empty cells — the artifact structure enforces completeness without instruction overhead |
| V-02 | phrasing-register (mechanism-first fill-in-the-blank template) | C-05 | A positive structural template — "The [component] [action] when [condition], producing [wrong] instead of [required]" — is harder to fill with a symptom than to fill correctly because the sentence structure demands component + action + condition |
| V-03 | role-sequence (pre-flight surface enumeration before Expected) | C-01, C-02, C-10 | Enumerating contract surfaces before writing Expected Output forces the Expert to read the spec for breadth first; the surface list becomes a forward-looking coverage denominator that prevents C-01 contamination and C-02 compression |
| V-04 | lifecycle-emphasis + phrasing-register (R9 priority-1 combination: clause-enumeration gate + per-criterion cost-of-silence) | C-02, C-05, C-08, C-10 | Structural denominator (sealed clause index) enforces C-02/C-10 mechanically; per-criterion downstream-damage framing raises the cost of skipping C-05/C-08 at the exact moment each is tempted |
| V-05 | output-format + role-sequence (R9 priority-2 combination: clause-by-clause interlaced + Contract Skeptic) | C-02, C-05 | Interlaced format removes the phase gap that allows C-02 omissions; Contract Skeptic reviews hypotheses post-write; the two C-05 interventions act at different lifecycle points without overlap |

---

## V-01 — Output Format: Parallel Contract Table

**axis:** output-format
**hypothesis:** All prior output-format variations have separated Expected, Actual, and Diff into sequential prose sections. Sequential layout creates an addressability problem: the diff section references elements from the expected section by name, but the connection is prose-level — an operator can perform the diff from memory rather than from the list, and memory compresses. A two-column table (Expected | Actual) with one row per contract clause changes the enforcement mode: a blank Actual cell or a blank Result cell is visually absent, not silently absent. C-02 (no silent omissions) becomes a structural property of the table: the table cannot skip rows without producing a visible gap. C-03 (severity label) and C-04 (spec reference) are in the same row as the clause — finding metadata is co-located with the clause rather than delegated to a separate section. The hypothesis, which requires prose depth, moves to a findings expansion block below the table. Prediction: the table enforces C-02, C-03, and C-04 at write time; C-07 (three-directory layers labeled) is satisfied automatically by the table's column header structure.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### ROLE: Connectors Contract Expert

**Step 1 — Contract Scope**

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline — no external file references)
- Spec version and section governing this operation's output contract

Self-contained. A reader must determine scope from this section alone.

**Step 2 — Expected Clauses**

Before running anything, list every element the spec requires for this operation as a numbered clause list. Derive from the spec alone; do not run the operation first.

```
## Expected Clauses (spec-derived — do not run before completing this list)

CL-01  {element name}: {expected value or constraint}  [spec §X.Y]
CL-02  {element name}: {expected value or constraint}  [spec §X.Y]
...
CL-N   {element name}: {expected value or constraint}  [spec §X.Y]
```

Cover all contract surfaces:
- Success path — nominal input → nominal output
- Error path — invalid or missing input → error response
- At least one edge case — empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not defined in the spec: `CL-N  [surface]: not specified in spec  [no clause]`

When complete, write: `[CONTRACT COMMITTED — clause list sealed — Automate begins here]`

---

### ROLE: Automate

You begin after `[CONTRACT COMMITTED]`. Do not add to or modify the clause list above.

**Step 3 — Contract Comparison Table**

Run or simulate the operation against the input fixture. Then produce the following table. Every clause in the Expected Clauses list must appear as a row. Do not skip rows.

```
## Contract Comparison (20-Expected vs. 30-Actual)

| CL-ID | Element | Expected (spec) | Actual (observed) | Result | Severity |
|-------|---------|-----------------|-------------------|--------|----------|
| CL-01 | {name} | {spec-required value} | {observed value} | ✓ / F-NN | — / breaking / degraded / cosmetic |
| CL-02 | {name} | {spec-required value} | {observed value} | ✓ / F-NN | — / breaking / degraded / cosmetic |
...
| CL-N  | {name} | {spec-required value} | {observed value} | ✓ / F-NN | — / breaking / degraded / cosmetic |
```

Column rules:
- **Expected**: copy the expected value from the clause list — do not paraphrase
- **Actual**: state what the operation produced for this element; do not leave blank
- **Result**: `✓` if actual satisfies expected; `F-NN` (e.g., `F-01`) if it deviates
- **Severity**: `—` for satisfied rows; exactly one of `breaking` / `degraded` / `cosmetic` for findings

A blank Actual cell means the element was not verified. A blank Severity cell on a finding row means C-03 is not satisfied. Neither is acceptable.

Severity definitions:
- `breaking` — a consumer relying on the contract cannot function correctly
- `degraded` — the operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness or consumer behavior

**Step 4 — Findings (hypothesis and recommendation)**

For every `F-NN` row in the table, write a finding expansion block:

```
Finding F-NN (CL-NN — {element name})
spec: [spec clause from clause list — same reference]
hypothesis: [one sentence naming the mechanism — the process, path, or condition that produced the wrong value, not a restatement of what differed]
```

For every `breaking` or `degraded` finding, add:
```
recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
```

If there are no findings: write `## Findings — No deviations. All clauses satisfied.`

**Step 5 — Summary**

```
## Summary

| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

Verdict: Contract violated / Contract satisfied

Coverage: {N satisfied rows} / {N total rows in table} clauses verified, {N findings}

Recommendations:
[F-NN (CL-NN): amend-spec / fix-impl / needs-discussion — rationale]
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Phrasing Register: Mechanism-First Fill-in-the-Blank Template

**axis:** phrasing-register
**hypothesis:** All prior C-05 interventions have been prohibitive (DO NOT begin with "the output did not") or exemplary (gallery of accepted/rejected hypotheses). Both approaches operate on the operator's judgment — they instruct the operator to recognize the failure mode and choose differently. The failure persists when the operator cannot distinguish symptom from mechanism, not when they know the rule but fail to apply it. A fill-in-the-blank sentence template operates on sentence structure rather than judgment: "The `[component or code path]` `[action: maps / serializes / validates / short-circuits / omits / overwrites]` `[field or collection]` when `[condition under which the wrong behavior occurs]`, producing `[actual wrong output]` instead of the spec-required `[expected correct output]`." To fill this template with a symptom restatement, the operator would need to write "The [output] [was not as] [expected] when [observed]" — grammatically awkward, structurally incoherent. The template demands a component name, an action verb, and a condition. All three require knowledge of the system under test. If the operator cannot name all three, the template forces `[component: unknown]` or `[condition: unknown]` — the honest answer rather than a dressed-up symptom. Prediction: the template eliminates symptom restatements that use technical language ("the connector failed to serialize the field") without naming a mechanism, because the sentence structure cannot be completed with technical-sounding vagueness.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### ROLE: Connectors Contract Expert

**Step 1 — Contract Scope**

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline — no external file references)
- Spec version and section governing this operation's output contract

Self-contained.

**Step 2 — Expected Output (the contract)**

Write a `## Expected Output` section from the spec alone. The operation has not been run.

For each required element:
- State the element and its value constraint
- Cite the spec clause in parentheses

Cover all contract surfaces:
- **Success path** — nominal input → nominal output
- **Error path** — invalid or missing input → error response
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not defined in the spec: `[surface]: not specified in spec`.

Write: `[CONTRACT COMMITTED — Automate begins here]`

---

### ROLE: Automate

**Step 3 — Actual Output**

Run or simulate the operation against the input fixture. Write a `## Actual Output` section: status code, full response body, headers, observable side effects.

**Step 4 — Diff**

Write a `## Diff` section. For every element in the Expected Output:
- `✓ {element} — satisfied`
- `F-NN — {element} — deviation (see findings)`

Every element must appear. Silent omissions fail C-02.

If no deviations: write `## Diff — Contract satisfied. No findings.` and proceed to Summary.

**Step 5 — Findings**

For each deviation, write a finding entry:

```
Finding F-NN
deviation: [expected X; actual Y — state both sides]
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated]
```

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness or consumer behavior

**Hypothesis — use this template exactly:**

```
hypothesis: The `[component or code path]` `[action: maps | serializes | validates |
short-circuits | omits | overwrites | filters]` `[field or collection]` when
`[condition under which the wrong behavior occurs]`, producing `[actual wrong output]`
instead of the spec-required `[expected correct output]`.
```

Fill every bracketed slot with a specific value. Rules:
- **component**: name the class, service, middleware, adapter, or path — not "the connector" generically
- **action**: choose the verb that names what the component does wrong — not "fails to"
- **condition**: name the state, input property, or execution context that triggers the wrong behavior
- If you cannot name a slot: write `[slot: unknown]` — do not remove the slot or replace it with a vague phrase
- A hypothesis where all three specific slots are filled is almost certainly a mechanism, not a symptom

For every `breaking` or `degraded` finding, add:
```
recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
```

**Step 6 — Summary**

Write a `## Summary` section:

```
| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

Verdict: Contract violated / Contract satisfied

Coverage: {N} / {total elements in Expected Output} clauses verified, {N} deviations

Recommendations:
[F-NN: amend-spec / fix-impl / needs-discussion — rationale]
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Role Sequence: Pre-Flight Surface Enumeration

**axis:** role-sequence
**hypothesis:** The clause-enumeration gate (R9-V-01) enumerates elements *after* the Expected Output section is written — it builds the denominator from what the operator already wrote, meaning the denominator reflects the operator's implicit decisions about what to include. Surfaces the operator chose not to address remain absent from the index. A Pre-Flight surface enumeration that happens *before* Expected Output changes the order: the Contract Expert first reads the spec for breadth, listing every contract surface the spec defines with a surface ID (S-01, S-02, ...) and confirming whether each surface is defined or not. The Expected Output section must then address every declared surface. C-01 (expected-first) benefits because the Pre-Flight forces a full spec read before any element is written — contamination from observed behavior requires running the operation, which cannot happen while still in Pre-Flight. C-02 (diff complete) and C-10 (coverage ratio) benefit because the surface list is the coverage denominator — forward-declared from the spec rather than backward-derived from recall. Prediction: pre-flight enumeration improves breadth more than clause-enumeration gate because it catches missing surfaces (not just missing elements within surfaces already addressed) and cannot be shortened by omitting hard surfaces.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### ROLE: Connectors Contract Expert

**Step 0 — Pre-Flight: Enumerate contract surfaces before writing anything**

Read the spec and list every contract surface it defines for this operation. A surface is a category of behavior the spec makes a claim about (e.g., success response, 4xx error, 429 throttle response, empty result set, missing required field, auth expiry).

Do not run the operation before completing this step.

Write a `## Pre-Flight Surface Map` section:

```
## Pre-Flight Surface Map

S-01  {surface name}: {one-line description}  — spec §{X.Y}
S-02  {surface name}: {one-line description}  — spec §{X.Y}
...
S-N   {surface name}: {one-line description}  — spec §{X.Y}

Total surfaces identified: N
Surfaces defined in spec: N
Surfaces not defined (acknowledged gap): [list any]
```

Every surface in this list must be addressed in the Expected Output section. A surface you identify here but skip in Expected Output must be noted explicitly: `S-NN: skipped — [reason]`. Silent omission of a declared surface fails C-02.

When complete, write: `[PRE-FLIGHT COMPLETE — expected output begins below]`

---

**Step 1 — Contract Scope**

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline — no external file references)
- Spec version and section governing this operation's output contract

---

**Step 2 — Expected Output (the contract)**

Write a `## Expected Output` section from the spec alone. Organize by surface — use the S-NN IDs from the Pre-Flight Surface Map as subsection headers:

```
### S-01 — {surface name}

{element}: {expected value}  [spec §X.Y]
{element}: {expected value}  [spec §X.Y]
...

### S-02 — {surface name}
...
```

For surfaces not defined in the spec:
```
### S-NN — {surface name}
Not specified in spec — no contract clause exists for this surface.
```

When every surface in the Pre-Flight map is addressed, write: `[CONTRACT COMMITTED — Automate begins here]`

---

### ROLE: Automate

You begin after `[CONTRACT COMMITTED]`. Do not modify the Pre-Flight Surface Map or Expected Output.

**Step 3 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section: status code, full response body, headers, observable side effects.

**Step 4 — Diff (by surface)**

Write a `## Diff` section organized by surface (same S-NN IDs from the Pre-Flight map). For each surface:

```
### S-NN — {surface name}

{For each element in this surface's Expected Output subsection:}
✓ {element} — satisfied
F-NN — {element} — deviation (see findings)

Surface verdict: all satisfied / N finding(s)
```

Every surface from the Pre-Flight map must appear. Every element within each surface must appear. Silent omission at surface or element level fails C-02.

If no deviations across all surfaces: write `## Diff — All surfaces verified: contract satisfied.` and proceed to Summary.

**Step 5 — Findings**

For each deviation:

```
Finding F-NN
surface: S-NN — {surface name}
deviation: [expected X; actual Y — state both sides]
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated]
hypothesis: [one sentence naming the mechanism — the process, path, or condition that produced the wrong value]
```

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness or consumer behavior

For every `breaking` or `degraded` finding:
```
recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
```

**Step 6 — Summary**

```
## Summary

| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

Verdict: Contract violated / Contract satisfied

Surface coverage: {N surfaces fully satisfied} / {N surfaces in Pre-Flight map} surfaces
Clause coverage: {N elements verified} / {N total elements in Expected Output} clauses, {N deviations}

Recommendations:
[F-NN (S-NN): amend-spec / fix-impl / needs-discussion — rationale]
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Combination: Clause-Enumeration Gate + Per-Criterion Cost-of-Silence

**axes:** lifecycle-emphasis + phrasing-register
**hypothesis:** R9 priority-1 combination. R9-V-01 (clause-enumeration gate) addresses C-02 and C-10 structurally: a sealed numbered clause index prevents the diff from silently compressing — every clause must appear in the check; coverage ratio is arithmetic over the index rather than recalled from prose. R9-V-03 (per-criterion cost-of-silence) addresses C-05 and C-08 by consequence framing: at each criterion, naming the downstream damage of skipping it — the finding that cannot be actioned, the ambiguity that survives to the next release — raises the cost of abbreviation at the exact moment the operator is tempted. These two mechanisms target different criteria via different modes: V-01 is structural (the list cannot be silently shortened), V-03 is motivational (the operator sees what is lost if they skip). They are non-overlapping: V-01 produces no improvement on C-05/C-08; V-03 produces no structural improvement on C-02/C-10. Combination prediction: four criteria addressed — C-02 and C-10 via index structure, C-05 and C-08 via consequence framing — without the mechanisms interfering.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### ROLE: Connectors Contract Expert

**Step 1 — Contract Scope**

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline — no external file references)
- Spec version and section governing this operation's output contract

Self-contained. A reader must determine scope from this section alone.

**Step 2 — Expected Output (the contract)**

Write a `## Expected Output` section derived from the spec alone. The operation has not been run.

For each required element:
- State the element and its value constraint
- Cite the spec clause in parentheses

Cover all contract surfaces:
- **Success path** — nominal input → nominal output
- **Error path** — invalid or missing input → error response
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not defined in the spec: `[surface]: not specified in spec`.

**Step 3 — Clause Index (required before committing)**

At the end of the Expected Output section, emit a numbered clause index — one line per expected element. This index is the coverage denominator for the entire trace. Once written, it cannot be added to or removed from.

```
## Clause Index (sealed — coverage denominator — do not modify)

CL-01  {short element name} — {spec clause reference}
CL-02  {short element name} — {spec clause reference}
...
CL-N   {short element name} — {spec clause reference}

Total clauses: N
```

Every element written in Step 2 must appear in this index. An element absent from the index is an element that will not be verified.

Write: `[CONTRACT COMMITTED — Clause index sealed. Automate begins here.]`

---

### ROLE: Automate

You begin after `[CONTRACT COMMITTED]`. Do not add to, remove from, or modify the Clause Index.

**Step 4 — Actual Output**

Run or simulate the operation against the input fixture. Write a `## Actual Output` section: status code, full response body, headers, observable side effects.

**Step 5 — Diff (work through every clause in the index)**

Write a `## Diff` section. Work through the Clause Index from CL-01 to CL-N. For each clause:

- `CL-NN ✓ — {element name} — satisfied`
- `CL-NN F-XX — {element name} — deviation (see findings)`

Every clause in the index must appear. A clause you skip is a gap in coverage.

> **If you skip a clause silently:** there is no record that the contract was verified for that element. When a consumer reports a regression against this clause in the next release, this trace will appear clean when it is not. A skipped clause produces the same outcome as not running the trace at all for that element.

When the diff is complete, count: satisfied / findings / not exercised (surfaces unreachable with this fixture).

If no deviations: write `## Diff — All CL-01 through CL-N verified: contract satisfied.` and proceed to Summary.

**Step 6 — Findings**

For each deviation:

```
Finding F-NN
clause: CL-NN — {element name}
deviation: [expected X; actual Y — state both sides]
severity: [breaking | degraded | cosmetic]
spec: [spec clause — same reference from Clause Index]
hypothesis: [one sentence naming the mechanism that produced the deviation]
```

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness or consumer behavior

> **Hypothesis — if this names a symptom, the finding cannot be actioned:**
> "The field was not returned" and "the value did not match" describe what the trace already shows. A developer picking up this finding still does not know where to look. The finding will sit unresolved until someone investigates — the same state it was in before the trace. A mechanism hypothesis names the process, path, or condition that produced the wrong output. If you cannot name the mechanism: `hypothesis: mechanism unknown — investigation required at [named component or path]`.

For every `breaking` or `degraded` finding, add:
```
recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
```

> **Recommendation — if omitted, the session ends without a decision:**
> A breaking or degraded finding with severity and spec reference but no recommendation leaves the team unable to determine whether to open a spec amendment ticket or a fix ticket. The ambiguity outlasts the trace. `needs-discussion` is valid when the answer is genuinely unclear — but name the specific question: "unclear whether spec intended this field to be required in error responses or only in success responses."

**Step 7 — Summary**

```
## Summary

| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

Verdict: Contract violated / Contract satisfied

Coverage: {N satisfied} / {N total in Clause Index} clauses verified, {N deviations}, {N not exercised}

Recommendations:
[F-NN (CL-NN): amend-spec / fix-impl / needs-discussion — rationale]
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — Combination: Clause-by-Clause Interlaced + Contract Skeptic

**axes:** output-format + role-sequence
**hypothesis:** R9 priority-2 combination. R9-V-02 (clause-by-clause interlaced) targets C-02 by collapsing the phase gap: when expected → actual → result are written per clause rather than per phase, an operator cannot skip a clause by advancing to the next phase — there is no "next phase" until the current clause is resolved. This addresses the mechanism by which C-02 fails (mental compression during phase transitions). R9-V-04's Contract Skeptic targets C-05 at the post-write stage: a hypothesis that survived the operator's own judgment is challenged by a reader whose only question is "What caused this?" These two mechanisms are non-overlapping: interlaced format operates on write-time structure (preventing omissions); the Skeptic operates on post-write content (improving hypothesis quality). The combination test question: does the interlaced format itself change hypothesis quality, or does C-05 require Skeptic review regardless of format? If the Skeptic finds fewer rejections against V-05 than against a sequential-format artifact with the same Skeptic, the format is improving pre-write hypothesis reasoning. If rejection rates are unchanged, the Skeptic is the load-bearing mechanism and the format is defense-in-depth.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate + Contract Skeptic.

---

### Step 1 — Contract Scope

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline — no external file references)
- Spec version and section governing this operation's output contract

Self-contained. No external files needed to understand scope.

---

### Step 2 — Clause-by-Clause Trace

**This trace is written clause by clause, not phase by phase.**

Run the operation once against the input fixture. Then, for each contract clause the spec defines for this operation, write one clause block. Complete each block before starting the next.

```
### Clause {N} — {element name}

Expected: {what the spec requires — exact value, type, or constraint}
Spec: {spec clause reference}
Actual: {what the operation produced for this element}
Result: ✓ satisfied / F-NN deviation
```

If Result is `F-NN deviation`, immediately append a finding block before moving to the next clause:

```
Finding F-NN
severity: [breaking | degraded | cosmetic]
spec: [same spec clause as above]
hypothesis: [one sentence — name the mechanism, not the observed difference]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]
(omit recommendation only if cosmetic)
```

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness or consumer behavior

**Hypothesis guidance:** The hypothesis must explain *why* the actual value was produced, not restate that it differed. The question is: what process, path, mapping failure, condition, or execution order produced this output instead of the expected one? An answer that could be written by reading only the Expected and Actual lines — without knowledge of the system — is a symptom restatement.

Do not batch clauses. Each element gets its own block. A summary line ("the success path was clean") does not satisfy any clause.

Cover all contract surfaces:
- **Success path** — nominal input, nominal output
- **Error path** — invalid or missing input, error response
- **Edge cases** — at least one: empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not defined in the spec: one clause block with `Actual: not exercised — surface not in spec`.

When all clause blocks are complete, write: `[CLAUSE TRACE COMPLETE — Contract Skeptic reviews findings here]`

---

### ROLE: Contract Skeptic

You are the Contract Skeptic. You review every finding's hypothesis. Your one question: **"Does this hypothesis name what caused the deviation, or does it describe that a deviation occurred?"**

Read each finding in sequence.

**If the hypothesis names a causal mechanism** — a process, a code path condition, a mapping failure, a wrong default, a missing step, a serialization error, a middleware behavior — mark:

```
F-NN hypothesis: ACCEPTED — [one sentence confirming the mechanism is named and actionable]
```

**If the hypothesis describes what differed without naming what caused it** — "the output did not match", "the field was not returned", "there is a mismatch", "the connector failed to produce" without a named mechanism — mark:

```
F-NN hypothesis: REJECTED — symptom restatement
Skeptic challenge: "{quoted hypothesis}" names what differed, not what caused it.
Rewrite prompt: What [component / path / condition] in the system produces this output?
```

For each REJECTED finding: Automate rewrites the hypothesis in response to the Skeptic's challenge. The Skeptic reviews the rewrite once. If still a symptom:

```
F-NN hypothesis: UNRESOLVED — mechanism not established
Investigation required at: {narrowest-scope component, path, or interface you can state}
```

When all findings are ACCEPTED or UNRESOLVED, write: `[SKEPTIC REVIEW COMPLETE — proceeding to Summary]`

---

### Step 3 — Summary

After Skeptic review, write a `## Summary` section:

```
## Summary

| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

Verdict: Contract violated / Contract satisfied

Coverage: {N clauses written} total, {N ✓ satisfied}, {N deviations}, {N not exercised}

Recommendations:
[F-NN (Clause N): amend-spec / fix-impl / needs-discussion — rationale]

Skeptic outcome:
{N findings accepted | N rejected-then-accepted | N unresolved}
{For each UNRESOLVED: F-NN — investigation required at: [component/path]}
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## Combination Candidates for Round 11

| Priority | Combination | Primary Targets | Rationale |
|----------|-------------|-----------------|-----------|
| 1 | V-03 (pre-flight surface enumeration) + V-02 (mechanism-first template) | C-01, C-02, C-05, C-10 | Pre-flight reads spec for breadth before Expected is written (C-01, C-10); mechanism template constrains hypothesis form (C-05); orthogonal axes, no overlap. Pre-flight surface framing may prime mechanism thinking earlier than the template alone. |
| 2 | V-01 (parallel contract table) + V-02 (mechanism-first template) | C-02, C-03, C-04, C-05, C-07 | Table enforces C-02/C-03/C-04/C-07 structurally; template enforces C-05 in the finding expansion blocks below the table. Five criteria, two mechanisms, no overlap. Tests whether structural completeness enforcement and positive-form hypothesis enforcement compound or interfere. |
| 3 | V-03 (pre-flight) + V-04 mechanisms (clause-enumeration + cost-of-silence) | C-01, C-02, C-05, C-08, C-10 | Pre-flight declares surfaces before writing (C-01, breadth); clause-enumeration creates element-level denominator after writing (C-02, depth); cost-of-silence frames each criterion by consequence (C-05, C-08). Three lifecycle points, five criteria. Maximum coverage test for this axis combination. |

## Evaluation Order Guidance

| Priority | Variation | Rationale |
|----------|-----------|-----------|
| 1 | V-01 (parallel contract table) | Most structural single-axis change of R10. Table rows are visible; empty cells are visible; C-02/C-03/C-04 failures become layout failures. Evaluate first to establish the table-format baseline. |
| 2 | V-03 (pre-flight surface enumeration) | Only R10 variation that changes what happens before Expected Output is written. Evaluate second to isolate whether forward-declared coverage improves breadth vs. backward-declared (R9-V-01). |
| 3 | V-02 (mechanism-first template) | Positive-form C-05 intervention. Evaluate after structural variations to isolate: does the template alone produce mechanism-naming hypotheses, or does C-05 still require Skeptic review even with the template? |
| 4 | V-04 (clause-enumeration gate + cost-of-silence) | R9 priority-1 combination. Both axes validated in R9 individually; this confirms whether they compound without interference. |
| 5 | V-05 (clause-by-clause + Skeptic) | R9 priority-2 combination. Most complex R10 variation. Use Skeptic rejection rate as a leading indicator: if V-02's template already produces low rejection rates, V-05 confirms template sufficiency and Skeptic as defense-in-depth. |
