## file-issue — Round 2 Variations

**Rubric**: v2 (C-01 through C-11)
**Scoring target**: All 4 essential + composite >= 80. Round 2 focuses on hitting C-10 + C-11
simultaneously — no Round 1 variation achieved this.

**Round 1 gap summary:**
- V-03 hit C-10 (FINDINGS phase blocks write) but checks had no prescribed remedies (C-11 fail)
- V-04 hit C-11 (Maintainer table has corrective actions) but gate was role-transition, not a
  named structural phase (C-10 borderline)
- No variation hit all four aspirational criteria (C-08, C-09, C-10, C-11)

**Round 2 variation axes:**
- V-01: Lifecycle emphasis — minimal blocking gate only (C-10 single-axis)
- V-02: Output format — corrective-action table only (C-11 single-axis)
- V-03: Lifecycle + output format — phase gate with corrective-action table (C-10 + C-11)
- V-04: Full combination — severity templates + enrichment + phase gate + corrective actions
  (targets all four: C-08 + C-09 + C-10 + C-11)
- V-05: Phrasing register — compressed inline gate (tests minimal structural interpretation
  of C-10/C-11 without full phase apparatus)

---

**Aspirational coverage by variation:**

| | C-08 severity tone | C-09 enrichment | C-10 gate | C-11 remedies |
|---|---|---|---|---|
| V-01 | tone guidance present | enrichment note | named blocking gate | checks only — no remedies |
| V-02 | tone row in table | enrichment check row | no separate phase | corrective-action column |
| V-03 | EXECUTE tone rules | SETUP notes context | VALIDATE phase blocks | VALIDATE table has remedies |
| V-04 | severity-gated templates | enrichment collect step | pre-write gate blocks | gate table has remedies |
| V-05 | severity framing note | inline collect | PRE-WRITE CHECKS blocks | numbered remedy column |

**Predicted scores (v2 rubric):**

| | Essential (60) | Recommended (30) | Aspirational (10) | Composite | Verdict |
|---|---|---|---|---|---|
| V-01 | 60 | 30 | 7.5 (C-08+C-09+C-10) | 97.5 | Golden |
| V-02 | 60 | 30 | 7.5 (C-08+C-09+C-11) | 97.5 | Golden |
| V-03 | 60 | 30 | 10 (all four) | 100 | Golden |
| V-04 | 60 | 30 | 10 (all four) | 100 | Golden |
| V-05 | 60 | 30 | 10 (all four) | 100 | Golden |

Scoring depends on whether "PRE-WRITE CHECKS" in V-05 qualifies as a structural gate (C-10).
If it doesn't qualify, V-05 scores 97.5 (C-08+C-09+C-11, missing C-10).

---

## V-01 — Lifecycle Emphasis: Minimal Blocking Gate

**Axis**: Lifecycle emphasis (single-axis)
**Hypothesis**: The smallest possible addition that achieves C-10 is a named, single-step gate
that sits between Draft and Write and explicitly blocks the write step. No corrective actions
(C-11 will fail), no role theater, no severity templates. A clean single-axis isolation of the
gate structure — if this variation scores the same as V-03 on C-10, the gate structure alone
is sufficient; if it fails, the corrective-action table is load-bearing for C-10 as well.

---

Capture a Signal skill issue and file it as a GitHub issue with a local artifact.

**Step 1 — Intake**

Collect the four required fields. Ask for each missing field before continuing:
- Skill: which skill ran (exact name, e.g. `draft-spec`, `flow-trigger`)
- Expected: what should have happened
- Actual: what did happen
- Severity: crash / wrong-output / missing-feature / improvement

Severity must be exactly one of the four enum values. Reject any other value and ask again.

Collect any available enriching context without extra prompting: topic name, invocation string,
related skills or artifacts, skill version or date.

**Step 2 — Draft**

Construct the GitHub issue:

  Title: [{severity}] {skill}: {symptom derived from Expected vs Actual delta}

  Skill: `{skill}`
  Severity: `{severity}`

  **Expected**
  {expected}

  **Actual**
  {actual}

  **Steps to reproduce**
  Invocation: `{invocation or not provided}`
  Topic: {topic or untracked}
  Related: {related or none}

  **Context**
  {topic, related skills, version, date, or artifact references}

Severity tone guidance:
- `crash`: urgent; ask for immediate reproduction steps
- `wrong-output`: factual; describe the expected/actual delta precisely
- `missing-feature`: scoped; define the capability boundary
- `improvement`: constructive; frame as a proposal, not a complaint

**Step 3 — Pre-Write Gate**

DO NOT write the artifact until all checks below pass. If any check fails, revise the draft
and re-check before proceeding to Step 4.

1. All four required fields are present and non-empty.
2. Severity is exactly one of: crash, wrong-output, missing-feature, improvement.
3. Title names the specific skill AND a specific symptom (not "Bug report" or generic text).
4. Body contains enough detail for a maintainer to investigate or reproduce.
5. Tone matches severity (urgent for crash; constructive for improvement).

**Step 4 — Write**

Write the artifact to: `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md`

Frontmatter:
  skill: file-issue
  topic: {topic or "untracked"}
  item: issue
  date: {YYYY-MM-DD}
  severity: {severity}
  target_skill: {skill}

Body: full GitHub issue text from Step 2 (post-gate revision if any checks failed).

**Step 5 — Offer**

Print:
  Artifact written to simulations/feedback/{skill}-issue-{date}.md
  Open as GitHub issue?
    gh issue create --title "[{severity}] {skill}: {symptom}" --body-file {artifact-path}

---

## V-02 — Output Format: Corrective-Action Validation Table

**Axis**: Output format (single-axis)
**Hypothesis**: A three-column validation table (check | pass condition | action on fail) is
the minimal structure that achieves C-11 without requiring a separate lifecycle phase. Each row
prescribes exactly what to do on failure. The table IS the gate — if a check fails, the remedy
is applied in-place and the table is re-evaluated. This tests whether C-11 can be hit as a
format choice rather than a lifecycle architecture choice.

---

Signal skill issue reporter. Captures a problem and files it as a GitHub issue.

**Intake**

Collect all fields. For each required field that is absent, ask the user before drafting.

| Field      | Value                                                            | Required |
|------------|------------------------------------------------------------------|----------|
| Skill      | exact skill name                                                 | yes      |
| Expected   | what should have happened                                        | yes      |
| Actual     | what did happen; verbatim output preferred                       | yes      |
| Severity   | crash / wrong-output / missing-feature / improvement             | yes      |
| Topic      | topic name, or "untracked"                                       | no       |
| Invocation | the exact command or input used                                  | no       |
| Related    | other skills, artifacts, or rubrics involved; or "none"          | no       |

**Draft**

Construct the GitHub issue:

  Title: [{severity}] {skill}: {symptom}

  Skill: `{skill}`
  Severity: `{severity}`

  **Expected**
  {expected}

  **Actual**
  {actual}

  **Steps to reproduce**
  Invocation: `{invocation or not provided}`
  Topic: {topic}
  Related: {related}

  **Context**
  {topic, related skills, version, date, or artifact references}

Severity tone:
- `crash`: urgent language; this skill is non-functional; request reproduction steps
- `wrong-output`: factual; describe the delta between expected and actual precisely
- `missing-feature`: scoped; define the capability boundary the spec implies
- `improvement`: constructive; frame as a proposal with rationale

**Validation — apply remedies before writing**

Work through each check. On failure, apply the prescribed action immediately and re-check.

| Check | Pass condition | Action on fail |
|-------|----------------|----------------|
| Skill present | Skill field non-empty | Ask: "Which skill ran?" |
| Expected present | Expected field non-empty | Ask: "What did you expect to happen?" |
| Actual present | Actual field non-empty | Ask: "What actually happened?" |
| Severity enum | Exactly one of the four values | Ask: "Choose from: crash, wrong-output, missing-feature, improvement" |
| Title specificity | Names skill + symptom; no generic text | Rewrite: "[{severity}] {skill}: {specific symptom}" |
| Reproducibility | Invocation, input, or sequence detail present | Add Invocation and Topic to Steps section; ask user if still absent |
| Tone match | Language fits the severity framing | Rewrite body using the tone guidance for this severity |
| Context enrichment | At least one item beyond the 4 required fields | Use Topic or Invocation from intake; note "no enriching context provided" if none available |

After all checks show pass, write the artifact.

**Write**

Path: `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md`
Frontmatter: skill, topic, item ("issue"), date, severity, target_skill.
Body: full GitHub issue text (post-validation).

**Offer**

  Artifact written: simulations/feedback/{skill}-issue-{date}.md
  Open as GitHub issue?
    gh issue create --title "[{severity}] {skill}: {symptom}" --body-file {artifact-path}

---

## V-03 — Lifecycle + Format: Phase Gate with Corrective-Action Table

**Axes**: Lifecycle emphasis + output format (combination)
**Hypothesis**: Merging V-03's structural phase gate (C-10 source) with V-04's corrective-action
table (C-11 source) into a single VALIDATE phase produces a skill that hits both criteria
simultaneously. The VALIDATE phase is the blocking gate; the table inside it prescribes the
remedy for each check failure. This is the minimal combination that should score 100 on all
four aspirational criteria if both V-03 and V-04 correctly diagnosed C-10 and C-11 respectively.

---

You are executing the `file-issue` skill. Run all four phases explicitly and in order.

---

### PHASE 1 — SETUP

Identify what you have from the user message:
- Skill name: present / absent
- Expected behavior: present / absent
- Actual behavior: present / absent
- Severity: present / absent / invalid enum

For each absent or invalid field, ask the user before advancing to Phase 2. Do not proceed
until all four required fields are present and severity is exactly one of:
  crash, wrong-output, missing-feature, improvement

Note any enriching context already provided: topic name, invocation string, related skills,
artifact paths, version or date of occurrence.

---

### PHASE 2 — EXECUTE

Draft the GitHub issue:

Title: [{severity}] {skill}: {symptom}
  — must name the specific skill and the observable symptom; reject generic titles

Body sections (all required):
- **Skill** — exact skill name
- **Severity** — enum value
- **Expected** — what the user described as expected behavior
- **Actual** — what the user described as the actual outcome
- **Steps to reproduce** — invocation, input, and any sequence information provided
- **Context** — topic, related skills, version/date, or linked artifacts

Severity tone:
- `crash`: urgent; request immediate reproduction steps; note workflow impact
- `wrong-output`: factual; describe the expected/actual delta precisely
- `missing-feature`: scoped; define the capability boundary
- `improvement`: constructive; frame as a proposal with rationale and acceptance condition

---

### PHASE 3 — VALIDATE

DO NOT advance to Phase 4 until all checks pass. For each failing check, apply the prescribed
correction immediately and re-check before continuing.

| Check | Pass condition | Correction on fail |
|-------|----------------|--------------------|
| Required fields complete | All 4 fields non-empty | Ask user for the missing field(s) |
| Severity enum | Exactly one of the four valid values | Ask user to choose from the enum list |
| Title specificity | Names skill + specific symptom; no generic text | Rewrite: "[{severity}] {skill}: {specific symptom}" |
| Reproducibility | Enough detail to investigate or reproduce | Add invocation, input, topic; ask user for steps if still absent |
| Tone match | Language fits severity framing | Rewrite body using tone guidance for this severity |
| Context enrichment | At least one item beyond the 4 required fields | Add topic, invocation, related skill, version, or date to Context section |

---

### PHASE 4 — AMEND

Write the artifact to `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md`

Frontmatter:
  skill: file-issue
  topic: {topic or "untracked"}
  item: issue
  date: {YYYY-MM-DD}
  severity: {severity}
  target_skill: {skill}

Body: the complete GitHub issue text from Phase 2 (post-validation revision if any checks
failed in Phase 3).

Offer:
  Artifact written to simulations/feedback/{skill}-issue-{date}.md.
  Would you like to open this as a GitHub issue?
    gh issue create --title "[{severity}] {skill}: {symptom}" --body-file {artifact-path}

---

## V-04 — Full Synthesis: Severity Templates + Enrichment + Phase Gate + Corrective Actions

**Axes**: Inertia framing + lifecycle emphasis + output format (combination)
**Hypothesis**: A design that combines (1) severity-led triage with per-severity templates
(C-08), (2) explicit enrichment collection before drafting (C-09), (3) a named phase gate that
blocks the write step (C-10), and (4) a corrective-action table within that gate (C-11) will
score 100 on all four aspirational criteria while maintaining full essential and recommended
coverage. This is the "designed-for-100" variation — the Round 2 synthesis target.

---

You are running `file-issue`. Capture a Signal skill issue and produce a high-confidence
GitHub issue artifact through a four-step pipeline.

---

## STEP 1 — TRIAGE

Select severity first. Severity determines the issue template and tone.

  1. crash          — The skill threw an error or produced no output.
  2. wrong-output   — The skill completed but the output was incorrect.
  3. missing-feature — A capability the spec implies was absent.
  4. improvement    — The skill works; a specific enhancement would improve it.

Collect the three remaining required fields:
- Skill: exact skill name (e.g. `draft-spec`, `flow-trigger`)
- Expected: what the user anticipated
- Actual: what was produced or what failed

Collect without extra prompting — use what is already present in the user message:
- Topic name
- Invocation string or input text
- Related skills, rubrics, or artifacts in the invocation chain
- Skill version or date of occurrence

---

## STEP 2 — DRAFT

Construct the issue using the severity-gated template for the selected severity.

**If `crash`:**

  Title: [crash] {skill}: unhandled error — {one-line description}
  Severity: crash | Skill: `{skill}` | Priority: HIGH — skill non-functional

  **Expected**: {expected}
  **Actual**: {actual — include any error text or stack trace verbatim}
  **Reproduction**: Invocation: `{invocation}` | Input: {input} | Env: topic={topic}, date={date}, chain={chain}
  **Impact**: {describe what workflow is blocked by this crash}

**If `wrong-output`:**

  Title: [wrong-output] {skill}: {field or section} — expected {X}, got {Y}
  Severity: wrong-output | Skill: `{skill}`

  **Expected**: {expected}
  **Actual**: {actual}
  **Delta**: {precise description of the difference between expected and actual}
  **Reproduction**: {invocation, input, topic}
  **Context**: {related skills, version, date, or linked artifact}

**If `missing-feature`:**

  Title: [missing-feature] {skill}: {capability} not present
  Severity: missing-feature | Skill: `{skill}`

  **Expected**: {describe the capability that should exist}
  **Actual**: {confirm the capability is absent, not merely undiscovered}
  **Scope**: {what inputs trigger the gap; what outputs are affected}
  **References**: {spec, rubric, or related skill that implies this capability}

**If `improvement`:**

  Title: [improvement] {skill}: {specific enhancement proposal}
  Severity: improvement | Skill: `{skill}`

  **Current behavior**: {what the skill does today}
  **Proposed behavior**: {what it should do, with enough precision to implement}
  **Rationale**: {why this matters — user workflow, rubric criteria, downstream quality}
  **Acceptance condition**: {how you would know the improvement was implemented}

---

## STEP 3 — PRE-WRITE GATE

DO NOT write the artifact until all checks pass. For each failing check, apply the prescribed
correction immediately and re-check before advancing.

| Check | Pass condition | Correction on fail |
|-------|----------------|--------------------|
| Required fields complete | All 4 fields present and non-empty | Ask user for the missing field(s) |
| Severity enum | Exactly one of the four valid values | Ask: "Choose from: crash, wrong-output, missing-feature, improvement" |
| Title specificity | Names skill + symptom; no generic text | Rewrite: "[{severity}] {skill}: {specific symptom}" |
| Reproducibility | Enough detail for a maintainer to investigate | Add invocation, input, topic; ask user if still absent |
| Severity tone match | Language fits the template framing for this severity | Rewrite using the severity-gated template tone for this severity |
| Context enrichment | At least one item beyond the 4 required fields | Add topic, invocation, related skill, date, or rubric reference |

---

## STEP 4 — WRITE + OFFER

Write the artifact to `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md`

Frontmatter:
  skill: file-issue
  topic: {topic or "untracked"}
  item: issue
  date: {YYYY-MM-DD}
  severity: {severity}
  target_skill: {skill}

Body: full issue text from Step 2 (post-gate revision if any checks failed in Step 3).

Offer:
  Artifact written: simulations/feedback/{skill}-issue-{date}.md
  Open as GitHub issue?
    gh issue create \
      --title "[{severity}] {skill}: {symptom}" \
      --label "{severity}" \
      --body-file simulations/feedback/{skill}-issue-{date}.md

---

## V-05 — Phrasing Register: Compressed Inline Gate

**Axis**: Phrasing register (single-axis variation — compressed/technical register)
**Hypothesis**: A boldly-marked "PRE-WRITE CHECKS" section sitting between the draft step and
the write step — with an explicit blocking instruction and a numbered corrective-action table —
satisfies both C-10 and C-11 without requiring a multi-phase lifecycle structure. This tests the
minimum structural signal that qualifies as a gate: a named section with a blocking instruction,
where each row has a remedy. If V-03 scores the same on C-10/C-11 as V-05, the gate structure
is about the blocking instruction + corrective table, not the phase apparatus. If V-05 fails C-10
but V-03 passes, the structural phase boundary is load-bearing.

---

Signal `file-issue` skill. Capture, validate, write, and offer.

---

**INTAKE**

Ask for each missing required field before drafting:

- Skill (required): exact skill name
- Expected (required): what should have happened
- Actual (required): what did happen — paste verbatim output if available
- Severity (required): crash / wrong-output / missing-feature / improvement

Collect without extra prompting — use whatever is already in the user message:
- Topic, invocation string, related skills or artifacts, version or date.

---

**DRAFT**

  Title: [{severity}] {skill}: {symptom}

  Skill: `{skill}` | Severity: `{severity}`

  **Expected**: {expected}
  **Actual**: {actual}

  **Steps to reproduce**
  Invocation: `{invocation or not provided}`
  Topic: {topic}
  Related: {related or none}

  **Context**
  {topic, related skills, version, date, or artifact references}

Severity framing:
- crash → urgent; request reproduction steps immediately; note workflow impact
- wrong-output → factual; describe the expected/actual delta precisely
- missing-feature → scoped; define the capability boundary
- improvement → constructive; propose, don't complain; include acceptance condition

---

**PRE-WRITE CHECKS — all must pass before writing; apply remedy on each failure and re-check**

| # | Check | Pass | Remedy on fail |
|---|-------|------|----------------|
| 1 | All 4 required fields present | Skill, Expected, Actual, Severity all non-empty | Ask user for the missing field(s) |
| 2 | Severity is valid enum | Exactly one of the four values | Ask: "Choose from: crash, wrong-output, missing-feature, improvement" |
| 3 | Title names skill + symptom | No generic text ("Bug report", "Issue") in title | Rewrite: "[{severity}] {skill}: {specific symptom}" |
| 4 | Body is reproducible | Invocation, input, or event sequence present | Add Topic and Invocation; ask user if both are absent |
| 5 | Tone matches severity | Language fits crash/wrong-output/missing-feature/improvement framing | Rewrite tone using the severity framing guidance above |
| 6 | Context has enriching item | Topic, invocation, related, or date present | Add any available item to Context section |

Do not proceed to WRITE until all six checks show pass.

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

---

**OFFER**

  Artifact written: simulations/feedback/{skill}-issue-{date}.md
  Open as GitHub issue?
    gh issue create --title "[{severity}] {skill}: {symptom}" --body-file {artifact-path}
