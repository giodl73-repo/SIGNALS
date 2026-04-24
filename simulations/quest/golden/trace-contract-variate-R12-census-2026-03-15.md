# trace-contract Variate — Round 12 (census rubric, C-29–C-34)

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** census-v12 (C-29–C-34; C-33 + C-34 are new this round)
**Round:** R12 — 3 new single-axis explorations + 2 priority combinations from R11

---

## Round 12 Variation Map

| Variation | Axis | Primary Targets | Hypothesis |
|-----------|------|-----------------|------------|
| V-01 | phrasing-register (explicit verbatim-copy directive at Summary) | C-33 | A named `VERBATIM-COPY` directive at the Summary instruction site converts an inferred data flow into a structural obligation — the operator is told *where* to get the value, not just *what* value to write |
| V-02 | output-format (`source: group-candidate-N` field in Multi-pattern template) | C-34 | When `source:` is a named field in the branch template, filling it is a format-compliance act; when it is absent, adding it is a judgment call that is skipped under cognitive pressure |
| V-03 | lifecycle-emphasis (Gate S6.5 blocks Summary until `mechanism-distribution:` is quoted) | C-33 | A blocking gate converts copy-forward from a value-placement instruction into a behavioral precondition — the operator must reproduce the line from S5.5 Sub-task A to unlock the Summary section |
| V-04 | phrasing-register + output-format (verbatim-copy directive + source field — C-33 + C-34 dual) | C-33, C-34 | C-33 and C-34 close two independent derivation sites (Summary and Patterns); the axes are orthogonal, so combining them closes both gaps without interference |
| V-05 | role-sequence + lifecycle-emphasis + output-format (Expert produces named census artifacts; downstream consumers copy by name) | C-29–C-34 | Named census artifacts with downstream named consumption convert data flow into role-enforced handoffs, eliminating re-derivation at both C-33 (Summary) and C-34 (Patterns) sites |

---

## V-01 — Phrasing Register: Explicit Verbatim-Copy Directive at Summary

**axis:** phrasing-register
**hypothesis:** In prior rounds, the Summary section instructs the operator to include `mechanism-distribution:` but does not say *where* it comes from. The inferred rule is: copy from S5.5 Sub-task A. An inferred rule is not enforced — an operator who re-counts findings from scratch produces a syntactically valid Summary that violates C-33. The gap is not at S5.5 (Sub-task A produces the value) but at S7 (Summary consumes it without a named source obligation). Adding a named directive `VERBATIM-COPY from [S5.5 Sub-task A · mechanism-distribution]` at the Summary instruction site eliminates the inference: the operator is told to go to a named prior output and copy the line, not to compute a value. The copy-forward obligation is structural rather than implied by data flow. Prediction: explicit source designation in the Summary instruction eliminates Summary-site re-derivation and makes the C-33 obligation as legible as the C-31 gate token.

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

Walk findings F-01 through F-NN in order. Read each `mechanism-type:` token. Tally. This is your verification pass: if a token appears misclassified for this contract domain, note a correction.

Emit this line — it is the authoritative value for downstream Summary consumption:

```
mechanism-distribution: {type}:{count} {type}:{count} ...
```

Correction format (if applicable): `mechanism-distribution: field-mapping:2[1 reclassified from serialization-path] conditional-branch:1`

If no findings: `mechanism-distribution: (none — contract satisfied)`

**Sub-task B — Group-candidate staging**

For each candidate Patterns group, emit a staging line before any branch template in S6 is filled. Include a rationale for the grouping decision:

```
group-candidate-N: findings=[F-NN, F-MM, ...] mechanism-type-shared={type token | mixed} rationale={one sentence — why these findings share a root or require independent fixes}
```

- `mechanism-type-shared` = single type token if every finding in the group shares the same `mechanism-type`
- `mechanism-type-shared` = `mixed` if the group spans more than one type token
- `rationale` must name the shared component, path, or condition — not restate the type token
- One staging line per candidate group

Emit:

```
[TAXONOMY-CENSUS-COMPLETE | distribution-tokens:N | group-candidates:M | census-author:Connectors-Contract-Expert]
```

#### S5.6 — Gate Closure

```
[EXPECTED-RESOLVED | gate-clauses:N | clauses-resolved:M | phase:2-complete]
```

---

### ROLE: Connectors Contract Expert (continues)

#### S6 — Patterns

Branch on finding count. All `mechanism-type-shared:` values are copied verbatim from S5.5 Sub-task B staging lines. Do not re-derive mechanism alignment at write time.

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

**Copy-forward step (required before writing body):** Locate the `mechanism-distribution:` line emitted by S5.5 Sub-task A above. Copy that line verbatim. Paste it into the `mechanism-distribution:` field below. This is a copy operation, not a computation — do not recount findings.

```
clauses-committed: N
clauses-resolved: M
severity-breakdown: breaking:{X} degraded:{Y} cosmetic:{Z}
mechanism-distribution: {VERBATIM-COPY from [S5.5 Sub-task A · mechanism-distribution] — do not recount}
assessment: {one sentence}
```

The `mechanism-distribution:` line must be the exact text from S5.5 Sub-task A. If a fresh count of findings would produce a different value, the S5.5 value is authoritative.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Output Format: `source: group-candidate-N` Field in Multi-pattern Template

**axis:** output-format
**hypothesis:** In prior rounds, the Multi-pattern branch template has no field naming the S5.5 Sub-task B staging line it was derived from. The operator fills `mechanism-type-shared:` by copying from the staging line, but there is no structural requirement that the pattern entry name its source. An operator who re-derives `mechanism-type-shared:` at template-fill time produces a syntactically valid pattern entry that violates C-34. The gap is that the template does not require a back-reference — adding a `source:` field converts source attribution from a judgment call into a format-compliance act. The field is present in the template; the operator fills it with the staging line identifier; any entry without a `source:` field is visibly incomplete. A filled `source:` field makes the audit chain inspectable: a reviewer can go from `pattern-N:` to `group-candidate-N:` to F-NN and verify the derivation path without re-running the census. Prediction: a required `source:` field in the template eliminates template-site re-derivation and creates a closed traceability chain from patterns back to staging decisions.

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

Every element must appear.

If no deviations: write `## Diff — Contract satisfied. No findings.`

#### S5 — Findings

For each deviation, write a finding block:

```
F-NN: {title}
severity: breaking | degraded | cosmetic
mechanism-type: field-mapping | serialization-path | conditional-branch | lifecycle-event | type-coercion | cardinality-violation | ordering-constraint | missing-field
root-cause-hypothesis: {one sentence — name the mechanism, not the symptom}
spec-ref: {section or clause}
```

Self-test: if `root-cause-hypothesis` could be written from the diff alone, it is a symptom — revise to name a component, path, or condition.

Write: `[FINDINGS-COMPLETE | count:N]`

---

### ROLE: Connectors Contract Expert (resumes)

#### S5.5 — Taxonomy Census (mandatory — do not proceed to S6 until both sub-tasks complete)

**Sub-task A — Mechanism distribution tally**

Walk findings in order. Tally each `mechanism-type:` token. Emit:

```
mechanism-distribution: {type}:{count} {type}:{count} ...
```

If no findings: `mechanism-distribution: (none — contract satisfied)`

**Sub-task B — Group-candidate staging**

For each candidate Patterns group, emit a staging line before any branch template is filled:

```
group-candidate-N: findings=[F-NN, F-MM, ...] mechanism-type-shared={type token | mixed} rationale={one sentence}
```

Emit: `[TAXONOMY-CENSUS-COMPLETE | distribution-tokens:N | group-candidates:M]`

#### S5.6 — Gate Closure

```
[EXPECTED-RESOLVED | gate-clauses:N | clauses-resolved:M | phase:2-complete]
```

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

**Multiple findings:**

For each group from S5.5 Sub-task B staging, fill the template below. The `source:` field names the staging line this entry was derived from — it is a required field. Do not re-derive `mechanism-type-shared:` at template-fill time; copy it from the named staging line.

```
pattern-N: {title}
findings: [F-NN, F-MM, ...]
source: group-candidate-N
mechanism-type-shared: {copy verbatim from the source group-candidate-N staging line in S5.5 Sub-task B}
root-cause: {unified root cause if single type; one sentence per independent cause if mixed}
fix-strategy: {one sentence per root cause}
```

A `pattern-N:` entry without a `source:` field is incomplete. A `pattern-N:` entry where `mechanism-type-shared:` differs from the named staging line value is a C-34 violation.

#### S7 — Summary

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

## V-03 — Lifecycle Emphasis: Gate S6.5 Blocks Summary Until `mechanism-distribution:` Is Quoted

**axis:** lifecycle-emphasis
**hypothesis:** In prior rounds, the Summary section carries a copy-from-S5.5 instruction as a prose comment inside the template. This instruction is a value-placement directive: it tells the operator what to write, but writing is still a single act at template-fill time. An operator under cognitive load can satisfy the instruction by re-counting findings — producing a value that looks correct but was not copied. The copy-forward obligation is behavioral only at the point of writing, not enforced before writing begins. A hard gate between S5.6 and S7 changes the enforcement mode: the gate token requires the operator to quote the `mechanism-distribution:` line from S5.5 Sub-task A output before the Summary section is unlocked. To emit the gate token, the operator must go back to S5.5 Sub-task A, find the authoritative line, and reproduce it — which is the copy action itself. The gate converts data flow from an inferred obligation into a precondition for advancement. Prediction: a blocking gate at S6.5 eliminates Summary-site re-derivation because the act of unlocking S7 requires the copy to have occurred.

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

#### S5.5 — Taxonomy Census (mandatory interstitial — do not skip)

**Sub-task A — Mechanism distribution tally**

Walk findings in order. Tally each `mechanism-type:` token. Emit on its own line:

```
mechanism-distribution: {type}:{count} {type}:{count} ...
```

If no findings: `mechanism-distribution: (none — contract satisfied)`

**Sub-task B — Group-candidate staging**

For each candidate Patterns group:

```
group-candidate-N: findings=[F-NN, F-MM, ...] mechanism-type-shared={type token | mixed} rationale={one sentence}
```

Emit: `[TAXONOMY-CENSUS-COMPLETE | distribution-tokens:N | group-candidates:M]`

#### S5.6 — Gate Closure

```
[EXPECTED-RESOLVED | gate-clauses:N | clauses-resolved:M | phase:2-complete]
```

---

**GATE S6.5 — Summary Pre-flight (blocking)**

Do not write the `## Summary` section header until this gate token is emitted.

Locate the `mechanism-distribution:` line from S5.5 Sub-task A above. Copy it exactly as written. Emit:

```
[SUMMARY-PREFLIGHT | mechanism-distribution-confirmed: {paste the mechanism-distribution line here, verbatim} | source:S5.5-Sub-task-A | gate:open]
```

The gate token `[SUMMARY-PREFLIGHT ... gate:open]` unlocks S7. A Summary written without this gate token fails C-33. A Summary whose `mechanism-distribution:` value differs from the value inside this gate token fails C-33.

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
mechanism-type-shared: {copy verbatim from group-candidate-1 in S5.5 Sub-task B}
root-cause: {copy from F-NN root-cause-hypothesis}
fix-strategy: {one sentence}
```

**Multiple findings:**

```
pattern-N: {title}
findings: [F-NN, F-MM, ...]
mechanism-type-shared: {copy verbatim from group-candidate-N in S5.5 Sub-task B}
root-cause: {unified if single type; per-cause sentences if mixed}
fix-strategy: {one sentence per root cause}
```

#### S7 — Summary

Gate S6.5 must be emitted before this section.

```
clauses-committed: N
clauses-resolved: M
severity-breakdown: breaking:{X} degraded:{Y} cosmetic:{Z}
mechanism-distribution: {copy from [SUMMARY-PREFLIGHT] gate token above — same value, no recount}
assessment: {one sentence}
```

The `mechanism-distribution:` value in Summary must match the value in the `[SUMMARY-PREFLIGHT]` gate token exactly.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Combination: Phrasing Register + Output Format (C-33 + C-34 Dual)

**axis:** phrasing-register + output-format
**hypothesis:** C-33 closes the Summary consumption gap: the operator must copy `mechanism-distribution:` from S5.5 Sub-task A rather than re-deriving it. C-34 closes the Patterns traceability gap: each `pattern-N:` entry must carry a `source: group-candidate-N` back-reference. These are independent derivation sites — one in S7 (Summary), one in S6 (Patterns). V-01 addresses C-33 via a named copy directive in the Summary instruction; V-02 addresses C-34 via a named field in the branch template. The axes do not overlap: the copy-forward directive governs Summary behavior, the `source:` field governs Patterns format. Combining them closes both gaps without interference. The combined prompt adds two focused structural changes to the R11 census baseline: a named copy-from directive in the Summary instruction and a required `source:` field in the Multi-pattern template. Prediction: V-04 scores full credit on both C-33 and C-34 without degrading C-29 through C-32, because the mechanism for each criterion is added at a different lifecycle site.

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

Every element must appear. Silent omission fails coverage.

If no deviations: write `## Diff — Contract satisfied. No findings.`

#### S5 — Findings

For each deviation, write a finding block:

```
F-NN: {title}
severity: breaking | degraded | cosmetic
mechanism-type: field-mapping | serialization-path | conditional-branch | lifecycle-event | type-coercion | cardinality-violation | ordering-constraint | missing-field
root-cause-hypothesis: {one sentence — name the mechanism, not the symptom}
spec-ref: {section or clause}
```

Severity definitions:
- `breaking` — consumer cannot function correctly
- `degraded` — guarantee violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness

Self-test: if `root-cause-hypothesis` could be written from the diff alone, it is a symptom — revise to name a component, path, or condition.

Write: `[FINDINGS-COMPLETE | count:N]`

---

### ROLE: Connectors Contract Expert (resumes for S5.5 and closure)

**You own the Taxonomy Census. This is contract-level synthesis, not formatting.**

#### S5.5 — Taxonomy Census (mandatory interstitial — do not skip to S6 until both sub-tasks complete)

**Sub-task A — Mechanism distribution tally**

Walk findings F-01 through F-NN in order. Read each `mechanism-type:` token. Tally.

Emit this line — it is the authoritative value consumed by Summary:

```
mechanism-distribution: {type}:{count} {type}:{count} ...
```

If no findings: `mechanism-distribution: (none — contract satisfied)`

**Sub-task B — Group-candidate staging**

For each candidate Patterns group, emit a staging line before any branch template in S6 is filled. Include rationale for the grouping decision:

```
group-candidate-N: findings=[F-NN, F-MM, ...] mechanism-type-shared={type token | mixed} rationale={one sentence — why these findings share a root or require independent fixes}
```

- `mechanism-type-shared` = single type token if all findings in the group share the same type
- `mechanism-type-shared` = `mixed` if the group spans more than one type token
- `rationale` must name the shared component, path, or condition — not restate the type token

One staging line per candidate group. Emit:

```
[TAXONOMY-CENSUS-COMPLETE | distribution-tokens:N | group-candidates:M | census-author:Connectors-Contract-Expert]
```

#### S5.6 — Gate Closure

```
[EXPECTED-RESOLVED | gate-clauses:N | clauses-resolved:M | phase:2-complete]
```

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

**Multiple findings:**

For each group from S5.5 Sub-task B, fill the template below. The `source:` field names the staging line this entry was derived from — it is a required field. Do not re-derive `mechanism-type-shared:` at template-fill time; copy it from the named staging line.

```
pattern-N: {title}
findings: [F-NN, F-MM, ...]
source: group-candidate-N
mechanism-type-shared: {copy verbatim from the source group-candidate-N staging line in S5.5 Sub-task B}
root-cause: {unified root cause if single type; one sentence per independent cause if mixed}
fix-strategy: {one sentence per root cause}
```

Audit rule: for every `pattern-N:` entry, verify that (a) `source:` names a `group-candidate-N` from S5.5 Sub-task B, and (b) `mechanism-type-shared:` matches that staging line's value exactly. A mismatch is a C-34 violation.

#### S7 — Summary

**Copy-forward step (required before writing body):** Locate the `mechanism-distribution:` line emitted by S5.5 Sub-task A above. Copy that line verbatim. Paste it into the `mechanism-distribution:` field below. This is a copy operation — do not recount findings.

```
clauses-committed: N
clauses-resolved: M
severity-breakdown: breaking:{X} degraded:{Y} cosmetic:{Z}
mechanism-distribution: {VERBATIM-COPY from [S5.5 Sub-task A · mechanism-distribution] — exact text, no recount}
assessment: {one sentence}
```

The `mechanism-distribution:` line must be the exact text from S5.5 Sub-task A. If a fresh count would produce a different value, the S5.5 value is authoritative.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — Role Sequence + Lifecycle Emphasis + Output Format: Named Census Artifacts with Downstream Consumption by Name

**axis:** role-sequence + lifecycle-emphasis + output-format
**hypothesis:** In all prior rounds the Connectors Contract Expert nominally owns S5.5, but downstream consumption sites (S6 Patterns templates and S7 Summary) are not structurally linked to the Expert's census output as a named artifact. The data flow is: Expert produces → operator is told to copy → operator may re-derive instead. The failure mode is at the consumption site, not the production site. Adding role-enforced handoffs changes the structure: the Expert produces two named census artifacts — `[CENSUS-ARTIFACT-A: mechanism-distribution]` and `[CENSUS-ARTIFACT-B: group-candidate-N staging]` — and every downstream consumer identifies these artifacts by name before using their values. The Singleton and Multi-pattern branch templates reference `[CENSUS-ARTIFACT-B · group-candidate-N]` by name; the Summary references `[CENSUS-ARTIFACT-A · mechanism-distribution]` by name. Named artifact consumption makes re-derivation visible: if the operator computes a value rather than copying from the named artifact, the artifact reference is missing and the copy chain is broken. The `source:` field in each `pattern-N:` entry and the `VERBATIM-COPY` directive in Summary are both consequences of the named-artifact architecture, not independent interventions. Prediction: role-owned named artifacts with downstream named consumption eliminate re-derivation at both C-33 (Summary) and C-34 (Patterns) sites, and the named reference structure enables audit chain verification without re-running the census.

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
root-cause-hypothesis: {one sentence — name the component, path, or condition; not a symptom restatement}
spec-ref: {section or clause}
```

Severity:
- `breaking` — consumer cannot function correctly
- `degraded` — guarantee violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness

Self-test: the hypothesis requires system knowledge to write. If it could come from the diff alone, revise.

Write: `[FINDINGS-COMPLETE | count:N]`

---

### ROLE: Connectors Contract Expert (resumes — Census Owner)

You produced the Expected Output. You now perform the census. The findings are Automate's execution report; the synthesis is yours.

You will produce two named census artifacts that downstream sections consume by reference. Do not skip to S6 until both artifacts are emitted.

#### S5.5 — Taxonomy Census

**Sub-task A — Mechanism distribution tally**

Walk findings F-01 through F-NN in order. Read each `mechanism-type:` token. Tally. If a token appears misclassified for this contract domain, note a correction.

Emit the artifact — bounded by open and close tags:

```
[CENSUS-ARTIFACT-A]
mechanism-distribution: {type}:{count} {type}:{count} ...
[/CENSUS-ARTIFACT-A]
```

Correction format: `mechanism-distribution: field-mapping:2[1 reclassified from serialization-path] conditional-branch:1`

If no findings: `mechanism-distribution: (none — contract satisfied)`

**Sub-task B — Group-candidate staging**

For each candidate Patterns group, emit a staging entry in the artifact:

```
[CENSUS-ARTIFACT-B]
group-candidate-1: findings=[F-NN, F-MM, ...] mechanism-type-shared={type token | mixed} rationale={one sentence — shared root cause or independent symptoms}
group-candidate-2: findings=[F-PP, ...] mechanism-type-shared={type token | mixed} rationale={one sentence}
[/CENSUS-ARTIFACT-B]
```

- `mechanism-type-shared` = single type token if all findings share it; `mixed` otherwise
- `rationale` must name the shared mechanism — not restate the type token
- One entry per candidate group
- If only one finding: `group-candidate-1: findings=[F-NN] mechanism-type-shared={type} rationale={one sentence}`
- If no findings: `group-candidate: (none)`

Emit: `[TAXONOMY-CENSUS-COMPLETE | artifact-A:sealed | artifact-B:sealed | census-author:Connectors-Contract-Expert]`

#### S5.6 — Gate Closure

```
[EXPECTED-RESOLVED | gate-clauses:N | clauses-resolved:M | phase:2-complete]
```

---

### ROLE: Connectors Contract Expert (continues)

#### S6 — Patterns

Branch on finding count. All branch templates consume from named census artifacts — do not re-derive values at template-fill time.

**Zero findings:**

```
no-pattern-confirmation: contract verified — all N clauses resolved with zero deviations
```

**Singleton finding (exactly one F-NN):**

```
pattern-1: {title}
single-finding-ref: F-NN
source: [CENSUS-ARTIFACT-B · group-candidate-1]
mechanism-type-shared: {copy verbatim from [CENSUS-ARTIFACT-B · group-candidate-1] mechanism-type-shared value}
root-cause: {copy from F-NN root-cause-hypothesis}
fix-strategy: {one sentence}
```

**Multiple findings:**

For each `group-candidate-N` entry in `[CENSUS-ARTIFACT-B]`, fill one template entry. The `source:` field is required and names the census artifact entry this template was derived from:

```
pattern-N: {title}
findings: [F-NN, F-MM, ...]
source: [CENSUS-ARTIFACT-B · group-candidate-N]
mechanism-type-shared: {copy verbatim from [CENSUS-ARTIFACT-B · group-candidate-N] mechanism-type-shared value}
root-cause: {unified if single type; one sentence per cause if mixed}
fix-strategy: {one sentence per root cause}
```

Audit rule: every `pattern-N:` entry must have a `source:` field naming a `[CENSUS-ARTIFACT-B · group-candidate-N]`. A `mechanism-type-shared:` value that differs from the named artifact entry is a C-34 derivation violation.

#### S7 — Summary

Consume `[CENSUS-ARTIFACT-A]` by reference. Do not re-derive the distribution.

```
clauses-committed: N
clauses-resolved: M
severity-breakdown: breaking:{X} degraded:{Y} cosmetic:{Z}
mechanism-distribution: {VERBATIM-COPY from [CENSUS-ARTIFACT-A · mechanism-distribution] — exact text from the artifact}
assessment: {one sentence}
```

The `mechanism-distribution:` line is a verbatim copy of the value inside `[CENSUS-ARTIFACT-A]`. If the value in Summary differs from the artifact, the artifact is authoritative. Do not recount findings.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## Evaluation Notes

**Recommended evaluation order:**

1. **V-04 first** — highest-information test: two independent C-33 and C-34 mechanisms at different lifecycle sites (Summary directive + Patterns `source:` field); if V-04 scores full credit on both, the combination is sufficient and single-axis variants are analyzed for contribution
2. **V-05 second** — ceiling test: named-artifact architecture is a superset of V-04 mechanisms; if V-05 scores higher, role ownership and bounded artifact tags add independent value beyond the V-04 directive + field approach
3. **V-03 third** — isolates whether a blocking gate adds value over a named directive for C-33; if V-03 ties V-01, the gate adds no marginal value and V-01's directive is sufficient
4. **V-01 fourth** — single-axis baseline for C-33; establishes the minimum intervention needed
5. **V-02 fifth** — single-axis baseline for C-34; establishes the minimum intervention needed

**Critical criterion tests for this round:**

- **C-33** (copy-forward mandate): Is `mechanism-distribution:` in Summary the verbatim text from S5.5 Sub-task A, or a re-derived value? The test is a character-level comparison, not a semantic comparison. A correct distribution that was re-derived fails C-33.
- **C-34** (staging-to-template reference chain): Does each `pattern-N:` entry name a specific `group-candidate-N` from S5.5 Sub-task B? Is `mechanism-type-shared:` traceable to that staging line without a fresh derivation? A pattern entry that computes type alignment independently at template-fill time fails C-34.

**Failure mode to watch:**
V-01 and V-03 both target C-33 at the Summary site via different enforcement modes (directive vs. gate). If V-01 scores full C-33 credit, the gate in V-03 is redundant overhead. If V-01 fails and V-03 passes, the gate is the necessary mechanism. V-04 combines V-01's directive with V-02's `source:` field — if V-04 passes C-33 and C-34 while V-01 and V-02 each score partial credit alone, the combination is synergistic; if V-04 scores the same as V-01 + V-02 separately, the interventions are additive rather than synergistic.
