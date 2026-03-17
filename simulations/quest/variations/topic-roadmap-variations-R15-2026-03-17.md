Now I have enough context to generate all 5 variations. The three new criteria are:
- **C-34**: Formal titled labels on both failure modes in the PROPOSAL BIAS AUDIT guard (LEVEL 1/LEVEL 2 as referenceable labels)
- **C-35**: SECTION SCOPE includes an explicit auditor navigation note for C-24
- **C-36**: CONTRACT at absolute document-first position (before INERTIA COMPETITOR DECLARATION), with self-referential confirmation, four-site CONTRACT A, and violation-detection language in CONTRACT B

---

# topic-roadmap — Quest Variate Round 15

```yaml
skill: quest-variate
skill_target: topic-roadmap
round: R15
date: 2026-03-17
rubric_version: v15
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single:
    V-01: proposal_bias_audit_c34 -- upgrade guard to give each failure mode a formal titled label (LEVEL 1/LEVEL 2) enabling cross-reference by name
    V-02: phase6_section_scope_c35 -- add auditor navigation note confirming C-24 auditor locates row-level bias labeling from scope declaration without traversing phase content
    V-03: output_schema_contract_c36 -- CONTRACT before INERTIA COMPETITOR DECLARATION with self-referential confirmation, four-site CONTRACT A, violation-detection language
  combined:
    V-04: c34+c35 -- formal guard labels + auditor navigation note (CONTRACT unchanged from R14 V-05)
    V-05: c34+c35+c36 -- all three; CONTRACT at absolute document-first; guard labels cross-referenced in scope navigation note
rubric_anchor: >
  v15 adds C-34 (PROPOSAL BIAS AUDIT failure modes carry formal descriptive titles
  LEVEL 1/LEVEL 2 enabling cross-reference by name), C-35 (SECTION SCOPE includes
  an explicit auditor navigation note for C-24), C-36 (CONTRACT at absolute
  document-first position before INERTIA COMPETITOR DECLARATION, with self-referential
  confirmation, four-site CONTRACT A, and violation-detection language in CONTRACT B).
  Formula denominator 50->56. R14 V-01/V-02/V-03 each scored 46/50 = 9.20 under v14;
  under v15 they score 48/56 = 8.57. An R15 variate targeting all three achieves 56/56 = 10.00.
round_targets: >
  C-34 full pass (2): PROPOSAL BIAS AUDIT guard names each failure mode with a formal
  titled label (LEVEL 1: SYSTEMIC PHASE STRUCTURE BIAS, LEVEL 2: MOTIVATED REASONING
  AT THE INDIVIDUAL PROPOSAL DECISION SURFACE) co-located in the guard body; titles
  specific enough to be cited by name from CONTRACT or SECTION SCOPE.
  C-35 full pass (2): Phase 6 SECTION SCOPE includes an explicit navigation note
  stating that a C-24 auditor verifying row-level bias labeling finds it enumerated
  in the scope declaration; note identifies the enumeration item by number or label.
  C-36 full pass (2): CONTRACT is the first section in the document, preceding
  INERTIA COMPETITOR DECLARATION; self-referential confirmation statement present;
  CONTRACT A names all four consequence field sites including Phase 5 exit criterion;
  CONTRACT B includes violation-detection language enabling scorer to detect column
  absence from the CONTRACT block alone.
orthogonality_notes: >
  V-01 (C-34 FULL, C-35 partial, C-36 partial): guard labels added; SECTION SCOPE
  unchanged from R14 V-05 (no explicit auditor navigation note); CONTRACT unchanged
  from R14 V-05 (before INERTIA DECL but missing C-36 additions).
  V-02 (C-34 partial, C-35 FULL, C-36 partial): guard unchanged from R14 V-05 (labels
  absent); SECTION SCOPE upgraded with explicit auditor navigation note; CONTRACT
  unchanged from R14 V-05.
  V-03 (C-34 partial, C-35 partial, C-36 FULL): guard unchanged from R14 V-05;
  SECTION SCOPE unchanged from R14 V-05; CONTRACT upgraded to absolute document-first
  with self-referential confirmation and four-site CONTRACT A and violation-detection.
  V-04 (C-34 FULL, C-35 FULL, C-36 partial): guard labeled + scope navigation note;
  CONTRACT unchanged from R14 V-05.
  V-05 (C-34 FULL, C-35 FULL, C-36 FULL): all three; CONTRACT at absolute first;
  guard labels present in body; scope navigation note identifies enumeration item
  and cross-references LEVEL 2 label; CONTRACT B names violation-detection language.
```

## Variation Summary

| Var | C-34 | C-35 | C-36 | CONTRACT position | Expected score | Hypothesis |
|-----|------|------|------|-------------------|----------------|------------|
| V-01 | FULL | partial | partial | R14 pre-INERTIA DECL | 48/56 | Formal guard labels achieve C-34 independently without touching scope or contract |
| V-02 | partial | FULL | partial | R14 pre-INERTIA DECL | 48/56 | Explicit auditor navigation note achieves C-35 independently |
| V-03 | partial | partial | FULL | absolute document-first | 48/56 | Self-referential CONTRACT with four-site A and violation-detection B achieves C-36 independently |
| V-04 | FULL | FULL | partial | R14 pre-INERTIA DECL | 52/56 | C-34+C-35 combined; guard labels cited in scope note |
| V-05 | FULL | FULL | FULL | absolute document-first | 56/56 | All three; CONTRACT first; scope note cites LEVEL 2 label; CONTRACT B names "Bias blocked by guard" with violation-detection |

---

## V-01 — Single axis: C-34 PROPOSAL BIAS AUDIT formal titled labels

**Variation axis**: The PROPOSAL BIAS AUDIT guard at Phase 6 entry is upgraded from
R14 V-05. In R14 V-05, the guard names both failure modes with prose descriptions
(LEVEL 1 and LEVEL 2 labels appear but each is a run-on inline identifier, not a
formal titled label that stands alone as a referenceable artifact). V-01 upgrades
the guard to give each failure mode a formal descriptive title in the style of a
named artifact:

```
LEVEL 1: SYSTEMIC PHASE STRUCTURE BIAS
LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE
```

Each title is placed on its own line at the head of its failure mode paragraph,
capitalized in full, making it referenceable by label from the CONTRACT or SECTION
SCOPE without repeating the prose. The guard also asserts explicitly: "Both levels
are required. LEVEL 1 does not protect against LEVEL 2. LEVEL 2 does not protect
against LEVEL 1. These are distinct failure modes at distinct granularities. Neither
substitutes for the other."

SECTION SCOPE is unchanged from R14 V-05 (no auditor navigation note — C-35 partial).
CONTRACT is the R14 V-05 position (before INERTIA COMPETITOR DECLARATION — C-36
partial because self-referential confirmation and four-site enumeration are absent).

**Hypothesis**: C-34 full pass requires each failure mode to carry a formal titled label
co-located in the guard body that is specific enough to cite by name. R14 V-05 named
both failure modes with prose descriptions but did not give them isolated formal titles
that serve as referenceable identifiers. Adding "LEVEL 1: SYSTEMIC PHASE STRUCTURE BIAS"
and "LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE" as
formal headings achieves C-34=2 independently of C-35 and C-36.

**Expected score gain**: +2 (C-34 full) over R14 V-05 baseline = 48/56

---

```
You are running /topic:plan -- signal strategy revision for a Signal topic.

---

## OUTPUT SCHEMA CONTRACT

[>> GUARD: SCHEMA CONTRACT <<]
[>> Bias blocked: post-hoc rationalization -- consequence field name and proposal bias
     column committed before any file is read; violations detectable against this block <<]

CONTRACT A -- Consequence field name (four sites):
The exact string "Consequence if unchanged" is the canonical consequence field name.
It must appear at:
  Site 1: Phase 5 defeat assessment table -- column header
  Site 2: Phase 6a Additions table -- column header
  Site 3: Phase 6b Removals/Reprioritizations table -- column header
  Site 4: Phase 5 EXIT CRITERION -- "exit blocked if any DEFEATED row has an empty
           'Consequence if unchanged' field" clause

CONTRACT B -- Proposal bias column (two tables):
The column "Bias blocked by guard" is required in Phase 6a and Phase 6b.
Absence of this column from either table is a schema contract violation.
Each non-null proposal row must carry a populated entry naming the cognitive bias
the guard prevents at that row's decision point.

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
     enforces HOLDS exclusion at this phase entry.
     (2) PROPOSAL GENERATION: The Phase 6a Additions table and Phase 6b Removals/
     Reprioritizations tables are produced in this section.
     (3) ROW-LEVEL BIAS LABELING: The PROPOSAL BIAS AUDIT guard (immediately below,
     co-located with the INERTIA-GATE at this phase entry boundary) enforces the
     "Bias blocked by guard" column requirement. Per-row bias labeling is produced
     within this section at the individual proposal row level.
     A C-24 auditor verifying that row-level bias labeling belongs to Phase 6's
     declared scope finds it enumerated here. <<]

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

     LEVEL 1: SYSTEMIC PHASE STRUCTURE BIAS
     The tendency to treat the existence of the proposal phase as implicit evidence
     that change is warranted, before any individual row is evaluated. This failure
     mode operates at the phase boundary: the model enters a proposal-generation frame
     and produces proposals because the phase structure implies they are expected, not
     because evidence warrants them. The INERTIA-GATE at phase entry (Site 2, immediately
     above) addresses LEVEL 1 at the phase-level granularity. It does not evaluate
     individual proposals and does not address LEVEL 2.

     LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE
     Justifying a pre-decided change after a signal suggests it, without surfacing the
     cognitive pull that drove the proposal framing. This failure mode operates below
     phase granularity: it is present even in a run where LEVEL 1 was correctly blocked,
     because it occurs at the individual proposal row's decision point. The "Bias blocked
     by guard" column enforces LEVEL 2 by requiring each proposal row to name the
     specific cognitive bias the guard prevents at that row's decision surface.

     BOTH LEVELS ARE REQUIRED. LEVEL 1 does not protect against LEVEL 2. LEVEL 2 does
     not protect against LEVEL 1. These are distinct failure modes at distinct
     granularities. Neither substitutes for the other. Presence of one without the
     other is a structural gap in bias coverage. Each proposal row MUST carry a "Bias
     blocked by guard" entry naming the cognitive bias the guard prevents at that row's
     specific decision point. <<]

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

## V-02 — Single axis: C-35 SECTION SCOPE auditor navigation note

**Variation axis**: The Phase 6 SECTION SCOPE declaration is upgraded from R14 V-05.
In R14 V-05, the SECTION SCOPE lists row-level bias labeling as content type (3) and
closes with: "A C-24 auditor verifying that row-level bias labeling belongs to Phase
6's declared scope finds it enumerated here." This is an auditor navigation note in
form, but it does not identify the enumeration item by number or label — the auditor
is told "it is enumerated here" but not told which item number to look at. Under C-35,
a Full score requires the navigation note to "identify the enumeration item by number
or label."

V-02 upgrades the SECTION SCOPE to:
- Close with an explicit navigation note: "A C-24 auditor verifying row-level bias
  labeling finds it enumerated as content type (3) in the scope declaration above.
  The enumeration item is: (3) ROW-LEVEL BIAS LABELING. No traversal of Phase 6a
  or Phase 6b tables is required to confirm that row-level bias labeling is within
  this section's declared scope."

The PROPOSAL BIAS AUDIT guard is unchanged from R14 V-05 (no formal titled labels —
C-34 partial). CONTRACT is unchanged from R14 V-05 (C-36 partial).

**Hypothesis**: C-35 full pass requires the navigation note to identify the enumeration
item by number or label, enabling the auditor to go directly to the numbered item
without scanning the scope prose. The "find it enumerated here" closing in R14 V-05
tells the auditor where to look but not what to look for. Naming the item explicitly
("content type (3)") satisfies the identification requirement.

**Expected score gain**: +2 (C-35 full) over R14 V-05 baseline = 48/56

---

```
You are running /topic:plan -- signal strategy revision for a Signal topic.

---

## OUTPUT SCHEMA CONTRACT

[>> GUARD: SCHEMA CONTRACT <<]
[>> Bias blocked: post-hoc rationalization -- consequence field name and proposal bias
     column committed before any file is read; violations detectable against this block <<]

CONTRACT A -- Consequence field name (four sites):
The exact string "Consequence if unchanged" is the canonical consequence field name.
It must appear at:
  Site 1: Phase 5 defeat assessment table -- column header
  Site 2: Phase 6a Additions table -- column header
  Site 3: Phase 6b Removals/Reprioritizations table -- column header
  Site 4: Phase 5 EXIT CRITERION -- "exit blocked if any DEFEATED row has an empty
           'Consequence if unchanged' field" clause

CONTRACT B -- Proposal bias column (two tables):
The column "Bias blocked by guard" is required in Phase 6a and Phase 6b.
Absence of this column from either table is a schema contract violation.
Each non-null proposal row must carry a populated entry naming the cognitive bias
the guard prevents at that row's decision point.

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
     external boundaries.
     AUDITOR NAVIGATION NOTE (C-24): A C-24 auditor verifying that row-level bias
     labeling is within Phase 6's declared scope finds it enumerated as content type
     (3) above: "(3) ROW-LEVEL BIAS LABELING." No traversal of the Phase 6a or Phase 6b
     tables is required to confirm the enumeration -- the scope declaration itself
     identifies the item by number and label. <<]

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
     The phase-level gate (INERTIA-GATE, Site 2 above) prevents the tendency to treat
     the existence of the proposal phase as implicit evidence that change is warranted,
     before any individual row is evaluated. This failure mode operates at the phase
     boundary. The INERTIA-GATE at phase entry addresses it. It does not address
     individual proposals.

     Per-row labeling prevents motivated reasoning at the individual proposal decision
     surface -- justifying a pre-decided change after a signal suggests it, without
     surfacing the cognitive pull that drove the proposal framing. This failure mode
     operates below phase granularity: it is present even in a run where the phase-level
     gate fired correctly, because it occurs at the individual proposal row's decision
     point. The phase-level gate does not evaluate individual proposals and cannot block
     this failure mode. Row-level labeling addresses it where it occurs.

     BOTH LEVELS ARE REQUIRED. The phase-level gate does not protect against per-proposal
     motivated reasoning. The row-level column does not protect against systemic phase
     structure bias. These are distinct failure modes at distinct granularities. Presence
     of one without the other is a structural gap in bias coverage. Each proposal row
     MUST carry a "Bias blocked by guard" entry naming the cognitive bias the guard
     prevents at that row's specific decision point. <<]

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

## V-03 — Single axis: C-36 OUTPUT SCHEMA CONTRACT at absolute document-first position

**Variation axis**: The OUTPUT SCHEMA CONTRACT becomes the absolute first section of
the document — before the INERTIA COMPETITOR DECLARATION — and gains three upgrades
over R14 V-05:

1. **Self-referential confirmation statement**: "No file read instruction appears
   before this CONTRACT. No structural section appears before this CONTRACT."
2. **CONTRACT A names all four consequence field sites**, including the Phase 5 exit
   criterion as "Site 4" (R14 V-05 listed three sites in the embedded annotation but
   did not enumerate them; the standalone CONTRACT in R14 V-03 listed four sites but
   the C-36 criterion requires this to be present in the full pre-INERTIA position).
3. **CONTRACT B includes violation-detection language**: "A scorer detecting absence
   of the 'Bias blocked by guard' column from either Phase 6 table can confirm that
   violation from this CONTRACT block alone, without reading Phase 6a or Phase 6b
   table content. The column name is 'Bias blocked by guard'; the tables are Phase 6a
   and Phase 6b; absence is the violation."

The PROPOSAL BIAS AUDIT guard is unchanged from R14 V-05 (no formal titled labels
— C-34 partial). SECTION SCOPE is unchanged from R14 V-05 (no explicit auditor
navigation note — C-35 partial).

**Hypothesis**: C-36 requires (a) CONTRACT before INERTIA COMPETITOR DECLARATION,
(b) self-referential confirmation, (c) four-site CONTRACT A, (d) violation-detection
language in CONTRACT B. R14 V-05 achieved (a) but lacked (b), and the four-site
enumeration was present but CONTRACT B did not have explicit violation-detection
phrasing as an isolated sentence. These three additions achieve C-36=2.

**Expected score gain**: +2 (C-36 full) over R14 V-05 baseline = 48/56

---

```
You are running /topic:plan -- signal strategy revision for a Signal topic.

---

## OUTPUT SCHEMA CONTRACT -- Absolute Document-First Commitment

No file read instruction appears before this CONTRACT.
No structural section appears before this CONTRACT.
This CONTRACT is the first reader-encountered content in this execution.
Both contract violations below are detectable from this block alone
without reading any phase of the execution.

CONTRACT A -- Consequence field name (four sites):
The exact string "Consequence if unchanged" is the canonical consequence field name
for this execution. It must appear at exactly four sites:
  Site 1: Phase 5 defeat assessment table -- column header "Consequence if unchanged"
  Site 2: Phase 6a Additions table -- column header "Consequence if unchanged"
  Site 3: Phase 6b Removals/Reprioritizations table -- column header "Consequence if unchanged"
  Site 4 (exit criterion): Phase 5 EXIT CRITERION -- the blocking clause reads:
    "exit blocked if any DEFEATED row has an empty 'Consequence if unchanged' field"

A CONTRACT A violation is any deviation from "Consequence if unchanged" at any of
these four sites. Detection requires only: (a) the actual string at the site, and
(b) the canonical string above. No surrounding prose or other sections required.

CONTRACT B -- Proposal bias column (two tables):
The column "Bias blocked by guard" is a required column in Phase 6a and Phase 6b
proposal tables. A scorer detecting absence of this column from either Phase 6 table
can confirm that violation from this CONTRACT block alone, without reading Phase 6a
or Phase 6b table content. The column name is "Bias blocked by guard." The tables
are Phase 6a (Additions) and Phase 6b (Removals and Reprioritizations). Absence of
this named column from either table is the violation. Each non-null proposal row must
carry a populated entry naming the cognitive bias the guard prevents at that row's
decision point.

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
     block above. <<]

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
     within this section at the individual proposal row level.
     A C-24 auditor verifying that row-level bias labeling belongs to Phase 6's
     declared scope finds it enumerated here. <<]

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
     The phase-level gate (INERTIA-GATE, Site 2 above) prevents the tendency to treat
     the existence of the proposal phase as implicit evidence that change is warranted,
     before any individual row is evaluated. This failure mode operates at the phase
     boundary. It does not address individual proposals.

     Per-row labeling prevents motivated reasoning at the individual proposal decision
     surface -- justifying a pre-decided change after a signal suggests it, without
     surfacing the cognitive pull that drove the proposal framing. This failure mode
     operates below phase granularity. Row-level labeling addresses it where it occurs.

     BOTH LEVELS ARE REQUIRED. The phase-level gate does not protect against per-proposal
     motivated reasoning. The row-level column does not protect against systemic phase
     structure bias. These are distinct failure modes at distinct granularities.
     Presence of one without the other is a structural gap in bias coverage. Each
     proposal row MUST carry a "Bias blocked by guard" entry naming the cognitive bias
     the guard prevents at that row's specific decision point. <<]

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

## V-04 — Combined: C-34 + C-35 (formal guard labels + auditor navigation note)

**Variation axis**: V-01's formal titled labels (C-34) combined with V-02's auditor
navigation note (C-35). The scope note now cross-references the LEVEL 2 label from
the guard, creating a closed reference loop: the SECTION SCOPE navigation note names
"content type (3): ROW-LEVEL BIAS LABELING" and adds: "This content is enforced by
the PROPOSAL BIAS AUDIT guard co-located at Phase 6 entry, which addresses LEVEL 2:
MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE." CONTRACT is
unchanged from R14 V-05 (C-36 partial — before INERTIA COMPETITOR DECLARATION but
missing self-referential confirmation and four-site enumeration headers).

**Hypothesis**: The closed reference loop between guard labels and scope navigation
note achieves both C-34=2 and C-35=2 independently. The scope note satisfies C-35
because it identifies the enumeration item by number and label. The guard body
satisfies C-34 because each failure mode carries a formal titled label. C-36 stays
at R14 V-05 level (partial).

**Expected score gain**: +4 (C-34 full + C-35 full) over R14 V-05 baseline = 52/56

---

```
You are running /topic:plan -- signal strategy revision for a Signal topic.

---

## OUTPUT SCHEMA CONTRACT

[>> GUARD: SCHEMA CONTRACT <<]
[>> Bias blocked: post-hoc rationalization -- consequence field name and proposal bias
     column committed before any file is read; violations detectable against this block <<]

CONTRACT A -- Consequence field name (four sites):
The exact string "Consequence if unchanged" is the canonical consequence field name.
It must appear at:
  Site 1: Phase 5 defeat assessment table -- column header
  Site 2: Phase 6a Additions table -- column header
  Site 3: Phase 6b Removals/Reprioritizations table -- column header
  Site 4: Phase 5 EXIT CRITERION -- "exit blocked if any DEFEATED row has an empty
           'Consequence if unchanged' field" clause

CONTRACT B -- Proposal bias column (two tables):
The column "Bias blocked by guard" is required in Phase 6a and Phase 6b.
Absence of this column from either table is a schema contract violation.
Each non-null proposal row must carry a populated entry naming the cognitive bias
the guard prevents at that row's decision point.

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
     distinct from per-phase annotations; row-level labeling is produced inside this
     section at the individual proposal row, not at phase entry boundaries.
     AUDITOR NAVIGATION NOTE (C-24): A C-24 auditor verifying that row-level bias
     labeling is within Phase 6's declared scope finds it enumerated as content type
     (3) in the scope declaration above: "(3) ROW-LEVEL BIAS LABELING." This labeling
     is enforced by the PROPOSAL BIAS AUDIT guard co-located at Phase 6 entry, which
     addresses LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION
     SURFACE. No traversal of Phase 6a or Phase 6b table content is required to
     confirm the enumeration -- the scope declaration identifies the item by number
     and label, and names the guard that enforces it. <<]

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

     LEVEL 1: SYSTEMIC PHASE STRUCTURE BIAS
     The tendency to treat the existence of the proposal phase as implicit evidence
     that change is warranted, before any individual row is evaluated. This failure
     mode operates at the phase boundary: the model enters a proposal-generation frame
     and produces proposals because the phase structure implies they are expected, not
     because evidence warrants them. The INERTIA-GATE at Phase 6 entry (Site 2,
     immediately above) addresses LEVEL 1 at phase-level granularity. LEVEL 1 does
     not address individual proposals and does not protect against LEVEL 2.

     LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE
     Justifying a pre-decided change after a signal suggests it, without surfacing the
     cognitive pull that drove the proposal framing. This failure mode operates below
     phase granularity: it is present even in a run where LEVEL 1 was correctly blocked,
     because it occurs at the individual proposal row's decision point. The phase-level
     gate (LEVEL 1) does not evaluate individual proposals and cannot block this failure
     mode. The "Bias blocked by guard" column enforces LEVEL 2 by requiring each
     proposal row to name the specific cognitive bias the guard prevents at that row's
     decision surface. LEVEL 2 does not protect against LEVEL 1.

     BOTH LEVELS ARE REQUIRED. Neither substitutes for the other. Presence of one
     without the other is a structural gap in bias coverage. Each proposal row MUST
     carry a "Bias blocked by guard" entry naming the cognitive bias the guard prevents
     at that row's specific decision point. <<]

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

## V-05 — Combined: C-34 + C-35 + C-36 (all three — targeting 56/56)

**Variation axis**: All three criteria combined. The CONTRACT is the absolute first
section of the document — before INERTIA COMPETITOR DECLARATION — with self-referential
confirmation, four-site CONTRACT A with labeled site headers, and CONTRACT B with
explicit violation-detection language. The PROPOSAL BIAS AUDIT guard carries formal
titled labels (LEVEL 1/LEVEL 2) as referenceable identifiers in the guard body. The
Phase 6 SECTION SCOPE carries an explicit auditor navigation note that identifies the
enumeration item by number and label and cross-references the LEVEL 2 label from the
guard — creating a closed reference triangle: CONTRACT B names "Bias blocked by guard,"
SECTION SCOPE item (3) names "ROW-LEVEL BIAS LABELING" and references LEVEL 2, and
the PROPOSAL BIAS AUDIT guard body defines LEVEL 2 with a formal title.

**Hypothesis**: This is the 56/56 candidate. All three criteria are satisfied:
- C-34: formal titled labels in guard body (LEVEL 1/LEVEL 2), citeable by name
- C-35: SECTION SCOPE auditor navigation note identifies item (3) by number and label, names enforcing guard
- C-36: CONTRACT is absolute document-first; self-referential confirmation present;
  CONTRACT A names all four consequence field sites; CONTRACT B names "Bias blocked by
  guard" with violation-detection language enabling scorer to confirm absence from
  CONTRACT block alone

**Expected score gain**: +6 (C-34 full + C-35 full + C-36 full) = 56/56

---

```
You are running /topic:plan -- signal strategy revision for a Signal topic.

---

## OUTPUT SCHEMA CONTRACT -- Absolute Document-First Commitment

No file read instruction appears before this CONTRACT.
No structural section appears before this CONTRACT.
This CONTRACT is the first reader-encountered content in this execution.
Both contract violations below are detectable from this block alone,
without reading any phase of the execution.

CONTRACT A -- Consequence field name (four sites):
The exact string "Consequence if unchanged" is the canonical consequence field name
for this execution. It must appear at exactly four sites:
  Site 1 (Phase 5 table): column header -- "Consequence if unchanged"
  Site 2 (Phase 6a table): column header -- "Consequence if unchanged"
  Site 3 (Phase 6b table): column header -- "Consequence if unchanged"
  Site 4 (Phase 5 exit criterion): the blocking clause reads:
    "exit blocked if any DEFEATED row has an empty 'Consequence if unchanged' field"

A CONTRACT A violation is any deviation from "Consequence if unchanged" at any of
these four sites. Detection requires only: (a) the actual string at the site, (b) the
canonical string above. No surrounding prose or other sections required to detect the
violation.

CONTRACT B -- Proposal bias column (two tables):
The column "Bias blocked by guard" is a required column in Phase 6a (Additions) and
Phase 6b (Removals and Reprioritizations) proposal tables. A scorer detecting absence
of this column from either Phase 6 table can confirm that violation from this CONTRACT
block alone, without reading Phase 6a or Phase 6b table content. The column name is
"Bias blocked by guard." The tables are Phase 6a and Phase 6b. Absence of this named
column from either table is the violation. Each non-null proposal row must carry a
populated entry naming the cognitive bias the guard prevents at that row's decision
point.

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
     block above. <<]

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
     distinct from per-phase annotations; row-level labeling occurs inside this section
     at the individual proposal row, not at phase entry boundaries.
     AUDITOR NAVIGATION NOTE (C-24): A C-24 auditor verifying that row-level bias
     labeling is within Phase 6's declared scope finds it enumerated as content type
     (3) above: "(3) ROW-LEVEL BIAS LABELING." This labeling is enforced by the
     PROPOSAL BIAS AUDIT guard co-located at Phase 6 entry, which addresses
     LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE.
     No traversal of Phase 6a or Phase 6b table content is required -- the scope
     declaration identifies the item by number "(3)" and label "ROW-LEVEL BIAS
     LABELING" and names the guard (PROPOSAL BIAS AUDIT) and the failure mode it
     addresses (LEVEL 2). <<]

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

     LEVEL 1: SYSTEMIC PHASE STRUCTURE BIAS
     The tendency to treat the existence of the proposal phase as implicit evidence
     that change is warranted, before any individual row is evaluated. This failure
     mode operates at the phase boundary: the model enters a proposal-generation frame
     and produces proposals because the phase structure implies they are expected, not
     because evidence warrants them. The INERTIA-GATE at Phase 6 entry (Site 2,
     immediately above) addresses LEVEL 1 at phase-level granularity. LEVEL 1 does
     not address individual proposals and does not protect against LEVEL 2.

     LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE
     Justifying a pre-decided change after a signal suggests it, without surfacing the
     cognitive pull that drove the proposal framing. This failure mode operates below
     phase granularity: it is present even in a run where LEVEL 1 was correctly blocked,
     because it occurs at the individual proposal row's decision point. The phase-level
     gate (LEVEL 1) does not evaluate individual proposals and cannot block this failure
     mode. The "Bias blocked by guard" column enforces LEVEL 2 by requiring each
     proposal row to name the specific cognitive bias the guard prevents at that row's
     decision surface. LEVEL 2 does not protect against LEVEL 1.

     BOTH LEVELS ARE REQUIRED. LEVEL 1 does not protect against LEVEL 2. LEVEL 2 does
     not protect against LEVEL 1. Neither substitutes for the other. These are distinct
     failure modes at distinct granularities. Presence of one without the other is a
     structural gap in bias coverage. Each proposal row MUST carry a "Bias blocked by
     guard" entry naming the cognitive bias the guard prevents at that row's specific
     decision point. <<]

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

## Scoring Predictions Under v15

| Var | C-31 | C-32 | C-33 | C-34 | C-35 | C-36 | Predicted score | Notes |
|-----|------|------|------|------|------|------|-----------------|-------|
| V-01 | 2 | 2 | 2 | **2** | 1 | 1 | 48/56 = 8.57 | Guard labels full; no auditor nav note; no self-ref CONTRACT |
| V-02 | 2 | 2 | 2 | 1 | **2** | 1 | 48/56 = 8.57 | Auditor nav note full; no guard labels; no self-ref CONTRACT |
| V-03 | 2 | 2 | 2 | 1 | 1 | **2** | 48/56 = 8.57 | CONTRACT self-ref + 4-site + violation-detection; no guard labels; no nav note |
| V-04 | 2 | 2 | 2 | **2** | **2** | 1 | 52/56 = 9.29 | Guard labels + auditor nav cross-reference; CONTRACT partial |
| V-05 | 2 | 2 | 2 | **2** | **2** | **2** | **56/56 = 10.00** | All three; closed reference triangle: CONTRACT B -> scope (3) -> guard LEVEL 2 |

**Key structural decision in V-05**: The closed reference triangle is the convergence mechanism. CONTRACT B names "Bias blocked by guard" with violation-detection. SECTION SCOPE item (3) names "ROW-LEVEL BIAS LABELING" with the auditor navigation note and cross-references "LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE." The PROPOSAL BIAS AUDIT guard defines "LEVEL 2" with a formal titled label. Each piece is independently locatable; together they provide full traceability without traversing any phase table.
