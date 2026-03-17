---
skill: quest-variate
skill_target: topic-achievements
round: 12
date: 2026-03-17
rubric_version: 12
basis: V-05 R11 scored 100 on rubric v11 (C-01--C-32, 24/24 aspirational). Rubric v12
       extracts two new aspirational criteria from V-05 R11 excellence signals. C-33: V-05
       R11's SECTION INVENTORY declares pair counts per section ([C-30]) but does not
       annotate the pair count line with [C-31], leaving per-section C-31 compliance
       inferred from section body traversal rather than declared in the INVENTORY. C-34:
       V-05 R11's CLOSURE GATE forward-binding assertion names the MANIFEST ("Phase N+1
       inputs constrained to PHASE N MANIFEST [C-32]") but does not embed the manifest
       dimension values inline, leaving the constraint referential rather than numerically
       falsifiable. R12 formalizes both as explicitly labeled, individually auditable
       mechanisms. N_aspirational = 26. Scoring formula: aspirational_pass / 26 * 10
       (was /24).
---

# Variate R12 -- topic-achievements (2026-03-17)

5 complete prompt body variations for the `topic-achievements` skill.
Single-axis variations first (V-01 through V-02), then combinations (V-03 through V-05).

Rubric v12 adds two new aspirational criteria beyond the v11 baseline:

- **C-33 (new)**: Per-section [C-31] compliance declaration in SECTION INVENTORY -- from
  V-05 R11's SECTION INVENTORY pattern. C-30 requires a SECTION INVENTORY that records
  each C-27+ section by name and pair count. C-31 requires that each section's checks be
  expressed as per-phase named pairs. The SECTION INVENTORY satisfying C-30 declares that
  each section exists with a pair count; it does not declare whether those pairs carry
  [C-31] tags. Without a [C-31] annotation on the pair count line, a checker verifying
  C-31 compliance for a specific section must traverse that section body, accumulate pair
  tags manually, and determine compliance by structural interpretation rather than by a
  string match in the INVENTORY. C-33 tests whether the SECTION INVENTORY pair count line
  for each C-27+ section carries a [C-31] tag alongside the existing [C-30] tag, making
  per-section C-31 compliance a string-match-verifiable fact. A checker locates the
  INVENTORY, finds the pair count line for any section, and confirms [C-31] presence
  without reading section bodies. **C-33 requires C-30 and C-31 as preconditions.**
  Closes the gap that C-30 alone leaves open: INVENTORY records pair counts but does not
  assert per-phase pair structure is applied to all of them.

- **C-34 (new)**: Inline manifest digest in CLOSURE GATE forward-binding assertion --
  from V-05 R11's C-32 assertion pattern. C-32 requires the CLOSURE GATE to include an
  explicit forward-binding constraint: "Phase N+1 inputs constrained to PHASE N MANIFEST
  [C-32]." This assertion is referential -- it names the manifest but does not quantify
  it. A future reinterpretation that produces N+K artifacts can reference the MANIFEST
  while expanding scope without contradicting a stated count. C-34 tests whether the
  CLOSURE GATE forward-binding assertion embeds the Phase N MANIFEST dimension values
  (artifact count + second dimension) inline: "Phase N+1 inputs constrained to PHASE N
  MANIFEST: [K] artifacts, [N] namespaces [C-32/C-34]." The count converts the constraint
  from referential to falsifiable -- any Phase N+1 execution producing a set of size != K
  directly contradicts an explicit in-gate claim. **C-34 requires C-28 and C-32 as
  preconditions.** Closes the gap C-32 alone does not close: constraint asserted but not
  numerically grounded.

All variations carry the full v11 baseline: essential C-01--C-05, recommended C-06--C-08,
aspirational C-09--C-32. Scoring formula: `(essential_pass/5 * 60) + (recommended_pass/3
* 30) + (aspirational_pass/26 * 10)`.

---

## Variation Axes Selected

| Axis | Hypothesis | Used In |
|------|------------|---------|
| C-33: [C-31] tag on SECTION INVENTORY pair count lines | Adding [C-31] to each section's pair count line in the INVENTORY converts per-section C-31 compliance from inferred (traverse body) to declared (string-match INVENTORY) | V-01, V-03, V-04, V-05 |
| C-34: inline manifest dimension values in CLOSURE GATE forward-binding | Embedding [K] artifacts + [N] namespaces inline in the forward-binding assertion converts the constraint from referential (names MANIFEST) to falsifiable (states MANIFEST size) | V-02, V-03, V-04, V-05 |
| Self-application: C-33/C-34 SECTION INVENTORY entries also carry [C-31] | New criterion sections (C-33, C-34) introduced in R12 must themselves receive [C-31] annotations in the INVENTORY or C-33 is incomplete for those sections | V-05 |

---

## V-01 -- Single Axis: C-33 SECTION INVENTORY [C-31] Annotations

**Axis**: C-33 -- add `[C-31]` tag to the pair count line of each C-27+ section entry in
the C-30 SECTION INVENTORY. Current R11 V-05 format: `C-27 section pair count: [2] pairs
x 2 phases = [4] individual checks (required: >=2) [C-30]: [confirmed]`. V-01 format:
`C-27 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2)
[C-30/C-31]: [confirmed]`. Apply to sections C-27, C-28, C-29, C-32. Add a new `-- C-33
SECTION [C-30] --` in the STRUCTURAL AUDIT GATE with 2 [C-31]-tagged pairs verifying
the [C-31] annotations exist in the INVENTORY. Add C-33 entry to the INVENTORY with pair
count (no [C-31] self-annotation -- V-01 gap). No C-34 changes.

**Hypothesis**: V-05 R11's SECTION INVENTORY already declares pair counts per section,
satisfying C-30. But the pair count line carries only [C-30], not [C-31]. A checker
verifying C-31 compliance for the C-28 section must search the C-28 section body for
[C-31]-tagged pair names rather than reading a single INVENTORY line. Adding [C-31] to
the pair count line makes per-section C-31 compliance directly addressable: `grep [C-31]`
on the INVENTORY locates all sections where per-phase pair structure is declared. V-01
applies this to the 4 pre-existing sections (C-27/C-28/C-29/C-32). The C-33 section
introduced by this variation does not yet have [C-31] self-annotation -- that is the gap
V-05 closes. No inline manifest digest; C-34 absent.

---

You are running `topic-achievements`. Scan all signal artifacts for the topic. Compute
achievement state. Show contributor leaderboard and next recommended action.

**INPUT**: `{{topic}}` (auto-detect from context or TOPICS.md if not provided)

---

### OUTPUT SCHEMAS

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

### OUTPUT TEMPLATE [C-27/C-30/C-31/C-32/C-33]

Fill all `[FIELD]` values. Do not modify pre-printed headers, dividers, barrier lines,
MANIFEST labels, DUAL-LAYER BARRIER blocks, or STRUCTURAL AUDIT GATE section headers.
Barriers marked `[C-26][C-27]` are pre-printed structural elements (model transcribes,
not generates). Each phase boundary carries two independent barrier mechanisms:
instruction-enforced STOP [C-26] and structure-enforced pre-printed divider [C-27]; both
must fail simultaneously for barrier omission [C-29]. Each CLOSURE GATE includes a
forward-binding constraint assertion [C-32] tying Phase N+1 scope to the Phase N
MANIFEST; any scope expansion directly contradicts this claim. The STRUCTURAL AUDIT GATE
uses dedicated named sections tagged [C-30] for each criterion C-27 or later (C-27,
C-28, C-29, C-32, C-33); within each section, checks are expressed as per-phase pairs
tagged [C-31] with Phase 1 and Phase 2 verified independently. The C-30 SECTION
INVENTORY pair count line for each C-27+ section carries [C-31] to make per-section
C-31 compliance string-match verifiable [C-33].

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

STRUCTURAL AUDIT GATE [C-20/C-26/C-27/C-28/C-29/C-30/C-31/C-32/C-33]:
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
  -- C-33 SECTION [C-30] --
  SECTION INVENTORY [C-31] annotations present for targeted sections [C-33/C-31]:
    Phase 1: targeted sections (C-27/C-28/C-29/C-32) have [C-31] on pair count lines in template: [confirmed]
    Phase 2: execution confirms per-phase pair compliance for all 4 targeted sections: [confirmed]
  SECTION INVENTORY [C-31] annotation count matches declared coverage [C-33/C-31]:
    Phase 1: [4] pair count lines carry [C-31] tag in template: [confirmed]
    Phase 2: all [4] annotated sections contain >=2 per-phase pairs confirmed: [confirmed]
  -- C-30 SECTION INVENTORY [C-30] --
  C-27 section header "-- C-27 SECTION [C-30] --" present [C-30]: [confirmed]
  C-27 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30/C-31]: [confirmed]
  C-28 section header "-- C-28 SECTION [C-30] --" present [C-30]: [confirmed]
  C-28 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30/C-31]: [confirmed]
  C-29 section header "-- C-29 SECTION [C-30] --" present [C-30]: [confirmed]
  C-29 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30/C-31]: [confirmed]
  C-32 section header "-- C-32 SECTION [C-30] --" present [C-30]: [confirmed]
  C-32 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30/C-31]: [confirmed]
  C-33 section header "-- C-33 SECTION [C-30] --" present [C-30]: [confirmed]
  C-33 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30]: [confirmed]
  -- Summary --
  Result: [N] gates. [2] STOP barriers (C-26). [2] closure gate confirmations (C-26).
    [2] [C-27]-tagged barriers (C-27). [2] MANIFEST blocks with 2 dimensions each (C-28).
    [2] dual-layer declarations with independence (C-29). [5] dedicated [C-30]-tagged
    sections (C-30). All C-27/C-28/C-29/C-32/C-33 checks as per-phase [C-31] pairs (C-31).
    [2] [C-32]-tagged forward-binding assertions (C-32). [4] INVENTORY pair count lines
    carry [C-31] (C-33 covers C-27/C-28/C-29/C-32; C-33 section entry lacks [C-31]).
    Violations: [n].
  Fail Tier 1: Gate missing criterion ID -> halt.
  Fail Tier 2: [C-30] section header absent for any criterion C-27+ -> finding.
  Fail Tier 2: INVENTORY pair count line missing [C-31] for any targeted section -> finding.
  Fail Tier 3: Any barrier or closure gate permits retroactive Phase N alteration -> halt.
```

**Write artifact**: `simulations/topic/{{topic}}-achievements-{{date}}.md`

---

## V-02 -- Single Axis: C-34 Inline Manifest Digest

**Axis**: C-34 -- embed Phase N MANIFEST dimension values inline in each CLOSURE GATE
forward-binding assertion. Current R11 V-05 format: `Phase 2 inputs constrained to
PHASE 1 MANIFEST [C-32].` V-02 format: `Phase 2 inputs constrained to PHASE 1 MANIFEST:
[K] artifacts, [N] namespaces [C-32/C-34].` Update CLOSURE GATE label to
`[C-26/C-32/C-34]`. Add `-- C-34 SECTION [C-30] --` to STRUCTURAL AUDIT GATE with 2
[C-31] pairs verifying inline digest presence and value per phase. Add C-34 entry to the
INVENTORY with pair count (no [C-33] annotation since C-33 absent). No C-33 changes.

**Hypothesis**: V-05 R11's CLOSURE GATE forward-binding asserts "Phase N+1 inputs
constrained to PHASE N MANIFEST [C-32]" -- naming the manifest as constraint source.
But the assertion is referential: a future run could claim "constrained to MANIFEST"
while producing N+3 artifacts beyond what the MANIFEST records, arguing that the added
artifacts are outside MANIFEST scope. No stated number exists to contradict. Embedding
`[K] artifacts, [N] namespaces` inline converts the constraint from a named reference to
a falsifiable count claim. Any Phase N+1 execution producing a set of size != K
directly contradicts an explicit number in the gate pass. V-02 adds this to both CLOSURE
GATES and adds a C-34 SECTION verifying the inline digest per phase. Risk: the inline
count must be filled from the MANIFEST block; misalignment between MANIFEST count and
inline count creates a new failure mode. This is a feature, not a bug -- it forces the
model to read its own MANIFEST before asserting the count. C-33 is not added.

---

You are running `topic-achievements`. Scan all signal artifacts for the topic. Compute
achievement state. Show contributor leaderboard and next recommended action.

**INPUT**: `{{topic}}` (auto-detect from context or TOPICS.md if not provided)

---

### OUTPUT SCHEMAS

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

### OUTPUT TEMPLATE [C-27/C-30/C-31/C-32/C-34]

Fill all `[FIELD]` values. Do not modify pre-printed headers, dividers, barrier lines,
MANIFEST labels, DUAL-LAYER BARRIER blocks, or STRUCTURAL AUDIT GATE section headers.
Barriers marked `[C-26][C-27]` are pre-printed structural elements (model transcribes,
not generates). Each phase boundary carries two independent barrier mechanisms:
instruction-enforced STOP [C-26] and structure-enforced pre-printed divider [C-27]; both
must fail simultaneously for barrier omission [C-29]. Each CLOSURE GATE includes a
forward-binding constraint assertion [C-32/C-34] that names the Phase N MANIFEST AND
embeds the manifest dimension values inline; any Phase N+1 scope not matching the stated
count directly contradicts the assertion. The STRUCTURAL AUDIT GATE uses dedicated named
sections tagged [C-30] for each criterion C-27 or later (C-27, C-28, C-29, C-32, C-34);
within each section, checks are expressed as per-phase pairs tagged [C-31].

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

PHASE 1 CLOSURE GATE [C-26/C-32/C-34]:
  (1) Verify PHASE 1 MANIFEST [C-28] is recorded above with artifact count and namespace count.
  (2) Phase 2 inputs constrained to PHASE 1 MANIFEST: [K] artifacts, [N] namespaces [C-32/C-34].
      Any Phase 2 artifact scope not matching this count directly contradicts this assertion.
  Pass: "PHASE 1 CLOSURE GATE [C-26]: Manifest verified ([K] artifacts, [N] namespaces).
    Phase 2 inputs constrained to PHASE 1 MANIFEST: [K] artifacts, [N] namespaces [C-32/C-34]."

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

PHASE 2 CLOSURE GATE [C-26/C-32/C-34]:
  (1) Verify PHASE 2 MANIFEST [C-28] is recorded above with row count and EARNED count.
  (2) Phase 3 inputs constrained to PHASE 2 MANIFEST: 7 rows, [N] EARNED [C-32/C-34].
      Any Phase 3 scope not matching this count directly contradicts this assertion.
  Pass: "PHASE 2 CLOSURE GATE [C-26]: Manifest verified (7 rows, [N] EARNED).
    Phase 3 inputs constrained to PHASE 2 MANIFEST: 7 rows, [N] EARNED [C-32/C-34]."

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

STRUCTURAL AUDIT GATE [C-20/C-26/C-27/C-28/C-29/C-30/C-31/C-32/C-34]:
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
  -- C-34 SECTION [C-30] --
  CLOSURE GATE forward-binding includes inline dimension values [C-34/C-31]:
    Phase 1: PHASE 1 CLOSURE GATE pass includes "[K] artifacts, [N] namespaces" inline: [confirmed]
    Phase 2: PHASE 2 CLOSURE GATE pass includes "7 rows, [N] EARNED" inline: [confirmed]
  Inline values match PHASE N MANIFEST declared fields [C-34/C-31]:
    Phase 1: inline artifact count equals PHASE 1 MANIFEST artifact count: [confirmed]
    Phase 2: inline row count equals PHASE 2 MANIFEST achievement row count (7): [confirmed]
  -- C-30 SECTION INVENTORY [C-30] --
  C-27 section header "-- C-27 SECTION [C-30] --" present [C-30]: [confirmed]
  C-27 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30]: [confirmed]
  C-28 section header "-- C-28 SECTION [C-30] --" present [C-30]: [confirmed]
  C-28 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30]: [confirmed]
  C-29 section header "-- C-29 SECTION [C-30] --" present [C-30]: [confirmed]
  C-29 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30]: [confirmed]
  C-32 section header "-- C-32 SECTION [C-30] --" present [C-30]: [confirmed]
  C-32 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30]: [confirmed]
  C-34 section header "-- C-34 SECTION [C-30] --" present [C-30]: [confirmed]
  C-34 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30]: [confirmed]
  -- Summary --
  Result: [N] gates. [2] STOP barriers (C-26). [2] closure gate confirmations (C-26).
    [2] [C-27]-tagged barriers (C-27). [2] MANIFEST blocks with 2 dimensions each (C-28).
    [2] dual-layer declarations with independence (C-29). [5] dedicated [C-30]-tagged
    sections (C-30). All C-27/C-28/C-29/C-32/C-34 checks as per-phase [C-31] pairs (C-31).
    [2] [C-32]-tagged forward-binding assertions (C-32). [2] [C-34]-tagged inline digests
    in closure gates (C-34). INVENTORY pair count lines carry [C-30] only (C-33 absent).
    Violations: [n].
  Fail Tier 1: Gate missing criterion ID -> halt.
  Fail Tier 2: [C-30] section header absent for any criterion C-27+ -> finding.
  Fail Tier 2: CLOSURE GATE forward-binding assertion lacks inline dimension values -> finding.
  Fail Tier 3: Any barrier or closure gate permits retroactive Phase N alteration -> halt.
```

**Write artifact**: `simulations/topic/{{topic}}-achievements-{{date}}.md`

---

## V-03 -- Combined: C-33 + C-34, No Self-Application

**Axes**: C-33 (V-01) + C-34 (V-02). Both new mechanisms applied. C-33 covers the 4
pre-existing C-27+ sections (C-27/C-28/C-29/C-32). C-34 inline digest in both CLOSURE
GATES. New C-33 SECTION [C-30] and C-34 SECTION [C-30] added to STRUCTURAL AUDIT GATE.
The C-33 and C-34 SECTION INVENTORY entries declare pair counts [C-30] but do NOT carry
[C-31] on their pair count lines (no self-application -- V-03 gap).

**Hypothesis**: V-01 isolates C-33 auditability ([C-31] on INVENTORY pair count lines
for pre-existing sections). V-02 isolates C-34 auditability (inline digest in CLOSURE
GATE). Combining them adds both mechanisms. However, C-33 and C-34 introduce new C-27+
sections that themselves require [C-30] section entries. Those new section entries carry
pair counts per C-30 but without [C-31] annotation -- a verifier checking C-33 compliance
for the C-33 or C-34 sections must read section bodies rather than the INVENTORY. This
is the same structural gap V-01 leaves for the C-33 section: the mechanism is applied to
pre-existing sections but not yet to the sections it introduces. V-05 closes this by
self-applying [C-31] to the C-33 and C-34 INVENTORY entries.

---

You are running `topic-achievements`. Scan all signal artifacts for the topic. Compute
achievement state. Show contributor leaderboard and next recommended action.

**INPUT**: `{{topic}}` (auto-detect from context or TOPICS.md if not provided)

---

### OUTPUT SCHEMAS

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

### OUTPUT TEMPLATE [C-27/C-30/C-31/C-32/C-33/C-34]

Fill all `[FIELD]` values. Do not modify pre-printed headers, dividers, barrier lines,
MANIFEST labels, DUAL-LAYER BARRIER blocks, or STRUCTURAL AUDIT GATE section headers.
Barriers marked `[C-26][C-27]` are pre-printed structural elements (model transcribes,
not generates). Each phase boundary carries two independent barrier mechanisms:
instruction-enforced STOP [C-26] and structure-enforced pre-printed divider [C-27]; both
must fail simultaneously for barrier omission [C-29]. Each CLOSURE GATE includes a
forward-binding constraint assertion [C-32/C-34] naming the Phase N MANIFEST with inline
dimension values; any Phase N+1 scope not matching the stated count directly contradicts
the assertion. The STRUCTURAL AUDIT GATE uses dedicated named sections tagged [C-30] for
each criterion C-27 or later; within each section, checks are expressed as per-phase
pairs tagged [C-31]. The C-30 SECTION INVENTORY pair count line for each pre-existing
C-27+ section (C-27/C-28/C-29/C-32) carries [C-31] for string-match-verifiable C-33
compliance [C-33].

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

PHASE 1 CLOSURE GATE [C-26/C-32/C-34]:
  (1) Verify PHASE 1 MANIFEST [C-28] is recorded above with artifact count and namespace count.
  (2) Phase 2 inputs constrained to PHASE 1 MANIFEST: [K] artifacts, [N] namespaces [C-32/C-34].
      Any Phase 2 artifact scope not matching this count directly contradicts this assertion.
  Pass: "PHASE 1 CLOSURE GATE [C-26]: Manifest verified ([K] artifacts, [N] namespaces).
    Phase 2 inputs constrained to PHASE 1 MANIFEST: [K] artifacts, [N] namespaces [C-32/C-34]."

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

PHASE 2 CLOSURE GATE [C-26/C-32/C-34]:
  (1) Verify PHASE 2 MANIFEST [C-28] is recorded above with row count and EARNED count.
  (2) Phase 3 inputs constrained to PHASE 2 MANIFEST: 7 rows, [N] EARNED [C-32/C-34].
      Any Phase 3 scope not matching this count directly contradicts this assertion.
  Pass: "PHASE 2 CLOSURE GATE [C-26]: Manifest verified (7 rows, [N] EARNED).
    Phase 3 inputs constrained to PHASE 2 MANIFEST: 7 rows, [N] EARNED [C-32/C-34]."

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

STRUCTURAL AUDIT GATE [C-20/C-26/C-27/C-28/C-29/C-30/C-31/C-32/C-33/C-34]:
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
  -- C-33 SECTION [C-30] --
  SECTION INVENTORY [C-31] annotations present for targeted sections [C-33/C-31]:
    Phase 1: targeted sections (C-27/C-28/C-29/C-32) have [C-31] on pair count lines in template: [confirmed]
    Phase 2: execution confirms per-phase pair compliance for all 4 targeted sections: [confirmed]
  SECTION INVENTORY [C-31] annotation count matches declared coverage [C-33/C-31]:
    Phase 1: [4] pair count lines carry [C-31] tag in template: [confirmed]
    Phase 2: all [4] annotated sections contain >=2 per-phase pairs confirmed: [confirmed]
  -- C-34 SECTION [C-30] --
  CLOSURE GATE forward-binding includes inline dimension values [C-34/C-31]:
    Phase 1: PHASE 1 CLOSURE GATE pass includes "[K] artifacts, [N] namespaces" inline: [confirmed]
    Phase 2: PHASE 2 CLOSURE GATE pass includes "7 rows, [N] EARNED" inline: [confirmed]
  Inline values match PHASE N MANIFEST declared fields [C-34/C-31]:
    Phase 1: inline artifact count equals PHASE 1 MANIFEST artifact count: [confirmed]
    Phase 2: inline row count equals PHASE 2 MANIFEST achievement row count (7): [confirmed]
  -- C-30 SECTION INVENTORY [C-30] --
  C-27 section header "-- C-27 SECTION [C-30] --" present [C-30]: [confirmed]
  C-27 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30/C-31]: [confirmed]
  C-28 section header "-- C-28 SECTION [C-30] --" present [C-30]: [confirmed]
  C-28 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30/C-31]: [confirmed]
  C-29 section header "-- C-29 SECTION [C-30] --" present [C-30]: [confirmed]
  C-29 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30/C-31]: [confirmed]
  C-32 section header "-- C-32 SECTION [C-30] --" present [C-30]: [confirmed]
  C-32 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30/C-31]: [confirmed]
  C-33 section header "-- C-33 SECTION [C-30] --" present [C-30]: [confirmed]
  C-33 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30]: [confirmed]
  C-34 section header "-- C-34 SECTION [C-30] --" present [C-30]: [confirmed]
  C-34 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30]: [confirmed]
  -- Summary --
  Result: [N] gates. [2] STOP barriers (C-26). [2] closure gate confirmations (C-26).
    [2] [C-27]-tagged barriers (C-27). [2] MANIFEST blocks with 2 dimensions each (C-28).
    [2] dual-layer declarations with independence (C-29). [6] dedicated [C-30]-tagged
    sections (C-30). All C-27/C-28/C-29/C-32/C-33/C-34 checks as per-phase [C-31] pairs
    (C-31). [2] [C-32]-tagged forward-binding assertions (C-32). [4] INVENTORY pair count
    lines carry [C-31] for C-27/C-28/C-29/C-32; C-33/C-34 entries carry [C-30] only
    (C-33 gap: new sections not self-annotated). [2] inline digests in closure gates (C-34).
    Violations: [n].
  Fail Tier 1: Gate missing criterion ID -> halt.
  Fail Tier 2: [C-30] section header absent for any criterion C-27+ -> finding.
  Fail Tier 2: INVENTORY pair count line missing [C-31] for targeted section -> finding.
  Fail Tier 2: CLOSURE GATE forward-binding assertion lacks inline dimension values -> finding.
  Fail Tier 3: Any barrier or closure gate permits retroactive Phase N alteration -> halt.
```

**Write artifact**: `simulations/topic/{{topic}}-achievements-{{date}}.md`

---

## V-04 -- Combined: C-33 + C-34, C-34 Section Receives [C-31] Self-Annotation

**Axes**: C-33 + C-34 from V-03, extended: the C-34 SECTION INVENTORY entry now carries
[C-31] on its pair count line (partial self-application). C-33 SECTION extended to cover
C-34 section compliance (5 [C-31] pairs: C-27/C-28/C-29/C-32/C-34). C-33 SECTION
INVENTORY entry still lacks [C-31] self-annotation -- the one remaining V-04 gap.

**Hypothesis**: V-03 introduces both C-33 and C-34 sections but neither receives [C-31]
on its INVENTORY pair count line. A checker verifying C-33 compliance for C-33 or C-34
sections must traverse those section bodies. V-04 applies [C-31] to C-34's INVENTORY
entry first: C-34 is the simpler case (2 [C-31] pairs, straightforward inline digest
checks). The C-33 SECTION is extended to also verify C-34's INVENTORY annotation,
bringing C-34 fully under C-33's coverage. The remaining gap: C-33 section's own
INVENTORY entry still carries only [C-30] (no [C-31]). This makes C-33 incomplete for
exactly one section -- its own. V-05 closes this by self-applying [C-31] to the C-33
INVENTORY entry and extending the C-33 SECTION to 6 [C-31] pairs.

---

You are running `topic-achievements`. Scan all signal artifacts for the topic. Compute
achievement state. Show contributor leaderboard and next recommended action.

**INPUT**: `{{topic}}` (auto-detect from context or TOPICS.md if not provided)

---

### OUTPUT SCHEMAS

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

### OUTPUT TEMPLATE [C-27/C-30/C-31/C-32/C-33/C-34]

Fill all `[FIELD]` values. Do not modify pre-printed headers, dividers, barrier lines,
MANIFEST labels, DUAL-LAYER BARRIER blocks, or STRUCTURAL AUDIT GATE section headers.
Barriers marked `[C-26][C-27]` are pre-printed structural elements (model transcribes,
not generates). Each phase boundary carries two independent barrier mechanisms:
instruction-enforced STOP [C-26] and structure-enforced pre-printed divider [C-27]; both
must fail simultaneously for barrier omission [C-29]. Each CLOSURE GATE includes a
forward-binding constraint assertion [C-32/C-34] naming the Phase N MANIFEST with inline
dimension values; any Phase N+1 scope not matching the stated count directly contradicts
the assertion. The STRUCTURAL AUDIT GATE uses dedicated named sections tagged [C-30] for
each criterion C-27 or later; within each section, checks are expressed as per-phase
pairs tagged [C-31]. The C-30 SECTION INVENTORY pair count line for C-27/C-28/C-29/C-32
and C-34 sections carries [C-31] [C-33]; the C-33 section entry carries [C-30] only
(addressed in V-05).

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

PHASE 1 CLOSURE GATE [C-26/C-32/C-34]:
  (1) Verify PHASE 1 MANIFEST [C-28] is recorded above with artifact count and namespace count.
  (2) Phase 2 inputs constrained to PHASE 1 MANIFEST: [K] artifacts, [N] namespaces [C-32/C-34].
      Any Phase 2 artifact scope not matching this count directly contradicts this assertion.
  Pass: "PHASE 1 CLOSURE GATE [C-26]: Manifest verified ([K] artifacts, [N] namespaces).
    Phase 2 inputs constrained to PHASE 1 MANIFEST: [K] artifacts, [N] namespaces [C-32/C-34]."

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

PHASE 2 CLOSURE GATE [C-26/C-32/C-34]:
  (1) Verify PHASE 2 MANIFEST [C-28] is recorded above with row count and EARNED count.
  (2) Phase 3 inputs constrained to PHASE 2 MANIFEST: 7 rows, [N] EARNED [C-32/C-34].
      Any Phase 3 scope not matching this count directly contradicts this assertion.
  Pass: "PHASE 2 CLOSURE GATE [C-26]: Manifest verified (7 rows, [N] EARNED).
    Phase 3 inputs constrained to PHASE 2 MANIFEST: 7 rows, [N] EARNED [C-32/C-34]."

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

STRUCTURAL AUDIT GATE [C-20/C-26/C-27/C-28/C-29/C-30/C-31/C-32/C-33/C-34]:
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
  -- C-33 SECTION [C-30] --
  SECTION INVENTORY [C-31] annotations present for targeted sections [C-33/C-31]:
    Phase 1: targeted sections (C-27/C-28/C-29/C-32/C-34) have [C-31] on pair count lines: [confirmed]
    Phase 2: execution confirms per-phase pair compliance for all 5 targeted sections: [confirmed]
  SECTION INVENTORY [C-31] annotation count matches declared coverage [C-33/C-31]:
    Phase 1: [5] pair count lines carry [C-31] tag in template: [confirmed]
    Phase 2: all [5] annotated sections contain >=2 per-phase pairs confirmed: [confirmed]
  -- C-34 SECTION [C-30] --
  CLOSURE GATE forward-binding includes inline dimension values [C-34/C-31]:
    Phase 1: PHASE 1 CLOSURE GATE pass includes "[K] artifacts, [N] namespaces" inline: [confirmed]
    Phase 2: PHASE 2 CLOSURE GATE pass includes "7 rows, [N] EARNED" inline: [confirmed]
  Inline values match PHASE N MANIFEST declared fields [C-34/C-31]:
    Phase 1: inline artifact count equals PHASE 1 MANIFEST artifact count: [confirmed]
    Phase 2: inline row count equals PHASE 2 MANIFEST achievement row count (7): [confirmed]
  -- C-30 SECTION INVENTORY [C-30] --
  C-27 section header "-- C-27 SECTION [C-30] --" present [C-30]: [confirmed]
  C-27 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30/C-31]: [confirmed]
  C-28 section header "-- C-28 SECTION [C-30] --" present [C-30]: [confirmed]
  C-28 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30/C-31]: [confirmed]
  C-29 section header "-- C-29 SECTION [C-30] --" present [C-30]: [confirmed]
  C-29 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30/C-31]: [confirmed]
  C-32 section header "-- C-32 SECTION [C-30] --" present [C-30]: [confirmed]
  C-32 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30/C-31]: [confirmed]
  C-33 section header "-- C-33 SECTION [C-30] --" present [C-30]: [confirmed]
  C-33 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30]: [confirmed]
  C-34 section header "-- C-34 SECTION [C-30] --" present [C-30]: [confirmed]
  C-34 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30/C-31]: [confirmed]
  -- Summary --
  Result: [N] gates. [2] STOP barriers (C-26). [2] closure gate confirmations (C-26).
    [2] [C-27]-tagged barriers (C-27). [2] MANIFEST blocks with 2 dimensions each (C-28).
    [2] dual-layer declarations with independence (C-29). [6] dedicated [C-30]-tagged
    sections (C-30). All C-27/C-28/C-29/C-32/C-33/C-34 checks as per-phase [C-31] pairs
    (C-31). [2] [C-32]-tagged forward-binding assertions (C-32). [5] INVENTORY pair count
    lines carry [C-31] for C-27/C-28/C-29/C-32/C-34; C-33 entry carries [C-30] only
    (C-33 incomplete: C-33 section self-annotation absent). [2] inline digests in closure
    gates (C-34). Violations: [n].
  Fail Tier 1: Gate missing criterion ID -> halt.
  Fail Tier 2: [C-30] section header absent for any criterion C-27+ -> finding.
  Fail Tier 2: INVENTORY pair count line missing [C-31] for targeted section -> finding.
  Fail Tier 2: CLOSURE GATE forward-binding assertion lacks inline dimension values -> finding.
  Fail Tier 3: Any barrier or closure gate permits retroactive Phase N alteration -> halt.
```

**Write artifact**: `simulations/topic/{{topic}}-achievements-{{date}}.md`

---

## V-05 -- Full Integration: C-33 + C-34 + Complete Self-Application

**Axes**: All R12 mechanisms combined with full self-application.
- V-01 axis: [C-31] on SECTION INVENTORY pair count lines for C-27/C-28/C-29/C-32
- V-02 axis: [C-34] inline manifest digest in CLOSURE GATES
- Self-application: C-33 and C-34 SECTION INVENTORY entries also carry [C-31] on their
  pair count lines; C-33 SECTION extended to 6 [C-31] pairs (covers all C-27+ sections
  including C-33 and C-34 themselves)

**Hypothesis**: V-04 annotates 5/6 C-27+ sections (C-27/C-28/C-29/C-32/C-34) with
[C-31] in the INVENTORY. The sole missing annotation is C-33's own entry -- the criterion
that governs [C-31] INVENTORY annotations cannot self-annotate at the V-04 stage because
V-04's C-33 SECTION only checks 5 sections (not itself). V-05 closes this: the C-33
SECTION is extended to also verify itself (6th [C-31] pair), and the C-33 INVENTORY
entry gets [C-31] on its pair count line. The result: a checker verifying C-33 for ALL
C-27+ sections (C-27 through C-34) can use only the SECTION INVENTORY, string-matching
[C-31] on the pair count line of each entry, without traversing any section body. All 6
C-27+ sections are uniformly structured: [C-30]-tagged header, [C-31]-tagged pair count,
[C-33]-annotated for per-phase pair compliance. C-34 adds inline falsifiability to all
CLOSURE GATE forward-binding assertions.

---

You are running `topic-achievements`. Scan all signal artifacts for the topic. Compute
achievement state. Show contributor leaderboard and next recommended action.

**INPUT**: `{{topic}}` (auto-detect from context or TOPICS.md if not provided)

---

### OUTPUT SCHEMAS

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

### OUTPUT TEMPLATE [C-27/C-30/C-31/C-32/C-33/C-34]

Fill all `[FIELD]` values. Do not modify pre-printed headers, dividers, barrier lines,
MANIFEST labels, DUAL-LAYER BARRIER blocks, or STRUCTURAL AUDIT GATE section headers.
Barriers marked `[C-26][C-27]` are pre-printed structural elements (model transcribes,
not generates). Each phase boundary carries two independent barrier mechanisms:
instruction-enforced STOP [C-26] and structure-enforced pre-printed divider [C-27]; both
must fail simultaneously for barrier omission [C-29]. Each CLOSURE GATE includes a
forward-binding constraint assertion [C-32/C-34] naming the Phase N MANIFEST with inline
dimension values; any Phase N+1 scope not matching the stated count directly contradicts
the assertion. The STRUCTURAL AUDIT GATE uses dedicated named sections tagged [C-30] for
each criterion C-27 or later (C-27, C-28, C-29, C-32, C-33, C-34); within each section,
checks are expressed as per-phase pairs tagged [C-31] with Phase 1 and Phase 2 verified
independently. The C-30 SECTION INVENTORY pair count line for ALL C-27+ sections carries
[C-31] to make per-section C-31 compliance string-match verifiable [C-33], including
for the C-33 and C-34 sections themselves (complete self-application).

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

PHASE 1 CLOSURE GATE [C-26/C-32/C-34]:
  (1) Verify PHASE 1 MANIFEST [C-28] is recorded above with artifact count and namespace count.
  (2) Phase 2 inputs constrained to PHASE 1 MANIFEST: [K] artifacts, [N] namespaces [C-32/C-34].
      Any Phase 2 artifact scope not matching this count directly contradicts this assertion.
  Pass: "PHASE 1 CLOSURE GATE [C-26]: Manifest verified ([K] artifacts, [N] namespaces).
    Phase 2 inputs constrained to PHASE 1 MANIFEST: [K] artifacts, [N] namespaces [C-32/C-34]."

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

PHASE 2 CLOSURE GATE [C-26/C-32/C-34]:
  (1) Verify PHASE 2 MANIFEST [C-28] is recorded above with row count and EARNED count.
  (2) Phase 3 inputs constrained to PHASE 2 MANIFEST: 7 rows, [N] EARNED [C-32/C-34].
      Any Phase 3 scope not matching this count directly contradicts this assertion.
  Pass: "PHASE 2 CLOSURE GATE [C-26]: Manifest verified (7 rows, [N] EARNED).
    Phase 3 inputs constrained to PHASE 2 MANIFEST: 7 rows, [N] EARNED [C-32/C-34]."

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

STRUCTURAL AUDIT GATE [C-20/C-26/C-27/C-28/C-29/C-30/C-31/C-32/C-33/C-34]:
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
  -- C-33 SECTION [C-30] --
  SECTION INVENTORY [C-31] annotations present for all C-27+ sections [C-33/C-31]:
    Phase 1: all 6 sections (C-27/C-28/C-29/C-32/C-33/C-34) have [C-31] on pair count lines: [confirmed]
    Phase 2: execution confirms per-phase pair compliance for all 6 sections: [confirmed]
  SECTION INVENTORY [C-31] annotation count matches required coverage [C-33/C-31]:
    Phase 1: [6] pair count lines carry [C-31] tag in template (all C-27+ sections): [confirmed]
    Phase 2: all [6] annotated sections contain >=2 per-phase pairs confirmed: [confirmed]
  -- C-34 SECTION [C-30] --
  CLOSURE GATE forward-binding includes inline dimension values [C-34/C-31]:
    Phase 1: PHASE 1 CLOSURE GATE pass includes "[K] artifacts, [N] namespaces" inline: [confirmed]
    Phase 2: PHASE 2 CLOSURE GATE pass includes "7 rows, [N] EARNED" inline: [confirmed]
  Inline values match PHASE N MANIFEST declared fields [C-34/C-31]:
    Phase 1: inline artifact count equals PHASE 1 MANIFEST artifact count: [confirmed]
    Phase 2: inline row count equals PHASE 2 MANIFEST achievement row count (7): [confirmed]
  -- C-30 SECTION INVENTORY [C-30] --
  C-27 section header "-- C-27 SECTION [C-30] --" present [C-30]: [confirmed]
  C-27 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30/C-31]: [confirmed]
  C-28 section header "-- C-28 SECTION [C-30] --" present [C-30]: [confirmed]
  C-28 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30/C-31]: [confirmed]
  C-29 section header "-- C-29 SECTION [C-30] --" present [C-30]: [confirmed]
  C-29 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30/C-31]: [confirmed]
  C-32 section header "-- C-32 SECTION [C-30] --" present [C-30]: [confirmed]
  C-32 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30/C-31]: [confirmed]
  C-33 section header "-- C-33 SECTION [C-30] --" present [C-30]: [confirmed]
  C-33 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30/C-31]: [confirmed]
  C-34 section header "-- C-34 SECTION [C-30] --" present [C-30]: [confirmed]
  C-34 section pair count: [2] pairs x 2 phases = [4] individual checks (required: >=2) [C-30/C-31]: [confirmed]
  -- Summary --
  Result: [N] gates. [2] STOP barriers (C-26). [2] closure gate confirmations (C-26).
    [2] [C-27]-tagged barriers (C-27). [2] MANIFEST blocks with 2 dimensions each (C-28).
    [2] dual-layer declarations with independence (C-29). [6] dedicated [C-30]-tagged
    sections (C-30). All C-27/C-28/C-29/C-32/C-33/C-34 checks as per-phase [C-31] pairs
    (C-31). [2] [C-32]-tagged forward-binding assertions (C-32). All [6] C-27+ SECTION
    INVENTORY pair count lines carry [C-31] -- complete [C-33] coverage including C-33
    and C-34 self-application. [2] inline digests in closure gates (C-34). Violations: [n].
  Fail Tier 1: Gate missing criterion ID -> halt.
  Fail Tier 2: [C-30] section header absent for any criterion C-27+ -> finding.
  Fail Tier 2: INVENTORY pair count line missing [C-31] for any C-27+ section -> finding.
  Fail Tier 2: CLOSURE GATE forward-binding assertion lacks inline dimension values -> finding.
  Fail Tier 3: Any barrier or closure gate permits retroactive Phase N alteration -> halt.
```

**Write artifact**: `simulations/topic/{{topic}}-achievements-{{date}}.md`

---

## Variation Summary

| Feature | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| [C-31] on C-27/C-28/C-29/C-32 INVENTORY pair count lines [C-33] | YES | -- | YES | YES | YES |
| [C-31] on C-34 INVENTORY pair count line [C-33] | -- | -- | -- | YES | YES |
| [C-31] on C-33 INVENTORY pair count line (self-application) [C-33] | -- | -- | -- | -- | YES |
| C-33 SECTION [C-30] added | YES | -- | YES | YES | YES |
| C-33 SECTION covers C-27/C-28/C-29/C-32 (4 pairs) | YES | -- | YES | -- | -- |
| C-33 SECTION covers C-27..C-32/C-34 (5 pairs) | -- | -- | -- | YES | -- |
| C-33 SECTION covers all 6 C-27+ sections (6 pairs) | -- | -- | -- | -- | YES |
| Inline manifest digest in CLOSURE GATES [C-34] | -- | YES | YES | YES | YES |
| C-34 SECTION [C-30] added | -- | YES | YES | YES | YES |
| New mechanism count | 1 | 1 | 2 | 2+ | 3 |

## C-33/C-34 Failure Mode Coverage

| Failure Mode | V-01 | V-02 | V-03 | V-04 | V-05 |
|--------------|------|------|------|------|------|
| C-33: INVENTORY entry lacks [C-31] for a pre-existing section | DETECTED | -- | DETECTED | DETECTED | DETECTED |
| C-33: C-33/C-34 sections lack [C-31] self-annotation in INVENTORY | Undetected | -- | Undetected | C-34 detected, C-33 undetected | DETECTED |
| C-34: forward-binding assertion lacks inline count | Undetected | DETECTED | DETECTED | DETECTED | DETECTED |
| C-34: inline count mismatches MANIFEST value | Undetected | DETECTED (match check) | DETECTED | DETECTED | DETECTED |
| Retroactive scope expansion by count | Implicitly blocked (C-32) | EXPLICITLY BLOCKED (count claim) | EXPLICITLY BLOCKED | EXPLICITLY BLOCKED | EXPLICITLY BLOCKED |

## Predicted Scoring (rubric v12)

Scoring formula: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/26 * 10)`.
Per aspirational criterion: 10/26 = 0.385 pts.

**V-01**: C-09--C-32 PASS (full baseline 24/24). C-33: FAIL. C-33 covers 4/5 indexed
sections (C-27/C-28/C-29/C-32); C-33 section INVENTORY entry lacks [C-31]. A scorer
checking C-33 compliance for the C-33 section must traverse the section body, not the
INVENTORY. C-34: FAIL. No inline digest.
Aspirational: 24/26. Score: 60 + 30 + (24/26 * 10) = 60 + 30 + 9.23 = **99.23**

**V-02**: C-09--C-32 PASS. C-33: FAIL. No [C-31] on any INVENTORY pair count lines.
C-34: PASS. Inline digest present and match-verifiable in both CLOSURE GATES; dedicated
C-34 SECTION with 2 [C-31] pairs confirms per phase.
Aspirational: 25/26. Score: 60 + 30 + (25/26 * 10) = 60 + 30 + 9.62 = **99.62**

**V-03**: C-09--C-32 PASS. C-33: FAIL. [C-31] present for C-27/C-28/C-29/C-32 (4/6
indexed sections); C-33 and C-34 INVENTORY entries lack [C-31]. A scorer verifying C-33
for C-33/C-34 sections must read section bodies. C-34: PASS.
Aspirational: 25/26. Score: **99.62**

**V-04**: C-09--C-32 PASS. C-33: FAIL. [C-31] present for C-27/C-28/C-29/C-32/C-34
(5/6 indexed sections); C-33 INVENTORY entry still lacks [C-31] (one section
unverifiable from INVENTORY alone). C-34: PASS.
Aspirational: 25/26. Score: **99.62**

**V-05**: C-09--C-32 PASS. C-33: PASS. All 6 C-27+ sections (C-27 through C-34) have
[C-31] on their INVENTORY pair count lines. A scorer can verify C-33 compliance for any
section by string-matching [C-31] in the INVENTORY without section body traversal.
C-33 SECTION covers all 6 sections (6 [C-31] pairs) including itself (self-application).
C-34: PASS.
Aspirational: 26/26. Score: 60 + 30 + (26/26 * 10) = **100**

| Variation | C-33 | C-34 | Asp | Score | Rank |
|-----------|------|------|-----|-------|------|
| V-05 | PASS | PASS | 26/26 | **100** | 1 |
| V-02 | FAIL | PASS | 25/26 | **99.62** | 2 (tie) |
| V-03 | FAIL | PASS | 25/26 | **99.62** | 2 (tie) |
| V-04 | FAIL | PASS | 25/26 | **99.62** | 2 (tie) |
| V-01 | FAIL | FAIL | 24/26 | **99.23** | 5 |

V-02/V-03/V-04 tie at 99.62 with different C-33 failure modes: V-02 has no [C-31]
annotations at all; V-03 annotates 4/6 sections; V-04 annotates 5/6 sections (C-33
self-annotation is the sole gap). V-01 is the only variation below 99.6 because it
introduces C-33 machinery without C-34, scoring two criteria FAIL.

---

## Open Excellence Signals for C-35+

**E-01 -- INVENTORY as complete single-point audit record**
V-05's SECTION INVENTORY is the first version where a scorer can verify C-33 compliance
for every C-27+ section by reading only the INVENTORY -- no section body traversal.
This extends the INVENTORY from a C-30 record (sections exist, pair counts declared)
to a C-31 record (per-phase pair structure declared per section). A potential C-35
criterion: the SECTION INVENTORY also declares the inline digest presence for C-34
compliance per section -- "C-34 inline digest embedded [C-34]: [confirmed]" on any
section that contains a CLOSURE GATE (i.e., closure-owning phases). Converts C-34 from
a per-gate check into a per-section declaration accessible from the INVENTORY.

**E-02 -- Inline count as cross-reference integrity check**
V-05's C-34 SECTION verifies that the inline count matches the MANIFEST declared value
(pair 2: "Inline values match PHASE N MANIFEST declared fields"). This match check is
currently inside the C-34 SECTION body -- a scorer must read the section to verify the
match was confirmed. A potential C-35 criterion: the match confirmation result ("inline
[K] = MANIFEST [K]: confirmed") is promoted to the SECTION INVENTORY as a per-section
declaration, making the cross-reference integrity check accessible from the single-point
INVENTORY record without section traversal.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Complete SECTION INVENTORY self-application: all 6 C-27+ sections (C-27 through C-34 including C-33 and C-34 themselves) have [C-31] on their INVENTORY pair count lines, enabling single-point C-33 audit without any section body traversal", "C-34 inline count as falsifiability anchor: embedding manifest dimension values in the forward-binding assertion converts the constraint from referential (names MANIFEST) to numerically falsifiable (states MANIFEST size), and the C-34 SECTION match check verifies the inline value equals the MANIFEST field -- two independent checks per phase"]}
```
