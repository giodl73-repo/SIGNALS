# trace-contract Variate — Round 14 (Rubric v16)

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v16 (C-01–C-10; essential C-01–C-05; golden threshold: all essential pass + composite >= 80)
**Round:** R14 — 3 new single-axis + 2 priority combinations; axes not yet explored as pure single-axis under v16

---

## Round 14 Variation Map

| Variation | Axis | Primary Targets | Hypothesis |
|-----------|------|-----------------|------------|
| V-01 | lifecycle-emphasis (findings phase dominates instructional space; pre-run phases compressed) | C-05, C-03, C-04 | When the findings phase receives 3x the instructional space of the expected-writing phase, with separate dedicated paragraphs for hypothesis, severity, and spec-reference, operator attention tracks the allocation — the hardest criteria are no longer buried at equal density with mechanical steps |
| V-02 | inertia-framing (status-quo trap named and itemized before any instruction; each failure mode mapped to a structural answer) | C-01, C-05, C-02 | Naming the five failure modes of the unstructured practice before any instruction appears makes each structural requirement feel motivated rather than bureaucratic; operators who understand what they are upgrading from are less likely to replicate the flat content of their default practice inside the new structure |
| V-03 | role-sequence (sealed contract isolation — Contract Expert writes and formally seals expected section; Automate captures actual independently; Contract Expert resumes for diff; isolation observable in the artifact) | C-01, C-02, C-07 | Making role isolation structural and artifact-visible — a formal seal token and role-boundary marker — enforces C-01 more durably than an instructional gate; Automate's independent record enforces C-02 completeness by removing the expected section as a checklist anchor |
| V-04 | lifecycle-emphasis + role-sequence (V-01 findings expansion combined with V-03 sealed isolation) | C-01, C-02, C-03, C-04, C-05, C-07 | The two axes are orthogonal: sealed isolation targets C-01/C-02/C-07; findings-phase expansion targets C-05/C-03/C-04; combining them covers the full essential surface without either axis crowding out the other |
| V-05 | inertia-framing + output-format (status-quo contrast from V-02; severity ledger table where every cell must be filled replaces the finding block template) | C-01, C-02, C-03, C-04, C-05, C-09, C-10 | The inertia frame motivates the table structure (each blank cell is the named failure mode of "silent omission"); the ledger table enforces C-02 at the cell level — an empty Actual cell is visually indistinguishable from a gap in prose, which is not visually invisible in a table |

---

## V-01 — Lifecycle Emphasis: Findings Phase Dominance

**axis:** lifecycle-emphasis (findings phase receives disproportionate instructional space; pre-run phases are brief and mechanical)
**hypothesis:** All prior variations allocate roughly equal instruction density per step. The hardest criteria to satisfy — C-05 (hypothesis naming a mechanism, not restating the symptom), C-03 (severity with defined meaning, not free-form label), C-04 (spec reference traceable to a clause) — appear at the same density as mechanical steps such as "write the scope section." Volume is a proxy for importance in dense prompts: a three-sentence step reads as less important than a twelve-sentence step. When the findings phase receives 3x the instructional space of the expected-writing phase — with separate dedicated paragraphs for deviation statement, severity, spec reference, and hypothesis, each with its own failure-mode description — operator attention tracks the allocation. The pre-run steps are compressed to minimal mechanical instructions; their function is to commit the contract and capture the actual, not to produce insight. Prediction: C-05 improves because the hypothesis instruction is a standalone paragraph with a named anti-pattern and a structural test, not one item in a compact template; C-03 improves because severity definitions occupy visible space with concrete consumer-impact descriptions rather than a one-line parenthetical.

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

Write a `## Contract Scope` section naming: the operation and method, the connector or Automate flow and environment, the input fixture (inline), and the spec version and section governing the output contract. Self-contained — no external file references.

**Step 2 — Expected Output**

Read the spec. Write a `## Expected Output` section. List every field, status code, header, and behavioral guarantee the spec makes for this operation under the given input fixture. Format: `- {field}: {expected value or constraint}  [spec §X.Y]`. Every entry must cite a spec clause. If a surface is not spec-defined: `- {field}: not specified in spec`. Cover the success path, at least one error path, and at least one edge case (empty collection, missing required field, auth expiry, or rate-limit trigger).

When all spec-defined fields are listed, write: `[CONTRACT COMMITTED]`

The operation must not be run before `[CONTRACT COMMITTED]` is written.

---

### ROLE: Automate

You begin only after `[CONTRACT COMMITTED]` appears above.

**Step 3 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section. List every field in the same order as the Expected Output section: `- {field}: {observed value}`. If a field was not returned: `- {field}: [not returned]`. If not verifiable: `- {field}: [not verifiable — reason]`. Do not omit any field that appears in the Expected Output section.

---

### ROLE: Connectors Contract Expert (resumed)

**Step 4 — Findings**

This step is the core of the contract trace. The following four tasks are distinct intellectual operations. Do not compress them.

Write a `## Findings` section. For each field in the Expected Output section, compare the expected value against the actual observed value. For fields that match: `- {field}: PASS`. For fields that deviate, write a Finding block. The Finding block has four required parts, each described below.

---

**Part 1 — Deviation statement.**

Transcribe both sides. State what was expected (from the Expected Output section) and what was actually observed (from the Actual Output section). Both values must appear explicitly. Do not summarize. Do not editorialize. The deviation statement is mechanical: it is a verbatim record of what the spec said and what the implementation produced.

Example of a correct deviation statement: `deviation: expected status 200 with body {items: [{id: "abc", name: "Widget"}]}; actual status 422 with body {error: "schema_validation_failed", detail: "missing required field 'name'"}`

Example of an incorrect deviation statement: `deviation: the response was wrong` — this does not state both sides and provides no basis for the diff.

---

**Part 2 — Severity classification.**

Assign exactly one severity label from the three defined below. The label describes the effect of the deviation on a consumer who relies on the contract — not the visual appearance of the difference, not its cosmetic significance to a reader.

`breaking` — the contract violation prevents a consumer from functioning correctly. The consumer's code path that relies on the specified behavior fails, produces errors, or produces incorrect output that cannot be detected without external signals. The consumer has no fallback; the contract they relied on is not honored.

`degraded` — the operation completes and returns a response, but a guarantee the consumer relied on is silently violated. The consumer receives a result but cannot trust that the specified guarantee was honored. Possible consequences include: data loss, incorrect state written, missing error signal where the spec promised one, or misleading output that propagates silently.

`cosmetic` — the output deviates from the contract in a way that does not affect correctness or consumer behavior. The contract should be updated to match reality, but no consumer operation is broken or degraded by the deviation.

When uncertain between `breaking` and `degraded`: choose `breaking`. Do not invent a fourth label. Do not use unlabeled severity descriptions.

---

**Part 3 — Spec reference.**

Name the exact spec clause the deviation violates. Write the section number, field definition identifier, or contract clause as it appears in the spec document. The reference must be locatable without ambiguity by someone reading the spec directly.

If you cannot find the clause: write `spec: [not located — reason]` and flag the finding for spec audit follow-up. Do not omit the spec-reference field on a finding. A finding without a spec reference is a note, not a contract finding — it is not disputable, not actionable, and not auditable.

---

**Part 4 — Root cause hypothesis.**

This is the most important part of the finding block and the hardest to write correctly.

Write one sentence that names the mechanism that produced the deviation. The mechanism is the component, condition, sequence, or boundary condition that caused the wrong output. It is not the deviation restated in different words.

The test for a valid hypothesis: after reading your sentence, could an engineer identify what to investigate? If the answer is no, the hypothesis is a symptom restatement.

Anti-pattern (symptom restatement): `The response code did not match the expected value.`
Anti-pattern (observation repeat): `The API returned 422 instead of 200.`
Anti-pattern (component-free): `Something in the connector caused the mismatch.`

Valid hypothesis: `The connector's schema validator runs a strict content-type check before routing; if the Automate flow sends application/json without an explicit charset, the validator rejects the payload at the routing layer before the operation executes, producing 422 before the operation is invoked.`

If you do not know the mechanism, write a falsifiable guess — name the most likely component and the condition you believe triggers the deviation: `Hypothesis: the field is being truncated at the serialization boundary between the connector runtime and the Automate response adapter, not by the operation logic itself — the operation produces the correct value but the adapter drops it when normalizing the response envelope.`

A falsifiable guess is useful because it is investigable. A symptom restatement is not useful because it contributes nothing beyond the deviation statement already written in Part 1.

---

**Part 5 — Recommendation (breaking and degraded only).**

For every `breaking` or `degraded` finding, write one of: `recommendation: amend-spec` (the spec stated a guarantee the implementation was never designed to provide), `recommendation: fix-impl` (the implementation deviates from a correct spec), or `recommendation: needs-discussion` (both the spec and the implementation have defensible positions and the right resolution requires a design decision). Follow with one sentence of rationale.

---

**Finding block format:**

```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
spec: [exact spec clause]
hypothesis: [mechanism sentence]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

If no deviations exist across all fields: write `Contract satisfied — all fields matched expected output. No findings.`

---

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

Coverage: {N matched fields} / {N total expected fields} fields verified, {N deviations} deviations found
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Inertia Framing: Status-Quo Trap Opening

**axis:** inertia-framing (the prompt opens with an explicit named description of the unstructured status-quo practice and each of its five failure modes, before any instruction appears; each failure mode is mapped to the structural answer the skill provides)
**hypothesis:** Operators arrive with a default practice: run the operation, scan the output for anything surprising, write up what you found. This practice produces the anti-pattern every rubric criterion is designed to prevent — but operators do not perceive the connection between their default practice and the structure being asked of them. They follow the structure mechanically while replicating the flat content of their default practice: surface-level hypotheses, implicit severity, missing spec references, fields checked by selective attention not by enumeration. Naming the status-quo trap explicitly — describing what the unstructured approach does and naming each specific failure mode — creates contrast that makes each structural requirement feel motivated rather than bureaucratic. When an operator reads "without a spec-first expected section, you are comparing against your memory of how the operation usually behaves — not the contract," the `[CONTRACT COMMITTED]` gate becomes protection against a named failure mode, not an arbitrary checkpoint. When they read "noting what seems surprising is not a root cause hypothesis — it is exactly the status-quo practice this step replaces," the requirement to name a mechanism becomes recognizable as an upgrade rather than a formality. Prediction: C-01 improves because operators understand the cost of contaminating expected output with observation; C-05 improves because "write what you noticed" is named as the anti-pattern; C-02 improves because "fields checked by selective attention" is named as the failure mode the complete enumeration answers.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### What this skill replaces

Before /trace:contract, the standard practice was:

1. Run the operation.
2. Scan the output for anything that looks wrong.
3. Write up what you found.

That practice has five failure modes. This skill is designed to eliminate each one. The structure below is the structural answer to each failure mode — not bureaucratic overhead.

**Failure mode 1 — Diffing against memory, not the spec.**
You compare the output to what you expect based on prior runs or intuition, not against the written contract. Bugs in the spec itself are invisible. Fields the spec guarantees but that you've never personally seen deviate go unchecked. You are testing your expectations, not the contract.
*Structural answer: write the expected output from the spec before running the operation. The contract is the spec, not your memory.*

**Failure mode 2 — Silent field omission.**
You record the fields that caught your eye. Fields that matched, or fields you never thought to check, are never recorded. Coverage is undefined. A future operator cannot tell whether a field was verified or silently skipped.
*Structural answer: every field in the expected output must appear in the diff with an explicit PASS or finding. No field may be silently absent.*

**Failure mode 3 — Unlabeled severity.**
You describe what was wrong. The reader infers whether it is blocking or cosmetic from your tone. Triage decisions made on that inference are undocumented, unrepeatable, and disputably subjective.
*Structural answer: every finding carries exactly one severity label from a defined vocabulary.*

**Failure mode 4 — No spec anchor.**
Your finding floats. It cannot be verified: readers cannot determine whether the actual behavior is wrong by the spec or wrong by your expectation. The finding is a disputable opinion, not a contract violation.
*Structural answer: every finding cites the specific spec clause the deviation violates.*

**Failure mode 5 — Symptoms noted, not causes hypothesized.**
You write what differed. The next engineer inherits the diff but not the diagnosis. The finding has no investigative value beyond the diff itself. "The response code was wrong" contributes nothing that a reader of the diff doesn't already know.
*Structural answer: every finding includes a mechanism hypothesis — a sentence naming the component, condition, or sequence that produced the wrong output.*

---

### ROLE: Connectors Contract Expert

**Step 1 — Contract Scope**

Write a `## Contract Scope` section naming: the operation and method, the connector or Automate flow and environment, the input fixture (inline, self-contained), and the spec version and section that governs the output contract.

**Step 2 — Expected Output (the answer to failure mode 1)**

Read the spec. Write a `## Expected Output` section. Do not run the operation first. Do not look at the actual output and then backfill the expected section — that is failure mode 1 exactly.

List every field, status code, header, and behavioral guarantee the spec makes for this operation under the given input fixture: `- {field}: {expected value or constraint}  [spec §X.Y]`. Every entry must cite a spec clause. If a surface is not defined in the spec: `- {field}: not specified in spec`. Cover the success path, at least one error path, and at least one edge case.

When every spec-defined field is listed, write: `[CONTRACT COMMITTED]`

The operation must not be run before `[CONTRACT COMMITTED]` is written. Running first and writing expected second is failure mode 1 with extra steps.

---

### ROLE: Automate

You begin only after `[CONTRACT COMMITTED]` appears above.

**Step 3 — Actual Output (the answer to failure mode 2)**

Run or simulate the operation. Write a `## Actual Output` section. This step must answer failure mode 2: every field that appears in the Expected Output section must appear here. List fields in the same order: `- {field}: {observed value}`. If a field was not returned: `- {field}: [not returned]`. If not verifiable: `- {field}: [not verifiable — reason]`.

A field with no Actual entry is a field that was not verified. Silent absence is failure mode 2.

---

### ROLE: Connectors Contract Expert (resumed)

**Step 4 — Diff and Findings**

Write a `## Findings` section. Compare expected and actual field by field.

For fields that match: `- {field}: PASS`

For deviations, write a finding block. The finding block answers failure modes 3, 4, and 5 simultaneously.

```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
  — breaking: consumer cannot function correctly on the violated contract
  — degraded: operation completes but a guarantee is silently violated; data loss or incorrect state possible
  — cosmetic: deviates without affecting correctness or consumer behavior
spec: [exact spec clause — this is the answer to failure mode 4]
hypothesis: [one sentence naming the mechanism — not what differed, but what component, condition, or sequence produced it — this is the answer to failure mode 5]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

The spec reference is the answer to failure mode 4. If you cannot locate the clause: `spec: [not located — reason]`.

The hypothesis is the answer to failure mode 5. "The field did not match" is failure mode 5. "The output was wrong" is failure mode 5. Name what produced it.

If no deviations exist: `Contract satisfied — all fields matched expected output. No findings.`

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

Coverage: {N matched} / {N total expected fields} fields verified, {N deviations} deviations
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Role Sequence: Sealed Contract Isolation

**axis:** role-sequence (Contract Expert writes the expected section and formally seals it with a role-boundary token before Automate is present; Automate's role header states it has not read the expected section; Contract Expert resumes for diff — isolation is structural and artifact-visible, not merely instructional)
**hypothesis:** All prior variations enforce the expected-first commitment with a `[CONTRACT COMMITTED]` gate token. This is an instructional commitment device: it relies on the operator not contaminating the expected section even though both role sections are visible in the same prompt. An operator writing expected output can mentally run the operation or recall prior runs, and the gate does not prevent it — the gate only marks the transition point. A sealed contract model makes isolation structural and verifiable in the artifact itself: the Contract Expert's role section ends with a formal seal token and a named role-boundary before Automate's section begins. Automate's role header explicitly states the constraint: "you have not read the Expected Output section above." When the artifact is reviewed, the seal and the role-boundary are observable signals that isolation was maintained — not inferred from the absence of contamination, but visible as structural markers. The three-role sequence also maps cleanly to the three-directory pattern: Contract Expert's pre-run phase is the 20-expected layer; Automate's capture phase is the 30-actual layer; Contract Expert's post-run phase is the diff. Prediction: C-01 improves because isolation is not merely instructed but structurally enforced and observable in the artifact; C-02 improves because Automate's section is isolated from the expected section and must produce a complete independent record (Automate cannot use the expected list as a checklist, so it must enumerate what it actually observes); C-07 improves because the three roles map directly and explicitly to the three directory layers.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

This skill uses a sealed contract model. The Contract Expert produces the expected output section from the spec and seals it before Automate runs the operation. Automate records the actual output independently. The Contract Expert resumes for the diff after Automate exits. The seal token in the artifact is the observable evidence of C-01 compliance.

---

### ROLE: Connectors Contract Expert — Pre-Run Phase [20-EXPECTED]

**Step 1 — Contract Scope**

Write a `## Contract Scope` section. State: operation and method, connector or Automate flow and environment, input fixture (inline, self-contained), spec version and section governing the output contract.

**Step 2 — Expected Output**

Read the spec. Do not run the operation. Do not observe actual output. Write a `## Expected Output` section. List every field, status code, header, and behavioral guarantee the spec makes for this operation under the given input fixture.

Format: `- {field}: {expected value or constraint}  [spec §X.Y]`

Every entry must cite a spec clause. If a field is not spec-defined: `- {field}: not specified in spec`. Cover the success path, at least one error path, and at least one edge case (empty collection, missing required field, auth expiry, or rate-limit trigger).

When all spec-defined fields are listed — write the seal:

`[SEALED — Contract Expert exits. Expected Output above is locked. Automate begins below. No modification to the Expected Output section is permitted after this line.]`

The Contract Expert role ends here. Do not continue below the seal until Automate has completed Step 3.

---

### ROLE: Automate — Actual Capture Phase [30-ACTUAL]

You begin here. You have not read the Expected Output section above the seal. Your task is to produce a complete, independent record of what the operation actually returns — not a comparison against the expected section, which you have not seen.

**Step 3 — Actual Output**

Run or simulate the operation with the given input fixture. Write a `## Actual Output` section. Record every field, status code, header, and observable behavior the operation produces.

Format: `- {field}: {observed value}`

Record everything the operation returns. Include fields you did not anticipate. If a field is absent: `- {field}: [not returned]`. If not verifiable: `- {field}: [not verifiable — reason]`. Do not omit anything — your record is the only source of actual values for the diff.

When the actual output is fully recorded, write:

`[ACTUAL OUTPUT COMPLETE — Automate exits. Contract Expert resumes below.]`

---

### ROLE: Connectors Contract Expert — Post-Run Phase

You resume here. You now have access to both the sealed Expected Output and the recorded Actual Output. Your task is to produce the complete diff and findings.

**Step 4 — Diff and Findings**

Write a `## Findings` section. Compare each entry in the Expected Output section against the corresponding entry in the Actual Output section.

For each Expected Output entry where Actual Output matches: `- {field}: PASS`
For each Expected Output entry where Actual Output deviates: write a Finding block (below)
For each Expected Output entry absent from Actual Output entirely: that is a deviation — write a Finding block with `actual: [not returned]`
For each Actual Output entry with no corresponding Expected Output entry: note as `- {field}: UNEXPECTED — present in actual, absent from spec contract`

**Finding block:**

```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
  — breaking: consumer cannot function correctly on the violated contract
  — degraded: operation completes but a guarantee is silently violated
  — cosmetic: deviates without affecting correctness or consumer behavior
spec: [exact spec clause violated]
hypothesis: [one sentence naming the mechanism — which component, condition, or sequence produced the wrong output]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

Hypothesis rule: the sentence must name something investigable — a component, a condition, a sequence. "The value did not match" is not a hypothesis; it is the deviation restated. If you do not know the mechanism, write a falsifiable guess: "Hypothesis: [component] [condition] [effect]."

If no deviations exist: `Contract satisfied — all Expected Output entries matched Actual Output. No findings.`

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

Coverage: {N PASS entries} / {N total Expected Output entries} entries verified, {N deviations}, {N unexpected actuals} unexpected fields in actual
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Combination: Lifecycle Emphasis + Sealed Contract Isolation

**axis:** lifecycle-emphasis + role-sequence (expanded findings phase from V-01 combined with sealed contract isolation from V-03)
**hypothesis:** V-01 and V-03 target orthogonal criteria. V-03's sealed isolation addresses C-01 (expected-first compliance, structurally enforced and artifact-visible), C-02 (Automate's independent record enforces completeness by removing the expected list as a silent checklist), and C-07 (three roles map directly to three directory layers). V-01's expanded findings phase addresses C-05 (hypothesis receives a standalone paragraph with anti-pattern exemplars and a structural validity test), C-03 (severity definitions are expanded with consumer-impact descriptions), and C-04 (spec reference explanation names the failure mode of a floating finding). Because the two axes target different criteria through different mechanisms, combining them should cover the full essential surface (C-01 through C-05) plus C-07 without either axis crowding out the other. The primary risk is prompt length: the seal structure adds role-transition overhead, and the expanded findings phase adds instruction density. Prediction: composite score improves over either single-axis alone; no ceiling effect on essential criteria because each axis addresses different failure modes; the risk is that length pressure causes the operator to compress the findings phase despite the expanded instructions.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

This skill uses a sealed contract model. The Contract Expert writes and seals the expected output section from the spec before Automate runs the operation. Automate records actual output independently. The Contract Expert resumes for the diff with expanded findings instructions. The seal token in the artifact is the observable evidence of C-01 compliance.

---

### ROLE: Connectors Contract Expert — Pre-Run Phase [20-EXPECTED]

**Step 1 — Contract Scope**

Write a `## Contract Scope` section: operation and method, connector or Automate flow and environment, input fixture (inline, self-contained), spec version and section governing the output contract.

**Step 2 — Expected Output**

Read the spec. Do not run the operation. Do not observe any actual output. Write a `## Expected Output` section. List every field, status code, header, and behavioral guarantee the spec makes for this operation under the given input fixture.

Format: `- {field}: {expected value or constraint}  [spec §X.Y]`

Every entry must cite a spec clause. If a field is not spec-defined: `- {field}: not specified in spec`. Cover the success path, at least one error path, and at least one edge case.

When all spec-defined fields are listed, write:

`[SEALED — Contract Expert exits. Expected Output above is locked. Automate begins below. No modification to the Expected Output section is permitted after this line.]`

---

### ROLE: Automate — Actual Capture Phase [30-ACTUAL]

You begin here. You have not read the Expected Output section above the seal.

**Step 3 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section. Record every field, status code, header, and observable behavior the operation produces. Your record is the only source of actual values for the diff — record everything, including fields you did not anticipate.

Format: `- {field}: {observed value}`. If absent: `- {field}: [not returned]`. If not verifiable: `- {field}: [not verifiable — reason]`.

When complete, write:

`[ACTUAL OUTPUT COMPLETE — Automate exits. Contract Expert resumes below.]`

---

### ROLE: Connectors Contract Expert — Post-Run Phase

You resume here with access to both sections. The findings phase is the primary deliverable. Give it the majority of your attention.

**Step 4 — Diff and Findings**

Write a `## Findings` section. Compare each Expected Output entry against the corresponding Actual Output entry.

- Expected entry matches actual: `- {field}: PASS`
- Expected entry deviates from actual: write a Finding block
- Expected entry absent from actual entirely: write a Finding block with `actual: [not returned]`
- Actual entry with no corresponding expected entry: `- {field}: UNEXPECTED — present in actual, absent from spec contract`

**The Finding block has five required parts. Each is a distinct task.**

---

**Part 1 — Deviation statement.**

Transcribe both sides explicitly: expected value (from the Expected Output section) and actual value (from the Actual Output section). Both must appear. Do not summarize.

Example: `deviation: expected status 200 with body {items: [...]}, items array non-empty; actual status 200 with body {items: []}, items array empty`

---

**Part 2 — Severity classification.**

Assign exactly one label. The label describes the effect on a consumer who relies on the contract.

`breaking` — the contract violation prevents a consumer from functioning correctly. The consumer's reliance on the specified behavior fails, produces errors, or produces incorrect output that cannot be self-detected.

`degraded` — the operation completes and returns a response, but a guarantee the consumer relied on is silently violated. The consumer cannot trust the result. Possible consequences: data loss, incorrect state, missing error signal, misleading output that propagates without detection.

`cosmetic` — deviates from the contract without affecting correctness or consumer behavior. The spec should be updated to match reality, but nothing breaks.

When uncertain between `breaking` and `degraded`: choose `breaking`. Do not invent a fourth label.

---

**Part 3 — Spec reference.**

Name the exact spec clause violated. Write the section number or contract clause identifier as it appears in the spec document. The reference must be locatable by a reader of the spec without ambiguity.

If you cannot find the clause: `spec: [not located — reason]`. Flag for spec audit follow-up. A finding without a spec reference cannot be acted on, disputed, or used to drive an amendment.

---

**Part 4 — Root cause hypothesis.**

Write one sentence naming the mechanism that produced the deviation. The mechanism is the component, condition, sequence, or boundary condition responsible — not the deviation restated.

Structural test for a valid hypothesis: after reading your sentence, could an engineer identify what to investigate? If no — it is a symptom restatement.

Anti-patterns:
- `The response did not match the expected value.` (symptom restatement — identical to Part 1)
- `The API behaved incorrectly.` (component-free — names nothing investigable)

Valid form: `The connector's cursor normalization step converts null cursors to an empty string before passing them to the pagination adapter; the adapter interprets an empty string cursor as an end-of-collection signal and returns an empty items array rather than the first page.`

If you do not know the mechanism: write a falsifiable guess. `Hypothesis: [component] [condition] [effect on output].` A falsifiable guess is investigable. A symptom restatement is not.

---

**Part 5 — Recommendation (breaking and degraded only).**

One of: `amend-spec` (the spec was wrong — the implementation was never designed to provide the specified guarantee), `fix-impl` (the implementation deviates from a correct spec), or `needs-discussion` (both the spec and the implementation have defensible positions). One sentence of rationale.

---

**Finding block format:**

```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
spec: [exact spec clause]
hypothesis: [mechanism sentence]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

If no deviations: `Contract satisfied — all Expected Output entries matched. No findings.`

---

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

Coverage: {N PASS} / {N total Expected Output entries} entries verified, {N deviations}, {N unexpected actuals} unexpected
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — Combination: Inertia Framing + Severity Ledger Format

**axis:** inertia-framing + output-format (status-quo contrast opening names each failure mode of unstructured practice; severity ledger table format replaces finding block template — every row is one contract field, every cell must be filled)
**hypothesis:** V-02 addresses the "why" — naming the status-quo failure modes makes each structural requirement feel motivated. A separate axis (not explored as single-axis yet) addresses the "how" at the cell level: a pre-printed ledger table with columns `Field | Expected | Actual | Status | Severity | Spec | Hypothesis` makes silent omissions visually impossible in a way that prose sections cannot. An empty Actual cell in a table is a visible gap — it is adjacent to the Field name and the Expected value, and its emptiness registers as a local formatting break. An omitted field in a prose "Actual Output" section is invisible: the section simply ends. The combined hypothesis is: the inertia frame motivates the table structure (each blank cell is the named failure mode of "selective attention" from the opening), and the table structure enforces completeness at the cell level. Additionally, the ledger format satisfies C-09 and C-10 by construction: the table is a severity distribution summary with a calculable coverage ratio. Prediction: C-02 improves because silent omissions are structurally impossible in a filled table; C-09 and C-10 pass by construction; C-05 improves because the hypothesis cell is visually parallel to the other cells — operators who fill every other cell correctly feel completion pressure to fill the hypothesis cell with something non-trivial; the inertia frame amplifies this by naming "noting what seems wrong" as the anti-pattern the hypothesis cell replaces.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### What this skill replaces

Without /trace:contract, the standard practice is: run the operation, look at the output, note anything that seems wrong. That practice fails in five ways:

1. **Memory as contract** — you compare against your memory or intuition, not the written spec. Fields the spec guarantees but that have never deviated go unchecked.
2. **Selective coverage** — you record the fields that caught your eye. Fields that seemed fine are silently omitted. Coverage is unknown.
3. **Implicit severity** — you describe problems; readers infer priority from your tone. Triage decisions are undocumented and unrepeatable.
4. **Floating findings** — without a spec anchor, findings are disputable opinions rather than contract violations.
5. **Symptoms, not causes** — you note what differed. The next engineer still has to figure out why.

The severity ledger below is the structural answer to all five. Every row is one contract field. Every cell must be filled. A blank cell is not a missing value — it is an unverified field. Blank cells are structurally visible; silently omitted fields are not.

---

### ROLE: Connectors Contract Expert

**Step 1 — Contract Scope**

Write a `## Contract Scope` section: operation and method, connector or Automate flow and environment, input fixture (inline, self-contained), spec version and section governing the contract.

**Step 2 — Contract Ledger: Field and Expected columns**

Write a `## Contract Ledger` section. Create the table below. Fill the **Field** and **Expected** columns from the spec now. Do not fill any other column. Do not run the operation.

```
| Field | Expected [spec §] | Actual | Status | Severity | Spec Clause | Hypothesis |
|-------|-------------------|--------|--------|----------|-------------|------------|
```

Every spec-defined field gets one row. The Expected cell must contain the spec-specified value or constraint plus a spec clause reference in brackets: `{value} [spec §X.Y]`. If not spec-defined: `not specified [§?]`.

Organize by surface with separator rows:

```
| **Surface: Success Path** | — input: {fixture description} | | | | | |
| {field 1} | {expected value} [spec §X.Y] | | | | | |
| {field 2} | {expected value} [spec §X.Y] | | | | | |
| **Surface: Error Path — {name}** | — input: {error-trigger description} | | | | | |
| {field} | {expected value} [spec §X.Y] | | | | | |
| **Surface: Edge Case — {name}** | — input: {edge-case description} | | | | | |
| {field} | {expected value} [spec §X.Y] | | | | | |
```

Cover the success path, at least one error path, and at least one edge case.

When all rows are entered, write: `[CONTRACT COMMITTED — Automate fills Actual column]`

---

### ROLE: Automate

You begin after `[CONTRACT COMMITTED]`. Fill the **Actual** column for every row in the Contract Ledger. Run or simulate the operation. For each field row, write the observed value in the Actual cell.

Rules:
- If a field was not returned: `[not returned]`
- If a field is not verifiable: `[not verifiable — reason]`
- Do not leave any Actual cell blank. A blank Actual cell means the field was not verified — it is failure mode 2 from the opening.
- Do not modify the Field or Expected columns.

When the Actual column is fully populated, write: `[ACTUAL COMPLETE — Contract Expert fills Status, Severity, Spec Clause, Hypothesis]`

---

### ROLE: Connectors Contract Expert (resumed)

**Step 3 — Complete the Ledger**

For every field row, fill the remaining four columns:

**Status column:**
- `PASS` — Actual matches Expected
- `F-NN` (e.g., F-01, F-02) — Actual deviates from Expected

**Severity column (F-NN rows only):**
- `breaking` — consumer cannot function correctly on the violated contract
- `degraded` — operation completes but a guarantee is silently violated; data loss or incorrect state possible
- `cosmetic` — deviates without affecting correctness or consumer behavior
- Leave blank only on PASS rows.

**Spec Clause column (F-NN rows only):**
Write the exact spec clause violated. If not locatable: `[not located — reason]`. Do not leave blank on an F-NN row — a finding without a spec anchor is a note, not a contract violation (failure mode 4 from the opening).

**Hypothesis column (F-NN rows only):**
Write one phrase naming the mechanism that produced the deviation. The mechanism is what component, condition, or sequence caused it — not the deviation restated. "The value was wrong" is the deviation — it is already in the Actual column (failure mode 5 from the opening). Name what caused it. Example: `cursor normalizer converts null to empty string; adapter reads empty string as end-of-collection signal`. If guessing: `hypothesis: [component] [condition] [effect]`. Leave blank only on PASS rows.

**Step 4 — Finding Expansions (breaking and degraded only)**

For every F-NN row with severity `breaking` or `degraded`, write a Finding Expansion block below the ledger:

```
Finding F-NN
element: {field} — {surface}
deviation: expected {X}; actual {Y}
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

Coverage: {N PASS rows} / {N total field rows} fields verified, {N F-NN rows} deviations
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`
