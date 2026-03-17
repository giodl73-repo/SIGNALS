---
skill: quest-variate
skill_target: topic-plan
date: 2026-03-15
round: 14
rubric: topic-plan-rubric-v14-2026-03-15.md
new_criteria: [C-46, C-47]
prior_ceiling: R13
---

# topic-plan Skill Variations — Round 14 (2026-03-15)

Rubric: v14 (C-01–C-47, 39 aspirational, formula: essential×60 + recommended×30 + aspirational×10)
New criteria this round: C-46 (schema-gate pass-threshold annotation), C-47 (gate-pass condition
exhaustive item cross-reference)

---

## Round 14 Design Notes

Round 13 V-05 satisfied C-43 (cell-exhaustive column gates), C-44 (numbered Gate-0 header),
and C-45 (per-§ID schema atomicity). The two new v14 criteria were predicted by observing what
V-05 has that V-03 lacks in the Gate-0 annotation and condition line:

1. **C-46 from R13 V-03 annotation gap** — V-03's arithmetic annotation reads "8 declared
   schemas + 3 structural checks = 11 items total" and "Gate passes when all 11 confirmed."
   C-46 requires the annotation to name the gate by label — "Gate passes" is a generic reference;
   "Gate-0 passes" names the specific gate. An annotation naming the item count without naming
   the gate cannot be verified as belonging to this gate without reading the gate header.

2. **C-47 from R13 V-03 condition line gap** — V-03's condition reads `[CONTRACT GATE:
   PASS/STOP -- condition: schemas [A1][A2][A3][A4][A5][A6][A7][A8] all present + phase index
   [B] complete + constraint index [C] complete + null annotations [D] all present]`. The gate
   prefix `[CONTRACT GATE:]` is an unnamed label — an auditor reading only the condition line
   cannot confirm this is Gate-0 (chain-position-zero) without scanning the surrounding section
   header. C-47 requires the condition line to be fully self-contained: an auditor reading only
   the PASS/STOP line can identify every item that must be satisfied AND which gate is evaluated.

**R13 gap analysis for R14:**

| Gap | Description | R14 axis |
|-----|-------------|----------|
| G-01 | Gate-0 annotation names threshold but uses generic "Gate" label, not "Gate-0" | V-01: Lifecycle emphasis — named-gate threshold annotation (C-46) |
| G-02 | Gate-0 condition line uses un-numbered gate prefix; self-containment not auditable from line alone | V-02: Output format — exhaustive flat-conjunction condition (C-47) |
| G-03 | C-46 threshold annotation delivered inline; may be missed when embedded in arithmetic | V-03: Phrasing register — labeled THRESHOLD line as independent element (C-46 variant) |
| G-04 | G-01 + G-02 co-present; ceiling requires both closed | V-04: Combined lifecycle + output format (C-46 + C-47) |
| G-05 | All five criteria (C-43 through C-47) require simultaneous satisfaction | V-05: Combined all axes (C-43 + C-44 + C-45 + C-46 + C-47) |

**Round 14 variation map:**

| Variation | Axis | Criteria targeted |
|-----------|------|-------------------|
| V-01 | Lifecycle emphasis — named-gate threshold annotation | C-46 |
| V-02 | Output format — flat AND-conjunction condition line | C-47 |
| V-03 | Phrasing register — labeled THRESHOLD element | C-46 (variant) |
| V-04 | Combined lifecycle + output format | C-46 + C-47 |
| V-05 | Combined all axes (full R14 ceiling) | C-43 + C-44 + C-45 + C-46 + C-47 |

---

## V-01: Lifecycle Emphasis — Named-Gate Threshold Annotation

**Variation axis**: Lifecycle emphasis — the Gate-0 annotation is restructured to place the
gate-pass threshold as a standalone sentence separate from the arithmetic decomposition. The
threshold sentence explicitly names "Gate-0" as its subject, satisfying C-46's requirement that
the annotation names the gate and declares the threshold. The condition line is NOT modified from
R13 V-05 (C-47 not addressed in this variation).

**Hypothesis**: C-46 closes the gap where "Gate passes when all 11 confirmed" (generic gate
reference) satisfies C-45 but fails C-46 because a reader cannot trace the threshold to a
specific numbered gate without the gate label. V-01 tests whether separating arithmetic from
threshold into two dedicated sentences — each on its own line — and explicitly using "Gate-0"
as the subject of the threshold sentence is sufficient for C-46 in isolation. Phase 2/3/5 cell-
exhaustive gates carry over from R13 V-05 (C-43 preserved); Gate-0 header carries "Gate-0" label
(C-44 preserved); check items [A1]–[A8] are individual (C-45 preserved).

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

  Arithmetic decomposition: 8 declared schemas + 3 structural checks = 11 items.
  Gate-0 passes when all 11 items above are confirmed; one STOP result halts Phase 1.

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

## V-02: Output Format — Flat AND-Conjunction Condition Line

**Variation axis**: Output format — the Gate-0 PASS/STOP condition line is rewritten as a flat
AND-conjunction enumerating every item label individually, so that reading the condition line
alone is sufficient to identify all 11 items that must be satisfied. Applied to Gate-0 only.
The annotation is NOT modified for named-gate threshold (C-46 not the target of this axis).

**Hypothesis**: C-47 requires the condition line itself — not the checklist body — to enumerate
all items. A condition that groups items as "schemas [A1]–[A8] all present + structural [B][C][D]
complete" satisfies C-45 (checklist atomicity) but an auditor reading only the condition line
sees ranges or categories rather than named items. V-02 tests whether a flat AND-conjunction
(`[A1] AND [A2] AND ... AND [A8] AND [B] AND [C] AND [D]`) satisfies C-47 by making every item
label explicit at the condition-line level. The annotation is unchanged from R13 V-05 ("Gate-0
passes when all 11 confirmed") — C-46 coverage via that annotation is preserved, not the focus.

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
  A missing §ID produces a detectable missing check item, not a silently failing compound condition.

  [GATE-0: PASS/STOP -- condition: [A1] AND [A2] AND [A3] AND [A4] AND [A5] AND [A6] AND [A7]
  AND [A8] AND [B] AND [C] AND [D]; all 11 items must individually confirm before gate passes]

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
  Check [5a]: §5 PROPOSAL SCOPE reproduced (per R-4)?
  Check [5b]: violation condition line present in reproduced §5?
  Check [5c]: all action types declared (non-null rows and typed null rows per §6 format)?
  Check [5d]: every non-null proposal row has "Why this beats NO CHANGE [R-0]" entry?
  [PHASE 5 GATE: PASS/STOP -- condition: §5 reproduced [5a] + violation condition [5b] +
  all types declared [5c] + R-0 applied to all rows [5d]]

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

## V-03: Phrasing Register — Labeled THRESHOLD Element

**Variation axis**: Phrasing register — the Gate-0 block introduces an explicitly labeled
"GATE-0 PASS THRESHOLD" line as a standalone named element separate from the arithmetic
decomposition and from the condition line. The threshold is institutionalized as a first-class
field, not an inline sentence. This tests whether C-46's "annotation naming the gate and
declaring the threshold" is better satisfied by a dedicated labeled element than by an inline
sentence embedded in the arithmetic commentary.

**Hypothesis**: An inline threshold sentence ("Gate-0 passes when all 11 confirmed") satisfies
C-46 structurally but may be visually buried in prose. A named field — "GATE-0 PASS THRESHOLD:
passes when all 11 items confirmed" — mirrors the convention used for §1 "Null behavior:" and
§4 "missing row != absent namespace": a labeled field that states its rule in isolation. V-03
tests whether this labeled-field format produces more reliable C-46 satisfaction than the inline
sentence form. C-47 not independently targeted: condition line follows R13 V-05 structure.

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

  Item decomposition: 8 declared schemas ([A1] through [A8]) + 3 structural checks ([B][C][D]).
  Item total: 11 items.
  GATE-0 PASS THRESHOLD: passes when all 11 items confirmed; blocked by any single STOP result.

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
  Check [5a]: §5 PROPOSAL SCOPE reproduced (per R-4)?
  Check [5b]: violation condition line present in reproduced §5?
  Check [5c]: all action types declared (non-null rows and typed null rows per §6 format)?
  Check [5d]: every non-null proposal row has "Why this beats NO CHANGE [R-0]" entry?
  [PHASE 5 GATE: PASS/STOP -- condition: §5 reproduced [5a] + violation condition [5b] +
  all types declared [5c] + R-0 applied to all rows [5d]]

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

## V-04: Combined — Named-Gate Threshold Annotation + Flat AND-Conjunction Condition

**Variation axis**: Combined V-01 (lifecycle emphasis — named-gate threshold annotation, C-46)
and V-02 (output format — flat AND-conjunction condition line, C-47). All other structure from
R13 V-05 is preserved (C-43 cell-exhaustive Phase 2/3/5 gates; C-44 Gate-0 header; C-45 per-§ID
check items).

**Hypothesis**: V-04 tests whether C-46 and C-47 are compatible and independently additive, or
whether one implementation creates interference with the other. The two mechanisms operate at
different levels: C-46 acts on the annotation sentence (above the checklist), C-47 acts on the
condition line (below the checklist). If they are structurally orthogonal, V-04 should pass both
without degradation of C-43 through C-45.

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

  Arithmetic decomposition: 8 declared schemas + 3 structural checks = 11 items.
  Gate-0 passes when all 11 items above are confirmed; one STOP result halts Phase 1.

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

  [GATE-0: PASS/STOP -- condition: [A1] AND [A2] AND [A3] AND [A4] AND [A5] AND [A6] AND [A7]
  AND [A8] AND [B] AND [C] AND [D]; all 11 items must individually confirm before gate passes]

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

## V-05: Combined All — C-43 + C-44 + C-45 + C-46 + C-47

**Variation axis**: Full combination — all five criteria simultaneously. Gate-0 carries:
(1) numbered "Gate-0" header (C-44), (2) per-§ID check items [A1]–[A8] (C-45), (3) named-gate
threshold annotation on its own dedicated line (C-46), (4) flat AND-conjunction condition
enumerating all 11 items individually (C-47). Phase 2/3/5 gates carry cell-exhaustive column
enumeration (C-43). No single-axis isolation — all mechanisms present simultaneously.

**Hypothesis**: C-43 through C-47 are structurally orthogonal and can be satisfied simultaneously
without interference. The named-gate threshold annotation (C-46) occupies the pre-checklist
annotation position; the flat AND-conjunction condition (C-47) occupies the post-checklist
condition line. The per-§ID checklist (C-45) populates the body. The Gate-0 header (C-44)
provides the section-level named identifier. The cell-exhaustive column gates in Phases 2/3/5
(C-43) are independent of Gate-0 entirely. V-05 predicts no degradation on C-01 through C-42.

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

  Arithmetic decomposition: 8 declared schemas + 3 structural checks = 11 items.
  Gate-0 passes when all 11 items above are confirmed; one STOP result halts Phase 1.

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
  reading this condition line enumerates all 11 items required; no item may be inferred by range]

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
| C-43 cell-exhaustive gate enumeration | PASS | FAIL | FAIL | PASS | PASS |
| C-44 numbered Gate-0 label in header | PASS | PASS | PASS | PASS | PASS |
| C-45 schema-gate checklist atomicity | PASS | PASS | PASS | PASS | PASS |
| C-46 schema-gate pass-threshold annotation | PASS | partial | PASS | PASS | PASS |
| C-47 gate-pass condition exhaustive item cross-reference | FAIL | PASS | FAIL | PASS | PASS |

**Single-axis isolation:**
- V-01 passes C-46 (named-gate threshold annotation) but not C-47 (condition still grouped)
- V-02 passes C-47 (flat AND-conjunction condition) but C-46 is partial (inline sentence, not separated)
- V-03 passes C-46 via labeled THRESHOLD element but not C-47 (same condition structure as R13 V-05)
- V-04 passes C-46 + C-47 (V-01 annotation + V-02 condition); preserves C-43 from R13 V-05
- V-05 passes all five criteria (C-43 through C-47); full ceiling for R14

**Key structural differences vs R13 V-05:**

| Site | R13 V-05 | V-01 (C-46) | V-02 (C-47) | V-03 (C-46 alt) | V-04 (C-46+C-47) | V-05 (all) |
|------|----------|-------------|-------------|-----------------|------------------|------------|
| Annotation sentence | "Gate-0 passes when all 11 confirmed." (inline) | Separate line: "Gate-0 passes when all 11 items above are confirmed" | Same as R13 | Labeled field: "GATE-0 PASS THRESHOLD:" | V-01 style | V-01 style |
| Condition line | `schemas [A1]...[A8] all present + [B] + [C] + [D]` | Same as R13 | `[A1] AND [A2] ... AND [D]` flat conjunction | Same as R13 | V-02 style | explicit enumeration + self-containment note |

**Predicted ceiling for R14**: V-04 or V-05. V-04 is the minimal combination; V-05 adds
the self-containment note in the condition line that explicitly states all items are enumerated
(no inference by range), which may improve reliability on C-47 in live runs.
