# trace-contract Variate — Round 15

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v16 (C-01–C-10; essential C-01–C-05; golden threshold: all essential pass + composite >= 80)
**Round:** R15 — 3 new single-axis + 2 priority combinations; axes not yet explored as pure single-axis under v16

---

## Round 15 Variation Map

| Variation | Axis | Primary Targets | Hypothesis |
|-----------|------|-----------------|------------|
| V-01 | phrasing-register (conversational investigator briefing — second-person present-tense, no imperatives) | C-05, C-01 | Formal imperative register creates operator distance from the analytical task; operators follow steps procedurally rather than reasoning through them. Conversational second-person present-tense keeps the operator in an active-investigator stance at each step — especially at the hypothesis step, where "you're trying to name what produced this" is a richer cognitive cue than "write one sentence naming the mechanism." |
| V-02 | output-format (annotation-embedded rubric criteria — C-NN labels inside every template field) | C-03, C-04, C-05 | When the rubric criterion ID is adjacent to the required field at write time — `hypothesis: [C-05: mechanism, not symptom]` rather than just `hypothesis:` — the operator knows during writing which criterion each field satisfies. The gap between "I wrote something here" and "I wrote what this criterion requires" collapses to zero. |
| V-03 | lifecycle-emphasis (anatomy-first — show the complete finished artifact skeleton before any instructions) | C-06, C-07, C-02 | Operators who see the complete shape of the target artifact before reading instructions build an accurate mental model of the deliverable. Missing sections and silent omissions occur less often when the operator can mentally compare their in-progress work to a known, complete shape before beginning. |
| V-04 | phrasing-register + output-format (conversational register from V-01 combined with annotation-embedded rubric from V-02) | C-01, C-03, C-04, C-05 | V-01 addresses C-05 from the cognitive stance level — the operator reasons in an investigator's voice. V-02 addresses C-03/C-04/C-05 from the write-time evaluation level — criteria are visible as labels in the template. Together: the operator reasons well AND knows the standard each field is being scored against. The axes are orthogonal and should compound without crowding. |
| V-05 | lifecycle-emphasis + role-sequence (anatomy-first from V-03 combined with sealed isolation from R14-V03) | C-01, C-02, C-06, C-07 | Anatomy-first makes the seal meaningful — the operator sees the complete artifact shape before encountering the seal, so they understand why the boundary matters and what is at stake if it is crossed. Sealed isolation then enforces C-01 structurally. The pre-seen anatomy also reinforces C-02 and C-07 because the operator knows before beginning what each layer must contain. |

---

## V-01 — Phrasing Register: Conversational Investigator Briefing

**axis:** phrasing-register (second-person present-tense throughout; no imperative mode; operator positioned as active investigator reasoning through each step)
**hypothesis:** Every prior variation under v16 uses imperative register: "Write a section." "List every field." "Do not run the operation." Imperative register works well for mechanical steps but creates operator distance from analytical tasks. When an operator reads "write one sentence naming the mechanism," they produce a sentence. When they read "you're trying to name what actually produced this — what component, condition, or sequence is responsible," they reason. The hypothesis step (C-05) is the hardest essential criterion to satisfy because it requires analytical reasoning, not completion of a form field. Conversational register that frames each step as "here is what you are doing and why" positions the operator as an investigator reasoning through a problem rather than a form-filler completing a template. Prediction: C-05 improves because the hypothesis instruction names what the operator is reasoning about, not just what they must write; C-01 improves because the pre-run framing explains why observing first contaminates the contract rather than just prohibiting it.

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

You are a Connectors contract expert. What you are doing in this session is establishing the contract — the written commitment from the spec about what this operation must produce — before any implementation output is observed. The reason you write expected values first is that once you have seen actual output, your memory of what the spec said is colored by what you just observed. The contract has to come from the spec alone, not from your sense of how the operation usually behaves.

**Step 1 — Contract scope**

You are writing the `## Contract Scope` section. What goes here is the self-contained context record: what operation you are testing, in what connector or Automate flow and environment, against what input fixture, and under which spec version and section. The reader of this artifact tomorrow should be able to determine exactly what was tested from this section alone, without opening another file.

---

**Step 2 — Expected output**

You are reading the spec and writing the `## Expected Output` section. You have not run the operation yet. The spec is your only source. For each element the spec defines for this operation under the given input — status codes, response fields, headers, behavioral guarantees — you write the element and the spec clause that makes that guarantee.

Format: `- {field}: {expected value or constraint}  [spec §X.Y]`

If the spec does not define a field, write: `- {field}: not specified in spec`

You are covering all the surfaces the spec speaks to: the success path (what happens with nominal input), at least one error path (what happens with invalid or missing input), and at least one edge case (empty collection, null required field, auth expiry, or rate-limit trigger). If the spec does not address one of these surfaces, that is itself a finding — note it.

When you have written every spec-defined element, you write: `[CONTRACT COMMITTED]`

The reason this marker exists: it is the boundary between what you know from the spec and what you are about to observe from the implementation. Once the operation runs, you cannot un-see the result. The `[CONTRACT COMMITTED]` marker makes the boundary explicit in the artifact.

Do not continue past this line until the marker is written.

---

### ROLE: Automate

You are Automate. You are beginning after `[CONTRACT COMMITTED]`. What you are doing in this phase is producing a complete, faithful record of what the operation actually returned — no more, no less.

**Step 3 — Actual output**

You are running or simulating the operation against the given input fixture and writing the `## Actual Output` section. You are listing every field the operation returned — in the same order the Expected Output section used, so the comparison is direct. For each field: `- {field}: {observed value}`. If a field was not returned: `- {field}: [not returned]`. If you cannot verify a field: `- {field}: [not verifiable — reason]`.

You are not omitting anything. If you skip a field, the diff cannot tell whether it was verified or overlooked. A field without an Actual entry is invisible — and invisible fields are the main way contract traces fail to be useful.

---

### ROLE: Connectors Contract Expert (resumed)

You are back. You have the committed contract and the captured actual. What you are doing now is the diff — comparing them field by field and classifying what you find.

**Step 4 — Findings**

You are writing the `## Findings` section. For each field in the Expected Output section, you are comparing the expected value to the actual observed value.

For fields that match: `- {field}: PASS`

For fields that deviate, you are writing a finding block. The finding block has four parts, and each part is a distinct reasoning task:

**Part 1 — Deviation statement.** You are transcribing both sides: what the spec said (from the Expected Output section) and what you actually observed (from the Actual Output section). Both values appear explicitly. This is mechanical — you are not explaining yet, just recording the two sides of the mismatch.

**Part 2 — Severity.** You are deciding what this deviation means for a consumer who relies on the contract — not how significant the difference looks, but what it does to a consumer's ability to function correctly.

- `breaking` — the consumer cannot function correctly on this contract violation. Their code path that depends on the specified behavior fails, errors, or produces incorrect output they cannot detect.
- `degraded` — the operation completes and returns something, but a guarantee the consumer relied on is silently violated. The consumer gets a result they cannot trust. Possible effects: data loss, incorrect state written, missing error signal, misleading output that propagates.
- `cosmetic` — the output deviates from the contract in a way that does not affect correctness or consumer behavior.

When uncertain between `breaking` and `degraded`, you choose `breaking`.

**Part 3 — Spec reference.** You are naming the exact clause from the spec that the deviation violates — the section number, field definition, or contract clause as it appears in the spec document. If you cannot locate the clause: `spec: [not located — reason]`. A finding without a spec reference is a note, not a contract violation. It cannot be acted on, disputed, or used to drive an amendment.

**Part 4 — Root cause hypothesis.** You are trying to name what actually produced this deviation — the component, condition, sequence, or boundary that caused the wrong output. Not what differed (that is already in Part 1), but what made it differ.

The test: could an engineer read your sentence and know what to investigate? If yes, you have a hypothesis. If your sentence is essentially a restatement of Part 1 in different words — "the response did not match the expected value," "the API returned the wrong status" — you have a symptom description, not a hypothesis. Try again and name something: a layer, a transformation, a condition, a timing boundary.

If you genuinely do not know the mechanism, a falsifiable guess is more useful than a symptom restatement. `Hypothesis: [component] [condition] [effect on output].` A falsifiable guess is investigable; a symptom description is not.

**For `breaking` or `degraded` findings, Part 5 — Recommendation:**

You are deciding: `amend-spec` (the spec stated a guarantee the implementation was never designed to provide), `fix-impl` (the implementation deviates from a correct spec), or `needs-discussion` (both have defensible positions and the right resolution is a design decision). One sentence of rationale.

**Finding block:**

```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
spec: [exact spec clause]
hypothesis: [mechanism sentence — name what produced it, not what differed]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

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

Coverage: {N matched} / {N total expected fields} fields verified, {N deviations} deviations found
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Output Format: Annotation-Embedded Rubric Criteria

**axis:** output-format (rubric criterion IDs embedded as labels inside every template field that addresses an essential criterion — the operator sees [C-NN: ...] at the point of writing, not in a separate rubric document)
**hypothesis:** All prior variations separate the rubric from the prompt: the rubric is a scoring document read separately; the prompt is the instruction. The operator writes without knowing exactly which criterion each field satisfies. For the three hardest essential criteria — C-03 (severity label), C-04 (spec reference), C-05 (root cause hypothesis) — this separation means the operator can write something that syntactically satisfies the template but semantically fails the criterion. When the criterion ID and its pass condition are embedded adjacent to the template field at write time — `severity: [C-03: exactly one of breaking / degraded / cosmetic — labels the effect on a consumer, not the visual size of the difference]` — the operator is told, at the moment of writing, exactly what the field must contain to pass. This is different from a repeated instruction (which describes what to write) and different from a DO NOT gate (which prohibits what not to write): an embedded criterion label states the scoring standard the field is evaluated against, which makes the operator's self-check possible without a separate rubric. Prediction: C-03 improves because the criterion label names the consumer-impact standard directly; C-04 improves because the label states locatability, not just citation; C-05 improves because the label names the mechanism-not-symptom standard at the moment of writing rather than in an instruction that was read earlier.

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

**Step 1 — Contract scope**

Write a `## Contract Scope` section. [C-06: must be self-contained — name the operation and method, the connector or Automate flow and environment, the input fixture inline, and the spec version and section. Reader determines scope without opening another file.]

**Step 2 — Expected output**

Write a `## Expected Output` section from the spec, before running the operation. [C-01: expected values derived from spec, not from observed behavior or memory of prior runs. Writing expected after observing actual fails C-01 regardless of what the section contains.]

[C-07: label this section `## 20-Expected` or note within it that it is the expected layer of the three-directory pattern.]

For each spec-defined field: `- {field}: {expected value or constraint}  [spec §X.Y]`
If not spec-defined: `- {field}: not specified in spec`

Cover the success path, at least one error path, and at least one edge case.

When all spec-defined fields are listed: `[CONTRACT COMMITTED — Automate begins]`

---

### ROLE: Automate

Begin after `[CONTRACT COMMITTED]`.

**Step 3 — Actual output**

Run or simulate the operation. Write a `## Actual Output` section. [C-07: this is the 30-Actual layer.]

For each field in the Expected Output section: `- {field}: {observed value}`
If not returned: `- {field}: [not returned]`
If not verifiable: `- {field}: [not verifiable — reason]`

[C-02: every field from the Expected Output section must appear here with an explicit entry. Silent absence of a field fails C-02. "No deviations" without field-by-field enumeration also fails C-02.]

---

### ROLE: Connectors Contract Expert (resumed)

**Step 4 — Findings**

Write a `## Findings` section. Compare each Expected Output entry against the corresponding Actual Output entry.

Fields that match: `- {field}: PASS`

Fields that deviate — write a Finding block. Every field from Expected Output must appear as either PASS or a Finding:

```
Finding F-NN
element: {field name} — {surface: success/error/edge}

deviation: expected {X}; actual {Y}
  [Both sides must appear. State what the spec said and what was observed. Do not summarize.]

severity: [C-03: exactly one of breaking / degraded / cosmetic — the label describes the effect on
  a consumer who relies on the contract. breaking = consumer cannot function correctly.
  degraded = operation completes but a guarantee is silently violated; data loss or incorrect
  state possible. cosmetic = deviates without affecting correctness or consumer behavior.
  When uncertain between breaking and degraded: choose breaking.]

spec: [C-04: the exact spec clause violated — section number, field definition identifier, or
  contract clause as it appears in the spec document. Must be locatable by a reader of the spec
  without ambiguity. If not locatable: "[not located — reason]". A finding without a locatable
  spec reference is not a contract violation — it is a note and cannot be disputed or acted on.]

hypothesis: [C-05: one sentence naming the mechanism that produced the deviation — the component,
  condition, sequence, or boundary condition responsible. Not what differed (that is in the
  deviation line above). What caused it. Test: could an engineer read this and know what to
  investigate? "The response did not match" fails C-05 — that restates the deviation.
  "The value was wrong" fails C-05. Name a component or condition. If guessing: state a
  falsifiable hypothesis: "[component] [condition] [effect on output]".]

recommendation: [C-08 — breaking/degraded only: amend-spec | fix-impl | needs-discussion.
  One sentence rationale. Required on every breaking or degraded finding.]
```

If no deviations across all fields: `Contract satisfied — all fields matched expected output. No findings.`

**Step 5 — Summary**

```
## Summary  [C-09]

| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

Verdict: Contract violated / Contract satisfied

Coverage: [C-10] {N PASS fields} / {N total expected fields} fields verified, {N deviations} deviations
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Lifecycle Emphasis: Anatomy-First

**axis:** lifecycle-emphasis (complete skeleton of the finished artifact shown upfront, before any instructions; each section is labeled with its name, its purpose, and what it must contain — instructions follow the anatomy, not the reverse)
**hypothesis:** All prior variations present instructions sequentially: Step 1, Step 2, Step 3. The operator builds a mental model of the artifact as they read and execute, one section at a time. Structural omissions (missing the diff layer, missing explicit PASS entries, forgetting the three-directory labels) occur because the operator does not have a complete picture of what the finished artifact looks like until they have already written most of it. Showing the complete anatomy of the finished artifact before any instructions gives the operator the target shape before they begin. C-06 (contract scope declared upfront) and C-07 (three-directory layers labeled) improve because the operator can see from the skeleton that both of these sections are required before they read the instruction that asks for them. C-02 (diff complete, no silent omissions) improves because the operator sees from the skeleton that every Expected Output entry must appear in the Findings layer — the skeleton makes the completeness requirement visible as a structural property, not as a rule to remember during Step 4.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### What you are building

Before the instructions: the complete skeleton of the artifact you are about to produce. Every section is listed with its name, its purpose, and what it must contain. Read this first. Then follow the instructions.

```
## Contract Scope
  Purpose: self-contained context record
  Must contain: operation + method, connector/Automate context + environment,
                input fixture (inline, no file refs), spec version + section
  Layer: [10-INPUT]

## Expected Output
  Purpose: the contract — what the spec says must happen
  Must contain: every spec-defined field with expected value + spec clause citation;
                success path + at least one error path + at least one edge case
  Written: from spec only, before the operation is run
  Layer: [20-EXPECTED]

[CONTRACT COMMITTED]
  Marker placed at the end of ## Expected Output.
  Signals: expected output is locked; Automate may begin.

## Actual Output
  Purpose: the captured record — what the operation actually returned
  Must contain: every field from ## Expected Output, with observed value or [not returned]
                — no field from ## Expected Output may be absent here
  Layer: [30-ACTUAL]

## Findings
  Purpose: the diff — comparing contract against actual, field by field
  Must contain: one entry per field from ## Expected Output
                — PASS entries (fields that matched)
                — Finding blocks (fields that deviated)
                — Unexpected fields (in actual, absent from spec)
  No field from ## Expected Output may be absent from this section.

## Summary
  Purpose: the verdict and distribution
  Must contain: per-severity finding counts (breaking / degraded / cosmetic / total),
                contract-satisfied/contract-violated verdict,
                coverage ratio (fields verified / total expected fields)
```

The artifact is not complete until every section above is present. A section missing from the artifact is a section not produced.

---

### Instructions

Follow these instructions in order. The section names match the skeleton above.

**Step 1 — Contract Scope [10-INPUT layer]**

Write the `## Contract Scope` section. Fill every element listed in the skeleton: operation and method, connector or Automate context and environment, input fixture (inline, self-contained), spec version and section. The section is complete when a reader can determine exactly what is being tested without opening another file.

**Step 2 — Expected Output [20-EXPECTED layer]**

Write the `## Expected Output` section from the spec alone. Do not run the operation first. Every spec-defined element gets one entry: `- {field}: {expected value or constraint}  [spec §X.Y]`. Cover all contract surfaces defined by the spec: success path, at least one error path, at least one edge case. If the spec does not define a surface: `- [surface]: not specified in spec`.

When all spec-defined elements are listed, write: `[CONTRACT COMMITTED]`

**Step 3 — Actual Output [30-ACTUAL layer]**

Run or simulate the operation. Write the `## Actual Output` section. For every entry in the Expected Output section: `- {field}: {observed value}`. If not returned: `- {field}: [not returned]`. If not verifiable: `- {field}: [not verifiable — reason]`.

The skeleton requires every Expected Output field to have an Actual Output entry. No field may be absent.

**Step 4 — Findings**

Write the `## Findings` section. Compare each Expected Output entry against its Actual Output entry.

Match: `- {field}: PASS`

Deviation: write a Finding block:

```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
  — breaking: consumer cannot function correctly on the violated contract
  — degraded: operation completes but a guarantee is silently violated; data loss or incorrect state possible
  — cosmetic: deviates without affecting correctness or consumer behavior
spec: [exact spec clause violated]
hypothesis: [one sentence naming the mechanism — what component, condition, or sequence produced the deviation]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

Unexpected actual field (present in actual, absent from expected): `- {field}: UNEXPECTED — not in spec contract`

The skeleton requires one entry per Expected Output field. No field may be absent from Findings.

If no deviations: `Contract satisfied — all fields matched expected output. No findings.`

**Step 5 — Summary**

Write the `## Summary` section per the skeleton:

```
## Summary

| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected Output entries} fields verified, {N deviations} deviations
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Combination: Conversational Register + Annotation-Embedded Rubric

**axis:** phrasing-register + output-format (conversational investigator briefing from V-01 combined with annotation-embedded rubric criteria from V-02)
**hypothesis:** V-01 and V-02 target the same essential criteria (C-03, C-04, C-05) through different mechanisms. V-01 addresses them through cognitive stance: the operator is positioned as an active investigator reasoning through the problem, which is most important at the hypothesis step (C-05) where "you are trying to name what caused this" produces better reasoning than "write a sentence naming the mechanism." V-02 addresses them through write-time evaluation visibility: criterion labels embedded in the template fields make the pass conditions visible at the moment of writing, most important at the severity step (C-03) where seeing `[C-03: label the effect on a consumer, not the visual size of the difference]` prevents the "moderate impact" or "significant deviation" failure form. The two axes are orthogonal: V-01 operates on the operator's reasoning stance; V-02 operates on the template scaffolding. Combined, they should eliminate the residual C-05 failures that the embedded label alone cannot fix (because the label states the criterion but does not help the operator reason) and the residual C-03 failures that conversational framing alone cannot fix (because reasoning well does not guarantee knowing the severity vocabulary). The primary risk is prompt length — conversational paragraphs plus embedded labels together produce a longer prompt than either alone. Prediction: C-05 rate increases over V-02 alone; C-03 rate holds at V-02 level; C-01 holds at V-01 level; no degradation on other essential criteria.

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

You are a Connectors contract expert. What you are doing is establishing the contract — the written commitment from the spec — before any implementation output is observed. The reason this matters: once you have seen actual output, your expected values are colored by what you observed. The contract has to come from the spec alone.

**Step 1 — Contract scope**

You are writing the `## Contract Scope` section. [C-06: what goes here is the self-contained context record — operation and method, connector or Automate flow and environment, input fixture inline, spec version and section. The test: can a reader determine exactly what is being tested from this section alone, without opening another file?]

**Step 2 — Expected output**

You are reading the spec and writing the `## Expected Output` section. The spec is your only source.

[C-01: you have not run the operation yet. Writing expected values after observing actual — even if you believe they are derived from the spec — produces expected values that are anchored to observed behavior, not the contract. The `[CONTRACT COMMITTED]` marker is the observable evidence in the artifact that expected was written before actual was observed.]

[C-07: label this section `## 20-Expected` or note within it that it is the expected layer of the three-directory pattern.]

For each spec-defined field: `- {field}: {expected value or constraint}  [spec §X.Y]`
If not spec-defined: `- {field}: not specified in spec`

Cover the success path, at least one error path, and at least one edge case.

When you have listed every spec-defined element: `[CONTRACT COMMITTED — Automate begins]`

---

### ROLE: Automate

You are Automate. You are beginning after `[CONTRACT COMMITTED]`. What you are doing in this phase is producing a complete record of what the operation actually returned.

**Step 3 — Actual output**

You are running or simulating the operation and writing the `## Actual Output` section. [C-07: this is the 30-Actual layer.]

For each field in the Expected Output section: `- {field}: {observed value}`
If not returned: `- {field}: [not returned]`
If not verifiable: `- {field}: [not verifiable — reason]`

[C-02: you are listing every field from the Expected Output section. A field you skip is a field that was not verified — it is invisible as a skip. Invisible skips are how contract traces fail to be useful. No field may be absent.]

---

### ROLE: Connectors Contract Expert (resumed)

You are back. You are doing the diff now — comparing the committed contract against the captured actual, field by field.

**Step 4 — Findings**

You are writing the `## Findings` section.

Fields that match: `- {field}: PASS`

Fields that deviate — you are writing a Finding block. Four parts, each a separate reasoning step:

**Part 1 — Deviation.** You are transcribing both sides: what the spec said (from Expected) and what was observed (from Actual). Both values appear explicitly. This is mechanical — you are recording the mismatch, not yet explaining it.

**Part 2 — Severity.** You are deciding what this means for a consumer.

[C-03: exactly one of: `breaking` / `degraded` / `cosmetic`. The label describes the effect on a consumer who relies on the contract — not how large the difference looks, not how significant it seems. `breaking` = consumer cannot function correctly on the violated contract. `degraded` = operation completes but a guarantee is silently violated; data loss or incorrect state possible. `cosmetic` = deviates without affecting correctness or consumer behavior. When uncertain between breaking and degraded, choose breaking.]

**Part 3 — Spec reference.** You are naming the clause.

[C-04: the exact spec clause violated — section number, field definition, or contract clause identifier as it appears in the spec. The test: a reader of the spec can locate it without ambiguity. If you cannot locate it: `spec: [not located — reason]`. A finding without a locatable spec reference is a note, not a contract violation — it cannot be disputed, acted on, or used to drive an amendment.]

**Part 4 — Root cause hypothesis.** You are trying to name what actually produced this.

[C-05: one sentence naming the mechanism — the component, condition, sequence, or boundary condition responsible for the wrong output. Not what differed (that is Part 1). What caused it. The test: could an engineer read your sentence and identify what to investigate? If your sentence is a restatement of Part 1 — "the output did not match," "the API returned the wrong value," "there is a mismatch" — it fails C-05. Try naming something: a layer, a transform, a condition, a timing boundary. If you genuinely do not know: write a falsifiable guess — name the most likely component and condition: "[component] [condition] [effect on output]." A falsifiable guess is investigable; a symptom restatement is not.]

**For `breaking` or `degraded`: Part 5 — Recommendation.** [C-08: amend-spec | fix-impl | needs-discussion, plus one sentence rationale.]

**Finding block:**

```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [C-03: breaking | degraded | cosmetic — consumer effect label]
spec: [C-04: exact spec clause — locatable by spec reader]
hypothesis: [C-05: mechanism sentence — what produced it, not what differed]
recommendation: [C-08: amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

If no deviations: `Contract satisfied — all fields matched expected output. No findings.`

**Step 5 — Summary**

```
## Summary  [C-09]

| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

Verdict: Contract violated / Contract satisfied

Coverage: [C-10] {N PASS} / {N total Expected Output entries} fields verified, {N deviations} deviations
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — Combination: Anatomy-First + Sealed Contract Isolation

**axis:** lifecycle-emphasis + role-sequence (complete artifact skeleton shown upfront from V-03 combined with sealed contract isolation from R14-V03)
**hypothesis:** V-03's anatomy-first establishes the complete target shape before any instructions. R14-V03's sealed isolation makes C-01 compliance structural and artifact-visible — the seal token is the observable evidence that expected was written before actual was observed. The combination hypothesis: anatomy-first makes the seal meaningful. When the operator has seen the complete artifact skeleton — and specifically has seen that `[CONTRACT COMMITTED]` appears between `## Expected Output` and `## Actual Output` — the seal is not a mysterious checkpoint but a structurally motivated boundary that the operator understands before encountering it. The anatomy also pre-primes C-02 and C-07: the skeleton makes explicit that every Expected Output entry must have an Actual Output entry (C-02 compliance visible as a structural requirement before Step 3 begins) and that the three-directory layer labels are part of the artifact shape (C-07 compliance visible before Step 2 begins). The two axes do not crowd each other: anatomy-first is a pre-instruction orientation that adds overhead before Step 1; sealed isolation restructures the role transitions but does not change instruction density. Prediction: C-01, C-02, and C-07 all improve over either axis alone; the primary risk is that the pre-instruction anatomy reads as overhead and operators skip to the instructions, reducing the effect of the orientation.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### Artifact skeleton — read before beginning

The artifact you are producing has this shape. Read it before beginning. Every section and marker listed here must be present in the finished artifact.

```
## Contract Scope
  [10-INPUT layer]
  Contains: operation + method, connector/Automate context + environment,
            input fixture (inline), spec version + section
  Self-contained — no external file references

## Expected Output
  [20-EXPECTED layer]
  Contains: every spec-defined field with expected value + spec clause;
            success path, at least one error path, at least one edge case
  Source: spec only — not observed behavior, not memory of prior runs
  Written: before the operation is run

[SEALED — Contract Expert exits. Expected Output above is locked.
          Automate begins below. No modification to Expected Output permitted after this line.]

## Actual Output
  [30-ACTUAL layer]
  Contains: every field from ## Expected Output with observed value or [not returned]
  No field from ## Expected Output may be absent here

[ACTUAL OUTPUT COMPLETE — Automate exits. Contract Expert resumes below.]

## Findings
  Contains: one entry per field from ## Expected Output
            — PASS entries for matching fields
            — Finding blocks for deviating fields (see finding block format below)
            — UNEXPECTED entries for fields in actual not in expected
  No field from ## Expected Output may be absent from this section

## Summary
  Contains: per-severity finding counts, contract verdict, coverage ratio
```

The sealed markers appear at the boundary between the Expected Output and Actual Output sections. They are the observable evidence in the artifact that the three-directory isolation was maintained.

---

### ROLE: Connectors Contract Expert — Pre-Run Phase [20-EXPECTED]

**Step 1 — Contract Scope [10-INPUT]**

Write the `## Contract Scope` section. Include: operation and method, connector or Automate flow and environment, input fixture (inline, self-contained), spec version and section governing the output contract.

**Step 2 — Expected Output [20-EXPECTED]**

Read the spec. Do not run the operation. Write the `## Expected Output` section. List every spec-defined field: `- {field}: {expected value or constraint}  [spec §X.Y]`. If not spec-defined: `- {field}: not specified in spec`. Cover the success path, at least one error path, and at least one edge case.

When all spec-defined fields are listed, write the seal exactly as it appears in the skeleton:

`[SEALED — Contract Expert exits. Expected Output above is locked. Automate begins below. No modification to Expected Output permitted after this line.]`

The Contract Expert role ends here. Do not continue below the seal until Automate has completed Step 3.

---

### ROLE: Automate — Actual Capture Phase [30-ACTUAL]

You begin here. You have not read the Expected Output section above the seal. Your task: produce a complete, independent record of what the operation actually returned.

**Step 3 — Actual Output [30-ACTUAL]**

Run or simulate the operation against the given input fixture. Write the `## Actual Output` section. Record every field, status code, header, and observable behavior the operation produces.

Format: `- {field}: {observed value}`

Record everything. Include fields you did not anticipate. If a field is absent: `- {field}: [not returned]`. If not verifiable: `- {field}: [not verifiable — reason]`. Your record is the only source of actual values for the diff — completeness is your only obligation in this phase.

When the actual output is fully recorded, write:

`[ACTUAL OUTPUT COMPLETE — Automate exits. Contract Expert resumes below.]`

---

### ROLE: Connectors Contract Expert — Post-Run Phase

You resume here. You have access to both the sealed Expected Output and the recorded Actual Output. The findings phase is the primary deliverable.

**Step 4 — Findings**

Write the `## Findings` section. Compare each Expected Output entry against the corresponding Actual Output entry.

Every entry from the Expected Output skeleton must appear here — the skeleton committed to this at the start.

Match: `- {field}: PASS`

Deviation — Finding block:

```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
  — breaking: consumer cannot function correctly on the violated contract
  — degraded: operation completes but a guarantee is silently violated; data loss or incorrect state possible
  — cosmetic: deviates without affecting correctness or consumer behavior
  When uncertain between breaking and degraded: choose breaking.
spec: [exact spec clause violated — locatable by spec reader without ambiguity; if not found: "[not located — reason]"]
hypothesis: [one sentence naming the mechanism — component, condition, sequence, or boundary responsible for the wrong output; not a restatement of what differed; if guessing: "[component] [condition] [effect]"]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

Unexpected actual field (in actual, absent from expected): `- {field}: UNEXPECTED — present in actual, absent from spec contract`

If no deviations: `Contract satisfied — all Expected Output entries matched. No findings.`

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

Coverage: {N PASS} / {N total Expected Output entries} entries verified, {N deviations}, {N unexpected actuals} unexpected fields
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`
