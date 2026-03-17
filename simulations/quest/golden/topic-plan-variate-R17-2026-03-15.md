---
skill: quest-variate
skill_target: topic-plan
date: 2026-03-15
round: 17
rubric: topic-plan-rubric-v17-2026-03-15.md
new_criteria: [C-52, C-53]
prior_ceiling: R16-V05
---

# topic-plan Skill Variations -- Round 17 (2026-03-15)

Rubric: v17 (C-01--C-53, 45 aspirational, formula: essential*60 + recommended*30 + aspirational*10)
New criteria this round: C-52 (pass-threshold count derivation arithmetic exposed),
C-53 (procedural pre-proposal step declared as named schema block)

---

## Round 17 Design Notes

R16 V-05 is the implicit ceiling that revealed C-52 and C-53. The two new v17 criteria
emerge from contrasting R16 V-05 against R16 V-01-V-04 at Gate-0:

1. **C-52 from R16 V-01-V-04 threshold-annotation gap** -- R16 V-01, V-02, V-03, and
   V-04 all satisfy C-46 (pass-threshold annotation states "passes when all N confirmed")
   using a constant N without derivation: "GATE-0 PASS THRESHOLD: passes when all 11
   items confirmed." R16 V-05 introduces a separate "Arithmetic decomposition: 9 declared
   schemas + 3 structural checks = 12 items total" line adjacent to the threshold field.
   C-52 requires the arithmetic to be absorbed INTO the threshold annotation itself:
   "GATE-0 PASS THRESHOLD: 9 declared schemas + 3 structural checks = 12 items total;
   passes when all 12 confirmed." When the arithmetic is inside the threshold field, the
   item count is derivable from the field alone -- a writer who adds or removes a schema
   block must update both M and N in the threshold annotation, making divergence between
   the Phase -1 schema inventory and the gate item count immediately detectable. R16 V-05
   has arithmetic adjacent to (not inside) the threshold; this form satisfies the spirit
   but is detected as failing C-52's letter requirement.

2. **C-53 from R16 V-01-V-04 §5b classification gap** -- R16 V-01, V-02, V-03, and V-04
   treat §5b (NO CHANGE EVALUATION) as an inline Phase 5 instruction with no schema block
   declared in the contract and no Gate-0 check item. R16 V-05 promotes §5b to a named
   contract schema block with its own §ID and a corresponding Gate-0 Check [A6], making
   the pre-proposal evaluation independently auditable. C-53 formalizes this: a procedural
   evaluation step that appears only as an inline instruction cannot be detected as absent
   by Gate-0; a named schema block with its own check item can.

**R16 gap analysis for R17:**

| Gap | R16 variations missing | R17 axis |
|-----|------------------------|----------|
| G-01 | V-01-V-04 lack C-52 (arithmetic outside threshold) | V-01: Output format -- arithmetic merged into THRESHOLD field (C-52 isolated) |
| G-02 | V-01-V-04 lack C-53 (§5b not a schema block) | V-02: Lifecycle emphasis -- §5b promoted to named schema block (C-53 isolated) |
| G-03 | No variation tests C-52 without C-49 (attestation) | V-03: Phrasing register -- arithmetic in threshold, no attestation (C-52 isolated, C-49 absent) |
| G-04 | No variation names C-52+C-53 as combined target | V-04: Combined output+lifecycle -- arithmetic in threshold + §5b schema block (C-52+C-53) |
| G-05 | C-43-C-53 require simultaneous satisfaction | V-05: Full ceiling -- all axes (C-43--C-53) + role sequence (§5b evaluated first) |

**Round 17 variation map:**

| Variation | Axis | Criteria targeted | C-52 | C-53 |
|-----------|------|-------------------|------|------|
| V-01 | Output format -- arithmetic merged into THRESHOLD field | C-52 | YES | NO |
| V-02 | Lifecycle emphasis -- §5b promoted to named schema block | C-53 | NO | YES |
| V-03 | Phrasing register -- arithmetic in threshold, no attestation | C-52 (C-49 absent) | YES | NO |
| V-04 | Combined output format + lifecycle | C-52+C-53 | YES | YES |
| V-05 | Combined all axes (full R17 ceiling) | C-43--C-53 | YES | YES |

---

## V-01: Output Format -- Arithmetic Merged into THRESHOLD Field (C-52 only)

**Variation axis**: Output format -- single axis. The Gate-0 annotation is upgraded from
R16 V-04 (two separate labeled fields: "Arithmetic decomposition: 8 declared schemas... =
11 items total" + "GATE-0 PASS THRESHOLD: passes when all 11 confirmed") to a single
merged field: "GATE-0 PASS THRESHOLD: 8 declared schemas + 3 structural checks = 11 items
total; passes when all 11 items confirmed; blocked by any single STOP result." The
separate "Arithmetic decomposition:" label is removed. The attestation clause (C-49),
grouped condition line (C-50), and co-location in dedicated labeled field (C-51) are all
carried forward from R16 V-04 unchanged. §5b is NOT a schema block (C-53 absent).

**Hypothesis**: C-52 requires the schema-phase gate pass-threshold annotation to make the
item count N derivable from an explicit arithmetic decomposition embedded within the
annotation itself. R16 V-04 satisfies C-46 (threshold annotation present) with a bare
count: "passes when all 11 confirmed." The separate "Arithmetic decomposition:" line
establishes the derivation but lives outside the threshold field. C-52 requires N to be
derivable from the threshold annotation alone -- not from an adjacent field. V-01 tests
whether merging the arithmetic into the THRESHOLD field ("8 declared schemas + 3
structural checks = 11 items total; passes when all 11 confirmed") satisfies C-52 while
leaving all R16 V-04 criteria (C-43-C-51) unchanged. §5b absent isolates C-52.

---

```
You are executing the topic-plan skill: revise the signal strategy as new information arrives.

The default outcome of this skill is NO CHANGE to strategy.md.
Every proposal carries the burden of proof against leaving the strategy unchanged.

══════════════════════════════════════════════════════════════
SKILL EXECUTION CONTRACT
══════════════════════════════════════════════════════════════

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
    Why this beats NO CHANGE [R-0]
    Action types: ADD / REMOVE / REPRIORITIZE.
    Null row: "[TYPE]: none -- inertia holds [R-0]."
    missing null row != no proposals -- a missing null row means the type was not evaluated.
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

PHASE AUTHORIZATION INDEX:
  Phase 1 -- §1 §2 §3 §7
  Phase 2 -- §4 §7
  Phase 3 -- §7 only
  Phase 4 -- §8 §7
  Phase 5 -- §5 §6 §7
  Phase 6 -- §7 (confirmation variant) only
  Phase 7 -- write to strategy.md (post-confirmation only)

CONSTRAINT RULES:
  R-0: Default outcome is NO CHANGE. Every proposal must prove that leaving the strategy
       unchanged produces a worse outcome than the proposed change. A proposal unable to
       name a concrete consequence of NOT changing fails R-0 and must be dropped.
  R-1: strategy.md sealed after §3. May not be re-read before user confirmation.
  R-2: Before values in §6 must trace to §1 Schema A rows at seal time. A Before value
       not in Schema A at seal time is a SEAL violation and must be dropped.
  R-3: Evidence restricted to artifacts dated after STRATEGY DATE. Evidence from prior
       artifacts is ineligible regardless of namespace.
  R-4: Enforcement reproductions cite both contract name and §ID (double-anchored attribution).

CONSTRAINT SCOPE INDEX:
  R-0: Phases 5-6 (active during proposal evaluation and confirmation framing)
  R-1: Phases 1-6 (active from §3 seal through Phase 6 confirmation)
  R-2: Phase 5 only (Before-value sourcing in §6 proposals table)
  R-3: Phases 4-5 (delta detection in Phase 4; proposal evidence in Phase 5)
  R-4: Phase 5 only (§5 PROPOSAL SCOPE and §6 reproductions)

PHASE SEQUENCE:
  Phase 1 (Commitment) -> Phase 2 (Inventory) -> Phase 3 (Gate) ->
  Phase 4 (Reading + Conflict Audit) -> Phase 5 (Proposals) ->
  Phase 6 (Confirmation -- halt) -> Phase 7 (Apply -- only after YES or REVISED)

══════════════════════════════════════════════════════════════
Gate-0 -- CONTRACT COMPLETENESS GATE
══════════════════════════════════════════════════════════════

Before Phase 1 begins, verify the SKILL EXECUTION CONTRACT above is complete.

  GATE-0 PASS THRESHOLD: 8 declared schemas + 3 structural checks = 11 items total;
  passes when all 11 items confirmed; blocked by any single STOP result.

  Schema checks -- one item per declared §ID:
  Check [A1]: §1 SCHEMA A -- columns D-N | Dimension label | Current value present,
              null behavior "no row may be omitted" present, phase authorization Phase 1?
  Check [A2]: §2 VERBATIM BLOCK -- delimiters present, Source dimension field present,
              Enforcement note field present, phase authorization Phase 1?
  Check [A3]: §3 SEALED BLOCK -- Schema A complete field present, VERBATIM BLOCK present
              field present, Temporal attestation present, Re-read prohibition [R-1] present,
              SEAL violation [R-2] present, phase authorization Phase 1?
  Check [A4]: §4 NAMESPACE INVENTORY TABLE -- columns namespace | total artifacts | new
              present, missing-row annotation present, phase authorization Phase 2?
  Check [A5]: §5 PROPOSAL SCOPE BLOCK -- HIGH-PRESSURE NAMESPACES field present, Evidence
              restriction present, SCOPE violation line present, missing-block annotation
              present, phase authorization Phase 5?
  Check [A6]: §6 PROPOSALS TABLE -- columns Action | Proposal | Before | After | Evidence
              artifact | Why present, null row format present, missing-null annotation present,
              phase authorization Phase 5?
  Check [A7]: §7 GATE BLOCK -- [PHASE N GATE: PASS/STOP] format present, compound [Na][Nb]
              labeling present, phase authorization "any gate phase" present?
  Check [A8]: §8 CONFLICT AUDIT BLOCK -- typed null or contradiction table format present,
              missing-block annotation present, phase authorization Phase 4?

  Structural checks:
  Check [B]: PHASE AUTHORIZATION INDEX present and populated?
    All 7 phases (Phase 1 through Phase 7) listed with their authorized §IDs.
  Check [C]: CONSTRAINT SCOPE INDEX present and populated?
    All R-N rules (R-0 through R-4) listed with their active phase ranges.
  Check [D]: Null annotations present on all typed-null-capable sections?
    §4 "missing row != absent namespace"
    §5 "missing block != null"
    §6 "missing null row != no proposals"
    §8 "missing block != null"

  Item count: 11 items ([A1][A2][A3][A4][A5][A6][A7][A8][B][C][D]) = 8 schemas + 3 structural.
  A missing §ID produces a detectable missing check item, not a silently failing compound condition.

  [GATE-0: PASS/STOP -- condition: schemas [A1][A2][A3][A4][A5][A6][A7][A8] all present +
  phase index [B] complete + constraint index [C] complete + null annotations [D] all present;
  reading this condition line enumerates all 11 required items; no item may be inferred by range]

Phase 1 does not begin until Gate-0 passes.

══════════════════════════════════════════════════════════════
PHASE 1 -- Commitment  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 1: §1 Schema A, §2 VERBATIM BLOCK, §3 SEALED BLOCK, §7 Gate block.
  Active constraint rules for Phase 1 (per §CONSTRAINT SCOPE INDEX): R-1 activates at §3.
  No other §ID templates may be instantiated in this phase.

Open strategy.md. Extract last-modified date: STRATEGY DATE: [YYYY-MM-DD]. Close.
Re-open to read content. Fill §1 SCHEMA A. Close.

Fill §1 SCHEMA A (reproduced from Skill Execution Contract §1):
  | D-N | Dimension label | Current value |
  [all strategy dimensions -- per §1 null behavior: no row may be omitted]

Write §2 VERBATIM BLOCK (reproduced from Skill Execution Contract §2):
  ===VERBATIM BLOCK START===
  "[exact quoted sentence]"
  Source dimension: D-N -- [matching Schema A row]
  Enforcement note: A Source dimension field not matching a D-N label in Schema A
                    at seal time is a SEAL violation and fails this block.
  ===VERBATIM BLOCK END===

Write §3 SEALED BLOCK (reproduced from Skill Execution Contract §3) -- R-1 activates here:
  ===STRATEGY SEALED===
  Schema A: COMPLETE
  VERBATIM BLOCK: PRESENT -- D-N source, enforcement note labeled
  Temporal attestation: Commitment phase complete. No signal artifacts read yet.
  Re-read prohibition: strategy.md may not be re-opened until user applies changes. [R-1]
  SEAL violation: A Before value not in Schema A at seal time is a SEAL violation. [R-2]
  ===STRATEGY SEALED===

Gate 1 (§7 -- reproduced from Skill Execution Contract §7):
  Check [1]: §1 Schema A complete -- all D-N rows present?
  Check [2]:
    [2a] §2 VERBATIM BLOCK delimiters present?
    [2b] Source dimension in D-N format matching Schema A?
    [2c] Enforcement note present as labeled field?
  Check [3]: §3 SEALED BLOCK present with all fields including re-read prohibition [R-1]
             and SEAL violation definition [R-2]?
  [PHASE 1 GATE: PASS/STOP -- condition: §1 [1] + §2 [2a][2b][2c] + §3 [3]]

══════════════════════════════════════════════════════════════
PHASE 2 -- Signal Inventory  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 2: §4 Namespace inventory table, §7 Gate block.
  Active constraint rules for Phase 2 (per §CONSTRAINT SCOPE INDEX): R-1 (seal holds).
  No other §ID templates may be instantiated in this phase.

Locate all signal artifact files for the topic in simulations/.

Fill §4 NAMESPACE INVENTORY TABLE (reproduced from Skill Execution Contract §4):
  | namespace | total artifacts | new (date > STRATEGY DATE) |
  [all 9 namespace rows -- per contract §4: a missing row != 0|0; every namespace must appear]

HIGH-PRESSURE namespaces: those with new > 0.

Gate 2 (§7 -- reproduced from Skill Execution Contract §7):
  Check [2a]: namespace column -- all 9 values present and non-null
              (scout, draft, review, flow, trace, prove, listen, program, topic)?
  Check [2b]: total-artifacts column -- non-null for every row?
  Check [2c]: new(date > STRATEGY DATE) column -- non-null for every row?
  [PHASE 2 GATE: PASS/STOP -- condition: namespace column [2a] + total-artifacts column [2b] +
  new column [2c] all non-null across all 9 rows; no blank cells in mandatory columns]

══════════════════════════════════════════════════════════════
PHASE 3 -- Inventory Completeness Gate  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 3: §7 Gate block only.
  Active constraint rules for Phase 3 (per §CONSTRAINT SCOPE INDEX): R-1 (seal holds).
  No other §ID templates may be instantiated in this phase.

  Check [3a]: namespace column: all 9 names present -- scout, draft, review, flow, trace,
              prove, listen, program, topic -- each exactly once?
  Check [3b]: total-artifacts column: non-null for all 9 rows?
  Check [3c]: new column: non-null for all 9 rows?
  Check [3d]: HIGH-PRESSURE namespaces identified from rows where new > 0?
  [PHASE 3 GATE: PASS/STOP -- condition: §4 namespace column [3a] + total-artifacts column [3b] +
  new column [3c] all non-null across all rows; HIGH-PRESSURE namespaces identified [3d]]

══════════════════════════════════════════════════════════════
PHASE 4 -- Artifact Reading + Conflict Audit  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 4: §8 Conflict audit block, §7 Gate block.
  Active constraint rules for Phase 4 (per §CONSTRAINT SCOPE INDEX): R-1 (seal holds),
    R-3 (evidence restricted to artifacts dated after STRATEGY DATE).
  No other §ID templates may be instantiated in this phase.

Read every artifact classified new (date > STRATEGY DATE) in full. [R-3 active]

§8 CONFLICT AUDIT BLOCK (reproduced from Skill Execution Contract §8):
  Conflict audit: [typed null "no cross-artifact contradictions found" or contradiction table]
  [Per contract §8: missing block != null -- declare the null if no contradictions found.]

For each observation:
  Condition 1: artifact date > STRATEGY DATE? [R-3 eligibility]
  Condition 2: absent from §1 Schema A? [R-2 dependency]
  CONFIRMED NEW = both YES. PRIOR-ONLY = C1 YES, C2 NO. Label: "PRIOR-ONLY -- not a delta."

Dimension Coverage Map:
  | Schema A D-N | Dimension | Signal coverage | Status |

Gate 4 (§7 -- reproduced from Skill Execution Contract §7):
  [PHASE 4 GATE: PASS/STOP -- condition: §8 declared (typed null or table) + delta labels applied]

══════════════════════════════════════════════════════════════
PHASE 5 -- Proposals  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 5: §5 PROPOSAL SCOPE, §6 Proposals table, §7 Gate block.
  Active constraint rules for Phase 5 (per §CONSTRAINT SCOPE INDEX): R-0 (inertia test
    for each proposal), R-1 (seal holds), R-2 (Before values from §1 Schema A only),
    R-3 (evidence dated after STRATEGY DATE), R-4 (reproductions double-anchored).
  No other §ID templates may be instantiated in this phase.

Reproduce §5 PROPOSAL SCOPE BLOCK (reproduced from Skill Execution Contract §5, per R-4):
  HIGH-PRESSURE NAMESPACES: [namespaces with new > 0; "none" if empty]
  Evidence restriction: Only HIGH-PRESSURE namespace artifacts may support proposals.
  SCOPE violation: A proposal row citing an excluded namespace is a SCOPE violation.
  [Per contract §5: missing block != null -- an absent §5 block means the scope filter
  was not applied.]

Scope Gate (§7 -- reproduced from Skill Execution Contract §7):
  [SCOPE GATE: PASS/STOP -- condition: §5 block present; violation condition line present]

Produce §6 PROPOSALS TABLE (reproduced from Skill Execution Contract §6, per R-4):
  Before values sourced from §1 Schema A -- not from strategy.md. [R-2 active]
  Evidence from HIGH-PRESSURE namespace artifacts only, dated after STRATEGY DATE. [R-3 active]
  Every proposal must name a concrete consequence of NOT changing to pass R-0. [R-0 active]

  | Action | Proposal | Before (from §1 Schema A [R-2]) | After |
    Evidence artifact [R-3] | Why this beats NO CHANGE [R-0] |

  [Per contract §6: a missing null row != no proposals for that type]
  ADD: none -- inertia holds [R-0].
  REMOVE: none -- inertia holds [R-0].
  REPRIORITIZE: none -- inertia holds [R-0].

Gate 5 (§7 -- reproduced from Skill Execution Contract §7):
  Check [5a]: Action column -- non-null for every row?
  Check [5b]: Proposal column -- non-null for every non-null action row?
  Check [5c]: Before column -- non-null; sourced from §1 Schema A [R-2]?
  Check [5d]: After column -- non-null for every non-null action row?
  Check [5e]: Evidence artifact column -- non-null for every non-null action row [R-3]?
  Check [5f]: Why this beats NO CHANGE column -- non-null for every non-null action row [R-0]?
  [PHASE 5 GATE: PASS/STOP -- condition: Action column [5a] + Proposal column [5b] +
  Before column [5c] + After column [5d] + Evidence artifact column [5e] +
  Why column [5f] all non-null across all non-null action rows]

══════════════════════════════════════════════════════════════
PHASE 6 -- Confirmation Gate  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 6: §7 Gate block (CONFIRMATION variant) only.
  Active constraint rules for Phase 6 (per §CONSTRAINT SCOPE INDEX): R-0 (inertia co-equal
    option), R-1 (seal holds until YES/REVISED).
  No other §ID templates may be instantiated in this phase.

Present the proposals table. Write:
"Proposed changes to strategy.md above. The default is NO CHANGE [R-0]. Apply?
Reply YES to proceed, NO to cancel, or REVISED with modifications."

Stop. Do not write to strategy.md. Halt here and wait for user reply.

══════════════════════════════════════════════════════════════
PHASE 7 -- Apply  (after YES or REVISED only)
══════════════════════════════════════════════════════════════

Apply confirmed proposals to strategy.md. Write only what was confirmed.
No unrequested additions.
```

---

## V-02: Lifecycle Emphasis -- §5b Promoted to Named Schema Block (C-53 only)

**Variation axis**: Lifecycle emphasis -- single axis. §5b NO CHANGE EVALUATION BLOCK is
promoted from an inline Phase 5 instruction to a named contract schema block with its own
§ID and a corresponding Gate-0 Check [A6]. The schema renumbering shifts old [A6]-[A8] to
[A7]-[A9], producing 9 declared schemas. The item count rises from 11 to 12. The GATE-0
PASS THRESHOLD retains the bare-count form: "passes when all 12 items confirmed; blocked
by any single STOP result." The arithmetic appears as a SEPARATE "Item count: 12 items =
9 schemas + 3 structural" annotation (same placement as R16 V-04), NOT inside the
THRESHOLD field itself. C-52 is deliberately absent. C-49, C-50, C-51 carry forward from
R16 V-04.

**Hypothesis**: C-53 requires a procedural pre-proposal step to be declared as a named
schema block participating in Gate-0. R16 V-01-V-04 treat §5b as an inline Phase 5
instruction; it has no §ID, no Gate-0 check, and cannot be detected as absent. V-02
tests whether promoting §5b to a named schema block with Check [A6] satisfies C-53 while
the threshold annotation remains bare-count (C-52 absent). The item count annotation is
updated to 12 (separate from threshold), confirming the arithmetic is present but NOT
embedded inside the threshold field. If C-52 and C-53 score independently, V-02 should
gain C-53 without gaining C-52.

---

```
You are executing the topic-plan skill: revise the signal strategy as new information arrives.

The default outcome of this skill is NO CHANGE to strategy.md.
Every proposal carries the burden of proof against leaving the strategy unchanged.

══════════════════════════════════════════════════════════════
SKILL EXECUTION CONTRACT
══════════════════════════════════════════════════════════════

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

§5b NO CHANGE EVALUATION BLOCK TEMPLATE
    NO CHANGE EVALUATION [R-0]:
    Status quo dimensions: [every §1 Schema A D-N label with current value]
    New signal pressure: [HIGH-PRESSURE namespaces with artifact counts; "none" if empty]
    Evaluation: [for each dimension under new signal pressure, state whether new signal
                 evidence reveals a concrete consequence of NOT changing that dimension;
                 "no pressure" is a valid finding for dimensions with no coverage]
    Outcome: NO CHANGE HOLDS / PARTIAL CHANGE WARRANTED / FULL CHANGE WARRANTED
    Null behavior: if no HIGH-PRESSURE namespaces, write "Outcome: NO CHANGE HOLDS --
                   no new signals since strategy date."
    missing block != null -- a missing §5b block means the inertia evaluation was not run.
    Phase authorization: Phase 5 only (after §5 PROPOSAL SCOPE, before §6 PROPOSALS TABLE).

§6  PROPOSALS TABLE TEMPLATE
    Action | Proposal | Before (from §1 Schema A) | After | Evidence artifact |
    Why this beats NO CHANGE [R-0]
    Action types: ADD / REMOVE / REPRIORITIZE.
    Null row: "[TYPE]: none -- inertia holds [R-0]."
    missing null row != no proposals -- a missing null row means the type was not evaluated.
    Phase authorization: Phase 5 only (after §5b NO CHANGE EVALUATION).

§7  GATE BLOCK TEMPLATE
    [PHASE N GATE: PASS/STOP -- condition: ...]
    Compound gates use [Na][Nb][Nc] labels on sub-conditions.
    Phase authorization: any gate phase.

§8  CONFLICT AUDIT BLOCK TEMPLATE
    Conflict audit: [typed null "no cross-artifact contradictions found"
                     or contradiction table: Artifact A | Artifact B | Dimension | Contradiction]
    missing block != null -- a missing §8 block means the audit was not run.
    Phase authorization: Phase 4 only.

PHASE AUTHORIZATION INDEX:
  Phase 1 -- §1 §2 §3 §7
  Phase 2 -- §4 §7
  Phase 3 -- §7 only
  Phase 4 -- §8 §7
  Phase 5 -- §5 §5b §6 §7
  Phase 6 -- §7 (confirmation variant) only
  Phase 7 -- write to strategy.md (post-confirmation only)

CONSTRAINT RULES:
  R-0: Default outcome is NO CHANGE. Every proposal must prove that leaving the strategy
       unchanged produces a worse outcome than the proposed change. A proposal unable to
       name a concrete consequence of NOT changing fails R-0 and must be dropped.
       NO CHANGE is evaluated first as a named option in §5b before any proposals are
       generated; proposals must beat the §5b evaluation outcome for that dimension.
  R-1: strategy.md sealed after §3. May not be re-read before user confirmation.
  R-2: Before values in §6 must trace to §1 Schema A rows at seal time. A Before value
       not in Schema A at seal time is a SEAL violation and must be dropped.
  R-3: Evidence restricted to artifacts dated after STRATEGY DATE. Evidence from prior
       artifacts is ineligible regardless of namespace.
  R-4: Enforcement reproductions cite both contract name and §ID (double-anchored attribution).

CONSTRAINT SCOPE INDEX:
  R-0: Phases 5-6 (§5b evaluation, §6 proposal generation, and confirmation framing)
  R-1: Phases 1-6 (active from §3 seal through Phase 6 confirmation)
  R-2: Phase 5 only (Before-value sourcing in §6 proposals table)
  R-3: Phases 4-5 (delta detection in Phase 4; proposal evidence in Phase 5)
  R-4: Phase 5 only (§5, §5b, and §6 reproductions)

PHASE SEQUENCE:
  Phase 1 (Commitment) -> Phase 2 (Inventory) -> Phase 3 (Gate) ->
  Phase 4 (Reading + Conflict Audit) -> Phase 5 (Proposals) ->
  Phase 6 (Confirmation -- halt) -> Phase 7 (Apply -- only after YES or REVISED)

══════════════════════════════════════════════════════════════
Gate-0 -- CONTRACT COMPLETENESS GATE
══════════════════════════════════════════════════════════════

Before Phase 1 begins, verify the SKILL EXECUTION CONTRACT above is complete.

  Item count: 12 items ([A1][A2][A3][A4][A5][A6][A7][A8][A9][B][C][D]) = 9 schemas + 3 structural.
  GATE-0 PASS THRESHOLD: passes when all 12 items confirmed; blocked by any single STOP result.

  Schema checks -- one item per declared §ID:
  Check [A1]: §1 SCHEMA A -- columns D-N | Dimension label | Current value present,
              null behavior "no row may be omitted" present, phase authorization Phase 1?
  Check [A2]: §2 VERBATIM BLOCK -- delimiters present, Source dimension field present,
              Enforcement note field present, phase authorization Phase 1?
  Check [A3]: §3 SEALED BLOCK -- Schema A complete field present, VERBATIM BLOCK present
              field present, Temporal attestation present, Re-read prohibition [R-1] present,
              SEAL violation [R-2] present, phase authorization Phase 1?
  Check [A4]: §4 NAMESPACE INVENTORY TABLE -- columns namespace | total artifacts | new
              present, missing-row annotation present, phase authorization Phase 2?
  Check [A5]: §5 PROPOSAL SCOPE BLOCK -- HIGH-PRESSURE NAMESPACES field present, Evidence
              restriction present, SCOPE violation line present, missing-block annotation
              present, phase authorization Phase 5?
  Check [A6]: §5b NO CHANGE EVALUATION BLOCK -- Status quo dimensions field present, New
              signal pressure field present, Evaluation field present, Outcome field present,
              null behavior for zero-pressure case present, missing-block annotation present,
              phase authorization Phase 5 (after §5, before §6)?
  Check [A7]: §6 PROPOSALS TABLE -- columns Action | Proposal | Before | After | Evidence
              artifact | Why present, null row format present, missing-null annotation present,
              phase authorization Phase 5 (after §5b)?
  Check [A8]: §7 GATE BLOCK -- [PHASE N GATE: PASS/STOP] format present, compound [Na][Nb]
              labeling present, phase authorization "any gate phase" present?
  Check [A9]: §8 CONFLICT AUDIT BLOCK -- typed null or contradiction table format present,
              missing-block annotation present, phase authorization Phase 4?

  Structural checks:
  Check [B]: PHASE AUTHORIZATION INDEX present and populated?
    All 7 phases listed with authorized §IDs.
    Phase 5 must list §5, §5b, §6, and §7.
  Check [C]: CONSTRAINT SCOPE INDEX present and populated?
    All R-N rules (R-0 through R-4) listed with active phase ranges.
    R-0 must reference §5b evaluation in its scope description.
  Check [D]: Null annotations present on all typed-null-capable sections?
    §4 "missing row != absent namespace"
    §5 "missing block != null"
    §5b "missing block != null"
    §6 "missing null row != no proposals"
    §8 "missing block != null"

  A missing §ID produces a detectable missing check item, not a silently failing compound condition.

  [GATE-0: PASS/STOP -- condition: schemas [A1][A2][A3][A4][A5][A6][A7][A8][A9] all present +
  phase index [B] complete + constraint index [C] complete + null annotations [D] all present;
  reading this condition line enumerates all 12 required items; no item may be inferred by range]

Phase 1 does not begin until Gate-0 passes.

══════════════════════════════════════════════════════════════
PHASE 1 -- Commitment  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 1: §1 Schema A, §2 VERBATIM BLOCK, §3 SEALED BLOCK, §7 Gate block.
  Active constraint rules for Phase 1 (per §CONSTRAINT SCOPE INDEX): R-1 activates at §3.
  No other §ID templates may be instantiated in this phase.

Open strategy.md. Extract last-modified date: STRATEGY DATE: [YYYY-MM-DD]. Close.
Re-open to read content. Fill §1 SCHEMA A. Close.

Fill §1 SCHEMA A (reproduced from Skill Execution Contract §1):
  | D-N | Dimension label | Current value |
  [all strategy dimensions -- per §1 null behavior: no row may be omitted]

Write §2 VERBATIM BLOCK (reproduced from Skill Execution Contract §2):
  ===VERBATIM BLOCK START===
  "[exact quoted sentence]"
  Source dimension: D-N -- [matching Schema A row]
  Enforcement note: A Source dimension field not matching a D-N label in Schema A
                    at seal time is a SEAL violation and fails this block.
  ===VERBATIM BLOCK END===

Write §3 SEALED BLOCK (reproduced from Skill Execution Contract §3) -- R-1 activates here:
  ===STRATEGY SEALED===
  Schema A: COMPLETE
  VERBATIM BLOCK: PRESENT -- D-N source, enforcement note labeled
  Temporal attestation: Commitment phase complete. No signal artifacts read yet.
  Re-read prohibition: strategy.md may not be re-opened until user applies changes. [R-1]
  SEAL violation: A Before value not in Schema A at seal time is a SEAL violation. [R-2]
  ===STRATEGY SEALED===

Gate 1 (§7 -- reproduced from Skill Execution Contract §7):
  Check [1]: §1 Schema A complete -- all D-N rows present?
  Check [2]:
    [2a] §2 VERBATIM BLOCK delimiters present?
    [2b] Source dimension in D-N format matching Schema A?
    [2c] Enforcement note present as labeled field?
  Check [3]: §3 SEALED BLOCK present with all fields including re-read prohibition [R-1]
             and SEAL violation definition [R-2]?
  [PHASE 1 GATE: PASS/STOP -- condition: §1 [1] + §2 [2a][2b][2c] + §3 [3]]

══════════════════════════════════════════════════════════════
PHASE 2 -- Signal Inventory  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 2: §4 Namespace inventory table, §7 Gate block.
  Active constraint rules for Phase 2 (per §CONSTRAINT SCOPE INDEX): R-1 (seal holds).
  No other §ID templates may be instantiated in this phase.

Locate all signal artifact files for the topic in simulations/.

Fill §4 NAMESPACE INVENTORY TABLE (reproduced from Skill Execution Contract §4):
  | namespace | total artifacts | new (date > STRATEGY DATE) |
  [all 9 namespace rows -- per contract §4: a missing row != 0|0; every namespace must appear]

HIGH-PRESSURE namespaces: those with new > 0.

Gate 2 (§7 -- reproduced from Skill Execution Contract §7):
  Check [2a]: namespace column -- all 9 values present and non-null
              (scout, draft, review, flow, trace, prove, listen, program, topic)?
  Check [2b]: total-artifacts column -- non-null for every row?
  Check [2c]: new(date > STRATEGY DATE) column -- non-null for every row?
  [PHASE 2 GATE: PASS/STOP -- condition: namespace column [2a] + total-artifacts column [2b] +
  new column [2c] all non-null across all 9 rows; no blank cells in mandatory columns]

══════════════════════════════════════════════════════════════
PHASE 3 -- Inventory Completeness Gate  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 3: §7 Gate block only.
  Active constraint rules for Phase 3 (per §CONSTRAINT SCOPE INDEX): R-1 (seal holds).
  No other §ID templates may be instantiated in this phase.

  Check [3a]: namespace column: all 9 names present -- scout, draft, review, flow, trace,
              prove, listen, program, topic -- each exactly once?
  Check [3b]: total-artifacts column: non-null for all 9 rows?
  Check [3c]: new column: non-null for all 9 rows?
  Check [3d]: HIGH-PRESSURE namespaces identified from rows where new > 0?
  [PHASE 3 GATE: PASS/STOP -- condition: §4 namespace column [3a] + total-artifacts column [3b] +
  new column [3c] all non-null across all rows; HIGH-PRESSURE namespaces identified [3d]]

══════════════════════════════════════════════════════════════
PHASE 4 -- Artifact Reading + Conflict Audit  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 4: §8 Conflict audit block, §7 Gate block.
  Active constraint rules for Phase 4 (per §CONSTRAINT SCOPE INDEX): R-1 (seal holds),
    R-3 (evidence restricted to artifacts dated after STRATEGY DATE).
  No other §ID templates may be instantiated in this phase.

Read every artifact classified new (date > STRATEGY DATE) in full. [R-3 active]

§8 CONFLICT AUDIT BLOCK (reproduced from Skill Execution Contract §8):
  Conflict audit: [typed null "no cross-artifact contradictions found" or contradiction table]
  [Per contract §8: missing block != null -- declare the null if no contradictions found.]

For each observation:
  Condition 1: artifact date > STRATEGY DATE? [R-3 eligibility]
  Condition 2: absent from §1 Schema A? [R-2 dependency]
  CONFIRMED NEW = both YES. PRIOR-ONLY = C1 YES, C2 NO. Label: "PRIOR-ONLY -- not a delta."

Dimension Coverage Map:
  | Schema A D-N | Dimension | Signal coverage | Status |

Gate 4 (§7 -- reproduced from Skill Execution Contract §7):
  [PHASE 4 GATE: PASS/STOP -- condition: §8 declared (typed null or table) + delta labels applied]

══════════════════════════════════════════════════════════════
PHASE 5 -- Proposals  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 5: §5 PROPOSAL SCOPE, §5b NO CHANGE EVALUATION, §6 Proposals
    table, §7 Gate block.
  Active constraint rules for Phase 5 (per §CONSTRAINT SCOPE INDEX): R-0 (§5b evaluation
    then §6 per-row inertia test), R-1 (seal holds), R-2 (Before values from §1 Schema A
    only), R-3 (evidence dated after STRATEGY DATE), R-4 (reproductions double-anchored).
  No other §ID templates may be instantiated in this phase.

Reproduce §5 PROPOSAL SCOPE BLOCK (reproduced from Skill Execution Contract §5, per R-4):
  HIGH-PRESSURE NAMESPACES: [namespaces with new > 0; "none" if empty]
  Evidence restriction: Only HIGH-PRESSURE namespace artifacts may support proposals.
  SCOPE violation: A proposal row citing an excluded namespace is a SCOPE violation.
  [Per contract §5: missing block != null -- an absent §5 block means the scope filter
  was not applied.]

Scope Gate (§7 -- reproduced from Skill Execution Contract §7):
  [SCOPE GATE: PASS/STOP -- condition: §5 block present; violation condition line present]

Produce §5b NO CHANGE EVALUATION BLOCK (reproduced from Skill Execution Contract §5b, per R-4):
  NO CHANGE EVALUATION [R-0]:
  Status quo dimensions: [every §1 Schema A D-N label with current value]
  New signal pressure: [HIGH-PRESSURE namespaces with artifact counts; "none" if empty]
  Evaluation: [for each dimension under new signal pressure, state whether new signal
               evidence reveals a concrete consequence of NOT changing that dimension]
  Outcome: NO CHANGE HOLDS / PARTIAL CHANGE WARRANTED / FULL CHANGE WARRANTED
  [Per contract §5b: missing block != null -- an absent §5b block means the inertia
  evaluation was not run.]

Produce §6 PROPOSALS TABLE (reproduced from Skill Execution Contract §6, per R-4):
  Before values sourced from §1 Schema A -- not from strategy.md. [R-2 active]
  Evidence from HIGH-PRESSURE namespace artifacts only, dated after STRATEGY DATE. [R-3 active]
  Every proposal must name a concrete consequence of NOT changing to pass R-0. [R-0 active]

  | Action | Proposal | Before (from §1 Schema A [R-2]) | After |
    Evidence artifact [R-3] | Why this beats NO CHANGE [R-0] |

  [Per contract §6: a missing null row != no proposals for that type]
  ADD: none -- inertia holds [R-0].
  REMOVE: none -- inertia holds [R-0].
  REPRIORITIZE: none -- inertia holds [R-0].

Gate 5 (§7 -- reproduced from Skill Execution Contract §7):
  Check [5a]: Action column -- non-null for every row?
  Check [5b]: Proposal column -- non-null for every non-null action row?
  Check [5c]: Before column -- non-null; sourced from §1 Schema A [R-2]?
  Check [5d]: After column -- non-null for every non-null action row?
  Check [5e]: Evidence artifact column -- non-null for every non-null action row [R-3]?
  Check [5f]: Why this beats NO CHANGE column -- non-null for every non-null action row [R-0]?
  [PHASE 5 GATE: PASS/STOP -- condition: Action column [5a] + Proposal column [5b] +
  Before column [5c] + After column [5d] + Evidence artifact column [5e] +
  Why column [5f] all non-null across all non-null action rows]

══════════════════════════════════════════════════════════════
PHASE 6 -- Confirmation Gate  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 6: §7 Gate block (CONFIRMATION variant) only.
  Active constraint rules for Phase 6 (per §CONSTRAINT SCOPE INDEX): R-0 (inertia co-equal
    option), R-1 (seal holds until YES/REVISED).
  No other §ID templates may be instantiated in this phase.

Present the proposals table. Write:
"Proposed changes to strategy.md above. The default is NO CHANGE [R-0]. Apply?
Reply YES to proceed, NO to cancel, or REVISED with modifications."

Stop. Do not write to strategy.md. Halt here and wait for user reply.

══════════════════════════════════════════════════════════════
PHASE 7 -- Apply  (after YES or REVISED only)
══════════════════════════════════════════════════════════════

Apply confirmed proposals to strategy.md. Write only what was confirmed.
No unrequested additions.
```

---

## V-03: Phrasing Register -- Arithmetic in THRESHOLD, No Attestation (C-52 isolated, C-49 absent)

**Variation axis**: Phrasing register -- single axis. The inertia framing is elevated:
the opening declares NO CHANGE as the only hypothesis the skill is capable of falsifying,
borrowing hypothesis-test language. Gate-0 THRESHOLD absorbs the arithmetic (C-52:
"8 declared schemas + 3 structural checks = 11 items total; passes when all 11 items
confirmed; blocked by any single STOP result"). The condition line uses the grouped format
(C-50) but omits the self-containment attestation clause (C-49 absent -- no "reading this
condition line enumerates all N items required; no item may be inferred by range").
The labeled THRESHOLD field satisfies C-51. §5b is NOT a schema block (C-53 absent).

**Hypothesis**: V-01 confirmed C-52 on the R16 V-04 base (C-49+C-50+C-51 all present).
V-03 tests whether C-52 is independently satisfiable when C-49 is absent -- i.e., whether
the arithmetic-in-threshold form still satisfies C-52's "derivable by inspection" standard
without the attestation clause declaring the condition line's own completeness. If C-52
requires only that the arithmetic be inside the threshold field (not that the condition
line attest to its own completeness), V-03 should score C-52 without C-49. The phrasing
register change (hypothesis-test framing) is orthogonal and tests whether different
opening language produces any criterion interaction.

---

```
You are executing the topic-plan skill: revise the signal strategy as new information arrives.

NO CHANGE is the null hypothesis. Every proposal is an attempt to falsify it.
The null hypothesis stands unless a new signal artifact reveals a concrete consequence
of leaving the strategy unchanged -- and that consequence is worse than the cost of change.
A proposal that cannot name the consequence of inaction does not falsify the null.

══════════════════════════════════════════════════════════════
SKILL EXECUTION CONTRACT
══════════════════════════════════════════════════════════════

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
    Why this beats NO CHANGE [R-0]
    Action types: ADD / REMOVE / REPRIORITIZE.
    Null row: "[TYPE]: none -- inertia holds [R-0]."
    missing null row != no proposals -- a missing null row means the type was not evaluated.
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

PHASE AUTHORIZATION INDEX:
  Phase 1 -- §1 §2 §3 §7
  Phase 2 -- §4 §7
  Phase 3 -- §7 only
  Phase 4 -- §8 §7
  Phase 5 -- §5 §6 §7
  Phase 6 -- §7 (confirmation variant) only
  Phase 7 -- write to strategy.md (post-confirmation only)

CONSTRAINT RULES:
  R-0: Default outcome is NO CHANGE. Every proposal must prove that leaving the strategy
       unchanged produces a worse outcome than the proposed change. A proposal unable to
       name a concrete consequence of NOT changing fails R-0 and must be dropped.
  R-1: strategy.md sealed after §3. May not be re-read before user confirmation.
  R-2: Before values in §6 must trace to §1 Schema A rows at seal time. A Before value
       not in Schema A at seal time is a SEAL violation and must be dropped.
  R-3: Evidence restricted to artifacts dated after STRATEGY DATE. Evidence from prior
       artifacts is ineligible regardless of namespace.
  R-4: Enforcement reproductions cite both contract name and §ID (double-anchored attribution).

CONSTRAINT SCOPE INDEX:
  R-0: Phases 5-6 (active during proposal evaluation and confirmation framing)
  R-1: Phases 1-6 (active from §3 seal through Phase 6 confirmation)
  R-2: Phase 5 only (Before-value sourcing in §6 proposals table)
  R-3: Phases 4-5 (delta detection in Phase 4; proposal evidence in Phase 5)
  R-4: Phase 5 only (§5 PROPOSAL SCOPE and §6 reproductions)

PHASE SEQUENCE:
  Phase 1 (Commitment) -> Phase 2 (Inventory) -> Phase 3 (Gate) ->
  Phase 4 (Reading + Conflict Audit) -> Phase 5 (Proposals) ->
  Phase 6 (Confirmation -- halt) -> Phase 7 (Apply -- only after YES or REVISED)

══════════════════════════════════════════════════════════════
Gate-0 -- CONTRACT COMPLETENESS GATE
══════════════════════════════════════════════════════════════

Before Phase 1 begins, verify the SKILL EXECUTION CONTRACT above is complete.

  GATE-0 PASS THRESHOLD: 8 declared schemas + 3 structural checks = 11 items total;
  passes when all 11 items confirmed; blocked by any single STOP result.

  Schema checks -- one item per declared §ID:
  Check [A1]: §1 SCHEMA A -- columns D-N | Dimension label | Current value present,
              null behavior "no row may be omitted" present, phase authorization Phase 1?
  Check [A2]: §2 VERBATIM BLOCK -- delimiters present, Source dimension field present,
              Enforcement note field present, phase authorization Phase 1?
  Check [A3]: §3 SEALED BLOCK -- Schema A complete field present, VERBATIM BLOCK present
              field present, Temporal attestation present, Re-read prohibition [R-1] present,
              SEAL violation [R-2] present, phase authorization Phase 1?
  Check [A4]: §4 NAMESPACE INVENTORY TABLE -- columns namespace | total artifacts | new
              present, missing-row annotation present, phase authorization Phase 2?
  Check [A5]: §5 PROPOSAL SCOPE BLOCK -- HIGH-PRESSURE NAMESPACES field present, Evidence
              restriction present, SCOPE violation line present, missing-block annotation
              present, phase authorization Phase 5?
  Check [A6]: §6 PROPOSALS TABLE -- columns Action | Proposal | Before | After | Evidence
              artifact | Why present, null row format present, missing-null annotation present,
              phase authorization Phase 5?
  Check [A7]: §7 GATE BLOCK -- [PHASE N GATE: PASS/STOP] format present, compound [Na][Nb]
              labeling present, phase authorization "any gate phase" present?
  Check [A8]: §8 CONFLICT AUDIT BLOCK -- typed null or contradiction table format present,
              missing-block annotation present, phase authorization Phase 4?

  Structural checks:
  Check [B]: PHASE AUTHORIZATION INDEX present and populated?
    All 7 phases (Phase 1 through Phase 7) listed with their authorized §IDs.
  Check [C]: CONSTRAINT SCOPE INDEX present and populated?
    All R-N rules (R-0 through R-4) listed with their active phase ranges.
  Check [D]: Null annotations present on all typed-null-capable sections?
    §4 "missing row != absent namespace"
    §5 "missing block != null"
    §6 "missing null row != no proposals"
    §8 "missing block != null"

  Item count: 11 items ([A1][A2][A3][A4][A5][A6][A7][A8][B][C][D]) = 8 schemas + 3 structural.
  A missing §ID produces a detectable missing check item, not a silently failing compound condition.

  [GATE-0: PASS/STOP -- condition: schemas [A1][A2][A3][A4][A5][A6][A7][A8] all present +
  phase index [B] complete + constraint index [C] complete + null annotations [D] all present]

Phase 1 does not begin until Gate-0 passes.

══════════════════════════════════════════════════════════════
PHASE 1 -- Commitment  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 1: §1 Schema A, §2 VERBATIM BLOCK, §3 SEALED BLOCK, §7 Gate block.
  Active constraint rules for Phase 1 (per §CONSTRAINT SCOPE INDEX): R-1 activates at §3.
  No other §ID templates may be instantiated in this phase.

Open strategy.md. Extract last-modified date: STRATEGY DATE: [YYYY-MM-DD]. Close.
Re-open to read content. Fill §1 SCHEMA A. Close.

Fill §1 SCHEMA A (reproduced from Skill Execution Contract §1):
  | D-N | Dimension label | Current value |
  [all strategy dimensions -- per §1 null behavior: no row may be omitted]

Write §2 VERBATIM BLOCK (reproduced from Skill Execution Contract §2):
  ===VERBATIM BLOCK START===
  "[exact quoted sentence]"
  Source dimension: D-N -- [matching Schema A row]
  Enforcement note: A Source dimension field not matching a D-N label in Schema A
                    at seal time is a SEAL violation and fails this block.
  ===VERBATIM BLOCK END===

Write §3 SEALED BLOCK (reproduced from Skill Execution Contract §3) -- R-1 activates here:
  ===STRATEGY SEALED===
  Schema A: COMPLETE
  VERBATIM BLOCK: PRESENT -- D-N source, enforcement note labeled
  Temporal attestation: Commitment phase complete. No signal artifacts read yet.
  Re-read prohibition: strategy.md may not be re-opened until user applies changes. [R-1]
  SEAL violation: A Before value not in Schema A at seal time is a SEAL violation. [R-2]
  ===STRATEGY SEALED===

Gate 1 (§7 -- reproduced from Skill Execution Contract §7):
  Check [1]: §1 Schema A complete -- all D-N rows present?
  Check [2]:
    [2a] §2 VERBATIM BLOCK delimiters present?
    [2b] Source dimension in D-N format matching Schema A?
    [2c] Enforcement note present as labeled field?
  Check [3]: §3 SEALED BLOCK present with all fields including re-read prohibition [R-1]
             and SEAL violation definition [R-2]?
  [PHASE 1 GATE: PASS/STOP -- condition: §1 [1] + §2 [2a][2b][2c] + §3 [3]]

══════════════════════════════════════════════════════════════
PHASE 2 -- Signal Inventory  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 2: §4 Namespace inventory table, §7 Gate block.
  Active constraint rules for Phase 2 (per §CONSTRAINT SCOPE INDEX): R-1 (seal holds).
  No other §ID templates may be instantiated in this phase.

Locate all signal artifact files for the topic in simulations/.

Fill §4 NAMESPACE INVENTORY TABLE (reproduced from Skill Execution Contract §4):
  | namespace | total artifacts | new (date > STRATEGY DATE) |
  [all 9 namespace rows -- per contract §4: a missing row != 0|0; every namespace must appear]

HIGH-PRESSURE namespaces: those with new > 0.

Gate 2 (§7 -- reproduced from Skill Execution Contract §7):
  Check [2a]: namespace column -- all 9 values present and non-null
              (scout, draft, review, flow, trace, prove, listen, program, topic)?
  Check [2b]: total-artifacts column -- non-null for every row?
  Check [2c]: new(date > STRATEGY DATE) column -- non-null for every row?
  [PHASE 2 GATE: PASS/STOP -- condition: namespace column [2a] + total-artifacts column [2b] +
  new column [2c] all non-null across all 9 rows; no blank cells in mandatory columns]

══════════════════════════════════════════════════════════════
PHASE 3 -- Inventory Completeness Gate  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 3: §7 Gate block only.
  Active constraint rules for Phase 3 (per §CONSTRAINT SCOPE INDEX): R-1 (seal holds).
  No other §ID templates may be instantiated in this phase.

  Check [3a]: namespace column: all 9 names present -- scout, draft, review, flow, trace,
              prove, listen, program, topic -- each exactly once?
  Check [3b]: total-artifacts column: non-null for all 9 rows?
  Check [3c]: new column: non-null for all 9 rows?
  Check [3d]: HIGH-PRESSURE namespaces identified from rows where new > 0?
  [PHASE 3 GATE: PASS/STOP -- condition: §4 namespace column [3a] + total-artifacts column [3b] +
  new column [3c] all non-null across all rows; HIGH-PRESSURE namespaces identified [3d]]

══════════════════════════════════════════════════════════════
PHASE 4 -- Artifact Reading + Conflict Audit  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 4: §8 Conflict audit block, §7 Gate block.
  Active constraint rules for Phase 4 (per §CONSTRAINT SCOPE INDEX): R-1 (seal holds),
    R-3 (evidence restricted to artifacts dated after STRATEGY DATE).
  No other §ID templates may be instantiated in this phase.

Read every artifact classified new (date > STRATEGY DATE) in full. [R-3 active]

§8 CONFLICT AUDIT BLOCK (reproduced from Skill Execution Contract §8):
  Conflict audit: [typed null "no cross-artifact contradictions found" or contradiction table]
  [Per contract §8: missing block != null -- declare the null if no contradictions found.]

For each observation:
  Condition 1: artifact date > STRATEGY DATE? [R-3 eligibility]
  Condition 2: absent from §1 Schema A? [R-2 dependency]
  CONFIRMED NEW = both YES. PRIOR-ONLY = C1 YES, C2 NO. Label: "PRIOR-ONLY -- not a delta."

Dimension Coverage Map:
  | Schema A D-N | Dimension | Signal coverage | Status |

Gate 4 (§7 -- reproduced from Skill Execution Contract §7):
  [PHASE 4 GATE: PASS/STOP -- condition: §8 declared (typed null or table) + delta labels applied]

══════════════════════════════════════════════════════════════
PHASE 5 -- Proposals  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 5: §5 PROPOSAL SCOPE, §6 Proposals table, §7 Gate block.
  Active constraint rules for Phase 5 (per §CONSTRAINT SCOPE INDEX): R-0 (inertia test
    for each proposal), R-1 (seal holds), R-2 (Before values from §1 Schema A only),
    R-3 (evidence dated after STRATEGY DATE), R-4 (reproductions double-anchored).
  No other §ID templates may be instantiated in this phase.

Reproduce §5 PROPOSAL SCOPE BLOCK (reproduced from Skill Execution Contract §5, per R-4):
  HIGH-PRESSURE NAMESPACES: [namespaces with new > 0; "none" if empty]
  Evidence restriction: Only HIGH-PRESSURE namespace artifacts may support proposals.
  SCOPE violation: A proposal row citing an excluded namespace is a SCOPE violation.
  [Per contract §5: missing block != null -- an absent §5 block means the scope filter
  was not applied.]

Scope Gate (§7 -- reproduced from Skill Execution Contract §7):
  [SCOPE GATE: PASS/STOP -- condition: §5 block present; violation condition line present]

Produce §6 PROPOSALS TABLE (reproduced from Skill Execution Contract §6, per R-4):
  Before values sourced from §1 Schema A -- not from strategy.md. [R-2 active]
  Evidence from HIGH-PRESSURE namespace artifacts only, dated after STRATEGY DATE. [R-3 active]
  Every proposal must name a concrete consequence of NOT changing to pass R-0. [R-0 active]

  | Action | Proposal | Before (from §1 Schema A [R-2]) | After |
    Evidence artifact [R-3] | Why this beats NO CHANGE [R-0] |

  [Per contract §6: a missing null row != no proposals for that type]
  ADD: none -- inertia holds [R-0].
  REMOVE: none -- inertia holds [R-0].
  REPRIORITIZE: none -- inertia holds [R-0].

Gate 5 (§7 -- reproduced from Skill Execution Contract §7):
  Check [5a]: Action column -- non-null for every row?
  Check [5b]: Proposal column -- non-null for every non-null action row?
  Check [5c]: Before column -- non-null; sourced from §1 Schema A [R-2]?
  Check [5d]: After column -- non-null for every non-null action row?
  Check [5e]: Evidence artifact column -- non-null for every non-null action row [R-3]?
  Check [5f]: Why this beats NO CHANGE column -- non-null for every non-null action row [R-0]?
  [PHASE 5 GATE: PASS/STOP -- condition: Action column [5a] + Proposal column [5b] +
  Before column [5c] + After column [5d] + Evidence artifact column [5e] +
  Why column [5f] all non-null across all non-null action rows]

══════════════════════════════════════════════════════════════
PHASE 6 -- Confirmation Gate  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 6: §7 Gate block (CONFIRMATION variant) only.
  Active constraint rules for Phase 6 (per §CONSTRAINT SCOPE INDEX): R-0 (inertia co-equal
    option), R-1 (seal holds until YES/REVISED).
  No other §ID templates may be instantiated in this phase.

Present the proposals table. Write:
"Proposed changes to strategy.md above. The default is NO CHANGE [R-0]. Apply?
Reply YES to proceed, NO to cancel, or REVISED with modifications."

Stop. Do not write to strategy.md. Halt here and wait for user reply.

══════════════════════════════════════════════════════════════
PHASE 7 -- Apply  (after YES or REVISED only)
══════════════════════════════════════════════════════════════

Apply confirmed proposals to strategy.md. Write only what was confirmed.
No unrequested additions.
```

---

## V-04: Combined Output Format + Lifecycle -- C-52+C-53 Together

**Variation axis**: Combined output format + lifecycle emphasis. Gate-0 THRESHOLD absorbs
the arithmetic (C-52): "GATE-0 PASS THRESHOLD: 9 declared schemas + 3 structural checks =
12 items total; passes when all 12 items confirmed; blocked by any single STOP result."
§5b NO CHANGE EVALUATION BLOCK is declared as a named schema block [A6] in the contract
(C-53), shifting old [A6]-[A8] to [A7]-[A9] and raising the item count to 12. The
attestation clause (C-49), grouped condition line (C-50), and co-location in dedicated
labeled field (C-51) all carry forward from R16 V-04. The arithmetic is inside the
THRESHOLD field (not a separate labeled line). This is the first variation to satisfy
both C-52 and C-53 simultaneously.

**Hypothesis**: V-01 confirmed C-52 independently (arithmetic inside threshold, 8 schemas).
V-02 confirmed C-53 independently (§5b schema block, arithmetic outside threshold). V-04
tests whether the two criteria are simultaneously satisfiable when §5b is promoted to a
schema block AND the arithmetic is embedded inside the threshold field. The item count
change from 11 to 12 tests whether the grouped condition line scales correctly when a new
schema block is added: the arithmetic in the threshold must update from
"8 declared schemas + 3 structural checks = 11 items total" to
"9 declared schemas + 3 structural checks = 12 items total", confirming that the derivation
link between Phase -1 schema inventory and Gate-0 item count is auditable by inspection.

---

```
You are executing the topic-plan skill: revise the signal strategy as new information arrives.

The default outcome of this skill is NO CHANGE to strategy.md.
Every proposal carries the burden of proof against leaving the strategy unchanged.
NO CHANGE is not a fallback -- it is the named default option that proposals must
explicitly defeat, dimension by dimension, against new signal evidence.

══════════════════════════════════════════════════════════════
SKILL EXECUTION CONTRACT
══════════════════════════════════════════════════════════════

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

§5b NO CHANGE EVALUATION BLOCK TEMPLATE
    NO CHANGE EVALUATION [R-0]:
    Status quo dimensions: [every §1 Schema A D-N label with current value]
    New signal pressure: [HIGH-PRESSURE namespaces with artifact counts; "none" if empty]
    Evaluation: [for each dimension under new signal pressure, state whether new signal
                 evidence reveals a concrete consequence of NOT changing that dimension;
                 "no pressure" is a valid finding for dimensions with no coverage]
    Outcome: NO CHANGE HOLDS / PARTIAL CHANGE WARRANTED / FULL CHANGE WARRANTED
    Null behavior: if no HIGH-PRESSURE namespaces, write "Outcome: NO CHANGE HOLDS --
                   no new signals since strategy date."
    missing block != null -- a missing §5b block means the inertia evaluation was not run.
    Phase authorization: Phase 5 only (after §5 PROPOSAL SCOPE, before §6 PROPOSALS TABLE).

§6  PROPOSALS TABLE TEMPLATE
    Action | Proposal | Before (from §1 Schema A) | After | Evidence artifact |
    Why this beats NO CHANGE [R-0]
    Action types: ADD / REMOVE / REPRIORITIZE.
    Null row: "[TYPE]: none -- inertia holds [R-0]."
    missing null row != no proposals -- a missing null row means the type was not evaluated.
    Phase authorization: Phase 5 only (after §5b NO CHANGE EVALUATION).

§7  GATE BLOCK TEMPLATE
    [PHASE N GATE: PASS/STOP -- condition: ...]
    Compound gates use [Na][Nb][Nc] labels on sub-conditions.
    Phase authorization: any gate phase.

§8  CONFLICT AUDIT BLOCK TEMPLATE
    Conflict audit: [typed null "no cross-artifact contradictions found"
                     or contradiction table: Artifact A | Artifact B | Dimension | Contradiction]
    missing block != null -- a missing §8 block means the audit was not run.
    Phase authorization: Phase 4 only.

PHASE AUTHORIZATION INDEX:
  Phase 1 -- §1 §2 §3 §7
  Phase 2 -- §4 §7
  Phase 3 -- §7 only
  Phase 4 -- §8 §7
  Phase 5 -- §5 §5b §6 §7
  Phase 6 -- §7 (confirmation variant) only
  Phase 7 -- write to strategy.md (post-confirmation only)

CONSTRAINT RULES:
  R-0: Default outcome is NO CHANGE. Every proposal must prove that leaving the strategy
       unchanged produces a worse outcome than the proposed change. A proposal unable to
       name a concrete consequence of NOT changing fails R-0 and must be dropped.
       NO CHANGE is evaluated first as a named option in §5b before any proposals are
       generated; proposals must beat the §5b evaluation outcome for that dimension.
  R-1: strategy.md sealed after §3. May not be re-read before user confirmation.
  R-2: Before values in §6 must trace to §1 Schema A rows at seal time. A Before value
       not in Schema A at seal time is a SEAL violation and must be dropped.
  R-3: Evidence restricted to artifacts dated after STRATEGY DATE. Evidence from prior
       artifacts is ineligible regardless of namespace.
  R-4: Enforcement reproductions cite both contract name and §ID (double-anchored attribution).

CONSTRAINT SCOPE INDEX:
  R-0: Phases 5-6 (§5b evaluation, §6 proposal generation, and confirmation framing)
  R-1: Phases 1-6 (active from §3 seal through Phase 6 confirmation)
  R-2: Phase 5 only (Before-value sourcing in §6 proposals table)
  R-3: Phases 4-5 (delta detection in Phase 4; proposal evidence in Phase 5)
  R-4: Phase 5 only (§5, §5b, and §6 reproductions)

PHASE SEQUENCE:
  Phase 1 (Commitment) -> Phase 2 (Inventory) -> Phase 3 (Gate) ->
  Phase 4 (Reading + Conflict Audit) -> Phase 5 (Proposals) ->
  Phase 6 (Confirmation -- halt) -> Phase 7 (Apply -- only after YES or REVISED)

══════════════════════════════════════════════════════════════
Gate-0 -- CONTRACT COMPLETENESS GATE
══════════════════════════════════════════════════════════════

Before Phase 1 begins, verify the SKILL EXECUTION CONTRACT above is complete.

  GATE-0 PASS THRESHOLD: 9 declared schemas + 3 structural checks = 12 items total;
  passes when all 12 items confirmed; blocked by any single STOP result.

  Schema checks -- one item per declared §ID:
  Check [A1]: §1 SCHEMA A -- columns D-N | Dimension label | Current value present,
              null behavior "no row may be omitted" present, phase authorization Phase 1?
  Check [A2]: §2 VERBATIM BLOCK -- delimiters present, Source dimension field present,
              Enforcement note field present, phase authorization Phase 1?
  Check [A3]: §3 SEALED BLOCK -- Schema A complete field present, VERBATIM BLOCK present
              field present, Temporal attestation present, Re-read prohibition [R-1] present,
              SEAL violation [R-2] present, phase authorization Phase 1?
  Check [A4]: §4 NAMESPACE INVENTORY TABLE -- columns namespace | total artifacts | new
              present, missing-row annotation present, phase authorization Phase 2?
  Check [A5]: §5 PROPOSAL SCOPE BLOCK -- HIGH-PRESSURE NAMESPACES field present, Evidence
              restriction present, SCOPE violation line present, missing-block annotation
              present, phase authorization Phase 5?
  Check [A6]: §5b NO CHANGE EVALUATION BLOCK -- Status quo dimensions field present, New
              signal pressure field present, Evaluation field present, Outcome field present,
              null behavior for zero-pressure case present, missing-block annotation present,
              phase authorization Phase 5 (after §5, before §6)?
  Check [A7]: §6 PROPOSALS TABLE -- columns Action | Proposal | Before | After | Evidence
              artifact | Why present, null row format present, missing-null annotation present,
              phase authorization Phase 5 (after §5b)?
  Check [A8]: §7 GATE BLOCK -- [PHASE N GATE: PASS/STOP] format present, compound [Na][Nb]
              labeling present, phase authorization "any gate phase" present?
  Check [A9]: §8 CONFLICT AUDIT BLOCK -- typed null or contradiction table format present,
              missing-block annotation present, phase authorization Phase 4?

  Structural checks:
  Check [B]: PHASE AUTHORIZATION INDEX present and populated?
    All 7 phases listed with authorized §IDs.
    Phase 5 must list §5, §5b, §6, and §7.
  Check [C]: CONSTRAINT SCOPE INDEX present and populated?
    All R-N rules (R-0 through R-4) listed with active phase ranges.
    R-0 must reference §5b evaluation in its scope description.
  Check [D]: Null annotations present on all typed-null-capable sections?
    §4 "missing row != absent namespace"
    §5 "missing block != null"
    §5b "missing block != null"
    §6 "missing null row != no proposals"
    §8 "missing block != null"

  Item count: 12 items ([A1][A2][A3][A4][A5][A6][A7][A8][A9][B][C][D]) = 9 schemas + 3 structural.
  A missing §ID produces a detectable missing check item, not a silently failing compound condition.

  [GATE-0: PASS/STOP -- condition: schemas [A1][A2][A3][A4][A5][A6][A7][A8][A9] all present +
  phase index [B] complete + constraint index [C] complete + null annotations [D] all present;
  reading this condition line enumerates all 12 required items; no item may be inferred by range]

Phase 1 does not begin until Gate-0 passes.

══════════════════════════════════════════════════════════════
PHASE 1 -- Commitment  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 1: §1 Schema A, §2 VERBATIM BLOCK, §3 SEALED BLOCK, §7 Gate block.
  Active constraint rules for Phase 1 (per §CONSTRAINT SCOPE INDEX): R-1 activates at §3.
  No other §ID templates may be instantiated in this phase.

Open strategy.md. Extract last-modified date: STRATEGY DATE: [YYYY-MM-DD]. Close.
Re-open to read content. Fill §1 SCHEMA A. Close.

Fill §1 SCHEMA A (reproduced from Skill Execution Contract §1):
  | D-N | Dimension label | Current value |
  [all strategy dimensions -- per §1 null behavior: no row may be omitted]

Write §2 VERBATIM BLOCK (reproduced from Skill Execution Contract §2):
  ===VERBATIM BLOCK START===
  "[exact quoted sentence]"
  Source dimension: D-N -- [matching Schema A row]
  Enforcement note: A Source dimension field not matching a D-N label in Schema A
                    at seal time is a SEAL violation and fails this block.
  ===VERBATIM BLOCK END===

Write §3 SEALED BLOCK (reproduced from Skill Execution Contract §3) -- R-1 activates here:
  ===STRATEGY SEALED===
  Schema A: COMPLETE
  VERBATIM BLOCK: PRESENT -- D-N source, enforcement note labeled
  Temporal attestation: Commitment phase complete. No signal artifacts read yet.
  Re-read prohibition: strategy.md may not be re-opened until user applies changes. [R-1]
  SEAL violation: A Before value not in Schema A at seal time is a SEAL violation. [R-2]
  ===STRATEGY SEALED===

Gate 1 (§7 -- reproduced from Skill Execution Contract §7):
  Check [1]: §1 Schema A complete -- all D-N rows present?
  Check [2]:
    [2a] §2 VERBATIM BLOCK delimiters present?
    [2b] Source dimension in D-N format matching Schema A?
    [2c] Enforcement note present as labeled field?
  Check [3]: §3 SEALED BLOCK present with all fields including re-read prohibition [R-1]
             and SEAL violation definition [R-2]?
  [PHASE 1 GATE: PASS/STOP -- condition: §1 [1] + §2 [2a][2b][2c] + §3 [3]]

══════════════════════════════════════════════════════════════
PHASE 2 -- Signal Inventory  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 2: §4 Namespace inventory table, §7 Gate block.
  Active constraint rules for Phase 2 (per §CONSTRAINT SCOPE INDEX): R-1 (seal holds).
  No other §ID templates may be instantiated in this phase.

Locate all signal artifact files for the topic in simulations/.

Fill §4 NAMESPACE INVENTORY TABLE (reproduced from Skill Execution Contract §4):
  | namespace | total artifacts | new (date > STRATEGY DATE) |
  [all 9 namespace rows -- per contract §4: a missing row != 0|0; every namespace must appear]

HIGH-PRESSURE namespaces: those with new > 0.

Gate 2 (§7 -- reproduced from Skill Execution Contract §7):
  Check [2a]: namespace column -- all 9 values present and non-null
              (scout, draft, review, flow, trace, prove, listen, program, topic)?
  Check [2b]: total-artifacts column -- non-null for every row?
  Check [2c]: new(date > STRATEGY DATE) column -- non-null for every row?
  [PHASE 2 GATE: PASS/STOP -- condition: namespace column [2a] + total-artifacts column [2b] +
  new column [2c] all non-null across all 9 rows; no blank cells in mandatory columns]

══════════════════════════════════════════════════════════════
PHASE 3 -- Inventory Completeness Gate  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 3: §7 Gate block only.
  Active constraint rules for Phase 3 (per §CONSTRAINT SCOPE INDEX): R-1 (seal holds).
  No other §ID templates may be instantiated in this phase.

  Check [3a]: namespace column: all 9 names present -- scout, draft, review, flow, trace,
              prove, listen, program, topic -- each exactly once?
  Check [3b]: total-artifacts column: non-null for all 9 rows?
  Check [3c]: new column: non-null for all 9 rows?
  Check [3d]: HIGH-PRESSURE namespaces identified from rows where new > 0?
  [PHASE 3 GATE: PASS/STOP -- condition: §4 namespace column [3a] + total-artifacts column [3b] +
  new column [3c] all non-null across all rows; HIGH-PRESSURE namespaces identified [3d]]

══════════════════════════════════════════════════════════════
PHASE 4 -- Artifact Reading + Conflict Audit  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 4: §8 Conflict audit block, §7 Gate block.
  Active constraint rules for Phase 4 (per §CONSTRAINT SCOPE INDEX): R-1 (seal holds),
    R-3 (evidence restricted to artifacts dated after STRATEGY DATE).
  No other §ID templates may be instantiated in this phase.

Read every artifact classified new (date > STRATEGY DATE) in full. [R-3 active]

§8 CONFLICT AUDIT BLOCK (reproduced from Skill Execution Contract §8):
  Conflict audit: [typed null "no cross-artifact contradictions found" or contradiction table]
  [Per contract §8: missing block != null -- declare the null if no contradictions found.]

For each observation:
  Condition 1: artifact date > STRATEGY DATE? [R-3 eligibility]
  Condition 2: absent from §1 Schema A? [R-2 dependency]
  CONFIRMED NEW = both YES. PRIOR-ONLY = C1 YES, C2 NO. Label: "PRIOR-ONLY -- not a delta."

Dimension Coverage Map:
  | Schema A D-N | Dimension | Signal coverage | Status |

Gate 4 (§7 -- reproduced from Skill Execution Contract §7):
  [PHASE 4 GATE: PASS/STOP -- condition: §8 declared (typed null or table) + delta labels applied]

══════════════════════════════════════════════════════════════
PHASE 5 -- Proposals  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 5: §5 PROPOSAL SCOPE, §5b NO CHANGE EVALUATION, §6 Proposals
    table, §7 Gate block.
  Active constraint rules for Phase 5 (per §CONSTRAINT SCOPE INDEX): R-0 (§5b evaluation
    then §6 per-row inertia test), R-1 (seal holds), R-2 (Before values from §1 Schema A
    only), R-3 (evidence dated after STRATEGY DATE), R-4 (reproductions double-anchored).
  No other §ID templates may be instantiated in this phase.

Reproduce §5 PROPOSAL SCOPE BLOCK (reproduced from Skill Execution Contract §5, per R-4):
  HIGH-PRESSURE NAMESPACES: [namespaces with new > 0; "none" if empty]
  Evidence restriction: Only HIGH-PRESSURE namespace artifacts may support proposals.
  SCOPE violation: A proposal row citing an excluded namespace is a SCOPE violation.
  [Per contract §5: missing block != null -- an absent §5 block means the scope filter
  was not applied.]

Scope Gate (§7 -- reproduced from Skill Execution Contract §7):
  [SCOPE GATE: PASS/STOP -- condition: §5 block present; violation condition line present]

Produce §5b NO CHANGE EVALUATION BLOCK (reproduced from Skill Execution Contract §5b, per R-4):
  NO CHANGE EVALUATION [R-0]:
  Status quo dimensions: [every §1 Schema A D-N label with current value]
  New signal pressure: [HIGH-PRESSURE namespaces with artifact counts; "none" if empty]
  Evaluation: [for each dimension under new signal pressure, state whether new signal
               evidence reveals a concrete consequence of NOT changing that dimension]
  Outcome: NO CHANGE HOLDS / PARTIAL CHANGE WARRANTED / FULL CHANGE WARRANTED
  [Per contract §5b: missing block != null -- an absent §5b block means the inertia
  evaluation was not run.]

Produce §6 PROPOSALS TABLE (reproduced from Skill Execution Contract §6, per R-4):
  Before values sourced from §1 Schema A -- not from strategy.md. [R-2 active]
  Evidence from HIGH-PRESSURE namespace artifacts only, dated after STRATEGY DATE. [R-3 active]
  Every proposal must name a concrete consequence of NOT changing to pass R-0. [R-0 active]

  | Action | Proposal | Before (from §1 Schema A [R-2]) | After |
    Evidence artifact [R-3] | Why this beats NO CHANGE [R-0] |

  [Per contract §6: a missing null row != no proposals for that type]
  ADD: none -- inertia holds [R-0].
  REMOVE: none -- inertia holds [R-0].
  REPRIORITIZE: none -- inertia holds [R-0].

Gate 5 (§7 -- reproduced from Skill Execution Contract §7):
  Check [5a]: Action column -- non-null for every row?
  Check [5b]: Proposal column -- non-null for every non-null action row?
  Check [5c]: Before column -- non-null; sourced from §1 Schema A [R-2]?
  Check [5d]: After column -- non-null for every non-null action row?
  Check [5e]: Evidence artifact column -- non-null for every non-null action row [R-3]?
  Check [5f]: Why this beats NO CHANGE column -- non-null for every non-null action row [R-0]?
  [PHASE 5 GATE: PASS/STOP -- condition: Action column [5a] + Proposal column [5b] +
  Before column [5c] + After column [5d] + Evidence artifact column [5e] +
  Why column [5f] all non-null across all non-null action rows]

══════════════════════════════════════════════════════════════
PHASE 6 -- Confirmation Gate  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 6: §7 Gate block (CONFIRMATION variant) only.
  Active constraint rules for Phase 6 (per §CONSTRAINT SCOPE INDEX): R-0 (inertia co-equal
    option), R-1 (seal holds until YES/REVISED).
  No other §ID templates may be instantiated in this phase.

Present the proposals table. Write:
"Proposed changes to strategy.md above. The default is NO CHANGE [R-0]. Apply?
Reply YES to proceed, NO to cancel, or REVISED with modifications."

Stop. Do not write to strategy.md. Halt here and wait for user reply.

══════════════════════════════════════════════════════════════
PHASE 7 -- Apply  (after YES or REVISED only)
══════════════════════════════════════════════════════════════

Apply confirmed proposals to strategy.md. Write only what was confirmed.
No unrequested additions.
```

---

## V-05: Full Ceiling -- Combined All Axes (C-43--C-53)

**Variation axis**: Combined lifecycle emphasis + output format + role sequence. Gate-0
carries all R17 criteria: §5b as named schema block [A6] (C-53), arithmetic merged into
THRESHOLD field (C-52), grouped condition line (C-50), labeled THRESHOLD field (C-51),
self-containment attestation (C-49). The role sequence axis is added in Phase 5: §5b NO
CHANGE EVALUATION runs FIRST in Phase 5 -- before §5 PROPOSAL SCOPE -- so NO CHANGE is
evaluated against all new signal evidence before scope filtering narrows the evidence set.
The PHASE AUTHORIZATION INDEX lists Phase 5 as "§5b §5 §6 §7" (§5b first). The R-0
constraint scope note is updated: "§5b evaluated before §5 scope to ensure inertia is
assessed against all new evidence, not just HIGH-PRESSURE namespace evidence." C-43
(cell-exhaustive gate enumeration) is explicitly satisfied in Phase 2 and Phase 5 gates
by naming every mandatory column in the pass condition.

**Hypothesis**: V-04 confirmed C-52+C-53 together on the R16 V-04 base (C-49+C-50+C-51
preserved). V-05 tests the role sequence axis: running §5b before §5 changes when inertia
is evaluated (before scope vs. after scope). This tests whether role sequence interacts
with C-53 -- specifically, whether the §5b schema block declaration in the contract must
specify its phase-5 position relative to §5 to satisfy C-53's "independently auditable"
requirement. V-05 also confirms that all eleven R17 criteria (C-43-C-53) are simultaneously
satisfiable in a single coherent prompt.

---

```
You are executing the topic-plan skill: revise the signal strategy as new information arrives.

The default outcome of this skill is NO CHANGE to strategy.md.
Every proposal carries the burden of proof against leaving the strategy unchanged.
NO CHANGE is not a fallback -- it is the named default option that proposals must
explicitly defeat, dimension by dimension, against new signal evidence.
The inertia evaluation runs first, before scope filtering, to ensure the status quo
is tested against all new evidence -- not only the subset that survived the scope gate.

══════════════════════════════════════════════════════════════
SKILL EXECUTION CONTRACT
══════════════════════════════════════════════════════════════

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

§5b NO CHANGE EVALUATION BLOCK TEMPLATE
    NO CHANGE EVALUATION [R-0]:
    Status quo dimensions: [every §1 Schema A D-N label with current value]
    New signal pressure: [all new artifacts by namespace, regardless of HIGH-PRESSURE
                         classification; "none" if new = 0 across all namespaces]
    Evaluation: [for each dimension with any new signal coverage, state whether the
                 new signal evidence reveals a concrete consequence of NOT changing
                 that dimension; "no coverage" is a valid finding]
    Outcome: NO CHANGE HOLDS / PARTIAL CHANGE WARRANTED / FULL CHANGE WARRANTED
    Null behavior: if new = 0 across all namespaces, write "Outcome: NO CHANGE HOLDS --
                   no new signals since strategy date."
    missing block != null -- a missing §5b block means the inertia evaluation was not run.
    Phase authorization: Phase 5 only (before §5 PROPOSAL SCOPE and §6 PROPOSALS TABLE).

§5  PROPOSAL SCOPE BLOCK TEMPLATE
    HIGH-PRESSURE NAMESPACES: [namespaces with new > 0; "none" if list is empty]
    Evidence restriction: Only HIGH-PRESSURE namespace artifacts may support proposals.
    SCOPE violation: A proposal row citing an excluded namespace is a SCOPE violation.
    missing block != null -- a missing §5 block means the scope filter was not applied.
    Phase authorization: Phase 5 only (after §5b NO CHANGE EVALUATION).

§6  PROPOSALS TABLE TEMPLATE
    Action | Proposal | Before (from §1 Schema A) | After | Evidence artifact |
    Why this beats NO CHANGE [R-0]
    Action types: ADD / REMOVE / REPRIORITIZE.
    Null row: "[TYPE]: none -- inertia holds [R-0]."
    missing null row != no proposals -- a missing null row means the type was not evaluated.
    Phase authorization: Phase 5 only (after §5 PROPOSAL SCOPE).

§7  GATE BLOCK TEMPLATE
    [PHASE N GATE: PASS/STOP -- condition: ...]
    Compound gates use [Na][Nb][Nc] labels on sub-conditions.
    Phase authorization: any gate phase.

§8  CONFLICT AUDIT BLOCK TEMPLATE
    Conflict audit: [typed null "no cross-artifact contradictions found"
                     or contradiction table: Artifact A | Artifact B | Dimension | Contradiction]
    missing block != null -- a missing §8 block means the audit was not run.
    Phase authorization: Phase 4 only.

PHASE AUTHORIZATION INDEX:
  Phase 1 -- §1 §2 §3 §7
  Phase 2 -- §4 §7
  Phase 3 -- §7 only
  Phase 4 -- §8 §7
  Phase 5 -- §5b §5 §6 §7
  Phase 6 -- §7 (confirmation variant) only
  Phase 7 -- write to strategy.md (post-confirmation only)

CONSTRAINT RULES:
  R-0: Default outcome is NO CHANGE. Every proposal must prove that leaving the strategy
       unchanged produces a worse outcome than the proposed change. A proposal unable to
       name a concrete consequence of NOT changing fails R-0 and must be dropped.
       §5b evaluates NO CHANGE first -- before scope filtering -- against all new signals.
       §6 proposals must beat the §5b evaluation outcome for the relevant dimension.
  R-1: strategy.md sealed after §3. May not be re-read before user confirmation.
  R-2: Before values in §6 must trace to §1 Schema A rows at seal time. A Before value
       not in Schema A at seal time is a SEAL violation and must be dropped.
  R-3: Evidence restricted to artifacts dated after STRATEGY DATE. Evidence from prior
       artifacts is ineligible regardless of namespace.
  R-4: Enforcement reproductions cite both contract name and §ID (double-anchored attribution).

CONSTRAINT SCOPE INDEX:
  R-0: Phases 5-6 (§5b evaluated before §5 scope to ensure inertia is assessed against
       all new evidence, not just HIGH-PRESSURE namespace evidence; then §6 per-row test;
       then confirmation framing)
  R-1: Phases 1-6 (active from §3 seal through Phase 6 confirmation)
  R-2: Phase 5 only (Before-value sourcing in §6 proposals table)
  R-3: Phases 4-5 (delta detection in Phase 4; proposal evidence in Phase 5)
  R-4: Phase 5 only (§5b, §5, and §6 reproductions)

PHASE SEQUENCE:
  Phase 1 (Commitment) -> Phase 2 (Inventory) -> Phase 3 (Gate) ->
  Phase 4 (Reading + Conflict Audit) -> Phase 5 (Proposals) ->
  Phase 6 (Confirmation -- halt) -> Phase 7 (Apply -- only after YES or REVISED)

══════════════════════════════════════════════════════════════
Gate-0 -- CONTRACT COMPLETENESS GATE
══════════════════════════════════════════════════════════════

Before Phase 1 begins, verify the SKILL EXECUTION CONTRACT above is complete.

  GATE-0 PASS THRESHOLD: 9 declared schemas + 3 structural checks = 12 items total;
  passes when all 12 items confirmed; blocked by any single STOP result.

  Schema checks -- one item per declared §ID:
  Check [A1]: §1 SCHEMA A -- columns D-N | Dimension label | Current value present,
              null behavior "no row may be omitted" present, phase authorization Phase 1?
  Check [A2]: §2 VERBATIM BLOCK -- delimiters present, Source dimension field present,
              Enforcement note field present, phase authorization Phase 1?
  Check [A3]: §3 SEALED BLOCK -- Schema A complete field present, VERBATIM BLOCK present
              field present, Temporal attestation present, Re-read prohibition [R-1] present,
              SEAL violation [R-2] present, phase authorization Phase 1?
  Check [A4]: §4 NAMESPACE INVENTORY TABLE -- columns namespace | total artifacts | new
              present, missing-row annotation present, phase authorization Phase 2?
  Check [A5]: §5b NO CHANGE EVALUATION BLOCK -- Status quo dimensions field present, New
              signal pressure field (all new artifacts, pre-scope) present, Evaluation field
              present, Outcome field present, null behavior for zero-new case present,
              missing-block annotation present, phase authorization Phase 5 (before §5)?
  Check [A6]: §5 PROPOSAL SCOPE BLOCK -- HIGH-PRESSURE NAMESPACES field present, Evidence
              restriction present, SCOPE violation line present, missing-block annotation
              present, phase authorization Phase 5 (after §5b)?
  Check [A7]: §6 PROPOSALS TABLE -- columns Action | Proposal | Before | After | Evidence
              artifact | Why present, null row format present, missing-null annotation present,
              phase authorization Phase 5 (after §5)?
  Check [A8]: §7 GATE BLOCK -- [PHASE N GATE: PASS/STOP] format present, compound [Na][Nb]
              labeling present, phase authorization "any gate phase" present?
  Check [A9]: §8 CONFLICT AUDIT BLOCK -- typed null or contradiction table format present,
              missing-block annotation present, phase authorization Phase 4?

  Structural checks:
  Check [B]: PHASE AUTHORIZATION INDEX present and populated?
    All 7 phases listed with authorized §IDs.
    Phase 5 must list §5b, §5, §6, and §7 in that order (§5b before §5).
  Check [C]: CONSTRAINT SCOPE INDEX present and populated?
    All R-N rules (R-0 through R-4) listed with active phase ranges.
    R-0 must note that §5b evaluates before §5 scope.
  Check [D]: Null annotations present on all typed-null-capable sections?
    §4 "missing row != absent namespace"
    §5b "missing block != null"
    §5 "missing block != null"
    §6 "missing null row != no proposals"
    §8 "missing block != null"

  Item count: 12 items ([A1][A2][A3][A4][A5][A6][A7][A8][A9][B][C][D]) = 9 schemas + 3 structural.
  A missing §ID produces a detectable missing check item, not a silently failing compound condition.

  [GATE-0: PASS/STOP -- condition: schemas [A1][A2][A3][A4][A5][A6][A7][A8][A9] all present +
  phase index [B] complete + constraint index [C] complete + null annotations [D] all present;
  reading this condition line enumerates all 12 required items; no item may be inferred by range]

Phase 1 does not begin until Gate-0 passes.

══════════════════════════════════════════════════════════════
PHASE 1 -- Commitment  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 1: §1 Schema A, §2 VERBATIM BLOCK, §3 SEALED BLOCK, §7 Gate block.
  Active constraint rules for Phase 1 (per §CONSTRAINT SCOPE INDEX): R-1 activates at §3.
  No other §ID templates may be instantiated in this phase.

Open strategy.md. Extract last-modified date: STRATEGY DATE: [YYYY-MM-DD]. Close.
Re-open to read content. Fill §1 SCHEMA A. Close.

Fill §1 SCHEMA A (reproduced from Skill Execution Contract §1):
  | D-N | Dimension label | Current value |
  [all strategy dimensions -- per §1 null behavior: no row may be omitted]

Write §2 VERBATIM BLOCK (reproduced from Skill Execution Contract §2):
  ===VERBATIM BLOCK START===
  "[exact quoted sentence]"
  Source dimension: D-N -- [matching Schema A row]
  Enforcement note: A Source dimension field not matching a D-N label in Schema A
                    at seal time is a SEAL violation and fails this block.
  ===VERBATIM BLOCK END===

Write §3 SEALED BLOCK (reproduced from Skill Execution Contract §3) -- R-1 activates here:
  ===STRATEGY SEALED===
  Schema A: COMPLETE
  VERBATIM BLOCK: PRESENT -- D-N source, enforcement note labeled
  Temporal attestation: Commitment phase complete. No signal artifacts read yet.
  Re-read prohibition: strategy.md may not be re-opened until user applies changes. [R-1]
  SEAL violation: A Before value not in Schema A at seal time is a SEAL violation. [R-2]
  ===STRATEGY SEALED===

Gate 1 (§7 -- reproduced from Skill Execution Contract §7):
  Check [1]: §1 Schema A complete -- all D-N rows present?
  Check [2]:
    [2a] §2 VERBATIM BLOCK delimiters present?
    [2b] Source dimension in D-N format matching Schema A?
    [2c] Enforcement note present as labeled field?
  Check [3]: §3 SEALED BLOCK present with all fields including re-read prohibition [R-1]
             and SEAL violation definition [R-2]?
  [PHASE 1 GATE: PASS/STOP -- condition: §1 [1] + §2 [2a][2b][2c] + §3 [3]]

══════════════════════════════════════════════════════════════
PHASE 2 -- Signal Inventory  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 2: §4 Namespace inventory table, §7 Gate block.
  Active constraint rules for Phase 2 (per §CONSTRAINT SCOPE INDEX): R-1 (seal holds).
  No other §ID templates may be instantiated in this phase.

Locate all signal artifact files for the topic in simulations/.

Fill §4 NAMESPACE INVENTORY TABLE (reproduced from Skill Execution Contract §4):
  | namespace | total artifacts | new (date > STRATEGY DATE) |
  [all 9 namespace rows -- per contract §4: a missing row != 0|0; every namespace must appear]

HIGH-PRESSURE namespaces: those with new > 0.

Gate 2 (§7 -- reproduced from Skill Execution Contract §7):
  Check [2a]: namespace column -- all 9 values present and non-null
              (scout, draft, review, flow, trace, prove, listen, program, topic)?
  Check [2b]: total-artifacts column -- non-null for every row?
  Check [2c]: new(date > STRATEGY DATE) column -- non-null for every row?
  [PHASE 2 GATE: PASS/STOP -- condition: namespace column [2a] + total-artifacts column [2b] +
  new column [2c] all non-null across all 9 rows; no blank cells in mandatory columns]

══════════════════════════════════════════════════════════════
PHASE 3 -- Inventory Completeness Gate  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 3: §7 Gate block only.
  Active constraint rules for Phase 3 (per §CONSTRAINT SCOPE INDEX): R-1 (seal holds).
  No other §ID templates may be instantiated in this phase.

  Check [3a]: namespace column: all 9 names present -- scout, draft, review, flow, trace,
              prove, listen, program, topic -- each exactly once?
  Check [3b]: total-artifacts column: non-null for all 9 rows?
  Check [3c]: new column: non-null for all 9 rows?
  Check [3d]: HIGH-PRESSURE namespaces identified from rows where new > 0?
  [PHASE 3 GATE: PASS/STOP -- condition: §4 namespace column [3a] + total-artifacts column [3b] +
  new column [3c] all non-null across all rows; HIGH-PRESSURE namespaces identified [3d]]

══════════════════════════════════════════════════════════════
PHASE 4 -- Artifact Reading + Conflict Audit  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 4: §8 Conflict audit block, §7 Gate block.
  Active constraint rules for Phase 4 (per §CONSTRAINT SCOPE INDEX): R-1 (seal holds),
    R-3 (evidence restricted to artifacts dated after STRATEGY DATE).
  No other §ID templates may be instantiated in this phase.

Read every artifact classified new (date > STRATEGY DATE) in full. [R-3 active]

§8 CONFLICT AUDIT BLOCK (reproduced from Skill Execution Contract §8):
  Conflict audit: [typed null "no cross-artifact contradictions found" or contradiction table]
  [Per contract §8: missing block != null -- declare the null if no contradictions found.]

For each observation:
  Condition 1: artifact date > STRATEGY DATE? [R-3 eligibility]
  Condition 2: absent from §1 Schema A? [R-2 dependency]
  CONFIRMED NEW = both YES. PRIOR-ONLY = C1 YES, C2 NO. Label: "PRIOR-ONLY -- not a delta."

Dimension Coverage Map:
  | Schema A D-N | Dimension | Signal coverage | Status |

Gate 4 (§7 -- reproduced from Skill Execution Contract §7):
  [PHASE 4 GATE: PASS/STOP -- condition: §8 declared (typed null or table) + delta labels applied]

══════════════════════════════════════════════════════════════
PHASE 5 -- Proposals  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 5: §5b NO CHANGE EVALUATION (first), §5 PROPOSAL SCOPE
    (second), §6 Proposals table (third), §7 Gate block.
  Active constraint rules for Phase 5 (per §CONSTRAINT SCOPE INDEX): R-0 (§5b first,
    evaluated against all new evidence before scope filtering; then §6 per-row inertia
    test), R-1 (seal holds), R-2 (Before values from §1 Schema A only), R-3 (evidence
    dated after STRATEGY DATE), R-4 (reproductions double-anchored).
  No other §ID templates may be instantiated in this phase.

Produce §5b NO CHANGE EVALUATION BLOCK (reproduced from Skill Execution Contract §5b, per R-4):
  Evaluate against ALL new artifacts (date > STRATEGY DATE), regardless of namespace
  HIGH-PRESSURE classification. This runs before scope filtering. [R-0 active]
  NO CHANGE EVALUATION [R-0]:
  Status quo dimensions: [every §1 Schema A D-N label with current value]
  New signal pressure: [all new artifacts by namespace; "none" if new = 0 everywhere]
  Evaluation: [for each dimension with any new signal coverage, state whether new signal
               evidence reveals a concrete consequence of NOT changing that dimension]
  Outcome: NO CHANGE HOLDS / PARTIAL CHANGE WARRANTED / FULL CHANGE WARRANTED
  [Per contract §5b: missing block != null -- an absent §5b block means the inertia
  evaluation was not run.]

Inertia Gate (§7 -- reproduced from Skill Execution Contract §7):
  [INERTIA GATE: PASS/STOP -- condition: §5b block present; Outcome field non-null]

Reproduce §5 PROPOSAL SCOPE BLOCK (reproduced from Skill Execution Contract §5, per R-4):
  HIGH-PRESSURE NAMESPACES: [namespaces with new > 0; "none" if empty]
  Evidence restriction: Only HIGH-PRESSURE namespace artifacts may support proposals.
  SCOPE violation: A proposal row citing an excluded namespace is a SCOPE violation.
  [Per contract §5: missing block != null -- an absent §5 block means the scope filter
  was not applied.]

Scope Gate (§7 -- reproduced from Skill Execution Contract §7):
  [SCOPE GATE: PASS/STOP -- condition: §5 block present; violation condition line present]

Produce §6 PROPOSALS TABLE (reproduced from Skill Execution Contract §6, per R-4):
  Before values sourced from §1 Schema A -- not from strategy.md. [R-2 active]
  Evidence from HIGH-PRESSURE namespace artifacts only, dated after STRATEGY DATE. [R-3 active]
  Every proposal must name a concrete consequence of NOT changing to pass R-0. [R-0 active]

  | Action | Proposal | Before (from §1 Schema A [R-2]) | After |
    Evidence artifact [R-3] | Why this beats NO CHANGE [R-0] |

  [Per contract §6: a missing null row != no proposals for that type]
  ADD: none -- inertia holds [R-0].
  REMOVE: none -- inertia holds [R-0].
  REPRIORITIZE: none -- inertia holds [R-0].

Gate 5 (§7 -- reproduced from Skill Execution Contract §7):
  Check [5a]: Action column -- non-null for every row?
  Check [5b]: Proposal column -- non-null for every non-null action row?
  Check [5c]: Before column -- non-null; sourced from §1 Schema A [R-2]?
  Check [5d]: After column -- non-null for every non-null action row?
  Check [5e]: Evidence artifact column -- non-null for every non-null action row [R-3]?
  Check [5f]: Why this beats NO CHANGE column -- non-null for every non-null action row [R-0]?
  [PHASE 5 GATE: PASS/STOP -- condition: Action column [5a] + Proposal column [5b] +
  Before column [5c] + After column [5d] + Evidence artifact column [5e] +
  Why column [5f] all non-null across all non-null action rows]

══════════════════════════════════════════════════════════════
PHASE 6 -- Confirmation Gate  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 6: §7 Gate block (CONFIRMATION variant) only.
  Active constraint rules for Phase 6 (per §CONSTRAINT SCOPE INDEX): R-0 (inertia co-equal
    option), R-1 (seal holds until YES/REVISED).
  No other §ID templates may be instantiated in this phase.

Present the proposals table. Write:
"Proposed changes to strategy.md above. The default is NO CHANGE [R-0]. Apply?
Reply YES to proceed, NO to cancel, or REVISED with modifications."

Stop. Do not write to strategy.md. Halt here and wait for user reply.

══════════════════════════════════════════════════════════════
PHASE 7 -- Apply  (after YES or REVISED only)
══════════════════════════════════════════════════════════════

Apply confirmed proposals to strategy.md. Write only what was confirmed.
No unrequested additions.
```
