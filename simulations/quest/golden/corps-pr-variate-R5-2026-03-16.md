---
skill: quest-variate
skill_target: corps-pr
round: 5
date: 2026-03-16
rubric_version: 5
---

# Variate R5 — corps-pr

5 complete prompt body variations for the `corps-pr` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Axes Selected

| Axis | Used In | R5 Focus |
|------|---------|----------|
| Inertia framing (IA as cost ledger with 4 named categories; technical roles dispute specific line items) | V-01, V-04, V-05 | C-17: cost-term framing by schema, not instruction |
| Lifecycle emphasis (top-level pipeline declaration names all 5 phases with entry/exit conditions and criteria gated, before execution) | V-02, V-04 | C-18: phase-gate structure auditable before execution |
| Role sequence (two-pass finding generation: draft all → batch domain-lens audit → output only passing findings; audit is the named Phase C exit) | V-03, V-05 | C-18: domain-lens gate as Phase C exit, not per-finding reminder |
| Output format (named-field schema for all blocks including AMEND) | V-02, V-04, V-05 | C-16: AMEND block as schema, not prose |
| Phrasing register (ban-to-fix substitution table) | V-03, V-04, V-05 | C-13: banned phrases paired with required replacement forms |

**What changed from R4:**
- R4 V-04 introduced the budget authority framing and 5-phase gates, which became C-17 and C-18.
- R5 V-01 formalizes C-17 as a 4-category cost ledger schema — IA fills cells, technical roles dispute specific cost line items, not general conclusions.
- R5 V-02 formalizes C-18 as a top-level pipeline declaration block before execution — the phase-gate structure is declared and auditable before a single finding is written.
- R5 V-03 formalizes C-18's domain-lens exit gate differently: two-pass finding generation (draft → batch audit → output) makes the gate a named phase transition, not a per-finding reminder embedded in a template.
- R5 V-04 combines V-01 + V-02: cost ledger + pipeline declaration, cross-referenced so Phase C IA anchors cite specific ledger cost categories.
- R5 V-05 combines V-01 + V-03 + ban-to-fix: cost ledger + two-pass audit + substitution table, all three working at different phases of the review.

---

## V-01 — Inertia Framing: IA Cost Ledger

**Axis**: Inertia framing
**Hypothesis**: Requiring the Inertia Advocate to fill a 4-category cost ledger (maintenance
burden, incident exposure, integration cost, regression risk — each with a current-state
cost and an adoption cost) makes C-17 a fill-or-fail format constraint rather than a
behavioral instruction. Technical roles that dispute the IA must name a specific cost
category from the ledger and counter the IA's estimate with a code-grounded reason — they
cannot acknowledge the IA in general terms. The ledger also makes the IA verdict quantified
by construction: a section that lists concerns without filling cost cells fails the schema.

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
## Routing

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern from org.yaml that matched] |
| (all files) | default | Inertia Advocate | default — always included |
```

Rules:
- Every changed file appears in at least one row. No file is silently dropped.
- Role selection must cite the org.yaml scope pattern — not inferred from filename.
- Coverage gap: if any file has no org.yaml match, write immediately after the table:
  `COVERAGE GAP: [file] — no org.yaml scope pattern covers this path.`

---

**STEP 2 — INERTIA ADVOCATE (always first)**

The IA section appears before all technical role sections. This is structural and
non-configurable. Technical roles read the IA cost ledger before writing their own findings.

The IA is the status-quo budget authority. Their verdict must be expressed in cost terms —
not as enumerated risks or concerns, but as a quantified tradeoff: what it costs to keep
the current codebase as-is, versus what it costs to adopt this PR. Technical roles must
engage the arithmetic — they must dispute a specific cost cell, not dismiss the IA position
as preference or conservatism.

Fill every cost ledger cell. Use LOW / MED / HIGH / CRITICAL for magnitude.

```
## Inertia Advocate

Null hypothesis: The codebase currently [does X via mechanism Y].

Cost ledger:
| Cost Category    | Current-State Cost                                      | Adoption Cost (this PR)                        | Net delta |
|---|---|---|---|
| Maintenance      | [LOW/MED/HIGH — what it costs to keep current approach] | [cost of owning new code path long-term]       | [+/-]     |
| Incident exposure| [current failure frequency/severity in this area]      | [residual exposure if PR merges]               | [+/-]     |
| Integration cost | [coordination overhead to keep current approach]       | [churn, downstream wiring, test fixture cost]  | [+/-]     |
| Regression risk  | [risk of new failures from current approach as-is]     | [risk of regressions introduced by this PR]    | [+/-]     |

Budget verdict: [one sentence — does total adoption cost exceed total current-state cost?]
Budget strength: HIGH / MEDIUM / LOW
  HIGH   — adoption cost clearly exceeds benefit; status quo is credible
  MEDIUM — tradeoff is real; PR must demonstrate benefit exceeds switching cost
  LOW    — adoption cost is justified; status quo case is weak

Findings:
F-01 [P1/P2/P3] [specific argument current state is sufficient — names an existing mechanism,
     path, or function, not a category]
     Owner: [role] | Resolution: [what must change for this finding to close]
F-02 [P1/P2/P3] [second argument, grounded in the cost ledger above]
     Owner: [role] | Resolution: [concrete action]
[minimum 2 findings]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence grounded in the cost ledger]
```

---

**STEP 3 — TECHNICAL ROLE REVIEWS**

Run each role from the routing table. Sequence: security and compliance roles first →
domain-specific technical roles second → PM/TPM roles last.

For each finding in every technical role section, execute the domain-lens gate before
writing the finding:

```
DOMAIN-LENS GATE (execute per finding):

Step A — Binary test:
  "Would only [this role] raise this finding, given their domain?"
  YES → the finding is domain-loaded. Write it.
  NO  → any generic reviewer could write this. Do not write it. Go to Step B.

Step B — Rewrite consequence:
  Revise the finding to name a specific mechanism, function, path, or contract that
  belongs to this role's domain and is unreachable without it. Then re-execute Step A.
  A finding that still returns NO after revision must be dropped.
```

The gate tests domain fidelity, not specificity. A finding that names
`auth/middleware.ts:88` satisfies a location contract but still fails Step A if any
reviewer could have written the same observation regardless of domain.

Use this section template:

```
## Review: [Role Name]

Source files:  [files from routing table that triggered this role]
Orientation:   [one phrase from .roles/ — what this role is trained to catch]

IA cost anchor:
  IA budget strength:         [HIGH / MEDIUM / LOW]
  Cost category disputed:     [which ledger row this role addresses — Maintenance /
                               Incident exposure / Integration cost / Regression risk]
  IA's estimate for that row: [brief restatement of what the IA wrote in that cell]
  This role [confirms / disputes] that estimate because:
    [names the code surface, function, or architectural mechanism — not the role's
     perspective or priority. Example: "IA rated Integration cost MED based on downstream
     wiring; compiler-lead disputes this: the new codegen emission at compiler/emit.ts:214
     requires rewriting 3 test fixtures not counted in the IA's coordination estimate."]

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

IA cost ledger: Budget strength was [HIGH / MEDIUM / LOW].
  Technical roles collectively [reinforced / challenged / defeated] the IA's cost estimate.
  Net: [one sentence — does the benefit case exceed the cost budget, or not?]

Agreement: [area] — [role-A] and [role-B] independently raised [concern]

Divergence: [role-A] rates [concern] P[N]; [role-B] rates it P[N].
  Mechanism: [the specific code or architectural property causing the rating difference —
  names a structural fact in the code, not a perspective difference]

Critical: [F-XX from role] — [one sentence on why this finding most threatens the merge]
```

**Divergence mechanism self-audit — scan every Mechanism line against all five phrases
before submitting. Each phrase is independently checkable:**

- `[ ]` "they have different perspectives" — BANNED
- `[ ]` "they prioritize differently" — BANNED
- `[ ]` "they see this through different lenses" — BANNED
- `[ ]` "their roles lead them to different conclusions" — BANNED
- `[ ]` "from [role]'s perspective" (when used as the sole cause of divergence) — BANNED

Replace any banned phrase with the architectural mechanism — even if a mechanism is also
named alongside it.

---

**STEP 5 — DECISION**

```
## Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary reason: [F-XX from [role]] — [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] — sign-off: [role who confirms resolution before merge]
2. [additional condition if present] — sign-off: [role]
```

Exactly one decision. Values: GO, NO-GO, GO WITH CONDITIONS only.
Delegated decisions ("the team should decide") fail. Hedged decisions ("consider merging")
fail.

---

**AMEND**

When invoked with an AMEND directive, output this block BEFORE STEP 1. Each named field
is mandatory; write "none" if not applicable.

```
## AMEND SCOPE

What was amended:           [describe the change from default routing]
Roles added:                [list of roles added, or "none"]
Roles removed:              [list of roles removed, or "none"]
Files triggering addition:  [list of changed files that caused a new role, or
                            "n/a — scope change was manually directed"]
Prior findings superseded:  [list of F-IDs from any prior run that are voided, or
                            "none — first run"]
```

Then run STEPS 1–5 with the amended scope.

---

## V-02 — Lifecycle Emphasis: Top-Level Pipeline Declaration

**Axis**: Lifecycle emphasis
**Hypothesis**: Moving the phase-gate declarations to a top-level pipeline specification —
before any content begins — makes the review structure auditable before execution: a
reviewer can inspect whether the output followed the declared pipeline without having to
reconstruct the intended structure from scattered inline notes. The domain-lens gate appears
as the named Phase C exit condition in the pipeline spec, satisfying C-18 by declaration.
An output that produces correct findings without matching the declared phase structure fails
C-18 even if all other criteria pass — the spec is the contract, and the output either
satisfies it or it doesn't.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline. The pipeline
declaration below is the execution contract. Read it before producing any output. Each
phase may not begin until its stated entry condition is satisfied.

---

**PIPELINE DECLARATION**

```
| Phase | Name              | Entry Condition                              | Exit Condition                                                      | Criteria Gated                  |
|-------|-------------------|----------------------------------------------|---------------------------------------------------------------------|---------------------------------|
| A     | Route             | org.yaml + PR diff + .roles/ loaded    | Routing table complete; every changed file has a row; every role    | C-01, C-06                      |
|       |                   |                                              | cites an org.yaml scope pattern                                     |                                 |
| B     | Inertia Review    | Phase A exit met                             | IA section complete: null hypothesis stated, budget strength         | C-11, C-17                      |
|       |                   |                                              | declared, cost terms present in all 4 ledger cells, IA verdict       |                                 |
|       |                   |                                              | issued in cost terms                                                |                                 |
| C     | Technical Reviews | Phase B exit met; roles read Phase B before  | All role sections complete; every finding in every section has       | C-02, C-05, C-07, C-14, C-15   |
|       |                   | writing                                      | passed the domain-lens gate (Step A binary test + Step B rewrite    |                                 |
|       |                   |                                              | consequence); no finding advances to Phase D without passing it     |                                 |
| D     | Synthesis         | Phase C exit met                             | Consensus complete; all divergence Mechanism lines free of          | C-03, C-09, C-12, C-13         |
|       |                   |                                              | perspective-label phrases from the ban list                         |                                 |
| E     | Decision          | Phase D exit met                             | Exactly one GO / NO-GO / GO WITH CONDITIONS decision issued with    | C-04, C-10                      |
|       |                   |                                              | justification and sign-off roles for any conditions                 |                                 |
```

**Phase C exit condition governs all technical role findings.** No finding advances to
Phase D synthesis without passing the domain-lens gate. This is non-negotiable regardless
of finding quality in other respects.

---

**PHASE A — ROUTE**

Entry condition: `org.yaml`, PR diff, and `.roles/` loaded.

```
## Phase A: Routing

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern from org.yaml] |
| (all files) | default | Inertia Advocate | default — always included |
```

Coverage gap: if any file matches no org.yaml scope pattern, append immediately:
`COVERAGE GAP: [file] — no org.yaml scope pattern covers this path.`

Phase A exit: routing table complete; every file has a row; every role cites an org.yaml
scope pattern.

---

**PHASE B — INERTIA REVIEW**

Entry condition: Phase A exit met.

The IA is the status-quo budget authority. Their section establishes the quantified cost
case for not merging. Their verdict must be expressed in cost terms — what the current
state costs to maintain, what this PR costs to adopt — so technical roles must engage the
arithmetic in Phase C. A Phase B section that lists concerns without filling cost terms
fails its exit condition.

```
## Phase B: Inertia Advocate

Null hypothesis: The codebase currently [does X via mechanism Y].

Cost terms (required; all four rows must be filled):
  Maintenance cost:    [what it costs to keep the current approach — one sentence]
  Incident exposure:   [current failure risk/frequency in this area]
  Adoption cost:       [coordination overhead + downstream impact of this PR]
  Regression risk:     [new failure risk introduced by this PR vs. current state]

Budget verdict: [one sentence — does adoption cost exceed current-state cost, or not?]
Budget strength: HIGH / MEDIUM / LOW

Findings:
F-01 [P1/P2/P3] [specific argument current state is sufficient — names existing mechanism,
     path, or function]
     Owner: [role] | Resolution: [what must change for this finding to close]
F-02 [P1/P2/P3] [second argument grounded in cost analysis]
     Owner: [role] | Resolution: [concrete action]
[minimum 2 findings]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence in cost terms]
```

Phase B exit: null hypothesis stated; all 4 cost terms filled; budget strength declared;
IA verdict issued.

---

**PHASE C — TECHNICAL REVIEWS**

Entry condition: Phase B exit met. Technical roles read Phase B before writing.

Sequence: security/compliance → domain-specific → PM/TPM.

**Domain-lens gate — Phase C exit condition. All findings must pass before Phase D begins.**

For each finding candidate in every role section:

```
Step A — Binary test: "Would only [this role] raise this finding, given their domain?"
  YES → finding is domain-loaded. Include it.
  NO  → any generic reviewer could write this. Go to Step B.

Step B — Rewrite consequence: revise the finding to name a specific mechanism, path,
  function, or contract owned by this role's domain — something unreachable without it.
  Re-execute Step A. A finding that still returns NO after revision is dropped.
```

The gate tests domain fidelity, not specificity. A finding naming a precise location passes
a location check; it passes Step A only if the observation requires this role's domain.

Per-role template:

```
## Phase C: [Role Name]

Source files:   [files from Phase A routing that triggered this role]
Orientation:    [one phrase from .roles/]

IA cost anchor:
  Phase B budget strength:    [HIGH / MEDIUM / LOW]
  IA cost term bearing on this domain:
    [which Phase B cost row is most relevant to this role's findings]
  This role [confirms / disputes] that cost estimate because:
    [names the code surface, function, or mechanism — not role perspective or priority]

Findings: [all passed domain-lens gate]
F-01 [P1/P2/P3] [domain-specific finding — mechanism within this role's scope]
     Owner: [role] | Resolution: [concrete action — what and where]
F-02 [P1/P2/P3] [second finding]
     Owner: [role] | Resolution: [action]
[minimum 2; more if warranted]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

Phase C exit: all role sections complete; every finding passed Step A of the domain-lens
gate; Phase C exit condition from the pipeline declaration is satisfied.

---

**PHASE D — SYNTHESIS**

Entry condition: Phase C exit met.

```
## Phase D: Consensus

IA cost verdict: Budget strength was [HIGH / MEDIUM / LOW].
  Technical roles [reinforced / challenged / defeated] this verdict.
  [One sentence: does benefit case exceed the cost budget?]

Agreement: [area] — [role-A] and [role-B] independently raised [concern]

Divergence: [role-A] rates [area] P[N]; [role-B] rates P[N].
  Mechanism: [structural or architectural property of the code causing the difference —
  names a fact in the code, not a perspective difference]

Critical: [F-XX from role] — [why this finding most threatens the merge]
```

**Perspective-label ban-to-fix — apply before writing any Mechanism line. Each row is
independently checkable:**

| Banned (do not write) | Required replacement form |
|---|---|
| "they have different perspectives" | "[role-A] sees [code mechanism X]; [role-B] sees [code mechanism Y] — different code surfaces, not different viewpoints" |
| "they prioritize differently" | "[path X] is inside [role-A]'s domain and outside [role-B]'s — they own different parts of the affected stack" |
| "they see this through different lenses" | "the change affects [mechanism A] (in [role-A]'s domain) and [mechanism B] (in [role-B]'s domain) through separate paths at [locations]" |
| "from [role]'s perspective" as sole cause | name the code property that creates risk — the architectural fact, not the role attribute |
| "their roles lead them to different conclusions" | "[role-A]'s scope includes [code surface X] where the PR changes [Y]; [role-B]'s scope does not include X — different change surfaces" |

A Mechanism line containing a banned phrase fails even if a code mechanism is also named.
Apply all rows before Phase D is declared complete.

Phase D exit: agreement/divergence/critical addressed; no banned phrases in any Mechanism
line.

---

**PHASE E — DECISION**

Entry condition: Phase D exit met.

```
## Phase E: Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from [role]] — [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] — sign-off: [role who confirms before merge]
2. [additional condition if present] — sign-off: [role]
```

One decision only. Values: GO, NO-GO, GO WITH CONDITIONS. Delegated decisions fail.
Hedged decisions fail.

Phase E exit: exactly one decision stated with value, justification, and sign-off roles if
conditions apply.

---

**AMEND**

When invoked with an AMEND directive, output this named-field block before PHASE A.
Every field is mandatory; write "none" if not applicable.

```
## AMEND SCOPE

What was amended:           [description]
Roles added:                [list, or "none"]
Roles removed:              [list, or "none"]
Files triggering addition:  [list, or "n/a — scope change was manually directed"]
Prior findings superseded:  [F-IDs, or "none — first run"]
```

Run PHASES A–E with the amended scope.

---

## V-03 — Role Sequence: Two-Pass Finding Generation

**Axis**: Role sequence (finding generation procedure)
**Hypothesis**: A two-pass finding generation model — draft all candidates first, then run
a batch domain-lens audit before any finding is output — makes the domain-lens gate a named
phase transition rather than a per-finding reminder embedded in a template. The audit log
(one line per draft, stating pass/fail/revision) is the explicit Phase C exit gate: if any
draft finding is still in the audit without a disposition, Phase C is incomplete. This makes
C-18's domain-lens exit condition structurally visible as an unfilled audit log, not as a
behavioral instruction that may or may not have been followed.

---

You are running `/corps-pr`. Follow each numbered step exactly.

**1. READ INPUTS**

Read: `org.yaml`, PR diff, `.roles/`.

---

**2. BUILD THE ROUTING TABLE**

Output before advancing to step 3. Do not begin reviews until the table is complete.

```
## Routing

| File / File Group | Change Type | Role | org.yaml Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role] | [pattern from org.yaml] |
| (all files) | default | Inertia Advocate | default |
```

Every file gets a row. Every role cites its org.yaml scope pattern. Do not infer roles
from filenames.

Coverage gap: any file with no org.yaml match gets:
`COVERAGE GAP: [file] — no org.yaml scope pattern matches this path.`

---

**3. RUN THE INERTIA ADVOCATE**

The IA section appears before all technical role sections.

The IA is the status-quo budget authority. Their verdict is expressed in cost terms: what
it costs to maintain the current approach and what it costs to adopt this PR. Their findings
are grounded in the cost tradeoff — not enumerated risks, but a quantified case.

```
## Inertia Advocate

Null hypothesis: [what the codebase currently does in this area — one sentence]

Cost terms:
  Current-state cost: [maintenance burden + incident exposure — one sentence]
  Adoption cost:      [integration overhead + regression risk of this PR — one sentence]
  Budget verdict:     [net: does adoption cost exceed current-state cost?]

Budget strength: HIGH / MEDIUM / LOW

F-01 [P1/P2/P3] [argument current state is sufficient — names a mechanism or path]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second argument, grounded in cost terms]
     Owner: [role] | Resolution: [action]
[minimum 2 findings]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence]
```

---

**4. GENERATE TECHNICAL ROLE FINDINGS — TWO PASSES**

For each role in the routing table, run sub-steps 4A → 4B → 4C in sequence.
Sequence across roles: security/compliance → domain-specific → PM/TPM.

**4A — Draft pass: write all finding candidates without filtering.**

Write every plausible finding for this role. Label each draft D-01, D-02, ... Do not apply
the domain-lens test yet. Include the IA cost anchor as a separate block before the drafts.

IA cost anchor (write before drafts):
```
IA budget strength for this domain: [HIGH / MEDIUM / LOW]
IA cost term bearing on this role: [which cost category — maintenance / incident /
  integration / regression]
IA's estimate: [brief restatement]
This role's initial position: [confirms / disputes — one phrase]
```

Draft findings:
```
D-01: [finding candidate — write exactly what you would output, without filtering]
D-02: [second candidate]
[all candidates, no floor]
```

**4B — Audit pass: domain-lens gate on every draft.**

For each draft D-XX, apply the audit test:

```
AUDIT TEST: "Would only [this role] raise this finding, given their domain?"
```

- YES → finding is domain-loaded. Assign it the next F-ID (F-01, F-02, ...). Advance to 4C.
- NO  → any generic reviewer could write this. Rewrite: name a specific mechanism, path,
  function, or contract owned by this role's domain — something unreachable without it.
  Re-apply the test.
  - Rewrite returns YES → assign F-ID. Advance to 4C.
  - Rewrite still returns NO → drop the finding.

The test is about domain fidelity, not location precision. A finding naming
`auth/middleware.ts:88` passes a specificity check; it passes the audit only if the
observation requires this role's domain to make — not if any reviewer could arrive there.

Write the audit log (this is the Phase C exit gate — it must be complete before synthesis):

```
## Audit log — [Role Name]

D-01 → [YES → F-01 | NO → revised → F-01 | NO → dropped]
D-02 → [YES → F-02 | NO → revised → F-02 | NO → dropped]
[one line per draft]

Audit complete: [N] drafts → [M] findings passed
```

**4C — Output pass: write the findings section.**

Write only findings that passed 4B. Include the IA cost anchor from 4A, revised with the
final role position.

```
## [Role Name]

Source files:  [files that triggered this role]
Orientation:   [one phrase from .roles/]

IA cost anchor:
  IA budget strength: [HIGH / MEDIUM / LOW]
  Cost category: [which ledger row bears on this role]
  This role [confirms / disputes] the IA estimate because:
    [code surface, function, or mechanism — not role attribute]

Findings: [only findings that passed the audit in 4B]
F-01 [P1/P2/P3] [finding — passed domain-lens audit]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second finding — passed audit]
     Owner: [role] | Resolution: [action]
[minimum 2; more if warranted]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

All role audit logs must be complete before proceeding to step 5. An incomplete audit log
is an incomplete Phase C.

---

**5. WRITE CONSENSUS**

After all per-role sections and their audit logs are complete:

```
## Consensus

IA budget: [HIGH/MEDIUM/LOW] — [one sentence: how technical roles responded to the cost case]

Agreement: [area] — [role-A] and [role-B] both flagged [concern] independently

Divergence: [role-A] P[N] vs [role-B] P[N]
  Mechanism: [structural or architectural property causing the rating difference]

Critical: [F-XX from role] — [why this one most threatens the merge]
```

**Divergence ban-to-fix — apply before writing any Mechanism line:**

| Banned | Required replacement |
|---|---|
| "they have different perspectives" | "[role-A] sees [code mechanism X]; [role-B] sees [code mechanism Y] — different code surfaces" |
| "they prioritize differently" | "[path X] is in [role-A]'s domain and outside [role-B]'s — different parts of the affected stack" |
| "they see this through different lenses" | "the change affects [mechanism A] (owned by [role-A]) and [mechanism B] (owned by [role-B]) at [locations]" |
| "from [role]'s perspective" as sole cause | name the code property causing risk — the fact, not the role attribute |
| "their roles lead them to different conclusions" | "[role-A]'s scope includes [code surface X] where the PR changes [Y]; [role-B]'s scope does not" |

---

**6. OUTPUT THE DECISION**

```
## Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary reason: [F-XX from [role]] — [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what to resolve] — sign-off: [role]
2. [additional condition if present] — sign-off: [role]
```

One decision. No delegation. No hedging.

---

**7. AMEND MODE**

When invoked with an AMEND directive, output this named-field block BEFORE step 2.
Every field is mandatory; write "none" if not applicable.

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

## V-04 — Combined: IA Cost Ledger + Pipeline Declaration

**Axes**: Inertia framing + Lifecycle emphasis
**Hypothesis**: The IA cost ledger (C-17) and the pipeline declaration block (C-18)
reinforce each other when combined: the pipeline spec explicitly references the IA cost
ledger as a Phase B exit requirement, and Phase C IA anchors are required to cite a
specific ledger row — creating a chain from the declared spec through the IA section into
each technical role section. C-17 is satisfied by the cost ledger schema; C-18 is satisfied
by the top-level pipeline declaration that names the domain-lens gate as the Phase C exit
condition. An output that skips either the cost cells or the declared phase structure fails
both criteria independently. The combination makes the two criteria mutually reinforcing
rather than parallel.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline. The pipeline
declaration below is the execution contract. Read it before any output begins. Each phase
may not begin until its stated entry condition is satisfied.

---

**PIPELINE DECLARATION**

```
| Phase | Name              | Entry Condition                               | Exit Condition                                                       | Criteria Gated             |
|-------|-------------------|-----------------------------------------------|----------------------------------------------------------------------|----------------------------|
| A     | Route             | org.yaml + PR diff + .roles/ loaded     | Routing table complete; every file has a row; every role cites       | C-01, C-06                 |
|       |                   |                                               | an org.yaml scope pattern                                            |                            |
| B     | Inertia Review    | Phase A exit met                              | IA cost ledger complete (all 4 rows filled with current-state and    | C-11, C-17                 |
|       |                   |                                               | adoption cost per row); budget strength declared; IA verdict issued  |                            |
|       |                   |                                               | in cost terms                                                        |                            |
| C     | Technical Reviews | Phase B exit met; roles read the Phase B cost | All role sections complete; each section names a specific Phase B    | C-02, C-05, C-07, C-14,   |
|       |                   | ledger before writing                         | cost row in its IA anchor; every finding passed the domain-lens gate | C-15, C-18                 |
|       |                   |                                               | (binary test + rewrite consequence)                                  |                            |
| D     | Synthesis         | Phase C exit met                              | Consensus complete; Divergence Mechanism lines free of               | C-03, C-09, C-12, C-13    |
|       |                   |                                               | perspective-label phrases                                            |                            |
| E     | Decision          | Phase D exit met                              | Exactly one GO / NO-GO / GO WITH CONDITIONS issued with              | C-04, C-10                 |
|       |                   |                                               | justification and sign-off roles for any conditions                  |                            |
```

**Phase B exit requires filled cost ledger cells** — a Phase B section with missing cost
cells does not satisfy its exit condition. **Phase C exit requires the domain-lens gate** —
no finding advances to Phase D without passing the binary test + rewrite consequence.

---

**PHASE A — ROUTE**

Entry condition: `org.yaml`, PR diff, and `.roles/` loaded.

```
## Phase A: Routing

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern from org.yaml] |
| (all files) | default | Inertia Advocate | default — always included |
```

Coverage gap: if any file matches no org.yaml scope pattern, append:
`COVERAGE GAP: [file] — no org.yaml scope pattern covers this path.`

Phase A exit: routing table complete; every file has a row; every role cites a scope
pattern.

---

**PHASE B — INERTIA REVIEW**

Entry condition: Phase A exit met.

The IA is the status-quo budget authority. Phase B's exit condition requires all four cost
ledger rows to be filled. A section that lists concerns without cost terms fails the Phase B
exit condition regardless of finding quality.

```
## Phase B: Inertia Advocate

Null hypothesis: The codebase currently [does X via mechanism Y].

Cost ledger (Phase B exit requires all rows filled):
| Cost Category    | Current-State Cost                                      | Adoption Cost (this PR)                         | Net delta |
|---|---|---|---|
| Maintenance      | [LOW/MED/HIGH — what it costs to keep current approach] | [cost of owning new code path long-term]        | [+/-]     |
| Incident exposure| [current failure frequency/severity in this area]      | [residual exposure if PR merges]                | [+/-]     |
| Integration cost | [coordination overhead to keep current approach]       | [churn, downstream wiring, test fixture burden] | [+/-]     |
| Regression risk  | [risk from current approach as-is]                     | [risk of regressions introduced by this PR]     | [+/-]     |

Budget verdict: [one sentence — does total adoption cost exceed total current-state cost?]
Budget strength: HIGH / MEDIUM / LOW

Findings:
F-01 [P1/P2/P3] [specific argument current state is sufficient — names existing mechanism
     or path]
     Owner: [role] | Resolution: [what must change for this finding to close]
F-02 [P1/P2/P3] [second argument grounded in the cost ledger]
     Owner: [role] | Resolution: [concrete action]
[minimum 2 findings]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence in cost terms]
```

Phase B exit: null hypothesis stated; all 4 cost ledger rows filled; budget strength
declared; IA verdict issued.

---

**PHASE C — TECHNICAL REVIEWS**

Entry condition: Phase B exit met. Technical roles read the Phase B cost ledger before
writing. Phase C exit condition: every finding passed the domain-lens gate; each role
section names a specific Phase B cost ledger row in its IA anchor.

Sequence: security/compliance → domain-specific → PM/TPM.

**Domain-lens gate (Phase C exit condition — all findings must pass before Phase D):**

```
Step A — Binary test: "Would only [this role] raise this finding, given their domain?"
  YES → domain-loaded. Include the finding.
  NO  → any generic reviewer could write this. Go to Step B.

Step B — Rewrite consequence: revise to name a specific mechanism, path, function, or
  contract owned by this role's domain — unreachable without it. Re-execute Step A.
  Still NO → drop the finding.
```

Per-role template:

```
## Phase C: [Role Name]

Source files:   [files from Phase A routing that triggered this role]
Orientation:    [one phrase from .roles/]

IA cost anchor (required — cite a specific Phase B ledger row):
  Phase B budget strength:       [HIGH / MEDIUM / LOW]
  Phase B cost row cited:        [Maintenance / Incident exposure / Integration cost /
                                  Regression risk]
  Phase B estimate for that row: [current-state cost and adoption cost, as IA stated]
  This role [confirms / disputes] that estimate because:
    [names the code surface, function, or mechanism — not role perspective or priority.
     Example: "IA rated Integration cost MED; compiler-lead disputes this: the new
     codegen emission at compiler/emit.ts:214 requires rewriting 3 test fixtures not
     counted in the IA's coordination estimate."]

Findings: [all passed the domain-lens gate]
F-01 [P1/P2/P3] [domain-specific finding — mechanism within this role's scope]
     Owner: [role] | Resolution: [concrete action — what and where]
F-02 [P1/P2/P3] [second finding]
     Owner: [role] | Resolution: [action]
[minimum 2; more if warranted]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

Phase C exit: all role sections complete; every section names a Phase B cost row; every
finding passed Step A of the domain-lens gate.

---

**PHASE D — SYNTHESIS**

Entry condition: Phase C exit met.

```
## Phase D: Consensus

IA cost ledger: Budget strength was [HIGH / MEDIUM / LOW].
  Technical roles collectively [reinforced / challenged / defeated] the IA's cost estimate.
  Net: [one sentence — does the benefit case exceed the cost budget?]

Agreement: [area] — [role-A] and [role-B] independently raised [concern]

Divergence: [role-A] rates [area] P[N]; [role-B] rates P[N].
  Mechanism: [structural or architectural property of the code causing the difference]

Critical: [F-XX from role] — [why this finding most threatens the merge]
```

**Perspective-label ban-to-fix — apply before writing any Mechanism line:**

| Banned (do not write) | Required replacement form |
|---|---|
| "they have different perspectives" | "[role-A] sees [code mechanism X]; [role-B] sees [code mechanism Y] — different code surfaces" |
| "they prioritize differently" | "[path X] is inside [role-A]'s domain and outside [role-B]'s — different parts of the affected stack" |
| "they see this through different lenses" | "the change affects [mechanism A] (in [role-A]'s domain) and [mechanism B] (in [role-B]'s domain) at [locations]" |
| "from [role]'s perspective" as sole cause | name the architectural fact causing risk — not the role attribute |
| "their roles lead them to different conclusions" | "[role-A]'s scope includes [code surface X] where the PR changes [Y]; [role-B]'s scope does not include X" |

A Mechanism line containing a banned phrase fails even if a code mechanism is also named.

Phase D exit: agreement/divergence/critical addressed; no banned phrases in any Mechanism
line.

---

**PHASE E — DECISION**

Entry condition: Phase D exit met.

```
## Phase E: Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from [role]] — [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] — sign-off: [role who confirms before merge]
2. [additional condition if present] — sign-off: [role]
```

One decision. Delegated decisions fail. Hedged decisions fail.

Phase E exit: exactly one decision stated with value, justification, and sign-off roles if
conditions apply.

---

**AMEND**

When invoked with an AMEND directive, output this named-field block before PHASE A.
Every field is mandatory; write "none" if not applicable.

```
## AMEND SCOPE

What was amended:           [description — e.g., "added security-architect reviewer",
                            "scoped to auth/ changes only"]
Roles added:                [comma-separated list, or "none"]
Roles removed:              [comma-separated list, or "none"]
Files triggering addition:  [comma-separated list of PR diff files causing the addition, or
                            "n/a — scope change was manually directed"]
Prior findings superseded:  [comma-separated F-IDs from prior run, or "none — first run"]
```

Run PHASES A–E with the amended scope.

---

## V-05 — Combined: IA Cost Ledger + Two-Pass Audit + Ban-to-Fix

**Axes**: Inertia framing + Role sequence + Phrasing register
**Hypothesis**: Three mechanisms, each enforcing a different criterion at a different phase:
the IA cost ledger (C-17) structures Phase B output as arithmetic that technical roles must
dispute with code evidence; the two-pass finding generation (C-18) structures Phase C as a
draft-then-audit sequence where the audit log is the explicit Phase C exit gate; and the
ban-to-fix substitution table (C-13) structures Phase D by pairing each banned phrase with
a required replacement form. The three are additive: cost ledger enforces IA depth, audit
log enforces Phase C exit, substitution table enforces Phase D depth. A run that satisfies
all three produces correct output that is also auditable at each phase transition.

---

You are running `/corps-pr`. Follow each numbered step exactly. Fill every named field and
template slot. A missing field or incomplete audit log is a structural failure regardless
of prose quality.

---

**1. READ INPUTS**

Read: `org.yaml`, PR diff, `.roles/`.

---

**2. BUILD THE ROUTING TABLE**

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

**3. INERTIA ADVOCATE SECTION**

Fill the cost ledger. Every row is mandatory. This block appears before all technical
role sections and before the two-pass finding generation begins.

```
## Inertia Advocate

Null hypothesis:          [what the codebase currently does — one sentence]
Null hypothesis strength: HIGH / MEDIUM / LOW

Cost ledger (all rows required — Phase B exit condition):
| Cost Category    | Current-State Cost                                | Adoption Cost (this PR)                        | Net delta |
|---|---|---|---|
| Maintenance      | [LOW/MED/HIGH — keeping current approach]         | [owning this new code path]                    | [+/-]     |
| Incident exposure| [failure risk/frequency under status quo]         | [residual exposure if PR merges]               | [+/-]     |
| Integration cost | [coordination overhead of current approach]       | [churn, downstream wiring, test burden]        | [+/-]     |
| Regression risk  | [risk from current approach as-is]                | [risk of new failures from this PR]            | [+/-]     |

Budget verdict:  [net: does adoption cost exceed current-state cost?]
Budget strength: HIGH / MEDIUM / LOW

Findings:
| ID   | Finding                                                              | Severity | Owner  | Resolution              |
|------|----------------------------------------------------------------------|----------|--------|-------------------------|
| F-01 | [argument current state is sufficient — names existing mechanism]    | P1/P2/P3 | [role] | [concrete action]       |
| F-02 | [second argument grounded in cost ledger]                            | P1/P2/P3 | [role] | [concrete action]       |

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence in cost terms]
```

---

**4. TECHNICAL ROLE FINDINGS — TWO-PASS GENERATION**

For each role in the routing table, run sub-steps 4A → 4B → 4C in sequence.
Sequence across roles: security/compliance → domain-specific → PM/TPM.

**4A — Draft pass: write all finding candidates without filtering.**

Write every plausible finding candidate for this role. Label each D-01, D-02, ... Do not
apply the domain-lens test in this pass. Write the IA cost anchor first.

IA cost anchor (draft — one block per role before the drafts):

```
IA budget strength:              [HIGH / MEDIUM / LOW]
Cost category bearing on role:   [Maintenance / Incident exposure / Integration cost /
                                  Regression risk]
IA estimate for that category:   [brief restatement from ledger]
Initial role position:           [confirms / disputes — one phrase]
```

Draft findings:

```
D-01: [finding candidate — write exactly, without filtering]
D-02: [second candidate]
[all candidates]
```

**4B — Audit pass: domain-lens gate on all drafts.**

```
AUDIT TEST (per draft): "Would only [this role] raise this finding, given their domain?"
```

- YES → assign next F-ID. Mark in audit log as "→ F-0N".
- NO  → rewrite: name a specific mechanism, path, function, or contract owned by this
  role's domain — something unreachable without it. Re-apply test.
  - Rewrite YES → assign F-ID. Mark as "→ F-0N (revised)".
  - Rewrite NO  → drop. Mark as "→ dropped".

Write the audit log before proceeding to 4C. The audit log is the Phase C exit gate —
an incomplete log means Phase C is not finished.

```
## Audit log — [Role Name]

D-01 → [F-01 | F-01 (revised) | dropped]
D-02 → [F-02 | F-02 (revised) | dropped]
[one line per draft; all drafts accounted for]

Audit result: [N] drafts → [M] findings passed ([x] direct, [y] revised, [z] dropped)
```

The audit tests domain fidelity, not location precision. A finding naming a precise path
passes a location check; it passes the audit only if the observation requires this role's
domain — not if any reviewer could arrive at the same observation at that location.

**4C — Output pass: write the findings section.**

Write only findings that passed 4B. Revise the IA cost anchor to reflect the final role
position after reviewing all findings.

```
## [Role Name]

Source files:   [files that triggered this role]
Orientation:    [one phrase from .roles/]

IA cost anchor:
  IA budget strength:      [HIGH / MEDIUM / LOW]
  Cost category cited:     [Maintenance / Incident exposure / Integration cost /
                            Regression risk]
  IA estimate:             [brief restatement from ledger]
  This role [confirms / disputes] because:
    [code surface, function, or mechanism — not role attribute or perspective]

Findings:
| ID   | Finding                                        | Severity | Domain-Lens | Owner  | Resolution         |
|------|------------------------------------------------|----------|-------------|--------|--------------------|
| F-01 | [finding — passed domain-lens audit in 4B]     | P1/P2/P3 | Passed 4B   | [role] | [concrete action]  |
| F-02 | [second finding — passed audit]                | P1/P2/P3 | Passed 4B   | [role] | [concrete action]  |

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

All role audit logs must be written and complete before proceeding to step 5.

---

**5. CONSENSUS TABLE**

Fill after all per-role sections and audit logs are complete.

```
## Consensus

| Signal     | Finding Area              | Roles                  | Mechanism / Notes                                    |
|------------|---------------------------|------------------------|------------------------------------------------------|
| IA budget  | [cost ledger area]        | Inertia Advocate       | Strength: [HIGH/MEDIUM/LOW] — [how technical roles   |
|            |                           |                        | responded to the cost case]                          |
| Agreement  | [shared concern area]     | [role-A], [role-B]     | [one sentence on shared concern]                     |
| Divergence | [divergent area]          | [role-A (P1)],[role-B] | [structural or architectural code property causing   |
|            |                           | (P3)                   | the rating difference — see ban-to-fix below]        |
| Critical   | [top finding area]        | [role]                 | [why this finding most threatens the merge]          |
```

**Divergence Mechanism ban-to-fix — apply before writing any Divergence Mechanism cell.
Each row is independently checkable:**

| Banned phrase (do not write) | Required replacement form (write this instead) |
|---|---|
| "they have different perspectives" | "[role-A] sees [code mechanism X]; [role-B] sees [code mechanism Y] — different code surfaces affected by the change" |
| "they prioritize differently" | "[path X] is inside [role-A]'s domain scope and outside [role-B]'s — they are assessing different parts of the affected stack" |
| "they see this through different lenses" | "the change modifies [mechanism A] (in [role-A]'s domain) and [mechanism B] (in [role-B]'s domain) through separate paths at [locations]" |
| "from [role]'s perspective" as sole cause | name the code property that makes this role see risk — the architectural fact, not the role attribute |
| "their roles lead them to different conclusions" | "[role-A]'s scope includes [code surface X] where the PR changes [Y]; [role-B]'s scope does not include X — they are reviewing different change surfaces" |

A Mechanism cell containing a banned phrase fails even if a code mechanism is also named
in the same cell. Apply all rows before outputting the consensus table.

---

**6. RECOMMENDATION BLOCK**

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

**7. AMEND SCOPE BLOCK (use only when AMEND directive present)**

When invoked with an AMEND directive, fill and output this named-field block BEFORE step 2.
Every field is mandatory; write "none" if not applicable. Do not convert to prose.

```
## AMEND SCOPE

What was amended:           [description of the change from default routing or scope]
Roles added:                [comma-separated list, or "none"]
Roles removed:              [comma-separated list, or "none"]
Files triggering addition:  [comma-separated list of PR diff files causing a new role to
                            be added, or "n/a — scope change was manually directed"]
Prior findings superseded:  [comma-separated F-IDs from prior run, or "none — first run"]
```

Run steps 2–6 with the amended scope.

Default mode (no AMEND directive): omit step 7 entirely.
