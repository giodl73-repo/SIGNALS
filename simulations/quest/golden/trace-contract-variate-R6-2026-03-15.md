# trace-contract Variate — Round 6

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v6 (C-21 + C-22 + C-23 introduced; denominator increases to 106 pts)
**Round:** R6 — three single-axis passes targeting C-21/C-22/C-23 + two combination passes

---

## Round 6 Variation Map

| Variation | Axis | C-21 | C-22 | C-23 | Notes |
|-----------|------|------|------|------|-------|
| V-01 | Role-separated Expected authorship | PASS | — | — | Single-axis: named Contract Author role with no runtime knowledge; Automate prohibited from modifying Expected; disagreement = finding |
| V-02 | Pre-authoring rules block at document head | — | PASS | — | Single-axis: numbered rules block before any Expected content, covering all three mandated items |
| V-03 | Taxonomy declared pre-gate in Expected phase | — | — | PASS | Single-axis: mechanism taxonomy declared and sealed inside Phase 1 before gate commits; Phase 3 vocabulary is bound pre-gate |
| V-04 | Role separation + Pre-authoring rules | PASS | PASS | — | Combination: rules block names the role prohibition before the Contract Author writes anything; C-22 is the delivery mechanism for C-21 |
| V-05 | Full: Role separation + Pre-authoring rules + Pre-gate taxonomy | PASS | PASS | PASS | Platinum target: all three v6 mechanisms; pre-authoring rules cover all three mandated items; taxonomy sealed before gate; Automate's vocabulary bound before execution |

---

## V-01 — Role-Separated Expected Authorship

**axis:** C-21 role-separated Expected authorship

**hypothesis:** C-01 and C-04 in earlier rounds were instruction targets — the prompt told the analyst not to infer from runtime and to include spec references. C-21 converts those instructions into structural properties by assigning Phase 1 authorship to a named role (Contract Author) who is explicitly declared to have no runtime knowledge. A role that has not observed the runtime cannot rationalize toward it — not because of a prohibition, but because the rationalization pathway requires runtime knowledge the role does not possess. The executing role (Automate) encounters the Expected section as a committed artifact that predates its activation. Any disagreement Automate has with Expected entries must be logged as a finding, not resolved by editing — the Expected section was authored by a different role before Automate existed in the document.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state description or inline fixture — state inline, not by reference}
**Spec source:** {spec file path and section — e.g., signal-trace-2026-03-14.md#trace-contract}

---

## Authorship Declaration

This artifact is authored in two phases by two distinct roles.

**Phase 1 — Expected Output** is the exclusive work of: **Contract Author**

The Contract Author has not observed the runtime. The Contract Author has not run the operation. The Contract Author reads the spec alone and states what the operation must produce. The Contract Author's work is complete when the commit gate is written.

**Phase 3 — Diff and Findings** is the exclusive work of: **Automate**

Automate has observed the runtime. Automate MUST NOT modify, supplement, correct, or annotate Phase 1 content. If Automate believes a Phase 1 entry is wrong, incomplete, or inconsistent with the spec, that belief is a **finding** — it is not a license to edit the Expected section. Any deviation between Phase 1 entries and Phase 3 observations is a finding with the deviation pointing both directions: what Phase 1 said and what Phase 3 observed.

Shared authorship of the Expected section — or failure to attribute Phase 1 to the Contract Author — makes this artifact a single-author trace and removes the authoring wall.

---

### CONTRACT AUTHOR — your steps follow

**Step 1 — Contract Scope**

Write a `## Contract Scope` section. Include:
- Operation name and HTTP method (or equivalent)
- Connector or Automate context and environment
- Input fixture — stated inline; do not reference external files
- Spec version and section governing this contract

This section must be self-contained. A scope that requires the reader to open an external file fails this step.

---

**Step 2 — Expected Output (your section — complete before runtime begins)**

Write the `## Expected Output` section from the spec alone.

For each expected element:
- State the element (e.g., `status: 200`, `body.items: array`, `header X-Request-Id: present`)
- Cite the spec clause that requires it (e.g., `spec §3.2: success response must include items array`)

An expected element without a spec reference is not a valid contract entry. Remove it or find the reference before committing. Do not carry unanchored entries past the gate.

Write three independent labeled surface blocks — not rows in a shared table:

**Block: Success Path**
Expected nominal output for nominal input. One element per line with spec citation.

**Block: Error Path**
Expected error response for malformed, missing, or unauthorized input. One element per line with spec citation. If the spec does not define an error contract, write: `Error path: not specified in spec — omitted by Contract Author.`

**Block: Edge Case — [name the edge explicitly]**
Expected behavior for at least one edge condition (empty collection, null required field, auth expiry, overflow, rate-limit trigger). Name the edge in the block heading. One element per line with spec citation.

Each block is a required section. A surface block may not be silently omitted — if a surface has no expected content, write the block heading and state why.

---

**COMMIT GATE**

When all three surface blocks are complete and every expected element has a spec reference, write exactly:

> `[CONTRACT COMMITTED — no modifications after this gate. Contract Author's role ends here. Automate begins after this line.]`

The gate is the structural proof that Phase 1 was completed by a role that had not observed the runtime. The Contract Author may not add, remove, or revise Expected entries after this line. Automate may not add, remove, or revise Expected entries at any point.

---

### AUTOMATE — your steps begin at the gate

The Contract Author has committed the expected output above. Your role begins at the commit gate line. DO NOT modify the Expected Output section for any reason. If you believe an entry there is wrong, log it as a finding.

---

**Step 3 — Actual Output**

Run or simulate the operation against the input fixture. Write the `## Actual Output` section. Include: status code, full response body, all relevant headers, observable side effects.

---

**Step 4 — Diff (three independent surface blocks required)**

Write one diff block per contract surface. Every block is required — even if clean.

**Diff Block: Success Path**
For each expected success-path element by name: write `✓ [element] — satisfied` or begin a finding. If no deviations: `Success path: no deviations — contract satisfied for this surface.`

**Diff Block: Error Path**
For each expected error-path element by name: write `✓ [element] — satisfied` or begin a finding. If no deviations: `Error path: no deviations — contract satisfied for this surface.` If Phase 1 omitted this surface: `Error path: omitted by Contract Author — no diff possible.`

**Diff Block: Edge Case — [edge name from Phase 1]**
For each expected edge element by name: write `✓ [element] — satisfied` or begin a finding. If no deviations: `[Edge name]: no deviations — contract satisfied for this surface.`

A diff that folds all surfaces into a single flat list without surface attribution fails. A missing surface block fails.

---

**Step 5 — Findings**

For every deviation found across all diff blocks, write a finding entry:

```
Finding F-NN
surface: success | error | edge
deviation: [expected X per Phase 1, actual Y per Phase 3 — both sides required]
severity: breaking | degraded | cosmetic
spec: [spec clause cited in Phase 1 for this element]
hypothesis: [causal mechanism — not a restatement of the deviation]
recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
```

Severity definitions:
- `breaking` — a consumer relying on the contract cannot function correctly
- `degraded` — the operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — the output differs but correctness and consumer behavior are unaffected

DO NOT write a hypothesis that restates the deviation. "The output did not match the expected value" describes what happened, not why it happened.

---

**Step 6 — Summary**

Write a `## Summary` section:
1. Severity counts: `breaking: N | degraded: N | cosmetic: N | total: N`
2. Surface status: one line per surface — `[Surface]: satisfied / N findings`
3. Verdict: `Contract violated` or `Contract satisfied`
4. For every `breaking` or `degraded` finding: `F-NN recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Pre-Authoring Rules Block at Document Head

**axis:** C-22 pre-authoring rules block at document head

**hypothesis:** The criteria C-18 (independent surface blocks), C-19 (spec-reference removal imperative), and C-23 (pre-gate taxonomy) all describe authoring constraints — but in prior rounds they were embedded in the body of phase instructions, where they function as scoring criteria checked after the fact rather than authoring rules consulted before writing. An analyst who reads phase instructions while writing can rationalize toward compliance during scoring. An analyst who reads a numbered rules block before writing anything cannot retroactively claim ignorance. Moving the constraints to document head — numbered, imperative, and placed before any Expected content instructions — converts them from rubric checks into authoring norms. The analyst reads the rules before opening a text editor. The rules are present at the moment of first temptation, not discovered at the moment of evaluation.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state description or inline fixture}
**Spec source:** {spec file path and section}

---

## PRE-AUTHORING RULES

Read these rules before writing any Expected content. These rules govern authorship. They are not scoring criteria — they are constraints that bind you before the first field is written.

**Rule 1 — Spec-anchoring imperative.**
Every expected value in Phase 1 must cite the spec clause that requires it. An expected value without a spec reference is not a valid contract entry. Do not carry it past the gate — remove it, or find the reference first. "Seems reasonable" is not a spec reference. A section name is not a spec reference. The clause that makes the value required is the reference.

**Rule 2 — Independent surface block mandate.**
Phase 1 must contain one structurally independent labeled section per contract surface: success path, error path, and edge case. A flat list with a Surface column is not compliant. A table with surface as a row attribute is not compliant. Each surface must be its own section. A surface with no expected elements must carry its heading with an explicit acknowledgment — omitting a surface block entirely is not permitted.

**Rule 3 — Pre-gate taxonomy declaration requirement.**
The mechanism taxonomy used for hypotheses in Phase 3 must be declared inside Phase 1, before the commit gate. Write the taxonomy as a named list in Phase 1. The vocabulary becomes binding on Phase 3 at gate commit. Declaring the taxonomy for the first time in Phase 3 — after observing deviations — is not permitted. A post-hoc taxonomy can be shaped around findings. A pre-gate taxonomy must honestly anticipate failure modes from the spec, not from the output.

These three rules take effect the moment you begin Phase 1. A document that violates any rule is not a valid contract trace.

---

Stock roles: Connectors contract expert (Phase 1) + Automate (Phase 3). Phase 1 is complete at the commit gate. Phase 3 does not begin until the gate is written.

---

**Phase 0 — Contract Scope**

Write a `## Contract Scope` section:
- Operation name and HTTP method
- Connector or Automate context and environment
- Input fixture — stated inline, not by reference to external files
- Spec version and section governing this contract

---

**Phase 1 — Expected Output**

Write the `## Expected Output` section from the spec alone, before running the operation.

Follow Rule 1: every element cites the spec clause. Follow Rule 2: write three independent labeled surface blocks.

**Block: Success Path**
Expected nominal output for nominal input. Per element: state the element and its spec clause.

**Block: Error Path**
Expected error response per spec. Per element: state the element and its spec clause. If spec does not define an error contract, write this block as: `Error path: not specified in spec — no contract entries.`

**Block: Edge Case — [name the edge]**
Expected behavior for at least one edge condition. Name the edge in the heading. Per element: state the element and its spec clause.

Follow Rule 3: before closing Phase 1, declare the mechanism taxonomy as a named section titled `## Mechanism Taxonomy`. List the mechanisms that will be available to Phase 3 authors. Seal the taxonomy before the commit gate.

---

**COMMIT GATE**

Write:

> `[CONTRACT COMMITTED — no modifications after this gate]`

The gate seals Phase 1 content and the mechanism taxonomy simultaneously. No Expected entries and no taxonomy entries may be added, removed, or revised after this line.

---

**Phase 2 — Actual Output**

Run or simulate the operation. Write the `## Actual Output` section: status code, full response body, headers, observable side effects.

---

**Phase 3 — Diff**

Write one labeled diff block per contract surface:

**Diff Block: Success Path**
For each expected element by name: `✓ [element] — satisfied` or write a finding. If clean: `Success path: no deviations.`

**Diff Block: Error Path**
For each expected element by name: `✓ [element] — satisfied` or write a finding. If clean: `Error path: no deviations.`

**Diff Block: Edge Case — [edge name from Phase 1]**
For each expected element by name: `✓ [element] — satisfied` or write a finding. If clean: `[Edge name]: no deviations.`

---

**Findings**

For every deviation, write:

```
Finding F-NN
surface: success | error | edge
deviation: [expected X, actual Y — both sides]
severity: breaking | degraded | cosmetic
spec: [spec clause from Phase 1]
hypothesis:
  mechanism: [select from the taxonomy declared in Phase 1]
  explanation: [one sentence — causal mechanism, not a symptom restatement]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]
```

The mechanism field must select from the taxonomy sealed in Phase 1. Do not introduce a mechanism that was not declared pre-gate.

Severity: `breaking` = consumer fails | `degraded` = silent violation | `cosmetic` = non-correctness difference

DO NOT write a hypothesis whose explanation begins "The output did not match" or "The actual value differed from" — that is a symptom restatement, not a hypothesis, regardless of mechanism label.

---

**Summary**

Write a `## Summary` section:
1. Severity counts: `breaking: N | degraded: N | cosmetic: N | total: N`
2. Mechanism distribution: one line per mechanism used (e.g., `field-mapping-gap: 2 | wrong-enum: 1`)
3. Surface status: one line per surface
4. Verdict: `Contract violated` or `Contract satisfied`
5. Recommendations for every `breaking` or `degraded` finding

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Taxonomy Declared Pre-Gate in Expected Phase

**axis:** C-23 mechanism taxonomy declared and sealed in Phase 1 before the gate commits

**hypothesis:** C-13 (mechanism taxonomy enforcement) requires that every hypothesis selects a category from a declared taxonomy. In prior rounds, the taxonomy appears in Phase 3 — at the point where the analyst is classifying deviations they have already observed. A Phase 3 taxonomy is selected after the analyst knows what the findings are; the analyst can shape the taxonomy — consciously or not — toward mechanisms that match the findings rather than mechanisms that the spec honestly predicts as possible failure modes. Declaring the taxonomy in Phase 1, as a sub-step inside the Expected phase before the gate commits, reverses this: the analyst must name the failure modes they expect given the spec before observing any deviation. A pre-gate taxonomy that lists `field-mapping-gap` is a prediction — it forces the analyst to reason about the spec's data model before running the operation. A post-hoc taxonomy that lists `field-mapping-gap` is a label applied after the gap was already found. The pre-gate placement makes the taxonomy an independent diagnostic instrument rather than a post-hoc classification system.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state description or inline fixture}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert (writes and commits Phase 1) + Automate (captures Phase 2, diffs Phase 3, classifies Phase 4).

---

**Step 1 — Contract Scope**

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture — stated inline
- Spec version and section governing this contract

---

**Step 2 — Expected Output**

Write the `## Expected Output` section from the spec alone. For each expected element, cite the spec clause.

Required contract surfaces — write three independently labeled blocks:

**Block: Success Path**
Expected nominal output for nominal input. One element per line with spec citation.

**Block: Error Path**
Expected error response for invalid or unauthorized input. One element per line with spec citation. If spec defines no error contract: write the block as `Error path: not specified in spec.`

**Block: Edge Case — [name the edge]**
Expected behavior for at least one edge condition. Name the edge in the heading. One element per line with spec citation.

An expected element without a spec reference is not a valid contract entry. Remove it or find the reference before committing.

---

**Step 2B — Mechanism Taxonomy (seal before the gate)**

Before committing, declare the mechanism taxonomy. Write it as a numbered list under `## Mechanism Taxonomy (pre-gate)`.

The taxonomy is your prediction of the failure modes this operation is susceptible to, given what you know from the spec alone. Each entry names a mechanism and explains the failure mode it covers.

Required: at minimum four mechanisms. Suggested starting set — modify based on this operation's spec:

1. **field-mapping-gap** — a field required by the contract is not mapped in the implementation
2. **wrong-enum** — an enumerated value is serialized or deserialized using the wrong member
3. **serialization-path** — a value exists internally but is transformed incorrectly during output (wrong type, encoding, or format)
4. **missing-guard** — a conditional branch that should handle an error or edge case is absent, causing fallthrough
5. **logic-branch** — the implementation selects the wrong execution path for the given input
6. **contract-ambiguity** — the spec clause governing this element is underspecified or contradictory

You may add mechanisms to this list if the spec makes other failure modes plausible. You may remove mechanisms if none of this operation's contract elements is susceptible to them — but justify each removal with a note. You may NOT add mechanisms in Phase 3. The taxonomy is sealed at the gate.

---

**COMMIT GATE**

When the Expected Output blocks and the Mechanism Taxonomy are both complete, write:

> `[CONTRACT COMMITTED — taxonomy sealed. Phase 3 authors are bound to the mechanisms declared above. No taxonomy additions after this gate.]`

---

**Step 3 — Actual Output**

Run or simulate the operation. Write the `## Actual Output` section: status code, full response body, headers, side effects.

---

**Step 4 — Diff (three surface blocks)**

Write one labeled diff block per contract surface:

**Diff Block: Success Path**
For each expected element by name: `✓ [element] — satisfied` or write a finding. If clean: `Success path: no deviations.`

**Diff Block: Error Path**
For each expected element by name: `✓ [element] — satisfied` or write a finding. If clean: `Error path: no deviations.`

**Diff Block: Edge Case — [edge name from Phase 1]**
For each expected element by name: `✓ [element] — satisfied` or write a finding. If clean: `[Edge name]: no deviations.`

---

**Step 5 — Findings**

For every deviation, write:

```
Finding F-NN
surface: success | error | edge
deviation: [expected X per spec, actual Y per runtime — both sides]
severity: breaking | degraded | cosmetic
spec: [spec clause from Phase 1]
hypothesis:
  mechanism: [select from the taxonomy sealed in Step 2B — no new mechanisms]
  explanation: [one sentence stating why that mechanism produced this deviation]
recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
```

The mechanism MUST be selected from the taxonomy sealed in Step 2B. A mechanism not in the pre-gate list is not available.

If no mechanism fits, use the closest one and explain the gap in the explanation field — do not invent a new mechanism label.

Severity: `breaking` = consumer cannot rely on contract | `degraded` = silent violation possible | `cosmetic` = non-correctness difference

DO NOT write an explanation that begins "The output did not match" — that is a symptom restatement. The explanation must state why the mechanism produced this specific deviation, not describe what the deviation was.

---

**Step 6 — Summary**

Write a `## Summary` section:
1. Severity counts: `breaking: N | degraded: N | cosmetic: N | total: N`
2. Mechanism distribution: one line per mechanism used in findings (e.g., `field-mapping-gap: 2 | missing-guard: 1`)
3. Surface status: one line per surface — `[Surface]: satisfied / N findings`
4. Verdict: `Contract violated` or `Contract satisfied`
5. Recommendation for every `breaking` or `degraded` finding: `F-NN recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Role Separation + Pre-Authoring Rules Block

**axes:** C-21 role-separated Expected authorship + C-22 pre-authoring rules block at document head

**hypothesis:** In V-01, the role attribution (Contract Author, no runtime knowledge) appears at the document head as an Authorship Declaration. In V-02, the pre-authoring rules block appears at the document head as a numbered constraint list. Combined, these two mechanisms occupy the same architectural position — the document head — and address the same failure mode from different angles: C-22 names the constraints before the analyst writes; C-21 names the identity of the writer before the analyst writes. Together they form a two-layer gate: the analyst learns their constraints (rules block) and their identity (role attribution) before writing the first field. In isolation, either mechanism can be bypassed by an analyst who treats it as boilerplate. Together, the rules block provides the specific prohibitions and the role attribution provides the identity constraint that makes those prohibitions binding. An analyst who has been told "you are Contract Author, you have not observed the runtime, you are now reading the rules for Contract Author" cannot rationalize away rule 1 as "that applies to the other role."

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state description or inline fixture}
**Spec source:** {spec file path and section}

---

## Role Assignment

This document is authored by two roles in strict sequence.

**Contract Author** writes Phase 1 (Expected Output). Contract Author has not run the operation. Contract Author has not observed any runtime output. Contract Author reads the spec alone.

**Automate** writes Phase 2 (Actual Output) and Phase 3 (Diff and Findings). Automate's work begins at the commit gate. Automate MUST NOT modify Phase 1 content. If Automate finds a Phase 1 entry inconsistent with the runtime, that inconsistency is a finding — it is not a license to correct the entry. The Expected section was authored by a role that did not have access to the runtime; any entry there that turns out to be wrong represents a spec-reading error or a spec gap, and must be preserved as a finding target.

---

## Pre-Authoring Rules (Contract Author reads these before writing Phase 1)

**Rule 1 — Spec-anchoring imperative.**
Every expected value in Phase 1 must cite the spec clause that requires it. An expected value without a spec reference is not a valid contract entry. Remove it or find the reference — do not carry unanchored entries past the gate. "Based on prior behavior" is not a spec reference. A section heading is not a spec reference. The clause that makes the value required is the reference.

**Rule 2 — Independent surface block mandate.**
Phase 1 must contain three structurally independent labeled sections: Success Path, Error Path, and Edge Case. A flat list without section headings is not compliant. A single table with a Surface column is not compliant. Each surface must be its own labeled block. A surface block with no content must still appear — write the block heading and state the reason (e.g., "not specified in spec").

**Rule 3 — Pre-gate taxonomy declaration requirement.**
The mechanism taxonomy that Phase 3 (Automate) will use for hypotheses must be declared inside Phase 1, before the commit gate. Contract Author declares the taxonomy as a prediction from the spec. The taxonomy vocabulary is binding on Automate from gate commit forward. Automate may not add, rename, or remove taxonomy entries in Phase 3.

These rules govern the Contract Author's work from this line forward.

---

### Phase 1 — Contract Author's Work

**Step 1 — Contract Scope**

Write a `## Contract Scope` section:
- Operation name and HTTP method
- Connector or Automate context and environment
- Input fixture — stated inline
- Spec version and section governing this contract

---

**Step 2 — Expected Output**

Write the `## Expected Output` section from the spec alone.

Apply Rule 1 (every element has a spec citation) and Rule 2 (three independent surface blocks):

**Block: Success Path**
Expected nominal output for nominal input. One element per line with spec citation.

**Block: Error Path**
Expected error response for invalid or unauthorized input. One element per line with spec citation. If spec does not define an error contract: `Error path: not specified in spec — no contract entries.`

**Block: Edge Case — [name the edge explicitly]**
Expected behavior for at least one edge condition. Name the edge in the block heading. One element per line with spec citation.

---

**Step 2B — Mechanism Taxonomy (Rule 3 — declare and seal before the gate)**

Write the taxonomy under `## Mechanism Taxonomy`. Name each mechanism and the failure mode it covers.

Minimum required mechanisms:
- **field-mapping-gap** — required field absent or mapped to wrong path
- **wrong-enum** — enumerated value serialized using wrong member
- **serialization-path** — value transformed incorrectly during output
- **missing-guard** — absent conditional branch causes fallthrough at error or edge
- **logic-branch** — implementation selects wrong execution path for this input
- **contract-ambiguity** — spec clause is underspecified or contradictory

Add mechanisms if this operation's spec makes additional failure modes plausible. Remove mechanisms only with a written justification. This list is sealed at the gate.

---

**COMMIT GATE**

When Expected Output and Mechanism Taxonomy are complete:

> `[CONTRACT COMMITTED — no modifications after this gate. Contract Author's role ends. Automate begins. Taxonomy sealed — no taxonomy additions in Phase 3.]`

---

### Phase 2 — Automate's Work begins here

The Contract Author has committed the expected output and mechanism taxonomy above. Your role begins at this gate. DO NOT modify any Phase 1 content. Any disagreement with a Phase 1 entry is a finding.

---

**Step 3 — Actual Output**

Run or simulate the operation. Write the `## Actual Output` section: status code, full response body, all headers, observable side effects.

---

**Step 4 — Diff (three required surface blocks)**

Write one labeled diff block per surface. Every block is required.

**Diff Block: Success Path**
For each expected element by name: `✓ [element] — satisfied` or write a finding. If clean: `Success path: no deviations — contract satisfied for this surface.`

**Diff Block: Error Path**
For each expected element by name: `✓ [element] — satisfied` or write a finding. If clean: `Error path: no deviations.` If Phase 1 omitted this surface: `Error path: omitted in Phase 1 — no diff possible.`

**Diff Block: Edge Case — [name from Phase 1]**
For each expected element by name: `✓ [element] — satisfied` or write a finding. If clean: `[Edge name]: no deviations.`

A diff that folds surfaces into a flat list without block attribution fails. A missing surface block fails.

---

**Step 5 — Findings**

For every deviation found in any diff block:

```
Finding F-NN
surface: success | error | edge
deviation: [expected X per Phase 1, actual Y per Phase 2 — both sides]
severity: breaking | degraded | cosmetic
spec: [spec clause cited in Phase 1 for this element]
hypothesis:
  mechanism: [select from the taxonomy in Phase 1 — must be a declared mechanism]
  explanation: [one sentence — why the mechanism produced this deviation, not what the deviation was]
recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
```

Mechanism must be selected from the Phase 1 taxonomy. DO NOT introduce a mechanism not declared pre-gate.

Severity: `breaking` = consumer cannot rely on contract | `degraded` = silent violation possible | `cosmetic` = non-correctness difference

DO NOT write an explanation that begins "The output did not match" or "The actual value was different." Those are symptom restatements. The explanation names the mechanism and states why that mechanism produced this specific deviation.

---

**Step 6 — Summary**

Write a `## Summary` section:
1. Severity counts: `breaking: N | degraded: N | cosmetic: N | total: N`
2. Mechanism distribution: one line per mechanism used in findings
3. Surface status: one line per surface
4. Verdict: `Contract violated` or `Contract satisfied`
5. Recommendation for every `breaking` or `degraded` finding

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — Full: Role Separation + Pre-Authoring Rules + Pre-Gate Taxonomy

**axes:** C-21 role-separated Expected authorship + C-22 pre-authoring rules block + C-23 taxonomy declared pre-gate

**hypothesis:** The three v6 architectural properties operate at distinct temporal positions in the document and close distinct rationalization pathways. C-22 (pre-authoring rules block) fires at document head — before any content is written. Its three mandated items cover spec-anchoring, surface architecture, and taxonomy timing. C-21 (role-separated authorship) fires at role declaration — it establishes the Contract Author's ignorance of runtime as an identity fact, not an instruction. C-23 (pre-gate taxonomy) fires inside Phase 1 — it forces the Contract Author to commit to a mechanism vocabulary before observing any deviation. Together they form a three-point temporal enforcement chain: rules before authoring → identity before writing → vocabulary before execution. A document with all three mechanisms cannot rationalize backward at any entry point: not at document head (C-22 blocks it), not at the Expected section (C-21 removes the runtime-knowledge required for rationalization), and not at Phase 3 hypothesis writing (C-23 seals the vocabulary before deviations are known). V-05 tests whether these three properties compound cleanly or whether layering them produces interference.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state description or inline fixture}
**Spec source:** {spec file path and section}

---

## Pre-Authoring Rules

Read these rules before writing any content. These are authoring constraints — they govern how the document is written, not how it is scored.

**Rule 1 — Spec-anchoring imperative.**
Every expected value in Phase 1 must cite the spec clause that requires it. An expected value without a spec reference is not a valid contract entry. Remove it or find the reference before the commit gate. Do not carry unanchored entries past the gate. Citing a section heading is not sufficient — cite the clause within the section that makes the value required.

**Rule 2 — Independent surface block mandate.**
Phase 1 must contain three structurally independent labeled sections: Success Path, Error Path, and Edge Case. A flat list is not compliant. A table with a Surface column is not compliant. A surface block with no expected elements must still appear — write the heading and state why there are no entries. Omitting a surface block entirely is not permitted.

**Rule 3 — Pre-gate taxonomy declaration requirement.**
The mechanism taxonomy used for hypotheses must be declared inside Phase 1, before the commit gate commits. The taxonomy is a prediction from the spec — what failure modes are plausible given the operation's contract. The vocabulary is binding on Phase 3 authors at gate commit. Adding, renaming, or removing taxonomy entries in Phase 3 is not permitted.

These rules bind Contract Author beginning now.

---

## Role Assignment

**Contract Author** is responsible for Phase 1 (Expected Output, Mechanism Taxonomy, and Commit Gate). Contract Author has not run the operation and has not observed any runtime output. Contract Author reads the spec alone. Contract Author's work ends when the gate line is written.

**Automate** is responsible for Phase 2 (Actual Output), Phase 3 (Diff), and Phase 4 (Findings and Summary). Automate's work begins at the commit gate. Automate MUST NOT modify, supplement, annotate, or correct Phase 1 content. If Automate disagrees with a Phase 1 entry — believes it is wrong, incomplete, or inconsistent — that disagreement is a **finding**. The Phase 1 entry was authored by a role that had not observed the runtime; Automate's observation that the runtime differs from the entry is precisely the signal this artifact is designed to capture.

---

### Contract Author — Phase 1

**Step 1 — Contract Scope**

Write a `## Contract Scope` section. Must be self-contained:
- Operation name and HTTP method (or equivalent)
- Connector or Automate context and environment
- Input fixture — stated inline; do not reference external files
- Spec version and section governing this contract

A Contract Scope that requires the reader to open an external file to understand what is being tested fails this step.

---

**Step 2 — Expected Output**

Write the `## Expected Output` section from the spec alone.

Apply Rule 1 (every element cites a spec clause) and Rule 2 (three independent surface blocks):

**Block: Success Path**
Expected nominal output for nominal input. For each element: state the field/value and the spec clause that requires it.

```
[field]: [expected value or shape]
spec: [clause, section, and line reference]
```

**Block: Error Path**
Expected error response for malformed, missing, or unauthorized input. For each element: state the field/value and spec clause. If spec does not define an error contract for this operation: write `Error path: not specified in spec — Contract Author omits. This surface is not available for diff.`

```
[field]: [expected value or shape]
spec: [clause, section, and line reference]
```

**Block: Edge Case — [name the specific edge condition]**
Expected behavior for at least one edge condition (empty collection, null required field, auth expiry, overflow, rate-limit trigger). Name the edge in the block heading. For each element: state the field/value and spec clause.

```
[field]: [expected value or shape]
spec: [clause, section, and line reference]
```

---

**Step 2B — Mechanism Taxonomy (Rule 3 — declare and seal before the gate)**

Write the taxonomy under `## Mechanism Taxonomy (sealed pre-gate)`.

This is your prediction, as Contract Author reading the spec, of the failure modes this operation is susceptible to. Phase 3 authors are bound to this vocabulary — they may not introduce mechanisms not listed here.

| Mechanism | Failure Mode | Plausibility for This Operation |
|-----------|-------------|--------------------------------|
| field-mapping-gap | A field required by the contract is absent in the output or mapped to the wrong path | [state why this is plausible given the spec, or "low — omit if not plausible"] |
| wrong-enum | An enumerated value serialized using the wrong member | [state why...] |
| serialization-path | A value exists internally but is transformed incorrectly during output (wrong type, encoding, or format) | [state why...] |
| missing-guard | A conditional branch that should handle an error or edge case is absent, causing fallthrough to an unintended path | [state why...] |
| logic-branch | The implementation selects the wrong execution path for the given input — a condition evaluates incorrectly | [state why...] |
| contract-ambiguity | The spec clause governing this element is underspecified or contradictory — the implementation may be correct under one reading | [state why...] |

Remove a mechanism only if you can state why it is implausible for this specific operation's contract. Add a mechanism only now — not in Phase 3.

---

**COMMIT GATE**

When all three surface blocks are complete (every entry anchored to a spec clause), and the mechanism taxonomy is written and justified:

> `[CONTRACT COMMITTED — taxonomy sealed. No Expected entries and no taxonomy entries may be added, removed, or revised after this gate. Contract Author's role ends here. Automate begins after this line.]`

The gate is the structural proof that Phase 1 was authored before runtime observation and that the mechanism vocabulary was committed before deviations were known.

---

### Automate — Phases 2, 3, and 4

The Contract Author has committed the expected output and mechanism taxonomy above. Your role begins at the commit gate. DO NOT modify Phase 1 content. Any disagreement with a Phase 1 entry is a finding.

---

**Step 3 — Actual Output**

Run or simulate the operation against the input fixture stated in Contract Scope. Write the `## Actual Output` section: status code, full response body, all relevant headers, observable side effects. Capture the full response — do not summarize.

---

**Step 4 — Diff (three required surface blocks)**

Write one independently labeled diff block per contract surface. Every block is required — even if clean.

**Diff Block: Success Path**
Compare every expected success-path element (listed by field name in Phase 1) against actual output:
- For each element: `✓ [field] — [expected value]: satisfied` or begin a finding entry
- If all elements satisfied: `Success path: no deviations — contract satisfied for this surface.`
- A surface-level "no deviations" statement without enumerating individual fields = partial coverage.

**Diff Block: Error Path**
Compare every expected error-path element against actual output:
- For each element: `✓ [field] — [expected value]: satisfied` or begin a finding entry
- If all elements satisfied: `Error path: no deviations — contract satisfied for this surface.`
- If Phase 1 omitted this surface: `Error path: omitted by Contract Author — diff not possible.`

**Diff Block: Edge Case — [edge name from Phase 1]**
Compare every expected edge element against actual output:
- For each element: `✓ [field] — [expected value]: satisfied` or begin a finding entry
- If all elements satisfied: `[Edge name]: no deviations — contract satisfied for this surface.`

A diff that folds all surfaces into a single flat list without block attribution fails. A missing surface block fails. Element-level enumeration is required — a surface-level acknowledgment without per-field confirmation counts as partial.

---

**Step 5 — Findings**

For every deviation found across all diff blocks, write a finding entry:

```
Finding F-NN
surface: success | error | edge
deviation: [expected X per Phase 1, actual Y per Phase 2 — both sides required]
severity: breaking | degraded | cosmetic
spec: [spec clause cited in Phase 1 for this element]
hypothesis:
  mechanism: [select from the Phase 1 taxonomy — no mechanism additions in Phase 3]
  explanation: [one sentence — why the mechanism produced this deviation; not what the deviation was]
recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
```

**Severity definitions:**
- `breaking` — a consumer relying on the contract cannot function correctly
- `degraded` — the operation runs but a guarantee is violated; silent failure or data loss is possible
- `cosmetic` — the output differs but correctness and consumer behavior are unaffected

**Hypothesis rules:**
- Mechanism MUST be selected from the taxonomy sealed in Phase 1. If none fits, use the closest and explain the gap in the explanation. Do not write a mechanism label that was not in the pre-gate list.
- DO NOT write an explanation that begins "The output did not match the expected value." That is a symptom restatement — it describes what happened, not why.
- DO NOT write an explanation that substitutes deviation terms into a template like "The [field] was not [value] because the [field] was not [value]." That is symptom restatement in mechanism dress.
- The explanation must state why the selected mechanism produced this specific deviation given the spec and the implementation.

**Recommendation coverage:**
Every finding of any severity — including `cosmetic` — must carry a `recommendation:` line. A cosmetic finding left without disposition is an incomplete finding.

---

**Step 6 — Summary**

Write a `## Summary` section:

1. **Severity distribution:** `breaking: N | degraded: N | cosmetic: N | total: N`
2. **Mechanism distribution:** one entry per mechanism used across all findings (e.g., `field-mapping-gap: 2 | missing-guard: 1 | wrong-enum: 0`)
3. **Surface status:** one line per surface — `Success path: satisfied / N findings` | `Error path: satisfied / N findings / not in spec` | `Edge case ([name]): satisfied / N findings`
4. **Verdict:** `Contract violated` or `Contract satisfied`
5. **Recommendations:** for every `breaking` or `degraded` finding:
   `F-NN recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]`

DO NOT omit a recommendation for any `breaking` or `degraded` finding.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## Combination Candidates for Round 7

| Priority | Axis Combination | Rationale |
|----------|-----------------|-----------|
| 1 | C-21 + C-23 (V-01 + V-03) | The role separation in V-01 creates a named author for Phase 1 but says nothing about the taxonomy timing. V-03 requires the taxonomy inside Phase 1. Together: the Contract Author who cannot observe the runtime is also the author who seals the mechanism vocabulary before execution. The taxonomy is then doubly protected — it predates execution and was authored by a role with no runtime knowledge. |
| 2 | C-22 + C-23 (V-02 + V-03) | The pre-authoring rules block in V-02 already contains Rule 3 (pre-gate taxonomy requirement), but Rule 3 is an instruction. V-03 operationalizes Rule 3 by providing the full taxonomy declaration sub-step inside Phase 1. Testing V-02 + V-03 together measures whether the rules block instruction is sufficient on its own or whether the sub-step structure is required for the taxonomy to actually appear pre-gate. |

## Evaluation Order Guidance

| Priority | Variation | Rationale |
|----------|-----------|-----------|
| 1 | V-03 (pre-gate taxonomy) | C-23 is entirely new in v6 and represents a temporal mechanism not tested in any prior round. Establish the baseline for this axis first — it has no dependency on V-01 or V-02 and may reveal interference with the existing C-13 mechanism in prior prompt bodies. |
| 2 | V-01 (role-separated authorship) | C-21 extends C-01 and C-04 structurally. Evaluating the structural role wall independently before combining with the rules block verifies that the role attribution alone is sufficient for C-21 pass without requiring the rules block as scaffolding. |
| 3 | V-02 (pre-authoring rules block) | C-22 is a format criterion — it checks whether a numbered block appears at document head. Evaluating it independently confirms the criterion can be satisfied by a pure format change before combining it with the role and taxonomy mechanisms. |
| 4 | V-04 (C-21 + C-22) | Tests whether the rules block is the natural delivery vehicle for the role prohibition — and whether the two mechanisms reinforce each other or whether the rules block makes the Role Assignment section redundant. |
| 5 | V-05 (all three) | Upper-ceiling test. Evaluate last to measure whether all three v6 mechanisms compound cleanly or whether the taxonomy sub-step in Phase 1 creates structural overhead that degrades the foundational criteria from earlier rounds. |
