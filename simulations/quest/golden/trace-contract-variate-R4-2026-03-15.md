# trace-contract Variate — Round 4 (rubric v16)

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v16 (C-01–C-10; essential C-01–C-05; golden threshold: all essential + composite >= 80)
**Round:** R4 — 3 single-axis (new sub-axis angles) + 2 combinations not yet attempted

---

## Round 4 Variation Map

| Variation | Axis | Primary Target | Hypothesis |
|-----------|------|----------------|------------|
| V-01 | phrasing-register (new angle: three named C-01 failure forms) | C-01 | Naming the three specific surface-compliant-but-substance-failing C-01 forms with examples closes the gap that generic prohibitions miss |
| V-02 | output-format (new angle: pre-printed placeholder slots) | C-02, C-03, C-04, C-05 | Pre-printed REQUIRED slot labels in every finding entry create a visual commitment cue that makes omission visible at write time, not at review time |
| V-03 | lifecycle-emphasis (new angle: surface-colocated diff blocks) | C-02, C-07 | Moving each surface's diff block immediately after its expected block eliminates the lost-context failure where edge-case elements are silently omitted from a monolithic diff |
| V-04 | role-sequence + hypothesis-architecture | C-01, C-05 | Sealing the causal mechanism taxonomy in the same commit gate as the expected contract binds Automate's hypothesis vocabulary before execution, preventing post-hoc category invention |
| V-05 | all five axes integrated | C-01–C-10 | Six mechanisms targeting six independent failure modes can be combined without degradation because each operates in a different phase against a different criterion |

---

## V-01 — Phrasing-Register: Three Named C-01 Failure Forms

**axis:** phrasing-register
**hypothesis:** R1 V-04 and R2 V-01 use "DO NOT infer expected from observed behavior" — a prohibition against a general failure class. C-01 fails in three more specific forms that look compliant on the surface but aren't: (1) **copy-from-prior** — the Expected section is taken from a prior trace of the same operation; the entries match spec but weren't re-derived from it, so spec amendments since the prior trace are silently absent; (2) **implementation-vocabulary contamination** — expected values use internal field names or behaviors from the current implementation rather than spec vocabulary, making the expected and actual mirrors of each other even when they don't violate the spec; (3) **spec-gap laundering** — "not specified in spec" is written for surfaces that are in fact defined but harder to derive, laundering the omission as a spec limitation. Naming all three with examples blocks the full failure space rather than the single most-obvious form.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {describe or paste the input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

**Step 1 — Contract Scope**

Write a `## Contract Scope` section:
- Operation name and HTTP method (or equivalent)
- Connector or Automate context and environment
- Input fixture — state inline; do not reference external files
- Spec version and section governing this operation's output contract

Self-contained. A reader must determine scope without opening another file.

---

**Step 2 — Expected Output**

Write the `## Expected Output` section from the spec alone. This is the contract.

**Before writing any expected element, read all three prohibited forms:**

**Prohibited Form A — Copy-from-Prior.** Do not reuse an Expected Output section from a previous trace of the same operation, even if the spec hasn't changed. C-01 requires derivation, not retrieval. Copy-from-prior is recognizable when expected elements use vocabulary that has since been updated in the spec, or when edge-case entries exactly match those in a prior artifact.

**Prohibited Form B — Implementation-Vocabulary Contamination.** Do not use the current implementation's field names, enum values, or behavior descriptions when the spec uses different vocabulary. Write expected values in spec vocabulary. An expected section that mirrors the implementation's output format because the operator knows the implementation satisfies C-01 in form but not in substance — the contract is a copy of the implementation, not a check on it.

**Prohibited Form C — Spec-Gap Laundering.** Do not write `not specified in spec` for a contract surface unless the spec genuinely defines no behavior for that surface. If the spec defines an error contract, an edge case, or a side effect somewhere other than the obvious section, find it. Laundering a hard-to-find spec requirement as a gap leaves the expected contract incomplete without any visible failure marker.

For each required element, state the element and cite the spec clause. Cover all three contract surfaces the spec defines:
- **Success path** — nominal input → expected nominal output
- **Error path** — invalid or missing input → expected error response (if genuinely not in spec: write "error contract: not defined in spec — confirmed by searching all sections")
- **At least one edge case** — empty collection, null required field, rate-limit trigger, or auth expiry

When complete, write: `[CONTRACT COMMITTED — Automate begins here]`

---

**Step 3 — Actual Output**

Run or simulate the operation. Write the `## Actual Output` section: status code, response body, relevant headers, observable side effects.

---

**Step 4 — Diff**

Write a `## Diff` section. For every element in Expected Output, state one of:
- `✓ {element} — satisfied`
- A finding entry (element deviates)

Every element must appear. Silent omissions fail C-02 regardless of how many findings are correctly classified.

If no deviations: write `## Diff — Contract satisfied.` and enumerate each element as `✓ satisfied`.

**Finding format:**
```
Finding F-NN
deviation: [expected X; actual Y — state both sides]
severity: breaking | degraded | cosmetic
spec: [clause from Expected Output — must match an entry already cited above]
hypothesis: [causal mechanism, not symptom — one sentence]
```

Severity: `breaking` — consumer cannot function; `degraded` — guarantee violated, silent failure possible; `cosmetic` — no correctness impact.

---

**Step 5 — Summary**

Write a `## Summary` section:
1. Counts: `breaking: N | degraded: N | cosmetic: N | total: N`
2. Verdict: `Contract violated` or `Contract satisfied`
3. For every `breaking` or `degraded` finding: `F-NN: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]`
4. Coverage ratio: `{N} / {total elements in Expected Output} clauses verified, {N} deviations`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Output-Format: Pre-Printed Placeholder Slots

**axis:** output-format
**hypothesis:** R1 V-02 (mandatory findings table) makes empty columns visible at review time. A further improvement is making empty fields visible at write time — before any reviewer sees them. Pre-printing every required field label with a REQUIRED placeholder in the finding entry creates a commitment surface: the author sees the unfilled slot as an incomplete entry, not an optional one. Table format delivers the same signal as a missing column, but a pre-printed entry template creates that signal inside the author's writing flow rather than at the scan-review step. C-03, C-04, and C-05 omissions are most common when authors are moving quickly; a pre-printed slot they must actively replace is harder to skip than a column they must remember to populate.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {describe or paste the input state — inline}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

**Step 1 — Contract Scope**

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture — inline; no external file references
- Spec version and section

Self-contained.

---

**Step 2 — Expected Output** (the contract — write from spec before running anything)

Write the `## Expected Output` section. For each required element, state the element and cite the spec clause. Cover all contract surfaces defined by the spec:
- **Success path** — nominal input → nominal output
- **Error path** — invalid or missing input → error response
- **At least one edge case**

Do not run the operation before this section is complete. Write: `[CONTRACT COMMITTED]` when done.

---

**Step 3 — Actual Output**

Run or simulate the operation. Write the `## Actual Output` section: status code, body, headers, side effects.

---

**Step 4 — Diff and Findings**

For every element in the Expected Output section, write one of:
- `✓ {element identifier} — satisfied`
- `F-NN {element identifier} — deviation (see finding entry below)`

Every element must appear. Missing entries are silent omissions.

If no deviations, write: `No deviations found. Contract satisfied.`

For every deviation, write a finding entry. **Copy this template and fill every slot.** A slot still containing its placeholder label means the finding is incomplete:

```
Finding F-NN
deviation:   [REQUIRED — state the expected value on the left and actual value on the right, separated by →]
severity:    [REQUIRED — replace with exactly one of: breaking | degraded | cosmetic]
spec:        [REQUIRED — copy the clause identifier from the Expected Output section above; do not paraphrase]
hypothesis:  [REQUIRED — state the likely causal mechanism in one sentence; do not restate the deviation]
```

Severity:
- `breaking` — a consumer relying on the contract cannot function correctly
- `degraded` — the operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract; correctness and consumer behavior unaffected

No finding entry is complete while any slot contains its placeholder label. An unfilled `[REQUIRED — ...]` means the field has not been written.

---

**Step 5 — Summary**

Write a `## Summary` section. Copy and fill this template:

```
Severity counts: breaking: [N] | degraded: [N] | cosmetic: [N] | total: [N]
Verdict: [Contract violated | Contract satisfied]
Coverage: [N] / [total expected elements] clauses verified, [N] deviations found

Recommendations (every breaking or degraded finding requires one):
F-NN: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
```

A Summary section that still contains unfilled bracketed slots is incomplete.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Lifecycle-Emphasis: Surface-Colocated Diff Blocks

**axis:** lifecycle-emphasis
**hypothesis:** R1 V-03 names the three-directory layers as phase headings (`10-Input`, `20-Expected`, `30-Actual`). That variation improves C-07 (layers labeled) and C-02 (diff completeness) by making the structure legible. V-03 here goes further: instead of one monolithic diff block after all expected content, each contract surface gets its own mini-lifecycle immediately — expected, then actual, then diff, for that surface alone, before moving to the next surface. The lost-context failure mode for C-02 is most common at the edge-case surface: by the time operators reach the diff section, they've forgotten exactly which fields were defined only in the edge-case block. Colocation eliminates the context gap — the diff sits adjacent to its expected block, making omission impossible to miss without explicitly deciding to omit.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation}
**Connector / Automate context:** {connector or flow context and environment}
**Input fixture:** {input state — inline}
**Spec source:** {spec path and section}

Stock roles: Connectors contract expert + Automate.

---

**Step 1 — Contract Scope**

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture — inline
- Spec version and section

---

**Step 2 — Contract Surfaces (Expected → Actual → Diff, per surface)**

This trace is structured by contract surface. Each surface has three colocated blocks. Complete all three blocks for one surface before moving to the next. Do not write a monolithic diff section.

---

### Surface A: Success Path

**Step 2A — Expected (Success)**

Write `## Expected — Success Path` from the spec alone. List every required element: status code, response body fields, headers, side effects. For each element, cite the spec clause.

Spec-derived only. Do not run the operation before completing this block.

**Step 2B — Actual (Success)**

Write `## Actual — Success Path`. Run or simulate the operation with a valid nominal input. Capture the full response: status code, body, headers, side effects.

**Step 2C — Diff (Success)**

Write `## Diff — Success Path`. For every element in `## Expected — Success Path`, state:
- `✓ {element} — satisfied`, or
- a finding entry

Every element from the Expected block must appear. Silent omissions fail C-02.

Finding format for this surface:
```
Finding F-NN [Success]
deviation: [expected X; actual Y]
severity: breaking | degraded | cosmetic
spec: [clause from Expected — Success Path]
hypothesis: [causal mechanism]
```

---

### Surface B: Error Path

**Step 3A — Expected (Error)**

Write `## Expected — Error Path` from the spec. Cover the invalid-input and missing-input error responses the spec defines. For each element, cite the spec clause. If the spec defines no error contract, write: `Error path: not defined in spec — [confirm by naming which sections were checked]`.

**Step 3B — Actual (Error)**

Write `## Actual — Error Path`. Run or simulate the operation with invalid or missing input. Capture the full response.

**Step 3C — Diff (Error)**

Write `## Diff — Error Path`. For every element in `## Expected — Error Path`, state satisfied or finding. Every element must appear.

Finding format: same as Surface A with `[Error]` suffix on F-NN ID.

---

### Surface C: Edge Case

**Step 4A — Expected (Edge)**

Write `## Expected — Edge Case` from the spec. Cover at least one of: empty collection, null required field, rate-limit trigger, auth expiry, overflow value. Cite the spec clause for each. If genuinely no edge case is defined, write: `Edge case: not defined in spec — [confirm by naming sections checked]`.

**Step 4B — Actual (Edge)**

Write `## Actual — Edge Case`. Run or simulate the edge-case input. Capture the full response.

**Step 4C — Diff (Edge)**

Write `## Diff — Edge Case`. For every element in `## Expected — Edge Case`, state satisfied or finding. Every element must appear.

---

**Step 5 — Summary**

Write a `## Summary` section:
1. Per-surface finding counts
2. Total: `breaking: N | degraded: N | cosmetic: N | total: N`
3. Verdict: `Contract violated` or `Contract satisfied`
4. For every `breaking` or `degraded` finding: `F-NN: [amend-spec | fix-impl | needs-discussion] — [rationale]`
5. Coverage: `{N} / {total expected elements across all surfaces} clauses verified`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Combo: Role-Sequence + Hypothesis-Architecture (Pre-Gate Taxonomy Lock)

**axes:** role-sequence + hypothesis-architecture
**hypothesis:** R2 V-04 (hypothesis-architecture taxonomy) supplies a mechanism taxonomy in the prompt itself — the operator uses it, but it's provided by the prompt, not committed as part of the contract artifact. R1/R2 V-01 (role-sequence commit gate) seals the expected output before Automate begins. Combining both: require the Contract Expert to declare the causal mechanism taxonomy inside Phase 1 before the commit gate. The taxonomy becomes a committed artifact, not a prompt-supplied tool. Automate's hypothesis on every finding must use a category from the pre-committed taxonomy. If no category fits, Automate writes `taxonomy gap: [description]` — which is a finding on the taxonomy, not a license to invent a new category. This binding relationship improves C-05 (mechanism not symptom) by forcing a category selection from an already-committed vocabulary, making causal-sounding symptom restatements obviously wrong — they don't match any taxonomy category.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {describe or paste the input state — inline}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert (Phase 1) + Automate (Phase 2 onward).

---

### ROLE: Connectors Contract Expert

You are the Connectors contract expert. You have not run the operation. You have not observed any output. Your role covers Phase 1. It ends when you write the commit gate.

**Phase 1 — Step 1: Contract Scope**

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture — state inline
- Spec version and section governing this contract

---

**Phase 1 — Step 2: Expected Output**

Write the `## Expected Output` section from the spec alone. For each required element, state the element and cite the spec clause. Cover all contract surfaces:
- **Success path** — nominal input → nominal output per spec
- **Error path** — invalid input → error response per spec
- **At least one edge case** — empty, null, rate-limit, auth expiry

Do not run the operation. Do not infer expected values from implementation knowledge or a previous run. If a surface is not defined in the spec, write: `[surface]: not defined in spec`.

---

**Phase 1 — Step 3: Mechanism Taxonomy Declaration**

Write a `## Mechanism Taxonomy` section. Before the commit gate, declare the causal mechanism categories Automate will use when writing finding hypotheses. This vocabulary is sealed at commit.

Required categories (customize per operation domain):

| Category | Description | Example |
|----------|-------------|---------|
| field-mapping | A field is absent, renamed, or mapped to the wrong target | `connection_id` mapped to `connectionId` |
| type-serialization | A value is serialized in the wrong type or format | enum serialized as integer instead of string |
| auth-propagation | Auth state or token not correctly propagated to downstream call | token expires mid-request; refresh not triggered |
| boundary-handling | Edge-case input (empty, null, overflow) produces wrong output | empty array returns null instead of `[]` |
| contract-omission | Implementation does not implement a spec-required field or behavior | required header absent from success response |
| spec-gap | No spec clause governs the observed behavior; spec is silent on this surface | status code not defined for this error condition |

You may add or remove categories before the commit gate. Categories may not be added after the commit gate.

When both Step 2 and Step 3 are complete, write exactly:

`[CONTRACT COMMITTED — Automate begins here]`

Your role ends here.

---

### ROLE: Automate

You are Automate. The contract and taxonomy are committed above. Your role begins at the commit gate.

Read: `## Contract Scope`, `## Expected Output`, `## Mechanism Taxonomy`.
Do NOT read Phase 1 authoring instructions above the commit gate.
Do NOT revise or supplement the Expected Output or Mechanism Taxonomy sections.

**Phase 2 — Actual Output**

Run or simulate the operation. Write the `## Actual Output` section: status code, body, headers, side effects.

---

**Phase 3 — Diff**

Write a `## Diff` section. For every element in `## Expected Output`, state:
- `✓ {element} — satisfied`, or
- `F-NN {element} — deviation (see findings)`

Every element must appear. Silent omissions fail the artifact.

If no deviations: write `## Diff — Contract satisfied.` and enumerate all elements as `✓ satisfied`.

---

**Phase 4 — Classify Findings**

For every deviation, write a finding entry:

```
Finding F-NN
deviation: [expected X; actual Y — both sides]
severity: breaking | degraded | cosmetic
spec: [clause from Expected Output — must match a cited clause]
hypothesis: [mechanism-category: one sentence naming the cause]
```

The `hypothesis` field must begin with a mechanism category from `## Mechanism Taxonomy`. Example: `field-mapping: the connector serializes \`status\` as an integer but the spec requires the string enum value.`

If no taxonomy category fits, write: `taxonomy gap: [description of mechanism]` — this is a signal that the Mechanism Taxonomy is incomplete, not a license to write a symptom restatement.

DO NOT write a hypothesis that begins "The output did not match" or restates the deviation. A valid hypothesis names a category and a cause.

Severity:
- `breaking` — consumer relying on contract cannot function
- `degraded` — guarantee violated; silent failure or data loss possible
- `cosmetic` — no correctness or consumer-behavior impact

---

**Phase 5 — Summary**

Write a `## Summary` section:
1. Counts: `breaking: N | degraded: N | cosmetic: N | total: N`
2. Verdict: `Contract violated` or `Contract satisfied`
3. For every `breaking` or `degraded` finding: `F-NN: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]`
4. Coverage: `{N} / {total elements in Expected Output} clauses verified, {N} deviations`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — All Axes Integrated: Full-Strength Round 4 Synthesis

**axes:** phrasing-register + output-format + lifecycle-emphasis + role-sequence + hypothesis-architecture + inertia-framing
**hypothesis:** V-01 through V-04 each target a different failure mode via a different mechanism. V-01 (three named C-01 failure forms) operates at the language level, blocking specific prohibited derivation paths. V-02 (pre-printed placeholder slots) operates at the write-time visual level, making omission visible before review. V-03 (surface-colocated diffs) operates at the document structure level, eliminating the context-gap omission failure. V-04 (pre-gate taxonomy lock) operates at the commitment level, binding Automate's hypothesis vocabulary before execution. These four mechanisms are phase-independent: V-01 targets Phase 1 derivation; V-02 targets Phase 4 writing; V-03 targets Phase 4 structure; V-04 targets Phase 1-to-4 vocabulary continuity. Inertia framing adds motivational context at each phase. Combined, they should yield the highest composite score of any v16 variation because they compound without interference.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {describe or paste the input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert (Phase 1) + Automate (Phase 2 onward).

---

### Why this artifact is worth the discipline

The status quo: run the operation, look at the output, decide it seems right. The status quo produces no committed expected, no structured diff, and no classification of what failed and why. When behavior regresses, there is no baseline. When the question is "spec bug or implementation bug?" — there is no artifact to argue from.

Each phase below produces an artifact the status quo cannot produce. Leave any phase incomplete and the artifact partially collapses back to the status quo.

---

### ROLE: Connectors Contract Expert

You are the Connectors contract expert. You have not run the operation. You have not seen any runtime output. Your role covers Phase 1. It ends at the commit gate.

---

**Phase 1 — Build the contract** *(status quo: no contract exists before running)*

**Step 1 — Contract Scope** *(status quo: scope is implicit in someone's memory)*

Write a `## Contract Scope` section:
- Operation name and HTTP method
- Connector or Automate context and environment
- Input fixture — state inline; do not reference external files
- Spec version and section governing this contract

Self-contained. A reader must understand scope without opening another file.

---

**Step 2 — Expected Output** *(status quo: run first, observe, call it expected)*

Write the `## Expected Output` section from the spec alone.

The status quo runs first. That makes the implementation the de facto contract. Writing expected from spec before running creates a contract that exists independently of current behavior.

**Three derivation errors that produce a compliant-looking but invalid Expected section — avoid all three:**

- **Copy-from-prior:** Do not reuse a previous trace's Expected section. Derive from the current spec version. Prior traces may predate spec amendments.
- **Implementation-vocabulary contamination:** Write expected values in spec vocabulary, not in the implementation's internal field names. An expected section that mirrors the implementation's output is not a check — it's a copy.
- **Spec-gap laundering:** Do not write `not specified in spec` without confirming. If the spec defines behavior in a non-obvious section, find it. Laundering a hard-to-find requirement as a gap leaves the contract incomplete without a visible failure marker.

For each required element, state the element and cite the spec clause. Cover all three contract surfaces:
- **Success path** — nominal input → nominal output per spec
- **Error path** — invalid or missing input → error response per spec (if genuinely absent: "error contract: not defined in spec — confirmed by searching [sections]")
- **At least one edge case** — empty, null, rate-limit, auth expiry

---

**Step 3 — Mechanism Taxonomy** *(status quo: failure causes are never classified)*

Write a `## Mechanism Taxonomy` section before the commit gate. Declare the causal categories Automate will use in finding hypotheses.

| Category | Description |
|----------|-------------|
| field-mapping | Field absent, renamed, or mapped to wrong target |
| type-serialization | Value serialized in wrong type or format |
| auth-propagation | Auth state or token not correctly forwarded |
| boundary-handling | Edge-case input produces wrong output |
| contract-omission | Implementation does not implement a spec-required behavior |
| spec-gap | No spec clause governs the observed behavior |

Add or remove categories as needed before the gate. This vocabulary is sealed at commit.

When Steps 1–3 are complete, write:

`[CONTRACT COMMITTED — Automate begins here]`

Your role ends here.

---

### ROLE: Automate

You are Automate. The contract and mechanism taxonomy are committed above. Your role begins at the commit gate.

Read: `## Contract Scope`, `## Expected Output`, `## Mechanism Taxonomy`.
Do NOT read Phase 1 authoring instructions.
Do NOT revise or supplement Phase 1 content. If you believe a Phase 1 entry is wrong, that is a finding — not a license to edit.

---

**Phase 2 — Capture actual output** *(status quo: this is where observation ends)*

Run or simulate the operation against the input fixture. Write the `## Actual Output` section: status code, body, headers, observable side effects.

The status quo stops here. There is no Phase 3.

---

**Phase 3 — Diff by surface** *(status quo: "it doesn't look right" with no structure)*

This diff is organized by contract surface. For each surface, write the diff block immediately after this section — do not consolidate into one section at the end.

**Surface: Success Path — Diff**

For every element in `## Expected Output — Success Path`, state:
- `✓ {element} — satisfied`
- `F-NN [Success] {element} — deviation (see finding below)`

Every element must appear. Silent omissions fail the artifact regardless of finding quality.

**Surface: Error Path — Diff**

For every element in `## Expected Output — Error Path`, state satisfied or deviation. Every element must appear.

**Surface: Edge Case — Diff**

For every element in `## Expected Output — Edge Case`, state satisfied or deviation. Every element must appear.

If a full surface has no deviations, write: `[Surface] — Contract satisfied. No deviations.` and enumerate each element as `✓ satisfied`.

---

**Phase 4 — Classify findings** *(status quo: "file a bug" with no spec anchor)*

For each deviation, write a finding entry. **Copy this template. Replace every [REQUIRED] slot.** An unfilled slot means the finding is incomplete:

```
Finding F-NN
deviation:   [REQUIRED — expected value → actual value; both sides explicit]
severity:    [REQUIRED — exactly one of: breaking | degraded | cosmetic]
spec:        [REQUIRED — clause identifier from Expected Output; no paraphrase]
hypothesis:  [REQUIRED — taxonomy-category: one sentence naming the mechanism]
```

The `hypothesis` field must begin with a category from `## Mechanism Taxonomy` followed by a colon and a one-sentence cause description. Example: `contract-omission: the success response omits the required \`correlation_id\` field that spec §4.3 mandates for all async operations.`

If no taxonomy category fits: `taxonomy gap: [description]` — signals that the taxonomy needs a new category; does not permit a symptom restatement.

Severity:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract; no correctness or consumer-behavior impact

---

**Phase 5 — Decide** *(status quo: this decision cannot be made without a committed contract)*

Write a `## Summary` section. Copy and fill:

```
Severity counts: breaking: [N] | degraded: [N] | cosmetic: [N] | total: [N]
Verdict: [Contract violated | Contract satisfied]

Recommendations (required for every breaking or degraded finding):
F-NN: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]

Coverage: [N] / [total expected elements] clauses verified, [N] deviations found
```

This is the decision the status quo cannot make. Without a committed expected contract, you cannot determine whether the implementation is wrong or the spec is wrong — you can only observe that they differ. The recommendation line is the payoff that justifies the discipline.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## Combination Candidates for Round 5

| Priority | Axis Pair | Primary Targets | Rationale |
|----------|-----------|-----------------|-----------|
| 1 | V-03 + V-04 (surface-colocated diffs + pre-gate taxonomy) | C-02, C-05, C-07 | Surface-colocated diffs enforce per-surface diff completeness; pre-gate taxonomy seals hypothesis vocabulary per surface — each surface's findings use only the taxonomy declared before that surface was committed |
| 2 | V-01 + V-02 (three named failure forms + pre-printed slots) | C-01, C-03, C-04, C-05 | Named failure forms block C-01 at derivation time; pre-printed slots block C-03/C-04/C-05 at writing time — two gates at two different points in the artifact lifecycle |
| 3 | V-03 + V-01 + V-02 (surface lifecycle + named prohibitions + slots) | C-01, C-02, C-03, C-04, C-05 | Triple axis with per-surface colocation as the structural backbone; named prohibitions guard Expected derivation; slots guard finding completeness within each surface |

## Evaluation Order Guidance

| Priority | Variation | Rationale |
|----------|-----------|-----------|
| 1 | V-04 (role-sequence + hypothesis-architecture: pre-gate taxonomy lock) | Tests whether taxonomy commitment improves C-05 beyond R2 V-04's prompt-supplied taxonomy. If C-05 pass rate is the same, the lock is overhead; if higher, binding matters |
| 2 | V-02 (output-format: pre-printed slots) | Tests whether write-time visual commitment cue outperforms R1 V-02's table format. If similar C-03/C-04 pass rate, slots add no value over columns; if higher, write-time cue matters |
| 3 | V-01 (phrasing-register: three named failure forms) | Tests whether named failure-form prohibitions outperform R1 V-04's generic DO NOT gates for C-01. Compare C-01 pass rate to R2 V-01 |
| 4 | V-03 (lifecycle-emphasis: surface-colocated diffs) | Tests whether colocation improves C-02 over R2 V-03's per-surface table approach. R2 V-03 used tables; V-03 uses prose diffs. Compare C-02 pass rate |
| 5 | V-05 (all axes integrated) | Evaluate after individual axes are scored. If V-04 and V-02 together already achieve golden, V-05 tests whether adding V-01 and V-03 compounds or degrades |
