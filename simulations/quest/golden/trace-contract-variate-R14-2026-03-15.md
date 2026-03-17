# trace-contract Variate — Round 14
**Date:** 2026-03-15
**Rubric:** v13 (C-08–C-39; denominator /32; total max 128)
**Baseline:** R13 V-05 = 30/30 on v12 rubric (C-38 and C-39 absent from v12; v13 adds them as scored criteria)
**Target criteria:** C-38 (Axis identity label in surface-status heading), C-39 (REQUIRED designation in mandatory protocol block headings)

---

## Round 14 Variation Map

| Variation | Axis | C-38 | C-39 | Notes |
|-----------|------|------|------|-------|
| V-01 | Output format — surface-status heading carries REQUIRED but no axis identity label | PARTIAL | PASS | Single-axis: "**Surface Status — REQUIRED**" without "(Axis 3)"; three-axis architecture not visible on scan; fallback heading still carries REQUIRED so C-39 passes |
| V-02 | Phrasing register — fallback block heading carries no REQUIRED designation | PASS | PARTIAL | Single-axis: "**Incomplete Taxonomy Fallback**" heading strips REQUIRED; surface-status heading "**Surface Status — REQUIRED (Axis 3)**" passes C-38 but C-39 requires REQUIRED in every mandatory block heading — one block without it = partial |
| V-03 | Phrasing register — axis identity uses English ordinal ("Third Axis") instead of numeric notation | PASS | PASS | Single-axis: "**Surface Status — REQUIRED (Third Axis)**" — tests whether axis identity requires numeric form; REQUIRED present in both mandatory block headings |
| V-04 | Output format + phrasing register combination — both mandatory block headings stripped of REQUIRED and axis label | PARTIAL | PARTIAL | Combination: surface-status heading "**Surface Status**" (no REQUIRED, no axis label); fallback heading "**Incomplete Taxonomy Fallback**" (no REQUIRED); both new criteria fail simultaneously |
| V-05 | Full platinum (C-08 through C-39) | PASS | PASS | All axes: R13 V-05 baseline + strongest C-38 form (axis identity + cross-reference to Axes 1 and 2 in heading prose) + strongest C-39 form (REQUIRED in both mandatory block headings with mandate rationale); expected 32/32 |

---

## V-01 — REQUIRED Without Axis Identity (C-38 Partial)

**Axis:** Output format — the surface-status section heading in Step 6 carries "REQUIRED" but omits the axis identity label, so the three-axis reporting architecture is not visible on document scan

**Hypothesis:** C-38 PARTIAL because the heading reads "**Surface Status — REQUIRED**" — REQUIRED announces the mandate (satisfying C-39's contribution from this block) but the heading contains no signal that this is a third reporting axis alongside severity and mechanism. A scanner reading headings knows a mandatory surface count exists but cannot confirm the three-axis architecture without reading the body. The axis identity label "(Axis 3)" is what C-38 requires; its absence makes the third axis structurally unnamed at scan resolution. C-39 PASS because both mandatory block headings carry REQUIRED: the surface-status heading carries "REQUIRED" and the fallback block heading carries "REQUIRED".

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
Read this before you commit to a mechanism selection. If no listed mechanism fits a finding's causal chain: (1) select the closest listed mechanism — do not leave the mechanism field blank or use an invented label, (2) in the explanation field, name the gap: state which aspect of the causal chain the closest mechanism does not capture and why the true mechanism is absent from the sealed list, (3) DO NOT introduce an unlisted mechanism label under any circumstances — including in parentheses, as a qualifier, or as an alternate. Forced best-fit with a documented gap is the only compliant form when no exact match exists. This fallback applies only when the sealed list genuinely contains no fitting mechanism — if a listed mechanism fits approximately, use it without invoking the fallback.

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

(Include only mechanisms with >=1 finding.)

**Surface Status — REQUIRED**
Write the surface finding counts as a standalone pipe-separated line — not as a row in a table, not as a comma-separated inline entry, not embedded in the Axis 2 table:
`success: N findings | error: N findings | edge: N findings`
This line is structurally independent of Axes 1 and 2 — it is a distinct reporting signal, not a dimension inside either of the first two. Embedding it in the Axis 2 table collapses the surface axis and makes it unscannable. The standalone pipe-separated format is the only valid form for this item.

**Verdict:** `Contract violated` or `Contract satisfied`

**Recommendations — every finding, every severity, including cosmetic:**
`F-NN recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Fallback Block Heading Strips REQUIRED (C-39 Partial)

**Axis:** Phrasing register — the "Incomplete Taxonomy Fallback" block heading in Step 2B carries no REQUIRED designation; the surface-status heading retains "REQUIRED (Axis 3)"

**Hypothesis:** C-39 PARTIAL because C-39 requires every mandatory protocol block heading to carry "REQUIRED" — and the fallback block heading "**Incomplete Taxonomy Fallback**" violates this. The surface-status heading "**Surface Status — REQUIRED (Axis 3)**" satisfies C-39's mandate for that block, but C-39 is not satisfied by one of two required blocks alone. The fallback block is a mandatory protocol constraint; authors scanning headings encounter it without any "REQUIRED" signal and must read the prose to discover the obligation. C-38 PASS because "**Surface Status — REQUIRED (Axis 3)**" carries the axis identity label. C-35 PASS and C-37 PASS because the fallback instruction is co-located in Step 2B and its prose is complete — the deficiency is in the heading only.

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

**Incomplete Taxonomy Fallback**
Read this before you commit to a mechanism selection. If no listed mechanism fits a finding's causal chain: (1) select the closest listed mechanism — do not leave the mechanism field blank or use an invented label, (2) in the explanation field, name the gap: state which aspect of the causal chain the closest mechanism does not capture and why the true mechanism is absent from the sealed list, (3) DO NOT introduce an unlisted mechanism label under any circumstances — including in parentheses, as a qualifier, or as an alternate. Forced best-fit with a documented gap is the only compliant form when no exact match exists. This fallback applies only when the sealed list genuinely contains no fitting mechanism — if a listed mechanism fits approximately, use it without invoking the fallback.

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

(Include only mechanisms with >=1 finding.)

**Surface Status — REQUIRED (Axis 3)**
Write the surface finding counts as a standalone pipe-separated line — not as a row in a table, not as a comma-separated inline entry, not embedded in the Axis 2 table:
`success: N findings | error: N findings | edge: N findings`
This line is structurally independent of Axes 1 and 2 — it is a distinct reporting signal, not a dimension inside either of the first two. Embedding it in the Axis 2 table collapses the third axis and makes it unscannable. The standalone pipe-separated format is the only valid form for this item.

**Verdict:** `Contract violated` or `Contract satisfied`

**Recommendations — every finding, every severity, including cosmetic:**
`F-NN recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — English Ordinal Axis Label (C-38 Pass, C-39 Pass, Phrasing Variant)

**Axis:** Phrasing register — axis identity in the surface-status heading uses English ordinal notation ("Third Axis") instead of numeric abbreviation ("Axis 3"); tests whether the axis identity criterion requires a specific numeric form or whether any unambiguous axis-position label satisfies C-38

**Hypothesis:** C-38 PASS because "**Surface Status — REQUIRED (Third Axis)**" names the axis position — a scanner reading headings knows this is a distinct third reporting axis. The criterion requires the heading to "announce axis position"; it does not require the label to use a specific numeric form. English ordinal is unambiguous and equivalent to the numeric form for scanners. C-39 PASS because both mandatory block headings carry REQUIRED: "**Surface Status — REQUIRED (Third Axis)**" and "**Incomplete Taxonomy Fallback — REQUIRED**". This variation tests whether the phrasing register of the axis label affects compliance.

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
Read this before you commit to a mechanism selection. If no listed mechanism fits a finding's causal chain: (1) select the closest listed mechanism — do not leave the mechanism field blank or use an invented label, (2) in the explanation field, name the gap: state which aspect of the causal chain the closest mechanism does not capture and why the true mechanism is absent from the sealed list, (3) DO NOT introduce an unlisted mechanism label under any circumstances — including in parentheses, as a qualifier, or as an alternate. Forced best-fit with a documented gap is the only compliant form when no exact match exists. This fallback applies only when the sealed list genuinely contains no fitting mechanism — if a listed mechanism fits approximately, use it without invoking the fallback.

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

(Include only mechanisms with >=1 finding.)

**Surface Status — REQUIRED (Third Axis)**
Write the surface finding counts as a standalone pipe-separated line — not as a row in a table, not as a comma-separated inline entry, not embedded in the Axis 2 table:
`success: N findings | error: N findings | edge: N findings`
This line is the third reporting axis, alongside Axis 1 (severity) and Axis 2 (mechanism). It is structurally independent of both — a distinct reporting signal, not a dimension inside either of the first two. Embedding it in the Axis 2 table collapses the third axis and makes it unscannable. The standalone pipe-separated format is the only valid form for this item.

**Verdict:** `Contract violated` or `Contract satisfied`

**Recommendations — every finding, every severity, including cosmetic:**
`F-NN recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Both Mandatory Block Headings Stripped (C-38 Partial, C-39 Partial)

**Axis:** Output format + phrasing register combination — surface-status heading is "**Surface Status**" (no REQUIRED, no axis label); fallback block heading is "**Incomplete Taxonomy Fallback**" (no REQUIRED); tests simultaneous failure of both new criteria

**Hypothesis:** C-38 PARTIAL because "**Surface Status**" carries no axis identity label — a scanner reading headings cannot confirm the three-axis architecture. C-36 PASS because the content beneath the heading is a standalone pipe-separated line, satisfying the structural independence requirement; C-38 requires the heading itself to announce axis position, which this heading does not. C-39 PARTIAL because neither mandatory block heading carries "REQUIRED" — both the surface-status section and the fallback block omit the mandate signal at heading level, requiring authors to read prose to discover the obligations. C-35 PASS and C-37 PASS because the fallback instruction remains co-located in Step 2B in full prose; C-38 and C-39 deficiencies are heading-level only, not content-level.

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

**Incomplete Taxonomy Fallback**
Read this before you commit to a mechanism selection. If no listed mechanism fits a finding's causal chain: (1) select the closest listed mechanism — do not leave the mechanism field blank or use an invented label, (2) in the explanation field, name the gap: state which aspect of the causal chain the closest mechanism does not capture and why the true mechanism is absent from the sealed list, (3) DO NOT introduce an unlisted mechanism label under any circumstances — including in parentheses, as a qualifier, or as an alternate. Forced best-fit with a documented gap is the only compliant form when no exact match exists. This fallback applies only when the sealed list genuinely contains no fitting mechanism — if a listed mechanism fits approximately, use it without invoking the fallback.

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

(Include only mechanisms with >=1 finding.)

**Surface Status**
Write the surface finding counts as a standalone pipe-separated line — not as a row in a table, not as a comma-separated inline entry, not embedded in the Axis 2 table:
`success: N findings | error: N findings | edge: N findings`
This line is structurally independent of the severity and mechanism tables above. Embedding it in the Axis 2 table collapses the surface dimension and makes it unscannable. The standalone pipe-separated format is the only valid form for this item.

**Verdict:** `Contract violated` or `Contract satisfied`

**Recommendations — every finding, every severity, including cosmetic:**
`F-NN recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — Full Platinum (C-08 through C-39)

**Axis:** All axes — R13 V-05 baseline extended with strongest passing form for C-38 (axis identity label with explicit cross-reference to the other two axes) and C-39 (REQUIRED in both mandatory block headings with mandate rationale embedded in heading prose); expected 32/32 on v13 rubric

**Hypothesis:** C-38 PASS through "**Surface Status — REQUIRED (Axis 3)**" — axis identity present; a scanner reading headings knows three axes exist (severity Axis 1, mechanism Axis 2, surface Axis 3) without reading Summary body. C-39 PASS through "REQUIRED" present in both mandatory protocol block headings: "**Surface Status — REQUIRED (Axis 3)**" and "**Incomplete Taxonomy Fallback — REQUIRED**" — both mandate obligations visible at scan resolution before any prose is read. The V-05 enhancement over R13 V-05: the surface-status heading prose reinforces the axis architecture by naming all three axes; the fallback block heading prose opens with "Read this before you commit" — the mandate rationale is visible from the heading position, not buried.

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
Read this before you commit to a mechanism selection. When no listed mechanism fits a finding's causal chain: (1) select the closest listed mechanism — do not leave the mechanism field blank or use an invented label, (2) in the explanation field, name the gap precisely: state which aspect of the causal chain the closest mechanism does not capture and why the true causal mechanism is absent from the sealed list, (3) DO NOT introduce an unlisted mechanism label under any circumstances — including in parentheses, as a qualifier, or as a secondary alternate. Forced best-fit with a fully documented gap is the only compliant form when no exact match exists. This fallback applies only when the sealed list genuinely contains no fitting mechanism — if a listed mechanism fits approximately, use it without invoking the fallback.

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

Write a `## Summary` section. The Summary reports three independent axes — each is a distinct structural section, not a row in a shared table.

**Axis 1 — Severity distribution** (required)
`breaking: N | degraded: N | cosmetic: N | total: N`

**Axis 2 — Mechanism distribution** (required)

| Mechanism | Finding Count |
|-----------|--------------|
| [mechanism-name] | N |

(Include only mechanisms with >=1 finding.)

**Surface Status — REQUIRED (Axis 3)**
Write the surface finding counts as a standalone pipe-separated line. This is the third reporting axis — alongside Axis 1 (severity distribution) and Axis 2 (mechanism distribution). It must not be embedded as a row in the Axis 2 table, collapsed into a prose sentence, or combined with either of the first two axes in any shared structure. The standalone pipe-separated format is the only valid form:
`success: N findings | error: N findings | edge: N findings`
A scanner reading headings must be able to confirm all three axes exist without reading the Summary body. This heading — "Surface Status — REQUIRED (Axis 3)" — is that confirmation for the third axis.

**Verdict:** `Contract violated` or `Contract satisfied`

**Recommendations — every finding, every severity, including cosmetic:**
`F-NN recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`
