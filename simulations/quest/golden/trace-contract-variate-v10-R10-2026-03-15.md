# trace-contract Variate -- Round 10 (rubric v10)

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v10 (C-01--C-30; essential C-01--C-05; max composite 110; golden threshold: all essential pass + composite >= 80)
**Round:** R10 -- targeting C-29 and C-30 in isolation (V-01, V-02, V-03), then in combination (V-04, V-05)

---

## Round 10 Context

R9 best score: V-05 at full platinum across C-01--C-28 (all 28 criteria). Two new R10 criteria are C-29 and C-30.

Both criteria are escalations from C-28 (mechanism taxonomy, R9). C-28 required a per-finding `mechanism-type:` token selected from a five-item enumeration. R9 V-05 already carries precursor forms of both:

- **C-29 precursor in R9 V-05**: `mechanism-type-shared: [the type token shared by this group, if applicable -- confirms taxonomy alignment; write "mixed" if types differ]` -- the field exists in the Singleton and Multi-pattern branch templates but is marked "if applicable," making it optional. C-29 escalates: the field becomes unconditionally required, and the fix-strategy semantics are explicit -- same-class groupings (`mechanism-type-shared: field-mapping`) signal a systemic root cause requiring one fix; mixed-class groupings (`mechanism-type-shared: mixed`) signal coincident symptoms requiring independent fixes. The fix-strategy implication must be stated so the author understands what the field is doing, not just what to write.

- **C-30 precursor in R9 V-05**: `Mechanism taxonomy distribution: field-mapping:? | serialization-path:? | conditional-branch:? | lifecycle-event:? | schema-contract:? | TAXONOMY-GAP:?` -- the distribution line exists in the Summary but uses pipe-delimited placeholders (`?`) rather than a computed aggregate and uses a verbose label rather than the compact key `mechanism-distribution:`. C-30 escalates: the Summary carries a compact `mechanism-distribution: field-mapping:N serialization-path:N ...` line where `N` is the actual count enumerated from the finding blocks -- not a fill-in template. The author must count type tokens from S5 to fill the aggregate, converting the distribution line from a placeholder to a cross-session-comparable signal.

The two new criteria operate on different structural layers:
- **C-29** -- synthesis-semantics layer: the meaning and required/optional status of `mechanism-type-shared:` inside Patterns branch templates
- **C-30** -- summary-aggregate layer: the format and computation obligation for the taxonomy distribution line in Summary

The two layers are orthogonal:
- C-29 operates on what `mechanism-type-shared:` means and whether it is required
- C-30 operates on whether the Summary distribution line is a template placeholder or a computed aggregate

---

## Round 10 Variation Map

| Variation | Axis | Primary Targets | Hypothesis |
|-----------|------|-----------------|------------|
| V-01 | role-sequence (C-29 isolation) | C-29 | R9 V-05 marks `mechanism-type-shared:` as "if applicable." C-29 requires it as an unconditional field with fix-strategy semantics. V-01 uses the role-sequence axis: the Connectors contract expert owns both Phase 1 (expected output) and Phase 4 (Patterns synthesis). Because the same expert who authored the contract specification is responsible for grouping findings by mechanism class, `mechanism-type-shared:` becomes a required expert judgment -- not an optional annotation -- and the fix-strategy semantics are stated as part of the expert's synthesis obligation. Isolation tests whether role-sequence framing promotes `mechanism-type-shared:` from optional to required without C-30 changes. |
| V-02 | output-format (C-30 isolation) | C-30 | R9 V-05 carries a pipe-delimited `Mechanism taxonomy distribution: field-mapping:? \| ...` template. C-30 requires a computed compact aggregate. V-02 uses the output-format axis: the Summary `mechanism-distribution:` line is structured as a compact key:count space-separated aggregate (`mechanism-distribution: field-mapping:2 serialization-path:1`), and the fill instruction explicitly requires the author to enumerate type tokens from S5 finding blocks rather than fill a template. The format change (pipe-delimited placeholders to computed space-separated aggregate) and the instruction change (template fill to enumeration obligation) are the axis changes. Isolation tests whether the output-format upgrade to Summary produces C-30 without touching Patterns. |
| V-03 | lifecycle-emphasis (C-29 + C-30 via taxonomy census) | C-29, C-30 | V-01 and V-02 reach C-29 and C-30 independently via orthogonal axes. V-03 uses the lifecycle-emphasis axis to crack both via a single mechanism: a named "Taxonomy Synthesis" step (Step 5.5) inserted between Findings (S5) and the post-findings closure token. The step requires the author to: (a) enumerate all `mechanism-type:` tokens from S5 finding blocks and write the `mechanism-distribution:` aggregate -- feeding C-30 directly; (b) for each Patterns group candidate, identify whether the grouped findings share a single type token or span multiple types, and annotate the group with `mechanism-type-shared:` -- feeding C-29 directly. The synthesis step creates a lifecycle position where both fields are computed before the gates are written, making them obligatory rather than optional. Isolation tests whether a dedicated synthesis step between S5 and S6 satisfies both new criteria via a single axis change. |
| V-04 | role-sequence x output-format (C-29 x C-30) | C-29, C-30 | C-29 (synthesis-semantics) and C-30 (summary-aggregate) operate on different structural positions. V-04 combines V-01 role-sequence and V-02 output-format: Connectors expert owns Patterns synthesis (making `mechanism-type-shared:` a required expert judgment with fix-strategy semantics) and the output-format upgrade to Summary makes `mechanism-distribution:` a computed aggregate. Tests whether the two-axis combination produces additive coverage without regression against C-01--C-28. |
| V-05 | role-sequence x output-format x lifecycle-emphasis + R9 platinum base | C-29, C-30, C-01--C-28 | Full R10 ceiling. All three new-axis changes layered onto the R9 V-05 platinum base via skeleton pre-declaration: `mechanism-type-shared:` promoted from "if applicable" to required with fix-strategy semantics in both Singleton and Multi-pattern branch templates; `mechanism-distribution:` upgraded from pipe-delimited placeholder to compact computed aggregate in Summary; explicit Taxonomy Synthesis step named in the behavioral protocol as a required transition between S5 and S7; skeleton now carries the upgraded Summary slot and upgraded Patterns branch templates so both obligations are visible before Phase 1 begins. Two new behavioral protocol invariants added (C-29 invariant: `mechanism-type-shared:` always required; C-30 invariant: `mechanism-distribution:` computed from S5, not from a template). Regression hypothesis: the two new invariants add slot-filling obligations without changing role structure, phase sequence, or essential coverage requirements. |

---

## V-01 -- Role Sequence: Connectors Expert Owns Patterns Synthesis (C-29 isolation)

**axis:** role-sequence
**hypothesis:** R9 V-05 carries `mechanism-type-shared:` in the Patterns branch templates but marks it "if applicable," making it an optional taxonomy annotation. C-29 escalates: the field must be unconditionally required, and its purpose must be stated -- same-class groupings signal a systemic root cause (one fix resolves all grouped findings); mixed-class groupings signal coincident symptoms (independent fixes). The role-sequence axis creates a structural reason for the field to be required: the Connectors contract expert owns both Phase 1 (expected output, sealed by gate token) and Phase 4 (Patterns synthesis). Because the same expert who authored the contract specification groups findings by mechanism class, `mechanism-type-shared:` is not an optional annotation -- it is the expert's required statement of mechanism alignment, and the fix-strategy semantics are part of the synthesis judgment. Automate cannot make this judgment because Automate does not hold the contract; the expert who knows which mechanisms are systemic vs coincident is the one who wrote the spec. Isolation: only the role-sequence framing and the `mechanism-type-shared:` promotion from optional to required with fix-strategy semantics change. C-30 is not targeted.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state -- inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### Role Assignments

Two roles with strict phase ownership:

**Connectors Contract Expert** -- Phase 1 (Expected Output) + Phase 4 (Patterns Synthesis)
Domain authority on Automate/Connectors contracts. You hold the spec. You have not run the operation. You write the contract from the spec alone and seal it. After Automate files findings, you synthesize patterns by grouping findings by shared mechanism class. You judge whether grouped findings share a single mechanism type (systemic root cause) or span multiple types (coincident symptoms).

**Automate** -- Phase 2 (Execution) + Phase 3 (Diff and Findings)
Execution authority. You begin after the expected-output gate is placed. You run the operation, capture actual output, diff against sealed expected output, and write findings. You do not modify the Expected Output section.

---

### Step 1 -- Contract Scope

Write a `## Contract Scope` section:
- Operation name and HTTP method (or equivalent)
- Connector or Automate context and environment
- Input fixture -- state inline; no external file references
- Spec version and section governing this operation's output contract

---

### Step 2 -- Expected Output (Phase 1 -- Connectors Contract Expert)

You are the Connectors contract expert. You have not run the operation. You write from the spec alone. Your role ends when the gate token is placed.

Write the `## Expected Output` section. Cover all three contract surfaces:
- **Success path** -- nominal input, nominal output per spec
- **Error path** -- invalid or missing input, expected error response per spec
- **At least one edge case** -- empty collection, null required field, rate-limit trigger, auth expiry

For each expected element, cite the specific clause from the spec that requires it (rule number, named constraint, or sub-clause path -- not a section heading alone). An expected element without a spec citation is not a valid contract entry. If a surface is not defined in the spec, write: `[surface]: not specified in spec`.

When Expected Output is complete and every element carries a spec citation, count the distinct expected elements. Write the gate token on its own line immediately after the last expected element:

```
[EXPECTED-SEALED | clauses:{N} | date:{YYYY-MM-DD} | author:contract-expert | phase:1-complete]
```

Replace `{N}` with the exact element count. Replace `{YYYY-MM-DD}` with today's date. Do not run or simulate the operation before writing this token.

---

### Step 3 -- Actual Output (Phase 2 -- Automate)

You are Automate. You begin after the `[EXPECTED-SEALED ...]` token. Do not modify the Expected Output section. Any belief that an Expected entry is incorrect is a finding -- record it in Step 5; do not edit.

Run or simulate the operation. Write the `## Actual Output` section: status code, response body, headers, all observable side effects.

---

### Step 4 -- Diff (Phase 2 -- Automate)

Write the `## Diff` section. For every element in `## Expected Output`:
- `pass -- {element} -- satisfied`, or
- `F-NN -- {element} -- deviation (see findings)`

Every element must appear. Elements present in Expected Output but absent from the Diff are silent omissions -- the trace fails C-02 regardless of finding quality.

If no deviations: write `## Diff -- Contract satisfied. No findings.` and skip to Step 6.

---

### Step 5 -- Findings (Phase 2 -- Automate)

For each deviation, write a finding entry using the appropriate severity-tier template:

**BREAKING FINDING**
```
Finding F-NN [BREAKING]
deviation:        expected [X]; actual [Y]
spec:             [specific clause from Expected Output -- rule number, named constraint, or sub-clause path]
hypothesis-draft: [write your initial hypothesis here]
self-test:        [Could you have written this from the deviation line alone, without knowing the system? YES -- symptom restatement; rewrite naming the internal mechanism. NO -- mechanism; proceed.]
mechanism-type:   [select one: field-mapping | serialization-path | conditional-branch | lifecycle-event | schema-contract -- or TAXONOMY-GAP + explanation]
mechanism:        [final hypothesis after self-test -- names the internal process, mapping, serialization path, or code condition; must be consistent with mechanism-type]
connector-impact: [what breaks for Automate flows or Connector integrations relying on this field/behavior]
recommendation:   [amend-spec | fix-impl | needs-discussion]
rationale:        [one sentence: which side of the contract is wrong and why, grounded in the mechanism]
```

**DEGRADED FINDING**
```
Finding F-NN [DEGRADED]
deviation:        expected [X]; actual [Y]
spec:             [specific clause]
hypothesis-draft: [write your initial hypothesis here]
self-test:        [Could you have written this from the deviation line alone? YES -- rewrite. NO -- proceed.]
mechanism-type:   [select one token from the taxonomy, or TAXONOMY-GAP + explanation]
mechanism:        [final hypothesis after self-test]
connector-impact: [what silently fails or degrades for Automate flows or Connector integrations]
recommendation:   [amend-spec | fix-impl | needs-discussion]
```

**COSMETIC FINDING**
```
Finding F-NN [COSMETIC]
deviation:        expected [X]; actual [Y]
spec:             [specific clause]
hypothesis-draft: [write your initial hypothesis here]
self-test:        [Could you have written this from the deviation line alone? YES -- rewrite. NO -- proceed.]
mechanism-type:   [select one token from the taxonomy, or TAXONOMY-GAP + explanation]
mechanism:        [final hypothesis after self-test]
```

Hypothesis protocol (all tiers): `hypothesis-draft:` is the initial attempt. `self-test:` applies the necessary-information condition: could this draft have been written by reading only `expected [X]; actual [Y]` with no knowledge of the system's architecture, code, or schema? YES: symptom restatement -- rewrite naming a specific internal component. NO: mechanism -- proceed. `mechanism-type:` selects the token that best describes the class of failure. `mechanism:` is the final hypothesis, consistent with the selected type token.

**After the last finding block**, write the post-findings closure token on its own line:

```
[FINDINGS-RESOLVED | gate-clauses:{N from EXPECTED-SEALED} | clauses-resolved:{M} | phase:5-complete]
```

- `gate-clauses:{N}` must echo the `clauses:` value from `[EXPECTED-SEALED]`
- `clauses-resolved:{M}` = count of expected elements that either passed in the Diff or have a finding filed against them
- If `gate-clauses != clauses-resolved`: write `CLAUSE-GAP -- unaccounted clause IDs: [list]` and resolve before proceeding

---

### Step 6 -- Summary

Write a `## Summary` section:

```
| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

Verdict: Contract violated / Contract satisfied

Recommendations:
[F-NN: amend-spec / fix-impl / needs-discussion -- rationale -- one line per breaking/degraded finding]

Coverage: {N} / {total in Expected Output} clauses verified, {N} deviations found

Mechanism taxonomy distribution: field-mapping:{N} | serialization-path:{N} | conditional-branch:{N} | lifecycle-event:{N} | schema-contract:{N} | TAXONOMY-GAP:{N}
```

---

### Step 7 -- Patterns (Phase 4 -- Connectors Contract Expert)

You are the Connectors contract expert. You resume after Automate has filed all findings and written the post-findings closure token. Write the `## Patterns` section.

Count distinct root cause groups across all findings. Apply exactly one of the three branch templates below. **This section may not be silently omitted regardless of finding count.**

For each group, determine whether the findings share a single mechanism type token. This judgment belongs to the Connectors contract expert: same-class groupings indicate a systemic defect in one mapping, serialization path, or contract interpretation -- one fix resolves the group. Mixed-class groupings indicate coincident symptoms with independent root causes -- each finding likely requires a separate fix.

**Branch: Zero (apply when: total findings = 0, OR no two findings share a root cause)**

```
## Patterns
no-pattern-confirmation: [confirm either (a) no deviations were found and the contract was fully satisfied, or (b) each finding has an independent root cause and no cross-finding pattern exists]
```

**Branch: Singleton (apply when: exactly one root cause group containing two or more findings exists)**

```
## Patterns
single-finding-ref:    [finding IDs in this group, e.g., F-01, F-03]
root-cause:            [the shared causal mechanism -- the internal process or condition common to all findings]
mechanism-type-shared: [the single mechanism-type token if all findings share one class, e.g., field-mapping; write "mixed" if findings span multiple classes -- REQUIRED]
fix-strategy:          [same-class: one spec or implementation change resolves all findings in this group | mixed: findings require independent fixes -- enumerate per finding]
attribution:
  - F-NN: [one sentence: how this finding follows from the shared root cause]
  - F-NN: [one sentence: how this finding follows from the shared root cause]
single-fix:            [the change that resolves all findings if mechanism-type-shared is a single class; or "see fix-strategy" if mixed]
```

`mechanism-type-shared:` is required. It is the Connectors contract expert's determination of mechanism alignment for this group. "If applicable" does not apply -- fill unconditionally.

**Branch: Multi-pattern (apply when: two or more distinct root cause groups, each with two or more findings)**

```
## Patterns
pattern-1:
  root-cause:           [shared causal mechanism for this group]
  mechanism-type-shared: [the single mechanism-type token if all findings in this group share one class; write "mixed" if they span classes -- REQUIRED]
  fix-strategy:         [same-class: one fix | mixed: independent fixes -- enumerate per finding]
  findings:             [F-NN, F-MM]
  single-fix:           [resolution for this group if same-class; or "see fix-strategy" if mixed]
pattern-2:
  root-cause:           [shared causal mechanism for this group]
  mechanism-type-shared: [token or "mixed" -- REQUIRED]
  fix-strategy:         [same-class: one fix | mixed: independent fixes]
  findings:             [F-PP, F-QQ]
  single-fix:           [resolution]
[repeat pattern-N block for each additional group]
patterns-summary: {N} patterns identified covering {M} of {total} findings
```

`mechanism-type-shared:` is required in every pattern block. All four slots (`root-cause:`, `mechanism-type-shared:`, `findings:`, `fix-strategy:`) are unconditional.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 -- Output Format: Computed Mechanism-Distribution Aggregate in Summary (C-30 isolation)

**axis:** output-format
**hypothesis:** R9 V-05 carries `Mechanism taxonomy distribution: field-mapping:? | serialization-path:? | conditional-branch:? | lifecycle-event:? | schema-contract:? | TAXONOMY-GAP:?` in the Summary -- the correct structural position, but with pipe-delimited placeholders and a verbose label. The author fills `?` values but has no explicit instruction to enumerate type tokens from the finding blocks. C-30 escalates: the Summary carries a compact `mechanism-distribution:` key with space-separated type:count pairs (`mechanism-distribution: field-mapping:2 serialization-path:1`), and the fill instruction explicitly directs the author to enumerate `mechanism-type:` tokens from S5 finding blocks and count per type -- not to fill a template. The aggregate is computed, not estimated. This compact format is cross-session comparable: a reader can compare `mechanism-distribution` lines across multiple contract runs to detect trending of systemic failure patterns. Isolation: only the Summary aggregate format and fill instruction change. C-29 is not targeted -- `mechanism-type-shared:` in Patterns branches remains as in R9 V-05 (present but marked "if applicable").

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state -- inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### Step 1 -- Contract Scope

Write a `## Contract Scope` section:
- Operation name and HTTP method (or equivalent)
- Connector or Automate context and environment
- Input fixture -- state inline; no external file references
- Spec version and section governing this operation's output contract

---

### Step 2 -- Expected Output (Phase 1 -- Connectors Contract Expert)

**Role**: You are the Connectors contract expert. You have not run the operation. You write from the spec alone. Your role ends when the gate token is placed.

Write the `## Expected Output` section. Cover all three contract surfaces:
- **Success path** -- nominal input, nominal output per spec
- **Error path** -- invalid or missing input, expected error response per spec
- **At least one edge case** -- empty collection, null required field, rate-limit trigger, auth expiry

For each expected element, cite the specific clause from the spec (rule number, named constraint, or sub-clause path -- not a section heading alone). An expected element without a spec citation is not a valid contract entry. If a surface is not defined in the spec, write: `[surface]: not specified in spec`.

When Expected Output is complete, count the distinct expected elements. Write the gate token immediately after the last expected element:

```
[EXPECTED-SEALED | clauses:{N} | date:{YYYY-MM-DD} | author:contract-expert | phase:1-complete]
```

Do not run or simulate the operation before writing this token.

---

### Step 3 -- Actual Output (Phase 2 -- Automate)

**Role**: You are Automate. You begin after `[EXPECTED-SEALED ...]`. Do not modify the Expected Output section.

Run or simulate the operation. Write the `## Actual Output` section: status code, response body, headers, all observable side effects.

---

### Step 4 -- Diff

Write the `## Diff` section. For every element in `## Expected Output`:
- `pass -- {element} -- satisfied`, or
- `F-NN -- {element} -- deviation (see findings)`

Every element must appear. Missing elements are silent omissions -- the trace fails C-02 regardless of finding quality.

If no deviations: write `## Diff -- Contract satisfied. No findings.` and skip to Step 6.

---

### Step 5 -- Findings

For each deviation, write a finding entry:

**BREAKING FINDING**
```
Finding F-NN [BREAKING]
deviation:        expected [X]; actual [Y]
spec:             [specific clause from Expected Output]
hypothesis-draft: [initial hypothesis]
self-test:        [Could you have written this from the deviation line alone without system knowledge? YES -- rewrite. NO -- proceed.]
mechanism-type:   [field-mapping | serialization-path | conditional-branch | lifecycle-event | schema-contract | TAXONOMY-GAP + explanation]
mechanism:        [final hypothesis after self-test -- consistent with mechanism-type]
connector-impact: [what breaks for Automate flows or Connector integrations]
recommendation:   [amend-spec | fix-impl | needs-discussion]
rationale:        [one sentence: which side is wrong and why]
```

**DEGRADED FINDING**
```
Finding F-NN [DEGRADED]
deviation:        expected [X]; actual [Y]
spec:             [specific clause]
hypothesis-draft: [initial hypothesis]
self-test:        [Could you have written this from the deviation line alone? YES -- rewrite. NO -- proceed.]
mechanism-type:   [token from taxonomy, or TAXONOMY-GAP + explanation]
mechanism:        [final hypothesis after self-test]
connector-impact: [what silently fails or degrades]
recommendation:   [amend-spec | fix-impl | needs-discussion]
```

**COSMETIC FINDING**
```
Finding F-NN [COSMETIC]
deviation:        expected [X]; actual [Y]
spec:             [specific clause]
hypothesis-draft: [initial hypothesis]
self-test:        [Could you have written this from the deviation line alone? YES -- rewrite. NO -- proceed.]
mechanism-type:   [token from taxonomy, or TAXONOMY-GAP + explanation]
mechanism:        [final hypothesis after self-test]
```

**After the last finding block**, write the post-findings closure token:

```
[FINDINGS-RESOLVED | gate-clauses:{N from EXPECTED-SEALED} | clauses-resolved:{M} | phase:5-complete]
```

If `gate-clauses != clauses-resolved`: write `CLAUSE-GAP -- unaccounted clause IDs: [list]` and resolve before continuing.

---

### Step 6 -- Summary

Write a `## Summary` section using the following format:

```
| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

Verdict: Contract violated / Contract satisfied

Recommendations:
[F-NN: amend-spec / fix-impl / needs-discussion -- rationale -- one line per breaking/degraded finding]

Coverage: {N} / {total in Expected Output} clauses verified, {N} deviations found

mechanism-distribution: [type]:[count] [type]:[count] ...
```

**`mechanism-distribution:` fill instruction**: Walk through every finding block in S5. For each finding, read its `mechanism-type:` field. Tally the count per type token. Write the result as space-separated type:count pairs, omitting types with zero occurrences. Include only types that appear in at least one finding. Example: `mechanism-distribution: field-mapping:2 serialization-path:1` means two findings had `mechanism-type: field-mapping` and one had `mechanism-type: serialization-path`. If there are zero findings, write: `mechanism-distribution: none`.

This aggregate is not a template to fill with estimates -- it is enumerated directly from the S5 finding blocks. A distribution line with placeholder values or pipe-delimited format fails this requirement.

---

### Step 7 -- Patterns

Write a `## Patterns` section.

If two or more findings share a root cause, group them, name the shared mechanism, list the finding IDs, and state the single fix that would resolve all findings in the group. When grouping, note whether grouped findings share a `mechanism-type` token -- same-type groupings often indicate a single systemic fix.

If no findings share a root cause (or if there are zero or one findings), write: `No cross-finding patterns detected.`

**This section may not be silently omitted regardless of finding count.**

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 -- Lifecycle Emphasis: Taxonomy Synthesis Step (C-29 + C-30 via census)

**axis:** lifecycle-emphasis
**hypothesis:** V-01 reaches C-29 by promoting `mechanism-type-shared:` from optional to required via role-sequence framing. V-02 reaches C-30 by changing the Summary aggregate format and adding an enumeration instruction. V-03 reaches both via a single lifecycle change: a named "Taxonomy Synthesis" step (Step 5.5) inserted between the last finding block and the post-findings closure token. Step 5.5 has two sub-tasks: (a) enumerate all `mechanism-type:` tokens from S5 finding blocks, tally per type, and write the `mechanism-distribution:` aggregate -- this directly satisfies C-30; (b) for each candidate Patterns group, read the `mechanism-type:` tokens of the group's findings, determine whether they share a single class or span multiple classes, and write the `mechanism-type-shared:` determination for each group -- this directly satisfies C-29 by making the determination a named lifecycle step rather than a Patterns template slot that may or may not be filled. The synthesis step is positioned before the gate is closed (`[FINDINGS-RESOLVED ...]`), so both outputs are computed before the Summary is written and before the Patterns section applies any branch template. The lifecycle position is the axis: by placing taxonomy analysis as a required transition step between findings and closure, both C-29 and C-30 are satisfied as direct outputs of the step rather than as structural obligations that must be remembered.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state -- inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### Step 1 -- Contract Scope

Write a `## Contract Scope` section:
- Operation name and HTTP method (or equivalent)
- Connector or Automate context and environment
- Input fixture -- state inline; no external file references
- Spec version and section governing this operation's output contract

---

### Step 2 -- Expected Output (Phase 1 -- Connectors Contract Expert)

**Role**: You are the Connectors contract expert. You have not run the operation. You write from the spec alone. Your role ends when the gate token is placed.

Write the `## Expected Output` section. Cover all three contract surfaces:
- **Success path** -- nominal input, nominal output per spec
- **Error path** -- invalid or missing input, expected error response per spec
- **At least one edge case** -- empty collection, null required field, rate-limit trigger, auth expiry

For each expected element, cite the specific spec clause (rule number, named constraint, or sub-clause path -- not a section heading alone). An expected element without a spec citation is not a valid contract entry. If a surface is not in the spec, write: `[surface]: not specified in spec`.

When Expected Output is complete, write:

```
[EXPECTED-SEALED | clauses:{N} | date:{YYYY-MM-DD} | author:contract-expert | phase:1-complete]
```

Do not run or simulate the operation before writing this token.

---

### Step 3 -- Actual Output (Phase 2 -- Automate)

**Role**: You are Automate. You begin after `[EXPECTED-SEALED ...]`. Do not modify the Expected Output section.

Run or simulate the operation. Write the `## Actual Output` section: status code, response body, headers, observable side effects.

---

### Step 4 -- Diff

Write the `## Diff` section. For every element in `## Expected Output`:
- `pass -- {element} -- satisfied`, or
- `F-NN -- {element} -- deviation (see findings)`

Every element must appear. Missing elements are silent omissions.

If no deviations: write `## Diff -- Contract satisfied. No findings.` and skip to Step 5.5.

---

### Step 5 -- Findings

For each deviation, write a finding entry using the appropriate severity-tier template:

**BREAKING FINDING**
```
Finding F-NN [BREAKING]
deviation:        expected [X]; actual [Y]
spec:             [specific clause from Expected Output -- rule number, named constraint, or sub-clause path]
hypothesis-draft: [initial hypothesis]
self-test:        [Could you have written this from the deviation line alone, without system knowledge? YES -- rewrite. NO -- proceed.]
mechanism-type:   [field-mapping | serialization-path | conditional-branch | lifecycle-event | schema-contract | TAXONOMY-GAP + explanation]
mechanism:        [final hypothesis after self-test -- consistent with mechanism-type]
connector-impact: [what breaks for Automate flows or Connector integrations]
recommendation:   [amend-spec | fix-impl | needs-discussion]
rationale:        [one sentence: which side is wrong and why]
```

**DEGRADED FINDING**
```
Finding F-NN [DEGRADED]
deviation:        expected [X]; actual [Y]
spec:             [specific clause]
hypothesis-draft: [initial hypothesis]
self-test:        [Could you have written this from the deviation line alone? YES -- rewrite. NO -- proceed.]
mechanism-type:   [token from taxonomy, or TAXONOMY-GAP]
mechanism:        [final hypothesis after self-test]
connector-impact: [what silently fails or degrades]
recommendation:   [amend-spec | fix-impl | needs-discussion]
```

**COSMETIC FINDING**
```
Finding F-NN [COSMETIC]
deviation:        expected [X]; actual [Y]
spec:             [specific clause]
hypothesis-draft: [initial hypothesis]
self-test:        [Could you have written this from the deviation line alone? YES -- rewrite. NO -- proceed.]
mechanism-type:   [token from taxonomy, or TAXONOMY-GAP]
mechanism:        [final hypothesis after self-test]
```

---

### Step 5.5 -- Taxonomy Synthesis (required transition step)

This step is required before writing the post-findings closure token, the Summary, or the Patterns section. It has two sub-tasks.

**Sub-task A -- Mechanism-Distribution Census**

Walk through every finding block written in Step 5 in order. For each finding, read the `mechanism-type:` field value. Tally the count per type token across all findings. Write the result as the `mechanism-distribution:` line:

```
mechanism-distribution: [type]:[count] [type]:[count] ...
```

Include only type tokens that appear in at least one finding. Use space-separated type:count pairs. Example: `mechanism-distribution: field-mapping:3 conditional-branch:1`. If zero findings: `mechanism-distribution: none`.

This line will be copied verbatim into the Summary in Step 6.

**Sub-task B -- Group Type Alignment**

For each candidate Patterns group (two or more findings sharing a root cause), read the `mechanism-type:` token of each finding in the group. Determine: do all findings in this group share a single mechanism type, or do they span multiple types?

Write one line per candidate group:

```
group-candidate-N: findings=[F-NN, F-MM] mechanism-type-shared=[type token if all share one class; or "mixed"]
```

These determinations will be copied into the Patterns branch template in Step 7.

After completing both sub-tasks, write the post-findings closure token:

```
[FINDINGS-RESOLVED | gate-clauses:{N from EXPECTED-SEALED} | clauses-resolved:{M} | phase:5-complete]
```

If `gate-clauses != clauses-resolved`: write `CLAUSE-GAP -- unaccounted clause IDs: [list]` and resolve before continuing.

---

### Step 6 -- Summary

Write a `## Summary` section:

```
| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

Verdict: Contract violated / Contract satisfied

Recommendations:
[F-NN: amend-spec / fix-impl / needs-discussion -- rationale -- one line per breaking/degraded finding]

Coverage: {N} / {total in Expected Output} clauses verified, {N} deviations found

mechanism-distribution: [copy the line from Step 5.5 Sub-task A verbatim]
```

---

### Step 7 -- Patterns

Write a `## Patterns` section. Count distinct root cause groups. Apply the matching branch template. **This section may not be silently omitted.**

**Branch: Zero (apply when: total findings = 0, OR no two findings share a root cause)**

```
## Patterns
no-pattern-confirmation: [confirm no deviations found or each finding has an independent root cause]
```

**Branch: Singleton (apply when: exactly one root cause group containing two or more findings)**

```
## Patterns
single-finding-ref:    [finding IDs in this group]
root-cause:            [shared causal mechanism]
mechanism-type-shared: [copy from Step 5.5 Sub-task B group determination for this group]
attribution:
  - F-NN: [one sentence: how this finding follows from the shared root cause]
  - F-NN: [one sentence: how this finding follows from the shared root cause]
single-fix:            [what change resolves all findings if mechanism-type-shared is a single class; enumerate per finding if "mixed"]
```

**Branch: Multi-pattern (apply when: two or more distinct root cause groups)**

```
## Patterns
pattern-1:
  root-cause:           [shared causal mechanism]
  mechanism-type-shared: [copy from Step 5.5 Sub-task B for this group]
  findings:             [F-NN, F-MM]
  single-fix:           [resolution if same-class; enumerate per finding if "mixed"]
pattern-2:
  root-cause:           [shared causal mechanism]
  mechanism-type-shared: [copy from Step 5.5 Sub-task B for this group]
  findings:             [F-PP, F-QQ]
  single-fix:           [resolution]
[repeat pattern-N block for each additional group]
patterns-summary: {N} patterns identified covering {M} of {total} findings
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 -- Combination: Role Sequence x Output Format (C-29 x C-30)

**axes:** role-sequence x output-format
**hypothesis:** C-29 (mechanism-type-shared as required field with fix-strategy semantics) and C-30 (mechanism-distribution as computed compact aggregate) operate on different structural positions: C-29 on the Patterns synthesis layer, C-30 on the Summary aggregate layer. V-04 combines V-01 role-sequence and V-02 output-format: the Connectors contract expert owns Phase 4 (Patterns synthesis), making `mechanism-type-shared:` a required expert judgment; the Summary uses the compact `mechanism-distribution: type:count type:count` format with an explicit enumeration instruction. The combination is additive: neither change helps the other's failure mode -- role framing does not produce a correct Summary aggregate, and output format does not promote `mechanism-type-shared:` from optional to required. Their co-presence via a single prompt provides both mechanisms without interaction. Tests whether C-29 + C-30 can be simultaneously satisfied while preserving all C-01--C-28 criteria from the R9 V-05 base.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state -- inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### Role Assignments

**Connectors Contract Expert** -- Phase 1 (Expected Output) + Phase 4 (Patterns Synthesis)
Domain authority on the Automate/Connectors contract. You write the expected output from the spec and seal it. After Automate files findings, you own the Patterns synthesis: you group findings by shared mechanism class and make the required `mechanism-type-shared:` determination for each group.

**Automate** -- Phase 2 (Execution) + Phase 3 (Diff and Findings)
Execution authority. You begin after the expected-output gate. You run the operation, diff, and write findings. You do not modify the Expected Output section.

---

### Step 1 -- Contract Scope

Write a `## Contract Scope` section:
- Operation name and HTTP method (or equivalent)
- Connector or Automate context and environment
- Input fixture -- state inline; no external file references
- Spec version and section governing this operation's output contract

---

### Step 2 -- Expected Output (Phase 1 -- Connectors Contract Expert)

You are the Connectors contract expert. You have not run the operation. You write from the spec alone.

Write the `## Expected Output` section. Cover all three contract surfaces:
- **Success path** -- nominal input, nominal output per spec
- **Error path** -- invalid or missing input, expected error response per spec
- **At least one edge case** -- empty collection, null required field, rate-limit trigger, auth expiry

For each expected element, cite the specific spec clause (rule number, named constraint, or sub-clause path -- not a section heading alone). An expected element without a spec citation is not a valid contract entry. If a surface is not in the spec, write: `[surface]: not specified in spec`.

When Expected Output is complete, count the distinct expected elements and write the gate token:

```
[EXPECTED-SEALED | clauses:{N} | date:{YYYY-MM-DD} | author:contract-expert | phase:1-complete]
```

Do not run or simulate the operation before writing this token. Your role is suspended until Step 7.

---

### Step 3 -- Actual Output (Phase 2 -- Automate)

You are Automate. You begin after `[EXPECTED-SEALED ...]`. Do not modify the Expected Output section.

Run or simulate the operation. Write the `## Actual Output` section: status code, response body, headers, all observable side effects.

---

### Step 4 -- Diff (Phase 2 -- Automate)

Write the `## Diff` section. For every element in `## Expected Output`:
- `pass -- {element} -- satisfied`, or
- `F-NN -- {element} -- deviation (see findings)`

Every element must appear. Missing elements fail C-02 regardless of finding quality.

If no deviations: write `## Diff -- Contract satisfied. No findings.` and skip to Step 6.

---

### Step 5 -- Findings (Phase 2 -- Automate)

For each deviation, write a finding entry using the appropriate severity-tier template:

**BREAKING FINDING**
```
Finding F-NN [BREAKING]
deviation:        expected [X]; actual [Y]
spec:             [specific clause from Expected Output]
hypothesis-draft: [initial hypothesis]
self-test:        [Could you have written this from the deviation line alone, without system knowledge? YES -- rewrite. NO -- proceed.]
mechanism-type:   [field-mapping | serialization-path | conditional-branch | lifecycle-event | schema-contract | TAXONOMY-GAP + explanation]
mechanism:        [final hypothesis after self-test -- consistent with mechanism-type]
connector-impact: [what breaks for Automate flows or Connector integrations]
recommendation:   [amend-spec | fix-impl | needs-discussion]
rationale:        [one sentence: which side is wrong and why]
```

**DEGRADED FINDING**
```
Finding F-NN [DEGRADED]
deviation:        expected [X]; actual [Y]
spec:             [specific clause]
hypothesis-draft: [initial hypothesis]
self-test:        [Could you have written this from the deviation line alone? YES -- rewrite. NO -- proceed.]
mechanism-type:   [token from taxonomy, or TAXONOMY-GAP]
mechanism:        [final hypothesis after self-test]
connector-impact: [what silently fails or degrades]
recommendation:   [amend-spec | fix-impl | needs-discussion]
```

**COSMETIC FINDING**
```
Finding F-NN [COSMETIC]
deviation:        expected [X]; actual [Y]
spec:             [specific clause]
hypothesis-draft: [initial hypothesis]
self-test:        [Could you have written this from the deviation line alone? YES -- rewrite. NO -- proceed.]
mechanism-type:   [token from taxonomy, or TAXONOMY-GAP]
mechanism:        [final hypothesis after self-test]
```

After the last finding block, write the post-findings closure token:

```
[FINDINGS-RESOLVED | gate-clauses:{N from EXPECTED-SEALED} | clauses-resolved:{M} | phase:5-complete]
```

If `gate-clauses != clauses-resolved`: write `CLAUSE-GAP -- unaccounted clause IDs: [list]` and resolve before continuing.

---

### Step 6 -- Summary

Write a `## Summary` section:

```
| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

Verdict: Contract violated / Contract satisfied

Recommendations:
[F-NN: amend-spec / fix-impl / needs-discussion -- rationale -- one line per breaking/degraded finding]

Coverage: {N} / {total in Expected Output} clauses verified, {N} deviations found

mechanism-distribution: [type]:[count] [type]:[count] ...
```

**`mechanism-distribution:` fill instruction**: Enumerate every `mechanism-type:` field value across all finding blocks in S5. Count occurrences per type token. Write as space-separated type:count pairs, omitting zero-occurrence types. Example: `mechanism-distribution: conditional-branch:2 field-mapping:1`. If zero findings: `mechanism-distribution: none`. This line is enumerated from S5, not estimated.

---

### Step 7 -- Patterns (Phase 4 -- Connectors Contract Expert)

You are the Connectors contract expert. You resume after Automate has written the post-findings closure token.

Write the `## Patterns` section. Count distinct root cause groups. Apply exactly one branch template. **This section may not be silently omitted.**

For each group, you determine whether findings share a single mechanism type. This is a required expert judgment:
- Same-class (`mechanism-type-shared: field-mapping`) -- the defect is systemic in one mechanism; one spec or implementation change resolves the group
- Mixed-class (`mechanism-type-shared: mixed`) -- findings have coincident but independent root causes; each requires a separate fix

**Branch: Zero (apply when: total findings = 0, OR no two findings share a root cause)**

```
## Patterns
no-pattern-confirmation: [confirm no deviations or each finding is independent]
```

**Branch: Singleton (apply when: exactly one root cause group with two or more findings)**

```
## Patterns
single-finding-ref:    [finding IDs]
root-cause:            [shared causal mechanism]
mechanism-type-shared: [single type token if all findings share one class; "mixed" if they span classes -- REQUIRED]
fix-strategy:          [same-class: one fix resolves all | mixed: enumerate per-finding fixes]
attribution:
  - F-NN: [how this finding follows from the shared root cause]
  - F-NN: [how this finding follows from the shared root cause]
single-fix:            [resolution if same-class; "see fix-strategy" if mixed]
```

**Branch: Multi-pattern (apply when: two or more distinct root cause groups)**

```
## Patterns
pattern-1:
  root-cause:           [shared causal mechanism]
  mechanism-type-shared: [single type token or "mixed" -- REQUIRED]
  fix-strategy:         [same-class: one fix | mixed: independent fixes]
  findings:             [F-NN, F-MM]
  single-fix:           [resolution]
pattern-2:
  root-cause:           [shared causal mechanism]
  mechanism-type-shared: [single type token or "mixed" -- REQUIRED]
  fix-strategy:         [same-class: one fix | mixed: independent fixes]
  findings:             [F-PP, F-QQ]
  single-fix:           [resolution]
[repeat pattern-N block for each additional group]
patterns-summary: {N} patterns identified covering {M} of {total} findings
```

`mechanism-type-shared:` is required in every non-zero branch. It is the Connectors contract expert's determination, not an optional annotation.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 -- Full R10 Ceiling: Role Sequence x Output Format x Lifecycle Emphasis + R9 Platinum Base (C-29 x C-30 + C-01--C-28)

**axes:** role-sequence x output-format x lifecycle-emphasis (plus R9 V-05 platinum base)
**hypothesis:** The two new R10 criteria operate on orthogonal structural layers -- C-29 on the Patterns synthesis semantics, C-30 on the Summary aggregate format. Both are escalations from C-28 (per-finding mechanism-type token) and both require the author to do something with the type tokens that R9 V-05 did not require. C-29 requires recognizing when grouped findings share a class vs span classes and making that determination a named required field. C-30 requires enumerating type tokens across all findings and computing a compact cross-session-comparable aggregate. All three axes are layered onto the R9 V-05 platinum base via skeleton pre-declaration: (1) role-sequence framing makes `mechanism-type-shared:` a required expert judgment in Phase 4; (2) output-format upgrade makes `mechanism-distribution:` a computed compact aggregate in Summary; (3) lifecycle-emphasis Taxonomy Synthesis step (Step 5.5) creates a named transition between findings and closure where both computations are performed before the gate is closed. Two new behavioral protocol invariants extend the R9 V-05 ten-point protocol: the C-29 invariant (mechanism-type-shared is unconditional in every non-zero Patterns branch) and the C-30 invariant (mechanism-distribution is enumerated from S5 finding blocks, not from a template). The regression hypothesis: the two new invariants add slot-filling and computation obligations without changing role boundaries, phase sequence, or essential coverage requirements. The skeleton pre-declares all upgraded positions so no new obligation is introduced under write-time cognitive pressure.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state -- inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### Behavioral Protocol (Pre-Phase-1)

Commit to these structural rules before any phase begins:

1. **Skeleton immutability**: All section headers, template slots, token formats, finding templates with self-test and taxonomy fields, post-findings closure token, Taxonomy Synthesis step, Patterns branch templates with `mechanism-type-shared:` slots, and Summary `mechanism-distribution:` slot are declared in the skeleton below. No section may be added, removed, or reordered after the skeleton is written.
2. **Phase-separation invariant**: Expected output (Phase 1) must be complete and the gate token placed before any operation is run or observed. The gate token commits the clause count as a sealed value.
3. **Role-boundary rule**: The Connectors contract expert does not run or simulate the operation. Automate does not modify S2. Role authority is unconditional within each phase. The Connectors contract expert owns Phase 4 (Patterns synthesis) as the domain authority on mechanism class alignment.
4. **Coverage obligation**: Every element in S2 must appear in S4. A missing element is a silent omission -- the trace fails C-02 regardless of finding quality.
5. **Gate manifest invariant**: The opening gate token carries `clauses:N` and one identity field. The post-findings closure token echoes the count. Any divergence between `gate-clauses` and `clauses-resolved` signals an orphaned clause and must be resolved with a `CLAUSE-GAP` signal before S5.5 proceeds.
6. **Tier-stratified template invariant**: Use the template matching the severity of each finding. All fields within each template are unconditionally required.
7. **Self-test invariant**: Every `hypothesis-draft:` must pass the necessary-information self-test before `mechanism-type:` and `mechanism:` are filled. A finding with `hypothesis-draft:` only is incomplete.
8. **Taxonomy invariant**: Every finding must carry a `mechanism-type:` token selected from the five-item enumeration before the `mechanism:` prose. Free-text without a preceding type token is a structural violation.
9. **Post-findings closure invariant**: The `[FINDINGS-RESOLVED ...]` token must appear immediately after the last finding block and after S5.5 is complete, before S6. `clauses-resolved:M` must equal `gate-clauses:N` or produce a `CLAUSE-GAP` signal.
10. **Patterns non-omission**: S7 may not be silently omitted for any finding count. Apply the matching branch template from the skeleton unconditionally. All pre-printed slots in the applied branch must be filled.
11. **C-29 invariant**: `mechanism-type-shared:` is unconditionally required in every non-zero Patterns branch (Singleton and Multi-pattern). Writing "N/A", leaving the slot blank, or omitting it is a structural violation. "If applicable" does not apply.
12. **C-30 invariant**: `mechanism-distribution:` in S6 is enumerated from S5 finding blocks by the Taxonomy Synthesis step (S5.5). It is not a template to fill with estimates or placeholders. A distribution line with `?` values, pipe-delimited format, or a verbose label fails.

---

### Mechanism Taxonomy

Five named type tokens. Select exactly one per finding in the `mechanism-type:` field.

| Token | Applies when |
|-------|--------------|
| `field-mapping` | Mapping rule fails to correctly translate source field to target field (absent, misnamed, wrong value) |
| `serialization-path` | Value present internally but lost, truncated, or transformed during serialization (JSON encode, XML schema, wire format) |
| `conditional-branch` | Wrong code branch executes on a condition (null check, enum comparison, flag test) for this input |
| `lifecycle-event` | Expected event at a lifecycle stage (auth refresh, pagination close, error teardown) did not fire or fired out of sequence |
| `schema-contract` | Schema-level agreement (required field, type constraint, cardinality, version negotiation) not honored by implementation |

If none fits: `mechanism-type: TAXONOMY-GAP` + one-sentence explanation. Flagged for taxonomy extension review.

---

Before Phase 1 begins, write the following artifact skeleton. Every section header, template slot, token format, finding template, post-findings closure token, Taxonomy Synthesis step, and Patterns branch template appears below in its final position.

```
## Artifact Skeleton -- {topic}-contract-{date}.md

## 1. Contract Scope
- Operation: [fill -- Phase 1]
- Connector / Automate context: [fill -- Phase 1]
- Input fixture (inline): [fill -- Phase 1]
- Spec version and section: [fill -- Phase 1]

## 2. Expected Output (Phase 1 -- Connectors Contract Expert)

### Success Path
| Element | Spec Clause |
|---------|-------------|
| [fill]  | [fill]      |

### Error Path
| Element | Spec Clause |
|---------|-------------|
| [fill]  | [fill]      |

### Edge Case: [name -- fill Phase 1]
| Element | Spec Clause |
|---------|-------------|
| [fill]  | [fill]      |

[EXPECTED-SEALED | clauses:{N} | date:{YYYY-MM-DD} | author:contract-expert | phase:1-complete]

## 3. Actual Output (Phase 2 -- Automate)
- Status code: [fill]
- Response body: [fill]
- Headers: [fill]
- Observable side effects: [fill]

## 4. Diff
| Element | Result |
|---------|--------|
| [element from S2] | satisfied / F-NN deviation |

## 5. Findings

--- BREAKING FINDING TEMPLATE (9 unconditional fields) ---

Finding F-NN [BREAKING]
deviation:        expected [X]; actual [Y]
spec:             [specific clause from S2 -- rule number, named constraint, or sub-clause path; not a section heading alone]
hypothesis-draft: [write your initial hypothesis here]
self-test:        [Could you have written this from the deviation line alone, without knowing the system? YES -- symptom restatement; rewrite naming the internal mechanism. NO -- mechanism; proceed.]
mechanism-type:   [select one: field-mapping | serialization-path | conditional-branch | lifecycle-event | schema-contract -- or TAXONOMY-GAP + explanation]
mechanism:        [final hypothesis after self-test -- names the internal process, mapping, serialization path, or code condition; must be consistent with mechanism-type]
connector-impact: [what breaks for Automate flows or Connector integrations relying on this field/behavior]
recommendation:   [amend-spec | fix-impl | needs-discussion]
rationale:        [one sentence: which side of the contract is wrong and why, grounded in the mechanism]

--- DEGRADED FINDING TEMPLATE (8 unconditional fields) ---

Finding F-NN [DEGRADED]
deviation:        expected [X]; actual [Y]
spec:             [specific clause from S2]
hypothesis-draft: [write your initial hypothesis here]
self-test:        [Could you have written this from the deviation line alone? YES -- rewrite. NO -- proceed.]
mechanism-type:   [select one token from taxonomy, or TAXONOMY-GAP]
mechanism:        [final hypothesis after self-test]
connector-impact: [what silently fails or degrades for Automate flows or Connector integrations]
recommendation:   [amend-spec | fix-impl | needs-discussion]

--- COSMETIC FINDING TEMPLATE (7 unconditional fields) ---

Finding F-NN [COSMETIC]
deviation:        expected [X]; actual [Y]
spec:             [specific clause from S2]
hypothesis-draft: [write your initial hypothesis here]
self-test:        [Could you have written this from the deviation line alone? YES -- rewrite. NO -- proceed.]
mechanism-type:   [select one token from taxonomy, or TAXONOMY-GAP]
mechanism:        [final hypothesis after self-test]
connector-impact: [Automate / Connector integration impact -- write "none" if not applicable; field always present]

## 5.5. Taxonomy Synthesis (required -- complete before closure token)

Sub-task A -- Mechanism-Distribution Census:
Walk through every finding block in S5. Tally mechanism-type tokens per type.
mechanism-distribution: [type]:[count] [type]:[count] ...
(Omit zero-occurrence types. If zero findings: mechanism-distribution: none.)

Sub-task B -- Group Type Alignment:
For each candidate Patterns group (two or more findings sharing a root cause):
group-candidate-N: findings=[F-NN, F-MM] mechanism-type-shared=[single type token; or "mixed"]

[FINDINGS-RESOLVED | gate-clauses:{N from EXPECTED-SEALED} | clauses-resolved:{M} | phase:5-complete]

## 6. Summary
| Severity | Count |
|----------|-------|
| breaking | ?     |
| degraded | ?     |
| cosmetic | ?     |
| total    | ?     |

Verdict: [Contract violated / Contract satisfied]

Recommendations:
- F-NN: [amend-spec / fix-impl / needs-discussion] -- [rationale]

Coverage: ? / ? clauses verified, ? deviations found

mechanism-distribution: [copy verbatim from S5.5 Sub-task A]

## 7. Patterns (Phase 4 -- Connectors Contract Expert)

--- BRANCH: ZERO PATTERNS ---
Apply when: total findings = 0, OR no two findings share a root cause.
no-pattern-confirmation: [confirm (a) no deviations found, or (b) each finding is independent with no cross-finding patterns]

--- BRANCH: SINGLETON ---
Apply when: exactly one root cause group containing two or more findings exists, and no other groups exist.
single-finding-ref:    [finding IDs in this group]
root-cause:            [the shared causal mechanism]
mechanism-type-shared: [copy from S5.5 Sub-task B -- single type token or "mixed" -- REQUIRED; same-class signals systemic root cause one fix; mixed signals coincident symptoms independent fixes]
fix-strategy:          [same-class: one fix resolves all findings | mixed: enumerate per-finding fixes]
attribution:
  - F-NN: [one sentence: how this finding follows from the shared root cause]
  - F-NN: [one sentence: how this finding follows from the shared root cause]
single-fix:            [resolution if same-class; "see fix-strategy" if mixed]

--- BRANCH: MULTI-PATTERN ---
Apply when: two or more distinct root cause groups, each with two or more findings.
pattern-1:
  root-cause:           [shared causal mechanism]
  mechanism-type-shared: [copy from S5.5 Sub-task B -- single type token or "mixed" -- REQUIRED; same-class: one fix; mixed: independent fixes]
  fix-strategy:         [same-class: one fix | mixed: independent fixes]
  findings:             [F-NN, F-MM]
  single-fix:           [resolution if same-class; "see fix-strategy" if mixed]
pattern-2:
  root-cause:           [shared causal mechanism]
  mechanism-type-shared: [copy from S5.5 Sub-task B -- single type token or "mixed" -- REQUIRED]
  fix-strategy:         [same-class: one fix | mixed: independent fixes]
  findings:             [F-PP, F-QQ]
  single-fix:           [resolution]
[repeat pattern-N block for each additional group]
patterns-summary: {N} patterns identified covering {M} of {total} findings
```

The skeleton commits the complete document structure, all three severity-tier templates (with self-test, taxonomy, and connector-impact slots), the Taxonomy Synthesis step (S5.5) with both sub-tasks, the post-findings closure token positioned after S5.5, the upgraded Summary `mechanism-distribution:` slot, and all three Patterns branch templates with `mechanism-type-shared:` and `fix-strategy:` slots marked REQUIRED. Every structural obligation is unconditional and visible before Phase 1 begins.

---

### Phase 1 -- Connectors Contract Expert: Expected Output

You are the Connectors contract expert. You have not run the operation. You have not observed implementation output. You write from the spec alone. Your role is active during Phase 1 and resumes for Phase 4 (Patterns synthesis).

**Fill S1 -- Contract Scope.** Replace all `[fill -- Phase 1]` slots: operation name and HTTP method; connector or Automate context and environment; input fixture (inline, no file references); spec version and section.

**Fill S2 -- Expected Output.** Three surface blocks are required:
- Success path: every field, value, type, and ordering guarantee the spec promises for nominal input
- Error path: every error code, message format, and header the spec promises for invalid or missing input
- Edge case: at least one scenario (empty collection, null required field, rate-limit, auth expiry)

For each expected element, cite the specific clause (rule number, named constraint, or sub-clause path -- not a section heading alone). An expected element without a spec citation is not a valid contract entry. If a surface is not defined in the spec, write: `[surface]: not specified in spec`.

Count the distinct expected elements. When Expected Output is complete and every element carries a spec citation, replace the `[EXPECTED-SEALED ...]` slot with:

```
[EXPECTED-SEALED | clauses:{N} | date:{YYYY-MM-DD} | author:contract-expert | phase:1-complete]
```

Where `{N}` is the element count and `{YYYY-MM-DD}` is today's date. Do not run or simulate the operation before placing this token. Your role is suspended after this token; Automate begins.

---

### Phase 2 -- Automate: Execute, Diff, Findings, and Taxonomy Synthesis

You begin after the `[EXPECTED-SEALED ...]` token. Do not modify S2. Any belief that an Expected entry is incorrect is a finding -- record it in S5, do not edit.

**Fill S3 -- Actual Output.** Run or simulate the operation. Record the full response: status code, response body, headers, all observable side effects.

**Fill S4 -- Diff.** For every element row in S2, write its result:
- `pass -- {element} -- satisfied`, or
- `F-NN -- {element} -- deviation (see S5)`

Every element must appear. Missing elements fail C-02 regardless of finding quality.

If no deviations: replace S5 with `## 5. Findings -- none. Contract satisfied.` Fill S5.5 as `mechanism-distribution: none` with no group candidates. Write the post-findings closure token with both counts equal to gate-clauses. Fill S6 all-zero. Fill S7 using the Zero branch template.

**Fill S5 -- Findings.** For each deviation from S4, select the matching severity tier template and fill all fields. Hypothesis protocol: `hypothesis-draft:` first, then `self-test:`, then `mechanism-type:` from the taxonomy, then `mechanism:` consistent with the type token. All fields unconditional.

**Fill S5.5 -- Taxonomy Synthesis (required before closure token).**

Sub-task A: Walk through every finding block in S5. Read each `mechanism-type:` field. Tally per type. Replace the `mechanism-distribution:` placeholder with the computed aggregate.

Sub-task B: For each candidate Patterns group you intend to create in S7, identify the `mechanism-type:` tokens of the findings in that group. Determine single class or mixed. Fill each `group-candidate-N:` line.

**Write the post-findings closure token after S5.5.** Replace the `[FINDINGS-RESOLVED ...]` slot:
- `gate-clauses:` = `clauses:` value from `[EXPECTED-SEALED]`
- `clauses-resolved:` = count of expected elements that either passed in S4 or have a finding filed in S5
- If `gate-clauses != clauses-resolved`: write `CLAUSE-GAP -- unaccounted clause IDs: [list]` and resolve before S6.

**Fill S6 -- Summary.** Replace every `?` with actual values. Copy `mechanism-distribution:` verbatim from S5.5 Sub-task A.

---

### Phase 4 -- Connectors Contract Expert: Patterns Synthesis

You resume after Automate has completed S6. Write `## Patterns` (Step 7) using the skeleton.

Apply exactly one branch template based on the finding count and grouping structure. Fill all pre-printed slots in the applied branch. Delete inapplicable branches.

`mechanism-type-shared:` is required in every non-zero branch. Copy from S5.5 Sub-task B. This is your expert determination of mechanism class alignment for the group:
- Single class token (e.g., `field-mapping`) -- findings share a systemic root cause; one spec or implementation change should resolve the group
- `mixed` -- findings have coincident but independent mechanism types; they require separate fixes; enumerate per-finding resolutions in `fix-strategy:`

Do not silently omit `mechanism-type-shared:`. Do not write "if applicable." It is unconditional.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## Scorecard Reference

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-29: `mechanism-type-shared:` required with fix-strategy semantics | PASS | FAIL | PASS | PASS | PASS |
| C-30: `mechanism-distribution:` compact computed aggregate | FAIL | PASS | PASS | PASS | PASS |
| C-28: mechanism taxonomy (R9 inherited) | PASS | PASS | PASS | PASS | PASS |
| C-26: post-findings closure token (R9 inherited) | PASS | PASS | PASS | PASS | PASS |
| C-27: branch template slots (R9 inherited) | PASS | PASS | PASS | PASS | PASS |
| C-23--C-25: gate manifest, multi-branch, self-test (R8 inherited) | PASS | PASS | PASS | PASS | PASS |

**Predicted composite scores (rubric v10):**
- V-01: C-29 PASS, C-30 FAIL -> 29/30 criteria -> ceiling under role-sequence isolation
- V-02: C-29 FAIL, C-30 PASS -> 29/30 criteria -> ceiling under output-format isolation
- V-03: C-29 PASS, C-30 PASS -> 30/30 criteria -> ceiling under lifecycle-emphasis via taxonomy census
- V-04: C-29 PASS, C-30 PASS -> 30/30 criteria -> ceiling under role-sequence x output-format
- V-05: C-29 PASS, C-30 PASS -> 30/30 criteria -> **new ceiling, all criteria satisfied via skeleton pre-declaration**

V-01 and V-02 tie under isolation. V-03 cracks both via the taxonomy census step -- a single lifecycle mechanism that forces both computations before the gate closes. V-04 cracks both via two independent structural changes at two different section positions. V-05 is the canonical ceiling: skeleton pre-declaration of all upgraded positions with two new behavioral protocol invariants, making no obligation dependent on write-time memory.
