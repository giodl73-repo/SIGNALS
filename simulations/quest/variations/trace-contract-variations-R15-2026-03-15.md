Now I have everything I need. Writing the five complete variations.

---

# trace-contract Variate — Round 15

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v15 (C-08–C-41; denominator /34; total max 136)
**Baseline:** R14 V-05 passes C-37 and C-38; C-39, C-40, C-41 absent from v14 rubric — added now as scored criteria
**Target criteria:**
- **C-39** — Schema co-requirement as structural field constraint: `census-distribution:` and `gate-provenance:` declared as co-required sibling fields in a named gate token schema, detectable by field inspection without reading prose
- **C-40** — Formal imperative as execution-method specification: all copy-forward and amendment-path obligations stated as named executable commands (`Bind:`, `Assert:`, `Prohibit:`) auditable by structural inspection of the instruction
- **C-41** — Role ownership of attestation and witness falsifiability: gate execution protocol assigns attestation to census owner by role name; assigns independent character-for-character verification to a distinct witness role; no single role satisfies both

---

## Round 15 Variation Map

| Variation | Axis | C-39 | C-40 | C-41 | Notes |
|-----------|------|------|------|------|-------|
| V-01 | Output format — named gate token schema with explicit required-fields manifest; co-requirement declared as schema property | PASS | PARTIAL | PARTIAL | Single-axis: schema header declares `census-distribution` and `gate-provenance` as co-required siblings (C-39 PASS); Bind: used for census-distribution but amendment-path obligations remain prose (C-40 PARTIAL); Automate witness present but no role-name separation of attestation from verification (C-41 PARTIAL) |
| V-02 | Phrasing register — full formal imperative: every copy-forward and amendment obligation stated as Bind:/Assert:/Prohibit: command | PARTIAL | PASS | PARTIAL | Single-axis: Bind:/Assert: cover census-distribution and gate-provenance (C-40 PASS); gate token fields are correctly emitted but co-requirement not declared as a named schema structure — fields are present by instruction, not by schema property (C-39 PARTIAL); role-name separation absent (C-41 PARTIAL) |
| V-03 | Role sequence — two-party gate protocol: census owner (by role name) attests; Automate Witness (named separately) performs character-for-character comparison; no single role satisfies both | PARTIAL | PARTIAL | PASS | Single-axis: two roles named, responsibilities non-overlapping (C-41 PASS); gate-provenance emitted correctly (C-39 PARTIAL — adjacent but not schema-declared co-required); Bind: used for census-distribution but amendment path is prose (C-40 PARTIAL) |
| V-04 | Output format + phrasing register — named schema co-requirement combined with full Bind:/Assert:/Prohibit: imperative chain | PASS | PASS | PARTIAL | Combination: schema declares co-required sibling fields (C-39 PASS); all copy-forward and amendment obligations in formal imperative (C-40 PASS); Automate witness present but attestation and witness share the same S6.5 block without role-name separation of attestation function (C-41 PARTIAL) |
| V-05 | Output format + phrasing register + role sequence — schema co-requirement + full formal imperative + two-party attestation protocol | PASS | PASS | PASS | Combination: all three axes converge; schema declares co-required fields (C-39); Bind:/Assert:/Prohibit: cover all obligations (C-40); census owner attests by role name, Automate Witness verifies character-for-character independently (C-41) |

---

## V-01 — Output Format: Named Gate Token Schema with Co-Required Fields

**axis:** output-format — S6.5 gate token declared as a named schema (`GateTokenSchema: S6.5-CENSUS-GATE`) with an explicit `required-fields:` manifest listing `census-distribution` and `gate-provenance` as co-required siblings at fixed schema position; the schema header precedes all fill instructions so that field presence is a schema property, not an authoring convention inferred from prose

**hypothesis:** In R14 V-02 and V-04, `census-distribution:` and `gate-provenance:` appear as adjacent fields in the gate block and both are correctly emitted. What they lack is a declared schema relationship: nothing in the prompt asserts that the two fields are co-required as a structural pair. An author who names Sub-task A in the provenance-binding prose but omits the `gate-provenance:` field does not visibly break any schema rule — the instruction says "emit this field" but does not declare it as a co-required sibling of `census-distribution:`. The schema-header approach changes this: a named `GateTokenSchema` with `required-fields: [census-distribution, gate-provenance, gate-status]` and a co-requirement annotation makes omitting either field a structural violation detectable by inspecting the schema manifest, without reading the authoring prose. Prediction: C-39 PASS — the schema declares both fields as co-required siblings; omitting either is a schema violation independent of prose. C-40 PARTIAL — `Bind:` is used for the census-distribution copy-forward step but amendment-path obligations at Sub-task B remain in prose form. C-41 PARTIAL — Automate witness is present and functions correctly but the attestation function is not assigned to the census owner by explicit role name; both steps occur within a shared S6.5 block.

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

These staging lines are the authoritative per-group record.

Write: `[TAXONOMY-CENSUS-COMPLETE | artifact-A:sealed | artifact-B:sealed | census-author:Connectors-Contract-Expert]`

---

### ROLE: Connectors Contract Expert (continues — Patterns Author)

#### S6 — Patterns

Branch on finding count. All branch templates consume from Sub-task B staging lines — do not re-derive `mechanism-type-shared:` at template-fill time.

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
root-cause: {copy from F-NN root-cause-hypothesis}
fix-strategy: {one sentence}
```

**Multiple findings:**
```
pattern-N: {title}
findings: [F-NN, F-MM, ...]
source: group-candidate-N
mechanism-type-shared: {verbatim from group-candidate-N mechanism-type-shared value}
root-cause: {unified if single type; one sentence per cause if mixed}
fix-strategy: {one sentence per root cause}
```

`mechanism-type-shared:` at each fill site must equal the value on the named `group-candidate-N` staging line. A value that differs from the staging line is a derivation violation — correct the staging line at Sub-task B and re-propagate; do not patch the fill site.

---

### S6.5 — Census Gate

**Gate token schema (declared before fill):**

```
GateTokenSchema: S6.5-CENSUS-GATE
required-fields:
  - census-distribution    # REQUIRED: verbatim copy of Sub-task A mechanism-distribution line
  - gate-provenance        # REQUIRED: named source of census-distribution; co-required with census-distribution
  - gate-status            # REQUIRED: LOCKED | OPEN
co-requirement: census-distribution and gate-provenance are co-required sibling fields.
  A gate token that includes one but omits the other is a schema violation.
  Field presence is detectable by inspecting the field manifest above.
  Naming the source in authoring prose without emitting the gate-provenance field does not satisfy this schema.
```

**Step 1 — Verification table**

Populate one row per pattern entry after all pattern entries are complete:

| pattern-N | source | mechanism-type-shared (fill site) | mechanism-type-shared (from staging) | verdict |
|-----------|--------|------------------------------------|--------------------------------------|---------|
| pattern-1 | group-candidate-1 | {value at fill site} | {value from staging line} | PASS / FAIL |

A row holds FAIL when the fill-site value does not match the staging-line value.

**Step 2 — Provenance-binding sub-step**

Locate the `mechanism-distribution:` line from S5.5 Sub-task A. This is the authoritative census output. Do not recount; do not re-derive.

Bind: `census-distribution` := verbatim copy of the Sub-task A `mechanism-distribution:` line.

Emit the gate token conforming to `GateTokenSchema: S6.5-CENSUS-GATE`:

```
S6.5-CENSUS-GATE:
  census-distribution: {verbatim Sub-task A mechanism-distribution value}
  gate-provenance: S5.5-Sub-task-A
  gate-status: LOCKED
```

Both `census-distribution` and `gate-provenance` must be present as named fields. Omitting either field is a schema violation against `GateTokenSchema: S6.5-CENSUS-GATE`.

**Step 3 — Automate witness**

Confirm that the `census-distribution:` value in the gate token matches the `mechanism-distribution:` line from Sub-task A character-for-character.

If match: `automate-witness: CONFIRMED — census-distribution encodes Sub-task A output faithfully`

If mismatch: `automate-witness: MISMATCH — gate-status remains LOCKED; Expert must re-emit from Sub-task A verbatim`

**Step 4 — Verdict-gate closure**

If any verification table row holds FAIL: `gate-status` remains LOCKED. The document may not proceed to `## Summary`. To advance: correct the source grouping in Sub-task B. Do not patch the pattern fill site.

When all rows hold PASS and `automate-witness: CONFIRMED`:

```
S6.5-CENSUS-GATE:
  census-distribution: {verbatim}
  gate-provenance: S5.5-Sub-task-A
  gate-status: OPEN
```

Write: `[GATE-OPEN | census-distribution:{value} | schema:GateTokenSchema-S6.5-CENSUS-GATE | verified-by:Automate]`

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

`mechanism-distribution:` is a verbatim copy of the `census-distribution:` value from the gate token. Do not recount. The gate token is authoritative for Summary consumption.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Phrasing Register: Full Formal Imperative for All Obligations

**axis:** phrasing-register — every copy-forward obligation and amendment-path rule stated as a named executable command (`Bind:`, `Assert:`, `Prohibit:`); no obligation is stated as behavioral guidance or prose convention; the instruction is auditable by structural inspection of command tokens without reading surrounding prose

**hypothesis:** In R14 V-04, `Bind:` is used for the census-distribution copy step and `Block:` for the verdict-gate closure — two obligations receive formal imperative form. The remaining obligations (amendment path for FAIL rows, Summary consumption rule, prohibition on fill-site patching) are stated in prose: "correct the source grouping," "do not patch the fill site," "the gate token is authoritative." Prose obligations create a behavioral hedge: "do not patch the fill site" allows an author to comply with the letter while still producing a functionally equivalent patch at Sub-task B. A `Prohibit:` command eliminates the hedge by naming the forbidden action as an executable constraint. The full-imperative hypothesis is that converting every obligation — not just the binding step — into a named command makes each constraint auditable without inferring behavioral intent. Prediction: C-40 PASS — all copy-forward and amendment-path obligations are `Bind:`, `Assert:`, or `Prohibit:` commands; the complete obligation chain is auditable by scanning command tokens. C-39 PARTIAL — `census-distribution` and `gate-provenance` are correctly emitted as adjacent fields, but the co-requirement is stated as a `Prohibit:` command rather than a named schema structure; detectable by instruction inspection but not by gate-token field inspection alone. C-41 PARTIAL — Automate witness is present and named, but the attestation step is not assigned to the census owner by explicit role-name ownership; both steps reside in a shared S6.5 block.

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

**Hypothesis self-test:** if the hypothesis could be derived from the diff alone without implementation knowledge, revise it.

Write: `[FINDINGS-COMPLETE | count:N]`

---

### ROLE: Connectors Contract Expert (resumes — Census Owner)

#### S5.5 — Taxonomy Census

**Obligation chain — read before executing Sub-task A or B:**

```
Bind: census-distribution := Sub-task A mechanism-distribution verbatim
  — census-distribution has exactly one production site: Sub-task A
  — Prohibit: re-deriving census-distribution from finding list at any downstream site
  — Prohibit: re-deriving census-distribution from verification table at S6.5
  — Prohibit: re-deriving census-distribution from Summary at S7

Assert: mechanism-type-shared at each pattern fill site = verbatim value from named group-candidate-N staging line
  — Prohibit: fill-site patch of mechanism-type-shared without amending the staging line at Sub-task B
  — Prohibit: writing a mechanism-type-shared value at pattern fill site that differs from its named source

Assert: gate-provenance: S5.5-Sub-task-A is present as a named field in the S6.5-CENSUS-GATE token
  — This field names the sole authoritative source of census-distribution
  — Prohibit: omitting gate-provenance from the gate token regardless of prose description of the source

Prohibit: advancing to ## Summary while any verification table row at S6.5 holds FAIL
  — Resolution path: amend the Sub-task B staging line; re-propagate to the pattern fill site
  — Prohibit: patching the pattern fill site directly without amending the staging line
```

**Sub-task A — Mechanism-type column scan**

Walk findings F-01 through F-NN in order. Read each `mechanism-type:` token. Tally each token.

Emit:
```
mechanism-distribution: {type}:{count} {type}:{count} ...
```

`Bind: census-distribution := this line verbatim` — this is the sole production site.

If no findings: `mechanism-distribution: (none — contract satisfied)`

**Sub-task B — Group-candidate staging**

For each candidate Patterns group, emit one staging line:

```
group-candidate-N: findings=[F-NN, F-MM, ...] mechanism-type-shared={type token | mixed} rationale={one sentence — shared root cause}
```

`Assert: mechanism-type-shared value at each downstream fill site = verbatim value from this staging line.`

Write: `[TAXONOMY-CENSUS-COMPLETE | artifact-A:sealed | artifact-B:sealed | census-author:Connectors-Contract-Expert]`

---

### ROLE: Connectors Contract Expert (continues — Patterns Author)

#### S6 — Patterns

All branch templates consume from Sub-task B staging lines. `Prohibit: re-deriving mechanism-type-shared at template-fill time.`

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
root-cause: {copy from F-NN root-cause-hypothesis}
fix-strategy: {one sentence}
```

**Multiple findings:**
```
pattern-N: {title}
findings: [F-NN, F-MM, ...]
source: group-candidate-N
mechanism-type-shared: {verbatim from group-candidate-N mechanism-type-shared value}
root-cause: {unified if single type; one sentence per cause if mixed}
fix-strategy: {one sentence per root cause}
```

---

### S6.5 — Census Gate

All pattern entries are complete. Execute steps in order. `Prohibit: writing ## Summary before step 4 completes.`

**Step 1 — Verification table**

| pattern-N | source | mechanism-type-shared (fill site) | mechanism-type-shared (from staging) | verdict |
|-----------|--------|------------------------------------|--------------------------------------|---------|
| pattern-1 | group-candidate-1 | {fill-site value} | {staging-line value} | PASS / FAIL |

`Assert: verdict = PASS iff fill-site value = staging-line value exactly.`

**Step 2 — Provenance-binding**

```
Bind: census-distribution := verbatim Sub-task A mechanism-distribution line
Assert: gate-provenance: S5.5-Sub-task-A is present as a named field in the emitted gate token
Prohibit: omitting gate-provenance from the gate token
```

Emit:
```
S6.5-CENSUS-GATE:
  census-distribution: {Bind: verbatim Sub-task A value}
  gate-provenance: S5.5-Sub-task-A
  gate-status: LOCKED
```

**Step 3 — Automate witness**

`Assert: census-distribution in gate token = mechanism-distribution line from Sub-task A, character-for-character.`

If confirmed: `automate-witness: CONFIRMED`
If mismatch: `automate-witness: MISMATCH — gate-status remains LOCKED; Prohibit: advancing until Expert re-emits from Sub-task A verbatim`

**Step 4 — Verdict-gate closure**

`Assert: all verification table rows hold PASS before gate-status transitions to OPEN.`
`Prohibit: advancing to ## Summary while any row holds FAIL.`
Resolution path when FAIL present: `amend Sub-task B staging line; re-propagate to pattern fill site; Prohibit: patching fill site directly.`

When all rows PASS and `automate-witness: CONFIRMED`:
```
S6.5-CENSUS-GATE:
  census-distribution: {verbatim}
  gate-provenance: S5.5-Sub-task-A
  gate-status: OPEN
```

Write: `[GATE-OPEN | census-distribution:{value} | verified-by:Automate]`

---

### ROLE: Connectors Contract Expert (continues — Summary Author)

*Reachable only after `[GATE-OPEN]`.*

#### S7 — Summary

```
clauses-committed: N
clauses-resolved: M
severity-breakdown: breaking:{X} degraded:{Y} cosmetic:{Z}
mechanism-distribution: {Bind: verbatim census-distribution value from S6.5-CENSUS-GATE token}
assessment: {one sentence}
```

`Bind: mechanism-distribution := census-distribution value from S6.5-CENSUS-GATE token verbatim.`
`Prohibit: recounting findings at this site.`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Role Sequence: Two-Party Attestation Protocol

**axis:** role-sequence — S6.5 split into two non-overlapping ownership zones: the census owner (Connectors Contract Expert, named by role) executes the provenance-binding sub-step and emits the attestation claim; a distinct Automate Witness role performs character-for-character comparison and records the verification result; no single role can satisfy both obligations; the gate token is auditable as a two-party claim-plus-proof structure

**hypothesis:** In R14 V-05, the Expert owns the provenance-binding sub-step and Automate acts as an encoding witness — but both steps reside in a shared S6.5 block where the role boundary is signaled only by a parenthetical annotation. The attestation and the verification are structurally adjacent without a non-overlap guarantee: a single author could write both the Expert's attestation claim and the Automate witness confirmation in sequence without any structural barrier. The two-party protocol hypothesis is that separating the gate into two named sub-blocks with exclusive ownership — `ATTESTATION: Connectors-Contract-Expert` and `VERIFICATION: Automate-Witness` — creates a non-overlap constraint: only the Expert can write the attestation claim; only the Witness can write the verification result; neither can write the other's artifact. The gate token is then auditable as a claim authored by one role and a proof authored by a different role, at the gate boundary, without re-inspecting the findings section to verify provenance. Prediction: C-41 PASS — attestation assigned to census owner by explicit role name; verification assigned to a distinct witness role; non-overlapping responsibilities enforced by block ownership. C-39 PARTIAL — gate-provenance emitted correctly as a named field; co-requirement not declared as a named schema structure. C-40 PARTIAL — `Bind:` used for census-distribution; amendment-path obligations prose-stated.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors Contract Expert (Census Owner) · Automate · Automate Witness.

The Automate Witness is a distinct role from Automate. Automate runs the operation and produces findings. The Automate Witness performs gate-boundary verification only. These two functions must not be combined into a single role step.

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

You begin after `[EXPECTED-SEALED]`. Do not modify the Expected Output. Do not perform gate-boundary verification — that is the Automate Witness function.

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

**Hypothesis self-test:** if the hypothesis could be derived from the diff alone without implementation knowledge, revise it.

Write: `[FINDINGS-COMPLETE | count:N]`

---

### ROLE: Connectors Contract Expert (resumes — Census Owner)

#### S5.5 — Taxonomy Census

**Sub-task A — Mechanism-type column scan**

Walk findings F-01 through F-NN in order. Read each `mechanism-type:` token. Tally each token.

Emit:
```
mechanism-distribution: {type}:{count} {type}:{count} ...
```

This line is the authoritative census output. Sub-task A is the sole production site. Do not recompute at any downstream site.

If no findings: `mechanism-distribution: (none — contract satisfied)`

**Sub-task B — Group-candidate staging**

For each candidate Patterns group, emit one staging line:

```
group-candidate-N: findings=[F-NN, F-MM, ...] mechanism-type-shared={type token | mixed} rationale={one sentence — shared root cause}
```

Rules: `mechanism-type-shared` = single type if all findings share it; `mixed` otherwise. Rationale must name the mechanism, not restate the type token.

Write: `[TAXONOMY-CENSUS-COMPLETE | artifact-A:sealed | artifact-B:sealed | census-author:Connectors-Contract-Expert]`

---

### ROLE: Connectors Contract Expert (continues — Patterns Author)

#### S6 — Patterns

All templates consume from Sub-task B staging lines. Do not re-derive `mechanism-type-shared:` at template-fill time.

**Zero findings:**
```
no-pattern-confirmation: contract verified — all N clauses resolved with zero deviations
```

**Singleton / multiple findings** — fill as in baseline, consuming from `group-candidate-N` staging lines; `mechanism-type-shared:` at each fill site = verbatim value from the named staging line.

---

### S6.5 — Census Gate

This gate has two exclusive ownership zones. The zones must not be combined. No single role may write artifacts for both zones.

---

#### ATTESTATION ZONE — owned by: Connectors Contract Expert (Census Owner)

*Only the census owner executes this zone. The Automate Witness does not write here.*

**Step A1 — Verification table**

Populate one row per pattern entry:

| pattern-N | source | mechanism-type-shared (fill site) | mechanism-type-shared (from staging) | verdict |
|-----------|--------|------------------------------------|--------------------------------------|---------|
| pattern-1 | group-candidate-1 | {fill-site value} | {staging-line value} | PASS / FAIL |

A row holds FAIL when the fill-site value does not match the staging-line value.

**Step A2 — Provenance attestation**

Locate the `mechanism-distribution:` line from S5.5 Sub-task A. Do not recount. Do not re-derive.

As Census Owner: I attest that the `census-distribution:` value below is a verbatim copy of the Sub-task A `mechanism-distribution:` line. Re-derivation from the findings section or verification table is a role-boundary violation — only the census owner can attest their own Sub-task A output.

Emit:
```
S6.5-CENSUS-GATE:
  census-distribution: {verbatim Sub-task A mechanism-distribution value}
  gate-provenance: S5.5-Sub-task-A
  gate-status: LOCKED
census-owner-attestation: census-distribution is verbatim Sub-task A output — attested by Connectors-Contract-Expert
```

Write: `[ATTESTATION-COMPLETE | attested-by:Connectors-Contract-Expert | gate-status:LOCKED]`

---

#### VERIFICATION ZONE — owned by: Automate Witness

*Only the Automate Witness executes this zone. The Connectors Contract Expert does not write here.*

**Step V1 — Character-for-character comparison**

You have received the census-owner attestation above. Your function is falsification, not confirmation: determine independently whether the `census-distribution:` value in the gate token matches the `mechanism-distribution:` line emitted in S5.5 Sub-task A character-for-character.

Compare the two values. Do not infer; do not paraphrase. Match or no-match.

If match:
```
automate-witness-verification: CONFIRMED
comparison: census-distribution in gate token = Sub-task A mechanism-distribution line, character-for-character
witness-role: Automate-Witness (distinct from Automate operations role)
```

If mismatch:
```
automate-witness-verification: MISMATCH
discrepancy: {state the differing characters or tokens}
gate-status: remains LOCKED
resolution: Census Owner must re-emit gate token from Sub-task A verbatim; Automate Witness re-verifies after re-emission
```

**Step V2 — Verdict-gate closure**

If any verification table row holds FAIL: gate-status remains LOCKED. Document may not proceed to `## Summary`. Resolution: census owner must amend Sub-task B staging line and re-propagate to pattern fill site. Do not patch the fill site directly.

When all rows hold PASS and `automate-witness-verification: CONFIRMED`:

```
S6.5-CENSUS-GATE:
  census-distribution: {verbatim}
  gate-provenance: S5.5-Sub-task-A
  gate-status: OPEN
```

Write: `[GATE-OPEN | census-distribution:{value} | attested-by:Connectors-Contract-Expert | verified-by:Automate-Witness]`

---

### ROLE: Connectors Contract Expert (continues — Summary Author)

*Reachable only after `[GATE-OPEN]`.*

#### S7 — Summary

```
clauses-committed: N
clauses-resolved: M
severity-breakdown: breaking:{X} degraded:{Y} cosmetic:{Z}
mechanism-distribution: {verbatim copy of census-distribution: value from S6.5-CENSUS-GATE token}
assessment: {one sentence}
```

`mechanism-distribution:` is a verbatim copy of the `census-distribution:` value from the gate token. Do not recount. The gate token is authoritative.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Combined: Schema Co-Requirement + Full Formal Imperative

**axis:** output-format + phrasing-register — named gate token schema declaring `census-distribution` and `gate-provenance` as co-required sibling fields (C-39 axis from V-01) combined with full `Bind:`/`Assert:`/`Prohibit:` imperative chain covering all obligations (C-40 axis from V-02); the two axes are orthogonal and should not interfere: the schema declares structural co-presence, the imperative chain specifies the execution method for each obligation

**hypothesis:** V-01 establishes structural co-presence via schema declaration but leaves amendment-path obligations in prose. V-02 covers all obligations with formal imperatives but does not declare co-presence as a named schema property — field presence is detectable from the instruction's command chain but not from the gate token itself. Combining both axes should pass both C-39 and C-40: the schema manifest makes co-presence a structural property of the gate token (C-39); the `Bind:`/`Assert:`/`Prohibit:` commands make every execution obligation auditable without prose inference (C-40). The combination should not crowd: the schema declaration is a structural header; the imperative chain is an obligation list; they operate at different levels of the prompt without overlapping. C-41 PARTIAL predicted: Automate witness is present and named; the two-party structure functions correctly but attestation is not assigned to the census owner by explicit role-name ownership within a non-overlap protocol — both steps reside in a shared S6.5 block where the role boundary is not enforced structurally.

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

For each element in the Expected Output:
- `✓ {element} — satisfied`
- `F-NN — {element} — deviation (see findings)`

Every element must appear. No element may be silently omitted.

If no deviations: write `## Diff — Contract satisfied. No findings.`

#### S5 — Findings

```
F-NN: {title}
severity: breaking | degraded | cosmetic
mechanism-type: field-mapping | serialization-path | conditional-branch | lifecycle-event | type-coercion | cardinality-violation | ordering-constraint | missing-field
root-cause-hypothesis: {one sentence — name the component, path, or condition; not a symptom restatement}
spec-ref: {section or clause}
```

**Hypothesis self-test:** if the hypothesis could be derived from the diff alone without implementation knowledge, revise it.

Write: `[FINDINGS-COMPLETE | count:N]`

---

### ROLE: Connectors Contract Expert (resumes — Census Owner)

#### S5.5 — Taxonomy Census

**Obligation chain — binding before Sub-task A:**

```
Bind: census-distribution := Sub-task A mechanism-distribution verbatim
  — Sub-task A is the sole production site
  — Prohibit: re-deriving census-distribution from finding list at any downstream site
  — Prohibit: re-deriving census-distribution from verification table at S6.5
  — Prohibit: re-deriving census-distribution from Summary at S7

Assert: mechanism-type-shared at each pattern fill site = verbatim value from named group-candidate-N staging line
  — Prohibit: fill-site patch of mechanism-type-shared without amending Sub-task B staging line first
  — Prohibit: writing a mechanism-type-shared value that differs from its named staging-line source

Assert: gate-provenance: S5.5-Sub-task-A is present as a named field in the S6.5-CENSUS-GATE token
  — gate-provenance is co-required with census-distribution; both must appear as named fields
  — Prohibit: omitting gate-provenance from the gate token regardless of prose description

Prohibit: advancing to ## Summary while any verification table row at S6.5 holds FAIL
  — Resolution path: amend Sub-task B staging line; re-propagate to pattern fill site
  — Prohibit: patching pattern fill site directly without amending staging line
```

**Sub-task A — Mechanism-type column scan**

Walk findings F-01 through F-NN. Tally each `mechanism-type:` token.

Emit:
```
mechanism-distribution: {type}:{count} {type}:{count} ...
```

`Bind: census-distribution := this line verbatim` — sole production site. If no findings: `mechanism-distribution: (none — contract satisfied)`

**Sub-task B — Group-candidate staging**

```
group-candidate-N: findings=[F-NN, ...] mechanism-type-shared={type | mixed} rationale={shared root cause, not type-token restatement}
```

`Assert: mechanism-type-shared at each downstream fill site = verbatim value from this staging line.`

Write: `[TAXONOMY-CENSUS-COMPLETE | artifact-A:sealed | artifact-B:sealed | census-author:Connectors-Contract-Expert]`

---

### ROLE: Connectors Contract Expert (continues — Patterns Author)

#### S6 — Patterns

`Prohibit: re-deriving mechanism-type-shared at template-fill time.`

**Zero findings:** `no-pattern-confirmation: contract verified — all N clauses resolved with zero deviations`

**Singleton / multiple findings:**
```
pattern-N: {title}
findings: [F-NN, ...]
source: group-candidate-N
mechanism-type-shared: {verbatim from group-candidate-N}
root-cause: {unified if single type; one sentence per cause if mixed}
fix-strategy: {one sentence per root cause}
```

---

### S6.5 — Census Gate

**Gate token schema — declared before fill:**

```
GateTokenSchema: S6.5-CENSUS-GATE
required-fields:
  - census-distribution    # REQUIRED: Bind: verbatim Sub-task A mechanism-distribution line
  - gate-provenance        # REQUIRED: co-required with census-distribution; names the authoritative source
  - gate-status            # REQUIRED: LOCKED | OPEN
co-requirement: census-distribution and gate-provenance are co-required sibling fields.
  Omitting either field is a schema violation detectable by field-manifest inspection.
  Naming the source in prose without emitting gate-provenance does not satisfy GateTokenSchema.
  A gate token missing census-distribution violates the Bind: obligation at Sub-task A.
  A gate token missing gate-provenance violates the Assert: at S5.5 obligation chain.
```

**Obligation chain for S6.5:**

```
Assert: verification table row verdict = PASS iff fill-site value = staging-line value exactly
Prohibit: advancing to ## Summary while any row holds FAIL
  — Resolution: amend Sub-task B staging line; re-propagate; Prohibit: fill-site patch
Bind: census-distribution := verbatim Sub-task A mechanism-distribution (sole source; already bound at S5.5)
Assert: gate-provenance: S5.5-Sub-task-A present as named field (co-required with census-distribution)
Assert: automate-witness: CONFIRMED before gate-status transitions to OPEN
```

**Step 1 — Verification table**

| pattern-N | source | mechanism-type-shared (fill site) | mechanism-type-shared (from staging) | verdict |
|-----------|--------|------------------------------------|--------------------------------------|---------|
| pattern-1 | group-candidate-1 | {value} | {value} | PASS / FAIL |

**Step 2 — Provenance-binding**

Emit gate token conforming to `GateTokenSchema: S6.5-CENSUS-GATE`:

```
S6.5-CENSUS-GATE:
  census-distribution: {Bind: verbatim Sub-task A mechanism-distribution value}
  gate-provenance: S5.5-Sub-task-A
  gate-status: LOCKED
```

Both fields present as required by schema manifest. `Prohibit: emitting a gate token that omits either field.`

**Step 3 — Automate witness**

`Assert: census-distribution in gate token = Sub-task A mechanism-distribution line, character-for-character.`

If confirmed: `automate-witness: CONFIRMED — census-distribution encodes Sub-task A output faithfully`
If mismatch: `automate-witness: MISMATCH — gate-status remains LOCKED; Expert must re-emit from Sub-task A verbatim`

**Step 4 — Verdict-gate closure**

`Prohibit: writing gate-status: OPEN while any verification table row holds FAIL.`
`Prohibit: writing ## Summary before this step completes with all PASS and automate-witness: CONFIRMED.`

When all rows PASS and `automate-witness: CONFIRMED`:

```
S6.5-CENSUS-GATE:
  census-distribution: {verbatim}
  gate-provenance: S5.5-Sub-task-A
  gate-status: OPEN
```

Write: `[GATE-OPEN | census-distribution:{value} | schema:GateTokenSchema-S6.5-CENSUS-GATE | verified-by:Automate]`

---

### ROLE: Connectors Contract Expert (continues — Summary Author)

*Reachable only after `[GATE-OPEN]`.*

#### S7 — Summary

```
clauses-committed: N
clauses-resolved: M
severity-breakdown: breaking:{X} degraded:{Y} cosmetic:{Z}
mechanism-distribution: {Bind: verbatim census-distribution value from S6.5-CENSUS-GATE token}
assessment: {one sentence}
```

`Bind: mechanism-distribution := census-distribution value from gate token verbatim.`
`Prohibit: recounting findings at this site. Prohibit: re-deriving from findings section.`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — Combined: Schema Co-Requirement + Formal Imperative + Two-Party Attestation Protocol

**axis:** output-format + phrasing-register + role-sequence — all three synthesis axes converge; named gate token schema with co-required fields (C-39); full `Bind:`/`Assert:`/`Prohibit:` imperative chain covering all obligations (C-40); two-party attestation protocol with non-overlapping role ownership — census owner attests by role name, Automate Witness verifies character-for-character independently (C-41)

**hypothesis:** V-01 passes C-39 but leaves amendment-path obligations in prose and lacks a two-party non-overlap structure. V-02 passes C-40 but declares co-presence by instruction rather than schema, and does not separate attestation from verification by role boundary. V-03 passes C-41 but uses prose for amendment-path obligations and does not declare a named schema co-requirement. V-04 passes C-39 and C-40 but lacks the two-party non-overlap structure for C-41. V-05 combines all three without crowding by operating at three distinct structural levels: the schema manifest (structural property of the gate token output), the obligation chain (execution specification of the instruction), and the role protocol (ownership boundaries at S6.5). These levels do not overlap: the schema governs what fields must appear in the output; the obligation chain governs how each value must be computed and what transitions are forbidden; the role protocol governs who may write each artifact at the gate boundary. Three axes, three levels, zero conflicts. Prediction: C-39 PASS — `GateTokenSchema: S6.5-CENSUS-GATE` declares `census-distribution` and `gate-provenance` as co-required fields; omitting either is a schema violation detectable by manifest inspection. C-40 PASS — all copy-forward and amendment-path obligations are `Bind:`, `Assert:`, or `Prohibit:` commands; every constraint is auditable by scanning command tokens. C-41 PASS — `ATTESTATION ZONE: Connectors-Contract-Expert` owns the gate-token emission and census-owner attestation; `VERIFICATION ZONE: Automate-Witness` owns the character-for-character comparison; ownership is mutually exclusive; no single role satisfies both.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors Contract Expert (Census Owner) · Automate · Automate Witness.

**Role separation rule:** Automate executes the operation and produces findings (S3–S5). Automate Witness performs gate-boundary verification only (S6.5 Verification Zone). These two Automate functions are separate roles with non-overlapping artifact ownership. The Connectors Contract Expert owns all attestation claims. No single role may write artifacts for more than one ownership zone in S6.5.

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

You begin after `[EXPECTED-SEALED]`. Do not perform gate-boundary verification — that is the Automate Witness function.

#### S3 — Actual Output

Run or simulate the operation. Write a `## Actual Output` section: status code, full response body, headers, observable side effects.

#### S4 — Diff

For each element in the Expected Output:
- `✓ {element} — satisfied`
- `F-NN — {element} — deviation (see findings)`

Every element must appear. No element may be silently omitted.

If no deviations: write `## Diff — Contract satisfied. No findings.`

#### S5 — Findings

```
F-NN: {title}
severity: breaking | degraded | cosmetic
mechanism-type: field-mapping | serialization-path | conditional-branch | lifecycle-event | type-coercion | cardinality-violation | ordering-constraint | missing-field
root-cause-hypothesis: {one sentence — name the component, path, or condition; not a symptom restatement}
spec-ref: {section or clause}
```

**Hypothesis self-test:** if the hypothesis could be derived from the diff alone without implementation knowledge, revise it.

Write: `[FINDINGS-COMPLETE | count:N]`

---

### ROLE: Connectors Contract Expert (resumes — Census Owner)

#### S5.5 — Taxonomy Census

**Obligation chain — binding before Sub-task A:**

```
Bind: census-distribution := Sub-task A mechanism-distribution verbatim
  — Sub-task A is the sole production site for mechanism-distribution
  — Prohibit: re-deriving census-distribution from finding list at any downstream site
  — Prohibit: re-deriving census-distribution from verification table at S6.5
  — Prohibit: re-deriving census-distribution from Summary at S7

Assert: mechanism-type-shared at each pattern fill site = verbatim value from named group-candidate-N staging line
  — Prohibit: fill-site patch of mechanism-type-shared without amending Sub-task B staging line first
  — Prohibit: writing a mechanism-type-shared value at fill site that differs from its named source

Assert: gate-provenance: S5.5-Sub-task-A is present as a named field in the S6.5-CENSUS-GATE token
  — gate-provenance is co-required with census-distribution under GateTokenSchema: S6.5-CENSUS-GATE
  — Prohibit: omitting gate-provenance from the gate token regardless of prose source description
  — Prohibit: satisfying co-requirement by prose alone without emitting the gate-provenance field

Prohibit: advancing to ## Summary while any verification table row holds FAIL
  — Resolution: amend Sub-task B staging line; re-propagate; Prohibit: fill-site patch without staging-line amendment
```

**Sub-task A — Mechanism-type column scan**

Walk findings F-01 through F-NN. Tally each `mechanism-type:` token.

`Bind: census-distribution := this line verbatim`

Emit:
```
mechanism-distribution: {type}:{count} {type}:{count} ...
```

Sole production site. If no findings: `mechanism-distribution: (none — contract satisfied)`

**Sub-task B — Group-candidate staging**

```
group-candidate-N: findings=[F-NN, ...] mechanism-type-shared={type | mixed} rationale={shared root cause, not type-token restatement}
```

`Assert: mechanism-type-shared at each downstream fill site = verbatim value from this staging line.`

Write: `[TAXONOMY-CENSUS-COMPLETE | artifact-A:sealed | artifact-B:sealed | census-author:Connectors-Contract-Expert]`

---

### ROLE: Connectors Contract Expert (continues — Patterns Author)

#### S6 — Patterns

`Prohibit: re-deriving mechanism-type-shared at template-fill time.` All templates consume from Sub-task B staging lines.

**Zero findings:** `no-pattern-confirmation: contract verified — all N clauses resolved with zero deviations`

**Singleton / multiple findings:**
```
pattern-N: {title}
findings: [F-NN, ...]
source: group-candidate-N
mechanism-type-shared: {verbatim from group-candidate-N}
root-cause: {unified if single type; one sentence per cause if mixed}
fix-strategy: {one sentence per root cause}
```

---

### S6.5 — Census Gate

**Gate token schema — declared before any fill:**

```
GateTokenSchema: S6.5-CENSUS-GATE
required-fields:
  - census-distribution    # REQUIRED — Bind: verbatim Sub-task A mechanism-distribution
  - gate-provenance        # REQUIRED — co-required with census-distribution; value: S5.5-Sub-task-A
  - gate-status            # REQUIRED — LOCKED | OPEN
co-requirement:
  census-distribution and gate-provenance are co-required sibling fields.
  Omitting either field is a schema violation detectable by field-manifest inspection alone.
  Prose naming of the source without emitting gate-provenance does not satisfy GateTokenSchema.
  Assert: both fields present in every gate token emitted by this step.
  Prohibit: emitting a gate token that satisfies one field while omitting the other.
```

**S6.5 ownership zones — mutually exclusive:**

```
ATTESTATION ZONE   owned by: Connectors-Contract-Expert (Census Owner)
                   — produces: verification table, gate token emission, census-owner attestation
                   — Prohibit: Automate Witness writing in this zone

VERIFICATION ZONE  owned by: Automate-Witness
                   — produces: character-for-character comparison, witness verification record
                   — Prohibit: Connectors Contract Expert writing in this zone
```

---

#### ATTESTATION ZONE — Connectors Contract Expert (Census Owner)

`Prohibit: Automate Witness writing in this zone.`

**Step A1 — Verification table**

Populate one row per pattern entry:

| pattern-N | source | mechanism-type-shared (fill site) | mechanism-type-shared (from staging) | verdict |
|-----------|--------|------------------------------------|--------------------------------------|---------|
| pattern-1 | group-candidate-1 | {fill-site value} | {staging-line value} | PASS / FAIL |

`Assert: verdict = PASS iff fill-site value = staging-line value exactly.`

**Step A2 — Provenance attestation and gate token emission**

`Bind: census-distribution := verbatim Sub-task A mechanism-distribution line (sole source; already bound at S5.5).`
`Assert: gate-provenance: S5.5-Sub-task-A present as named field — co-required with census-distribution under GateTokenSchema.`
`Prohibit: emitting a gate token with census-distribution but without gate-provenance.`
`Prohibit: emitting a gate token with gate-provenance but without census-distribution.`

As Census Owner: I attest that the `census-distribution:` value below is a verbatim copy of the Sub-task A `mechanism-distribution:` line. Only the census owner can attest their own Sub-task A output — re-derivation by any other role or from any other source is a role-boundary violation.

Emit gate token conforming to `GateTokenSchema: S6.5-CENSUS-GATE`:

```
S6.5-CENSUS-GATE:
  census-distribution: {Bind: verbatim Sub-task A mechanism-distribution value}
  gate-provenance: S5.5-Sub-task-A
  gate-status: LOCKED
census-owner-attestation: census-distribution is verbatim Sub-task A output — attested by Connectors-Contract-Expert
```

Write: `[ATTESTATION-COMPLETE | attested-by:Connectors-Contract-Expert | gate-status:LOCKED]`

---

#### VERIFICATION ZONE — Automate Witness

`Prohibit: Connectors Contract Expert writing in this zone.`

**Step V1 — Character-for-character comparison**

You have received the census-owner attestation above. Your function is independent falsification: determine whether the `census-distribution:` value in the gate token matches the `mechanism-distribution:` line from S5.5 Sub-task A character-for-character. Do not infer from context. Do not paraphrase. Match or no-match on the literal character sequence.

`Assert: comparison is character-for-character, not semantic equivalence.`
`Prohibit: recording CONFIRMED based on semantic similarity without character-level match.`

If match:
```
automate-witness-verification: CONFIRMED
comparison-method: character-for-character
result: census-distribution in gate token = Sub-task A mechanism-distribution line exactly
witness-role: Automate-Witness (distinct from Automate operations role — Prohibit: combining these functions)
```

If mismatch:
```
automate-witness-verification: MISMATCH
discrepancy: {state the exact differing characters or tokens}
gate-status: remains LOCKED
resolution-required: Census Owner must re-emit gate token from Sub-task A verbatim; Automate Witness re-verifies after re-emission
Prohibit: advancing to ## Summary until CONFIRMED is recorded
```

**Step V2 — Verdict-gate closure**

`Assert: all verification table rows hold PASS before gate-status transitions to OPEN.`
`Prohibit: gate-status: OPEN while any row holds FAIL.`
`Prohibit: writing ## Summary before this step records CONFIRMED and all-PASS.`

Resolution when FAIL present: Census Owner must amend Sub-task B staging line. `Prohibit: fill-site patch without staging-line amendment.`

When all rows PASS and `automate-witness-verification: CONFIRMED`:

```
S6.5-CENSUS-GATE:
  census-distribution: {verbatim}
  gate-provenance: S5.5-Sub-task-A
  gate-status: OPEN
```

Write: `[GATE-OPEN | census-distribution:{value} | schema:GateTokenSchema-S6.5-CENSUS-GATE | attested-by:Connectors-Contract-Expert | verified-by:Automate-Witness]`

---

### ROLE: Connectors Contract Expert (continues — Summary Author)

*Reachable only after `[GATE-OPEN]` is written by Automate Witness.*

#### S7 — Summary

```
clauses-committed: N
clauses-resolved: M
severity-breakdown: breaking:{X} degraded:{Y} cosmetic:{Z}
mechanism-distribution: {Bind: verbatim census-distribution value from S6.5-CENSUS-GATE token}
assessment: {one sentence}
```

`Bind: mechanism-distribution := census-distribution value from gate token verbatim.`
`Prohibit: recounting findings.`
`Prohibit: re-deriving from findings section or verification table.`
The gate token is authoritative for Summary consumption.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## Predicted Discrimination Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-39 (schema co-requirement as structural field constraint) | **PASS** | PARTIAL | PARTIAL | **PASS** | **PASS** |
| C-40 (formal imperative as execution-method specification) | PARTIAL | **PASS** | PARTIAL | **PASS** | **PASS** |
| C-41 (role ownership + witness falsifiability) | PARTIAL | PARTIAL | **PASS** | PARTIAL | **PASS** |

**Single-axis isolation:** V-01 cracks C-39 only; V-02 cracks C-40 only; V-03 cracks C-41 only. V-04 cracks C-39 + C-40, leaving C-41 as the open axis. V-05 is the new ceiling.

**V-01 PARTIAL on C-40:** `Bind:` is used for census-distribution but amendment-path obligations at Sub-task B remain prose. The schema declares co-presence structurally but does not state `Prohibit: fill-site patch without staging-line amendment` as a command.

**V-02 PARTIAL on C-39:** All obligations are formal imperatives including `Prohibit: omitting gate-provenance` — this makes co-presence detectable by scanning command tokens. What it lacks is a named schema structure (`GateTokenSchema:`) that declares co-presence as a field-manifest property; the gate token itself does not carry a schema header that a reader can inspect to confirm co-requirement without reading the instruction.

**V-03 PARTIAL on C-40:** `Bind:` covers census-distribution; amendment-path obligations are prose. The role-sequence structure is the variation axis; formal imperative is not introduced.

**V-04 PARTIAL on C-41:** Both schema and imperative chains are present; Automate witness is correct. What it lacks is the explicit non-overlap ownership protocol — attestation and verification reside in a shared S6.5 block where both could be written by a single actor without a structural barrier.
