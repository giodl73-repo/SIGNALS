# trace-contract Variate --- Round 2

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v2 (C-01 through C-12; aspirational C-09-C-12 are the Round 2 targets)
**Round:** R2 -- 3 single-axis + 2 combination; all variations target aspirational criteria missed by R1 top scorers

---

## Round 2 Variation Map

| Variation | Axis | Target Aspirational | Hypothesis |
|-----------|------|---------------------|------------|
| V-01 | phase-gate confirmation | C-12 | An explicit gate question answered in the document passes C-12; sequencing alone (R1 V-01, V-04) does not |
| V-02 | structural field enforcement | C-11 | Column-aligned labeled slots make any missing required field visibly empty at write time; prose entries allow silent omission |
| V-03 | amendment suggestion embedded in finding format | C-09 | Embedding recommended-action inside the finding block means it is written at classification time, before it can be omitted |
| V-04 | pattern recognition + amendment | C-09, C-10 | A required Patterns section plus inline amendment line covers both criteria without changing the expected/actual/diff pipeline |
| V-05 | all aspirational combined | C-09, C-10, C-11, C-12 | Full integration: gate lock + labeled-slot blocks + amendment line + patterns section; compliant response scores 100 |

---

## V-01 -- Phase-Gate Confirmation (C-12 only)

**axis:** phase-gate confirmation
**hypothesis:** C-12 requires an explicit gate artifact written to the document -- a named question answered or a lock statement -- before execution begins. R1 top variants enforce sequencing with 'do not proceed' language and [CONTRACT COMMITTED] markers, but neither requires the model to answer a gate question confirming the expected section is sealed. A gate check answered in the document is qualitatively different from an ordering instruction: the model must write an affirmative claim, making contamination detectable as a missing claim rather than an unobservable sequencing violation.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {describe or paste the input state used for this trace}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert (writes expected from spec) + Automate (executes and diffs).

---

**Step 1 -- Contract identity**

Write a `## Contract Scope` section:
- Operation name and HTTP method
- Connector or Automate context and environment
- Input fixture summary (inline -- do not reference external files)
- Spec version and section governing this contract

This section must be self-contained.

---

**Step 2 -- Expected output**

You are the Connectors contract expert. Write from the spec alone. Do not run the operation.

Write the `## Expected Output (from spec)` section. For every required element, write:
- The expected value or shape
- The spec clause that requires it

Cover all three contract surfaces:
- Success path: nominal input -- expected nominal output per spec
- Error path: invalid or missing input -- expected error response per spec
- At least one edge case: empty collection, null required field, auth failure, or rate-limit trigger

When the Expected Output section is complete, answer the gate check and write the gate token:

    GATE CHECK -- Expected output section complete?
    Answer YES or NO before proceeding.
    If YES, write exactly: [EXPECTED SEALED -- execution begins here]
    If NO, complete the Expected Output section before answering.

Do not write [EXPECTED SEALED] until every contract surface has expected elements with spec citations. Do not begin Step 3 before this line is present in the document.

---

**Step 3 -- Actual output**

You are Automate. The expected output is sealed above. Do not revise the Expected Output section.

Run or simulate the operation. Write the `## Actual Output` section: status code, full response body, headers, observable side effects.

---

**Step 4 -- Diff**

Write the `## Diff` section. Compare every element in the Expected Output section against the actual output.

- Match: satisfied -- contract honored
- Deviation: write a finding entry (see Step 5)

If no deviations: write `## Diff -- Contract Satisfied` with `No deviations found.` and proceed to Step 6.

---

**Step 5 -- Classify findings**

For each deviation:

```
Finding F-NN
deviation: [expected X vs. actual Y -- both sides]
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated]
hypothesis: [one sentence cause -- not a symptom restatement]
```

Severity: breaking = consumer will fail; degraded = silent violation possible; cosmetic = non-correctness difference.

Automate / Connectors lens: for at least one finding, explicitly state whether the deviation affects integration-level consumers (Automate connector mappings, schema-bound fields) or is isolated to runtime behavior.

---

**Step 6 -- Summary**

Write a `## Summary` section:
1. Finding counts: `breaking: N | degraded: N | cosmetic: N | total: N`
2. Verdict: `Contract violated` or `Contract satisfied`
3. For every breaking or degraded finding: `F-NN recommendation: [amend-spec | fix-impl | needs-discussion] -- [one sentence rationale]`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 -- Structural Field Enforcement (C-11 only)

**axis:** structural field enforcement
**hypothesis:** C-11 requires missing required fields to be visually self-announcing at write time. Prose finding entries allow severity, spec-ref, or root-cause to be omitted silently -- the absence of a keyword in prose is invisible. Column-aligned labeled-slot lines in a fixed per-finding block leave a visible empty slot when a field is missing, immediately apparent to the model at write time and to any reviewer. The slot format also improves C-03 and C-04 compliance as a side effect: when the format insists on named slots, filling them becomes the path of least resistance.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {describe or paste the input state used for this trace}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert (writes expected from spec) + Automate (executes and diffs).

---

**Step 1 -- Contract identity**

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline -- no external file references)
- Spec section and version governing this contract

Self-contained: scope must be derivable without opening any external file.

---

**Step 2 -- Expected output**

Write from spec. Do not run the operation first.

Write the `## Expected Output (from spec)` section. For each required element, state the expected value or shape and the spec clause that requires it.

Cover all three contract surfaces: success path, error path, at least one edge case. Cite a spec clause for every element.

---

**Step 3 -- Actual output**

Run or simulate the operation. Write the `## Actual Output` section: status code, full response body, headers, observable side effects.

---

**Step 4 -- Diff and findings**

Write the `## Findings` section. If no deviations: write `Contract satisfied -- no deviations found.` and proceed to Step 5.

Otherwise, for each deviation write one finding block using this exact format. Every slot is required. An empty slot line means the finding is incomplete -- fill it or remove the finding:

```
Finding F-NN
  deviation        : [REQUIRED -- expected X, actual Y; both sides must be stated]
  severity         : [REQUIRED -- exactly one of: breaking | degraded | cosmetic]
  spec-ref         : [REQUIRED -- spec clause, section, or field definition violated]
  root-cause       : [REQUIRED -- one sentence cause; name a mechanism, not restate the deviation]
  connector-impact : [REQUIRED -- does this break Automate mappings or schema bindings? state explicitly]
```

Severity: breaking = consumer will fail; degraded = silent violation possible; cosmetic = non-correctness difference.

The `connector-impact` slot satisfies the Automate / Connectors lens. It may not be left blank.

---

**Step 5 -- Summary**

Write a `## Summary` section:
1. Finding counts: `breaking: N | degraded: N | cosmetic: N | total: N`
2. Verdict: `Contract violated` or `Contract satisfied`
3. For every breaking or degraded finding: `F-NN recommendation: [amend-spec | fix-impl | needs-discussion] -- [rationale]`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 -- Amendment Suggestion Embedded in Finding Format (C-09 only)

**axis:** amendment suggestion embedded in finding format
**hypothesis:** C-09 requires every breaking finding to include a concrete Recommended action line distinguishing spec-side vs. implementation-side resolution. R1 variants defer this to the Summary step, which means it can be omitted for individual findings without a visible gap. Embedding a recommended-action slot directly inside the finding block template -- required only for severity breaking -- means the recommendation is written at the moment of classification. Deferral becomes structurally impossible: the finding block is open until the slot is filled.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {describe or paste the input state used for this trace}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert (writes expected from spec) + Automate (executes and diffs).

---

**Step 1 -- Contract identity**

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline)
- Spec section and version governing this contract

Must be self-contained.

---

**Step 2 -- Expected output**

Connectors contract expert writes from spec. Do not run the operation first.

Write the `## Expected Output (from spec)` section. For each required element, state the expected value or shape and the spec clause that requires it.

Cover all contract surfaces: success path, error path, at least one edge case.

When this section is complete, write: `[EXPECTED COMMITTED]`. Do not proceed to Step 3 before this line.

---

**Step 3 -- Actual output**

Automate. Do not revise the Expected Output section.

Run or simulate the operation. Write the `## Actual Output` section: status code, full response body, headers, observable side effects.

---

**Step 4 -- Diff**

Write the `## Diff` section. For each expected element, state whether actual satisfies or deviates.

If no deviations: write `Contract satisfied -- no findings.` and proceed to Step 6.

---

**Step 5 -- Classify findings**

For each deviation, write a finding block. Format depends on severity.

For `degraded` or `cosmetic` findings:
```
Finding F-NN
deviation: [expected X, actual Y -- both sides]
severity: [degraded | cosmetic]
spec: [spec clause violated]
hypothesis: [one sentence cause -- not symptom]
```

For `breaking` findings, the recommended-action field is required:
```
Finding F-NN
deviation: [expected X, actual Y -- both sides]
severity: breaking
spec: [spec clause violated]
hypothesis: [one sentence cause -- not symptom]
recommended-action: [amend-spec | fix-impl] -- [one sentence rationale: which side is wrong and why]
```

A breaking finding without recommended-action is incomplete. The rationale must distinguish which side is wrong -- spec contract or implementation behavior -- not merely state that they differ.

Severity: breaking = consumer will fail; degraded = silent violation possible; cosmetic = non-correctness difference.

Automate / Connectors lens: for at least one finding, state whether the deviation breaks integration-level consumers or is confined to runtime behavior.

---

**Step 6 -- Summary**

Write a `## Summary` section:
1. Finding counts: `breaking: N | degraded: N | cosmetic: N | total: N`
2. Verdict: `Contract violated` or `Contract satisfied`
3. Recommended-action index: one line per breaking finding -- `F-NN: [amend-spec | fix-impl] -- [rationale]` -- extracted from the finding blocks above

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 -- Pattern Recognition + Amendment (C-09 + C-10)

**axis:** pattern recognition + amendment suggestion (combination)
**hypothesis:** C-10 requires an explicit Patterns section or inline grouping notes when two or more findings share a root cause. C-09 requires an amendment recommendation on every breaking finding. These two criteria are structurally compatible and neither requires a change to the expected/actual/diff pipeline. A dedicated Patterns section immediately after findings -- with explicit grouping-by-root-cause instruction -- achieves C-10 without disrupting the finding structure R1 top variants established. The inline amendment line from V-03 achieves C-09. Together the two aspirational criteria add one structural section and one inline field to the R1 90-point baseline.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {describe or paste the input state used for this trace}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert (writes expected from spec) + Automate (executes and diffs).

---

**Step 1 -- Contract identity**

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline)
- Spec section and version governing this contract

Must be self-contained.

---

**Step 2 -- Expected output**

Connectors contract expert writes from spec. Do not run the operation.

Write the `## Expected Output (from spec)` section. For each required element, state the expected value or shape and the spec clause that requires it.

Cover all contract surfaces: success path, error path, at least one edge case.

When complete, write: `[EXPECTED COMMITTED]`. Do not proceed to Step 3 before this line.

---

**Step 3 -- Actual output**

Automate. Do not revise the Expected Output section.

Run or simulate the operation. Write the `## Actual Output` section: status code, full response body, headers, observable side effects.

---

**Step 4 -- Diff**

Write the `## Diff` section. For each expected element: satisfied or write a finding (see Step 5). If no deviations: write `Contract satisfied -- no findings.` and proceed to Step 7.

---

**Step 5 -- Classify findings**

For each deviation:

```
Finding F-NN
deviation: [expected X, actual Y -- both sides]
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated]
hypothesis: [one sentence cause -- not symptom]
```

For every `breaking` finding, append immediately:
```
recommended-action: [amend-spec | fix-impl] -- [one sentence rationale distinguishing spec-side vs. implementation-side error]
```

A breaking finding without recommended-action is incomplete.

Severity: breaking = consumer will fail; degraded = silent violation possible; cosmetic = non-correctness difference.

Automate / Connectors lens: for at least one finding, explicitly call out integration-level impact or confirm its absence.

---

**Step 6 -- Patterns**

Write a `## Patterns` section immediately after the findings.

If total findings >= 2: scan finding hypotheses for shared root causes. For each group of two or more findings sharing a root cause:

```
Pattern P-NN
findings: [F-NN, F-MM, ...]
shared-root-cause: [one sentence describing the common mechanism]
single-fix: [one concrete fix that would close all findings in this group]
```

If no two findings share a root cause, write: `No patterns -- all findings have distinct root causes.`

If total findings < 2, omit this section.

The Patterns section reduces apparent finding count: three findings grouped under one pattern means one fix resolves all three.

---

**Step 7 -- Summary**

Write a `## Summary` section:
1. Finding counts: `breaking: N | degraded: N | cosmetic: N | total: N`
2. Pattern count: `patterns identified: N` (or `none`)
3. Verdict: `Contract violated` or `Contract satisfied`
4. Recommended-action index: one line per breaking finding -- `F-NN: [amend-spec | fix-impl] -- [rationale]` -- extracted from Step 5

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 -- All Aspirational Combined (C-09 + C-10 + C-11 + C-12)

**axis:** full aspirational combination
**hypothesis:** C-09, C-10, C-11, and C-12 address four independent failure modes in R1 top variants: missing amendment decisions, missing pattern grouping, silently incomplete finding fields, and contaminated expected output. All four can be addressed simultaneously without structural conflict. A gate token (C-12) operates at the Phase 1/2 boundary; labeled slots (C-11) operate at the finding block level; an inline amendment field (C-09) extends breaking findings only; a Patterns section (C-10) follows the findings list. These four mechanisms compose cleanly. A response that follows this variation fully scores 100 against the v2 rubric.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {describe or paste the input state used for this trace}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert (writes expected from spec) + Automate (executes and diffs).

---

**Step 1 -- Contract identity**

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline -- no external file references)
- Spec version and section governing this contract

Must be self-contained.

---

**Step 2 -- Expected output**

You are the Connectors contract expert. Write from the spec alone. Do not run the operation.

Write the `## Expected Output (from spec)` section. For each required element, state:
- The expected value or shape
- The spec clause that requires it

Cover all three contract surfaces: success path, error path, at least one edge case.

When the Expected Output section is complete, answer the gate check and write the gate token:

    GATE CHECK -- Is the Expected Output section complete and sealed?
    Answer: [YES -- all contract surfaces have expected elements with spec citations; no actual output observed]

    [EXPECTED SEALED -- execution begins here]

Do not write [EXPECTED SEALED] until the answer is YES. Do not begin Step 3 before this line. The Expected Output section must not be modified after this line.

---

**Step 3 -- Actual output**

You are Automate. The expected output is sealed above. Do not revise it.

Run or simulate the operation. Write the `## Actual Output` section: status code, full response body, all relevant headers, observable side effects.

---

**Step 4 -- Diff**

Write the `## Diff` section. Compare every element in the Expected Output section against the actual output.

- Match: satisfied -- contract honored
- Deviation: write a finding block (see Step 5)

If no deviations: write `## Diff -- Contract Satisfied` with `No deviations found.` and proceed to Step 7.

---

**Step 5 -- Classify findings**

For each deviation, write one finding block using the labeled-slot format. Every slot is required. An empty slot means the finding is incomplete -- fill it before moving to the next finding:

```
Finding F-NN
  deviation        : [REQUIRED -- expected X, actual Y; both sides must be stated]
  severity         : [REQUIRED -- exactly one of: breaking | degraded | cosmetic]
  spec-ref         : [REQUIRED -- spec clause, section, or field definition violated]
  root-cause       : [REQUIRED -- one sentence cause; name a mechanism, not restate the deviation]
  connector-impact : [REQUIRED -- does this break Automate mappings or schema bindings? state explicitly]
```

For every finding where severity is `breaking`, append one additional required slot immediately:

```
  recommended-action : [REQUIRED for breaking -- amend-spec | fix-impl -- rationale: which side is wrong and why]
```

A breaking finding without recommended-action is incomplete. The rationale must argue which side is wrong -- spec or implementation -- not merely that they differ.

Severity: breaking = consumer will fail; degraded = silent violation possible; cosmetic = non-correctness difference.

---

**Step 6 -- Patterns**

Write a `## Patterns` section immediately after all finding blocks.

If total findings >= 2: scan root-cause slots for shared mechanisms. For each group of two or more findings sharing a root cause:

```
Pattern P-NN
  findings         : [F-NN, F-MM, ...]
  shared-root-cause: [one sentence describing the common mechanism]
  single-fix       : [one concrete fix that closes all findings in this group]
```

If no two findings share a root cause: write `No patterns -- all findings have distinct root causes.`

If total findings < 2: omit this section.

---

**Step 7 -- Summary**

Write a `## Summary` section:
1. Finding counts: `breaking: N | degraded: N | cosmetic: N | total: N`
2. Pattern count: `patterns identified: N` (or `none`)
3. Verdict: `Contract violated` or `Contract satisfied`
4. Recommended-action index: one line per breaking finding -- `F-NN: [amend-spec | fix-impl] -- [rationale]` -- extracted from the finding blocks above

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## Evaluation Order Guidance

| Priority | Variation | Rationale |
|----------|-----------|-----------|
| 1 | V-01 (phase-gate) | Tests C-12 in isolation. Gate question + token is the minimal change from R1 baseline. Establishes whether C-12 requires a question-answer pattern or just a named lock token. |
| 2 | V-02 (structural field enforcement) | Tests C-11 in isolation. Column-aligned slots are directly measurable. Establishes whether labeled slots self-announce gaps or whether models fill them from prose habits. |
| 3 | V-03 (amendment in finding format) | Tests C-09 with the inline-block approach. If V-03 passes C-09 and V-04 adds no improvement, the inline approach is sufficient. |
| 4 | V-04 (C-09 + C-10 combined) | Tests C-10 pattern recognition. Evaluate after V-03 establishes C-09 baseline -- isolates C-10 marginal contribution. |
| 5 | V-05 (all four aspirational) | Full integration test. Expected score: 100. Evaluate last to confirm all four mechanisms compose without interference. |

## Round 2 Combination Candidates for Round 3

| Priority | Axis Pair | Rationale |
|----------|-----------|-----------|
| 1 | V-01 (gate) + V-02 (labeled slots) | Gate lock handles C-12; labeled slots handle C-11. No interference. Expected score: 95. Useful intermediate if V-05 does not reach 100. |
| 2 | V-03 (amendment) + V-01 (gate) | Smallest structural additions to R1 baseline. If this combination scores 95 without labeled slots or patterns, V-05 becomes an incremental addition rather than a full rewrite. |
