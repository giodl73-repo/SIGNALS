---
skill: quest-variate
skill_target: corps-pr
round: 4
date: 2026-03-16
rubric_version: 4
---

# Variate R4 — corps-pr

5 complete prompt body variations for the `corps-pr` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Axes Selected

| Axis | Used In | R4 Focus |
|------|---------|----------|
| Role sequence (domain-lens gate as two-step inline procedure per-finding) | V-01, V-04 | C-15: binary test + rewrite consequence structurally enforced |
| Output format (named-field template slots for all blocks including AMEND) | V-02, V-05 | C-16: AMEND block as schema, not prose |
| Phrasing register (imperative with ban-to-fix substitution pairs) | V-03, V-05 | C-13: banned phrases paired with required replacements |
| Lifecycle emphasis (phase gates with explicit entry/exit conditions) | V-04 | C-15: phase-level domain-lens audit before synthesis |
| Inertia framing (IA as status-quo budget authority) | V-04 | C-11/C-14: IA as cost benchmark all technical roles must argue against |

**What changed from R3:**
- R3 V-01 had a mandatory IA-anchor slot but no two-step domain-lens gate (C-15 gap).
- R3 V-02 had a `domain-lens` column but enforced specificity (file+line), not the binary
  validity test + rewrite consequence (C-15 gap).
- R3 V-03 had AMEND with prose instructions ("state what role was added...") but no
  named-field template block (C-16 gap).
- R3 V-04/V-05 had ban lists but no paired required-replacement forms (C-13 depth gap).

R4 addresses all four gaps across the five variations.

---

## V-01 — Role Sequence: Two-Step Domain-Lens Gate per Finding

**Axis**: Role sequence
**Hypothesis**: Embedding the domain-lens validity check as a named two-step gate
(Step A: binary test; Step B: rewrite consequence) directly in the per-role section
header — before any findings are written — makes C-15 a production constraint, not a
post-hoc instruction. The gate is not a column or a note; it is a sequential procedure
the model must execute per-finding. A finding that fails Step A without going through
Step B is structurally incomplete, not just stylistically weak.

---

You are running `/corps-pr`. Route this PR through the org and produce a structured
pre-merge review. Read all inputs before any output begins.

**INPUTS**

- `org.yaml` — role scope patterns and committee definitions
- PR diff — every changed file and the nature of each change
- `.roles/` — domain lens and orientation for each role

---

**STEP 1 — ROUTING TABLE**

Map every changed file to an org.yaml role. Output the routing table before any review
begins. Do not begin reviews until the table is complete.

```
## Reviewer Selection

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern from org.yaml that matched] |
| (all files) | default | Inertia Advocate | default — always included |
```

Rules:
- Every changed file appears in at least one row. No file is silently dropped.
- Role selection must cite the org.yaml scope pattern — not inferred from filename or
  project structure.
- Coverage gap: if any file has no org.yaml match, write immediately after the table:
  `COVERAGE GAP: [file] — no org.yaml scope pattern covers this path.`

---

**STEP 2 — INERTIA ADVOCATE (always first)**

The IA section appears before all technical role sections. This is structural and
non-configurable. Technical roles read the IA section before writing their own findings.

The IA's mandate: make the strongest possible case that this PR should not merge — not
because the code is defective, but because the current codebase may already handle the
problem adequately.

```
## Review: Inertia Advocate

Null hypothesis: The codebase currently [does X via mechanism Y]. This PR is justified
only if [condition].
Null hypothesis strength: HIGH / MEDIUM / LOW
  HIGH   — the status-quo case is credible and the PR does not defeat it
  MEDIUM — the PR names a real problem but does not justify the switching cost
  LOW    — the PR directly defeats the status-quo argument

Findings:
F-01 [P1/P2/P3] [argument that the status quo is sufficient — names an existing mechanism,
     path, or function, not a category]
     Owner: [role] | Resolution: [what must change for this finding to close]
F-02 [P1/P2/P3] [second argument]
     Owner: [role] | Resolution: [concrete action]
[minimum 2 findings]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence]
```

---

**STEP 3 — TECHNICAL ROLE REVIEWS**

Run each role from the routing table. Sequence: security and compliance roles first →
domain-specific technical roles second → PM/TPM roles last.

**For each finding in every technical role section, execute the domain-lens gate
before writing the finding:**

```
DOMAIN-LENS GATE (execute per finding, in order):

Step A — Binary test:
  Ask: "Would only [this role] raise this finding, given their domain?"
  If YES → the finding carries the role's domain signal. Proceed to write it.
  If NO  → any generic reviewer could write this sentence. Do not write it. Go to Step B.

Step B — Rewrite consequence:
  Revise the finding to name a specific mechanism, function, path, or contract that
  belongs to this role's domain and could not be raised by a reviewer without that
  domain. Then re-execute Step A.
  A finding that still answers NO after revision must be dropped.
```

The gate distinguishes role-domain fidelity from specificity. A finding that names
`auth/middleware.ts:88` satisfies a specificity contract but still fails Step A if any
reviewer could have written it. The rewrite must add the role-specific mechanism, not
just the location.

Use this section template:

```
## Review: [Role Name]

Source files: [files from routing table that triggered this role]
Orientation: [one phrase from .roles/ — what this role is trained to catch]

IA anchor:
  IA verdict: [BLOCK / CONDITION / PASS]
  Relevant IA finding: [brief summary of the IA finding most bearing on this role's scope]
  This role [confirms / extends / disputes] that assessment because: [names the
  code surface, function, or architectural mechanism — not the role's perspective or focus]
  Example: "IA found the existing auth guard sufficient at the API boundary.
  Compiler-lead disputes this: the new codegen emission path at compiler/emit.ts:214
  bypasses the guard entirely — a regression surface the IA section did not reach because
  it does not own compilation outputs."

Findings: [each finding below passed Steps A and B of the domain-lens gate]
F-01 [P1/P2/P3] [domain-specific finding — names the mechanism within this role's domain]
     Owner: [role] | Resolution: [concrete action naming what to do and where]
F-02 [P1/P2/P3] [second finding]
     Owner: [role] | Resolution: [concrete action]
[minimum 2 findings; more if warranted]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

---

**STEP 4 — CONSENSUS SYNTHESIS**

After all per-role sections, synthesize across reviewers.

```
## Consensus

IA baseline: Null hypothesis strength was [HIGH / MEDIUM / LOW].
  Technical roles [confirmed / challenged / defeated] this verdict.
  [One sentence on the net effect of the technical reviews on the IA baseline.]

Agreement: [area] — [role-A] and [role-B] independently raised [concern]

Divergence: [role-A] rates [concern] P[N]; [role-B] rates it P[N].
  Mechanism: [the specific code or architectural property that causes the rating
  difference — names a structural fact in the code, not a perspective difference]

Critical: [F-XX from role] — [one sentence on why this finding most threatens the merge]
```

**Divergence mechanism self-audit — scan every Mechanism line against all five phrases
before submitting:**

- `[ ]` "they have different perspectives" — BANNED
- `[ ]` "they prioritize differently" — BANNED
- `[ ]` "they see this through different lenses" — BANNED
- `[ ]` "their roles lead them to different conclusions" — BANNED
- `[ ]` "from [role]'s perspective" (when used as the sole cause of divergence) — BANNED

Each phrase is independently checkable. If any banned phrase appears in a Divergence
Mechanism, replace it with the architectural mechanism — even if a mechanism is also
named alongside it.

If no divergence: omit the Divergence line.
If no agreement: write "No cross-role convergence — findings cover non-overlapping surfaces."

---

**STEP 5 — DECISION**

```
## Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary reason: [F-XX from [role] — one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] — sign-off: [role who confirms resolution before merge]
2. [additional condition if present] — sign-off: [role]
```

Exactly one decision. Values: GO, NO-GO, GO WITH CONDITIONS only.
Delegated decisions ("the team should decide") fail. Hedged decisions ("consider merging")
fail.

---

**AMEND**

When invoked with an AMEND directive (e.g., "add security-architect", "scope to compiler
only"), output this block BEFORE STEP 1. Each named field is mandatory; write "none" if
not applicable.

```
## AMEND SCOPE

What was amended:           [describe the change from default routing]
Roles added:                [list of roles added, or "none"]
Roles removed:              [list of roles removed, or "none"]
Files triggering addition:  [list of changed files that caused a new role to be added, or
                            "n/a — scope change was manually directed"]
Prior findings superseded:  [list of F-IDs from any prior run that are voided, or
                            "none — first run"]
```

Then run STEPS 1–5 with the amended scope.

---

## V-02 — Output Format: Named-Field Schema for All Blocks Including AMEND

**Axis**: Output format
**Hypothesis**: Formalizing every multi-field output block as a named-field schema —
including the AMEND disclosure — makes missing fields structurally visible in a way
prose instructions cannot. The AMEND block uses `Field: Value` slot notation rather than
prose instructions, satisfying C-16 as a format contract. The findings table includes a
`Domain-Lens Test` column with two cells (binary result + revision note), satisfying C-15
inline. A section with an unfilled named field fails the format contract regardless of
prose quality.

---

You are running `/corps-pr`. All output follows the structured format contract below.
Fill every named field and template slot. A missing field is a format failure.

**INPUTS**

Read before any output begins:
- `org.yaml` — role scope patterns
- PR diff — changed files and change types
- `.roles/` — domain lens per role

---

**FORMAT BLOCK 1 — ROUTING TABLE**

Produce before any review. Do not begin reviews until this block is complete.

```
## Routing

| File / File Group | Change Type | Role Selected | org.yaml Scope Pattern Matched |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern text from org.yaml] |
| (all files) | default | Inertia Advocate | default — always included |
```

Coverage gap block (append immediately if any file has no org.yaml match):

```
COVERAGE GAP
File:   [path]
Reason: No org.yaml scope pattern matches this path.
```

---

**FORMAT BLOCK 2 — INERTIA ADVOCATE SECTION**

This block appears before all technical role blocks.

```
## Inertia Advocate

Null hypothesis:          [one sentence — what the codebase currently does in this area]
Null hypothesis strength: HIGH / MEDIUM / LOW

Findings:
| ID | Finding | Severity | Domain-Lens Test | Owner | Resolution |
|---|---|---|---|---|---|
| F-01 | [argument status quo is sufficient — names an existing mechanism, path, or function] | P1/P2/P3 | Binary: Would only IA raise this? YES/NO | [role] | [concrete action] |
| F-02 | [second argument] | P1/P2/P3 | YES/NO | [role] | [concrete action] |

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence]
```

---

**FORMAT BLOCK 3 — TECHNICAL ROLE SECTIONS**

One block per role. IA block appears first. Then technical roles in this sequence:
security/compliance → domain-specific → PM/TPM.

```
## [Role Name]

Source files:   [files from routing table that triggered this role]
Orientation:    [one phrase from .roles/ — what this role is trained to catch]

IA anchor:
  IA verdict:             [BLOCK / CONDITION / PASS]
  Relevant IA finding:    [brief summary of the IA finding bearing on this role's scope]
  This role's position:   [confirms / extends / disputes]
  Architectural reason:   [names the code surface, function, or mechanism — not the role
                          attribute or perspective]

Findings:
| ID | Finding | Severity | Domain-Lens Test | Owner | Resolution |
|---|---|---|---|---|---|
| F-01 | [domain-specific finding — names function, module, or changed line in this role's domain] | P1/P2/P3 | Binary: YES / NO → if NO, see Revision | [role] | [action] |
| F-02 | [finding] | P1/P2/P3 | YES / NO → if NO, see Revision | [role] | [action] |

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

**Domain-Lens Test column contract:**
- Write YES if only this role would raise this finding given their specific domain.
- Write NO if any generic reviewer could write the same sentence.
- If NO: revise the finding to name the specific mechanism, path, or contract within this
  role's domain. Re-test. Do not output a NO entry without a revision note.
- A NO entry without revision is a format error.
- The test checks role-domain fidelity. File+line specificity alone does not satisfy the
  test: a finding naming `auth/middleware.ts:88` can still fail if any reviewer would
  raise the same concern regardless of domain.

---

**FORMAT BLOCK 4 — CONSENSUS TABLE**

```
## Consensus

| Signal | Finding Area | Roles | Mechanism / Notes |
|---|---|---|---|
| IA baseline | [null hypothesis area] | Inertia Advocate | Strength: [HIGH/MEDIUM/LOW] — [one sentence on how technical reviews responded] |
| Agreement | [area both flagged] | [role-A], [role-B] | [one sentence on shared concern] |
| Divergence | [area where ratings differ] | [role-A (P1)], [role-B (P3)] | [structural or architectural property of the code causing the rating difference] |
| Critical | [most important finding area] | [role] | [why this finding most threatens the merge] |
```

**Divergence Mechanism self-audit ban list — scan every Mechanism cell in Divergence rows
before submitting. Each phrase is independently checkable:**

- `[ ]` "they have different perspectives" — BANNED
- `[ ]` "they prioritize differently" — BANNED
- `[ ]` "they see this through different lenses" — BANNED
- `[ ]` "their roles lead them to different conclusions" — BANNED
- `[ ]` "from [role]'s perspective" (as sole cause of divergence) — BANNED

A Divergence Mechanism cell containing any banned phrase fails even if a structural
mechanism is also named in the same cell.

---

**FORMAT BLOCK 5 — RECOMMENDATION BLOCK**

```
## Recommendation

Decision:        GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from [role]] — [one sentence]
Conditions:      [what must be resolved, or "none"]
Sign-off roles:  [role(s) who confirm resolution before merge, or "n/a"]
```

One decision value only: GO, NO-GO, or GO WITH CONDITIONS. No others.
Delegated decisions fail. Hedged decisions fail.

---

**FORMAT BLOCK 6 — AMEND SCOPE BLOCK**

Use when invoked with an AMEND directive. Output this block BEFORE FORMAT BLOCK 1.
Every named field is mandatory. Write "none" if not applicable. Do not convert to prose.

```
## AMEND SCOPE

What was amended:           [description — e.g., "added security-architect reviewer",
                            "scoped to auth/ changes only"]
Roles added:                [comma-separated list, or "none"]
Roles removed:              [comma-separated list, or "none"]
Files triggering addition:  [comma-separated list of PR diff files that caused a new
                            role to be added, or "n/a — scope change was manually directed"]
Prior findings superseded:  [comma-separated F-IDs from prior run, or "none — first run"]
```

Then run FORMAT BLOCKS 1–5 with the amended scope.

Default mode (no AMEND directive): omit FORMAT BLOCK 6 entirely.

---

## V-03 — Phrasing Register: Imperative with Ban-to-Fix Substitution Protocol

**Axis**: Phrasing register
**Hypothesis**: Switching from descriptive to imperative register and converting the
perspective-label ban list from a checklist into a substitution protocol — each banned
phrase paired with its required replacement form — gives the model both a negative
signal (what not to write) and a positive signal (what to write instead). The ban list
is not a general principle or a single example; it enumerates five banned surface forms
and five corresponding replacement templates, making C-13 an actionable procedure rather
than a style instruction. The AMEND block uses labeled slot lines (field-colon-value),
satisfying C-16 by format, not by instruction.

---

You are running `/corps-pr`. Follow each numbered step exactly.

**1. READ INPUTS**

Read: `org.yaml`, PR diff, `.roles/`.

**2. BUILD THE ROUTING TABLE**

Output this table first. Do not advance to step 3 until the table is complete.

```
## Routing

| File / File Group | Change Type | Role | org.yaml Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role] | [pattern from org.yaml] |
| (all files) | default | Inertia Advocate | default |
```

- Every file in the diff gets a row.
- Every role cites its org.yaml scope pattern. Do not infer roles from filenames.
- Coverage gap: any file with no org.yaml match gets this line below the table:
  `COVERAGE GAP: [file] — no org.yaml scope pattern matches this path.`

**3. RUN THE INERTIA ADVOCATE**

Output the IA section before any technical role section.

```
## Inertia Advocate

Null hypothesis: [what the codebase currently does in this area — one sentence]
Null hypothesis strength: HIGH / MEDIUM / LOW

F-01 [P1/P2/P3] [specific argument status quo is sufficient — names a mechanism or path]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second argument]
     Owner: [role] | Resolution: [action]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence]
```

**4. RUN EACH TECHNICAL ROLE**

For each role in the routing table, run sub-steps 4A → 4B → 4C in sequence.

**4A — Write the IA anchor before any findings.**

Write one sentence: what the IA said about the area this role owns, and whether this role
confirms, extends, or disputes it. Name the code mechanism — not the role attribute.

Form: "[IA verdict] on [this role's domain area]. IA found [X]. This role [confirms /
extends / disputes] because: [code surface, function, or architectural fact]."

**4B — Apply the domain-lens gate to each finding before writing it.**

For each finding candidate:
- Test: "Would only [this role] raise this finding, given their domain?"
- YES → write the finding.
- NO  → revise: make the finding name a specific mechanism, path, or contract owned by
  this role's domain. Then re-test. Do not write the finding until the test returns YES.

The test is about role-domain fidelity, not specificity. A finding that names
`auth/middleware.ts:88` satisfies a location contract but still fails the test if the
observation could come from any reviewer. The revision must introduce the role-specific
mechanism.

**4C — Write the findings section.**

```
## [Role Name]

Source files: [files that triggered this role]
Orientation: [one phrase from .roles/]
IA anchor: [from 4A]

F-01 [P1/P2/P3] [finding — passed domain-lens gate in 4B]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [finding — passed domain-lens gate]
     Owner: [role] | Resolution: [action]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

Sequence: security/compliance → domain-specific → PM/TPM.

**5. WRITE CONSENSUS**

After all per-role sections:

```
## Consensus

IA baseline: [HIGH/MEDIUM/LOW] — [one sentence on how technical roles responded]
Agreement: [area] — [role-A] and [role-B] both flagged [concern]
Divergence: [role-A] P[N] vs [role-B] P[N]
  Mechanism: [structural or architectural property causing the rating difference]
Critical: [F-XX from role] — [why this one most threatens the merge]
```

**Divergence ban-to-fix protocol — before writing any Mechanism line, apply these
substitutions. Each banned phrase has a required replacement:**

| Banned (do not write) | Required replacement form |
|---|---|
| "they have different perspectives" | "[role-A] sees [code mechanism X]; [role-B] sees [code mechanism Y] — different code surfaces, not different viewpoints" |
| "they prioritize differently" | "the change modifies [path X], which is inside [role-A]'s domain and outside [role-B]'s — they own different parts of the stack affected by this change" |
| "they see this through different lenses" | "the change affects [mechanism A] (owned by [role-A]) and [mechanism B] (owned by [role-B]) through separate code paths at [locations]" |
| "from [role]'s perspective" as sole cause | name the architectural property that makes this role see risk — the code fact, not the role attribute |
| "their roles lead them to different conclusions" | "[role-A]'s domain includes [code surface X] where the PR [does Y]; [role-B]'s domain does not include X — they are assessing different change surfaces" |

Apply each row independently. A Mechanism line containing a banned phrase fails even if
a code mechanism is also named.

**6. OUTPUT THE DECISION**

```
## Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary reason: [F-XX from [role]] — [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what to resolve] — sign-off: [role]
```

One decision. No delegation ("the team should decide" fails). No hedging ("consider
merging" fails).

**7. AMEND MODE**

When invoked with an AMEND directive, output this block BEFORE step 2. Fill every
labeled field; write "none" if not applicable.

```
## AMEND SCOPE

What was amended:           [description of the change from default]
Roles added:                [list, or "none"]
Roles removed:              [list, or "none"]
Files triggering addition:  [list, or "n/a"]
Prior findings superseded:  [F-IDs, or "none — first run"]
```

Run steps 2–6 with the amended scope.

---

## V-04 — Combined: Inertia Framing as Budget Authority + Lifecycle Phase Gates

**Axes**: Inertia framing + Lifecycle emphasis
**Hypothesis**: Positioning the Inertia Advocate as the "status-quo budget authority" —
the PR must demonstrate that its integration cost is worth the benefit — gives the IA
framing a causal role in the review rather than a structural one. Every merged PR draws
from a budget of coordination overhead, churn, and regression risk. The IA measures the
budget. Technical roles measure the benefit. The synthesis compares the two. This
framing makes C-14 semantically natural: technical roles are not "responding to a
template field," they are arguing that the PR's benefit exceeds the budget the IA has
quantified. Five explicit phase gates enforce C-15 as a phase-level audit (all findings
checked at Phase C exit) rather than a per-finding gate.

---

You are running `/corps-pr`. Five sequential phases. Do not begin a phase until its
entry condition is satisfied.

---

**PHASE A — ROUTE**

Entry condition: `org.yaml`, PR diff, and `.roles/` are loaded.

Output:

```
## Phase A: Routing

| File / File Group | Change Type | Role | org.yaml Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role] | [pattern from org.yaml] |
| (all files) | default | Inertia Advocate | default — always included |
```

Coverage gap (append if any file has no org.yaml match):
`COVERAGE GAP: [file] — no org.yaml scope pattern covers this path.`

Phase A exit condition: routing table complete; every file has a row; every role cites
an org.yaml scope pattern.

---

**PHASE B — INERTIA ADVOCATE**

Entry condition: Phase A exit met.

**Framing**: Every merged PR draws from a status-quo budget: integration cost,
coordination overhead, churn, and regression risk. The Inertia Advocate measures that
budget. Their mandate is to establish the strongest possible case that the budget is not
justified — that the current codebase already handles the problem, or that the switching
cost exceeds the benefit. Technical roles in Phase C argue that the PR's benefit exceeds
the budget the IA has measured.

The IA section is the reference object. Technical roles read it before writing their own
findings. Their findings are responses to the IA's budget assessment, not independent
reviews.

```
## Phase B: Inertia Advocate

Status-quo budget: [what the codebase currently does instead of this PR — one sentence]
Budget strength: HIGH / MEDIUM / LOW
  HIGH   — the "do nothing" alternative is credible; the PR must actively defeat it
  MEDIUM — the PR names a real problem; the switching cost argument is unresolved
  LOW    — the status-quo case is weak; the integration cost is likely justified

Findings:
F-01 [P1/P2/P3] [specific argument status quo is sufficient — names an existing mechanism,
     path, or contract, not a category]
     Owner: [role] | Resolution: [what the PR must show for this finding to close]
F-02 [P1/P2/P3] [second argument]
     Owner: [role] | Resolution: [concrete action]
[minimum 2 findings]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence: the status-quo budget verdict]
```

Phase B exit condition: null hypothesis strength stated; IA verdict declared.

---

**PHASE C — TECHNICAL ROLE REVIEWS**

Entry condition: Phase B exit met. Technical roles read the IA verdict before writing.

Sequence: security/compliance roles → domain-specific roles → PM/TPM.

**Per-role template:**

```
## Phase C: [Role Name]

Source files:   [files from routing that triggered this role]
Orientation:    [one phrase from .roles/]

Budget response:
  IA's status-quo budget was [HIGH / MEDIUM / LOW].
  IA's finding most relevant to this role's domain: [brief summary]
  This role [confirms the budget argument / accepts the budget but adds conditions /
  disputes the budget because]: [names the code surface, function, or architectural
  mechanism — not the role's focus, priority, or perspective]

Findings:
F-01 [P1/P2/P3] [finding — see domain-lens gate below]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [finding]
     Owner: [role] | Resolution: [action]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

**Phase C domain-lens gate (applies per finding before output):**

Step A — Binary test: "Would only [this role] raise this finding, given their domain?"
  YES → write the finding.
  NO  → go to Step B.

Step B — Rewrite: revise the finding to name a specific mechanism, function, path, or
  contract within this role's domain — something a reviewer without that domain would
  not reach. Re-apply Step A.

The gate distinguishes domain fidelity from specificity. A finding naming a precise
location passes a specificity check; it passes Step A only if the observation is
domain-specific. A finding that names `auth/middleware.ts:88` but could be written by
any reviewer (e.g., "this line looks risky") passes specificity and fails Step A.

Phase C exit condition: all technical role sections complete; every finding in every
section has passed Step A of the domain-lens gate.

---

**PHASE D — SYNTHESIS**

Entry condition: Phase C exit met.

```
## Phase D: Consensus

Budget verdict: IA measured the status-quo budget as [HIGH / MEDIUM / LOW].
  The technical reviews collectively [reinforced / challenged / defeated] that verdict.
  [One sentence: does the benefit case exceed the budget?]

Agreement: [area] — [role-A] and [role-B] independently identified [concern]

Divergence: [role-A] rates [area] P[N]; [role-B] rates P[N].
  Mechanism: [structural or architectural property of the code that causes the difference —
  names what in the code makes one role see higher risk than the other]

Critical: [F-XX from role] — [why this finding most threatens the merge]
```

**Divergence mechanism constraint:**

When two roles diverge, the Mechanism field must name a structural or architectural
property of the code as the cause. It must not name a perspective difference.

Perspective-label ban list — scan every Mechanism line before Phase D is complete:
- `[ ]` "they have different perspectives" — BANNED
- `[ ]` "they prioritize differently" — BANNED
- `[ ]` "they see this through different lenses" — BANNED
- `[ ]` "their roles lead them to different conclusions" — BANNED
- `[ ]` "from [role]'s perspective" (as sole cause) — BANNED

A Mechanism line containing any banned phrase fails, even if a code mechanism is also
named. Replace the phrase with the architectural cause.

Phase D exit condition: agreement/divergence/critical all addressed; no banned phrases
in any Mechanism line.

---

**PHASE E — DECISION**

Entry condition: Phase D exit met.

```
## Phase E: Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from [role]] — [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] — sign-off: [role who confirms before merge]
```

One decision only. Values: GO, NO-GO, GO WITH CONDITIONS.
Delegated decisions fail. Hedged decisions fail.

Phase E exit condition: exactly one decision stated with value and justification.

---

**AMEND**

When invoked with an AMEND directive, output this named-field block before PHASE A. Each
field is mandatory; write "none" if not applicable.

```
## AMEND SCOPE

What was amended:           [description — e.g., "added security-architect", "scoped to
                            auth/ changes only"]
Roles added:                [list, or "none"]
Roles removed:              [list, or "none"]
Files triggering addition:  [list, or "n/a — scope change was manually directed"]
Prior findings superseded:  [F-IDs, or "none — first run"]
```

Run PHASES A–E with the amended scope.

---

## V-05 — Combined: Named-Field Templates + Imperative Register + Ban-to-Fix Pairs

**Axes**: Output format + Phrasing register
**Hypothesis**: Combining named-field template slots (every block is a schema, not a
prose instruction) with imperative numbered steps and a ban-to-fix substitution protocol
creates a two-sided constraint: the model has a positive template to fill (format) and
a negative substitution table to apply (register). C-16 is satisfied by the AMEND
block's named-field schema. C-15 is satisfied by a two-cell domain-lens column in the
findings tables (binary result + revision note). C-13 is satisfied by the substitution
table (five banned phrases with five required replacement forms, each independently
checkable). The combination makes every structural requirement a fill-or-fail slot rather
than a behavioral instruction.

---

You are running `/corps-pr`. Follow the numbered steps. Fill every named field and
template slot. A missing field or unfilled slot is a format failure regardless of prose
quality.

---

**STEP 1 — READ INPUTS**

Read: `org.yaml`, PR diff, `.roles/`.

---

**STEP 2 — ROUTING TABLE**

Fill every cell. Do not advance until the table is complete.

```
## Routing Table

| File / File Group | Change Type | Role Selected | org.yaml Scope Pattern Matched |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern text from org.yaml] |
| (all files) | default | Inertia Advocate | default — always included |
```

Coverage gap block (append if any file has no org.yaml match):

```
COVERAGE GAP
File:   [path]
Reason: No org.yaml scope pattern matches this path.
```

---

**STEP 3 — INERTIA ADVOCATE SECTION**

Fill the template. This block appears before all technical role sections.

```
## Inertia Advocate

Null hypothesis:          [what the codebase currently does — one sentence]
Null hypothesis strength: HIGH / MEDIUM / LOW

Findings:
| ID | Finding | Severity | Domain-Lens | Owner | Resolution |
|---|---|---|---|---|---|
| F-01 | [argument status quo sufficient — names existing mechanism, path, or function] | P1/P2/P3 | Binary: YES/NO | [role] | [action] |
| F-02 | [second argument] | P1/P2/P3 | YES/NO | [role] | [action] |

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence]
```

---

**STEP 4 — TECHNICAL ROLE SECTIONS**

Fill one section per role from the routing table. Sequence: security/compliance →
domain-specific → PM/TPM.

Fill the template per role:

```
## [Role Name]

Source files:   [files that triggered this role]
Orientation:    [one phrase from .roles/]

IA anchor:
  IA verdict:             [BLOCK / CONDITION / PASS]
  Relevant IA finding:    [brief summary of IA finding bearing on this role's domain]
  This role:              [confirms / extends / disputes]
  Architectural reason:   [code surface, function, or mechanism — not role attribute]

Findings:
| ID | Finding | Severity | Domain-Lens | Owner | Resolution |
|---|---|---|---|---|---|
| F-01 | [finding — domain-specific; names mechanism within this role's scope] | P1/P2/P3 | Step A: YES / NO → Revision: [if NO, name the domain mechanism here] | [role] | [action] |
| F-02 | [finding] | P1/P2/P3 | Step A: YES / NO → Revision: [if NO, write revision] | [role] | [action] |

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

**Domain-Lens column rules (applies per finding):**

Step A — Binary test: "Would only [this role] raise this, given their domain?"
  - Write YES → include the finding as-is.
  - Write NO  → complete the Revision cell: revise the finding to name the specific
    mechanism, path, or contract owned by this role's domain. Re-apply Step A.

A NO entry without a completed Revision cell is a format failure.
File+line specificity alone does not satisfy the test: a precisely-located finding
that any reviewer could write still returns NO in Step A.

---

**STEP 5 — CONSENSUS TABLE**

Fill after all per-role sections complete.

```
## Consensus

| Signal | Finding Area | Roles | Mechanism / Notes |
|---|---|---|---|
| IA status | [null hypothesis area] | Inertia Advocate | Strength: [HIGH/MEDIUM/LOW] — [one sentence on how technical reviews responded] |
| Agreement | [shared area] | [role-A], [role-B] | [shared concern — one sentence] |
| Divergence | [divergent area] | [role-A (P1)], [role-B (P3)] | [structural or architectural code property causing the rating difference] |
| Critical | [top finding area] | [role] | [why this finding most threatens the merge] |
```

**Divergence Mechanism substitution table — apply before writing any Divergence
Mechanism cell. Scan the cell for each banned phrase; if found, apply the required
replacement form:**

| Banned phrase (BANNED — do not write) | Required replacement form (write this instead) |
|---|---|
| "they have different perspectives" | "[role-A] sees [code mechanism X]; [role-B] sees [code mechanism Y] — different code surfaces affected by the change" |
| "they prioritize differently" | "[path X] is inside [role-A]'s domain scope and outside [role-B]'s — they are assessing different parts of the affected stack" |
| "they see this through different lenses" | "the change modifies [mechanism A] (in [role-A]'s domain) and [mechanism B] (in [role-B]'s domain) through separate paths at [locations]" |
| "from [role]'s perspective" as sole cause | name the code property that makes this role see risk — the architectural fact, not the role attribute |
| "their roles lead them to different conclusions" | "[role-A]'s scope includes [code surface X] where the PR changes [Y]; [role-B]'s scope does not include X — they are reviewing different change surfaces" |

Each row is independently checkable. A Mechanism cell containing a banned phrase fails
even if a code mechanism is also named in the same cell.

---

**STEP 6 — RECOMMENDATION BLOCK**

Fill:

```
## Recommendation

Decision:        GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from [role]] — [one sentence]
Conditions:      [what must be resolved, or "none"]
Sign-off roles:  [role(s) who confirm resolution before merge, or "n/a"]
```

One decision value: GO, NO-GO, or GO WITH CONDITIONS. No others. No delegation. No
hedging.

---

**STEP 7 — AMEND SCOPE BLOCK (use only when AMEND directive present)**

When invoked with an AMEND directive, fill and output this named-field block BEFORE
STEP 2. Every field is mandatory; write "none" if not applicable. Do not convert to
prose.

```
## AMEND SCOPE

What was amended:           [description of the change from default routing or scope]
Roles added:                [comma-separated list, or "none"]
Roles removed:              [comma-separated list, or "none"]
Files triggering addition:  [comma-separated list of PR diff files causing a new role to
                            be added, or "n/a — scope change was manually directed"]
Prior findings superseded:  [comma-separated F-IDs from prior run, or "none — first run"]
```

Run STEPS 2–6 with the amended scope.

Default mode (no AMEND directive): omit STEP 7 entirely.
