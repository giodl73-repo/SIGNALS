---
skill: quest-variate
skill_target: topic-plan
date: 2026-03-15
round: 12
rubric: topic-plan-rubric-v12-2026-03-15.md
new_criteria: [C-39, C-40, C-41]
prior_ceiling: 120
new_ceiling: 123
---

# topic-plan Skill Variations — Round 12 (2026-03-15)

Rubric: v12 (C-01–C-41, /33 aspirational, max composite 123)
New criteria this round: C-39 (constraint scope index in contract), C-40 (per-phase active
R-N rules in authorization header), C-41 ("missing block != null" extended to all
typed-null-capable sections)

---

## Round 12 Design Notes

Round 11 reached ceiling 120 on variations saturating C-36, C-37, C-38. The three new v12
criteria were all predicted by R11's gap analysis:

1. **C-39 from R11 V-02** — V-02 introduced a CONSTRAINT SCOPE INDEX in the contract mapping
   each R-N rule to its active phases, symmetric to C-35's PHASE AUTHORIZATION INDEX. C-39
   formalizes this: the contract must include this index for per-phase constraint conformance
   to be verifiable by inspection alone.

2. **C-40 from R11 V-02 + V-05** — Authorization headers in R11 V-02 and V-05 included not
   just authorized §IDs but also "Active constraint rules for Phase N (per §CONSTRAINT SCOPE
   INDEX): R-N". C-40 formalizes: each phase's authorization header must name its active R-N
   rules, completing the dual-axis authorization check (§IDs + R-N rules).

3. **C-41 from R11 V-03 + V-05** — V-03 extended "missing block != null" from §8 alone to §4,
   §5, §6, §8. C-41 formalizes: all typed-null-capable sections must carry the
   absence-is-not-null annotation.

**R12 baseline**: R11 V-05 satisfies C-01 through C-41. All R12 variations inherit this
complete contract structure. New axes explore structural patterns beyond the current ceiling.

**R11 gap analysis for R12:**

| Gap | Description | R12 axis |
|-----|-------------|----------|
| G-01 | SKILL EXECUTION CONTRACT pre-declares all elements but its own completeness is never verified — a contract missing §IDs or indexes would begin Phase 1 undetected | V-01: Contract completeness pre-gate |
| G-02 | Authorization check declares §IDs and R-N rules but as separate prose lines — C-36+C-40 compliance is not a named compound gate with labeled sub-conditions | V-02: Compound authorization gate with [1a][1b] identifiers |
| G-03 | R-N identifiers appear in authorization headers and at enforcement points inline, but enforcement RESULTS are not declared — R-N is cited, not reported | V-03: R-N enforcement result declarations at application points |
| G-04 | Null rows in §6 say "inertia holds [R-0]" but R-0 requires proving worse outcome from NOT changing; the evaluation record is absent — inertia is asserted but not documented | V-04: R-0 evaluation documentation in typed-null rows |

**Round 12 single-axis choices:**

| Variation | Axis | Primary mechanism |
|-----------|------|-------------------|
| V-01 | Lifecycle emphasis | CONTRACT COMPLETENESS GATE before Phase 1 verifies contract structure |
| V-02 | Output format | Authorization check at each phase entry is a compound gate with [1a][1b] sub-conditions |
| V-03 | Phrasing register | R-N enforcement results declared "[R-N APPLIED/VIOLATION]" at each application point |
| V-04 | Inertia framing | Null rows include "R-0 evaluation: [consequence evaluated and found insufficient]" |
| V-05 | Combined | V-01 pre-gate + V-02 compound auth + V-03 R-N results + V-04 R-0 documentation |

---

## V-01: Lifecycle Emphasis — Contract Completeness Pre-Gate

**Variation axis**: Lifecycle emphasis — before Phase 1 begins, a named CONTRACT COMPLETENESS
GATE verifies that the SKILL EXECUTION CONTRACT is structurally complete: all eight §ID
sections present, both indexes populated (PHASE AUTHORIZATION INDEX and CONSTRAINT SCOPE
INDEX), and all typed-null-capable sections annotated. Phase 1 does not open until this
gate passes.

**Hypothesis**: C-30 requires the contract to pre-declare all templates and rules. C-39 requires
the CONSTRAINT SCOPE INDEX. C-41 requires null annotations on all four typed-null-capable
sections. But none of these criteria require the contract's own completeness to be VERIFIED
before execution begins. A pre-Phase-1 gate that checks four structural conditions ([A] §IDs,
[B] phase index, [C] constraint index, [D] null annotations) creates a new criterion: contract-
level completeness verification distinct from per-phase authorization checks (C-36/C-40). This
mirrors the relationship between declaring a gate condition (C-14) and actually enforcing it
(C-11) — the contract declares requirements; this gate enforces them.

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
    Source dimension: D-N — [label matching a Schema A row]
    Enforcement note: A Source dimension field not matching a D-N label in Schema A
                      at seal time is a SEAL violation and fails this block.
    ===VERBATIM BLOCK END===
    Phase authorization: Phase 1 only.

§3  SEALED BLOCK TEMPLATE
    ===STRATEGY SEALED===
    Schema A: COMPLETE
    VERBATIM BLOCK: PRESENT — D-N source, enforcement note labeled
    Temporal attestation: Commitment phase complete. No signal artifacts read yet.
    Re-read prohibition: strategy.md may not be re-opened until user applies changes. [R-1]
    SEAL violation: A Before value not in Schema A at seal time is a SEAL violation. [R-2]
    ===STRATEGY SEALED===
    Phase authorization: Phase 1 only.

§4  NAMESPACE INVENTORY TABLE TEMPLATE
    namespace | total artifacts | new (date > STRATEGY DATE)
    All 9 namespaces listed. Absent: 0 total | 0 new.
    missing row != absent namespace — a missing row means the namespace was not checked.
    Phase authorization: Phase 2 only.

§5  PROPOSAL SCOPE BLOCK TEMPLATE
    HIGH-PRESSURE NAMESPACES: [namespaces with new > 0; "none" if list is empty]
    Evidence restriction: Only HIGH-PRESSURE namespace artifacts may support proposals.
    SCOPE violation: A proposal row citing an excluded namespace is a SCOPE violation.
    missing block != null — a missing §5 block means the scope filter was not applied.
    Phase authorization: Phase 5 only.

§6  PROPOSALS TABLE TEMPLATE
    Action | Proposal | Before (from §1 Schema A) | After | Evidence artifact |
    Why this beats NO CHANGE [R-0]
    Action types: ADD / REMOVE / REPRIORITIZE.
    Null row: "[TYPE]: none — inertia holds [R-0]."
    missing null row != no proposals — a missing null row means the type was not evaluated.
    Phase authorization: Phase 5 only.

§7  GATE BLOCK TEMPLATE
    [PHASE N GATE: PASS/STOP — condition: ...]
    Compound gates use [Na][Nb][Nc] labels on sub-conditions.
    Phase authorization: any gate phase.

§8  CONFLICT AUDIT BLOCK TEMPLATE
    Conflict audit: [typed null "no cross-artifact contradictions found"
                     or contradiction table: Artifact A | Artifact B | Dimension | Contradiction]
    missing block != null — a missing §8 block means the audit was not run.
    Phase authorization: Phase 4 only.

PHASE AUTHORIZATION INDEX:
  Phase 1 — §1 §2 §3 §7
  Phase 2 — §4 §7
  Phase 3 — §7 only
  Phase 4 — §8 §7
  Phase 5 — §5 §6 §7
  Phase 6 — §7 (confirmation variant) only
  Phase 7 — write to strategy.md (post-confirmation only)

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
  Authorized §IDs for Phase 6: §7 Gate block (CONFIRMATION GATE variant) only.
  Active constraint rules for Phase 6 (per §CONSTRAINT SCOPE INDEX): R-0 (inertia is
    a co-equal option at confirmation), R-1 (seal holds until YES/REVISED).
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

## V-02: Output Format — Compound Authorization Gate at Phase Entry

**Variation axis**: Output format — each phase's authorization check is restructured as a
compound gate with two labeled sub-conditions: [1a] for authorized §IDs (per PHASE
AUTHORIZATION INDEX) and [1b] for active R-N rules (per CONSTRAINT SCOPE INDEX), followed
by a named AUTHORIZATION GATE with a PASS/STOP result. C-36 and C-40 are currently two
separate prose lines in the authorization block; V-02 makes them a single named compound gate
whose sub-conditions are independently addressable.

**Hypothesis**: C-36 requires each phase to list its authorized §IDs. C-40 requires each
phase to list its active R-N rules. Both currently appear as separate prose lines under one
"Authorization check" header, but neither is a named gate with a PASS/STOP result. Making
the dual-axis check a compound gate with [1a][1b] identifier labels creates a new structural
element: "authorization header as named compound gate." This parallels C-29 (gate sub-
requirements use identifier labels) but at the authorization level rather than the gate-check
level. A phase authorization block that lists §IDs and R-N rules (satisfying C-36+C-40) but
does not structure them as a named compound gate with PASS/STOP might fail this new criterion.

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
PHASE 1 -- Commitment  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract):
  [1a] Authorized §IDs (per §PHASE AUTHORIZATION INDEX):
       §1 Schema A, §2 VERBATIM BLOCK, §3 SEALED BLOCK, §7 Gate block.
  [1b] Active constraint rules (per §CONSTRAINT SCOPE INDEX):
       R-1 activates at §3 seal point.
  [AUTHORIZATION GATE: PASS/STOP -- condition: [1a] §IDs verified against PHASE
  AUTHORIZATION INDEX + [1b] R-N rules verified against CONSTRAINT SCOPE INDEX]
  No §IDs or rules beyond those declared above may be applied in this phase.

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

Authorization check (per Skill Execution Contract):
  [1a] Authorized §IDs (per §PHASE AUTHORIZATION INDEX):
       §4 Namespace inventory table, §7 Gate block.
  [1b] Active constraint rules (per §CONSTRAINT SCOPE INDEX):
       R-1 (seal holds throughout this phase).
  [AUTHORIZATION GATE: PASS/STOP -- condition: [1a] §IDs verified against PHASE
  AUTHORIZATION INDEX + [1b] R-N rules verified against CONSTRAINT SCOPE INDEX]
  No §IDs or rules beyond those declared above may be applied in this phase.

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

Authorization check (per Skill Execution Contract):
  [1a] Authorized §IDs (per §PHASE AUTHORIZATION INDEX): §7 Gate block only.
  [1b] Active constraint rules (per §CONSTRAINT SCOPE INDEX): R-1 (seal holds).
  [AUTHORIZATION GATE: PASS/STOP -- condition: [1a] §IDs verified + [1b] R-N rules verified]
  No §IDs or rules beyond those declared above may be applied in this phase.

[PHASE 3 GATE: PASS/STOP -- condition: §4 complete; HIGH-PRESSURE namespaces identified]

══════════════════════════════════════════════════════════════
PHASE 4 -- Artifact Reading + Conflict Audit  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract):
  [1a] Authorized §IDs (per §PHASE AUTHORIZATION INDEX):
       §8 Conflict audit block, §7 Gate block.
  [1b] Active constraint rules (per §CONSTRAINT SCOPE INDEX):
       R-1 (seal holds), R-3 (evidence restricted to artifacts dated after STRATEGY DATE).
  [AUTHORIZATION GATE: PASS/STOP -- condition: [1a] §IDs verified against PHASE
  AUTHORIZATION INDEX + [1b] R-N rules verified against CONSTRAINT SCOPE INDEX]
  No §IDs or rules beyond those declared above may be applied in this phase.

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

Authorization check (per Skill Execution Contract):
  [1a] Authorized §IDs (per §PHASE AUTHORIZATION INDEX):
       §5 PROPOSAL SCOPE, §6 Proposals table, §7 Gate block.
  [1b] Active constraint rules (per §CONSTRAINT SCOPE INDEX):
       R-0 (inertia test for each proposal), R-1 (seal holds), R-2 (Before values from §1
       Schema A only), R-3 (evidence dated after STRATEGY DATE), R-4 (reproductions
       double-anchored).
  [AUTHORIZATION GATE: PASS/STOP -- condition: [1a] §IDs verified against PHASE
  AUTHORIZATION INDEX + [1b] R-N rules verified against CONSTRAINT SCOPE INDEX]
  No §IDs or rules beyond those declared above may be applied in this phase.

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

Authorization check (per Skill Execution Contract):
  [1a] Authorized §IDs (per §PHASE AUTHORIZATION INDEX): §7 Gate block (CONFIRMATION variant).
  [1b] Active constraint rules (per §CONSTRAINT SCOPE INDEX): R-0 (inertia co-equal option),
       R-1 (seal holds until YES/REVISED).
  [AUTHORIZATION GATE: PASS/STOP -- condition: [1a] §IDs verified + [1b] R-N rules verified]
  No §IDs or rules beyond those declared above may be applied in this phase.

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

## V-03: Phrasing Register — R-N Enforcement Result Declarations

**Variation axis**: Phrasing register — at each point where a constraint rule is applied,
the enforcement produces an explicit declarative result statement "[R-N APPLIED: ...]"
naming the rule, the enforcement action, and what a violation would look like. R-N
identifiers are currently cited inline (e.g., "[R-1]" at the seal point) but no result is
declared. V-03 makes each enforcement event a structured output with a named result.

**Hypothesis**: C-37 requires R-N identifiers on constraint rules. C-40 requires each phase
to name active R-N rules in its authorization header. Neither criterion requires enforcement
RESULTS to be declared at the point of application. A "[R-1 APPLIED: strategy.md sealed --
re-read from this point onward is a violation]" declaration at §3 creates an enforcement event
record that is independently auditable without tracing the phase authorization header. This
may reveal a new criterion: "R-N enforcement event declaration" -- the rule cited, applied,
and its outcome stated at the application point, not just at the authorization header level.
This closes the chain from declaration (contract R-N) to authorization (phase header) to
application (enforcement point), making each step independently auditable.

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

Write §3 SEALED BLOCK (reproduced from Skill Execution Contract §3):
  ===STRATEGY SEALED===
  Schema A: COMPLETE
  VERBATIM BLOCK: PRESENT -- D-N source, enforcement note labeled
  Temporal attestation: Commitment phase complete. No signal artifacts read yet.
  Re-read prohibition: strategy.md may not be re-opened until user applies changes. [R-1]
  SEAL violation: A Before value not in Schema A at seal time is a SEAL violation. [R-2]
  ===STRATEGY SEALED===
  [R-1 APPLIED: strategy.md is now sealed -- any re-read of strategy.md before user
  confirmation at Phase 6 is a violation of R-1. R-2 is now active: Before values
  in §6 must trace to the Schema A rows above, not to strategy.md.]

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

Read every artifact classified new (date > STRATEGY DATE) in full.
  [R-3 APPLIED: reading only artifacts with date > STRATEGY DATE -- any artifact dated on or
  before STRATEGY DATE is ineligible evidence regardless of namespace. Per §CONSTRAINT SCOPE
  INDEX, R-3 is active in Phases 4 and 5.]

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

Reproduce §5 PROPOSAL SCOPE BLOCK (reproduced from Skill Execution Contract §5):
  HIGH-PRESSURE NAMESPACES: [namespaces with new > 0; "none" if empty]
  Evidence restriction: Only HIGH-PRESSURE namespace artifacts may support proposals.
  SCOPE violation: A proposal row citing an excluded namespace is a SCOPE violation.
  [Per contract §5: missing block != null -- an absent §5 block means the scope filter
  was not applied.]
  [R-4 APPLIED: §5 reproduced from Skill Execution Contract §5 -- contract name and §ID cited.
  Any reproduction lacking both contract name and §ID reference fails R-4.]

Scope Gate (§7 -- reproduced from Skill Execution Contract §7):
  [SCOPE GATE: PASS/STOP -- condition: §5 block present; violation condition line present]

Produce §6 PROPOSALS TABLE (reproduced from Skill Execution Contract §6):
  [R-2 APPLIED: Before values must trace to §1 Schema A rows sealed in Phase 1 -- any
  Before value containing text not present in Schema A at seal time is a SEAL violation
  and must be dropped. Per §CONSTRAINT SCOPE INDEX, R-2 is active in Phase 5 only.]
  Evidence from HIGH-PRESSURE namespace artifacts only, dated after STRATEGY DATE.
  [R-3 APPLIED: evidence restricted to artifacts dated after STRATEGY DATE -- per R-3
  active in Phase 5. Any artifact dated on or before STRATEGY DATE is ineligible.]

  | Action | Proposal | Before (from §1 Schema A [R-2]) | After |
    Evidence artifact [R-3] | Why this beats NO CHANGE [R-0] |

  [Per contract §6: a missing null row != no proposals for that type]
  ADD: none -- inertia holds [R-0].
  REMOVE: none -- inertia holds [R-0].
  REPRIORITIZE: none -- inertia holds [R-0].

Gate 5 (§7 -- reproduced from Skill Execution Contract §7):
  Check [1]: §5 PROPOSAL SCOPE reproduced with R-4 attribution?
  Check [2]: violation condition line present in reproduced §5?
  Check [3]: all action types declared (non-null rows and typed null rows per §6 format)?
  Check [4]: every non-null proposal row has "Why this beats NO CHANGE [R-0]" entry?
  [PHASE 5 GATE: PASS/STOP -- condition: §5 reproduced [1] + violation condition [2] +
  all types declared [3] + R-0 applied to all rows [4]]

══════════════════════════════════════════════════════════════
PHASE 6 -- Confirmation Gate  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 6: §7 Gate block (CONFIRMATION GATE variant) only.
  Active constraint rules for Phase 6 (per §CONSTRAINT SCOPE INDEX): R-0 (inertia is
    a co-equal option at confirmation), R-1 (seal holds until YES/REVISED).
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

## V-04: Inertia Framing — R-0 Evaluation Documentation in Typed-Null Rows

**Variation axis**: Inertia framing — null rows in the §6 proposals table include an explicit
"R-0 evaluation" field that documents the specific consequence examined and found insufficient
to warrant change. Currently null rows say "inertia holds [R-0]" which states the outcome but
not the evaluation. V-04 requires each null row to name what was assessed and why it failed
to meet R-0's burden-of-proof threshold.

**Hypothesis**: C-08 requires inertia justification for non-null proposals. C-09 requires typed
null declarations for action types with no proposals. R-0 requires proving that NOT changing
produces a worse outcome. Currently null rows satisfy C-09 format requirements (typed label,
inertia holds [R-0]) but do not document the evaluation behind the null claim. An "R-0
evaluation: [consequence examined and found insufficient]" field in each null row extends the
inertia obligation from non-null proposals (C-08) to null declarations: the absence of a
proposal is as much a decision as its presence, and the reasoning behind it should be
traceable. This might reveal a new criterion: "R-0 evaluation trace in null rows" -- parallel
to C-06 (evidence citation for non-null proposals) applied to the null case.

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
    Null row: "[TYPE]: none -- inertia holds [R-0]. R-0 evaluation: [consequence examined
              and found insufficient to warrant change]."
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

  [Per contract §6: a missing null row != no proposals for that type. Each null row must
  include R-0 evaluation documenting the consequence examined and found insufficient.]

  ADD: none -- inertia holds [R-0].
    R-0 evaluation: no new dimension identified in HIGH-PRESSURE artifacts whose absence
    from strategy produces a demonstrably worse outcome than current coverage.
  REMOVE: none -- inertia holds [R-0].
    R-0 evaluation: no dimension in current strategy found without NEW artifact support
    where removal would produce better outcomes than retention.
  REPRIORITIZE: none -- inertia holds [R-0].
    R-0 evaluation: no NEW artifact evidence found for an ordering that produces better
    sequencing outcomes than current priority structure.

Gate 5 (§7 -- reproduced from Skill Execution Contract §7):
  Check [1]: §5 PROPOSAL SCOPE reproduced (per R-4)?
  Check [2]: violation condition line present in reproduced §5?
  Check [3]: all action types declared (non-null rows and typed null rows per §6 format)?
  Check [4]: every non-null proposal row has "Why this beats NO CHANGE [R-0]" entry?
  Check [5]: every null row has "R-0 evaluation" field documenting consequence examined?
  [PHASE 5 GATE: PASS/STOP -- condition: §5 reproduced [1] + violation condition [2] +
  all types declared [3] + R-0 applied to all rows [4] + R-0 evaluation on null rows [5]]

══════════════════════════════════════════════════════════════
PHASE 6 -- Confirmation Gate  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX):
  Authorized §IDs for Phase 6: §7 Gate block (CONFIRMATION GATE variant) only.
  Active constraint rules for Phase 6 (per §CONSTRAINT SCOPE INDEX): R-0 (inertia is
    a co-equal option at confirmation), R-1 (seal holds until YES/REVISED).
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

## V-05: Combined -- Contract Pre-Gate + Compound Authorization + R-N Results + R-0 Documentation

**Variation axes combined**: Lifecycle emphasis (V-01 contract completeness pre-gate),
output format (V-02 compound authorization gate with [1a][1b]), phrasing register (V-03
R-N enforcement result declarations), inertia framing (V-04 R-0 evaluation in null rows).

**Hypothesis**: The four single-axis innovations are structurally non-conflicting and additive:
the contract pre-gate (V-01) operates before Phase 1; the compound authorization gate (V-02)
changes the authorization check format at each phase entry; R-N enforcement results (V-03)
add declarations at application points within phases; R-0 evaluation (V-04) changes the null
row format in §6. Combining all four creates the maximum-coverage variation for R12. This also
tests whether the combination surfaces new structural patterns visible only when all four axes
are simultaneously active -- a V-05 "combination criterion" effect observed in R11.

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
    Null row: "[TYPE]: none -- inertia holds [R-0]. R-0 evaluation: [consequence examined
              and found insufficient to warrant change]."
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
CONTRACT COMPLETENESS GATE  [V-01 axis]
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

Authorization check (per Skill Execution Contract):  [V-02 axis]
  [1a] Authorized §IDs (per §PHASE AUTHORIZATION INDEX):
       §1 Schema A, §2 VERBATIM BLOCK, §3 SEALED BLOCK, §7 Gate block.
  [1b] Active constraint rules (per §CONSTRAINT SCOPE INDEX):
       R-1 activates at §3 seal point.
  [AUTHORIZATION GATE: PASS/STOP -- condition: [1a] §IDs verified against PHASE
  AUTHORIZATION INDEX + [1b] R-N rules verified against CONSTRAINT SCOPE INDEX]
  No §IDs or rules beyond those declared above may be applied in this phase.

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

Write §3 SEALED BLOCK (reproduced from Skill Execution Contract §3):
  ===STRATEGY SEALED===
  Schema A: COMPLETE
  VERBATIM BLOCK: PRESENT -- D-N source, enforcement note labeled
  Temporal attestation: Commitment phase complete. No signal artifacts read yet.
  Re-read prohibition: strategy.md may not be re-opened until user applies changes. [R-1]
  SEAL violation: A Before value not in Schema A at seal time is a SEAL violation. [R-2]
  ===STRATEGY SEALED===
  [R-1 APPLIED: strategy.md is now sealed -- any re-read before user confirmation is a
  violation of R-1. R-2 activates: Before values in §6 must trace to Schema A above.]  [V-03 axis]

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

Authorization check (per Skill Execution Contract):  [V-02 axis]
  [1a] Authorized §IDs (per §PHASE AUTHORIZATION INDEX):
       §4 Namespace inventory table, §7 Gate block.
  [1b] Active constraint rules (per §CONSTRAINT SCOPE INDEX):
       R-1 (seal holds throughout this phase).
  [AUTHORIZATION GATE: PASS/STOP -- condition: [1a] §IDs verified against PHASE
  AUTHORIZATION INDEX + [1b] R-N rules verified against CONSTRAINT SCOPE INDEX]
  No §IDs or rules beyond those declared above may be applied in this phase.

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

Authorization check (per Skill Execution Contract):  [V-02 axis]
  [1a] Authorized §IDs (per §PHASE AUTHORIZATION INDEX): §7 Gate block only.
  [1b] Active constraint rules (per §CONSTRAINT SCOPE INDEX): R-1 (seal holds).
  [AUTHORIZATION GATE: PASS/STOP -- condition: [1a] §IDs verified + [1b] R-N rules verified]
  No §IDs or rules beyond those declared above may be applied in this phase.

[PHASE 3 GATE: PASS/STOP -- condition: §4 complete; HIGH-PRESSURE namespaces identified]

══════════════════════════════════════════════════════════════
PHASE 4 -- Artifact Reading + Conflict Audit  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract):  [V-02 axis]
  [1a] Authorized §IDs (per §PHASE AUTHORIZATION INDEX):
       §8 Conflict audit block, §7 Gate block.
  [1b] Active constraint rules (per §CONSTRAINT SCOPE INDEX):
       R-1 (seal holds), R-3 (evidence restricted to artifacts dated after STRATEGY DATE).
  [AUTHORIZATION GATE: PASS/STOP -- condition: [1a] §IDs verified against PHASE
  AUTHORIZATION INDEX + [1b] R-N rules verified against CONSTRAINT SCOPE INDEX]
  No §IDs or rules beyond those declared above may be applied in this phase.

Read every artifact classified new (date > STRATEGY DATE) in full.
  [R-3 APPLIED: reading only artifacts with date > STRATEGY DATE -- any artifact dated on or
  before STRATEGY DATE is ineligible evidence. Per §CONSTRAINT SCOPE INDEX, R-3 is active
  in Phases 4 and 5.]  [V-03 axis]

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

Authorization check (per Skill Execution Contract):  [V-02 axis]
  [1a] Authorized §IDs (per §PHASE AUTHORIZATION INDEX):
       §5 PROPOSAL SCOPE, §6 Proposals table, §7 Gate block.
  [1b] Active constraint rules (per §CONSTRAINT SCOPE INDEX):
       R-0 (inertia test for each proposal), R-1 (seal holds), R-2 (Before values from §1
       Schema A only), R-3 (evidence dated after STRATEGY DATE), R-4 (reproductions
       double-anchored).
  [AUTHORIZATION GATE: PASS/STOP -- condition: [1a] §IDs verified against PHASE
  AUTHORIZATION INDEX + [1b] R-N rules verified against CONSTRAINT SCOPE INDEX]
  No §IDs or rules beyond those declared above may be applied in this phase.

Reproduce §5 PROPOSAL SCOPE BLOCK (reproduced from Skill Execution Contract §5):
  HIGH-PRESSURE NAMESPACES: [namespaces with new > 0; "none" if empty]
  Evidence restriction: Only HIGH-PRESSURE namespace artifacts may support proposals.
  SCOPE violation: A proposal row citing an excluded namespace is a SCOPE violation.
  [Per contract §5: missing block != null -- an absent §5 block means the scope filter
  was not applied.]
  [R-4 APPLIED: §5 reproduced from Skill Execution Contract §5 -- contract name and §ID
  cited. Any reproduction lacking both contract name and §ID reference fails R-4.]  [V-03 axis]

Scope Gate (§7 -- reproduced from Skill Execution Contract §7):
  [SCOPE GATE: PASS/STOP -- condition: §5 block present; violation condition line present]

Produce §6 PROPOSALS TABLE (reproduced from Skill Execution Contract §6):
  [R-2 APPLIED: Before values must trace to §1 Schema A sealed in Phase 1 -- any Before
  value not present in Schema A at seal time is a SEAL violation and must be dropped.
  Per §CONSTRAINT SCOPE INDEX, R-2 is active in Phase 5 only.]  [V-03 axis]
  Evidence from HIGH-PRESSURE namespace artifacts only, dated after STRATEGY DATE.
  [R-3 APPLIED: evidence restricted to artifacts dated after STRATEGY DATE -- artifacts
  dated on or before STRATEGY DATE are ineligible. Per §CONSTRAINT SCOPE INDEX, R-3 active
  in Phase 5.]  [V-03 axis]

  | Action | Proposal | Before (from §1 Schema A [R-2]) | After |
    Evidence artifact [R-3] | Why this beats NO CHANGE [R-0] |

  [Per contract §6: a missing null row != no proposals for that type. Each null row must
  include R-0 evaluation documenting the consequence examined and found insufficient.]

  ADD: none -- inertia holds [R-0].
    R-0 evaluation: no new dimension identified in HIGH-PRESSURE artifacts whose absence
    from strategy produces a demonstrably worse outcome than current coverage.  [V-04 axis]
  REMOVE: none -- inertia holds [R-0].
    R-0 evaluation: no dimension in current strategy found without NEW artifact support
    where removal would produce better outcomes than retention.  [V-04 axis]
  REPRIORITIZE: none -- inertia holds [R-0].
    R-0 evaluation: no NEW artifact evidence found for an ordering that produces better
    sequencing outcomes than current priority structure.  [V-04 axis]

Gate 5 (§7 -- reproduced from Skill Execution Contract §7):
  Check [1]: §5 PROPOSAL SCOPE reproduced with R-4 attribution?
  Check [2]: violation condition line present in reproduced §5?
  Check [3]: all action types declared (non-null rows and typed null rows per §6 format)?
  Check [4]: every non-null proposal row has "Why this beats NO CHANGE [R-0]" entry?
  Check [5]: every null row has "R-0 evaluation" field documenting consequence examined?
  [PHASE 5 GATE: PASS/STOP -- condition: §5 reproduced [1] + violation condition [2] +
  all types declared [3] + R-0 applied to all rows [4] + R-0 evaluation on null rows [5]]

══════════════════════════════════════════════════════════════
PHASE 6 -- Confirmation Gate  [per Skill Execution Contract]
══════════════════════════════════════════════════════════════

Authorization check (per Skill Execution Contract):  [V-02 axis]
  [1a] Authorized §IDs (per §PHASE AUTHORIZATION INDEX): §7 Gate block (CONFIRMATION variant).
  [1b] Active constraint rules (per §CONSTRAINT SCOPE INDEX): R-0 (inertia co-equal option),
       R-1 (seal holds until YES/REVISED).
  [AUTHORIZATION GATE: PASS/STOP -- condition: [1a] §IDs verified + [1b] R-N rules verified]
  No §IDs or rules beyond those declared above may be applied in this phase.

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

## Discrimination Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-39: CONSTRAINT SCOPE INDEX in contract | YES (baseline) | YES (baseline) | YES (baseline) | YES (baseline) | YES (baseline) |
| C-40: Per-phase active R-N rules in auth header | YES (baseline) | YES (compound gate form) | YES (baseline) | YES (baseline) | YES (compound gate form) |
| C-41: "missing block != null" on all 4 typed-null sections | YES (baseline) | YES (baseline) | YES (baseline) | YES (baseline + §6 null row format) | YES (baseline + §6 null row format) |
| G-01: Contract completeness pre-gate | YES (named CONTRACT GATE) | NO | NO | NO | YES (named CONTRACT GATE) |
| G-02: Authorization check as compound gate with [1a][1b] | NO | YES ([1a][1b] + AUTHORIZATION GATE) | NO | NO | YES ([1a][1b] + AUTHORIZATION GATE) |
| G-03: R-N enforcement result declarations at application points | NO | NO | YES ([R-N APPLIED: ...]) | NO | YES ([R-N APPLIED: ...]) |
| G-04: R-0 evaluation documentation in null rows | NO | NO | NO | YES (R-0 evaluation field) | YES (R-0 evaluation field) |
| Prior criteria (C-01 to C-38) | preserved | preserved | preserved | preserved | preserved |

**Expected ceiling crackers**: V-05 targets all four new axes; V-01 targets G-01 alone with
the strongest gate structure; V-02 targets G-02 with the most explicit compound gate labeling;
V-03 targets G-03 with inline enforcement result declarations; V-04 targets G-04 with the
most fully specified R-0 evaluation trace.

**Most likely to surface new criteria**: V-02 (compound authorization gate is structurally
symmetric to C-29's compound gate sub-requirements -- if [Na][Nb] on gate checks produced
C-29, then [1a][1b] on authorization checks may produce an analogous criterion) and V-04
(R-0 evaluation in null rows is structurally symmetric to C-06's evidence citation in non-null
rows -- the null case and non-null case would then be equally documented).

---

## Predicted Scores (v12 rubric, ceiling 123)

All five variations satisfy C-01 through C-41 by design (baseline from R11 V-05).

| Variation | New axis satisfied | Ceiling risk | Predicted composite |
|-----------|-------------------|--------------|---------------------|
| V-01 | G-01 contract pre-gate | none | 123 |
| V-02 | G-02 compound auth gate | none | 123 |
| V-03 | G-03 R-N enforcement results | none | 123 |
| V-04 | G-04 R-0 evaluation trace | none | 123 |
| V-05 | G-01 + G-02 + G-03 + G-04 | none | 123 |

All five are expected to reach the v12 ceiling. Discriminating criteria for R13 will emerge
from scoring which new axes produce the clearest structural patterns independent of existing
criteria -- primary candidates being G-02 (compound authorization gate, structurally
analogous to C-29) and G-04 (R-0 evaluation in null rows, structurally analogous to C-06).

```json
{
  "round": 12,
  "rubric_version": "v12",
  "ceiling": 123,
  "new_criteria": ["C-39", "C-40", "C-41"],
  "predicted_top_score": 123,
  "predicted_all_essential_pass": true,
  "predicted_discriminators_round_13": [
    "Contract completeness pre-gate: does a named gate before Phase 1 verify the SKILL EXECUTION CONTRACT has all §IDs, both indexes, and all null annotations?",
    "Compound authorization gate with labeled sub-conditions: does each phase's authorization check use [1a][1b] identifier labels for the §ID check and R-N check, structured as a named AUTHORIZATION GATE with PASS/STOP?",
    "R-N enforcement event declaration: at each point where a constraint rule is applied, is there an explicit '[R-N APPLIED: ...]' declaration stating the rule, the action taken, and what a violation would look like?",
    "R-0 evaluation documentation in null rows: do typed-null rows in §6 include an 'R-0 evaluation' field naming the specific consequence examined and found insufficient to warrant change?"
  ]
}
```
