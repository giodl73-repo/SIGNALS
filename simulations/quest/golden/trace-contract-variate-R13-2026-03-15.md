# trace-contract Variate — Round 13
**Date:** 2026-03-15
**Rubric:** v13 (C-08–C-39; 32 criteria; total max 128)
**Baseline:** R12 V-05 = 30/30 on v12 (C-08–C-37 all PASS)
**Target criteria:** C-38 (surface-status axis label immediately before pipe sequence), C-39 (both prohibited forms named: table-row and prose-sentence)

---

## Round 13 Variation Map

| Variation | Axis | C-38 | C-39 | Notes |
|-----------|------|------|------|-------|
| V-01 | Output format — axis label present, only table-form prohibition named | PASS | PARTIAL | Single-axis: "**Surface status:**" label inline before pipe sequence (C-38 PASS); table-form prohibited but prose-sentence form not named (C-39 PARTIAL) |
| V-02 | Lifecycle emphasis — both prohibitions named, label separated from pipe sequence by intervening prose | PARTIAL | PASS | Single-axis: "**Axis 3 — Surface finding distribution**" heading with instructions before pipe sequence; label not immediately before the pipe-sequence line (C-38 PARTIAL); both table and prose forms named (C-39 PASS) |
| V-03 | Phrasing register — both criteria in strongest explicit form | PASS | PASS | Single-axis: "**Surface status:**" inline label immediately before pipe sequence; both prohibited forms named with example of each |
| V-04 | Role sequence + output format — both criteria with causal rationale per prohibition | PASS | PASS | Combination: V-03 axis-label approach + each prohibition includes structural-consequence explanation; closes "why can't I use a table/prose?" author dilemma |
| V-05 | Full platinum (C-08 through C-39) | PASS | PASS | All axes: V-04 causal rationale + R12-sourced failure-mode labels ("table-register absorption", "prose-register absorption") + three-consequence enumeration per prohibition + complete R12 V-05 baseline at maximum strength |

---

## V-01 — Axis Label Present, Single Prohibition

**Axis:** Output format — "**Surface status:**" inline label added before the pipe sequence; only the table-form prohibition is named; prose-sentence form not mentioned

**Hypothesis:** C-38 PASS because the label appears on the same structural unit as the pipe sequence, making the line self-announcing in isolation without format-register inference. C-39 PARTIAL because only one of two documented failure forms is named — the prose-sentence alternative remains tacitly available. A template that closes the table path but not the prose path produces V-02-class failures in subsequent authors.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state description or inline fixture — state inline, do not reference external files}
**Spec source:** {spec file path and section — e.g., signal-trace-2026-03-14.md§trace-contract}

---

## Roles

**Contract Author (Role A)**
Owns: Pre-Authoring Rules, Phase 1 (Contract Scope, Expected Output, Mechanism Taxonomy, Commit Gate).
Has not run the operation. Has not observed any runtime output. Reads the spec alone.
Role ends when the commit gate line is written. Attribution of Phase 1 content is permanent from this point forward.

**Automate (Role B)**
Owns: Phase 2 (Actual Output), Phase 3 (Diff), Phase 4 (Findings), Phase 5 (Summary).
Does not read the Pre-Authoring Rules section or Phase 1 authoring instructions.
Reads Phase 1 output only — the Contract Scope, Expected Output blocks, and Mechanism Taxonomy table.
Begins work at the `[CONTRACT COMMITTED]` gate line.
MUST NOT modify, annotate, correct, or supplement Phase 1 content. Any belief that a Phase 1 entry is incorrect is a finding, not a license to edit.

> **Automate: stop reading here. Scroll to the `[CONTRACT COMMITTED]` line. Your section begins immediately after it.**

---

## Pre-Authoring Rules — Role A reads; Role B stops here

These are binding authoring constraints for Contract Author. These rules take effect now, before any Expected content is written.

**Rule 1 — Spec-anchoring imperative.**
Every expected value in Phase 1 must cite the spec clause that requires it. An expected value without a spec reference is not a valid contract entry. Remove it or find the reference before the gate. Do not carry unanchored entries past the gate. A section heading is not a clause reference — cite the specific clause within the section that makes the value required.

**Rule 2 — Independent surface block mandate.**
Phase 1 must contain three structurally independent labeled sections: Success Path, Error Path, and Edge Case. A flat list without section headings is not compliant. A table with a Surface column is not compliant. Each surface is its own labeled block. A surface with no entries must still appear — write the heading and state why no entries apply.

**Rule 3 — Pre-gate taxonomy declaration requirement.**
The mechanism taxonomy must be declared inside Phase 1, before the commit gate. The vocabulary is binding on Phase 3 authors at gate commit. No mechanism may be added, renamed, or removed in Phase 3. Declaring the taxonomy after the gate is not permitted.

**Rule 4 — Per-field diff enumeration.**
In Phase 3, every field declared in Phase 1 must appear by name in the diff block for its surface with an explicit result: satisfied or finding. Surface-level acknowledgment without per-field enumeration is a partial artifact. The template offers no condensed form as an alternative. Per-field enumeration is the only valid form for any surface, clean or otherwise.

**Rule 5 — Attribution permanence.**
Contract Author's authorship of Phase 1 is permanently attributed at this point — before any Expected content is written. Attribution may not be retroactively disclaimed by Contract Author or claimed by Automate. Any Phase 1 entry that Automate believes is incorrect is a finding. This permanence does not wait for the gate — it is established now by Rule 5.

These rules bind Contract Author beginning now. Automate is not bound by these rules — Automate does not read them.

---

### Contract Author — Phase 1

**Step 1 — Contract Scope**

Write a `## Contract Scope` section. The section must be self-contained — a reader must be able to understand what is being tested without opening any external file:
- Operation name and HTTP method (or equivalent)
- Connector or Automate context and environment
- Input fixture — stated inline; do not reference external files
- Spec version and section governing the output contract for this operation

---

**Step 2 — Expected Output**

Write the `## Expected Output` section from the spec alone. Apply Rule 1 (every element cites a spec clause) and Rule 2 (three independent surface blocks).

**Block: Success Path**
Expected nominal output for nominal input. For each field:

```
[field-name]: [expected value or shape]
spec: [spec clause that requires this field and value]
```

**Block: Error Path**
Expected error response for malformed, missing, or unauthorized input. For each field:

```
[field-name]: [expected value or shape]
spec: [spec clause that requires this field and value]
```

If the spec does not define an error contract for this operation: `Error path: not specified in spec — Contract Author omits. This surface is not available for diff.`

**Block: Edge Case — [name the specific edge condition]**
Expected behavior for at least one edge condition (empty collection, null required field, auth expiry, overflow, rate-limit trigger). Name the edge condition in the block heading. For each field:

```
[field-name]: [expected value or shape]
spec: [spec clause that requires this field and value]
```

---

**Step 2B — Mechanism Taxonomy (Rule 3 — declare and seal before the gate)**

Write the taxonomy under `## Mechanism Taxonomy (sealed pre-gate)`.

This is Contract Author's prediction of the failure modes this operation is susceptible to, derived from reading the spec. Phase 3 authors are bound to this vocabulary from gate commit forward.

| Mechanism | Failure Mode |
|-----------|-------------|
| field-mapping-gap | A field required by the contract is absent in the output or mapped to the wrong path |
| wrong-enum | An enumerated value serialized using the wrong member |
| serialization-path | A value exists internally but is transformed incorrectly during output (wrong type, encoding, or format) |
| missing-guard | A conditional branch that should handle an error or edge is absent, causing fallthrough |
| logic-branch | The implementation selects the wrong execution path for the given input |
| contract-ambiguity | The spec clause governing this element is underspecified or contradictory |

Add mechanisms only if this operation's spec makes additional failure modes plausible — state the spec basis for each addition. Remove only with written justification. This list is sealed at the gate. After the gate, Phase 3 authors must select from this exact list.

**Incomplete Taxonomy Fallback — REQUIRED:** If no listed mechanism fits a finding's causal chain, use the closest mechanism from the sealed list and explain the gap in the explanation field. Do not introduce an unlisted mechanism label — the taxonomy is sealed and the gap explanation keeps the record honest.

---

**COMMIT GATE**

When Expected Output blocks and Mechanism Taxonomy are both complete, write this gate exactly:

> `[CONTRACT COMMITTED — the following acts are permanently frozen at this gate:`
> `(1) Contract content: the Expected Output blocks above are frozen and may not be modified, supplemented, annotated, or corrected after this line.`
> `(2) Expected authorship: Contract Author's attribution of Phase 1 is closed. Automate may not claim authorship of or modify any Phase 1 entry.`
> `(3) Mechanism taxonomy: the vocabulary declared in Step 2B is sealed. No mechanism may be added, renamed, or removed by Phase 3 authors. Selection is restricted to the exact list above.`
> `All three freezes take effect simultaneously at this gate. Automate begins here.]`

---

### Automate — Phase 2 begins here

The Contract Author has committed the expected output, closed authorship, and sealed the mechanism taxonomy above. DO NOT modify any Phase 1 content. Any disagreement with a Phase 1 entry is a finding — not a correction.

---

**Step 3 — Actual Output**

Run or simulate the operation against the input fixture. Write the `## Actual Output` section. Include: status code, full response body, all relevant headers, observable side effects.

---

**Step 4 — Diff**

Write one labeled diff block per contract surface from Phase 1. Every block is required — including surfaces with no deviations. Rule 4 applies: for every field declared in Phase 1 under each surface, write the field name and its result explicitly. No surface may be collapsed to a single acknowledgment line.

**Diff Block: Success Path**
For each field declared in Phase 1 under Success Path:
- `✓ [field-name] — [expected value]: satisfied` if actual matches expected
- Or open a finding: `→ F-NN: [field-name] — expected [X], actual [Y]`

All fields from the Phase 1 Success Path block must appear. No field may be silently omitted.

**Diff Block: Error Path**
For each field declared in Phase 1 under Error Path, write the field name and result. If Phase 1 declared this surface as omitted: `Error path: omitted in Phase 1 — no diff possible.`

All declared fields must appear by name.

**Diff Block: Edge Case — [name from Phase 1]**
For each field declared in Phase 1 under this edge, write the field name and result. All declared fields must appear by name.

---

**Step 5 — Findings**

For every deviation found in any diff block, write a complete finding entry. All fields are required:

```
Finding F-NN
surface: success | error | edge
deviation: [expected X per Phase 1, actual Y per Phase 2 — both sides required]
severity: breaking | degraded | cosmetic
spec: [spec clause cited in Phase 1 for this element — must match a Phase 1 citation]
hypothesis:
  mechanism: [select from the taxonomy sealed in Phase 1 — must be a declared mechanism]
  explanation: [causal chain — see hypothesis rules below]
recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
```

Severity definitions:
- `breaking` — a consumer relying on the contract cannot function correctly
- `degraded` — the operation runs but violates a guarantee; silent failure or data loss is possible
- `cosmetic` — the output differs from the contract in a way that does not affect correctness or consumer behavior

**Hypothesis rules — read before writing any explanation:**

A valid hypothesis names the mechanism AND explains the causal chain that produced this specific deviation. Example of a valid hypothesis: "The trigger-payload deserializer omits nullable fields rather than mapping them to null, so `connectionId` is absent in the response when the connection is in a pending state."

Three prohibited forms:

1. **Direct symptom restatement** — DO NOT write "The output did not match the expected value" or "The actual value was different from what was specified." These describe what happened, not why.

2. **Mechanism-dress restatement** — DO NOT write "The field-mapping-gap caused the field to be absent" or "The serialization-path produced an incorrect output format." Naming the mechanism category is not sufficient. The explanation must state WHY the mechanism produced this specific deviation for this specific input. Example of mechanism-dress restatement that is prohibited: "The serialization-path mechanism produced an incorrect result" — mechanism named, causal chain absent.

3. **Black-box hedge** — DO NOT write "Something in the output pipeline may have caused a mismatch" or "It is unclear what caused the field to be absent." If the mechanism is uncertain: name the most plausible mechanism from the sealed taxonomy, explain the causal chain that makes it plausible given the observable evidence, and acknowledge the uncertainty explicitly in the explanation — do not abandon the causal chain for a hedge.

Recommendation is required for every finding at every severity — including cosmetic.

---

**Step 6 — Summary**

Write a `## Summary` section with three reporting axes. The axes must occupy distinct format registers — Axis 1 is a compact line, Axis 2 is a table, Axis 3 is a labeled compact line.

**Axis 1 — Severity distribution (compact line):**
`breaking: N | degraded: N | cosmetic: N | total: N`

**Axis 2 — Mechanism distribution (table):**

| Mechanism | Count |
|-----------|-------|
| [mechanism-name] | N |

(Only mechanisms with ≥1 finding. Omit mechanisms with zero count.)

**Axis 3 — Surface finding distribution (compact line):**

**Surface status:** `success: N findings | error: N findings | edge: N findings`

Do not render Axis 3 as a table — a table in this position uses the same format register as Axis 2 and cannot be distinguished from mechanism distribution on document scan.

**Verdict:** `Contract violated` or `Contract satisfied`

**Recommendations (all findings, including cosmetic):**
`F-NN recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Both Prohibitions Named, Label Separated from Pipe Sequence

**Axis:** Lifecycle emphasis — both failure-form prohibitions present (C-39 PASS); axis label "**Axis 3 — Surface finding distribution:**" appears as a section heading with instructions between the label and the pipe sequence, so the label is not immediately before the pipe-sequence line (C-38 PARTIAL)

**Hypothesis:** C-39 PASS because both the table-row form and the prose-sentence form are explicitly named as non-compliant. C-38 PARTIAL because the label is a heading that precedes intervening instruction text; the pipe-sequence line itself does not carry the label. A reader encountering only `success: N findings | error: N findings | edge: N findings` in isolation cannot identify it as the surface-status axis without reading the heading above. The line is not self-announcing — axis identity still requires structural context.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state description or inline fixture — state inline, do not reference external files}
**Spec source:** {spec file path and section — e.g., signal-trace-2026-03-14.md§trace-contract}

---

## Roles

**Contract Author (Role A)**
Owns: Pre-Authoring Rules, Phase 1 (Contract Scope, Expected Output, Mechanism Taxonomy, Commit Gate).
Has not run the operation. Has not observed any runtime output. Reads the spec alone.
Role ends when the commit gate line is written. Attribution of Phase 1 content is permanent from this point forward.

**Automate (Role B)**
Owns: Phase 2 (Actual Output), Phase 3 (Diff), Phase 4 (Findings), Phase 5 (Summary).
Does not read the Pre-Authoring Rules section or Phase 1 authoring instructions.
Reads Phase 1 output only — the Contract Scope, Expected Output blocks, and Mechanism Taxonomy table.
Begins work at the `[CONTRACT COMMITTED]` gate line.
MUST NOT modify, annotate, correct, or supplement Phase 1 content. Any belief that a Phase 1 entry is incorrect is a finding, not a license to edit.

> **Automate: stop reading here. Scroll to the `[CONTRACT COMMITTED]` line. Your section begins immediately after it.**

---

## Pre-Authoring Rules — Role A reads; Role B stops here

These are binding authoring constraints for Contract Author. These rules take effect now, before any Expected content is written.

**Rule 1 — Spec-anchoring imperative.**
Every expected value in Phase 1 must cite the spec clause that requires it. An expected value without a spec reference is not a valid contract entry. Remove it or find the reference before the gate. Do not carry unanchored entries past the gate. A section heading is not a clause reference — cite the specific clause within the section that makes the value required.

**Rule 2 — Independent surface block mandate.**
Phase 1 must contain three structurally independent labeled sections: Success Path, Error Path, and Edge Case. A flat list without section headings is not compliant. A table with a Surface column is not compliant. Each surface is its own labeled block. A surface with no entries must still appear — write the heading and state why no entries apply.

**Rule 3 — Pre-gate taxonomy declaration requirement.**
The mechanism taxonomy must be declared inside Phase 1, before the commit gate. The vocabulary is binding on Phase 3 authors at gate commit. No mechanism may be added, renamed, or removed in Phase 3. Declaring the taxonomy after the gate is not permitted.

**Rule 4 — Per-field diff enumeration.**
In Phase 3, every field declared in Phase 1 must appear by name in the diff block for its surface with an explicit result: satisfied or finding. Surface-level acknowledgment without per-field enumeration is a partial artifact. The template offers no condensed form as an alternative. Per-field enumeration is the only valid form for any surface, clean or otherwise.

**Rule 5 — Attribution permanence.**
Contract Author's authorship of Phase 1 is permanently attributed at this point — before any Expected content is written. Attribution may not be retroactively disclaimed by Contract Author or claimed by Automate. Any Phase 1 entry that Automate believes is incorrect is a finding. This permanence does not wait for the gate — it is established now by Rule 5.

These rules bind Contract Author beginning now. Automate is not bound by these rules — Automate does not read them.

---

### Contract Author — Phase 1

**Step 1 — Contract Scope**

Write a `## Contract Scope` section. The section must be self-contained — a reader must be able to understand what is being tested without opening any external file:
- Operation name and HTTP method (or equivalent)
- Connector or Automate context and environment
- Input fixture — stated inline; do not reference external files
- Spec version and section governing the output contract for this operation

---

**Step 2 — Expected Output**

Write the `## Expected Output` section from the spec alone. Apply Rule 1 (every element cites a spec clause) and Rule 2 (three independent surface blocks).

**Block: Success Path**
Expected nominal output for nominal input. For each field:

```
[field-name]: [expected value or shape]
spec: [spec clause that requires this field and value]
```

**Block: Error Path**
Expected error response for malformed, missing, or unauthorized input. For each field:

```
[field-name]: [expected value or shape]
spec: [spec clause that requires this field and value]
```

If the spec does not define an error contract for this operation: `Error path: not specified in spec — Contract Author omits. This surface is not available for diff.`

**Block: Edge Case — [name the specific edge condition]**
Expected behavior for at least one edge condition (empty collection, null required field, auth expiry, overflow, rate-limit trigger). Name the edge condition in the block heading. For each field:

```
[field-name]: [expected value or shape]
spec: [spec clause that requires this field and value]
```

---

**Step 2B — Mechanism Taxonomy (Rule 3 — declare and seal before the gate)**

Write the taxonomy under `## Mechanism Taxonomy (sealed pre-gate)`.

This is Contract Author's prediction of the failure modes this operation is susceptible to, derived from reading the spec. Phase 3 authors are bound to this vocabulary from gate commit forward.

| Mechanism | Failure Mode |
|-----------|-------------|
| field-mapping-gap | A field required by the contract is absent in the output or mapped to the wrong path |
| wrong-enum | An enumerated value serialized using the wrong member |
| serialization-path | A value exists internally but is transformed incorrectly during output (wrong type, encoding, or format) |
| missing-guard | A conditional branch that should handle an error or edge is absent, causing fallthrough |
| logic-branch | The implementation selects the wrong execution path for the given input |
| contract-ambiguity | The spec clause governing this element is underspecified or contradictory |

Add mechanisms only if this operation's spec makes additional failure modes plausible — state the spec basis for each addition. Remove only with written justification. This list is sealed at the gate. After the gate, Phase 3 authors must select from this exact list.

**Incomplete Taxonomy Fallback — REQUIRED:** If no listed mechanism fits a finding's causal chain, use the closest mechanism from the sealed list and explain the gap in the explanation field. Do not introduce an unlisted mechanism label — the taxonomy is sealed and the gap explanation keeps the record honest.

---

**COMMIT GATE**

When Expected Output blocks and Mechanism Taxonomy are both complete, write this gate exactly:

> `[CONTRACT COMMITTED — the following acts are permanently frozen at this gate:`
> `(1) Contract content: the Expected Output blocks above are frozen and may not be modified, supplemented, annotated, or corrected after this line.`
> `(2) Expected authorship: Contract Author's attribution of Phase 1 is closed. Automate may not claim authorship of or modify any Phase 1 entry.`
> `(3) Mechanism taxonomy: the vocabulary declared in Step 2B is sealed. No mechanism may be added, renamed, or removed by Phase 3 authors. Selection is restricted to the exact list above.`
> `All three freezes take effect simultaneously at this gate. Automate begins here.]`

---

### Automate — Phase 2 begins here

The Contract Author has committed the expected output, closed authorship, and sealed the mechanism taxonomy above. DO NOT modify any Phase 1 content. Any disagreement with a Phase 1 entry is a finding — not a correction.

---

**Step 3 — Actual Output**

Run or simulate the operation against the input fixture. Write the `## Actual Output` section. Include: status code, full response body, all relevant headers, observable side effects.

---

**Step 4 — Diff**

Write one labeled diff block per contract surface from Phase 1. Every block is required — including surfaces with no deviations. Rule 4 applies: for every field declared in Phase 1 under each surface, write the field name and its result explicitly. No surface may be collapsed to a single acknowledgment line.

**Diff Block: Success Path**
For each field declared in Phase 1 under Success Path:
- `✓ [field-name] — [expected value]: satisfied` if actual matches expected
- Or open a finding: `→ F-NN: [field-name] — expected [X], actual [Y]`

All fields from the Phase 1 Success Path block must appear. No field may be silently omitted.

**Diff Block: Error Path**
For each field declared in Phase 1 under Error Path, write the field name and result. If Phase 1 declared this surface as omitted: `Error path: omitted in Phase 1 — no diff possible.`

All declared fields must appear by name.

**Diff Block: Edge Case — [name from Phase 1]**
For each field declared in Phase 1 under this edge, write the field name and result. All declared fields must appear by name.

---

**Step 5 — Findings**

For every deviation found in any diff block, write a complete finding entry. All fields are required:

```
Finding F-NN
surface: success | error | edge
deviation: [expected X per Phase 1, actual Y per Phase 2 — both sides required]
severity: breaking | degraded | cosmetic
spec: [spec clause cited in Phase 1 for this element — must match a Phase 1 citation]
hypothesis:
  mechanism: [select from the taxonomy sealed in Phase 1 — must be a declared mechanism]
  explanation: [causal chain — see hypothesis rules below]
recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
```

Severity definitions:
- `breaking` — a consumer relying on the contract cannot function correctly
- `degraded` — the operation runs but violates a guarantee; silent failure or data loss is possible
- `cosmetic` — the output differs from the contract in a way that does not affect correctness or consumer behavior

**Hypothesis rules — read before writing any explanation:**

A valid hypothesis names the mechanism AND explains the causal chain that produced this specific deviation. Example of a valid hypothesis: "The trigger-payload deserializer omits nullable fields rather than mapping them to null, so `connectionId` is absent in the response when the connection is in a pending state."

Three prohibited forms:

1. **Direct symptom restatement** — DO NOT write "The output did not match the expected value" or "The actual value was different from what was specified." These describe what happened, not why.

2. **Mechanism-dress restatement** — DO NOT write "The field-mapping-gap caused the field to be absent" or "The serialization-path produced an incorrect output format." Naming the mechanism category is not sufficient. The explanation must state WHY the mechanism produced this specific deviation for this specific input. Example of mechanism-dress restatement that is prohibited: "The serialization-path mechanism produced an incorrect result" — mechanism named, causal chain absent.

3. **Black-box hedge** — DO NOT write "Something in the output pipeline may have caused a mismatch" or "It is unclear what caused the field to be absent." If the mechanism is uncertain: name the most plausible mechanism from the sealed taxonomy, explain the causal chain that makes it plausible given the observable evidence, and acknowledge the uncertainty explicitly in the explanation — do not abandon the causal chain for a hedge.

Recommendation is required for every finding at every severity — including cosmetic.

---

**Step 6 — Summary**

Write a `## Summary` section with three reporting axes in fixed format registers.

**Axis 1 — Severity distribution (compact line):**
`breaking: N | degraded: N | cosmetic: N | total: N`

**Axis 2 — Mechanism distribution (table):**

| Mechanism | Count |
|-----------|-------|
| [mechanism-name] | N |

(Only mechanisms with ≥1 finding. Omit mechanisms with zero count.)

**Axis 3 — Surface finding distribution:**

Use the pipe-delimited compact line exactly as shown. The following two forms are non-compliant and must not be used:

- **Table-row form not compliant:** Do not embed surface counts as rows in a shared table alongside severity or mechanism counts. This collapses Axis 3 into the same format register as Axis 2, making the surface dimension indistinguishable from mechanism distribution on document scan.
- **Prose-sentence form not compliant:** Do not embed surface counts as a prose sentence or parenthetical (e.g., "success (N), error (N), edge (N)"). This collapses Axis 3 into the same format register as Axis 1, absorbing the surface dimension into the severity narrative.

Compliant form:
`success: N findings | error: N findings | edge: N findings`

**Verdict:** `Contract violated` or `Contract satisfied`

**Recommendations (all findings, including cosmetic):**
`F-NN recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Inline Label + Both Prohibitions Named

**Axis:** Phrasing register — "**Surface status:**" label inline immediately before the pipe sequence; both prohibited forms named with a concrete example of each

**Hypothesis:** C-38 PASS because the label appears on the same structural unit as the pipe sequence — a reader encountering the line alone identifies the surface dimension from the label without structural context. C-39 PASS because both the table-row form and the prose-sentence form are explicitly named as non-compliant, each with a concrete example. Both criteria satisfied simultaneously with strong imperative phrasing — a single-axis variation demonstrating they can be co-satisfied without the causal rationale of V-04.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state description or inline fixture — state inline, do not reference external files}
**Spec source:** {spec file path and section — e.g., signal-trace-2026-03-14.md§trace-contract}

---

## Roles

**Contract Author (Role A)**
Owns: Pre-Authoring Rules, Phase 1 (Contract Scope, Expected Output, Mechanism Taxonomy, Commit Gate).
Has not run the operation. Has not observed any runtime output. Reads the spec alone.
Role ends when the commit gate line is written. Attribution of Phase 1 content is permanent from this point forward.

**Automate (Role B)**
Owns: Phase 2 (Actual Output), Phase 3 (Diff), Phase 4 (Findings), Phase 5 (Summary).
Does not read the Pre-Authoring Rules section or Phase 1 authoring instructions.
Reads Phase 1 output only — the Contract Scope, Expected Output blocks, and Mechanism Taxonomy table.
Begins work at the `[CONTRACT COMMITTED]` gate line.
MUST NOT modify, annotate, correct, or supplement Phase 1 content. Any belief that a Phase 1 entry is incorrect is a finding, not a license to edit.

> **Automate: stop reading here. Scroll to the `[CONTRACT COMMITTED]` line. Your section begins immediately after it.**

---

## Pre-Authoring Rules — Role A reads; Role B stops here

These are binding authoring constraints for Contract Author. These rules take effect now, before any Expected content is written.

**Rule 1 — Spec-anchoring imperative.**
Every expected value in Phase 1 must cite the spec clause that requires it. An expected value without a spec reference is not a valid contract entry. Remove it or find the reference before the gate. Do not carry unanchored entries past the gate. A section heading is not a clause reference — cite the specific clause within the section that makes the value required.

**Rule 2 — Independent surface block mandate.**
Phase 1 must contain three structurally independent labeled sections: Success Path, Error Path, and Edge Case. A flat list without section headings is not compliant. A table with a Surface column is not compliant. Each surface is its own labeled block. A surface with no entries must still appear — write the heading and state why no entries apply.

**Rule 3 — Pre-gate taxonomy declaration requirement.**
The mechanism taxonomy must be declared inside Phase 1, before the commit gate. The vocabulary is binding on Phase 3 authors at gate commit. No mechanism may be added, renamed, or removed in Phase 3. Declaring the taxonomy after the gate is not permitted.

**Rule 4 — Per-field diff enumeration.**
In Phase 3, every field declared in Phase 1 must appear by name in the diff block for its surface with an explicit result: satisfied or finding. Surface-level acknowledgment without per-field enumeration is a partial artifact. The template offers no condensed form as an alternative. Per-field enumeration is the only valid form for any surface, clean or otherwise.

**Rule 5 — Attribution permanence.**
Contract Author's authorship of Phase 1 is permanently attributed at this point — before any Expected content is written. Attribution may not be retroactively disclaimed by Contract Author or claimed by Automate. Any Phase 1 entry that Automate believes is incorrect is a finding. This permanence does not wait for the gate — it is established now by Rule 5.

These rules bind Contract Author beginning now. Automate is not bound by these rules — Automate does not read them.

---

### Contract Author — Phase 1

**Step 1 — Contract Scope**

Write a `## Contract Scope` section. The section must be self-contained — a reader must be able to understand what is being tested without opening any external file:
- Operation name and HTTP method (or equivalent)
- Connector or Automate context and environment
- Input fixture — stated inline; do not reference external files
- Spec version and section governing the output contract for this operation

---

**Step 2 — Expected Output**

Write the `## Expected Output` section from the spec alone. Apply Rule 1 (every element cites a spec clause) and Rule 2 (three independent surface blocks).

**Block: Success Path**
Expected nominal output for nominal input. For each field:

```
[field-name]: [expected value or shape]
spec: [spec clause that requires this field and value]
```

**Block: Error Path**
Expected error response for malformed, missing, or unauthorized input. For each field:

```
[field-name]: [expected value or shape]
spec: [spec clause that requires this field and value]
```

If the spec does not define an error contract for this operation: `Error path: not specified in spec — Contract Author omits. This surface is not available for diff.`

**Block: Edge Case — [name the specific edge condition]**
Expected behavior for at least one edge condition (empty collection, null required field, auth expiry, overflow, rate-limit trigger). Name the edge condition in the block heading. For each field:

```
[field-name]: [expected value or shape]
spec: [spec clause that requires this field and value]
```

---

**Step 2B — Mechanism Taxonomy (Rule 3 — declare and seal before the gate)**

Write the taxonomy under `## Mechanism Taxonomy (sealed pre-gate)`.

This is Contract Author's prediction of the failure modes this operation is susceptible to, derived from reading the spec. Phase 3 authors are bound to this vocabulary from gate commit forward.

| Mechanism | Failure Mode |
|-----------|-------------|
| field-mapping-gap | A field required by the contract is absent in the output or mapped to the wrong path |
| wrong-enum | An enumerated value serialized using the wrong member |
| serialization-path | A value exists internally but is transformed incorrectly during output (wrong type, encoding, or format) |
| missing-guard | A conditional branch that should handle an error or edge is absent, causing fallthrough |
| logic-branch | The implementation selects the wrong execution path for the given input |
| contract-ambiguity | The spec clause governing this element is underspecified or contradictory |

Add mechanisms only if this operation's spec makes additional failure modes plausible — state the spec basis for each addition. Remove only with written justification. This list is sealed at the gate. After the gate, Phase 3 authors must select from this exact list.

**Incomplete Taxonomy Fallback — REQUIRED:** If no listed mechanism fits a finding's causal chain, use the closest mechanism from the sealed list and explain the gap in the explanation field. Do not introduce an unlisted mechanism label — the taxonomy is sealed and the gap explanation keeps the record honest.

---

**COMMIT GATE**

When Expected Output blocks and Mechanism Taxonomy are both complete, write this gate exactly:

> `[CONTRACT COMMITTED — the following acts are permanently frozen at this gate:`
> `(1) Contract content: the Expected Output blocks above are frozen and may not be modified, supplemented, annotated, or corrected after this line.`
> `(2) Expected authorship: Contract Author's attribution of Phase 1 is closed. Automate may not claim authorship of or modify any Phase 1 entry.`
> `(3) Mechanism taxonomy: the vocabulary declared in Step 2B is sealed. No mechanism may be added, renamed, or removed by Phase 3 authors. Selection is restricted to the exact list above.`
> `All three freezes take effect simultaneously at this gate. Automate begins here.]`

---

### Automate — Phase 2 begins here

The Contract Author has committed the expected output, closed authorship, and sealed the mechanism taxonomy above. DO NOT modify any Phase 1 content. Any disagreement with a Phase 1 entry is a finding — not a correction.

---

**Step 3 — Actual Output**

Run or simulate the operation against the input fixture. Write the `## Actual Output` section. Include: status code, full response body, all relevant headers, observable side effects.

---

**Step 4 — Diff**

Write one labeled diff block per contract surface from Phase 1. Every block is required — including surfaces with no deviations. Rule 4 applies: for every field declared in Phase 1 under each surface, write the field name and its result explicitly. No surface may be collapsed to a single acknowledgment line.

**Diff Block: Success Path**
For each field declared in Phase 1 under Success Path:
- `✓ [field-name] — [expected value]: satisfied` if actual matches expected
- Or open a finding: `→ F-NN: [field-name] — expected [X], actual [Y]`

All fields from the Phase 1 Success Path block must appear. No field may be silently omitted.

**Diff Block: Error Path**
For each field declared in Phase 1 under Error Path, write the field name and result. If Phase 1 declared this surface as omitted: `Error path: omitted in Phase 1 — no diff possible.`

All declared fields must appear by name.

**Diff Block: Edge Case — [name from Phase 1]**
For each field declared in Phase 1 under this edge, write the field name and result. All declared fields must appear by name.

---

**Step 5 — Findings**

For every deviation found in any diff block, write a complete finding entry. All fields are required:

```
Finding F-NN
surface: success | error | edge
deviation: [expected X per Phase 1, actual Y per Phase 2 — both sides required]
severity: breaking | degraded | cosmetic
spec: [spec clause cited in Phase 1 for this element — must match a Phase 1 citation]
hypothesis:
  mechanism: [select from the taxonomy sealed in Phase 1 — must be a declared mechanism]
  explanation: [causal chain — see hypothesis rules below]
recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
```

Severity definitions:
- `breaking` — a consumer relying on the contract cannot function correctly
- `degraded` — the operation runs but violates a guarantee; silent failure or data loss is possible
- `cosmetic` — the output differs from the contract in a way that does not affect correctness or consumer behavior

**Hypothesis rules — read before writing any explanation:**

A valid hypothesis names the mechanism AND explains the causal chain that produced this specific deviation. Example of a valid hypothesis: "The trigger-payload deserializer omits nullable fields rather than mapping them to null, so `connectionId` is absent in the response when the connection is in a pending state."

Three prohibited forms:

1. **Direct symptom restatement** — DO NOT write "The output did not match the expected value" or "The actual value was different from what was specified." These describe what happened, not why.

2. **Mechanism-dress restatement** — DO NOT write "The field-mapping-gap caused the field to be absent" or "The serialization-path produced an incorrect output format." Naming the mechanism category is not sufficient. The explanation must state WHY the mechanism produced this specific deviation for this specific input. Example of mechanism-dress restatement that is prohibited: "The serialization-path mechanism produced an incorrect result" — mechanism named, causal chain absent.

3. **Black-box hedge** — DO NOT write "Something in the output pipeline may have caused a mismatch" or "It is unclear what caused the field to be absent." If the mechanism is uncertain: name the most plausible mechanism from the sealed taxonomy, explain the causal chain that makes it plausible given the observable evidence, and acknowledge the uncertainty explicitly in the explanation — do not abandon the causal chain for a hedge.

Recommendation is required for every finding at every severity — including cosmetic.

---

**Step 6 — Summary**

Write a `## Summary` section. Three reporting axes are required. Each axis occupies a distinct format register — the registers are fixed and non-interchangeable.

**Axis 1 — Severity distribution (compact line):**
`breaking: N | degraded: N | cosmetic: N | total: N`

**Axis 2 — Mechanism distribution (table):**

| Mechanism | Count |
|-----------|-------|
| [mechanism-name] | N |

(Only mechanisms with ≥1 finding. Omit mechanisms with zero count.)

**Axis 3 — Surface finding distribution (compact line — self-labeled):**

Write the surface-status line in this exact form. The label must appear immediately before the pipe-delimited count sequence on the same structural unit — the label is what makes the line identifiable in isolation:

**Surface status:** `success: N findings | error: N findings | edge: N findings`

The following two forms are not compliant and must not be used:

1. **Table-row form not compliant** — Do not render surface counts as rows in a shared table alongside severity or mechanism counts. Example of prohibited form: `| Surface | success: N, error: N, edge: N |` as a row in a Dimension table. A table in this position uses the same format register as Axis 2 and is indistinguishable from mechanism distribution on document scan.

2. **Prose-sentence form not compliant** — Do not embed surface counts as a prose sentence or parenthetical. Example of prohibited form: "**Surface distribution:** success (N), error (N), edge (N)." Prose embedding uses the same format register as Axis 1 and absorbs the surface dimension into the severity narrative.

**Verdict:** `Contract violated` or `Contract satisfied`

**Recommendations (all findings, including cosmetic):**
`F-NN recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Inline Label + Both Prohibitions with Structural-Consequence Rationale

**Axis:** Role sequence + output format — C-38 and C-39 both satisfied; each prohibition includes a structural-consequence explanation of the failure mode it prevents

**Hypothesis:** C-38 PASS (label inline before pipe sequence). C-39 PASS (both forms named). The addition over V-03: each prohibition names the structural consequence of using the alternative form — register collision for the table form, register absorption for the prose form. Authors cannot rationalize the non-compliant form as a cosmetic preference because the rationale makes the structural damage legible and testable.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state description or inline fixture — state inline, do not reference external files}
**Spec source:** {spec file path and section — e.g., signal-trace-2026-03-14.md§trace-contract}

---

## Roles

**Contract Author (Role A)**
Owns: Pre-Authoring Rules, Phase 1 (Contract Scope, Expected Output, Mechanism Taxonomy, Commit Gate).
Has not run the operation. Has not observed any runtime output. Reads the spec alone.
Role ends when the commit gate line is written. Attribution of Phase 1 content is permanent from this point forward.

**Automate (Role B)**
Owns: Phase 2 (Actual Output), Phase 3 (Diff), Phase 4 (Findings), Phase 5 (Summary).
Does not read the Pre-Authoring Rules section or Phase 1 authoring instructions.
Reads Phase 1 output only — the Contract Scope, Expected Output blocks, and Mechanism Taxonomy table.
Begins work at the `[CONTRACT COMMITTED]` gate line.
MUST NOT modify, annotate, correct, or supplement Phase 1 content. Any belief that a Phase 1 entry is incorrect is a finding, not a license to edit.

> **Automate: stop reading here. Scroll to the `[CONTRACT COMMITTED]` line. Your section begins immediately after it.**

---

## Pre-Authoring Rules — Role A reads; Role B stops here

These are binding authoring constraints for Contract Author. These rules take effect now, before any Expected content is written.

**Rule 1 — Spec-anchoring imperative.**
Every expected value in Phase 1 must cite the spec clause that requires it. An expected value without a spec reference is not a valid contract entry. Remove it or find the reference before the gate. Do not carry unanchored entries past the gate. A section heading is not a clause reference — cite the specific clause within the section that makes the value required.

**Rule 2 — Independent surface block mandate.**
Phase 1 must contain three structurally independent labeled sections: Success Path, Error Path, and Edge Case. A flat list without section headings is not compliant. A table with a Surface column is not compliant. Each surface is its own labeled block. A surface with no entries must still appear — write the heading and state why no entries apply.

**Rule 3 — Pre-gate taxonomy declaration requirement.**
The mechanism taxonomy must be declared inside Phase 1, before the commit gate. The vocabulary is binding on Phase 3 authors at gate commit. No mechanism may be added, renamed, or removed in Phase 3. Declaring the taxonomy after the gate is not permitted.

**Rule 4 — Per-field diff enumeration.**
In Phase 3, every field declared in Phase 1 must appear by name in the diff block for its surface with an explicit result: satisfied or finding. Surface-level acknowledgment without per-field enumeration is a partial artifact. The template offers no condensed form as an alternative. Per-field enumeration is the only valid form for any surface, clean or otherwise.

**Rule 5 — Attribution permanence.**
Contract Author's authorship of Phase 1 is permanently attributed at this point — before any Expected content is written. Attribution may not be retroactively disclaimed by Contract Author or claimed by Automate. Any Phase 1 entry that Automate believes is incorrect is a finding. This permanence does not wait for the gate — it is established now by Rule 5.

These rules bind Contract Author beginning now. Automate is not bound by these rules — Automate does not read them.

---

### Contract Author — Phase 1

**Step 1 — Contract Scope**

Write a `## Contract Scope` section. The section must be self-contained — a reader must be able to understand what is being tested without opening any external file:
- Operation name and HTTP method (or equivalent)
- Connector or Automate context and environment
- Input fixture — stated inline; do not reference external files
- Spec version and section governing the output contract for this operation

---

**Step 2 — Expected Output**

Write the `## Expected Output` section from the spec alone. Apply Rule 1 (every element cites a spec clause) and Rule 2 (three independent surface blocks).

**Block: Success Path**
Expected nominal output for nominal input. For each field:

```
[field-name]: [expected value or shape]
spec: [spec clause that requires this field and value]
```

**Block: Error Path**
Expected error response for malformed, missing, or unauthorized input. For each field:

```
[field-name]: [expected value or shape]
spec: [spec clause that requires this field and value]
```

If the spec does not define an error contract for this operation: `Error path: not specified in spec — Contract Author omits. This surface is not available for diff.`

**Block: Edge Case — [name the specific edge condition]**
Expected behavior for at least one edge condition (empty collection, null required field, auth expiry, overflow, rate-limit trigger). Name the edge condition in the block heading. For each field:

```
[field-name]: [expected value or shape]
spec: [spec clause that requires this field and value]
```

---

**Step 2B — Mechanism Taxonomy (Rule 3 — declare and seal before the gate)**

Write the taxonomy under `## Mechanism Taxonomy (sealed pre-gate)`.

This is Contract Author's prediction of the failure modes this operation is susceptible to, derived from reading the spec. Phase 3 authors are bound to this vocabulary from gate commit forward.

| Mechanism | Failure Mode |
|-----------|-------------|
| field-mapping-gap | A field required by the contract is absent in the output or mapped to the wrong path |
| wrong-enum | An enumerated value serialized using the wrong member |
| serialization-path | A value exists internally but is transformed incorrectly during output (wrong type, encoding, or format) |
| missing-guard | A conditional branch that should handle an error or edge is absent, causing fallthrough |
| logic-branch | The implementation selects the wrong execution path for the given input |
| contract-ambiguity | The spec clause governing this element is underspecified or contradictory |

Add mechanisms only if this operation's spec makes additional failure modes plausible — state the spec basis for each addition. Remove only with written justification. This list is sealed at the gate. After the gate, Phase 3 authors must select from this exact list.

**Incomplete Taxonomy Fallback — REQUIRED:** If no listed mechanism fits a finding's causal chain, use the closest mechanism from the sealed list and explain the gap in the explanation field. Do not introduce an unlisted mechanism label — the taxonomy is sealed and the gap explanation keeps the record honest.

---

**COMMIT GATE**

When Expected Output blocks and Mechanism Taxonomy are both complete, write this gate exactly:

> `[CONTRACT COMMITTED — the following acts are permanently frozen at this gate:`
> `(1) Contract content: the Expected Output blocks above are frozen and may not be modified, supplemented, annotated, or corrected after this line.`
> `(2) Expected authorship: Contract Author's attribution of Phase 1 is closed. Automate may not claim authorship of or modify any Phase 1 entry.`
> `(3) Mechanism taxonomy: the vocabulary declared in Step 2B is sealed. No mechanism may be added, renamed, or removed by Phase 3 authors. Selection is restricted to the exact list above.`
> `All three freezes take effect simultaneously at this gate. Automate begins here.]`

---

### Automate — Phase 2 begins here

The Contract Author has committed the expected output, closed authorship, and sealed the mechanism taxonomy above. DO NOT modify any Phase 1 content. Any disagreement with a Phase 1 entry is a finding — not a correction.

---

**Step 3 — Actual Output**

Run or simulate the operation against the input fixture. Write the `## Actual Output` section. Include: status code, full response body, all relevant headers, observable side effects.

---

**Step 4 — Diff**

Write one labeled diff block per contract surface from Phase 1. Every block is required — including surfaces with no deviations. Rule 4 applies: for every field declared in Phase 1 under each surface, write the field name and its result explicitly. No surface may be collapsed to a single acknowledgment line.

**Diff Block: Success Path**
For each field declared in Phase 1 under Success Path:
- `✓ [field-name] — [expected value]: satisfied` if actual matches expected
- Or open a finding: `→ F-NN: [field-name] — expected [X], actual [Y]`

All fields from the Phase 1 Success Path block must appear. No field may be silently omitted.

**Diff Block: Error Path**
For each field declared in Phase 1 under Error Path, write the field name and result. If Phase 1 declared this surface as omitted: `Error path: omitted in Phase 1 — no diff possible.`

All declared fields must appear by name.

**Diff Block: Edge Case — [name from Phase 1]**
For each field declared in Phase 1 under this edge, write the field name and result. All declared fields must appear by name.

---

**Step 5 — Findings**

For every deviation found in any diff block, write a complete finding entry. All fields are required:

```
Finding F-NN
surface: success | error | edge
deviation: [expected X per Phase 1, actual Y per Phase 2 — both sides required]
severity: breaking | degraded | cosmetic
spec: [spec clause cited in Phase 1 for this element — must match a Phase 1 citation]
hypothesis:
  mechanism: [select from the taxonomy sealed in Phase 1 — must be a declared mechanism]
  explanation: [causal chain — see hypothesis rules below]
recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
```

Severity definitions:
- `breaking` — a consumer relying on the contract cannot function correctly
- `degraded` — the operation runs but violates a guarantee; silent failure or data loss is possible
- `cosmetic` — the output differs from the contract in a way that does not affect correctness or consumer behavior

**Hypothesis rules — read before writing any explanation:**

A valid hypothesis names the mechanism AND explains the causal chain that produced this specific deviation. Example of a valid hypothesis: "The trigger-payload deserializer omits nullable fields rather than mapping them to null, so `connectionId` is absent in the response when the connection is in a pending state."

Three prohibited forms:

1. **Direct symptom restatement** — DO NOT write "The output did not match the expected value" or "The actual value was different from what was specified." These describe what happened, not why.

2. **Mechanism-dress restatement** — DO NOT write "The field-mapping-gap caused the field to be absent" or "The serialization-path produced an incorrect output format." Naming the mechanism category is not sufficient. The explanation must state WHY the mechanism produced this specific deviation for this specific input. Example of mechanism-dress restatement that is prohibited: "The serialization-path mechanism produced an incorrect result" — mechanism named, causal chain absent.

3. **Black-box hedge** — DO NOT write "Something in the output pipeline may have caused a mismatch" or "It is unclear what caused the field to be absent." If the mechanism is uncertain: name the most plausible mechanism from the sealed taxonomy, explain the causal chain that makes it plausible given the observable evidence, and acknowledge the uncertainty explicitly in the explanation — do not abandon the causal chain for a hedge.

Recommendation is required for every finding at every severity — including cosmetic.

---

**Step 6 — Summary**

Write a `## Summary` section. The Summary has exactly three reporting axes, each in a fixed format register. The register assignment is a structural separability requirement — not a style choice. The three axes must be independently identifiable on document scan without reading axis content.

**Axis 1 — Severity distribution (compact line):**
`breaking: N | degraded: N | cosmetic: N | total: N`

**Axis 2 — Mechanism distribution (table):**

| Mechanism | Count |
|-----------|-------|
| [mechanism-name] | N |

(Only mechanisms with ≥1 finding. Omit mechanisms with zero count.)

**Axis 3 — Surface finding distribution (compact line — self-labeled):**

The surface-status line carries its own axis label immediately before the pipe-delimited count sequence. The label is a structural requirement — it makes the line self-announcing, so that a reader encountering the line in isolation identifies the surface dimension from the label alone without inferring it from format-register comparison with Axis 1 or Axis 2.

Required form:
**Surface status:** `success: N findings | error: N findings | edge: N findings`

Two forms are not compliant for Axis 3:

1. **Table-row form not compliant** — Do not embed surface counts as rows in a shared table alongside severity or mechanism counts. Structural consequence: a table in the Axis 3 slot occupies the same format register as Axis 2. A scanner cannot distinguish "findings by surface" from "findings by mechanism" without reading axis labels — structural separability between the mechanism and surface dimensions is lost. This is a structural failure, not a formatting preference.

2. **Prose-sentence form not compliant** — Do not embed surface counts as a prose sentence or continuation (e.g., "**Surface distribution:** success (N), error (N), edge (N)"). Structural consequence: prose embedding occupies the same format register as Axis 1. The surface dimension is absorbed into the severity narrative; a scanner encounters two compact-line items and cannot identify which is severity and which is surface without reading both.

**Verdict:** `Contract violated` or `Contract satisfied`

**Recommendations (all findings, including cosmetic):**
`F-NN recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — Full Platinum (C-08 through C-39)

**Axis:** Full platinum — C-38 and C-39 at maximum strength with R12-sourced failure-mode labels; V-04 structural-consequence rationale extended with three-consequence enumeration; complete R12 V-05 baseline throughout

**Hypothesis:** C-38 PASS at maximum strength — label is bold, inline, immediately before the pipe sequence, and accompanied by an explicit statement that the label enables axis-identity-in-isolation, not inferred from register comparison. C-39 PASS at maximum strength — both prohibited forms named with their R12 failure-mode labels ("table-register absorption" and "prose-register absorption"), each prohibition enumerates three structural consequences, and examples match the exact failure artifacts from R12. Authors can apply the prohibitions reflexively: "my Axis 3 looks like Axis 2 on scan" triggers the table-register absorption label; "my Axis 3 reads as a continuation of Axis 1" triggers the prose-register absorption label.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state description or inline fixture — state inline, do not reference external files}
**Spec source:** {spec file path and section — e.g., signal-trace-2026-03-14.md§trace-contract}

---

## Roles

**Contract Author (Role A)**
Owns: Pre-Authoring Rules, Phase 1 (Contract Scope, Expected Output, Mechanism Taxonomy, Commit Gate).
Has not run the operation. Has not observed any runtime output. Reads the spec alone.
Role ends when the commit gate line is written. Attribution of Phase 1 content is permanent from this point forward.

**Automate (Role B)**
Owns: Phase 2 (Actual Output), Phase 3 (Diff), Phase 4 (Findings), Phase 5 (Summary).
Does not read the Pre-Authoring Rules section or Phase 1 authoring instructions.
Reads Phase 1 output only — the Contract Scope, Expected Output blocks, and Mechanism Taxonomy table.
Begins work at the `[CONTRACT COMMITTED]` gate line.
MUST NOT modify, annotate, correct, or supplement Phase 1 content. Any belief that a Phase 1 entry is incorrect is a finding, not a license to edit.

> **Automate: stop reading here. Scroll to the `[CONTRACT COMMITTED]` line. Your section begins immediately after it.**

---

## Pre-Authoring Rules — Role A reads; Role B stops here

These are binding authoring constraints for Contract Author. These rules take effect now, before any Expected content is written.

**Rule 1 — Spec-anchoring imperative.**
Every expected value in Phase 1 must cite the spec clause that requires it. An expected value without a spec reference is not a valid contract entry. Remove it or find the reference before the gate. Do not carry unanchored entries past the gate. A section heading is not a clause reference — cite the specific clause within the section that makes the value required.

**Rule 2 — Independent surface block mandate.**
Phase 1 must contain three structurally independent labeled sections: Success Path, Error Path, and Edge Case. A flat list without section headings is not compliant. A table with a Surface column is not compliant. Each surface is its own labeled block. A surface with no entries must still appear — write the heading and state why no entries apply.

**Rule 3 — Pre-gate taxonomy declaration requirement.**
The mechanism taxonomy must be declared inside Phase 1, before the commit gate. The vocabulary is binding on Phase 3 authors at gate commit. No mechanism may be added, renamed, or removed in Phase 3. Declaring the taxonomy after the gate is not permitted.

**Rule 4 — Per-field diff enumeration.**
In Phase 3, every field declared in Phase 1 must appear by name in the diff block for its surface with an explicit result: satisfied or finding. Surface-level acknowledgment without per-field enumeration is a partial artifact. The template offers no condensed form as an alternative. Per-field enumeration is the only valid form for any surface, clean or otherwise.

**Rule 5 — Attribution permanence.**
Contract Author's authorship of Phase 1 is permanently attributed at this point — before any Expected content is written. Attribution may not be retroactively disclaimed by Contract Author or claimed by Automate. Any Phase 1 entry that Automate believes is incorrect is a finding. This permanence does not wait for the gate — it is established now by Rule 5.

These rules bind Contract Author beginning now. Automate is not bound by these rules — Automate does not read them.

---

### Contract Author — Phase 1

**Step 1 — Contract Scope**

Write a `## Contract Scope` section. The section must be self-contained — a reader must be able to understand what is being tested without opening any external file:
- Operation name and HTTP method (or equivalent)
- Connector or Automate context and environment
- Input fixture — stated inline; do not reference external files
- Spec version and section governing the output contract for this operation

---

**Step 2 — Expected Output**

Write the `## Expected Output` section from the spec alone. Apply Rule 1 (every element cites a spec clause) and Rule 2 (three independent surface blocks).

**Block: Success Path**
Expected nominal output for nominal input. For each field:

```
[field-name]: [expected value or shape]
spec: [spec clause that requires this field and value]
```

**Block: Error Path**
Expected error response for malformed, missing, or unauthorized input. For each field:

```
[field-name]: [expected value or shape]
spec: [spec clause that requires this field and value]
```

If the spec does not define an error contract for this operation: `Error path: not specified in spec — Contract Author omits. This surface is not available for diff.`

**Block: Edge Case — [name the specific edge condition]**
Expected behavior for at least one edge condition (empty collection, null required field, auth expiry, overflow, rate-limit trigger). Name the edge condition in the block heading. For each field:

```
[field-name]: [expected value or shape]
spec: [spec clause that requires this field and value]
```

---

**Step 2B — Mechanism Taxonomy (Rule 3 — declare and seal before the gate)**

Write the taxonomy under `## Mechanism Taxonomy (sealed pre-gate)`.

This is Contract Author's prediction of the failure modes this operation is susceptible to, derived from reading the spec. Phase 3 authors are bound to this vocabulary from gate commit forward.

| Mechanism | Failure Mode |
|-----------|-------------|
| field-mapping-gap | A field required by the contract is absent in the output or mapped to the wrong path |
| wrong-enum | An enumerated value serialized using the wrong member |
| serialization-path | A value exists internally but is transformed incorrectly during output (wrong type, encoding, or format) |
| missing-guard | A conditional branch that should handle an error or edge is absent, causing fallthrough |
| logic-branch | The implementation selects the wrong execution path for the given input |
| contract-ambiguity | The spec clause governing this element is underspecified or contradictory |

Add mechanisms only if this operation's spec makes additional failure modes plausible — state the spec basis for each addition. Remove only with written justification. This list is sealed at the gate. After the gate, Phase 3 authors must select from this exact list.

**Incomplete Taxonomy Fallback — REQUIRED:** If no listed mechanism fits a finding's causal chain, use the closest mechanism from the sealed list and explain the gap in the explanation field. Do not introduce an unlisted mechanism label — the taxonomy is sealed and the gap explanation keeps the record honest.

---

**COMMIT GATE**

When Expected Output blocks and Mechanism Taxonomy are both complete, write this gate exactly:

> `[CONTRACT COMMITTED — the following acts are permanently frozen at this gate:`
> `(1) Contract content: the Expected Output blocks above are frozen and may not be modified, supplemented, annotated, or corrected after this line.`
> `(2) Expected authorship: Contract Author's attribution of Phase 1 is closed. Automate may not claim authorship of or modify any Phase 1 entry.`
> `(3) Mechanism taxonomy: the vocabulary declared in Step 2B is sealed. No mechanism may be added, renamed, or removed by Phase 3 authors. Selection is restricted to the exact list above.`
> `All three freezes take effect simultaneously at this gate. Automate begins here.]`

---

### Automate — Phase 2 begins here

The Contract Author has committed the expected output, closed authorship, and sealed the mechanism taxonomy above. DO NOT modify any Phase 1 content. Any disagreement with a Phase 1 entry is a finding — not a correction.

---

**Step 3 — Actual Output**

Run or simulate the operation against the input fixture. Write the `## Actual Output` section. Include: status code, full response body, all relevant headers, observable side effects.

---

**Step 4 — Diff**

Write one labeled diff block per contract surface from Phase 1. Every block is required — including surfaces with no deviations. Rule 4 applies: for every field declared in Phase 1 under each surface, write the field name and its result explicitly. No surface may be collapsed to a single acknowledgment line.

**Diff Block: Success Path**
For each field declared in Phase 1 under Success Path:
- `✓ [field-name] — [expected value]: satisfied` if actual matches expected
- Or open a finding: `→ F-NN: [field-name] — expected [X], actual [Y]`

All fields from the Phase 1 Success Path block must appear. No field may be silently omitted.

**Diff Block: Error Path**
For each field declared in Phase 1 under Error Path, write the field name and result. If Phase 1 declared this surface as omitted: `Error path: omitted in Phase 1 — no diff possible.`

All declared fields must appear by name.

**Diff Block: Edge Case — [name from Phase 1]**
For each field declared in Phase 1 under this edge, write the field name and result. All declared fields must appear by name.

---

**Step 5 — Findings**

For every deviation found in any diff block, write a complete finding entry. All fields are required:

```
Finding F-NN
surface: success | error | edge
deviation: [expected X per Phase 1, actual Y per Phase 2 — both sides required]
severity: breaking | degraded | cosmetic
spec: [spec clause cited in Phase 1 for this element — must match a Phase 1 citation]
hypothesis:
  mechanism: [select from the taxonomy sealed in Phase 1 — must be a declared mechanism]
  explanation: [causal chain — see hypothesis rules below]
recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
```

Severity definitions:
- `breaking` — a consumer relying on the contract cannot function correctly
- `degraded` — the operation runs but violates a guarantee; silent failure or data loss is possible
- `cosmetic` — the output differs from the contract in a way that does not affect correctness or consumer behavior

**Hypothesis rules — read before writing any explanation:**

A valid hypothesis names the mechanism AND explains the causal chain that produced this specific deviation. Example of a valid hypothesis: "The trigger-payload deserializer omits nullable fields rather than mapping them to null, so `connectionId` is absent in the response when the connection is in a pending state."

Three prohibited forms:

1. **Direct symptom restatement** — DO NOT write "The output did not match the expected value" or "The actual value was different from what was specified." These describe what happened, not why.

2. **Mechanism-dress restatement** — DO NOT write "The field-mapping-gap caused the field to be absent" or "The serialization-path produced an incorrect output format." Naming the mechanism category is not sufficient. The explanation must state WHY the mechanism produced this specific deviation for this specific input. Example of mechanism-dress restatement that is prohibited: "The serialization-path mechanism produced an incorrect result" — mechanism named, causal chain absent.

3. **Black-box hedge** — DO NOT write "Something in the output pipeline may have caused a mismatch" or "It is unclear what caused the field to be absent." If the mechanism is uncertain: name the most plausible mechanism from the sealed taxonomy, explain the causal chain that makes it plausible given the observable evidence, and acknowledge the uncertainty explicitly in the explanation — do not abandon the causal chain for a hedge.

Recommendation is required for every finding at every severity — including cosmetic.

---

**Step 6 — Summary**

Write a `## Summary` section. The Summary contains exactly three reporting axes. Each axis occupies a distinct, fixed format register. The register assignment is a structural separability requirement — not a formatting convention. The purpose: each axis must be independently identifiable on document scan without reading any axis's content.

**Axis 1 — Severity distribution (compact line):**
`breaking: N | degraded: N | cosmetic: N | total: N`

**Axis 2 — Mechanism distribution (table — table register belongs to Axis 2 only):**

| Mechanism | Count |
|-----------|-------|
| [mechanism-name] | N |

(Only mechanisms with ≥1 finding. Omit mechanisms with zero count.)

**Axis 3 — Surface finding distribution (compact line — axis label required on same structural unit):**

The surface-status line must carry an explicit axis label printed immediately before the pipe-delimited count sequence. The label is a structural requirement, not a formatting preference. Its function: a reader encountering the line in any context — including in isolation, excerpted from the Summary — must be able to identify the surface dimension from the label alone, without inferring it by comparing the line's format register against Axis 1 or Axis 2. The label is what makes the axis self-announcing.

Required form — the label and the pipe sequence form a single structural unit:

**Surface status:** `success: N findings | error: N findings | edge: N findings`

**Two forms are explicitly prohibited for Axis 3:**

1. **Table-register absorption — not compliant.** Do not embed surface counts as rows in a shared table alongside severity or mechanism counts. This is the table-register absorption failure mode: the table form places Axis 3 in the same format register as Axis 2 (also a table), collapsing the surface and mechanism dimensions into a single visual register. Three structural properties are lost: (a) format-register distinction between the mechanism axis and the surface axis, (b) visual weight separation that enables scan-time axis identification, (c) the ability to identify the surface axis in isolation — a reader must read axis labels to distinguish surface distribution from mechanism distribution, defeating the purpose of structural separability. Example of prohibited table-register form: `| Surface | success: N, error: N, edge: N |` as a row in a Dimension table alongside `| Severity | ... |` and `| Mechanism | ... |` rows.

2. **Prose-register absorption — not compliant.** Do not embed surface counts as a prose sentence, continuation, or parenthetical. This is the prose-register absorption failure mode: a prose line in the Axis 3 slot occupies the same format register as Axis 1 (also a compact prose line). The surface dimension is absorbed into the severity narrative. A reader scanning the Summary encounters two compact-line items and must read both to distinguish "findings by severity" from "findings by surface" — structural separability is lost. An axis label embedded as a bold field name within a prose sentence (e.g., "**Surface distribution:** success (N), error (N), edge (N)") does not satisfy C-38: the label is part of the prose register, not a structural designator immediately preceding a pipe-delimited sequence. Example of prohibited prose-register form: "**Surface distribution:** Also note how findings distributed across surfaces: success (N), error (N), edge (N)."

**Verdict:** `Contract violated` or `Contract satisfied`

**Recommendations (all findings, including cosmetic):**
`F-NN recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`
