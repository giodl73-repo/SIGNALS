---
skill: quest-variate
skill_target: topic-roadmap
round: R19
date: 2026-03-17
rubric_version: v19
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single:
    V-01: triangle_closure_c45 -- CONTRACT B self-sufficiency declaration names §9 as
      enforcement site inside declaration body; CONSISTENCY AUDIT CLAUSE names
      prerequisites as validity conditions but carries no self-referential satisfaction
      confirmations (C-46=FAIL)
    V-02: audit_clause_confirmations_c46 -- CONSISTENCY AUDIT CLAUSE carries
      self-referential satisfaction confirmations with intra-block location pointers;
      CONTRACT B self-sufficiency block does not name §9 as enforcement site (C-45=FAIL)
    V-03: partial_triangle_plus_full_c46 -- §9 enforcement site reference appears in
      preamble annotation outside self-sufficiency declaration body (C-45=PARTIAL);
      CONSISTENCY AUDIT CLAUSE carries full satisfaction confirmations with intra-block
      location pointers (C-46=FULL)
  combined:
    V-04: c45+c46_partial_audit -- CONTRACT B self-sufficiency block names §9 as
      enforcement site inside declaration (C-45=FULL); CONSISTENCY AUDIT CLAUSE has
      self-referential satisfaction confirmations but no intra-block location pointers
      (C-46=PARTIAL)
    V-05: c45+c46_maximal -- §9 named inside self-sufficiency declaration body; CONSISTENCY
      AUDIT CLAUSE uses formal structural labels with self-referential satisfaction
      confirmations and intra-block location pointers; machine-verifiable by label-matching
      alone without block inspection
rubric_anchor: >
  v19 adds C-45 (CONTRACT B's self-sufficiency declaration names §9 as the enforcement
  site for the value requirement, closing the pointer triangle opened by C-43:
  §9 obligation → CONTRACT B (C-43); CONTRACT B self-sufficiency → §9 (C-45);
  CONTRACT B → governed value (C-39)) and C-46 (CONTRACT B's CONSISTENCY AUDIT CLAUSE
  carries self-referential satisfaction confirmations -- for each named prerequisite, the
  clause additionally declares that the current CONTRACT B block satisfies that prerequisite
  and identifies the specific intra-block location where the prerequisite is met, making
  the audit machine-completeable from clause text alone without block inspection). Formula
  denominator 72→76 (38 aspirational × 2). R18 V-05 scores 76/76 = 10.00 under v19 (its
  bidirectional architecture and CONSISTENCY AUDIT CLAUSE already satisfy C-45 and C-46).
  R18 V-04 drops to 72/76 = 9.47 (C-45=0: self-sufficiency block does not name §9;
  C-46=0: prerequisites named as validity conditions but no satisfaction confirmations
  with intra-block location pointers).
round_targets: >
  C-45 full pass (2): CONTRACT B's self-sufficiency block explicitly names §9 as the
  enforcement site for the value requirement inside the self-sufficiency declaration body
  or its directly attached consistency clause; a reader of CONTRACT B alone can identify
  §9 as the enforcement site without consulting any section outside CONTRACT B; C-43 FULL
  and C-42 FULL required.
  C-46 full pass (2): CONTRACT B's self-sufficiency block includes a CONSISTENCY AUDIT
  CLAUSE (formally labeled or structurally equivalent) in which each structural
  prerequisite named under C-44 (EXACT-VALUE REQUIREMENT, TAXONOMY-SPLIT REQUIREMENT)
  is accompanied by: (a) a self-referential satisfaction confirmation -- the clause states
  that this CONTRACT B block satisfies the named prerequisite -- and (b) an intra-block
  location pointer identifying the specific structural location within CONTRACT B where the
  prerequisite is met; a scorer can determine from the clause alone, without inspecting
  block content, that both prerequisites are declared satisfied and where; C-44 FULL
  required.
orthogonality_notes: >
  C-45 depends on C-43 FULL (§9→CONTRACT B leg must exist for the reverse leg to close
  the triangle) and C-42 FULL (self-sufficiency declaration must exist before it can name
  §9). C-46 depends on C-44 FULL (named prerequisites must exist before self-referential
  satisfaction can be confirmed). All five variations carry C-37 through C-44 at FULL to
  enable clean isolation testing of C-45 and C-46.
  V-01 (C-45=FULL, C-46=FAIL): §9 named inside self-sufficiency block; prerequisites
    named as validity conditions without satisfaction confirmations.
  V-02 (C-45=FAIL, C-46=FULL): CONSISTENCY AUDIT CLAUSE with satisfaction confirmations
    and intra-block pointers; §9 not named inside self-sufficiency block.
  V-03 (C-45=PARTIAL, C-46=FULL): §9 reference in preamble annotation outside
    self-sufficiency declaration body; full satisfaction confirmations with pointers.
  V-04 (C-45=FULL, C-46=PARTIAL): §9 named inside self-sufficiency block; satisfaction
    confirmations declared without intra-block location pointers.
  V-05 (C-45=FULL, C-46=FULL): maximal -- §9 named inside declaration body; CONSISTENCY
    AUDIT CLAUSE with formal structural labels, self-referential satisfaction confirmations,
    and intra-block location pointers.
---

## Variation Summary

| Var | C-37 | C-38 | C-39 | C-40 | C-41 | C-42 | C-43 | C-44 | C-45 | C-46 | Expected | Hypothesis |
|-----|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:--------:|------------|
| V-01 | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FAIL | 74/76 = 9.74 | §9 naming inside declaration achieves C-45 independently of C-46 |
| V-02 | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FAIL | FULL | 74/76 = 9.74 | Satisfaction confirmations with intra-block pointers achieve C-46 independently of C-45 |
| V-03 | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL | PARTIAL | FULL | 75/76 = 9.87 | Preamble-annotation §9 reference earns C-45 PARTIAL even when C-46 is FULL |
| V-04 | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL | PARTIAL | 75/76 = 9.87 | Satisfaction confirmations without location pointers earn C-46 PARTIAL |
| V-05 | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL | 76/76 = 10.00 | Maximal: §9 named inside declaration body + CONSISTENCY AUDIT CLAUSE with confirmations + intra-block pointers |

---

## V-01 -- Single axis: C-45 triangle closure (§9 named inside self-sufficiency declaration)

**Variation axis**: CONTRACT B's SCORER SELF-SUFFICIENCY DECLARATION is upgraded in one
dimension: it now explicitly names the PROPOSAL BIAS AUDIT guard [§9] at Phase 6 entry
as the compliance enforcement site for this declaration, with the naming located inside
the self-sufficiency declaration body. This closes the pointer triangle that C-43 opens:
§9's compliance obligation declares CONTRACT B as governing authority (C-43); CONTRACT B's
self-sufficiency declaration names §9 as enforcement site (C-45). The triangle leg
CONTRACT B → §9 is now present from within CONTRACT B. A reader of CONTRACT B alone can
identify §9 as the enforcement site without consulting any section outside CONTRACT B.

CONTRACT B's CONSISTENCY AUDIT CLAUSE names both structural prerequisites (EXACT-VALUE
REQUIREMENT and TAXONOMY-SPLIT REQUIREMENT) as validity conditions for the declaration,
but carries no self-referential satisfaction confirmations. The clause declares that a
CONTRACT B failing either named requirement is internally inconsistent, but does not
additionally state "this CONTRACT B block satisfies X at location Y." A scorer must still
inspect block content to confirm satisfaction. C-46=FAIL.

**Hypothesis**: C-45 full pass requires the §9 enforcement site naming to be located
inside the self-sufficiency declaration body or its directly attached consistency clause.
Placing "The compliance enforcement site for this declaration is the PROPOSAL BIAS AUDIT
guard [§9] at Phase 6 entry." inside the SCORER SELF-SUFFICIENCY DECLARATION achieves
C-45=2. The CONSISTENCY AUDIT CLAUSE's use of validity-condition language without
self-referential satisfaction confirmations holds C-46 at FAIL, confirming C-45 and C-46
as independently testable axes.

**Expected score**: 68 (C-09--C-42 all FULL) + 2 (C-43) + 2 (C-44) + 2 (C-45) + 0 (C-46) = **74/76 = 9.74**

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
     Validity conditions for this assertion, named here by structural property type:
       Prerequisite 1 -- exact-value requirement: the exact string 'Bias blocked by
         guard' must be present in CONTRACT B as the defined compliant value. Without
         the exact-value requirement, test (b) has no reference literal and cannot be
         executed. A self-sufficiency assertion made without the exact-value requirement
         present is internally inconsistent and detectable as such from this block.
       Prerequisite 2 -- taxonomy-split requirement: CONTRACT B must define STRUCTURAL
         and VALUE as separately labeled, independently detectable violation categories.
         Without the taxonomy-split requirement, tests (a) and (b) are not independently
         distinguishable. A self-sufficiency assertion made without the taxonomy-split
         requirement present is internally inconsistent and detectable as such from
         this block.
     Both prerequisites are named as validity conditions for this assertion. A scorer
     verifying whether this assertion is internally consistent checks both prerequisites
     from this CONTRACT B block alone, without inspecting phase content. <<]

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
[>> Bias blocked: consequence-omission bias -- consequence stated before verdict assigned <<]
Any row with an empty "Consequence if unchanged" field cannot advance.
Populate "Consequence if unchanged" before assigning a verdict to that row.

| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if unchanged |

If all verdicts are HOLDS: emit "NULL_DELTA: INERTIA RETAINED ACROSS ALL DIMENSIONS."
Stop. Phase 6 does NOT open.

EXIT CRITERION: All dimensions adjudicated; NULL_DELTA if all HOLDS; exit blocked if
any DEFEATED row has an empty "Consequence if unchanged" field. At least one DEFEATED
verdict with populated "Consequence if unchanged" to proceed.

---

## Phase 6 -- Change Proposals (DEFEATED dimensions only)

[>> SECTION SCOPE: This section contains gate-exclusion text, proposal generation, and
     row-level bias labeling. It does not redefine verdict semantics. It does not contain
     schema contract clauses.
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
     without relying on the Phase 5 site to carry the constraint. <<]

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

     BOTH LEVELS ARE REQUIRED. Presence of one without the other is a structural gap
     in bias coverage.

     COMPLIANCE OBLIGATION: Every §6 proposal row must carry the exact string
     'Bias blocked by guard' in the Bias blocked by guard column. CONTRACT B is the
     governing authority for this value requirement: it defines the required value
     'Bias blocked by guard', the STRUCTURAL and VALUE violation taxonomy, and the
     scorer self-sufficiency declaration, and names this guard [§9] as the compliance
     enforcement site. A scorer reading this compliance obligation statement identifies
     the required value 'Bias blocked by guard' and CONTRACT B as the governing source
     for that value requirement, from this obligation statement alone, without consulting
     any section outside §9. <<]

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

## V-02 -- Single axis: C-46 CONSISTENCY AUDIT CLAUSE with satisfaction confirmations

**Variation axis**: CONTRACT B's CONSISTENCY AUDIT CLAUSE is upgraded in one dimension:
each named structural prerequisite now additionally carries a self-referential satisfaction
confirmation -- a statement that this CONTRACT B block satisfies the named prerequisite --
plus an intra-block location pointer identifying where within the block the prerequisite
is met. A scorer can determine from the clause text alone, without inspecting block
content, that both prerequisites are declared satisfied and at which structural location.
Without consulting the sections referenced by the pointers, the clause is self-confirming.

CONTRACT B's self-sufficiency declaration does NOT name §9 as the compliance enforcement
site inside the declaration body. The self-sufficiency block states that both test types
are defined in CONTRACT B with no external source required, but carries no sentence naming
§9 as enforcement site. A reader of CONTRACT B alone cannot identify §9 as the
enforcement site without consulting a section outside CONTRACT B. C-45=FAIL.

**Hypothesis**: C-46 full pass requires each named prerequisite in the CONSISTENCY AUDIT
CLAUSE to carry both (a) a self-referential satisfaction confirmation and (b) an
intra-block location pointer to where the prerequisite is met within the block. Providing
"This CONTRACT B block satisfies the EXACT-VALUE REQUIREMENT at the 'Compliant value'
line above" and "This CONTRACT B block satisfies the TAXONOMY-SPLIT REQUIREMENT at the
'Violation taxonomy' section above" for both prerequisites achieves C-46=2. The absence
of any §9 naming inside the self-sufficiency declaration holds C-45 at FAIL, confirming
C-45 and C-46 as independently testable axes.

**Expected score**: 68 (C-09--C-42 all FULL) + 2 (C-43) + 2 (C-44) + 0 (C-45) + 2 (C-46) = **74/76 = 9.74**

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
     required to perform either test.
     CONSISTENCY AUDIT CLAUSE -- validity conditions for this self-sufficiency
     declaration, named here by structural property label:
       EXACT-VALUE REQUIREMENT: the exact string 'Bias blocked by guard' must be
         present in CONTRACT B as the defined compliant value. This CONTRACT B block
         satisfies the EXACT-VALUE REQUIREMENT at the "Compliant value" line above.
         Without the EXACT-VALUE REQUIREMENT, test (b) has no reference literal; a
         self-sufficiency declaration made without it is internally inconsistent and
         detectable as such from this block.
       TAXONOMY-SPLIT REQUIREMENT: CONTRACT B must define STRUCTURAL and VALUE as
         separately labeled, independently detectable violation categories. This
         CONTRACT B block satisfies the TAXONOMY-SPLIT REQUIREMENT at the "Violation
         taxonomy" section above. Without the TAXONOMY-SPLIT REQUIREMENT, tests (a)
         and (b) are not independently distinguishable; a self-sufficiency declaration
         made without it is internally inconsistent and detectable as such from this
         block.
     Both the EXACT-VALUE REQUIREMENT and the TAXONOMY-SPLIT REQUIREMENT are named
     as validity conditions for this declaration. Internal inconsistency is machine-
     detectable from this CONTRACT B block without inspecting phase content: verify
     that EXACT-VALUE REQUIREMENT is satisfied (compliant value line present) and
     TAXONOMY-SPLIT REQUIREMENT is satisfied (STRUCTURAL and VALUE categories labeled).
     A CONTRACT B block making this declaration while failing either named requirement
     is detectable as internally inconsistent from this block alone. <<]

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
[>> Bias blocked: consequence-omission bias -- consequence stated before verdict assigned <<]
Any row with an empty "Consequence if unchanged" field cannot advance.
Populate "Consequence if unchanged" before assigning a verdict to that row.

| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if unchanged |

If all verdicts are HOLDS: emit "NULL_DELTA: INERTIA RETAINED ACROSS ALL DIMENSIONS."
Stop. Phase 6 does NOT open.

EXIT CRITERION: All dimensions adjudicated; NULL_DELTA if all HOLDS; exit blocked if
any DEFEATED row has an empty "Consequence if unchanged" field. At least one DEFEATED
verdict with populated "Consequence if unchanged" to proceed.

---

## Phase 6 -- Change Proposals (DEFEATED dimensions only)

[>> SECTION SCOPE: This section contains gate-exclusion text, proposal generation, and
     row-level bias labeling. It does not redefine verdict semantics. It does not contain
     schema contract clauses.
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
     without relying on the Phase 5 site to carry the constraint. <<]

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

     BOTH LEVELS ARE REQUIRED. Presence of one without the other is a structural gap
     in bias coverage.

     COMPLIANCE OBLIGATION: Every §6 proposal row must carry the exact string
     'Bias blocked by guard' in the Bias blocked by guard column. CONTRACT B is the
     governing authority for this value requirement: it names the required value
     'Bias blocked by guard', defines the STRUCTURAL and VALUE violation taxonomy, and
     asserts scorer self-sufficiency. A scorer reading this compliance obligation
     statement traces the value requirement 'Bias blocked by guard' to CONTRACT B as
     its governing source, from this obligation statement alone, without consulting any
     section outside §9. <<]

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

## V-03 -- Partial C-45 (preamble annotation) + Full C-46

**Variation axis**: Two changes from V-02. First, a preamble annotation is added to the
CONTRACT B block -- appearing before the SCORER SELF-SUFFICIENCY DECLARATION -- that
references §9 as the compliance enforcement site. The annotation reads:
`[>> Enforcement site for the value requirement governed by this declaration: PROPOSAL
BIAS AUDIT guard [§9] at Phase 6 entry. <<]`
The self-sufficiency declaration body does not name §9. A scorer reading only the
SCORER SELF-SUFFICIENCY DECLARATION body cannot identify §9 as the enforcement site
without reading the preamble annotation that precedes it. The §9 reference exists inside
the CONTRACT B block but outside the self-sufficiency declaration body. C-45=PARTIAL.

Second, the CONSISTENCY AUDIT CLAUSE retains the full satisfaction confirmations and
intra-block location pointers from V-02 (C-46=FULL).

**Hypothesis**: C-45 PARTIAL distinguishes reference-exists-but-wrong-location from FULL
(inside declaration body). A §9 reference in a preamble annotation satisfies the
existence requirement for PARTIAL but not the structural location requirement for FULL.
C-46 at FULL raises the combined total to 75/76 = 9.87, confirming that partial C-45
is a distinct structural state with its own score band below FULL.

**Expected score**: 68 (C-09--C-42 all FULL) + 2 (C-43) + 2 (C-44) + 1 (C-45 partial) + 2 (C-46) = **75/76 = 9.87**

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
     [>> Enforcement site for the value requirement governed by this declaration:
          PROPOSAL BIAS AUDIT guard [§9] at Phase 6 entry. <<]
     SCORER SELF-SUFFICIENCY DECLARATION: A scorer reading CONTRACT B alone can verify:
       (a) Structural compliance test: whether the "Bias blocked by guard" column
           exists in the Phase 6 table schema. Detection: table headers, no row read.
       (b) Value compliance test: whether each cell in the "Bias blocked by guard"
           column contains the exact string 'Bias blocked by guard'. Detection: cell
           value comparison against the exact literal defined in this block.
     Both test types are defined in this CONTRACT B block. No external source is
     required to perform either test.
     CONSISTENCY AUDIT CLAUSE -- validity conditions for this self-sufficiency
     declaration, named here by structural property label:
       EXACT-VALUE REQUIREMENT: the exact string 'Bias blocked by guard' must be
         present in CONTRACT B as the defined compliant value. This CONTRACT B block
         satisfies the EXACT-VALUE REQUIREMENT at the "Compliant value" line above.
         Without the EXACT-VALUE REQUIREMENT, test (b) has no reference literal; a
         self-sufficiency declaration made without it is internally inconsistent and
         detectable as such from this block.
       TAXONOMY-SPLIT REQUIREMENT: CONTRACT B must define STRUCTURAL and VALUE as
         separately labeled, independently detectable violation categories. This
         CONTRACT B block satisfies the TAXONOMY-SPLIT REQUIREMENT at the "Violation
         taxonomy" section above. Without the TAXONOMY-SPLIT REQUIREMENT, tests (a)
         and (b) are not independently distinguishable; a self-sufficiency declaration
         made without it is internally inconsistent and detectable as such from this
         block.
     Both the EXACT-VALUE REQUIREMENT and the TAXONOMY-SPLIT REQUIREMENT are named
     as validity conditions for this declaration. Internal inconsistency is machine-
     detectable from this CONTRACT B block without inspecting phase content: verify
     that EXACT-VALUE REQUIREMENT is satisfied (compliant value line present) and
     TAXONOMY-SPLIT REQUIREMENT is satisfied (STRUCTURAL and VALUE categories labeled).
     A CONTRACT B block making this declaration while failing either named requirement
     is detectable as internally inconsistent from this block alone. <<]

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
[>> Bias blocked: consequence-omission bias -- consequence stated before verdict assigned <<]
Any row with an empty "Consequence if unchanged" field cannot advance.
Populate "Consequence if unchanged" before assigning a verdict to that row.

| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if unchanged |

If all verdicts are HOLDS: emit "NULL_DELTA: INERTIA RETAINED ACROSS ALL DIMENSIONS."
Stop. Phase 6 does NOT open.

EXIT CRITERION: All dimensions adjudicated; NULL_DELTA if all HOLDS; exit blocked if
any DEFEATED row has an empty "Consequence if unchanged" field. At least one DEFEATED
verdict with populated "Consequence if unchanged" to proceed.

---

## Phase 6 -- Change Proposals (DEFEATED dimensions only)

[>> SECTION SCOPE: This section contains gate-exclusion text, proposal generation, and
     row-level bias labeling. It does not redefine verdict semantics. It does not contain
     schema contract clauses.
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
     without relying on the Phase 5 site to carry the constraint. <<]

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

     BOTH LEVELS ARE REQUIRED. Presence of one without the other is a structural gap
     in bias coverage.

     COMPLIANCE OBLIGATION: Every §6 proposal row must carry the exact string
     'Bias blocked by guard' in the Bias blocked by guard column. CONTRACT B is the
     governing authority for this value requirement: it names the required value
     'Bias blocked by guard', defines the STRUCTURAL and VALUE violation taxonomy, and
     asserts scorer self-sufficiency. A scorer reading this compliance obligation
     statement traces the value requirement 'Bias blocked by guard' to CONTRACT B as
     its governing source, from this obligation statement alone, without consulting any
     section outside §9. <<]

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

## V-04 -- Combined: C-45 FULL + C-46 PARTIAL (confirmation without location pointers)

**Variation axis**: Both C-45 and C-46 are addressed simultaneously, with C-45 at FULL
and C-46 at PARTIAL. CONTRACT B's self-sufficiency declaration names §9 as enforcement
site inside the declaration body (C-45=FULL). CONTRACT B's CONSISTENCY AUDIT CLAUSE
carries self-referential satisfaction confirmations for both named prerequisites -- it
declares that this CONTRACT B block satisfies each named requirement -- but the
confirmations do not include intra-block location pointers. The clause states "This
CONTRACT B block satisfies the EXACT-VALUE REQUIREMENT" and "This CONTRACT B block
satisfies the TAXONOMY-SPLIT REQUIREMENT" without additionally naming the specific
structural location within the block where each requirement is met. A scorer reading
the clause knows both prerequisites are declared satisfied but must inspect block
content to locate the evidence of satisfaction. C-46=PARTIAL.

**Hypothesis**: C-46 PARTIAL distinguishes satisfaction-declared-without-pointer from
FULL (satisfaction declared WITH intra-block location pointer). Adding "This block
satisfies X" without "at the Y line/section above" is a structurally distinct state
below FULL: the scorer cannot determine from the clause alone WHERE in the block each
requirement is satisfied, requiring content inspection to confirm the declarations. C-45
at FULL earns 2; C-46 at PARTIAL earns 1; combined total 75/76 = 9.87.

**Expected score**: 68 (C-09--C-42 all FULL) + 2 (C-43) + 2 (C-44) + 2 (C-45) + 1 (C-46 partial) = **75/76 = 9.87**

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
         satisfies the EXACT-VALUE REQUIREMENT. Without the EXACT-VALUE REQUIREMENT,
         test (b) has no reference literal and cannot be executed; a self-sufficiency
         declaration made without it is internally inconsistent and detectable as such
         from this block.
       TAXONOMY-SPLIT REQUIREMENT: CONTRACT B must define STRUCTURAL and VALUE as
         separately labeled, independently detectable violation categories. This
         CONTRACT B block satisfies the TAXONOMY-SPLIT REQUIREMENT. Without the
         TAXONOMY-SPLIT REQUIREMENT, tests (a) and (b) are not independently
         distinguishable; a self-sufficiency declaration made without it is internally
         inconsistent and detectable as such from this block.
     Both the EXACT-VALUE REQUIREMENT and the TAXONOMY-SPLIT REQUIREMENT are named
     as validity conditions for this declaration. Satisfaction of both is declared in
     this CONSISTENCY AUDIT CLAUSE. Internal inconsistency is machine-detectable from
     this CONTRACT B block without inspecting phase content. <<]

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
[>> Bias blocked: consequence-omission bias -- consequence stated before verdict assigned <<]
Any row with an empty "Consequence if unchanged" field cannot advance.
Populate "Consequence if unchanged" before assigning a verdict to that row.

| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if unchanged |

If all verdicts are HOLDS: emit "NULL_DELTA: INERTIA RETAINED ACROSS ALL DIMENSIONS."
Stop. Phase 6 does NOT open.

EXIT CRITERION: All dimensions adjudicated; NULL_DELTA if all HOLDS; exit blocked if
any DEFEATED row has an empty "Consequence if unchanged" field. At least one DEFEATED
verdict with populated "Consequence if unchanged" to proceed.

---

## Phase 6 -- Change Proposals (DEFEATED dimensions only)

[>> SECTION SCOPE: This section contains gate-exclusion text, proposal generation, and
     row-level bias labeling. It does not redefine verdict semantics. It does not contain
     schema contract clauses.
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
     without relying on the Phase 5 site to carry the constraint. <<]

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

     BOTH LEVELS ARE REQUIRED. Presence of one without the other is a structural gap
     in bias coverage.

     COMPLIANCE OBLIGATION: Every §6 proposal row must carry the exact string
     'Bias blocked by guard' in the Bias blocked by guard column. CONTRACT B is the
     governing authority for this value requirement: it defines the required value
     'Bias blocked by guard', the STRUCTURAL and VALUE violation taxonomy, and the
     scorer self-sufficiency declaration, and names this guard [§9] as the compliance
     enforcement site. A scorer reading this compliance obligation statement identifies
     the required value 'Bias blocked by guard' and CONTRACT B as the governing source
     for that value requirement, from this obligation statement alone, without consulting
     any section outside §9. <<]

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

## V-05 -- Combined: C-45 + C-46 (maximal, bidirectional + fully self-auditing)

**Variation axis**: Both C-45 and C-46 at maximum structural rigor. Three differences
from V-04: (1) CONTRACT B's CONSISTENCY AUDIT CLAUSE carries intra-block location
pointers for both satisfaction confirmations, making each confirmation machine-verifiable
by pointer-following alone: "at the 'Compliant value' line above" and "at the 'Violation
taxonomy' section above"; (2) the §9 compliance obligation explicitly states that this
guard [§9] is the enforcement site named in CONTRACT B's self-sufficiency declaration,
completing the bidirectional cross-reference at both ends; (3) the CONSISTENCY AUDIT
CLAUSE is elevated to formal structural status with explicit machine-verification
framing: a reader checking internal consistency reads the clause, follows the two
intra-block pointers, and confirms both prerequisites are present -- without consulting
any content outside the named locations.

The result is a self-auditing CONTRACT B: a scorer reading the CONSISTENCY AUDIT CLAUSE
alone can identify both prerequisites as declared satisfied, locate the satisfying
evidence at named intra-block positions, and confirm the enforcement site without
consulting any section outside CONTRACT B.

**Hypothesis**: V-04 achieves 75/76 through C-45 FULL and C-46 PARTIAL. V-05 elevates
C-46 to FULL by adding the intra-block location pointers. The score improvement from
9.87 to 10.00 isolates the pointer requirement as the final structural step from
PARTIAL to FULL for C-46. Only V-05 achieves 10.00 under v19.

**Expected score**: 68 (C-09--C-42 all FULL) + 2 (C-43) + 2 (C-44) + 2 (C-45) + 2 (C-46) = **76/76 = 10.00**

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
         Without the EXACT-VALUE REQUIREMENT, test (b) has no reference literal; a
         self-sufficiency declaration made without it is internally inconsistent and
         machine-detectable as such by verifying whether the EXACT-VALUE REQUIREMENT
         is present at the named location in this block.
       TAXONOMY-SPLIT REQUIREMENT: CONTRACT B must define STRUCTURAL and VALUE as
         separately labeled, independently detectable violation categories. This
         CONTRACT B block satisfies the TAXONOMY-SPLIT REQUIREMENT at the "Violation
         taxonomy" section above. Without the TAXONOMY-SPLIT REQUIREMENT, tests (a)
         and (b) are not independently distinguishable; a self-sufficiency declaration
         made without it is internally inconsistent and machine-detectable as such by
         verifying whether the TAXONOMY-SPLIT REQUIREMENT is present at the named
         location in this block.
     Both the EXACT-VALUE REQUIREMENT and the TAXONOMY-SPLIT REQUIREMENT are named
     as validity conditions for this declaration. Internal inconsistency is machine-
     detectable from this CONTRACT B block without inspecting phase content: verify
     that EXACT-VALUE REQUIREMENT is satisfied (compliant value line present at the
     named location above) and TAXONOMY-SPLIT REQUIREMENT is satisfied (STRUCTURAL
     and VALUE categories labeled at the named location above). A CONTRACT B block
     making this self-sufficiency declaration while failing either named requirement
     is detectable as internally inconsistent from this CONSISTENCY AUDIT CLAUSE alone,
     without reading phase content or consulting any section outside CONTRACT B. <<]

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
     governing authority for this value requirement: CONTRACT B names the required
     value 'Bias blocked by guard', defines the STRUCTURAL and VALUE violation
     taxonomy, and declares scorer self-sufficiency. This guard [§9] is the enforcement
     site named in CONTRACT B's self-sufficiency declaration. A scorer reading this
     compliance obligation statement identifies both the required value 'Bias blocked
     by guard' and CONTRACT B as the governing authority for that value requirement,
     from within this obligation statement alone, without consulting any section outside
     §9. The guard-contract relationship is bidirectional: CONTRACT B declares the
     governed value; this §9 obligation names the value and declares CONTRACT B as
     source authority; CONTRACT B's self-sufficiency declaration names §9 as the
     enforcement site. <<]

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
{"round": "R19", "rubric_version": "v19", "denominator": 76, "variations": {"V-01": {"C-37": 2, "C-38": 2, "C-39": 2, "C-40": 2, "C-41": 2, "C-42": 2, "C-43": 2, "C-44": 2, "C-45": 2, "C-46": 0, "expected_total": 74, "expected_score": 9.74}, "V-02": {"C-37": 2, "C-38": 2, "C-39": 2, "C-40": 2, "C-41": 2, "C-42": 2, "C-43": 2, "C-44": 2, "C-45": 0, "C-46": 2, "expected_total": 74, "expected_score": 9.74}, "V-03": {"C-37": 2, "C-38": 2, "C-39": 2, "C-40": 2, "C-41": 2, "C-42": 2, "C-43": 2, "C-44": 2, "C-45": 1, "C-46": 2, "expected_total": 75, "expected_score": 9.87}, "V-04": {"C-37": 2, "C-38": 2, "C-39": 2, "C-40": 2, "C-41": 2, "C-42": 2, "C-43": 2, "C-44": 2, "C-45": 2, "C-46": 1, "expected_total": 75, "expected_score": 9.87}, "V-05": {"C-37": 2, "C-38": 2, "C-39": 2, "C-40": 2, "C-41": 2, "C-42": 2, "C-43": 2, "C-44": 2, "C-45": 2, "C-46": 2, "expected_total": 76, "expected_score": 10.0}}, "top_expected": 10.0, "gradient": [9.74, 9.74, 9.87, 9.87, 10.0], "new_criteria_under_test": ["C-45: CONTRACT B self-sufficiency declaration names §9 as enforcement site inside declaration body (triangle closure: C-43 opens §9→CONTRACT B leg; C-45 opens CONTRACT B→§9 leg)", "C-46: CONTRACT B CONSISTENCY AUDIT CLAUSE carries self-referential satisfaction confirmations with intra-block location pointers for each named prerequisite (machine-completeable audit without block inspection)"]}
```
