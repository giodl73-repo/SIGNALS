---
skill: corps-pr
skill_target: Run a PR through the full org with per-role findings and go/no-go recommendation
round: R20-QU5
date: 2026-03-17
rubric_version: 18
source_variation: V-01 (Role Sequence -- Security-First)
---

# QU5 Simplification Pass -- corps-pr

## Task

Find the minimal golden prompt: the shortest version of the R20 V-01 winning prompt that still
passes all essential rubric criteria (C-01 through C-05).

## What was removed and why

| Removed | Lines (approx) | Why |
|---------|---------------|-----|
| "Fourteen structural compliance mechanisms are active: ..." catalog paragraph | 12 | Criterion-code metadata. Does no behavioral work -- all mechanisms are already enforced by the template structure below. |
| All `Gates: C-XX, ...` lines from pipeline declaration | 5 lines | Criterion-code audit trail only. Model doesn't need these to execute the phases. |
| Structural enforcement levels block (exit-condition/block/table-column partition) | 27 lines | Enforces C-41, C-44, C-46, C-49, C-50 -- all aspirational. The actual structural requirements are already stated in the pipeline exit conditions. |
| Closed paths block | 9 lines | Enforces C-43, C-45 -- aspirational. Prohibition on inline-cell-label path is implicit from the column-header template. |
| `[C-26]` annotations on C1/C2 sub-condition headers | inline | C-52 is aspirational. Labels carry zero behavioral weight. |
| `[C-25]` / `[C-53]` annotations on B3 budget verdict lines | inline | C-53 is aspirational. The three-line structure is preserved; criterion codes are removed. |
| `[C-37]`, `[C-39]`, `[C-54]`, `[C-35]` inline tags in C2 sub-condition description | inline | All aspirational. The structural requirements they name are preserved in prose. |
| `[C-33, C-37, C-39, C-26/C2, C-54]` label on STEP 2 header | inline | Criterion-code metadata only. |
| `[C-34, C-38, C-40, C-43]` label on STEP 4 header | inline | Criterion-code metadata only. |
| C-36 compliance explanation block (3 lines) | 3 lines | Aspirational (C-36). The exit-condition statement in pipeline Phase C exit item (3) already says "Phase D does not begin". |
| C-37/C-39 compliance explanation block (3 lines) | 3 lines | Aspirational. C2 RESULT block template already states per-field and same-block requirements. |
| C-54 compliance explanation block (3 lines) | 3 lines | Aspirational (C-54). Field (e) instruction already shows "inline value OR cross-reference". |
| F-01 IA-RESPONSE format rules section (8 lines) | 8 lines | Enforces C-38, C-40, C-43, C-46, C-49 -- all aspirational. The findings table template already has `[IA-VERDICT]` and `[ROLE-MECHANISM]` as column headers. |
| Long parenthetical in Phase D entry (7 C-XX codes) | partial | Aspirational criteria list. Replaced with "Phase C exit met". |

## Essential criteria check

| Criterion | What the simplified prompt provides | Pass? |
|-----------|-------------------------------------|-------|
| C-01 | Phase A routing table with `[exact pattern]` column and `COVERAGE GAP:` format string | YES |
| C-02 | Phase C present; "Role sequence: security/compliance roles first..." declared explicitly | YES |
| C-03 | Phase D Consensus section covers Agreement/Divergence/Critical across all roles | YES |
| C-04 | Phase E: "One decision. Values: GO, NO-GO, GO WITH CONDITIONS only. Delegated decisions fail. Hedged decisions fail." | YES |
| C-05 | Findings table: F-01 IA-RESPONSE row + F-02 DOMAIN row + "[minimum 2]" | YES |

Recommended criteria (C-06/C-07/C-08) also preserved: coverage-gap format string, two-step domain-lens gate, post-commitment delta block.

## Word counts

| Version | Words |
|---------|-------|
| Original V-01 prompt (between fences) | 2,280 |
| Simplified prompt (between fences) | 1,400 |
| Reduction | 880 words (38.6%) |

---

## Simplified Prompt

```
You are running `/corps-pr`. This skill runs as a five-phase pipeline.
Read the full pipeline declaration before producing any output.

---

**PIPELINE DECLARATION**

Phase A -- Route
  Entry:    org.yaml + PR diff + .craft/roles/ loaded
  Exit:     Routing table complete; every file has a row; every role cites exact scope
            pattern; coverage gaps declared

Phase B -- Inertia Review
  Entry:    Phase A exit met
  Exit:     (B1) Null hypothesis stated
            (B2) Cost ledger: 4 rows x 2 columns x Net direction per row filled
            (B3) Budget verdict: three separate labeled lines -- each on own line
            (B4) Budget strength declared as terminal field below separator
            (B5) IA verdict in cost terms

Phase C -- Technical Reviews
  Entry:    Two sub-conditions, each producing an exact result token:
            C1 (Phase B exit pre-flight, phase-level):
              Scope: Phase B completeness.
              Terminal: C1 RESULT: ALL CLEAR
              or C1 RESULT: BLOCKED -- [B-number]
            C2 (READ RECEIPT completeness, per-role):
              Scope: receipt fields (a)-(e) complete. NOT Phase B re-check.
              C2 RESULT block enumerates (a)-(e) with PRESENT/ABSENT per field.
              Per-field evidence and terminal verdict co-appear in same block.
              Field (e) validation names both acceptable forms as disjuncts.
              C2 RESULT must appear after READ RECEIPT block in output.
              Terminal (within the C2 RESULT block): C2 RESULT: SATISFIED [all five PRESENT]
              or C2 RESULT: UNSATISFIED -- field (x): [label]
  Exit:     (1) C1 ends in ALL CLEAR
            (2) All C2 blocks end in SATISFIED
            (3) READ RECEIPT precedes C2 RESULT per role -- a C2 RESULT before its READ
                RECEIPT is a Phase C exit-condition failure; Phase D does not begin
            (4) C2 RESULT block enumerates fields (a)-(e) with PRESENT/ABSENT; terminal
                verdict in same block; no cross-block reading required
            (5) PRE-COMMITMENT blocks precede findings tables
            (6) F-01 in every findings table: Type = IA-RESPONSE; [IA-VERDICT] and
                [ROLE-MECHANISM] are column headers
            (7) All findings passed domain-lens gate
  Role sequence: security/compliance roles first, then domain-specific roles, then PM/TPM.

Phase D -- Synthesis
  Entry:    Phase C exit met
  Exit:     Consensus complete; all Mechanism lines pass ban-to-fix check

Phase E -- Decision
  Entry:    Phase D exit met
  Exit:     Exactly one GO / NO-GO / GO WITH CONDITIONS; conditions name sign-off

---

## Phase A: Routing

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|---|---|---|---|
| [paths] | [add/modify/delete] | [role name] | [exact pattern] |
| (all files) | default | Inertia Advocate | default -- always included |

Coverage gap: `COVERAGE GAP: [file] -- no org.yaml scope pattern covers this path.`

---

## Phase B: Inertia Advocate

Status-quo champion: First reviewer in the pipeline. Defends the current codebase.
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
WORSE rows: [Cost Categories where Net = WORSE, or "none"]               <- B3 line 1
BETTER rows: [Cost Categories where Net = BETTER, or "none"]             <- B3 line 2
Conclusion: [one sentence -- is adoption justified?]                     <- B3 line 3

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

**C1 -- Phase B Exit Pre-Flight [scope: Phase B completeness]:**

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

**Per-Role Output Sequence (STEP 1 must precede STEP 2; STEP 2 before STEP 1 is a
Phase C exit-condition failure -- Phase D blocked):**

Role sequence: security/compliance roles first, then domain-specific roles, then PM/TPM.

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

**STEP 3 -- PRE-COMMITMENT [before reading diff]:**

PRE-COMMITMENT: [Role Name]

Cost row assessed:  [Maintenance / Incident exposure / Integration cost / Regression risk]
Initial position:   [CONFIRMS / DISPUTES] [Net direction] on [Cost row]
                    [one phrase based on domain knowledge + Phase B ledger]
Basis:              Domain knowledge only. PR diff not yet examined.
                    [one sentence naming the code surface or architectural pattern]

[PRE-COMMITMENT SEALED]

**STEP 4 -- FINDINGS:**

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

---

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

## Simplification Report

**What was removed and why** (summary):

1. **Criterion-code catalog preamble** (~112 words): "Fourteen structural compliance mechanisms are
   active: ..." lists C-25 through C-50 criterion codes. This is an audit manifest, not a behavioral
   instruction. The model executes phases because the template below tells it to -- not because a
   code catalog was listed.

2. **All `Gates:` lines** (~48 words): Five lines listing criterion codes per phase. Zero behavioral
   content -- the model runs Phase A because Phase A has a template, not because "Gates: C-01, C-06"
   appears.

3. **Structural enforcement levels block** (~280 words): The exit-condition/block/table-column
   partition enforces C-41, C-44, C-46, C-49, C-50 -- all aspirational. The actual structural
   requirements (READ RECEIPT before C2 RESULT; per-field PRESENT/ABSENT; column-header schema)
   are already stated in the pipeline exit conditions and template steps.

4. **Closed paths block** (~110 words): Enforces C-43, C-45 -- aspirational. The prohibition on
   inline-cell-label F-01 format is implicit from the column-header findings table template.

5. **Inline [C-XX] annotations** (~90 words total): `[C-26]` on C1/C2 headers, `[C-25]`/`[C-53]`
   on B3 lines, `[C-37]`/`[C-39]`/`[C-54]`/`[C-35]` in C2 sub-condition description, bracket
   label clusters on STEP 2 and STEP 4 headers. All aspirational criterion trackers -- the template
   instructions they annotate are preserved without the codes.

6. **Three compliance explanation blocks** (~100 words): "C-36 compliance: If...", "C-37/C-39
   compliance: ...", "C-54 compliance: ..." These restate in prose what the pipeline exit condition
   and C2 RESULT block template already mandate structurally.

7. **F-01 IA-RESPONSE format rules section** (~65 words): "Type cell: exactly IA-RESPONSE /
   [IA-VERDICT] and [ROLE-MECHANISM] are column headers. O(1) column-count verification. Prohibition
   [C-43]: do not use inline-cell-label path..." Enforces C-38, C-40, C-43, C-46, C-49 --
   aspirational. The findings table template already shows the correct column-header form.

8. **Phase D entry parenthetical** (~20 words): Long parenthetical list of C-XX codes in Phase D
   entry condition. Replaced with "Phase C exit met" -- the behavioral meaning is unchanged.

**Nothing functional was removed.** All five phases exist. All templates are intact. Role sequence
declaration preserved. Coverage gap format string preserved. Domain-lens two-step gate preserved.
Post-commitment delta block preserved. F-01 IA-RESPONSE type designation preserved in the findings
table template.

```json
{"simplified_word_count": 1400, "original_word_count": 2280, "all_essential_still_pass": true}
```
