---
skill: quest-variate
skill_target: corps-pr
round: 11
date: 2026-03-16
rubric_version: 10
---

# Variate R11 — corps-pr

5 complete prompt body variations for the `corps-pr` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Axes Selected

| Axis | Used In | R11 Focus |
|------|---------|----------|
| Lifecycle emphasis (C-33: C2 RESULT semantically scoped as READ RECEIPT completeness check — verifies receipt fields (a)-(e) present, not PRE-COMMITMENT existence) | V-01, V-04, V-05 | C-33: C2 and C1 must be independently auditable at separate scopes; C2 checks receipt field list, not Phase B ledger content |
| Output format (C-34: F-01 typed IA-RESPONSE in per-role findings table — Type column with IA-RESPONSE designation on first finding; Description must contain IA verdict + role mechanism in the same entry) | V-02, V-04, V-05 | C-34: template typing elevates C-31 from rubric check to template invariant; F-01 absent or mis-typed fails the template regardless of finding content |
| Role sequence (C-35: READ RECEIPT block precedes C2 RESULT in per-role output — C2 RESULT structurally follows the receipt block, closing receipt-before-findings ordering from both directions) | V-03, V-04, V-05 | C-35: C2 cannot confirm receipt completeness if the receipt has not yet been written; the ordering is a structural compliance precondition, not a style preference |

**What changed from R8:**
- R8 V-05 C2 compliance block checked WORSE/BETTER row verbatim citations and a ledger row with Net direction — a Phase B ledger read check. This kept C1 and C2 scope-overlapping: both verified Phase B content, differing only in granularity. R11 V-01 separates the scopes. C1 is Phase B completeness (phase-level, once before Phase C). C2 is READ RECEIPT field completeness (per-role, after the receipt block is written). A C2 block that re-verifies Phase B content satisfies C-26 ordering but fails C-33 because neither block is independently auditable at its own scope without consulting the other.
- R8's findings tables had a Domain-Lens column but no Type column. F-01 could be any domain finding; the IA counterpoint was in the IA cost anchor block outside the findings table. R11 V-02 makes F-01 a typed IA-RESPONSE slot — the Type column must show IA-RESPONSE on the first row, and F-01's Description must contain both the IA's verdict/cost position and the role's disagreeing mechanism in the same entry. A findings table without a Type column fails C-34 even if C-31 is satisfied.
- R8 V-05's per-role structure was 3A (receipt) -> 3B (PRE-COMMITMENT) -> 3C (C2 + findings). C2 RESULT appeared in 3C, after the receipt in 3A — C-35's ordering was implicitly satisfied. R11 V-03 makes the ordering constraint explicit: the pipeline names C-35 as an exit condition and the per-role template declares READ RECEIPT -> C2 RESULT as a required sequence. Structural absence of the ordering declaration fails C-35 even if the output happens to be ordered correctly.
- V-04 integrates C-33 and C-35: C-35 makes C-33 auditable — C2 cannot confirm receipt completeness if the receipt has not been written; the ordering guarantee is the precondition for the semantic check.
- V-05 integrates all three: READ RECEIPT -> C2 RESULT (receipt field completeness) -> PRE-COMMITMENT (SEALED) -> findings table (F-01 IA-RESPONSE). Each mechanism is an independent template invariant, not a style preference.

---

## V-01 — Lifecycle Emphasis: C-33 C2 RESULT Scoped as READ RECEIPT Completeness

**Axis**: Lifecycle emphasis
**Hypothesis**: R8 V-05's C2 block verified WORSE/BETTER row verbatim citations and a named ledger row with Net direction — checking Phase B content. C1 also checks Phase B content (B1-B5 completeness). The overlap means C2 is not independently auditable from C1: both blocks verify Phase B, differing only in coverage. C-33 requires C2 to target receipt field completeness — confirming that all five required fields (a)-(e) are present in the receipt block for this role, not re-verifying Phase B. A C2 block whose declared verification target is "ledger citation present" or "WORSE/BETTER rows verbatim" satisfies C-26 ordering but fails C-33 because it is audited against Phase B content, not the receipt's field list. R11 V-01 replaces the C2 block content with a receipt field checklist: one row per field, each marked present or absent. C2 RESULT: SATISFIED means all five receipt fields are populated; C2 RESULT: UNSATISFIED names the specific missing field. No Phase B content is re-checked in C2.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline with three structural
compliance mechanisms active: string-matchable Budget verdict (C-25), named result tokens
(C-26), and PRE-COMMITMENT blocks (C-27). Read the full pipeline declaration before
producing any output.

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
            (B3) Budget verdict: three separate labeled lines --
                 line starting "WORSE rows:", line starting "BETTER rows:",
                 line starting "Conclusion:" -- each on its own line, independently
                 string-matchable [C-25]
            (B4) Budget strength declared as terminal field below separator
            (B5) IA verdict in cost terms
  Gates:    C-11, C-17, C-19, C-21, C-25

Phase C -- Technical Reviews
  Entry:    Two sub-conditions, each producing an exact result token [C-26]:
            C1 (Phase B exit pre-flight, phase-level):
              B1-B5 checklist, including B3 three-line scan.
              Terminal line: C1 RESULT: ALL CLEAR
              or             C1 RESULT: BLOCKED -- [B-number that failed]
            C2 (READ RECEIPT completeness, per-role) [C-33]:
              Each role writes a READ RECEIPT block (3A), then immediately outputs
              a C2 receipt field check block. C2 verifies that the receipt contains
              all five required fields (a)-(e). C2 does NOT re-check Phase B content
              -- that is C1's scope.
              Terminal line per role: C2 RESULT: SATISFIED
              or                     C2 RESULT: UNSATISFIED -- [field (x): missing]
  Exit:     C1 ends in ALL CLEAR; all C2 blocks end in SATISFIED; PRE-COMMITMENT
            blocks precede findings tables; all findings passed domain-lens gate
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26, C-27, C-33
```

---

**PHASE A -- ROUTE**

Entry: inputs loaded.

```
## Phase A: Routing

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern] |
| (all files) | default | Inertia Advocate | default -- always included |
```

Coverage gap: `COVERAGE GAP: [file] -- no org.yaml scope pattern covers this path.`

Phase A exit: complete.

---

**PHASE B -- INERTIA REVIEW**

Entry: Phase A exit met.

The Budget verdict appears as three separate labeled output lines below the separator.
Each line begins with its clause label. No clause appears inside a table cell or merged
with another clause on the same line.

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
[minimum 2]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS -- [one sentence in cost terms]      <- B5
```

Phase B exit: B1-B5 met; three Budget verdict lines present as separate output lines.

---

**PHASE C -- TECHNICAL REVIEWS**

**C1 -- Phase B Exit Pre-Flight [C-26/C1]:**

Output this block before the first role section. B3 check scans for all three Budget
verdict lines. C1's scope is Phase B completeness -- not per-role receipt content.

```
## Phase C Pre-Flight (C1)

[ ] B1 -- Null hypothesis stated
[ ] B2 -- Cost ledger: 4 rows x 2 columns x Net direction per row filled
[ ] B3 -- Budget verdict: three labeled lines present as separate output lines
         Scan: "WORSE rows:" on own line? [yes/no]
               "BETTER rows:" on own line? [yes/no]
               "Conclusion:" on own line? [yes/no]
         All three must be yes.
[ ] B4 -- Budget strength terminal field below separator
[ ] B5 -- IA verdict in cost terms

C1 RESULT: ALL CLEAR
```

If any box unchecked: `C1 RESULT: BLOCKED -- [B-number and what failed]`

C1 checks Phase B completeness. A passing C1 does not confirm any role's READ RECEIPT.

**Per-Role Structure -- 3A -> 3B -> 3C:**

For each role: security/compliance -> domain-specific -> PM/TPM.

**3A -- IA READ RECEIPT:**

Write immediately after reading Phase B. Fill every field accurately. Do not use
placeholder text. The receipt is an output artifact: a reviewer must be able to audit
all five fields post-hoc from the text.

```
## IA READ RECEIPT -- [Role Name]

(a) Section read:        Phase B -- Inertia Advocate
(b) Budget verdict:
      WORSE rows:        [restate Phase B "WORSE rows:" line verbatim]
      BETTER rows:       [restate Phase B "BETTER rows:" line verbatim]
      Conclusion:        [restate Phase B "Conclusion:" line accurately]
(c) Budget strength:     HIGH / MEDIUM / LOW [from Phase B terminal field]
(d) Ledger row:          [Maintenance / Incident exposure / Integration cost / Regression risk
                         -- the row most relevant to this role's domain]
(e) Initial position:    [CONFIRMS / DISPUTES] Net direction on [row (d)]
                         [one phrase -- based on domain knowledge and Phase B ledger;
                          no PR diff content yet]
```

**3B -- C2 RECEIPT FIELD CHECK [C-33, C-26/C2]:**

C2's scope is READ RECEIPT field completeness -- not Phase B ledger content. Output
this block immediately after 3A. Check whether each of the five receipt fields is
populated. A field is present if it contains substantive content -- not a placeholder.
Field (e) may appear as a cross-reference to a PRE-COMMITMENT block if C-27 is active.

```
## C2 Receipt Check -- [Role Name]

(a) Section read:        present / absent
(b) Budget verdict:      present / absent -- [note if Conclusion uses placeholder]
(c) Budget strength:     present / absent
(d) Ledger row named:    present / absent
(e) Initial position:    present / absent -- [also valid: cross-reference to PRE-COMMITMENT block]

C2 RESULT: SATISFIED
```

If any field is absent or contains placeholder text:
`C2 RESULT: UNSATISFIED -- [field (x): what is missing or placeholder]`

C2 RESULT: SATISFIED confirms the receipt is a complete output artifact. It does NOT
confirm that Phase B was re-read, that WORSE/BETTER rows were cited verbatim, or that
any PRE-COMMITMENT block was produced. Those are C1's scope or separate criteria.

**3C -- PRE-COMMITMENT (written after 3B, before reading diff for findings) [C-27]:**

The PRE-COMMITMENT block is a distinct named element following the C2 check and
preceding the findings table. Write it now, before examining the PR diff for findings.

```
PRE-COMMITMENT: [Role Name]

Cost row assessed:  [Maintenance / Incident exposure / Integration cost / Regression risk]
                    [same as receipt field (d)]
Initial position:   [CONFIRMS / DISPUTES] [Net direction from Phase B] on [Cost row]
                    [one phrase -- domain knowledge and Phase B cost ledger only]
Basis:              Domain knowledge only. PR diff not yet examined.
                    [one sentence naming the code surface or architectural pattern
                     this role expects to be relevant -- must name a code artifact]

[PRE-COMMITMENT SEALED]
```

The SEALED token closes the block. No PRE-COMMITMENT content is revised after findings.

**3D -- FINDINGS:**

Now examine the PR diff. Apply the domain-lens gate per finding:

```
Step A: "Would only [this role] raise this finding, given their domain?"
  YES -> domain-loaded. Include.
  NO  -> Step B.
Step B: Revise to name a specific mechanism owned by this role's domain.
  Re-execute Step A. Still NO -> drop.
```

Then write findings and post-commitment delta:

```
## Phase C: [Role Name]

Source files:  [from Phase A routing]
Orientation:   [one phrase from .craft/roles/]

[READ RECEIPT -- 3A above]
[C2 RECEIPT CHECK -- 3B above]
[PRE-COMMITMENT -- 3C above]

Findings: [all passed domain-lens gate]

| ID | Severity | Finding | Domain-Lens | Owner | Resolution |
|----|----------|---------|-------------|-------|------------|
| F-01 | P1/P2/P3 | [IA found X; [role] rates P-N because [mechanism]] | Passed | [role] | [action] |
| F-02 | P1/P2/P3 | [domain finding] | Passed | [role] | [action] |
[minimum 2]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3

Post-commitment delta:
  Pre-committed:   [CONFIRMS / DISPUTES] [Cost row] (from PRE-COMMITMENT block)
  After findings:  [HELD / CHANGED]
  If HELD:         [name code artifact from diff that confirmed the position]
  If CHANGED:      [name code artifact that changed it; state revised position]
```

Phase C exit: C1 ALL CLEAR (Phase B scope); every C2 SATISFIED (receipt field scope);
PRE-COMMITMENT blocks precede findings tables; all findings passed domain-lens gate.

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
  Mechanism: [structural or architectural property of the code causing the difference]

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
2. [additional condition] -- sign-off: [role]
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

## V-02 -- Output Format: C-34 F-01 Typed IA-RESPONSE in Findings Table

**Axis**: Output format
**Hypothesis**: R8 V-05's findings table had ID, Severity, Finding, Domain-Lens, Owner, Resolution columns. The IA counterpoint was surfaced in the IA cost anchor block -- a section-level element outside the findings table. This meant C-31 (IA counterpoint in a specific finding's body text) could be satisfied by placing the reference anywhere in a finding's description, but there was no template-level invariant forcing it into F-01. A role section could write the IA counterpoint in F-03 or any finding and satisfy C-31. C-34 closes this by designating F-01 as a typed slot: the findings table must include a Type column, F-01's Type cell must contain "IA-RESPONSE," and F-01's Description must contain the IA's verdict/cost position and the role's disagreeing mechanism in the same entry. A table with no Type column fails C-34. An F-01 with Type=DOMAIN fails C-34. An F-01 with Type=IA-RESPONSE but a Description that names only a domain finding without the IA position fails C-34. The type designation is what makes IA counterpoint placement structurally non-optional -- the template cannot be filled without it.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline with three structural
compliance mechanisms active: string-matchable Budget verdict (C-25), named result tokens
(C-26), and PRE-COMMITMENT blocks (C-27). Read the full pipeline declaration before
producing any output.

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
            (B3) Budget verdict: three separate labeled lines --
                 "WORSE rows: [values]" on its own line,
                 "BETTER rows: [values]" on its own line,
                 "Conclusion: [text]" on its own line [C-25]
            (B4) Budget strength declared as terminal field below separator
            (B5) IA verdict in cost terms
  Gates:    C-11, C-17, C-19, C-21, C-25

Phase C -- Technical Reviews
  Entry:    Two sub-conditions, each producing an exact result token [C-26]:
            C1 (Phase B exit pre-flight):
              B1-B5 checklist. Terminal: C1 RESULT: ALL CLEAR
              or C1 RESULT: BLOCKED -- [B-number]
            C2 (IA read prerequisite, per-role):
              Each role cites WORSE/BETTER rows verbatim from Phase B and names
              ledger row + Net direction. Terminal: C2 RESULT: SATISFIED
              or C2 RESULT: UNSATISFIED -- [what is missing]
  Exit:     C1 ends in ALL CLEAR; all C2 blocks end in SATISFIED; PRE-COMMITMENT
            blocks precede findings tables; F-01 in every findings table typed
            IA-RESPONSE [C-34]; all findings passed domain-lens gate
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26, C-27, C-34
```

---

**PHASE A -- ROUTE**

Entry: inputs loaded.

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
F-02 [P1/P2/P3] [second argument]
     Owner: [role] | Resolution: [action]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS -- [one sentence in cost terms]      <- B5
```

Phase B exit: B1-B5 met; three Budget verdict lines present as separate output lines.

---

**PHASE C -- TECHNICAL REVIEWS**

**C1 -- Phase B Exit Pre-Flight [C-26/C1]:**

```
## Phase C Pre-Flight (C1)

[ ] B1 -- Null hypothesis stated
[ ] B2 -- Cost ledger: 4 rows x 2 columns x Net direction per row filled
[ ] B3 -- Budget verdict: three labeled lines present
         Scan: "WORSE rows:" on own line? [yes/no]
               "BETTER rows:" on own line? [yes/no]
               "Conclusion:" on own line? [yes/no]
         All three must be yes.
[ ] B4 -- Budget strength terminal field
[ ] B5 -- IA verdict in cost terms

C1 RESULT: ALL CLEAR
```

If any box unchecked: `C1 RESULT: BLOCKED -- [B-number and what failed]`

**Per-Role Structure -- 3A -> 3B -> 3C:**

Sequence: security/compliance -> domain-specific -> PM/TPM.

**3A -- IA READ RECEIPT:**

```
## IA READ RECEIPT -- [Role Name]

Section read:     Phase B -- Inertia Advocate
WORSE rows:       [restate Phase B "WORSE rows:" line verbatim]
BETTER rows:      [restate Phase B "BETTER rows:" line verbatim]
Conclusion:       [restate Phase B "Conclusion:" line accurately]
Budget strength:  HIGH / MEDIUM / LOW [from Phase B terminal field]
```

**3B -- C2 COMPLIANCE BLOCK [C-26/C2]:**

```
## C2 Compliance -- [Role Name]

WORSE rows cited:    [copy verbatim from Phase B "WORSE rows:" line]
BETTER rows cited:   [copy verbatim from Phase B "BETTER rows:" line]
Budget strength:     [HIGH / MEDIUM / LOW -- from Phase B]
Ledger row cited:    [same row as PRE-COMMITMENT block]
Net direction:       [WORSE / BETTER / NEUTRAL -- from Phase B table]

C2 RESULT: SATISFIED
```

If citation absent or row/Net direction missing:
`C2 RESULT: UNSATISFIED -- [WORSE rows / BETTER rows / ledger row / Net direction: what is missing]`

**3C -- PRE-COMMITMENT (before reading diff) [C-27]:**

```
PRE-COMMITMENT: [Role Name]

Cost row assessed:  [Maintenance / Incident exposure / Integration cost / Regression risk]
Initial position:   [CONFIRMS / DISPUTES] [Net direction from Phase B] on [Cost row]
                    [one phrase -- domain knowledge and Phase B cost ledger only]
Basis:              Domain knowledge only. PR diff not yet examined.
                    [one sentence naming the code surface or architectural pattern]

[PRE-COMMITMENT SEALED]
```

**3D -- FINDINGS [C-34]:**

Apply domain-lens gate per finding:

```
Step A: "Would only [this role] raise this finding, given their domain?"
  YES -> include. NO -> Step B.
Step B: Revise to name domain-owned mechanism. Re-execute Step A.
  Still NO -> drop.
```

The findings table MUST include a Type column. F-01 MUST have Type = IA-RESPONSE.
The IA-RESPONSE type designation is required in the Type cell -- not in prose below the
table. F-01's Description must name both the IA's verdict/cost position and this role's
disagreeing code mechanism in the same entry. A findings table without a Type column
fails C-34. An F-01 row with Type = DOMAIN or any other type fails C-34. An F-01 row
with an empty Type cell fails C-34. Subsequent findings use Type = DOMAIN.

```
## Phase C: [Role Name]

Source files:  [from Phase A routing]
Orientation:   [one phrase from .craft/roles/]

[READ RECEIPT -- 3A above]
[C2 COMPLIANCE -- 3B above]
[PRE-COMMITMENT -- 3C above]

Findings: [all passed domain-lens gate]

| ID | Type | Severity | Description | Domain-Lens | Owner | Resolution |
|----|------|----------|-------------|-------------|-------|------------|
| F-01 | IA-RESPONSE | P1/P2/P3 | IA found [verdict/cost position]; [role] rates [P-N] because [specific mechanism in this role's domain -- names code artifact] | Passed | [role] | [action] |
| F-02 | DOMAIN | P1/P2/P3 | [domain finding] | Passed | [role] | [action] |
[minimum 2]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3

Post-commitment delta:
  Pre-committed:   [CONFIRMS / DISPUTES] [Cost row] (from PRE-COMMITMENT block)
  After findings:  [HELD / CHANGED]
  If HELD:         [name code artifact from diff that confirmed the position]
  If CHANGED:      [name code artifact that changed it; state revised position]
```

F-01 IA-RESPONSE format rules:
- Type cell: exactly "IA-RESPONSE" -- no other value passes
- Description: "[IA found X; [role] rates P-N because Y]" where X is the IA verdict or
  cost position (named from the cost ledger or IA verdict line) and Y is the code
  mechanism within this role's domain
- A description that names only a domain finding without the IA position fails C-34
- A description that names only the IA position without the role's disagreeing mechanism
  fails C-34
- Both must appear in the same Description cell

Phase C exit: C1 ALL CLEAR; every C2 SATISFIED; PRE-COMMITMENT before findings;
F-01 Type=IA-RESPONSE in every findings table; all findings passed domain-lens gate.

---

**PHASE D -- SYNTHESIS**

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

---

**PHASE E -- DECISION**

```
## Phase E: Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from role] -- [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] -- sign-off: [role who confirms before merge]
```

One decision. Delegated decisions fail.

---

**AMEND**

Before Phase A if AMEND directive received:

```
## AMEND SCOPE

What was amended:           [description]
Roles added:                [list, or "none"]
Roles removed:              [list, or "none"]
Files triggering addition:  [list, or "n/a -- manually directed"]
Prior findings superseded:  [F-IDs, or "none -- first run"]
```

---

## V-03 -- Role Sequence: C-35 READ RECEIPT Precedes C2 RESULT in Per-Role Output

**Axis**: Role sequence
**Hypothesis**: R8 V-05's per-role structure was 3A (receipt) -> 3B (PRE-COMMITMENT) -> 3C (C2 + findings). The C2 RESULT appeared after the receipt in 3A, implicitly satisfying C-35. But the pipeline declaration did not name C-35 as an exit condition, and the per-role template showed C2 RESULT inside the "3C" step without explicitly constraining its position relative to the receipt. A variation that places the C2 compliance block before the receipt (e.g., outputs headers and C2 block first, then receipt) would satisfy C-26 ordering requirements while failing C-35. The implicit ordering is not a declared invariant. R11 V-03 makes the ordering explicit: (1) the pipeline Phase C exit conditions name "READ RECEIPT precedes C2 RESULT per role" as a named compliance item; (2) the per-role template shows the sequence as labeled steps with explicit step ordering (step 1: receipt, step 2: C2 RESULT). A per-role output where C2 RESULT precedes the receipt is a visible template violation detectable by scanning for the receipt header and C2 RESULT line in output order.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline with four structural
compliance mechanisms active: string-matchable Budget verdict (C-25), named result tokens
(C-26), PRE-COMMITMENT blocks (C-27), and READ RECEIPT before C2 RESULT ordering (C-35).
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
            (B4) Budget strength declared as terminal field
            (B5) IA verdict in cost terms
  Gates:    C-11, C-17, C-19, C-21, C-25

Phase C -- Technical Reviews
  Entry:    Two sub-conditions, each producing an exact result token [C-26]:
            C1 (Phase B exit pre-flight):
              B1-B5 checklist. Terminal: C1 RESULT: ALL CLEAR
              or C1 RESULT: BLOCKED -- [B-number]
            C2 (per-role IA read prerequisite):
              Each role cites WORSE/BETTER rows verbatim, ledger row, Net direction.
              Terminal: C2 RESULT: SATISFIED
              or C2 RESULT: UNSATISFIED -- [what is missing]
  Exit:     C1 ends in ALL CLEAR; all C2 blocks end in SATISFIED;
            READ RECEIPT appears before C2 RESULT in the output for every role [C-35];
            PRE-COMMITMENT blocks precede findings tables; all findings passed
            domain-lens gate
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26, C-27, C-35

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

Entry: inputs loaded.

```
## Phase A: Routing

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern] |
| (all files) | default | Inertia Advocate | default -- always included |
```

Coverage gap: `COVERAGE GAP: [file] -- no org.yaml scope pattern covers this path.`

Phase A exit: complete.

---

**PHASE B -- INERTIA REVIEW**

Entry: Phase A exit met.

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
WORSE rows: [Cost Categories where Net = WORSE, or "none"]               <- B3 line 1
BETTER rows: [Cost Categories where Net = BETTER, or "none"]             <- B3 line 2
Conclusion: [one sentence -- is adoption justified?]                     <- B3 line 3

Budget strength: HIGH / MEDIUM / LOW                                      <- B4

Findings:
F-01 [P1/P2/P3] [argument current state is sufficient]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second argument]
     Owner: [role] | Resolution: [action]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS -- [one sentence in cost terms]      <- B5
```

Phase B exit: B1-B5 met; three labeled Budget verdict lines present.

---

**PHASE C -- TECHNICAL REVIEWS**

**C1 -- Phase B Exit Pre-Flight [C-26/C1]:**

```
## Phase C Pre-Flight (C1)

[ ] B1 -- Null hypothesis stated
[ ] B2 -- Cost ledger: 4 rows x 2 columns x Net direction per row filled
[ ] B3 -- Budget verdict: three separate labeled lines
         (scan "WORSE rows:", "BETTER rows:", "Conclusion:" each on own line)
[ ] B4 -- Budget strength terminal field below separator
[ ] B5 -- IA verdict in cost terms

C1 RESULT: ALL CLEAR
```

If any box unchecked: `C1 RESULT: BLOCKED -- [B-number and what failed]`

**Per-Role Structure -- ordered steps (C-35 compliance requires step 1 before step 2):**

Sequence across roles: security/compliance -> domain-specific -> PM/TPM.

For each role, output STEP 1, then STEP 2, then STEP 3, then STEP 4. No step may be
reordered. STEP 2 (C2 RESULT) must appear in the output AFTER STEP 1 (READ RECEIPT).
A C2 RESULT line that appears before the READ RECEIPT block for that role is a C-35
violation detectable by scanning the output top-to-bottom for each role section.

**STEP 1 -- IA READ RECEIPT [must appear before STEP 2]:**

```
## IA READ RECEIPT -- [Role Name]

Section read:     Phase B -- Inertia Advocate
WORSE rows:       [restate Phase B "WORSE rows:" line verbatim]
BETTER rows:      [restate Phase B "BETTER rows:" line verbatim]
Conclusion:       [restate Phase B "Conclusion:" line accurately]
Budget strength:  HIGH / MEDIUM / LOW [from Phase B terminal field]
```

The READ RECEIPT block must be present in the output before STEP 2 begins. A role
section that begins STEP 2 before completing STEP 1 fails C-35 for that role.

**STEP 2 -- C2 COMPLIANCE BLOCK [C2 RESULT must follow STEP 1 in output] [C-26/C2, C-35]:**

```
## C2 Compliance -- [Role Name]

WORSE rows cited:    [copy verbatim from Phase B "WORSE rows:" line]
BETTER rows cited:   [copy verbatim from Phase B "BETTER rows:" line]
Budget strength:     [HIGH / MEDIUM / LOW -- from Phase B]
Ledger row cited:    [Maintenance / Incident exposure / Integration cost / Regression risk]
Net direction:       [WORSE / BETTER / NEUTRAL -- from Phase B table]

C2 RESULT: SATISFIED
```

C-35 compliance check: scan the output text for this role. Locate the READ RECEIPT
block header ("## IA READ RECEIPT -- [Role Name]"). Locate the C2 RESULT line. If
the C2 RESULT line appears before the READ RECEIPT header, C-35 fails for this role.
If no READ RECEIPT header precedes the C2 RESULT line, C-35 fails.

If citation absent: `C2 RESULT: UNSATISFIED -- [specify what is missing]`

**STEP 3 -- PRE-COMMITMENT (before reading diff for findings) [C-27]:**

```
PRE-COMMITMENT: [Role Name]

Cost row assessed:  [Maintenance / Incident exposure / Integration cost / Regression risk]
Initial position:   [CONFIRMS / DISPUTES] [Net direction] on [Cost row]
                    [one phrase -- domain knowledge and Phase B ledger only]
Basis:              Domain knowledge only. PR diff not yet examined.
                    [one sentence naming the code surface or architectural pattern]

[PRE-COMMITMENT SEALED]
```

**STEP 4 -- FINDINGS:**

Apply domain-lens gate per finding:

```
Step A: "Would only [this role] raise this finding, given their domain?"
  YES -> include. NO -> Step B.
Step B: Revise to name domain-owned mechanism. Re-execute Step A.
  Still NO -> drop.
```

```
## Phase C: [Role Name]

Source files:  [from Phase A routing]
Orientation:   [one phrase from .craft/roles/]

[STEP 1: READ RECEIPT above]
[STEP 2: C2 COMPLIANCE above -- C2 RESULT must follow READ RECEIPT in output]
[STEP 3: PRE-COMMITMENT above]

Findings: [all passed domain-lens gate]

| ID | Severity | Finding | Domain-Lens | Owner | Resolution |
|----|----------|---------|-------------|-------|------------|
| F-01 | P1/P2/P3 | [IA found X; [role] rates P-N because [mechanism]] | Passed | [role] | [action] |
| F-02 | P1/P2/P3 | [domain finding] | Passed | [role] | [action] |
[minimum 2]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3

Post-commitment delta:
  Pre-committed:   [CONFIRMS / DISPUTES] [Cost row]
  After findings:  [HELD / CHANGED]
  If HELD:         [code artifact from diff that confirmed the position]
  If CHANGED:      [code artifact that changed it; revised position]
```

Phase C exit: C1 ALL CLEAR; every C2 SATISFIED; READ RECEIPT precedes C2 RESULT per
role in the output text [C-35]; PRE-COMMITMENT before findings; all findings passed
domain-lens gate.

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
| "from [role]'s perspective" as sole cause | name the architectural fact |
| "their roles lead them to different conclusions" | "[role-A]'s scope includes [surface X]; [role-B]'s does not" |

Phase D exit: all Mechanism lines pass.

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

One decision. Delegated decisions fail.

---

**AMEND**

Before Phase A if AMEND directive received:

```
## AMEND SCOPE

What was amended:           [description]
Roles added:                [list, or "none"]
Roles removed:              [list, or "none"]
Files triggering addition:  [list, or "n/a -- manually directed"]
Prior findings superseded:  [F-IDs, or "none -- first run"]
```

---

## V-04 -- Combination: C-33 + C-35 (Receipt Completeness + Ordering Enforcement)

**Axis**: Lifecycle emphasis + Role sequence
**Hypothesis**: V-01 changed C2's verification target from Phase B ledger content to READ RECEIPT field completeness (C-33). V-03 made the receipt-before-C2-RESULT ordering an explicit pipeline invariant (C-35). The integration argument: C-35 is the structural precondition for C-33. C2 can only confirm receipt field completeness if the receipt exists when C2 RESULT is written -- an ordering violation (C2 RESULT before receipt) makes C2 RESULT a forward assertion about content that has not yet appeared, which is neither auditable nor meaningful. The two criteria are causally linked: C-35's ordering guarantee is what makes C-33's completeness check independently verifiable. V-04 wires them in the pipeline declaration as complementary Phase C exit conditions: "READ RECEIPT precedes C2 RESULT in the output" and "C2 RESULT verifies receipt fields (a)-(e) complete." The C2 block template is the receipt field checklist from V-01. The per-role template explicitly labels the required step sequence from V-03.

---

You are running `/corps-pr`. This skill runs as a five-phase pipeline. Four structural
compliance mechanisms are active: string-matchable Budget verdict (C-25), named result
tokens (C-26), PRE-COMMITMENT blocks (C-27), and the receipt-completeness / ordering
pair (C-33 + C-35). Read the full pipeline declaration before producing any output.

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
            (B3) Budget verdict: three separate labeled lines --
                 "WORSE rows: [values]" / "BETTER rows: [values]" / "Conclusion: [text]"
                 each on its own output line [C-25]
            (B4) Budget strength declared as terminal field below separator
            (B5) IA verdict in cost terms
  Gates:    C-11, C-17, C-19, C-21, C-25

Phase C -- Technical Reviews
  Entry:    Two sub-conditions [C-26]:
            C1 (Phase B exit pre-flight, phase-level):
              B1-B5 checklist. Scope: Phase B completeness only.
              Terminal: C1 RESULT: ALL CLEAR
              or C1 RESULT: BLOCKED -- [B-number]
            C2 (READ RECEIPT field completeness, per-role) [C-33]:
              Scope: READ RECEIPT fields (a)-(e) complete. Does NOT re-check Phase B.
              C2 RESULT must appear after the READ RECEIPT block in the output [C-35].
              Terminal: C2 RESULT: SATISFIED
              or C2 RESULT: UNSATISFIED -- [field (x): missing]
  Exit:     C1 ends in ALL CLEAR; all C2 blocks end in SATISFIED;
            READ RECEIPT precedes C2 RESULT per role in the output text [C-35];
            C2 verified receipt field completeness, not Phase B re-read [C-33];
            PRE-COMMITMENT blocks precede findings tables;
            all findings passed domain-lens gate
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26, C-27, C-33, C-35

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
F-02 [P1/P2/P3] [second argument]
     Owner: [role] | Resolution: [action]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS -- [one sentence in cost terms]      <- B5
```

Phase B exit: B1-B5 met.

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

**STEP 2 -- C2 RECEIPT FIELD CHECK [C-33, C-26/C2, must follow STEP 1 in output] [C-35]:**

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

C-35 check: the READ RECEIPT block header must appear above this C2 RESULT line in the
output text for this role. A C2 RESULT: SATISFIED that precedes the receipt block header
fails C-35 for this role.

C-33 check: each checklist line in this block addresses a receipt field, not Phase B
content. Replacing any checklist line with "WORSE rows verbatim cited: yes" would violate
C-33 -- that is a Phase B check (C1 scope), not a receipt field check.

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

**STEP 4 -- FINDINGS:**

```
Step A: "Would only [this role] raise this finding, given their domain?"
  YES -> include. NO -> Step B.
Step B: Revise to name domain-owned mechanism. Still NO -> drop.
```

```
## Phase C: [Role Name]

Source files:  [from Phase A routing]
Orientation:   [one phrase from .craft/roles/]

[STEP 1: READ RECEIPT]
[STEP 2: C2 RECEIPT CHECK -- C2 RESULT follows receipt block per C-35]
[STEP 3: PRE-COMMITMENT]

Findings:

| ID | Severity | Finding | Domain-Lens | Owner | Resolution |
|----|----------|---------|-------------|-------|------------|
| F-01 | P1/P2/P3 | [IA found X; [role] rates P-N because [mechanism]] | Passed | [role] | [action] |
| F-02 | P1/P2/P3 | [domain finding] | Passed | [role] | [action] |
[minimum 2]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3

Post-commitment delta:
  Pre-committed:   [CONFIRMS / DISPUTES] [Cost row]
  After findings:  [HELD / CHANGED]
  If HELD:         [code artifact from diff that confirmed the position]
  If CHANGED:      [code artifact that changed it; revised position]
```

Phase C exit: C1 ALL CLEAR (Phase B scope); every C2 SATISFIED (receipt scope, post-receipt
in output per C-35); PRE-COMMITMENT before findings; all findings passed gate.

---

**PHASE D -- SYNTHESIS**

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
| "from [role]'s perspective" as sole cause | name the architectural fact |
| "their roles lead them to different conclusions" | "[role-A]'s scope includes [surface X]; [role-B]'s does not" |

---

**PHASE E -- DECISION**

```
## Phase E: Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from role] -- [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] -- sign-off: [role who confirms before merge]
```

One decision. Delegated decisions fail.

---

**AMEND**

```
## AMEND SCOPE

What was amended:           [description]
Roles added:                [list, or "none"]
Roles removed:              [list, or "none"]
Files triggering addition:  [list, or "n/a -- manually directed"]
Prior findings superseded:  [F-IDs, or "none -- first run"]
```

---

## V-05 -- Full R11 Integration: C-33 + C-34 + C-35

**Axis**: Lifecycle emphasis + Output format + Role sequence
**Hypothesis**: V-01 (C-33), V-02 (C-34), and V-03 (C-35) each address one structural gap. V-04 showed that C-33 and C-35 are causally linked: C-35's ordering guarantee is the precondition for C-33's completeness check. V-05 adds C-34 to the integrated chain. The per-role output sequence is now a four-step invariant: (1) READ RECEIPT -- containing fields (a)-(e); (2) C2 RECEIPT CHECK -- confirming receipt field completeness (C-33), appearing after the receipt (C-35); (3) PRE-COMMITMENT -- SEALED before diff analysis; (4) Findings table -- F-01 typed IA-RESPONSE with IA verdict + role mechanism in the same Description entry (C-34). The three mechanisms are independent but non-overlapping: C-35 enforces output text ordering; C-33 enforces C2 semantic scope; C-34 enforces findings template typing. A variation that satisfies two of the three -- for example, receipt-before-C2-RESULT and receipt completeness check, but F-01 untyped -- passes C-33 and C-35 but fails C-34 because the IA counterpoint is not a template invariant. All three must be active simultaneously.

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
            (B4) Budget strength terminal field below separator
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
            (6) F-01 in every findings table: Type = IA-RESPONSE, Description contains
                IA verdict/cost position AND role mechanism in the same entry [C-34]
            (7) All findings passed domain-lens gate
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26, C-27, C-33, C-34, C-35

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
[minimum 2]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS -- [one sentence in cost terms]      <- B5
```

Phase B exit: B1-B5 met; three labeled Budget verdict lines present as separate output lines.

---

**PHASE C -- TECHNICAL REVIEWS**

Phase C uses five structural mechanisms: C1 pre-flight (C-26/C1), READ RECEIPT (C-23),
C2 receipt field check (C-26/C2, C-33), ordering constraint (C-35), PRE-COMMITMENT (C-27),
and F-01 IA-RESPONSE template typing (C-34).

**C1 -- Phase B Exit Pre-Flight [C-26/C1, scope: Phase B completeness]:**

Output this block before the first role section. C1 scope is Phase B. C1 RESULT does
not verify any role's receipt content.

```
## Phase C Pre-Flight (C1)

[ ] B1 -- Null hypothesis stated
[ ] B2 -- Cost ledger: 4 rows x 2 columns x Net direction per row filled
[ ] B3 -- Budget verdict: three labeled lines present as separate output lines
         "WORSE rows:" on own line? [yes/no]
         "BETTER rows:" on own line? [yes/no]
         "Conclusion:" on own line? [yes/no]
         All three must be yes.
[ ] B4 -- Budget strength terminal field below separator
[ ] B5 -- IA verdict in cost terms

C1 RESULT: ALL CLEAR
```

If any box unchecked: `C1 RESULT: BLOCKED -- [B-number and what failed]`

Phase C cannot advance until C1 RESULT: ALL CLEAR appears in the output.

**Per-Role Output Sequence -- four mandatory steps in output order:**

Sequence across roles: security/compliance -> domain-specific -> PM/TPM.

For each role, output STEP 1, then STEP 2, then STEP 3, then STEP 4.
The order is a structural invariant, not a preference. STEP 2 (C2 RESULT) must
follow STEP 1 (READ RECEIPT) in the output text. STEP 3 (PRE-COMMITMENT) must be
SEALED before any diff content appears in STEP 4 (Findings).

**STEP 1 -- IA READ RECEIPT [must appear in output before STEP 2] [C-23]:**

```
## IA READ RECEIPT -- [Role Name]

(a) Section read:        Phase B -- Inertia Advocate
(b) Budget verdict:
      WORSE rows:        [restate Phase B "WORSE rows:" line verbatim]
      BETTER rows:       [restate Phase B "BETTER rows:" line verbatim]
      Conclusion:        [restate Phase B "Conclusion:" line accurately]
(c) Budget strength:     HIGH / MEDIUM / LOW [from Phase B terminal field]
(d) Ledger row:          [Maintenance / Incident exposure / Integration cost / Regression risk
                         -- the row most relevant to this role's domain]
(e) Initial position:    [CONFIRMS / DISPUTES] Net direction on [row (d)]
                         [one phrase -- domain knowledge and Phase B ledger only; or:
                          "see PRE-COMMITMENT block below: (d) [row name], (e) committed below"]
```

Field (e) may be a forward cross-reference to the PRE-COMMITMENT block in STEP 3
("see PRE-COMMITMENT block below"). The cross-reference must name the row and indicate
the position is committed in the named block. A receipt where (e) is entirely absent
with no cross-reference fails C-23 and will fail C2 in STEP 2.

**STEP 2 -- C2 RECEIPT FIELD CHECK [C-33, C-26/C2] [must follow STEP 1 in output] [C-35]:**

C2 scope: READ RECEIPT field completeness. C2 confirms that the receipt written in STEP 1
contains all five required fields. C2 does NOT re-verify Phase B budget content -- that is
C1's scope. Replacing a receipt field check with "WORSE rows verbatim cited: yes" would be
a C-33 violation even if C2 RESULT: SATISFIED is output.

```
## C2 Receipt Check -- [Role Name]

(a) Section read named:    present / absent
(b) Budget verdict:        present / absent
    (three sub-lines present -- WORSE rows, BETTER rows, Conclusion -- no placeholder text)
(c) Budget strength:       present / absent
(d) Ledger row named:      present / absent
(e) Initial position:      present / absent
    (valid: (i) stated inline in the receipt, or
            (ii) explicit cross-reference to PRE-COMMITMENT block by label name)

C2 RESULT: SATISFIED
```

C-35 verification: this C2 RESULT line appears in the output AFTER the READ RECEIPT block
header ("## IA READ RECEIPT -- [Role Name]") for this role. A C2 RESULT line that precedes
the receipt block header fails C-35 for this role regardless of the C2 content.

C-33 verification: every checklist line targets a receipt field (a)-(e). A C2 block where
any checklist line re-checks a Phase B field (e.g., "WORSE rows verbatim cited" instead of
"(b) Budget verdict: present") fails C-33 -- the verification scope is wrong.

If any receipt field is absent or uses placeholder text:
`C2 RESULT: UNSATISFIED -- [field (x): missing or placeholder text found]`

**STEP 3 -- PRE-COMMITMENT [C-27, C-29, written before reading diff for findings]:**

The PRE-COMMITMENT block is a distinct named element. It follows STEP 2 and precedes the
findings table. Write it before examining the PR diff for this role's findings.

```
PRE-COMMITMENT: [Role Name]

Cost row assessed:  [Maintenance / Incident exposure / Integration cost / Regression risk]
                    [same row as receipt field (d)]
Initial position:   [CONFIRMS / DISPUTES] [Net direction from Phase B] on [Cost row]
                    [one phrase -- domain knowledge + Phase B cost ledger; diff not yet read]
Basis:              Domain knowledge only. PR diff not yet examined.
                    [one sentence naming the code surface or architectural pattern this role
                     expects to be relevant -- must name a code artifact, not a process concern]

[PRE-COMMITMENT SEALED]
```

The SEALED token closes the block. No content in the PRE-COMMITMENT block is revised after
findings are generated. The token's position in the output text is the timing claim.

**STEP 4 -- FINDINGS TABLE [C-34: F-01 typed IA-RESPONSE] [C-24: Domain-Lens column]:**

Now examine the PR diff. Apply the domain-lens gate per finding:

```
Step A: "Would only [this role] raise this finding, given their domain?"
  YES -> domain-loaded. Include.
  NO  -> Go to Step B.
Step B: Revise to name a specific mechanism owned by this role's domain -- unreachable
  without it. Re-execute Step A. Still NO -> drop.
```

The findings table MUST include a Type column and a Domain-Lens column.

F-01 template typing rules:
- F-01 Type cell: exactly "IA-RESPONSE" -- no other value, no blank
- F-01 Description: "[IA found [verdict/cost position from Phase B]; [role] rates [P-N]
  because [code mechanism in this role's domain -- names a specific code artifact]]"
- Both the IA position and the role's disagreeing mechanism must appear in the same
  Description cell. A Description with only the IA position fails C-34. A Description
  with only the domain mechanism fails C-34.
- F-01 is a required slot. A findings table where F-01 is absent fails C-34.
- Subsequent findings use Type = DOMAIN (or appropriate type label).

```
## Phase C: [Role Name]

Source files:  [from Phase A routing]
Orientation:   [one phrase from .craft/roles/]

[STEP 1: READ RECEIPT above]
[STEP 2: C2 RECEIPT CHECK above -- C2 RESULT follows READ RECEIPT per C-35]
[STEP 3: PRE-COMMITMENT above -- SEALED before diff content]

Findings: [all passed domain-lens gate]

| ID | Type | Severity | Description | Domain-Lens | Owner | Resolution |
|----|------|----------|-------------|-------------|-------|------------|
| F-01 | IA-RESPONSE | P1/P2/P3 | IA found [verdict/cost position]; [role] rates [P-N] because [specific code mechanism in this role's domain] | Passed | [role] | [action] |
| F-02 | DOMAIN | P1/P2/P3 | [domain finding -- names mechanism unreachable without this role] | Passed | [role] | [action] |
[minimum 2 findings total]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3

Post-commitment delta:
  Pre-committed:   [CONFIRMS / DISPUTES] [Cost row] (from PRE-COMMITMENT block above)
  After findings:  [HELD / CHANGED]
  If HELD:         [name the code artifact from the diff that confirmed the position]
  If CHANGED:      [name the code artifact that changed it; state the revised position]
```

Phase C exit conditions (all must be satisfied):
1. C1 RESULT: ALL CLEAR in the output (Phase B completeness, phase-level)
2. Every C2 RESULT: SATISFIED in the output (receipt field completeness, per-role) [C-33]
3. Each READ RECEIPT block header precedes the C2 RESULT line for that role [C-35]
4. Each PRE-COMMITMENT block carries a SEALED token before any diff content [C-27, C-29]
5. Every findings table has a Type column with F-01 Type=IA-RESPONSE [C-34]
6. Every findings table has a Domain-Lens column with gate value per row [C-24]
7. All findings passed domain-lens gate Steps A and B

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
  Mechanism: [structural or architectural property of the code causing the difference --
             not a perspective difference]

Critical: [F-XX from role] -- [why this most threatens the merge]
```

Perspective-label ban-to-fix (scan every Mechanism line against all five before writing):

| Banned | Required replacement |
|---|---|
| "they have different perspectives" | "[role-A] sees [mechanism X]; [role-B] sees [mechanism Y]" |
| "they prioritize differently" | "[path X] is inside [role-A]'s domain and outside [role-B]'s" |
| "they see this through different lenses" | "change affects [mechanism A] in [role-A]'s domain and [mechanism B] in [role-B]'s" |
| "from [role]'s perspective" as sole cause | name the architectural fact causing the risk |
| "their roles lead them to different conclusions" | "[role-A]'s scope includes [code surface X]; [role-B]'s does not" |

A Mechanism line containing a banned phrase fails even if an architectural mechanism is
also named in the same sentence.

Phase D exit: consensus complete; all Mechanism lines pass the ban-to-fix check.

---

**PHASE E -- DECISION**

Entry: Phase D exit met.

```
## Phase E: Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from role] -- [one sentence on why this finding drives the decision]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] -- sign-off: [role who confirms resolution before merge]
2. [additional condition if present] -- sign-off: [role]
```

Exactly one decision. Values: GO, NO-GO, GO WITH CONDITIONS only.
Delegated decisions fail. Hedged decisions fail.

Phase E exit: exactly one decision with value, primary finding justification, and
sign-off roles for each condition.

---

**AMEND**

When invoked with an AMEND directive, output this named-field block before Phase A.
All fields mandatory; write "none" if not applicable. Do not convert to prose.

```
## AMEND SCOPE

What was amended:           [description of the change from default routing]
Roles added:                [comma-separated list, or "none"]
Roles removed:              [comma-separated list, or "none"]
Files triggering addition:  [comma-separated list, or "n/a -- manually directed"]
Prior findings superseded:  [comma-separated F-IDs from any prior run, or "none -- first run"]
```

Run Phases A-E with the amended scope.
