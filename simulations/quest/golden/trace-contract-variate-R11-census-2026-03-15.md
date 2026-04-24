# trace-contract Variate — Round 11 (census rubric, C-26–C-32)

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** census-v11 (C-26–C-32; C-31 + C-32 are new this round)
**Round:** R11 — 3 new single-axis explorations + 2 priority combinations from R10

---

## Round 11 Variation Map

| Variation | Axis | Primary Targets | Hypothesis |
|-----------|------|-----------------|------------|
| V-01 | role-sequence (Expert resumes ownership of S5.5 Census) | C-31, C-32, C-29, C-30 | Assigning S5.5 to the Connectors Contract Expert by name engages the spec-reading role's contract domain context for the synthesis step, rather than leaving census ownership ambiguous between phases |
| V-02 | output-format (tabular findings with mechanism-type column) | C-28, C-31, C-32 | A table column for mechanism-type makes the enumeration constraint structural — an empty cell is visually absent; S5.5 Sub-task A becomes a mechanical column tally rather than a prose-block parse |
| V-03 | lifecycle-emphasis (S5.5 as hard STOP gate with BLOCKED signal) | C-31, C-32 | Naming S5.5 as a blocking gate with explicit STOP language converts C-31 from advisory to enforced — the model cannot reach Patterns or Summary without emitting [TAXONOMY-CENSUS-COMPLETE] |
| V-04 | role-sequence + lifecycle-emphasis (Expert owns S5.5 hard STOP) | C-31, C-32, C-29, C-30 | Role ownership (quality of census decisions) + gate enforcement (emission guarantee) target C-31/C-32 at orthogonal failure modes — no interference |
| V-05 | output-format + phrasing-register (tabular findings + staging lines as decision documentation with rationale) | C-28, C-31, C-32, C-29 | Tabular mechanism-type column makes Sub-task A mechanical; rationale-bearing staging lines make Sub-task B deliberate rather than format-compliant fill-in |

---

## V-01 — Role Sequence: Expert Resumes Ownership of S5.5 Census

**axis:** role-sequence
**hypothesis:** All prior S5.5 variations introduce the step as a neutral interstitial with no named owner. At S5.5, role assignment is ambiguous: Automate just finished the findings (S5) and is still nominally active. Without explicit reassignment, the model may treat S5.5 as a mechanical formatting step rather than a contract-level synthesis. The Connectors Contract Expert read the spec to build the Expected Output; they hold the contract domain context and the mechanism vocabulary appropriate for this operation. Reassigning S5.5 explicitly to the Expert — with the instruction "the findings are Automate's work; the synthesis is yours" — changes the cognitive frame at the census site. Sub-task A is not bookkeeping; it is the Expert's verification that Automate's mechanism-type tokens are plausible for this contract domain. Sub-task B group-candidate staging is not pre-formatting; it is the Expert's determination of whether grouped findings share a systemic root cause requiring one fix or are coincident symptoms requiring independent fixes. Prediction: role assignment improves the quality of group-candidate `mechanism-type-shared` decisions because the Expert's contract-reading context is engaged at the decision site, not Automate's execution-reporting context.

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

Write the opening gate token:

```
[EXPECTED-SEALED | clauses:N | date:YYYY-MM-DD | author:Connectors-Contract-Expert | phase:1-complete]
```

Replace `N` with the count of distinct contractual clauses in the Expected Output.

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

For each deviation, write a finding block:

```
F-NN: {title}
severity: breaking | degraded | cosmetic
mechanism-type: field-mapping | serialization-path | conditional-branch | lifecycle-event | type-coercion | cardinality-violation | ordering-constraint | missing-field
root-cause-hypothesis: {one sentence — the process or condition that produced the wrong value, not a restatement of what differed}
spec-ref: {section or clause}
```

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness or consumer behavior

`mechanism-type` must be drawn from the named enumeration. If no listed type fits: `other:{description}`.

Self-test: does `root-cause-hypothesis` name a component, path, or condition? If it only restates what the diff already shows, revise until it names a mechanism.

Write: `[FINDINGS-COMPLETE | count:N]`

---

### ROLE: Connectors Contract Expert (resumes for S5.5 and closure)

**You own the Taxonomy Census. The findings are Automate's execution report. The synthesis is yours.**

You hold the spec context. You are performing the census — not formatting output, but drawing a contract-level conclusion about what failure classes this operation produced and whether they share systemic roots.

#### S5.5 — Taxonomy Census (mandatory interstitial — do not skip to S6 until both sub-tasks complete)

**Sub-task A — Mechanism distribution tally**

Walk findings F-01 through F-NN in order. Read each `mechanism-type:` token Automate assigned. Tally. This is your verification pass: if a token appears misclassified for this contract domain, note a correction.

```
mechanism-distribution: {type}:{count} {type}:{count} ...
```

Correction format (if applicable): `mechanism-distribution: field-mapping:2[1 reclassified from serialization-path] conditional-branch:1`

If no findings: `mechanism-distribution: (none — contract satisfied)`

**Sub-task B — Group-candidate staging**

For each candidate Patterns group, emit a staging line now — before any branch template in S6 is filled. This is your determination of mechanism alignment: same mechanism-type = single systemic root requiring one fix; different types = coincident symptoms requiring independent fixes.

```
group-candidate-N: findings=[F-NN, F-MM, ...] mechanism-type-shared={type token | mixed}
```

- `mechanism-type-shared` = single type token if every finding in the group shares the same `mechanism-type`
- `mechanism-type-shared` = `mixed` if the group spans more than one type token
- One staging line per candidate group
- If only one finding exists: one `group-candidate-1` line for it
- If no findings: `group-candidate: (none)`

Emit:

```
[TAXONOMY-CENSUS-COMPLETE | distribution-tokens:N | group-candidates:M | census-author:Connectors-Contract-Expert]
```

#### S5.6 — Gate Closure

Immediately after `[TAXONOMY-CENSUS-COMPLETE]`:

```
[EXPECTED-RESOLVED | gate-clauses:N | clauses-resolved:M | phase:2-complete]
```

- `gate-clauses` must equal `clauses:N` from `[EXPECTED-SEALED]`
- `clauses-resolved` = count of findings that address a committed clause

---

### ROLE: Connectors Contract Expert (continues)

#### S6 — Patterns

Branch on finding count. All `mechanism-type-shared:` values must be copied verbatim from S5.5 Sub-task B staging lines. Do not re-derive mechanism alignment at write time.

**Zero findings:**

```
no-pattern-confirmation: contract verified — all N clauses resolved with zero deviations
```

**Singleton finding (exactly one F-NN):**

```
pattern-1: {title}
single-finding-ref: F-NN
mechanism-type-shared: {copy verbatim from group-candidate-1 in S5.5 Sub-task B}
root-cause: {copy from F-NN root-cause-hypothesis}
fix-strategy: {one sentence}
```

**Multiple findings:**

For each group from S5.5 Sub-task B staging:

```
pattern-N: {title}
findings: [F-NN, F-MM, ...]
mechanism-type-shared: {copy verbatim from group-candidate-N in S5.5 Sub-task B}
root-cause: {unified root cause if single type; one sentence per independent cause if mixed}
fix-strategy: {one sentence per root cause}
```

#### S7 — Summary

```
clauses-committed: N
clauses-resolved: M
severity-breakdown: breaking:{X} degraded:{Y} cosmetic:{Z}
mechanism-distribution: {copy verbatim from S5.5 Sub-task A — do not re-derive}
assessment: {one sentence}
```

`mechanism-distribution` must be copied verbatim from S5.5 Sub-task A. Do not re-compute from findings.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Output Format: Tabular Findings with Mechanism-Type Column

**axis:** output-format
**hypothesis:** In all prior variations, `mechanism-type:` is a field inside a prose finding block. A prose field can be filled with a syntactically valid but semantically empty value — "other:unknown" or a pasted token — without visual resistance. The constraint is on the value, but there is no layout pressure to fill it correctly. A table column for mechanism-type changes the enforcement mode: the column header is always visible, the cell value is isolated from surrounding prose, and a blank cell is a visible gap in an otherwise complete row. More importantly, when mechanism-type is a column, S5.5 Sub-task A becomes a mechanical scan of one column rather than a parse of prose blocks — reducing the chance that a re-derivation in Summary diverges from per-finding values. Sub-task B group-candidate staging remains prose (grouping decisions require reasoning, not a cell value), but the input to that reasoning is a column scan rather than a block scan. Prediction: tabular format reduces mechanism-type token drift across findings and makes S5.5 Sub-task A a counting operation rather than a search-and-extract operation.

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

For each required element: state the element, its value constraint, and the spec clause.

Cover all contract surfaces:
- **Success path** — nominal input → nominal output
- **Error path** — invalid or missing input → error response
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not in the spec: `[surface]: not specified in spec — no clause`.

Write the opening gate token:

```
[EXPECTED-SEALED | clauses:N | date:YYYY-MM-DD | author:Connectors-Contract-Expert | phase:1-complete]
```

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

#### S5 — Findings Table

Write a `## Findings` section as a table. Every deviation from S4 must appear as a row.

```
| F-ID | Element (spec-ref) | Severity | Mechanism-Type | Root-Cause-Hypothesis |
|------|--------------------|----------|----------------|-----------------------|
| F-01 | {element} (§X.Y) | breaking \| degraded \| cosmetic | {enumeration value} | {mechanism sentence} |
```

Column rules:

- **Element**: exact name from Expected Output; spec clause in parentheses
- **Severity**:
  - `breaking` — consumer relying on the contract cannot function correctly
  - `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
  - `cosmetic` — differs from contract without affecting correctness or consumer behavior
- **Mechanism-Type**: must be drawn from `field-mapping` | `serialization-path` | `conditional-branch` | `lifecycle-event` | `type-coercion` | `cardinality-violation` | `ordering-constraint` | `missing-field` — or `other:{description}` if no type fits; cell cannot be blank
- **Root-Cause-Hypothesis**: one sentence naming the mechanism — the process, path, or condition that produced the wrong value. Self-test: requires knowledge of the system to write (component, path, condition)? If it could be written from the diff alone, it is a symptom — revise.

A blank Mechanism-Type cell fails C-28. A hypothesis that restates the Severity or Element fails C-05.

If no findings: `## Findings — No deviations. All clauses satisfied.`

#### S5.5 — Taxonomy Census (mandatory — complete before Patterns or Summary)

**Sub-task A — Mechanism distribution tally**

Scan the Mechanism-Type column in the Findings table. Tally each value. Produce exactly one line:

```
mechanism-distribution: {type}:{count} {type}:{count} ...
```

If no findings: `mechanism-distribution: (none — contract satisfied)`

**Sub-task B — Group-candidate staging**

Scan the Findings table for grouping candidates. For each candidate group, emit a staging line before filling any Patterns branch template:

```
group-candidate-N: findings=[F-NN, F-MM, ...] mechanism-type-shared={type token | mixed}
```

- `mechanism-type-shared` = single type token if all findings in the group share the same Mechanism-Type column value
- `mechanism-type-shared` = `mixed` if the candidate group spans more than one type token
- One staging line per candidate group; do not skip candidates
- If no findings: `group-candidate: (none)`

Emit:

```
[TAXONOMY-CENSUS-COMPLETE | distribution-tokens:N | group-candidates:M]
```

#### S5.6 — Gate Closure

```
[EXPECTED-RESOLVED | gate-clauses:N | clauses-resolved:M | phase:2-complete]
```

- `gate-clauses` = `clauses:N` from `[EXPECTED-SEALED]`
- `clauses-resolved` = count of F-NN rows that correspond to a committed clause

#### S6 — Patterns

Branch on finding count. All `mechanism-type-shared:` values copied verbatim from S5.5 Sub-task B staging lines. Do not re-derive.

**Zero findings:**

```
no-pattern-confirmation: contract verified — all N clauses resolved with zero deviations
```

**Singleton finding:**

```
pattern-1: {title}
single-finding-ref: F-01
mechanism-type-shared: {copy verbatim from group-candidate-1}
root-cause: {copy Root-Cause-Hypothesis from Findings table row F-01}
fix-strategy: {one sentence}
```

**Multiple findings:**

For each group from Sub-task B:

```
pattern-N: {title}
findings: [F-NN, F-MM, ...]
mechanism-type-shared: {copy verbatim from group-candidate-N}
root-cause: {unified if single type; one sentence per independent cause if mixed}
fix-strategy: {one sentence per root cause}
```

#### S7 — Summary

```
clauses-committed: N
clauses-resolved: M
severity-breakdown: breaking:{X} degraded:{Y} cosmetic:{Z}
mechanism-distribution: {copy verbatim from S5.5 Sub-task A — do not re-derive from table}
assessment: {one sentence}
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Lifecycle Emphasis: S5.5 as Hard STOP Gate

**axis:** lifecycle-emphasis
**hypothesis:** Prior variations name S5.5 as mandatory but do not establish a blocking condition. The model can advance from S5 (findings) directly to S6 (Patterns) without emitting S5.5 outputs; the skip is only detectable after the artifact is complete — when Summary `mechanism-distribution:` and Patterns `mechanism-type-shared:` are found to have been re-derived rather than copied. C-31 requires S5.5 as an interstitial lifecycle step; the escalation is that S5.5 must be enforced as a gate, not just named. A hard STOP with explicit BLOCKED language changes the execution path: "STOP. Before writing S6, S7, or the gate-closure token, emit both S5.5 sub-task outputs. If you advance without completing both, the artifact is BLOCKED." The BLOCKED framing makes the consequence of skipping visible at the decision point rather than at review time. Additional signal: "If there are zero findings, S5.5 collapses to two one-line outputs — the gate still requires them." This closes the most common skip path (zero-finding case treated as S5.5-exempt). Prediction: STOP gate language eliminates S5.5 skips in the zero-finding case and reduces re-derivation errors because the copy instruction is the literal next step after the census token.

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

For each required element: state the element, its value constraint, and the spec clause.

Cover all contract surfaces:
- **Success path** — nominal input → nominal output
- **Error path** — invalid or missing input → error response
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not in the spec: `[surface]: not specified in spec — no clause`.

Write:

```
[EXPECTED-SEALED | clauses:N | date:YYYY-MM-DD | author:Connectors-Contract-Expert | phase:1-complete]
```

---

### ROLE: Automate

You begin after `[EXPECTED-SEALED]`. Do not modify the Expected Output.

#### S3 — Actual Output

Run or simulate the operation against the input fixture. Write a `## Actual Output` section: status code, full response body, headers, observable side effects.

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
root-cause-hypothesis: {one sentence — process or condition that produced the wrong value}
spec-ref: {section or clause}
```

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness or consumer behavior

`mechanism-type` must be drawn from the named enumeration. If no type fits: `other:{description}`.

Self-test: does `root-cause-hypothesis` name a mechanism or restate the diff? Revise if it restates.

---

#### STOP — S5.5 TAXONOMY CENSUS (MANDATORY GATE)

**Do not write S6 (Patterns), S7 (Summary), or the gate-closure token until this step emits both sub-task outputs and produces `[TAXONOMY-CENSUS-COMPLETE]`.**

**If you advance to any of those sections without completing S5.5, the artifact is in a BLOCKED state.**

This gate applies in the zero-finding case. Zero findings → both sub-tasks produce one-line outputs — both are still required before the gate lifts.

---

**Sub-task A — Mechanism distribution tally**

Walk findings F-01 through F-NN in order. Tally each `mechanism-type:` token. Produce exactly one output line:

```
mechanism-distribution: {type}:{count} {type}:{count} ...
```

If no findings: `mechanism-distribution: (none — contract satisfied)`

**Sub-task B — Group-candidate staging**

For each candidate Patterns group, emit a staging line now — before any Patterns branch template is written. The branch template will copy from these lines; it must not re-derive.

```
group-candidate-N: findings=[F-NN, F-MM, ...] mechanism-type-shared={type token | mixed}
```

- `mechanism-type-shared` = single type token if every finding in the group shares the same `mechanism-type`
- `mechanism-type-shared` = `mixed` if the group spans more than one type token
- One staging line per candidate group
- If no findings: `group-candidate: (none)`

Emit the census completion token:

```
[TAXONOMY-CENSUS-COMPLETE | distribution-tokens:N | group-candidates:M]
```

**The STOP gate is lifted. Proceed to S5.6.**

---

#### S5.6 — Gate Closure

Immediately after `[TAXONOMY-CENSUS-COMPLETE]`:

```
[EXPECTED-RESOLVED | gate-clauses:N | clauses-resolved:M | phase:2-complete]
```

- `gate-clauses` must equal `clauses:N` from `[EXPECTED-SEALED]`
- `clauses-resolved` = count of findings that address a committed clause

#### S6 — Patterns

Branch on finding count. Copy `mechanism-type-shared:` verbatim from S5.5 Sub-task B staging lines. Do not re-derive.

**Zero findings:**

```
no-pattern-confirmation: contract verified — all N clauses resolved with zero deviations
```

**Singleton finding:**

```
pattern-1: {title}
single-finding-ref: F-NN
mechanism-type-shared: {copy verbatim from group-candidate-1 in S5.5 Sub-task B}
root-cause: {copy from F-NN root-cause-hypothesis}
fix-strategy: {one sentence}
```

**Multiple findings:**

For each group from Sub-task B staging:

```
pattern-N: {title}
findings: [F-NN, F-MM, ...]
mechanism-type-shared: {copy verbatim from group-candidate-N in S5.5 Sub-task B}
root-cause: {unified root cause if single type; one sentence per independent cause if mixed}
fix-strategy: {one sentence per root cause}
```

#### S7 — Summary

```
clauses-committed: N
clauses-resolved: M
severity-breakdown: breaking:{X} degraded:{Y} cosmetic:{Z}
mechanism-distribution: {copy verbatim from S5.5 Sub-task A — do not re-compute}
assessment: {one sentence}
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Combination: Expert Owns S5.5 + Hard STOP Gate

**axes:** role-sequence + lifecycle-emphasis
**hypothesis:** R11 priority-1 combination. V-01 assigns S5.5 to the Connectors Contract Expert by name, engaging the spec-reading role's contract-domain context for the synthesis step. V-03 enforces S5.5 with a hard STOP gate, making advancement to Patterns/Summary impossible without emitting both sub-task outputs. These mechanisms target C-31 and C-32 at different levels: role ownership targets the *quality* of S5.5 outputs (better group-candidate decisions when the Expert's contract context is active); the gate targets the *emission guarantee* (S5.5 cannot be skipped regardless of who is nominally writing). The combination test question: does role ownership independently improve Sub-task B quality beyond what the gate ensures? If yes, the two mechanisms compound. If quality is unchanged whether the Expert or Automate runs the census, role assignment is decorative and the gate is the load-bearing constraint. Prediction: no interference — ownership provides no skip-prevention guarantee; the gate provides no quality guarantee. V-04 confirms whether the two orthogonal failure modes of C-31 and C-32 (skip vs. shallow) require orthogonal interventions.

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

For each required element: state the element, its value constraint, and the spec clause.

Cover all contract surfaces:
- **Success path** — nominal input → nominal output
- **Error path** — invalid or missing input → error response
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not in the spec: `[surface]: not specified in spec — no clause`.

Write:

```
[EXPECTED-SEALED | clauses:N | date:YYYY-MM-DD | author:Connectors-Contract-Expert | phase:1-complete]
```

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
root-cause-hypothesis: {one sentence — the process or condition that produced the wrong value}
spec-ref: {section or clause}
```

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness or consumer behavior

`mechanism-type` must be drawn from the enumeration. If no type fits: `other:{description}`.

Self-test: does `root-cause-hypothesis` name a mechanism? Revise if it restates the diff.

Write: `[FINDINGS-COMPLETE | count:N]`

---

### ROLE: Connectors Contract Expert (resumes — Taxonomy Census ownership)

**You own this step. The findings are Automate's execution report. The Taxonomy Census is your contract-level synthesis.**

---

#### STOP — S5.5 TAXONOMY CENSUS (MANDATORY GATE — Expert executes)

**Automate's work ends at `[FINDINGS-COMPLETE]`. The Connectors Contract Expert now performs the Taxonomy Census.**

**Do not write S6 (Patterns), S7 (Summary), or the gate-closure token until both sub-tasks are complete and `[TAXONOMY-CENSUS-COMPLETE]` is emitted. The artifact is BLOCKED until this gate is lifted.**

This gate applies in the zero-finding case. Zero findings → both sub-tasks produce one-line outputs — still required before the gate lifts.

---

**Sub-task A — Mechanism distribution tally (Expert verification pass)**

Walk findings F-01 through F-NN. For each finding, read the `mechanism-type:` token Automate assigned. This is your verification pass: if a token appears inconsistent with the contract domain for this operation, note a correction annotation before counting.

```
mechanism-distribution: {type}:{count} {type}:{count} ...
```

Correction format: `mechanism-distribution: field-mapping:2[1 reclassified from serialization-path] conditional-branch:1`

If no findings: `mechanism-distribution: (none — contract satisfied)`

**Sub-task B — Group-candidate staging (Expert determines mechanism alignment)**

For each candidate Patterns group, emit a staging line now. You are deciding whether grouped findings share a systemic root cause (same mechanism-type, same fix owner) or are coincident symptoms (different types, different fix owners). This decision propagates into S6 fix-strategy framing.

```
group-candidate-N: findings=[F-NN, F-MM, ...] mechanism-type-shared={type token | mixed}
```

- `mechanism-type-shared` = single type token → unified fix-strategy applicable in S6
- `mechanism-type-shared` = `mixed` → independent fix-strategies required per finding in S6
- One staging line per candidate group
- If no findings: `group-candidate: (none)`

Emit:

```
[TAXONOMY-CENSUS-COMPLETE | distribution-tokens:N | group-candidates:M | census-author:Connectors-Contract-Expert]
```

**The STOP gate is lifted. Proceed to S5.6.**

---

#### S5.6 — Gate Closure (Expert)

```
[EXPECTED-RESOLVED | gate-clauses:N | clauses-resolved:M | phase:2-complete]
```

- `gate-clauses` = `clauses:N` from `[EXPECTED-SEALED]`
- `clauses-resolved` = count of findings addressing a committed clause

#### S6 — Patterns (Expert)

Branch on finding count. All `mechanism-type-shared:` values copied verbatim from S5.5 Sub-task B staging lines. Do not re-derive.

**Zero findings:**

```
no-pattern-confirmation: contract verified — all N clauses resolved with zero deviations
```

**Singleton finding:**

```
pattern-1: {title}
single-finding-ref: F-NN
mechanism-type-shared: {copy verbatim from group-candidate-1}
root-cause: {copy from F-NN root-cause-hypothesis}
fix-strategy: {one sentence — unified framing for single mechanism-type}
```

**Multiple findings:**

For each group from Sub-task B:

```
pattern-N: {title}
findings: [F-NN, F-MM, ...]
mechanism-type-shared: {copy verbatim from group-candidate-N}
root-cause: {unified if single type; one sentence per independent cause if mixed}
fix-strategy: {one sentence per root cause — independent per cause if mixed}
```

#### S7 — Summary (Expert)

```
clauses-committed: N
clauses-resolved: M
severity-breakdown: breaking:{X} degraded:{Y} cosmetic:{Z}
mechanism-distribution: {copy verbatim from S5.5 Sub-task A — do not re-derive}
assessment: {one sentence}
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — Combination: Tabular Findings + Staging Lines as Decision Documentation

**axes:** output-format + phrasing-register
**hypothesis:** R11 priority-2 combination. V-02 encodes mechanism-type as a table column, making the enumeration constraint structural (blank cell = visible gap; column scan replaces block parse for Sub-task A). The remaining S5.5 weakness: Sub-task B group-candidate staging lines can be written mechanically — one finding per group, no genuine grouping decision — without violating the format requirement. The phrasing-register axis reframes group-candidate lines as decision documentation: each staging line must include a `rationale:` clause explaining why these findings are grouped together or kept separate. Rationale-writing changes the cognitive load at Sub-task B from "emit a format-compliant line" to "document a grouping decision" — the rationale requires the model to have actually performed the comparison, not just formatted an output. Prediction: the combination improves both Sub-task A (tabular column → mechanical tally, fewer re-derivation errors in Summary) and Sub-task B (rationale → deliberate grouping decisions, more accurate `mechanism-type-shared` values). Test signal: do rationale-bearing staging lines produce fewer `mixed` overrides that mask same-mechanism findings, and fewer single-type declarations that mask genuinely different mechanisms?

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

For each required element: state the element, its value constraint, and the spec clause.

Cover all contract surfaces:
- **Success path** — nominal input → nominal output
- **Error path** — invalid or missing input → error response
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not in the spec: `[surface]: not specified in spec — no clause`.

Write:

```
[EXPECTED-SEALED | clauses:N | date:YYYY-MM-DD | author:Connectors-Contract-Expert | phase:1-complete]
```

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

#### S5 — Findings Table

Write a `## Findings` section as a table. Every deviation from S4 must appear as a row.

```
| F-ID | Element (spec-ref) | Severity | Mechanism-Type | Root-Cause-Hypothesis |
|------|--------------------|----------|----------------|-----------------------|
| F-01 | {element} (§X.Y) | breaking \| degraded \| cosmetic | {enumeration value} | {mechanism sentence} |
```

Column rules:

- **Element**: exact name from Expected Output; spec clause in parentheses
- **Severity**:
  - `breaking` — consumer relying on the contract cannot function correctly
  - `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
  - `cosmetic` — differs from contract without affecting correctness or consumer behavior
- **Mechanism-Type**: must be drawn from `field-mapping` | `serialization-path` | `conditional-branch` | `lifecycle-event` | `type-coercion` | `cardinality-violation` | `ordering-constraint` | `missing-field` — or `other:{description}`; cell cannot be blank
- **Root-Cause-Hypothesis**: one sentence naming the mechanism. Self-test: requires system knowledge to write (component, path, condition)? If writable from the diff alone, it is a symptom — revise.

If no findings: `## Findings — No deviations. All clauses satisfied.`

#### S5.5 — Taxonomy Census (mandatory — complete before Patterns or Summary)

**Sub-task A — Mechanism distribution tally**

Scan the Mechanism-Type column in the Findings table. Tally each value. Produce exactly one line:

```
mechanism-distribution: {type}:{count} {type}:{count} ...
```

If no findings: `mechanism-distribution: (none — contract satisfied)`

**Sub-task B — Group-candidate staging (decision documentation)**

For each candidate Patterns group, emit a staging line — before any Patterns branch template is written. Each line documents the grouping decision; a format entry without a rationale is insufficient.

```
group-candidate-N: findings=[F-NN, F-MM, ...] mechanism-type-shared={type token | mixed} rationale={one sentence}
```

Rationale guidance:
- If `mechanism-type-shared` is a single type token: rationale names the shared mechanism and why one fix addresses all findings in the group (e.g., "both findings trace to the field-mapping step in the response adapter — fixing the mapping resolves both")
- If `mechanism-type-shared` is `mixed`: rationale names why the findings are coincident symptoms rather than a single root cause (e.g., "F-01 is a serialization-path issue in the body encoder; F-02 is a missing-field issue in the header builder — different components, different fix owners")
- If a finding does not group with others: one staging line for it alone with rationale explaining the isolation (e.g., "no other finding shares a lifecycle-event mechanism — kept as singleton to preserve independent fix tracking")

One staging line per candidate group.

If no findings: `group-candidate: (none)`

Emit:

```
[TAXONOMY-CENSUS-COMPLETE | distribution-tokens:N | group-candidates:M]
```

#### S5.6 — Gate Closure

```
[EXPECTED-RESOLVED | gate-clauses:N | clauses-resolved:M | phase:2-complete]
```

- `gate-clauses` = `clauses:N` from `[EXPECTED-SEALED]`
- `clauses-resolved` = count of F-NN rows that correspond to a committed clause

#### S6 — Patterns

Branch on finding count. `mechanism-type-shared:` values copied verbatim from S5.5 Sub-task B staging lines. `fix-strategy:` framing informed by Sub-task B rationale.

**Zero findings:**

```
no-pattern-confirmation: contract verified — all N clauses resolved with zero deviations
```

**Singleton finding:**

```
pattern-1: {title}
single-finding-ref: F-01
mechanism-type-shared: {copy verbatim from group-candidate-1 mechanism-type-shared}
root-cause: {copy Root-Cause-Hypothesis from Findings table row F-01}
fix-strategy: {one sentence — consistent with group-candidate-1 rationale}
```

**Multiple findings:**

For each group from Sub-task B:

```
pattern-N: {title}
findings: [F-NN, F-MM, ...]
mechanism-type-shared: {copy verbatim from group-candidate-N mechanism-type-shared}
root-cause: {one sentence per independent cause — consistent with group-candidate-N rationale}
fix-strategy: {one sentence per root cause}
```

#### S7 — Summary

```
clauses-committed: N
clauses-resolved: M
severity-breakdown: breaking:{X} degraded:{Y} cosmetic:{Z}
mechanism-distribution: {copy verbatim from S5.5 Sub-task A — do not re-derive from table}
assessment: {one sentence}
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## Combination Candidates for Round 12

| Priority | Combination | Primary Targets | Rationale |
|----------|-------------|-----------------|-----------|
| 1 | V-03 (hard STOP gate) + V-05 (tabular + rationale staging) | C-31, C-32, C-28 | Gate ensures S5.5 is never skipped; tabular column makes Sub-task A mechanical; rationale-bearing staging makes Sub-task B deliberate — three orthogonal mechanisms at prevention, tally, and decision-quality levels |
| 2 | V-01 (Expert ownership) + V-02 (tabular findings) | C-28, C-29, C-30, C-31, C-32 | Tabular mechanism-type column makes tally structural; Expert ownership makes group-candidate decisions contract-level; both downstream consumers copy from a single census pass with role accountability |
| 3 | V-04 (Expert STOP) + V-05 (tabular + rationale) | C-28, C-29, C-30, C-31, C-32 | Maximum C-31/C-32 coverage: gate enforces emission, Expert assigns ownership, tabular column makes tally mechanical, rationale makes staging deliberate — four mechanisms across role, lifecycle, format, and phrasing axes |

## Evaluation Order Guidance

| Priority | Variation | Rationale |
|----------|-----------|-----------|
| 1 | V-03 (hard STOP gate) | Most direct C-31 enforcement. Tests whether explicit gate language alone eliminates S5.5 skips — establishes the emission-guarantee baseline before quality interventions are layered |
| 2 | V-02 (tabular findings) | Structural change to the findings section; Sub-task A becomes a column tally. Evaluate early to isolate whether tabular format reduces mechanism-type drift independently of gate enforcement |
| 3 | V-01 (Expert resumes for S5.5) | Role assignment alone — no gate. Measures quality improvement in group-candidate decisions when the census has role accountability but no blocking constraint |
| 4 | V-04 (Expert + STOP combination) | Confirms whether quality (V-01) and emission guarantee (V-03) compound without interference — V-03 baseline required first |
| 5 | V-05 (tabular + rationale staging) | Most complex R11 variation. Rationale-bearing staging lines are the new C-32 escalation test: do they produce more accurate `mechanism-type-shared` values, or does rationale-writing become a pro-forma step? |
