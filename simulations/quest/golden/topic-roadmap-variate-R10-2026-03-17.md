---
skill: quest-variate
skill_target: topic-roadmap
round: R10
date: 2026-03-17
rubric: topic-roadmap-rubric-v10-2026-03-17.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [spatial_separation_c24, phase5_antiduplicate_c25, c24_plus_c25_minimal]
  combined:
    V-04: c21 + c22 + c23 + c24 + c25 (full stack from R9 V-04 base)
    V-05: c21 + c22 + c23 + c24 + c25 (heading-level scope annotations)
rubric_anchor: >
  v10 adds C-24 (structural mechanism spatial separation -- Phase 1 / verdict block /
  INERTIA-GATE sites occupy non-overlapping sections; each verifiable in isolation
  without encountering the other mechanisms' text) and C-25 (Phase 5 verdict deferral
  with anti-duplication clause -- Phase 5 forward-references the standalone verdict
  vocabulary block and prohibits inline redefinition). Formula denominator changes to
  34 (17 aspirational x 2 max each).
round_targets: >
  C-24 full pass: Phase 1 section contains read-barrier and restart clause only
  (no verdict vocabulary, no INERTIA-GATE exclusion text); verdict vocabulary block
  contains only verdict definitions (no gate labels, no restart text); Phase 5
  INERTIA-GATE contains only gate-exclusion text (no verdict redefinitions, no restart
  language); sections do not reference each other's content inline.
  C-25 full pass: Phase 5 contains explicit forward-reference to the verdict vocabulary
  block ("Apply the Verdict Vocabulary defined above"); an anti-duplication clause is
  co-located in Phase 5 ("Do not redefine verdict semantics here" or equivalent);
  Phase 5 contains no inline DEFEATED/HOLDS semantic definitions.
  Key gap in R9 V-05: Phase 5 INERTIA-GATE block re-embeds verdict semantic
  descriptions ("HOLDS is the default verdict; DEFEATED requires specific named signal
  evidence") within the gate text -- violating spatial separation (C-24) even though
  the standalone verdict vocabulary block exists (C-23 passes) and Phase 5 has a
  forward-reference with anti-duplication (C-25 passes). C-24 requires the INERTIA-GATE
  sites to contain only gate-exclusion text, not verdict semantics.
orthogonality_notes: >
  C-24 fails / C-25 passes: Phase 5 has forward-reference + anti-duplication clause,
  but the Phase 5 INERTIA-GATE block still embeds inline verdict descriptions
  ("HOLDS = default; DEFEATED = requires evidence") alongside gate-exclusion text.
  Spatial purity violated even though single-source is enforced at the application site.
  C-25 fails / C-24 passes: All three mechanisms occupy spatially clean sections with
  SECTION SCOPE declarations; Phase 5 INERTIA-GATE contains only gate-exclusion text;
  but Phase 5 application block merely says "Apply the Verdict Vocabulary above" without
  the explicit anti-duplication clause ("Do not redefine here"). Forward-reference
  present but anti-duplication absent.
---

## V-01 -- Axis: Structural Mechanism Spatial Separation (C-24)

**Variation axis**: Each of the three structural mechanism sections acquires an explicit
SECTION SCOPE declaration. Phase 1 declares it contains read-barrier and restart clause
only -- no verdict vocabulary, no INERTIA-GATE exclusion text. The Verdict Vocabulary
block declares it contains verdict definitions only -- no gate labels, no restart text.
The Phase 5 INERTIA-GATE is stripped of inline verdict semantic descriptions; it
contains gate-exclusion text only. The Phase 6 INERTIA-GATE contains gate-exclusion
text only. A reviewer checking any one mechanism section does not encounter text
belonging to the other two.

**Hypothesis**: C-24 fails in R9 V-05 because the Phase 5 INERTIA-GATE block
re-embeds verdict semantics ("HOLDS is the default verdict; DEFEATED requires specific
named signal evidence") within the gate annotation. Removing those descriptions from
the gate block and adding explicit SECTION SCOPE declarations makes spatial
independence verifiable at each section boundary. C-25 is present (Phase 5 has
"Apply the Verdict Vocabulary above") but the anti-duplication clause ("Do not redefine
here") is absent in V-01 -- that is isolated to V-02. Base is R9 V-04 (C-21 + C-22)
plus the standalone verdict block added as C-23 prerequisite. C-25 is partial
(forward-reference present, anti-duplication absent).

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
| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if HOLDS |

Phase 6a -- Additions:
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because |

Phase 6b -- Removals and Reprioritizations:
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because |

---

## Phase 1 -- Pre-Signal Defense Register

[>> SECTION SCOPE: This section contains the Phase 1 read-barrier and restart
     isolation clause ONLY. It does not contain verdict vocabulary definitions.
     It does not contain INERTIA-GATE exclusion text. A reviewer auditing the
     read-barrier does not encounter content from the Verdict Vocabulary section
     or either INERTIA-GATE site. <<]

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
     It does not contain INERTIA-GATE exclusion text. A reviewer auditing verdict
     semantics does not encounter content from Phase 1 or either INERTIA-GATE site. <<]

[>> GUARD: VERDICT SEMANTICS BLOCK <<]
[>> Bias blocked: definitional ambiguity -- both verdict outcomes fully specified as
     standalone definitions, independently verifiable without reading Phase 5 <<]
[>> Mechanism: A scorer or auditor can confirm verdict semantics from this block alone.
     Distributing definitions across phase instructions requires reading all of Phase 5
     to reconstruct the semantics. This block makes them atomic and self-contained.
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

[>> SECTION SCOPE: This section contains gate-exclusion text ONLY. It does not
     redefine verdict semantics (those are defined in the Verdict Vocabulary block
     above). It does not contain restart isolation language. A reviewer auditing the
     Phase 5 gate does not encounter verdict redefinitions or restart clause text. <<]

[>> GUARD: INERTIA-GATE [Site 1 of 2 -- Phase 5 entry] <<]
[>> Bias blocked: action-default bias; status-quo neglect <<]
[>> Mechanism: Only DEFEATED dimensions advance to Phase 6. HOLDS dimensions have
     no path to Phase 6. This enforcement is at the Phase 5 entry site. A second
     independent enforcement exists at Phase 6 entry (Site 2 of 2). <<]

ENTRY CONDITION: Phase 4 EXIT CRITERION met (all four delta categories present).
Do NOT open Phase 5 until Phase 4 EXIT CRITERION is confirmed in output above.

Apply the Verdict Vocabulary defined above.

| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if HOLDS |

If all verdicts are HOLDS: emit "NULL_DELTA: INERTIA RETAINED ACROSS ALL DIMENSIONS."
Stop. Phase 6 does NOT open.

EXIT CRITERION: Verdict table complete; all dimensions adjudicated; NULL_DELTA emitted
if all HOLDS; at least one DEFEATED verdict present to proceed to Phase 6.

---

## Phase 6 -- Change Proposals (DEFEATED dimensions only)

[>> SECTION SCOPE: This section contains gate-exclusion text and proposal generation
     only. It does not redefine verdict semantics. A reviewer auditing the Phase 6
     gate does not encounter verdict redefinitions. <<]

[>> GUARD: INERTIA-GATE [Site 2 of 2 -- Phase 6 entry] <<]
[>> Bias blocked: action-default bias <<]
[>> Mechanism: HOLDS dimensions have no row and no path to this phase. This enforcement
     is independent of Site 1 at Phase 5. A model that bypasses Phase 5 and arrives
     directly at Phase 6 still encounters this gate. HOLDS exclusion is enforced here
     without relying on the Phase 5 site to carry the constraint. A reviewer can
     confirm HOLDS exclusion from this block alone, without reading Phase 5. <<]

ENTRY CONDITION: Phase 5 EXIT CRITERION met; at least one DEFEATED verdict present;
NULL_DELTA not emitted. Do NOT open Phase 6 if NULL_DELTA was emitted in Phase 5.

### 6a -- Additions
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because |
Null: "ADDITIONS: none -- INERTIA holds on all addition candidates."

### 6b -- Removals and Reprioritizations
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because |
Null-REMOVALS: "REMOVALS: none -- INERTIA holds."
Null-REPRIORITIZATIONS: "REPRIORITIZATIONS: none -- INERTIA holds."

All 9 namespaces must have a row. Silence is not a null declaration.

EXIT CRITERION: All three change-type tables present with labeled nulls; all 9
namespaces covered; each DEFEATED dimension from Phase 5 has a corresponding row.
Phase 7 may NOT open until this is met.

---

## Phase 7 -- Confirmation Gate

[>> GUARD: CONFIRMATION GATE <<]
[>> Bias blocked: recency bias; sunk-cost bias <<]
[>> Mechanism: The most-recently-read signals are disproportionately salient at this
     point. This gate requires explicit user confirmation before any write, ensuring
     the full proposal set is reviewed. The absence of NO is not implicit YES. <<]

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

## V-02 -- Axis: Phase 5 Verdict Deferral with Anti-Duplication Clause (C-25)

**Variation axis**: Phase 5 acquires an explicit anti-duplication clause co-located
with the forward-reference: "Apply the Verdict Vocabulary block defined above. Do not
redefine verdict semantics here. Any inline DEFEATED or HOLDS definition appearing in
this phase is a structural violation of single-source." The forward-reference names
the block by title ("Verdict Vocabulary") and the prohibition is categorical. The
Phase 5 INERTIA-GATE block, however, retains its inline verdict semantic descriptions
("HOLDS is the default verdict; DEFEATED requires specific named signal evidence") --
this deliberately creates the C-24 failure scenario to isolate C-25.

**Hypothesis**: C-25 requires not just a forward-reference but an explicit prohibition
on redefinition. R9 V-03 had "Do not redefine DEFEATED or HOLDS here" -- V-02 extends
this to a structural violation declaration: "Any inline DEFEATED/HOLDS definition in
this phase is a structural violation." The prohibition is categorical and unambiguous.
Meanwhile, C-24 intentionally fails: the Phase 5 INERTIA-GATE block embeds verdict
semantic descriptions alongside gate-exclusion text. This is the exact orthogonality
scenario from the rubric: C-24 fails (INERTIA-GATE contains verdict semantics), C-25
passes (Phase 5 application block has forward-reference + explicit anti-duplication).
Base is R9 V-04 (C-21 + C-22), plus standalone verdict block (C-23 prerequisite).
No SECTION SCOPE declarations -- C-24 explicitly absent.

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
| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if HOLDS |

Phase 6a -- Additions:
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because |

Phase 6b -- Removals and Reprioritizations:
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because |

---

## Phase 1 -- Pre-Signal Defense Register

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

[>> GUARD: INERTIA-GATE [Site 1 of 2 -- Phase 5 entry] <<]
[>> Bias blocked: action-default bias; status-quo neglect <<]
[>> Mechanism: HOLDS is the default verdict and requires no evidence; DEFEATED requires
     specific named signal evidence. Both verdicts are structurally equal outputs -- a
     dimension without an explicit verdict is a structural gap. Only DEFEATED dimensions
     advance to Phase 6. HOLDS dimensions have no path to Phase 6. This enforcement is
     at the Phase 5 entry site. A second independent enforcement exists at Phase 6
     entry (Site 2 of 2). <<]

ENTRY CONDITION: Phase 4 EXIT CRITERION met (all four delta categories present).
Do NOT open Phase 5 until Phase 4 EXIT CRITERION is confirmed in output above.

Apply the Verdict Vocabulary block defined above.
Do not redefine verdict semantics here.
Any inline DEFEATED or HOLDS definition appearing in this phase is a structural
violation of the single-source guarantee established by the Verdict Vocabulary block.

| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if HOLDS |

If all verdicts are HOLDS: emit "NULL_DELTA: INERTIA RETAINED ACROSS ALL DIMENSIONS."
Stop. Phase 6 does NOT open.

EXIT CRITERION: Verdict table complete; all dimensions adjudicated; NULL_DELTA emitted
if all HOLDS; at least one DEFEATED verdict present to proceed to Phase 6.

---

## Phase 6 -- Change Proposals (DEFEATED dimensions only)

[>> GUARD: INERTIA-GATE [Site 2 of 2 -- Phase 6 entry] <<]
[>> Bias blocked: action-default bias <<]
[>> Mechanism: HOLDS dimensions have no row and no path to this phase. This enforcement
     is independent of Site 1 at Phase 5. A model that bypasses Phase 5 and arrives
     directly at Phase 6 still encounters this gate. HOLDS exclusion is enforced here
     without relying on the Phase 5 site to carry the constraint. A reviewer can
     confirm HOLDS exclusion from this block alone, without reading Phase 5. <<]

ENTRY CONDITION: Phase 5 EXIT CRITERION met; at least one DEFEATED verdict present;
NULL_DELTA not emitted. Do NOT open Phase 6 if NULL_DELTA was emitted in Phase 5.

### 6a -- Additions
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because |
Null: "ADDITIONS: none -- INERTIA holds on all addition candidates."

### 6b -- Removals and Reprioritizations
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because |
Null-REMOVALS: "REMOVALS: none -- INERTIA holds."
Null-REPRIORITIZATIONS: "REPRIORITIZATIONS: none -- INERTIA holds."

All 9 namespaces must have a row. Silence is not a null declaration.

EXIT CRITERION: All three change-type tables present with labeled nulls; all 9
namespaces covered; each DEFEATED dimension from Phase 5 has a corresponding row.
Phase 7 may NOT open until this is met.

---

## Phase 7 -- Confirmation Gate

[>> GUARD: CONFIRMATION GATE <<]
[>> Bias blocked: recency bias; sunk-cost bias <<]
[>> Mechanism: The most-recently-read signals are disproportionately salient at this
     point. This gate requires explicit user confirmation before any write, ensuring
     the full proposal set is reviewed. The absence of NO is not implicit YES. <<]

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

## V-03 -- Combined: Spatial Separation + Phase 5 Anti-Duplication (C-24 + C-25, minimal)

**Variation axes**: V-01 (SECTION SCOPE declarations + clean Phase 5 INERTIA-GATE,
C-24) + V-02 (Phase 5 forward-reference + categorical anti-duplication clause, C-25).

**Hypothesis**: C-24 and C-25 are tested together on a minimal base (R9 V-03: C-23
only, no dual-site gate C-21, no restart clause C-22). This isolates the combined
effect of the two new criteria without the R9 features. The minimal base allows a
clean read: if this variation achieves C-24 + C-25, the pattern is confirmed as
independent of whether C-21/C-22 are present. Key structural choices: Phase 5
INERTIA-GATE contains only gate-exclusion text (no verdict descriptions); Verdict
Vocabulary block has SECTION SCOPE (no gate labels, no restart text); Phase 5
application block has forward-reference + categorical anti-duplication. C-21 is
absent (single-site INERTIA-GATE only). C-22 is absent (no restart clause). If
V-03 scores well on C-24 + C-25 but V-04 adds marginal value via C-21 + C-22, the
minimal combination is sufficient for production promotion of C-24 + C-25 alone.

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
| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if HOLDS |

Phase 6a -- Additions:
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because |

Phase 6b -- Removals and Reprioritizations:
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because |

---

## Phase 1 -- Pre-Signal Defense Register

[>> SECTION SCOPE: This section contains the Phase 1 read-barrier ONLY. It does not
     contain verdict vocabulary definitions. It does not contain INERTIA-GATE
     exclusion text. <<]

[>> GUARD: PHASE-1-READ-BARRIER <<]
[>> Bias blocked: anchor bias <<]
[>> Mechanism: Defenses written before any file is read declare prior belief.
     Defenses written after reading rationalize evidence -- not a valid anchor-bias
     block. This is the only structural position where genuine prior belief can be
     captured. <<]

ENTRY CONDITION: No files have been read yet.
DO NOT read strategy.md or any signal file before Phase 1 is complete.
If any file has been read, restart Phase 1 without it in context.

| Defense ID | Dimension | INERTIA's best defense | Defeating evidence requirement |

EXIT CRITERION: Defense register table present; each known dimension has a row;
no file has been read. Phase 2 may NOT open until this is met.

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
[>> Mechanism: Signal files are fixed as of this inventory. Re-reading after this
     point introduces post-hoc vocabulary alignment with the strategy frame.
     Signal files may NOT be re-read after this inventory is written. <<]

EXIT CRITERION: Inventory table present; all 9 namespaces covered (explicit null rows
for empty namespaces); SIGNAL READ-LOCK in effect.
Phase 3 may NOT open until this is met.

---

## Phase 3 -- Read Strategy
[Bias blocked: framing bias -- signals classified before strategy vocabulary opens]

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
[Bias blocked: confirmation bias -- four-category forcing function]

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
     A reviewer auditing verdict semantics does not encounter content from Phase 1 or
     either INERTIA-GATE site. <<]

[>> GUARD: VERDICT SEMANTICS BLOCK <<]
[>> Bias blocked: definitional ambiguity -- both verdict outcomes fully specified as
     standalone definitions, independently verifiable without reading Phase 5 <<]
[>> Mechanism: A scorer can confirm verdict semantics from this block alone. Phase 5
     applies these definitions; it does not redefine them. <<]

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

[>> SECTION SCOPE: This section contains gate-exclusion text and verdict application
     ONLY. It does not redefine verdict semantics (defined in the Verdict Vocabulary
     block above). It does not contain restart isolation language. <<]

[>> GUARD: INERTIA-GATE <<]
[>> Bias blocked: action-default bias; status-quo neglect <<]
[>> Mechanism: Only DEFEATED dimensions advance to Phase 6. HOLDS dimensions have
     no path to Phase 6. <<]

ENTRY CONDITION: Phase 4 EXIT CRITERION met (all four delta categories present).
Do NOT open Phase 5 until Phase 4 EXIT CRITERION is confirmed in output above.

Apply the Verdict Vocabulary defined above.
Do not redefine verdict semantics here.
Any inline DEFEATED or HOLDS definition in this phase is a structural violation.

| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if HOLDS |

If all verdicts are HOLDS: emit "NULL_DELTA: INERTIA RETAINED ACROSS ALL DIMENSIONS."
Stop. Phase 6 does NOT open.

EXIT CRITERION: Verdict table complete; all dimensions adjudicated; NULL_DELTA emitted
if all HOLDS; at least one DEFEATED verdict to proceed to Phase 6.

---

## Phase 6 -- Change Proposals (DEFEATED dimensions only)

[>> SECTION SCOPE: This section contains gate-exclusion text and proposal generation
     ONLY. It does not redefine verdict semantics. <<]

[>> GUARD: INERTIA-GATE (Phase 6 entry) <<]
[>> Bias blocked: action-default bias <<]
[>> Mechanism: Only DEFEATED dimensions from Phase 5 appear here. HOLDS dimensions
     have no row and no path to this phase. <<]

ENTRY CONDITION: Phase 5 EXIT CRITERION met; at least one DEFEATED verdict present;
NULL_DELTA not emitted. Do NOT open Phase 6 if NULL_DELTA was emitted in Phase 5.

### 6a -- Additions
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because |
Null: "ADDITIONS: none -- INERTIA holds on all addition candidates."

### 6b -- Removals and Reprioritizations
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because |
Null-REMOVALS: "REMOVALS: none -- INERTIA holds."
Null-REPRIORITIZATIONS: "REPRIORITIZATIONS: none -- INERTIA holds."

All 9 namespaces must have a row. Silence is not a null declaration.

EXIT CRITERION: All three change-type tables present with labeled nulls; all 9
namespaces covered; each DEFEATED dimension has a row. Phase 7 may NOT open until
this is met.

---

## Phase 7 -- Confirmation Gate

[>> GUARD: CONFIRMATION GATE <<]
[>> Bias blocked: recency bias; sunk-cost bias <<]
[>> Mechanism: Explicit user confirmation required before any write. Absence of NO
     is not implicit YES. <<]

[>> GUARD: WRITE GUARD <<]
[>> Bias blocked: premature closure bias <<]
[>> Mechanism: strategy.md is not modified until explicit YES or REVISED is received.
     strategy.md has NOT been modified at this point. <<]

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

## V-04 -- Combined: Full Stack on R9 V-04 Base (C-21 + C-22 + C-23 + C-24 + C-25)

**Variation axes**: R9 V-04 (C-21 + C-22) as base. Add standalone verdict block
(C-23). Add SECTION SCOPE declarations with MUST NOT CONTAIN prohibitions (C-24).
Add Phase 5 categorical anti-duplication clause (C-25). This is the five-criterion
integration built incrementally from the R9 V-04 foundation rather than from R9 V-05.

**Hypothesis**: R9 V-04 combined C-21 and C-22 and confirmed they coexist without
structural tension. V-04 R10 adds the three vocabulary/spatial criteria on top of that
proven base. The SECTION SCOPE declarations use an explicit MUST NOT CONTAIN
prohibition format (stronger than V-01's DOES NOT CONTAIN description). This
formulation makes violations structurally detectable: a scorer finding restart clause
text in the Verdict Vocabulary block can cite the MUST NOT CONTAIN prohibition
directly. Phase 5 anti-duplication uses the categorical "structural violation"
language from V-02. All five criteria should achieve full pass. The primary question
is whether the MUST NOT CONTAIN formulation is detectably stronger than V-01's
SECTION SCOPE description form.

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
| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if HOLDS |

Phase 6a -- Additions:
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because |

Phase 6b -- Removals and Reprioritizations:
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because |

---

## Phase 1 -- Pre-Signal Defense Register

[>> SECTION SCOPE <<]
[>> CONTAINS: read-barrier and restart isolation clause ONLY <<]
[>> MUST NOT CONTAIN: verdict vocabulary definitions; INERTIA-GATE exclusion text <<]
[>> A reviewer auditing the Phase 1 read-barrier does not encounter content from
     the Verdict Vocabulary section or either INERTIA-GATE site. <<]

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

[>> SECTION SCOPE <<]
[>> CONTAINS: verdict definitions ONLY <<]
[>> MUST NOT CONTAIN: Phase 1 read-barrier language; restart isolation clause text;
     INERTIA-GATE exclusion text from Phase 5 or Phase 6 <<]
[>> A reviewer auditing verdict semantics does not encounter content from Phase 1,
     Phase 5 gate, or Phase 6 gate. <<]

[>> GUARD: VERDICT SEMANTICS BLOCK <<]
[>> Bias blocked: definitional ambiguity -- both verdict outcomes fully specified as
     standalone definitions, independently verifiable without reading Phase 5 <<]
[>> Mechanism: A scorer or auditor can confirm verdict semantics from this block alone.
     Distributing definitions across phase instructions requires reading all of Phase 5
     to reconstruct the semantics. This block makes them atomic and self-contained.
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

[>> SECTION SCOPE <<]
[>> CONTAINS: gate-exclusion text and verdict application ONLY <<]
[>> MUST NOT CONTAIN: verdict semantic redefinitions; restart isolation language <<]
[>> Verdict semantics are defined in the Verdict Vocabulary block above.
     Re-embedding them here is a structural violation. <<]

[>> GUARD: INERTIA-GATE [Site 1 of 2 -- Phase 5 entry] <<]
[>> Bias blocked: action-default bias; status-quo neglect <<]
[>> Mechanism: Only DEFEATED dimensions advance to Phase 6. HOLDS dimensions have no
     path to Phase 6. This enforcement is at the Phase 5 entry site. A second
     independent enforcement exists at Phase 6 entry (Site 2 of 2). <<]

ENTRY CONDITION: Phase 4 EXIT CRITERION met (all four delta categories present).
Do NOT open Phase 5 until Phase 4 EXIT CRITERION is confirmed in output above.

Apply the Verdict Vocabulary block defined above.
Do not redefine verdict semantics here.
Any inline DEFEATED or HOLDS definition appearing in this phase is a structural
violation of the single-source guarantee established by the Verdict Vocabulary block.

| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if HOLDS |

If all verdicts are HOLDS: emit "NULL_DELTA: INERTIA RETAINED ACROSS ALL DIMENSIONS."
Stop. Phase 6 does NOT open.

EXIT CRITERION: Verdict table complete; all dimensions adjudicated; NULL_DELTA emitted
if all HOLDS; at least one DEFEATED verdict present to proceed to Phase 6.

---

## Phase 6 -- Change Proposals (DEFEATED dimensions only)

[>> SECTION SCOPE <<]
[>> CONTAINS: gate-exclusion text and proposal generation ONLY <<]
[>> MUST NOT CONTAIN: verdict semantic redefinitions <<]

[>> GUARD: INERTIA-GATE [Site 2 of 2 -- Phase 6 entry] <<]
[>> Bias blocked: action-default bias <<]
[>> Mechanism: HOLDS dimensions have no row and no path to this phase. This enforcement
     is independent of Site 1 at Phase 5. A model that bypasses Phase 5 and arrives
     directly at Phase 6 still encounters this gate. HOLDS exclusion is enforced here
     without relying on the Phase 5 site to carry the constraint. A reviewer can
     confirm HOLDS exclusion from this block alone, without reading Phase 5. <<]

ENTRY CONDITION: Phase 5 EXIT CRITERION met; at least one DEFEATED verdict present;
NULL_DELTA not emitted. Do NOT open Phase 6 if NULL_DELTA was emitted in Phase 5.

### 6a -- Additions
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because |
Null: "ADDITIONS: none -- INERTIA holds on all addition candidates."

### 6b -- Removals and Reprioritizations
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because |
Null-REMOVALS: "REMOVALS: none -- INERTIA holds."
Null-REPRIORITIZATIONS: "REPRIORITIZATIONS: none -- INERTIA holds."

All 9 namespaces must have a row. Silence is not a null declaration.

EXIT CRITERION: All three change-type tables present with labeled nulls; all 9
namespaces covered; each DEFEATED dimension from Phase 5 has a corresponding row.
Phase 7 may NOT open until this is met.

---

## Phase 7 -- Confirmation Gate

[>> GUARD: CONFIRMATION GATE <<]
[>> Bias blocked: recency bias; sunk-cost bias <<]
[>> Mechanism: The most-recently-read signals are disproportionately salient at this
     point. This gate requires explicit user confirmation before any write, ensuring
     the full proposal set is reviewed. The absence of NO is not implicit YES. <<]

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

## V-05 -- Full Integration: All Five Criteria with Heading-Level Scope Annotations (C-21 + C-22 + C-23 + C-24 + C-25)

**Variation axes**: R9 V-05 (C-21 + C-22 + C-23) as base. Add C-24 via heading-level
scope annotations embedded in section headings themselves -- each mechanism section
carries its scope constraint in the `##` heading line. Add C-25 with the categorical
anti-duplication formulation from V-02. The Phase 5 INERTIA-GATE block is stripped of
verdict semantic descriptions; it contains gate-exclusion text only.

**Hypothesis**: Heading-level scope annotation (e.g., "## Verdict Vocabulary
[SCOPE: verdict definitions only]") makes spatial separation verifiable from the
document outline alone -- a reviewer scanning headers can confirm each section's
declared scope without reading body text. This is a stronger C-24 signal than inline
SECTION SCOPE blocks (V-01/V-04): the constraint is visible at the heading level,
not buried in annotation text that must be read to discover it. If V-05 achieves
higher C-24 scoring than V-04, the heading-level form is the preferred pattern for
production. R9 V-05's Phase 5 already had "Apply the Verdict Vocabulary defined above.
Do not redefine DEFEATED or HOLDS here." -- V-05 R10 extends this to the categorical
"structural violation" formulation and removes verdict semantic descriptions from the
Phase 5 INERTIA-GATE annotation block.

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
| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if HOLDS |

Phase 6a -- Additions:
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because |

Phase 6b -- Removals and Reprioritizations:
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because |

---

## Phase 1 -- Pre-Signal Defense Register [SCOPE: read-barrier and restart clause only -- no verdict vocabulary, no INERTIA-GATE text]

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
     The reader unconsciously matches artifact language to strategy categories already
     read. This lock closes that path. Signal files may NOT be re-read after this
     inventory is written. All subsequent phases use the written inventory only. <<]

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

## Verdict Vocabulary [SCOPE: verdict definitions only -- no gate labels, no restart text, no phase instructions]

[>> GUARD: VERDICT SEMANTICS BLOCK <<]
[>> Bias blocked: definitional ambiguity -- both verdict outcomes fully specified as
     standalone definitions, independently verifiable without reading Phase 5 <<]
[>> Mechanism: A scorer or auditor can confirm verdict semantics from this block alone.
     Distributing definitions across phase instructions requires reading all of Phase 5
     to reconstruct the semantics. This block makes them atomic and self-contained.
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

## Phase 5 -- INERTIA DEFEAT ASSESSMENT [SCOPE: gate-exclusion and verdict application only -- no verdict redefinitions, no restart language]

[>> GUARD: INERTIA-GATE [Site 1 of 2 -- Phase 5 entry] <<]
[>> Bias blocked: action-default bias; status-quo neglect <<]
[>> Mechanism: Only DEFEATED dimensions advance to Phase 6. HOLDS dimensions have no
     path to Phase 6. This enforcement is at the Phase 5 entry site. A second
     independent enforcement exists at Phase 6 entry (Site 2 of 2). <<]

ENTRY CONDITION: Phase 4 EXIT CRITERION met (all four delta categories present).
Do NOT open Phase 5 until Phase 4 EXIT CRITERION is confirmed in output above.

Apply the Verdict Vocabulary block defined above.
Do not redefine verdict semantics here.
Any inline DEFEATED or HOLDS definition appearing in this phase is a structural
violation of the single-source guarantee established by the Verdict Vocabulary block.

| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if HOLDS |

If all verdicts are HOLDS: emit "NULL_DELTA: INERTIA RETAINED ACROSS ALL DIMENSIONS."
Stop. Phase 6 does NOT open.

EXIT CRITERION: Verdict table complete; all dimensions adjudicated; NULL_DELTA emitted
if all HOLDS; at least one DEFEATED verdict present to proceed to Phase 6.

---

## Phase 6 -- Change Proposals [SCOPE: proposal generation only -- DEFEATED dimensions; no verdict redefinitions]

[>> GUARD: INERTIA-GATE [Site 2 of 2 -- Phase 6 entry] <<]
[>> Bias blocked: action-default bias <<]
[>> Mechanism: HOLDS dimensions have no row and no path to this phase. This enforcement
     is independent of Site 1 at Phase 5. A model that bypasses Phase 5 and arrives
     directly at Phase 6 still encounters this gate. HOLDS exclusion is enforced here
     without relying on the Phase 5 site to carry the constraint. A reviewer can
     confirm HOLDS exclusion from this block alone, without reading Phase 5. <<]

ENTRY CONDITION: Phase 5 EXIT CRITERION met; at least one DEFEATED verdict present;
NULL_DELTA not emitted. Do NOT open Phase 6 if NULL_DELTA was emitted in Phase 5.

### 6a -- Additions
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because |
Null: "ADDITIONS: none -- INERTIA holds on all addition candidates."

### 6b -- Removals and Reprioritizations
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because |
Null-REMOVALS: "REMOVALS: none -- INERTIA holds."
Null-REPRIORITIZATIONS: "REPRIORITIZATIONS: none -- INERTIA holds."

All 9 namespaces must have a row. Silence is not a null declaration.

EXIT CRITERION: All three change-type tables present with labeled nulls; all 9
namespaces covered; each DEFEATED dimension from Phase 5 has a corresponding row.
Phase 7 may NOT open until this is met.

---

## Phase 7 -- Confirmation Gate

[>> GUARD: CONFIRMATION GATE <<]
[>> Bias blocked: recency bias; sunk-cost bias <<]
[>> Mechanism: The most-recently-read signals are disproportionately salient at this
     point. This gate requires explicit user confirmation before any write, ensuring
     the full proposal set is reviewed. The absence of NO is not implicit YES. <<]

[>> GUARD: WRITE GUARD <<]
[>> Bias blocked: premature closure bias <<]
[>> Mechanism: strategy.md is not modified until explicit YES or REVISED is received
     at this gate. The write step does not execute based on agent confidence in the
     proposals -- only on explicit user authorization. strategy.md has NOT been
     modified at this point. <<]

ENTRY CONDITION: Phase 6 EXIT CRITERION met.
Do NOT modify strategy.md before Phase 7 confirmation is received.

Present: Phase 4 delta findings (all four categories), Phase 6 proposals (all
three tables -- 6a and 6b).

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

## Criteria Coverage Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-21 Dual-site INERTIA-GATE | pass | pass | fail | pass | pass |
| C-22 Restart isolation clause | pass | pass | fail | pass | pass |
| C-23 Standalone verdict vocabulary block | pass | pass | pass | pass | pass |
| C-24 Structural mechanism spatial separation | pass | FAIL | pass | pass | pass |
| C-25 Phase 5 deferral + anti-duplication | partial | pass | pass | pass | pass |
| Primary axis tested | C-24 | C-25 | C-24+C-25 minimal | All 5 from V04 base | All 5 heading-scope |

**C-24 fail in V-02**: Phase 5 INERTIA-GATE block retains inline verdict semantic
descriptions ("HOLDS is the default verdict; DEFEATED requires specific named signal
evidence") -- gate-exclusion text and verdict semantics co-located, violating spatial
separation.

**C-25 partial in V-01**: Phase 5 has forward-reference ("Apply the Verdict Vocabulary
defined above") but no anti-duplication clause ("Do not redefine here"). A partial pass
per rubric: "Phase 5 forward-references the block but omits the anti-duplication
clause."

**Key differentiator V-04 vs V-05**: V-04 uses inline SECTION SCOPE annotation blocks
with MUST NOT CONTAIN prohibitions. V-05 uses heading-level `[SCOPE: ...]` annotations
embedded in `##` heading lines, making spatial separation verifiable from the document
outline without reading section body text.
