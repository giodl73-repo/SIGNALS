Written to `simulations/quest/variations/trace-contract-variations-R1-2026-03-14.md`.

---

## Round 1 Variations — Summary

**5 complete prompt bodies** across 3 single-axis + 2 combo variations:

| V | Axis | Key mechanism | Weakest criterion |
|---|------|---------------|------------------|
| **V-01** | Output format | Pre-printed `Severity` + `Spec Ref` columns in the diff table — C-02/C-03 structurally unavoidable | C-01 (instruction-only, no gate) |
| **V-02** | Role sequence | CONNECTORS EXPERT owns expected block + sign-off gate before AUTOMATE ENGINEER can speak — C-01 structurally unavoidable | C-06 (no 10+/20+/30+ labels) |
| **V-03** | Lifecycle emphasis | Four named phases with explicit GATE 1–4 checkpoints — C-01 enforced by physical phase separation | C-07 (domain terms not named in template) |
| **V-04** | Phrasing register | Conversational "you" voice, step-by-step numbered instructions, no formal headers | C-06 likely fails (no labeled three-directory structure); most failure surface overall |
| **V-05** | Format + role sequence | V-01 columns + V-02 role gate — covers C-01/C-02/C-03 structurally; pre-printed Root Cause covers C-04; section separation covers C-05 | Strongest essential coverage |

**Predicted ceiling:** V-05. The two structural guarantees (column anchoring + role gate) cover all five essential criteria without instruction-level compliance. V-03 is the closest competitor; its phase gates are equally structural for C-01 but the domain column (C-07) is absent.

**Key open question for Round 2:** Does V-04 (conversational register) pass C-06 despite no labeled headers, because the numbered steps imply the 10+/20+/30+ phasing? If yes, phrasing register has less rubric impact than predicted.
s the closest competitor (phase gates are also structural).
V-04 is the floor test: does the imperative voice produce enough structure on its own?

---

## V-01: Output Format — Pre-Printed Comparison Table

**Axis:** Output format -- the field-by-field comparison is a pre-printed table with
mandatory columns including `Severity` and `Spec Ref`. The findings section has pre-printed
sub-fields for Root Cause and Next Step.
**Hypothesis:** When Severity and Spec Ref are column headers in the comparison table, the
model cannot produce a row without filling both cells. C-02 and C-03 become structurally
unavoidable. The findings section pre-printing Root Cause prevents the "diff dump with no
analysis" failure mode. Tests whether column-level structural anchoring beats instruction-level
anchoring for these two criteria.

```
You are running /trace:contract. Fill in this structured template.
All section headers and column headers are fixed. Do not reorder, rename, or remove any
header, column, or template fragment.

---

## SETUP

Contract:   [Name the contract -- e.g., connector name + operation, OpenAPI path, typed action]
Input:      [The test input being used -- e.g., location="Seattle", recordId="12345"]
Spec ref:   [Document and section that defines the expected output -- e.g., signal-trace-2026-03-14.md#trace-contract]

Roles active: Automate engineer, Connectors contract expert

---

## 10+ INPUT

[Describe the test input fully. For a connector operation: endpoint, parameters, auth context,
version. For a typed action: input payload. For a report spec: filter criteria, date range.
Enough detail that the operation could be reproduced exactly.]

---

## 20+ EXPECTED OUTPUT

[Write the complete expected output FROM THE SPEC before capturing any actual output.
Do not reference what you know the actual output to be. Write what the contract says it should be.]

Expected output (from spec):
[Full expected payload, schema, or report structure]

Expected field summary:
| Field path | Expected type | Expected value / constraint |
|------------|--------------|----------------------------|
| [field]    | [type]       | [value or constraint]       |
| [field]    | [type]       | [value or constraint]       |
[Add rows for every field the spec defines. Nested fields use dot notation: forecast[].date]

---

## 30+ ACTUAL OUTPUT

[Capture the actual output by running the operation mentally from the contract definition,
API documentation, or last known behavior. Do not adjust to match expectations.]

Actual output captured:
[Full actual payload, schema, or report structure]

Actual field summary:
| Field path | Actual type | Actual value |
|------------|------------|--------------|
| [field]    | [type]     | [value]      |
| [field]    | [type]     | [value]      |
[Add all fields present in actual output, including unexpected fields not in the spec.]

---

## DIFF TABLE

[Complete this table for every field that appears in either the expected or actual summary above.
All five columns are required for every row -- do not leave any cell blank or write "N/A" without
explanation. Status values: MATCH / TYPE MISMATCH / VALUE MISMATCH / MISSING / UNEXPECTED.]

| Field path | Expected type | Actual type | Status | Severity | Spec Ref |
|------------|--------------|-------------|--------|----------|----------|
| [field]    | [type]       | [type]      | [status] | breaking / degraded / cosmetic | [spec section or field name] |
| [field]    | [type]       | [type]      | [status] | breaking / degraded / cosmetic | [spec section or field name] |

[Severity guidance -- fill in, do not omit the column:
  breaking  = consumer cannot parse or use the response; feature does not work
  degraded  = consumer can proceed but with data loss, coercion, or incorrect values
  cosmetic  = no consumer impact; documentation or naming inconsistency only
For MATCH rows: severity = N/A (write "N/A" with no explanation needed)]

[Spec Ref guidance -- fill in, do not omit the column:
  For MATCH rows: spec ref = N/A
  For any mismatch: cite the specific field name, section heading, or clause number in the spec.
  "See spec" or "spec" alone does not qualify -- name the field or section.]

---

## FINDINGS

[Write one finding entry per mismatch row. MATCH rows do not need a finding.
All three sub-fields are required for every finding -- do not omit any line.]

**Breaking findings (block the feature):**

F-[N]: [Field path] -- [One-sentence description of the mismatch]
  Root cause hypothesis: [Why did this deviation occur? e.g., field renamed in v2.1,
    type coercion removed in recent API update, schema not regenerated after backend change]
  Next step: [Specific action -- e.g., update OpenAPI definition field name,
    add backwards-compat shim, regenerate schema from provider swagger]

[Repeat for each breaking finding. If none: write "None."]

**Degraded findings (feature works, quality reduced):**

F-[N]: [Field path] -- [One-sentence description of the mismatch]
  Root cause hypothesis: [Why did this deviation occur?]
  Next step: [Specific action -- name what to check or change]

[Repeat for each degraded finding. If none: write "None."]

**Cosmetic findings (no consumer impact):**

F-[N]: [Field path] -- [One-sentence description of the mismatch]
  Root cause hypothesis: [Why did this deviation occur?]
  Next step: [Specific action or "Update OpenAPI definition to reflect current behavior."]

[Repeat for each cosmetic finding. If none: write "None."]

---

## FINDING SUMMARY

| Severity | Count |
|----------|-------|
| Breaking | [N]   |
| Degraded | [N]   |
| Cosmetic | [N]   |
| **Total** | **[N]** |

Feature status: [BLOCKED (any breaking) / DEGRADED (degraded only) / CLEAN (cosmetic only or no findings)]

---

## CONTRACT DELTA

[List only the spec clauses that need amendment based on the findings above.
Suitable for direct input into a spec update workflow. One line per clause.]

Spec amendments needed:
1. [Spec section / field]: [What the clause currently says vs. what it should say]
2. [Spec section / field]: [What the clause currently says vs. what it should say]
[If no amendments needed: write "No amendments needed -- spec matches actual behavior."]

---

Write artifact: simulations/trace/contract/{topic}-contract-{date}.md
Frontmatter: skill, topic, date, contract_name, input, feature_status, breaking_count,
degraded_count, cosmetic_count, spec_ref.
```

---

## V-02: Role Sequence — Connectors Writes Expected, Automate Owns Findings

**Axis:** Role sequence -- Connectors contract expert owns and writes the expected output
block before the Automate engineer captures actual. Each role has an explicit ownership
statement and a handoff gate between them.
**Hypothesis:** Naming which role writes the expected block (Connectors, who knows the schema
contract) and which role runs the actual (Automate, who knows what the runtime produces)
makes the expected-before-actual discipline feel natural rather than arbitrary. The handoff
gate is a structural barrier: Automate cannot begin until Connectors has signed off. C-01
failure requires overriding a named gate, not just ignoring a text instruction. Tests whether
role-ownership semantics strengthen the expected-first guarantee more than format alone.

```
You are running /trace:contract with two active roles:

  CONNECTORS EXPERT -- owns the contract definition and expected output. Writes the
    expected block from spec before any actual output is captured.
  AUTOMATE ENGINEER -- owns the runtime. Captures actual output and leads finding analysis.

Role handoff rule: AUTOMATE ENGINEER does not write or speak until CONNECTORS EXPERT has
completed and closed the expected output block. This is a hard gate -- do not blend phases.

---

## SETUP

Contract:   [Name the contract -- connector name + operation, OpenAPI path, typed action]
Input:      [The test input being used]
Spec:       [Document and section that defines the expected schema]

---

## CONNECTORS EXPERT: EXPECTED OUTPUT

[CONNECTORS EXPERT writes this section entirely from the contract spec, before any actual
output is referenced. Do not let AUTOMATE ENGINEER speak here.]

From spec [SPEC REFERENCE], the contract for [CONTRACT NAME] with input [INPUT] should return:

Expected payload:
[Full expected schema / payload written from spec]

Field-by-field contract:
| Field path | Type | Constraint / expected value | Spec clause |
|------------|------|-----------------------------|-------------|
| [field]    | [type] | [value or constraint]     | [section or field name in spec] |
| [field]    | [type] | [value or constraint]     | [section or field name in spec] |
[Every field the spec defines. Nested fields use dot notation.]

CONNECTORS EXPERT sign-off: "Expected output written from [SPEC]. [N] fields defined.
Handing off to AUTOMATE ENGINEER."

[Gate: AUTOMATE ENGINEER does not proceed until this sign-off line is present.]

---

## AUTOMATE ENGINEER: ACTUAL OUTPUT

[AUTOMATE ENGINEER writes this section from the runtime -- API documentation, connector
test run, or last known actual response. Do not refer back to the expected block while writing.]

Actual response from [CONTRACT NAME] with input [INPUT]:

Actual payload:
[Full actual response as returned]

Actual fields observed:
| Field path | Type | Observed value |
|------------|------|----------------|
| [field]    | [type] | [value]      |
| [field]    | [type] | [value]      |
[Include all fields present in the actual response, including unexpected ones.]

---

## JOINT: DIFF AND CLASSIFICATION

[Both roles collaborate on this section. CONNECTORS EXPERT flags schema violations.
AUTOMATE ENGINEER flags runtime deviations.]

| Field path | Expected (Connectors) | Actual (Automate) | Status | Severity |
|------------|-----------------------|-------------------|--------|----------|
| [field]    | [type / value]        | [type / value]    | MATCH / MISMATCH / MISSING / UNEXPECTED | breaking / degraded / cosmetic / N/A |

Severity definitions:
  breaking  = AUTOMATE flow cannot parse response; connector unusable in this state
  degraded  = flow runs but produces incorrect or incomplete data
  cosmetic  = no runtime impact; schema documentation out of date

---

## AUTOMATE ENGINEER: FINDINGS

[AUTOMATE ENGINEER leads findings. CONNECTORS EXPERT provides spec clause references
for each finding. Both fields required for every finding.]

F-[N] ([SEVERITY]): [Field path] -- [What the mismatch is]
  Spec clause (Connectors): [Exact spec field name or section that defines expected behavior]
  Root cause hypothesis (Automate): [Why the runtime deviates -- schema version, rename,
    type coercion, missing field mapping, auth response shape change]
  Next step: [Specific action -- update OpenAPI definition / add shim / file connector bug /
    regenerate schema / update Parse JSON schema in flow]

[Repeat for every mismatch in the diff table. MATCH rows do not need a finding.]

---

## SUMMARY

| Severity | Count |
|----------|-------|
| Breaking | [N]   |
| Degraded | [N]   |
| Cosmetic | [N]   |

Feature status: [BLOCKED / DEGRADED / CLEAN]

Contract delta (CONNECTORS EXPERT to action):
[List spec clauses that need amendment. One line per finding that requires a spec change.]
- [Spec clause]: [Current wording] -> [Corrected wording]
[If none: "Spec is accurate -- amendments needed on provider side only."]

---

Write artifact: simulations/trace/contract/{topic}-contract-{date}.md
Frontmatter: skill, topic, date, contract_name, connectors_expert, automate_engineer,
feature_status, breaking_count, degraded_count, cosmetic_count.
```

---

## V-03: Lifecycle Emphasis — Four Hard Phases with Named Gates

**Axis:** Lifecycle emphasis -- the skill is divided into four explicitly named phases with
hard gate checks at each boundary. Advancing to the next phase requires the gate condition to
be met. The phases are: PHASE 1 (write expected), PHASE 2 (capture actual), PHASE 3 (diff),
PHASE 4 (findings). Each gate is printed as a named checkpoint.
**Hypothesis:** Phase-blending is the most common trace-contract failure: writing findings
while capturing actual, or referencing actual while writing expected. Named gates with
pass/fail conditions prevent blending by making the phase boundary explicit and checkable.
C-01 (expected before actual) is guaranteed by PHASE 1 ending with a gate that must pass
before PHASE 2 begins. Tests whether gate language eliminates blending more reliably than
column ordering or role ownership.

```
You are running /trace:contract. This skill runs in four sequential phases.
Complete each phase fully before advancing. Each phase ends with a named gate.
If a gate does not pass, complete the phase before proceeding -- do not skip gates.

---

## SETUP

Contract:   [Name the contract being validated]
Input:      [The test input]
Spec:       [Spec document and section defining the contract]
Roles:      Automate engineer, Connectors contract expert

---

## PHASE 1: EXPECTED OUTPUT

Write the complete expected output from the contract spec. Do not reference what you
know the actual output to be. This is the contract. If the spec is ambiguous, note it
but make a determination based on the most literal reading.

Expected output (from spec):
[Full expected payload as the spec defines it]

Expected field list:
| Field path | Expected type | Expected value / constraint | Spec clause |
|------------|--------------|----------------------------|-------------|
| [field]    | [type]       | [value or constraint]      | [field name or section] |
[One row per field the spec defines. Nested paths use dot notation.]

### GATE 1: EXPECTED COMPLETE
[ ] All fields from the spec are listed in the expected field table
[ ] Each row has a spec clause reference (not "see spec" -- name the field or section)
[ ] No actual output has been referenced in this phase

Status: [PASS / NEEDS COMPLETION]
Do not begin PHASE 2 until GATE 1 passes.

---

## PHASE 2: ACTUAL OUTPUT

Capture the actual output by running the operation from API documentation, connector
definition, or last known response. Do not adjust to match Phase 1 expectations.

Actual output captured:
[Full actual payload as returned by the operation]

Actual field list:
| Field path | Actual type | Actual value |
|------------|------------|--------------|
| [field]    | [type]     | [value]      |
[All fields present in actual response, including unexpected ones not in the spec.]

### GATE 2: ACTUAL COMPLETE
[ ] Actual output is captured without reference to Phase 1 expected values
[ ] All fields in the actual response are listed, including unexpected fields
[ ] Source of actual output is identified (API doc version, connector definition date, test run)

Source: [API documentation version / connector definition / test run date]
Status: [PASS / NEEDS COMPLETION]
Do not begin PHASE 3 until GATE 2 passes.

---

## PHASE 3: DIFF

Compare Phase 1 (expected) to Phase 2 (actual) field by field. Every field from either
phase must appear in this table. Do not add findings yet -- classification only in this phase.

Status values: MATCH | TYPE MISMATCH | VALUE MISMATCH | MISSING (in actual) | UNEXPECTED (in actual)

| Field path | Expected type/value | Actual type/value | Status |
|------------|--------------------|--------------------|--------|
| [field]    | [type / value]     | [type / value]     | [status] |
[One row per field from either Phase 1 or Phase 2.]

### GATE 3: DIFF COMPLETE
[ ] Every Phase 1 field appears in the diff table
[ ] Every Phase 2 field (including unexpected) appears in the diff table
[ ] No finding analysis or root cause hypotheses in this section -- classification only

Mismatch count: [N] (rows that are not MATCH)
Status: [PASS / NEEDS COMPLETION]
Do not begin PHASE 4 until GATE 3 passes.

---

## PHASE 4: FINDINGS

Write one finding for every mismatch row from Phase 3. MATCH rows do not get findings.
All four sub-fields are required for every finding.

**Breaking findings (consumer cannot use the response):**

F-[N]: [Field path] ([STATUS from Phase 3])
  Spec clause: [Phase 1 spec clause for this field]
  Severity: breaking
  Root cause hypothesis: [Why -- schema version, field rename, type handling change,
    missing mapping, auth response shape, provider API change]
  Next step: [Specific -- update OpenAPI definition / add type coercion shim /
    regenerate connector schema / update Parse JSON action / file provider bug]

[Repeat for all breaking mismatches. If none: "No breaking findings."]

**Degraded findings (consumer proceeds with reduced quality):**

F-[N]: [Field path] ([STATUS from Phase 3])
  Spec clause: [Phase 1 spec clause]
  Severity: degraded
  Root cause hypothesis: [Why]
  Next step: [Specific action]

[Repeat for all degraded mismatches. If none: "No degraded findings."]

**Cosmetic findings (no consumer impact):**

F-[N]: [Field path] ([STATUS from Phase 3])
  Spec clause: [Phase 1 spec clause]
  Severity: cosmetic
  Root cause hypothesis: [Why]
  Next step: [Specific action or "Update spec to reflect current behavior."]

[Repeat for all cosmetic mismatches. If none: "No cosmetic findings."]

### GATE 4: FINDINGS COMPLETE
[ ] Every mismatch from Phase 3 has a finding entry
[ ] No finding is missing root cause hypothesis or next step
[ ] Severity distribution reviewed -- not all one level unless explicitly justified

Feature status: [BLOCKED (any breaking) / DEGRADED / CLEAN]

---

## CONTRACT DELTA

[For spec update workflow. List only clauses that need amendment.]

| Spec clause | Current definition | Required amendment |
|-------------|-------------------|--------------------|
| [field/section] | [current] | [corrected] |
[If no amendments: "Spec accurate. Amendments needed on provider side or in connector definition."]

---

Write artifact: simulations/trace/contract/{topic}-contract-{date}.md
Frontmatter: skill, topic, date, contract_name, input, source, feature_status,
breaking_count, degraded_count, cosmetic_count, mismatch_count.
```

---

## V-04: Phrasing Register — Conversational Imperative

**Axis:** Phrasing register -- no formal section headers in the body; the skill is written
as direct imperative instructions in "you" voice. The model follows a sequence of numbered
steps. Structure emerges from procedure, not from pre-printed scaffold.
**Hypothesis:** Some developers find formal template headers ("## 20+ EXPECTED OUTPUT") stiff
and ignore or skim them. Conversational imperative voice ("Before you look at what the API
actually returns, write down what the contract says it should return") puts the reasoning in
plain language. C-01 compliance depends on the instruction sequence being followed, not on
section ordering. Tests whether procedural register can produce equivalent rubric coverage
without template scaffolding, and whether it scores lower on C-06 (three-directory structure
explicit) due to the absence of labeled headers.

```
You are running /trace:contract.

Here is how this works: you are checking whether what an API, connector, or typed action
actually returns matches what its spec says it should return. The expected output is the
contract. Any deviation is a finding.

Do these steps in order. Do not skip steps. Do not blend steps.

---

**Step 1 -- Name the contract.**

Tell me: what are you testing? Give me the connector name and operation (or API path, or
typed action), the test input you are using, and the spec document that defines what the
output should look like. Write it out:

  Contract:  [e.g., WeatherEnrichment connector, GetForecast operation]
  Input:     [e.g., location="Seattle"]
  Spec:      [e.g., signal-trace-2026-03-14.md section trace:contract, or OpenAPI v2.3]

Roles running: Automate engineer + Connectors contract expert.

---

**Step 2 -- Write what you expect. Do this before you look at what actually comes back.**

Open the spec. Read what this operation is supposed to return. Write it out here as a
field-by-field list. For each field: name, type, what value or constraint the spec says.
Do not write what you know the actual response contains. Write what the contract says.

| Field | Expected type | Expected value or constraint | Where in the spec |
|-------|--------------|------------------------------|------------------|
| [field] | [type] | [value or rule] | [field name or section] |

If the spec is silent on a field, say so. If the spec is ambiguous, make the most literal
reading and note it.

---

**Step 3 -- Now capture what actually comes back.**

Run the operation (mentally, from API docs, or from a real test run). Write down every field
in the actual response -- including fields that are not in your Step 2 list. Be exact about
types and values. Do not adjust what you observed to match what you expected.

| Field | Actual type | Actual value | Source |
|-------|------------|--------------|--------|
| [field] | [type] | [value] | [API doc version / test run] |

Source of actual output: [API documentation version, connector definition date, or test run timestamp]

---

**Step 4 -- Do the diff.**

Go through both tables. For every field that appears in either Step 2 or Step 3, write a
comparison row. Status is: MATCH, TYPE MISMATCH, VALUE MISMATCH, MISSING (in actual), or
UNEXPECTED (not in spec). Do not write findings yet -- just the comparison.

| Field | Expected | Actual | Status |
|-------|----------|--------|--------|
| [field] | [type/value] | [type/value] | [status] |

Count your mismatches before moving on: [N] fields did not match.

---

**Step 5 -- For each mismatch, write a finding.**

For every row in Step 4 that is not MATCH, write a finding. Use this format:

F-[N]: [field name] is [STATUS].
  Severity: [breaking / degraded / cosmetic]
    breaking = the Automate consumer cannot parse the response; flow breaks
    degraded = flow runs but with wrong or missing data
    cosmetic = no runtime impact, just documentation drift
  Spec says: [The specific spec clause, field name, or section that defines expected behavior.
    Do not write "see spec" -- name the field or section.]
  Why this probably happened: [Your root cause hypothesis. e.g., "API provider renamed the
    field in v2.1", "type coercion was removed", "schema not regenerated after backend change",
    "field missing from connector action parameter mapping"]
  Fix: [Specific next action. e.g., "Update OpenAPI definition to rename temperature back",
    "Add a Select action in the flow to coerce humidity string to number",
    "Regenerate the connector schema from the updated swagger endpoint"]

Write "No findings." for severity levels that have no mismatches.

Group your findings by severity: breaking first, then degraded, then cosmetic.

---

**Step 6 -- Summary and contract delta.**

Write a one-line feature status:

  Finding summary: [N] breaking, [N] degraded, [N] cosmetic
  Feature status: [BLOCKED / DEGRADED / CLEAN]

Then list the spec clauses that need to be updated based on your findings. One line per
clause. These are the inputs to a spec amendment workflow:

  Spec delta:
  1. [Field/section]: [What it currently says] -> [What it should say]
  [If no spec changes needed: "Spec accurate. Fix is on provider/connector side."]

---

Write artifact: simulations/trace/contract/{topic}-contract-{date}.md
Frontmatter: skill, topic, date, contract_name, input, feature_status, breaking_count,
degraded_count, cosmetic_count.
```

---

## V-05: Output Format + Role Sequence (Axes 1+2)

**Axes:** Pre-printed comparison table (V-01) + role-ownership handoff (V-02)
**Hypothesis:** The pre-printed table with mandatory Severity and Spec Ref columns (V-01)
makes C-02 and C-03 structurally unavoidable: no row can exist without both. The role
handoff (V-02) makes C-01 structurally unavoidable: AUTOMATE cannot speak until CONNECTORS
has signed off on the expected block. These two guarantees cover the three essential criteria
most likely to fail (C-01, C-02, C-03) without any instruction-level compliance required.
C-04 is covered by a pre-printed Root Cause sub-field in the findings section. C-05 is
covered by the Breaking/Degraded/Cosmetic section separation. This is the combination
candidate for the golden synthesis in later rounds.

```
You are running /trace:contract with two active roles:

  CONNECTORS EXPERT -- owns the contract spec and writes the expected output block.
    Has final say on what the spec requires.
  AUTOMATE ENGINEER -- owns the runtime. Captures actual output.
    Leads finding analysis and owns the next steps.

Hard sequencing rule: AUTOMATE ENGINEER does not write any output until CONNECTORS EXPERT
has completed and signed off on the expected output block. This is a structural gate.
Do not blend the phases.

All column headers in the diff table are fixed. Do not remove or rename columns.
All sub-fields in the findings section are required -- do not omit any line.

---

## SETUP

Contract:       [Connector name + operation, OpenAPI path, typed action, or report spec]
Input:          [Test input in full]
Spec document:  [Document and section defining the contract]

---

## CONNECTORS EXPERT: EXPECTED OUTPUT

[CONNECTORS EXPERT writes this section. AUTOMATE ENGINEER does not contribute here.]

Reading [SPEC DOCUMENT], the contract for [CONTRACT] with input [INPUT] specifies:

Expected payload:
[Full expected response/schema as the spec defines it]

Expected field contract:
| Field path | Expected type | Expected value / constraint | Spec clause |
|------------|--------------|----------------------------|-------------|
| [field]    | [type]       | [value or constraint]      | [spec field name or section] |
| [field]    | [type]       | [value or constraint]      | [spec field name or section] |
[One row per field the spec defines. Nested fields use dot notation (forecast[].date).]

CONNECTORS EXPERT sign-off: "Expected output written from [SPEC DOCUMENT]. [N] contract
fields defined. Gate clear -- AUTOMATE ENGINEER may proceed."

[AUTOMATE ENGINEER does not write below until this sign-off line appears.]

---

## AUTOMATE ENGINEER: ACTUAL OUTPUT

[AUTOMATE ENGINEER writes this section. Capture actual from API docs, connector definition,
or test run. Do not adjust to match the expected block above.]

Actual response from [CONTRACT] with input [INPUT]:

Actual payload:
[Full actual response]

Actual fields observed:
| Field path | Actual type | Actual value | Source |
|------------|------------|--------------|--------|
| [field]    | [type]     | [value]      | [source] |
[All fields in actual, including unexpected fields not in the expected block.]

Source: [API doc version / connector definition date / test run timestamp]

---

## DIFF TABLE

[Complete for every field from either the expected or actual block. All six columns required
for every row. Do not leave Severity or Spec Ref blank on mismatch rows.]

Status values: MATCH | TYPE MISMATCH | VALUE MISMATCH | MISSING | UNEXPECTED

Severity (for mismatches):
  breaking  = AUTOMATE consumer cannot parse response; connector is non-functional
  degraded  = consumer proceeds but with incorrect, coerced, or incomplete data
  cosmetic  = no runtime impact; schema documentation is stale

Spec Ref (for mismatches): name the exact field path or spec section -- not "see spec".

| Field path | Expected (type/value) | Actual (type/value) | Status | Severity | Spec Ref |
|------------|-----------------------|---------------------|--------|----------|----------|
| [field]    | [type / value]        | [type / value]      | [status] | [breaking/degraded/cosmetic/N/A] | [spec field or section / N/A] |
| [field]    | [type / value]        | [type / value]      | [status] | [breaking/degraded/cosmetic/N/A] | [spec field or section / N/A] |

---

## FINDINGS

[AUTOMATE ENGINEER leads findings. CONNECTORS EXPERT provides spec clause verification.
One finding per mismatch row. MATCH rows do not get findings.
All four sub-fields required for every finding -- do not omit any line.]

**Breaking findings:**

F-[N] (breaking): [Field path] -- [Mismatch description]
  Spec clause (Connectors): [Exact spec field or section from diff table Spec Ref column]
  Root cause hypothesis (Automate): [Why the runtime deviates -- e.g., API provider renamed
    field in v2.1, type coercion removed from connector action, auth token response shape
    changed, field missing from action parameter mapping, schema generated from wrong version]
  Next step: [Specific -- update OpenAPI definition / add coercion shim / regenerate
    connector schema / update Parse JSON schema in flow / file provider API bug]

[Repeat for all breaking findings. If none: "No breaking findings."]

**Degraded findings:**

F-[N] (degraded): [Field path] -- [Mismatch description]
  Spec clause (Connectors): [Spec field or section]
  Root cause hypothesis (Automate): [Why]
  Next step: [Specific action]

[Repeat for all degraded findings. If none: "No degraded findings."]

**Cosmetic findings:**

F-[N] (cosmetic): [Field path] -- [Mismatch description]
  Spec clause (Connectors): [Spec field or section]
  Root cause hypothesis (Automate): [Why]
  Next step: [Specific action or "Update OpenAPI definition to reflect current provider behavior."]

[Repeat for all cosmetic findings. If none: "No cosmetic findings."]

---

## SUMMARY

| Severity | Count |
|----------|-------|
| Breaking | [N]   |
| Degraded | [N]   |
| Cosmetic | [N]   |
| **Total mismatches** | **[N]** |

Feature status: [BLOCKED (any breaking) / DEGRADED (degraded, no breaking) / CLEAN (cosmetic only or zero findings)]

---

## CONTRACT DELTA

[CONNECTORS EXPERT owns this section. List only spec clauses requiring amendment.
Suitable for direct input into a spec update workflow.]

| Spec clause | Current definition | Required amendment | Finding ref |
|-------------|-------------------|--------------------|-------------|
| [field/section] | [current text] | [corrected text] | F-[N] |
[If no spec amendments needed: "Spec accurate. Amendments required on provider side or connector definition only."]

---

Write artifact: simulations/trace/contract/{topic}-contract-{date}.md
Frontmatter: skill, topic, date, contract_name, input, source, feature_status,
breaking_count, degraded_count, cosmetic_count, spec_ref.
```

---

## Round 1 Design Notes

### Axis selection rationale

Three single-axis variations test the three surfaces most likely to determine essential
criterion pass/fail:

- **V-01 (format):** Targets C-02 and C-03 -- the most common diff-dump failure modes.
  When Severity and Spec Ref are column headers, every row must fill them.
- **V-02 (role sequence):** Targets C-01 -- the expected-first discipline. Role ownership
  makes the constraint feel domain-natural, not arbitrary.
- **V-03 (lifecycle):** Targets C-01 via a different mechanism -- phase gates rather than
  role ownership. Tests whether structural phase separation outperforms role semantics.
- **V-04 (register):** Tests the floor. Conversational voice might reduce friction but
  likely lowers C-06 (three-directory structure explicit) because no labeled headers.
- **V-05 (combo):** Inherits V-01 structural column guarantees + V-02 role handoff gate.
  Expected to score highest on essential criteria.

### Predicted rubric performance

| V | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | Notes |
|---|------|------|------|------|------|------|------|------|------|------|-------|
| V-01 | instruction | pre-printed | pre-printed | pre-printed | section | labeled | via domain | pre-printed | calibration reminder | pre-printed | C-01 weakest -- instruction only |
| V-02 | gate | instruction | pre-printed | pre-printed | section | implied | named roles | pre-printed | not addressed | pre-printed | C-06 weakest -- no 10+/20+/30+ labels |
| V-03 | gate | instruction | column | pre-printed | section | phase names | not named | pre-printed | gate reminder | pre-printed | C-07 weakest -- domain terms absent |
| V-04 | instruction | instruction | instruction | instruction | grouping | absent | absent | instruction | absent | instruction | Most failure surface; C-06 likely fails |
| V-05 | gate | pre-printed | pre-printed | pre-printed | section | labeled | named roles | pre-printed | calibration | pre-printed | Strongest essential coverage |

### Open research questions for Round 2

1. Does V-03's phase gate language produce cleaner expected-actual separation than V-02's
   role handoff on live model runs? (C-01 mechanism comparison)
2. Does V-04 pass C-06 despite absent headers, or does the model infer structure from the
   step labels? The step-by-step format has implicit 10+/20+/30+ phasing.
3. Does the pre-printed Spec Ref column in V-01/V-05 reduce spec-reference quality (model
   fills in a field name mechanically) vs. V-03/V-04 where the model reasons through the
   spec citation more deliberately?
4. V-07 (Connectors domain emphasis axis) not yet tested: would pre-printing connector-
   specific sub-fields (authentication handshake, action parameter mapping, trigger payload
   shape) improve C-07 beyond role naming alone?
