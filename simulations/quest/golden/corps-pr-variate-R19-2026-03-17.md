---
skill: corps-pr
skill_target: Run a PR through the full org with per-role findings and go/no-go recommendation
round: R19
date: 2026-03-17
rubric_version: 17
---

# Variate R19 -- corps-pr

## Variation Axes

| Code | Axis | Description |
|------|------|-------------|
| V-01 | Lifecycle Emphasis | Explicit ENTER/EXIT banners per phase; checklist-style gate declarations at each boundary |
| V-02 | Inertia Framing | IA as Null Hypothesis Defender; default verdict BLOCK; B5 framed as "defeats / fails to defeat the null" |
| V-03 | Output Format | Phase E appends risk-register table with Likelihood / Impact / Mitigation-status columns |
| V-04 | Lifecycle Emphasis + Inertia Framing | ENTER/EXIT banners + null-hypothesis-defender framing combined |
| V-05 | Full Combination | Lifecycle Emphasis + Inertia Framing + Phrasing Register (second-person imperative) |

## R18 Baseline Summary

R18 achieved 42/42 aspirational (100 composite against v16 rubric) across all five variations by
carrying the C-49 + C-50 bidirectional symmetry declaration in the invariant structural core.
Four new criteria were extracted from R18 excellence signals:

- **C-51**: IA section header carries explicit adversarial function designation label distinct
  from the role name -- e.g., `Status-quo champion [C-11]:` -- making the section's structural
  purpose auditable by label-reading alone.
- **C-52**: Each C1 and C2 sub-condition description individually carries a bracketed criterion
  annotation citing the criterion that governs its result token format -- e.g., `[C-26]` on
  each sub-condition header, so the governing criterion is traceable from the pipeline
  declaration text without consulting the rubric.
- **C-53**: Named Budget verdict clause output lines carry inline governing criterion
  annotations as end-of-line markers -- `<- B3 line 1 [C-25]` etc. -- making per-line
  compliance traceable by line-scan.
- **C-54**: C2 RESULT per-field validation for field (e) names both acceptable evidence forms
  as explicit disjuncts: `inline value OR cross-reference "see PRE-COMMITMENT block: [row]"`.

## R19 Target

Propagate all four annotation/designation patterns across all five variations. Target:
46/46 aspirational (100 composite against v17 rubric).

## Predicted Scores (v17 rubric)

| Variation | C-51 | C-52 | C-53 | C-54 | Predicted Score | Composite |
|-----------|------|------|------|------|-----------------|-----------|
| V-01 | Pass | Pass | Pass | Pass | 46/46 | 100 |
| V-02 | Pass | Pass | Pass | Pass | 46/46 | 100 |
| V-03 | Pass | Pass | Pass | Pass | 46/46 | 100 |
| V-04 | Pass | Pass | Pass | Pass | 46/46 | 100 |
| V-05 | Pass | Pass | Pass | Pass | 46/46 | 100 |

---

## V-01 -- Lifecycle Emphasis (Explicit Phase Banners)

**Axis**: Lifecycle Emphasis -- each phase boundary carries an explicit `=== ENTER PHASE [X] ===`
banner before execution and an `=== EXIT PHASE [X] -- gate conditions met ===` declaration
before the next phase begins. Gate declarations appear as a named checklist at each boundary,
not embedded in prose. All other structure is invariant.

**Hypothesis**: Explicit enter/exit banners make phase-gate violations auditable by banner-scan
rather than prose parsing. A reviewer can locate any gate failure by finding the closest
`=== EXIT PHASE` declaration and checking whether the required checklist items are marked
complete. Structural compliance (C-51 through C-54) is unaffected because the annotation
patterns are carried in section headers and field templates, not in phase-boundary prose.

```
You are running `/corps-pr`. This skill runs as a five-phase pipeline. Fourteen structural
compliance mechanisms are active: string-matchable Budget verdict (C-25), named result tokens
with per-sub-condition criterion annotations (C-26 / C-52), PRE-COMMITMENT blocks (C-27),
receipt-completeness / ordering pair (C-33 + C-35), ordering as phase-gate failure (C-36),
self-contained per-field C2 RESULT block with dual-form field (e) validation (C-37 + C-39 + C-54),
F-01 IA-RESPONSE column-header schema (C-34 + C-38 + C-40), IA section adversarial designation
label (C-51), three-level structural enforcement partition with named path-negation sub-entry
(C-41 + C-46), CLOSED PATHS enumeration in pipeline declaration with format-rules restatement
(C-43 + C-45), Budget verdict governing criterion annotations (C-53), and
Eliminated-to-CLOSED-PATHS reverse cross-reference with bidirectional symmetry declaration
(C-49 + C-50).
Read the full pipeline declaration before producing any output.

---

**PIPELINE DECLARATION**

Phase A -- Route
  ENTER: org.yaml + PR diff + .craft/roles/ loaded
  EXIT:  Routing table complete; every file has a row; every role cites exact scope
         pattern; coverage gaps declared
  Gates: C-01, C-06

Phase B -- Inertia Review
  ENTER: Phase A exit met
  EXIT:  (B1) Null hypothesis stated
         (B2) Cost ledger: 4 rows x 2 columns x Net direction per row filled
         (B3) Budget verdict: three separate labeled lines [C-25] -- each on own line
              with governing criterion annotation [C-53]
         (B4) Budget strength declared as terminal field below separator
         (B5) IA verdict in cost terms
  Gates: C-11, C-17, C-19, C-21, C-25, C-51, C-53

Phase C -- Technical Reviews
  ENTER: Phase B exit met
  Entry: Two sub-conditions, each producing an exact result token:
         C1 (Phase B exit pre-flight, phase-level) [C-26]:
           Scope: Phase B completeness.
           Terminal: C1 RESULT: ALL CLEAR
           or C1 RESULT: BLOCKED -- [B-number]
         C2 (READ RECEIPT completeness, per-role) [C-26/C-33]:
           Scope: receipt fields (a)-(e) complete. NOT Phase B re-check.
           C2 RESULT block enumerates (a)-(e) with PRESENT/ABSENT per field [C-37].
           Per-field evidence and terminal verdict co-appear in same block [C-39].
           Field (e) validation names both acceptable forms as disjuncts [C-54].
           C2 RESULT must appear after READ RECEIPT block in output [C-35].
           Terminal (within the C2 RESULT block): C2 RESULT: SATISFIED [all five PRESENT]
           or C2 RESULT: UNSATISFIED -- field (x): [label] [ABSENT field named inline]
  EXIT:  (1) C1 ends in ALL CLEAR
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
  Gates: C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26, C-27, C-33, C-34,
         C-35, C-36, C-37, C-38, C-39, C-40, C-41, C-43, C-44, C-45, C-46, C-52, C-54

Phase D -- Synthesis
  ENTER: Phase C exit met (all 7 conditions including C-36 ordering, C-37/C-39
         self-contained block, C-38/C-40 column-header schema, C-41/C-46 declared
         partition + named negation sub-entry, C-43/C-45 CLOSED PATHS + format-rules
         restatement, C-49/C-50 reverse cross-reference + bidirectional symmetry)
  EXIT:  Consensus complete; all Mechanism lines pass ban-to-fix check
  Gates: C-03, C-09, C-12, C-13

Phase E -- Decision
  ENTER: Phase D exit met
  EXIT:  Exactly one GO / NO-GO / GO WITH CONDITIONS; conditions name sign-off
  Gates: C-04, C-10

Structural enforcement levels [C-41]:
  Exit-condition level -- Phase C exit checklist item (3):
    C-36: READ RECEIPT-before-C2-RESULT ordering is a Phase C exit-condition violation
          when not met; Phase D does not begin. Auditable by reading exit item (3) alone.
  Block level -- C2 RESULT named block (## C2 RESULT -- [Role Name]):
    C-37: C2 RESULT block enumerates receipt fields (a)-(e) with PRESENT/ABSENT per field.
    C-39: Per-field evidence and terminal verdict co-appear in the same named block;
          no cross-block reading required; UNSATISFIED path handled inline.
    C-54: Field (e) validation instruction names both acceptable evidence forms as
          explicit disjuncts: inline value OR cross-reference "see PRE-COMMITMENT block: [row]".
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

=== ENTER PHASE A -- ROUTE ===

## Phase A: Routing

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern] |
| (all files) | default | Inertia Advocate | default -- always included |

Coverage gap: `COVERAGE GAP: [file] -- no org.yaml scope pattern covers this path.`

=== EXIT PHASE A ===
Gate checklist:
[ ] Routing table complete -- every file has a row
[ ] Every role row cites exact org.yaml scope pattern
[ ] Coverage gaps declared (or "none")
All checked: Phase A exit met. Proceed to Phase B.

---

=== ENTER PHASE B -- INERTIA REVIEW ===
Entry: Phase A exit met.

The Budget verdict appears as exactly three separate labeled lines below the separator.
Each line begins with its clause label and carries its governing criterion annotation.

## Phase B: Inertia Advocate

Status-quo champion [C-11]: First reviewer in the pipeline. Defends the current codebase.
  The PR must demonstrate net improvement over doing nothing.

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

=== EXIT PHASE B ===
Gate checklist:
[ ] B1 -- Null hypothesis stated
[ ] B2 -- Cost ledger: 4 rows x 2 columns x Net direction per row
[ ] B3 -- Three Budget verdict lines present, each on own line with [C-25] annotation
[ ] B4 -- Budget strength terminal field present
[ ] B5 -- IA verdict in cost terms
[ ] Status-quo champion [C-11]: designation label present in section header
All checked: Phase B exit met. Proceed to Phase C.

---

=== ENTER PHASE C -- TECHNICAL REVIEWS ===

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

**STEP 2 -- C2 RESULT BLOCK [C-33, C-37, C-39, C-26/C2, C-54] [must follow STEP 1 -- C-35/C-36]:**

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
C2 RESULT line is in this same block, derived from the per-field rows above.

C-54 compliance: Field (e) names both valid evidence forms as disjuncts -- inline value
and cross-reference -- so an auditor reading this block can identify both valid paths.

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
  Step A: "Would only [this role] raise this finding, given their domain?" YES -> include.
  NO -> Step B: revise to name domain-owned mechanism. Still NO -> drop.

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

F-01 IA-RESPONSE format rules [C-34, C-38, C-40, C-43]:
- Type cell: exactly "IA-RESPONSE"
- [IA-VERDICT] and [ROLE-MECHANISM] are column headers. O(1) column-count verification.
- Prohibition [C-43]: do not use inline-cell-label path. See CLOSED PATHS [C-45],
  Eliminated [C-46] [C-46], and Eliminated back-reference to CLOSED PATHS [C-49].
- DOMAIN findings (F-02 onward): "--" in [IA-VERDICT] and [ROLE-MECHANISM].

=== EXIT PHASE C ===
Gate checklist:
[ ] C1 ALL CLEAR (Phase B scope)
[ ] Every C2 RESULT block: (a)-(e) with PRESENT/ABSENT; terminal verdict in same block
[ ] READ RECEIPT precedes C2 RESULT per role -- ordering violation = exit failure [C-35/C-36]
[ ] Field (e) in each C2 RESULT names both valid forms as disjuncts [C-54]
[ ] PRE-COMMITMENT before findings [C-27]
[ ] F-01: Type=IA-RESPONSE; [IA-VERDICT] and [ROLE-MECHANISM] as column headers [C-34/C-38/C-40]
[ ] "Status-quo champion [C-11]:" designation present in Phase B IA section header [C-51]
[ ] C1 and C2 sub-condition descriptions each carry [C-26] criterion annotation [C-52]
[ ] Budget verdict clause lines carry [C-25] governing criterion annotations [C-53]
[ ] "Eliminated [C-46]:" carries reverse cross-reference [C-49]; symmetry declared [C-50]
[ ] All findings passed domain-lens gate
All checked: Phase C exit met. Proceed to Phase D.

---

=== ENTER PHASE D -- SYNTHESIS ===
Entry: Phase C exit met (all gate checklist items above).

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

=== EXIT PHASE D ===
Gate checklist:
[ ] Consensus written: IA ledger summary, agreement, divergence, critical finding
[ ] Every Mechanism line passes ban-to-fix check
All checked: Phase D exit met. Proceed to Phase E.

---

=== ENTER PHASE E -- DECISION ===
Entry: Phase D exit met.

## Phase E: Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from role] -- [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] -- sign-off: [role who confirms before merge]

One decision. Values: GO, NO-GO, GO WITH CONDITIONS only.
Delegated decisions fail. Hedged decisions fail.

=== EXIT PHASE E ===

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

## V-02 -- Inertia Framing (Null Hypothesis Defender)

**Axis**: Inertia Framing -- the IA role is explicitly the "Null Hypothesis Defender." Phase B
entry declares that the burden of proof rests with the PR: the null hypothesis (current state
is acceptable) holds until the cost ledger refutes it. B1 becomes "Null hypothesis stated and
defended." B5 framed as "defeats / fails to defeat the null hypothesis." All structural elements
are invariant.

**Hypothesis**: Foregrounding the IA as a formal null-hypothesis institution (not merely a
cost-reviewer) makes it structurally harder to dismiss Phase B findings as advisory -- the
PR must demonstrably defeat the null before Phase C can proceed. The C-51 designation label
`Status-quo champion [C-11]:` is the anchor for this framing. Structural compliance
(C-52/C-53/C-54) is unaffected because those patterns live in pipeline sub-condition headers,
Budget verdict lines, and C2 RESULT field templates.

```
You are running `/corps-pr`. This skill runs as a five-phase pipeline. Fourteen structural
compliance mechanisms are active: string-matchable Budget verdict (C-25), named result tokens
with per-sub-condition criterion annotations (C-26 / C-52), PRE-COMMITMENT blocks (C-27),
receipt-completeness / ordering pair (C-33 + C-35), ordering as phase-gate failure (C-36),
self-contained per-field C2 RESULT block with dual-form field (e) validation (C-37 + C-39 + C-54),
F-01 IA-RESPONSE column-header schema (C-34 + C-38 + C-40), IA section adversarial designation
label (C-51), three-level structural enforcement partition with named path-negation sub-entry
(C-41 + C-46), CLOSED PATHS enumeration in pipeline declaration with format-rules restatement
(C-43 + C-45), Budget verdict governing criterion annotations (C-53), and
Eliminated-to-CLOSED-PATHS reverse cross-reference with bidirectional symmetry declaration
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
  Entry:    Phase A exit met.
            IA role: Null Hypothesis Defender. The null hypothesis is that the current
            codebase is acceptable. The burden of proof rests with the PR; the default
            verdict is BLOCK until the cost ledger demonstrates net improvement.
  Exit:     (B1) Null hypothesis stated and defended -- the current state mechanism named
            (B2) Cost ledger: 4 rows x 2 columns x Net direction per row filled
            (B3) Budget verdict: three separate labeled lines [C-25] with [C-53] annotations
                 "WORSE rows: [values]" on its own line
                 "BETTER rows: [values]" on its own line
                 "Conclusion: [text]" on its own line
            (B4) Budget strength declared as terminal field below separator
            (B5) IA verdict: PR defeats / fails to defeat the null hypothesis
  Gates:    C-11, C-17, C-19, C-21, C-25, C-51, C-53

Phase C -- Technical Reviews
  Entry:    Two sub-conditions, each producing an exact result token:
            C1 (Phase B exit pre-flight, phase-level) [C-26]:
              Scope: Phase B completeness.
              Terminal: C1 RESULT: ALL CLEAR
              or C1 RESULT: BLOCKED -- [B-number]
            C2 (READ RECEIPT completeness, per-role) [C-26/C-33]:
              Scope: receipt fields (a)-(e) complete. NOT Phase B re-check.
              C2 RESULT block enumerates (a)-(e) with PRESENT/ABSENT per field [C-37].
              Per-field evidence and terminal verdict co-appear in same block [C-39].
              Field (e) validation names both acceptable forms as disjuncts [C-54].
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
            C-35, C-36, C-37, C-38, C-39, C-40, C-41, C-43, C-44, C-45, C-46, C-52, C-54

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
    C-54: Field (e) validation instruction names both acceptable evidence forms as
          explicit disjuncts: inline value OR cross-reference "see PRE-COMMITMENT block: [row]".
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

Entry: Phase A exit met. The IA is the Null Hypothesis Defender. The null hypothesis --
that the current codebase is acceptable and adoption is not required -- holds until the
cost ledger demonstrates net improvement. The default verdict is BLOCK.

The Budget verdict appears as exactly three separate labeled lines below the separator.
Each line begins with its clause label and carries its governing criterion annotation.

## Phase B: Inertia Advocate

Status-quo champion [C-11]: Null Hypothesis Defender. Sequenced first. The null hypothesis
  holds until the cost ledger refutes it. Default verdict: BLOCK.

Null hypothesis: The codebase currently [does X via mechanism Y].           <- B1
  The null: the current mechanism is acceptable; adoption is not required.

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
Conclusion: [one sentence -- does the PR defeat the null hypothesis?]    <- B3 line 3 [C-25]

Budget strength: HIGH / MEDIUM / LOW                                      <- B4

Findings:
F-01 [P1/P2/P3] [argument the null hypothesis holds]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second argument grounded in cost ledger]
     Owner: [role] | Resolution: [action]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS -- [one sentence: PR defeats / fails to defeat null] <- B5

Phase B exit: B1-B5 met; three Budget verdict lines present as separate output lines
with governing criterion annotations [C-53].

---

**PHASE C -- TECHNICAL REVIEWS**

**C1 -- Phase B Exit Pre-Flight [C-26/C1, scope: Phase B completeness]:**

## Phase C Pre-Flight (C1)

[ ] B1 -- Null hypothesis stated and defended
[ ] B2 -- Cost ledger: 4 rows x 2 columns x Net direction per row
[ ] B3 -- Budget verdict: three labeled lines present
         "WORSE rows:" on own line? [yes/no]
         "BETTER rows:" on own line? [yes/no]
         "Conclusion:" on own line? [yes/no] -- all must be yes
[ ] B4 -- Budget strength terminal field
[ ] B5 -- IA verdict: defeats / fails to defeat null hypothesis

C1 RESULT: ALL CLEAR

If any box unchecked: `C1 RESULT: BLOCKED -- [B-number]`

C1 scope is Phase B. C1 RESULT does not confirm any role's READ RECEIPT content.

**Per-Role Output Sequence (C-35/C-36: STEP 1 must precede STEP 2 in the output;
STEP 2 before STEP 1 is a Phase C exit-condition failure -- Phase D blocked):**

Sequence across roles: domain-specific -> security/compliance -> PM/TPM.

**STEP 1 -- READ RECEIPT [must appear in output before STEP 2]:**

## IA READ RECEIPT -- [Role Name]

(a) Section read:        Phase B -- Inertia Advocate (Null Hypothesis Defender)
(b) Budget verdict:
      WORSE rows:        [restate Phase B "WORSE rows:" line verbatim]
      BETTER rows:       [restate Phase B "BETTER rows:" line verbatim]
      Conclusion:        [restate Phase B "Conclusion:" line accurately]
(c) Budget strength:     HIGH / MEDIUM / LOW [from Phase B terminal field]
(d) Ledger row:          [Maintenance / Incident exposure / Integration cost / Regression risk]
(e) Initial position:    [CONFIRMS / DISPUTES] Net direction on [row (d)]
                         [one phrase -- domain knowledge and Phase B ledger only]

**STEP 2 -- C2 RESULT BLOCK [C-33, C-37, C-39, C-26/C2, C-54] [must follow STEP 1]:**

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
  Step A: "Would only [this role] raise this finding?" YES -> include. NO -> Step B.
  Step B: Revise to name domain-owned mechanism. Still NO -> drop.

## Phase C: [Role Name]

Source files:  [from Phase A routing]
Orientation:   [one phrase from .craft/roles/]

[STEP 1: READ RECEIPT]
[STEP 2: C2 RESULT -- (a)-(e) + terminal verdict in same block]
[STEP 3: PRE-COMMITMENT]

Findings:

| ID | Type | Severity | [IA-VERDICT] | [ROLE-MECHANISM] | Domain-Lens | Owner | Resolution |
|----|------|----------|--------------|------------------|-------------|-------|------------|
| F-01 | IA-RESPONSE | P1/P2/P3 | [null hypothesis position or cost position from Phase B] | [specific code artifact in this role's domain] | Passed | [role] | [action] |
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
- Prohibition [C-43]: do not use inline-cell-label path. See CLOSED PATHS [C-45],
  Eliminated [C-46] [C-46], reverse cross-reference [C-49].
- F-01: null hypothesis position in [IA-VERDICT]; code artifact in [ROLE-MECHANISM].
- DOMAIN findings (F-02 onward): "--" in [IA-VERDICT] and [ROLE-MECHANISM].

Phase C exit: C1 ALL CLEAR; every C2 RESULT block: (a)-(e) PRESENT/ABSENT + terminal
verdict in same block [C-33, C-37, C-39]; field (e) names both valid forms [C-54]; READ
RECEIPT before C2 RESULT [C-35/C-36]; PRE-COMMITMENT before findings [C-27]; [IA-VERDICT]
and [ROLE-MECHANISM] as column headers [C-34/C-38/C-40]; "Status-quo champion [C-11]:"
designation in Phase B header [C-51]; C1 and C2 each carry [C-26] annotation [C-52];
Budget verdict clause lines carry [C-25] annotations [C-53]; "Eliminated [C-46]:" with
reverse cross-reference [C-49]; symmetry declared [C-50].

---

**PHASE D -- SYNTHESIS**

Entry: Phase C exit met (C-36, C-37/C-39, C-38/C-40, C-41/C-46, C-43/C-45, C-49/C-50,
C-51, C-52, C-53, C-54).

## Phase D: Consensus

IA cost ledger: Budget strength was [HIGH / MEDIUM / LOW].
  The null hypothesis was [sustained / refuted] by the cost ledger.
  WORSE rows were: [restate]. BETTER rows were: [restate].
  Technical roles collectively [reinforced / challenged / defeated] the IA's null position.
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

## V-03 -- Output Format (Risk Register)

**Axis**: Output Format -- Phase E appends a risk-register table. Each finding that reaches
Phase E becomes a risk entry with Likelihood (H/M/L), Impact (H/M/L), Risk Score
(H/M/L derived), Mitigation-status (Open / Resolved / Accepted), and Owner. The merge gate
evaluates unresolved High risk-score entries, not raw P1 count. Phase E exit conditions
updated to require the risk register.

**Hypothesis**: A risk-register format forces explicit Likelihood x Impact assessment for every
finding before the GO/NO-GO decision, surfacing findings where P1 severity understates systemic
risk (high likelihood x medium impact may outrank low likelihood x P1). The merge gate becomes
risk-score-adjusted rather than severity-count-adjusted. Structural compliance (C-51 through
C-54) is unaffected because the annotation patterns are in Phase B headers, C1/C2 sub-conditions,
Budget verdict lines, and C2 RESULT field templates.

```
You are running `/corps-pr`. This skill runs as a five-phase pipeline. Fourteen structural
compliance mechanisms are active: string-matchable Budget verdict (C-25), named result tokens
with per-sub-condition criterion annotations (C-26 / C-52), PRE-COMMITMENT blocks (C-27),
receipt-completeness / ordering pair (C-33 + C-35), ordering as phase-gate failure (C-36),
self-contained per-field C2 RESULT block with dual-form field (e) validation (C-37 + C-39 + C-54),
F-01 IA-RESPONSE column-header schema (C-34 + C-38 + C-40), IA section adversarial designation
label (C-51), three-level structural enforcement partition with named path-negation sub-entry
(C-41 + C-46), CLOSED PATHS enumeration in pipeline declaration with format-rules restatement
(C-43 + C-45), Budget verdict governing criterion annotations (C-53), and
Eliminated-to-CLOSED-PATHS reverse cross-reference with bidirectional symmetry declaration
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
            (B3) Budget verdict: three separate labeled lines [C-25] with [C-53] annotations
                 "WORSE rows: [values]" on its own line
                 "BETTER rows: [values]" on its own line
                 "Conclusion: [text]" on its own line
            (B4) Budget strength declared as terminal field below separator
            (B5) IA verdict in cost terms
  Gates:    C-11, C-17, C-19, C-21, C-25, C-51, C-53

Phase C -- Technical Reviews
  Entry:    Two sub-conditions, each producing an exact result token:
            C1 (Phase B exit pre-flight, phase-level) [C-26]:
              Scope: Phase B completeness.
              Terminal: C1 RESULT: ALL CLEAR
              or C1 RESULT: BLOCKED -- [B-number]
            C2 (READ RECEIPT completeness, per-role) [C-26/C-33]:
              Scope: receipt fields (a)-(e) complete. NOT Phase B re-check.
              C2 RESULT block enumerates (a)-(e) with PRESENT/ABSENT per field [C-37].
              Per-field evidence and terminal verdict co-appear in same block [C-39].
              Field (e) validation names both acceptable forms as disjuncts [C-54].
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
            C-35, C-36, C-37, C-38, C-39, C-40, C-41, C-43, C-44, C-45, C-46, C-52, C-54

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
            (E3) Risk register: every finding from all routed roles has a row;
                 Likelihood / Impact / Risk Score / Mitigation-status / Owner columns present;
                 Merge gate line states unresolved-High-risk-score rule
  Gates:    C-04, C-10

Structural enforcement levels [C-41]:
  Exit-condition level -- Phase C exit checklist item (3):
    C-36: READ RECEIPT-before-C2-RESULT ordering is a Phase C exit-condition violation
          when not met; Phase D does not begin. Auditable by reading exit item (3) alone.
  Block level -- C2 RESULT named block (## C2 RESULT -- [Role Name]):
    C-37: C2 RESULT block enumerates receipt fields (a)-(e) with PRESENT/ABSENT per field.
    C-39: Per-field evidence and terminal verdict co-appear in the same named block;
          no cross-block reading required; UNSATISFIED path handled inline.
    C-54: Field (e) validation instruction names both acceptable evidence forms as
          explicit disjuncts: inline value OR cross-reference "see PRE-COMMITMENT block: [row]".
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
Each line begins with its clause label and carries its governing criterion annotation.

## Phase B: Inertia Advocate

Status-quo champion [C-11]: First reviewer in the pipeline. Defends the current codebase.
  The PR must demonstrate net improvement over doing nothing.

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

Phase B exit: B1-B5 met; three Budget verdict lines present as separate output lines
with governing criterion annotations [C-53].

---

**PHASE C -- TECHNICAL REVIEWS**

**C1 -- Phase B Exit Pre-Flight [C-26/C1, scope: Phase B completeness]:**

## Phase C Pre-Flight (C1)

[ ] B1 -- Null hypothesis stated
[ ] B2 -- Cost ledger: 4 rows x 2 columns x Net direction per row
[ ] B3 -- Budget verdict: three labeled lines present with [C-25] annotations
         "WORSE rows:" on own line? [yes/no]
         "BETTER rows:" on own line? [yes/no]
         "Conclusion:" on own line? [yes/no] -- all must be yes
[ ] B4 -- Budget strength terminal field
[ ] B5 -- IA verdict in cost terms

C1 RESULT: ALL CLEAR

If any box unchecked: `C1 RESULT: BLOCKED -- [B-number]`

C1 scope is Phase B. C1 RESULT does not confirm any role's READ RECEIPT content.

**Per-Role Output Sequence (C-35/C-36: STEP 1 must precede STEP 2; violation = Phase D blocked):**

Sequence across roles: domain-specific -> security/compliance -> PM/TPM.

**STEP 1 -- READ RECEIPT [must appear in output before STEP 2]:**

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

**STEP 2 -- C2 RESULT BLOCK [C-33, C-37, C-39, C-26/C2, C-54] [must follow STEP 1]:**

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
  Step A: "Would only [this role] raise this finding?" YES -> include.
  NO -> Step B: revise to name domain-owned mechanism. Still NO -> drop.

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

F-01 IA-RESPONSE format rules [C-34, C-38, C-40, C-43]:
- Type cell: exactly "IA-RESPONSE"
- [IA-VERDICT] and [ROLE-MECHANISM] are column headers. O(1) column-count verification.
- Prohibition [C-43]: do not use inline-cell-label path. See CLOSED PATHS [C-45],
  Eliminated [C-46] [C-46], reverse cross-reference [C-49].
- DOMAIN findings (F-02 onward): "--" in [IA-VERDICT] and [ROLE-MECHANISM].

Phase C exit: C1 ALL CLEAR; every C2 RESULT block: (a)-(e) PRESENT/ABSENT + terminal verdict
in same block [C-33, C-37, C-39]; field (e) names both valid forms [C-54]; READ RECEIPT before
C2 RESULT [C-35/C-36]; PRE-COMMITMENT before findings [C-27]; [IA-VERDICT] and [ROLE-MECHANISM]
as column headers [C-34/C-38/C-40]; "Status-quo champion [C-11]:" designation present [C-51];
C1 and C2 each carry [C-26] annotation [C-52]; Budget verdict lines carry [C-25] annotations
[C-53]; "Eliminated [C-46]:" reverse cross-reference [C-49]; symmetry declared [C-50].

---

**PHASE D -- SYNTHESIS**

Entry: Phase C exit met (C-36, C-37/C-39, C-38/C-40, C-41/C-46, C-43/C-45, C-49/C-50,
C-51, C-52, C-53, C-54).

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

Risk register -- all findings from all routed roles:

| Finding | Role | Severity | Likelihood | Impact | Risk Score | Mitigation Status | Owner |
|---------|------|----------|------------|--------|------------|-------------------|-------|
| F-01 | Inertia Advocate | P[N] | H/M/L | H/M/L | H/M/L | Open / Resolved / Accepted | [role] |
| F-02 | [Role Name] | P[N] | H/M/L | H/M/L | H/M/L | Open / Resolved / Accepted | [role] |
[one row per finding across all routed roles]

Risk Score derivation: H x H = High; H x M or M x H = High; H x L or L x H = Medium;
  M x M = Medium; M x L or L x M = Low; L x L = Low.

Merge gate: GO requires zero unresolved High risk-score entries.
  Current unresolved High risk-score count: [n].

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

## V-04 -- Lifecycle Emphasis + Inertia Framing

**Axis**: Lifecycle Emphasis (ENTER/EXIT banners) + Inertia Framing (Null Hypothesis Defender,
default BLOCK, B5 as "defeats / fails to defeat"). This is the combination of V-01 and V-02
axes without register change.

**Hypothesis**: The combination of phase banners and adversarial null-hypothesis framing creates
the tightest structural accountability: the IA's default-BLOCK position must be explicitly
overridden by the cost ledger before the EXIT PHASE B banner can fire, and each subsequent
phase banner confirms that the prior phase's adversarial gate was met. The four new annotation
patterns (C-51 through C-54) integrate naturally: C-51 appears in the Phase B template,
C-52/C-53/C-54 in the pipeline declaration and C2 RESULT block.

```
You are running `/corps-pr`. This skill runs as a five-phase pipeline. Fourteen structural
compliance mechanisms are active: string-matchable Budget verdict (C-25), named result tokens
with per-sub-condition criterion annotations (C-26 / C-52), PRE-COMMITMENT blocks (C-27),
receipt-completeness / ordering pair (C-33 + C-35), ordering as phase-gate failure (C-36),
self-contained per-field C2 RESULT block with dual-form field (e) validation (C-37 + C-39 + C-54),
F-01 IA-RESPONSE column-header schema (C-34 + C-38 + C-40), IA section adversarial designation
label (C-51), three-level structural enforcement partition with named path-negation sub-entry
(C-41 + C-46), CLOSED PATHS enumeration in pipeline declaration with format-rules restatement
(C-43 + C-45), Budget verdict governing criterion annotations (C-53), and
Eliminated-to-CLOSED-PATHS reverse cross-reference with bidirectional symmetry declaration
(C-49 + C-50).
Read the full pipeline declaration before producing any output.

---

**PIPELINE DECLARATION**

Phase A -- Route
  ENTER: org.yaml + PR diff + .craft/roles/ loaded
  EXIT:  Routing table complete; every file has a row; every role cites exact scope
         pattern; coverage gaps declared
  Gates: C-01, C-06

Phase B -- Inertia Review
  ENTER: Phase A exit met.
         IA role: Null Hypothesis Defender. The null hypothesis holds until the cost ledger
         refutes it. Default verdict: BLOCK.
  EXIT:  (B1) Null hypothesis stated and defended
         (B2) Cost ledger: 4 rows x 2 columns x Net direction per row filled
         (B3) Budget verdict: three separate labeled lines [C-25] with [C-53] annotations
              "WORSE rows: [values]" on its own line
              "BETTER rows: [values]" on its own line
              "Conclusion: [text]" on its own line
         (B4) Budget strength declared as terminal field below separator
         (B5) IA verdict: PR defeats / fails to defeat the null hypothesis
  Gates: C-11, C-17, C-19, C-21, C-25, C-51, C-53

Phase C -- Technical Reviews
  ENTER: Phase B exit met
  Entry: Two sub-conditions, each producing an exact result token:
         C1 (Phase B exit pre-flight, phase-level) [C-26]:
           Scope: Phase B completeness.
           Terminal: C1 RESULT: ALL CLEAR
           or C1 RESULT: BLOCKED -- [B-number]
         C2 (READ RECEIPT completeness, per-role) [C-26/C-33]:
           Scope: receipt fields (a)-(e) complete. NOT Phase B re-check.
           C2 RESULT block enumerates (a)-(e) with PRESENT/ABSENT per field [C-37].
           Per-field evidence and terminal verdict co-appear in same block [C-39].
           Field (e) validation names both acceptable forms as disjuncts [C-54].
           C2 RESULT must appear after READ RECEIPT block in output [C-35].
           Terminal (within the C2 RESULT block): C2 RESULT: SATISFIED [all five PRESENT]
           or C2 RESULT: UNSATISFIED -- field (x): [label] [ABSENT field named inline]
  EXIT:  (1) C1 ends in ALL CLEAR
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
  Gates: C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26, C-27, C-33, C-34,
         C-35, C-36, C-37, C-38, C-39, C-40, C-41, C-43, C-44, C-45, C-46, C-52, C-54

Phase D -- Synthesis
  ENTER: Phase C exit met (all 7 conditions including C-36, C-37/C-39, C-38/C-40,
         C-41/C-46, C-43/C-45, C-49/C-50, C-51, C-52, C-53, C-54)
  EXIT:  Consensus complete; all Mechanism lines pass ban-to-fix check
  Gates: C-03, C-09, C-12, C-13

Phase E -- Decision
  ENTER: Phase D exit met
  EXIT:  Exactly one GO / NO-GO / GO WITH CONDITIONS; conditions name sign-off
  Gates: C-04, C-10

Structural enforcement levels [C-41]:
  Exit-condition level -- Phase C exit checklist item (3):
    C-36: READ RECEIPT-before-C2-RESULT ordering is a Phase C exit-condition violation
          when not met; Phase D does not begin. Auditable by reading exit item (3) alone.
  Block level -- C2 RESULT named block (## C2 RESULT -- [Role Name]):
    C-37: C2 RESULT block enumerates receipt fields (a)-(e) with PRESENT/ABSENT per field.
    C-39: Per-field evidence and terminal verdict co-appear in the same named block;
          no cross-block reading required; UNSATISFIED path handled inline.
    C-54: Field (e) validation instruction names both acceptable evidence forms as
          explicit disjuncts: inline value OR cross-reference "see PRE-COMMITMENT block: [row]".
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

=== ENTER PHASE A -- ROUTE ===

## Phase A: Routing

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern] |
| (all files) | default | Inertia Advocate | default -- always included |

Coverage gap: `COVERAGE GAP: [file] -- no org.yaml scope pattern covers this path.`

=== EXIT PHASE A ===
Gate checklist:
[ ] Routing table complete -- every file has a row
[ ] Every role row cites exact org.yaml scope pattern
[ ] Coverage gaps declared (or "none")
All checked: Phase A exit met.

---

=== ENTER PHASE B -- INERTIA REVIEW ===
Entry: Phase A exit met. IA is Null Hypothesis Defender. Default verdict: BLOCK.

The Budget verdict appears as exactly three separate labeled lines below the separator.

## Phase B: Inertia Advocate

Status-quo champion [C-11]: Null Hypothesis Defender. Sequenced first. The null holds
  until the cost ledger refutes it. Default verdict is BLOCK.

Null hypothesis: The codebase currently [does X via mechanism Y].           <- B1
  The null: the current mechanism is acceptable; adoption is not required.

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
Conclusion: [one sentence -- does the PR defeat the null?]               <- B3 line 3 [C-25]

Budget strength: HIGH / MEDIUM / LOW                                      <- B4

Findings:
F-01 [P1/P2/P3] [argument the null hypothesis holds]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second argument grounded in cost ledger]
     Owner: [role] | Resolution: [action]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS -- [PR defeats / fails to defeat the null]  <- B5

=== EXIT PHASE B ===
Gate checklist:
[ ] B1 -- Null hypothesis stated and defended
[ ] B2 -- Cost ledger: 4 rows x 2 columns x Net direction per row
[ ] B3 -- Three Budget verdict lines on own lines with [C-25] annotations
[ ] B4 -- Budget strength terminal field
[ ] B5 -- IA verdict in "defeats / fails to defeat" language
[ ] "Status-quo champion [C-11]:" designation present in section header [C-51]
All checked: Phase B exit met.

---

=== ENTER PHASE C -- TECHNICAL REVIEWS ===

**C1 -- Phase B Exit Pre-Flight [C-26/C1, scope: Phase B completeness]:**

## Phase C Pre-Flight (C1)

[ ] B1 -- Null hypothesis stated and defended
[ ] B2 -- Cost ledger: 4 rows x 2 columns x Net direction per row
[ ] B3 -- Three Budget verdict lines present with [C-25] annotations
         "WORSE rows:" on own line? [yes/no]
         "BETTER rows:" on own line? [yes/no]
         "Conclusion:" on own line? [yes/no] -- all must be yes
[ ] B4 -- Budget strength terminal field
[ ] B5 -- IA verdict in "defeats / fails to defeat" language

C1 RESULT: ALL CLEAR

If any box unchecked: `C1 RESULT: BLOCKED -- [B-number]`

**Per-Role Output Sequence (STEP 1 before STEP 2; violation = EXIT PHASE C BLOCKED):**

Sequence across roles: domain-specific -> security/compliance -> PM/TPM.

**STEP 1 -- READ RECEIPT [output before STEP 2]:**

## IA READ RECEIPT -- [Role Name]

(a) Section read:        Phase B -- Inertia Advocate (Null Hypothesis Defender)
(b) Budget verdict:
      WORSE rows:        [restate Phase B "WORSE rows:" line verbatim]
      BETTER rows:       [restate Phase B "BETTER rows:" line verbatim]
      Conclusion:        [restate Phase B "Conclusion:" line accurately]
(c) Budget strength:     HIGH / MEDIUM / LOW [from Phase B terminal field]
(d) Ledger row:          [Maintenance / Incident exposure / Integration cost / Regression risk]
(e) Initial position:    [CONFIRMS / DISPUTES] Net direction on [row (d)]
                         [one phrase -- domain knowledge and Phase B ledger only]

**STEP 2 -- C2 RESULT BLOCK [must follow STEP 1]:**

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

[PRE-COMMITMENT SEALED]

**STEP 4 -- FINDINGS:**

Apply domain-lens gate per finding.

## Phase C: [Role Name]

Source files:  [from Phase A routing]
Orientation:   [one phrase from .craft/roles/]

[STEP 1: READ RECEIPT]
[STEP 2: C2 RESULT -- (a)-(e) + terminal verdict in same block]
[STEP 3: PRE-COMMITMENT]

Findings:

| ID | Type | Severity | [IA-VERDICT] | [ROLE-MECHANISM] | Domain-Lens | Owner | Resolution |
|----|------|----------|--------------|------------------|-------------|-------|------------|
| F-01 | IA-RESPONSE | P1/P2/P3 | [null hypothesis position from Phase B] | [code artifact in this role's domain] | Passed | [role] | [action] |
| F-02 | DOMAIN | P1/P2/P3 | -- | [domain finding] | Passed | [role] | [action] |
[minimum 2]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3

Post-commitment delta:
  Pre-committed:   [CONFIRMS / DISPUTES] [Cost row]
  After findings:  [HELD / CHANGED]

F-01 IA-RESPONSE format rules: Type=IA-RESPONSE; [IA-VERDICT] and [ROLE-MECHANISM] as column
headers [C-34/C-38/C-40]; no inline-cell-label path [C-43, C-45, C-46, C-49].

=== EXIT PHASE C ===
Gate checklist:
[ ] C1 ALL CLEAR
[ ] Every C2 RESULT: (a)-(e) PRESENT/ABSENT; terminal verdict in same block [C-37/C-39]
[ ] READ RECEIPT before C2 RESULT per role [C-35/C-36]
[ ] Field (e) names both valid forms as disjuncts [C-54]
[ ] PRE-COMMITMENT before findings [C-27]
[ ] F-01: [IA-VERDICT] and [ROLE-MECHANISM] as column headers [C-34/C-38/C-40]
[ ] "Status-quo champion [C-11]:" in Phase B header [C-51]
[ ] C1 and C2 each carry [C-26] annotation [C-52]
[ ] Budget verdict lines carry [C-25] annotations [C-53]
[ ] Symmetry declared [C-50]; reverse cross-reference [C-49]
All checked: Phase C exit met.

---

=== ENTER PHASE D -- SYNTHESIS ===

## Phase D: Consensus

IA cost ledger: Budget strength was [HIGH / MEDIUM / LOW].
  The null hypothesis was [sustained / refuted].
  WORSE rows: [restate]. BETTER rows: [restate].
  Technical roles [reinforced / challenged / defeated] the null position.
  Net: [one sentence]

Agreement: [area] -- [role-A] and [role-B] independently raised [concern]
Divergence: [role-A] rates [area] P[N]; [role-B] rates P[N].
  Mechanism: [architectural fact -- not perspective]
Critical: [F-XX from role] -- [why]

Ban-to-fix: [Mechanism lines must name code facts, not role perspectives -- see table]

| Banned | Replacement |
|---|---|
| "they have different perspectives" | "[role-A] sees [mechanism X]; [role-B] sees [mechanism Y]" |
| "they prioritize differently" | "[path X] is in [role-A]'s domain, outside [role-B]'s" |
| "they see this through different lenses" | "change affects [A] in [role-A]'s domain and [B] in [role-B]'s" |
| "from [role]'s perspective" as sole cause | name the architectural fact causing risk |
| "their roles lead them to different conclusions" | "[role-A]'s scope includes [surface X]; [role-B]'s does not" |

=== EXIT PHASE D ===
Gate checklist:
[ ] Consensus written with IA ledger summary, agreement, divergence, critical finding
[ ] All Mechanism lines pass ban-to-fix check
All checked: Phase D exit met.

---

=== ENTER PHASE E -- DECISION ===

## Phase E: Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from role] -- [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] -- sign-off: [role]

One decision. GO, NO-GO, GO WITH CONDITIONS only. No delegation. No hedging.

=== EXIT PHASE E ===

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

## V-05 -- Full Combination (Lifecycle + Inertia Framing + Phrasing Register)

**Axis**: Lifecycle Emphasis (ENTER/EXIT banners) + Inertia Framing (Null Hypothesis Defender,
default BLOCK) + Phrasing Register (second-person imperative throughout). This is the maximum
annotation density variation: every phase boundary is bannered, the IA's adversarial position
is foregrounded with the `Status-quo champion [C-11]:` designation, and the register is
direct second-person imperative.

**Hypothesis**: The R18 V-05 full-combination pattern achieved the best structural compliance
density by combining adversarial framing, forced enumeration, and imperative register. Carrying
that pattern into R19 with C-51 through C-54 integrated confirms that the annotation layer
(designation labels, inline criterion cross-references, Budget verdict annotations, dual-form
field validation) is fully compatible with the adversarial + imperative style that drove the
highest compliance in prior rounds.

```
You are running `/corps-pr`. The Inertia Advocate is the Null Hypothesis Defender: Phase B
requires the PR to defeat the null hypothesis, not merely document it. Run this as a
five-phase pipeline. You have fourteen structural compliance rules to enforce: write a
string-matchable Budget verdict with governing criterion annotations (C-25 + C-53), produce
named result tokens with per-sub-condition criterion cross-references (C-26 + C-52), write
PRE-COMMITMENT blocks before reading the diff (C-27), verify receipt completeness before
ordering (C-33 + C-35), treat ordering violations as phase-gate failures (C-36), put all
five receipt fields and the terminal verdict in the same C2 RESULT block with dual-form
field (e) validation (C-37 + C-39 + C-54), use [IA-VERDICT] and [ROLE-MECHANISM] as column
headers in every findings table (C-34 + C-38 + C-40), put the adversarial designation label
in the IA section header (C-51), declare a three-level structural enforcement partition with
a named path-negation sub-entry (C-41 + C-46), put CLOSED PATHS in the pipeline declaration
with a format-rules restatement (C-43 + C-45), and carry the reverse cross-reference and
bidirectional symmetry declaration (C-49 + C-50).
Read the full pipeline declaration before writing any output.

---

**PIPELINE DECLARATION**

Phase A -- Route
  ENTER: Load org.yaml + PR diff + .craft/roles/
  EXIT:  Every file has a routing row; every role cites its exact scope pattern;
         coverage gaps declared
  Gates: C-01, C-06

Phase B -- Inertia Review
  ENTER: Phase A exit met.
         IA role: Null Hypothesis Defender. Adoption requires defeating the null.
         Default verdict is BLOCK until the cost ledger shows net improvement.
  EXIT:  (B1) Null hypothesis stated and defended
         (B2) Cost ledger: 4 rows x 2 columns x Net direction per row filled
         (B3) Budget verdict: three separate labeled lines [C-25] with [C-53] annotations
              "WORSE rows: [values]" on its own line
              "BETTER rows: [values]" on its own line
              "Conclusion: [text]" on its own line
         (B4) Budget strength declared as terminal field below separator
         (B5) IA verdict: PR defeats / fails to defeat the null hypothesis
  Gates: C-11, C-17, C-19, C-21, C-25, C-51, C-53

Phase C -- Technical Reviews
  ENTER: Phase B exit met
  Entry: Two sub-conditions, each producing an exact result token:
         C1 (Phase B exit pre-flight, phase-level) [C-26]:
           Scope: Phase B completeness.
           Write: C1 RESULT: ALL CLEAR
           or: C1 RESULT: BLOCKED -- [B-number]
         C2 (READ RECEIPT completeness, per-role) [C-26/C-33]:
           Scope: receipt fields (a)-(e) complete. NOT Phase B re-check.
           Enumerate (a)-(e) with PRESENT/ABSENT in the C2 RESULT block [C-37].
           Put per-field evidence and terminal verdict in the same block [C-39].
           For field (e), name both valid evidence forms as disjuncts [C-54].
           Write C2 RESULT after READ RECEIPT in output [C-35].
           Write: C2 RESULT: SATISFIED [all five PRESENT]
           or: C2 RESULT: UNSATISFIED -- field (x): [label] [ABSENT field named inline]
  EXIT:  (1) C1 ends in ALL CLEAR
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
  Gates: C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26, C-27, C-33, C-34,
         C-35, C-36, C-37, C-38, C-39, C-40, C-41, C-43, C-44, C-45, C-46, C-52, C-54

Phase D -- Synthesis
  ENTER: Phase C exit met (all 7 conditions: C-36, C-37/C-39, C-38/C-40, C-41/C-46,
         C-43/C-45, C-49/C-50, C-51, C-52, C-53, C-54)
  EXIT:  Write consensus; every Mechanism line passes ban-to-fix check
  Gates: C-03, C-09, C-12, C-13

Phase E -- Decision
  ENTER: Phase D exit met
  EXIT:  (E1) Write exactly one GO / NO-GO / GO WITH CONDITIONS; name sign-off
         (E2) Cite primary finding
         (E3) Write findings scorecard: every routed role has a row; P1/P2/P3 tallied;
              IA verdict row present; Merge gate line states unresolved-P1 rule
  Gates: C-04, C-10

Structural enforcement levels [C-41]:
  Exit-condition level -- Phase C exit checklist item (3):
    C-36: If you write a C2 RESULT terminal line before the READ RECEIPT header for that
          role, that is a Phase C exit-condition failure -- stop; do not begin Phase D.
          Auditable by reading exit item (3) alone.
  Block level -- C2 RESULT named block (## C2 RESULT -- [Role Name]):
    C-37: In the C2 RESULT block, enumerate receipt fields (a)-(e) with PRESENT/ABSENT.
    C-39: Put per-field evidence and terminal verdict in the same block; handle the
          UNSATISFIED path inline; do not use a separate fence.
    C-54: For field (e), name both valid evidence forms as explicit disjuncts:
          inline value OR cross-reference "see PRE-COMMITMENT block: [row]".
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

=== ENTER PHASE A -- ROUTE ===

Build a routing table. Give every file a row. Cite the exact org.yaml scope pattern.

## Phase A: Routing

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern] |
| (all files) | default | Inertia Advocate | default -- always included |

Coverage gap: `COVERAGE GAP: [file] -- no org.yaml scope pattern covers this path.`

=== EXIT PHASE A ===
[ ] Routing table complete -- every file has a row
[ ] Every role cites exact org.yaml scope pattern
[ ] Coverage gaps declared or "none"
All checked: proceed.

---

=== ENTER PHASE B -- INERTIA REVIEW ===
Entry: Phase A exit met. The IA is the Null Hypothesis Defender. Default verdict is BLOCK
until the cost ledger shows net improvement.

Write the Budget verdict as exactly three separate labeled lines below the separator.
Start each line with its clause label and end it with its governing criterion annotation.
Do not embed any clause in a table cell or on the same line as another clause.

## Phase B: Inertia Advocate

Status-quo champion [C-11]: Null Hypothesis Defender. Sequenced first [C-11].
  Default verdict: BLOCK. The PR must defeat the null to unlock CONDITION or PASS.

Null hypothesis: The codebase currently [does X via mechanism Y].                      <- B1
  The null: the current mechanism is acceptable; doing nothing is the valid choice.

Cost ledger:                                                                            <- B2

| Cost Category     | Current-State Cost                             | Adoption Cost (this PR)                 | Net                      |
|-------------------|------------------------------------------------|-----------------------------------------|--------------------------|
| Maintenance       | [LOW/MED/HIGH -- maintaining current path]     | [maintaining new path post-merge]       | WORSE / BETTER / NEUTRAL |
| Incident exposure | [failure risk/severity under status quo]       | [residual exposure after merge]         | WORSE / BETTER / NEUTRAL |
| Integration cost  | [coordination overhead of current approach]    | [churn, downstream wiring, test burden] | WORSE / BETTER / NEUTRAL |
| Regression risk   | [risk of new failures from current approach]   | [risk introduced by this PR]            | WORSE / BETTER / NEUTRAL |

---
WORSE rows: [Cost Categories where Net = WORSE, or "none"]               <- B3 line 1 [C-25]
BETTER rows: [Cost Categories where Net = BETTER, or "none"]             <- B3 line 2 [C-25]
Conclusion: [one sentence -- does the PR defeat the null hypothesis?]    <- B3 line 3 [C-25]

Budget strength: HIGH / MEDIUM / LOW                                      <- B4

Findings:
F-01 [P1/P2/P3] [argument the null hypothesis holds]
     Owner: [role] | Resolution: [action]
F-02 [P1/P2/P3] [second argument grounded in cost ledger]
     Owner: [role] | Resolution: [action]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS -- [PR defeats / fails to defeat the null]        <- B5

=== EXIT PHASE B ===
[ ] B1 -- Null hypothesis stated and defended
[ ] B2 -- Cost ledger: 4 rows x 2 columns x Net direction per row
[ ] B3 -- Three Budget verdict lines present; each on own line with [C-25] annotation
[ ] B4 -- Budget strength terminal field
[ ] B5 -- "defeats / fails to defeat" language in IA verdict
[ ] "Status-quo champion [C-11]:" designation label present in section header [C-51]
All checked: proceed.

---

=== ENTER PHASE C -- TECHNICAL REVIEWS ===

**Run the Phase B exit pre-flight now. C1 scope is Phase B only [C-26/C1]:**

## Phase C Pre-Flight (C1)

[ ] B1 -- Null hypothesis stated and defended
[ ] B2 -- Cost ledger: 4 rows x 2 columns x Net direction per row
[ ] B3 -- Three labeled Budget verdict lines present with [C-25] annotations
         "WORSE rows:" on own line? [yes/no]
         "BETTER rows:" on own line? [yes/no]
         "Conclusion:" on own line? [yes/no] -- all must be yes
[ ] B4 -- Budget strength terminal field
[ ] B5 -- "defeats / fails to defeat" in IA verdict

If all checked: C1 RESULT: ALL CLEAR
If any unchecked: C1 RESULT: BLOCKED -- [B-number]

C1 scope is Phase B only. Do not use C1 to confirm any role's READ RECEIPT.

**For each routed role, write steps 1-4 in this exact sequence.
Role order: domain-specific -> security/compliance -> PM/TPM.**

**STEP 1 -- Write the READ RECEIPT now [C-35/C-36]. Do not write C2 RESULT first.**

## IA READ RECEIPT -- [Role Name]

(a) Section read:        Phase B -- Inertia Advocate (Null Hypothesis Defender)
(b) Budget verdict:
      WORSE rows:        [restate Phase B "WORSE rows:" line verbatim]
      BETTER rows:       [restate Phase B "BETTER rows:" line verbatim]
      Conclusion:        [restate Phase B "Conclusion:" line accurately]
(c) Budget strength:     HIGH / MEDIUM / LOW [from Phase B terminal field]
(d) Ledger row:          [Maintenance / Incident exposure / Integration cost / Regression risk]
(e) Initial position:    [CONFIRMS / DISPUTES] Net direction on [row (d)]
                         [one phrase -- domain knowledge and Phase B ledger only]

**STEP 2 -- Write the C2 RESULT block now [must follow STEP 1; C-33, C-37, C-39, C-26/C2, C-54]:**

Enumerate all five receipt fields (a)-(e) with PRESENT or ABSENT. Derive the terminal
verdict from the per-field lines. Put everything in one block. Handle UNSATISFIED inline.
For field (e), name both valid evidence forms as explicit disjuncts [C-54].

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

Domain-lens gate:
  Ask: "Would only [this role] raise this?" YES -> include.
  NO -> revise to name domain-owned mechanism. Still NO -> drop.

Use [IA-VERDICT] and [ROLE-MECHANISM] as column headers -- not cell labels.

## Phase C: [Role Name]

Source files:  [from Phase A routing]
Orientation:   [one phrase from .craft/roles/]

[STEP 1: READ RECEIPT]
[STEP 2: C2 RESULT -- (a)-(e) + terminal verdict in same block, dual-form field (e)]
[STEP 3: PRE-COMMITMENT]

Findings:

| ID | Type | Severity | [IA-VERDICT] | [ROLE-MECHANISM] | Domain-Lens | Owner | Resolution |
|----|------|----------|--------------|------------------|-------------|-------|------------|
| F-01 | IA-RESPONSE | P1/P2/P3 | [null hypothesis position from Phase B] | [specific code artifact in this role's domain] | Passed | [role] | [action] |
| F-02 | DOMAIN | P1/P2/P3 | -- | [domain finding] | Passed | [role] | [action] |
[minimum 2]

Summary: [N] findings -- [x] P1, [y] P2, [z] P3

Post-commitment delta:
  Pre-committed:   [CONFIRMS / DISPUTES] [Cost row]
  After findings:  [HELD / CHANGED]
  If HELD:         [code artifact from diff that confirmed the position]
  If CHANGED:      [code artifact that changed it; revised position]

F-01 format rules [C-34, C-38, C-40, C-43]:
- Write exactly "IA-RESPONSE" in Type.
- Use [IA-VERDICT] and [ROLE-MECHANISM] as column headers. O(1) column-count check.
- Do not use the inline-cell-label path. See CLOSED PATHS [C-45], Eliminated [C-46] [C-49].
- F-01: null hypothesis position in [IA-VERDICT]; code artifact in [ROLE-MECHANISM].
- DOMAIN findings (F-02 onward): "--" in [IA-VERDICT] and [ROLE-MECHANISM].

=== EXIT PHASE C ===
[ ] C1 ALL CLEAR (Phase B scope only)
[ ] Every C2 RESULT: (a)-(e) with PRESENT/ABSENT; terminal verdict in same block [C-37/C-39]
[ ] READ RECEIPT before C2 RESULT per role -- violation = phase gate failure [C-35/C-36]
[ ] Field (e) names both valid forms as disjuncts [C-54]
[ ] PRE-COMMITMENT before findings [C-27]
[ ] [IA-VERDICT] and [ROLE-MECHANISM] as column headers [C-34/C-38/C-40]
[ ] "Status-quo champion [C-11]:" designation in Phase B header [C-51]
[ ] C1 and C2 sub-condition descriptions each carry [C-26] annotation [C-52]
[ ] Budget verdict clause lines carry [C-25] annotations [C-53]
[ ] "Eliminated [C-46]:" with reverse cross-reference [C-49]; symmetry declared [C-50]
[ ] All findings passed domain-lens gate
All checked: proceed.

---

=== ENTER PHASE D -- SYNTHESIS ===
Entry: Phase C exit met (all checklist items above).

## Phase D: Consensus

Write the IA cost ledger summary:
  Budget strength was [HIGH / MEDIUM / LOW].
  The null hypothesis was [sustained / refuted].
  WORSE rows were: [restate]. BETTER rows were: [restate].
  Technical roles [reinforced / challenged / defeated] the null position.
  Net: [one sentence]

Find agreement: [area] -- [role-A] and [role-B] independently raised [concern]

Find divergence: [role-A] rates [area] P[N]; [role-B] rates P[N].
  Write the Mechanism: [architectural property -- not perspective]

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

=== EXIT PHASE D ===
[ ] Consensus written: null hypothesis outcome, agreement, divergence, critical finding
[ ] Every Mechanism line passes ban-to-fix check
All checked: proceed.

---

=== ENTER PHASE E -- DECISION ===
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
[one row per routed role]

IA verdict: [BLOCK / CONDITION / PASS from Phase B] -- [defeats / fails to defeat the null]
Merge gate: GO requires zero unresolved P1s. Current unresolved P1 count: [n].

One decision only: GO, NO-GO, or GO WITH CONDITIONS. Do not delegate. Do not hedge.

=== EXIT PHASE E ===

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
