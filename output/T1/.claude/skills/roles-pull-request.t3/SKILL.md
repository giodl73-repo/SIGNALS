---
name: roles-pull-request
description: Run a PR through the full org. Selects reviewers based on files changed -- compiler changes get compiler roles, security
allowed-tools: [Read, Write, Glob, Bash]
param_set: full
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


confidence: standard
# low    -> include findings without citation
# standard -> cite source section for each finding (default)
# strict  -> only include findings with quotable specific evidence


for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


iterations: 1  # run 1x independently, aggregate findings, mark new vs confirmed


This skill executes as `/corps-pr`. A five-phase pipeline is followed. Fourteen structural
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
The full pipeline declaration is to be read before any output is produced.

---

**PIPELINE DECLARATION**

Phase A -- Route
  Entry:    org.yaml + PR diff + .craft/roles/ are loaded
  Exit:     The routing table is complete; every file has a row; every role cites exact
            scope pattern; coverage gaps are declared
  Gates:    C-01, C-06

Phase B -- Inertia Review
  Entry:    Phase A exit is met
  Exit:     (B1) Null hypothesis is stated
            (B2) Cost ledger: 4 rows x 2 columns x Net direction per row is populated
            (B3) Budget verdict: three separate labeled lines [C-25] appear, each on its
                 own line with governing criterion annotation [C-53]
            (B4) Budget strength is declared as terminal field below separator
            (B5) IA verdict is expressed in cost terms
  Gates:    C-11, C-17, C-19, C-21, C-25, C-51, C-53

Phase C -- Technical Reviews
  Entry:    Two sub-conditions are satisfied, each producing an exact result token:
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
                a C2 RESULT line appearing before its role's READ RECEIPT block constitutes
                a Phase C exit-condition failure; Phase D does not begin
            (4) C2 RESULT block enumerates receipt fields (a)-(e) with PRESENT/ABSENT per
                field; terminal verdict is derived within same block; no cross-block reading
                is required [C-33, C-37, C-39]
            (5) PRE-COMMITMENT blocks precede findings tables [C-27]
            (6) F-01 in every findings table: Type = IA-RESPONSE; [IA-VERDICT] and
                [ROLE-MECHANISM] are column headers; slot compliance is O(1) column-count
                [C-34, C-38, C-40]; the pipeline declaration CLOSED PATHS names the
                prohibited inline-cell-label path [C-43, C-45]
            (7) All findings have passed the domain-lens gate
  Role sequence: security/compliance roles first, then domain-specific roles, then PM/TPM.
  Gates:    C-02, C-05, C-07, C-14, C-15, C-18, C-20, C-22, C-26, C-27, C-33, C-34,
            C-35, C-36, C-37, C-38, C-39, C-40, C-41, C-43, C-44, C-45, C-46, C-52, C-54

Phase D -- Synthesis
  Entry:    Phase C exit is met (all 7 conditions including C-36 ordering, C-37/C-39
            self-contained block, C-38/C-40 column-header schema, C-41/C-46 declared
            partition + named negation sub-entry, C-43/C-45 CLOSED PATHS + format-rules
            restatement, C-49/C-50 reverse cross-reference + bidirectional symmetry)
  Exit:     Consensus ranked table is complete; Mechanism column contains no banned phrases;
            IA ledger summary and critical finding fields are populated
  Output:   Named fields + ranked finding table (not prose paragraphs)
  Gates:    C-03, C-09, C-12, C-13

Phase E -- Decision
  Entry:    Phase D exit is met
  Exit:     Exactly one GO / NO-GO / GO WITH CONDITIONS is produced; conditions name sign-off
  Gates:    C-04, C-10

Structural enforcement levels [C-41]:
  Exit-condition level -- Phase C exit checklist item (3):
    C-36: READ RECEIPT-before-C2-RESULT ordering constitutes a Phase C exit-condition
          violation when not met; Phase D does not begin. Auditable by reading exit
          item (3) alone.
  Block level -- C2 RESULT named block (## C2 RESULT -- [Role Name]):
    C-37: C2 RESULT block enumerates receipt fields (a)-(e) with PRESENT/ABSENT per field.
    C-39: Per-field evidence and terminal verdict co-appear in the same named block;
          no cross-block reading is required; UNSATISFIED path is handled inline.
    C-54: Field (e) validation instruction names both acceptable evidence forms as
          explicit disjuncts: inline value OR cross-reference "see PRE-COMMITMENT block: [row]".
    Auditable by reading the C2 RESULT block alone.
  Table-column level -- findings table header row:
    C-38: F-01 IA-RESPONSE Description field declares [IA-VERDICT] and [ROLE-MECHANISM]
          as named schema slots visible in output.
    C-40: [IA-VERDICT] and [ROLE-MECHANISM] are column headers in the findings table;
          slot compliance is O(1) column-count check.
    Eliminated [C-46]: no inline-cell alternative path exists for [IA-VERDICT]/[ROLE-MECHANISM].
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
  Description cell) satisfies C-38 but is C-40 noncompliant -- this path is not to be used.
  Only the column-header form (separate named [IA-VERDICT] and [ROLE-MECHANISM] columns)
  satisfies the table-column level requirement. A reviewer auditing this section can verify
  the closed path by name without reading format rules [C-45].
  Path negation: see "Eliminated [C-46]:" in structural enforcement levels above [C-46].

---

## Phase A: Routing

The routing table is produced as follows:

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern] |
| (all files) | default | Inertia Advocate | default -- always included |

Coverage gaps are declared as: `COVERAGE GAP: [file] -- no org.yaml scope pattern covers this path.`

---

## Phase B: Inertia Advocate

Status-quo champion [C-11]: The first reviewer in the pipeline. The current codebase is
  defended. The PR must demonstrate net improvement over doing nothing.

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

---

## Phase C: Technical Reviews

**C1 -- Phase B Exit Pre-Flight [C-26/C1, scope: Phase B completeness]:**

The following checklist is evaluated:

[ ] B1 -- Null hypothesis stated
[ ] B2 -- Cost ledger: 4 rows x 2 columns x Net direction per row
[ ] B3 -- Budget verdict: three labeled lines present
         "WORSE rows:" on own line? [yes/no]
         "BETTER rows:" on own line? [yes/no]
         "Conclusion:" on own line? [yes/no] -- all must be yes
[ ] B4 -- Budget strength terminal field
[ ] B5 -- IA verdict in cost terms

C1 RESULT: ALL CLEAR

If any box is unchecked: `C1 RESULT: BLOCKED -- [B-number]`

C1 scope is Phase B. C1 RESULT does not confirm any role's READ RECEIPT content.

**Per-Role Output Sequence (C-35/C-36: STEP 1 must precede STEP 2 in the output;
STEP 2 before STEP 1 constitutes a Phase C exit-condition failure -- Phase D blocked):**

Sequence across roles: security/compliance first, then domain-specific, then PM/TPM.

**STEP 1 -- READ RECEIPT [must appear in output before STEP 2]:**

The READ RECEIPT block is produced before any C2 RESULT block for this role.

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

[the terminal verdict is derived from the per-field lines above -- exactly one is written:]
All five PRESENT:  C2 RESULT: SATISFIED -- all five fields PRESENT
Any ABSENT:        C2 RESULT: UNSATISFIED -- field (x): [label of absent field]

C-36 compliance: A "C2 RESULT:" terminal line appearing before the "## IA READ RECEIPT"
header for this role constitutes a Phase C exit-condition failure -- Phase D blocked.

C-37 / C-39 compliance: (a)-(e) each on its own labeled line with PRESENT/ABSENT; the
terminal C2 RESULT line is in this same block, derived from the per-field rows above.

C-54 compliance: Field (e) names both valid evidence forms as disjuncts -- inline value
and cross-reference -- so both valid paths are identifiable by reading this block alone.

**STEP 3 -- PRE-COMMITMENT [C-27, before reading diff]:**

PRE-COMMITMENT: [Role Name]

Cost row assessed:  [Maintenance / Incident exposure / Integration cost / Regression risk]
Initial position:   [CONFIRMS / DISPUTES] [Net direction] on [Cost row]
                    [one phrase based on domain knowledge + Phase B ledger]
Basis:              Domain knowledge only. PR diff not yet examined.
                    [one sentence naming the code surface or architectural pattern]

[PRE-COMMITMENT SEALED]

**STEP 4 -- FINDINGS [C-34, C-38, C-40, C-43]:**

Domain-lens gate is applied per finding:
  Step A: "Would only [this role] raise this finding, given their domain?" YES -> included.
  NO -> Step B: revise to name domain-owned mechanism. Still NO -> dropped.

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
- Prohibited path [C-43]: the inline-cell-label path is not to be used. See CLOSED PATHS [C-45],
  Eliminated [C-46] [C-46], and Eliminated back-reference to CLOSED PATHS [C-49].
- DOMAIN findings (F-02 onward): "--" in [IA-VERDICT] and [ROLE-MECHANISM].

---

## Phase D: Consensus

IA ledger:      Budget strength [HIGH / MEDIUM / LOW]; WORSE rows [restate]; BETTER rows [restate].
IA position:    Technical roles [reinforced / challenged / defeated] the IA's estimate.

Ranked consensus table (sorted by Severity descending):

| Rank | Finding | Source Role | Severity | Consensus | Mechanism |
|------|---------|-------------|----------|-----------|-----------|
| 1 | [F-XX] | [role] | P1/P2/P3 | [AGREEMENT / DIVERGENCE] | [architectural fact -- no banned phrases] |
| 2 | [F-XX] | [role] | P1/P2/P3 | [AGREEMENT / DIVERGENCE] | [architectural fact] |
[all Phase C findings ranked; minimum one P1 row]

Mechanism column ban-to-fix:
- Each Mechanism cell must name an architectural fact. Banned phrases fail even if a code
  mechanism is also named.

| Banned phrase | Required replacement form |
|---|---|
| "different perspectives" | "[role-A] sees [mechanism X]; [role-B] sees [mechanism Y]" |
| "prioritize differently" | "[path X] is in [role-A]'s domain, outside [role-B]'s" |
| "different lenses" | "change affects [A] in [role-A]'s domain and [B] in [role-B]'s" |
| "from [role]'s perspective" as sole cause | name the architectural fact causing risk |
| "roles lead them to different conclusions" | "[role-A]'s scope includes [surface X]; [role-B]'s does not" |

Critical finding:  [Rank 1 row F-ID] -- [one sentence: why this most threatens the merge]

---

## Phase E: Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary finding: [F-XX from role] -- [one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] -- sign-off: [role who confirms before merge]

One decision. Values: GO, NO-GO, GO WITH CONDITIONS only.
Delegated decisions fail. Hedged decisions fail.

---

**AMEND**

When invoked with an AMEND directive, the following named-field block is produced before Phase A.

## AMEND SCOPE

What was amended:           [description]
Roles added:                [list, or "none"]
Roles removed:              [list, or "none"]
Files triggering addition:  [list, or "n/a -- manually directed"]
Prior findings superseded:  [F-IDs, or "none -- first run"]

Phases A-E are then run with the amended scope.