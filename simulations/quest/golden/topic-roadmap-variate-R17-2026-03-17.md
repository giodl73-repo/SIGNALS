---
skill: quest-variate
skill_target: topic-roadmap
round: R17
date: 2026-03-17
rubric_version: v17
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single:
    V-01: contract_taxonomy_c40 -- upgrade CONTRACT B to add STRUCTURAL/VALUE labeled violation taxonomy split; §9 compliance stays generic; no self-sufficiency assertion
    V-02: guard_value_literal_c41 -- upgrade §9 compliance obligation to name exact 'Bias blocked by guard' literal; CONTRACT B mentions both failure modes without formal labels; no self-sufficiency assertion
    V-03: scorer_self_sufficiency_c42 -- add explicit scorer self-sufficiency assertion to CONTRACT B (built on C-39+C-40 base); §9 compliance stays generic
  combined:
    V-04: c40+c41+c42 standard -- all three new criteria at FULL, direct formulation
    V-05: c40+c41+c42 maximal -- all three with mutual cross-references between §9 guard and CONTRACT B; C-42 includes falsifiability clause naming C-39/C-40 as structural consistency dependencies
rubric_anchor: >
  v17 adds C-40 (CONTRACT B structural/value violation taxonomy split: STRUCTURAL and
  VALUE as labeled, independently detectable categories), C-41 (§9 guard body compliance
  obligation names exact 'Bias blocked by guard' literal, creating mutual reinforcement
  with CONTRACT B), C-42 (CONTRACT B explicit scorer self-sufficiency assertion covering
  both structural and value compliance test types, falsifiable). Formula denominator
  62->68 (34 aspirational x 2). R16 V-05 already satisfies all three at FULL (68/68);
  R16 V-04 scores 60/68 = 8.82 under v17 (C-40=0, C-41=0, C-42=0). V-03 from R16
  earns C-40=1 partial (value violation named, no formal STRUCTURAL label), yielding
  60/68 = 8.82, tying V-04. An R17 variate hitting all three simultaneously achieves
  56+6+6 = 68/68 = 10.00.
round_targets: >
  C-40 full pass (2): CONTRACT B defines and labels at least two violation categories --
  STRUCTURAL (column absent) and VALUE (column present but value != exact literal) --
  each with independent detection language; categories are formally named so they are
  referenceable by name; a scorer determines from CONTRACT B alone which category
  applies without consulting phase content.
  C-41 full pass (2): The §9 guard body compliance obligation statement names the exact
  literal 'Bias blocked by guard'; literal matches CONTRACT B; obligation is inside the
  §9 guard body; guard is independently sufficient for value identification without
  consulting CONTRACT B.
  C-42 full pass (2): CONTRACT B contains an explicit declarative statement asserting
  that a scorer reading CONTRACT B alone can verify both the structural compliance test
  (column exists) and the value compliance test (column contains exact literal); assertion
  identifies both test types; located inside CONTRACT B block; claim is falsifiable --
  a CONTRACT B that makes the claim but fails C-39 or C-40 is internally inconsistent.
orthogonality_notes: >
  C-40 depends on C-39 FULL (value string must exist to be independently detectable as
  a VALUE violation). C-41 depends on C-39 FULL (guard-body literal should match
  CONTRACT B literal). C-42 depends on C-39 FULL and C-40 FULL (self-sufficiency claim
  requires value string present and two-category framework in place). All five variations
  have C-37=FULL, C-38=FULL, C-39=FULL to enable isolation testing.
  V-01 (C-40=FULL, C-41=FAIL, C-42=FAIL): labeled taxonomy present; guard generic.
  V-02 (C-40=PARTIAL, C-41=FULL, C-42=FAIL): guard names exact literal; CONTRACT B
  mentions both failure modes without formal STRUCTURAL/VALUE category labels.
  V-03 (C-40=FULL, C-41=FAIL, C-42=FULL): taxonomy + self-sufficiency in CONTRACT B;
  guard compliance obligation stays generic.
  V-04 (C-40=FULL, C-41=FULL, C-42=FULL): standard combined formulation.
  V-05 (C-40=FULL, C-41=FULL, C-42=FULL): maximal -- §9 names literal and explicitly
  references CONTRACT B as governing document; C-42 includes falsifiability clause.
---

## Variation Summary

| Var | C-37 | C-38 | C-39 | C-40 | C-41 | C-42 | Expected | Hypothesis |
|-----|:----:|:----:|:----:|:----:|:----:|:----:|:--------:|------------|
| V-01 | FULL | FULL | FULL | FULL | FAIL | FAIL | 64/68 = 9.41 | STRUCTURAL/VALUE taxonomy in CONTRACT B achieves C-40 independently |
| V-02 | FULL | FULL | FULL | PARTIAL | FULL | FAIL | 65/68 = 9.56 | Exact literal in §9 compliance obligation achieves C-41 independently |
| V-03 | FULL | FULL | FULL | FULL | FAIL | FULL | 66/68 = 9.71 | Self-sufficiency assertion on C-39+C-40 base achieves C-42 independently |
| V-04 | FULL | FULL | FULL | FULL | FULL | FULL | 68/68 = 10.00 | All three combined, direct formulation |
| V-05 | FULL | FULL | FULL | FULL | FULL | FULL | 68/68 = 10.00 | Maximal: mutual cross-references + falsifiability clause |

---

## V-01 -- Single axis: C-40 CONTRACT B violation taxonomy split

**Variation axis**: CONTRACT B is upgraded from R16 V-05 in one dimension only: the
addition of a formally named STRUCTURAL/VALUE violation taxonomy split. In R16 V-04,
CONTRACT B names column absence as a violation but does not split violation types into
labeled categories. R16 V-03 names the exact literal `'Bias blocked by guard'` (C-39=FULL)
and mentions value violations, but the taxonomy is not organized into independently named
categories. V-01 adds formal STRUCTURAL and VALUE category labels with independent
detection rules for each, making each violation type referenceable by name and detectable
from the contract block alone without reading phase content.

The §9 PROPOSAL BIAS AUDIT guard compliance obligation is unchanged: it uses generic
"non-null Bias guard value" language (C-41=FAIL). No scorer self-sufficiency assertion
is added to CONTRACT B (C-42=FAIL). C-37 and C-38 carry the R16 V-05 full-credit
formulations throughout.

**Hypothesis**: C-40 full pass requires CONTRACT B to define and formally label at least
two violation categories -- STRUCTURAL (column absent) and VALUE (column present but
wrong string) -- each with independent detection logic. Adding explicit category names
makes each violation referenceable and independently testable from CONTRACT B alone.
C-41 and C-42 remain unaddressed, staying at FAIL.

**Expected score**: 56 (C-09--C-36) + 2 (C-37) + 2 (C-38) + 2 (C-39) + 2 (C-40) + 0 (C-41) + 0 (C-42) = **64/68 = 9.41**

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

[>> CONTRACT A -- Consequence field naming: The string "Consequence if unchanged" is
     the canonical name for the consequence column. This string MUST appear as the
     column header in the Phase 5 defeat assessment table. This string MUST appear as
     the column header in the Phase 6a Additions table. This string MUST appear as the
     column header in the Phase 6b Removals/Reprioritizations table. This string MUST
     appear as the field name in the Phase 5 exit criterion advancement condition.
     Any deviation from "Consequence if unchanged" at any of these four sites is a
     schema contract violation detectable against this block without reading the phases. <<]

[>> CONTRACT B -- Proposal bias column: The column "Bias blocked by guard" is a
     required column in Phase 6a and Phase 6b proposal tables. This column MUST be
     present in the table schema for both tables. Each non-null proposal row MUST
     carry a populated entry naming the cognitive bias the guard prevents at that
     row's decision point. Absence of this column from either Phase 6 table is a
     schema contract violation detectable against this block without reading Phase 6.
     Compliant value: the exact string 'Bias blocked by guard'. No approximate variant
     ('bias blocked', 'guard applied', 'both levels passed') satisfies this contract.
     Violation taxonomy (two independently labeled categories):
       STRUCTURAL: the "Bias blocked by guard" column is absent from the table schema.
         Detection rule: check column presence from table headers alone, without
         reading any row content. A STRUCTURAL violation is identifiable from table
         structure without reading proposal rows.
       VALUE: the "Bias blocked by guard" column is present but does not contain the
         exact string 'Bias blocked by guard'. Detection rule: check cell value against
         the exact literal defined in this contract. A VALUE violation is identifiable
         by comparing cell content to the exact literal named above.
     Each violation category is independently labeled and independently detectable
     from this CONTRACT B block without consulting phase execution content. <<]

---

## Phase 1 -- Pre-Signal Defense Register

[>> SECTION SCOPE: This section contains the Phase 1 read-barrier and restart
     isolation clause ONLY. It does not contain verdict vocabulary definitions.
     It does not contain INERTIA-GATE exclusion text. It does not contain schema
     contract clauses. A reviewer auditing the read-barrier does not encounter
     content from the Verdict Vocabulary section, either INERTIA-GATE site, or
     the Output Schema block. <<]

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
Write the defense register from prior knowledge only.

ENTRY CONDITION: No files have been read since Phase 1 began (first run or restart).

| Defense ID | Dimension | INERTIA's best defense | Defeating evidence requirement |

EXIT CRITERION: Defense register table present; each known dimension has a row; no
file has been read. Phase 2 may NOT open until this is met.

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
     after this point introduces post-hoc vocabulary alignment. Signal files may NOT
     be re-read after this inventory is written. All subsequent phases use the written
     inventory only. <<]

EXIT CRITERION: Inventory table present; all 9 namespaces covered; SIGNAL READ-LOCK
in effect. Phase 3 may NOT open until this is met.

---

## Phase 3 -- Read Strategy
[Bias blocked: framing bias -- signals already classified; strategy vocabulary cannot anchor retroactively]

ENTRY CONDITION: Phase 2 EXIT CRITERION met.
Do NOT read strategy.md until Phase 2 EXIT CRITERION is confirmed in output above.

Read strategy.md. Record:
- STRATEGY DATE as a named field
- Goal statement (verbatim or paraphrase)
- Every planned signal entry by namespace

EXIT CRITERION: STRATEGY DATE recorded; goal statement present; planned signals
enumerated by namespace. Phase 4 may NOT open until this is met.

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
     Phase 1 read-barrier language. It does not contain INERTIA-GATE exclusion text.
     It does not contain schema contract clauses. A reviewer auditing verdict semantics
     does not encounter content from Phase 1, either INERTIA-GATE site, the consequence
     gate, or the Output Schema block. <<]

[>> GUARD: VERDICT SEMANTICS BLOCK <<]
[>> Bias blocked: definitional ambiguity -- both verdict outcomes fully specified as
     standalone definitions, independently verifiable without reading Phase 5 <<]

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
     enforcement ONLY. It does not redefine verdict semantics. It does not contain
     restart isolation language. It does not contain schema contract clauses. A reviewer
     auditing the Phase 5 gate does not encounter verdict redefinitions, restart clause
     text, or Output Schema content. <<]

[>> GUARD: INERTIA-GATE [Site 1 of 2 -- Phase 5 entry] <<]
[>> Bias blocked: action-default bias; status-quo neglect <<]
[>> Mechanism: Only DEFEATED dimensions advance to Phase 6. HOLDS dimensions have
     no path to Phase 6. This enforcement is at the Phase 5 entry site. A second
     independent enforcement exists at Phase 6 entry (Site 2 of 2). <<]

ENTRY CONDITION: Phase 4 EXIT CRITERION met (all four delta categories present).
Do NOT open Phase 5 until Phase 4 EXIT CRITERION is confirmed in output above.

Apply the Verdict Vocabulary defined above. Do not redefine verdict semantics here.

[>> GUARD: CONSEQUENCE GATE [Site 1 of 2 -- table entry] <<]
[>> Bias blocked: consequence-omission bias -- consequence stated before verdict assigned <<]
[>> Mechanism: Requiring the consequence field before the verdict prevents post-hoc
     rationalization where verdict is assigned first and consequence invented to justify
     it. This rule is stated at this preamble site independently. <<]
Any row with an empty "Consequence if unchanged" field cannot be evaluated and cannot
advance. Populate "Consequence if unchanged" before assigning a verdict to that row.

| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if unchanged |

If all verdicts are HOLDS: emit "NULL_DELTA: INERTIA RETAINED ACROSS ALL DIMENSIONS."
Stop. Phase 6 does NOT open.

EXIT CRITERION: Verdict table complete; all dimensions adjudicated; NULL_DELTA emitted
if all HOLDS; exit blocked if any DEFEATED row has empty "Consequence if unchanged" --
this blocking rule is stated at this exit criterion site independently. At least one
DEFEATED verdict with populated "Consequence if unchanged" to proceed to Phase 6.

---

## Phase 6 -- Change Proposals (DEFEATED dimensions only)

[>> SECTION SCOPE: This section contains gate-exclusion text, proposal generation, and
     row-level bias labeling. It does not redefine verdict semantics. It does not contain
     schema contract clauses. A reviewer auditing the Phase 6 gate does not encounter
     verdict redefinitions or Output Schema content.
     The higher-order failure mode protected against in this phase is
     LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE.
     Note that LEVEL 1: CONFIRMATION ANCHORING AT THE EVIDENCE SCAN SURFACE does not
     protect against LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION
     SURFACE; both levels must be checked independently per the PROPOSAL BIAS AUDIT
     guard below. A C-24 auditor checking this scope can traverse from this scope note
     to the guard using the formal label LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL
     PROPOSAL DECISION SURFACE without reading phase execution content. <<]

[>> GUARD: INERTIA-GATE [Site 2 of 2 -- Phase 6 entry] <<]
[>> Bias blocked: action-default bias <<]
[>> Mechanism: HOLDS dimensions have no row and no path to this phase. This enforcement
     is independent of Site 1 at Phase 5. A model that bypasses Phase 5 and arrives
     directly at Phase 6 still encounters this gate. HOLDS exclusion is enforced here
     without relying on the Phase 5 site. <<]

[>> GUARD: PROPOSAL BIAS AUDIT [§9] <<]
[>> Bias blocked: two distinct failure modes at two distinct granularities <<]
[>> Mechanism:
     LEVEL 1 -- PHASE-LEVEL GATE (INERTIA-GATE, Site 2 above):
     LEVEL 1 prevents SYSTEMIC PHASE STRUCTURE BIAS -- the tendency to treat the
     existence of the proposal phase as implicit evidence that change is warranted,
     before any individual row is evaluated. The INERTIA-GATE at phase entry addresses
     this failure mode at the phase-level granularity. It does not address individual
     proposals.

     LEVEL 2 -- ROW-LEVEL BIAS LABELING ("Bias blocked by guard" column):
     LEVEL 2 prevents MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE --
     justifying a pre-decided change after a signal suggests it, without surfacing the
     cognitive pull that drove the proposal framing. This failure mode operates below
     phase granularity: it is present even in a run where the phase-level gate fired
     correctly, because it occurs at the individual proposal row's decision point. The
     phase-level gate does not evaluate individual proposals and cannot block this
     failure mode. Row-level labeling addresses it where it occurs.

     LEVEL 1 does not protect against LEVEL 2. A balanced evidence scan (LEVEL 1
     satisfied) does not prevent motivated reasoning at the proposal decision surface
     (LEVEL 2). The protection hierarchy is not transitive; both guards must be applied
     independently. A LEVEL 1 pass confers zero LEVEL 2 protection.

     BOTH LEVELS ARE REQUIRED. Presence of one without the other is a structural gap
     in bias coverage. Each proposal row MUST carry a populated "Bias blocked by guard"
     entry naming the cognitive bias the guard prevents at that row's specific decision
     point. <<]

ENTRY CONDITION: Phase 5 EXIT CRITERION met; at least one DEFEATED verdict present;
NULL_DELTA not emitted.

### 6a -- Additions
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |
Null: "ADDITIONS: none -- INERTIA holds on all addition candidates."

### 6b -- Removals and Reprioritizations
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |
Null-REMOVALS: "REMOVALS: none -- INERTIA holds."
Null-REPRIORITIZATIONS: "REPRIORITIZATIONS: none -- INERTIA holds."

All 9 namespaces must have a row. Silence is not a null declaration.

EXIT CRITERION: All three change-type tables present with labeled nulls; all 9
namespaces covered; each DEFEATED dimension has a corresponding row; each non-null
proposal row carries a populated "Bias blocked by guard" entry. Phase 7 may NOT open.

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
---
STOP HERE. Write nothing further until the user replies.

EXIT CRITERION: User has replied YES, NO, REVISED, or WITHDRAW.

---

## Phase 8 -- Apply (after YES or REVISED only)

ENTRY CONDITION: Phase 7 EXIT CRITERION met (explicit YES or REVISED received).

[>> GUARD: WRITE GUARD (confirmed) <<]
[>> Bias blocked: premature closure bias -- write authorized by user at Phase 7 <<]

Write confirmed (non-withdrawn) changes to strategy.md. No reformatting of unchanged sections.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations.
INERTIA displaced on: [dimension list]."
```

---

## V-02 -- Single axis: C-41 guard compliance obligation names exact literal

**Variation axis**: The §9 PROPOSAL BIAS AUDIT guard compliance obligation is upgraded.
In R16 V-04, the obligation reads "Each proposal row MUST carry a populated 'Bias blocked
by guard' entry naming the cognitive bias the guard prevents at that row's decision point"
-- a non-null requirement without naming the required value string. V-02 changes this
compliance obligation line to name the exact literal `'Bias blocked by guard'` as the
required value, making the guard body independently sufficient for value identification
without consulting CONTRACT B.

CONTRACT B retains C-39 (exact literal present) and mentions both failure modes (column
absent vs incorrect value) but does not use formal STRUCTURAL/VALUE category names --
the two failure modes are described as "structural failure" and "value failure" in prose
without being formally labeled as referenceable categories. This gives C-40=PARTIAL(1).
No scorer self-sufficiency assertion is added (C-42=FAIL). C-37 and C-38 carry the
R16 V-05 full-credit formulations.

**Hypothesis**: C-41 full pass requires the §9 guard body compliance obligation to name
the exact required value string, not merely require a non-null entry. Adding the literal
`'Bias blocked by guard'` to the compliance obligation line achieves C-41=2 independently.
CONTRACT B's informal treatment of both failure modes earns partial C-40 credit.

**Expected score**: 56 (C-09--C-36) + 2 (C-37) + 2 (C-38) + 2 (C-39) + 1 (C-40 partial) + 2 (C-41) + 0 (C-42) = **65/68 = 9.56**

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

[>> CONTRACT A -- Consequence field naming: The string "Consequence if unchanged" is
     the canonical name for the consequence column. This string MUST appear as the
     column header in the Phase 5 defeat assessment table. This string MUST appear as
     the column header in the Phase 6a Additions table. This string MUST appear as the
     column header in the Phase 6b Removals/Reprioritizations table. This string MUST
     appear as the field name in the Phase 5 exit criterion advancement condition.
     Any deviation from "Consequence if unchanged" at any of these four sites is a
     schema contract violation detectable against this block without reading the phases. <<]

[>> CONTRACT B -- Proposal bias column: The column "Bias blocked by guard" is a
     required column in Phase 6a and Phase 6b proposal tables. This column MUST be
     present in the table schema for both tables. Each non-null proposal row MUST
     carry a populated entry naming the cognitive bias the guard prevents at that
     row's decision point. Absence of this column from either Phase 6 table is a
     schema contract violation detectable against this block without reading Phase 6.
     Compliant value: the exact string 'Bias blocked by guard'. Two compliance failures
     are possible: a structural failure (the column is absent from the table schema)
     and a value failure (the column is present but contains an incorrect string).
     A scorer checking this contract can distinguish between the two cases using the
     exact literal defined here. Only the exact string 'Bias blocked by guard' satisfies
     value compliance; approximate variants ('bias blocked', 'guard applied',
     'both levels passed') are not compliant. <<]

---

## Phase 1 -- Pre-Signal Defense Register

[>> SECTION SCOPE: This section contains the Phase 1 read-barrier and restart
     isolation clause ONLY. It does not contain verdict vocabulary definitions.
     It does not contain INERTIA-GATE exclusion text. It does not contain schema
     contract clauses. A reviewer auditing the read-barrier does not encounter
     content from the Verdict Vocabulary section, either INERTIA-GATE site, or
     the Output Schema block. <<]

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
Write the defense register from prior knowledge only.

ENTRY CONDITION: No files have been read since Phase 1 began (first run or restart).

| Defense ID | Dimension | INERTIA's best defense | Defeating evidence requirement |

EXIT CRITERION: Defense register table present; each known dimension has a row; no
file has been read. Phase 2 may NOT open until this is met.

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
[>> Mechanism: Signal files are fixed as of this inventory. Signal files may NOT
     be re-read after this inventory is written. All subsequent phases use the written
     inventory only. <<]

EXIT CRITERION: Inventory table present; all 9 namespaces covered; SIGNAL READ-LOCK
in effect. Phase 3 may NOT open until this is met.

---

## Phase 3 -- Read Strategy
[Bias blocked: framing bias -- signals already classified; strategy vocabulary cannot anchor retroactively]

ENTRY CONDITION: Phase 2 EXIT CRITERION met.

Read strategy.md. Record STRATEGY DATE as a named field; goal statement; planned
signals enumerated by namespace.

EXIT CRITERION: STRATEGY DATE recorded; goal statement present; planned signals
enumerated. Phase 4 may NOT open until this is met.

---

## Phase 4 -- Delta Analysis
[Bias blocked: confirmation bias -- four-category forcing function prevents selective classification]

ENTRY CONDITION: Phase 3 EXIT CRITERION met.

For each NEW artifact, classify each finding. Do not merge categories.

### CONFIRMED
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "CONFIRMED: none -- no NEW artifacts validate INERTIA's assumptions."

### EXPANDED
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "EXPANDED: none -- no NEW artifacts expand INERTIA's assumptions."

### UNEXPECTED
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "UNEXPECTED: none -- no NEW artifacts reveal uncovered dimensions."

### CHALLENGED
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "CHALLENGED: none -- no NEW artifacts challenge INERTIA's assumptions."

EXIT CRITERION: All four category tables present with labeled nulls; each NEW artifact
in at least one category. Phase 5 may NOT open until this is met.

---

## Verdict Vocabulary

[>> SECTION SCOPE: This section contains verdict definitions ONLY. <<]

[>> GUARD: VERDICT SEMANTICS BLOCK <<]
[>> Bias blocked: definitional ambiguity -- both verdict outcomes fully specified <<]

DEFEATED: Challenger evidence overcomes INERTIA's Phase 1 defense. Forward path: Phase 6.
HOLDS: INERTIA's defense survives. Forward path: no path to Phase 6.

Confidence tier for DEFEATED rows: HIGH (2+ independent artifacts) / MEDIUM (1 artifact) / LOW (inference only).

---

## Phase 5 -- INERTIA DEFEAT ASSESSMENT

[>> SECTION SCOPE: This section contains gate-exclusion text and consequence blocking
     enforcement ONLY. It does not redefine verdict semantics or contain schema contract
     clauses. <<]

[>> GUARD: INERTIA-GATE [Site 1 of 2 -- Phase 5 entry] <<]
[>> Bias blocked: action-default bias; status-quo neglect <<]
[>> Mechanism: Only DEFEATED dimensions advance to Phase 6. HOLDS dimensions have
     no path to Phase 6. A second independent enforcement exists at Phase 6 entry. <<]

ENTRY CONDITION: Phase 4 EXIT CRITERION met.

Apply the Verdict Vocabulary defined above. Do not redefine verdict semantics here.

[>> GUARD: CONSEQUENCE GATE [Site 1 of 2 -- table entry] <<]
[>> Bias blocked: consequence-omission bias <<]
Any row with an empty "Consequence if unchanged" field cannot advance.
Populate "Consequence if unchanged" before assigning a verdict.

| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if unchanged |

If all verdicts are HOLDS: emit "NULL_DELTA: INERTIA RETAINED ACROSS ALL DIMENSIONS." Stop.

EXIT CRITERION: Verdict table complete; NULL_DELTA emitted if all HOLDS; exit blocked
if any DEFEATED row has empty "Consequence if unchanged". At least one DEFEATED verdict
with populated consequence to proceed to Phase 6.

---

## Phase 6 -- Change Proposals (DEFEATED dimensions only)

[>> SECTION SCOPE: This section contains gate-exclusion text, proposal generation, and
     row-level bias labeling. It does not redefine verdict semantics or contain schema
     contract clauses.
     The higher-order failure mode protected against in this phase is
     LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE.
     Note that LEVEL 1: CONFIRMATION ANCHORING AT THE EVIDENCE SCAN SURFACE does not
     protect against LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION
     SURFACE; both levels must be checked independently per the PROPOSAL BIAS AUDIT
     guard below. A C-24 auditor checking this scope can traverse from this scope note
     to the guard using the formal label LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL
     PROPOSAL DECISION SURFACE without reading phase execution content. <<]

[>> GUARD: INERTIA-GATE [Site 2 of 2 -- Phase 6 entry] <<]
[>> Bias blocked: action-default bias <<]
[>> Mechanism: HOLDS dimensions have no path to this phase. Independent of Site 1.
     A model bypassing Phase 5 and arriving at Phase 6 still encounters this gate. <<]

[>> GUARD: PROPOSAL BIAS AUDIT [§9] <<]
[>> Bias blocked: two distinct failure modes at two distinct granularities <<]
[>> Mechanism:
     LEVEL 1 -- PHASE-LEVEL GATE (INERTIA-GATE, Site 2 above):
     LEVEL 1 prevents SYSTEMIC PHASE STRUCTURE BIAS. The INERTIA-GATE at phase entry
     addresses this failure mode at phase-level granularity. It does not address
     individual proposals.

     LEVEL 2 -- ROW-LEVEL BIAS LABELING ("Bias blocked by guard" column):
     LEVEL 2 prevents MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE.
     This failure mode operates below phase granularity. The phase-level gate cannot
     block this failure mode. Row-level labeling addresses it where it occurs.

     LEVEL 1 does not protect against LEVEL 2. A balanced evidence scan (LEVEL 1
     satisfied) does not prevent motivated reasoning at the proposal decision surface
     (LEVEL 2). The protection hierarchy is not transitive; both guards must be applied
     independently. A LEVEL 1 pass confers zero LEVEL 2 protection.

     COMPLIANCE OBLIGATION: Every §6 proposal row must carry the exact string
     'Bias blocked by guard' in the Bias blocked by guard column. This exact literal --
     'Bias blocked by guard' -- is the required value. The value requirement is stated
     here in the §9 guard body independently; a scorer reading this guard block can
     identify the required column value without consulting CONTRACT B. A non-null entry
     that does not contain this exact literal is a value violation per CONTRACT B. <<]

ENTRY CONDITION: Phase 5 EXIT CRITERION met; at least one DEFEATED verdict present;
NULL_DELTA not emitted.

### 6a -- Additions
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |
Null: "ADDITIONS: none -- INERTIA holds on all addition candidates."

### 6b -- Removals and Reprioritizations
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |
Null-REMOVALS: "REMOVALS: none -- INERTIA holds."
Null-REPRIORITIZATIONS: "REPRIORITIZATIONS: none -- INERTIA holds."

All 9 namespaces must have a row. Silence is not a null declaration.

EXIT CRITERION: All three change-type tables present with labeled nulls; all 9
namespaces covered; each DEFEATED dimension has a row; each non-null proposal row
carries a populated "Bias blocked by guard" entry. Phase 7 may NOT open.

---

## Phase 7 -- Confirmation Gate

[>> GUARD: CONFIRMATION GATE <<]
[>> GUARD: WRITE GUARD <<]
[>> Bias blocked: premature closure bias -- strategy.md NOT modified until explicit YES <<]

ENTRY CONDITION: Phase 6 EXIT CRITERION met.

Present: Phase 4 delta findings (all four categories), Phase 6 proposals (6a and 6b).

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.
INERTIA currently holds. Proposed challenges: [N] additions / [N] removals / [N] reprioritizations

Reply YES to displace INERTIA on all listed dimensions
Reply NO to retain INERTIA (all dimensions unchanged)
Reply REVISED + edited table to displace INERTIA on custom dimensions
Reply WITHDRAW [#] to remove specific proposals before confirming
---
STOP HERE. Write nothing further until the user replies.

---

## Phase 8 -- Apply (after YES or REVISED only)

ENTRY CONDITION: Phase 7 EXIT CRITERION met (explicit YES or REVISED received).

[>> GUARD: WRITE GUARD (confirmed) <<]

Write confirmed (non-withdrawn) changes to strategy.md. No reformatting of unchanged sections.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations.
INERTIA displaced on: [dimension list]."
```

---

## V-03 -- Single axis: C-42 scorer self-sufficiency assertion

**Variation axis**: CONTRACT B is upgraded to add an explicit scorer self-sufficiency
assertion (C-42), built on a C-39=FULL + C-40=FULL base. The taxonomy split from V-01
is retained; the new element is the explicit declarative statement that a scorer reading
CONTRACT B alone can verify both the structural compliance test and the value compliance
test. The self-sufficiency assertion identifies both test types by name and is located
inside the CONTRACT B block.

The §9 PROPOSAL BIAS AUDIT guard compliance obligation is unchanged: it uses generic
"non-null Bias guard value" language without naming the exact literal (C-41=FAIL). C-37
and C-38 carry the R16 V-05 full-credit formulations.

**Hypothesis**: C-42 full pass requires CONTRACT B to make an explicit, named,
falsifiable self-sufficiency claim identifying both test types. Building on a C-40=FULL
base (taxonomy split present) provides the structural prerequisite. Adding the explicit
assertion achieves C-42=2 without touching the §9 guard. C-41 stays at FAIL because
the guard compliance obligation does not name the exact literal.

**Expected score**: 56 (C-09--C-36) + 2 (C-37) + 2 (C-38) + 2 (C-39) + 2 (C-40) + 0 (C-41) + 2 (C-42) = **66/68 = 9.71**

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

[>> CONTRACT A -- Consequence field naming: The string "Consequence if unchanged" is
     the canonical name for the consequence column. This string MUST appear as the
     column header in the Phase 5 defeat assessment table. This string MUST appear as
     the column header in the Phase 6a Additions table. This string MUST appear as the
     column header in the Phase 6b Removals/Reprioritizations table. This string MUST
     appear as the field name in the Phase 5 exit criterion advancement condition.
     Any deviation from "Consequence if unchanged" at any of these four sites is a
     schema contract violation detectable against this block without reading the phases. <<]

[>> CONTRACT B -- Proposal bias column: The column "Bias blocked by guard" is a
     required column in Phase 6a and Phase 6b proposal tables. This column MUST be
     present in the table schema for both tables. Each non-null proposal row MUST
     carry a populated entry naming the cognitive bias the guard prevents at that
     row's decision point. Absence of this column from either Phase 6 table is a
     schema contract violation detectable against this block without reading Phase 6.
     Compliant value: the exact string 'Bias blocked by guard'. No approximate variant
     satisfies this contract.
     Violation taxonomy (two independently labeled categories):
       STRUCTURAL: the "Bias blocked by guard" column is absent from the table schema.
         Detection rule: check column presence from table headers alone, without
         reading any row content.
       VALUE: the column is present but does not contain the exact string
         'Bias blocked by guard'. Detection rule: check cell value against the exact
         literal defined in this contract.
     Each violation category is independently labeled and independently detectable
     from this CONTRACT B block without consulting phase execution content.
     SCORER SELF-SUFFICIENCY DECLARATION: A scorer reading CONTRACT B alone can verify:
       (a) Structural compliance test: whether the "Bias blocked by guard" column
           exists in the Phase 6 table schema.
       (b) Value compliance test: whether the column contains the exact string
           'Bias blocked by guard'.
     Both test types are defined in this CONTRACT B block. This declaration is
     falsifiable: a CONTRACT B block that makes this self-sufficiency claim but does
     not name the exact required value string (required for test (b)) or does not
     define both violation categories (required to make (a) and (b) independently
     distinguishable) is internally inconsistent -- a detectable structural error. <<]

---

## Phase 1 -- Pre-Signal Defense Register

[>> SECTION SCOPE: This section contains the Phase 1 read-barrier and restart
     isolation clause ONLY. It does not contain verdict vocabulary definitions,
     INERTIA-GATE exclusion text, or schema contract clauses. <<]

[>> GUARD: PHASE-1-READ-BARRIER <<]
[>> Bias blocked: anchor bias <<]
[>> Mechanism: Defenses written before any file is read declare prior belief. <<]

FIRST-RUN ISOLATION: No files have been read yet.
DO NOT read strategy.md or any signal file before Phase 1 is complete.
If any file has been read, restart Phase 1 without it in context.

RESTART ISOLATION: Do NOT re-read any file to reconstruct state after interruption.
Write the defense register from prior knowledge only.

ENTRY CONDITION: No files have been read since Phase 1 began.

| Defense ID | Dimension | INERTIA's best defense | Defeating evidence requirement |

EXIT CRITERION: Defense register table present; no file read. Phase 2 may NOT open.

---

## Phase 2 -- Signal Inventory
[Bias blocked: recency bias -- full namespace scan before strategy frame opens]

ENTRY CONDITION: Phase 1 EXIT CRITERION met.

Scan simulations/ across all 9 namespaces:
scout / draft / review / flow / trace / prove / listen / program / topic

Read TOPICS.md. Record STRATEGY DATE. Classify each artifact as NEW or PRIOR.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

All 9 namespaces must appear. Zero-artifact namespaces emit an explicit null row.

[>> GUARD: SIGNAL READ-LOCK <<]
[>> Bias blocked: confirmation bias <<]
[>> Signal files may NOT be re-read after this inventory is written. <<]

EXIT CRITERION: Inventory present; all 9 namespaces covered; SIGNAL READ-LOCK in effect.

---

## Phase 3 -- Read Strategy
[Bias blocked: framing bias]

ENTRY CONDITION: Phase 2 EXIT CRITERION met.

Read strategy.md. Record STRATEGY DATE, goal statement, planned signals by namespace.

EXIT CRITERION: STRATEGY DATE recorded; goal and planned signals present.

---

## Phase 4 -- Delta Analysis
[Bias blocked: confirmation bias]

ENTRY CONDITION: Phase 3 EXIT CRITERION met.

### CONFIRMED
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "CONFIRMED: none -- no NEW artifacts validate INERTIA's assumptions."

### EXPANDED
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "EXPANDED: none -- no NEW artifacts expand INERTIA's assumptions."

### UNEXPECTED
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "UNEXPECTED: none -- no NEW artifacts reveal uncovered dimensions."

### CHALLENGED
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "CHALLENGED: none -- no NEW artifacts challenge INERTIA's assumptions."

EXIT CRITERION: All four category tables with labeled nulls; each NEW artifact covered.

---

## Verdict Vocabulary

[>> SECTION SCOPE: Verdict definitions ONLY. <<]
[>> GUARD: VERDICT SEMANTICS BLOCK <<]

DEFEATED: Evidence overcomes INERTIA's defense. Forward path: Phase 6.
HOLDS: INERTIA survives. No path to Phase 6.

Confidence: HIGH (2+ artifacts) / MEDIUM (1 artifact) / LOW (inference only).

---

## Phase 5 -- INERTIA DEFEAT ASSESSMENT

[>> SECTION SCOPE: Gate-exclusion text and consequence blocking enforcement ONLY. <<]

[>> GUARD: INERTIA-GATE [Site 1 of 2 -- Phase 5 entry] <<]
[>> Only DEFEATED dimensions advance to Phase 6. <<]

ENTRY CONDITION: Phase 4 EXIT CRITERION met.

[>> GUARD: CONSEQUENCE GATE [Site 1 of 2] <<]
Populate "Consequence if unchanged" before assigning a verdict to any row.

| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if unchanged |

If all HOLDS: emit "NULL_DELTA: INERTIA RETAINED ACROSS ALL DIMENSIONS." Stop.

EXIT CRITERION: All dimensions adjudicated; NULL_DELTA if all HOLDS; blocked if any
DEFEATED row has empty "Consequence if unchanged".

---

## Phase 6 -- Change Proposals (DEFEATED dimensions only)

[>> SECTION SCOPE: Gate-exclusion text, proposal generation, and row-level bias labeling.
     No verdict redefinitions. No schema contract clauses.
     The higher-order failure mode protected against in this phase is
     LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE.
     Note that LEVEL 1: CONFIRMATION ANCHORING AT THE EVIDENCE SCAN SURFACE does not
     protect against LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION
     SURFACE; both levels must be checked independently per the PROPOSAL BIAS AUDIT
     guard below. A C-24 auditor can traverse from this scope note to the guard using
     the formal label LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION
     SURFACE without reading phase execution content. <<]

[>> GUARD: INERTIA-GATE [Site 2 of 2 -- Phase 6 entry] <<]
[>> HOLDS dimensions have no path here. Independent of Site 1. <<]

[>> GUARD: PROPOSAL BIAS AUDIT [§9] <<]
[>> Bias blocked: two distinct failure modes at two distinct granularities <<]
[>> Mechanism:
     LEVEL 1 -- PHASE-LEVEL GATE (INERTIA-GATE, Site 2 above):
     LEVEL 1 prevents SYSTEMIC PHASE STRUCTURE BIAS. Addresses failure at phase-level
     granularity. Does not address individual proposals.

     LEVEL 2 -- ROW-LEVEL BIAS LABELING ("Bias blocked by guard" column):
     LEVEL 2 prevents MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE.
     Operates below phase granularity. Phase-level gate cannot block this failure mode.

     LEVEL 1 does not protect against LEVEL 2. A balanced evidence scan (LEVEL 1
     satisfied) does not prevent motivated reasoning at the proposal decision surface
     (LEVEL 2). The protection hierarchy is not transitive; both guards must be applied
     independently. A LEVEL 1 pass confers zero LEVEL 2 protection.

     BOTH LEVELS ARE REQUIRED. Each proposal row MUST carry a populated "Bias blocked
     by guard" entry naming the cognitive bias the guard prevents at that row's specific
     decision point. <<]

ENTRY CONDITION: Phase 5 EXIT CRITERION met; at least one DEFEATED; NULL_DELTA not emitted.

### 6a -- Additions
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |
Null: "ADDITIONS: none -- INERTIA holds on all addition candidates."

### 6b -- Removals and Reprioritizations
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |
Null-REMOVALS: "REMOVALS: none -- INERTIA holds."
Null-REPRIORITIZATIONS: "REPRIORITIZATIONS: none -- INERTIA holds."

All 9 namespaces must have a row. Silence is not a null declaration.

EXIT CRITERION: All tables present; all 9 namespaces covered; non-null rows carry
"Bias blocked by guard" entry. Phase 7 may NOT open.

---

## Phase 7 -- Confirmation Gate

[>> GUARD: CONFIRMATION GATE <<]
[>> GUARD: WRITE GUARD -- strategy.md NOT modified until explicit YES <<]

ENTRY CONDITION: Phase 6 EXIT CRITERION met.

Present: Phase 4 delta findings (all four categories), Phase 6 proposals (6a and 6b).

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.
INERTIA currently holds. Proposed challenges: [N] additions / [N] removals / [N] reprioritizations

Reply YES / NO / REVISED + edited table / WITHDRAW [#]
---
STOP HERE. Write nothing further until the user replies.

---

## Phase 8 -- Apply (after YES or REVISED only)

ENTRY CONDITION: Phase 7 EXIT CRITERION met.
[>> GUARD: WRITE GUARD (confirmed) <<]

Write confirmed changes. No reformatting of unchanged sections.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations.
INERTIA displaced on: [dimension list]."
```

---

## V-04 -- Combined: C-40 + C-41 + C-42 (standard formulation)

**Variation axis**: All three R17 criteria are addressed simultaneously in a direct,
combined formulation. CONTRACT B adds the STRUCTURAL/VALUE taxonomy split (C-40) and
the explicit scorer self-sufficiency assertion (C-42). The §9 guard compliance obligation
names the exact literal `'Bias blocked by guard'` (C-41). All three are present in their
clearest direct form without additional cross-reference language between the guard body
and CONTRACT B.

C-37 and C-38 carry the R16 V-05 full-credit formulations. The difference from V-05 is
that V-04 presents each criterion independently, while V-05 adds explicit mutual
reinforcement language showing how the guard and contract reinforce each other.

**Hypothesis**: The three new criteria are orthogonal at the implementation level. A
direct combined formulation that satisfies each independently achieves 10.00 without
requiring the additional cross-reference layer that V-05 adds.

**Expected score**: 56 (C-09--C-36) + 2 (C-37) + 2 (C-38) + 2 (C-39) + 2 (C-40) + 2 (C-41) + 2 (C-42) = **68/68 = 10.00**

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

[>> CONTRACT A -- Consequence field naming: The string "Consequence if unchanged" is
     the canonical name for the consequence column. This string MUST appear as the
     column header in the Phase 5 defeat assessment table. This string MUST appear as
     the column header in the Phase 6a Additions table. This string MUST appear as the
     column header in the Phase 6b Removals/Reprioritizations table. This string MUST
     appear as the field name in the Phase 5 exit criterion advancement condition.
     Any deviation from "Consequence if unchanged" at any of these four sites is a
     schema contract violation detectable against this block without reading the phases. <<]

[>> CONTRACT B -- Proposal bias column: The column "Bias blocked by guard" is a
     required column in Phase 6a and Phase 6b proposal tables. This column MUST be
     present in the table schema for both tables. Each non-null proposal row MUST
     carry a populated entry naming the cognitive bias the guard prevents at that
     row's decision point. Absence of this column from either Phase 6 table is a
     schema contract violation detectable against this block without reading Phase 6.
     Compliant value: the exact string 'Bias blocked by guard'. No approximate variant
     ('bias blocked', 'guard applied', 'both levels passed') satisfies this contract.
     Violation taxonomy (two independently labeled categories):
       STRUCTURAL: the "Bias blocked by guard" column is absent from the table schema.
         Detection rule: check column presence from table headers alone.
         A STRUCTURAL violation is detectable from table structure without reading rows.
       VALUE: the column is present but does not contain the exact string
         'Bias blocked by guard'. Detection rule: check cell value against the exact
         literal defined in this contract. A VALUE violation is detectable by comparing
         cell content to this literal without reading any other phase content.
     Each category is independently labeled and independently detectable from this
     CONTRACT B block without consulting phase execution content.
     SCORER SELF-SUFFICIENCY: A scorer reading CONTRACT B alone can verify:
       (a) Structural compliance test: whether the "Bias blocked by guard" column
           exists in the Phase 6 table schema.
       (b) Value compliance test: whether the column contains the exact string
           'Bias blocked by guard'.
     Both test types are defined in this CONTRACT B block. This self-sufficiency claim
     is falsifiable: a CONTRACT B block that makes this claim but does not name the
     exact required value string (required for test (b)) or does not define both
     violation categories as labeled types (required for (a) and (b) to be independently
     distinguishable) is internally inconsistent -- a detectable structural error. <<]

---

## Phase 1 -- Pre-Signal Defense Register

[>> SECTION SCOPE: This section contains the Phase 1 read-barrier and restart
     isolation clause ONLY. It does not contain verdict vocabulary definitions,
     INERTIA-GATE exclusion text, or schema contract clauses. <<]

[>> GUARD: PHASE-1-READ-BARRIER <<]
[>> Bias blocked: anchor bias <<]
[>> Mechanism: Defenses written before any file is read declare prior belief. <<]

FIRST-RUN ISOLATION: No files have been read yet.
DO NOT read strategy.md or any signal file before Phase 1 is complete.
If any file has been read, restart Phase 1 without it in context.

RESTART ISOLATION: Do NOT re-read any file after interruption. Write defense register
from prior knowledge only.

ENTRY CONDITION: No files have been read since Phase 1 began.

| Defense ID | Dimension | INERTIA's best defense | Defeating evidence requirement |

EXIT CRITERION: Defense register present; no file read. Phase 2 may NOT open.

---

## Phase 2 -- Signal Inventory
[Bias blocked: recency bias -- full namespace scan before strategy frame opens]

ENTRY CONDITION: Phase 1 EXIT CRITERION met.

Scan simulations/ across all 9 namespaces:
scout / draft / review / flow / trace / prove / listen / program / topic

Read TOPICS.md. Record STRATEGY DATE. Classify each artifact as NEW or PRIOR.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

All 9 namespaces must appear with explicit null rows for empty namespaces.

[>> GUARD: SIGNAL READ-LOCK <<]
[>> Bias blocked: confirmation bias; vocabulary contamination <<]
[>> Signal files may NOT be re-read after this inventory is written. <<]

EXIT CRITERION: Inventory present; all 9 namespaces covered; SIGNAL READ-LOCK in effect.

---

## Phase 3 -- Read Strategy
[Bias blocked: framing bias -- signals classified; strategy vocabulary cannot anchor retroactively]

ENTRY CONDITION: Phase 2 EXIT CRITERION met.

Read strategy.md. Record STRATEGY DATE, goal statement, planned signals by namespace.

EXIT CRITERION: STRATEGY DATE recorded; goal and planned signals present.

---

## Phase 4 -- Delta Analysis
[Bias blocked: confirmation bias -- four-category forcing function]

ENTRY CONDITION: Phase 3 EXIT CRITERION met.

### CONFIRMED
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "CONFIRMED: none -- no NEW artifacts validate INERTIA's assumptions."

### EXPANDED
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "EXPANDED: none -- no NEW artifacts expand INERTIA's assumptions."

### UNEXPECTED
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "UNEXPECTED: none -- no NEW artifacts reveal uncovered dimensions."

### CHALLENGED
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "CHALLENGED: none -- no NEW artifacts challenge INERTIA's assumptions."

EXIT CRITERION: All four categories present with labeled nulls; each NEW artifact covered.

---

## Verdict Vocabulary

[>> SECTION SCOPE: Verdict definitions ONLY. <<]
[>> GUARD: VERDICT SEMANTICS BLOCK <<]
[>> Bias blocked: definitional ambiguity -- both outcomes fully specified <<]

DEFEATED: Evidence overcomes INERTIA's defense. Forward path: Phase 6.
HOLDS: INERTIA survives. No path to Phase 6.

Confidence: HIGH (2+ independent artifacts) / MEDIUM (1 artifact) / LOW (inference).

---

## Phase 5 -- INERTIA DEFEAT ASSESSMENT

[>> SECTION SCOPE: Gate-exclusion and consequence blocking enforcement ONLY. <<]

[>> GUARD: INERTIA-GATE [Site 1 of 2 -- Phase 5 entry] <<]
[>> Only DEFEATED dimensions advance to Phase 6. Independent Site 2 at Phase 6. <<]

ENTRY CONDITION: Phase 4 EXIT CRITERION met.

Apply Verdict Vocabulary above. Do not redefine verdict semantics here.

[>> GUARD: CONSEQUENCE GATE [Site 1 of 2] <<]
[>> Populate "Consequence if unchanged" before assigning any verdict. <<]

| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if unchanged |

If all HOLDS: emit "NULL_DELTA: INERTIA RETAINED ACROSS ALL DIMENSIONS." Stop.

EXIT CRITERION: All dimensions adjudicated; blocked if DEFEATED rows lack consequence.

---

## Phase 6 -- Change Proposals (DEFEATED dimensions only)

[>> SECTION SCOPE: Gate-exclusion text, proposal generation, and row-level bias labeling.
     No verdict redefinitions. No schema contract clauses.
     The higher-order failure mode protected against in this phase is
     LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE.
     Note that LEVEL 1: CONFIRMATION ANCHORING AT THE EVIDENCE SCAN SURFACE does not
     protect against LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION
     SURFACE; both levels must be checked independently per the PROPOSAL BIAS AUDIT
     guard below. A C-24 auditor can traverse from this scope note to the guard using
     the formal label LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION
     SURFACE without reading phase execution content. <<]

[>> GUARD: INERTIA-GATE [Site 2 of 2 -- Phase 6 entry] <<]
[>> HOLDS dimensions have no path here. Independent of Site 1. <<]

[>> GUARD: PROPOSAL BIAS AUDIT [§9] <<]
[>> Bias blocked: two distinct failure modes at two distinct granularities <<]
[>> Mechanism:
     LEVEL 1 -- PHASE-LEVEL GATE (INERTIA-GATE, Site 2 above):
     LEVEL 1 prevents SYSTEMIC PHASE STRUCTURE BIAS -- treating the existence of the
     proposal phase as implicit evidence that change is warranted. Addresses failure at
     phase-level granularity. Does not address individual proposals.

     LEVEL 2 -- ROW-LEVEL BIAS LABELING ("Bias blocked by guard" column):
     LEVEL 2 prevents MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE.
     Operates below phase granularity; present even when LEVEL 1 fires correctly. The
     phase-level gate cannot block this failure mode. Row-level labeling addresses it
     where it occurs.

     LEVEL 1 does not protect against LEVEL 2. A balanced evidence scan (LEVEL 1
     satisfied) does not prevent motivated reasoning at the proposal decision surface
     (LEVEL 2). The protection hierarchy is not transitive; both guards must be applied
     independently. A LEVEL 1 pass confers zero LEVEL 2 protection.

     COMPLIANCE OBLIGATION: Every §6 proposal row must carry 'Bias blocked by guard'
     in the Bias blocked by guard column. This is the exact required value.
     A non-null entry that deviates from 'Bias blocked by guard' is a VALUE violation
     per the violation taxonomy defined in CONTRACT B. <<]

ENTRY CONDITION: Phase 5 EXIT CRITERION met; at least one DEFEATED; NULL_DELTA not emitted.

### 6a -- Additions
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |
Null: "ADDITIONS: none -- INERTIA holds on all addition candidates."

### 6b -- Removals and Reprioritizations
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because | Bias blocked by guard |
Null-REMOVALS: "REMOVALS: none -- INERTIA holds."
Null-REPRIORITIZATIONS: "REPRIORITIZATIONS: none -- INERTIA holds."

All 9 namespaces must have a row. Silence is not a null declaration.

EXIT CRITERION: All tables present; all 9 namespaces covered; non-null rows carry
populated "Bias blocked by guard" entry. Phase 7 may NOT open.

---

## Phase 7 -- Confirmation Gate

[>> GUARD: CONFIRMATION GATE <<]
[>> GUARD: WRITE GUARD -- strategy.md NOT modified until explicit YES <<]

ENTRY CONDITION: Phase 6 EXIT CRITERION met.

Present: Phase 4 delta findings (all four categories), Phase 6 proposals (6a and 6b).

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.
INERTIA currently holds. Proposed challenges: [N] additions / [N] removals / [N] reprioritizations

Reply YES to displace INERTIA on all listed dimensions
Reply NO to retain INERTIA (all dimensions unchanged)
Reply REVISED + edited table to displace INERTIA on custom dimensions
Reply WITHDRAW [#] to remove specific proposals before confirming
---
STOP HERE. Write nothing further until the user replies.

---

## Phase 8 -- Apply (after YES or REVISED only)

ENTRY CONDITION: Phase 7 EXIT CRITERION met.
[>> GUARD: WRITE GUARD (confirmed) <<]

Write confirmed changes. No reformatting of unchanged sections.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations.
INERTIA displaced on: [dimension list]."
```

---

## V-05 -- Combined: C-40 + C-41 + C-42 (maximal, mutual reinforcement)

**Variation axis**: All three R17 criteria are addressed with maximum structural rigor.
The key differences from V-04: (1) the §9 compliance obligation explicitly states that
the guard body is independently sufficient for value identification AND names CONTRACT B
as the governing compliance document -- making the mutual reinforcement between guard
and contract an explicit, declared property; (2) the CONTRACT B self-sufficiency
assertion includes a falsifiability clause that names C-39 and C-40 as structural
consistency dependencies; (3) CONTRACT B's taxonomy split includes explicit independent
detection logic statements making each category machine-auditable.

C-37 and C-38 carry the R16 V-05 full-credit formulations.

**Hypothesis**: V-04 achieves 10.00 through independent satisfaction of each criterion.
V-05 achieves the same score but through a tighter structural architecture where the
guard and contract explicitly declare their mutual reinforcement relationship, making
the compliance system self-documenting at every site. This produces a prompt whose
correctness is verifiable from structural declarations alone, without relying on inferred
consistency between separate blocks.

**Expected score**: 56 (C-09--C-36) + 2 (C-37) + 2 (C-38) + 2 (C-39) + 2 (C-40) + 2 (C-41) + 2 (C-42) = **68/68 = 10.00**

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

[>> CONTRACT A -- Consequence field naming: The string "Consequence if unchanged" is
     the canonical name for the consequence column. This string MUST appear as the
     column header in the Phase 5 defeat assessment table. This string MUST appear as
     the column header in the Phase 6a Additions table. This string MUST appear as the
     column header in the Phase 6b Removals/Reprioritizations table. This string MUST
     appear as the field name in the Phase 5 exit criterion advancement condition.
     Any deviation from "Consequence if unchanged" at any of these four sites is a
     schema contract violation detectable against this block without reading the phases. <<]

[>> CONTRACT B -- Proposal bias column: The column "Bias blocked by guard" is a
     required column in Phase 6a and Phase 6b proposal tables. This column MUST be
     present in the table schema for both tables. Each non-null proposal row MUST
     carry a populated entry naming the cognitive bias the guard prevents at that
     row's decision point. Absence of this column from either Phase 6 table is a
     schema contract violation detectable against this block without reading Phase 6.
     Compliant value: the exact string 'Bias blocked by guard'. No approximate variant
     ('bias blocked', 'guard applied', 'both levels passed') satisfies this contract.
     Violation taxonomy (two independently labeled categories with independent
     detection logic):
       STRUCTURAL: the "Bias blocked by guard" column is absent from the table schema.
         Detection rule: check column presence from table headers alone, without
         reading any row content or consulting phase execution output. A STRUCTURAL
         violation is identifiable from table structure independently of all row values.
         This category is independently referenceable by the label STRUCTURAL.
       VALUE: the "Bias blocked by guard" column is present in the table schema but
         does not contain the exact string 'Bias blocked by guard' in one or more rows.
         Detection rule: check each cell value against the exact literal defined in
         this contract. A VALUE violation is identifiable by comparing cell content
         to the exact literal 'Bias blocked by guard' defined here, without consulting
         any other phase content, guard text, or external definition.
         This category is independently referenceable by the label VALUE.
     STRUCTURAL violations are detectable without reading row content.
     VALUE violations are detectable without reading phase content beyond cell values.
     Each category is independently labeled, independently detectable, and independently
     referenceable from this CONTRACT B block alone.
     SCORER SELF-SUFFICIENCY DECLARATION: A scorer reading CONTRACT B alone can verify:
       (a) Structural compliance test: whether the "Bias blocked by guard" column
           exists in the Phase 6 table schema. Detection: table headers, no row read.
       (b) Value compliance test: whether each cell in the "Bias blocked by guard"
           column contains the exact string 'Bias blocked by guard'. Detection: cell
           value comparison against the exact literal defined in this block.
     Both test types are defined in this CONTRACT B block. No external source is
     required to perform either test. This declaration is falsifiable as a structural
     consistency check: a CONTRACT B block that makes this self-sufficiency claim but
     omits the exact required value string (prerequisite for test (b)) or omits the
     labeled violation taxonomy (prerequisite for independently distinguishable test
     execution) is internally inconsistent -- a detectable structural error that does
     not require reading phase content to identify. <<]

---

## Phase 1 -- Pre-Signal Defense Register

[>> SECTION SCOPE: This section contains the Phase 1 read-barrier and restart
     isolation clause ONLY. It does not contain verdict vocabulary definitions,
     INERTIA-GATE exclusion text, or schema contract clauses. A reviewer auditing
     the read-barrier does not encounter content from the Verdict Vocabulary section,
     either INERTIA-GATE site, or the Output Schema block. <<]

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
for empty namespaces); SIGNAL READ-LOCK in effect. Phase 3 may NOT open until this is met.

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
     Phase 1 read-barrier language, INERTIA-GATE exclusion text, schema contract clauses,
     or consequence blocking enforcement. A reviewer auditing verdict semantics does not
     encounter content from Phase 1, either INERTIA-GATE site, the consequence gate,
     or the Output Schema block. <<]

[>> GUARD: VERDICT SEMANTICS BLOCK <<]
[>> Bias blocked: definitional ambiguity -- both verdict outcomes fully specified as
     standalone definitions, independently verifiable without reading Phase 5 <<]

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
     enforcement ONLY. It does not redefine verdict semantics (defined in Verdict
     Vocabulary above). It does not contain restart isolation language or schema
     contract clauses. A reviewer auditing Phase 5 does not encounter verdict
     redefinitions, restart clause text, or Output Schema content. <<]

[>> GUARD: INERTIA-GATE [Site 1 of 2 -- Phase 5 entry] <<]
[>> Bias blocked: action-default bias; status-quo neglect <<]
[>> Mechanism: Only DEFEATED dimensions advance to Phase 6. HOLDS dimensions have
     no path to Phase 6. This enforcement is at the Phase 5 entry site. A second
     independent enforcement exists at Phase 6 entry (Site 2 of 2). <<]

ENTRY CONDITION: Phase 4 EXIT CRITERION met (all four delta categories present).
Do NOT open Phase 5 until Phase 4 EXIT CRITERION is confirmed in output above.

Apply the Verdict Vocabulary defined above. Do not redefine verdict semantics here.
Any inline DEFEATED or HOLDS definition appearing in this phase is a structural
violation of the single-source guarantee established by the Verdict Vocabulary block.

[>> GUARD: CONSEQUENCE GATE [Site 1 of 2 -- table entry] <<]
[>> Bias blocked: consequence-omission bias -- consequence stated before verdict assigned <<]
[>> Mechanism: Requiring the consequence field before the verdict prevents post-hoc
     rationalization. This rule is stated at this preamble site independently. It does
     not delegate to the Phase 5 exit criterion to carry the constraint. <<]
Any row with an empty "Consequence if unchanged" field cannot be evaluated and cannot
advance. Populate "Consequence if unchanged" before assigning a verdict to that row.

| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if unchanged |

If all verdicts are HOLDS: emit "NULL_DELTA: INERTIA RETAINED ACROSS ALL DIMENSIONS."
Stop. Phase 6 does NOT open.

EXIT CRITERION: Verdict table complete; all dimensions adjudicated; NULL_DELTA emitted
if all HOLDS; exit blocked if any DEFEATED row has an empty "Consequence if unchanged"
field -- this blocking rule is stated at this exit criterion site independently. At
least one DEFEATED verdict with populated "Consequence if unchanged" to proceed.

---

## Phase 6 -- Change Proposals (DEFEATED dimensions only)

[>> SECTION SCOPE: This section contains gate-exclusion text, proposal generation, and
     row-level bias labeling. It does not redefine verdict semantics. It does not contain
     schema contract clauses. A reviewer auditing the Phase 6 gate does not encounter
     verdict redefinitions or Output Schema content.
     The higher-order failure mode protected against in this phase is
     LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE.
     Note that LEVEL 1: CONFIRMATION ANCHORING AT THE EVIDENCE SCAN SURFACE does not
     protect against LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION
     SURFACE; both levels must be checked independently per the PROPOSAL BIAS AUDIT
     guard below. A C-24 auditor checking this scope can traverse from this scope note
     to the guard using the formal label LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL
     PROPOSAL DECISION SURFACE without reading phase execution content. Row-level bias
     labeling is an explicit named scope item of this phase, enforced by the PROPOSAL
     BIAS AUDIT guard [§9] co-located at this phase entry. <<]

[>> GUARD: INERTIA-GATE [Site 2 of 2 -- Phase 6 entry] <<]
[>> Bias blocked: action-default bias <<]
[>> Mechanism: HOLDS dimensions have no row and no path to this phase. This enforcement
     is independent of Site 1 at Phase 5. A model that bypasses Phase 5 and arrives
     directly at Phase 6 still encounters this gate. HOLDS exclusion is enforced here
     without relying on the Phase 5 site to carry the constraint. A reviewer can
     confirm HOLDS exclusion from this block alone, without reading Phase 5. <<]

[>> GUARD: PROPOSAL BIAS AUDIT [§9] <<]
[>> Bias blocked: two distinct failure modes at two distinct granularities <<]
[>> Mechanism:
     LEVEL 1 -- PHASE-LEVEL GATE (INERTIA-GATE, Site 2 above):
     LEVEL 1 prevents SYSTEMIC PHASE STRUCTURE BIAS -- the tendency to treat the
     existence of the proposal phase as implicit evidence that change is warranted,
     before any individual row is evaluated. This failure mode operates at the phase
     boundary. The INERTIA-GATE at phase entry addresses this failure mode at the
     phase-level granularity. It does not address individual proposals.

     LEVEL 2 -- ROW-LEVEL BIAS LABELING ("Bias blocked by guard" column):
     LEVEL 2 prevents MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE --
     justifying a pre-decided change after a signal suggests it, without surfacing the
     cognitive pull that drove the proposal framing. This failure mode operates below
     phase granularity: it is present even in a run where the phase-level gate fired
     correctly, because it occurs at the individual proposal row's decision point. The
     phase-level gate does not evaluate individual proposals and cannot block this
     failure mode. Row-level labeling addresses it where it occurs.

     LEVEL 1 does not protect against LEVEL 2. A balanced evidence scan (LEVEL 1
     satisfied) does not prevent motivated reasoning at the proposal decision surface
     (LEVEL 2). The protection hierarchy is not transitive; both guards must be applied
     independently. A LEVEL 1 pass confers zero LEVEL 2 protection.

     BOTH LEVELS ARE REQUIRED. Presence of one without the other is a structural gap
     in bias coverage.

     COMPLIANCE OBLIGATION: Every §6 proposal row must carry the exact string
     'Bias blocked by guard' in the Bias blocked by guard column. This exact literal --
     'Bias blocked by guard' -- is the required value. This value is named here in the
     §9 guard body; a scorer reading this guard block can identify the required column
     value without consulting CONTRACT B. CONTRACT B governs compliance: it defines the
     STRUCTURAL and VALUE violation taxonomy and declares scorer self-sufficiency for
     both compliance tests. This guard and CONTRACT B are mutually reinforcing: the
     guard declares the required value at the obligation site; CONTRACT B defines the
     violation taxonomy and governs compliance. Each is independently sufficient for
     value identification: a scorer reading only the §9 guard body finds the required
     literal; a scorer reading only CONTRACT B finds the required literal plus the
     taxonomy split and self-sufficiency assertion. <<]

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

```json
{"round": "R17", "rubric_version": "v17", "denominator": 68, "variations": {"V-01": {"C-37": 2, "C-38": 2, "C-39": 2, "C-40": 2, "C-41": 0, "C-42": 0, "expected_total": 64, "expected_score": 9.41}, "V-02": {"C-37": 2, "C-38": 2, "C-39": 2, "C-40": 1, "C-41": 2, "C-42": 0, "expected_total": 65, "expected_score": 9.56}, "V-03": {"C-37": 2, "C-38": 2, "C-39": 2, "C-40": 2, "C-41": 0, "C-42": 2, "expected_total": 66, "expected_score": 9.71}, "V-04": {"C-37": 2, "C-38": 2, "C-39": 2, "C-40": 2, "C-41": 2, "C-42": 2, "expected_total": 68, "expected_score": 10.0}, "V-05": {"C-37": 2, "C-38": 2, "C-39": 2, "C-40": 2, "C-41": 2, "C-42": 2, "expected_total": 68, "expected_score": 10.0}}, "top_expected": 10.0, "gradient": [9.41, 9.56, 9.71, 10.0, 10.0], "new_criteria_under_test": ["C-40: CONTRACT B STRUCTURAL/VALUE labeled taxonomy split", "C-41: §9 guard compliance obligation names exact 'Bias blocked by guard' literal", "C-42: CONTRACT B explicit scorer self-sufficiency assertion with falsifiability clause"]}
```
