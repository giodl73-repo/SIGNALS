---
skill: quest-variate
skill_target: corps-pr
round: 7
date: 2026-03-16
rubric_version: 7
---

# Variate R7 — corps-pr

5 complete prompt body variations for the `corps-pr` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Axes Selected

| Axis | Used In | R7 Focus |
|------|---------|----------|
| Inertia framing (C-21 Budget verdict derivation formula — 3-clause structure: WORSE rows named, BETTER rows named, Conclusion sentence) | V-01, V-04, V-05 | C-21: verdict is a traceable derivation from row evidence, not a standalone assertion |
| Lifecycle emphasis (C-22 symmetric dual-clause Phase C entry — C1 pre-flight and C2 per-role each produce a named output block with an explicit PASS/BLOCK result line) | V-02, V-04, V-05 | C-22: each sub-condition independently auditable via its own output block |
| Role sequence (C-23 pre-commitment initial position — READ RECEIPT is written before re-reading PR diff; initial position is a pre-commitment signal; IA cost anchor shows whether position changed and why) | V-03, V-05 | C-23: receipt is a genuine before-signal, not a post-hoc rationalization |
| Output format (C-24 universal Domain-Lens column — ALL findings tables, including IA, use the same named-field schema with Domain-Lens column; IA findings use gate label "IA-gate" instead of "Passed") | V-05 | C-24: output is uniformly auditable; Domain-Lens column present in every findings table |

**What changed from R6:**
- R6 V-01 introduced the Net direction column and required Budget verdict to be "derived from row directions." R7 V-01 tightens it: the Budget verdict must follow a 3-clause formula that names the WORSE rows and the BETTER rows explicitly before drawing a conclusion. A one-sentence verdict that reaches a correct conclusion but does not name the rows fails C-21 — the row-naming structure is the derivation signal.
- R6 V-02 introduced C1/C2 as two named sub-conditions. R7 V-02 tightens it: both sub-conditions produce a named output block with an explicit result line. C1 produces a pre-flight block ending with `C1 RESULT: ALL CHECKED — Phase C may begin` or `C1 RESULT: BLOCKED — [missing condition]`. C2 produces a compliance block per role ending with `C2 RESULT: SATISFIED` or `C2 RESULT: UNSATISFIED — [gap]`. The symmetric structure means non-compliance is a visible output gap for both sub-conditions, not only for C1.
- R6 V-03 introduced the IA READ RECEIPT with 5 fields. R7 V-03 tightens the 5th field (initial position): the receipt is written before the PR diff is re-read for findings, making the initial position a genuine pre-commitment signal. The IA cost anchor, written after findings, must state whether the initial position changed and name the code artifact that caused the change (or confirm the position held and name the artifact that supported it).
- R7 V-04 combines V-01 and V-02: the 3-clause Budget verdict formula feeds directly into C1's checklist (B3 is verified as "three-clause verdict") and C2's per-role compliance block (role cites the WORSE/BETTER rows from the Budget verdict, making the Net direction citation derivable from the verdict structure itself).
- R7 V-05 combines all four R7 criteria: C-21 derivation formula + C-22 symmetric dual-clause + C-23 pre-commitment receipt + C-24 universal Domain-Lens table. Tests whether all four mechanisms integrate without added complexity.

---

## V-01 — Inertia Framing: C-21 Budget Verdict Derivation Formula

**Axis**: Inertia framing
**Hypothesis**: R6 V-01 required Budget verdict to be "derived from row directions." The gap:
"derived from" is enforceable only by reading the prose and checking consistency against the
table — there is no structural marker in the verdict text that names the rows. A verdict
can reach a correct directional conclusion while leaving the row evidence implicit. R7 V-01
enforces a 3-clause formula: Clause 1 names all WORSE rows from the Net column. Clause 2
names all BETTER rows. Clause 3 states the net conclusion. If no rows are WORSE, Clause 1
reads "WORSE rows: none." A verdict that jumps to a conclusion without the row-naming clauses
satisfies C-17 and C-19 but fails C-21 — the 3-clause structure is the derivation evidence
checkable by row-name string match, not by prose interpretation.

---

You are running `/corps-pr`. Route this PR through the org and produce a structured
pre-merge review. Read all inputs before any output begins.

**INPUTS**

- `org.yaml` — role scope patterns and committee definitions
- PR diff — every changed file and the nature of each change
- `.craft/roles/` — domain lens and orientation for each role

---

**STEP 1 — ROUTING TABLE**

Map every changed file to an org.yaml role. Output the routing table before any review
begins. Do not begin reviews until the table is complete.

```
## Routing Table

| File / File Group | Change Type | Role Selected | org.yaml Scope Pattern Matched |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern text from org.yaml] |
| (all files) | default | Inertia Advocate | default — always included |
```

Rules:
- Every changed file appears in at least one row. No file is silently dropped.
- Every role cites the exact org.yaml scope pattern matched — do not paraphrase or infer.
- Coverage gap: if any file matches no org.yaml scope pattern, append immediately after
  the table:

```
COVERAGE GAP
File:    [path]
Reason:  No org.yaml scope pattern matches this path.
```

---

**STEP 2 — INERTIA ADVOCATE (always first)**

The IA section appears before all technical role sections. This is structural and
non-configurable. Technical roles read the IA section before writing their own findings.

The IA is the status-quo budget authority. Fill every cell in the cost ledger with a
magnitude label (LOW / MED / HIGH / CRITICAL) and a one-sentence explanation. Each row
also requires a Net direction: WORSE means this PR makes this cost category worse compared
to the status quo; BETTER means the PR reduces this cost; NEUTRAL means no material change.

After the cost table, declare the two terminal fields and the 3-clause Budget verdict
below a separator. The verdict must name the WORSE rows and BETTER rows by their Category
name before stating a conclusion — this is the derivation structure, not a prose summary.

```
## Inertia Advocate

Null hypothesis: The codebase currently [does X via mechanism Y].

Cost ledger:

| Cost Category     | Current-State Cost                                        | Adoption Cost (this PR)                               | Net       |
|-------------------|-----------------------------------------------------------|-------------------------------------------------------|-----------|
| Maintenance       | [LOW/MED/HIGH/CRITICAL — burden to maintain current path] | [burden to maintain new code path post-merge]         | WORSE / BETTER / NEUTRAL |
| Incident exposure | [failure risk/severity under current approach]            | [residual exposure if this PR merges]                 | WORSE / BETTER / NEUTRAL |
| Integration cost  | [coordination overhead of current approach]               | [churn, downstream wiring, test fixture burden]       | WORSE / BETTER / NEUTRAL |
| Regression risk   | [risk of new failures from current approach as-is]        | [risk of new failures introduced by this PR]          | WORSE / BETTER / NEUTRAL |

---
Budget verdict:
  WORSE rows:  [names of Cost Categories where Net = WORSE, or "none"]
  BETTER rows: [names of Cost Categories where Net = BETTER, or "none"]
  Conclusion:  [one sentence — is adoption justified given the balance of WORSE and BETTER?]

Budget strength: HIGH / MEDIUM / LOW
  HIGH   — adoption cost clearly exceeds benefit; status quo is the credible position
  MEDIUM — tradeoff is genuine; this PR must demonstrate benefit exceeds switching cost
  LOW    — adoption cost is justified; the status quo case is weak

Findings:
F-01 [P1/P2/P3] [specific argument current state is sufficient — names existing mechanism,
     path, or function; references at least one Net row direction from the ledger]
     Owner: [role] | Resolution: [what must change for this finding to close]
F-02 [P1/P2/P3] [second argument grounded in a specific cost row]
     Owner: [role] | Resolution: [concrete action]
[minimum 2 findings]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence in cost terms, citing the Budget verdict]
```

The 3-clause Budget verdict is non-negotiable: "WORSE rows:" and "BETTER rows:" must appear
as named lines naming the rows by their Category names. A verdict that reaches a correct
directional conclusion without the named-row lines fails C-21 regardless of prose quality.

---

**STEP 3 — TECHNICAL ROLE REVIEWS**

Technical roles read the IA section before writing their own findings. Each role's IA cost
anchor must reference the Budget verdict's named rows and at least one specific ledger row
to demonstrate the read.

Sequence: security/compliance → domain-specific → PM/TPM.

For each finding in every technical role section, execute the domain-lens gate before writing:

```
DOMAIN-LENS GATE (per finding):

Step A — Binary test:
  "Would only [this role] raise this finding, given their domain?"
  YES → domain-loaded. Write it.
  NO  → any generic reviewer could write this. Go to Step B.

Step B — Rewrite consequence:
  Revise the finding to name a specific mechanism, path, function, or contract that
  belongs to this role's domain and is unreachable without it. Re-execute Step A.
  Still NO after revision → drop the finding.
```

The gate tests domain fidelity, not location precision. Naming a file and line does not
substitute for passing Step A.

Per-role section template:

```
## Review: [Role Name]

Source files:   [files from routing table that triggered this role]
Orientation:    [one phrase from .craft/roles/ describing this role's domain]

IA cost anchor (demonstrates Step 2 read — cite a specific ledger row and the Budget verdict):
  Budget verdict (WORSE rows):  [restate WORSE rows named in the Budget verdict]
  Budget verdict (BETTER rows): [restate BETTER rows named in the Budget verdict]
  Budget strength:               [HIGH / MEDIUM / LOW — from IA terminal field]
  Ledger row cited:              [Maintenance / Incident exposure / Integration cost / Regression risk]
  Net direction for that row:    [WORSE / BETTER / NEUTRAL — from the IA's ledger]
  This role [confirms / disputes] that Net direction because:
    [names the specific code surface, function, or architectural mechanism — not role
     perspective or priority. Must name a code artifact the IA's estimate did or did
     not account for.]

Findings: [all passed domain-lens gate Steps A and B]
F-01 [P1/P2/P3] [domain-specific finding — names the mechanism within this role's domain]
     Owner: [role] | Resolution: [concrete action naming what to do and where]
F-02 [P1/P2/P3] [second finding]
     Owner: [role] | Resolution: [action]
[minimum 2 findings]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

---

**STEP 4 — CONSENSUS SYNTHESIS**

After all per-role sections are complete:

```
## Consensus

IA cost ledger: Budget strength was [HIGH / MEDIUM / LOW].
  WORSE rows were: [list]. BETTER rows were: [list].
  Technical roles collectively [reinforced / challenged / defeated] the IA's cost estimate.
  Net: [one sentence — does the benefit case exceed the cost budget?]

Agreement: [area] — [role-A] and [role-B] independently raised [concern]

Divergence: [role-A] rates [concern] P[N]; [role-B] rates it P[N].
  Mechanism: [the specific code or architectural property causing the rating difference —
             names a structural fact in the code, not a perspective difference]

Critical: [F-XX from role] — [one sentence on why this finding most threatens the merge]
```

Perspective-label ban — scan every Mechanism line against all five phrases before writing:

- `[ ]` "they have different perspectives" — BANNED
- `[ ]` "they prioritize differently" — BANNED
- `[ ]` "they see this through different lenses" — BANNED
- `[ ]` "their roles lead them to different conclusions" — BANNED
- `[ ]` "from [role]'s perspective" as the sole cause of divergence — BANNED

Replace any banned phrase with the architectural mechanism. A Mechanism line containing
a banned phrase fails even if a code mechanism is also named in the same sentence.

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
Delegated decisions fail. Hedged decisions fail.

---

**AMEND**

When invoked with an AMEND directive, output this named-field block BEFORE STEP 1.
All fields are mandatory; write "none" if not applicable. Do not convert to prose.

```
## AMEND SCOPE

What was amended:           [describe the change from default routing]
Roles added:                [comma-separated list, or "none"]
Roles removed:              [comma-separated list, or "none"]
Files triggering addition:  [comma-separated list of PR diff files that caused a new role,
                            or "n/a — scope change was manually directed"]
Prior findings superseded:  [comma-separated F-IDs from any prior run that are voided,
                            or "none — first run"]
```

Run STEPS 1–5 with the amended scope.

---

## V-02 — Lifecycle Emphasis: C-22 Symmetric Dual-Clause with Named Output Blocks

**Axis**: Lifecycle emphasis
**Hypothesis**: R6 V-02 established C1 and C2 as two named sub-conditions. The asymmetry:
C1 failure produces an explicit output consequence ("Phase C cannot begin — return to Phase B"),
but C2 failure is described as locatable to a specific role without a named output block. A
reviewer checking C2 compliance must read each role section to find whether the anchor is
present — there is no structural gap signal in the output. R7 V-02 adds symmetric output
blocks: C1 produces a PRE-FLIGHT RESULT block ending with `C1: ALL CLEAR` or `C1: BLOCKED`;
C2 produces a COMPLIANCE RESULT block per role ending with `C2: SATISFIED` or `C2: UNSATISFIED
— [named gap]`. The symmetry means both sub-conditions produce verifiable output artifacts,
and non-compliance for either is detectable by scanning for a BLOCKED or UNSATISFIED line
without reading the prose of each section.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline. The pipeline
declaration below is the execution contract. Read every entry before producing any output.
No phase may begin until its stated entry conditions are satisfied.

---

**PIPELINE DECLARATION**

```
Phase A — Route
  Entry:    org.yaml + PR diff + .craft/roles/ loaded
  Exit:     Routing table complete; every changed file has a row; every role cites an
            exact org.yaml scope pattern; coverage gaps declared if any
  Gates:    C-01, C-06

Phase B — Inertia Review
  Entry:    Phase A exit met
  Exit:     (B1) Null hypothesis stated
            (B2) Cost ledger filled: 4 named rows, 2 named columns, Net direction per row
            (B3) Budget verdict declared as 3-clause terminal field (WORSE rows named,
                 BETTER rows named, Conclusion stated) below the cost table
            (B4) Budget strength declared as named terminal field below the cost table
            (B5) IA verdict issued in cost terms
            All five conditions must be met for Phase B to exit.
  Gates:    C-11, C-17, C-19, C-21

Phase C — Technical Reviews
  Entry:    Two independently auditable sub-conditions:
            C1 (Phase B exit pre-flight):
              A checklist of all Phase B exit conditions, checked once before Phase C
              begins. Any unchecked item blocks Phase C from starting. C1 compliance is
              demonstrated by a PRE-FLIGHT RESULT block in the output.
            C2 (IA read prerequisite — per-role):
              Each technical role must demonstrate it read Phase B by writing a C2
              COMPLIANCE RESULT block before findings. The block must cite a specific Phase B
              ledger row name and that row's Net direction. A role section missing the
              compliance block fails C2 for that role independently of other roles.
  Exit:     All role sections complete; every role's C2 block is present and SATISFIED;
            every finding passed the domain-lens gate
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-23

Phase D — Synthesis
  Entry:    Phase C exit met
  Exit:     Consensus complete; all Mechanism lines pass the ban-to-fix substitution check
  Gates:    C-03, C-09, C-12, C-13

Phase E — Decision
  Entry:    Phase D exit met
  Exit:     Exactly one GO / NO-GO / GO WITH CONDITIONS issued; conditions name sign-off
            role; decision is not delegated or hedged
  Gates:    C-04, C-10
```

---

**PHASE A — ROUTE**

Entry condition: `org.yaml`, PR diff, and `.craft/roles/` loaded.

```
## Phase A: Routing

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern from org.yaml] |
| (all files) | default | Inertia Advocate | default — always included |
```

Coverage gap: if any file matches no org.yaml scope pattern, append immediately:
`COVERAGE GAP: [file] — no org.yaml scope pattern covers this path.`

Phase A exit: table complete; every file has a row; every role cites a scope pattern.

---

**PHASE B — INERTIA REVIEW**

Entry condition: Phase A exit met.

Phase B has five exit conditions (B1–B5). B3 requires the Budget verdict to be a 3-clause
structure below the separator — not embedded in the table and not a single prose sentence.

```
## Phase B: Inertia Advocate

Null hypothesis: The codebase currently [does X via mechanism Y].           ← B1

Cost ledger (B2 — all 4 rows × 2 columns × Net direction required):

| Cost Category     | Current-State Cost                                        | Adoption Cost (this PR)                          | Net       |
|-------------------|-----------------------------------------------------------|--------------------------------------------------|-----------|
| Maintenance       | [LOW/MED/HIGH — maintaining current path]                 | [maintaining new path post-merge]                | WORSE / BETTER / NEUTRAL |
| Incident exposure | [failure risk/severity under status quo]                  | [residual exposure after merge]                  | WORSE / BETTER / NEUTRAL |
| Integration cost  | [coordination overhead of current approach]               | [churn, downstream wiring, test burden]          | WORSE / BETTER / NEUTRAL |
| Regression risk   | [risk of new failures from current approach as-is]        | [risk introduced by this PR]                     | WORSE / BETTER / NEUTRAL |

---
Budget verdict:                                                              ← B3
  WORSE rows:  [Cost Categories where Net = WORSE, or "none"]
  BETTER rows: [Cost Categories where Net = BETTER, or "none"]
  Conclusion:  [one sentence — is adoption justified given the balance?]

Budget strength: HIGH / MEDIUM / LOW                                        ← B4

Findings:
F-01 [P1/P2/P3] [argument current state is sufficient — names mechanism, path, or function]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second argument grounded in cost ledger]
     Owner: [role] | Resolution: [action]
[minimum 2 findings]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence in cost terms]         ← B5
```

Phase B exit: B1 through B5 all met.

---

**PHASE C — TECHNICAL REVIEWS**

Phase C has two entry conditions: C1 (pre-flight) and C2 (per-role). Each produces a named
output block with an explicit result line. Both must show a passing result before any
technical role findings are written.

**C1 — Phase B Exit Pre-Flight Block:**

Output this block immediately before the first technical role section. It is the C1
compliance artifact — a reviewer verifies C1 by scanning for this block and its result line.

```
## Phase C Pre-Flight (C1)

[ ] B1 — Null hypothesis stated in Phase B
[ ] B2 — Cost ledger: 4 rows × 2 columns × Net direction per row filled
[ ] B3 — Budget verdict: 3-clause structure (WORSE rows, BETTER rows, Conclusion) present
[ ] B4 — Budget strength declared as named terminal field below separator
[ ] B5 — IA verdict issued in cost terms

C1 RESULT: ALL CLEAR — Phase C may begin.
```

If any box is unchecked, the result line reads:
`C1 RESULT: BLOCKED — [B-number] not met. Return to Phase B.`
Phase C cannot begin until C1 RESULT is ALL CLEAR.

**C2 — IA Read Prerequisite (Per-Role):**

Each technical role section begins with a C2 COMPLIANCE block immediately before findings.
This is the per-role C2 artifact. A role section missing the block fails C2 for that role.

```
## C2 Compliance — [Role Name]

Phase B ledger row cited:    [Maintenance / Incident exposure / Integration cost / Regression risk]
Net direction for that row:  [WORSE / BETTER / NEUTRAL — from Phase B table]
Budget strength cited:       [HIGH / MEDIUM / LOW — from Phase B terminal field]

C2 RESULT: SATISFIED — [Role Name] may generate findings.
```

If the role cannot cite a specific Phase B row and Net direction, the result line reads:
`C2 RESULT: UNSATISFIED — ledger row and Net direction not cited. Role section incomplete.`
A role with C2 RESULT: UNSATISFIED cannot advance to findings until the block is completed.

Sequence across roles: security/compliance → domain-specific → PM/TPM.

**Domain-lens gate (Phase C exit condition for all findings):**

```
Step A: "Would only [this role] raise this finding, given their domain?"
  YES → domain-loaded. Include the finding.
  NO  → any generic reviewer could write this. Go to Step B.

Step B: Revise to name a specific mechanism, path, function, or contract owned by this
  role's domain — unreachable without it. Re-execute Step A.
  Still NO → drop the finding.
```

Per-role template (written after C1 block and after this role's C2 block are complete):

```
## Phase C: [Role Name]

Source files:   [files from Phase A routing that triggered this role]
Orientation:    [one phrase from .craft/roles/]

[C2 COMPLIANCE BLOCK — paste completed block from above]

IA cost anchor (demonstrates Phase B read — cite ledger row and Budget verdict):
  Phase B ledger row cited:  [same row as C2 compliance block]
  Net direction:             [WORSE / BETTER / NEUTRAL]
  Budget strength:           [HIGH / MEDIUM / LOW]
  This role [confirms / disputes] that Net direction because:
    [names the code surface, function, or mechanism — not role perspective or priority.
     Must name a code artifact the IA estimate did or did not account for.]

Findings: [all passed domain-lens gate Steps A and B]
F-01 [P1/P2/P3] [domain-specific finding]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second finding]
     Owner: [role] | Resolution: [action]
[minimum 2]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

Phase C exit: C1 PRE-FLIGHT shows ALL CLEAR; every role's C2 block shows SATISFIED;
every finding passed Step A of the domain-lens gate.

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
| "from [role]'s perspective" as sole cause | name the architectural fact causing risk — the code property, not the role attribute |
| "their roles lead them to different conclusions" | "[role-A]'s scope includes [code surface X] where the PR changes [Y]; [role-B]'s scope does not include X" |

A Mechanism line containing a banned phrase fails even if a code mechanism is also named.

Phase D exit: agreement/divergence/critical addressed; no banned phrases in any Mechanism line.

---

**PHASE E — DECISION**

Entry condition: Phase D exit met.

```
## Phase E: Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from [role]] — [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] — sign-off: [role who confirms before merge]
2. [additional condition] — sign-off: [role]
```

One decision. Values: GO, NO-GO, GO WITH CONDITIONS. Delegated decisions fail. Hedged
decisions fail.

Phase E exit: exactly one decision stated with value, justification, and sign-off roles.

---

**AMEND**

When invoked with an AMEND directive, output this named-field block before Phase A. All
fields are mandatory; write "none" if not applicable.

```
## AMEND SCOPE

What was amended:           [description]
Roles added:                [list, or "none"]
Roles removed:              [list, or "none"]
Files triggering addition:  [list, or "n/a — scope change was manually directed"]
Prior findings superseded:  [F-IDs, or "none — first run"]
```

Run Phases A–E with the amended scope.

---

## V-03 — Role Sequence: C-23 Pre-Commitment Initial Position with Post-Findings Delta

**Axis**: Role sequence
**Hypothesis**: C-23 requires the READ RECEIPT to include "the role's initial position on
[the cited cost row]." In R6 V-03, the initial position field says "[confirms / disputes —
one phrase]" but the template does not enforce *when* this position is formed. A role could
write the receipt after reading the PR diff, making the initial position a post-hoc
rationalization rather than a genuine pre-commitment signal. R7 V-03 enforces timing: the
READ RECEIPT (including the initial position) is written immediately after the IA section,
*before* the PR diff is examined for findings. The initial position is pre-commitment —
it is the role's prior based on domain knowledge alone. After findings are generated, the
IA cost anchor states whether the initial position changed (and names the code artifact that
caused the change) or held (and names the artifact that supported it). The before/after
delta is a required output field — a role where the initial position is simply confirmed
without any explanatory code artifact fails the delta requirement.

---

You are running `/corps-pr`. Follow each numbered step exactly. Fill every named field and
template slot. A missing receipt block or absent delta analysis is a structural output
failure regardless of finding quality.

**READ INPUTS**

Read: `org.yaml`, PR diff, `.craft/roles/`.

---

**STEP 1 — ROUTING TABLE**

Output before advancing to step 2. Do not begin any review section until complete.

```
## Routing Table

| File / File Group | Change Type | Role Selected | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern from org.yaml] |
| (all files) | default | Inertia Advocate | default — always included |
```

Every file gets a row. Every role cites its exact org.yaml scope pattern.

Coverage gap — append immediately after the table if any file has no match:

```
COVERAGE GAP
File:    [path]
Reason:  No org.yaml scope pattern matches this path.
```

---

**STEP 2 — INERTIA ADVOCATE SECTION**

The IA section appears first. Fill the cost ledger completely. Budget verdict (3-clause:
WORSE rows, BETTER rows, Conclusion) and Budget strength are terminal declarations below the
separator — do not embed them as additional table rows.

```
## Inertia Advocate

Null hypothesis: The codebase currently [does X via mechanism Y].

Cost ledger:

| Cost Category     | Current-State Cost                                        | Adoption Cost (this PR)                          | Net       |
|-------------------|-----------------------------------------------------------|--------------------------------------------------|-----------|
| Maintenance       | [LOW/MED/HIGH — maintaining current path]                 | [maintaining new path post-merge]                | WORSE / BETTER / NEUTRAL |
| Incident exposure | [failure risk/severity under status quo]                  | [residual exposure after merge]                  | WORSE / BETTER / NEUTRAL |
| Integration cost  | [coordination overhead of current approach]               | [churn, downstream wiring, test burden]          | WORSE / BETTER / NEUTRAL |
| Regression risk   | [risk of new failures from current approach as-is]        | [risk introduced by this PR]                     | WORSE / BETTER / NEUTRAL |

---
Budget verdict:
  WORSE rows:  [Cost Categories where Net = WORSE, or "none"]
  BETTER rows: [Cost Categories where Net = BETTER, or "none"]
  Conclusion:  [one sentence — is adoption justified?]

Budget strength: HIGH / MEDIUM / LOW

Findings:
F-01 [P1/P2/P3] [argument current state is sufficient — names mechanism, path, or function]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second argument]
     Owner: [role] | Resolution: [action]
[minimum 2]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence in cost terms]
```

---

**STEP 3 — TECHNICAL ROLE SECTIONS**

For each role in the routing table, run sub-steps 3A → 3B → 3C in sequence.
Sequence across roles: security/compliance → domain-specific → PM/TPM.

**3A — IA READ RECEIPT (write BEFORE re-reading PR diff for this role)**

The READ RECEIPT is written immediately after reading the IA section and before examining
the PR diff for findings. This is the pre-commitment moment: the role states its initial
position based on domain knowledge and the IA's cost estimate alone — not based on findings
already generated. Writing the receipt after findings are known would produce a rationalized
initial position; the pre-commitment requirement exists to capture the role's genuine prior.

Fill every field. A receipt with placeholder text (e.g., "see Phase 2") or a missing field
fails to demonstrate the read prerequisite.

```
## IA READ RECEIPT — [Role Name]

Section read:              Phase 2 — Inertia Advocate
Budget verdict read:
  WORSE rows:              [restate WORSE rows from Phase 2 Budget verdict]
  BETTER rows:             [restate BETTER rows from Phase 2 Budget verdict]
  Conclusion restated:     [restate Phase 2 Conclusion in one accurate sentence]
Budget strength read:      HIGH / MEDIUM / LOW [from Phase 2 terminal field]
Cost row most relevant     [Maintenance / Incident exposure / Integration cost / Regression risk]
  to this role's domain:
Phase 2 estimate for row:  Current-State: [cell value] | Adoption: [cell value] | Net: [direction]
Initial role position:     [confirms / disputes the IA's Net direction for the cited row]
  Pre-commitment reason:   [one phrase from domain knowledge alone — no finding content yet]
```

This receipt is the pre-commitment artifact. It is timestamped at the moment before
findings are generated. After findings, the IA cost anchor will show whether this
position held or changed.

**3B — GENERATE FINDINGS**

After completing 3A, re-read the PR diff with this role's domain lens. For each finding
candidate, apply the domain-lens gate:

```
DOMAIN-LENS GATE (per finding):

Step A: "Would only [this role] raise this finding, given their domain?"
  YES → domain-loaded. Write it.
  NO  → generic. Go to Step B.

Step B: Revise to name a specific mechanism, path, function, or contract owned by this
  role's domain — unreachable without it. Re-execute Step A.
  Still NO → drop the finding.
```

**3C — OUTPUT SECTION**

Write the section after 3A (receipt) and 3B (gate) are complete. The IA cost anchor in 3C
shows whether the initial position from 3A held or changed in light of findings.

```
## [Role Name]

Source files:   [files that triggered this role]
Orientation:    [one phrase from .craft/roles/]

IA READ RECEIPT:
[paste the completed receipt from 3A here — do not summarize or abbreviate]

IA cost anchor (post-findings position — required delta analysis):
  Phase 2 ledger row:    [same row cited in receipt]
  Net direction:         [WORSE / BETTER / NEUTRAL — from Phase 2]
  Budget strength:       [from Phase 2 terminal field]
  Position after findings:
    [CONFIRMED / REVISED] — [one sentence]
    Artifact: [names the specific code surface, function, or mechanism that confirmed
               or revised the initial position — must name a code artifact from the PR diff;
               "no change" without a named artifact fails this field]

Findings: [only findings that passed Steps A and B]
| ID   | Finding                                      | Severity | Domain-Lens | Owner  | Resolution        |
|------|----------------------------------------------|----------|-------------|--------|-------------------|
| F-01 | [finding — passed gate]                      | P1/P2/P3 | Passed      | [role] | [concrete action] |
| F-02 | [second finding — passed gate]               | P1/P2/P3 | Passed      | [role] | [concrete action] |

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

All role sections (including their receipt blocks and delta analyses) must be complete
before proceeding to step 4.

---

**STEP 4 — CONSENSUS**

After all per-role sections are complete:

```
## Consensus

IA budget: Budget strength was [HIGH / MEDIUM / LOW].
  Technical roles [reinforced / challenged / defeated] the cost estimate.
  [one sentence: does benefit exceed the cost budget?]

Agreement: [area] — [role-A] and [role-B] independently raised [concern]

Divergence: [role-A] P[N] vs [role-B] P[N]
  Mechanism: [structural or architectural code property causing the difference]

Critical: [F-XX from role] — [why this most threatens the merge]
```

Perspective-label ban-to-fix — apply before writing any Mechanism line:

| Banned phrase | Required replacement form |
|---|---|
| "they have different perspectives" | "[role-A] sees [code mechanism X]; [role-B] sees [code mechanism Y] — different code surfaces" |
| "they prioritize differently" | "[path X] is in [role-A]'s domain scope and outside [role-B]'s" |
| "they see this through different lenses" | "the change affects [mechanism A] (owned by [role-A]) and [mechanism B] (owned by [role-B]) at [locations]" |
| "from [role]'s perspective" as sole cause | name the code property causing risk — the fact, not the role attribute |
| "their roles lead them to different conclusions" | "[role-A]'s scope includes [code surface X] where the PR changes [Y]; [role-B]'s does not" |

---

**STEP 5 — DECISION**

```
## Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary reason: [F-XX from [role]] — [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what to resolve] — sign-off: [role]
2. [additional condition] — sign-off: [role]
```

One decision. No delegation. No hedging.

---

**AMEND MODE**

When invoked with an AMEND directive, output this block BEFORE STEP 1. All fields are
mandatory; write "none" if not applicable.

```
## AMEND SCOPE

What was amended:           [description]
Roles added:                [list, or "none"]
Roles removed:              [list, or "none"]
Files triggering addition:  [list, or "n/a — manually directed"]
Prior findings superseded:  [F-IDs, or "none — first run"]
```

Run steps 1–5 with the amended scope.

---

## V-04 — Combined: C-21 Derivation Formula + C-22 Symmetric Dual-Clause

**Axes**: Inertia framing + Lifecycle emphasis
**Hypothesis**: V-01 enforces C-21: Budget verdict is a 3-clause derivation (WORSE rows,
BETTER rows, Conclusion). V-02 enforces C-22: Phase C entry has two symmetric output blocks
(C1 pre-flight with PASS/BLOCK result; C2 per-role compliance with SATISFIED/UNSATISFIED
result). The integration insight: C1's B3 checklist item can now be specifically verified
against the 3-clause structure — B3 is checked if and only if "WORSE rows:", "BETTER rows:",
and "Conclusion:" all appear as named lines in the Budget verdict. C2's per-role compliance
block cites the Budget verdict's WORSE/BETTER row list, not just a raw ledger row, making
the cited evidence derivable from the verdict structure itself. A run that satisfies V-01
and V-02 independently but does not chain them (i.e., C1's B3 check does not name the
3-clause format, and C2 does not cite the verdict's row names) passes both criteria in
isolation but misses the structural integration that makes the pipeline self-verifying.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline. The pipeline
declaration below is the execution contract. Read every entry before producing any output.
No phase may begin until its stated entry conditions are satisfied.

---

**PIPELINE DECLARATION**

```
Phase A — Route
  Entry:    org.yaml + PR diff + .craft/roles/ loaded
  Exit:     Routing table complete; every changed file has a row; every role cites an
            exact org.yaml scope pattern; coverage gaps declared if any
  Gates:    C-01, C-06

Phase B — Inertia Review
  Entry:    Phase A exit met
  Exit:     (B1) Null hypothesis stated
            (B2) Cost ledger: 4 named rows × 2 named columns × Net direction per row filled
            (B3) Budget verdict: 3-clause structure with "WORSE rows:" and "BETTER rows:"
                 and "Conclusion:" as named lines, declared below the cost table separator
            (B4) Budget strength declared as named terminal field below the cost table
            (B5) IA verdict issued in cost terms
  Gates:    C-11, C-17, C-19, C-21

Phase C — Technical Reviews
  Entry:    C1 (Phase B exit pre-flight — verified once, produces a PRE-FLIGHT RESULT block):
              [ ] B1 met — null hypothesis stated
              [ ] B2 met — 4 rows × 2 columns × Net direction filled
              [ ] B3 met — Budget verdict has "WORSE rows:", "BETTER rows:", "Conclusion:"
              [ ] B4 met — Budget strength as named terminal field
              [ ] B5 met — IA verdict issued
              C1 RESULT line must be ALL CLEAR for Phase C to begin.
            C2 (IA read prerequisite — per-role, produces C2 COMPLIANCE RESULT per role):
              Each technical role cites: (a) a named Phase B ledger row, (b) that row's
              Net direction from Phase B, (c) the WORSE/BETTER row lists from the Budget
              verdict. C2 RESULT line per role must be SATISFIED.
  Exit:     C1 PRE-FLIGHT shows ALL CLEAR; every role's C2 shows SATISFIED; every finding
            passed the domain-lens gate
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-23

Phase D — Synthesis
  Entry:    Phase C exit met
  Exit:     Consensus complete; all Mechanism lines pass the ban-to-fix substitution check
  Gates:    C-03, C-09, C-12, C-13

Phase E — Decision
  Entry:    Phase D exit met
  Exit:     Exactly one GO / NO-GO / GO WITH CONDITIONS issued with justification and
            sign-off roles for any conditions
  Gates:    C-04, C-10
```

---

**PHASE A — ROUTE**

Entry condition: `org.yaml`, PR diff, and `.craft/roles/` loaded.

```
## Phase A: Routing

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern from org.yaml] |
| (all files) | default | Inertia Advocate | default — always included |
```

Coverage gap: append immediately after table if any file has no org.yaml match:
`COVERAGE GAP: [file] — no org.yaml scope pattern covers this path.`

Phase A exit: table complete; every file has a row; every role cites a scope pattern.

---

**PHASE B — INERTIA REVIEW**

Entry condition: Phase A exit met.

Phase B has five exit conditions. B3 requires Budget verdict to be a 3-clause structure
below the cost table — "WORSE rows:", "BETTER rows:", and "Conclusion:" as named lines.
A single-sentence verdict satisfies C-17 but fails B3 and therefore blocks Phase C C1.

```
## Phase B: Inertia Advocate

Null hypothesis: The codebase currently [does X via mechanism Y].           ← B1

Cost ledger (B2 — all rows, columns, Net directions required):

| Cost Category     | Current-State Cost                                        | Adoption Cost (this PR)                          | Net       |
|-------------------|-----------------------------------------------------------|--------------------------------------------------|-----------|
| Maintenance       | [LOW/MED/HIGH — maintaining current path]                 | [maintaining new path post-merge]                | WORSE / BETTER / NEUTRAL |
| Incident exposure | [failure risk/severity under status quo]                  | [residual exposure after merge]                  | WORSE / BETTER / NEUTRAL |
| Integration cost  | [coordination overhead of current approach]               | [churn, downstream wiring, test burden]          | WORSE / BETTER / NEUTRAL |
| Regression risk   | [risk of new failures from current approach as-is]        | [risk introduced by this PR]                     | WORSE / BETTER / NEUTRAL |

---
Budget verdict:                                                              ← B3
  WORSE rows:  [Cost Categories where Net = WORSE, or "none"]
  BETTER rows: [Cost Categories where Net = BETTER, or "none"]
  Conclusion:  [one sentence — is adoption justified given the WORSE/BETTER balance?]

Budget strength: HIGH / MEDIUM / LOW                                        ← B4

Findings:
F-01 [P1/P2/P3] [argument current state is sufficient — names mechanism, path, or function]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second argument]
     Owner: [role] | Resolution: [action]
[minimum 2]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence in cost terms]         ← B5
```

Phase B exit: B1–B5 all met.

---

**PHASE C — TECHNICAL REVIEWS**

Phase C has two entry conditions. Each produces a named output block.

**C1 — Pre-Flight Block (output before first technical role section):**

```
## Phase C Pre-Flight (C1)

[ ] B1 — Null hypothesis stated in Phase B
[ ] B2 — Cost ledger: 4 rows × 2 columns × Net direction per row filled
[ ] B3 — Budget verdict: "WORSE rows:", "BETTER rows:", "Conclusion:" lines present
[ ] B4 — Budget strength declared as named terminal field (below separator)
[ ] B5 — IA verdict issued in cost terms

C1 RESULT: ALL CLEAR — Phase C may begin.
```

If any box is unchecked: `C1 RESULT: BLOCKED — [B-number] not met. Return to Phase B.`

**C2 — Per-Role Compliance Block (output before each role's findings):**

```
## C2 Compliance — [Role Name]

Phase B ledger row cited:    [Maintenance / Incident exposure / Integration cost / Regression risk]
Net direction for that row:  [WORSE / BETTER / NEUTRAL — exact value from Phase B ledger]
Budget verdict WORSE rows:   [restate Phase B Budget verdict "WORSE rows:" line]
Budget verdict BETTER rows:  [restate Phase B Budget verdict "BETTER rows:" line]
Budget strength cited:       [HIGH / MEDIUM / LOW — from Phase B terminal field]

C2 RESULT: SATISFIED — [Role Name] may generate findings.
```

If ledger row + Net direction + verdict row lists not all cited:
`C2 RESULT: UNSATISFIED — [named gap]. Role section incomplete until resolved.`

Sequence: security/compliance → domain-specific → PM/TPM.

**Domain-lens gate (Phase C exit condition):**

```
Step A: "Would only [this role] raise this finding, given their domain?"
  YES → include.
  NO  → Go to Step B.

Step B: Revise to name a specific mechanism, path, function, or contract owned by this
  role's domain — unreachable without it. Re-execute Step A.
  Still NO → drop.
```

Per-role template (written after C2 COMPLIANCE block for this role):

```
## Phase C: [Role Name]

Source files:   [files from Phase A routing that triggered this role]
Orientation:    [one phrase from .craft/roles/]

[C2 COMPLIANCE BLOCK — paste completed block above]

IA cost anchor (post-C2 position — confirms or disputes Phase B Net direction):
  Phase B ledger row:    [same row cited in C2 compliance block]
  Net direction:         [WORSE / BETTER / NEUTRAL — from Phase B ledger, this row]
  Budget strength:       [HIGH / MEDIUM / LOW — from Phase B terminal field]
  This role [confirms / disputes] that Net direction because:
    [names the specific code artifact — function, path, mechanism — the IA estimate
     did or did not account for; grounded in PR diff content]

Findings: [all passed domain-lens gate]
F-01 [P1/P2/P3] [domain-specific finding]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second finding]
     Owner: [role] | Resolution: [action]
[minimum 2]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

Phase C exit: C1 ALL CLEAR; every role C2 SATISFIED; every finding passed domain-lens gate.

---

**PHASE D — SYNTHESIS**

Entry condition: Phase C exit met.

```
## Phase D: Consensus

IA cost ledger: Budget strength was [HIGH / MEDIUM / LOW].
  WORSE rows were: [list from Phase B verdict]. BETTER rows were: [list].
  Technical roles collectively [reinforced / challenged / defeated] the IA's cost estimate.
  Net: [one sentence]

Agreement: [area] — [role-A] and [role-B] independently raised [concern]

Divergence: [role-A] rates [area] P[N]; [role-B] rates P[N].
  Mechanism: [structural or architectural property of the code causing the difference]

Critical: [F-XX from role] — [why this finding most threatens the merge]
```

**Perspective-label ban-to-fix — apply before writing any Mechanism line:**

| Banned (do not write) | Required replacement form |
|---|---|
| "they have different perspectives" | "[role-A] sees [code mechanism X]; [role-B] sees [code mechanism Y] — different code surfaces" |
| "they prioritize differently" | "[path X] is inside [role-A]'s domain and outside [role-B]'s — different affected stack segments" |
| "they see this through different lenses" | "the change affects [mechanism A] (in [role-A]'s domain) and [mechanism B] (in [role-B]'s domain) at [locations]" |
| "from [role]'s perspective" as sole cause | name the architectural fact — the code property, not the role attribute |
| "their roles lead them to different conclusions" | "[role-A]'s scope includes [code surface X] where the PR changes [Y]; [role-B]'s scope does not include X" |

Phase D exit: agreement/divergence/critical addressed; no banned phrases in any Mechanism line.

---

**PHASE E — DECISION**

Entry condition: Phase D exit met.

```
## Phase E: Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from [role]] — [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] — sign-off: [role who confirms before merge]
2. [additional condition] — sign-off: [role]
```

One decision. Delegated decisions fail. Hedged decisions fail.

Phase E exit: exactly one decision with value, justification, and sign-off roles.

---

**AMEND**

When invoked with an AMEND directive, output this named-field block before Phase A. All
fields are mandatory; write "none" if not applicable.

```
## AMEND SCOPE

What was amended:           [description]
Roles added:                [list, or "none"]
Roles removed:              [list, or "none"]
Files triggering addition:  [list, or "n/a — scope change was manually directed"]
Prior findings superseded:  [F-IDs, or "none — first run"]
```

Run Phases A–E with the amended scope.

---

## V-05 — Combined: C-21 + C-22 + C-23 + C-24 Full Integration

**Axes**: Inertia framing + Lifecycle emphasis + Role sequence + Output format
**Hypothesis**: V-01 enforces C-21 (Budget verdict derivation formula). V-02 enforces C-22
(symmetric dual-clause C1/C2 with output result blocks). V-03 enforces C-23 (pre-commitment
READ RECEIPT with post-findings delta). All three prior variations leave findings in prose or
numbered list format. V-05 adds C-24 universalization: ALL findings tables (IA + all technical
roles) use the same named-field schema with Domain-Lens column. For IA findings, the column
shows "IA-gate" (does this finding require the IA's budget authority position to raise it?
A generic reviewer without cost authority could not frame a finding as a budget position).
The integration chain: Phase B Budget verdict (3-clause) → C1 checklist verifies B3 clause
structure → Phase C C2 compliance cites WORSE/BETTER rows from verdict → READ RECEIPT restates
verdict clauses → post-findings delta names the code artifact → findings table has Domain-Lens
column per finding. A run that passes all four R7 criteria produces output where every output
block is independently auditable against a named criterion without reconstructing the pipeline
from a declaration.

---

You are running `/corps-pr`. Follow each step exactly. Fill every named field and template
slot. A missing output block, empty table column, or absent result line is a structural
failure — prose quality does not compensate for a structural gap.

**READ INPUTS**

Read: `org.yaml`, PR diff, `.craft/roles/`.

---

**STEP 1 — ROUTING TABLE**

Output before advancing. Do not begin any review section until complete.

```
## Routing Table

| File / File Group | Change Type | Role Selected | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern from org.yaml] |
| (all files) | default | Inertia Advocate | default — always included |
```

Every file gets a row. Every role cites its exact org.yaml scope pattern (literal text, not
inferred). Coverage gap — append if any file has no match:

```
COVERAGE GAP
File:    [path]
Reason:  No org.yaml scope pattern matches this path.
```

---

**STEP 2 — INERTIA ADVOCATE SECTION**

The IA section appears before all technical role sections. Fill the cost ledger. Budget
verdict (3-clause) and Budget strength are terminal fields below the separator — do not
embed them as table rows. IA findings use the universal findings table schema with an
IA-gate column (not Domain-Lens — the IA has no domain-lens gate).

```
## Inertia Advocate

Null hypothesis:
  The codebase currently [does X via mechanism Y].

Cost ledger (all rows, columns, and Net directions required):

| Cost Category     | Current-State Cost                                        | Adoption Cost (this PR)                          | Net       |
|-------------------|-----------------------------------------------------------|--------------------------------------------------|-----------|
| Maintenance       | [LOW/MED/HIGH — burden of maintaining current path]       | [burden of maintaining new path post-merge]      | WORSE / BETTER / NEUTRAL |
| Incident exposure | [failure risk/severity under status quo]                  | [residual exposure after merge]                  | WORSE / BETTER / NEUTRAL |
| Integration cost  | [coordination overhead of current approach]               | [churn, downstream wiring, test burden]          | WORSE / BETTER / NEUTRAL |
| Regression risk   | [risk of new failures from current approach as-is]        | [risk introduced by this PR]                     | WORSE / BETTER / NEUTRAL |

---
Budget verdict:
  WORSE rows:  [Cost Categories where Net = WORSE, or "none"]
  BETTER rows: [Cost Categories where Net = BETTER, or "none"]
  Conclusion:  [one sentence — is adoption justified given the WORSE/BETTER balance?]

Budget strength: HIGH / MEDIUM / LOW

Findings:
| ID   | Finding                                                           | Severity | IA-gate                               | Owner  | Resolution              |
|------|-------------------------------------------------------------------|----------|---------------------------------------|--------|-------------------------|
| F-01 | [argument current state sufficient — names mechanism, path]       | P1/P2/P3 | Passed — requires IA budget authority | [role] | [concrete action]       |
| F-02 | [second argument grounded in a cost row]                          | P1/P2/P3 | Passed — requires IA budget authority | [role] | [concrete action]       |

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence citing the Budget verdict Conclusion]
```

IA-gate test: "Would only a reviewer with budget authority over the current state frame this
finding as a cost position?" YES → Passed. NO → revise the finding to be framed in cost
terms, or drop it if budget authority is not relevant to the observation.

---

**STEP 3 — PRE-FLIGHT BLOCK (C1)**

Output this block before the first technical role section. It is the C1 compliance
artifact for Phase C entry.

```
## Phase C Pre-Flight (C1)

[ ] B1 — Null hypothesis stated in Step 2
[ ] B2 — Cost ledger: 4 rows × 2 columns × Net direction per row filled
[ ] B3 — Budget verdict: "WORSE rows:", "BETTER rows:", "Conclusion:" all present as named lines
[ ] B4 — Budget strength declared as named terminal field (below separator, not in table)
[ ] B5 — IA verdict issued in cost terms

C1 RESULT: ALL CLEAR — technical role sections may begin.
```

If any box is unchecked: `C1 RESULT: BLOCKED — [B-number] not met. Complete Phase B.`
Technical role sections cannot begin until C1 RESULT is ALL CLEAR.

---

**STEP 4 — TECHNICAL ROLE SECTIONS**

For each role in the routing table, run sub-steps 4A → 4B → 4C → 4D in sequence.
Sequence across roles: security/compliance → domain-specific → PM/TPM.

**4A — IA READ RECEIPT (pre-commitment — write before re-reading PR diff)**

Write the READ RECEIPT immediately after reading the IA section. Do not re-read the PR
diff before completing the receipt. The initial position is pre-commitment: it reflects
domain knowledge and the IA's cost estimate, not findings yet generated. A receipt written
after findings are known produces a rationalized initial position and fails C-23.

```
## IA READ RECEIPT — [Role Name]

Section read:              Step 2 — Inertia Advocate
Budget verdict read:
  WORSE rows restated:     [restate "WORSE rows:" line from Step 2 Budget verdict]
  BETTER rows restated:    [restate "BETTER rows:" line from Step 2 Budget verdict]
  Conclusion restated:     [restate "Conclusion:" sentence from Step 2 Budget verdict]
Budget strength read:      HIGH / MEDIUM / LOW [from Step 2 terminal field]
Cost row most relevant     [Maintenance / Incident exposure / Integration cost / Regression risk]
  to this role's domain:
Step 2 estimate for row:   Current-State: [cell value] | Adoption: [cell value] | Net: [direction]
Initial role position:     [confirms / disputes the IA's Net direction for the cited row]
  Pre-commitment reason:   [one phrase from domain knowledge alone — no PR diff findings yet]
```

**4B — C2 COMPLIANCE BLOCK (output after receipt, before findings)**

```
## C2 Compliance — [Role Name]

Phase B ledger row cited:     [same row as READ RECEIPT]
Net direction cited:          [WORSE / BETTER / NEUTRAL — from Step 2 table, this row]
Budget verdict WORSE rows:    [from Step 2 "WORSE rows:" line]
Budget verdict BETTER rows:   [from Step 2 "BETTER rows:" line]
Budget strength cited:        [HIGH / MEDIUM / LOW — from Step 2 terminal field]

C2 RESULT: SATISFIED — [Role Name] may generate findings.
```

If any field is missing or not sourced from Step 2 content:
`C2 RESULT: UNSATISFIED — [named gap]. Role section incomplete.`

**4C — GENERATE FINDINGS**

After completing 4A and 4B, re-read the PR diff for this role. For each finding candidate,
apply the domain-lens gate:

```
DOMAIN-LENS GATE (per finding):

Step A: "Would only [this role] raise this finding, given their domain?"
  YES → domain-loaded. Include it.
  NO  → generic. Go to Step B.

Step B: Revise to name a specific mechanism, path, function, or contract owned by this
  role's domain — unreachable without it. Re-execute Step A.
  Still NO → drop.
```

**4D — OUTPUT SECTION**

```
## [Role Name]

Source files:   [files that triggered this role]
Orientation:    [one phrase from .craft/roles/]

IA READ RECEIPT:
[paste the completed receipt from 4A — do not summarize or abbreviate any field]

C2 COMPLIANCE:
[paste the completed C2 block from 4B]

IA cost anchor (post-findings — required delta analysis):
  Phase B ledger row:       [same row as receipt and C2]
  Net direction:            [WORSE / BETTER / NEUTRAL]
  Budget strength:          [HIGH / MEDIUM / LOW]
  Position after findings:  [CONFIRMED / REVISED] — [one sentence]
  Artifact:                 [names the specific code surface, function, or mechanism from
                             the PR diff that confirmed or revised the initial position;
                             "no change" without a named artifact fails this field]

Findings: [only findings that passed the domain-lens gate]
| ID   | Finding                                        | Severity | Domain-Lens | Owner  | Resolution         |
|------|------------------------------------------------|----------|-------------|--------|--------------------|
| F-01 | [finding — passed gate Steps A and B]          | P1/P2/P3 | Passed      | [role] | [concrete action]  |
| F-02 | [second finding — passed gate]                 | P1/P2/P3 | Passed      | [role] | [concrete action]  |

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

Domain-Lens column: every finding row must have "Passed" in the Domain-Lens cell. A finding
row with an empty or missing Domain-Lens cell fails C-24 for that finding. A role section
with zero findings passes C-24 by default (no rows to check).

All role sections must be complete before proceeding to step 5.

---

**STEP 5 — CONSENSUS**

After all per-role sections are complete:

```
## Consensus

IA cost ledger: Budget strength was [HIGH / MEDIUM / LOW].
  WORSE rows:  [from Step 2 Budget verdict]
  BETTER rows: [from Step 2 Budget verdict]
  Technical roles [reinforced / challenged / defeated] the IA's cost estimate.
  Net: [one sentence — does the benefit case exceed the cost budget?]

Agreement: [area] — [role-A] and [role-B] independently raised [concern]

Divergence: [role-A] rates [area] P[N]; [role-B] rates P[N].
  Mechanism: [structural or architectural code property causing the difference]

Critical: [F-XX from role] — [why this most threatens the merge]
```

Perspective-label ban-to-fix — apply before writing any Mechanism line:

| Banned phrase (do not write) | Required replacement form |
|---|---|
| "they have different perspectives" | "[role-A] sees [code mechanism X]; [role-B] sees [code mechanism Y] — different code surfaces" |
| "they prioritize differently" | "[path X] is in [role-A]'s domain scope and outside [role-B]'s — different parts of the affected stack" |
| "they see this through different lenses" | "the change affects [mechanism A] (in [role-A]'s domain) and [mechanism B] (in [role-B]'s domain) at [locations]" |
| "from [role]'s perspective" as sole cause | name the code property causing risk — the architectural fact, not the role attribute |
| "their roles lead them to different conclusions" | "[role-A]'s scope includes [code surface X] where the PR changes [Y]; [role-B]'s scope does not include X" |

A Mechanism cell containing a banned phrase fails even if a code mechanism is also named.

---

**STEP 6 — DECISION**

```
## Recommendation

Decision:        GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from [role]] — [one sentence]
Conditions:      [what must be resolved, or "none"]
Sign-off roles:  [role(s) who confirm resolution before merge, or "n/a"]
```

One decision value: GO, NO-GO, or GO WITH CONDITIONS. No others. No delegation. No hedging.

---

**STEP 7 — AMEND SCOPE BLOCK (use only when AMEND directive present)**

When invoked with an AMEND directive, fill and output this block BEFORE STEP 1. All fields
are mandatory; write "none" if not applicable. Do not convert to prose.

```
## AMEND SCOPE

What was amended:           [description of change from default routing or scope]
Roles added:                [comma-separated list, or "none"]
Roles removed:              [comma-separated list, or "none"]
Files triggering addition:  [comma-separated list of PR diff files causing a new role, or
                            "n/a — scope change was manually directed"]
Prior findings superseded:  [comma-separated F-IDs from prior run, or "none — first run"]
```

Run steps 1–6 with the amended scope.
