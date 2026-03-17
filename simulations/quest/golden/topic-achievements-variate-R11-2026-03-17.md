---
skill: quest-variate
skill_target: topic-achievements
round: 11
date: 2026-03-17
rubric_version: 11
basis: V-05 R10 (corps-achievements) scored 100 on rubric v10 (C-01--C-29, 21/21
       aspirational). Rubric v11 extracts three new aspirational criteria from V-05 R10
       excellence signals. C-30: V-05 R10's STRUCTURAL AUDIT GATE already contains
       dedicated named sections (-- C-26 checks --, -- C-27 checks --, -- C-28 checks --,
       -- C-29 checks --) with >=2 individual checks per section -- satisfying C-30
       structurally but not declaring itself as the C-30 mechanism. C-31: V-05 R10
       states C-27/C-28/C-29 checks as separate Phase 1 and Phase 2 lines (per-phase
       granularity present but not expressed as named per-phase pairs with [C-31] tags).
       C-32: V-05 R10's CLOSURE GATE pass confirmation includes "Phase 2 inputs
       constrained to PHASE 1 MANIFEST" -- forward-binding language present but not
       labeled [C-32] or given a dedicated audit section. R11 formalizes these three
       implicit satisfactions into explicitly labeled, individually auditable mechanisms.
       N_aspirational = 24. Scoring formula: aspirational_pass / 24 * 10 (was /21).
---

# Variate R11 -- topic-achievements (2026-03-17)

5 complete prompt body variations for the `topic-achievements` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

Rubric v11 adds three new aspirational criteria beyond the v10 baseline:

- **C-30 (new)**: Per-criterion dedicated audit sections with granular individual checks
  (>=2 per section, string-match verifiable) -- from V-05 R10's STRUCTURAL AUDIT GATE
  pattern. Prior variations either bundle new criteria (V-04 R10 checks C-26/C-27/C-28
  in one block) or verify them globally. V-05 R10 gives C-27, C-28, and C-29 dedicated
  named sections with >=2 individual checks each. C-30 formalizes this: the STRUCTURAL
  AUDIT GATE must contain a dedicated named section for each aspirational criterion
  introduced at C-27 or later, with >=2 granular individual checks per section, string-
  match verifiable. A checker searches for the section header by name and counts sub-
  checks independently without scorer interpretation. Structurally independent of C-31:
  sections can carry global (non-per-phase) checks and still satisfy C-30.

- **C-31 (new)**: Per-phase audit granularity -- each check applied independently per
  phase, not as a single global assertion -- from V-05 R10's per-phase check expression.
  Prior variations verify criteria globally ("MANIFEST block present"). V-05 R10 states
  each check separately per phase: "Phase 1 MANIFEST block present" / "Phase 2 MANIFEST
  block present". C-31 formalizes this as a named property: each audit check for C-27
  and above is expressed as a per-phase pair (Phase 1 / Phase 2), with a [C-31] tag on
  the pair. A single global check cannot detect phase-specific failures -- Phase 1
  compliance does not prove Phase 2 compliance. Structurally independent of C-30: per-
  phase pairs can exist inside sections without [C-30] tags.

- **C-32 (new)**: Forward-binding manifest constraint assertion in CLOSURE GATE -- from
  V-05 R10's "Phase 2 inputs constrained to PHASE 1 MANIFEST" language. C-28 requires
  recording the Phase N output-set manifest before the closure seal; it does not require
  the prompt to assert that the manifest locks Phase N+1 scope. Without forward-binding
  language the manifest is on-record but its constraining role is implicit -- retroactive
  scope expansion via reinterpretation does not contradict an unlabeled list. C-32 tests
  whether the CLOSURE GATE includes an explicit forward-binding constraint assertion
  (labeled [C-32]) tying Phase N+1 scope to the Phase N manifest. Any Phase N+1 scope
  expansion must now directly contradict an explicit claim, not merely ignore an implicit
  boundary. **C-32 requires C-28 as a precondition.** Addresses the retroactive
  reframing gap that C-28 alone does not close: manifest recorded but not forward-bound.

All variations carry the full v10 baseline: essential C-01--C-05, recommended C-06--C-08,
aspirational C-09--C-29. Scoring formula: `(essential_pass/5 * 60) + (recommended_pass/3
* 30) + (aspirational_pass/24 * 10)`.

---

## Variation Axes Selected

| Axis | Hypothesis | Used In |
|------|------------|---------|
| C-30: [C-30] tag on dedicated section headers + SECTION INVENTORY step | Adding [C-30] to section headers makes each dedicated section string-match verifiable as a C-30 element; the SECTION INVENTORY step records section names and check counts, converting C-30's >=2 requirement from a manual count to a declared fact | V-01, V-04, V-05 |
| C-31: per-phase pair expression with [C-31] tag on each pair name | Expressing each audit check as a named per-phase pair (Phase 1 / Phase 2 sub-checks under a single [C-31]-tagged pair name) converts implicit per-phase coverage into an explicitly declared, individually verifiable property | V-02, V-04, V-05 |
| C-32: [C-32] tag on CLOSURE GATE forward-binding assertion + dedicated C-32 audit section | Adding [C-32] to the forward-binding pass confirmation and a dedicated C-32 section in the STRUCTURAL AUDIT GATE closes the gap C-28 leaves open: manifest recorded but constraint direction unlabeled | V-03, V-05 |

---

## V-01 -- Single Axis: C-30 Dedicated Section Tagging

**Axis**: C-30 -- add `[C-30]` tag to each dedicated criterion section header in the
STRUCTURAL AUDIT GATE (`-- C-27 SECTION [C-30] --`, `-- C-28 SECTION [C-30] --`,
`-- C-29 SECTION [C-30] --`). Add a C-30 SECTION INVENTORY step that names each
section and records its check count. Declare in the template preamble that the
STRUCTURAL AUDIT GATE uses dedicated named sections tagged [C-30].

**Hypothesis**: V-05 R10's STRUCTURAL AUDIT GATE already has the dedicated section
structure (-- C-27 checks --, etc.) satisfying C-30 structurally but not labeling
itself as the C-30 mechanism. A scorer evaluating C-30 must infer section structure
from indentation. Adding [C-30] to each section header makes each section a named,
criterion-referenced evidence point: the audit gate can verify C-30 by checking for
`-- C-XX SECTION [C-30] --` header strings rather than interpreting format. The
SECTION INVENTORY step converts C-30's ">=2 checks per section" requirement from a
manual count to a declared record. Risk: section headers are pre-printed -- the model
transcribes them not generates them -- so C-30 compliance is structurally enforced.
C-31 (per-phase pairs) and C-32 (forward-binding) are not added; their implicit
satisfactions from R10 V-05 remain present but unlabeled.

---

You are running `topic-achievements`. Scan all signal artifacts for the topic. Compute
achievement state. Show contributor leaderboard and next recommended action.

**INPUT**: `{{topic}}` (auto-detect from context or TOPICS.md if not provided)

---

### OUTPUT SCHEMAS [C-37]

**Achievement row**: `| Category | Achievement | State | Evidence | Progress |`
State: EARNED / IN-PROGRESS / LOCKED (exactly one). [C-01]
Evidence: artifact path from Phase 1 STATE. [C-03]
Progress: `n of m [requirement]` for IN-PROGRESS; `--` otherwise. [C-04]

**Leaderboard row**: `| Rank | Contributor | Signals | Topics | Milestones | Score | Pattern |`

**1-Away row**: `| Topic/Milestone | Achievement | Gap | Exact Action |`

**Next action**: `Next: /[skill] [topic] -> produces [artifact] -> advances [Achievement] -> Unlocks [Achievement] -> Breaks [PATTERN]`

---

### REGISTRY PRIMACY GATE [C-24]

Read `simulations/TOPICS.md` before any phase begins.
The registry entry for `{{topic}}` is the **sole authoritative gate contract** for this skill.
Phase instructions are subordinate. Registry governs on conflict.

FAIL Tier 1 [C-25]: Topic absent -> halt.
FAIL Tier 3 [C-25]: Phase result contradicts registry -> registry governs, record override.

---

### ATTRIBUTION INTEGRITY GATE [C-24/C-30]

Before Phase 1 begins:
(1) Confirm `{{topic}}` in TOPICS.md. [C-24]
(2) Glob `simulations/**/{{topic}}-*.md`. Build ATTRIBUTION BASELINE: file count + contributor list.
(3) Record: `ATTRIBUTION BASELINE: [N] artifacts. Contributors: [list]`.

FAIL Tier 1 [C-25]: 0 artifacts -> halt.
FAIL Tier 2 [C-25]: Some frontmatter missing contributor field -> record count, continue.
FAIL Tier 3 [C-25]: Achievement names contributor not in ATTRIBUTION BASELINE -> halt.

---

### OUTPUT TEMPLATE [C-27/C-30]

Fill all `[FIELD]` values. Do not modify pre-printed headers, dividers, barrier lines,
MANIFEST labels, or DUAL-LAYER BARRIER blocks. Barriers marked `[C-26][C-27]` are
pre-printed structural elements (model transcribes, not generates). Each phase boundary
carries two independent barrier mechanisms: instruction-enforced STOP [C-26] and
structure-enforced pre-printed divider [C-27]. Both must fail simultaneously for barrier
omission [C-29]. The STRUCTURAL AUDIT GATE uses dedicated named sections tagged [C-30]
for each aspirational criterion introduced at C-27 or later (C-27, C-28, C-29); each
section contains >=2 granular individual checks verifiable by string match.

```
## PHASE 1 -- EVIDENCE SCAN

SCAN STATE:
  Namespaces with signals: [list]
  Per-namespace count: [ns: n, ns: n, ...]
  Total signals: [N]
  Milestones (from registry): [M]
  Contributors: [list]
  Earliest: [date]  Latest: [date]

SCAN GATE [C-01/C-15]:
  (1) simulations/ accessible; glob >= 1 file.
  (2) All files assigned to known namespace.
  (3) Contributor list matches ATTRIBUTION BASELINE.
  (4) PHASE 1 STATE complete.
  Pass: "SCAN GATE [C-01/C-15]: [N] signals, [M] namespaces. Contributors: [list]."
  Fail Tier 1: "SCAN GATE FAIL [C-01/C-15]: [condition] -- [path]."

PHASE 1 MANIFEST [C-28]:
  Artifact count: [K]
  Namespace count: [N]

PHASE 1 CLOSURE GATE [C-26]:
  (1) Verify PHASE 1 MANIFEST [C-28] is recorded above with artifact count and namespace count.
  (2) Phase 2 inputs are limited to items in PHASE 1 MANIFEST. Phase 2 may not
      introduce artifact data not present in PHASE 1 STATE.
  Pass: "PHASE 1 CLOSURE GATE [C-26]: Manifest verified ([K] artifacts, [N] namespaces).
    Phase 2 inputs constrained to PHASE 1 MANIFEST."

STOP. Phase 1 complete. [C-26]
--- PHASE 1 SEALED [C-26][C-27] ---
DUAL-LAYER BARRIER [C-26/C-27][C-29]:
  Layer 1: STOP declaration above (instruction-enforced) [C-26]
  Layer 2: Pre-printed divider above (structure-enforced -- model transcribes, not generates) [C-27]
  Independence: Layer 1 fails if model omits the STOP instruction; Layer 2 fails if model
    actively skips or deletes a pre-printed element. Both must fail simultaneously for
    barrier omission. [C-29]
Phase 1 scan results are closed. PHASE 1 STATE and PHASE 1 MANIFEST are immutable.
Phase 2 reads PHASE 1 STATE above. Phase 2 may not alter signal counts,
contributor lists, namespace assignments, or artifact citations.

## PHASE 2 -- ACHIEVEMENT CLASSIFICATION

Achievement table (use PHASE 1 STATE only; all 7 categories required) [C-06]:

| Category       | Achievement         | State              | Evidence [C-03]  | Progress [C-04]   |
|----------------|---------------------|-------------------|------------------|-------------------|
| Exploration    | Namespace Spread    | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Depth          | Signal Depth        | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Coverage       | Full Coverage       | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Quality        | Falsified [C-02]    | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Chain          | Signal Chain        | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Discovery      | Unexpected Echo     | [EARNED/LOC]      | [artifact path]  | [--]              |
| Corps/Crew     | Team Breadth        | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |

CLASSIFICATION GATE [C-03/C-25]:
  (1) Every EARNED row cites artifact path from PHASE 1 STATE. [C-03]
  (2) Every IN-PROGRESS row shows `n of m` form. [C-04]
  (3) All 7 categories appear. [C-06]
  (4) No citation to path absent from PHASE 1 STATE.
  Fail Tier 2: Missing citation -> `(UNCITED)`. Fail Tier 3: Absent path -> halt.

1-AWAY TABLE [C-09/C-18]:
| Topic/Milestone | Achievement | Gap | Exact Action |
|-----------------|-------------|-----|--------------|
| [item]          | [name]      | [n] | [action]     |

Pattern [C-17]: [SOLO_ISLAND / NAMESPACE_MOAT / SPRINT_FREEZE / SHALLOW_POOL / ORPHAN_TOPIC / NONE]

PHASE 2 STATE:
  Rows: [7] | 1-Away: [N] | Pattern: [label] | Dominant contributor: [name]

PHASE 2 MANIFEST [C-28]:
  Achievement row count: 7
  EARNED count: [N]

PHASE 2 CLOSURE GATE [C-26]:
  (1) Verify PHASE 2 MANIFEST [C-28] is recorded above with row count and EARNED count.
  (2) Phase 3 inputs are limited to items in PHASE 2 MANIFEST. Phase 3 may not
      alter EARNED/IN-PROGRESS/LOCKED assignments or category coverage decisions.
  Pass: "PHASE 2 CLOSURE GATE [C-26]: Manifest verified (7 rows, [N] EARNED).
    Phase 3 inputs constrained to PHASE 2 MANIFEST."

STOP. Phase 2 complete. [C-26]
--- PHASE 2 SEALED [C-26][C-27] ---
DUAL-LAYER BARRIER [C-26/C-27][C-29]:
  Layer 1: STOP declaration above (instruction-enforced) [C-26]
  Layer 2: Pre-printed divider above (structure-enforced -- model transcribes, not generates) [C-27]
  Independence: Layer 1 fails if model omits the STOP instruction; Layer 2 fails if model
    actively skips or deletes a pre-printed element. Both must fail simultaneously for
    barrier omission. [C-29]
Phase 2 classifications are closed. PHASE 2 STATE and PHASE 2 MANIFEST are immutable.
Phase 3 reads PHASE 2 STATE above. Phase 3 may not alter EARNED/IN-PROGRESS/LOCKED
assignments or category coverage decisions.

## PHASE 3 -- OUTPUT

PRE-WRITE GATE [C-11]: All values in tables below derive from PHASE 1 STATE and PHASE 2 STATE.
No artifact rescanning required.
  [Confirmation: pass / Fail: [specific value requiring rescan and corrective action]]

LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]:
  Formula: Score = (Signals x 1) + (Topics x 3) + (Milestones x 5) [C-16]
  | Rank | Contributor | Signals | Topics | Milestones | Score | Pattern |
  Rank 1 worked example [C-19]: Score = [S]x1 + [T]x3 + [M]x5 = [total]
  Correction [C-21]: [applied: [old]->[new] / not needed]
  Label enumeration (C-25): [C-16/C-19/C-21] verified.
  Pass: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Formula (C-16): confirmed.
    Example (C-19): [total]. Correction (C-21): [applied/not needed].
    Label enumeration (C-25): [C-16/C-19/C-21] verified."

**TEAM INSIGHT -- [descriptive name] [C-13]:** [cross-table synthesis finding]

INSIGHT GATE [C-13/C-22]:
  (1) Names specific pattern or contributor: [confirmed]
  (2) Not a single-row restatement: [confirmed]
  (3) Requires cross-table synthesis; not derivable from achievements table alone [C-22]: [confirmed]

ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]:
  Next: /[skill] [topic] -> produces [artifact] -> advances [Achievement] [C-05]
    -> Unlocks [Achievement] -> Breaks [PATTERN] [C-12]
  (1) Names specific skill, artifact, advancement [C-05]: confirmed
  (2) Unlock chain present [C-12]: confirmed
  (3) Registry labels exact, no invented labels [C-14]: confirmed
  (4) All gates in this run carry criterion ID [C-20]: confirmed
  (5) Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified.
  Fail Tier 1: Gate missing criterion ID -> halt.
  Fail Tier 3: Criterion ID replaced by narrative -> halt.
  Pass: "ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]: Action (C-05): confirmed.
    Unlock chain (C-12): confirmed. Registry labels (C-14): confirmed.
    Gate IDs (C-20): confirmed. Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified."

STRUCTURAL AUDIT GATE [C-20/C-26/C-27/C-28/C-29/C-30]:
  Gates executed: [list all gate labels in this run]
  All carry criterion ID [C-20]: [confirmed / violations: list]
  LEADERBOARD CLUSTER enumerates C-16, C-19, C-21 [C-25]: [confirmed]
  ACTIONS CLUSTER enumerates C-05, C-12, C-14, C-20 [C-25]: [confirmed]
  -- C-26 SECTION --
  Phase 1 STOP barrier written [C-26]: [confirmed]
  Phase 1 CLOSURE GATE pass confirmation recorded [C-26]: [confirmed]
  Phase 2 STOP barrier written [C-26]: [confirmed]
  Phase 2 CLOSURE GATE pass confirmation recorded [C-26]: [confirmed]
  -- C-27 SECTION [C-30] --
  Phase 1 "--- PHASE 1 SEALED [C-26][C-27] ---" pre-printed with [C-27] tag [C-27]: [confirmed]
  Phase 2 "--- PHASE 2 SEALED [C-26][C-27] ---" pre-printed with [C-27] tag [C-27]: [confirmed]
  -- C-28 SECTION [C-30] --
  Phase 1 MANIFEST [C-28] block present before seal [C-28]: [confirmed]
  Phase 1 MANIFEST artifact count + namespace count recorded [C-28]: [confirmed]
  Phase 2 MANIFEST [C-28] block present before seal [C-28]: [confirmed]
  Phase 2 MANIFEST row count + EARNED count recorded [C-28]: [confirmed]
  -- C-29 SECTION [C-30] --
  Phase 1 DUAL-LAYER BARRIER block names Layer 1 (STOP) [C-29]: [confirmed]
  Phase 1 DUAL-LAYER BARRIER block names Layer 2 (pre-printed) [C-29]: [confirmed]
  Phase 1 DUAL-LAYER BARRIER independence assertion present [C-29]: [confirmed]
  Phase 2 DUAL-LAYER BARRIER block names Layer 1 (STOP) [C-29]: [confirmed]
  Phase 2 DUAL-LAYER BARRIER block names Layer 2 (pre-printed) [C-29]: [confirmed]
  Phase 2 DUAL-LAYER BARRIER independence assertion present [C-29]: [confirmed]
  -- C-30 SECTION INVENTORY [C-30] --
  C-27 section header "-- C-27 SECTION [C-30] --" present [C-30]: [confirmed]
  C-27 section check count: [2] (required: >=2) [C-30]: [confirmed]
  C-28 section header "-- C-28 SECTION [C-30] --" present [C-30]: [confirmed]
  C-28 section check count: [4] (required: >=2) [C-30]: [confirmed]
  C-29 section header "-- C-29 SECTION [C-30] --" present [C-30]: [confirmed]
  C-29 section check count: [6] (required: >=2) [C-30]: [confirmed]
  -- Summary --
  Result: [N] gates checked. [2] STOP barriers (C-26). [2] closure gate confirmations (C-26).
    [2] [C-27]-tagged barriers (C-27). [2] MANIFEST blocks with 2 dimensions each (C-28).
    [2] dual-layer declarations with independence (C-29). [3] dedicated [C-30]-tagged
    sections with >=2 checks each (C-30). Violations: [n].
  Fail Tier 1: Gate missing criterion ID -> halt.
  Fail Tier 2: [C-30] section header absent for any criterion C-27+ -> finding.
  Fail Tier 2: Section check count < 2 for any [C-30] section -> finding.
  Fail Tier 3: Any barrier or closure gate permits retroactive Phase N alteration -> halt.
```

**Write artifact**: `simulations/topic/{{topic}}-achievements-{{date}}.md`

---

## V-02 -- Single Axis: C-31 Per-Phase Pair Expression

**Axis**: C-31 -- express each audit check for C-27, C-28, and C-29 in the STRUCTURAL
AUDIT GATE as a named per-phase pair: a single [C-31]-tagged pair name with Phase 1 and
Phase 2 as indented sub-checks rather than separate flat lines. Section headers remain
plain (no [C-30] tags). Template preamble notes per-phase granularity as a declared
property.

**Hypothesis**: V-05 R10 already states Phase 1 and Phase 2 checks on separate lines,
satisfying C-31 structurally. But C-31 compliance is inferred: a scorer must recognize
that the Phase 1 / Phase 2 separation is intentional per-phase granularity, not just
verbosity. Naming each check as a [C-31]-tagged pair ("MANIFEST block present [C-31]:")
with Phase 1 / Phase 2 as sub-checks makes the per-phase requirement an explicitly
declared structural property. A checker can verify C-31 by searching for [C-31]-tagged
pair names and confirming both Phase 1 and Phase 2 sub-checks exist under each. Risk:
the pair structure changes the visual format of the audit gate -- Phase 1 / Phase 2 are
now subordinate to a pair name rather than parallel flat lines. This may make the gate
longer but each pair is more independently auditable. C-30 (section tags) and C-32
(forward-binding) are not added.

---

You are running `topic-achievements`. Scan all signal artifacts for the topic. Compute
achievement state. Show contributor leaderboard and next recommended action.

**INPUT**: `{{topic}}` (auto-detect from context or TOPICS.md if not provided)

---

### OUTPUT SCHEMAS [C-37]

**Achievement row**: `| Category | Achievement | State | Evidence | Progress |`
State: EARNED / IN-PROGRESS / LOCKED (exactly one). [C-01]
Evidence: artifact path from Phase 1 STATE. [C-03]
Progress: `n of m [requirement]` for IN-PROGRESS; `--` otherwise. [C-04]

**Leaderboard row**: `| Rank | Contributor | Signals | Topics | Milestones | Score | Pattern |`

**1-Away row**: `| Topic/Milestone | Achievement | Gap | Exact Action |`

**Next action**: `Next: /[skill] [topic] -> produces [artifact] -> advances [Achievement] -> Unlocks [Achievement] -> Breaks [PATTERN]`

---

### REGISTRY PRIMACY GATE [C-24]

Read `simulations/TOPICS.md` before any phase begins.
The registry entry for `{{topic}}` is the **sole authoritative gate contract** for this skill.
Phase instructions are subordinate. Registry governs on conflict.

FAIL Tier 1 [C-25]: Topic absent -> halt.
FAIL Tier 3 [C-25]: Phase result contradicts registry -> registry governs, record override.

---

### ATTRIBUTION INTEGRITY GATE [C-24/C-30]

Before Phase 1 begins:
(1) Confirm `{{topic}}` in TOPICS.md. [C-24]
(2) Glob `simulations/**/{{topic}}-*.md`. Build ATTRIBUTION BASELINE: file count + contributor list.
(3) Record: `ATTRIBUTION BASELINE: [N] artifacts. Contributors: [list]`.

FAIL Tier 1 [C-25]: 0 artifacts -> halt.
FAIL Tier 2 [C-25]: Some frontmatter missing contributor field -> record count, continue.
FAIL Tier 3 [C-25]: Achievement names contributor not in ATTRIBUTION BASELINE -> halt.

---

### OUTPUT TEMPLATE [C-27/C-31]

Fill all `[FIELD]` values. Do not modify pre-printed headers, dividers, barrier lines,
MANIFEST labels, or DUAL-LAYER BARRIER blocks. Barriers marked `[C-26][C-27]` are
pre-printed structural elements (model transcribes, not generates). Each phase boundary
carries two independent barrier mechanisms: instruction-enforced STOP [C-26] and
structure-enforced pre-printed divider [C-27]. Both must fail simultaneously for barrier
omission [C-29]. The STRUCTURAL AUDIT GATE checks each criterion independently per phase
[C-31]: each C-27/C-28/C-29 check is expressed as a named per-phase pair with Phase 1
and Phase 2 sub-checks verified separately.

```
## PHASE 1 -- EVIDENCE SCAN

SCAN STATE:
  Namespaces with signals: [list]
  Per-namespace count: [ns: n, ns: n, ...]
  Total signals: [N]
  Milestones (from registry): [M]
  Contributors: [list]
  Earliest: [date]  Latest: [date]

SCAN GATE [C-01/C-15]:
  (1) simulations/ accessible; glob >= 1 file.
  (2) All files assigned to known namespace.
  (3) Contributor list matches ATTRIBUTION BASELINE.
  (4) PHASE 1 STATE complete.
  Pass: "SCAN GATE [C-01/C-15]: [N] signals, [M] namespaces. Contributors: [list]."
  Fail Tier 1: "SCAN GATE FAIL [C-01/C-15]: [condition] -- [path]."

PHASE 1 MANIFEST [C-28]:
  Artifact count: [K]
  Namespace count: [N]

PHASE 1 CLOSURE GATE [C-26]:
  (1) Verify PHASE 1 MANIFEST [C-28] is recorded above with artifact count and namespace count.
  (2) Phase 2 inputs are limited to items in PHASE 1 MANIFEST. Phase 2 may not
      introduce artifact data not present in PHASE 1 STATE.
  Pass: "PHASE 1 CLOSURE GATE [C-26]: Manifest verified ([K] artifacts, [N] namespaces).
    Phase 2 inputs constrained to PHASE 1 MANIFEST."

STOP. Phase 1 complete. [C-26]
--- PHASE 1 SEALED [C-26][C-27] ---
DUAL-LAYER BARRIER [C-26/C-27][C-29]:
  Layer 1: STOP declaration above (instruction-enforced) [C-26]
  Layer 2: Pre-printed divider above (structure-enforced -- model transcribes, not generates) [C-27]
  Independence: Layer 1 fails if model omits the STOP instruction; Layer 2 fails if model
    actively skips or deletes a pre-printed element. Both must fail simultaneously for
    barrier omission. [C-29]
Phase 1 scan results are closed. PHASE 1 STATE and PHASE 1 MANIFEST are immutable.
Phase 2 reads PHASE 1 STATE above. Phase 2 may not alter signal counts,
contributor lists, namespace assignments, or artifact citations.

## PHASE 2 -- ACHIEVEMENT CLASSIFICATION

Achievement table (use PHASE 1 STATE only; all 7 categories required) [C-06]:

| Category       | Achievement         | State              | Evidence [C-03]  | Progress [C-04]   |
|----------------|---------------------|-------------------|------------------|-------------------|
| Exploration    | Namespace Spread    | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Depth          | Signal Depth        | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Coverage       | Full Coverage       | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Quality        | Falsified [C-02]    | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Chain          | Signal Chain        | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Discovery      | Unexpected Echo     | [EARNED/LOC]      | [artifact path]  | [--]              |
| Corps/Crew     | Team Breadth        | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |

CLASSIFICATION GATE [C-03/C-25]:
  (1) Every EARNED row cites artifact path from PHASE 1 STATE. [C-03]
  (2) Every IN-PROGRESS row shows `n of m` form. [C-04]
  (3) All 7 categories appear. [C-06]
  (4) No citation to path absent from PHASE 1 STATE.
  Fail Tier 2: Missing citation -> `(UNCITED)`. Fail Tier 3: Absent path -> halt.

1-AWAY TABLE [C-09/C-18]:
| Topic/Milestone | Achievement | Gap | Exact Action |
|-----------------|-------------|-----|--------------|
| [item]          | [name]      | [n] | [action]     |

Pattern [C-17]: [SOLO_ISLAND / NAMESPACE_MOAT / SPRINT_FREEZE / SHALLOW_POOL / ORPHAN_TOPIC / NONE]

PHASE 2 STATE:
  Rows: [7] | 1-Away: [N] | Pattern: [label] | Dominant contributor: [name]

PHASE 2 MANIFEST [C-28]:
  Achievement row count: 7
  EARNED count: [N]

PHASE 2 CLOSURE GATE [C-26]:
  (1) Verify PHASE 2 MANIFEST [C-28] is recorded above with row count and EARNED count.
  (2) Phase 3 inputs are limited to items in PHASE 2 MANIFEST. Phase 3 may not
      alter EARNED/IN-PROGRESS/LOCKED assignments or category coverage decisions.
  Pass: "PHASE 2 CLOSURE GATE [C-26]: Manifest verified (7 rows, [N] EARNED).
    Phase 3 inputs constrained to PHASE 2 MANIFEST."

STOP. Phase 2 complete. [C-26]
--- PHASE 2 SEALED [C-26][C-27] ---
DUAL-LAYER BARRIER [C-26/C-27][C-29]:
  Layer 1: STOP declaration above (instruction-enforced) [C-26]
  Layer 2: Pre-printed divider above (structure-enforced -- model transcribes, not generates) [C-27]
  Independence: Layer 1 fails if model omits the STOP instruction; Layer 2 fails if model
    actively skips or deletes a pre-printed element. Both must fail simultaneously for
    barrier omission. [C-29]
Phase 2 classifications are closed. PHASE 2 STATE and PHASE 2 MANIFEST are immutable.
Phase 3 reads PHASE 2 STATE above. Phase 3 may not alter EARNED/IN-PROGRESS/LOCKED
assignments or category coverage decisions.

## PHASE 3 -- OUTPUT

PRE-WRITE GATE [C-11]: All values in tables below derive from PHASE 1 STATE and PHASE 2 STATE.
No artifact rescanning required.
  [Confirmation: pass / Fail: [specific value requiring rescan and corrective action]]

LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]:
  Formula: Score = (Signals x 1) + (Topics x 3) + (Milestones x 5) [C-16]
  | Rank | Contributor | Signals | Topics | Milestones | Score | Pattern |
  Rank 1 worked example [C-19]: Score = [S]x1 + [T]x3 + [M]x5 = [total]
  Correction [C-21]: [applied: [old]->[new] / not needed]
  Label enumeration (C-25): [C-16/C-19/C-21] verified.
  Pass: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Formula (C-16): confirmed.
    Example (C-19): [total]. Correction (C-21): [applied/not needed].
    Label enumeration (C-25): [C-16/C-19/C-21] verified."

**TEAM INSIGHT -- [descriptive name] [C-13]:** [cross-table synthesis finding]

INSIGHT GATE [C-13/C-22]:
  (1) Names specific pattern or contributor: [confirmed]
  (2) Not a single-row restatement: [confirmed]
  (3) Requires cross-table synthesis; not derivable from achievements table alone [C-22]: [confirmed]

ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]:
  Next: /[skill] [topic] -> produces [artifact] -> advances [Achievement] [C-05]
    -> Unlocks [Achievement] -> Breaks [PATTERN] [C-12]
  (1) Names specific skill, artifact, advancement [C-05]: confirmed
  (2) Unlock chain present [C-12]: confirmed
  (3) Registry labels exact, no invented labels [C-14]: confirmed
  (4) All gates in this run carry criterion ID [C-20]: confirmed
  (5) Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified.
  Fail Tier 1: Gate missing criterion ID -> halt.
  Fail Tier 3: Criterion ID replaced by narrative -> halt.
  Pass: "ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]: Action (C-05): confirmed.
    Unlock chain (C-12): confirmed. Registry labels (C-14): confirmed.
    Gate IDs (C-20): confirmed. Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified."

STRUCTURAL AUDIT GATE [C-20/C-26/C-27/C-28/C-29/C-31]:
  Gates executed: [list all gate labels in this run]
  All carry criterion ID [C-20]: [confirmed / violations: list]
  LEADERBOARD CLUSTER enumerates C-16, C-19, C-21 [C-25]: [confirmed]
  ACTIONS CLUSTER enumerates C-05, C-12, C-14, C-20 [C-25]: [confirmed]
  -- C-26 checks --
  Phase 1 STOP barrier written [C-26]: [confirmed]
  Phase 1 CLOSURE GATE pass confirmation recorded [C-26]: [confirmed]
  Phase 2 STOP barrier written [C-26]: [confirmed]
  Phase 2 CLOSURE GATE pass confirmation recorded [C-26]: [confirmed]
  -- C-27 checks --
  [C-27] tag on pre-printed barrier [C-31]:
    Phase 1: "--- PHASE 1 SEALED [C-26][C-27] ---" present with [C-27] tag: [confirmed]
    Phase 2: "--- PHASE 2 SEALED [C-26][C-27] ---" present with [C-27] tag: [confirmed]
  -- C-28 checks --
  MANIFEST block present before seal [C-31]:
    Phase 1: PHASE 1 MANIFEST [C-28] block present: [confirmed]
    Phase 2: PHASE 2 MANIFEST [C-28] block present: [confirmed]
  MANIFEST records two dimensions [C-31]:
    Phase 1: artifact count + namespace count recorded: [confirmed]
    Phase 2: row count + EARNED count recorded: [confirmed]
  -- C-29 checks --
  DUAL-LAYER BARRIER names both layers [C-31]:
    Phase 1: Layer 1 (STOP) + Layer 2 (pre-printed) named: [confirmed]
    Phase 2: Layer 1 (STOP) + Layer 2 (pre-printed) named: [confirmed]
  DUAL-LAYER BARRIER independence assertion [C-31]:
    Phase 1: independence assertion present: [confirmed]
    Phase 2: independence assertion present: [confirmed]
  -- Summary --
  Result: [N] gates checked. [2] STOP barriers (C-26). [2] closure gate confirmations (C-26).
    [2] [C-27]-tagged barriers (C-27). [2] MANIFEST blocks with 2 dimensions each (C-28).
    [2] dual-layer declarations with independence (C-29). All C-27/C-28/C-29 checks
    expressed as per-phase pairs [C-31]. Violations: [n].
  Fail Tier 1: Gate missing criterion ID -> halt.
  Fail Tier 2: C-27/C-28/C-29 check expressed as global assertion, not per-phase pair -> finding.
  Fail Tier 2: [C-31] tag absent from a per-phase pair name -> finding.
  Fail Tier 3: Any barrier or closure gate permits retroactive Phase N alteration -> halt.
```

**Write artifact**: `simulations/topic/{{topic}}-achievements-{{date}}.md`

---

## V-03 -- Single Axis: C-32 Forward-Binding Manifest Constraint

**Axis**: C-32 -- add `[C-32]` tag to the forward-binding assertion in each CLOSURE
GATE pass confirmation ("Phase N+1 inputs constrained to PHASE N MANIFEST [C-32]").
Strengthen the assertion to make the constraint explicit: any Phase N+1 artifact scope
not present in PHASE N MANIFEST directly contradicts this claim. Add a dedicated
`-- C-32 SECTION --` in the STRUCTURAL AUDIT GATE with >=2 checks per phase.

**Hypothesis**: V-05 R10's CLOSURE GATE pass confirmation already includes "Phase 2
inputs constrained to PHASE 1 MANIFEST" -- satisfying C-32 structurally. But C-32
compliance is inferred: the constraining role of the manifest is implicit. Adding [C-32]
to the forward-binding assertion converts an unmarked sentence into a named contractual
claim. A scorer verifying C-32 searches for "[C-32]" in the CLOSURE GATE pass line
rather than interpreting whether an unlabeled sentence implies constraint. The dedicated
C-32 audit section closes the detection loop: each phase's forward-binding assertion is
independently verified. Risk: C-32 depends on C-28 (MANIFEST must exist before the
forward-binding can reference it); V-03 inherits the MANIFEST block from R10 V-05
baseline, satisfying the precondition. C-30 and C-31 are not added.

---

You are running `topic-achievements`. Scan all signal artifacts for the topic. Compute
achievement state. Show contributor leaderboard and next recommended action.

**INPUT**: `{{topic}}` (auto-detect from context or TOPICS.md if not provided)

---

### OUTPUT SCHEMAS [C-37]

**Achievement row**: `| Category | Achievement | State | Evidence | Progress |`
State: EARNED / IN-PROGRESS / LOCKED (exactly one). [C-01]
Evidence: artifact path from Phase 1 STATE. [C-03]
Progress: `n of m [requirement]` for IN-PROGRESS; `--` otherwise. [C-04]

**Leaderboard row**: `| Rank | Contributor | Signals | Topics | Milestones | Score | Pattern |`

**1-Away row**: `| Topic/Milestone | Achievement | Gap | Exact Action |`

**Next action**: `Next: /[skill] [topic] -> produces [artifact] -> advances [Achievement] -> Unlocks [Achievement] -> Breaks [PATTERN]`

---

### REGISTRY PRIMACY GATE [C-24]

Read `simulations/TOPICS.md` before any phase begins.
The registry entry for `{{topic}}` is the **sole authoritative gate contract** for this skill.
Phase instructions are subordinate. Registry governs on conflict.

FAIL Tier 1 [C-25]: Topic absent -> halt.
FAIL Tier 3 [C-25]: Phase result contradicts registry -> registry governs, record override.

---

### ATTRIBUTION INTEGRITY GATE [C-24/C-30]

Before Phase 1 begins:
(1) Confirm `{{topic}}` in TOPICS.md. [C-24]
(2) Glob `simulations/**/{{topic}}-*.md`. Build ATTRIBUTION BASELINE: file count + contributor list.
(3) Record: `ATTRIBUTION BASELINE: [N] artifacts. Contributors: [list]`.

FAIL Tier 1 [C-25]: 0 artifacts -> halt.
FAIL Tier 2 [C-25]: Some frontmatter missing contributor field -> record count, continue.
FAIL Tier 3 [C-25]: Achievement names contributor not in ATTRIBUTION BASELINE -> halt.

---

### OUTPUT TEMPLATE [C-27/C-32]

Fill all `[FIELD]` values. Do not modify pre-printed headers, dividers, barrier lines,
MANIFEST labels, or DUAL-LAYER BARRIER blocks. Barriers marked `[C-26][C-27]` are
pre-printed structural elements (model transcribes, not generates). Each phase boundary
carries two independent barrier mechanisms: instruction-enforced STOP [C-26] and
structure-enforced pre-printed divider [C-27]. Both must fail simultaneously for barrier
omission [C-29]. Each CLOSURE GATE includes an explicit forward-binding constraint
assertion [C-32] tying Phase N+1 scope to the Phase N MANIFEST; any Phase N+1 scope
expansion directly contradicts this assertion.

```
## PHASE 1 -- EVIDENCE SCAN

SCAN STATE:
  Namespaces with signals: [list]
  Per-namespace count: [ns: n, ns: n, ...]
  Total signals: [N]
  Milestones (from registry): [M]
  Contributors: [list]
  Earliest: [date]  Latest: [date]

SCAN GATE [C-01/C-15]:
  (1) simulations/ accessible; glob >= 1 file.
  (2) All files assigned to known namespace.
  (3) Contributor list matches ATTRIBUTION BASELINE.
  (4) PHASE 1 STATE complete.
  Pass: "SCAN GATE [C-01/C-15]: [N] signals, [M] namespaces. Contributors: [list]."
  Fail Tier 1: "SCAN GATE FAIL [C-01/C-15]: [condition] -- [path]."

PHASE 1 MANIFEST [C-28]:
  Artifact count: [K]
  Namespace count: [N]

PHASE 1 CLOSURE GATE [C-26/C-32]:
  (1) Verify PHASE 1 MANIFEST [C-28] is recorded above with artifact count and namespace count.
  (2) Phase 2 inputs constrained to PHASE 1 MANIFEST [C-32]. Any Phase 2 artifact scope
      not present in PHASE 1 MANIFEST above directly contradicts this assertion.
  Pass: "PHASE 1 CLOSURE GATE [C-26]: Manifest verified ([K] artifacts, [N] namespaces).
    Phase 2 inputs constrained to PHASE 1 MANIFEST [C-32]."

STOP. Phase 1 complete. [C-26]
--- PHASE 1 SEALED [C-26][C-27] ---
DUAL-LAYER BARRIER [C-26/C-27][C-29]:
  Layer 1: STOP declaration above (instruction-enforced) [C-26]
  Layer 2: Pre-printed divider above (structure-enforced -- model transcribes, not generates) [C-27]
  Independence: Layer 1 fails if model omits the STOP instruction; Layer 2 fails if model
    actively skips or deletes a pre-printed element. Both must fail simultaneously for
    barrier omission. [C-29]
Phase 1 scan results are closed. PHASE 1 STATE and PHASE 1 MANIFEST are immutable.
Phase 2 reads PHASE 1 STATE above. Phase 2 may not alter signal counts,
contributor lists, namespace assignments, or artifact citations.

## PHASE 2 -- ACHIEVEMENT CLASSIFICATION

Achievement table (use PHASE 1 STATE only; all 7 categories required) [C-06]:

| Category       | Achievement         | State              | Evidence [C-03]  | Progress [C-04]   |
|----------------|---------------------|-------------------|------------------|-------------------|
| Exploration    | Namespace Spread    | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Depth          | Signal Depth        | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Coverage       | Full Coverage       | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Quality        | Falsified [C-02]    | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Chain          | Signal Chain        | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Discovery      | Unexpected Echo     | [EARNED/LOC]      | [artifact path]  | [--]              |
| Corps/Crew     | Team Breadth        | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |

CLASSIFICATION GATE [C-03/C-25]:
  (1) Every EARNED row cites artifact path from PHASE 1 STATE. [C-03]
  (2) Every IN-PROGRESS row shows `n of m` form. [C-04]
  (3) All 7 categories appear. [C-06]
  (4) No citation to path absent from PHASE 1 STATE.
  Fail Tier 2: Missing citation -> `(UNCITED)`. Fail Tier 3: Absent path -> halt.

1-AWAY TABLE [C-09/C-18]:
| Topic/Milestone | Achievement | Gap | Exact Action |
|-----------------|-------------|-----|--------------|
| [item]          | [name]      | [n] | [action]     |

Pattern [C-17]: [SOLO_ISLAND / NAMESPACE_MOAT / SPRINT_FREEZE / SHALLOW_POOL / ORPHAN_TOPIC / NONE]

PHASE 2 STATE:
  Rows: [7] | 1-Away: [N] | Pattern: [label] | Dominant contributor: [name]

PHASE 2 MANIFEST [C-28]:
  Achievement row count: 7
  EARNED count: [N]

PHASE 2 CLOSURE GATE [C-26/C-32]:
  (1) Verify PHASE 2 MANIFEST [C-28] is recorded above with row count and EARNED count.
  (2) Phase 3 inputs constrained to PHASE 2 MANIFEST [C-32]. Any Phase 3 scope
      not present in PHASE 2 MANIFEST above directly contradicts this assertion.
  Pass: "PHASE 2 CLOSURE GATE [C-26]: Manifest verified (7 rows, [N] EARNED).
    Phase 3 inputs constrained to PHASE 2 MANIFEST [C-32]."

STOP. Phase 2 complete. [C-26]
--- PHASE 2 SEALED [C-26][C-27] ---
DUAL-LAYER BARRIER [C-26/C-27][C-29]:
  Layer 1: STOP declaration above (instruction-enforced) [C-26]
  Layer 2: Pre-printed divider above (structure-enforced -- model transcribes, not generates) [C-27]
  Independence: Layer 1 fails if model omits the STOP instruction; Layer 2 fails if model
    actively skips or deletes a pre-printed element. Both must fail simultaneously for
    barrier omission. [C-29]
Phase 2 classifications are closed. PHASE 2 STATE and PHASE 2 MANIFEST are immutable.
Phase 3 reads PHASE 2 STATE above. Phase 3 may not alter EARNED/IN-PROGRESS/LOCKED
assignments or category coverage decisions.

## PHASE 3 -- OUTPUT

PRE-WRITE GATE [C-11]: All values in tables below derive from PHASE 1 STATE and PHASE 2 STATE.
No artifact rescanning required.
  [Confirmation: pass / Fail: [specific value requiring rescan and corrective action]]

LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]:
  Formula: Score = (Signals x 1) + (Topics x 3) + (Milestones x 5) [C-16]
  | Rank | Contributor | Signals | Topics | Milestones | Score | Pattern |
  Rank 1 worked example [C-19]: Score = [S]x1 + [T]x3 + [M]x5 = [total]
  Correction [C-21]: [applied: [old]->[new] / not needed]
  Label enumeration (C-25): [C-16/C-19/C-21] verified.
  Pass: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Formula (C-16): confirmed.
    Example (C-19): [total]. Correction (C-21): [applied/not needed].
    Label enumeration (C-25): [C-16/C-19/C-21] verified."

**TEAM INSIGHT -- [descriptive name] [C-13]:** [cross-table synthesis finding]

INSIGHT GATE [C-13/C-22]:
  (1) Names specific pattern or contributor: [confirmed]
  (2) Not a single-row restatement: [confirmed]
  (3) Requires cross-table synthesis; not derivable from achievements table alone [C-22]: [confirmed]

ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]:
  Next: /[skill] [topic] -> produces [artifact] -> advances [Achievement] [C-05]
    -> Unlocks [Achievement] -> Breaks [PATTERN] [C-12]
  (1) Names specific skill, artifact, advancement [C-05]: confirmed
  (2) Unlock chain present [C-12]: confirmed
  (3) Registry labels exact, no invented labels [C-14]: confirmed
  (4) All gates in this run carry criterion ID [C-20]: confirmed
  (5) Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified.
  Fail Tier 1: Gate missing criterion ID -> halt.
  Fail Tier 3: Criterion ID replaced by narrative -> halt.
  Pass: "ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]: Action (C-05): confirmed.
    Unlock chain (C-12): confirmed. Registry labels (C-14): confirmed.
    Gate IDs (C-20): confirmed. Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified."

STRUCTURAL AUDIT GATE [C-20/C-26/C-27/C-28/C-29/C-32]:
  Gates executed: [list all gate labels in this run]
  All carry criterion ID [C-20]: [confirmed / violations: list]
  LEADERBOARD CLUSTER enumerates C-16, C-19, C-21 [C-25]: [confirmed]
  ACTIONS CLUSTER enumerates C-05, C-12, C-14, C-20 [C-25]: [confirmed]
  -- C-26 checks --
  Phase 1 STOP barrier written [C-26]: [confirmed]
  Phase 1 CLOSURE GATE pass confirmation recorded [C-26]: [confirmed]
  Phase 2 STOP barrier written [C-26]: [confirmed]
  Phase 2 CLOSURE GATE pass confirmation recorded [C-26]: [confirmed]
  -- C-27 checks --
  Phase 1 "--- PHASE 1 SEALED [C-26][C-27] ---" pre-printed with [C-27] tag [C-27]: [confirmed]
  Phase 2 "--- PHASE 2 SEALED [C-26][C-27] ---" pre-printed with [C-27] tag [C-27]: [confirmed]
  -- C-28 checks --
  Phase 1 MANIFEST [C-28] block present before seal [C-28]: [confirmed]
  Phase 1 MANIFEST artifact count + namespace count recorded [C-28]: [confirmed]
  Phase 2 MANIFEST [C-28] block present before seal [C-28]: [confirmed]
  Phase 2 MANIFEST row count + EARNED count recorded [C-28]: [confirmed]
  -- C-29 checks --
  Phase 1 DUAL-LAYER BARRIER block names Layer 1 (STOP) [C-29]: [confirmed]
  Phase 1 DUAL-LAYER BARRIER block names Layer 2 (pre-printed) [C-29]: [confirmed]
  Phase 1 DUAL-LAYER BARRIER independence assertion present [C-29]: [confirmed]
  Phase 2 DUAL-LAYER BARRIER block names Layer 1 (STOP) [C-29]: [confirmed]
  Phase 2 DUAL-LAYER BARRIER block names Layer 2 (pre-printed) [C-29]: [confirmed]
  Phase 2 DUAL-LAYER BARRIER independence assertion present [C-29]: [confirmed]
  -- C-32 checks --
  Phase 1 CLOSURE GATE forward-binding assertion [C-32] present [C-32]: [confirmed]
  Phase 1 CLOSURE GATE names PHASE 1 MANIFEST as constraint source [C-32]: [confirmed]
  Phase 2 CLOSURE GATE forward-binding assertion [C-32] present [C-32]: [confirmed]
  Phase 2 CLOSURE GATE names PHASE 2 MANIFEST as constraint source [C-32]: [confirmed]
  -- Summary --
  Result: [N] gates checked. [2] STOP barriers (C-26). [2] closure gate confirmations (C-26).
    [2] [C-27]-tagged barriers (C-27). [2] MANIFEST blocks with 2 dimensions each (C-28).
    [2] dual-layer declarations with independence (C-29). [2] [C-32]-tagged forward-binding
    assertions in closure gates (C-32). Violations: [n].
  Fail Tier 1: Gate missing criterion ID -> halt.
  Fail Tier 2: CLOSURE GATE forward-binding assertion present but [C-32] tag absent -> finding.
  Fail Tier 2: CLOSURE GATE names MANIFEST but does not assert constraint direction -> finding.
  Fail Tier 3: Any barrier or closure gate permits retroactive Phase N alteration -> halt.
```

**Write artifact**: `simulations/topic/{{topic}}-achievements-{{date}}.md`

---

## V-04 -- Combined: C-30 Dedicated Section Tagging + C-31 Per-Phase Pair Expression

**Axes**: C-30 (V-01) + C-31 (V-02).

**Hypothesis**: V-01 isolates C-30 auditability ([C-30]-tagged section headers + SECTION
INVENTORY). V-02 isolates C-31 auditability ([C-31]-tagged per-phase pair expression).
Combining them creates two orthogonal structural properties in the STRUCTURAL AUDIT GATE:
each dedicated section is addressable by its [C-30] header, and within each section each
criterion check is expressed as a per-phase pair addressable by its [C-31] pair name.
Together, a scorer can verify C-30 (section present? check count >=2?) and C-31 (check
expressed as Phase 1 / Phase 2 pair?) independently using only string search. V-04 does
not include C-32; CLOSURE GATE forward-binding language from R10 V-05 baseline is present
implicitly but unlabeled.

---

You are running `topic-achievements`. Scan all signal artifacts for the topic. Compute
achievement state. Show contributor leaderboard and next recommended action.

**INPUT**: `{{topic}}` (auto-detect from context or TOPICS.md if not provided)

---

### OUTPUT SCHEMAS [C-37]

**Achievement row**: `| Category | Achievement | State | Evidence | Progress |`
State: EARNED / IN-PROGRESS / LOCKED (exactly one). [C-01]
Evidence: artifact path from Phase 1 STATE. [C-03]
Progress: `n of m [requirement]` for IN-PROGRESS; `--` otherwise. [C-04]

**Leaderboard row**: `| Rank | Contributor | Signals | Topics | Milestones | Score | Pattern |`

**1-Away row**: `| Topic/Milestone | Achievement | Gap | Exact Action |`

**Next action**: `Next: /[skill] [topic] -> produces [artifact] -> advances [Achievement] -> Unlocks [Achievement] -> Breaks [PATTERN]`

---

### REGISTRY PRIMACY GATE [C-24]

Read `simulations/TOPICS.md` before any phase begins.
The registry entry for `{{topic}}` is the **sole authoritative gate contract** for this skill.
Phase instructions are subordinate. Registry governs on conflict.

FAIL Tier 1 [C-25]: Topic absent -> halt.
FAIL Tier 3 [C-25]: Phase result contradicts registry -> registry governs, record override.

---

### ATTRIBUTION INTEGRITY GATE [C-24/C-30]

Before Phase 1 begins:
(1) Confirm `{{topic}}` in TOPICS.md. [C-24]
(2) Glob `simulations/**/{{topic}}-*.md`. Build ATTRIBUTION BASELINE: file count + contributor list.
(3) Record: `ATTRIBUTION BASELINE: [N] artifacts. Contributors: [list]`.

FAIL Tier 1 [C-25]: 0 artifacts -> halt.
FAIL Tier 2 [C-25]: Some frontmatter missing contributor field -> record count, continue.
FAIL Tier 3 [C-25]: Achievement names contributor not in ATTRIBUTION BASELINE -> halt.

---

### OUTPUT TEMPLATE [C-27/C-30/C-31]

Fill all `[FIELD]` values. Do not modify pre-printed headers, dividers, barrier lines,
MANIFEST labels, or DUAL-LAYER BARRIER blocks. Barriers marked `[C-26][C-27]` are
pre-printed structural elements (model transcribes, not generates). Each phase boundary
carries two independent barrier mechanisms: instruction-enforced STOP [C-26] and
structure-enforced pre-printed divider [C-27]. Both must fail simultaneously for barrier
omission [C-29]. The STRUCTURAL AUDIT GATE uses dedicated named sections tagged [C-30]
for each criterion C-27 or later; within each section, checks are expressed as per-phase
pairs tagged [C-31] so that Phase 1 and Phase 2 compliance are independently verifiable.

```
## PHASE 1 -- EVIDENCE SCAN

SCAN STATE:
  Namespaces with signals: [list]
  Per-namespace count: [ns: n, ns: n, ...]
  Total signals: [N]
  Milestones (from registry): [M]
  Contributors: [list]
  Earliest: [date]  Latest: [date]

SCAN GATE [C-01/C-15]:
  (1) simulations/ accessible; glob >= 1 file.
  (2) All files assigned to known namespace.
  (3) Contributor list matches ATTRIBUTION BASELINE.
  (4) PHASE 1 STATE complete.
  Pass: "SCAN GATE [C-01/C-15]: [N] signals, [M] namespaces. Contributors: [list]."
  Fail Tier 1: "SCAN GATE FAIL [C-01/C-15]: [condition] -- [path]."

PHASE 1 MANIFEST [C-28]:
  Artifact count: [K]
  Namespace count: [N]

PHASE 1 CLOSURE GATE [C-26]:
  (1) Verify PHASE 1 MANIFEST [C-28] is recorded above with artifact count and namespace count.
  (2) Phase 2 inputs are limited to items in PHASE 1 MANIFEST. Phase 2 may not
      introduce artifact data not present in PHASE 1 STATE.
  Pass: "PHASE 1 CLOSURE GATE [C-26]: Manifest verified ([K] artifacts, [N] namespaces).
    Phase 2 inputs constrained to PHASE 1 MANIFEST."

STOP. Phase 1 complete. [C-26]
--- PHASE 1 SEALED [C-26][C-27] ---
DUAL-LAYER BARRIER [C-26/C-27][C-29]:
  Layer 1: STOP declaration above (instruction-enforced) [C-26]
  Layer 2: Pre-printed divider above (structure-enforced -- model transcribes, not generates) [C-27]
  Independence: Layer 1 fails if model omits the STOP instruction; Layer 2 fails if model
    actively skips or deletes a pre-printed element. Both must fail simultaneously for
    barrier omission. [C-29]
Phase 1 scan results are closed. PHASE 1 STATE and PHASE 1 MANIFEST are immutable.
Phase 2 reads PHASE 1 STATE above. Phase 2 may not alter signal counts,
contributor lists, namespace assignments, or artifact citations.

## PHASE 2 -- ACHIEVEMENT CLASSIFICATION

Achievement table (use PHASE 1 STATE only; all 7 categories required) [C-06]:

| Category       | Achievement         | State              | Evidence [C-03]  | Progress [C-04]   |
|----------------|---------------------|-------------------|------------------|-------------------|
| Exploration    | Namespace Spread    | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Depth          | Signal Depth        | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Coverage       | Full Coverage       | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Quality        | Falsified [C-02]    | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Chain          | Signal Chain        | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Discovery      | Unexpected Echo     | [EARNED/LOC]      | [artifact path]  | [--]              |
| Corps/Crew     | Team Breadth        | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |

CLASSIFICATION GATE [C-03/C-25]:
  (1) Every EARNED row cites artifact path from PHASE 1 STATE. [C-03]
  (2) Every IN-PROGRESS row shows `n of m` form. [C-04]
  (3) All 7 categories appear. [C-06]
  (4) No citation to path absent from PHASE 1 STATE.
  Fail Tier 2: Missing citation -> `(UNCITED)`. Fail Tier 3: Absent path -> halt.

1-AWAY TABLE [C-09/C-18]:
| Topic/Milestone | Achievement | Gap | Exact Action |
|-----------------|-------------|-----|--------------|
| [item]          | [name]      | [n] | [action]     |

Pattern [C-17]: [SOLO_ISLAND / NAMESPACE_MOAT / SPRINT_FREEZE / SHALLOW_POOL / ORPHAN_TOPIC / NONE]

PHASE 2 STATE:
  Rows: [7] | 1-Away: [N] | Pattern: [label] | Dominant contributor: [name]

PHASE 2 MANIFEST [C-28]:
  Achievement row count: 7
  EARNED count: [N]

PHASE 2 CLOSURE GATE [C-26]:
  (1) Verify PHASE 2 MANIFEST [C-28] is recorded above with row count and EARNED count.
  (2) Phase 3 inputs are limited to items in PHASE 2 MANIFEST. Phase 3 may not
      alter EARNED/IN-PROGRESS/LOCKED assignments or category coverage decisions.
  Pass: "PHASE 2 CLOSURE GATE [C-26]: Manifest verified (7 rows, [N] EARNED).
    Phase 3 inputs constrained to PHASE 2 MANIFEST."

STOP. Phase 2 complete. [C-26]
--- PHASE 2 SEALED [C-26][C-27] ---
DUAL-LAYER BARRIER [C-26/C-27][C-29]:
  Layer 1: STOP declaration above (instruction-enforced) [C-26]
  Layer 2: Pre-printed divider above (structure-enforced -- model transcribes, not generates) [C-27]
  Independence: Layer 1 fails if model omits the STOP instruction; Layer 2 fails if model
    actively skips or deletes a pre-printed element. Both must fail simultaneously for
    barrier omission. [C-29]
Phase 2 classifications are closed. PHASE 2 STATE and PHASE 2 MANIFEST are immutable.
Phase 3 reads PHASE 2 STATE above. Phase 3 may not alter EARNED/IN-PROGRESS/LOCKED
assignments or category coverage decisions.

## PHASE 3 -- OUTPUT

PRE-WRITE GATE [C-11]: All values in tables below derive from PHASE 1 STATE and PHASE 2 STATE.
No artifact rescanning required.
  [Confirmation: pass / Fail: [specific value requiring rescan and corrective action]]

LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]:
  Formula: Score = (Signals x 1) + (Topics x 3) + (Milestones x 5) [C-16]
  | Rank | Contributor | Signals | Topics | Milestones | Score | Pattern |
  Rank 1 worked example [C-19]: Score = [S]x1 + [T]x3 + [M]x5 = [total]
  Correction [C-21]: [applied: [old]->[new] / not needed]
  Label enumeration (C-25): [C-16/C-19/C-21] verified.
  Pass: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Formula (C-16): confirmed.
    Example (C-19): [total]. Correction (C-21): [applied/not needed].
    Label enumeration (C-25): [C-16/C-19/C-21] verified."

**TEAM INSIGHT -- [descriptive name] [C-13]:** [cross-table synthesis finding]

INSIGHT GATE [C-13/C-22]:
  (1) Names specific pattern or contributor: [confirmed]
  (2) Not a single-row restatement: [confirmed]
  (3) Requires cross-table synthesis; not derivable from achievements table alone [C-22]: [confirmed]

ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]:
  Next: /[skill] [topic] -> produces [artifact] -> advances [Achievement] [C-05]
    -> Unlocks [Achievement] -> Breaks [PATTERN] [C-12]
  (1) Names specific skill, artifact, advancement [C-05]: confirmed
  (2) Unlock chain present [C-12]: confirmed
  (3) Registry labels exact, no invented labels [C-14]: confirmed
  (4) All gates in this run carry criterion ID [C-20]: confirmed
  (5) Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified.
  Fail Tier 1: Gate missing criterion ID -> halt.
  Fail Tier 3: Criterion ID replaced by narrative -> halt.
  Pass: "ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]: Action (C-05): confirmed.
    Unlock chain (C-12): confirmed. Registry labels (C-14): confirmed.
    Gate IDs (C-20): confirmed. Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified."

STRUCTURAL AUDIT GATE [C-20/C-26/C-27/C-28/C-29/C-30/C-31]:
  Gates executed: [list all gate labels in this run]
  All carry criterion ID [C-20]: [confirmed / violations: list]
  LEADERBOARD CLUSTER enumerates C-16, C-19, C-21 [C-25]: [confirmed]
  ACTIONS CLUSTER enumerates C-05, C-12, C-14, C-20 [C-25]: [confirmed]
  -- C-26 SECTION --
  STOP barrier written [C-31]:
    Phase 1: STOP barrier present: [confirmed]
    Phase 2: STOP barrier present: [confirmed]
  CLOSURE GATE pass confirmation [C-31]:
    Phase 1: pass confirmation recorded: [confirmed]
    Phase 2: pass confirmation recorded: [confirmed]
  -- C-27 SECTION [C-30] --
  [C-27] tag on pre-printed barrier [C-31]:
    Phase 1: "--- PHASE 1 SEALED [C-26][C-27] ---" with [C-27] tag: [confirmed]
    Phase 2: "--- PHASE 2 SEALED [C-26][C-27] ---" with [C-27] tag: [confirmed]
  DUAL-LAYER BARRIER cites barrier as Layer 2 [C-31]:
    Phase 1: Layer 2 pre-printed reference present: [confirmed]
    Phase 2: Layer 2 pre-printed reference present: [confirmed]
  -- C-28 SECTION [C-30] --
  MANIFEST block present before seal [C-31]:
    Phase 1: PHASE 1 MANIFEST [C-28] present: [confirmed]
    Phase 2: PHASE 2 MANIFEST [C-28] present: [confirmed]
  MANIFEST records two dimensions [C-31]:
    Phase 1: artifact count + namespace count: [confirmed]
    Phase 2: row count + EARNED count: [confirmed]
  -- C-29 SECTION [C-30] --
  DUAL-LAYER BARRIER names both layers [C-31]:
    Phase 1: Layer 1 (STOP) + Layer 2 (pre-printed) named: [confirmed]
    Phase 2: Layer 1 (STOP) + Layer 2 (pre-printed) named: [confirmed]
  DUAL-LAYER BARRIER independence assertion [C-31]:
    Phase 1: independence assertion present: [confirmed]
    Phase 2: independence assertion present: [confirmed]
  -- C-30 SECTION INVENTORY [C-30] --
  C-27 section header "-- C-27 SECTION [C-30] --" present [C-30]: [confirmed]
  C-27 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30]: [confirmed]
  C-28 section header "-- C-28 SECTION [C-30] --" present [C-30]: [confirmed]
  C-28 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30]: [confirmed]
  C-29 section header "-- C-29 SECTION [C-30] --" present [C-30]: [confirmed]
  C-29 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30]: [confirmed]
  -- Summary --
  Result: [N] gates checked. [2] STOP barriers (C-26). [2] closure gate confirmations (C-26).
    [2] [C-27]-tagged barriers (C-27). [2] MANIFEST blocks with 2 dimensions each (C-28).
    [2] dual-layer declarations with independence (C-29). [3] dedicated [C-30]-tagged
    sections with >=2 per-phase pairs each (C-30). All C-27/C-28/C-29 checks as per-phase
    pairs with [C-31] tags (C-31). Violations: [n].
  Fail Tier 1: Gate missing criterion ID -> halt.
  Fail Tier 2: [C-30] section header absent for any criterion C-27+ -> finding.
  Fail Tier 2: Per-phase pair expressed as global assertion (missing [C-31] tag) -> finding.
  Fail Tier 3: Any barrier or closure gate permits retroactive Phase N alteration -> halt.
```

**Write artifact**: `simulations/topic/{{topic}}-achievements-{{date}}.md`

---

## V-05 -- Full Integration: C-30 + C-31 + C-32

**Axes**: All three R11 mechanisms combined.
- V-01 axis: [C-30] tags on dedicated section headers + SECTION INVENTORY
- V-02 axis: [C-31] per-phase pair expression within each section
- V-03 axis: [C-32] forward-binding assertion in CLOSURE GATE + dedicated C-32 section

**Hypothesis**: V-01 makes C-30 individually auditable ([C-30] on section headers +
SECTION INVENTORY declares counts). V-02 makes C-31 individually auditable ([C-31] on
per-phase pair names). V-03 makes C-32 individually auditable ([C-32] on forward-binding
assertion + dedicated C-32 section). Combined, each new criterion has a named, directly
addressable evidence point: C-30 by searching for `[C-30]` section headers and the
SECTION INVENTORY, C-31 by searching for `[C-31]`-tagged pair names with Phase 1/Phase 2
sub-checks, C-32 by searching for `[C-32]` in CLOSURE GATE pass confirmation lines. The
C-32 section itself gets [C-30] tagging and [C-31] per-phase pair structure, making all
four new-criterion sections (C-27, C-28, C-29, C-32) uniformly structured. The SECTION
INVENTORY in V-05 lists all four sections and their pair counts. Risk: the STRUCTURAL
AUDIT GATE grows substantially; however, the gate is pre-printed -- the model fills
confirmed/count values into labeled slots, not the section structure or pair names.

---

You are running `topic-achievements`. Scan all signal artifacts for the topic. Compute
achievement state. Show contributor leaderboard and next recommended action.

**INPUT**: `{{topic}}` (auto-detect from context or TOPICS.md if not provided)

---

### OUTPUT SCHEMAS [C-37]

**Achievement row**: `| Category | Achievement | State | Evidence | Progress |`
State: EARNED / IN-PROGRESS / LOCKED (exactly one). [C-01]
Evidence: artifact path from Phase 1 STATE. [C-03]
Progress: `n of m [requirement]` for IN-PROGRESS; `--` otherwise. [C-04]

**Leaderboard row**: `| Rank | Contributor | Signals | Topics | Milestones | Score | Pattern |`

**1-Away row**: `| Topic/Milestone | Achievement | Gap | Exact Action |`

**Next action**: `Next: /[skill] [topic] -> produces [artifact] -> advances [Achievement] -> Unlocks [Achievement] -> Breaks [PATTERN]`

---

### REGISTRY PRIMACY GATE [C-24]

Read `simulations/TOPICS.md` before any phase begins.
The registry entry for `{{topic}}` is the **sole authoritative gate contract** for this skill.
Phase instructions are subordinate. Registry governs on conflict.

FAIL Tier 1 [C-25]: Topic absent -> halt.
FAIL Tier 3 [C-25]: Phase result contradicts registry -> registry governs, record override.

---

### ATTRIBUTION INTEGRITY GATE [C-24/C-30]

Before Phase 1 begins:
(1) Confirm `{{topic}}` in TOPICS.md. [C-24]
(2) Glob `simulations/**/{{topic}}-*.md`. Build ATTRIBUTION BASELINE: file count + contributor list.
(3) Record: `ATTRIBUTION BASELINE: [N] artifacts. Contributors: [list]`.

FAIL Tier 1 [C-25]: 0 artifacts -> halt.
FAIL Tier 2 [C-25]: Some frontmatter missing contributor field -> record count, continue.
FAIL Tier 3 [C-25]: Achievement names contributor not in ATTRIBUTION BASELINE -> halt.

---

### OUTPUT TEMPLATE [C-27/C-30/C-31/C-32]

Fill all `[FIELD]` values. Do not modify pre-printed headers, dividers, barrier lines,
MANIFEST labels, DUAL-LAYER BARRIER blocks, or STRUCTURAL AUDIT GATE section headers.
Barriers marked `[C-26][C-27]` are pre-printed structural elements (model transcribes,
not generates). Each phase boundary carries two independent barrier mechanisms:
instruction-enforced STOP [C-26] and structure-enforced pre-printed divider [C-27]; both
must fail simultaneously for barrier omission [C-29]. Each CLOSURE GATE includes a
forward-binding constraint assertion [C-32] tying Phase N+1 scope to the Phase N
MANIFEST; any scope expansion directly contradicts this claim. The STRUCTURAL AUDIT GATE
uses dedicated named sections tagged [C-30] for each criterion C-27 or later (C-27,
C-28, C-29, C-32); within each section, checks are expressed as per-phase pairs tagged
[C-31] with Phase 1 and Phase 2 verified independently.

```
## PHASE 1 -- EVIDENCE SCAN

SCAN STATE:
  Namespaces with signals: [list]
  Per-namespace count: [ns: n, ns: n, ...]
  Total signals: [N]
  Milestones (from registry): [M]
  Contributors: [list]
  Earliest: [date]  Latest: [date]

SCAN GATE [C-01/C-15]:
  (1) simulations/ accessible; glob >= 1 file.
  (2) All files assigned to known namespace.
  (3) Contributor list matches ATTRIBUTION BASELINE.
  (4) PHASE 1 STATE complete.
  Pass: "SCAN GATE [C-01/C-15]: [N] signals, [M] namespaces. Contributors: [list]."
  Fail Tier 1: "SCAN GATE FAIL [C-01/C-15]: [condition] -- [path]."

PHASE 1 MANIFEST [C-28]:
  Artifact count: [K]
  Namespace count: [N]

PHASE 1 CLOSURE GATE [C-26/C-32]:
  (1) Verify PHASE 1 MANIFEST [C-28] is recorded above with artifact count and namespace count.
  (2) Phase 2 inputs constrained to PHASE 1 MANIFEST [C-32]. Any Phase 2 artifact scope
      not present in PHASE 1 MANIFEST above directly contradicts this assertion.
  Pass: "PHASE 1 CLOSURE GATE [C-26]: Manifest verified ([K] artifacts, [N] namespaces).
    Phase 2 inputs constrained to PHASE 1 MANIFEST [C-32]."

STOP. Phase 1 complete. [C-26]
--- PHASE 1 SEALED [C-26][C-27] ---
DUAL-LAYER BARRIER [C-26/C-27][C-29]:
  Layer 1: STOP declaration above (instruction-enforced) [C-26]
  Layer 2: Pre-printed divider above (structure-enforced -- model transcribes, not generates) [C-27]
  Independence: Layer 1 fails if model omits the STOP instruction; Layer 2 fails if model
    actively skips or deletes a pre-printed element. Both must fail simultaneously for
    barrier omission. [C-29]
Phase 1 scan results are closed. PHASE 1 STATE and PHASE 1 MANIFEST are immutable.
Phase 2 reads PHASE 1 STATE above. Phase 2 may not alter signal counts,
contributor lists, namespace assignments, or artifact citations.

## PHASE 2 -- ACHIEVEMENT CLASSIFICATION

Achievement table (use PHASE 1 STATE only; all 7 categories required) [C-06]:

| Category       | Achievement         | State              | Evidence [C-03]  | Progress [C-04]   |
|----------------|---------------------|-------------------|------------------|-------------------|
| Exploration    | Namespace Spread    | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Depth          | Signal Depth        | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Coverage       | Full Coverage       | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Quality        | Falsified [C-02]    | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Chain          | Signal Chain        | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Discovery      | Unexpected Echo     | [EARNED/LOC]      | [artifact path]  | [--]              |
| Corps/Crew     | Team Breadth        | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |

CLASSIFICATION GATE [C-03/C-25]:
  (1) Every EARNED row cites artifact path from PHASE 1 STATE. [C-03]
  (2) Every IN-PROGRESS row shows `n of m` form. [C-04]
  (3) All 7 categories appear. [C-06]
  (4) No citation to path absent from PHASE 1 STATE.
  Fail Tier 2: Missing citation -> `(UNCITED)`. Fail Tier 3: Absent path -> halt.

1-AWAY TABLE [C-09/C-18]:
| Topic/Milestone | Achievement | Gap | Exact Action |
|-----------------|-------------|-----|--------------|
| [item]          | [name]      | [n] | [action]     |

Pattern [C-17]: [SOLO_ISLAND / NAMESPACE_MOAT / SPRINT_FREEZE / SHALLOW_POOL / ORPHAN_TOPIC / NONE]

PHASE 2 STATE:
  Rows: [7] | 1-Away: [N] | Pattern: [label] | Dominant contributor: [name]

PHASE 2 MANIFEST [C-28]:
  Achievement row count: 7
  EARNED count: [N]

PHASE 2 CLOSURE GATE [C-26/C-32]:
  (1) Verify PHASE 2 MANIFEST [C-28] is recorded above with row count and EARNED count.
  (2) Phase 3 inputs constrained to PHASE 2 MANIFEST [C-32]. Any Phase 3 scope not
      present in PHASE 2 MANIFEST above directly contradicts this assertion.
  Pass: "PHASE 2 CLOSURE GATE [C-26]: Manifest verified (7 rows, [N] EARNED).
    Phase 3 inputs constrained to PHASE 2 MANIFEST [C-32]."

STOP. Phase 2 complete. [C-26]
--- PHASE 2 SEALED [C-26][C-27] ---
DUAL-LAYER BARRIER [C-26/C-27][C-29]:
  Layer 1: STOP declaration above (instruction-enforced) [C-26]
  Layer 2: Pre-printed divider above (structure-enforced -- model transcribes, not generates) [C-27]
  Independence: Layer 1 fails if model omits the STOP instruction; Layer 2 fails if model
    actively skips or deletes a pre-printed element. Both must fail simultaneously for
    barrier omission. [C-29]
Phase 2 classifications are closed. PHASE 2 STATE and PHASE 2 MANIFEST are immutable.
Phase 3 reads PHASE 2 STATE above. Phase 3 may not alter EARNED/IN-PROGRESS/LOCKED
assignments or category coverage decisions.

## PHASE 3 -- OUTPUT

PRE-WRITE GATE [C-11]: All values in tables below derive from PHASE 1 STATE and PHASE 2 STATE.
No artifact rescanning required.
  [Confirmation: pass / Fail: [specific value requiring rescan and corrective action]]

LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]:
  Formula: Score = (Signals x 1) + (Topics x 3) + (Milestones x 5) [C-16]
  | Rank | Contributor | Signals | Topics | Milestones | Score | Pattern |
  Rank 1 worked example [C-19]: Score = [S]x1 + [T]x3 + [M]x5 = [total]
  Correction [C-21]: [applied: [old]->[new] / not needed]
  Label enumeration (C-25): [C-16/C-19/C-21] verified.
  Pass: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Formula (C-16): confirmed.
    Example (C-19): [total]. Correction (C-21): [applied/not needed].
    Label enumeration (C-25): [C-16/C-19/C-21] verified."

**TEAM INSIGHT -- [descriptive name] [C-13]:** [cross-table synthesis finding]

INSIGHT GATE [C-13/C-22]:
  (1) Names specific pattern or contributor: [confirmed]
  (2) Not a single-row restatement: [confirmed]
  (3) Requires cross-table synthesis; not derivable from achievements table alone [C-22]: [confirmed]

ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]:
  Next: /[skill] [topic] -> produces [artifact] -> advances [Achievement] [C-05]
    -> Unlocks [Achievement] -> Breaks [PATTERN] [C-12]
  (1) Names specific skill, artifact, advancement [C-05]: confirmed
  (2) Unlock chain present [C-12]: confirmed
  (3) Registry labels exact, no invented labels [C-14]: confirmed
  (4) All gates in this run carry criterion ID [C-20]: confirmed
  (5) Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified.
  Fail Tier 1: Gate missing criterion ID -> halt.
  Fail Tier 3: Criterion ID replaced by narrative -> halt.
  Pass: "ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]: Action (C-05): confirmed.
    Unlock chain (C-12): confirmed. Registry labels (C-14): confirmed.
    Gate IDs (C-20): confirmed. Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified."

STRUCTURAL AUDIT GATE [C-20/C-26/C-27/C-28/C-29/C-30/C-31/C-32]:
  Gates executed: [list all gate labels in this run]
  All carry criterion ID [C-20]: [confirmed / violations: list]
  LEADERBOARD CLUSTER enumerates C-16, C-19, C-21 [C-25]: [confirmed]
  ACTIONS CLUSTER enumerates C-05, C-12, C-14, C-20 [C-25]: [confirmed]
  -- C-26 SECTION --
  STOP barrier written [C-31]:
    Phase 1: STOP barrier present: [confirmed]
    Phase 2: STOP barrier present: [confirmed]
  CLOSURE GATE pass confirmation [C-31]:
    Phase 1: pass confirmation recorded: [confirmed]
    Phase 2: pass confirmation recorded: [confirmed]
  -- C-27 SECTION [C-30] --
  [C-27] tag on pre-printed barrier [C-31]:
    Phase 1: "--- PHASE 1 SEALED [C-26][C-27] ---" with [C-27] tag: [confirmed]
    Phase 2: "--- PHASE 2 SEALED [C-26][C-27] ---" with [C-27] tag: [confirmed]
  DUAL-LAYER BARRIER cites barrier as Layer 2 [C-31]:
    Phase 1: Layer 2 pre-printed reference present: [confirmed]
    Phase 2: Layer 2 pre-printed reference present: [confirmed]
  -- C-28 SECTION [C-30] --
  MANIFEST block present before seal [C-31]:
    Phase 1: PHASE 1 MANIFEST [C-28] present: [confirmed]
    Phase 2: PHASE 2 MANIFEST [C-28] present: [confirmed]
  MANIFEST records two dimensions [C-31]:
    Phase 1: artifact count + namespace count: [confirmed]
    Phase 2: row count + EARNED count: [confirmed]
  -- C-29 SECTION [C-30] --
  DUAL-LAYER BARRIER names both layers [C-31]:
    Phase 1: Layer 1 (STOP) + Layer 2 (pre-printed) named: [confirmed]
    Phase 2: Layer 1 (STOP) + Layer 2 (pre-printed) named: [confirmed]
  DUAL-LAYER BARRIER independence assertion [C-31]:
    Phase 1: independence assertion present: [confirmed]
    Phase 2: independence assertion present: [confirmed]
  -- C-32 SECTION [C-30] --
  CLOSURE GATE forward-binding assertion [C-32] present [C-31]:
    Phase 1: "[C-32]" tag in PHASE 1 CLOSURE GATE pass confirmation: [confirmed]
    Phase 2: "[C-32]" tag in PHASE 2 CLOSURE GATE pass confirmation: [confirmed]
  CLOSURE GATE names Phase N MANIFEST as constraint source [C-31]:
    Phase 1: "PHASE 1 MANIFEST" named as constraint source: [confirmed]
    Phase 2: "PHASE 2 MANIFEST" named as constraint source: [confirmed]
  -- C-30 SECTION INVENTORY [C-30] --
  C-27 section header "-- C-27 SECTION [C-30] --" present [C-30]: [confirmed]
  C-27 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30]: [confirmed]
  C-28 section header "-- C-28 SECTION [C-30] --" present [C-30]: [confirmed]
  C-28 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30]: [confirmed]
  C-29 section header "-- C-29 SECTION [C-30] --" present [C-30]: [confirmed]
  C-29 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30]: [confirmed]
  C-32 section header "-- C-32 SECTION [C-30] --" present [C-30]: [confirmed]
  C-32 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30]: [confirmed]
  -- Summary --
  Result: [N] gates. [2] STOP barriers (C-26). [2] closure gate confirmations (C-26).
    [2] [C-27]-tagged barriers (C-27). [2] MANIFEST blocks with 2 dimensions each (C-28).
    [2] dual-layer declarations with independence (C-29). [4] dedicated [C-30]-tagged
    sections with >=2 per-phase pairs each (C-30). All C-27/C-28/C-29/C-32 checks as
    per-phase pairs with [C-31] tags (C-31). [2] [C-32]-tagged forward-binding assertions
    in closure gates (C-32). Violations: [n].
  Fail Tier 1: Gate missing criterion ID -> halt.
  Fail Tier 2: [C-30] section header absent for any criterion C-27+ -> finding.
  Fail Tier 2: Section pair count < 2 for any [C-30] section -> finding.
  Fail Tier 2: Check expressed as global assertion not per-phase pair -> finding.
  Fail Tier 2: CLOSURE GATE forward-binding present but [C-32] tag absent -> finding.
  Fail Tier 3: Any barrier or closure gate permits retroactive Phase N alteration -> halt.
```

**Write artifact**: `simulations/topic/{{topic}}-achievements-{{date}}.md`

---

## Variation Summary

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| [C-30] tag on dedicated section headers | YES | -- | -- | YES | YES |
| C-30 SECTION INVENTORY step | YES | -- | -- | YES | YES |
| [C-31] per-phase pair expression | -- | YES | -- | YES | YES |
| [C-32] tag on CLOSURE GATE forward-binding | -- | -- | YES | -- | YES |
| Dedicated C-32 audit section | -- | -- | YES | -- | YES |
| Structural audit checks C-30 by name | YES | -- | -- | YES | YES |
| Structural audit checks C-31 by name | -- | YES | -- | YES | YES |
| Structural audit checks C-32 by name | -- | -- | YES | -- | YES |
| New mechanism count | 1 | 1 | 1 | 2 | 3 |

## C-30/C-31/C-32 Failure Mode Coverage

| Failure Mode | V-01 | V-02 | V-03 | V-04 | V-05 |
|--------------|------|------|------|------|------|
| C-30: section absent for a criterion C-27+ | DETECTED (INVENTORY check) | Undetected | Undetected | DETECTED | DETECTED |
| C-30: section present but check count < 2 | DETECTED (INVENTORY count) | Undetected | Undetected | DETECTED | DETECTED |
| C-31: criterion check expressed globally not per-phase | Undetected | DETECTED ([C-31] pair check) | Undetected | DETECTED | DETECTED |
| C-31: Phase 2 check omitted while Phase 1 passes | Undetected | DETECTED (pair sub-check) | Undetected | DETECTED | DETECTED |
| C-32: forward-binding language absent from CLOSURE GATE | Undetected | Undetected | DETECTED ([C-32] check) | Undetected | DETECTED |
| C-32: manifest cited but constraint direction unlabeled | Undetected | Undetected | DETECTED (dedicated section) | Undetected | DETECTED |
| Retroactive scope expansion via reinterpretation | Implicitly blocked (C-28 manifest) | Implicitly blocked | EXPLICITLY BLOCKED ([C-32] assertion) | Implicitly blocked | EXPLICITLY BLOCKED |

## Predicted Scoring (rubric v11)

Aspirational formula: `aspirational_pass / 24 * 10`. C-09 through C-32 = 24 criteria.

**V-01**: C-09--C-29 PASS (baseline). C-30: PASS (tagged section headers + SECTION
INVENTORY with confirmed counts). C-31: borderline PASS (V-05 R10 baseline has separate
Phase 1/Phase 2 lines, satisfying C-31 structurally; no [C-31] tags but per-phase
granularity is present). C-32: borderline PASS (CLOSURE GATE says "constrained to
MANIFEST" implicitly from baseline; no [C-32] tag, but forward-binding language present).
Predicted: 22-24/24 aspirational.

**V-02**: C-09--C-29 PASS. C-30: borderline PASS (sections exist from baseline structure;
no [C-30] tags, section headers are plain). C-31: PASS (explicit [C-31]-tagged per-phase
pairs in all C-27/C-28/C-29 sections). C-32: borderline PASS (baseline forward-binding
present but unlabeled). Predicted: 22-24/24 aspirational.

**V-03**: C-09--C-29 PASS. C-30: borderline PASS (sections exist; C-32 section is new
and named but not [C-30]-tagged). C-31: borderline PASS (C-32 checks are per-phase but
no [C-31] tags on them). C-32: PASS (explicit [C-32] tag in CLOSURE GATE pass +
dedicated C-32 audit section with per-phase checks). Predicted: 23-24/24 aspirational.

**V-04**: C-09--C-29 PASS. C-30: PASS (tagged section headers + SECTION INVENTORY).
C-31: PASS ([C-31]-tagged per-phase pairs in all sections). C-32: borderline PASS
(baseline forward-binding present but unlabeled; manifest scope constraint implied
by C-28 MANIFEST). Predicted: 23-24/24 aspirational.

**V-05**: C-09--C-29 PASS. C-30: PASS (4 [C-30]-tagged sections + SECTION INVENTORY
with pair counts). C-31: PASS (all C-27/C-28/C-29/C-32 checks as [C-31]-tagged per-
phase pairs). C-32: PASS ([C-32] tag in both CLOSURE GATE pass confirmations + dedicated
C-32 section; forward-binding named and labeled). Predicted: 24/24 aspirational.

**Predicted top performer**: V-05 -- all three new criteria have named, directly
addressable evidence points individually checkable in the STRUCTURAL AUDIT GATE
[C-20/C-26/C-27/C-28/C-29/C-30/C-31/C-32]. V-05 is the only variation where a scorer
can verify each criterion C-27 through C-32 by direct string match without interpretation.
The C-32 SECTION uses [C-30] tagging and [C-31] per-phase pair structure, making it
the first criterion section introduced in R11 with all R11 mechanisms applied to itself.

**Open excellence signals** (C-33+ candidates):

- V-05 introduces a C-30 SECTION INVENTORY that counts pairs and individual checks.
  A potential C-33 criterion: the SECTION INVENTORY includes a C-31 compliance assertion
  per section ("all checks in this section expressed as per-phase pairs"), converting
  C-31 verification from a per-pair check across the gate into a per-section declaration.

- V-03/V-05 adds a C-32 forward-binding assertion naming Phase N MANIFEST as constraint
  source. A potential C-34 criterion: the CLOSURE GATE records the Phase N MANIFEST
  digest (artifact count + namespace count) *inline* in the forward-binding assertion
  ("Phase 2 inputs constrained to PHASE 1 MANIFEST: [K] artifacts, [N] namespaces
  [C-32]"), making the constraint reference self-contained and eliminating the need to
  cross-reference the MANIFEST block to determine what scope was locked.
