---
skill: quest-variate
skill_target: topic-plan
date: 2026-03-17
round: 16
rubric: topic-plan-rubric-v16-2026-03-17.md
new_criteria: [C-37, C-38, C-39]
prior_ceiling: R15-V-05 (62/62 under v16)
---

# topic-plan Skill Variations -- Round 16 (2026-03-17)

Rubric: v16 (C-37 directional protection gap assertion; C-38 SECTION SCOPE guard-label
cross-reference by complete title; C-39 CONTRACT B exact compliant column value string)

Three single-axis variations (V-01, V-02, V-03) then two combinations (V-04, V-05).

---

## Round 16 Design Notes

R15 V-05 is the ceiling that revealed C-37, C-38, and C-39. All three new criteria emerge
from contrasting V-05 against V-01/V-02/V-03/V-04 at the PROPOSAL BIAS AUDIT, SECTION SCOPE,
and CONTRACT B structural sites:

1. **C-37 from R15 V-01 gap** -- V-01 added the PROPOSAL BIAS AUDIT with LEVEL 1 and LEVEL 2
   labels (satisfying C-34) and the mutual necessity assertion ("both levels are required").
   V-05 alone extended the assertion to be directional: "LEVEL 1 does not protect against
   LEVEL 2." This converts co-requirement into a hierarchy explanation: a reader now knows
   WHY the levels are distinct, not just THAT they are both needed. V-01/V-02/V-03/V-04
   state co-requirement without the protection-gap direction.

2. **C-38 from R15 V-02 gap** -- V-02 included a SECTION SCOPE navigation note citing
   "item 2" by enumeration position (satisfying C-35). V-05 extended the note to cite
   "LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE" by its
   complete formal title, enabling auditor traversal from the scope declaration to the
   specific guard level using the label string alone, without reading the guard body.
   V-01/V-03/V-04 cite the level by enumeration position only.

3. **C-39 from R15 V-01/V-02/V-03/V-04 gap** -- All four non-ceiling variates included
   CONTRACT B column-presence enforcement (satisfying C-36: column absence is a violation).
   V-05 added the exact compliant column value string "Bias blocked by guard", enabling
   value-verification (not just presence-verification) from CONTRACT B alone. None of the
   other R15 variates named this exact string.

**R15 gap analysis for R16:**

| Gap | R15 variations missing | R16 axis |
|-----|------------------------|----------|
| G-01 | V-01/V-02/V-03/V-04 lack directional protection gap | V-01: Lifecycle emphasis -- directional assertion only (C-37 isolated) |
| G-02 | V-01/V-03/V-04 lack complete-title guard citation in SECTION SCOPE | V-02: Output format -- complete-title navigation note (C-38 isolated) |
| G-03 | V-01/V-02/V-03/V-04 lack exact compliant value in CONTRACT B | V-03: Phrasing register -- exact literal value string (C-39 isolated) |
| G-04 | G-01 + G-02 co-present; CONTRACT B presence-only | V-04: Combined lifecycle + output format (C-37 + C-38) |
| G-05 | All three criteria require simultaneous satisfaction | V-05: Full ceiling -- directional + title + exact value (C-37 + C-38 + C-39) |

**Round 16 variation map:**

| Variation | Axis | C-37 | C-38 | C-39 |
|-----------|------|------|------|------|
| V-01 | Lifecycle emphasis -- directional assertion | YES | NO | NO |
| V-02 | Output format -- complete-title citation | NO | YES | NO |
| V-03 | Phrasing register -- exact column value | NO | NO | YES |
| V-04 | Combined lifecycle + output format | YES | YES | NO |
| V-05 | Full ceiling (all three axes) | YES | YES | YES |

---

## V-01: Lifecycle Emphasis -- Directional Protection Gap Assertion (C-37)

**Variation axis**: Lifecycle emphasis -- single axis. The PROPOSAL BIAS AUDIT guard
introduces a directional protection gap assertion: "LEVEL 1 does not protect against
LEVEL 2." This extends the mutual necessity statement from co-requirement to hierarchy
explanation. The SECTION SCOPE navigation note cites the higher-order failure mode by
enumeration position only ("item 2"), not by complete formal title. CONTRACT B specifies
column-presence enforcement only, without naming the exact compliant value string.

**Hypothesis**: C-37 tests whether the mutual necessity assertion is *directional* -- naming
the specific protection gap, not merely asserting that both levels are needed. V-01 isolates
this by adding the directional formulation to a base that otherwise satisfies C-34 (labeled
levels) and C-36 (column-presence enforcement) but not C-38 (complete-title citation) or
C-39 (exact value string). A directional assertion enables downstream readers to understand
WHY the hierarchy exists: LEVEL 1 evidence-selection filtering passes through motivated
reasoning at the proposal surface untouched. C-38 and C-39 are deliberately absent to
confirm C-37 can be achieved and scored independently.

```
You are executing the topic-plan skill: revise the signal strategy as new information arrives.

The default outcome of this skill is NO CHANGE to strategy.md.
Every proposal carries the burden of proof against leaving the strategy unchanged.

==============================================================
SKILL EXECUTION CONTRACT
==============================================================

All output templates, constraint rules, phase authorization, and null obligations are
pre-declared below. Every phase executes against this contract and may audit against it.

§1  SCHEMA A TEMPLATE
    D-N | Dimension label | Current value
    Source: strategy.md (filled before any signal is examined).
    Null behavior: all strategy dimensions must appear; no row may be omitted.
    Phase authorization: Phase 1 only.

§2  VERBATIM BLOCK TEMPLATE
    ===VERBATIM BLOCK START===
    "[exact quoted sentence from strategy.md]"
    Source dimension: D-N -- [label matching a Schema A row]
    Enforcement note: A Source dimension field not matching a D-N label in Schema A
                      at seal time is a SEAL violation and fails this block.
    ===VERBATIM BLOCK END===
    Phase authorization: Phase 1 only.

§3  SEALED BLOCK TEMPLATE
    ===STRATEGY SEALED===
    Schema A: COMPLETE
    VERBATIM BLOCK: PRESENT -- D-N source, enforcement note labeled
    Temporal attestation: Commitment phase complete. No signal artifacts read yet.
    Re-read prohibition: strategy.md may not be re-opened until user applies changes. [R-1]
    SEAL violation: A Before value not in Schema A at seal time is a SEAL violation. [R-2]
    ===STRATEGY SEALED===
    Phase authorization: Phase 1 only.

§4  NAMESPACE INVENTORY TABLE TEMPLATE
    namespace | total artifacts | new (date > STRATEGY DATE)
    All 9 namespaces listed. Absent: 0 total | 0 new.
    missing row != absent namespace -- a missing row means the namespace was not checked.
    Phase authorization: Phase 2 only.

§5  PROPOSAL SCOPE BLOCK TEMPLATE
    HIGH-PRESSURE NAMESPACES: [namespaces with new > 0; "none" if list is empty]
    Evidence restriction: Only HIGH-PRESSURE namespace artifacts may support proposals.
    SCOPE violation: A proposal row citing an excluded namespace is a SCOPE violation.
    missing block != null -- a missing §5 block means the scope filter was not applied.
    Phase authorization: Phase 5 only.

§6  PROPOSALS TABLE TEMPLATE
    Action | Proposal | Before (from §1 Schema A) | After | Evidence artifact |
    Why this beats NO CHANGE [R-0] | Bias guard
    Action types: ADD / REMOVE / REPRIORITIZE.
    Null row: "[TYPE]: none -- inertia holds [R-0]."
    missing null row != no proposals -- a missing null row means the type was not evaluated.
    Bias guard column: mandatory in every row; column absence is a CONTRACT B violation.
    Phase authorization: Phase 5 only.

§7  GATE BLOCK TEMPLATE
    [PHASE N GATE: PASS/STOP -- condition: ...]
    Compound gates use [Na][Nb][Nc] labels on sub-conditions.
    Phase authorization: any gate phase.

§8  CONFLICT AUDIT BLOCK TEMPLATE
    Conflict audit: [typed null "no cross-artifact contradictions found"
                     or contradiction table: Artifact A | Artifact B | Dimension | Contradiction]
    missing block != null -- a missing §8 block means the audit was not run.
    Phase authorization: Phase 4 only.

§9  PROPOSAL BIAS AUDIT TEMPLATE
    Two failure modes enumerated as formal labeled levels:

    LEVEL 1: CONFIRMATION ANCHORING AT THE EVIDENCE SCAN SURFACE
    The model reads artifacts through the lens of what it expects to find,
    preferentially noting observations that confirm or oppose the strategy in
    a predetermined direction, rather than reading each artifact without
    regard to desired outcome.

    LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE
    At the moment of individual proposal construction, the model has implicitly
    decided the proposal direction before evaluating evidence, and constructs
    post-hoc justification to fill the Before/After/Evidence/Why columns.

    Mutual necessity: LEVEL 1 and LEVEL 2 guards are both required.
    LEVEL 1 does not protect against LEVEL 2. A balanced evidence scan
    (LEVEL 1 satisfied) does not prevent motivated reasoning at the proposal
    decision surface (LEVEL 2). The protection hierarchy is not transitive;
    both guards must be applied independently.

    Compliance: every §6 proposal row must carry a non-null Bias guard value.
    Phase authorization: declared pre-execution; audit applies during Phase 5.

PHASE AUTHORIZATION INDEX:
  Phase 1 -- §1 §2 §3 §7
  Phase 2 -- §4 §7
  Phase 3 -- §7 only
  Phase 4 -- §8 §7
  Phase 5 -- §5 §6 §7 (§9 audit active)
  Phase 6 -- §7 (confirmation variant) only
  Phase 7 -- write to strategy.md (post-confirmation only)

CONSTRAINT RULES:
  R-0: Default outcome is NO CHANGE. Every proposal must prove that leaving the strategy
       unchanged produces a worse outcome than the proposed change.
  R-1: strategy.md sealed after §3. May not be re-read before user confirmation.
  R-2: Before values in §6 must trace to §1 Schema A rows at seal time.
  R-3: Evidence restricted to artifacts dated after STRATEGY DATE.
  R-4: Enforcement reproductions cite both contract name and §ID (double-anchored attribution).

CONSTRAINT SCOPE INDEX:
  R-0: Phases 5-6
  R-1: Phases 1-6
  R-2: Phase 5 only
  R-3: Phases 4-5
  R-4: Phase 5 only

PHASE SEQUENCE:
  Phase 1 (Commitment) -> Phase 2 (Inventory) -> Phase 3 (Gate) ->
  Phase 4 (Reading + Conflict Audit) -> Phase 5 (Proposals) ->
  Phase 6 (Confirmation -- halt) -> Phase 7 (Apply -- only after YES or REVISED)

==============================================================
SECTION SCOPE DECLARATION
==============================================================

This skill operates on HIGH-PRESSURE namespaces only (those with new artifacts since
STRATEGY DATE). Proposals citing non-HIGH-PRESSURE namespaces are SCOPE violations.

Bias guard navigation (auditor): the PROPOSAL BIAS AUDIT guard is enumerated in §9 above.
The higher-order failure mode -- motivated reasoning at the proposal decision surface --
is item 2 in the guard. A proposal row with a non-null Bias guard value has passed both
guard levels. A null or absent value signals the guard was not applied.

==============================================================
CONTRACT B -- BIAS GUARD COMPLIANCE CONTRACT
==============================================================

Column "Bias guard" is mandatory in every §6 PROPOSALS TABLE row.
Structural compliance: column must be present in every row (including typed-null rows).
A missing column in any row is a CONTRACT B structural violation.

Compliant state: column present with a value indicating both guard levels were applied.
A row with a null or blank Bias guard value is a CONTRACT B value violation even if the
column header is present.

==============================================================
Gate-0 -- CONTRACT COMPLETENESS GATE
==============================================================

Before Phase 1 begins, verify the SKILL EXECUTION CONTRACT above is complete.

  Arithmetic decomposition: 9 declared schemas + 3 structural checks = 12 items.
  Gate-0 passes when all 12 items confirmed; one STOP result halts Phase 1.

  Schema checks:
  Check [A1]: §1 SCHEMA A present with D-N column, null behavior, phase auth Phase 1?
  Check [A2]: §2 VERBATIM BLOCK present with delimiters, Source dimension field,
              Enforcement note, phase auth Phase 1?
  Check [A3]: §3 SEALED BLOCK present with all 5 fields including R-1 and R-2, phase auth Phase 1?
  Check [A4]: §4 NAMESPACE INVENTORY TABLE present with 3 columns, missing-row annotation,
              phase auth Phase 2?
  Check [A5]: §5 PROPOSAL SCOPE BLOCK present with HIGH-PRESSURE field, violation line,
              missing-block annotation, phase auth Phase 5?
  Check [A6]: §6 PROPOSALS TABLE present with all 7 columns including Bias guard, null row
              format, missing-null annotation, CONTRACT B reference, phase auth Phase 5?
  Check [A7]: §7 GATE BLOCK present with PASS/STOP format, compound labeling, phase auth any?
  Check [A8]: §8 CONFLICT AUDIT BLOCK present with typed-null or table format, missing-block
              annotation, phase auth Phase 4?
  Check [A9]: §9 PROPOSAL BIAS AUDIT present with LEVEL 1 and LEVEL 2 formal titled labels,
              mutual necessity assertion including directional gap statement (LEVEL 1 does not
              protect against LEVEL 2), compliance note, phase auth declaration?

  Structural checks:
  Check [B]: PHASE AUTHORIZATION INDEX -- all 7 phases listed with authorized §IDs?
  Check [C]: CONSTRAINT SCOPE INDEX -- all R-N rules listed with active phase ranges?
  Check [D]: Null annotations present on all typed-null-capable sections?
    §4 "missing row != absent namespace"
    §5 "missing block != null"
    §6 "missing null row != no proposals"
    §8 "missing block != null"

  Item count: 12 items ([A1][A2][A3][A4][A5][A6][A7][A8][A9][B][C][D]).
  A missing §ID produces a detectable missing check item.

  [GATE-0: PASS/STOP -- condition: schemas [A1][A2][A3][A4][A5][A6][A7][A8][A9] all present +
  phase index [B] complete + constraint index [C] complete + null annotations [D] all present;
  reading this condition line enumerates all 12 items required; no item may be inferred by range]

Phase 1 does not begin until Gate-0 passes.

==============================================================
PHASE 1 -- Commitment  [per Skill Execution Contract]
==============================================================

Authorization check: Authorized §IDs for Phase 1: §1 §2 §3 §7.

Open strategy.md. Extract STRATEGY DATE. Fill §1 SCHEMA A.

  | D-N | Dimension label | Current value |

Write §2 VERBATIM BLOCK:
  ===VERBATIM BLOCK START===
  "[exact quoted sentence]"
  Source dimension: D-N -- [matching Schema A row]
  Enforcement note: A Source dimension field not matching a D-N label in Schema A
                    at seal time is a SEAL violation and fails this block.
  ===VERBATIM BLOCK END===

Write §3 SEALED BLOCK:
  ===STRATEGY SEALED===
  Schema A: COMPLETE
  VERBATIM BLOCK: PRESENT -- D-N source, enforcement note labeled
  Temporal attestation: Commitment phase complete. No signal artifacts read yet.
  Re-read prohibition: strategy.md may not be re-opened until user applies changes. [R-1]
  SEAL violation: A Before value not in Schema A at seal time is a SEAL violation. [R-2]
  ===STRATEGY SEALED===

Gate 1: [PHASE 1 GATE: PASS/STOP -- condition: §1 complete [1] + §2 [2a][2b][2c] + §3 [3]]

==============================================================
PHASE 2 -- Signal Inventory  [per Skill Execution Contract]
==============================================================

Authorization check: Authorized §IDs for Phase 2: §4 §7.

Locate all signal artifact files for the topic in simulations/.

Fill §4 NAMESPACE INVENTORY TABLE:
  | namespace | total artifacts | new (date > STRATEGY DATE) |
  [all 9 rows -- scout / draft / review / flow / trace / prove / listen / program / topic]
  [a missing row != 0|0; every namespace must appear]

Gate 2: [PHASE 2 GATE: PASS/STOP -- condition: namespace [2a] + total-artifacts [2b] +
new [2c] all non-null across all 9 rows]

==============================================================
PHASE 3 -- Inventory Completeness Gate  [per Skill Execution Contract]
==============================================================

Authorization check: Authorized §IDs for Phase 3: §7 only.

  Check [3a]: all 9 namespaces present exactly once?
  Check [3b]: total-artifacts non-null for all 9 rows?
  Check [3c]: new non-null for all 9 rows?
  Check [3d]: HIGH-PRESSURE namespaces identified?

  [PHASE 3 GATE: PASS/STOP -- condition: [3a][3b][3c][3d] all satisfied]

==============================================================
PHASE 4 -- Artifact Reading + Conflict Audit  [per Skill Execution Contract]
==============================================================

Authorization check: Authorized §IDs for Phase 4: §8 §7. Active rules: R-1, R-3.

Read every artifact with new > 0 (date > STRATEGY DATE). [R-3 active]

§8 CONFLICT AUDIT BLOCK:
  Conflict audit: [typed null "no cross-artifact contradictions found" or contradiction table]
  [missing block != null -- declare the null if no contradictions found]

Dimension Coverage Map:
  | Schema A D-N | Dimension | Signal coverage | Status |

Gate 4: [PHASE 4 GATE: PASS/STOP -- condition: §8 declared + coverage map present]

==============================================================
PHASE 5 -- Proposals  [per Skill Execution Contract]
==============================================================

Authorization check: Authorized §IDs for Phase 5: §5 §6 §7. §9 audit active.
Active rules: R-0 R-1 R-2 R-3 R-4.

Reproduce §5 PROPOSAL SCOPE BLOCK (per R-4, citing Skill Execution Contract §5):
  HIGH-PRESSURE NAMESPACES: [list or "none"]
  Evidence restriction: Only HIGH-PRESSURE namespace artifacts may support proposals.
  SCOPE violation: A proposal row citing an excluded namespace is a SCOPE violation.
  [missing block != null]

Scope Gate: [SCOPE GATE: PASS/STOP -- condition: §5 present; violation condition stated]

PROPOSAL BIAS AUDIT -- apply §9 guard before constructing any proposal row:
  Check LEVEL 1: Evidence selection was artifact-driven, not expectation-anchored?
  Check LEVEL 2: Each proposal direction emerged from evidence, not from a predetermined
                 conclusion? (LEVEL 1 passing does not certify LEVEL 2 -- check independently.)
  Compliance result for each row: Bias guard = [compliance statement] if both levels pass,
  or identify which level failed and drop the proposal.

Produce §6 PROPOSALS TABLE:
  Before values from §1 Schema A [R-2]. Evidence dated after STRATEGY DATE [R-3].
  Every proposal must name a concrete consequence of NOT changing [R-0].

  | Action | Proposal | Before (§1 [R-2]) | After | Evidence [R-3] |
    Why this beats NO CHANGE [R-0] | Bias guard |

  [missing null row != no proposals for that type]
  ADD: none -- inertia holds [R-0].
  REMOVE: none -- inertia holds [R-0].
  REPRIORITIZE: none -- inertia holds [R-0].

Gate 5: [PHASE 5 GATE: PASS/STOP -- condition: Action [5a] + Proposal [5b] +
Before [5c] + After [5d] + Evidence [5e] + Why [5f] + Bias guard [5g] all non-null
across all non-null action rows]

==============================================================
PHASE 6 -- Confirmation Gate  [per Skill Execution Contract]
==============================================================

Authorization check: §7 only.

Present the proposals table. Write:
"Proposed changes to strategy.md above. The default is NO CHANGE [R-0]. Apply?
Reply YES to proceed, NO to cancel, or REVISED with modifications."

Stop. Do not write to strategy.md. Halt here and wait for user reply.

==============================================================
PHASE 7 -- Apply  (after YES or REVISED only)
==============================================================

Apply confirmed proposals to strategy.md. Write only what was confirmed.
No unrequested additions.
```

---

## V-02: Output Format -- Complete-Title Guard-Label Cross-Reference (C-38)

**Variation axis**: Output format -- single axis. The SECTION SCOPE navigation note
cross-references the higher-order failure mode by its complete formal title:
"LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE". An auditor
reading the SECTION SCOPE can traverse directly to the specific guard level by label,
without reading the §9 guard body. The PROPOSAL BIAS AUDIT retains the non-directional
mutual necessity assertion ("both levels are required") without the explicit LEVEL 1 →
LEVEL 2 protection gap direction (C-37 absent). CONTRACT B specifies column-presence
enforcement only, without naming the exact compliant value string (C-39 absent).

**Hypothesis**: C-38 tests whether the SECTION SCOPE navigation note names the formal
guard label by its complete title, creating bidirectional navigation between the scope
declaration and the specific guard level. V-02 isolates this by extending only the
navigation note from enumeration-position citation ("item 2") to complete-title citation
("LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE"), while
preserving the non-directional mutual necessity assertion and the presence-only CONTRACT B.
The complete title string allows a scope-to-guard traversal path that is anchored to a
named artifact, not just a positional index. An auditor who knows the label but not the
enumeration position can still traverse to the correct guard level.

```
You are executing the topic-plan skill: revise the signal strategy as new information arrives.

The default outcome of this skill is NO CHANGE to strategy.md.
Every proposal carries the burden of proof against leaving the strategy unchanged.

==============================================================
SKILL EXECUTION CONTRACT
==============================================================

All output templates, constraint rules, phase authorization, and null obligations are
pre-declared below. Every phase executes against this contract and may audit against it.

§1  SCHEMA A TEMPLATE
    D-N | Dimension label | Current value
    Source: strategy.md (filled before any signal is examined).
    Null behavior: all strategy dimensions must appear; no row may be omitted.
    Phase authorization: Phase 1 only.

§2  VERBATIM BLOCK TEMPLATE
    ===VERBATIM BLOCK START===
    "[exact quoted sentence from strategy.md]"
    Source dimension: D-N -- [label matching a Schema A row]
    Enforcement note: A Source dimension field not matching a D-N label in Schema A
                      at seal time is a SEAL violation and fails this block.
    ===VERBATIM BLOCK END===
    Phase authorization: Phase 1 only.

§3  SEALED BLOCK TEMPLATE
    ===STRATEGY SEALED===
    Schema A: COMPLETE
    VERBATIM BLOCK: PRESENT -- D-N source, enforcement note labeled
    Temporal attestation: Commitment phase complete. No signal artifacts read yet.
    Re-read prohibition: strategy.md may not be re-opened until user applies changes. [R-1]
    SEAL violation: A Before value not in Schema A at seal time is a SEAL violation. [R-2]
    ===STRATEGY SEALED===
    Phase authorization: Phase 1 only.

§4  NAMESPACE INVENTORY TABLE TEMPLATE
    namespace | total artifacts | new (date > STRATEGY DATE)
    All 9 namespaces listed. Absent: 0 total | 0 new.
    missing row != absent namespace -- a missing row means the namespace was not checked.
    Phase authorization: Phase 2 only.

§5  PROPOSAL SCOPE BLOCK TEMPLATE
    HIGH-PRESSURE NAMESPACES: [namespaces with new > 0; "none" if list is empty]
    Evidence restriction: Only HIGH-PRESSURE namespace artifacts may support proposals.
    SCOPE violation: A proposal row citing an excluded namespace is a SCOPE violation.
    missing block != null -- a missing §5 block means the scope filter was not applied.
    Phase authorization: Phase 5 only.

§6  PROPOSALS TABLE TEMPLATE
    Action | Proposal | Before (from §1 Schema A) | After | Evidence artifact |
    Why this beats NO CHANGE [R-0] | Bias guard
    Action types: ADD / REMOVE / REPRIORITIZE.
    Null row: "[TYPE]: none -- inertia holds [R-0]."
    missing null row != no proposals -- a missing null row means the type was not evaluated.
    Bias guard column: mandatory in every row; column absence is a CONTRACT B violation.
    Phase authorization: Phase 5 only.

§7  GATE BLOCK TEMPLATE
    [PHASE N GATE: PASS/STOP -- condition: ...]
    Compound gates use [Na][Nb][Nc] labels on sub-conditions.
    Phase authorization: any gate phase.

§8  CONFLICT AUDIT BLOCK TEMPLATE
    Conflict audit: [typed null "no cross-artifact contradictions found"
                     or contradiction table: Artifact A | Artifact B | Dimension | Contradiction]
    missing block != null -- a missing §8 block means the audit was not run.
    Phase authorization: Phase 4 only.

§9  PROPOSAL BIAS AUDIT TEMPLATE
    Two failure modes enumerated as formal labeled levels:

    LEVEL 1: CONFIRMATION ANCHORING AT THE EVIDENCE SCAN SURFACE
    The model reads artifacts through the lens of what it expects to find,
    preferentially noting observations that confirm or oppose the strategy in
    a predetermined direction, rather than reading each artifact without
    regard to desired outcome.

    LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE
    At the moment of individual proposal construction, the model has implicitly
    decided the proposal direction before evaluating evidence, and constructs
    post-hoc justification to fill the Before/After/Evidence/Why columns.

    Mutual necessity: Both LEVEL 1 and LEVEL 2 guards are required for complete
    bias protection. A proposal table that passed LEVEL 1 screening is not
    automatically protected against LEVEL 2 failure.

    Compliance: every §6 proposal row must carry a non-null Bias guard value.
    Phase authorization: declared pre-execution; audit applies during Phase 5.

PHASE AUTHORIZATION INDEX:
  Phase 1 -- §1 §2 §3 §7
  Phase 2 -- §4 §7
  Phase 3 -- §7 only
  Phase 4 -- §8 §7
  Phase 5 -- §5 §6 §7 (§9 audit active)
  Phase 6 -- §7 (confirmation variant) only
  Phase 7 -- write to strategy.md (post-confirmation only)

CONSTRAINT RULES:
  R-0: Default outcome is NO CHANGE. Every proposal must prove that leaving the strategy
       unchanged produces a worse outcome than the proposed change.
  R-1: strategy.md sealed after §3. May not be re-read before user confirmation.
  R-2: Before values in §6 must trace to §1 Schema A rows at seal time.
  R-3: Evidence restricted to artifacts dated after STRATEGY DATE.
  R-4: Enforcement reproductions cite both contract name and §ID (double-anchored attribution).

CONSTRAINT SCOPE INDEX:
  R-0: Phases 5-6
  R-1: Phases 1-6
  R-2: Phase 5 only
  R-3: Phases 4-5
  R-4: Phase 5 only

PHASE SEQUENCE:
  Phase 1 (Commitment) -> Phase 2 (Inventory) -> Phase 3 (Gate) ->
  Phase 4 (Reading + Conflict Audit) -> Phase 5 (Proposals) ->
  Phase 6 (Confirmation -- halt) -> Phase 7 (Apply -- only after YES or REVISED)

==============================================================
SECTION SCOPE DECLARATION
==============================================================

This skill operates on HIGH-PRESSURE namespaces only (those with new artifacts since
STRATEGY DATE). Proposals citing non-HIGH-PRESSURE namespaces are SCOPE violations.

Bias guard navigation (auditor): the PROPOSAL BIAS AUDIT guard is in §9 above.
The more sophisticated failure mode addressed by this guard is
LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE.
A proposal row carrying a non-null Bias guard value has passed both guard levels,
including LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE.

==============================================================
CONTRACT B -- BIAS GUARD COMPLIANCE CONTRACT
==============================================================

Column "Bias guard" is mandatory in every §6 PROPOSALS TABLE row.
Structural compliance: column must be present in every row (including typed-null rows).
A missing column in any row is a CONTRACT B structural violation.

Compliant state: column present with a value indicating both guard levels were applied.
A row with a null or blank Bias guard value is a CONTRACT B value violation even if the
column header is present.

==============================================================
Gate-0 -- CONTRACT COMPLETENESS GATE
==============================================================

Before Phase 1 begins, verify the SKILL EXECUTION CONTRACT above is complete.

  Arithmetic decomposition: 9 declared schemas + 3 structural checks = 12 items.
  Gate-0 passes when all 12 items confirmed; one STOP result halts Phase 1.

  Schema checks:
  Check [A1]: §1 SCHEMA A present with D-N column, null behavior, phase auth Phase 1?
  Check [A2]: §2 VERBATIM BLOCK present with delimiters, Source dimension, Enforcement note,
              phase auth Phase 1?
  Check [A3]: §3 SEALED BLOCK present with all 5 fields including R-1 and R-2, phase auth Phase 1?
  Check [A4]: §4 NAMESPACE INVENTORY TABLE present with 3 columns, missing-row annotation,
              phase auth Phase 2?
  Check [A5]: §5 PROPOSAL SCOPE BLOCK present with HIGH-PRESSURE field, violation line,
              missing-block annotation, phase auth Phase 5?
  Check [A6]: §6 PROPOSALS TABLE present with all 7 columns including Bias guard, null row
              format, missing-null annotation, CONTRACT B reference, phase auth Phase 5?
  Check [A7]: §7 GATE BLOCK present with PASS/STOP format, compound labeling, phase auth any?
  Check [A8]: §8 CONFLICT AUDIT BLOCK present with typed-null or table format, missing-block
              annotation, phase auth Phase 4?
  Check [A9]: §9 PROPOSAL BIAS AUDIT present with LEVEL 1 and LEVEL 2 formal titled labels,
              mutual necessity assertion, compliance note, phase auth declaration?

  Structural checks:
  Check [B]: PHASE AUTHORIZATION INDEX -- all 7 phases listed with authorized §IDs?
  Check [C]: CONSTRAINT SCOPE INDEX -- all R-N rules listed with active phase ranges?
  Check [D]: Null annotations present on all typed-null-capable sections?
    §4 "missing row != absent namespace"
    §5 "missing block != null"
    §6 "missing null row != no proposals"
    §8 "missing block != null"

  Item count: 12 items ([A1][A2][A3][A4][A5][A6][A7][A8][A9][B][C][D]).

  [GATE-0: PASS/STOP -- condition: schemas [A1][A2][A3][A4][A5][A6][A7][A8][A9] all present +
  phase index [B] complete + constraint index [C] complete + null annotations [D] all present;
  reading this condition line enumerates all 12 items required; no item may be inferred by range]

Phase 1 does not begin until Gate-0 passes.

==============================================================
PHASE 1 -- Commitment  [per Skill Execution Contract]
==============================================================

Authorization check: Authorized §IDs for Phase 1: §1 §2 §3 §7.

Open strategy.md. Extract STRATEGY DATE. Fill §1 SCHEMA A.

  | D-N | Dimension label | Current value |

Write §2 VERBATIM BLOCK:
  ===VERBATIM BLOCK START===
  "[exact quoted sentence]"
  Source dimension: D-N -- [matching Schema A row]
  Enforcement note: A Source dimension field not matching a D-N label in Schema A
                    at seal time is a SEAL violation and fails this block.
  ===VERBATIM BLOCK END===

Write §3 SEALED BLOCK:
  ===STRATEGY SEALED===
  Schema A: COMPLETE
  VERBATIM BLOCK: PRESENT -- D-N source, enforcement note labeled
  Temporal attestation: Commitment phase complete. No signal artifacts read yet.
  Re-read prohibition: strategy.md may not be re-opened until user applies changes. [R-1]
  SEAL violation: A Before value not in Schema A at seal time is a SEAL violation. [R-2]
  ===STRATEGY SEALED===

Gate 1: [PHASE 1 GATE: PASS/STOP -- condition: §1 complete [1] + §2 [2a][2b][2c] + §3 [3]]

==============================================================
PHASE 2 -- Signal Inventory  [per Skill Execution Contract]
==============================================================

Authorization check: Authorized §IDs for Phase 2: §4 §7.

Locate all signal artifact files for the topic in simulations/.

Fill §4 NAMESPACE INVENTORY TABLE:
  | namespace | total artifacts | new (date > STRATEGY DATE) |
  [all 9 rows -- scout / draft / review / flow / trace / prove / listen / program / topic]
  [a missing row != 0|0; every namespace must appear]

Gate 2: [PHASE 2 GATE: PASS/STOP -- condition: namespace [2a] + total-artifacts [2b] +
new [2c] all non-null across all 9 rows]

==============================================================
PHASE 3 -- Inventory Completeness Gate  [per Skill Execution Contract]
==============================================================

Authorization check: Authorized §IDs for Phase 3: §7 only.

  Check [3a]: all 9 namespaces present exactly once?
  Check [3b]: total-artifacts non-null for all 9 rows?
  Check [3c]: new non-null for all 9 rows?
  Check [3d]: HIGH-PRESSURE namespaces identified?

  [PHASE 3 GATE: PASS/STOP -- condition: [3a][3b][3c][3d] all satisfied]

==============================================================
PHASE 4 -- Artifact Reading + Conflict Audit  [per Skill Execution Contract]
==============================================================

Authorization check: Authorized §IDs for Phase 4: §8 §7. Active rules: R-1, R-3.

Read every artifact classified new (date > STRATEGY DATE). [R-3 active]

§8 CONFLICT AUDIT BLOCK:
  Conflict audit: [typed null or contradiction table]
  [missing block != null]

Dimension Coverage Map:
  | Schema A D-N | Dimension | Signal coverage | Status |

Gate 4: [PHASE 4 GATE: PASS/STOP -- condition: §8 declared + coverage map present]

==============================================================
PHASE 5 -- Proposals  [per Skill Execution Contract]
==============================================================

Authorization check: Authorized §IDs for Phase 5: §5 §6 §7. §9 audit active.
Active rules: R-0 R-1 R-2 R-3 R-4.

Reproduce §5 PROPOSAL SCOPE BLOCK (per R-4, citing Skill Execution Contract §5):
  HIGH-PRESSURE NAMESPACES: [list or "none"]
  Evidence restriction: Only HIGH-PRESSURE namespace artifacts may support proposals.
  SCOPE violation: A proposal row citing an excluded namespace is a SCOPE violation.
  [missing block != null]

Scope Gate: [SCOPE GATE: PASS/STOP -- condition: §5 present; violation condition stated]

PROPOSAL BIAS AUDIT -- apply §9 guard before constructing any proposal row:
  Check LEVEL 1: Evidence selection was artifact-driven, not expectation-anchored?
  Check LEVEL 2: Each proposal direction emerged from evidence? (check independently of LEVEL 1)
  Note: LEVEL 2 is MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE.
  Compliance result for each row: Bias guard = [compliance statement] if both levels pass.

Produce §6 PROPOSALS TABLE:
  Before values from §1 Schema A [R-2]. Evidence dated after STRATEGY DATE [R-3].

  | Action | Proposal | Before (§1 [R-2]) | After | Evidence [R-3] |
    Why this beats NO CHANGE [R-0] | Bias guard |

  ADD: none -- inertia holds [R-0].
  REMOVE: none -- inertia holds [R-0].
  REPRIORITIZE: none -- inertia holds [R-0].

Gate 5: [PHASE 5 GATE: PASS/STOP -- condition: Action [5a] + Proposal [5b] +
Before [5c] + After [5d] + Evidence [5e] + Why [5f] + Bias guard [5g] all non-null
across all non-null action rows]

==============================================================
PHASE 6 -- Confirmation Gate  [per Skill Execution Contract]
==============================================================

Authorization check: §7 only.

Present the proposals table. Write:
"Proposed changes to strategy.md above. The default is NO CHANGE [R-0]. Apply?
Reply YES to proceed, NO to cancel, or REVISED with modifications."

Stop. Do not write to strategy.md. Halt here and wait for user reply.

==============================================================
PHASE 7 -- Apply  (after YES or REVISED only)
==============================================================

Apply confirmed proposals to strategy.md. Write only what was confirmed.
No unrequested additions.
```

---

## V-03: Phrasing Register -- Exact Compliant Column Value String (C-39)

**Variation axis**: Phrasing register -- single axis. CONTRACT B names the exact literal
string that constitutes the compliant Bias guard column value: "Bias blocked by guard".
This enables value-verification (not just presence-verification) from CONTRACT B alone.
The PROPOSAL BIAS AUDIT retains the non-directional mutual necessity assertion (C-37
absent). The SECTION SCOPE navigation note cites the higher-order failure mode by
enumeration position only -- "item 2 in the §9 guard" (C-38 absent, no complete title).

**Hypothesis**: C-39 tests whether CONTRACT B specifies the exact literal compliant value
string, enabling a scorer to verify not only that the column exists but that it carries
the correct value. V-03 isolates this by adding "Bias blocked by guard" as the named
compliant state to a CONTRACT B that otherwise performs only structural (presence) checking.
The phrasing register variation is the quoting style: the string is delimited in single
quotes to make approximate matches distinguishable from exact matches. C-37 and C-38 are
deliberately absent to confirm C-39 can be scored independently.

```
You are executing the topic-plan skill: revise the signal strategy as new information arrives.

The default outcome of this skill is NO CHANGE to strategy.md.
Every proposal carries the burden of proof against leaving the strategy unchanged.

==============================================================
SKILL EXECUTION CONTRACT
==============================================================

All output templates, constraint rules, phase authorization, and null obligations are
pre-declared below. Every phase executes against this contract and may audit against it.

§1  SCHEMA A TEMPLATE
    D-N | Dimension label | Current value
    Source: strategy.md (filled before any signal is examined).
    Null behavior: all strategy dimensions must appear; no row may be omitted.
    Phase authorization: Phase 1 only.

§2  VERBATIM BLOCK TEMPLATE
    ===VERBATIM BLOCK START===
    "[exact quoted sentence from strategy.md]"
    Source dimension: D-N -- [label matching a Schema A row]
    Enforcement note: A Source dimension field not matching a D-N label in Schema A
                      at seal time is a SEAL violation and fails this block.
    ===VERBATIM BLOCK END===
    Phase authorization: Phase 1 only.

§3  SEALED BLOCK TEMPLATE
    ===STRATEGY SEALED===
    Schema A: COMPLETE
    VERBATIM BLOCK: PRESENT -- D-N source, enforcement note labeled
    Temporal attestation: Commitment phase complete. No signal artifacts read yet.
    Re-read prohibition: strategy.md may not be re-opened until user applies changes. [R-1]
    SEAL violation: A Before value not in Schema A at seal time is a SEAL violation. [R-2]
    ===STRATEGY SEALED===
    Phase authorization: Phase 1 only.

§4  NAMESPACE INVENTORY TABLE TEMPLATE
    namespace | total artifacts | new (date > STRATEGY DATE)
    All 9 namespaces listed. Absent: 0 total | 0 new.
    missing row != absent namespace -- a missing row means the namespace was not checked.
    Phase authorization: Phase 2 only.

§5  PROPOSAL SCOPE BLOCK TEMPLATE
    HIGH-PRESSURE NAMESPACES: [namespaces with new > 0; "none" if list is empty]
    Evidence restriction: Only HIGH-PRESSURE namespace artifacts may support proposals.
    SCOPE violation: A proposal row citing an excluded namespace is a SCOPE violation.
    missing block != null -- a missing §5 block means the scope filter was not applied.
    Phase authorization: Phase 5 only.

§6  PROPOSALS TABLE TEMPLATE
    Action | Proposal | Before (from §1 Schema A) | After | Evidence artifact |
    Why this beats NO CHANGE [R-0] | Bias guard
    Action types: ADD / REMOVE / REPRIORITIZE.
    Null row: "[TYPE]: none -- inertia holds [R-0]."
    missing null row != no proposals -- a missing null row means the type was not evaluated.
    Bias guard column: mandatory in every row; column absence is a CONTRACT B violation.
    Compliant value: 'Bias blocked by guard' (exact literal -- see CONTRACT B).
    Phase authorization: Phase 5 only.

§7  GATE BLOCK TEMPLATE
    [PHASE N GATE: PASS/STOP -- condition: ...]
    Compound gates use [Na][Nb][Nc] labels on sub-conditions.
    Phase authorization: any gate phase.

§8  CONFLICT AUDIT BLOCK TEMPLATE
    Conflict audit: [typed null "no cross-artifact contradictions found"
                     or contradiction table: Artifact A | Artifact B | Dimension | Contradiction]
    missing block != null -- a missing §8 block means the audit was not run.
    Phase authorization: Phase 4 only.

§9  PROPOSAL BIAS AUDIT TEMPLATE
    Two failure modes enumerated as formal labeled levels:

    LEVEL 1: CONFIRMATION ANCHORING AT THE EVIDENCE SCAN SURFACE
    The model reads artifacts through the lens of what it expects to find,
    preferentially noting observations that confirm or oppose the strategy in
    a predetermined direction, rather than reading each artifact without
    regard to desired outcome.

    LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE
    At the moment of individual proposal construction, the model has implicitly
    decided the proposal direction before evaluating evidence, and constructs
    post-hoc justification to fill the Before/After/Evidence/Why columns.

    Mutual necessity: Both LEVEL 1 and LEVEL 2 guards are required for complete
    bias protection. A proposal table that passed LEVEL 1 screening is not
    automatically protected against LEVEL 2 failure.

    Compliance: every §6 proposal row must carry a non-null Bias guard value.
    Compliant value: 'Bias blocked by guard' (see CONTRACT B for exact specification).
    Phase authorization: declared pre-execution; audit applies during Phase 5.

PHASE AUTHORIZATION INDEX:
  Phase 1 -- §1 §2 §3 §7
  Phase 2 -- §4 §7
  Phase 3 -- §7 only
  Phase 4 -- §8 §7
  Phase 5 -- §5 §6 §7 (§9 audit active)
  Phase 6 -- §7 (confirmation variant) only
  Phase 7 -- write to strategy.md (post-confirmation only)

CONSTRAINT RULES:
  R-0: Default outcome is NO CHANGE. Every proposal must prove that leaving the strategy
       unchanged produces a worse outcome than the proposed change.
  R-1: strategy.md sealed after §3. May not be re-read before user confirmation.
  R-2: Before values in §6 must trace to §1 Schema A rows at seal time.
  R-3: Evidence restricted to artifacts dated after STRATEGY DATE.
  R-4: Enforcement reproductions cite both contract name and §ID (double-anchored attribution).

CONSTRAINT SCOPE INDEX:
  R-0: Phases 5-6
  R-1: Phases 1-6
  R-2: Phase 5 only
  R-3: Phases 4-5
  R-4: Phase 5 only

PHASE SEQUENCE:
  Phase 1 (Commitment) -> Phase 2 (Inventory) -> Phase 3 (Gate) ->
  Phase 4 (Reading + Conflict Audit) -> Phase 5 (Proposals) ->
  Phase 6 (Confirmation -- halt) -> Phase 7 (Apply -- only after YES or REVISED)

==============================================================
SECTION SCOPE DECLARATION
==============================================================

This skill operates on HIGH-PRESSURE namespaces only (those with new artifacts since
STRATEGY DATE). Proposals citing non-HIGH-PRESSURE namespaces are SCOPE violations.

Bias guard navigation (auditor): the PROPOSAL BIAS AUDIT guard is in §9 above.
The higher-order failure mode is item 2 in the §9 guard. A proposal row carrying
'Bias blocked by guard' in the Bias guard column has passed both guard levels.

==============================================================
CONTRACT B -- BIAS GUARD COMPLIANCE CONTRACT
==============================================================

Column "Bias guard" is mandatory in every §6 PROPOSALS TABLE row.

Structural compliance: column must be present in every row (including typed-null rows).
A missing column in any row is a CONTRACT B structural violation.

Value compliance: the compliant column value is exactly 'Bias blocked by guard'.
A column that is present but does not contain this exact literal string is a CONTRACT B
value violation. Approximate variants ('bias blocked', 'guard applied', 'both levels passed')
are not compliant; only the exact string 'Bias blocked by guard' satisfies value compliance.

Violation detection from this contract alone:
  STRUCTURAL: Bias guard column absent from any row -> CONTRACT B structural violation.
  VALUE: Bias guard column present but value != 'Bias blocked by guard' -> CONTRACT B value violation.

==============================================================
Gate-0 -- CONTRACT COMPLETENESS GATE
==============================================================

Before Phase 1 begins, verify the SKILL EXECUTION CONTRACT above is complete.

  Arithmetic decomposition: 9 declared schemas + 3 structural checks = 12 items.
  Gate-0 passes when all 12 items confirmed; one STOP result halts Phase 1.

  Schema checks:
  Check [A1]: §1 SCHEMA A present with D-N column, null behavior, phase auth Phase 1?
  Check [A2]: §2 VERBATIM BLOCK present with delimiters, Source dimension, Enforcement note,
              phase auth Phase 1?
  Check [A3]: §3 SEALED BLOCK present with all 5 fields including R-1 and R-2, phase auth Phase 1?
  Check [A4]: §4 NAMESPACE INVENTORY TABLE present with 3 columns, missing-row annotation,
              phase auth Phase 2?
  Check [A5]: §5 PROPOSAL SCOPE BLOCK present with HIGH-PRESSURE field, violation line,
              missing-block annotation, phase auth Phase 5?
  Check [A6]: §6 PROPOSALS TABLE present with all 7 columns including Bias guard and exact
              value reference, null row format, missing-null annotation, phase auth Phase 5?
  Check [A7]: §7 GATE BLOCK present with PASS/STOP format, compound labeling, phase auth any?
  Check [A8]: §8 CONFLICT AUDIT BLOCK present with typed-null or table format, missing-block
              annotation, phase auth Phase 4?
  Check [A9]: §9 PROPOSAL BIAS AUDIT present with LEVEL 1 and LEVEL 2 formal titled labels,
              mutual necessity assertion, exact compliant value reference, phase auth declaration?

  Structural checks:
  Check [B]: PHASE AUTHORIZATION INDEX -- all 7 phases listed with authorized §IDs?
  Check [C]: CONSTRAINT SCOPE INDEX -- all R-N rules listed with active phase ranges?
  Check [D]: Null annotations present on all typed-null-capable sections?
    §4 "missing row != absent namespace"
    §5 "missing block != null"
    §6 "missing null row != no proposals"
    §8 "missing block != null"

  Item count: 12 items ([A1][A2][A3][A4][A5][A6][A7][A8][A9][B][C][D]).

  [GATE-0: PASS/STOP -- condition: schemas [A1][A2][A3][A4][A5][A6][A7][A8][A9] all present +
  phase index [B] complete + constraint index [C] complete + null annotations [D] all present;
  reading this condition line enumerates all 12 items required; no item may be inferred by range]

Phase 1 does not begin until Gate-0 passes.

==============================================================
PHASE 1 -- Commitment  [per Skill Execution Contract]
==============================================================

Authorization check: Authorized §IDs for Phase 1: §1 §2 §3 §7.

Open strategy.md. Extract STRATEGY DATE. Fill §1 SCHEMA A.

  | D-N | Dimension label | Current value |

Write §2 VERBATIM BLOCK:
  ===VERBATIM BLOCK START===
  "[exact quoted sentence]"
  Source dimension: D-N -- [matching Schema A row]
  Enforcement note: A Source dimension field not matching a D-N label in Schema A
                    at seal time is a SEAL violation and fails this block.
  ===VERBATIM BLOCK END===

Write §3 SEALED BLOCK:
  ===STRATEGY SEALED===
  Schema A: COMPLETE
  VERBATIM BLOCK: PRESENT -- D-N source, enforcement note labeled
  Temporal attestation: Commitment phase complete. No signal artifacts read yet.
  Re-read prohibition: strategy.md may not be re-opened until user applies changes. [R-1]
  SEAL violation: A Before value not in Schema A at seal time is a SEAL violation. [R-2]
  ===STRATEGY SEALED===

Gate 1: [PHASE 1 GATE: PASS/STOP -- condition: §1 complete [1] + §2 [2a][2b][2c] + §3 [3]]

==============================================================
PHASE 2 -- Signal Inventory  [per Skill Execution Contract]
==============================================================

Authorization check: Authorized §IDs for Phase 2: §4 §7.

Locate all signal artifact files for the topic in simulations/.

Fill §4 NAMESPACE INVENTORY TABLE:
  | namespace | total artifacts | new (date > STRATEGY DATE) |
  [all 9 rows -- scout / draft / review / flow / trace / prove / listen / program / topic]
  [a missing row != 0|0; every namespace must appear]

Gate 2: [PHASE 2 GATE: PASS/STOP -- condition: namespace [2a] + total-artifacts [2b] +
new [2c] all non-null across all 9 rows]

==============================================================
PHASE 3 -- Inventory Completeness Gate  [per Skill Execution Contract]
==============================================================

Authorization check: Authorized §IDs for Phase 3: §7 only.

  Check [3a]: all 9 namespaces present exactly once?
  Check [3b]: total-artifacts non-null for all 9 rows?
  Check [3c]: new non-null for all 9 rows?
  Check [3d]: HIGH-PRESSURE namespaces identified?

  [PHASE 3 GATE: PASS/STOP -- condition: [3a][3b][3c][3d] all satisfied]

==============================================================
PHASE 4 -- Artifact Reading + Conflict Audit  [per Skill Execution Contract]
==============================================================

Authorization check: Authorized §IDs for Phase 4: §8 §7. Active rules: R-1, R-3.

Read every artifact classified new (date > STRATEGY DATE). [R-3 active]

§8 CONFLICT AUDIT BLOCK:
  Conflict audit: [typed null or contradiction table]
  [missing block != null]

Dimension Coverage Map:
  | Schema A D-N | Dimension | Signal coverage | Status |

Gate 4: [PHASE 4 GATE: PASS/STOP -- condition: §8 declared + coverage map present]

==============================================================
PHASE 5 -- Proposals  [per Skill Execution Contract]
==============================================================

Authorization check: Authorized §IDs for Phase 5: §5 §6 §7. §9 audit active.
Active rules: R-0 R-1 R-2 R-3 R-4.

Reproduce §5 PROPOSAL SCOPE BLOCK (per R-4, citing Skill Execution Contract §5):
  HIGH-PRESSURE NAMESPACES: [list or "none"]
  Evidence restriction: Only HIGH-PRESSURE namespace artifacts may support proposals.
  SCOPE violation: A proposal row citing an excluded namespace is a SCOPE violation.
  [missing block != null]

Scope Gate: [SCOPE GATE: PASS/STOP -- condition: §5 present; violation condition stated]

PROPOSAL BIAS AUDIT -- apply §9 guard before constructing any proposal row:
  Check LEVEL 1: Evidence selection artifact-driven, not expectation-anchored?
  Check LEVEL 2: Proposal direction emerged from evidence independently? (§9, item 2)
  Compliance for each row: Bias guard = 'Bias blocked by guard' if both levels pass
  (CONTRACT B exact value requirement -- any other string is a value violation).

Produce §6 PROPOSALS TABLE:
  Before values from §1 Schema A [R-2]. Evidence dated after STRATEGY DATE [R-3].

  | Action | Proposal | Before (§1 [R-2]) | After | Evidence [R-3] |
    Why this beats NO CHANGE [R-0] | Bias guard |

  ADD: none -- inertia holds [R-0].
  REMOVE: none -- inertia holds [R-0].
  REPRIORITIZE: none -- inertia holds [R-0].

Gate 5: [PHASE 5 GATE: PASS/STOP -- condition: Action [5a] + Proposal [5b] +
Before [5c] + After [5d] + Evidence [5e] + Why [5f] + Bias guard [5g] all non-null
across all non-null action rows; Bias guard value = 'Bias blocked by guard' [CONTRACT B]]

==============================================================
PHASE 6 -- Confirmation Gate  [per Skill Execution Contract]
==============================================================

Authorization check: §7 only.

Present the proposals table. Write:
"Proposed changes to strategy.md above. The default is NO CHANGE [R-0]. Apply?
Reply YES to proceed, NO to cancel, or REVISED with modifications."

Stop. Do not write to strategy.md. Halt here and wait for user reply.

==============================================================
PHASE 7 -- Apply  (after YES or REVISED only)
==============================================================

Apply confirmed proposals to strategy.md. Write only what was confirmed.
No unrequested additions.
```

---

## V-04: Combined Lifecycle + Output Format -- Directional Assertion + Complete-Title Citation (C-37 + C-38)

**Variation axis**: Combined lifecycle emphasis (C-37) and output format (C-38). The PROPOSAL
BIAS AUDIT guard includes the directional protection gap assertion "LEVEL 1 does not protect
against LEVEL 2." The SECTION SCOPE navigation note cites "LEVEL 2: MOTIVATED REASONING AT
THE INDIVIDUAL PROPOSAL DECISION SURFACE" by its complete formal title. CONTRACT B specifies
column-presence enforcement only, without naming the exact compliant value string (C-39 absent).

**Hypothesis**: V-04 tests whether C-37 and C-38 can be satisfied simultaneously on a single
base while C-39 remains absent. The directional assertion and the complete-title citation are
structurally independent: one lives in the §9 PROPOSAL BIAS AUDIT guard body, the other in
the SECTION SCOPE navigation note. Their co-presence requires only that both sites carry the
appropriate extensions -- neither change affects the other. The expected result is C-37=FULL,
C-38=FULL, C-39=FAIL (CONTRACT B states presence-only compliance). This serves as the
penultimate rung before the full-ceiling V-05 and verifies that C-39 is the only remaining
gap at this combination point.

```
You are executing the topic-plan skill: revise the signal strategy as new information arrives.

The default outcome of this skill is NO CHANGE to strategy.md.
Every proposal carries the burden of proof against leaving the strategy unchanged.

==============================================================
SKILL EXECUTION CONTRACT
==============================================================

All output templates, constraint rules, phase authorization, and null obligations are
pre-declared below. Every phase executes against this contract and may audit against it.

§1  SCHEMA A TEMPLATE
    D-N | Dimension label | Current value
    Source: strategy.md (filled before any signal is examined).
    Null behavior: all strategy dimensions must appear; no row may be omitted.
    Phase authorization: Phase 1 only.

§2  VERBATIM BLOCK TEMPLATE
    ===VERBATIM BLOCK START===
    "[exact quoted sentence from strategy.md]"
    Source dimension: D-N -- [label matching a Schema A row]
    Enforcement note: A Source dimension field not matching a D-N label in Schema A
                      at seal time is a SEAL violation and fails this block.
    ===VERBATIM BLOCK END===
    Phase authorization: Phase 1 only.

§3  SEALED BLOCK TEMPLATE
    ===STRATEGY SEALED===
    Schema A: COMPLETE
    VERBATIM BLOCK: PRESENT -- D-N source, enforcement note labeled
    Temporal attestation: Commitment phase complete. No signal artifacts read yet.
    Re-read prohibition: strategy.md may not be re-opened until user applies changes. [R-1]
    SEAL violation: A Before value not in Schema A at seal time is a SEAL violation. [R-2]
    ===STRATEGY SEALED===
    Phase authorization: Phase 1 only.

§4  NAMESPACE INVENTORY TABLE TEMPLATE
    namespace | total artifacts | new (date > STRATEGY DATE)
    All 9 namespaces listed. Absent: 0 total | 0 new.
    missing row != absent namespace -- a missing row means the namespace was not checked.
    Phase authorization: Phase 2 only.

§5  PROPOSAL SCOPE BLOCK TEMPLATE
    HIGH-PRESSURE NAMESPACES: [namespaces with new > 0; "none" if list is empty]
    Evidence restriction: Only HIGH-PRESSURE namespace artifacts may support proposals.
    SCOPE violation: A proposal row citing an excluded namespace is a SCOPE violation.
    missing block != null -- a missing §5 block means the scope filter was not applied.
    Phase authorization: Phase 5 only.

§6  PROPOSALS TABLE TEMPLATE
    Action | Proposal | Before (from §1 Schema A) | After | Evidence artifact |
    Why this beats NO CHANGE [R-0] | Bias guard
    Action types: ADD / REMOVE / REPRIORITIZE.
    Null row: "[TYPE]: none -- inertia holds [R-0]."
    missing null row != no proposals -- a missing null row means the type was not evaluated.
    Bias guard column: mandatory in every row; column absence is a CONTRACT B violation.
    Phase authorization: Phase 5 only.

§7  GATE BLOCK TEMPLATE
    [PHASE N GATE: PASS/STOP -- condition: ...]
    Compound gates use [Na][Nb][Nc] labels on sub-conditions.
    Phase authorization: any gate phase.

§8  CONFLICT AUDIT BLOCK TEMPLATE
    Conflict audit: [typed null "no cross-artifact contradictions found"
                     or contradiction table: Artifact A | Artifact B | Dimension | Contradiction]
    missing block != null -- a missing §8 block means the audit was not run.
    Phase authorization: Phase 4 only.

§9  PROPOSAL BIAS AUDIT TEMPLATE
    Two failure modes enumerated as formal labeled levels:

    LEVEL 1: CONFIRMATION ANCHORING AT THE EVIDENCE SCAN SURFACE
    The model reads artifacts through the lens of what it expects to find,
    preferentially noting observations that confirm or oppose the strategy in
    a predetermined direction, rather than reading each artifact without
    regard to desired outcome.

    LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE
    At the moment of individual proposal construction, the model has implicitly
    decided the proposal direction before evaluating evidence, and constructs
    post-hoc justification to fill the Before/After/Evidence/Why columns.

    Mutual necessity: LEVEL 1 and LEVEL 2 guards are both required.
    LEVEL 1 does not protect against LEVEL 2. A balanced evidence scan (LEVEL 1
    satisfied) does not prevent motivated reasoning at the proposal decision surface
    (LEVEL 2). The protection hierarchy is not transitive; both guards must be applied
    independently. Passing LEVEL 1 confers no LEVEL 2 protection.

    Compliance: every §6 proposal row must carry a non-null Bias guard value.
    Phase authorization: declared pre-execution; audit applies during Phase 5.

PHASE AUTHORIZATION INDEX:
  Phase 1 -- §1 §2 §3 §7
  Phase 2 -- §4 §7
  Phase 3 -- §7 only
  Phase 4 -- §8 §7
  Phase 5 -- §5 §6 §7 (§9 audit active)
  Phase 6 -- §7 (confirmation variant) only
  Phase 7 -- write to strategy.md (post-confirmation only)

CONSTRAINT RULES:
  R-0: Default outcome is NO CHANGE. Every proposal must prove that leaving the strategy
       unchanged produces a worse outcome than the proposed change.
  R-1: strategy.md sealed after §3. May not be re-read before user confirmation.
  R-2: Before values in §6 must trace to §1 Schema A rows at seal time.
  R-3: Evidence restricted to artifacts dated after STRATEGY DATE.
  R-4: Enforcement reproductions cite both contract name and §ID (double-anchored attribution).

CONSTRAINT SCOPE INDEX:
  R-0: Phases 5-6
  R-1: Phases 1-6
  R-2: Phase 5 only
  R-3: Phases 4-5
  R-4: Phase 5 only

PHASE SEQUENCE:
  Phase 1 (Commitment) -> Phase 2 (Inventory) -> Phase 3 (Gate) ->
  Phase 4 (Reading + Conflict Audit) -> Phase 5 (Proposals) ->
  Phase 6 (Confirmation -- halt) -> Phase 7 (Apply -- only after YES or REVISED)

==============================================================
SECTION SCOPE DECLARATION
==============================================================

This skill operates on HIGH-PRESSURE namespaces only (those with new artifacts since
STRATEGY DATE). Proposals citing non-HIGH-PRESSURE namespaces are SCOPE violations.

Bias guard navigation (auditor): the PROPOSAL BIAS AUDIT guard is in §9 above.
The more sophisticated failure mode protected against in Phase 5 is
LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE.
Note that LEVEL 1: CONFIRMATION ANCHORING AT THE EVIDENCE SCAN SURFACE does not
protect against LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE;
both levels must be checked independently per §9. A proposal row with a non-null Bias
guard value confirms that LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL
DECISION SURFACE was explicitly checked and cleared before the row was written.

==============================================================
CONTRACT B -- BIAS GUARD COMPLIANCE CONTRACT
==============================================================

Column "Bias guard" is mandatory in every §6 PROPOSALS TABLE row.
Structural compliance: column must be present in every row (including typed-null rows).
A missing column in any row is a CONTRACT B structural violation.

Compliant state: column present with a value indicating both guard levels were applied.
A row with a null or blank Bias guard value is a CONTRACT B value violation even if the
column header is present.

==============================================================
Gate-0 -- CONTRACT COMPLETENESS GATE
==============================================================

Before Phase 1 begins, verify the SKILL EXECUTION CONTRACT above is complete.

  Arithmetic decomposition: 9 declared schemas + 3 structural checks = 12 items.
  Gate-0 passes when all 12 items confirmed; one STOP result halts Phase 1.

  Schema checks:
  Check [A1]: §1 SCHEMA A present with D-N column, null behavior, phase auth Phase 1?
  Check [A2]: §2 VERBATIM BLOCK present with delimiters, Source dimension, Enforcement note,
              phase auth Phase 1?
  Check [A3]: §3 SEALED BLOCK present with all 5 fields including R-1 and R-2, phase auth Phase 1?
  Check [A4]: §4 NAMESPACE INVENTORY TABLE present with 3 columns, missing-row annotation,
              phase auth Phase 2?
  Check [A5]: §5 PROPOSAL SCOPE BLOCK present with HIGH-PRESSURE field, violation line,
              missing-block annotation, phase auth Phase 5?
  Check [A6]: §6 PROPOSALS TABLE present with all 7 columns including Bias guard, null row
              format, missing-null annotation, CONTRACT B reference, phase auth Phase 5?
  Check [A7]: §7 GATE BLOCK present with PASS/STOP format, compound labeling, phase auth any?
  Check [A8]: §8 CONFLICT AUDIT BLOCK present with typed-null or table format, missing-block
              annotation, phase auth Phase 4?
  Check [A9]: §9 PROPOSAL BIAS AUDIT present with LEVEL 1 and LEVEL 2 formal titled labels,
              directional mutual necessity assertion (LEVEL 1 does not protect against LEVEL 2),
              compliance note, phase auth declaration?

  Structural checks:
  Check [B]: PHASE AUTHORIZATION INDEX -- all 7 phases listed with authorized §IDs?
  Check [C]: CONSTRAINT SCOPE INDEX -- all R-N rules listed with active phase ranges?
  Check [D]: Null annotations present on all typed-null-capable sections?
    §4 "missing row != absent namespace"
    §5 "missing block != null"
    §6 "missing null row != no proposals"
    §8 "missing block != null"

  Item count: 12 items ([A1][A2][A3][A4][A5][A6][A7][A8][A9][B][C][D]).

  [GATE-0: PASS/STOP -- condition: schemas [A1][A2][A3][A4][A5][A6][A7][A8][A9] all present +
  phase index [B] complete + constraint index [C] complete + null annotations [D] all present;
  reading this condition line enumerates all 12 items required; no item may be inferred by range]

Phase 1 does not begin until Gate-0 passes.

==============================================================
PHASE 1 -- Commitment  [per Skill Execution Contract]
==============================================================

Authorization check: Authorized §IDs for Phase 1: §1 §2 §3 §7.

Open strategy.md. Extract STRATEGY DATE. Fill §1 SCHEMA A.

  | D-N | Dimension label | Current value |

Write §2 VERBATIM BLOCK:
  ===VERBATIM BLOCK START===
  "[exact quoted sentence]"
  Source dimension: D-N -- [matching Schema A row]
  Enforcement note: A Source dimension field not matching a D-N label in Schema A
                    at seal time is a SEAL violation and fails this block.
  ===VERBATIM BLOCK END===

Write §3 SEALED BLOCK:
  ===STRATEGY SEALED===
  Schema A: COMPLETE
  VERBATIM BLOCK: PRESENT -- D-N source, enforcement note labeled
  Temporal attestation: Commitment phase complete. No signal artifacts read yet.
  Re-read prohibition: strategy.md may not be re-opened until user applies changes. [R-1]
  SEAL violation: A Before value not in Schema A at seal time is a SEAL violation. [R-2]
  ===STRATEGY SEALED===

Gate 1: [PHASE 1 GATE: PASS/STOP -- condition: §1 complete [1] + §2 [2a][2b][2c] + §3 [3]]

==============================================================
PHASE 2 -- Signal Inventory  [per Skill Execution Contract]
==============================================================

Authorization check: Authorized §IDs for Phase 2: §4 §7.

Locate all signal artifact files for the topic in simulations/.

Fill §4 NAMESPACE INVENTORY TABLE:
  | namespace | total artifacts | new (date > STRATEGY DATE) |
  [all 9 rows -- scout / draft / review / flow / trace / prove / listen / program / topic]
  [a missing row != 0|0; every namespace must appear]

Gate 2: [PHASE 2 GATE: PASS/STOP -- condition: namespace [2a] + total-artifacts [2b] +
new [2c] all non-null across all 9 rows]

==============================================================
PHASE 3 -- Inventory Completeness Gate  [per Skill Execution Contract]
==============================================================

Authorization check: Authorized §IDs for Phase 3: §7 only.

  Check [3a]: all 9 namespaces present exactly once?
  Check [3b]: total-artifacts non-null for all 9 rows?
  Check [3c]: new non-null for all 9 rows?
  Check [3d]: HIGH-PRESSURE namespaces identified?

  [PHASE 3 GATE: PASS/STOP -- condition: [3a][3b][3c][3d] all satisfied]

==============================================================
PHASE 4 -- Artifact Reading + Conflict Audit  [per Skill Execution Contract]
==============================================================

Authorization check: Authorized §IDs for Phase 4: §8 §7. Active rules: R-1, R-3.

Read every artifact classified new (date > STRATEGY DATE). [R-3 active]

§8 CONFLICT AUDIT BLOCK:
  Conflict audit: [typed null or contradiction table]
  [missing block != null]

Dimension Coverage Map:
  | Schema A D-N | Dimension | Signal coverage | Status |

Gate 4: [PHASE 4 GATE: PASS/STOP -- condition: §8 declared + coverage map present]

==============================================================
PHASE 5 -- Proposals  [per Skill Execution Contract]
==============================================================

Authorization check: Authorized §IDs for Phase 5: §5 §6 §7. §9 audit active.
Active rules: R-0 R-1 R-2 R-3 R-4.

Reproduce §5 PROPOSAL SCOPE BLOCK (per R-4, citing Skill Execution Contract §5):
  HIGH-PRESSURE NAMESPACES: [list or "none"]
  Evidence restriction: Only HIGH-PRESSURE namespace artifacts may support proposals.
  SCOPE violation: A proposal row citing an excluded namespace is a SCOPE violation.
  [missing block != null]

Scope Gate: [SCOPE GATE: PASS/STOP -- condition: §5 present; violation condition stated]

PROPOSAL BIAS AUDIT -- apply §9 guard before constructing any proposal row:
  Check LEVEL 1: Evidence selection artifact-driven, not expectation-anchored?
  Check LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE check:
    proposal direction emerged from evidence independently of LEVEL 1 result?
    (LEVEL 1 does not protect against LEVEL 2 -- check independently per §9)
  Compliance: Bias guard = [compliance statement] if both levels pass independently.

Produce §6 PROPOSALS TABLE:
  Before values from §1 Schema A [R-2]. Evidence dated after STRATEGY DATE [R-3].

  | Action | Proposal | Before (§1 [R-2]) | After | Evidence [R-3] |
    Why this beats NO CHANGE [R-0] | Bias guard |

  ADD: none -- inertia holds [R-0].
  REMOVE: none -- inertia holds [R-0].
  REPRIORITIZE: none -- inertia holds [R-0].

Gate 5: [PHASE 5 GATE: PASS/STOP -- condition: Action [5a] + Proposal [5b] +
Before [5c] + After [5d] + Evidence [5e] + Why [5f] + Bias guard [5g] all non-null
across all non-null action rows]

==============================================================
PHASE 6 -- Confirmation Gate  [per Skill Execution Contract]
==============================================================

Authorization check: §7 only.

Present the proposals table. Write:
"Proposed changes to strategy.md above. The default is NO CHANGE [R-0]. Apply?
Reply YES to proceed, NO to cancel, or REVISED with modifications."

Stop. Do not write to strategy.md. Halt here and wait for user reply.

==============================================================
PHASE 7 -- Apply  (after YES or REVISED only)
==============================================================

Apply confirmed proposals to strategy.md. Write only what was confirmed.
No unrequested additions.
```

---

## V-05: Full Ceiling -- Directional Assertion + Complete-Title Citation + Exact Column Value (C-37 + C-38 + C-39)

**Variation axis**: Full combination of all three R16 axes. The PROPOSAL BIAS AUDIT
includes the directional assertion "LEVEL 1 does not protect against LEVEL 2." The SECTION
SCOPE navigation note cites "LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL
DECISION SURFACE" by its complete formal title. CONTRACT B names the exact literal compliant
value string "Bias blocked by guard", enabling value-verification from CONTRACT B alone.

**Hypothesis**: V-05 is the full-ceiling variation that should achieve C-37=FULL, C-38=FULL,
C-39=FULL simultaneously. C-37 and C-38 are structural extensions to existing sites (§9 guard
body and SECTION SCOPE), and C-39 is an extension to CONTRACT B. All three can co-exist
without interaction because they occupy separate structural locations. The denominator expands
from 56 to 62 under v16; V-05 targets 62/62 = 10.00. The exact value string 'Bias blocked by
guard' is quoted/delimited in CONTRACT B so that approximate matches are distinguishable from
exact matches -- this is the precision the rubric requires for C-39 FULL.

```
You are executing the topic-plan skill: revise the signal strategy as new information arrives.

The default outcome of this skill is NO CHANGE to strategy.md.
Every proposal carries the burden of proof against leaving the strategy unchanged.

==============================================================
SKILL EXECUTION CONTRACT
==============================================================

All output templates, constraint rules, phase authorization, and null obligations are
pre-declared below. Every phase executes against this contract and may audit against it.

§1  SCHEMA A TEMPLATE
    D-N | Dimension label | Current value
    Source: strategy.md (filled before any signal is examined).
    Null behavior: all strategy dimensions must appear; no row may be omitted.
    Phase authorization: Phase 1 only.

§2  VERBATIM BLOCK TEMPLATE
    ===VERBATIM BLOCK START===
    "[exact quoted sentence from strategy.md]"
    Source dimension: D-N -- [label matching a Schema A row]
    Enforcement note: A Source dimension field not matching a D-N label in Schema A
                      at seal time is a SEAL violation and fails this block.
    ===VERBATIM BLOCK END===
    Phase authorization: Phase 1 only.

§3  SEALED BLOCK TEMPLATE
    ===STRATEGY SEALED===
    Schema A: COMPLETE
    VERBATIM BLOCK: PRESENT -- D-N source, enforcement note labeled
    Temporal attestation: Commitment phase complete. No signal artifacts read yet.
    Re-read prohibition: strategy.md may not be re-opened until user applies changes. [R-1]
    SEAL violation: A Before value not in Schema A at seal time is a SEAL violation. [R-2]
    ===STRATEGY SEALED===
    Phase authorization: Phase 1 only.

§4  NAMESPACE INVENTORY TABLE TEMPLATE
    namespace | total artifacts | new (date > STRATEGY DATE)
    All 9 namespaces listed. Absent: 0 total | 0 new.
    missing row != absent namespace -- a missing row means the namespace was not checked.
    Phase authorization: Phase 2 only.

§5  PROPOSAL SCOPE BLOCK TEMPLATE
    HIGH-PRESSURE NAMESPACES: [namespaces with new > 0; "none" if list is empty]
    Evidence restriction: Only HIGH-PRESSURE namespace artifacts may support proposals.
    SCOPE violation: A proposal row citing an excluded namespace is a SCOPE violation.
    missing block != null -- a missing §5 block means the scope filter was not applied.
    Phase authorization: Phase 5 only.

§6  PROPOSALS TABLE TEMPLATE
    Action | Proposal | Before (from §1 Schema A) | After | Evidence artifact |
    Why this beats NO CHANGE [R-0] | Bias guard
    Action types: ADD / REMOVE / REPRIORITIZE.
    Null row: "[TYPE]: none -- inertia holds [R-0]."
    missing null row != no proposals -- a missing null row means the type was not evaluated.
    Bias guard column: mandatory in every row; column absence is a CONTRACT B violation.
    Compliant value: 'Bias blocked by guard' (exact literal -- see CONTRACT B).
    Phase authorization: Phase 5 only.

§7  GATE BLOCK TEMPLATE
    [PHASE N GATE: PASS/STOP -- condition: ...]
    Compound gates use [Na][Nb][Nc] labels on sub-conditions.
    Phase authorization: any gate phase.

§8  CONFLICT AUDIT BLOCK TEMPLATE
    Conflict audit: [typed null "no cross-artifact contradictions found"
                     or contradiction table: Artifact A | Artifact B | Dimension | Contradiction]
    missing block != null -- a missing §8 block means the audit was not run.
    Phase authorization: Phase 4 only.

§9  PROPOSAL BIAS AUDIT TEMPLATE
    Two failure modes enumerated as formal labeled levels:

    LEVEL 1: CONFIRMATION ANCHORING AT THE EVIDENCE SCAN SURFACE
    The model reads artifacts through the lens of what it expects to find,
    preferentially noting observations that confirm or oppose the strategy in
    a predetermined direction, rather than reading each artifact without
    regard to desired outcome.

    LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE
    At the moment of individual proposal construction, the model has implicitly
    decided the proposal direction before evaluating evidence, and constructs
    post-hoc justification to fill the Before/After/Evidence/Why columns.

    Mutual necessity: LEVEL 1 and LEVEL 2 guards are both required.
    LEVEL 1 does not protect against LEVEL 2. A run that produces a balanced
    evidence scan (LEVEL 1 satisfied) may still generate proposals driven by
    motivated reasoning at the individual proposal decision surface (LEVEL 2
    failure). The protection hierarchy is not transitive. Both guards must be
    applied independently. A LEVEL 1 pass confers zero LEVEL 2 protection.

    Compliance: every §6 proposal row must carry 'Bias blocked by guard' in the
    Bias guard column. CONTRACT B governs both structural and value compliance.
    Phase authorization: declared pre-execution; audit applies during Phase 5.

PHASE AUTHORIZATION INDEX:
  Phase 1 -- §1 §2 §3 §7
  Phase 2 -- §4 §7
  Phase 3 -- §7 only
  Phase 4 -- §8 §7
  Phase 5 -- §5 §6 §7 (§9 audit active)
  Phase 6 -- §7 (confirmation variant) only
  Phase 7 -- write to strategy.md (post-confirmation only)

CONSTRAINT RULES:
  R-0: Default outcome is NO CHANGE. Every proposal must prove that leaving the strategy
       unchanged produces a worse outcome than the proposed change.
  R-1: strategy.md sealed after §3. May not be re-read before user confirmation.
  R-2: Before values in §6 must trace to §1 Schema A rows at seal time.
  R-3: Evidence restricted to artifacts dated after STRATEGY DATE.
  R-4: Enforcement reproductions cite both contract name and §ID (double-anchored attribution).

CONSTRAINT SCOPE INDEX:
  R-0: Phases 5-6
  R-1: Phases 1-6
  R-2: Phase 5 only
  R-3: Phases 4-5
  R-4: Phase 5 only

PHASE SEQUENCE:
  Phase 1 (Commitment) -> Phase 2 (Inventory) -> Phase 3 (Gate) ->
  Phase 4 (Reading + Conflict Audit) -> Phase 5 (Proposals) ->
  Phase 6 (Confirmation -- halt) -> Phase 7 (Apply -- only after YES or REVISED)

==============================================================
SECTION SCOPE DECLARATION
==============================================================

This skill operates on HIGH-PRESSURE namespaces only (those with new artifacts since
STRATEGY DATE). Proposals citing non-HIGH-PRESSURE namespaces are SCOPE violations.

Bias guard navigation (auditor): the PROPOSAL BIAS AUDIT guard is in §9 above.
The more sophisticated failure mode addressed by this guard is
LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE.
Note that LEVEL 1: CONFIRMATION ANCHORING AT THE EVIDENCE SCAN SURFACE does not protect
against LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE -- both
levels must be applied independently. A proposal row carrying 'Bias blocked by guard'
in the Bias guard column confirms that LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL
PROPOSAL DECISION SURFACE was explicitly checked and cleared, independently of LEVEL 1.

==============================================================
CONTRACT B -- BIAS GUARD COMPLIANCE CONTRACT
==============================================================

Column "Bias guard" is mandatory in every §6 PROPOSALS TABLE row.

Structural compliance: column must be present in every row (including typed-null rows).
A missing column in any row is a CONTRACT B structural violation.

Value compliance: the compliant column value is exactly 'Bias blocked by guard'.
A scorer reading CONTRACT B alone can verify:
  (a) Column exists: structural compliance test.
  (b) Column contains 'Bias blocked by guard': value compliance test.
A column present but not containing 'Bias blocked by guard' is a CONTRACT B value violation.
Approximate variants ('bias blocked', 'guard applied', 'both levels cleared') are not
compliant. Only the exact string 'Bias blocked by guard' satisfies value compliance.

Violation detection from this contract alone:
  STRUCTURAL: Bias guard column absent from any row -> CONTRACT B structural violation.
  VALUE: Bias guard column present but value != 'Bias blocked by guard' -> CONTRACT B value violation.

Both violation types are detectable from this CONTRACT B block without reading phase content.

==============================================================
Gate-0 -- CONTRACT COMPLETENESS GATE
==============================================================

Before Phase 1 begins, verify the SKILL EXECUTION CONTRACT above is complete.

  Arithmetic decomposition: 9 declared schemas + 3 structural checks = 12 items.
  Gate-0 passes when all 12 items confirmed; one STOP result halts Phase 1.

  Schema checks:
  Check [A1]: §1 SCHEMA A present with D-N column, null behavior, phase auth Phase 1?
  Check [A2]: §2 VERBATIM BLOCK present with delimiters, Source dimension, Enforcement note,
              phase auth Phase 1?
  Check [A3]: §3 SEALED BLOCK present with all 5 fields including R-1 and R-2, phase auth Phase 1?
  Check [A4]: §4 NAMESPACE INVENTORY TABLE present with 3 columns, missing-row annotation,
              phase auth Phase 2?
  Check [A5]: §5 PROPOSAL SCOPE BLOCK present with HIGH-PRESSURE field, violation line,
              missing-block annotation, phase auth Phase 5?
  Check [A6]: §6 PROPOSALS TABLE present with all 7 columns including Bias guard with exact
              value reference, null row format, missing-null annotation, phase auth Phase 5?
  Check [A7]: §7 GATE BLOCK present with PASS/STOP format, compound labeling, phase auth any?
  Check [A8]: §8 CONFLICT AUDIT BLOCK present with typed-null or table format, missing-block
              annotation, phase auth Phase 4?
  Check [A9]: §9 PROPOSAL BIAS AUDIT present with LEVEL 1 and LEVEL 2 formal titled labels,
              directional mutual necessity assertion (LEVEL 1 does not protect against LEVEL 2),
              exact compliant value 'Bias blocked by guard', phase auth declaration?

  Structural checks:
  Check [B]: PHASE AUTHORIZATION INDEX -- all 7 phases listed with authorized §IDs?
  Check [C]: CONSTRAINT SCOPE INDEX -- all R-N rules listed with active phase ranges?
  Check [D]: Null annotations present on all typed-null-capable sections?
    §4 "missing row != absent namespace"
    §5 "missing block != null"
    §6 "missing null row != no proposals"
    §8 "missing block != null"

  Item count: 12 items ([A1][A2][A3][A4][A5][A6][A7][A8][A9][B][C][D]).
  A missing §ID produces a detectable missing check item, not a silently failing condition.

  [GATE-0: PASS/STOP -- condition: schemas [A1][A2][A3][A4][A5][A6][A7][A8][A9] all present +
  phase index [B] complete + constraint index [C] complete + null annotations [D] all present;
  reading this condition line enumerates all 12 items required; no item may be inferred by range]

Phase 1 does not begin until Gate-0 passes.

==============================================================
PHASE 1 -- Commitment  [per Skill Execution Contract]
==============================================================

Authorization check: Authorized §IDs for Phase 1: §1 §2 §3 §7.

Open strategy.md. Extract STRATEGY DATE. Fill §1 SCHEMA A.

  | D-N | Dimension label | Current value |

Write §2 VERBATIM BLOCK:
  ===VERBATIM BLOCK START===
  "[exact quoted sentence]"
  Source dimension: D-N -- [matching Schema A row]
  Enforcement note: A Source dimension field not matching a D-N label in Schema A
                    at seal time is a SEAL violation and fails this block.
  ===VERBATIM BLOCK END===

Write §3 SEALED BLOCK:
  ===STRATEGY SEALED===
  Schema A: COMPLETE
  VERBATIM BLOCK: PRESENT -- D-N source, enforcement note labeled
  Temporal attestation: Commitment phase complete. No signal artifacts read yet.
  Re-read prohibition: strategy.md may not be re-opened until user applies changes. [R-1]
  SEAL violation: A Before value not in Schema A at seal time is a SEAL violation. [R-2]
  ===STRATEGY SEALED===

Gate 1: [PHASE 1 GATE: PASS/STOP -- condition: §1 complete [1] + §2 [2a][2b][2c] + §3 [3]]

==============================================================
PHASE 2 -- Signal Inventory  [per Skill Execution Contract]
==============================================================

Authorization check: Authorized §IDs for Phase 2: §4 §7.

Locate all signal artifact files for the topic in simulations/.

Fill §4 NAMESPACE INVENTORY TABLE:
  | namespace | total artifacts | new (date > STRATEGY DATE) |
  [all 9 rows -- scout / draft / review / flow / trace / prove / listen / program / topic]
  [a missing row != 0|0; every namespace must appear]

Gate 2: [PHASE 2 GATE: PASS/STOP -- condition: namespace [2a] + total-artifacts [2b] +
new [2c] all non-null across all 9 rows]

==============================================================
PHASE 3 -- Inventory Completeness Gate  [per Skill Execution Contract]
==============================================================

Authorization check: Authorized §IDs for Phase 3: §7 only.

  Check [3a]: all 9 namespaces present exactly once?
  Check [3b]: total-artifacts non-null for all 9 rows?
  Check [3c]: new non-null for all 9 rows?
  Check [3d]: HIGH-PRESSURE namespaces identified?

  [PHASE 3 GATE: PASS/STOP -- condition: [3a][3b][3c][3d] all satisfied]

==============================================================
PHASE 4 -- Artifact Reading + Conflict Audit  [per Skill Execution Contract]
==============================================================

Authorization check: Authorized §IDs for Phase 4: §8 §7. Active rules: R-1, R-3.

Read every artifact classified new (date > STRATEGY DATE). [R-3 active]

§8 CONFLICT AUDIT BLOCK:
  Conflict audit: [typed null or contradiction table]
  [missing block != null]

Dimension Coverage Map:
  | Schema A D-N | Dimension | Signal coverage | Status |

Gate 4: [PHASE 4 GATE: PASS/STOP -- condition: §8 declared + coverage map present]

==============================================================
PHASE 5 -- Proposals  [per Skill Execution Contract]
==============================================================

Authorization check: Authorized §IDs for Phase 5: §5 §6 §7. §9 audit active.
Active rules: R-0 R-1 R-2 R-3 R-4.

Reproduce §5 PROPOSAL SCOPE BLOCK (per R-4, citing Skill Execution Contract §5):
  HIGH-PRESSURE NAMESPACES: [list or "none"]
  Evidence restriction: Only HIGH-PRESSURE namespace artifacts may support proposals.
  SCOPE violation: A proposal row citing an excluded namespace is a SCOPE violation.
  [missing block != null]

Scope Gate: [SCOPE GATE: PASS/STOP -- condition: §5 present; violation condition stated]

PROPOSAL BIAS AUDIT -- apply §9 guard before constructing any proposal row:
  Check LEVEL 1: Evidence selection artifact-driven, not expectation-anchored?
  Check LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE check:
    each proposal direction emerged from evidence independently of LEVEL 1 result?
    (LEVEL 1 does not protect against LEVEL 2; this check is independent per §9.)
  If both LEVEL 1 and LEVEL 2 pass: Bias guard = 'Bias blocked by guard' (CONTRACT B).
  If either level fails: drop the proposal; do not populate the row.

Produce §6 PROPOSALS TABLE:
  Before values from §1 Schema A [R-2]. Evidence dated after STRATEGY DATE [R-3].
  Every proposal must name a concrete consequence of NOT changing [R-0].

  | Action | Proposal | Before (§1 [R-2]) | After | Evidence [R-3] |
    Why this beats NO CHANGE [R-0] | Bias guard |

  [missing null row != no proposals for that type]
  ADD: none -- inertia holds [R-0].
  REMOVE: none -- inertia holds [R-0].
  REPRIORITIZE: none -- inertia holds [R-0].

Gate 5: [PHASE 5 GATE: PASS/STOP -- condition: Action [5a] + Proposal [5b] +
Before [5c] + After [5d] + Evidence [5e] + Why [5f] + Bias guard [5g] = 'Bias blocked by guard'
[CONTRACT B] all satisfied across all non-null action rows]

==============================================================
PHASE 6 -- Confirmation Gate  [per Skill Execution Contract]
==============================================================

Authorization check: §7 only.

Present the proposals table. Write:
"Proposed changes to strategy.md above. The default is NO CHANGE [R-0]. Apply?
Reply YES to proceed, NO to cancel, or REVISED with modifications."

Stop. Do not write to strategy.md. Halt here and wait for user reply.

==============================================================
PHASE 7 -- Apply  (after YES or REVISED only)
==============================================================

Apply confirmed proposals to strategy.md. Write only what was confirmed.
No unrequested additions.
```
