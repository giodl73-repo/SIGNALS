Written to `simulations/quest/variations/trace-contract-variations-R3-2026-03-14.md`.

---

## Round 3 Variations — Summary

**5 complete prompt bodies** across 1 single-axis-discriminator + 1 single-axis-extension + 1 domain-combo + 1 lifecycle-split + 1 full synthesis:

| V | Axis | Key mechanism | Predicted score |
|---|------|---------------|-----------------|
| **V-01** | Gate binding form — declaration vs checkbox | CONFIRMED/NOT CONFIRMED numbered declarations replace checkboxes | **97.5 or 100** (C-14/C-15 key test) |
| **V-02** | C-16 extended — full gate manifest | ALL gate outcomes as frontmatter keys (6 keys, not just `gate1`) | **100** |
| **V-03** | Domain columns + automation layer | V-03 R2's element-type column + V-05 R2's full gate apparatus | **100** |
| **V-04** | Standalone calibration phase | Phase 4B is a separate phase with its own GATE 4B — cannot be buried in findings | **100** |
| **V-05** | Full synthesis | Domain columns + full gate manifest + standalone calibration + isolation checkpoint | **100** |

**Ceiling:** V-05. All four additive mechanisms compose without conflict.

**Key discriminators for scoring:**

- **C-14 test (V-01):** `[statement] -- [CONFIRMED / NOT CONFIRMED]` declaration format. The rubric says "fillable checkbox or *equivalent* confirmable gate item." If declarations qualify, V-01 scores 100. If only checkbox syntax qualifies, V-01 scores 97.5 (C-14 fail, C-15 fail, C-16 pass → 6/8 A = 7.5).
- **C-16 test (V-02 vs V-05 R2):** Multi-gate (6 keys) vs single-gate (1 key). Both pass C-16; the question is whether the richer manifest changes downstream automation design.
- **C-13 test (V-04 standalone gate):** Phase 4B forces calibration to be a first-class stop — the model cannot combine or skip it inside findings. Stronger structurally than Gate 4's combined checkpoint in V-05 R2.
b_calibration_confirmed: true` | **100** |
| **V-05** | Full synthesis | All mechanisms from V-01–V-04 combined: domain columns + full gate manifest + standalone calibration | GATE 1 checkbox + element-type completeness check | GATE 3 blank-cell + element-type checks | Six frontmatter gate keys | **100** |

**Predicted ceiling:** V-05. The four structural mechanisms (domain columns, full gate manifest,
standalone calibration, isolation checkbox) operate independently — no combination breaks any
criterion. V-02 and V-03 and V-04 each add one non-competing mechanism to V-05 R2's base.

**Key discriminators for scoring:**

- **C-14 test (V-01):** The rubric says "fillable checkbox or equivalent confirmable gate item."
  V-01's CONFIRMED/NOT CONFIRMED declaration items are the test. If declarations satisfy
  "equivalent," declaration form and checkbox form are interchangeable for C-14. If not,
  checkbox syntax is required.
- **C-15 test (V-01):** Same question for blank-cell enforcement — are numbered attestation
  items that name blank cells a gate failure condition equivalent to checkboxes?
- **C-16 test (V-02 vs V-05 R2):** Multi-gate frontmatter (six keys) vs single-gate (one key).
  Both pass C-16, but multi-gate enables automation to query any gate outcome, not just isolation.
- **C-13 test (V-04 vs V-05 R2):** Does a standalone Phase 4B gate produce stronger C-13
  evidence than Gate 4's combined findings-and-calibration checkpoint? Both pass; V-04's
  mechanism is structurally stronger (calibration cannot be buried in or skipped during findings).

---

## V-01: Gate Binding Form (Declaration Log)

**Axis:** Gate binding form — replaces checkbox items with numbered completion declarations
(format: `[statement about gate condition] — [CONFIRMED / NOT CONFIRMED]`). The same phases,
phase gates, and isolation requirement as V-05 R2, but every gate uses declaration syntax
rather than markdown checkbox syntax.

**Hypothesis:** C-14 defines "equivalent confirmable gate item" alongside "fillable checkbox."
A CONFIRMED/NOT CONFIRMED token appended to an explicit isolation statement may satisfy
"equivalent" — the model must produce the attestation word, cannot skip it, and the two-clause
framing is preserved verbatim. Tests whether the rubric's intent (structural confirmability)
covers declaration form or requires checkbox syntax specifically. C-15 is the same test applied
to blank-cell enforcement at Gate 3.

```
You are running /trace:contract. This skill runs in four sequential phases.
Complete each phase fully before advancing. Each phase ends with a GATE ATTESTATION LOG.
Write CONFIRMED or NOT CONFIRMED for every item. Do not advance to the next phase until
all items in the current gate read CONFIRMED.

All column headers in the diff table are fixed. Do not remove or rename any column.
All sub-fields in the findings section are required. Do not omit any sub-field.

---

## SETUP

Contract:       [Connector name + operation, OpenAPI path, typed action, or report spec]
Input:          [Test input in full -- parameters, auth context, version]
Spec document:  [Document and section defining the contract]
Roles:          Automate engineer, Connectors contract expert

---

## PHASE 1: EXPECTED OUTPUT

Write the complete expected output from the contract spec. Do not reference what you know
the actual output to be. Do not consult the runtime, API documentation, or any knowledge
of what the operation currently returns. The spec is the only source.
If the spec is ambiguous, note it and make the most literal determination.

Expected payload (from spec):
[Full expected response / schema / report structure as the spec defines it]

Expected field contract:
| Field path | Expected type | Expected value / constraint | Spec clause |
|------------|--------------|----------------------------|-------------|
| [field]    | [type]       | [value or constraint]      | [field name or section in spec] |
[One row per field the spec defines. Nested paths use dot notation: forecast[].date]

### GATE 1 ATTESTATION LOG

Complete each item. Write CONFIRMED or NOT CONFIRMED after the dash.

1. Expected completeness: All fields defined in the spec are listed in the expected field table --
   [CONFIRMED / NOT CONFIRMED]
2. Spec clause coverage: Each row has a named spec clause reference -- not "see spec", name the
   field or section --
   [CONFIRMED / NOT CONFIRMED]
3. Isolation: Actual output was not referenced during this phase -- not just ordered after,
   but not consulted at all --
   [CONFIRMED / NOT CONFIRMED]

Gate status: [PASS -- all three items CONFIRMED / NEEDS COMPLETION -- list unconfirmed items]
Do not begin PHASE 2 until all three GATE 1 items read CONFIRMED.

---

## PHASE 2: ACTUAL OUTPUT

Capture the actual output from API documentation, connector definition, or last known
response. Do not adjust any field or value to match Phase 1. Report what the runtime
produces exactly, including unexpected fields not in the spec.

Actual payload captured:
[Full actual response as returned by the operation]

Actual field list:
| Field path | Actual type | Actual value | Source |
|------------|------------|--------------|--------|
| [field]    | [type]     | [value]      | [source] |
[All fields in actual response, including unexpected fields not in Phase 1.]

Source: [API documentation version, connector definition date, or test run timestamp]

### GATE 2 ATTESTATION LOG

1. Actual completeness: All fields in the actual response are listed, including unexpected fields --
   [CONFIRMED / NOT CONFIRMED]
2. Independence: Actual output captured without adjusting to match Phase 1 expected values --
   [CONFIRMED / NOT CONFIRMED]
3. Source identified: Source of actual output is identified (version, date, or test run) --
   [CONFIRMED / NOT CONFIRMED]

Gate status: [PASS / NEEDS COMPLETION]
Do not begin PHASE 3 until all three GATE 2 items read CONFIRMED.

---

## PHASE 3: DIFF TABLE -- CLASSIFICATION ONLY

Compare Phase 1 (expected) to Phase 2 (actual) field by field. Every field from either
phase must appear in this table. Classification only in this phase -- do not write root
cause hypotheses here. Do not write findings here. Analysis belongs in Phase 4.

Status values: MATCH | TYPE MISMATCH | VALUE MISMATCH | MISSING (in Phase 1, absent from Phase 2) | UNEXPECTED (in Phase 2, absent from Phase 1)

Severity (for mismatches):
  breaking  = consumer cannot parse or use the response; feature does not work
  degraded  = consumer can proceed but with data loss, coercion, or incorrect values
  cosmetic  = no consumer impact; documentation or naming inconsistency only
For MATCH rows: Severity = N/A, Spec Ref = N/A

Spec Ref for mismatches: name the exact field path or spec section.
"See spec" or "spec" alone does not qualify. A mismatch row with no Spec Ref is incomplete.

| Field path | Phase 1 expected (type/value) | Phase 2 actual (type/value) | Status | Severity | Spec Ref |
|------------|------------------------------|------------------------------|--------|----------|----------|
| [field]    | [type / value]               | [type / value]               | [status] | [breaking/degraded/cosmetic/N/A] | [spec field or section / N/A] |

### GATE 3 ATTESTATION LOG

1. Phase 1 coverage: Every Phase 1 field appears in the diff table --
   [CONFIRMED / NOT CONFIRMED]
2. Phase 2 coverage: Every Phase 2 field (including unexpected) appears in the diff table --
   [CONFIRMED / NOT CONFIRMED]
3. Classification only: No root cause hypotheses or analysis text in this section --
   [CONFIRMED / NOT CONFIRMED]
4. Severity completeness: No Severity cells blank on mismatch rows --
   [CONFIRMED / NOT CONFIRMED]
5. Spec Ref completeness: No Spec Ref cells blank on mismatch rows --
   [CONFIRMED / NOT CONFIRMED]

Mismatch count: [N] (rows where Status is not MATCH)
Gate status: [PASS / NEEDS COMPLETION]
Do not begin PHASE 4 until all five GATE 3 items read CONFIRMED.

---

## PHASE 4: FINDINGS

Write one finding for every mismatch row from Phase 3. MATCH rows do not get findings.
All four sub-fields are required for every finding. Do not omit any sub-field.

**Breaking findings (consumer cannot use the response):**

F-[N] (breaking): [Field path] -- [What the mismatch is, from Phase 3 Status]
  Spec clause: [Phase 3 Spec Ref value for this row -- exact field or section]
  Root cause hypothesis: [Why the runtime deviates -- e.g., API provider renamed field
    in v2.1, type coercion removed from connector action, auth token response shape
    changed, field missing from action parameter mapping, schema generated from stale
    swagger, provider API version mismatch between spec and connector definition]
  Next step: [Specific -- update OpenAPI definition / add type coercion shim / regenerate
    connector schema from updated swagger / update Parse JSON schema in flow /
    file provider API bug report with field path and version evidence]

[Repeat for all breaking findings. If none: "No breaking findings."]

**Degraded findings (feature works, quality reduced):**

F-[N] (degraded): [Field path] -- [What the mismatch is]
  Spec clause: [Spec field or section]
  Root cause hypothesis: [Why]
  Next step: [Specific action]

[Repeat for all degraded findings. If none: "No degraded findings."]

**Cosmetic findings (no consumer impact):**

F-[N] (cosmetic): [Field path] -- [What the mismatch is]
  Spec clause: [Spec field or section]
  Root cause hypothesis: [Why]
  Next step: [Specific action or "Update OpenAPI definition to reflect current behavior."]

[Repeat for all cosmetic findings. If none: "No cosmetic findings."]

### GATE 4 ATTESTATION LOG

1. Mismatch coverage: Every mismatch from Phase 3 has a finding entry --
   [CONFIRMED / NOT CONFIRMED]
2. Sub-field completeness: No finding is missing root cause hypothesis or next step --
   [CONFIRMED / NOT CONFIRMED]
3. Severity calibration: Severity distribution reviewed before finalizing -- not all one level
   unless explicitly justified (if uniform, state the justification here) --
   [CONFIRMED / NOT CONFIRMED -- if uniform, append: "Uniform because: [reason]"]

Feature status: [BLOCKED (any breaking) / DEGRADED (degraded, no breaking) / CLEAN]
Gate status: [PASS / NEEDS COMPLETION]

---

## CONTRACT DELTA

[For spec update workflow. List only clauses requiring amendment based on findings.
Spec-accurate deviations (provider side) do not belong here -- note them separately.]

| Spec clause | Current definition | Required amendment | Finding ref |
|-------------|-------------------|--------------------|-------------|
| [field/section] | [current wording] | [corrected wording] | F-[N] |
[If no spec amendments needed: "Spec accurate. Amendments required on provider side
or connector definition only -- no spec clause changes needed."]

---

Write artifact: simulations/trace/contract/{topic}-contract-{date}.md
Frontmatter: skill, topic, date, contract_name, input, source, feature_status,
breaking_count, degraded_count, cosmetic_count, mismatch_count, spec_ref,
gate1_isolation_confirmed: true.
```

---

## V-02: C-16 Extended (Full Gate Manifest)

**Axis:** C-16 extended -- while V-05 R2 records only `gate1_isolation_confirmed: true` in
frontmatter, this variation records ALL gate outcomes as machine-readable frontmatter keys.
Gate structure and checkbox syntax are identical to V-05 R2.

**Hypothesis:** C-16 passes for any single gate key in frontmatter. Multi-gate manifest is a
richer variant that enables downstream automation to query any phase's completion status --
not just isolation. A CI check can filter runs where `gate3_diff_complete: true` (clean
classification) separately from runs where `gate4_calibration_confirmed: true` (calibrated).
The hypothesis is that multi-gate manifest is strictly superior to single-gate for pipeline
use cases, and the Round 2 V-05 pattern should be extended to cover all gates.

```
You are running /trace:contract. This skill runs in four sequential phases.
Complete each phase fully before advancing. Each phase ends with a named gate.
If a gate does not pass, resolve the gap before proceeding -- do not skip gates.

All column headers in the diff table are fixed. Do not remove or rename any column.
All sub-fields in the findings section are required. Do not omit any sub-field.

---

## SETUP

Contract:       [Connector name + operation, OpenAPI path, typed action, or report spec]
Input:          [Test input in full -- parameters, auth context, version]
Spec document:  [Document and section defining the contract]
Roles:          Automate engineer, Connectors contract expert

---

## PHASE 1: EXPECTED OUTPUT

Write the complete expected output from the contract spec. Do not reference what you know
the actual output to be. Do not consult the runtime, API documentation, or any knowledge
of what the operation currently returns. The spec is the only source.
If the spec is ambiguous, note it and make the most literal determination.

Expected payload (from spec):
[Full expected response / schema / report structure as the spec defines it]

Expected field contract:
| Field path | Expected type | Expected value / constraint | Spec clause |
|------------|--------------|----------------------------|-------------|
| [field]    | [type]       | [value or constraint]      | [field name or section in spec] |
[One row per field the spec defines. Nested paths use dot notation: forecast[].date]

### GATE 1: EXPECTED COMPLETE
[ ] All fields defined in the spec are listed in the expected field table
[ ] Each row has a named spec clause reference -- not "see spec", name the field or section
[ ] Actual output was not referenced during this phase -- not just ordered after,
    but not consulted at all (isolation check: the actual block was not read at this point)

Gate status: [PASS / NEEDS COMPLETION -- describe what is missing]
Do not begin PHASE 2 until all three GATE 1 checkboxes are confirmed.

---

## PHASE 2: ACTUAL OUTPUT

Capture the actual output from API documentation, connector definition, or last known
response. Do not adjust any field or value to match Phase 1. Report what the runtime
produces exactly, including unexpected fields not in the spec.

Actual payload captured:
[Full actual response as returned by the operation]

Actual field list:
| Field path | Actual type | Actual value | Source |
|------------|------------|--------------|--------|
| [field]    | [type]     | [value]      | [source] |
[All fields in actual response, including unexpected fields not in Phase 1.]

Source: [API documentation version, connector definition date, or test run timestamp]

### GATE 2: ACTUAL COMPLETE
[ ] Actual output captured without adjusting to match Phase 1 expected values
[ ] All fields in the actual response are listed, including unexpected fields
[ ] Source of actual output is identified (version, date, or test run)

Gate status: [PASS / NEEDS COMPLETION]
Do not begin PHASE 3 until GATE 2 passes.

---

## PHASE 3: DIFF TABLE -- CLASSIFICATION ONLY

Compare Phase 1 (expected) to Phase 2 (actual) field by field. Every field from either
phase must appear in this table. Classification only in this phase -- do not write root
cause hypotheses here. Do not write findings here. Analysis belongs in Phase 4.

Status values: MATCH | TYPE MISMATCH | VALUE MISMATCH | MISSING (in Phase 1, absent from Phase 2) | UNEXPECTED (in Phase 2, absent from Phase 1)

Severity (for mismatches):
  breaking  = consumer cannot parse or use the response; feature does not work
  degraded  = consumer can proceed but with data loss, coercion, or incorrect values
  cosmetic  = no consumer impact; documentation or naming inconsistency only
For MATCH rows: Severity = N/A, Spec Ref = N/A

Spec Ref for mismatches: name the exact field path or spec section.
"See spec" or "spec" alone does not qualify. A mismatch row with no Spec Ref is incomplete.

| Field path | Phase 1 expected (type/value) | Phase 2 actual (type/value) | Status | Severity | Spec Ref |
|------------|------------------------------|------------------------------|--------|----------|----------|
| [field]    | [type / value]               | [type / value]               | [status] | [breaking/degraded/cosmetic/N/A] | [spec field or section / N/A] |

### GATE 3: DIFF COMPLETE
[ ] Every Phase 1 field appears in the diff table
[ ] Every Phase 2 field (including unexpected) appears in the diff table
[ ] No root cause hypotheses or analysis text in this section -- classification only
[ ] No Severity cells blank on mismatch rows
[ ] No Spec Ref cells blank on mismatch rows

Mismatch count: [N] (rows where Status is not MATCH)
Gate status: [PASS / NEEDS COMPLETION]
Do not begin PHASE 4 until GATE 3 passes with all five checkboxes confirmed.

---

## PHASE 4: FINDINGS

Write one finding for every mismatch row from Phase 3. MATCH rows do not get findings.
All four sub-fields are required for every finding. Do not omit any sub-field.

**Breaking findings (consumer cannot use the response):**

F-[N] (breaking): [Field path] -- [What the mismatch is, from Phase 3 Status]
  Spec clause: [Phase 3 Spec Ref value for this row -- exact field or section]
  Root cause hypothesis: [Why the runtime deviates -- e.g., API provider renamed field
    in v2.1, type coercion removed from connector action, auth token response shape
    changed, field missing from action parameter mapping, schema generated from stale
    swagger, provider API version mismatch between spec and connector definition]
  Next step: [Specific -- update OpenAPI definition / add type coercion shim / regenerate
    connector schema from updated swagger / update Parse JSON schema in flow /
    file provider API bug report with field path and version evidence]

[Repeat for all breaking findings. If none: "No breaking findings."]

**Degraded findings (feature works, quality reduced):**

F-[N] (degraded): [Field path] -- [What the mismatch is]
  Spec clause: [Spec field or section]
  Root cause hypothesis: [Why]
  Next step: [Specific action]

[Repeat for all degraded findings. If none: "No degraded findings."]

**Cosmetic findings (no consumer impact):**

F-[N] (cosmetic): [Field path] -- [What the mismatch is]
  Spec clause: [Spec field or section]
  Root cause hypothesis: [Why]
  Next step: [Specific action or "Update OpenAPI definition to reflect current behavior."]

[Repeat for all cosmetic findings. If none: "No cosmetic findings."]

### GATE 4: FINDINGS COMPLETE
[ ] Every mismatch from Phase 3 has a finding entry
[ ] No finding is missing root cause hypothesis or next step
[ ] Severity distribution reviewed before finalizing -- not all one level unless
    explicitly justified: "[State justification if uniform, or confirm distribution
    is multi-level as expected]"

Feature status: [BLOCKED (any breaking) / DEGRADED (degraded, no breaking) / CLEAN]
Gate status: [PASS / NEEDS COMPLETION]

---

## CONTRACT DELTA

[For spec update workflow. List only clauses requiring amendment based on findings.
Spec-accurate deviations (provider side) do not belong here -- note them separately.]

| Spec clause | Current definition | Required amendment | Finding ref |
|-------------|-------------------|--------------------|-------------|
| [field/section] | [current wording] | [corrected wording] | F-[N] |
[If no spec amendments needed: "Spec accurate. Amendments required on provider side
or connector definition only -- no spec clause changes needed."]

---

Write artifact: simulations/trace/contract/{topic}-contract-{date}.md
Frontmatter: skill, topic, date, contract_name, input, source, feature_status,
breaking_count, degraded_count, cosmetic_count, mismatch_count, spec_ref,
gate1_isolation_confirmed: true,
gate2_actual_complete: true,
gate3_diff_complete: true,
gate3_completeness_enforced: true,
gate4_findings_complete: true,
gate4_calibration_confirmed: true.
```

---

## V-03: Domain Columns + Automation Layer

**Axis:** Combination -- V-03 R2's Contract-element-type column (strongest C-07 mechanism
across all prior rounds) integrated with V-05 R2's full automation layer (isolation checkbox
for C-14, blank-cell gate for C-15, machine-readable frontmatter for C-16).

**Hypothesis:** V-03 R2 scored lowest on the v2 rubric (92) because it had no C-11/C-12/C-13
mechanisms. Its domain coverage (category column + Connector surface sub-field) was the
strongest of any variation. V-05 R2 had the strongest process structure. This variation tests
whether the two are fully composable: adding V-05 R2's gate apparatus to V-03 R2's domain
columns should produce a variation that scores higher on C-07 than V-05 R2 while retaining
all of V-05 R2's structural guarantees.

```
You are running /trace:contract. This skill runs in four sequential phases.
Complete each phase fully before advancing. Each phase ends with a named gate.
If a gate does not pass, resolve the gap before proceeding -- do not skip gates.

All column headers are fixed. Do not remove, rename, or reorder any column.
Contract element type is a required column on every field row -- do not leave it blank.
All sub-fields in the findings section are required. Do not omit any sub-field.

Contract element types (assign exactly one per field):
  schema-field      = a typed data field in the response payload
  auth-handshake    = authentication or token field (bearer token, API key, scope, expiry)
  action-payload    = input or output of a Power Automate connector action parameter
  trigger-payload   = field in a connector trigger event payload
  error-shape       = field in an error response structure (code, message, detail, retry-after)
  metadata          = response envelope field not part of business payload (headers,
                      pagination cursors, correlation IDs, ETags, timestamps)

---

## SETUP

Contract:       [Connector name + operation, OpenAPI path, typed action, or report spec]
Input:          [Test input in full -- parameters, auth context, version]
Spec document:  [Document and section defining the contract]
Roles:          Automate engineer, Connectors contract expert

---

## PHASE 1: EXPECTED OUTPUT

Write the complete expected output from the contract spec. Do not reference what you know
the actual output to be. Do not consult the runtime, API documentation, or any knowledge
of what the operation currently returns. The spec is the only source.
Assign a contract element type to every field.

Expected payload (from spec):
[Full expected response / schema / report structure as the spec defines it]

Expected field contract:
| Field path | Contract element type | Expected type | Expected value / constraint | Spec clause |
|------------|----------------------|--------------|----------------------------|-------------|
| [field]    | [schema-field / auth-handshake / action-payload / trigger-payload / error-shape / metadata] | [type] | [value or constraint] | [field name or section in spec] |
[One row per field the spec defines. Every row must have a contract element type assigned.]

### GATE 1: EXPECTED COMPLETE
[ ] All fields defined in the spec are listed in the expected field table
[ ] Each row has a named spec clause reference -- not "see spec", name the field or section
[ ] Each row has a contract element type assigned -- no blank Contract element type cells
[ ] Actual output was not referenced during this phase -- not just ordered after,
    but not consulted at all (isolation check: the actual block was not read at this point)

Gate status: [PASS / NEEDS COMPLETION -- describe what is missing]
Do not begin PHASE 2 until all four GATE 1 checkboxes are confirmed.

---

## PHASE 2: ACTUAL OUTPUT

Capture the actual output from API documentation, connector definition, or last known
response. Do not adjust any field or value to match Phase 1. Report what the runtime
produces exactly, including unexpected fields. Assign contract element types to every row.

Actual payload captured:
[Full actual response as returned by the operation]

Actual field list:
| Field path | Contract element type | Actual type | Actual value | Source |
|------------|----------------------|------------|--------------|--------|
| [field]    | [schema-field / auth-handshake / action-payload / trigger-payload / error-shape / metadata] | [type] | [value] | [source] |
[All fields in actual response, including unexpected fields not in Phase 1.
For unexpected fields, assign the most fitting contract element type.]

Source: [API documentation version, connector definition date, or test run timestamp]

### GATE 2: ACTUAL COMPLETE
[ ] Actual output captured without adjusting to match Phase 1 expected values
[ ] All fields in the actual response are listed, including unexpected fields
[ ] Contract element type assigned to every actual field row -- no blank type cells
[ ] Source of actual output is identified (version, date, or test run)

Gate status: [PASS / NEEDS COMPLETION]
Do not begin PHASE 3 until GATE 2 passes.

---

## PHASE 3: DIFF TABLE -- CLASSIFICATION ONLY

Compare Phase 1 (expected) to Phase 2 (actual) field by field. Every field from either
phase must appear in this table. Carry the contract element type from Phase 1 or Phase 2.
Classification only -- do not write root cause hypotheses here. Analysis belongs in Phase 4.

Status values: MATCH | TYPE MISMATCH | VALUE MISMATCH | MISSING (in Phase 1, absent from Phase 2) | UNEXPECTED (in Phase 2, absent from Phase 1)

Severity (for mismatches):
  breaking  = consumer cannot parse or use the response; feature does not work
  degraded  = consumer can proceed but with data loss, coercion, or incorrect values
  cosmetic  = no consumer impact; documentation or naming inconsistency only
For MATCH rows: Severity = N/A, Spec Ref = N/A

Spec Ref for mismatches: name the exact field path or spec section.
"See spec" or "spec" alone does not qualify. A mismatch row with no Spec Ref is incomplete.

| Field path | Contract element type | Phase 1 expected (type/value) | Phase 2 actual (type/value) | Status | Severity | Spec Ref |
|------------|-----------------------|------------------------------|------------------------------|--------|----------|----------|
| [field]    | [element type]        | [type / value]               | [type / value]               | [status] | [breaking/degraded/cosmetic/N/A] | [spec field or section / N/A] |

### GATE 3: DIFF COMPLETE
[ ] Every Phase 1 field appears in the diff table
[ ] Every Phase 2 field (including unexpected) appears in the diff table
[ ] No root cause hypotheses or analysis text in this section -- classification only
[ ] No Severity cells blank on mismatch rows
[ ] No Spec Ref cells blank on mismatch rows
[ ] Contract element type carried to every row -- no blank type cells in diff

Mismatch count: [N] (rows where Status is not MATCH)
Gate status: [PASS / NEEDS COMPLETION]
Do not begin PHASE 4 until GATE 3 passes with all six checkboxes confirmed.

---

## PHASE 4: FINDINGS

Write one finding for every mismatch row from Phase 3. MATCH rows do not get findings.
All five sub-fields are required for every finding. Do not omit any sub-field.
"Connector surface" names where in the Automate/Connectors stack the fix lives.

**Breaking findings (consumer cannot use the response):**

F-[N] (breaking): [Field path] -- [What the mismatch is, from Phase 3 Status]
  Contract element type: [from Phase 3 diff table]
  Connector surface: [Where the fix lives -- connector action definition / OpenAPI schema /
    trigger payload definition / auth token handler / error response parser /
    Parse JSON schema in Power Automate flow]
  Spec clause: [Phase 3 Spec Ref value for this row -- exact field or section]
  Root cause hypothesis: [Why the runtime deviates -- API provider renamed field in v2.1,
    type coercion removed from connector action, auth token response shape changed,
    field absent from action parameter definition, schema from stale swagger,
    provider API version mismatch between spec and connector definition]
  Next step: [Specific action at the named connector surface]

[Repeat for all breaking findings. If none: "No breaking findings."]

**Degraded findings (feature works, quality reduced):**

F-[N] (degraded): [Field path] -- [What the mismatch is]
  Contract element type: [element type]
  Connector surface: [Where the fix lives]
  Spec clause: [Spec field or section]
  Root cause hypothesis: [Why]
  Next step: [Specific action]

[Repeat for all degraded findings. If none: "No degraded findings."]

**Cosmetic findings (no consumer impact):**

F-[N] (cosmetic): [Field path] -- [What the mismatch is]
  Contract element type: [element type]
  Connector surface: [Where the fix lives]
  Spec clause: [Spec field or section]
  Root cause hypothesis: [Why]
  Next step: [Specific action or "Update OpenAPI definition to reflect current behavior."]

[Repeat for all cosmetic findings. If none: "No cosmetic findings."]

### GATE 4: FINDINGS COMPLETE
[ ] Every mismatch from Phase 3 has a finding entry
[ ] No finding is missing contract element type, connector surface, root cause hypothesis, or next step
[ ] Severity distribution reviewed before finalizing -- not all one level unless
    explicitly justified: "[State justification if uniform, or confirm distribution
    is multi-level as expected]"

Feature status: [BLOCKED (any breaking) / DEGRADED (degraded, no breaking) / CLEAN]
Gate status: [PASS / NEEDS COMPLETION]

---

## CONTRACT DELTA

[For spec update workflow. List only clauses requiring amendment based on findings.
Spec-accurate deviations (provider side) do not belong here -- note them separately.]

| Spec clause | Contract element type | Current definition | Required amendment | Finding ref |
|-------------|----------------------|-------------------|--------------------|-------------|
| [field/section] | [element type] | [current wording] | [corrected wording] | F-[N] |
[If no spec amendments needed: "Spec accurate. Amendments required on provider side
or connector definition only -- no spec clause changes needed."]

---

Write artifact: simulations/trace/contract/{topic}-contract-{date}.md
Frontmatter: skill, topic, date, contract_name, input, source, feature_status,
breaking_count, degraded_count, cosmetic_count, mismatch_count, spec_ref,
element_types_used: [list of contract element types that appeared in findings],
gate1_isolation_confirmed: true.
```

---

## V-04: Standalone Calibration Phase (Phase 4B)

**Axis:** Lifecycle -- splits Phase 4 (findings) and calibration review into two separate
sequential phases. Phase 4 ends with a gate that checks findings completeness only. Phase 4B
is a dedicated calibration phase with its own gate. The calibration section is structurally
separate and cannot be combined with or buried in the findings writing step.

**Hypothesis:** V-05 R2 GATE 4 combines findings completeness check and calibration review
into a single gate at the end of Phase 4. This is structurally correct but allows calibration
to be treated as an afterthought if the model prioritizes the findings completeness items.
A standalone Phase 4B forces calibration to be a full phase -- the model must stop findings
writing, close Phase 4, open a new section, and produce the calibration assessment as a
first-class artifact. This tests whether a structurally separate calibration gate produces
stronger C-13 evidence than a combined gate, and whether Phase 4B frontmatter
(gate4b_calibration_confirmed: true) is a useful second machine-readable key.

```
You are running /trace:contract. This skill runs in five sequential phases.
Phase 4 (findings) and Phase 4B (calibration review) are separate -- do not merge them.
Calibration is a standalone gate; it cannot be completed inside the findings writing step.
Each phase ends with a named gate. Do not skip gates or phases.

All column headers in the diff table are fixed. Do not remove or rename any column.
All sub-fields in the findings section are required. Do not omit any sub-field.

---

## SETUP

Contract:       [Connector name + operation, OpenAPI path, typed action, or report spec]
Input:          [Test input in full -- parameters, auth context, version]
Spec document:  [Document and section defining the contract]
Roles:          Automate engineer, Connectors contract expert

---

## PHASE 1: EXPECTED OUTPUT

Write the complete expected output from the contract spec. Do not reference what you know
the actual output to be. Do not consult the runtime, API documentation, or any knowledge
of what the operation currently returns. The spec is the only source.
If the spec is ambiguous, note it and make the most literal determination.

Expected payload (from spec):
[Full expected response / schema / report structure as the spec defines it]

Expected field contract:
| Field path | Expected type | Expected value / constraint | Spec clause |
|------------|--------------|----------------------------|-------------|
| [field]    | [type]       | [value or constraint]      | [field name or section in spec] |
[One row per field the spec defines. Nested paths use dot notation: forecast[].date]

### GATE 1: EXPECTED COMPLETE
[ ] All fields defined in the spec are listed in the expected field table
[ ] Each row has a named spec clause reference -- not "see spec", name the field or section
[ ] Actual output was not referenced during this phase -- not just ordered after,
    but not consulted at all (isolation check: the actual block was not read at this point)

Gate status: [PASS / NEEDS COMPLETION -- describe what is missing]
Do not begin PHASE 2 until all three GATE 1 checkboxes are confirmed.

---

## PHASE 2: ACTUAL OUTPUT

Capture the actual output from API documentation, connector definition, or last known
response. Do not adjust any field or value to match Phase 1. Report what the runtime
produces exactly, including unexpected fields not in the spec.

Actual payload captured:
[Full actual response as returned by the operation]

Actual field list:
| Field path | Actual type | Actual value | Source |
|------------|------------|--------------|--------|
| [field]    | [type]     | [value]      | [source] |
[All fields in actual response, including unexpected fields not in Phase 1.]

Source: [API documentation version, connector definition date, or test run timestamp]

### GATE 2: ACTUAL COMPLETE
[ ] Actual output captured without adjusting to match Phase 1 expected values
[ ] All fields in the actual response are listed, including unexpected fields
[ ] Source of actual output is identified (version, date, or test run)

Gate status: [PASS / NEEDS COMPLETION]
Do not begin PHASE 3 until GATE 2 passes.

---

## PHASE 3: DIFF TABLE -- CLASSIFICATION ONLY

Compare Phase 1 (expected) to Phase 2 (actual) field by field. Every field from either
phase must appear in this table. Classification only in this phase -- do not write root
cause hypotheses here. Do not write findings here. Analysis belongs in Phase 4.

Status values: MATCH | TYPE MISMATCH | VALUE MISMATCH | MISSING (in Phase 1, absent from Phase 2) | UNEXPECTED (in Phase 2, absent from Phase 1)

Severity (for mismatches):
  breaking  = consumer cannot parse or use the response; feature does not work
  degraded  = consumer can proceed but with data loss, coercion, or incorrect values
  cosmetic  = no consumer impact; documentation or naming inconsistency only
For MATCH rows: Severity = N/A, Spec Ref = N/A

Spec Ref for mismatches: name the exact field path or spec section.
"See spec" or "spec" alone does not qualify. A mismatch row with no Spec Ref is incomplete.

| Field path | Phase 1 expected (type/value) | Phase 2 actual (type/value) | Status | Severity | Spec Ref |
|------------|------------------------------|------------------------------|--------|----------|----------|
| [field]    | [type / value]               | [type / value]               | [status] | [breaking/degraded/cosmetic/N/A] | [spec field or section / N/A] |

### GATE 3: DIFF COMPLETE
[ ] Every Phase 1 field appears in the diff table
[ ] Every Phase 2 field (including unexpected) appears in the diff table
[ ] No root cause hypotheses or analysis text in this section -- classification only
[ ] No Severity cells blank on mismatch rows
[ ] No Spec Ref cells blank on mismatch rows

Mismatch count: [N] (rows where Status is not MATCH)
Gate status: [PASS / NEEDS COMPLETION]
Do not begin PHASE 4 until GATE 3 passes with all five checkboxes confirmed.

---

## PHASE 4: FINDINGS

Write one finding for every mismatch row from Phase 3. MATCH rows do not get findings.
All four sub-fields are required for every finding. Do not omit any sub-field.
Do not evaluate severity calibration here -- that is Phase 4B.

**Breaking findings (consumer cannot use the response):**

F-[N] (breaking): [Field path] -- [What the mismatch is, from Phase 3 Status]
  Spec clause: [Phase 3 Spec Ref value for this row -- exact field or section]
  Root cause hypothesis: [Why the runtime deviates -- e.g., API provider renamed field
    in v2.1, type coercion removed from connector action, auth token response shape
    changed, field missing from action parameter mapping, schema generated from stale
    swagger, provider API version mismatch between spec and connector definition]
  Next step: [Specific -- update OpenAPI definition / add type coercion shim / regenerate
    connector schema from updated swagger / update Parse JSON schema in flow /
    file provider API bug report with field path and version evidence]

[Repeat for all breaking findings. If none: "No breaking findings."]

**Degraded findings (feature works, quality reduced):**

F-[N] (degraded): [Field path] -- [What the mismatch is]
  Spec clause: [Spec field or section]
  Root cause hypothesis: [Why]
  Next step: [Specific action]

[Repeat for all degraded findings. If none: "No degraded findings."]

**Cosmetic findings (no consumer impact):**

F-[N] (cosmetic): [Field path] -- [What the mismatch is]
  Spec clause: [Spec field or section]
  Root cause hypothesis: [Why]
  Next step: [Specific action or "Update OpenAPI definition to reflect current behavior."]

[Repeat for all cosmetic findings. If none: "No cosmetic findings."]

### GATE 4: FINDINGS COMPLETE
[ ] Every mismatch from Phase 3 has a finding entry
[ ] No finding is missing root cause hypothesis or next step

Gate status: [PASS / NEEDS COMPLETION]
Do not begin PHASE 4B until GATE 4 passes.

---

## PHASE 4B: SEVERITY CALIBRATION REVIEW

Review the complete severity distribution across all Phase 4 findings before writing
the summary. This phase exists because calibration requires the full finding set in view --
it cannot be done reliably while findings are still being written.

Severity tally (count from Phase 4 findings):
| Severity | Count |
|----------|-------|
| Breaking | [N]   |
| Degraded | [N]   |
| Cosmetic | [N]   |
| Total    | [N]   |

Calibration assessment:
Is the severity distribution uniform (all one level)? [YES / NO]

If YES -- state explicit justification:
"All findings are [breaking / degraded / cosmetic] because [specific reason that explains
why every mismatch has the same consumer impact. This is not a default assignment -- it
reflects the actual connector surface behavior where: (explain)]."

If NO -- confirm the distribution is reasonable:
"Distribution spans [severity levels present]. The assignments are consistent with
consumer impact at each connector surface: [brief explanation of why different severities
appear across the mismatch types found]."

### GATE 4B: CALIBRATION CONFIRMED
[ ] Severity tally matches Phase 4 findings exactly
[ ] Calibration assessment is written -- either uniform-distribution justification or
    multi-level confirmation, not left blank
[ ] Feature status determined from tally: BLOCKED if any breaking, DEGRADED if degraded
    with no breaking, CLEAN if all cosmetic or no findings

Feature status: [BLOCKED / DEGRADED / CLEAN]
Gate status: [PASS / NEEDS COMPLETION]
Do not write CONTRACT DELTA until GATE 4B passes.

---

## CONTRACT DELTA

[For spec update workflow. List only clauses requiring amendment based on findings.
Spec-accurate deviations (provider side) do not belong here -- note them separately.]

| Spec clause | Current definition | Required amendment | Finding ref |
|-------------|-------------------|--------------------|-------------|
| [field/section] | [current wording] | [corrected wording] | F-[N] |
[If no spec amendments needed: "Spec accurate. Amendments required on provider side
or connector definition only -- no spec clause changes needed."]

---

Write artifact: simulations/trace/contract/{topic}-contract-{date}.md
Frontmatter: skill, topic, date, contract_name, input, source, feature_status,
breaking_count, degraded_count, cosmetic_count, mismatch_count, spec_ref,
gate1_isolation_confirmed: true,
gate4b_calibration_confirmed: true.
```

---

## V-05: Full Synthesis (Domain Columns + Full Gate Manifest + Standalone Calibration)

**Axes:** V-05 R2 as base + V-03 R3's Contract-element-type column and Connector-surface
sub-field (domain emphasis) + V-02 R3's multi-gate frontmatter (C-16 extended) + V-04 R3's
standalone Phase 4B calibration gate (C-13 structural isolation).

**Hypothesis:** The four mechanisms operate independently. Domain columns add C-07 depth
without touching gate structure. Multi-gate frontmatter adds queryable keys without changing
gate content. Standalone calibration adds C-13 structural rigor without affecting the diff
or isolation mechanisms. No combination is contradictory. This is the designed-for-100 ceiling
variation on the v3 rubric: all 16 criteria structurally guaranteed.

```
You are running /trace:contract. This skill runs in five sequential phases.
Phase 4 (findings) and Phase 4B (calibration review) are separate -- do not merge them.
Each phase ends with a named gate. Do not skip gates or phases.

All column headers are fixed. Do not remove, rename, or reorder any column.
Contract element type is a required column on every field row -- do not leave it blank.
All sub-fields in the findings section are required. Do not omit any sub-field.

Contract element types (assign exactly one per field):
  schema-field      = a typed data field in the response payload
  auth-handshake    = authentication or token field (bearer token, API key, scope, expiry)
  action-payload    = input or output of a Power Automate connector action parameter
  trigger-payload   = field in a connector trigger event payload
  error-shape       = field in an error response structure (code, message, detail, retry-after)
  metadata          = response envelope field not part of business payload (headers,
                      pagination cursors, correlation IDs, ETags, timestamps)

---

## SETUP

Contract:       [Connector name + operation, OpenAPI path, typed action, or report spec]
Input:          [Test input in full -- parameters, auth context, version]
Spec document:  [Document and section defining the contract]
Roles:          Automate engineer, Connectors contract expert

---

## PHASE 1: EXPECTED OUTPUT

Write the complete expected output from the contract spec. Do not reference what you know
the actual output to be. Do not consult the runtime, API documentation, or any knowledge
of what the operation currently returns. The spec is the only source.
Assign a contract element type to every field.

Expected payload (from spec):
[Full expected response / schema / report structure as the spec defines it]

Expected field contract:
| Field path | Contract element type | Expected type | Expected value / constraint | Spec clause |
|------------|----------------------|--------------|----------------------------|-------------|
| [field]    | [schema-field / auth-handshake / action-payload / trigger-payload / error-shape / metadata] | [type] | [value or constraint] | [field name or section in spec] |
[One row per field the spec defines. Every row must have a contract element type assigned.]

### GATE 1: EXPECTED COMPLETE
[ ] All fields defined in the spec are listed in the expected field table
[ ] Each row has a named spec clause reference -- not "see spec", name the field or section
[ ] Each row has a contract element type assigned -- no blank Contract element type cells
[ ] Actual output was not referenced during this phase -- not just ordered after,
    but not consulted at all (isolation check: the actual block was not read at this point)

Gate status: [PASS / NEEDS COMPLETION -- describe what is missing]
Do not begin PHASE 2 until all four GATE 1 checkboxes are confirmed.

---

## PHASE 2: ACTUAL OUTPUT

Capture the actual output from API documentation, connector definition, or last known
response. Do not adjust any field or value to match Phase 1. Report what the runtime
produces exactly, including unexpected fields. Assign contract element types to every row.

Actual payload captured:
[Full actual response as returned by the operation]

Actual field list:
| Field path | Contract element type | Actual type | Actual value | Source |
|------------|----------------------|------------|--------------|--------|
| [field]    | [schema-field / auth-handshake / action-payload / trigger-payload / error-shape / metadata] | [type] | [value] | [source] |
[All fields in actual response, including unexpected fields not in Phase 1.
For unexpected fields, assign the most fitting contract element type.]

Source: [API documentation version, connector definition date, or test run timestamp]

### GATE 2: ACTUAL COMPLETE
[ ] Actual output captured without adjusting to match Phase 1 expected values
[ ] All fields in the actual response are listed, including unexpected fields
[ ] Contract element type assigned to every actual field row -- no blank type cells
[ ] Source of actual output is identified (version, date, or test run)

Gate status: [PASS / NEEDS COMPLETION]
Do not begin PHASE 3 until GATE 2 passes.

---

## PHASE 3: DIFF TABLE -- CLASSIFICATION ONLY

Compare Phase 1 (expected) to Phase 2 (actual) field by field. Every field from either
phase must appear in this table. Carry the contract element type from Phase 1 or Phase 2.
Classification only -- do not write root cause hypotheses here. Analysis belongs in Phase 4.

Status values: MATCH | TYPE MISMATCH | VALUE MISMATCH | MISSING (in Phase 1, absent from Phase 2) | UNEXPECTED (in Phase 2, absent from Phase 1)

Severity (for mismatches):
  breaking  = consumer cannot parse or use the response; feature does not work
  degraded  = consumer can proceed but with data loss, coercion, or incorrect values
  cosmetic  = no consumer impact; documentation or naming inconsistency only
For MATCH rows: Severity = N/A, Spec Ref = N/A

Spec Ref for mismatches: name the exact field path or spec section.
"See spec" or "spec" alone does not qualify. A mismatch row with no Spec Ref is incomplete.

| Field path | Contract element type | Phase 1 expected (type/value) | Phase 2 actual (type/value) | Status | Severity | Spec Ref |
|------------|-----------------------|------------------------------|------------------------------|--------|----------|----------|
| [field]    | [element type]        | [type / value]               | [type / value]               | [status] | [breaking/degraded/cosmetic/N/A] | [spec field or section / N/A] |

### GATE 3: DIFF COMPLETE
[ ] Every Phase 1 field appears in the diff table
[ ] Every Phase 2 field (including unexpected) appears in the diff table
[ ] No root cause hypotheses or analysis text in this section -- classification only
[ ] No Severity cells blank on mismatch rows
[ ] No Spec Ref cells blank on mismatch rows
[ ] Contract element type carried to every row -- no blank type cells in diff

Mismatch count: [N] (rows where Status is not MATCH)
Gate status: [PASS / NEEDS COMPLETION]
Do not begin PHASE 4 until GATE 3 passes with all six checkboxes confirmed.

---

## PHASE 4: FINDINGS

Write one finding for every mismatch row from Phase 3. MATCH rows do not get findings.
All five sub-fields are required for every finding. Do not evaluate severity calibration
here -- that is Phase 4B.

**Breaking findings (consumer cannot use the response):**

F-[N] (breaking): [Field path] -- [What the mismatch is, from Phase 3 Status]
  Contract element type: [from Phase 3 diff table]
  Connector surface: [Where the fix lives -- connector action definition / OpenAPI schema /
    trigger payload definition / auth token handler / error response parser /
    Parse JSON schema in Power Automate flow]
  Spec clause: [Phase 3 Spec Ref value for this row -- exact field or section]
  Root cause hypothesis: [Why the runtime deviates -- API provider renamed field in v2.1,
    type coercion removed from connector action, auth token response shape changed,
    field absent from action parameter definition, schema from stale swagger,
    provider API version mismatch between spec and connector definition]
  Next step: [Specific action at the named connector surface]

[Repeat for all breaking findings. If none: "No breaking findings."]

**Degraded findings (feature works, quality reduced):**

F-[N] (degraded): [Field path] -- [What the mismatch is]
  Contract element type: [element type]
  Connector surface: [Where the fix lives]
  Spec clause: [Spec field or section]
  Root cause hypothesis: [Why]
  Next step: [Specific action]

[Repeat for all degraded findings. If none: "No degraded findings."]

**Cosmetic findings (no consumer impact):**

F-[N] (cosmetic): [Field path] -- [What the mismatch is]
  Contract element type: [element type]
  Connector surface: [Where the fix lives]
  Spec clause: [Spec field or section]
  Root cause hypothesis: [Why]
  Next step: [Specific action or "Update OpenAPI definition to reflect current behavior."]

[Repeat for all cosmetic findings. If none: "No cosmetic findings."]

### GATE 4: FINDINGS COMPLETE
[ ] Every mismatch from Phase 3 has a finding entry
[ ] No finding is missing contract element type, connector surface, root cause hypothesis,
    or next step

Gate status: [PASS / NEEDS COMPLETION]
Do not begin PHASE 4B until GATE 4 passes.

---

## PHASE 4B: SEVERITY CALIBRATION REVIEW

Review the complete severity distribution across all Phase 4 findings before writing
the summary. This phase exists because calibration requires the full finding set in view.

Severity tally:
| Severity | Count |
|----------|-------|
| Breaking | [N]   |
| Degraded | [N]   |
| Cosmetic | [N]   |
| Total    | [N]   |

Calibration assessment:
Is the severity distribution uniform (all one level)? [YES / NO]

If YES -- state explicit justification:
"All findings are [breaking / degraded / cosmetic] because [specific reason every mismatch
has the same consumer impact -- not a default, an earned claim based on the connector
surface behavior]."

If NO -- confirm the distribution is reasonable:
"Distribution spans [severity levels present]. The assignments are consistent with consumer
impact at each connector surface."

### GATE 4B: CALIBRATION CONFIRMED
[ ] Severity tally matches Phase 4 findings exactly
[ ] Calibration assessment written -- uniform distribution justified, or multi-level confirmed
[ ] Feature status determined: BLOCKED if any breaking, DEGRADED if degraded with no breaking,
    CLEAN if all cosmetic or no findings

Feature status: [BLOCKED / DEGRADED / CLEAN]
Gate status: [PASS / NEEDS COMPLETION]
Do not write CONTRACT DELTA until GATE 4B passes.

---

## CONTRACT DELTA

[For spec update workflow. List only clauses requiring amendment based on findings.
Spec-accurate deviations (provider side) do not belong here -- note them separately.]

| Spec clause | Contract element type | Current definition | Required amendment | Finding ref |
|-------------|----------------------|-------------------|--------------------|-------------|
| [field/section] | [element type] | [current wording] | [corrected wording] | F-[N] |
[If no spec amendments needed: "Spec accurate. Amendments required on provider side
or connector definition only -- no spec clause changes needed."]

---

Write artifact: simulations/trace/contract/{topic}-contract-{date}.md
Frontmatter: skill, topic, date, contract_name, input, source, feature_status,
breaking_count, degraded_count, cosmetic_count, mismatch_count, spec_ref,
element_types_used: [list of contract element types that appeared in findings],
gate1_isolation_confirmed: true,
gate2_actual_complete: true,
gate3_diff_complete: true,
gate3_completeness_enforced: true,
gate4_findings_complete: true,
gate4b_calibration_confirmed: true.
```

---

## Round 3 Design Notes

### Axis selection rationale

Round 3 answers four open questions from Round 2's design notes:

**Q1 (R2 Q1) -- Minimum isolation declaration form (V-01):** Round 2 showed that role-semantic
prose (V-02 R2) and gate-level checkbox (V-05 R2) both pass C-12. Round 3 V-01 tests whether
a numbered CONFIRMED/NOT CONFIRMED declaration satisfies C-14's "equivalent confirmable gate
item." If it does, declaration form is equivalent to checkbox for both C-12 and C-14. If it
fails C-14, checkbox syntax is the specifically required form.

**Q2 (R2 Q2) -- Domain column integration (V-03):** Round 2 confirmed that V-03 R2's category
column produced the strongest C-07 coverage of any variation. Round 3 V-03 integrates it with
V-05 R2's full automation layer. If V-03 R3 scores 100 (predicted), the category column adds
to V-05 R2 without cost.

**Q3 (R2 Q3) -- Hybrid inertia + gates:** Not revisited in Round 3. Round 2 confirmed V-04 R2's
anti-pattern framing produced C-09/C-11/C-13 without gate machinery. Adding C-14/C-15/C-16 to
an inertia-framing variation would require adding checkboxes -- at which point it becomes a
gate-based variant. The hybrid is V-05 R2, which already achieves this.

**Q4 (R2 Q4) -- Standalone calibration section (V-04):** Implemented directly. Phase 4B
isolates the calibration review as a first-class phase. The test is whether a standalone
calibration gate produces different C-13 evidence than a combined findings/calibration gate,
and whether `gate4b_calibration_confirmed: true` as a distinct frontmatter key is useful.

**V-02 R3 (multi-gate manifest):** Addresses the natural extension of C-16. V-05 R2 records
one gate key. V-02 R3 records all six. Tests whether downstream tooling should expect one key
per skill or one key per gate.

**V-05 R3 (full synthesis):** Combines all four additive mechanisms. Designed for 100/100 with
no criterion relying on instruction-level compliance -- every criterion has a structural guarantee.

### Predicted rubric performance (v3 rubric, 16 criteria)

| V | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | Score |
|---|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-------|
| V-01 | SETUP section | GATE 3 item 4 | GATE 3 item 5 | sub-field | sections | phase labels | role names | next step | GATE 4 item 3 | pre-printed | GATE 3 item 3 | GATE 1 item 3 | GATE 4 item 3 | item 3 = "equivalent"? | item 4-5 = "equivalent"? | frontmatter key | 97.5 or 100 |
| V-02 | SETUP section | GATE 3 checkbox | GATE 3 checkbox | sub-field | sections | phase labels | role names | next step | GATE 4 checkbox | pre-printed | GATE 3 checkbox | GATE 1 checkbox | GATE 4 checkbox | GATE 1 checkbox | GATE 3 checkbox | 6 frontmatter keys | **100** |
| V-03 | SETUP section | GATE 3 checkbox | GATE 3 checkbox | sub-field | sections | phase labels | element-type column + Connector surface | next step | GATE 4 checkbox | pre-printed + element type | GATE 3 checkbox | GATE 1 checkbox | GATE 4 checkbox | GATE 1 checkbox | GATE 3 checkbox | frontmatter key | **100** |
| V-04 | SETUP section | GATE 3 checkbox | GATE 3 checkbox | sub-field | sections | phase labels | role names | next step | GATE 4B | pre-printed | GATE 3 checkbox | GATE 1 checkbox | GATE 4B standalone | GATE 1 checkbox | GATE 3 checkbox | 2 frontmatter keys | **100** |
| V-05 | SETUP section | GATE 3 checkbox | GATE 3 checkbox | sub-field | sections | phase labels | element-type column + Connector surface | next step | GATE 4B | pre-printed + element type | GATE 3 checkbox | GATE 1 checkbox | GATE 4B standalone | GATE 1 checkbox | GATE 3 checkbox | 6 frontmatter keys | **100** |

### Open research questions for Round 4

1. **C-14 declaration form (V-01 test result):** If CONFIRMED/NOT CONFIRMED declarations
   satisfy C-14, what is the minimum token required? Would a bare "YES/NO" completion work,
   or does the two-clause language need to appear in the item regardless of token form?
2. **C-16 granularity (V-02 vs others):** Does multi-gate frontmatter produce measurably
   different automation value, or is single gate1_isolation key sufficient for the primary
   pipeline use case? The scoring rubric awards a pass for any single key -- multi-gate
   exceeds the criterion but may not change the score.
3. **Phase 4B as a spec-level pattern:** V-04/V-05 R3's standalone calibration phase is a
   new structural pattern not present in any prior round. If calibration-as-phase becomes
   the standard, should GATE 4B be mandatory in the reference implementation, or is GATE 4's
   combined checkpoint acceptable?
4. **Element-type column vs Connector-surface sub-field as independent C-07 mechanisms:**
   V-03/V-05 R3 use both. A future variation could test each alone against C-07 to determine
   which is load-bearing and which is redundant.

```json
{"top_score_predicted": 100, "ceiling_variation": "V-05", "key_discriminator": "C-14 test: V-01 CONFIRMED/NOT CONFIRMED declaration form vs checkbox -- determines whether declaration syntax qualifies as equivalent confirmable gate item", "new_patterns": ["Multi-gate frontmatter manifest: all gate outcomes as queryable frontmatter fields, not just gate1_isolation_confirmed", "Standalone Phase 4B calibration section: calibration review as a first-class phase with its own gate, structurally separate from findings writing", "Domain columns + automation layer composability: Contract-element-type column and Connector-surface sub-field add to V-05 R2 without displacing any gate structure"]}
```
