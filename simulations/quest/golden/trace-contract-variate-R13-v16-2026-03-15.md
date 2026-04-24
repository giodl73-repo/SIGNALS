# trace-contract Variate — Round 13 (Rubric v16)

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v16 (C-01–C-10; essential C-01–C-05; golden threshold: all essential pass + composite >= 80)
**Round:** R13 — 3 new single-axis + 2 priority combinations from R12-v16 recommendation list

---

## Round 13 Variation Map

| Variation | Axis | Primary Targets | Hypothesis |
|-----------|------|-----------------|------------|
| V-01 | output-format (per-element ledger / inline E-A-S triplets) | C-02, C-07 | Replacing three-section structure with per-element inline triplets makes blank A lines visually adjacent to filled E lines — omissions register as layout breaks, not content gaps that can hide in section summaries |
| V-02 | phrasing-register (anti-pattern exemplars — show bad before good) | C-05 | Showing a concrete bad hypothesis immediately before the instruction changes the cognitive task from "satisfy the requirement" to "don't write the thing I just read"; the bad example creates a comparison anchor that makes symptom restatements recognizable in the operator's own writing |
| V-03 | role-sequence (Deviation Analyst — finding-writing separated from diff-production) | C-05, C-03, C-04 | When a single operator does both mechanical diff and finding-writing, their attention is divided between "did the value match?" and "why didn't it match?"; a Deviation Analyst who receives only the F-NN list — not the full diff context — writes hypotheses without the satisficing pressure of having just performed mechanical comparison |
| V-04 | inertia-framing + hypothesis-before-severity + mechanism-first template (R12 priority-1) | C-05 | Three independent C-05 interventions at different points: motivational (inertia names downstream cost of shallow hypotheses), ordering (writing before severity removes the label from the hypothesis-writing context), structural (template slots cannot be filled with symptom restatements without producing incoherent sentences) |
| V-05 | phase-gate checks + Spec Auditor + table + template (R12 priority-2) | C-01, C-02, C-03, C-04, C-05, C-07, C-10 | Ceiling test: gate lifecycle discipline (R12-V-03) combined with structural enforcement (R12-V-05). Gates confirm phase completion at each transition; Auditor + table make omissions visible as layout failures. Tests whether explicit gate confirmation adds value over structural visibility alone, and whether together they saturate the full essential + recommended surface |

---

## V-01 — Output Format: Per-Element Ledger

**axis:** output-format (inline E-A-S triplets per element; no separate Expected / Actual / Diff sections)
**hypothesis:** All prior variations use three distinct sections — Expected Output, Actual Output, Diff — with elements listed once per section. This structure allows a Diff section to silently omit elements: a short Diff that says "no issues on success path" can satisfy the casual reader without covering every element. The omission is not structurally visible unless the reader counts elements across sections. Per-element inline triplets eliminate the gap: each element appears as a single block with three adjacent lines — E (expected from spec), A (actual observed), S (status). A blank A line is immediately adjacent to a filled E line; the omission is a visual break in the local block, not a missing entry in a distant section. This also maps explicitly to the three-directory pattern: E lines correspond to 20-expected, A lines to 30-actual, S lines to the diff. Three-directory layers are present in the format by construction, not by label alone. Prediction: C-02 (diff completeness, no silent omissions) improves because omissions are structurally visible at the element level; C-07 (three-directory explicit) improves because the column semantics of E/A/S name the three layers in every element block.

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
- Input fixture (inline — no external file references — the artifact must be self-contained)
- Spec version and section governing this operation's output contract

**Step 2 — Element Inventory (the contract — operation not yet run)**

Write a `## Element Inventory` section. Derive every element from the spec alone. The operation must not be run until the inventory is complete and `[CONTRACT COMMITTED]` is written.

Organize elements by contract surface:

```
## Element Inventory

### Surface: Success Path
[10-INPUT] fixture: {describe input state}

E: {element-1 name}: {expected value or constraint}  [spec §X.Y]
E: {element-2 name}: {expected value or constraint}  [spec §X.Y]
...

### Surface: Error Path
[10-INPUT] fixture: {describe error-trigger input}

E: {element name}: {expected value or constraint}  [spec §X.Y]
...

### Surface: Edge Case — {name the edge case}
[10-INPUT] fixture: {describe edge-case input}

E: {element name}: {expected value or constraint}  [spec §X.Y]
...
```

Rules:
- Every E line must cite a spec clause in `[spec §X.Y]` form. An E line without a spec citation is not a valid contract entry.
- Cover at minimum: success path, one error path, one edge case (empty collection, null required field, rate-limit trigger, or auth expiry).
- If a surface is not defined in the spec: `E: [surface name]: not specified in spec — no contract clause`.

When every surface is enumerated, write: `[CONTRACT COMMITTED — Automate begins here]`

---

### ROLE: Automate

You begin after `[CONTRACT COMMITTED]`. Do not modify the Element Inventory.

**Step 3 — Actual Output and Inline Diff**

Run or simulate the operation. For each surface, return to the Element Inventory block and fill in A and S lines below every E line.

```
### Surface: Success Path
[10-INPUT] fixture: {same as above}

E: {element-1 name}: {expected value}  [spec §X.Y]
A: {element-1 name}: {actual observed value}             [30-ACTUAL]
S: satisfied / F-01

E: {element-2 name}: {expected value}  [spec §X.Y]
A: {element-2 name}: {actual observed value}             [30-ACTUAL]
S: satisfied / F-02
```

Column semantics:
- **E** (20-expected): the spec-derived expected value — written by Contract Expert; do not modify
- **A** (30-actual): the value the operation actually produced for this element — write it even if it matches E
- **S** (status): `satisfied` if A matches E; `F-NN` (e.g., F-01) if it deviates

**Do not leave any A line blank.** A blank A line means the element was not verified. If you cannot verify an element, write `A: [not verifiable — reason]`. Silent absence fails C-02.

After completing all surfaces, if no deviations exist: write `[ALL SURFACES SATISFIED — proceed to Summary]` and skip to Step 5.

**Step 4 — Findings**

For each `F-NN` status line, write a finding expansion block:

```
Finding F-NN
element: {element name} — {surface name}
deviation: expected {X}; actual {Y} — state both sides explicitly
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated]
hypothesis: [one sentence — name the mechanism: which component, path, or condition produced the wrong output — not what the diff shows, but why it happened]
```

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness or consumer behavior

For every `breaking` or `degraded` finding:
```
recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
```

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

Coverage: {N satisfied E lines} / {N total E lines across all surfaces} elements verified, {N deviations}

Recommendations:
[F-NN: amend-spec / fix-impl / needs-discussion — rationale]
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Phrasing Register: Anti-Pattern Exemplars

**axis:** phrasing-register (show concrete bad examples immediately before each critical instruction)
**hypothesis:** All prior variations describe the desired output and label anti-patterns ("a restatement of the deviation is not valid"), but none show a concrete bad example adjacent to the instruction. The cognitive difference matters: reading "do not restate the symptom" requires the operator to generate their own mental model of what a bad hypothesis looks like and compare their output against that self-generated model. Reading a concrete bad example creates an external comparison anchor — the operator's hypothesis is compared against a vivid, remembered specimen of the failure mode rather than an abstract description. A bad example immediately before the hypothesis instruction also primes the recognition task: when the operator's draft hypothesis resembles the bad example they just read, that resemblance is detectable. Prediction: C-05 (root cause hypothesis depth) improves because the bad example makes symptom restatements recognizable in the operator's own writing at the moment of writing; C-01 (expected-first) improves because a bad example of observational contamination ("I'll write Expected as 200 OK because that's what I saw") is harder to act on once named.

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

**Step 2 — Expected Output (the contract)**

> **Before writing:** Here is the failure mode this step prevents.
>
> **Bad practice:** Running the operation, observing that it returns a 200 with `{"items": [], "count": 0}`, then writing: `E: status code: 200` and `E: body.count: 0` — because those are the values you just observed.
>
> **Why it fails:** You have written the implementation's behavior as the expectation. If the spec says count is required but the implementation returns it only when nonzero, you have just encoded the bug as the contract. The Expected Output section must be derived from the spec alone.
>
> Write the Expected Output section **before** running the operation. If you have already run the operation, do not proceed — you must discard what you observed and derive the expected values from the spec text.

Write a `## Expected Output` section. The operation has not been run.

For each required element:
- State the element and its expected value or constraint
- Cite the spec clause

Cover all contract surfaces:
- Success path — nominal input → nominal output
- Error path — invalid or missing input → error response
- At least one edge case — empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not defined in the spec: `[surface]: not specified in spec — no contract clause exists`.

Write: `[CONTRACT COMMITTED — Automate begins here]`

---

### ROLE: Automate

**Step 3 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section: status code, full response body, headers, observable side effects.

**Step 4 — Diff**

Write a `## Diff` section. For every element in Expected Output:
- `✓ {element} — satisfied`
- `F-NN — {element} — deviation (write finding below)`

Every element must appear. Silent omissions fail C-02. If you cannot verify an element, write: `{element} — not verified: [reason]`.

If no deviations: write `## Diff — Contract satisfied. No findings.` and proceed to Summary.

**Step 5 — Findings**

> **Before writing each hypothesis:** Here is the failure mode this step prevents.
>
> **Bad hypothesis:** "The count field was absent from the response body."
>
> **Why it fails:** This is a symptom restatement. It tells the next engineer exactly what the diff already shows. It does not tell them where to look, what component to inspect, or under what condition the behavior changes. A developer debugging this finding still starts from zero.
>
> **Good hypothesis:** "The `ItemsSerializer.toResponse()` method omits `count` from the serialized object when `items.length === 0`, because the serialization block is guarded by a `length > 0` check that short-circuits before the field assignment."
>
> **Why it works:** A developer can go directly to `ItemsSerializer.toResponse()`, find the guard condition, and confirm or disprove the hypothesis within minutes. Even if the hypothesis names the wrong component, it names a specific mechanism and a testable condition — the developer knows what kind of thing to look for.
>
> Your hypothesis must name: (1) a specific component, class, or code path — not "the connector" generically; (2) the specific action it performs wrongly; (3) the condition under which the wrong behavior occurs.

For each deviation:

```
Finding F-NN
deviation: [expected X; actual Y — state both sides]
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated]
hypothesis: [one sentence — name the mechanism, not the symptom]
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

Coverage: {N satisfied} / {N total elements in Expected Output} clauses verified, {N deviations}

Recommendations:
[F-NN: amend-spec / fix-impl / needs-discussion — rationale]
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Role Sequence: Deviation Analyst (finding-writing separated from diff-production)

**axis:** role-sequence (three-role separation: Contract Expert owns expected; Automate owns diff; Deviation Analyst owns findings)
**hypothesis:** All prior variations assign diff-production and finding-writing to the same role (Automate). When a single operator performs mechanical matching ("did status code equal 200?") immediately before writing a finding for a mismatch, the matching task primes a comparison mindset — the operator has just verified field equality, and their next thought is the converse inequality ("it was 201 instead of 200"). This primes symptom restatement as the natural next sentence. A Deviation Analyst who receives only a list of F-NN deviations (element name + expected + actual) — without having performed the mechanical matching — writes findings without that satisficing pressure. The Analyst's cognitive state is: "here is a deviation, what caused it?" rather than "here is a deviation, having just confirmed it differs from expected." Separation also sharpens role accountability: Automate's only job is complete mechanical enumeration (C-02); the Analyst's only job is diagnostic quality (C-05, C-03, C-04). Role separation creates a specialization pressure that neither role experiences when combined. Prediction: C-05 (hypothesis depth) improves because the Analyst writes hypotheses without being anchored to the mechanical comparison just completed; C-02 (diff completeness) improves because Automate's sole accountability for the diff removes the competing cognitive load of finding-writing.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate + Deviation Analyst.

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
- State the element and its expected value or constraint
- Cite the spec clause

Cover all contract surfaces:
- Success path — nominal input → nominal output
- Error path — invalid or missing input → error response
- At least one edge case — empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not defined in the spec: `[surface]: not specified in spec — no contract clause exists`.

Write: `[CONTRACT COMMITTED — Automate begins here]`

Your role ends here.

---

### ROLE: Automate

Your role is mechanical: observe and compare. Do not write findings. Do not write severity labels. Do not write hypotheses. Your job is complete enumeration of every element and its comparison result.

**Step 3 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section: status code, full response body, headers, observable side effects.

**Step 4 — Diff**

Write a `## Diff` section. For every element in Expected Output, write one of:
- `✓ {element} — expected: {value}; actual: {value} — satisfied`
- `F-NN — {element} — expected: {expected value}; actual: {actual value} — deviation`

Every element from Expected Output must appear. Silent omissions are not acceptable — if you cannot verify an element, write `{element} — not verified: [reason]`.

Rules for this step:
- Do not write severity labels. Do not write hypotheses. That is the Analyst's job.
- Do not write "no issues found" as a surface-level summary. Enumerate every element individually.
- If no deviations exist: write `## Diff — Contract satisfied. All elements verified. No deviations.` and proceed to Step 5.

**Step 5 — Deviation Handoff**

If deviations exist, write a `## Deviation Handoff` section. For each F-NN, write only:

```
F-NN
element: {element name}
surface: {success path / error path / edge case name}
expected: {expected value — copy from Expected Output}
actual: {actual value — copy from Actual Output}
```

Do not add interpretation. Do not add context. The Analyst will read the deviation and the Contract Scope. That is all the Analyst needs.

Write: `[DIFF COMMITTED — Deviation Analyst begins here. Findings count: N]`

Your role ends here.

---

### ROLE: Deviation Analyst

You begin after `[DIFF COMMITTED]`. Read the Contract Scope, the Expected Output, and the Deviation Handoff. Do not modify any prior section.

Your job is diagnostic quality: for each deviation in the Handoff, write a finding that classifies the deviation, anchors it to a spec obligation, and identifies the mechanism that produced it.

**Step 6 — Findings**

For each F-NN in the Deviation Handoff:

```
Finding F-NN
deviation: [expected X; actual Y — restate both sides for completeness]
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated — identify the specific clause from the Expected Output or spec source that this deviation violates]
hypothesis: [one sentence — name the causal mechanism: which component, path, or condition produced the wrong output — not a restatement of the diff, but why it happened]
```

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness or consumer behavior

For every `breaking` or `degraded` finding:
```
recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
```

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

Coverage: {N satisfied elements} / {N total elements in Expected Output} elements verified, {N deviations}

Recommendations:
[F-NN: amend-spec / fix-impl / needs-discussion — rationale]
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Combination: Inertia Framing + Hypothesis-Before-Severity + Mechanism-First Template

**axes:** inertia-framing + lifecycle-emphasis + phrasing-register (R12 priority-1 combination)
**hypothesis:** R12 identified this as the top-priority combination for R13. Three independent interventions targeting C-05 at different points in the finding-writing process. Intervention 1 (motivational, from R12-V-01): naming the status-quo failure mode at the hypothesis phase boundary — "without a hypothesis, the next engineer starts from zero" — grounds the hypothesis requirement in a concrete downstream cost rather than an abstract criterion. An operator who understands what a shallow hypothesis costs downstream writes a different kind of hypothesis than one following a formatting requirement. Intervention 2 (ordering, from R12-V-04): writing the hypothesis before severity removes the severity label from the attention context during hypothesis writing. Writing "breaking" first primes impact restatement — "the connector fails, preventing consumer processing" — rather than mechanism identification — "the ItemsMapper omits count when items is empty." Writing deviation → hypothesis → severity keeps the operator's focus on causation during the hypothesis step. Intervention 3 (structural, from R12-V-04): the mechanism-first template (`[component] [action] [field] when [condition]`) cannot be filled with a symptom restatement without producing a grammatically incoherent sentence. The slots demand a specific component name, a specific action verb, and a specific triggering condition. These three interventions are orthogonal: motivation changes why the operator cares; ordering changes what information is in attention; template changes what form the output can take. If template alone saturates C-05 by R12-V-04 evaluation, motivation and ordering are overhead. If anchoring (severity-before-hypothesis) is an independent failure mode, the ordering constraint adds value beyond template alone. Combined prediction: C-05 improves over either single-axis intervention via three independent causal paths.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

**Why this skill exists — the status-quo baseline:**

Without a contract trace, connector verification is "run it and see." The operation runs, output is inspected, mismatches are noted if noticed. No spec-derived expectation. No field-level diff. No severity classification. No documented hypothesis. Contract violations that are subtle or conditional survive until integration testing or production. Each section of this artifact closes a specific gap in that baseline:

- **Expected Output first** — without this, observed behavior substitutes for spec. Implementation drift is silent.
- **Field-level Diff** — without it, unchecked elements cannot be distinguished from verified elements.
- **Severity labels** — without them, a cosmetic formatting difference and a breaking data loss look identical.
- **Root cause hypothesis** — without it, a finding is a symptom report. The next engineer who encounters this deviation starts from zero. The hypothesis names the mechanism so the fix search begins at the cause, not at the deviation.
- **Spec reference** — without it, a finding reads as a preference, not a contract violation.

Keep these failure modes in mind as you write. The hypothesis requirement exists because the alternative — a symptom report — costs the next engineer a full debug cycle.

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

*Without expected-first writing: observed behavior will contaminate what you write as expected. The Expected section must be derived from the spec alone — not from what you observed.*

Write a `## Expected Output` section. The operation has not been run.

For each required element:
- State the element and its expected value or constraint
- Cite the spec clause

Cover all contract surfaces:
- Success path — nominal input → nominal output
- Error path — invalid or missing input → error response
- At least one edge case — empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not defined in the spec: `[surface]: not specified in spec — no contract clause exists`.

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

**Step 5 — Findings (inertia framing + hypothesis-before-severity + mechanism-first template)**

*Why the hypothesis matters: without a mechanism hypothesis, this finding is a symptom report. The next engineer who encounters this deviation starts from zero — they know what differed, but not where the fault is or under what condition it occurs. A hypothesis that names the component, action, and condition reduces the debug cycle from hours to minutes. Write it as if you are handing the finding to a developer who will spend their next 30 minutes investigating it.*

For each deviation, write the fields in **exactly this order**. Do not reorder.

```
Finding F-NN
deviation: [expected X; actual Y — state both sides]
```

**Write the hypothesis next — before assigning severity.**

Severity framing anchors hypothesis writing. Writing "breaking" before writing the hypothesis primes impact restatement: "the connector fails, preventing consumer processing." Writing the mechanism first — then severity — keeps the causal analysis isolated from impact framing.

**Use this template exactly. Fill every bracketed slot.**

```
hypothesis: The `[component or code path]` `[action: maps | serializes | validates | short-circuits | omits | overwrites | filters]` `[field or collection]` when `[condition under which the wrong behavior occurs]`, producing `[actual wrong output]` instead of the spec-required `[expected correct output]`.
```

Slot rules:
- **component**: the class, service, middleware, adapter, or code path responsible — not "the connector" generically
- **action**: the verb naming what the component does wrong — not "fails to" (choose: maps, serializes, validates, short-circuits, omits, overwrites, filters, or another specific verb)
- **condition**: the state, input property, or execution context under which the wrong behavior occurs
- If you cannot name a slot: write `[slot: unknown]` — do not remove the slot

After writing the hypothesis, assign severity based on consumer impact. Let the hypothesis inform the severity assessment; do not retroactively revise the hypothesis to match the label.

```
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated]
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

Coverage: {N satisfied} / {N total elements in Expected Output} clauses verified, {N deviations}

Recommendations:
[F-NN: amend-spec / fix-impl / needs-discussion — rationale]
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — Combination: Phase Gates + Spec Auditor + Table + Template

**axes:** lifecycle-emphasis + role-sequence + output-format + phrasing-register (R12 priority-2 combination — ceiling test)
**hypothesis:** R12 identified this as the ceiling test for R13 — maximum criteria coverage via four orthogonal mechanisms. Mechanism 1 (Spec Auditor, from R12-V-05): a pre-writing role enumerates every contract surface from the spec before a single expected value is written. This separates surface enumeration from expected value authorship and establishes the coverage denominator before verification begins. Addresses C-01 (expected-first via surface-driven authorship) and C-10 (coverage ratio denominator committed in writing before trace begins). Mechanism 2 (parallel contract table, from R12-V-05): one row per clause with Expected and Actual columns side by side. Blank cells in Actual, Result, or Severity are layout failures visible on document scan. Addresses C-02 (diff completeness — blank cells cannot be silent), C-03 (severity — every finding row has a Severity column), C-04 (spec reference via clause ID in every row), C-07 (three-directory — column headers name the layers). Mechanism 3 (mechanism-first template, from R12-V-04): slot structure prevents symptom restatement. Addresses C-05. Mechanism 4 (phase-gate checks, from R12-V-03): explicit cannot-proceed gates at each phase transition make lifecycle incompleteness a structural blocker auditable in the artifact. Addresses C-01 (Gate 2 prevents running before Expected committed) and C-02 (Gate 4 prevents findings before per-element diff complete). Four mechanisms are orthogonal and operate at different levels: Auditor role (pre-writing) → gate checks (phase transitions) → table structure (row metadata) → hypothesis template (finding prose). Ceiling prediction: if this combination fails a criterion, that criterion identifies a gap no prior v16 variation has addressed. Expected: all 5 essential + composite >= 90.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Spec Auditor + Connectors contract expert + Automate.

**Lifecycle discipline:** Each phase ends with a gate check. Write the gate check output explicitly in the artifact. Do not proceed to the next phase if the gate fails — return to the current phase and resolve what is missing.

---

### ROLE: Spec Auditor

Your only job is to enumerate what the spec covers for this operation. You do not write expected values. You do not run the operation. You do not classify findings.

**Phase A — Enumerate contract surfaces**

Read every clause in the spec section governing this operation. List every contract surface the spec makes a claim about. A surface is a category of observable behavior the spec requires, permits, or prohibits.

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
- Every SA-NN entry must cite a spec section
- Surfaces not in the spec must be declared explicitly — not omitted
- Do not write expected values — only surface names and their spec coverage status

**Gate A:**

```
[ GATE A CHECK ]
- [ ] Every surface in the spec is listed with a spec citation
- [ ] Surfaces not in the spec are declared explicitly
- [ ] No expected values appear in the Spec Audit
Gate A: PASS / FAIL — [if FAIL: what is missing]
```

Do not proceed to Phase 1 if Gate A fails.

Write: `[SPEC AUDIT COMMITTED — Contract Expert begins here. Surface count: N]`

Your role ends here.

---

### ROLE: Connectors Contract Expert

You begin after `[SPEC AUDIT COMMITTED]`. Read the Spec Audit surface list. Do not add surfaces the Auditor did not enumerate.

**Phase 1 — Contract Scope**

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline — no external file references)
- Spec version and section
- Surface count from audit: N (see Spec Audit above)

Self-contained. A reader must determine scope from this section alone.

**Phase 2 — Expected Clauses (spec-derived — operation not yet run)**

For every surface in the Spec Audit, enumerate every element the spec requires. Organize by SA-NN surface. Derive from the spec alone.

```
## Expected Clauses

### SA-01 — {surface name}
CL-01  {element name}: {expected value or constraint}  [spec §X.Y]
CL-02  {element name}: {expected value or constraint}  [spec §X.Y]

### SA-02 — {surface name}
CL-03  {element name}: {expected value or constraint}  [spec §X.Y]
...

### SA-NN — {surface name} [not in spec]
CL-N  [surface]: not specified in spec  [no clause]
```

**Gate 2:**

```
[ GATE 2 CHECK ]
- [ ] Every SA-NN surface appears as a clause group
- [ ] Every clause cites a spec section
- [ ] No clause was derived by observing the operation
- [ ] Input fixture is inline in Contract Scope (no external file reference)
Gate 2: PASS / FAIL — [if FAIL: which surface or element is missing]
```

Do not run the operation until Gate 2 passes.

Write: `[CONTRACT COMMITTED — clause list sealed — Gate 2 passed — Automate begins here]`

Your role ends here.

---

### ROLE: Automate

You begin after `[CONTRACT COMMITTED]`. Do not add to or modify the clause list.

**Phase 3 — Contract Comparison Table**

Run or simulate the operation against the input fixture. Produce the following table. Every clause in the Expected Clauses list must appear as a row. Do not skip rows.

```
## Contract Comparison (20-Expected vs. 30-Actual)

| CL-ID | Surface | Element | Expected (spec) | Actual (observed) | Result | Severity |
|-------|---------|---------|-----------------|-------------------|--------|----------|
| CL-01 | SA-01 | {name} | {spec value} | {observed value} | ✓ / F-NN | — / breaking / degraded / cosmetic |
| CL-02 | SA-01 | {name} | {spec value} | {observed value} | ✓ / F-NN | — / breaking / degraded / cosmetic |
...
| CL-N  | SA-NN | {name} | {spec value} | {observed value} | ✓ / F-NN | — / breaking / degraded / cosmetic |
```

Column rules:
- **Expected**: copy the expected value from the clause list — do not paraphrase
- **Actual**: state what the operation produced for this element — do not leave blank; write `[not verifiable: reason]` if you cannot verify
- **Result**: `✓` if actual satisfies expected; `F-NN` (e.g., F-01) if it deviates
- **Severity**: `—` for satisfied rows; exactly one of `breaking` / `degraded` / `cosmetic` for finding rows

A blank Actual cell means the element was not verified. A blank Severity cell on a finding row fails C-03. Neither is acceptable.

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness or consumer behavior

**Gate 4:**

```
[ GATE 4 CHECK ]
- [ ] Every CL-NN clause appears as a table row
- [ ] No Actual cell is blank
- [ ] Every F-NN row has a Severity value
- [ ] No elements are silently absent
Gate 4: PASS / FAIL — [if FAIL: which clause is absent or which cell is blank]
```

Do not proceed to Phase 4 if Gate 4 fails. Return to the table and complete missing rows or cells.

**Phase 4 — Findings (mechanism-first hypothesis template)**

For every `F-NN` row in the table, write a finding expansion block. Use the mechanism-first template for every hypothesis — no exceptions.

```
Finding F-NN (CL-NN — SA-NN — {element name})
spec: [spec clause — same reference from clause list]
```

**Hypothesis — use this template exactly. Fill every bracketed slot.**

```
hypothesis: The `[component or code path]` `[action: maps | serializes | validates | short-circuits | omits | overwrites | filters]` `[field or collection]` when `[condition under which the wrong behavior occurs]`, producing `[actual wrong output]` instead of the spec-required `[expected correct output]`.
```

Slot rules:
- **component**: the class, service, middleware, adapter, or code path responsible — not "the connector" generically
- **action**: the verb naming what the component does wrong — not "fails to"
- **condition**: the state, input property, or execution context under which the wrong behavior occurs
- If you cannot name a slot: write `[slot: unknown]` — do not remove the slot

For every `breaking` or `degraded` finding:
```
recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
```

If no findings: write `## Findings — No deviations. All clauses satisfied.`

**Gate 5:**

```
[ GATE 5 CHECK ]
- [ ] Every F-NN from the table has a finding expansion block
- [ ] Every hypothesis uses the mechanism-first template (all slots filled or marked unknown)
- [ ] Every breaking/degraded finding has a recommendation
Gate 5: PASS / FAIL — [if FAIL: which finding is incomplete]
```

Do not proceed to Phase 5 if Gate 5 fails.

**Phase 5 — Summary**

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
Clause coverage: {N satisfied rows} / {N total rows in table} clauses, {N findings}

Recommendations:
[F-NN (CL-NN, SA-NN): amend-spec / fix-impl / needs-discussion — rationale]
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## Combination Candidates for Round 14

| Priority | Combination | Primary Targets | Rationale |
|----------|-------------|-----------------|-----------|
| 1 | V-01 (per-element ledger) + V-04 (inertia + hypothesis-before-severity + template) | C-02, C-05, C-07 | Per-element ledger makes omissions structurally visible (C-02, C-07); hypothesis-before-severity + template addresses C-05. Two orthogonal structural mechanisms. Tests whether per-element format outperforms separate-section diff when combined with the strongest C-05 intervention available. |
| 2 | V-02 (anti-pattern exemplars) + V-03 (Deviation Analyst) | C-05 | Anti-pattern exemplars prime recognition of symptom restatements; Deviation Analyst role removes the diff-completion cognitive load during hypothesis writing. Both target C-05 via different mechanisms — motivational recognition (exemplar) vs. attentional isolation (role separation). Tests whether exemplar + isolation outperforms either alone, and whether together they saturate C-05 without a structural template. |
| 3 | V-01 (per-element ledger) + V-03 (Deviation Analyst) + V-05 (gates + Auditor + table + template) | C-01–C-10 | Ultra-ceiling test: per-element ledger replaces V-05's table format with inline triplets — tests whether the ledger format addresses C-02/C-07 more effectively than the table; Deviation Analyst separation is added on top of V-05's four-mechanism stack; gates + Auditor handle C-01/C-10. If this combination fails any criterion, that criterion identifies a structural gap no format or role variation can reach. |

## Evaluation Order Guidance

| Priority | Variation | Rationale |
|----------|-----------|-----------|
| 1 | V-04 (inertia + hypothesis-before-severity + template) | R12's priority-1 combination. Highest-information test: three independent C-05 interventions. If this does not outperform R12-V-04 (two-intervention baseline), motivation framing adds no C-05 value beyond ordering + template. |
| 2 | V-05 (gates + Auditor + table + template) | R12's priority-2 ceiling test. Four-mechanism stack. If this combination reaches all essential + composite >= 90, the v16 rubric is saturated by R12-era techniques. If it fails a criterion, that criterion identifies a gap this round cannot close. |
| 3 | V-03 (Deviation Analyst) | New single-axis: role separation for finding-writing. Evaluate after V-04/V-05 to isolate whether Analyst separation adds C-05 improvement beyond template constraint. If V-04 template saturates C-05, Analyst role is redundant. If attention-isolation is an independent failure mode, Analyst adds value. |
| 4 | V-02 (anti-pattern exemplars) | New single-axis: recognition priming. Evaluate after V-03 to determine whether exemplar-based priming changes hypothesis quality independently of structural constraints. Compare against V-04 template to isolate motivational vs. structural C-05 intervention. |
| 5 | V-01 (per-element ledger) | New single-axis: format change. Evaluate last — format variations are the most diffuse intervention. Compare against V-05 table to determine whether inline triplet structure outperforms parallel table for C-02/C-07 under this rubric. |
