# org-review Skill Body — V-01 through V-05

---

## V-01 — Axis: Role Sequence (Gate-Ordered Execution)

**Hypothesis:** Grouping roles by their natural lifecycle gate (null-hypothesis reviewers first, domain reviewers second, commitment reviewers last) prevents domain experts from anchoring to build-readiness before the problem itself is validated.

```markdown
You are running /org-review on the artifact provided below.

---

## DISPOSITION_CONTRACT

All severity labels in this review are bound to the following commit-gate semantics.
This contract is named DISPOSITION_CONTRACT and governs every reviewer section.

| Label | Commit-Gate Meaning |
|-------|---------------------|
| HIGH | This finding BLOCKS commitment to build. Commitment cannot proceed until resolved. |
| MEDIUM | This finding CONDITIONS commitment. Remediation required before proceeding. |
| LOW | This finding is ADVISORY. Commitment may proceed; remediation is recommended. |

Every reviewer section must cite this contract by name before listing findings.

---

## Step 1 — Artifact Scope

Before any reviewer runs, enumerate the artifact surface under review. List every
document, section, decision record, and prior commitment that is in scope. If a
material artifact is discovered mid-review, halt and amend this scope block before
continuing.

Scope includes:
- The primary artifact text (as provided)
- Any referenced specs, designs, or feasibility documents named in the artifact
- Prior decisions that would be invalidated by a commitment to build
- Competitive context if named in the artifact

State scope as a numbered list. Mark each item IN-SCOPE or OUT-OF-SCOPE with a
one-line rationale.

---

## Step 2 — Load Reviewer Roles

Read `.roles/`. Select reviewers relevant to this artifact type. You must
include at least one representative from each of the following archetypes:

- Product (validates problem framing and user value)
- Engineering (validates technical feasibility and implementation risk)
- Design (validates user experience and interaction model)
- Data / Research (validates evidence quality and measurement plan)
- Governance / Compliance (validates regulatory and policy exposure)
- Business / Strategy (validates market fit and competitive positioning)

List selected roles explicitly. Label each with archetype and name (or
placeholder label if no named role exists). Unlabeled or anonymous roles fail C-01.

---

## Step 3 — Gate-Ordered Review Execution

Run reviewers in three ordered gates. Do not advance to the next gate until
the current gate is complete. Gates are not parallel; they are sequential.

### Gate 1 — Null Hypothesis Challenge
**Roles:** Product, Business / Strategy, Data / Research
**Question this gate answers:** Does the problem warrant building at all?
**Inertia baseline:** The status quo (doing nothing, or continuing with what
users do today) is the named competitor at this gate.

For each role in Gate 1, produce a reviewer block using this template:

```
### [Role Name] — Gate 1: Null Hypothesis

DISPOSITION_CONTRACT: [cite by name — confirm you are bound to it]

CH-[ID]: [state the challenge claim this reviewer is raising]

Finding [N]:
  Severity: [HIGH / MEDIUM / LOW]
  Claim: [what this reviewer challenges]
  Evidence: [what evidence would resolve this challenge]
  Recommendation: [PASS / CONDITIONAL PASS / BLOCK]
```

A reviewer may produce multiple findings. Each finding gets a unique CH-ID.

### Gate 2 — Domain Assessment
**Roles:** Engineering, Design
**Question this gate answers:** Is the artifact technically and experientially sound?
**Entry condition:** Gate 1 produced no unresolved HIGH findings. If Gate 1 has
unresolved HIGHs, state that Gate 2 is BLOCKED and list which HIGHs must be
resolved first.

For each role in Gate 2, produce a reviewer block using the same template as
Gate 1, substituting `Gate 2: Domain Assessment`.

### Gate 3 — Commitment Readiness
**Roles:** All selected reviewers
**Question this gate answers:** Is the team prepared to commit to build?
**Entry condition:** Gates 1 and 2 produced no unresolved HIGH or unresolved
MEDIUM findings. If either gate has unresolved findings above LOW, state that
Gate 3 is BLOCKED and enumerate the open items.

For each role in Gate 3, produce a reviewer block using the same template,
substituting `Gate 3: Commitment Readiness`.

---

## Step 4 — Action Item Register

After all three gates, produce an action item register. Each action item must:
- Trace to the CH-ID of the finding that generated it
- Carry a disposition class: BLOCKED, CONDITIONAL, or ADVISORY
- Name the role responsible for resolution
- State the resolution criterion (what "done" looks like)

Format:

| CH-ID | Disposition | Owner Role | Resolution Criterion |
|-------|-------------|------------|----------------------|

Sort by disposition: BLOCKED first, then CONDITIONAL, then ADVISORY.

---

## Step 5 — Synthesis

In 3–5 sentences, state the overall recommendation: COMMIT, CONDITIONAL COMMIT,
or DO NOT COMMIT. Cite the highest-severity open finding that drives the
recommendation. Do not introduce new findings at synthesis.
```

---

## V-02 — Axis: Output Format (Table-First, Scan → Drill)

**Hypothesis:** Leading with a severity matrix table and following with per-reviewer prose lets a reader assess overall signal in under 30 seconds, then drill to specific findings. Reduces the cognitive cost of interpreting a large review.

```markdown
You are running /org-review on the artifact provided below.

---

## DISPOSITION_CONTRACT

Name: DISPOSITION_CONTRACT
Governs: All severity labels in this entire review document.

| Severity | Commit-Gate Meaning |
|----------|---------------------|
| HIGH | Blocks commitment. Build cannot proceed. |
| MEDIUM | Conditions commitment. Remediation required before proceeding. |
| LOW | Advisory. Commitment may proceed; remediation recommended. |

Every reviewer section must cite DISPOSITION_CONTRACT by name.

---

## Phase A — Scope Declaration

Enumerate the full artifact surface. List every document, section, and prior
decision in scope before any reviewer runs. New artifacts discovered mid-review
require a scope amendment; do not silently expand scope.

---

## Phase B — Role Selection

Read `.roles/`. Select the relevant reviewer set. You must cover all five
archetypes: Product, Engineering, Design, Research/Data, Business/Governance.
Name each selected reviewer (role label + archetype).

---

## Phase C — Summary Matrix (produce this FIRST)

Before writing any per-reviewer prose, produce the summary matrix. This is the
top-level scan view.

```
## Review Summary Matrix

| Reviewer | Archetype | Gate | CH-ID | Severity | Finding Summary | Recommendation |
|----------|-----------|------|-------|----------|-----------------|----------------|
| [name]   | [arch]    | [1/2/3] | CH-[n] | HIGH/MEDIUM/LOW | [one line] | PASS/BLOCK/CONDITIONAL |
```

Include one row per finding. If a reviewer has three findings, they occupy three
rows. Sort rows by severity (HIGH first).

---

## Phase D — Per-Reviewer Detail

After the matrix, expand each reviewer's findings in full. Use this template
for each reviewer:

```
### [Reviewer Name] ([Archetype])

DISPOSITION_CONTRACT: [cite by name]

#### Lifecycle Stage: [Null Hypothesis / Domain Assessment / Commitment Readiness]

**CH-[ID] — [Finding Title]**
- Severity: HIGH / MEDIUM / LOW
- Challenge: [what is being challenged]
- Evidence Required: [what would resolve this]
- Recommendation: PASS / BLOCK / CONDITIONAL PASS
```

Lifecycle stage sequence must be respected: Null Hypothesis reviewers run before
Domain Assessment reviewers, who run before Commitment Readiness reviewers. Do not
mix stages within a reviewer block.

---

## Phase E — Action Register

```
## Action Item Register

| CH-ID | Disposition | Owner | Resolution Criterion | Status |
|-------|-------------|-------|----------------------|--------|
```

Disposition classes: BLOCKED (must resolve before any commitment), CONDITIONAL
(must resolve before proceeding), ADVISORY (may defer).

Sort: BLOCKED → CONDITIONAL → ADVISORY.

---

## Phase F — Decision

State overall disposition: COMMIT / CONDITIONAL COMMIT / DO NOT COMMIT.
One sentence. Cite the controlling CH-ID.
```

---

## V-03 — Axis: Lifecycle Emphasis (Explicit Phase Boundaries with Entry/Exit Gates)

**Hypothesis:** Naming explicit entry conditions and exit criteria for each lifecycle phase — and requiring reviewers to confirm the phase is open before writing — prevents phase collapse and ensures null hypothesis is never quietly skipped.

```markdown
You are running /org-review on the artifact provided below.

This review proceeds through three lifecycle phases. Each phase has named entry
conditions and exit criteria. A phase cannot be entered until its entry conditions
are met. A phase cannot be exited until its exit criteria are satisfied. Reviewers
must explicitly confirm phase status before producing findings.

---

## DISPOSITION_CONTRACT

This contract governs all severity labels across all phases.
Contract name: DISPOSITION_CONTRACT.

```
HIGH   → blocks commitment; phase cannot close with open HIGHs
MEDIUM → conditions commitment; phase can close only with explicit remediation plan
LOW    → advisory; phase may close; remediation recommended but not required
```

Every reviewer block must include the line:
  `Contract: DISPOSITION_CONTRACT (bound)`

---

## Artifact Scope

Before entering Phase 1, declare the full artifact surface.

List:
1. Primary artifact (as provided)
2. All referenced documents named in the artifact
3. All prior decisions that a commitment to build would invalidate
4. Competitive context named in the artifact

Mark each IN-SCOPE or OUT-OF-SCOPE. If scope is ambiguous, mark PENDING and
resolve before Phase 1 begins.

---

## Role Set

Read `.roles/`. Select reviewers for this artifact type. Cover all
archetypes: Product, Engineering, Design, Data/Research, Governance, Business.
Name each selected reviewer explicitly.

---

## Phase 1 — Null Hypothesis Challenge

**Entry Condition:** Artifact scope is declared and closed. No PENDING scope items.

**Central Question:** Does the problem described in this artifact warrant building
a solution? Is the null hypothesis — "do nothing; the current state is acceptable"
— falsifiable given the evidence in the artifact?

**Inertia Competitor:** For Phase 1, the named baseline is the status quo. Every
finding in Phase 1 must compare the artifact's claim against the status quo, not
against an ideal.

**Reviewers for Phase 1:** Product, Business/Strategy, Data/Research

For each Phase 1 reviewer, produce:

```
### [Reviewer] — Phase 1: Null Hypothesis

Contract: DISPOSITION_CONTRACT (bound)

Scope acknowledgment: [confirm scope block above is accepted or state objection]

CH-[ID]: [challenge claim, stated as a falsifiable proposition]

Finding:
  Severity (per DISPOSITION_CONTRACT): HIGH / MEDIUM / LOW
  Challenge: [precise challenge to the null hypothesis argument]
  Evidence required to resolve: [concrete, verifiable]
  Disposition: PASS / CONDITIONAL PASS / BLOCK
```

**Exit Criteria for Phase 1:**
- All Phase 1 reviewer blocks complete
- No unacknowledged HIGH findings
- Any CONDITIONAL findings have a named remediation path

**Phase 1 Gate Decision:** [OPEN / BLOCKED — list open HIGHs if BLOCKED]

---

## Phase 2 — Domain Assessment

**Entry Condition:** Phase 1 Gate Decision = OPEN.
If Phase 1 is BLOCKED, do not produce Phase 2 output. State: "Phase 2 is
BLOCKED pending resolution of: [list CH-IDs]."

**Central Question:** Is the artifact technically and experientially sound?
Does the solution design address the validated problem correctly?

**Reviewers for Phase 2:** Engineering, Design

For each Phase 2 reviewer, produce:

```
### [Reviewer] — Phase 2: Domain Assessment

Contract: DISPOSITION_CONTRACT (bound)

Phase 1 Gate: [confirm OPEN — required to proceed]

CH-[ID]: [challenge claim]

Finding:
  Severity (per DISPOSITION_CONTRACT): HIGH / MEDIUM / LOW
  Challenge: [precise domain challenge]
  Evidence required: [concrete]
  Disposition: PASS / CONDITIONAL PASS / BLOCK
```

**Exit Criteria for Phase 2:**
- All Phase 2 reviewer blocks complete
- No unacknowledged HIGH findings
- MEDIUM findings have named remediation plans

**Phase 2 Gate Decision:** [OPEN / BLOCKED]

---

## Phase 3 — Commitment Readiness

**Entry Condition:** Phase 1 Gate = OPEN AND Phase 2 Gate = OPEN.
If either gate is BLOCKED, state: "Phase 3 is BLOCKED pending: [list CH-IDs]."

**Central Question:** Is the team prepared to commit to build this?
Are resources, dependencies, risks, and acceptance criteria clear?

**Reviewers for Phase 3:** All selected reviewers

For each Phase 3 reviewer, produce:

```
### [Reviewer] — Phase 3: Commitment Readiness

Contract: DISPOSITION_CONTRACT (bound)

Phase 2 Gate: [confirm OPEN — required to proceed]

CH-[ID]: [challenge claim]

Finding:
  Severity (per DISPOSITION_CONTRACT): HIGH / MEDIUM / LOW
  Challenge: [commitment-readiness challenge]
  Disposition: PASS / CONDITIONAL PASS / BLOCK
```

**Exit Criteria for Phase 3:**
- All reviewer blocks complete
- No unresolved HIGHs or MEDIUMs

**Phase 3 Gate Decision:** [OPEN / BLOCKED]

---

## Action Register

Collect all CH-IDs across all phases:

| CH-ID | Phase | Disposition | Owner | Resolution Criterion |
|-------|-------|-------------|-------|----------------------|

Disposition: BLOCKED (gate-blocking), CONDITIONAL (remediation required),
ADVISORY (may defer). Sort BLOCKED first.

---

## Final Decision

Based on Phase 3 Gate Decision:
- OPEN with no CONDITIONAL → **COMMIT**
- OPEN with open CONDITIONALs → **CONDITIONAL COMMIT** (list conditions)
- BLOCKED → **DO NOT COMMIT** (cite controlling CH-ID)
```

---

## V-04 — Axes: Role Sequence + Output Format (Alphabetical Order + Numbered Finding Lists)

**Hypothesis:** Alphabetical role ordering removes implied priority hierarchy among reviewers; numbered finding lists make per-finding traceability mechanical and remove the possibility of ambiguous CH-ID references.

```markdown
You are running /org-review on the artifact provided below.

---

## DISPOSITION_CONTRACT

Name: DISPOSITION_CONTRACT
Scope: All severity labels in this document — no exceptions.

Severity definitions:
  1. HIGH — commitment BLOCKED until resolved
  2. MEDIUM — commitment CONDITIONAL on remediation
  3. LOW — commitment may proceed; remediation advisory

Reviewers cite this contract as: `[DISPOSITION_CONTRACT: bound]`

---

## 1. Scope Block

List the full artifact surface. Include every document, section, prior decision,
and competitive reference in scope. Number each item. Mark IN-SCOPE / OUT-OF-SCOPE
/ PENDING. Resolve all PENDING before proceeding.

```
Scope Item 1: [name] — [IN-SCOPE / OUT-OF-SCOPE]
Scope Item 2: ...
```

---

## 2. Role Selection

Read `.roles/`. Select the relevant reviewer set. Required archetypes:
Business/Strategy, Data/Research, Design, Engineering, Governance/Compliance,
Product.

List selected reviewers in alphabetical order by role label. Alphabetical
ordering is intentional — it removes implied priority. All roles are equally
empowered to produce HIGH findings at any lifecycle stage.

```
Selected Roles (alphabetical):
- [Role A] ([Archetype])
- [Role B] ([Archetype])
...
```

---

## 3. Review Execution

Run all reviewers. Each reviewer covers all three lifecycle questions in their
own section:

  Q1 (Null Hypothesis): Does the problem warrant building?
  Q2 (Domain): Is the artifact sound?
  Q3 (Commitment): Is the team ready?

Lifecycle questions are sequential within each reviewer block. A reviewer does
not skip Q1 to jump to Q3.

For each reviewer, produce the following block. Reviewers appear in the same
alphabetical order established in Section 2.

```
### [Role Label] ([Archetype])

[DISPOSITION_CONTRACT: bound]

**Q1 — Null Hypothesis**

Finding 1.1 (CH-[ID]):
  Severity: HIGH / MEDIUM / LOW
  Challenge: [what is being challenged]
  Resolution: [what resolves this finding]
  Disposition: PASS / CONDITIONAL PASS / BLOCK

Finding 1.2 (CH-[ID]):  ← add only if this reviewer has additional Q1 findings
  ...

**Q2 — Domain Assessment**
[Entry: proceed only if no unresolved HIGHs from Q1 across all roles;
 state BLOCKED if entry condition fails]

Finding 2.1 (CH-[ID]):
  Severity: HIGH / MEDIUM / LOW
  Challenge: [domain-specific challenge]
  Resolution: [what resolves this]
  Disposition: PASS / CONDITIONAL PASS / BLOCK

**Q3 — Commitment Readiness**
[Entry: proceed only if no unresolved HIGHs or MEDIUMs from Q1/Q2;
 state BLOCKED if entry condition fails]

Finding 3.1 (CH-[ID]):
  Severity: HIGH / MEDIUM / LOW
  Challenge: [commitment challenge]
  Resolution: [what resolves this]
  Disposition: PASS / CONDITIONAL PASS / BLOCK
```

---

## 4. Finding Index

After all reviewer blocks, produce a numbered index of all findings across all
roles. CH-IDs must be unique document-wide.

```
Finding Index:

CH-01: [Role] — Q[n] — [one-line title] — Severity: [H/M/L]
CH-02: ...
```

Sort: HIGH first, then MEDIUM, then LOW. Within severity, alphabetical by role.

---

## 5. Action Register

For every CH-ID with a disposition of BLOCK or CONDITIONAL PASS, produce an
action item.

```
Action Register:

| CH-ID | Disposition Class | Owner Role | Resolution Criterion |
|-------|-------------------|------------|----------------------|
```

Disposition Class:
- BLOCKED — must resolve before any commitment decision
- CONDITIONAL — must resolve before proceeding to build
- ADVISORY — may defer; note if LOW finding warrants tracking

---

## 6. Decision

Overall recommendation in one sentence. Cite the controlling CH-ID(s).
Options: COMMIT / CONDITIONAL COMMIT (list conditions) / DO NOT COMMIT.
```

---

## V-05 — Axes: Lifecycle Emphasis + Inertia Framing (Status-Quo as Named Baseline)

**Hypothesis:** Making the status-quo competitor a named, persistent presence throughout the review — not just a framing device in the introduction — forces every reviewer to benchmark their findings against "does this beat doing nothing?" rather than against an ideal or a peer competitor. This raises the bar at the null-hypothesis gate and prevents domain reviewers from assuming the problem is already settled.

```markdown
You are running /org-review on the artifact provided below.

---

## DISPOSITION_CONTRACT

This contract is named DISPOSITION_CONTRACT. All severity labels in this review
are governed by it. Every reviewer section must include the line:
  `DISPOSITION_CONTRACT: [bound]`

Severity commit-gate semantics:

  HIGH    — This finding BLOCKS commitment to build. The team cannot proceed
            until this finding is resolved. A HIGH finding at any gate prevents
            advancement to the next gate.

  MEDIUM  — This finding CONDITIONS commitment. The team must produce and accept
            a remediation plan before proceeding. A gate with open MEDIUMs may
            not close without a documented remediation path.

  LOW     — This finding is ADVISORY. Commitment may proceed. Remediation is
            recommended but not required to advance.

Severity is independent of reviewer role. Any role may raise a HIGH.

---

## Inertia Competitor Declaration

Before any reviewer runs, name the inertia competitor explicitly. This is the
artifact's primary competitive baseline throughout the entire review — not a
market competitor, but the current state of affairs if no action is taken.

```
Inertia Competitor: [describe the status quo — what users do today, what
exists today, what would continue if this artifact never became a product]
```

Every Phase 1 reviewer MUST compare their findings against this named
inertia competitor, not against an ideal state or a hypothetical alternative.
Phase 2 and Phase 3 reviewers may reference the inertia competitor when
relevant to their domain finding.

---

## Artifact Scope

Enumerate the full surface under review:

1. [Primary artifact]
2. [Referenced specs or designs]
3. [Prior decisions a commitment would invalidate]
4. [Competitive context named in the artifact — distinguished from the
   inertia competitor above, which is implicit in all features]

Mark IN-SCOPE or OUT-OF-SCOPE. Scope is closed before Phase 1 begins.

---

## Role Set

Read `.roles/`. Select reviewers. Required archetypes: Product,
Engineering, Design, Data/Research, Business/Strategy, Governance.
Name each reviewer explicitly.

---

## Phase 1 — Null Hypothesis Challenge

**Lifecycle question:** Does the problem described in this artifact justify
displacing the inertia competitor?

**Inertia framing:** At this phase, the inertia competitor named above is
the only competitor that matters. A finding that the artifact beats a
market competitor but does not beat the inertia competitor is a HIGH finding.

**Reviewers:** Product, Business/Strategy, Data/Research

For each Phase 1 reviewer:

```
### [Reviewer] — Phase 1: Null Hypothesis

DISPOSITION_CONTRACT: [bound]

Inertia competitor: [restate from declaration above — must appear per reviewer]

CH-[ID] — [Challenge Title]

  Severity: HIGH / MEDIUM / LOW
  Challenge: [What specific claim in the artifact does this challenge?
              How does this challenge relate to the inertia competitor?]
  Evidence required: [What concrete evidence would falsify this challenge?]
  Recommendation: PASS / CONDITIONAL PASS / BLOCK
```

**Phase 1 Gate:** After all Phase 1 reviewers run, list all CH-IDs and their
severity. State gate status:
- OPEN: no unresolved HIGHs
- BLOCKED: [list CH-IDs with HIGH that remain unresolved]

If BLOCKED, Phase 2 does not run. Output: "Phase 2 BLOCKED pending [CH-IDs]."

---

## Phase 2 — Domain Assessment

**Entry condition:** Phase 1 Gate = OPEN.

**Lifecycle question:** Is the artifact technically and experientially sound?
Does it do what it claims, and do so well?

**Inertia framing:** Phase 2 reviewers may invoke the inertia competitor if
they find that the artifact's technical or experience approach produces
equivalent outcomes to the status quo (a disguised null finding).

**Reviewers:** Engineering, Design

For each Phase 2 reviewer:

```
### [Reviewer] — Phase 2: Domain Assessment

DISPOSITION_CONTRACT: [bound]

Phase 1 Gate: OPEN [required — do not proceed if blocked]

CH-[ID] — [Challenge Title]

  Severity: HIGH / MEDIUM / LOW
  Challenge: [Domain-specific challenge]
  Inertia note (if applicable): [Does this finding suggest the approach
    merely replicates the status quo without improvement?]
  Evidence required: [What resolves this?]
  Recommendation: PASS / CONDITIONAL PASS / BLOCK
```

**Phase 2 Gate:** List all Phase 2 CH-IDs and severity. State OPEN or BLOCKED.

---

## Phase 3 — Commitment Readiness

**Entry condition:** Phase 1 Gate = OPEN AND Phase 2 Gate = OPEN.

**Lifecycle question:** Is the team prepared to commit resources, accept
risks, and begin build?

**Inertia framing:** At Phase 3, the inertia competitor appears as
opportunity cost. A MEDIUM or HIGH finding here may mean the team is not
yet positioned to beat the status quo even if the artifact is sound.

**Reviewers:** All selected reviewers

For each Phase 3 reviewer:

```
### [Reviewer] — Phase 3: Commitment Readiness

DISPOSITION_CONTRACT: [bound]

Phase 2 Gate: OPEN [required — do not proceed if blocked]

CH-[ID] — [Challenge Title]

  Severity: HIGH / MEDIUM / LOW
  Challenge: [Commitment readiness challenge]
  Inertia cost (if applicable): [Does unresolved risk here mean the
    inertia competitor wins by default?]
  Recommendation: PASS / CONDITIONAL PASS / BLOCK
```

**Phase 3 Gate:** State OPEN or BLOCKED.

---

## Action Register

All CH-IDs with BLOCK or CONDITIONAL PASS disposition:

| CH-ID | Phase | Severity | Disposition Class | Owner | Resolution Criterion |
|-------|-------|----------|-------------------|-------|----------------------|

Disposition Class:
- BLOCKED — gate-blocking; must resolve before commitment
- CONDITIONAL — must resolve before proceeding to build
- ADVISORY — may defer

Sort: BLOCKED → CONDITIONAL → ADVISORY. Within each class, Phase 1 first.

---

## Final Decision

Based on Phase 3 Gate status:
- All gates OPEN, no CONDITIONALs: **COMMIT**
- All gates OPEN, open CONDITIONALs: **CONDITIONAL COMMIT** (list CH-IDs)
- Any gate BLOCKED: **DO NOT COMMIT** (cite controlling CH-ID)

State whether the inertia competitor is currently winning. One sentence.
```

---

## Variation Summary

| Variation | Primary Axis | Secondary Axis | Key Structural Bet |
|-----------|-------------|----------------|-------------------|
| V-01 | Role Sequence | — | Gate-ordered execution; roles grouped by lifecycle gate |
| V-02 | Output Format | — | Summary matrix first, prose detail second; scan → drill |
| V-03 | Lifecycle Emphasis | — | Explicit entry/exit conditions; gate decision blocks next phase |
| V-04 | Role Sequence | Output Format | Alphabetical roles; numbered CH-ID finding lists |
| V-05 | Lifecycle Emphasis | Inertia Framing | Inertia competitor named and carried through all three phases |
