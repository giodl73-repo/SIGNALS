---
skill: quest-variate
skill_target: topic-roadmap
round: R18
date: 2026-03-17
rubric_version: v18
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single:
    V-01: guard_governing_declaration_c43 -- §9 compliance obligation declares CONTRACT B as governing authority inside obligation statement; self-sufficiency assertion uses test-type names only (C-44=FAIL)
    V-02: assertion_prerequisite_naming_c44 -- self-sufficiency assertion names structural prerequisites by property type (exact-value requirement, taxonomy-split requirement); §9 obligation names exact literal but does not declare governing authority (C-43=FAIL)
    V-03: partial_governing_plus_full_c44 -- §9 preamble annotation names CONTRACT B as governing but obligation statement itself does not (C-43=PARTIAL); assertion names structural prerequisites by property type (C-44=FULL)
  combined:
    V-04: c43+c44 standard -- governing declaration inside obligation statement + structural prerequisites named by property type; direct formulation
    V-05: c43+c44 maximal -- bidirectional governing declaration with CONTRACT B cross-referencing §9; assertion names structural prerequisites with machine-verifiable validity conditions declared inside assertion block
rubric_anchor: >
  v18 adds C-43 (§9 guard body compliance obligation declares CONTRACT B as governing
  authority for the required value, with governing reference inside the obligation
  statement itself -- bidirectional pointer: CONTRACT B declares value; guard names
  value and declares CONTRACT B as source authority) and C-44 (CONTRACT B self-
  sufficiency assertion names its own structural prerequisites -- exact-value requirement
  and taxonomy-split requirement -- as validity conditions, converting assertion from
  a coverage claim into a self-auditing consistency contract). Formula denominator
  68->72 (36 aspirational x 2). R17 V-05 scores 72/72 = 10.00 under v18; R17 V-04
  drops to 68/72 = 9.44 (C-43=FAIL: no governing declaration; C-44=FAIL: no
  prerequisite-by-property-type naming). An R18 variate satisfying both simultaneously
  at FULL achieves 68+2+2 = 72/72 = 10.00.
round_targets: >
  C-43 full pass (2): The §9 compliance obligation names the exact literal 'Bias blocked
  by guard' (C-41 satisfied) AND explicitly declares CONTRACT B by its structural label
  as the governing authority for that value requirement; the governing reference is
  located inside the §9 compliance obligation statement itself, not in a preamble
  annotation, guard title, or separate parenthetical; a scorer reading the §9 guard
  body can trace the value requirement to CONTRACT B without consulting any section
  outside §9.
  C-44 full pass (2): CONTRACT B's self-sufficiency assertion explicitly names both
  structural prerequisites -- the exact-value requirement (C-39 equivalent: exact
  literal 'Bias blocked by guard' present in CONTRACT B) and the taxonomy-split
  requirement (C-40 equivalent: STRUCTURAL and VALUE formally labeled) -- as validity
  conditions for the assertion; prerequisites are named inside the assertion block or
  directly attached consistency clause that is part of CONTRACT B; a scorer can
  determine from assertion text alone that failing either named prerequisite is an
  internal inconsistency detectable without inspecting phase content.
orthogonality_notes: >
  C-43 depends on C-41 FULL (guard must name exact literal for governing reference to
  be meaningful). C-44 depends on C-42 FULL (self-sufficiency assertion must exist
  before it can name its own prerequisites). All five variations carry C-37 through
  C-42 at FULL to enable clean isolation testing of C-43 and C-44.
  V-01 (C-43=FULL, C-44=FAIL): governing declaration present in obligation statement;
    assertion names test types, not structural property types.
  V-02 (C-43=FAIL, C-44=FULL): assertion names structural prerequisites; obligation
    names exact literal but does not declare governing authority.
  V-03 (C-43=PARTIAL, C-44=FULL): governing reference in preamble annotation only;
    assertion names structural prerequisites at FULL.
  V-04 (C-43=FULL, C-44=FULL): standard combined formulation.
  V-05 (C-43=FULL, C-44=FULL): maximal -- bidirectional framing; CONTRACT B assertion
    names §9 as enforcement site; prerequisites declared with machine-verifiable
    consistency conditions.
---

## Variation Summary

| Var | C-37 | C-38 | C-39 | C-40 | C-41 | C-42 | C-43 | C-44 | Expected | Hypothesis |
|-----|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:--------:|------------|
| V-01 | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FAIL | 70/72 = 9.72 | Governing declaration in obligation statement achieves C-43 independently |
| V-02 | FULL | FULL | FULL | FULL | FULL | FULL | FAIL | FULL | 70/72 = 9.72 | Structural property names in assertion achieve C-44 independently |
| V-03 | FULL | FULL | FULL | FULL | FULL | FULL | PARTIAL | FULL | 71/72 = 9.86 | Preamble annotation earns only C-43 PARTIAL even with C-44 FULL |
| V-04 | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL | 72/72 = 10.00 | Standard combined formulation achieves both at FULL |
| V-05 | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL | 72/72 = 10.00 | Maximal: bidirectional pointer + self-auditing prerequisites declared |

---

## V-01 -- Single axis: C-43 governing declaration in obligation statement

**Variation axis**: The §9 PROPOSAL BIAS AUDIT guard COMPLIANCE OBLIGATION is upgraded
in one dimension: it now explicitly declares CONTRACT B as the governing authority for
the value requirement, with the governing reference located inside the obligation
statement itself. This creates the bidirectional pointer C-43 requires: CONTRACT B
declares the governed value; the §9 obligation names the value and declares CONTRACT B
as source authority. A scorer reading the §9 obligation statement traces the value
requirement to CONTRACT B without consulting any section outside §9.

CONTRACT B's self-sufficiency assertion retains the falsifiability clause from R17 V-04,
naming test types ("structural compliance test," "value compliance test") rather than
structural property types. This earns C-42=FULL but fails C-44: the prerequisites are
named by the compliance test they enable, not by the structural property that must hold
for the assertion to be valid. C-37 through C-42 carry the R17 V-05 full-credit
formulations throughout.

**Hypothesis**: C-43 full pass requires the governing reference to be located inside the
compliance obligation statement itself -- not in a preamble annotation, guard title, or
parenthetical clause. Placing "CONTRACT B is the governing authority for this value
requirement" inside the COMPLIANCE OBLIGATION text achieves C-43=2. The self-sufficiency
assertion's use of test-type names rather than structural property type names holds
C-44 at FAIL, confirming C-43 and C-44 as independently testable axes.

**Expected score**: 56 (C-09--C-36) + 2 (C-37) + 2 (C-38) + 2 (C-39) + 2 (C-40) + 2 (C-41) + 2 (C-42) + 2 (C-43) + 0 (C-44) = **70/72 = 9.72**

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
     required to perform either test. This declaration is falsifiable: a CONTRACT B
     block that makes this self-sufficiency claim but fails the structural compliance
     test precondition (no exact value string defined, making test (b) impossible to
     execute) or fails the value compliance test precondition (no independently labeled
     violation categories, making tests (a) and (b) indistinguishable) is internally
     inconsistent -- a detectable structural error that does not require reading phase
     content to identify. <<]

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
     'Bias blocked by guard' in the Bias blocked by guard column. CONTRACT B is the
     governing authority for this value requirement: it defines the compliant value
     string, the STRUCTURAL and VALUE violation taxonomy, and the scorer self-
     sufficiency declaration. A scorer reading this compliance obligation statement
     identifies both the required value 'Bias blocked by guard' and CONTRACT B as
     the governing source for that value requirement, without consulting any section
     outside this §9 obligation statement. <<]

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

## V-02 -- Single axis: C-44 structural prerequisite naming in assertion

**Variation axis**: CONTRACT B's self-sufficiency assertion is upgraded in one dimension:
the falsifiability clause now names the structural prerequisites by property type rather
than by the test they enable. V-01 named "structural compliance test" and "value
compliance test" as the failure conditions; V-02 names "exact-value requirement" (the
C-39 equivalent: the exact literal 'Bias blocked by guard' must be present in CONTRACT B
as the defined compliant value) and "taxonomy-split requirement" (the C-40 equivalent:
STRUCTURAL and VALUE must be formally labeled as independently detectable categories).
These are the structural properties whose absence makes the self-sufficiency claim
internally inconsistent -- named as validity conditions for the assertion itself.

The §9 compliance obligation names the exact literal 'Bias blocked by guard' and
references CONTRACT B for the violation taxonomy, but does not declare CONTRACT B
as the governing authority for the value requirement. No governing declaration appears
inside the obligation statement -- only a reference to "the violation taxonomy defined
in CONTRACT B." C-43=FAIL.

**Hypothesis**: C-44 full pass requires the falsifiability clause to name prerequisites
by structural property type, not by the test type they enable. "exact-value requirement"
and "taxonomy-split requirement" are the structural property names; a CONTRACT B that
makes the self-sufficiency claim while lacking either named property is detectable as
internally inconsistent from the assertion text alone. C-43 stays at FAIL because the
obligation references CONTRACT B for taxonomy but does not declare it as governing
authority inside the obligation statement.

**Expected score**: 56 (C-09--C-36) + 2 (C-37) + 2 (C-38) + 2 (C-39) + 2 (C-40) + 2 (C-41) + 2 (C-42) + 0 (C-43) + 2 (C-44) = **70/72 = 9.72**

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
     required to perform either test. This declaration is falsifiable, with its
     validity conditions named here by structural property type:
       Prerequisite 1 -- exact-value requirement: the exact string 'Bias blocked by
         guard' must be present in CONTRACT B as the defined compliant value. Without
         the exact-value requirement, test (b) has no reference literal and cannot be
         executed. A self-sufficiency assertion made in the absence of the exact-value
         requirement is internally inconsistent and detectable as such from this block.
       Prerequisite 2 -- taxonomy-split requirement: CONTRACT B must define STRUCTURAL
         and VALUE as separately labeled, independently detectable violation categories.
         Without the taxonomy-split requirement, tests (a) and (b) are not independently
         distinguishable; a scorer cannot determine which failure type applies. A self-
         sufficiency assertion made in the absence of the taxonomy-split requirement is
         internally inconsistent and detectable as such from this block.
     Both prerequisites are named here as validity conditions for this assertion. A
     scorer determining whether this assertion is internally consistent can verify both
     prerequisites from this CONTRACT B block alone, without inspecting phase content. <<]

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
     enforcement ONLY. It does not redefine verdict semantics. It does not contain
     restart isolation language or schema contract clauses. <<]

[>> GUARD: INERTIA-GATE [Site 1 of 2 -- Phase 5 entry] <<]
[>> Bias blocked: action-default bias; status-quo neglect <<]
[>> Mechanism: Only DEFEATED dimensions advance to Phase 6. HOLDS dimensions have
     no path to Phase 6. A second independent enforcement exists at Phase 6 entry. <<]

ENTRY CONDITION: Phase 4 EXIT CRITERION met.
Do NOT open Phase 5 until Phase 4 EXIT CRITERION is confirmed in output above.

Apply the Verdict Vocabulary defined above. Do not redefine verdict semantics here.

[>> GUARD: CONSEQUENCE GATE [Site 1 of 2 -- table entry] <<]
[>> Populate "Consequence if unchanged" before assigning any verdict. <<]
Any row with an empty "Consequence if unchanged" field cannot advance.

| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if unchanged |

If all verdicts are HOLDS: emit "NULL_DELTA: INERTIA RETAINED ACROSS ALL DIMENSIONS."
Stop. Phase 6 does NOT open.

EXIT CRITERION: All dimensions adjudicated; NULL_DELTA if all HOLDS; blocked if any
DEFEATED row lacks populated "Consequence if unchanged".

---

## Phase 6 -- Change Proposals (DEFEATED dimensions only)

[>> SECTION SCOPE: Gate-exclusion text, proposal generation, and row-level bias
     labeling. No verdict redefinitions. No schema contract clauses.
     The higher-order failure mode protected against in this phase is
     LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE.
     Note that LEVEL 1: CONFIRMATION ANCHORING AT THE EVIDENCE SCAN SURFACE does not
     protect against LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION
     SURFACE; both levels must be checked independently per the PROPOSAL BIAS AUDIT
     guard below. A C-24 auditor checking this scope can traverse from this scope note
     to the guard using the formal label LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL
     PROPOSAL DECISION SURFACE without reading phase execution content. <<]

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

     LEVEL 1 does not protect against LEVEL 2. Both guards must be applied independently.

     BOTH LEVELS ARE REQUIRED.

     COMPLIANCE OBLIGATION: Every §6 proposal row must carry the exact string
     'Bias blocked by guard' in the Bias blocked by guard column. This exact literal --
     'Bias blocked by guard' -- is the required value. This value is named here in the
     §9 guard body independently; a scorer reading this guard block can identify the
     required column value without consulting CONTRACT B. A non-null entry that deviates
     from this exact string is a VALUE violation per the violation taxonomy defined in
     CONTRACT B. <<]

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

## V-03 -- Partial C-43 (preamble annotation) + Full C-44

**Variation axis**: Two changes from V-02. First, CONTRACT B's self-sufficiency
assertion retains the structural-property-type prerequisite naming from V-02 (C-44=FULL).
Second, the §9 guard is modified to reference CONTRACT B as governing -- but the
reference appears in a preamble annotation line inside the guard block, not inside the
COMPLIANCE OBLIGATION statement itself. The obligation statement names the exact literal
independently and references CONTRACT B for the violation taxonomy, but does not declare
CONTRACT B as governing authority within the obligation text. This places the governing
reference in the guard preamble rather than inside the obligation statement, testing
whether C-43 PARTIAL is earned when the governing reference exists but at the wrong
structural location.

**Hypothesis**: C-43 PARTIAL requires the governing reference to exist but be located
outside the obligation statement. Placing the governing declaration in a preamble
annotation earns PARTIAL(1) -- the reference exists, proving the design intent is
present, but it fails FULL because a scorer reading only the COMPLIANCE OBLIGATION
statement cannot trace the value to CONTRACT B without reading the preamble. C-44
at FULL raises the total to 71/72 = 9.86, confirming that partial C-43 is a distinct
structural state below FULL.

**Expected score**: 56 (C-09--C-36) + 2 (C-37) + 2 (C-38) + 2 (C-39) + 2 (C-40) + 2 (C-41) + 2 (C-42) + 1 (C-43 partial) + 2 (C-44) = **71/72 = 9.86**

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
     required to perform either test. This declaration is falsifiable, with its
     validity conditions named here by structural property type:
       Prerequisite 1 -- exact-value requirement: the exact string 'Bias blocked by
         guard' must be present in CONTRACT B as the defined compliant value. Without
         the exact-value requirement, test (b) has no reference literal; a self-
         sufficiency assertion made without it is internally inconsistent.
       Prerequisite 2 -- taxonomy-split requirement: CONTRACT B must define STRUCTURAL
         and VALUE as separately labeled, independently detectable violation categories.
         Without the taxonomy-split requirement, tests (a) and (b) are not independently
         distinguishable; a self-sufficiency assertion made without it is internally
         inconsistent.
     Both prerequisites are named here as validity conditions. A scorer verifying
     whether this assertion is internally consistent checks both prerequisites from
     this CONTRACT B block alone, without inspecting phase content. <<]

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

All 9 namespaces must appear. Zero-artifact namespaces emit an explicit null row.

[>> GUARD: SIGNAL READ-LOCK <<]
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

EXIT CRITERION: All four categories with labeled nulls; each NEW artifact covered.

---

## Verdict Vocabulary

[>> SECTION SCOPE: Verdict definitions ONLY. <<]
[>> GUARD: VERDICT SEMANTICS BLOCK <<]

DEFEATED: Evidence overcomes INERTIA's defense. Forward path: Phase 6.
HOLDS: INERTIA survives. No path to Phase 6.

Confidence: HIGH (2+ artifacts) / MEDIUM (1 artifact) / LOW (inference only).

---

## Phase 5 -- INERTIA DEFEAT ASSESSMENT

[>> SECTION SCOPE: Gate-exclusion and consequence blocking enforcement ONLY. <<]

[>> GUARD: INERTIA-GATE [Site 1 of 2 -- Phase 5 entry] <<]
[>> Only DEFEATED dimensions advance to Phase 6. <<]

ENTRY CONDITION: Phase 4 EXIT CRITERION met.

[>> GUARD: CONSEQUENCE GATE [Site 1 of 2] <<]
Populate "Consequence if unchanged" before assigning a verdict to any row.

| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if unchanged |

If all HOLDS: emit "NULL_DELTA: INERTIA RETAINED ACROSS ALL DIMENSIONS." Stop.

EXIT CRITERION: All dimensions adjudicated; blocked if DEFEATED rows lack consequence.

---

## Phase 6 -- Change Proposals (DEFEATED dimensions only)

[>> SECTION SCOPE: Gate-exclusion text, proposal generation, and row-level bias
     labeling. No verdict redefinitions. No schema contract clauses.
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
[>> Governing authority: CONTRACT B defines the value compliance contract for this
     guard; see CONTRACT B block in Output Schema for the governing specification. <<]
[>> Bias blocked: two distinct failure modes at two distinct granularities <<]
[>> Mechanism:
     LEVEL 1 -- PHASE-LEVEL GATE (INERTIA-GATE, Site 2 above):
     LEVEL 1 prevents SYSTEMIC PHASE STRUCTURE BIAS. Addresses failure at phase-level
     granularity. Does not address individual proposals.

     LEVEL 2 -- ROW-LEVEL BIAS LABELING ("Bias blocked by guard" column):
     LEVEL 2 prevents MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE.
     Operates below phase granularity. Phase-level gate cannot block this failure mode.

     LEVEL 1 does not protect against LEVEL 2. Both guards must be applied independently.

     BOTH LEVELS ARE REQUIRED.

     COMPLIANCE OBLIGATION: Every §6 proposal row must carry the exact string
     'Bias blocked by guard' in the Bias blocked by guard column. This exact literal --
     'Bias blocked by guard' -- is the required value. This value is named here in the
     §9 guard body independently; a scorer reading this guard block can identify the
     required column value without consulting CONTRACT B. A non-null entry that deviates
     from this exact string is a VALUE violation per the violation taxonomy defined in
     CONTRACT B. <<]

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

## V-04 -- Combined: C-43 + C-44 (standard formulation)

**Variation axis**: Both R18 criteria are addressed simultaneously in direct, combined
form. The §9 compliance obligation declares CONTRACT B as the governing authority inside
the obligation statement (C-43=FULL). CONTRACT B's self-sufficiency assertion names both
structural prerequisites by property type inside the assertion block (C-44=FULL). Each
criterion is satisfied independently in its clearest direct form. V-04 presents the two
criteria without additional cross-referential architecture: the guard declares governing
authority; the assertion declares its prerequisites. The mutual relationship is present
but not explicitly declared as a bidirectional architecture. The difference from V-05 is
that V-04's assertion does not cross-reference the §9 guard by name as the enforcement
site, and the governing declaration does not echo back from CONTRACT B into the guard.

**Hypothesis**: C-43 and C-44 are orthogonal at the implementation level. A direct
combined formulation satisfying each criterion independently achieves 72/72 = 10.00
without requiring the additional cross-reference layer V-05 adds.

**Expected score**: 56 (C-09--C-36) + 2 (C-37) + 2 (C-38) + 2 (C-39) + 2 (C-40) + 2 (C-41) + 2 (C-42) + 2 (C-43) + 2 (C-44) = **72/72 = 10.00**

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
     required to perform either test. This declaration is falsifiable, with its
     validity conditions named here by structural property type:
       Prerequisite 1 -- exact-value requirement: the exact string 'Bias blocked by
         guard' must be present in CONTRACT B as the defined compliant value. A self-
         sufficiency assertion made without the exact-value requirement present in
         CONTRACT B is internally inconsistent: test (b) cannot be executed without a
         reference literal, and the inconsistency is detectable from this block alone.
       Prerequisite 2 -- taxonomy-split requirement: CONTRACT B must define STRUCTURAL
         and VALUE as separately labeled, independently detectable violation categories.
         A self-sufficiency assertion made without the taxonomy-split requirement present
         is internally inconsistent: tests (a) and (b) cannot be independently executed
         without labeled categories, and the inconsistency is detectable from this block.
     Both prerequisites are named as validity conditions for this assertion. Internal
     inconsistency is machine-detectable from this CONTRACT B block without inspecting
     phase content: check whether the exact-value requirement and taxonomy-split
     requirement are both present. <<]

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
     Signal files may NOT be re-read after this inventory is written. All subsequent
     phases use the written inventory only. <<]

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
     or consequence blocking enforcement. <<]

[>> GUARD: VERDICT SEMANTICS BLOCK <<]
[>> Bias blocked: definitional ambiguity -- both verdict outcomes fully specified <<]

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

[>> SECTION SCOPE: Gate-exclusion text and consequence blocking enforcement ONLY. <<]

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

[>> SECTION SCOPE: Gate-exclusion text, proposal generation, and row-level bias
     labeling. No verdict redefinitions. No schema contract clauses.
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
     without relying on the Phase 5 site. <<]

[>> GUARD: PROPOSAL BIAS AUDIT [§9] <<]
[>> Bias blocked: two distinct failure modes at two distinct granularities <<]
[>> Mechanism:
     LEVEL 1 -- PHASE-LEVEL GATE (INERTIA-GATE, Site 2 above):
     LEVEL 1 prevents SYSTEMIC PHASE STRUCTURE BIAS -- the tendency to treat the
     existence of the proposal phase as implicit evidence that change is warranted.
     Addresses failure at phase-level granularity. Does not address individual proposals.

     LEVEL 2 -- ROW-LEVEL BIAS LABELING ("Bias blocked by guard" column):
     LEVEL 2 prevents MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE.
     Operates below phase granularity. Phase-level gate cannot block this failure mode.

     LEVEL 1 does not protect against LEVEL 2. Both guards must be applied independently.

     BOTH LEVELS ARE REQUIRED.

     COMPLIANCE OBLIGATION: Every §6 proposal row must carry the exact string
     'Bias blocked by guard' in the Bias blocked by guard column. CONTRACT B is the
     governing authority for this value requirement: it names the required value,
     defines the violation taxonomy, and asserts scorer self-sufficiency. A scorer
     reading this compliance obligation statement traces the value requirement 'Bias
     blocked by guard' to CONTRACT B as its governing source, from this obligation
     statement alone without consulting any section outside §9. <<]

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

## V-05 -- Combined: C-43 + C-44 (maximal, bidirectional + self-auditing)

**Variation axis**: Both R18 criteria at maximum structural rigor. Three differences from
V-04: (1) the §9 compliance obligation explicitly states that CONTRACT B is the governing
authority AND that the governing relationship is bidirectional -- the obligation names the
required value and names CONTRACT B as source; CONTRACT B's self-sufficiency declaration
in turn names §9 as the enforcement site where the value is required, completing the
bidirectional pointer; (2) CONTRACT B's self-sufficiency assertion names its structural
prerequisites by property type AND locates them as a dedicated consistency-audit clause
inside the assertion block, with explicit machine-verifiable framing: a reader checking
internal consistency reads the clause, identifies the two named prerequisites, and
verifies their presence without consulting phase content; (3) the consistency-audit clause
uses the structural labels EXACT-VALUE REQUIREMENT and TAXONOMY-SPLIT REQUIREMENT as
formal identifiers, making internal inconsistency detectable by label-matching alone.

**Hypothesis**: V-04 achieves 10.00 through independent satisfaction of each criterion.
V-05 achieves the same score through a tighter architecture where the guard-contract
relationship is a declared, named, bidirectional structure, and the self-sufficiency
assertion is formally self-auditing: its validity conditions are declared as a named
consistency clause, not merely inferable from the falsifiability language. This makes
CONTRACT B a self-auditing artifact: internal consistency is machine-verifiable from
the assertion block alone, without relying on a scorer's inference about what the
prerequisites must be.

**Expected score**: 56 (C-09--C-36) + 2 (C-37) + 2 (C-38) + 2 (C-39) + 2 (C-40) + 2 (C-41) + 2 (C-42) + 2 (C-43) + 2 (C-44) = **72/72 = 10.00**

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
     required to perform either test. The compliance enforcement site for this
     declaration is the PROPOSAL BIAS AUDIT guard [§9] at Phase 6 entry.
     CONSISTENCY AUDIT CLAUSE -- validity conditions for this self-sufficiency
     declaration, named here by structural property label:
       EXACT-VALUE REQUIREMENT: the exact string 'Bias blocked by guard' must be
         present in CONTRACT B as the defined compliant value. This CONTRACT B block
         satisfies the EXACT-VALUE REQUIREMENT at the "Compliant value" line above.
         A self-sufficiency declaration made without the EXACT-VALUE REQUIREMENT
         present is internally inconsistent: test (b) has no reference literal, and
         the inconsistency is machine-detectable by checking whether the EXACT-VALUE
         REQUIREMENT is present in this block.
       TAXONOMY-SPLIT REQUIREMENT: CONTRACT B must define STRUCTURAL and VALUE as
         separately labeled, independently detectable violation categories. This
         CONTRACT B block satisfies the TAXONOMY-SPLIT REQUIREMENT at the "Violation
         taxonomy" section above. A self-sufficiency declaration made without the
         TAXONOMY-SPLIT REQUIREMENT present is internally inconsistent: tests (a) and
         (b) are not independently distinguishable without labeled categories, and the
         inconsistency is machine-detectable by checking whether the TAXONOMY-SPLIT
         REQUIREMENT is present in this block.
     Both the EXACT-VALUE REQUIREMENT and the TAXONOMY-SPLIT REQUIREMENT are named
     as validity conditions for this declaration. Internal inconsistency is machine-
     detectable from this CONTRACT B block without inspecting phase content: verify
     that EXACT-VALUE REQUIREMENT is satisfied (compliant value line present) and
     TAXONOMY-SPLIT REQUIREMENT is satisfied (STRUCTURAL and VALUE categories labeled).
     A CONTRACT B block making this self-sufficiency declaration while failing either
     named requirement is detectable as internally inconsistent from this block alone. <<]

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
     'Bias blocked by guard' in the Bias blocked by guard column. CONTRACT B is the
     governing authority for this value requirement: CONTRACT B names the required value
     'Bias blocked by guard', defines the STRUCTURAL and VALUE violation taxonomy, and
     declares scorer self-sufficiency. This guard [§9] is the enforcement site named in
     CONTRACT B's self-sufficiency declaration. A scorer reading this compliance
     obligation statement identifies both the required value and CONTRACT B as the
     governing authority for that value, from within this obligation statement alone,
     without consulting any section outside §9. The guard-contract relationship is
     bidirectional: CONTRACT B declares the governed value; this §9 obligation names
     the value and declares CONTRACT B as source authority; CONTRACT B's self-sufficiency
     declaration names §9 as the enforcement site. <<]

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
{"round": "R18", "rubric_version": "v18", "denominator": 72, "variations": {"V-01": {"C-37": 2, "C-38": 2, "C-39": 2, "C-40": 2, "C-41": 2, "C-42": 2, "C-43": 2, "C-44": 0, "expected_total": 70, "expected_score": 9.72}, "V-02": {"C-37": 2, "C-38": 2, "C-39": 2, "C-40": 2, "C-41": 2, "C-42": 2, "C-43": 0, "C-44": 2, "expected_total": 70, "expected_score": 9.72}, "V-03": {"C-37": 2, "C-38": 2, "C-39": 2, "C-40": 2, "C-41": 2, "C-42": 2, "C-43": 1, "C-44": 2, "expected_total": 71, "expected_score": 9.86}, "V-04": {"C-37": 2, "C-38": 2, "C-39": 2, "C-40": 2, "C-41": 2, "C-42": 2, "C-43": 2, "C-44": 2, "expected_total": 72, "expected_score": 10.0}, "V-05": {"C-37": 2, "C-38": 2, "C-39": 2, "C-40": 2, "C-41": 2, "C-42": 2, "C-43": 2, "C-44": 2, "expected_total": 72, "expected_score": 10.0}}, "top_expected": 10.0, "gradient": [9.72, 9.72, 9.86, 10.0, 10.0], "new_criteria_under_test": ["C-43: §9 compliance obligation declares CONTRACT B as governing authority inside obligation statement (bidirectional pointer)", "C-44: self-sufficiency assertion names structural prerequisites by property type (EXACT-VALUE REQUIREMENT, TAXONOMY-SPLIT REQUIREMENT)"]}
```
