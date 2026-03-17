---
skill: quest-variate
skill_target: corps-achievements
round: 11
date: 2026-03-16
rubric_version: 10
basis: R9 V-05 scored 100 on v8 rubric; no R10 variate produced; R11 is first round targeting v10, which adds C-29 (retry loop), C-30 (attribution constraint), and redefines C-28 (first-person ownership)
---

# Variate R11 — corps-achievements

5 complete prompt body variations for the `corps-achievements` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

v10 introduced three changes from v8/v9:

- **C-28 (redefined)**: The pre-write confirmation must be a first-person ownership statement —
  `"Before I write this section, I confirm [C-28]: …"` — binding the model as committed agent,
  not auditor. Framing like "Does X satisfy C-28?" does not satisfy.

- **C-29 (new)**: When any gate fails, the skill must instruct the model to emit a named
  correction triad — `GATE FAILED [C-XX]: [specific instance] — CORRECTION: [action].
  Re-running this section.` — and then re-run the affected section. Halting without re-running
  does not satisfy.

- **C-30 (new)**: The leaderboard pre-write gate must explicitly prohibit inferring
  achievements backward from contributor identity — scores derive from Phase 1 census evidence,
  not from prior knowledge of contributors' roles or prominence.

R9's V-05 (conversational + dense tables) scored 100 on the v8 rubric and carries all
C-01–C-28 baseline. R11 carries that baseline and explores five axes for integrating the
three v10 changes cleanly without structural regressions.

---

## Variation Axes Selected

| Axis | Hypothesis | Used In |
|------|------------|---------|
| C-29 as labeled RETRY blocks | Making C-29 retries visible as labeled blocks (not just instructed) turns the correction procedure into an auditable artifact — the reader can see both the failure and the re-run | V-01, V-04 |
| C-30 as standalone ATTRIBUTION INTEGRITY GATE | Isolating C-30 as its own named gate forces backward-inference prohibition to be a distinct verification step, not a sub-item absorbed into a larger gate pass | V-02, V-04 |
| C-28 pervasive first-person ownership | Applying C-28 "Before I write this section, I confirm [C-28]:" at every output section header — not just leaderboard — creates systematic agent commitment rather than spot-check compliance | V-03, V-04 |
| Stagnation-first lifecycle (C-29 retries as pattern corrections) | Naming the stagnation pattern in Phase 0 before any gate runs makes C-29 retries contextually richer — the retry frame naturally includes "this failure is evidence of [PATTERN_LABEL]" | V-04 |
| C-29/C-30 absorbed into super-gate labels, C-27 updated | Merging C-30 into LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-30] and expanding the structural audit to [C-20/C-25/C-26/C-27/C-28/C-29/C-30] makes both new criteria first-class members of the cluster architecture, enforced by C-27's named super-gate verification | V-05 |

---

## Shared Resources (all variations reference these)

### Stagnation Pattern Registry

| Label | Pattern |
|-------|---------|
| SOLO_ISLAND | One contributor owns all signals — no breadth or coverage diversity |
| NAMESPACE_MOAT | All signals from one namespace — no cross-namespace synthesis possible |
| SPRINT_FREEZE | No new signals added in the current sprint window — momentum stalled |
| SHALLOW_POOL | Multiple topics with <3 signals each — Signal Depth unreached across the board |
| ORPHAN_TOPIC | Topics exist with no contributor metadata — ownership and accountability unknown |

Use label syntax `[PATTERN_LABEL from registry]`. Do not invent labels.

### Weighted Scoring Formula

`Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

- **Signals** = total signal files attributed to this contributor
- **Topics** = count of distinct topics the contributor has contributed to
- **Milestones** = count of the three team milestones this contributor's work evidenced

---

## V-01 — C-29 as Labeled RETRY Blocks

**Axis**: Gate-failure retry loop — C-29 corrections emit a named `RETRY:` block that
makes the re-run visible in output, not merely instructed. Every gate's fail path produces
the correction triad followed by an explicit re-execution boundary.

**Hypothesis**: When the retry is labeled (`> RETRY: [section name]` / `> END RETRY`), the
correction is an observable artifact — the reader can audit both the failure and the corrected
output side by side. A correction that is merely instructed but invisible in output cannot be
verified; a labeled block cannot be silently dropped.

---

You are running `corps-achievements`. Scan the workspace and compute team achievement state.
No arguments. Execute three phases in sequence. Do not begin a phase until the previous
phase's gate passes.

**Gate failure protocol [C-29]**: When any gate fails, emit the correction triad:
```
GATE FAILED [C-XX]: [specific instance] — CORRECTION: [action]. Re-running this section.
> RETRY: [section name]
[Re-executed section output]
> END RETRY
```
Then continue. Do not halt permanently.

---

### STAGNATION PATTERN REGISTRY

| Label | Pattern |
|-------|---------|
| SOLO_ISLAND | One contributor owns all signals — no breadth |
| NAMESPACE_MOAT | All signals from one namespace — no synthesis possible |
| SPRINT_FREEZE | No new signals in current sprint — momentum stalled |
| SHALLOW_POOL | Multiple topics, none reaching Signal Depth |
| ORPHAN_TOPIC | Topics with no contributor metadata — ownership unknown |

Use label syntax `[PATTERN_LABEL from registry]`. Do not invent labels.

### SCORING FORMULA

`Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

---

## PHASE 1 — SCAN AND COMPUTE

### 1A — SCAN [C-01]

Glob `simulations/**/*.md`. Extract topic path, namespace, contributor per file.

```
SCAN STATE (internal):
  Topics: [list]  Namespaces: [list]  Contributors: [list]  Total signals: [n]
```

**SCAN GATE [C-01/C-15]** — numbered sub-steps [C-23]:
> "(1) `simulations/` accessible, >= 1 file from glob.
>  (2) Every file assigned to a real topic path from glob output.
>  (3) Scan state complete. (4) No file skipped."
>
> Pass: "SCAN GATE [C-01]: [n] signals, [n] topics, contributors: [list]."
> Fail: `GATE FAILED [C-01]: [specific path or condition] — CORRECTION: [action]. Re-running this section.`
>   → `> RETRY: 1A SCAN` / `[re-execute glob and rebuild scan state]` / `> END RETRY`

### 1B — ACHIEVEMENTS [C-02/C-06/C-07]

Before I write this section, I confirm [C-28]: every topic from scan state appears below in
either Earned or Locked — I have not added topics from memory and have not skipped any.

Achievement definitions: First Signal (>=1), Signal Depth (>=3), Full Sweep (>=3 namespaces),
Solo Pioneer (1 contributor), Team Topic (>=2 contributors with >=1 signal each).

```markdown
## Earned Achievements — {{date}}

**[topic path]** ([n] signals)
  - **[Achievement name]**: [evidence — counts, contributor names, or namespace list]

## Locked Achievements

**[topic path]** ([n] signals)
  - o [Achievement name]: needs [quantified gap]
```

**COMPUTE GATE [C-02/C-15]** — numbered sub-steps [C-23]:
> "(1) Every scan-state topic appears in Earned or Locked — count matches scan state total.
>  (2) Every Earned entry has specific evidence — no bare achievement names without evidence.
>  (3) Every Locked entry quantifies the gap with a specific count or target."
>
> Pass: "COMPUTE GATE [C-02]: [n] topics covered."
> Fail: `GATE FAILED [C-02]: [specific topic name] — CORRECTION: [add topic to Earned or Locked with evidence]. Re-running this section.`
>   → `> RETRY: 1B ACHIEVEMENTS` / `[re-execute achievements for missing topic]` / `> END RETRY`

### 1C — CONTRIBUTOR LEADERBOARD [C-04/C-16/C-19/C-21/C-30]

Before I write this leaderboard, I confirm [C-28]: my contributor counts are derived from
the Phase 1 achievement census — not from my prior knowledge of who is prominent or active.

**Attribution integrity check [C-30]**: "Is every contributor listed here identified in
scan state? Are their Signals/Topics/Milestones counts derived from census evidence, not
inferred from their name, role, or seniority? If I notice myself assigning higher counts to
a contributor I recognize as senior, I must stop, re-derive from evidence only, and emit the
correction triad."

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
```

Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

**LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]** — numbered sub-steps [C-23]:
> "(1) Formula Score=(Signals×1)+(Topics×3)+(Milestones×5) used — not raw count. [C-16]
>  (2) Worked example Rank 1: Score = {S}×1 + {T}×3 + {M}×5 = {total}. [C-19]
>  (3) Compare {total} to Score column for Rank 1. [C-21]
>  (4) If mismatch: correct Score column; state 'Corrected: {old}→{new}.' [C-21]
>  (5) Score column for Rank 1 = {total}. [C-21]
>  (6) Gate label [C-16/C-19/C-21] enumerates all covered IDs. [C-25]"
>
> Pass: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Passed.
>   Formula (C-16): confirmed. Example (C-19): {total}. Reconciliation (C-21): [applied/clear].
>   Label enumeration (C-25): [C-16/C-19/C-21] verified."
> Fail: `GATE FAILED [C-16]: condition ([n]) — CORRECTION: [action]. Re-running this section.`
>   → `> RETRY: 1C LEADERBOARD` / `[re-execute leaderboard]` / `> END RETRY`
> Not applicable: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Not applicable — no contributors."

### 1D — RECORD PHASE 1 STATE (internal)

```
PHASE 1 STATE:
  Topics covered: [n]
  Achievements earned per topic: [list]
  1-away gap topics: [list/"none"]
  Contributors: [list with scores]
```

---

## PHASE 2 — MILESTONES, GAPS, INSIGHT, AND ACTIONS

### 2A — TEAM MILESTONES [C-03]

```markdown
## Team Milestones — {{date}}

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [path/"—"] | [gap/"—"] |
| shared coverage | EARNED / NOT YET | [2+contrib×2+topics/"—"] | [gap/"—"] |
| debate starter | EARNED / NOT YET | [topic+namespaces/"—"] | [gap/"—"] |
```

**MILESTONES GATE [C-03/C-15]** — numbered sub-steps [C-23]:
> "(1) Row 1 = 'first team signal'. (2) Row 2 = 'shared coverage'. (3) Row 3 = 'debate starter'.
>  (4) Evidence and Gap cells populated or '—'. (5) No row name paraphrased."
>
> Pass: "MILESTONES GATE [C-03]: 3 rows, all cells populated."
> Fail: `GATE FAILED [C-03]: [milestone name, condition] — CORRECTION: [add missing row or populate cell]. Re-running this section.`
>   → `> RETRY: 2A MILESTONES` / `[re-execute milestones table]` / `> END RETRY`

### 2B — 1-AWAY GAPS [C-09/C-18]

```markdown
## Almost There — 1-Away Gaps

| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
|-------------------|-----------------------|-----|---------------------|
```

**1-AWAY GATE [C-09/C-18]** — numbered sub-steps [C-23]:
> "(1) Checked all topics vs all achievement thresholds for exactly-1-step gaps.
>  (2) Checked all milestones for 1-step gaps.
>  (3) Every row has all four columns populated."
>
> Pass: "1-AWAY GATE [C-09/C-18]: [n] 1-away items listed, all four columns present."
> Fail: `GATE FAILED [C-09]: row '[topic]' missing '[column]' — CORRECTION: populate missing column. Re-running this section.`
>   → `> RETRY: 2B 1-AWAY GAPS` / `[re-execute with columns filled]` / `> END RETRY`

### 2C — TEAM INSIGHT [C-10/C-13/C-22]

**Step A**: Candidate insight — specific numbers, names, or topic references.
**Step B**: Per-topic derivability test — for each topic: "Can this be derived from [topic] alone? YES/NO"
**Step C**: All NO → approved. Any YES → generate new candidate (up to 2 attempts).
**Step D**: Confirm distinct from any stagnation pattern or gap statement already made.

**INSIGHT GATE [C-10/C-13/C-22]** — numbered sub-steps [C-23]:
> "(1) Formatted as **TEAM INSIGHT — [descriptive name]:**. [C-13]
>  (2) Cites specific topics, contributors, or numeric values. [C-10]
>  (3) Passed per-topic derivability elimination for every topic in scan state. [C-22]
>  (4) Distinct from any stagnation or gap statement written above. [C-10]"
>
> Pass: "INSIGHT GATE [C-10/C-13/C-22]: Passed."
> Fail: `GATE FAILED [C-10]: condition ([n]) — CORRECTION: [generate new candidate / add specific data]. Re-running this section.`
>   → `> RETRY: 2C TEAM INSIGHT` / `[re-execute with corrected insight]` / `> END RETRY`

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight sentence]
```

### 2D — NEXT ACTIONS [C-05/C-12/C-14/C-17]

State dominant stagnation pattern from registry before writing actions.

```markdown
## Next Actions

Dominant stagnation pattern: **[PATTERN_LABEL from registry]**

1. **[action — namespace and topic explicit]**
   → Unlocks **[Achievement or Milestone]**
   → Breaks **[PATTERN_LABEL from registry]**: [one sentence]

2. [same format]

3. [same format]
```

**ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]** — numbered sub-steps [C-23]:
This gate covers unlock naming (C-05), anti-inertia format (C-12), registry labels (C-14),
and gate ID enumeration (C-20). All four checked together.

> "(1) Each action names specific namespace and topic. [C-05]
>  (2) Each action names exact achievement or milestone it unlocks. [C-05]
>  (3) Format [Action] → Unlocks [X] → Breaks [Pattern]. [C-12]
>  (4) Every pattern label from the registry — no invented labels. [C-14]
>  (5) At least 3 actions. [C-05]
>  (6) Gate label [C-05/C-12/C-14/C-20] enumerates all covered IDs. [C-25]"
>
> Pass: "ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]: Passed.
>   Unlock named (C-05): confirmed. Anti-inertia format (C-12): confirmed.
>   Registry labels (C-14): confirmed. Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified."
> Fail: `GATE FAILED [C-05]: action [n], condition ([n]) — CORRECTION: [rewrite action with explicit unlock]. Re-running this section.`
>   → `> RETRY: 2D NEXT ACTIONS` / `[re-execute actions from the failed row]` / `> END RETRY`

### 2E — RECORD PHASE 2 STATE (internal)

```
PHASE 2 STATE:
  Milestones not yet earned: [list/"all earned"]
  1-away gap topics: [list/"none"]
  Implied missing topics: [list/"none"]
  Retries executed this run: [n, listing section names]
```

---

## PHASE 3 — CROSS-PHASE CORRECTION AND STRUCTURAL AUDIT

### 3A — CROSS-PHASE CONTINUITY GATE [C-24]

**CROSS-PHASE GATE [C-24/C-01/C-02]** — numbered sub-steps [C-23]:
> "(1) Read Phase 2 State: milestone gaps, 1-away topics, implied missing topics.
>  (2) Did Phase 2 gaps surface topics absent from Phase 1 scan state? YES/NO.
>  (3) Did Phase 2 gaps surface contributors absent from Phase 1 leaderboard? YES/NO.
>  (4) YES to (2): add missing topics to Phase 1B Achievements with evidence or gap.
>      State: 'CROSS-PHASE UPDATE [C-24]: topic(s) [list] added.'
>  (5) YES to (3): flag in frontmatter as `c24_missing_contributors: [list]`.
>  (6) NO to both: 'CROSS-PHASE GATE [C-24]: No additions.'
>  (7) Phase 1 topic list and Phase 2 achievement tables finalized."
>
> Pass: "CROSS-PHASE GATE [C-24]: Passed. Additions: [n / 0]."
> Fail: `GATE FAILED [C-24]: [topic or contributor name] — CORRECTION: add to Phase 1B/frontmatter. Re-running this section.`
>   → `> RETRY: 3A CROSS-PHASE` / `[re-execute with additions]` / `> END RETRY`

### 3B — STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]

Scan back through all output in Phases 1–2. List every gate label.

**STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]** — numbered sub-steps [C-23]:
> "(1) List every gate label executed in this run (Phases 1–2 output).
>  (2) For each gate label: confirm it carries at least one [C-XX] criterion ID reference.
>  (3) Verify each multi-criterion super-gate by full label name and exact IDs expected:
>      - 'LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]' — confirm enumerates C-16, C-19, C-21.
>      - 'ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]' — confirm enumerates C-05, C-12, C-14, C-20.
>  (4) Missing ID: 'AUDIT FAIL [C-20/C-26]: gate "[full label]" missing criterion ID.'
>  (5) Wrong enumeration: 'AUDIT FAIL [C-27]: gate "[label]" — expected [C-XX/...], found [C-XX/...].'
>  (6) Count: [n] gates audited, [n] correct, [n] violations.
>  (7) Outcome:
>      All pass: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]: Passed. [n] gates correct,
>        super-gate enumeration verified for [C-16/C-19/C-21] and [C-05/C-12/C-14/C-20].'
>      Any fail: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]: [n] violation(s). See findings.'"
>
> Violations are findings, not blockers — record in frontmatter and proceed.

### WRITE ARTIFACT [C-08]

Write to `simulations/corps/achievements-{{date}}.md`.

```yaml
---
skill: corps-achievements
date: {{date}}
topics_scanned: [n]
topics_added_via_cross_phase: [n or 0]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
stagnation_pattern: [PATTERN_LABEL]
c21_correction_applied: [true/false/not_applicable]
c22_derivability_passed: [true/false]
c24_cross_phase_gate: [additions_made/no_additions]
c25_super_gates: ["LEADERBOARD CLUSTER [C-16/C-19/C-21]", "ACTIONS CLUSTER [C-05/C-12/C-14/C-20]"]
c26_structural_audit_gates_checked: [n]
c26_structural_audit_violations: [n or "none"]
c27_super_gate_enumeration_verified: [true/false]
c29_retries_executed: [n, list of section names or "none"]
c30_attribution_integrity: confirmed
variation: V-01
axis: c29-labeled-retry-blocks
---
```

---

## V-02 — C-30 as Standalone ATTRIBUTION INTEGRITY GATE

**Axis**: C-30 attribution constraint — pulled out of the leaderboard pre-write into a
dedicated named gate `ATTRIBUTION INTEGRITY GATE [C-28/C-30]` that runs before the
leaderboard is written, making the backward-inference prohibition a structurally isolated
verification step.

**Hypothesis**: When C-30 is embedded as sub-step (6) in a larger cluster gate, the model
can satisfy other sub-steps and implicitly treat the attribution check as residual.
A standalone named gate forces the prohibition to be its own pass/fail — it cannot be
absorbed by adjacent criteria passing. Isolation also enables C-27 to verify this gate
label specifically, making the attribution constraint a named member of the gate inventory.

---

You are running `corps-achievements`. Scan the workspace and compute team achievement state.
No arguments. Execute three phases in sequence. Do not begin a phase until the previous
phase's gate passes.

---

### STAGNATION PATTERN REGISTRY

| Label | Pattern |
|-------|---------|
| SOLO_ISLAND | One contributor owns all signals — no breadth |
| NAMESPACE_MOAT | All signals from one namespace — no synthesis possible |
| SPRINT_FREEZE | No new signals in current sprint — momentum stalled |
| SHALLOW_POOL | Multiple topics, none reaching Signal Depth |
| ORPHAN_TOPIC | Topics with no contributor metadata — ownership unknown |

Use label syntax `[PATTERN_LABEL from registry]`. Do not invent labels.

### SCORING FORMULA

`Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

---

## PHASE 1 — SCAN AND COMPUTE

### 1A — SCAN [C-01]

Glob `simulations/**/*.md`. Extract topic path, namespace, contributor per file.

```
SCAN STATE (internal):
  Topics: [list]  Namespaces: [list]  Contributors: [list]  Total signals: [n]
```

**SCAN GATE [C-01/C-15]** — numbered sub-steps [C-23]:
> "(1) `simulations/` accessible, >= 1 file from glob.
>  (2) Every file assigned to a real topic path from glob output.
>  (3) Scan state complete. (4) No file skipped."
>
> Pass: "SCAN GATE [C-01]: [n] signals, [n] topics, contributors: [list]."
> Fail: `GATE FAILED [C-01]: [specific path or condition] — CORRECTION: [action]. Re-running this section.`

### 1B — ACHIEVEMENTS [C-02/C-06/C-07]

Before I write this section, I confirm [C-28]: all topics from scan state appear below — none
added from memory, none skipped.

Achievement definitions: First Signal (>=1), Signal Depth (>=3), Full Sweep (>=3 namespaces),
Solo Pioneer (1 contributor), Team Topic (>=2 contributors with >=1 signal each).

```markdown
## Earned Achievements — {{date}}

**[topic path]** ([n] signals)
  - **[Achievement name]**: [evidence — counts, contributor names, or namespace list]

## Locked Achievements

**[topic path]** ([n] signals)
  - o [Achievement name]: needs [quantified gap]
```

**COMPUTE GATE [C-02/C-15]** — numbered sub-steps [C-23]:
> "(1) Every scan-state topic in Earned or Locked — count matches.
>  (2) Every Earned has specific evidence. (3) Every Locked has quantified gap."
>
> Pass: "COMPUTE GATE [C-02]: [n] topics covered."
> Fail: `GATE FAILED [C-02]: [specific topic name] — CORRECTION: add with evidence or gap. Re-running this section.`

### 1C — ATTRIBUTION INTEGRITY CHECK [C-28/C-30]

Before writing the contributor leaderboard, run this gate as its own verification step.

**ATTRIBUTION INTEGRITY GATE [C-28/C-30]** — numbered sub-steps [C-23]:
> "Before I write this leaderboard, I confirm [C-28]:
>  (1) Every contributor I am about to list was identified in the Phase 1 scan state —
>      I did not add contributors from prior knowledge or familiarity. [C-30]
>  (2) Each contributor's Signals count is the count of signal files attributed to them
>      in scan state — not an estimate based on their role or seniority. [C-30]
>  (3) Each contributor's Topics count is the count of distinct topics in scan state —
>      not inferred from their team membership or responsibilities. [C-30]
>  (4) If I find myself assigning a higher count to a contributor I recognize as a lead or
>      senior member, I must stop, re-derive from census evidence only, and emit:
>      GATE FAILED [C-30]: [contributor name] — CORRECTION: re-derive from scan state only.
>      Re-running this section. [C-29]
>  (5) Gate label [C-28/C-30] enumerates both covered IDs. [C-25]"
>
> Pass: "ATTRIBUTION INTEGRITY GATE [C-28/C-30]: Passed.
>   All contributors from scan state. Scores census-derived. Backward inference: none.
>   Label enumeration (C-25): [C-28/C-30] verified."
> Fail: `GATE FAILED [C-30]: [contributor name, specific inference detected] — CORRECTION: re-derive from scan state. Re-running this section.`

### 1D — CONTRIBUTOR LEADERBOARD [C-04/C-16/C-19/C-21]

(Written only after ATTRIBUTION INTEGRITY GATE passes.)

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
```

Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

**LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]** — numbered sub-steps [C-23]:
> "(1) Formula used — not raw count. [C-16]
>  (2) Worked example Rank 1: {S}×1 + {T}×3 + {M}×5 = {total}. [C-19]
>  (3) Compare {total} to Score column. [C-21]
>  (4) If mismatch: correct and state 'Corrected: {old}→{new}.' [C-21]
>  (5) Score column for Rank 1 = {total}. [C-21]
>  (6) Gate label [C-16/C-19/C-21] enumerates all covered IDs. [C-25]"
>
> Pass: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Passed.
>   Formula (C-16): confirmed. Example (C-19): {total}. Reconciliation (C-21): [applied/clear].
>   Label enumeration (C-25): [C-16/C-19/C-21] verified."
> Fail: `GATE FAILED [C-16]: condition ([n]) — CORRECTION: [action]. Re-running this section.`
> Not applicable: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Not applicable — no contributors."

---

## PHASE 2 — MILESTONES, GAPS, INSIGHT, AND ACTIONS

### 2A — TEAM MILESTONES [C-03]

```markdown
## Team Milestones — {{date}}

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [path/"—"] | [gap/"—"] |
| shared coverage | EARNED / NOT YET | [2+contrib×2+topics/"—"] | [gap/"—"] |
| debate starter | EARNED / NOT YET | [topic+namespaces/"—"] | [gap/"—"] |
```

**MILESTONES GATE [C-03/C-15]** — numbered sub-steps [C-23]:
> "(1) Row 1 = 'first team signal'. (2) Row 2 = 'shared coverage'. (3) Row 3 = 'debate starter'.
>  (4) Evidence and Gap cells populated or '—'."
>
> Pass: "MILESTONES GATE [C-03]: 3 rows confirmed."
> Fail: `GATE FAILED [C-03]: [milestone name] — CORRECTION: add row or populate cell. Re-running this section.`

### 2B — 1-AWAY GAPS [C-09/C-18]

```markdown
## Almost There — 1-Away Gaps

| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
|-------------------|-----------------------|-----|---------------------|
```

**1-AWAY GATE [C-09/C-18]** — numbered sub-steps [C-23]:
> "(1) All topics checked vs thresholds. (2) All milestones checked. (3) All rows four columns."
>
> Pass: "1-AWAY GATE [C-09/C-18]: [n] items, all columns present."
> Fail: `GATE FAILED [C-09]: row '[topic]' missing '[column]' — CORRECTION: populate. Re-running this section.`

### 2C — TEAM INSIGHT [C-10/C-13/C-22]

**Step A**: Candidate insight — specific numbers, names, or topic references.
**Step B**: Per-topic derivability test — for each topic: "Can this be derived from [topic] alone? YES/NO"
**Step C**: All NO → approved. Any YES → generate new candidate (up to 2 attempts).
**Step D**: Confirm distinct from any stagnation pattern or gap statement already made.

**INSIGHT GATE [C-10/C-13/C-22]** — numbered sub-steps [C-23]:
> "(1) Formatted as **TEAM INSIGHT — [descriptive name]:**. [C-13]
>  (2) Cites specific data. [C-10]
>  (3) Passed per-topic derivability test. [C-22]
>  (4) Distinct from gap/stagnation statements above. [C-10]"
>
> Pass: "INSIGHT GATE [C-10/C-13/C-22]: Passed."
> Fail: `GATE FAILED [C-10]: condition ([n]) — CORRECTION: [generate new candidate]. Re-running this section.`

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight sentence]
```

### 2D — NEXT ACTIONS [C-05/C-12/C-14/C-17]

```markdown
## Next Actions

Dominant stagnation pattern: **[PATTERN_LABEL from registry]**

1. **[action — namespace and topic explicit]**
   → Unlocks **[Achievement or Milestone]**
   → Breaks **[PATTERN_LABEL from registry]**: [one sentence]

2. [same format]

3. [same format]
```

**ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]** — numbered sub-steps [C-23]:
> "(1) Each action names namespace and topic. [C-05]
>  (2) Names exact unlock. [C-05]
>  (3) Format [Action] → Unlocks [X] → Breaks [Pattern]. [C-12]
>  (4) Registry labels only. [C-14]
>  (5) At least 3 actions. [C-05]
>  (6) Gate label [C-05/C-12/C-14/C-20] enumerates all covered IDs. [C-25]"
>
> Pass: "ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]: Passed.
>   Unlock named (C-05): confirmed. Anti-inertia format (C-12): confirmed.
>   Registry labels (C-14): confirmed. Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified."
> Fail: `GATE FAILED [C-05]: action [n], condition ([n]) — CORRECTION: rewrite action with explicit unlock and registry label. Re-running this section.`

### 2E — RECORD PHASE 2 STATE (internal)

```
PHASE 2 STATE:
  Milestones not yet earned: [list/"all earned"]
  1-away gap topics: [list/"none"]
  Implied missing topics: [list/"none"]
```

---

## PHASE 3 — CROSS-PHASE CORRECTION AND STRUCTURAL AUDIT

### 3A — CROSS-PHASE CONTINUITY GATE [C-24]

**CROSS-PHASE GATE [C-24/C-01/C-02]** — numbered sub-steps [C-23]:
> "(1) Read Phase 2 State entries.
>  (2) Did Phase 2 gaps surface topics absent from Phase 1 scan state? YES/NO.
>  (3) Did Phase 2 gaps imply contributors absent from Phase 1 leaderboard? YES/NO.
>  (4) YES to (2): add to Phase 1B with evidence or gap.
>      'CROSS-PHASE UPDATE [C-24]: topic(s) [list] added.'
>  (5) YES to (3): frontmatter `c24_missing_contributors: [list]`.
>  (6) NO to both: 'CROSS-PHASE GATE [C-24]: No additions.'
>  (7) Topic list finalized."
>
> Pass: "CROSS-PHASE GATE [C-24]: Passed. Additions: [n / 0]."
> Fail: `GATE FAILED [C-24]: [topic or contributor name] — CORRECTION: add to Phase 1B or frontmatter. Re-running this section.`

### 3B — STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]

Scan back through all output in Phases 1–2. List every gate label.

**STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]** — numbered sub-steps [C-23]:
> "(1) List every gate label executed in this run (Phases 1–2).
>  (2) For each: confirm it carries at least one [C-XX] criterion ID.
>  (3) Verify each multi-criterion super-gate by full label and exact IDs expected:
>      - 'ATTRIBUTION INTEGRITY GATE [C-28/C-30]' — confirm enumerates C-28, C-30.
>      - 'LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]' — confirm enumerates C-16, C-19, C-21.
>      - 'ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]' — confirm enumerates C-05, C-12, C-14, C-20.
>  (4) Missing ID: 'AUDIT FAIL [C-20/C-26]: gate "[label]" missing ID.'
>  (5) Wrong enumeration: 'AUDIT FAIL [C-27]: gate "[label]" — expected [C-XX/...], found [C-XX/...].'
>  (6) Count: [n] gates audited, [n] correct, [n] violations.
>  (7) Outcome:
>      All pass: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]: Passed. [n] gates correct,
>        super-gate enumeration verified for ATTRIBUTION INTEGRITY [C-28/C-30],
>        LEADERBOARD CLUSTER [C-16/C-19/C-21], and ACTIONS CLUSTER [C-05/C-12/C-14/C-20].'
>      Any fail: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]: [n] violation(s).'"
>
> Violations are findings, not blockers.

### WRITE ARTIFACT [C-08]

Write to `simulations/corps/achievements-{{date}}.md`.

```yaml
---
skill: corps-achievements
date: {{date}}
topics_scanned: [n]
topics_added_via_cross_phase: [n or 0]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
stagnation_pattern: [PATTERN_LABEL]
c21_correction_applied: [true/false/not_applicable]
c22_derivability_passed: [true/false]
c24_cross_phase_gate: [additions_made/no_additions]
c25_super_gates: ["ATTRIBUTION INTEGRITY [C-28/C-30]", "LEADERBOARD CLUSTER [C-16/C-19/C-21]", "ACTIONS CLUSTER [C-05/C-12/C-14/C-20]"]
c26_structural_audit_gates_checked: [n]
c26_structural_audit_violations: [n or "none"]
c27_super_gate_enumeration_verified: [true/false]
c30_attribution_gate: standalone
c30_backward_inference: none_detected
variation: V-02
axis: c30-standalone-attribution-gate
---
```

---

## V-03 — C-28 Pervasive First-Person Ownership

**Axis**: C-28 first-person ownership syntax applied at every output section — not just the
leaderboard pre-write, but achievements, milestones, insight, and next actions. Each section
that writes structured output begins with "Before I write this section, I confirm [C-28]: …"

**Hypothesis**: C-28 at a single gate (leaderboard) creates a narrow compliance point that
can be satisfied in isolation while the rest of the skill operates in auditor mode ("Does
X satisfy C-08?"). Pervasive first-person ownership shifts the model's self-framing throughout
execution — it commits as agent at each section boundary rather than completing a checklist
task. This produces more consistent evidence-derivation behavior across all sections, not
just the leaderboard.

---

You are running `corps-achievements`. Scan the workspace and compute team achievement state.
No arguments. Execute three phases in sequence. At every output section, begin with a
first-person confirmation statement before generating content. Do not begin a phase until
the previous phase's gate passes.

---

### STAGNATION PATTERN REGISTRY

| Label | Pattern |
|-------|---------|
| SOLO_ISLAND | One contributor owns all signals — no breadth |
| NAMESPACE_MOAT | All signals from one namespace — no synthesis possible |
| SPRINT_FREEZE | No new signals in current sprint — momentum stalled |
| SHALLOW_POOL | Multiple topics, none reaching Signal Depth |
| ORPHAN_TOPIC | Topics with no contributor metadata — ownership unknown |

Use label syntax `[PATTERN_LABEL from registry]`. Do not invent labels.

### SCORING FORMULA

`Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

---

## PHASE 1 — SCAN AND COMPUTE

### 1A — SCAN [C-01]

Before I run the scan, I confirm [C-28]: I will extract topics, namespaces, and contributors
from actual file paths returned by the glob — not from memory. My scan state will reflect
only what exists on disk.

Glob `simulations/**/*.md`. Extract topic path, namespace, contributor per file.

```
SCAN STATE (internal):
  Topics: [list]  Namespaces: [list]  Contributors: [list]  Total signals: [n]
```

**SCAN GATE [C-01/C-15]** — numbered sub-steps [C-23]:
> "(1) `simulations/` accessible, >= 1 file from glob.
>  (2) Every file assigned to a real topic path from glob output.
>  (3) Scan state complete. (4) No file skipped."
>
> Pass: "SCAN GATE [C-01]: [n] signals, [n] topics, contributors: [list]."
> Fail: `GATE FAILED [C-01]: [specific path or condition] — CORRECTION: [action]. Re-running this section.`

### 1B — ACHIEVEMENTS [C-02/C-06/C-07]

Before I write this section, I confirm [C-28]: every topic I am about to list is present
in scan state. I will not list a topic from memory. My Earned and Locked totals will sum
to the scan state topic count.

Achievement definitions: First Signal (>=1), Signal Depth (>=3), Full Sweep (>=3 namespaces),
Solo Pioneer (1 contributor), Team Topic (>=2 contributors with >=1 signal each).

```markdown
## Earned Achievements — {{date}}

**[topic path]** ([n] signals)
  - **[Achievement name]**: [evidence — counts, contributor names, namespace list]

## Locked Achievements

**[topic path]** ([n] signals)
  - o [Achievement name]: needs [quantified gap]
```

**COMPUTE GATE [C-02/C-15]** — numbered sub-steps [C-23]:
> "(1) Every scan-state topic in Earned or Locked — count matches.
>  (2) Every Earned has specific evidence. (3) Every Locked has quantified gap."
>
> Pass: "COMPUTE GATE [C-02]: [n] topics covered."
> Fail: `GATE FAILED [C-02]: [specific topic] — CORRECTION: add with evidence or gap. Re-running this section.`

### 1C — CONTRIBUTOR LEADERBOARD [C-04/C-16/C-19/C-21/C-30]

Before I write this leaderboard, I confirm [C-28]: my contributor list and all
Signals/Topics/Milestones counts are derived from Phase 1 scan state evidence — not
from my prior knowledge of who the prominent contributors are. I am not inferring
backward from contributor identity. [C-30]

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
```

Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

**LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]** — numbered sub-steps [C-23]:
> "(1) Formula used — not raw count. [C-16]
>  (2) Worked example Rank 1: {S}×1 + {T}×3 + {M}×5 = {total}. [C-19]
>  (3) Compare {total} to Score column. [C-21]
>  (4) If mismatch: correct and state 'Corrected: {old}→{new}.' [C-21]
>  (5) Score column for Rank 1 = {total}. [C-21]
>  (6) Gate label [C-16/C-19/C-21] enumerates all covered IDs. [C-25]"
>
> Pass: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Passed.
>   Formula (C-16): confirmed. Example (C-19): {total}. Reconciliation (C-21): [applied/clear].
>   Label enumeration (C-25): [C-16/C-19/C-21] verified."
> Fail: `GATE FAILED [C-16]: condition ([n]) — CORRECTION: [action]. Re-running this section.`
> Not applicable: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Not applicable — no contributors."

---

## PHASE 2 — MILESTONES, GAPS, INSIGHT, AND ACTIONS

### 2A — TEAM MILESTONES [C-03]

Before I write this section, I confirm [C-28]: the three milestone rows below are populated
from evidence in scan state — I will not mark a milestone EARNED without a specific file
path or contributor/topic count as evidence.

```markdown
## Team Milestones — {{date}}

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [path/"—"] | [gap/"—"] |
| shared coverage | EARNED / NOT YET | [2+contrib×2+topics/"—"] | [gap/"—"] |
| debate starter | EARNED / NOT YET | [topic+namespaces/"—"] | [gap/"—"] |
```

**MILESTONES GATE [C-03/C-15]** — numbered sub-steps [C-23]:
> "(1) Row 1 = 'first team signal'. (2) Row 2 = 'shared coverage'. (3) Row 3 = 'debate starter'.
>  (4) Evidence and Gap cells populated or '—'. (5) No row name paraphrased."
>
> Pass: "MILESTONES GATE [C-03]: 3 rows confirmed."
> Fail: `GATE FAILED [C-03]: [milestone name] — CORRECTION: add or populate. Re-running this section.`

### 2B — 1-AWAY GAPS [C-09/C-18]

Before I write this section, I confirm [C-28]: every row in the 1-away table derives from
a specific topic and achievement threshold I computed above — I will not populate this table
with generic examples.

```markdown
## Almost There — 1-Away Gaps

| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
|-------------------|-----------------------|-----|---------------------|
```

**1-AWAY GATE [C-09/C-18]** — numbered sub-steps [C-23]:
> "(1) All topics checked vs thresholds. (2) All milestones checked. (3) All rows four columns."
>
> Pass: "1-AWAY GATE [C-09/C-18]: [n] items, all columns present."
> Fail: `GATE FAILED [C-09]: row '[topic]' missing '[column]' — CORRECTION: populate. Re-running this section.`

### 2C — TEAM INSIGHT [C-10/C-13/C-22]

Before I write this section, I confirm [C-28]: my candidate insight is grounded in specific
topics and counts from scan state — I will run the per-topic derivability test before
committing to the final insight.

**Step A**: Candidate insight — specific numbers, names, or topic references.
**Step B**: Per-topic derivability test — for each topic: "Can this be derived from [topic] alone? YES/NO"
**Step C**: All NO → approved. Any YES → generate new candidate (up to 2 attempts).
**Step D**: Confirm distinct from any stagnation or gap statement already written.

**INSIGHT GATE [C-10/C-13/C-22]** — numbered sub-steps [C-23]:
> "(1) Formatted as **TEAM INSIGHT — [descriptive name]:**. [C-13]
>  (2) Cites specific data. [C-10]
>  (3) Passed per-topic derivability test. [C-22]
>  (4) Distinct from gap/stagnation statements above. [C-10]"
>
> Pass: "INSIGHT GATE [C-10/C-13/C-22]: Passed."
> Fail: `GATE FAILED [C-10]: condition ([n]) — CORRECTION: generate new candidate with specific data. Re-running this section.`

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight sentence]
```

### 2D — NEXT ACTIONS [C-05/C-12/C-14/C-17]

Before I write this section, I confirm [C-28]: each action below names a specific namespace
and topic, a specific achievement it unlocks, and a registry pattern label it breaks — I will
not write a generic action.

```markdown
## Next Actions

Dominant stagnation pattern: **[PATTERN_LABEL from registry]**

1. **[action — namespace and topic explicit]**
   → Unlocks **[Achievement or Milestone]**
   → Breaks **[PATTERN_LABEL from registry]**: [one sentence]

2. [same format]

3. [same format]
```

**ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]** — numbered sub-steps [C-23]:
> "(1) Each action names namespace and topic. [C-05]
>  (2) Names exact unlock. [C-05]
>  (3) Format [Action] → Unlocks [X] → Breaks [Pattern]. [C-12]
>  (4) Registry labels only. [C-14]
>  (5) At least 3 actions. [C-05]
>  (6) Gate label [C-05/C-12/C-14/C-20] enumerates all covered IDs. [C-25]"
>
> Pass: "ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]: Passed.
>   Unlock named (C-05): confirmed. Anti-inertia format (C-12): confirmed.
>   Registry labels (C-14): confirmed. Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified."
> Fail: `GATE FAILED [C-05]: action [n], condition ([n]) — CORRECTION: rewrite. Re-running this section.`

### 2E — RECORD PHASE 2 STATE (internal)

```
PHASE 2 STATE:
  Milestones not yet earned: [list/"all earned"]
  1-away gap topics: [list/"none"]
  Implied missing topics: [list/"none"]
```

---

## PHASE 3 — CROSS-PHASE CORRECTION AND STRUCTURAL AUDIT

### 3A — CROSS-PHASE CONTINUITY GATE [C-24]

**CROSS-PHASE GATE [C-24/C-01/C-02]** — numbered sub-steps [C-23]:
> "(1) Read Phase 2 State entries.
>  (2) Did Phase 2 gaps surface topics absent from Phase 1 scan state? YES/NO.
>  (3) Did Phase 2 gaps surface contributors absent from Phase 1 leaderboard? YES/NO.
>  (4) YES to (2): add to Phase 1B with evidence or gap.
>      'CROSS-PHASE UPDATE [C-24]: topic(s) [list] added.'
>  (5) YES to (3): frontmatter `c24_missing_contributors: [list]`.
>  (6) NO to both: 'CROSS-PHASE GATE [C-24]: No additions.'
>  (7) Phase 1 topic list finalized."
>
> Pass: "CROSS-PHASE GATE [C-24]: Passed. Additions: [n / 0]."
> Fail: `GATE FAILED [C-24]: [topic or contributor] — CORRECTION: add. Re-running this section.`

### 3B — STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]

Before I write this audit, I confirm [C-28]: I will read back through every gate label
produced in this run — I will not assert that gates pass without scanning the output.

**STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]** — numbered sub-steps [C-23]:
> "(1) List every gate label executed in this run (Phases 1–2).
>  (2) For each: confirm it carries at least one [C-XX] criterion ID.
>  (3) Verify each multi-criterion super-gate by full label and exact IDs expected:
>      - 'LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]' — confirm enumerates C-16, C-19, C-21.
>      - 'ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]' — confirm enumerates C-05, C-12, C-14, C-20.
>  (4) Missing ID: 'AUDIT FAIL [C-20/C-26]: gate "[label]" missing ID.'
>  (5) Wrong enumeration: 'AUDIT FAIL [C-27]: gate "[label]" — expected [C-XX/...], found [C-XX/...].'
>  (6) Count: [n] gates audited, [n] correct, [n] violations.
>  (7) Outcome:
>      All pass: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]: Passed. [n] gates correct,
>        super-gate enumeration verified for [C-16/C-19/C-21] and [C-05/C-12/C-14/C-20].'
>      Any fail: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]: [n] violation(s).'"
>
> Violations are findings, not blockers.

### WRITE ARTIFACT [C-08]

Write to `simulations/corps/achievements-{{date}}.md`.

```yaml
---
skill: corps-achievements
date: {{date}}
topics_scanned: [n]
topics_added_via_cross_phase: [n or 0]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
stagnation_pattern: [PATTERN_LABEL]
c21_correction_applied: [true/false/not_applicable]
c22_derivability_passed: [true/false]
c24_cross_phase_gate: [additions_made/no_additions]
c25_super_gates: ["LEADERBOARD CLUSTER [C-16/C-19/C-21]", "ACTIONS CLUSTER [C-05/C-12/C-14/C-20]"]
c26_structural_audit_gates_checked: [n]
c26_structural_audit_violations: [n or "none"]
c27_super_gate_enumeration_verified: [true/false]
c28_first_person_ownership: pervasive
c30_attribution_check: embedded_in_1c_confirmation
variation: V-03
axis: c28-pervasive-first-person-ownership
---
```

---

## V-04 — Combination: Labeled RETRY Blocks + Standalone Attribution Gate + Stagnation-First

**Axes**: C-29 labeled RETRY blocks (V-01) + C-30 standalone ATTRIBUTION INTEGRITY GATE
(V-02) + stagnation-first lifecycle (Phase 0 pattern diagnosis before any achievement work).

**Hypothesis**: Stagnation-first framing makes C-29 retries more informative — a retry for
a missing topic is not just a data correction but confirmation that the stagnation pattern
predicts the gap. C-30's standalone gate is most defensible after Phase 0 has enumerated
contributors from the workspace without assigning scores, establishing the enumeration as a
prior step separate from scoring. Together: Phase 0 names the pattern, Phase 1A enumerates
contributors from census, Phase 1B runs the attribution gate before scoring, and any gate
failure emits a labeled RETRY block that contextualizes the correction in the pattern frame.

---

You are running `corps-achievements`. Scan the workspace and compute team achievement state.
No arguments. Execute four phases in strict sequence. Phase 0 is the stagnation diagnosis.
Do not begin a phase until the previous phase's gate passes.

**Gate failure protocol [C-29]**: When any gate fails, emit the correction triad:
```
GATE FAILED [C-XX]: [specific instance] — CORRECTION: [action]. Re-running this section.
> RETRY: [section name]
[Re-executed section output]
> END RETRY
```

---

### STAGNATION PATTERN REGISTRY

| Label | Pattern |
|-------|---------|
| SOLO_ISLAND | One contributor owns all signals — no breadth |
| NAMESPACE_MOAT | All signals from one namespace — no synthesis possible |
| SPRINT_FREEZE | No new signals in current sprint — momentum stalled |
| SHALLOW_POOL | Multiple topics, none reaching Signal Depth |
| ORPHAN_TOPIC | Topics with no contributor metadata — ownership unknown |

Use label syntax `[PATTERN_LABEL from registry]`. Do not invent labels.

### SCORING FORMULA

`Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

---

## PHASE 0 — STAGNATION DIAGNOSIS

Before computing any achievements, diagnose the dominant stagnation pattern from workspace
metadata. This frame governs how achievements and retries are interpreted downstream.

Lightweight glob `simulations/**/*.md`. Record only: signal count, contributor count,
namespace count, date of most recent file.

**STAGNATION DIAGNOSIS GATE [C-14/C-17]** — numbered sub-steps [C-23]:
> "(1) contributor count = 1? → SOLO_ISLAND candidate.
>  (2) namespace count = 1? → NAMESPACE_MOAT candidate.
>  (3) most recent file > 7 days ago? → SPRINT_FREEZE candidate.
>  (4) total signals < (topic count × 3)? → SHALLOW_POOL candidate.
>  (5) contributor fields absent or 'unknown'? → ORPHAN_TOPIC candidate.
>  (6) Select single dominant pattern — most strongly evidenced condition above.
>  (7) Label from registry — no invented labels. [C-14]
>  (8) Label is semantic name encoding pattern type. [C-17]"
>
> Pass: "STAGNATION DIAGNOSIS GATE [C-14/C-17]: Dominant = [PATTERN_LABEL]. Evidence: [conditions]."
> Fail: `GATE FAILED [C-14]: condition ([n]) — CORRECTION: re-evaluate using registry labels only. Re-running this section.`
>   → `> RETRY: 0A STAGNATION DIAGNOSIS` / `[re-execute diagnosis]` / `> END RETRY`

```markdown
## Team Stagnation Diagnosis — {{date}}

**Dominant pattern: [PATTERN_LABEL from registry]**
[One sentence: evidence for why this pattern is dominant.]

*All subsequent retries are annotated with whether they are predicted by this pattern.*
```

---

## PHASE 1 — FULL SCAN, ATTRIBUTION CHECK, AND LEADERBOARD

### 1A — SCAN [C-01]

Before I run the scan, I confirm [C-28]: I will build scan state from actual glob output —
not from memory or from the Phase 0 lightweight count.

Glob `simulations/**/*.md` (full extraction). Extract topic path, namespace, contributor.

```
SCAN STATE (internal):
  Topics: [list]  Namespaces: [list]  Contributors: [list]  Total signals: [n]
  Pattern frame: [PATTERN_LABEL from Phase 0]
```

**SCAN GATE [C-01/C-15]** — numbered sub-steps [C-23]:
> "(1) `simulations/` accessible, >= 1 file from glob.
>  (2) Every file assigned to real topic path from glob output.
>  (3) Scan state complete including pattern frame field. (4) No file skipped."
>
> Pass: "SCAN GATE [C-01]: [n] signals, [n] topics, contributors: [list]."
> Fail: `GATE FAILED [C-01]: [specific path] — CORRECTION: re-glob and rebuild scan state. Re-running this section.`
>   → `> RETRY: 1A SCAN` / `[re-execute]` / `> END RETRY`
> Pattern annotation: "Is this failure predicted by [PATTERN_LABEL]? [YES/NO]."

### 1B — ATTRIBUTION INTEGRITY CHECK [C-28/C-30]

**ATTRIBUTION INTEGRITY GATE [C-28/C-30]** — numbered sub-steps [C-23]:
> "Before I write this leaderboard, I confirm [C-28]:
>  (1) Every contributor I am about to list was identified in the Phase 1 scan state. [C-30]
>  (2) Each contributor's Signals/Topics/Milestones counts derive from census evidence only. [C-30]
>  (3) I am NOT using prior knowledge of contributors' roles, seniority, or prominence to
>      assign higher counts. [C-30]
>  (4) If I detect backward inference (a contributor I recognize being scored higher without
>      census support): emit GATE FAILED [C-30] with correction triad and re-run. [C-29]
>  (5) Gate label [C-28/C-30] enumerates both covered IDs. [C-25]"
>
> Pass: "ATTRIBUTION INTEGRITY GATE [C-28/C-30]: Passed.
>   All contributors from scan state. Scores census-derived. Backward inference: none.
>   Label enumeration (C-25): [C-28/C-30] verified."
> Fail: `GATE FAILED [C-30]: [contributor name, specific inference] — CORRECTION: re-derive scores from census. Re-running this section.`
>   → `> RETRY: 1B ATTRIBUTION CHECK` / `[re-execute with census-only scores]` / `> END RETRY`

### 1C — CONTRIBUTOR LEADERBOARD [C-04/C-16/C-19/C-21]

(Written only after ATTRIBUTION INTEGRITY GATE passes.)

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
```

Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

**LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]** — numbered sub-steps [C-23]:
> "(1) Formula used — not raw count. [C-16]
>  (2) Worked example Rank 1: {S}×1 + {T}×3 + {M}×5 = {total}. [C-19]
>  (3) Compare {total} to Score column. [C-21]
>  (4) If mismatch: correct; state 'Corrected: {old}→{new}.' [C-21]
>  (5) Score column for Rank 1 = {total}. [C-21]
>  (6) Gate label [C-16/C-19/C-21] enumerates all covered IDs. [C-25]"
>
> Pass: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Passed.
>   Formula (C-16): confirmed. Example (C-19): {total}. Reconciliation (C-21): [applied/clear].
>   Label enumeration (C-25): [C-16/C-19/C-21] verified."
> Fail: `GATE FAILED [C-16]: condition ([n]) — CORRECTION: [action]. Re-running this section.`
>   → `> RETRY: 1C LEADERBOARD` / `[re-execute]` / `> END RETRY`
> Not applicable: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Not applicable — no contributors."

---

## PHASE 2 — ACHIEVEMENTS, MILESTONES, GAPS, INSIGHT, AND ACTIONS

### 2A — ACHIEVEMENTS [C-02/C-06/C-07]

Before I write this section, I confirm [C-28]: all scan state topics appear below — any
missing topic will be predicted by [PATTERN_LABEL] and named as such.

Achievement definitions: First Signal (>=1), Signal Depth (>=3), Full Sweep (>=3 namespaces),
Solo Pioneer (1 contributor), Team Topic (>=2 contributors).

```markdown
## Earned Achievements — {{date}}
*(Earned despite [PATTERN_LABEL])*

**[topic]** ([n] signals)
  - **[Achievement]**: [evidence using Phase 1 contributor names]

## Locked Achievements
*(Blocked by [PATTERN_LABEL])*

**[topic]** ([n] signals)
  - o [Achievement]: needs [quantified gap] — *predicted by [PATTERN_LABEL]*
```

**COMPUTE GATE [C-02/C-15]** — numbered sub-steps [C-23]:
> "(1) All scan-state topics in Earned or Locked. (2) All Earned have evidence.
>  (3) All Locked have quantified gap. (4) Evidence uses Phase 1 contributor names."
>
> Pass: "COMPUTE GATE [C-02]: [n] topics covered."
> Fail: `GATE FAILED [C-02]: [specific topic] — CORRECTION: add with evidence or gap [predicted by PATTERN_LABEL]. Re-running this section.`
>   → `> RETRY: 2A ACHIEVEMENTS` / `[add missing topic]` / `> END RETRY`

### 2B — TEAM MILESTONES [C-03]

```markdown
## Team Milestones — {{date}}

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [path/"—"] | [gap/"—"] |
| shared coverage | EARNED / NOT YET | [2+contrib×2+topics/"—"] | [gap/"—"] |
| debate starter | EARNED / NOT YET | [topic+namespaces/"—"] | [gap/"—"] |
```

**MILESTONES GATE [C-03/C-15]** — numbered sub-steps [C-23]:
> "(1) Row 1 = 'first team signal'. (2) Row 2 = 'shared coverage'. (3) Row 3 = 'debate starter'.
>  (4) Evidence and Gap populated or '—'."
>
> Pass: "MILESTONES GATE [C-03]: 3 rows confirmed."
> Fail: `GATE FAILED [C-03]: [milestone name] — CORRECTION: add row or populate cell. Re-running this section.`
>   → `> RETRY: 2B MILESTONES` / `[re-execute milestones]` / `> END RETRY`

### 2C — 1-AWAY GAPS [C-09/C-18]

```markdown
## Almost There — 1-Away Gaps

| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
|-------------------|-----------------------|-----|---------------------|
```

**1-AWAY GATE [C-09/C-18]** — numbered sub-steps [C-23]:
> "(1) All topics checked vs thresholds. (2) All milestones checked. (3) All rows four columns."
>
> Pass: "1-AWAY GATE [C-09/C-18]: [n] items."
> Fail: `GATE FAILED [C-09]: row '[topic]' missing '[column]' — CORRECTION: populate. Re-running this section.`
>   → `> RETRY: 2C 1-AWAY GAPS` / `[populate missing column]` / `> END RETRY`

### 2D — TEAM INSIGHT [C-10/C-13/C-22]

Insight must relate to the stagnation pattern frame without merely restating it.

**Step A**: Candidate insight.
**Step B**: Per-topic derivability test.
**Step C**: All NO → approved. Any YES → new candidate (up to 2 attempts).
**Step D**: Confirm distinct from Phase 0 diagnosis.

**INSIGHT GATE [C-10/C-13/C-22]** — numbered sub-steps [C-23]:
> "(1) **TEAM INSIGHT — [name]:**. [C-13]
>  (2) Specific data. [C-10]
>  (3) Per-topic derivability test passed. [C-22]
>  (4) Distinct from Phase 0 stagnation diagnosis. [C-10]"
>
> Pass: "INSIGHT GATE [C-10/C-13/C-22]: Passed."
> Fail: `GATE FAILED [C-10]: condition ([n]) — CORRECTION: generate new candidate. Re-running this section.`
>   → `> RETRY: 2D TEAM INSIGHT` / `[generate new candidate]` / `> END RETRY`

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight sentence]
```

### 2E — NEXT ACTIONS [C-05/C-12/C-14/C-17]

Actions ordered by pattern-breaking impact — highest-impact first.

```markdown
## Next Actions

Dominant stagnation pattern: **[PATTERN_LABEL from registry]**

1. **[action — namespace and topic explicit]**
   → Unlocks **[Achievement or Milestone]**
   → Breaks **[PATTERN_LABEL from registry]**: [mechanism]

2. [same format]

3. [same format]
```

**ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]** — numbered sub-steps [C-23]:
> "(1) Each action names namespace and topic. [C-05]
>  (2) Names exact unlock. [C-05]
>  (3) Format [Action] → Unlocks [X] → Breaks [Pattern]. [C-12]
>  (4) Registry labels only. [C-14]
>  (5) At least 3 actions. [C-05]
>  (6) Gate label [C-05/C-12/C-14/C-20] enumerates all covered IDs. [C-25]"
>
> Pass: "ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]: Passed.
>   Unlock named (C-05): confirmed. Anti-inertia format (C-12): confirmed.
>   Registry labels (C-14): confirmed. Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified."
> Fail: `GATE FAILED [C-05]: action [n], condition ([n]) — CORRECTION: rewrite. Re-running this section.`
>   → `> RETRY: 2E NEXT ACTIONS` / `[re-execute from failed row]` / `> END RETRY`

### 2F — RECORD PHASE 2 STATE (internal)

```
PHASE 2 STATE:
  Milestones not yet earned: [list/"all earned"]
  1-away gap topics: [list/"none"]
  Implied missing topics: [list/"none"]
  RETRY blocks executed: [n, list section names / "none"]
  Pattern frame reconfirmed: [yes/revised to PATTERN_LABEL]
```

---

## PHASE 3 — CROSS-PHASE CORRECTION AND STRUCTURAL AUDIT

### 3A — CROSS-PHASE CONTINUITY GATE [C-24]

**CROSS-PHASE GATE [C-24/C-01/C-02]** — numbered sub-steps [C-23]:
> "(1) Read Phase 2 State entries.
>  (2) Did Phase 2 gaps surface topics absent from Phase 1 scan state? YES/NO.
>  (3) Did Phase 2 gaps surface contributors absent from Phase 1 leaderboard? YES/NO.
>  (4) YES to (2): add to Phase 2A Achievements; 'CROSS-PHASE UPDATE [C-24]: [list] added.'
>  (5) YES to (3): frontmatter `c24_missing_contributors: [list]`.
>  (6) NO to both: 'CROSS-PHASE GATE [C-24]: No additions.'
>  (7) Topic list finalized."
>
> Pass: "CROSS-PHASE GATE [C-24]: Passed. Additions: [n / 0]."
> Fail: `GATE FAILED [C-24]: [topic or contributor] — CORRECTION: add. Re-running this section.`
>   → `> RETRY: 3A CROSS-PHASE` / `[add and re-execute]` / `> END RETRY`

### 3B — STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]

**STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]** — numbered sub-steps [C-23]:
> "(1) List every gate label executed in this run (Phases 0–2).
>  (2) For each: confirm it carries at least one [C-XX] criterion ID.
>  (3) Verify each multi-criterion super-gate by full label and exact IDs expected:
>      - 'STAGNATION DIAGNOSIS GATE [C-14/C-17]' — confirm enumerates C-14, C-17.
>      - 'ATTRIBUTION INTEGRITY GATE [C-28/C-30]' — confirm enumerates C-28, C-30.
>      - 'LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]' — confirm enumerates C-16, C-19, C-21.
>      - 'ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]' — confirm enumerates C-05, C-12, C-14, C-20.
>  (4) Missing ID: 'AUDIT FAIL [C-20/C-26]: gate "[label]" missing ID.'
>  (5) Wrong enumeration: 'AUDIT FAIL [C-27]: gate "[label]" — expected [C-XX/...], found [C-XX/...].'
>  (6) Count: [n] gates, [n] correct, [n] violations.
>  (7) Outcome:
>      All pass: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]: Passed. [n] gates correct,
>        super-gate enumeration verified for STAGNATION DIAGNOSIS [C-14/C-17],
>        ATTRIBUTION INTEGRITY [C-28/C-30], LEADERBOARD CLUSTER [C-16/C-19/C-21],
>        ACTIONS CLUSTER [C-05/C-12/C-14/C-20].'
>      Any fail: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]: [n] violation(s).'"
>
> Violations are findings, not blockers.

### WRITE ARTIFACT [C-08]

Write to `simulations/corps/achievements-{{date}}.md`.

```yaml
---
skill: corps-achievements
date: {{date}}
topics_scanned: [n]
topics_added_via_cross_phase: [n or 0]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
stagnation_pattern: [PATTERN_LABEL]
c21_correction_applied: [true/false/not_applicable]
c22_derivability_passed: [true/false]
c24_cross_phase_gate: [additions_made/no_additions]
c25_super_gates: ["STAGNATION DIAGNOSIS [C-14/C-17]", "ATTRIBUTION INTEGRITY [C-28/C-30]", "LEADERBOARD CLUSTER [C-16/C-19/C-21]", "ACTIONS CLUSTER [C-05/C-12/C-14/C-20]"]
c26_structural_audit_gates_checked: [n]
c26_structural_audit_violations: [n or "none"]
c27_super_gate_enumeration_verified: [true/false]
c29_retries_executed: [n, list of section names or "none"]
c30_attribution_gate: standalone_phase1b
inertia_framing: stagnation-first
variation: V-04
axes: c29-labeled-retry-blocks + c30-standalone-gate + stagnation-first
---
```

---

## V-05 — Combination: C-29/C-30 Absorbed into Super-Gates, C-27 Updated for New Labels

**Axes**: C-30 absorbed into LEADERBOARD CLUSTER GATE making it `[C-16/C-19/C-21/C-30]` +
structural audit expanded to `[C-20/C-25/C-26/C-27/C-28/C-29/C-30]` + C-27's named
super-gate verification extended to cover the new cluster label + dense table output format.

**Hypothesis**: When C-30 is a member of the LEADERBOARD CLUSTER GATE label rather than a
standalone gate, C-27's verification mechanism — which checks for wrong-enumeration failures
in the super-gate label — extends to catch C-30 omissions structurally. A model that
writes `[C-16/C-19/C-21]` when `[C-16/C-19/C-21/C-30]` is required produces an enumeration
error that C-27 will flag, not a silent omission. Similarly, expanding the structural audit
label to cover C-28/C-29/C-30 makes those criteria verifiable by the audit's own gate without
adding new standalone gates. This is the maximum-integration approach: three criteria, two
label changes, one structural audit expansion.

---

You are running `corps-achievements`. Scan the workspace and compute team achievement state.
No arguments. Execute three phases in sequence. All output rendered as tables. Do not begin
a phase until the previous phase's gate passes.

**Gate failure protocol [C-29]**: When any gate fails, emit:
```
GATE FAILED [C-XX]: [specific instance] — CORRECTION: [action]. Re-running this section.
```
Then re-run the affected section. Do not halt permanently.

---

### STAGNATION PATTERN REGISTRY

| Label | Pattern |
|-------|---------|
| SOLO_ISLAND | One contributor owns all signals — no breadth |
| NAMESPACE_MOAT | All signals from one namespace — no synthesis possible |
| SPRINT_FREEZE | No new signals in current sprint — momentum stalled |
| SHALLOW_POOL | Multiple topics, none reaching Signal Depth |
| ORPHAN_TOPIC | Topics with no contributor metadata — ownership unknown |

Use label syntax `[PATTERN_LABEL from registry]`. Do not invent labels.

### SCORING FORMULA

`Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

---

## PHASE 1 — SCAN AND COMPUTE

### 1A — SCAN [C-01]

Glob `simulations/**/*.md`. Extract topic path, namespace, contributor per file.

```
SCAN STATE (internal):
  Topics: [list]  Namespaces: [list]  Contributors: [list]  Total signals: [n]
```

**SCAN GATE [C-01/C-15]** — numbered sub-steps [C-23]:
> "(1) `simulations/` accessible, >= 1 file from glob.
>  (2) Every file assigned to a real topic path from glob output.
>  (3) Scan state complete. (4) No file skipped."
>
> Pass: "SCAN GATE [C-01]: [n] signals, [n] topics, contributors: [list]."
> Fail: `GATE FAILED [C-01]: [specific path or condition] — CORRECTION: re-glob. Re-running this section.`

### 1B — ACHIEVEMENTS TABLE [C-02/C-06/C-07]

Before I write this section, I confirm [C-28]: topic count below matches scan state total.

Achievement definitions: First Signal (>=1), Signal Depth (>=3), Full Sweep (>=3 namespaces),
Solo Pioneer (1 contributor), Team Topic (>=2 contributors).

```markdown
## Earned Achievements — {{date}}

| Topic | Achievement | Evidence |
|-------|-------------|----------|
| [topic] | [achievement] | [counts, names, or namespace list] |

## Locked Achievements

| Topic | Achievement | Gap (exact count or target) |
|-------|-------------|------------------------------|
| [topic] | [achievement] | [e.g., "2 more signals", "1 more namespace"] |
```

**COMPUTE GATE [C-02/C-15]** — numbered sub-steps [C-23]:
> "(1) Topic count across Earned+Locked matches scan state total.
>  (2) Every Earned row has Evidence populated.
>  (3) Every Locked row has specific quantified Gap."
>
> Pass: "COMPUTE GATE [C-02]: [n] topics covered."
> Fail: `GATE FAILED [C-02]: [specific topic] — CORRECTION: add row. Re-running this section.`

### 1C — CONTRIBUTOR LEADERBOARD TABLE [C-04/C-16/C-19/C-21/C-30]

Before I write this leaderboard, I confirm [C-28]: contributor counts are derived from
Phase 1 census — not from prior knowledge of contributor identity, role, or prominence [C-30].

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
```

Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

**LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-30]** — numbered sub-steps [C-23]:
This gate covers formula-driven scoring (C-16), worked example (C-19), reconciliation loop
(C-21), and achievement-derived attribution constraint (C-30). All four together: C-16 without
C-19 is an unverifiable claim; C-19 without C-21 is display without enforcement; C-21 without
C-30 audits formula correctness but not the integrity of the inputs it operates on.

> "(1) Leaderboard uses formula Score=(Signals×1)+(Topics×3)+(Milestones×5) — not raw count. [C-16]
>  (2) Worked example Rank 1: Score = {S}×1 + {T}×3 + {M}×5 = {total}. [C-19]
>  (3) Compare {total} to Score column for Rank 1. [C-21]
>  (4) If mismatch: correct Score column to {total}; state 'Corrected: {old}→{new}.' [C-21]
>  (5) Score column for Rank 1 = {total}. [C-21]
>  (6) Every contributor in this table was identified in Phase 1 scan state — not inferred
>      from prior knowledge of who is prominent. Scores derive from census evidence only. [C-30]
>  (7) Gate label [C-16/C-19/C-21/C-30] enumerates all four covered IDs. [C-25]"
>
> Pass: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-30]: Passed.
>   Formula (C-16): confirmed. Example (C-19): {total}. Reconciliation (C-21): [applied/clear].
>   Attribution (C-30): census-derived, no backward inference.
>   Label enumeration (C-25): [C-16/C-19/C-21/C-30] verified."
> Fail: `GATE FAILED [C-16 or C-30]: condition ([n]) — CORRECTION: [re-derive from census / correct formula]. Re-running this section.`
> Not applicable: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-30]: Not applicable — no contributors."

---

## PHASE 2 — MILESTONES, GAPS, INSIGHT, AND ACTIONS

### 2A — MILESTONES TABLE [C-03]

```markdown
## Team Milestones — {{date}}

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [path/"—"] | [gap/"—"] |
| shared coverage | EARNED / NOT YET | [2+contrib×2+topics/"—"] | [gap/"—"] |
| debate starter | EARNED / NOT YET | [topic+namespaces/"—"] | [gap/"—"] |
```

**MILESTONES GATE [C-03/C-15]** — numbered sub-steps [C-23]:
> "(1) Row 1 = 'first team signal'. (2) Row 2 = 'shared coverage'. (3) Row 3 = 'debate starter'.
>  (4) Evidence and Gap populated or '—'. (5) No row name paraphrased."
>
> Pass: "MILESTONES GATE [C-03]: 3 rows confirmed."
> Fail: `GATE FAILED [C-03]: [milestone name, condition] — CORRECTION: add or populate. Re-running this section.`

### 2B — 1-AWAY GAPS TABLE [C-09/C-18]

```markdown
## Almost There — 1-Away Gaps

| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
|-------------------|-----------------------|-----|---------------------|
```

**1-AWAY GATE [C-09/C-18]** — numbered sub-steps [C-23]:
> "(1) All topics checked vs thresholds. (2) All milestones checked. (3) All rows four columns."
>
> Pass: "1-AWAY GATE [C-09/C-18]: [n] items, all columns present."
> Fail: `GATE FAILED [C-09]: row '[topic]' missing '[column]' — CORRECTION: populate. Re-running this section.`

### 2C — TEAM INSIGHT [C-10/C-13/C-22]

**Step A**: Candidate insight.
**Step B**: Per-topic derivability test — for each topic: "Can this be derived from [topic] alone? YES/NO"
**Step C**: All NO → approved. Any YES → new candidate (up to 2 attempts).
**Step D**: Confirm distinct from gap or stagnation statement already made.

**INSIGHT GATE [C-10/C-13/C-22]** — numbered sub-steps [C-23]:
> "(1) **TEAM INSIGHT — [descriptive name]:**. [C-13]
>  (2) Specific data. [C-10]
>  (3) Per-topic derivability test passed. [C-22]
>  (4) Distinct from gap/stagnation above. [C-10]"
>
> Pass: "INSIGHT GATE [C-10/C-13/C-22]: Passed."
> Fail: `GATE FAILED [C-10]: condition ([n]) — CORRECTION: generate new candidate. Re-running this section.`

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight sentence]
```

### 2D — NEXT ACTIONS TABLE [C-05/C-12/C-14/C-17]

```markdown
## Next Actions

Dominant stagnation pattern: **[PATTERN_LABEL from registry]**

| # | Action (namespace + topic explicit) | Unlocks | Breaks (from registry) |
|---|-------------------------------------|---------|------------------------|
| 1 | [action] | [Achievement/Milestone] | [PATTERN_LABEL from registry] |
| 2 | [action] | [Achievement/Milestone] | [PATTERN_LABEL from registry] |
| 3 | [action] | [Achievement/Milestone] | [PATTERN_LABEL from registry] |
```

**ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]** — numbered sub-steps [C-23]:
> "(1) Each row names specific namespace and topic. [C-05]
>  (2) Each row has Unlocks column populated with exact achievement or milestone. [C-05]
>  (3) Each row's Breaks column uses registry label — no invented labels. [C-14]
>  (4) At least 3 rows. [C-05]
>  (5) Gate label [C-05/C-12/C-14/C-20] enumerates all covered IDs. [C-25]"
>
> Pass: "ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]: Passed.
>   Unlock named (C-05): confirmed. Anti-inertia format (C-12): confirmed.
>   Registry labels (C-14): confirmed. Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified."
> Fail: `GATE FAILED [C-05]: row [n], condition ([n]) — CORRECTION: rewrite row. Re-running this section.`

### 2E — RECORD PHASE 2 STATE (internal)

```
PHASE 2 STATE:
  Milestones not yet earned: [list/"all earned"]
  1-away gap topics: [list/"none"]
  Implied missing topics: [list/"none"]
  Retries executed: [n, section names / "none"]
```

---

## PHASE 3 — CROSS-PHASE CORRECTION AND STRUCTURAL AUDIT

### 3A — CROSS-PHASE CONTINUITY GATE [C-24]

**CROSS-PHASE GATE [C-24/C-01/C-02]** — numbered sub-steps [C-23]:
> "(1) Read Phase 2 State entries.
>  (2) Did Phase 2 gaps surface topics absent from Phase 1 scan state? YES/NO.
>  (3) Did Phase 2 gaps surface contributors absent from Phase 1 leaderboard? YES/NO.
>  (4) YES to (2): add to Phase 1B Earned/Locked tables.
>      'CROSS-PHASE UPDATE [C-24]: topic(s) [list] added.'
>  (5) YES to (3): frontmatter `c24_missing_contributors: [list]`.
>  (6) NO to both: 'CROSS-PHASE GATE [C-24]: No additions.'
>  (7) Topic list and achievement tables finalized."
>
> Pass: "CROSS-PHASE GATE [C-24]: Passed. Additions: [n / 0]."
> Fail: `GATE FAILED [C-24]: [topic or contributor] — CORRECTION: add. Re-running this section.`

### 3B — STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27/C-28/C-29/C-30]

Scan back through all output in Phases 1–2. List every gate label.

**STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27/C-28/C-29/C-30]** — numbered sub-steps [C-23]:
This gate covers: gate ID references (C-20), multi-criterion label enumeration (C-25),
meta-verification of gate labels (C-26), named super-gate verification (C-27), first-person
ownership syntax presence (C-28), correction triad in fail paths (C-29), and attribution
constraint coverage (C-30). All seven verified together — C-27 without C-28/C-29/C-30 would
audit the v8 super-gate labels but miss the v10 additions.

> "(1) List every gate label executed in this run (Phases 1–2 output).
>  (2) For each gate label: confirm it carries at least one [C-XX] criterion ID. [C-20]
>  (3) Verify each multi-criterion super-gate by full label name and exact IDs expected: [C-27]
>      - 'LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-30]' — confirm enumerates C-16, C-19, C-21, C-30.
>      - 'ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]' — confirm enumerates C-05, C-12, C-14, C-20.
>  (4) Confirm this skill includes at least one gate with a first-person 'Before I write...
>      I confirm [C-28]:' ownership statement. [C-28]
>  (5) Confirm all gate fail paths in this run used the correction triad format
>      'GATE FAILED [C-XX]: [instance] — CORRECTION: [action]. Re-running this section.' [C-29]
>  (6) Confirm the LEADERBOARD CLUSTER GATE label includes C-30 (not [C-16/C-19/C-21] alone). [C-30]
>  (7) Any gate missing criterion ID: 'AUDIT FAIL [C-20/C-26]: gate "[label]" missing ID.'
>  (8) Any super-gate with wrong enumeration: 'AUDIT FAIL [C-27]: gate "[label]" — expected
>      [C-XX/...], found [C-XX/...].'
>  (9) C-28 missing: 'AUDIT FAIL [C-28]: no first-person ownership statement found.'
>  (10) C-29 fail path non-conforming: 'AUDIT FAIL [C-29]: gate "[label]" fail path does
>       not use correction triad format.'
>  (11) C-30 missing from leaderboard label: 'AUDIT FAIL [C-30]: LEADERBOARD CLUSTER GATE
>       label missing C-30 — found [label], expected [C-16/C-19/C-21/C-30].'
>  (12) Count: [n] gates audited, [n] correct, [n] violations.
>  (13) Outcome:
>       All pass: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27/C-28/C-29/C-30]: Passed.
>         [n] gates correct. Super-gate enumeration verified:
>         LEADERBOARD CLUSTER [C-16/C-19/C-21/C-30] — C-16, C-19, C-21, C-30 confirmed.
>         ACTIONS CLUSTER [C-05/C-12/C-14/C-20] — C-05, C-12, C-14, C-20 confirmed.
>         C-28 first-person ownership: present. C-29 correction triads: all fail paths conforming.
>         C-30 attribution label: present.'
>       Any fail: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27/C-28/C-29/C-30]: [n] violation(s).'"
>
> Violations are findings, not blockers — record in frontmatter and write the artifact.

### WRITE ARTIFACT [C-08]

Write to `simulations/corps/achievements-{{date}}.md`.

```yaml
---
skill: corps-achievements
date: {{date}}
topics_scanned: [n]
topics_added_via_cross_phase: [n or 0]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
stagnation_pattern: [PATTERN_LABEL]
c21_correction_applied: [true/false/not_applicable]
c22_derivability_passed: [true/false]
c24_cross_phase_gate: [additions_made/no_additions]
c25_super_gates: ["LEADERBOARD CLUSTER [C-16/C-19/C-21/C-30]", "ACTIONS CLUSTER [C-05/C-12/C-14/C-20]"]
c26_structural_audit_gates_checked: [n]
c26_structural_audit_violations: [n or "none"]
c27_super_gate_enumeration_verified: [true/false]
c28_first_person_ownership: present
c29_retries_executed: [n, list of section names or "none"]
c29_fail_path_conformance: [all_triads/partial/not_triggered]
c30_leaderboard_cluster_label: "[C-16/C-19/C-21/C-30]"
c30_attribution_constraint: census-derived-only
output_format: dense-table
variation: V-05
axes: c29-c30-super-gate-integration + c27-updated-labels + dense-table
---
```
