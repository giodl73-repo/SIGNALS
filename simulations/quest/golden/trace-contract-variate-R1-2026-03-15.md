# trace-contract Variate — Round 1

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v1 (C-01 through C-09; essential C-01–C-04)
**Round:** R1 — single-axis pass (3 single-axis + 1 role-sequence combo axis + 1 inertia-framing)

---

## Round 1 Variation Map

| Variation | Axis | What Changed | Hypothesis |
|-----------|------|--------------|------------|
| V-01 | role-sequence | Expert writes expected first, explicit handoff to Automate for actual | Temporal role separation reduces C-01 failures where expected output is inferred backward from observed behavior |
| V-02 | output-format | Findings as structured table with mandatory columns | Column-enforced format makes missing severity/spec-ref visible at the cell level, improving C-03 and C-04 pass rates |
| V-03 | lifecycle-emphasis | Diff phase expanded with explicit per-surface pass/fail requirements | Naming the three contract surfaces (success/error/edge) as required rows improves C-07 boundary coverage |
| V-04 | phrasing-register | Formal imperative with explicit DO NOT gates | Forbidden-form framing targets C-01 by naming the specific prohibited action (capturing actual before expected is complete) |
| V-05 | inertia-framing | Ad-hoc observation framed as status-quo competitor throughout | Framing each phase as an improvement over "run and observe" forces C-09 amendment/fix recommendations to argue against a concrete alternative |

---

## V-01 — Role Sequence: Expert-Before-Automate

**axis:** role-sequence
**hypothesis:** Explicit role separation — Connectors contract expert writes and commits the expected output section before the Automate persona captures any actual output — reduces C-01 (expected-first contract) failures. When both roles are described together without a handoff, operators infer expected output from observed behavior and label it "from spec." Requiring the expert to complete and commit their section before Automate activates prevents this contamination. C-04 (spec reference per finding) should also improve because the expert's pre-committed spec anchors are already in the document when Automate writes findings.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or flow name and environment}
**Input fixture:** {describe or paste the input state used for this trace}
**Spec source:** {spec file path and section — e.g., signal-trace-2026-03-14.md#trace-contract}

---

### ROLE: Connectors Contract Expert

You are a Connectors contract expert. Your job is to write the expected output — the contract — from the spec alone, before any operation is run. You do not observe behavior. You read the spec and state what the operation must produce.

**Step 1 — Contract identity**

At the top of the artifact, state:
- Operation name and method
- Connector or Automate context
- Input fixture summary (what state is being fed in)
- Spec section governing this operation's output contract

This section must be self-contained. A reader must be able to understand what is being tested without opening any external file.

**Step 2 — Expected output (the contract)**

Write every field, status code, response body shape, header, and side effect the spec requires for this operation and input fixture. For each expected element:
- State the element (e.g., `status: 200`, `body.items: array`, `X-Retry-After header: present when throttled`)
- Cite the spec clause that requires it (e.g., `spec §3.2: success response must include items array`)

Cover all contract surfaces the spec defines:
- Success path (nominal input, expected nominal output)
- Error path (invalid/missing input, expected error response)
- At least one edge case (empty collection, null field, auth failure, overflow value)

Label this section: `## Expected Output (Contract)`

**Step 3 — Commit**

When the Expected Output section is complete, write: `[CONTRACT COMMITTED — Automate begins here]`

Do not proceed to Step 4 until this line is present.

---

### ROLE: Automate

You are Automate. The contract expert has committed the expected output above. Your job is to capture the actual output and produce the diff. You do not rewrite or revise the expected section.

**Step 4 — Actual output**

Run or simulate the operation against the input fixture. Capture the full actual response: status code, response body, headers, side effects. Label this section: `## Actual Output`

**Step 5 — Diff**

Compare the actual output against every element in the Expected Output section. For each element:
- If actual matches expected: write `✓ {element} — contract satisfied`
- If actual deviates from expected: write a finding entry (see Step 6)

If no deviations exist, write: `## Diff — Contract Satisfied` and stop here.

Label this section: `## Diff`

**Step 6 — Classify each finding**

For each deviation found in Step 5, write a finding entry with all of the following:

```
**Finding F-NN**
deviation: [describe what the actual output produced vs. what was expected]
severity: [exactly one of: breaking | degraded | cosmetic]
spec: [spec clause violated — same clause cited in the Expected Output section]
hypothesis: [one sentence on the likely cause — not a symptom description, a cause]
```

Severity definitions:
- `breaking` — the operation cannot be used correctly; a consumer relying on the contract will fail
- `degraded` — the operation functions but violates a guarantee; silent errors or data loss possible
- `cosmetic` — the output differs in a way that does not affect correctness or consumer behavior

**Step 7 — Synthesis**

Write a `## Summary` section containing:
1. Findings table: one row per finding (ID | Severity | Spec Clause | Hypothesis one-liner)
2. Count by severity: `breaking: N | degraded: N | cosmetic: N`
3. Verdict: `Contract violated` or `Contract satisfied`
4. For every `breaking` or `degraded` finding, a recommendation line:
   `recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Output Format: Findings Table

**axis:** output-format
**hypothesis:** Presenting findings in a structured table with mandatory columns (Deviation | Severity | Spec Ref | Root Cause Hypothesis) makes missing C-03 (severity classification) and C-04 (spec reference) entries visible as empty cells at the moment of writing, before scoring. Prose finding entries allow those elements to be omitted silently; an empty table cell creates an immediate visual cue that the entry is incomplete. C-03 and C-04 pass rates should increase because incompleteness is self-evident in the table format.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or flow name and environment}
**Input fixture:** {describe or paste the input state used for this trace}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert (expected output from spec) + Automate (actual output and diff).

---

**Step 1 — Contract identity**

Open the artifact with a `## Contract Scope` section. Include:
- Operation name and method
- Connector or Automate context
- Input fixture (brief description or inline)
- Spec section and version governing this contract

This section must be self-contained. Scope must be derivable without reading external files.

**Step 2 — Expected output**

Write the `## Expected Output` section from the spec before running anything.

List every required element: status codes, response fields, headers, side effects. For each element include the spec clause that requires it.

Cover all contract surfaces:
- Success path (nominal input → expected nominal output)
- Error path (invalid or missing input → expected error response)
- At least one edge case (empty, null, overflow, auth failure)

**Step 3 — Actual output**

Run or simulate the operation. Write the `## Actual Output` section with the full captured response.

**Step 4 — Findings table**

Write the `## Findings` section. If no deviations exist, write: `No deviations — contract satisfied.`

Otherwise, produce a findings table. Every finding is one row. Every column is required:

| ID | Deviation | Severity | Spec Ref | Root Cause Hypothesis |
|----|-----------|----------|----------|-----------------------|
| F-01 | [what actual produced vs. what expected required] | `breaking` / `degraded` / `cosmetic` | [spec clause or field ref] | [one-sentence cause, not symptom] |
| F-02 | ... | ... | ... | ... |

Column rules:
- **Deviation**: describe both sides — what was expected and what was actual
- **Severity**: exactly one of `breaking`, `degraded`, `cosmetic` — no cell may be blank
- **Spec Ref**: the specific clause, section, or field definition from the spec — no cell may be blank
- **Root Cause Hypothesis**: the likely cause (field mapping gap, wrong enum, serialization error) — not a symptom restatement

An empty cell in Severity or Spec Ref means the finding is incomplete. Fill it or remove the row.

Severity definitions:
- `breaking` — consumer relying on the contract will fail
- `degraded` — silent data loss or violated guarantee; consumer may not detect failure
- `cosmetic` — differs from contract in a way that does not affect correctness

**Step 5 — Summary**

Write a `## Summary` section:
1. Finding counts: `breaking: N | degraded: N | cosmetic: N | total: N`
2. Verdict: `Contract violated` or `Contract satisfied`
3. For every `breaking` or `degraded` row, one recommendation:
   - `F-NN recommendation: amend-spec` — [rationale]
   - `F-NN recommendation: fix-impl` — [rationale]
   - `F-NN recommendation: needs-discussion` — [rationale]

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Lifecycle Emphasis: Diff-Phase-Heavy

**axis:** lifecycle-emphasis
**hypothesis:** Expanding the diff phase with explicit per-surface pass/fail requirements — naming success, error, and edge as required contract surfaces with a dedicated row for each, even when no deviation is found — improves C-07 (complete boundary coverage) because the operator cannot omit a surface without producing a visible gap. Contracts that only cover the happy path fail because the happy path is only one of three required rows. Setup and synthesis are compressed to one paragraph each to maximize instructional surface on the diff phase, where boundary coverage failures actually occur.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation}
**Connector / Automate context:** {connector or flow context}
**Input fixture:** {input state}
**Spec source:** {spec path and section}

Stock roles: Connectors contract expert + Automate.

**Setup (one paragraph):** State operation, context, fixture, spec source. Must be self-contained.

**Write expected output** from spec. Label: `## Expected Output`. Cover success, error, and edge surfaces. Cite spec clause for each element.

---

### DIFF PHASE — read this section carefully

This is the core of the trace. The diff phase has three required contract surfaces. You must produce a finding block for each surface, even if the surface has no deviations.

**Surface 1 — Success path**
```
## Diff: Success Path
contract surface: nominal input → nominal output
[compare every expected element against actual for the success case]
```
For each expected element: `✓ satisfied` or write a finding (see Finding Format below).

**Surface 2 — Error path**
```
## Diff: Error Path
contract surface: invalid or missing input → error response
[compare every expected error behavior against actual]
```
For each expected element: `✓ satisfied` or write a finding.

If the spec does not define an error contract for this operation, write:
`error path: not specified in spec — no finding possible`

**Surface 3 — Edge case**
```
## Diff: Edge Case — [name the edge: empty, null, overflow, auth failure, etc.]
contract surface: [describe the edge condition and expected behavior from spec]
[compare expected edge behavior against actual]
```
For each expected element: `✓ satisfied` or write a finding.

If you exercise only one surface, the trace fails C-07 regardless of finding quality. Three surfaces are required.

---

**Finding Format** (use within each surface block):

```
Finding F-NN
deviation: [expected X, actual Y]
severity: breaking | degraded | cosmetic
spec: [spec clause]
hypothesis: [cause, not symptom]
```

Severity definitions:
- `breaking` — consumer will fail relying on the contract
- `degraded` — silent violation; consumer may not detect
- `cosmetic` — non-correctness difference

---

**Synthesis (one paragraph + table):**

`## Summary`
- Count per severity: `breaking: N | degraded: N | cosmetic: N`
- Verdict: `Contract violated` or `Contract satisfied`
- For each `breaking` or `degraded` finding: `F-NN: [amend-spec | fix-impl | needs-discussion] — [rationale]`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Phrasing Register: Formal Imperative with DO NOT Gates

**axis:** phrasing-register
**hypothesis:** Formal imperative language with explicit DO NOT gates targets C-01 (expected-first contract) failures by naming the failure mode as a prohibited action rather than an implied guideline. The specific gate — "DO NOT capture actual output before the Expected Output section is complete and committed" — is a constraint that C-01 failures violate by definition. Operators who drift toward inferring expected output from observation are stopped by a named prohibition rather than a general instruction to "write expected first." C-01 pass rate should increase; no regression on other criteria because the structural sequence is identical to V-01 baseline.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state description or inline fixture}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

**STEP 1 — CONTRACT IDENTITY**

REQUIRED. Write a `## Contract Scope` section. It MUST include:
- Operation name and HTTP method (or equivalent)
- Connector or Automate context and environment
- Input fixture — state what is being fed in; do not reference external files
- Spec version and section governing this contract

A Contract Scope section that requires the reader to open an external file to understand scope fails this step.

---

**STEP 2 — EXPECTED OUTPUT**

REQUIRED. Write the `## Expected Output` section from the spec alone.

DO NOT capture actual output before this section is complete and committed.
DO NOT infer expected values from a previous run or observed behavior.
DO NOT mark this section complete until every contract surface has an expected element with a spec citation.

Write every required element: status codes, response body fields, headers, side effects. For each element, cite the spec clause that requires it.

REQUIRED surfaces:
- Success path (nominal input → expected nominal output)
- Error path (malformed, missing, or unauthorized input → expected error response)
- At least one edge case (empty collection, null required field, rate-limit trigger, auth expiry)

When this section is complete, write: `[EXPECTED COMMITTED]`

DO NOT proceed to Step 3 before writing `[EXPECTED COMMITTED]`.

---

**STEP 3 — ACTUAL OUTPUT**

Run or simulate the operation against the input fixture. Capture the full actual response.

REQUIRED. Write the `## Actual Output` section. Include: status code, full response body, all relevant headers, observable side effects.

DO NOT edit or revise the Expected Output section after this step begins.

---

**STEP 4 — DIFF**

REQUIRED. Write the `## Diff` section. Compare the actual output against every element in the Expected Output section.

For each element: state whether actual satisfies or deviates from expected.

If no deviations exist: write `Contract satisfied — no findings.` and proceed to Step 6.

---

**STEP 5 — CLASSIFY FINDINGS**

REQUIRED. For every deviation, write a finding entry. Every field is REQUIRED:

```
Finding F-NN
deviation: [what was expected vs. what was actual — both sides required]
severity: [EXACTLY ONE OF: breaking | degraded | cosmetic — NO OTHER VALUES]
spec: [spec clause violated — MUST match a clause cited in Step 2]
hypothesis: [one sentence on the cause — NOT a restatement of the symptom]
```

DO NOT write a finding without a severity label.
DO NOT write a finding without a spec clause reference.
DO NOT write a hypothesis that begins "The output did not match" — that is a symptom, not a cause.

Severity definitions:
- `breaking` — a consumer relying on the contract cannot function correctly
- `degraded` — the operation runs but violates a guarantee; silent failure or data loss is possible
- `cosmetic` — the output differs but correctness and consumer behavior are unaffected

---

**STEP 6 — SYNTHESIS**

REQUIRED. Write a `## Summary` section:
1. Findings severity count: `breaking: N | degraded: N | cosmetic: N | total: N`
2. Verdict line: `Contract violated` or `Contract satisfied`
3. For EVERY `breaking` or `degraded` finding, one recommendation:
   `F-NN recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]`

DO NOT omit a recommendation for any `breaking` or `degraded` finding.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — Inertia Framing: Ad-Hoc Observation as Status-Quo Competitor

**axis:** inertia-framing
**hypothesis:** Framing ad-hoc observation ("run the flow, see if it looks right") as the explicit status-quo competitor throughout the skill body forces each phase to argue its improvement over that baseline. C-09 (amendment or fix recommendation) pass rate should increase because the recommendation step is framed as "the decision you cannot make without this artifact" — making the payoff of the discipline concrete. C-06 (contract identity and scope) should also improve because the contrast with ad-hoc testing makes the value of an explicit upfront scope statement legible: without it, you are back to observing without a contract.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state description or inline fixture}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### Why This Discipline Exists

Without this skill, a developer runs the operation, observes the output, and decides "that looks right." That is the status quo — ad-hoc observation against an unwritten contract. The problem: when output changes in the next build, there is no record of what was expected. When a consumer reports a regression, there is no baseline to diff against. When a question arises about whether the spec or the implementation is wrong, there is no artifact to argue from.

This skill produces the artifact the status quo cannot produce: a committed expected contract, a captured actual output, and a classified diff — the record that makes questions answerable and decisions traceable.

Each phase below is an explicit improvement over ad-hoc observation. Treat the status quo as the competitor you are leaving behind at each step.

---

**Phase 0 — Name the contract (improvement: the status quo has no contract)**

Write a `## Contract Scope` section. Without this, you are still doing ad-hoc observation — just with notes. Scope must include:
- Operation name and method
- Connector or Automate context and environment
- Input fixture — state it inline; do not reference external files
- Spec section governing the output contract for this operation

The status quo leaves scope implicit. This phase makes it explicit and referenceable.

---

**Phase 1 — Write expected output before running anything (improvement: the status quo never writes expected first)**

Write the `## Expected Output` section from the spec alone. Do not run the operation first.

The status quo runs first and observes. That makes the observation the de facto contract. By writing expected from spec before running, you create a contract that exists independently of what the implementation currently does.

Write every required element: status codes, response body shape, headers, side effects. For each element, cite the spec clause that requires it.

Cover all contract surfaces the spec defines:
- Success path (nominal input → expected output per spec)
- Error path (invalid or missing input → expected error per spec)
- At least one edge case (empty, null, overflow, auth failure)

When complete, write: `[CONTRACT COMMITTED]`

---

**Phase 2 — Capture actual output (improvement: you now have a committed contract to diff against)**

Run or simulate the operation against the input fixture. Write the `## Actual Output` section. Include the full response: status, body, headers, observable side effects.

The status quo stops here. You have observed. The status quo has no Phase 3.

---

**Phase 3 — Diff: compare, do not re-observe (improvement: the status quo has no diff because it has no expected)**

Write the `## Diff` section. For each element in the Expected Output section, state whether actual satisfies or deviates.

If no deviations: write `Contract satisfied — no findings.` and proceed to Phase 5.

---

**Phase 4 — Classify findings (improvement: the status quo calls deviations "bugs" without evidence)**

For each deviation, write a finding entry:

```
Finding F-NN
deviation: [what was expected vs. what was actual]
severity: breaking | degraded | cosmetic
spec: [spec clause violated]
hypothesis: [likely cause — not symptom]
```

Severity definitions:
- `breaking` — consumer relying on the contract will fail
- `degraded` — operation runs but a guarantee is violated; silent failure possible
- `cosmetic` — differs from contract without affecting correctness

Every finding must have severity and spec reference. A finding without a spec reference is an observation, not a contract violation — it does not belong in this artifact.

---

**Phase 5 — Decide: amend the spec or fix the implementation (improvement: this is the decision the status quo cannot make because it has no contract)**

Write a `## Summary` section:
1. Finding counts: `breaking: N | degraded: N | cosmetic: N`
2. Verdict: `Contract violated` or `Contract satisfied`
3. For every `breaking` or `degraded` finding, state:
   `F-NN recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]`

This is the step ad-hoc observation cannot reach. Without a committed expected contract, you cannot determine whether the implementation is wrong or the spec is wrong — you can only observe that they differ. This artifact makes the argument traceable.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## Combination Candidates for Round 2

| Priority | Axis Pair | Rationale |
|----------|-----------|-----------|
| 1 | role-sequence + phrasing-register (V-01 + V-04) | V-01's expert handoff commits the expected contract structurally; V-04's DO NOT gates prevent the specific failure mode (inferring expected from actual) at the language level. Combined, the structural separation and the prohibition operate at two levels simultaneously. Targets C-01 from both the process design and the language constraint angles. |
| 2 | output-format + inertia-framing (V-02 + V-05) | V-02's findings table makes C-03 and C-04 failures visible as empty cells; V-05's inertia framing makes the C-09 recommendation step concrete by framing it as the payoff the status quo cannot produce. Combined, the table catches missing severity/spec-ref while the inertia framing motivates the synthesis step. Targets C-03, C-04, and C-09 simultaneously. |

## Evaluation Order Guidance

| Priority | Variation | Rationale |
|----------|-----------|-----------|
| 1 | V-02 (output-format: findings table) | Most directly testable — column presence/absence maps 1:1 to C-03 and C-04 criteria. Establishes the baseline table format for combination candidates. |
| 2 | V-04 (phrasing-register: formal imperative) | Tests C-01 directly with a named prohibition. If "DO NOT capture actual before committed" does not improve C-01 pass rate, the failure is structural, not linguistic — informs V-01 evaluation. |
| 3 | V-01 (role-sequence: expert-before-automate) | Structural C-01 fix. Evaluate after V-04 to isolate: if V-04 improves C-01 and V-01 does not add further improvement, language is sufficient and structural separation is overhead. |
| 4 | V-05 (inertia-framing: ad-hoc as competitor) | C-09 target. Evaluate after V-02 establishes table baseline — if V-02 already passes C-09 via the recommendation column, V-05's framing improvement is incremental. |
| 5 | V-03 (lifecycle-emphasis: diff-phase-heavy) | C-07 target. Evaluate last — three-surface enforcement is the most structural change and its interaction with other criteria needs the single-axis baselines established first. |
