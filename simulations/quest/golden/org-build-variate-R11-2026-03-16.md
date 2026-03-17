---
skill: quest-variate
skill_target: org-build
date: 2026-03-16
round: R11
rubric_version: v8
status: variate
---

# org-build Variate -- Round 11 (Rubric v8)

**Date:** 2026-03-16
**Skill:** org-build
**Rubric:** v8 (C-01 through C-28; C-27/C-28 new from v8)
**Round:** R11

**R10 ceiling under v8 rubric:**
Two structural failures persist across all R10 variations:

1. **C-27 gap (depth-flag-conditional count floor):** R10 Phase 1 declares
   T1-DEPTH-FLAG but states the count range (20-30 / 50+) as flat text — either
   in preamble or in Phase 2's instructions — without encoding it as a conditional
   bound to the flag value inside Phase 1's instruction body. C-27 requires the
   binding to live in Phase 1 as an explicit conditional: "T1-DEPTH-FLAG = standard
   → MUST enumerate 20-30 roles; T1-DEPTH-FLAG = deep → MUST enumerate 50+ roles."
   Moving the range to a rubric note or Phase 2 default fails C-27 regardless of
   whether the model produces the correct count.

2. **C-28 gap (ordering anchor as named first field inside record block):** R10 uses
   FORBIDDEN directives in preamble prose before or after record blocks, then claims
   structural unification in that preamble. C-28 requires the `PHASE-ORDERING-GUARD:`
   field to be structurally inside the block as its first entry. Preamble-level
   assertions that the block IS the ordering anchor do not satisfy C-28 — the
   mechanism must be the field itself, not a prose claim about the field.

**R11 target:** Close C-27 and C-28 across all five variations. V-01/V-02/V-03 are
single-axis; V-04/V-05 are combined.

---

## Variation Map

| V | Axis | Hypothesis |
|---|------|------------|
| V-01 | Count-conditional binding (single) | Encoding the depth-flag-to-count binding as an explicit two-branch conditional in Phase 1's instruction body — before the record block — closes C-27 without requiring any other structural change; the PHASE-ORDERING-GUARD field as first block entry closes C-28 |
| V-02 | Record block anchor structure (single) | Designing every record block with PHASE-ORDERING-GUARD as a structurally mandatory first field — and adding a block-architecture declaration at prompt open explaining why the first field is required — forces C-28 compliance at the schema level, not the instance level |
| V-03 | Inertia-first verdict declaration (single) | Moving the IA scope template selection into Phase 1 (as a gate output alongside T1-VERDICT) makes T1-IA-SCOPE-KEY a named typed variable that Phase 2 consumes via explicit input contract, wiring C-11/C-17 through the gate machinery rather than as standalone instructions |
| V-04 | Count-conditional + Record anchor + Phrasing register (combined) | Full MUST/FORBIDDEN register throughout, count-floor binding as explicit Phase 1 conditional (C-27), and PHASE-ORDERING-GUARD as first block field (C-28) interact: when every constraint is imperative, the block-structure requirement and count-binding requirement feel structurally equivalent — each is a constraint on a named variable, not a formatting preference |
| V-05 | Count-conditional + Record anchor + Unification architecture (combined) | Designing each record block as the explicit unification artifact (C-26) — with in-block commentary naming the four observable properties — makes PHASE-ORDERING-GUARD-as-first-field the natural consequence of the unification claim rather than a bolted-on format rule; an IA role file skeleton with `{{T1-IA-SCOPE-KEY-TEMPLATE}}` slot satisfies C-22 |

---

## V-01 -- Count-Conditional Binding

**axis:** count-conditional binding in Phase 1 instruction
**hypothesis:** Encoding the depth-flag-to-count binding as an explicit two-branch
conditional inside Phase 1's instruction body closes C-27. The binding is a Phase 1
output variable (T1-COUNT-FLOOR), not a Phase 2 default. PHASE-ORDERING-GUARD as
first field in every record block closes C-28.

---

```
You are running `/org-build {topic}`.

Build a complete organizational structure from the provided scan results or
repository. Every phase produces a named record block. Every record block's first
field is PHASE-ORDERING-GUARD, which carries the FORBIDDEN for the next phase.
No phase begins until the prior phase's record block is emitted.

---

PHASE 1 -- ASSESS

Read all provided inputs before any step.

Step 1.1 -- Depth Flag

Classify the invocation depth:
  `--depth deep` passed  -> T1-DEPTH-FLAG = deep
  otherwise              -> T1-DEPTH-FLAG = standard

DEPTH-FLAG-CONDITIONAL COUNT FLOOR -- encode this binding now as a Phase 1 output:
  T1-DEPTH-FLAG = standard -> T1-COUNT-FLOOR = 20-30
  T1-DEPTH-FLAG = deep     -> T1-COUNT-FLOOR = 50+

FORBIDDEN: declaring T1-DEPTH-FLAG without declaring T1-COUNT-FLOOR.
FORBIDDEN: stating a flat count range that does not reference T1-DEPTH-FLAG.
FORBIDDEN: placing the count-floor binding outside Phase 1.

Step 1.2 -- Inertia Assessment

Assess the case for flat operation from the inputs. Evaluate:
  1. Coordination mechanisms in use (named channels, cadences, shared artifacts)
  2. Decision velocity (blocked / normal / fast)
  3. Cross-functional friction (high / medium / low)
  4. Structural symptom evidence (present / absent)

Assign FLAT-CASE-PRESSURE from the closed set: LOW | MODERATE | ELEVATED | HIGH
  LOW:      no observable coordination failures
  MODERATE: coordination strain under load; no failures yet
  ELEVATED: observable failures or blocked decisions
  HIGH:     systematic breakdown; structure is clearly warranted

Step 1.3 -- Verdict

Write exactly one verdict from the closed set:
  CAN-OPERATE-FLAT
  STRUCTURE-WARRANTED

Only one verdict. Both is an error. Neither is an error.
FORBIDDEN: writing both verdicts.
FORBIDDEN: omitting the verdict.
MUST reference FLAT-CASE-PRESSURE by name in the verdict reasoning.

Step 1.4 -- IA Scope Template Selection

Select the verbatim template keyed to T1-PRESSURE:
  LOW:
    "Monitor adoption signals and flag emerging resistance patterns. No structural
    intervention warranted at current pressure level."
  MODERATE:
    "Actively surface status-quo arguments in reviews. Ensure inertia costs are
    quantified before each major design commitment."
  ELEVATED:
    "Challenge every architectural constraint inherited from prior systems. Document
    each instance where the team defaults to familiar patterns over evidence-based
    choices."
  HIGH:
    "Veto any design decision that cannot demonstrate superiority over the current
    approach. The burden of proof for change is maximal; operate as the primary
    structural check on premature commitment."

Record: T1-IA-SCOPE-KEY = [LOW | MODERATE | ELEVATED | HIGH]
FORBIDDEN: applying a template keyed to a rating other than T1-PRESSURE.
FORBIDDEN: beginning Phase 2 before emitting the Phase 1 record block.

=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD:  FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG:         [standard | deep]
T1-COUNT-FLOOR:        [20-30 | 50+]
T1-PRESSURE:           [LOW | MODERATE | ELEVATED | HIGH]
T1-VERDICT:            [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T1-IA-SCOPE-KEY:       [LOW | MODERATE | ELEVATED | HIGH]
T1-MECHANISM-COUNT:    [number]
===

---

PHASE 2 -- ENUMERATE ROLES

INBOUND CONTRACT: FORBIDDEN: Phase 2 begins before Phase 1 record block is emitted.
MUST read: T1-DEPTH-FLAG, T1-COUNT-FLOOR, T1-IA-SCOPE-KEY from Phase 1 record block.
FORBIDDEN: executing this phase if any of those variables are unresolved.

Step 2.1 -- Role Count

MUST produce the count bound to T1-COUNT-FLOOR from Phase 1:
  T1-DEPTH-FLAG = standard -> MUST produce 20-30 roles
  T1-DEPTH-FLAG = deep     -> MUST produce 50+ roles

FORBIDDEN: producing fewer than the lower bound of T1-COUNT-FLOOR.
FORBIDDEN: exceeding the upper bound by >20% without the deep flag.

Step 2.2 -- Role Files

Write one .craft/roles/{area}/{role}.md file per role.
MUST group roles under area subdirectories.
MUST use at least 2 area subdirectories.
FORBIDDEN: all roles in a flat directory without area grouping.

Every role file MUST contain exactly these five fields:
  orientation:       [primary axis: people | product | process | technical]
  lens:              [cognitive or professional filter this role applies]
  expertise:         [domain knowledge this role holds]
  scope:             [boundary of this role's authority and decisions]
  collaborates_with: [list of role names this role works with regularly]

FORBIDDEN: any role file missing one or more of these five fields.

Step 2.3 -- Inertia-Advocate Role

MUST include inertia-advocate unconditionally.
FORBIDDEN: omitting inertia-advocate for any reason.

The inertia-advocate scope MUST use the verbatim template text for T1-IA-SCOPE-KEY:
  LOW:
    "Monitor adoption signals and flag emerging resistance patterns. No structural
    intervention warranted at current pressure level."
  MODERATE:
    "Actively surface status-quo arguments in reviews. Ensure inertia costs are
    quantified before each major design commitment."
  ELEVATED:
    "Challenge every architectural constraint inherited from prior systems. Document
    each instance where the team defaults to familiar patterns over evidence-based
    choices."
  HIGH:
    "Veto any design decision that cannot demonstrate superiority over the current
    approach. The burden of proof for change is maximal; operate as the primary
    structural check on premature commitment."

FORBIDDEN: paraphrasing the template text.
FORBIDDEN: composing a new scope instead of applying the template.
FORBIDDEN: applying a template keyed to a rating other than T1-IA-SCOPE-KEY.

Count role files after writing. Verify count is within T1-COUNT-FLOOR range.
FORBIDDEN: beginning Phase 3 before emitting the Phase 2 record block.

=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD:    FORBIDDEN: Phase 3 begins before this block is emitted.
T2-ROLE-COUNT:           [number]
T2-AREA-COUNT:           [number]
T2-COUNT-CHECK:          [PASS: within T1-COUNT-FLOOR range | FAIL: outside range]
T2-IA-PRESENT:           [YES | NO]
T2-IA-SCOPE-FIRST-WORDS: [verbatim first 8 words of scope field applied]
===

---

PHASE 3 -- BUILD ORG-CHART.MD

INBOUND CONTRACT: FORBIDDEN: Phase 3 begins before Phase 2 record block is emitted.
FORBIDDEN: proceeding if T2-COUNT-CHECK = FAIL or T2-IA-PRESENT = NO.
MUST read: T1-VERDICT, T1-PRESSURE from Phase 1 record block.

Write org-chart.md with all nine sections in this order:

SECTION 1: ASCII HIERARCHY DIAGRAM
MUST render a box-and-line ASCII diagram with at least 2 org levels.
FORBIDDEN: flat name list without hierarchy structure.

SECTION 2: HEADCOUNT BY AREA TABLE
MUST include columns: Area | Headcount | Key Roles | Decides | Escalates
FORBIDDEN: omitting the Decides column.
FORBIDDEN: omitting the Escalates column.
FORBIDDEN: merging Decides and Escalates into a single column.

SECTION 3: LEVEL DISTRIBUTION
Show role distribution across levels (IC, Lead, Principal, Manager, Director, etc.).

SECTION 4: INERTIA VERDICT BLOCK
Emit:
  FLAT-CASE-PRESSURE: [T1-PRESSURE from Phase 1 record]
  VERDICT: [T1-VERDICT from Phase 1 record]
Only one verdict. Both is an error. Neither is an error.
FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED.
FORBIDDEN: omitting the verdict block.

SECTION 5: ANTI-PATTERN CATEGORY DERIVATION
Derive anti-pattern categories from T1-VERDICT:
  T1-VERDICT = CAN-OPERATE-FLAT:
    MUST use cat-2 (coordination overhead) and cat-3 (role ambiguity).
    FORBIDDEN: cat-1 (span of control) in this path.
    FORBIDDEN: cat-4 (reporting hierarchy) in this path.
  T1-VERDICT = STRUCTURE-WARRANTED:
    MUST use cat-1 (span of control) and cat-4 (reporting hierarchy).
    FORBIDDEN: cat-2 (coordination overhead) in this path.
    FORBIDDEN: cat-3 (role ambiguity) in this path.
Record: T3-ANTI-PATTERN-PATH = [path selected]

SECTION 6: ANTI-PATTERN WATCH TABLE
Columns: Anti-Pattern | Why It Applies Here | Mitigation
MUST open every "Why It Applies Here" cell with:
  [element name] (cat-N) -- [one sentence of specific relevance]
FORBIDDEN: plain prose without the (cat-N) citation syntax.
FORBIDDEN: cat codes outside T3-ANTI-PATTERN-PATH.
MUST include a specific remediation action in every Mitigation cell.
FORBIDDEN: format instructions or column-structure guidance in Mitigation cells.

SECTION 7: OPERATING RHYTHM TABLE
Columns: Cadence | Frequency | Owner | Purpose
MUST include at least 3 distinct rows: ROB + shiproom + governance meeting.
FORBIDDEN: combining two meetings into one row.

SECTION 8: COMMITTEE CHARTERS
Write one charter per governance meeting. Each charter MUST include:
  Name:
  Cadence:
  Owner:
  Participants:
  Quorum: [N of M]
FORBIDDEN: Quorum expressed without the N of M fraction format.

SECTION 9: ORG EVOLUTION ROADMAP
MUST include at least 2 rows: | Trigger | Structural Change | Type |
Row 1 MUST be a headcount threshold trigger.
Row 2 MUST be a different category (velocity signal, structural symptom, or milestone).
FORBIDDEN: two headcount threshold rows.

FORBIDDEN: beginning Phase 4 before emitting the Phase 3 record block.

=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD:    FORBIDDEN: Phase 4 begins before this block is emitted.
T3-ORG-CHART-SECTIONS:   [section numbers produced, comma-separated]
T3-ANTI-PATTERN-PATH:    [CAN-OPERATE-FLAT: cat-2/cat-3 | STRUCTURE-WARRANTED: cat-1/cat-4]
T3-VERDICT-EMITTED:      [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T3-EVOLUTION-ROW-TYPES:  [Row 1 type, Row 2 type]
===

---

PHASE 4 -- VERIFY

INBOUND CONTRACT: FORBIDDEN: Phase 4 begins before Phase 3 record block is emitted.

Cross-record consistency checks:
  T1-VERDICT = T3-VERDICT-EMITTED          -> T4-VERDICT-CONSISTENT
  T2-COUNT-CHECK = PASS                    -> T4-COUNT-CONSISTENT
  T2-IA-PRESENT = YES                      -> T4-IA-PRESENT
  T2-IA-SCOPE-FIRST-WORDS verbatim match
    for T1-IA-SCOPE-KEY template           -> T4-IA-SCOPE-VERBATIM

FORBIDDEN: declaring completion if any check = FAIL.
MUST correct all failing checks before recording COMPLETE.

=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD:   FORBIDDEN: declaring completion before this block is emitted.
T4-VERDICT-CONSISTENT:  [PASS | FAIL]
T4-COUNT-CONSISTENT:    [PASS | FAIL]
T4-IA-PRESENT:          [PASS | FAIL]
T4-IA-SCOPE-VERBATIM:   [PASS | FAIL]
T4-FINAL-STATUS:        [COMPLETE | REQUIRES-CORRECTION]
===
```

---

## V-02 -- Record Block Anchor Structure

**axis:** record block designed as structural anchor; PHASE-ORDERING-GUARD is the
mandatory first field at the schema level
**hypothesis:** Declaring the block architecture at prompt open -- explaining that
PHASE-ORDERING-GUARD is always the first field and why -- forces C-28 compliance
as a schema property of every record block, not as an instance-level instruction.
The block format becomes self-describing: a reader who encounters any record block
knows the guard is the first field without reading surrounding prose.

---

```
You are running `/org-build {topic}`.

RECORD BLOCK ARCHITECTURE: Every phase boundary in this skill is anchored by a
named record block (=== RECORD: PHASE-N ===). The record block is the observable
gate for that phase. Its structure is fixed:

  === RECORD: PHASE-N ===
  PHASE-ORDERING-GUARD: FORBIDDEN: Phase N+1 begins before this block is emitted.
  [variable-1]: [value]
  [variable-2]: [value]
  ...
  ===

PHASE-ORDERING-GUARD is always the first field inside the block. It carries the
FORBIDDEN directive that prevents the next phase from beginning before this block
is emitted. The guard is inside the block -- not in surrounding prose, not in
preamble instructions, not after the closing ===. A record block without
PHASE-ORDERING-GUARD as its first field is malformed and fails this skill.

Every phase has an INBOUND CONTRACT (FORBIDDEN before this phase begins, referencing
the prior phase's record block) and an OUTBOUND GATE (the record block itself,
emitted before the next phase begins).

---

PHASE 1 -- ASSESS

Read all provided inputs.

1.1 -- Depth Flag

Classify:
  `--depth deep` passed  -> T1-DEPTH-FLAG = deep
  otherwise              -> T1-DEPTH-FLAG = standard

Bind count floor to T1-DEPTH-FLAG now -- this is a Phase 1 gate output:
  T1-DEPTH-FLAG = standard -> T1-COUNT-FLOOR = 20-30
  T1-DEPTH-FLAG = deep     -> T1-COUNT-FLOOR = 50+

FORBIDDEN: declaring T1-DEPTH-FLAG without T1-COUNT-FLOOR.
FORBIDDEN: a flat count range not derived from T1-DEPTH-FLAG.
FORBIDDEN: placing this binding in a later phase.

1.2 -- Inertia Assessment

Document coordination mechanisms in use:
  | Mechanism Name | Type | Frequency / Participants |
  Type closed set: Channel / Informal Role / Recurring Cadence / Shared Artifact

MUST include at least 2 mechanism rows.
Name the single coordination failure this flat arrangement cannot resolve.

1.3 -- FLAT-CASE-PRESSURE

Assign from the closed set: LOW | MODERATE | ELEVATED | HIGH
  LOW:      no observable coordination failures
  MODERATE: strain under load; no failures yet
  ELEVATED: observable failures or blocked decisions
  HIGH:     systematic breakdown

1.4 -- Verdict

Assign exactly one:
  CAN-OPERATE-FLAT
  STRUCTURE-WARRANTED

Only one verdict. Both is an error. Neither is an error.
FORBIDDEN: writing both. FORBIDDEN: omitting both.

1.5 -- IA Scope Template Selection

Select verbatim template keyed to T1-PRESSURE:
  LOW:
    "Monitor adoption signals and flag emerging resistance patterns. No structural
    intervention warranted at current pressure level."
  MODERATE:
    "Actively surface status-quo arguments in reviews. Ensure inertia costs are
    quantified before each major design commitment."
  ELEVATED:
    "Challenge every architectural constraint inherited from prior systems. Document
    each instance where the team defaults to familiar patterns over evidence-based
    choices."
  HIGH:
    "Veto any design decision that cannot demonstrate superiority over the current
    approach. The burden of proof for change is maximal; operate as the primary
    structural check on premature commitment."

Record: T1-IA-SCOPE-KEY = [LOW | MODERATE | ELEVATED | HIGH]

OUTBOUND GATE -- emit record block now. PHASE-ORDERING-GUARD is the first field.

=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD:  FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG:         [standard | deep]
T1-COUNT-FLOOR:        [20-30 | 50+]
T1-PRESSURE:           [LOW | MODERATE | ELEVATED | HIGH]
T1-VERDICT:            [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T1-IA-SCOPE-KEY:       [LOW | MODERATE | ELEVATED | HIGH]
T1-MECHANISM-COUNT:    [number]
===

---

PHASE 2 -- ENUMERATE ROLES

INBOUND CONTRACT: FORBIDDEN: Phase 2 begins before Phase 1 record block is emitted.
MUST read: T1-DEPTH-FLAG, T1-COUNT-FLOOR, T1-IA-SCOPE-KEY from Phase 1 record block.

2.1 -- Role Count

MUST produce roles per T1-COUNT-FLOOR from Phase 1:
  T1-DEPTH-FLAG = standard -> MUST produce 20-30 roles
  T1-DEPTH-FLAG = deep     -> MUST produce 50+ roles

FORBIDDEN: fewer than the lower bound of T1-COUNT-FLOOR.

2.2 -- Role Files

Write .craft/roles/{area}/{role}.md per role.
MUST use at least 2 area subdirectories.
Every role file MUST contain: orientation, lens, expertise, scope, collaborates_with
FORBIDDEN: any missing field.

2.3 -- Inertia-Advocate

MUST include inertia-advocate. FORBIDDEN: omitting it.

Scope MUST be the verbatim template text for T1-IA-SCOPE-KEY from Phase 1 record:
  LOW:
    "Monitor adoption signals and flag emerging resistance patterns. No structural
    intervention warranted at current pressure level."
  MODERATE:
    "Actively surface status-quo arguments in reviews. Ensure inertia costs are
    quantified before each major design commitment."
  ELEVATED:
    "Challenge every architectural constraint inherited from prior systems. Document
    each instance where the team defaults to familiar patterns over evidence-based
    choices."
  HIGH:
    "Veto any design decision that cannot demonstrate superiority over the current
    approach. The burden of proof for change is maximal; operate as the primary
    structural check on premature commitment."

FORBIDDEN: paraphrasing. FORBIDDEN: composing a new scope.

OUTBOUND GATE -- emit record block now. PHASE-ORDERING-GUARD is the first field.

=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD:    FORBIDDEN: Phase 3 begins before this block is emitted.
T2-ROLE-COUNT:           [number]
T2-AREA-COUNT:           [number]
T2-COUNT-CHECK:          [PASS | FAIL]
T2-IA-PRESENT:           [YES | NO]
T2-IA-SCOPE-FIRST-WORDS: [verbatim first 8 words of scope applied]
===

---

PHASE 3 -- BUILD ORG-CHART.MD

INBOUND CONTRACT: FORBIDDEN: Phase 3 begins before Phase 2 record block is emitted.
FORBIDDEN: proceeding if T2-COUNT-CHECK = FAIL or T2-IA-PRESENT = NO.
MUST read: T1-VERDICT, T1-PRESSURE from Phase 1 record block.

Write org-chart.md:

SECTION 1: ASCII HIERARCHY DIAGRAM
MUST show at least 2 org levels with box-and-line ASCII. FORBIDDEN: flat name list.

SECTION 2: HEADCOUNT BY AREA TABLE
MUST include: Area | Headcount | Key Roles | Decides | Escalates
FORBIDDEN: missing Decides or Escalates. FORBIDDEN: merging them.

SECTION 3: LEVEL DISTRIBUTION
Role distribution across levels.

SECTION 4: INERTIA VERDICT BLOCK
  FLAT-CASE-PRESSURE: [T1-PRESSURE]
  VERDICT: [T1-VERDICT]
Only one verdict. Both is an error. Neither is an error.

SECTION 5: ANTI-PATTERN CATEGORY DERIVATION
  CAN-OPERATE-FLAT    -> MUST use cat-2/cat-3. FORBIDDEN: cat-1/cat-4.
  STRUCTURE-WARRANTED -> MUST use cat-1/cat-4. FORBIDDEN: cat-2/cat-3.
Record: T3-ANTI-PATTERN-PATH

SECTION 6: ANTI-PATTERN WATCH TABLE
  Why It Applies Here: MUST begin [element name] (cat-N) -- [sentence]
  Mitigation: MUST contain specific remediation action. FORBIDDEN: format instructions.

SECTION 7: OPERATING RHYTHM TABLE
At least 3 rows: ROB + shiproom + governance. FORBIDDEN: combining rows.

SECTION 8: COMMITTEE CHARTERS
Per governance meeting: Name, Cadence, Owner, Participants, Quorum: [N of M]
FORBIDDEN: Quorum without N of M fraction.

SECTION 9: ORG EVOLUTION ROADMAP
Row 1: headcount threshold. Row 2: different category. FORBIDDEN: two headcount rows.

OUTBOUND GATE -- emit record block now. PHASE-ORDERING-GUARD is the first field.

=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD:    FORBIDDEN: Phase 4 begins before this block is emitted.
T3-ORG-CHART-SECTIONS:   [sections produced, comma-separated]
T3-ANTI-PATTERN-PATH:    [CAN-OPERATE-FLAT: cat-2/cat-3 | STRUCTURE-WARRANTED: cat-1/cat-4]
T3-VERDICT-EMITTED:      [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T3-EVOLUTION-ROW-TYPES:  [Row 1 type, Row 2 type]
===

---

PHASE 4 -- VERIFY

INBOUND CONTRACT: FORBIDDEN: Phase 4 begins before Phase 3 record block is emitted.

Verify:
  T1-VERDICT = T3-VERDICT-EMITTED               -> T4-VERDICT-CONSISTENT
  T2-COUNT-CHECK = PASS                          -> T4-COUNT-CONSISTENT
  T2-IA-PRESENT = YES                            -> T4-IA-PRESENT
  T2-IA-SCOPE-FIRST-WORDS is verbatim match
    for T1-IA-SCOPE-KEY template                 -> T4-IA-SCOPE-VERBATIM

FORBIDDEN: declaring completion if any check = FAIL.

OUTBOUND GATE -- emit record block now. PHASE-ORDERING-GUARD is the first field.

=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD:   FORBIDDEN: declaring completion before this block is emitted.
T4-VERDICT-CONSISTENT:  [PASS | FAIL]
T4-COUNT-CONSISTENT:    [PASS | FAIL]
T4-IA-PRESENT:          [PASS | FAIL]
T4-IA-SCOPE-VERBATIM:   [PASS | FAIL]
T4-FINAL-STATUS:        [COMPLETE | REQUIRES-CORRECTION]
===
```

---

## V-03 -- Inertia-First Verdict Declaration

**axis:** FLAT-CASE-PRESSURE + VERDICT + IA scope template selection are all Phase 1
outputs; Phase 2 consumes T1-IA-SCOPE-KEY as a named typed gate variable
**hypothesis:** Moving the IA scope template selection into Phase 1's gate contract
(alongside T1-VERDICT) means Phase 2 does not need to re-derive which template to
apply -- it reads T1-IA-SCOPE-KEY from the record block and copies the template
verbatim. The derivation is gated, not advisory. C-11 and C-17 become structural
consequences of the gate rather than standalone instructions that can be missed.

---

```
You are running `/org-build {topic}`.

The inertia-advocate speaks first. Before any role is written or any diagram is
drawn, the status quo makes its case. The structural decision -- CAN-OPERATE-FLAT
or STRUCTURE-WARRANTED -- is Phase 1's primary output. The inertia-advocate's scope
template is selected in Phase 1 and recorded as a gate variable consumed by Phase 2.

Every phase boundary is anchored by a named record block. PHASE-ORDERING-GUARD is
always the first field inside the block.

---

PHASE 1 -- STATUS QUO SPEAKS

Read all provided inputs.

1.1 -- Depth Flag

  `--depth deep` passed  -> T1-DEPTH-FLAG = deep
  otherwise              -> T1-DEPTH-FLAG = standard

COUNT FLOOR BINDING -- Phase 1 gate output, not Phase 2 default:
  T1-DEPTH-FLAG = standard -> T1-COUNT-FLOOR = 20-30
  T1-DEPTH-FLAG = deep     -> T1-COUNT-FLOOR = 50+

FORBIDDEN: declaring T1-DEPTH-FLAG without T1-COUNT-FLOOR.
FORBIDDEN: encoding this binding anywhere except Phase 1.

1.2 -- Flat Case

Document coordination mechanisms already in use:
  | Mechanism Name | Type | Frequency / Participants |
  Type closed set: Channel / Informal Role / Recurring Cadence / Shared Artifact

MUST include at least 2 rows.
Name the single coordination failure this flat arrangement cannot resolve.
MUST name an observable failure mode -- blocked decision, missed SLA, knowledge silo.
FORBIDDEN: "the team is growing" without naming a specific failure.

1.3 -- FLAT-CASE-PRESSURE Rating

Assign from: LOW | MODERATE | ELEVATED | HIGH
  LOW:      no observable failures; flat team functions well
  MODERATE: strain under load; friction without breakdown
  ELEVATED: observable failures or blocked decisions
  HIGH:     systematic coordination breakdown

MUST cite the specific mechanism or failure that drove the rating.

1.4 -- Verdict

Assign exactly one:
  CAN-OPERATE-FLAT
  STRUCTURE-WARRANTED

Only one verdict. Both is an error. Neither is an error.
FORBIDDEN: writing both. FORBIDDEN: omitting both.
MUST reference FLAT-CASE-PRESSURE by name in verdict reasoning.

1.5 -- IA Scope Template Selection (Phase 1 gate output)

The inertia-advocate scope is determined here -- before Phase 2 writes any role file.
Select the verbatim template keyed to T1-PRESSURE:

  LOW:
    "Monitor adoption signals and flag emerging resistance patterns. No structural
    intervention warranted at current pressure level."
  MODERATE:
    "Actively surface status-quo arguments in reviews. Ensure inertia costs are
    quantified before each major design commitment."
  ELEVATED:
    "Challenge every architectural constraint inherited from prior systems. Document
    each instance where the team defaults to familiar patterns over evidence-based
    choices."
  HIGH:
    "Veto any design decision that cannot demonstrate superiority over the current
    approach. The burden of proof for change is maximal; operate as the primary
    structural check on premature commitment."

Record: T1-IA-SCOPE-KEY = [LOW | MODERATE | ELEVATED | HIGH]
FORBIDDEN: selecting a template keyed to a rating other than T1-PRESSURE.
FORBIDDEN: beginning Phase 2 before emitting the Phase 1 record block.

=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD:    FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG:           [standard | deep]
T1-COUNT-FLOOR:          [20-30 | 50+]
T1-PRESSURE:             [LOW | MODERATE | ELEVATED | HIGH]
T1-VERDICT:              [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T1-IA-SCOPE-KEY:         [LOW | MODERATE | ELEVATED | HIGH]
T1-MECHANISM-COUNT:      [number]
T1-NAMED-FAILURE:        [one-line description of the coordination failure named above]
===

---

PHASE 2 -- ENUMERATE ROLES

INBOUND CONTRACT: FORBIDDEN: Phase 2 begins before Phase 1 record block is emitted.
MUST read from Phase 1 record block:
  T1-DEPTH-FLAG, T1-COUNT-FLOOR, T1-IA-SCOPE-KEY, T1-VERDICT
FORBIDDEN: executing this phase if any of those variables are unresolved.

2.1 -- Role Count

Role count is bound to T1-COUNT-FLOOR from Phase 1 record:
  T1-DEPTH-FLAG = standard -> MUST produce 20-30 roles
  T1-DEPTH-FLAG = deep     -> MUST produce 50+ roles

FORBIDDEN: fewer than the lower bound. FORBIDDEN: exceeding upper bound by >20% without deep flag.

2.2 -- Role Files

Write .craft/roles/{area}/{role}.md per role.
MUST use at least 2 area subdirectories.

Every role file MUST contain:
  orientation:       [people | product | process | technical]
  lens:              [cognitive or professional filter]
  expertise:         [domain knowledge]
  scope:             [authority and decision boundary]
  collaborates_with: [list of role names]

FORBIDDEN: any missing field.

2.3 -- Inertia-Advocate (Phase 1 scope key applied here)

MUST include inertia-advocate. FORBIDDEN: omitting it.

Read T1-IA-SCOPE-KEY from Phase 1 record block.
The inertia-advocate scope MUST be the verbatim template for that key:
  LOW:
    "Monitor adoption signals and flag emerging resistance patterns. No structural
    intervention warranted at current pressure level."
  MODERATE:
    "Actively surface status-quo arguments in reviews. Ensure inertia costs are
    quantified before each major design commitment."
  ELEVATED:
    "Challenge every architectural constraint inherited from prior systems. Document
    each instance where the team defaults to familiar patterns over evidence-based
    choices."
  HIGH:
    "Veto any design decision that cannot demonstrate superiority over the current
    approach. The burden of proof for change is maximal; operate as the primary
    structural check on premature commitment."

FORBIDDEN: paraphrasing. FORBIDDEN: composing a new scope.
FORBIDDEN: applying a template keyed to a different rating than T1-IA-SCOPE-KEY.

Count role files. Verify within T1-COUNT-FLOOR range.
FORBIDDEN: beginning Phase 3 before emitting the Phase 2 record block.

=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD:    FORBIDDEN: Phase 3 begins before this block is emitted.
T2-ROLE-COUNT:           [number]
T2-AREA-COUNT:           [number]
T2-COUNT-CHECK:          [PASS | FAIL]
T2-IA-PRESENT:           [YES | NO]
T2-IA-SCOPE-FIRST-WORDS: [verbatim first 8 words of scope applied]
T2-IA-KEY-APPLIED:       [LOW | MODERATE | ELEVATED | HIGH]
===

---

PHASE 3 -- BUILD ORG-CHART.MD

INBOUND CONTRACT: FORBIDDEN: Phase 3 begins before Phase 2 record block is emitted.
FORBIDDEN: proceeding if T2-COUNT-CHECK = FAIL or T2-IA-PRESENT = NO.
MUST read T1-VERDICT and T1-PRESSURE from Phase 1 record block.

Write org-chart.md with sections in order:

SECTION 1: ASCII HIERARCHY DIAGRAM
MUST show at least 2 org levels. FORBIDDEN: flat name list.

SECTION 2: HEADCOUNT BY AREA TABLE
MUST include: Area | Headcount | Key Roles | Decides | Escalates
FORBIDDEN: missing or merged Decides/Escalates columns.

SECTION 3: LEVEL DISTRIBUTION

SECTION 4: INERTIA VERDICT BLOCK
  FLAT-CASE-PRESSURE: [T1-PRESSURE]
  VERDICT: [T1-VERDICT]
Only one verdict. Both is an error. Neither is an error.

SECTION 5: ANTI-PATTERN CATEGORY DERIVATION
  CAN-OPERATE-FLAT    -> MUST use cat-2/cat-3. FORBIDDEN: cat-1/cat-4.
  STRUCTURE-WARRANTED -> MUST use cat-1/cat-4. FORBIDDEN: cat-2/cat-3.

SECTION 6: ANTI-PATTERN WATCH TABLE
  Why It Applies Here: MUST begin [element name] (cat-N) -- [sentence]
  Mitigation: MUST contain specific remediation action.

SECTION 7: OPERATING RHYTHM TABLE -- at least 3 rows: ROB + shiproom + governance.

SECTION 8: COMMITTEE CHARTERS -- per governance meeting: all 5 fields, Quorum: [N of M]

SECTION 9: ORG EVOLUTION ROADMAP
Row 1: headcount threshold. Row 2: different category. FORBIDDEN: two headcount rows.

FORBIDDEN: beginning Phase 4 before emitting the Phase 3 record block.

=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD:    FORBIDDEN: Phase 4 begins before this block is emitted.
T3-ORG-CHART-SECTIONS:   [sections produced]
T3-ANTI-PATTERN-PATH:    [CAN-OPERATE-FLAT: cat-2/cat-3 | STRUCTURE-WARRANTED: cat-1/cat-4]
T3-VERDICT-EMITTED:      [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T3-EVOLUTION-ROW-TYPES:  [Row 1 type, Row 2 type]
===

---

PHASE 4 -- VERIFY

INBOUND CONTRACT: FORBIDDEN: Phase 4 begins before Phase 3 record block is emitted.

Verify:
  T1-VERDICT = T3-VERDICT-EMITTED                    -> T4-VERDICT-CONSISTENT
  T2-COUNT-CHECK = PASS                              -> T4-COUNT-CONSISTENT
  T2-IA-PRESENT = YES                                -> T4-IA-PRESENT
  T2-IA-KEY-APPLIED = T1-IA-SCOPE-KEY                -> T4-KEY-MATCH
  T2-IA-SCOPE-FIRST-WORDS verbatim match for key     -> T4-IA-SCOPE-VERBATIM

FORBIDDEN: declaring completion if any check = FAIL.

=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD:   FORBIDDEN: declaring completion before this block is emitted.
T4-VERDICT-CONSISTENT:  [PASS | FAIL]
T4-COUNT-CONSISTENT:    [PASS | FAIL]
T4-IA-PRESENT:          [PASS | FAIL]
T4-KEY-MATCH:           [PASS | FAIL]
T4-IA-SCOPE-VERBATIM:   [PASS | FAIL]
T4-FINAL-STATUS:        [COMPLETE | REQUIRES-CORRECTION]
===
```

---

## V-04 -- Count-Conditional + Record Anchor + Phrasing Register

**axis:** all three mechanisms combined with full MUST/FORBIDDEN register
**hypothesis:** When every constraint uses MUST or FORBIDDEN, the count-floor
binding (C-27) and PHASE-ORDERING-GUARD-as-first-field (C-28) become structurally
equivalent to any other constraint: each is a named variable governed by an
imperative. The uniform register makes partial compliance impossible -- a model
that softens one constraint softens all of them.

---

```
You are running `/org-build {topic}`.

CONSTRAINT REGISTER: Every rule in this prompt uses MUST (required) or FORBIDDEN
(prohibited). Advisory language -- "should", "prefer", "typically", "consider" --
does not appear in constraint contexts. A constraint is binary: satisfied or violated.

RECORD BLOCK ARCHITECTURE: Every phase produces a named record block. PHASE-ORDERING-GUARD
is always the first field inside the block. It carries the FORBIDDEN for the next phase.
FORBIDDEN: any record block that does not begin with PHASE-ORDERING-GUARD as its first field.

---

PHASE 1 -- ASSESS

MUST read all provided inputs before acting.

1.1 -- Depth Flag

MUST classify:
  `--depth deep` passed  -> T1-DEPTH-FLAG = deep
  otherwise              -> T1-DEPTH-FLAG = standard

MUST bind count floor to T1-DEPTH-FLAG as a Phase 1 gate output:
  T1-DEPTH-FLAG = standard -> T1-COUNT-FLOOR = 20-30
  T1-DEPTH-FLAG = deep     -> T1-COUNT-FLOOR = 50+

FORBIDDEN: declaring T1-DEPTH-FLAG without declaring T1-COUNT-FLOOR.
FORBIDDEN: a flat count range not derived from T1-DEPTH-FLAG.
FORBIDDEN: placing the count-floor binding outside Phase 1.

1.2 -- Inertia Assessment

MUST produce a coordination mechanism table:
  | Mechanism Name | Type | Frequency / Participants |

Type MUST be exactly one from: Channel / Informal Role / Recurring Cadence / Shared Artifact
FORBIDDEN: Type values outside this closed set.
MUST include minimum 2 data rows.
FORBIDDEN: fewer than 2 rows.

MUST name the single coordination failure the flat arrangement cannot resolve.
MUST name an observable failure mode.
FORBIDDEN: "the team is growing" without a named failure.

1.3 -- FLAT-CASE-PRESSURE Rating

MUST assign from the closed set: LOW | MODERATE | ELEVATED | HIGH
  LOW:      no observable failures
  MODERATE: strain under load; no failures
  ELEVATED: observable failures or blocked decisions
  HIGH:     systematic breakdown
FORBIDDEN: values outside this closed set.

1.4 -- Verdict

MUST write exactly one verdict:
  CAN-OPERATE-FLAT
  STRUCTURE-WARRANTED
FORBIDDEN: writing both verdicts. Both is an error.
FORBIDDEN: omitting both verdicts. Neither is an error.
MUST reference FLAT-CASE-PRESSURE by name in the verdict reasoning.

1.5 -- IA Scope Template Selection

MUST select the verbatim template keyed to T1-PRESSURE:
  LOW:
    "Monitor adoption signals and flag emerging resistance patterns. No structural
    intervention warranted at current pressure level."
  MODERATE:
    "Actively surface status-quo arguments in reviews. Ensure inertia costs are
    quantified before each major design commitment."
  ELEVATED:
    "Challenge every architectural constraint inherited from prior systems. Document
    each instance where the team defaults to familiar patterns over evidence-based
    choices."
  HIGH:
    "Veto any design decision that cannot demonstrate superiority over the current
    approach. The burden of proof for change is maximal; operate as the primary
    structural check on premature commitment."

FORBIDDEN: applying a template keyed to a different rating than T1-PRESSURE.
FORBIDDEN: paraphrasing the selected template.
MUST record: T1-IA-SCOPE-KEY = [LOW | MODERATE | ELEVATED | HIGH]
FORBIDDEN: beginning Phase 2 before emitting the Phase 1 record block.

=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD:  FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG:         [standard | deep]
T1-COUNT-FLOOR:        [20-30 | 50+]
T1-PRESSURE:           [LOW | MODERATE | ELEVATED | HIGH]
T1-VERDICT:            [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T1-IA-SCOPE-KEY:       [LOW | MODERATE | ELEVATED | HIGH]
T1-MECHANISM-COUNT:    [number]
===

IA ROLE FILE SKELETON (pre-print before Phase 2 runs -- slots keyed to gate variables):

  .craft/roles/inertia/inertia-advocate.md:
    orientation: [T1-VERDICT -> CAN-OPERATE-FLAT: "process" | STRUCTURE-WARRANTED: "technical"]
    lens:        status-quo challenge -- question every structural assumption
    expertise:   coordination pattern recognition; inertia cost quantification
    scope:       {{T1-IA-SCOPE-KEY-TEMPLATE}}
    collaborates_with: [T2-ROLE-MANIFEST-first-3-roles]

{{T1-IA-SCOPE-KEY-TEMPLATE}} maps to the verbatim template for T1-IA-SCOPE-KEY above.
FORBIDDEN: any deviation from the verbatim template text when filling this slot.

---

PHASE 2 -- ENUMERATE ROLES

INBOUND CONTRACT: FORBIDDEN: Phase 2 begins before Phase 1 record block is emitted.
MUST read: T1-DEPTH-FLAG, T1-COUNT-FLOOR, T1-IA-SCOPE-KEY from Phase 1 record block.
FORBIDDEN: executing this phase if any of those variables are unresolved.

2.1 -- Role Count

MUST produce exactly the count bound to T1-COUNT-FLOOR:
  T1-DEPTH-FLAG = standard -> MUST produce 20-30 roles
  T1-DEPTH-FLAG = deep     -> MUST produce 50+ roles

FORBIDDEN: fewer than the lower bound.
FORBIDDEN: exceeding upper bound by >20% without deep flag.

2.2 -- Role Files

MUST write one .craft/roles/{area}/{role}.md per role.
MUST group under area subdirectories.
MUST use at least 2 area subdirectories.
FORBIDDEN: all roles flat without area grouping.

MUST include in every role file:
  orientation:       [people | product | process | technical]
  lens:              [filter this role applies]
  expertise:         [domain knowledge]
  scope:             [authority and decision boundary]
  collaborates_with: [role names]
FORBIDDEN: any role file missing one or more of these five fields.

2.3 -- Inertia-Advocate

MUST include inertia-advocate. FORBIDDEN: omitting it.

MUST apply the verbatim IA scope template for T1-IA-SCOPE-KEY from Phase 1 record:
  LOW:
    "Monitor adoption signals and flag emerging resistance patterns. No structural
    intervention warranted at current pressure level."
  MODERATE:
    "Actively surface status-quo arguments in reviews. Ensure inertia costs are
    quantified before each major design commitment."
  ELEVATED:
    "Challenge every architectural constraint inherited from prior systems. Document
    each instance where the team defaults to familiar patterns over evidence-based
    choices."
  HIGH:
    "Veto any design decision that cannot demonstrate superiority over the current
    approach. The burden of proof for change is maximal; operate as the primary
    structural check on premature commitment."

FORBIDDEN: paraphrasing.
FORBIDDEN: composing a new scope.
FORBIDDEN: applying a template keyed to a different rating than T1-IA-SCOPE-KEY.

MUST count role files after writing.
MUST verify count is within T1-COUNT-FLOOR range.
FORBIDDEN: proceeding to record block if count is below the lower bound.
FORBIDDEN: beginning Phase 3 before emitting the Phase 2 record block.

=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD:    FORBIDDEN: Phase 3 begins before this block is emitted.
T2-ROLE-COUNT:           [number]
T2-AREA-COUNT:           [number]
T2-COUNT-CHECK:          [PASS | FAIL]
T2-IA-PRESENT:           [YES | NO]
T2-IA-SCOPE-FIRST-WORDS: [verbatim first 8 words of scope applied]
===

---

PHASE 3 -- BUILD ORG-CHART.MD

INBOUND CONTRACT: FORBIDDEN: Phase 3 begins before Phase 2 record block is emitted.
FORBIDDEN: proceeding if T2-COUNT-CHECK = FAIL.
FORBIDDEN: proceeding if T2-IA-PRESENT = NO.
MUST read: T1-VERDICT, T1-PRESSURE from Phase 1 record block.

MUST write org-chart.md with all sections in order:

SECTION 1: ASCII HIERARCHY DIAGRAM
MUST render box-and-line ASCII with at least 2 org levels.
FORBIDDEN: flat name list without hierarchy.

SECTION 2: HEADCOUNT BY AREA TABLE
MUST include: Area | Headcount | Key Roles | Decides | Escalates
FORBIDDEN: omitting Decides column.
FORBIDDEN: omitting Escalates column.
FORBIDDEN: merging Decides and Escalates.

SECTION 3: LEVEL DISTRIBUTION
MUST show role distribution across levels.

SECTION 4: INERTIA VERDICT BLOCK
MUST emit:
  FLAT-CASE-PRESSURE: [T1-PRESSURE]
  VERDICT: [T1-VERDICT]
FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Both is an error.
FORBIDDEN: omitting the verdict. Neither is an error.

SECTION 5: ANTI-PATTERN CATEGORY DERIVATION
MUST derive from T1-VERDICT:
  T1-VERDICT = CAN-OPERATE-FLAT:
    MUST use cat-2 (coordination overhead) and cat-3 (role ambiguity).
    FORBIDDEN: cat-1 in this path.
    FORBIDDEN: cat-4 in this path.
  T1-VERDICT = STRUCTURE-WARRANTED:
    MUST use cat-1 (span of control) and cat-4 (reporting hierarchy).
    FORBIDDEN: cat-2 in this path.
    FORBIDDEN: cat-3 in this path.
MUST record: T3-ANTI-PATTERN-PATH

SECTION 6: ANTI-PATTERN WATCH TABLE
Columns: Anti-Pattern | Why It Applies Here | Mitigation
MUST open every "Why It Applies Here" cell with: [element name] (cat-N) -- [sentence]
FORBIDDEN: plain prose without (cat-N) citation.
FORBIDDEN: cat codes outside T3-ANTI-PATTERN-PATH.
MUST include a specific remediation action in every Mitigation cell.
FORBIDDEN: format instructions or column-structure guidance in Mitigation cells.

SECTION 7: OPERATING RHYTHM TABLE
MUST include: Cadence | Frequency | Owner | Purpose
MUST include at least 3 rows: ROB + shiproom + governance.
FORBIDDEN: combining two meetings into one row.

SECTION 8: COMMITTEE CHARTERS
MUST write one charter per governance meeting.
Each charter MUST include: Name, Cadence, Owner, Participants, Quorum: [N of M]
FORBIDDEN: Quorum without N of M fraction.

SECTION 9: ORG EVOLUTION ROADMAP
MUST include at least 2 rows: | Trigger | Structural Change | Type |
Row 1 MUST be headcount threshold.
Row 2 MUST be a different category.
FORBIDDEN: two headcount threshold rows.

FORBIDDEN: beginning Phase 4 before emitting the Phase 3 record block.

=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD:    FORBIDDEN: Phase 4 begins before this block is emitted.
T3-ORG-CHART-SECTIONS:   [sections, comma-separated]
T3-ANTI-PATTERN-PATH:    [CAN-OPERATE-FLAT: cat-2/cat-3 | STRUCTURE-WARRANTED: cat-1/cat-4]
T3-VERDICT-EMITTED:      [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T3-EVOLUTION-ROW-TYPES:  [Row 1 type, Row 2 type]
===

---

PHASE 4 -- VERIFY

INBOUND CONTRACT: FORBIDDEN: Phase 4 begins before Phase 3 record block is emitted.

MUST check:
  T1-VERDICT = T3-VERDICT-EMITTED               -> T4-VERDICT-CONSISTENT
  T2-COUNT-CHECK = PASS                          -> T4-COUNT-CONSISTENT
  T2-IA-PRESENT = YES                            -> T4-IA-PRESENT
  T2-IA-SCOPE-FIRST-WORDS is verbatim match
    for T1-IA-SCOPE-KEY template                 -> T4-IA-SCOPE-VERBATIM

FORBIDDEN: declaring completion if any check = FAIL.
MUST correct all failing checks before recording COMPLETE.

=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD:   FORBIDDEN: declaring completion before this block is emitted.
T4-VERDICT-CONSISTENT:  [PASS | FAIL]
T4-COUNT-CONSISTENT:    [PASS | FAIL]
T4-IA-PRESENT:          [PASS | FAIL]
T4-IA-SCOPE-VERBATIM:   [PASS | FAIL]
T4-FINAL-STATUS:        [COMPLETE | REQUIRES-CORRECTION]
===
```

---

## V-05 -- Count-Conditional + Record Anchor + Unification Architecture

**axis:** record block as explicit unification artifact (C-26) with in-block
commentary; IA role file skeleton with named gate-variable slots (C-22)
**hypothesis:** Designing each record block as the unification artifact -- with
in-block commentary stating that a reader who sees only this block can derive
the gate schema, ordering constraint anchor, and materialization checkpoint --
makes PHASE-ORDERING-GUARD-as-first-field the natural consequence of the
unification claim. A block that claims unification but places the guard in
preamble prose is internally contradictory; the structural commentary enforces
the structural requirement.

---

```
You are running `/org-build {topic}`.

UNIFICATION ARCHITECTURE: Every phase boundary is anchored by a named record block.
Each record block is the unification artifact for that phase: one structure that
simultaneously (1) declares the typed output variables produced by the phase,
(2) anchors the ordering constraint -- PHASE-ORDERING-GUARD, always the first field,
carries the FORBIDDEN directive naming the next phase, (3) materializes the variable
values as auditable checkpoints before downstream phases consume them. A reader who
sees only the record block can derive the gate schema, the ordering constraint, and
the materialization checkpoint without reading surrounding instructions. This property
is structural, not claimed in prose: it holds because PHASE-ORDERING-GUARD is the
first field in the block and the variable values are materialized inside the block.

PHASE BOUNDARY RULE: Every phase has both an outbound gate (FORBIDDEN before emitting
the record block) and an inbound contract (FORBIDDEN before executing this phase,
referencing the prior record block). Both directions are required at every boundary.

---

PHASE 1 -- ASSESS

INBOUND: No prior record block required. This phase begins at invocation.

Read all provided inputs.

1.1 -- Depth Flag

  `--depth deep` passed  -> T1-DEPTH-FLAG = deep
  otherwise              -> T1-DEPTH-FLAG = standard

DEPTH-FLAG-CONDITIONAL COUNT FLOOR -- Phase 1 typed output, not Phase 2 default:
  T1-DEPTH-FLAG = standard -> T1-COUNT-FLOOR = 20-30
  T1-DEPTH-FLAG = deep     -> T1-COUNT-FLOOR = 50+

FORBIDDEN: declaring T1-DEPTH-FLAG without T1-COUNT-FLOOR.
FORBIDDEN: a flat count range not derived from T1-DEPTH-FLAG.
FORBIDDEN: encoding this binding in a phase other than Phase 1.

1.2 -- Inertia Assessment

Document flat-team coordination mechanisms:
  | Mechanism Name | Type | Frequency / Participants |
  Type closed set: Channel / Informal Role / Recurring Cadence / Shared Artifact
MUST include at least 2 rows.
Name the single coordination failure this arrangement cannot resolve.

1.3 -- FLAT-CASE-PRESSURE

Assign from: LOW | MODERATE | ELEVATED | HIGH

1.4 -- Verdict

Assign exactly one:
  CAN-OPERATE-FLAT
  STRUCTURE-WARRANTED

Only one verdict. Both is an error. Neither is an error.
FORBIDDEN: writing both. FORBIDDEN: omitting both.

1.5 -- IA Scope Template Selection

Select verbatim template keyed to T1-PRESSURE:
  LOW:
    "Monitor adoption signals and flag emerging resistance patterns. No structural
    intervention warranted at current pressure level."
  MODERATE:
    "Actively surface status-quo arguments in reviews. Ensure inertia costs are
    quantified before each major design commitment."
  ELEVATED:
    "Challenge every architectural constraint inherited from prior systems. Document
    each instance where the team defaults to familiar patterns over evidence-based
    choices."
  HIGH:
    "Veto any design decision that cannot demonstrate superiority over the current
    approach. The burden of proof for change is maximal; operate as the primary
    structural check on premature commitment."

Record: T1-IA-SCOPE-KEY = [LOW | MODERATE | ELEVATED | HIGH]
FORBIDDEN: template keyed to a rating other than T1-PRESSURE.

IA ROLE FILE SKELETON (prefill before Phase 2 -- slots keyed to Phase 1 gate variables):

  .craft/roles/inertia/inertia-advocate.md:
    orientation: [T1-VERDICT -> CAN-OPERATE-FLAT: "process" | STRUCTURE-WARRANTED: "technical"]
    lens:        status-quo challenge -- interrogate every structural assumption before adoption
    expertise:   coordination pattern recognition; inertia cost quantification; adoption signal reading
    scope:       {{T1-IA-SCOPE-KEY-TEMPLATE}}
    collaborates_with: [T2-ROLE-MANIFEST-first-3-roles]

{{T1-IA-SCOPE-KEY-TEMPLATE}} is the slot name for the verbatim template text selected above.
A reader who knows only T1-IA-SCOPE-KEY can fill this slot without ambiguity.
FORBIDDEN: any deviation from the verbatim template when filling {{T1-IA-SCOPE-KEY-TEMPLATE}}.

OUTBOUND GATE: FORBIDDEN: beginning Phase 2 before emitting the record block below.

The record block below is the Phase 1 unification artifact. From this block alone:
  - Gate schema: T1-DEPTH-FLAG, T1-COUNT-FLOOR, T1-PRESSURE, T1-VERDICT, T1-IA-SCOPE-KEY
  - Ordering constraint: PHASE-ORDERING-GUARD (first field) carries the FORBIDDEN for Phase 2
  - Materialization checkpoint: filled values are the observable Phase 1 gate state

=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD:  FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG:         [standard | deep]
T1-COUNT-FLOOR:        [20-30 | 50+]
T1-PRESSURE:           [LOW | MODERATE | ELEVATED | HIGH]
T1-VERDICT:            [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T1-IA-SCOPE-KEY:       [LOW | MODERATE | ELEVATED | HIGH]
T1-MECHANISM-COUNT:    [number]
===

---

PHASE 2 -- ENUMERATE ROLES

INBOUND CONTRACT: FORBIDDEN: Phase 2 begins before Phase 1 record block is emitted.
MUST read from Phase 1 record block: T1-DEPTH-FLAG, T1-COUNT-FLOOR, T1-IA-SCOPE-KEY.
FORBIDDEN: executing this phase if any of those variables are unresolved.

2.1 -- Role Count

MUST produce count bound to T1-COUNT-FLOOR from Phase 1 record:
  T1-DEPTH-FLAG = standard -> MUST produce 20-30 roles
  T1-DEPTH-FLAG = deep     -> MUST produce 50+ roles

FORBIDDEN: fewer than the lower bound.

2.2 -- Role Files

MUST write .craft/roles/{area}/{role}.md per role.
MUST use at least 2 area subdirectories.

Every role file MUST contain: orientation, lens, expertise, scope, collaborates_with
FORBIDDEN: any missing field.

2.3 -- Inertia-Advocate

MUST include inertia-advocate. FORBIDDEN: omitting it.

Fill the IA role file skeleton from Phase 1 using T1-IA-SCOPE-KEY from Phase 1 record:
  LOW:
    "Monitor adoption signals and flag emerging resistance patterns. No structural
    intervention warranted at current pressure level."
  MODERATE:
    "Actively surface status-quo arguments in reviews. Ensure inertia costs are
    quantified before each major design commitment."
  ELEVATED:
    "Challenge every architectural constraint inherited from prior systems. Document
    each instance where the team defaults to familiar patterns over evidence-based
    choices."
  HIGH:
    "Veto any design decision that cannot demonstrate superiority over the current
    approach. The burden of proof for change is maximal; operate as the primary
    structural check on premature commitment."

FORBIDDEN: paraphrase. FORBIDDEN: composition. FORBIDDEN: wrong template key.

Count role files. Verify against T1-COUNT-FLOOR.
OUTBOUND GATE: FORBIDDEN: beginning Phase 3 before emitting the record block below.

The record block below is the Phase 2 unification artifact. From this block alone:
  - Gate schema: T2-ROLE-COUNT, T2-AREA-COUNT, T2-COUNT-CHECK, T2-IA-PRESENT, T2-IA-SCOPE-FIRST-WORDS
  - Ordering constraint: PHASE-ORDERING-GUARD (first field) carries the FORBIDDEN for Phase 3
  - Materialization checkpoint: values consumed by Phase 3's input contract

=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD:    FORBIDDEN: Phase 3 begins before this block is emitted.
T2-ROLE-COUNT:           [number]
T2-AREA-COUNT:           [number]
T2-COUNT-CHECK:          [PASS | FAIL]
T2-IA-PRESENT:           [YES | NO]
T2-IA-SCOPE-FIRST-WORDS: [verbatim first 8 words of scope applied]
===

---

PHASE 3 -- BUILD ORG-CHART.MD

INBOUND CONTRACT: FORBIDDEN: Phase 3 begins before Phase 2 record block is emitted.
FORBIDDEN: proceeding if T2-COUNT-CHECK = FAIL or T2-IA-PRESENT = NO.
MUST read: T1-VERDICT, T1-PRESSURE from Phase 1 record block.

Write org-chart.md:

SECTION 1: ASCII HIERARCHY DIAGRAM -- at least 2 org levels. FORBIDDEN: flat list.

SECTION 2: HEADCOUNT BY AREA TABLE
MUST include: Area | Headcount | Key Roles | Decides | Escalates
FORBIDDEN: missing or merged Decides/Escalates.

SECTION 3: LEVEL DISTRIBUTION

SECTION 4: INERTIA VERDICT BLOCK
  FLAT-CASE-PRESSURE: [T1-PRESSURE]
  VERDICT: [T1-VERDICT]
Only one verdict. Both is an error. Neither is an error.

SECTION 5: ANTI-PATTERN CATEGORY DERIVATION
  CAN-OPERATE-FLAT    -> MUST use cat-2/cat-3. FORBIDDEN: cat-1/cat-4.
  STRUCTURE-WARRANTED -> MUST use cat-1/cat-4. FORBIDDEN: cat-2/cat-3.

SECTION 6: ANTI-PATTERN WATCH TABLE
  Why It Applies Here: MUST begin [element name] (cat-N) -- [sentence]
  Mitigation: MUST contain specific remediation action. FORBIDDEN: format instructions.

SECTION 7: OPERATING RHYTHM TABLE -- at least 3 rows: ROB + shiproom + governance.

SECTION 8: COMMITTEE CHARTERS -- per governance meeting, all 5 fields, Quorum: [N of M]

SECTION 9: ORG EVOLUTION ROADMAP
Row 1: headcount threshold. Row 2: different category. FORBIDDEN: two headcount rows.

OUTBOUND GATE: FORBIDDEN: beginning Phase 4 before emitting the record block below.

The record block below is the Phase 3 unification artifact. From this block alone:
  - Gate schema: T3-ORG-CHART-SECTIONS, T3-ANTI-PATTERN-PATH, T3-VERDICT-EMITTED
  - Ordering constraint: PHASE-ORDERING-GUARD (first field) carries the FORBIDDEN for Phase 4
  - Materialization checkpoint: values consumed by Phase 4's consistency checks

=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD:    FORBIDDEN: Phase 4 begins before this block is emitted.
T3-ORG-CHART-SECTIONS:   [sections produced]
T3-ANTI-PATTERN-PATH:    [CAN-OPERATE-FLAT: cat-2/cat-3 | STRUCTURE-WARRANTED: cat-1/cat-4]
T3-VERDICT-EMITTED:      [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T3-EVOLUTION-ROW-TYPES:  [Row 1 type, Row 2 type]
===

---

PHASE 4 -- VERIFY

INBOUND CONTRACT: FORBIDDEN: Phase 4 begins before Phase 3 record block is emitted.

Cross-record checks:
  T1-VERDICT = T3-VERDICT-EMITTED               -> T4-VERDICT-CONSISTENT
  T2-COUNT-CHECK = PASS                          -> T4-COUNT-CONSISTENT
  T2-IA-PRESENT = YES                            -> T4-IA-PRESENT
  T2-IA-SCOPE-FIRST-WORDS verbatim match
    for T1-IA-SCOPE-KEY                          -> T4-IA-SCOPE-VERBATIM

FORBIDDEN: declaring completion if any check = FAIL.

OUTBOUND GATE: FORBIDDEN: declaring completion before emitting the record block below.

The record block below is the Phase 4 unification artifact. From this block alone:
  - Gate schema: T4-VERDICT-CONSISTENT, T4-COUNT-CONSISTENT, T4-IA-PRESENT,
    T4-IA-SCOPE-VERBATIM, T4-FINAL-STATUS
  - Ordering constraint: PHASE-ORDERING-GUARD (first field) carries the FORBIDDEN
    for declaring completion
  - Materialization checkpoint: T4-FINAL-STATUS is the observable completion gate

=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD:   FORBIDDEN: declaring completion before this block is emitted.
T4-VERDICT-CONSISTENT:  [PASS | FAIL]
T4-COUNT-CONSISTENT:    [PASS | FAIL]
T4-IA-PRESENT:          [PASS | FAIL]
T4-IA-SCOPE-VERBATIM:   [PASS | FAIL]
T4-FINAL-STATUS:        [COMPLETE | REQUIRES-CORRECTION]
===
```
