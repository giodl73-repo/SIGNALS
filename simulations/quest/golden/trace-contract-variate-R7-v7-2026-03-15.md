# trace-contract Variate — Round 7 (rubric v7)

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v7 (C-01–C-22; essential C-01–C-05; max composite 104; golden threshold: all essential pass + composite ≥ 80)
**Round:** R7 — targeting C-22 in isolation and combined with the structural template criteria (C-15/C-16) and sequencing criteria (C-13/C-14) that R6 best performers are missing

---

## Round 7 Context

R6 best scores: 101 (tied — V-02 with C-21 PASS; V-03 with C-20 + C-22 PASS, each failing 2 other criteria).
R6-V-01 scores 100: fails C-15, C-16, and C-22.
Max composite (v7): 104. Gap from R6 leader to max: 3 pts.

The 3 missing points in R6 leaders are likely drawn from:
- **C-15** — amendment enforcement by template structure (requires `recommended-action` as an unconditional labeled slot in the breaking-finding template, not conditional language)
- **C-16** — severity-stratified template architecture (requires three distinct templates, one per tier, not a unified template with conditional fields)
- **C-13** — machine-readable gate token (requires a parseable structured token, not just a prose commit gate)

C-14 (per-finding integration coverage) is the fourth candidate if the above three are already passing in some R6 variants.

---

## Round 7 Variation Map

| Variation | Axis | Primary Targets | Hypothesis |
|-----------|------|-----------------|------------|
| V-01 | output-format (C-22 skeleton isolation) | C-22 | R6-V-03 passes C-22 in combination with C-20 and C-21. Isolation tests whether the skeleton-first mechanism alone reliably enforces document shape without the role-separation wall |
| V-02 | output-format (C-16 severity-stratified templates) | C-16, C-15 | C-16 requires three distinct templates — one per severity tier. Isolating the stratified architecture tests whether removing the unified template's conditional fields produces reliable C-15 compliance as a structural side effect |
| V-03 | lifecycle-emphasis (C-13 machine-readable gate) | C-13, C-12 | C-12 is satisfied by prose gate acknowledgment. C-13 escalates to a parseable structured token. Isolation tests whether the token format is achievable without adding skeleton or template overhead |
| V-04 | output-format × output-format (C-22 + C-16) | C-22, C-16, C-15 | Skeleton pre-declares severity-tier templates in their final positions before Phase 1. The skeleton makes C-16's stratified architecture visible from document open rather than only at the findings phase |
| V-05 | output-format × lifecycle-emphasis × depth (C-22 + C-16 + C-13 + C-14) | C-22, C-16, C-15, C-13, C-14 | Platinum: four orthogonal mechanisms — document shape (C-22), finding tier structure (C-16), sequencing token (C-13), per-finding integration slot (C-14). Covers the four failure modes that differ between 101 and 104 |

---

## V-01 — Output Format: Full Artifact Skeleton Before Phase 1 (C-22 isolation)

**axis:** output-format
**hypothesis:** C-22 requires the complete artifact skeleton — all section headers and template slots in final position — to appear as a named structural declaration before Phase 1 begins. R6-V-03 passes C-22 but only in combination with C-20 (pre-printed Patterns slot in the Phase 5 summary template) and C-21 (role-separated authorship). The two mechanisms were entangled: the skeleton appeared as part of the role-separation structure, not as an independent preamble. Isolating C-22 tests whether pre-printing the complete artifact shape alone acts as a structural guarantor. The hypothesis: a pre-declared skeleton makes every section header unconditionally visible from document open. The analyst cannot omit the Summary section, the Patterns section, or the phase gate without leaving a visible hole in the committed skeleton — a structural debt that must be discharged, not a forgotten obligation. This is distinct from C-19 (behavioral rules before Phase 1, which instruct without pre-printing) and from C-20 (which pre-prints one section, not the whole shape).

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

Before Phase 1 begins, write the following artifact skeleton in full. Every section header and template slot appears below in its final position. Sections are filled during the phases that follow. No section may be added, removed, or reordered after the skeleton is written.

```
## Artifact Skeleton — {topic}-contract-{date}.md

## 1. Contract Scope
- Operation: [fill — Phase 1]
- Connector / Automate context: [fill — Phase 1]
- Input fixture (inline): [fill — Phase 1]
- Spec version and section: [fill — Phase 1]

## 2. Expected Output (Phase 1 — from spec only)

### Success Path
| Element | Spec Clause |
|---------|-------------|
| [fill — Phase 1] | [fill — Phase 1] |

### Error Path
| Element | Spec Clause |
|---------|-------------|
| [fill — Phase 1] | [fill — Phase 1] |

### Edge Case: [name — fill Phase 1]
| Element | Spec Clause |
|---------|-------------|
| [fill — Phase 1] | [fill — Phase 1] |

[EXPECTED SEALED]

## 3. Actual Output (Phase 3 — run after gate)
- Status code: [fill — Phase 3]
- Response body: [fill — Phase 3]
- Headers: [fill — Phase 3]
- Observable side effects: [fill — Phase 3]

## 4. Diff
| Element | Result |
|---------|--------|
| [element from §2] | ✓ satisfied / F-NN deviation |

## 5. Findings
[Finding blocks go here — one per deviation from §4]

## 6. Summary
| Severity | Count |
|----------|-------|
| breaking | ?     |
| degraded | ?     |
| cosmetic | ?     |
| total    | ?     |

Verdict: [Contract violated / Contract satisfied]

Recommendations:
- F-NN: [amend-spec / fix-impl / needs-discussion] — [rationale]

Coverage: ? / ? clauses verified, ? deviations found

## 7. Patterns
[If N ≥ 2 findings share a root cause: name the shared mechanism and list grouped findings]
[If N ≥ 2 but no shared root cause: "No patterns — all findings are independent"]
[If N ≤ 1: omit this section entirely]
```

The skeleton above is the committed document structure. Fill each slot during the phase it belongs to. Do not add sections. Do not omit sections.

---

### Phase 1 — Connectors Contract Expert

You are the Connectors contract expert. You have not run the operation. You have not observed implementation output. You write from the spec alone.

**Fill § 1 — Contract Scope.** Replace each `[fill — Phase 1]` slot with: operation name and HTTP method (or equivalent); connector or Automate context and environment; input fixture (inline — no external file references); spec version and section.

**Fill § 2 — Expected Output.** Replace each `[fill — Phase 1]` slot with expected elements and spec citations.

Three surface blocks are required. If a surface is not defined in the spec, write the block heading and state: `[surface]: not specified in spec`.

An expected element without a spec citation is not a valid contract entry. Do not carry unanchored elements past the gate.

When Expected Output is complete and every element carries a spec citation, write exactly:

`[EXPECTED SEALED — Phase 1 complete. Contract Author role ends. Automate begins after this line.]`

Replace the `[EXPECTED SEALED]` slot in § 2 with this line.

---

### Phase 3 — Automate

You begin after the `[EXPECTED SEALED]` token. Do not modify § 2 — Expected Output. Any belief that an Expected entry is wrong is a finding, not a license to edit.

**Fill § 3 — Actual Output.** Run or simulate the operation. Full response: status code, response body, headers, observable side effects.

**Fill § 4 — Diff.** For every element row in § 2, add its result to the Diff table. Every element must appear:
- `✓ {element} — satisfied`, or
- `F-NN — {element} — deviation (see § 5)`

Elements present in § 2 but absent from § 4 are silent omissions — the trace fails C-02 regardless of finding quality.

If no deviations: replace § 5 with `## 5. Findings — none. Contract satisfied.` Fill § 6 (all counts zero, verdict `Contract satisfied`, coverage). Skip finding instructions below.

**Fill § 5 — Findings.** For each deviation from § 4:

```
Finding F-NN
deviation: expected [X]; actual [Y] — both sides required
severity: [breaking | degraded | cosmetic]
spec: [clause from §2 that this finding violates — must match]
hypothesis: [causal mechanism — the process, mapping, serialization path, or condition that produced the wrong output; not a restatement of what differed]
recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
```

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness or consumer behavior

Include `recommendation` for `breaking` and `degraded` findings. Omit it for `cosmetic`.

**Fill § 6 — Summary.** Replace every `?` with actual values. The artifact is not complete while any `?` remains.

**Fill § 7 — Patterns.** Follow the Patterns instruction in the skeleton. This section may not be silently omitted.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Output Format: Severity-Stratified Finding Templates (C-16 isolation)

**axis:** output-format
**hypothesis:** C-16 requires three distinct finding templates — one per severity tier — where required fields within each tier are unconditionally mandatory, with no conditional language ("required if breaking"). Prior rounds use a unified finding template with conditional fields: `recommendation` is required for breaking and degraded, optional for cosmetic. A unified template allows breaking findings to omit required fields by accident: the operator reads "required if breaking," determines the severity during writing, and may fail to circle back. Stratified templates eliminate this: a BREAKING template has `recommendation` and `connector-impact` as unconditional top-level slots — the operator cannot submit the template without filling them because there is no conditional. A COSMETIC template does not have those fields; it is structurally shorter. C-15 (amendment enforcement by template structure) follows as a structural side effect of C-16: when the BREAKING template includes `recommended-action` as an unconditional labeled slot, C-15 is satisfied without additional instruction. This variation isolates C-16 without adding skeleton preamble or role-separation overhead — the rest of the prompt follows the established step-sequence baseline.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
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

### Step 2 — Expected Output (the contract)

Write the `## Expected Output` section from the spec alone. Do not run or simulate the operation before this section is complete.

For each required element:
- State the element
- Cite the spec clause that requires it

Cover all three contract surfaces:
- **Success path** — nominal input, nominal output per spec
- **Error path** — invalid or missing input, expected error response per spec
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not in the spec, write: `[surface]: not specified in spec`.

Write: `[CONTRACT COMMITTED]`

Do not proceed to Step 3 before writing this line.

---

### Step 3 — Actual Output

Run or simulate the operation. Write the `## Actual Output` section: status code, response body, headers, observable side effects.

---

### Step 4 — Diff

Write the `## Diff` section. For every element in `## Expected Output`:
- `✓ {element} — satisfied`, or
- `F-NN — {element} — deviation (see findings)`

Every element must appear. A missing element is a silent omission — the trace fails C-02 regardless of finding quality.

If no deviations: write `## Diff — Contract satisfied. No findings.` and skip to Step 6.

---

### Step 5 — Findings

**Use the matching severity tier template for each finding. Do not use a unified template.**

Identify the severity of each deviation first. Then copy the template for that tier and fill all fields. Fields in each template are unconditionally required — there are no conditional fields.

---

**BREAKING FINDING TEMPLATE**

For any finding where a consumer relying on the contract cannot function correctly.

```
Finding F-NN [BREAKING]
deviation:        expected [X]; actual [Y]
spec:             [clause from Expected Output that this finding violates]
hypothesis:       [the mechanism — name the process, mapping, or condition that caused this]
connector-impact: [what breaks for an Automate flow or Connector integration relying on this field/behavior]
recommendation:   [amend-spec | fix-impl | needs-discussion]
rationale:        [one sentence: which side of the contract is wrong and why — grounded in the hypothesis]
```

All six fields are unconditionally required for a BREAKING finding. A BREAKING block with any field blank is incomplete.

---

**DEGRADED FINDING TEMPLATE**

For any finding where the operation runs but a guarantee is violated; silent failure or data loss is possible.

```
Finding F-NN [DEGRADED]
deviation:        expected [X]; actual [Y]
spec:             [clause from Expected Output that this finding violates]
hypothesis:       [the mechanism — name the process, mapping, or condition that caused this]
connector-impact: [what silently fails or degrades for an Automate flow or Connector integration]
recommendation:   [amend-spec | fix-impl | needs-discussion]
```

All five fields are unconditionally required for a DEGRADED finding.

---

**COSMETIC FINDING TEMPLATE**

For any finding that differs from the contract without affecting correctness or consumer behavior.

```
Finding F-NN [COSMETIC]
deviation:  expected [X]; actual [Y]
spec:       [clause from Expected Output that this finding violates]
hypothesis: [the mechanism — name the process, mapping, or condition that caused this]
```

All three fields are unconditionally required for a COSMETIC finding. COSMETIC findings do not carry `recommendation`, `connector-impact`, or `rationale` — those fields belong to higher severity tiers.

---

**Hypothesis rule (applies to all tiers):** The hypothesis names a causal mechanism. It does not restate the deviation. If your hypothesis could be written without knowing anything about the system under test — only from reading the deviation line — it is a symptom restatement, not a mechanism. A valid hypothesis requires knowledge of why: what process, mapping, serialization path, or condition produced the wrong output.

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
[F-NN: amend-spec / fix-impl / needs-discussion — rationale — one line per breaking/degraded finding]

Coverage: {N} / {total in Expected Output} clauses verified, {N} deviations found
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Lifecycle Emphasis: Machine-Readable Gate Token (C-13 isolation)

**axis:** lifecycle-emphasis
**hypothesis:** C-12 (phase-gate confirmation) is satisfied by any explicit acknowledgment that expected was sealed before execution began — a prose statement like "[CONTRACT COMMITTED — no modifications after this gate]" passes C-12. C-13 escalates: the gate must use a structured, parseable marker that can be verified mechanically without reading surrounding prose. Prior rounds satisfy C-12 but not C-13 because the gate line is prose — a reader must parse it semantically to confirm the invariant. A structured token like `[EXPECTED-SEALED | clauses:N | date:YYYY-MM-DD | author:contract-expert | phase:1-complete]` is machine-verifiable: a script could extract the token, parse the clause count, confirm the date, and assert the role. The clause count embedded in the token adds a secondary invariant — the Phase 1 element count is committed at gate time, making any post-gate addition visible as a count mismatch. This variation isolates C-13 as the sole mechanism: the prompt follows the established step-sequence baseline, and the only change is replacing the prose commit gate with a structured token carrying parseable fields.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
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

Write the `## Expected Output` section from the spec alone. Do not run or simulate the operation before this section is complete.

For each required element:
- State the element
- Cite the spec clause that requires it

Cover all three contract surfaces:
- **Success path** — nominal input, nominal output per spec
- **Error path** — invalid or missing input, expected error response per spec
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not in the spec, write: `[surface]: not specified in spec`.

When Expected Output is complete, count the distinct expected elements written in this section. Write the phase gate token in the following exact format — a single line, immediately after the last expected element:

```
[EXPECTED-SEALED | clauses:{N} | date:{YYYY-MM-DD} | author:contract-expert | phase:1-complete]
```

Replace `{N}` with the count of expected elements. Replace `{YYYY-MM-DD}` with today's date. The token must appear exactly once, after the last expected element, before any actual output.

Do not run or simulate the operation before writing this token. The token asserts that Phase 1 was completed by a role that had not observed runtime output, and commits the clause count as a sealed value.

---

### Step 3 — Actual Output (Phase 3 — begins after gate token)

You begin after the `[EXPECTED-SEALED ...]` token. Do not modify the Expected Output section. Any belief that an Expected entry is incorrect is a finding — record it in Step 5, do not edit.

Run or simulate the operation. Write the `## Actual Output` section: status code, response body, headers, observable side effects.

---

### Step 4 — Diff

Write the `## Diff` section. For every element in `## Expected Output`:
- `✓ {element} — satisfied`, or
- `F-NN — {element} — deviation (see findings)`

Every element must appear. If no deviations: write `## Diff — Contract satisfied. No findings.` and skip to Step 6.

---

### Step 5 — Findings

For each deviation, write a finding entry:

```
Finding F-NN
deviation: [expected X; actual Y — both sides required]
severity:  [breaking | degraded | cosmetic]
spec:      [spec clause violated — must match a clause cited in Expected Output]
hypothesis: [the causal mechanism — name the process, mapping, serialization path, or condition that produced the wrong output; not what differed]
```

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness or consumer behavior

For every `breaking` or `degraded` finding, add:
```
recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
```

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
[F-NN: amend-spec / fix-impl / needs-discussion — rationale — one line per breaking/degraded finding]

Coverage: {N} / {total in Expected Output} clauses verified, {N} deviations found
```

After completing the Summary, write the closure token:

```
[TRACE-COMPLETE | findings:{N} | breaking:{N} | degraded:{N} | cosmetic:{N} | verdict:{violated|satisfied} | gate-clauses:{N from EXPECTED-SEALED token}]
```

The `gate-clauses` field echoes the clause count from the `[EXPECTED-SEALED]` token. If the Total clauses in Summary diverges from `gate-clauses`, note the discrepancy.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Combination: Skeleton-First + Severity-Stratified Templates (C-22 × C-16)

**axes:** output-format × output-format
**hypothesis:** V-01 establishes that skeleton-first (C-22) pre-declares document shape before Phase 1. V-02 establishes that severity-stratified templates (C-16) replace the unified finding template with three tier-specific blocks. The combination tests a specific interaction: the skeleton can pre-declare not just section headers but also the three severity-tier finding templates in their final positions, before Phase 1 begins. This means C-16's stratified architecture is visible from document open — the analyst sees the BREAKING, DEGRADED, and COSMETIC templates before writing a single expected element. The pre-declared finding templates make the tier-specific mandatory fields visible as structural obligations from the start. The hypothesis: pre-declaration of stratified templates (via C-22 skeleton) is a stronger enforcer than stratified templates introduced at the findings phase (V-02 alone), because the analyst has already "seen" the mandatory fields before the cognitive pressure of the findings phase begins.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

Before Phase 1 begins, write the following artifact skeleton. All section headers and finding templates appear below in their final positions. No section may be added, removed, or reordered after this skeleton is written.

```
## Artifact Skeleton — {topic}-contract-{date}.md

## 1. Contract Scope
- Operation: [fill — Phase 1]
- Connector / Automate context: [fill — Phase 1]
- Input fixture (inline): [fill — Phase 1]
- Spec version and section: [fill — Phase 1]

## 2. Expected Output (Phase 1 — from spec only)

### Success Path
| Element | Spec Clause |
|---------|-------------|
| [fill] | [fill] |

### Error Path
| Element | Spec Clause |
|---------|-------------|
| [fill] | [fill] |

### Edge Case: [name — fill Phase 1]
| Element | Spec Clause |
|---------|-------------|
| [fill] | [fill] |

[EXPECTED SEALED]

## 3. Actual Output (Phase 3 — after gate)
- Status code: [fill]
- Response body: [fill]
- Headers: [fill]
- Observable side effects: [fill]

## 4. Diff
| Element | Result |
|---------|--------|
| [element from §2] | ✓ satisfied / F-NN deviation |

## 5. Findings

--- BREAKING FINDING TEMPLATE (for each breaking deviation) ---

Finding F-NN [BREAKING]
deviation:        expected [X]; actual [Y]
spec:             [clause from §2]
hypothesis:       [the mechanism — causal process, mapping, or condition]
connector-impact: [what breaks for Automate flows or Connector integrations]
recommendation:   [amend-spec | fix-impl | needs-discussion]
rationale:        [which side of the contract is wrong and why — one sentence]

--- DEGRADED FINDING TEMPLATE (for each degraded deviation) ---

Finding F-NN [DEGRADED]
deviation:        expected [X]; actual [Y]
spec:             [clause from §2]
hypothesis:       [the mechanism — causal process, mapping, or condition]
connector-impact: [what silently fails or degrades]
recommendation:   [amend-spec | fix-impl | needs-discussion]

--- COSMETIC FINDING TEMPLATE (for each cosmetic deviation) ---

Finding F-NN [COSMETIC]
deviation:  expected [X]; actual [Y]
spec:       [clause from §2]
hypothesis: [the mechanism — causal process, mapping, or condition]

## 6. Summary
| Severity | Count |
|----------|-------|
| breaking | ?     |
| degraded | ?     |
| cosmetic | ?     |
| total    | ?     |

Verdict: [Contract violated / Contract satisfied]

Recommendations:
- F-NN: [amend-spec / fix-impl / needs-discussion] — [rationale]

Coverage: ? / ? clauses verified, ? deviations found

## 7. Patterns
[N ≥ 2 findings with shared root cause: name the mechanism and list grouped findings]
[N ≥ 2 but no shared root cause: "No patterns — all findings are independent"]
[N ≤ 1: omit this section]
```

The skeleton commits the document structure and finding templates. Every tier template is visible before Phase 1 begins. Fill each slot during the phase it belongs to.

---

### Phase 1 — Connectors Contract Expert

You are the Connectors contract expert. You have not run the operation. You write from the spec alone.

**Fill § 1 — Contract Scope.** Replace `[fill — Phase 1]` slots: operation name and HTTP method; connector or Automate context and environment; input fixture (inline, no file references); spec version and section.

**Fill § 2 — Expected Output.** Replace `[fill]` slots with expected elements and spec citations. Three surface blocks are required. If a surface is not in the spec, write the block heading and state: `[surface]: not specified in spec`.

An expected element without a spec citation is not a valid contract entry.

When Expected Output is complete and every element carries a spec citation, write:

`[EXPECTED SEALED — Phase 1 complete. All {N} clauses committed. Automate begins after this line.]`

Replace the `[EXPECTED SEALED]` slot in the skeleton with this line.

---

### Phase 3 — Automate

You begin after the `[EXPECTED SEALED]` token. Do not modify § 2.

**Fill § 3 — Actual Output.** Run or simulate the operation. Full response: status code, response body, headers, side effects.

**Fill § 4 — Diff.** For every element in § 2, add its result row. Every element must appear. Missing elements fail C-02.

If no deviations: replace § 5 with `## 5. Findings — none. Contract satisfied.` Fill § 6 (all counts zero, verdict `Contract satisfied`, coverage). Skip finding instructions.

**Fill § 5 — Findings.** For each deviation from § 4, select the matching severity tier template from the skeleton and fill all fields.

Field rules:
- `deviation` — both sides: what was expected and what was actual
- `spec` — must match a clause cited in § 2
- `hypothesis` — names the causal mechanism; "The output did not match" restates the deviation and is not acceptable
- `connector-impact` — present on BREAKING and DEGRADED templates; names what breaks or silently fails for Automate or Connector integrations
- `recommendation` — present on BREAKING and DEGRADED templates
- `rationale` — present on BREAKING template only; one sentence grounded in the hypothesis

**Fill § 6 — Summary.** Replace every `?`. The artifact is incomplete while any `?` remains.

**Fill § 7 — Patterns.** Follow the Patterns instruction in the skeleton. This section may not be silently omitted.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — Platinum Combination: Skeleton + Stratified Templates + Machine-Readable Gate + Per-Finding Integration (C-22 × C-16 × C-13 × C-14)

**axes:** output-format × output-format × lifecycle-emphasis × depth
**hypothesis:** Four mechanisms address four orthogonal failure modes in the trace lifecycle. The artifact skeleton (C-22) enforces document shape from document open — all sections and templates exist before writing begins. The severity-stratified templates (C-16) enforce finding field completeness by tier — no conditional fields, no per-tier amnesia. The machine-readable gate token (C-13) adds a parseable sequencing assertion to the phase boundary — clause count and role identity committed in a parseable form. Per-finding integration coverage (C-14) makes `connector-impact` a structural obligation on every finding, not an at-least-one callout. The four mechanisms are orthogonal: shape obligation operates on the document, tier structure operates on each finding block, the sequencing token operates on the phase boundary, and the integration slot operates on each finding's depth. No mechanism helps the others' failure mode; each must be present independently. The hypothesis: four non-redundant mechanisms covering four distinct failure dimensions can be simultaneously satisfied without producing cognitive overhead that regresses the essential criteria (C-01 through C-05). The skeleton pre-declares all four mechanisms before Phase 1, making every obligation visible at document open rather than encountered step by step.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

Before Phase 1 begins, write the following artifact skeleton. All section headers, templates, and gate token formats appear below in their final positions. No section may be added, removed, or reordered after the skeleton is written. The skeleton commits the complete document structure and every mandatory field obligation before the first expected element is written.

```
## Artifact Skeleton — {topic}-contract-{date}.md

## 1. Contract Scope
- Operation: [fill — Phase 1]
- Connector / Automate context: [fill — Phase 1]
- Input fixture (inline): [fill — Phase 1]
- Spec version and section: [fill — Phase 1]

## 2. Expected Output (Phase 1 — from spec only)

### Success Path
| Element | Spec Clause |
|---------|-------------|
| [fill] | [fill] |

### Error Path
| Element | Spec Clause |
|---------|-------------|
| [fill] | [fill] |

### Edge Case: [name — fill Phase 1]
| Element | Spec Clause |
|---------|-------------|
| [fill] | [fill] |

[EXPECTED-SEALED | clauses:{N} | date:{YYYY-MM-DD} | author:contract-expert | phase:1-complete]

## 3. Actual Output (Phase 3 — after gate token)
- Status code: [fill]
- Response body: [fill]
- Headers: [fill]
- Observable side effects: [fill]

## 4. Diff
| Element | Result |
|---------|--------|
| [element from §2] | ✓ satisfied / F-NN deviation |

## 5. Findings

--- BREAKING FINDING TEMPLATE ---

Finding F-NN [BREAKING]
deviation:        expected [X]; actual [Y]
spec:             [clause from §2]
hypothesis:       [the mechanism — causal process, mapping, or condition]
connector-impact: [what breaks for Automate flows or Connector integrations relying on this]
recommendation:   [amend-spec | fix-impl | needs-discussion]
rationale:        [which side of the contract is wrong and why — one sentence]

--- DEGRADED FINDING TEMPLATE ---

Finding F-NN [DEGRADED]
deviation:        expected [X]; actual [Y]
spec:             [clause from §2]
hypothesis:       [the mechanism — causal process, mapping, or condition]
connector-impact: [what silently fails or degrades — always required for DEGRADED]
recommendation:   [amend-spec | fix-impl | needs-discussion]

--- COSMETIC FINDING TEMPLATE ---

Finding F-NN [COSMETIC]
deviation:        expected [X]; actual [Y]
spec:             [clause from §2]
hypothesis:       [the mechanism — causal process, mapping, or condition]
connector-impact: [Automate / Connector integration impact, if any — write "none" if not applicable]

## 6. Summary
| Severity | Count |
|----------|-------|
| breaking | ?     |
| degraded | ?     |
| cosmetic | ?     |
| total    | ?     |

Verdict: [Contract violated / Contract satisfied]

Recommendations:
- F-NN: [amend-spec / fix-impl / needs-discussion] — [rationale]

Coverage: ? / ? clauses verified, ? deviations found

[TRACE-COMPLETE | findings:{N} | breaking:{N} | degraded:{N} | cosmetic:{N} | verdict:{violated|satisfied} | gate-clauses:{N}]

## 7. Patterns
[N ≥ 2 findings with shared root cause: name the mechanism and list grouped findings]
[N ≥ 2 but no shared root cause: "No patterns — all findings are independent"]
[N ≤ 1: omit this section]
```

The skeleton above commits the complete document shape, all finding templates, both structured tokens, and the integration-impact slot on every tier. These obligations are unconditional — they exist before Phase 1 begins.

---

### Phase 1 — Connectors Contract Expert

You are the Connectors contract expert. You have not run the operation. You write from the spec alone.

**Fill § 1 — Contract Scope.** Replace all `[fill — Phase 1]` slots with: operation name and HTTP method; connector or Automate context and environment; input fixture (inline, no file references); spec version and section.

**Fill § 2 — Expected Output.** Replace `[fill]` slots. Three surface blocks are required. If a surface is not in the spec, write the block heading and state: `[surface]: not specified in spec`. An element without a spec citation is not a valid contract entry.

Count the distinct expected elements written. When Expected Output is complete, write the phase gate token — replacing the `[EXPECTED-SEALED ...]` slot in the skeleton with:

```
[EXPECTED-SEALED | clauses:{N} | date:{YYYY-MM-DD} | author:contract-expert | phase:1-complete]
```

Where `{N}` is the count of expected elements and `{YYYY-MM-DD}` is today's date.

Do not run or simulate the operation before writing this token.

---

### Phase 3 — Automate

You begin after the `[EXPECTED-SEALED ...]` token. Do not modify § 2.

**Fill § 3 — Actual Output.** Run or simulate the operation. Full response: status code, response body, headers, side effects.

**Fill § 4 — Diff.** For every element in § 2, add its result. Every element must appear. Missing elements fail C-02.

If no deviations: replace § 5 with `## 5. Findings — none. Contract satisfied.` Fill § 6 and write the `[TRACE-COMPLETE ...]` token. Skip finding instructions.

**Fill § 5 — Findings.** For each deviation from § 4, select the matching tier template from the skeleton and fill all fields.

Field rules:
- `deviation` — both sides required: what was expected and what was actual
- `spec` — must match a clause from § 2; findings without a matched clause fail C-04
- `hypothesis` — names the causal mechanism: what process, mapping, condition, or code path produced the wrong output. "The output did not match" is a symptom restatement, not a hypothesis
- `connector-impact` — required on all three tiers in this variation; for COSMETIC findings, write "none" if no integration impact exists; do not omit the field
- `recommendation` — required on BREAKING and DEGRADED; omit on COSMETIC
- `rationale` — required on BREAKING only; one sentence grounded in the hypothesis

**Fill § 6 — Summary.** Replace every `?` with actual values.

**Write the `[TRACE-COMPLETE ...]` closure token** — replacing the token slot in the skeleton with actual values. The `gate-clauses` field echoes the clause count from the `[EXPECTED-SEALED]` token. If the verified clause count in Summary differs from `gate-clauses`, note the discrepancy.

**Fill § 7 — Patterns.** This section may not be silently omitted.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## Combination Candidates for Round 8

| Priority | Axis Combination | Primary Targets | Rationale |
|----------|-----------------|-----------------|-----------|
| 1 | V-05 (all four) + Contract Skeptic role | C-05, C-13, C-14, C-16, C-22 | V-05 covers the structural obligations; adding a Skeptic role to review hypotheses post-findings adds the semantic C-05 enforcement. Tests whether five mechanisms can coexist without essential criterion regression |
| 2 | V-04 (skeleton + stratified) + machine-readable gate (V-03) | C-13, C-16, C-22 | V-04 tested skeleton + stratified without the machine-readable gate. Adding C-13 to the V-04 combination tests whether the skeleton pre-declaration of the gate token format improves token compliance over V-03's step-embedded token instruction |
| 3 | V-02 (stratified) + pre-gate mechanism taxonomy | C-16, C-23 | V-02's stratified templates create per-tier hypothesis fields. Pre-sealing the mechanism taxonomy before the gate (C-23) constrains the vocabulary those hypothesis fields must use — vocabulary is bound before execution, not inferred post-observation |

## Evaluation Order Guidance

| Priority | Variation | Rationale |
|----------|-----------|-----------|
| 1 | V-02 (stratified templates) | C-16 is the most likely shared failing criterion across R6 leaders. Isolating it establishes the baseline contribution before combining with skeleton overhead |
| 2 | V-01 (skeleton isolation) | C-22 was already passing in R6-V-03 in combination. Isolation tests whether C-22 is achievable cheaply — if yes, it is worth including in every combination |
| 3 | V-03 (machine-readable gate) | C-13 isolation establishes whether the parseable token format is achievable without other structural overhead. Needed before combining with V-04/V-05 |
| 4 | V-04 (skeleton + stratified) | Combination of the two format mechanisms. Run after V-01 and V-02 to distinguish additive from non-additive interaction |
| 5 | V-05 (platinum) | Evaluate last — if V-02, V-01, V-03 each reliably pass in isolation, V-05 tests whether all four mechanisms are simultaneously achievable without regression |
