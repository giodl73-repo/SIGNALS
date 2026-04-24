Written to `simulations/quest/variations/trace-contract-variations-R2-2026-03-14.md`.

---

## Round 2 Variations — Summary

**5 complete prompt bodies** across 3 single-axis + 1 single-axis-new + 1 combo variation:

| V | Axis | Key mechanism | Weakest criterion | Predicted score |
|---|------|---------------|------------------|-----------------|
| **V-01** | Lifecycle (minimal gate) | Single classification gate on diff section — C-11 minimum viable mechanism | C-12/C-13 absent | 87.5 |
| **V-02** | Role sequence + isolation | CONNECTORS EXPERT isolation attestation ("not just ordered after, but not consulted at all") | C-13 absent | 92.5 |
| **V-03** | Domain emphasis | Pre-printed "Contract element type" column + "Connector surface" findings sub-field | C-11/C-12/C-13 absent | 92.5 |
| **V-04** | Inertia framing | Three anti-pattern warnings before instructions; contrast frames C-09/C-11/C-13 implicitly | C-12 absent; C-13 mechanism is implicit | 87.5 |
| **V-05** | Lifecycle + format + isolation | V-03 R1 phases + V-01 columns + Gate 1 two-checkbox isolation | Structurally guarantees all 13 | **100** |

**Predicted ceiling:** V-05. The three structural guarantees (phase gates for C-11/C-13, pre-printed columns for C-02/C-03, explicit isolation checkbox for C-12) cover all 13 criteria without instruction-level compliance. No single gap from V-03 R1 or V-01 R1 survives the combination.

**Key discriminators for scoring:**

- **C-12 test:** Does V-02's role attestation ("actual was not consulted at all") satisfy C-12 as well as V-05's phase checkpoint? If yes, role-semantic isolation is equivalent.
- **C-07 test:** Does V-03's category column produce stronger domain coverage than V-02's role naming? If yes, domain columns earn a place in Round 3's synthesis.
- **C-13 test:** Does V-04's inertia framing ("justify a uniform severity distribution") pass C-13 without a named gate? If yes, contrast framing is a valid lighter-weight mechanism.

**Key design decision:** V-05 carries `gate1_isolation_confirmed: true` in its frontmatter — the machine-readable signal that GATE 1's isolation checkbox was confirmed, enabling downstream automation to distinguish isolation-confirmed runs from ordering-only runs.
n the diff section alone ("STATUS CLASSIFICATION ONLY
-- no root cause hypotheses in this section") is the minimum viable mechanism. If this single
gate achieves C-11, then V-03 R1's three other gates address C-12 and C-13 but are not
necessary for C-11 specifically. C-12 will likely fail (no isolation declaration) and C-13
will likely fail (no calibration checkpoint before findings). Essential and recommended
criteria should all pass -- the gate structure preserves C-01 via section ordering and
C-06 via labeled 10+/20+/30+ headers. Predicted score: 87.5 (5/5 essential, 3/3 recommended,
1/5 aspirational -- C-11 only).

```
You are running /trace:contract. Fill in this structured template.
All section headers are fixed. Do not reorder, rename, or remove any section.
The expected output is the contract. Any deviation is a finding.

---

## SETUP

Contract:   [Name the contract -- connector name + operation, OpenAPI path, typed action]
Input:      [The test input -- e.g., location="Seattle", recordId="12345"]
Spec:       [Spec document and section that defines the expected output]

Roles: Automate engineer, Connectors contract expert

---

## 10+ INPUT

[Describe the test input fully. For a connector operation: endpoint, parameters, auth context,
version. For a typed action: input payload. For a report spec: filter criteria, date range.
Enough detail that the operation could be reproduced exactly.]

---

## 20+ EXPECTED OUTPUT

[Write the complete expected output from the spec before capturing any actual output.
Do not reference what you know the actual output to be. Write what the contract says.]

Expected payload (from spec):
[Full expected schema / payload / report structure as the spec defines it]

Expected field table:
| Field path | Expected type | Expected value / constraint | Spec clause |
|------------|--------------|----------------------------|-------------|
| [field]    | [type]       | [value or constraint]      | [field name or section] |
[One row per spec-defined field. Nested paths use dot notation: forecast[].date]

---

## 30+ ACTUAL OUTPUT

[Capture the actual output from API documentation, connector definition, or test run.
Do not adjust to match the expected output above. Report what the runtime produces exactly.]

Actual payload captured:
[Full actual payload / schema / report structure]

Actual field table:
| Field path | Actual type | Actual value | Source |
|------------|------------|--------------|--------|
| [field]    | [type]     | [value]      | [API doc version / connector definition / test run] |
[All fields in actual response, including fields not in the expected table.]

Source: [API documentation version, connector definition date, or test run timestamp]

---

## DIFF -- CLASSIFICATION ONLY

[Complete this table for every field from either the expected or actual table above.
STATUS AND SEVERITY CLASSIFICATION ONLY IN THIS SECTION.
Do not write root cause hypotheses here. Do not write findings here.
Analysis comes after this section -- not during diff construction.]

### CLASSIFICATION GATE
[ ] Every field from the expected table appears in the diff
[ ] Every field from the actual table (including unexpected fields) appears in the diff
[ ] No root cause hypotheses or analysis text in this section -- classification only

Status values: MATCH | TYPE MISMATCH | VALUE MISMATCH | MISSING (absent from actual) | UNEXPECTED (absent from spec)

Severity (for mismatches only):
  breaking  = consumer cannot parse or use the response; feature does not work
  degraded  = consumer can proceed but with data loss, coercion, or incorrect values
  cosmetic  = no consumer impact; documentation or naming inconsistency only
For MATCH rows: severity = N/A

| Field path | Expected type/value | Actual type/value | Status | Severity | Spec Ref |
|------------|--------------------|--------------------|--------|----------|----------|
| [field]    | [type / value]     | [type / value]     | [status] | [breaking/degraded/cosmetic/N/A] | [spec field or section / N/A] |

Gate status: [PASS -- no analysis in diff section / NEEDS REVIEW -- remove hypotheses before proceeding]
Mismatch count: [N]

Do not write findings until the classification gate passes.

---

## FINDINGS

[Write one finding per mismatch row. MATCH rows do not get findings.
All four sub-fields are required for every finding.]

**Breaking findings (block the feature):**

F-[N] (breaking): [Field path] -- [What the mismatch is]
  Spec clause: [Exact spec field or section from diff table Spec Ref column]
  Root cause hypothesis: [Why the runtime deviates -- e.g., API provider renamed field
    in v2.1, type coercion removed from connector action, auth token response shape
    changed, field missing from action parameter mapping, schema from stale swagger]
  Next step: [Specific -- update OpenAPI definition / add coercion shim / regenerate
    connector schema / update Parse JSON schema in flow / file provider API bug]

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
  Next step: [Specific action or "Update spec to reflect current provider behavior."]

[Repeat for all cosmetic findings. If none: "No cosmetic findings."]

---

## SUMMARY

| Severity | Count |
|----------|-------|
| Breaking | [N]   |
| Degraded | [N]   |
| Cosmetic | [N]   |
| **Total mismatches** | **[N]** |

Feature status: [BLOCKED (any breaking) / DEGRADED (no breaking, degraded present) / CLEAN]

---

## CONTRACT DELTA

[List spec clauses requiring amendment. Suitable for direct input into spec update workflow.]

| Spec clause | Current definition | Required amendment | Finding ref |
|-------------|-------------------|--------------------|-------------|
| [field/section] | [current text] | [corrected text] | F-[N] |
[If no amendments: "Spec accurate. Amendments required on provider side or connector
definition only."]

---

Write artifact: simulations/trace/contract/{topic}-contract-{date}.md
Frontmatter: skill, topic, date, contract_name, input, source, feature_status,
breaking_count, degraded_count, cosmetic_count, mismatch_count, spec_ref.
```

---

## V-02: Role Sequence (Isolation Declaration)

**Axis:** Role sequence -- extends V-02 R1's role handoff gate with an explicit
negative-constraint isolation attestation. CONNECTORS EXPERT must not only declare that
expected output is complete but must attest that actual output was *not referenced* during
the expected phase -- not just ordered after it, but not consulted at all. AUTOMATE ENGINEER
must confirm classification is complete before writing root cause analysis.

**Hypothesis:** V-02 R1 enforced ordering (AUTOMATE cannot speak until CONNECTORS signs off)
but not isolation -- a model that can see both blocks may still contaminate expected-phase
writing with knowledge of actual behavior. Adding "actual output was not referenced during
this phase" as an explicit attestation in the CONNECTORS sign-off creates the negative-
constraint check that satisfies C-12. The AUTOMATE ENGINEER classification confirmation
before findings creates the separation that satisfies C-11 via role-semantic mechanism.
Tests whether role-semantic isolation is as strong as phase-structural isolation (V-05).
C-13 will likely fail -- no explicit calibration gate before findings finalized.
Predicted score: 92.5 (5/5 essential, 3/3 recommended, 2/5 aspirational -- C-11 and C-12).

```
You are running /trace:contract with two active roles:

  CONNECTORS EXPERT -- owns the contract definition and expected output. Writes the
    expected block from spec before any actual output is captured or referenced.
  AUTOMATE ENGINEER -- owns the runtime. Captures actual output. Leads finding analysis
    and owns next steps.

Role sequencing rules:
  1. CONNECTORS EXPERT completes and signs off the expected output block first.
  2. The sign-off must include an isolation attestation: actual output was not referenced
     during the expected phase -- not just ordered after, but not consulted at all.
  3. AUTOMATE ENGINEER does not write any output until the sign-off line appears.
  4. Before AUTOMATE ENGINEER begins root cause analysis, classification must be confirmed
     complete. No root cause hypotheses may appear in the diff section.

These are hard sequencing constraints. Do not blend phases or roles.

---

## SETUP

Contract:       [Connector name + operation, OpenAPI path, typed action, or report spec]
Input:          [Test input in full]
Spec document:  [Document and section defining the contract]

---

## CONNECTORS EXPERT: EXPECTED OUTPUT

[CONNECTORS EXPERT writes this section entirely from the contract spec.
Do not reference, preview, or consult actual runtime output while writing this section.
AUTOMATE ENGINEER does not contribute here.]

Reading [SPEC DOCUMENT], the contract for [CONTRACT] with input [INPUT] specifies:

Expected payload:
[Full expected response / schema as the spec defines it]

Expected field contract:
| Field path | Expected type | Expected value / constraint | Spec clause |
|------------|--------------|----------------------------|-------------|
| [field]    | [type]       | [value or constraint]      | [spec field name or section] |
[One row per spec-defined field. Nested fields use dot notation: forecast[].date]

---

CONNECTORS EXPERT isolation sign-off:
"Expected output written from [SPEC DOCUMENT]. [N] contract fields defined.
Actual output was not referenced during this phase -- not just ordered after,
but not consulted at all.
Gate clear -- AUTOMATE ENGINEER may proceed."

[AUTOMATE ENGINEER does not write below until this sign-off appears with the isolation
attestation. A sign-off that omits the non-reference declaration is incomplete.]

---

## AUTOMATE ENGINEER: ACTUAL OUTPUT

[AUTOMATE ENGINEER writes this section from runtime only -- API documentation, connector
test run, or last known actual response. Do not reference the expected block above while
writing field values. Capture what the runtime produces.]

Actual response from [CONTRACT] with input [INPUT]:

Actual payload:
[Full actual response as returned]

Actual fields observed:
| Field path | Actual type | Actual value | Source |
|------------|------------|--------------|--------|
| [field]    | [type]     | [value]      | [source] |
[All fields in actual, including unexpected fields not in the expected block.]

Source: [API doc version / connector definition date / test run timestamp]

---

## JOINT: DIFF TABLE -- CLASSIFICATION ONLY

[Both roles collaborate on classification. No root cause analysis in this section.
AUTOMATE ENGINEER confirms classification is complete before findings begin.]

Status values: MATCH | TYPE MISMATCH | VALUE MISMATCH | MISSING | UNEXPECTED

Severity:
  breaking  = AUTOMATE consumer cannot parse response; connector unusable
  degraded  = consumer proceeds but with incorrect, coerced, or incomplete data
  cosmetic  = no runtime impact; schema documentation stale
For MATCH rows: severity = N/A

| Field path | Expected (Connectors) | Actual (Automate) | Status | Severity | Spec Ref |
|------------|-----------------------|-------------------|--------|----------|----------|
| [field]    | [type / value]        | [type / value]    | [status] | [severity or N/A] | [spec clause / N/A] |

AUTOMATE ENGINEER classification confirmation:
"Diff complete. [N] mismatches classified. No root cause hypotheses were written during
diff construction -- classification only. Proceeding to findings analysis."

[Do not begin findings until this confirmation line appears.]

---

## AUTOMATE ENGINEER: FINDINGS

[AUTOMATE ENGINEER leads findings. CONNECTORS EXPERT provides spec clause verification.
One finding per mismatch row. MATCH rows do not get findings.
All four sub-fields required for every finding.]

**Breaking findings (consumer cannot use the response):**

F-[N] (breaking): [Field path] -- [What the mismatch is]
  Spec clause (Connectors): [Exact spec field or section from sign-off table]
  Root cause hypothesis (Automate): [Why the runtime deviates -- schema version, field
    rename, type coercion removal, missing action parameter mapping, auth response shape
    change, connector schema generated from stale swagger definition]
  Next step: [Specific -- update OpenAPI definition / add coercion shim / regenerate
    connector schema / update Parse JSON action schema / file provider API bug]

[Repeat for all breaking findings. If none: "No breaking findings."]

**Degraded findings (feature works, quality reduced):**

F-[N] (degraded): [Field path] -- [What the mismatch is]
  Spec clause (Connectors): [Spec field or section]
  Root cause hypothesis (Automate): [Why]
  Next step: [Specific action]

[Repeat for all degraded findings. If none: "No degraded findings."]

**Cosmetic findings (no consumer impact):**

F-[N] (cosmetic): [Field path] -- [What the mismatch is]
  Spec clause (Connectors): [Spec field or section]
  Root cause hypothesis (Automate): [Why]
  Next step: [Specific action or "Update OpenAPI definition to reflect current behavior."]

[Repeat for all cosmetic findings. If none: "No cosmetic findings."]

---

## SUMMARY

| Severity | Count |
|----------|-------|
| Breaking | [N]   |
| Degraded | [N]   |
| Cosmetic | [N]   |
| **Total mismatches** | **[N]** |

Feature status: [BLOCKED (any breaking) / DEGRADED (no breaking, degraded present) / CLEAN]

Contract delta (CONNECTORS EXPERT to action):
[List spec clauses requiring amendment. One line per finding requiring a spec change.]
- [Spec clause]: [Current wording] -> [Corrected wording]
[If none: "Spec accurate -- amendments needed on provider side or connector definition only."]

---

Write artifact: simulations/trace/contract/{topic}-contract-{date}.md
Frontmatter: skill, topic, date, contract_name, connectors_expert, automate_engineer,
isolation_attestation: true, feature_status, breaking_count, degraded_count, cosmetic_count.
```

---

## V-03: Output Format (Connector-Domain Category Column)

**Axis:** Output format -- addresses the R1 open question about domain emphasis axis (V-07
candidate). The expected and actual field tables include a pre-printed "Contract element type"
column that forces classification of each field by connector domain category before values
are compared. The diff table inherits the column. Findings include a pre-printed "Connector
surface" line naming where in the Automate/Connectors stack the mismatch manifests.

**Hypothesis:** C-07 requires findings to reference domain-specific contract elements
(connector schema, action/trigger payloads, auth handshake, field mappings, error shapes).
V-03 R1 failed C-07 because domain terms were absent from the template -- the model had to
generate them from role description alone. Pre-printing a "Contract element type" column
forces every field row to name its domain category. Findings that reference those rows
inherit the domain specificity automatically. Tests whether column-level domain anchoring
beats role-label anchoring for C-07 coverage. C-11/C-12/C-13 are not the primary focus;
this variation accepts lower aspirational scores to test the domain axis cleanly.
Predicted score: 92.5 (5/5 essential, 3/3 recommended, 2/5 aspirational -- C-09/C-10,
because the contract delta section is pre-printed and calibration can follow the format).

```
You are running /trace:contract. Fill in this structured template.
All section headers and column headers are fixed. Do not rename or remove any column.
Contract element types are defined below -- assign exactly one to every field row.

Contract element types (assign one per field):
  schema-field      = a typed data field in the response payload
  auth-handshake    = authentication or token field (bearer token, API key, scope, expiry)
  action-payload    = input or output of a Power Automate connector action parameter
  trigger-payload   = field in a connector trigger event payload
  error-shape       = field in an error response structure (code, message, detail, retry-after)
  metadata          = response envelope field not part of business payload (headers,
                      pagination cursors, correlation IDs, ETags, timestamps)

---

## SETUP

Contract:   [Connector name + operation, OpenAPI path, typed action, or trigger definition]
Input:      [The test input -- parameters, auth context, connector version]
Spec:       [Spec document and section defining the contract]

Roles: Automate engineer, Connectors contract expert

---

## 10+ INPUT

[Describe the test input fully: endpoint, parameters, authentication context, connector
definition version. Enough detail for exact reproduction.]

---

## 20+ EXPECTED OUTPUT

[Write the complete expected output from the spec before capturing actual output.
Do not reference what you know the runtime returns. Write what the contract requires.
Assign a contract element type to every field.]

Expected payload (from spec):
[Full expected response structure]

Expected field contract:
| Field path | Contract element type | Expected type | Expected value / constraint | Spec clause |
|------------|----------------------|--------------|----------------------------|-------------|
| [field]    | [schema-field / auth-handshake / action-payload / trigger-payload / error-shape / metadata] | [type] | [value or constraint] | [spec field or section] |
[One row per spec-defined field. Every row must have a contract element type assigned.]

---

## 30+ ACTUAL OUTPUT

[Capture actual from API docs, connector definition, or test run. Do not adjust to match
expected. Assign the same contract element type categories to actual fields.]

Actual payload captured:
[Full actual response structure]

Actual fields observed:
| Field path | Contract element type | Actual type | Actual value | Source |
|------------|----------------------|------------|--------------|--------|
| [field]    | [schema-field / auth-handshake / action-payload / trigger-payload / error-shape / metadata] | [type] | [value] | [source] |
[All fields in actual, including unexpected fields. Assign a contract element type
to every row -- for unexpected fields, choose the most appropriate category.]

Source: [API documentation version, connector definition date, or test run timestamp]

---

## DIFF TABLE

[Complete for every field from either table. All seven columns required for every row.
Contract element type is carried from the expected or actual table -- copy it here.
Do not leave Severity or Spec Ref blank on mismatch rows.]

Status values: MATCH | TYPE MISMATCH | VALUE MISMATCH | MISSING | UNEXPECTED

Severity (mismatches only):
  breaking  = consumer cannot parse response; connector non-functional at this surface
  degraded  = consumer proceeds with incorrect, coerced, or incomplete data
  cosmetic  = no runtime impact; documentation or naming inconsistency only

| Field path | Contract element type | Expected type/value | Actual type/value | Status | Severity | Spec Ref |
|------------|-----------------------|--------------------|--------------------|--------|----------|----------|
| [field]    | [element type]        | [type / value]     | [type / value]     | [status] | [breaking/degraded/cosmetic/N/A] | [spec field or section / N/A] |

---

## FINDINGS

[One finding per mismatch row. MATCH rows do not get findings.
All five sub-fields required for every finding.
"Connector surface" names where in the Automate/Connectors stack the fix lives.]

**Breaking findings:**

F-[N] (breaking): [Field path] -- [What the mismatch is]
  Contract element type: [from diff table]
  Connector surface: [Where the fix lives -- connector action definition / OpenAPI schema /
    trigger payload definition / auth token handler / error response parser /
    Parse JSON schema in Power Automate flow]
  Spec clause: [Exact spec field or section from diff table Spec Ref column]
  Root cause hypothesis: [Why the runtime deviates -- API provider renamed field in v2.1,
    type coercion removed from connector action, auth token response shape changed,
    field absent from action parameter definition, schema generated from outdated swagger]
  Next step: [Specific action at the named connector surface]

[Repeat for all breaking findings. If none: "No breaking findings."]

**Degraded findings:**

F-[N] (degraded): [Field path] -- [What the mismatch is]
  Contract element type: [element type]
  Connector surface: [Where the fix lives]
  Spec clause: [Spec field or section]
  Root cause hypothesis: [Why]
  Next step: [Specific action]

[Repeat for all degraded findings. If none: "No degraded findings."]

**Cosmetic findings:**

F-[N] (cosmetic): [Field path] -- [What the mismatch is]
  Contract element type: [element type]
  Connector surface: [Where the fix lives]
  Spec clause: [Spec field or section]
  Root cause hypothesis: [Why]
  Next step: [Specific action or "Update OpenAPI definition to reflect current behavior."]

[Repeat for all cosmetic findings. If none: "No cosmetic findings."]

---

## SUMMARY

| Severity | Count |
|----------|-------|
| Breaking | [N]   |
| Degraded | [N]   |
| Cosmetic | [N]   |
| **Total mismatches** | **[N]** |

Feature status: [BLOCKED / DEGRADED / CLEAN]

---

## CONTRACT DELTA

[List only spec clauses requiring amendment. One row per finding needing a spec change.]

| Spec clause | Contract element type | Current definition | Required amendment | Finding ref |
|-------------|----------------------|-------------------|--------------------|-------------|
| [field/section] | [element type] | [current] | [corrected] | F-[N] |
[If none: "Spec accurate. Amendments required on provider side or connector definition only."]

---

Write artifact: simulations/trace/contract/{topic}-contract-{date}.md
Frontmatter: skill, topic, date, contract_name, input, source, feature_status,
breaking_count, degraded_count, cosmetic_count, mismatch_count, spec_ref,
element_types_used: [list of contract element types that appeared in findings].
```

---

## V-04: Phrasing Register (Inertia Framing -- Anti-Pattern Warning)

**Axis:** Inertia framing -- opens with an explicit description of the three failure modes
this skill replaces. Each phase header echoes which anti-pattern it prevents. The contrast
between wrong and right behavior is named before each instruction block.

**Hypothesis:** Naming the wrong behavior before the correct behavior creates contrast that
primes the model to avoid the failure mode. Three anti-patterns are named: (1) expected-after-
actual contamination, (2) diff dump with no hypotheses, (3) severity inflation. A model that
has just read "the failure mode is marking everything breaking without justification" is primed
to calibrate severity (C-09). A model that has just read "the failure mode is writing findings
while reading the API docs" is primed to separate classification from analysis (C-11 via
contrast, not gate). Tests whether anti-pattern framing produces C-09/C-11 without structural
gate language. The hypothesis is that contrast framing is a weaker but distinct mechanism.
C-12 (isolation check) will fail -- no attestation mechanism. C-13 (calibration gate) may
partially pass if the anti-pattern warning at Step 3 functions as an implicit gate.
Predicted score: 87.5 (5/5 essential, 3/3 recommended, 1-2/5 aspirational).

```
You are running /trace:contract.

Before the steps: here are the three failure modes this skill prevents. Reading these
will help you understand why each step is structured the way it is.

**Failure mode 1: Expected-after-actual contamination.**
What usually happens: you open the API docs, see what fields come back, and write those
down as "expected." The spec is not consulted independently. Expected and actual are the
same source. The diff finds nothing because you already adjusted expected to match actual.
What this skill does instead: expected is written from the spec in isolation -- before
actual output is captured. The diff compares two genuinely independent sources.

**Failure mode 2: Diff dump with no hypotheses.**
What usually happens: a table of mismatches is produced with status labels (MISSING, TYPE
MISMATCH) but no analysis. The reader cannot tell whether a MISSING field is a schema
version lag, a renamed field, a removed feature, or a provider bug. Without a hypothesis,
the finding has no resolution path.
What this skill does instead: every mismatch has a root cause hypothesis -- a named reason
for why the deviation occurred -- before a next step is written.

**Failure mode 3: Severity inflation.**
What usually happens: everything is marked breaking to be safe. A cosmetic naming
inconsistency gets the same severity as a null response that crashes the flow. The feature
gets BLOCKED status when it would run fine.
What this skill does instead: severity is assigned by consumer impact. If all findings
fall into one severity level, that claim must be explicitly justified -- not accepted by default.

With those three failure modes in mind, here are the steps.

---

## SETUP

Contract:   [Name the contract -- connector name + operation, OpenAPI path, typed action]
Input:      [The test input]
Spec:       [Spec document and section defining the contract]

Roles: Automate engineer, Connectors contract expert

---

## STEP 1: WRITE EXPECTED OUTPUT [prevents failure mode 1]

[This step prevents contamination. Write the expected output from the spec only.
Do not reference the runtime, the API docs, or any knowledge of what the operation
currently returns. The spec is the only source. If the spec is ambiguous, make the
most literal reading and note the ambiguity -- do not resolve it by consulting runtime behavior.]

Expected payload (from spec):
[Full expected schema / payload as the spec defines it]

Expected field table:
| Field path | Expected type | Expected value / constraint | Spec clause |
|------------|--------------|----------------------------|-------------|
| [field]    | [type]       | [value or constraint]      | [spec field name or section] |
[One row per spec-defined field. Nested paths: forecast[].date]

---

## STEP 2: CAPTURE ACTUAL OUTPUT [independent of Step 1]

[Capture actual from API docs, connector definition, or test run. Do not adjust any
field to match Step 1. Unexpected fields (not in Step 1) belong here -- include them.]

Actual payload:
[Full actual response]

Actual field table:
| Field path | Actual type | Actual value | Source |
|------------|------------|--------------|--------|
| [field]    | [type]     | [value]      | [source] |

Source: [API doc version / connector definition / test run timestamp]

---

## STEP 3: CLASSIFY -- STATUS AND SEVERITY ONLY [prevents failure mode 2, classification phase]

[This step is classification only. Do not write root cause hypotheses here.
Do not write findings here. Assign status and severity for every field from Step 1 or Step 2.

The reason for this separation: writing a hypothesis while building the diff anchors the
hypothesis to the first plausible explanation before the full mismatch pattern is visible.
Complete classification first. Analysis happens in Step 4.]

Status values: MATCH | TYPE MISMATCH | VALUE MISMATCH | MISSING | UNEXPECTED

Severity:
  breaking  = consumer cannot parse the response; feature does not work
  degraded  = consumer proceeds but with wrong or incomplete data
  cosmetic  = no runtime impact; documentation drift only

| Field path | Step 1 expected | Step 2 actual | Status | Severity | Spec Ref |
|------------|----------------|---------------|--------|----------|----------|
| [field]    | [type / value] | [type / value] | [status] | [severity or N/A] | [spec clause or N/A] |

Mismatch count: [N] fields did not match.

---

## STEP 4: WRITE FINDINGS [prevents failure mode 2 and 3]

[Now write root cause hypotheses. Every mismatch from Step 3 gets a finding.
Every finding must have a hypothesis -- not an observation. "Field is missing" is an
observation. "Field was renamed in v2.1 of the provider API" is a hypothesis.

Before grouping findings by severity, check the distribution. If all mismatches are the
same severity, justify that distribution explicitly. A uniform distribution is valid only
when the mismatches truly all impact the consumer the same way. The claim "all breaking"
or "all cosmetic" must be earned, not assumed. If the distribution is not uniform, that
is expected -- name the reasons for the differences.]

**Breaking findings (consumer cannot use the response):**

F-[N] (breaking): [Field path] -- [What the mismatch is]
  Spec clause: [From Step 1 table -- field name or spec section]
  Root cause hypothesis: [Why this deviation occurred -- e.g., API provider renamed field
    in v2.1, type coercion removed from connector action, auth token shape changed,
    field missing from action parameter mapping, schema from stale swagger]
  Next step: [Specific action -- update OpenAPI definition / add coercion shim /
    regenerate connector schema / update Parse JSON schema / file provider API bug]

[Repeat for all breaking findings. If none: "No breaking findings."]

**Degraded findings (feature works, data quality reduced):**

F-[N] (degraded): [Field path] -- [What the mismatch is]
  Spec clause: [Spec field or section]
  Root cause hypothesis: [Why]
  Next step: [Specific action]

[Repeat for all degraded findings. If none: "No degraded findings."]

**Cosmetic findings (no consumer impact):**

F-[N] (cosmetic): [Field path] -- [What the mismatch is]
  Spec clause: [Spec field or section]
  Root cause hypothesis: [Why]
  Next step: [Specific action or "Update spec to document current behavior."]

[Repeat for all cosmetic findings. If none: "No cosmetic findings."]

---

## STEP 5: SUMMARY AND CONTRACT DELTA

Finding summary:
| Severity | Count |
|----------|-------|
| Breaking | [N]   |
| Degraded | [N]   |
| Cosmetic | [N]   |

Feature status: [BLOCKED (any breaking) / DEGRADED (no breaking, degraded present) / CLEAN]

Contract delta (spec clauses requiring amendment):
1. [Spec clause / field]: [Current definition] -> [Required amendment]
[If none: "Spec accurate. Fix is on provider or connector definition side."]

---

Write artifact: simulations/trace/contract/{topic}-contract-{date}.md
Frontmatter: skill, topic, date, contract_name, input, source, feature_status,
breaking_count, degraded_count, cosmetic_count, mismatch_count.
```

---

## V-05: Full Synthesis (V-03 R1 Phases + V-01 Columns + C-12 Isolation)

**Axes:** V-03 R1 four-phase lifecycle (proven at 100 for C-11/C-13) + V-01 R1 six-column
pre-printed diff table (structural guarantee for C-02/C-03) + explicit negative-constraint
isolation declaration at GATE 1 (closes the C-12 gap from V-03 R1).

**Hypothesis:** V-03 R1 scored 100 but the v2 rubric introduces C-12 which distinguishes
isolation from ordering. V-03 R1's GATE 1 check "[ ] No actual output has been referenced
in this phase" may satisfy C-12 as written, but the rubric explicitly says artifacts that
"confirm ordering but not isolation do not pass." Adding a second checkbox "[ ] Actual output
was not consulted at all -- not just ordered after" makes the negative-constraint framing
unambiguous. Pairing this with V-01's pre-printed six-column diff table (Severity and Spec Ref
as mandatory columns) removes C-02/C-03 as failure modes structurally -- no row can exist
without both filled in. The four phases retain C-11 (Gate 3: no hypotheses during diff) and
C-13 (Gate 4: calibration review before finalization). This is the designed-for-100 candidate
on the v2 rubric: structural guarantees cover all five essential, all three recommended, and
all five aspirational criteria. Predicted score: 100.

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

Capture the actual output by running the operation from API documentation, connector
definition, or last known response. Do not adjust any field or value to match Phase 1.
Report what the runtime produces exactly, including unexpected fields not in the spec.

Actual payload captured:
[Full actual response as returned by the operation]

Actual field list:
| Field path | Actual type | Actual value | Source |
|------------|------------|--------------|--------|
| [field]    | [type]     | [value]      | [source] |
[All fields in actual response, including unexpected fields not in Phase 1.]

Source: [API documentation version, connector definition date, or test run timestamp]

### GATE 2: ACTUAL COMPLETE
[ ] Actual output is captured without reference to Phase 1 expected values
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
gate1_isolation_confirmed: true.
```

---

## Round 2 Design Notes

### Axis selection rationale

Round 2 targets four research questions from Round 1's open list:

**Q1 -- C-11 minimum viable gate (V-01):** Can a single classification gate on the diff
section achieve C-11 without V-03 R1's full four-phase apparatus? The lightweight version
tests whether the gate language is the active ingredient, or whether the full phase structure
is necessary. If V-01 achieves C-11, the minimum viable mechanism is confirmed.

**Q2 -- C-12 via role semantics (V-02):** Does an isolation attestation in the CONNECTORS
EXPERT sign-off achieve C-12? V-02 R1 enforced ordering but not isolation. Adding "actual
output was not referenced -- not just ordered after, but not consulted at all" tests whether
role-semantic isolation is equivalent to phase-structural isolation. If V-02 R2 passes C-12
and V-01 does not, it confirms isolation declaration is required regardless of mechanism form.

**Q3 -- Domain emphasis via category column (V-03):** Does pre-printing a "Contract element
type" column (schema-field / auth-handshake / action-payload / trigger-payload / error-shape /
metadata) improve C-07 beyond role-label anchoring? V-03 R1 was the only R1 variation to
fail C-07. This tests whether structural domain column anchoring addresses that gap.

**Q4 -- Inertia framing as C-09/C-11 mechanism (V-04):** Does naming three anti-patterns
before instructions produce calibrated severity (C-09) and classification separation (C-11)
without structural gates? If yes, anti-pattern framing is a viable lighter-weight alternative
for C-09/C-11. If no, gates are necessary and framing is insufficient.

**V-05 (synthesis):** V-03 R1's four phases + V-01's pre-printed six-column table + explicit
GATE 1 isolation declaration. Designed to hit all 13 criteria in the v2 rubric.

### Predicted rubric performance (v2 rubric, 13 criteria)

| V | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | Score |
|---|------|------|------|------|------|------|------|------|------|------|------|------|------|-------|
| V-01 | section | column | column | sub-field | section | labeled | absent | sub-field | absent | pre-printed | gate | absent | absent | 87.5 |
| V-02 | role gate | column | diff table | sub-field | section | implicit | named roles | sub-field | absent | pre-printed | role confirm | role attestation | absent | 92.5 |
| V-03 | section | column | column | sub-field | section | labeled | category column | connector surface | absent | pre-printed | absent | absent | absent | 92.5 |
| V-04 | instruction | instruction | contrast frame | sub-field | section | step labels | role mention | sub-field | contrast frame | step 5 | contrast frame | absent | contrast frame | 87.5 |
| V-05 | phase gate | pre-printed | pre-printed | sub-field | section | phase labels | named roles | sub-field | gate 4 | pre-printed | gate 3 | gate 1 explicit | gate 4 | 100 |

### Key discriminators

**C-12 (isolation vs. ordering):** Only V-02 and V-05 attempt C-12. V-02 uses a role
attestation in CONNECTORS EXPERT sign-off. V-05 uses Gate 1 with two explicit checkboxes --
one for ordering, one for isolation. If V-02's role attestation passes C-12, role-semantic
isolation is established as equivalent to phase-structural isolation for this criterion.

**C-11 (classification gate):** V-01 uses a lightweight single gate. V-02 uses a role
confirmation line (AUTOMATE ENGINEER classification confirmation). V-05 uses Gate 3 with
an explicit "no hypotheses" checkbox. Comparing V-01 and V-02 against V-05 reveals whether
the mechanism form (gate label vs. role confirmation vs. phase checkpoint) matters for C-11.

**C-13 (calibration gate):** Only V-05 has an explicit Gate 4 calibration review with a
checkbox. V-04's anti-pattern warning at Step 4 is an implicit calibration prompt. If V-04
passes C-13, implicit contrast framing is sufficient. If it fails, only an explicit gate
(named checkpoint, checkbox, or gate status line) satisfies C-13.

**C-07 (domain engagement):** V-03's category column is the clearest test. If V-03 outscores
V-02 on C-07 despite both having similar essential coverage, domain column pre-printing
earns a place in the Round 3 synthesis alongside V-05's phase structure.

### Open research questions for Round 3

1. If V-02's role attestation passes C-12 but V-01 fails, what is the minimum declaration
   form needed? Must it be a named attestation line, or is any first-person "not consulted"
   language sufficient?
2. Does V-03's category column improve C-07, and if so, should it be integrated into V-05
   as V-06 (full synthesis + domain columns) in Round 3?
3. If V-04's inertia framing passes C-09/C-11 but fails C-12/C-13, what is the hybrid
   between inertia framing (V-04) and explicit gates (V-05) that achieves all five
   aspirational criteria with the least template complexity?
4. V-06 candidate (not yet tested): calibration checkpoint as a standalone section between
   findings and the summary -- separates Gate 4 into two parts (findings complete check,
   then calibration review) to test whether the calibration gate is more reliably triggered
   when it appears as its own named section.
