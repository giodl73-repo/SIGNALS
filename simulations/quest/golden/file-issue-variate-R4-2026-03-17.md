## file-issue — Round 4 Variations

**Rubric**: v4 (C-01 through C-15)
**Scoring target**: 8/8 aspirational = 100.
**Context**: Round 3 V-02 achieved C-14 (severity-first, 7/8 = 98.75). Round 3 V-04 achieved C-15
(macro-phase boundary, 7/8 = 98.75). No Round 3 variation achieved both simultaneously. Round 4
targets 100 by combining them.

**Round 3 gap summary (v4 perspective):**
- V-01: C-14 FAIL (all fields collected together), C-15 FAIL (conversational, no phases) → 97.5
- V-02: C-14 PASS (severity isolated), C-15 FAIL (step sequence, not macro-phase) → 98.75
- V-03: C-14 FAIL (no severity-first ordering), C-15 FAIL (four phases, not two) → 97.5
- V-04: C-15 PASS (DO NOT BEGIN PHASE B), C-14 FAIL (form table presents all fields together) → 98.75

**Round 4 variation axes:**
- V-01: Role sequence — severity-first isolation (single axis, C-14 targeted)
- V-02: Lifecycle emphasis — symmetric macro-phase (single axis, C-15 targeted)
- V-03: Output format — table-driven collection (single axis, neither C-14 nor C-15)
- V-04: Combined role sequence + lifecycle emphasis (C-14 + C-15 simultaneously)
- V-05: Combined all three axes — severity-first + macro-phase + table format (all 15 criteria)

**Key Round 4 hypotheses:**

| | C-14 (severity-first gate) | C-15 (macro-phase boundary) | All others (C-08–C-13) |
|---|---|---|---|
| V-01 | PASS — severity asked alone, explicit gate | FAIL — step sequence | all PASS |
| V-02 | FAIL — severity in A1 form with other fields | PASS — DO NOT BEGIN instruction | all PASS |
| V-03 | FAIL — table collects all fields together | FAIL — no macro-phase | all PASS |
| V-04 | PASS — severity alone in A1, gates A2+A3 | PASS — two phases, DO NOT BEGIN | all PASS |
| V-05 | PASS — severity alone gates phase + form load | PASS — two phases, DO NOT BEGIN | all PASS |

**Predicted scores (v4 rubric):**

| | Essential (60) | Recommended (30) | Aspirational (10) | Composite | Verdict |
|---|---|---|---|---|---|
| V-01 | 60 | 30 | 8.75 (7/8) | 98.75 | Golden |
| V-02 | 60 | 30 | 8.75 (7/8) | 98.75 | Golden |
| V-03 | 60 | 30 | 7.5 (6/8) | 97.5 | Golden |
| V-04 | 60 | 30 | 10 (8/8) | 100 | Golden |
| V-05 | 60 | 30 | 10 (8/8) | 100 | Golden |

Scores are predicted. Actual scoring by quest-score will determine whether the C-14/C-15 combined
implementations satisfy both criteria structurally.

---

## V-01 — Role Sequence: Severity-First Isolation

**Axis**: Role sequence (single-axis)
**Hypothesis**: Asking for severity in isolation — one question, no other fields — and explicitly
stating the gate condition achieves C-14. If V-01 scores 7/8 (C-14 PASS, C-15 FAIL), the severity-
first step pattern is sufficient for C-14 independent of macro-phase structure. If V-01 fails C-14,
the isolation phrasing is load-bearing and requires macro-phase framing to be recognized.

---

You are running `file-issue`. Capture a Signal skill issue and write a GitHub issue artifact.

---

**STEP 1 — SEVERITY (one question only)**

Ask: "What kind of issue is this?"

Accept only these four values:
- `crash` — the skill threw an error or produced no output
- `wrong-output` — the skill ran but the output was incorrect
- `missing-feature` — a capability the spec implies was absent
- `improvement` — the skill works; you have a specific enhancement idea

If the user provides any other value, reject it and re-prompt:
> "Not a valid severity. Choose from: crash, wrong-output, missing-feature, improvement."

**Do not collect any other field until a valid severity value is confirmed.** Severity determines
both the collection form (Step 2) and the output template (Step 3).

---

**STEP 2 — REMAINING FIELDS (load the severity-appropriate form)**

Now that severity is confirmed, load the matching form and collect all required fields.

**crash form:**
- Skill [required]: exact skill name (e.g., `draft-spec`, `flow-trigger`)
- Expected [required]: what the skill should have produced
- Actual [required]: what happened instead — paste verbatim error text or output
- Impact: what workflow or task is now blocked
- Invocation, topic, chain, version/date: collect if present in context

**wrong-output form:**
- Skill [required]: exact skill name
- Expected [required]: what the output should have contained
- Actual [required]: what the output contained instead
- Delta: the precise difference between expected and actual
- Invocation, topic, related skill or artifact, version/date

**missing-feature form:**
- Skill [required]: exact skill name
- Expected [required]: the capability that should exist
- Actual [required]: confirm the capability is absent, not merely unused
- Scope: which inputs trigger the gap; which outputs or sections are affected
- References: spec, rubric, or related skill that implies this capability
- Topic, invocation

**improvement form:**
- Skill [required]: exact skill name
- Expected [required]: the proposed behavior after the improvement
- Actual [required]: current behavior — what happens today that motivates the change
- Acceptance condition [required for improvement]: specific, testable definition of done
- Rationale: why this improvement matters — workflow, rubric criterion, or downstream quality
- Topic, related skill or rubric criterion

---

**STEP 3 — DRAFT**

Draft the GitHub issue using the template for the confirmed severity.

**crash template:**

  Title: [crash] {skill}: unhandled error — {one-line description}
  Severity: crash | Skill: `{skill}` | Priority: HIGH — skill non-functional

  **Expected**: {expected}
  **Actual**: {actual — include verbatim error text or stack trace}
  **Impact**: {what workflow is blocked by this crash}
  **Steps to reproduce**
  Invocation: `{invocation}` | Topic: {topic} | Chain: {chain}
  **Context**: {version, date, related artifacts}

**wrong-output template:**

  Title: [wrong-output] {skill}: {section} — expected {X}, got {Y}
  Severity: wrong-output | Skill: `{skill}`

  **Expected**: {expected}
  **Actual**: {actual}
  **Delta**: {precise description of what differs between expected and actual}
  **Steps to reproduce**
  Invocation: `{invocation}` | Topic: {topic}
  **Context**: {related skill, version, date}

**missing-feature template:**

  Title: [missing-feature] {skill}: {capability} not implemented
  Severity: missing-feature | Skill: `{skill}`

  **Expected**: {capability that should exist}
  **Actual**: {confirmed absence}
  **Scope**: {triggering inputs; affected outputs or sections}
  **References**: {spec, rubric criterion, or related skill}
  **Context**: topic={topic} | invocation={invocation}

**improvement template:**

  Title: [improvement] {skill}: {specific enhancement proposal}
  Severity: improvement | Skill: `{skill}`

  **Current behavior**: {actual — specific, not generic}
  **Proposed behavior**: {expected — precise enough for a maintainer to implement}
  **Rationale**: {why this matters}
  **Acceptance condition**: {how you confirm the improvement is done}
  **Context**: topic={topic} | related={related}

---

**STEP 4 — PRE-WRITE GATE**

Do not write the artifact until every row shows PASS. Apply the correction on each failure and
re-check that row before continuing.

| Check | Pass condition | Correction on fail |
|-------|----------------|--------------------|
| Required fields complete | All required fields for this severity form are non-empty | Ask user for the missing field(s) by name |
| Severity enum | Exactly one of the four valid values | Re-prompt: "Choose from: crash, wrong-output, missing-feature, improvement" |
| Title names skill + symptom | No generic text; names specific skill and observable problem | Rewrite: "[{severity}] {skill}: {specific symptom}" |
| Reproducibility present | Invocation, input, topic, or event sequence in body | Add Topic + Invocation to Steps; ask user if both absent |
| Tone matches severity | crash=urgent+priority+impact; improvement=proposal+acceptance condition | Rewrite body using the tone from the severity template |
| Context enriched | At least one item beyond the 4 required fields present | Add any available: topic, invocation, chain, version, date, rubric reference |

---

**STEP 5 — WRITE**

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

## V-02 — Lifecycle Emphasis: Symmetric Macro-Phase

**Axis**: Lifecycle emphasis (single-axis)
**Hypothesis**: Compressing all intake and authoring into Phase A and all quality enforcement and
output into Phase B — with an explicit DO NOT BEGIN instruction at the boundary — achieves C-15
independent of severity ordering. If V-02 scores 7/8 (C-15 PASS, C-14 FAIL), the macro-phase
structure is sufficient for C-15 regardless of whether severity comes first within the phase.

---

You are running `file-issue`. Two phases. Phase A produces the issue draft. Phase B validates
and writes. Complete Phase A entirely before beginning Phase B.

---

## PHASE A: COLLECT AND DRAFT

Phase A encompasses both field intake and issue authoring. A1 and A2 must both complete before
Phase B begins.

### A1 — COLLECT

Ask the user for all four required fields:

1. **Skill** — which Signal skill ran? (exact name, e.g., `trace-state`, `scout-competitors`)
2. **Expected** — what should the skill have produced?
3. **Actual** — what happened instead? (paste verbatim error text or output if available)
4. **Severity** — must be exactly one of:
   `crash` / `wrong-output` / `missing-feature` / `improvement`

If severity is not one of these four values, reject it and re-prompt. Do not proceed to A2 until
all four fields are provided and severity is valid.

Also collect without prompting: topic name, invocation string, related skills in the invocation
chain, version or date. Include available items in the issue body.

### A2 — DRAFT

Using the confirmed severity, select the matching template and draft the issue.

**crash template:**

  Title: [crash] {skill}: unhandled error — {description}
  Severity: crash | Skill: `{skill}` | Priority: HIGH — skill non-functional

  **Expected**: {expected}
  **Actual**: {actual — verbatim}
  **Impact**: {what workflow or task is blocked}
  **Steps to reproduce**
  Invocation: `{invocation}` | Topic: {topic} | Chain: {chain}
  **Context**: {version, date, related artifacts}

**wrong-output template:**

  Title: [wrong-output] {skill}: {section} — expected {X}, got {Y}
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

  **Current behavior**: {actual — specific}
  **Proposed behavior**: {expected — implementable}
  **Rationale**: {why this matters}
  **Acceptance condition**: {specific, testable definition of done}
  **Context**: topic={topic} | related={related}

Show the draft to the user before proceeding.

---

**DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE.**

Phase A is complete when: all four required fields are collected, severity is validated as one of
the four enum values, and the draft issue has been shown to the user.

---

## PHASE B: VALIDATE AND WRITE

Phase B encompasses quality enforcement and all artifact output. B1, B2, and B3 run in sequence.

### B1 — VALIDATE

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

### B2 — WRITE

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

### B3 — OFFER

  Artifact written: simulations/feedback/{skill}-issue-{date}.md
  Open as GitHub issue?

    gh issue create \
      --title "[{severity}] {skill}: {symptom}" \
      --label "{severity}" \
      --body-file simulations/feedback/{skill}-issue-{date}.md

---

## V-03 — Output Format: Table-Driven Collection

**Axis**: Output format (single-axis)
**Hypothesis**: Presenting the collection form as a structured table — with fields, severity-
applicability markers, and requirement indicators in columns — improves C-06 (reproducibility)
and C-09 (enrichment) compliance by making optional fields explicit and visible. If V-03 scores
the same as variations with prose collection, output format is neutral for coverage compliance.
If V-03 scores higher on C-06/C-09, the table format is structurally load-bearing.

---

You are running `file-issue`. Use the structured intake table to collect fields, then draft a
severity-appropriate GitHub issue.

---

**INTAKE**

Collect all fields using the table below. Fields marked **required** must be non-empty before
drafting. Fields marked *recommended* should be collected if present in context or user message.

| Field | Required? | crash | wrong-output | missing-feature | improvement |
|-------|-----------|-------|--------------|-----------------|-------------|
| Skill | required | ✓ | ✓ | ✓ | ✓ |
| Severity | required | crash | wrong-output | missing-feature | improvement |
| Expected | required | ✓ | ✓ | ✓ | ✓ |
| Actual | required | ✓ | ✓ | ✓ | ✓ |
| Acceptance condition | required for improvement | — | — | — | ✓ |
| Impact / blocked workflow | recommended | ✓ | — | — | — |
| Delta (precise difference) | recommended | — | ✓ | — | — |
| Scope / affected outputs | recommended | — | — | ✓ | — |
| Rationale | recommended | — | — | — | ✓ |
| Topic | recommended | ✓ | ✓ | ✓ | ✓ |
| Invocation | recommended | ✓ | ✓ | ✓ | ✓ |
| Related skill / rubric ref | recommended | ✓ | ✓ | ✓ | ✓ |
| Version / date | recommended | ✓ | ✓ | ✓ | ✓ |

Severity must be exactly one of the four values in the table header row. Reject any other value
and re-prompt before accepting other fields.

For any required field that is absent, ask the user before proceeding to DRAFT.

---

**DRAFT**

Select the template for the confirmed severity value and construct the issue.

**crash template:**

  Title: [crash] {skill}: unhandled error — {description}
  Severity: crash | Skill: `{skill}` | Priority: HIGH — skill non-functional

  **Expected**: {expected}
  **Actual**: {actual — verbatim error text or output}
  **Impact**: {what workflow or task is blocked}
  **Steps to reproduce**
  Invocation: `{invocation}` | Topic: {topic} | Chain: {chain}
  **Context**: {version, date, related artifacts}

**wrong-output template:**

  Title: [wrong-output] {skill}: {section} — expected {X}, got {Y}
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

  **Current behavior**: {actual}
  **Proposed behavior**: {expected}
  **Rationale**: {why this matters}
  **Acceptance condition**: {specific, testable definition of done}
  **Context**: topic={topic} | related={related}

---

**PRE-WRITE GATE**

Do not write the artifact until every row shows PASS. Apply the correction on each failure and
re-check that row before proceeding.

| # | Check | Pass condition | Correction on fail |
|---|-------|----------------|--------------------|
| 1 | All required fields present | No required row is empty for this severity | Ask user for the missing field(s) by name |
| 2 | Severity enum | Exactly one of: crash, wrong-output, missing-feature, improvement | Re-prompt with the four valid values |
| 3 | Title names skill + symptom | Specific skill name and symptom; no generic text | Rewrite: "[{severity}] {skill}: {specific symptom}" |
| 4 | Reproducibility present | Invocation, input, topic, or event sequence in body | Add Topic + Invocation; ask user if both absent |
| 5 | Tone matches severity | crash=urgent+priority+impact; improvement=proposal+acceptance | Rewrite using severity template tone |
| 6 | Context enriched | At least one recommended field present beyond the 4 required | Add topic, invocation, related, version, date, or rubric ref |

---

**WRITE**

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

Body: full issue text from DRAFT (post-gate revision if any checks failed).

**OFFER**

  Artifact written: simulations/feedback/{skill}-issue-{date}.md
  Open as GitHub issue?

    gh issue create \
      --title "[{severity}] {skill}: {symptom}" \
      --label "{severity}" \
      --body-file simulations/feedback/{skill}-issue-{date}.md

---

## V-04 — Combined: Severity-First + Macro-Phase (C-14 + C-15)

**Axes**: Role sequence + lifecycle emphasis (combination)
**Hypothesis**: Placing severity confirmation as Phase A's first and only operation — with an
explicit gate preventing collection of any other field until severity is confirmed — satisfies
C-14 within a macro-phase structure that satisfies C-15. The single event of severity confirmation
both loads the severity-appropriate form (C-14: template selection driven by severity) and marks
the completion of A1 (enabling A2 to begin). If V-04 scores 100, the combined implementation is
sufficient. If V-04 fails C-14, severity confirmation within Phase A is not equivalent to the
stronger single-step isolation in V-01.

---

You are running `file-issue`. Severity is confirmed first. It loads the form. It determines the
template. Phase A collects and drafts. Phase B validates and writes.

---

## PHASE A: SEVERITY, COLLECT, DRAFT

Phase A has three operations: confirming severity, collecting remaining fields using the severity-
appropriate form, and drafting the issue using the severity-appropriate template. All three must
complete before Phase B begins.

### A1 — SEVERITY (first and only)

Ask: "What kind of issue is this?"

Accept only:
- `crash` — skill threw an error or produced no output
- `wrong-output` — skill ran but output was incorrect
- `missing-feature` — a capability the spec implies was absent
- `improvement` — skill works; you have a specific enhancement idea

Reject any other value and re-prompt. **Do not collect any other field until a valid severity
value is confirmed.** Severity determines both the collection form (A2) and the output template (A3).

### A2 — COLLECT (load the severity-appropriate form)

With severity confirmed, load the matching form and collect all required fields.

**crash form:**
- Skill [required]: exact skill name
- Expected [required]: what the skill should have produced
- Actual [required]: what happened instead — paste verbatim error or output
- Impact: what workflow or task is now blocked
- Invocation, topic, chain, version/date: collect if present

**wrong-output form:**
- Skill [required]: exact skill name
- Expected [required]: what the output should have contained
- Actual [required]: what it contained instead
- Delta: the precise difference between expected and actual
- Invocation, topic, related skill or artifact, version/date

**missing-feature form:**
- Skill [required]: exact skill name
- Expected [required]: the capability that should exist
- Actual [required]: confirm the capability is absent, not merely undiscovered
- Scope: inputs triggering the gap; outputs or sections affected
- References: spec, rubric, or related skill implying this capability
- Topic, invocation

**improvement form:**
- Skill [required]: exact skill name
- Expected [required]: the proposed behavior after the improvement
- Actual [required]: current behavior — what happens today
- Acceptance condition [required]: specific, testable definition of done
- Rationale: why this matters
- Topic, related skill or rubric criterion

### A3 — DRAFT (template selected by confirmed severity)

Draft the GitHub issue using the template for the severity confirmed in A1.

**crash template:**

  Title: [crash] {skill}: unhandled error — {description}
  Severity: crash | Skill: `{skill}` | Priority: HIGH — skill non-functional

  **Expected**: {expected}
  **Actual**: {actual — verbatim error or output}
  **Impact**: {what workflow is blocked}
  **Steps to reproduce**
  Invocation: `{invocation}` | Topic: {topic} | Chain: {chain}
  **Context**: {version, date, related artifacts}

**wrong-output template:**

  Title: [wrong-output] {skill}: {section} — expected {X}, got {Y}
  Severity: wrong-output | Skill: `{skill}`

  **Expected**: {expected}
  **Actual**: {actual}
  **Delta**: {precise difference}
  **Steps to reproduce**
  Invocation: `{invocation}` | Topic: {topic}
  **Context**: {related, version, date}

**missing-feature template:**

  Title: [missing-feature] {skill}: {capability} not implemented
  Severity: missing-feature | Skill: `{skill}`

  **Expected**: {capability that should exist}
  **Actual**: {confirmed absence}
  **Scope**: {triggering inputs; affected outputs}
  **References**: {spec, rubric, related skill}
  **Context**: topic={topic} | invocation={invocation}

**improvement template:**

  Title: [improvement] {skill}: {specific enhancement}
  Severity: improvement | Skill: `{skill}`

  **Current behavior**: {actual}
  **Proposed behavior**: {expected}
  **Rationale**: {why this matters}
  **Acceptance condition**: {specific, testable definition of done}
  **Context**: topic={topic} | related={related}

Show the draft to the user before proceeding.

---

**DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE.**

Phase A is complete when: severity is confirmed as one of the four valid values (A1), all
required fields from the severity-appropriate form are collected (A2), and the draft issue
has been shown to the user (A3).

---

## PHASE B: VALIDATE AND WRITE

Phase B encompasses quality enforcement and all artifact output. B1, B2, and B3 run in sequence.

### B1 — VALIDATE

Run every row. Apply the correction on failure and re-check that row. Do not begin B2 until all
rows pass.

| Check | Pass condition | Correction on fail |
|-------|----------------|--------------------|
| Severity confirmed | Exactly one of the four valid values | Return to A1, re-collect severity |
| Required fields complete | All required fields for this severity form are non-empty | Return to A2, ask for the missing field(s) |
| Title names skill + symptom | Specific skill name and observable symptom; no generic text | Rewrite: "[{severity}] {skill}: {specific symptom}" |
| Severity-appropriate sections present | Body contains all sections defined in the A3 template for this severity | Add the missing section(s) from the template |
| Reproducibility present | Invocation, input, topic, or event sequence in body | Add Topic + Invocation; ask user if both absent |
| Tone matches template | crash=urgent+priority+impact; improvement=proposal+acceptance | Rewrite using severity template tone |
| Context enriched | At least one item beyond the 4 required fields | Add topic, invocation, chain, version, date, or rubric reference |

### B2 — WRITE

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

### B3 — OFFER

  Artifact written: simulations/feedback/{skill}-issue-{date}.md
  Open as GitHub issue?

    gh issue create \
      --title "[{severity}] {skill}: {symptom}" \
      --label "{severity}" \
      --body-file simulations/feedback/{skill}-issue-{date}.md

---

## V-05 — Combined: Severity-First + Macro-Phase + Table Format (All 15 Criteria)

**Axes**: Role sequence + lifecycle emphasis + output format (full combination)
**Hypothesis**: The three axes are mutually compatible: severity-first gate (C-14) and macro-phase
boundary (C-15) are both achieved in Phase A / Phase B structure, while table-format collection
(V-03 axis) makes the severity-field relationship explicit without collapsing the sequencing.
The collection table only loads after severity is confirmed, so the table format reinforces rather
than undermines C-14. If V-05 scores the same as V-04, the table format axis is neutral. If V-05
scores higher on C-06/C-09, the table format is independently contributing to coverage quality.

---

You are running `file-issue`. Severity is the gating signal: it is confirmed first, loads the
intake table, and selects the output template. Phase A collects and drafts. Phase B validates
and writes.

---

## PHASE A: CONFIRM SEVERITY, LOAD TABLE, COLLECT, DRAFT

Phase A has four operations: severity confirmation, intake table load, field collection, and
issue drafting. All four must complete before Phase B begins.

### A1 — SEVERITY (confirm before any other field)

Ask: "What kind of issue is this?"

Accept only:
- `crash` — skill threw an error or produced no output
- `wrong-output` — skill ran but output was incorrect
- `missing-feature` — a capability the spec implies was absent
- `improvement` — skill works; you have a specific enhancement idea

Reject any other value with: "Not valid. Choose from: crash, wrong-output, missing-feature,
improvement." **Do not load the intake table or collect any other field until severity is
confirmed.** Severity selects the intake table (A2) and the output template (A3).

### A2 — INTAKE TABLE (loaded after severity is confirmed)

Load the intake table for the confirmed severity. Fields marked **required** must be non-empty
before drafting. Fields marked *recommended* should be collected if available in context.

**crash intake table:**

| Field | Required? | Notes |
|-------|-----------|-------|
| Skill | required | Exact skill name (e.g., `flow-trigger`, `trace-state`) |
| Expected | required | What the skill should have produced |
| Actual | required | What happened instead — paste verbatim error or output |
| Impact | recommended | What workflow or task is now blocked |
| Invocation | recommended | Exact command or input used |
| Topic | recommended | Topic name, or "untracked" |
| Chain | recommended | Related skills in the invocation chain |
| Version / date | recommended | When this occurred |

**wrong-output intake table:**

| Field | Required? | Notes |
|-------|-----------|-------|
| Skill | required | Exact skill name |
| Expected | required | What the output should have contained |
| Actual | required | What it contained instead |
| Delta | recommended | Precise difference between expected and actual |
| Invocation | recommended | Exact command or input used |
| Topic | recommended | Topic name, or "untracked" |
| Related | recommended | Linked rubric, golden artifact, or specification |
| Version / date | recommended | When this occurred |

**missing-feature intake table:**

| Field | Required? | Notes |
|-------|-----------|-------|
| Skill | required | Exact skill name |
| Expected | required | The capability that should exist |
| Actual | required | Confirm absence — not just unused |
| Scope | recommended | Inputs triggering the gap; outputs affected |
| References | recommended | Spec, rubric, or related skill implying this capability |
| Topic | recommended | Topic name, or "untracked" |
| Invocation | recommended | Exact invocation string if applicable |

**improvement intake table:**

| Field | Required? | Notes |
|-------|-----------|-------|
| Skill | required | Exact skill name |
| Expected | required | Proposed behavior after the improvement |
| Actual | required | Current behavior — what happens today |
| Acceptance condition | required | Specific, testable definition of done |
| Rationale | recommended | Why this matters — workflow, rubric criterion, quality |
| Topic | recommended | Topic name, or "untracked" |
| Related | recommended | Linked rubric criterion, skill, or example |

For any required field that is absent, ask the user before proceeding to A3.

### A3 — DRAFT (template selected by confirmed severity)

Construct the GitHub issue using the output template for the confirmed severity.

**crash template:**

  Title: [crash] {skill}: unhandled error — {description}
  Severity: crash | Skill: `{skill}` | Priority: HIGH — skill non-functional

  **Expected**: {expected}
  **Actual**: {actual — verbatim error or output}
  **Impact**: {what workflow is blocked}
  **Steps to reproduce**
  Invocation: `{invocation}` | Topic: {topic} | Chain: {chain}
  **Context**: {version, date, related artifacts}

**wrong-output template:**

  Title: [wrong-output] {skill}: {section} — expected {X}, got {Y}
  Severity: wrong-output | Skill: `{skill}`

  **Expected**: {expected}
  **Actual**: {actual}
  **Delta**: {precise difference between expected and actual}
  **Steps to reproduce**
  Invocation: `{invocation}` | Topic: {topic}
  **Context**: {related skill or artifact, version, date}

**missing-feature template:**

  Title: [missing-feature] {skill}: {capability} not implemented
  Severity: missing-feature | Skill: `{skill}`

  **Expected**: {capability that should exist}
  **Actual**: {confirmed absence}
  **Scope**: {triggering inputs; affected outputs or sections}
  **References**: {spec, rubric criterion, or related skill}
  **Context**: topic={topic} | invocation={invocation}

**improvement template:**

  Title: [improvement] {skill}: {specific enhancement}
  Severity: improvement | Skill: `{skill}`

  **Current behavior**: {actual — specific}
  **Proposed behavior**: {expected — precise enough to implement}
  **Rationale**: {why this matters}
  **Acceptance condition**: {specific, testable definition of done}
  **Context**: topic={topic} | related={related}

Show the draft to the user before proceeding.

---

**DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE.**

Phase A is complete when: severity is confirmed as one of the four valid values (A1), all
required fields in the severity-appropriate intake table are collected (A2), and the draft issue
has been shown to the user (A3).

---

## PHASE B: VALIDATE AND WRITE

Phase B encompasses all quality enforcement and artifact output. B1, B2, and B3 run in sequence.

### B1 — VALIDATE

Run every row. Apply the correction on failure and re-check that row before continuing. Do not
begin B2 until every row shows PASS.

| Check | Pass condition | Correction on fail |
|-------|----------------|--------------------|
| Severity confirmed | Exactly one of the four valid values | Return to A1, re-collect severity |
| Required intake fields complete | All required rows in the A2 table for this severity are non-empty | Return to A2, ask for the missing field(s) by name |
| Title format | Matches `[{severity}] {skill}: {description}` pattern | Rewrite title to match pattern |
| Title specificity | Names specific skill and observable symptom; no generic text | Rewrite: "[{severity}] {skill}: {specific symptom}" |
| Severity-appropriate sections | All sections defined in the A3 template for this severity are present | Add the missing section(s) from the A3 template |
| Reproducibility present | Invocation, input, topic, or event sequence in body | Add Topic + Invocation; ask user if both absent |
| Tone matches severity | crash=urgent+priority+impact; improvement=proposal+acceptance | Rewrite body using the A3 template tone for this severity |
| Context enriched | At least one recommended intake field present in body | Add any available: topic, invocation, chain, version, date, rubric reference |

### B2 — WRITE

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

### B3 — OFFER

  Artifact written: simulations/feedback/{skill}-issue-{date}.md
  Open as GitHub issue?

    gh issue create \
      --title "[{severity}] {skill}: {symptom}" \
      --label "{severity}" \
      --body-file simulations/feedback/{skill}-issue-{date}.md
