# trace-contract Variate — Round 7 (rubric v7)

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v7 (C-01–C-27; essential C-01–C-04; aspirational denominator 20; golden threshold: all essential pass + composite >= 80)
**Round:** R7 — targeting C-24 through C-27 (four new aspirational criteria); covers all untested two-axis pairs and the all-four gold attempt

---

## Round 7 Variation Map

| Variation | Axis | Primary Target | Hypothesis |
|-----------|------|----------------|------------|
| V-01 | inertia-framing (C-27 isolation) | C-27 | C-27 was only tested in combination with C-26 (R6-V-05). Isolation reveals whether the per-phase skip-cost annotation mechanism alone elevates amend-spec adoption without the summary-shell-first structural device |
| V-02 | output-format (C-24 + C-26 co-located) | C-24, C-26 | Both are document-head format obligations. Co-locating them as a two-part obligation register tests whether mutual proximity reinforces both — checklist names the summary criteria, shell makes satisfying them feel immediate |
| V-03 | role-sequence + lifecycle-emphasis (C-25 + C-26) | C-25, C-26 | Not tested together in R6. The summary shell's forward-planning discipline may improve what Automate submits to the Skeptic; the Skeptic's verdicts should make the Recommendations section feel earned rather than mechanical |
| V-04 | output-format + role-sequence + lifecycle-emphasis (C-24 + C-25 + C-26) | C-24, C-25, C-26 | Priority-1 combination from R6 candidate list. Three mechanisms at three lifecycle points: checklist enforces coverage visibility at write-time, summary shell creates forward-counting obligations from document open, Skeptic enforces hypothesis quality post-findings |
| V-05 | all four (C-24 + C-25 + C-26 + C-27) | C-24, C-25, C-26, C-27 | Gold attempt: all four new criteria in one prompt. Tests whether the full obligation set is coherent enough to execute without the artifact becoming unparseable overhead |

---

## V-01 — Inertia-Framing: Cost-of-Skipping Annotations in Isolation

**axis:** inertia-framing
**hypothesis:** C-27 was tested in R6 only inside V-05, combined with C-26's summary-first structure. The two mechanisms were entangled — cost-of-skipping annotations appeared at each phase, but the summary shell was also there creating forward-counting pull. Isolating C-27 tests whether the annotation mechanism alone elevates amend-spec adoption. The annotation at the Step 6 recommendation point must explicitly name amend-spec as the decision the status quo permanently forfeits because it had no pre-committed expected output; that is the specific claim C-27 requires at the findings phase. If C-27 alone delivers C-08 improvement, it is a cheaper intervention than the combined V-05 structure.

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
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline — no external file references)
- Spec version and section governing this operation's output contract

**What the status quo loses here:** An informal test observation has no scope declaration. When the implementation changes, there is no record of what context the observation was made in — what environment, what input, what spec version. Without a declared scope, the trace cannot be versioned, compared across builds, or filed as evidence in a finding review.

---

### Step 2 — Expected Output (the contract)

**Before running the operation**, write the `## 20-Expected Layer` section. Derive every element from the spec. For each element:
- State the element
- Cite the spec clause that requires it

Cover all contract surfaces:
- **Success path** — nominal input, expected nominal output
- **Error path** — invalid or missing input, expected error response
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not defined in the spec, write: `[surface]: not specified in spec`.

**CONTRACT-FIRST GUARANTEE:** Do not run the operation before this section is complete.

When done, write: `[CONTRACT COMMITTED]`
Then attest: `I have not referenced any actual output in writing the Expected section.`

**What the status quo loses here:** Running the operation first makes the current implementation output the de facto contract. Any deviation becomes invisible because "that's what it does." Writing Expected from spec first creates a contract that exists independently of what the implementation currently produces — the necessary precondition for the `amend-spec` classification to mean anything.

---

### Step 3 — Actual Output

Run or simulate the operation. Write the `## 30-Actual Layer` section: status code, full response body, headers, observable side effects.

Record without modification. When done, write: `[ACTUAL OUTPUT RECORDED — no fields modified or omitted]`

---

### Step 4 — Input Layer

Write the `## 10-Input Layer` section: setup record — what was fed in, what environment, what spec governed.

---

### Step 5 — Diff

Write the `## Diff` section. For every element in `20-Expected Layer`, write exactly one of:
- `✓ {element} — satisfied`
- `F-NN — {element} — deviation (see findings)`

**POST-TABLE PROSE PROHIBITION:** Every element must appear. Elements present in Expected but absent from Diff are silent omissions — contract surfaces you observed but did not compare.

Write: `[DIFF COMPLETE — every expected element has an explicit result]`

If no deviations: write `## Diff — Contract satisfied. No findings.` and skip to Step 7.

**What the status quo loses here:** The diff is the per-field delta between what the spec required and what the implementation produced. The status quo has no Expected layer to diff against. It can observe that something looks wrong; it cannot state which specific contract clause was violated or what the expected value was. The per-field comparison is the record that makes regression detection possible when the implementation changes next sprint.

---

### Step 6 — Findings

For each deviation from Step 5, write a finding block with all fields together:

```
Finding F-NN
deviation: [expected X; actual Y — state both sides explicitly]
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated — same clause cited in 20-Expected Layer]
Connectors classification: [structural schema violation | behavioral contract violation]
hypothesis: [mechanism, not symptom — name the causal process, not the observed difference]
Automate review: [confirm the classification; note if this breaks a downstream flow or consumer]
recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
(recommendation required for breaking or degraded; omit for cosmetic)
```

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness or consumer behavior

Connectors Expert classifies structural vs. behavioral first. Automate reviews every breaking finding after. This sequence is declared here and is not left to author judgment.

**What the status quo loses here, specifically:** Without a pre-committed expected output, you cannot determine whether the implementation is wrong or the spec is wrong — you can only observe that they differ. The `amend-spec` path exists only if the expected was written before the actual was observed. The three-way recommendation classification (amend-spec / fix-impl / needs-discussion) is the decision the status quo permanently forfeits because it had no pre-committed expected output to argue from.

---

### Step 7 — Summary

Write the `## Summary` section:

```
| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

Verdict: Contract violated / Contract satisfied

Recommendations (one per breaking/degraded finding):
F-NN: [amend-spec | fix-impl | needs-discussion] — [rationale]

Coverage: {N} / {total in 20-Expected Layer} clauses verified, {N} deviations found
```

**What the status quo loses here:** The coverage ratio is evidence that you covered the full contract surface rather than stopping at the happy path. The status quo produces no such number. "I ran it and it worked" cannot be compared across versions, cannot distinguish "I checked the success path only" from "I checked all 15 contract clauses." "I verified 12 of 15 clauses, 2 deviations found" is a completeness claim the status quo is structurally unable to make.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Output Format: Preflight Checklist + Summary Shell Co-located at Document Head

**axis:** output-format (C-24 + C-26 as unified obligation register)
**hypothesis:** C-24 (preflight checklist) and C-26 (summary shell) are both format criteria that operate at document head before any content section is written. Tested individually in R6 (V-01 and V-03), each was effective at making its target criterion visible, but they never appeared together. Co-locating them as two adjacent obligations in a single "obligation register" block creates mutual reinforcement: the checklist names C-09 and C-10 by criterion number and points directly to the shell below; the shell makes satisfying those criteria feel immediate (fill in the count) rather than abstract (remember to write a summary later). A reader checking the artifact before submission sees both obligations in one scan.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### Step 0 — Obligation Register (write this before any contract content)

Before writing any contract scope, expected output, or actual output, write the following two-part block at the top of the artifact.

**Part A — Preflight Checklist**

```
## Preflight Checklist

- [ ] C-01  Expected Output section written from spec before any actual output was observed
- [ ] C-02  Every expected element appears in the diff (check or F-NN — no silent omissions)
- [ ] C-03  Every finding carries exactly one severity label: breaking / degraded / cosmetic
- [ ] C-04  Every finding cites a specific spec clause
- [ ] C-05  Every finding hypothesis names a causal mechanism, not a symptom
- [ ] C-06  Contract scope declared (operation, context, input fixture inline, spec source)
- [ ] C-07  Three-directory layers (10-Input / 20-Expected / 30-Actual) explicitly labeled
- [ ] C-08  Every breaking/degraded finding carries a recommendation (amend-spec / fix-impl / needs-discussion)
- [ ] C-09  Summary table with per-severity counts and verdict — see Part B below
- [ ] C-10  Coverage ratio stated — see Part B below
```

Tick each box as you complete the corresponding section. An unchecked box at submission is a named visible gap, not a silent omission.

**Part B — Summary Shell**

Immediately after the checklist, write the summary shell:

```
## Summary (forward plan — fill in as trace proceeds)

| Severity | Count |
|----------|-------|
| breaking |   ?   |
| degraded |   ?   |
| cosmetic |   ?   |
| total    |   ?   |

Verdict: [fill after diff is complete]

Recommendations:
[F-NN: amend-spec / fix-impl / needs-discussion — rationale]
[fill here as findings are written — one line per breaking/degraded finding]

Coverage: ? / ? clauses verified, ? deviations found
```

Incremental fill instructions:
- **After Step 2 (Expected):** update the coverage denominator (`? / {count of expected elements}`)
- **After Step 5 (Diff):** update the coverage numerator (`{clauses verified} / {total}`)
- **After Step 6 (Findings):** update each severity count row and add recommendation lines
- **After Step 7:** set Verdict; confirm no `?` remains

The artifact is complete when no `?` remains in the Summary shell.

---

### Step 1 — Contract Scope

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline — no external file references)
- Spec version and section governing this operation's output contract

Tick `C-06` in the preflight checklist.

---

### Step 2 — Expected Output (the contract)

**Before running the operation**, write the `## 20-Expected Layer` section. Derive every element from the spec. For each element:
- State the element
- Cite the spec clause that requires it

Cover all contract surfaces:
- **Success path** — nominal input, expected nominal output
- **Error path** — invalid or missing input, expected error response
- **At least one edge case**

If a surface is not defined in the spec, write: `[surface]: not specified in spec`.

As you write expected elements, update the coverage denominator in the Summary shell: replace `? / ?` with `? / {count so far}`.

**CONTRACT-FIRST GUARANTEE:** Do not run the operation before this section is complete.

When done, write: `[CONTRACT COMMITTED]`
Attest: `I have not referenced any actual output.`

Tick `C-01` and `C-07 (Expected layer)` in the preflight checklist.

---

### Step 3 — Actual Output

Run or simulate the operation. Write the `## 30-Actual Layer` section: status code, response body, headers, side effects.

Write: `[ACTUAL OUTPUT RECORDED]`

Tick `C-07 (Actual layer)`.

---

### Step 4 — Input Layer

Write the `## 10-Input Layer` section: setup record — input, environment, spec.

Tick `C-07 (Input layer)`.

---

### Step 5 — Diff

Write the `## Diff` section. For every element in `20-Expected Layer`:
- `check {element} — satisfied`
- `F-NN — {element} — deviation (see findings)`

Every element must appear. Elements in Expected absent from Diff are silent omissions.

As you complete the diff, update the coverage numerator in the Summary shell.

Write: `[DIFF COMPLETE]`

Tick `C-02`.

If no deviations: write `## Diff — Contract satisfied. No findings.` and go to Step 7.

---

### Step 6 — Findings

For each deviation, write a finding block with all fields together (no field may be omitted):

```
Finding F-NN
deviation: [expected X; actual Y — both sides explicit]
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated — same clause cited in 20-Expected Layer]
Connectors classification: [structural schema violation | behavioral contract violation]
hypothesis: [mechanism, not symptom — name the causal process]
Automate review: [confirm classification; note downstream consumer impact if breaking]
recommendation: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
(recommendation required for breaking or degraded; omit for cosmetic)
```

Severity:
- `breaking` — consumer cannot function correctly
- `degraded` — guarantee violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness

Connectors Expert classifies structural vs. behavioral first. Automate reviews each breaking finding after.

As you write each finding, update the severity count row in the Summary shell and add the recommendation line.

Tick `C-03`, `C-04`, `C-05`, `C-08` in the preflight checklist.

---

### Step 7 — Complete the Summary

Return to the `## Summary` shell at the top of the artifact. Replace every `?` with its actual value:
- Severity counts from Step 6
- Verdict: `Contract violated` or `Contract satisfied`
- Recommendations (one per breaking/degraded finding — already written in Step 6 blocks)
- Coverage: `{verified} / {total in 20-Expected Layer} clauses verified, {N} deviations found`

Tick `C-09` and `C-10` in the preflight checklist.

**Final step:** Review the preflight checklist. Every box must be ticked. An unchecked box is a named gap.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Role Sequence + Lifecycle Emphasis: Skeptic + Summary-First (untested pair)

**axis:** role-sequence + lifecycle-emphasis
**hypothesis:** C-25 (Contract Skeptic) and C-26 (summary-first) were never tested together in R6. The Skeptic operates post-findings; the summary shell operates pre-content. Combining them tests a lifecycle claim: the forward-planning discipline imposed by writing the summary shell first should produce more deliberate Automate draft findings — because Automate can see the blank severity counts in the shell and knows what it owes — and the Skeptic's per-hypothesis verdicts should make the Recommendations section feel earned rather than mechanical, since each recommendation only finalizes after its hypothesis passes ACCEPTED. Testing without a preflight checklist isolates the combined contribution of these two mechanisms from the document-head format effect of C-24.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate + Contract Skeptic.

**Write your output in this exact order. Do not reorder steps.**

---

### Step 1 — Write the Summary Shell First

Before writing any contract content, write the `## Summary` shell with placeholder cells. This is your forward-looking plan.

```
## Summary (forward plan — fill in as trace proceeds)

| Severity | Count |
|----------|-------|
| breaking |   ?   |
| degraded |   ?   |
| cosmetic |   ?   |
| total    |   ?   |

Verdict: [fill after diff is complete]

Recommendations:
[F-NN: amend-spec / fix-impl / needs-discussion — rationale]
[fill here as findings are written; Skeptic may amend after hypothesis review]

Coverage: ? / ? clauses verified, ? deviations found
```

Every `?` is a gap to fill before the artifact is complete. The artifact is complete when no `?` remains.

---

### ROLE: Connectors Contract Expert

You are the Connectors contract expert. You have not run the operation. You have not observed any implementation output.

**Step 2 — Contract Scope**

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline — no external file references)
- Spec version and section

**Step 3 — Expected Output**

**Before running the operation**, write the `## 20-Expected Layer` from the spec alone. For each element:
- State the element
- Cite the spec clause that requires it

Cover all contract surfaces:
- **Success path** — nominal input → nominal output
- **Error path** — invalid or missing input → error response
- **At least one edge case**

If a surface is not in the spec, write: `[surface]: not specified in spec`.

As you write, update the coverage denominator in the Summary shell: `? / {count so far}`.

When complete, write:
`[CONTRACT COMMITTED — Automate begins here]`
`I have not referenced any actual output.`

Your role ends at this line.

---

### ROLE: Automate

You begin after `[CONTRACT COMMITTED]`. Do not modify the 20-Expected Layer.

**Step 4 — Actual Output**

Run or simulate the operation. Write the `## 30-Actual Layer`: status code, response body, headers, side effects.

Write: `[ACTUAL OUTPUT RECORDED — no fields modified or omitted]`

**Step 5 — Input Layer**

Write the `## 10-Input Layer`: setup record — input, environment, spec.

**Step 6 — Diff**

Write the `## Diff` section. For every element in `20-Expected Layer`:
- `check {element} — satisfied`
- `F-NN — {element} — deviation (see findings)`

Every element must appear. Update the coverage numerator in the Summary shell as you proceed.

Write: `[DIFF COMPLETE]`

If no deviations: write `## Diff — Contract satisfied. No findings.` and go to Step 9.

**Step 7 — Draft Findings**

For each deviation, write a draft finding:

```
Finding F-NN [DRAFT — awaiting Skeptic review]
deviation: [expected X; actual Y — both sides explicit]
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated — same clause cited in 20-Expected Layer]
Connectors classification: [structural schema violation | behavioral contract violation]
hypothesis: [your best hypothesis — name the mechanism, not the symptom]
Automate review: [confirm classification; note downstream consumer impact if breaking]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]
(recommendation required for breaking or degraded; omit for cosmetic)
```

Severity:
- `breaking` — consumer cannot function correctly
- `degraded` — guarantee violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness

Connectors Expert classifies structural vs. behavioral first. Automate reviews breaking findings after.

As you write each finding, update the severity count rows in the Summary shell and add a recommendation line.

Write: `[FINDINGS SUBMITTED TO SKEPTIC]`

---

### ROLE: Contract Skeptic

You are the Contract Skeptic. Read the draft findings above. For each, apply one test: **"What caused this?"**

If the hypothesis names a causal mechanism — a process, a mapping failure, a serialization error, a wrong default, a missing condition — mark:

```
F-NN hypothesis: ACCEPTED — [one sentence confirming the mechanism is named]
```

If the hypothesis restates the deviation — "the output did not match," "the value is incorrect," "there is a mismatch" — mark:

```
F-NN hypothesis: REJECTED — symptom restatement. Return to Automate.
Skeptic note: "{quoted hypothesis}" states what differed, not why. Name the mechanism that caused the difference.
```

For each REJECTED finding, Automate rewrites the hypothesis. Skeptic reviews the rewrite. If the rewrite is still rejected, mark:

```
F-NN hypothesis: UNRESOLVED — mechanism unknown. Gap noted.
```

**Step 8 — Skeptic completes the Summary**

After all hypotheses are ACCEPTED or UNRESOLVED, fill every `?` in the Summary shell:
- Severity counts (from Step 7 draft findings)
- Verdict: `Contract violated` or `Contract satisfied`
- Recommendations: one line per breaking/degraded finding (from Step 7, updated if hypotheses were rewritten)
- Coverage: `{verified} / {total in 20-Expected Layer} clauses verified, {N} deviations found`

If any hypotheses are UNRESOLVED, append:
`F-NN hypothesis gap: mechanism unknown — further investigation required`

The artifact is complete when no `?` remains in the Summary section.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Triple: Preflight Checklist + Contract Skeptic + Summary-First (C-24 + C-25 + C-26)

**axes:** output-format + role-sequence + lifecycle-emphasis
**hypothesis:** This is the priority-1 combination from the R6 candidate list. Three mechanisms, three lifecycle points, three distinct failure modes addressed: the preflight checklist (C-24) makes criterion gaps visible at write-time — named boxes cannot become silent omissions; the summary shell (C-26) creates forward-counting obligations from document open — blank cells pull work toward them before a single finding is written; the Contract Skeptic (C-25) enforces the one criterion (C-05) that structural mechanisms cannot enforce because hypothesis quality is semantic, not structural. C-05 is Skeptic-gated in the preflight checklist — Automate cannot self-tick it. Together these should reach Gold by eliminating the three most common failure modes simultaneously without the inertia-framing overhead of C-27.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate + Contract Skeptic.

**Write output in this exact order. Do not reorder steps.**

---

### Step 0 — Obligation Register (write before any contract content)

**Part A — Preflight Checklist**

```
## Preflight Checklist

- [ ] C-01  Expected written from spec before any actual output was observed
- [ ] C-02  Every expected element in diff (check or F-NN — no silent omissions)
- [ ] C-03  Every finding has exactly one severity label: breaking / degraded / cosmetic
- [ ] C-04  Every finding cites a specific spec clause
- [ ] C-05  Every hypothesis names a causal mechanism — SKEPTIC-GATED (Automate cannot self-tick)
- [ ] C-06  Contract scope declared (operation, context, input fixture inline, spec source)
- [ ] C-07  Three-directory layers (10-Input / 20-Expected / 30-Actual) labeled
- [ ] C-08  Every breaking/degraded finding carries a recommendation
- [ ] C-09  Summary table with per-severity counts and verdict — see Part B
- [ ] C-10  Coverage ratio stated — see Part B
```

**C-05 is Skeptic-gated.** Only the Contract Skeptic ticks it, after reviewing all hypotheses. If Automate ticks C-05, the checklist is invalid.

**Part B — Summary Shell**

```
## Summary (forward plan — fill incrementally; no ? at submission)

| Severity | Count |
|----------|-------|
| breaking |   ?   |
| degraded |   ?   |
| cosmetic |   ?   |
| total    |   ?   |

Verdict: [fill after diff is complete]

Recommendations:
[F-NN: amend-spec / fix-impl / needs-discussion — rationale]
[add here as findings are written; Skeptic may amend after hypothesis review]

Coverage: ? / ? clauses verified, ? deviations found
```

Update rules:
- **During Step 3 (Expected):** set denominator (`? / {N}`)
- **During Step 6 (Diff):** set numerator (`{verified} / N`)
- **During Step 7 (Findings):** update severity counts + add recommendation lines
- **After Step 9 (Skeptic):** set Verdict; confirm no `?` remains

The artifact is complete when no `?` remains in the Summary shell.

---

### ROLE: Connectors Contract Expert

You are the Connectors contract expert. You have not run the operation.

**Step 1 — Contract Scope**

Write a `## Contract Scope` section: operation, context, input fixture (inline), spec source.

State role-firing order:
```
role_order: connectors-first
Connectors Expert writes expected output and classifies deviations (structural vs. behavioral).
Automate reviews every breaking finding after Connectors classification.
Contract Skeptic reviews all hypotheses after Automate draft findings are complete.
```

Tick `C-06`.

**Step 2 — Expected Output**

Write the `## 20-Expected Layer` from the spec alone. For each element:
- State the element
- Cite the spec clause

Cover: success path, error path, and at least one edge case. If a surface is absent from spec, write: `[surface]: not specified in spec`.

As you write, update the coverage denominator in the Summary shell.

Tick `C-01` and `C-07 (Expected layer)`.

When done, write:
`[CONTRACT COMMITTED — PHASE 2 CLOSE. DO NOT RUN THE OPERATION BEFORE THIS MARKER.]`
`I have not referenced any actual output.`

Your role ends here.

---

### ROLE: Automate

You begin after `[CONTRACT COMMITTED]`. Do not modify the 20-Expected Layer.

**Step 3 — Actual Output**

Run or simulate the operation. Write the `## 30-Actual Layer`: status code, response body, headers, side effects.

Write: `[ACTUAL OUTPUT RECORDED — no fields modified or omitted]`

Tick `C-07 (Actual layer)`.

**Step 4 — Input Layer**

Write the `## 10-Input Layer`: setup record.

Tick `C-07 (Input layer)`.

**Step 5 — Diff**

Write the `## Diff` section. For every element in `20-Expected Layer`:
- `check {element} — satisfied`
- `F-NN — {element} — deviation (see findings)`

**POST-TABLE PROSE PROHIBITION:** Every element must appear. Do not add prose findings outside the comparison entries.

Update the coverage numerator in the Summary shell.

Write: `[DIFF COMPLETE — every expected element has an explicit result]`

Tick `C-02`.

If no deviations: write `## Diff — Contract satisfied. No findings.` and skip to Step 9.

**Step 6 — Role Severity Review**

If you assign a different severity than Connectors Expert on any finding, add:
```
CONTRACT AMBIGUITY — F-NN: Connectors Expert: {severity}; Automate: {severity}. Requires: {what evidence or spec clarification would resolve}.
```

**Step 7 — Draft Findings**

For each deviation, write a complete finding block (all five fields required together — a block missing any field does not qualify):

```
Finding F-NN [DRAFT]
deviation: [expected X; actual Y — both sides explicit]
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated — same clause cited in 20-Expected Layer]
Connectors classification: [structural schema violation | behavioral contract violation]
hypothesis: [your best hypothesis — mechanism, not symptom]
Automate review: [confirm classification; note consumer impact if breaking]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]
(recommendation required for breaking or degraded; omit for cosmetic)
```

Severity:
- `breaking` — consumer cannot function correctly
- `degraded` — guarantee violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness

As you write each finding, update severity counts and add a recommendation line in the Summary shell.

Tick `C-03`, `C-04`, `C-08`.

**Do not tick C-05.** Write: `[FINDINGS SUBMITTED TO SKEPTIC]`

---

### ROLE: Contract Skeptic

You are the Contract Skeptic. Read the draft findings. For each, apply one test: **"What caused this?"**

If the hypothesis names a mechanism:
```
F-NN hypothesis: ACCEPTED — [one sentence confirming mechanism is named]
```

If the hypothesis restates the deviation:
```
F-NN hypothesis: REJECTED — symptom restatement
Skeptic note: "{quoted}" names what differed. Name the causal mechanism — a process, a mapping failure, a wrong default, a missing condition.
```

Automate rewrites each REJECTED hypothesis. Skeptic reviews the rewrite. If still rejected:
```
F-NN hypothesis: UNRESOLVED — mechanism unknown. Gap noted.
```

**Step 8 — Skeptic completes**

After all hypotheses are ACCEPTED or UNRESOLVED, tick `C-05` in the preflight checklist.

**Step 9 — Summary**

Fill every `?` in the Summary shell:
- Severity counts
- Verdict: `Contract violated` or `Contract satisfied`
- Recommendations (one per breaking/degraded finding; amend if hypotheses were rewritten)
- Coverage: `{verified} / {total in 20-Expected Layer} clauses verified, {N} deviations found`

Note any UNRESOLVED hypotheses: `F-NN hypothesis gap: mechanism unknown — further investigation required`

Tick `C-09` and `C-10`.

**Final step:** Review the preflight checklist. Every box must be ticked. An unchecked box at submission is a named gap in the artifact.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — All Four: Preflight + Skeptic + Summary-First + Cost-of-Skipping (C-24 + C-25 + C-26 + C-27)

**axes:** output-format + role-sequence + lifecycle-emphasis + inertia-framing
**hypothesis:** The four new criteria form a coherent set addressing four distinct failure modes: C-24 (checklist) makes criterion gaps visible before they become silent omissions; C-26 (summary shell) converts the summary from a retrospective obligation into a forward-planning scaffold; C-27 (skip-cost annotations) names at each phase what unique evidentiary value that phase produces that the status quo permanently forfeits; C-25 (Skeptic) enforces the one semantic quality that structural mechanisms cannot enforce. The claim is that these four mechanisms do not crowd each other out — they operate at write-time (C-24, C-26), at each phase boundary (C-27), and post-draft (C-25) — and their combination should produce a Gold-band artifact where each mechanism handles exactly the failure mode it was designed for.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate + Contract Skeptic.

**Write output in this exact order. Do not reorder steps.**

---

### Step 0 — Obligation Register (write before any contract content)

**Part A — Preflight Checklist**

```
## Preflight Checklist

- [ ] C-01  Expected Output written from spec before any actual output was observed
- [ ] C-02  Every expected element in diff (check or F-NN — no silent omissions)
- [ ] C-03  Every finding carries exactly one severity label: breaking / degraded / cosmetic
- [ ] C-04  Every finding cites a specific spec clause
- [ ] C-05  Every hypothesis names a causal mechanism — SKEPTIC-GATED (Automate cannot self-tick)
- [ ] C-06  Contract scope declared (operation, context, input fixture inline, spec source)
- [ ] C-07  Three-directory layers (10-Input / 20-Expected / 30-Actual) explicitly labeled
- [ ] C-08  Every breaking/degraded finding carries a recommendation
- [ ] C-09  Summary table with per-severity counts and verdict — see Part B
- [ ] C-10  Coverage ratio stated — see Part B
```

**C-05 is Skeptic-gated.** Only the Contract Skeptic ticks it. Automate must not self-tick C-05.

**Part B — Summary Shell**

```
## Summary (forward plan — fill incrementally; no ? at submission)

| Severity | Count |
|----------|-------|
| breaking |   ?   |
| degraded |   ?   |
| cosmetic |   ?   |
| total    |   ?   |

Verdict: [fill after diff is complete]

Recommendations:
[F-NN: amend-spec / fix-impl / needs-discussion — rationale]
[add here as findings are written; Skeptic may amend after hypothesis review]

Coverage: ? / ? clauses verified, ? deviations found
```

Update rules:
- **During Step 2 (Expected):** set denominator (`? / {N}`)
- **During Step 5 (Diff):** set numerator (`{verified} / N`)
- **During Step 6 (Findings):** update severity counts + add recommendation lines
- **After Step 8 (Skeptic):** set Verdict; confirm no `?` remains

The artifact is complete when no `?` remains.

---

### ROLE: Connectors Contract Expert

**Step 1 — Contract Scope**

Write a `## Contract Scope` section: operation, context, input fixture (inline), spec source.

State role-firing order: `Connectors Expert → Automate → Contract Skeptic`

Tick `C-06`.

**What the status quo loses here:** An informal observation has no scope. When the implementation changes, there is no record of what context, environment, or spec version the observation was made in. Without a declared scope this trace cannot be versioned, replayed, or filed as evidence.

**Step 2 — Expected Output**

Write the `## 20-Expected Layer` from the spec alone. For each element:
- State the element
- Cite the spec clause

Cover: success path, error path, and at least one edge case. If a surface is absent from spec, write: `[surface]: not specified in spec`.

As you write, update the coverage denominator in the Summary shell.

**What the status quo loses here:** Running the operation first makes the current implementation the de facto contract. Any deviation becomes invisible — "that's what it does." Writing Expected from spec first creates a contract that exists independently of the implementation's current output. Without this document, the `amend-spec` classification cannot be meaningful — there is nothing to amend against.

Tick `C-01` and `C-07 (Expected layer)`.

When done:
`[CONTRACT COMMITTED — PHASE 2 CLOSE. DO NOT RUN THE OPERATION BEFORE THIS MARKER.]`
`I have not referenced any actual output.`

---

### ROLE: Automate

You begin after `[CONTRACT COMMITTED]`. Do not modify the 20-Expected Layer.

**Step 3 — Actual Output**

Run or simulate the operation. Write the `## 30-Actual Layer`: status code, response body, headers, side effects.

Write: `[ACTUAL OUTPUT RECORDED — no fields modified or omitted]`

Tick `C-07 (Actual layer)`.

**Step 4 — Input Layer**

Write the `## 10-Input Layer`: setup record — input, environment, spec.

Tick `C-07 (Input layer)`.

**Step 5 — Diff**

Write the `## Diff` section. For every element in `20-Expected Layer`:
- `check {element} — satisfied`
- `F-NN — {element} — deviation (see findings)`

**POST-TABLE PROSE PROHIBITION:** Every element must appear. No prose findings outside the comparison entries.

Update the coverage numerator in the Summary shell as you proceed.

Write: `[DIFF COMPLETE — every expected element has an explicit result]`

Tick `C-02`.

If no deviations: write `## Diff — Contract satisfied. No findings.` and skip to Step 8.

**What the status quo loses here:** The per-field diff is the record that makes regression detection possible. The status quo has no Expected layer to diff against — it can only say "something looks wrong." The diff is the first artifact in this trace that could not exist without a pre-committed expected output.

**Step 6 — Draft Findings**

For each deviation, write a complete finding block (all fields required together — a block missing any field does not qualify):

```
Finding F-NN [DRAFT]
deviation: [expected X; actual Y — both sides explicit]
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated — same clause cited in 20-Expected Layer]
Connectors classification: [structural schema violation | behavioral contract violation]
hypothesis: [mechanism, not symptom — name the causal process]
Automate review: [confirm classification; note consumer impact if breaking]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]
(recommendation required for breaking or degraded; omit for cosmetic)
```

Severity:
- `breaking` — consumer cannot function correctly
- `degraded` — guarantee violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness

Connectors Expert classifies structural vs. behavioral first. Automate reviews every breaking finding after. If you assign a different severity than Connectors Expert, add:
```
CONTRACT AMBIGUITY — F-NN: Connectors Expert: {severity}; Automate: {severity}. Requires: {spec clarification or additional evidence needed to resolve}.
```

As you write each finding, update the severity counts in the Summary shell and add a recommendation line.

Tick `C-03`, `C-04`, `C-08`.

**Do not tick C-05.**

**What the status quo loses here, specifically:** Without a pre-committed expected output, you cannot determine whether the implementation is wrong or the spec is wrong — you can only observe that they differ. The `amend-spec` path is the decision the status quo permanently forfeits because it had no contract to argue from. The three-way classification (amend-spec / fix-impl / needs-discussion) is only meaningful when the expected was written before the actual was observed.

Write: `[FINDINGS SUBMITTED TO SKEPTIC]`

---

### ROLE: Contract Skeptic

You are the Contract Skeptic. Read the draft findings. For each, apply one test: **"What caused this?"**

If the hypothesis names a causal mechanism — a process, a mapping failure, a serialization error, a wrong default, a missing condition:
```
F-NN hypothesis: ACCEPTED — [one sentence confirming mechanism is named]
```

If the hypothesis restates the deviation — "the output did not match," "the value is incorrect," "there is a mismatch":
```
F-NN hypothesis: REJECTED — symptom restatement
Skeptic note: "{quoted}" names what differed. Rewrite to name the causal mechanism.
```

Automate rewrites each REJECTED hypothesis. Skeptic reviews the rewrite. If still rejected:
```
F-NN hypothesis: UNRESOLVED — mechanism unknown. Gap noted.
```

**Step 7 — Skeptic completes**

After all hypotheses are ACCEPTED or UNRESOLVED, tick `C-05` in the preflight checklist.

**Step 8 — Summary**

Fill every `?` in the Summary shell:
- Severity counts
- Verdict: `Contract violated` or `Contract satisfied`
- Recommendations (one per breaking/degraded finding; amend if hypotheses were rewritten during Skeptic review)
- Coverage: `{verified} / {total in 20-Expected Layer} clauses verified, {N} deviations found`

Note any UNRESOLVED hypotheses: `F-NN hypothesis gap: mechanism unknown — further investigation required`

**What the status quo loses here:** The coverage ratio is the completeness claim the status quo cannot make. "I verified 12 of 15 contract clauses, 2 deviations found" is a specific, checkable claim. "I ran it and it seemed fine" is not. The ratio distinguishes deliberate contract coverage from happy-path observation — and it is only computable because the Expected layer enumerated the clauses before the operation ran.

Tick `C-09` and `C-10`.

**Final step:** Review the preflight checklist. Every box must be ticked. An unchecked box is a named gap in the artifact.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## Evaluation Order Guidance for R7

| Priority | Variation | Rationale |
|----------|-----------|-----------|
| 1 | V-01 (C-27 isolation) | Fills the last single-axis gap. If C-27 alone delivers C-08 improvement, it is the cheapest intervention. Baseline before combining. |
| 2 | V-02 (C-24 + C-26) | Tests the two format-head criteria together without Skeptic complexity. Determines whether co-location reinforces both or one crowds out the other. |
| 3 | V-03 (C-25 + C-26) | Tests the untested Skeptic + summary-first pair. Determines whether forward-planning discipline improves what the Skeptic receives. |
| 4 | V-04 (C-24 + C-25 + C-26) | Triple combination. Compare against V-02 and V-03 individually — does the checklist add value when the Skeptic is already enforcing C-05? |
| 5 | V-05 (all four) | Gold attempt. Evaluate last — only attempt all-four once V-01 through V-04 establish which mechanisms are load-bearing. |

## Combination Candidates for Round 8

| Priority | Axis Combination | Primary Targets | Rationale |
|----------|-----------------|-----------------|-----------|
| 1 | V-05 + C-18 (multi-phase attestation chain) | C-24–C-27, C-18 | If V-05 reaches Gold, R8 tests whether adding C-18's two additional author-voiced attestations closes the remaining honor-system gaps at Phase 2 and Phase 3 boundaries without disrupting V-05's four-mechanism structure |
| 2 | V-04 + C-22 (columnar table enforcement) | C-24, C-25, C-26, C-22 | C-22 requires named columns (Severity, Spec Clause, Hypothesis, role fields); combined with V-04's triple mechanism, tests whether table-column enforcement catches field omissions that C-20's complete-block template misses |
| 3 | V-05 + C-14 + C-19 (frontmatter role_order + phase bookends) | C-24–C-27, C-14, C-19 | C-14 (frontmatter role_order) and C-19 (symmetric PHASE N OPEN/CLOSE bookends) are machine-readable structural criteria; adding them to V-05 tests whether the full aspirational set can coexist in one coherent artifact |
