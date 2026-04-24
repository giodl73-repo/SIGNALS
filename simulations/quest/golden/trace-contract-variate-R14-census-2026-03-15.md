# trace-contract Variate — Round 14 (census rubric)

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v14 (C-26–C-38; denominator /190)
**Baseline:** R13 V-05 passes C-26–C-36; C-37 and C-38 absent from v13 rubric — added now as scored criteria
**Target criteria:** C-37 (provenance-binding sub-step within S6.5 naming S5.5 Sub-task A; `gate-provenance: S5.5-Sub-task-A` emitted), C-38 (verdict-gate closure rule blocking `## Summary` while any verdict-table row holds FAIL; resolution path requires amending S5.5 Sub-task B staging line)

---

## Round 14 Variation Map

| Variation | Axis | C-37 | C-38 | Notes |
|-----------|------|------|------|-------|
| V-01 | Role sequence — Automate acts as encoding witness at S6.5; Expert attest provenance, Automate confirms fidelity | PASS | PARTIAL | Single-axis: Expert names Sub-task A source and emits `gate-provenance: S5.5-Sub-task-A` (C-37 PASS); verdict-gate closure rule present but resolution path does not specify amending S5.5 Sub-task B staging line — says "correct the source" without naming the staging line as the correction target (C-38 PARTIAL) |
| V-02 | Output format — schema-defined gate block with required-fields list; `census-distribution:` and `gate-provenance:` as sibling named fields at fixed indent | PASS | PASS | Single-axis: named schema properties make provenance-binding a structural requirement (C-37 PASS); verdict-gate closure rule present with explicit resolution-path callout naming S5.5 Sub-task B as the amendment site (C-38 PASS) |
| V-03 | Lifecycle emphasis — S6.5 as a phase with explicit ENTER and EXIT conditions; FAIL row = BLOCKED exit; `gate-status: LOCKED` until all verdicts PASS | PARTIAL | PASS | Single-axis: gate token written as phase-header with enter/exit conditions (C-38 PASS via BLOCKED exit); provenance-binding sub-step present but `gate-provenance:` field not emitted — only names Sub-task A as source without the explicit field (C-37 PARTIAL) |
| V-04 | Phrasing register — formal imperative throughout: "Bind:", "Emit:", "Assert:", "Block:" at all gate steps | PASS | PASS | Single-axis: "Bind: census-distribution := verbatim from S5.5 Sub-task A mechanism-distribution" + "Emit: gate-provenance: S5.5-Sub-task-A" (C-37 PASS); "Block: document cannot proceed to ## Summary while any verdict-table row holds FAIL; resolution path: amend S5.5 Sub-task B staging line" (C-38 PASS) |
| V-05 | Role sequence + Lifecycle emphasis — Expert owns S6.5 provenance-binding as named step; S6.5 has explicit ENTER/EXIT conditions with Automate as witness-validator | PASS | PASS | Combination: Expert executes provenance-binding sub-step with `gate-provenance:` emission (C-37 PASS); BLOCKED exit condition names S5.5 Sub-task B as amendment target (C-38 PASS); Automate witness role makes provenance claim falsifiable at each gate |

---

## V-01 — Role Sequence: Automate as Encoding Witness at S6.5

**axis:** role-sequence — Automate assigned as encoding witness at S6.5; Connectors Contract Expert writes the provenance-binding sub-step and emits the gate token; Automate confirms that `census-distribution:` encodes the Sub-task A value faithfully before `gate-status: OPEN` is written

**hypothesis:** In R13, S6.5 is written by a single actor with no witness role at the gate-writing step. The provenance-binding surface is: the actor who writes `census-distribution:` could derive the value from the findings section rather than copying from Sub-task A output — there is no structural check at the moment of gate authorship. Assigning Automate as an encoding witness changes the gate from a unilateral assertion to a two-party confirmation: the Expert names the source and writes the gate token; Automate confirms that the `census-distribution:` value in the token matches the Sub-task A output verbatim. If the Expert re-derived the value, the Automate witness step surfaces the discrepancy before `gate-status: OPEN` can be written. C-37 PASS predicted: the Expert's provenance-binding sub-step names Sub-task A as the authoritative source and emits `gate-provenance: S5.5-Sub-task-A`. C-38 PARTIAL predicted: the verdict-gate closure rule blocks Summary on unresolved FAIL rows but does not specify the S5.5 Sub-task B staging line as the amendment site — the resolution path names "correct the source grouping" without pinning the correction to the census stage.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors Contract Expert · Automate.

---

### ROLE: Connectors Contract Expert

#### S1 — Contract Scope

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline — no external file references)
- Spec version and section governing this operation's output contract

Self-contained: a reader must understand what is being tested without opening any external file.

#### S2 — Expected Output (the contract)

Write the complete `## Expected Output` from the spec alone. The operation has not run.

For each required element: state the element, its value constraint, and the spec clause. Cover all contract surfaces:
- **Success path** — nominal input → nominal output
- **Error path** — invalid or missing input → error response
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not in the spec: `[surface]: not specified in spec — no clause`.

Write: `[EXPECTED-SEALED | clauses:N | date:YYYY-MM-DD | author:Connectors-Contract-Expert | phase:1-complete]`

---

### ROLE: Automate

You begin after `[EXPECTED-SEALED]`. Do not modify the Expected Output.

#### S3 — Actual Output

Run or simulate the operation. Write a `## Actual Output` section: status code, full response body, headers, observable side effects.

#### S4 — Diff

Write a `## Diff` section. For each element in the Expected Output:
- `✓ {element} — satisfied`
- `F-NN — {element} — deviation (see findings)`

Every element must appear. No element may be silently omitted.

If no deviations: write `## Diff — Contract satisfied. No findings.`

#### S5 — Findings

For each deviation:

```
F-NN: {title}
severity: breaking | degraded | cosmetic
mechanism-type: field-mapping | serialization-path | conditional-branch | lifecycle-event | type-coercion | cardinality-violation | ordering-constraint | missing-field
root-cause-hypothesis: {one sentence — name the component, path, or condition; not a symptom restatement}
spec-ref: {section or clause}
```

Severity:
- `breaking` — consumer cannot function correctly
- `degraded` — guarantee violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness

**Hypothesis self-test:** the hypothesis requires system knowledge to write. If it could be derived from the diff alone without knowing implementation details, revise it.

Write: `[FINDINGS-COMPLETE | count:N]`

---

### ROLE: Connectors Contract Expert (resumes — Census Owner)

You produced the Expected Output and hold the contract domain context for this operation. The findings are Automate's execution report; the synthesis is yours. Do not skip to S6 until both sub-tasks below are complete.

#### S5.5 — Taxonomy Census

**Sub-task A — Mechanism-type column scan**

Walk findings F-01 through F-NN in order. Read each `mechanism-type:` token. Tally each token. If a token appears misclassified for this contract domain, note a correction inline.

Emit the census artifact:

```
mechanism-distribution: {type}:{count} {type}:{count} ...
```

This line is the authoritative census output. Sub-task A is the sole production site for `mechanism-distribution:`. Do not recompute this value at any downstream site.

If no findings: `mechanism-distribution: (none — contract satisfied)`

**Sub-task B — Group-candidate staging**

For each candidate Patterns group, emit one staging line:

```
group-candidate-N: findings=[F-NN, F-MM, ...] mechanism-type-shared={type token | mixed} rationale={one sentence — shared root cause, not a type-token restatement}
```

Rules:
- `mechanism-type-shared` = single type token if all findings in the group share it; `mixed` otherwise
- `rationale` must name the shared mechanism — not restate the type token
- One staging line per candidate group
- If only one finding: `group-candidate-1: findings=[F-NN] mechanism-type-shared={type} rationale={one sentence}`
- If no findings: `group-candidate: (none)`

These staging lines are the authoritative per-group record. Every `mechanism-type-shared:` value that reaches the Patterns section must trace to a staging line here.

Write: `[TAXONOMY-CENSUS-COMPLETE | artifact-A:sealed | artifact-B:sealed | census-author:Connectors-Contract-Expert]`

---

### ROLE: Connectors Contract Expert (continues — Patterns Author)

#### S6 — Patterns

Branch on finding count. All branch templates consume from the Sub-task B staging lines — do not re-derive `mechanism-type-shared:` at template-fill time.

**Zero findings:**
```
no-pattern-confirmation: contract verified — all N clauses resolved with zero deviations
```

**Singleton finding (exactly one F-NN):**
```
pattern-1: {title}
single-finding-ref: F-NN
source: group-candidate-1
mechanism-type-shared: {verbatim from group-candidate-1 mechanism-type-shared value}
root-cause: {copy from F-NN root-cause-hypothesis}
fix-strategy: {one sentence}
```

**Multiple findings:**

For each `group-candidate-N` entry in Sub-task B, fill one pattern entry. The `source:` field is required and names the Sub-task B staging line this entry was derived from:

```
pattern-N: {title}
findings: [F-NN, F-MM, ...]
source: group-candidate-N
mechanism-type-shared: {verbatim from group-candidate-N mechanism-type-shared value}
root-cause: {unified if single type; one sentence per cause if mixed}
fix-strategy: {one sentence per root cause}
```

`mechanism-type-shared:` at each fill site must equal the value on the named `group-candidate-N` staging line. A value that differs from the staging line is a C-34 derivation violation — correct the staging line at Sub-task B and re-propagate, do not patch the fill site.

---

### S6.5 — Census Gate

**[Connectors Contract Expert writes. Automate acts as encoding witness.]**

All pattern entries are complete. Before writing `## Summary`, perform the following steps in order. Do not write `## Summary` until step 3 is complete.

**Step 1 — Cross-field verification table**

Populate one row per pattern entry. Write the table after all pattern entries are complete:

| pattern-N | source | mechanism-type-shared (fill site) | mechanism-type-shared (from staging) | verdict |
|-----------|--------|------------------------------------|--------------------------------------|---------|
| pattern-1 | group-candidate-1 | {value at fill site} | {value from staging line} | PASS / FAIL |

A row holds FAIL when the value at the fill site does not match the value on the named staging line.

**Step 2 — Provenance-binding sub-step**

*(Connectors Contract Expert executes this step.)*

Locate the `mechanism-distribution:` line from S5.5 Sub-task A above. This is the authoritative census output. Do not recount findings; do not re-derive from the verification table; do not re-read the findings section. Copy the Sub-task A output line verbatim.

Emit the gate token:

```
S6.5-CENSUS-GATE:
  source: S5.5 Sub-task A
  census-distribution: {verbatim copy of the mechanism-distribution: line from Sub-task A}
  gate-provenance: S5.5-Sub-task-A
  gate-status: LOCKED
```

*(Automate witness step)* Confirm that the `census-distribution:` value in the gate token matches the `mechanism-distribution:` line emitted in Sub-task A above. If they match character-for-character, record:
`automate-witness: CONFIRMED — census-distribution encodes Sub-task A output faithfully`

If they differ, record:
`automate-witness: MISMATCH — gate-status remains LOCKED; Expert must re-emit from Sub-task A verbatim`

**Step 3 — Verdict-gate closure check**

If any row in the verification table holds FAIL: the gate remains LOCKED. The document may not proceed to `## Summary`.

To advance: correct the source grouping in Sub-task B. Return to `## Summary` only when all rows hold PASS.

When all rows hold PASS and `automate-witness: CONFIRMED`:

```
S6.5-CENSUS-GATE:
  ...
  gate-status: OPEN
```

Write: `[GATE-OPEN | census-distribution:{distribution value} | verified-by:Automate]`

---

### ROLE: Connectors Contract Expert (continues — Summary Author)

*This section is reachable only after `[GATE-OPEN]` is written.*

#### S7 — Summary

```
clauses-committed: N
clauses-resolved: M
severity-breakdown: breaking:{X} degraded:{Y} cosmetic:{Z}
mechanism-distribution: {verbatim copy of census-distribution: value from S6.5-CENSUS-GATE token}
assessment: {one sentence}
```

The `mechanism-distribution:` line is a verbatim copy of the `census-distribution:` value in the S6.5-CENSUS-GATE token. Do not recount findings. The gate token is authoritative for Summary consumption.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Output Format: Schema-Defined Gate Block with Named Required Fields

**axis:** output-format — S6.5 gate token written as a named schema block with an explicit required-fields list; `census-distribution:` and `gate-provenance:` are sibling fields at fixed indentation; the schema declaration precedes the fill instructions, making field presence a schema property rather than a prose convention

**hypothesis:** In R13, the gate block's field names are correct but their schema relationship is not stated — `census-distribution:` and `gate-provenance:` are adjacent but their co-presence is not declared as a required pair. An author can omit `gate-provenance:` without violating the visible structure because there is no schema header that lists required fields. Declaring the gate token as a named schema with a required-fields manifest changes the authoring constraint: the schema header specifies that both `census-distribution:` and `gate-provenance:` are required fields, making any absent field a schema violation detectable on structural inspection. C-37 PASS predicted: the schema declares `gate-provenance: S5.5-Sub-task-A` as a required field alongside `census-distribution:`; the provenance-binding sub-step reproduces Sub-task A output verbatim into the schema slot. C-38 PASS predicted: the verdict-gate closure rule explicitly names S5.5 Sub-task B staging line as the amendment target for FAIL rows, not the template fill site.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors Contract Expert · Automate.

---

### ROLE: Connectors Contract Expert

#### S1 — Contract Scope

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline — no external file references)
- Spec version and section governing this operation's output contract

Self-contained.

#### S2 — Expected Output (the contract)

Write the complete `## Expected Output` from the spec alone. The operation has not run.

For each required element: state the element, its value constraint, and the spec clause. Cover:
- **Success path** — nominal input → nominal output
- **Error path** — invalid or missing input → error response
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not in the spec: `[surface]: not specified in spec — no clause`.

Write: `[EXPECTED-SEALED | clauses:N | date:YYYY-MM-DD | author:Connectors-Contract-Expert | phase:1-complete]`

---

### ROLE: Automate

You begin after `[EXPECTED-SEALED]`. Do not modify the Expected Output.

#### S3 — Actual Output

Run or simulate the operation. Write a `## Actual Output` section: status code, full response body, headers, observable side effects.

#### S4 — Diff

Write a `## Diff` section. For each element in the Expected Output:
- `✓ {element} — satisfied`
- `F-NN — {element} — deviation (see findings)`

Every element must appear. No element may be silently omitted.

#### S5 — Findings

For each deviation:

```
F-NN: {title}
severity: breaking | degraded | cosmetic
mechanism-type: field-mapping | serialization-path | conditional-branch | lifecycle-event | type-coercion | cardinality-violation | ordering-constraint | missing-field
root-cause-hypothesis: {one sentence — component, path, or condition; not a symptom restatement}
spec-ref: {section or clause}
```

Write: `[FINDINGS-COMPLETE | count:N]`

---

### ROLE: Connectors Contract Expert (resumes — Census Owner)

Do not skip to S6 until both sub-tasks below are complete.

#### S5.5 — Taxonomy Census

**Sub-task A — Mechanism-type column scan**

Walk findings F-01 through F-NN in order. Tally each `mechanism-type:` token.

Emit:
```
mechanism-distribution: {type}:{count} {type}:{count} ...
```

This line is the sole authoritative census output. Do not recompute at any downstream site.

**Sub-task B — Group-candidate staging**

For each candidate Patterns group:
```
group-candidate-N: findings=[F-NN, F-MM, ...] mechanism-type-shared={type token | mixed} rationale={one sentence}
```

Write: `[TAXONOMY-CENSUS-COMPLETE | artifact-A:sealed | artifact-B:sealed | census-author:Connectors-Contract-Expert]`

---

### ROLE: Connectors Contract Expert (continues — Patterns Author)

#### S6 — Patterns

Branch on finding count. `mechanism-type-shared:` values are copied from Sub-task B staging lines — not re-derived at fill time.

**Zero findings:**
```
no-pattern-confirmation: contract verified — all N clauses resolved with zero deviations
```

**Singleton finding:**
```
pattern-1: {title}
single-finding-ref: F-NN
source: group-candidate-1
mechanism-type-shared: {verbatim from group-candidate-1}
root-cause: {from F-NN root-cause-hypothesis}
fix-strategy: {one sentence}
```

**Multiple findings:** one entry per `group-candidate-N` from Sub-task B:
```
pattern-N: {title}
findings: [F-NN, F-MM, ...]
source: group-candidate-N
mechanism-type-shared: {verbatim from group-candidate-N}
root-cause: {unified or per-cause}
fix-strategy: {one sentence per root cause}
```

---

### S6.5 — Census Gate

All pattern entries are complete. Before writing `## Summary`, execute S6.5 in full. `## Summary` is not reachable until `gate-status: OPEN` is written below.

**Step 1 — Cross-field verification table**

After all pattern entries are complete, populate the following table. One row per pattern:

| pattern-N | source | mechanism-type-shared (fill site) | mechanism-type-shared (from staging) | verdict |
|-----------|--------|------------------------------------|--------------------------------------|---------|
| pattern-1 | group-candidate-1 | {fill-site value} | {staging-line value} | PASS / FAIL |

A row holds FAIL when fill-site value ≠ staging-line value.

**Step 2 — S6.5-CENSUS-GATE token (required schema)**

The gate token is a named schema block. All five fields are required. Omitting any field is a schema violation.

```
# S6.5-CENSUS-GATE schema (required fields: source, census-distribution, gate-provenance, provenance-basis, gate-status)
S6.5-CENSUS-GATE:
  source: S5.5 Sub-task A                          # required — names the authoritative source
  census-distribution: {fill from Sub-task A}       # required — verbatim from mechanism-distribution: line above
  gate-provenance: S5.5-Sub-task-A                  # required — identifies the provenance-binding source by step name
  provenance-basis: verbatim-copy-not-re-derived    # required — attests the copy method
  gate-status: LOCKED | OPEN                        # required — OPEN only when all conditions below are satisfied
```

**Provenance-binding instruction:**
To fill `census-distribution:`: locate the `mechanism-distribution:` line emitted in Sub-task A above. Copy it character-for-character into the `census-distribution:` field. Do not recount. Do not re-derive from findings. Do not compute from the verification table. The Sub-task A output line is the value; this step encodes it into the gate token with its source named in `gate-provenance:`.

**Step 3 — Verdict-gate closure rule**

> The document **may not proceed to `## Summary`** while any row in the verification table holds FAIL.
>
> **Resolution path for a FAIL row:** Amend the `group-candidate-N` staging line in **S5.5 Sub-task B** for the affected group. Do not patch the `mechanism-type-shared:` value at the Patterns fill site — a direct patch at the template is not a valid resolution. The staging line is the authoritative record; the template fill site is a copy of it. Amend at the source, re-propagate to the template, and update the verification table row. Every correction is then traceable to the census stage.
>
> Only when all rows hold PASS: set `gate-status: OPEN`.

Write: `[GATE-OPEN | census-distribution:{distribution value}]`

---

### ROLE: Connectors Contract Expert (continues — Summary Author)

*Reachable only after `[GATE-OPEN]` is written.*

#### S7 — Summary

```
clauses-committed: N
clauses-resolved: M
severity-breakdown: breaking:{X} degraded:{Y} cosmetic:{Z}
mechanism-distribution: {verbatim copy of census-distribution: from S6.5-CENSUS-GATE token}
assessment: {one sentence}
```

`mechanism-distribution:` is a verbatim copy of `census-distribution:` from the gate token. The gate token consumed Sub-task A output; Summary consumes the gate token. Do not recount.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Lifecycle Emphasis: S6.5 as Phase with Explicit ENTER and EXIT Conditions

**axis:** lifecycle-emphasis — S6.5 is structured as a named lifecycle phase with an explicit ENTER condition (all patterns complete, table populated) and an explicit EXIT condition (all verdict-table rows PASS, gate-status OPEN); FAIL rows set the EXIT condition to BLOCKED; the verdict-gate closure rule is the EXIT condition definition, not an advisory note

**hypothesis:** In R13, the verdict-gate closure rule is a behavioral instruction — "do not proceed to Summary if FAILs exist." A behavioral instruction can be followed partially: an author reads it, acknowledges the constraint, and proceeds anyway if there is no structural barrier. Naming S6.5 as a lifecycle phase with a BLOCKED exit condition changes the constraint from advisory to architectural — the exit condition is a named gate state, and BLOCKED is a terminal state that cannot transition to OPEN while FAIL rows exist. The Summary section header is structurally inaccessible during BLOCKED state; it becomes accessible only when exit condition = SATISFIED. C-38 PASS predicted: the lifecycle phase frame makes the verdict-gate closure rule the EXIT condition definition with explicit BLOCKED state. C-37 PARTIAL predicted: the gate token names Sub-task A as source and emits `census-distribution:` verbatim, but the `gate-provenance: S5.5-Sub-task-A` field is omitted — the phase structure provides enter/exit discipline without the explicit provenance field.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors Contract Expert · Automate.

---

### ROLE: Connectors Contract Expert

#### S1 — Contract Scope

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline — no external file references)
- Spec version and section governing this operation's output contract

#### S2 — Expected Output (the contract)

Write the complete `## Expected Output` from the spec alone.

For each required element: state the element, its value constraint, and the spec clause. Cover:
- **Success path** — nominal input → nominal output
- **Error path** — invalid or missing input → error response
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

Write: `[EXPECTED-SEALED | clauses:N | date:YYYY-MM-DD | author:Connectors-Contract-Expert | phase:1-complete]`

---

### ROLE: Automate

You begin after `[EXPECTED-SEALED]`. Do not modify the Expected Output.

#### S3 — Actual Output

Run or simulate the operation. Write a `## Actual Output` section.

#### S4 — Diff

Write a `## Diff` section. Every element from the Expected Output must appear by name.

#### S5 — Findings

For each deviation:

```
F-NN: {title}
severity: breaking | degraded | cosmetic
mechanism-type: field-mapping | serialization-path | conditional-branch | lifecycle-event | type-coercion | cardinality-violation | ordering-constraint | missing-field
root-cause-hypothesis: {one sentence}
spec-ref: {section or clause}
```

Write: `[FINDINGS-COMPLETE | count:N]`

---

### ROLE: Connectors Contract Expert (resumes — Census Owner)

**Phase: TAXONOMY-CENSUS**
**ENTER condition:** `[FINDINGS-COMPLETE]` written above
**EXIT condition:** `[TAXONOMY-CENSUS-COMPLETE]` written below; both sub-tasks done; do not exit before both are complete

#### S5.5 — Taxonomy Census

**Sub-task A — Mechanism-type column scan**

Walk findings F-01 through F-NN in order. Tally each `mechanism-type:` token.

Emit:
```
mechanism-distribution: {type}:{count} {type}:{count} ...
```

Authoritative census output. Do not recompute at any downstream site.

**Sub-task B — Group-candidate staging**

For each candidate Patterns group:
```
group-candidate-N: findings=[F-NN, F-MM, ...] mechanism-type-shared={type token | mixed} rationale={one sentence}
```

**EXIT: Write** `[TAXONOMY-CENSUS-COMPLETE | artifact-A:sealed | artifact-B:sealed | census-author:Connectors-Contract-Expert]`

---

**Phase: PATTERNS**
**ENTER condition:** `[TAXONOMY-CENSUS-COMPLETE]` written above
**EXIT condition:** All pattern entries complete; verification table populated (happens in S6.5)

#### S6 — Patterns

Branch on finding count. `mechanism-type-shared:` copied from Sub-task B staging lines.

**Zero findings:**
```
no-pattern-confirmation: contract verified — all N clauses resolved with zero deviations
```

**Singleton:**
```
pattern-1: {title}
single-finding-ref: F-NN
source: group-candidate-1
mechanism-type-shared: {verbatim from group-candidate-1}
root-cause: {from F-NN}
fix-strategy: {one sentence}
```

**Multiple findings:**
```
pattern-N: {title}
findings: [F-NN, F-MM, ...]
source: group-candidate-N
mechanism-type-shared: {verbatim from group-candidate-N}
root-cause: {unified or per-cause}
fix-strategy: {one sentence per root cause}
```

---

**Phase: CENSUS-GATE**
**ENTER condition:** All pattern entries complete
**EXIT condition:** All verification-table rows PASS AND census-distribution written from Sub-task A verbatim
**BLOCKED state:** Any verification-table row holds FAIL → exit condition = BLOCKED; Summary is not reachable

#### S6.5 — Census Gate

Execute all steps before transitioning to `## Summary`.

**Step 1 — Cross-field verification table**

| pattern-N | source | mechanism-type-shared (fill site) | mechanism-type-shared (from staging) | verdict |
|-----------|--------|------------------------------------|--------------------------------------|---------|
| pattern-1 | group-candidate-1 | {fill-site value} | {staging-line value} | PASS / FAIL |

FAIL when fill-site value ≠ staging-line value. Any FAIL row → exit condition = BLOCKED. See verdict-gate closure rule below.

**Step 2 — Census gate token**

Locate the `mechanism-distribution:` line from Sub-task A. Copy it verbatim into `census-distribution:`.

```
S6.5-CENSUS-GATE:
  source: S5.5 Sub-task A
  census-distribution: {verbatim from Sub-task A mechanism-distribution:}
  gate-status: LOCKED
```

**Step 3 — Verdict-gate closure rule (EXIT CONDITION)**

> **BLOCKED:** The CENSUS-GATE phase may not exit to SUMMARY while any verification-table row holds FAIL. The exit condition is BLOCKED.
>
> **Resolution path:** To clear a FAIL row, amend the `group-candidate-N` entry in **S5.5 Sub-task B** for the affected group. This is the only valid resolution path — amending the staging line at the census stage and re-propagating forward. Do not overwrite the `mechanism-type-shared:` value at the Patterns fill site without amending the staging line first. A fill-site patch without a staging-line amendment does not clear the FAIL row: the correction must trace to the census stage to be valid.
>
> **SATISFIED:** When all rows hold PASS: exit condition is SATISFIED.

Set `gate-status: OPEN`.

Write: `[GATE-OPEN | exit-condition:SATISFIED | summary:accessible]`

---

**Phase: SUMMARY**
**ENTER condition:** `[GATE-OPEN]` written above

#### S7 — Summary

```
clauses-committed: N
clauses-resolved: M
severity-breakdown: breaking:{X} degraded:{Y} cosmetic:{Z}
mechanism-distribution: {verbatim from census-distribution: in S6.5-CENSUS-GATE}
assessment: {one sentence}
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Phrasing Register: Formal Imperative Throughout

**axis:** phrasing-register — all authoring instructions use formal imperative verb forms at gate steps: "Bind:", "Emit:", "Assert:", "Block:", "Name:", "Propagate:"; hedging constructions ("should copy", "must not proceed", "is required to") are replaced with direct command forms that admit no behavioral interpretation

**hypothesis:** In R13, the provenance-binding instruction reads: "write the census-distribution field by copying from Sub-task A output." This is prescriptive prose — it specifies the intended outcome but not the execution command. An author can satisfy the prose constraint while re-deriving the value if the result matches Sub-task A by coincidence; the prose does not constrain the computation method, only the result. Formal imperative phrasing changes the constraint surface: "Bind: census-distribution := S5.5 Sub-task A mechanism-distribution verbatim" is a command whose execution method is defined — a binding operation, not a computation. Re-derivation that produces the correct value is still a non-compliant execution of the Bind command. Similarly, "Block: document cannot proceed to Summary while any FAIL row exists; Require: amend S5.5 Sub-task B staging line" cannot be partially satisfied — there is no behavioral hedge available. C-37 PASS predicted: "Bind:" and "Emit: gate-provenance: S5.5-Sub-task-A" make the provenance-binding sub-step commands rather than recommendations. C-38 PASS predicted: "Block:" and "Require:" make the verdict-gate closure rule commands with the amendment target named precisely.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors Contract Expert · Automate.

---

### ROLE: Connectors Contract Expert

#### S1 — Contract Scope

**Write:** a `## Contract Scope` section containing operation name and method, connector or Automate context and environment, input fixture (inline — no external file references), spec version and section.

#### S2 — Expected Output

**Write:** the complete `## Expected Output` from the spec alone. The operation has not run.

**Assert:** every element cites the spec clause that requires it. An element without a spec citation is not a valid contract entry.

Cover all surfaces:
- **Success path** — nominal input → nominal output
- **Error path** — invalid or missing input → error response
- **Edge case** — at least one: empty collection, null required field, rate-limit trigger, auth expiry

**Emit:** `[EXPECTED-SEALED | clauses:N | date:YYYY-MM-DD | author:Connectors-Contract-Expert | phase:1-complete]`

---

### ROLE: Automate

**Begin:** after `[EXPECTED-SEALED]`. **Prohibit:** modifying the Expected Output.

#### S3 — Actual Output

**Capture:** run or simulate the operation. **Write:** `## Actual Output` with status code, full response body, headers, observable side effects.

#### S4 — Diff

**Write:** `## Diff`. **Enumerate:** every element from the Expected Output by name.
- `✓ {element} — satisfied`
- `F-NN — {element} — deviation (see findings)`

**Assert:** no element is silently omitted.

#### S5 — Findings

**Write** one entry per deviation:

```
F-NN: {title}
severity: breaking | degraded | cosmetic
mechanism-type: field-mapping | serialization-path | conditional-branch | lifecycle-event | type-coercion | cardinality-violation | ordering-constraint | missing-field
root-cause-hypothesis: {one sentence — name the component, path, or condition}
spec-ref: {section or clause}
```

**Assert:** hypothesis names the causal mechanism. **Prohibit:** symptom restatements ("did not match", "was different").

**Emit:** `[FINDINGS-COMPLETE | count:N]`

---

### ROLE: Connectors Contract Expert (resumes)

**Assert:** `[FINDINGS-COMPLETE]` is written above. **Prohibit:** advancing to S6 before both sub-tasks below are complete.

#### S5.5 — Taxonomy Census

**Sub-task A — Mechanism-type column scan**

**Walk:** findings F-01 through F-NN in order. **Tally:** each `mechanism-type:` token by type.

**Emit:**
```
mechanism-distribution: {type}:{count} {type}:{count} ...
```

**Designate:** this line as the sole authoritative census output. **Prohibit:** recomputing this value at any downstream site.

**Sub-task B — Group-candidate staging**

**Emit** one staging line per candidate group:
```
group-candidate-N: findings=[F-NN, F-MM, ...] mechanism-type-shared={type token | mixed} rationale={one sentence}
```

**Assert:** `rationale` names the shared mechanism — not a type-token restatement.

**Emit:** `[TAXONOMY-CENSUS-COMPLETE | artifact-A:sealed | artifact-B:sealed | census-author:Connectors-Contract-Expert]`

---

### ROLE: Connectors Contract Expert (continues)

#### S6 — Patterns

**Branch** on finding count. **Prohibit:** re-deriving `mechanism-type-shared:` at fill time.

**Zero findings:**
```
no-pattern-confirmation: contract verified — all N clauses resolved with zero deviations
```

**Singleton:**
```
pattern-1: {title}
single-finding-ref: F-NN
source: group-candidate-1
mechanism-type-shared: {propagate verbatim from group-candidate-1}
root-cause: {propagate from F-NN root-cause-hypothesis}
fix-strategy: {one sentence}
```

**Multiple findings** — one entry per `group-candidate-N`:
```
pattern-N: {title}
findings: [F-NN, F-MM, ...]
source: group-candidate-N
mechanism-type-shared: {propagate verbatim from group-candidate-N}
root-cause: {unified or per-cause}
fix-strategy: {one sentence per root cause}
```

**Assert:** each `mechanism-type-shared:` value at fill site equals the value on the named staging line. **Prohibit:** direct fill-site patches — propagate from the staging line.

---

### S6.5 — Census Gate

**Precondition:** all pattern entries complete. **Assert:** `## Summary` is not written until Step 3 exits OPEN.

**Step 1 — Cross-field verification table**

**Populate** one row per pattern:

| pattern-N | source | mechanism-type-shared (fill site) | mechanism-type-shared (from staging) | verdict |
|-----------|--------|------------------------------------|--------------------------------------|---------|
| pattern-1 | group-candidate-1 | {fill-site value} | {staging-line value} | PASS / FAIL |

**Assert:** a row holds FAIL when fill-site ≠ staging-line value.

**Step 2 — Provenance-binding sub-step**

**Name:** S5.5 Sub-task A as the authoritative source for `census-distribution:`.

**Bind:** `census-distribution` := the `mechanism-distribution:` line from S5.5 Sub-task A, verbatim. Do not recount. Do not re-derive from findings. Do not re-derive from the verification table. The Sub-task A line is copied as-is.

**Emit:**
```
S6.5-CENSUS-GATE:
  source: S5.5 Sub-task A
  census-distribution: {verbatim from Sub-task A mechanism-distribution:}
  gate-provenance: S5.5-Sub-task-A
  gate-status: LOCKED
```

**Assert:** `gate-provenance: S5.5-Sub-task-A` is present and names the census step. **Prohibit:** omitting the `gate-provenance:` field.

**Step 3 — Verdict-gate closure**

**Block:** document cannot proceed to `## Summary` while any verification-table row holds FAIL.

**Require** (for each FAIL row): amend the `group-candidate-N` entry at **S5.5 Sub-task B** for the affected group. **Prohibit:** overwriting `mechanism-type-shared:` at the Patterns fill site without amending the staging line. **Assert:** every correction is traceable to the census stage.

**Propagate:** amended staging-line value to the Patterns fill site. **Update:** verification-table row.

**Open** (when all rows hold PASS):

```
S6.5-CENSUS-GATE:
  ...
  gate-status: OPEN
```

**Emit:** `[GATE-OPEN | census-distribution:{value}]`

---

### ROLE: Connectors Contract Expert

**Assert:** `[GATE-OPEN]` is written. **Begin:** `## Summary`.

#### S7 — Summary

```
clauses-committed: N
clauses-resolved: M
severity-breakdown: breaking:{X} degraded:{Y} cosmetic:{Z}
mechanism-distribution: {propagate verbatim from census-distribution: in S6.5-CENSUS-GATE}
assessment: {one sentence}
```

**Propagate:** `mechanism-distribution:` from `census-distribution:` in the gate token. **Prohibit:** recounting findings.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — Role Sequence + Lifecycle Emphasis: Expert Owns S6.5 Provenance-Binding; Phase ENTER/EXIT at Every Transition

**axis:** role-sequence + lifecycle-emphasis — Connectors Contract Expert explicitly owns the S6.5 provenance-binding sub-step as a named step within their resumed role; each lifecycle phase carries an explicit ENTER condition and EXIT condition; Automate acts as encoding witness at S6.5 (role sequence addition); BLOCKED exit condition for FAIL rows is the lifecycle definition of C-38 (lifecycle emphasis addition)

**hypothesis:** Two independent failure surfaces in R13: (1) The provenance-binding sub-step in S6.5 has no named owner — any actor can write it, which means the Expert's census authority does not extend into the gate-writing step. Assigning S6.5 Step 2 to the Expert by name establishes that the census owner is the provenance attester — making re-derivation at the gate step a role boundary violation. (2) The verdict-gate closure rule is advisory rather than architectural — it can be read and bypassed. Adding a BLOCKED lifecycle exit condition converts it from advisory to structural: the Summary phase cannot be entered while exit condition = BLOCKED. C-37 PASS predicted: Expert-owned provenance-binding sub-step with explicit `gate-provenance: S5.5-Sub-task-A` field emission, auditable as the Expert's attestation of the S5.5 census value. C-38 PASS predicted: BLOCKED exit condition at the CENSUS-GATE phase, with amendment target named as S5.5 Sub-task B staging line and traceability requirement for every correction to the census stage.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors Contract Expert · Automate.

---

### ROLE: Connectors Contract Expert

**Phase: CONTRACT-SCOPE**
**ENTER condition:** session start
**EXIT condition:** `[EXPECTED-SEALED]` written

#### S1 — Contract Scope

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline — no external file references)
- Spec version and section governing this operation's output contract

Self-contained.

#### S2 — Expected Output (the contract)

Write the complete `## Expected Output` from the spec alone. The operation has not run.

For each required element: state the element, its value constraint, and the spec clause. Cover:
- **Success path** — nominal input → nominal output
- **Error path** — invalid or missing input → error response
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not in the spec: `[surface]: not specified in spec — no clause`.

**EXIT: Write** `[EXPECTED-SEALED | clauses:N | date:YYYY-MM-DD | author:Connectors-Contract-Expert | phase:1-complete]`

---

### ROLE: Automate

**Phase: EXECUTION**
**ENTER condition:** `[EXPECTED-SEALED]` written above
**EXIT condition:** `[FINDINGS-COMPLETE]` written below

Do not modify the Expected Output.

#### S3 — Actual Output

Run or simulate the operation. Write a `## Actual Output` section: status code, full response body, headers, observable side effects.

#### S4 — Diff

Write a `## Diff` section. Every element from the Expected Output must appear by name:
- `✓ {element} — satisfied`
- `F-NN — {element} — deviation (see findings)`

No element may be silently omitted.

#### S5 — Findings

For each deviation:

```
F-NN: {title}
severity: breaking | degraded | cosmetic
mechanism-type: field-mapping | serialization-path | conditional-branch | lifecycle-event | type-coercion | cardinality-violation | ordering-constraint | missing-field
root-cause-hypothesis: {one sentence — component, path, or condition; not a symptom restatement}
spec-ref: {section or clause}
```

**EXIT: Write** `[FINDINGS-COMPLETE | count:N]`

---

### ROLE: Connectors Contract Expert (resumes — Census Owner)

**Phase: TAXONOMY-CENSUS**
**ENTER condition:** `[FINDINGS-COMPLETE]` written above
**EXIT condition:** `[TAXONOMY-CENSUS-COMPLETE]` written below; both sub-tasks complete; do not exit before both

#### S5.5 — Taxonomy Census

You produced the Expected Output. You now perform the census. The findings are Automate's execution report; the synthesis is yours.

**Sub-task A — Mechanism-type column scan**

Walk findings F-01 through F-NN in order. Read each `mechanism-type:` token. Tally.

Emit:
```
mechanism-distribution: {type}:{count} {type}:{count} ...
```

Sub-task A is the sole production site for `mechanism-distribution:`. This line is the authoritative census output. Do not recompute at any downstream site.

If no findings: `mechanism-distribution: (none — contract satisfied)`

**Sub-task B — Group-candidate staging**

For each candidate Patterns group:
```
group-candidate-N: findings=[F-NN, F-MM, ...] mechanism-type-shared={type token | mixed} rationale={one sentence — shared root cause, not a type-token restatement}
```

Rules:
- `mechanism-type-shared` = single type token if all findings share it; `mixed` otherwise
- `rationale` must name the shared mechanism, not restate the type token

These staging lines are the authoritative per-group record. Every `mechanism-type-shared:` value that reaches the Patterns section must trace to a staging line here.

**EXIT: Write** `[TAXONOMY-CENSUS-COMPLETE | artifact-A:sealed | artifact-B:sealed | census-author:Connectors-Contract-Expert]`

---

### ROLE: Connectors Contract Expert (continues — Patterns Author)

**Phase: PATTERNS**
**ENTER condition:** `[TAXONOMY-CENSUS-COMPLETE]` written above
**EXIT condition:** all pattern entries complete; transition to CENSUS-GATE phase

#### S6 — Patterns

Branch on finding count. `mechanism-type-shared:` values are copied verbatim from Sub-task B staging lines — not re-derived at fill time.

**Zero findings:**
```
no-pattern-confirmation: contract verified — all N clauses resolved with zero deviations
```

**Singleton finding:**
```
pattern-1: {title}
single-finding-ref: F-NN
source: group-candidate-1
mechanism-type-shared: {verbatim from group-candidate-1 mechanism-type-shared value}
root-cause: {copy from F-NN root-cause-hypothesis}
fix-strategy: {one sentence}
```

**Multiple findings** — one entry per `group-candidate-N` from Sub-task B:
```
pattern-N: {title}
findings: [F-NN, F-MM, ...]
source: group-candidate-N
mechanism-type-shared: {verbatim from group-candidate-N mechanism-type-shared value}
root-cause: {unified if single type; one sentence per cause if mixed}
fix-strategy: {one sentence per root cause}
```

Audit rule: `mechanism-type-shared:` at each fill site must equal the value on the named staging line. A value that differs from the staging line is a derivation violation — see the CENSUS-GATE resolution path.

---

### ROLE: Connectors Contract Expert (continues — Gate Author) · Automate (encoding witness)

**Phase: CENSUS-GATE**
**ENTER condition:** all pattern entries complete (PATTERNS phase exited)
**EXIT condition SATISFIED:** all verification-table rows PASS AND `gate-status: OPEN` written AND `automate-witness: CONFIRMED`
**EXIT condition BLOCKED:** any verification-table row holds FAIL; transition to SUMMARY is prohibited while BLOCKED

#### S6.5 — Census Gate

Execute all steps in order. `## Summary` is not reachable until exit condition = SATISFIED.

**Step 1 — Cross-field verification table**

*(Written by: Connectors Contract Expert)*

After all pattern entries are complete, populate one row per pattern:

| pattern-N | source | mechanism-type-shared (fill site) | mechanism-type-shared (from staging) | verdict |
|-----------|--------|------------------------------------|--------------------------------------|---------|
| pattern-1 | group-candidate-1 | {fill-site value} | {staging-line value} | PASS / FAIL |

A row holds FAIL when fill-site value ≠ staging-line value.

**Step 2 — Provenance-binding sub-step**

*(Owned by: Connectors Contract Expert — this step is not delegated to Automate)*

You are the census owner. You produced the `mechanism-distribution:` line in Sub-task A. This step binds that output into the gate token with your authority as the census author. Execute:

1. Locate the `mechanism-distribution:` line you emitted in S5.5 Sub-task A above.
2. Copy it verbatim — do not recount findings, do not re-derive from the verification table, do not re-read the findings section. The Sub-task A output line is the value; copy it character-for-character.
3. Emit the gate token:

```
S6.5-CENSUS-GATE:
  source: S5.5 Sub-task A
  census-distribution: {verbatim copy of mechanism-distribution: from Sub-task A}
  gate-provenance: S5.5-Sub-task-A
  gate-status: LOCKED
```

The `gate-provenance: S5.5-Sub-task-A` field is the Expert's attestation that `census-distribution:` is a verbatim copy from Sub-task A and was not re-derived at this step.

**Step 3 — Automate encoding witness**

*(Performed by: Automate)*

Confirm that `census-distribution:` in the gate token matches the `mechanism-distribution:` line from Sub-task A above. Character-for-character comparison.

If they match:
`automate-witness: CONFIRMED — census-distribution encodes Sub-task A output faithfully; gate-provenance attested by Expert`

If they differ:
`automate-witness: MISMATCH — values differ; gate-status remains LOCKED; Expert must re-execute provenance-binding sub-step from Sub-task A verbatim`

**Step 4 — Verdict-gate closure rule (EXIT CONDITION DEFINITION)**

> **EXIT condition BLOCKED:** The CENSUS-GATE phase may not transition to SUMMARY while any verification-table row holds FAIL. The SUMMARY phase is not accessible during BLOCKED state.
>
> **Resolution path for a FAIL row (the only valid path):**
> Amend the `group-candidate-N` staging line in **S5.5 Sub-task B** for the affected group. This is the census stage amendment — do not patch the `mechanism-type-shared:` value at the Patterns fill site directly. The staging line is the authoritative record; the fill site is a derived copy. Correct at the source, re-propagate the amended value to the Patterns fill site, and update the verification-table row. The correction is then traceable to the census stage.
>
> **EXIT condition SATISFIED:** all verification-table rows hold PASS AND `automate-witness: CONFIRMED`. When both conditions are met:

```
S6.5-CENSUS-GATE:
  source: S5.5 Sub-task A
  census-distribution: {value}
  gate-provenance: S5.5-Sub-task-A
  gate-status: OPEN
```

Write: `[GATE-OPEN | exit-condition:SATISFIED | census-distribution:{value} | witness:Automate-CONFIRMED]`

---

### ROLE: Connectors Contract Expert (continues — Summary Author)

**Phase: SUMMARY**
**ENTER condition:** `[GATE-OPEN]` with `exit-condition:SATISFIED` written above

#### S7 — Summary

```
clauses-committed: N
clauses-resolved: M
severity-breakdown: breaking:{X} degraded:{Y} cosmetic:{Z}
mechanism-distribution: {verbatim copy of census-distribution: from S6.5-CENSUS-GATE token}
assessment: {one sentence}
```

`mechanism-distribution:` is a verbatim copy of `census-distribution:` from the gate token. The gate token consumed Sub-task A output; Summary consumes the gate token. Do not recount.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## Evaluation Notes

**Recommended evaluation order:**

1. **V-05 first** — ceiling test: role ownership + lifecycle enter/exit is the highest-information combination; if V-05 passes both C-37 and C-38 at maximum strength, the combination is sufficient; analyze V-01 and V-03 to determine which axis contributes marginal value
2. **V-04 second** — single-axis phrasing register test; if formal imperative produces the same C-37/C-38 scores as V-05 with less structural machinery, phrasing register is the dominant lever
3. **V-02 third** — single-axis output format test; the schema-defined gate block is the closest structural analog to V-05's explicit provenance-binding ownership claim; if V-02 matches V-05 on C-37, named schema properties substitute for role ownership
4. **V-01 fourth** — role sequence in isolation; isolates whether Automate witness attestation adds value over the Expert's unilateral gate-authorship
5. **V-03 fifth** — lifecycle emphasis in isolation; if V-03 passes C-38 while failing C-37 (predicted), isolates the BLOCKED exit condition as the minimum C-38 mechanism and confirms `gate-provenance:` field emission is required independently for C-37

**Critical criterion tests:**

- **C-37** — Character-level test: is `gate-provenance: S5.5-Sub-task-A` present as a named field in the gate token? AND is the provenance-binding sub-step a named step (not just an inline comment) that identifies Sub-task A as the authoritative source? A gate token with `census-distribution:` but without `gate-provenance:` fails C-37.
- **C-38** — Structural test: does the verdict-gate closure rule (a) explicitly block `## Summary` while any FAIL row exists AND (b) name S5.5 Sub-task B staging line as the amendment target (not the template fill site)? A rule that says "correct the error" without naming the staging line as the correction site fails C-38 on the resolution-path requirement.

**Failure mode to watch:**

V-01 PARTIAL predicted on C-38: the Automate witness step confirms encoding fidelity but the resolution path for FAIL rows says "correct the source grouping" — plausible without naming Sub-task B. If V-01 produces this exact failure, it confirms that amendment-target specificity in the resolution path is a distinct requirement from the gate-blocking constraint itself. V-03 PARTIAL predicted on C-37: the lifecycle phase structure provides enter/exit discipline but omits the `gate-provenance:` field. If V-03 produces this failure, it confirms that the explicit field emission is a requirement independent of the lifecycle framing — structural phase discipline does not substitute for the named provenance field.
