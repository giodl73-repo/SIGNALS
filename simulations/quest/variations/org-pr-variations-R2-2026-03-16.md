Written to `simulations/quest/variations/org-pr-variations-R2-2026-03-16.md`.

---

## R2 Variations — Summary

Five complete prompt bodies targeting the aspirational criteria added in rubric v2:

| Variation | Primary Target | Key Mechanism |
|-----------|---------------|---------------|
| **V-01** | C-12 (locator anti-pattern) | `LOCATOR RULES` block with named disallowed forms: "The codebase is not a location", "Throughout is not a location", etc. |
| **V-02** | C-11 (formula lock) | Dedicated formula block: "not editable" + reclassify-or-accept closure removes the third option entirely |
| **V-03** | C-13 (inertia framing) | Required `If this stays in:` line on every finding — must name a specific downstream failure mode, not a vague risk |
| **V-04** | C-09 (author-blind) | Assumption audit (3+ assumptions rated by suspicion) + each reviewer must challenge at least one before producing findings |
| **V-05** | C-09 + C-11 + C-12 + C-13 | All four mechanisms on the R1 V-02 matrix base — findings matrix has both a valid locator column and an `If this stays in` column |

**Scoring prediction**: V-05 has the highest composite ceiling but also the highest execution complexity. V-02 is the cleanest single-mechanism bet — formula lock is a one-block addition to an otherwise proven structure. If V-05 degrades on execution, a V-06 should inject the V-02 formula block verbatim into V-05 without other changes.
m. Negative examples are a stronger guard than a floor percentage alone.

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

## STEP 3 — LOCATOR RULES

**What counts as a locator** (every finding must have one):
- File name: `auth/middleware.ts`
- File + function: `auth/middleware.ts:validateToken`
- File + line range: `auth/middleware.ts:L42-L57`
- Named code pattern: `validateToken error branch`
- Named config key: `RATE_LIMIT_MAX in config/throttle.yaml`

**What does NOT count as a locator** (reject any finding that uses only these):
- "The codebase" — not a location
- "This area" — not a location
- "Throughout" — not a location
- "The auth module" without a filename — not a location
- "The relevant file" — not a location
- "General concern" — not a location
- "The changed files" — not a location

If you draft a finding and its location field contains any disallowed form, rewrite
the location before adding it to the matrix.

---

## STEP 4 — FINDINGS MATRIX

All findings from all ACTIVE roles in one table. Each row is one finding.

| # | Role | Severity | File | Location (function / line / pattern) | Finding |
|---|------|----------|------|---------------------------------------|---------|
| 1 | [role] | P1 / P2 / P3 | [filename from manifest] | [locator per Step 3 rules] | [one sentence] |
| 2 | ... | ... | ... | ... | ... |

**Rules**:
- Every finding must have a severity of P1, P2, or P3. No other values permitted.
- Every finding must have a location that passes the locator rules in Step 3.
- If an ACTIVE role has zero findings, add one row:
  role=[role], severity=P3, file="n/a", location="n/a", finding="No concerns from this role's perspective."
- Minimum 2 ACTIVE roles must contribute at least one non-null finding row.

---

## STEP 5 — CONSENSUS ANALYSIS

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

## STEP 6 — GO / NO-GO

**Formula** (apply without editorial override):
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

## V-02 — Formula Lock (targeting C-11)

**Axis**: Non-overridable verdict formula — explicitly blocking rationalization
**Hypothesis**: R1 V-01 applied the formula correctly ("this formula is not editable at this step") and that language was noted as an excellence signal. V-02 makes formula lock structural: a dedicated block explains not only the formula but why it cannot be rationalized away and what to do if you disagree with it. The argument is: if you believe a P1 is not serious enough to block, you have misclassified it. Reclassify to P2, or accept the No-Go. This closes the rationalization path at the source.

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

## SEVERITY CLASSIFICATION GUIDE

Before running reviewer sections, read this classification guide once.

**P1 — Must fix before merge**. This finding, if not resolved, would cause a production
failure, security breach, data loss, test coverage collapse, or regulatory violation that
cannot be patched after the fact.

**P2 — Should fix soon**. This finding represents technical debt, a gap in coverage,
or a risk that is currently contained but will compound under normal usage.

**P3 — Low risk / informational**. This finding is a suggestion, an improvement opportunity,
or a potential future concern with no current failure path.

**Ambiguous between P1 and P2**: If you are unsure whether a finding is P1 or P2, ask:
"Would this cause an incident in production within the first week of shipping?" If yes, P1.
If no, P2.

---

## VERDICT FORMULA

```
Any open P1 finding  -->  No-Go
Zero open P1 findings  -->  Go
```

**This formula is not editable. It applies without exception.**

It does not matter if:
- The P1 finding is in a code path that "probably won't be hit"
- The team is close to a deadline
- The finding would be easy to patch post-merge
- Other reviewers think the risk is low

If you believe a finding you tagged P1 is not actually serious enough to block the merge,
you have two choices:
1. Reclassify it as P2, and explicitly explain why it does not meet the P1 threshold above.
2. Accept the No-Go verdict.

There is no third choice. The formula cannot be rationalized away at this step.

---

## REVIEWER SECTIONS

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
- [surface] — flagged by [role-A] and [role-B]
- (repeat for each convergence point, or write "None detected.")

**Conflicts** (two roles with incompatible assessments of the same surface):
- [role-A] says [X], [role-B] says [Y] — tension: [one sentence]
- (repeat, or write "None detected.")

---

## GO / NO-GO

**Open P1 findings**: [list any P1 findings by role and finding number, or "None"]

Apply the verdict formula from above. Do not editorialize. The formula is not editable.

**Verdict**: Go / No-Go

**Basis**: [One sentence. If No-Go: name the specific P1 finding(s) that block it.
If Go: state the highest-severity open item the team accepts.]

---

**Pull request diff:**

{{diff}}
```

---

## V-03 — Inertia Framing per Finding (targeting C-13)

**Axis**: Downstream failure framing — each finding answers "what breaks if this stays in"
**Hypothesis**: Generic findings describe the issue as it exists today ("this function doesn't validate input"). Inertia-framed findings describe the future state if the issue persists ("this validation gap means the next caller that passes null will receive a 500 in production, and the stack trace will be logged without scrubbing PII"). Requiring each finding to project forward forces the model to think about failure modes, not just code smells. This naturally surfaces non-obvious cross-cutting concerns (C-10) because downstream projections often touch surfaces outside the diff.

---

```
You are running `org-pr` on the pull request diff below.

`org-pr` runs a PR through the full org. Each relevant role reviews the diff from their
perspective and produces findings with downstream impact framing. Every finding answers
two questions: what is the issue, and what breaks if it is not fixed before merge.

---

## SETUP

**File Manifest**

| File | Type | Change Summary |
|------|------|----------------|
| [filename] | [type] | [one line] |

**Role Selection**

| Role | Decision | Rationale (which changed file activates this role) |
|------|----------|----------------------------------------------------|
| security | INCLUDED / EXCLUDED | ... |
| testing | INCLUDED / EXCLUDED | ... |
| architect | INCLUDED / EXCLUDED | ... |
| performance | INCLUDED / EXCLUDED | ... |
| ux | INCLUDED / EXCLUDED | ... |
| compliance | INCLUDED / EXCLUDED | ... |

---

## FINDING FORMAT

Each finding follows this three-part structure:

```
[P1 / P2 / P3] | [file:location] | [What the issue is]
  --> If this stays in: [specific failure mode, degradation, or compounding effect
      that would occur downstream if this issue is not resolved before merge]
```

The "If this stays in" line is required on every finding. It must:
- Name a specific downstream effect (not "this could cause problems")
- Reference a concrete failure mode, caller, or dependent system
- Describe what breaks, degrades, or becomes harder to fix over time

**Examples of passing "If this stays in" lines**:
- "If this stays in: the next authenticated request from a non-admin will silently succeed,
   bypassing the role check added in the prior PR."
- "If this stays in: the missing test will let a future refactor of this function ship without
   catching the off-by-one error that already exists in the branch logic."
- "If this stays in: the PII logged here will appear in the audit trail for 90 days, creating
   a compliance gap on the next data subject request."

**Examples of failing "If this stays in" lines** (do not use these):
- "This could cause issues later." — no specificity
- "This may become a problem." — no failure mode named
- "Future maintainers will be confused." — not a failure mode

---

## REVIEWER SECTIONS

For each INCLUDED role, produce one section:

---

### [ROLE NAME]

**Files reviewed**: [from File Manifest]

**Findings**:

[P1 / P2 / P3] | [file:location] | [issue in one sentence]
  --> If this stays in: [downstream failure mode, specific and concrete]

[repeat for each finding]

If this role has no findings:
> No concerns from this role's perspective. No failure modes identified in the activated surfaces.

**Top concern**: [The finding with the most serious downstream effect, or "None".]

---

## CONSENSUS ANALYSIS

**Convergence**: surfaces flagged by 2+ roles independently.
(Name each surface, the roles that flagged it, and whether their downstream projections agree.)

**Conflicts**: roles with incompatible assessments of the same surface.
(Name the tension. If none, write "None detected.")

---

## GO / NO-GO

**Open P1 findings**: [list, or "None"]

**Verdict**: Go / No-Go

**Formula**: Any open P1 = No-Go. This formula is not editable at this step.

**Basis**: [One sentence naming the primary driver — which P1 blocks (and its downstream effect),
or the highest-severity item accepted on a Go.]

---

**Pull request diff:**

{{diff}}
```

---

## V-04 — Author-Blind Challenge (targeting C-09)

**Axis**: Author-distrust instruction — explicit "assume the author's stated reason is wrong" framing
**Hypothesis**: R1 identified C-09 (author-blind perspective) as the weakest criterion across all five variations. Every R1 variation instructs the model to find issues, but none explicitly instruct it to challenge the diff's stated intent. A reviewer who assumes the author's code correctly implements its stated purpose will only find bugs. A reviewer who assumes the stated purpose might itself be wrong will find design assumptions worth questioning. This variation introduces a mandatory "assumption audit" before domain findings run, where the reviewer names the assumptions embedded in the diff and rates each one's suspicion level.

---

```
You are running `org-pr` on the pull request diff below. Your operating posture for
this review is author-blind: you have access to the diff but not to the PR description,
the author's intent, the ticket it closes, or any prior context the author would provide.
You reason only from what the diff shows.

This posture is intentional. The goal is to surface issues the author cannot self-identify
because they are too close to their own reasoning. Your job is to read the diff as if
you wrote none of it and trust nothing about why the changes were made.

---

## STEP 1 — FILE MANIFEST AND INTENT INFERENCE

List every changed file.

| File | Type | What this file change appears to be doing (from the diff alone) |
|------|------|------------------------------------------------------------------|
| [filename] | [type] | [one sentence — inferred from diff, no benefit of the doubt] |

**Inferred PR purpose** (from the diff alone, no author explanation):
[One sentence. If the diff's purpose is ambiguous, say so explicitly.]

---

## STEP 2 — ASSUMPTION AUDIT

Before domain reviewers run, identify the assumptions embedded in this diff.

An assumption is something the author must have believed to be true in order to write
this code the way they wrote it. Examples:
- "This input will always be validated upstream."
- "The caller will never pass null."
- "This code path is not reachable in production."
- "This table has no PII."
- "The existing tests cover this branch."

For each assumption you identify, rate its suspicion level:
- **Low** — the diff provides evidence this assumption is correct
- **Medium** — the diff neither confirms nor denies this assumption
- **High** — the diff provides no evidence this assumption holds, or there is evidence
  it may not hold

| # | Assumption embedded in diff | Suspicion | Evidence in diff (or "none") |
|---|----------------------------|-----------|------------------------------|
| A-1 | [assumption] | Low / Medium / High | [evidence or "none"] |
| A-2 | ... | ... | ... |

List at least 3 assumptions. If you cannot identify 3, look harder — every nontrivial
change embeds assumptions.

---

## STEP 3 — ROLE SELECTION

| Role | Decision | Files activated |
|------|----------|-----------------|
| security | INCLUDED / EXCLUDED | [files or "none"] |
| testing | INCLUDED / EXCLUDED | ... |
| architect | INCLUDED / EXCLUDED | ... |
| performance | INCLUDED / EXCLUDED | ... |
| ux | INCLUDED / EXCLUDED | ... |
| compliance | INCLUDED / EXCLUDED | ... |

---

## STEP 4 — REVIEWER SECTIONS

For each INCLUDED role, produce one section.

Each reviewer must address at least one assumption from the Assumption Audit (Step 2).
The reviewer's job is to challenge the assumption from their domain perspective — not
to confirm it. If the reviewer believes an assumption is safe, they must explain why
with evidence from the diff.

---

### [ROLE NAME]

**Assumptions this role challenges** (from Step 2):
- A-[N]: [one sentence — what this role's lens reveals about this assumption, especially
  if it is suspicious or unverifiable]

**Findings** (include at least one finding that challenges an embedded assumption, not
just a finding that identifies a bug):

| # | Finding | File / Location | Severity |
|---|---------|-----------------|----------|
| 1 | [finding — may reference an assumption: "Assumption A-2 is unverified: if X is false, then Y fails"] | [file:function] | P1 / P2 / P3 |

Every finding must have a severity.

**Top concern**: [one sentence — the assumption or finding this role would not let through]

---

## STEP 5 — CONSENSUS ANALYSIS

**Convergence** (2+ roles flagged the same surface or assumption):
[Name the surface, the roles, and which assumption it relates to if any.]

**Conflicts** (incompatible assessments):
[Name the tension, or "None detected."]

**Unresolved high-suspicion assumptions**:
[List any A-N assumptions still rated High after reviewer sections, with the roles that
tried to address them. These are the cross-cutting concerns the author could not self-identify.]

---

## STEP 6 — GO / NO-GO

**Open P1 findings**: [list, or "None"]

**Verdict**: Go / No-Go

**Formula**: Any open P1 = No-Go. This formula is not editable at this step.

**Basis**: [One sentence. Name the specific P1 or the highest-severity accepted condition.]

---

**Pull request diff:**

{{diff}}
```

---

## V-05 — Full Aspirational Combination (targeting C-09 + C-11 + C-12 + C-13)

**Axes combined**: Author-blind assumption audit (C-09, V-04) + formula lock (C-11, V-02) + locator anti-pattern (C-12, V-01) + inertia framing per finding (C-13, V-03) — all layered on the matrix base from R1 V-02
**Hypothesis**: The matrix format from R1 V-02 provided the strongest essential-band coverage (C-01 through C-05 nearly guaranteed). The four aspirational mechanisms from R2 V-01 through V-04 each target one criterion in isolation. Combining all four on the matrix base should produce the highest composite score — the essential band holds from the matrix structure, and the aspirational band opens from the four new mechanisms. The risk is prompt complexity overwhelming coherence; the counter-measure is clear labeled sections that isolate each mechanism so they reinforce rather than interfere.

---

```
You are running `org-pr` on the pull request diff below. Execute each phase in sequence.

`org-pr` runs a PR through the full org. Every finding includes a specific file locator
and a downstream impact statement. The go/no-go verdict is derived by formula. The
formula is not editable.

---

## PHASE 1 — DIFF ANALYSIS

### 1A — File Manifest

| # | File | Category | Change Type |
|---|------|----------|-------------|
| 1 | [filename] | [auth / schema / test / config / UI / API / infra / other] | [add / modify / delete] |

### 1B — Inferred Intent

One sentence: what does this diff appear to be doing, inferred from the changes alone
with no benefit of the doubt to the author?

### 1C — Assumption Audit

Every nontrivial diff embeds assumptions. List at least 3. For each, rate suspicion.

| # | Assumption embedded in diff | Suspicion |
|---|----------------------------|-----------|
| A-1 | [assumption] | Low / Medium / High |
| A-2 | ... | ... |
| A-3 | ... | ... |

---

## PHASE 2 — ROLE ACTIVATION

| Role | Status | File(s) That Activate It |
|------|--------|--------------------------|
| security | ACTIVE / INACTIVE | [specific files or "none"] |
| testing | ACTIVE / INACTIVE | ... |
| architect | ACTIVE / INACTIVE | ... |
| performance | ACTIVE / INACTIVE | ... |
| ux | ACTIVE / INACTIVE | ... |
| compliance | ACTIVE / INACTIVE | ... |

Minimum 2 rows must be ACTIVE.

---

## PHASE 3 — LOCATOR RULES

These rules apply to every row in the Findings Matrix.

**Valid locators** (use one of these forms):
- `filename.ext:functionName`
- `filename.ext:L42-L57`
- `filename.ext` + named code pattern (e.g., "error branch in validateToken")
- Named config key in a named config file

**Invalid locators** (if your finding uses one of these, rewrite it before adding to the matrix):
- "The codebase" — not a location
- "This area" or "this module" without a filename — not a location
- "Throughout" — not a location
- "The relevant file" — not a location
- "General concern" — not a location

If you cannot produce a valid locator for a finding, the finding is too vague to be actionable.
Either sharpen it to a specific location, or do not include it.

---

## PHASE 4 — FINDINGS MATRIX

All findings from all ACTIVE roles in one table. Roles run in this sequence: security,
testing, architect, performance, ux, compliance. Skip INACTIVE roles.

Each finding has two parts: the issue and the downstream impact.

| # | Role | Sev | File | Location | Issue | If this stays in |
|---|------|-----|------|----------|-------|-----------------|
| 1 | [role] | P1/P2/P3 | [file] | [valid locator per Phase 3] | [issue in one sentence] | [specific downstream effect or failure mode] |

**Rules**:
- Severity must be P1, P2, or P3. No other values.
- Location must pass Phase 3 locator rules.
- "If this stays in" must name a specific failure mode, not a vague risk.
- Each ACTIVE role must contribute at least one row. If no findings, write:
  `| [N] | [role] | P3 | n/a | n/a | No concerns from this role's perspective. | No downstream impact identified. |`
- At least one finding per role section must challenge an assumption from the Assumption Audit.
  Reference the assumption number: "A-2 is unverified: if X holds, then Y fails."

---

## PHASE 5 — CONSENSUS ANALYSIS

**P1 count**: [N]
**P2 count**: [N]
**P3 count**: [N]

**Convergence** (same file or assumption flagged by 2+ roles):
| Surface / Assumption | Roles | Row Numbers |
|---------------------|-------|-------------|
| [file or A-N] | [roles] | [rows] |
(Write "None detected." if no convergence.)

**Conflicts** (incompatible findings on the same surface):
| Surface | Role A / Row | Role B / Row | Tension |
|---------|-------------|-------------|---------|
(Write "None detected." if no conflicts.)

**Unresolved high-suspicion assumptions** (still rated High after reviewer sections):
| Assumption | Roles That Addressed It | Status |
|------------|------------------------|--------|
| A-[N] | [roles or "none"] | Unresolved / Resolved |

---

## PHASE 6 — GO / NO-GO

**Verdict formula** — this formula is not editable, applies without exception, and cannot
be rationalized away by any finding, consensus judgment, or deadline pressure:

```
P1 count > 0  -->  No-Go
P1 count = 0  -->  Go
```

If you believe a P1 finding is not serious enough to block the merge: you have misclassified it.
Reclassify it as P2 with explicit justification, or accept the No-Go. There is no third option.

**P1 count**: [copy from Phase 5]

**Verdict**: Go / No-Go

**Basis**:
- If No-Go: "Blocked by row(s) [N, N] — [one-clause summary of the P1 finding(s) and their downstream effect]."
- If Go: "Highest open item: row [N], [role], P[N] — [finding summary and downstream impact]."

---

**Pull request diff:**

{{diff}}
```

---

## Variation Summary

| Variation | Primary Target | Axis | Key Mechanism |
|-----------|---------------|------|---------------|
| V-01 | C-12 (locator anti-pattern) | Single | Dedicated LOCATOR RULES block naming disallowed forms by example |
| V-02 | C-11 (formula lock) | Single | Dedicated formula block with "not editable" + reclassify-or-accept closure |
| V-03 | C-13 (inertia framing) | Single | Required "If this stays in" line on every finding with specificity rules |
| V-04 | C-09 (author-blind) | Single | Assumption audit (3+ assumptions) + reviewer must challenge at least one |
| V-05 | C-09 + C-11 + C-12 + C-13 | Combination | All four aspirational mechanisms layered on matrix base |

**Rubric prediction before scoring**:

- V-01: C-08 PASS (locator rules eliminate vague findings), C-12 PASS (anti-pattern named explicitly).
  Risk: C-09/C-13 not directly addressed — author-blind and inertia framing absent.
- V-02: C-07 PASS (formula applied), C-11 PASS (lock explicit + reclassify clause removes third option).
  Risk: C-12/C-13 not targeted — findings matrix may have vague locators or no downstream framing.
- V-03: C-13 PASS (required per finding with specificity rules), C-10 PASS (downstream projection surfaces cross-cutting concerns naturally).
  Risk: C-11 light ("not editable" present but no reclassify clause), C-12 absent.
- V-04: C-09 PASS (assumption audit + explicit challenge instruction), C-10 PASS (unresolved high-suspicion assumptions section).
  Risk: C-12/C-11/C-13 not targeted — locators, formula lock, and inertia framing not enforced.
- V-05: Highest composite predicted — all four aspirational mechanisms present plus matrix essential-band foundation.
  Risk: Prompt length may produce incomplete execution; "If this stays in" + assumption reference per row is a high mechanical bar.

**Weakest criterion in this round**: C-11 in V-01, V-03, V-04. The lock language is absent or soft in those three. V-02 and V-05 are the only variations with a true formula lock. If V-05 degrades on execution, a V-06 should inject the V-02 formula block verbatim into V-05 without other changes.
