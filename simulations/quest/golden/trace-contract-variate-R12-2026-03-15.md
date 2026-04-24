# trace-contract Variate — Round 12
**Date:** 2026-03-15
**Rubric:** v11 (C-08–C-35; denominator /28; total max 118)
**Baseline:** R10 V-05 = 28/28 skill criteria (C-34 and C-35 already present as R10 excellence signals; v11 formalizes them as scored criteria)
**Target criteria:** C-34 (Summary surface-status line), C-35 (Taxonomy fallback instruction)

---

## Round 12 Variation Map

| Variation | Axis | C-34 | C-35 | Notes |
|-----------|------|------|------|-------|
| V-01 | Output format — surface counts merged into combined summary table | PARTIAL | PASS | Single-axis: all three reporting dimensions present but collapsed into table rows; C-34 partial because prescribed pipe-separated line format absent and third-axis framing absent |
| V-02 | Lifecycle emphasis — fallback instruction relocated from taxonomy block to Step 5 hypothesis rules | PASS | PARTIAL | Single-axis: fallback instruction exists but outside the taxonomy block; C-35 criterion requires "The taxonomy block includes" the fallback |
| V-03 | Phrasing register — both criteria in explicit imperative register with named blocks | PASS | PASS | Single-axis: surface-status labeled "REQUIRED — Axis 3"; fallback as headed "Incomplete Taxonomy Fallback Rule" block; strongest single-axis treatment |
| V-04 | Role sequence + output format — three-axis explicit headers + taxonomy fallback as named taxonomy rule | PASS | PASS | Combination: V-01 axis-label approach + V-02 taxonomy-block placement; dual-mechanism satisfaction |
| V-05 | Full platinum (C-08 through C-35) | PASS | PASS | All axes: V-03 imperative register + explicit axis labels + named fallback rule in taxonomy block + complete R10 V-05 baseline; expected 28/28 |

---

## V-01 — Combined Summary Reporting Table

**Axis:** Output format — all three Summary reporting dimensions collapsed into a single unified table rather than separate numbered items

**Hypothesis:** C-34 PARTIAL because the surface-status counts appear but not as a distinct third-axis line in the prescribed `success: N findings | error: N findings | edge: N findings` format — they appear as a table row labeled "Surface" with comma-separated values. C-35 PASS unchanged from R10 V-05 (fallback present in taxonomy block as trailing prose). Scoring this variation identifies whether format matters for C-34 compliance or whether the presence of the dimension is sufficient.

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

## Pre-Authoring Rules — Contract Author reads; Automate stops here

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

Add mechanisms only if this operation's spec makes additional failure modes plausible — state the spec basis for each addition. Remove only with written justification. This list is sealed at the gate. After the gate, Phase 3 authors must select from this exact list. If no listed mechanism fits a finding's causal chain, use the closest mechanism and explain the gap in the explanation field — do not introduce an unlisted mechanism label.

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

Write a `## Summary` section containing a single unified reporting table followed by verdict and recommendations:

**Reporting table (all three dimensions required):**

| Dimension | Distribution |
|-----------|-------------|
| Severity | breaking: N, degraded: N, cosmetic: N, total: N |
| Mechanism | [mechanism-name]: N; [mechanism-name]: N (only mechanisms with ≥1 finding) |
| Surface | success: N, error: N, edge: N |

**Verdict:** `Contract violated` or `Contract satisfied`

**Recommendations (all findings, including cosmetic):**
`F-NN recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Fallback Instruction Relocated to Step 5

**Axis:** Lifecycle emphasis — fallback instruction for incomplete taxonomy moved from the taxonomy block (Step 2B) to the hypothesis rules in Step 5

**Hypothesis:** C-35 PARTIAL because the pass condition states "The taxonomy block includes an explicit fallback instruction" — placing the fallback in Step 5 means the taxonomy block no longer contains it. Phase 3 authors encountering the sealed taxonomy first (before reading hypothesis rules) face the dilemma the criterion is designed to prevent. C-34 PASS unchanged from R10 V-05 (surface-status line present as item 3 in Step 6).

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

## Pre-Authoring Rules — Contract Author reads; Automate stops here

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

**Incomplete taxonomy fallback:** If no listed mechanism fits a finding's causal chain, use the closest listed mechanism and explain the gap in the explanation field — do not introduce an unlisted mechanism label. The sealed vocabulary in Phase 1 permits no extensions in Phase 3.

Recommendation is required for every finding at every severity — including cosmetic.

---

**Step 6 — Summary**

Write a `## Summary` section:
1. Severity counts: `breaking: N | degraded: N | cosmetic: N | total: N`
2. Mechanism distribution table:

| Mechanism | Finding Count |
|-----------|--------------|
| [mechanism-name] | N |

(Include only mechanisms that appear in at least one finding. Omit mechanisms with zero findings.)

3. Surface status: one line per surface (`success: N findings | error: N findings | edge: N findings`)
4. Verdict: `Contract violated` or `Contract satisfied`
5. Recommendation for **every finding** — list all, including cosmetic. Format: `F-NN recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Imperative Register: Both Criteria as Named Mandatory Blocks

**Axis:** Phrasing register — both C-34 and C-35 reformulated in explicit imperative register: surface-status line gets a named mandatory block heading; taxonomy fallback gets a named rule block with capital-letter prohibition

**Hypothesis:** C-34 PASS (stronger than baseline) because the surface-status requirement is surfaced as a labeled mandatory section heading inside Step 6 — not merely an item in a numbered list — eliminating the possibility of treating it as optional. C-35 PASS (stronger than baseline) because the fallback is its own named block (`**Incomplete Taxonomy Fallback — REQUIRED**`) with an explicit prohibition at imperative register: "DO NOT introduce an unlisted mechanism label." Both criteria pass robustly under imperative enforcement; the variation tests whether the strengthen registers above minimum compliance.

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

## Pre-Authoring Rules — Contract Author reads; Automate stops here

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

**Incomplete Taxonomy Fallback — REQUIRED**
When no listed mechanism fits a finding's causal chain: (1) select the closest listed mechanism, (2) explain the gap between that mechanism and the true causal mechanism in the explanation field, (3) DO NOT introduce an unlisted mechanism label under any circumstances. The sealed vocabulary permits no extensions. A finding that uses an unlisted label violates C-13 — use the closest compliant label and document the gap.

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

Write a `## Summary` section:
1. Severity counts: `breaking: N | degraded: N | cosmetic: N | total: N`
2. Mechanism distribution table:

| Mechanism | Finding Count |
|-----------|--------------|
| [mechanism-name] | N |

(Include only mechanisms that appear in at least one finding. Omit mechanisms with zero findings.)

**REQUIRED — Third Reporting Axis: Surface Finding Distribution**
Write one line per surface — this line is mandatory and may not be omitted:
`success: N findings | error: N findings | edge: N findings`
This third axis reveals cross-surface concentration patterns that severity counts and mechanism distribution cannot. A Summary without this line is incomplete.

4. Verdict: `Contract violated` or `Contract satisfied`
5. Recommendation for **every finding** — list all, including cosmetic. Format: `F-NN recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Three-Axis Summary Labels + Named Taxonomy Rule (Combination)

**Axis:** Role sequence + output format — combines V-03's imperative register for C-34 (REQUIRED axis header in Step 6) with V-03's named taxonomy rule block for C-35 (Incomplete Taxonomy Fallback block in Step 2B), while the base structure from V-01 and V-02 is replaced by the stronger formulations

**Hypothesis:** C-34 PASS through the REQUIRED heading in Step 6 — surface-status cannot be read as optional when it carries an imperative block label. C-35 PASS through the named fallback block in Step 2B — the fallback is physically inside the taxonomy block, satisfying "The taxonomy block includes an explicit fallback instruction," and the named block format makes it impossible to miss. Both mechanisms are independent and non-overlapping; the combination tests whether dual strengthening produces additive reliability or whether one mechanism is redundant.

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

## Pre-Authoring Rules — Contract Author reads; Automate stops here

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

**Incomplete Taxonomy Fallback — REQUIRED**
If no listed mechanism fits a finding's causal chain: (1) select the closest listed mechanism — do not leave the field blank, (2) explain the gap between the closest mechanism and the true causal chain in the explanation field, (3) DO NOT introduce an unlisted mechanism label. Forced bad-fit with documented gap is always preferable to introducing a new label. The sealed vocabulary permits no Phase 3 extensions.

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

Write a `## Summary` section:

**Axis 1 — Severity distribution** (required)
`breaking: N | degraded: N | cosmetic: N | total: N`

**Axis 2 — Mechanism distribution** (required)

| Mechanism | Finding Count |
|-----------|--------------|
| [mechanism-name] | N |

(Include only mechanisms that appear in at least one finding. Omit mechanisms with zero findings.)

**Axis 3 — Surface finding distribution** (required — reveals cross-surface imbalance)
`success: N findings | error: N findings | edge: N findings`

Verdict: `Contract violated` or `Contract satisfied`

Recommendations — every finding, every severity, including cosmetic:
`F-NN recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — Full Platinum (C-08 through C-35)

**Axis:** All criteria — V-03 imperative register for both new criteria + V-04 dual-mechanism satisfaction + complete R10 V-05 baseline for all C-08 through C-33

**Hypothesis:** C-34 PASS through the dedicated Axis 3 block heading in Step 6 — structurally distinguishable from the severity and mechanism reporting dimensions, format matches the prescribed pipe-separated line, and the heading is imperative ("required"). C-35 PASS through the dedicated `**Incomplete Taxonomy Fallback — REQUIRED**` block inside Step 2B — the fallback is physically inside the taxonomy block, structurally labeled, and includes both the action rule (use closest mechanism + explain gap) and the prohibition (DO NOT introduce unlisted label). Every other criterion satisfied by the full R10 V-05 baseline architecture: role separation (C-21, C-31, C-32, C-33), gate permanence (C-27), hypothesis prohibitions covering direct, mechanism-dress, and black-box forms (C-20, C-26, C-29), positive hypothesis formulation (C-28), clean-surface shortcut prohibition (C-24), reading boundary (C-30), pre-gate taxonomy placement (C-23), gate-sealed vocabulary (C-25). Expected: 28/28 skill criteria.

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

## Pre-Authoring Rules — Contract Author reads; Automate stops here

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

**Incomplete Taxonomy Fallback — REQUIRED**
This rule addresses the case where no listed mechanism fits a finding's causal chain. In that case: (1) select the closest listed mechanism from the sealed vocabulary, (2) write the explanation field normally — and within it, explicitly name the gap: "Closest match is [mechanism]; true mechanism appears to be [brief description] — no listed mechanism captures this precisely," (3) DO NOT introduce an unlisted mechanism label. The sealed vocabulary is irrevocable. Forced closest-fit with documented gap is the only compliant path.

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

Write a `## Summary` section. Three reporting axes are required — omitting any axis leaves the Summary incomplete.

**Axis 1 — Severity distribution** (required by C-08)
`breaking: N | degraded: N | cosmetic: N | total: N`

**Axis 2 — Mechanism distribution** (required by C-14)

| Mechanism | Finding Count |
|-----------|--------------|
| [mechanism-name] | N |

(Include only mechanisms that appear in at least one finding. Omit mechanisms with zero findings.)

**Axis 3 — Surface finding distribution** (required — reveals where findings concentrate across contract surfaces; severity and mechanism axes cannot show this)
`success: N findings | error: N findings | edge: N findings`

Verdict: `Contract violated` or `Contract satisfied`

Recommendations — list every finding at every severity, including cosmetic. A finding without a recommendation is incomplete:
`F-NN recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`
