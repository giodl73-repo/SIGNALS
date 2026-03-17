# trace-contract Variate — Round 5 (rubric v5)

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v5 (C-01 through C-19; essential C-01-C-05; golden threshold: all essential + composite >= 80)
**Round:** R5 — 3 single-axis + 2 combinations

---

## Round 5 Variation Map

| Variation | Axis | Primary Target | Hypothesis |
|-----------|------|----------------|------------|
| V-01 | lifecycle-emphasis (preamble-first token contract) | C-19, C-18, C-13 | Isolating the full token behavioral contract as a named Behavioral Contract section before Phase 1 ensures the model reads all cross-phase rules before any phase instruction — preamble placement is the single structural change that converts C-18 satisfaction into C-19 satisfaction |
| V-02 | output-format (severity-stratified templates) | C-16, C-15, C-11 | Three distinct templates — one per severity tier — remove conditional field logic entirely; every field within a given tier's template is unconditionally required, making a missing field visually self-announcing at write time without any "required if breaking" hedge |
| V-03 | phrasing-register (integration-first, collaborative) | C-06, C-14 | Introducing the Automate/Connectors integration lens in a named framing section before Phase 1 (conversational register) primes integration-impact evaluation for every finding, converting at-least-one callout (C-06) into per-finding structural inclusion (C-14) |
| V-04 | lifecycle + output-format (preamble + stratified + rationale) | C-19, C-16, C-17 | Preamble-first governs sequencing before any phase begins; severity-stratified templates govern write-time field completeness; rationale-anchored recommended-action in the breaking template binds resolution direction to root cause — three mechanisms at three lifecycle points without interference |
| V-05 | all five axes (preamble + stratified + integration + pattern + inertia) | C-01 through C-19 full coverage | V-01 through V-04 each target a different failure mode at a different lifecycle point; combining all five axes plus pattern detection and inertia framing should yield the highest composite score of any v5 variation because the mechanisms are phase-independent and additive |

---

## V-01 — Lifecycle: Preamble-First Behavioral Protocol

**axis:** lifecycle-emphasis
**hypothesis:** R4 V-05 embeds the token contract inline within Phase 1 instructions — after the Phase 1 heading has already been read. C-18 passes because the contract is complete; C-19 fails because the contract appears inside a phase block rather than before Phase 1 begins. The fix is structural, not content: move the entire token behavioral contract into a named Behavioral Contract section that appears before any Phase 1 or ROLE: heading. When the model encounters the preamble section first, all cross-phase behavioral rules — token placement, non-substitutability, verification mechanism — are in context before any phase instruction begins. This is the minimum change that converts C-18 compliance into C-19 compliance.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {describe or paste the input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert (Phase 1) + Automate (Phase 2 onward).

---

## Behavioral Contract

Read this section before Phase 1. It governs the sequencing invariant for this entire artifact. Phase instructions below do not override it.

**Gate token:** `[EXPECTED SEALED]`

**Placement rule:** The token appears on its own line, immediately after the last entry in the Expected Output section, before any Phase 2 content. No text appears between the last Expected Output entry and the token line. No text appears between the token line and the Phase 2 heading.

**Non-substitutability constraint:** The token `[EXPECTED SEALED]` is the only valid gate marker. The following do NOT satisfy the sequencing invariant:
- `[CONTRACT COMMITTED]`, `[EXPECTED COMPLETE]`, `[PHASE 1 DONE]`
- Any prose: "Expected output is now complete", "Proceeding to actual output", "Contract sealed"
- Any variation in capitalization, bracket style, or wording

Prose equivalents are not machine-parseable. Only the exact string `[EXPECTED SEALED]` enables automated verification.

**Verification mechanism:** Automated tooling scans the artifact for the exact string `[EXPECTED SEALED]`. Absent token — artifact fails sequencing check. Token present after Phase 2 content — artifact fails sequencing check. The token's document position is the machine-verifiable evidence that Phase 1 completed before Phase 2 began.

---

### ROLE: Connectors Contract Expert

You are the Connectors contract expert. Your role covers Phase 1 only. You write the expected output — the contract — from the spec alone. You have not run the operation and have not observed any output. Your role ends at the gate token.

**Phase 1 — Step 1: Contract Scope**

Write a `## Contract Scope` section:
- Operation name and HTTP method (or equivalent)
- Connector or Automate context and environment
- Input fixture — state inline; do not reference external files
- Spec version and section governing this operation's output contract

Self-contained. A reader must determine scope without opening another file.

---

**Phase 1 — Step 2: Expected Output**

Write the `## Expected Output` section from the spec alone. This is the contract. For each required element, state the element and cite the spec clause. Cover all three contract surfaces:

- **Success path** — nominal input to nominal output per spec
- **Error path** — invalid or missing input to error response per spec. If the spec genuinely defines no error contract, write: `Error path: not defined in spec — confirmed by searching [name the sections checked]`
- **At least one edge case** — empty collection, null required field, rate-limit trigger, or auth expiry

Do not run the operation before this section is complete.

**When the Expected Output section is complete, write exactly — on its own line:**

`[EXPECTED SEALED]`

See the Behavioral Contract above for placement and non-substitutability rules. Your role ends here.

---

### ROLE: Automate

You are Automate. The contract is sealed above. Your role begins after `[EXPECTED SEALED]`.

Read: `## Contract Scope`, `## Expected Output`.
Do NOT read the Phase 1 authoring instructions above the gate token.
Do NOT revise the Expected Output section. Any belief that an Expected entry is wrong is a finding — not a license to edit.

---

**Phase 2 — Actual Output**

Run or simulate the operation against the input fixture. Write the `## Actual Output` section: status code, full response body, relevant headers, observable side effects.

---

**Phase 3 — Diff**

Write a `## Diff` section. For every element in `## Expected Output`, write one of:
- `check {element} — satisfied`
- `F-NN {element} — deviation (see finding below)`

Every element must appear. An element present in Expected but absent from Diff is a silent omission — the artifact fails C-02 regardless of finding quality.

If no deviations: write `## Diff — Contract satisfied.` and enumerate each element as `check satisfied`.

---

**Phase 4 — Findings**

For each deviation, write a finding entry with all five fields:

```
Finding F-NN
deviation:        [expected value or behavior -> actual value or behavior; both sides explicit]
severity:         [exactly one of: breaking | degraded | cosmetic]
spec:             [clause identifier from Expected Output — must match a clause already cited; no paraphrase]
hypothesis:       [one sentence naming the causal mechanism — not a symptom restatement]
connector-impact: [integration-level impact — e.g., "breaks Automate connector field mappings for {field}"; or "no connector-level impact — cosmetic only"]
```

Severity:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract; no correctness or consumer-behavior impact

For every `breaking` finding, add a sixth field:

```
recommended-action: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale: which side of the contract is wrong and why]
```

---

**Phase 5 — Summary**

Write a `## Summary` section:
1. Severity counts: `breaking: N | degraded: N | cosmetic: N | total: N`
2. Verdict: `Contract violated` or `Contract satisfied`
3. For every `breaking` or `degraded` finding: `F-NN: [amend-spec | fix-impl | needs-discussion] — [rationale]`
4. Coverage ratio: `{N} / {total elements in Expected Output} clauses verified, {N} deviations`
5. **Pattern note:** If two or more findings share a root cause mechanism, write: `Pattern: F-NN and F-MM share [mechanism] — single fix resolves both.`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Output Format: Severity-Stratified Templates

**axis:** output-format
**hypothesis:** R4 V-02 uses pre-printed placeholder slots in a single unified finding template with a `recommended-action` field marked "required if breaking." A unified template with a conditional field cannot satisfy C-16 because the template architecture itself contains conditional logic. The fix is architectural: three templates, one per severity tier, each with only the fields unconditionally appropriate to that tier. Breaking findings use a six-field template; degraded use a five-field template; cosmetic use a four-field template. There is no conditional language anywhere — every field in every template is always required when that template is used. An author filling the breaking template cannot complete it without filling `recommended-action`, because there is no conditional; they would have to leave a visually empty slot. C-15 (amendment enforcement by template structure) and C-11 (structural field enforcement) follow automatically from this architecture.

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

Self-contained.

---

**Step 2 — Expected Output** *(the contract — write from spec before running)*

Write the `## Expected Output` section from the spec alone. For each required element, state the element and cite the spec clause. Cover all contract surfaces:
- **Success path** — nominal input to nominal output per spec
- **Error path** — invalid or missing input to error response per spec
- **At least one edge case** — empty, null, rate-limit, auth expiry

Do not run the operation before completing this section. When done, write: `[EXPECTED SEALED]`

---

**Step 3 — Actual Output**

Run or simulate the operation. Write the `## Actual Output` section: status code, body, headers, side effects.

---

**Step 4 — Diff**

Write a `## Diff` section. For every element in Expected Output, state:
- `check {element} — satisfied`, or
- `F-NN {element} — deviation (see finding below)`

Every element must appear. If no deviations: write `## Diff — Contract satisfied.` and enumerate all elements as `check satisfied`.

---

**Step 5 — Findings by Severity Tier**

Write each finding using the template that matches its severity. Do not mix templates. Every labeled slot in the chosen template is required — there are no optional fields within a template.

---

**Breaking Finding Template** *(use only when severity = breaking)*

```
Breaking Finding F-NN
deviation:          [expected value or behavior -> actual value or behavior; both sides explicit]
severity:           breaking
spec:               [clause identifier from Expected Output — must match a cited clause; no paraphrase]
hypothesis:         [one sentence naming the causal mechanism — not a symptom restatement]
connector-impact:   [integration-level impact — e.g., "Automate connector field mapping for {field} breaks at runtime"]
recommended-action: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale: which side of the contract is wrong and why]
```

All six slots are required. A breaking finding with any slot unfilled is incomplete.

---

**Degraded Finding Template** *(use only when severity = degraded)*

```
Degraded Finding F-NN
deviation:        [expected value or behavior -> actual value or behavior; both sides explicit]
severity:         degraded
spec:             [clause identifier from Expected Output — must match a cited clause; no paraphrase]
hypothesis:       [one sentence naming the causal mechanism — not a symptom restatement]
connector-impact: [integration-level impact — e.g., "Automate flows may silently receive incorrect data for {field}"]
```

All five slots are required. A degraded finding with any slot unfilled is incomplete.

---

**Cosmetic Finding Template** *(use only when severity = cosmetic)*

```
Cosmetic Finding F-NN
deviation:  [expected value or behavior -> actual value or behavior; both sides explicit]
severity:   cosmetic
spec:       [clause identifier from Expected Output — must match a cited clause; no paraphrase]
hypothesis: [one sentence naming the causal mechanism — not a symptom restatement]
```

All four slots are required. A cosmetic finding with any slot unfilled is incomplete.

---

Severity definitions (use to select the right template):
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract; no correctness or consumer-behavior impact

---

**Step 6 — Summary**

Write a `## Summary` section:

```
Severity counts: breaking: [N] | degraded: [N] | cosmetic: [N] | total: [N]
Verdict: [Contract violated | Contract satisfied]
Coverage: [N] / [total elements in Expected Output] clauses verified, [N] deviations

Recommendations (required for every breaking and degraded finding):
F-NN: [amend-spec | fix-impl | needs-discussion] — [rationale]
```

A Summary section with any unfilled bracket placeholder is incomplete.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Phrasing Register: Integration-First, Collaborative Frame

**axis:** phrasing-register
**hypothesis:** R1 through R4 variations use a formal imperative register throughout: "Write a section containing...", "DO NOT run the operation...", "Every element must appear." This register delivers rules efficiently but does not foreground the integration perspective that C-06 and C-14 require. A collaborative register — naming the reader as a participant in a shared goal, describing what each phase achieves for integration consumers rather than mandating compliance — establishes the Automate/Connectors lens at the preamble level before any phase instruction is read. When the integration frame is set before Phase 1, per-finding integration-impact assessment becomes natural rather than a bolted-on field requirement. The hypothesis is that framing-before-instruction converts C-06 at-least-one coverage into C-14 per-finding structural inclusion without requiring a structural template change — the reader already has the lens by the time they write the first finding.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {describe or paste the input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

## Integration Lens

Before Phase 1 begins, orient to your audience. The primary consumers of this contract trace are Automate flow builders and Connectors integration authors. They do not run operations directly — they build on the output contract, wiring field mappings, handling error codes, setting retry policies. What looks cosmetic from an API perspective may be breaking from theirs: a renamed field silently breaks a connector mapping; a missing error code leaves a flow with no retry path; a type mismatch causes silent data corruption downstream.

Throughout this trace, keep the integration lens active. For every finding, ask: if someone wired up a connector or Automate flow to the expected output, and the actual output is what arrived instead, what happens to their integration? Would it break, silently misbehave, or work fine?

---

**Phase 1 — Name the contract**

Begin with a `## Contract Scope` section. The goal is a self-contained record that an integration author can read without opening another file. Include:
- The operation name and HTTP method (or equivalent)
- The Connector or Automate context: which connector, which flow, which environment
- The input fixture: describe or paste the state being used; no external file references
- The spec version and section governing the output contract for this operation

Precise scope produces precise findings. Vague scope produces findings that no one can act on.

---

**Phase 2 — Write what you expect before you run**

Write the `## Expected Output` section from the spec alone. This section is the contract — what an integration author would reasonably wire their connector or flow to, based on the spec.

For each required element, write the element and cite the spec clause. Think in terms of what an Automate flow builder needs to see:
- Field names and types they will map
- Status codes that will trigger retry or error branches
- Headers that influence caching, routing, or authentication state
- Edge-case behaviors that could cause a flow to stall, loop, or silently drop data

Cover all three surfaces the spec defines:
- **Success path** — what the spec says comes back on a valid, nominal call
- **Error path** — what the spec says comes back on invalid or missing input. If the spec genuinely does not define this: `Error path: not defined in spec — confirmed by checking [name the sections]`
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

Do not run the operation before this section is complete. When done, write: `[EXPECTED SEALED]`

---

**Phase 3 — Capture what actually arrived**

Run or simulate the operation against the input fixture. Write the `## Actual Output` section — the full response: status code, body, all headers that carry integration-relevant meaning, observable side effects.

---

**Phase 4 — Find the gaps**

Write a `## Diff` section. For every element in Expected Output, state whether actual matches or deviates:
- `check {element} — satisfied` — the contract was honored for this element
- `F-NN {element} — deviation (see finding below)` — there is a gap

Cover every element. An element you listed in Expected but did not check in Diff is a silent gap.

If nothing deviates: write `## Diff — Contract satisfied.` and list every element as `check satisfied`.

---

**Phase 5 — Classify each gap**

For each deviation, write a finding entry. The goal is a record that an integration author can read and know exactly what happened, why, and what it means for their work:

```
Finding F-NN
deviation:        [expected value or behavior -> actual value or behavior — be specific on both sides]
severity:         [breaking | degraded | cosmetic]
spec:             [the spec clause from Expected Output this deviates from — copy the identifier, do not paraphrase]
hypothesis:       [why this probably happened — name a mechanism, not just "it didn't match"]
connector-impact: [what this means for an integration author — e.g., "any connector mapping {field} by name will break at runtime"; "Automate error-path branches on this status code will not trigger"; "no integration impact — cosmetic difference only"]
```

Severity from the integration perspective:
- `breaking` — an integration author relying on this contract cannot build a working connector or flow
- `degraded` — the integration will appear to work but will silently mishandle some inputs or produce incorrect outputs
- `cosmetic` — the deviation does not affect how integrations behave in practice

For every `breaking` finding, add a recommendation:

```
recommended-action: [amend-spec | fix-impl | needs-discussion] — [one sentence: which side is wrong and why]
```

---

**Phase 6 — Summarize and decide**

Write a `## Summary` section:
1. Counts: `breaking: N | degraded: N | cosmetic: N | total: N`
2. Verdict: `Contract violated` or `Contract satisfied`
3. For every `breaking` or `degraded` finding: `F-NN: [amend-spec | fix-impl | needs-discussion] — [rationale]`
4. Coverage: `{N} / {total elements in Expected Output} clauses verified, {N} deviations`
5. If two or more findings share a root cause: `Pattern: F-NN and F-MM share [mechanism] — single fix resolves both.`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Combo: Preamble + Severity-Stratified + Rationale-Anchored

**axes:** lifecycle-emphasis + output-format
**hypothesis:** V-01 (preamble-first) and V-02 (severity-stratified templates) operate at different lifecycle points without overlap: V-01 governs pre-Phase-1 behavioral setup (C-19); V-02 governs Phase 4 finding structure (C-16). Adding C-17 rationale-anchored resolution completes the breaking-finding contract: V-02's breaking template already satisfies C-15 (amendment enforcement by structure); extending the recommended-action slot to require both a vocabulary choice and a rationale sentence elevates it to C-17. The three mechanisms compound: preamble ensures all behavioral rules are read before Phase 1; stratified templates ensure every field is unconditionally required within its tier; rationale anchoring ensures resolution direction is grounded in root cause. None of the three mechanisms interfere with the others.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {describe or paste the input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert (Phase 1) + Automate (Phase 2 onward).

---

## Behavioral Contract

Read this section before Phase 1. It governs the sequencing invariant for this artifact and all cross-phase behavioral rules. Phase instructions below do not override it.

**Gate token:** `[EXPECTED SEALED]`

**Placement rule:** The token appears on its own line, immediately after the last entry in the Expected Output section, before any Phase 2 content. No text appears between the last Expected Output entry and the token line. No text appears between the token line and the Phase 2 heading.

**Non-substitutability constraint:** Only the exact string `[EXPECTED SEALED]` is a valid gate marker. These do NOT qualify:
- `[CONTRACT COMMITTED]`, `[EXPECTED COMPLETE]`, `[PHASE 1 SEALED]`, any variant spelling
- Any prose statement that expected was written before running
- Any markdown-formatted version of the token (bold, code, italic) — the token must be bare text on its own line

**Verification mechanism:** Automated tooling scans for the exact string `[EXPECTED SEALED]`. Absent — artifact fails sequencing check. Present after Phase 2 content — artifact fails sequencing check. The token's document position is the machine-verifiable evidence of Phase 1 completion before Phase 2 began.

---

### ROLE: Connectors Contract Expert

You are the Connectors contract expert. Your role covers Phase 1. You write the expected output from the spec alone. You have not run the operation and have not observed any output. Your role ends at the gate token.

**Phase 1 — Step 1: Contract Scope**

Write a `## Contract Scope` section:
- Operation name and HTTP method (or equivalent)
- Connector or Automate context and environment
- Input fixture — state inline; do not reference external files
- Spec version and section governing this operation's output contract

Self-contained. A reader must determine scope without opening another file.

---

**Phase 1 — Step 2: Expected Output**

Write the `## Expected Output` section from the spec alone. For each required element, state the element and cite the spec clause. Cover all three contract surfaces:

- **Success path** — nominal input to nominal output per spec
- **Error path** — invalid or missing input to error response per spec. If genuinely not in spec: `Error path: not defined in spec — confirmed by searching [sections checked]`
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

Do not run the operation before this section is complete.

**When the Expected Output section is complete, write on its own line:**

`[EXPECTED SEALED]`

Your role ends here.

---

### ROLE: Automate

You are Automate. The contract is sealed above. Your role begins after `[EXPECTED SEALED]`.

Read: `## Contract Scope`, `## Expected Output`.
Do NOT read Phase 1 authoring instructions above the gate token.
Do NOT revise the Expected Output section. Any belief that an Expected entry is wrong is a finding.

---

**Phase 2 — Actual Output**

Run or simulate the operation. Write the `## Actual Output` section: status code, body, headers, side effects.

---

**Phase 3 — Diff**

Write a `## Diff` section. For every element in `## Expected Output`, write:
- `check {element} — satisfied`, or
- `F-NN {element} — deviation (see finding below)`

Every element must appear. If no deviations: write `## Diff — Contract satisfied.` and enumerate each element as `check satisfied`.

---

**Phase 4 — Findings by Severity Tier**

Write each finding using the template for its severity tier. Every labeled slot within the chosen template is unconditionally required.

---

**Breaking Finding Template** *(severity = breaking: consumer cannot function correctly)*

```
Breaking Finding F-NN
deviation:          [expected -> actual; both sides explicit]
severity:           breaking
spec:               [clause from Expected Output — must match a cited clause; no paraphrase]
hypothesis:         [one sentence: causal mechanism, not symptom restatement]
connector-impact:   [integration-level impact — e.g., "Automate connector mapping for {field} fails at runtime"]
recommended-action: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale identifying which side of the contract is wrong and why, grounded in the hypothesis above]
```

All six slots are unconditionally required. The `recommended-action` slot must contain both a vocabulary choice and a rationale sentence. A vocabulary choice without a rationale sentence does not complete this slot.

---

**Degraded Finding Template** *(severity = degraded: operation runs but guarantee violated)*

```
Degraded Finding F-NN
deviation:        [expected -> actual; both sides explicit]
severity:         degraded
spec:             [clause from Expected Output — must match a cited clause; no paraphrase]
hypothesis:       [one sentence: causal mechanism, not symptom restatement]
connector-impact: [integration-level impact — e.g., "Automate flows may silently receive incorrect data for {field}"]
```

All five slots are unconditionally required.

---

**Cosmetic Finding Template** *(severity = cosmetic: no correctness or consumer-behavior impact)*

```
Cosmetic Finding F-NN
deviation:  [expected -> actual; both sides explicit]
severity:   cosmetic
spec:       [clause from Expected Output — must match a cited clause; no paraphrase]
hypothesis: [one sentence: causal mechanism, not symptom restatement]
```

All four slots are unconditionally required.

---

**Phase 5 — Summary**

Write a `## Summary` section:
1. Severity counts: `breaking: N | degraded: N | cosmetic: N | total: N`
2. Verdict: `Contract violated` or `Contract satisfied`
3. For every `breaking` or `degraded` finding: `F-NN: [amend-spec | fix-impl | needs-discussion] — [rationale]`
4. Coverage: `{N} / {total elements in Expected Output} clauses verified, {N} deviations`
5. **Pattern note:** If two or more findings share a root cause: `Pattern: F-NN and F-MM — [mechanism] — single fix resolves both.`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — All Axes: Full-Strength Round 5 Synthesis

**axes:** lifecycle-emphasis + output-format + phrasing-register + role-sequence + inertia-framing
**hypothesis:** V-01 targets C-19 at the pre-Phase-1 sequencing level. V-02 targets C-16 at the finding-template architecture level. V-03 targets C-06/C-14 at the framing-register level. V-04 targets C-17 at the resolution-rationale level. Each mechanism operates at a different lifecycle point: pre-execution behavioral rules, finding write-time structure, reader frame establishment, resolution vocabulary. Inertia framing added at each phase boundary names the status-quo alternative, converting each phase from a compliance obligation into a legible improvement. Pattern detection and per-finding connector-impact complete the aspirational tier. These mechanisms are additive because they are phase-independent: preamble governs setup, integration-first framing governs finding perspective, stratified templates govern finding structure, rationale anchoring governs resolution depth, inertia framing governs motivation. Combining all five should produce the highest composite score of any R5 variation.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {describe or paste the input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert (Phase 1) + Automate (Phase 2 onward).

---

## Behavioral Contract

Read this section before Phase 1. It governs sequencing and cross-phase behavioral rules for this artifact. Phase instructions below cannot override it.

**Gate token:** `[EXPECTED SEALED]`

**Placement rule:** The token appears on its own line, immediately after the last entry in `## Expected Output`, before any Phase 2 content. No text between the last Expected Output entry and the token. No text between the token and the Phase 2 heading.

**Non-substitutability constraint:** Only the exact string `[EXPECTED SEALED]` is the parseable gate marker. These do NOT qualify:
- Any bracket variant: `[CONTRACT COMMITTED]`, `[EXPECTED COMPLETE]`, `[PHASE 1 DONE]`
- Any prose: "Expected output is now sealed", "Moving to Phase 2", "Contract locked"
- Any markdown-formatted version of the token (bold, code, italic)

**Verification mechanism:** Automated tooling scans for the exact string `[EXPECTED SEALED]`. Token absent — sequencing check fails. Token present after Phase 2 content — sequencing check fails. The token's document position is the machine-verifiable evidence that Phase 1 completed before Phase 2 began.

---

## Integration Lens

Before Phase 1 begins: orient to your audience. The primary consumers of this contract trace are Automate flow builders and Connectors integration authors. They build on the output contract — wiring field mappings, error branches, retry policies. A field rename they did not expect breaks a mapping silently. A missing error code leaves their flow with no retry path. Throughout this trace, for every finding, ask: what does this mean for someone who built a connector or flow against the expected output?

---

### ROLE: Connectors Contract Expert

You are the Connectors contract expert. Your role covers Phase 1. You write the expected output from the spec alone. You have not run the operation. Your role ends at the gate token.

---

**Phase 1 — Build the contract** *(status quo: no contract exists before running — this phase creates one)*

**Step 1 — Contract Scope** *(status quo: scope is in someone's memory, not in an artifact)*

Write a `## Contract Scope` section:
- Operation name and HTTP method (or equivalent)
- Connector or Automate context and environment
- Input fixture — state inline; do not reference external files
- Spec version and section governing this operation's output contract

Self-contained. The status quo leaves scope implicit. This section makes it referenceable.

---

**Step 2 — Expected Output** *(status quo: run first, observe, call it expected — the implementation becomes the de facto contract)*

Write the `## Expected Output` section from the spec alone. Writing expected before running creates a contract that exists independently of what the implementation currently produces.

For each required element, state the element and cite the spec clause. Cover all three contract surfaces:

- **Success path** — nominal input to nominal output per spec
- **Error path** — invalid or missing input to error response per spec. If genuinely not in spec: `Error path: not defined in spec — confirmed by searching [sections checked]`
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

Do not run the operation before this section is complete.

**When the Expected Output section is complete, write on its own line:**

`[EXPECTED SEALED]`

See the Behavioral Contract above. Your role ends here.

---

### ROLE: Automate

You are Automate. The contract is sealed above. Your role begins after `[EXPECTED SEALED]`.

Read: `## Contract Scope`, `## Expected Output`.
Do NOT read Phase 1 authoring instructions above the gate token.
Do NOT revise the Expected Output section. Any belief that an Expected entry is wrong is a finding — not a license to edit.

---

**Phase 2 — Capture actual output** *(status quo: this is where observation ends — no diff, no classification)*

Run or simulate the operation against the input fixture. Write the `## Actual Output` section: status code, full response body, relevant headers, observable side effects.

The status quo stops here. Phases 3 through 5 are what the status quo cannot do.

---

**Phase 3 — Diff** *(status quo: no diff because no expected exists)*

Write a `## Diff` section. For every element in `## Expected Output`, write:
- `check {element} — satisfied`
- `F-NN {element} — deviation (see finding below)`

Every element must appear. An element present in Expected but absent from Diff is a silent gap — the trace partially collapses back to status quo for that element.

If no deviations: write `## Diff — Contract satisfied.` and enumerate each element as `check satisfied`.

---

**Phase 4 — Classify findings** *(status quo: "file a bug" with no spec anchor and no severity)*

Write each finding using the template for its severity tier. Remember the integration lens: connector-impact is not overhead — it is the answer to "who is affected and how."

---

**Breaking Finding Template** *(consumer cannot function correctly)*

```
Breaking Finding F-NN
deviation:          [expected -> actual; both sides explicit]
severity:           breaking
spec:               [clause from Expected Output — must match a cited clause; no paraphrase]
hypothesis:         [one sentence: causal mechanism, not symptom restatement]
connector-impact:   [integration-level impact — how this breaks a connector or Automate flow wired to the expected output]
recommended-action: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale: which side of the contract is wrong and why, grounded in the hypothesis above]
```

All six slots are required. `recommended-action` requires both a vocabulary choice and a rationale sentence grounded in the root cause. This is the step the status quo cannot take: without a committed expected contract, you cannot determine whether the spec or the implementation is wrong.

---

**Degraded Finding Template** *(operation runs but guarantee is violated)*

```
Degraded Finding F-NN
deviation:        [expected -> actual; both sides explicit]
severity:         degraded
spec:             [clause from Expected Output — must match a cited clause; no paraphrase]
hypothesis:       [one sentence: causal mechanism, not symptom restatement]
connector-impact: [integration-level impact — how integrations are silently affected even though the call appears to succeed]
```

All five slots are required.

---

**Cosmetic Finding Template** *(no correctness or consumer-behavior impact)*

```
Cosmetic Finding F-NN
deviation:  [expected -> actual; both sides explicit]
severity:   cosmetic
spec:       [clause from Expected Output — must match a cited clause; no paraphrase]
hypothesis: [one sentence: causal mechanism, not symptom restatement]
```

All four slots are required.

---

**Phase 5 — Summarize and decide** *(status quo: this decision cannot be made without a committed contract)*

Write a `## Summary` section:

```
Severity counts: breaking: [N] | degraded: [N] | cosmetic: [N] | total: [N]
Verdict: [Contract violated | Contract satisfied]
Coverage: [N] / [total elements in Expected Output] clauses verified, [N] deviations

Recommendations (required for every breaking and degraded finding):
F-NN: [amend-spec | fix-impl | needs-discussion] — [rationale]
```

After the counts and verdict, write:

**Pattern analysis:** If two or more findings share a root cause mechanism, group them:
`Pattern: F-NN and F-MM share [mechanism] — a single fix at [location] resolves both.`

If no pattern exists: `No patterns detected — findings have independent root causes.`

The summary is the decision record the status quo cannot produce: which findings are regressions, which are spec gaps, which need a conversation. Without a committed expected contract, you can only observe that things looked fine or didn't.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## Combination Candidates for Round 6

| Priority | Axis Pair | Primary Targets | Rationale |
|----------|-----------|-----------------|-----------|
| 1 | V-01 + V-03 (preamble + integration-first framing) | C-19, C-14 | Both mechanisms operate before Phase 1 content begins — preamble governs sequencing invariant; integration framing governs finding perspective. The cleanest pre-execution compound: two preamble-level mechanisms reinforcing different criteria |
| 2 | V-02 + V-03 (stratified templates + integration-first) | C-16, C-14, C-06 | Stratified templates supply structural per-finding coverage; integration-first framing supplies substantive connector-impact content — structure and perspective reinforcing the same finding-quality goal from different directions |
| 3 | V-01 + V-02 + C-17 rationale (full structural tier) | C-19, C-16, C-17, C-15 | Preamble-first ensures behavioral rules precede Phase 1; stratified templates eliminate conditional field logic; rationale-anchored breaking template captures C-17 — all three structural criteria in one compound |

## Evaluation Order Guidance

| Priority | Variation | Rationale |
|----------|-----------|-----------|
| 1 | V-01 (preamble-first behavioral protocol) | Tests whether moving the token contract before Phase 1 converts C-18 compliance into C-19 compliance. If C-19 passes on V-01, the structural fix is confirmed. If C-19 still fails, there is a content gap in the token contract itself that needs diagnosis. |
| 2 | V-02 (severity-stratified templates) | Tests whether three-tier template architecture satisfies C-16 where R4 V-02's single unified template with conditional fields could not. C-15 and C-11 should follow automatically. |
| 3 | V-03 (integration-first framing) | Tests whether preamble-level integration framing drives C-14 per-finding coverage without structural template enforcement. Compare C-14 pass rate to V-02 (structural enforcement) to determine whether framing or structure is the more reliable mechanism for integration coverage. |
| 4 | V-04 (preamble + stratified + rationale) | Evaluate after V-01 and V-02 are individually scored. If both pass their primary targets, V-04 should pass both plus C-17 without degradation. The combination tests whether rationale-anchoring (C-17) adds cost without benefit or is genuinely compositional. |
| 5 | V-05 (all axes) | Evaluate last. If V-01 through V-04 all pass their primary targets, V-05 determines whether full-axis combination adds aspirational coverage or introduces coherence degradation from prompt complexity. |
