# trace-contract Variate — Round 8 (rubric v8)

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v8 (C-01–C-25; essential C-01–C-05; max composite 107; golden threshold: all essential pass + composite >= 80)
**Round:** R8 — targeting C-23, C-24, C-25 in isolation (V-01 through V-03), then in combination (V-04, V-05)

---

## Round 8 Context

R7 best scores: 101 tied (V-02 passes C-22 skeleton; V-03 passes C-20 + C-22 together; V-05 platinum covers C-13/C-14/C-16/C-22).
Max composite (v8): 107. R7 ceiling was 104. Three new R8 points are C-23, C-24, C-25.

The three new criteria operate on orthogonal structural layers:
- **C-23** — phase-boundary layer: gate token carries `clauses:N` + one identity field, not just a bracket label
- **C-24** — synthesis-block layer: explicit zero/one/many branch instructions, not just a grouping note when N>=2
- **C-25** — finding-field layer: mechanical self-test decision rule embedded in the template, not just a named disqualifier

---

## Round 8 Variation Map

| Variation | Axis | Primary Targets | Hypothesis |
|-----------|------|-----------------|------------|
| V-01 | lifecycle-emphasis (C-23 isolation) | C-23 | R7 passes C-13 (bracket token present) but not C-23 (clause count + identity field missing). Isolation tests whether upgrading the gate token spec to include `clauses:N` and one identity field is achievable without skeleton or template overhead |
| V-02 | output-format (C-24 isolation) | C-24 | R7 Patterns blocks satisfy C-10 (grouping when N>=2) but not C-24 (no explicit per-branch instructions for zero, singleton, multi). Isolation tests whether adding branch-labeled instructions in the Patterns block produces reliable three-way coverage |
| V-03 | depth (C-25 isolation) | C-25 | R7 satisfies C-05 (named disqualifier present) but not C-25 (no self-applicable decision rule). Isolation tests whether embedding the necessary-information self-test in the finding template eliminates symptom restatements at write time |
| V-04 | lifecycle-emphasis x output-format (C-23 x C-24) | C-23, C-24 | C-23 (phase boundary) and C-24 (synthesis block) operate on different structural layers. Combination tests whether skeleton pre-declaration of both the gate token format and the three-branch Patterns template produces additive coverage without essential criterion regression |
| V-05 | lifecycle-emphasis x output-format x depth (C-23 x C-24 x C-25 + R7 platinum base) | C-23, C-24, C-25, C-13, C-14, C-16, C-22 | Full R8 ceiling. Three new criteria layered onto the R7 V-05 platinum base. Tests whether all 25 criteria can be simultaneously targeted without cognitive overhead that regresses C-01 through C-05 |

---

## V-01 — Lifecycle Emphasis: Gate Structured-Metadata Manifest (C-23 isolation)

**axis:** lifecycle-emphasis
**hypothesis:** C-13 requires a parseable bracket token at the phase boundary — any structured label such as `[EXPECTED SEALED]` passes. C-23 escalates: the token must carry key-value metadata — at minimum `clauses:N` capturing how many expected elements were committed, plus at least one identity field (`date:`, `author:`, or `phase:`). The clause count converts the binary seal/unseal into a quantitative commit invariant: the element count is locked at Phase 1 close and can be echoed at Phase 5 close to detect post-gate additions. A discrepancy between gate count and summary coverage count signals contamination. The identity field turns the gate into a provenance trace — an auditor can confirm which role sealed the contract and when without reading surrounding prose. This variation isolates C-23 as the sole axis change from the R7 step-sequence baseline (which already passes C-12, C-13, and most essential criteria). Only the gate token format is upgraded.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### Step 1 — Contract Scope

Write a `## Contract Scope` section:
- Operation name and HTTP method (or equivalent)
- Connector or Automate context and environment
- Input fixture — state inline; no external file references
- Spec version and section governing this operation's output contract

---

### Step 2 — Expected Output (Phase 1 — from spec only)

**Role**: You are the Connectors contract expert. You have not run the operation. You have not observed implementation output. You write from the spec alone. Your role ends when the gate token is placed.

Write the `## Expected Output` section. Cover all three contract surfaces:
- **Success path** — nominal input, nominal output per spec
- **Error path** — invalid or missing input, expected error response per spec
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

For each expected element, cite the specific clause from the spec that requires it (rule number, named constraint, or sub-clause path — not a section heading alone). An expected element without a spec citation is not a valid contract entry. If a surface is not defined in the spec, write: `[surface]: not specified in spec`.

When Expected Output is complete and every element carries a spec citation, count the number of distinct expected elements written in this section. Write the phase gate token on its own line immediately after the last expected element:

```
[EXPECTED-SEALED | clauses:{N} | date:{YYYY-MM-DD} | author:contract-expert | phase:1-complete]
```

Replace `{N}` with the exact count of expected elements. Replace `{YYYY-MM-DD}` with today's date. The token must appear exactly once — after the last expected element, before any actual output.

Do not run or simulate the operation before writing this token. The token asserts that Phase 1 was completed by the Connectors contract expert — a role that had not observed runtime output — and commits the clause count as a sealed auditable value.

---

### Step 3 — Actual Output

**Role**: You are Automate. You begin after the `[EXPECTED-SEALED ...]` token. Do not modify the Expected Output section. Any belief that an Expected entry is incorrect is a finding — record it in Step 5; do not edit.

Run or simulate the operation. Write the `## Actual Output` section: status code, response body, headers, observable side effects.

---

### Step 4 — Diff

Write the `## Diff` section. For every element in `## Expected Output`:
- `pass -- {element} -- satisfied`, or
- `F-NN -- {element} -- deviation (see findings)`

Every element must appear. Elements present in Expected Output but absent from the Diff are silent omissions — the trace fails C-02 regardless of finding quality.

If no deviations: write `## Diff -- Contract satisfied. No findings.` and skip to Step 6.

---

### Step 5 — Findings

For each deviation, write a finding entry using the appropriate severity-tier template:

**BREAKING FINDING**
```
Finding F-NN [BREAKING]
deviation:        expected [X]; actual [Y]
spec:             [specific clause from Expected Output -- rule number, named constraint, or sub-clause path]
hypothesis:       [the causal mechanism -- name the process, mapping, serialization path, or condition that produced the wrong output; not a restatement of what differed]
connector-impact: [what breaks for Automate flows or Connector integrations relying on this field/behavior]
recommendation:   [amend-spec | fix-impl | needs-discussion]
rationale:        [one sentence: which side of the contract is wrong and why, grounded in the hypothesis]
```

**DEGRADED FINDING**
```
Finding F-NN [DEGRADED]
deviation:        expected [X]; actual [Y]
spec:             [specific clause]
hypothesis:       [the causal mechanism -- name the process, mapping, serialization path, or condition]
connector-impact: [what silently fails or degrades for Automate flows or Connector integrations]
recommendation:   [amend-spec | fix-impl | needs-discussion]
```

**COSMETIC FINDING**
```
Finding F-NN [COSMETIC]
deviation:  expected [X]; actual [Y]
spec:       [specific clause]
hypothesis: [the causal mechanism -- name the process, mapping, serialization path, or condition]
```

Hypothesis rule (applies to all tiers): The hypothesis names a causal mechanism — it does not restate the deviation. If your hypothesis could be written without knowing anything about the system under test — only from reading the deviation line — it is a symptom restatement, not a mechanism. A valid hypothesis requires knowledge of why: what process, mapping, serialization path, or code path produced the wrong output.

---

### Step 6 — Summary

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

After completing the Summary, write the closure token:

```
[TRACE-COMPLETE | findings:{N} | breaking:{N} | degraded:{N} | cosmetic:{N} | verdict:{violated|satisfied} | gate-clauses:{N from EXPECTED-SEALED token}]
```

The `gate-clauses` value must echo the `clauses:` field from the `[EXPECTED-SEALED]` token written in Step 2. If the verified clause count in Summary diverges from `gate-clauses`, note the discrepancy — it signals that expected elements were added or removed after the gate was sealed.

---

### Step 7 — Patterns

Write a `## Patterns` section.

If two or more findings share a root cause, group them, name the shared mechanism, list the finding IDs, and state the single fix that would resolve all findings in the group.

If no findings share a root cause (or if there are zero or one findings), write: `No cross-finding patterns detected.`

This section may not be silently omitted regardless of finding count.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Output Format: Multi-Branch Patterns Handling (C-24 isolation)

**axis:** output-format
**hypothesis:** C-10 requires pattern recognition: when two or more findings share a root cause, call it out explicitly. C-24 escalates: explicit branch instructions for all three cardinality cases. Zero patterns: an affirmative confirmation statement is required — writing nothing, or silently omitting the section, does not satisfy the zero-pattern branch; the section must exist and must state that no patterns were found. Singleton: two or more findings traceable to one root cause, and this is the only such group — the attribution must explain why each finding follows from that mechanism, not just assert "same root cause." Multi-pattern: two or more distinct root cause groups, each grouped with a per-group single-fix claim. Prior rounds satisfy C-10 for the multi-pattern case but leave zero and singleton cases ambiguous — the Patterns section is either absent (zero findings) or not explicitly singleton-labeled (two findings, one pattern). Isolation tests whether adding explicit branch-labeled instructions in the Patterns block alone produces reliable C-24 compliance.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state -- inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### Step 1 — Contract Scope

Write a `## Contract Scope` section:
- Operation name and HTTP method (or equivalent)
- Connector or Automate context and environment
- Input fixture — state inline; no external file references
- Spec version and section governing this operation's output contract

---

### Step 2 — Expected Output (Phase 1 — from spec only)

**Role**: You are the Connectors contract expert. You have not run the operation. You write from the spec alone. Your role ends when the gate token is placed.

Write the `## Expected Output` section. Cover all three contract surfaces:
- **Success path** — nominal input, nominal output per spec
- **Error path** — invalid or missing input, expected error response per spec
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

For each expected element, cite the specific spec clause that requires it (rule number, named constraint, or sub-clause path — not a section heading alone). An expected element without a spec citation is not a valid contract entry. If a surface is not in the spec, write: `[surface]: not specified in spec`.

When Expected Output is complete, write: `[CONTRACT COMMITTED]`

Do not proceed to Step 3 before writing this line.

---

### Step 3 — Actual Output

**Role**: You are Automate. You begin after `[CONTRACT COMMITTED]`. Do not modify the Expected Output section.

Run or simulate the operation. Write the `## Actual Output` section: status code, response body, headers, observable side effects.

---

### Step 4 — Diff

Write the `## Diff` section. For every element in `## Expected Output`:
- `pass -- {element} -- satisfied`, or
- `F-NN -- {element} -- deviation (see findings)`

Every element must appear. Elements present in Expected Output but absent from the Diff are silent omissions — the trace fails C-02 regardless of finding quality.

If no deviations: write `## Diff -- Contract satisfied. No findings.` and skip to Step 6.

---

### Step 5 — Findings

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

### Step 6 — Summary

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

### Step 7 — Patterns

Write a `## Patterns` section. Determine the count of distinct root cause groups across all findings. Apply the matching branch instruction below. This section may not be silently omitted regardless of finding count.

**Branch: Zero patterns**
Apply when: total findings = 0 or 1, OR when no two findings share a root cause.
Write:
```
Patterns: none
No findings share a root cause. Each deviation is attributable to an independent mechanism. (If no findings were produced: no deviations were found to pattern-analyze.)
```
This branch is not optional for low-finding runs. A blank section, a missing section, or a section containing only a heading does not satisfy this branch.

**Branch: Singleton**
Apply when: exactly one root cause group exists containing two or more findings, and no other groups exist.
Write:
```
Pattern P-01: [name the shared root cause mechanism]
Findings: [list all finding IDs in this group]
Attribution:
  - F-NN: [one sentence explaining how this finding follows from the shared mechanism]
  - F-NN: [one sentence explaining how this finding follows from the shared mechanism]
Single fix: [what change -- to spec or implementation -- would resolve all findings in this group]
```
The attribution lines are required. Asserting "same root cause" without explaining the connection per finding does not satisfy the singleton branch.

**Branch: Multi-pattern**
Apply when: two or more distinct root cause groups each containing two or more findings.
Write:
```
Pattern P-01: [mechanism name]
Findings: [finding IDs]
Single fix: [resolution]

Pattern P-02: [mechanism name]
Findings: [finding IDs]
Single fix: [resolution]

[Continue for additional pattern groups]
{N} patterns identified covering {M} of {total} findings.
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Depth: Hypothesis Self-Test Rule (C-25 isolation)

**axis:** depth
**hypothesis:** C-05 requires that the hypothesis field explicitly disqualifies symptom restatements — the finding template or instructions must include a disqualifier such as "not a restatement of what differed." C-25 escalates: a mechanical self-test decision rule must be embedded in the template, applicable at write time without external judgment. The specific decision procedure uses a necessary-information condition: if the hypothesis could be written from the deviation line alone — without knowing anything about the system under test — it is a symptom restatement. The test is self-applicable because it has a binary outcome the model can evaluate: does the hypothesis require system knowledge to write? A hypothesis that could be generated from the deviation alone ("the field was absent") contains no system knowledge. A hypothesis that names an internal mapping, serialization path, or conditional branch ("the cursor-generation step short-circuits on zero-count and the spec requires the field even when null") requires knowledge of the system's internal behavior. The self-test converts a named requirement into a decision procedure. This variation isolates C-25 as the sole axis change, embedding the self-test protocol inside the finding template without adding structural overhead.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state -- inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### Step 1 — Contract Scope

Write a `## Contract Scope` section:
- Operation name and HTTP method (or equivalent)
- Connector or Automate context and environment
- Input fixture — state inline; no external file references
- Spec version and section governing this operation's output contract

---

### Step 2 — Expected Output (Phase 1 — from spec only)

**Role**: You are the Connectors contract expert. You have not run the operation. You write from the spec alone. Your role ends when the gate token is placed.

Write the `## Expected Output` section. Cover all three contract surfaces:
- **Success path** — nominal input, nominal output per spec
- **Error path** — invalid or missing input, expected error response per spec
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

For each expected element, cite the specific spec clause that requires it. An expected element without a spec citation is not a valid contract entry. If a surface is not in the spec, write: `[surface]: not specified in spec`.

When Expected Output is complete, write: `[CONTRACT COMMITTED]`

Do not proceed to Step 3 before writing this line.

---

### Step 3 — Actual Output

**Role**: You are Automate. You begin after `[CONTRACT COMMITTED]`. Do not modify the Expected Output section.

Run or simulate the operation. Write the `## Actual Output` section: status code, response body, headers, observable side effects.

---

### Step 4 — Diff

Write the `## Diff` section. For every element in `## Expected Output`:
- `pass -- {element} -- satisfied`, or
- `F-NN -- {element} -- deviation (see findings)`

Every element must appear. Elements present in Expected Output but absent from the Diff are silent omissions — the trace fails C-02 regardless of finding quality.

If no deviations: write `## Diff -- Contract satisfied. No findings.` and skip to Step 6.

---

### Step 5 — Findings

For each deviation, write a finding entry. The hypothesis field uses a two-stage self-test protocol described below each template.

**BREAKING FINDING**
```
Finding F-NN [BREAKING]
deviation:        expected [X]; actual [Y]
spec:             [specific clause -- rule number, named constraint, or sub-clause path]
hypothesis-draft: [write your initial hypothesis here before applying the self-test]
self-test:        [Could you have written this hypothesis from the deviation line alone, without knowing anything about the system under test? YES means it is a symptom restatement -- rewrite it naming the internal mechanism. NO means it contains system knowledge -- proceed.]
mechanism:        [final hypothesis after self-test -- names the internal process, mapping, serialization path, or code condition]
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
self-test:        [Could you have written this from the deviation line alone, without knowing the system? YES -- restatement; rewrite. NO -- mechanism; proceed.]
mechanism:        [final hypothesis after self-test]
connector-impact: [what silently fails or degrades for Automate flows or Connector integrations]
recommendation:   [amend-spec | fix-impl | needs-discussion]
```

**COSMETIC FINDING**
```
Finding F-NN [COSMETIC]
deviation:  expected [X]; actual [Y]
spec:       [specific clause]
hypothesis-draft: [write your initial hypothesis here]
self-test:  [Could you have written this from the deviation line alone? YES -- restatement; rewrite. NO -- mechanism; proceed.]
mechanism:  [final hypothesis after self-test]
```

**Self-test protocol (applies to all tiers):**

The self-test applies a necessary-information condition to distinguish causal mechanisms from symptom restatements:

1. Write a draft hypothesis in `hypothesis-draft`.
2. Apply the self-test: could this hypothesis have been written by someone who read only the deviation line `expected [X]; actual [Y]` — with no knowledge of the system's internal implementation, architecture, or code?
   - YES: the draft is a symptom restatement. It describes the gap between X and Y but contains no knowledge about why the system produced Y instead of X. Rewrite it to name a specific internal process, mapping, lookup, schema transform, or code condition.
   - NO: the draft requires knowledge of the system's internals to write. It is a valid causal mechanism.
3. Record the self-test verdict in `self-test:` (YES -- rewriting / NO -- proceeding).
4. Record the final hypothesis in `mechanism:`.

The `self-test:` and `mechanism:` fields are required on every finding. A finding with only `hypothesis-draft:` filled is incomplete.

---

### Step 6 — Summary

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

### Step 7 — Patterns

Write a `## Patterns` section.

If two or more findings share a root cause: name the shared mechanism, list finding IDs, and state the single fix that would resolve all findings in the group.

If no findings share a root cause: write `No cross-finding patterns detected.`

This section may not be silently omitted.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Combination: Gate Manifest + Multi-Branch Patterns (C-23 x C-24)

**axes:** lifecycle-emphasis x output-format
**hypothesis:** C-23 (phase-boundary layer) and C-24 (synthesis-block layer) are structurally independent: upgrading the gate token to carry a clause count does not help the Patterns section become branch-aware, and adding Patterns branch instructions does not help the gate token carry metadata. The combination tests whether both can be satisfied simultaneously when the artifact skeleton pre-declares both obligations before Phase 1 begins. The interaction hypothesis: pre-declaring the structured gate token format in the skeleton makes the clause-count commitment visible from document open — the analyst must count elements before they begin writing Phase 2, not as an afterthought at gate time. Pre-declaring the three-branch Patterns template makes each branch an explicit slot to fill rather than an open-ended instruction to follow under cognitive load. Neither mechanism helps the other's failure mode; their combination is additive if both are pre-declared in the skeleton. This variation adds V-01 gate manifest (C-23) and V-02 three-branch Patterns (C-24) to the R7 platinum baseline, without yet adding the C-25 self-test.

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

1. **Skeleton immutability**: All section headers, template slots, token formats, and Patterns branch instructions are declared in the skeleton below. No section may be added, removed, or reordered after the skeleton is written.
2. **Phase-separation invariant**: Expected output (Phase 1) must be complete and the gate token placed before any operation is run or observed. Phases 1 and 2 may not overlap.
3. **Role-boundary rule**: The Connectors contract expert does not run or simulate the operation. Automate does not modify the Expected Output section. Role authority is unconditional within each phase.
4. **Coverage obligation**: Every element in the Expected Output section must appear in the Diff. A missing element is a silent omission -- the trace fails C-02 regardless of finding quality.
5. **Gate manifest invariant**: The gate token commits `clauses:N` and one identity field. The closure token echoes the clause count. Any divergence signals post-gate contamination.
6. **Patterns non-omission**: The Patterns section (S7) may not be silently omitted for any finding count. Apply the matching branch instruction from the skeleton unconditionally.

---

Before Phase 1 begins, write the following artifact skeleton. Every section header, template slot, token format, and Patterns branch instruction appears below in its final position.

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
spec:             [specific clause from S2]
hypothesis:       [the mechanism -- causal process, mapping, serialization path, or condition]
connector-impact: [what breaks for Automate flows or Connector integrations]
recommendation:   [amend-spec | fix-impl | needs-discussion]
rationale:        [one sentence: which side of the contract is wrong and why]

--- DEGRADED FINDING TEMPLATE ---

Finding F-NN [DEGRADED]
deviation:        expected [X]; actual [Y]
spec:             [specific clause from S2]
hypothesis:       [the mechanism -- causal process, mapping, serialization path, or condition]
connector-impact: [what silently fails or degrades]
recommendation:   [amend-spec | fix-impl | needs-discussion]

--- COSMETIC FINDING TEMPLATE ---

Finding F-NN [COSMETIC]
deviation:  expected [X]; actual [Y]
spec:       [specific clause from S2]
hypothesis: [the mechanism -- causal process, mapping, serialization path, or condition]

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

[TRACE-COMPLETE | findings:{N} | breaking:{N} | degraded:{N} | cosmetic:{N} | verdict:{violated|satisfied} | gate-clauses:{N}]

## 7. Patterns

--- BRANCH: ZERO PATTERNS ---
Apply when: total findings = 0 or 1, OR no two findings share a root cause.
Patterns: none
No findings share a root cause. Each deviation is independently caused. (Or: no findings were produced.)

--- BRANCH: SINGLETON ---
Apply when: exactly one root cause group exists (two or more findings), no other groups.
Pattern P-01: [name the shared root cause mechanism]
Findings: [list finding IDs]
Attribution:
  - F-NN: [how this finding follows from the shared mechanism]
  - F-NN: [how this finding follows from the shared mechanism]
Single fix: [what change would resolve all findings in this group]

--- BRANCH: MULTI-PATTERN ---
Apply when: two or more distinct root cause groups, each with two or more findings.
Pattern P-01: [mechanism name]
Findings: [finding IDs]
Single fix: [resolution]

Pattern P-02: [mechanism name]
Findings: [finding IDs]
Single fix: [resolution]

{N} patterns identified covering {M} of {total} findings.
```

The skeleton commits the complete document structure, all finding templates, both structured tokens, and all three Patterns branch instructions. Apply the branch in S7 that matches the actual finding distribution; delete the inapplicable branches when filling.

---

### Phase 1 — Connectors Contract Expert: Expected Output

You are the Connectors contract expert. You have not run the operation. You write from the spec alone. Your role ends when the gate token is placed.

**Fill S1 -- Contract Scope.** Replace all `[fill -- Phase 1]` slots.

**Fill S2 -- Expected Output.** Three surface blocks are required. An element without a spec citation is not a valid contract entry. If a surface is not in the spec, write: `[surface]: not specified in spec`.

Count the distinct expected elements. When Expected Output is complete, replace the `[EXPECTED-SEALED ...]` slot with:

```
[EXPECTED-SEALED | clauses:{N} | date:{YYYY-MM-DD} | author:contract-expert | phase:1-complete]
```

Where `{N}` is the count of expected elements and `{YYYY-MM-DD}` is today's date. Do not run the operation before placing this token.

---

### Phase 2 — Automate: Execute, Diff, and Findings

You begin after the `[EXPECTED-SEALED ...]` token. Do not modify S2.

**Fill S3 -- Actual Output.** Run or simulate. Full response: status code, body, headers, side effects.

**Fill S4 -- Diff.** Every element from S2 must appear. Missing elements fail C-02.

If no deviations: replace S5 with `## 5. Findings -- none. Contract satisfied.` Fill S6 all-zero, write `[TRACE-COMPLETE ...]` closure token, then fill S7 using the Zero patterns branch.

**Fill S5 -- Findings.** For each deviation, select the matching tier template and fill all fields. The hypothesis names the causal mechanism -- not a restatement of the deviation. If the hypothesis could be written from the deviation line alone without knowing the system, it is a symptom restatement; rewrite it.

**Fill S6 -- Summary.** Replace every `?`. Write the `[TRACE-COMPLETE ...]` closure token echoing `gate-clauses` from the `[EXPECTED-SEALED]` token. Flag any count discrepancy.

**Fill S7 -- Patterns.** Apply exactly one branch from the skeleton. Delete inapplicable branches. Do not silently omit.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — Full R8 Ceiling: Gate Manifest + Multi-Branch Patterns + Hypothesis Self-Test + Skeleton + Stratified Templates (C-23 x C-24 x C-25 + C-22 x C-16 x C-14)

**axes:** lifecycle-emphasis x output-format x depth (plus output-format x depth from R7 platinum base)
**hypothesis:** The three new R8 criteria operate on three distinct layers: C-23 on the phase boundary, C-24 on the synthesis block, C-25 on each finding's hypothesis field. All three are orthogonal to the four R7 platinum mechanisms: C-22 (document shape), C-16 (finding tier structure), C-13 (parseable gate token -- superseded by C-23), C-14 (per-finding integration slot). The combined prompt targets all seven mechanisms simultaneously via skeleton pre-declaration: the skeleton makes every structural obligation visible from document open, before Phase 1 begins, so each mechanism is a slot to fill rather than an obligation to remember under cognitive pressure. The regression hypothesis: pre-declaration reduces cognitive load by converting deferred obligations into visible gaps -- the model fills committed slots rather than inventing structure mid-execution. Essential criteria C-01 through C-05 should remain stable because the skeleton pre-declares their requirements (role assignment in S2 header, coverage obligation in S4 instruction, one-finding-per-deviation in S5 instruction, spec citations in S2 format, hypothesis self-test in S5 template) without adding competing instructions.

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

1. **Skeleton immutability**: All section headers, template slots, token formats, Patterns branch instructions, and hypothesis self-test slots are declared in the skeleton below. No section may be added, removed, or reordered after the skeleton is written. The skeleton functions simultaneously as: a document-shape commitment device (C-22), a structural completeness enforcer for all sections including Patterns (C-24), and a phase-separation guarantor (C-12, C-23).
2. **Phase-separation invariant**: Expected output (Phase 1) must be complete and the gate token placed before any operation is run or observed. The gate token commits the clause count as a sealed value.
3. **Role-boundary rule**: The Connectors contract expert does not run or simulate the operation. Automate does not modify S2. Role authority is unconditional within each phase.
4. **Coverage obligation**: Every element in S2 must appear in S4. A missing element is a silent omission -- the trace fails C-02 regardless of finding quality.
5. **Gate manifest invariant**: The gate token carries `clauses:N` and one identity field. The closure token echoes the count. Any divergence signals post-gate contamination.
6. **Tier-stratified template invariant**: Use the template matching the severity of each finding. Fields within each template are unconditionally required -- there are no conditional fields.
7. **Self-test invariant**: Every hypothesis field must pass the self-test before the finding block is considered complete. A `hypothesis-draft:` without a `self-test:` + `mechanism:` pair is incomplete.
8. **Patterns non-omission**: S7 may not be silently omitted for any finding count. Apply the matching branch from the skeleton unconditionally.

---

Before Phase 1 begins, write the following artifact skeleton. Every section header, template slot, token format, Patterns branch instruction, and self-test slot appears below in its final position.

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

--- BREAKING FINDING TEMPLATE (6 unconditional fields) ---

Finding F-NN [BREAKING]
deviation:        expected [X]; actual [Y]
spec:             [specific clause from S2 -- rule number, named constraint, or sub-clause path; not a section heading alone]
hypothesis-draft: [write your initial hypothesis here]
self-test:        [Could you have written this from the deviation line alone, without knowing the system? YES -- restatement; rewrite naming the internal mechanism. NO -- mechanism; proceed.]
mechanism:        [final hypothesis -- names the internal process, mapping, serialization path, or code condition]
connector-impact: [what breaks for Automate flows or Connector integrations relying on this field/behavior]
recommendation:   [amend-spec | fix-impl | needs-discussion]
rationale:        [one sentence: which side of the contract is wrong and why, grounded in the mechanism]

--- DEGRADED FINDING TEMPLATE (6 unconditional fields) ---

Finding F-NN [DEGRADED]
deviation:        expected [X]; actual [Y]
spec:             [specific clause from S2]
hypothesis-draft: [write your initial hypothesis here]
self-test:        [Could you have written this from the deviation line alone? YES -- restatement; rewrite. NO -- mechanism; proceed.]
mechanism:        [final hypothesis]
connector-impact: [what silently fails or degrades for Automate flows or Connector integrations]
recommendation:   [amend-spec | fix-impl | needs-discussion]

--- COSMETIC FINDING TEMPLATE (5 unconditional fields) ---

Finding F-NN [COSMETIC]
deviation:        expected [X]; actual [Y]
spec:             [specific clause from S2]
hypothesis-draft: [write your initial hypothesis here]
self-test:        [Could you have written this from the deviation line alone? YES -- restatement; rewrite. NO -- mechanism; proceed.]
mechanism:        [final hypothesis]
connector-impact: [Automate / Connector integration impact -- write "none" if not applicable; field always present]

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

[TRACE-COMPLETE | findings:{N} | breaking:{N} | degraded:{N} | cosmetic:{N} | verdict:{violated|satisfied} | gate-clauses:{N from EXPECTED-SEALED}]

## 7. Patterns

--- BRANCH: ZERO PATTERNS ---
Apply when: total findings = 0 or 1, OR no two findings share a root cause.
Patterns: none
No findings share a root cause. Each deviation is independently caused. (Or: no findings were produced.)
[Do not silently omit this section -- write the above statement even when there are no findings.]

--- BRANCH: SINGLETON ---
Apply when: exactly one root cause group exists (two or more findings trace to it), no other groups.
Pattern P-01: [name the shared root cause mechanism]
Findings: [list all finding IDs]
Attribution:
  - F-NN: [one sentence explaining how this finding follows from the shared mechanism -- not just "same cause"]
  - F-NN: [one sentence explaining how this finding follows from the shared mechanism]
Single fix: [what change -- spec or implementation -- would resolve all findings in this group]

--- BRANCH: MULTI-PATTERN ---
Apply when: two or more distinct root cause groups, each with two or more findings.
Pattern P-01: [mechanism name]
Findings: [finding IDs]
Single fix: [resolution]

Pattern P-02: [mechanism name]
Findings: [finding IDs]
Single fix: [resolution]

[Continue for additional patterns]
{N} patterns identified covering {M} of {total} findings.
```

The skeleton above commits the complete document structure, all three severity-tier templates with self-test slots, both structured tokens, the `connector-impact` slot on every tier, and all three Patterns branch instructions. Every structural obligation is unconditional and visible before Phase 1 begins.

---

### Phase 1 — Connectors Contract Expert: Expected Output

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

### Phase 2 — Automate: Execute, Diff, and Findings

You begin after the `[EXPECTED-SEALED ...]` token. Do not modify S2. Any belief that an Expected entry is incorrect is a finding -- record it in S5, do not edit.

**Fill S3 -- Actual Output.** Run or simulate the operation. Record the full response: status code, response body, headers, all observable side effects.

**Fill S4 -- Diff.** For every element row in S2, write its result:
- `pass -- {element} -- satisfied`, or
- `F-NN -- {element} -- deviation (see S5)`

Every element must appear. Missing elements fail C-02 regardless of finding quality.

If no deviations: replace S5 with `## 5. Findings -- none. Contract satisfied.` Fill S6 all-zero counts, write `[TRACE-COMPLETE ...]` closure token, then fill S7 using the Zero patterns branch. Skip finding instructions below.

**Fill S5 -- Findings.** For each deviation from S4, select the matching severity tier template from the skeleton and fill all fields.

Field rules:
- `deviation` -- both sides required: the exact expected value and the exact actual value
- `spec` -- must match a clause cited in S2; a finding without a matched clause fails C-04; a section-heading citation does not satisfy C-18
- `hypothesis-draft` -- write an initial hypothesis before applying the self-test
- `self-test` -- apply the necessary-information condition: could this hypothesis have been written from the deviation line alone, without knowing the system's internal implementation? YES: restatement -- rewrite. NO: mechanism -- proceed.
- `mechanism` -- the final hypothesis after self-test: names the internal process, mapping, lookup, serialization path, or code condition that caused the deviation
- `connector-impact` -- present on all three tiers; for COSMETIC findings write "none" if no integration impact; do not omit the field
- `recommendation` -- present on BREAKING and DEGRADED; structurally absent on COSMETIC
- `rationale` -- present on BREAKING only; one sentence grounded in the mechanism field

A finding block with any unconditional field blank is incomplete and must be filled before proceeding to the next finding.

**Fill S6 -- Summary.** Replace every `?` with actual values. Write the `[TRACE-COMPLETE ...]` closure token -- echoing `gate-clauses` from the `[EXPECTED-SEALED]` token. If the Coverage clause count differs from `gate-clauses`, note: `Note: clause count diverges from gate manifest -- verify no post-gate additions were made to S2.`

**Fill S7 -- Patterns.** Apply exactly one branch from the skeleton based on actual finding distribution. Delete inapplicable branches when filling. Do not silently omit this section.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`
