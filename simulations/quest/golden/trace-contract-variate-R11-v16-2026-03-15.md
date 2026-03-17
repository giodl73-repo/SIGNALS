# trace-contract Variate — Round 11 (rubric v16)

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v16 (C-01–C-10; essential C-01–C-05; golden threshold: all essential pass + composite >= 80)
**Round:** R11 — 3 new single-axis explorations + 2 priority combinations from R10

---

## Round 11 Variation Map

| Variation | Axis | Primary Targets | Hypothesis |
|-----------|------|-----------------|------------|
| V-01 | role-sequence (Spec Auditor pre-role) | C-01, C-06, C-10 | A dedicated Spec Auditor role that produces a signed-off surface inventory before the Expert writes a single expected element changes the spec-reading phase from an implicit prerequisite to an auditable handoff — the surface list is a role artifact, not a side effect of writing |
| V-02 | output-format (deviation-priority layout) | C-05, C-08, C-09 | Placing the Findings section immediately after Actual Output — before the Summary — and organizing the artifact for a reader who wants to know "what broke" before "what was verified" makes finding depth the primary quality signal, shifting operator attention from coverage breadth to finding quality |
| V-03 | lifecycle-emphasis (hypothesis-before-severity) | C-05 | Writing the hypothesis before assigning severity within each finding prevents severity anchoring: when the operator sees "breaking" before writing the hypothesis, they tend to write a more alarming restatement; writing mechanism first forces independent causal reasoning |
| V-04 | role-sequence + phrasing-register (R10 priority-1: pre-flight enumeration + mechanism-first template) | C-01, C-02, C-05, C-10 | Pre-flight reads spec for breadth before Expected is written (C-01, C-10); mechanism-first template constrains hypothesis form at the sentence-structure level (C-05); orthogonal axes with no overlap |
| V-05 | output-format + phrasing-register (R10 priority-2: parallel contract table + mechanism-first template) | C-02, C-03, C-04, C-05, C-07 | Table enforces C-02/C-03/C-04/C-07 structurally via visible blank cells; mechanism-first template enforces C-05 in the finding expansion blocks below the table; five criteria, two independent mechanisms |

---

## V-01 — Role Sequence: Spec Auditor Pre-Role

**axis:** role-sequence
**hypothesis:** All prior role-sequence variations assign the spec-reading responsibility to the Contract Expert, as a Step 0 or pre-flight task. The Expert still writes the surface list and the Expected Output in the same role pass, meaning the surface enumeration and the expected value authorship are entangled in the same cognitive act — the Expert can short-circuit by writing expected values while still in spec-reading mode, without separating "what surfaces exist" from "what the values should be." A dedicated Spec Auditor role that only enumerates surfaces and declares their spec coverage — and cannot write expected output — separates these two acts into distinct role identities with a role-handoff gate between them. The Expert cannot begin writing Expected Output until the Auditor's surface inventory is complete and committed. The Auditor has no expected-output responsibility, which prevents them from contaminating the inventory with implementation assumptions. Prediction: C-01 (expected-first) improves because the Expert reads a spec-derived surface list before writing anything, not after; C-06 (contract scope declared upfront) improves because the Auditor's output is the scope declaration; C-10 (coverage ratio) improves because the Auditor's surface count is the denominator and is established before any verification occurs.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Spec Auditor + Connectors contract expert + Automate.

---

### ROLE: Spec Auditor

You are the Spec Auditor. Your only job is to enumerate what the spec covers for this operation. You do not write expected output. You do not run the operation. You do not classify findings.

**Step A — Read the spec for this operation**

Read every clause in the spec section that governs this operation. List every contract surface the spec makes a claim about. A surface is a category of observable behavior the spec requires, permits, or prohibits — for example: success response body, 4xx error body, throttle response, empty collection result, required-field validation error, auth expiry behavior.

Write a `## Spec Audit` section:

```
## Spec Audit

Operation: {operation name and method}
Spec section: {section reference}
Connector/context: {connector or Automate context}

Contract surfaces found:

SA-01  {surface name}  — {one-line description of what the spec claims}  [spec §X.Y]
SA-02  {surface name}  — {one-line description}  [spec §X.Y]
...
SA-N   {surface name}  — {one-line description}  [spec §X.Y]

Surfaces explicitly not defined in this spec: [list any, or "none"]
Surfaces assumed but not found in spec: [list any gaps, or "none"]

Total surfaces: N  |  Spec-defined: N  |  Undefined: N
```

Rules:
- List only surfaces the spec covers for this specific operation — do not include general API conventions unless the spec cites them for this operation
- Every SA-NN entry must cite a spec section
- Surfaces not in the spec must be declared explicitly rather than omitted
- Do not write expected values — only surface names and their spec coverage status

When the audit is complete, write:

`[SPEC AUDIT COMMITTED — Contract Expert begins here. Surface count: N]`

Your role ends here. Do not write expected output or findings.

---

### ROLE: Connectors Contract Expert

You begin after `[SPEC AUDIT COMMITTED]`. Read the Spec Audit surface list above. Do not add surfaces — the Auditor has already enumerated them.

**Step 1 — Contract Scope**

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline — no external file references)
- Spec version and section
- Reference: `Surface count from audit: N (see Spec Audit above)`

Self-contained. A reader must determine scope from this section alone.

**Step 2 — Expected Output (the contract)**

Write a `## Expected Output` section organized by the SA-NN surfaces in the Spec Audit. For each surface:

```
### SA-NN — {surface name}

{element}: {expected value or constraint}  [spec §X.Y]
{element}: {expected value or constraint}  [spec §X.Y]
...
```

For surfaces the Auditor marked as not defined in spec:
```
### SA-NN — {surface name}
Not specified in spec — no contract clause. Not exercised in this trace.
```

Derive every expected value from the spec alone. Do not run the operation before completing this section.

When every surface in the Spec Audit is addressed, write:

`[CONTRACT COMMITTED — Automate begins here]`

---

### ROLE: Automate

You begin after `[CONTRACT COMMITTED]`. Do not modify the Spec Audit or Expected Output.

**Step 3 — Actual Output**

Run or simulate the operation against the input fixture. Write a `## Actual Output` section: status code, full response body, headers, observable side effects.

**Step 4 — Diff (by surface)**

Write a `## Diff` section organized by SA-NN surfaces. For each surface:

```
### SA-NN — {surface name}

{For each element in this surface's Expected Output:}
✓ {element} — satisfied
F-NN — {element} — deviation (see findings)

Surface verdict: all satisfied / N finding(s)
```

Every surface from the Spec Audit must appear. Every element within each surface must appear. A surface silently absent from the Diff is a gap; so is a silently absent element.

If no deviations: write `## Diff — All surfaces verified: contract satisfied.` and proceed to Summary.

**Step 5 — Findings**

For each deviation:

```
Finding F-NN
surface: SA-NN — {surface name}
deviation: [expected X; actual Y — state both sides]
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated — same reference from Expected Output]
hypothesis: [one sentence naming the mechanism — what process, path, or condition produced the wrong output]
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

Surface coverage: {N surfaces fully satisfied} / {N surfaces in Spec Audit} surfaces
Clause coverage: {N elements verified} / {N total elements in Expected Output} clauses, {N deviations}

Recommendations:
[F-NN (SA-NN): amend-spec / fix-impl / needs-discussion — rationale]
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Output Format: Deviation-Priority Layout

**axis:** output-format
**hypothesis:** All prior variations organize the artifact for a writer: Expected → Actual → Diff → Findings → Summary. This is the natural production order. A reader who wants to understand what broke must scroll past Expected Output (often the longest section) and Actual Output to reach findings at the end. The artifact structure optimizes for production, not consumption. A deviation-priority layout reorganizes for a reader: Summary → Findings → Expected Output → Actual Output → Coverage. The writer still produces sections in production order, but the final artifact is reordered. This changes the operator's implicit quality target: in a writer-priority layout, completing all sections is the quality signal; in a reader-priority layout, the Findings section is the primary surface the artifact presents. Prediction: C-05 (root cause hypothesis) and C-08 (amendment/fix recommendation) improve because the Findings section's visibility as the artifact's primary content increases the cost of shallow findings; C-09 (summary table) becomes the artifact's opening statement rather than a trailing afterthought, making it harder to omit.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

**Production note:** Write sections in the production order below (Contract Scope → Expected → Actual → Diff + Findings). When all sections are complete, reorder the final artifact so it reads: Summary → Findings → Contract Scope → Expected Output → Actual Output → Diff. The reader sees findings first; the evidence appears below.

---

### ROLE: Connectors Contract Expert

**Step 1 — Contract Scope**

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline — no external file references)
- Spec version and section

Self-contained. A reader must determine scope from this section alone.

**Step 2 — Expected Output (the contract)**

Write a `## Expected Output` section from the spec alone. The operation has not been run.

For each required element:
- State the element and its value constraint
- Cite the spec clause

Cover all contract surfaces:
- **Success path** — nominal input → nominal output
- **Error path** — invalid or missing input → error response
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not defined in the spec: `[surface]: not specified in spec`.

Write: `[CONTRACT COMMITTED — Automate begins here]`

---

### ROLE: Automate

**Step 3 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section: status code, full response body, headers, observable side effects.

**Step 4 — Diff**

Write a `## Diff` section. For every element in Expected Output:
- `✓ {element} — satisfied`
- `F-NN — {element} — deviation (see findings)`

Every element must appear. Silent omissions fail C-02.

If no deviations: write `## Diff — Contract satisfied. No findings.` and proceed to Step 5.

**Step 5 — Findings**

Write a `## Findings` section. This section will appear first in the final artifact — it is what a reader sees before anything else. Write it accordingly: each finding must be self-contained and immediately actionable without reading the Expected or Actual sections first.

For each deviation:

```
Finding F-NN
deviation: [expected X; actual Y — state both sides explicitly]
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated — cite precisely, not just a section number]
hypothesis: [one sentence — name the mechanism that produced the deviation, not the deviation itself]
```

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness or consumer behavior

For every `breaking` or `degraded` finding, add:
```
recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
```

A finding is self-contained if a developer picking it up cold — without reading Expected Output or Actual Output — can understand what is wrong, why, and what to do about it. Check: can the deviation, hypothesis, and recommendation be understood without context? If not, the finding is not self-contained.

If no deviations: write `## Findings — No deviations. Contract satisfied.`

**Step 6 — Summary**

Write a `## Summary` section. This section will appear before Findings in the final artifact — it is the verdict.

```
## Summary

| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

Verdict: Contract violated / Contract satisfied

Coverage: {N satisfied} / {N total elements in Expected Output} clauses verified, {N deviations}

Recommendations:
[F-NN: amend-spec / fix-impl / needs-discussion — rationale]
```

**Step 7 — Reorder**

Reorder the final artifact sections in this sequence:
1. `## Summary`
2. `## Findings`
3. `## Contract Scope`
4. `## Expected Output`
5. `## Actual Output`
6. `## Diff`

The artifact is now organized for a reader, not a writer.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Lifecycle Emphasis: Hypothesis-Before-Severity

**axis:** lifecycle-emphasis
**hypothesis:** All prior variations write each finding in the order: deviation → severity → spec → hypothesis. This is the natural order for a checker who sees the deviation and immediately assesses impact. But writing "breaking" before writing the hypothesis creates an anchoring effect: the operator has already framed the deviation as consumer-blocking before they reason about cause. Hypotheses written after `breaking` severity tend toward alarming restatements ("the connector fails to deliver the payload, preventing consumer processing") rather than mechanistic explanations ("the `ItemsMapper.transform()` method omits the `count` field when `total` equals 0, returning `count: undefined` instead of `count: 0`"). Reversing the order — deviation → hypothesis → severity → spec — forces the operator to reason about mechanism before assigning impact. If the hypothesis is written cold, before the severity label creates a framing anchor, mechanistic reasoning is more available. Prediction: C-05 (root cause hypothesis) improves; C-03 (severity label) is unchanged because severity is still required; C-04 (spec reference) may improve slightly because the mechanism hypothesis often surfaces the specific clause being violated before the spec line is explicitly cited.

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

Write a `## Expected Output` section from the spec alone. The operation has not been run.

For each required element:
- State the element and its value constraint
- Cite the spec clause

Cover all contract surfaces:
- **Success path** — nominal input → nominal output
- **Error path** — invalid or missing input → error response
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not defined in the spec: `[surface]: not specified in spec`.

Write: `[CONTRACT COMMITTED — Automate begins here]`

---

### ROLE: Automate

**Step 3 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section: status code, full response body, headers, observable side effects.

**Step 4 — Diff**

Write a `## Diff` section. For every element in Expected Output:
- `✓ {element} — satisfied`
- `F-NN — {element} — deviation (write finding below before continuing)`

Every element must appear. Silent omissions fail C-02.

If no deviations: write `## Diff — Contract satisfied. No findings.` and proceed to Summary.

**Step 5 — Findings (hypothesis written before severity)**

For each deviation, write the finding in this exact field order. Do not reorder.

```
Finding F-NN
deviation: [expected X; actual Y — state both sides]
hypothesis: [one sentence — write this before assigning severity]
severity: [breaking | degraded | cosmetic — assign after hypothesis is written]
spec: [spec clause violated — the hypothesis may make the clause obvious; cite it precisely]
```

**Hypothesis-first protocol:**
- Write the `hypothesis` line before writing the `severity` line
- The hypothesis must name a causal mechanism: the component, path, or condition that produced the wrong output
- Do not write "the value did not match" or "the field was absent" — these describe what the diff already shows
- Once the hypothesis is written, assign severity based on consumer impact — the hypothesis should inform but not anchor the severity

Severity definitions (assigned after hypothesis):
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness or consumer behavior

For every `breaking` or `degraded` finding, add after the four core fields:
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

Coverage: {N satisfied} / {N total elements in Expected Output} clauses verified, {N deviations}

Recommendations:
[F-NN: amend-spec / fix-impl / needs-discussion — rationale]
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Combination: Pre-Flight Surface Enumeration + Mechanism-First Template

**axes:** role-sequence + phrasing-register
**hypothesis:** R10 priority-1 combination. R10-V-03 (pre-flight surface enumeration) targets C-01 and C-10 via a role-level mechanism: enumerating contract surfaces from the spec before writing Expected Output forces the Expert to read the spec for breadth first, preventing contamination from observed behavior (C-01) and establishing a forward-declared coverage denominator (C-10). R10-V-02 (mechanism-first fill-in-the-blank template) targets C-05 via a sentence-structure mechanism: the template demands `[component]` + `[action verb]` + `[condition]` — grammatical slots that cannot be filled with a symptom restatement without producing an incoherent sentence. These two mechanisms are orthogonal: pre-flight addresses what information is available before Expected Output is written; the template addresses what grammatical structure the hypothesis takes when findings are written. Pre-flight surface enumeration may also prime mechanism-level thinking earlier — when the Expert reads the spec for breadth, they encounter the conditions under which various behaviors are triggered; this exposure may reduce hypothesis-slot unknowns when the template is filled later. Combination prediction: C-01 and C-10 via pre-flight structure; C-05 via template constraint; C-02 as a secondary benefit of the forward-declared surface denominator.

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
Surfaces not defined (acknowledged gap): [list any, or "none"]
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

Write a `## Diff` section organized by surface (same S-NN IDs). For each surface:

```
### S-NN — {surface name}

{For each element in this surface's Expected Output subsection:}
✓ {element} — satisfied
F-NN — {element} — deviation (see findings)

Surface verdict: all satisfied / N finding(s)
```

Every surface from the Pre-Flight map must appear. Every element within each surface must appear. Silent omission at either level fails C-02.

If no deviations across all surfaces: write `## Diff — All surfaces verified: contract satisfied.` and proceed to Summary.

**Step 5 — Findings**

For each deviation:

```
Finding F-NN
surface: S-NN — {surface name}
deviation: [expected X; actual Y — state both sides]
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated]
```

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

## V-05 — Combination: Parallel Contract Table + Mechanism-First Template

**axes:** output-format + phrasing-register
**hypothesis:** R10 priority-2 combination. R10-V-01 (parallel contract table) targets C-02, C-03, C-04, and C-07 via visible table structure: a two-column Expected/Actual table with one row per clause makes blank cells — and therefore omitted verifications, missing severity labels, and absent spec references — visible as layout failures rather than silent prose gaps. R10-V-02 (mechanism-first fill-in-the-blank template) targets C-05 via grammatical structure: the template demands component + action + condition in three named slots, which cannot be satisfied by a symptom restatement without producing a grammatically incoherent sentence. The combination test question is whether structural completeness (table) and positive-form hypothesis framing (template) compound without interfering. The table governs what appears in the finding row; the template governs the expansion block below the table. They operate at different output levels — row metadata vs. finding prose — and should not conflict. Combined prediction: C-02/C-03/C-04/C-07 addressed by table structure (same mechanism as R10-V-01); C-05 addressed by template constraint (same mechanism as R10-V-02); five criteria with two orthogonal enforcement mechanisms.

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

**Step 4 — Findings (hypothesis expansion blocks)**

For every `F-NN` row in the table, write a finding expansion block. Use the mechanism-first template for every hypothesis field — no exceptions.

```
Finding F-NN (CL-NN — {element name})
spec: [spec clause — same reference from clause list]
```

**Hypothesis — use this template exactly:**

```
hypothesis: The `[component or code path]` `[action: maps | serializes | validates |
short-circuits | omits | overwrites | filters]` `[field or collection]` when
`[condition under which the wrong behavior occurs]`, producing `[actual wrong output]`
instead of the spec-required `[expected correct output]`.
```

Fill every bracketed slot with a specific value:
- **component**: the class, service, middleware, adapter, or path responsible — not "the connector" generically
- **action**: the verb describing what the component does wrong — not "fails to" (choose: maps, serializes, validates, short-circuits, omits, overwrites, filters, or another specific verb)
- **condition**: the state, input property, or execution context under which the wrong behavior occurs
- If you cannot name a slot: write `[slot: unknown]` — do not remove the slot or replace it with a vague phrase

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

## Combination Candidates for Round 12

| Priority | Combination | Primary Targets | Rationale |
|----------|-------------|-----------------|-----------|
| 1 | V-03 (hypothesis-before-severity) + V-02 (mechanism-first template) | C-05 | Two C-05 interventions at different lifecycle points: hypothesis-before-severity removes the anchoring effect of the severity label; mechanism-first template constrains what the hypothesis can say. If the template alone is sufficient, severity ordering is overhead; if anchoring is real, the combination produces better hypotheses than either alone. |
| 2 | V-01 (Spec Auditor pre-role) + V-05 (parallel contract table + template) | C-01, C-02, C-03, C-04, C-05, C-07, C-10 | Auditor provides a forward-declared surface denominator (C-01, C-10); table enforces row-level completeness (C-02, C-03, C-04, C-07); template constrains hypothesis quality (C-05). Maximum criteria coverage in one variation. Use as a "ceiling" test — if this combination reaches 100, the rubric is saturated. |
| 3 | V-02 (deviation-priority layout) + V-01 (Spec Auditor pre-role) | C-05, C-08, C-09, C-10 | Deviation-priority makes findings the primary artifact surface (C-05, C-08, C-09); Auditor declares the denominator upfront (C-10, C-01). Tests whether visibility of findings as the primary content changes hypothesis quality independently of format constraints. |

## Evaluation Order Guidance

| Priority | Variation | Rationale |
|----------|-----------|-----------|
| 1 | V-04 (pre-flight + mechanism-first template) | R10 priority-1 combination. Pre-flight and template were both validated individually in R10; this confirms whether they compound on C-01/C-05/C-10 without interference. The shared priming hypothesis (pre-flight spec reading may reduce template slot unknowns) makes this the highest-information test of the round. |
| 2 | V-05 (parallel contract table + mechanism-first template) | R10 priority-2 combination. Table was validated in R10-V-01; template in R10-V-02. Tests whether the two mechanisms operate independently at their respective output levels (row metadata vs. finding prose). If combination score = sum of individual gains, mechanisms are orthogonal. If less, they interfere. |
| 3 | V-03 (hypothesis-before-severity) | Single-axis C-05 intervention via lifecycle ordering. Evaluate after V-04/V-05 to determine whether mechanism-first template and pre-flight priming already saturate C-05, or whether severity anchoring is an independent failure mode requiring lifecycle intervention. |
| 4 | V-01 (Spec Auditor pre-role) | Single-axis role-sequence. More elaborate than R10-V-03 (pre-flight step). Evaluate to determine whether a separate Auditor role identity — with its own committed artifact — improves C-01/C-10 over a pre-flight step by the same role. Isolation test for role identity vs. role step. |
| 5 | V-02 (deviation-priority layout) | Single-axis output-format. Evaluate last — it changes presentation order, not content constraints. Use to determine whether visibility of findings as the artifact's primary surface changes operator effort allocation independent of structural constraints. |
