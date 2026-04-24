# corps-pr — Round 9 Variations (V-01 through V-05)

---

## V-01

**Variation axis:** Inertia framing
**Hypothesis:** Framing the IA explicitly as a *budget authority* with a mandatory cost ledger — and requiring the ledger verdict to appear in each technical role's finding body text, not as a section header — will close C-31 while advancing C-17, C-19, C-21, C-25, C-28.

---

```markdown
# /corps-pr

Run a PR through the full organizational review. Each role examines the
diff from its domain lens. Output: per-role findings table, consensus
analysis, and a single go/no-go recommendation.

---

## STEP 1 — READ ORG YAML

Read `org.yaml`. Extract:
- All defined roles and their domain scope
- Committee definitions
- Inertia Advocate configuration (IA role name, cost framing defaults)

---

## STEP 2 — AMEND CHECK

If the invocation includes an AMEND directive, output the following
structured block before any other output:

```
AMEND SCOPE DISCLOSURE
----------------------
(a) Amendment: [what was changed — added reviewer / changed scope]
(b) Roles added: [list, or "none"]
(c) Roles removed: [list, or "none"]
(d) Prior findings superseded: [finding IDs from previous run, or "none"]
```

A run without an AMEND directive skips this block entirely.

---

## STEP 3 — REVIEWER ROUTING

Examine the PR diff. For each file changed, identify which role domains
are touched. Activate roles whose scope covers at least one changed file.
Always activate the Inertia Advocate as the first reviewer when the IA
role is defined in org.yaml.

Output a routing summary:

```
ROUTING SUMMARY
---------------
Files changed: [count]
Roles activated: [list in activation order, IA first]
Routing rationale: [one line per role naming the files that triggered it]
```

---

## STEP 4 — INERTIA ADVOCATE REVIEW (runs before all technical roles)

The Inertia Advocate is the status quo's budget authority. Their job is
not to list risks — it is to state what the current system costs to
maintain and what this change costs to adopt, expressed as a cost ledger.

### 4a — Cost Ledger

Output the following ledger table:

| Cost Row           | Current-State Cost | Adoption Cost | Net Direction |
|--------------------|--------------------|---------------|---------------|
| Maintenance burden | [value]            | [value]       | WORSE / BETTER / NEUTRAL |
| Incident exposure  | [value]            | [value]       | WORSE / BETTER / NEUTRAL |
| [additional rows]  | [value]            | [value]       | WORSE / BETTER / NEUTRAL |

Net Direction must be one of: WORSE, BETTER, NEUTRAL. Every row requires
a value in all three columns. No empty cells.

### 4b — Budget Verdict (three-clause formula)

After the cost ledger, output the Budget verdict using exactly this
structure. Each clause appears on its own line with no other label or
value on the same line:

```
WORSE rows: [list rows where Net Direction = WORSE, or "none"]
BETTER rows: [list rows where Net Direction = BETTER, or "none"]
Conclusion: [verdict text — the IA's tradeoff conclusion derived from the named rows]
```

The Conclusion must cite which rows drove it. A Conclusion not grounded
in the named rows fails the three-clause formula requirement.

### 4c — Budget Strength

Output a terminal field:

```
Budget strength: [LOW / MEDIUM / HIGH — confidence level of the IA position]
```

---

## STEP 5 — TECHNICAL ROLE REVIEWS

For each activated technical role (in routing order, after the IA):

### 5a — PRE-COMMITMENT Block

Before reading the PR diff for findings, output:

```
PRE-COMMITMENT: [Role Name]
---------------------------
(a) IA section read: [yes/no]
(b) Budget verdict restated: [restate WORSE rows / BETTER rows / Conclusion accurately]
(c) Budget strength: [value from IA terminal field]
(d) Cost row most relevant to this domain: [row name from IA ledger]
(e) Initial position on that row: [this role's pre-analysis position — AGREE / DISAGREE / PARTIAL]

[PRE-COMMITMENT SEALED]
```

The `[PRE-COMMITMENT SEALED]` token must appear as a distinct output line
closing the block. No PR diff file, function, or line reference may appear
before this token.

### 5b — Findings Table

Output findings as a named-field table with a Domain-Lens column:

| ID   | Severity | Location | Description | Domain-Lens Gate |
|------|----------|----------|-------------|-----------------|
| F-01 | P1/P2/P3 | file:line | [description] | Passed |

**Domain-Lens Gate rule:** For each finding, ask: "Would only this role
raise this finding given their domain?" If any generic reviewer could
write the same sentence, revise it before including it. Mark the gate
result as "Passed" only after applying this test. A finding that fails
the gate is rewritten or dropped — it does not enter the table with a
"Failed" marker.

**IA Counterpoint requirement (C-31):** For at least one finding in this
role's table, the Description field must name the Inertia Advocate's
cost position AND this role's disagreeing mechanism in the same field.
The IA counterpoint appears inside the Description text of a specific
finding — not as a separate section header, not as an "IA Position:"
block above or below the table. Example Description text:

> "IA rates maintenance burden NEUTRAL (no additional burden cited);
> compiler-lead rates P1 because the new codegen path at src/emit.ts:144
> bypasses the existing null-guard and will surface as silent truncation
> under concurrent emit."

This format binds the IA cost position and the role's disagreeing
mechanism into one auditable finding body.

### 5c — Role Summary Line

After the findings table, output:

```
[Role name] total: [N] findings — [x] P1, [y] P2, [z] P3
```

---

## STEP 6 — CONSENSUS ANALYSIS

For each finding where two or more roles diverge in severity:

1. Name the finding and the severity ratings assigned by each role.
2. Identify the architectural mechanism that explains the divergence —
   not the difference in perspective, not the difference in priorities,
   but the structural or code-level reason one role sees higher risk.
   Example: "compiler-lead rates P1 because the change bypasses the
   null-guard at src/emit.ts:144; tpm rates P3 because no user-facing
   path exercises the concurrent emit branch."
3. The consensus section must not use perspective-label explanations.
   Prohibited phrase surface forms (enumerated ban list):
   - "they see this differently because of their role"
   - "this is a matter of perspective"
   - "compiler-lead prioritizes differently than tpm"
   - "it depends on which lens you use"
   Any explanation that could be written by substituting role names
   without changing the mechanism description fails the ban list test.

---

## STEP 7 — GO/NO-GO RECOMMENDATION

Output one of:
- **GO** — no blocking findings remain after consensus
- **GO WITH CONDITIONS** — merge allowed after named conditions are met;
  each condition names: (a) what must be resolved, (b) which role must
  confirm resolution before merge
- **NO-GO** — blocking finding(s) prevent merge; name each blocker

---

## AMEND MODE

When invoked with `AMEND: add [role]` — run only the added role's review
against the existing diff. Output the AMEND SCOPE DISCLOSURE block (Step 2)
before any role output. The added role follows the same PRE-COMMITMENT →
Findings → Summary sequence as Step 5.

When invoked with `AMEND: scope=[domain]` — re-run routing limited to the
named domain. Output the AMEND SCOPE DISCLOSURE block stating which roles
were deactivated and which prior findings are superseded.
```

---

## V-02

**Variation axis:** Lifecycle emphasis
**Hypothesis:** Making the review pipeline explicit as named phases with entry/exit conditions — and making Phase C's entry a dual-clause sub-condition that outputs C1 RESULT and C2 RESULT lines — will close C-18, C-22, C-26, C-30 while creating the structural context that makes C-31 and C-32 enforceable.

---

```markdown
# /corps-pr

Run a PR through the full organizational review as a four-phase pipeline.
Each phase has named entry and exit conditions. No phase begins until its
entry condition is satisfied. No phase ends until its exit condition is met.

---

## PIPELINE DECLARATION

```
Phase A — Routing
  Entry: PR diff is available; org.yaml is readable
  Exit:  Routing summary output; all activated roles listed; IA sequenced first
  Gates: C-01 (role selection), C-02 (routing rationale)

Phase B — IA Review (Inertia Advocate)
  Entry: Phase A exited
  Exit:  Cost ledger complete; Budget verdict output as three-clause formula;
         Budget strength field present; PRE-COMMITMENT blocks precede findings tables
  Gates: C-11, C-17, C-19, C-21, C-25, C-27, C-28, C-29, C-30

Phase C — Technical Role Reviews
  Entry (two independently auditable sub-conditions):
    C1: Phase B pre-flight checklist — ALL of the following must be true before Phase C starts:
        [ ] Cost ledger has at least two named rows (maintenance burden, incident exposure)
        [ ] Budget verdict contains all three labeled clauses (WORSE rows / BETTER rows / Conclusion)
        [ ] Budget strength field is present
        [ ] PRE-COMMITMENT blocks for Phase B are sealed before any diff content
        Blocked items prevent Phase C from starting.
        Output: C1 RESULT: ALL CLEAR  — or —  C1 RESULT: BLOCKED -- [item that failed]
    C2: Per-role IA read prerequisite — before each role generates findings:
        The role cites specific Phase B content (Budget verdict text, cost row, Budget strength)
        A role section missing these citations fails C2 for that role independently.
        Output per role: C2 RESULT: SATISFIED  — or —  C2 RESULT: UNSATISFIED -- [citation missing]
  Exit:  All role findings tables complete; per-role summary lines present;
         domain-lens gate applied to every finding;
         at least one finding per role contains an IA counterpoint in its body text;
         PRE-COMMITMENT blocks precede findings tables (Phase C exit compliance item)
  Gates: C-14, C-15, C-18, C-20, C-22, C-23, C-24, C-26, C-30, C-31, C-32

Phase D — Synthesis
  Entry: Phase C exited; all role summaries present
  Exit:  Consensus analysis complete; divergence explanations name architectural mechanisms;
         go/no-go recommendation output with conditions named
  Gates: C-09, C-10, C-12, C-13
```

---

## PHASE A — ROUTING

Read `org.yaml`. Identify all roles and their domain scope.

Examine the PR diff. Activate roles whose scope covers at least one
changed file. Activate the Inertia Advocate first, always, if defined.

```
ROUTING SUMMARY
---------------
Files changed: [count]
Roles activated: [IA first, then technical roles in order]
Routing rationale:
  - [Role]: triggered by [file(s)]
```

Phase A exit check: routing summary output, IA sequenced first.

---

## PHASE B — IA REVIEW

The Inertia Advocate does not list concerns. They hold a budget authority
position: what does the current system cost to maintain, and what does
this change cost to adopt?

### Cost Ledger

| Cost Row           | Current-State Cost | Adoption Cost | Net Direction |
|--------------------|--------------------|---------------|---------------|
| Maintenance burden | [value]            | [value]       | WORSE / BETTER / NEUTRAL |
| Incident exposure  | [value]            | [value]       | WORSE / BETTER / NEUTRAL |
| [additional rows as warranted] | [value] | [value] | WORSE / BETTER / NEUTRAL |

### Budget Verdict

Each labeled clause on its own line, independently retrievable by
line-scan. No two clauses share a line. No clause is embedded in prose:

```
WORSE rows: [list, or "none"]
BETTER rows: [list, or "none"]
Conclusion: [verdict derived from the named row directions above]
```

### Budget Strength

```
Budget strength: [LOW / MEDIUM / HIGH]
```

Phase B exit check: cost ledger present; three-clause verdict output with
each clause on its own line; Budget strength present; PRE-COMMITMENT blocks
precede findings tables (C-30 gate item).

---

## PHASE C — TECHNICAL ROLE REVIEWS

### C1 Pre-flight Check

Before any role section begins, verify all Phase B exit conditions:

```
C1 RESULT: ALL CLEAR
```

— or if any item fails:

```
C1 RESULT: BLOCKED -- [item that failed]
```

A BLOCKED C1 RESULT halts Phase C. No technical role output is generated
until the block is resolved.

### Per-Role Structure

For each activated technical role, in this sequence:

**1. PRE-COMMITMENT Block**

Declared before any diff analysis. Closes with a seal token as a distinct
output line before any file, function, or line reference from the PR diff:

```
PRE-COMMITMENT: [Role Name]
---------------------------
(a) IA section read: yes
(b) Budget verdict: WORSE rows: [restate] / BETTER rows: [restate] / Conclusion: [restate]
(c) Budget strength: [restate value]
(d) Cost row most relevant to this domain: [row name]
(e) Initial position on that row: [AGREE / DISAGREE / PARTIAL — committed before diff analysis]

[PRE-COMMITMENT SEALED]
```

**2. C2 Result Line**

Immediately after the PRE-COMMITMENT block:

```
C2 RESULT: SATISFIED
```

— or if the block is missing Phase B content citations:

```
C2 RESULT: UNSATISFIED -- [citation missing]
```

**3. IA READ RECEIPT**

```
IA READ RECEIPT: [Role Name]
-----------------------------
(a) IA section read: [Phase B IA section]
(b) Budget verdict: [restate WORSE rows / BETTER rows / Conclusion accurately]
(c) Budget strength: [value]
(d) Cost row most relevant to this domain: see PRE-COMMITMENT block — (d) [row name]
(e) Initial position: see PRE-COMMITMENT block — (e) committed above
```

Fields (d) and (e) must either cross-reference the PRE-COMMITMENT block
by its label name, or restate their values inline. A receipt that omits
both fields entirely fails.

**4. Findings Table**

| ID   | Severity | Location | Description | Domain-Lens Gate |
|------|----------|----------|-------------|-----------------|
| F-01 | P1/P2/P3 | file:line | [text]      | Passed |

Domain-Lens Gate: ask for each finding — "Would only this role raise this
finding given their domain?" Revise or drop if generic. Gate must be
applied before writing the finding; mark "Passed" in the column as the
verification artifact.

IA Counterpoint in finding body (C-31): at least one finding's Description
field must contain the IA's cost position AND this role's disagreeing
mechanism in the same text. The IA reference belongs inside a specific
finding entry — not as a header, not as a block above or below the table.

**5. Role Summary Line**

```
[Role]: [N] findings — [x] P1, [y] P2, [z] P3
```

Phase C exit check: all role findings tables present; per-role summary
lines present; domain-lens gate applied; at least one finding per role
contains IA counterpoint in body text; PRE-COMMITMENT blocks precede
findings tables.

---

## PHASE D — SYNTHESIS

### Consensus Analysis

For each finding with role-divergent severity ratings:
- Name the finding and each role's severity rating.
- Name the architectural mechanism that explains the divergence. This is
  a structural or code-level reason — not a perspective difference.

Enumerated ban list of prohibited perspective-label forms:
1. "they see this differently because of their role"
2. "it's a matter of perspective / focus / priorities"
3. "[Role A] prioritizes [X] while [Role B] prioritizes [Y]"
4. "this depends on which lens you apply"
5. "each role has a different view of the same finding"

Any explanation that matches a ban list form is rewritten to name the
mechanism before the consensus section is complete.

### Recommendation

Output one of:
- **GO**
- **GO WITH CONDITIONS** — list each condition with (a) resolution
  required and (b) named role responsible for sign-off
- **NO-GO** — list each blocking finding

Phase D exit check: consensus analysis complete; ban list applied;
recommendation output with conditions and owners named.
```

---

## V-03

**Variation axis:** Output format
**Hypothesis:** Making every output element a named template block — with explicit field slots for the READ RECEIPT (including C-32 cross-reference syntax), the PRE-COMMITMENT seal, and the finding table's Domain-Lens column — will drive compliance through template fidelity rather than instruction-following.

---

```markdown
# /corps-pr

Produce a structured organizational PR review. All output blocks are
template-driven. Fill every named field. Do not invent new field names
or merge existing fields. A missing field is a visible gap.

---

## READ FIRST

Read `org.yaml`. Extract role definitions, domain scopes, committee
membership, and Inertia Advocate configuration.

---

## AMEND CHECK

If invoked with an AMEND directive, produce this block before all other
output. Omit entirely if no AMEND directive is present.

```
┌─ AMEND SCOPE DISCLOSURE ─────────────────────────────────────────┐
│ (a) Amendment:         [describe what was changed]               │
│ (b) Roles added:       [list, or "none"]                         │
│ (c) Roles removed:     [list, or "none"]                         │
│ (d) Findings superseded: [finding IDs from prior run, or "none"] │
└──────────────────────────────────────────────────────────────────┘
```

---

## ROUTING BLOCK

```
┌─ ROUTING SUMMARY ─────────────────────────────────────────┐
│ Files changed:   [count]                                   │
│ Roles activated: [list in order — IA first if configured]  │
│ Rationale:                                                 │
│   [Role]: triggered by [file(s)]                           │
│   [Role]: triggered by [file(s)]                           │
└───────────────────────────────────────────────────────────┘
```

---

## IA REVIEW BLOCK

Produce this block before any technical role section. The Inertia Advocate
is the status quo's budget authority.

### IA Cost Ledger

```
┌─ IA COST LEDGER ─────────────────────────────────────────────────────────┐
│ Row               │ Current-State Cost │ Adoption Cost │ Net Direction   │
│───────────────────┼────────────────────┼───────────────┼─────────────────│
│ Maintenance burden│ [value]            │ [value]       │ WORSE/BETTER/   │
│                   │                   │               │ NEUTRAL          │
│ Incident exposure │ [value]            │ [value]       │ WORSE/BETTER/   │
│                   │                   │               │ NEUTRAL          │
│ [additional row]  │ [value]            │ [value]       │ WORSE/BETTER/   │
│                   │                   │               │ NEUTRAL          │
└──────────────────────────────────────────────────────────────────────────┘
```

All cells required. Net Direction must be one of the three named values.

### IA Budget Verdict

Each clause on its own line. No two clauses share a line:

```
WORSE rows: [list all rows with Net Direction = WORSE, or "none"]
BETTER rows: [list all rows with Net Direction = BETTER, or "none"]
Conclusion: [verdict text citing which rows drove the conclusion]
```

### IA Budget Strength

```
Budget strength: [LOW / MEDIUM / HIGH]
```

---

## TECHNICAL ROLE BLOCK TEMPLATE

Repeat this complete block for each activated technical role, in routing order.

### [Role Name] — PRE-COMMITMENT

This block appears before any PR diff content is referenced. The seal
token closes the block. No file path, function name, or line number from
the PR diff may appear before the seal token.

```
┌─ PRE-COMMITMENT: [Role Name] ────────────────────────────────────┐
│ (a) IA section read: yes                                         │
│ (b) Budget verdict restated:                                     │
│     WORSE rows: [accurate restatement]                           │
│     BETTER rows: [accurate restatement]                          │
│     Conclusion: [accurate restatement]                           │
│ (c) Budget strength: [value from IA terminal field]              │
│ (d) Cost row most relevant to this domain: [row name]            │
│ (e) Initial position on that row: [AGREE / DISAGREE / PARTIAL]   │
└──────────────────────────────────────────────────────────────────┘
[PRE-COMMITMENT SEALED]
```

`[PRE-COMMITMENT SEALED]` is a required output line. It closes the block.
Everything after it may reference the PR diff.

### [Role Name] — IA READ RECEIPT

This block appears before the findings table:

```
┌─ IA READ RECEIPT: [Role Name] ───────────────────────────────────┐
│ (a) IA section read: [name the IA review section]                │
│ (b) Budget verdict: WORSE rows: [restate] / BETTER rows:         │
│     [restate] / Conclusion: [restate]                            │
│ (c) Budget strength: [value]                                     │
│ (d) Cost row most relevant: see PRE-COMMITMENT block —           │
│     (d) [row name]                                               │
│ (e) Initial position: see PRE-COMMITMENT block —                 │
│     (e) committed above                                          │
└──────────────────────────────────────────────────────────────────┘
```

Fields (d) and (e) must cross-reference the PRE-COMMITMENT block by its
label name ("PRE-COMMITMENT block") with the field letter cited, or restate
the values inline. An omission of both (d) and (e) without either form
is a receipt gap.

### [Role Name] — Findings Table

```
| ID   | Sev  | Location      | Description                                       | Domain-Lens Gate |
|------|------|---------------|---------------------------------------------------|-----------------|
| F-01 | P[n] | [file]:[line] | [text — see IA counterpoint rule below]           | Passed           |
| F-02 | P[n] | [file]:[line] | [text]                                            | Passed           |
```

**Domain-Lens Gate** (required per finding): Before writing each finding,
ask: "Would only this role raise this finding given their domain scope?"
If any generic reviewer could write the same sentence, revise it to name
the domain-specific mechanism. Gate value "Passed" appears only after
this test is applied. A finding with an empty or missing Domain-Lens cell
is incomplete.

**IA Counterpoint rule (C-31):** At least one finding in this role's table
must contain an IA counterpoint inside the Description field. The
counterpoint names: (i) the IA's specific cost position or verdict on this
area, and (ii) the architectural mechanism by which this role disagrees.
Both (i) and (ii) appear in the same Description cell. The IA counterpoint
is not a separate "IA Position:" header above the table, not a standalone
section, and not a bullet below the table — it is inside a specific
finding's Description text.

Example Description with IA counterpoint:
> "IA rates incident exposure NEUTRAL, no new failure mode cited; security-
> lead rates P1 because the token validation bypass at api/auth.ts:203 is
> reachable from the public endpoint introduced in this diff."

### [Role Name] — Summary

```
[Role Name]: [N] findings — [x] P1, [y] P2, [z] P3
```

---

## CONSENSUS BLOCK

```
┌─ CONSENSUS ANALYSIS ───────────────────────────────────────────────┐
│ Divergent findings:                                                │
│                                                                    │
│ [Finding ID]: [Role A] = P[n], [Role B] = P[m]                     │
│   Mechanism: [structural or code-level reason for divergence —     │
│   not a perspective label — naming the specific component, guard,  │
│   or path that causes the severity gap]                            │
│                                                                    │
│ [repeat for each divergent finding]                                │
└────────────────────────────────────────────────────────────────────┘
```

Prohibited explanation forms (enumerated — apply before output):
- "they see this differently because of their role"
- "[Role] prioritizes [X] while [Role] prioritizes [Y]"
- "it's a matter of perspective / focus"
- "each role views this finding differently"
- "this depends on which lens is applied"

Any explanation matching the above is a rewrite trigger.

---

## RECOMMENDATION BLOCK

Output exactly one of:

```
RECOMMENDATION: GO
```

```
RECOMMENDATION: GO WITH CONDITIONS
Conditions:
  1. [What must be resolved] — sign-off: [Role responsible]
  2. [What must be resolved] — sign-off: [Role responsible]
```

```
RECOMMENDATION: NO-GO
Blockers:
  - [Finding ID]: [reason merge is blocked]
```
```

---

## V-04

**Variation axes:** Phase gates + Inertia framing (combined)
**Hypothesis:** Combining explicit phase-gate pipeline with the IA-as-budget-authority structure — and making the C-31 and C-32 requirements visible as named phase exit conditions rather than inline rules — will close both gaps through structural enforcement rather than instruction-following.

---

```markdown
# /corps-pr

Run a PR through the full organizational review as a structured pipeline.
The Inertia Advocate is the status quo's budget authority and runs first.
Technical roles review the IA's cost position before analyzing the diff.

---

## INVOCATION HANDLING

**Default mode:** Route all activated roles from org.yaml.

**AMEND mode:** If an AMEND directive is present, output before all phases:

```
AMEND SCOPE DISCLOSURE
(a) Amendment: [description]
(b) Roles added: [list or "none"]
(c) Roles removed: [list or "none"]
(d) Prior findings superseded: [finding IDs or "none"]
```

---

## PHASE A — ROUTING

**Entry condition:** PR diff is available; org.yaml is readable.

Read org.yaml. Activate roles whose domain scope covers at least one
changed file. Inertia Advocate activates first, always, when configured.

```
ROUTING SUMMARY
Files changed: [count]
Roles activated: [IA first, then technical roles]
  [Role]: [files that triggered activation]
```

**Exit condition:** Routing summary output; IA sequenced first in
activation list.

---

## PHASE B — INERTIA ADVOCATE

**Entry condition:** Phase A exited.

The IA holds a budget authority position. Their output is a cost ledger
and a three-clause verdict, not a list of concerns.

### Cost Ledger

| Cost Row           | Current-State Cost | Adoption Cost | Net Direction |
|--------------------|--------------------|---------------|---------------|
| Maintenance burden | [value]            | [value]       | WORSE / BETTER / NEUTRAL |
| Incident exposure  | [value]            | [value]       | WORSE / BETTER / NEUTRAL |
| [additional rows]  | [value]            | [value]       | WORSE / BETTER / NEUTRAL |

### Budget Verdict — Three-Clause Formula

Output on exactly three lines. Each label at line start, nothing else on
that line:

```
WORSE rows: [list, or "none"]
BETTER rows: [list, or "none"]
Conclusion: [verdict explicitly derived from the named row directions]
```

### Budget Strength

```
Budget strength: [LOW / MEDIUM / HIGH]
```

**Exit conditions:**
- Cost ledger present with at least maintenance burden and incident
  exposure rows, each with a Net Direction value
- Budget verdict output with all three clauses, each on its own line
- Budget strength terminal field present
- PRE-COMMITMENT blocks for Phase C precede all diff content ← named
  Phase B exit gate for C-30 compliance; absence of PRE-COMMITMENT
  blocks is a Phase B exit violation, not merely a format issue

---

## PHASE C — TECHNICAL ROLE REVIEWS

**Entry condition — two independently auditable sub-conditions:**

**C1 (pre-flight checklist):** Before Phase C begins, verify:
- [ ] Cost ledger has maintenance burden and incident exposure rows
- [ ] Budget verdict has all three clauses (WORSE rows / BETTER rows / Conclusion)
- [ ] Each clause is on its own line
- [ ] Budget strength field is present
- [ ] PRE-COMMITMENT blocks precede findings tables (Phase B exit gate)

Output one line:
```
C1 RESULT: ALL CLEAR
```
or:
```
C1 RESULT: BLOCKED -- [item that failed]
```
A BLOCKED result halts Phase C.

**C2 (per-role IA read prerequisite):** Before each role generates findings,
that role must cite specific Phase B content — Budget verdict text, cost
row, Budget strength value — in its PRE-COMMITMENT block. Absence of these
citations fails C2 for that role independently.

Output in each role section, after the PRE-COMMITMENT block:
```
C2 RESULT: SATISFIED
```
or:
```
C2 RESULT: UNSATISFIED -- [citation missing]
```

### Per-Role Sequence

For each activated technical role:

**Step C.1 — PRE-COMMITMENT Block**

No PR diff file, function, or line number appears before this block closes.

```
PRE-COMMITMENT: [Role Name]
(a) IA section read: yes
(b) Budget verdict: [restate WORSE rows / BETTER rows / Conclusion accurately]
(c) Budget strength: [restate value]
(d) Cost row most relevant to this domain: [row name from Phase B ledger]
(e) Initial position on that row: [AGREE / DISAGREE / PARTIAL — committed now]

[PRE-COMMITMENT SEALED]
```

**Step C.2 — C2 Result**

```
C2 RESULT: SATISFIED  (or UNSATISFIED -- [what is missing])
```

**Step C.3 — IA READ RECEIPT**

```
IA READ RECEIPT: [Role Name]
(a) IA section read: Phase B IA Review
(b) Budget verdict: WORSE rows: [restate] / BETTER rows: [restate] / Conclusion: [restate]
(c) Budget strength: [value]
(d) Cost row most relevant: see PRE-COMMITMENT block — (d) [row name]
(e) Initial position: see PRE-COMMITMENT block — (e) committed above
```

Fields (d) and (e) must cross-reference the PRE-COMMITMENT block by its
label, citing both field letters. Alternative: restate both values inline
in the receipt. A receipt missing both fields without a cross-reference
fails Phase C completeness check.

**Step C.4 — Findings Table**

| ID   | Sev  | Location | Description | Domain-Lens Gate |
|------|------|----------|-------------|-----------------|
| F-01 | P[n] | file:line | [text] | Passed |

Domain-Lens Gate: per finding, test "Would only this role raise this given
their domain?" Revise until the test passes. Write "Passed" only after the
test is applied.

IA Counterpoint — finding body placement (C-31): at least one finding's
Description field must contain both (i) the IA's cost verdict on this area
and (ii) the architectural mechanism by which this role disagrees — in the
same Description text. This is not a separate "IA Position:" block, not a
section header, and not a trailing bullet. It is inside one specific
finding's Description cell. The finding is identifiable by its F-NN ID.
A role section where the IA counterpoint appears only as a section-level
element outside all finding cells fails this Phase C exit condition.

**Step C.5 — Role Summary**

```
[Role Name]: [N] findings — [x] P1, [y] P2, [z] P3
```

**Phase C exit conditions:**
- C1 RESULT: ALL CLEAR output
- All role PRE-COMMITMENT blocks sealed before diff content
- All C2 RESULT lines output per role
- All READ RECEIPTs complete with (d) and (e) present or cross-referenced
- All findings tables have Domain-Lens Gate "Passed" per finding
- At least one finding per role has IA counterpoint in finding body text
- All role summary lines present

---

## PHASE D — SYNTHESIS

**Entry condition:** Phase C exited.

### Consensus Analysis

For each finding with divergent severity ratings across roles:
- State the finding ID, the ratings, and the roles assigning them.
- State the architectural mechanism — a structural, code-level reason one
  role rates higher. Name the component, guard, path, or interface.
- Do not use perspective labels. Enumerated ban list:
  1. "they see this differently because of their role"
  2. "it's a matter of perspective"
  3. "[Role] prioritizes [X] differently"
  4. "depends on which lens"
  5. "each role has a different view"
  6. "role-based difference in assessment"

### Recommendation

```
RECOMMENDATION: GO
```
```
RECOMMENDATION: GO WITH CONDITIONS
  Condition 1: [what] — confirmed by: [role]
  Condition 2: [what] — confirmed by: [role]
```
```
RECOMMENDATION: NO-GO
  Blocker: [finding ID] — [reason]
```

**Phase D exit conditions:** Consensus analysis output; all divergence
explanations cite mechanisms not perspective labels; recommendation output
with owners named if GO WITH CONDITIONS.
```

---

## V-05

**Variation axes:** All axes combined — maximum structure
**Hypothesis:** Full integration of all axes — phase gates driving structural enforcement, IA as ledger-based budget authority, template-driven output blocks, finding-body IA anchor as an explicit named field, and READ RECEIPT with required PRE-COMMITMENT cross-reference syntax — will achieve the highest rubric composite by making C-31 and C-32 unavoidable structural slots rather than optional instructions.

---

```markdown
# /corps-pr

Run a PR through the full organizational review. This skill produces a
structured pipeline output with named phases, template-driven blocks, and
explicit gate enforcement. The Inertia Advocate is the first reviewer and
holds a budget authority position. Technical roles pre-commit their IA
position before analyzing the diff.

---

## PRE-RUN: AMEND CHECK

If invoked with an AMEND directive, produce this block before any phase
begins. Omit entirely in default mode.

```
┌─ AMEND SCOPE DISCLOSURE ───────────────────────────────────────────┐
│ (a) Amendment:              [what was changed]                     │
│ (b) Roles added:            [list, or "none"]                      │
│ (c) Roles removed:          [list, or "none"]                      │
│ (d) Prior findings superseded: [IDs, or "none"]                    │
└────────────────────────────────────────────────────────────────────┘
```

---

## PIPELINE DECLARATION

```
┌─────────────────────────────────────────────────────────────────────────┐
│ PHASE A — Routing                                                       │
│   Entry:  PR diff available; org.yaml readable                          │
│   Exit:   Routing summary output; IA first in activation list           │
│   Gates:  role selection, routing rationale                             │
├─────────────────────────────────────────────────────────────────────────┤
│ PHASE B — Inertia Advocate (budget authority)                           │
│   Entry:  Phase A exited                                                │
│   Exit:   Cost ledger complete; three-clause verdict with each clause   │
│           on its own line; Budget strength present;                     │
│           PRE-COMMITMENT blocks precede findings tables ← named gate    │
│   Gates:  C-17, C-19, C-21, C-25, C-27, C-28, C-29, C-30              │
├─────────────────────────────────────────────────────────────────────────┤
│ PHASE C — Technical Role Reviews                                        │
│   Entry:  C1 pre-flight Phase B exit checklist (ALL CLEAR required)    │
│           C2 per-role IA read prerequisite (verified per role)          │
│   Exit:   All role findings tables complete; Domain-Lens Gate applied   │
│           per finding; at least one finding per role has IA counterpoint│
│           in finding body text; READ RECEIPTs complete with (d)+(e);   │
│           PRE-COMMITMENT blocks precede findings tables ← named gate    │
│   Gates:  C-14, C-18, C-20, C-22, C-23, C-24, C-26, C-30, C-31, C-32 │
├─────────────────────────────────────────────────────────────────────────┤
│ PHASE D — Synthesis                                                     │
│   Entry:  Phase C exited; all role summaries present                    │
│   Exit:   Consensus analysis complete; ban list applied;                │
│           recommendation output with conditions and owners named         │
│   Gates:  C-09, C-10, C-12, C-13                                       │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## PHASE A — ROUTING

Read `org.yaml`. Extract all role definitions, domain scopes, and IA
configuration.

Activate roles whose domain scope covers at least one changed file.
Inertia Advocate activates first, always.

```
┌─ ROUTING SUMMARY ──────────────────────────────────────────────────┐
│ Files changed:   [count]                                           │
│ Roles activated: IA first, then technical roles in order           │
│   [Role]:  triggered by [file(s)]                                  │
│   [Role]:  triggered by [file(s)]                                  │
└────────────────────────────────────────────────────────────────────┘
```

Phase A exit gate: routing summary output; IA listed first.

---

## PHASE B — INERTIA ADVOCATE

Entry: Phase A exited.

The Inertia Advocate is the status quo's budget authority. Output a
cost ledger and a three-clause verdict. Do not list concerns. Frame
as tradeoffs with explicit cost terms.

### B.1 — IA Cost Ledger

| Cost Row           | Current-State Cost | Adoption Cost | Net Direction         |
|--------------------|--------------------|---------------|-----------------------|
| Maintenance burden | [value]            | [value]       | WORSE / BETTER / NEUTRAL |
| Incident exposure  | [value]            | [value]       | WORSE / BETTER / NEUTRAL |
| [additional rows]  | [value]            | [value]       | WORSE / BETTER / NEUTRAL |

All cells required. Net Direction values: WORSE, BETTER, or NEUTRAL only.

### B.2 — Budget Verdict

Three clauses. Each on its own output line. No clause shares its line
with another label or value. Each label appears at line start:

```
WORSE rows: [list all WORSE-direction rows, or "none"]
BETTER rows: [list all BETTER-direction rows, or "none"]
Conclusion: [verdict explicitly derived from the named row directions]
```

Conclusion must cite which rows drove it. A conclusion that does not
reference named rows fails the derivation requirement.

### B.3 — Budget Strength

```
Budget strength: [LOW / MEDIUM / HIGH]
```

Phase B exit gate:
- [ ] Cost ledger has maintenance burden + incident exposure rows, each
      with Net Direction value
- [ ] Budget verdict has WORSE rows / BETTER rows / Conclusion clauses,
      each on its own line
- [ ] Budget strength present
- [ ] PRE-COMMITMENT blocks precede findings tables ← compliance item;
      absence is a Phase B exit violation

---

## PHASE C — TECHNICAL ROLE REVIEWS

### C.0 — C1 Pre-flight Check

Before any role section begins, verify all Phase B exit conditions.
Output exactly one of:

```
C1 RESULT: ALL CLEAR
```

```
C1 RESULT: BLOCKED -- [item that failed from Phase B exit checklist]
```

A BLOCKED result halts Phase C. No technical role output until resolved.

---

### Per-Role Block Template

Repeat for each activated technical role, in routing order:

---

#### [Role Name]

**C.1 — PRE-COMMITMENT**

No PR diff content (file path, function, line number) may appear in the
output before this block closes with its seal token.

```
┌─ PRE-COMMITMENT: [Role Name] ─────────────────────────────────────┐
│ (a) IA section read: yes                                          │
│ (b) Budget verdict restated:                                      │
│     WORSE rows: [accurate restatement from Phase B]               │
│     BETTER rows: [accurate restatement from Phase B]              │
│     Conclusion: [accurate restatement from Phase B]               │
│ (c) Budget strength: [value from Phase B terminal field]          │
│ (d) Cost row most relevant to this domain: [row name]             │
│ (e) Initial position on (d): [AGREE / DISAGREE / PARTIAL]         │
│     [one sentence stating the pre-analysis reasoning]             │
└───────────────────────────────────────────────────────────────────┘
[PRE-COMMITMENT SEALED]
```

`[PRE-COMMITMENT SEALED]` is a required output line. It closes the block.
All PR diff references follow after this line.

**C.2 — C2 Result**

```
C2 RESULT: SATISFIED
```

or if Phase B content citations are missing from the PRE-COMMITMENT block:

```
C2 RESULT: UNSATISFIED -- [citation missing: field (a)/(b)/(c)/(d)/(e)]
```

**C.3 — IA READ RECEIPT**

This block appears before the findings table. Fields (d) and (e) must be
present — either as explicit cross-references to the PRE-COMMITMENT block
by label name, or restated inline. An omission of both without either
form fails the receipt completeness check.

```
┌─ IA READ RECEIPT: [Role Name] ────────────────────────────────────┐
│ (a) IA section read: Phase B — Inertia Advocate                   │
│ (b) Budget verdict:                                               │
│     WORSE rows: [restate]                                         │
│     BETTER rows: [restate]                                        │
│     Conclusion: [restate]                                         │
│ (c) Budget strength: [value]                                      │
│ (d) Cost row most relevant: see PRE-COMMITMENT block —            │
│     (d) [row name]                                                │
│ (e) Initial position: see PRE-COMMITMENT block —                  │
│     (e) committed above                                           │
└───────────────────────────────────────────────────────────────────┘
```

Fields (d) and (e) satisfy C-32 via either:
- Cross-reference form: `see PRE-COMMITMENT block — (d/e) [value]`
- Inline restatement: write the value directly in the receipt

Both forms are acceptable. A receipt where (d) and (e) are absent with
neither form present is a receipt gap.

**C.4 — Findings Table**

| ID   | Sev  | Location      | Description                                     | Domain-Lens Gate |
|------|------|---------------|-------------------------------------------------|-----------------|
| F-01 | P[n] | [file]:[line] | [See IA counterpoint rule for at least one row] | Passed           |
| F-02 | P[n] | [file]:[line] | [text]                                          | Passed           |

**Domain-Lens Gate (per finding):**
Test: "Would only this role raise this finding given their domain scope?"
If any generic reviewer could write the same sentence, revise before
including. Apply this test before writing each finding. Write "Passed"
in the gate column only after the test is applied and passed.

**IA Counterpoint in finding body text (C-31):**
For at least one finding in this table, the Description field must contain:
- (i) The IA's specific cost position or verdict on this area — cite the
  cost row, Net Direction, and Conclusion language from Phase B
- (ii) The architectural mechanism by which this role disagrees — name the
  file, function, or code path, and state the specific failure mode

Both (i) and (ii) must appear in the same Description cell of the same
finding row. The IA counterpoint is not:
- A separate "IA Position:" block before the table
- A section header above or below the table
- A trailing annotation beneath the table
- An introductory paragraph before F-01

It is inside a specific finding's Description column. The finding is
identified by its F-NN ID. If this role has no findings, this requirement
is automatically satisfied.

Example compliant Description for F-01:
> "IA rates maintenance burden NEUTRAL — no additional maintenance cost
> cited from the token validation change. Compiler-lead rates P1: the
> new emit path at src/codegen/emit.ts:144 bypasses the null-guard
> introduced in the prior release, creating silent truncation under
> concurrent emit that will not surface in unit tests."

Example non-compliant forms (these fail C-31):
- A "IA Position: ..." block before the table with F-01 having no IA text
- A section footer: "IA found current state sufficient; we disagree
  for the above reasons"
- An "IA disagreement note" bullet below the table

**C.5 — Role Summary**

```
[Role Name]: [N] findings — [x] P1, [y] P2, [z] P3
```

Phase C exit gate (per role before proceeding to next role):
- [ ] PRE-COMMITMENT block sealed before diff content
- [ ] C2 RESULT line present
- [ ] READ RECEIPT complete: (d) and (e) present or cross-referenced
- [ ] Findings table: Domain-Lens Gate "Passed" per row
- [ ] At least one finding's Description contains IA counterpoint
      with both (i) IA cost position and (ii) disagreeing mechanism
- [ ] Role summary line present

---

## PHASE D — SYNTHESIS

Entry: Phase C exited; all role summaries present.

### D.1 — Consensus Analysis

For each finding with divergent severity ratings:

1. State the finding ID and each role's severity rating.
2. Name the architectural mechanism explaining the divergence. This is
   a code-level, structural, or interface-level reason — not a framing
   difference, not a priority difference.

**Enumerated ban list — apply before outputting any divergence explanation:**
1. "they see this differently because of their role"
2. "it's a matter of perspective / focus / priorities"
3. "[Role A] prioritizes [X] while [Role B] prioritizes [Y]"
4. "this depends on which lens you apply"
5. "each role has a different view of this finding"
6. "role-based assessment difference"
7. "it reflects their area of ownership"

Any explanation matching a ban-list form is a rewrite trigger. Apply
the rewrite before this section is complete.

### D.2 — Recommendation

Output exactly one block:

```
RECOMMENDATION: GO
Basis: [one sentence — all findings at acceptable severity]
```

```
RECOMMENDATION: GO WITH CONDITIONS
Conditions:
  1. [What must be resolved]
     Sign-off required from: [Role name]
  2. [What must be resolved]
     Sign-off required from: [Role name]
```

```
RECOMMENDATION: NO-GO
Blockers:
  - [Finding ID]: [finding summary and reason merge is blocked]
```

Phase D exit gate: consensus analysis complete; ban list applied to all
divergence explanations; recommendation output with named owners for
each condition (GO WITH CONDITIONS) or named blockers (NO-GO).
```

---

## Variation Summary

| Variation | Primary Axis | C-31 Mechanism | C-32 Mechanism |
|-----------|-------------|----------------|----------------|
| V-01 | Inertia framing | Finding template with IA counterpoint field in Description | READ RECEIPT template with PRE-COMMITMENT field cross-reference syntax |
| V-02 | Phase gate lifecycle | Phase C exit condition names IA counterpoint in body as a gate | Phase C exit condition names (d)+(e) receipt completeness as a gate |
| V-03 | Output format | Findings table template with explicit IA counterpoint slot and compliant/non-compliant examples | READ RECEIPT template with explicit `see PRE-COMMITMENT block — (d/e)` syntax |
| V-04 | Phase gates + IA framing | C-31 named as a Phase C exit condition; finding template names both (i) cost position and (ii) mechanism | C-32 named as a Phase C exit condition; receipt template requires cross-reference label by name |
| V-05 | All axes | Named field in findings Description; compliant and non-compliant forms enumerated | Dual-form compliance (cross-reference or inline restatement); absence described as "receipt gap" |
