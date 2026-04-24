# trace-contract Variate -- Round 9 (rubric v9)

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v9 (C-01--C-28; essential C-01--C-05; max composite 110; golden threshold: all essential pass + composite >= 80)
**Round:** R9 -- targeting C-26, C-27, C-28 in isolation (V-01 through V-03), then in combination (V-04, V-05)

---

## Round 9 Context

R8 best score: V-05 at 107/107 (full platinum). Three new R9 points are C-26, C-27, C-28.

The three new criteria operate on orthogonal structural layers:
- **C-26** -- phase-lifecycle layer: a matched closure token placed immediately after the findings section echoes `gate-clauses:N` and adds `clauses-resolved:M`, enabling clause-count verification before the summary is written
- **C-27** -- synthesis-slot layer: each Patterns branch carries pre-printed structural slots (`no-pattern-confirmation:`, `single-finding-ref:` + `root-cause:`, `pattern-N: root-cause: findings:[]`) that enforce field completion within the branch at write time rather than relying on branch instructions
- **C-28** -- vocabulary layer: a mechanism taxonomy with five named type tokens constrains the first declaration of every mechanism hypothesis, preventing free-text drift and enabling cross-finding pattern recognition by type

The three layers are orthogonal:
- C-26 operates on lifecycle position (when the gate closes relative to the findings section)
- C-27 operates on template shape (what pre-printed fields exist inside each Patterns branch)
- C-28 operates on field vocabulary (what terms are allowed in the mechanism type slot)

---

## Round 9 Variation Map

| Variation | Axis | Primary Targets | Hypothesis |
|-----------|------|-----------------|------------|
| V-01 | lifecycle-emphasis (C-26 isolation) | C-26 | R8 V-01 places `[TRACE-COMPLETE]` at Summary close. C-26 requires an additional closure token immediately after the findings section -- before the Summary -- echoing the committed clause count and adding `clauses-resolved:M`. Isolation tests whether adding this post-findings closure token can be achieved without structural overhead while preserving the R8 gate manifest (C-23) base |
| V-02 | output-format (C-27 isolation) | C-27 | R8 V-02 satisfies C-24 (per-branch instructions for zero/singleton/multi) but not C-27 (no pre-printed structural slots within each branch). C-27 escalates from instructions to template slots: each branch has labeled fields to fill rather than instructions to follow. Isolation tests whether adding pre-printed slots inside the existing branch structure reliably enforces field completion |
| V-03 | phrasing-register (C-28 isolation) | C-28 | R8 V-03 satisfies C-25 (self-test procedure) but every mechanism field uses free-text. C-28 escalates: a mechanism type token from a five-item enumeration must precede the mechanism statement, converting unconstrained prose into a type-prefixed declaration. Isolation tests whether embedding the taxonomy in the finding template alongside the self-test produces consistent type-token usage without essential criterion regression |
| V-04 | lifecycle-emphasis x output-format (C-26 x C-27) | C-26, C-27 | C-26 (post-findings closure) and C-27 (branch template slots) operate on different sections. Combination tests whether pre-declaring both in the artifact skeleton produces additive coverage without regression, building on R8 V-04 (C-23 x C-24) |
| V-05 | lifecycle-emphasis x output-format x phrasing-register (C-26 x C-27 x C-28 + R8 platinum base) | C-26, C-27, C-28, C-23, C-24, C-25, C-22, C-16, C-14, C-13 | Full R9 ceiling. Three new criteria layered onto the R8 V-05 platinum base (all 25 prior criteria). Tests whether all 28 criteria can be simultaneously targeted via skeleton pre-declaration without cognitive overhead that regresses C-01 through C-05 |

---

## V-01 -- Lifecycle Emphasis: Post-Findings Closure Token (C-26 isolation)

**axis:** lifecycle-emphasis
**hypothesis:** R8 V-01 achieves C-23 (gate manifest: `clauses:N` + identity fields in the opening token) and carries a closure token in S6 as `[TRACE-COMPLETE | ... | gate-clauses:N]`. C-26 escalates: a second matched closure token must be placed immediately after the findings section -- before the Summary -- that echoes `gate-clauses:N` from the opening gate and adds `clauses-resolved:M` where M is the count of expected clauses that were either passed with no finding or had a finding filed against them. The position matters: placing the resolution token at S5-close rather than S6-close means the clause-resolution count is established before the summary is computed, enabling the summary to verify against it rather than recount from scratch. The `clauses-resolved` field enables automated verification that no committed clause was orphaned -- every clause either passed or has a finding, and the gate count and resolved count must agree. This variation isolates C-26 as the sole axis change from the R8 V-01 base, adding only the post-findings closure token and the `clauses-resolved` count mechanism.

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

### Step 2 -- Expected Output (Phase 1 -- from spec only)

**Role**: You are the Connectors contract expert. You have not run the operation. You have not observed implementation output. You write from the spec alone. Your role ends when the gate token is placed.

Write the `## Expected Output` section. Cover all three contract surfaces:
- **Success path** -- nominal input, nominal output per spec
- **Error path** -- invalid or missing input, expected error response per spec
- **At least one edge case** -- empty collection, null required field, rate-limit trigger, auth expiry

For each expected element, cite the specific clause from the spec that requires it (rule number, named constraint, or sub-clause path -- not a section heading alone). An expected element without a spec citation is not a valid contract entry. If a surface is not defined in the spec, write: `[surface]: not specified in spec`.

When Expected Output is complete and every element carries a spec citation, count the number of distinct expected elements. Write the phase gate token on its own line immediately after the last expected element:

```
[EXPECTED-SEALED | clauses:{N} | date:{YYYY-MM-DD} | author:contract-expert | phase:1-complete]
```

Replace `{N}` with the exact element count. Replace `{YYYY-MM-DD}` with today's date. The token must appear exactly once. Do not run or simulate the operation before writing this token.

---

### Step 3 -- Actual Output

**Role**: You are Automate. You begin after the `[EXPECTED-SEALED ...]` token. Do not modify the Expected Output section. Any belief that an Expected entry is incorrect is a finding -- record it in Step 5; do not edit.

Run or simulate the operation. Write the `## Actual Output` section: status code, response body, headers, observable side effects.

---

### Step 4 -- Diff

Write the `## Diff` section. For every element in `## Expected Output`:
- `pass -- {element} -- satisfied`, or
- `F-NN -- {element} -- deviation (see findings)`

Every element must appear. Elements present in Expected Output but absent from the Diff are silent omissions -- the trace fails C-02 regardless of finding quality.

If no deviations: write `## Diff -- Contract satisfied. No findings.` and skip to Step 6.

---

### Step 5 -- Findings

For each deviation, write a finding entry using the appropriate severity-tier template:

**BREAKING FINDING**
```
Finding F-NN [BREAKING]
deviation:        expected [X]; actual [Y]
spec:             [specific clause from Expected Output -- rule number, named constraint, or sub-clause path]
hypothesis:       [the causal mechanism -- name the internal process, mapping, serialization path, or condition that produced the wrong output; not a restatement of what differed]
connector-impact: [what breaks for Automate flows or Connector integrations relying on this field/behavior]
recommendation:   [amend-spec | fix-impl | needs-discussion]
rationale:        [one sentence: which side of the contract is wrong and why, grounded in the hypothesis]
```

**DEGRADED FINDING**
```
Finding F-NN [DEGRADED]
deviation:        expected [X]; actual [Y]
spec:             [specific clause]
hypothesis:       [the causal mechanism -- name the internal process, mapping, serialization path, or condition]
connector-impact: [what silently fails or degrades for Automate flows or Connector integrations]
recommendation:   [amend-spec | fix-impl | needs-discussion]
```

**COSMETIC FINDING**
```
Finding F-NN [COSMETIC]
deviation:  expected [X]; actual [Y]
spec:       [specific clause]
hypothesis: [the causal mechanism -- name the internal process, mapping, serialization path, or condition]
```

Hypothesis rule (all tiers): The hypothesis names a causal mechanism -- it does not restate the deviation. If your hypothesis could be written without knowing anything about the system under test -- only from reading the deviation line -- it is a symptom restatement, not a mechanism.

**After the last finding block**, write the post-findings closure token on its own line:

```
[FINDINGS-RESOLVED | gate-clauses:{N} | clauses-resolved:{M} | phase:5-complete]
```

- `gate-clauses:{N}` must echo the `clauses:` value from the `[EXPECTED-SEALED ...]` token
- `clauses-resolved:{M}` = count of expected elements that were either: (a) marked `pass` in the Diff, OR (b) referenced by a filed finding. Every expected clause must appear in exactly one of these two categories.
- If `gate-clauses != clauses-resolved`: write `CLAUSE-GAP -- gate-clauses:{N} resolved:{M} -- unaccounted clause IDs: [list]` and investigate before proceeding.

This token appears once, immediately after the last finding block, before the Summary section.

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
```

---

### Step 7 -- Patterns

Write a `## Patterns` section.

If two or more findings share a root cause, group them, name the shared mechanism, list the finding IDs, and state the single fix that would resolve all findings in the group.

If no findings share a root cause (or if there are zero or one findings), write: `No cross-finding patterns detected.`

This section may not be silently omitted regardless of finding count.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 -- Output Format: Branch-Conditional Patterns Template Slots (C-27 isolation)

**axis:** output-format
**hypothesis:** R8 V-02 satisfies C-24 by providing explicit branch instructions for all three cardinality cases: zero patterns requires an affirmative confirmation statement; singleton requires per-finding attribution explaining how each finding follows from the shared mechanism; multi-pattern requires per-group sections with a single-fix claim. C-27 escalates from instructions to structural slots: each branch carries pre-printed labeled fields that must be filled, not descriptions of what to write. The zero branch carries `no-pattern-confirmation:` as a labeled slot -- the model must fill it, not decide whether to include it. The singleton branch carries `single-finding-ref:` and `root-cause:` as separate labeled slots -- root-cause is separated from the finding reference, preventing conflation. The multi-branch carries `pattern-N: root-cause: findings:[]` as pre-printed structure -- the model repeats the pattern block for each group. The shift from instruction to slot converts a procedural guide into a structural template: filling labeled fields is more reliable under write-time cognitive pressure than following branching instructions. This variation isolates C-27 as the sole axis change from the R8 V-02 base.

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

### Step 2 -- Expected Output (Phase 1 -- from spec only)

**Role**: You are the Connectors contract expert. You have not run the operation. You write from the spec alone. Your role ends when the gate token is placed.

Write the `## Expected Output` section. Cover all three contract surfaces:
- **Success path** -- nominal input, nominal output per spec
- **Error path** -- invalid or missing input, expected error response per spec
- **At least one edge case** -- empty collection, null required field, rate-limit trigger, auth expiry

For each expected element, cite the specific spec clause that requires it (rule number, named constraint, or sub-clause path -- not a section heading alone). An expected element without a spec citation is not a valid contract entry. If a surface is not in the spec, write: `[surface]: not specified in spec`.

When Expected Output is complete, write: `[CONTRACT COMMITTED]`

Do not proceed to Step 3 before writing this line.

---

### Step 3 -- Actual Output

**Role**: You are Automate. You begin after `[CONTRACT COMMITTED]`. Do not modify the Expected Output section.

Run or simulate the operation. Write the `## Actual Output` section: status code, response body, headers, observable side effects.

---

### Step 4 -- Diff

Write the `## Diff` section. For every element in `## Expected Output`:
- `pass -- {element} -- satisfied`, or
- `F-NN -- {element} -- deviation (see findings)`

Every element must appear. Elements present in Expected Output but absent from the Diff are silent omissions -- the trace fails C-02 regardless of finding quality.

If no deviations: write `## Diff -- Contract satisfied. No findings.` and skip to Step 6.

---

### Step 5 -- Findings

For each deviation:

**BREAKING FINDING**
```
Finding F-NN [BREAKING]
deviation:        expected [X]; actual [Y]
spec:             [specific clause -- rule number, named constraint, or sub-clause path]
hypothesis:       [the mechanism -- name the process, mapping, serialization path, or condition that caused this; not a restatement of what differed]
connector-impact: [what breaks for Automate flows or Connector integrations relying on this]
recommendation:   [amend-spec | fix-impl | needs-discussion]
rationale:        [one sentence: which side of the contract is wrong and why]
```

**DEGRADED FINDING**
```
Finding F-NN [DEGRADED]
deviation:        expected [X]; actual [Y]
spec:             [specific clause]
hypothesis:       [the mechanism -- name the process, mapping, serialization path, or condition]
connector-impact: [what silently fails or degrades for Automate flows or Connector integrations]
recommendation:   [amend-spec | fix-impl | needs-discussion]
```

**COSMETIC FINDING**
```
Finding F-NN [COSMETIC]
deviation:  expected [X]; actual [Y]
spec:       [specific clause]
hypothesis: [the mechanism -- name the process, mapping, serialization path, or condition]
```

Hypothesis rule: The hypothesis names a causal mechanism. It does not restate the deviation. If your hypothesis could be written from the deviation line alone without knowing anything about the system under test, it is a symptom restatement, not a mechanism. Rewrite it.

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
```

---

### Step 7 -- Patterns

Write a `## Patterns` section. Count distinct root cause groups across all findings. Apply exactly one of the three branch templates below. This section may not be silently omitted regardless of finding count.

**Branch: Zero (apply when: total findings = 0, OR no two findings share a root cause)**

```
## Patterns
no-pattern-confirmation: [write a statement confirming either (a) no deviations were found and the contract was fully satisfied, or (b) each finding has an independent root cause and no cross-finding patterns exist]
```

The `no-pattern-confirmation:` slot must be filled with a statement. A blank slot, a missing slot, or a section with only a heading does not satisfy this branch.

**Branch: Singleton (apply when: exactly one root cause group containing two or more findings exists, and no other groups exist)**

```
## Patterns
single-finding-ref: [list the finding IDs that belong to this group, e.g., F-01, F-03]
root-cause: [name the shared causal mechanism -- the internal process, mapping, or condition shared by all findings in this group]
attribution:
  - F-NN: [one sentence explaining how this specific finding follows from the shared root cause]
  - F-NN: [one sentence explaining how this specific finding follows from the shared root cause]
single-fix: [what change -- spec or implementation -- would resolve all findings in this group]
```

All slots are required. Writing only `single-finding-ref:` and `root-cause:` without `attribution:` lines does not satisfy the singleton branch.

**Branch: Multi-pattern (apply when: two or more distinct root cause groups, each with two or more findings)**

```
## Patterns
pattern-1:
  root-cause: [shared causal mechanism for this group]
  findings: [F-NN, F-MM]
  single-fix: [resolution for this group]
pattern-2:
  root-cause: [shared causal mechanism for this group]
  findings: [F-PP, F-QQ]
  single-fix: [resolution for this group]
[repeat pattern-N block for each additional group]
patterns-summary: {N} patterns identified covering {M} of {total} findings
```

Each `pattern-N` block carries three slots: `root-cause:`, `findings:[]`, and `single-fix:`. All three slots are required per block. The `patterns-summary:` slot closes the section with a count.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 -- Phrasing Register: Mechanism Taxonomy Constraint (C-28 isolation)

**axis:** phrasing-register
**hypothesis:** R8 V-03 satisfies C-25 (hypothesis self-test via the necessary-information condition) and produces mechanism fields that name internal processes, but the vocabulary is unconstrained -- the model may describe any mechanism in any terms. C-28 escalates: a vocabulary-constrained mechanism taxonomy with five named type tokens constrains what the mechanism field declares as its first assertion. Before elaborating in prose, the author must select a type token from the enumeration: `field-mapping`, `serialization-path`, `conditional-branch`, `lifecycle-event`, `schema-contract`. The type token is a required field that precedes the mechanism prose. The phrasing-register axis: the shift from free-text mechanism description to type-token-first declaration is a register change -- the finding's mechanism section moves from descriptive prose to structured type assertion followed by causal narrative. This makes the mechanism field parseable as a type class (enabling cross-finding grouping by mechanism class) while the prose retains the causal narrative. Isolation tests whether adding `mechanism-type:` as a required field before the mechanism prose produces consistent taxonomy coverage without regressing the self-test discipline (C-25) or the essential criteria.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state -- inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### Mechanism Taxonomy (Pre-Phase-1 Declaration)

Every finding hypothesis must begin with a mechanism type token selected from the following enumeration. The type token appears in the `mechanism-type:` field, which precedes the `mechanism:` prose field in every finding template.

| Type Token | Applies when |
|------------|--------------|
| `field-mapping` | A field is absent, misnamed, or assigned an incorrect value due to a mapping rule that failed to correctly translate the source field to the target field |
| `serialization-path` | A value is present in the internal model but lost, truncated, or transformed during serialization (JSON encode, XML schema, wire format conversion) |
| `conditional-branch` | A code path branches on a condition (null check, enum comparison, flag test) and the wrong branch executes, producing unexpected output for this input |
| `lifecycle-event` | The deviation occurs because an event expected at a specific lifecycle stage (connection init, auth refresh, pagination close, error teardown) did not fire or fired out of sequence |
| `schema-contract` | The deviation traces to a schema-level agreement (required field, type constraint, cardinality rule, version negotiation) that the implementation fails to honor |

If none of the five tokens accurately describes the mechanism: write `mechanism-type: TAXONOMY-GAP` and provide a one-sentence description of the gap. A `TAXONOMY-GAP` finding is flagged for taxonomy extension review.

The taxonomy is declared once here. Do not redeclare it within individual findings.

---

### Step 1 -- Contract Scope

Write a `## Contract Scope` section:
- Operation name and HTTP method (or equivalent)
- Connector or Automate context and environment
- Input fixture -- state inline; no external file references
- Spec version and section governing this operation's output contract

---

### Step 2 -- Expected Output (Phase 1 -- from spec only)

**Role**: You are the Connectors contract expert. You have not run the operation. You write from the spec alone. Your role ends when the gate token is placed.

Write the `## Expected Output` section. Cover all three contract surfaces:
- **Success path** -- nominal input, nominal output per spec
- **Error path** -- invalid or missing input, expected error response per spec
- **At least one edge case** -- empty collection, null required field, rate-limit trigger, auth expiry

For each expected element, cite the specific spec clause that requires it. An expected element without a spec citation is not a valid contract entry. If a surface is not in the spec, write: `[surface]: not specified in spec`.

When Expected Output is complete, write: `[CONTRACT COMMITTED]`

Do not proceed to Step 3 before writing this line.

---

### Step 3 -- Actual Output

**Role**: You are Automate. You begin after `[CONTRACT COMMITTED]`. Do not modify the Expected Output section.

Run or simulate the operation. Write the `## Actual Output` section: status code, response body, headers, observable side effects.

---

### Step 4 -- Diff

Write the `## Diff` section. For every element in `## Expected Output`:
- `pass -- {element} -- satisfied`, or
- `F-NN -- {element} -- deviation (see findings)`

Every element must appear. Elements present in Expected Output but absent from the Diff are silent omissions -- the trace fails C-02 regardless of finding quality.

If no deviations: write `## Diff -- Contract satisfied. No findings.` and skip to Step 6.

---

### Step 5 -- Findings

For each deviation, write a finding entry. The hypothesis block uses a three-field self-test and taxonomy protocol.

**BREAKING FINDING**
```
Finding F-NN [BREAKING]
deviation:        expected [X]; actual [Y]
spec:             [specific clause from Expected Output -- rule number, named constraint, or sub-clause path]
hypothesis-draft: [write your initial hypothesis here before applying the self-test]
self-test:        [Could you have written this hypothesis from the deviation line alone, without knowing anything about the system under test? YES -- symptom restatement; rewrite naming the internal mechanism. NO -- mechanism; proceed.]
mechanism-type:   [select one token: field-mapping | serialization-path | conditional-branch | lifecycle-event | schema-contract -- or write TAXONOMY-GAP + explanation]
mechanism:        [final hypothesis after self-test -- names the internal process, mapping, serialization path, or code condition; must be consistent with the mechanism-type token]
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
mechanism-type:   [select one token from the taxonomy, or TAXONOMY-GAP]
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
mechanism-type:   [select one token from the taxonomy, or TAXONOMY-GAP]
mechanism:        [final hypothesis after self-test]
```

**Hypothesis protocol (all tiers):**

1. Write `hypothesis-draft:` -- initial attempt at the causal mechanism.
2. Apply `self-test:` -- necessary-information condition: could this draft have been written by reading only `expected [X]; actual [Y]` with no knowledge of the system's internal architecture, code, or schema? YES: symptom restatement -- rewrite naming a specific internal component. NO: mechanism -- proceed.
3. Select `mechanism-type:` -- choose the token from the taxonomy declared above that best describes the class of failure. The type token must be consistent with the mechanism prose.
4. Write `mechanism:` -- the final hypothesis, consistent with the selected type token.

A finding block is complete only when all four hypothesis fields are filled. `mechanism-type:` and `mechanism:` fields depend on passing the self-test; a finding where `self-test:` is YES and `mechanism:` is unchanged is incomplete.

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

The taxonomy distribution line summarizes type token usage across all findings. It appears once in the Summary.

---

### Step 7 -- Patterns

Write a `## Patterns` section.

If two or more findings share a root cause, group them, name the shared mechanism, list the finding IDs, and state the single fix that would resolve all findings in the group. When grouping, note whether grouped findings share a `mechanism-type` token -- same-type groupings often indicate a single systemic fix.

If no findings share a root cause (or if there are zero or one findings), write: `No cross-finding patterns detected.`

This section may not be silently omitted regardless of finding count.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 -- Combination: Post-Findings Closure Token + Branch Template Slots (C-26 x C-27)

**axes:** lifecycle-emphasis x output-format
**hypothesis:** C-26 (post-findings closure token) and C-27 (branch template slots in Patterns) operate on different sections: C-26 on the S5/S6 boundary, C-27 on S7. Their combination is additive if both can be pre-declared in the artifact skeleton. Building on R8 V-04 (which already satisfies C-23 x C-24 via skeleton pre-declaration), this variation upgrades two skeleton sections: (1) adds the `[FINDINGS-RESOLVED ...]` token slot at the end of the S5 template area so the analyst sees its required form before writing any finding; (2) replaces the per-branch instruction text in S7 with pre-printed slot templates so each branch is a block with labeled fields to fill rather than instructions to execute. The interaction hypothesis: skeleton pre-declaration of both mechanisms makes the obligations visible simultaneously from document open -- the post-findings closure token and the Patterns template slots are structural commitments the analyst fills rather than obligations they remember. Neither mechanism helps the other's failure mode; their combination via skeleton is additive and should not regress C-23 or C-24 (which the skeleton already satisfies) nor affect C-25 (not targeted in this variation).

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

1. **Skeleton immutability**: All section headers, template slots, token formats, and Patterns branch template slots are declared in the skeleton below. No section may be added, removed, or reordered after the skeleton is written.
2. **Phase-separation invariant**: Expected output (Phase 1) must be complete and the gate token placed before any operation is run or observed. The gate token commits the clause count as a sealed value.
3. **Role-boundary rule**: The Connectors contract expert does not run or simulate the operation. Automate does not modify S2. Role authority is unconditional within each phase.
4. **Coverage obligation**: Every element in S2 must appear in S4. A missing element is a silent omission -- the trace fails C-02 regardless of finding quality.
5. **Gate manifest invariant**: The opening gate token carries `clauses:N` and one identity field. The post-findings closure token echoes the count and adds `clauses-resolved:M`. Any divergence signals an orphaned clause and must be resolved before S6 is filled.
6. **Patterns non-omission**: S7 may not be silently omitted for any finding count. Apply the matching branch template from the skeleton unconditionally. All pre-printed slots in the applied branch must be filled.

---

Before Phase 1 begins, write the following artifact skeleton. Every section header, template slot, token format, and Patterns branch template appears below in its final position.

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

## 3. Actual Output (Phase 2 -- Automate, after gate token)
- Status code: [fill]
- Response body: [fill]
- Headers: [fill]
- Observable side effects: [fill]

## 4. Diff
| Element | Result |
|---------|--------|
| [element from S2] | satisfied / F-NN deviation |

## 5. Findings

--- BREAKING FINDING TEMPLATE ---

Finding F-NN [BREAKING]
deviation:        expected [X]; actual [Y]
spec:             [specific clause from S2 -- rule number, named constraint, or sub-clause path]
hypothesis:       [the causal mechanism -- name the internal process, mapping, serialization path, or condition; not a restatement of what differed]
connector-impact: [what breaks for Automate flows or Connector integrations]
recommendation:   [amend-spec | fix-impl | needs-discussion]
rationale:        [one sentence: which side of the contract is wrong and why]

--- DEGRADED FINDING TEMPLATE ---

Finding F-NN [DEGRADED]
deviation:        expected [X]; actual [Y]
spec:             [specific clause from S2]
hypothesis:       [the causal mechanism]
connector-impact: [what silently fails or degrades]
recommendation:   [amend-spec | fix-impl | needs-discussion]

--- COSMETIC FINDING TEMPLATE ---

Finding F-NN [COSMETIC]
deviation:  expected [X]; actual [Y]
spec:       [specific clause from S2]
hypothesis: [the causal mechanism]

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

## 7. Patterns

--- BRANCH: ZERO PATTERNS ---
Apply when: total findings = 0, OR no two findings share a root cause.
no-pattern-confirmation: [write a statement confirming either (a) no deviations were found and the contract was fully satisfied, or (b) each finding has an independent root cause and no cross-finding pattern exists]

--- BRANCH: SINGLETON ---
Apply when: exactly one root cause group containing two or more findings exists, and no other groups exist.
single-finding-ref: [finding IDs in this group, e.g., F-01, F-03]
root-cause: [the shared causal mechanism -- the internal process or condition common to all findings in this group]
attribution:
  - F-NN: [one sentence: how this finding follows from the shared root cause]
  - F-NN: [one sentence: how this finding follows from the shared root cause]
single-fix: [what change -- spec or implementation -- would resolve all findings in this group]

--- BRANCH: MULTI-PATTERN ---
Apply when: two or more distinct root cause groups, each with two or more findings.
pattern-1:
  root-cause: [shared causal mechanism for this group]
  findings: [F-NN, F-MM]
  single-fix: [resolution for this group]
pattern-2:
  root-cause: [shared causal mechanism for this group]
  findings: [F-PP, F-QQ]
  single-fix: [resolution for this group]
[repeat pattern-N block for each additional group]
patterns-summary: {N} patterns identified covering {M} of {total} findings
```

The skeleton commits the complete document structure, all finding templates, both structured tokens (opening gate + post-findings closure), and all three Patterns branch templates with pre-printed slots. Apply the branch in S7 that matches the actual finding distribution; delete inapplicable branches when filling.

---

### Phase 1 -- Connectors Contract Expert: Expected Output

You are the Connectors contract expert. You have not run the operation. You write from the spec alone. Your role ends when the gate token is placed.

**Fill S1 -- Contract Scope.** Replace all `[fill -- Phase 1]` slots.

**Fill S2 -- Expected Output.** Three surface blocks are required. An element without a spec citation is not a valid contract entry. If a surface is not in the spec, write: `[surface]: not specified in spec`.

Count the distinct expected elements. When Expected Output is complete, replace the `[EXPECTED-SEALED ...]` slot with:

```
[EXPECTED-SEALED | clauses:{N} | date:{YYYY-MM-DD} | author:contract-expert | phase:1-complete]
```

Where `{N}` is the element count and `{YYYY-MM-DD}` is today's date. Do not run the operation before placing this token.

---

### Phase 2 -- Automate: Execute, Diff, and Findings

You begin after the `[EXPECTED-SEALED ...]` token. Do not modify S2.

**Fill S3 -- Actual Output.** Run or simulate. Full response: status code, body, headers, side effects.

**Fill S4 -- Diff.** Every element from S2 must appear. Missing elements fail C-02.

If no deviations: replace S5 with `## 5. Findings -- none. Contract satisfied.` Replace the `[FINDINGS-RESOLVED ...]` slot with `[FINDINGS-RESOLVED | gate-clauses:{N} | clauses-resolved:{N} | phase:5-complete]` where both counts echo the gate-clauses value. Fill S6 all-zero, then fill S7 using the Zero branch template.

**Fill S5 -- Findings.** For each deviation, select the matching tier template and fill all fields. The hypothesis names the causal mechanism -- not a restatement of the deviation.

**Fill the post-findings closure token.** After the last finding block, replace the `[FINDINGS-RESOLVED ...]` slot:
- `gate-clauses:` = the `clauses:` value from `[EXPECTED-SEALED]`
- `clauses-resolved:` = count of expected elements that either passed in S4 or have a finding filed in S5
- If `gate-clauses != clauses-resolved`: write `CLAUSE-GAP` and list unaccounted clause IDs before proceeding to S6.

**Fill S6 -- Summary.** Replace every `?` with actual values.

**Fill S7 -- Patterns.** Apply exactly one branch template from the skeleton. Fill all pre-printed slots in the matching branch. Delete inapplicable branches. Do not silently omit.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 -- Full R9 Ceiling: Post-Findings Closure + Branch Template Slots + Mechanism Taxonomy + R8 Platinum Base (C-26 x C-27 x C-28 + C-23/24/25/22/16/14)

**axes:** lifecycle-emphasis x output-format x phrasing-register (plus R8 platinum base)
**hypothesis:** The three new R9 criteria operate on three distinct layers: C-26 on the S5/S6 lifecycle boundary, C-27 on the Patterns template structure, C-28 on the mechanism hypothesis vocabulary. All three are orthogonal to the ten R8 platinum mechanisms and are structurally independent of each other -- adding the post-findings closure token does not help Patterns slot coverage, adding slot templates does not constrain mechanism vocabulary, and adding the taxonomy does not position the closure token. The full R9 ceiling layers all three onto the R8 V-05 platinum base via skeleton pre-declaration: the `[FINDINGS-RESOLVED ...]` token slot appears in its final position in the S5 template area; the Patterns branches carry pre-printed labeled slots with taxonomy-aligned fields; the mechanism taxonomy type token is a required field in every severity template. The regression hypothesis: skeleton pre-declaration of all three mechanisms preserves the essential criteria because each new obligation is a slot to fill rather than a new instruction to follow under cognitive pressure. The eight R8 behavioral protocol rules are extended with two new invariants: the post-findings closure invariant (gate-clauses must equal clauses-resolved or produce a CLAUSE-GAP signal) and the taxonomy invariant (every mechanism field is preceded by a mechanism-type token from the enumeration or TAXONOMY-GAP).

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

1. **Skeleton immutability**: All section headers, template slots, token formats, Patterns branch templates, mechanism taxonomy, and self-test slots are declared in the skeleton below. No section may be added, removed, or reordered after the skeleton is written.
2. **Phase-separation invariant**: Expected output (Phase 1) must be complete and the gate token placed before any operation is run or observed. The gate token commits the clause count as a sealed value.
3. **Role-boundary rule**: The Connectors contract expert does not run or simulate the operation. Automate does not modify S2. Role authority is unconditional within each phase.
4. **Coverage obligation**: Every element in S2 must appear in S4. A missing element is a silent omission -- the trace fails C-02 regardless of finding quality.
5. **Gate manifest invariant**: The opening gate token carries `clauses:N` and one identity field. The post-findings closure token echoes the count. Any divergence between `gate-clauses` and `clauses-resolved` signals an orphaned clause and must be resolved before S6 is filled.
6. **Tier-stratified template invariant**: Use the template matching the severity of each finding. All fields within each template are unconditionally required -- there are no conditional fields.
7. **Self-test invariant**: Every `hypothesis-draft:` must pass the necessary-information self-test before `mechanism-type:` and `mechanism:` are filled. A finding with `hypothesis-draft:` only is incomplete.
8. **Taxonomy invariant**: Every finding must carry a `mechanism-type:` token selected from the five-item enumeration before the `mechanism:` prose. Free-text in the mechanism slot without a preceding type token is a structural violation.
9. **Post-findings closure invariant**: The `[FINDINGS-RESOLVED ...]` token must appear immediately after the last finding block, before S6. `clauses-resolved:M` must equal `gate-clauses:N` or produce a `CLAUSE-GAP` signal with unaccounted clause IDs.
10. **Patterns non-omission**: S7 may not be silently omitted for any finding count. Apply the matching branch template from the skeleton unconditionally. All pre-printed slots in the applied branch must be filled.

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

Before Phase 1 begins, write the following artifact skeleton. Every section header, template slot, token format, finding template with self-test and taxonomy fields, post-findings closure token, and Patterns branch template appears below in its final position.

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

Mechanism taxonomy distribution: field-mapping:? | serialization-path:? | conditional-branch:? | lifecycle-event:? | schema-contract:? | TAXONOMY-GAP:?

## 7. Patterns

--- BRANCH: ZERO PATTERNS ---
Apply when: total findings = 0, OR no two findings share a root cause.
no-pattern-confirmation: [write a statement confirming either (a) no deviations were found and the contract was fully satisfied, or (b) each finding has an independent root cause and no cross-finding pattern exists]

--- BRANCH: SINGLETON ---
Apply when: exactly one root cause group containing two or more findings exists, and no other groups exist.
single-finding-ref: [finding IDs in this group, e.g., F-01, F-03]
root-cause: [the shared causal mechanism -- the internal process or condition common to all findings in this group]
mechanism-type-shared: [the type token shared by this group, if applicable -- confirms taxonomy alignment; write "mixed" if types differ]
attribution:
  - F-NN: [one sentence: how this finding follows from the shared root cause]
  - F-NN: [one sentence: how this finding follows from the shared root cause]
single-fix: [what change -- spec or implementation -- would resolve all findings in this group]

--- BRANCH: MULTI-PATTERN ---
Apply when: two or more distinct root cause groups, each with two or more findings.
pattern-1:
  root-cause: [shared causal mechanism for this group]
  mechanism-type-shared: [type token shared by this group, or "mixed"]
  findings: [F-NN, F-MM]
  single-fix: [resolution for this group]
pattern-2:
  root-cause: [shared causal mechanism for this group]
  mechanism-type-shared: [type token shared by this group, or "mixed"]
  findings: [F-PP, F-QQ]
  single-fix: [resolution for this group]
[repeat pattern-N block for each additional group]
patterns-summary: {N} patterns identified covering {M} of {total} findings
```

The skeleton commits the complete document structure, all three severity-tier templates (with self-test, taxonomy, and connector-impact slots), both structured tokens (opening gate + post-findings closure), and all three Patterns branch templates with pre-printed slots including `mechanism-type-shared:`. Every structural obligation is unconditional and visible before Phase 1 begins.

---

### Phase 1 -- Connectors Contract Expert: Expected Output

You are the Connectors contract expert. You have not run the operation. You have not observed implementation output. You write from the spec alone. Your role ends when the gate token is placed.

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

Where `{N}` is the element count and `{YYYY-MM-DD}` is today's date. Do not run or simulate the operation before placing this token.

---

### Phase 2 -- Automate: Execute, Diff, Findings, and Closure

You begin after the `[EXPECTED-SEALED ...]` token. Do not modify S2. Any belief that an Expected entry is incorrect is a finding -- record it in S5, do not edit.

**Fill S3 -- Actual Output.** Run or simulate the operation. Record the full response: status code, response body, headers, all observable side effects.

**Fill S4 -- Diff.** For every element row in S2, write its result:
- `pass -- {element} -- satisfied`, or
- `F-NN -- {element} -- deviation (see S5)`

Every element must appear. Missing elements fail C-02 regardless of finding quality.

If no deviations: replace S5 with `## 5. Findings -- none. Contract satisfied.` Replace the `[FINDINGS-RESOLVED ...]` slot with `[FINDINGS-RESOLVED | gate-clauses:{N} | clauses-resolved:{N} | phase:5-complete]` where both counts echo the gate-clauses value. Fill S6 all-zero counts and taxonomy distribution all-zero. Fill S7 using the Zero branch template.

**Fill S5 -- Findings.** For each deviation from S4, select the matching severity tier template from the skeleton and fill all fields.

Field rules:
- `deviation` -- both sides required: exact expected value and exact actual value
- `spec` -- must match a clause cited in S2; a finding without a matched clause fails C-04; section-heading citation does not satisfy C-18
- `hypothesis-draft` -- write an initial hypothesis before applying the self-test
- `self-test` -- apply the necessary-information condition: could this draft have been written from the deviation line alone, without knowing the system's internal implementation? YES: restatement -- rewrite. NO: mechanism -- proceed
- `mechanism-type` -- select one token from the taxonomy declared above; must be consistent with the mechanism prose; if no token fits, write `TAXONOMY-GAP` and explain
- `mechanism` -- the final hypothesis after self-test and taxonomy selection: names the internal process, mapping, lookup, serialization path, or code condition; must be consistent with the `mechanism-type` token
- `connector-impact` -- present on all three tiers; for COSMETIC findings write "none" if no integration impact; do not omit the field
- `recommendation` -- present on BREAKING and DEGRADED; structurally absent on COSMETIC
- `rationale` -- present on BREAKING only; one sentence grounded in the mechanism field

A finding block with any unconditional field blank is incomplete and must be filled before proceeding to the next finding.

**Fill the post-findings closure token.** After the last finding block, replace the `[FINDINGS-RESOLVED ...]` slot:
- `gate-clauses:` = the `clauses:` value from `[EXPECTED-SEALED]`
- `clauses-resolved:` = count of expected elements that either passed in S4 (marked `pass`) or have a finding filed in S5
- If `gate-clauses != clauses-resolved`: write `CLAUSE-GAP -- gate-clauses:{N} resolved:{M} -- unaccounted clause IDs: [list]` and investigate before proceeding to S6

**Fill S6 -- Summary.** Replace every `?` with actual values. Include the mechanism taxonomy distribution line using counts from all S5 findings.

**Fill S7 -- Patterns.** Apply exactly one branch template from the skeleton based on actual finding distribution. Fill all pre-printed slots in the applied branch. Delete inapplicable branches. Do not silently omit. For Singleton and Multi-pattern branches, check whether grouped findings share a `mechanism-type` token and fill `mechanism-type-shared:` accordingly.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`
