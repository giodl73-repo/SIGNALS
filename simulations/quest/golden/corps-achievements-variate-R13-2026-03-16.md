---
skill: quest-variate
skill_target: corps-achievements
round: 13
date: 2026-03-16
rubric_version: 12
basis: R12 V-01 (global RETRY PROTOCOL + standalone attribution gate + 9-gate structural audit)
       scored highest on v11 rubric. R13 targets all seven v12 additions: C-35 (named retry step
       labels), C-36 (row-count assertion in structural audit), C-37 (preamble OUTPUT SCHEMAS),
       C-38 (attribution gate fires before Phase 1 scan), C-39 (phase exit/entry contracts),
       C-40 (universal first-person at all section headers), C-41 (pre-evidence insight hypothesis).
---

# Variate R13 — corps-achievements

5 complete prompt body variations for the `corps-achievements` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

v12 introduced seven changes from v11:

- **C-35 (new)**: Global retry protocol block subdivides into explicitly named sequential steps
  with shorthand labels — `Step 1 TRIAD:`, `Step 2 DELIMIT:`, `Step 3 CONTINUE:` — making each
  retry phase individually addressable. Descriptive step text without shorthand labels does not
  satisfy.

- **C-36 (new)**: Structural audit gate asserts the expected item count explicitly —
  `"Row count = N. All N enumerated."` — making N-completeness machine-checkable. Enumerating
  all gates correctly but omitting the count assertion does not satisfy.

- **C-37 (new)**: Output schemas declared as a preamble-level artifact (an `OUTPUT SCHEMAS`
  block) before any gate fires. Schema specifications embedded inside individual gate conditions
  (e.g., column list inside C-18's gate check) do not satisfy this criterion.

- **C-38 (new)**: Attribution integrity gate fires before Phase 1 evidence scanning begins —
  committing to an empty contributor list before any artifacts are read, making backward inference
  architecturally impossible. A standalone attribution gate (C-33) that fires after any evidence
  has been gathered does not satisfy, even with the prohibition explicitly stated.

- **C-39 (new)**: Each phase boundary carries an explicit exit contract (what this phase produced)
  and entry contract (what the next phase requires) — turning transitions into verifiable handoff
  points. Cross-phase gate questions (C-24) without formal contract objects do not satisfy.

- **C-40 (new)**: First-person ownership framing extended to ALL major section headers and phase
  openers, not only gate confirmation statements. Phase openers use "I will now scan...",
  "I am generating the leaderboard..." etc. Satisfying C-28 in gate confirmations only does not
  satisfy.

- **C-41 (new)**: Before generating the cross-topic insight, the skill instructs the model to
  state a candidate hypothesis — the tentative insight claim — before consulting achievement
  evidence, then confirm or revise after the derivability test. Applying the derivability test
  after composing the insight without a pre-evidence hypothesis declaration does not satisfy.

R12's best performer was V-01 (module-style RETRY PROTOCOL + Phase-2-to-3 standalone attribution
+ 9-gate tabular audit). R13 carries that foundation and explores five axes for implementing all
seven new criteria.

---

## Gate Catalog (R13 — 9 cluster gates)

V-01 and V-03 keep the R12 gate labels. V-02 repositions the attribution gate to Phase-0.
V-04 and V-05 update INSIGHT GATE and STRUCTURAL AUDIT GATE to absorb C-41 and C-36 respectively.
The structural audit must enumerate all 9 gates (C-34) with exact criterion IDs (C-27).

| Gate | Criterion IDs | Notes |
|------|--------------|-------|
| ATTRIBUTION INTEGRITY GATE | [C-28/C-30] | C-38: must fire before Phase 1 scan in V-02/V-04/V-05 |
| SCAN GATE | [C-01/C-02/C-23] | — |
| MILESTONE GATE | [C-03/C-23] | — |
| ACHIEVEMENT CLUSTER GATE | [C-06/C-07/C-11/C-23] | — |
| LEADERBOARD CLUSTER GATE | [C-16/C-19/C-21/C-25] | — |
| 1-AWAY GATE | [C-09/C-18/C-23] | — |
| ACTIONS GATE | [C-05/C-12/C-14/C-20/C-25] | — |
| INSIGHT GATE | [C-10/C-13/C-22/C-24/C-25] or [C-10/C-13/C-22/C-24/C-25/C-41] | C-41 absorbed in V-04/V-05 |
| STRUCTURAL AUDIT GATE | [C-26/C-27/C-34] or [C-26/C-27/C-34/C-36] | C-36 absorbed in V-01/V-05 |

---

## Variation Axes Selected

| Axis | Hypothesis | Used In |
|------|------------|---------|
| C-35/C-36: Named step labels + row-count assertion | Shorthand step labels (TRIAD/DELIMIT/CONTINUE) make each retry phase a named target — a partial execution is diagnosable by step name. Row-count assertion in the audit makes N-completeness a single arithmetic check rather than a semantic enumeration read. | V-01, V-05 |
| C-37/C-38: Preamble OUTPUT SCHEMAS + Phase-0 attribution gate | Declaring schemas before gates fires anchors all section structure to a shared reference artifact, not a gate condition. Moving the attribution gate to Phase-0 makes backward inference architecturally impossible: there is no evidence yet to back-attribute from. | V-02, V-04, V-05 |
| C-39/C-40: Phase exit/entry contracts + universal first-person | Formalizing handoffs as typed contracts turns phase transitions into verifiable transfer points. Extending first-person framing to ALL structural boundaries makes committed agency visible throughout — the model's ownership claim is not limited to gate confirmations. | V-03, V-05 |
| C-41 as pre-evidence HYPOTHESIS block | Requiring a hypothesis declaration before consulting evidence forces genuine prediction rather than post-hoc narrative. The hypothesis becomes a falsifiable claim — it either survives the derivability test or is revised, and both outcomes are visible in the output. | V-04, V-05 |

---

## Shared Resources (all variations)

### STAGNATION PATTERN REGISTRY

| Label | Pattern |
|-------|---------|
| SOLO_ISLAND | One contributor owns all signals for a topic — no peer coverage |
| NAMESPACE_MOAT | All signals from one namespace — cross-namespace synthesis blocked |
| SPRINT_FREEZE | No new signals in current sprint window — momentum stalled |
| SHALLOW_POOL | Multiple topics each with <3 signals — Signal Depth unreached across the board |
| ORPHAN_TOPIC | Topic in TOPICS.md with zero signal artifacts — unstarted |

Use label syntax `[PATTERN_LABEL from registry]` only. Do not invent labels inline.

### WEIGHTED SCORING FORMULA

`Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

- **Signals** = total signal files attributed to contributor
- **Topics** = count of distinct topics contributor has contributed to
- **Milestones** = count of team milestones contributor's work evidenced

---

---

## V-01 — Axis: C-35/C-36 Named Retry Steps + Row-Count Assertion

**Axis**: Two focused structural upgrades to the R12 V-01 baseline — rename the RETRY PROTOCOL
steps to shorthand labels that are individually addressable (C-35), and add an explicit row-count
assertion to the structural audit (C-36).

**Hypothesis**: When retry steps carry shorthand labels (TRIAD/DELIMIT/CONTINUE), a partial retry
execution is diagnosable by step name — "the model completed Step 1 TRIAD but not Step 2 DELIMIT"
is a precise failure description. When the structural audit asserts "Row count = 9. All 9
enumerated.", the completeness check becomes a single arithmetic comparison rather than a semantic
read of the list.

---

```
═══════════════════════════════════════════════════════
RETRY PROTOCOL [C-29/C-31/C-32/C-35]
═══════════════════════════════════════════════════════
This is the global retry protocol for all gates in this skill.
Do not embed separate retry instructions in any gate fail-path.
All gates reference this block by name only.

When any gate fails, execute these steps in order:

Step 1 TRIAD:
  Emit the named correction triad:
  GATE FAILED [C-XX]: [specific instance that triggered failure] — CORRECTION: [action to take]. Re-running this section.

Step 2 DELIMIT:
  Wrap the re-run output in labeled delimiters:
  > RETRY [C-XX]: [specific instance]
  [re-run output here — complete section, not summary]
  > END RETRY [C-XX]

Step 3 CONTINUE:
  Proceed to the next gate. Do not halt permanently.
═══════════════════════════════════════════════════════

STAGNATION PATTERN REGISTRY — see Shared Resources.
SCORING FORMULA — Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)
```

---

You are running `/corps-achievements` for the Signal plugin workspace.
Scan all signal artifacts, compute team-level achievements, and deliver a full achievement report.
Sprint anchor: use the most recent artifact date or the date in TOPICS.md.

Execute phases in order. Do not begin a phase until its gate passes.
On gate failure: apply RETRY PROTOCOL — do not embed retry logic here.

---

### Phase 1 — Artifact Scan

Glob `simulations/**/*.md`. For each file, extract: topic path, namespace, skill, contributor,
and date. Build the internal scan state:

```
SCAN STATE:
  Topics: [list]     Namespaces: [list]     Contributors: [list]     Total signals: [n]
```

Cross-reference topics against TOPICS.md. Flag any topic in TOPICS.md with no matching artifacts
as `[ORPHAN_TOPIC from registry]`.

**SCAN GATE [C-01/C-02/C-23]**
Before I write the scan state, I confirm [C-01/C-02/C-23]:
(1) Every topic in my list is traceable to a real file from the glob — no hallucinated topics.
(2) Every discovered topic will appear in the achievements output section — none will be dropped.
(3) TOPICS.md topics with no artifacts are explicitly marked [ORPHAN_TOPIC from registry].
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 2 — Milestones

Evaluate which of the three team milestones are earned across the full workspace:
- **First Team Signal**: any contributor has filed any signal on any topic.
- **Shared Coverage**: at least two contributors have signals on the same topic.
- **Debate Starter**: at least two competing signals in the same topic+namespace pair.

Output sprint framing: "Sprint ending {date} — {N} topics tracked."

**MILESTONE GATE [C-03/C-23]**
Before I write the milestones section, I confirm [C-03/C-23]:
(1) "First Team Signal" appears by exact name in the output.
(2) "Shared Coverage" appears by exact name in the output.
(3) "Debate Starter" appears by exact name in the output.
If any sub-condition fails: apply RETRY PROTOCOL.

---

### ATTRIBUTION INTEGRITY GATE [C-28/C-30]

Before I write any contributor-attributing section, I confirm [C-28/C-30]:
(1) Every contributor I am about to credit is traceable to a real artifact filename or
    frontmatter field discovered in Phase 1 — no contributor was inferred from their
    known role, seniority, or prior project prominence.
(2) No achievement or score will be attributed to any contributor not present in scan state.
If condition (1) fails: apply RETRY PROTOCOL — specify the contributor name not evidenced.
If condition (2) fails: apply RETRY PROTOCOL — specify the attribution that lacks artifact basis.

---

### Phase 3 — Achievement Census

For each topic, list earned (✓) and available (○) achievements.
Group under two named categories:
- **Category A — Individual Signals**: First Signal, Signal Depth (≥3), Full Sweep (≥3 namespaces)
- **Category B — Team Milestones**: First Team Signal, Shared Coverage, Debate Starter

**ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23]**
Before I write the achievements section, I confirm [C-06/C-07/C-11/C-23]:
(1) Earned (✓) and available (○) achievements are visually distinguished for every topic row.
(2) All achievements appear under a named category label — at least Category A and Category B.
(3) Self-test: does every next action I plan to write name the exact achievement it unlocks?
    I commit: yes, I will enforce this in Phase 6 before writing any action row.
(4) Gate label enumerates all covered IDs: C-06, C-07, C-11, C-23.
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 4 — Contributor Leaderboard

Using Phase 1 scan state (not prior knowledge), compute contributor scores.
Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`
Rank by Score descending.

Render worked example for Rank-1 inline above the table:
`Rank-1 calculation: Score = {S}×1 + {T}×3 + {M}×5 = {total}`

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|

**LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25]**
Before I write the leaderboard table, I confirm [C-16/C-19/C-21/C-25]:
(1) Every row uses Score = Signals×1 + Topics×3 + Milestones×5 — no rank-ordered counts. [C-16]
(2) Rank-1 worked example is rendered inline above the table. [C-19]
(3) If the worked example total ≠ Score column for Rank-1, I correct the table before continuing. [C-21]
(4) Gate label enumerates all covered IDs: C-16, C-19, C-21, C-25. [C-25]
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 5 — 1-Away Callouts

Identify every topic or contributor exactly one action away from unlocking an achievement.
Render as a dedicated structured table:

| Topic/Target | Achievement to Unlock | Gap (What's Missing) | Exact Action Needed |
|---|---|---|---|

**1-AWAY GATE [C-09/C-18/C-23]**
Before I write the 1-away table, I confirm [C-09/C-18/C-23]:
(1) The 1-away section is standalone — not merged with next actions or achievements.
(2) Table has all four columns: Topic/Target, Achievement to Unlock, Gap, Exact Action Needed.
(3) Every row has all four columns populated — no blank cells, no merged prose.
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 6 — Next Actions

For each recommended action, use anti-inertia format:
`[Action] → Unlocks [Achievement] → Breaks [PATTERN_LABEL from registry]`

All pattern labels must come from the Stagnation Pattern Registry. No inline invented labels.

**ACTIONS GATE [C-05/C-12/C-14/C-20/C-25]**
Before I write the next actions section, I confirm [C-05/C-12/C-14/C-20/C-25]:
(1) Every action names the exact achievement it unlocks — not a vague goal. [C-05/C-12]
(2) Every action names the stagnation pattern it breaks, using a registry label. [C-12/C-14]
(3) No pattern label in this section was invented inline — every label is in the registry. [C-14]
(4) Gate label enumerates all covered IDs: C-05, C-12, C-14, C-20, C-25. [C-20/C-25]
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 7 — Cross-Topic Team Insight

Identify one insight that cannot be derived from any single topic view alone.

**INSIGHT GATE [C-10/C-13/C-22/C-24/C-25]**
Before I write the team insight, I confirm [C-10/C-13/C-22/C-24/C-25]:
(1) The insight requires synthesis of at least two topics or two contributors — it is NOT
    derivable from any single topic view alone. [C-10/C-22]
(2) The insight differs from any stagnation pattern statement or gap observation already made. [C-10]
(3) Insight is formatted as: **TEAM INSIGHT — [descriptive name]: [insight text]** [C-13]
(4) Did Phase 1's scan surface any cross-topic pattern that changes what this insight should say?
    If yes, update the insight before proceeding. [C-24]
(5) Gate label enumerates all covered IDs: C-10, C-13, C-22, C-24, C-25. [C-25]
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Structural Audit

**STRUCTURAL AUDIT GATE [C-26/C-27/C-34/C-36]**
Before I mark this skill complete, I confirm [C-26/C-27/C-34/C-36]:

(1) Every gate label in this skill carries at least one criterion ID reference: [C-26]
    - SCAN GATE [C-01/C-02/C-23] ✓
    - MILESTONE GATE [C-03/C-23] ✓
    - ATTRIBUTION INTEGRITY GATE [C-28/C-30] ✓
    - ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23] ✓
    - LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25] ✓
    - 1-AWAY GATE [C-09/C-18/C-23] ✓
    - ACTIONS GATE [C-05/C-12/C-14/C-20/C-25] ✓
    - INSIGHT GATE [C-10/C-13/C-22/C-24/C-25] ✓
    - STRUCTURAL AUDIT GATE [C-26/C-27/C-34/C-36] ✓

(2) Each multi-criterion cluster gate named by full label with exact expected criterion IDs: [C-27]
    - "SCAN GATE [C-01/C-02/C-23]" — expected: C-01, C-02, C-23
    - "MILESTONE GATE [C-03/C-23]" — expected: C-03, C-23
    - "ATTRIBUTION INTEGRITY GATE [C-28/C-30]" — expected: C-28, C-30
    - "ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23]" — expected: C-06, C-07, C-11, C-23
    - "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25]" — expected: C-16, C-19, C-21, C-25
    - "1-AWAY GATE [C-09/C-18/C-23]" — expected: C-09, C-18, C-23
    - "ACTIONS GATE [C-05/C-12/C-14/C-20/C-25]" — expected: C-05, C-12, C-14, C-20, C-25
    - "INSIGHT GATE [C-10/C-13/C-22/C-24/C-25]" — expected: C-10, C-13, C-22, C-24, C-25
    - "STRUCTURAL AUDIT GATE [C-26/C-27/C-34/C-36]" — expected: C-26, C-27, C-34, C-36

(3) Row count = 9. All 9 enumerated. [C-34/C-36]

If any sub-condition fails: apply RETRY PROTOCOL.

---

---

## V-02 — Axis: C-37/C-38 Preamble OUTPUT SCHEMAS + Phase-0 Attribution Gate

**Axis**: Two structural pre-execution declarations. First, a preamble OUTPUT SCHEMAS block
declares the schema for every major output section before any gate fires — making section
structure a persistent shared reference rather than a gate-embedded specification. Second, the
ATTRIBUTION INTEGRITY GATE moves to Phase 0 — before the artifact scan — so the contributor
list is committed as empty before any evidence exists to back-attribute from.

**Hypothesis**: When OUTPUT SCHEMAS are declared in the preamble, a model generating any section
can always consult the canonical schema rather than reconstructing it from a gate condition it may
have already passed. When the attribution gate fires at Phase 0 with an empty contributor list,
backward inference is architecturally impossible — there is nothing yet to back-attribute from,
not merely prohibited by instruction.

---

```
OUTPUT SCHEMAS [C-37]
──────────────────────────────────────────────────────
Declare the required schema for each major output section.
These schemas are canonical. Gate conditions reference them; they do not redefine them.

SCAN STATE schema:
  Topics: [list]  |  Namespaces: [list]  |  Contributors: [list]  |  Total signals: [n]

ACHIEVEMENTS TABLE schema:
  Topic | Category | Achievement Name | Status (✓ earned / ○ available)

LEADERBOARD TABLE schema:
  Rank | Contributor | Signals | Topics | Milestones | Score

1-AWAY TABLE schema:
  Topic/Target | Achievement to Unlock | Gap (What's Missing) | Exact Action Needed

NEXT ACTIONS schema:
  [Action] → Unlocks [Achievement] → Breaks [PATTERN_LABEL from registry]

TEAM INSIGHT schema:
  **TEAM INSIGHT — [descriptive name]: [insight text]**
──────────────────────────────────────────────────────

RETRY PROTOCOL [C-29/C-31/C-32/C-35]
══════════════════════════════════════
When any gate fails, execute in order:
Step 1 TRIAD: Emit — GATE FAILED [C-XX]: [specific instance] — CORRECTION: [action]. Re-running this section.
Step 2 DELIMIT: Wrap re-run in > RETRY [C-XX]: [instance] … > END RETRY [C-XX]
Step 3 CONTINUE: Proceed to next gate. Do not halt.
══════════════════════════════════════

STAGNATION PATTERN REGISTRY — see Shared Resources.
SCORING FORMULA — Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)
```

---

You are running `/corps-achievements` for the Signal plugin workspace.
Scan all signal artifacts, compute team-level achievements, and deliver a full achievement report.
Sprint anchor: use the most recent artifact date or the date in TOPICS.md.

**Execute Phase 0 before any artifact is read. Then execute phases 1–7 in order.**
On gate failure: apply RETRY PROTOCOL.

---

### Phase 0 — Attribution Pre-Commitment

Before scanning any artifact, commit to an empty contributor list.

```
ATTRIBUTION PRE-COMMITMENT:
  Contributors discovered so far: [empty — no artifacts scanned yet]
  Backward inference prohibited: any contributor added after this point must be
  traceable to a real artifact filename or frontmatter field from the Phase 1 scan.
```

**ATTRIBUTION INTEGRITY GATE [C-28/C-30]**
Before I scan any artifact, I confirm [C-28/C-30]:
(1) My contributor list is currently empty — I have not inferred any contributors from their
    known role, seniority, or prior project prominence. The list above reflects this commitment.
(2) I commit: no achievement or score will be attributed to any contributor not discovered
    in the Phase 1 artifact scan that follows.
If condition (1) fails: apply RETRY PROTOCOL — specify the contributor I have pre-loaded.
If condition (2) fails: apply RETRY PROTOCOL — specify the attribution that lacks scan basis.

---

### Phase 1 — Artifact Scan

Glob `simulations/**/*.md`. For each file, extract: topic path, namespace, skill, contributor,
and date. Add discovered contributors to the attribution pre-commitment list (Phase 0) only as
they appear in artifact metadata.

Build SCAN STATE using the preamble schema.

Cross-reference topics against TOPICS.md. Flag any topic in TOPICS.md with no matching artifacts
as `[ORPHAN_TOPIC from registry]`.

**SCAN GATE [C-01/C-02/C-23]**
Before I write the scan state, I confirm [C-01/C-02/C-23]:
(1) Every topic in my list is traceable to a real file from the glob — no hallucinated topics.
(2) Every discovered topic will appear in the achievements output section — none will be dropped.
(3) TOPICS.md topics with no artifacts are explicitly marked [ORPHAN_TOPIC from registry].
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 2 — Milestones

Evaluate which of the three team milestones are earned across the full workspace:
- **First Team Signal**: any contributor has filed any signal on any topic.
- **Shared Coverage**: at least two contributors have signals on the same topic.
- **Debate Starter**: at least two competing signals in the same topic+namespace pair.

Output sprint framing using C-08: "Sprint ending {date} — {N} topics tracked."

**MILESTONE GATE [C-03/C-23]**
Before I write the milestones section, I confirm [C-03/C-23]:
(1) "First Team Signal" appears by exact name in the output.
(2) "Shared Coverage" appears by exact name in the output.
(3) "Debate Starter" appears by exact name in the output.
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 3 — Achievement Census

For each topic, list earned (✓) and available (○) achievements using ACHIEVEMENTS TABLE schema.
Group under two named categories:
- **Category A — Individual Signals**: First Signal, Signal Depth (≥3), Full Sweep (≥3 namespaces)
- **Category B — Team Milestones**: First Team Signal, Shared Coverage, Debate Starter

**ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23]**
Before I write the achievements section, I confirm [C-06/C-07/C-11/C-23]:
(1) Earned (✓) and available (○) achievements are visually distinguished for every topic row.
(2) All achievements appear under a named category label — at least Category A and Category B.
(3) Self-test: will every next action I write name the exact achievement it unlocks?
    I commit: yes, I will enforce this in Phase 6.
(4) Gate label enumerates all covered IDs: C-06, C-07, C-11, C-23.
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 4 — Contributor Leaderboard

Using Phase 1 scan state (not prior knowledge), compute contributor scores per LEADERBOARD TABLE
schema and SCORING FORMULA.

Render worked example for Rank-1 inline above the table:
`Rank-1 calculation: Score = {S}×1 + {T}×3 + {M}×5 = {total}`

**LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25]**
Before I write the leaderboard table, I confirm [C-16/C-19/C-21/C-25]:
(1) Every row uses Score = Signals×1 + Topics×3 + Milestones×5. [C-16]
(2) Rank-1 worked example is rendered inline above the table. [C-19]
(3) If the worked example total ≠ Score column for Rank-1, I correct the table. [C-21]
(4) Gate label enumerates all covered IDs: C-16, C-19, C-21, C-25. [C-25]
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 5 — 1-Away Callouts

Identify every topic or contributor exactly one action away from unlocking an achievement.
Render using the 1-AWAY TABLE schema from the preamble OUTPUT SCHEMAS.

**1-AWAY GATE [C-09/C-18/C-23]**
Before I write the 1-away table, I confirm [C-09/C-18/C-23]:
(1) The 1-away section is standalone — not merged with next actions or achievements.
(2) Table uses the preamble 1-AWAY TABLE schema: all four columns present.
(3) Every row has all four columns populated — no blank cells, no merged prose.
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 6 — Next Actions

For each action, use the NEXT ACTIONS schema from the preamble OUTPUT SCHEMAS:
`[Action] → Unlocks [Achievement] → Breaks [PATTERN_LABEL from registry]`

**ACTIONS GATE [C-05/C-12/C-14/C-20/C-25]**
Before I write the next actions section, I confirm [C-05/C-12/C-14/C-20/C-25]:
(1) Every action names the exact achievement it unlocks. [C-05/C-12]
(2) Every action names the stagnation pattern it breaks, using a registry label. [C-12/C-14]
(3) No pattern label was invented inline — every label is in the registry. [C-14]
(4) Gate label enumerates all covered IDs: C-05, C-12, C-14, C-20, C-25. [C-20/C-25]
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 7 — Cross-Topic Team Insight

Identify one insight that cannot be derived from any single topic view alone.
Format using the TEAM INSIGHT schema from the preamble OUTPUT SCHEMAS.

**INSIGHT GATE [C-10/C-13/C-22/C-24/C-25]**
Before I write the team insight, I confirm [C-10/C-13/C-22/C-24/C-25]:
(1) The insight is NOT derivable from any single topic view alone. [C-10/C-22]
(2) The insight differs from any stagnation pattern or gap statement already made. [C-10]
(3) Insight uses the preamble TEAM INSIGHT schema: **TEAM INSIGHT — [name]: [text]** [C-13]
(4) Did Phase 1's scan surface any cross-topic pattern that changes this insight? Update if yes. [C-24]
(5) Gate label enumerates all covered IDs: C-10, C-13, C-22, C-24, C-25. [C-25]
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Structural Audit

**STRUCTURAL AUDIT GATE [C-26/C-27/C-34]**
Before I mark this skill complete, I confirm [C-26/C-27/C-34]:

(1) Every gate label carries at least one criterion ID: [C-26]
    ATTRIBUTION INTEGRITY GATE [C-28/C-30] ✓ | SCAN GATE [C-01/C-02/C-23] ✓
    MILESTONE GATE [C-03/C-23] ✓ | ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23] ✓
    LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25] ✓ | 1-AWAY GATE [C-09/C-18/C-23] ✓
    ACTIONS GATE [C-05/C-12/C-14/C-20/C-25] ✓ | INSIGHT GATE [C-10/C-13/C-22/C-24/C-25] ✓
    STRUCTURAL AUDIT GATE [C-26/C-27/C-34] ✓

(2) Each multi-criterion cluster gate named by full label with exact expected criterion IDs: [C-27]
    - "ATTRIBUTION INTEGRITY GATE [C-28/C-30]" — expected: C-28, C-30
    - "SCAN GATE [C-01/C-02/C-23]" — expected: C-01, C-02, C-23
    - "MILESTONE GATE [C-03/C-23]" — expected: C-03, C-23
    - "ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23]" — expected: C-06, C-07, C-11, C-23
    - "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25]" — expected: C-16, C-19, C-21, C-25
    - "1-AWAY GATE [C-09/C-18/C-23]" — expected: C-09, C-18, C-23
    - "ACTIONS GATE [C-05/C-12/C-14/C-20/C-25]" — expected: C-05, C-12, C-14, C-20, C-25
    - "INSIGHT GATE [C-10/C-13/C-22/C-24/C-25]" — expected: C-10, C-13, C-22, C-24, C-25
    - "STRUCTURAL AUDIT GATE [C-26/C-27/C-34]" — expected: C-26, C-27, C-34

(3) Enumeration covers all 9 cluster gates present in this skill (N=9, all N verified). [C-34]

If any sub-condition fails: apply RETRY PROTOCOL.

---

---

## V-03 — Axis: C-39/C-40 Phase Exit/Entry Contracts + Universal First-Person

**Axis**: Two framing upgrades applied pervasively across the skill. First, every phase boundary
carries an explicit EXIT CONTRACT (what this phase produced) and ENTRY CONTRACT (what the next
phase requires) — turning narrative continuations into typed handoff objects. Second, every
section header and phase opener uses first-person commitment framing ("I will now...", "I am
generating..."), extending C-28 ownership to every structural boundary.

**Hypothesis**: When phase transitions are named contracts, a model can verify it has satisfied
each entry requirement before proceeding — phase ordering errors become detectable failures, not
silent misexecutions. When first-person framing appears at every structural boundary, the model's
agency commitment is visible throughout the output, not only at gate confirmations.

---

```
RETRY PROTOCOL [C-29/C-31/C-32/C-35]
══════════════════════════════════════
When any gate fails, execute in order:
Step 1 TRIAD: Emit — GATE FAILED [C-XX]: [specific instance] — CORRECTION: [action]. Re-running this section.
Step 2 DELIMIT: Wrap re-run in > RETRY [C-XX]: [instance] … > END RETRY [C-XX]
Step 3 CONTINUE: Proceed to next gate. Do not halt.
══════════════════════════════════════

STAGNATION PATTERN REGISTRY — see Shared Resources.
SCORING FORMULA — Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)
```

---

You are running `/corps-achievements` for the Signal plugin workspace.
I will scan all signal artifacts, compute team-level achievements, and deliver a full achievement
report. Sprint anchor: use the most recent artifact date or the date in TOPICS.md.

I will execute phases in order. I will not begin a phase until its gate passes.
On gate failure: apply RETRY PROTOCOL.

---

### I will now perform the artifact scan — Phase 1

Glob `simulations/**/*.md`. For each file, I will extract: topic path, namespace, skill,
contributor, and date. I will build the SCAN STATE:

```
SCAN STATE:
  Topics: [list]     Namespaces: [list]     Contributors: [list]     Total signals: [n]
```

I will cross-reference topics against TOPICS.md and flag any unstarted topic as
`[ORPHAN_TOPIC from registry]`.

**SCAN GATE [C-01/C-02/C-23]**
Before I write the scan state, I confirm [C-01/C-02/C-23]:
(1) Every topic in my list is traceable to a real file from the glob — no hallucinated topics.
(2) Every discovered topic will appear in the achievements output section — none will be dropped.
(3) TOPICS.md topics with no artifacts are explicitly marked [ORPHAN_TOPIC from registry].
If any sub-condition fails: apply RETRY PROTOCOL.

```
EXIT CONTRACT — Phase 1:
  Produced: SCAN STATE with Topics=[list], Contributors=[list], Total signals=[n]
ENTRY CONTRACT — Phase 2 requires:
  SCAN STATE must be complete before milestone evaluation begins.
  Minimum: at least one topic discovered. If SCAN STATE is empty, halt and diagnose.
```

---

### I will now evaluate team milestones — Phase 2

I am evaluating which of the three named team milestones are earned:
- **First Team Signal**: any contributor has filed any signal on any topic.
- **Shared Coverage**: at least two contributors have signals on the same topic.
- **Debate Starter**: at least two competing signals in the same topic+namespace pair.

I will output sprint framing: "Sprint ending {date} — {N} topics tracked."

**MILESTONE GATE [C-03/C-23]**
Before I write the milestones section, I confirm [C-03/C-23]:
(1) "First Team Signal" appears by exact name in the output.
(2) "Shared Coverage" appears by exact name in the output.
(3) "Debate Starter" appears by exact name in the output.
If any sub-condition fails: apply RETRY PROTOCOL.

```
EXIT CONTRACT — Phase 2:
  Produced: milestone earn/gap table with all three named milestones evaluated.
ENTRY CONTRACT — ATTRIBUTION INTEGRITY GATE requires:
  Phase 1 SCAN STATE available. No contributor names may be cited before this gate passes.
```

---

### ATTRIBUTION INTEGRITY GATE [C-28/C-30]

Before I write any contributor-attributing section, I confirm [C-28/C-30]:
(1) Every contributor I am about to credit is traceable to a real artifact filename or
    frontmatter field from Phase 1 — no contributor was inferred from role or prominence.
(2) No achievement or score will be attributed to any contributor not in scan state.
If condition (1) fails: apply RETRY PROTOCOL — specify the contributor name not evidenced.
If condition (2) fails: apply RETRY PROTOCOL — specify the attribution that lacks artifact basis.

```
EXIT CONTRACT — Attribution Gate:
  Produced: confirmed contributor set = [Phase 1 contributors only, no additions]
ENTRY CONTRACT — Phase 3 requires:
  Attribution gate must have passed. Contributor set is now locked to Phase 1 discoveries.
```

---

### I am now generating the achievement census — Phase 3

For each topic, I will list earned (✓) and available (○) achievements.
I am grouping under two named categories:
- **Category A — Individual Signals**: First Signal, Signal Depth (≥3), Full Sweep (≥3 namespaces)
- **Category B — Team Milestones**: First Team Signal, Shared Coverage, Debate Starter

**ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23]**
Before I write the achievements section, I confirm [C-06/C-07/C-11/C-23]:
(1) Earned (✓) and available (○) achievements are visually distinguished for every topic row.
(2) All achievements appear under a named category label — at least Category A and Category B.
(3) Self-test: will every next action I write name the exact achievement it unlocks?
    I commit: yes, I will enforce this in Phase 6.
(4) Gate label enumerates all covered IDs: C-06, C-07, C-11, C-23.
If any sub-condition fails: apply RETRY PROTOCOL.

```
EXIT CONTRACT — Phase 3:
  Produced: achievement census per topic with earned/available distinguished, grouped by category.
ENTRY CONTRACT — Phase 4 requires:
  Achievement census complete. Contributor set locked from attribution gate.
  Did Phase 3 reveal any topics not in Phase 1 SCAN STATE? If yes, halt and reconcile.
```

---

### I am now computing the contributor leaderboard — Phase 4

Using Phase 1 scan state only, I am computing contributor scores.
Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

I will render a worked example for Rank-1 inline above the table:
`Rank-1 calculation: Score = {S}×1 + {T}×3 + {M}×5 = {total}`

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|

**LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25]**
Before I write the leaderboard table, I confirm [C-16/C-19/C-21/C-25]:
(1) Every row uses Score = Signals×1 + Topics×3 + Milestones×5. [C-16]
(2) Rank-1 worked example rendered inline above the table. [C-19]
(3) If worked example total ≠ Score column for Rank-1, I correct the table. [C-21]
(4) Gate label enumerates all covered IDs: C-16, C-19, C-21, C-25. [C-25]
If any sub-condition fails: apply RETRY PROTOCOL.

```
EXIT CONTRACT — Phase 4:
  Produced: leaderboard table with formula-computed scores, Rank-1 worked example verified.
ENTRY CONTRACT — Phase 5 requires:
  Achievement census (Phase 3) and leaderboard (Phase 4) complete.
  1-away analysis draws from both.
```

---

### I am now identifying 1-away callouts — Phase 5

I will identify every topic or contributor exactly one action away from unlocking an achievement.

| Topic/Target | Achievement to Unlock | Gap (What's Missing) | Exact Action Needed |
|---|---|---|---|

**1-AWAY GATE [C-09/C-18/C-23]**
Before I write the 1-away table, I confirm [C-09/C-18/C-23]:
(1) The 1-away section is standalone — not merged with next actions or achievements.
(2) Table has all four columns: Topic/Target, Achievement to Unlock, Gap, Exact Action Needed.
(3) Every row has all four columns populated — no blank cells, no merged prose.
If any sub-condition fails: apply RETRY PROTOCOL.

```
EXIT CONTRACT — Phase 5:
  Produced: 1-away table with all four columns populated for each near-unlock entry.
ENTRY CONTRACT — Phase 6 requires:
  1-away table available. Next actions should address 1-away entries before lower-priority gaps.
```

---

### I am now generating next actions — Phase 6

For each action, I will use anti-inertia format:
`[Action] → Unlocks [Achievement] → Breaks [PATTERN_LABEL from registry]`

**ACTIONS GATE [C-05/C-12/C-14/C-20/C-25]**
Before I write the next actions section, I confirm [C-05/C-12/C-14/C-20/C-25]:
(1) Every action names the exact achievement it unlocks. [C-05/C-12]
(2) Every action names the stagnation pattern it breaks, using a registry label. [C-12/C-14]
(3) No pattern label was invented inline — every label is in the registry. [C-14]
(4) Gate label enumerates all covered IDs: C-05, C-12, C-14, C-20, C-25. [C-20/C-25]
If any sub-condition fails: apply RETRY PROTOCOL.

```
EXIT CONTRACT — Phase 6:
  Produced: next actions in anti-inertia format, each with achievement and registry pattern.
ENTRY CONTRACT — Phase 7 requires:
  All prior phase outputs available for synthesis.
  The insight must draw on patterns not visible from any single phase output alone.
```

---

### I am now synthesizing the cross-topic team insight — Phase 7

I will identify one insight that cannot be derived from any single topic view alone.

**INSIGHT GATE [C-10/C-13/C-22/C-24/C-25]**
Before I write the team insight, I confirm [C-10/C-13/C-22/C-24/C-25]:
(1) The insight is NOT derivable from any single topic view alone. [C-10/C-22]
(2) The insight differs from any stagnation pattern or gap statement already made. [C-10]
(3) Insight formatted as: **TEAM INSIGHT — [descriptive name]: [insight text]** [C-13]
(4) Did Phase 1's scan surface any cross-topic pattern that changes this insight? Update if yes. [C-24]
(5) Gate label enumerates all covered IDs: C-10, C-13, C-22, C-24, C-25. [C-25]
If any sub-condition fails: apply RETRY PROTOCOL.

---

### I am now running the structural audit — Structural Audit

**STRUCTURAL AUDIT GATE [C-26/C-27/C-34]**
Before I mark this skill complete, I confirm [C-26/C-27/C-34]:

(1) Every gate label carries at least one criterion ID: [C-26]
    SCAN GATE [C-01/C-02/C-23] ✓ | MILESTONE GATE [C-03/C-23] ✓
    ATTRIBUTION INTEGRITY GATE [C-28/C-30] ✓ | ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23] ✓
    LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25] ✓ | 1-AWAY GATE [C-09/C-18/C-23] ✓
    ACTIONS GATE [C-05/C-12/C-14/C-20/C-25] ✓ | INSIGHT GATE [C-10/C-13/C-22/C-24/C-25] ✓
    STRUCTURAL AUDIT GATE [C-26/C-27/C-34] ✓

(2) Each multi-criterion cluster gate named by full label with exact expected criterion IDs: [C-27]
    - "SCAN GATE [C-01/C-02/C-23]" — expected: C-01, C-02, C-23
    - "MILESTONE GATE [C-03/C-23]" — expected: C-03, C-23
    - "ATTRIBUTION INTEGRITY GATE [C-28/C-30]" — expected: C-28, C-30
    - "ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23]" — expected: C-06, C-07, C-11, C-23
    - "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25]" — expected: C-16, C-19, C-21, C-25
    - "1-AWAY GATE [C-09/C-18/C-23]" — expected: C-09, C-18, C-23
    - "ACTIONS GATE [C-05/C-12/C-14/C-20/C-25]" — expected: C-05, C-12, C-14, C-20, C-25
    - "INSIGHT GATE [C-10/C-13/C-22/C-24/C-25]" — expected: C-10, C-13, C-22, C-24, C-25
    - "STRUCTURAL AUDIT GATE [C-26/C-27/C-34]" — expected: C-26, C-27, C-34

(3) Enumeration covers all 9 cluster gates present in this skill (N=9, all N verified). [C-34]

If any sub-condition fails: apply RETRY PROTOCOL.

---

---

## V-04 — Axis: C-37/C-38 + C-41 Combination (Preamble Schemas + Phase-0 Attribution + Pre-Evidence Hypothesis)

**Axis**: Combines three criteria that all share the same structural logic — declare commitments
before evidence is available. C-37 declares output schemas before gates fire. C-38 declares an
empty contributor list before Phase 1 scanning begins. C-41 states a candidate insight hypothesis
before consulting achievement evidence. Together they push all pre-commitment logic into the
preamble and Phase-0, so the model begins every evidential phase with declared constraints rather
than discovering them mid-execution.

**Hypothesis**: When the model must commit to schemas, contributor scope, and synthesis direction
before any evidence is read, the output becomes a test of whether evidence confirms or revises
pre-stated positions — every major section produces an observable delta between prediction and
finding. The insight in particular becomes genuinely falsifiable: a hypothesis declared before
evidence is available either survives the derivability test or is explicitly revised, and both
outcomes appear in the output.

---

```
OUTPUT SCHEMAS [C-37]
──────────────────────────────────────────────────────
SCAN STATE:   Topics | Namespaces | Contributors | Total signals
ACHIEVEMENTS: Topic | Category | Achievement Name | Status (✓ / ○)
LEADERBOARD:  Rank | Contributor | Signals | Topics | Milestones | Score
1-AWAY:       Topic/Target | Achievement to Unlock | Gap | Exact Action Needed
NEXT ACTIONS: [Action] → Unlocks [Achievement] → Breaks [PATTERN_LABEL from registry]
TEAM INSIGHT: **TEAM INSIGHT — [descriptive name]: [insight text]**
──────────────────────────────────────────────────────

HYPOTHESIS PRE-SCAN [C-41]
──────────────────────────────────────────────────────
Before consulting any achievement evidence, state a candidate synthesis hypothesis:
CANDIDATE INSIGHT: [write your tentative cross-topic insight claim here, before reviewing evidence]
This hypothesis will be confirmed or revised in Phase 7 after the single-topic-derivability test.
──────────────────────────────────────────────────────

RETRY PROTOCOL [C-29/C-31/C-32/C-35]
══════════════════════════════════════
When any gate fails, execute in order:
Step 1 TRIAD: Emit — GATE FAILED [C-XX]: [specific instance] — CORRECTION: [action]. Re-running this section.
Step 2 DELIMIT: Wrap re-run in > RETRY [C-XX]: [instance] … > END RETRY [C-XX]
Step 3 CONTINUE: Proceed to next gate. Do not halt.
══════════════════════════════════════

STAGNATION PATTERN REGISTRY — see Shared Resources.
SCORING FORMULA — Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)
```

---

You are running `/corps-achievements` for the Signal plugin workspace.
Scan all signal artifacts, compute team-level achievements, and deliver a full achievement report.
Sprint anchor: use the most recent artifact date or the date in TOPICS.md.

**Phase 0 executes before any artifact is read. Phases 1–7 execute in order.**
On gate failure: apply RETRY PROTOCOL.

---

### Phase 0 — Attribution Pre-Commitment

Before scanning any artifact, commit to an empty contributor list.

```
ATTRIBUTION PRE-COMMITMENT:
  Contributors at this point: [empty]
  No contributor may be added except from Phase 1 artifact metadata.
```

**ATTRIBUTION INTEGRITY GATE [C-28/C-30]**
Before I scan any artifact, I confirm [C-28/C-30]:
(1) My contributor list is currently empty — I have not pre-loaded any names from prior knowledge.
(2) I commit: every contributor credited in this report will come from Phase 1 artifact metadata.
If condition (1) fails: apply RETRY PROTOCOL — specify the contributor pre-loaded.

---

### Phase 1 — Artifact Scan

Glob `simulations/**/*.md`. Extract per-file: topic path, namespace, skill, contributor, date.
Build SCAN STATE (preamble schema). Populate contributor list from artifact metadata only.
Flag TOPICS.md topics with no artifacts as `[ORPHAN_TOPIC from registry]`.

**SCAN GATE [C-01/C-02/C-23]**
Before I write the scan state, I confirm [C-01/C-02/C-23]:
(1) Every topic traceable to a real file — no hallucinated topics.
(2) Every discovered topic will appear in achievements output.
(3) Unstarted TOPICS.md topics flagged [ORPHAN_TOPIC from registry].
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 2 — Milestones

Evaluate the three named team milestones. Output sprint framing: "Sprint ending {date} — {N} topics tracked."

**MILESTONE GATE [C-03/C-23]**
Before I write the milestones section, I confirm [C-03/C-23]:
(1) "First Team Signal" appears by exact name.
(2) "Shared Coverage" appears by exact name.
(3) "Debate Starter" appears by exact name.
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 3 — Achievement Census

For each topic, list earned (✓) and available (○) achievements using the preamble ACHIEVEMENTS
schema. Group under:
- **Category A — Individual Signals**: First Signal, Signal Depth (≥3), Full Sweep (≥3 namespaces)
- **Category B — Team Milestones**: First Team Signal, Shared Coverage, Debate Starter

**ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23]**
Before I write the achievements section, I confirm [C-06/C-07/C-11/C-23]:
(1) Earned (✓) and available (○) distinguished for every topic row.
(2) At least Category A and Category B labels present.
(3) Self-test: will every next action name the exact achievement it unlocks? I commit: yes.
(4) Gate label enumerates C-06, C-07, C-11, C-23.
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 4 — Contributor Leaderboard

Using Phase 1 scan state only. Render Rank-1 worked example inline above the table.
Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|

**LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25]**
Before I write the leaderboard, I confirm [C-16/C-19/C-21/C-25]:
(1) Every row uses the formula — no rank-ordered counts. [C-16]
(2) Rank-1 worked example rendered inline. [C-19]
(3) If worked example ≠ Score column, correct before continuing. [C-21]
(4) Gate label enumerates C-16, C-19, C-21, C-25. [C-25]
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 5 — 1-Away Callouts

Render as structured table using the preamble 1-AWAY schema.

| Topic/Target | Achievement to Unlock | Gap (What's Missing) | Exact Action Needed |
|---|---|---|---|

**1-AWAY GATE [C-09/C-18/C-23]**
Before I write the 1-away table, I confirm [C-09/C-18/C-23]:
(1) Section is standalone.
(2) All four columns present per preamble schema.
(3) Every row fully populated — no blank cells.
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 6 — Next Actions

Anti-inertia format using preamble NEXT ACTIONS schema:
`[Action] → Unlocks [Achievement] → Breaks [PATTERN_LABEL from registry]`

**ACTIONS GATE [C-05/C-12/C-14/C-20/C-25]**
Before I write next actions, I confirm [C-05/C-12/C-14/C-20/C-25]:
(1) Every action names the exact achievement it unlocks. [C-05/C-12]
(2) Every action names the stagnation pattern it breaks using a registry label. [C-12/C-14]
(3) No inline-invented labels. [C-14]
(4) Gate label enumerates C-05, C-12, C-14, C-20, C-25. [C-20/C-25]
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 7 — Cross-Topic Team Insight

Revisit the CANDIDATE INSIGHT declared in the preamble HYPOTHESIS PRE-SCAN.
Now consulting achievement evidence, apply the single-topic-derivability test.
State: "Confirmed: [insight]" or "Revised: [original hypothesis] → [updated insight] because [reason]."

Format the final insight using the preamble TEAM INSIGHT schema.

**INSIGHT GATE [C-10/C-13/C-22/C-24/C-25/C-41]**
Before I write the team insight, I confirm [C-10/C-13/C-22/C-24/C-25/C-41]:
(1) The insight is NOT derivable from any single topic view alone. [C-10/C-22]
(2) The insight differs from any stagnation pattern or gap observation already made. [C-10]
(3) Insight uses preamble TEAM INSIGHT schema. [C-13]
(4) Did Phase 1's scan change what this insight should say? Update if yes. [C-24]
(5) The preamble CANDIDATE INSIGHT was declared before consulting evidence, and I have
    explicitly confirmed or revised it after the derivability test above. [C-41]
(6) Gate label enumerates C-10, C-13, C-22, C-24, C-25, C-41. [C-25]
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Structural Audit

**STRUCTURAL AUDIT GATE [C-26/C-27/C-34]**
Before I mark this skill complete, I confirm [C-26/C-27/C-34]:

(1) Every gate label carries at least one criterion ID: [C-26]
    ATTRIBUTION INTEGRITY GATE [C-28/C-30] ✓ | SCAN GATE [C-01/C-02/C-23] ✓
    MILESTONE GATE [C-03/C-23] ✓ | ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23] ✓
    LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25] ✓ | 1-AWAY GATE [C-09/C-18/C-23] ✓
    ACTIONS GATE [C-05/C-12/C-14/C-20/C-25] ✓ | INSIGHT GATE [C-10/C-13/C-22/C-24/C-25/C-41] ✓
    STRUCTURAL AUDIT GATE [C-26/C-27/C-34] ✓

(2) Each multi-criterion cluster gate named by full label with exact expected criterion IDs: [C-27]
    - "ATTRIBUTION INTEGRITY GATE [C-28/C-30]" — expected: C-28, C-30
    - "SCAN GATE [C-01/C-02/C-23]" — expected: C-01, C-02, C-23
    - "MILESTONE GATE [C-03/C-23]" — expected: C-03, C-23
    - "ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23]" — expected: C-06, C-07, C-11, C-23
    - "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25]" — expected: C-16, C-19, C-21, C-25
    - "1-AWAY GATE [C-09/C-18/C-23]" — expected: C-09, C-18, C-23
    - "ACTIONS GATE [C-05/C-12/C-14/C-20/C-25]" — expected: C-05, C-12, C-14, C-20, C-25
    - "INSIGHT GATE [C-10/C-13/C-22/C-24/C-25/C-41]" — expected: C-10, C-13, C-22, C-24, C-25, C-41
    - "STRUCTURAL AUDIT GATE [C-26/C-27/C-34]" — expected: C-26, C-27, C-34

(3) Enumeration covers all 9 cluster gates present in this skill (N=9, all N verified). [C-34]

If any sub-condition fails: apply RETRY PROTOCOL.

---

---

## V-05 — Full Combination: All Seven v12 Criteria

**Axes combined**: C-35 (named retry step labels) + C-36 (row-count assertion) + C-37 (preamble
OUTPUT SCHEMAS) + C-38 (Phase-0 attribution gate) + C-39 (exit/entry contracts) + C-40 (universal
first-person) + C-41 (pre-evidence insight hypothesis).

**Hypothesis**: All seven v12 criteria share a single structural logic: commitments declared
before their violation becomes possible, not after. Schemas before gates (C-37), contributor scope
before scan (C-38), insight direction before evidence (C-41), step labels that make partial retry
diagnosable (C-35), count assertions that make completeness arithmetic (C-36), exit/entry contracts
that make phase ordering verifiable (C-39), first-person at every boundary that makes agency
traceable (C-40). When all seven are combined, the skill's entire execution becomes a sequence of
falsifiable pre-commitments — the model's predictions are visible, and every phase tests them.

---

```
OUTPUT SCHEMAS [C-37]
──────────────────────────────────────────────────────
Declare canonical schema for each major output section. All gates reference; none redefine.

SCAN STATE:   Topics: [list] | Namespaces: [list] | Contributors: [list] | Total signals: [n]
ACHIEVEMENTS: Topic | Category | Achievement Name | Status (✓ earned / ○ available)
LEADERBOARD:  Rank | Contributor | Signals | Topics | Milestones | Score
1-AWAY:       Topic/Target | Achievement to Unlock | Gap (What's Missing) | Exact Action Needed
NEXT ACTIONS: [Action] → Unlocks [Achievement] → Breaks [PATTERN_LABEL from registry]
TEAM INSIGHT: **TEAM INSIGHT — [descriptive name]: [insight text]**
──────────────────────────────────────────────────────

HYPOTHESIS PRE-SCAN [C-41]
──────────────────────────────────────────────────────
Before consulting any achievement evidence, state a candidate synthesis hypothesis:
CANDIDATE INSIGHT: [write tentative cross-topic insight here — before reviewing evidence]
This hypothesis will be confirmed or explicitly revised in Phase 7 after the derivability test.
──────────────────────────────────────────────────────

RETRY PROTOCOL [C-29/C-31/C-32/C-35]
═══════════════════════════════════════════════════════
This is the global retry protocol for all gates. Do not embed retry logic in any gate fail-path.
All gates reference this block by name only.

Step 1 TRIAD:
  Emit — GATE FAILED [C-XX]: [specific instance that triggered failure] — CORRECTION: [action to take]. Re-running this section.

Step 2 DELIMIT:
  Wrap the complete re-run output in labeled delimiters:
  > RETRY [C-XX]: [specific instance]
  [re-run output — complete section, not summary]
  > END RETRY [C-XX]

Step 3 CONTINUE:
  Proceed to the next gate. Do not halt permanently.
═══════════════════════════════════════════════════════

STAGNATION PATTERN REGISTRY — see Shared Resources above.
SCORING FORMULA: Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)
```

---

I am running `/corps-achievements` for the Signal plugin workspace.
I will scan all signal artifacts, compute team-level achievements, and deliver a full achievement
report. Sprint anchor: I will use the most recent artifact date or the date in TOPICS.md.

I will execute Phase 0 before any artifact is read. I will then execute phases 1–7 in order.
I will not begin a phase until its gate passes. On gate failure: apply RETRY PROTOCOL.

---

### Phase 0 — I am declaring attribution pre-commitment

Before I scan any artifact, I commit to an empty contributor list.

```
ATTRIBUTION PRE-COMMITMENT:
  Contributors at this point: [empty — no artifacts scanned]
  I commit: no contributor will be added except from Phase 1 artifact metadata.
```

**ATTRIBUTION INTEGRITY GATE [C-28/C-30]**
Before I scan any artifact, I confirm [C-28/C-30]:
(1) My contributor list is currently empty — I have not pre-loaded any names from prior knowledge
    of roles, seniority, or project prominence.
(2) I commit: every contributor credited in this report will be discovered from Phase 1 artifact
    metadata — backward inference from identity is architecturally blocked by this empty list.
If condition (1) fails: apply RETRY PROTOCOL — name the contributor I have pre-loaded.
If condition (2) fails: apply RETRY PROTOCOL — name the attribution lacking scan basis.

```
EXIT CONTRACT — Phase 0:
  Produced: attribution pre-commitment with empty contributor list.
ENTRY CONTRACT — Phase 1 requires:
  Attribution pre-commitment must be in place before any artifact is read.
```

---

### Phase 1 — I will now perform the artifact scan

I am globbing `simulations/**/*.md`. For each file, I will extract: topic path, namespace, skill,
contributor, and date. I will populate the contributor list from artifact metadata only.

I will build SCAN STATE using the preamble OUTPUT SCHEMAS:
```
SCAN STATE:
  Topics: [list]     Namespaces: [list]     Contributors: [list]     Total signals: [n]
```

I will cross-reference topics against TOPICS.md and flag unstarted topics as
`[ORPHAN_TOPIC from registry]`.

**SCAN GATE [C-01/C-02/C-23]**
Before I write the scan state, I confirm [C-01/C-02/C-23]:
(1) Every topic in my list is traceable to a real file from the glob — no hallucinated topics.
(2) Every discovered topic will appear in the achievements output section — none will be dropped.
(3) TOPICS.md topics with no artifacts are explicitly marked [ORPHAN_TOPIC from registry].
If any sub-condition fails: apply RETRY PROTOCOL.

```
EXIT CONTRACT — Phase 1:
  Produced: SCAN STATE with Topics=[list], Contributors=[list], Total signals=[n].
ENTRY CONTRACT — Phase 2 requires:
  SCAN STATE complete. At least one topic discovered. Contributor list populated from metadata.
```

---

### Phase 2 — I will now evaluate team milestones

I am evaluating which of the three named team milestones are earned:
- **First Team Signal**: any contributor has filed any signal on any topic.
- **Shared Coverage**: at least two contributors have signals on the same topic.
- **Debate Starter**: at least two competing signals in the same topic+namespace pair.

I will output sprint framing: "Sprint ending {date} — {N} topics tracked."

**MILESTONE GATE [C-03/C-23]**
Before I write the milestones section, I confirm [C-03/C-23]:
(1) "First Team Signal" appears by exact name in the output.
(2) "Shared Coverage" appears by exact name in the output.
(3) "Debate Starter" appears by exact name in the output.
If any sub-condition fails: apply RETRY PROTOCOL.

```
EXIT CONTRACT — Phase 2:
  Produced: milestone earn/gap evaluation for all three named milestones.
ENTRY CONTRACT — Phase 3 requires:
  Phase 1 SCAN STATE available. Attribution pre-commitment (Phase 0) in force.
  Did Phase 2 milestone analysis surface any topics not in Phase 1 SCAN STATE? Reconcile if yes.
```

---

### Phase 3 — I am now generating the achievement census

For each topic, I will list earned (✓) and available (○) achievements using the preamble
ACHIEVEMENTS schema. I am grouping under two named categories:
- **Category A — Individual Signals**: First Signal, Signal Depth (≥3), Full Sweep (≥3 namespaces)
- **Category B — Team Milestones**: First Team Signal, Shared Coverage, Debate Starter

**ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23]**
Before I write the achievements section, I confirm [C-06/C-07/C-11/C-23]:
(1) Earned (✓) and available (○) achievements visually distinguished for every topic row.
(2) All achievements appear under a named category label — at least Category A and Category B.
(3) Self-test: will every next action I write name the exact achievement it unlocks?
    I commit: yes, I will enforce this in Phase 6 before writing any action row.
(4) Gate label enumerates all covered IDs: C-06, C-07, C-11, C-23.
If any sub-condition fails: apply RETRY PROTOCOL.

```
EXIT CONTRACT — Phase 3:
  Produced: per-topic achievement census, earned/available distinguished, grouped by category.
ENTRY CONTRACT — Phase 4 requires:
  Achievement census complete. Contributor list locked to Phase 0/1 discoveries.
```

---

### Phase 4 — I am now computing the contributor leaderboard

Using Phase 1 scan state only (attribution pre-commitment locks the contributor set), I am
computing contributor scores per the preamble LEADERBOARD schema and SCORING FORMULA.

I will render a worked example for Rank-1 inline above the table:
`Rank-1 calculation: Score = {S}×1 + {T}×3 + {M}×5 = {total}`

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|

**LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25]**
Before I write the leaderboard table, I confirm [C-16/C-19/C-21/C-25]:
(1) Every row uses Score = Signals×1 + Topics×3 + Milestones×5 — no rank-ordered counts. [C-16]
(2) Rank-1 worked example is rendered inline above the table. [C-19]
(3) If the worked example total ≠ Score column for Rank-1, I correct the table before proceeding. [C-21]
(4) Gate label enumerates all covered IDs: C-16, C-19, C-21, C-25. [C-25]
If any sub-condition fails: apply RETRY PROTOCOL.

```
EXIT CONTRACT — Phase 4:
  Produced: leaderboard table with formula-computed scores, Rank-1 worked example verified.
ENTRY CONTRACT — Phase 5 requires:
  Achievement census (Phase 3) and leaderboard (Phase 4) complete.
```

---

### Phase 5 — I am now identifying 1-away callouts

I will identify every topic or contributor exactly one action away from unlocking an achievement.
I will render using the preamble 1-AWAY schema:

| Topic/Target | Achievement to Unlock | Gap (What's Missing) | Exact Action Needed |
|---|---|---|---|

**1-AWAY GATE [C-09/C-18/C-23]**
Before I write the 1-away table, I confirm [C-09/C-18/C-23]:
(1) The 1-away section is standalone — not merged with next actions or achievements.
(2) Table uses the preamble 1-AWAY schema: all four columns present.
(3) Every row has all four columns populated — no blank cells, no merged prose.
If any sub-condition fails: apply RETRY PROTOCOL.

```
EXIT CONTRACT — Phase 5:
  Produced: 1-away table with all four columns fully populated.
ENTRY CONTRACT — Phase 6 requires:
  1-away table available. Next actions should address near-unlock entries first.
```

---

### Phase 6 — I am now generating next actions

I will use the preamble NEXT ACTIONS schema:
`[Action] → Unlocks [Achievement] → Breaks [PATTERN_LABEL from registry]`

All pattern labels must come from the Stagnation Pattern Registry. No inline invented labels.

**ACTIONS GATE [C-05/C-12/C-14/C-20/C-25]**
Before I write the next actions section, I confirm [C-05/C-12/C-14/C-20/C-25]:
(1) Every action names the exact achievement it unlocks — not a vague goal. [C-05/C-12]
(2) Every action names the stagnation pattern it breaks, using a registry label. [C-12/C-14]
(3) No pattern label in this section was invented inline — every label is in the registry. [C-14]
(4) Gate label enumerates all covered IDs: C-05, C-12, C-14, C-20, C-25. [C-20/C-25]
If any sub-condition fails: apply RETRY PROTOCOL.

```
EXIT CONTRACT — Phase 6:
  Produced: next actions in anti-inertia format, each with achievement and registry pattern label.
ENTRY CONTRACT — Phase 7 requires:
  All prior phase outputs available for synthesis.
  The CANDIDATE INSIGHT declared in the preamble HYPOTHESIS PRE-SCAN must be revisited now.
```

---

### Phase 7 — I am now synthesizing the cross-topic team insight

I will revisit the CANDIDATE INSIGHT declared in the preamble HYPOTHESIS PRE-SCAN.
I will now consult achievement evidence and apply the single-topic-derivability test.

I will state: "Confirmed: [insight remains as hypothesized]" or
"Revised: [original hypothesis] → [updated insight] because [evidence delta]."

I will format the final insight per the preamble TEAM INSIGHT schema.

**INSIGHT GATE [C-10/C-13/C-22/C-24/C-25/C-41]**
Before I write the team insight, I confirm [C-10/C-13/C-22/C-24/C-25/C-41]:
(1) The insight is NOT derivable from any single topic view alone. [C-10/C-22]
(2) The insight differs from any stagnation pattern or gap statement already made. [C-10]
(3) Insight uses the preamble TEAM INSIGHT schema: **TEAM INSIGHT — [name]: [text]** [C-13]
(4) Did Phase 1's scan surface any cross-topic pattern that changes this insight? Update if yes. [C-24]
(5) The preamble CANDIDATE INSIGHT was declared before consulting evidence, and I have
    explicitly confirmed or revised it here after the derivability test. [C-41]
(6) Gate label enumerates all covered IDs: C-10, C-13, C-22, C-24, C-25, C-41. [C-25]
If any sub-condition fails: apply RETRY PROTOCOL.

---

### I am now running the structural audit

**STRUCTURAL AUDIT GATE [C-26/C-27/C-34/C-36]**
Before I mark this skill complete, I confirm [C-26/C-27/C-34/C-36]:

(1) Every gate label in this skill carries at least one criterion ID reference: [C-26]
    - ATTRIBUTION INTEGRITY GATE [C-28/C-30] ✓
    - SCAN GATE [C-01/C-02/C-23] ✓
    - MILESTONE GATE [C-03/C-23] ✓
    - ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23] ✓
    - LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25] ✓
    - 1-AWAY GATE [C-09/C-18/C-23] ✓
    - ACTIONS GATE [C-05/C-12/C-14/C-20/C-25] ✓
    - INSIGHT GATE [C-10/C-13/C-22/C-24/C-25/C-41] ✓
    - STRUCTURAL AUDIT GATE [C-26/C-27/C-34/C-36] ✓

(2) Each multi-criterion cluster gate named by full label with exact expected criterion IDs: [C-27]
    - "ATTRIBUTION INTEGRITY GATE [C-28/C-30]" — expected: C-28, C-30
    - "SCAN GATE [C-01/C-02/C-23]" — expected: C-01, C-02, C-23
    - "MILESTONE GATE [C-03/C-23]" — expected: C-03, C-23
    - "ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23]" — expected: C-06, C-07, C-11, C-23
    - "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25]" — expected: C-16, C-19, C-21, C-25
    - "1-AWAY GATE [C-09/C-18/C-23]" — expected: C-09, C-18, C-23
    - "ACTIONS GATE [C-05/C-12/C-14/C-20/C-25]" — expected: C-05, C-12, C-14, C-20, C-25
    - "INSIGHT GATE [C-10/C-13/C-22/C-24/C-25/C-41]" — expected: C-10, C-13, C-22, C-24, C-25, C-41
    - "STRUCTURAL AUDIT GATE [C-26/C-27/C-34/C-36]" — expected: C-26, C-27, C-34, C-36

(3) Row count = 9. All 9 enumerated. [C-34/C-36]

If any sub-condition fails: apply RETRY PROTOCOL.

---

## R13 Criteria Coverage Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-35 (named retry step labels: TRIAD/DELIMIT/CONTINUE) | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-36 (row-count assertion in structural audit) | ✓ | — | — | — | ✓ |
| C-37 (preamble OUTPUT SCHEMAS) | — | ✓ | — | ✓ | ✓ |
| C-38 (attribution gate before Phase 1 scan) | — | ✓ | — | ✓ | ✓ |
| C-39 (exit/entry contracts at phase boundaries) | — | — | ✓ | — | ✓ |
| C-40 (universal first-person at all headers) | — | — | ✓ | — | ✓ |
| C-41 (pre-evidence insight hypothesis) | — | — | — | ✓ | ✓ |
| All prior v11 criteria (C-29–C-34) | ✓ | ✓ | ✓ | ✓ | ✓ |
| All prior v10 criteria (C-28, C-30) | ✓ | ✓ | ✓ | ✓ | ✓ |

Note: All variations carry C-35 (named step labels) as the minimum upgrade from R12. V-05 is the
full-combination target. V-01 is the minimal upgrade — just steps + row count. V-02 and V-03 each
isolate one independent axis pair. V-04 combines the two axes that share the "pre-evidence
commitment" structural pattern.
