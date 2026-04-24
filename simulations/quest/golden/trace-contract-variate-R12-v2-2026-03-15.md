# trace-contract Variate — Round 12 (Rubric v12)
**Date:** 2026-03-15
**Rubric:** v12 (C-08–C-36; denominator /29; total max 119)
**Baseline:** R12 V-05 = 28/28 on v11 (C-34 and C-35 PASS; v12 adds C-36 as new scored criterion)
**Target criterion:** C-36 (Surface-status compact line format)

---

## Round 12 Variation Map

| Variation | Axis | C-36 | Notes |
|-----------|------|------|-------|
| V-01 | Output format — surface-status rendered as table matching Axis 2 register | PARTIAL | Single-axis: information present (C-34 PASS) but table form blurs boundary with mechanism distribution table (C-14); compact line format absent |
| V-02 | Phrasing register — surface-status embedded in prose sentence, no format-register distinction | PARTIAL | Single-axis: surface counts present but comma-separated in prose; pipe-delimited compact line absent; no axis-level format register instruction |
| V-03 | Lifecycle emphasis — Step 6 restructured with explicit format-register labels and compact-line mandate | PASS | Single-axis: three-register layout named explicitly; table form prohibited for Axis 3 with structural reason; pipe-delimited format prescribed |
| V-04 | Output format + phrasing register (combination) — V-03 format-register labels + prohibition rationale naming register-blurring consequence | PASS | Combination: explicit compact-line mandate + prohibition text explaining why table form is disqualifying (conflates Axis 3 with Axis 2 in same register, degrades scan-time separability) |
| V-05 | Full platinum (C-08 through C-36) | PASS | All axes: V-04 approach for C-36 + complete R12 V-05 baseline for all C-08 through C-35; expected 29/29 |

---

## V-01 — Table Form for Axis 3

**Axis:** Output format — surface-status rendered as a three-row labeled table, matching the format register of the Axis 2 mechanism distribution table (C-14)

**Hypothesis:** C-36 PARTIAL because the surface-status dimension appears as a table (`| Surface | Findings |` with three rows) rather than a compact pipe-delimited line. The information axis is present and C-34 is satisfied. But C-36 requires the surface-status to occupy a distinct format register from the Axis 2 mechanism table — a table in the Axis 3 slot collapses two separate reporting dimensions into the same visual form, making them indistinguishable on document scan. C-34 PASS (third axis present). C-36 PARTIAL (format register not distinguished from C-14). All other criteria from R12 V-05 intact.

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

**Axis 1 — Severity distribution**
`breaking: N | degraded: N | cosmetic: N | total: N`

**Axis 2 — Mechanism distribution**

| Mechanism | Finding Count |
|-----------|--------------|
| [mechanism-name] | N |

(Include only mechanisms that appear in at least one finding. Omit mechanisms with zero findings.)

**Axis 3 — Surface finding distribution**

| Surface | Findings |
|---------|----------|
| success | N |
| error | N |
| edge | N |

Verdict: `Contract violated` or `Contract satisfied`

Recommendations — list every finding at every severity, including cosmetic. A finding without a recommendation is incomplete:
`F-NN recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Prose Embedding for Axis 3

**Axis:** Phrasing register — surface-status embedded as a prose sentence following the severity distribution line; no structural axis heading, no pipe-delimited format, no format-register distinction

**Hypothesis:** C-36 PARTIAL because the surface counts appear as a comma-separated sentence rather than a compact pipe-delimited line in a distinct format register. The information is present (C-34 PASS) but the phrasing register does not signal a structurally independent third reporting dimension — it reads as a continuation of the Axis 1 severity commentary rather than a separate axis. No instruction text tells Automate to use the pipe-delimited format; no prohibition on prose form exists. C-34 PASS (information present). C-36 PARTIAL (compact line format absent; format register not distinguished from narrative prose). All other criteria from R12 V-05 intact.

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

Write a `## Summary` section. Three reporting dimensions are required.

**Severity distribution:**
`breaking: N | degraded: N | cosmetic: N | total: N`

**Mechanism distribution:**

| Mechanism | Finding Count |
|-----------|--------------|
| [mechanism-name] | N |

(Include only mechanisms that appear in at least one finding. Omit mechanisms with zero findings.)

**Surface distribution:** Also report how findings distributed across contract surfaces: success (N), error (N), edge (N).

Verdict: `Contract violated` or `Contract satisfied`

Recommendations — list every finding at every severity, including cosmetic. A finding without a recommendation is incomplete:
`F-NN recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Explicit Format-Register Labels

**Axis:** Lifecycle emphasis — Step 6 is restructured to explicitly name the format register for each axis, mandate the compact line format for Axis 3, and prohibit table form

**Hypothesis:** C-36 PASS through the format-register label in the Axis 3 heading ("compact line — table form prohibited") and the prescription of the exact `success: N findings | error: N findings | edge: N findings` pattern. The heading makes the format register constraint visible on document scan without requiring Automate to read supporting prose. The prohibition text names the exact failure mode (table form) and references the register-blurring consequence (Axis 3 in table form is indistinguishable from Axis 2 on scan). C-34 PASS (surface counts required and prescribed). All other criteria from R12 V-05 intact. Expected: 29/29.

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

Write a `## Summary` section. Three reporting axes are required, each occupying a distinct format register. The three registers are fixed: Axis 1 is a compact line, Axis 2 is a table, Axis 3 is a compact line. Do not change the format of any axis.

**Axis 1 — Severity distribution (compact line)**
`breaking: N | degraded: N | cosmetic: N | total: N`

**Axis 2 — Mechanism distribution (table)**

| Mechanism | Finding Count |
|-----------|--------------|
| [mechanism-name] | N |

(Include only mechanisms that appear in at least one finding. Omit mechanisms with zero findings.)

**Axis 3 — Surface finding distribution (compact line — table form prohibited)**
`success: N findings | error: N findings | edge: N findings`

Use the pipe-delimited compact line exactly as shown. Do not render this axis as a table. A table in the Axis 3 position is indistinguishable from Axis 2 on document scan and is not compliant.

Verdict: `Contract violated` or `Contract satisfied`

Recommendations — list every finding at every severity, including cosmetic. A finding without a recommendation is incomplete:
`F-NN recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Format-Register Labels + Register-Blurring Prohibition Rationale (Combination)

**Axis:** Output format + phrasing register — combines V-03's explicit format-register axis labels with prohibition text that names the specific register-blurring consequence of table form in the Axis 3 slot

**Hypothesis:** C-36 PASS at higher confidence than V-03. V-03's compact-line mandate and table prohibition are structurally correct but do not explain WHY the constraint exists. V-04 adds the rationale: a table in the Axis 3 position collapses two independent reporting dimensions (surface distribution and mechanism distribution) into the same format register, making them indistinguishable on scan without reopening diff blocks. The rationale is not decorative — it enables Automate to diagnose its own compliance failure: "My Axis 3 looks like Axis 2 on scan, which means I violated the register separation constraint." C-34 PASS. C-36 PASS with rationale preventing the V-01 failure mode (author substitutes table, believing format is cosmetic). All other criteria from R12 V-05 intact. Expected: 29/29.

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

Write a `## Summary` section. The Summary has exactly three reporting axes, each in a fixed format register. The format registers are not interchangeable: Axis 1 and Axis 3 are compact lines; Axis 2 is a table. Rendering Axis 3 as a table collapses it into the same format register as Axis 2, making the surface distribution and mechanism distribution dimensions visually indistinguishable on scan without reopening diff blocks. This is not a cosmetic preference — it is a structural separability requirement. Use the formats exactly as prescribed.

**Axis 1 — Severity distribution (compact line)**
`breaking: N | degraded: N | cosmetic: N | total: N`

**Axis 2 — Mechanism distribution (table)**

| Mechanism | Finding Count |
|-----------|--------------|
| [mechanism-name] | N |

(Include only mechanisms that appear in at least one finding. Omit mechanisms with zero findings.)

**Axis 3 — Surface finding distribution (compact line — table form is not compliant)**
`success: N findings | error: N findings | edge: N findings`

Use this exact pipe-delimited compact line. DO NOT render Axis 3 as a table. A table in the Axis 3 slot introduces visual weight that blurs the boundary with the Axis 2 mechanism table; a reader scanning the Summary can no longer distinguish "where did findings concentrate" from "how did findings distribute by mechanism" without reading the axis labels. The compact line is the format register that keeps the two dimensions separable.

Verdict: `Contract violated` or `Contract satisfied`

Recommendations — list every finding at every severity, including cosmetic. A finding without a recommendation is incomplete:
`F-NN recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — Full Platinum (C-08 through C-36)

**Axis:** All criteria — V-04 format-register labels + register-blurring prohibition rationale for C-36 + complete R12 V-05 baseline for all C-08 through C-35

**Hypothesis:** C-36 PASS through V-04's explicit format-register taxonomy in Step 6: three axes named, three registers declared, table form prohibited for Axis 3 with the register-blurring rationale that explains WHY the constraint exists. C-34 PASS (surface counts required, exact format prescribed, structural axis heading). C-35 PASS through the dedicated `**Incomplete Taxonomy Fallback — REQUIRED**` block inside Step 2B — physically inside the taxonomy block, labeled, and covers both the action rule and the prohibition. Every other criterion satisfied by the full R12 V-05 baseline: role separation and reading boundary (C-21, C-30, C-31, C-32, C-33), gate permanence across all committed acts (C-27), taxonomy declared pre-gate and sealed (C-23, C-25), hypothesis prohibitions covering direct, mechanism-dress, and black-box forms with concrete examples (C-20, C-26, C-29), positive hypothesis formulation (C-28), clean-surface shortcut prohibition (C-24), spec-anchoring imperative (C-19), independent surface block architecture (C-18), element-level diff granularity (C-16), full-coverage recommendations (C-17), pre-authoring rules block at document head with role-boundary heading (C-22, C-33). Expected: 29/29 skill criteria.

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

Write a `## Summary` section. The Summary has exactly three reporting axes, each occupying a fixed and distinct format register. The three registers are: Axis 1 compact line, Axis 2 table, Axis 3 compact line. The register assignment is not interchangeable — it is the structural mechanism that makes the three dimensions separable on document scan. Rendering Axis 3 as a table collapses it into the same visual form as Axis 2; a reader can no longer distinguish "where did findings concentrate by surface" from "how did findings distribute by mechanism" without reading axis labels in detail. This is a structural separability requirement, not cosmetic formatting. Use the prescribed formats exactly.

**Axis 1 — Severity distribution (compact line)**
`breaking: N | degraded: N | cosmetic: N | total: N`

**Axis 2 — Mechanism distribution (table)**

| Mechanism | Finding Count |
|-----------|--------------|
| [mechanism-name] | N |

(Include only mechanisms that appear in at least one finding. Omit mechanisms with zero findings.)

**Axis 3 — Surface finding distribution (compact line — table form not compliant)**
`success: N findings | error: N findings | edge: N findings`

Use this exact pipe-delimited compact line. DO NOT render Axis 3 as a table. A table in the Axis 3 slot: (1) uses the same format register as Axis 2, (2) introduces visual weight that blurs the boundary between the mechanism dimension and the surface dimension, (3) degrades scan-time separability — the reader must read axis labels rather than register differences to distinguish the two. The compact line is the only compliant form for Axis 3.

Verdict: `Contract violated` or `Contract satisfied`

Recommendations — list every finding at every severity, including cosmetic. A finding without a recommendation is incomplete:
`F-NN recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`
