---
skill: quest-variate
skill_target: corps-pr
round: 14
date: 2026-03-17
rubric_version: 12
---

# Variate R14 — corps-pr

5 complete prompt body variations for the `corps-pr` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Axes Selected

| Axis | Used In | R14 Focus |
|------|---------|----------|
| Output format — block structure (C-39: C2 RESULT block is self-contained; per-field evidence and terminal verdict co-appear in single named block; UNSATISFIED path cannot split to adjacent block) | V-01, V-04, V-05 | C-39: R13 V-05 shows the UNSATISFIED terminal verdict in a separate code fence from the per-field evidence block. A model following the template could write per-field rows in the main block and the UNSATISFIED terminal verdict outside it -- per-field checklist and terminal verdict in different blocks. Self-containment requires a single conditional derivation inside the block. |
| Output format — column-header promotion (C-40: [IA-VERDICT] and [ROLE-MECHANISM] must be column headers; the "or" inline-cell path satisfies C-38 but fails C-40) | V-02, V-05 | C-40: R13 V-05 format rules offer an "or" path -- "[IA-VERDICT: X] | [ROLE-MECHANISM: Y] in a single Description cell" as an alternative to column headers. C-40 requires column headers as the only valid form; slot compliance must be O(1) column-count, not O(cell-content). Removing the "or" path and marking it explicitly as C-38-compliant / C-40-noncompliant closes the gap. |
| Lifecycle emphasis — three-level partition declaration (C-41: pipeline declaration must explicitly name exit-condition / block / table-column levels and assign each criterion family) | V-03, V-04, V-05 | C-41: R13 V-05 satisfies C-36/C-37/C-38 in output but never declares the structural level each criterion family occupies. A reviewer cannot read the pipeline declaration alone and verify the three-level partition. V-03 adds the structural enforcement table. |

**Baseline (R13 V-05 against v12 rubric)**:
- C-39 fails: UNSATISFIED terminal verdict in a separate code fence; per-field rows are in the `## C2 RESULT` block, UNSATISFIED verdict is in an adjacent block -- cross-block reading required in the failure case
- C-40 fails: F-01 format rules include "or" path (`[IA-VERDICT: X] | [ROLE-MECHANISM: Y]` in a single Description cell) -- slot compliance is O(cell-content) not O(column-count) via that path
- C-41 fails: no structural enforcement table in pipeline declaration; C-36/C-37/C-38 are satisfied in output but their structural levels are never declared as a named partition

**R14 target**: V-05 addresses all three while preserving R13 V-05's 30/30 aspirational pass set → 33/33 aspirational against v12.

---

## V-01 — Output Format: C-39 Self-Contained C2 RESULT Block

**Axis**: Output format (block structure)
**Hypothesis**: R13 V-05 STEP 2 shows the SATISFIED path inline within the `## C2 RESULT` block and the UNSATISFIED path in a separate code fence (`If any field is ABSENT: ``` (x)...: ABSENT / C2 RESULT: UNSATISFIED... ```). When a receipt field is actually absent, a model following the template writes the per-field verdicts inside the main block and the UNSATISFIED terminal verdict in the adjacent fence -- two separate named structures, requiring cross-block reading to verify the verdict. C-39 requires both the per-field checklist and the terminal verdict to co-appear in a single named block regardless of outcome. V-01 changes exactly one section: STEP 2 replaces the separate UNSATISFIED fence with a conditional derivation line inside the `## C2 RESULT` block itself. The block's terminal line always derives its verdict from the per-field rows above it -- SATISFIED when all five are PRESENT, UNSATISFIED naming the absent field when any are ABSENT. A reviewer reads one block and finds both the evidence and the conclusion.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline. Seven structural
compliance mechanisms are active: string-matchable Budget verdict (C-25), named result
tokens (C-26), PRE-COMMITMENT blocks (C-27), receipt-completeness / ordering pair
(C-33 + C-35), ordering as phase-gate failure (C-36), self-contained per-field C2 RESULT
block (C-37 + C-39), and F-01 IA-RESPONSE template typing with named Description slots
(C-34 + C-38). Read the full pipeline declaration before producing any output.

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
                field; terminal verdict derives from per-field rows within same block;
                no cross-block reading required to verify verdict [C-33, C-37, C-39]
            (5) PRE-COMMITMENT blocks precede findings tables [C-27]
            (6) F-01 in every findings table: Type = IA-RESPONSE; Description uses
                two-slot schema with [IA-VERDICT: ...] and [ROLE-MECHANISM: ...] as
                separately-labeled slots visible in output [C-34, C-38]
            (7) All findings passed domain-lens gate
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26, C-27, C-33, C-34,
            C-35, C-36, C-37, C-38, C-39

Phase D -- Synthesis
  Entry:    Phase C exit met (all 7 conditions including C-36 ordering, C-37/C-39
            self-contained block, and C-38 named slots)
  Exit:     Consensus complete; all Mechanism lines pass ban-to-fix check
  Gates:    C-03, C-09, C-12, C-13

Phase E -- Decision
  Entry:    Phase D exit met
  Exit:     Exactly one GO / NO-GO / GO WITH CONDITIONS; conditions name sign-off
  Gates:    C-04, C-10
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
PRESENT or ABSENT verdict per field as a separate labeled line. The terminal C2 RESULT
line derives from the per-field verdicts above it and appears within this same block.
C2 scope is receipt field completeness -- not Phase B ledger content.

The UNSATISFIED path is handled within this block -- not in a separate adjacent fence.
A reviewer verifies both the per-field evidence and the terminal verdict by reading this
single block. No cross-block reading is required [C-39].

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

**STEP 4 -- FINDINGS [C-34, C-38]:**

Apply domain-lens gate per finding:

```
Step A: "Would only [this role] raise this finding, given their domain?"
  YES -> include. NO -> Step B.
Step B: Revise to name domain-owned mechanism. Still NO -> drop.
```

The findings table MUST include a Type column. F-01 MUST have Type = IA-RESPONSE.
F-01 Description MUST use the two-slot schema -- both slot labels visible in output.

```
## Phase C: [Role Name]

Source files:  [from Phase A routing]
Orientation:   [one phrase from .craft/roles/]

[STEP 1: READ RECEIPT]
[STEP 2: C2 RESULT -- (a)-(e) per-field + terminal verdict in same block, no separate fence]
[STEP 3: PRE-COMMITMENT]

Findings:

| ID | Type | Severity | [IA-VERDICT] | [ROLE-MECHANISM] | Domain-Lens | Owner | Resolution |
|----|------|----------|--------------|------------------|-------------|-------|------------|
| F-01 | IA-RESPONSE | P1/P2/P3 | [IA-VERDICT: IA's verdict or cost position] | [ROLE-MECHANISM: specific code artifact in this role's domain] | Passed | [role] | [action] |
| F-02 | DOMAIN | P1/P2/P3 | [domain finding] | -- | Passed | [role] | [action] |
[minimum 2]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3

Post-commitment delta:
  Pre-committed:   [CONFIRMS / DISPUTES] [Cost row]
  After findings:  [HELD / CHANGED]
  If HELD:         [code artifact from diff that confirmed the position]
  If CHANGED:      [code artifact that changed it; revised position]
```

F-01 IA-RESPONSE format rules [C-34, C-38]:
- Type cell: exactly "IA-RESPONSE" -- no other value passes
- Description schema: two separately-labeled slots -- both labels MUST appear as visible
  text in the output. Preferred form: separate table columns (as shown above).
  Alternative form (C-38 compliant only): "[IA-VERDICT: X] | [ROLE-MECHANISM: Y]" in a
  single Description cell -- both labels independently matchable.
- A description of the form "IA found X; [role] rates P-N because Y" names both components
  but carries no labeled slots -- satisfies C-34, fails C-38.
- Both labeled slots must appear in the F-01 row.
- DOMAIN findings (F-02 onward): [IA-VERDICT] and [ROLE-MECHANISM] columns show "--"

Phase C exit: C1 ALL CLEAR (Phase B scope); every C2 RESULT block enumerates (a)-(e)
PRESENT/ABSENT and derives terminal verdict in same block -- no cross-block reading [C-33,
C-37, C-39]; READ RECEIPT precedes C2 RESULT per role -- ordering violation is Phase C
exit-condition failure, Phase D blocked [C-35/C-36]; PRE-COMMITMENT before findings [C-27];
F-01 Type=IA-RESPONSE with [IA-VERDICT] and [ROLE-MECHANISM] labeled slots visible [C-34/C-38];
all findings passed domain-lens gate.

---

**PHASE D -- SYNTHESIS**

Entry: Phase C exit met (C-36 ordering, C-37/C-39 self-contained block, C-38 named slots).

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

## V-02 — Output Format: C-40 Column-Header Promotion (No "Or" Path)

**Axis**: Output format (column structure)
**Hypothesis**: R13 V-05 format rules offer an "or" path for F-01 Description: "[IA-VERDICT: X] | [ROLE-MECHANISM: Y] in a single Description cell" as an alternative to separate column headers. The "or" path satisfies C-38 because both slot labels appear as independently matchable text in the output. But C-40 requires [IA-VERDICT] and [ROLE-MECHANISM] to be column headers -- slot compliance must be O(1) column-count, not O(cell-content). The "or" path makes compliance depend on parsing cell content, which is what C-40 is designed to eliminate. V-02 removes the "or" path and marks it explicitly as C-38-compliant / C-40-noncompliant. The table header and F-01 row require separate [IA-VERDICT] and [ROLE-MECHANISM] columns in all cases. The only change from R13 V-05 is the F-01 format rules and the removal of the "or" path language.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline. Seven structural
compliance mechanisms are active: string-matchable Budget verdict (C-25), named result
tokens (C-26), PRE-COMMITMENT blocks (C-27), receipt-completeness / ordering pair
(C-33 + C-35), ordering as phase-gate failure (C-36), per-field C2 RESULT enumeration
(C-37), and F-01 IA-RESPONSE column-header schema (C-34 + C-38 + C-40).
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
              C2 RESULT must appear after READ RECEIPT block in output [C-35].
              Terminal: C2 RESULT: SATISFIED [all five PRESENT]
              or C2 RESULT: UNSATISFIED -- [field (x): ABSENT]
  Exit:     (1) C1 ends in ALL CLEAR
            (2) All C2 blocks end in SATISFIED
            (3) READ RECEIPT precedes C2 RESULT per role in the output [C-35/C-36] --
                a C2 RESULT line that appears before its role's READ RECEIPT block is a
                Phase C exit-condition failure; Phase D does not begin
            (4) C2 RESULT block enumerates receipt fields (a)-(e) with PRESENT/ABSENT
                per field; terminal line cites all five PRESENT [C-33, C-37]
            (5) PRE-COMMITMENT blocks precede findings tables [C-27]
            (6) F-01 in every findings table: Type = IA-RESPONSE; findings table has
                [IA-VERDICT] and [ROLE-MECHANISM] as column headers; F-01 cells populate
                each column; slot compliance is O(1) column-count [C-34, C-38, C-40]
            (7) All findings passed domain-lens gate
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26, C-27, C-33, C-34,
            C-35, C-36, C-37, C-38, C-40

Phase D -- Synthesis
  Entry:    Phase C exit met (all 7 conditions including C-40 column-header compliance)
  Exit:     Consensus complete; all Mechanism lines pass ban-to-fix check
  Gates:    C-03, C-09, C-12, C-13

Phase E -- Decision
  Entry:    Phase D exit met
  Exit:     Exactly one GO / NO-GO / GO WITH CONDITIONS; conditions name sign-off
  Gates:    C-04, C-10
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

**STEP 2 -- C2 RESULT BLOCK [C-33, C-37, C-26/C2] [must follow STEP 1 -- C-35/C-36]:**

The C2 RESULT block enumerates all five receipt fields (a)-(e) by label with an explicit
PRESENT or ABSENT verdict per field. The terminal C2 RESULT line derives from the per-field
verdicts above it. C2 scope is receipt completeness -- not Phase B ledger content.

```
## C2 RESULT -- [Role Name]

(a) Section read named:       PRESENT / ABSENT
(b) Budget verdict populated: PRESENT / ABSENT
(c) Budget strength stated:   PRESENT / ABSENT
(d) Ledger row named:         PRESENT / ABSENT
(e) Initial position stated:  PRESENT / ABSENT
    [valid: inline value OR cross-reference "see PRE-COMMITMENT block: [row]"]

C2 RESULT: SATISFIED   [all five fields PRESENT]
```

If any field is ABSENT:
```
(x) [field label]:   ABSENT

C2 RESULT: UNSATISFIED -- field (x): [what is missing]
```

C-36 compliance: If "C2 RESULT:" terminal line appears before "## IA READ RECEIPT" header
for this role, this is a Phase C exit-condition failure -- Phase D blocked.

C-37 compliance: (a)-(e) each on own labeled line with PRESENT/ABSENT; terminal line
cites "all five fields PRESENT."

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

**STEP 4 -- FINDINGS [C-34, C-38, C-40]:**

Apply domain-lens gate per finding:

```
Step A: "Would only [this role] raise this finding, given their domain?"
  YES -> include. NO -> Step B.
Step B: Revise to name domain-owned mechanism. Still NO -> drop.
```

The findings table MUST include a Type column. F-01 MUST have Type = IA-RESPONSE.
[IA-VERDICT] and [ROLE-MECHANISM] MUST be column headers -- not inline cell labels.

```
## Phase C: [Role Name]

Source files:  [from Phase A routing]
Orientation:   [one phrase from .craft/roles/]

[STEP 1: READ RECEIPT]
[STEP 2: C2 RESULT -- (a)-(e) per-field PRESENT/ABSENT + terminal line]
[STEP 3: PRE-COMMITMENT]

Findings:

| ID | Type | Severity | [IA-VERDICT] | [ROLE-MECHANISM] | Domain-Lens | Owner | Resolution |
|----|------|----------|--------------|------------------|-------------|-------|------------|
| F-01 | IA-RESPONSE | P1/P2/P3 | [IA-VERDICT: IA's verdict or cost position] | [ROLE-MECHANISM: specific code artifact in this role's domain] | Passed | [role] | [action] |
| F-02 | DOMAIN | P1/P2/P3 | [domain finding] | -- | Passed | [role] | [action] |
[minimum 2]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3

Post-commitment delta:
  Pre-committed:   [CONFIRMS / DISPUTES] [Cost row]
  After findings:  [HELD / CHANGED]
  If HELD:         [code artifact from diff that confirmed the position]
  If CHANGED:      [code artifact that changed it; revised position]
```

F-01 IA-RESPONSE format rules [C-34, C-38, C-40]:
- Type cell: exactly "IA-RESPONSE" -- no other value passes
- Column structure: [IA-VERDICT] and [ROLE-MECHANISM] are column headers in the findings
  table -- slot compliance is O(1) column-count. A reviewer verifies presence by counting
  columns, not by parsing cell content.
- F-01 cells: [IA-VERDICT] cell contains the IA's verdict or cost position from Phase B;
  [ROLE-MECHANISM] cell contains the specific code artifact or mechanism in this role's domain.
- The "or" path (inline labels within a single Description cell) is C-38 compliant but
  C-40 noncompliant -- do not use it. Only separate column headers satisfy C-40.
- A description of the form "IA found X; [role] rates P-N because Y" names both components
  but carries no labeled slots -- satisfies C-34, fails C-38 and C-40.
- DOMAIN findings (F-02 onward): [IA-VERDICT] and [ROLE-MECHANISM] columns show "--"

Phase C exit: C1 ALL CLEAR (Phase B scope); every C2 RESULT block enumerates (a)-(e)
PRESENT/ABSENT, terminal line cites all five [C-33, C-37]; READ RECEIPT precedes C2 RESULT
per role -- ordering violation is Phase C exit-condition failure, Phase D blocked [C-35/C-36];
PRE-COMMITMENT before findings [C-27]; F-01 Type=IA-RESPONSE with [IA-VERDICT] and
[ROLE-MECHANISM] as column headers in the findings table [C-34/C-38/C-40]; all findings
passed domain-lens gate.

---

**PHASE D -- SYNTHESIS**

Entry: Phase C exit met (C-36 ordering, C-37 per-field, C-38/C-40 column-header compliance).

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

## V-03 — Lifecycle Emphasis: C-41 Three-Level Structural Enforcement Partition

**Axis**: Lifecycle emphasis (pipeline declaration)
**Hypothesis**: R13 V-05 satisfies C-36 (exit-condition enforcement), C-37 (block-level enumeration), and C-38 (template-level named slots) in output but never declares the structural level each criterion family occupies. C-41 requires the pipeline declaration itself to name three structural enforcement levels and assign each criterion family to its natural layer -- so that a reviewer reading the pipeline declaration alone can verify the partition without reading skill output. V-03 adds a STRUCTURAL ENFORCEMENT LEVELS section to the pipeline declaration, assigning C-36 to exit-condition level, C-37/C-39 to block level, C-38/C-40 to table-column level. The only change from R13 V-05 is the addition of this section. C-39 and C-40 are not active in V-03 output (UNSATISFIED still in separate fence; "or" path retained in format rules) -- but the declaration names them at their levels, establishing the framework that V-05 will fully populate.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline. Eight structural
compliance mechanisms are active: string-matchable Budget verdict (C-25), named result
tokens (C-26), PRE-COMMITMENT blocks (C-27), receipt-completeness / ordering pair
(C-33 + C-35), ordering as phase-gate failure (C-36), per-field C2 RESULT enumeration
(C-37), F-01 IA-RESPONSE template typing with named Description slots (C-34 + C-38), and
three-level structural enforcement partition declared in pipeline (C-41).
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
              C2 RESULT must appear after READ RECEIPT block in output [C-35].
              Terminal: C2 RESULT: SATISFIED [all five PRESENT]
              or C2 RESULT: UNSATISFIED -- [field (x): ABSENT]
  Exit:     (1) C1 ends in ALL CLEAR
            (2) All C2 blocks end in SATISFIED
            (3) READ RECEIPT precedes C2 RESULT per role in the output [C-35/C-36] --
                a C2 RESULT line that appears before its role's READ RECEIPT block is a
                Phase C exit-condition failure; Phase D does not begin
            (4) C2 RESULT block enumerates receipt fields (a)-(e) with PRESENT/ABSENT
                per field; terminal line cites all five PRESENT [C-33, C-37]
            (5) PRE-COMMITMENT blocks precede findings tables [C-27]
            (6) F-01 in every findings table: Type = IA-RESPONSE; Description uses
                two-slot schema with [IA-VERDICT: ...] and [ROLE-MECHANISM: ...] as
                separately-labeled slots visible in output [C-34, C-38]
            (7) All findings passed domain-lens gate
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26, C-27, C-33, C-34,
            C-35, C-36, C-37, C-38, C-41

Phase D -- Synthesis
  Entry:    Phase C exit met (all 7 conditions including C-36 ordering, C-37 per-field,
            C-38 named slots)
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
          no cross-block reading required to verify the verdict.
    Auditable by reading the C2 RESULT block alone.
  Table-column level -- findings table header row:
    C-38: F-01 IA-RESPONSE Description field declares [IA-VERDICT] and [ROLE-MECHANISM]
          as named schema slots visible in output.
    C-40: [IA-VERDICT] and [ROLE-MECHANISM] are column headers in the findings table;
          slot compliance is O(1) column-count check.
    Auditable by counting table columns alone.
  Each level is independently auditable without reading adjacent levels.
  No two criterion families share a level.
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

**STEP 2 -- C2 RESULT BLOCK [C-33, C-37, C-26/C2] [must follow STEP 1 -- C-35/C-36]:**

The C2 RESULT block enumerates all five receipt fields (a)-(e) by label with an explicit
PRESENT or ABSENT verdict per field. The terminal C2 RESULT line derives from the per-field
verdicts above it in this same block. C2 scope is receipt completeness -- not Phase B.

```
## C2 RESULT -- [Role Name]

(a) Section read named:       PRESENT / ABSENT
(b) Budget verdict populated: PRESENT / ABSENT
(c) Budget strength stated:   PRESENT / ABSENT
(d) Ledger row named:         PRESENT / ABSENT
(e) Initial position stated:  PRESENT / ABSENT
    [valid: inline value OR cross-reference "see PRE-COMMITMENT block: [row]"]

C2 RESULT: SATISFIED   [all five fields PRESENT]
```

If any field is ABSENT:
```
(x) [field label]:   ABSENT

C2 RESULT: UNSATISFIED -- field (x): [what is missing]
```

C-36 compliance: If "C2 RESULT:" appears before "## IA READ RECEIPT" for this role,
this is a Phase C exit-condition failure -- Phase D blocked.

C-37 compliance: (a)-(e) each on own labeled line with PRESENT/ABSENT; terminal line
cites "all five fields PRESENT."

C-33 scope: every labeled line targets a receipt field, not Phase B content.

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

**STEP 4 -- FINDINGS [C-34, C-38]:**

Apply domain-lens gate per finding:

```
Step A: "Would only [this role] raise this finding, given their domain?"
  YES -> include. NO -> Step B.
Step B: Revise to name domain-owned mechanism. Still NO -> drop.
```

The findings table MUST include a Type column. F-01 MUST have Type = IA-RESPONSE.
F-01 Description MUST use the two-slot schema -- both slot labels visible in output.

```
## Phase C: [Role Name]

Source files:  [from Phase A routing]
Orientation:   [one phrase from .craft/roles/]

[STEP 1: READ RECEIPT]
[STEP 2: C2 RESULT -- (a)-(e) per-field PRESENT/ABSENT + terminal line]
[STEP 3: PRE-COMMITMENT]

Findings:

| ID | Type | Severity | [IA-VERDICT] | [ROLE-MECHANISM] | Domain-Lens | Owner | Resolution |
|----|------|----------|--------------|------------------|-------------|-------|------------|
| F-01 | IA-RESPONSE | P1/P2/P3 | [IA-VERDICT: IA's verdict or cost position] | [ROLE-MECHANISM: specific code artifact in this role's domain] | Passed | [role] | [action] |
| F-02 | DOMAIN | P1/P2/P3 | [domain finding] | -- | Passed | [role] | [action] |
[minimum 2]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3

Post-commitment delta:
  Pre-committed:   [CONFIRMS / DISPUTES] [Cost row]
  After findings:  [HELD / CHANGED]
  If HELD:         [code artifact from diff that confirmed the position]
  If CHANGED:      [code artifact that changed it; revised position]
```

F-01 IA-RESPONSE format rules [C-34, C-38]:
- Type cell: exactly "IA-RESPONSE" -- no other value passes
- Description schema: two separately-labeled slots -- both labels MUST appear as visible
  text in the output cell. Preferred form: separate table columns (as shown above).
  Alternative form (C-38 compliant): "[IA-VERDICT: X] | [ROLE-MECHANISM: Y]" in a single
  Description cell -- both labels independently matchable.
  Note: the alternative form satisfies C-38 but does not satisfy C-40 (column-header
  promotion). C-40 requires column headers; the alternative form is O(cell-content).
- DOMAIN findings (F-02 onward): [IA-VERDICT] and [ROLE-MECHANISM] columns show "--"

Phase C exit: C1 ALL CLEAR; every C2 RESULT block enumerates (a)-(e) PRESENT/ABSENT [C-33,
C-37]; READ RECEIPT precedes C2 RESULT per role -- ordering violation is Phase C
exit-condition failure [C-35/C-36]; PRE-COMMITMENT before findings [C-27]; F-01
Type=IA-RESPONSE with [IA-VERDICT]/[ROLE-MECHANISM] labeled slots [C-34/C-38]; three-level
structural enforcement levels declared in pipeline [C-41]; all findings passed gate.

---

**PHASE D -- SYNTHESIS**

Entry: Phase C exit met (C-36 ordering, C-37 per-field, C-38 named slots, C-41 declared).

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

## V-04 — Combination: C-39 + C-41 (Self-Contained Block + Declared Partition)

**Axes**: Output format (block structure) + Lifecycle emphasis (pipeline declaration)
**Hypothesis**: C-39 and C-41 are structurally connected at the block level: C-39 is the block-level closure (per-field evidence and terminal verdict in one named block), and C-41 assigns that closure to the block-level slot in the three-level partition. If the C2 RESULT block is not self-contained (C-39 fail), the pipeline declaration names a structural layer that the output violates. V-04 wires both: STEP 2 uses the self-contained conditional template (V-01 change), and the pipeline declaration names the three levels with C-39 at block level (V-03 change). C-40 is not active in V-04 -- the "or" path remains in F-01 format rules. This tests whether block self-containment + declared partition passes C-41 without column-header promotion: the block and exit-condition levels are fully enforced, but the table-column level names C-40 in the declaration without enforcing it in output.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline. Eight structural
compliance mechanisms are active: string-matchable Budget verdict (C-25), named result
tokens (C-26), PRE-COMMITMENT blocks (C-27), receipt-completeness / ordering pair
(C-33 + C-35), ordering as phase-gate failure (C-36), self-contained per-field C2 RESULT
block (C-37 + C-39), F-01 IA-RESPONSE template typing with named Description slots
(C-34 + C-38), and three-level structural enforcement partition declared in pipeline (C-41).
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
            (6) F-01 in every findings table: Type = IA-RESPONSE; Description uses
                two-slot schema with [IA-VERDICT: ...] and [ROLE-MECHANISM: ...] as
                separately-labeled slots visible in output [C-34, C-38]
            (7) All findings passed domain-lens gate
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26, C-27, C-33, C-34,
            C-35, C-36, C-37, C-38, C-39, C-41

Phase D -- Synthesis
  Entry:    Phase C exit met (all 7 conditions including C-36 ordering, C-37/C-39
            self-contained block, C-38 named slots, C-41 declared partition)
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
          no cross-block reading required to verify the verdict.
    Auditable by reading the C2 RESULT block alone.
  Table-column level -- findings table header row:
    C-38: F-01 IA-RESPONSE Description field declares [IA-VERDICT] and [ROLE-MECHANISM]
          as named schema slots visible in output.
    C-40: [IA-VERDICT] and [ROLE-MECHANISM] are column headers in the findings table;
          slot compliance is O(1) column-count check.
    Auditable by counting table columns alone.
  Each level is independently auditable without reading adjacent levels.
  No two criterion families share a level.
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

**Per-Role Output Sequence (C-35/C-36: STEP 1 must precede STEP 2; STEP 2 before STEP 1
is a Phase C exit-condition failure -- Phase D blocked):**

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

C-36 compliance: If "C2 RESULT:" appears before "## IA READ RECEIPT" for this role,
Phase C exit-condition failure -- Phase D blocked.

C-37 / C-39 compliance: (a)-(e) each on own labeled line with PRESENT/ABSENT; terminal
verdict in this same block; no separate fence; no adjacent prose carrying the verdict.

C-33 scope: every labeled line targets a receipt field, not Phase B content.

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

**STEP 4 -- FINDINGS [C-34, C-38]:**

Apply domain-lens gate per finding:

```
Step A: "Would only [this role] raise this finding, given their domain?"
  YES -> include. NO -> Step B.
Step B: Revise to name domain-owned mechanism. Still NO -> drop.
```

The findings table MUST include a Type column. F-01 MUST have Type = IA-RESPONSE.
F-01 Description MUST use the two-slot schema -- both slot labels visible in output.

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
| F-01 | IA-RESPONSE | P1/P2/P3 | [IA-VERDICT: IA's verdict or cost position] | [ROLE-MECHANISM: specific code artifact in this role's domain] | Passed | [role] | [action] |
| F-02 | DOMAIN | P1/P2/P3 | [domain finding] | -- | Passed | [role] | [action] |
[minimum 2]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3

Post-commitment delta:
  Pre-committed:   [CONFIRMS / DISPUTES] [Cost row]
  After findings:  [HELD / CHANGED]
  If HELD:         [code artifact from diff that confirmed the position]
  If CHANGED:      [code artifact that changed it; revised position]
```

F-01 IA-RESPONSE format rules [C-34, C-38]:
- Type cell: exactly "IA-RESPONSE" -- no other value passes
- Description schema: two separately-labeled slots -- both labels MUST appear as visible
  text in the output. Preferred form: separate table columns (as shown above).
  Alternative form (C-38 compliant): "[IA-VERDICT: X] | [ROLE-MECHANISM: Y]" in a single
  Description cell. Note: alternative form does not satisfy C-40 (column-header promotion).
- DOMAIN findings (F-02 onward): [IA-VERDICT] and [ROLE-MECHANISM] columns show "--"

Phase C exit: C1 ALL CLEAR; every C2 RESULT block enumerates (a)-(e) PRESENT/ABSENT and
derives terminal verdict in same block [C-33, C-37, C-39]; READ RECEIPT precedes C2 RESULT
per role -- ordering violation is Phase C exit-condition failure [C-35/C-36]; PRE-COMMITMENT
before findings [C-27]; F-01 Type=IA-RESPONSE with [IA-VERDICT]/[ROLE-MECHANISM] labeled
slots [C-34/C-38]; three-level enforcement declared in pipeline [C-41]; all findings passed.

---

**PHASE D -- SYNTHESIS**

Entry: Phase C exit met (C-36 ordering, C-37/C-39 self-contained block, C-38 named slots,
C-41 three-level partition declared in pipeline).

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

## V-05 — Full R14 Integration: C-39 + C-40 + C-41

**Axes**: Output format (block structure) + Output format (column structure) + Lifecycle emphasis (pipeline declaration)
**Hypothesis**: The three new v12 criteria form a complete structural closure at three independent levels. C-39 closes the block-level gap: the C2 RESULT block is self-contained, per-field evidence and terminal verdict always co-appearing in one named block without requiring a separate fence for the UNSATISFIED case. C-40 closes the table-column gap: [IA-VERDICT] and [ROLE-MECHANISM] are column headers only -- the "or" inline-cell path is removed, making slot compliance O(1) column-count. C-41 closes the declaration gap: the pipeline declaration explicitly names the three structural levels (exit-condition / block / table-column) and assigns each criterion family (C-36 / C-37+C-39 / C-38+C-40) to its natural layer, independently auditable without reading output. Each criterion is independent: C-39 can fail while C-40 passes (block split vs column structure are orthogonal), and C-41 requires both the declaration and the output to be consistent. V-05 addresses all three simultaneously, preserving R13 V-05's full 30/30 aspirational pass set and adding the three structural closures that v12 introduced. This is the direct path to 33/33 aspirational against rubric v12.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline. Nine structural
compliance mechanisms are active: string-matchable Budget verdict (C-25), named result
tokens (C-26), PRE-COMMITMENT blocks (C-27), receipt-completeness / ordering pair
(C-33 + C-35), ordering as phase-gate failure (C-36), self-contained per-field C2 RESULT
block (C-37 + C-39), F-01 IA-RESPONSE column-header schema (C-34 + C-38 + C-40), and
three-level structural enforcement partition declared in pipeline (C-41).
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
              Terminal (within C2 RESULT block): C2 RESULT: SATISFIED [all five PRESENT]
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
                [ROLE-MECHANISM] are column headers in the findings table; F-01 cells
                populate each column; slot compliance is O(1) column-count [C-34, C-38, C-40]
            (7) All findings passed domain-lens gate
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26, C-27, C-33, C-34,
            C-35, C-36, C-37, C-38, C-39, C-40, C-41

Phase D -- Synthesis
  Entry:    Phase C exit met (all 7 conditions including C-36 ordering, C-37/C-39
            self-contained block, C-38/C-40 column-header schema, C-41 declared partition)
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
          no cross-block reading required; UNSATISFIED path handled inline, not in separate fence.
    Auditable by reading the C2 RESULT block alone.
  Table-column level -- findings table header row:
    C-38: F-01 IA-RESPONSE Description field declares [IA-VERDICT] and [ROLE-MECHANISM]
          as named schema slots visible in output.
    C-40: [IA-VERDICT] and [ROLE-MECHANISM] are column headers in the findings table;
          slot compliance is O(1) column-count check; no inline-cell "or" path.
    Auditable by counting table columns alone.
  Each level is independently auditable without reading adjacent levels.
  No two criterion families share a level.
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

**Per-Role Output Sequence (C-35/C-36: STEP 1 must precede STEP 2; STEP 2 before STEP 1
is a Phase C exit-condition failure -- Phase D blocked):**

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
Phase B. The UNSATISFIED path is handled within this block using the conditional terminal line
below -- no separate adjacent fence required. A reviewer verifies both the per-field evidence
and the terminal verdict by reading this single block.

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

C-36 compliance: If "C2 RESULT:" appears before "## IA READ RECEIPT" for this role,
Phase C exit-condition failure -- Phase D blocked.

C-37 / C-39 compliance: (a)-(e) each on own labeled line with PRESENT/ABSENT; terminal
verdict is in this same block, derived from the per-field rows above; no separate fence
carries the verdict; a reviewer reads one block to find evidence + conclusion.

C-33 scope: every labeled line targets a receipt field, not Phase B content.

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

**STEP 4 -- FINDINGS [C-34, C-38, C-40]:**

Apply domain-lens gate per finding:

```
Step A: "Would only [this role] raise this finding, given their domain?"
  YES -> include. NO -> Step B.
Step B: Revise to name domain-owned mechanism. Still NO -> drop.
```

The findings table MUST include a Type column. F-01 MUST have Type = IA-RESPONSE.
[IA-VERDICT] and [ROLE-MECHANISM] MUST be column headers -- no inline-cell alternative.

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
| F-01 | IA-RESPONSE | P1/P2/P3 | [IA-VERDICT: IA's verdict or cost position] | [ROLE-MECHANISM: specific code artifact in this role's domain] | Passed | [role] | [action] |
| F-02 | DOMAIN | P1/P2/P3 | [domain finding] | -- | Passed | [role] | [action] |
[minimum 2]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3

Post-commitment delta:
  Pre-committed:   [CONFIRMS / DISPUTES] [Cost row]
  After findings:  [HELD / CHANGED]
  If HELD:         [code artifact from diff that confirmed the position]
  If CHANGED:      [code artifact that changed it; revised position]
```

F-01 IA-RESPONSE format rules [C-34, C-38, C-40]:
- Type cell: exactly "IA-RESPONSE" -- no other value passes
- Column structure: [IA-VERDICT] and [ROLE-MECHANISM] are column headers in the findings
  table. Slot compliance is O(1) column-count: a reviewer verifies presence by counting
  columns. There is no inline-cell "or" path -- the alternative form ("[IA-VERDICT: X] |
  [ROLE-MECHANISM: Y]" in a single Description cell) satisfies C-38 but fails C-40 and
  must not be used.
- F-01 cells: [IA-VERDICT] cell contains the IA's verdict or cost position from Phase B
  cost ledger or IA verdict line; [ROLE-MECHANISM] cell contains the specific code artifact
  or mechanism in this role's domain.
- A description of the form "IA found X; [role] rates P-N because Y" carries no labeled
  slots -- satisfies C-34, fails C-38 and C-40.
- DOMAIN findings (F-02 onward): [IA-VERDICT] and [ROLE-MECHANISM] columns show "--"

Phase C exit: C1 ALL CLEAR (Phase B scope); every C2 RESULT block enumerates (a)-(e)
PRESENT/ABSENT and derives terminal verdict in same block, no separate fence [C-33, C-37,
C-39]; READ RECEIPT precedes C2 RESULT per role -- ordering violation is Phase C
exit-condition failure, Phase D blocked [C-35/C-36]; PRE-COMMITMENT before findings [C-27];
F-01 Type=IA-RESPONSE with [IA-VERDICT] and [ROLE-MECHANISM] as column headers [C-34/C-38/
C-40]; three-level enforcement partition declared in pipeline [C-41]; all findings passed gate.

---

**PHASE D -- SYNTHESIS**

Entry: Phase C exit met (all 7 conditions: C-36 ordering, C-37/C-39 self-contained block,
C-38/C-40 column-header schema, C-41 declared three-level partition).

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

## What changed from R13 V-05

**C-39 (V-01, V-04, V-05)**: STEP 2 template restructured to fold the UNSATISFIED terminal
verdict into the C2 RESULT block. R13 V-05 showed the UNSATISFIED path in a separate code
fence ("If any field is ABSENT: ``` ... ```") -- per-field rows in the main block, terminal
verdict in adjacent fence. C-39 requires both to co-appear in one named block. The fix: a
conditional derivation line at the bottom of the block ("All five PRESENT: C2 RESULT:
SATISFIED -- all five fields PRESENT / Any ABSENT: C2 RESULT: UNSATISFIED -- field (x):
[label]") replaces the separate fence. A reviewer reads one block and finds evidence +
conclusion regardless of outcome.

**C-40 (V-02, V-05)**: F-01 format rules remove the "or" path. R13 V-05 permitted
"[IA-VERDICT: X] | [ROLE-MECHANISM: Y]" in a single Description cell as an alternative
to column headers -- O(cell-content) compliance, not O(column-count). C-40 requires
column headers as the only valid structure. The fix: the "or" path is explicitly marked
"C-38 compliant / C-40 noncompliant -- do not use." The findings table always has [IA-VERDICT]
and [ROLE-MECHANISM] as column headers. Slot compliance is verified by column count alone.

**C-41 (V-03, V-04, V-05)**: A STRUCTURAL ENFORCEMENT LEVELS section is added to the
pipeline declaration. R13 V-05 satisfied C-36/C-37/C-38 in output but never declared their
structural levels as a named partition. C-41 requires the pipeline to name exit-condition /
block / table-column levels and assign each criterion family (C-36 / C-37+C-39 / C-38+C-40)
to its layer. The fix: a declared table in the pipeline maps each criterion family to its
structural level, making the partition independently auditable by reading the pipeline alone.
