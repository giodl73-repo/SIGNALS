---
skill: quest-variate
skill_target: corps-pr
round: 8
date: 2026-03-16
rubric_version: 8
---

# Variate R8 — corps-pr

5 complete prompt body variations for the `corps-pr` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Axes Selected

| Axis | Used In | R8 Focus |
|------|---------|----------|
| Inertia framing (C-25 string-matchable Budget verdict — three separate labeled lines at line boundary; each independently matchable by string search; compound-clause or single-line form fails) | V-01, V-04, V-05 | C-25: the three-clause structure is the derivation evidence — row names must appear as scannable output lines, not as content embedded in prose |
| Lifecycle emphasis (C-26 exact named output result lines — `C1 RESULT: ALL CLEAR` / `C1 RESULT: BLOCKED -- [item]` and `C2 RESULT: SATISFIED` / `C2 RESULT: UNSATISFIED -- [citation missing]` as terminal-line tokens) | V-02, V-04, V-05 | C-26: result tokens are the compliance artifact; non-compliance is a visible output gap detectable by token scan, not by reading prose or the pipeline declaration |
| Role sequence (C-27 PRE-COMMITMENT labeled block structurally before findings — initial position is a standalone named element that precedes the findings table, not a receipt field that can be back-filled after the diff is read) | V-03, V-05 | C-27: PRE-COMMITMENT block precedes findings in the output text, making timing independently verifiable without re-running the skill |

**What changed from R7:**
- R7 V-01 enforced the 3-clause Budget verdict formula (WORSE rows named, BETTER rows named, Conclusion stated). The gap: the three clauses could appear as three indented fields under a single `Budget verdict:` label — readable but not independently string-matchable per clause. R8 V-01 requires each clause on its own line at line start (or consistent indent level), so `grep "^WORSE rows:"` or `grep "^BETTER rows:"` finds the line without prose parsing. A verdict where WORSE rows are mentioned inside a Conclusion sentence fails C-25 — the line-level separation is the derivation structure.
- R7 V-02 introduced C1 and C2 output blocks with result lines. The gap: result lines included supplementary text (`C1 RESULT: ALL CLEAR — Phase C may begin`) that is not part of the matchable token. A compliance check tool scanning for `C1 RESULT: ALL CLEAR` would fail on `C1 RESULT: ALL CLEAR — Phase C may begin` unless the suffix is known. R8 V-02 strips the supplementary text from the token and names the exact strings: `C1 RESULT: ALL CLEAR` (no suffix) or `C1 RESULT: BLOCKED -- [item]`. The double-dash separator is the diagnostic boundary. Same for C2: `C2 RESULT: SATISFIED` or `C2 RESULT: UNSATISFIED -- [citation missing]`.
- R7 V-03 required the READ RECEIPT (including initial position) to be written before re-reading the PR diff. The gap: the initial position is a field WITHIN the receipt template — it appears in the same block as the Budget verdict restatement and Budget strength. A role could write the receipt after findings and fill the initial position field consistently. There is no structural separator in the output between "what I knew before the diff" and "what I found in the diff." R8 V-03 adds a distinct `PRE-COMMITMENT:` labeled block that is a separate named element in the output text — it follows the receipt and precedes the findings table. The initial position moves from the receipt into this block. Ordering is independently verifiable: PRE-COMMITMENT appears before the findings table in the output text.
- R8 V-04 combines V-01 and V-02: the three-clause labeled lines in the Budget verdict feed directly into C1's B3 check ("three labeled lines present: WORSE rows, BETTER rows, Conclusion") and C2 requires each role to cite those lines verbatim, making C2 compliance a traceable quotation of B3 structure.
- R8 V-05 integrates all three axes: three-clause labeled lines (C-25) + exact result tokens (C-26) + PRE-COMMITMENT block before findings (C-27). Tests whether all three mechanisms integrate without added pipeline complexity.

---

## V-01 — Inertia Framing: C-25 String-Matchable Budget Verdict Formula

**Axis**: Inertia framing
**Hypothesis**: R7 V-01 required the Budget verdict to be a 3-clause formula with WORSE rows and BETTER rows named. The remaining gap: the three clauses appear as indented fields under a single `Budget verdict:` label block — a human reader can verify row presence, but string-based compliance scanning requires knowing the indented label format. A verdict written as prose with embedded row names ("Maintenance and Regression risk are WORSE; Integration cost is BETTER; adoption is not yet justified") satisfies C-21 content requirements but fails C-25 because neither clause is independently scannable. R8 V-01 enforces line-level separation: each clause must appear as a standalone labeled line, making `WORSE rows:`, `BETTER rows:`, and `Conclusion:` independently string-matchable. A compound form such as `Budget verdict: WORSE — Maintenance, Regression; BETTER — Integration; not justified` fails even if all rows are named, because no single-line scan retrieves each clause separately.

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

After the cost table, declare the Budget verdict, Budget strength, and findings below a
separator. The Budget verdict MUST appear as exactly three separate labeled lines — one
line per clause. Each line starts at the same indent level, begins with its clause label,
and contains only that clause. This line-level structure makes every row citation
independently string-matchable without parsing the surrounding prose.

```
## Inertia Advocate

Null hypothesis: The codebase currently [does X via mechanism Y].

Cost ledger:

| Cost Category     | Current-State Cost                                        | Adoption Cost (this PR)                               | Net                      |
|-------------------|-----------------------------------------------------------|-------------------------------------------------------|--------------------------|
| Maintenance       | [LOW/MED/HIGH — burden to maintain current path]          | [burden to maintain new code path post-merge]         | WORSE / BETTER / NEUTRAL |
| Incident exposure | [failure risk/severity under current approach]            | [residual exposure if this PR merges]                 | WORSE / BETTER / NEUTRAL |
| Integration cost  | [coordination overhead of current approach]               | [churn, downstream wiring, test fixture burden]       | WORSE / BETTER / NEUTRAL |
| Regression risk   | [risk of new failures from current approach as-is]        | [risk of new failures introduced by this PR]          | WORSE / BETTER / NEUTRAL |

---
WORSE rows: [names of Cost Categories where Net = WORSE, or "none"]
BETTER rows: [names of Cost Categories where Net = BETTER, or "none"]
Conclusion: [one sentence — is adoption justified given the balance of WORSE and BETTER?]

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

The three-clause structure is the string-matchability contract:
- `WORSE rows:` must be its own line. It may not appear inside the Conclusion sentence.
- `BETTER rows:` must be its own line. It must appear even when no rows improved — write `BETTER rows: none`.
- `Conclusion:` must be its own line. It names the rows by citing the WORSE/BETTER lines above it.
A verdict that names all rows correctly in prose but omits any of the three labeled lines fails C-25.

---

**STEP 3 — TECHNICAL ROLE REVIEWS**

Technical roles read the IA section before writing findings. Each role's IA cost anchor
must restate the three Budget verdict lines verbatim — not paraphrased, not merged, not
summarized into a single sentence.

Sequence: security/compliance → domain-specific → PM/TPM.

Domain-lens gate — execute per finding before writing:

```
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
Orientation:    [one phrase from .roles/ describing this role's domain]

IA cost anchor (demonstrates Step 2 read — cite Budget verdict lines verbatim):
  WORSE rows: [copied verbatim from Step 2 Budget verdict line]
  BETTER rows: [copied verbatim from Step 2 Budget verdict line]
  Conclusion: [copied verbatim from Step 2 Budget verdict line]
  Budget strength: [HIGH / MEDIUM / LOW — from Step 2 terminal field]
  Ledger row cited: [Maintenance / Incident exposure / Integration cost / Regression risk]
  Net direction for that row: [WORSE / BETTER / NEUTRAL — from Step 2 ledger]
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

The IA cost anchor requires copying the three labeled lines from Step 2 exactly — same
label text, same value, one line per clause. A role that writes "WORSE and BETTER rows
were Maintenance and Integration cost" in prose does not demonstrate the read.

---

**STEP 4 — CONSENSUS SYNTHESIS**

After all per-role sections are complete:

```
## Consensus

IA cost ledger: Budget strength was [HIGH / MEDIUM / LOW].
  WORSE rows were: [restate from Step 2]. BETTER rows were: [restate from Step 2].
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

## V-02 — Lifecycle Emphasis: C-26 Exact Named Output Result Lines for C1 and C2

**Axis**: Lifecycle emphasis
**Hypothesis**: R7 V-02 established C1 and C2 compliance blocks, each with a result line. The
gap: the result lines included supplementary text such as "Phase C may begin" and "Role may
generate findings" appended after the core token. A compliance scan looking for
`C1 RESULT: ALL CLEAR` would fail a literal string match on
`C1 RESULT: ALL CLEAR — Phase C may begin` unless the suffix pattern is also known. R8 V-02
strips the supplementary text from the core token and defines exact matchable strings:
`C1 RESULT: ALL CLEAR` (no suffix) or `C1 RESULT: BLOCKED -- [item]` (double-dash diagnostic).
C2 uses `C2 RESULT: SATISFIED` or `C2 RESULT: UNSATISFIED -- [citation missing]`. The
double-dash boundary separates the pass/fail token from the diagnostic text, so either half
is independently scannable. A result line written as `C2: satisfied (IA read confirmed)` fails
because the token is neither the exact string nor in the required format.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline. The pipeline
declaration below is the execution contract. Read every phase entry before producing
any output. No phase may begin until its stated entry conditions are satisfied.

---

**PIPELINE DECLARATION**

```
Phase A — Route
  Entry:    org.yaml + PR diff + .roles/ loaded
  Exit:     Routing table complete; every changed file has a row; every role cites
            exact org.yaml scope pattern; coverage gaps declared if any
  Gates:    C-01, C-06

Phase B — Inertia Review
  Entry:    Phase A exit met
  Exit:     (B1) Null hypothesis stated
            (B2) Cost ledger filled: 4 named rows × 2 columns × Net direction per row
            (B3) Budget verdict: three separate labeled lines present —
                 line 1 starts "WORSE rows:", line 2 starts "BETTER rows:",
                 line 3 starts "Conclusion:"
            (B4) Budget strength declared as named terminal field below separator
            (B5) IA verdict issued in cost terms
            All five conditions must be met for Phase B to exit.
  Gates:    C-11, C-17, C-19, C-21, C-25

Phase C — Technical Reviews
  Entry:    Two independently auditable sub-conditions:
            C1 (Phase B exit pre-flight):
              Verify B1–B5 once, before Phase C begins. Any unchecked item blocks
              Phase C. Output the PRE-FLIGHT block ending with the exact result token.
            C2 (IA read prerequisite — per-role):
              Each role outputs a COMPLIANCE block before findings, ending with the
              exact result token. A missing block or wrong token fails C2 for that
              role independently.
  Exit:     C1 result token is ALL CLEAR; every role's C2 result token is SATISFIED;
            every finding passed the domain-lens gate
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26

Phase D — Synthesis
  Entry:    Phase C exit met
  Exit:     Consensus complete; all Mechanism lines pass the ban-to-fix check
  Gates:    C-03, C-09, C-12, C-13

Phase E — Decision
  Entry:    Phase D exit met
  Exit:     Exactly one GO / NO-GO / GO WITH CONDITIONS; conditions name sign-off role
  Gates:    C-04, C-10
```

---

**PHASE A — ROUTE**

Entry: `org.yaml`, PR diff, `.roles/` loaded.

```
## Phase A: Routing

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern from org.yaml] |
| (all files) | default | Inertia Advocate | default — always included |
```

Coverage gap: if any file matches no org.yaml scope pattern, append:
`COVERAGE GAP: [file] — no org.yaml scope pattern covers this path.`

Phase A exit: table complete; every file has a row; every role cites a scope pattern.

---

**PHASE B — INERTIA REVIEW**

Entry: Phase A exit met.

Phase B has five exit conditions (B1–B5). B3 requires three separate labeled lines for
the Budget verdict — each on its own line, beginning with its clause label. The three
lines are not embedded in any table cell and not merged into a prose sentence.

```
## Phase B: Inertia Advocate

Null hypothesis: The codebase currently [does X via mechanism Y].           ← B1

Cost ledger (B2 — 4 rows × 2 columns × Net direction per row):

| Cost Category     | Current-State Cost                                        | Adoption Cost (this PR)                          | Net                      |
|-------------------|-----------------------------------------------------------|--------------------------------------------------|--------------------------|
| Maintenance       | [LOW/MED/HIGH — maintaining current path]                 | [maintaining new path post-merge]                | WORSE / BETTER / NEUTRAL |
| Incident exposure | [failure risk/severity under status quo]                  | [residual exposure after merge]                  | WORSE / BETTER / NEUTRAL |
| Integration cost  | [coordination overhead of current approach]               | [churn, downstream wiring, test burden]          | WORSE / BETTER / NEUTRAL |
| Regression risk   | [risk of new failures from current approach as-is]        | [risk introduced by this PR]                     | WORSE / BETTER / NEUTRAL |

---
WORSE rows: [Cost Categories where Net = WORSE, or "none"]              ← B3 line 1
BETTER rows: [Cost Categories where Net = BETTER, or "none"]            ← B3 line 2
Conclusion: [one sentence — is adoption justified given the balance?]   ← B3 line 3

Budget strength: HIGH / MEDIUM / LOW                                     ← B4

Findings:
F-01 [P1/P2/P3] [argument current state is sufficient]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second argument grounded in cost ledger]
     Owner: [role] | Resolution: [action]
[minimum 2]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence in cost terms]      ← B5
```

Phase B exit: B1 through B5 all met; the three Budget verdict lines appear as separate
labeled output lines in the text.

---

**PHASE C — TECHNICAL REVIEWS**

Phase C has two entry conditions: C1 and C2. Each produces an output block ending with an
exact result token. The token strings are fixed — no suffix, no paraphrase, no alternative
capitalization. Compliance is verified by scanning for the token string.

**C1 — Phase B Exit Pre-Flight Block:**

Output this block immediately before the first technical role section. The C1 result token
is the compliance artifact — write it as the final line of the block.

```
## Phase C Pre-Flight (C1)

[ ] B1 — Null hypothesis stated in Phase B
[ ] B2 — Cost ledger: 4 rows × 2 columns × Net direction per row filled
[ ] B3 — Budget verdict: three separate labeled lines present
         (WORSE rows: / BETTER rows: / Conclusion: each on own line)
[ ] B4 — Budget strength declared as named terminal field below separator
[ ] B5 — IA verdict issued in cost terms

C1 RESULT: ALL CLEAR
```

If any box is unchecked, replace the final line with:
`C1 RESULT: BLOCKED -- [B-number that failed]`
Phase C cannot begin until C1 RESULT: ALL CLEAR appears. No supplementary text is added
to the token line. The token is the full content of that line.

**C2 — IA Read Prerequisite (Per-Role):**

Each technical role section begins with a C2 compliance block before any findings. The
C2 result token is the final line of the block.

```
## C2 Compliance — [Role Name]

Phase B ledger row cited:    [Maintenance / Incident exposure / Integration cost / Regression risk]
Net direction for that row:  [WORSE / BETTER / NEUTRAL — from Phase B table]
Budget strength cited:       [HIGH / MEDIUM / LOW — from Phase B terminal field]

C2 RESULT: SATISFIED
```

If the role cannot cite a specific Phase B row and Net direction, replace the final line
with:
`C2 RESULT: UNSATISFIED -- [ledger row or Net direction missing]`
A role section with UNSATISFIED cannot advance to findings. A role section missing the C2
block entirely produces no result token — absence is treated as UNSATISFIED.

Sequence across roles: security/compliance → domain-specific → PM/TPM.

**Domain-lens gate (applied per finding before writing):**

```
Step A: "Would only [this role] raise this finding, given their domain?"
  YES → domain-loaded. Include the finding.
  NO  → any generic reviewer could write this. Go to Step B.

Step B: Revise to name a specific mechanism, path, function, or contract owned by this
  role's domain — unreachable without it. Re-execute Step A.
  Still NO → drop the finding.
```

Per-role template:

```
## Phase C: [Role Name]

Source files:   [files from Phase A routing that triggered this role]
Orientation:    [one phrase from .roles/]

[C2 COMPLIANCE BLOCK — completed block from above, ending in C2 RESULT token]

IA cost anchor (demonstrates Phase B read):
  Ledger row cited:      [same row as C2 compliance block]
  Net direction:         [WORSE / BETTER / NEUTRAL]
  Budget strength:       [HIGH / MEDIUM / LOW]
  This role [confirms / disputes] that Net direction because:
    [names the code surface, function, or mechanism — not role perspective or priority]

Findings: [all passed domain-lens gate]
F-01 [P1/P2/P3] [domain-specific finding]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second finding]
     Owner: [role] | Resolution: [action]
[minimum 2]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

Phase C exit: C1 block ends in `C1 RESULT: ALL CLEAR`; every role's C2 block ends in
`C2 RESULT: SATISFIED`; every finding passed Step A of the domain-lens gate.

---

**PHASE D — SYNTHESIS**

Entry: Phase C exit met.

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

Perspective-label ban-to-fix:

| Banned (do not write) | Required replacement form |
|---|---|
| "they have different perspectives" | "[role-A] sees [code mechanism X]; [role-B] sees [code mechanism Y]" |
| "they prioritize differently" | "[path X] is inside [role-A]'s domain and outside [role-B]'s" |
| "they see this through different lenses" | "the change affects [mechanism A] (in [role-A]'s domain) and [mechanism B] (in [role-B]'s domain)" |
| "from [role]'s perspective" as sole cause | name the architectural fact causing risk |
| "their roles lead them to different conclusions" | "[role-A]'s scope includes [code surface X]; [role-B]'s does not" |

Phase D exit: all Mechanism lines pass the ban-to-fix check.

---

**PHASE E — DECISION**

Entry: Phase D exit met.

```
## Phase E: Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from [role]] — [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] — sign-off: [role who confirms before merge]
2. [additional condition] — sign-off: [role]
```

One decision. Values: GO, NO-GO, GO WITH CONDITIONS. Delegated decisions fail.

Phase E exit: exactly one decision with value, justification, and sign-off roles.

---

**AMEND**

When invoked with an AMEND directive, output this named-field block before Phase A.

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

## V-03 — Role Sequence: C-27 PRE-COMMITMENT Block Structurally Before Findings

**Axis**: Role sequence
**Hypothesis**: R7 V-03 required the READ RECEIPT (including the initial position) to be
written before re-reading the PR diff. The gap: the initial position is the fifth field
inside the receipt template — it appears at the same structural level as the Budget verdict
restatement and Budget strength. There is no element in the output text that separates
"what I knew before the diff" from "what the diff changed." A role could write the receipt
template after findings, fill the initial position field consistently, and satisfy all
field-presence checks — the output would pass a structural inspection because all fields are
present. R8 V-03 adds a distinct `PRE-COMMITMENT:` labeled block that is a separate named
output element following the receipt and preceding the findings table. The initial position
moves from the receipt into this block. PRE-COMMITMENT contains three fields: the cost row
assessed, the initial position on that row, and the basis for that position (domain knowledge
only — the diff has not been read for findings yet). Post-findings, the IA cost anchor states
whether the pre-committed position changed or held, naming the code artifact that caused or
confirmed the position. The structural ordering — receipt → PRE-COMMITMENT → findings — is
independently verifiable by reading the output text top-to-bottom.

---

You are running `/corps-pr`. Follow each numbered step exactly. Fill every named field and
template slot. A missing PRE-COMMITMENT block or absent post-findings delta is a structural
output failure regardless of finding quality.

**READ INPUTS**

Read: `org.yaml`, PR diff, `.roles/`.

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

The IA section appears first. Fill the cost ledger completely. The Budget verdict appears as
three separate labeled lines below the separator — one line per clause.

```
## Inertia Advocate

Null hypothesis: The codebase currently [does X via mechanism Y].

Cost ledger:

| Cost Category     | Current-State Cost                                        | Adoption Cost (this PR)                          | Net                      |
|-------------------|-----------------------------------------------------------|--------------------------------------------------|--------------------------|
| Maintenance       | [LOW/MED/HIGH — maintaining current path]                 | [maintaining new path post-merge]                | WORSE / BETTER / NEUTRAL |
| Incident exposure | [failure risk/severity under status quo]                  | [residual exposure after merge]                  | WORSE / BETTER / NEUTRAL |
| Integration cost  | [coordination overhead of current approach]               | [churn, downstream wiring, test burden]          | WORSE / BETTER / NEUTRAL |
| Regression risk   | [risk of new failures from current approach as-is]        | [risk introduced by this PR]                     | WORSE / BETTER / NEUTRAL |

---
WORSE rows: [Cost Categories where Net = WORSE, or "none"]
BETTER rows: [Cost Categories where Net = BETTER, or "none"]
Conclusion: [one sentence — is adoption justified?]

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

**3A — IA READ RECEIPT (write immediately after reading the IA section)**

The READ RECEIPT documents that Phase 2 was read. Fill every field accurately. Do not
use placeholder text. This block comes before the PRE-COMMITMENT block.

```
## IA READ RECEIPT — [Role Name]

Section read:          Phase 2 — Inertia Advocate
Budget verdict:
  WORSE rows:          [restate from Phase 2 — verbatim]
  BETTER rows:         [restate from Phase 2 — verbatim]
  Conclusion:          [restate Phase 2 Conclusion line accurately]
Budget strength:       HIGH / MEDIUM / LOW [from Phase 2 terminal field]
```

**3B — PRE-COMMITMENT (write BEFORE reading PR diff for findings)**

The PRE-COMMITMENT block is a distinct named element in the output text. It appears after
the READ RECEIPT and before the findings table. This ordering is the verifiability contract:
a reader can confirm the pre-commitment preceded findings by reading the output top-to-bottom.

Write the PRE-COMMITMENT block immediately after completing 3A, before examining the PR diff
for findings. The initial position is a prior based on domain knowledge and the IA's cost
estimate alone — the diff has not yet been read for findings purposes.

```
PRE-COMMITMENT: [Role Name]

Cost row assessed:    [Maintenance / Incident exposure / Integration cost / Regression risk]
Initial position:     [CONFIRMS Net direction / DISPUTES Net direction] — [one phrase stating
                      this role's expectation about the cited row, based on domain knowledge
                      and the IA's cost estimate; no finding has been generated yet]
Basis:                Domain knowledge only — PR diff not yet examined for findings.
                      [One sentence naming the domain mechanism this role expects to be
                      relevant, before reading the diff. Must name a code surface or
                      architectural pattern, not a process concern.]
```

The PRE-COMMITMENT block is sealed at this point. Do not revise it after findings
are generated. It is a pre-commitment artifact — its value comes from being written before
the diff is read.

**3C — FINDINGS AND POST-COMMITMENT DELTA**

Now examine the PR diff for this role. Apply the domain-lens gate per finding:

```
Step A: "Would only [this role] raise this finding, given their domain?"
  YES → domain-loaded. Include the finding.
  NO  → Go to Step B.

Step B: Revise to name a specific mechanism owned by this role's domain.
  Re-execute Step A. Still NO → drop the finding.
```

Then write the findings, followed by the IA cost anchor with post-commitment delta:

```
## Review: [Role Name]

[Reference to READ RECEIPT and PRE-COMMITMENT blocks above]

Findings: [all passed domain-lens gate]
F-01 [P1/P2/P3] [domain-specific finding]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second finding]
     Owner: [role] | Resolution: [action]
[minimum 2]

Summary: [N] findings — [x] P1, [y] P2, [z] P3

IA cost anchor — post-findings delta:
  Pre-committed position:   [CONFIRMS / DISPUTES] [Cost row from PRE-COMMITMENT block]
  Position after findings:  [HELD / CHANGED]
  If HELD:   [name the code artifact from the diff that confirmed the pre-committed position]
  If CHANGED: [name the code artifact from the diff that caused the position to change, and
              state the revised position in one sentence]
```

The post-findings delta is a required output field. A role that fills the HELD/CHANGED
field with a placeholder or omits it entirely fails the delta requirement — the artifact
citation is what makes the delta verifiable.

---

**STEP 4 — CONSENSUS SYNTHESIS**

After all role sections are complete:

```
## Consensus

IA cost ledger: Budget strength was [HIGH / MEDIUM / LOW].
  WORSE rows were: [restate]. BETTER rows were: [restate].
  Technical roles collectively [reinforced / challenged / defeated] the IA's cost estimate.
  Net: [one sentence — does the benefit case exceed the cost budget?]

Agreement: [area] — [role-A] and [role-B] independently raised [concern]

Divergence: [role-A] rates [area] P[N]; [role-B] rates P[N].
  Mechanism: [structural or architectural property of the code causing the difference]

Critical: [F-XX from role] — [why this finding most threatens the merge]
```

Perspective-label ban — scan every Mechanism line before writing:

- `[ ]` "they have different perspectives" — BANNED
- `[ ]` "they prioritize differently" — BANNED
- `[ ]` "they see this through different lenses" — BANNED
- `[ ]` "their roles lead them to different conclusions" — BANNED
- `[ ]` "from [role]'s perspective" as the sole cause — BANNED

---

**STEP 5 — DECISION**

```
## Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary reason: [F-XX from [role]] — [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] — sign-off: [role]
2. [additional condition] — sign-off: [role]
```

Exactly one decision. Delegated decisions fail. Hedged decisions fail.

---

**AMEND**

When invoked with an AMEND directive, output this named-field block BEFORE STEP 1.

```
## AMEND SCOPE

What was amended:           [description]
Roles added:                [list, or "none"]
Roles removed:              [list, or "none"]
Files triggering addition:  [list, or "n/a — scope change was manually directed"]
Prior findings superseded:  [F-IDs, or "none — first run"]
```

Run STEPS 1–5 with the amended scope.

---

## V-04 — Combination: C-25 String-Matchable Verdict + C-26 Exact Result Tokens

**Axis**: Inertia framing + Lifecycle emphasis
**Hypothesis**: V-01 required the Budget verdict to appear as three separate labeled lines
(C-25). V-02 required C1 and C2 to produce exact result tokens (C-26). The combination:
B3 in the C1 pre-flight checklist now explicitly verifies "three labeled lines present —
WORSE rows:, BETTER rows:, Conclusion: each on own line." C2 per-role compliance cites
the WORSE rows and BETTER rows verbatim from those lines, making C2 a direct quotation of
the B3 string-matchable structure. The chain is: three-clause labeled lines (C-25) → B3
checks those lines (C1 pre-flight) → C2 per-role cites those lines → result tokens
confirm both checks. A B3 failure blocks Phase C at C1; a C2 citation failure is visible
as `C2 RESULT: UNSATISFIED`. No supplementary text appears after any result token.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline. Read the pipeline
declaration before producing any output. Each phase begins only when entry conditions are met.

---

**PIPELINE DECLARATION**

```
Phase A — Route
  Entry:    org.yaml + PR diff + .roles/ loaded
  Exit:     Routing table complete; every file has a row; every role cites exact scope
            pattern; coverage gaps declared
  Gates:    C-01, C-06

Phase B — Inertia Review
  Entry:    Phase A exit met
  Exit:     (B1) Null hypothesis stated
            (B2) Cost ledger: 4 rows × 2 columns × Net direction per row
            (B3) Budget verdict: three separate labeled lines —
                 "WORSE rows: [values]" on its own line,
                 "BETTER rows: [values]" on its own line,
                 "Conclusion: [text]" on its own line
                 (not in a table cell; not merged into prose; each line independently
                 string-matchable)
            (B4) Budget strength declared as terminal field below separator
            (B5) IA verdict in cost terms
  Gates:    C-11, C-17, C-19, C-21, C-25

Phase C — Technical Reviews
  Entry:    C1 (pre-flight): verify B1–B5; output PRE-FLIGHT block ending in
              C1 RESULT: ALL CLEAR
            or C1 RESULT: BLOCKED -- [B-number that failed]
            C2 (per-role): each role cites WORSE rows and BETTER rows verbatim from
              Phase B's three labeled lines; output COMPLIANCE block ending in
              C2 RESULT: SATISFIED
            or C2 RESULT: UNSATISFIED -- [which line was not cited]
  Exit:     C1 ends in ALL CLEAR token; all C2 blocks end in SATISFIED token; all
            findings passed domain-lens gate
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26

Phase D — Synthesis
  Entry:    Phase C exit met
  Exit:     Consensus complete; all Mechanism lines pass ban-to-fix check
  Gates:    C-03, C-09, C-12, C-13

Phase E — Decision
  Entry:    Phase D exit met
  Exit:     Exactly one GO / NO-GO / GO WITH CONDITIONS; conditions name sign-off
  Gates:    C-04, C-10
```

---

**PHASE A — ROUTE**

Entry: inputs loaded.

```
## Phase A: Routing

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern] |
| (all files) | default | Inertia Advocate | default — always included |
```

Coverage gap: `COVERAGE GAP: [file] — no org.yaml scope pattern covers this path.`

---

**PHASE B — INERTIA REVIEW**

Entry: Phase A exit met.

B3 compliance requires three lines that each begin with their clause label and appear as
separate lines in the output text — not as a compound line, not as table cells, not as a
prose sentence that mentions the rows.

```
## Phase B: Inertia Advocate

Null hypothesis: The codebase currently [does X via mechanism Y].           ← B1

Cost ledger:                                                                 ← B2

| Cost Category     | Current-State Cost                                        | Adoption Cost (this PR)                          | Net                      |
|-------------------|-----------------------------------------------------------|--------------------------------------------------|--------------------------|
| Maintenance       | [LOW/MED/HIGH — maintaining current path]                 | [maintaining new path post-merge]                | WORSE / BETTER / NEUTRAL |
| Incident exposure | [failure risk/severity under status quo]                  | [residual exposure after merge]                  | WORSE / BETTER / NEUTRAL |
| Integration cost  | [coordination overhead of current approach]               | [churn, downstream wiring, test burden]          | WORSE / BETTER / NEUTRAL |
| Regression risk   | [risk of new failures from current approach as-is]        | [risk introduced by this PR]                     | WORSE / BETTER / NEUTRAL |

---
WORSE rows: [Cost Categories where Net = WORSE, or "none"]               ← B3 line 1
BETTER rows: [Cost Categories where Net = BETTER, or "none"]             ← B3 line 2
Conclusion: [one sentence — is adoption justified?]                      ← B3 line 3

Budget strength: HIGH / MEDIUM / LOW                                      ← B4

Findings:
F-01 [P1/P2/P3] [argument current state is sufficient]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second argument]
     Owner: [role] | Resolution: [action]
[minimum 2]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence in cost terms]       ← B5
```

Phase B exit: B1–B5 met; three labeled Budget verdict lines present as separate output lines.

---

**PHASE C — TECHNICAL REVIEWS**

**C1 — Phase B Exit Pre-Flight:**

Output this block before the first technical role section. B3 check requires confirming
the three labeled lines are present — scan for each line label separately.

```
## Phase C Pre-Flight (C1)

[ ] B1 — Null hypothesis stated
[ ] B2 — Cost ledger: 4 rows × 2 columns × Net direction per row filled
[ ] B3 — Budget verdict: three separate labeled lines present
         (scan: "WORSE rows:" on own line ✓/✗, "BETTER rows:" on own line ✓/✗,
         "Conclusion:" on own line ✓/✗ — all three must be ✓)
[ ] B4 — Budget strength declared as terminal field
[ ] B5 — IA verdict in cost terms

C1 RESULT: ALL CLEAR
```

If any box unchecked: `C1 RESULT: BLOCKED -- [B-number that failed]`

**C2 — IA Read Prerequisite (Per-Role):**

Each role's C2 block cites the WORSE rows and BETTER rows verbatim from Phase B's three
labeled lines. This citation is what makes C2 compliance a direct verification of B3.

```
## C2 Compliance — [Role Name]

WORSE rows cited (from Phase B):  [copy verbatim from Phase B "WORSE rows:" line]
BETTER rows cited (from Phase B): [copy verbatim from Phase B "BETTER rows:" line]
Budget strength cited:            [HIGH / MEDIUM / LOW — from Phase B]
Ledger row most relevant:         [Maintenance / Incident exposure / Integration cost / Regression risk]
Net direction for that row:       [WORSE / BETTER / NEUTRAL — from Phase B table]

C2 RESULT: SATISFIED
```

If verbatim citation is absent or row/Net direction missing:
`C2 RESULT: UNSATISFIED -- [WORSE rows line / BETTER rows line / ledger row / Net direction — whichever is missing]`

Domain-lens gate (Phase C exit condition per finding):

```
Step A: "Would only [this role] raise this finding?"  YES → write it.  NO → Step B.
Step B: Revise to name domain-owned mechanism. Re-execute Step A.  Still NO → drop.
```

Per-role template:

```
## Phase C: [Role Name]

Source files:  [from Phase A routing]
Orientation:   [one phrase from .roles/]

[C2 COMPLIANCE BLOCK ending in C2 RESULT token]

IA cost anchor:
  Row cited:       [same as C2 block]
  Net direction:   [WORSE / BETTER / NEUTRAL]
  Budget strength: [HIGH / MEDIUM / LOW]
  This role [confirms / disputes] that direction because:
    [names code artifact — not role perspective or priority]

Findings: [all passed domain-lens gate]
F-01 [P1/P2/P3] [domain-specific finding]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second finding]
     Owner: [role] | Resolution: [action]
[minimum 2]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

Phase C exit: C1 ends in `C1 RESULT: ALL CLEAR`; every C2 ends in `C2 RESULT: SATISFIED`.

---

**PHASE D — SYNTHESIS**

```
## Phase D: Consensus

IA cost ledger: Budget strength was [HIGH / MEDIUM / LOW].
  WORSE rows: [restate]. BETTER rows: [restate].
  Technical roles collectively [reinforced / challenged / defeated] the IA's estimate.
  Net: [one sentence]

Agreement: [area] — [role-A] and [role-B] raised [concern]

Divergence: [role-A] rates P[N]; [role-B] rates P[N].
  Mechanism: [architectural property — not perspective difference]

Critical: [F-XX from role] — [why this most threatens the merge]
```

Perspective-label ban:

| Banned | Replacement form |
|---|---|
| "they have different perspectives" | "[role-A] sees [mechanism X]; [role-B] sees [mechanism Y]" |
| "they prioritize differently" | "[path X] is in [role-A]'s domain, outside [role-B]'s" |
| "they see this through different lenses" | "change affects [A] in [role-A]'s domain and [B] in [role-B]'s" |
| "from [role]'s perspective" as sole cause | name the architectural fact causing risk |
| "their roles lead them to different conclusions" | "[role-A]'s scope includes [surface X]; [role-B]'s does not" |

---

**PHASE E — DECISION**

```
## Phase E: Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from role] — [one sentence]

Conditions (if GO WITH CONDITIONS):
1. [what must be resolved] — sign-off: [role]
```

One decision. Delegated or hedged decisions fail.

---

**AMEND**

Before Phase A if AMEND directive received:

```
## AMEND SCOPE

What was amended:           [description]
Roles added:                [list, or "none"]
Roles removed:              [list, or "none"]
Files triggering addition:  [list, or "n/a — manually directed"]
Prior findings superseded:  [F-IDs, or "none — first run"]
```

---

## V-05 — Full R8 Integration: C-25 + C-26 + C-27

**Axis**: Inertia framing + Lifecycle emphasis + Role sequence
**Hypothesis**: V-01 (C-25), V-02 (C-26), and V-03 (C-27) each address one structural gap
from R7. V-05 integrates all three: the Budget verdict appears as three separate labeled
lines (C-25) → C1 verifies those lines and outputs `C1 RESULT: ALL CLEAR` (C-26/C1) → each
role writes a PRE-COMMITMENT block before the diff is read (C-27), then a C2 compliance
block citing the WORSE/BETTER lines verbatim ending in `C2 RESULT: SATISFIED` (C-26/C2) →
findings are written → the post-commitment delta names the code artifact that held or
changed the pre-committed position. The three mechanisms are independent: C-25 is output
structure, C-26 is token compliance, C-27 is timing. Together they close three verification
gaps: row-citation parsability, sub-condition visibility, and pre-commitment integrity.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline with three structural
compliance mechanisms active: string-matchable Budget verdict (C-25), named result tokens
(C-26), and PRE-COMMITMENT blocks (C-27). Read the full pipeline declaration before
producing any output.

---

**PIPELINE DECLARATION**

```
Phase A — Route
  Entry:    org.yaml + PR diff + .roles/ loaded
  Exit:     Routing table complete; every file has a row; every role cites exact scope
            pattern; coverage gaps declared
  Gates:    C-01, C-06

Phase B — Inertia Review
  Entry:    Phase A exit met
  Exit:     (B1) Null hypothesis stated
            (B2) Cost ledger: 4 rows × 2 columns × Net direction per row filled
            (B3) Budget verdict as three separate labeled lines in the output text:
                 line starting "WORSE rows:", line starting "BETTER rows:",
                 line starting "Conclusion:" — each on its own line, independently
                 string-matchable [C-25]
            (B4) Budget strength terminal field below separator
            (B5) IA verdict in cost terms
  Gates:    C-11, C-17, C-19, C-21, C-25

Phase C — Technical Reviews
  Entry:    Two sub-conditions, each producing an exact result token [C-26]:
            C1 (Phase B exit pre-flight):
              B1–B5 checklist, including B3 three-line scan.
              Terminal line: C1 RESULT: ALL CLEAR
              or             C1 RESULT: BLOCKED -- [B-number]
            C2 (per-role IA read prerequisite):
              Each role writes PRE-COMMITMENT block [C-27] before reading diff,
              then C2 compliance block citing WORSE/BETTER lines verbatim.
              Terminal line per role: C2 RESULT: SATISFIED
              or                     C2 RESULT: UNSATISFIED -- [what is missing]
  Exit:     C1 ends in ALL CLEAR; all C2 blocks end in SATISFIED; PRE-COMMITMENT blocks
            precede findings tables; all findings passed domain-lens gate
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26, C-27

Phase D — Synthesis
  Entry:    Phase C exit met
  Exit:     Consensus complete; all Mechanism lines pass ban-to-fix check
  Gates:    C-03, C-09, C-12, C-13

Phase E — Decision
  Entry:    Phase D exit met
  Exit:     Exactly one GO / NO-GO / GO WITH CONDITIONS; conditions name sign-off
  Gates:    C-04, C-10
```

---

**PHASE A — ROUTE**

Entry: inputs loaded.

```
## Phase A: Routing

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern] |
| (all files) | default | Inertia Advocate | default — always included |
```

Coverage gap: `COVERAGE GAP: [file] — no org.yaml scope pattern covers this path.`

Phase A exit: complete.

---

**PHASE B — INERTIA REVIEW**

Entry: Phase A exit met.

The Budget verdict appears as three separate labeled output lines below the separator.
Each line begins with its clause label. No clause appears inside a table cell, inside
the Conclusion of another clause, or merged with another clause on the same line.

```
## Phase B: Inertia Advocate

Null hypothesis: The codebase currently [does X via mechanism Y].           ← B1

Cost ledger:                                                                 ← B2

| Cost Category     | Current-State Cost                                        | Adoption Cost (this PR)                          | Net                      |
|-------------------|-----------------------------------------------------------|--------------------------------------------------|--------------------------|
| Maintenance       | [LOW/MED/HIGH — maintaining current path]                 | [maintaining new path post-merge]                | WORSE / BETTER / NEUTRAL |
| Incident exposure | [failure risk/severity under status quo]                  | [residual exposure after merge]                  | WORSE / BETTER / NEUTRAL |
| Integration cost  | [coordination overhead of current approach]               | [churn, downstream wiring, test burden]          | WORSE / BETTER / NEUTRAL |
| Regression risk   | [risk of new failures from current approach as-is]        | [risk introduced by this PR]                     | WORSE / BETTER / NEUTRAL |

---
WORSE rows: [Cost Categories where Net = WORSE, or "none"]               ← B3 line 1 [C-25]
BETTER rows: [Cost Categories where Net = BETTER, or "none"]             ← B3 line 2 [C-25]
Conclusion: [one sentence — is adoption justified?]                      ← B3 line 3 [C-25]

Budget strength: HIGH / MEDIUM / LOW                                      ← B4

Findings:
F-01 [P1/P2/P3] [argument current state is sufficient]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second argument grounded in cost ledger]
     Owner: [role] | Resolution: [action]
[minimum 2]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence in cost terms]       ← B5
```

Phase B exit: B1–B5 met; three Budget verdict lines present as separate output lines.

---

**PHASE C — TECHNICAL REVIEWS**

Phase C uses three structural mechanisms: C1 pre-flight (C-26/C1), PRE-COMMITMENT block
per role (C-27), and C2 compliance block per role (C-26/C2). All three must be present
and passing before findings are written.

**C1 — Phase B Exit Pre-Flight [C-26/C1]:**

Output this block before the first role section. B3 check requires scanning for all three
Budget verdict lines — confirm each label appears on its own line.

```
## Phase C Pre-Flight (C1)

[ ] B1 — Null hypothesis stated
[ ] B2 — Cost ledger: 4 rows × 2 columns × Net direction per row filled
[ ] B3 — Budget verdict: three labeled lines present as separate output lines
         Scan: "WORSE rows:" on own line ✓/✗
               "BETTER rows:" on own line ✓/✗
               "Conclusion:" on own line ✓/✗
         All three must be ✓
[ ] B4 — Budget strength terminal field below separator
[ ] B5 — IA verdict in cost terms

C1 RESULT: ALL CLEAR
```

If any box unchecked: `C1 RESULT: BLOCKED -- [B-number and what failed]`

Phase C cannot advance until C1 RESULT: ALL CLEAR appears in the output.

**Per-Role Structure — 3A → 3B → 3C:**

For each role, in order: security/compliance → domain-specific → PM/TPM.

**3A — IA READ RECEIPT (written immediately after reading Phase B):**

```
## IA READ RECEIPT — [Role Name]

Section read:     Phase B — Inertia Advocate
WORSE rows:       [restate Phase B "WORSE rows:" line verbatim]
BETTER rows:      [restate Phase B "BETTER rows:" line verbatim]
Conclusion:       [restate Phase B "Conclusion:" line accurately]
Budget strength:  HIGH / MEDIUM / LOW [from Phase B terminal field]
```

**3B — PRE-COMMITMENT (written after 3A, before reading diff for findings) [C-27]:**

The PRE-COMMITMENT block is a distinct named element in the output text. It follows the
READ RECEIPT and precedes the findings table. Write it now, before examining the PR diff
for this role's findings. The initial position is based on the Phase B cost ledger and
domain knowledge alone — no findings have been generated yet.

```
PRE-COMMITMENT: [Role Name]

Cost row assessed:  [Maintenance / Incident exposure / Integration cost / Regression risk]
Initial position:   [CONFIRMS / DISPUTES] [Net direction from Phase B] on [Cost row]
                    [one phrase stating the expectation — based on domain knowledge
                     and Phase B cost ledger; PR diff not yet examined for findings]
Basis:              Domain knowledge only. PR diff not examined.
                    [one sentence naming the domain mechanism this role expects to
                     be relevant — must name a code surface or architectural pattern]
```

The PRE-COMMITMENT block is sealed here. Its content is not revised after findings.

**3C — C2 COMPLIANCE BLOCK + FINDINGS [C-26/C2]:**

Now examine the PR diff. Apply the domain-lens gate per finding:

```
Step A: "Would only [this role] raise this finding, given their domain?"
  YES → include. NO → Step B.
Step B: Revise to name domain-owned mechanism. Re-execute Step A.
  Still NO → drop.
```

Write the C2 compliance block first, then findings:

```
## C2 Compliance — [Role Name]

WORSE rows cited:    [copy verbatim from Phase B "WORSE rows:" line]
BETTER rows cited:   [copy verbatim from Phase B "BETTER rows:" line]
Budget strength:     [HIGH / MEDIUM / LOW — from Phase B]
Ledger row cited:    [same row as PRE-COMMITMENT block]
Net direction:       [WORSE / BETTER / NEUTRAL — from Phase B table]

C2 RESULT: SATISFIED
```

If verbatim citation absent or row/Net direction missing:
`C2 RESULT: UNSATISFIED -- [specify: WORSE rows line / BETTER rows line / ledger row / Net direction]`

Then write the findings table and post-commitment delta:

```
## Phase C: [Role Name]

Source files:  [from Phase A routing]
Orientation:   [one phrase from .roles/]

[READ RECEIPT — 3A above]
[PRE-COMMITMENT — 3B above]
[C2 COMPLIANCE — result token above]

Findings: [all passed domain-lens gate]

| ID | Severity | Finding | Domain-Lens | Owner | Resolution |
|----|----------|---------|-------------|-------|------------|
| F-01 | P1/P2/P3 | [finding — names mechanism in this role's domain] | Passed | [role] | [action] |
| F-02 | P1/P2/P3 | [second finding] | Passed | [role] | [action] |
[minimum 2]

Summary: [N] findings — [x] P1, [y] P2, [z] P3

Post-commitment delta:
  Pre-committed:     [CONFIRMS / DISPUTES] [Cost row] (from PRE-COMMITMENT block)
  After findings:    [HELD / CHANGED]
  If HELD:           [name code artifact from diff that confirmed the position]
  If CHANGED:        [name code artifact that changed it; state revised position]
```

The Domain-Lens column must appear in every findings table with a gate compliance value
per finding. A table without the Domain-Lens column fails C-24 for this role.

Phase C exit: C1 `ALL CLEAR`; every C2 `SATISFIED`; every PRE-COMMITMENT precedes its
findings table; every finding has a Domain-Lens gate value.

---

**PHASE D — SYNTHESIS**

Entry: Phase C exit met.

```
## Phase D: Consensus

IA cost ledger: Budget strength was [HIGH / MEDIUM / LOW].
  WORSE rows were: [restate]. BETTER rows were: [restate].
  Technical roles collectively [reinforced / challenged / defeated] the IA's estimate.
  Net: [one sentence]

Agreement: [area] — [role-A] and [role-B] independently raised [concern]

Divergence: [role-A] rates [area] P[N]; [role-B] rates P[N].
  Mechanism: [architectural property of the code causing the difference — not perspective]

Critical: [F-XX from role] — [why this most threatens the merge]
```

Perspective-label ban-to-fix:

| Banned | Replacement |
|---|---|
| "they have different perspectives" | "[role-A] sees [mechanism X]; [role-B] sees [mechanism Y]" |
| "they prioritize differently" | "[path X] is in [role-A]'s domain, outside [role-B]'s" |
| "they see this through different lenses" | "change affects [A] in [role-A]'s domain and [B] in [role-B]'s" |
| "from [role]'s perspective" as sole cause | name the architectural fact |
| "their roles lead them to different conclusions" | "[role-A]'s scope includes [surface X]; [role-B]'s does not" |

A Mechanism line with a banned phrase fails even if a code mechanism is also named.

Phase D exit: consensus complete; all Mechanism lines pass.

---

**PHASE E — DECISION**

Entry: Phase D exit met.

```
## Phase E: Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from role] — [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] — sign-off: [role who confirms before merge]
2. [additional condition] — sign-off: [role]
```

One decision. Values: GO, NO-GO, GO WITH CONDITIONS only.
Delegated decisions fail. Hedged decisions fail.

Phase E exit: exactly one decision with value, justification, and sign-off roles.

---

**AMEND**

When invoked with an AMEND directive, output this named-field block before Phase A.
All fields mandatory; write "none" if not applicable.

```
## AMEND SCOPE

What was amended:           [description]
Roles added:                [list, or "none"]
Roles removed:              [list, or "none"]
Files triggering addition:  [list, or "n/a — manually directed"]
Prior findings superseded:  [F-IDs, or "none — first run"]
```

Run Phases A–E with the amended scope.
