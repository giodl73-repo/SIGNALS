---
skill: quest-score
skill_target: topic-plan
date: 2026-03-15
round: 12
rubric: topic-plan-rubric-v12-2026-03-15.md
variations_scored: [V-01, V-02, V-03, V-04, V-05]
ceiling: 123
---

# topic-plan Skill Score — Round 12 (2026-03-15)

Rubric: v12 (C-01–C-41, /33 aspirational, max composite 123)
New criteria this round: C-39 (constraint scope index in contract), C-40 (per-phase active
R-N rules in authorization header), C-41 ("missing block != null" on all typed-null-capable
sections)

---

## Baseline Declaration

All five R12 variations inherit R11 V-05 as their complete baseline. R11 V-05 was confirmed
to satisfy C-01 through C-38 at the prior ceiling. R12 adds C-39, C-40, C-41 as new
aspirational criteria. All five R12 variations include the CONSTRAINT SCOPE INDEX (C-39),
per-phase active R-N rule declarations (C-40), and null annotations on all four typed-null-
capable sections (C-41) — these were the baseline for R12 variation construction, not new
features to test. The new axes (G-01 through G-04) are the discriminators, but they are not
yet rubric criteria: they do not affect the v12 composite score.

---

## Per-Variation Scoring

### V-01: Contract Completeness Pre-Gate

**New axis**: CONTRACT COMPLETENESS GATE before Phase 1 — verifies contract has all §IDs,
both indexes, and all null annotations. Gate uses [A][B][C][D] labeled sub-conditions and
emits [CONTRACT GATE: PASS/STOP].

**Authorization headers**: Prose form. Satisfies C-36 (labeled sub-header with §IDs) and
C-40 (active R-N rules listed). Does NOT restructure as compound gate with PASS/STOP.

| Criterion Block | Result | Evidence |
|-----------------|--------|----------|
| C-01 (read strategy.md) | PASS | Phase 1 opens strategy.md, fills Schema A |
| C-02 (signal inventory) | PASS | Phase 2, §4 all 9 namespaces |
| C-03 (delta detection) | PASS | STRATEGY DATE gating, CONFIRMED NEW / PRIOR-ONLY labels |
| C-04 (typed proposals) | PASS | §6 ADD/REMOVE/REPRIORITIZE with typed null rows |
| C-05 (confirmation gate) | PASS | Phase 6 halts with YES/NO/REVISED prompt |
| C-06 (evidence citation) | PASS | Evidence artifact [R-3] column in §6 |
| C-07 (before/after diff) | PASS | Before (from §1 Schema A [R-2]) / After columns |
| C-08 (inertia justification) | PASS | "Why this beats NO CHANGE [R-0]" column |
| C-09 (type-labeled null) | PASS | ADD/REMOVE/REPRIORITIZE: none -- inertia holds [R-0] |
| C-10 (conflict detection) | PASS | §8 conflict audit with typed null declared |
| C-11 (phase-gated lifecycle) | PASS | 7 named phases with PASS/STOP gates |
| C-12 (pre-scan commitment) | PASS | Phase 1 commitment before signal reading |
| C-13 (commitment reference integrity) | PASS | Before values from §1 Schema A; re-read prohibited |
| C-14 (self-documenting gate) | PASS | All gates name conditions explicitly |
| C-15 (temporal boundary attestation) | PASS | "Commitment phase complete. No signal artifacts read yet." in §3 |
| C-16 (verbatim quotation) | PASS | §2 VERBATIM BLOCK with quoted sentence |
| C-17 (per-namespace quantified) | PASS | total | new counts for all 9 namespaces |
| C-18 (re-read prohibition) | PASS | "Re-read prohibition: strategy.md may not be re-opened..." [R-1] |
| C-19 (source-anchored verbatim) | PASS | Source dimension: D-N in VERBATIM BLOCK |
| C-20 (change-pressure filter) | PASS | HIGH-PRESSURE namespaces gating §5 |
| C-21 (SEAL violation named) | PASS | "SEAL violation: A Before value not in Schema A at seal time..." [R-2] |
| C-22 (SCOPE violation named) | PASS | "SCOPE violation: A proposal row citing an excluded namespace is a SCOPE violation." |
| C-23 (source enforcement note) | PASS | "Enforcement note: A Source dimension field not matching a D-N label fails this block." |
| C-24 (commitment compound gate) | PASS | Gate 1: Check [1] §1, Check [2] §2, Check [3] §3 |
| C-25 (Gate 1 audits enforcement note) | PASS | [2c] Enforcement note present as labeled field |
| C-26 (PROPOSAL SCOPE reproduced Phase 5) | PASS | §5 reproduced at Phase 5 enforcement point |
| C-27 (scope gate audits violation condition) | PASS | SCOPE GATE checks violation condition line present |
| C-28 (enforcement note as labeled field) | PASS | "Enforcement note: ..." as labeled field in §2 template |
| C-29 (gate sub-requirements with labels) | PASS | [2a][2b][2c] in Gate 1 |
| C-30 (Skill Execution Contract) | PASS | Named SKILL EXECUTION CONTRACT pre-declares all templates, rules, sequence |
| C-31 (phases execute against contract) | PASS | "[per Skill Execution Contract]" at each phase header |
| C-32 (enforcement linked to contract) | PASS | "(reproduced from Skill Execution Contract §5)" in Phase 5 |
| C-33 (conflict audit null declaration) | PASS | Typed null declared in §8 |
| C-34 (double-anchored attribution) | PASS | "reproduced from Skill Execution Contract §5" -- name + §ID |
| C-35 (phase authorization index) | PASS | PHASE AUTHORIZATION INDEX with §ID mappings per phase |
| C-36 (per-phase authorization sub-header) | PASS | Labeled "Authorization check (per Skill Execution Contract §PHASE AUTHORIZATION INDEX)" at each phase |
| C-37 (constraint rules R-N numbered) | PASS | R-0 through R-4 in CONSTRAINT RULES |
| C-38 ("missing block != null" in §8) | PASS | §8 annotated "missing block != null" |
| C-39 (constraint scope index in contract) | PASS | CONSTRAINT SCOPE INDEX with R-0–R-4 phase ranges |
| C-40 (per-phase active R-N in auth header) | PASS | "Active constraint rules for Phase N (per §CONSTRAINT SCOPE INDEX): R-N" at each phase |
| C-41 (null annotation all typed-null sections) | PASS | §4, §5, §6, §8 all annotated with absence-is-not-null |

**Essential**: 5/5 PASS
**Recommended**: 3/3 PASS
**Aspirational**: 33/33 PASS

**Composite**: 60 + 30 + 33 = **123**
**Golden**: YES

**Gap coverage**: G-01 PRESENT (CONTRACT COMPLETENESS GATE with [A][B][C][D]), G-02 absent, G-03 absent, G-04 absent

---

### V-02: Compound Authorization Gate at Phase Entry

**New axis**: Authorization check at each phase entry restructured as compound gate with
[1a] §IDs (per PHASE AUTHORIZATION INDEX) and [1b] R-N rules (per CONSTRAINT SCOPE INDEX),
followed by [AUTHORIZATION GATE: PASS/STOP]. Makes C-36+C-40 a named compound gate.

**Note**: V-02 does NOT include a CONTRACT COMPLETENESS GATE before Phase 1 (G-01 absent).

| Criterion Block | Result | Evidence |
|-----------------|--------|----------|
| C-01 through C-38 | PASS (all) | Same as V-01 -- baseline fully preserved |
| C-39 (constraint scope index) | PASS | CONSTRAINT SCOPE INDEX with R-0–R-4 phase ranges |
| C-40 (per-phase active R-N in auth header) | PASS | [1b] Active constraint rules at each phase, structured as compound gate sub-condition |
| C-41 (null annotation all typed-null sections) | PASS | §4, §5, §6, §8 all annotated |

**V-02 authorization header form** (G-02):
```
[1a] Authorized §IDs (per §PHASE AUTHORIZATION INDEX): ...
[1b] Active constraint rules (per §CONSTRAINT SCOPE INDEX): ...
[AUTHORIZATION GATE: PASS/STOP -- condition: [1a] §IDs verified + [1b] R-N rules verified]
```
C-36 and C-40 each become a labeled sub-condition of a named compound gate, structurally
analogous to C-29 (gate sub-requirements with identifier labels) at the authorization level.

**Essential**: 5/5 PASS
**Recommended**: 3/3 PASS
**Aspirational**: 33/33 PASS

**Composite**: 60 + 30 + 33 = **123**
**Golden**: YES

**Gap coverage**: G-01 absent, G-02 PRESENT ([1a][1b] + AUTHORIZATION GATE PASS/STOP), G-03 absent, G-04 absent

---

### V-03: R-N Enforcement Result Declarations

**New axis**: At each point where a constraint rule is applied, an explicit declarative
result is emitted: "[R-N APPLIED: rule, action, what a violation looks like]".

**Enforcement points with declarations in V-03**:
- §3 seal: `[R-1 APPLIED: strategy.md is now sealed -- any re-read of strategy.md before user confirmation at Phase 6 is a violation of R-1. R-2 is now active: Before values in §6 must trace to the Schema A rows above, not to strategy.md.]`
- Phase 4 reading: `[R-3 APPLIED: reading only artifacts with date > STRATEGY DATE -- any artifact dated on or before STRATEGY DATE is ineligible evidence regardless of namespace. Per §CONSTRAINT SCOPE INDEX, R-3 is active in Phases 4 and 5.]`
- §5 reproduction: `[R-4 APPLIED: §5 reproduced from Skill Execution Contract §5 -- contract name and §ID cited. Any reproduction lacking both contract name and §ID reference fails R-4.]`
- §6 Before values: `[R-2 APPLIED: Before values must trace to §1 Schema A sealed in Phase 1...]`
- §6 evidence: `[R-3 APPLIED: evidence restricted to artifacts dated after STRATEGY DATE...]`

**Authorization headers**: Prose form (baseline). Satisfies C-36 and C-40 but NOT as
compound gate (G-02 absent).

| Criterion Block | Result | Evidence |
|-----------------|--------|----------|
| C-01 through C-38 | PASS (all) | Baseline preserved |
| C-39 (constraint scope index) | PASS | CONSTRAINT SCOPE INDEX with R-0–R-4 phase ranges |
| C-40 (per-phase active R-N in auth header) | PASS | "Active constraint rules for Phase N (per §CONSTRAINT SCOPE INDEX): R-N" |
| C-41 (null annotation all typed-null sections) | PASS | §4, §5, §6, §8 all annotated |

**Essential**: 5/5 PASS
**Recommended**: 3/3 PASS
**Aspirational**: 33/33 PASS

**Composite**: 60 + 30 + 33 = **123**
**Golden**: YES

**Gap coverage**: G-01 absent, G-02 absent, G-03 PRESENT ([R-N APPLIED: ...] at each application point), G-04 absent

---

### V-04: R-0 Evaluation Documentation in Null Rows

**New axis**: Each typed-null row in §6 carries an "R-0 evaluation" field documenting the
specific consequence examined and found insufficient to warrant change.

**§6 null row template extended in V-04**:
```
Null row: "[TYPE]: none -- inertia holds [R-0]. R-0 evaluation: [consequence examined
          and found insufficient to warrant change]."
```

**Phase 5 null rows** (V-04 documenting specific evaluations):
```
ADD: none -- inertia holds [R-0].
  R-0 evaluation: no new dimension identified in HIGH-PRESSURE artifacts whose absence
  from strategy produces a demonstrably worse outcome than current coverage.
REMOVE: none -- inertia holds [R-0].
  R-0 evaluation: no dimension in current strategy found without NEW artifact support
  where removal would produce better outcomes than retention.
REPRIORITIZE: none -- inertia holds [R-0].
  R-0 evaluation: no NEW artifact evidence found for an ordering that produces better
  sequencing outcomes than current priority structure.
```

**Gate 5 extended** with Check [5]: "every null row has 'R-0 evaluation' field documenting
consequence examined."

**Authorization headers**: Prose form (baseline). C-41 intact — §6 null row format change
preserves "missing null row != no proposals" annotation in the §6 template section.

| Criterion Block | Result | Evidence |
|-----------------|--------|----------|
| C-01 through C-38 | PASS (all) | Baseline preserved |
| C-39 (constraint scope index) | PASS | CONSTRAINT SCOPE INDEX with R-0–R-4 phase ranges |
| C-40 (per-phase active R-N in auth header) | PASS | "Active constraint rules for Phase N (per §CONSTRAINT SCOPE INDEX): R-N" |
| C-41 (null annotation all typed-null sections) | PASS | §4 "missing row != absent namespace", §5 "missing block != null", §6 "missing null row != no proposals", §8 "missing block != null" -- all present in §6 template section alongside extended null row format |

**Essential**: 5/5 PASS
**Recommended**: 3/3 PASS
**Aspirational**: 33/33 PASS

**Composite**: 60 + 30 + 33 = **123**
**Golden**: YES

**Gap coverage**: G-01 absent, G-02 absent, G-03 absent, G-04 PRESENT (R-0 evaluation field in null rows for ADD/REMOVE/REPRIORITIZE)

---

### V-05: Combined — All Four Axes

**New axes combined**: V-01 CONTRACT COMPLETENESS GATE + V-02 compound authorization gate
[1a][1b] + V-03 R-N enforcement result declarations + V-04 R-0 evaluation in null rows.

V-05 carries `[V-01 axis]`, `[V-02 axis]`, `[V-03 axis]`, `[V-04 axis]` annotations at each
new structural element. The four axes are structurally non-conflicting and additive.

| Criterion Block | Result | Evidence |
|-----------------|--------|----------|
| C-01 through C-38 | PASS (all) | Baseline preserved |
| C-39 (constraint scope index) | PASS | CONSTRAINT SCOPE INDEX with R-0–R-4 phase ranges |
| C-40 (per-phase active R-N in auth header) | PASS | [1b] in compound authorization gate form at each phase |
| C-41 (null annotation all typed-null sections) | PASS | §4, §5, §6, §8 all annotated; §6 extended null row format preserves "missing null row != no proposals" |

**Essential**: 5/5 PASS
**Recommended**: 3/3 PASS
**Aspirational**: 33/33 PASS

**Composite**: 60 + 30 + 33 = **123**
**Golden**: YES

**Gap coverage**: G-01 PRESENT, G-02 PRESENT, G-03 PRESENT, G-04 PRESENT

---

## Summary Table

| Variation | Essential | Recommended | Aspirational | Composite | Golden | G-01 | G-02 | G-03 | G-04 |
|-----------|-----------|-------------|--------------|-----------|--------|------|------|------|------|
| V-01 | 5/5 | 3/3 | 33/33 | **123** | YES | YES | no | no | no |
| V-02 | 5/5 | 3/3 | 33/33 | **123** | YES | no | YES | no | no |
| V-03 | 5/5 | 3/3 | 33/33 | **123** | YES | no | no | YES | no |
| V-04 | 5/5 | 3/3 | 33/33 | **123** | YES | no | no | no | YES |
| V-05 | 5/5 | 3/3 | 33/33 | **123** | YES | YES | YES | YES | YES |

All five variations hit the v12 ceiling of 123. Discrimination is on the Gap axes only.

---

## Ranking

All five variations are tied at 123. Ranking by structural richness (Gap axis coverage):

1. **V-05** (123) — all four Gap axes present simultaneously; maximum structural surface
2. **V-01** (123) — G-01: CONTRACT COMPLETENESS GATE, strongest lifecycle framing
3. **V-02** (123) — G-02: compound AUTHORIZATION GATE, strongest output format framing
4. **V-03** (123) — G-03: R-N enforcement event declarations, strongest phrasing register
5. **V-04** (123) — G-04: R-0 evaluation trace in null rows, strongest inertia framing

V-05 is the top variation by convention (combined placed first when ceiling is shared).

---

## Excellence Signals (from V-05)

V-05 surfaces four structural patterns not yet captured as rubric criteria:

**Signal 1 — Contract completeness verification as named pre-execution gate** (G-01):
V-05 adds a CONTRACT COMPLETENESS GATE with four labeled sub-conditions ([A] §IDs, [B] phase
index, [C] constraint index, [D] null annotations) that must PASS before Phase 1 begins.
This parallels how phases verify their own entry conditions at runtime, but operates at the
contract level. Pattern: the contract declares requirements; this gate verifies the contract
itself is complete before any phase executes. Distinct from all existing criteria: C-30
requires the contract to pre-declare; C-35+C-39 require it to include both indexes; C-41
requires null annotations -- but no criterion requires the contract's completeness to be
VERIFIED before execution begins.

**Signal 2 — Authorization header as compound gate with [1a][1b] and named PASS/STOP** (G-02):
V-05 restructures each phase's authorization check as a named compound gate:
`[1a]` for §IDs (C-36) and `[1b]` for R-N rules (C-40), followed by
`[AUTHORIZATION GATE: PASS/STOP -- condition: [1a] §IDs verified + [1b] R-N rules verified]`.
This is structurally analogous to C-29 (gate sub-requirements with identifier labels [Na][Nb][Nc])
applied at the authorization header level. C-36+C-40 compliance becomes independently
verifiable via labeled sub-conditions with a named PASS/STOP result, not just readable prose.

**Signal 3 — Enforcement event declaration at application point** (G-03):
V-05 adds `[R-N APPLIED: ...]` declarations at each enforcement point, stating (a) the rule
identifier, (b) the action taken, and (c) what a violation would look like. This closes the
traceability chain: contract declares R-N → phase authorization header lists R-N as active
→ application point declares R-N applied with result. Each link is independently auditable
without cross-referencing another section. Pattern: three-link enforcement chain — declare,
authorize, apply — each link with a named artifact.

**Signal 4 — R-0 evaluation documentation in typed-null rows** (G-04):
V-05 extends the inertia obligation from non-null proposals (C-08: must prove change beats
NO CHANGE) to null declarations: each typed-null row carries "R-0 evaluation: [consequence
examined and found insufficient]" naming the specific decision not to propose. Structurally
symmetric to C-06 (evidence citation in non-null proposals): non-null rows name the artifact
motivating change; null rows name the consequence evaluated and found insufficient. Pattern:
the proposals table becomes a complete decision record for both the positive (proposed) and
null (no proposal) cases.

---

## New Patterns for R13

| Gap | Pattern | Structural analogue | Strength |
|-----|---------|---------------------|----------|
| G-01 | Contract completeness pre-gate with [A][B][C][D] | Contract declares; gate verifies (mirrors phase-entry gates) | Strong |
| G-02 | Authorization header as compound gate [1a][1b] + AUTHORIZATION GATE PASS/STOP | C-29 gate sub-requirements with labels -- same structure at auth level | Strongest |
| G-03 | R-N enforcement event declaration [R-N APPLIED: ...] at application point | Three-link chain: contract declare -> phase authorize -> point apply | Strong |
| G-04 | R-0 evaluation trace in null rows | C-06 evidence citation applied to null case symmetrically | Strongest |

Predicted discriminators for R13: G-02 (compound authorization gate is the direct auth-level
analogue of C-29's gate sub-requirements) and G-04 (R-0 evaluation in null rows is the direct
null-case analogue of C-06's evidence citation in non-null proposals).

---

```json
{"top_score": 123, "all_essential_pass": true, "new_patterns": ["contract completeness verification as named pre-execution gate before Phase 1 (CONTRACT COMPLETENESS GATE with [A][B][C][D] sub-conditions) -- contract declares requirements; this gate verifies the contract itself is complete before any phase executes", "authorization header as compound gate with [1a] §IDs and [1b] R-N rules plus named AUTHORIZATION GATE PASS/STOP -- C-36+C-40 structured as independently verifiable labeled sub-conditions, structurally analogous to C-29 applied at the authorization level", "R-N enforcement event declaration [R-N APPLIED: ...] at each application point -- closes three-link enforcement chain: contract declare -> phase authorize -> application point apply, each independently auditable", "R-0 evaluation documentation in typed-null rows -- null declarations carry consequence-examined-and-found-insufficient reasoning, symmetric to C-06 evidence citation in non-null proposals; proposals table becomes a complete decision record for both the positive and null cases"]}
```
