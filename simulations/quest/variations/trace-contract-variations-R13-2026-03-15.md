Now I have everything. Let me write the 5 complete variations.

---

# trace-contract Variate — Round 13

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** census-v13 (C-29–C-36; C-35 + C-36 are new this round)
**Round:** R13 — 3 new single-axis explorations + 2 priority combinations from R12

---

## Round 13 Variation Map

| Variation | Axis | Primary Targets | Hypothesis |
|-----------|------|-----------------|------------|
| V-01 | output-format (structured gate token block + cross-field verification table) | C-35, C-36 | Formatting the S6.5 gate token as a key-value block with an explicit `census-distribution:` field makes C-35 verifiable by field inspection; a cross-field verification table makes C-36 violations mechanically detectable as row failures |
| V-02 | phrasing-register (formal SHALL/SHALL NOT constraint language) | C-35, C-36 | Prohibition language ("SHALL NOT write `## Summary` header until...") converts lifecycle ordering into a detectable predicate failure; equality predicates ("SHALL equal the value on the named staging line; any inequality is a C-36 violation") make re-derivation distinguishable from compliance |
| V-03 | lifecycle-emphasis (S6.5 as named lifecycle step with entry/exit conditions) | C-35, C-33 | R12 V-03 introduced S6.5 as a behavioral gate. C-35 requires a structural invariant — making S6.5 a lifecycle step with entry condition, job, and exit condition converts it from a directive to an auditable state transition; the Summary section carries an explicit prerequisites block |
| V-04 | role-sequence (Connectors Expert returns after template population for C-36 cross-field verification) | C-36, C-34 | Automate fills templates (execution context); the Connectors Contract Expert holds the staging registry (contract context). Returning the Expert for a dedicated verification step separates template population from consistency verification, engaging the right role at the C-36 decision site |
| V-05 | role-sequence + lifecycle-emphasis + output-format | C-35, C-36 | Ceiling test: Expert-owned staging registry (role), S6.5 as named lifecycle step with structured gate token (lifecycle + format), cross-field verification table after template population (format + role) — three orthogonal enforcement mechanisms targeting C-35 and C-36 at different architectural levels |

---

## V-01 — Output Format: Structured Gate Token Block + Cross-Field Verification Table

**axis:** output-format
**hypothesis:** R12 V-03 introduced S6.5 as a prose blocking directive — "do not write the Summary header until this gate token is emitted." C-35 requires the gate token to *encode the verbatim mechanism-distribution value* from S5.5 Sub-task A, converting the gate from a sequencing instruction into a value-binding checkpoint. Formatting the S6.5 gate token as a structured key-value block with an explicit `census-distribution:` field makes the encoding presence and correctness verifiable by inspection — the field is either present with the correct value, or absent, or carries a derived value. For C-36, prior rounds require `source: group-candidate-N` in each `pattern-N:` entry but leave the consistency check implicit — a `source:` field that points to a staging line does not prevent re-derivation if the operator never compares the values. A cross-field verification table placed immediately after template population — with columns `pattern-N | source | mechanism-type-shared (at fill site) | mechanism-type-shared (from staging) | verdict` — makes the consistency check a structural row operation rather than an inferred obligation. A mismatch in the verdict column is a C-36 violation visible without re-inspecting the findings section. Prediction: structured gate token format makes C-35 detectable as a field-presence check; verification table makes C-36 detectable as a row-verdict check.

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

Self-contained. A reader must determine scope from this section alone.

#### S2 — Expected Output (the contract)

Write the complete `## Expected Output` from the spec alone. The operation has not run.

For each required element: state the element, its value constraint, and the spec clause.

Cover all contract surfaces:
- **Success path** — nominal input → nominal output
- **Error path** — invalid or missing input → error response
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not in the spec: `[surface]: not specified in spec — no clause`.

Write: `[EXPECTED-SEALED | clauses:N | date:YYYY-MM-DD | author:Connectors-Contract-Expert | phase:1-complete]`

---

### ROLE: Automate

You begin after `[EXPECTED-SEALED]`. Do not modify the Expected Output.

#### S3 — Actual Output

Run or simulate the operation against the input fixture. Write a `## Actual Output` section: status code, full response body, headers, observable side effects.

#### S4 — Diff

Write a `## Diff` section. For each element in the Expected Output:
- `✓ {element} — satisfied`
- `F-NN — {element} — deviation (see findings)`

Every element must appear. Silent omission fails coverage.

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

Write: `[FINDINGS-COMPLETE | count:N]`

---

### ROLE: Connectors Contract Expert (resumes for S5.5 and closure)

#### S5.5 — Taxonomy Census (mandatory interstitial — do not skip to S6 until both sub-tasks complete)

**Sub-task A — Mechanism distribution tally**

Walk findings F-01 through F-NN in order. Read each `mechanism-type:` token. Tally.

Emit on its own line — this is the census-authoritative value; label it `[CENSUS-DIST]` for downstream reference:

```
mechanism-distribution: {type}:{count} {type}:{count} ...
```

If no findings: `mechanism-distribution: (none — contract satisfied)`

**Sub-task B — Group-candidate staging**

For each candidate Patterns group, emit a staging line before any branch template is filled:

```
group-candidate-N: findings=[F-NN, F-MM, ...] mechanism-type-shared={type token | mixed} rationale={one sentence — why these findings share a root or require independent fixes}
```

`mechanism-type-shared` = single type token if all findings in the group share one `mechanism-type`; `mixed` if they span more than one.

Emit: `[TAXONOMY-CENSUS-COMPLETE | distribution-tokens:N | group-candidates:M | census-author:Connectors-Contract-Expert]`

#### S5.6 — Gate Closure

```
[EXPECTED-RESOLVED | gate-clauses:N | clauses-resolved:M | phase:2-complete]
```

---

**S6.5 — Census Gate (structured gate token block — mandatory before S7)**

Locate the `mechanism-distribution:` line emitted by S5.5 Sub-task A above. Copy the value exactly. Emit this structured gate token block:

```
S6.5-CENSUS-GATE:
  census-closed: true
  source: S5.5-Sub-task-A
  census-distribution: {paste the full mechanism-distribution line here, verbatim — including all type:count tokens}
  gate-status: OPEN
```

**The `## Summary` section header must not appear before this block is written. The gate-status field must read `OPEN`. If `census-distribution:` does not contain the verbatim line from S5.5 Sub-task A, the gate is not satisfied.**

The `census-distribution:` value in this block is the authoritative value for Summary consumption. Summary's `mechanism-distribution:` field is a copy of this block's `census-distribution:` field — not a recount.

---

### ROLE: Connectors Contract Expert (continues)

#### S6 — Patterns

Branch on finding count.

**Zero findings:**

```
no-pattern-confirmation: contract verified — all N clauses resolved with zero deviations
```

**Singleton finding (exactly one F-NN):**

```
pattern-1: {title}
single-finding-ref: F-NN
source: group-candidate-1
mechanism-type-shared: {copy verbatim from group-candidate-1 in S5.5 Sub-task B}
root-cause: {copy from F-NN root-cause-hypothesis}
fix-strategy: {one sentence}
```

**Multiple findings — fill one template per group-candidate from S5.5 Sub-task B:**

```
pattern-N: {title}
findings: [F-NN, F-MM, ...]
source: group-candidate-N
mechanism-type-shared: {value — see cross-field check below before writing}
root-cause: {unified root cause if single type; one sentence per independent cause if mixed}
fix-strategy: {one sentence per root cause}
```

**After all `pattern-N:` entries are written, produce the Cross-Field Verification Table:**

```
## Cross-Field Verification (C-36)

| Entry     | source:           | mechanism-type-shared (at fill site) | mechanism-type-shared (on staging line) | Verdict                |
|-----------|-------------------|--------------------------------------|-----------------------------------------|------------------------|
| pattern-1 | group-candidate-1 | {value written in pattern-1}         | {value from group-candidate-1 staging}  | CONSISTENT / C-36-VIOLATION |
| pattern-2 | group-candidate-2 | {value written in pattern-2}         | {value from group-candidate-2 staging}  | CONSISTENT / C-36-VIOLATION |
| ...       | ...               | ...                                  | ...                                     | ...                    |
```

A row is CONSISTENT when both values are identical. A row is a C-36 VIOLATION when they differ — the template field was re-derived at write time rather than copied from the staging decision. A C-36 VIOLATION means the `mechanism-type-shared:` value in that `pattern-N:` entry must be corrected to the staging line value before proceeding.

Do not write the S7 Summary header until all rows in this table show CONSISTENT.

#### S7 — Summary

S6.5 gate must be open before this section. Copy `census-distribution:` from the S6.5-CENSUS-GATE block above verbatim into `mechanism-distribution:` below. This is a copy operation, not a computation.

```
clauses-committed: N
clauses-resolved: M
severity-breakdown: breaking:{X} degraded:{Y} cosmetic:{Z}
mechanism-distribution: {VERBATIM-COPY from S6.5-CENSUS-GATE census-distribution — do not recount}
assessment: {one sentence}
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Phrasing Register: Formal Constraint Language (SHALL/SHALL NOT)

**axis:** phrasing-register (formal constraint language)
**hypothesis:** All prior variations express C-35 and C-36 as procedural instructions and copy directives. A copy directive ("copy verbatim from S5.5 Sub-task A") tells the operator *what to do* but does not declare a violation if they fail. An equality directive ("copy from the named staging line") does not state a verification predicate. Formal constraint language changes the register from instruction to obligation: "SHALL NOT write `## Summary` section header until S6.5 gate token is emitted" is a prohibition — the violation is the act of writing the header, not the absence of a copy. "The `mechanism-type-shared:` value at the fill site SHALL equal the value on the named staging line; any inequality is a C-36 violation" is a consistency predicate — satisfaction requires equality, not presence. The formal register makes each criterion evaluable as a boolean without rubric knowledge: either the predicate holds or a named violation has occurred. Prediction: SHA/SHALL NOT language for C-35 converts sequencing failure from a missing step into a detectable prohibition violation; equality predicate for C-36 converts source-reference absence into a consistency check failure with a named violation class.

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

Self-contained. A reader must determine scope from this section alone.

#### S2 — Expected Output (the contract)

Write the complete `## Expected Output` from the spec alone. The operation has not run.

For each required element: state the element, its value constraint, and the spec clause.

Cover all contract surfaces:
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

Every element must appear.

If no deviations: write `## Diff — Contract satisfied. No findings.`

#### S5 — Findings

For each deviation:

```
F-NN: {title}
severity: breaking | degraded | cosmetic
mechanism-type: field-mapping | serialization-path | conditional-branch | lifecycle-event | type-coercion | cardinality-violation | ordering-constraint | missing-field
root-cause-hypothesis: {one sentence — mechanism, not symptom restatement}
spec-ref: {section or clause}
```

Write: `[FINDINGS-COMPLETE | count:N]`

---

### ROLE: Connectors Contract Expert (resumes)

#### S5.5 — Taxonomy Census

**Constraint C-31:** S5.5 SHALL execute as a mandatory interstitial step. No branch template in S6 SHALL be populated before `[TAXONOMY-CENSUS-COMPLETE]` is emitted.

**Sub-task A — Mechanism distribution tally**

Walk findings in order. Tally each `mechanism-type:` token. The output of this sub-task is the census-authoritative distribution value — no downstream step SHALL recompute it.

```
mechanism-distribution: {type}:{count} {type}:{count} ...
```

If no findings: `mechanism-distribution: (none — contract satisfied)`

**Sub-task B — Group-candidate staging**

**Constraint C-32:** Each staging line SHALL carry a `rationale:` clause. A staging line without a rationale clause is incomplete and SHALL NOT be used as a source for S6 template population.

For each candidate Patterns group:

```
group-candidate-N: findings=[F-NN, F-MM, ...] mechanism-type-shared={type token | mixed} rationale={one sentence — shared component, path, or condition}
```

Emit: `[TAXONOMY-CENSUS-COMPLETE | distribution-tokens:N | group-candidates:M | census-author:Connectors-Contract-Expert]`

#### S5.6 — Gate Closure

```
[EXPECTED-RESOLVED | gate-clauses:N | clauses-resolved:M | phase:2-complete]
```

---

**S6.5 — Blocking Gate: Census Primacy Invariant**

**Constraint C-35:** The `## Summary` section header SHALL NOT be written until this gate step emits a gate token that encodes the verbatim `mechanism-distribution:` value from S5.5 Sub-task A. A `## Summary` header written before this gate token is a C-35 violation. A gate token whose encoded value differs from the S5.5 Sub-task A output is a C-35 violation.

Locate the `mechanism-distribution:` line from S5.5 Sub-task A. Reproduce it verbatim in the gate token below:

```
[S6.5-GATE | mechanism-distribution:{paste verbatim from S5.5 Sub-task A} | source:S5.5-Sub-task-A | gate:OPEN]
```

This gate token is the structural precondition for S7. Until it is emitted, S7 SHALL NOT begin. This is a lifecycle invariant, not a behavioral instruction — the Summary section's availability is conditional on census close, not on operator intent.

---

### ROLE: Connectors Contract Expert (continues)

#### S6 — Patterns

Branch on finding count.

**Zero findings:**

```
no-pattern-confirmation: contract verified — all N clauses resolved with zero deviations
```

**Singleton finding:**

```
pattern-1: {title}
single-finding-ref: F-NN
source: group-candidate-1
mechanism-type-shared: {copy verbatim from group-candidate-1 in S5.5 Sub-task B}
root-cause: {copy from F-NN root-cause-hypothesis}
fix-strategy: {one sentence}
```

**Multiple findings:**

**Constraint C-34:** Each `pattern-N:` entry SHALL carry a `source: group-candidate-N` field naming the S5.5 Sub-task B staging line it was derived from. An entry without a `source:` field is a C-34 violation.

**Constraint C-36:** The `mechanism-type-shared:` value in each `pattern-N:` entry SHALL equal the `mechanism-type-shared:` value on the staging line named by `source:`. Any inequality is a C-36 violation — the template field was re-derived at write time rather than copied from the staging decision. A C-36 violation is detectable by direct field comparison without re-inspecting the findings section.

For each group from S5.5 Sub-task B:

```
pattern-N: {title}
findings: [F-NN, F-MM, ...]
source: group-candidate-N
mechanism-type-shared: {SHALL equal the value on the group-candidate-N staging line — any deviation is a C-36 violation}
root-cause: {unified root cause if single type; one sentence per independent cause if mixed}
fix-strategy: {one sentence per root cause}
```

#### S7 — Summary

**Constraint C-35:** This section SHALL NOT begin before S6.5 gate is open. Verify `[S6.5-GATE ... gate:OPEN]` appears above.

**Constraint C-33:** The `mechanism-distribution:` line in this section SHALL be a verbatim copy of the value from S5.5 Sub-task A, as encoded in the S6.5 gate token. S5.5 Sub-task A is the authoritative source; this section SHALL NOT recompute or recount. If a fresh count would produce a different value, the S5.5 value is authoritative.

```
clauses-committed: N
clauses-resolved: M
severity-breakdown: breaking:{X} degraded:{Y} cosmetic:{Z}
mechanism-distribution: {SHALL equal the value in [S6.5-GATE mechanism-distribution:...] — verbatim copy, not recount}
assessment: {one sentence}
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Lifecycle Emphasis: S6.5 as Named Lifecycle Step with Entry/Exit Conditions

**axis:** lifecycle-emphasis
**hypothesis:** R12 V-03 introduced S6.5 as a prose blocking directive embedded between Patterns and Summary: "Do not write the `## Summary` section header until this gate token is emitted." That formulation makes compliance behavioral — the operator must not write the header, but the step has no named entry condition, no job description, and no named exit condition distinguishing "gate open" from "gate satisfied." C-35 requires the gate to function as a structural lifecycle precondition, not as a prohibition. A named lifecycle step with explicit entry condition, job description, and exit condition converts S6.5 from a directive into an auditable state transition: entry requires census complete (condition), the job is gate token emission encoding the census value (action), and the exit condition is that the gate token is present in the artifact encoding the verbatim distribution value (observable state). The Summary section carries an explicit prerequisites block listing the S6.5 exit condition as its authoring precondition, making the dependency structural rather than inferred from reading sequence. Prediction: named lifecycle step architecture converts C-35 from a behavioral instruction into an architectural invariant; the prerequisites block on S7 makes the dependency inspectable without rubric knowledge.

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

Self-contained. A reader must determine scope from this section alone.

#### S2 — Expected Output (the contract)

Write the complete `## Expected Output` from the spec alone. The operation has not run.

For each required element: state the element, its value constraint, and the spec clause.

Cover all contract surfaces:
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

Write a `## Diff` section. For each element:
- `✓ {element} — satisfied`
- `F-NN — {element} — deviation (see findings)`

Every element must appear.

If no deviations: write `## Diff — Contract satisfied. No findings.`

#### S5 — Findings

For each deviation:

```
F-NN: {title}
severity: breaking | degraded | cosmetic
mechanism-type: field-mapping | serialization-path | conditional-branch | lifecycle-event | type-coercion | cardinality-violation | ordering-constraint | missing-field
root-cause-hypothesis: {one sentence — mechanism, not symptom restatement}
spec-ref: {section or clause}
```

Write: `[FINDINGS-COMPLETE | count:N]`

---

### ROLE: Connectors Contract Expert (resumes)

#### S5.5 — Taxonomy Census (mandatory interstitial — do not skip to S6 until both sub-tasks complete)

**Sub-task A — Mechanism distribution tally**

Walk findings in order. Tally each `mechanism-type:` token. Emit on its own line:

```
mechanism-distribution: {type}:{count} {type}:{count} ...
```

If no findings: `mechanism-distribution: (none — contract satisfied)`

**Sub-task B — Group-candidate staging**

For each candidate Patterns group:

```
group-candidate-N: findings=[F-NN, F-MM, ...] mechanism-type-shared={type token | mixed} rationale={one sentence — why these findings share a root or require independent fixes}
```

`mechanism-type-shared` = single type if all findings share one type; `mixed` if they span more than one.

Emit: `[TAXONOMY-CENSUS-COMPLETE | distribution-tokens:N | group-candidates:M | census-author:Connectors-Contract-Expert]`

#### S5.6 — Gate Closure

```
[EXPECTED-RESOLVED | gate-clauses:N | clauses-resolved:M | phase:2-complete]
```

---

### LIFECYCLE STEP S6.5 — Census Gate

**Entry condition:** `[TAXONOMY-CENSUS-COMPLETE]` has been emitted. The `mechanism-distribution:` line from S5.5 Sub-task A is present in the artifact. S5.6 gate is closed.

**Job:** Emit a gate token that binds the census output to the Summary authoring lifecycle. The gate token must encode the verbatim `mechanism-distribution:` value from S5.5 Sub-task A. The gate token's presence in the artifact is the structural precondition for S7 — not a formatting step, but a lifecycle state transition that marks census close as an architectural invariant.

Locate the `mechanism-distribution:` line from S5.5 Sub-task A. Reproduce it in the gate token:

```
[S6.5-GATE-OPEN | mechanism-distribution-census:{verbatim line from S5.5 Sub-task A} | census-source:S5.5-Sub-task-A | lifecycle-state:summary-authoring-unlocked]
```

**Exit condition:** This gate token is present in the artifact. The `mechanism-distribution-census:` field contains the verbatim value from S5.5 Sub-task A. The lifecycle-state reads `summary-authoring-unlocked`.

**If entry condition is not met** (census not complete, or mechanism-distribution line not present): do not proceed. Return to S5.5 and complete the census before emitting this gate.

---

### ROLE: Connectors Contract Expert (continues)

#### S6 — Patterns

Branch on finding count.

**Zero findings:**

```
no-pattern-confirmation: contract verified — all N clauses resolved with zero deviations
```

**Singleton finding:**

```
pattern-1: {title}
single-finding-ref: F-NN
source: group-candidate-1
mechanism-type-shared: {copy verbatim from group-candidate-1 in S5.5 Sub-task B}
root-cause: {copy from F-NN root-cause-hypothesis}
fix-strategy: {one sentence}
```

**Multiple findings:**

For each group from S5.5 Sub-task B staging:

```
pattern-N: {title}
findings: [F-NN, F-MM, ...]
source: group-candidate-N
mechanism-type-shared: {copy verbatim from the group-candidate-N staging line — do not re-derive}
root-cause: {unified root cause if single type; one sentence per independent cause if mixed}
fix-strategy: {one sentence per root cause}
```

The `source:` field is required. A `pattern-N:` entry without `source:` is incomplete. The `mechanism-type-shared:` value must equal the value on the named staging line; a mismatch is a cross-field consistency violation — the template field was re-derived rather than copied from the staging decision.

#### S7 — Summary

**Prerequisites for authoring this section:**
1. S6.5 gate token is present: `[S6.5-GATE-OPEN ... lifecycle-state:summary-authoring-unlocked]`
2. The `mechanism-distribution-census:` value from the S6.5 gate token is available for copy

If prerequisite 1 is not satisfied, S7 must not begin. Emit `[S7-BLOCKED: S6.5 gate not open]` and return to S6.5.

**Authoritative source directive:** The `mechanism-distribution:` line in this section is a verbatim copy from the S6.5 gate token's `mechanism-distribution-census:` field. S5.5 Sub-task A is the authoritative source for this value. Do not recount findings at this step.

```
clauses-committed: N
clauses-resolved: M
severity-breakdown: breaking:{X} degraded:{Y} cosmetic:{Z}
mechanism-distribution: {VERBATIM-COPY from S6.5-GATE-OPEN mechanism-distribution-census — do not recount}
assessment: {one sentence}
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Role Sequence: Connectors Expert Returns for Cross-Field Verification

**axis:** role-sequence
**hypothesis:** All prior variations assign the Patterns section to the Connectors Contract Expert after S5.5 census is complete. The Expert fills the branch templates and the `source:` field in each entry. The cross-field consistency check (C-36) — verifying that `mechanism-type-shared:` at the fill site equals the value on the named staging line — requires the same role context as S5.5 Sub-task B: knowledge of what was decided at the census site, not what was observed during execution. If the Expert writes and verifies in the same pass, cognitive anchoring from template-population may suppress independent consistency checking. Separating template population from consistency verification by inserting a named Expert-owned verification step after Automate's S4 Diff creates a clean handoff: Automate's execution context ends at Findings; the Expert's contract context resumes for S5.5 census, then hands back to the Expert for Patterns template population, then returns to a dedicated verification role (S6.3) that holds only the staging registry and the filled templates as its inputs. The verifier has no execution memory — it reads two artifacts (staging lines, pattern entries) and produces a verdict. Prediction: a named verification step with a staging registry lookup converts C-36 from an implicit copy obligation into an explicit consistency check that is clearly distinguishable from template population.

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

Self-contained. A reader must determine scope from this section alone.

#### S2 — Expected Output (the contract)

Write the complete `## Expected Output` from the spec alone. The operation has not run.

For each required element: state the element, its value constraint, and the spec clause.

Cover all contract surfaces:
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

Write a `## Diff` section. For each element:
- `✓ {element} — satisfied`
- `F-NN — {element} — deviation (see findings)`

Every element must appear.

If no deviations: write `## Diff — Contract satisfied. No findings.`

#### S5 — Findings

For each deviation:

```
F-NN: {title}
severity: breaking | degraded | cosmetic
mechanism-type: field-mapping | serialization-path | conditional-branch | lifecycle-event | type-coercion | cardinality-violation | ordering-constraint | missing-field
root-cause-hypothesis: {one sentence — mechanism, not symptom}
spec-ref: {section or clause}
```

Write: `[FINDINGS-COMPLETE | count:N]`

---

### ROLE: Connectors Contract Expert (resumes for census and closure)

#### S5.5 — Taxonomy Census (mandatory — do not skip to S6 until both sub-tasks complete)

**Sub-task A — Mechanism distribution tally**

Walk findings in order. Tally each `mechanism-type:` token. Emit:

```
mechanism-distribution: {type}:{count} {type}:{count} ...
```

If no findings: `mechanism-distribution: (none — contract satisfied)`

**Sub-task B — Group-candidate staging**

Emit one staging line per candidate Patterns group before any branch template is filled. This staging line is the authoritative source for downstream `mechanism-type-shared:` values — the staging registry.

```
group-candidate-N: findings=[F-NN, F-MM, ...] mechanism-type-shared={type token | mixed} rationale={one sentence — shared component, path, or condition}
```

Emit: `[TAXONOMY-CENSUS-COMPLETE | distribution-tokens:N | group-candidates:M | census-author:Connectors-Contract-Expert]`

**After emitting the census-complete token, build the staging registry** — this is the authoritative lookup for the S6.3 cross-field verification step:

```
STAGING-REGISTRY:
  group-candidate-1: mechanism-type-shared={value}
  group-candidate-2: mechanism-type-shared={value}
  ... (one entry per group-candidate)
```

#### S5.6 — Gate Closure

```
[EXPECTED-RESOLVED | gate-clauses:N | clauses-resolved:M | phase:2-complete]
```

---

**S6.5 — Summary Pre-flight Gate (blocking)**

Locate the `mechanism-distribution:` line from S5.5 Sub-task A. Copy it verbatim. Emit:

```
[S6.5-PREFLIGHT | mechanism-distribution-authoritative:{verbatim from S5.5 Sub-task A} | source:S5.5-Sub-task-A | gate:OPEN]
```

The `## Summary` section header must not appear before this gate token.

---

#### S6 — Patterns (template population — Connectors Contract Expert)

Branch on finding count.

**Zero findings:**

```
no-pattern-confirmation: contract verified — all N clauses resolved with zero deviations
```

**Singleton finding:**

```
pattern-1: {title}
single-finding-ref: F-NN
source: group-candidate-1
mechanism-type-shared: {copy verbatim from group-candidate-1 in staging registry}
root-cause: {copy from F-NN root-cause-hypothesis}
fix-strategy: {one sentence}
```

**Multiple findings:**

For each group from S5.5 Sub-task B, populate the template. The `source:` field is required. Copy `mechanism-type-shared:` from the named staging line — do not re-derive.

```
pattern-N: {title}
findings: [F-NN, F-MM, ...]
source: group-candidate-N
mechanism-type-shared: {copy from staging registry entry for group-candidate-N}
root-cause: {unified or per-cause}
fix-strategy: {one sentence per root cause}
```

---

### ROLE: Connectors Contract Expert — S6.3 Cross-Field Verification

**You hold two artifacts: the STAGING-REGISTRY from S5.5 Sub-task B, and the populated `pattern-N:` entries from S6. Your job is to verify that `mechanism-type-shared:` at each fill site equals the value in the staging registry for the named `source:`. You do not re-read findings. You do not re-run the census. You compare two already-written values.**

For each `pattern-N:` entry:
1. Read `source: group-candidate-N`
2. Look up `group-candidate-N` in the STAGING-REGISTRY — record its `mechanism-type-shared` value
3. Read the `mechanism-type-shared:` value at the template fill site
4. If they are equal: CONSISTENT. If they differ: C-36 VIOLATION — the fill-site value was re-derived rather than copied from the staging decision

Write the verification result for each entry:

```
S6.3-CROSS-FIELD-CHECK:
  pattern-1: source=group-candidate-1 | staging-value={from registry} | fill-site-value={from template} | verdict=CONSISTENT / C-36-VIOLATION
  pattern-2: source=group-candidate-2 | staging-value={from registry} | fill-site-value={from template} | verdict=CONSISTENT / C-36-VIOLATION
  ...
  overall: CONSISTENT / VIOLATIONS-PRESENT
```

If any row shows C-36-VIOLATION: correct the `mechanism-type-shared:` value in the affected `pattern-N:` entry to match the staging registry value before proceeding. Write: `[S6.3-CORRECTION: pattern-N mechanism-type-shared corrected from {wrong} to {staging-value}]`

If all rows show CONSISTENT: write `[S6.3-VERIFIED: all pattern entries consistent with staging registry]`

---

#### S7 — Summary

Gate S6.5 must be open. Copy `mechanism-distribution-authoritative:` from the S6.5-PREFLIGHT gate token verbatim.

```
clauses-committed: N
clauses-resolved: M
severity-breakdown: breaking:{X} degraded:{Y} cosmetic:{Z}
mechanism-distribution: {VERBATIM-COPY from S6.5-PREFLIGHT mechanism-distribution-authoritative — do not recount}
assessment: {one sentence}
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — Combined: Expert-Owned Staging Registry + S6.5 Named Lifecycle Step + Cross-Field Verification Table

**axes:** role-sequence + lifecycle-emphasis + output-format
**hypothesis:** C-35 and C-36 are independent criteria that fail at different points in the lifecycle and for different reasons. C-35 fails when Summary is written before the census value is architecturally committed — the failure mode is premature section authoring. C-36 fails when the template fill site re-derives a value instead of copying from the staging decision — the failure mode is re-derivation at the wrong lifecycle site. Three orthogonal mechanisms: (1) Role assignment: Connectors Expert explicitly owns S5.5 Sub-task B and produces a named, attributed STAGING-REGISTRY artifact — an Expert-attributed artifact has higher authority than a result in an undifferentiated output block, engaging the Expert's contract domain context for grouping decisions and making the registry the declared source of truth for all downstream `mechanism-type-shared:` consumption. (2) Lifecycle architecture: S6.5 is a named lifecycle step (not a gate comment) with entry condition, job description, and exit condition — the exit condition's readability in the artifact is the structural precondition for S7, converting the Summary header from a format element into a dependent artifact in the lifecycle DAG. (3) Output format: after template population, a cross-field verification table (Expert-owned) produces one PASS/C-36-VIOLATION verdict row per pattern entry by direct comparison of fill-site vs staging-registry values — the table makes the consistency rule checkable without re-inspecting the findings section. Prediction: the three mechanisms compound on C-35 (role + lifecycle close the gap between census production and summary authoring) and C-36 (role + format make re-derivation detectable as a named verdict) without degrading C-29 through C-34.

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

Self-contained. A reader must determine scope from this section alone.

#### S2 — Expected Output (the contract)

Write the complete `## Expected Output` from the spec alone. The operation has not run.

For each required element: state the element, its value constraint, and the spec clause.

Cover all contract surfaces:
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

Write a `## Diff` section. For each element:
- `✓ {element} — satisfied`
- `F-NN — {element} — deviation (see findings)`

Every element must appear.

If no deviations: write `## Diff — Contract satisfied. No findings.`

#### S5 — Findings

For each deviation:

```
F-NN: {title}
severity: breaking | degraded | cosmetic
mechanism-type: field-mapping | serialization-path | conditional-branch | lifecycle-event | type-coercion | cardinality-violation | ordering-constraint | missing-field
root-cause-hypothesis: {one sentence — mechanism, not symptom}
spec-ref: {section or clause}
```

Write: `[FINDINGS-COMPLETE | count:N]`

---

### ROLE: Connectors Contract Expert (resumes — owns census and staging registry)

**You own the Taxonomy Census. The findings above are Automate's execution report. The census is your contract-level synthesis. Sub-task B staging decisions are Expert-attributed: once emitted, they are the authoritative source for all downstream mechanism-type-shared consumption.**

#### S5.5 — Taxonomy Census (mandatory interstitial — do not proceed to S6 until both sub-tasks complete)

**Sub-task A — Mechanism distribution tally**

Walk findings in order. Tally each `mechanism-type:` token. Emit on its own line — this is the census-authoritative distribution. Label it mentally as `[CENSUS-DIST]` for S6.5 consumption:

```
mechanism-distribution: {type}:{count} {type}:{count} ...
```

If no findings: `mechanism-distribution: (none — contract satisfied)`

**Sub-task B — Group-candidate staging and registry publication**

For each candidate Patterns group, emit a staging line with rationale. This staging line is an Expert decision — make it deliberate. `rationale:` must name the shared component, path, or condition, not restate the type token.

```
group-candidate-N: findings=[F-NN, F-MM, ...] mechanism-type-shared={type token | mixed} rationale={one sentence}
```

Emit: `[TAXONOMY-CENSUS-COMPLETE | distribution-tokens:N | group-candidates:M | census-author:Connectors-Contract-Expert]`

**Immediately after the census-complete token, publish the STAGING-REGISTRY.** This registry is the authoritative lookup for cross-field verification. Every downstream consumer of `mechanism-type-shared:` reads from this registry — not from re-inspection of the findings section.

```
STAGING-REGISTRY (Expert-attributed, census-authoritative):
  group-candidate-1: mechanism-type-shared={value} | rationale-summary={three words max}
  group-candidate-2: mechanism-type-shared={value} | rationale-summary={three words max}
  ... (one row per group-candidate)
```

#### S5.6 — Gate Closure

```
[EXPECTED-RESOLVED | gate-clauses:N | clauses-resolved:M | phase:2-complete]
```

---

### LIFECYCLE STEP S6.5 — Census Gate (structural precondition for S7)

**Entry condition:** `[TAXONOMY-CENSUS-COMPLETE]` has been emitted. STAGING-REGISTRY has been published. The `mechanism-distribution:` line from S5.5 Sub-task A is present in the artifact.

**Job:** Emit a gate token that binds the census output to the Summary authoring lifecycle. The gate token encodes the verbatim `mechanism-distribution:` value from S5.5 Sub-task A. This emission is the state transition from `census-open` to `summary-authoring-unlocked`. The `## Summary` section header is a dependent artifact in the lifecycle DAG — it cannot appear before this state transition occurs.

Locate the `mechanism-distribution:` line from S5.5 Sub-task A. Reproduce its value in the gate token:

```
[S6.5-GATE
  entry: TAXONOMY-CENSUS-COMPLETE=true, STAGING-REGISTRY=published
  mechanism-distribution-census: {verbatim line from S5.5 Sub-task A}
  source: S5.5-Sub-task-A
  lifecycle-state: summary-authoring-unlocked
  exit: gate-token-emitted=true
]
```

**Exit condition:** This gate token is present in the artifact. `mechanism-distribution-census:` contains the verbatim value from S5.5 Sub-task A. `lifecycle-state` reads `summary-authoring-unlocked`.

If entry condition is not met: write `[S6.5-BLOCKED: census not complete]` and return to S5.5.

---

### ROLE: Connectors Contract Expert (continues)

#### S6 — Patterns

Branch on finding count.

**Zero findings:**

```
no-pattern-confirmation: contract verified — all N clauses resolved with zero deviations
```

**Singleton finding:**

```
pattern-1: {title}
single-finding-ref: F-NN
source: group-candidate-1
mechanism-type-shared: {copy from STAGING-REGISTRY entry for group-candidate-1}
root-cause: {copy from F-NN root-cause-hypothesis}
fix-strategy: {one sentence}
```

**Multiple findings:**

For each group-candidate in the STAGING-REGISTRY, populate one branch template entry. The `source:` field is required — it names the staging line and enables the S6.3 cross-field verification step.

```
pattern-N: {title}
findings: [F-NN, F-MM, ...]
source: group-candidate-N
mechanism-type-shared: {copy from STAGING-REGISTRY entry for group-candidate-N}
root-cause: {unified root cause if single type; one sentence per independent cause if mixed}
fix-strategy: {one sentence per root cause}
```

---

#### S6.3 — Cross-Field Verification Table (Expert-owned, mandatory after all pattern entries are written)

**You hold the STAGING-REGISTRY and the completed `pattern-N:` entries. Your job is to verify that `mechanism-type-shared:` at each fill site equals the value in the STAGING-REGISTRY for the named `source:`. This check is independent of the findings section — it reads two already-written artifacts.**

Produce the following table. One row per `pattern-N:` entry. Do not skip rows.

```
## Cross-Field Verification — S6.3

| pattern   | source:           | fill-site mechanism-type-shared | registry mechanism-type-shared | verdict                |
|-----------|-------------------|--------------------------------|--------------------------------|------------------------|
| pattern-1 | group-candidate-1 | {from pattern-1 entry}         | {from STAGING-REGISTRY}        | CONSISTENT / C-36-VIOLATION |
| pattern-2 | group-candidate-2 | {from pattern-2 entry}         | {from STAGING-REGISTRY}        | CONSISTENT / C-36-VIOLATION |
| ...       | ...               | ...                            | ...                            | ...                    |
```

**Verdict rules:**
- `CONSISTENT` — fill-site value equals registry value (identical tokens, including `mixed` if applicable)
- `C-36-VIOLATION` — values differ; the template field was re-derived at write time rather than copied from the staging decision

**If any row shows C-36-VIOLATION:** correct the affected `pattern-N:` entry's `mechanism-type-shared:` to the registry value. Write a correction notice:

```
[S6.3-CORRECTION: pattern-N mechanism-type-shared corrected from '{wrong-value}' to '{registry-value}' per STAGING-REGISTRY]
```

Emit: `[S6.3-COMPLETE | rows-checked:N | violations:M | corrections-applied:M]`

---

#### S7 — Summary

**Prerequisites:**
1. S6.5 gate token present: `lifecycle-state=summary-authoring-unlocked`
2. S6.3 cross-field verification complete: `[S6.3-COMPLETE]` emitted

If either prerequisite is absent, emit `[S7-BLOCKED: {missing prerequisite}]` and do not write the `## Summary` header.

**Authoritative-source directive (C-33):** The `mechanism-distribution:` field below is a verbatim copy of the value from the S6.5 gate token's `mechanism-distribution-census:` field. S5.5 Sub-task A is the authoritative source via the S6.5 gate. Do not recount findings at this step. If a fresh count would produce a different value, the S6.5-gate-encoded value is authoritative.

```
## Summary

clauses-committed: N
clauses-resolved: M
severity-breakdown: breaking:{X} degraded:{Y} cosmetic:{Z}
mechanism-distribution: {VERBATIM-COPY from [S6.5-GATE mechanism-distribution-census:] — do not recount}
assessment: {one sentence}
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## Combination Candidates for Round 14

| Priority | Combination | Primary Targets | Rationale |
|----------|-------------|-----------------|-----------|
| 1 | V-02 (formal constraint) + V-05 (combined) | C-35, C-36 | Formal SHALL/SHALL NOT language (V-02) over the V-05 structural architecture: lifecycle step + role ownership + verification table all stated as evaluable predicates. Tests whether formal constraint language adds detectable scoring value when the structural mechanisms are already in place, or whether structure alone saturates both criteria. |
| 2 | V-03 (lifecycle step) + V-04 (role sequence) | C-35, C-36 | V-03 targets C-35 via S6.5 architecture; V-04 targets C-36 via Expert cross-field verification. Orthogonal — V-03 governs when Summary authoring opens; V-04 governs who verifies template consistency. Combination tests whether the two criteria are independent at the scoring level or whether satisfying one structurally helps the other. |
| 3 | V-01 (output format) + V-04 (role sequence) | C-36 | V-01 provides the verification table format; V-04 provides the Expert verification role. Table-only vs. Expert-plus-table — isolates whether Expert role ownership adds scoring value over format alone for C-36. |

## Evaluation Order Guidance

| Priority | Variation | Rationale |
|----------|-----------|-----------|
| 1 | V-05 (combined) | Ceiling test — maximum structural enforcement of both C-35 and C-36. If V-05 does not score full credit on both, identifies which mechanism is insufficient. |
| 2 | V-02 (formal constraint) | Single-axis register test. If formal SHALL language alone reaches both criteria, structural complexity in V-03/V-04/V-05 is overhead. Compare against V-05 to determine whether formal language adds value over structure. |
| 3 | V-03 (lifecycle step) | Single-axis C-35 target. Evaluate whether named lifecycle step architecture reaches C-35 without combining with role or format mechanisms. |
| 4 | V-04 (role sequence) | Single-axis C-36 target. Evaluate whether Expert cross-field verification alone reaches C-36 without structural gate or format mechanisms. |
| 5 | V-01 (output format) | Single-axis format test. Evaluate last — structured gate token block + verification table without lifecycle or role framing. Isolates whether format visibility alone achieves both criteria. |
