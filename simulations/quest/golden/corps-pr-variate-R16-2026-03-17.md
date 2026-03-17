---
skill: quest-variate
skill_target: corps-pr
round: 16
date: 2026-03-17
rubric_version: 14
---

# Variate R16 — corps-pr

5 complete prompt body variations for the `corps-pr` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Axes Selected

| Axis | Used In | R16 Focus |
|------|---------|----------|
| Role sequence (which roles run first in Phase C) | V-01, V-04 | Orthogonality test: C-43/44/45/46 integration should survive any Phase C sequence permutation. V-01 swaps to PM/TPM-first to verify no sequence-dependent pass/fail on the four target criteria. |
| Output format -- C-43 prohibition placement (CLOSED PATHS only vs. CLOSED PATHS + format-rules restatement) | V-02, V-05 | C-43 can be satisfied by the CLOSED PATHS block alone (V-03 R15 pattern). V-02 tests whether adding a full four-element restatement in format rules alongside the CLOSED PATHS block introduces any conflict or redundancy, and whether double coverage strengthens or complicates C-45 auditing. |
| Phrasing register -- negation statement form (inline clause appended to C-40 vs. named standalone sub-entry) | V-03, V-04, V-05 | C-46 requires "an explicit path-negation statement" in the structural enforcement levels section. R15 V-02 used an inline clause ("; no inline-cell alternative path"). V-03 tests elevating the negation to a named, labeled sub-entry with its own line ("Eliminated [C-46]: ...") to make the negation independently scannable without parsing the C-40 description. |

**Baseline (R15 V-03 against v14 rubric)**:
- C-42 passes: two-branch conditional C2 RESULT template present
- C-43 passes: CLOSED PATHS block in pipeline declaration carries all four elements
- C-44 FAILS: format rules still describe "Alternative form (C-38 compliant)" as an offered path -- declaration and template inconsistent
- C-45 passes: CLOSED PATHS block in declaration, auditable without reading format rules
- C-46 FAILS: structural enforcement levels section has no negation statement for the inline-cell-label path -- elimination is observable only by absence from template, not declared

**R16 target**: All five variations close C-44 and C-46 simultaneously with C-43 and C-45. The minimal fix from R15 V-03: (1) add "no inline-cell alternative path" to structural enforcement C-40 entry, (2) remove alternative form from format rules. Variations test whether the form of the negation statement (inline vs. named sub-entry) and the coverage of the C-43 prohibition (declaration-only vs. double coverage) affect rubric compliance.

**Predicted scores vs. v14**:

| Var | C-43 | C-44 | C-45 | C-46 | Aspirational | Composite |
|-----|------|------|------|------|--------------|-----------|
| V-01 | PASS | PASS | PASS | PASS | 38/38 | 100 |
| V-02 | PASS | PASS | PASS | PASS | 38/38 | 100 |
| V-03 | PASS | PASS | PASS | PASS | 38/38 | 100 |
| V-04 | PASS | PASS | PASS | PASS | 38/38 | 100 |
| V-05 | PASS | PASS | PASS | PASS | 38/38 | 100 |

Risk: V-01 and V-04 (PM/TPM-first sequence) may expose sequencing bugs if the CLOSED PATHS or negation constraints interact with role-order assumptions. V-02 and V-05 (double coverage) may introduce a C-43/C-45 ambiguity if a rubric scorer reads the format-rules restatement as the "primary" prohibition and misses the CLOSED PATHS block elevation.

---

## V-01 — Role Sequence: PM/TPM First

**Axis**: Role sequence (which Phase C roles execute first)
**Hypothesis**: The phase-gate constraints enforcing C-43/44/45/46 live in the pipeline declaration and structural enforcement levels section -- both are pre-read before any role executes. Role sequence (security/compliance-first vs. PM/TPM-first) is therefore orthogonal to path-closure compliance. V-01 applies the full R16 integration fix (CLOSED PATHS block + structural enforcement negation + path elimination from format rules) while swapping the Phase C sequence to PM/TPM -> domain-specific -> security/compliance. Expected: all four pass. Risk: if C-14 (IA anchoring) or C-23 (READ RECEIPT) has implicit sequence assumptions, a sequence swap may surface them.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline. Ten structural
compliance mechanisms are active: string-matchable Budget verdict (C-25), named result
tokens (C-26), PRE-COMMITMENT blocks (C-27), receipt-completeness / ordering pair
(C-33 + C-35), ordering as phase-gate failure (C-36), self-contained per-field C2 RESULT
block (C-37 + C-39), F-01 IA-RESPONSE column-header schema (C-34 + C-38 + C-40),
three-level structural enforcement partition with path-negation declaration (C-41 + C-46),
and CLOSED PATHS enumeration in pipeline declaration (C-43 + C-45).
Read the full pipeline declaration before producing any output.

---

**PIPELINE DECLARATION**

```
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
            partition + negation, C-43/C-45 CLOSED PATHS enumeration)
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
          slot compliance is O(1) column-count check; no inline-cell alternative path [C-46].
    Auditable by counting table columns alone.
  Each level is independently auditable without reading adjacent levels.
  No two criterion families share a level.

Closed paths [C-43]:
  C-40 (table-column level) supersedes C-38 (block level) for F-01 Description schema.
  The inline-cell-label "or" path ("[IA-VERDICT: X] | [ROLE-MECHANISM: Y]" in a single
  Description cell) satisfies C-38 but is C-40 noncompliant -- do not use it.
  Only the column-header form (separate named [IA-VERDICT] and [ROLE-MECHANISM] columns)
  satisfies the table-column level requirement. A reviewer auditing this section can verify
  the closed path by name without reading format rules [C-45].
```

---

**PHASE A -- ROUTE**

```
## Phase A: Routing

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern] |
| (all files) | default | Inertia Advocate | default -- always included |
```

Coverage gap: `COVERAGE GAP: [file] -- no org.yaml scope pattern covers this path.`

---

**PHASE B -- INERTIA REVIEW**

Entry: Phase A exit met.

The Budget verdict appears as exactly three separate labeled lines below the separator.
Each line begins with its clause label. No clause is embedded in a table cell, in the
Conclusion of another clause, or merged with another clause on the same line.

```
## Phase B: Inertia Advocate

Null hypothesis: The codebase currently [does X via mechanism Y].           <- B1

Cost ledger:                                                                 <- B2

| Cost Category     | Current-State Cost                                        | Adoption Cost (this PR)                          | Net                      |
|-------------------|-----------------------------------------------------------|--------------------------------------------------|--------------------------|
| Maintenance       | [LOW/MED/HIGH -- maintaining current path]                | [maintaining new path post-merge]                | WORSE / BETTER / NEUTRAL |
| Incident exposure | [failure risk/severity under status quo]                  | [residual exposure after merge]                  | WORSE / BETTER / NEUTRAL |
| Integration cost  | [coordination overhead of current approach]               | [churn, downstream wiring, test burden]          | WORSE / BETTER / NEUTRAL |
| Regression risk   | [risk of new failures from current approach as-is]        | [risk introduced by this PR]                     | WORSE / BETTER / NEUTRAL |

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
```

Phase B exit: B1-B5 met; three Budget verdict lines present as separate output lines.

---

**PHASE C -- TECHNICAL REVIEWS**

**C1 -- Phase B Exit Pre-Flight [C-26/C1, scope: Phase B completeness]:**

```
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
```

If any box unchecked: `C1 RESULT: BLOCKED -- [B-number]`

C1 scope is Phase B. C1 RESULT does not confirm any role's READ RECEIPT content.

**Per-Role Output Sequence (C-35/C-36: STEP 1 must precede STEP 2 in the output;
STEP 2 before STEP 1 is a Phase C exit-condition failure -- Phase D blocked):**

Sequence across roles: PM/TPM -> domain-specific -> security/compliance.

**STEP 1 -- READ RECEIPT [must appear in output before STEP 2]:**

Output the READ RECEIPT block now, before writing any C2 RESULT block for this role.

```
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
```

**STEP 2 -- C2 RESULT BLOCK [C-33, C-37, C-39, C-26/C2] [must follow STEP 1 -- C-35/C-36]:**

The C2 RESULT block enumerates all five receipt fields (a)-(e) by label with an explicit
PRESENT or ABSENT verdict per field. The terminal C2 RESULT line derives from the per-field
verdicts above it and appears within this same block. C2 scope is receipt completeness -- not
Phase B. The UNSATISFIED path is handled within this block -- not in a separate adjacent fence.
A reviewer verifies both the per-field evidence and the terminal verdict by reading this
single block. No cross-block reading required [C-39].

```
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
```

C-36 compliance: If "C2 RESULT:" terminal line appears before "## IA READ RECEIPT" header
for this role in the output, this is a Phase C exit-condition failure -- Phase D blocked.

C-37 / C-39 compliance: (a)-(e) each on its own labeled line with PRESENT/ABSENT; terminal
C2 RESULT line is in this same block, derived from the per-field rows above -- no separate
fence, no adjacent prose carrying the verdict.

C-33 scope check: every labeled line in this block targets a receipt field, not Phase B.

**STEP 3 -- PRE-COMMITMENT [C-27, before reading diff]:**

```
PRE-COMMITMENT: [Role Name]

Cost row assessed:  [Maintenance / Incident exposure / Integration cost / Regression risk]
Initial position:   [CONFIRMS / DISPUTES] [Net direction] on [Cost row]
                    [one phrase based on domain knowledge + Phase B ledger]
Basis:              Domain knowledge only. PR diff not yet examined.
                    [one sentence naming the code surface or architectural pattern]

[PRE-COMMITMENT SEALED]
```

**STEP 4 -- FINDINGS [C-34, C-38, C-40, C-43]:**

Apply domain-lens gate per finding:

```
Step A: "Would only [this role] raise this finding, given their domain?"
  YES -> include. NO -> Step B.
Step B: Revise to name domain-owned mechanism. Still NO -> drop.
```

The findings table MUST include a Type column. F-01 MUST have Type = IA-RESPONSE.
[IA-VERDICT] and [ROLE-MECHANISM] MUST be column headers -- no inline-cell path.
See pipeline declaration CLOSED PATHS [C-43] for the prohibited inline-cell-label path.

```
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
```

F-01 IA-RESPONSE format rules [C-34, C-38, C-40, C-43]:
- Type cell: exactly "IA-RESPONSE" -- no other value passes
- Column structure: [IA-VERDICT] and [ROLE-MECHANISM] are column headers in the findings
  table. Slot compliance is O(1) column-count: a reviewer verifies presence by counting
  columns, not parsing cell content.
- See pipeline declaration CLOSED PATHS [C-43] for the prohibited inline-cell-label path.
- F-01 cells: [IA-VERDICT] cell contains the IA's verdict or cost position from Phase B;
  [ROLE-MECHANISM] cell contains the specific code artifact or mechanism in this role's domain.
- DOMAIN findings (F-02 onward): [IA-VERDICT] and [ROLE-MECHANISM] columns show "--"

Phase C exit: C1 ALL CLEAR (Phase B scope); every C2 RESULT block enumerates (a)-(e)
PRESENT/ABSENT and derives terminal verdict in same block [C-33, C-37, C-39]; READ RECEIPT
precedes C2 RESULT per role -- ordering violation is Phase C exit-condition failure
[C-35/C-36]; PRE-COMMITMENT before findings [C-27]; F-01 Type=IA-RESPONSE with [IA-VERDICT]
and [ROLE-MECHANISM] as column headers [C-34/C-38/C-40]; three-level enforcement partition
with inline negation in C-40 entry [C-41, C-46]; CLOSED PATHS enumeration in pipeline
declaration [C-43, C-45]; all findings passed domain-lens gate.

---

**PHASE D -- SYNTHESIS**

Entry: Phase C exit met (C-36 ordering, C-37/C-39 self-contained block, C-38/C-40
column-header schema, C-41/C-46 three-level partition + negation, C-43/C-45 CLOSED PATHS).

```
## Phase D: Consensus

IA cost ledger: Budget strength was [HIGH / MEDIUM / LOW].
  WORSE rows were: [restate]. BETTER rows were: [restate].
  Technical roles collectively [reinforced / challenged / defeated] the IA's estimate.
  Net: [one sentence]

Agreement: [area] -- [role-A] and [role-B] independently raised [concern]

Divergence: [role-A] rates [area] P[N]; [role-B] rates P[N].
  Mechanism: [architectural property of the code -- not perspective difference]

Critical: [F-XX from role] -- [why this most threatens the merge]
```

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

```
## Phase E: Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from role] -- [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] -- sign-off: [role who confirms before merge]
```

One decision. Values: GO, NO-GO, GO WITH CONDITIONS only.
Delegated decisions fail. Hedged decisions fail.

---

**AMEND**

When invoked with an AMEND directive, output this named-field block before Phase A.

```
## AMEND SCOPE

What was amended:           [description]
Roles added:                [list, or "none"]
Roles removed:              [list, or "none"]
Files triggering addition:  [list, or "n/a -- manually directed"]
Prior findings superseded:  [F-IDs, or "none -- first run"]
```

Run Phases A-E with the amended scope.

---

## V-02 — Output Format: Double C-43 Coverage

**Axis**: Output format (C-43 prohibition placement -- CLOSED PATHS declaration + format-rules restatement)
**Hypothesis**: R15 V-03 satisfies C-43 via the CLOSED PATHS block in the pipeline declaration alone; the format rules section only cross-references it. C-45 requires the prohibition to live in the declaration so path closures are auditable at declaration level without reading format rules. V-02 tests whether adding a full four-element C-43 restatement in the format rules section (in addition to the CLOSED PATHS block) introduces any conflict or ambiguity for the rubric scorer. Both paths carry the same four elements; C-43 and C-45 should pass. The negation statement in the structural enforcement C-40 entry closes C-46; the absence of the alternative form from the format rules template closes C-44. This is the most redundant form -- every C-43/44/45/46 check can be satisfied by reading any one of three places (declaration, structural enforcement, or format rules).

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline. Ten structural
compliance mechanisms are active: string-matchable Budget verdict (C-25), named result
tokens (C-26), PRE-COMMITMENT blocks (C-27), receipt-completeness / ordering pair
(C-33 + C-35), ordering as phase-gate failure (C-36), self-contained per-field C2 RESULT
block (C-37 + C-39), F-01 IA-RESPONSE column-header schema (C-34 + C-38 + C-40),
three-level structural enforcement partition with path-negation declaration (C-41 + C-46),
and CLOSED PATHS enumeration in pipeline declaration (C-43 + C-45).
Read the full pipeline declaration before producing any output.

---

**PIPELINE DECLARATION**

```
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
            partition + negation, C-43/C-45 CLOSED PATHS enumeration)
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
          slot compliance is O(1) column-count check; no inline-cell alternative path [C-46].
    Auditable by counting table columns alone.
  Each level is independently auditable without reading adjacent levels.
  No two criterion families share a level.

Closed paths [C-43]:
  C-40 (table-column level) supersedes C-38 (block level) for F-01 Description schema.
  The inline-cell-label "or" path ("[IA-VERDICT: X] | [ROLE-MECHANISM: Y]" in a single
  Description cell) satisfies C-38 but is C-40 noncompliant -- do not use it.
  Only the column-header form (separate named [IA-VERDICT] and [ROLE-MECHANISM] columns)
  satisfies the table-column level requirement. A reviewer auditing this section can verify
  the closed path by name without reading format rules [C-45].
```

---

**PHASE A -- ROUTE**

```
## Phase A: Routing

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern] |
| (all files) | default | Inertia Advocate | default -- always included |
```

Coverage gap: `COVERAGE GAP: [file] -- no org.yaml scope pattern covers this path.`

---

**PHASE B -- INERTIA REVIEW**

Entry: Phase A exit met.

The Budget verdict appears as exactly three separate labeled lines below the separator.
Each line begins with its clause label. No clause is embedded in a table cell, in the
Conclusion of another clause, or merged with another clause on the same line.

```
## Phase B: Inertia Advocate

Null hypothesis: The codebase currently [does X via mechanism Y].           <- B1

Cost ledger:                                                                 <- B2

| Cost Category     | Current-State Cost                                        | Adoption Cost (this PR)                          | Net                      |
|-------------------|-----------------------------------------------------------|--------------------------------------------------|--------------------------|
| Maintenance       | [LOW/MED/HIGH -- maintaining current path]                | [maintaining new path post-merge]                | WORSE / BETTER / NEUTRAL |
| Incident exposure | [failure risk/severity under status quo]                  | [residual exposure after merge]                  | WORSE / BETTER / NEUTRAL |
| Integration cost  | [coordination overhead of current approach]               | [churn, downstream wiring, test burden]          | WORSE / BETTER / NEUTRAL |
| Regression risk   | [risk of new failures from current approach as-is]        | [risk introduced by this PR]                     | WORSE / BETTER / NEUTRAL |

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
```

Phase B exit: B1-B5 met; three Budget verdict lines present as separate output lines.

---

**PHASE C -- TECHNICAL REVIEWS**

**C1 -- Phase B Exit Pre-Flight [C-26/C1, scope: Phase B completeness]:**

```
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
```

If any box unchecked: `C1 RESULT: BLOCKED -- [B-number]`

C1 scope is Phase B. C1 RESULT does not confirm any role's READ RECEIPT content.

**Per-Role Output Sequence (C-35/C-36: STEP 1 must precede STEP 2 in the output;
STEP 2 before STEP 1 is a Phase C exit-condition failure -- Phase D blocked):**

Sequence across roles: security/compliance -> domain-specific -> PM/TPM.

**STEP 1 -- READ RECEIPT [must appear in output before STEP 2]:**

Output the READ RECEIPT block now, before writing any C2 RESULT block for this role.

```
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
```

**STEP 2 -- C2 RESULT BLOCK [C-33, C-37, C-39, C-26/C2] [must follow STEP 1 -- C-35/C-36]:**

The C2 RESULT block enumerates all five receipt fields (a)-(e) by label with an explicit
PRESENT or ABSENT verdict per field. The terminal C2 RESULT line derives from the per-field
verdicts above it and appears within this same block. C2 scope is receipt completeness -- not
Phase B. The UNSATISFIED path is handled within this block -- not in a separate adjacent fence.
A reviewer verifies both the per-field evidence and the terminal verdict by reading this
single block. No cross-block reading required [C-39].

```
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
```

C-36 compliance: If "C2 RESULT:" terminal line appears before "## IA READ RECEIPT" header
for this role in the output, this is a Phase C exit-condition failure -- Phase D blocked.

C-37 / C-39 compliance: (a)-(e) each on its own labeled line with PRESENT/ABSENT; terminal
C2 RESULT line is in this same block, derived from the per-field rows above -- no separate
fence, no adjacent prose carrying the verdict.

C-33 scope check: every labeled line in this block targets a receipt field, not Phase B.

**STEP 3 -- PRE-COMMITMENT [C-27, before reading diff]:**

```
PRE-COMMITMENT: [Role Name]

Cost row assessed:  [Maintenance / Incident exposure / Integration cost / Regression risk]
Initial position:   [CONFIRMS / DISPUTES] [Net direction] on [Cost row]
                    [one phrase based on domain knowledge + Phase B ledger]
Basis:              Domain knowledge only. PR diff not yet examined.
                    [one sentence naming the code surface or architectural pattern]

[PRE-COMMITMENT SEALED]
```

**STEP 4 -- FINDINGS [C-34, C-38, C-40, C-43]:**

Apply domain-lens gate per finding:

```
Step A: "Would only [this role] raise this finding, given their domain?"
  YES -> include. NO -> Step B.
Step B: Revise to name domain-owned mechanism. Still NO -> drop.
```

The findings table MUST include a Type column. F-01 MUST have Type = IA-RESPONSE.
[IA-VERDICT] and [ROLE-MECHANISM] MUST be column headers -- no inline-cell path.

```
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
```

F-01 IA-RESPONSE format rules [C-34, C-38, C-40, C-43]:
- Type cell: exactly "IA-RESPONSE" -- no other value passes
- Column structure: [IA-VERDICT] and [ROLE-MECHANISM] are column headers in the findings
  table. Slot compliance is O(1) column-count: a reviewer verifies presence by counting
  columns, not parsing cell content.
- Prohibition [C-43]: the inline-cell-label path ("[IA-VERDICT: X] | [ROLE-MECHANISM: Y]"
  in a single Description cell) satisfies C-38 but is C-40 noncompliant -- do not use it.
  (Also declared at declaration level in pipeline CLOSED PATHS above [C-45].)
- F-01 cells: [IA-VERDICT] cell contains the IA's verdict or cost position from Phase B;
  [ROLE-MECHANISM] cell contains the specific code artifact or mechanism in this role's domain.
- DOMAIN findings (F-02 onward): [IA-VERDICT] and [ROLE-MECHANISM] columns show "--"

Phase C exit: C1 ALL CLEAR (Phase B scope); every C2 RESULT block enumerates (a)-(e)
PRESENT/ABSENT and derives terminal verdict in same block [C-33, C-37, C-39]; READ RECEIPT
precedes C2 RESULT per role -- ordering violation is Phase C exit-condition failure
[C-35/C-36]; PRE-COMMITMENT before findings [C-27]; F-01 Type=IA-RESPONSE with [IA-VERDICT]
and [ROLE-MECHANISM] as column headers [C-34/C-38/C-40]; structural enforcement partition
with inline negation in C-40 entry [C-41, C-46]; CLOSED PATHS in declaration + prohibition
in format rules [C-43, C-45]; all findings passed domain-lens gate.

---

**PHASE D -- SYNTHESIS**

Entry: Phase C exit met (C-36 ordering, C-37/C-39 self-contained block, C-38/C-40
column-header schema, C-41/C-46 three-level partition + negation, C-43/C-45 CLOSED PATHS
in declaration + format rules).

```
## Phase D: Consensus

IA cost ledger: Budget strength was [HIGH / MEDIUM / LOW].
  WORSE rows were: [restate]. BETTER rows were: [restate].
  Technical roles collectively [reinforced / challenged / defeated] the IA's estimate.
  Net: [one sentence]

Agreement: [area] -- [role-A] and [role-B] independently raised [concern]

Divergence: [role-A] rates [area] P[N]; [role-B] rates P[N].
  Mechanism: [architectural property of the code -- not perspective difference]

Critical: [F-XX from role] -- [why this most threatens the merge]
```

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

```
## Phase E: Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from role] -- [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] -- sign-off: [role who confirms before merge]
```

One decision. Values: GO, NO-GO, GO WITH CONDITIONS only.
Delegated decisions fail. Hedged decisions fail.

---

**AMEND**

When invoked with an AMEND directive, output this named-field block before Phase A.

```
## AMEND SCOPE

What was amended:           [description]
Roles added:                [list, or "none"]
Roles removed:              [list, or "none"]
Files triggering addition:  [list, or "n/a -- manually directed"]
Prior findings superseded:  [F-IDs, or "none -- first run"]
```

Run Phases A-E with the amended scope.

---

## V-03 — Phrasing Register: Named Sub-Entry Negation

**Axis**: Phrasing register (structural form of C-46 negation in structural enforcement section)
**Hypothesis**: R15 V-02 satisfied C-46 with an inline clause appended to the C-40 entry ("; no inline-cell alternative path"). This is readable but requires parsing the C-40 description to locate the negation. V-03 tests elevating the negation to a named standalone sub-entry with its own label ("Eliminated [C-46]:") as a distinct line under the table-column level section. The named sub-entry form makes the negation independently scannable by label-matching -- the same O(1) property that column headers provide for C-40. All four criteria use the same core content as V-01 but express C-46's negation as a named element rather than an inline clause. The question is whether the named sub-entry form passes C-46 more robustly or if the inline clause is equally auditable per the rubric.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline. Ten structural
compliance mechanisms are active: string-matchable Budget verdict (C-25), named result
tokens (C-26), PRE-COMMITMENT blocks (C-27), receipt-completeness / ordering pair
(C-33 + C-35), ordering as phase-gate failure (C-36), self-contained per-field C2 RESULT
block (C-37 + C-39), F-01 IA-RESPONSE column-header schema (C-34 + C-38 + C-40),
three-level structural enforcement partition with named path-negation sub-entry (C-41 + C-46),
and CLOSED PATHS enumeration in pipeline declaration (C-43 + C-45).
Read the full pipeline declaration before producing any output.

---

**PIPELINE DECLARATION**

```
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
            partition + named negation sub-entry, C-43/C-45 CLOSED PATHS enumeration)
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
    Auditable by counting table columns alone; negation auditable by label-scan.
  Each level is independently auditable without reading adjacent levels.
  No two criterion families share a level.

Closed paths [C-43]:
  C-40 (table-column level) supersedes C-38 (block level) for F-01 Description schema.
  The inline-cell-label "or" path ("[IA-VERDICT: X] | [ROLE-MECHANISM: Y]" in a single
  Description cell) satisfies C-38 but is C-40 noncompliant -- do not use it.
  Only the column-header form (separate named [IA-VERDICT] and [ROLE-MECHANISM] columns)
  satisfies the table-column level requirement. A reviewer auditing this section can verify
  the closed path by name without reading format rules [C-45].
```

---

**PHASE A -- ROUTE**

```
## Phase A: Routing

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern] |
| (all files) | default | Inertia Advocate | default -- always included |
```

Coverage gap: `COVERAGE GAP: [file] -- no org.yaml scope pattern covers this path.`

---

**PHASE B -- INERTIA REVIEW**

Entry: Phase A exit met.

The Budget verdict appears as exactly three separate labeled lines below the separator.
Each line begins with its clause label. No clause is embedded in a table cell, in the
Conclusion of another clause, or merged with another clause on the same line.

```
## Phase B: Inertia Advocate

Null hypothesis: The codebase currently [does X via mechanism Y].           <- B1

Cost ledger:                                                                 <- B2

| Cost Category     | Current-State Cost                                        | Adoption Cost (this PR)                          | Net                      |
|-------------------|-----------------------------------------------------------|--------------------------------------------------|--------------------------|
| Maintenance       | [LOW/MED/HIGH -- maintaining current path]                | [maintaining new path post-merge]                | WORSE / BETTER / NEUTRAL |
| Incident exposure | [failure risk/severity under status quo]                  | [residual exposure after merge]                  | WORSE / BETTER / NEUTRAL |
| Integration cost  | [coordination overhead of current approach]               | [churn, downstream wiring, test burden]          | WORSE / BETTER / NEUTRAL |
| Regression risk   | [risk of new failures from current approach as-is]        | [risk introduced by this PR]                     | WORSE / BETTER / NEUTRAL |

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
```

Phase B exit: B1-B5 met; three Budget verdict lines present as separate output lines.

---

**PHASE C -- TECHNICAL REVIEWS**

**C1 -- Phase B Exit Pre-Flight [C-26/C1, scope: Phase B completeness]:**

```
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
```

If any box unchecked: `C1 RESULT: BLOCKED -- [B-number]`

C1 scope is Phase B. C1 RESULT does not confirm any role's READ RECEIPT content.

**Per-Role Output Sequence (C-35/C-36: STEP 1 must precede STEP 2 in the output;
STEP 2 before STEP 1 is a Phase C exit-condition failure -- Phase D blocked):**

Sequence across roles: security/compliance -> domain-specific -> PM/TPM.

**STEP 1 -- READ RECEIPT [must appear in output before STEP 2]:**

Output the READ RECEIPT block now, before writing any C2 RESULT block for this role.

```
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
```

**STEP 2 -- C2 RESULT BLOCK [C-33, C-37, C-39, C-26/C2] [must follow STEP 1 -- C-35/C-36]:**

The C2 RESULT block enumerates all five receipt fields (a)-(e) by label with an explicit
PRESENT or ABSENT verdict per field. The terminal C2 RESULT line derives from the per-field
verdicts above it and appears within this same block. C2 scope is receipt completeness -- not
Phase B. The UNSATISFIED path is handled within this block -- not in a separate adjacent fence.
A reviewer verifies both the per-field evidence and the terminal verdict by reading this
single block. No cross-block reading required [C-39].

```
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
```

C-36 compliance: If "C2 RESULT:" terminal line appears before "## IA READ RECEIPT" header
for this role in the output, this is a Phase C exit-condition failure -- Phase D blocked.

C-37 / C-39 compliance: (a)-(e) each on its own labeled line with PRESENT/ABSENT; terminal
C2 RESULT line is in this same block, derived from the per-field rows above -- no separate
fence, no adjacent prose carrying the verdict.

C-33 scope check: every labeled line in this block targets a receipt field, not Phase B.

**STEP 3 -- PRE-COMMITMENT [C-27, before reading diff]:**

```
PRE-COMMITMENT: [Role Name]

Cost row assessed:  [Maintenance / Incident exposure / Integration cost / Regression risk]
Initial position:   [CONFIRMS / DISPUTES] [Net direction] on [Cost row]
                    [one phrase based on domain knowledge + Phase B ledger]
Basis:              Domain knowledge only. PR diff not yet examined.
                    [one sentence naming the code surface or architectural pattern]

[PRE-COMMITMENT SEALED]
```

**STEP 4 -- FINDINGS [C-34, C-38, C-40, C-43]:**

Apply domain-lens gate per finding:

```
Step A: "Would only [this role] raise this finding, given their domain?"
  YES -> include. NO -> Step B.
Step B: Revise to name domain-owned mechanism. Still NO -> drop.
```

The findings table MUST include a Type column. F-01 MUST have Type = IA-RESPONSE.
[IA-VERDICT] and [ROLE-MECHANISM] MUST be column headers.
See pipeline declaration Structural enforcement levels "Eliminated [C-46]:" entry and
CLOSED PATHS [C-43] for the prohibited inline-cell-label path.

```
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
```

F-01 IA-RESPONSE format rules [C-34, C-38, C-40, C-43]:
- Type cell: exactly "IA-RESPONSE" -- no other value passes
- Column structure: [IA-VERDICT] and [ROLE-MECHANISM] are column headers in the findings
  table. Slot compliance is O(1) column-count: a reviewer verifies presence by counting
  columns, not parsing cell content.
- See pipeline declaration CLOSED PATHS [C-43] for the prohibited inline-cell-label path.
  See structural enforcement "Eliminated [C-46]:" sub-entry for the path-negation declaration.
- F-01 cells: [IA-VERDICT] cell contains the IA's verdict or cost position from Phase B;
  [ROLE-MECHANISM] cell contains the specific code artifact or mechanism in this role's domain.
- DOMAIN findings (F-02 onward): [IA-VERDICT] and [ROLE-MECHANISM] columns show "--"

Phase C exit: C1 ALL CLEAR (Phase B scope); every C2 RESULT block enumerates (a)-(e)
PRESENT/ABSENT and derives terminal verdict in same block [C-33, C-37, C-39]; READ RECEIPT
precedes C2 RESULT per role -- ordering violation is Phase C exit-condition failure
[C-35/C-36]; PRE-COMMITMENT before findings [C-27]; F-01 Type=IA-RESPONSE with [IA-VERDICT]
and [ROLE-MECHANISM] as column headers [C-34/C-38/C-40]; three-level enforcement partition
with named negation sub-entry "Eliminated [C-46]:" [C-41, C-46]; CLOSED PATHS enumeration
in pipeline declaration [C-43, C-45]; all findings passed domain-lens gate.

---

**PHASE D -- SYNTHESIS**

Entry: Phase C exit met (C-36 ordering, C-37/C-39 self-contained block, C-38/C-40
column-header schema, C-41/C-46 three-level partition + named negation sub-entry,
C-43/C-45 CLOSED PATHS in declaration).

```
## Phase D: Consensus

IA cost ledger: Budget strength was [HIGH / MEDIUM / LOW].
  WORSE rows were: [restate]. BETTER rows were: [restate].
  Technical roles collectively [reinforced / challenged / defeated] the IA's estimate.
  Net: [one sentence]

Agreement: [area] -- [role-A] and [role-B] independently raised [concern]

Divergence: [role-A] rates [area] P[N]; [role-B] rates P[N].
  Mechanism: [architectural property of the code -- not perspective difference]

Critical: [F-XX from role] -- [why this most threatens the merge]
```

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

```
## Phase E: Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from role] -- [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] -- sign-off: [role who confirms before merge]
```

One decision. Values: GO, NO-GO, GO WITH CONDITIONS only.
Delegated decisions fail. Hedged decisions fail.

---

**AMEND**

When invoked with an AMEND directive, output this named-field block before Phase A.

```
## AMEND SCOPE

What was amended:           [description]
Roles added:                [list, or "none"]
Roles removed:              [list, or "none"]
Files triggering addition:  [list, or "n/a -- manually directed"]
Prior findings superseded:  [F-IDs, or "none -- first run"]
```

Run Phases A-E with the amended scope.

---

## V-04 — Combination: Role Sequence + Named Sub-Entry Negation

**Axes**: Role sequence (PM/TPM first) + Phrasing register (named sub-entry negation)
**Hypothesis**: Combines V-01's PM/TPM-first sequence with V-03's named "Eliminated [C-46]:" sub-entry negation. Tests whether the named sub-entry form interacts with the sequence permutation: if a PM/TPM reviewer is first and its READ RECEIPT/PRE-COMMITMENT sequence is correct, the named negation sub-entry (which is read at pipeline-declaration time before any role executes) should remain fully effective. Expected: all four pass, confirming that both axes are structurally independent.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline. Ten structural
compliance mechanisms are active: string-matchable Budget verdict (C-25), named result
tokens (C-26), PRE-COMMITMENT blocks (C-27), receipt-completeness / ordering pair
(C-33 + C-35), ordering as phase-gate failure (C-36), self-contained per-field C2 RESULT
block (C-37 + C-39), F-01 IA-RESPONSE column-header schema (C-34 + C-38 + C-40),
three-level structural enforcement partition with named path-negation sub-entry (C-41 + C-46),
and CLOSED PATHS enumeration in pipeline declaration (C-43 + C-45).
Read the full pipeline declaration before producing any output.

---

**PIPELINE DECLARATION**

```
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
            partition + named negation sub-entry, C-43/C-45 CLOSED PATHS enumeration)
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
    Auditable by counting table columns alone; negation auditable by label-scan.
  Each level is independently auditable without reading adjacent levels.
  No two criterion families share a level.

Closed paths [C-43]:
  C-40 (table-column level) supersedes C-38 (block level) for F-01 Description schema.
  The inline-cell-label "or" path ("[IA-VERDICT: X] | [ROLE-MECHANISM: Y]" in a single
  Description cell) satisfies C-38 but is C-40 noncompliant -- do not use it.
  Only the column-header form (separate named [IA-VERDICT] and [ROLE-MECHANISM] columns)
  satisfies the table-column level requirement. A reviewer auditing this section can verify
  the closed path by name without reading format rules [C-45].
```

---

**PHASE A -- ROUTE**

```
## Phase A: Routing

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern] |
| (all files) | default | Inertia Advocate | default -- always included |
```

Coverage gap: `COVERAGE GAP: [file] -- no org.yaml scope pattern covers this path.`

---

**PHASE B -- INERTIA REVIEW**

Entry: Phase A exit met.

The Budget verdict appears as exactly three separate labeled lines below the separator.
Each line begins with its clause label. No clause is embedded in a table cell, in the
Conclusion of another clause, or merged with another clause on the same line.

```
## Phase B: Inertia Advocate

Null hypothesis: The codebase currently [does X via mechanism Y].           <- B1

Cost ledger:                                                                 <- B2

| Cost Category     | Current-State Cost                                        | Adoption Cost (this PR)                          | Net                      |
|-------------------|-----------------------------------------------------------|--------------------------------------------------|--------------------------|
| Maintenance       | [LOW/MED/HIGH -- maintaining current path]                | [maintaining new path post-merge]                | WORSE / BETTER / NEUTRAL |
| Incident exposure | [failure risk/severity under status quo]                  | [residual exposure after merge]                  | WORSE / BETTER / NEUTRAL |
| Integration cost  | [coordination overhead of current approach]               | [churn, downstream wiring, test burden]          | WORSE / BETTER / NEUTRAL |
| Regression risk   | [risk of new failures from current approach as-is]        | [risk introduced by this PR]                     | WORSE / BETTER / NEUTRAL |

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
```

Phase B exit: B1-B5 met; three Budget verdict lines present as separate output lines.

---

**PHASE C -- TECHNICAL REVIEWS**

**C1 -- Phase B Exit Pre-Flight [C-26/C1, scope: Phase B completeness]:**

```
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
```

If any box unchecked: `C1 RESULT: BLOCKED -- [B-number]`

C1 scope is Phase B. C1 RESULT does not confirm any role's READ RECEIPT content.

**Per-Role Output Sequence (C-35/C-36: STEP 1 must precede STEP 2 in the output;
STEP 2 before STEP 1 is a Phase C exit-condition failure -- Phase D blocked):**

Sequence across roles: PM/TPM -> domain-specific -> security/compliance.

**STEP 1 -- READ RECEIPT [must appear in output before STEP 2]:**

Output the READ RECEIPT block now, before writing any C2 RESULT block for this role.

```
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
```

**STEP 2 -- C2 RESULT BLOCK [C-33, C-37, C-39, C-26/C2] [must follow STEP 1 -- C-35/C-36]:**

The C2 RESULT block enumerates all five receipt fields (a)-(e) by label with an explicit
PRESENT or ABSENT verdict per field. The terminal C2 RESULT line derives from the per-field
verdicts above it and appears within this same block. C2 scope is receipt completeness -- not
Phase B. The UNSATISFIED path is handled within this block -- not in a separate adjacent fence.
A reviewer verifies both the per-field evidence and the terminal verdict by reading this
single block. No cross-block reading required [C-39].

```
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
```

C-36 compliance: If "C2 RESULT:" terminal line appears before "## IA READ RECEIPT" header
for this role in the output, this is a Phase C exit-condition failure -- Phase D blocked.

C-37 / C-39 compliance: (a)-(e) each on its own labeled line with PRESENT/ABSENT; terminal
C2 RESULT line is in this same block, derived from the per-field rows above -- no separate
fence, no adjacent prose carrying the verdict.

C-33 scope check: every labeled line in this block targets a receipt field, not Phase B.

**STEP 3 -- PRE-COMMITMENT [C-27, before reading diff]:**

```
PRE-COMMITMENT: [Role Name]

Cost row assessed:  [Maintenance / Incident exposure / Integration cost / Regression risk]
Initial position:   [CONFIRMS / DISPUTES] [Net direction] on [Cost row]
                    [one phrase based on domain knowledge + Phase B ledger]
Basis:              Domain knowledge only. PR diff not yet examined.
                    [one sentence naming the code surface or architectural pattern]

[PRE-COMMITMENT SEALED]
```

**STEP 4 -- FINDINGS [C-34, C-38, C-40, C-43]:**

Apply domain-lens gate per finding:

```
Step A: "Would only [this role] raise this finding, given their domain?"
  YES -> include. NO -> Step B.
Step B: Revise to name domain-owned mechanism. Still NO -> drop.
```

The findings table MUST include a Type column. F-01 MUST have Type = IA-RESPONSE.
[IA-VERDICT] and [ROLE-MECHANISM] MUST be column headers.
See pipeline declaration Structural enforcement levels "Eliminated [C-46]:" entry and
CLOSED PATHS [C-43] for the prohibited inline-cell-label path.

```
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
```

F-01 IA-RESPONSE format rules [C-34, C-38, C-40, C-43]:
- Type cell: exactly "IA-RESPONSE" -- no other value passes
- Column structure: [IA-VERDICT] and [ROLE-MECHANISM] are column headers in the findings
  table. Slot compliance is O(1) column-count: a reviewer verifies presence by counting
  columns, not parsing cell content.
- See pipeline declaration CLOSED PATHS [C-43] for the prohibited inline-cell-label path.
  See structural enforcement "Eliminated [C-46]:" sub-entry for the path-negation declaration.
- F-01 cells: [IA-VERDICT] cell contains the IA's verdict or cost position from Phase B;
  [ROLE-MECHANISM] cell contains the specific code artifact or mechanism in this role's domain.
- DOMAIN findings (F-02 onward): [IA-VERDICT] and [ROLE-MECHANISM] columns show "--"

Phase C exit: C1 ALL CLEAR (Phase B scope); every C2 RESULT block enumerates (a)-(e)
PRESENT/ABSENT and derives terminal verdict in same block [C-33, C-37, C-39]; READ RECEIPT
precedes C2 RESULT per role -- ordering violation is Phase C exit-condition failure
[C-35/C-36]; PRE-COMMITMENT before findings [C-27]; F-01 Type=IA-RESPONSE with [IA-VERDICT]
and [ROLE-MECHANISM] as column headers [C-34/C-38/C-40]; three-level enforcement partition
with named negation sub-entry "Eliminated [C-46]:" [C-41, C-46]; CLOSED PATHS enumeration
in pipeline declaration [C-43, C-45]; all findings passed domain-lens gate.

---

**PHASE D -- SYNTHESIS**

Entry: Phase C exit met (C-36 ordering, C-37/C-39 self-contained block, C-38/C-40
column-header schema, C-41/C-46 three-level partition + named negation sub-entry,
C-43/C-45 CLOSED PATHS in declaration).

```
## Phase D: Consensus

IA cost ledger: Budget strength was [HIGH / MEDIUM / LOW].
  WORSE rows were: [restate]. BETTER rows were: [restate].
  Technical roles collectively [reinforced / challenged / defeated] the IA's estimate.
  Net: [one sentence]

Agreement: [area] -- [role-A] and [role-B] independently raised [concern]

Divergence: [role-A] rates [area] P[N]; [role-B] rates P[N].
  Mechanism: [architectural property of the code -- not perspective difference]

Critical: [F-XX from role] -- [why this most threatens the merge]
```

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

```
## Phase E: Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from role] -- [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] -- sign-off: [role who confirms before merge]
```

One decision. Values: GO, NO-GO, GO WITH CONDITIONS only.
Delegated decisions fail. Hedged decisions fail.

---

**AMEND**

When invoked with an AMEND directive, output this named-field block before Phase A.

```
## AMEND SCOPE

What was amended:           [description]
Roles added:                [list, or "none"]
Roles removed:              [list, or "none"]
Files triggering addition:  [list, or "n/a -- manually directed"]
Prior findings superseded:  [F-IDs, or "none -- first run"]
```

Run Phases A-E with the amended scope.

---

## V-05 — Combination: Double Coverage + Named Sub-Entry Negation

**Axes**: Output format (double C-43 coverage) + Phrasing register (named sub-entry negation)
**Hypothesis**: The most redundant form: C-43 prohibition appears in both the CLOSED PATHS declaration (C-45) and the format rules section (four-element restatement). The C-46 negation appears as a named "Eliminated [C-46]:" sub-entry (not inline clause). This is the highest-coverage form -- every compliance check is satisfiable from multiple independent locations. The combination tests whether the double coverage of C-43 and the named sub-entry form of C-46 create any conflicts or whether they compound the robustness. An additional format-rules cross-reference to the "Eliminated [C-46]:" sub-entry connects the format rules coverage of C-43 directly to the structural enforcement declaration of C-46, making the C-44/C-46 audit trail complete from either the format rules or the structural enforcement section alone.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline. Ten structural
compliance mechanisms are active: string-matchable Budget verdict (C-25), named result
tokens (C-26), PRE-COMMITMENT blocks (C-27), receipt-completeness / ordering pair
(C-33 + C-35), ordering as phase-gate failure (C-36), self-contained per-field C2 RESULT
block (C-37 + C-39), F-01 IA-RESPONSE column-header schema (C-34 + C-38 + C-40),
three-level structural enforcement partition with named path-negation sub-entry (C-41 + C-46),
and CLOSED PATHS enumeration in pipeline declaration with format-rules restatement (C-43 + C-45).
Read the full pipeline declaration before producing any output.

---

**PIPELINE DECLARATION**

```
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
            restatement)
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
    Auditable by counting table columns alone; negation auditable by label-scan.
  Each level is independently auditable without reading adjacent levels.
  No two criterion families share a level.

Closed paths [C-43]:
  C-40 (table-column level) supersedes C-38 (block level) for F-01 Description schema.
  The inline-cell-label "or" path ("[IA-VERDICT: X] | [ROLE-MECHANISM: Y]" in a single
  Description cell) satisfies C-38 but is C-40 noncompliant -- do not use it.
  Only the column-header form (separate named [IA-VERDICT] and [ROLE-MECHANISM] columns)
  satisfies the table-column level requirement. A reviewer auditing this section can verify
  the closed path by name without reading format rules [C-45].
  Path negation: see "Eliminated [C-46]:" in structural enforcement levels above [C-46].
```

---

**PHASE A -- ROUTE**

```
## Phase A: Routing

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern] |
| (all files) | default | Inertia Advocate | default -- always included |
```

Coverage gap: `COVERAGE GAP: [file] -- no org.yaml scope pattern covers this path.`

---

**PHASE B -- INERTIA REVIEW**

Entry: Phase A exit met.

The Budget verdict appears as exactly three separate labeled lines below the separator.
Each line begins with its clause label. No clause is embedded in a table cell, in the
Conclusion of another clause, or merged with another clause on the same line.

```
## Phase B: Inertia Advocate

Null hypothesis: The codebase currently [does X via mechanism Y].           <- B1

Cost ledger:                                                                 <- B2

| Cost Category     | Current-State Cost                                        | Adoption Cost (this PR)                          | Net                      |
|-------------------|-----------------------------------------------------------|--------------------------------------------------|--------------------------|
| Maintenance       | [LOW/MED/HIGH -- maintaining current path]                | [maintaining new path post-merge]                | WORSE / BETTER / NEUTRAL |
| Incident exposure | [failure risk/severity under status quo]                  | [residual exposure after merge]                  | WORSE / BETTER / NEUTRAL |
| Integration cost  | [coordination overhead of current approach]               | [churn, downstream wiring, test burden]          | WORSE / BETTER / NEUTRAL |
| Regression risk   | [risk of new failures from current approach as-is]        | [risk introduced by this PR]                     | WORSE / BETTER / NEUTRAL |

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
```

Phase B exit: B1-B5 met; three Budget verdict lines present as separate output lines.

---

**PHASE C -- TECHNICAL REVIEWS**

**C1 -- Phase B Exit Pre-Flight [C-26/C1, scope: Phase B completeness]:**

```
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
```

If any box unchecked: `C1 RESULT: BLOCKED -- [B-number]`

C1 scope is Phase B. C1 RESULT does not confirm any role's READ RECEIPT content.

**Per-Role Output Sequence (C-35/C-36: STEP 1 must precede STEP 2 in the output;
STEP 2 before STEP 1 is a Phase C exit-condition failure -- Phase D blocked):**

Sequence across roles: security/compliance -> domain-specific -> PM/TPM.

**STEP 1 -- READ RECEIPT [must appear in output before STEP 2]:**

Output the READ RECEIPT block now, before writing any C2 RESULT block for this role.

```
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
```

**STEP 2 -- C2 RESULT BLOCK [C-33, C-37, C-39, C-26/C2] [must follow STEP 1 -- C-35/C-36]:**

The C2 RESULT block enumerates all five receipt fields (a)-(e) by label with an explicit
PRESENT or ABSENT verdict per field. The terminal C2 RESULT line derives from the per-field
verdicts above it and appears within this same block. C2 scope is receipt completeness -- not
Phase B. The UNSATISFIED path is handled within this block -- not in a separate adjacent fence.
A reviewer verifies both the per-field evidence and the terminal verdict by reading this
single block. No cross-block reading required [C-39].

```
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
```

C-36 compliance: If "C2 RESULT:" terminal line appears before "## IA READ RECEIPT" header
for this role in the output, this is a Phase C exit-condition failure -- Phase D blocked.

C-37 / C-39 compliance: (a)-(e) each on its own labeled line with PRESENT/ABSENT; terminal
C2 RESULT line is in this same block, derived from the per-field rows above -- no separate
fence, no adjacent prose carrying the verdict.

C-33 scope check: every labeled line in this block targets a receipt field, not Phase B.

**STEP 3 -- PRE-COMMITMENT [C-27, before reading diff]:**

```
PRE-COMMITMENT: [Role Name]

Cost row assessed:  [Maintenance / Incident exposure / Integration cost / Regression risk]
Initial position:   [CONFIRMS / DISPUTES] [Net direction] on [Cost row]
                    [one phrase based on domain knowledge + Phase B ledger]
Basis:              Domain knowledge only. PR diff not yet examined.
                    [one sentence naming the code surface or architectural pattern]

[PRE-COMMITMENT SEALED]
```

**STEP 4 -- FINDINGS [C-34, C-38, C-40, C-43]:**

Apply domain-lens gate per finding:

```
Step A: "Would only [this role] raise this finding, given their domain?"
  YES -> include. NO -> Step B.
Step B: Revise to name domain-owned mechanism. Still NO -> drop.
```

The findings table MUST include a Type column. F-01 MUST have Type = IA-RESPONSE.
[IA-VERDICT] and [ROLE-MECHANISM] MUST be column headers.

```
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
```

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
with named negation sub-entry "Eliminated [C-46]:" [C-41, C-46]; CLOSED PATHS in declaration
+ four-element prohibition in format rules [C-43, C-45]; all findings passed domain-lens gate.

---

**PHASE D -- SYNTHESIS**

Entry: Phase C exit met (C-36 ordering, C-37/C-39 self-contained block, C-38/C-40
column-header schema, C-41/C-46 three-level partition + named negation sub-entry,
C-43/C-45 CLOSED PATHS in declaration + format rules restatement).

```
## Phase D: Consensus

IA cost ledger: Budget strength was [HIGH / MEDIUM / LOW].
  WORSE rows were: [restate]. BETTER rows were: [restate].
  Technical roles collectively [reinforced / challenged / defeated] the IA's estimate.
  Net: [one sentence]

Agreement: [area] -- [role-A] and [role-B] independently raised [concern]

Divergence: [role-A] rates [area] P[N]; [role-B] rates P[N].
  Mechanism: [architectural property of the code -- not perspective difference]

Critical: [F-XX from role] -- [why this most threatens the merge]
```

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

```
## Phase E: Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from role] -- [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] -- sign-off: [role who confirms before merge]
```

One decision. Values: GO, NO-GO, GO WITH CONDITIONS only.
Delegated decisions fail. Hedged decisions fail.

---

**AMEND**

When invoked with an AMEND directive, output this named-field block before Phase A.

```
## AMEND SCOPE

What was amended:           [description]
Roles added:                [list, or "none"]
Roles removed:              [list, or "none"]
Files triggering addition:  [list, or "n/a -- manually directed"]
Prior findings superseded:  [F-IDs, or "none -- first run"]
```

Run Phases A-E with the amended scope.
