---
skill: quest-variate
skill_target: corps-pr
round: 6
date: 2026-03-16
rubric_version: 6
---

# Variate R6 — corps-pr

5 complete prompt body variations for the `corps-pr` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Axes Selected

| Axis | Used In | R6 Focus |
|------|---------|----------|
| Inertia framing (C-19 terminal field separation — Budget verdict + Budget strength below the table as standalone declarations, not table rows; per-row net direction label WORSE/BETTER/NEUTRAL) | V-01, V-04, V-05 | C-19: named terminal fields structurally distinct from cost rows |
| Lifecycle emphasis (C-20 dual-clause entry condition — Phase C entry split into C1: Phase B exit checklist and C2: IA read prerequisite per-role, separately auditable) | V-02, V-04 | C-20: two named sub-conditions independently checkable |
| Role sequence (IA read-receipt as per-role structural prefix — each technical role section begins with a named IA READ RECEIPT block before any findings; C-20 satisfied per-role rather than by pipeline declaration) | V-03, V-05 | C-20: per-role read prerequisite as traceable output artifact |
| Output format (named-field schema universal — every output block uses named-field templates; finding tables include a Domain-Lens column to make gate compliance visible per finding) | V-03, V-05 | C-05, C-15: gate compliance traceable in output, not only in execution |
| Phrasing register (ban-to-fix substitution table) | V-02, V-04, V-05 | C-13: enumerated ban list with replacement forms |

**What changed from R5:**
- R5 V-01 introduced the cost ledger schema, which became C-19. R6 V-01 tightens it: Budget verdict and Budget strength are terminal fields below a visual separator, not additional rows. Adds a Net column (WORSE / BETTER / NEUTRAL) so the verdict is a direct derivation from row directions.
- R5 V-04 introduced the Phase C entry condition "Phase B exit met; roles read Phase B before writing," which became C-20. R6 V-02 tightens it: Phase C entry is two named sub-conditions (C1, C2) each with a checklist, independently auditable.
- R6 V-03 tests whether C-20 can be satisfied without a pipeline-level declaration by requiring a per-role IA READ RECEIPT block as the first structural element of every technical role section.
- R6 V-04 combines V-01 + V-02: C-19 terminal field schema + C-20 dual-clause entry condition, with the Phase C C2 checklist referencing named Phase B terminal fields.
- R6 V-05 combines V-01 + V-03 + ban-to-fix: C-19 ledger schema + per-role read receipts + substitution table; tests whether per-role materialization of C-20 is sufficient without a pipeline declaration.

---

## V-01 — Inertia Framing: C-19 Terminal Field Separation

**Axis**: Inertia framing
**Hypothesis**: R5 V-01 introduced the 4-row x 2-column cost ledger that became C-19. A gap
remained: Budget verdict and Budget strength appeared after the table but without enforced
structural separation from the cost rows — a section could embed them as a 5th row and satisfy
C-17 while failing C-19. R6 V-01 enforces terminal field separation explicitly: the cost table
has exactly 4 named rows and exactly 2 named columns plus a Net direction column
(WORSE/BETTER/NEUTRAL); Budget verdict and Budget strength appear below a horizontal separator
as standalone named declarations. The three-part structure makes C-19 a three-part check:
(a) 4 rows × 2 columns filled, (b) Net direction per row, (c) two terminal fields declared
below the table. A section that fills the table but folds the verdict into a 5th row fails
C-19 on part (c) alone.

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
## Routing Table

| File / File Group | Change Type | Role Selected | org.yaml Scope Pattern Matched |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern text from org.yaml] |
| (all files) | default | Inertia Advocate | default — always included |
```

Rules:
- Every changed file appears in at least one row. No file is silently dropped.
- Every role cites the exact org.yaml scope pattern matched — do not infer from filename.
- Coverage gap: if any file has no org.yaml match, append immediately after the table:

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
also requires a Net direction: WORSE means adopting this PR makes this cost category worse
compared to the status quo; BETTER means the PR reduces this cost; NEUTRAL means no
material change.

After the cost table, declare the two terminal fields as standalone named lines below a
separator. Do not add a 5th cost row — Budget verdict and Budget strength summarize the
entire ledger and must appear as terminal declarations outside the table.

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
Budget verdict:  [one sentence deriving the net cost/benefit from the row directions above —
                 name which rows are WORSE and which are BETTER and state whether adoption
                 is justified given the balance]
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

The separator (`---`) between the cost table and the terminal fields is structural — it marks
the boundary between the cost evidence rows and the summary declarations. A section that
embeds Budget verdict inside the table fails C-19 regardless of content quality.

---

**STEP 3 — TECHNICAL ROLE REVIEWS**

Technical roles read the IA section before writing their own findings. This is a prerequisite,
not a sequencing convention: each role's IA cost anchor must reference specific Phase 2 content
— a named ledger row and its Net direction — to demonstrate that the role read the IA section
before writing.

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

The gate tests domain fidelity, not location precision. A finding may name a precise file:line
and still fail Step A if any reviewer could reach the same observation without this role's domain.

Per-role section template:

```
## Review: [Role Name]

Source files:   [files from routing table that triggered this role]
Orientation:    [one phrase from .roles/ describing this role's domain]

IA cost anchor (demonstrates Phase 2 read prerequisite — cite a specific ledger row):
  Ledger row cited:      [Maintenance / Incident exposure / Integration cost / Regression risk]
  Current-State Cost:    [restate IA's cell value for this row]
  Adoption Cost:         [restate IA's cell value for this row]
  Net direction:         [WORSE / BETTER / NEUTRAL — from the IA's ledger]
  Budget strength:       [HIGH / MEDIUM / LOW — from IA's terminal field]
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

Replace any banned phrase with the architectural mechanism. A Mechanism line containing a
banned phrase fails even if a code mechanism is also named in the same sentence.

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

## V-02 — Lifecycle Emphasis: C-20 Dual-Clause Entry Condition

**Axis**: Lifecycle emphasis
**Hypothesis**: R5 V-02 introduced the top-level pipeline declaration that became C-18. R5 V-04
added the Phase C entry condition "Phase B exit met; roles read Phase B before writing," which
became C-20. The remaining gap: that single-sentence entry condition conflates two independently
auditable requirements. R6 V-02 splits Phase C entry into two named sub-conditions — C1 and C2
— each with its own verification mechanism. C1 is verified by a Phase B exit checklist
(declarative, checked before Phase C begins). C2 is verified by the IA cost anchor in each
technical role section (per-role, checked after each section is written). A run that satisfies
C1 but whose role sections omit the ledger row reference fails C2 for those roles — the
dual-clause structure makes the failure locatable to the specific role, not just the phase.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline. The pipeline
declaration below is the execution contract. Read every entry before producing any output.
No phase may begin until its stated entry conditions are satisfied.

---

**PIPELINE DECLARATION**

```
Phase A — Route
  Entry:    org.yaml + PR diff + .roles/ loaded
  Exit:     Routing table complete; every changed file has a row; every role cites an
            exact org.yaml scope pattern; coverage gaps declared if any
  Gates:    C-01, C-06

Phase B — Inertia Review
  Entry:    Phase A exit met
  Exit:     (B1) Null hypothesis stated
            (B2) Cost ledger filled: 4 named rows, 2 named columns, Net direction per row
            (B3) Budget verdict declared as named terminal field below the cost table
            (B4) Budget strength declared as named terminal field below the cost table
            (B5) IA verdict issued in cost terms
            All five conditions must be met for Phase B to exit.
  Gates:    C-11, C-17, C-19

Phase C — Technical Reviews
  Entry:    C1 (Phase B exit): all five Phase B exit conditions (B1–B5) are met
            C2 (IA read prerequisite): each technical role reads Phase B before writing
               findings; demonstrated by an IA cost anchor block naming a specific Phase B
               ledger row and restating that row's Current-State Cost, Adoption Cost, and
               Net direction values
            C1 is a pre-flight condition: if Phase B exit is incomplete, Phase C cannot
            begin. C2 is a per-role condition: if a role's IA cost anchor does not name a
            specific Phase B ledger row, C2 is not satisfied for that role.
  Exit:     All role sections complete; every role's IA anchor satisfies C2; every finding
            passed the domain-lens gate (Step A binary test + Step B rewrite consequence)
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20

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

Phase A exit: table complete; every file has a row; every role cites a scope pattern.

---

**PHASE B — INERTIA REVIEW**

Entry condition: Phase A exit met.

The IA is the status-quo budget authority. Phase B has five exit conditions (B1–B5). A section
that satisfies B1–B2 but omits the terminal fields (B3, B4) fails Phase B exit — Phase C
cannot begin until all five conditions are met.

```
## Phase B: Inertia Advocate

Null hypothesis: The codebase currently [does X via mechanism Y].           ← satisfies B1

Cost ledger (satisfies B2 when all 4 rows × 2 columns + Net filled):

| Cost Category     | Current-State Cost                                        | Adoption Cost (this PR)                          | Net       |
|-------------------|-----------------------------------------------------------|--------------------------------------------------|-----------|
| Maintenance       | [LOW/MED/HIGH — maintaining current path]                 | [maintaining new path post-merge]                | WORSE / BETTER / NEUTRAL |
| Incident exposure | [failure risk/severity under status quo]                  | [residual exposure after merge]                  | WORSE / BETTER / NEUTRAL |
| Integration cost  | [coordination overhead of current approach]               | [churn, downstream wiring, test burden]          | WORSE / BETTER / NEUTRAL |
| Regression risk   | [risk of new failures from current approach as-is]        | [risk introduced by this PR]                     | WORSE / BETTER / NEUTRAL |

---
Budget verdict:  [net cost/benefit conclusion from the row directions]           ← satisfies B3
Budget strength: HIGH / MEDIUM / LOW                                             ← satisfies B4

Findings:
F-01 [P1/P2/P3] [argument current state is sufficient — names mechanism, path, or function]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second argument grounded in cost ledger]
     Owner: [role] | Resolution: [action]
[minimum 2 findings]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence in cost terms]              ← satisfies B5
```

Phase B exit: B1 through B5 all met.

---

**PHASE C — TECHNICAL REVIEWS**

Phase C has two entry conditions.

**C1 — Phase B exit verification:**
Before Phase C begins, confirm all Phase B exit conditions are met:
- `[ ]` B1 — Null hypothesis stated
- `[ ]` B2 — Cost ledger: 4 rows × 2 columns × Net direction filled
- `[ ]` B3 — Budget verdict declared as named terminal field
- `[ ]` B4 — Budget strength declared as named terminal field
- `[ ]` B5 — IA verdict issued in cost terms

If any box is unchecked, Phase C cannot begin. Return to Phase B and complete the unmet
condition before proceeding.

**C2 — IA read prerequisite (per-role):**
Each technical role must demonstrate that it read Phase B before writing findings. Compliance
is demonstrated by an IA cost anchor block that: (a) names a specific Phase B ledger row,
(b) restates that row's Current-State Cost and Adoption Cost values as stated in Phase B, and
(c) states the Net direction from Phase B for that row. An anchor that paraphrases the ledger
without naming a specific row fails C2 for that role.

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

IA cost anchor (C2 compliance — cite Phase B ledger content):
  Phase B ledger row:          [Maintenance / Incident exposure / Integration cost / Regression risk]
  Current-State Cost (row):    [restate Phase B cell value exactly]
  Adoption Cost (row):         [restate Phase B cell value exactly]
  Net direction (row):         [WORSE / BETTER / NEUTRAL — from Phase B]
  Budget strength:             [HIGH / MEDIUM / LOW — from Phase B terminal field]
  This role [confirms / disputes] that Net direction because:
    [names the code surface, function, or mechanism; must name a code artifact the IA
     estimate did or did not account for — not role perspective or priority]

Findings: [all passed domain-lens gate]
F-01 [P1/P2/P3] [domain-specific finding]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second finding]
     Owner: [role] | Resolution: [action]
[minimum 2]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

Phase C exit: all role sections complete; every role's IA anchor names a Phase B ledger row
(C2); every finding passed Step A of the domain-lens gate.

---

**PHASE D — SYNTHESIS**

Entry condition: Phase C exit met.

```
## Phase D: Consensus

IA cost ledger: Budget strength was [HIGH / MEDIUM / LOW].
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

Phase E exit: exactly one decision stated with value, justification, and sign-off roles if
conditions apply.

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

## V-03 — Role Sequence: IA Read-Receipt as Per-Role Structural Prefix

**Axis**: Role sequence
**Hypothesis**: R5 V-04 and R6 V-02 satisfy C-20 via a pipeline-level declaration: the entry
condition names the IA read prerequisite once, as an architectural contract. This tests a
different approach: C-20 satisfied by per-role output artifact rather than pipeline declaration.
Each technical role section begins with a named IA READ RECEIPT block that is output before
any finding is written. The receipt must name the Phase B section read, acknowledge the Budget
strength and Budget verdict, and state the role's initial position on a specific cost row.
Because the receipt is output (not declaration), it is auditable post-hoc per role: a reviewer
can verify C-20 compliance by checking whether each receipt block cites Phase B content. A
missing receipt block is a visible output gap, not a pipeline violation. This tests whether
per-role materialization produces stronger C-20 signal than a single pipeline-level declaration.

---

You are running `/corps-pr`. Follow each numbered step exactly. Fill every named field and
template slot. A missing block or incomplete receipt is a structural output failure.

**READ INPUTS**

Read: `org.yaml`, PR diff, `.roles/`.

---

**STEP 1 — ROUTING TABLE**

Output before advancing to step 2. Do not begin reviews until the table is complete.

```
## Routing Table

| File / File Group | Change Type | Role Selected | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern from org.yaml] |
| (all files) | default | Inertia Advocate | default — always included |
```

Every file gets a row. Every role cites its exact org.yaml scope pattern.

Coverage gap: append immediately after the table if any file has no org.yaml match:

```
COVERAGE GAP
File:    [path]
Reason:  No org.yaml scope pattern matches this path.
```

---

**STEP 2 — INERTIA ADVOCATE SECTION**

The IA section appears first. Fill the cost ledger completely. Budget verdict and Budget
strength are terminal declarations below the table — do not embed them as additional rows.

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
Budget verdict:  [net cost/benefit conclusion derived from row directions above]
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

**3A — IA READ RECEIPT (write before any findings)**

Every technical role section begins with an IA READ RECEIPT block. This block demonstrates
that the role read the IA section before generating findings. It is output, not declared —
it must appear in the text for C-20 compliance to be verifiable.

```
## IA READ RECEIPT — [Role Name]

Section read:         Phase 2 — Inertia Advocate
Budget verdict read:  [restate the IA's Budget verdict verbatim or in one accurate sentence]
Budget strength read: HIGH / MEDIUM / LOW [from IA terminal field]
Cost row most        [Maintenance / Incident exposure / Integration cost / Regression risk]
  relevant to this
  role's domain:
IA's estimate for    Current-State: [cell value] | Adoption: [cell value] | Net: [direction]
  that row:
Initial role         [confirms / disputes the IA's estimate for the cited row — one phrase
  position:          before seeing any PR diff findings]
```

A receipt block that uses placeholder text (e.g., "see Phase 2") or does not restate the
IA's Budget verdict fails to demonstrate the read prerequisite.

**3B — GENERATE FINDINGS**

After completing 3A, write findings for this role. For each finding candidate, apply the
domain-lens gate:

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

Write the section after 3A (receipt) and 3B (gate) are complete.

```
## [Role Name]

Source files:   [files that triggered this role]
Orientation:    [one phrase from .roles/]

IA READ RECEIPT: [paste the completed receipt block from 3A here]

IA cost anchor (revise initial position if findings changed it):
  This role [confirms / disputes] IA's [row] estimate because:
    [names the code surface, function, or mechanism — not role attribute]

Findings: [only findings that passed Steps A and B]
| ID   | Finding                                      | Severity | Domain-Lens | Owner  | Resolution        |
|------|----------------------------------------------|----------|-------------|--------|-------------------|
| F-01 | [finding — passed gate]                      | P1/P2/P3 | Passed      | [role] | [concrete action] |
| F-02 | [second finding — passed gate]               | P1/P2/P3 | Passed      | [role] | [concrete action] |

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

All role sections (including their receipt blocks) must be complete before proceeding to step 4.

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

## V-04 — Combined: C-19 Terminal Field Schema + C-20 Dual-Clause Pipeline

**Axes**: Inertia framing + Lifecycle emphasis
**Hypothesis**: V-01 tightens C-19: terminal fields separated from cost rows, Net direction
per row. V-02 tightens C-20: Phase C entry split into C1 (Phase B exit checklist) and C2
(per-role IA read prerequisite). Combining them creates a chain: Phase B exit requires all
four cost rows + Net direction + two terminal fields (C-19 compliance) → Phase C C1 checklist
verifies those specific fields → Phase C C2 per-role anchor requires naming a specific row's
Net direction value (the net direction is in the Phase B table, so citing it proves the role
read Phase B). The chain makes C-19 and C-20 mutually reinforcing: C-20 C2 compliance is
directly verified by asking whether the role cited a Phase B Net direction value, and that
value only exists if Phase B satisfied C-19. A run that satisfies C-19 and C-20 independently
but does not chain them (i.e., the IA anchor does not reference the Net column) passes both
criteria in isolation but misses the architectural integration.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline. The pipeline
declaration below is the execution contract. Read every entry before producing any output.
No phase may begin until its stated entry conditions are satisfied.

---

**PIPELINE DECLARATION**

```
Phase A — Route
  Entry:    org.yaml + PR diff + .roles/ loaded
  Exit:     Routing table complete; every changed file has a row; every role cites an
            exact org.yaml scope pattern; coverage gaps declared if any
  Gates:    C-01, C-06

Phase B — Inertia Review
  Entry:    Phase A exit met
  Exit:     (B1) Null hypothesis stated
            (B2) Cost ledger: 4 named rows × 2 named columns × Net direction per row filled
            (B3) Budget verdict declared as named terminal field below the cost table
            (B4) Budget strength declared as named terminal field below the cost table
            (B5) IA verdict issued in cost terms
  Gates:    C-11, C-17, C-19

Phase C — Technical Reviews
  Entry:    C1 (Phase B exit verification):
              [ ] B1 met — null hypothesis stated
              [ ] B2 met — 4 rows × 2 columns × Net direction filled
              [ ] B3 met — Budget verdict declared as terminal field
              [ ] B4 met — Budget strength declared as terminal field
              [ ] B5 met — IA verdict issued
            C1 is a pre-flight check. If any box is unchecked, Phase C does not begin.
            C2 (IA read prerequisite — per-role):
              Each technical role demonstrates it read Phase B by citing: (a) a specific
              Phase B ledger row name, (b) that row's Net direction from Phase B, and
              (c) Budget strength from Phase B terminal field. An anchor that does not
              cite a specific row Net direction value fails C2 for that role.
  Exit:     All role sections complete; every role's IA anchor satisfies C2; every finding
            passed the domain-lens gate
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20

Phase D — Synthesis
  Entry:    Phase C exit met
  Exit:     Consensus complete; all Mechanism lines pass the ban-to-fix check
  Gates:    C-03, C-09, C-12, C-13

Phase E — Decision
  Entry:    Phase D exit met
  Exit:     Exactly one GO / NO-GO / GO WITH CONDITIONS issued with justification and
            sign-off roles for any conditions
  Gates:    C-04, C-10
```

Phase C C2 compliance is verified by the presence of a Net direction citation in each role's
IA anchor. The Net direction exists only in the Phase B cost table — citing it is proof of
read, not just acknowledgment of read.

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

Coverage gap: append immediately after table if any file has no org.yaml match:
`COVERAGE GAP: [file] — no org.yaml scope pattern covers this path.`

Phase A exit: table complete; every file has a row; every role cites a scope pattern.

---

**PHASE B — INERTIA REVIEW**

Entry condition: Phase A exit met.

Phase B has five exit conditions. B3 and B4 require Budget verdict and Budget strength to
appear as named terminal fields below the cost table — not as additional table rows.

```
## Phase B: Inertia Advocate

Null hypothesis: The codebase currently [does X via mechanism Y].

Cost ledger (Phase B exit conditions B2 — all rows, columns, Net directions required):

| Cost Category     | Current-State Cost                                        | Adoption Cost (this PR)                          | Net       |
|-------------------|-----------------------------------------------------------|--------------------------------------------------|-----------|
| Maintenance       | [LOW/MED/HIGH — maintaining current path]                 | [maintaining new path post-merge]                | WORSE / BETTER / NEUTRAL |
| Incident exposure | [failure risk/severity under status quo]                  | [residual exposure after merge]                  | WORSE / BETTER / NEUTRAL |
| Integration cost  | [coordination overhead of current approach]               | [churn, downstream wiring, test burden]          | WORSE / BETTER / NEUTRAL |
| Regression risk   | [risk of new failures from current approach as-is]        | [risk introduced by this PR]                     | WORSE / BETTER / NEUTRAL |

---
Budget verdict:  [net conclusion from the row Net directions above]   ← B3 (terminal field)
Budget strength: HIGH / MEDIUM / LOW                                  ← B4 (terminal field)

Findings:
F-01 [P1/P2/P3] [argument current state is sufficient — names mechanism, path, or function]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second argument]
     Owner: [role] | Resolution: [action]
[minimum 2]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence in cost terms]   ← B5
```

Phase B exit: B1–B5 all met. Phase C C1 pre-flight check now available.

---

**PHASE C — TECHNICAL REVIEWS**

Before beginning Phase C, verify Phase C C1:

```
Phase C C1 pre-flight:
[ ] B1 — Null hypothesis stated in Phase B
[ ] B2 — Cost ledger: 4 rows × 2 columns × Net direction per row filled
[ ] B3 — Budget verdict declared as terminal field (below separator, not in table)
[ ] B4 — Budget strength declared as terminal field (below separator, not in table)
[ ] B5 — IA verdict issued in cost terms

If all checked: Phase C may begin.
If any unchecked: return to Phase B and satisfy the missing condition.
```

Sequence: security/compliance → domain-specific → PM/TPM.

**Domain-lens gate (Phase C exit condition):**

```
Step A: "Would only [this role] raise this finding, given their domain?"
  YES → include the finding.
  NO  → Go to Step B.

Step B: Revise to name a specific mechanism, path, function, or contract owned by this
  role's domain — unreachable without it. Re-execute Step A.
  Still NO → drop the finding.
```

Per-role template:

```
## Phase C: [Role Name]

Source files:   [files from Phase A routing that triggered this role]
Orientation:    [one phrase from .roles/]

IA cost anchor (C2 compliance — cite Phase B table content to demonstrate read):
  Phase B ledger row:    [Maintenance / Incident exposure / Integration cost / Regression risk]
  Net direction (row):   [WORSE / BETTER / NEUTRAL — from Phase B table, this specific row]
  Current-State Cost:    [restate Phase B cell value for this row]
  Adoption Cost:         [restate Phase B cell value for this row]
  Budget strength:       [HIGH / MEDIUM / LOW — from Phase B terminal field]
  This role [confirms / disputes] that Net direction because:
    [names the specific code artifact — function, path, mechanism — that the IA estimate
     did or did not account for; must be grounded in PR diff content]

Findings: [all passed domain-lens gate]
F-01 [P1/P2/P3] [domain-specific finding]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second finding]
     Owner: [role] | Resolution: [action]
[minimum 2]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

Phase C exit: all role sections complete; every anchor cites a Phase B Net direction (C2
verified); every finding passed Step A of the domain-lens gate.

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

## V-05 — Combined: C-19 Terminal Field Schema + Per-Role Read Receipt + Ban-to-Fix

**Axes**: Inertia framing + Role sequence + Phrasing register
**Hypothesis**: Three mechanisms, each satisfying a different criterion at a different phase
without a top-level pipeline declaration. C-19 (Phase B): cost ledger with Net direction per
row + Budget verdict and Budget strength as terminal fields below the table. C-20 (Phase C,
per-role): IA READ RECEIPT block at the start of each technical role section; the receipt
must restate the Phase B Net direction for one named cost row — Net direction citation is the
verifiable C-20 read proof. C-13 (Phase D): ban-to-fix substitution table for perspective-
label phrases. The combination tests whether per-role materialization (V-03's C-20 approach)
can achieve the same structural audit properties as a pipeline declaration (V-02's C-20
approach), while simultaneously enforcing C-19 and C-13. A run that satisfies all three
mechanisms produces output that is auditable at each phase transition without requiring the
reader to reconstruct the intended pipeline structure from a separate declaration.

---

You are running `/corps-pr`. Follow each numbered step exactly. Fill every named field and
template slot. A missing receipt block or incomplete cost ledger is a structural failure
regardless of prose quality.

**READ INPUTS**

Read: `org.yaml`, PR diff, `.roles/`.

---

**STEP 1 — ROUTING TABLE**

Fill every cell. Output before advancing.

```
## Routing Table

| File / File Group | Change Type | Role Selected | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern from org.yaml] |
| (all files) | default | Inertia Advocate | default — always included |
```

Coverage gap block — append if any file has no org.yaml match:

```
COVERAGE GAP
File:    [path]
Reason:  No org.yaml scope pattern matches this path.
```

---

**STEP 2 — INERTIA ADVOCATE SECTION**

Fill the cost ledger. All rows and both named columns are required. The Net direction column
states WORSE, BETTER, or NEUTRAL for each row — not a magnitude, not a sentence, one of
those three values. Budget verdict and Budget strength are terminal fields declared below the
separator line. Do not embed them as table rows.

```
## Inertia Advocate

Null hypothesis:          [what the codebase currently does in this area — one sentence]
Null hypothesis strength: HIGH / MEDIUM / LOW

Cost ledger (all rows, columns, and Net directions required):

| Cost Category     | Current-State Cost                                        | Adoption Cost (this PR)                          | Net       |
|-------------------|-----------------------------------------------------------|--------------------------------------------------|-----------|
| Maintenance       | [LOW/MED/HIGH — burden of maintaining current path]       | [burden of maintaining new path post-merge]      | WORSE / BETTER / NEUTRAL |
| Incident exposure | [failure risk/severity under status quo]                  | [residual exposure after merge]                  | WORSE / BETTER / NEUTRAL |
| Integration cost  | [coordination overhead of current approach]               | [churn, downstream wiring, test burden]          | WORSE / BETTER / NEUTRAL |
| Regression risk   | [risk of new failures from current approach as-is]        | [risk introduced by this PR]                     | WORSE / BETTER / NEUTRAL |

---
Budget verdict:  [net conclusion derived from the Net direction column above — which rows
                 are WORSE, which are BETTER, and whether adoption is justified overall]
Budget strength: HIGH / MEDIUM / LOW

Findings:
| ID   | Finding                                                        | Severity | Owner  | Resolution              |
|------|----------------------------------------------------------------|----------|--------|-------------------------|
| F-01 | [argument current state is sufficient — names mechanism, path] | P1/P2/P3 | [role] | [concrete action]       |
| F-02 | [second argument grounded in a cost row]                       | P1/P2/P3 | [role] | [concrete action]       |

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence citing the Budget verdict]
```

---

**STEP 3 — TECHNICAL ROLE SECTIONS**

For each role in the routing table, run sub-steps 3A → 3B → 3C in sequence.
Sequence across roles: security/compliance → domain-specific → PM/TPM.

**3A — IA READ RECEIPT (output before any findings)**

The receipt block is required for every technical role. It is output, not declared — its
presence in the text is the C-20 compliance artifact. The receipt must cite a specific Phase 2
cost row by name and restate that row's Net direction value from the Phase 2 ledger. A receipt
that acknowledges the IA section without naming a specific row Net direction value is
incomplete and does not satisfy the read prerequisite.

```
## IA READ RECEIPT — [Role Name]

Section read:           Phase 2 — Inertia Advocate
Budget verdict read:    [restate Phase 2 Budget verdict in one accurate sentence]
Budget strength read:   HIGH / MEDIUM / LOW [from Phase 2 terminal field]
Cost row most           [Maintenance / Incident exposure / Integration cost / Regression risk]
  relevant to this
  role's domain:
Net direction for       WORSE / BETTER / NEUTRAL [exact value from Phase 2 ledger for this row]
  that row:
Initial role position:  [confirms / disputes — one phrase]
```

**3B — FINDING GENERATION**

After completing 3A, generate findings for this role. For each finding candidate, apply the
domain-lens gate:

```
DOMAIN-LENS GATE:

Step A: "Would only [this role] raise this finding, given their domain?"
  YES → include.
  NO  → generic. Go to Step B.

Step B: Revise to name a mechanism, path, function, or contract owned by this role's
  domain — unreachable without it. Re-execute Step A.
  Still NO → drop.
```

**3C — OUTPUT SECTION**

```
## [Role Name]

Source files:   [files that triggered this role]
Orientation:    [one phrase from .roles/]

IA READ RECEIPT:
[paste the completed receipt from 3A here]

IA cost anchor (revise initial position after findings if needed):
  This role [confirms / disputes] Phase 2 [row name] Net direction ([value]) because:
    [names the code surface, function, or mechanism — not role attribute or perspective]

Findings:
| ID   | Finding                                        | Severity | Domain-Lens | Owner  | Resolution         |
|------|------------------------------------------------|----------|-------------|--------|--------------------|
| F-01 | [finding — passed gate]                        | P1/P2/P3 | Passed      | [role] | [concrete action]  |
| F-02 | [second finding — passed gate]                 | P1/P2/P3 | Passed      | [role] | [concrete action]  |

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

All role sections (including their receipt blocks) must be complete before proceeding to step 4.

---

**STEP 4 — CONSENSUS TABLE**

```
## Consensus

| Signal     | Finding Area              | Roles                  | Mechanism / Notes                                    |
|------------|---------------------------|------------------------|------------------------------------------------------|
| IA budget  | [cost ledger]             | Inertia Advocate       | Strength: [HIGH/MEDIUM/LOW] — [how technical roles   |
|            |                           |                        | responded to the cost case]                          |
| Agreement  | [shared concern area]     | [role-A], [role-B]     | [one sentence on shared concern]                     |
| Divergence | [divergent area]          | [role-A (PN)],         | [structural or architectural property causing the    |
|            |                           | [role-B (PN)]          | difference — see ban-to-fix below]                   |
| Critical   | [top finding area]        | [role]                 | [why this finding most threatens the merge]          |
```

**Divergence Mechanism ban-to-fix — apply before writing any Divergence Mechanism cell.
Each row is independently checkable:**

| Banned phrase (do not write) | Required replacement form (write this instead) |
|---|---|
| "they have different perspectives" | "[role-A] sees [code mechanism X]; [role-B] sees [code mechanism Y] — different code surfaces affected by the change" |
| "they prioritize differently" | "[path X] is inside [role-A]'s domain scope and outside [role-B]'s — they are assessing different parts of the affected stack" |
| "they see this through different lenses" | "the change modifies [mechanism A] (in [role-A]'s domain) and [mechanism B] (in [role-B]'s domain) through separate paths at [locations]" |
| "from [role]'s perspective" as sole cause | name the code property making this role see risk — the architectural fact, not the role attribute |
| "their roles lead them to different conclusions" | "[role-A]'s scope includes [code surface X] where the PR changes [Y]; [role-B]'s scope does not include X — they are reviewing different change surfaces" |

A Mechanism cell containing a banned phrase fails even if a code mechanism is also named.

---

**STEP 5 — RECOMMENDATION BLOCK**

```
## Recommendation

Decision:        GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from [role]] — [one sentence]
Conditions:      [what must be resolved, or "none"]
Sign-off roles:  [role(s) who confirm resolution before merge, or "n/a"]
```

One decision value: GO, NO-GO, or GO WITH CONDITIONS. No others. No delegation. No hedging.

---

**STEP 6 — AMEND SCOPE BLOCK (use only when AMEND directive present)**

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

Run steps 1–5 with the amended scope.
