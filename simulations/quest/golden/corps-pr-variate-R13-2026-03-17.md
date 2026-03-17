---
skill: quest-variate
skill_target: corps-pr
round: 13
date: 2026-03-17
rubric_version: 11
---

# Variate R13 — corps-pr

5 complete prompt body variations for the `corps-pr` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Axes Selected

| Axis | Used In | R13 Focus |
|------|---------|----------|
| Lifecycle emphasis (C-36: Phase C exit condition names READ RECEIPT-before-C2-RESULT ordering as a named compliance item — violation is a phase-gate failure, not only a C-35 output gap) | V-01, V-04, V-05 | C-36: C-35 names the ordering in output; C-36 requires the pipeline exit condition to name it as a phase-gate failure trigger, not merely a listed condition |
| Output format (C-37: C2 RESULT block enumerates receipt fields (a)-(e) by label with an explicit PRESENT/ABSENT verdict per field inside the C2 RESULT block — not only in a preceding check) | V-02, V-04, V-05 | C-37: V-05 had a separate C2 Receipt Check block with per-field lines, but the C2 RESULT: SATISFIED terminal line carried no per-field enumeration; C-37 requires the per-field audit to appear within the C2 RESULT block itself |
| Phrasing register — schema formalization (C-38: F-01 IA-RESPONSE Description field uses two named schema slots [IA-VERDICT] and [ROLE-MECHANISM] as visible output labels — not prose that includes both components without naming them as slots) | V-03, V-04, V-05 | C-38: V-05's F-01 Description was "IA found X; role rates P-N because Y" — both components present (C-34 pass) but no labeled slots; C-38 requires [IA-VERDICT: ...] and [ROLE-MECHANISM: ...] as independently matchable labels in the output |

**Baseline (R11 V-05 against v11 rubric)**:
- C-36 fails: Phase C exit condition lists ordering as item (3) but does not name violation as a phase-gate failure — just a listed condition, not an elevated compliance item
- C-37 fails: C2 RESULT: SATISFIED terminal line carries no per-field enumeration; per-field check appears in a separate preceding block, not within the C2 RESULT block itself
- C-38 fails: F-01 Description template "IA found X; role rates P-N because Y" — both C-34 components present but not declared as named schema slots [IA-VERDICT] and [ROLE-MECHANISM]

**R13 target**: V-05 addresses all three simultaneously while preserving R11 V-05's full 27/27 aspirational pass set → 30/30 aspirational against v11.

---

## V-01 — Lifecycle Emphasis: C-36 Phase C Exit Condition as Phase-Gate Failure Trigger

**Axis**: Lifecycle emphasis
**Hypothesis**: R11 V-05's Phase C exit condition item (3) listed "READ RECEIPT precedes C2 RESULT per role in the output [C-35]" as a condition but did not name violation as a phase-gate failure. C-36 is not satisfied by listing the ordering — it requires the exit condition to explicitly state that a C-35 ordering violation elevates to a Phase C exit-condition failure, blocking Phase D from starting. This is the C-30 analog: C-30 made PRE-COMMITMENT absence a phase-gate violation (not only a C-27 format issue); C-36 does the same for READ RECEIPT ordering. A run that produces correct output ordering (passing C-35) without the phase-gate failure language in the exit condition satisfies C-35 and fails C-36. V-01 adds exactly one change to V-05: item (3) in the Phase C exit condition gains explicit phase-gate failure language and the Phase C summary line names it as an exit-condition violation trigger.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline. Five structural
compliance mechanisms are active: string-matchable Budget verdict (C-25), named result
tokens (C-26), PRE-COMMITMENT blocks (C-27), receipt-completeness / ordering pair
(C-33 + C-35), and F-01 IA-RESPONSE template typing (C-34). Read the full pipeline
declaration before producing any output.

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
              C2 RESULT must appear after READ RECEIPT block in output [C-35].
              Terminal: C2 RESULT: SATISFIED
              or C2 RESULT: UNSATISFIED -- [field (x): missing]
  Exit:     (1) C1 ends in ALL CLEAR
            (2) All C2 blocks end in SATISFIED
            (3) READ RECEIPT precedes C2 RESULT per role in the output [C-35/C-36] --
                a C2 RESULT line that appears before its role's READ RECEIPT block is a
                Phase C exit-condition failure, not only a C-35 output ordering gap;
                Phase D does not begin until this condition is met for every role
            (4) C2 verified receipt field completeness, not Phase B [C-33]
            (5) PRE-COMMITMENT blocks precede findings tables [C-27]
            (6) F-01 in every findings table: Type = IA-RESPONSE, Description contains
                IA verdict/cost position AND role mechanism in the same entry [C-34]
            (7) All findings passed domain-lens gate
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26, C-27, C-33, C-34, C-35, C-36

Phase D -- Synthesis
  Entry:    Phase C exit met (all 7 exit conditions satisfied, including C-36 ordering)
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
a STEP 2 line before STEP 1 is a Phase C exit-condition failure):**

Sequence across roles: security/compliance -> domain-specific -> PM/TPM.

**STEP 1 -- READ RECEIPT [must appear in output before STEP 2]:**

Output the READ RECEIPT block now, before writing any C2 RESULT line for this role.

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

**STEP 2 -- C2 RECEIPT FIELD CHECK [C-33, C-26/C2] [must follow STEP 1 in output -- C-35/C-36]:**

C2 scope is READ RECEIPT completeness. Verify that the receipt written in STEP 1 contains
all five fields. Do not re-verify Phase B content here -- that is C1's scope.

```
## C2 Receipt Check -- [Role Name]

(a) Section read named:    present / absent
(b) Budget verdict:        present / absent
    -- note if any of the three verdict sub-lines use placeholder text
(c) Budget strength:       present / absent
(d) Ledger row named:      present / absent
(e) Initial position:      present / absent
    -- valid forms: (i) stated inline, or
                    (ii) "see PRE-COMMITMENT block: [row name], committed below/above"

C2 RESULT: SATISFIED
```

C-35/C-36 check: scan the output text for this role. Locate the READ RECEIPT block header
("## IA READ RECEIPT -- [Role Name]"). Locate the C2 RESULT line. If the C2 RESULT line
appears before the READ RECEIPT block header, this is a Phase C exit-condition failure --
not a formatting issue. Phase D does not begin.

C-33 check: each checklist line addresses a receipt field, not Phase B content.

If any receipt field is absent or placeholder:
`C2 RESULT: UNSATISFIED -- [field (x): missing or placeholder]`

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

**STEP 4 -- FINDINGS [C-34]:**

Apply domain-lens gate per finding:

```
Step A: "Would only [this role] raise this finding, given their domain?"
  YES -> include. NO -> Step B.
Step B: Revise to name domain-owned mechanism. Still NO -> drop.
```

The findings table MUST include a Type column. F-01 MUST have Type = IA-RESPONSE.

```
## Phase C: [Role Name]

Source files:  [from Phase A routing]
Orientation:   [one phrase from .craft/roles/]

[STEP 1: READ RECEIPT]
[STEP 2: C2 RECEIPT CHECK -- C2 RESULT follows receipt block; violation is Phase C exit failure]
[STEP 3: PRE-COMMITMENT]

Findings:

| ID | Type | Severity | Description | Domain-Lens | Owner | Resolution |
|----|------|----------|-------------|-------------|-------|------------|
| F-01 | IA-RESPONSE | P1/P2/P3 | IA found [verdict/cost position]; [role] rates [P-N] because [specific mechanism in this role's domain -- names code artifact] | Passed | [role] | [action] |
| F-02 | DOMAIN | P1/P2/P3 | [domain finding] | Passed | [role] | [action] |
[minimum 2]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3

Post-commitment delta:
  Pre-committed:   [CONFIRMS / DISPUTES] [Cost row]
  After findings:  [HELD / CHANGED]
  If HELD:         [code artifact from diff that confirmed the position]
  If CHANGED:      [code artifact that changed it; revised position]
```

F-01 IA-RESPONSE format rules:
- Type cell: exactly "IA-RESPONSE" -- no other value passes
- Description: "[IA found X; [role] rates P-N because Y]" where X is the IA verdict or
  cost position (named from the cost ledger or IA verdict line) and Y is the code
  mechanism within this role's domain
- A description that names only a domain finding without the IA position fails C-34
- A description that names only the IA position without the role's disagreeing mechanism fails C-34
- Both must appear in the same Description cell

Phase C exit: C1 ALL CLEAR (Phase B scope); every C2 SATISFIED (receipt scope);
READ RECEIPT precedes C2 RESULT per role -- ordering violation is a Phase C exit-condition
failure, Phase D blocked [C-35/C-36]; PRE-COMMITMENT before findings; F-01 Type=IA-RESPONSE;
all findings passed domain-lens gate.

---

**PHASE D -- SYNTHESIS**

Entry: Phase C exit met (including C-36 ordering compliance).

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

## V-02 — Output Format: C-37 C2 RESULT Block with Per-Field Enumeration

**Axis**: Output format
**Hypothesis**: R11 V-05's per-role structure had a "C2 Receipt Check" block (per-field present/absent checklist) preceding the "C2 RESULT: SATISFIED" terminal line. C-37 requires the per-field enumeration to appear within the C2 RESULT block itself -- not in a separate preceding block. A C2 RESULT: SATISFIED that follows a separate per-field check block (even if that block is a complete receipt audit) satisfies C-33 but fails C-37 because the C2 RESULT terminal line carries no per-field audit evidence: a reviewer reading only the "C2 RESULT: SATISFIED" line cannot verify which fields were checked without reading the preceding block. V-02 merges the per-field check into the C2 RESULT block: the block header is "C2 RESULT", each field (a)-(e) has an explicit PRESENT/ABSENT verdict as a separate labeled line, and the terminal "C2 RESULT: SATISFIED" or "C2 RESULT: UNSATISFIED -- [field]" line derives from the per-field verdicts in the same block. A reviewer can confirm all five fields and the terminal verdict by reading the single block without consulting adjacent blocks.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline. Five structural
compliance mechanisms are active: string-matchable Budget verdict (C-25), named result
tokens (C-26), PRE-COMMITMENT blocks (C-27), receipt-completeness / ordering pair
(C-33 + C-35), and F-01 IA-RESPONSE template typing (C-34). Read the full pipeline
declaration before producing any output.

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
              C2 RESULT block enumerates all five receipt fields (a)-(e) by label
              with an explicit PRESENT/ABSENT verdict per field [C-37].
              C2 RESULT must appear after READ RECEIPT block in output [C-35].
              Terminal: C2 RESULT: SATISFIED [all five PRESENT]
              or C2 RESULT: UNSATISFIED -- [field (x): ABSENT]
  Exit:     (1) C1 ends in ALL CLEAR
            (2) All C2 blocks end in SATISFIED
            (3) READ RECEIPT precedes C2 RESULT per role in the output [C-35]
            (4) C2 verified receipt field completeness, not Phase B [C-33]; C2 block
                enumerates (a)-(e) with PRESENT/ABSENT per field [C-37]
            (5) PRE-COMMITMENT blocks precede findings tables [C-27]
            (6) F-01 in every findings table: Type = IA-RESPONSE, Description contains
                IA verdict/cost position AND role mechanism in the same entry [C-34]
            (7) All findings passed domain-lens gate
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26, C-27, C-33, C-34, C-35, C-37

Phase D -- Synthesis
  Entry:    Phase C exit met
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

**Per-Role Output Sequence (C-35: STEP 1 must precede STEP 2 in the output):**

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

**STEP 2 -- C2 RESULT BLOCK [C-33, C-37, C-26/C2] [must follow STEP 1 in output -- C-35]:**

The C2 RESULT block enumerates all five receipt fields by label with an explicit PRESENT or
ABSENT verdict on each field's own line. The terminal C2 RESULT: SATISFIED / UNSATISFIED
line derives from the per-field verdicts above it in the same block. Do not re-verify Phase B
content here -- that is C1's scope. A reviewer must be able to verify each field's verdict
and the overall result by reading this single block.

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

C-33 scope check: every labeled line in this block targets a receipt field. A line that
re-checks "WORSE rows cited verbatim" is a Phase B check -- remove it.

C-37 compliance: each of (a)-(e) appears on its own labeled line with a PRESENT/ABSENT
verdict. The C2 RESULT: SATISFIED line cites "all five fields PRESENT" making its basis
independently verifiable from the per-field lines above it in this block.

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

**STEP 4 -- FINDINGS [C-34]:**

Apply domain-lens gate per finding:

```
Step A: "Would only [this role] raise this finding, given their domain?"
  YES -> include. NO -> Step B.
Step B: Revise to name domain-owned mechanism. Still NO -> drop.
```

The findings table MUST include a Type column. F-01 MUST have Type = IA-RESPONSE.

```
## Phase C: [Role Name]

Source files:  [from Phase A routing]
Orientation:   [one phrase from .craft/roles/]

[STEP 1: READ RECEIPT]
[STEP 2: C2 RESULT -- per-field (a)-(e) enumeration + terminal line in same block]
[STEP 3: PRE-COMMITMENT]

Findings:

| ID | Type | Severity | Description | Domain-Lens | Owner | Resolution |
|----|------|----------|-------------|-------------|-------|------------|
| F-01 | IA-RESPONSE | P1/P2/P3 | IA found [verdict/cost position]; [role] rates [P-N] because [specific mechanism in this role's domain -- names code artifact] | Passed | [role] | [action] |
| F-02 | DOMAIN | P1/P2/P3 | [domain finding] | Passed | [role] | [action] |
[minimum 2]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3

Post-commitment delta:
  Pre-committed:   [CONFIRMS / DISPUTES] [Cost row]
  After findings:  [HELD / CHANGED]
  If HELD:         [code artifact from diff that confirmed the position]
  If CHANGED:      [code artifact that changed it; revised position]
```

F-01 IA-RESPONSE format rules:
- Type cell: exactly "IA-RESPONSE"
- Description: "[IA found X; [role] rates P-N because Y]" where X is the IA verdict or
  cost position and Y is the code mechanism within this role's domain
- Both must appear in the same Description cell

Phase C exit: C1 ALL CLEAR (Phase B scope); every C2 SATISFIED -- C2 RESULT block
enumerates (a)-(e) with PRESENT/ABSENT per field, terminal line in same block [C-33, C-37];
READ RECEIPT precedes C2 RESULT per role in output [C-35]; PRE-COMMITMENT before findings;
F-01 Type=IA-RESPONSE; all findings passed domain-lens gate.

---

**PHASE D -- SYNTHESIS**

Entry: Phase C exit met.

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

One decision. Delegated decisions fail. Hedged decisions fail.

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

## V-03 — Phrasing Register / Schema Formalization: C-38 F-01 Named Schema Slots

**Axis**: Phrasing register (formal schema declaration)
**Hypothesis**: R11 V-05's F-01 IA-RESPONSE format rules stated "Description: '[IA found X; [role] rates P-N because Y]'" -- both C-34 components (IA verdict and role mechanism) are required to appear in the same Description cell, and V-05 produced output with both. C-38 closes the remaining gap: the template must declare [IA-VERDICT] and [ROLE-MECHANISM] as separately-labeled schema slots, not as a prose format instruction. The distinction: V-05's format satisfied C-34 because both components were present; C-38 requires the components to be independently matchable by label in the output text without prose parsing. A reviewer checking C-38 compliance should be able to find "[IA-VERDICT:" and "[ROLE-MECHANISM:" as literal strings in the F-01 Description cell. V-03 changes exactly one section: the F-01 IA-RESPONSE template row and format rules adopt the two-slot schema with named labels as visible output text.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline. Five structural
compliance mechanisms are active: string-matchable Budget verdict (C-25), named result
tokens (C-26), PRE-COMMITMENT blocks (C-27), receipt-completeness / ordering pair
(C-33 + C-35), and F-01 IA-RESPONSE template typing with named Description slots (C-34 + C-38).
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
              C2 RESULT must appear after READ RECEIPT block in output [C-35].
              Terminal: C2 RESULT: SATISFIED
              or C2 RESULT: UNSATISFIED -- [field (x): missing]
  Exit:     (1) C1 ends in ALL CLEAR
            (2) All C2 blocks end in SATISFIED
            (3) READ RECEIPT precedes C2 RESULT per role in the output [C-35]
            (4) C2 verified receipt field completeness, not Phase B [C-33]
            (5) PRE-COMMITMENT blocks precede findings tables [C-27]
            (6) F-01 in every findings table: Type = IA-RESPONSE; Description uses
                two-slot schema [IA-VERDICT: ...] | [ROLE-MECHANISM: ...] with both
                slot labels visible in the output cell [C-34, C-38]
            (7) All findings passed domain-lens gate
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26, C-27, C-33, C-34, C-35, C-38

Phase D -- Synthesis
  Entry:    Phase C exit met
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

**Per-Role Output Sequence (C-35: STEP 1 must precede STEP 2 in the output):**

Sequence across roles: security/compliance -> domain-specific -> PM/TPM.

**STEP 1 -- READ RECEIPT [must appear in output before STEP 2]:**

Output the READ RECEIPT block now, before writing any C2 RESULT line for this role.

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

**STEP 2 -- C2 RECEIPT FIELD CHECK [C-33, C-26/C2] [must follow STEP 1 in output -- C-35]:**

C2 scope is READ RECEIPT completeness. Verify that the receipt written in STEP 1 contains
all five fields. Do not re-verify Phase B content here -- that is C1's scope.

```
## C2 Receipt Check -- [Role Name]

(a) Section read named:    present / absent
(b) Budget verdict:        present / absent
    -- note if any of the three verdict sub-lines use placeholder text
(c) Budget strength:       present / absent
(d) Ledger row named:      present / absent
(e) Initial position:      present / absent
    -- valid forms: (i) stated inline, or
                    (ii) "see PRE-COMMITMENT block: [row name], committed below/above"

C2 RESULT: SATISFIED
```

If any receipt field is absent or placeholder:
`C2 RESULT: UNSATISFIED -- [field (x): missing or placeholder]`

C-33 check: each checklist line addresses a receipt field, not Phase B content.

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
F-01 Description MUST use the two-slot schema with both labels visible in the output cell.

```
## Phase C: [Role Name]

Source files:  [from Phase A routing]
Orientation:   [one phrase from .craft/roles/]

[STEP 1: READ RECEIPT]
[STEP 2: C2 RECEIPT CHECK -- C2 RESULT follows receipt block per C-35]
[STEP 3: PRE-COMMITMENT]

Findings:

| ID | Type | Severity | Description | Domain-Lens | Owner | Resolution |
|----|------|----------|-------------|-------------|-------|------------|
| F-01 | IA-RESPONSE | P1/P2/P3 | [IA-VERDICT: IA's verdict or cost position] | [ROLE-MECHANISM: specific code artifact or mechanism in this role's domain] | Passed | [role] | [action] |
| F-02 | DOMAIN | P1/P2/P3 | [domain finding] | Passed | [role] | [action] |
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
- Description field: two-slot schema -- both slot labels MUST appear as visible text in the cell:
    [IA-VERDICT: <the IA's verdict or cost position from Phase B>]
    [ROLE-MECHANISM: <the specific code artifact or mechanism in this role's domain>]
  The labels [IA-VERDICT] and [ROLE-MECHANISM] are separately matchable in the output.
  A description of the form "IA found X; [role] rates P-N because Y" names both components
  but uses no labeled slots -- satisfies C-34, fails C-38.
  A description with [IA-VERDICT: X] but no [ROLE-MECHANISM: Y] label fails both C-34 and C-38.
  Both labeled slots must appear in the same Description cell.
- Note: the findings table has two content columns for F-01 (IA-VERDICT slot and
  ROLE-MECHANISM slot) -- write them as two separate cells in the table row [C-38]

Phase C exit: C1 ALL CLEAR (Phase B scope); every C2 SATISFIED (receipt scope, post-receipt
in output per C-35); PRE-COMMITMENT before findings; F-01 Type=IA-RESPONSE with
[IA-VERDICT] and [ROLE-MECHANISM] labeled slots visible in output [C-34/C-38];
all findings passed domain-lens gate.

---

**PHASE D -- SYNTHESIS**

Entry: Phase C exit met.

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

One decision. Delegated decisions fail. Hedged decisions fail.

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

## V-04 -- Combination: C-36 + C-37 (Phase-Gate Elevation + Per-Field C2 Enumeration)

**Axes**: Lifecycle emphasis + Output format
**Hypothesis**: V-01 added phase-gate failure language to Phase C exit condition item (3) for the ordering requirement (C-36). V-02 merged the per-field receipt check into the C2 RESULT block with explicit PRESENT/ABSENT per field (C-37). The integration argument: C-36 and C-37 are complementary enforcement elevations on the same chain. C-36 elevates the ordering violation to a phase-gate failure (structural enforcement on the pipeline level); C-37 elevates the completeness audit to per-field granularity visible in the C2 RESULT block (structural enforcement on the block level). Neither change affects the F-01 Description format (C-38 remains unaddressed). V-04 wires both in one prompt: Phase C exit condition item (3) carries the phase-gate failure language; the C2 RESULT block carries per-field (a)-(e) enumeration with PRESENT/ABSENT verdicts and a terminal line referencing all five fields.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline. Six structural
compliance mechanisms are active: string-matchable Budget verdict (C-25), named result
tokens (C-26), PRE-COMMITMENT blocks (C-27), receipt-completeness / ordering pair
(C-33 + C-35), F-01 IA-RESPONSE template typing (C-34), and ordering as phase-gate
failure / per-field C2 enumeration (C-36 + C-37). Read the full pipeline declaration
before producing any output.

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
            (6) F-01 in every findings table: Type = IA-RESPONSE, Description contains
                IA verdict/cost position AND role mechanism in the same entry [C-34]
            (7) All findings passed domain-lens gate
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26, C-27, C-33, C-34,
            C-35, C-36, C-37

Phase D -- Synthesis
  Entry:    Phase C exit met (including C-36 ordering and C-37 per-field compliance)
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

**Per-Role Output Sequence (C-35/C-36: STEP 1 must precede STEP 2; a STEP 2 before STEP 1
is a Phase C exit-condition failure, not a format issue):**

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

C-36 compliance: scan the output text for this role. If the "## C2 RESULT" block header
or the "C2 RESULT:" terminal line appears before the "## IA READ RECEIPT" block header
for this role, this is a Phase C exit-condition failure. Phase D is blocked.

C-37 compliance: each of (a)-(e) appears on its own labeled line with a PRESENT/ABSENT
verdict; the terminal C2 RESULT: SATISFIED line cites "all five fields PRESENT."

C-33 scope check: every labeled line in this block targets a receipt field, not Phase B
content.

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

**STEP 4 -- FINDINGS [C-34]:**

Apply domain-lens gate per finding:

```
Step A: "Would only [this role] raise this finding, given their domain?"
  YES -> include. NO -> Step B.
Step B: Revise to name domain-owned mechanism. Still NO -> drop.
```

The findings table MUST include a Type column. F-01 MUST have Type = IA-RESPONSE.

```
## Phase C: [Role Name]

Source files:  [from Phase A routing]
Orientation:   [one phrase from .craft/roles/]

[STEP 1: READ RECEIPT]
[STEP 2: C2 RESULT -- (a)-(e) per-field verdicts + terminal line in same block]
[STEP 3: PRE-COMMITMENT]

Findings:

| ID | Type | Severity | Description | Domain-Lens | Owner | Resolution |
|----|------|----------|-------------|-------------|-------|------------|
| F-01 | IA-RESPONSE | P1/P2/P3 | IA found [verdict/cost position]; [role] rates [P-N] because [specific mechanism in this role's domain -- names code artifact] | Passed | [role] | [action] |
| F-02 | DOMAIN | P1/P2/P3 | [domain finding] | Passed | [role] | [action] |
[minimum 2]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3

Post-commitment delta:
  Pre-committed:   [CONFIRMS / DISPUTES] [Cost row]
  After findings:  [HELD / CHANGED]
  If HELD:         [code artifact from diff that confirmed the position]
  If CHANGED:      [code artifact that changed it; revised position]
```

F-01 IA-RESPONSE format rules:
- Type cell: exactly "IA-RESPONSE"
- Description: "[IA found X; [role] rates P-N because Y]" where X is IA verdict/cost
  position and Y is the code mechanism within this role's domain -- both in same cell

Phase C exit: C1 ALL CLEAR; every C2 RESULT block enumerates (a)-(e) PRESENT/ABSENT
[C-33, C-37]; READ RECEIPT precedes C2 RESULT per role -- ordering violation is Phase C
exit-condition failure [C-35/C-36]; PRE-COMMITMENT before findings; F-01 Type=IA-RESPONSE;
all findings passed gate.

---

**PHASE D -- SYNTHESIS**

Entry: Phase C exit met (C-36 ordering and C-37 per-field compliance confirmed).

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

One decision. Delegated decisions fail. Hedged decisions fail.

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

## V-05 -- Full R13 Integration: C-36 + C-37 + C-38

**Axes**: Lifecycle emphasis + Output format + Phrasing register (schema formalization)
**Hypothesis**: V-01 (C-36), V-02 (C-37), and V-03 (C-38) each address one structural gap from v11. V-04 showed C-36 and C-37 are complementary enforcement elevations on the same ordering chain. V-05 adds C-38 to the integrated structure. The three mechanisms are independent and non-overlapping: C-36 elevates ordering violation to phase-gate failure (pipeline level); C-37 elevates C2 audit to per-field granularity visible in the C2 RESULT block itself (block level); C-38 elevates F-01 Description to named schema slots visible in the output cell (template level). A variation that addresses two of three -- e.g., ordering elevated and per-field C2, but F-01 Description still prose -- passes C-36 and C-37 and fails C-38. All three must be active simultaneously. V-05 is the direct path to 30/30 aspirational against rubric v11: it preserves the full R11 V-05 pass set (C-33, C-34, C-35 and everything prior) and adds the three new phase-gate / block / template enforcement layers.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline. Seven structural
compliance mechanisms are active: string-matchable Budget verdict (C-25), named result
tokens (C-26), PRE-COMMITMENT blocks (C-27), receipt-completeness / ordering pair
(C-33 + C-35), F-01 IA-RESPONSE template typing with named Description slots (C-34 + C-38),
ordering as phase-gate failure (C-36), and per-field C2 RESULT enumeration (C-37).
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
                separately-labeled slots visible in the output cell [C-34, C-38]
            (7) All findings passed domain-lens gate
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26, C-27, C-33, C-34,
            C-35, C-36, C-37, C-38

Phase D -- Synthesis
  Entry:    Phase C exit met (all 7 conditions including C-36 ordering, C-37 per-field,
            and C-38 named slots)
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

**STEP 2 -- C2 RESULT BLOCK [C-33, C-37, C-26/C2] [must follow STEP 1 -- C-35/C-36]:**

The C2 RESULT block enumerates all five receipt fields (a)-(e) by label with an explicit
PRESENT or ABSENT verdict per field as a separate labeled line. The terminal C2 RESULT
line derives from the per-field verdicts above it in this same block. C2 scope is receipt
field completeness -- not Phase B ledger content. A reviewer must be able to verify all
five field verdicts and the overall result by reading this single block without consulting
adjacent blocks.

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

C-36 compliance: locate "## IA READ RECEIPT -- [Role Name]" header and "C2 RESULT:"
terminal line for this role in the output. If "C2 RESULT:" appears before the receipt
header, this is a Phase C exit-condition failure -- Phase D blocked.

C-37 compliance: each of (a)-(e) appears as a separate labeled line with PRESENT/ABSENT;
C2 RESULT: SATISFIED cites "all five fields PRESENT" making each field independently
verifiable within this block.

C-33 scope check: every labeled line in this block targets a receipt field, not Phase B
content.

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
F-01 Description MUST use the two-slot schema -- both slot labels visible in the output.

```
## Phase C: [Role Name]

Source files:  [from Phase A routing]
Orientation:   [one phrase from .craft/roles/]

[STEP 1: READ RECEIPT]
[STEP 2: C2 RESULT -- (a)-(e) per-field PRESENT/ABSENT + terminal line in same block]
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
  text in the output cell:
    [IA-VERDICT: <IA's verdict or cost position from Phase B cost ledger or IA verdict line>]
    [ROLE-MECHANISM: <specific code artifact or mechanism in this role's domain>]
  The findings table header row names these columns explicitly: "[IA-VERDICT]" and
  "[ROLE-MECHANISM]" -- making slot compliance independently auditable by column.
  A description of the form "IA found X; [role] rates P-N because Y" names both
  components but carries no labeled slots -- satisfies C-34, fails C-38.
  A cell with [IA-VERDICT: X] but no [ROLE-MECHANISM: Y] label fails both C-34 and C-38.
  Both labeled slots must appear in the F-01 row, either as separate columns (as shown)
  or as "[IA-VERDICT: X] | [ROLE-MECHANISM: Y]" in a single Description cell.
- DOMAIN findings (F-02 onward): use single Description column, [IA-VERDICT] and
  [ROLE-MECHANISM] columns show "--" (not applicable)

Phase C exit: C1 ALL CLEAR (Phase B scope); every C2 RESULT block enumerates (a)-(e)
PRESENT/ABSENT, terminal C2 RESULT: SATISFIED cites all five [C-33, C-37]; READ RECEIPT
precedes C2 RESULT per role -- ordering violation is Phase C exit-condition failure, Phase D
blocked [C-35/C-36]; PRE-COMMITMENT before findings [C-27]; F-01 Type=IA-RESPONSE with
[IA-VERDICT] and [ROLE-MECHANISM] labeled slots visible in output [C-34/C-38]; all findings
passed domain-lens gate.

---

**PHASE D -- SYNTHESIS**

Entry: Phase C exit met (C-36 ordering, C-37 per-field, and C-38 named slots all confirmed).

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

## What changed from R11 V-05

**C-36 (V-01, V-04, V-05)**: Phase C exit condition item (3) gains explicit phase-gate
failure language: "a C2 RESULT line that appears before its role's READ RECEIPT block is a
Phase C exit-condition failure; Phase D does not begin." R11 V-05 listed the ordering as
item (3) but did not name violation as a phase-gate failure. The distinction: C-35 requires
correct ordering in the output; C-36 requires the exit condition to state that a violation
is a Phase C failure (not a C-35 output format gap). Phase D entry condition in V-01 also
references C-36.

**C-37 (V-02, V-04, V-05)**: The separate "C2 Receipt Check" block (with per-field
present/absent followed by a standalone "C2 RESULT: SATISFIED" terminal line) is replaced
by a unified "C2 RESULT" block that contains the per-field enumeration (a)-(e) with
explicit PRESENT/ABSENT verdict on each field's own labeled line, followed immediately by
"C2 RESULT: SATISFIED [all five fields PRESENT]". The per-field verdicts and the terminal
result are within the same block. A reviewer reading the C2 RESULT block alone can verify
all five field verdicts without reading any adjacent block.

**C-38 (V-03, V-05)**: F-01 Description template changes from prose format "IA found X;
[role] rates P-N because Y" to a two-slot schema with [IA-VERDICT: ...] and
[ROLE-MECHANISM: ...] as separately-labeled columns in the findings table (or labeled
slots within a single Description cell). The findings table header in V-05 names the
columns explicitly. Both slot labels must appear as visible text in the F-01 row. The
Phase C exit condition item (6) is updated to name C-38 alongside C-34.
