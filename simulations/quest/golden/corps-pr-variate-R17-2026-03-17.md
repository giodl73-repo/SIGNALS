---
skill: corps-pr
skill_target: Run a PR through the full org with per-role findings and go/no-go recommendation
round: R17
date: 2026-03-17
rubric_version: 15
---

# Variate R17 — corps-pr

## Variation Axes

| Code | Axis | Description |
|------|------|-------------|
| V-01 | Inertia Framing | IA is "status-quo champion"; Phase B requires PR to defeat the null, not merely document it |
| V-02 | Output Format | Phase E appends per-role findings scorecard table (P1/P2/P3 tally + IA verdict + merge gate) |
| V-03 | Phrasing Register | Conversational imperative: second-person direct commands throughout |
| V-04 | Role Sequence + Lifecycle Emphasis | Domain-specific -> security/compliance -> PM/TPM; explicit ENTRY/EXIT banners in phase templates |
| V-05 | Full Combination | V-01 + V-02 + V-03 (Inertia Framing + Output Format + Phrasing Register) |

## R16 Baseline Summary

R16 V-05 scored 40/40 against the v15 rubric — the first variation to satisfy both C-47 and C-48:

- **C-47**: Named sub-entry `Eliminated [C-46]:` appears as a distinct labeled sub-entry in the structural enforcement levels section, with the self-declaration that it is "auditable by label-matching 'Eliminated [C-46]:' without parsing C-40."
- **C-48**: CLOSED PATHS block contains exactly: `Path negation: see "Eliminated [C-46]:" in structural enforcement levels above [C-46].`

R16 scores against v15 rubric:
- V-01, V-02 (R16): 38/40 — inline clause form; missed C-47 and C-48
- V-03, V-04 (R16): 39/40 — named sub-entry (C-47 passes); missed C-48 (no cross-reference in CLOSED PATHS)
- V-05 (R16): 40/40 — both C-47 and C-48 satisfied

## R17 Target

Replicate V-05's 40/40 pattern across ALL five variations. Every variation carries the invariant structural core verbatim in its PIPELINE DECLARATION. Every variation must score 40/40 aspirational (100 composite) against the v15 rubric.

## Predicted Scores (v15 rubric)

| Variation | C-47 | C-48 | Predicted Score | Composite |
|-----------|------|------|-----------------|-----------|
| V-01 | Pass | Pass | 40/40 | 100 |
| V-02 | Pass | Pass | 40/40 | 100 |
| V-03 | Pass | Pass | 40/40 | 100 |
| V-04 | Pass | Pass | 40/40 | 100 |
| V-05 | Pass | Pass | 40/40 | 100 |

---

## V-01 — Inertia Framing (Status-Quo Champion)

**Axis**: Inertia Framing — The IA is explicitly the status-quo champion. Phase B requires the PR to defeat the null hypothesis, not merely document costs. B1 label changes to "Status-quo position:"; the verdict asks whether the PR defeats the status quo.

**Hypothesis**: Framing the IA as an active defender of the status quo (rather than a neutral cost accountant) sharpens Phase B's adversarial structure. The model is more likely to produce a genuine null-defeat argument rather than a balanced ledger summary. Structural compliance (C-47, C-48) is unaffected because the invariant structural core is carried verbatim.

```
You are running `/corps-pr`. The Inertia Advocate is the status-quo champion: Phase B
requires the PR to defeat the null hypothesis, not merely document it. This skill runs
as a five-phase pipeline. Ten structural compliance mechanisms are active: string-matchable
Budget verdict (C-25), named result tokens (C-26), PRE-COMMITMENT blocks (C-27), receipt-
completeness / ordering pair (C-33 + C-35), ordering as phase-gate failure (C-36),
self-contained per-field C2 RESULT block (C-37 + C-39), F-01 IA-RESPONSE column-header
schema (C-34 + C-38 + C-40), three-level structural enforcement partition with named
path-negation sub-entry (C-41 + C-46), and CLOSED PATHS enumeration in pipeline declaration
with format-rules restatement (C-43 + C-45).
Read the full pipeline declaration before producing any output.

---

**PIPELINE DECLARATION**

Phase A -- Route
  Entry:    org.yaml + PR diff + .roles/ loaded
  Exit:     Routing table complete; every file has a row; every role cites exact scope
            pattern; coverage gaps declared
  Gates:    C-01, C-06

Phase B -- Inertia Review
  Entry:    Phase A exit met
            IA role: status-quo champion. Adoption requires demonstrating net improvement
            over doing nothing.
  Exit:     (B1) Status-quo position stated
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

Entry: Phase A exit met. The IA defends the status quo. The PR must demonstrate net
improvement; the default verdict is BLOCK until the cost ledger shows otherwise.

The Budget verdict appears as exactly three separate labeled lines below the separator.
Each line begins with its clause label. No clause is embedded in a table cell, in the
Conclusion of another clause, or merged with another clause on the same line.

## Phase B: Inertia Advocate (Status-Quo Champion)

Status-quo position: The codebase currently [does X via mechanism Y]. The null:           <- B1
  doing nothing is the valid choice until shown otherwise.

Cost ledger:                                                                               <- B2

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
IA verdict: BLOCK / CONDITION / PASS -- [one sentence: does this PR defeat the status quo?] <- B5

Phase B exit: B1-B5 met; three Budget verdict lines present as separate output lines.

---

**PHASE C -- TECHNICAL REVIEWS**

**C1 -- Phase B Exit Pre-Flight [C-26/C1, scope: Phase B completeness]:**

## Phase C Pre-Flight (C1)

[ ] B1 -- Status-quo position stated
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

(a) Section read:        Phase B -- Inertia Advocate (Status-Quo Champion)
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
Orientation:   [one phrase from .roles/]

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
with named negation sub-entry "Eliminated [C-46]:" [C-41, C-46]; CLOSED PATHS in declaration
+ four-element prohibition in format rules [C-43, C-45]; all findings passed domain-lens gate.

---

**PHASE D -- SYNTHESIS**

Entry: Phase C exit met (C-36 ordering, C-37/C-39 self-contained block, C-38/C-40
column-header schema, C-41/C-46 three-level partition + named negation sub-entry,
C-43/C-45 CLOSED PATHS in declaration + format rules restatement).

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

## V-02 — Output Format (Phase E Findings Scorecard)

**Axis**: Output Format — Phase E appends a per-role findings scorecard table that tallies P1/P2/P3 counts per role, includes the IA verdict, and states a merge gate condition.

**Hypothesis**: Adding a scorecard table to Phase E gives the model a structural forcing function for the final decision: it must enumerate every role's finding counts before issuing the GO/NO-GO. This reduces the risk of an omitted role in synthesis. The scorecard also surfaces whether any unresolved P1s exist at the point of decision, making the merge gate machine-checkable. Structural compliance (C-47, C-48) is unaffected because the invariant structural core is carried verbatim.

```
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

Phase A -- Route
  Entry:    org.yaml + PR diff + .roles/ loaded
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
  Exit:     (E1) Exactly one GO / NO-GO / GO WITH CONDITIONS; conditions name sign-off
            (E2) Primary finding cited
            (E3) Findings scorecard: per-role P1/P2/P3 tally + Merge gate stated
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
Orientation:   [one phrase from .roles/]

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
with named negation sub-entry "Eliminated [C-46]:" [C-41, C-46]; CLOSED PATHS in declaration
+ four-element prohibition in format rules [C-43, C-45]; all findings passed domain-lens gate.

---

**PHASE D -- SYNTHESIS**

Entry: Phase C exit met (C-36 ordering, C-37/C-39 self-contained block, C-38/C-40
column-header schema, C-41/C-46 three-level partition + named negation sub-entry,
C-43/C-45 CLOSED PATHS in declaration + format rules restatement).

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

Findings scorecard:

| Role | P1 | P2 | P3 | Total | IA-Verdict |
|------|----|----|-----|-------|------------|
| Inertia Advocate | [n] | [n] | [n] | [n] | BLOCK/CONDITION/PASS |
| [Role] | [n] | [n] | [n] | [n] | -- |
| [Role] | [n] | [n] | [n] | [n] | -- |
| [Role] | [n] | [n] | [n] | [n] | -- |

Merge gate: GO requires no unresolved P1s across all roles.

Phase E exit: E1 decision present (GO / NO-GO / GO WITH CONDITIONS); E2 primary finding
cited; E3 scorecard complete: all roles listed, P1/P2/P3 tallied, Merge gate stated.

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

**Axis**: Phrasing Register — All phase instructions are rewritten as second-person direct commands. The opening instructs the model to read before writing. Each phase transition is a directive, not a description.

**Hypothesis**: Imperative register makes the ordering constraint explicit as a behavioral command rather than a declarative rule. The model is less likely to anticipate content from a later phase because each phase instruction says "do this now." This may reduce C-36 and C-35 violations where the model collapses STEP 1 and STEP 2 into a single block. Structural compliance (C-47, C-48) is unaffected because the invariant structural core is carried verbatim.

```
You are running `/corps-pr`. Read the full pipeline declaration below before writing a
single line of output. Do not begin Phase A until you have read it completely. Ten
structural compliance mechanisms are active: string-matchable Budget verdict (C-25), named
result tokens (C-26), PRE-COMMITMENT blocks (C-27), receipt-completeness / ordering pair
(C-33 + C-35), ordering as phase-gate failure (C-36), self-contained per-field C2 RESULT
block (C-37 + C-39), F-01 IA-RESPONSE column-header schema (C-34 + C-38 + C-40),
three-level structural enforcement partition with named path-negation sub-entry (C-41 + C-46),
and CLOSED PATHS enumeration in pipeline declaration with format-rules restatement (C-43 + C-45).

---

**PIPELINE DECLARATION**

Phase A -- Route
  Entry:    org.yaml + PR diff + .roles/ loaded
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

---

**PHASE A -- ROUTE: Build the routing table now.**

Entry: org.yaml, PR diff, and .roles/ are loaded. Build the routing table. Give
every file a row. Cite the exact org.yaml scope pattern for each role. Declare any
coverage gaps before moving on.

## Phase A: Routing

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern] |
| (all files) | default | Inertia Advocate | default -- always included |

Coverage gap: `COVERAGE GAP: [file] -- no org.yaml scope pattern covers this path.`

---

**PHASE B -- INERTIA REVIEW: Begin the inertia review now.**

Entry: Phase A exit is met. Begin the inertia review. Write the null hypothesis first.
Then fill the cost ledger. Then write the three Budget verdict lines. Do not proceed to
Phase C until B1-B5 are all present.

The Budget verdict appears as exactly three separate labeled lines below the separator.
Each line begins with its clause label. No clause is embedded in a table cell, in the
Conclusion of another clause, or merged with another clause on the same line.

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

Phase B exit: B1-B5 met; three Budget verdict lines present as separate output lines.

---

**PHASE C -- TECHNICAL REVIEWS: Run C1, then each role in sequence.**

**C1 -- Phase B Exit Pre-Flight [C-26/C1, scope: Phase B completeness]:**

Run C1 now. Check each B-item. Write the result token before doing anything else in Phase C.

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

**STEP 1 -- READ RECEIPT: Write the READ RECEIPT block now. Do not write the C2 RESULT
block until the READ RECEIPT is complete in the output.**

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

**STEP 2 -- C2 RESULT BLOCK: Write the C2 RESULT block now. Enumerate (a)-(e) with
PRESENT/ABSENT. Derive the terminal verdict from the per-field rows above it. Keep
everything in this single block. [C-33, C-37, C-39, C-26/C2]**

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

Write the PRE-COMMITMENT block now. Do not read the diff until this block is sealed.

PRE-COMMITMENT: [Role Name]

Cost row assessed:  [Maintenance / Incident exposure / Integration cost / Regression risk]
Initial position:   [CONFIRMS / DISPUTES] [Net direction] on [Cost row]
                    [one phrase based on domain knowledge + Phase B ledger]
Basis:              Domain knowledge only. PR diff not yet examined.
                    [one sentence naming the code surface or architectural pattern]

[PRE-COMMITMENT SEALED]

**STEP 4 -- FINDINGS: Read the diff now and produce findings. [C-34, C-38, C-40, C-43]**

Apply domain-lens gate per finding:

Step A: "Would only [this role] raise this finding, given their domain?"
  YES -> include. NO -> Step B.
Step B: Revise to name domain-owned mechanism. Still NO -> drop.

The findings table MUST include a Type column. F-01 MUST have Type = IA-RESPONSE.
[IA-VERDICT] and [ROLE-MECHANISM] MUST be column headers.

## Phase C: [Role Name]

Source files:  [from Phase A routing]
Orientation:   [one phrase from .roles/]

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

Do not begin Phase D until all 7 exit conditions are met.

Phase C exit: C1 ALL CLEAR (Phase B scope); every C2 RESULT block enumerates (a)-(e)
PRESENT/ABSENT and derives terminal verdict in same block [C-33, C-37, C-39]; READ RECEIPT
precedes C2 RESULT per role -- ordering violation is Phase C exit-condition failure
[C-35/C-36]; PRE-COMMITMENT before findings [C-27]; F-01 Type=IA-RESPONSE with [IA-VERDICT]
and [ROLE-MECHANISM] as column headers [C-34/C-38/C-40]; three-level enforcement partition
with named negation sub-entry "Eliminated [C-46]:" [C-41, C-46]; CLOSED PATHS in declaration
+ four-element prohibition in format rules [C-43, C-45]; all findings passed domain-lens gate.

---

**PHASE D -- SYNTHESIS: Enter Phase D only after Phase C exit is confirmed.**

Entry: Phase C exit met (C-36 ordering, C-37/C-39 self-contained block, C-38/C-40
column-header schema, C-41/C-46 three-level partition + named negation sub-entry,
C-43/C-45 CLOSED PATHS in declaration + format rules restatement).

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

**PHASE E -- DECISION: Write exactly one decision now.**

Entry: Phase D exit met.

## Phase E: Recommendation

Write exactly one decision: GO, NO-GO, or GO WITH CONDITIONS. Do not delegate. Do not hedge.

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

## V-04 — Role Sequence + Lifecycle Emphasis (Domain-First + Entry/Exit Banners)

**Axis**: Role Sequence (domain-specific -> security/compliance -> PM/TPM) + Lifecycle Emphasis (explicit ENTRY CHECK / EXIT CHECK banners in each phase's output template).

**Hypothesis**: Putting domain reviewers first lets security and compliance roles react to domain findings rather than anticipating them, which may produce sharper F-01 IA-RESPONSE positioning. The entry/exit banners force the model to make each phase gate visible in the output, giving a post-hoc audit trail for every gate decision. Structural compliance (C-47, C-48) is unaffected because the invariant structural core is carried verbatim.

```
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

Phase A -- Route
  Entry:    org.yaml + PR diff + .roles/ loaded
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

---

**PHASE A -- ROUTE**

=== PHASE A ENTRY: org.yaml + PR diff + .roles/ loaded ===

## Phase A: Routing

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern] |
| (all files) | default | Inertia Advocate | default -- always included |

Coverage gap: `COVERAGE GAP: [file] -- no org.yaml scope pattern covers this path.`

=== PHASE A EXIT: routing table complete; all files have rows; every role cites exact scope pattern; coverage gaps declared ===

---

**PHASE B -- INERTIA REVIEW**

=== PHASE B ENTRY: Phase A exit confirmed ===

Entry: Phase A exit met.

The Budget verdict appears as exactly three separate labeled lines below the separator.
Each line begins with its clause label. No clause is embedded in a table cell, in the
Conclusion of another clause, or merged with another clause on the same line.

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

=== PHASE B EXIT: B1-B5 met; three Budget verdict lines present as separate output lines ===

---

**PHASE C -- TECHNICAL REVIEWS**

=== PHASE C ENTRY: C1 and C2 sub-conditions must both be satisfied ===

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
Orientation:   [one phrase from .roles/]

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

=== PHASE C EXIT: all 7 conditions met / BLOCKED at [condition if applicable] ===

Phase C exit: C1 ALL CLEAR (Phase B scope); every C2 RESULT block enumerates (a)-(e)
PRESENT/ABSENT and derives terminal verdict in same block [C-33, C-37, C-39]; READ RECEIPT
precedes C2 RESULT per role -- ordering violation is Phase C exit-condition failure
[C-35/C-36]; PRE-COMMITMENT before findings [C-27]; F-01 Type=IA-RESPONSE with [IA-VERDICT]
and [ROLE-MECHANISM] as column headers [C-34/C-38/C-40]; three-level enforcement partition
with named negation sub-entry "Eliminated [C-46]:" [C-41, C-46]; CLOSED PATHS in declaration
+ four-element prohibition in format rules [C-43, C-45]; all findings passed domain-lens gate.

---

**PHASE D -- SYNTHESIS**

=== PHASE D ENTRY: Phase C exit confirmed (all 7 conditions met) ===

Entry: Phase C exit met (C-36 ordering, C-37/C-39 self-contained block, C-38/C-40
column-header schema, C-41/C-46 three-level partition + named negation sub-entry,
C-43/C-45 CLOSED PATHS in declaration + format rules restatement; role sequence was
domain-specific -> security/compliance -> PM/TPM).

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

=== PHASE D EXIT: consensus complete; all Mechanism lines pass ban-to-fix check ===

---

**PHASE E -- DECISION**

=== PHASE E ENTRY: Phase D exit confirmed ===

Entry: Phase D exit met.

## Phase E: Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from role] -- [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] -- sign-off: [role who confirms before merge]

One decision. Values: GO, NO-GO, GO WITH CONDITIONS only.
Delegated decisions fail. Hedged decisions fail.

=== PHASE E EXIT: exactly one decision present; conditions name sign-off ===

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

**Axis**: Combines V-01 (status-quo champion framing in Phase B) + V-02 (Phase E findings scorecard) + V-03 (imperative register throughout). This is the maximum-signal variation: every axis that affects model behavior in a complementary direction is active simultaneously.

**Hypothesis**: The three axes reinforce each other. Imperative register ensures the model does not anticipate phases. Inertia framing makes Phase B a genuine adversarial test rather than a documentation exercise. The scorecard forces Phase E to enumerate all roles before issuing the decision, catching cases where a role's findings were silently dropped in synthesis. Together they maximize the probability of producing a well-structured, complete run. Structural compliance (C-47, C-48) is unaffected because the invariant structural core is carried verbatim.

```
You are running `/corps-pr`. Read the full pipeline declaration below before writing a
single line of output. Do not begin Phase A until you have read it completely. The Inertia
Advocate is the status-quo champion: Phase B requires the PR to defeat the null hypothesis,
not merely document it. Ten structural compliance mechanisms are active: string-matchable
Budget verdict (C-25), named result tokens (C-26), PRE-COMMITMENT blocks (C-27), receipt-
completeness / ordering pair (C-33 + C-35), ordering as phase-gate failure (C-36),
self-contained per-field C2 RESULT block (C-37 + C-39), F-01 IA-RESPONSE column-header
schema (C-34 + C-38 + C-40), three-level structural enforcement partition with named
path-negation sub-entry (C-41 + C-46), CLOSED PATHS enumeration in pipeline declaration
with format-rules restatement (C-43 + C-45), status-quo champion framing in Phase B,
per-role findings scorecard in Phase E, and imperative-register instructions throughout.

---

**PIPELINE DECLARATION**

Phase A -- Route
  Entry:    org.yaml + PR diff + .roles/ loaded
  Exit:     Routing table complete; every file has a row; every role cites exact scope
            pattern; coverage gaps declared
  Gates:    C-01, C-06

Phase B -- Inertia Review
  Entry:    Phase A exit met
            IA role: status-quo champion. Adoption requires demonstrating net improvement
            over doing nothing.
  Exit:     (B1) Status-quo position stated
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
  Exit:     (E1) Exactly one GO / NO-GO / GO WITH CONDITIONS; conditions name sign-off
            (E2) Primary finding cited
            (E3) Findings scorecard: per-role P1/P2/P3 tally + Merge gate stated
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

---

**PHASE A -- ROUTE: Build the routing table now.**

Entry: org.yaml, PR diff, and .roles/ are loaded. Build the routing table. Give
every file a row. Cite the exact org.yaml scope pattern for each role. Declare any
coverage gaps before moving on.

## Phase A: Routing

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern] |
| (all files) | default | Inertia Advocate | default -- always included |

Coverage gap: `COVERAGE GAP: [file] -- no org.yaml scope pattern covers this path.`

---

**PHASE B -- INERTIA REVIEW: Begin the inertia review now. The IA defends the status quo.**

Entry: Phase A exit is met. The IA defends the status quo. The PR must demonstrate net
improvement; the default verdict is BLOCK until the cost ledger shows otherwise. Write
the status-quo position first. Then fill the cost ledger. Then write the three Budget
verdict lines. Do not proceed to Phase C until B1-B5 are all present.

The Budget verdict appears as exactly three separate labeled lines below the separator.
Each line begins with its clause label. No clause is embedded in a table cell, in the
Conclusion of another clause, or merged with another clause on the same line.

## Phase B: Inertia Advocate (Status-Quo Champion)

Status-quo position: The codebase currently [does X via mechanism Y]. The null:           <- B1
  doing nothing is the valid choice until shown otherwise.

Cost ledger:                                                                               <- B2

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
IA verdict: BLOCK / CONDITION / PASS -- [one sentence: does this PR defeat the status quo?] <- B5

Phase B exit: B1-B5 met; three Budget verdict lines present as separate output lines.

---

**PHASE C -- TECHNICAL REVIEWS: Run C1, then each role in sequence.**

**C1 -- Phase B Exit Pre-Flight [C-26/C1, scope: Phase B completeness]:**

Run C1 now. Check each B-item. Write the result token before doing anything else in Phase C.

## Phase C Pre-Flight (C1)

[ ] B1 -- Status-quo position stated
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

**STEP 1 -- READ RECEIPT: Write the READ RECEIPT block now. Do not write the C2 RESULT
block until the READ RECEIPT is complete in the output.**

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

**STEP 2 -- C2 RESULT BLOCK: Write the C2 RESULT block now. Enumerate (a)-(e) with
PRESENT/ABSENT. Derive the terminal verdict from the per-field rows above it. Keep
everything in this single block. [C-33, C-37, C-39, C-26/C2]**

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

**STEP 3 -- PRE-COMMITMENT: Write the PRE-COMMITMENT block now. Do not read the diff until
this block is sealed. [C-27]**

PRE-COMMITMENT: [Role Name]

Cost row assessed:  [Maintenance / Incident exposure / Integration cost / Regression risk]
Initial position:   [CONFIRMS / DISPUTES] [Net direction] on [Cost row]
                    [one phrase based on domain knowledge + Phase B ledger]
Basis:              Domain knowledge only. PR diff not yet examined.
                    [one sentence naming the code surface or architectural pattern]

[PRE-COMMITMENT SEALED]

**STEP 4 -- FINDINGS: Read the diff now and produce findings. [C-34, C-38, C-40, C-43]**

Apply domain-lens gate per finding:

Step A: "Would only [this role] raise this finding, given their domain?"
  YES -> include. NO -> Step B.
Step B: Revise to name domain-owned mechanism. Still NO -> drop.

The findings table MUST include a Type column. F-01 MUST have Type = IA-RESPONSE.
[IA-VERDICT] and [ROLE-MECHANISM] MUST be column headers.

## Phase C: [Role Name]

Source files:  [from Phase A routing]
Orientation:   [one phrase from .roles/]

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

Do not begin Phase D until all 7 exit conditions are met.

Phase C exit: C1 ALL CLEAR (Phase B scope); every C2 RESULT block enumerates (a)-(e)
PRESENT/ABSENT and derives terminal verdict in same block [C-33, C-37, C-39]; READ RECEIPT
precedes C2 RESULT per role -- ordering violation is Phase C exit-condition failure
[C-35/C-36]; PRE-COMMITMENT before findings [C-27]; F-01 Type=IA-RESPONSE with [IA-VERDICT]
and [ROLE-MECHANISM] as column headers [C-34/C-38/C-40]; three-level enforcement partition
with named negation sub-entry "Eliminated [C-46]:" [C-41, C-46]; CLOSED PATHS in declaration
+ four-element prohibition in format rules [C-43, C-45]; all findings passed domain-lens gate.

---

**PHASE D -- SYNTHESIS: Enter Phase D only after Phase C exit is confirmed.**

Entry: Phase C exit met (C-36 ordering, C-37/C-39 self-contained block, C-38/C-40
column-header schema, C-41/C-46 three-level partition + named negation sub-entry,
C-43/C-45 CLOSED PATHS in declaration + format rules restatement).

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

**PHASE E -- DECISION: Write exactly one decision now.**

Entry: Phase D exit met.

## Phase E: Recommendation

Write exactly one decision: GO, NO-GO, or GO WITH CONDITIONS. Do not delegate. Do not hedge.

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from role] -- [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] -- sign-off: [role who confirms before merge]

One decision. Values: GO, NO-GO, GO WITH CONDITIONS only.
Delegated decisions fail. Hedged decisions fail.

Findings scorecard:

| Role | P1 | P2 | P3 | Total | IA-Verdict |
|------|----|----|-----|-------|------------|
| Inertia Advocate | [n] | [n] | [n] | [n] | BLOCK/CONDITION/PASS |
| [Role] | [n] | [n] | [n] | [n] | -- |
| [Role] | [n] | [n] | [n] | [n] | -- |
| [Role] | [n] | [n] | [n] | [n] | -- |

Merge gate: GO requires no unresolved P1s across all roles.

Phase E exit: E1 decision present (GO / NO-GO / GO WITH CONDITIONS); E2 primary finding
cited; E3 scorecard complete: all roles listed, P1/P2/P3 tallied, Merge gate stated.

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
