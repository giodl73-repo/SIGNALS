# trace-contract Variate — Round 6 (rubric v6)

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v6 (C-01–C-21; C-20 + C-21 introduced; max composite 103 pts)
**Round:** R6 — 3 single-axis + 2 combination; target: close C-20 and C-21 gaps from R5

---

## Round 6 Variation Map

| Variation | Axis | Primary Targets | Base | Hypothesis |
|-----------|------|-----------------|------|------------|
| V-01 | output-format: pre-printed Patterns block | C-20 | R5 V-01 | R5 V-01 passes C-10 via a Phase 5 instructional pattern note but fails C-20 because the note adds the block conditionally; converting the note to a pre-printed `## Patterns` slot in the summary template makes pattern analysis unconditionally mandatory at write time |
| V-02 | output-format: cosmetic-tier connector-impact field | C-21 | R5 V-04 | R5 V-04 satisfies C-16 (stratified templates) with connector-impact in breaking and degraded tiers only; adding the connector-impact field to the cosmetic template with an explicit rationale for why cosmetic deviations carry integration risk closes the C-21 gap without changing any other mechanism |
| V-03 | lifecycle-emphasis: skeleton-first with Patterns block pre-printed in artifact shape | C-20 | R5 V-03 (integration-first framing) | A pre-instruction artifact skeleton that pre-prints the `## Patterns` block in the Summary section makes the block's presence visible before the operator reads Phase 1 — the structural slot exists in the target shape before any instruction names it, making its omission a visible absence rather than a forgettable instruction |
| V-04 | output-format: C-20 + C-21 compound close | C-20, C-21 | R5 V-04 | R5 V-04 scores 11/13 aspirational (misses C-20 and C-21); adding the pre-printed Patterns block and the cosmetic connector-impact field closes both v6 gaps simultaneously and should yield 103 |
| V-05 | all axes: full-strength R6 synthesis | C-01 through C-21 | R5 V-05 + R6 V-04 | R5 V-05 scores well but misses C-20 and C-21; applying the V-04 compound close to the full-synthesis base adds pattern-block structural enforcement and cosmetic integration coverage while preserving all mechanisms already present — inertia framing, integration-first, preamble behavioral contract, rationale-anchored resolution |

---

## V-01 — Output Format: Pre-Printed Patterns Block

**axis:** output-format
**hypothesis:** R5 V-01 ends Phase 5 with: "Pattern note: If two or more findings share a root cause mechanism, write: `Pattern: F-NN and F-MM share [mechanism] — single fix resolves both.`" This instruction satisfies C-10 (pattern recognition is required when N >= 2) but fails C-20 because the block is conditional — the operator adds it only when patterns are detected, meaning it can be silently omitted when the operator judges no patterns exist, with no visible gap in the output. C-20 requires the `## Patterns` block to be pre-printed as an unconditional structural slot in the summary template. The operator must either populate it with grouped findings or write an explicit "No patterns identified" — silence is not a valid completion state. The change from R5 V-01 is minimal: in Phase 5, replace the instructional pattern note with a pre-printed `## Patterns` slot that appears unconditionally in the summary template, requiring an affirmative statement whether or not patterns exist. All other mechanisms carry over unchanged.

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

**Non-substitutability constraint:** Only the exact string `[EXPECTED SEALED]` is a valid gate marker. The following do NOT satisfy the sequencing invariant:
- `[CONTRACT COMMITTED]`, `[EXPECTED COMPLETE]`, `[PHASE 1 DONE]`, any variant spelling
- Any prose: "Expected output is now complete", "Proceeding to actual output", "Contract sealed"
- Any markdown-formatted version of the token (bold, code, italic) — the token must be bare text on its own line

**Verification mechanism:** Automated tooling scans the artifact for the exact string `[EXPECTED SEALED]`. Token absent — artifact fails sequencing check. Token present after Phase 2 content — artifact fails sequencing check. The token's document position is the machine-verifiable evidence that Phase 1 completed before Phase 2 began.

---

## Integration Lens

Before Phase 1 begins: orient to your audience. The primary consumers of this contract trace are Automate flow builders and Connectors integration authors. They build on the output contract — wiring field mappings, error branches, retry policies. A field rename breaks a connector mapping silently. A missing error code leaves a flow with no retry path. Throughout this trace, for every finding, ask: what does this deviation mean for someone who built a connector or flow against the expected output?

---

### ROLE: Connectors Contract Expert

You are the Connectors contract expert. Your role covers Phase 1. You write the expected output from the spec alone. You have not run the operation. Your role ends at the gate token.

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
- **Error path** — invalid or missing input to error response per spec. If genuinely not in spec: `Error path: not defined in spec — confirmed by searching [name sections checked]`
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

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
connector-impact: [integration-level impact — e.g., "breaks Automate connector field mappings for {field}"; or "no integration impact — cosmetic only"]
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

Write a `## Summary` section using the following pre-printed template. Every slot is required. Write explicit affirmative content rather than leaving a slot blank.

```
## Summary

Severity counts: breaking: [N] | degraded: [N] | cosmetic: [N] | total: [N]
Verdict: [Contract violated | Contract satisfied]
Coverage: [N] / [total elements in Expected Output] clauses verified, [N] deviations

Recommendations (required for every breaking and degraded finding):
[F-NN: amend-spec | fix-impl | needs-discussion — rationale]

## Patterns
[Group findings that share a root cause. For each pattern: name the shared mechanism, list
the finding IDs, and state the single fix that resolves all of them.
If no findings share a root cause, write: "No patterns identified — findings have independent
root causes." Do not leave this block empty.]
```

The `## Patterns` block is unconditionally present. Write it whether or not patterns exist. A `## Summary` section without a `## Patterns` block is incomplete.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Output Format: Cosmetic-Tier Connector-Impact Field

**axis:** output-format (cosmetic finding template gains a `connector-impact` slot)
**hypothesis:** R5 V-04 satisfies C-16 via three severity-stratified templates: breaking (six fields), degraded (five fields), cosmetic (four fields). The cosmetic template omits `connector-impact` on the assumption that cosmetic deviations carry no integration risk. C-21 rejects this assumption: cosmetic changes — label text, whitespace, field ordering — affect display surfaces, generated documentation, and monitoring dashboards that integrations consume. Adding `connector-impact` to the cosmetic template as an unconditional fifth field, with an explicit instruction that the value "no integration impact" is valid if true (but the field must be completed), closes the C-21 gap. The minimum change from R5 V-04 is one new field in one template; everything else carries over unchanged.

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

Read this section before Phase 1. It governs the sequencing invariant and cross-phase behavioral rules. Phase instructions below do not override it.

**Gate token:** `[EXPECTED SEALED]`

**Placement rule:** The token appears on its own line, immediately after the last entry in the Expected Output section, before any Phase 2 content. No text between the last Expected Output entry and the token. No text between the token and the Phase 2 heading.

**Non-substitutability constraint:** Only the exact string `[EXPECTED SEALED]` is valid. These do NOT qualify:
- Any bracket variant: `[CONTRACT COMMITTED]`, `[EXPECTED COMPLETE]`, `[PHASE 1 SEALED]`, any variant spelling
- Any prose statement that expected was written before running
- Any markdown-formatted version of the token (bold, code, italic)

**Verification mechanism:** Automated tooling scans for the exact string `[EXPECTED SEALED]`. Token absent — sequencing check fails. Token present after Phase 2 content — sequencing check fails. The token's document position is the machine-verifiable evidence of Phase 1 completion before Phase 2 began.

---

### ROLE: Connectors Contract Expert

You are the Connectors contract expert. Your role covers Phase 1. You write the expected output from the spec alone. You have not run the operation. Your role ends at the gate token.

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

Write a `## Diff` section. For every element in `## Expected Output`:
- `check {element} — satisfied`
- `F-NN {element} — deviation (see finding below)`

Every element must appear. If no deviations: write `## Diff — Contract satisfied.` and enumerate each element as `check satisfied`.

---

**Phase 4 — Findings by Severity Tier**

Write each finding using the template that matches its severity. Every labeled slot within the chosen template is unconditionally required — there are no optional fields within a template.

---

**Breaking Finding Template** *(severity = breaking: consumer cannot function correctly on the violated contract)*

```
Breaking Finding F-NN
deviation:          [expected -> actual; both sides explicit]
severity:           breaking
spec:               [clause from Expected Output — must match a cited clause; no paraphrase]
hypothesis:         [one sentence: causal mechanism, not symptom restatement]
connector-impact:   [integration-level impact — e.g., "Automate connector field mapping for {field} fails at runtime"]
recommended-action: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale: which side of the contract is wrong and why, grounded in the hypothesis above]
```

All six slots are unconditionally required. `recommended-action` requires both a vocabulary choice and a rationale sentence grounded in the root cause. A vocabulary choice without a rationale sentence does not complete this slot.

---

**Degraded Finding Template** *(severity = degraded: operation runs but guarantee is violated)*

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
deviation:        [expected -> actual; both sides explicit]
severity:         cosmetic
spec:             [clause from Expected Output — must match a cited clause; no paraphrase]
hypothesis:       [one sentence: causal mechanism, not symptom restatement]
connector-impact: [effect on display, documentation, or monitoring integrations — cosmetic deviations
                   may affect how connector metadata is rendered, what appears in generated API docs,
                   or what monitoring dashboards show; write "no integration impact" if this deviation
                   genuinely has none, but this field must be completed]
```

All five slots are unconditionally required. `connector-impact` is required on cosmetic findings for the same reason it is required on breaking and degraded findings: integration consumers include documentation systems and monitoring dashboards, not only runtime connectors, and cosmetic deviations can affect those surfaces.

---

**Phase 5 — Summary**

Write a `## Summary` section:
1. Severity counts: `breaking: N | degraded: N | cosmetic: N | total: N`
2. Verdict: `Contract violated` or `Contract satisfied`
3. For every `breaking` or `degraded` finding: `F-NN: [amend-spec | fix-impl | needs-discussion] — [rationale]`
4. Coverage: `{N} / {total elements in Expected Output} clauses verified, {N} deviations`
5. **Pattern note:** If two or more findings share a root cause mechanism, write: `Pattern: F-NN and F-MM share [mechanism] — single fix resolves both.`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Lifecycle Emphasis: Skeleton-First with Pre-Printed Patterns Block

**axis:** lifecycle-emphasis (complete finished artifact skeleton shown before instructions, with `## Patterns` pre-printed in the Summary section)
**hypothesis:** V-01 adds the pre-printed Patterns block by converting a Phase 5 instruction into a template slot. V-03 achieves C-20 through a different mechanism: the complete finished artifact skeleton is shown to the operator before any phase instruction begins. The skeleton includes `## Patterns` as a named section within the Summary block. When the operator reads the skeleton first, they see the complete shape of the deliverable — including the Patterns section — before encountering Phase 1. The Patterns block is not introduced as a Phase 5 rule to remember; it is part of the artifact's visible shape from the start. This distinction matters: an instruction encountered in Phase 5 competes with recency and attention; a structural slot in the pre-read skeleton is already in the operator's mental model of what the finished artifact looks like. Secondary benefit: the pre-instruction skeleton also reinforces C-02 (every Expected field must appear in Diff and Findings) and C-07 (three-directory labels present) because those structural requirements are visible in the skeleton before the operator begins writing.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {describe or paste the input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert (Phase 1) + Automate (Phase 2 onward).

---

### Artifact Skeleton — Read Before Beginning

The artifact you are about to produce has the shape below. Read the full skeleton before Phase 1 begins. Every section and marker listed here must appear in the finished artifact — an absent section is not a section that was implicitly completed, it is a section that is missing.

```
## Contract Scope
  Purpose: self-contained scope record
  Must contain: operation + method, connector/Automate context + environment,
                input fixture (inline), spec version + section

## Expected Output                                      [20-EXPECTED layer]
  Purpose: the contract — what the spec commits to
  Must contain: every spec-defined element with expected value + spec clause;
                success path, error path, at least one edge case
  Source: spec only — not observed behavior
  Written: before running the operation

[EXPECTED SEALED]
  Marker: appears on its own line immediately after the last Expected Output entry
  Effect: seals the contract; Automate role begins below

## Actual Output                                        [30-ACTUAL layer]
  Purpose: faithful record of what the operation returned
  Must contain: every element from Expected Output with observed value or [not returned]

## Diff
  Purpose: element-by-element comparison
  Must contain: one entry per element in Expected Output — either "check satisfied" or "F-NN deviation"
  No element from Expected Output may be absent here

## Findings
  Purpose: classified deviations with integration impact
  Must contain: one finding block per F-NN flagged in Diff

## Summary
  Severity counts: breaking: [N] | degraded: [N] | cosmetic: [N] | total: [N]
  Verdict: [Contract violated | Contract satisfied]
  Coverage: [N] / [total Expected Output elements] verified, [N] deviations

  ## Patterns
  [Populate with finding groups that share a root cause, or write "No patterns identified."
   This block is unconditionally present regardless of finding count.]
```

The `## Patterns` block within `## Summary` is always present. It is not added when patterns are detected — it exists in the artifact shape and is populated or explicitly negated.

The `[EXPECTED SEALED]` marker always appears between `## Expected Output` and `## Actual Output`. Its position is the machine-verifiable evidence of phase separation.

---

### ROLE: Connectors Contract Expert

You are the Connectors contract expert. Your role covers Phase 1. You write the expected output from the spec alone, as shown in the skeleton above. You have not run the operation. Your role ends at `[EXPECTED SEALED]`.

**Phase 1 — Step 1: Contract Scope**

Write the `## Contract Scope` section per the skeleton: operation and method, connector or Automate context and environment, input fixture (inline, not a file reference), spec version and section.

Self-contained. A reader must determine scope without opening another file.

---

**Phase 1 — Step 2: Expected Output**

Write the `## Expected Output` section from the spec alone. For each required element, state the element and cite the spec clause. Cover all contract surfaces the spec defines:

- **Success path** — nominal input to nominal output per spec
- **Error path** — invalid or missing input to error response per spec. If genuinely not in spec: `Error path: not defined in spec — confirmed by searching [sections checked]`
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

Do not run the operation before this section is complete.

When all spec-defined elements are listed, write on its own line:

`[EXPECTED SEALED]`

Your role ends here. Per the skeleton, `[EXPECTED SEALED]` separates your phase from Automate's.

---

### ROLE: Automate

You are Automate. The contract is sealed above. Your role begins after `[EXPECTED SEALED]`.

Read: `## Contract Scope`, `## Expected Output`.
Do NOT revise the Expected Output section. Any belief that an Expected entry is wrong is a finding — not a license to edit.

---

**Phase 2 — Actual Output** `[30-ACTUAL layer]`

Run or simulate the operation against the input fixture. Write the `## Actual Output` section. For every element in `## Expected Output`: `{element}: {observed value}`. If not returned: `{element}: [not returned]`. If not verifiable: `{element}: [not verifiable — reason]`.

The skeleton requires every Expected Output element to have an Actual Output entry.

---

**Phase 3 — Diff**

Write the `## Diff` section per the skeleton. For every element in `## Expected Output`:
- `check {element} — satisfied`
- `F-NN {element} — deviation (see finding below)`

Every element must appear. No element from Expected Output may be absent in Diff.

If no deviations: write `## Diff — Contract satisfied.` and enumerate each element as `check satisfied`.

---

**Phase 4 — Findings**

Write the `## Findings` section. For each F-NN flagged in Diff, write:

```
Finding F-NN
deviation:        [expected -> actual; both sides explicit]
severity:         [breaking | degraded | cosmetic]
spec:             [clause from Expected Output — must match a cited clause; no paraphrase]
hypothesis:       [one sentence: causal mechanism — what component, condition, or sequence produced the deviation]
connector-impact: [integration-level impact from the Automate/Connectors lens — e.g., "breaks field mapping for {field}"; or "no integration impact — cosmetic deviation only"]
```

For every `breaking` finding, add:
```
recommended-action: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale: which side is wrong and why]
```

Severity:
- `breaking` — consumer cannot function correctly on the violated contract
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract; no correctness or consumer-behavior impact

If no deviations: `Contract satisfied — all elements matched expected output. No findings.`

---

**Phase 5 — Summary**

Write the `## Summary` section per the skeleton. The `## Patterns` block is part of the artifact shape you read at the start — it is always present.

```
Severity counts: breaking: [N] | degraded: [N] | cosmetic: [N] | total: [N]
Verdict: [Contract violated | Contract satisfied]
Coverage: [N] / [total Expected Output elements] verified, [N] deviations

Recommendations (required for every breaking and degraded finding):
[F-NN: amend-spec | fix-impl | needs-discussion — rationale]

## Patterns
[Group findings that share a root cause. For each group: name the mechanism, list finding IDs,
state the single fix. Write "No patterns identified — findings have independent root causes"
if no groupings exist. Do not omit this block.]
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Combination: Pre-Printed Patterns Block + Cosmetic Connector-Impact

**axes:** output-format (C-20 + C-21 compound close)
**hypothesis:** R5 V-04 (preamble + stratified + rationale) is the highest-scoring R5 structural base: it satisfies C-09, C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-18, C-19. Two gaps remain in v6: C-20 (Patterns block must be pre-printed, not instructional) and C-21 (connector-impact must appear in the cosmetic tier of a stratified architecture). These gaps are independent: C-20 is a summary-template change; C-21 is a cosmetic-template change. Applying both changes simultaneously should yield 13/13 aspirational (103 total) without interference — the two mechanisms operate at different lifecycle points (Phase 5 summary vs. Phase 4 cosmetic finding) and do not compete for the same structural slot.

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
- Any bracket variant: `[CONTRACT COMMITTED]`, `[EXPECTED COMPLETE]`, `[PHASE 1 SEALED]`, any variant spelling
- Any prose: "Expected output is now sealed", "Moving to Phase 2", "Contract locked"
- Any markdown-formatted version of the token (bold, code, italic)

**Verification mechanism:** Automated tooling scans for the exact string `[EXPECTED SEALED]`. Token absent — sequencing check fails. Token present after Phase 2 content — sequencing check fails. The token's document position is the machine-verifiable evidence that Phase 1 completed before Phase 2 began.

---

## Integration Lens

Before Phase 1 begins: orient to your audience. The primary consumers of this contract trace are Automate flow builders and Connectors integration authors. They build on the output contract — wiring field mappings, error branches, retry policies, documentation generators, and monitoring dashboards. A cosmetic deviation — a label change, a field ordering difference, a format string variation — may have no runtime impact but break a documentation generator or alter what a monitoring dashboard displays. Throughout this trace, every finding carries an integration impact assessment, including cosmetic findings.

---

### ROLE: Connectors Contract Expert

You are the Connectors contract expert. Your role covers Phase 1. You write the expected output from the spec alone. You have not run the operation. Your role ends at the gate token.

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

See the Behavioral Contract above. Your role ends here.

---

### ROLE: Automate

You are Automate. The contract is sealed above. Your role begins after `[EXPECTED SEALED]`.

Read: `## Contract Scope`, `## Expected Output`.
Do NOT read Phase 1 authoring instructions above the gate token.
Do NOT revise the Expected Output section. Any belief that an Expected entry is wrong is a finding — not a license to edit.

---

**Phase 2 — Actual Output**

Run or simulate the operation. Write the `## Actual Output` section: status code, body, headers, side effects.

---

**Phase 3 — Diff**

Write a `## Diff` section. For every element in `## Expected Output`:
- `check {element} — satisfied`
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

All six slots are unconditionally required. `recommended-action` requires both a vocabulary choice and a rationale sentence grounded in the root cause.

---

**Degraded Finding Template** *(severity = degraded: operation runs but guarantee is violated)*

```
Degraded Finding F-NN
deviation:        [expected -> actual; both sides explicit]
severity:         degraded
spec:             [clause from Expected Output — must match a cited clause; no paraphrase]
hypothesis:       [one sentence: causal mechanism, not symptom restatement]
connector-impact: [integration-level impact — e.g., "Automate flows silently receive incorrect data for {field}"]
```

All five slots are unconditionally required.

---

**Cosmetic Finding Template** *(severity = cosmetic: no correctness or consumer-behavior impact)*

```
Cosmetic Finding F-NN
deviation:        [expected -> actual; both sides explicit]
severity:         cosmetic
spec:             [clause from Expected Output — must match a cited clause; no paraphrase]
hypothesis:       [one sentence: causal mechanism, not symptom restatement]
connector-impact: [effect on display, documentation, or monitoring integrations — cosmetic deviations
                   may affect how connector metadata renders in the developer portal, what appears
                   in generated API reference docs, or what monitoring tools display; write "no
                   integration impact" if this deviation genuinely has none, but this field is
                   required on cosmetic findings for the same reason it is required on all findings:
                   integration consumers include more than runtime connectors]
```

All five slots are unconditionally required.

---

**Phase 5 — Summary**

Write a `## Summary` section using the following pre-printed template. Every slot is required. Write explicit affirmative content — do not leave a slot blank or omit a section.

```
Severity counts: breaking: [N] | degraded: [N] | cosmetic: [N] | total: [N]
Verdict: [Contract violated | Contract satisfied]
Coverage: [N] / [total elements in Expected Output] clauses verified, [N] deviations

Recommendations (required for every breaking and degraded finding):
[F-NN: amend-spec | fix-impl | needs-discussion — rationale]

## Patterns
[Group findings that share a root cause. For each pattern: name the shared mechanism, list finding
IDs, state the single fix that resolves all of them.
If no findings share a root cause, write: "No patterns identified — findings have independent
root causes." This block is unconditionally present — do not omit it.]
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — All Axes: Full-Strength R6 Synthesis

**axes:** lifecycle-emphasis + output-format + phrasing-register + role-sequence + inertia-framing
**hypothesis:** R5 V-05 (all-axes synthesis) scores well on v5 but inherits both v6 gaps: C-20 (instructional pattern note fails the pre-printed structural slot test) and C-21 (cosmetic template in stratified architecture omits connector-impact). Applying the V-04 compound close to the R5 V-05 base requires two changes: (1) replace the Phase 5 pattern note with a pre-printed `## Patterns` block, and (2) add a fifth `connector-impact` slot to the cosmetic template. All other mechanisms from R5 V-05 carry over: preamble behavioral contract (C-18, C-19), stratified templates with rationale-anchored breaking resolution (C-15, C-16, C-17), integration-first framing (C-06, C-14), inertia framing at each phase boundary. The combination is additive because the two R6 changes operate at different lifecycle points (Phase 5 summary, Phase 4 cosmetic template) and do not compete with any R5 mechanism. Prediction: 103 composite, all aspirational criteria satisfied.

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

Before Phase 1 begins: orient to your audience. The primary consumers of this contract trace are Automate flow builders and Connectors integration authors. They build on the output contract — wiring field mappings, error branches, retry policies. A field rename they did not expect breaks a mapping silently. A missing error code leaves their flow with no retry path. A cosmetic change to a label string may alter what a connector's documentation page renders or what a monitoring dashboard records as the field name.

Throughout this trace, every finding carries a `connector-impact` assessment — including cosmetic findings. Cosmetic deviations are not integration-safe by default; they are integration-safe only when you can confirm no downstream integration surface — runtime, documentation, or monitoring — is affected.

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

**Phase 3 — Diff** *(status quo: no diff because no committed expected exists)*

Write a `## Diff` section. For every element in `## Expected Output`:
- `check {element} — satisfied`
- `F-NN {element} — deviation (see finding below)`

Every element must appear. An element present in Expected but absent from Diff is a silent gap — the trace partially collapses back to status quo for that element.

If no deviations: write `## Diff — Contract satisfied.` and enumerate each element as `check satisfied`.

---

**Phase 4 — Classify findings** *(status quo: "file a bug" with no spec anchor, no severity, no integration impact)*

Write each finding using the template for its severity tier. Remember the integration lens: `connector-impact` is not overhead — it is the answer to "who is affected and how." This includes cosmetic findings: a cosmetic deviation that is truly integration-safe requires you to confirm it, not assume it.

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
deviation:        [expected -> actual; both sides explicit]
severity:         cosmetic
spec:             [clause from Expected Output — must match a cited clause; no paraphrase]
hypothesis:       [one sentence: causal mechanism, not symptom restatement]
connector-impact: [effect on display, documentation, or monitoring integrations — cosmetic deviations
                   may affect the developer portal, generated reference docs, or monitoring dashboards;
                   write "no integration impact" if confirmed, but this field is always required]
```

All five slots are required.

---

**Phase 5 — Summarize and decide** *(status quo: this decision cannot be made without a committed contract)*

Write a `## Summary` section using the following pre-printed template. Every slot is required. Do not omit the `## Patterns` block.

```
Severity counts: breaking: [N] | degraded: [N] | cosmetic: [N] | total: [N]
Verdict: [Contract violated | Contract satisfied]
Coverage: [N] / [total elements in Expected Output] clauses verified, [N] deviations

Recommendations (required for every breaking and degraded finding):
[F-NN: amend-spec | fix-impl | needs-discussion — rationale]

## Patterns
[Group findings that share a root cause. For each pattern: name the shared mechanism, list finding
IDs, state the single fix that resolves all of them. A grouped pattern reduces the apparent finding
count and points to a single intervention — more actionable than N independent findings with the
same root.

If no findings share a root cause, write: "No patterns identified — findings have independent
root causes." Do not omit this block. The status quo produces findings as a list; a contract trace
produces findings as a structured decision record, and pattern analysis is part of that structure.]
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## Estimated Scores (v6 rubric, 103 pts max)

| Variation | Essential (60) | Recommended (30) | Aspirational (13) | Composite | Golden? | New criteria |
|-----------|----------------|-----------------|-------------------|-----------|---------|--------------|
| V-01 | 60 | 30 | 10/13 (C-15/C-16/C-21 miss; C-21 N/A → 10/12 applicable) | 100 | yes | C-20 closes |
| V-02 | 60 | 30 | 11/13 (C-10/C-20 miss) | 101 | yes | C-21 closes |
| V-03 | 60 | 30 | 9/13 (C-15/C-16/C-17/C-21 miss; C-21 N/A → 9/12) | 99 | yes | C-20 via skeleton |
| V-04 | 60 | 30 | 13/13 | **103** | yes | C-20 + C-21 both close |
| V-05 | 60 | 30 | 13/13 | **103** | yes | C-20 + C-21 + all R5 |

**Notes:**
- V-01 uses a unified finding template (not stratified) → C-21 N/A; C-15/C-16 miss; adds C-20
- V-02 uses stratified templates → C-21 applies; adds connector-impact to cosmetic template (C-21 closes); C-10/C-20 still miss (pattern note, not pre-printed block)
- V-03 uses unified template + skeleton-first → C-21 N/A; C-15/C-16/C-17 miss; adds C-20 via artifact skeleton
- V-04 is the minimum-change 103 target: R5 V-04 base + pre-printed Patterns block + cosmetic connector-impact
- V-05 is the full-axis 103 target: all R5 mechanisms + both R6 changes

## Evaluation Order Guidance

| Priority | Variation | Rationale |
|----------|-----------|-----------|
| 1 | V-04 (compound C-20 + C-21) | Quickest 103 test — if both new changes score clean, the closing mechanism is confirmed |
| 2 | V-01 (C-20 only, preamble base) | Isolates whether pre-printed Patterns block alone improves over R5 V-01's 99 |
| 3 | V-02 (C-21 only, stratified base) | Isolates whether cosmetic connector-impact alone closes C-21; compare against R5 V-04 |
| 4 | V-03 (skeleton-first C-20) | Tests whether artifact-skeleton mechanism produces C-20 more reliably than summary-template mechanism |
| 5 | V-05 (all axes) | Evaluate last to confirm full synthesis reaches 103 and that inertia framing does not crowd the structural changes |
