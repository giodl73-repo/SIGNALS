---
skill: quest-variate
skill_target: topic-plan
date: 2026-03-15
round: 13
rubric: topic-plan-rubric-v13-2026-03-15.md
new_criteria: [C-43, C-44, C-45]
prior_ceiling: R12
---

# topic-plan Skill Variations — Round 13 (2026-03-15)

Rubric: v13 (C-01–C-45, 37 aspirational, formula: essential×60 + recommended×30 + aspirational×10)
New criteria this round: C-43 (cell-exhaustive gate enumeration), C-44 (numbered Gate-0 label
in block header), C-45 (schema-gate checklist atomicity)

---

## Round 13 Design Notes

Round 12 variations (V-01, V-05) satisfied C-38, C-39, C-40, C-41 via CONTRACT COMPLETENESS
GATE with [A][B][C][D] checks, compound authorization gates, and R-N enforcement result
declarations. The three new v13 criteria were predicted by R12's gap analysis:

1. **C-44 from R12 all variations** — The CONTRACT COMPLETENESS GATE fires structurally before
   Phase 1 (satisfying C-26's pre-signal gate requirement) but carries only the label
   "CONTRACT COMPLETENESS GATE" as its section header — no numbered identifier. An auditor
   scanning section headers for "Gate-0" cannot locate the pre-signal gate without reading
   bodies. C-44 requires "Gate-0" (or equivalent numbered label) in the header so the gate is
   independently findable as chain-position-zero by header scan alone.

2. **C-43 from R12 Phase 2 gate** — The Phase 2 inventory gate passes when "all 9 namespace
   rows present; no namespace omitted." This is a ROW-PRESENCE gate, not a CELL-FILL gate. A
   row with namespace="scout", total=0, new=0 passes even if cells are wrong or blank. C-43
   requires each in-phase stop gate to enumerate every mandatory column by name so that a pass
   requires each named column to be non-null — rows existing is not sufficient.

3. **C-45 from R12 CONTRACT COMPLETENESS GATE Check [A]** — Check [A] groups all 8 §IDs into
   one compound item: "All §ID sections present? §1 Schema A, §2 Verbatim Block, ..." A missing
   §ID causes the compound to fail, but item count (4: [A][B][C][D]) does not equal schema
   count (8: §1–§8). An auditor cannot verify completeness by counting items. C-45 requires one
   check item per declared schema — item count must equal schema count.

**R12 gap analysis for R13:**

| Gap | Description | R13 axis |
|-----|-------------|----------|
| G-01 | CONTRACT COMPLETENESS GATE header carries no numbered identifier | V-01: Lifecycle emphasis — numbered Gate-0 label |
| G-02 | Phase 2 gate checks row presence only; columns not enumerated by name | V-02: Output format — cell-exhaustive column enumeration |
| G-03 | Schema gate check [A] groups all 8 §IDs into one compound item; item count != schema count | V-03: Output format B — per-§ID schema gate atomicity |
| G-04 | G-01 + G-02 co-present in all R12 variations | V-04: Combined lifecycle + output format A |
| G-05 | All three gaps present simultaneously; ceiling requires all three closed | V-05: Combined all three |

**Round 13 variation map:**

| Variation | Axis | Criteria targeted |
|-----------|------|-------------------|
| V-01 | Lifecycle emphasis — Gate-0 header only | C-44 |
| V-02 | Output format A — cell-exhaustive column gates | C-43 |
| V-03 | Output format B — per-§ID schema gate atomicity | C-45 |
| V-04 | Combined lifecycle + output A | C-44 + C-43 |
| V-05 | Combined all three axes | C-44 + C-43 + C-45 |

---

## V-01: Lifecycle Emphasis — Numbered Gate-0 Header

**Variation axis**: Lifecycle emphasis — the CONTRACT COMPLETENESS GATE section header is
renamed to carry "Gate-0" as its numbered chain identifier, making it independently scannable
as the first gate in the sequential gate chain without reading the gate body. The gate
condition label changes from "[CONTRACT GATE: ..." to "[GATE-0: ...". All other structure
is identical to R12 V-01.

**Hypothesis**: C-26 (pre-signal gate) is already satisfied — the CONTRACT COMPLETENESS GATE
fires before any artifact is read. C-44 adds a header-level requirement: "Gate-0" must appear
in the section header so an auditor scanning headers can confirm chain-position-zero without
reading body text. V-01 tests whether adding "Gate-0" to the header alone closes this gap.
Phase 2 gate remains row-presence only (C-43 not addressed); schema gate [A] remains grouped
(C-45 not addressed).

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

  Check [A]: All §ID sections present?
    §1 Schema A, §2 Verbatim Block, §3 Sealed Block, §4 Namespace Inventory,
    §5 Proposal Scope, §6 Proposals Table, §7 Gate Block, §8 Conflict Audit.
  Check [B]: PHASE AUTHORIZATION INDEX present and populated?
    All 7 phases (Phase 1 through Phase 7) listed with their authorized §IDs.
  Check [C]: CONSTRAINT SCOPE INDEX present and populated?
    All R-N rules (R-0 through R-4) listed with their active phase ranges.
  Check [D]: Null annotations present on all typed-null-capable sections?
    §4 "missing row != absent namespace"
    §5 "missing block != null"
    §6 "missing null row != no proposals"
    §8 "missing block != null"

  [GATE-0: PASS/STOP -- condition: [A] all §IDs present + [B] phase index complete +
  [C] constraint index complete + [D] all typed-null-capable §IDs annotated]

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
  [PHASE 2 GATE: PASS/STOP -- condition: all 9 namespace rows present; no namespace omitted]

══════════════════════════════════════════════════════════════
PHASE 3 -- Inventory Completeness Gate  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 3: §7 Gate block only.
  Active constraint rules for Phase 3 (per §CONSTRAINT SCOPE INDEX): R-1 (seal holds).
  No other §ID templates may be instantiated in this phase.

[PHASE 3 GATE: PASS/STOP -- condition: §4 complete; HIGH-PRESSURE namespaces identified]

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
  Check [1]: §5 PROPOSAL SCOPE reproduced (per R-4)?
  Check [2]: violation condition line present in reproduced §5?
  Check [3]: all action types declared (non-null rows and typed null rows per §6 format)?
  Check [4]: every non-null proposal row has "Why this beats NO CHANGE [R-0]" entry?
  [PHASE 5 GATE: PASS/STOP -- condition: §5 reproduced [1] + violation condition [2] +
  all types declared [3] + R-0 applied to all rows [4]]

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

## V-02: Output Format A — Cell-Exhaustive Column Enumeration in Gates

**Variation axis**: Output format — every in-phase stop gate that verifies a tabular §ID
section enumerates each mandatory column by name in its pass condition, requiring each named
column to be non-null before the phase may advance. Applied to Phase 2 gate (§4 inventory:
namespace, total-artifacts, new columns), Phase 3 gate (same §4 columns plus HIGH-PRESSURE
identification), and Phase 5 gate (§6 proposals: Action, Proposal, Before, After, Evidence
artifact, Why columns). Gate-0 header is NOT changed (C-44 not addressed).

**Hypothesis**: C-43 closes the gap left by C-12: a gate can satisfy "cell-fill intent" while
its actual pass condition checks only row presence. "All 9 namespace rows present" passes when
a row exists with any cell content. V-02 rewrites the Phase 2 gate condition to name namespace
column, total-artifacts column, and new column individually — so a row with any blank mandatory
cell cannot satisfy the condition. Same pattern applied to Phase 3 and Phase 5 gates for their
respective §IDs. Schema gate [A] remains grouped (C-45 not addressed by this axis).

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
CONTRACT COMPLETENESS GATE
══════════════════════════════════════════════════════════════

Before Phase 1 begins, verify the SKILL EXECUTION CONTRACT above is complete.

  Check [A]: All §ID sections present?
    §1 Schema A, §2 Verbatim Block, §3 Sealed Block, §4 Namespace Inventory,
    §5 Proposal Scope, §6 Proposals Table, §7 Gate Block, §8 Conflict Audit.
  Check [B]: PHASE AUTHORIZATION INDEX present and populated?
    All 7 phases (Phase 1 through Phase 7) listed with their authorized §IDs.
  Check [C]: CONSTRAINT SCOPE INDEX present and populated?
    All R-N rules (R-0 through R-4) listed with their active phase ranges.
  Check [D]: Null annotations present on all typed-null-capable sections?
    §4 "missing row != absent namespace"
    §5 "missing block != null"
    §6 "missing null row != no proposals"
    §8 "missing block != null"

  [CONTRACT GATE: PASS/STOP -- condition: [A] all §IDs present + [B] phase index complete +
  [C] constraint index complete + [D] all typed-null-capable §IDs annotated]

Phase 1 does not begin until this gate passes.

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
  Check [2b]: total-artifacts column -- non-null for every row
              (0 is a valid value; blank or missing is not)?
  Check [2c]: new(date > STRATEGY DATE) column -- non-null for every row
              (0 is a valid value; blank or missing is not)?
  A row with any blank cell in columns [2a][2b][2c] does not count as a checked namespace.
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
  Check [5a]: Action column -- non-null for every row
              (ADD/REMOVE/REPRIORITIZE or typed null "none -- inertia holds [R-0]")?
  Check [5b]: Proposal column -- non-null for every non-null action row?
  Check [5c]: Before column -- non-null for every non-null action row; sourced from §1 Schema A [R-2]?
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

## V-03: Output Format B — Per-§ID Schema Gate Atomicity

**Variation axis**: Output format — the CONTRACT COMPLETENESS GATE check [A] is restructured
from one compound item listing all 8 §IDs into eight individually labeled check items
[A1]–[A8], one per declared schema. Each item names the §ID and its mandatory fields. The
gate now has 11 independently verifiable items (8 schema checks + [B] + [C] + [D]), making
completeness verifiable by count: 11 items present means all schemas checked. Gate-0 header
NOT added (C-44 not addressed). Phase 2 gate remains row-presence only (C-43 not addressed).

**Hypothesis**: C-45 requires the schema gate to have one item per declared schema so that a
missing schema produces a detectable missing check item rather than a silently incomplete
compound condition. R12's [A] check cannot be audited by count — there is one item for 8
schemas. V-03 tests whether splitting [A] into [A1]–[A8] satisfies C-45 independently, without
the Gate-0 header change or cell-exhaustive inventory gate.

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
CONTRACT COMPLETENESS GATE
══════════════════════════════════════════════════════════════

Before Phase 1 begins, verify the SKILL EXECUTION CONTRACT above is complete.
8 declared schemas + 3 structural checks = 11 items total. Gate passes when all 11 confirmed.

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
  Missing §ID produces a detectable missing check item, not a silently failing compound condition.

  [CONTRACT GATE: PASS/STOP -- condition: schemas [A1][A2][A3][A4][A5][A6][A7][A8] all present +
  phase index [B] complete + constraint index [C] complete + null annotations [D] all present]

Phase 1 does not begin until this gate passes.

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
  [PHASE 2 GATE: PASS/STOP -- condition: all 9 namespace rows present; no namespace omitted]

══════════════════════════════════════════════════════════════
PHASE 3 -- Inventory Completeness Gate  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 3: §7 Gate block only.
  Active constraint rules for Phase 3 (per §CONSTRAINT SCOPE INDEX): R-1 (seal holds).
  No other §ID templates may be instantiated in this phase.

[PHASE 3 GATE: PASS/STOP -- condition: §4 complete; HIGH-PRESSURE namespaces identified]

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
  Check [1]: §5 PROPOSAL SCOPE reproduced (per R-4)?
  Check [2]: violation condition line present in reproduced §5?
  Check [3]: all action types declared (non-null rows and typed null rows per §6 format)?
  Check [4]: every non-null proposal row has "Why this beats NO CHANGE [R-0]" entry?
  [PHASE 5 GATE: PASS/STOP -- condition: §5 reproduced [1] + violation condition [2] +
  all types declared [3] + R-0 applied to all rows [4]]

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

## V-04: Combined — Numbered Gate-0 Header + Cell-Exhaustive Inventory Gates

**Variation axis**: Combined lifecycle emphasis + output format A — carries V-01's numbered
"Gate-0" section header and V-02's cell-exhaustive column enumeration in Phase 2, Phase 3,
and Phase 5 gates. Schema gate check [A] remains grouped (C-45 not addressed by this combination).

**Hypothesis**: C-44 and C-43 address orthogonal properties: C-44 is a header-level property
(not gate body), C-43 is a gate-condition property (body, not header). Combining them produces
no interference. V-04 tests the combined floor: all R12-satisfied criteria plus the two most
structurally distinct new criteria, isolating C-45 for V-05.

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

  Check [A]: All §ID sections present?
    §1 Schema A, §2 Verbatim Block, §3 Sealed Block, §4 Namespace Inventory,
    §5 Proposal Scope, §6 Proposals Table, §7 Gate Block, §8 Conflict Audit.
  Check [B]: PHASE AUTHORIZATION INDEX present and populated?
    All 7 phases (Phase 1 through Phase 7) listed with their authorized §IDs.
  Check [C]: CONSTRAINT SCOPE INDEX present and populated?
    All R-N rules (R-0 through R-4) listed with their active phase ranges.
  Check [D]: Null annotations present on all typed-null-capable sections?
    §4 "missing row != absent namespace"
    §5 "missing block != null"
    §6 "missing null row != no proposals"
    §8 "missing block != null"

  [GATE-0: PASS/STOP -- condition: [A] all §IDs present + [B] phase index complete +
  [C] constraint index complete + [D] all typed-null-capable §IDs annotated]

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
  Check [2b]: total-artifacts column -- non-null for every row
              (0 is a valid value; blank or missing is not)?
  Check [2c]: new(date > STRATEGY DATE) column -- non-null for every row
              (0 is a valid value; blank or missing is not)?
  A row with any blank cell in columns [2a][2b][2c] does not count as a checked namespace.
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
  Check [5a]: Action column -- non-null for every row
              (ADD/REMOVE/REPRIORITIZE or typed null "none -- inertia holds [R-0]")?
  Check [5b]: Proposal column -- non-null for every non-null action row?
  Check [5c]: Before column -- non-null for every non-null action row; sourced from §1 Schema A [R-2]?
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

## V-05: Combined — Gate-0 Header + Cell-Exhaustive Gates + Per-§ID Schema Atomicity

**Variation axis**: Combined all three axes — carries V-01's numbered Gate-0 section header
(C-44), V-02's cell-exhaustive column enumeration in Phase 2, Phase 3, and Phase 5 gates
(C-43), and V-03's per-§ID schema gate atomicity with [A1]–[A8] individual checks (C-45).
Ceiling variation: all R12-satisfied criteria plus all three new v13 criteria simultaneously.

**Hypothesis**: C-44, C-43, and C-45 address three distinct structural properties — header
scannability, gate-condition cell coverage, and schema-gate item count — that do not interfere
with each other. All three can be added additively. V-05 predicts no degradation on earlier
criteria while closing all three new gaps.

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
8 declared schemas + 3 structural checks = 11 items. Gate-0 passes when all 11 confirmed.

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
  A missing §ID produces a detectable missing item; completeness verifiable by count.

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
  Check [2b]: total-artifacts column -- non-null for every row
              (0 is a valid value; blank or missing is not)?
  Check [2c]: new(date > STRATEGY DATE) column -- non-null for every row
              (0 is a valid value; blank or missing is not)?
  A row with any blank cell in columns [2a][2b][2c] does not count as a checked namespace.
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
  Check [5a]: Action column -- non-null for every row
              (ADD/REMOVE/REPRIORITIZE or typed null "none -- inertia holds [R-0]")?
  Check [5b]: Proposal column -- non-null for every non-null action row?
  Check [5c]: Before column -- non-null for every non-null action row; sourced from §1 Schema A [R-2]?
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

## Criteria Coverage Map

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 strategy.md cited | pass | pass | pass | pass | pass |
| C-02 all 9 namespaces assessed | pass | pass | pass | pass | pass |
| C-03 delta / NEW-PRIOR split | pass | pass | pass | pass | pass |
| C-04 typed change proposals | pass | pass | pass | pass | pass |
| C-05 confirmation gate | pass | pass | pass | pass | pass |
| C-06 evidence citation | pass | pass | pass | pass | pass |
| C-07 before/after diff | pass | pass | pass | pass | pass |
| C-08 inertia justification | pass | pass | pass | pass | pass |
| C-26 pre-signal gate | pass | pass | pass | pass | pass |
| C-38 schema-phase gate in chain | pass | pass | pass | pass | pass |
| C-43 cell-exhaustive gate enumeration | FAIL | PASS | FAIL | PASS | PASS |
| C-44 numbered Gate-0 label in header | PASS | FAIL | FAIL | PASS | PASS |
| C-45 schema-gate checklist atomicity | FAIL | FAIL | PASS | FAIL | PASS |

**Single-axis isolation:**
- V-01 passes exactly C-44 of the three new criteria
- V-02 passes exactly C-43 of the three new criteria
- V-03 passes exactly C-45 of the three new criteria
- V-04 passes C-44 + C-43 (V-01 axis + V-02 axis)
- V-05 passes all three: C-43 + C-44 + C-45
