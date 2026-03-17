# trace-contract Variate — Round 3 (Rubric v3)

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v3 (C-01–C-15; essential C-01–C-05 = 60 pts; recommended C-06–C-08 = 30 pts; aspirational C-09–C-15 = 10 pts; golden threshold >= 80)
**Round:** R3 — 3 new single-axis + 2 priority combinations targeting C-13, C-14, C-15 (new aspirational criteria)

---

## Round 3 Variation Map

| Variation | Axis | Primary Targets | Hypothesis |
|-----------|------|-----------------|------------|
| V-01 | output-format (finding block extended with mandatory `connector-impact:` slot on every finding) | C-14 | C-06 is satisfied by at-least-one integration callout in any finding; C-14 requires the integration lens to be structurally mandatory per finding — when the template field is absent from a finding block, the omission is visually self-announcing; prose-adjacent coverage (satisfied C-06) becomes structurally enforced coverage (C-14) |
| V-02 | output-format (breaking-finding template has `recommended-action:` as a required fifth labeled slot) | C-15 | C-09 is satisfied when amendment content appears anywhere in a breaking finding; C-15 requires a dedicated labeled slot — a breaking finding block that omits `recommended-action:` is visibly incomplete at write time, not at review time; moving from prose inclusion (C-09) to template enforcement (C-15) requires no new reasoning but a structural template change |
| V-03 | lifecycle-emphasis (the phase-gate uses the exact token `[EXPECTED SEALED]` defined explicitly as a machine-parseable boundary marker) | C-13 | C-12 is satisfied by a prose acknowledgment that expected was sealed before execution; C-13 requires a distinct structured token — `[EXPECTED SEALED]` — that enables mechanical verification; current variations use `[CONTRACT COMMITTED]` or `[SEALED — ...]` which are close but not defined as machine-parseable; naming the token explicitly as a structured marker and specifying its exact format produces the token C-13 requires |
| V-04 | output-format combination (V-01 + V-02: per-finding `connector-impact:` slot + `recommended-action:` as required breaking-finding slot) | C-14 + C-15 | Both new criteria target finding-block structure; they are additive and non-competing — adding `connector-impact:` does not crowd `recommended-action:` and vice versa; the finding block template grows by one field for all findings and one field for breaking findings; the combined template enforces both C-14 and C-15 without requiring new reasoning at any step |
| V-05 | lifecycle-emphasis + output-format (V-03 + V-04: `[EXPECTED SEALED]` token + `connector-impact:` slot + `recommended-action:` slot — all three new aspirational criteria in a single variation) | C-13 + C-14 + C-15 | The three new criteria target three distinct points in the artifact: the phase gate (C-13), every finding block field list (C-14), and every breaking finding block field list (C-15); none of the three changes affects the same structural location; the combined variation is additive, not redundant; risk is prompt density — three new structural features may increase cognitive load; prediction: composite aspirational score approaches maximum under v3 |

---

## V-01 — Output Format: Per-Finding Connector-Impact Slot

**axis:** output-format (every finding block includes a required `connector-impact:` labeled field — mandatory on all findings when N findings >= 1, including cosmetic findings; the field is never optional; the operator writes a specific integration-layer impact statement or explicitly states "none" with a rationale)
**hypothesis:** Prior variations satisfy C-06 through at-least-one integration callout: somewhere in the findings, a note appears about connector or Automate impact. This is probe-and-annotate behavior — the operator mentions integration impact when it is salient, and C-06 counts it. C-14 requires per-finding structural enforcement: every finding block carries a `connector-impact:` labeled slot, making integration-lens coverage mandatory at write time for every finding. The difference between C-06 and C-14 is not "more coverage" but "different enforcement mechanism": C-06 measures output; C-14 measures structure. When the template includes `connector-impact:` as a named field with a pass condition stated inline, two things happen: (1) the operator who would have noted integration impact anyway now records it in the dedicated field; (2) the operator who would have omitted it now sees a blank slot that announces its own absence. Neither requires new analytical reasoning — both require only that the field exists. Prediction: C-14 passes because the slot is present in every finding block; C-06 continues to pass because the slot content satisfies the at-least-one callout requirement; C-03, C-04, C-05 unaffected.

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

Write a `## Contract Scope` section. Include: operation and method, connector or Automate flow and environment, input fixture (inline — do not reference external files), and the spec version and section governing this operation's output contract. The section is complete when a reader can determine exactly what is being tested without opening another file.

**Step 2 — Expected Output**

Read the spec. Do not run the operation. Write a `## Expected Output` section.

For each element the spec defines for this operation under the given input — status codes, response fields, headers, behavioral guarantees — write the element and the spec clause that requires it:

`- {field}: {expected value or constraint}  [spec §X.Y]`

If the spec does not define a field: `- {field}: not specified in spec`

Cover all contract surfaces: the success path, at least one error path, and at least one edge case. If the spec does not address a surface, note it.

When every spec-defined element is listed, write: `[CONTRACT COMMITTED]`

Do not continue past this line until the marker is written.

---

### ROLE: Automate

Begin after `[CONTRACT COMMITTED]`.

**Step 3 — Actual Output**

Run or simulate the operation against the given input fixture. Write a `## Actual Output` section. List every field the operation returned — in the same order the Expected Output section used:

`- {field}: {observed value}`

If a field was not returned: `- {field}: [not returned]`
If you cannot verify a field: `- {field}: [not verifiable — reason]`

Every field from the Expected Output section must appear here with an explicit entry. Silent absence of a field is an invisible skip.

---

### ROLE: Connectors Contract Expert (resumed)

**Step 4 — Findings**

Write a `## Findings` section. Compare each Expected Output entry against the corresponding Actual Output entry.

Fields that match: `- {field}: PASS`

Fields that deviate — write a finding block. The block has six fields. All six are required on every finding. For `breaking` and `degraded` findings, the sixth field (`recommendation:`) is required. For `cosmetic` findings, write `recommendation: N/A — cosmetic`.

**Finding block format:**

```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
  — breaking: consumer cannot function correctly on the violated contract
  — degraded: operation completes but a guarantee is silently violated; data loss or incorrect state possible
  — cosmetic: deviates without affecting correctness or consumer behavior
  When uncertain between breaking and degraded: choose breaking.
spec: [exact spec clause violated — section number, field definition, or contract clause as it appears in the spec; if not locatable: "[not located — reason]"]
connector-impact: [integration-layer impact of this deviation — write one of:
  (a) a specific impact: "breaks {Automate / connector name} {field mapping / expression / trigger condition} because {mechanism}"
  (b) explicit none: "none — this surface ({field}) is not consumed by connector schema or Automate flow expressions"
  No finding may omit this field. The integration lens applies to every finding, not only the salient ones.]
hypothesis: [one sentence naming the mechanism — the component, condition, sequence, or boundary condition that produced the wrong output; not a restatement of what differed; if guessing: "[component] [condition] [effect]"]
recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]  (breaking/degraded: required; cosmetic: write N/A)
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

## V-02 — Output Format: Breaking-Finding Template with Required `recommended-action:` Slot

**axis:** output-format (breaking findings use a separate six-field template in which `recommended-action:` is the required sixth labeled slot; the template makes it structurally impossible to record a complete breaking finding without addressing resolution path at write time)
**hypothesis:** C-09 is satisfied when a breaking finding includes content that proposes either a spec amendment or an implementation fix — the content can appear in `recommendation:`, in a prose note, or in the hypothesis field. C-15 requires that `recommended-action:` be a labeled slot in the breaking-finding template itself, so the slot's absence is self-announcing and its presence is structurally enforced. The key distinction: C-09 measures content (did the finding address resolution path?); C-15 measures template structure (does the breaking-finding block have a dedicated labeled slot for resolution path?). Current variations use `recommendation:` on breaking/degraded findings, which partially overlaps C-15, but the field name is `recommendation:` not `recommended-action:` and it is not defined as the required slot the C-15 criterion references. This variation: (1) defines separate templates for breaking vs degraded/cosmetic findings; (2) names the breaking-finding fifth field exactly `recommended-action:` with vocabulary `amend-spec | fix-impl | needs-discussion`; (3) makes the field required by template structure — omitting it produces a visibly incomplete block. Prediction: C-15 passes because the breaking-finding template has `recommended-action:` as a required labeled slot; C-09 continues to pass because the slot content satisfies the amendment-suggestion criterion.

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

Write a `## Contract Scope` section. Include: operation and method, connector or Automate flow and environment, input fixture (inline), spec version and section. Self-contained — reader can determine what is being tested without opening another file.

**Step 2 — Expected Output**

Read the spec. Do not run the operation. Write a `## Expected Output` section.

For each spec-defined element: `- {field}: {expected value or constraint}  [spec §X.Y]`
If not spec-defined: `- {field}: not specified in spec`

Cover: success path, at least one error path, at least one edge case.

When all spec-defined elements are listed: `[CONTRACT COMMITTED]`

Do not proceed past this line.

---

### ROLE: Automate

Begin after `[CONTRACT COMMITTED]`.

**Step 3 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section. For every entry in Expected Output: `- {field}: {observed value}`. If not returned: `- {field}: [not returned]`. If not verifiable: `- {field}: [not verifiable — reason]`. No field from Expected Output may be absent.

---

### ROLE: Connectors Contract Expert (resumed)

**Step 4 — Findings**

Write a `## Findings` section. Compare each Expected Output entry against its Actual Output entry.

Match: `- {field}: PASS`

Deviation — two templates exist. Use the correct one based on severity.

**Template A — Breaking finding (five required fields):**

Use when the consumer cannot function correctly on the violated contract.

```
Breaking Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
spec: [exact spec clause violated — must be locatable by a reader of the spec]
hypothesis: [one sentence naming the mechanism — component, condition, or sequence responsible; not a restatement of the deviation]
recommended-action: [amend-spec | fix-impl | needs-discussion] — [rationale: which side of the contract is wrong and why; one sentence]
```

`recommended-action:` is a required field on every breaking finding. A breaking finding block is not complete without it. Vocabulary: `amend-spec` (spec stated a guarantee the implementation was not designed to provide), `fix-impl` (implementation deviates from a correct spec), `needs-discussion` (defensible on both sides — resolution requires a design decision).

**Template B — Degraded or cosmetic finding (five fields, recommendation on degraded only):**

Use `degraded` when the operation completes but a guarantee is silently violated (data loss or incorrect state possible). Use `cosmetic` when the deviation does not affect correctness or consumer behavior.

```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [degraded | cosmetic]
spec: [exact spec clause violated]
hypothesis: [mechanism sentence]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (degraded: required; cosmetic: N/A)
```

When uncertain between breaking and degraded: use Template A.

Unexpected actual field (present in actual, absent from spec): `- {field}: UNEXPECTED — not in spec contract`

If no deviations: `Contract satisfied — all fields matched expected output. No findings.`

**Automate / Connectors lens:** At least one finding must explicitly note integration-level impact (e.g., which Automate flow expressions or connector field mappings the deviation affects). If no finding has integration impact, confirm: "Connector lens applied — no integration-layer impact found."

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

## V-03 — Lifecycle Emphasis: Machine-Readable Seal Token

**axis:** lifecycle-emphasis (the phase-gate uses the exact structured token `[EXPECTED SEALED]` — defined explicitly in the prompt as a machine-parseable boundary marker with a specific placement requirement: it appears immediately after the last Expected Output entry and before any execution begins; the token is not a prose acknowledgment and not a free-form alternative)
**hypothesis:** Prior variations use `[CONTRACT COMMITTED]` or `[SEALED — Contract Expert exits. Expected Output above is locked...]`. These satisfy C-12: an explicit acknowledgment that expected was sealed before execution. They do not satisfy C-13: C-13 requires a distinct *structured* token, specifically `[EXPECTED SEALED]`, that enables *automated or mechanical* verification of the sequencing invariant. The failure mode: operators read `[CONTRACT COMMITTED]` as equivalent to `[EXPECTED SEALED]` and produce the prose gate (C-12) without the exact token (C-13). This variation addresses that by: (1) naming the token `[EXPECTED SEALED]` explicitly in the prompt as the required string; (2) defining it as a machine-parseable marker, not a prose gate; (3) specifying its required placement (immediately after the last Expected Output entry, before execution begins); (4) distinguishing it from `[CONTRACT COMMITTED]` by explaining what "machine-parseable" means in this context — a parser can verify sequencing by finding `[EXPECTED SEALED]` before any Actual Output content. Prediction: C-13 passes because the operator writes the exact token `[EXPECTED SEALED]` at the correct location; C-12 continues to pass because the structured token also constitutes a phase-gate confirmation.

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

Write a `## Contract Scope` section. Include: operation and method, connector or Automate flow and environment, input fixture (inline), spec version and section governing the output contract. Self-contained — no external file references.

**Step 2 — Expected Output**

Read the spec. Do not run the operation. Write a `## Expected Output` section.

For each spec-defined element: `- {field}: {expected value or constraint}  [spec §X.Y]`
If not spec-defined: `- {field}: not specified in spec`

Cover: success path, at least one error path, at least one edge case.

When every spec-defined element is listed, write the following token on its own line:

```
[EXPECTED SEALED]
```

**What this token is:** `[EXPECTED SEALED]` is a machine-parseable boundary marker. It is the exact string that automated verification tools use to confirm that the expected output was written before any execution output appears in the document. A parser verifying sequencing checks: does `[EXPECTED SEALED]` appear before any `## Actual Output` content? If yes, the integrity constraint is satisfied. If not, the ordering cannot be verified mechanically.

This token is not a prose acknowledgment. Do not paraphrase it, prefix it, or suffix it with prose on the same line. The token on its own line is the marker. Prose explanation may appear in adjacent lines but must not replace or modify the bracketed string.

Do not continue past `[EXPECTED SEALED]` until Automate has completed Step 3.

---

### ROLE: Automate

Begin after `[EXPECTED SEALED]`.

**Step 3 — Actual Output**

Run or simulate the operation against the given input fixture. Write a `## Actual Output` section. For every entry in Expected Output: `- {field}: {observed value}`. If not returned: `- {field}: [not returned]`. If not verifiable: `- {field}: [not verifiable — reason]`.

Every field from Expected Output must appear here. No field may be absent — a field not listed cannot be distinguished from a field not checked.

---

### ROLE: Connectors Contract Expert (resumed)

**Step 4 — Findings**

Write a `## Findings` section. Compare each Expected Output entry against the corresponding Actual Output entry.

Match: `- {field}: PASS`

Deviation — finding block:

```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
  — breaking: consumer cannot function correctly on the violated contract
  — degraded: operation completes but a guarantee is silently violated; data loss or incorrect state possible
  — cosmetic: deviates without affecting correctness or consumer behavior
  When uncertain between breaking and degraded: choose breaking.
spec: [exact spec clause violated — section number or field definition; if not locatable: "[not located — reason]"]
hypothesis: [one sentence naming the mechanism — component, condition, or sequence responsible for the deviation; not a restatement of the deviation; if guessing: "[component] [condition] [effect]"]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded: required; cosmetic: N/A)
```

Automate / Connectors lens: At least one finding must explicitly state the integration-level impact (which Automate flow expressions or connector field mappings are affected). If no finding has integration impact: "Connector lens applied — no integration-layer impact found."

If no deviations: `Contract satisfied — all fields matched expected output. No findings.`

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

## V-04 — Combination: Per-Finding Connector-Impact Slot + Breaking-Finding `recommended-action:` Slot

**axis:** output-format combination (V-01's mandatory `connector-impact:` slot on every finding + V-02's `recommended-action:` as required fifth field in the breaking-finding template — both new structural fields in a single variation)
**hypothesis:** V-01 and V-02 target C-14 and C-15 respectively. Both axes operate on finding-block template structure and do not compete for the same slot position. V-01 adds a field between `spec:` and `hypothesis:`. V-02 adds a field at the end of the breaking-finding block as the fifth required slot. The combination: the finding block for all findings gains `connector-impact:` (satisfying C-14); the breaking-finding template gains `recommended-action:` as its required terminal slot (satisfying C-15). The combined template is longer by two fields. The risk is that operators write filler values to complete the template rather than substantive content. Prediction: C-14 and C-15 both pass; C-06 continues to pass because the `connector-impact:` slot satisfies the at-least-one callout; C-09 continues to pass because `recommended-action:` content satisfies the amendment-suggestion criterion. No regression on essential criteria (C-01 through C-05) is expected.

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

Write a `## Contract Scope` section. Include: operation and method, connector or Automate flow and environment, input fixture (inline), spec version and section. Self-contained — reader can determine exactly what is being tested without opening another file.

**Step 2 — Expected Output**

Read the spec. Do not run the operation. Write a `## Expected Output` section.

For each spec-defined element: `- {field}: {expected value or constraint}  [spec §X.Y]`
If not spec-defined: `- {field}: not specified in spec`

Cover: success path, at least one error path, at least one edge case.

When all spec-defined elements are listed: `[CONTRACT COMMITTED]`

Do not proceed past this line.

---

### ROLE: Automate

Begin after `[CONTRACT COMMITTED]`.

**Step 3 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section.

For every entry in Expected Output: `- {field}: {observed value}`
If not returned: `- {field}: [not returned]`
If not verifiable: `- {field}: [not verifiable — reason]`

No field from Expected Output may be absent. Every field must have an explicit entry.

---

### ROLE: Connectors Contract Expert (resumed)

**Step 4 — Findings**

Write a `## Findings` section. Compare each Expected Output entry against the corresponding Actual Output entry.

Match: `- {field}: PASS`

Deviation — two templates based on severity. Use the correct one.

**Template A — Breaking finding (six required fields):**

```
Breaking Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
spec: [exact spec clause violated — locatable by spec reader without ambiguity]
connector-impact: [integration-layer impact — e.g., "breaks Automate flow expression referencing {field} because the type change from {X} to {Y} invalidates existing bindings" | "breaks connector field mapping at {connector}/{mapping} because the renamed field no longer matches the registered schema key" | "none — this surface is not consumed by connector schema or Automate flow expressions"]
hypothesis: [one sentence naming the mechanism — component, condition, or sequence responsible; not a restatement of the deviation]
recommended-action: [amend-spec | fix-impl | needs-discussion] — [rationale: one sentence identifying which side of the contract is wrong and why]
```

All six fields are required on every breaking finding. `connector-impact:` requires a specific integration impact or an explicit "none" with rationale. `recommended-action:` requires one of the three vocabulary terms plus rationale.

When uncertain between breaking and degraded: use Template A.

**Template B — Degraded finding (six required fields):**

```
Degraded Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
spec: [exact spec clause violated]
connector-impact: [integration-layer impact or "none — [rationale]"]
hypothesis: [mechanism sentence]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]
```

**Template C — Cosmetic finding (five required fields):**

```
Cosmetic Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
spec: [exact spec clause violated]
connector-impact: [integration-layer impact or "none — [rationale]"]
hypothesis: [mechanism sentence]
```

Unexpected actual field (present in actual, absent from spec): `- {field}: UNEXPECTED — not in spec contract`

If no deviations: `Contract satisfied — all fields matched expected output. No findings.`

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

## V-05 — Combination: Machine-Readable Seal + Per-Finding Connector-Impact + Breaking-Finding `recommended-action:`

**axis:** lifecycle-emphasis + output-format (V-03's `[EXPECTED SEALED]` machine-parseable token + V-01's mandatory `connector-impact:` slot on every finding + V-02's `recommended-action:` as required sixth field in breaking-finding template — all three new aspirational criteria in a single variation)
**hypothesis:** C-13, C-14, and C-15 target three structurally independent points in the artifact: the phase-gate boundary (C-13), the per-finding block field list (C-14), and the breaking-finding block terminal slot (C-15). None of the three changes occupies the same structural location. V-03 changes the gate token name and defines it explicitly as machine-parseable. V-01 adds `connector-impact:` between `spec:` and `hypothesis:` in every finding block. V-02 adds `recommended-action:` as the terminal required slot in the breaking-finding template. The three changes are orthogonal and additive: adding `[EXPECTED SEALED]` does not affect the finding block template; adding `connector-impact:` does not affect the gate token; adding `recommended-action:` does not affect either. The primary risk is prompt density: three new structural features plus the full baseline template may exceed comfortable cognitive load. The skeleton approach (anatomy-first: show the complete artifact shape before instructions) mitigates this by giving the operator the target shape before any instruction is read — the three new fields are visible in the skeleton before the operator encounters the instructions that require them. Prediction: C-13, C-14, and C-15 all pass; composite aspirational score approaches maximum under v3 rubric.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### What you are building — read this first

The complete skeleton of the artifact you are about to produce. Every section, marker, and field listed here must appear in the finished artifact.

```
## Contract Scope
  Purpose: self-contained context record
  Must contain: operation + method, connector/Automate context + environment,
                input fixture (inline), spec version + section

## Expected Output
  Purpose: the contract — what the spec requires
  Must contain: every spec-defined field with expected value + spec clause;
                success path, at least one error path, at least one edge case
  Written: from spec only, before the operation is run

[EXPECTED SEALED]
  Marker: machine-parseable boundary token
  Placement: immediately after the last Expected Output entry, before any execution
  Format: the exact string [EXPECTED SEALED] on its own line
  Purpose: enables mechanical verification that expected was written before actual

## Actual Output
  Purpose: complete capture of what the operation returned
  Must contain: every field from ## Expected Output with observed value or [not returned]
  No field from ## Expected Output may be absent

## Findings
  Purpose: field-by-field diff of contract against actual
  Must contain: one entry per field from ## Expected Output
               — PASS entries for matching fields
               — Finding blocks for deviating fields (see templates below)
               — UNEXPECTED entries for fields in actual not in expected
  No field from ## Expected Output may be absent

  Finding block (all findings — fields required for each type):
    Breaking: element / deviation / spec / connector-impact / hypothesis / recommended-action
    Degraded:  element / deviation / spec / connector-impact / hypothesis / recommendation
    Cosmetic:  element / deviation / spec / connector-impact / hypothesis

## Summary
  Purpose: verdict and distribution
  Must contain: per-severity counts (breaking / degraded / cosmetic / total),
                contract-satisfied/violated verdict, coverage ratio
```

The artifact is complete when every section and marker above is present and every field in every finding block is filled.

---

### ROLE: Connectors Contract Expert

**Step 1 — Contract Scope**

Write the `## Contract Scope` section. Fill every element in the skeleton: operation and method, connector or Automate context and environment, input fixture (inline — no file references), spec version and section. Complete when a reader can determine exactly what is being tested without opening another file.

**Step 2 — Expected Output**

Write the `## Expected Output` section from the spec alone. Do not run the operation.

For each spec-defined element: `- {field}: {expected value or constraint}  [spec §X.Y]`
If not spec-defined: `- {field}: not specified in spec`

Cover all contract surfaces defined by the spec: success path, at least one error path, at least one edge case.

When all spec-defined elements are listed, write the seal token on its own line:

```
[EXPECTED SEALED]
```

`[EXPECTED SEALED]` is the machine-parseable boundary marker. It is not a prose acknowledgment and must not be paraphrased. Write the exact string. Do not add text on the same line. This is the token that mechanical verification tools search for to confirm sequencing.

Do not continue past `[EXPECTED SEALED]`. The Contract Expert role suspends here.

---

### ROLE: Automate

Begin after `[EXPECTED SEALED]`.

**Step 3 — Actual Output**

Run or simulate the operation against the given input fixture. Write the `## Actual Output` section.

For every entry in Expected Output: `- {field}: {observed value}`
If not returned: `- {field}: [not returned]`
If not verifiable: `- {field}: [not verifiable — reason]`

The skeleton requires every Expected Output field to appear here. No field may be absent.

---

### ROLE: Connectors Contract Expert (resumed)

**Step 4 — Findings**

Write the `## Findings` section. Compare each Expected Output entry against the corresponding Actual Output entry.

Match: `- {field}: PASS`

Unexpected actual field (in actual, absent from expected): `- {field}: UNEXPECTED — not in spec contract`

Deviation — use the template that matches the severity. The skeleton defines which fields each template requires.

**Template A — Breaking finding (six required fields):**

A breaking finding is one where the consumer cannot function correctly on the violated contract.

```
Breaking Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
spec: [exact spec clause violated — section number, field definition, or clause identifier; if not locatable: "[not located — reason]"]
connector-impact: [integration-layer impact —
  (a) specific: "breaks {Automate / connector} {expression / mapping / trigger} because {mechanism}"
  (b) explicit none: "none — {field} is not consumed by connector schema or Automate flow expressions"
  This field is required on all findings. Write (a) or (b). No finding may omit this field.]
hypothesis: [one sentence naming the mechanism — component, condition, sequence, or boundary condition responsible; not a restatement of the deviation; if guessing: "[component] [condition] [effect]"]
recommended-action: [amend-spec | fix-impl | needs-discussion] — [rationale: one sentence identifying which side of the contract is wrong and why; required on every breaking finding; this field is the fifth required slot in the breaking-finding template]
```

When uncertain between breaking and degraded: use Template A.

**Template B — Degraded finding (six required fields):**

A degraded finding is one where the operation completes but a guarantee is silently violated — data loss or incorrect state is possible.

```
Degraded Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
spec: [exact spec clause violated]
connector-impact: [integration impact (a) or explicit none (b) — required]
hypothesis: [mechanism sentence]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]
```

**Template C — Cosmetic finding (five required fields):**

A cosmetic finding is one that deviates without affecting correctness or consumer behavior.

```
Cosmetic Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
spec: [exact spec clause violated]
connector-impact: [integration impact (a) or explicit none (b) — required]
hypothesis: [mechanism sentence]
```

The skeleton requires one entry per Expected Output field. No field may be absent from Findings.

If no deviations across all fields: `Contract satisfied — all Expected Output entries matched. No findings.`

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
