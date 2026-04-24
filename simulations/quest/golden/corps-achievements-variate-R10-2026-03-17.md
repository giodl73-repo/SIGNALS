---
skill: quest-variate
skill_target: corps-achievements
round: 10
date: 2026-03-17
rubric_version: 10
basis: V-05 R9 scored 100 on rubric v9 (C-01--C-26, 18/18 aspirational). V-05 R9 also
       implicitly satisfies C-27/C-28/C-29 (unscored because criteria did not exist yet):
       pre-printed `--- PHASE N SEALED [C-26] ---` satisfies C-27; closure gate sub-steps
       enumerate counts before the seal, satisfying C-28; STOP + pre-printed = two
       independent layers, satisfying C-29. R10 formalizes these implicit satisfactions
       into explicitly labeled, individually auditable mechanisms. N_aspirational = 21.
       Scoring formula updated: aspirational_pass / 21 * 10 (was /18).
---

# Variate R10 -- corps-achievements (2026-03-17)

5 complete prompt body variations for the `corps-achievements` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

Rubric v10 adds three new aspirational criteria beyond the v9 baseline:

- **C-27 (new)**: Structural barrier omission resistance -- phase barrier markers are
  embedded as pre-printed elements in the output template. Omission requires the model
  to actively skip a pre-printed element rather than simply fail to follow an
  instruction. Structurally independent of C-26: a prompt could carry pre-printed
  dividers without STOP instructions (valid). C-27 does not prevent retroactive
  reframing via reinterpretation (only omission is blocked).

- **C-28 (new)**: Phase N output-set manifest declared before closure seal -- at each
  phase boundary, the prompt requires the model to enumerate and record specific output
  counts before writing the closure seal. Manifest must include at minimum: artifact
  count PLUS at least one additional dimension (contributor count, namespace count, or
  equivalent). A closure gate that writes the seal without first recording counts fails
  C-28. Structurally independent of C-26 and C-27; addresses retroactive scope expansion
  via reinterpretation (not omission). C-26 + C-28 together: barrier seals scope AND
  a manifest records what scope was at sealing.

- **C-29 (new)**: Dual-layer barrier redundancy -- each phase boundary carries two
  distinct, independently-implemented barrier mechanisms. **C-29 requires C-26 and C-27
  as preconditions.** Both must fail simultaneously for barrier omission. Limitation
  vs C-28: dual-layer redundancy eliminates omission risk but does not add output-set
  enumeration; retroactive reframing via reinterpretation remains possible unless C-28
  is also satisfied.

All variations carry the full v9 baseline: essential C-01--C-05, recommended C-06--C-08,
aspirational C-09--C-26. Scoring formula: `(essential_pass/5 * 60) + (recommended_pass/3
* 30) + (aspirational_pass/21 * 10)`.

---

## Variation Axes Selected

| Axis | Hypothesis | Used In |
|------|------------|---------|
| C-27: explicit [C-27] tag on pre-printed barriers | Adding [C-27] to the pre-printed barrier line and to the structural audit gate check closes any ambiguity about C-27 compliance; the audit gate can cite the specific tag rather than inferring structural compliance from the format alone | V-01, V-04, V-05 |
| C-28: standalone MANIFEST block before seal | A named `PHASE N MANIFEST [C-28]:` block structurally separate from the closure gate sub-steps makes C-28 unambiguous; the manifest appears as a distinct artifact on the page, not buried in numbered sub-step prose | V-02, V-04, V-05 |
| C-29: explicit DUAL-LAYER BARRIER declaration | An explicit `DUAL-LAYER BARRIER [C-26/C-27][C-29]:` block at each boundary that names both layers and their independence converts implicit structural redundancy into a named, auditable architectural property | V-03, V-05 |

---

## V-01 -- Single Axis: C-27 Explicit Tagging

**Axis**: C-27 -- add explicit `[C-27]` tag to the pre-printed barrier lines in the
output template (`--- PHASE N SEALED [C-26][C-27] ---`), declare the barriers as
pre-printed elements in the template preamble, and add a C-27-specific verification
step to the STRUCTURAL AUDIT GATE.

**Hypothesis**: R9 V-05's pre-printed `--- PHASE N SEALED [C-26] ---` satisfies C-27
structurally but does not label itself as the C-27 mechanism. A scorer evaluating C-27
must infer structural pre-printing from the template format. Adding `[C-27]` to the
barrier line makes the criterion reference explicit on the face of the artifact: the
audit gate can check for `[C-27]` presence by name, not by template-format inference.
This is the same strategy that V-01 R8 used to make C-15 auditable after it was present
but unlabeled. Risk: the [C-27] tag is still a pre-printed element -- the model
transcribes it, not generates it -- but the audit step is now a string match rather
than a structural interpretation.

---

You are running `corps-achievements`. Scan all signal artifacts for the topic. Compute
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

### OUTPUT TEMPLATE [C-27]

Fill all `[FIELD]` values. The pre-printed headers, dividers, and barrier lines define
the output structure. Do not modify them. Barriers marked `[C-26][C-27]` are pre-printed
structural elements -- the model transcribes them verbatim, not generates them.

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

PHASE 1 CLOSURE GATE [C-26]:
  (1) Count Phase 1 items: [N] namespace entries, [M] contributors, [K] artifact paths.
  (2) Declare output set: "Phase 1 produced: PHASE 1 STATE with [N] namespace entries,
      [M] contributors, [K] artifact paths."
  (3) Phase 2 inputs are limited to items in the declared output set above. Phase 2 may
      not introduce artifact data not present in PHASE 1 STATE.
  Pass: "PHASE 1 CLOSURE GATE [C-26]: [N] namespace entries, [M] contributors,
    [K] artifact paths. Output set declared. Phase 2 inputs constrained."

STOP. Phase 1 complete. [C-26]
--- PHASE 1 SEALED [C-26][C-27] ---
Phase 1 scan results are closed. PHASE 1 STATE is immutable.
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

PHASE 2 CLOSURE GATE [C-26]:
  (1) Count Phase 2 items: [7] achievement rows ([N] EARNED, [M] IN-PROGRESS, [K] LOCKED),
      [J] 1-away entries, pattern [LABEL].
  (2) Declare output set: "Phase 2 produced: 7 rows ([N] EARNED, [M] IN-PROGRESS, [K] LOCKED),
      [J] 1-away entries, pattern [LABEL]."
  (3) Phase 3 inputs are limited to items in the declared output set above. Phase 3 may not
      alter EARNED/IN-PROGRESS/LOCKED assignments or category coverage decisions.
  Pass: "PHASE 2 CLOSURE GATE [C-26]: 7 rows ([N] EARNED, [M] IN-PROGRESS, [K] LOCKED),
    [J] 1-away entries, pattern [LABEL]. Output set declared. Phase 3 inputs constrained."

STOP. Phase 2 complete. [C-26]
--- PHASE 2 SEALED [C-26][C-27] ---
Phase 2 classifications are closed. PHASE 2 STATE is immutable.
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

STRUCTURAL AUDIT GATE [C-20/C-26/C-27]:
  Gates executed: [list all gate labels in this run]
  All carry criterion ID [C-20]: [confirmed / violations: list]
  LEADERBOARD CLUSTER enumerates C-16, C-19, C-21 [C-25]: [confirmed]
  ACTIONS CLUSTER enumerates C-05, C-12, C-14, C-20 [C-25]: [confirmed]
  Phase 1 STOP barrier written [C-26]: [confirmed]
  Phase 1 "--- PHASE 1 SEALED [C-26][C-27] ---" pre-printed, [C-27] tag present [C-27]: [confirmed]
  Phase 1 CLOSURE GATE pass confirmation recorded [C-26]: [confirmed]
  Phase 2 STOP barrier written [C-26]: [confirmed]
  Phase 2 "--- PHASE 2 SEALED [C-26][C-27] ---" pre-printed, [C-27] tag present [C-27]: [confirmed]
  Phase 2 CLOSURE GATE pass confirmation recorded [C-26]: [confirmed]
  Result: [N] gates checked. [2] STOP barriers. [2] pre-printed [C-27] markers.
    [2] closure gate confirmations. Violations: [n].
  Fail Tier 1: Gate missing criterion ID -> halt.
  Fail Tier 2: Pre-printed barrier present but [C-27] tag absent -> finding.
  Fail Tier 3: Barrier or closure gate present but permits retroactive Phase N alteration -> halt.
```

**Write artifact**: `simulations/topic/{{topic}}-achievements-{{date}}.md`

---

## V-02 -- Single Axis: C-28 Standalone Manifest Block

**Axis**: C-28 -- at each phase boundary, add a named `PHASE N MANIFEST [C-28]:` block
that is structurally separate from both the SCAN/CLASSIFICATION output and the closure
gate sub-steps. The manifest must appear on the page BEFORE the closure seal. It declares
artifact count plus one additional dimension as a compact, named record.

**Hypothesis**: R9 V-05's closure gate sub-steps already count outputs ("Count Phase 1
items: [N] namespace entries, [M] contributors, [K] artifact paths") before writing the
STOP, satisfying C-28's spirit. But the counts are embedded in numbered sub-step prose
inside the closure gate -- a scorer must interpret the gate pass confirmation to verify
C-28. A standalone MANIFEST block that appears as a named artifact -- `PHASE N MANIFEST
[C-28]: Artifact count: K. Namespace count: N.` -- makes C-28 satisfaction a direct string
match. The manifest is structurally separate from both the gate sub-steps and the STOP
line, so C-28 compliance is auditable independently of C-26. Risk: the manifest block
is inside the template (pre-printed as a label, model fills counts) -- the model could
write wrong counts, but the counts are still on record before the seal, satisfying C-28's
structural requirement.

---

You are running `corps-achievements`. Scan all signal artifacts for the topic. Compute
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

### OUTPUT TEMPLATE

Fill all `[FIELD]` values. Do not modify pre-printed headers, dividers, or barrier lines.

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
  (2) Phase 2 inputs are limited to items in PHASE 1 MANIFEST above. Phase 2 may not
      introduce artifact data not present in PHASE 1 STATE.
  Pass: "PHASE 1 CLOSURE GATE [C-26]: Manifest verified ([K] artifacts, [N] namespaces).
    Phase 2 inputs constrained to PHASE 1 MANIFEST."

STOP. Phase 1 complete. [C-26]
--- PHASE 1 SEALED [C-26] ---
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
  (2) Phase 3 inputs are limited to items in PHASE 2 MANIFEST above. Phase 3 may not
      alter EARNED/IN-PROGRESS/LOCKED assignments or category coverage decisions.
  Pass: "PHASE 2 CLOSURE GATE [C-26]: Manifest verified (7 rows, [N] EARNED).
    Phase 3 inputs constrained to PHASE 2 MANIFEST."

STOP. Phase 2 complete. [C-26]
--- PHASE 2 SEALED [C-26] ---
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

STRUCTURAL AUDIT GATE [C-20/C-26/C-28]:
  Gates executed: [list all gate labels in this run]
  All carry criterion ID [C-20]: [confirmed / violations: list]
  LEADERBOARD CLUSTER enumerates C-16, C-19, C-21 [C-25]: [confirmed]
  ACTIONS CLUSTER enumerates C-05, C-12, C-14, C-20 [C-25]: [confirmed]
  Phase 1 MANIFEST [C-28] block present before seal [C-28]: [confirmed]
  Phase 1 MANIFEST contains artifact count + namespace count [C-28]: [confirmed]
  Phase 1 STOP barrier written [C-26]: [confirmed]
  Phase 1 "--- PHASE 1 SEALED [C-26] ---" present [C-26]: [confirmed]
  Phase 1 CLOSURE GATE references MANIFEST before sealing [C-26]: [confirmed]
  Phase 2 MANIFEST [C-28] block present before seal [C-28]: [confirmed]
  Phase 2 MANIFEST contains row count + EARNED count [C-28]: [confirmed]
  Phase 2 STOP barrier written [C-26]: [confirmed]
  Phase 2 "--- PHASE 2 SEALED [C-26] ---" present [C-26]: [confirmed]
  Phase 2 CLOSURE GATE references MANIFEST before sealing [C-26]: [confirmed]
  Result: [N] gates checked. [2] MANIFEST blocks. [2] STOP barriers. [2] pre-printed markers.
    Violations: [n].
  Fail Tier 1: Gate missing criterion ID -> halt.
  Fail Tier 2: MANIFEST present but lacks second dimension -> finding.
  Fail Tier 3: Barrier or closure gate permits retroactive Phase N alteration -> halt.
```

**Write artifact**: `simulations/topic/{{topic}}-achievements-{{date}}.md`

---

## V-03 -- Single Axis: C-29 Explicit Dual-Layer Declaration

**Axis**: C-29 -- at each phase boundary, add an explicit `DUAL-LAYER BARRIER
[C-26/C-27][C-29]:` block that names both barrier mechanisms (instruction-enforced STOP
and structure-enforced pre-printed divider), asserts their independence, and states the
redundancy property. This variation requires C-26 and C-27 as preconditions, so both
are present in the template. The structural audit gate verifies C-29 by checking for
the dual-layer declaration block at each boundary.

**Hypothesis**: R9 V-04 and V-05 already carry two independent C-26 layers (STOP +
pre-printed), which satisfies C-29's structural requirement. But C-29 compliance is
inferred, not declared: a scorer must identify both mechanisms and confirm they are
independent. An explicit DUAL-LAYER BARRIER block converts this architectural fact from
implicit to named: "Layer 1: STOP declaration (instruction-enforced). Layer 2: pre-printed
divider (structure-enforced). Both must fail simultaneously for barrier omission." The
declaration also enables the structural audit to check C-29 by name. Risk: the
dual-layer declaration block is still a text element the model writes, not the two
mechanisms themselves -- adding the declaration does not change the underlying barrier
architecture, only its auditability. C-28 (output-set manifest) is not added here;
retroactive reframing via reinterpretation is not addressed by C-29 alone.

---

You are running `corps-achievements`. Scan all signal artifacts for the topic. Compute
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

### OUTPUT TEMPLATE

Fill all `[FIELD]` values. Do not modify pre-printed headers, dividers, or barrier lines.
Each phase boundary carries two independent barrier mechanisms [C-29]: the STOP
instruction (Layer 1, instruction-enforced) and the pre-printed sealed divider (Layer 2,
structure-enforced). Both must fail simultaneously for barrier omission.

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

PHASE 1 CLOSURE GATE [C-26]:
  (1) Count Phase 1 items: [N] namespace entries, [M] contributors, [K] artifact paths.
  (2) Declare output set: "Phase 1 produced: PHASE 1 STATE with [N] namespace entries,
      [M] contributors, [K] artifact paths."
  (3) Phase 2 inputs are limited to items in the declared output set above. Phase 2 may
      not introduce artifact data not present in PHASE 1 STATE.
  Pass: "PHASE 1 CLOSURE GATE [C-26]: [N] namespace entries, [M] contributors,
    [K] artifact paths. Output set declared. Phase 2 inputs constrained."

STOP. Phase 1 complete. [C-26]
--- PHASE 1 SEALED [C-26] ---
DUAL-LAYER BARRIER [C-26/C-27][C-29]:
  Layer 1: STOP declaration above (instruction-enforced) [C-26]
  Layer 2: Pre-printed divider above (structure-enforced -- model transcribes, not generates) [C-27]
  Independence: Layer 1 fails if model omits the STOP instruction; Layer 2 fails if model
    actively skips or deletes a pre-printed element. Both must fail simultaneously for
    barrier omission. [C-29]
Phase 1 scan results are closed. PHASE 1 STATE is immutable.
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

PHASE 2 CLOSURE GATE [C-26]:
  (1) Count Phase 2 items: [7] achievement rows ([N] EARNED, [M] IN-PROGRESS, [K] LOCKED),
      [J] 1-away entries, pattern [LABEL].
  (2) Declare output set: "Phase 2 produced: 7 rows ([N] EARNED, [M] IN-PROGRESS, [K] LOCKED),
      [J] 1-away entries, pattern [LABEL]."
  (3) Phase 3 inputs are limited to items in the declared output set above. Phase 3 may not
      alter EARNED/IN-PROGRESS/LOCKED assignments or category coverage decisions.
  Pass: "PHASE 2 CLOSURE GATE [C-26]: 7 rows ([N] EARNED, [M] IN-PROGRESS, [K] LOCKED),
    [J] 1-away entries, pattern [LABEL]. Output set declared. Phase 3 inputs constrained."

STOP. Phase 2 complete. [C-26]
--- PHASE 2 SEALED [C-26] ---
DUAL-LAYER BARRIER [C-26/C-27][C-29]:
  Layer 1: STOP declaration above (instruction-enforced) [C-26]
  Layer 2: Pre-printed divider above (structure-enforced -- model transcribes, not generates) [C-27]
  Independence: Layer 1 fails if model omits the STOP instruction; Layer 2 fails if model
    actively skips or deletes a pre-printed element. Both must fail simultaneously for
    barrier omission. [C-29]
Phase 2 classifications are closed. PHASE 2 STATE is immutable.
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

STRUCTURAL AUDIT GATE [C-20/C-26/C-27/C-29]:
  Gates executed: [list all gate labels in this run]
  All carry criterion ID [C-20]: [confirmed / violations: list]
  LEADERBOARD CLUSTER enumerates C-16, C-19, C-21 [C-25]: [confirmed]
  ACTIONS CLUSTER enumerates C-05, C-12, C-14, C-20 [C-25]: [confirmed]
  Phase 1 STOP barrier written [C-26]: [confirmed]
  Phase 1 "--- PHASE 1 SEALED [C-26] ---" pre-printed [C-26]: [confirmed]
  Phase 1 DUAL-LAYER BARRIER block names Layer 1 + Layer 2 + independence [C-29]: [confirmed]
  Phase 1 CLOSURE GATE pass confirmation recorded [C-26]: [confirmed]
  Phase 2 STOP barrier written [C-26]: [confirmed]
  Phase 2 "--- PHASE 2 SEALED [C-26] ---" pre-printed [C-26]: [confirmed]
  Phase 2 DUAL-LAYER BARRIER block names Layer 1 + Layer 2 + independence [C-29]: [confirmed]
  Phase 2 CLOSURE GATE pass confirmation recorded [C-26]: [confirmed]
  Result: [N] gates checked. [2] STOP barriers. [2] pre-printed markers.
    [2] dual-layer declarations. [2] closure gate confirmations. Violations: [n].
  Fail Tier 1: Gate missing criterion ID -> halt.
  Fail Tier 2: DUAL-LAYER BARRIER block present but missing independence assertion -> finding.
  Fail Tier 3: Barrier or closure gate permits retroactive Phase N alteration -> halt.
```

**Write artifact**: `simulations/topic/{{topic}}-achievements-{{date}}.md`

---

## V-04 -- Combined: C-27 Explicit Tagging + C-28 Standalone Manifest

**Axes**: C-27 (V-01) + C-28 (V-02).

**Hypothesis**: V-01 isolates C-27 auditability (explicit [C-27] tag on pre-printed
barriers); V-02 isolates C-28 auditability (standalone MANIFEST block before seal).
Combining them creates two independently auditable structural properties: the pre-printed
barrier declares its criterion by tag, and the manifest declares its criterion by named
block. The structural audit gate can verify both by direct evidence -- no interpretation
required for either. V-04 does not include the dual-layer declaration (C-29); that
omission means C-29 is satisfied structurally (STOP + pre-printed = two layers) but not
declared. The open weakness is that neither C-27 tagging nor C-28 manifest adds omission
resistance beyond what the pre-printing already provides: retroactive reframing via
reinterpretation remains possible if Phase N+1 scope expands without contradicting the
manifest. The manifest blocks this -- any scope expansion would contradict the recorded
counts -- which is C-28's protection mechanism.

---

You are running `corps-achievements`. Scan all signal artifacts for the topic. Compute
achievement state. Show contributor leaderboard and next recommended action.

**INPUT**: `{{topic}}` (auto-detect from context or Topics.md if not provided)

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

### OUTPUT TEMPLATE [C-27]

Fill all `[FIELD]` values. Do not modify pre-printed headers, dividers, or barrier lines.
Barriers marked `[C-26][C-27]` are pre-printed structural elements.

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

STRUCTURAL AUDIT GATE [C-20/C-26/C-27/C-28]:
  Gates executed: [list all gate labels in this run]
  All carry criterion ID [C-20]: [confirmed / violations: list]
  LEADERBOARD CLUSTER enumerates C-16, C-19, C-21 [C-25]: [confirmed]
  ACTIONS CLUSTER enumerates C-05, C-12, C-14, C-20 [C-25]: [confirmed]
  Phase 1 MANIFEST [C-28] block present before seal [C-28]: [confirmed]
  Phase 1 MANIFEST contains artifact count + namespace count [C-28]: [confirmed]
  Phase 1 "--- PHASE 1 SEALED [C-26][C-27] ---" present with [C-27] tag [C-27]: [confirmed]
  Phase 1 STOP barrier written [C-26]: [confirmed]
  Phase 1 CLOSURE GATE references MANIFEST before sealing [C-26]: [confirmed]
  Phase 2 MANIFEST [C-28] block present before seal [C-28]: [confirmed]
  Phase 2 MANIFEST contains row count + EARNED count [C-28]: [confirmed]
  Phase 2 "--- PHASE 2 SEALED [C-26][C-27] ---" present with [C-27] tag [C-27]: [confirmed]
  Phase 2 STOP barrier written [C-26]: [confirmed]
  Phase 2 CLOSURE GATE references MANIFEST before sealing [C-26]: [confirmed]
  Result: [N] gates checked. [2] MANIFEST blocks (C-28). [2] [C-27]-tagged barriers (C-27).
    [2] STOP barriers. Violations: [n].
  Fail Tier 1: Gate missing criterion ID -> halt.
  Fail Tier 2: [C-27] tag absent from pre-printed barrier -> finding.
  Fail Tier 2: MANIFEST present but lacks second dimension -> finding.
  Fail Tier 3: Barrier or closure gate permits retroactive Phase N alteration -> halt.
```

**Write artifact**: `simulations/topic/{{topic}}-achievements-{{date}}.md`

---

## V-05 -- Full Integration: C-27 Explicit Tagging + C-28 Standalone Manifest + C-29 Dual-Layer Declaration

**Axes**: All three new R10 mechanisms combined.
- V-01 axis: Explicit [C-27] tag on pre-printed barriers
- V-02 axis: Standalone PHASE N MANIFEST [C-28] block before each seal
- V-03 axis: Explicit DUAL-LAYER BARRIER [C-26/C-27][C-29] declaration after each seal

**Hypothesis**: V-01 makes C-27 individually auditable (tag on barrier). V-02 makes C-28
individually auditable (named manifest block). V-03 makes C-29 individually auditable
(dual-layer declaration). Combined, each new criterion has its own named, directly
addressable evidence point in the output: a scorer can verify C-27 by checking for
[C-27] tags, verify C-28 by checking for MANIFEST blocks with two dimensions present
before the STOP, and verify C-29 by checking for DUAL-LAYER BARRIER blocks that name
both layers and assert independence. The structural audit gate in V-05 checks all three
new criteria independently in addition to the full v9 audit checklist. The overlap is
intentional: the DUAL-LAYER BARRIER block names the pre-printed barrier as Layer 2,
so C-27 evidence is cited in both the [C-27] tag on the barrier AND in the declaration
-- making C-27 compliance triply auditable. Risk: the audit gate itself becomes long;
however, the gate is pre-printed in the template and the model fills confirmations into
labeled slots rather than generating the verification logic.

---

You are running `corps-achievements`. Scan all signal artifacts for the topic. Compute
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

### OUTPUT TEMPLATE [C-27]

Fill all `[FIELD]` values. Do not modify pre-printed headers, dividers, barrier lines,
MANIFEST labels, or DUAL-LAYER BARRIER blocks. Barriers marked `[C-26][C-27]` are
pre-printed structural elements (model transcribes, not generates). Each phase boundary
carries two independent barrier mechanisms: instruction-enforced STOP [C-26] and
structure-enforced pre-printed divider [C-27]. Both must fail simultaneously for barrier
omission [C-29].

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

STRUCTURAL AUDIT GATE [C-20/C-26/C-27/C-28/C-29]:
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
  -- Summary --
  Result: [N] gates. [2] STOP barriers (C-26). [2] closure gate confirmations (C-26).
    [2] [C-27]-tagged barriers (C-27). [2] MANIFEST blocks with 2 dimensions each (C-28).
    [2] dual-layer declarations with independence (C-29). Violations: [n].
  Fail Tier 1: Gate missing criterion ID -> halt.
  Fail Tier 2: [C-27] tag absent from pre-printed barrier -> finding.
  Fail Tier 2: MANIFEST present but lacks second dimension -> finding.
  Fail Tier 2: DUAL-LAYER BARRIER present but independence assertion absent -> finding.
  Fail Tier 3: Any barrier or closure gate permits retroactive Phase N alteration -> halt.
```

**Write artifact**: `simulations/topic/{{topic}}-achievements-{{date}}.md`

---

## Variation Summary

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| [C-27] tag on pre-printed barriers | YES | -- | -- | YES | YES |
| Standalone MANIFEST [C-28] block | -- | YES | -- | YES | YES |
| DUAL-LAYER BARRIER [C-29] declaration | -- | -- | YES | -- | YES |
| Structural audit checks C-27 by name | YES | -- | -- | YES | YES |
| Structural audit checks C-28 by name | -- | YES | -- | YES | YES |
| Structural audit checks C-29 by name | -- | -- | YES | -- | YES |
| New mechanism count | 1 | 1 | 1 | 2 | 3 |

## C-27/C-28/C-29 Failure Mode Coverage

| Failure Mode | V-01 | V-02 | V-03 | V-04 | V-05 |
|--------------|------|------|------|------|------|
| C-27: barrier omitted (model skips pre-printed) | DETECTED by audit ([C-27] tag check) | Undetected (no tag) | Undetected (no tag) | DETECTED | DETECTED |
| C-27: barrier present but C-27 criterion unlabeled | FAIL -- tag missing | FAIL -- tag missing | FAIL -- tag missing | PASS | PASS |
| C-28: manifest absent before seal | Undetected | DETECTED (block present check) | Undetected | DETECTED | DETECTED |
| C-28: manifest has only one dimension | Undetected | DETECTED (two-dimension check) | Undetected | DETECTED | DETECTED |
| C-29: dual-layer architecture implicit, not declared | Undetected | Undetected | DETECTED (block present check) | Undetected | DETECTED |
| C-29: independence assertion absent | Undetected | Undetected | DETECTED (assertion check) | Undetected | DETECTED |
| Retroactive scope expansion (reinterpretation) | Not blocked | BLOCKED (manifest contradiction) | Not blocked | BLOCKED | BLOCKED |

## Predicted Scoring (rubric v10)

Aspirational formula: `aspirational_pass / 21 * 10`. C-09 through C-29 = 21 criteria.

**V-01**: C-09--C-26 PASS (baseline). C-27: PASS (tag present + audit check). C-28: PASS
(closure gate sub-steps count outputs, satisfying spirit; no standalone MANIFEST block
means C-28 evidence is embedded in gate pass confirmation -- borderline). C-29: PASS
(STOP + pre-printed = two independent layers; no explicit declaration but structurally
present). Predicted: 19-21/21 aspirational.

**V-02**: C-09--C-26 PASS. C-27: PASS (pre-printed marker present; no [C-27] tag, but
pre-printing itself satisfies C-27). C-28: PASS (standalone MANIFEST block with two
dimensions, explicitly labeled [C-28], before seal). C-29: PASS (STOP + pre-printed =
dual-layer). Predicted: 20-21/21 aspirational.

**V-03**: C-09--C-26 PASS. C-27: PASS (pre-printed barrier present). C-28: PASS (closure
gate sub-steps still enumerate counts). C-29: PASS (explicit dual-layer declaration;
strongest C-29 evidence). Predicted: 21/21 aspirational.

**V-04**: C-09--C-26 PASS. C-27: PASS (explicit tag). C-28: PASS (standalone MANIFEST
block). C-29: PASS (STOP + pre-printed = two independent layers; C-27 tag makes the
second layer explicitly labeled, strengthening C-29 evidence). Predicted: 21/21.

**V-05**: C-09--C-26 PASS. C-27: PASS (tag on barrier + named in dual-layer declaration).
C-28: PASS (standalone MANIFEST with two dimensions + closure gate references manifest).
C-29: PASS (explicit dual-layer declaration with independence assertion, citing both
[C-26] and [C-27] layers by name). Predicted: 21/21.

**Predicted top performer**: V-05 -- all three new criteria have named, directly
addressable evidence points, each individually checkable in the structural audit gate
(now [C-20/C-26/C-27/C-28/C-29]). V-05 is the only variation where a scorer can verify
each criterion by a direct string match without interpretation.

**Open excellence signals** (C-30+ candidates):

- V-03/V-05 introduces a DUAL-LAYER BARRIER block that explicitly asserts independence
  between layers. A potential C-30 criterion: the independence assertion includes a
  description of the specific failure mode each layer blocks (omission vs. reinterpretation),
  creating a typed failure-mode contract rather than a generic independence claim.

- V-02/V-04/V-05 introduces a MANIFEST block that is separate from the closure gate.
  A potential C-31 criterion: the MANIFEST block is cross-referenced from the closure
  gate pass confirmation (gate says "verified against MANIFEST above"), creating a
  traceable record that the seal was written AFTER the manifest was populated, not before.
