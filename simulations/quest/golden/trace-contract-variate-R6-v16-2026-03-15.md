# trace-contract Variate — Round 6 (rubric v16)

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v16 (C-01–C-10; essential C-01–C-05; golden threshold: all essential pass + composite >= 80)
**Round:** R6 — second pass at v16 axes; novel single-axis implementations + new combinations

---

## Round 6 Variation Map

| Variation | Axis | Primary Target | Hypothesis |
|-----------|------|----------------|------------|
| V-01 | output-format (preflight checklist) | C-01, C-09, C-10 | A visible per-criterion preflight block at the top forces the operator to consciously plan coverage before writing any content; omissions are named before they can silently occur |
| V-02 | role-sequence (Skeptic third role) | C-05 | Adding a Contract Skeptic who challenges each hypothesis forces mechanism specificity; a hypothesis that merely restates the symptom cannot survive a single "why?" |
| V-03 | lifecycle-emphasis (summary-first, fill backward) | C-09, C-10 | Writing the summary shell (counts, verdict, coverage) before the findings forces the operator to plan what they will cover; blank cells in the summary become pull-signals for missing work |
| V-04 | output-format + role-sequence (preflight + Skeptic) | C-01, C-05, C-09, C-10 | Preflight checklist catches structural gaps at write-time; Skeptic role catches hypothesis quality gaps after; the two mechanisms operate at different points in the trace lifecycle |
| V-05 | lifecycle-emphasis + inertia-framing (summary-first + cost-of-skipping) | C-08, C-09, C-10 | Summary-first makes C-09/C-10 mandatory to start; cost-of-skipping annotations at each phase make C-08's amendment recommendation feel like the payoff rather than overhead |

---

## V-01 — Output Format: Preflight Checklist Before Content

**axis:** output-format
**hypothesis:** Operators skip criteria most often when the criteria are stated in instruction prose that is read once and forgotten. A preflight checklist placed at the top of the output artifact — with one checkbox per criterion and a note that each must be ticked before the artifact is complete — makes skipped criteria visible at write time and at review time. C-01 (expected written from spec) and C-09/C-10 (summary table and coverage ratio) are most likely to benefit: C-01 because checking "I wrote expected before running" is a behavioral gate before the first keystroke of the Expected section; C-09 and C-10 because the checklist makes omitting the summary or coverage ratio a visible unchecked box rather than a missing paragraph.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### Step 0 — Preflight Checklist

Write the following block at the top of your output artifact. Fill in each item as you complete it. Do not submit the artifact with any box unchecked unless you are explicitly noting why the criterion is not applicable.

```
## Preflight Checklist

- [ ] C-01  Expected Output section written from spec before any actual output was observed
- [ ] C-02  Every expected element appears in the diff with an explicit result (✓ or finding)
- [ ] C-03  Every finding carries exactly one severity label: breaking / degraded / cosmetic
- [ ] C-04  Every finding cites a specific spec clause
- [ ] C-05  Every finding hypothesis names a mechanism, not a symptom
- [ ] C-06  Contract scope declared upfront (operation, context, input fixture, spec source)
- [ ] C-07  Three-directory layers (Input / Expected / Actual) explicitly labeled in the artifact
- [ ] C-08  Every breaking/degraded finding carries amend-spec / fix-impl / needs-discussion + rationale
- [ ] C-09  Summary table with per-severity counts and a verdict
- [ ] C-10  Coverage ratio stated (clauses checked / passed / failed)
```

Check each box as you complete the corresponding section. An unchecked box at submission is a known gap.

---

### Step 1 — Contract Scope

Write a `## Contract Scope` section. A reader must be able to determine scope from this section alone:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline — no external file references)
- Spec version and section governing this operation's output contract

Tick `C-06` in the preflight checklist.

---

### Step 2 — Expected Output (the contract)

**Before running the operation**, write the `## 20-Expected Layer` section. Derive every element from the spec. For each required element:
- State the element
- Cite the spec clause that requires it

Cover all contract surfaces the spec defines:
- **Success path** — nominal input, expected nominal output
- **Error path** — invalid or missing input, expected error response
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not defined in the spec, write: `[surface]: not specified in spec`.

**Do not run the operation before this section is complete.**

When done, write: `[CONTRACT COMMITTED]`

Tick `C-01` and `C-07 (Expected layer)` in the preflight checklist.

---

### Step 3 — Actual Output

Run or simulate the operation. Write the `## 30-Actual Layer` section: status code, response body, headers, observable side effects.

Tick `C-07 (Actual layer)` in the preflight checklist.

---

### Step 4 — Input Layer (backfill)

Write the `## 10-Input Layer` section: the setup record — what was fed in, what environment, what spec governed.

Tick `C-07 (Input layer)` in the preflight checklist.

---

### Step 5 — Diff

Write the `## Diff` section. For every element in `20-Expected Layer`, write exactly one of:
- `✓ {element} — satisfied`
- `F-NN — {element} — deviation (see findings)`

Every element must appear. Elements in Expected that are absent from the Diff are silent omissions.

If no deviations exist: write `## Diff — Contract satisfied. No findings.` and skip to Step 7.

Tick `C-02` in the preflight checklist.

---

### Step 6 — Findings

For each deviation from Step 5, write a finding entry with all four fields:

```
Finding F-NN
deviation: [expected X; actual Y — state both sides]
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated — same clause cited in 20-Expected Layer]
hypothesis: [mechanism, not symptom — names a causal process]
```

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but violates a guarantee; silent failure or data loss possible
- `cosmetic` — differs from contract in a way that does not affect correctness or consumer behavior

Tick `C-03` and `C-04` and `C-05` in the preflight checklist.

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

F-NN: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
(one recommendation line for every breaking or degraded finding)

Coverage: {N} / {total in 20-Expected Layer} clauses verified, {N} deviations found
```

Tick `C-08`, `C-09`, and `C-10` in the preflight checklist.

---

**Final step:** Review the preflight checklist. Every box must be checked. Any unchecked box is a gap in the artifact.

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Role Sequence: Contract Skeptic as Third Role

**axis:** role-sequence
**hypothesis:** C-05 fails in a predictable pattern: the hypothesis field is populated with a syntactically complete sentence that describes what happened rather than why it happened. A Connectors contract expert and Automate together do not naturally challenge each other's hypothesis quality — Automate writes findings, the expert committed the expected output, and no role is responsible for asking "what is the mechanism?" A third role — Contract Skeptic — reads the completed findings and challenges every hypothesis with a single question: "What caused this?" If the hypothesis answers that question, it passes. If it restates the deviation, the Skeptic returns the finding to Automate for rewrite. The Skeptic does not invent hypotheses; it only accepts or rejects. This models the reviewer pressure that would exist in a real two-person contract review and targets C-05 directly.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate + Contract Skeptic.

---

### ROLE: Connectors Contract Expert

You are the Connectors contract expert. You write the expected output from the spec alone. You have not run the operation. You have not observed any implementation output.

**Step 1 — Contract Scope**

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline — no external file references)
- Spec version and section governing this operation's output contract

**Step 2 — Expected Output**

Write the `## Expected Output` section from the spec alone, before any execution. For each required element, state the element and cite the spec clause. Cover all contract surfaces the spec defines:
- **Success path** — nominal input, expected nominal output
- **Error path** — invalid or missing input, expected error response
- **At least one edge case**

If a surface is not defined in the spec, write: `[surface]: not specified in spec`.

When complete, write:

`[CONTRACT COMMITTED — Automate begins here]`

Your role ends at this line.

---

### ROLE: Automate

You are Automate. The contract expert has committed the expected output. You do not revise the Expected Output section. You begin after `[CONTRACT COMMITTED]`.

**Step 3 — Actual Output**

Run or simulate the operation. Write the `## Actual Output` section: status code, full response body, headers, observable side effects.

**Step 4 — Diff**

Write the `## Diff` section. For every element in Expected Output, state one of:
- `✓ {element} — satisfied`
- `F-NN — {element} — deviation (see findings)`

Every element must appear. If no deviations: write `## Diff — Contract satisfied. No findings.` and skip to Step 6.

**Step 5 — Draft Findings**

For each deviation, write a draft finding:

```
Finding F-NN [DRAFT — awaiting Skeptic review]
deviation: [expected X; actual Y]
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated]
hypothesis: [your best hypothesis — name the mechanism]
```

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but violates a guarantee; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness

When all draft findings are written, write:

`[FINDINGS SUBMITTED TO SKEPTIC]`

Your draft phase ends here.

---

### ROLE: Contract Skeptic

You are the Contract Skeptic. You read the draft findings above. For each finding, ask exactly one question: **"What caused this?"**

If the hypothesis answers that question — it names a mechanism (a process, a mapping failure, a serialization error, a wrong default, a missing condition) — mark the finding:

```
F-NN hypothesis: ACCEPTED — [one sentence confirming the mechanism is named]
```

If the hypothesis restates the deviation ("the output did not match", "there is a mismatch", "the value is incorrect") — mark the finding:

```
F-NN hypothesis: REJECTED — symptom restatement. Return to Automate.
Skeptic note: "{quoted hypothesis}" names what differed, not why. Name the mechanism.
```

For each REJECTED finding, Automate must rewrite the hypothesis. Skeptic reviews the rewrite. This continues until all hypotheses are ACCEPTED or until two rewrites have been attempted (at which point the Skeptic marks the hypothesis `UNRESOLVED — mechanism unknown` and it remains as a finding gap).

**Step 6 — Summary**

After all hypotheses are ACCEPTED or UNRESOLVED, write the `## Summary` section:
1. Counts: `breaking: N | degraded: N | cosmetic: N | total: N`
2. Verdict: `Contract violated` or `Contract satisfied`
3. For every `breaking` or `degraded` finding:
   `F-NN: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]`
4. Coverage ratio: `{N} / {total in Expected Output} clauses verified, {N} deviations found`
5. If any hypotheses are UNRESOLVED, note: `F-NN hypothesis gap: mechanism unknown — further investigation required`

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Lifecycle Emphasis: Summary Shell Written First

**axis:** lifecycle-emphasis
**hypothesis:** C-09 (summary table) and C-10 (coverage ratio) are the most commonly skipped aspirational criteria because they require backward-looking synthesis at the end of a long trace. By requiring the operator to write the summary shell before writing any findings, the summary becomes a forward-looking plan rather than a trailing obligation. The blank severity counts become pull-signals: "I have N findings left to write before this row is accurate." The blank coverage ratio becomes a planning target: "I need to exercise at least these clause groups before I can fill this number in." Writing the shell first changes the relationship between the summary and the trace: the trace fills in the summary rather than summarizing a completed trace.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

**Write your output in this order. Do not reorder the steps.**

---

### Step 1 — Write the Summary Shell First

Before writing any expected output or running the operation, write the `## Summary` section with all fields empty or zero-filled. This is your forward-looking plan.

```
## Summary (shell — fill in as trace proceeds)

| Severity | Count |
|----------|-------|
| breaking |   ?   |
| degraded |   ?   |
| cosmetic |   ?   |
| total    |   ?   |

Verdict: [fill after diff is complete]

Recommendations: [one line per breaking/degraded finding — fill as findings are written]

Coverage: ? / ? clauses verified, ? deviations found
```

The shell tells you what the completed trace must contain. Every `?` is a gap to fill before the artifact is complete.

---

### Step 2 — Contract Scope

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline)
- Spec version and section

Self-contained — no external file references.

---

### Step 3 — Expected Output (the contract)

**Before running anything**, write the `## Expected Output` section from the spec. For each required element, state the element and cite the spec clause.

Cover all contract surfaces:
- **Success path** — nominal input → nominal output
- **Error path** — invalid or missing input → error response
- **At least one edge case**

If a surface is not in the spec, write: `[surface]: not specified in spec`.

As you write expected elements, update the coverage denominator in the Summary shell: `? / {count so far}`.

Write: `[CONTRACT COMMITTED]`

---

### Step 4 — Actual Output

Run or simulate the operation. Write the `## Actual Output` section: status code, response body, headers, side effects.

---

### Step 5 — Diff

Write the `## Diff` section. For every element in Expected Output, write:
- `✓ {element} — satisfied`
- `F-NN — {element} — deviation`

Every element must appear. If no deviations: write `## Diff — Contract satisfied. No findings.` and go to Step 7.

As you complete the diff, update the coverage numerator: `{clauses verified so far} / {total}`.

---

### Step 6 — Findings

For each deviation, write a finding entry:

```
Finding F-NN
deviation: [expected X; actual Y — state both sides]
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated]
hypothesis: [mechanism, not symptom — name the causal process]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]
(include recommendation for breaking or degraded; omit for cosmetic)
```

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness

As you write each finding, update the severity count in the Summary shell.

---

### Step 7 — Fill in the Summary

Return to the `## Summary` shell at the top of the artifact. Replace every `?` with the actual value:
- Severity counts from Step 6
- Verdict: `Contract violated` or `Contract satisfied`
- Recommendations from Step 6 (one per breaking/degraded finding)
- Coverage ratio: `{clauses verified} / {total in Expected Output} clauses verified, {N} deviations found`

The artifact is complete when no `?` remains in the Summary section.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Output Format + Role Sequence: Preflight Checklist + Contract Skeptic

**axes:** output-format + role-sequence
**hypothesis:** V-01's preflight checklist catches structural gaps before submission (C-01, C-09, C-10 are named before they can be silently omitted). V-02's Contract Skeptic catches hypothesis quality gaps after writing (C-05 hypotheses are challenged before they are locked). These two mechanisms operate at different points in the trace lifecycle: the preflight operates pre-write (planning the structure) and the Skeptic operates post-write (reviewing one specific criterion). Together they cover the full C-01–C-10 set: preflight enforces the structural criteria; Skeptic enforces the one criterion (C-05) that structural enforcement cannot catch because hypothesis quality is a semantic property, not a presence property.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate + Contract Skeptic.

---

### Step 0 — Preflight Checklist

Write the following checklist at the top of your output artifact. Tick each item as you complete the corresponding section:

```
## Preflight Checklist

- [ ] C-01  Expected written from spec before any actual output was observed
- [ ] C-02  Every expected element appears in the diff with an explicit result
- [ ] C-03  Every finding has exactly one severity label
- [ ] C-04  Every finding cites a specific spec clause
- [ ] C-05  Every finding hypothesis names a mechanism (Skeptic review required)
- [ ] C-06  Contract scope declared with operation, context, fixture, spec source
- [ ] C-07  Three-directory layers labeled in the artifact
- [ ] C-08  Every breaking/degraded finding has a recommendation
- [ ] C-09  Summary table with per-severity counts and verdict
- [ ] C-10  Coverage ratio stated
```

C-05 cannot be ticked by Automate. The Contract Skeptic ticks C-05 after reviewing all hypotheses.

---

### ROLE: Connectors Contract Expert

You are the Connectors contract expert. You write the expected output from the spec alone. You have not run the operation.

**Step 1 — Contract Scope**

Write a `## Contract Scope` section (operation, context, input fixture inline, spec source). Tick `C-06`.

**Step 2 — Expected Output**

Write the `## 20-Expected Layer` section from the spec. For each element, state the element and cite the spec clause. Cover success path, error path, and at least one edge case.

If a surface is not in the spec, write: `[surface]: not specified in spec`.

Tick `C-01` and `C-07 (Expected layer)`.

Write: `[CONTRACT COMMITTED — Automate begins here]`

---

### ROLE: Automate

You begin after `[CONTRACT COMMITTED]`. Do not modify the Expected Output section.

**Step 3 — Actual Output**

Run or simulate the operation. Write the `## 30-Actual Layer` section. Tick `C-07 (Actual layer)`.

**Step 4 — Input Layer**

Write the `## 10-Input Layer` section: the setup record. Tick `C-07 (Input layer)`.

**Step 5 — Diff**

Write the `## Diff` section. For every element in `20-Expected Layer`:
- `✓ {element} — satisfied`, or
- `F-NN — {element} — deviation`

Every element must appear. Tick `C-02`.

If no deviations: write `## Diff — Contract satisfied. No findings.` Skip to Step 7.

**Step 6 — Draft Findings**

For each deviation:

```
Finding F-NN [DRAFT]
deviation: [expected X; actual Y]
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated]
hypothesis: [your best hypothesis]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]
(recommendation required for breaking or degraded; omit for cosmetic)
```

Tick `C-03`, `C-04`, `C-08` after writing all findings.

Write: `[FINDINGS SUBMITTED TO SKEPTIC]`

Do not tick `C-05`. The Skeptic ticks it.

---

### ROLE: Contract Skeptic

You are the Contract Skeptic. Review each draft finding above.

For each finding, ask: **"What caused this?"**

If the hypothesis names a causal mechanism (process, mapping failure, serialization error, wrong default, missing condition): mark `ACCEPTED`.

If the hypothesis describes what differed without naming a cause: mark `REJECTED — symptom restatement` and note the rewrite requirement.

```
F-NN hypothesis: ACCEPTED — [one sentence confirming mechanism is named]
```
or
```
F-NN hypothesis: REJECTED — symptom restatement
Skeptic note: The hypothesis "{quoted}" states what differed. Name the mechanism that caused the difference.
```

For each REJECTED finding, Automate rewrites the hypothesis. Skeptic reviews once more. If the rewrite is still rejected, mark `UNRESOLVED — mechanism unknown`.

When all hypotheses are ACCEPTED or UNRESOLVED, tick `C-05`.

**Step 7 — Summary**

Write the `## Summary` section:

```
| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

Verdict: Contract violated / Contract satisfied
```

Recommendations (one per breaking/degraded finding):
`F-NN: [amend-spec | fix-impl | needs-discussion] — [rationale]`

Coverage: `{N} / {total in 20-Expected Layer} clauses verified, {N} deviations found`

Tick `C-09` and `C-10`.

**Final step:** Review the preflight checklist. Every box must be checked. Any unchecked box is a named gap.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — Lifecycle Emphasis + Inertia Framing: Summary-First + Cost-of-Skipping

**axes:** lifecycle-emphasis + inertia-framing
**hypothesis:** V-03's summary-first structure makes the summary and coverage ratio forward-looking obligations (blank cells pull work toward them). V-05 from R1 showed that naming what the status quo cannot do motivates each phase. Combined: writing the summary shell first makes C-09 and C-10 structural necessities rather than optional additions; annotating each phase with what is lost if it is skipped makes C-08's amendment recommendation feel like the specific payoff that the status quo permanently forfeits. The combination should reach the aspirational tier (C-09, C-10) reliably while also motivating C-08, because the "decision the status quo cannot make" annotation sits exactly at the recommendation step.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., POST /connections/trigger, GET /items/{id}}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### What this skill produces that the status quo cannot

Running the operation and deciding it looks right produces no artifact. When the output changes in the next build, there is no baseline. When a consumer reports a regression, there is no contract to diff against. When the question arises — is the spec wrong or is the implementation wrong? — there is no evidence to argue from.

This skill produces that evidence. Each phase below has exactly one thing the status quo cannot produce. Skipping a phase reverts that phase's contribution to nothing.

---

### Step 1 — Write the Summary Shell First *(locks in what you owe)*

Before writing anything else, write the `## Summary` shell:

```
## Summary (fill in as trace proceeds)

| Severity | Count |
|----------|-------|
| breaking |   ?   |
| degraded |   ?   |
| cosmetic |   ?   |
| total    |   ?   |

Verdict: [fill after diff]

Recommendations:
[F-NN: amend-spec / fix-impl / needs-discussion — rationale — one per breaking/degraded finding]

Coverage: ? / ? clauses verified, ? deviations found
```

**What the status quo loses here:** The status quo has no summary and no coverage ratio because it has no expected output. Writing this shell is the commitment to produce the artifact the status quo cannot produce. The `?` cells are debts that the trace must repay before the artifact is complete.

---

### Step 2 — Contract Scope *(improvement: the status quo has no contract — only notes)*

Write a `## Contract Scope` section:
- Operation name and method
- Connector or Automate context and environment
- Input fixture (inline)
- Spec version and section

Without this section, the trace is notes, not a contract. Notes cannot be diffed or versioned. Scope makes the contract referenceable.

---

### Step 3 — Expected Output *(improvement: the status quo runs first and makes observation the de facto contract)*

**Before running the operation**, write the `## Expected Output` section from the spec alone. For each required element:
- State the element
- Cite the spec clause that requires it

Cover all contract surfaces:
- **Success path** — nominal input → nominal output
- **Error path** — invalid or missing input → error response
- **At least one edge case** — empty collection, null required field, rate-limit trigger, auth expiry

If a surface is not in the spec, write: `[surface]: not specified in spec`.

As you write, update the coverage denominator in the Summary shell: `? / {count so far}`.

**What the status quo loses here:** Running first makes the current implementation output the de facto contract. Any deviation is invisible because it is "what the system does." Writing expected from spec first creates a contract that exists independently of what the implementation produces.

Write: `[CONTRACT COMMITTED]`

---

### Step 4 — Actual Output *(the status quo stops here)*

Run or simulate the operation. Write the `## Actual Output` section: status code, full response body, headers, observable side effects.

The status quo stops here. It has observed. It has no Phase 5.

---

### Step 5 — Diff *(improvement: the status quo has no diff because it has no expected)*

Write the `## Diff` section. For every element in Expected Output:
- `✓ {element} — satisfied`, or
- `F-NN — {element} — deviation`

Every element must appear. Elements in Expected that are absent from the Diff are silent omissions — they represent contract surfaces you observed but did not compare. The status quo produces only silent omissions.

As you complete each clause, update the coverage numerator in the Summary shell.

If no deviations: write `## Diff — Contract satisfied. No findings.` and go to Step 7.

---

### Step 6 — Classify Findings *(improvement: the status quo calls deviations "bugs" without evidence)*

For each deviation, write a finding entry:

```
Finding F-NN
deviation: [expected X; actual Y — state both sides]
severity: [breaking | degraded | cosmetic]
spec: [spec clause violated — same clause cited in Expected Output]
hypothesis: [mechanism, not symptom — name the causal process, not the observed difference]
```

Severity definitions:
- `breaking` — consumer relying on the contract cannot function correctly
- `degraded` — operation runs but a guarantee is violated; silent failure or data loss possible
- `cosmetic` — differs from contract without affecting correctness or consumer behavior

Update the severity counts in the Summary shell as you write each finding.

---

### Step 7 — Recommendations *(the decision the status quo cannot make)*

For every `breaking` or `degraded` finding, write a recommendation line in the Summary shell:

```
F-NN: [amend-spec | fix-impl | needs-discussion] — [one sentence rationale]
```

**What the status quo loses here, specifically:** Without a committed expected contract, you cannot determine whether the implementation is wrong or the spec is wrong — you can only observe that they differ. The `amend-spec` path exists only if the expected was written before the actual. This recommendation line is the payoff that the status quo permanently forfeits.

---

### Step 8 — Fill in the Summary *(evidence that you covered the contract, not just the happy path)*

Return to the `## Summary` shell. Replace every `?` with the actual value:
- Severity counts
- Verdict: `Contract violated` or `Contract satisfied`
- Recommendations (already written in Step 7)
- Coverage ratio: `{clauses verified} / {total in Expected Output} clauses verified, {N} deviations found`

**What the status quo loses here:** The coverage ratio is the evidence that you covered the contract surface rather than stopping at the success path. A status quo observation of the success path produces no number here because it has no expected output to count against. The coverage ratio distinguishes "I verified 12 of 15 contract clauses" from "I ran it and it seemed fine."

The artifact is complete when no `?` remains in the Summary section.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## Combination Candidates for Round 7

| Priority | Axis Combination | Primary Targets | Rationale |
|----------|-----------------|-----------------|-----------|
| 1 | preflight + summary-first + Skeptic (V-01+V-03+V-02) | C-01, C-05, C-09, C-10 | Triple-mechanism: preflight names all criteria; summary shell creates forward-looking counts; Skeptic enforces C-05 quality. Each mechanism targets a different failure point. |
| 2 | three-directory headings + preflight (R1-V-03 + V-01) | C-07, C-02, C-09, C-10 | Directory headings enforce C-07 structurally; preflight makes C-02 omissions visible. Candidate for determining whether V-01's checklist adds value when C-07 is already structurally enforced. |
| 3 | DO NOT gates + summary-first (R1-V-04 + V-03) | C-01, C-05, C-09, C-10 | DO NOT language targets C-01 and C-05 linguistically; summary-first targets C-09 and C-10 structurally. These operate on orthogonal criterion sets with no overlap — clean isolation of combined effect. |

## Evaluation Order Guidance

| Priority | Variation | Rationale |
|----------|-----------|-----------|
| 1 | V-03 (summary-first) | Tests C-09 and C-10 directly. If writing the shell first reliably produces a complete summary, the simplest structural change is sufficient for the aspirational tier. Establish the baseline before adding other mechanisms. |
| 2 | V-02 (Contract Skeptic) | Tests C-05 in isolation. If the Skeptic role reliably improves hypothesis quality without the preflight overhead, role addition is the minimal fix for C-05. |
| 3 | V-04 (preflight + Skeptic) | Tests V-01 and V-02 combined. Compare against each in isolation to determine whether preflight adds coverage beyond what the Skeptic already catches. |
| 4 | V-01 (preflight checklist) | Tests C-01, C-09, C-10 with minimal structural change. If V-03 already delivers C-09/C-10 reliably, V-01 tests whether the checklist adds value for C-01 specifically. |
| 5 | V-05 (summary-first + inertia-framing) | Tests whether inertia framing on top of summary-first improves C-08 specifically. Evaluate last — if V-03 delivers C-09/C-10, V-05 isolates the contribution of inertia framing to the amendment recommendation step. |
