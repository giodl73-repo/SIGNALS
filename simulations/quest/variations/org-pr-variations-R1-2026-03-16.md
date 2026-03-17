Now I have all the context I need. Generating the 5 variations.

---

# org-pr — Quest Variate R1 — 5 Complete Variations

**Skill**: org-pr
**Rubric**: v1 (2026-03-16)
**Input variable**: `{{diff}}`
**Role set**: architect, security, testing, compliance, performance, UX
**Single-axis variations**: V-01 (role sequence), V-02 (output format), V-03 (phrasing register)
**Combination variations**: V-04 (lifecycle emphasis + inertia framing), V-05 (role sequence + output format + phrasing)

---

## V-01 — Role Sequence: Risk-First Ordering

**Axis**: Role sequence
**Hypothesis**: Security and testing run first because they have no incentive to rationalize the author's choices. If the highest-risk perspectives run before architect or UX, they anchor the review on actual failure modes rather than on what the code intended to do. Later roles that see the diff are influenced by what came before; leading with adversarial roles maximizes author-blind findings.

---

```
You are running `org-pr` on the pull request diff below.

`org-pr` runs a PR through the full org. Each relevant role reviews the diff from their
perspective. Roles are selected based on which files changed. Every finding is tagged P1,
P2, or P3. Output closes with a go/no-go recommendation derived from the findings.

---

## SETUP

Read the diff. Before any reviewer runs:

**File Manifest**
List every file changed in the diff. For each file, name its type (e.g., API surface,
auth logic, schema, test file, config, UI component, etc.).

| File | Type | Change Summary (one line) |
|------|------|--------------------------|
| ...  | ...  | ...                      |

**Role Selection**
For each role below, state INCLUDED or EXCLUDED and one sentence of rationale based
on the File Manifest above. A role is excluded only if no changed file touches its concern.

| Role | Decision | Rationale |
|------|----------|-----------|
| security | INCLUDED / EXCLUDED | [which file(s) triggered this, or why excluded] |
| testing | INCLUDED / EXCLUDED | ... |
| architect | INCLUDED / EXCLUDED | ... |
| performance | INCLUDED / EXCLUDED | ... |
| ux | INCLUDED / EXCLUDED | ... |
| compliance | INCLUDED / EXCLUDED | ... |

Only INCLUDED roles produce reviewer sections. Excluded roles do not appear below.

---

## REVIEWER SECTIONS

Run roles in this order: security first, testing second, architect third,
performance fourth, ux fifth, compliance last.
This order is fixed. Do not reorder.

For each INCLUDED role, produce one section using this template:

---

### [ROLE NAME]

**Files reviewed**: [list from File Manifest that this role covers]

**Findings**:

| # | Finding | File / Location | Severity |
|---|---------|-----------------|----------|
| 1 | [finding] | [file:function or pattern] | P1 / P2 / P3 |
| 2 | ... | ... | ... |

Every finding requires a severity. If this role has no findings, write:
> No findings. No concerns from this role's perspective given the changed files.

**Top concern**: [One sentence — the single issue this role would block on, or "None".]

---

## CONSENSUS ANALYSIS

After all reviewer sections are complete:

**Convergence** (2+ roles independently flagged the same surface):
- [surface] — flagged by [role-A] and [role-B] — this is the highest-confidence signal
  in the review.
- (repeat for each convergence point, or write "None detected.")

**Conflicts** (two roles with incompatible assessments of the same surface):
- [role-A] says [X], [role-B] says [Y] — tension: [one sentence]
- (repeat, or write "None detected.")

---

## GO / NO-GO

**Open P1 findings**: [list any P1 findings by role and finding number, or "None"]

**Verdict**: Go / No-Go

**Basis**: [One sentence. If No-Go: name the specific P1 finding(s) that block it.
If Go: state the highest-severity open item the team accepts.]

**Formula**: Any open P1 = No-Go. This formula is not editable at this step.

---

**Pull request diff:**

{{diff}}
```

---

## V-02 — Output Format: Severity Matrix

**Axis**: Output format (table-driven matrix vs prose)
**Hypothesis**: A single unified findings matrix — all roles, all findings in one table — makes P1/P2/P3 coverage mechanically verifiable at a glance and eliminates the risk of an untagged finding hiding in prose. Cross-role comparison is immediate. The go/no-go formula becomes a simple filter on the Severity column.

---

```
You are running `org-pr` on the pull request diff below.

`org-pr` runs each relevant org role through the diff and produces a structured findings
matrix. Every row in the matrix carries a role, a severity, and a specific file locator.
The matrix is the complete output. Go/no-go is derived from it by formula.

---

## STEP 1 — FILE MANIFEST

List every changed file. One row per file.

| File | Category | Change Type |
|------|----------|-------------|
| [filename] | [auth / schema / UI / config / test / API / other] | [add / modify / delete] |

---

## STEP 2 — ROLE SELECTION MANIFEST

For each role, mark ACTIVE or SKIP. A role is ACTIVE if any file in the manifest
falls within its concern. Write one sentence of rationale.

| Role | Status | Triggered By |
|------|--------|--------------|
| architect | ACTIVE / SKIP | [file(s) or "no architectural surface changed"] |
| security | ACTIVE / SKIP | [file(s) or "no auth/input/crypto/secret surface"] |
| testing | ACTIVE / SKIP | [file(s) or "no test files and no testability impact"] |
| compliance | ACTIVE / SKIP | [file(s) or "no data handling, logging, or policy surface"] |
| performance | ACTIVE / SKIP | [file(s) or "no hot path, query, or resource surface"] |
| ux | ACTIVE / SKIP | [file(s) or "no user-visible surface changed"] |

---

## STEP 3 — FINDINGS MATRIX

All findings from all ACTIVE roles in one table. Each row is one finding.
Do not group by role in separate sections — every finding goes in this table.

| # | Role | Severity | File / Location | Finding |
|---|------|----------|-----------------|---------|
| 1 | [role] | P1 / P2 / P3 | [file:function or named pattern] | [one sentence] |
| 2 | ... | ... | ... | ... |

**Rules**:
- Every finding must have a severity. No row may omit the Severity column.
- Every finding must have a location. "General concern" is not a location.
- If an ACTIVE role has zero findings, add one row: role=[role], severity=P3,
  location="n/a", finding="No concerns from this role's perspective."
- Minimum 2 ACTIVE roles must contribute at least one non-null finding row.

---

## STEP 4 — CONSENSUS ANALYSIS

Using the Findings Matrix above:

**P1 count**: [N] — rows where Severity = P1
**P2 count**: [N]
**P3 count**: [N]

**Convergence** — same file or pattern flagged by 2+ roles independently:
| Surface | Roles | Signal Strength |
|---------|-------|-----------------|
| [file/pattern] | [role-A, role-B] | HIGH (2 roles) / MEDIUM (2 roles, different concern) |
(Write "None" if no convergence.)

**Conflicts** — incompatible findings on the same surface:
| Surface | Role A Says | Role B Says |
|---------|-------------|-------------|
| [surface] | [finding] | [finding] |
(Write "None" if no conflicts.)

---

## STEP 5 — GO / NO-GO

**Formula** (immutable — apply without editorial override):
```
P1 count > 0  -->  No-Go
P1 count = 0  -->  Go
```

**Verdict**: Go / No-Go

**Basis**: [One sentence. If No-Go: cite row numbers from Findings Matrix with P1 severity.
If Go: cite the highest-severity open item accepted.]

---

**Pull request diff:**

{{diff}}
```

---

## V-03 — Phrasing Register: Question-First (Conversational)

**Axis**: Phrasing register (formal/imperative vs conversational/question-driven)
**Hypothesis**: Asking each role to state its questions before its findings produces more author-blind output. Questions surface what the reviewer doesn't know or doesn't trust; findings state what the reviewer already concluded. A question-first pattern generates the "what if the author got this wrong?" concern that a direct-findings instruction suppresses.

---

```
You are running `org-pr`. Your job is to read this pull request as if you wrote none of it.

For each role that applies to this diff, ask: what would a careful reviewer in that role
want to know before approving? Then answer those questions with findings.

---

## Read the diff first.

Before assigning roles, answer:
- What is this PR trying to do? (One sentence, from the diff alone — no author explanation.)
- Which files changed, and what do those files touch? (List them.)
- Which of these changed areas could surprise a reviewer: auth, data, test coverage,
  user-facing behavior, performance-sensitive paths, policy-governed fields?

---

## Role selection

For each role listed, decide: does this PR touch their concern?

- **architect** — system design, module boundaries, contract changes
- **security** — auth, secrets, input validation, trust boundaries, data exposure
- **testing** — coverage, missing tests, test-only changes that don't test the right thing
- **compliance** — logging, PII, retention, audit trail, regulated fields
- **performance** — query plans, loops on hot paths, unbounded operations, caching effects
- **ux** — user-visible text, error messages, flow changes, accessibility

For each role you include, write one sentence: "I'm including [role] because [specific file
or pattern] touches their concern."

For each role you exclude, write one sentence: "I'm excluding [role] because no changed
file touches their concern."

---

## Reviewer sections

For each included role, write their review in this format:

---

### [Role name]

**Questions this reviewer would ask** (before seeing the findings — ask as the reviewer,
not the author):
1. [Question — what doesn't the reviewer trust or understand from the diff alone?]
2. [Question — what assumption might the author have made that a reviewer would challenge?]
3. [Optional third question]

**Findings** (answer the questions with specific evidence from the diff):

For each finding, write:
> [P1 / P2 / P3] — [file or specific location] — [what the issue is, in one sentence]

If a question has no corresponding finding, write:
> [P3] — [question answered] — No issue found. [one sentence explaining what was checked.]

Every question must produce at least a "no issue found" finding. No finding may be
left untagged.

**What would block this reviewer from approving?**
[One sentence: the single concern this role would not let through, or "Nothing blocks —
this role is satisfied."]

---

## After all reviewers

**What did two or more reviewers worry about independently?**
[Name the surface and the roles. This is the convergence signal — it has higher confidence
than any single-role finding.]

**Did any two reviewers reach opposite conclusions about the same surface?**
[Name the conflict and explain why it's unresolved, or write "No conflicts."]

---

## Verdict

Look at your findings. Count the P1s.

If any P1 exists: **No-Go**. State which finding blocks it and what would need to change.

If no P1 exists: **Go**. State the highest-severity unresolved concern the team accepts
by merging.

Write the verdict clearly: **Go** or **No-Go**, followed by one sentence of basis.

---

**Pull request diff:**

{{diff}}
```

---

## V-04 — Combination: Lifecycle Emphasis + Inertia Framing

**Axes**: Lifecycle emphasis (explicit file-manifest gate before reviewers unlock) + inertia framing (a "should this PR merge at all?" challenger voice before domain reviewers run)
**Hypothesis**: A hard lifecycle gate — where reviewers cannot run until the file manifest is verified — forces specificity in role selection and prevents generic findings. Adding an explicit inertia voice ("what argues against merging this?") before domain reviewers run generates the non-obvious cross-cutting concern that no individual domain role would produce, because it frames the PR as a candidate for rejection rather than a candidate for approval.

---

```
You are running `org-pr` on the pull request diff below.

`org-pr` has three phases. Each phase must complete before the next begins.
Do not begin Phase 2 until Phase 1 is complete. Do not begin Phase 3 until Phase 2 is complete.

---

## PHASE 1 — DIFF ANALYSIS GATE

**[GATE: complete this section in full before any reviewer runs]**

### Changed files

| # | File | Type | Lines +/- | What changed (one line) |
|---|------|------|-----------|--------------------------|
| 1 | [file] | [type] | [+N / -N] | [summary] |
...

### Concern surface map

Based on the changed files, which surfaces are live in this diff?

| Surface | Live? | Evidence (file name) |
|---------|-------|----------------------|
| Authentication / authorization | YES / NO | [file or "none"] |
| Input validation / trust boundary | YES / NO | ... |
| Data schema / migration | YES / NO | ... |
| Test coverage | YES / NO | ... |
| User-visible behavior | YES / NO | ... |
| Performance-sensitive path | YES / NO | ... |
| Policy-governed data (PII, audit, retention) | YES / NO | ... |
| Module boundary / public contract | YES / NO | ... |

### Role activation

| Role | Activated? | Activating surface |
|------|------------|--------------------|
| architect | YES / NO | [surface from map, or "none"] |
| security | YES / NO | ... |
| testing | YES / NO | ... |
| compliance | YES / NO | ... |
| performance | YES / NO | ... |
| ux | YES / NO | ... |

**[GATE CLEARED — Phase 2 may begin]**

---

## PHASE 2 — CHALLENGER REVIEW (before domain reviewers run)

Before the domain roles see the diff, the challenger asks: should this PR merge at all?

The challenger is not a domain reviewer. They argue from inertia: what is the case for
*not* merging this? This is not about bugs. It is about whether the change is necessary,
safe to ship now, or whether deferring it is the stronger move.

**What does the team do today without this change?** [One sentence — the status quo.]

**Case for not merging**:
1. [Argument 1 — why the status quo might be acceptable]
2. [Argument 2 — timing, scope, or coupling risk]
3. [Argument 3 — optional: a non-obvious reason this could be deferred safely]

For each argument: severity P1 / P2 / P3.

**Challenger verdict**: Merge / Defer / Block
**Basis**: [One sentence.]

*The challenger verdict is advisory. It does not override domain findings.
But if it is Block, the overall verdict must be No-Go regardless of domain findings.*

---

## PHASE 3 — DOMAIN REVIEWER SECTIONS

For each activated role from Phase 1, run their review now.
The challenger's case from Phase 2 is visible to domain reviewers. They may address or
contest any challenger argument.

For each activated role:

---

### [ROLE NAME]

**Challenger argument response** (optional — only if this role's domain perspective
bears on one of the challenger's arguments):
> [CH-N]: [role's response in one sentence, or "Not in this role's scope."]

**Findings**:

| Severity | Location (file / function / pattern) | Finding |
|----------|--------------------------------------|---------|
| P1 / P2 / P3 | [specific locator] | [finding in one sentence] |
...

If no findings: state "No concerns from this role given the activated surfaces."

**Would this role block the merge?** Yes (P1) / Conditional (P2) / No

---

## CONSENSUS ANALYSIS

**Convergence** (2+ roles flagged the same surface independently):
[List each convergence point. If none: "None detected."]

**Conflicts** (roles with incompatible assessments):
[List each conflict. If none: "None detected."]

**Challenger argument status**:
- CH-1: [Addressed / Unaddressed — by which role(s)]
- CH-2: [Addressed / Unaddressed]
- CH-3: [Addressed / Unaddressed, if active]

---

## GO / NO-GO

**Formula**:
```
Challenger verdict = Block                 --> No-Go (override)
Any P1 finding in domain sections          --> No-Go
Challenger = Defer AND no P1               --> Go (with noted conditions)
All verdicts clear                         --> Go
```

**P1 findings**: [list, or "None"]
**Challenger verdict**: [from Phase 2]

**Verdict**: Go / No-Go

**Basis**: [One sentence naming the primary driver — P1 finding, challenger block, or
highest-severity accepted condition.]

---

**Pull request diff:**

{{diff}}
```

---

## V-05 — Full Combination: Risk-First Sequence + Table Format + Imperative Phrasing

**Axes combined**: Role sequence (security leads, V-01) + output format (matrix table, V-02) + phrasing register (imperative direct commands, V-03 inverse — no conversational hedging)
**Hypothesis**: Combining risk-first sequencing, a unified findings matrix, and imperative phrasing produces the most consistently structured output under the rubric. The imperative register ("Produce exactly one row per finding") removes the model's freedom to describe findings narratively, which is how P1/P2/P3 tags get omitted. The risk-first sequence anchors the matrix on adversarial findings before optimization-oriented roles (UX, performance) soften the tone.

---

```
You are running `org-pr`. Execute each step exactly as written. Do not narrate.
Do not add explanatory prose between sections. Fill every labeled field.

---

## STEP 1 — FILE MANIFEST

Produce this table. One row per changed file. No omissions.

| File | Type | Change Class |
|------|------|--------------|
| [filename] | [auth / schema / test / config / UI / API / infra / other] | [add / modify / delete] |

---

## STEP 2 — ROLE ACTIVATION TABLE

Evaluate each role against the File Manifest. Mark ACTIVE or INACTIVE.
Write exactly one sentence of rationale. Do not skip any row.

Roles activate in this evaluation order but run in the sequence defined in Step 3.

| Role | Status | File(s) That Activate It |
|------|--------|--------------------------|
| security | ACTIVE / INACTIVE | [specific files or "none"] |
| testing | ACTIVE / INACTIVE | [specific files or "none"] |
| architect | ACTIVE / INACTIVE | [specific files or "none"] |
| performance | ACTIVE / INACTIVE | [specific files or "none"] |
| ux | ACTIVE / INACTIVE | [specific files or "none"] |
| compliance | ACTIVE / INACTIVE | [specific files or "none"] |

Minimum 2 rows must be ACTIVE. If fewer than 2 roles activate, reassess the File Manifest
— a change with no security, testing, or architectural surface is unusual and warrants
re-examination.

---

## STEP 3 — FINDINGS MATRIX

Run all ACTIVE roles in this fixed sequence: security, testing, architect, performance, ux,
compliance. Skip INACTIVE roles silently — do not produce a row for them.

Produce one unified table. One row per finding. No findings may live outside this table.

| Row | Role | Severity | File | Location (function / line / pattern) | Finding |
|-----|------|----------|------|---------------------------------------|---------|
| 1 | security | P1 / P2 / P3 | [file] | [specific locator] | [one sentence] |
| 2 | testing | P1 / P2 / P3 | [file] | [specific locator] | [one sentence] |
...

**Mandatory rules — enforce mechanically**:
1. Every row must have a Severity value of P1, P2, or P3. No other values permitted.
2. Every row must have a File value from the File Manifest. "General" is not a file.
3. Every row must have a Location value. "Throughout" is not a location.
4. Each ACTIVE role must contribute at least one row. If a role has no findings, produce:
   `| [N] | [role] | P3 | n/a | n/a | No concerns from this role's perspective. |`
5. Security and testing rows appear before architect rows. Architect rows appear before
   performance, ux, and compliance rows. This ordering is enforced.

---

## STEP 4 — SEVERITY SUMMARY

Count rows from the Findings Matrix.

| Severity | Count | Row Numbers |
|----------|-------|-------------|
| P1 | [N] | [row list] |
| P2 | [N] | [row list] |
| P3 | [N] | [row list] |
| Total | [N] | — |

---

## STEP 5 — CONSENSUS ANALYSIS

**Convergence**: Identify files or patterns that appear in 2+ rows from different roles.

| Surface | Roles | Row Numbers | Confidence |
|---------|-------|-------------|------------|
| [file/pattern] | [role-A, role-B] | [rows] | HIGH / MEDIUM |
(Write "None detected." if no surface appears in 2+ rows from different roles.)

**Conflicts**: Identify rows where two roles reached incompatible conclusions about the
same surface.

| Surface | Role A / Row | Role B / Row | Tension |
|---------|-------------|-------------|---------|
| [surface] | [role/row] | [role/row] | [one sentence] |
(Write "None detected." if no incompatible assessments exist.)

---

## STEP 6 — GO / NO-GO

Apply this formula. Do not editorialize. Evaluate the Severity Summary mechanically.

```
P1 count (from Step 4) > 0  -->  No-Go
P1 count = 0                -->  Go
```

**P1 count**: [copy from Step 4]

**Verdict**: Go / No-Go

**Basis**: [One sentence.]
- If No-Go: "Blocked by row(s) [N, N] — [P1 finding summary in one clause]."
- If Go: "Highest open item: row [N], [role], P[N] — [finding summary]."

---

**Pull request diff:**

{{diff}}
```

---

## Variation Summary

| Variation | Axis | Single/Combo | Key Structural Bet |
|-----------|------|-------------|-------------------|
| V-01 | Role sequence (risk-first) | Single | Security+testing run before architect anchors the frame |
| V-02 | Output format (unified matrix) | Single | One table enforces P1/P2/P3 coverage mechanically |
| V-03 | Phrasing register (question-first) | Single | Questions before findings surfaces author-blind assumptions |
| V-04 | Lifecycle emphasis + inertia framing | Combo | File-manifest gate + challenger voice generates non-obvious cross-cutting concerns |
| V-05 | Risk-first + matrix + imperative phrasing | Combo | All three single-axis bets combined; imperative removes model freedom to omit tags |

**Rubric prediction before scoring**:
- V-01 most likely to pass C-03 (file-based selection) and C-09 (author-blind perspective)
- V-02 most likely to pass C-02 (P1/P2/P3 on every finding) and C-07 (P1 blocks go) mechanically
- V-03 most likely to pass C-10 (non-obvious issue) — questions surface what the model wouldn't otherwise ask
- V-04 most likely to pass C-10 and C-06 (consensus analysis) — challenger + lifecycle emphasis
- V-05 most likely to pass the full essential band (C-01 through C-05) as a floor; C-09 and C-10 are the risk

**Weakest criterion across all five**: C-09 (author-blind challenge perspective) — every variation instructs the model to find issues but none explicitly instructs it to *challenge the diff's stated intent*. If V-03 (question-first) doesn't surface this, a V-06 should target C-09 directly with an explicit "assume the author's stated reason is wrong" instruction.
