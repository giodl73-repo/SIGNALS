# trace-contract Variate — Round 1 (rubric v16)

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v16 (C-01 through C-10; essential C-01–C-05; golden threshold: all essential pass + composite >= 80)
**Round:** R1 — 3 single-axis + 2 combination

---

## Round 1 Variation Map

| Variation | Axis | Primary Target | Hypothesis |
|-----------|------|----------------|------------|
| V-01 | role-sequence | C-01 | Gated expert-before-Automate handoff prevents expected-from-actual contamination structurally |
| V-02 | output-format | C-02, C-03, C-04 | Pass-confirm list + findings table makes silent omissions and missing columns self-evident at write time |
| V-03 | lifecycle-emphasis | C-07, C-02 | Naming the three-directory layers as phase headings forces explicit structure and prevents omitting non-deviation elements from the diff |
| V-04 | phrasing-register + role-sequence | C-01, C-05 | DO NOT gates on the specific failure modes (inferring expected from actual; restating symptom as hypothesis) target the two most common essential failures simultaneously |
| V-05 | inertia-framing | C-08, C-09, C-10 | Framing each phase against "run and observe" makes amendment/fix recommendation and coverage ratio feel like the natural payoff of the discipline, not overhead |

---

## V-01 — Role Sequence: Expert Commits Before Automate Enters

**axis:** role-sequence
**hypothesis:** When a single prompt describes both the expected-output and actual-output phases without a structural gate, operators write both passes mentally in the same reading and infer expected values from what they know the implementation does. Requiring the Connectors contract expert to complete the Expected Output section and write a commit marker before Automate reads any instruction past that point prevents this contamination structurally. The commit gate makes C-01 a binary checkpoint rather than an honor system. C-04 (spec reference per finding) should also improve because the expert's cited clauses are already in the document when Automate writes findings — Automate can copy the clause identifier rather than re-derive it.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {describe or paste the input state used for this trace — inline, not a file reference}
**Spec source:** {spec file path and section — e.g., signal-spec-2026-03-14.md §4.2}

Stock roles: Connectors contract expert (writes expected output from spec) + Automate (captures actual output, performs diff, classifies findings).

---

### ROLE: Connectors Contract Expert

You are a Connectors contract expert. You write the expected output — the contract — from the spec alone. You have not run the operation. You have not observed any output. Your role ends at the commit marker.

**Step 1 — Contract identity**

Write a `## Contract Scope` section containing:
- Operation name and HTTP method (or equivalent)
- Connector or Automate context and environment
- Input fixture summary — state inline; do not reference an external file
- Spec version and section governing this operation's output contract

A reader must be able to determine exactly what is being tested from this section alone.

**Step 2 — Expected output (the contract)**

Write a `## Expected Output` section. Derive every element from the spec. For each required element:
- State the element (e.g., `status: 200`, `body.items: array`, `X-RateLimit-Remaining: present when throttled`)
- Cite the spec clause that requires it (e.g., `spec §3.2 — success response must include items array`)

Cover all contract surfaces the spec defines:
- **Success path** — nominal input, expected nominal output
- **Error path** — invalid or missing input, expected error response
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

If the spec does not define a surface, write: `[surface]: not specified in spec`.

Label this section clearly: `## Expected Output`

**Step 3 — Commit gate**

When the Expected Output section is complete, write exactly:

`[CONTRACT COMMITTED — Automate begins here]`

Your role ends here. Do not proceed past this line.

---

### ROLE: Automate

You are Automate. The contract expert has committed the expected output above. You read the Expected Output section; you do not revise it. Your role begins at the commit marker.

**Step 4 — Actual output**

Run or simulate the operation against the input fixture. Write a `## Actual Output` section containing the full actual response: status code, response body, all relevant headers, observable side effects.

**Step 5 — Diff**

Write a `## Diff` section. For every element in the Expected Output section, state one of:
- `✓ {element} — satisfied` (actual matches expected)
- A finding entry (actual deviates from expected)

Every expected element must appear in the diff with an explicit result. An element that appears in Expected but is absent from the Diff is a silent omission — the trace fails C-02.

If no deviations exist: write `## Diff — Contract satisfied. No findings.` and proceed to Step 7.

**Step 6 — Classify findings**

For each deviation from Step 5, write a finding entry with all four fields:

```
Finding F-NN
deviation: [what was expected vs. what was actual — both sides]
severity: [exactly one of: breaking | degraded | cosmetic]
spec: [spec clause violated — must match a clause cited in Expected Output]
hypothesis: [one sentence on the likely cause — a mechanism, not a symptom restatement]
```

Severity definitions:
- `breaking` — a consumer relying on the contract cannot function correctly
- `degraded` — the operation runs but violates a guarantee; silent failure or data loss possible
- `cosmetic` — differs from contract in a way that does not affect correctness or consumer behavior

**Step 7 — Summary**

Write a `## Summary` section:
1. Finding counts: `breaking: N | degraded: N | cosmetic: N | total: N`
2. Verdict: `Contract violated` or `Contract satisfied`
3. For every `breaking` or `degraded` finding, one recommendation:
   `F-NN recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]`
4. Coverage ratio: `{clauses checked} / {clauses in Expected Output} checked, {N} findings`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Output Format: Pass-Confirm List + Findings Table

**axis:** output-format
**hypothesis:** Two structural format choices together prevent the most common essential failures. First: a pass-confirm list that requires an explicit `✓` or finding entry for every expected element prevents C-02 (silent omissions) — omitting an element is visible as a missing row rather than as a gap in prose. Second: a findings table with mandatory columns (Deviation | Severity | Spec Ref | Root Cause Hypothesis) makes C-03 (severity label) and C-04 (spec reference) failures visible as empty cells at write time. An empty cell creates a visual cue that the row is incomplete before any reviewer sees it. Together the two formats catch C-02, C-03, and C-04 failures at the point of writing.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {describe or paste the input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

**Step 1 — Contract scope**

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline description)
- Spec version and section

Self-contained — no external file references.

**Step 2 — Expected output**

Write the `## Expected Output` section from the spec before running anything. List every required element: status codes, response fields, headers, side effects. For each element, cite the spec clause.

Cover all contract surfaces:
- Success path (nominal input → expected nominal output)
- Error path (invalid or missing input → expected error response)
- At least one edge case (empty, null, overflow, auth failure)

**Step 3 — Actual output**

Run or simulate the operation. Write the `## Actual Output` section with the full captured response.

**Step 4 — Diff and findings**

Write the `## Diff` section as a pass-confirm list. For every element listed in the Expected Output section, write exactly one of:

```
✓ {element identifier} — satisfied
F-NN {element identifier} — deviation (see findings table)
```

Every element in Expected Output must appear in this list. Missing elements are silent omissions and cause C-02 to fail.

Then write a `## Findings` table. If there are no findings, write: `No deviations — contract satisfied.`

Otherwise, every finding is one row. Every column is required — no cell may be blank:

| ID | Deviation | Severity | Spec Ref | Root Cause Hypothesis |
|----|-----------|----------|----------|-----------------------|
| F-01 | [expected X; actual Y — state both sides] | `breaking` / `degraded` / `cosmetic` | [spec clause or field ref — no paraphrase, cite the clause] | [one-sentence cause — not a symptom restatement] |

Column rules:
- **Severity**: exactly one of `breaking`, `degraded`, `cosmetic` — no blank cells, no compound labels
- **Spec Ref**: the specific clause or field definition from the spec — not "see spec §3" but "spec §3.2 — success response must include items array"
- **Root Cause Hypothesis**: names a mechanism (field mapping error, wrong enum value, serialization failure) — not "the output did not match expected"

An empty cell in any column means the finding is incomplete. Fill it or remove the row.

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but violates a guarantee; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness or consumer behavior

**Step 5 — Summary**

Write a `## Summary` section:
1. Finding counts: `breaking: N | degraded: N | cosmetic: N | total: N`
2. Verdict: `Contract violated` or `Contract satisfied`
3. For every `breaking` or `degraded` row, one recommendation:
   `F-NN: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]`
4. Coverage ratio: `{N} / {total elements in Expected Output} clauses verified, {N} deviations found`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Lifecycle Emphasis: Three-Directory Layers as Named Phase Headings

**axis:** lifecycle-emphasis
**hypothesis:** The three-directory pattern (10-Input, 20-Expected, 30-Actual) is the structural backbone of this skill, but most prompt variants describe it as a note rather than as the organizing principle of the artifact. When the artifact's section headings are explicitly named after the three directories — `## 10-Input Layer`, `## 20-Expected Layer`, `## 30-Actual Layer` — the mapping from phase to directory is self-evident in the output without reading the instructions. C-07 (three-directory layers explicitly labeled) becomes a property of the output structure rather than a criterion the operator must remember to satisfy. C-02 (diff complete, no silent omissions) also improves because the explicit input-expected-actual structure makes it obvious when an element present in the Expected layer does not appear in the Actual layer comparison.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation}
**Connector / Automate context:** {connector or flow context and environment}
**Input fixture:** {input state — inline}
**Spec source:** {spec path and section}

Stock roles: Connectors contract expert + Automate.

---

This trace follows the three-directory pattern. The artifact has three layers. Each layer maps to one directory in the pattern. Use the headings below exactly.

---

### `## 10-Input Layer`

Write this section first. It is the setup record — not a finding, not an expectation, just a factual statement of what is being fed in.

Contents:
- Operation name and HTTP method (or equivalent)
- Connector or Automate context and environment
- Input fixture — describe or paste the state being used; no external file references
- Spec source version and section

This layer answers: "What are we testing and against what spec?"

---

### `## 20-Expected Layer` (the contract)

Write this section from the spec alone, before running anything. This is the contract. Every element here is a claim the spec makes about what the operation must produce.

For each required element:
- State the element (e.g., `status: 200`, `body.items: array`, `X-RateLimit-Remaining: present when throttled`)
- Cite the spec clause that requires it

Cover all contract surfaces defined by the spec:
- **Success path** — nominal input, nominal output per spec
- **Error path** — invalid or missing input, error response per spec
- **At least one edge case** — empty collection, null required field, rate-limit trigger, or auth expiry

If the spec does not define a surface for this operation, write: `[surface]: not specified in spec — no contract clause exists`.

This layer answers: "What does the spec say must happen?"

---

### `## 30-Actual Layer` (observed output)

Run or simulate the operation against the input fixture. Capture the full response.

Contents:
- Status code
- Response body (full or representative)
- All relevant headers
- Observable side effects

This layer answers: "What did the operation actually produce?"

---

### `## Diff`

For every element in the `20-Expected Layer`, state one of:
- `✓ {element} — satisfied` (actual matches expected)
- A finding entry (actual deviates)

Every element must appear. Silent omissions fail C-02 regardless of finding quality.

**Finding format:**
```
Finding F-NN
deviation: [expected X; actual Y]
severity: breaking | degraded | cosmetic
spec: [clause from 20-Expected Layer]
hypothesis: [mechanism — not symptom]
```

Severity:
- `breaking` — consumer relying on the contract cannot function
- `degraded` — operation runs but a guarantee is violated; silent failure possible
- `cosmetic` — non-correctness difference

---

### `## Summary`

- Counts: `breaking: N | degraded: N | cosmetic: N | total: N`
- Verdict: `Contract violated` or `Contract satisfied`
- For every `breaking` or `degraded` finding:
  `F-NN: [amend-spec | fix-impl | needs-discussion] — [rationale]`
- Coverage: `{N} / {total in 20-Expected Layer} clauses verified, {N} deviations`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Phrasing Register + Role Sequence: DO NOT Gates on the Two Most Common Essential Failures

**axes:** phrasing-register + role-sequence
**hypothesis:** C-01 and C-05 are the two essential criteria most frequently failed, and they fail in predictable ways: C-01 fails when expected values are inferred from observed behavior rather than derived from spec; C-05 fails when the hypothesis field restates the symptom ("the output did not match") rather than naming a mechanism. These failure modes are specific enough to be blocked by named prohibitions. V-01's role-sequence gate prevents C-01 structurally; adding explicit DO NOT language targeting the precise failure form should prevent it linguistically as well. DO NOT gates on C-05's failure form ("DO NOT begin a hypothesis with 'The output did not'") remove the path of least resistance for symptom restatement. Combined, these two axes address C-01 from both the process level and the language level, and address C-05 at the point where the failure actually occurs.

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

You are the Connectors contract expert. You write the expected output from the spec alone. You have not run the operation. You have not observed any output from the implementation.

**STEP 1 — CONTRACT SCOPE**

REQUIRED. Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture — state inline; DO NOT reference external files
- Spec version and section governing this operation's output contract

A scope section that requires the reader to open another file fails this step.

**STEP 2 — EXPECTED OUTPUT**

REQUIRED. Write the `## Expected Output` section from the spec alone.

DO NOT run the operation before completing this section.
DO NOT infer expected values from a previous run, from memory of observed behavior, or from knowledge of the current implementation.
DO NOT mark this section complete until every contract surface has at least one expected element with a spec citation.

For each required element, state the element and cite the spec clause. Cover:
- **Success path** — nominal input → nominal output
- **Error path** — invalid or missing input → error response
- **At least one edge case**

If a surface is not defined in the spec, write: `[surface]: not specified in spec`.

When this section is complete, write:

`[EXPECTED COMMITTED]`

DO NOT proceed to Step 3 before writing this line.

---

### ROLE: Automate

You are Automate. The contract is committed above. You begin after `[EXPECTED COMMITTED]`. DO NOT revise the Expected Output section. Any belief that an Expected entry is wrong is a finding, not a license to edit.

**STEP 3 — ACTUAL OUTPUT**

REQUIRED. Run or simulate the operation against the input fixture. Write the `## Actual Output` section: status code, response body, headers, side effects.

DO NOT edit the Expected Output section after this step begins.

**STEP 4 — DIFF**

REQUIRED. Write the `## Diff` section. For every element in Expected Output, state whether actual satisfies or deviates.

Every element must appear. Silent omissions fail C-02.

If no deviations: write `## Diff — Contract satisfied. No findings.` and proceed to Step 6.

**STEP 5 — CLASSIFY FINDINGS**

REQUIRED. For every deviation, write a finding entry with all four fields:

```
Finding F-NN
deviation: [expected X; actual Y — state both sides explicitly]
severity: [EXACTLY ONE OF: breaking | degraded | cosmetic]
spec: [spec clause violated — must match a clause from Expected Output]
hypothesis: [one sentence on the cause — a mechanism, not a symptom]
```

DO NOT write a finding without a severity label.
DO NOT write a finding without a spec clause reference.
DO NOT begin a hypothesis with "The output did not" — that is a symptom description, not a cause.
DO NOT begin a hypothesis with "There is a mismatch" or "The value is incorrect" — same failure.

A valid hypothesis names a causal mechanism: field mapping not applied after auth upgrade, enum serialized as integer instead of string, empty-collection short-circuit returns null rather than empty array.

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness or consumer behavior

**STEP 6 — SUMMARY**

REQUIRED. Write a `## Summary` section:
1. Counts: `breaking: N | degraded: N | cosmetic: N | total: N`
2. Verdict: `Contract violated` or `Contract satisfied`
3. For every `breaking` or `degraded` finding:
   `F-NN: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]`

DO NOT omit a recommendation for any `breaking` or `degraded` finding.

4. Coverage ratio: `{N} / {total elements in Expected Output} clauses checked, {N} deviations`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — Inertia Framing: Ad-Hoc Observation as Status-Quo Competitor

**axis:** inertia-framing
**hypothesis:** Teams skip the contract trace discipline because the alternative — running the operation and deciding "it looks right" — is faster and produces no artifact overhead. Each phase of this skill has a concrete payoff over that status quo, but standard prompt bodies state the payoff as a rule rather than as a contrast. Framing each phase against the named status-quo behavior ("without this step, you are still doing ad-hoc observation") makes the value of the phase legible to the operator rather than an obligation imposed by process. C-08 (amendment or fix recommendation) benefits most because the recommendation step is literally the decision the status quo cannot make — without a committed expected contract, you cannot determine whether spec or implementation is wrong, only that they differ. C-09 (summary table) and C-10 (coverage ratio) follow from the same framing: the summary and coverage statement are the artifact's evidence that you moved beyond observation.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### Why this skill exists

The status quo: run the operation, observe the output, decide it looks right. This produces no artifact. When the output changes in the next build, there is no record of what was expected. When a consumer reports a regression, there is no baseline to diff against. When a question arises about whether the spec or the implementation is wrong, there is no artifact to argue from — only the current observed state.

This skill exists to produce the artifact the status quo cannot produce: a committed expected contract, a captured actual output, and a classified diff. Every phase below is a named improvement over ad-hoc observation. Leave any phase incomplete and you are partially back to the status quo.

---

**Phase 0 — Name the contract** *(improvement: the status quo has no contract)*

Write a `## Contract Scope` section. Without this, you have notes, not a contract. Notes cannot be diffed. Scope must include:
- Operation name and method
- Connector or Automate context and environment
- Input fixture — state inline; external file references leave scope implicit
- Spec version and section governing the output contract

The status quo leaves scope implicit — you know what you ran but there is no record. This phase makes it explicit and referenceable.

---

**Phase 1 — Write expected output before running anything** *(improvement: the status quo never writes expected first)*

Write the `## Expected Output` section from the spec alone. Do not run the operation first.

The status quo runs first and observes. The observation becomes the de facto contract. By writing expected from spec before running, you create a contract that exists independently of what the implementation currently produces. If they differ, you have a finding. If the status quo runs first, it has no finding — only "that's what it does."

For each required element, cite the spec clause. Cover all contract surfaces the spec defines:
- Success path — nominal input → nominal output
- Error path — invalid or missing input → error response
- At least one edge case

When complete, write: `[CONTRACT COMMITTED]`

---

**Phase 2 — Capture actual output** *(improvement: you now have a contract to diff against)*

Run or simulate the operation. Write the `## Actual Output` section: status code, full response body, headers, observable side effects.

The status quo stops here. It has observed. It has no Phase 3.

---

**Phase 3 — Diff: compare against the contract, do not re-observe** *(improvement: the status quo has no diff because it has no expected)*

Write the `## Diff` section. For every element in the Expected Output section, state whether actual satisfies or deviates.

Every element must appear — `✓ satisfied` or a finding. Elements that appear in Expected but are absent from the Diff are silent omissions; the status quo produces only silent omissions. If no deviations: write `Contract satisfied — no findings.` and proceed to Phase 5.

---

**Phase 4 — Classify findings** *(improvement: the status quo calls deviations "bugs" without evidence)*

For each deviation, write a finding entry:

```
Finding F-NN
deviation: [expected X; actual Y]
severity: breaking | degraded | cosmetic
spec: [spec clause violated]
hypothesis: [likely cause — mechanism, not symptom]
```

Every finding must have a severity label and a spec reference. A finding without a spec reference is an observation — it does not belong in a contract trace because it cannot be argued from. The status quo produces observations; this skill produces classified contract violations.

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness

---

**Phase 5 — Decide: amend the spec or fix the implementation** *(improvement: this is the decision the status quo cannot make)*

Write a `## Summary` section:

1. Per-severity counts and total:

| Severity | Count |
|----------|-------|
| breaking | N |
| degraded | N |
| cosmetic | N |
| **total** | **N** |

2. Verdict: `Contract violated` or `Contract satisfied`

3. For every `breaking` or `degraded` finding, state:
   `F-NN: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]`

   This is the step the status quo cannot reach. Without a committed expected contract, you cannot determine whether the implementation is wrong or the spec is wrong — you can only observe that they differ. The recommendation line is the payoff that justifies the discipline.

4. Coverage ratio: `{N} / {total elements in Expected Output} clauses verified, {N} deviations found`

   The status quo has no coverage ratio because it has no expected output. This number is the evidence that you covered the contract, not just the happy path.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## Combination Candidates for Round 2

| Priority | Axis Pair | Primary Targets | Rationale |
|----------|-----------|-----------------|-----------|
| 1 | role-sequence + phrasing-register (V-01 + V-04) | C-01, C-05 | V-01's commit gate prevents C-01 structurally; V-04's DO NOT gates prevent it linguistically and block C-05's symptom-restatement failure. Two levels targeting the same essential criteria. |
| 2 | output-format + inertia-framing (V-02 + V-05) | C-02, C-03, C-04, C-08, C-09, C-10 | V-02's pass-confirm list and findings table catch essential failures at write time; V-05's status-quo framing motivates the recommended and aspirational criteria as the payoff steps. Covers essential through aspirational in one variation. |
| 3 | lifecycle-emphasis + output-format (V-03 + V-02) | C-07, C-02, C-03, C-04 | Three-directory headings enforce C-07; findings table enforces C-03/C-04. Natural structural pairing — directory labels provide the skeleton, table format provides the finding constraint. |

## Evaluation Order Guidance

| Priority | Variation | Rationale |
|----------|-----------|-----------|
| 1 | V-02 (output-format: pass-confirm + table) | Tests C-02, C-03, C-04 simultaneously. Column presence/absence maps 1:1 to criteria — most directly measurable of the five. Establishes the table format baseline for combination candidates. |
| 2 | V-04 (phrasing-register + role-sequence: DO NOT gates) | Tests C-01 and C-05 directly with named prohibitions. If DO NOT gates do not improve C-05, the failure is structural — informs whether mechanism-framing needs to be added to the hypothesis instruction rather than negated. |
| 3 | V-01 (role-sequence: expert commits first) | Structural C-01 fix. Evaluate after V-04 to isolate: if V-04's language gate alone passes C-01, structural separation is overhead. If V-04 partially fails C-01, V-01's gate is necessary. |
| 4 | V-03 (lifecycle-emphasis: three-directory headings) | C-07 + C-02 target. Directory heading structure is a formatting change; evaluate after V-02 establishes whether table format already satisfies C-02 through the pass-confirm list mechanism. |
| 5 | V-05 (inertia-framing: status-quo competitor) | C-08, C-09, C-10 target. Evaluate last — recommended and aspirational criteria. If essentials are passing across V-01–V-04, V-05 determines whether inertia framing is the marginal improvement needed to reach the aspirational tier. |
