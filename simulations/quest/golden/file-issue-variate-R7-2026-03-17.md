## file-issue -- Round 7 Variations

**Rubric**: v6 (C-01 through C-19)
**Scoring target**: 12/12 aspirational = 100.00
**Context**: Round 6 confirmed three 100.00 implementations (V-03, V-04, V-05) and answered all
three structural open questions. Round 7 explores new structural territory: accumulation path
symmetry (C-17 via C-19 alone), alternative blocking imperatives (C-15 form sensitivity),
table-based dispatch manifests (C-17/C-18/C-19 via structured notation), table-form completion
conditions (C-16/C-18 form sensitivity), and maximum compression (minimum token expression for
12/12).

---

**Round 6 confirmed scores:**

| Variation | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | Aspirational | Composite | Verdict |
|-----------|------|------|------|------|------|------|--------------|-----------|---------|
| V-01 | PASS | FAIL | FAIL | PASS | FAIL | PASS | 9/12 | **97.50** | Golden |
| V-02 | PASS | PASS | PASS | FAIL | PASS | FAIL | 10/12 | **98.33** | Golden |
| V-03 | PASS | PASS | PASS | PASS | PASS | PASS | 12/12 | **100.00** | Golden |
| V-04 | PASS | PASS | PASS | PASS | PASS | PASS | 12/12 | **100.00** | Golden |
| V-05 | PASS | PASS | PASS | PASS | PASS | PASS | 12/12 | **100.00** | Golden |

**Key Round 6 findings:**

1. "in Step N" is equivalent to "in A1" for C-19 -- step-level provenance satisfies the criterion.
2. C-18 (dispatch-verifying completion condition) is independently achievable without C-17.
3. "determines both" + C-18 + C-19 satisfies C-17 via structural accumulation.
4. C-15 is a hard prerequisite for C-16 and C-18, but NOT for C-17 or C-19.
5. The "simultaneously dispatches both" phrase in A1 is one path to C-17 but not the only path.
6. Inertia framing is orthogonal to structural compliance (no regression).

---

**Round 7 open questions:**

1. Is C-19 alone (without C-18) sufficient for C-17 accumulation when A1 uses "determines both"?
   R6 V-02 showed C-18 alone (no C-19) fails C-17. R6 V-03 showed C-18 + C-19 passes C-17.
   R7 V-01 tests C-19 alone (no C-18) with "determines both" -- is it symmetric with V-02?

2. Does C-15 require the exact "DO NOT BEGIN PHASE B" imperative, or is any strong blocking
   directive at the phase boundary sufficient? The rubric uses this phrase as an example, not
   as the mandatory text.

3. Can a dispatch manifest table in A1 -- where selecting a row simultaneously dispatches both
   the collection schema and output template -- satisfy C-17, C-18, and C-19 through table
   notation rather than prose?

4. Can the Phase A completion condition be expressed as a verification table (rows with Pass
   condition and Status columns) rather than numbered prose, while still satisfying C-16 and C-18?

5. What is the minimum token expression that preserves all 12 aspirational criteria? R6 V-05
   was compressed. Can further compression achieve 100.00, and where does it break?

---

**Round 7 variation axes:**

- V-01: Single axis -- C-19 accumulation only (C-18 intentionally absent, "determines both")
- V-02: Single axis -- alternative blocking imperative (C-15 form test, everything else R6-V04)
- V-03: Combined C-17/C-18/C-19 via dispatch manifest table (novel structural form)
- V-04: Completion condition as verification table (C-16/C-18 form test)
- V-05: Maximum compression (shortest 12/12 expression, tokens minimized)

**Round 7 key hypotheses:**

| | C-17 | C-18 | C-19 | Key question |
|---|---|---|---|---|
| V-01 | ? | FAIL | PASS | Is C-19 alone (no C-18) sufficient for C-17 accumulation? |
| V-02 | PASS | PASS | PASS | Is "PHASE B IS LOCKED" equivalent to "DO NOT BEGIN PHASE B"? |
| V-03 | ? | ? | ? | Does table-based dispatch manifest satisfy C-17/C-18/C-19? |
| V-04 | PASS | ? | PASS | Does table-form completion condition satisfy C-16/C-18? |
| V-05 | PASS | PASS | PASS | What is the minimum expression for 12/12? |

**Predicted scores (v6 rubric):**

| | Essential (60) | Recommended (30) | Aspirational (10) | Composite | Verdict |
|---|---|---|---|---|---|
| V-01 | 60 | 30 | 8.33 (10/12) | **98.33** | Golden |
| V-02 | 60 | 30 | 10.00 (12/12) | **100.00** | Golden |
| V-03 | 60 | 30 | 9.17-10.00 (11-12/12) | **99.17 or 100.00** | Golden |
| V-04 | 60 | 30 | 10.00 (12/12) | **100.00** | Golden |
| V-05 | 60 | 30 | 10.00 (12/12) | **100.00** | Golden |

Critical test: if V-01 scores 12/12 (C-17 PASS), then C-19 alone is sufficient for C-17
accumulation and C-18 is not required for the "determines both" path. If V-01 scores 10/12
(C-17 FAIL), then C-18 and C-19 are jointly required for the accumulation path -- neither is
sufficient alone.

---

## V-01 -- C-19 Accumulation Only (C-18 intentionally absent)

**Axis**: Lifecycle emphasis (single-axis)
**Hypothesis**: R6 proved that C-18 alone (without C-19) fails C-17 (V-02). R6 also proved that
C-18 + C-19 (with "determines both") passes C-17 (V-03). V-01 tests the symmetric case: C-19
alone (without C-18) with "determines both" in A1. If V-01 passes C-17, C-19 is sufficient
for the accumulation path independent of C-18 -- the "in A1" provenance in headings alone
establishes the dispatch chain. If V-01 fails C-17, C-18 is a required joint contributor to
accumulation -- neither heading provenance nor completion condition verification is sufficient
alone; both are required. The completion condition intentionally uses "severity confirmed and
collection and output stages completed" without the "dispatched by" language that passes C-18.

---

You are running `file-issue`. Severity is confirmed first. Phase A confirms severity, collects,
and drafts. Phase B validates and writes.

---

## PHASE A: CONFIRM SEVERITY, COLLECT, DRAFT

Phase A has three sub-operations: severity confirmation (A1), field collection using the
severity-appropriate schema (A2), and issue drafting using the severity-appropriate template (A3).
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
(1) Severity is confirmed as exactly one of the four valid enum values (A1 done).
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

## V-02 -- Alternative Blocking Imperative (C-15 Form Test)

**Axis**: Phrasing register (single-axis)
**Hypothesis**: C-15 requires "an explicit cross-phase blocking instruction at the boundary."
The rubric example is "DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE" but the criterion
specifies "explicit" and "blocking" -- not the exact imperative text. V-02 uses "PHASE B IS
LOCKED. Begin Phase B only after all Phase A conditions below are verified:" as the blocking
instruction. All other structural properties are identical to R6 V-04 (confirmed 100.00). If
V-02 scores 100.00 (C-15 PASS), the specific imperative form is not load-bearing -- any
explicit blocking directive at the phase boundary satisfies C-15. If V-02 scores 99.17 (C-15
FAIL), "DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE" or its close equivalents are required.

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

**PHASE B IS LOCKED. Begin Phase B only after all Phase A conditions below are verified:**

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

## V-03 -- Dispatch Manifest Table in A1 (novel structural form)

**Axes**: Output format + role sequence (combination)
**Hypothesis**: A1 presents a dispatch manifest table that maps each severity value to its
corresponding collection schema and output template. Confirming severity = selecting a manifest
row, which is the single event that simultaneously dispatches both pipelines. This table-based
dispatch form is structurally equivalent to prose-based dispatch declarations for C-17, and
provenance headings that reference "manifest row selected in A1" satisfy C-19. The completion
condition's requirement to verify "both pipelines dispatched by the manifest selection event"
satisfies C-18. If V-03 scores 100.00, table-based dispatch is a valid alternative implementation
path for C-17/C-18/C-19. If it fails on any of these, the criteria require prose-form dispatch
declarations and cannot be satisfied by structural table notation.

---

You are running `file-issue`. Severity is the dispatch key: confirming it selects a row in the
dispatch manifest, simultaneously loading both the collection schema and output template for that
severity. Phase A confirms, collects, and drafts. Phase B validates and writes.

---

## PHASE A: CONFIRM SEVERITY, COLLECT, DRAFT

Phase A has three sub-operations: severity confirmation via manifest selection (A1), field
collection using the schema loaded from the manifest (A2), and issue drafting using the template
loaded from the manifest (A3). All three must complete before Phase B begins.

### A1 -- SEVERITY (manifest selection -- first and only until confirmed)

Ask: "What kind of issue is this?"

Accept only one of the four valid severity values. Confirming severity is the single event that
selects a row in the dispatch manifest below, simultaneously dispatching both the collection
schema for A2 and the output template for A3. Do not proceed to A2 until one valid value is
confirmed.

Reject any other value: "Not valid. Choose from: crash, wrong-output, missing-feature, improvement."

**DISPATCH MANIFEST**

| Severity | Collection Schema (loaded in A2) | Output Template (loaded in A3) |
|----------|----------------------------------|-------------------------------|
| `crash` | crash-collection-schema | crash-output-template |
| `wrong-output` | wrong-output-collection-schema | wrong-output-output-template |
| `missing-feature` | missing-feature-collection-schema | missing-feature-output-template |
| `improvement` | improvement-collection-schema | improvement-output-template |

Confirming severity selects exactly one row. Both columns of the selected row are dispatched
by this single confirmation event.

### A2 -- COLLECT (collection schema from manifest row selected in A1)

Load the collection schema from the manifest row confirmed in A1 and collect all required fields.

**crash-collection-schema:**
- Skill [required]: exact skill name
- Expected [required]: what the skill should have produced
- Actual [required]: what happened instead -- paste verbatim error or output
- Impact: what workflow or task is now blocked
- Invocation, topic, chain, version/date: collect if present

**wrong-output-collection-schema:**
- Skill [required]: exact skill name
- Expected [required]: what the output should have contained
- Actual [required]: what it contained instead
- Delta: precise difference between expected and actual
- Invocation, topic, related skill or artifact, version/date

**missing-feature-collection-schema:**
- Skill [required]: exact skill name
- Expected [required]: the capability that should exist
- Actual [required]: confirm capability is absent, not merely unused
- Scope: inputs triggering the gap; outputs affected
- References: spec, rubric, or related skill implying this capability
- Topic, invocation

**improvement-collection-schema:**
- Skill [required]: exact skill name
- Expected [required]: proposed behavior after the improvement
- Actual [required]: current behavior -- what happens today
- Acceptance condition [required]: specific, testable definition of done
- Rationale: why this matters
- Topic, related skill or rubric criterion

### A3 -- DRAFT (output template from manifest row selected in A1)

Construct the GitHub issue using the output template from the manifest row confirmed in A1.

**crash-output-template:**

  Title: [crash] {skill}: unhandled error -- {description}
  Severity: crash | Skill: `{skill}` | Priority: HIGH -- skill non-functional

  **Expected**: {expected}
  **Actual**: {actual -- verbatim error or output}
  **Impact**: {what workflow is blocked}
  **Steps to reproduce**
  Invocation: `{invocation}` | Topic: {topic} | Chain: {chain}
  **Context**: {version, date, related artifacts}

**wrong-output-output-template:**

  Title: [wrong-output] {skill}: {section} -- expected {X}, got {Y}
  Severity: wrong-output | Skill: `{skill}`

  **Expected**: {expected}
  **Actual**: {actual}
  **Delta**: {precise difference between expected and actual}
  **Steps to reproduce**
  Invocation: `{invocation}` | Topic: {topic}
  **Context**: {related skill, version, date}

**missing-feature-output-template:**

  Title: [missing-feature] {skill}: {capability} not implemented
  Severity: missing-feature | Skill: `{skill}`

  **Expected**: {capability that should exist}
  **Actual**: {confirmed absence}
  **Scope**: {triggering inputs; affected outputs or sections}
  **References**: {spec, rubric, or related skill}
  **Context**: topic={topic} | invocation={invocation}

**improvement-output-template:**

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
    schema and the output template from the A1 dispatch manifest row have been dispatched by that
    manifest selection event (A1 done).
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
| Severity confirmed | Exactly one of the four valid values | Return to A1, re-confirm manifest row selection |
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

## V-04 -- Completion Condition as Verification Table (C-16/C-18 form test)

**Axes**: Output format + lifecycle emphasis (combination)
**Hypothesis**: The Phase A completion condition is currently expressed as numbered prose
conditions. V-04 replaces the prose completion condition with a four-row verification table
(columns: Check / Required State / Gate). The dispatch verification row -- "Dispatch | Both
collection schema and output template dispatched by severity confirmation | A1 done" --
carries the C-18 requirement in table form. The question is whether a table-format completion
condition satisfies C-16's "explicit, verifiable completion condition" and C-18's "completion
condition explicitly requires... dispatched by severity confirmation." All other structural
properties are identical to R6 V-04. If V-04 scores 100.00, tabular completion conditions are
valid for C-16 and C-18 -- the criteria do not require prose form. If V-04 fails C-16 or C-18,
the prose "all three conditions are simultaneously true and verifiable" formulation is load-bearing.

---

You are running `file-issue`. Severity is confirmed first. It simultaneously dispatches the
collection schema and the output template. Phase A confirms, collects, and drafts. Phase B
validates and writes.

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

Phase A completion verification table -- all rows must be TRUE before Phase B begins:

| Check | Required State | Gate |
|-------|----------------|------|
| Severity value | Exactly one of: crash, wrong-output, missing-feature, improvement | A1 done |
| Dispatch | Both the collection schema (A2) and the output template (A3) have been dispatched by the severity confirmation event | A1 done |
| Required fields | All required fields from the severity-dispatched collection schema are non-empty | A2 done |
| Draft shown | The draft issue, constructed from the severity-dispatched output template, has been shown to the user | A3 done |

Do not proceed to Phase B until all four rows are TRUE.

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

## V-05 -- Maximum Compression (shortest 12/12 expression)

**Axes**: Lifecycle emphasis + phrasing register (maximum compression)
**Hypothesis**: R6 V-05 was already compressed and scored 100.00. V-05 pushes compression
further: A1's unified dispatch declaration is reduced to one sentence rather than a bulleted
list; collection schemas are expressed as inline field chains rather than multi-line bullets;
output templates are condensed to their minimum structural footprint. The blocking instruction
and completion condition are preserved verbatim from R6 V-04 (confirmed C-15/C-16/C-18 PASS).
Provenance headings are preserved verbatim (confirmed C-19 PASS). C-17's "simultaneously
dispatches both" is preserved. If V-05 scores 100.00, the aspirational criteria survive
significant prose compression -- only the structural anchors (blocking instruction, completion
condition, provenance headings, dispatch declaration) are load-bearing, not the surrounding
elaboration. If any criterion fails, the adjacent prose that was compressed was carrying
semantic load for that criterion.

---

You are running `file-issue`. Severity is confirmed first -- it simultaneously dispatches the
collection schema and the output template. Phase A confirms, collects, and drafts. Phase B
validates and writes.

---

## PHASE A: CONFIRM SEVERITY, COLLECT, DRAFT

### A1 -- SEVERITY (unified pipeline key -- first and only operation until confirmed)

Ask: "What kind of issue is this?"

Valid values: `crash` / `wrong-output` / `missing-feature` / `improvement`

Reject any other: "Not valid. Choose from: crash, wrong-output, missing-feature, improvement."

**Do not collect any other field until severity is confirmed. Severity confirmation is the
single event that simultaneously dispatches both (a) the collection schema (A2) and (b) the
output template (A3). Both are determined by this single event.**

### A2 -- COLLECT (collection schema dispatched by severity in A1)

**crash:** Skill [req] | Expected [req] | Actual [req -- verbatim] | Impact | Invocation | Topic | Chain | Version/date

**wrong-output:** Skill [req] | Expected [req] | Actual [req] | Delta | Invocation | Topic | Related | Version/date

**missing-feature:** Skill [req] | Expected [req] | Actual [req -- confirmed absent] | Scope | References | Topic | Invocation

**improvement:** Skill [req] | Expected [req] | Actual [req] | Acceptance condition [req] | Rationale | Topic | Related

### A3 -- DRAFT (output template dispatched by severity in A1)

**crash:**

  Title: [crash] {skill}: unhandled error -- {description}
  Severity: crash | Skill: `{skill}` | Priority: HIGH -- skill non-functional
  **Expected**: {expected} | **Actual**: {actual -- verbatim} | **Impact**: {blocked workflow}
  **Steps to reproduce**: `{invocation}` | Topic: {topic} | Chain: {chain}
  **Context**: {version, date, related artifacts}

**wrong-output:**

  Title: [wrong-output] {skill}: {section} -- expected {X}, got {Y}
  Severity: wrong-output | Skill: `{skill}`
  **Expected**: {expected} | **Actual**: {actual} | **Delta**: {precise difference}
  **Steps to reproduce**: `{invocation}` | Topic: {topic}
  **Context**: {related skill, version, date}

**missing-feature:**

  Title: [missing-feature] {skill}: {capability} not implemented
  Severity: missing-feature | Skill: `{skill}`
  **Expected**: {capability} | **Actual**: {confirmed absence}
  **Scope**: {inputs; affected outputs} | **References**: {spec, rubric, related skill}
  **Context**: topic={topic} | invocation={invocation}

**improvement:**

  Title: [improvement] {skill}: {specific enhancement}
  Severity: improvement | Skill: `{skill}`
  **Current behavior**: {actual} | **Proposed behavior**: {expected}
  **Rationale**: {why this matters} | **Acceptance condition**: {testable definition of done}
  **Context**: topic={topic} | related={related}

Show draft to user before proceeding.

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
