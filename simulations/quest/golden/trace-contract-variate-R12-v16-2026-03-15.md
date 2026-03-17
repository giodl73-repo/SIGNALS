# trace-contract Variate — Round 12 (Rubric v16)

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v16 (C-01–C-10; essential C-01–C-05; golden threshold: all essential pass + composite >= 80)
**Round:** R12 — 3 new single-axis + 2 priority combinations from R11 recommendation list

---

## Round 12 Variation Map

| Variation | Axis | Primary Targets | Hypothesis |
|-----------|------|-----------------|------------|
| V-01 | inertia-framing (new) | C-01, C-05 | Naming the status-quo failure mode at each phase boundary grounds each section's purpose in a concrete consequence — operators who understand *why* expected-first prevents observational bias write better Expected sections; operators who understand *why* hypothesis matters for diagnosis write mechanistic hypotheses instead of symptom restatements |
| V-02 | phrasing-register (question-form / interrogative) | C-01, C-05, C-02 | Question-form register ("What does the spec require?") resists checkbox completion — you cannot satisfy a question with a section shape; questions that require spec retrieval force C-01 compliance; questions that ask "what caused this?" force C-05 causal reasoning rather than diff restatement |
| V-03 | lifecycle-emphasis (phase-gate checks) | C-01, C-02 | Explicit "cannot proceed until" checklists at phase transitions make lifecycle incompleteness visible as a structural blocker; Gate 2 prevents Automate from running before Expected is committed (C-01); Gate 4 prevents Findings before Diff is enumerated for every element (C-02) |
| V-04 | lifecycle-emphasis + phrasing-register (R11 priority-1: hypothesis-before-severity + mechanism-first template) | C-05 | Two C-05 interventions at different points in finding-writing: ordering prevents severity anchoring before hypothesis is written; template constrains hypothesis form at the sentence-structure level — if template alone saturates C-05, severity ordering is overhead; if anchoring is an independent failure mode, the combination outperforms either alone |
| V-05 | role-sequence + output-format (R11 priority-2: Spec Auditor + parallel contract table + mechanism-first template) | C-01, C-02, C-03, C-04, C-05, C-07, C-10 | Ceiling test: Auditor provides a forward-declared surface denominator (C-01, C-10); table enforces row-level completeness via visible blank cells (C-02, C-03, C-04, C-07); mechanism-first template constrains hypothesis quality (C-05) — maximum criteria coverage via three orthogonal mechanisms |

---

## V-01 — Inertia Framing

**axis:** inertia-framing
**hypothesis:** All prior variations present the skill as a sequence of steps without naming the baseline they replace. The status-quo for connector verification is "run it and see" — the operation runs, observed output is inspected, mismatches are noted informally. That baseline produces no spec-derived expectation, no field-level diff, no severity classification, and no causal hypothesis. Contract violations surface at integration time or in production, not in testing. A prompt that names this baseline at each phase boundary — "without this step, teams encounter X failure mode" — grounds each section's purpose in a concrete consequence rather than an abstract requirement. An operator who understands that expected-first writing prevents observational contamination is more likely to treat the Expected Output section as a genuine contract than as a formatting requirement. An operator who understands that a hypothesis matters for downstream diagnosis is more likely to write a mechanism than to restate the diff. Prediction: C-01 (expected-first) improves because the inertia frame at Phase 2 names observational bias as the failure mode it prevents; C-05 (hypothesis depth) improves because the inertia frame at Phase 5 names "the next engineer starts from zero" as the cost of a shallow hypothesis.

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

Without a contract trace, connector verification is "run it and see." The operation runs. Output is inspected. Mismatches are noted if they are noticed. There is no spec-derived expectation, no field-level diff, no severity classification, and no documented hypothesis. Contract violations that are subtle, conditional, or present only on edge-case paths survive until integration testing or production. Each section of this artifact exists to close a specific gap in that baseline:

- **Expected Output first** — without this ordering, observed behavior substitutes for spec. The implementation's actual output becomes the implicit expectation. Spec and implementation drift apart silently.
- **Field-level Diff** — without it, mismatches require mental comparison. Elements not checked cannot be distinguished from elements checked and satisfied.
- **Severity labels** — without them, a cosmetic formatting difference and a breaking data loss look identical in the record.
- **Root cause hypothesis** — without it, a finding is a symptom report. The next engineer to debug the deviation starts from zero. The hypothesis names the mechanism so the search begins in the right place.
- **Spec reference** — without it, a finding reads as a preference, not a contract violation. It cannot be tied to a specific obligation.

Keep these failure modes in mind as you write each section. If a section feels like overhead, name the failure mode it prevents.

---

### ROLE: Connectors Contract Expert

**Step 1 — Contract Scope**

Write a `## Contract Scope` section. Without this, the artifact cannot be reproduced by a second engineer.

- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline — no external file references — the artifact must be self-contained)
- Spec version and section governing this operation's output contract

**Step 2 — Expected Output (the contract)**

*Without expected-first writing: if you run the operation before writing Expected Output, observed behavior will contaminate what you write as expected. The Expected section must be derived from the spec alone — not from what you observed.*

Write a `## Expected Output` section. The operation has not been run.

For each required element:
- State the element and its expected value or constraint
- Cite the spec clause

Cover all contract surfaces:
- **Success path** — nominal input → nominal output
- **Error path** — invalid or missing input → error response
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not defined in the spec: `[surface]: not specified in spec — no contract clause exists`.

Write: `[CONTRACT COMMITTED — Automate begins here]`

---

### ROLE: Automate

**Step 3 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section: status code, full response body, headers, observable side effects.

**Step 4 — Diff**

*Without a field-level diff: a section-level "no issues found" verifies nothing. An element absent from the Diff was not checked — but there is no way to distinguish "checked and satisfied" from "not checked." Every element must appear with an explicit result.*

Write a `## Diff` section. For every element in Expected Output:
- `✓ {element} — satisfied`
- `F-NN — {element} — deviation (write finding below)`

Every element must appear. Silent omissions fail C-02.

If no deviations: write `## Diff — Contract satisfied. No findings.` and proceed to Summary.

**Step 5 — Findings**

*Without a root cause hypothesis: the finding is a symptom report. The next engineer who encounters this deviation starts from zero. A hypothesis names the mechanism so the fix search begins in the right place — not at the deviation, but at its cause.*

For each deviation:

```
Finding F-NN
deviation: [expected X; actual Y — state both sides]
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated — the finding is not traceable without this]
hypothesis: [one sentence — name the mechanism: what component, path, or condition produced the wrong output — not what the diff shows, but why it happened]
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

## V-02 — Phrasing Register: Question-Form

**axis:** phrasing-register (conversational / interrogative)
**hypothesis:** All prior variations use imperative commands: "Write a Contract Scope section." "For each finding, include a hypothesis." Commands invite checkbox completion — the operator writes the section to satisfy the command, not to answer a question. A question-form register replaces imperatives with questions the operator must answer: "What does the spec require for this operation's success response?" cannot be satisfied by producing a section shape; it requires retrieval and statement of spec content. Questions that cannot be answered without reading the spec force C-01 compliance structurally — you cannot answer "what does the spec say?" by running the operation first. Questions that ask "what produced this deviation?" rather than "write a hypothesis" force causal reasoning: an answer to "what caused this?" that restates the diff ("the value was wrong") is a failed answer to the question, not a valid section. Prediction: C-01 (expected-first) improves because question-form makes spec-retrieval the required cognitive act before writing; C-05 (hypothesis depth) improves because the question form "what caused this?" structurally rejects symptom restatements as non-answers; C-02 (diff completeness) improves because "did the actual output satisfy each expected element?" is answerable only if every element is addressed.

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

Answer these questions and write the answers as a `## Contract Scope` section:

- What operation is being verified, and what method?
- What connector or Automate context and environment is this running in?
- What is the exact input state the operation is receiving? Write it inline — do not reference an external file.
- Which spec version and section governs this operation's output contract?

A reader must be able to reproduce this trace from this section alone without opening any other file.

**Step 2 — Expected Output**

*Before running anything:* what does the spec say this operation must produce?

Write a `## Expected Output` section. Answer each question from the spec — do not run the operation first.

For the **success path**: What status code must the spec-defined nominal response carry? What fields must the response body contain, and with what constraints? What headers does the spec require?

For the **error path**: What must the operation return when a required field is missing? When auth is invalid? What status code and body structure does the spec define for each error case?

For **at least one edge case**: What does the spec say about empty collections? Rate-limit responses? Auth expiry? Pick the edge cases most applicable to this operation.

For any surface not defined in the spec: write `[surface]: not specified in spec`.

Cite the spec clause next to every expected value. If you cannot cite a clause, you are writing an assumption — label it as such.

When every surface is answered, write: `[CONTRACT COMMITTED — Automate begins here]`

---

### ROLE: Automate

**Step 3 — Actual Output**

What did the operation actually produce?

Run or simulate the operation against the input fixture. Write a `## Actual Output` section: what status code did it return? What was in the response body, field by field? What headers were present? Were there observable side effects?

**Step 4 — Diff**

For each element in the Expected Output: did the actual output satisfy what the spec requires?

Write a `## Diff` section. For every expected element, answer:
- `✓ {element} — satisfied`
- `F-NN — {element} — deviation`

Do not skip any element. If you cannot verify an element, say so explicitly — "not checked" is a valid answer; silent absence is not.

If there are no deviations: write `## Diff — Contract satisfied. No findings.` and proceed to Summary.

**Step 5 — Findings**

For each deviation, answer all of the following questions. Write the answers as a finding block.

```
Finding F-NN
deviation: What did the spec require, and what did the operation actually return? State both sides.
severity: Is this breaking (consumer cannot function), degraded (silent failure or data loss possible), or cosmetic (no correctness impact)?
spec: Which spec clause defines the contract obligation this deviation violates?
hypothesis: What caused this? Name the component, path, or condition that produced the wrong output — not what the diff shows, but the mechanism behind it. A restatement of the deviation is not an answer to this question.
```

For every `breaking` or `degraded` finding, also answer: should the spec be amended, should the implementation be fixed, or does this need further discussion? Give a one-sentence rationale.

```
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]
```

**Step 6 — Summary**

What is the verdict for this operation's contract?

```
## Summary

| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

Verdict: Contract violated / Contract satisfied

Coverage: {N satisfied} / {N total elements} clauses verified, {N deviations}

Recommendations:
[F-NN: amend-spec / fix-impl / needs-discussion — rationale]
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Lifecycle Emphasis: Phase Gate Checks

**axis:** lifecycle-emphasis (explicit phase-gate checks / cannot-proceed transitions)
**hypothesis:** All prior variations describe phases sequentially and trust the operator to complete each phase before proceeding. There are no visible checkpoints that make incompleteness a structural blocker — the operator can write findings without a complete diff, or write expected output while observing actual output, and the prompt cannot detect or prevent this. An explicit "cannot proceed" gate at each phase transition — with a named checklist the operator must confirm in writing — makes incompleteness visible as a decision point rather than an implicit assumption. Gate 2 (before Automate begins) prevents the operation from running before Expected Output is committed; Gate 4 (before Findings) prevents writing findings without a complete element-level diff. Writing the gate check output in the artifact makes compliance auditable. Prediction: C-01 (expected-first) improves because Gate 2 requires explicit confirmation that Expected Output was written before the operation ran; C-02 (diff complete, no silent omissions) improves because Gate 4 requires explicit confirmation that every element from Expected Output appears in the Diff before any finding is written.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

**Lifecycle discipline:** Each phase ends with a gate check. Write the gate check output explicitly in the artifact. Do not proceed to the next phase if the gate fails — return to the current phase and complete what is missing.

---

### ROLE: Connectors Contract Expert

**Phase 1 — Contract Scope**

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline — no external file references)
- Spec version and section governing this operation's output contract

**Gate 1:**

```
[ GATE 1 CHECK ]
- [ ] Operation and method are named
- [ ] Connector or Automate context is named
- [ ] Input fixture is written inline (not a file reference)
- [ ] Spec version and section are cited
Gate 1: PASS / FAIL — [if FAIL: what is missing]
```

Do not proceed to Phase 2 if Gate 1 fails.

---

**Phase 2 — Expected Output**

Write a `## Expected Output` section from the spec alone. The operation must not be run until Gate 2 passes and `[CONTRACT COMMITTED]` is written.

For each required element:
- State the element and its expected value or constraint
- Cite the spec clause

Cover all contract surfaces:
- Success path — nominal input → nominal output
- Error path — invalid or missing input → error response
- At least one edge case — empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not in the spec: `[surface]: not specified in spec`.

**Gate 2:**

```
[ GATE 2 CHECK ]
- [ ] Every contract surface from the spec is addressed in Expected Output
- [ ] Every expected element cites a spec clause
- [ ] No element in Expected Output was derived from observing the operation
- [ ] At least one edge case surface is covered
Gate 2: PASS / FAIL — [if FAIL: which surface or element is missing]
```

Do not run the operation until Gate 2 passes.

Write: `[CONTRACT COMMITTED — Gate 2 passed — Automate begins here]`

---

### ROLE: Automate

You begin after `[CONTRACT COMMITTED]`. Do not modify the Expected Output.

**Phase 3 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section: status code, full response body, headers, observable side effects.

---

**Phase 4 — Diff**

Write a `## Diff` section. For every element in Expected Output:
- `✓ {element} — satisfied`
- `F-NN — {element} — deviation`

Every element must appear with an explicit result.

**Gate 4:**

```
[ GATE 4 CHECK ]
- [ ] Every element from Expected Output appears in the Diff
- [ ] No element is silently absent
- [ ] Every deviation has an F-NN ID assigned
Gate 4: PASS / FAIL — [if FAIL: which element is absent]
```

Do not proceed to Phase 5 if Gate 4 fails. Return to Phase 4 and add the missing elements.

If no deviations: write `## Diff — Contract satisfied. No findings.` and proceed to Phase 6.

---

**Phase 5 — Findings**

For each deviation:

```
Finding F-NN
deviation: [expected X; actual Y — state both sides]
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated]
hypothesis: [one sentence — name the causal mechanism: what component, path, or condition produced the wrong output]
```

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness or consumer behavior

For every `breaking` or `degraded` finding:
```
recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
```

**Gate 5:**

```
[ GATE 5 CHECK ]
- [ ] Every F-NN from the Diff has a finding entry
- [ ] Every finding has a severity label
- [ ] Every finding has a spec reference
- [ ] Every finding has a hypothesis that names a mechanism (not a symptom restatement)
- [ ] Every breaking/degraded finding has a recommendation
Gate 5: PASS / FAIL — [if FAIL: which finding is incomplete and what is missing]
```

Do not proceed to Phase 6 if Gate 5 fails.

---

**Phase 6 — Summary**

```
## Summary

| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

Verdict: Contract violated / Contract satisfied

Coverage: {N satisfied} / {N total elements} clauses verified, {N deviations}

Recommendations:
[F-NN: amend-spec / fix-impl / needs-discussion — rationale]
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Combination: Hypothesis-Before-Severity + Mechanism-First Template

**axes:** lifecycle-emphasis + phrasing-register
**hypothesis:** R11 priority-1 combination. R11-V-03 (hypothesis-before-severity) targets C-05 via lifecycle ordering: the severity label is a framing anchor — writing "breaking" before the hypothesis tends to push hypothesis writing toward impact restatement ("the connector fails to deliver the payload, preventing consumer processing") rather than mechanism identification ("the ItemsMapper omits the count field when total equals zero"). Writing deviation → hypothesis → severity removes the label from the writing context at the point the hypothesis is written. R11-V-04/V-05 (mechanism-first template) targets C-05 via sentence-structure constraint: the `[component] [action verb] [field] when [condition]` template cannot be filled with a symptom restatement without producing a grammatically incoherent sentence — the slots demand a specific component, a specific verb, and a specific triggering condition. These two interventions are orthogonal: severity ordering changes what information is available in the operator's attention when writing the hypothesis; the template changes what grammatical form the hypothesis must take regardless of attention state. If the template alone saturates C-05, the severity ordering is overhead. If anchoring is an independent failure mode not addressed by template structure, the combination outperforms either alone. Combination prediction: C-05 improves over either single-axis intervention via two independent causal paths.

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
- State the element and its expected value or constraint
- Cite the spec clause

Cover all contract surfaces:
- Success path — nominal input → nominal output
- Error path — invalid or missing input → error response
- At least one edge case — empty collection, null required field, rate-limit trigger, auth expiry

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

**Step 5 — Findings (hypothesis-before-severity + mechanism-first template)**

For each deviation, write the finding fields in this exact order. **Do not reorder.**

```
Finding F-NN
deviation: [expected X; actual Y — state both sides]
```

Now write the hypothesis **before** assigning severity. **Why order matters:** Writing "breaking" before writing the hypothesis creates a framing anchor — the label primes impact restatement over mechanism identification. Write the mechanism first, before the severity label is in your attention.

**Hypothesis — use this template exactly. Fill every bracketed slot.**

```
hypothesis: The `[component or code path]` `[action: maps | serializes | validates | short-circuits | omits | overwrites | filters]` `[field or collection]` when `[condition under which the wrong behavior occurs]`, producing `[actual wrong output]` instead of the spec-required `[expected correct output]`.
```

Slot rules:
- **component**: the class, service, middleware, adapter, or code path responsible — not "the connector" generically
- **action**: the verb that names what the component does wrong — not "fails to" (choose: maps, serializes, validates, short-circuits, omits, overwrites, filters, or another specific verb)
- **condition**: the state, input property, or execution context under which the wrong behavior occurs
- If you cannot name a slot: write `[slot: unknown]` — do not remove the slot or replace it with a vague phrase

After writing the hypothesis, assign severity based on consumer impact. Let the hypothesis inform the severity assessment, but do not retroactively revise the hypothesis to match the severity label.

```
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated — the hypothesis may have surfaced the specific clause; cite it precisely]
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

## V-05 — Combination: Spec Auditor + Parallel Contract Table + Mechanism-First Template

**axes:** role-sequence + output-format + phrasing-register
**hypothesis:** R11 priority-2 combination — ceiling test. Three orthogonal mechanisms covering seven criteria. Mechanism 1: The Spec Auditor role (R11-V-01) enumerates contract surfaces from the spec and produces a committed surface inventory before the Contract Expert writes a single expected element. This separates surface enumeration (Auditor) from expected value authorship (Expert), preventing the Expert from short-circuiting spec-reading with expected-value writing. Addresses C-01 (expected-first, because Expected Output is organized around an Auditor-committed surface list) and C-10 (coverage ratio denominator is the Auditor's surface count, established before verification begins). Mechanism 2: The parallel contract table (R11-V-05) places Expected and Actual columns side-by-side with one row per clause. Blank cells in Actual, Result, or Severity are layout failures visible on document scan — they cannot be silently absent. Addresses C-02 (diff complete, no omissions), C-03 (severity on every finding), C-04 (spec reference via clause list), C-07 (three-directory structure via column labels). Mechanism 3: The mechanism-first fill-in-the-blank template constrains hypothesis form at the sentence-structure level — component + action + field + condition slots cannot be filled with a symptom restatement without producing a grammatically incoherent sentence. Addresses C-05 (root cause hypothesis). All three mechanisms are orthogonal and operate at different output levels: Auditor role (pre-writing phase) → table structure (row metadata) → hypothesis template (finding prose). Ceiling prediction: if this combination does not reach all five essential + composite >= 90, identify which criterion the combination fails to address and why.

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

Your only job is to enumerate what the spec covers for this operation. You do not write expected output. You do not run the operation. You do not classify findings.

**Step A — Enumerate contract surfaces**

Read every clause in the spec section governing this operation. List every contract surface the spec makes a claim about. A surface is a category of observable behavior the spec requires, permits, or prohibits — for example: success response body, 4xx error body, throttle response, empty collection result, required-field validation error, auth expiry behavior.

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

Write: `[SPEC AUDIT COMMITTED — Contract Expert begins here. Surface count: N]`

Your role ends here.

---

### ROLE: Connectors Contract Expert

You begin after `[SPEC AUDIT COMMITTED]`. Read the Spec Audit surface list. Do not add surfaces — the Auditor has already enumerated them.

**Step 1 — Contract Scope**

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline — no external file references)
- Spec version and section
- Surface count from audit: N (see Spec Audit above)

Self-contained. A reader must determine scope from this section alone.

**Step 2 — Expected Clauses (spec-derived — do not run before completing this list)**

For every surface in the Spec Audit, list every element the spec requires. Write as a numbered clause list organized by SA-NN surface. Derive from the spec alone; do not run the operation.

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

When every surface in the Spec Audit is addressed, write: `[CONTRACT COMMITTED — clause list sealed — Automate begins here]`

---

### ROLE: Automate

You begin after `[CONTRACT COMMITTED]`. Do not add to or modify the clause list above.

**Step 3 — Contract Comparison Table**

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
- **Actual**: state what the operation produced for this element; do not leave blank
- **Result**: `✓` if actual satisfies expected; `F-NN` (e.g., `F-01`) if it deviates
- **Severity**: `—` for satisfied rows; exactly one of `breaking` / `degraded` / `cosmetic` for finding rows

A blank Actual cell means the element was not verified. A blank Severity cell on a finding row means C-03 is not satisfied. Neither is acceptable.

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness or consumer behavior

**Step 4 — Findings (mechanism-first hypothesis template)**

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
- **component**: the class, service, middleware, adapter, or path responsible — not "the connector" generically
- **action**: the verb naming what the component does wrong — not "fails to"
- **condition**: the state, input property, or execution context under which the wrong behavior occurs
- If you cannot name a slot: write `[slot: unknown]` — do not remove the slot

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

Surface coverage: {N surfaces fully satisfied} / {N surfaces in Spec Audit} surfaces
Clause coverage: {N satisfied rows} / {N total rows in table} clauses, {N findings}

Recommendations:
[F-NN (CL-NN, SA-NN): amend-spec / fix-impl / needs-discussion — rationale]
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## Combination Candidates for Round 13

| Priority | Combination | Primary Targets | Rationale |
|----------|-------------|-----------------|-----------|
| 1 | V-01 (inertia framing) + V-04 (hypothesis-before-severity + template) | C-05 | Inertia framing names the downstream cost of shallow hypotheses ("the next engineer starts from zero"); hypothesis-before-severity + template constrains what the hypothesis can say structurally. Three-way C-05 intervention: motivational (inertia), ordering (before-severity), structural (template). Tests whether motivation compounds with structural constraints or is redundant once template is enforced. |
| 2 | V-03 (phase gate checks) + V-05 (Spec Auditor + table + template) | C-01, C-02, C-07, C-10 | Phase gates enforce lifecycle completion at transition points; V-05 provides structural enforcement via Auditor + table. Combines lifecycle discipline (gates confirm each phase completed) with structural discipline (Auditor + table make omissions visible as layout failures). Tests whether explicit gate confirmation adds value over structural visibility alone. |
| 3 | V-02 (question-form) + V-03 (phase gate checks) | C-01, C-02, C-05 | Question-form register requires retrieval and statement rather than section production; phase gates require explicit confirmation before proceeding. Both target completeness via different mechanisms: register (cognitive) and gates (structural). Tests whether the cognitive demand of question-form reduces the value of structural gates, or whether gates catch lapses that question-form does not prevent. |

## Evaluation Order Guidance

| Priority | Variation | Rationale |
|----------|-----------|-----------|
| 1 | V-04 (hypothesis-before-severity + template) | R11's top-priority combination. Two independent C-05 interventions at different points in finding-writing. Highest-information test: if this combination does not outperform either single-axis, mechanism-first template and severity anchoring address the same failure mode rather than separate ones. |
| 2 | V-05 (Spec Auditor + table + template) | R11's ceiling test. Maximum criteria coverage across three orthogonal mechanisms. If this combination reaches all essential + composite >= 90, the v16 rubric is saturated by known techniques. If it fails a criterion, that criterion identifies a gap no prior variation has addressed. |
| 3 | V-03 (phase gate checks) | Single-axis lifecycle intervention. Evaluate after V-04/V-05 to determine whether gate checks add C-01/C-02 gains beyond what Spec Auditor + table already provide structurally. If V-05 already saturates C-01/C-02, gates are overhead. |
| 4 | V-01 (inertia framing) | Single-axis motivation framing. Evaluate after V-03/V-04/V-05 to isolate whether motivation framing changes hypothesis quality independently of structural constraints. If template (V-04) already saturates C-05, inertia framing adds no C-05 value. |
| 5 | V-02 (question-form) | Single-axis register variation. Evaluate last — register is the most diffuse intervention; its effect on C-01/C-02/C-05 is the hardest to isolate. Compare against V-01 (motivation) and V-03 (gates) to determine whether question-form adds value beyond inertia context or structural gates. |
