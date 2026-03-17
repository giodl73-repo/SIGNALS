## file-issue -- Round 3 Variations

**Rubric**: v3 (C-01 through C-13)
**Scoring target**: All 4 essential + all 3 recommended + all 6 aspirational = 100.
**Context**: Round 2 V-04 achieved 100 under v3. Round 3 does not extend the rubric -- it tests
alternative structural implementations of C-12/C-13, the two new criteria added in v3. All five
variations are designed to satisfy all 13 criteria. The axes isolate WHICH structural approach
achieves each criterion most reliably, not whether to include it.

**Round 2 gap summary (v3 perspective):**
- V-01 through V-03: Missing C-12 (per-severity templates) and C-13 (--label flag)
- V-04: All 6 aspirational. The benchmark.
- V-05: Ambiguous C-10 ("PRE-WRITE CHECKS" section -- is that a named structural gate?)

**Round 3 variation axes:**
- V-01: Phrasing register -- conversational first-person imperative throughout
- V-02: Role sequence -- template-first (severity selected first; template drives collection)
- V-03: Inertia framing -- workflow blockage as organizing metaphor throughout
- V-04: Lifecycle compression -- two macro-phases (COLLECT+DRAFT / VALIDATE+WRITE)
- V-05: Minimal-token density -- all 13 criteria, densest possible form

**Key Round 3 hypotheses:**

| | C-12 (4 distinct templates) | C-13 (--label) | C-10 (blocking gate) | C-11 (remedies) |
|---|---|---|---|---|
| V-01 | per-severity blocks in conversational register | present | blocking instruction | remedies in plain language |
| V-02 | template IS the collection form (template-first) | present | post-draft validation gate | corrective-action table |
| V-03 | workflow-impact-first templates | present | VALIDATE phase blocks | remedies per check |
| V-04 | templates in macro-phase A; gate in macro-phase B | present | phase boundary blocks | table in phase B |
| V-05 | four inline template blocks | present | explicit STOP instruction | numbered remedy column |

**Predicted scores (v3 rubric):**

| | Essential (60) | Recommended (30) | Aspirational (10) | Composite | Verdict |
|---|---|---|---|---|---|
| V-01 | 60 | 30 | 10 (all 6) | 100 | Golden |
| V-02 | 60 | 30 | 10 (all 6) | 100 | Golden |
| V-03 | 60 | 30 | 10 (all 6) | 100 | Golden |
| V-04 | 60 | 30 | 10 (all 6) | 100 | Golden |
| V-05 | 60 | 30 | 10 (all 6) | 100 | Golden |

Scores are predicted. Actual scoring by quest-score will determine whether structural variations
produce different results for borderline criteria (especially C-10 / C-12).

---

## V-01 -- Phrasing Register: Conversational First-Person Imperative

**Axis**: Phrasing register (single-axis)
**Hypothesis**: A conversational register ("Which skill ran?", "What did you expect?") reduces
field-capture friction while preserving structural rigor. If V-01 and V-04 (Round 2) score the
same on all 13 criteria, register is irrelevant to compliance. If V-01 scores lower on C-10 or
C-12, formal imperative language is structurally load-bearing.

---

You are running `file-issue`. Walk the user through reporting a Signal skill issue, then produce
a GitHub issue artifact. Be direct and conversational -- ask, not instruct.

**Ask the user for the following. Do not draft until all four are answered.**

1. Which skill ran? (exact name -- e.g. `draft-spec`, `flow-trigger`)
2. What did you expect to happen?
3. What actually happened? (paste verbatim output or error if available)
4. How severe is this?
   - `crash` -- the skill threw an error or produced no output
   - `wrong-output` -- it ran but the output was incorrect
   - `missing-feature` -- a capability the spec implies was absent
   - `improvement` -- the skill works; you have a specific enhancement idea

If the user gives a severity value that is not one of these four, tell them: "Choose from:
crash, wrong-output, missing-feature, improvement -- no other values are accepted."

While collecting, also note anything already in the user message: topic name, invocation string,
related skills or artifacts, version or date. You will need these for enrichment.

---

**Draft the GitHub issue using the template for the selected severity.**

If `crash`:

  Title: [crash] {skill}: unhandled error -- {one-line description}
  Severity: crash | Skill: `{skill}` | Priority: HIGH -- skill non-functional

  **Expected**
  {expected}

  **Actual**
  {actual -- include any error text or stack trace verbatim}

  **Steps to reproduce**
  Invocation: `{invocation or not provided}`
  Topic: {topic or untracked}
  Chain: {related skills in the invocation chain, or none}

  **Impact**
  {describe what workflow is blocked -- this crash prevents completing what task?}

  **Context**
  {version, date, related artifacts, or rubric references}

If `wrong-output`:

  Title: [wrong-output] {skill}: {field or section} -- expected {X}, got {Y}
  Severity: wrong-output | Skill: `{skill}`

  **Expected**
  {expected}

  **Actual**
  {actual}

  **Delta**
  {precise description of what differs between expected and actual -- be specific}

  **Steps to reproduce**
  Invocation: `{invocation or not provided}`
  Topic: {topic or untracked}

  **Context**
  {related skills, version, date, or artifact references}

If `missing-feature`:

  Title: [missing-feature] {skill}: {capability} not implemented
  Severity: missing-feature | Skill: `{skill}`

  **Expected**
  {describe the capability that should exist}

  **Actual**
  {confirm the capability is absent, not just undiscovered -- test invocation if known}

  **Scope**
  {what inputs trigger the gap; what outputs or sections are affected}

  **References**
  {spec, rubric, related skill, or golden artifact that implies this capability}

  **Context**
  {topic, invocation, version, or date}

If `improvement`:

  Title: [improvement] {skill}: {specific enhancement proposal}
  Severity: improvement | Skill: `{skill}`

  **Current behavior**
  {what the skill does today -- be specific, not "it's not good enough"}

  **Proposed behavior**
  {what it should do, with enough precision for a maintainer to implement it}

  **Rationale**
  {why this matters -- user workflow, rubric criterion, downstream quality, or example}

  **Acceptance condition**
  {exactly how you would confirm the improvement was correctly implemented}

  **Context**
  {topic, invocation, related skills, version, or date}

---

**Before writing the artifact, check all of the following. If any check fails, fix the draft
and re-check -- do not write until every check passes.**

1. All four required fields present and non-empty?
   If not: ask the user for the missing one(s).
2. Severity is exactly one of the four enum values?
   If not: ask the user to choose from the list.
3. Title names the specific skill AND a specific symptom -- no generic text like "Bug report"?
   If not: rewrite the title as "[{severity}] {skill}: {specific symptom}".
4. Body contains enough detail for a maintainer to investigate -- invocation, input, or sequence?
   If not: add Topic and Invocation to the Steps section; ask the user if both are absent.
5. Tone fits the severity -- urgent for crash, constructive for improvement?
   If not: rewrite the body using the template tone guidance for this severity.
6. Body includes at least one enriching item beyond the four required fields?
   If not: add topic, invocation, related skill, date, or a rubric reference to the Context section.

---

**Write the artifact.**

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

Body: the complete GitHub issue from the draft above (post-check revision if any checks failed).

---

**Offer to open it.**

Tell the user:

  Artifact written: simulations/feedback/{skill}-issue-{date}.md
  Open as GitHub issue?

    gh issue create \
      --title "[{severity}] {skill}: {symptom}" \
      --label "{severity}" \
      --body-file simulations/feedback/{skill}-issue-{date}.md

---

## V-02 -- Role Sequence: Template-First (Severity Selects Template; Template Drives Collection)

**Axis**: Role sequence (single-axis)
**Hypothesis**: Selecting severity BEFORE collecting other fields means the template determines
what to ask, not what to do with answers. This produces architecturally better C-12 compliance
because the template is an INPUT form, not an OUTPUT form. If V-02 scores higher on C-12 than
other variations, template-first ordering is the correct architectural choice. If scores are
equal, collection order does not affect compliance.

---

You are running `file-issue`. Load the severity-gated input form before collecting any other
fields. Severity determines which fields are required.

---

**STEP 1 -- SELECT SEVERITY**

Ask the user first:

  What kind of issue is this?
    crash          -- the skill threw an error or produced no output
    wrong-output   -- the skill ran but the output was incorrect
    missing-feature -- a capability the spec implies was absent
    improvement    -- the skill works; you have a specific enhancement idea

Severity must be exactly one of these four values. Reject any other input and re-prompt.
Do not collect any other field until severity is confirmed.

---

**STEP 2 -- COLLECT FIELDS USING THE SEVERITY FORM**

Once severity is known, load the corresponding input form. Ask the user to fill in each field.
Fields marked [required] must be non-empty before you proceed to Step 3.

**Form: crash**
- Skill [required]: which skill ran? (exact name)
- Expected [required]: what should have happened?
- Actual [required]: what actually happened? (paste error text or output verbatim)
- Invocation: the exact command or input used
- Topic: topic name, or "untracked"
- Chain: other skills in the invocation chain
- Impact: what workflow or task is now blocked?
- Version / date: when did this occur?

**Form: wrong-output**
- Skill [required]: which skill ran?
- Expected [required]: what should the output have contained?
- Actual [required]: what did the output contain instead?
- Delta: the precise difference between expected and actual
- Invocation: the exact command or input used
- Topic: topic name, or "untracked"
- Related: linked rubric, golden artifact, or specification
- Version / date: when did this occur?

**Form: missing-feature**
- Skill [required]: which skill ran?
- Expected [required]: what capability should have been present?
- Actual [required]: confirm the capability was absent -- not just unused
- Scope: which inputs trigger the gap; which outputs are affected
- References: spec, rubric, or related skill that implies this capability
- Topic: topic name, or "untracked"
- Invocation: the exact invocation string, if applicable

**Form: improvement**
- Skill [required]: which skill would be enhanced?
- Expected [required]: what should it do after the improvement?
- Actual [required]: what does it do today that motivates the improvement?
- Acceptance condition [required for improvement]: how will you confirm the improvement is done?
- Rationale: why this matters -- workflow, rubric criterion, downstream quality
- Topic: topic name, or "untracked"
- Related: linked rubric criterion, skill, or example where this gap appeared

---

**STEP 3 -- DRAFT THE GITHUB ISSUE**

Construct the issue from the filled-in form. Title and body structure are determined by the
selected severity.

**crash issue:**

  Title: [crash] {skill}: unhandled error -- {one-line description}
  Severity: crash | Skill: `{skill}` | Priority: HIGH -- skill non-functional

  **Expected**: {expected}
  **Actual**: {actual}
  **Impact**: {impact -- what workflow is blocked}
  **Steps to reproduce**
  Invocation: `{invocation}` | Topic: {topic} | Chain: {chain}
  **Context**: {version, date, related artifacts}

**wrong-output issue:**

  Title: [wrong-output] {skill}: {field or section} -- expected {X}, got {Y}
  Severity: wrong-output | Skill: `{skill}`

  **Expected**: {expected}
  **Actual**: {actual}
  **Delta**: {delta}
  **Steps to reproduce**
  Invocation: `{invocation}` | Topic: {topic}
  **Context**: {related, version, date}

**missing-feature issue:**

  Title: [missing-feature] {skill}: {capability} not implemented
  Severity: missing-feature | Skill: `{skill}`

  **Expected**: {expected capability}
  **Actual**: {confirmed absence}
  **Scope**: {inputs and outputs affected}
  **References**: {spec, rubric, related skill}
  **Context**: topic={topic} | invocation={invocation}

**improvement issue:**

  Title: [improvement] {skill}: {specific enhancement}
  Severity: improvement | Skill: `{skill}`

  **Current behavior**: {actual}
  **Proposed behavior**: {expected}
  **Rationale**: {rationale}
  **Acceptance condition**: {acceptance condition}
  **Context**: topic={topic} | related={related}

---

**STEP 4 -- PRE-WRITE GATE**

DO NOT write the artifact until all rows below show PASS. For each FAIL, apply the correction
and re-evaluate the row before continuing.

| Check | Pass condition | Correction on fail |
|-------|----------------|--------------------|
| Required fields complete | All required fields for this severity form are non-empty | Ask the user for the missing field(s) by name |
| Severity enum | Exactly one of the four valid values | Re-prompt: "Choose from: crash, wrong-output, missing-feature, improvement" |
| Title specificity | Title names skill + symptom; no generic text | Rewrite: "[{severity}] {skill}: {specific symptom}" |
| Reproducibility | Invocation, input, or sequence detail present | Add Topic and Invocation to Steps; ask user if both absent |
| Severity tone | Language matches form framing (crash=urgent+priority; improvement=proposal+acceptance) | Rewrite body using the tone constraints of the form for this severity |
| Context enrichment | At least one enriching item present beyond the 4 required fields | Add any available form field value to the Context section |

---

**STEP 5 -- WRITE + OFFER**

Write the artifact to `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md`

Frontmatter:
```
skill: file-issue
topic: {topic or "untracked"}
item: issue
date: {YYYY-MM-DD}
severity: {severity}
target_skill: {skill}
```

Body: full issue text from Step 3 (post-gate revision if any checks failed in Step 4).

Offer:

  Artifact written: simulations/feedback/{skill}-issue-{date}.md
  Open as GitHub issue?

    gh issue create \
      --title "[{severity}] {skill}: {symptom}" \
      --label "{severity}" \
      --body-file simulations/feedback/{skill}-issue-{date}.md

---

## V-03 -- Inertia Framing: Workflow Blockage as Organizing Metaphor

**Axis**: Inertia framing (single-axis)
**Hypothesis**: Organizing the issue around "what workflow is blocked" rather than "describe a
bug" shifts the user's mental model toward actionable reporting. If V-03 produces richer C-06
(reproducibility) and C-09 (enrichment) content than other variations, inertia framing is
driving better input collection. If scores are equal, the framing metaphor is neutral.

---

You are running `file-issue`. The goal is not just to record what happened -- it is to unblock
a workflow. A useful issue tells a maintainer what was interrupted, what was expected, and
exactly how to restore the flow. Frame everything around the blocked workflow.

---

**TRIAGE -- What is blocked?**

Collect the four required fields. For each absent field, ask before proceeding.

1. Which skill broke the workflow? (exact skill name -- e.g. `trace-permissions`, `draft-spec`)
2. What workflow step were you trying to complete? What should the skill have produced?
3. What happened instead? (paste verbatim output or error if available)
4. How severe is the blockage?
   - `crash` -- workflow is completely stopped; skill produced nothing or errored
   - `wrong-output` -- workflow can limp forward but output is wrong
   - `missing-feature` -- workflow requires a capability the skill does not have
   - `improvement` -- workflow works but a specific change would make it faster or clearer

Reject any severity value not in this exact list. Ask again until one of the four is chosen.

Collect without prompting: topic name, invocation string, related skills in the chain, version
or date. These tell the maintainer where in the workflow this occurred.

---

**DRAFT -- Write the issue around the blocked workflow**

Use the template for the selected severity.

**crash:**

  Title: [crash] {skill}: workflow blocked -- {one-line description of what could not complete}
  Severity: crash | Skill: `{skill}` | Priority: HIGH -- workflow non-resumable

  **Workflow step blocked**
  {what the user was trying to accomplish when this crash occurred}

  **Expected**
  {what the skill should have produced to advance the workflow}

  **Actual**
  {what happened instead -- error text, stack trace, or empty output verbatim}

  **Steps to reproduce**
  Invocation: `{invocation or not provided}`
  Topic: {topic or untracked}
  Chain: {related skills preceding this in the invocation chain}

  **Workflow impact**
  {which downstream steps in the workflow are now blocked by this crash}

  **Context**
  {version, date, related artifacts, or rubric references}

**wrong-output:**

  Title: [wrong-output] {skill}: workflow degraded -- {field or section} incorrect
  Severity: wrong-output | Skill: `{skill}`

  **Workflow step affected**
  {what the user was doing; how wrong output affects downstream steps}

  **Expected**
  {what the output should have contained to correctly advance the workflow}

  **Actual**
  {what the output contained instead}

  **Delta**
  {precise description of what is wrong -- field name, value, section, or structure}

  **Steps to reproduce**
  Invocation: `{invocation or not provided}`
  Topic: {topic or untracked}

  **Context**
  {related skills, version, date, or linked golden artifact}

**missing-feature:**

  Title: [missing-feature] {skill}: workflow gap -- {capability} not present
  Severity: missing-feature | Skill: `{skill}`

  **Workflow step blocked**
  {which workflow step requires this capability; what the user cannot do without it}

  **Expected**
  {describe the capability that should exist to unblock the workflow}

  **Actual**
  {confirm the capability is absent -- not just unused or hard to find}

  **Scope**
  {which inputs trigger the gap; which workflow branches are affected}

  **References**
  {spec, rubric criterion, or related skill that implies this capability should exist}

  **Context**
  {topic, invocation, version, or date}

**improvement:**

  Title: [improvement] {skill}: workflow friction -- {specific enhancement proposal}
  Severity: improvement | Skill: `{skill}`

  **Current workflow**
  {what the user has to do today; where the friction appears}

  **Proposed workflow**
  {what the improved skill would produce; how workflow friction is reduced}

  **Rationale**
  {why this matters -- frequency, downstream quality, rubric criterion, or example}

  **Acceptance condition**
  {exactly how you would confirm the improvement was correctly implemented; what output or
  behavior change would close this issue}

  **Context**
  {topic, invocation, related skills, version, or date}

---

**VALIDATE -- Check before writing**

DO NOT write the artifact until all checks pass. For each failure, apply the correction
and re-check immediately. Do not batch failures -- resolve them one at a time.

| Check | Pass condition | Correction on fail |
|-------|----------------|--------------------|
| Required fields complete | All 4 fields non-empty | Ask user for the missing field(s) |
| Severity enum | Exactly one of the four valid values | Re-prompt: choose from crash / wrong-output / missing-feature / improvement |
| Title names skill + symptom | No generic text; names specific skill and observable problem | Rewrite: "[{severity}] {skill}: {specific symptom}" |
| Reproducibility | Invocation, input, or sequence detail present for a maintainer to investigate | Add Topic and Invocation to Steps; ask user if both are still absent |
| Workflow frame present | At least one workflow-framing section is populated (Workflow step blocked / Workflow impact / Current workflow) | Populate the framing section from the user's description of what they were trying to do |
| Tone matches severity | crash = urgent + priority + impact; improvement = constructive + proposal + acceptance condition | Rewrite using tone and section structure from the severity template |
| Context enriched | At least one item beyond the 4 required fields in the Context section | Add topic, invocation, chain, version, or date |

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

Body: complete issue text (post-validation revision if any checks failed).

**OFFER**

  Artifact written: simulations/feedback/{skill}-issue-{date}.md
  Open as GitHub issue?

    gh issue create \
      --title "[{severity}] {skill}: {symptom}" \
      --label "{severity}" \
      --body-file simulations/feedback/{skill}-issue-{date}.md

---

## V-04 -- Lifecycle Compression: Two Macro-Phases (COLLECT+DRAFT / VALIDATE+WRITE)

**Axes**: Lifecycle emphasis + role sequence (combination)
**Hypothesis**: Compressing four phases into two macro-phases (A: collect+draft; B: validate+write)
preserves structural blocking at the phase boundary while halving instruction overhead. If V-04
scores the same as Round 2 V-04 on all criteria -- especially C-10 (blocking gate) -- then the
gate property comes from the explicit blocking instruction at the phase boundary, not from having
four distinct phases. If V-04 fails C-10, the four-phase structure is structurally necessary.

---

You are running `file-issue`. Two phases. Phase A produces a draft. Phase B validates and writes.
Do not begin Phase B until Phase A is complete.

---

## PHASE A -- COLLECT + DRAFT

**A1 -- Triage and collect**

Select severity first. Load the matching input form.

  crash          -- skill threw an error or produced no output
  wrong-output   -- skill ran but output was incorrect
  missing-feature -- capability the spec implies was absent
  improvement    -- skill works; specific enhancement proposed

Severity must be exactly one of these four. Reject any other value and re-prompt.

Load the severity form. Ask the user to fill in all required fields before drafting.

| Form field | crash | wrong-output | missing-feature | improvement |
|------------|-------|--------------|-----------------|-------------|
| Skill | required | required | required | required |
| Expected | required | required | required | required |
| Actual | required | required | required | required |
| Acceptance condition | -- | -- | -- | required |
| Priority / Impact | required | -- | -- | -- |
| Delta | -- | required | -- | -- |
| Scope / References | -- | -- | recommended | -- |
| Topic, Invocation, Chain, Version | optional | optional | optional | optional |

**A2 -- Draft using the severity template**

Construct the GitHub issue body using the template for the selected severity.

**crash template:**

  Title: [crash] {skill}: unhandled error -- {one-line description}
  Severity: crash | Skill: `{skill}` | Priority: HIGH -- skill non-functional

  **Expected**: {expected}
  **Actual**: {actual -- verbatim error or output}
  **Impact**: {what workflow is blocked by this crash}
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
  **Context**: {related skills, version, date}

**missing-feature template:**

  Title: [missing-feature] {skill}: {capability} not implemented
  Severity: missing-feature | Skill: `{skill}`

  **Expected**: {capability that should exist}
  **Actual**: {confirmed absence}
  **Scope**: {inputs that trigger the gap; outputs affected}
  **References**: {spec, rubric, or related skill}
  **Context**: topic={topic} | invocation={invocation}

**improvement template:**

  Title: [improvement] {skill}: {specific enhancement}
  Severity: improvement | Skill: `{skill}`

  **Current behavior**: {actual}
  **Proposed behavior**: {expected}
  **Rationale**: {why this matters}
  **Acceptance condition**: {how you confirm the improvement is done}
  **Context**: topic={topic} | related={related}

---

## PHASE B -- VALIDATE + WRITE

**DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE (all required fields filled, draft written).**

**B1 -- Validate**

Run all checks. On failure, apply the correction immediately and re-check the row before
continuing. Do not proceed to B2 until every row shows PASS.

| Check | Pass condition | Correction on fail |
|-------|----------------|--------------------|
| All required fields present | No required form field is empty for this severity | Ask user for the specific missing field(s) |
| Severity enum | Exactly one of the four valid values | Re-prompt the severity enum |
| Title names skill + symptom | No generic text; specific skill and observable symptom | Rewrite: "[{severity}] {skill}: {specific symptom}" |
| Reproducibility | Invocation, input, topic, or event sequence present | Add Topic and Invocation; ask user if both absent |
| Tone matches template | Language matches the severity template's tone constraints | Rewrite using the tone requirements in the severity template |
| Context enriched | At least one item beyond the 4 required fields | Add topic, invocation, chain, version, date, or rubric reference |

**B2 -- Write**

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

Body: full issue text from Phase A (post-B1 revision if any checks failed).

**B3 -- Offer**

  Artifact written: simulations/feedback/{skill}-issue-{date}.md
  Open as GitHub issue?

    gh issue create \
      --title "[{severity}] {skill}: {symptom}" \
      --label "{severity}" \
      --body-file simulations/feedback/{skill}-issue-{date}.md

---

## V-05 -- Minimal-Token Density: All 13 Criteria, Densest Form

**Axis**: Phrasing register (compressed/technical, single-axis)
**Hypothesis**: The minimum structural signal for each criterion is: C-01 a field list with
required markers, C-02 an explicit reject-and-reprompt instruction, C-03 a titled-and-sectioned
template block, C-04 an explicit path instruction, C-05 a title pattern with {skill}+{symptom},
C-06 a reproducibility field in the template, C-07 a gh command in the offer, C-08/C-12 four
named template blocks with structurally distinct required fields, C-09 a context field,
C-10 a STOP instruction before write, C-11 a remedy column, C-13 --label in the gh command.
If V-05 scores the same as V-04 on all criteria, token count is irrelevant to compliance.
If V-05 fails C-10 or C-12, the structural apparatus of V-04 is load-bearing.

---

Signal `file-issue`. Capture issue, write artifact, offer GitHub issue.

**INTAKE**

Collect all four required fields. For any absent field, ask before drafting.

- Skill [required]: exact skill name
- Severity [required]: crash / wrong-output / missing-feature / improvement only; reject all other values and re-prompt
- Expected [required]: what should have happened
- Actual [required]: what did happen -- paste verbatim output or error if available

Also collect without prompting: topic, invocation, related skills, version or date.

**DRAFT**

Use the template for the selected severity. Template determines structure; do not merge or substitute.

*crash:*
  Title: [crash] {skill}: unhandled error -- {description}
  Severity: crash | Skill: `{skill}` | Priority: HIGH -- skill non-functional
  **Expected**: {expected}
  **Actual**: {actual -- verbatim}
  **Impact**: {what workflow is blocked}
  **Reproduce**: Invocation: `{invocation}` | Topic: {topic} | Chain: {chain}
  **Context**: {version, date, artifacts}

*wrong-output:*
  Title: [wrong-output] {skill}: {section} incorrect -- expected {X}, got {Y}
  Severity: wrong-output | Skill: `{skill}`
  **Expected**: {expected}
  **Actual**: {actual}
  **Delta**: {precise difference}
  **Reproduce**: Invocation: `{invocation}` | Topic: {topic}
  **Context**: {related, version, date}

*missing-feature:*
  Title: [missing-feature] {skill}: {capability} not implemented
  Severity: missing-feature | Skill: `{skill}`
  **Expected**: {capability that should exist}
  **Actual**: {confirmed absence}
  **Scope**: {triggering inputs; affected outputs}
  **References**: {spec, rubric, or related skill}
  **Context**: topic={topic} | invocation={invocation}

*improvement:*
  Title: [improvement] {skill}: {enhancement proposal}
  Severity: improvement | Skill: `{skill}`
  **Current behavior**: {actual}
  **Proposed behavior**: {expected}
  **Rationale**: {why this matters}
  **Acceptance condition**: {how you confirm it is done -- required for improvement}
  **Context**: topic={topic} | related={related}

**PRE-WRITE GATE -- STOP. Do not write until all rows pass. Apply remedy on each failure; re-check.**

| # | Check | Pass | Remedy on fail |
|---|-------|------|----------------|
| 1 | All 4 required fields present | Skill, Severity, Expected, Actual non-empty | Ask user for the missing field(s) |
| 2 | Severity is valid enum | Exactly one of the four values | Re-prompt: choose from crash / wrong-output / missing-feature / improvement |
| 3 | Title: skill + symptom | No generic text; names specific skill and specific problem | Rewrite: "[{severity}] {skill}: {specific symptom}" |
| 4 | Reproducibility present | Invocation, input, topic, or event sequence in body | Add Topic + Invocation to Reproduce; ask user if both absent |
| 5 | Severity tone matches template | crash=urgent+priority+impact; improvement=proposal+acceptance | Rewrite using the template tone for this severity |
| 6 | Context enriched | At least one item beyond the 4 required fields present | Add any available: topic, invocation, chain, version, date, rubric ref |

**WRITE**

Path: `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md`

Frontmatter: skill: file-issue | topic: {topic or untracked} | item: issue | date: {YYYY-MM-DD} | severity: {severity} | target_skill: {skill}

Body: issue text from DRAFT (post-gate revision if any checks failed).

**OFFER**

  Artifact: simulations/feedback/{skill}-issue-{date}.md
  Open as GitHub issue?
    gh issue create --title "[{severity}] {skill}: {symptom}" --label "{severity}" --body-file simulations/feedback/{skill}-issue-{date}.md
