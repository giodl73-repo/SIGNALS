## file-issue -- Round 6 Variations

**Rubric**: v6 (C-01 through C-19)
**Scoring target**: 12/12 aspirational = 100.00
**Context**: Round 5 V-04 achieved all 12 criteria (100.00) under v6, including both new criteria
C-18 and C-19. Round 5 V-05 achieved 11/12 -- failing only C-19 because headings said
"severity-dispatched collection schema" without naming the dispatch origin (A1). Round 6
isolates the two new criteria to understand their structural dependencies and tests alternative
implementations of the 12-criteria synthesis.

---

**Round 5 scoring under v6:**

| Variation | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | Aspirational hits | Composite | Verdict |
|-----------|------|------|------|------|------|------|-------------------|-----------|---------|
| V-01 | PASS | FAIL | FAIL | PASS | FAIL | FAIL | C-08 to C-14, C-17 (8/12) | **96.67** | Golden |
| V-02 | FAIL | PASS | PASS | FAIL | FAIL | FAIL | C-08 to C-13, C-15, C-16 (8/12) | **96.67** | Golden |
| V-03 | PASS | PASS | PASS | FAIL | FAIL | FAIL | C-08 to C-16 minus C-17 (9/12) | **97.50** | Golden |
| V-04 | PASS | PASS | PASS | PASS | PASS | PASS | all 12/12 | **100.00** | Golden |
| V-05 | PASS | PASS | PASS | PASS | PASS | FAIL | C-08 to C-18 (11/12) | **99.17** | Golden |

**Key Round 5 findings under v6:**

R5 V-04 is the canonical 100.00 implementation. The completion condition item (1) reads "both
the collection schema (A2) and output template (A3) have been dispatched by that confirmation
(A1 done)" -- the phrase "dispatched by that confirmation" verifies dispatch linkage, satisfying
C-18. Sub-operation headings "A2 -- COLLECT (collection schema dispatched by severity in A1)"
and "A3 -- DRAFT (output template dispatched by severity in A1)" name the dispatch origin (A1),
satisfying C-19.

R5 V-05 fails C-19. Headings say "severity-dispatched collection schema" and
"severity-dispatched output template" -- "severity-dispatched" does not name the origin
sub-operation. The "in A1" qualifier in R5 V-04 headings is load-bearing for C-19.

R5 V-03 fails C-18. Completion condition says "severity-appropriate collection form" and
"severity-appropriate output template" without verifying that both were dispatched by severity
confirmation. "Severity-appropriate" describes the result, not the dispatch chain.

---

**Round 6 open questions:**

1. Is C-19 achievable in a steps-based (non-phase) structure by naming the origin as "in Step 1"?
   This tests whether C-19 requires phase/sub-operation naming or whether any step reference works.

2. Is C-18 achievable without C-17 ("simultaneously dispatches") by adding dispatch verification
   only to the completion condition while using "determines both" in A1? If yes, C-18 and C-17 are
   independently achievable and the completion condition is a separate verifiable site for C-18.

3. Does the presence of C-18 (dispatch-verifying completion condition) + C-19 (provenance headings)
   provide enough structural evidence to satisfy C-17 ("determines both" language), even without
   the explicit "simultaneously dispatches both" phrase?

---

**Round 6 variation axes:**

- V-01: Single axis -- dispatch provenance in step headings (C-19 targeted, steps-based, no macro-phase)
- V-02: Single axis -- dispatch-verifying completion condition (C-18 targeted, macro-phase, "determines both" not "simultaneously dispatches")
- V-03: Combined C-18 + C-19 without "simultaneously dispatches" (tests C-17 dependence on that phrase)
- V-04: Full synthesis + inertia framing (all 12, conversational opening, same structural properties as R5 V-04)
- V-05: Minimal C-19 fix of R5 V-05 (patch heading wording only, everything else unchanged)

**Key Round 6 hypotheses:**

| | C-17 | C-18 | C-19 | Key question |
|---|---|---|---|---|
| V-01 | PASS | FAIL | PASS | Is "in Step 1" in a steps heading sufficient for C-19 without phase structure? |
| V-02 | FAIL | PASS | FAIL | Can completion condition verify dispatch (C-18) while A1 uses "determines both" (C-17 FAIL)? |
| V-03 | ? | PASS | PASS | Does "determines both" + C-18 + C-19 together satisfy C-17? |
| V-04 | PASS | PASS | PASS | Does inertia framing coexist with structural compliance (no regression)? |
| V-05 | PASS | PASS | PASS | Is "in A1" in headings the only change needed to promote R5 V-05 to 100.00? |

**Predicted scores (v6 rubric):**

| | Essential (60) | Recommended (30) | Aspirational (10) | Composite | Verdict |
|---|---|---|---|---|---|
| V-01 | 60 | 30 | 7.50 (9/12) | **97.50** | Golden |
| V-02 | 60 | 30 | 7.50 (9/12) or 8.33 (10/12) | **97.50 or 98.33** | Golden |
| V-03 | 60 | 30 | 9.17 (11/12) or 10.00 (12/12) | **99.17 or 100.00** | Golden |
| V-04 | 60 | 30 | 10.00 (12/12) | **100.00** | Golden |
| V-05 | 60 | 30 | 10.00 (12/12) | **100.00** | Golden |

Critical test: if V-03 scores 100.00 (C-17 PASS), then "determines both" is sufficient for C-17
and "simultaneously dispatches both" in R5 V-04 is stylistic. If V-03 scores 99.17 (C-17 FAIL),
"simultaneously dispatches both" is the load-bearing phrase for C-17.

---

## V-01 -- Dispatch Provenance in Step Headings (C-19, single axis)

**Axis**: Role sequence (single-axis)
**Hypothesis**: Adding the dispatch origin "(dispatched by severity in Step 1)" to sub-operation
step headings achieves C-19 in a steps-based (non-phase) structure. C-19 requires the dispatch
origin to be traceable through heading structure alone -- naming "Step 1" satisfies the criterion
equivalently to naming "A1." If V-01 scores 9/12 (C-19 PASS, C-15/C-16/C-18 FAIL), step-level
provenance headings are sufficient for C-19 independent of macro-phase structure. If V-01 fails
C-19, the phase-level sub-operation naming (A1/A2/A3) is required for C-19 compliance.

---

You are running `file-issue`. Capture a Signal skill issue and write a GitHub issue artifact.

---

**STEP 1 -- SEVERITY (unified pipeline key)**

Ask: "What kind of issue is this?"

Accept only:
- `crash` -- skill threw an error or produced no output
- `wrong-output` -- skill ran but output was incorrect
- `missing-feature` -- a capability the spec implies was absent
- `improvement` -- skill works; you have a specific enhancement idea

Reject any other value: "Not valid. Choose from: crash, wrong-output, missing-feature, improvement."

**Do not collect any other field until severity is confirmed.** Severity confirmation is the
single event that simultaneously dispatches both:
(a) the collection schema -- which fields to collect, in which form, with which prompts (Step 2)
(b) the output template -- which artifact structure to generate (Step 3)

Both selections are made by this one confirmation event.

---

**STEP 2 -- COLLECT (collection schema dispatched by severity in Step 1)**

Load the collection schema for the confirmed severity and collect all required fields.

**crash collection schema:**
- Skill [required]: exact skill name
- Expected [required]: what the skill should have produced
- Actual [required]: what happened instead -- paste verbatim error or output
- Impact: what workflow or task is now blocked
- Invocation, topic, chain, version/date: collect if present

**wrong-output collection schema:**
- Skill [required]: exact skill name
- Expected [required]: what the output should have contained
- Actual [required]: what it contained instead
- Delta: precise difference between expected and actual
- Invocation, topic, related skill or artifact, version/date

**missing-feature collection schema:**
- Skill [required]: exact skill name
- Expected [required]: the capability that should exist
- Actual [required]: confirm capability is absent, not merely unused
- Scope: inputs triggering the gap; outputs affected
- References: spec, rubric, or related skill implying this capability
- Topic, invocation

**improvement collection schema:**
- Skill [required]: exact skill name
- Expected [required]: proposed behavior after the improvement
- Actual [required]: current behavior -- what happens today
- Acceptance condition [required]: specific, testable definition of done
- Rationale: why this matters
- Topic, related skill or rubric criterion

---

**STEP 3 -- DRAFT (output template dispatched by severity in Step 1)**

Construct the GitHub issue using the output template that was dispatched when severity was
confirmed in Step 1.

**crash output template:**

  Title: [crash] {skill}: unhandled error -- {description}
  Severity: crash | Skill: `{skill}` | Priority: HIGH -- skill non-functional

  **Expected**: {expected}
  **Actual**: {actual -- verbatim error or output}
  **Impact**: {what workflow is blocked}
  **Steps to reproduce**
  Invocation: `{invocation}` | Topic: {topic} | Chain: {chain}
  **Context**: {version, date, related artifacts}

**wrong-output output template:**

  Title: [wrong-output] {skill}: {section} -- expected {X}, got {Y}
  Severity: wrong-output | Skill: `{skill}`

  **Expected**: {expected}
  **Actual**: {actual}
  **Delta**: {precise difference between expected and actual}
  **Steps to reproduce**
  Invocation: `{invocation}` | Topic: {topic}
  **Context**: {related skill, version, date}

**missing-feature output template:**

  Title: [missing-feature] {skill}: {capability} not implemented
  Severity: missing-feature | Skill: `{skill}`

  **Expected**: {capability that should exist}
  **Actual**: {confirmed absence}
  **Scope**: {triggering inputs; affected outputs or sections}
  **References**: {spec, rubric, or related skill}
  **Context**: topic={topic} | invocation={invocation}

**improvement output template:**

  Title: [improvement] {skill}: {specific enhancement}
  Severity: improvement | Skill: `{skill}`

  **Current behavior**: {actual -- specific}
  **Proposed behavior**: {expected -- precise enough to implement}
  **Rationale**: {why this matters}
  **Acceptance condition**: {specific, testable definition of done}
  **Context**: topic={topic} | related={related}

---

**STEP 4 -- PRE-WRITE GATE**

Do not write the artifact until every row shows PASS. Apply the correction on failure and
re-check that row before continuing.

| Check | Pass condition | Correction on fail |
|-------|----------------|--------------------|
| Required fields complete | All required fields for this severity schema are non-empty | Ask user for the missing field(s) by name |
| Severity enum | Exactly one of the four valid values | Re-prompt: "Choose from: crash, wrong-output, missing-feature, improvement" |
| Title names skill + symptom | No generic text; names specific skill and observable problem | Rewrite: "[{severity}] {skill}: {specific symptom}" |
| Reproducibility present | Invocation, input, topic, or event sequence in body | Add Topic + Invocation; ask user if both absent |
| Tone matches severity | crash=urgent+priority+impact; improvement=proposal+acceptance | Rewrite body using the tone from the output template |
| Context enriched | At least one item beyond the 4 required fields present | Add any available: topic, invocation, chain, version, date, rubric reference |

---

**STEP 5 -- WRITE**

Path: `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md`

Frontmatter:
```
skill: file-issue
topic: {topic or "untracked"}
item: issue
date: {YYYY-MM-DD}
severity: {severity}
target_skill: {skill}
```

Body: full issue text from Step 3 (post-gate revision if any checks failed).

**OFFER**

  Artifact written: simulations/feedback/{skill}-issue-{date}.md
  Open as GitHub issue?

    gh issue create \
      --title "[{severity}] {skill}: {symptom}" \
      --label "{severity}" \
      --body-file simulations/feedback/{skill}-issue-{date}.md

---

## V-02 -- Dispatch-Verifying Completion Condition (C-18, single axis)

**Axis**: Lifecycle emphasis (single-axis)
**Hypothesis**: A macro-phase completion condition that explicitly requires "both the collection
schema and the output template were dispatched by severity confirmation" achieves C-18 when the
A1 body uses "determines both" rather than "simultaneously dispatches both." The test is whether
C-18 is independently achievable through completion-condition language alone, decoupled from the
C-17 dispatch framing in A1. If V-02 scores 10/12 (C-18 PASS, C-17 FAIL), then the completion
condition is a separate verifiable site for C-18 -- and C-18 does not require C-17 as a
prerequisite. If V-02 also passes C-17, "determines both" in A1 is sufficient for C-17.

---

You are running `file-issue`. Severity is confirmed first. Phase A confirms severity, collects,
and drafts. Phase B validates and writes.

---

## PHASE A: CONFIRM SEVERITY, COLLECT, DRAFT

Phase A has three sub-operations: severity confirmation (A1), field collection (A2), and issue
drafting (A3). All three must complete before Phase B begins.

### A1 -- SEVERITY (first and only until confirmed)

Ask: "What kind of issue is this?"

Accept only:
- `crash` -- skill threw an error or produced no output
- `wrong-output` -- skill ran but output was incorrect
- `missing-feature` -- a capability the spec implies was absent
- `improvement` -- skill works; you have a specific enhancement idea

Reject any other value: "Not valid. Choose from: crash, wrong-output, missing-feature, improvement."

**Do not collect any other field until severity is confirmed.** Severity determines both the
collection schema used in A2 and the output template used in A3.

### A2 -- COLLECT

Load the collection schema for the confirmed severity and collect all required fields.

**crash collection schema:**
- Skill [required]: exact skill name
- Expected [required]: what the skill should have produced
- Actual [required]: what happened instead -- paste verbatim error or output
- Impact: what workflow or task is now blocked
- Invocation, topic, chain, version/date: collect if present

**wrong-output collection schema:**
- Skill [required]: exact skill name
- Expected [required]: what the output should have contained
- Actual [required]: what it contained instead
- Delta: precise difference between expected and actual
- Invocation, topic, related skill or artifact, version/date

**missing-feature collection schema:**
- Skill [required]: exact skill name
- Expected [required]: the capability that should exist
- Actual [required]: confirm capability is absent, not merely unused
- Scope: inputs triggering the gap; outputs affected
- References: spec, rubric, or related skill implying this capability
- Topic, invocation

**improvement collection schema:**
- Skill [required]: exact skill name
- Expected [required]: proposed behavior after the improvement
- Actual [required]: current behavior -- what happens today
- Acceptance condition [required]: specific, testable definition of done
- Rationale: why this matters
- Topic, related skill or rubric criterion

### A3 -- DRAFT

Construct the GitHub issue using the output template for the confirmed severity.

**crash output template:**

  Title: [crash] {skill}: unhandled error -- {description}
  Severity: crash | Skill: `{skill}` | Priority: HIGH -- skill non-functional

  **Expected**: {expected}
  **Actual**: {actual -- verbatim error or output}
  **Impact**: {what workflow is blocked}
  **Steps to reproduce**
  Invocation: `{invocation}` | Topic: {topic} | Chain: {chain}
  **Context**: {version, date, related artifacts}

**wrong-output output template:**

  Title: [wrong-output] {skill}: {section} -- expected {X}, got {Y}
  Severity: wrong-output | Skill: `{skill}`

  **Expected**: {expected}
  **Actual**: {actual}
  **Delta**: {precise difference between expected and actual}
  **Steps to reproduce**
  Invocation: `{invocation}` | Topic: {topic}
  **Context**: {related skill, version, date}

**missing-feature output template:**

  Title: [missing-feature] {skill}: {capability} not implemented
  Severity: missing-feature | Skill: `{skill}`

  **Expected**: {capability that should exist}
  **Actual**: {confirmed absence}
  **Scope**: {triggering inputs; affected outputs or sections}
  **References**: {spec, rubric, or related skill}
  **Context**: topic={topic} | invocation={invocation}

**improvement output template:**

  Title: [improvement] {skill}: {specific enhancement}
  Severity: improvement | Skill: `{skill}`

  **Current behavior**: {actual -- specific}
  **Proposed behavior**: {expected -- precise enough to implement}
  **Rationale**: {why this matters}
  **Acceptance condition**: {specific, testable definition of done}
  **Context**: topic={topic} | related={related}

Show the draft to the user before proceeding.

---

**DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE.**

Phase A is complete when all three conditions are simultaneously true and verifiable:
(1) Severity is confirmed as exactly one of the four valid enum values, and both the collection
    schema (A2) and the output template (A3) were dispatched by that confirmed severity (A1 done).
(2) All required fields from the severity-appropriate collection schema are non-empty (A2 done).
(3) The draft issue, constructed from the severity-appropriate output template, has been shown
    to the user (A3 done).

Do not proceed to Phase B until all three conditions are true.

---

## PHASE B: VALIDATE AND WRITE

Phase B encompasses all quality enforcement and artifact output. B1, B2, and B3 run in sequence.

### B1 -- VALIDATE

Run every row. Apply the correction on failure and re-check that row. Do not begin B2 until all
rows pass.

| Check | Pass condition | Correction on fail |
|-------|----------------|--------------------|
| Severity confirmed | Exactly one of the four valid values | Return to A1, re-collect severity |
| Required fields complete | All required fields for this severity schema are non-empty | Return to A2, ask for the missing field(s) by name |
| Title format | Matches `[{severity}] {skill}: {description}` pattern | Rewrite title to match pattern |
| Title specificity | Names specific skill and observable symptom; no generic text | Rewrite: "[{severity}] {skill}: {specific symptom}" |
| Severity-appropriate sections present | All sections defined in the A3 output template for this severity are present | Add the missing section(s) from the A3 template |
| Reproducibility present | Invocation, input, topic, or event sequence in body | Add Topic + Invocation; ask user if both absent |
| Tone matches template | crash=urgent+priority+impact; improvement=proposal+acceptance | Rewrite using A3 output template tone for this severity |
| Context enriched | At least one item beyond the 4 required fields present | Add any available: topic, invocation, chain, version, date, rubric reference |

### B2 -- WRITE

Path: `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md`

Frontmatter:
```
skill: file-issue
topic: {topic or "untracked"}
item: issue
date: {YYYY-MM-DD}
severity: {severity}
target_skill: {skill}
```

Body: full issue text from A3 (post-B1 revision if any checks failed).

### B3 -- OFFER

  Artifact written: simulations/feedback/{skill}-issue-{date}.md
  Open as GitHub issue?

    gh issue create \
      --title "[{severity}] {skill}: {symptom}" \
      --label "{severity}" \
      --body-file simulations/feedback/{skill}-issue-{date}.md

---

## V-03 -- Combined C-18 + C-19 Without "Simultaneously Dispatches" (C-17 independence test)

**Axes**: Lifecycle emphasis + role sequence (combination)
**Hypothesis**: When both C-18 (dispatch-verifying completion condition) and C-19 (provenance
headings naming "in A1") are present, the C-17 dispatch chain is structurally traceable through
the document even though A1 uses "determines both" instead of "simultaneously dispatches both."
If V-03 scores 12/12 (C-17 PASS), then the combination of dispatch-verifying completion
condition and provenance headings provides sufficient structural evidence for C-17 -- and the
phrase "simultaneously dispatches both" in R5 V-04 is not the minimal sufficient expression
for C-17. If V-03 scores 11/12 (C-17 FAIL), "simultaneously dispatches both" is load-bearing
and cannot be replaced by "determines both" even when C-18 and C-19 are both present.

---

You are running `file-issue`. Severity is confirmed first. Phase A confirms, collects, and
drafts. Phase B validates and writes.

---

## PHASE A: CONFIRM SEVERITY, COLLECT, DRAFT

Phase A has three sub-operations: severity confirmation (A1), field collection using the
severity-dispatched schema (A2), and issue drafting using the severity-dispatched template (A3).
All three must complete before Phase B begins.

### A1 -- SEVERITY (first and only until confirmed)

Ask: "What kind of issue is this?"

Accept only:
- `crash` -- skill threw an error or produced no output
- `wrong-output` -- skill ran but output was incorrect
- `missing-feature` -- a capability the spec implies was absent
- `improvement` -- skill works; you have a specific enhancement idea

Reject any other value: "Not valid. Choose from: crash, wrong-output, missing-feature, improvement."

**Do not collect any other field until severity is confirmed.** Severity determines both the
collection schema used in A2 and the output template used in A3.

### A2 -- COLLECT (collection schema dispatched by severity in A1)

Load the collection schema for the confirmed severity and collect all required fields.

**crash collection schema:**
- Skill [required]: exact skill name
- Expected [required]: what the skill should have produced
- Actual [required]: what happened instead -- paste verbatim error or output
- Impact: what workflow or task is now blocked
- Invocation, topic, chain, version/date: collect if present

**wrong-output collection schema:**
- Skill [required]: exact skill name
- Expected [required]: what the output should have contained
- Actual [required]: what it contained instead
- Delta: precise difference between expected and actual
- Invocation, topic, related skill or artifact, version/date

**missing-feature collection schema:**
- Skill [required]: exact skill name
- Expected [required]: the capability that should exist
- Actual [required]: confirm capability is absent, not merely unused
- Scope: inputs triggering the gap; outputs affected
- References: spec, rubric, or related skill implying this capability
- Topic, invocation

**improvement collection schema:**
- Skill [required]: exact skill name
- Expected [required]: proposed behavior after the improvement
- Actual [required]: current behavior -- what happens today
- Acceptance condition [required]: specific, testable definition of done
- Rationale: why this matters
- Topic, related skill or rubric criterion

### A3 -- DRAFT (output template dispatched by severity in A1)

Construct the GitHub issue using the output template that was dispatched when severity was
confirmed in A1.

**crash output template:**

  Title: [crash] {skill}: unhandled error -- {description}
  Severity: crash | Skill: `{skill}` | Priority: HIGH -- skill non-functional

  **Expected**: {expected}
  **Actual**: {actual -- verbatim error or output}
  **Impact**: {what workflow is blocked}
  **Steps to reproduce**
  Invocation: `{invocation}` | Topic: {topic} | Chain: {chain}
  **Context**: {version, date, related artifacts}

**wrong-output output template:**

  Title: [wrong-output] {skill}: {section} -- expected {X}, got {Y}
  Severity: wrong-output | Skill: `{skill}`

  **Expected**: {expected}
  **Actual**: {actual}
  **Delta**: {precise difference between expected and actual}
  **Steps to reproduce**
  Invocation: `{invocation}` | Topic: {topic}
  **Context**: {related skill, version, date}

**missing-feature output template:**

  Title: [missing-feature] {skill}: {capability} not implemented
  Severity: missing-feature | Skill: `{skill}`

  **Expected**: {capability that should exist}
  **Actual**: {confirmed absence}
  **Scope**: {triggering inputs; affected outputs or sections}
  **References**: {spec, rubric, or related skill}
  **Context**: topic={topic} | invocation={invocation}

**improvement output template:**

  Title: [improvement] {skill}: {specific enhancement}
  Severity: improvement | Skill: `{skill}`

  **Current behavior**: {actual -- specific}
  **Proposed behavior**: {expected -- precise enough to implement}
  **Rationale**: {why this matters}
  **Acceptance condition**: {specific, testable definition of done}
  **Context**: topic={topic} | related={related}

Show the draft to the user before proceeding.

---

**DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE.**

Phase A is complete when all three conditions are simultaneously true and verifiable:
(1) Severity is confirmed as exactly one of the four valid enum values, and both the collection
    schema (A2) and the output template (A3) were dispatched by that confirmed severity (A1 done).
(2) All required fields from the severity-dispatched collection schema are non-empty (A2 done).
(3) The draft issue, constructed from the severity-dispatched output template, has been shown
    to the user (A3 done).

Do not proceed to Phase B until all three conditions are true.

---

## PHASE B: VALIDATE AND WRITE

Phase B encompasses all quality enforcement and artifact output. B1, B2, and B3 run in sequence.

### B1 -- VALIDATE

Run every row. Apply the correction on failure and re-check that row. Do not begin B2 until all
rows pass.

| Check | Pass condition | Correction on fail |
|-------|----------------|--------------------|
| Severity confirmed | Exactly one of the four valid values | Return to A1, re-collect severity |
| Required fields complete | All required fields from the A2 schema for this severity are non-empty | Return to A2, ask for the missing field(s) by name |
| Title format | Matches `[{severity}] {skill}: {description}` pattern | Rewrite title to match pattern |
| Title specificity | Names specific skill and observable symptom; no generic text | Rewrite: "[{severity}] {skill}: {specific symptom}" |
| Severity-appropriate sections present | All sections from the A3 output template for this severity are present | Add the missing section(s) from the A3 template |
| Reproducibility present | Invocation, input, topic, or event sequence in body | Add Topic + Invocation; ask user if both absent |
| Tone matches template | crash=urgent+priority+impact; improvement=proposal+acceptance | Rewrite using A3 output template tone for this severity |
| Context enriched | At least one item beyond the 4 required fields present | Add any available: topic, invocation, chain, version, date, rubric reference |

### B2 -- WRITE

Path: `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md`

Frontmatter:
```
skill: file-issue
topic: {topic or "untracked"}
item: issue
date: {YYYY-MM-DD}
severity: {severity}
target_skill: {skill}
```

Body: full issue text from A3 (post-B1 revision if any checks failed).

### B3 -- OFFER

  Artifact written: simulations/feedback/{skill}-issue-{date}.md
  Open as GitHub issue?

    gh issue create \
      --title "[{severity}] {skill}: {symptom}" \
      --label "{severity}" \
      --body-file simulations/feedback/{skill}-issue-{date}.md

---

## V-04 -- Full Synthesis + Inertia Framing (all 12 criteria)

**Axes**: Full combination + phrasing register (inertia framing)
**Hypothesis**: The 12-criteria structural pattern from R5 V-04 is compatible with an inertia-
aware opening that names the cost of not filing. Framing the skill as a counterforce to the
developer reflex of "just moving on" does not interfere with structural compliance. If V-04
scores 100.00, inertia framing is additive with no regression. If any structural criterion fails,
the framing language introduced a competing interpretation that overrode structural reading.

---

Most issues go unfiled. The context that makes them reproducible -- the invocation, the topic,
the exact output -- disappears within hours. You are running `file-issue` because something
happened worth preserving. Severity is the unified pipeline key: confirmed first, it
simultaneously dispatches the collection schema and the output template. Phase A confirms,
collects, and drafts. Phase B validates and writes.

---

## PHASE A: CONFIRM SEVERITY, COLLECT, DRAFT

Phase A has three sub-operations: severity confirmation as the unified pipeline dispatch event
(A1), field collection using the severity-dispatched collection schema (A2), and issue drafting
using the severity-dispatched output template (A3). All three must complete before Phase B begins.

### A1 -- SEVERITY (unified pipeline key)

Ask: "What kind of issue is this?"

Accept only:
- `crash` -- skill threw an error or produced no output
- `wrong-output` -- skill ran but output was incorrect
- `missing-feature` -- a capability the spec implies was absent
- `improvement` -- skill works; you have a specific enhancement idea

Reject any other value: "Not valid. Choose from: crash, wrong-output, missing-feature, improvement."

**Do not collect any other field until severity is confirmed.**

**Severity confirmation is the single event that simultaneously dispatches both:**
- **(a) the collection schema** -- which fields to collect, in which form, with which prompts (A2)
- **(b) the output template** -- which artifact structure to generate (A3)

**Both selections are made by this one confirmation event. Neither pipeline is determined before
severity is confirmed; both are determined at the moment severity is confirmed.**

### A2 -- COLLECT (collection schema dispatched by severity in A1)

Load the collection schema for the confirmed severity and collect all required fields.

**crash collection schema:**
- Skill [required]: exact skill name
- Expected [required]: what the skill should have produced
- Actual [required]: what happened instead -- paste verbatim error or output
- Impact: what workflow or task is now blocked
- Invocation, topic, chain, version/date: collect if present

**wrong-output collection schema:**
- Skill [required]: exact skill name
- Expected [required]: what the output should have contained
- Actual [required]: what it contained instead
- Delta: precise difference between expected and actual
- Invocation, topic, related skill or artifact, version/date

**missing-feature collection schema:**
- Skill [required]: exact skill name
- Expected [required]: the capability that should exist
- Actual [required]: confirm capability is absent, not merely unused
- Scope: inputs triggering the gap; outputs affected
- References: spec, rubric, or related skill implying this capability
- Topic, invocation

**improvement collection schema:**
- Skill [required]: exact skill name
- Expected [required]: proposed behavior after the improvement
- Actual [required]: current behavior -- what happens today
- Acceptance condition [required]: specific, testable definition of done
- Rationale: why this matters
- Topic, related skill or rubric criterion

### A3 -- DRAFT (output template dispatched by severity in A1)

Construct the GitHub issue using the output template that was dispatched when severity was
confirmed in A1.

**crash output template:**

  Title: [crash] {skill}: unhandled error -- {description}
  Severity: crash | Skill: `{skill}` | Priority: HIGH -- skill non-functional

  **Expected**: {expected}
  **Actual**: {actual -- verbatim error or output}
  **Impact**: {what workflow is blocked}
  **Steps to reproduce**
  Invocation: `{invocation}` | Topic: {topic} | Chain: {chain}
  **Context**: {version, date, related artifacts}

**wrong-output output template:**

  Title: [wrong-output] {skill}: {section} -- expected {X}, got {Y}
  Severity: wrong-output | Skill: `{skill}`

  **Expected**: {expected}
  **Actual**: {actual}
  **Delta**: {precise difference between expected and actual}
  **Steps to reproduce**
  Invocation: `{invocation}` | Topic: {topic}
  **Context**: {related skill, version, date}

**missing-feature output template:**

  Title: [missing-feature] {skill}: {capability} not implemented
  Severity: missing-feature | Skill: `{skill}`

  **Expected**: {capability that should exist}
  **Actual**: {confirmed absence}
  **Scope**: {triggering inputs; affected outputs or sections}
  **References**: {spec, rubric, or related skill}
  **Context**: topic={topic} | invocation={invocation}

**improvement output template:**

  Title: [improvement] {skill}: {specific enhancement}
  Severity: improvement | Skill: `{skill}`

  **Current behavior**: {actual -- specific}
  **Proposed behavior**: {expected -- precise enough to implement}
  **Rationale**: {why this matters}
  **Acceptance condition**: {specific, testable definition of done}
  **Context**: topic={topic} | related={related}

Show the draft to the user before proceeding.

---

**DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE.**

Phase A is complete when all three conditions are simultaneously true and verifiable:
(1) Severity is confirmed as exactly one of the four valid enum values, and both the collection
    schema (A2) and output template (A3) have been dispatched by that confirmation (A1 done).
(2) All required fields from the severity-dispatched collection schema are non-empty (A2 done).
(3) The draft issue, constructed from the severity-dispatched output template, has been shown
    to the user (A3 done).

Do not proceed to Phase B until all three conditions are true.

---

## PHASE B: VALIDATE AND WRITE

Phase B encompasses all quality enforcement and artifact output. B1, B2, and B3 run in sequence.

### B1 -- VALIDATE

Run every row. Apply the correction on failure and re-check that row. Do not begin B2 until all
rows pass.

| Check | Pass condition | Correction on fail |
|-------|----------------|--------------------|
| Severity confirmed | Exactly one of the four valid values | Return to A1, re-collect severity |
| Required fields complete | All required fields from the A2 schema for this severity are non-empty | Return to A2, ask for the missing field(s) by name |
| Title format | Matches `[{severity}] {skill}: {description}` pattern | Rewrite title to match pattern |
| Title specificity | Names specific skill and observable symptom; no generic text | Rewrite: "[{severity}] {skill}: {specific symptom}" |
| Severity-appropriate sections present | All sections defined in the A3 output template for this severity are present | Add the missing section(s) from the A3 template |
| Reproducibility present | Invocation, input, topic, or event sequence in body | Add Topic + Invocation; ask user if both absent |
| Tone matches template | crash=urgent+priority+impact; improvement=proposal+acceptance | Rewrite using A3 output template tone for this severity |
| Context enriched | At least one item beyond the 4 required fields present | Add any available: topic, invocation, chain, version, date, rubric reference |

### B2 -- WRITE

Path: `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md`

Frontmatter:
```
skill: file-issue
topic: {topic or "untracked"}
item: issue
date: {YYYY-MM-DD}
severity: {severity}
target_skill: {skill}
```

Body: full issue text from A3 (post-B1 revision if any checks failed).

### B3 -- OFFER

  Artifact written: simulations/feedback/{skill}-issue-{date}.md
  Open as GitHub issue?

    gh issue create \
      --title "[{severity}] {skill}: {symptom}" \
      --label "{severity}" \
      --body-file simulations/feedback/{skill}-issue-{date}.md

---

## V-05 -- Minimal C-19 Fix of R5 V-05 (heading wording patch only)

**Axes**: Lifecycle emphasis (minimal change, single-axis patch)
**Hypothesis**: R5 V-05 failed C-19 because sub-operation headings said "severity-dispatched
collection schema" and "severity-dispatched output template" without naming the dispatch origin
(A1). Changing those headings to "(collection schema dispatched by severity in A1)" and
"(output template dispatched by severity in A1)" is the minimal and sufficient change to
achieve C-19. All other structural properties of R5 V-05 are preserved unchanged. If V-05 scores
100.00, the C-19 gap was entirely in heading wording and R5 V-05 was otherwise complete. If V-05
fails any other criterion, the patch exposed a regression elsewhere in the compressed form.

---

You are running `file-issue`. Severity is confirmed first. It simultaneously dispatches the
collection schema and the output template. Phase A collects and drafts. Phase B validates and writes.

---

## PHASE A: SEVERITY, COLLECT, DRAFT

### A1 -- SEVERITY (unified dispatch -- first and only operation until confirmed)

Ask: "What kind of issue is this?"

Valid values only: `crash` / `wrong-output` / `missing-feature` / `improvement`

Reject any other: "Not valid. Choose from: crash, wrong-output, missing-feature, improvement."

**Do not collect any other field until severity is confirmed. Severity confirmation simultaneously
dispatches both (a) the collection schema (A2) and (b) the output template (A3). Both are
determined by this single event.**

### A2 -- COLLECT (collection schema dispatched by severity in A1)

**crash:** Skill [req] | Expected [req] | Actual [req -- verbatim] | Impact | Invocation | Topic | Chain | Version/date

**wrong-output:** Skill [req] | Expected [req] | Actual [req] | Delta | Invocation | Topic | Related | Version/date

**missing-feature:** Skill [req] | Expected [req] | Actual [req -- confirmed absent] | Scope | References | Topic | Invocation

**improvement:** Skill [req] | Expected [req] | Actual [req] | Acceptance condition [req] | Rationale | Topic | Related

### A3 -- DRAFT (output template dispatched by severity in A1)

**crash:**

  Title: [crash] {skill}: unhandled error -- {description}
  Severity: crash | Skill: `{skill}` | Priority: HIGH -- skill non-functional
  **Expected**: {expected}
  **Actual**: {actual -- verbatim error or output}
  **Impact**: {what workflow is blocked}
  **Steps to reproduce**: Invocation: `{invocation}` | Topic: {topic} | Chain: {chain}
  **Context**: {version, date, related artifacts}

**wrong-output:**

  Title: [wrong-output] {skill}: {section} -- expected {X}, got {Y}
  Severity: wrong-output | Skill: `{skill}`
  **Expected**: {expected}
  **Actual**: {actual}
  **Delta**: {precise difference between expected and actual}
  **Steps to reproduce**: Invocation: `{invocation}` | Topic: {topic}
  **Context**: {related skill, version, date}

**missing-feature:**

  Title: [missing-feature] {skill}: {capability} not implemented
  Severity: missing-feature | Skill: `{skill}`
  **Expected**: {capability that should exist}
  **Actual**: {confirmed absence}
  **Scope**: {triggering inputs; affected outputs or sections}
  **References**: {spec, rubric, or related skill}
  **Context**: topic={topic} | invocation={invocation}

**improvement:**

  Title: [improvement] {skill}: {specific enhancement}
  Severity: improvement | Skill: `{skill}`
  **Current behavior**: {actual -- specific}
  **Proposed behavior**: {expected -- precise enough to implement}
  **Rationale**: {why this matters}
  **Acceptance condition**: {specific, testable definition of done}
  **Context**: topic={topic} | related={related}

Show draft to user before proceeding.

---

**DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE.**

Phase A is complete when: (1) severity is confirmed as one of the four valid enum values and
both the collection schema and output template have been dispatched by that event (A1 done),
(2) all required fields from the severity-dispatched collection schema are non-empty (A2 done),
and (3) the draft issue has been shown to the user (A3 done).

---

## PHASE B: VALIDATE AND WRITE

### B1 -- VALIDATE (do not begin B2 until all rows pass)

| Check | Pass condition | Correction on fail |
|-------|----------------|--------------------|
| Severity confirmed | Exactly one of the four valid values | Return to A1, re-collect severity |
| Required fields complete | All required fields from the A2 schema for this severity are non-empty | Return to A2, ask for the missing field(s) by name |
| Title names skill + symptom | Specific skill + observable symptom; no generic text | Rewrite: "[{severity}] {skill}: {specific symptom}" |
| Severity-appropriate sections present | All sections from the A3 output template are in the body | Add the missing section(s) from the A3 template |
| Reproducibility present | Invocation, input, topic, or event sequence in body | Add Topic + Invocation; ask user if both absent |
| Tone matches severity | crash=urgent+priority+impact; improvement=proposal+acceptance | Rewrite using A3 output template tone |
| Context enriched | At least one item beyond the 4 required fields present | Add topic, invocation, chain, version, date, or rubric reference |

### B2 -- WRITE

Path: `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md`

Frontmatter:
```
skill: file-issue
topic: {topic or "untracked"}
item: issue
date: {YYYY-MM-DD}
severity: {severity}
target_skill: {skill}
```

Body: full issue text from A3 (post-B1 revision if any checks failed).

### B3 -- OFFER

  Artifact written: simulations/feedback/{skill}-issue-{date}.md
  Open as GitHub issue?

    gh issue create \
      --title "[{severity}] {skill}: {symptom}" \
      --label "{severity}" \
      --body-file simulations/feedback/{skill}-issue-{date}.md
