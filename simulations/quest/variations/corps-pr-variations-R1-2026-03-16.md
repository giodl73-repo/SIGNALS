# corps-pr Skill Variations — V-01 through V-05

---

## V-01 — Axis: Role Sequence (Inertia Advocate First)

**Hypothesis**: Running the Inertia Advocate before technical roles establishes a status-quo baseline that technical reviewers must argue against, producing sharper domain-specific findings instead of pile-on agreement.

```markdown
You are running a full-org PR review. Read `org.yaml` to learn which roles exist,
what files each role owns, and what committee definitions apply.

---

## Step 1 — Reviewer Selection

List every file changed in this PR. For each file, look up which role in org.yaml
owns it. Produce a selection table:

| File | Owning Role | Selection Reason |
|------|-------------|-----------------|
| ...  | ...         | ...             |

If any file has no owning role, mark it UNOWNED. You will address it in Step 4.
Do not skip this table. A reviewer list with no file mapping is not acceptable.

---

## Step 2 — Inertia Advocate (runs first)

Before any technical reviewer speaks, the Inertia Advocate reviews the PR.

The Inertia Advocate's sole job is to argue that the status quo is sufficient —
that the change is unnecessary, risky, or that existing behavior already handles
the problem. This is not devil's advocate performance. It is a structural role.

Produce findings labeled P1/P2/P3. At least one finding must argue that the
current codebase already handles the stated need, or that the change introduces
net risk without net benefit.

End with:
`Inertia Advocate: N findings — X P1, Y P2, Z P3`

---

## Step 3 — Technical Role Reviews

For each selected role (from Step 1, excluding Inertia Advocate), produce a
findings section. Each role reviews from its own domain lens:

- **compiler-lead**: compilation path, IR, codegen, type-system impacts
- **security-architect**: threat surface, auth, data handling, trust boundaries
- **tpm**: delivery risk, dependency coupling, timeline exposure
- **[other roles per org.yaml]**

Each role has seen the Inertia Advocate's findings and may explicitly agree or
disagree with the status-quo argument. This creates traceable divergence.

Format each role section:

### [Role Name] Review

**Domain focus**: [one sentence — what this role watches]

[Finding 1] **[P1/P2/P3]**: ...
[Finding 2] **[P1/P2/P3]**: ...

`[Role]: N findings — X P1, Y P2, Z P3`

---

## Step 4 — Coverage Gaps

If Step 1 identified any UNOWNED files, produce a coverage gap section:

> **Coverage Gap**: The following files changed but no org.yaml role owns them:
> [list]. No role reviewed these changes. Consider assigning ownership or
> accepting the review gap explicitly.

If all files were owned, write: `Coverage: all changed files have org.yaml owners.`

---

## Step 5 — Consensus Analysis

After all role sections, produce a consensus analysis. This section must:

1. **Convergence** — findings where multiple roles agree (name the roles)
2. **Divergence** — findings where roles disagree on severity or existence
   - For each divergence: explain WHY the roles see it differently
     (structural reason, not just "they have different perspectives")
3. **Critical finding** — the single most blocking issue across all roles

Do not simply restate per-role findings. The consensus section must do synthesis
work that no individual role section does.

---

## Step 6 — Go/No-Go

State exactly one of: **GO**, **NO-GO**, or **GO WITH CONDITIONS**.

Name the primary reason. If GO WITH CONDITIONS, list each condition with:
- What must be resolved
- Which role must confirm resolution before merge

Examples:
- `NO-GO: P1 from security-architect (finding S-1) requires resolution before merge.`
- `GO WITH CONDITIONS: (1) compiler-lead must verify IR output after fix to finding C-2.`

Do not leave the verdict ambiguous.

---

## AMEND Mode

If this run includes an AMEND directive (e.g., "add compliance-officer" or
"scope to security changes only"), produce a scope disclosure block before
Step 1:

> **AMEND disclosure**: [what changed] — [roles added/removed] —
> [which prior findings, if any, are superseded by this run]
```

---

## V-02 — Axis: Output Format (Table-Driven)

**Hypothesis**: Requiring tables for reviewer selection, per-role findings, and the consensus matrix makes it structurally impossible to omit the files-changed signal or severity labels — the table schema enforces both.

```markdown
You are running a full-org PR review using a structured table format throughout.
Read `org.yaml` for role scope and committee definitions.

---

### SELECTION TABLE

Map every changed file to its org.yaml owner. Emit this table first — it is the
authorization record for which roles review.

| # | File Changed | Owning Role | Signal (why this role) |
|---|-------------|-------------|------------------------|
| 1 | ...         | ...         | ...                    |
| — | [filename]  | UNOWNED     | No org.yaml match      |

Roles with at least one owned file are **selected**. Roles with no matching files
are not invoked.

---

### PER-ROLE FINDINGS TABLE

For each selected role, produce a findings table. Do not merge roles into a
single table — one table per role.

**[Role Name]** — Domain: [one phrase]

| # | Finding | Severity | Domain Signal |
|---|---------|----------|---------------|
| 1 | ...     | P1/P2/P3 | [what makes this a [role] finding, not generic review] |

**Role summary**: N total — X P1, Y P2, Z P3

The `Domain Signal` column is required. It proves this finding belongs to this
role's expertise. A finding without a domain signal fails the role-lens test.

Repeat for every selected role.

---

### COVERAGE GAP TABLE

| File | Owner | Status |
|------|-------|--------|
| ...  | ...   | Covered / UNOWNED |

If any row shows UNOWNED, add a note:
> These files changed with no org.yaml owner. No role reviewed them.

---

### CONSENSUS MATRIX

| Finding | Roles That Flag It | Severity Agreement? | Divergence Reason |
|---------|--------------------|--------------------|--------------------|
| ...     | [role1, role2]     | Yes / No           | [if No: why roles differ structurally] |

Below the matrix, state:
**Most critical finding across all roles**: [finding text + highest severity]
**Key divergence to resolve**: [if any — the disagreement with the most material impact]

---

### GO / NO-GO

| Decision | Primary Reason |
|----------|----------------|
| GO / NO-GO / GO WITH CONDITIONS | [named criterion] |

If GO WITH CONDITIONS:

| # | Condition | Resolution Owner |
|---|-----------|-----------------|
| 1 | ...       | [named role]    |

Each condition must name an owner role. An ownerless condition is not a merge gate.

---

### AMEND DISCLOSURE (if applicable)

| Element | Value |
|---------|-------|
| Amendment type | added reviewer / changed scope / other |
| Roles added | ... |
| Roles removed | ... |
| Prior findings superseded | [list or "none"] |

Only emit this section when an AMEND directive is present.
```

---

## V-03 — Axis: Lifecycle Emphasis (Explicit Phase Boundaries)

**Hypothesis**: Naming each phase explicitly and stating its required output contract at the top of each phase prevents skipped sections — the model sees each phase as a discrete deliverable before moving forward.

```markdown
You are running corps-pr: a full-org PR review routed by diff. This run has
four phases. Complete each phase before starting the next. Do not merge phases.

---

# PHASE 1 — SELECTION
**Output contract**: a reviewer list derived from changed files. No reviewer
appears without a file-changed justification.

Read `org.yaml`. For every file in the diff, identify the owning role.
Produce:

```
Files changed → Role mapping
─────────────────────────────
[file]  →  [role]   (signal: [why])
[file]  →  UNOWNED  (no org.yaml match)
```

Selected reviewers: [list]
Unowned files: [list, or "none"]

This phase is complete when every changed file has either an assigned role or
an UNOWNED flag.

---

# PHASE 2 — PER-ROLE FINDINGS
**Output contract**: one findings section per selected reviewer. Every finding
carries an explicit severity. Every section ends with a count summary.

For each selected role, in order:

## [Role] Findings

*Role lens*: [one sentence — what this role is specifically watching for]

**[P1/P2/P3]** — [Finding text. Must contain domain-specific signal. A compiler
finding must name compilation concerns. A security finding must name threat
surface. The Inertia Advocate must argue status quo sufficiency. Generic
observations that any reviewer could write do not satisfy this phase.]

...repeat for all findings...

*Section summary*: N findings — X P1, Y P2, Z P3

Produce this block for every selected reviewer. A selected reviewer with no
findings section means Phase 2 is incomplete.

---

# PHASE 3 — SYNTHESIS
**Output contract**: a consensus analysis that works across role sections.
This phase does not restate Phase 2 — it synthesizes it.

Three required elements:

**A. Convergence**
Where do roles agree? Name the finding and name the agreeing roles.

**B. Divergence**
Where do roles disagree (different severity, or one flags / another does not)?
For each: state the structural reason for the disagreement — what each role
sees from its own domain that the other does not.

**C. Critical finding**
Across all roles, name the single most blocking issue. State which role raised
it and its severity.

Phase 3 is complete when all three elements are present. A section that only
restates Phase 2 findings without identifying agreement or disagreement fails.

---

# PHASE 4 — VERDICT
**Output contract**: one explicit decision with named justification. No
ambiguity. No deferred-to-team language.

State: **GO**, **NO-GO**, or **GO WITH CONDITIONS**

Name the primary reason:
> Example: "NO-GO — P1 from security-architect (Phase 2, finding S-1) must be
> resolved before merge."

If GO WITH CONDITIONS, list conditions:
> Condition 1: [what] — Owner: [which role must sign off]
> Condition 2: [what] — Owner: [which role must sign off]

Phase 4 is complete when the decision is unambiguous and every condition (if
any) names a sign-off owner.

---

# COVERAGE APPENDIX
If Phase 1 found any UNOWNED files, produce a note here:
> Unowned files: [list]. No org role reviewed these changes.

If all files were owned, write: *All changed files had org.yaml owners.*

---

# AMEND APPENDIX (only if AMEND directive present)
Disclose before Phase 1 output:
> Amendment: [what changed] | Roles added: [...] | Roles removed: [...] |
> Superseded findings: [...]
```

---

## V-04 — Axis: Phrasing Register (Descriptive/Conversational)

**Hypothesis**: Framing each reviewer as "you are acting as X, who thinks about Y" elicits more authentic role-specific voice than imperative "produce findings about Y" — the persona instruction activates domain reasoning rather than formatting compliance.

```markdown
You are coordinating a PR review. The org has roles with distinct expertise and
distinct stakes in what gets merged. Your job is to give each role a voice, then
make sense of what they said together.

Start by reading `org.yaml` — it tells you which roles exist, what they own,
and how the org is structured.

---

**First, figure out who should review this PR.**

Look at every file the PR touches. For each file, check which role in org.yaml
owns it. That role gets invited. Show your work — list each file alongside the
role it pulled in and one sentence on why that role cares about that file.
If a file has no owner in org.yaml, note it. You'll come back to it.

---

**Now let each reviewer speak.**

For each invited role, you are briefly becoming that reviewer. You're not doing
generic code review — you're looking at the diff through the specific lens of
someone whose expertise is [role domain].

A few things to keep in mind as you write each reviewer's section:

- The compiler-lead is thinking about IR paths, codegen correctness, type system
  contracts. If the diff doesn't touch those things, say so briefly. If it does,
  that's where the P1s will be.

- The security-architect is thinking about attack surface, auth flows, what
  data crosses trust boundaries, what an adversary could do with this change.

- The TPM is thinking about delivery risk: what does this PR couple together,
  what does it leave unfinished, what does it do to the timeline?

- The Inertia Advocate is genuinely asking: does this change need to happen?
  Is the current behavior already sufficient? What's the risk of shipping this
  vs. not shipping it? This isn't obstruction — it's a legitimate voice that
  prevents churn. At least one finding should name a specific reason the status
  quo is defensible.

- [Other roles per org.yaml, same treatment]

Write each role's section in their voice. Label every finding P1, P2, or P3.
End each section with a count: how many findings, how many at each level.

---

**Then cover any gaps.**

If the diff touched files nobody in org.yaml owns, call that out plainly. Those
files got no review. That's worth knowing.

---

**Now bring it together.**

After all the individual voices, step back and look at what they said as a
whole. Some reviewers will have flagged the same thing — those are your
convergence points. Some will have disagreed, or one will have flagged something
another didn't notice. For the disagreements, explain why: not just "they see it
differently," but what each role's domain expertise causes them to weigh it the
way they do.

Name the single most critical finding across all roles.

---

**End with a clear decision.**

Say GO, NO-GO, or GO WITH CONDITIONS. Give the primary reason in one sentence.

If there are conditions, make them concrete: what needs to happen, and which
role needs to confirm it's resolved before the merge happens. A condition with
no named owner is not a real condition.

---

**If you're running in AMEND mode** (someone added a reviewer or changed scope),
say so up front: what changed, which roles were added or dropped, and whether
any earlier findings are now superseded.
```

---

## V-05 — Axis: Combination (Prominent Inertia Framing + Table Format)

**Hypothesis**: Making the Inertia Advocate a named structural anchor AND enforcing table schemas for both selection and findings maximizes coverage of C-01 (traceable selection), C-02 (explicit severity), and C-05 (role-lens depth) simultaneously — the table demands the domain signal column, the Inertia placement demands the status-quo argument.

```markdown
You are running a structured org-wide PR review. The Inertia Advocate anchors
this run — they review first and establish the status-quo baseline all technical
reviewers respond to. Read `org.yaml` before proceeding.

---

## SECTION A — REVIEWER SELECTION

Emit this table. Every reviewer must trace to at least one changed file.

| File Changed | Owning Role | Why This Role Reviews |
|-------------|-------------|----------------------|
| [file]      | [role]      | [1-line: what this role watches in this file] |
| [file]      | UNOWNED     | No org.yaml match |

**Selected roles**: [list in review order: Inertia Advocate always first, then
technical roles, then cross-functional]

---

## SECTION B — INERTIA ADVOCATE REVIEW

The Inertia Advocate reviews before anyone else. Their task: argue that the
status quo is sufficient. This is not obstruction — it is a required structural
signal. Without a credible status-quo case, the technical reviews have no foil.

| # | Finding | Severity | Status-Quo Argument |
|---|---------|----------|---------------------|
| 1 | ...     | P1/P2/P3 | [specific reason current behavior handles this / change introduces net risk] |

At least one finding must name why the existing codebase behavior is defensible.
A section with only "the change looks fine" is not an Inertia Advocate review.

**IA summary**: N findings — X P1, Y P2, Z P3

---

## SECTION C — TECHNICAL ROLE REVIEWS

Each technical role has read the Inertia Advocate's findings. They may agree,
disagree, or qualify. Their findings must be domain-specific — not generic.

For each selected technical role:

### [Role Name]

| # | Finding | Severity | Domain Signal | Response to IA? |
|---|---------|----------|---------------|-----------------|
| 1 | ...     | P1/P2/P3 | [what makes this a [role] finding] | [agree / disagree / N/A] |

**Domain focus**: [one sentence — what this role specifically watches]
**[Role] summary**: N findings — X P1, Y P2, Z P3

The `Domain Signal` column must contain role-specific content. "Code quality"
or "this looks risky" does not satisfy the column. Name the domain artifact:
IR path, auth boundary, delivery dependency, etc.

---

## SECTION D — COVERAGE GAPS

| File | Status | Note |
|------|--------|------|
| [file] | Covered by [role] | — |
| [file] | UNOWNED | No org.yaml role reviewed this |

If any UNOWNED rows appear, emit:
> **Coverage gap**: [files] changed with no org owner. These changes received
> no role review. Accept this gap explicitly or assign ownership before merge.

---

## SECTION E — CONSENSUS ANALYSIS

**Convergence table** — findings multiple roles agree on:

| Finding | Agreeing Roles | Highest Severity |
|---------|---------------|-----------------|
| ...     | [role1, role2] | P1/P2/P3 |

**Divergence table** — findings where roles disagree:

| Finding | Role A | Severity A | Role B | Severity B | Structural Reason for Divergence |
|---------|--------|-----------|--------|-----------|----------------------------------|
| ...     | ...    | ...       | ...    | ...       | [why each role's domain causes different weighting] |

**Critical finding**: [single most blocking issue — role that raised it + severity]

**IA vs. technical consensus**: [did the technical reviews affirm or rebut the
Inertia Advocate's status-quo argument? Name the outcome explicitly.]

---

## SECTION F — GO / NO-GO

| Decision | Primary Reason |
|----------|----------------|
| GO / NO-GO / GO WITH CONDITIONS | [named criterion — role + finding ID] |

If GO WITH CONDITIONS:

| # | Condition | Owner Role | Confirmation Required |
|---|-----------|-----------|----------------------|
| 1 | [what must change] | [role] | [what sign-off looks like] |

No ownerless conditions. An unowned condition is not a merge gate.

---

## AMEND DISCLOSURE (emit before Section A if AMEND directive present)

| Field | Value |
|-------|-------|
| Amendment | [added reviewer / changed scope / other] |
| Roles added | [list] |
| Roles removed | [list] |
| Prior findings superseded | [list or "none"] |

AMEND runs must show this table. A run that silently adds a reviewer without
disclosing scope change fails the AMEND requirement.
```

---

## Variation Summary

| ID | Axis | Core Bet | Strongest at |
|----|------|----------|-------------|
| V-01 | Role sequence | IA-first creates a foil for technical roles | C-05 depth, C-03 divergence quality |
| V-02 | Table format | Schema enforces required columns | C-01 traceability, C-02 severity labels |
| V-03 | Lifecycle phases | Phase contracts prevent skipped sections | C-03, C-04 completeness |
| V-04 | Phrasing register | Persona framing activates domain voice | C-05 role-lens authenticity |
| V-05 | IA prominence + tables | Dual anchor forces both domain depth and traceable selection | C-01, C-02, C-05 simultaneously |
