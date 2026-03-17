## file-issue -- Round 5 Variations

**Rubric**: v5 (C-01 through C-17)
**Scoring target**: 10/10 aspirational = 100.
**Context**: Round 4 V-01 achieved C-14 + C-17 (8/10 = 98.0). Round 4 V-02 achieved C-15 + C-16
(8/10 = 98.0). No Round 4 variation achieved all four simultaneously. Round 5 targets 100 by
combining C-14 + C-15 + C-16 + C-17 in a single skill.

**Round 4 gap summary (v5 perspective):**
- V-01: C-14 PASS, C-15 FAIL, C-16 FAIL, C-17 PASS -- severity-first, no macro-phase, 8/10 = 98.0
- V-02: C-14 FAIL, C-15 PASS, C-16 PASS, C-17 FAIL -- macro-phase + completion, 8/10 = 98.0
- V-03: C-14 FAIL, C-15 FAIL, C-16 FAIL, C-17 FAIL -- table format only, 6/10 = 97.0
- V-04: C-14 PASS, C-15 PASS, C-16 PASS, C-17 FAIL -- combined, no unified dispatch, 9/10 = 99.0 (estimated)
- V-05: C-14 PASS, C-15 PASS, C-16 PASS, C-17 FAIL -- all-axis combined, no unified dispatch, 9/10 = 99.0 (estimated)

**Note on R4 retroactive scoring**: R4 V-04 and V-05 were scored at 100 under v4 (8/8 aspirational).
Under v5, the two new criteria C-16 and C-17 distinguish them. V-04 has a completion condition
(C-16 PASS) and severity-first isolation (C-14 PASS) but does not use unified-dispatch language
(C-17 depends on reading "determines both" as fully linking both pipelines to one event -- the
retroactive v5 score shown in the rubric assigns 98.0 to both V-01 and V-02, so R4 V-04 / V-05
would score approximately 99.0 if C-17 is borderline, or 98.0 if it fails).

**Round 5 variation axes:**
- V-01: Single axis -- unified pipeline dispatch (C-17 targeted, no macro-phase)
- V-02: Single axis -- completion condition in macro-phase (C-16 targeted, no severity isolation)
- V-03: Combined -- C-14 + C-15 + C-16 (severity-first + macro-phase + completion, no C-17 dispatch)
- V-04: Combined -- C-14 + C-15 + C-16 + C-17 (all four, full synthesis)
- V-05: Combined -- all four, compressed form

**Key Round 5 hypotheses:**

| | C-14 (severity-first) | C-15 (macro-phase) | C-16 (completion condition) | C-17 (unified dispatch) |
|---|---|---|---|---|
| V-01 | PASS | FAIL | FAIL | PASS |
| V-02 | FAIL | PASS | PASS | FAIL |
| V-03 | PASS | PASS | PASS | FAIL |
| V-04 | PASS | PASS | PASS | PASS |
| V-05 | PASS | PASS | PASS | PASS |

**Predicted scores (v5 rubric):**

| | Essential (60) | Recommended (30) | Aspirational (10) | Composite | Verdict |
|---|---|---|---|---|---|
| V-01 | 60 | 30 | 8.0 (8/10) | 98.0 | Golden |
| V-02 | 60 | 30 | 8.0 (8/10) | 98.0 | Golden |
| V-03 | 60 | 30 | 9.0 (9/10) | 99.0 | Golden |
| V-04 | 60 | 30 | 10.0 (10/10) | 100.0 | Golden |
| V-05 | 60 | 30 | 10.0 (10/10) | 100.0 | Golden |

Scores are predicted. C-17 is the key criterion under test: whether "the single event that
simultaneously dispatches both pipelines" language is necessary or whether "determines both X
and Y" (as in V-03) is sufficient. If V-03 passes C-17, it scores 100 and the explicit
"simultaneously dispatches both" phrasing in V-04/V-05 is redundant. If V-03 fails C-17, the
unified-dispatch framing is load-bearing and V-04/V-05 are the canonical implementations.

---

## V-01 -- Unified Pipeline Dispatch (C-17, single axis)

**Axis**: Role sequence (single-axis)
**Hypothesis**: Explicitly framing severity confirmation as "the pipeline key" that dispatches
both the collection schema and the output template -- using the word "dispatches" with both
targets named -- achieves C-17 independent of macro-phase structure. If V-01 scores 8/10 (C-17
PASS, C-15/C-16 FAIL), unified dispatch language is sufficient for C-17 without macro-phase
framing. If V-01 fails C-17, the "dispatches both simultaneously" language requires macro-phase
context to be structurally recognized.

---

You are running `file-issue`. Capture a Signal skill issue and write a GitHub issue artifact.

---

**STEP 1 -- SEVERITY (the pipeline key)**

Ask: "What kind of issue is this?"

Accept only:
- `crash` -- skill threw an error or produced no output
- `wrong-output` -- skill ran but output was incorrect
- `missing-feature` -- a capability the spec implies was absent
- `improvement` -- skill works; you have a specific enhancement idea

Reject any other value: "Not valid. Choose from: crash, wrong-output, missing-feature, improvement."

**Severity is the pipeline key. Do not collect any other field until severity is confirmed.
Severity confirmation is the single event that dispatches both:
(a) the collection schema -- which fields to collect, in which form, with which prompts (Step 2), and
(b) the output template -- which artifact structure to generate (Step 3).
Both selections are made by this one confirmation event.**

---

**STEP 2 -- COLLECT (collection schema dispatched by severity)**

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
- Scope: inputs triggering the gap; outputs or sections affected
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

**STEP 3 -- DRAFT (output template dispatched by severity)**

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

## V-02 -- Completion Condition in Macro-Phase (C-16, single axis)

**Axis**: Lifecycle emphasis (single-axis)
**Hypothesis**: A macro-phase boundary with an explicit, verifiable completion condition --
naming three distinct checkable states that must all be true before Phase B can begin --
achieves C-16 independent of whether severity is isolated first. If V-02 scores 8/10 (C-16 PASS,
C-14/C-17 FAIL), the completion condition language is sufficient for C-16 without severity
isolation. Severity is collected among other fields in A1, so C-14 and C-17 both fail. The test
is whether C-16 is independently achievable through completion-condition language alone.

---

You are running `file-issue`. Two phases. Phase A produces the issue draft. Phase B validates
and writes. Complete Phase A entirely before beginning Phase B.

---

## PHASE A: COLLECT AND DRAFT

Phase A encompasses field intake and issue authoring. A1 and A2 must both complete before
Phase B begins.

### A1 -- COLLECT

Ask the user for all four required fields:

1. **Skill** -- which Signal skill ran? (exact name, e.g., `trace-state`, `scout-competitors`)
2. **Expected** -- what should the skill have produced?
3. **Actual** -- what happened instead? (paste verbatim error text or output if available)
4. **Severity** -- must be exactly one of:
   `crash` / `wrong-output` / `missing-feature` / `improvement`

If severity is not one of these four values, reject and re-prompt. Do not proceed to A2 until
all four fields are provided and severity is valid.

Also collect without prompting: topic name, invocation string, related skills in the invocation
chain, version or date. Include available items in the issue body.

### A2 -- DRAFT

Using the confirmed severity, select the matching template and draft the issue.

**crash template:**

  Title: [crash] {skill}: unhandled error -- {description}
  Severity: crash | Skill: `{skill}` | Priority: HIGH -- skill non-functional

  **Expected**: {expected}
  **Actual**: {actual -- verbatim}
  **Impact**: {what workflow or task is blocked}
  **Steps to reproduce**
  Invocation: `{invocation}` | Topic: {topic} | Chain: {chain}
  **Context**: {version, date, related artifacts}

**wrong-output template:**

  Title: [wrong-output] {skill}: {section} -- expected {X}, got {Y}
  Severity: wrong-output | Skill: `{skill}`

  **Expected**: {expected}
  **Actual**: {actual}
  **Delta**: {precise difference between expected and actual}
  **Steps to reproduce**
  Invocation: `{invocation}` | Topic: {topic}
  **Context**: {related, version, date}

**missing-feature template:**

  Title: [missing-feature] {skill}: {capability} not implemented
  Severity: missing-feature | Skill: `{skill}`

  **Expected**: {capability that should exist}
  **Actual**: {confirmed absence}
  **Scope**: {inputs triggering the gap; outputs affected}
  **References**: {spec, rubric, or related skill}
  **Context**: topic={topic} | invocation={invocation}

**improvement template:**

  Title: [improvement] {skill}: {specific enhancement}
  Severity: improvement | Skill: `{skill}`

  **Current behavior**: {actual -- specific}
  **Proposed behavior**: {expected -- implementable}
  **Rationale**: {why this matters}
  **Acceptance condition**: {specific, testable definition of done}
  **Context**: topic={topic} | related={related}

Show the draft to the user before proceeding.

---

**DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE.**

Phase A is complete when all three conditions are simultaneously true and verifiable:
(1) All four required fields -- skill, expected, actual, severity -- are confirmed and non-empty.
(2) Severity is validated as exactly one of the four enum values: crash, wrong-output,
    missing-feature, or improvement.
(3) The draft issue, constructed from the severity-appropriate template, has been shown to
    the user and not yet revised for Phase B validation.

Do not proceed to Phase B until all three conditions are true.

---

## PHASE B: VALIDATE AND WRITE

Phase B encompasses quality enforcement and all artifact output. B1, B2, and B3 run in sequence.

### B1 -- VALIDATE

Run every row. Apply the correction on failure and re-check that row. Do not begin B2 until all
rows pass.

| Check | Pass condition | Correction on fail |
|-------|----------------|--------------------|
| All required fields present | Skill, Expected, Actual, Severity are non-empty | Ask user for the missing field(s) by name |
| Severity enum | Exactly one of the four values | Re-prompt: "Choose from: crash, wrong-output, missing-feature, improvement" |
| Title names skill + symptom | Specific skill name and observable symptom; no generic text | Rewrite: "[{severity}] {skill}: {specific symptom}" |
| Reproducibility present | Invocation, input, topic, or event sequence in body | Add Topic + Invocation; ask user if both absent |
| Tone matches template | crash=urgent+priority+impact; improvement=proposal+acceptance | Rewrite using severity template tone |
| Context enriched | At least one item beyond the 4 required fields | Add topic, invocation, chain, version, date, or rubric reference |

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

Body: full issue text from A2 (post-B1 revision if any checks failed).

### B3 -- OFFER

  Artifact written: simulations/feedback/{skill}-issue-{date}.md
  Open as GitHub issue?

    gh issue create \
      --title "[{severity}] {skill}: {symptom}" \
      --label "{severity}" \
      --body-file simulations/feedback/{skill}-issue-{date}.md

---

## V-03 -- Combined: C-14 + C-15 + C-16, Severity Gating Without Unified Dispatch

**Axes**: Role sequence + lifecycle emphasis (combination, C-17 excluded)
**Hypothesis**: Severity isolated first (C-14), two macro-phases with a blocking instruction
(C-15), and an explicit completion condition (C-16) together score 99.0. The missing element is
C-17: the skill describes severity as determining the collection form (A2) and output template
(A3) sequentially -- not as a single event simultaneously dispatching both pipelines. If V-03
scores 99.0 (C-17 FAIL), the unified-dispatch "simultaneously dispatches both" language in V-04
is structurally necessary for C-17. If V-03 also scores 100 (C-17 PASS), then describing
severity as determining both targets -- even without "simultaneously dispatches" -- is sufficient.

---

You are running `file-issue`. Severity is confirmed first and gates all field collection. Phase A
collects and drafts. Phase B validates and writes.

---

## PHASE A: CONFIRM SEVERITY, COLLECT, DRAFT

Phase A has three sub-operations: severity confirmation (A1), field collection using the severity-
appropriate form (A2), and issue drafting using the severity-appropriate template (A3). All three
must complete before Phase B begins.

### A1 -- SEVERITY (first and only operation until confirmed)

Ask: "What kind of issue is this?"

Accept only:
- `crash` -- skill threw an error or produced no output
- `wrong-output` -- skill ran but output was incorrect
- `missing-feature` -- a capability the spec implies was absent
- `improvement` -- skill works; you have a specific enhancement idea

Reject any other value: "Not valid. Choose from: crash, wrong-output, missing-feature, improvement."

**Do not collect any other field until a valid severity value is confirmed.** Severity determines
the collection form used in A2 and the output template used in A3.

### A2 -- COLLECT (load the severity-appropriate form)

With severity confirmed, load the matching collection form and ask for all required fields.

**crash form:**
- Skill [required]: exact skill name
- Expected [required]: what the skill should have produced
- Actual [required]: what happened instead -- verbatim error or output
- Impact: what workflow or task is now blocked
- Invocation, topic, chain, version/date: collect if present

**wrong-output form:**
- Skill [required]: exact skill name
- Expected [required]: what the output should have contained
- Actual [required]: what it contained instead
- Delta: precise difference between expected and actual
- Invocation, topic, related skill or artifact, version/date

**missing-feature form:**
- Skill [required]: exact skill name
- Expected [required]: the capability that should exist
- Actual [required]: confirm capability is absent, not merely unused
- Scope: inputs triggering the gap; outputs affected
- References: spec, rubric, or related skill implying this capability
- Topic, invocation

**improvement form:**
- Skill [required]: exact skill name
- Expected [required]: proposed behavior after the improvement
- Actual [required]: current behavior -- what happens today
- Acceptance condition [required]: specific, testable definition of done
- Rationale: why this matters
- Topic, related skill or rubric criterion

### A3 -- DRAFT (load the severity-appropriate template)

Draft the GitHub issue using the output template for the confirmed severity.

**crash template:**

  Title: [crash] {skill}: unhandled error -- {description}
  Severity: crash | Skill: `{skill}` | Priority: HIGH -- skill non-functional

  **Expected**: {expected}
  **Actual**: {actual -- verbatim}
  **Impact**: {what workflow is blocked}
  **Steps to reproduce**
  Invocation: `{invocation}` | Topic: {topic} | Chain: {chain}
  **Context**: {version, date, related artifacts}

**wrong-output template:**

  Title: [wrong-output] {skill}: {section} -- expected {X}, got {Y}
  Severity: wrong-output | Skill: `{skill}`

  **Expected**: {expected}
  **Actual**: {actual}
  **Delta**: {precise difference between expected and actual}
  **Steps to reproduce**
  Invocation: `{invocation}` | Topic: {topic}
  **Context**: {related skill, version, date}

**missing-feature template:**

  Title: [missing-feature] {skill}: {capability} not implemented
  Severity: missing-feature | Skill: `{skill}`

  **Expected**: {capability that should exist}
  **Actual**: {confirmed absence}
  **Scope**: {triggering inputs; affected outputs}
  **References**: {spec, rubric, or related skill}
  **Context**: topic={topic} | invocation={invocation}

**improvement template:**

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

Phase A is complete when all three conditions are simultaneously true:
(1) Severity is confirmed as exactly one of the four valid enum values (A1 done).
(2) All required fields from the severity-appropriate collection form are non-empty (A2 done).
(3) The draft issue, constructed from the severity-appropriate output template, has been shown
    to the user (A3 done).

---

## PHASE B: VALIDATE AND WRITE

Phase B encompasses all quality enforcement and artifact output. B1, B2, and B3 run in sequence.

### B1 -- VALIDATE

Run every row. Apply the correction on failure and re-check that row. Do not begin B2 until all
rows pass.

| Check | Pass condition | Correction on fail |
|-------|----------------|--------------------|
| Severity confirmed | Exactly one of the four valid values | Return to A1, re-collect severity |
| Required fields complete | All required fields for this severity form are non-empty | Return to A2, ask for the missing field(s) by name |
| Title names skill + symptom | Specific skill name and observable symptom; no generic text | Rewrite: "[{severity}] {skill}: {specific symptom}" |
| Severity-appropriate sections present | All sections defined in the A3 template for this severity are present | Add the missing section(s) from the template |
| Reproducibility present | Invocation, input, topic, or event sequence in body | Add Topic + Invocation; ask user if both absent |
| Tone matches template | crash=urgent+priority+impact; improvement=proposal+acceptance | Rewrite using severity template tone |
| Context enriched | At least one item beyond the 4 required fields | Add topic, invocation, chain, version, date, or rubric reference |

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

## V-04 -- Full Combination: C-14 + C-15 + C-16 + C-17

**Axes**: Role sequence + lifecycle emphasis (full combination)
**Hypothesis**: The four criteria are mutually compatible and reinforce each other: severity
confirmed first (C-14) as the single event that simultaneously dispatches both the collection
schema and the output template (C-17), within a macro-phase structure with an explicit DO NOT
BEGIN instruction (C-15) and a three-condition verifiable completion state (C-16). If V-04 scores
100, the combined implementation is the canonical form. If V-04 fails any of the four criteria,
the combined framing creates interference between the requirements.

---

You are running `file-issue`. Severity is the unified pipeline key: one confirmation event
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

## V-05 -- Full Combination Compressed (all four, densest form)

**Axes**: Role sequence + lifecycle emphasis (full combination, compressed)
**Hypothesis**: V-04 and V-05 target identical criteria (all 10 aspirational). V-05 tests whether
the structural properties of V-04 survive compression: the unified-dispatch instruction, the
completion condition, and the macro-phase boundary can all be expressed in fewer tokens without
losing the semantic precision needed to pass C-17 and C-16. If V-05 scores 100, token economy is
orthogonal to structural compliance. If V-05 scores lower than V-04 on C-16 or C-17, the
elaborated formulations in V-04 are load-bearing.

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

### A2 -- COLLECT (severity-dispatched collection schema)

**crash:** Skill [req] | Expected [req] | Actual [req -- verbatim] | Impact | Invocation | Topic | Chain | Version/date

**wrong-output:** Skill [req] | Expected [req] | Actual [req] | Delta | Invocation | Topic | Related | Version/date

**missing-feature:** Skill [req] | Expected [req] | Actual [req -- confirmed absent] | Scope | References | Topic | Invocation

**improvement:** Skill [req] | Expected [req] | Actual [req] | Acceptance condition [req] | Rationale | Topic | Related

### A3 -- DRAFT (severity-dispatched output template)

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
