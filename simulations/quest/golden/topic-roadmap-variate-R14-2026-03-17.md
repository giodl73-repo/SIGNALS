---
skill: quest-variate
skill_target: topic-roadmap
round: R14
date: 2026-03-17
rubric_version: v14
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single:
    V-01: proposal_bias_audit_c31 -- upgrade guard to name both failure modes and why both required
    V-02: phase6_section_scope_c32 -- explicit scope enumeration cross-referencing guard
    V-03: output_schema_contract_c33 -- standalone CONTRACT block at earliest position
  combined:
    V-04: c31+c32+c33 standard -- CONTRACT inside Output Schema section (before Phase 1)
    V-05: c31+c32+c33 pre-earliest -- CONTRACT before INERTIA COMPETITOR DECLARATION; guard cross-references scope
rubric_anchor: >
  v14 adds C-31 (PROPOSAL BIAS AUDIT guard must name both failure modes: per-row =
  motivated reasoning at individual decision surface; phase-level = systemic phase
  structure bias; and explain why both are required), C-32 (Phase 6 SECTION SCOPE
  explicitly enumerates row-level bias labeling as a named scope item), C-33 (OUTPUT
  SCHEMA CONTRACT pre-commits both consequence field name at all three C-29 sites and
  Bias blocked by guard column; both failures detectable from block alone). Formula
  denominator 44->50 (25 aspirational x 2). R13 V-04/V-05 scored 44/44 under v13;
  under v14 they score 44/50 = 8.80, providing 6 points of headroom.
round_targets: >
  C-31 full pass (2): Named PROPOSAL BIAS AUDIT guard at Phase 6 entry co-located with
  INERTIA-GATE. Guard text names the phase-level failure mode (systemic phase structure
  bias) AND the row-level failure mode (motivated reasoning at individual proposal
  decision surface) as two distinct failure modes. Guard explicitly states both are
  required and that neither substitutes for the other.
  C-32 full pass (2): Phase 6 SECTION SCOPE declaration explicitly enumerates
  row-level bias labeling as a named scope item alongside gate-exclusion text and
  proposal generation. Cross-reference to PROPOSAL BIAS AUDIT guard present. A C-24
  auditor checking Phase 6 scope finds row-level bias labeling declared within that
  scope, not outside it.
  C-33 full pass (2): Standalone OUTPUT SCHEMA CONTRACT block positioned before any
  file read instruction. CONTRACT A names all three C-29 sites (Phase 5 column,
  Phase 6a column, Phase 6b column) and the Phase 5 exit criterion. CONTRACT B names
  Bias blocked by guard as required in Phase 6a and Phase 6b. Both violations
  detectable from the contract block alone without reading any phase.
orthogonality_notes: >
  V-01 (C-31 full, C-32 partial, C-33 partial): guard upgraded to name both failure
  modes; SECTION SCOPE unchanged from R13 V-05 (has row-level bias labeling text but
  no cross-reference to guard); CONTRACT unchanged from R13 V-05 (embedded annotation,
  not standalone).
  V-02 (C-31 partial, C-32 full, C-33 partial): guard unchanged from R13 V-05; SECTION
  SCOPE upgraded with explicit scope enumeration and guard cross-reference; CONTRACT
  unchanged from R13 V-05.
  V-03 (C-31 partial, C-32 partial, C-33 full): guard unchanged from R13 V-05; SECTION
  SCOPE unchanged from R13 V-05; standalone OUTPUT SCHEMA CONTRACT block at earliest
  position naming all three sites and both columns.
  V-04 (C-31 full, C-32 full, C-33 full -- CONTRACT standard): all three criteria; CONTRACT
  positioned inside Output Schema section (before Phase 1, after phase schemas shown).
  V-05 (C-31 full, C-32 full, C-33 full -- CONTRACT pre-earliest): all three criteria;
  CONTRACT at document-first position before INERTIA COMPETITOR DECLARATION; C-31 guard
  explicitly cross-references the C-32 SECTION SCOPE.
---

## Variation Summary

| Var | C-31 | C-32 | C-33 | CONTRACT position | Expected score | Hypothesis |
|-----|------|------|------|-------------------|----------------|------------|
| V-01 | FULL | partial | partial | R13 embedded | 46/50 | Guard naming both failure modes achieves C-31 independently |
| V-02 | partial | FULL | partial | R13 embedded | 46/50 | Explicit scope enumeration with guard cross-ref achieves C-32 independently |
| V-03 | partial | partial | FULL | standalone earliest | 46/50 | Standalone CONTRACT at earliest position achieves C-33 independently |
| V-04 | FULL | FULL | FULL | inside Output Schema | 50/50 | All three combined with CONTRACT in standard pre-Phase-1 slot |
| V-05 | FULL | FULL | FULL | before INERTIA DECL | 50/50 | CONTRACT at absolute earliest; guard cross-references scope |

---

## V-01 -- Single axis: C-31 PROPOSAL BIAS AUDIT guard (both failure modes named)

**Variation axis**: The PROPOSAL BIAS AUDIT guard at Phase 6 entry is upgraded from
R13 V-05. In R13 V-05, the guard names the per-row failure mode (motivated reasoning
at individual decision surface) but labels the phase-level annotations only as
"bias prevented by the entire phase structure" -- it does not name the phase-level
failure mode or state why both are required. V-01 adds: (a) explicit name for the
phase-level failure mode: "systemic phase structure bias -- anchoring to the
existence of the proposal phase as implicit evidence that change is warranted before
any row is evaluated"; (b) explicit statement that both are required and neither
substitutes for the other; (c) the structure now reads as two named levels rather
than one named level vs one undescribed level.

SECTION SCOPE is unchanged from R13 V-05 (has "row-level bias labeling" but no
guard cross-reference -- C-32 partial). CONTRACT block is the R13 V-05 embedded
annotation (present but not standalone -- C-33 partial if standalone is required).

**Hypothesis**: C-31 full pass requires the guard to name BOTH failure modes and
explain why both are required. R13 V-05 named only the row-level failure mode. Adding
the phase-level failure mode name ("systemic phase structure bias") and the "both
required, neither substitutes" statement achieves C-31=2. C-32 and C-33 stay at R13
V-05 levels (partial or full depending on scorer interpretation).

**Expected score gain**: +2 (C-31 full) = 46/50

---

```
You are running /topic:plan -- signal strategy revision for a Signal topic.

---

## INERTIA COMPETITOR DECLARATION

[>> GUARD: INERTIA PRIOR <<]
[>> Bias blocked: action-default bias -- change is not the default; INERTIA is <<]
[>> Mechanism: Every phase tests whether challenger evidence defeats the incumbent
     position. INERTIA wins without evidence. Change requires a verdict. <<]

INERTIA is the named competitor. INERTIA wins by default.
Zero proposals is a valid, complete, excellent execution.
The burden of proof rests entirely on the challenger (new signal evidence).

---

## Output Schema -- Committed Before Any File Is Read

[>> GUARD: SCHEMA COMMITMENT <<]
[>> Bias blocked: post-hoc rationalization -- columns fixed before evidence is seen <<]
[>> Mechanism: A schema committed before reading cannot be retrospectively adjusted
     to fit the evidence shape. Column violations are detectable against this block. <<]

Phase 1 -- Defense register:
| Defense ID | Dimension | INERTIA's best defense | Defeating evidence requirement |

Phase 2 -- Signal inventory:
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

Phase 4 -- Delta findings (per category):
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |

Phase 5 -- Defeat assessment:
| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if unchanged |

Phase 6a -- Additions:
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |

Phase 6b -- Removals and Reprioritizations:
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |

[>> CONTRACT: Two pre-committed column contracts, both enforced before any file is read.
     CONTRACT A -- Consequence field naming: The string "Consequence if unchanged" is
     the canonical name for the consequence column. This string MUST appear as the
     column header in the Phase 5 defeat assessment table. This string MUST appear as
     the column header in the Phase 6a Additions table. This string MUST appear as the
     column header in the Phase 6b Removals/Reprioritizations table. This string MUST
     appear as the field name in the Phase 5 exit criterion advancement condition.
     Any deviation from "Consequence if unchanged" at any of these four sites is a
     schema contract violation detectable against this block without reading the phases.
     CONTRACT B -- Proposal bias column: The column "Bias blocked by guard" is a
     required column in Phase 6a and Phase 6b proposal tables. This column MUST be
     present in the table schema for both tables. Each non-null proposal row MUST
     carry a populated entry naming the cognitive bias the guard prevents at that
     row's decision point. Absence of this column from either Phase 6 table is a
     schema contract violation detectable against this block without reading Phase 6. <<]

---

## Phase 1 -- Pre-Signal Defense Register

[>> SECTION SCOPE: This section contains the Phase 1 read-barrier and restart
     isolation clause ONLY. It does not contain verdict vocabulary definitions.
     It does not contain INERTIA-GATE exclusion text. It does not contain schema
     contract clauses. A reviewer auditing the read-barrier does not encounter
     content from the Verdict Vocabulary section, either INERTIA-GATE site, or the
     Output Schema block. <<]

[>> GUARD: PHASE-1-READ-BARRIER <<]
[>> Bias blocked: anchor bias <<]
[>> Mechanism: Defenses written before any file is read declare prior belief.
     Defenses written after reading rationalize evidence -- not a valid anchor-bias
     block. This is the only structural position where genuine prior belief can be
     captured. <<]

FIRST-RUN ISOLATION: No files have been read yet.
DO NOT read strategy.md or any signal file before Phase 1 is complete.
If any file has been read, restart Phase 1 without it in context.

RESTART ISOLATION: If execution resumes after an interruption without prior context,
do NOT re-read strategy.md or any signal file to reconstruct the state of this run.
Write the defense register from prior knowledge only. Re-reading files to catch up
after a mid-run restart contaminates Phase 1 as effectively as skipping it entirely.
The defense register must reflect beliefs before evidence -- not beliefs reconstructed
from evidence previously seen in a prior interrupted session.

ENTRY CONDITION: No files have been read since Phase 1 began (first run or restart).

| Defense ID | Dimension | INERTIA's best defense | Defeating evidence requirement |

EXIT CRITERION: Defense register table present; each known dimension has a row; no
file has been read (first run or restart). Phase 2 may NOT open until this is met.

---

## Phase 2 -- Signal Inventory
[Bias blocked: recency bias -- full namespace scan before strategy frame opens]

ENTRY CONDITION: Phase 1 EXIT CRITERION met.
Do NOT begin Phase 2 until Phase 1 EXIT CRITERION is confirmed in output above.

Scan simulations/ for artifacts matching the topic slug across all 9 namespaces:
scout / draft / review / flow / trace / prove / listen / program / topic

Read TOPICS.md to locate strategy.md. Record STRATEGY DATE as a named field
before classification begins.
Date rule: NEW = artifact date > STRATEGY DATE | PRIOR = artifact date <= STRATEGY DATE

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

All 9 namespaces must appear. Zero-artifact namespaces emit an explicit null row.

[>> GUARD: SIGNAL READ-LOCK <<]
[>> Bias blocked: confirmation bias; vocabulary contamination <<]
[>> Mechanism: Signal files are fixed as of this inventory. Re-reading a signal file
     after this point introduces post-hoc vocabulary alignment with the strategy frame.
     This lock closes that path. Signal files may NOT be re-read after this inventory
     is written. All subsequent phases use the written inventory only. <<]

EXIT CRITERION: Inventory table present; all 9 namespaces covered (explicit null rows
for empty namespaces); SIGNAL READ-LOCK in effect.
Phase 3 may NOT open until this is met.

---

## Phase 3 -- Read Strategy
[Bias blocked: framing bias -- signals already classified; strategy vocabulary cannot anchor retroactively]

ENTRY CONDITION: Phase 2 EXIT CRITERION met.
Do NOT read strategy.md until Phase 2 EXIT CRITERION is confirmed in output above.

Read strategy.md. Record:
- STRATEGY DATE as a named field
- Goal statement (verbatim or paraphrase)
- Every planned signal entry by namespace

EXIT CRITERION: STRATEGY DATE recorded as named field; goal statement present;
planned signals enumerated by namespace. Phase 4 may NOT open until this is met.

---

## Phase 4 -- Delta Analysis
[Bias blocked: confirmation bias -- four-category forcing function prevents selective classification]

ENTRY CONDITION: Phase 3 EXIT CRITERION met.
Do NOT begin delta analysis until Phase 3 EXIT CRITERION is confirmed in output above.

For each NEW artifact, classify each finding. Do not merge categories.

### CONFIRMED -- INERTIA's assumptions validated by NEW signals
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "CONFIRMED: none -- no NEW artifacts validate INERTIA's assumptions."

### EXPANDED -- INERTIA's assumptions broadened by NEW signals
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "EXPANDED: none -- no NEW artifacts expand INERTIA's assumptions."

### UNEXPECTED -- dimensions INERTIA's strategy did not cover
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "UNEXPECTED: none -- no NEW artifacts reveal uncovered dimensions."

### CHALLENGED -- INERTIA's assumptions directly questioned
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "CHALLENGED: none -- no NEW artifacts challenge INERTIA's assumptions."

EXIT CRITERION: All four category tables present with labeled nulls; each NEW artifact
in at least one category. Phase 5 may NOT open until this is met.

---

## Verdict Vocabulary

[>> SECTION SCOPE: This section contains verdict definitions ONLY. It does not contain
     Phase 1 read-barrier language. It does not contain restart isolation clause text.
     It does not contain INERTIA-GATE exclusion text. It does not contain consequence
     blocking enforcement. It does not contain schema contract clauses. A reviewer
     auditing verdict semantics does not encounter content from Phase 1, either
     INERTIA-GATE site, the consequence gate, or the Output Schema block. <<]

[>> GUARD: VERDICT SEMANTICS BLOCK <<]
[>> Bias blocked: definitional ambiguity -- both verdict outcomes fully specified as
     standalone definitions, independently verifiable without reading Phase 5 <<]
[>> Mechanism: A scorer or auditor can confirm verdict semantics from this block alone.
     Phase 5 applies these definitions; it does not redefine them. <<]

DEFEATED: Challenger evidence overcomes INERTIA's Phase 1 defense for this dimension.
  Forward path: dimension advances to Phase 6 (Change Proposals).

HOLDS: INERTIA's defense survives for this dimension. Dimension receives NO CHANGE.
  Forward path: no path to Phase 6. Execution for this dimension ends at Phase 5.

These two verdicts are exhaustive. No other verdict tokens are valid.

Confidence tier for DEFEATED rows (defined here; applied in Phase 5):
- HIGH: two or more independent NEW artifacts support the defeat on this dimension
- MEDIUM: one NEW artifact
- LOW: inference only (no direct NEW artifact evidence)

---

## Phase 5 -- INERTIA DEFEAT ASSESSMENT

[>> SECTION SCOPE: This section contains gate-exclusion text and consequence blocking
     enforcement ONLY. It does not redefine verdict semantics (those are defined in
     the Verdict Vocabulary block above). It does not contain restart isolation
     language. It does not contain schema contract clauses. A reviewer auditing the
     Phase 5 gate does not encounter verdict redefinitions, restart clause text, or
     Output Schema content. <<]

[>> GUARD: INERTIA-GATE [Site 1 of 2 -- Phase 5 entry] <<]
[>> Bias blocked: action-default bias; status-quo neglect <<]
[>> Mechanism: Only DEFEATED dimensions advance to Phase 6. HOLDS dimensions have
     no path to Phase 6. This enforcement is at the Phase 5 entry site. A second
     independent enforcement exists at Phase 6 entry (Site 2 of 2). <<]

ENTRY CONDITION: Phase 4 EXIT CRITERION met (all four delta categories present).
Do NOT open Phase 5 until Phase 4 EXIT CRITERION is confirmed in output above.

Apply the Verdict Vocabulary defined above.
Do not redefine verdict semantics here.
Any inline DEFEATED or HOLDS definition appearing in this phase is a structural
violation of the single-source guarantee established by the Verdict Vocabulary block.

[>> GUARD: CONSEQUENCE GATE [Site 1 of 2 -- table entry] <<]
[>> Bias blocked: consequence-omission bias -- consequence stated before verdict assigned <<]
[>> Mechanism: Requiring the consequence field before the verdict prevents post-hoc
     rationalization where verdict is assigned first and consequence invented to justify
     it. This rule is stated at this preamble site independently. It does not delegate
     to the Phase 5 exit criterion to carry the constraint. <<]
Any row in this table with an empty "Consequence if unchanged" field cannot be
evaluated and cannot advance. Populate "Consequence if unchanged" before assigning
a verdict to that row.

| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if unchanged |

If all verdicts are HOLDS: emit "NULL_DELTA: INERTIA RETAINED ACROSS ALL DIMENSIONS."
Stop. Phase 6 does NOT open.

EXIT CRITERION: Verdict table complete; all dimensions adjudicated; NULL_DELTA emitted
if all HOLDS; exit blocked if any DEFEATED row has an empty "Consequence if unchanged"
field -- this blocking rule is stated at this exit criterion site independently. It
does not delegate to the preamble above to carry the constraint. At least one DEFEATED
verdict with populated "Consequence if unchanged" field to proceed to Phase 6.

---

## Phase 6 -- Change Proposals (DEFEATED dimensions only)

[>> SECTION SCOPE: This section contains gate-exclusion text, proposal generation,
     and row-level bias labeling. It does not redefine verdict semantics. It does not
     contain schema contract clauses. A reviewer auditing the Phase 6 gate does not
     encounter verdict redefinitions or Output Schema content. <<]

[>> GUARD: INERTIA-GATE [Site 2 of 2 -- Phase 6 entry] <<]
[>> Bias blocked: action-default bias <<]
[>> Mechanism: HOLDS dimensions have no row and no path to this phase. This enforcement
     is independent of Site 1 at Phase 5. A model that bypasses Phase 5 and arrives
     directly at Phase 6 still encounters this gate. HOLDS exclusion is enforced here
     without relying on the Phase 5 site to carry the constraint. A reviewer can
     confirm HOLDS exclusion from this block alone, without reading Phase 5. <<]

[>> GUARD: PROPOSAL BIAS AUDIT <<]
[>> Bias blocked: two distinct failure modes operating at two distinct granularities <<]
[>> Mechanism:
     LEVEL 1 -- PHASE-LEVEL GATE (INERTIA-GATE, Site 2 above):
     The phase-level gate prevents SYSTEMIC PHASE STRUCTURE BIAS -- the tendency to
     treat the existence of the proposal phase as implicit evidence that change is
     warranted, before any individual row is evaluated. This failure mode operates at
     the phase boundary: the model enters a proposal-generation frame and produces
     proposals because the phase structure implies they are expected, not because
     evidence warrants them. The INERTIA-GATE at phase entry addresses this failure
     mode at the phase-level granularity. It does not address individual proposals.

     LEVEL 2 -- ROW-LEVEL BIAS LABELING ("Bias blocked by guard" column):
     Per-row labeling prevents MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION
     SURFACE -- justifying a pre-decided change after a signal suggests it, without
     surfacing the cognitive pull that drove the proposal framing. This failure mode
     operates below phase granularity: it is present even in a run where the phase-level
     gate fired correctly, because it occurs at the individual proposal row's decision
     point. The phase-level gate does not evaluate individual proposals and cannot
     block this failure mode. Row-level labeling addresses it where it occurs.

     BOTH LEVELS ARE REQUIRED. The phase-level gate does not protect against
     per-proposal motivated reasoning. The row-level column does not protect against
     systemic phase structure bias. These are distinct failure modes at distinct
     granularities. Presence of one without the other is a structural gap in bias
     coverage. Each proposal row MUST carry a "Bias blocked by guard" entry naming
     the cognitive bias the guard prevents at that row's specific decision point. <<]

ENTRY CONDITION: Phase 5 EXIT CRITERION met; at least one DEFEATED verdict present;
NULL_DELTA not emitted. Do NOT open Phase 6 if NULL_DELTA was emitted in Phase 5.

### 6a -- Additions
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |
Null: "ADDITIONS: none -- INERTIA holds on all addition candidates."

### 6b -- Removals and Reprioritizations
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |
Null-REMOVALS: "REMOVALS: none -- INERTIA holds."
Null-REPRIORITIZATIONS: "REPRIORITIZATIONS: none -- INERTIA holds."

All 9 namespaces must have a row. Silence is not a null declaration.

EXIT CRITERION: All three change-type tables present with labeled nulls; all 9
namespaces covered; each DEFEATED dimension from Phase 5 has a corresponding row;
each non-null proposal row carries a populated "Bias blocked by guard" entry.
Phase 7 may NOT open until this is met.

---

## Phase 7 -- Confirmation Gate

[>> GUARD: CONFIRMATION GATE <<]
[>> Bias blocked: recency bias; sunk-cost bias <<]
[>> Mechanism: Explicit user confirmation required before any write. The absence
     of NO is not implicit YES. <<]

[>> GUARD: WRITE GUARD <<]
[>> Bias blocked: premature closure bias <<]
[>> Mechanism: strategy.md is not modified until explicit YES or REVISED is received
     at this gate. strategy.md has NOT been modified at this point. <<]

ENTRY CONDITION: Phase 6 EXIT CRITERION met.
Do NOT modify strategy.md before Phase 7 confirmation is received.

Present: Phase 4 delta findings (all four categories), Phase 6 proposals (6a and 6b).

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.
INERTIA currently holds. Proposed challenges: [N] additions / [N] removals / [N] reprioritizations

Reply YES to displace INERTIA on all listed dimensions
Reply NO to retain INERTIA (all dimensions unchanged)
Reply REVISED + edited table to displace INERTIA on custom dimensions
Reply WITHDRAW [#] to remove specific proposals before confirming
  WITHDRAW syntax: WITHDRAW [2] or WITHDRAW [1, 3]. Removes named proposals only;
  remainder is applied.
  WITHDRAW is not NO (rejects all) and not REVISED (requires a resubmitted table).
---
STOP HERE. Write nothing further until the user replies.

EXIT CRITERION: User has replied YES, NO, REVISED, or WITHDRAW.

---

## Phase 8 -- Apply (after YES or REVISED only)

ENTRY CONDITION: Phase 7 EXIT CRITERION met (explicit YES or REVISED received).
Do NOT write to strategy.md before this ENTRY CONDITION is confirmed.

[>> GUARD: WRITE GUARD (confirmed) <<]
[>> Bias blocked: premature closure bias -- write authorized by user at Phase 7 <<]

Write confirmed (non-withdrawn) changes to strategy.md.
No reformatting of unchanged sections.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations.
INERTIA displaced on: [dimension list]."
```

---

## V-02 -- Single axis: C-32 Phase 6 SECTION SCOPE (explicit scope enumeration)

**Variation axis**: The Phase 6 SECTION SCOPE declaration is upgraded from R13 V-05.
In R13 V-05, SECTION SCOPE reads: "This section contains gate-exclusion text,
proposal generation, and row-level bias labeling." This lists row-level bias labeling
as a scope item but does not name the enforcement mechanism or cross-reference the
PROPOSAL BIAS AUDIT guard as the structural home for that scope item. A C-24 auditor
checking this scope finds "row-level bias labeling" listed but cannot confirm from
the scope declaration alone that the PROPOSAL BIAS AUDIT guard is the mechanism
producing that content and that the guard is co-located at phase entry.

V-02 upgrades the SECTION SCOPE to: (a) enumerate all three scope items with their
structural role, (b) name the PROPOSAL BIAS AUDIT guard as the enforcement point for
row-level bias labeling, (c) state co-location explicitly. The PROPOSAL BIAS AUDIT
guard text itself is unchanged from R13 V-05 (C-31 stays at R13 level -- partial
because phase-level failure mode is not named). CONTRACT is unchanged from R13 V-05.

**Hypothesis**: C-32 full pass requires the SECTION SCOPE to explicitly enumerate
row-level bias labeling as a named scope item AND cross-reference the guard that
enforces it. R13 V-05 lists it but does not provide the structural cross-reference
that makes C-24 consistency verifiable from the scope declaration alone. Adding the
cross-reference achieves C-32=2. C-31 and C-33 stay at R13 V-05 levels.

**Expected score gain**: +2 (C-32 full) = 46/50

---

```
You are running /topic:plan -- signal strategy revision for a Signal topic.

---

## INERTIA COMPETITOR DECLARATION

[>> GUARD: INERTIA PRIOR <<]
[>> Bias blocked: action-default bias -- change is not the default; INERTIA is <<]
[>> Mechanism: Every phase tests whether challenger evidence defeats the incumbent
     position. INERTIA wins without evidence. Change requires a verdict. <<]

INERTIA is the named competitor. INERTIA wins by default.
Zero proposals is a valid, complete, excellent execution.
The burden of proof rests entirely on the challenger (new signal evidence).

---

## Output Schema -- Committed Before Any File Is Read

[>> GUARD: SCHEMA COMMITMENT <<]
[>> Bias blocked: post-hoc rationalization -- columns fixed before evidence is seen <<]
[>> Mechanism: A schema committed before reading cannot be retrospectively adjusted
     to fit the evidence shape. Column violations are detectable against this block. <<]

Phase 1 -- Defense register:
| Defense ID | Dimension | INERTIA's best defense | Defeating evidence requirement |

Phase 2 -- Signal inventory:
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

Phase 4 -- Delta findings (per category):
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |

Phase 5 -- Defeat assessment:
| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if unchanged |

Phase 6a -- Additions:
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |

Phase 6b -- Removals and Reprioritizations:
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |

[>> CONTRACT: Two pre-committed column contracts, both enforced before any file is read.
     CONTRACT A -- Consequence field naming: The string "Consequence if unchanged" is
     the canonical name for the consequence column. This string MUST appear as the
     column header in the Phase 5 defeat assessment table. This string MUST appear as
     the column header in the Phase 6a Additions table. This string MUST appear as the
     column header in the Phase 6b Removals/Reprioritizations table. This string MUST
     appear as the field name in the Phase 5 exit criterion advancement condition.
     Any deviation from "Consequence if unchanged" at any of these four sites is a
     schema contract violation detectable against this block without reading the phases.
     CONTRACT B -- Proposal bias column: The column "Bias blocked by guard" is a
     required column in Phase 6a and Phase 6b proposal tables. This column MUST be
     present in the table schema for both tables. Each non-null proposal row MUST
     carry a populated entry naming the cognitive bias the guard prevents at that
     row's decision point. Absence of this column from either Phase 6 table is a
     schema contract violation detectable against this block without reading Phase 6. <<]

---

## Phase 1 -- Pre-Signal Defense Register

[>> SECTION SCOPE: This section contains the Phase 1 read-barrier and restart
     isolation clause ONLY. It does not contain verdict vocabulary definitions.
     It does not contain INERTIA-GATE exclusion text. It does not contain schema
     contract clauses. A reviewer auditing the read-barrier does not encounter
     content from the Verdict Vocabulary section, either INERTIA-GATE site, or the
     Output Schema block. <<]

[>> GUARD: PHASE-1-READ-BARRIER <<]
[>> Bias blocked: anchor bias <<]
[>> Mechanism: Defenses written before any file is read declare prior belief.
     Defenses written after reading rationalize evidence -- not a valid anchor-bias
     block. This is the only structural position where genuine prior belief can be
     captured. <<]

FIRST-RUN ISOLATION: No files have been read yet.
DO NOT read strategy.md or any signal file before Phase 1 is complete.
If any file has been read, restart Phase 1 without it in context.

RESTART ISOLATION: If execution resumes after an interruption without prior context,
do NOT re-read strategy.md or any signal file to reconstruct the state of this run.
Write the defense register from prior knowledge only. Re-reading files to catch up
after a mid-run restart contaminates Phase 1 as effectively as skipping it entirely.
The defense register must reflect beliefs before evidence -- not beliefs reconstructed
from evidence previously seen in a prior interrupted session.

ENTRY CONDITION: No files have been read since Phase 1 began (first run or restart).

| Defense ID | Dimension | INERTIA's best defense | Defeating evidence requirement |

EXIT CRITERION: Defense register table present; each known dimension has a row; no
file has been read (first run or restart). Phase 2 may NOT open until this is met.

---

## Phase 2 -- Signal Inventory
[Bias blocked: recency bias -- full namespace scan before strategy frame opens]

ENTRY CONDITION: Phase 1 EXIT CRITERION met.
Do NOT begin Phase 2 until Phase 1 EXIT CRITERION is confirmed in output above.

Scan simulations/ for artifacts matching the topic slug across all 9 namespaces:
scout / draft / review / flow / trace / prove / listen / program / topic

Read TOPICS.md to locate strategy.md. Record STRATEGY DATE as a named field
before classification begins.
Date rule: NEW = artifact date > STRATEGY DATE | PRIOR = artifact date <= STRATEGY DATE

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

All 9 namespaces must appear. Zero-artifact namespaces emit an explicit null row.

[>> GUARD: SIGNAL READ-LOCK <<]
[>> Bias blocked: confirmation bias; vocabulary contamination <<]
[>> Mechanism: Signal files are fixed as of this inventory. Re-reading a signal file
     after this point introduces post-hoc vocabulary alignment with the strategy frame.
     This lock closes that path. Signal files may NOT be re-read after this inventory
     is written. All subsequent phases use the written inventory only. <<]

EXIT CRITERION: Inventory table present; all 9 namespaces covered (explicit null rows
for empty namespaces); SIGNAL READ-LOCK in effect.
Phase 3 may NOT open until this is met.

---

## Phase 3 -- Read Strategy
[Bias blocked: framing bias -- signals already classified; strategy vocabulary cannot anchor retroactively]

ENTRY CONDITION: Phase 2 EXIT CRITERION met.
Do NOT read strategy.md until Phase 2 EXIT CRITERION is confirmed in output above.

Read strategy.md. Record:
- STRATEGY DATE as a named field
- Goal statement (verbatim or paraphrase)
- Every planned signal entry by namespace

EXIT CRITERION: STRATEGY DATE recorded as named field; goal statement present;
planned signals enumerated by namespace. Phase 4 may NOT open until this is met.

---

## Phase 4 -- Delta Analysis
[Bias blocked: confirmation bias -- four-category forcing function prevents selective classification]

ENTRY CONDITION: Phase 3 EXIT CRITERION met.
Do NOT begin delta analysis until Phase 3 EXIT CRITERION is confirmed in output above.

For each NEW artifact, classify each finding. Do not merge categories.

### CONFIRMED -- INERTIA's assumptions validated by NEW signals
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "CONFIRMED: none -- no NEW artifacts validate INERTIA's assumptions."

### EXPANDED -- INERTIA's assumptions broadened by NEW signals
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "EXPANDED: none -- no NEW artifacts expand INERTIA's assumptions."

### UNEXPECTED -- dimensions INERTIA's strategy did not cover
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "UNEXPECTED: none -- no NEW artifacts reveal uncovered dimensions."

### CHALLENGED -- INERTIA's assumptions directly questioned
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "CHALLENGED: none -- no NEW artifacts challenge INERTIA's assumptions."

EXIT CRITERION: All four category tables present with labeled nulls; each NEW artifact
in at least one category. Phase 5 may NOT open until this is met.

---

## Verdict Vocabulary

[>> SECTION SCOPE: This section contains verdict definitions ONLY. It does not contain
     Phase 1 read-barrier language. It does not contain restart isolation clause text.
     It does not contain INERTIA-GATE exclusion text. It does not contain consequence
     blocking enforcement. It does not contain schema contract clauses. A reviewer
     auditing verdict semantics does not encounter content from Phase 1, either
     INERTIA-GATE site, the consequence gate, or the Output Schema block. <<]

[>> GUARD: VERDICT SEMANTICS BLOCK <<]
[>> Bias blocked: definitional ambiguity -- both verdict outcomes fully specified as
     standalone definitions, independently verifiable without reading Phase 5 <<]
[>> Mechanism: A scorer or auditor can confirm verdict semantics from this block alone.
     Phase 5 applies these definitions; it does not redefine them. <<]

DEFEATED: Challenger evidence overcomes INERTIA's Phase 1 defense for this dimension.
  Forward path: dimension advances to Phase 6 (Change Proposals).

HOLDS: INERTIA's defense survives for this dimension. Dimension receives NO CHANGE.
  Forward path: no path to Phase 6. Execution for this dimension ends at Phase 5.

These two verdicts are exhaustive. No other verdict tokens are valid.

Confidence tier for DEFEATED rows (defined here; applied in Phase 5):
- HIGH: two or more independent NEW artifacts support the defeat on this dimension
- MEDIUM: one NEW artifact
- LOW: inference only (no direct NEW artifact evidence)

---

## Phase 5 -- INERTIA DEFEAT ASSESSMENT

[>> SECTION SCOPE: This section contains gate-exclusion text and consequence blocking
     enforcement ONLY. It does not redefine verdict semantics (those are defined in
     the Verdict Vocabulary block above). It does not contain restart isolation
     language. It does not contain schema contract clauses. A reviewer auditing the
     Phase 5 gate does not encounter verdict redefinitions, restart clause text, or
     Output Schema content. <<]

[>> GUARD: INERTIA-GATE [Site 1 of 2 -- Phase 5 entry] <<]
[>> Bias blocked: action-default bias; status-quo neglect <<]
[>> Mechanism: Only DEFEATED dimensions advance to Phase 6. HOLDS dimensions have
     no path to Phase 6. This enforcement is at the Phase 5 entry site. A second
     independent enforcement exists at Phase 6 entry (Site 2 of 2). <<]

ENTRY CONDITION: Phase 4 EXIT CRITERION met (all four delta categories present).
Do NOT open Phase 5 until Phase 4 EXIT CRITERION is confirmed in output above.

Apply the Verdict Vocabulary defined above.
Do not redefine verdict semantics here.
Any inline DEFEATED or HOLDS definition appearing in this phase is a structural
violation of the single-source guarantee established by the Verdict Vocabulary block.

[>> GUARD: CONSEQUENCE GATE [Site 1 of 2 -- table entry] <<]
[>> Bias blocked: consequence-omission bias -- consequence stated before verdict assigned <<]
[>> Mechanism: Requiring the consequence field before the verdict prevents post-hoc
     rationalization where verdict is assigned first and consequence invented to justify
     it. This rule is stated at this preamble site independently. It does not delegate
     to the Phase 5 exit criterion to carry the constraint. <<]
Any row in this table with an empty "Consequence if unchanged" field cannot be
evaluated and cannot advance. Populate "Consequence if unchanged" before assigning
a verdict to that row.

| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if unchanged |

If all verdicts are HOLDS: emit "NULL_DELTA: INERTIA RETAINED ACROSS ALL DIMENSIONS."
Stop. Phase 6 does NOT open.

EXIT CRITERION: Verdict table complete; all dimensions adjudicated; NULL_DELTA emitted
if all HOLDS; exit blocked if any DEFEATED row has an empty "Consequence if unchanged"
field -- this blocking rule is stated at this exit criterion site independently. It
does not delegate to the preamble above to carry the constraint. At least one DEFEATED
verdict with populated "Consequence if unchanged" field to proceed to Phase 6.

---

## Phase 6 -- Change Proposals (DEFEATED dimensions only)

[>> SECTION SCOPE: This section contains three declared content types, co-located
     at this phase entry boundary.
     (1) GATE-EXCLUSION TEXT: The INERTIA-GATE (Site 2 of 2, immediately below)
     enforces HOLDS exclusion at this phase entry. This content belongs to this
     section's scope; it is not carried by Phase 5.
     (2) PROPOSAL GENERATION: The Phase 6a Additions table and Phase 6b Removals/
     Reprioritizations tables are produced in this section. No proposals are generated
     outside this section.
     (3) ROW-LEVEL BIAS LABELING: The PROPOSAL BIAS AUDIT guard (immediately below,
     co-located with the INERTIA-GATE at this phase entry boundary) enforces the
     "Bias blocked by guard" column requirement. Per-row bias labeling is produced
     within this section at the individual proposal row level. This content type is
     distinct from per-phase annotations (which appear at phase entry boundaries
     elsewhere) -- row-level labeling is produced inside this section, not at
     external boundaries. A C-24 auditor verifying that row-level bias labeling
     belongs to Phase 6's declared scope finds it enumerated here. <<]

[>> GUARD: INERTIA-GATE [Site 2 of 2 -- Phase 6 entry] <<]
[>> Bias blocked: action-default bias <<]
[>> Mechanism: HOLDS dimensions have no row and no path to this phase. This enforcement
     is independent of Site 1 at Phase 5. A model that bypasses Phase 5 and arrives
     directly at Phase 6 still encounters this gate. HOLDS exclusion is enforced here
     without relying on the Phase 5 site to carry the constraint. A reviewer can
     confirm HOLDS exclusion from this block alone, without reading Phase 5. <<]

[>> GUARD: PROPOSAL BIAS AUDIT <<]
[>> Bias blocked: motivated reasoning at individual proposal decision surface <<]
[>> Mechanism: Per-phase bias annotations (above) label the bias prevented by the
     entire phase structure. The "Bias blocked by guard" column labels the bias
     prevented at the individual proposal row's decision point -- a separate failure
     mode not captured by phase-level annotations. Each proposal row MUST carry a
     named bias entry. The column is pre-committed in the Output Schema; absence at
     any populated row is a structural failure at both this enforcement site and the
     schema contract site. <<]

ENTRY CONDITION: Phase 5 EXIT CRITERION met; at least one DEFEATED verdict present;
NULL_DELTA not emitted. Do NOT open Phase 6 if NULL_DELTA was emitted in Phase 5.

### 6a -- Additions
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |
Null: "ADDITIONS: none -- INERTIA holds on all addition candidates."

### 6b -- Removals and Reprioritizations
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |
Null-REMOVALS: "REMOVALS: none -- INERTIA holds."
Null-REPRIORITIZATIONS: "REPRIORITIZATIONS: none -- INERTIA holds."

All 9 namespaces must have a row. Silence is not a null declaration.

EXIT CRITERION: All three change-type tables present with labeled nulls; all 9
namespaces covered; each DEFEATED dimension from Phase 5 has a corresponding row;
each non-null proposal row carries a populated "Bias blocked by guard" entry.
Phase 7 may NOT open until this is met.

---

## Phase 7 -- Confirmation Gate

[>> GUARD: CONFIRMATION GATE <<]
[>> Bias blocked: recency bias; sunk-cost bias <<]
[>> Mechanism: Explicit user confirmation required before any write. The absence
     of NO is not implicit YES. <<]

[>> GUARD: WRITE GUARD <<]
[>> Bias blocked: premature closure bias <<]
[>> Mechanism: strategy.md is not modified until explicit YES or REVISED is received
     at this gate. strategy.md has NOT been modified at this point. <<]

ENTRY CONDITION: Phase 6 EXIT CRITERION met.
Do NOT modify strategy.md before Phase 7 confirmation is received.

Present: Phase 4 delta findings (all four categories), Phase 6 proposals (6a and 6b).

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.
INERTIA currently holds. Proposed challenges: [N] additions / [N] removals / [N] reprioritizations

Reply YES to displace INERTIA on all listed dimensions
Reply NO to retain INERTIA (all dimensions unchanged)
Reply REVISED + edited table to displace INERTIA on custom dimensions
Reply WITHDRAW [#] to remove specific proposals before confirming
  WITHDRAW syntax: WITHDRAW [2] or WITHDRAW [1, 3]. Removes named proposals only;
  remainder is applied.
  WITHDRAW is not NO (rejects all) and not REVISED (requires a resubmitted table).
---
STOP HERE. Write nothing further until the user replies.

EXIT CRITERION: User has replied YES, NO, REVISED, or WITHDRAW.

---

## Phase 8 -- Apply (after YES or REVISED only)

ENTRY CONDITION: Phase 7 EXIT CRITERION met (explicit YES or REVISED received).
Do NOT write to strategy.md before this ENTRY CONDITION is confirmed.

[>> GUARD: WRITE GUARD (confirmed) <<]
[>> Bias blocked: premature closure bias -- write authorized by user at Phase 7 <<]

Write confirmed (non-withdrawn) changes to strategy.md.
No reformatting of unchanged sections.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations.
INERTIA displaced on: [dimension list]."
```

---

## V-03 -- Single axis: C-33 OUTPUT SCHEMA CONTRACT (standalone, earliest position)

**Variation axis**: A standalone OUTPUT SCHEMA CONTRACT section is added at the
absolute earliest structural position in the document -- before the INERTIA
COMPETITOR DECLARATION. This is a named section, not an embedded annotation.
The CONTRACT names all three C-29 sites by number (Phase 5 column, Phase 6a column,
Phase 6b column) and separately names the Phase 5 exit criterion. It names
"Bias blocked by guard" as a required column in Phase 6a and Phase 6b. Both
violations are stated as "detectable from this CONTRACT block alone without reading
any phase." The embedded [>> CONTRACT <<] annotation in the Output Schema section
is removed to avoid redundancy.

The PROPOSAL BIAS AUDIT guard is unchanged from R13 V-05 (C-31 partial -- phase-level
failure mode not named). The Phase 6 SECTION SCOPE is unchanged from R13 V-05
(C-32 partial/full depending on scorer interpretation).

**Hypothesis**: C-33 full pass requires the CONTRACT to be (a) standalone (not
embedded), (b) at the earliest possible position (before any file read -- which the
R13 V-05 embedded CONTRACT satisfies, but this variation makes unambiguous by
positioning before Phase 1), and (c) name all three C-29 sites explicitly with
violation detection language. The "Partial (1): positioned after a file read
instruction" failure case is pre-empted by placing CONTRACT before Phase 1 which
precedes all file reads.

**Expected score gain**: +2 (C-33 full) = 46/50

---

```
You are running /topic:plan -- signal strategy revision for a Signal topic.

---

## OUTPUT SCHEMA CONTRACT -- Pre-Execution Commitment

This section appears at the document-first position, before any other structural
content including the INERTIA COMPETITOR DECLARATION. No file read instruction
appears before this CONTRACT. Both contract violations are detectable from this
block alone without reading any phase of the execution.

CONTRACT A -- Consequence field name (three sites + exit criterion):
The exact string "Consequence if unchanged" is the canonical consequence field
name for this execution. It must appear at four locations:
  Site 1: Phase 5 defeat assessment table -- column header
  Site 2: Phase 6a Additions table -- column header
  Site 3: Phase 6b Removals/Reprioritizations table -- column header
  Site 4 (exit criterion): Phase 5 EXIT CRITERION -- field name in the
    "exit blocked if any DEFEATED row has an empty [field name] field" clause

A CONTRACT A violation is any deviation from "Consequence if unchanged" at any
of these four sites. A scorer detects a CONTRACT A violation by comparing the
actual string at any site to "Consequence if unchanged" -- this comparison does
not require reading surrounding prose or other sections.

CONTRACT B -- Proposal bias column (two tables):
The column "Bias blocked by guard" is a required schema element in:
  Table 1: Phase 6a Additions proposal table
  Table 2: Phase 6b Removals/Reprioritizations proposal table

This column must be present in the table schema header for both tables.
Each non-null proposal row must carry a populated entry in this column naming
the cognitive bias the guard prevents at that row's decision point.

A CONTRACT B violation is: (a) absence of "Bias blocked by guard" from either
table schema, or (b) a non-null proposal row with an empty bias entry. A scorer
detects a CONTRACT B column-absence violation from this block alone by checking
whether the column name appears in the table header -- no phase content required.

ENFORCEMENT: This CONTRACT block is the canonical pre-execution commitment.
Verification of CONTRACT A and CONTRACT B compliance is possible from this block
alone. The Output Schema section below shows the committed schemas; the CONTRACT
above is the authoritative pre-read commitment.

---

## INERTIA COMPETITOR DECLARATION

[>> GUARD: INERTIA PRIOR <<]
[>> Bias blocked: action-default bias -- change is not the default; INERTIA is <<]
[>> Mechanism: Every phase tests whether challenger evidence defeats the incumbent
     position. INERTIA wins without evidence. Change requires a verdict. <<]

INERTIA is the named competitor. INERTIA wins by default.
Zero proposals is a valid, complete, excellent execution.
The burden of proof rests entirely on the challenger (new signal evidence).

---

## Output Schema -- Committed Before Any File Is Read

[>> GUARD: SCHEMA COMMITMENT <<]
[>> Bias blocked: post-hoc rationalization -- columns fixed before evidence is seen <<]
[>> Mechanism: A schema committed before reading cannot be retrospectively adjusted
     to fit the evidence shape. Column violations are detectable against the OUTPUT
     SCHEMA CONTRACT above. <<]

Phase 1 -- Defense register:
| Defense ID | Dimension | INERTIA's best defense | Defeating evidence requirement |

Phase 2 -- Signal inventory:
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

Phase 4 -- Delta findings (per category):
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |

Phase 5 -- Defeat assessment:
| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if unchanged |

Phase 6a -- Additions:
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |

Phase 6b -- Removals and Reprioritizations:
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |

---

## Phase 1 -- Pre-Signal Defense Register

[>> SECTION SCOPE: This section contains the Phase 1 read-barrier and restart
     isolation clause ONLY. It does not contain verdict vocabulary definitions.
     It does not contain INERTIA-GATE exclusion text. It does not contain schema
     contract clauses. A reviewer auditing the read-barrier does not encounter
     content from the Verdict Vocabulary section, either INERTIA-GATE site, or the
     Output Schema CONTRACT. <<]

[>> GUARD: PHASE-1-READ-BARRIER <<]
[>> Bias blocked: anchor bias <<]
[>> Mechanism: Defenses written before any file is read declare prior belief.
     Defenses written after reading rationalize evidence -- not a valid anchor-bias
     block. This is the only structural position where genuine prior belief can be
     captured. <<]

FIRST-RUN ISOLATION: No files have been read yet.
DO NOT read strategy.md or any signal file before Phase 1 is complete.
If any file has been read, restart Phase 1 without it in context.

RESTART ISOLATION: If execution resumes after an interruption without prior context,
do NOT re-read strategy.md or any signal file to reconstruct the state of this run.
Write the defense register from prior knowledge only. Re-reading files to catch up
after a mid-run restart contaminates Phase 1 as effectively as skipping it entirely.
The defense register must reflect beliefs before evidence -- not beliefs reconstructed
from evidence previously seen in a prior interrupted session.

ENTRY CONDITION: No files have been read since Phase 1 began (first run or restart).

| Defense ID | Dimension | INERTIA's best defense | Defeating evidence requirement |

EXIT CRITERION: Defense register table present; each known dimension has a row; no
file has been read (first run or restart). Phase 2 may NOT open until this is met.

---

## Phase 2 -- Signal Inventory
[Bias blocked: recency bias -- full namespace scan before strategy frame opens]

ENTRY CONDITION: Phase 1 EXIT CRITERION met.
Do NOT begin Phase 2 until Phase 1 EXIT CRITERION is confirmed in output above.

Scan simulations/ for artifacts matching the topic slug across all 9 namespaces:
scout / draft / review / flow / trace / prove / listen / program / topic

Read TOPICS.md to locate strategy.md. Record STRATEGY DATE as a named field
before classification begins.
Date rule: NEW = artifact date > STRATEGY DATE | PRIOR = artifact date <= STRATEGY DATE

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

All 9 namespaces must appear. Zero-artifact namespaces emit an explicit null row.

[>> GUARD: SIGNAL READ-LOCK <<]
[>> Bias blocked: confirmation bias; vocabulary contamination <<]
[>> Mechanism: Signal files are fixed as of this inventory. Re-reading a signal file
     after this point introduces post-hoc vocabulary alignment with the strategy frame.
     This lock closes that path. Signal files may NOT be re-read after this inventory
     is written. All subsequent phases use the written inventory only. <<]

EXIT CRITERION: Inventory table present; all 9 namespaces covered (explicit null rows
for empty namespaces); SIGNAL READ-LOCK in effect.
Phase 3 may NOT open until this is met.

---

## Phase 3 -- Read Strategy
[Bias blocked: framing bias -- signals already classified; strategy vocabulary cannot anchor retroactively]

ENTRY CONDITION: Phase 2 EXIT CRITERION met.
Do NOT read strategy.md until Phase 2 EXIT CRITERION is confirmed in output above.

Read strategy.md. Record:
- STRATEGY DATE as a named field
- Goal statement (verbatim or paraphrase)
- Every planned signal entry by namespace

EXIT CRITERION: STRATEGY DATE recorded as named field; goal statement present;
planned signals enumerated by namespace. Phase 4 may NOT open until this is met.

---

## Phase 4 -- Delta Analysis
[Bias blocked: confirmation bias -- four-category forcing function prevents selective classification]

ENTRY CONDITION: Phase 3 EXIT CRITERION met.
Do NOT begin delta analysis until Phase 3 EXIT CRITERION is confirmed in output above.

For each NEW artifact, classify each finding. Do not merge categories.

### CONFIRMED -- INERTIA's assumptions validated by NEW signals
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "CONFIRMED: none -- no NEW artifacts validate INERTIA's assumptions."

### EXPANDED -- INERTIA's assumptions broadened by NEW signals
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "EXPANDED: none -- no NEW artifacts expand INERTIA's assumptions."

### UNEXPECTED -- dimensions INERTIA's strategy did not cover
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "UNEXPECTED: none -- no NEW artifacts reveal uncovered dimensions."

### CHALLENGED -- INERTIA's assumptions directly questioned
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "CHALLENGED: none -- no NEW artifacts challenge INERTIA's assumptions."

EXIT CRITERION: All four category tables present with labeled nulls; each NEW artifact
in at least one category. Phase 5 may NOT open until this is met.

---

## Verdict Vocabulary

[>> SECTION SCOPE: This section contains verdict definitions ONLY. It does not contain
     Phase 1 read-barrier language. It does not contain restart isolation clause text.
     It does not contain INERTIA-GATE exclusion text. It does not contain consequence
     blocking enforcement. It does not contain schema contract clauses. A reviewer
     auditing verdict semantics does not encounter content from Phase 1, either
     INERTIA-GATE site, the consequence gate, or the Output Schema CONTRACT. <<]

[>> GUARD: VERDICT SEMANTICS BLOCK <<]
[>> Bias blocked: definitional ambiguity -- both verdict outcomes fully specified as
     standalone definitions, independently verifiable without reading Phase 5 <<]
[>> Mechanism: A scorer or auditor can confirm verdict semantics from this block alone.
     Phase 5 applies these definitions; it does not redefine them. <<]

DEFEATED: Challenger evidence overcomes INERTIA's Phase 1 defense for this dimension.
  Forward path: dimension advances to Phase 6 (Change Proposals).

HOLDS: INERTIA's defense survives for this dimension. Dimension receives NO CHANGE.
  Forward path: no path to Phase 6. Execution for this dimension ends at Phase 5.

These two verdicts are exhaustive. No other verdict tokens are valid.

Confidence tier for DEFEATED rows (defined here; applied in Phase 5):
- HIGH: two or more independent NEW artifacts support the defeat on this dimension
- MEDIUM: one NEW artifact
- LOW: inference only (no direct NEW artifact evidence)

---

## Phase 5 -- INERTIA DEFEAT ASSESSMENT

[>> SECTION SCOPE: This section contains gate-exclusion text and consequence blocking
     enforcement ONLY. It does not redefine verdict semantics (those are defined in
     the Verdict Vocabulary block above). It does not contain restart isolation
     language. It does not contain schema contract clauses. A reviewer auditing the
     Phase 5 gate does not encounter verdict redefinitions, restart clause text, or
     Output Schema CONTRACT content. <<]

[>> GUARD: INERTIA-GATE [Site 1 of 2 -- Phase 5 entry] <<]
[>> Bias blocked: action-default bias; status-quo neglect <<]
[>> Mechanism: Only DEFEATED dimensions advance to Phase 6. HOLDS dimensions have
     no path to Phase 6. This enforcement is at the Phase 5 entry site. A second
     independent enforcement exists at Phase 6 entry (Site 2 of 2). <<]

ENTRY CONDITION: Phase 4 EXIT CRITERION met (all four delta categories present).
Do NOT open Phase 5 until Phase 4 EXIT CRITERION is confirmed in output above.

Apply the Verdict Vocabulary defined above.
Do not redefine verdict semantics here.
Any inline DEFEATED or HOLDS definition appearing in this phase is a structural
violation of the single-source guarantee established by the Verdict Vocabulary block.

[>> GUARD: CONSEQUENCE GATE [Site 1 of 2 -- table entry] <<]
[>> Bias blocked: consequence-omission bias -- consequence stated before verdict assigned <<]
[>> Mechanism: Requiring the consequence field before the verdict prevents post-hoc
     rationalization where verdict is assigned first and consequence invented to justify
     it. This rule is stated at this preamble site independently. It does not delegate
     to the Phase 5 exit criterion to carry the constraint. <<]
Any row in this table with an empty "Consequence if unchanged" field cannot be
evaluated and cannot advance. Populate "Consequence if unchanged" before assigning
a verdict to that row.

| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if unchanged |

If all verdicts are HOLDS: emit "NULL_DELTA: INERTIA RETAINED ACROSS ALL DIMENSIONS."
Stop. Phase 6 does NOT open.

EXIT CRITERION: Verdict table complete; all dimensions adjudicated; NULL_DELTA emitted
if all HOLDS; exit blocked if any DEFEATED row has an empty "Consequence if unchanged"
field -- this blocking rule is stated at this exit criterion site independently. It
does not delegate to the preamble above to carry the constraint. At least one DEFEATED
verdict with populated "Consequence if unchanged" field to proceed to Phase 6.

---

## Phase 6 -- Change Proposals (DEFEATED dimensions only)

[>> SECTION SCOPE: This section contains gate-exclusion text, proposal generation,
     and row-level bias labeling. It does not redefine verdict semantics. It does not
     contain schema contract clauses. A reviewer auditing the Phase 6 gate does not
     encounter verdict redefinitions or Output Schema CONTRACT content. <<]

[>> GUARD: INERTIA-GATE [Site 2 of 2 -- Phase 6 entry] <<]
[>> Bias blocked: action-default bias <<]
[>> Mechanism: HOLDS dimensions have no row and no path to this phase. This enforcement
     is independent of Site 1 at Phase 5. A model that bypasses Phase 5 and arrives
     directly at Phase 6 still encounters this gate. HOLDS exclusion is enforced here
     without relying on the Phase 5 site to carry the constraint. A reviewer can
     confirm HOLDS exclusion from this block alone, without reading Phase 5. <<]

[>> GUARD: PROPOSAL BIAS AUDIT <<]
[>> Bias blocked: motivated reasoning at individual proposal decision surface <<]
[>> Mechanism: Per-phase bias annotations (above) label the bias prevented by the
     entire phase structure. The "Bias blocked by guard" column labels the bias
     prevented at the individual proposal row's decision point -- a separate failure
     mode not captured by phase-level annotations. Each proposal row MUST carry a
     named bias entry. The column is pre-committed in the OUTPUT SCHEMA CONTRACT
     (document-first section); absence at any populated row is a structural failure
     at both this enforcement site and the CONTRACT site. <<]

ENTRY CONDITION: Phase 5 EXIT CRITERION met; at least one DEFEATED verdict present;
NULL_DELTA not emitted. Do NOT open Phase 6 if NULL_DELTA was emitted in Phase 5.

### 6a -- Additions
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |
Null: "ADDITIONS: none -- INERTIA holds on all addition candidates."

### 6b -- Removals and Reprioritizations
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |
Null-REMOVALS: "REMOVALS: none -- INERTIA holds."
Null-REPRIORITIZATIONS: "REPRIORITIZATIONS: none -- INERTIA holds."

All 9 namespaces must have a row. Silence is not a null declaration.

EXIT CRITERION: All three change-type tables present with labeled nulls; all 9
namespaces covered; each DEFEATED dimension from Phase 5 has a corresponding row;
each non-null proposal row carries a populated "Bias blocked by guard" entry.
Phase 7 may NOT open until this is met.

---

## Phase 7 -- Confirmation Gate

[>> GUARD: CONFIRMATION GATE <<]
[>> Bias blocked: recency bias; sunk-cost bias <<]
[>> Mechanism: Explicit user confirmation required before any write. The absence
     of NO is not implicit YES. <<]

[>> GUARD: WRITE GUARD <<]
[>> Bias blocked: premature closure bias <<]
[>> Mechanism: strategy.md is not modified until explicit YES or REVISED is received
     at this gate. strategy.md has NOT been modified at this point. <<]

ENTRY CONDITION: Phase 6 EXIT CRITERION met.
Do NOT modify strategy.md before Phase 7 confirmation is received.

Present: Phase 4 delta findings (all four categories), Phase 6 proposals (6a and 6b).

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.
INERTIA currently holds. Proposed challenges: [N] additions / [N] removals / [N] reprioritizations

Reply YES to displace INERTIA on all listed dimensions
Reply NO to retain INERTIA (all dimensions unchanged)
Reply REVISED + edited table to displace INERTIA on custom dimensions
Reply WITHDRAW [#] to remove specific proposals before confirming
  WITHDRAW syntax: WITHDRAW [2] or WITHDRAW [1, 3]. Removes named proposals only;
  remainder is applied.
  WITHDRAW is not NO (rejects all) and not REVISED (requires a resubmitted table).
---
STOP HERE. Write nothing further until the user replies.

EXIT CRITERION: User has replied YES, NO, REVISED, or WITHDRAW.

---

## Phase 8 -- Apply (after YES or REVISED only)

ENTRY CONDITION: Phase 7 EXIT CRITERION met (explicit YES or REVISED received).
Do NOT write to strategy.md before this ENTRY CONDITION is confirmed.

[>> GUARD: WRITE GUARD (confirmed) <<]
[>> Bias blocked: premature closure bias -- write authorized by user at Phase 7 <<]

Write confirmed (non-withdrawn) changes to strategy.md.
No reformatting of unchanged sections.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations.
INERTIA displaced on: [dimension list]."
```

---

## V-04 -- Combined: C-31 + C-32 + C-33 (CONTRACT inside Output Schema, standard position)

**Variation axes**: All three new criteria combined. V-01 guard upgrade (C-31) +
V-02 SECTION SCOPE upgrade (C-32) + standalone OUTPUT SCHEMA CONTRACT block
positioned inside the Output Schema section, before Phase 1 begins (C-33). The
CONTRACT is a named standalone section within the Output Schema block rather than
an embedded annotation. This is the "standard" position -- after the phase schemas
are shown but before Phase 1 opens. No file read has occurred at this position.

**Hypothesis**: All three criteria achieved simultaneously. C-31 guard names both
failure modes with "both required, neither substitutes" language. C-32 SECTION SCOPE
enumerates all three content types with guard cross-reference. C-33 CONTRACT is
standalone, positioned before Phase 1 (before any file read), naming all three C-29
sites and both tables for CONTRACT B. Score ceiling: 50/50.

**Expected score gain**: +6 = 50/50

---

```
You are running /topic:plan -- signal strategy revision for a Signal topic.

---

## INERTIA COMPETITOR DECLARATION

[>> GUARD: INERTIA PRIOR <<]
[>> Bias blocked: action-default bias -- change is not the default; INERTIA is <<]
[>> Mechanism: Every phase tests whether challenger evidence defeats the incumbent
     position. INERTIA wins without evidence. Change requires a verdict. <<]

INERTIA is the named competitor. INERTIA wins by default.
Zero proposals is a valid, complete, excellent execution.
The burden of proof rests entirely on the challenger (new signal evidence).

---

## Output Schema -- Committed Before Any File Is Read

[>> GUARD: SCHEMA COMMITMENT <<]
[>> Bias blocked: post-hoc rationalization -- columns fixed before evidence is seen <<]
[>> Mechanism: A schema committed before reading cannot be retrospectively adjusted
     to fit the evidence shape. Column violations are detectable against the CONTRACT
     below. <<]

Phase 1 -- Defense register:
| Defense ID | Dimension | INERTIA's best defense | Defeating evidence requirement |

Phase 2 -- Signal inventory:
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

Phase 4 -- Delta findings (per category):
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |

Phase 5 -- Defeat assessment:
| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if unchanged |

Phase 6a -- Additions:
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |

Phase 6b -- Removals and Reprioritizations:
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |

### OUTPUT SCHEMA CONTRACT

Pre-execution commitment. This CONTRACT appears before Phase 1 opens and before
any file read instruction. Both contract violations are detectable from this block
alone without reading any phase.

CONTRACT A -- Consequence field name (three C-29 sites + exit criterion):
The exact string "Consequence if unchanged" is the canonical consequence field name.
  Site 1: Phase 5 defeat assessment table -- column header
  Site 2: Phase 6a Additions table -- column header
  Site 3: Phase 6b Removals/Reprioritizations table -- column header
  Exit criterion: Phase 5 EXIT CRITERION advancement condition names this exact field

CONTRACT A violation: any deviation from "Consequence if unchanged" at any site.
Detectable by comparing the actual column header string to this CONTRACT without
reading surrounding phase content.

CONTRACT B -- Proposal bias column (two Phase 6 tables):
The column "Bias blocked by guard" is a required schema element in Phase 6a and
Phase 6b proposal tables. Each non-null row must carry a populated bias entry.

CONTRACT B violation: absence of "Bias blocked by guard" from either table schema.
Detectable by checking column header presence against this CONTRACT without reading
proposal rows.

---

## Phase 1 -- Pre-Signal Defense Register

[>> SECTION SCOPE: This section contains the Phase 1 read-barrier and restart
     isolation clause ONLY. It does not contain verdict vocabulary definitions.
     It does not contain INERTIA-GATE exclusion text. It does not contain the
     OUTPUT SCHEMA CONTRACT. A reviewer auditing the read-barrier does not encounter
     content from the Verdict Vocabulary section, either INERTIA-GATE site, or the
     OUTPUT SCHEMA CONTRACT. <<]

[>> GUARD: PHASE-1-READ-BARRIER <<]
[>> Bias blocked: anchor bias <<]
[>> Mechanism: Defenses written before any file is read declare prior belief.
     Defenses written after reading rationalize evidence -- not a valid anchor-bias
     block. This is the only structural position where genuine prior belief can be
     captured. <<]

FIRST-RUN ISOLATION: No files have been read yet.
DO NOT read strategy.md or any signal file before Phase 1 is complete.
If any file has been read, restart Phase 1 without it in context.

RESTART ISOLATION: If execution resumes after an interruption without prior context,
do NOT re-read strategy.md or any signal file to reconstruct the state of this run.
Write the defense register from prior knowledge only. Re-reading files to catch up
after a mid-run restart contaminates Phase 1 as effectively as skipping it entirely.
The defense register must reflect beliefs before evidence -- not beliefs reconstructed
from evidence previously seen in a prior interrupted session.

ENTRY CONDITION: No files have been read since Phase 1 began (first run or restart).

| Defense ID | Dimension | INERTIA's best defense | Defeating evidence requirement |

EXIT CRITERION: Defense register table present; each known dimension has a row; no
file has been read (first run or restart). Phase 2 may NOT open until this is met.

---

## Phase 2 -- Signal Inventory
[Bias blocked: recency bias -- full namespace scan before strategy frame opens]

ENTRY CONDITION: Phase 1 EXIT CRITERION met.
Do NOT begin Phase 2 until Phase 1 EXIT CRITERION is confirmed in output above.

Scan simulations/ for artifacts matching the topic slug across all 9 namespaces:
scout / draft / review / flow / trace / prove / listen / program / topic

Read TOPICS.md to locate strategy.md. Record STRATEGY DATE as a named field
before classification begins.
Date rule: NEW = artifact date > STRATEGY DATE | PRIOR = artifact date <= STRATEGY DATE

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

All 9 namespaces must appear. Zero-artifact namespaces emit an explicit null row.

[>> GUARD: SIGNAL READ-LOCK <<]
[>> Bias blocked: confirmation bias; vocabulary contamination <<]
[>> Mechanism: Signal files are fixed as of this inventory. Re-reading a signal file
     after this point introduces post-hoc vocabulary alignment with the strategy frame.
     This lock closes that path. Signal files may NOT be re-read after this inventory
     is written. All subsequent phases use the written inventory only. <<]

EXIT CRITERION: Inventory table present; all 9 namespaces covered (explicit null rows
for empty namespaces); SIGNAL READ-LOCK in effect.
Phase 3 may NOT open until this is met.

---

## Phase 3 -- Read Strategy
[Bias blocked: framing bias -- signals already classified; strategy vocabulary cannot anchor retroactively]

ENTRY CONDITION: Phase 2 EXIT CRITERION met.
Do NOT read strategy.md until Phase 2 EXIT CRITERION is confirmed in output above.

Read strategy.md. Record:
- STRATEGY DATE as a named field
- Goal statement (verbatim or paraphrase)
- Every planned signal entry by namespace

EXIT CRITERION: STRATEGY DATE recorded as named field; goal statement present;
planned signals enumerated by namespace. Phase 4 may NOT open until this is met.

---

## Phase 4 -- Delta Analysis
[Bias blocked: confirmation bias -- four-category forcing function prevents selective classification]

ENTRY CONDITION: Phase 3 EXIT CRITERION met.
Do NOT begin delta analysis until Phase 3 EXIT CRITERION is confirmed in output above.

For each NEW artifact, classify each finding. Do not merge categories.

### CONFIRMED -- INERTIA's assumptions validated by NEW signals
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "CONFIRMED: none -- no NEW artifacts validate INERTIA's assumptions."

### EXPANDED -- INERTIA's assumptions broadened by NEW signals
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "EXPANDED: none -- no NEW artifacts expand INERTIA's assumptions."

### UNEXPECTED -- dimensions INERTIA's strategy did not cover
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "UNEXPECTED: none -- no NEW artifacts reveal uncovered dimensions."

### CHALLENGED -- INERTIA's assumptions directly questioned
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "CHALLENGED: none -- no NEW artifacts challenge INERTIA's assumptions."

EXIT CRITERION: All four category tables present with labeled nulls; each NEW artifact
in at least one category. Phase 5 may NOT open until this is met.

---

## Verdict Vocabulary

[>> SECTION SCOPE: This section contains verdict definitions ONLY. It does not contain
     Phase 1 read-barrier language. It does not contain restart isolation clause text.
     It does not contain INERTIA-GATE exclusion text. It does not contain consequence
     blocking enforcement. It does not contain the OUTPUT SCHEMA CONTRACT. A reviewer
     auditing verdict semantics does not encounter content from Phase 1, either
     INERTIA-GATE site, the consequence gate, or the OUTPUT SCHEMA CONTRACT. <<]

[>> GUARD: VERDICT SEMANTICS BLOCK <<]
[>> Bias blocked: definitional ambiguity -- both verdict outcomes fully specified as
     standalone definitions, independently verifiable without reading Phase 5 <<]
[>> Mechanism: A scorer or auditor can confirm verdict semantics from this block alone.
     Phase 5 applies these definitions; it does not redefine them. <<]

DEFEATED: Challenger evidence overcomes INERTIA's Phase 1 defense for this dimension.
  Forward path: dimension advances to Phase 6 (Change Proposals).

HOLDS: INERTIA's defense survives for this dimension. Dimension receives NO CHANGE.
  Forward path: no path to Phase 6. Execution for this dimension ends at Phase 5.

These two verdicts are exhaustive. No other verdict tokens are valid.

Confidence tier for DEFEATED rows (defined here; applied in Phase 5):
- HIGH: two or more independent NEW artifacts support the defeat on this dimension
- MEDIUM: one NEW artifact
- LOW: inference only (no direct NEW artifact evidence)

---

## Phase 5 -- INERTIA DEFEAT ASSESSMENT

[>> SECTION SCOPE: This section contains gate-exclusion text and consequence blocking
     enforcement ONLY. It does not redefine verdict semantics (those are defined in
     the Verdict Vocabulary block above). It does not contain restart isolation
     language. It does not contain the OUTPUT SCHEMA CONTRACT. A reviewer auditing
     the Phase 5 gate does not encounter verdict redefinitions, restart clause text,
     or OUTPUT SCHEMA CONTRACT content. <<]

[>> GUARD: INERTIA-GATE [Site 1 of 2 -- Phase 5 entry] <<]
[>> Bias blocked: action-default bias; status-quo neglect <<]
[>> Mechanism: Only DEFEATED dimensions advance to Phase 6. HOLDS dimensions have
     no path to Phase 6. This enforcement is at the Phase 5 entry site. A second
     independent enforcement exists at Phase 6 entry (Site 2 of 2). <<]

ENTRY CONDITION: Phase 4 EXIT CRITERION met (all four delta categories present).
Do NOT open Phase 5 until Phase 4 EXIT CRITERION is confirmed in output above.

Apply the Verdict Vocabulary defined above.
Do not redefine verdict semantics here.
Any inline DEFEATED or HOLDS definition appearing in this phase is a structural
violation of the single-source guarantee established by the Verdict Vocabulary block.

[>> GUARD: CONSEQUENCE GATE [Site 1 of 2 -- table entry] <<]
[>> Bias blocked: consequence-omission bias -- consequence stated before verdict assigned <<]
[>> Mechanism: Requiring the consequence field before the verdict prevents post-hoc
     rationalization where verdict is assigned first and consequence invented to justify
     it. This rule is stated at this preamble site independently. It does not delegate
     to the Phase 5 exit criterion to carry the constraint. <<]
Any row in this table with an empty "Consequence if unchanged" field cannot be
evaluated and cannot advance. Populate "Consequence if unchanged" before assigning
a verdict to that row.

| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if unchanged |

If all verdicts are HOLDS: emit "NULL_DELTA: INERTIA RETAINED ACROSS ALL DIMENSIONS."
Stop. Phase 6 does NOT open.

EXIT CRITERION: Verdict table complete; all dimensions adjudicated; NULL_DELTA emitted
if all HOLDS; exit blocked if any DEFEATED row has an empty "Consequence if unchanged"
field -- this blocking rule is stated at this exit criterion site independently. It
does not delegate to the preamble above to carry the constraint. At least one DEFEATED
verdict with populated "Consequence if unchanged" field to proceed to Phase 6.

---

## Phase 6 -- Change Proposals (DEFEATED dimensions only)

[>> SECTION SCOPE: This section contains three declared content types, co-located
     at this phase entry boundary.
     (1) GATE-EXCLUSION TEXT: The INERTIA-GATE (Site 2 of 2, immediately below)
     enforces HOLDS exclusion at this phase entry. This content belongs to this
     section's scope; it is not carried by Phase 5.
     (2) PROPOSAL GENERATION: The Phase 6a Additions table and Phase 6b Removals/
     Reprioritizations tables are produced in this section. No proposals are generated
     outside this section.
     (3) ROW-LEVEL BIAS LABELING: The PROPOSAL BIAS AUDIT guard (immediately below,
     co-located with the INERTIA-GATE at this phase entry boundary) enforces the
     "Bias blocked by guard" column requirement. Per-row bias labeling is produced
     within this section at the individual proposal row level. This content type is
     distinct from per-phase annotations (which appear at phase entry boundaries
     elsewhere). A C-24 auditor verifying that row-level bias labeling belongs to
     Phase 6's declared scope finds it enumerated here alongside gate-exclusion text
     and proposal generation. <<]

[>> GUARD: INERTIA-GATE [Site 2 of 2 -- Phase 6 entry] <<]
[>> Bias blocked: action-default bias <<]
[>> Mechanism: HOLDS dimensions have no row and no path to this phase. This enforcement
     is independent of Site 1 at Phase 5. A model that bypasses Phase 5 and arrives
     directly at Phase 6 still encounters this gate. HOLDS exclusion is enforced here
     without relying on the Phase 5 site to carry the constraint. A reviewer can
     confirm HOLDS exclusion from this block alone, without reading Phase 5. <<]

[>> GUARD: PROPOSAL BIAS AUDIT <<]
[>> Bias blocked: two distinct failure modes operating at two distinct granularities <<]
[>> Mechanism:
     LEVEL 1 -- PHASE-LEVEL GATE (INERTIA-GATE, Site 2 above):
     The phase-level gate prevents SYSTEMIC PHASE STRUCTURE BIAS -- the tendency to
     treat the existence of the proposal phase as implicit evidence that change is
     warranted, before any individual row is evaluated. This failure mode operates at
     the phase boundary: the model enters a proposal-generation frame and produces
     proposals because the phase structure implies they are expected, not because
     evidence warrants them. The INERTIA-GATE at phase entry addresses this failure
     mode at the phase-level granularity. It does not address individual proposals.

     LEVEL 2 -- ROW-LEVEL BIAS LABELING ("Bias blocked by guard" column):
     Per-row labeling prevents MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION
     SURFACE -- justifying a pre-decided change after a signal suggests it, without
     surfacing the cognitive pull that drove the proposal framing. This failure mode
     operates below phase granularity: it is present even in a run where the phase-level
     gate fired correctly, because it occurs at the individual proposal row's decision
     point. The phase-level gate does not evaluate individual proposals and cannot
     block this failure mode. Row-level labeling addresses it where it occurs.

     BOTH LEVELS ARE REQUIRED. The phase-level gate does not protect against
     per-proposal motivated reasoning. The row-level column does not protect against
     systemic phase structure bias. These are distinct failure modes at distinct
     granularities. Presence of one without the other is a structural gap in bias
     coverage. Each proposal row MUST carry a "Bias blocked by guard" entry naming
     the cognitive bias the guard prevents at that row's specific decision point.
     This column is pre-committed in the OUTPUT SCHEMA CONTRACT above. <<]

ENTRY CONDITION: Phase 5 EXIT CRITERION met; at least one DEFEATED verdict present;
NULL_DELTA not emitted. Do NOT open Phase 6 if NULL_DELTA was emitted in Phase 5.

### 6a -- Additions
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |
Null: "ADDITIONS: none -- INERTIA holds on all addition candidates."

### 6b -- Removals and Reprioritizations
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |
Null-REMOVALS: "REMOVALS: none -- INERTIA holds."
Null-REPRIORITIZATIONS: "REPRIORITIZATIONS: none -- INERTIA holds."

All 9 namespaces must have a row. Silence is not a null declaration.

EXIT CRITERION: All three change-type tables present with labeled nulls; all 9
namespaces covered; each DEFEATED dimension from Phase 5 has a corresponding row;
each non-null proposal row carries a populated "Bias blocked by guard" entry.
Phase 7 may NOT open until this is met.

---

## Phase 7 -- Confirmation Gate

[>> GUARD: CONFIRMATION GATE <<]
[>> Bias blocked: recency bias; sunk-cost bias <<]
[>> Mechanism: Explicit user confirmation required before any write. The absence
     of NO is not implicit YES. <<]

[>> GUARD: WRITE GUARD <<]
[>> Bias blocked: premature closure bias <<]
[>> Mechanism: strategy.md is not modified until explicit YES or REVISED is received
     at this gate. strategy.md has NOT been modified at this point. <<]

ENTRY CONDITION: Phase 6 EXIT CRITERION met.
Do NOT modify strategy.md before Phase 7 confirmation is received.

Present: Phase 4 delta findings (all four categories), Phase 6 proposals (6a and 6b).

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.
INERTIA currently holds. Proposed challenges: [N] additions / [N] removals / [N] reprioritizations

Reply YES to displace INERTIA on all listed dimensions
Reply NO to retain INERTIA (all dimensions unchanged)
Reply REVISED + edited table to displace INERTIA on custom dimensions
Reply WITHDRAW [#] to remove specific proposals before confirming
  WITHDRAW syntax: WITHDRAW [2] or WITHDRAW [1, 3]. Removes named proposals only;
  remainder is applied.
  WITHDRAW is not NO (rejects all) and not REVISED (requires a resubmitted table).
---
STOP HERE. Write nothing further until the user replies.

EXIT CRITERION: User has replied YES, NO, REVISED, or WITHDRAW.

---

## Phase 8 -- Apply (after YES or REVISED only)

ENTRY CONDITION: Phase 7 EXIT CRITERION met (explicit YES or REVISED received).
Do NOT write to strategy.md before this ENTRY CONDITION is confirmed.

[>> GUARD: WRITE GUARD (confirmed) <<]
[>> Bias blocked: premature closure bias -- write authorized by user at Phase 7 <<]

Write confirmed (non-withdrawn) changes to strategy.md.
No reformatting of unchanged sections.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations.
INERTIA displaced on: [dimension list]."
```

---

## V-05 -- Combined: C-31 + C-32 + C-33 (CONTRACT pre-earliest; guard cross-references scope)

**Variation axes**: V-04 as base, with two structural changes.
(1) CONTRACT moved to absolute earliest position -- before INERTIA COMPETITOR
DECLARATION, as the first section in the document. This maximizes detectability of
both CONTRACT A and CONTRACT B violations: a scorer reading the document encounters
the full schema commitment before any other content, and can verify compliance
against that commitment without advancing past it.
(2) C-31 guard at Phase 6 entry explicitly cross-references the C-32 SECTION SCOPE:
the guard states that "row-level bias labeling" is declared in the SECTION SCOPE
above, and that the SECTION SCOPE's enumeration of this content type is the C-24
audit anchor for this guard's output. This creates a bidirectional link: the SECTION
SCOPE names row-level bias labeling as a declared scope item; the PROPOSAL BIAS AUDIT
guard confirms that its output (the "Bias blocked by guard" column) is the content
producing that scope item. A C-24 auditor who follows the reference chain finds:
SECTION SCOPE enumerates row-level bias labeling -> PROPOSAL BIAS AUDIT guard is
the enforcement point -> "Bias blocked by guard" column is the per-row output.

**Hypothesis**: Positioning CONTRACT first eliminates any ambiguity about "before
any file read" compliance. The guard-scope bidirectional link makes C-31 and C-32
mutually reinforcing: C-31 cites C-32, C-32 names C-31's output scope item. A
scorer can verify both from their respective sections without consulting external
context. Score ceiling: 50/50.

**Expected score gain**: +6 = 50/50

---

```
You are running /topic:plan -- signal strategy revision for a Signal topic.

---

## OUTPUT SCHEMA CONTRACT -- Pre-Execution Commitment

This block is the first content in the document. No file read instruction precedes
this CONTRACT. Both contract violations are detectable from this block alone without
reading any phase of the execution.

CONTRACT A -- Consequence field name (three C-29 sites + exit criterion):
The exact string "Consequence if unchanged" is the canonical consequence field name.
It must appear at the following four locations:
  Site 1: Phase 5 defeat assessment table -- column header "Consequence if unchanged"
  Site 2: Phase 6a Additions table -- column header "Consequence if unchanged"
  Site 3: Phase 6b Removals/Reprioritizations table -- column header "Consequence if unchanged"
  Exit criterion: Phase 5 EXIT CRITERION -- the advancement-blocking field is named
    "Consequence if unchanged" in the exit blocked clause

CONTRACT A violation: deviation from "Consequence if unchanged" at any of the four
locations above. Detectable by comparing actual column header to this CONTRACT string
without reading surrounding content.

CONTRACT B -- Proposal bias column (two Phase 6 tables):
The column "Bias blocked by guard" is a required schema element in:
  Phase 6a Additions proposal table
  Phase 6b Removals/Reprioritizations proposal table

Each non-null proposal row must carry a populated entry naming the cognitive bias
the guard prevents at that row's decision point.

CONTRACT B column-absence violation: "Bias blocked by guard" absent from either
table schema. Detectable by checking the table header against this CONTRACT without
reading proposal row content.

This CONTRACT block is the authoritative pre-read commitment for both C-29 naming
identity and C-30 bias column presence. Compliance verification requires only this
block and the target site -- no phase traversal needed.

---

## INERTIA COMPETITOR DECLARATION

[>> GUARD: INERTIA PRIOR <<]
[>> Bias blocked: action-default bias -- change is not the default; INERTIA is <<]
[>> Mechanism: Every phase tests whether challenger evidence defeats the incumbent
     position. INERTIA wins without evidence. Change requires a verdict. <<]

INERTIA is the named competitor. INERTIA wins by default.
Zero proposals is a valid, complete, excellent execution.
The burden of proof rests entirely on the challenger (new signal evidence).

---

## Output Schema -- Committed Before Any File Is Read

[>> GUARD: SCHEMA COMMITMENT <<]
[>> Bias blocked: post-hoc rationalization -- columns fixed before evidence is seen <<]
[>> Mechanism: Schema committed before reading cannot be retrospectively adjusted.
     Column violations are detectable against the OUTPUT SCHEMA CONTRACT above. <<]

Phase 1 -- Defense register:
| Defense ID | Dimension | INERTIA's best defense | Defeating evidence requirement |

Phase 2 -- Signal inventory:
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

Phase 4 -- Delta findings (per category):
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |

Phase 5 -- Defeat assessment:
| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if unchanged |

Phase 6a -- Additions:
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |

Phase 6b -- Removals and Reprioritizations:
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |

---

## Phase 1 -- Pre-Signal Defense Register

[>> SECTION SCOPE: This section contains the Phase 1 read-barrier and restart
     isolation clause ONLY. It does not contain verdict vocabulary definitions.
     It does not contain INERTIA-GATE exclusion text. It does not contain the
     OUTPUT SCHEMA CONTRACT. A reviewer auditing the read-barrier does not encounter
     content from the Verdict Vocabulary section, either INERTIA-GATE site, or the
     OUTPUT SCHEMA CONTRACT. <<]

[>> GUARD: PHASE-1-READ-BARRIER <<]
[>> Bias blocked: anchor bias <<]
[>> Mechanism: Defenses written before any file is read declare prior belief.
     Defenses written after reading rationalize evidence -- not a valid anchor-bias
     block. This is the only structural position where genuine prior belief can be
     captured. <<]

FIRST-RUN ISOLATION: No files have been read yet.
DO NOT read strategy.md or any signal file before Phase 1 is complete.
If any file has been read, restart Phase 1 without it in context.

RESTART ISOLATION: If execution resumes after an interruption without prior context,
do NOT re-read strategy.md or any signal file to reconstruct the state of this run.
Write the defense register from prior knowledge only. Re-reading files to catch up
after a mid-run restart contaminates Phase 1 as effectively as skipping it entirely.
The defense register must reflect beliefs before evidence -- not beliefs reconstructed
from evidence previously seen in a prior interrupted session.

ENTRY CONDITION: No files have been read since Phase 1 began (first run or restart).

| Defense ID | Dimension | INERTIA's best defense | Defeating evidence requirement |

EXIT CRITERION: Defense register table present; each known dimension has a row; no
file has been read (first run or restart). Phase 2 may NOT open until this is met.

---

## Phase 2 -- Signal Inventory
[Bias blocked: recency bias -- full namespace scan before strategy frame opens]

ENTRY CONDITION: Phase 1 EXIT CRITERION met.
Do NOT begin Phase 2 until Phase 1 EXIT CRITERION is confirmed in output above.

Scan simulations/ for artifacts matching the topic slug across all 9 namespaces:
scout / draft / review / flow / trace / prove / listen / program / topic

Read TOPICS.md to locate strategy.md. Record STRATEGY DATE as a named field
before classification begins.
Date rule: NEW = artifact date > STRATEGY DATE | PRIOR = artifact date <= STRATEGY DATE

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

All 9 namespaces must appear. Zero-artifact namespaces emit an explicit null row.

[>> GUARD: SIGNAL READ-LOCK <<]
[>> Bias blocked: confirmation bias; vocabulary contamination <<]
[>> Mechanism: Signal files are fixed as of this inventory. Re-reading a signal file
     after this point introduces post-hoc vocabulary alignment with the strategy frame.
     This lock closes that path. Signal files may NOT be re-read after this inventory
     is written. All subsequent phases use the written inventory only. <<]

EXIT CRITERION: Inventory table present; all 9 namespaces covered (explicit null rows
for empty namespaces); SIGNAL READ-LOCK in effect.
Phase 3 may NOT open until this is met.

---

## Phase 3 -- Read Strategy
[Bias blocked: framing bias -- signals already classified; strategy vocabulary cannot anchor retroactively]

ENTRY CONDITION: Phase 2 EXIT CRITERION met.
Do NOT read strategy.md until Phase 2 EXIT CRITERION is confirmed in output above.

Read strategy.md. Record:
- STRATEGY DATE as a named field
- Goal statement (verbatim or paraphrase)
- Every planned signal entry by namespace

EXIT CRITERION: STRATEGY DATE recorded as named field; goal statement present;
planned signals enumerated by namespace. Phase 4 may NOT open until this is met.

---

## Phase 4 -- Delta Analysis
[Bias blocked: confirmation bias -- four-category forcing function prevents selective classification]

ENTRY CONDITION: Phase 3 EXIT CRITERION met.
Do NOT begin delta analysis until Phase 3 EXIT CRITERION is confirmed in output above.

For each NEW artifact, classify each finding. Do not merge categories.

### CONFIRMED -- INERTIA's assumptions validated by NEW signals
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "CONFIRMED: none -- no NEW artifacts validate INERTIA's assumptions."

### EXPANDED -- INERTIA's assumptions broadened by NEW signals
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "EXPANDED: none -- no NEW artifacts expand INERTIA's assumptions."

### UNEXPECTED -- dimensions INERTIA's strategy did not cover
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "UNEXPECTED: none -- no NEW artifacts reveal uncovered dimensions."

### CHALLENGED -- INERTIA's assumptions directly questioned
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "CHALLENGED: none -- no NEW artifacts challenge INERTIA's assumptions."

EXIT CRITERION: All four category tables present with labeled nulls; each NEW artifact
in at least one category. Phase 5 may NOT open until this is met.

---

## Verdict Vocabulary

[>> SECTION SCOPE: This section contains verdict definitions ONLY. It does not contain
     Phase 1 read-barrier language. It does not contain restart isolation clause text.
     It does not contain INERTIA-GATE exclusion text. It does not contain consequence
     blocking enforcement. It does not contain the OUTPUT SCHEMA CONTRACT. A reviewer
     auditing verdict semantics does not encounter content from Phase 1, either
     INERTIA-GATE site, the consequence gate, or the OUTPUT SCHEMA CONTRACT. <<]

[>> GUARD: VERDICT SEMANTICS BLOCK <<]
[>> Bias blocked: definitional ambiguity -- both verdict outcomes fully specified as
     standalone definitions, independently verifiable without reading Phase 5 <<]
[>> Mechanism: A scorer or auditor can confirm verdict semantics from this block alone.
     Phase 5 applies these definitions; it does not redefine them. <<]

DEFEATED: Challenger evidence overcomes INERTIA's Phase 1 defense for this dimension.
  Forward path: dimension advances to Phase 6 (Change Proposals).

HOLDS: INERTIA's defense survives for this dimension. Dimension receives NO CHANGE.
  Forward path: no path to Phase 6. Execution for this dimension ends at Phase 5.

These two verdicts are exhaustive. No other verdict tokens are valid.

Confidence tier for DEFEATED rows (defined here; applied in Phase 5):
- HIGH: two or more independent NEW artifacts support the defeat on this dimension
- MEDIUM: one NEW artifact
- LOW: inference only (no direct NEW artifact evidence)

---

## Phase 5 -- INERTIA DEFEAT ASSESSMENT

[>> SECTION SCOPE: This section contains gate-exclusion text and consequence blocking
     enforcement ONLY. It does not redefine verdict semantics (those are defined in
     the Verdict Vocabulary block above). It does not contain restart isolation
     language. It does not contain the OUTPUT SCHEMA CONTRACT. A reviewer auditing
     the Phase 5 gate does not encounter verdict redefinitions, restart clause text,
     or OUTPUT SCHEMA CONTRACT content. <<]

[>> GUARD: INERTIA-GATE [Site 1 of 2 -- Phase 5 entry] <<]
[>> Bias blocked: action-default bias; status-quo neglect <<]
[>> Mechanism: Only DEFEATED dimensions advance to Phase 6. HOLDS dimensions have
     no path to Phase 6. This enforcement is at the Phase 5 entry site. A second
     independent enforcement exists at Phase 6 entry (Site 2 of 2). <<]

ENTRY CONDITION: Phase 4 EXIT CRITERION met (all four delta categories present).
Do NOT open Phase 5 until Phase 4 EXIT CRITERION is confirmed in output above.

Apply the Verdict Vocabulary defined above.
Do not redefine verdict semantics here.
Any inline DEFEATED or HOLDS definition appearing in this phase is a structural
violation of the single-source guarantee established by the Verdict Vocabulary block.

[>> GUARD: CONSEQUENCE GATE [Site 1 of 2 -- table entry] <<]
[>> Bias blocked: consequence-omission bias -- consequence stated before verdict assigned <<]
[>> Mechanism: Requiring the consequence field before the verdict prevents post-hoc
     rationalization where verdict is assigned first and consequence invented to justify
     it. This rule is stated at this preamble site independently. It does not delegate
     to the Phase 5 exit criterion to carry the constraint. <<]
Any row in this table with an empty "Consequence if unchanged" field cannot be
evaluated and cannot advance. Populate "Consequence if unchanged" before assigning
a verdict to that row.

| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if unchanged |

If all verdicts are HOLDS: emit "NULL_DELTA: INERTIA RETAINED ACROSS ALL DIMENSIONS."
Stop. Phase 6 does NOT open.

EXIT CRITERION: Verdict table complete; all dimensions adjudicated; NULL_DELTA emitted
if all HOLDS; exit blocked if any DEFEATED row has an empty "Consequence if unchanged"
field -- this blocking rule is stated at this exit criterion site independently. It
does not delegate to the preamble above to carry the constraint. At least one DEFEATED
verdict with populated "Consequence if unchanged" field to proceed to Phase 6.

---

## Phase 6 -- Change Proposals (DEFEATED dimensions only)

[>> SECTION SCOPE: This section contains three declared content types, co-located
     at this phase entry boundary. A C-24 auditor verifying spatial separation finds
     all three enumerated here, and finds no Phase 6 content declared outside this
     section.
     (1) GATE-EXCLUSION TEXT: The INERTIA-GATE (Site 2 of 2, immediately below)
     enforces HOLDS exclusion at this phase entry. This enforcement belongs to this
     section's scope; it is not carried by Phase 5.
     (2) PROPOSAL GENERATION: The Phase 6a and Phase 6b tables are produced in this
     section. All proposal content originates here.
     (3) ROW-LEVEL BIAS LABELING: The PROPOSAL BIAS AUDIT guard (immediately below,
     co-located with the INERTIA-GATE) is the enforcement point for the "Bias blocked
     by guard" column. Per-row bias labeling is produced within this section at the
     individual proposal row level. The "Bias blocked by guard" column -- pre-committed
     in the OUTPUT SCHEMA CONTRACT (document-first position) -- is the per-row output
     of this content type. This content type is distinct from per-phase bias
     annotations; row-level labeling occurs inside this section, not at external
     phase boundaries. <<]

[>> GUARD: INERTIA-GATE [Site 2 of 2 -- Phase 6 entry] <<]
[>> Bias blocked: action-default bias <<]
[>> Mechanism: HOLDS dimensions have no row and no path to this phase. This enforcement
     is independent of Site 1 at Phase 5. A model that bypasses Phase 5 and arrives
     directly at Phase 6 still encounters this gate. HOLDS exclusion is enforced here
     without relying on the Phase 5 site to carry the constraint. A reviewer can
     confirm HOLDS exclusion from this block alone, without reading Phase 5. <<]

[>> GUARD: PROPOSAL BIAS AUDIT <<]
[>> Bias blocked: two distinct failure modes at two distinct granularities <<]
[>> Mechanism: See SECTION SCOPE above for co-location context. The SECTION SCOPE
     declares row-level bias labeling as a named content type of this section;
     this guard is the enforcement mechanism for that declared content type.

     LEVEL 1 -- PHASE-LEVEL GATE (INERTIA-GATE, Site 2 above):
     The phase-level gate prevents SYSTEMIC PHASE STRUCTURE BIAS -- the tendency to
     treat the existence of the proposal phase as implicit evidence that change is
     warranted, before any individual row is evaluated. This failure mode operates at
     the phase boundary: the model enters a proposal-generation frame and produces
     proposals because the phase structure implies they are expected, not because
     evidence warrants them. The INERTIA-GATE at phase entry addresses this failure
     mode at the phase-level granularity. It does not address individual proposals.

     LEVEL 2 -- ROW-LEVEL BIAS LABELING ("Bias blocked by guard" column):
     Per-row labeling prevents MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION
     SURFACE -- justifying a pre-decided change after a signal suggests it, without
     surfacing the cognitive pull that drove the proposal framing. This failure mode
     operates below phase granularity: it is present even in a run where the phase-level
     gate fired correctly, because it occurs at the individual proposal row's decision
     point. The phase-level gate does not evaluate individual proposals and cannot
     block this failure mode. Row-level labeling addresses it where it occurs.

     BOTH LEVELS ARE REQUIRED. The phase-level gate does not protect against
     per-proposal motivated reasoning. The row-level column does not protect against
     systemic phase structure bias. These are distinct failure modes at distinct
     granularities. Presence of one without the other is a structural gap in bias
     coverage. Each proposal row MUST carry a "Bias blocked by guard" entry naming
     the cognitive bias the guard prevents at that row's specific decision point.
     This column is pre-committed in the OUTPUT SCHEMA CONTRACT (document-first
     position) and declared as a scope item in the SECTION SCOPE above. <<]

ENTRY CONDITION: Phase 5 EXIT CRITERION met; at least one DEFEATED verdict present;
NULL_DELTA not emitted. Do NOT open Phase 6 if NULL_DELTA was emitted in Phase 5.

### 6a -- Additions
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |
Null: "ADDITIONS: none -- INERTIA holds on all addition candidates."

### 6b -- Removals and Reprioritizations
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |
Null-REMOVALS: "REMOVALS: none -- INERTIA holds."
Null-REPRIORITIZATIONS: "REPRIORITIZATIONS: none -- INERTIA holds."

All 9 namespaces must have a row. Silence is not a null declaration.

EXIT CRITERION: All three change-type tables present with labeled nulls; all 9
namespaces covered; each DEFEATED dimension from Phase 5 has a corresponding row;
each non-null proposal row carries a populated "Bias blocked by guard" entry.
Phase 7 may NOT open until this is met.

---

## Phase 7 -- Confirmation Gate

[>> GUARD: CONFIRMATION GATE <<]
[>> Bias blocked: recency bias; sunk-cost bias <<]
[>> Mechanism: Explicit user confirmation required before any write. The absence
     of NO is not implicit YES. <<]

[>> GUARD: WRITE GUARD <<]
[>> Bias blocked: premature closure bias <<]
[>> Mechanism: strategy.md is not modified until explicit YES or REVISED is received
     at this gate. strategy.md has NOT been modified at this point. <<]

ENTRY CONDITION: Phase 6 EXIT CRITERION met.
Do NOT modify strategy.md before Phase 7 confirmation is received.

Present: Phase 4 delta findings (all four categories), Phase 6 proposals (6a and 6b).

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.
INERTIA currently holds. Proposed challenges: [N] additions / [N] removals / [N] reprioritizations

Reply YES to displace INERTIA on all listed dimensions
Reply NO to retain INERTIA (all dimensions unchanged)
Reply REVISED + edited table to displace INERTIA on custom dimensions
Reply WITHDRAW [#] to remove specific proposals before confirming
  WITHDRAW syntax: WITHDRAW [2] or WITHDRAW [1, 3]. Removes named proposals only;
  remainder is applied.
  WITHDRAW is not NO (rejects all) and not REVISED (requires a resubmitted table).
---
STOP HERE. Write nothing further until the user replies.

EXIT CRITERION: User has replied YES, NO, REVISED, or WITHDRAW.

---

## Phase 8 -- Apply (after YES or REVISED only)

ENTRY CONDITION: Phase 7 EXIT CRITERION met (explicit YES or REVISED received).
Do NOT write to strategy.md before this ENTRY CONDITION is confirmed.

[>> GUARD: WRITE GUARD (confirmed) <<]
[>> Bias blocked: premature closure bias -- write authorized by user at Phase 7 <<]

Write confirmed (non-withdrawn) changes to strategy.md.
No reformatting of unchanged sections.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations.
INERTIA displaced on: [dimension list]."
```

---

## Orthogonality Check

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-29 | FULL | FULL | FULL | FULL | FULL |
| C-30 | FULL | FULL | FULL | FULL | FULL |
| C-31 | **FULL** | partial | partial | **FULL** | **FULL** |
| C-32 | partial | **FULL** | partial | **FULL** | **FULL** |
| C-33 | partial | partial | **FULL** | **FULL** | **FULL** |

C-31 targeted by V-01 independently: guard text names both failure modes (systemic
phase structure bias at phase level; motivated reasoning at row level) and states
"BOTH LEVELS ARE REQUIRED."

C-32 targeted by V-02 independently: SECTION SCOPE enumerates three named content
types with structural cross-references; "row-level bias labeling" explicitly names
the PROPOSAL BIAS AUDIT guard as its enforcement point.

C-33 targeted by V-03 independently: standalone OUTPUT SCHEMA CONTRACT section at
document-first position; names all three C-29 sites and both C-30 tables; states
"both violations detectable from this block alone."

V-04 vs V-05 differ only in CONTRACT position and guard-scope cross-reference link:
V-04 places CONTRACT inside Output Schema section; V-05 places it before INERTIA
COMPETITOR DECLARATION and adds bidirectional guard-scope reference chain.
