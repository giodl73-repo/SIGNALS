---
skill: corps-pr
skill_target: Run a PR through the full org with per-role findings and go/no-go recommendation
round: R18
date: 2026-03-17
rubric_version: 16
---

# Variate R18 — corps-pr

## Variation Axes

| Code | Axis | Description |
|------|------|-------------|
| V-01 | Role Sequence | Domain-specific first, then security/compliance, then PM/TPM |
| V-02 | Output Format | Phase E appends per-role scorecard table (P1/P2/P3 tally + merge gate) |
| V-03 | Phrasing Register | Conversational imperative: second-person direct commands throughout |
| V-04 | Role Sequence + Lifecycle Emphasis | Domain-first + explicit ENTRY GATE / EXIT GATE banners per phase |
| V-05 | Full Combination | Inertia Framing (status-quo champion) + Output Format (scorecard) + Phrasing Register (imperative) |

## R17 Baseline Summary

R17 achieved 40/40 aspirational (100 composite against v15 rubric) across all five variations by
carrying the C-47 + C-48 invariant structural core verbatim. Two new criteria were extracted:

- **C-49**: `Eliminated [C-46]:` sub-entry must carry a back-reference naming the CLOSED PATHS
  block by its label and section: `Declaration: see "Closed paths [C-43]:" in pipeline
  declaration [C-45].` This makes the audit loop traversable starting from the negation endpoint.
- **C-50**: A named terminal element in the structural enforcement levels section explicitly
  asserting bidirectional closure: `Audit loop closed [C-50]: "Closed paths [C-43]:" and
  "Eliminated [C-46]:" cross-reference each other bidirectionally -- traversable from either
  endpoint without reading intervening content.`

## R18 Target

Add C-49 back-reference and C-50 symmetry declaration to the invariant structural core, present
in all five variations. Target: 42/42 aspirational (100 composite against v16 rubric).

## Predicted Scores (v16 rubric)

| Variation | C-47 | C-48 | C-49 | C-50 | Predicted Score | Composite |
|-----------|------|------|------|------|-----------------|-----------|
| V-01 | Pass | Pass | Pass | Pass | 42/42 | 100 |
| V-02 | Pass | Pass | Pass | Pass | 42/42 | 100 |
| V-03 | Pass | Pass | Pass | Pass | 42/42 | 100 |
| V-04 | Pass | Pass | Pass | Pass | 42/42 | 100 |
| V-05 | Pass | Pass | Pass | Pass | 42/42 | 100 |

---

## V-01 — Role Sequence (Domain-First)

**Axis**: Role Sequence — Domain-specific roles run first in Phase C, then security/compliance,
then PM/TPM. Role order in the sequence header and Phase C template header changes; all other
structure is invariant.

**Hypothesis**: Running domain-expert roles first anchors Phase C findings in code-surface
specifics before security and compliance evaluate them. Security reviewers then scrutinize
already-named domain mechanisms rather than discovering them independently, reducing duplicate
findings. Structural compliance (C-47, C-48, C-49, C-50) is unaffected because the invariant
structural core is carried verbatim.

```
You are running `/corps-pr`. This skill runs as a five-phase pipeline. Eleven structural
compliance mechanisms are active: string-matchable Budget verdict (C-25), named result
tokens (C-26), PRE-COMMITMENT blocks (C-27), receipt-completeness / ordering pair
(C-33 + C-35), ordering as phase-gate failure (C-36), self-contained per-field C2 RESULT
block (C-37 + C-39), F-01 IA-RESPONSE column-header schema (C-34 + C-38 + C-40),
three-level structural enforcement partition with named path-negation sub-entry (C-41 + C-46),
CLOSED PATHS enumeration in pipeline declaration with format-rules restatement (C-43 + C-45),
and Eliminated-to-CLOSED-PATHS reverse cross-reference with bidirectional symmetry declaration
(C-49 + C-50).
Read the full pipeline declaration before producing any output.

---

**PIPELINE DECLARATION**

Phase A -- Route
  Entry:    org.yaml + PR diff + .craft/roles/ loaded
  Exit:     Routing table complete; every file has a row; every role cites exact scope
            pattern; coverage gaps declared
  Gates:    C-01, C-06

Phase B -- Inertia Review
  Entry:    Phase A exit met
  Exit:     (B1) Null hypothesis stated
            (B2) Cost ledger: 4 rows x 2 columns x Net direction per row filled
            (B3) Budget verdict: three separate labeled lines [C-25]
                 "WORSE rows: [values]" on its own line
                 "BETTER rows: [values]" on its own line
                 "Conclusion: [text]" on its own line
            (B4) Budget strength declared as terminal field below separator
            (B5) IA verdict in cost terms
  Gates:    C-11, C-17, C-19, C-21, C-25

Phase C -- Technical Reviews
  Entry:    Two sub-conditions, each producing an exact result token [C-26]:
            C1 (Phase B exit pre-flight, phase-level):
              Scope: Phase B completeness.
              Terminal: C1 RESULT: ALL CLEAR
              or C1 RESULT: BLOCKED -- [B-number]
            C2 (READ RECEIPT completeness, per-role) [C-33]:
              Scope: receipt fields (a)-(e) complete. NOT Phase B re-check.
              C2 RESULT block enumerates (a)-(e) with PRESENT/ABSENT per field [C-37].
              Per-field evidence and terminal verdict co-appear in same block [C-39].
              C2 RESULT must appear after READ RECEIPT block in output [C-35].
              Terminal (within the C2 RESULT block): C2 RESULT: SATISFIED [all five PRESENT]
              or C2 RESULT: UNSATISFIED -- field (x): [label] [ABSENT field named inline]
  Exit:     (1) C1 ends in ALL CLEAR
            (2) All C2 blocks end in SATISFIED
            (3) READ RECEIPT precedes C2 RESULT per role in the output [C-35/C-36] --
                a C2 RESULT line that appears before its role's READ RECEIPT block is a
                Phase C exit-condition failure; Phase D does not begin
            (4) C2 RESULT block enumerates receipt fields (a)-(e) with PRESENT/ABSENT per
                field; terminal verdict derives within same block; no cross-block reading
                required [C-33, C-37, C-39]
            (5) PRE-COMMITMENT blocks precede findings tables [C-27]
            (6) F-01 in every findings table: Type = IA-RESPONSE; [IA-VERDICT] and
                [ROLE-MECHANISM] are column headers; slot compliance is O(1) column-count
                [C-34, C-38, C-40]; pipeline declaration CLOSED PATHS names the
                prohibited inline-cell-label path [C-43, C-45]
            (7) All findings passed domain-lens gate
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26, C-27, C-33, C-34,
            C-35, C-36, C-37, C-38, C-39, C-40, C-41, C-43, C-44, C-45, C-46

Phase D -- Synthesis
  Entry:    Phase C exit met (all 7 conditions including C-36 ordering, C-37/C-39
            self-contained block, C-38/C-40 column-header schema, C-41/C-46 declared
            partition + named negation sub-entry, C-43/C-45 CLOSED PATHS + format-rules
            restatement, C-49/C-50 reverse cross-reference + bidirectional symmetry)
  Exit:     Consensus complete; all Mechanism lines pass ban-to-fix check
  Gates:    C-03, C-09, C-12, C-13

Phase E -- Decision
  Entry:    Phase D exit met
  Exit:     Exactly one GO / NO-GO / GO WITH CONDITIONS; conditions name sign-off
  Gates:    C-04, C-10

Structural enforcement levels [C-41]:
  Exit-condition level -- Phase C exit checklist item (3):
    C-36: READ RECEIPT-before-C2-RESULT ordering is a Phase C exit-condition violation
          when not met; Phase D does not begin. Auditable by reading exit item (3) alone.
  Block level -- C2 RESULT named block (## C2 RESULT -- [Role Name]):
    C-37: C2 RESULT block enumerates receipt fields (a)-(e) with PRESENT/ABSENT per field.
    C-39: Per-field evidence and terminal verdict co-appear in the same named block;
          no cross-block reading required; UNSATISFIED path handled inline.
    Auditable by reading the C2 RESULT block alone.
  Table-column level -- findings table header row:
    C-38: F-01 IA-RESPONSE Description field declares [IA-VERDICT] and [ROLE-MECHANISM]
          as named schema slots visible in output.
    C-40: [IA-VERDICT] and [ROLE-MECHANISM] are column headers in the findings table;
          slot compliance is O(1) column-count check.
    Eliminated [C-46]: no inline-cell alternative path for [IA-VERDICT]/[ROLE-MECHANISM].
          The column-header form (C-40, table-column level) supersedes the cell-label form
          (C-38, block level). This negation is declared independently of C-40's description
          and is auditable by label-matching "Eliminated [C-46]:" without parsing C-40.
          Declaration: see "Closed paths [C-43]:" in pipeline declaration [C-45]. [C-49]
    Auditable by counting table columns alone; negation auditable by label-scan.
  Each level is independently auditable without reading adjacent levels.
  No two criterion families share a level.
  Audit loop closed [C-50]: "Closed paths [C-43]:" and "Eliminated [C-46]:" cross-reference
    each other bidirectionally -- traversable from either endpoint without reading
    intervening content.

Closed paths [C-43]:
  C-40 (table-column level) supersedes C-38 (block level) for F-01 Description schema.
  The inline-cell-label "or" path ("[IA-VERDICT: X] | [ROLE-MECHANISM: Y]" in a single
  Description cell) satisfies C-38 but is C-40 noncompliant -- do not use it.
  Only the column-header form (separate named [IA-VERDICT] and [ROLE-MECHANISM] columns)
  satisfies the table-column level requirement. A reviewer auditing this section can verify
  the closed path by name without reading format rules [C-45].
  Path negation: see "Eliminated [C-46]:" in structural enforcement levels above [C-46].

---

**PHASE A -- ROUTE**

## Phase A: Routing

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern] |
| (all files) | default | Inertia Advocate | default -- always included |

Coverage gap: `COVERAGE GAP: [file] -- no org.yaml scope pattern covers this path.`

---

**PHASE B -- INERTIA REVIEW**

Entry: Phase A exit met.

The Budget verdict appears as exactly three separate labeled lines below the separator.
Each line begins with its clause label. No clause is embedded in a table cell, in the
Conclusion of another clause, or merged with another clause on the same line.

## Phase B: Inertia Advocate

Null hypothesis: The codebase currently [does X via mechanism Y].           <- B1

Cost ledger:                                                                 <- B2

| Cost Category     | Current-State Cost                             | Adoption Cost (this PR)                 | Net                      |
|-------------------|------------------------------------------------|-----------------------------------------|--------------------------|
| Maintenance       | [LOW/MED/HIGH -- maintaining current path]     | [maintaining new path post-merge]       | WORSE / BETTER / NEUTRAL |
| Incident exposure | [failure risk/severity under status quo]       | [residual exposure after merge]         | WORSE / BETTER / NEUTRAL |
| Integration cost  | [coordination overhead of current approach]    | [churn, downstream wiring, test burden] | WORSE / BETTER / NEUTRAL |
| Regression risk   | [risk of new failures from current approach]   | [risk introduced by this PR]            | WORSE / BETTER / NEUTRAL |

---
WORSE rows: [Cost Categories where Net = WORSE, or "none"]               <- B3 line 1 [C-25]
BETTER rows: [Cost Categories where Net = BETTER, or "none"]             <- B3 line 2 [C-25]
Conclusion: [one sentence -- is adoption justified?]                     <- B3 line 3 [C-25]

Budget strength: HIGH / MEDIUM / LOW                                      <- B4

Findings:
F-01 [P1/P2/P3] [argument current state is sufficient]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second argument grounded in cost ledger]
     Owner: [role] | Resolution: [action]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS -- [one sentence in cost terms]      <- B5

Phase B exit: B1-B5 met; three Budget verdict lines present as separate output lines.

---

**PHASE C -- TECHNICAL REVIEWS**

**C1 -- Phase B Exit Pre-Flight [C-26/C1, scope: Phase B completeness]:**

## Phase C Pre-Flight (C1)

[ ] B1 -- Null hypothesis stated
[ ] B2 -- Cost ledger: 4 rows x 2 columns x Net direction per row
[ ] B3 -- Budget verdict: three labeled lines present
         "WORSE rows:" on own line? [yes/no]
         "BETTER rows:" on own line? [yes/no]
         "Conclusion:" on own line? [yes/no] -- all must be yes
[ ] B4 -- Budget strength terminal field
[ ] B5 -- IA verdict in cost terms

C1 RESULT: ALL CLEAR

If any box unchecked: `C1 RESULT: BLOCKED -- [B-number]`

C1 scope is Phase B. C1 RESULT does not confirm any role's READ RECEIPT content.

**Per-Role Output Sequence (C-35/C-36: STEP 1 must precede STEP 2 in the output;
STEP 2 before STEP 1 is a Phase C exit-condition failure -- Phase D blocked):**

Sequence across roles: domain-specific -> security/compliance -> PM/TPM.

**STEP 1 -- READ RECEIPT [must appear in output before STEP 2]:**

Output the READ RECEIPT block now, before writing any C2 RESULT block for this role.

## IA READ RECEIPT -- [Role Name]

(a) Section read:        Phase B -- Inertia Advocate
(b) Budget verdict:
      WORSE rows:        [restate Phase B "WORSE rows:" line verbatim]
      BETTER rows:       [restate Phase B "BETTER rows:" line verbatim]
      Conclusion:        [restate Phase B "Conclusion:" line accurately]
(c) Budget strength:     HIGH / MEDIUM / LOW [from Phase B terminal field]
(d) Ledger row:          [Maintenance / Incident exposure / Integration cost / Regression risk]
(e) Initial position:    [CONFIRMS / DISPUTES] Net direction on [row (d)]
                         [one phrase -- domain knowledge and Phase B ledger only]

**STEP 2 -- C2 RESULT BLOCK [C-33, C-37, C-39, C-26/C2] [must follow STEP 1 -- C-35/C-36]:**

The C2 RESULT block enumerates all five receipt fields (a)-(e) by label with an explicit
PRESENT or ABSENT verdict per field. The terminal C2 RESULT line derives from the per-field
verdicts above it and appears within this same block. C2 scope is receipt completeness -- not
Phase B. The UNSATISFIED path is handled within this block -- not in a separate adjacent fence.
A reviewer verifies both the per-field evidence and the terminal verdict by reading this
single block. No cross-block reading required [C-39].

## C2 RESULT -- [Role Name]

(a) Section read named:       PRESENT / ABSENT
(b) Budget verdict populated: PRESENT / ABSENT
(c) Budget strength stated:   PRESENT / ABSENT
(d) Ledger row named:         PRESENT / ABSENT
(e) Initial position stated:  PRESENT / ABSENT
    [valid: inline value OR cross-reference "see PRE-COMMITMENT block: [row]"]

[derive terminal verdict from per-field lines above -- write exactly one:]
All five PRESENT:  C2 RESULT: SATISFIED -- all five fields PRESENT
Any ABSENT:        C2 RESULT: UNSATISFIED -- field (x): [label of absent field]

C-36 compliance: If "C2 RESULT:" terminal line appears before "## IA READ RECEIPT" header
for this role in the output, this is a Phase C exit-condition failure -- Phase D blocked.

C-37 / C-39 compliance: (a)-(e) each on its own labeled line with PRESENT/ABSENT; terminal
C2 RESULT line is in this same block, derived from the per-field rows above -- no separate
fence, no adjacent prose carrying the verdict.

C-33 scope check: every labeled line in this block targets a receipt field, not Phase B.

**STEP 3 -- PRE-COMMITMENT [C-27, before reading diff]:**

PRE-COMMITMENT: [Role Name]

Cost row assessed:  [Maintenance / Incident exposure / Integration cost / Regression risk]
Initial position:   [CONFIRMS / DISPUTES] [Net direction] on [Cost row]
                    [one phrase based on domain knowledge + Phase B ledger]
Basis:              Domain knowledge only. PR diff not yet examined.
                    [one sentence naming the code surface or architectural pattern]

[PRE-COMMITMENT SEALED]

**STEP 4 -- FINDINGS [C-34, C-38, C-40, C-43]:**

Apply domain-lens gate per finding:

Step A: "Would only [this role] raise this finding, given their domain?"
  YES -> include. NO -> Step B.
Step B: Revise to name domain-owned mechanism. Still NO -> drop.

The findings table MUST include a Type column. F-01 MUST have Type = IA-RESPONSE.
[IA-VERDICT] and [ROLE-MECHANISM] MUST be column headers.

## Phase C: [Role Name]

Source files:  [from Phase A routing]
Orientation:   [one phrase from .craft/roles/]

[STEP 1: READ RECEIPT]
[STEP 2: C2 RESULT -- (a)-(e) + terminal verdict in same block, no separate fence]
[STEP 3: PRE-COMMITMENT]

Findings:

| ID | Type | Severity | [IA-VERDICT] | [ROLE-MECHANISM] | Domain-Lens | Owner | Resolution |
|----|------|----------|--------------|------------------|-------------|-------|------------|
| F-01 | IA-RESPONSE | P1/P2/P3 | [IA's verdict or cost position from Phase B] | [specific code artifact in this role's domain] | Passed | [role] | [action] |
| F-02 | DOMAIN | P1/P2/P3 | -- | [domain finding] | Passed | [role] | [action] |
[minimum 2]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3

Post-commitment delta:
  Pre-committed:   [CONFIRMS / DISPUTES] [Cost row]
  After findings:  [HELD / CHANGED]
  If HELD:         [code artifact from diff that confirmed the position]
  If CHANGED:      [code artifact that changed it; revised position]

F-01 IA-RESPONSE format rules [C-34, C-38, C-40, C-43]:
- Type cell: exactly "IA-RESPONSE" -- no other value passes
- Column structure: [IA-VERDICT] and [ROLE-MECHANISM] are column headers in the findings
  table. Slot compliance is O(1) column-count: a reviewer verifies presence by counting
  columns, not parsing cell content.
- Prohibition [C-43]: the inline-cell-label path ("[IA-VERDICT: X] | [ROLE-MECHANISM: Y]"
  in a single Description cell) satisfies C-38 but is C-40 noncompliant -- do not use it.
  (Declared at declaration level in pipeline CLOSED PATHS [C-45]; negation declared in
  structural enforcement "Eliminated [C-46]:" sub-entry [C-46].)
- F-01 cells: [IA-VERDICT] cell contains the IA's verdict or cost position from Phase B;
  [ROLE-MECHANISM] cell contains the specific code artifact or mechanism in this role's domain.
- DOMAIN findings (F-02 onward): [IA-VERDICT] and [ROLE-MECHANISM] columns show "--"

Phase C exit: C1 ALL CLEAR (Phase B scope); every C2 RESULT block enumerates (a)-(e)
PRESENT/ABSENT and derives terminal verdict in same block [C-33, C-37, C-39]; READ RECEIPT
precedes C2 RESULT per role -- ordering violation is Phase C exit-condition failure
[C-35/C-36]; PRE-COMMITMENT before findings [C-27]; F-01 Type=IA-RESPONSE with [IA-VERDICT]
and [ROLE-MECHANISM] as column headers [C-34/C-38/C-40]; three-level enforcement partition
with named negation sub-entry "Eliminated [C-46]:" carrying reverse cross-reference [C-41,
C-46, C-49]; CLOSED PATHS in declaration + four-element prohibition in format rules [C-43,
C-45]; bidirectional symmetry declared [C-50]; all findings passed domain-lens gate.

---

**PHASE D -- SYNTHESIS**

Entry: Phase C exit met (C-36 ordering, C-37/C-39 self-contained block, C-38/C-40
column-header schema, C-41/C-46 three-level partition + named negation sub-entry,
C-43/C-45 CLOSED PATHS in declaration + format rules restatement, C-49/C-50 reverse
cross-reference + bidirectional symmetry declaration).

## Phase D: Consensus

IA cost ledger: Budget strength was [HIGH / MEDIUM / LOW].
  WORSE rows were: [restate]. BETTER rows were: [restate].
  Technical roles collectively [reinforced / challenged / defeated] the IA's estimate.
  Net: [one sentence]

Agreement: [area] -- [role-A] and [role-B] independently raised [concern]

Divergence: [role-A] rates [area] P[N]; [role-B] rates P[N].
  Mechanism: [architectural property of the code -- not perspective difference]

Critical: [F-XX from role] -- [why this most threatens the merge]

Perspective-label ban-to-fix:

| Banned | Replacement |
|---|---|
| "they have different perspectives" | "[role-A] sees [mechanism X]; [role-B] sees [mechanism Y]" |
| "they prioritize differently" | "[path X] is in [role-A]'s domain, outside [role-B]'s" |
| "they see this through different lenses" | "change affects [A] in [role-A]'s domain and [B] in [role-B]'s" |
| "from [role]'s perspective" as sole cause | name the architectural fact causing risk |
| "their roles lead them to different conclusions" | "[role-A]'s scope includes [surface X]; [role-B]'s does not" |

A Mechanism line with a banned phrase fails even if a code mechanism is also named.

Phase D exit: consensus complete; all Mechanism lines pass.

---

**PHASE E -- DECISION**

Entry: Phase D exit met.

## Phase E: Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from role] -- [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] -- sign-off: [role who confirms before merge]

One decision. Values: GO, NO-GO, GO WITH CONDITIONS only.
Delegated decisions fail. Hedged decisions fail.

---

**AMEND**

When invoked with an AMEND directive, output this named-field block before Phase A.

## AMEND SCOPE

What was amended:           [description]
Roles added:                [list, or "none"]
Roles removed:              [list, or "none"]
Files triggering addition:  [list, or "n/a -- manually directed"]
Prior findings superseded:  [F-IDs, or "none -- first run"]

Run Phases A-E with the amended scope.
```

---

## V-02 — Output Format (Phase E Scorecard)

**Axis**: Output Format — Phase E appends a per-role findings scorecard table tallying
P1/P2/P3 counts, the IA verdict, and a merge gate condition. Phase E exit conditions updated
to require the scorecard.

**Hypothesis**: A scorecard table forces enumeration of every role's finding counts before
the GO/NO-GO decision, reducing the risk of a silently dropped P1. The merge gate line makes
the decision machine-checkable: if any unresolved P1 row exists, GO is blocked. Structural
compliance (C-49, C-50) is unaffected because the invariant structural core is carried verbatim.

```
You are running `/corps-pr`. This skill runs as a five-phase pipeline. Eleven structural
compliance mechanisms are active: string-matchable Budget verdict (C-25), named result
tokens (C-26), PRE-COMMITMENT blocks (C-27), receipt-completeness / ordering pair
(C-33 + C-35), ordering as phase-gate failure (C-36), self-contained per-field C2 RESULT
block (C-37 + C-39), F-01 IA-RESPONSE column-header schema (C-34 + C-38 + C-40),
three-level structural enforcement partition with named path-negation sub-entry (C-41 + C-46),
CLOSED PATHS enumeration in pipeline declaration with format-rules restatement (C-43 + C-45),
and Eliminated-to-CLOSED-PATHS reverse cross-reference with bidirectional symmetry declaration
(C-49 + C-50).
Read the full pipeline declaration before producing any output.

---

**PIPELINE DECLARATION**

Phase A -- Route
  Entry:    org.yaml + PR diff + .craft/roles/ loaded
  Exit:     Routing table complete; every file has a row; every role cites exact scope
            pattern; coverage gaps declared
  Gates:    C-01, C-06

Phase B -- Inertia Review
  Entry:    Phase A exit met
  Exit:     (B1) Null hypothesis stated
            (B2) Cost ledger: 4 rows x 2 columns x Net direction per row filled
            (B3) Budget verdict: three separate labeled lines [C-25]
                 "WORSE rows: [values]" on its own line
                 "BETTER rows: [values]" on its own line
                 "Conclusion: [text]" on its own line
            (B4) Budget strength declared as terminal field below separator
            (B5) IA verdict in cost terms
  Gates:    C-11, C-17, C-19, C-21, C-25

Phase C -- Technical Reviews
  Entry:    Two sub-conditions, each producing an exact result token [C-26]:
            C1 (Phase B exit pre-flight, phase-level):
              Scope: Phase B completeness.
              Terminal: C1 RESULT: ALL CLEAR
              or C1 RESULT: BLOCKED -- [B-number]
            C2 (READ RECEIPT completeness, per-role) [C-33]:
              Scope: receipt fields (a)-(e) complete. NOT Phase B re-check.
              C2 RESULT block enumerates (a)-(e) with PRESENT/ABSENT per field [C-37].
              Per-field evidence and terminal verdict co-appear in same block [C-39].
              C2 RESULT must appear after READ RECEIPT block in output [C-35].
              Terminal (within the C2 RESULT block): C2 RESULT: SATISFIED [all five PRESENT]
              or C2 RESULT: UNSATISFIED -- field (x): [label] [ABSENT field named inline]
  Exit:     (1) C1 ends in ALL CLEAR
            (2) All C2 blocks end in SATISFIED
            (3) READ RECEIPT precedes C2 RESULT per role in the output [C-35/C-36] --
                a C2 RESULT line that appears before its role's READ RECEIPT block is a
                Phase C exit-condition failure; Phase D does not begin
            (4) C2 RESULT block enumerates receipt fields (a)-(e) with PRESENT/ABSENT per
                field; terminal verdict derives within same block; no cross-block reading
                required [C-33, C-37, C-39]
            (5) PRE-COMMITMENT blocks precede findings tables [C-27]
            (6) F-01 in every findings table: Type = IA-RESPONSE; [IA-VERDICT] and
                [ROLE-MECHANISM] are column headers; slot compliance is O(1) column-count
                [C-34, C-38, C-40]; pipeline declaration CLOSED PATHS names the
                prohibited inline-cell-label path [C-43, C-45]
            (7) All findings passed domain-lens gate
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26, C-27, C-33, C-34,
            C-35, C-36, C-37, C-38, C-39, C-40, C-41, C-43, C-44, C-45, C-46

Phase D -- Synthesis
  Entry:    Phase C exit met (all 7 conditions including C-36 ordering, C-37/C-39
            self-contained block, C-38/C-40 column-header schema, C-41/C-46 declared
            partition + named negation sub-entry, C-43/C-45 CLOSED PATHS + format-rules
            restatement, C-49/C-50 reverse cross-reference + bidirectional symmetry)
  Exit:     Consensus complete; all Mechanism lines pass ban-to-fix check
  Gates:    C-03, C-09, C-12, C-13

Phase E -- Decision
  Entry:    Phase D exit met
  Exit:     (E1) Exactly one GO / NO-GO / GO WITH CONDITIONS; conditions name sign-off
            (E2) Primary finding cited
            (E3) Findings scorecard table: every routed role has a row; P1/P2/P3 columns
                 tallied; IA verdict row present; Merge gate line states unresolved-P1 rule
  Gates:    C-04, C-10

Structural enforcement levels [C-41]:
  Exit-condition level -- Phase C exit checklist item (3):
    C-36: READ RECEIPT-before-C2-RESULT ordering is a Phase C exit-condition violation
          when not met; Phase D does not begin. Auditable by reading exit item (3) alone.
  Block level -- C2 RESULT named block (## C2 RESULT -- [Role Name]):
    C-37: C2 RESULT block enumerates receipt fields (a)-(e) with PRESENT/ABSENT per field.
    C-39: Per-field evidence and terminal verdict co-appear in the same named block;
          no cross-block reading required; UNSATISFIED path handled inline.
    Auditable by reading the C2 RESULT block alone.
  Table-column level -- findings table header row:
    C-38: F-01 IA-RESPONSE Description field declares [IA-VERDICT] and [ROLE-MECHANISM]
          as named schema slots visible in output.
    C-40: [IA-VERDICT] and [ROLE-MECHANISM] are column headers in the findings table;
          slot compliance is O(1) column-count check.
    Eliminated [C-46]: no inline-cell alternative path for [IA-VERDICT]/[ROLE-MECHANISM].
          The column-header form (C-40, table-column level) supersedes the cell-label form
          (C-38, block level). This negation is declared independently of C-40's description
          and is auditable by label-matching "Eliminated [C-46]:" without parsing C-40.
          Declaration: see "Closed paths [C-43]:" in pipeline declaration [C-45]. [C-49]
    Auditable by counting table columns alone; negation auditable by label-scan.
  Each level is independently auditable without reading adjacent levels.
  No two criterion families share a level.
  Audit loop closed [C-50]: "Closed paths [C-43]:" and "Eliminated [C-46]:" cross-reference
    each other bidirectionally -- traversable from either endpoint without reading
    intervening content.

Closed paths [C-43]:
  C-40 (table-column level) supersedes C-38 (block level) for F-01 Description schema.
  The inline-cell-label "or" path ("[IA-VERDICT: X] | [ROLE-MECHANISM: Y]" in a single
  Description cell) satisfies C-38 but is C-40 noncompliant -- do not use it.
  Only the column-header form (separate named [IA-VERDICT] and [ROLE-MECHANISM] columns)
  satisfies the table-column level requirement. A reviewer auditing this section can verify
  the closed path by name without reading format rules [C-45].
  Path negation: see "Eliminated [C-46]:" in structural enforcement levels above [C-46].

---

**PHASE A -- ROUTE**

## Phase A: Routing

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern] |
| (all files) | default | Inertia Advocate | default -- always included |

Coverage gap: `COVERAGE GAP: [file] -- no org.yaml scope pattern covers this path.`

---

**PHASE B -- INERTIA REVIEW**

Entry: Phase A exit met.

The Budget verdict appears as exactly three separate labeled lines below the separator.
Each line begins with its clause label. No clause is embedded in a table cell, in the
Conclusion of another clause, or merged with another clause on the same line.

## Phase B: Inertia Advocate

Null hypothesis: The codebase currently [does X via mechanism Y].           <- B1

Cost ledger:                                                                 <- B2

| Cost Category     | Current-State Cost                             | Adoption Cost (this PR)                 | Net                      |
|-------------------|------------------------------------------------|-----------------------------------------|--------------------------|
| Maintenance       | [LOW/MED/HIGH -- maintaining current path]     | [maintaining new path post-merge]       | WORSE / BETTER / NEUTRAL |
| Incident exposure | [failure risk/severity under status quo]       | [residual exposure after merge]         | WORSE / BETTER / NEUTRAL |
| Integration cost  | [coordination overhead of current approach]    | [churn, downstream wiring, test burden] | WORSE / BETTER / NEUTRAL |
| Regression risk   | [risk of new failures from current approach]   | [risk introduced by this PR]            | WORSE / BETTER / NEUTRAL |

---
WORSE rows: [Cost Categories where Net = WORSE, or "none"]               <- B3 line 1 [C-25]
BETTER rows: [Cost Categories where Net = BETTER, or "none"]             <- B3 line 2 [C-25]
Conclusion: [one sentence -- is adoption justified?]                     <- B3 line 3 [C-25]

Budget strength: HIGH / MEDIUM / LOW                                      <- B4

Findings:
F-01 [P1/P2/P3] [argument current state is sufficient]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second argument grounded in cost ledger]
     Owner: [role] | Resolution: [action]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS -- [one sentence in cost terms]      <- B5

Phase B exit: B1-B5 met; three Budget verdict lines present as separate output lines.

---

**PHASE C -- TECHNICAL REVIEWS**

**C1 -- Phase B Exit Pre-Flight [C-26/C1, scope: Phase B completeness]:**

## Phase C Pre-Flight (C1)

[ ] B1 -- Null hypothesis stated
[ ] B2 -- Cost ledger: 4 rows x 2 columns x Net direction per row
[ ] B3 -- Budget verdict: three labeled lines present
         "WORSE rows:" on own line? [yes/no]
         "BETTER rows:" on own line? [yes/no]
         "Conclusion:" on own line? [yes/no] -- all must be yes
[ ] B4 -- Budget strength terminal field
[ ] B5 -- IA verdict in cost terms

C1 RESULT: ALL CLEAR

If any box unchecked: `C1 RESULT: BLOCKED -- [B-number]`

C1 scope is Phase B. C1 RESULT does not confirm any role's READ RECEIPT content.

**Per-Role Output Sequence (C-35/C-36: STEP 1 must precede STEP 2 in the output;
STEP 2 before STEP 1 is a Phase C exit-condition failure -- Phase D blocked):**

Sequence across roles: security/compliance -> domain-specific -> PM/TPM.

**STEP 1 -- READ RECEIPT [must appear in output before STEP 2]:**

Output the READ RECEIPT block now, before writing any C2 RESULT block for this role.

## IA READ RECEIPT -- [Role Name]

(a) Section read:        Phase B -- Inertia Advocate
(b) Budget verdict:
      WORSE rows:        [restate Phase B "WORSE rows:" line verbatim]
      BETTER rows:       [restate Phase B "BETTER rows:" line verbatim]
      Conclusion:        [restate Phase B "Conclusion:" line accurately]
(c) Budget strength:     HIGH / MEDIUM / LOW [from Phase B terminal field]
(d) Ledger row:          [Maintenance / Incident exposure / Integration cost / Regression risk]
(e) Initial position:    [CONFIRMS / DISPUTES] Net direction on [row (d)]
                         [one phrase -- domain knowledge and Phase B ledger only]

**STEP 2 -- C2 RESULT BLOCK [C-33, C-37, C-39, C-26/C2] [must follow STEP 1 -- C-35/C-36]:**

The C2 RESULT block enumerates all five receipt fields (a)-(e) by label with an explicit
PRESENT or ABSENT verdict per field. The terminal C2 RESULT line derives from the per-field
verdicts above it and appears within this same block. C2 scope is receipt completeness -- not
Phase B. The UNSATISFIED path is handled within this block -- not in a separate adjacent fence.
A reviewer verifies both the per-field evidence and the terminal verdict by reading this
single block. No cross-block reading required [C-39].

## C2 RESULT -- [Role Name]

(a) Section read named:       PRESENT / ABSENT
(b) Budget verdict populated: PRESENT / ABSENT
(c) Budget strength stated:   PRESENT / ABSENT
(d) Ledger row named:         PRESENT / ABSENT
(e) Initial position stated:  PRESENT / ABSENT
    [valid: inline value OR cross-reference "see PRE-COMMITMENT block: [row]"]

[derive terminal verdict from per-field lines above -- write exactly one:]
All five PRESENT:  C2 RESULT: SATISFIED -- all five fields PRESENT
Any ABSENT:        C2 RESULT: UNSATISFIED -- field (x): [label of absent field]

C-36 compliance: If "C2 RESULT:" terminal line appears before "## IA READ RECEIPT" header
for this role in the output, this is a Phase C exit-condition failure -- Phase D blocked.

C-37 / C-39 compliance: (a)-(e) each on its own labeled line with PRESENT/ABSENT; terminal
C2 RESULT line is in this same block, derived from the per-field rows above -- no separate
fence, no adjacent prose carrying the verdict.

C-33 scope check: every labeled line in this block targets a receipt field, not Phase B.

**STEP 3 -- PRE-COMMITMENT [C-27, before reading diff]:**

PRE-COMMITMENT: [Role Name]

Cost row assessed:  [Maintenance / Incident exposure / Integration cost / Regression risk]
Initial position:   [CONFIRMS / DISPUTES] [Net direction] on [Cost row]
                    [one phrase based on domain knowledge + Phase B ledger]
Basis:              Domain knowledge only. PR diff not yet examined.
                    [one sentence naming the code surface or architectural pattern]

[PRE-COMMITMENT SEALED]

**STEP 4 -- FINDINGS [C-34, C-38, C-40, C-43]:**

Apply domain-lens gate per finding:

Step A: "Would only [this role] raise this finding, given their domain?"
  YES -> include. NO -> Step B.
Step B: Revise to name domain-owned mechanism. Still NO -> drop.

The findings table MUST include a Type column. F-01 MUST have Type = IA-RESPONSE.
[IA-VERDICT] and [ROLE-MECHANISM] MUST be column headers.

## Phase C: [Role Name]

Source files:  [from Phase A routing]
Orientation:   [one phrase from .craft/roles/]

[STEP 1: READ RECEIPT]
[STEP 2: C2 RESULT -- (a)-(e) + terminal verdict in same block, no separate fence]
[STEP 3: PRE-COMMITMENT]

Findings:

| ID | Type | Severity | [IA-VERDICT] | [ROLE-MECHANISM] | Domain-Lens | Owner | Resolution |
|----|------|----------|--------------|------------------|-------------|-------|------------|
| F-01 | IA-RESPONSE | P1/P2/P3 | [IA's verdict or cost position from Phase B] | [specific code artifact in this role's domain] | Passed | [role] | [action] |
| F-02 | DOMAIN | P1/P2/P3 | -- | [domain finding] | Passed | [role] | [action] |
[minimum 2]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3

Post-commitment delta:
  Pre-committed:   [CONFIRMS / DISPUTES] [Cost row]
  After findings:  [HELD / CHANGED]
  If HELD:         [code artifact from diff that confirmed the position]
  If CHANGED:      [code artifact that changed it; revised position]

F-01 IA-RESPONSE format rules [C-34, C-38, C-40, C-43]:
- Type cell: exactly "IA-RESPONSE" -- no other value passes
- Column structure: [IA-VERDICT] and [ROLE-MECHANISM] are column headers in the findings
  table. Slot compliance is O(1) column-count: a reviewer verifies presence by counting
  columns, not parsing cell content.
- Prohibition [C-43]: the inline-cell-label path ("[IA-VERDICT: X] | [ROLE-MECHANISM: Y]"
  in a single Description cell) satisfies C-38 but is C-40 noncompliant -- do not use it.
  (Declared at declaration level in pipeline CLOSED PATHS [C-45]; negation declared in
  structural enforcement "Eliminated [C-46]:" sub-entry [C-46].)
- F-01 cells: [IA-VERDICT] cell contains the IA's verdict or cost position from Phase B;
  [ROLE-MECHANISM] cell contains the specific code artifact or mechanism in this role's domain.
- DOMAIN findings (F-02 onward): [IA-VERDICT] and [ROLE-MECHANISM] columns show "--"

Phase C exit: C1 ALL CLEAR (Phase B scope); every C2 RESULT block enumerates (a)-(e)
PRESENT/ABSENT and derives terminal verdict in same block [C-33, C-37, C-39]; READ RECEIPT
precedes C2 RESULT per role -- ordering violation is Phase C exit-condition failure
[C-35/C-36]; PRE-COMMITMENT before findings [C-27]; F-01 Type=IA-RESPONSE with [IA-VERDICT]
and [ROLE-MECHANISM] as column headers [C-34/C-38/C-40]; three-level enforcement partition
with named negation sub-entry "Eliminated [C-46]:" carrying reverse cross-reference [C-41,
C-46, C-49]; CLOSED PATHS in declaration + four-element prohibition in format rules [C-43,
C-45]; bidirectional symmetry declared [C-50]; all findings passed domain-lens gate.

---

**PHASE D -- SYNTHESIS**

Entry: Phase C exit met (C-36 ordering, C-37/C-39 self-contained block, C-38/C-40
column-header schema, C-41/C-46 three-level partition + named negation sub-entry,
C-43/C-45 CLOSED PATHS in declaration + format rules restatement, C-49/C-50 reverse
cross-reference + bidirectional symmetry declaration).

## Phase D: Consensus

IA cost ledger: Budget strength was [HIGH / MEDIUM / LOW].
  WORSE rows were: [restate]. BETTER rows were: [restate].
  Technical roles collectively [reinforced / challenged / defeated] the IA's estimate.
  Net: [one sentence]

Agreement: [area] -- [role-A] and [role-B] independently raised [concern]

Divergence: [role-A] rates [area] P[N]; [role-B] rates P[N].
  Mechanism: [architectural property of the code -- not perspective difference]

Critical: [F-XX from role] -- [why this most threatens the merge]

Perspective-label ban-to-fix:

| Banned | Replacement |
|---|---|
| "they have different perspectives" | "[role-A] sees [mechanism X]; [role-B] sees [mechanism Y]" |
| "they prioritize differently" | "[path X] is in [role-A]'s domain, outside [role-B]'s" |
| "they see this through different lenses" | "change affects [A] in [role-A]'s domain and [B] in [role-B]'s" |
| "from [role]'s perspective" as sole cause | name the architectural fact causing risk |
| "their roles lead them to different conclusions" | "[role-A]'s scope includes [surface X]; [role-B]'s does not" |

A Mechanism line with a banned phrase fails even if a code mechanism is also named.

Phase D exit: consensus complete; all Mechanism lines pass.

---

**PHASE E -- DECISION**

Entry: Phase D exit met.

## Phase E: Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from role] -- [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] -- sign-off: [role who confirms before merge]

Findings scorecard:

| Role | P1 | P2 | P3 | Total |
|------|----|----|-----|-------|
| Inertia Advocate | [n] | [n] | [n] | [n] |
| [Role Name] | [n] | [n] | [n] | [n] |
| [Role Name] | [n] | [n] | [n] | [n] |
| [Role Name] | [n] | [n] | [n] | [n] |

IA verdict: [BLOCK / CONDITION / PASS from Phase B]
Merge gate: GO requires zero unresolved P1s. Current unresolved P1 count: [n].

One decision. Values: GO, NO-GO, GO WITH CONDITIONS only.
Delegated decisions fail. Hedged decisions fail.

---

**AMEND**

When invoked with an AMEND directive, output this named-field block before Phase A.

## AMEND SCOPE

What was amended:           [description]
Roles added:                [list, or "none"]
Roles removed:              [list, or "none"]
Files triggering addition:  [list, or "n/a -- manually directed"]
Prior findings superseded:  [F-IDs, or "none -- first run"]

Run Phases A-E with the amended scope.
```

---

## V-03 — Phrasing Register (Conversational Imperative)

**Axis**: Phrasing Register — Second-person direct commands throughout. Phase headers use
imperative voice. Structural enforcement is stated as instructions to the model, not
declarative descriptions of rules.

**Hypothesis**: Imperative second-person ("Do X before Y") reduces model latitude to
interpret structural rules as optional. Declarative rules ("C-36 requires X") invite
reinterpretation; commands ("Write the READ RECEIPT before any C2 RESULT") do not. Structural
compliance (C-49, C-50) is unaffected because the invariant structural core is carried verbatim.

```
You are running `/corps-pr`. Run this as a five-phase pipeline. You have eleven structural
compliance rules to enforce: write a string-matchable Budget verdict (C-25), produce named
result tokens for every gate (C-26), write PRE-COMMITMENT blocks before reading the diff
(C-27), verify receipt completeness before ordering (C-33 + C-35), treat ordering violations
as phase-gate failures (C-36), put all five receipt fields and the terminal verdict in the
same C2 RESULT block (C-37 + C-39), use [IA-VERDICT] and [ROLE-MECHANISM] as column headers
in every findings table (C-34 + C-38 + C-40), declare a three-level structural enforcement
partition with a named path-negation sub-entry (C-41 + C-46), put CLOSED PATHS in the
pipeline declaration with a format-rules restatement (C-43 + C-45), and carry the
reverse cross-reference and bidirectional symmetry declaration (C-49 + C-50).
Read the full pipeline declaration before writing any output.

---

**PIPELINE DECLARATION**

Phase A -- Route
  Entry:    Load org.yaml + PR diff + .craft/roles/
  Exit:     Every file has a routing row; every role cites its exact scope pattern;
            coverage gaps declared
  Gates:    C-01, C-06

Phase B -- Inertia Review
  Entry:    Phase A exit met
  Exit:     (B1) State the null hypothesis
            (B2) Fill the cost ledger: 4 rows x 2 columns x Net direction per row
            (B3) Write the Budget verdict as three separate labeled lines [C-25]:
                 "WORSE rows: [values]" on its own line
                 "BETTER rows: [values]" on its own line
                 "Conclusion: [text]" on its own line
            (B4) Declare Budget strength as terminal field below separator
            (B5) State the IA verdict in cost terms
  Gates:    C-11, C-17, C-19, C-21, C-25

Phase C -- Technical Reviews
  Entry:    Two sub-conditions, each producing an exact result token [C-26]:
            C1 (Phase B exit pre-flight, phase-level):
              Scope: Phase B completeness.
              Write: C1 RESULT: ALL CLEAR
              or: C1 RESULT: BLOCKED -- [B-number]
            C2 (READ RECEIPT completeness, per-role) [C-33]:
              Scope: receipt fields (a)-(e) complete. NOT Phase B re-check.
              Enumerate (a)-(e) with PRESENT/ABSENT per field in the C2 RESULT block [C-37].
              Put per-field evidence and terminal verdict in the same block [C-39].
              Write C2 RESULT after READ RECEIPT in output [C-35].
              Write: C2 RESULT: SATISFIED [all five PRESENT]
              or: C2 RESULT: UNSATISFIED -- field (x): [label] [ABSENT field named inline]
  Exit:     (1) C1 ends in ALL CLEAR
            (2) Every C2 block ends in SATISFIED
            (3) Write READ RECEIPT before C2 RESULT for each role [C-35/C-36] --
                if C2 RESULT appears before READ RECEIPT, stop: Phase C exit-condition
                failure; do not begin Phase D
            (4) In every C2 RESULT block, enumerate (a)-(e) with PRESENT/ABSENT; derive
                the terminal verdict in the same block [C-33, C-37, C-39]
            (5) Write PRE-COMMITMENT blocks before findings tables [C-27]
            (6) In every findings table, F-01 must have Type = IA-RESPONSE; use
                [IA-VERDICT] and [ROLE-MECHANISM] as column headers [C-34, C-38, C-40];
                the pipeline CLOSED PATHS block names the prohibited path [C-43, C-45]
            (7) Pass every finding through the domain-lens gate before including it
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26, C-27, C-33, C-34,
            C-35, C-36, C-37, C-38, C-39, C-40, C-41, C-43, C-44, C-45, C-46

Phase D -- Synthesis
  Entry:    Phase C exit met (all 7 conditions: C-36 ordering, C-37/C-39 same-block,
            C-38/C-40 column headers, C-41/C-46 partition + negation, C-43/C-45 CLOSED
            PATHS, C-49/C-50 reverse reference + symmetry)
  Exit:     Write consensus; every Mechanism line must pass the ban-to-fix check
  Gates:    C-03, C-09, C-12, C-13

Phase E -- Decision
  Entry:    Phase D exit met
  Exit:     Write exactly one GO / NO-GO / GO WITH CONDITIONS; name sign-off in conditions
  Gates:    C-04, C-10

Structural enforcement levels [C-41]:
  Exit-condition level -- Phase C exit checklist item (3):
    C-36: If you write a C2 RESULT terminal line before the READ RECEIPT header for that
          role, that is a Phase C exit-condition failure -- stop and do not begin Phase D.
          Auditable by reading exit item (3) alone.
  Block level -- C2 RESULT named block (## C2 RESULT -- [Role Name]):
    C-37: In the C2 RESULT block, enumerate receipt fields (a)-(e) with PRESENT/ABSENT.
    C-39: Put per-field evidence and terminal verdict in the same block; handle the
          UNSATISFIED path inline; do not use a separate fence.
    Auditable by reading the C2 RESULT block alone.
  Table-column level -- findings table header row:
    C-38: In the F-01 IA-RESPONSE row, use [IA-VERDICT] and [ROLE-MECHANISM] as named
          schema slots visible in the output.
    C-40: Make [IA-VERDICT] and [ROLE-MECHANISM] column headers -- not cell labels.
          Slot compliance is O(1) column-count check.
    Eliminated [C-46]: do not use the inline-cell-label path for [IA-VERDICT]/[ROLE-MECHANISM].
          The column-header form (C-40) supersedes the cell-label form (C-38). This
          negation is auditable by label-matching "Eliminated [C-46]:" without parsing C-40.
          Declaration: see "Closed paths [C-43]:" in pipeline declaration [C-45]. [C-49]
    Auditable by counting table columns alone; negation auditable by label-scan.
  Each level is independently auditable without reading adjacent levels.
  No two criterion families share a level.
  Audit loop closed [C-50]: "Closed paths [C-43]:" and "Eliminated [C-46]:" cross-reference
    each other bidirectionally -- traversable from either endpoint without reading
    intervening content.

Closed paths [C-43]:
  Do not use the inline-cell-label "or" path ("[IA-VERDICT: X] | [ROLE-MECHANISM: Y]" in
  a single Description cell). It satisfies C-38 but is C-40 noncompliant.
  Use only the column-header form: separate named [IA-VERDICT] and [ROLE-MECHANISM] columns.
  A reviewer can verify the closed path by name without reading format rules [C-45].
  Path negation: see "Eliminated [C-46]:" in structural enforcement levels above [C-46].

---

**PHASE A -- ROUTE**

## Phase A: Routing

Build a routing table. Give every file a row. Cite the exact org.yaml scope pattern for
each role. If a file has no matching pattern, write:
`COVERAGE GAP: [file] -- no org.yaml scope pattern covers this path.`

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern] |
| (all files) | default | Inertia Advocate | default -- always included |

---

**PHASE B -- INERTIA REVIEW**

Entry: Phase A exit met.

Write the Budget verdict as exactly three separate labeled lines below the separator.
Start each line with its clause label. Do not embed any clause in a table cell, in the
Conclusion of another clause, or on the same line as another clause.

## Phase B: Inertia Advocate

State the null hypothesis: The codebase currently [does X via mechanism Y].     <- B1

Fill the cost ledger:                                                            <- B2

| Cost Category     | Current-State Cost                             | Adoption Cost (this PR)                 | Net                      |
|-------------------|------------------------------------------------|-----------------------------------------|--------------------------|
| Maintenance       | [LOW/MED/HIGH -- maintaining current path]     | [maintaining new path post-merge]       | WORSE / BETTER / NEUTRAL |
| Incident exposure | [failure risk/severity under status quo]       | [residual exposure after merge]         | WORSE / BETTER / NEUTRAL |
| Integration cost  | [coordination overhead of current approach]    | [churn, downstream wiring, test burden] | WORSE / BETTER / NEUTRAL |
| Regression risk   | [risk of new failures from current approach]   | [risk introduced by this PR]            | WORSE / BETTER / NEUTRAL |

---
WORSE rows: [Cost Categories where Net = WORSE, or "none"]               <- B3 line 1 [C-25]
BETTER rows: [Cost Categories where Net = BETTER, or "none"]             <- B3 line 2 [C-25]
Conclusion: [one sentence -- is adoption justified?]                     <- B3 line 3 [C-25]

Budget strength: HIGH / MEDIUM / LOW                                      <- B4

Findings:
F-01 [P1/P2/P3] [argument current state is sufficient]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second argument grounded in cost ledger]
     Owner: [role] | Resolution: [action]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS -- [one sentence in cost terms]      <- B5

Check: are B1-B5 all present? Are all three Budget verdict lines on separate lines?
Phase B exit: yes to all.

---

**PHASE C -- TECHNICAL REVIEWS**

**C1 -- Run the Phase B Exit Pre-Flight [C-26/C1, scope: Phase B completeness]:**

## Phase C Pre-Flight (C1)

Check each item:
[ ] B1 -- Null hypothesis stated
[ ] B2 -- Cost ledger: 4 rows x 2 columns x Net direction per row
[ ] B3 -- Budget verdict: three labeled lines present
         "WORSE rows:" on own line? [yes/no]
         "BETTER rows:" on own line? [yes/no]
         "Conclusion:" on own line? [yes/no] -- all must be yes
[ ] B4 -- Budget strength terminal field
[ ] B5 -- IA verdict in cost terms

If all checked: C1 RESULT: ALL CLEAR
If any unchecked: C1 RESULT: BLOCKED -- [B-number]

C1 scope is Phase B only. Do not use C1 to confirm any role's READ RECEIPT content.

**For each routed role, write steps 1-4 in this exact sequence.
Role order: security/compliance -> domain-specific -> PM/TPM.**

**STEP 1 -- Write the READ RECEIPT now, before any C2 RESULT for this role [C-35/C-36]:**

## IA READ RECEIPT -- [Role Name]

(a) Section read:        Phase B -- Inertia Advocate
(b) Budget verdict:
      WORSE rows:        [restate Phase B "WORSE rows:" line verbatim]
      BETTER rows:       [restate Phase B "BETTER rows:" line verbatim]
      Conclusion:        [restate Phase B "Conclusion:" line accurately]
(c) Budget strength:     HIGH / MEDIUM / LOW [from Phase B terminal field]
(d) Ledger row:          [Maintenance / Incident exposure / Integration cost / Regression risk]
(e) Initial position:    [CONFIRMS / DISPUTES] Net direction on [row (d)]
                         [one phrase -- domain knowledge and Phase B ledger only]

**STEP 2 -- Write the C2 RESULT block now [C-33, C-37, C-39, C-26/C2].
Do not write this block before STEP 1 -- that is a Phase C exit-condition failure.**

Enumerate all five receipt fields (a)-(e) with PRESENT or ABSENT. Derive the terminal
verdict from the per-field lines above it. Put everything in this one block. Do not use a
separate fence for the UNSATISFIED path. The reviewer must be able to verify both the
per-field evidence and the terminal verdict by reading this block alone [C-39].

## C2 RESULT -- [Role Name]

(a) Section read named:       PRESENT / ABSENT
(b) Budget verdict populated: PRESENT / ABSENT
(c) Budget strength stated:   PRESENT / ABSENT
(d) Ledger row named:         PRESENT / ABSENT
(e) Initial position stated:  PRESENT / ABSENT
    [valid: inline value OR cross-reference "see PRE-COMMITMENT block: [row]"]

[derive terminal verdict from per-field lines above -- write exactly one:]
All five PRESENT:  C2 RESULT: SATISFIED -- all five fields PRESENT
Any ABSENT:        C2 RESULT: UNSATISFIED -- field (x): [label of absent field]

**STEP 3 -- Write the PRE-COMMITMENT block before reading the diff [C-27]:**

PRE-COMMITMENT: [Role Name]

Cost row assessed:  [Maintenance / Incident exposure / Integration cost / Regression risk]
Initial position:   [CONFIRMS / DISPUTES] [Net direction] on [Cost row]
                    [one phrase based on domain knowledge + Phase B ledger]
Basis:              Domain knowledge only. PR diff not yet examined.
                    [one sentence naming the code surface or architectural pattern]

[PRE-COMMITMENT SEALED]

**STEP 4 -- Now read the diff. Write the findings table [C-34, C-38, C-40, C-43].**

Before including any finding, run the domain-lens gate:
  Ask: "Would only [this role] raise this finding, given their domain?" YES -> include.
  NO -> revise to name domain-owned mechanism. Still NO -> drop.

The findings table must have a Type column. F-01 must have Type = IA-RESPONSE.
Use [IA-VERDICT] and [ROLE-MECHANISM] as column headers -- not cell labels.

## Phase C: [Role Name]

Source files:  [from Phase A routing]
Orientation:   [one phrase from .craft/roles/]

[STEP 1: READ RECEIPT]
[STEP 2: C2 RESULT -- enumerate (a)-(e) with PRESENT/ABSENT; terminal verdict in same block]
[STEP 3: PRE-COMMITMENT]

Findings:

| ID | Type | Severity | [IA-VERDICT] | [ROLE-MECHANISM] | Domain-Lens | Owner | Resolution |
|----|------|----------|--------------|------------------|-------------|-------|------------|
| F-01 | IA-RESPONSE | P1/P2/P3 | [IA's verdict or cost position from Phase B] | [specific code artifact in this role's domain] | Passed | [role] | [action] |
| F-02 | DOMAIN | P1/P2/P3 | -- | [domain finding] | Passed | [role] | [action] |
[minimum 2]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3

Post-commitment delta:
  Pre-committed:   [CONFIRMS / DISPUTES] [Cost row]
  After findings:  [HELD / CHANGED]
  If HELD:         [code artifact from diff that confirmed the position]
  If CHANGED:      [code artifact that changed it; revised position]

F-01 format rules [C-34, C-38, C-40, C-43]:
- Type cell: write exactly "IA-RESPONSE" -- no other value passes
- Use [IA-VERDICT] and [ROLE-MECHANISM] as column headers. Do not embed them as cell labels.
  A reviewer counts columns to verify -- O(1) check.
- Do not use the inline-cell-label path ("[IA-VERDICT: X] | [ROLE-MECHANISM: Y]" in one
  Description cell). It satisfies C-38 but fails C-40. (See CLOSED PATHS [C-45] and
  Eliminated [C-46] sub-entry [C-46] in the pipeline declaration.)
- F-01: put the IA's verdict in [IA-VERDICT]; put the specific code artifact in [ROLE-MECHANISM].
- F-02 onward (DOMAIN): write "--" in [IA-VERDICT] and [ROLE-MECHANISM].

Phase C exit: C1 ALL CLEAR; every C2 RESULT block has (a)-(e) with PRESENT/ABSENT and
terminal verdict in same block [C-33, C-37, C-39]; READ RECEIPT before C2 RESULT per role
[C-35/C-36]; PRE-COMMITMENT before findings [C-27]; [IA-VERDICT] and [ROLE-MECHANISM] are
column headers [C-34/C-38/C-40]; "Eliminated [C-46]:" sub-entry carries reverse reference
[C-41, C-46, C-49]; CLOSED PATHS in declaration [C-43, C-45]; symmetry declared [C-50].

---

**PHASE D -- SYNTHESIS**

Entry: Phase C exit met (C-36, C-37/C-39, C-38/C-40, C-41/C-46, C-43/C-45, C-49/C-50).

## Phase D: Consensus

Write the IA cost ledger summary:
  Budget strength was [HIGH / MEDIUM / LOW].
  WORSE rows were: [restate]. BETTER rows were: [restate].
  Technical roles [reinforced / challenged / defeated] the IA's estimate.
  Net: [one sentence]

Find agreement: [area] -- [role-A] and [role-B] independently raised [concern]

Find divergence: [role-A] rates [area] P[N]; [role-B] rates P[N].
  Write the Mechanism: [architectural property of the code -- not perspective difference]

Name the critical finding: [F-XX from role] -- [why this most threatens the merge]

Check every Mechanism line against the ban-to-fix table:

| Banned | Replacement |
|---|---|
| "they have different perspectives" | "[role-A] sees [mechanism X]; [role-B] sees [mechanism Y]" |
| "they prioritize differently" | "[path X] is in [role-A]'s domain, outside [role-B]'s" |
| "they see this through different lenses" | "change affects [A] in [role-A]'s domain and [B] in [role-B]'s" |
| "from [role]'s perspective" as sole cause | name the architectural fact causing risk |
| "their roles lead them to different conclusions" | "[role-A]'s scope includes [surface X]; [role-B]'s does not" |

A Mechanism line with a banned phrase fails even if a code mechanism is also named. Fix it.

Phase D exit: consensus written; every Mechanism line passes the ban-to-fix check.

---

**PHASE E -- DECISION**

Entry: Phase D exit met.

## Phase E: Recommendation

Write exactly one decision: GO / NO-GO / GO WITH CONDITIONS
Cite the primary finding: [F-XX from role] -- [one sentence]

If GO WITH CONDITIONS, list conditions:
1. [what must be resolved] -- sign-off: [role who confirms before merge]

Do not delegate. Do not hedge. GO, NO-GO, or GO WITH CONDITIONS -- pick one.

---

**AMEND**

When invoked with an AMEND directive, write this block before Phase A.

## AMEND SCOPE

What was amended:           [description]
Roles added:                [list, or "none"]
Roles removed:              [list, or "none"]
Files triggering addition:  [list, or "n/a -- manually directed"]
Prior findings superseded:  [F-IDs, or "none -- first run"]

Run Phases A-E with the amended scope.
```

---

## V-04 — Role Sequence + Lifecycle Emphasis (Domain-First + Entry/Exit Banners)

**Axis**: Role Sequence (domain-specific first, then security/compliance, then PM/TPM) combined
with Lifecycle Emphasis (explicit ENTRY GATE and EXIT GATE banners at each phase transition,
each carrying a self-check checklist).

**Hypothesis**: Entry/exit banners create hard structural anchors that the model processes
discretely rather than as continuous prose. The model must satisfy the entry checklist before
generating phase content and verify the exit checklist before advancing. Combined with
domain-first role ordering, Phase C gains the additional property that domain mechanisms are
named before security scrutinizes them. Structural compliance (C-49, C-50) is unaffected.

```
You are running `/corps-pr`. This skill runs as a five-phase pipeline. Eleven structural
compliance mechanisms are active: string-matchable Budget verdict (C-25), named result
tokens (C-26), PRE-COMMITMENT blocks (C-27), receipt-completeness / ordering pair
(C-33 + C-35), ordering as phase-gate failure (C-36), self-contained per-field C2 RESULT
block (C-37 + C-39), F-01 IA-RESPONSE column-header schema (C-34 + C-38 + C-40),
three-level structural enforcement partition with named path-negation sub-entry (C-41 + C-46),
CLOSED PATHS enumeration in pipeline declaration with format-rules restatement (C-43 + C-45),
and Eliminated-to-CLOSED-PATHS reverse cross-reference with bidirectional symmetry declaration
(C-49 + C-50).
Read the full pipeline declaration before producing any output.

---

**PIPELINE DECLARATION**

Phase A -- Route
  Entry:    org.yaml + PR diff + .craft/roles/ loaded
  Exit:     Routing table complete; every file has a row; every role cites exact scope
            pattern; coverage gaps declared
  Gates:    C-01, C-06

Phase B -- Inertia Review
  Entry:    Phase A exit met
  Exit:     (B1) Null hypothesis stated
            (B2) Cost ledger: 4 rows x 2 columns x Net direction per row filled
            (B3) Budget verdict: three separate labeled lines [C-25]
                 "WORSE rows: [values]" on its own line
                 "BETTER rows: [values]" on its own line
                 "Conclusion: [text]" on its own line
            (B4) Budget strength declared as terminal field below separator
            (B5) IA verdict in cost terms
  Gates:    C-11, C-17, C-19, C-21, C-25

Phase C -- Technical Reviews
  Entry:    Two sub-conditions, each producing an exact result token [C-26]:
            C1 (Phase B exit pre-flight, phase-level):
              Scope: Phase B completeness.
              Terminal: C1 RESULT: ALL CLEAR
              or C1 RESULT: BLOCKED -- [B-number]
            C2 (READ RECEIPT completeness, per-role) [C-33]:
              Scope: receipt fields (a)-(e) complete. NOT Phase B re-check.
              C2 RESULT block enumerates (a)-(e) with PRESENT/ABSENT per field [C-37].
              Per-field evidence and terminal verdict co-appear in same block [C-39].
              C2 RESULT must appear after READ RECEIPT block in output [C-35].
              Terminal (within the C2 RESULT block): C2 RESULT: SATISFIED [all five PRESENT]
              or C2 RESULT: UNSATISFIED -- field (x): [label] [ABSENT field named inline]
  Exit:     (1) C1 ends in ALL CLEAR
            (2) All C2 blocks end in SATISFIED
            (3) READ RECEIPT precedes C2 RESULT per role in the output [C-35/C-36] --
                a C2 RESULT line that appears before its role's READ RECEIPT block is a
                Phase C exit-condition failure; Phase D does not begin
            (4) C2 RESULT block enumerates receipt fields (a)-(e) with PRESENT/ABSENT per
                field; terminal verdict derives within same block; no cross-block reading
                required [C-33, C-37, C-39]
            (5) PRE-COMMITMENT blocks precede findings tables [C-27]
            (6) F-01 in every findings table: Type = IA-RESPONSE; [IA-VERDICT] and
                [ROLE-MECHANISM] are column headers; slot compliance is O(1) column-count
                [C-34, C-38, C-40]; pipeline declaration CLOSED PATHS names the
                prohibited inline-cell-label path [C-43, C-45]
            (7) All findings passed domain-lens gate
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26, C-27, C-33, C-34,
            C-35, C-36, C-37, C-38, C-39, C-40, C-41, C-43, C-44, C-45, C-46

Phase D -- Synthesis
  Entry:    Phase C exit met (all 7 conditions including C-36 ordering, C-37/C-39
            self-contained block, C-38/C-40 column-header schema, C-41/C-46 declared
            partition + named negation sub-entry, C-43/C-45 CLOSED PATHS + format-rules
            restatement, C-49/C-50 reverse cross-reference + bidirectional symmetry)
  Exit:     Consensus complete; all Mechanism lines pass ban-to-fix check
  Gates:    C-03, C-09, C-12, C-13

Phase E -- Decision
  Entry:    Phase D exit met
  Exit:     Exactly one GO / NO-GO / GO WITH CONDITIONS; conditions name sign-off
  Gates:    C-04, C-10

Structural enforcement levels [C-41]:
  Exit-condition level -- Phase C exit checklist item (3):
    C-36: READ RECEIPT-before-C2-RESULT ordering is a Phase C exit-condition violation
          when not met; Phase D does not begin. Auditable by reading exit item (3) alone.
  Block level -- C2 RESULT named block (## C2 RESULT -- [Role Name]):
    C-37: C2 RESULT block enumerates receipt fields (a)-(e) with PRESENT/ABSENT per field.
    C-39: Per-field evidence and terminal verdict co-appear in the same named block;
          no cross-block reading required; UNSATISFIED path handled inline.
    Auditable by reading the C2 RESULT block alone.
  Table-column level -- findings table header row:
    C-38: F-01 IA-RESPONSE Description field declares [IA-VERDICT] and [ROLE-MECHANISM]
          as named schema slots visible in output.
    C-40: [IA-VERDICT] and [ROLE-MECHANISM] are column headers in the findings table;
          slot compliance is O(1) column-count check.
    Eliminated [C-46]: no inline-cell alternative path for [IA-VERDICT]/[ROLE-MECHANISM].
          The column-header form (C-40, table-column level) supersedes the cell-label form
          (C-38, block level). This negation is declared independently of C-40's description
          and is auditable by label-matching "Eliminated [C-46]:" without parsing C-40.
          Declaration: see "Closed paths [C-43]:" in pipeline declaration [C-45]. [C-49]
    Auditable by counting table columns alone; negation auditable by label-scan.
  Each level is independently auditable without reading adjacent levels.
  No two criterion families share a level.
  Audit loop closed [C-50]: "Closed paths [C-43]:" and "Eliminated [C-46]:" cross-reference
    each other bidirectionally -- traversable from either endpoint without reading
    intervening content.

Closed paths [C-43]:
  C-40 (table-column level) supersedes C-38 (block level) for F-01 Description schema.
  The inline-cell-label "or" path ("[IA-VERDICT: X] | [ROLE-MECHANISM: Y]" in a single
  Description cell) satisfies C-38 but is C-40 noncompliant -- do not use it.
  Only the column-header form (separate named [IA-VERDICT] and [ROLE-MECHANISM] columns)
  satisfies the table-column level requirement. A reviewer auditing this section can verify
  the closed path by name without reading format rules [C-45].
  Path negation: see "Eliminated [C-46]:" in structural enforcement levels above [C-46].

---

=== ENTRY GATE: PHASE A ===
Required: org.yaml loaded | PR diff loaded | .craft/roles/ loaded
If any not loaded: STOP -- state what is missing.
=== BEGIN PHASE A ===

**PHASE A -- ROUTE**

## Phase A: Routing

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern] |
| (all files) | default | Inertia Advocate | default -- always included |

Coverage gap: `COVERAGE GAP: [file] -- no org.yaml scope pattern covers this path.`

=== EXIT GATE: PHASE A ===
[ ] Every file has a row
[ ] Every role cites exact scope pattern
[ ] Coverage gaps declared (or "none")
All checked -> proceed to Phase B.
=== PHASE A COMPLETE ===

---

=== ENTRY GATE: PHASE B ===
Required: Phase A EXIT GATE all checked.
=== BEGIN PHASE B ===

**PHASE B -- INERTIA REVIEW**

The Budget verdict appears as exactly three separate labeled lines below the separator.
Each line begins with its clause label. No clause is embedded in a table cell, in the
Conclusion of another clause, or merged with another clause on the same line.

## Phase B: Inertia Advocate

Null hypothesis: The codebase currently [does X via mechanism Y].           <- B1

Cost ledger:                                                                 <- B2

| Cost Category     | Current-State Cost                             | Adoption Cost (this PR)                 | Net                      |
|-------------------|------------------------------------------------|-----------------------------------------|--------------------------|
| Maintenance       | [LOW/MED/HIGH -- maintaining current path]     | [maintaining new path post-merge]       | WORSE / BETTER / NEUTRAL |
| Incident exposure | [failure risk/severity under status quo]       | [residual exposure after merge]         | WORSE / BETTER / NEUTRAL |
| Integration cost  | [coordination overhead of current approach]    | [churn, downstream wiring, test burden] | WORSE / BETTER / NEUTRAL |
| Regression risk   | [risk of new failures from current approach]   | [risk introduced by this PR]            | WORSE / BETTER / NEUTRAL |

---
WORSE rows: [Cost Categories where Net = WORSE, or "none"]               <- B3 line 1 [C-25]
BETTER rows: [Cost Categories where Net = BETTER, or "none"]             <- B3 line 2 [C-25]
Conclusion: [one sentence -- is adoption justified?]                     <- B3 line 3 [C-25]

Budget strength: HIGH / MEDIUM / LOW                                      <- B4

Findings:
F-01 [P1/P2/P3] [argument current state is sufficient]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second argument grounded in cost ledger]
     Owner: [role] | Resolution: [action]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS -- [one sentence in cost terms]      <- B5

=== EXIT GATE: PHASE B ===
[ ] B1 -- Null hypothesis stated
[ ] B2 -- Cost ledger: 4 rows x 2 columns x Net direction
[ ] B3 -- "WORSE rows:" on own line AND "BETTER rows:" on own line AND "Conclusion:" on own line
[ ] B4 -- Budget strength terminal field present
[ ] B5 -- IA verdict in cost terms present
All checked -> C1 RESULT: ALL CLEAR. Any unchecked -> C1 RESULT: BLOCKED -- [B-number].
=== PHASE B COMPLETE ===

---

=== ENTRY GATE: PHASE C ===
Required: Phase B EXIT GATE all checked; C1 RESULT: ALL CLEAR written.
Role sequence: domain-specific -> security/compliance -> PM/TPM.
=== BEGIN PHASE C ===

**PHASE C -- TECHNICAL REVIEWS**

**C1 -- Phase B Exit Pre-Flight [C-26/C1]:**
(C1 exit gate output is the Phase B EXIT GATE block above -- write C1 RESULT from it.)

**Per-role sequence: domain-specific -> security/compliance -> PM/TPM.**
For each role, execute steps 1-4 in strict sequence before advancing to the next role.

**STEP 1 -- READ RECEIPT [write before any C2 RESULT for this role -- C-35/C-36]:**

## IA READ RECEIPT -- [Role Name]

(a) Section read:        Phase B -- Inertia Advocate
(b) Budget verdict:
      WORSE rows:        [restate Phase B "WORSE rows:" line verbatim]
      BETTER rows:       [restate Phase B "BETTER rows:" line verbatim]
      Conclusion:        [restate Phase B "Conclusion:" line accurately]
(c) Budget strength:     HIGH / MEDIUM / LOW [from Phase B terminal field]
(d) Ledger row:          [Maintenance / Incident exposure / Integration cost / Regression risk]
(e) Initial position:    [CONFIRMS / DISPUTES] Net direction on [row (d)]
                         [one phrase -- domain knowledge and Phase B ledger only]

**STEP 2 -- C2 RESULT BLOCK [must follow STEP 1; C-33, C-37, C-39, C-26/C2]:**

The C2 RESULT block enumerates all five receipt fields (a)-(e) by label with an explicit
PRESENT or ABSENT verdict per field. The terminal C2 RESULT line derives from the per-field
verdicts above it and appears within this same block. C2 scope is receipt completeness -- not
Phase B. The UNSATISFIED path is handled within this block -- not in a separate adjacent fence.
No cross-block reading required [C-39].

## C2 RESULT -- [Role Name]

(a) Section read named:       PRESENT / ABSENT
(b) Budget verdict populated: PRESENT / ABSENT
(c) Budget strength stated:   PRESENT / ABSENT
(d) Ledger row named:         PRESENT / ABSENT
(e) Initial position stated:  PRESENT / ABSENT
    [valid: inline value OR cross-reference "see PRE-COMMITMENT block: [row]"]

[derive terminal verdict from per-field lines above -- write exactly one:]
All five PRESENT:  C2 RESULT: SATISFIED -- all five fields PRESENT
Any ABSENT:        C2 RESULT: UNSATISFIED -- field (x): [label of absent field]

**STEP 3 -- PRE-COMMITMENT [C-27, before reading diff]:**

PRE-COMMITMENT: [Role Name]

Cost row assessed:  [Maintenance / Incident exposure / Integration cost / Regression risk]
Initial position:   [CONFIRMS / DISPUTES] [Net direction] on [Cost row]
                    [one phrase based on domain knowledge + Phase B ledger]
Basis:              Domain knowledge only. PR diff not yet examined.
                    [one sentence naming the code surface or architectural pattern]

[PRE-COMMITMENT SEALED]

**STEP 4 -- FINDINGS [C-34, C-38, C-40, C-43]:**

Apply domain-lens gate per finding:

Step A: "Would only [this role] raise this finding, given their domain?"
  YES -> include. NO -> Step B.
Step B: Revise to name domain-owned mechanism. Still NO -> drop.

## Phase C: [Role Name]

Source files:  [from Phase A routing]
Orientation:   [one phrase from .craft/roles/]

[STEP 1: READ RECEIPT]
[STEP 2: C2 RESULT -- (a)-(e) + terminal verdict in same block, no separate fence]
[STEP 3: PRE-COMMITMENT]

Findings:

| ID | Type | Severity | [IA-VERDICT] | [ROLE-MECHANISM] | Domain-Lens | Owner | Resolution |
|----|------|----------|--------------|------------------|-------------|-------|------------|
| F-01 | IA-RESPONSE | P1/P2/P3 | [IA's verdict or cost position from Phase B] | [specific code artifact in this role's domain] | Passed | [role] | [action] |
| F-02 | DOMAIN | P1/P2/P3 | -- | [domain finding] | Passed | [role] | [action] |
[minimum 2]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3

Post-commitment delta:
  Pre-committed:   [CONFIRMS / DISPUTES] [Cost row]
  After findings:  [HELD / CHANGED]
  If HELD:         [code artifact from diff that confirmed the position]
  If CHANGED:      [code artifact that changed it; revised position]

F-01 IA-RESPONSE format rules [C-34, C-38, C-40, C-43]:
- Type cell: exactly "IA-RESPONSE"
- [IA-VERDICT] and [ROLE-MECHANISM] are column headers. O(1) column-count verification.
- Prohibition [C-43]: do not use inline-cell-label path. See CLOSED PATHS [C-45] and
  Eliminated [C-46] sub-entry [C-46].
- DOMAIN findings (F-02 onward): "--" in [IA-VERDICT] and [ROLE-MECHANISM].

=== EXIT GATE: PHASE C ===
[ ] C1 RESULT: ALL CLEAR written (Phase B scope)
[ ] Every C2 RESULT block: (a)-(e) enumerated with PRESENT/ABSENT; terminal verdict in same block
[ ] READ RECEIPT precedes C2 RESULT for every role (ordering violation = exit-condition failure)
[ ] PRE-COMMITMENT precedes findings for every role
[ ] F-01 Type=IA-RESPONSE; [IA-VERDICT] and [ROLE-MECHANISM] as column headers
[ ] "Eliminated [C-46]:" sub-entry present with C-49 reverse cross-reference
[ ] CLOSED PATHS block present in pipeline declaration
[ ] "Audit loop closed [C-50]:" declaration present
[ ] All findings passed domain-lens gate
All checked -> proceed to Phase D.
=== PHASE C COMPLETE ===

---

=== ENTRY GATE: PHASE D ===
Required: Phase C EXIT GATE all checked.
=== BEGIN PHASE D ===

**PHASE D -- SYNTHESIS**

## Phase D: Consensus

IA cost ledger: Budget strength was [HIGH / MEDIUM / LOW].
  WORSE rows were: [restate]. BETTER rows were: [restate].
  Technical roles collectively [reinforced / challenged / defeated] the IA's estimate.
  Net: [one sentence]

Agreement: [area] -- [role-A] and [role-B] independently raised [concern]

Divergence: [role-A] rates [area] P[N]; [role-B] rates P[N].
  Mechanism: [architectural property of the code -- not perspective difference]

Critical: [F-XX from role] -- [why this most threatens the merge]

Perspective-label ban-to-fix:

| Banned | Replacement |
|---|---|
| "they have different perspectives" | "[role-A] sees [mechanism X]; [role-B] sees [mechanism Y]" |
| "they prioritize differently" | "[path X] is in [role-A]'s domain, outside [role-B]'s" |
| "they see this through different lenses" | "change affects [A] in [role-A]'s domain and [B] in [role-B]'s" |
| "from [role]'s perspective" as sole cause | name the architectural fact causing risk |
| "their roles lead them to different conclusions" | "[role-A]'s scope includes [surface X]; [role-B]'s does not" |

A Mechanism line with a banned phrase fails even if a code mechanism is also named.

=== EXIT GATE: PHASE D ===
[ ] Consensus written
[ ] Every Mechanism line passes the ban-to-fix check
All checked -> proceed to Phase E.
=== PHASE D COMPLETE ===

---

=== ENTRY GATE: PHASE E ===
Required: Phase D EXIT GATE all checked.
=== BEGIN PHASE E ===

**PHASE E -- DECISION**

## Phase E: Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from role] -- [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] -- sign-off: [role who confirms before merge]

One decision. Values: GO, NO-GO, GO WITH CONDITIONS only.
Delegated decisions fail. Hedged decisions fail.

=== EXIT GATE: PHASE E ===
[ ] Exactly one GO / NO-GO / GO WITH CONDITIONS written
[ ] Primary finding cited
[ ] Conditions name sign-off (if GO WITH CONDITIONS)
=== PHASE E COMPLETE -- PIPELINE DONE ===

---

**AMEND**

When invoked with an AMEND directive, output this named-field block before Phase A.

## AMEND SCOPE

What was amended:           [description]
Roles added:                [list, or "none"]
Roles removed:              [list, or "none"]
Files triggering addition:  [list, or "n/a -- manually directed"]
Prior findings superseded:  [F-IDs, or "none -- first run"]

Run Phases A-E with the amended scope.
```

---

## V-05 — Full Combination (Inertia Framing + Output Format + Phrasing Register)

**Axis**: Inertia Framing (IA is status-quo champion; PR must defeat the null) + Output Format
(Phase E scorecard table) + Phrasing Register (second-person imperative). This is the same
combination as R17 V-05 which achieved 40/40 -- now carrying C-49 and C-50 in the invariant
structural core.

**Hypothesis**: R17 V-05's combination of adversarial IA framing, forced scorecard enumeration,
and imperative register drove the cleanest structural compliance. Adding C-49 and C-50 to the
same combination should produce 42/42 without introducing regressions, because the new
declarations extend existing structural elements rather than introducing new phases.

```
You are running `/corps-pr`. The Inertia Advocate is the status-quo champion: Phase B
requires the PR to defeat the null hypothesis, not merely document it. Run this as a
five-phase pipeline. You have eleven structural compliance rules to enforce: write a
string-matchable Budget verdict (C-25), produce named result tokens for every gate (C-26),
write PRE-COMMITMENT blocks before reading the diff (C-27), verify receipt completeness
before ordering (C-33 + C-35), treat ordering violations as phase-gate failures (C-36),
put all five receipt fields and the terminal verdict in the same C2 RESULT block (C-37 + C-39),
use [IA-VERDICT] and [ROLE-MECHANISM] as column headers in every findings table
(C-34 + C-38 + C-40), declare a three-level structural enforcement partition with a named
path-negation sub-entry (C-41 + C-46), put CLOSED PATHS in the pipeline declaration with a
format-rules restatement (C-43 + C-45), and carry the reverse cross-reference and
bidirectional symmetry declaration (C-49 + C-50).
Read the full pipeline declaration before writing any output.

---

**PIPELINE DECLARATION**

Phase A -- Route
  Entry:    Load org.yaml + PR diff + .craft/roles/
  Exit:     Every file has a routing row; every role cites its exact scope pattern;
            coverage gaps declared
  Gates:    C-01, C-06

Phase B -- Inertia Review
  Entry:    Phase A exit met.
            IA role: status-quo champion. Adoption requires demonstrating net improvement
            over doing nothing. The default verdict is BLOCK until the cost ledger shows
            otherwise.
  Exit:     (B1) Status-quo position stated
            (B2) Cost ledger: 4 rows x 2 columns x Net direction per row filled
            (B3) Budget verdict: three separate labeled lines [C-25]
                 "WORSE rows: [values]" on its own line
                 "BETTER rows: [values]" on its own line
                 "Conclusion: [text]" on its own line
            (B4) Budget strength declared as terminal field below separator
            (B5) IA verdict in cost terms -- does this PR defeat the status quo?
  Gates:    C-11, C-17, C-19, C-21, C-25

Phase C -- Technical Reviews
  Entry:    Two sub-conditions, each producing an exact result token [C-26]:
            C1 (Phase B exit pre-flight, phase-level):
              Scope: Phase B completeness.
              Write: C1 RESULT: ALL CLEAR
              or: C1 RESULT: BLOCKED -- [B-number]
            C2 (READ RECEIPT completeness, per-role) [C-33]:
              Scope: receipt fields (a)-(e) complete. NOT Phase B re-check.
              Enumerate (a)-(e) with PRESENT/ABSENT in the C2 RESULT block [C-37].
              Put per-field evidence and terminal verdict in the same block [C-39].
              Write C2 RESULT after READ RECEIPT in output [C-35].
              Write: C2 RESULT: SATISFIED [all five PRESENT]
              or: C2 RESULT: UNSATISFIED -- field (x): [label] [ABSENT field named inline]
  Exit:     (1) C1 ends in ALL CLEAR
            (2) Every C2 block ends in SATISFIED
            (3) Write READ RECEIPT before C2 RESULT for each role [C-35/C-36] --
                if C2 RESULT appears before READ RECEIPT, stop: Phase C exit-condition
                failure; do not begin Phase D
            (4) In every C2 RESULT block, enumerate (a)-(e) with PRESENT/ABSENT; derive
                the terminal verdict in the same block [C-33, C-37, C-39]
            (5) Write PRE-COMMITMENT blocks before findings tables [C-27]
            (6) In every findings table, F-01 must have Type = IA-RESPONSE; use
                [IA-VERDICT] and [ROLE-MECHANISM] as column headers [C-34, C-38, C-40];
                the pipeline CLOSED PATHS block names the prohibited path [C-43, C-45]
            (7) Pass every finding through the domain-lens gate before including it
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26, C-27, C-33, C-34,
            C-35, C-36, C-37, C-38, C-39, C-40, C-41, C-43, C-44, C-45, C-46

Phase D -- Synthesis
  Entry:    Phase C exit met (all 7 conditions: C-36, C-37/C-39, C-38/C-40, C-41/C-46,
            C-43/C-45, C-49/C-50)
  Exit:     Write consensus; every Mechanism line passes ban-to-fix check
  Gates:    C-03, C-09, C-12, C-13

Phase E -- Decision
  Entry:    Phase D exit met
  Exit:     (E1) Write exactly one GO / NO-GO / GO WITH CONDITIONS; name sign-off in conditions
            (E2) Cite primary finding
            (E3) Write findings scorecard: every routed role has a row; P1/P2/P3 columns
                 tallied; IA verdict row present; Merge gate line states unresolved-P1 rule
  Gates:    C-04, C-10

Structural enforcement levels [C-41]:
  Exit-condition level -- Phase C exit checklist item (3):
    C-36: If you write a C2 RESULT terminal line before the READ RECEIPT header for that
          role, that is a Phase C exit-condition failure -- stop; do not begin Phase D.
          Auditable by reading exit item (3) alone.
  Block level -- C2 RESULT named block (## C2 RESULT -- [Role Name]):
    C-37: In the C2 RESULT block, enumerate receipt fields (a)-(e) with PRESENT/ABSENT.
    C-39: Put per-field evidence and terminal verdict in the same block; handle the
          UNSATISFIED path inline; do not use a separate fence.
    Auditable by reading the C2 RESULT block alone.
  Table-column level -- findings table header row:
    C-38: In the F-01 IA-RESPONSE row, use [IA-VERDICT] and [ROLE-MECHANISM] as named
          schema slots visible in the output.
    C-40: Make [IA-VERDICT] and [ROLE-MECHANISM] column headers -- not cell labels.
          Slot compliance is O(1) column-count check.
    Eliminated [C-46]: do not use the inline-cell-label path for [IA-VERDICT]/[ROLE-MECHANISM].
          The column-header form (C-40) supersedes the cell-label form (C-38). This
          negation is auditable by label-matching "Eliminated [C-46]:" without parsing C-40.
          Declaration: see "Closed paths [C-43]:" in pipeline declaration [C-45]. [C-49]
    Auditable by counting table columns alone; negation auditable by label-scan.
  Each level is independently auditable without reading adjacent levels.
  No two criterion families share a level.
  Audit loop closed [C-50]: "Closed paths [C-43]:" and "Eliminated [C-46]:" cross-reference
    each other bidirectionally -- traversable from either endpoint without reading
    intervening content.

Closed paths [C-43]:
  Do not use the inline-cell-label "or" path ("[IA-VERDICT: X] | [ROLE-MECHANISM: Y]" in
  a single Description cell). It satisfies C-38 but is C-40 noncompliant.
  Use only the column-header form: separate named [IA-VERDICT] and [ROLE-MECHANISM] columns.
  A reviewer can verify the closed path by name without reading format rules [C-45].
  Path negation: see "Eliminated [C-46]:" in structural enforcement levels above [C-46].

---

**PHASE A -- ROUTE**

## Phase A: Routing

Build a routing table. Give every file a row. Cite the exact org.yaml scope pattern.

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern] |
| (all files) | default | Inertia Advocate | default -- always included |

Coverage gap: `COVERAGE GAP: [file] -- no org.yaml scope pattern covers this path.`

---

**PHASE B -- INERTIA REVIEW**

Entry: Phase A exit met. The IA defends the status quo. The PR must demonstrate net
improvement; the default verdict is BLOCK until the cost ledger shows otherwise.

Write the Budget verdict as exactly three separate labeled lines below the separator.
Start each line with its clause label. Do not embed any clause in a table cell or on
the same line as another clause.

## Phase B: Inertia Advocate (Status-Quo Champion)

Status-quo position: The codebase currently [does X via mechanism Y]. The null:           <- B1
  doing nothing is the valid choice until shown otherwise.

Cost ledger:                                                                               <- B2

| Cost Category     | Current-State Cost                             | Adoption Cost (this PR)                 | Net                      |
|-------------------|------------------------------------------------|-----------------------------------------|--------------------------|
| Maintenance       | [LOW/MED/HIGH -- maintaining current path]     | [maintaining new path post-merge]       | WORSE / BETTER / NEUTRAL |
| Incident exposure | [failure risk/severity under status quo]       | [residual exposure after merge]         | WORSE / BETTER / NEUTRAL |
| Integration cost  | [coordination overhead of current approach]    | [churn, downstream wiring, test burden] | WORSE / BETTER / NEUTRAL |
| Regression risk   | [risk of new failures from current approach]   | [risk introduced by this PR]            | WORSE / BETTER / NEUTRAL |

---
WORSE rows: [Cost Categories where Net = WORSE, or "none"]               <- B3 line 1 [C-25]
BETTER rows: [Cost Categories where Net = BETTER, or "none"]             <- B3 line 2 [C-25]
Conclusion: [one sentence -- is adoption justified?]                     <- B3 line 3 [C-25]

Budget strength: HIGH / MEDIUM / LOW                                      <- B4

Findings:
F-01 [P1/P2/P3] [argument current state is sufficient]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second argument grounded in cost ledger]
     Owner: [role] | Resolution: [action]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS -- [one sentence: does this PR defeat the status quo?] <- B5

Check B1-B5 and the three Budget verdict lines. Phase B exit: all present.

---

**PHASE C -- TECHNICAL REVIEWS**

**C1 -- Run the Phase B Exit Pre-Flight [C-26/C1, scope: Phase B completeness]:**

## Phase C Pre-Flight (C1)

[ ] B1 -- Status-quo position stated
[ ] B2 -- Cost ledger: 4 rows x 2 columns x Net direction per row
[ ] B3 -- Budget verdict: three labeled lines present
         "WORSE rows:" on own line? [yes/no]
         "BETTER rows:" on own line? [yes/no]
         "Conclusion:" on own line? [yes/no] -- all must be yes
[ ] B4 -- Budget strength terminal field
[ ] B5 -- IA verdict in cost terms

If all checked: C1 RESULT: ALL CLEAR
If any unchecked: C1 RESULT: BLOCKED -- [B-number]

C1 scope is Phase B only. Do not use C1 to confirm any role's READ RECEIPT.

**For each routed role, write steps 1-4 in this exact sequence.
Role order: security/compliance -> domain-specific -> PM/TPM.**

**STEP 1 -- Write the READ RECEIPT now [C-35/C-36]. Do not write C2 RESULT first.**

## IA READ RECEIPT -- [Role Name]

(a) Section read:        Phase B -- Inertia Advocate (Status-Quo Champion)
(b) Budget verdict:
      WORSE rows:        [restate Phase B "WORSE rows:" line verbatim]
      BETTER rows:       [restate Phase B "BETTER rows:" line verbatim]
      Conclusion:        [restate Phase B "Conclusion:" line accurately]
(c) Budget strength:     HIGH / MEDIUM / LOW [from Phase B terminal field]
(d) Ledger row:          [Maintenance / Incident exposure / Integration cost / Regression risk]
(e) Initial position:    [CONFIRMS / DISPUTES] Net direction on [row (d)]
                         [one phrase -- domain knowledge and Phase B ledger only]

**STEP 2 -- Write the C2 RESULT block now [must follow STEP 1; C-33, C-37, C-39, C-26/C2]:**

Enumerate all five receipt fields (a)-(e) with PRESENT or ABSENT. Derive the terminal
verdict from the per-field lines. Put everything in one block. Handle UNSATISFIED inline.
A reviewer must be able to verify both the evidence and the verdict by reading this block
alone [C-39]. No separate fence.

## C2 RESULT -- [Role Name]

(a) Section read named:       PRESENT / ABSENT
(b) Budget verdict populated: PRESENT / ABSENT
(c) Budget strength stated:   PRESENT / ABSENT
(d) Ledger row named:         PRESENT / ABSENT
(e) Initial position stated:  PRESENT / ABSENT
    [valid: inline value OR cross-reference "see PRE-COMMITMENT block: [row]"]

[derive terminal verdict from per-field lines above -- write exactly one:]
All five PRESENT:  C2 RESULT: SATISFIED -- all five fields PRESENT
Any ABSENT:        C2 RESULT: UNSATISFIED -- field (x): [label of absent field]

**STEP 3 -- Write the PRE-COMMITMENT block before reading the diff [C-27]:**

PRE-COMMITMENT: [Role Name]

Cost row assessed:  [Maintenance / Incident exposure / Integration cost / Regression risk]
Initial position:   [CONFIRMS / DISPUTES] [Net direction] on [Cost row]
                    [one phrase based on domain knowledge + Phase B ledger]
Basis:              Domain knowledge only. PR diff not yet examined.
                    [one sentence naming the code surface or architectural pattern]

[PRE-COMMITMENT SEALED]

**STEP 4 -- Now read the diff. Write the findings table [C-34, C-38, C-40, C-43].**

Domain-lens gate per finding:
  Ask: "Would only [this role] raise this?" YES -> include.
  NO -> revise to name domain-owned mechanism. Still NO -> drop.

Use [IA-VERDICT] and [ROLE-MECHANISM] as column headers -- not cell labels.

## Phase C: [Role Name]

Source files:  [from Phase A routing]
Orientation:   [one phrase from .craft/roles/]

[STEP 1: READ RECEIPT]
[STEP 2: C2 RESULT -- (a)-(e) + terminal verdict in same block]
[STEP 3: PRE-COMMITMENT]

Findings:

| ID | Type | Severity | [IA-VERDICT] | [ROLE-MECHANISM] | Domain-Lens | Owner | Resolution |
|----|------|----------|--------------|------------------|-------------|-------|------------|
| F-01 | IA-RESPONSE | P1/P2/P3 | [IA's verdict or cost position from Phase B] | [specific code artifact in this role's domain] | Passed | [role] | [action] |
| F-02 | DOMAIN | P1/P2/P3 | -- | [domain finding] | Passed | [role] | [action] |
[minimum 2]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3

Post-commitment delta:
  Pre-committed:   [CONFIRMS / DISPUTES] [Cost row]
  After findings:  [HELD / CHANGED]
  If HELD:         [code artifact from diff that confirmed the position]
  If CHANGED:      [code artifact that changed it; revised position]

F-01 format rules [C-34, C-38, C-40, C-43]:
- Type cell: write exactly "IA-RESPONSE"
- Use [IA-VERDICT] and [ROLE-MECHANISM] as column headers. O(1) column-count verification.
- Do not use the inline-cell-label path. See CLOSED PATHS [C-45] and Eliminated [C-46] [C-46].
- F-01: IA's verdict in [IA-VERDICT]; specific code artifact in [ROLE-MECHANISM].
- DOMAIN findings (F-02 onward): "--" in [IA-VERDICT] and [ROLE-MECHANISM].

Phase C exit: C1 ALL CLEAR; every C2 RESULT block has (a)-(e) with PRESENT/ABSENT and
terminal verdict in same block [C-33, C-37, C-39]; READ RECEIPT before C2 RESULT per role
[C-35/C-36]; PRE-COMMITMENT before findings [C-27]; [IA-VERDICT] and [ROLE-MECHANISM] as
column headers [C-34/C-38/C-40]; "Eliminated [C-46]:" with C-49 reverse reference [C-41,
C-46, C-49]; CLOSED PATHS in declaration [C-43, C-45]; symmetry declared [C-50].

---

**PHASE D -- SYNTHESIS**

Entry: Phase C exit met (C-36, C-37/C-39, C-38/C-40, C-41/C-46, C-43/C-45, C-49/C-50).

## Phase D: Consensus

Write the IA cost ledger summary:
  Budget strength was [HIGH / MEDIUM / LOW].
  WORSE rows were: [restate]. BETTER rows were: [restate].
  Technical roles [reinforced / challenged / defeated] the IA's estimate.
  Net: [one sentence]

Find agreement: [area] -- [role-A] and [role-B] independently raised [concern]

Find divergence: [role-A] rates [area] P[N]; [role-B] rates P[N].
  Write the Mechanism: [architectural property of the code -- not perspective difference]

Name the critical finding: [F-XX from role] -- [why this most threatens the merge]

Check every Mechanism line against the ban-to-fix table:

| Banned | Replacement |
|---|---|
| "they have different perspectives" | "[role-A] sees [mechanism X]; [role-B] sees [mechanism Y]" |
| "they prioritize differently" | "[path X] is in [role-A]'s domain, outside [role-B]'s" |
| "they see this through different lenses" | "change affects [A] in [role-A]'s domain and [B] in [role-B]'s" |
| "from [role]'s perspective" as sole cause | name the architectural fact causing risk |
| "their roles lead them to different conclusions" | "[role-A]'s scope includes [surface X]; [role-B]'s does not" |

A Mechanism line with a banned phrase fails even if a code mechanism is also named. Fix it.

Phase D exit: consensus written; every Mechanism line passes.

---

**PHASE E -- DECISION**

Entry: Phase D exit met.

## Phase E: Recommendation

Write exactly one decision: GO / NO-GO / GO WITH CONDITIONS
Cite the primary finding: [F-XX from role] -- [one sentence]

If GO WITH CONDITIONS:
1. [what must be resolved] -- sign-off: [role who confirms before merge]

Write the findings scorecard:

| Role | P1 | P2 | P3 | Total |
|------|----|----|-----|-------|
| Inertia Advocate | [n] | [n] | [n] | [n] |
| [Role Name] | [n] | [n] | [n] | [n] |
| [Role Name] | [n] | [n] | [n] | [n] |
| [Role Name] | [n] | [n] | [n] | [n] |

IA verdict: [BLOCK / CONDITION / PASS from Phase B]
Merge gate: GO requires zero unresolved P1s. Current unresolved P1 count: [n].

One decision only: GO, NO-GO, or GO WITH CONDITIONS. Do not delegate. Do not hedge.

---

**AMEND**

When invoked with an AMEND directive, write this block before Phase A.

## AMEND SCOPE

What was amended:           [description]
Roles added:                [list, or "none"]
Roles removed:              [list, or "none"]
Files triggering addition:  [list, or "n/a -- manually directed"]
Prior findings superseded:  [F-IDs, or "none -- first run"]

Run Phases A-E with the amended scope.
```
