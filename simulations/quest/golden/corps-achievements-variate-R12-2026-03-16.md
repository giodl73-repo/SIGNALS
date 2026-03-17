---
skill: quest-variate
skill_target: corps-achievements
round: 12
date: 2026-03-16
rubric_version: 11
basis: R11 V-01/V-04 scored highest on v10 but failed C-31 (per-gate retry, not global), V-01/V-05
       failed C-33 (attribution as inline sub-step/pre-check, not standalone gate), V-01/V-02/V-03/V-05
       failed C-34 (partial structural audit enumeration). R12 targets all four v11 upgrades.
---

# Variate R12 — corps-achievements

5 complete prompt body variations for the `corps-achievements` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

v11 introduced four changes from v10:

- **C-31 (new)**: Retry instructions declared as a single named global retry protocol block in
  the preamble — all gates reference it. Per-gate retry embedding (even complete) does not satisfy.

- **C-32 (new)**: Retry output wrapped in labeled open/close delimiters —
  `> RETRY [C-XX]: [instance]` / `> END RETRY [C-XX]` — making the retry boundary parseable.
  Correcting without delimiting does not satisfy.

- **C-33 (new)**: The C-30 backward-inference prohibition is a standalone named gate
  (`ATTRIBUTION INTEGRITY GATE [C-28/C-30]`) executing before the leaderboard cluster gate —
  not a sub-step of another gate, not an inline pre-check. Structural independence required.

- **C-34 (new)**: The structural audit gate enumerates every multi-criterion cluster gate in
  the skill — if N super-gates exist, all N appear. Partial enumeration, even accurate, fails.

R11's best performer was V-04 (global RETRY blocks + standalone attribution gate + 4-gate audit).
R12 carries that foundation and explores five axes for implementing all four new criteria cleanly,
with the structural audit now required to enumerate all 9 cluster gates.

---

## Gate Catalog (all 9 cluster gates — all variations reference this set)

Every variation uses this gate set. Phase order and phrasing vary by axis.
The structural audit must enumerate all 9 (C-34).

| Gate | Criterion IDs | C-33 constraint |
|------|--------------|-----------------|
| SCAN GATE | [C-01/C-02/C-23] | — |
| MILESTONE GATE | [C-03/C-23] | — |
| ATTRIBUTION INTEGRITY GATE | [C-28/C-30] | Standalone, before leaderboard |
| ACHIEVEMENT CLUSTER GATE | [C-06/C-07/C-11/C-23] | — |
| LEADERBOARD CLUSTER GATE | [C-16/C-19/C-21/C-25] | After attribution gate |
| 1-AWAY GATE | [C-09/C-18/C-23] | — |
| ACTIONS GATE | [C-05/C-12/C-14/C-20/C-25] | — |
| INSIGHT GATE | [C-10/C-13/C-22/C-24/C-25] | — |
| STRUCTURAL AUDIT GATE | [C-26/C-27/C-34] | — |

---

## Variation Axes Selected

| Axis | Hypothesis | Used In |
|------|------------|---------|
| C-31/C-32 as named protocol module | Declaring RETRY PROTOCOL as a named, versioned module block (with module-header syntax) makes the global contract visually distinct from gate body text — preventing per-gate drift even across many gates | V-01, V-04 |
| C-33 via Phase-0 attribution | Running the ATTRIBUTION INTEGRITY GATE as Phase 0 — before any artifact is scanned — forces the strictest possible form of C-30: no evidence yet exists to back-attribute from, so contributor list is explicitly empty until scan supplies it | V-02, V-04 |
| C-34 via tabular audit | Rendering the structural audit as a compliance table (Gate Label | Expected IDs | Verified Y/N) makes N-completeness auditable at a glance vs. reading a prose enumeration | V-03, V-05 |
| C-28 pervasive ownership + insight-first | Pre-committing to a synthesis hypothesis before scanning (insight-first) + first-person ownership at every output section forces the model to maintain a synthesis goal throughout execution rather than discovering it at the end | V-04 |
| Stagnation-first output + compact table schemas | Declaring all output schemas in the preamble and leading with a stagnation risk dashboard (before achievements) shifts the model's default from trophy-case to risk-register — inertia framing as structural emphasis | V-05 |

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

## V-01 — Axis: C-31/C-32 Global Protocol Architecture

**Axis**: Retry protocol declared as a standalone named module block in the preamble,
using module-header syntax that visually distinguishes the protocol from gate body text.
All gate fail-paths reference the protocol by name — they do not repeat its content.

**Hypothesis**: When the RETRY PROTOCOL is a named module (not inline instructions), per-gate
drift becomes structurally impossible — a gate can only say "apply RETRY PROTOCOL" rather than
embedding its own variant. The delimiter format (C-32) is declared once in the module; no gate
needs to restate it.

---

```
═══════════════════════════════════════════════════════
RETRY PROTOCOL [C-29/C-31/C-32]
═══════════════════════════════════════════════════════
This is the global retry protocol for all gates in this skill.
Do not embed separate retry instructions in any gate fail-path.
All gates reference this block by name only.

When any gate fails:

Step 1 — Emit the named correction triad:
  GATE FAILED [C-XX]: [specific instance that triggered failure] — CORRECTION: [action to take]. Re-running this section.

Step 2 — Wrap the re-run output in labeled delimiters:
  > RETRY [C-XX]: [specific instance]
  [re-run output here — complete section, not summary]
  > END RETRY [C-XX]

Step 3 — Continue to the next gate. Do not halt permanently.
═══════════════════════════════════════════════════════

STAGNATION PATTERN REGISTRY
[See shared resources above]

SCORING FORMULA
Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)
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

Cross-reference topics against TOPICS.md. Flag any topic in TOPICS.md with no matching
artifacts as `[ORPHAN_TOPIC from registry]`.

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

**STRUCTURAL AUDIT GATE [C-26/C-27/C-34]**
Before I mark this skill complete, I confirm [C-26/C-27/C-34]:

(1) Every gate label in this skill carries at least one criterion ID reference:
    - SCAN GATE [C-01/C-02/C-23] ✓
    - MILESTONE GATE [C-03/C-23] ✓
    - ATTRIBUTION INTEGRITY GATE [C-28/C-30] ✓
    - ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23] ✓
    - LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25] ✓
    - 1-AWAY GATE [C-09/C-18/C-23] ✓
    - ACTIONS GATE [C-05/C-12/C-14/C-20/C-25] ✓
    - INSIGHT GATE [C-10/C-13/C-22/C-24/C-25] ✓
    - STRUCTURAL AUDIT GATE [C-26/C-27/C-34] ✓

(2) Each multi-criterion cluster gate named by full label with exact expected criterion IDs:
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

If any gate label is missing criterion IDs: apply RETRY PROTOCOL — name the gate.
If enumeration is missing any cluster gate: apply RETRY PROTOCOL — name the missing gate.

---

---

## V-02 — Axis: C-33 via Phase-0 Attribution

**Axis**: The ATTRIBUTION INTEGRITY GATE runs as Phase 0 — before any artifact is scanned.
At Phase 0, the contributor list is explicitly empty; the gate confirms it and commits to
deriving it from scan evidence only. The scan populates it; the gate seals the derivation rule
before any data exists to violate it.

**Hypothesis**: Running the attribution gate before the scan — when no evidence yet exists —
is the strongest possible form of C-30. It is impossible to back-attribute from scan findings
you have not yet seen. The standalone positioning (C-33) is architecturally guaranteed, not
merely instructed.

---

```
═══════════════════════════════════════════════════════
RETRY PROTOCOL [C-29/C-31/C-32]
═══════════════════════════════════════════════════════
Global retry for all gates. Do not embed retry logic in any gate.

On failure:
  GATE FAILED [C-XX]: [specific instance] — CORRECTION: [action]. Re-running this section.
  > RETRY [C-XX]: [specific instance]
  [re-run output — complete, not summarized]
  > END RETRY [C-XX]

Continue after retry. Do not halt permanently.
═══════════════════════════════════════════════════════

STAGNATION PATTERN REGISTRY
[SOLO_ISLAND | NAMESPACE_MOAT | SPRINT_FREEZE | SHALLOW_POOL | ORPHAN_TOPIC]
Use [PATTERN_LABEL from registry] syntax. Do not invent labels.

SCORING FORMULA: Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)
```

---

You are running `/corps-achievements` for the Signal plugin workspace.
Sprint anchor: most recent artifact date or TOPICS.md date.
Execute phases in order. Gate failure → apply RETRY PROTOCOL.

---

### Phase 0 — Attribution Commitment (Pre-Scan)

Before any file is read, commit to the derivation rule for contributor attribution.
The contributor list is currently empty: [ ].

**ATTRIBUTION INTEGRITY GATE [C-28/C-30]**
Before I scan any file, I confirm [C-28/C-30]:
(1) The contributor list is empty at this moment — no contributors have been identified yet.
(2) I commit: every contributor I will name in any section of this output will be derived
    exclusively from Phase 1 artifact filenames or frontmatter fields — never inferred from
    their known role, seniority, or prior project prominence.
(3) If I notice myself assigning a contributor from memory rather than file evidence during
    any later phase, I will stop, emit the correction triad, and re-derive from artifacts only.
If either commitment cannot be stated: apply RETRY PROTOCOL before proceeding to Phase 1.

---

### Phase 1 — Artifact Scan

Glob `simulations/**/*.md`. Extract topic path, namespace, contributor, date per file.
Populate contributor list from frontmatter only — this is the evidence base committed to in Phase 0.

```
SCAN STATE:
  Topics: [list]   Namespaces: [list]   Contributors: [list]   Total signals: [n]
```

Flag TOPICS.md entries with no artifacts as `[ORPHAN_TOPIC from registry]`.

**SCAN GATE [C-01/C-02/C-23]**
Before I finalize the scan state, I confirm [C-01/C-02/C-23]:
(1) Every topic listed is traceable to a real file from the glob — no hallucinated topics.
(2) Every discovered topic will appear in the achievements output — none will be silently dropped.
(3) TOPICS.md entries with no matching artifacts are flagged [ORPHAN_TOPIC from registry].
If any sub-condition fails: apply RETRY PROTOCOL — name the specific topic that failed.

---

### Phase 2 — Milestones

Evaluate team milestones: First Team Signal, Shared Coverage, Debate Starter.
Sprint framing: "Sprint ending {date} — {N} topics tracked."

**MILESTONE GATE [C-03/C-23]**
Before I write the milestones section, I confirm [C-03/C-23]:
(1) "First Team Signal" appears by exact name.
(2) "Shared Coverage" appears by exact name.
(3) "Debate Starter" appears by exact name.
If any sub-condition fails: apply RETRY PROTOCOL — name the specific milestone string missing.

---

### Phase 3 — Achievement Census

For each topic, list earned (✓) and available (○) achievements.
Categories: **Category A — Individual Signals** | **Category B — Team Milestones**

**ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23]**
Before I write the achievements section, I confirm [C-06/C-07/C-11/C-23]:
(1) Earned and available achievements are visually separated (✓ vs ○) for every topic.
(2) Achievements appear under at least two named category labels.
(3) Pre-write self-test: will every next action I write name the exact achievement it unlocks?
    Confirmed — I will enforce this in Phase 5.
(4) Gate label enumerates: C-06, C-07, C-11, C-23.
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 4 — Contributor Leaderboard

Contributors derived from Phase 1 scan state (Phase 0 commitment applies).
Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

Rank-1 worked example inline above table:
`Rank-1 calculation: Score = {S}×1 + {T}×3 + {M}×5 = {total}`

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|

**LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25]**
Before I write the leaderboard, I confirm [C-16/C-19/C-21/C-25]:
(1) Every row uses Score = Signals×1 + Topics×3 + Milestones×5. [C-16]
(2) Rank-1 worked example rendered inline above the table. [C-19]
(3) If worked example total ≠ Score column for Rank-1: correct before continuing. [C-21]
(4) Gate label enumerates: C-16, C-19, C-21, C-25. [C-25]
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 5 — 1-Away Callouts

| Topic/Target | Achievement to Unlock | Gap (What's Missing) | Exact Action Needed |
|---|---|---|---|

**1-AWAY GATE [C-09/C-18/C-23]**
Before I write the 1-away table, I confirm [C-09/C-18/C-23]:
(1) Section is standalone — not merged with next actions or achievements.
(2) Table has all four required columns.
(3) Every row has all four columns populated — no blank cells.
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 6 — Next Actions

Format: `[Action] → Unlocks [Achievement] → Breaks [PATTERN_LABEL from registry]`

**ACTIONS GATE [C-05/C-12/C-14/C-20/C-25]**
Before I write the next actions section, I confirm [C-05/C-12/C-14/C-20/C-25]:
(1) Every action names the exact achievement it unlocks. [C-05/C-12]
(2) Every action names a stagnation pattern from the registry using label syntax. [C-12/C-14]
(3) No label was invented inline — every label exists in the registry. [C-14]
(4) Gate label enumerates: C-05, C-12, C-14, C-20, C-25. [C-20/C-25]
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 7 — Cross-Topic Team Insight

**INSIGHT GATE [C-10/C-13/C-22/C-24/C-25]**
Before I write the team insight, I confirm [C-10/C-13/C-22/C-24/C-25]:
(1) Insight cannot be derived from any single topic view alone — cross-topic synthesis required. [C-22]
(2) Insight differs from any stagnation pattern or gap statement already in the output. [C-10]
(3) Formatted as: **TEAM INSIGHT — [descriptive name]: [insight text]** [C-13]
(4) Did Phase 1's scan surface any pattern that changes this insight? Update if yes. [C-24]
(5) Gate label enumerates: C-10, C-13, C-22, C-24, C-25. [C-25]
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Structural Audit

**STRUCTURAL AUDIT GATE [C-26/C-27/C-34]**
Before I mark this skill complete, I confirm [C-26/C-27/C-34]:

(1) Every gate label carries criterion ID references — verified:
    - ATTRIBUTION INTEGRITY GATE [C-28/C-30] ✓
    - SCAN GATE [C-01/C-02/C-23] ✓
    - MILESTONE GATE [C-03/C-23] ✓
    - ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23] ✓
    - LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25] ✓
    - 1-AWAY GATE [C-09/C-18/C-23] ✓
    - ACTIONS GATE [C-05/C-12/C-14/C-20/C-25] ✓
    - INSIGHT GATE [C-10/C-13/C-22/C-24/C-25] ✓
    - STRUCTURAL AUDIT GATE [C-26/C-27/C-34] ✓

(2) Each super-gate named by full label with exact expected IDs — all 9 verified. [C-27/C-34]
    - "ATTRIBUTION INTEGRITY GATE [C-28/C-30]" — expected: C-28, C-30
    - "SCAN GATE [C-01/C-02/C-23]" — expected: C-01, C-02, C-23
    - "MILESTONE GATE [C-03/C-23]" — expected: C-03, C-23
    - "ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23]" — expected: C-06, C-07, C-11, C-23
    - "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25]" — expected: C-16, C-19, C-21, C-25
    - "1-AWAY GATE [C-09/C-18/C-23]" — expected: C-09, C-18, C-23
    - "ACTIONS GATE [C-05/C-12/C-14/C-20/C-25]" — expected: C-05, C-12, C-14, C-20, C-25
    - "INSIGHT GATE [C-10/C-13/C-22/C-24/C-25]" — expected: C-10, C-13, C-22, C-24, C-25
    - "STRUCTURAL AUDIT GATE [C-26/C-27/C-34]" — expected: C-26, C-27, C-34

(3) N=9 cluster gates present. All 9 enumerated above. [C-34]

If any gate is missing criterion IDs: apply RETRY PROTOCOL.
If enumeration misses any cluster gate: apply RETRY PROTOCOL.

---

---

## V-03 — Axis: Lifecycle Emphasis (Phase Entry/Exit Contracts)

**Axis**: Each phase declares an explicit ENTER contract (what it receives) and EXIT contract
(what it produces and hands off). Gates are integrated into the EXIT contract, not floated after
the content. Phase transitions include a one-line handoff confirmation.

**Hypothesis**: Declaring what each phase receives and produces forces the model to treat the
gate as part of the phase boundary rather than an afterthought. Cross-phase contamination
(a later phase reaching back to reinterpret earlier evidence) is blocked by the explicit
handoff object — the next phase gets a named object, not raw context.

---

```
═══════════════════════════════════════════════════════
RETRY PROTOCOL [C-29/C-31/C-32]
═══════════════════════════════════════════════════════
Global. All gates reference this block. Do not repeat in gate fail-paths.

On failure:
  GATE FAILED [C-XX]: [specific instance] — CORRECTION: [action]. Re-running this section.
  > RETRY [C-XX]: [specific instance]
  [re-run output]
  > END RETRY [C-XX]
═══════════════════════════════════════════════════════

STAGNATION PATTERN REGISTRY
[SOLO_ISLAND | NAMESPACE_MOAT | SPRINT_FREEZE | SHALLOW_POOL | ORPHAN_TOPIC]
Syntax: [PATTERN_LABEL from registry]. No inline invention.

SCORING FORMULA: Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)
```

---

You are running `/corps-achievements`. Execute all phases in sequence.
Sprint anchor: most recent artifact date or TOPICS.md date.
Phase failure → apply RETRY PROTOCOL.

---

### ATTRIBUTION INTEGRITY GATE [C-28/C-30]
*Executes before Phase 1. Standalone. Not part of any phase block.*

Before I begin, I confirm [C-28/C-30]:
(1) No contributor will be named in this output from memory, role knowledge, or identity inference —
    every contributor must be traced to a real artifact filename or frontmatter field.
(2) This commitment applies to all phases. Any phase that would violate it must apply RETRY PROTOCOL
    and re-derive from artifact evidence before continuing.
If this commitment cannot be made: apply RETRY PROTOCOL before Phase 1.

---

### Phase 1 — Artifact Scan

**ENTER**: workspace filesystem + TOPICS.md
**TASK**: Glob `simulations/**/*.md`. Build scan state with topic, namespace, contributor, date per file.

```
SCAN STATE [Phase 1 output]:
  Topics: [list]   Namespaces: [list]   Contributors: [list]   Signals: [n]
```

**EXIT — SCAN GATE [C-01/C-02/C-23]**
Before I hand scan state to Phase 2, I confirm [C-01/C-02/C-23]:
(1) Every topic in scan state is traceable to a real glob result — no hallucinated topics.
(2) Every topic in scan state will appear in the Phase 3 achievements output.
(3) TOPICS.md entries with no artifacts are flagged [ORPHAN_TOPIC from registry].
→ Handoff: SCAN STATE sealed. Phases 2–7 receive this state; they do not re-interpret raw files.
If any sub-condition fails: apply RETRY PROTOCOL — name the specific failing topic.

---

### Phase 2 — Milestones

**ENTER**: SCAN STATE from Phase 1
**TASK**: Evaluate three named team milestones. Sprint framing: "Sprint ending {date} — {N} topics tracked."

**EXIT — MILESTONE GATE [C-03/C-23]**
Before I hand milestone state to Phase 3, I confirm [C-03/C-23]:
(1) "First Team Signal" appears by exact name in the output.
(2) "Shared Coverage" appears by exact name in the output.
(3) "Debate Starter" appears by exact name in the output.
→ Handoff: MILESTONE STATE (earned/not-earned for each of 3 milestones).
If any sub-condition fails: apply RETRY PROTOCOL — name the missing milestone string.

---

### Phase 3 — Achievement Census

**ENTER**: SCAN STATE + MILESTONE STATE
**TASK**: For each topic, list earned (✓) and available (○) achievements under two named categories:
- **Category A — Individual Signals**: First Signal, Signal Depth, Full Sweep
- **Category B — Team Milestones**: First Team Signal, Shared Coverage, Debate Starter

**EXIT — ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23]**
Before I hand achievement census to Phase 4, I confirm [C-06/C-07/C-11/C-23]:
(1) Earned (✓) and available (○) are visually separated for every topic row.
(2) All achievements are under a named category label.
(3) Pre-write check for Phase 6: every next action I write will name the exact achievement it unlocks.
(4) Gate label enumerates: C-06, C-07, C-11, C-23.
→ Handoff: ACHIEVEMENT CENSUS (per-topic earned/available with category labels).
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 4 — Contributor Leaderboard

**ENTER**: SCAN STATE (Phase 0 attribution commitment applies)
**TASK**: Score all contributors. Render worked example for Rank-1 above table.

`Rank-1 calculation: Score = {S}×1 + {T}×3 + {M}×5 = {total}`

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|

**EXIT — LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25]**
Before I hand leaderboard to Phase 5, I confirm [C-16/C-19/C-21/C-25]:
(1) Every row uses Score = Signals×1 + Topics×3 + Milestones×5. [C-16]
(2) Rank-1 worked example is rendered above the table. [C-19]
(3) If worked example total ≠ Score column: correct before handoff. [C-21]
(4) Gate label enumerates: C-16, C-19, C-21, C-25. [C-25]
→ Handoff: LEADERBOARD (ranked, formula-verified).
If any sub-condition fails: apply RETRY PROTOCOL.

Did Phase 2's milestone census surface topics not yet in Phase 4's contributor totals?
If yes, update before proceeding. [C-24 cross-phase check]

---

### Phase 5 — 1-Away Callouts

**ENTER**: ACHIEVEMENT CENSUS + LEADERBOARD
**TASK**: Identify topics/contributors exactly one action from unlocking an achievement.

| Topic/Target | Achievement to Unlock | Gap (What's Missing) | Exact Action Needed |
|---|---|---|---|

**EXIT — 1-AWAY GATE [C-09/C-18/C-23]**
Before I hand 1-away table to Phase 6, I confirm [C-09/C-18/C-23]:
(1) Section is standalone — not merged with achievements or next actions.
(2) All four columns present: Topic/Target, Achievement to Unlock, Gap, Exact Action Needed.
(3) Every row fully populated — no blank cells.
→ Handoff: 1-AWAY TABLE (sealed, all rows complete).
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 6 — Next Actions

**ENTER**: ACHIEVEMENT CENSUS + 1-AWAY TABLE + STAGNATION PATTERN REGISTRY
**TASK**: Format: `[Action] → Unlocks [Achievement] → Breaks [PATTERN_LABEL from registry]`

**EXIT — ACTIONS GATE [C-05/C-12/C-14/C-20/C-25]**
Before I hand next actions to Phase 7, I confirm [C-05/C-12/C-14/C-20/C-25]:
(1) Every action names the exact achievement it unlocks. [C-05/C-12]
(2) Every action names a registry stagnation pattern. [C-12/C-14]
(3) No label was invented inline — all labels are in the registry. [C-14]
(4) Gate label enumerates: C-05, C-12, C-14, C-20, C-25. [C-20/C-25]
→ Handoff: NEXT ACTIONS (anti-inertia format, registry labels only).
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 7 — Cross-Topic Team Insight

**ENTER**: Full output from Phases 1–6
**TASK**: State one insight not derivable from any single topic view alone.

**EXIT — INSIGHT GATE [C-10/C-13/C-22/C-24/C-25]**
Before I write the team insight, I confirm [C-10/C-13/C-22/C-24/C-25]:
(1) Insight is not derivable from any single topic view alone — genuine synthesis required. [C-22]
(2) Insight differs from any stagnation pattern or gap already stated. [C-10]
(3) Formatted: **TEAM INSIGHT — [descriptive name]: [insight text]** [C-13]
(4) Did Phase 1's scan or Phase 6's actions surface a cross-topic pattern that changes this
    insight? If yes, update before writing. [C-24]
(5) Gate label enumerates: C-10, C-13, C-22, C-24, C-25. [C-25]
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Structural Audit

**STRUCTURAL AUDIT GATE [C-26/C-27/C-34]**
Before I mark complete, I confirm [C-26/C-27/C-34]:

(1) All gate labels carry criterion ID references — checked:
    ATTRIBUTION INTEGRITY GATE [C-28/C-30] ✓ | SCAN GATE [C-01/C-02/C-23] ✓
    MILESTONE GATE [C-03/C-23] ✓ | ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23] ✓
    LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25] ✓ | 1-AWAY GATE [C-09/C-18/C-23] ✓
    ACTIONS GATE [C-05/C-12/C-14/C-20/C-25] ✓ | INSIGHT GATE [C-10/C-13/C-22/C-24/C-25] ✓
    STRUCTURAL AUDIT GATE [C-26/C-27/C-34] ✓

(2) Full-label enumeration with expected IDs — all 9 super-gates [C-27/C-34]:
    "ATTRIBUTION INTEGRITY GATE [C-28/C-30]" → C-28, C-30
    "SCAN GATE [C-01/C-02/C-23]" → C-01, C-02, C-23
    "MILESTONE GATE [C-03/C-23]" → C-03, C-23
    "ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23]" → C-06, C-07, C-11, C-23
    "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25]" → C-16, C-19, C-21, C-25
    "1-AWAY GATE [C-09/C-18/C-23]" → C-09, C-18, C-23
    "ACTIONS GATE [C-05/C-12/C-14/C-20/C-25]" → C-05, C-12, C-14, C-20, C-25
    "INSIGHT GATE [C-10/C-13/C-22/C-24/C-25]" → C-10, C-13, C-22, C-24, C-25
    "STRUCTURAL AUDIT GATE [C-26/C-27/C-34]" → C-26, C-27, C-34

(3) N=9, all 9 enumerated. [C-34]

If missing criterion IDs in any label: apply RETRY PROTOCOL.
If any cluster gate missing from enumeration: apply RETRY PROTOCOL.

---

---

## V-04 — Combined: C-31/C-32 Protocol Module + C-33 Phase-0 + Phrasing Register

**Axes**:
1. **Global protocol module** (C-31/C-32): RETRY PROTOCOL declared as a versioned, titled module
   with explicit step labels — `Step 1: Triad`, `Step 2: Delimit`, `Step 3: Continue` — making
   the three-step procedure machine-readable.
2. **Phase-0 attribution** (C-33): Attribution gate at Phase 0, before scan, with an explicit
   "blank list" commitment that pre-dates all evidence.
3. **Phrasing register**: Universal first-person ownership — every output section header uses
   "Before I write this section, I confirm [C-28]:" framing, not just the leaderboard.

**Hypothesis**: When all three structural requirements (global retry protocol, pre-scan attribution
commitment, pervasive first-person ownership) are layered, the model is positioned as an agent
with an explicit contract before generating any content. Each section is an act of confirmed agency,
not a response to instructions. The output becomes a sequence of ownership statements rather than
a sequence of prompted completions.

---

```
╔═══════════════════════════════════════════════════════╗
║  RETRY PROTOCOL MODULE v1 [C-29/C-31/C-32]           ║
╠═══════════════════════════════════════════════════════╣
║  All gates reference this module. No gate embeds      ║
║  its own retry logic. Reference by module name only.  ║
╠═══════════════════════════════════════════════════════╣
║  Step 1 — TRIAD [C-29]:                               ║
║    GATE FAILED [C-XX]: [specific instance]            ║
║      — CORRECTION: [action]. Re-running this section. ║
║                                                       ║
║  Step 2 — DELIMIT [C-32]:                             ║
║    > RETRY [C-XX]: [specific instance]                ║
║    [complete re-run output]                           ║
║    > END RETRY [C-XX]                                 ║
║                                                       ║
║  Step 3 — CONTINUE [C-29]:                            ║
║    Proceed to next gate. Do not halt permanently.     ║
╚═══════════════════════════════════════════════════════╝

STAGNATION PATTERN REGISTRY
| SOLO_ISLAND | NAMESPACE_MOAT | SPRINT_FREEZE | SHALLOW_POOL | ORPHAN_TOPIC |
Use [PATTERN_LABEL from registry] syntax. No inline invention.

SCORING FORMULA: Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)
```

---

You are running `/corps-achievements`. Sprint anchor: most recent artifact date.
Execute phases in sequence. Gate failure → apply RETRY PROTOCOL MODULE v1.

---

### Phase 0 — Attribution Commitment (Pre-Scan)

The contributor list is empty. No artifacts have been read.

**ATTRIBUTION INTEGRITY GATE [C-28/C-30]**
Before I scan any file, I confirm [C-28/C-30]:
(1) I am committing, before any evidence exists, that every contributor I name in this output
    will be traceable to a real artifact filename or frontmatter field — not inferred from
    their known role, seniority, level, or project history.
(2) If during any later phase I notice myself assigning a score or achievement to a contributor
    I recognize rather than one evidenced by a file, I will stop and apply RETRY PROTOCOL MODULE v1.
Cannot make this commitment: apply RETRY PROTOCOL MODULE v1 before Phase 1.

---

### Phase 1 — Insight Hypothesis (Pre-Scan Synthesis Commitment)

Before scanning, commit to what the cross-topic insight might be.
Write: `INSIGHT HYPOTHESIS: I expect the team insight will be about [topic/pattern].`
This will be validated and refined after Phase 3.

---

### Phase 2 — Artifact Scan

Before I write the scan state, I confirm [C-28]: every file I am about to list is from a real
glob result — I have not added topics from memory and will not drop any from the output.

Glob `simulations/**/*.md`. Extract: topic path, namespace, contributor, date per file.

```
SCAN STATE:
  Topics: [list]   Namespaces: [list]   Contributors: [list]   Signals: [n]
```

**SCAN GATE [C-01/C-02/C-23]**
Before I seal scan state, I confirm [C-01/C-02/C-23]:
(1) Every topic is traceable to a real glob result — no hallucinated topics.
(2) Every topic will appear in the achievements output section.
(3) TOPICS.md entries with no artifacts are flagged [ORPHAN_TOPIC from registry].
If any sub-condition fails: apply RETRY PROTOCOL MODULE v1 — name the failing topic.

---

### Phase 3 — Milestones

Before I write the milestones section, I confirm [C-28]: all three milestone names appear
verbatim — I have not paraphrased them or merged them with other content.

**MILESTONE GATE [C-03/C-23]**
Before I finalize milestones, I confirm [C-03/C-23]:
(1) "First Team Signal" present by exact name.
(2) "Shared Coverage" present by exact name.
(3) "Debate Starter" present by exact name.
Sprint framing: "Sprint ending {date} — {N} topics tracked."
If any sub-condition fails: apply RETRY PROTOCOL MODULE v1.

---

### Phase 4 — Achievement Census

Before I write the achievement census, I confirm [C-28]: earned and available achievements
are visually separated, and every topic from scan state appears in the output.

**ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23]**
Before I seal the census, I confirm [C-06/C-07/C-11/C-23]:
(1) Earned (✓) / available (○) are separated for every topic.
(2) At least two named category labels used.
(3) Pre-write self-test: every next action in Phase 6 will name the exact achievement it unlocks.
(4) Gate label enumerates: C-06, C-07, C-11, C-23.
If any sub-condition fails: apply RETRY PROTOCOL MODULE v1.

---

### Phase 5 — Contributor Leaderboard

Before I write the leaderboard, I confirm [C-28]: every contributor score is derived from
Phase 2 scan state — no prior-knowledge attribution applies.

`Rank-1 calculation: Score = {S}×1 + {T}×3 + {M}×5 = {total}`

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|

**LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25]**
Before I seal the leaderboard, I confirm [C-16/C-19/C-21/C-25]:
(1) Every row uses Score = Signals×1 + Topics×3 + Milestones×5. [C-16]
(2) Rank-1 worked example rendered above the table. [C-19]
(3) If worked example ≠ Score column: correct before continuing. [C-21]
(4) Gate label enumerates: C-16, C-19, C-21, C-25. [C-25]
Did Phase 3's achievement census surface topics not yet in Phase 5's contributor totals?
If yes, update leaderboard before proceeding. [C-24]
If any sub-condition fails: apply RETRY PROTOCOL MODULE v1.

---

### Phase 6 — 1-Away Callouts

Before I write the 1-away table, I confirm [C-28]: this is a standalone section with
all four columns populated — I have not merged it with achievements or next actions.

| Topic/Target | Achievement to Unlock | Gap (What's Missing) | Exact Action Needed |
|---|---|---|---|

**1-AWAY GATE [C-09/C-18/C-23]**
Before I seal the 1-away table, I confirm [C-09/C-18/C-23]:
(1) Section is standalone.   (2) All four columns present.   (3) No blank cells.
If any sub-condition fails: apply RETRY PROTOCOL MODULE v1.

---

### Phase 7 — Next Actions

Before I write the next actions section, I confirm [C-28]: every action uses the anti-inertia
format and references a registry pattern label — no inline invention.

Format: `[Action] → Unlocks [Achievement] → Breaks [PATTERN_LABEL from registry]`

**ACTIONS GATE [C-05/C-12/C-14/C-20/C-25]**
Before I seal next actions, I confirm [C-05/C-12/C-14/C-20/C-25]:
(1) Every action names exact achievement it unlocks. [C-05/C-12]
(2) Every action names a registry pattern. [C-12/C-14]
(3) No label invented inline. [C-14]
(4) Gate label enumerates: C-05, C-12, C-14, C-20, C-25. [C-20/C-25]
If any sub-condition fails: apply RETRY PROTOCOL MODULE v1.

---

### Phase 8 — Cross-Topic Team Insight

Before I write the team insight, I confirm [C-28]: I am about to test my Phase 1 hypothesis
against scan findings — the insight must survive the derivability test, not just confirm
my pre-scan expectation.

Revisit INSIGHT HYPOTHESIS from Phase 1. Does scan evidence support, refute, or refine it?
State the outcome, then write the final insight.

**INSIGHT GATE [C-10/C-13/C-22/C-24/C-25]**
Before I seal the insight, I confirm [C-10/C-13/C-22/C-24/C-25]:
(1) Insight is not derivable from any single topic view alone. [C-22]
(2) Insight differs from any stagnation pattern or gap already stated. [C-10]
(3) Formatted: **TEAM INSIGHT — [descriptive name]: [insight text]** [C-13]
(4) Did Phase 7's action patterns surface anything that changes this insight? Update if yes. [C-24]
(5) Gate label enumerates: C-10, C-13, C-22, C-24, C-25. [C-25]
If any sub-condition fails: apply RETRY PROTOCOL MODULE v1.

---

### Structural Audit

Before I mark complete, I confirm [C-28]: I am about to verify that every gate in this skill
carries criterion IDs and that every cluster gate is named in the enumeration below.

**STRUCTURAL AUDIT GATE [C-26/C-27/C-34]**
Before I close this skill, I confirm [C-26/C-27/C-34]:

(1) All gate labels carry criterion IDs:
    ATTRIBUTION INTEGRITY GATE [C-28/C-30] ✓ | SCAN GATE [C-01/C-02/C-23] ✓
    MILESTONE GATE [C-03/C-23] ✓ | ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23] ✓
    LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25] ✓ | 1-AWAY GATE [C-09/C-18/C-23] ✓
    ACTIONS GATE [C-05/C-12/C-14/C-20/C-25] ✓ | INSIGHT GATE [C-10/C-13/C-22/C-24/C-25] ✓
    STRUCTURAL AUDIT GATE [C-26/C-27/C-34] ✓

(2) Full enumeration — all 9 super-gates with exact expected IDs [C-27/C-34]:
    "ATTRIBUTION INTEGRITY GATE [C-28/C-30]" → C-28, C-30
    "SCAN GATE [C-01/C-02/C-23]" → C-01, C-02, C-23
    "MILESTONE GATE [C-03/C-23]" → C-03, C-23
    "ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23]" → C-06, C-07, C-11, C-23
    "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25]" → C-16, C-19, C-21, C-25
    "1-AWAY GATE [C-09/C-18/C-23]" → C-09, C-18, C-23
    "ACTIONS GATE [C-05/C-12/C-14/C-20/C-25]" → C-05, C-12, C-14, C-20, C-25
    "INSIGHT GATE [C-10/C-13/C-22/C-24/C-25]" → C-10, C-13, C-22, C-24, C-25
    "STRUCTURAL AUDIT GATE [C-26/C-27/C-34]" → C-26, C-27, C-34

(3) N=9, all enumerated. [C-34]

If any gate label missing criterion IDs: apply RETRY PROTOCOL MODULE v1.
If any cluster gate missing from enumeration: apply RETRY PROTOCOL MODULE v1.

---

---

## V-05 — Combined: C-34 Tabular Audit + Inertia Framing + Output Schemas

**Axes**:
1. **C-34 tabular audit**: Structural audit rendered as a compliance table, not a prose
   enumeration. Each row: Gate Label | Expected IDs | Actual IDs | Status. Completeness
   is visible from row count without reading prose.
2. **Inertia framing**: The skill leads with a Stagnation Risk Dashboard (before achievements).
   What patterns are active? What momentum has stalled? Achievements follow as evidence of
   what broke the inertia. Next actions lead with the break, not the unlock.
3. **Output schemas**: All major output sections have their table schemas declared in the
   preamble. Gates verify schema compliance rather than schema design.

**Hypothesis**: Declaring schemas upfront + leading with stagnation risk frames the skill
as a risk register that happens to celebrate achievements, rather than a trophy case that
happens to note gaps. The tabular structural audit makes N-completeness machine-checkable:
count rows, compare to N.

---

```
═══════════════════════════════════════════════════════
RETRY PROTOCOL [C-29/C-31/C-32]
═══════════════════════════════════════════════════════
Global. All gates reference by name. No per-gate embedding.

On failure:
  GATE FAILED [C-XX]: [specific instance] — CORRECTION: [action]. Re-running this section.
  > RETRY [C-XX]: [specific instance]
  [re-run output]
  > END RETRY [C-XX]
═══════════════════════════════════════════════════════

STAGNATION PATTERN REGISTRY
| SOLO_ISLAND | NAMESPACE_MOAT | SPRINT_FREEZE | SHALLOW_POOL | ORPHAN_TOPIC |
[PATTERN_LABEL from registry] syntax only.

SCORING FORMULA: Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)

OUTPUT SCHEMAS (pre-declared — fill these, do not redesign)

SCHEMA-RISK: Stagnation Risk Dashboard
| Topic | Active Patterns | Severity (High/Med/Low) | Blocking Achievement |

SCHEMA-ACHIEVE: Achievement Census (per topic)
| Topic | Category | Achievement | Status (✓/○) | Evidence / Gap |

SCHEMA-LEADERBOARD: Contributor Leaderboard
| Rank | Contributor | Signals | Topics | Milestones | Score (S×1+T×3+M×5) |

SCHEMA-1AWAY: 1-Away Callouts
| Topic/Target | Achievement to Unlock | Gap (What's Missing) | Exact Action Needed |

SCHEMA-ACTIONS: Next Actions
| Action | Unlocks Achievement | Breaks Pattern [from registry] |

SCHEMA-MILESTONES: Team Milestones
| Milestone Name | Status (Earned/Not Earned) | Evidence |
```

---

You are running `/corps-achievements`. Sprint anchor: most recent artifact date.
Execute phases in order. Gate failure → apply RETRY PROTOCOL.

---

### ATTRIBUTION INTEGRITY GATE [C-28/C-30]
*Standalone. Executes before Phase 1. Not part of any phase block.*

Before I begin, I confirm [C-28/C-30]:
(1) No contributor will be named in this output from memory, role knowledge, or identity inference.
    Every contributor must be traced to a real artifact filename or frontmatter field.
(2) This commitment applies globally — any phase that violates it applies RETRY PROTOCOL.
Cannot commit: apply RETRY PROTOCOL before Phase 1.

---

### Phase 1 — Artifact Scan

Glob `simulations/**/*.md`. Extract topic, namespace, contributor, date per file.
Cross-reference TOPICS.md. Flag non-matching entries [ORPHAN_TOPIC from registry].

**SCAN GATE [C-01/C-02/C-23]**
Before I write scan state, I confirm [C-01/C-02/C-23]:
(1) Every topic is from a real glob result — no hallucinated topics.
(2) Every topic will appear in SCHEMA-ACHIEVE output.
(3) TOPICS.md entries with no files are flagged [ORPHAN_TOPIC from registry].
If any sub-condition fails: apply RETRY PROTOCOL — name the failing topic.

---

### Phase 2 — Stagnation Risk Dashboard (Leads Output)

**SECTION HEADER: STAGNATION RISK DASHBOARD — Sprint ending {date}**

Fill SCHEMA-RISK for all topics. Identify active patterns from the registry.
High severity: SOLO_ISLAND or ORPHAN_TOPIC. Med: NAMESPACE_MOAT or SPRINT_FREEZE.
Low: SHALLOW_POOL.

This section leads the output. Achievements follow as evidence of what was or could be unlocked.

**MILESTONE GATE [C-03/C-23]**
Before I write the milestones section (embedded in risk dashboard), I confirm [C-03/C-23]:
(1) "First Team Signal" present by exact name.
(2) "Shared Coverage" present by exact name.
(3) "Debate Starter" present by exact name.
Sprint framing present: "Sprint ending {date} — {N} topics tracked."
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 3 — Achievement Census

Fill SCHEMA-ACHIEVE for every topic from scan state.
Group rows under **Category A — Individual Signals** and **Category B — Team Milestones**.

**ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23]**
Before I write the census, I confirm [C-06/C-07/C-11/C-23]:
(1) Status column uses ✓ (earned) and ○ (available) — visually separated.
(2) All rows are under a named category label.
(3) Pre-write self-test: every action in Phase 5 will name the exact achievement it unlocks.
(4) Gate label enumerates: C-06, C-07, C-11, C-23.
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 4 — Contributor Leaderboard

Fill SCHEMA-LEADERBOARD using Phase 1 scan state (Phase 0 attribution commitment applies).
Render Rank-1 worked example above the table:
`Rank-1 calculation: Score = {S}×1 + {T}×3 + {M}×5 = {total}`

**LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25]**
Before I write the leaderboard, I confirm [C-16/C-19/C-21/C-25]:
(1) Score column uses Score = Signals×1 + Topics×3 + Milestones×5. [C-16]
(2) Rank-1 worked example rendered above table. [C-19]
(3) If worked example ≠ Score column: correct before continuing. [C-21]
(4) Gate label enumerates: C-16, C-19, C-21, C-25. [C-25]
Did Phase 2's stagnation patterns surface topics not in Phase 4's leaderboard? Update if yes. [C-24]
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 5 — 1-Away Callouts

Fill SCHEMA-1AWAY. Standalone section — not merged with achievements or next actions.

**1-AWAY GATE [C-09/C-18/C-23]**
Before I write the 1-away table, I confirm [C-09/C-18/C-23]:
(1) Section is standalone.
(2) All four schema columns present: Topic/Target, Achievement to Unlock, Gap, Exact Action Needed.
(3) Every row has all four columns populated.
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 6 — Next Actions

Fill SCHEMA-ACTIONS. Inertia-first framing: lead with the stagnation break, then the unlock.
Format: `[Action] → Unlocks [Achievement] → Breaks [PATTERN_LABEL from registry]`

**ACTIONS GATE [C-05/C-12/C-14/C-20/C-25]**
Before I write the next actions section, I confirm [C-05/C-12/C-14/C-20/C-25]:
(1) Every action names the exact achievement it unlocks. [C-05/C-12]
(2) Every action names a registry stagnation pattern. [C-12/C-14]
(3) No pattern label invented inline. [C-14]
(4) Gate label enumerates: C-05, C-12, C-14, C-20, C-25. [C-20/C-25]
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Phase 7 — Cross-Topic Team Insight

**INSIGHT GATE [C-10/C-13/C-22/C-24/C-25]**
Before I write the team insight, I confirm [C-10/C-13/C-22/C-24/C-25]:
(1) Insight is not derivable from any single topic view alone — requires synthesis. [C-22]
(2) Insight differs from any stagnation pattern or gap already stated. [C-10]
(3) Formatted: **TEAM INSIGHT — [descriptive name]: [insight text]** [C-13]
(4) Did Phase 2's stagnation dashboard or Phase 6's actions surface anything that changes this
    insight? Update if yes. [C-24]
(5) Gate label enumerates: C-10, C-13, C-22, C-24, C-25. [C-25]
If any sub-condition fails: apply RETRY PROTOCOL.

---

### Structural Audit

**STRUCTURAL AUDIT GATE [C-26/C-27/C-34]**
Before I mark complete, I confirm [C-26/C-27/C-34].

Render the compliance table (tabular audit for C-34):

| Gate Label | Expected IDs | Status |
|---|---|---|
| ATTRIBUTION INTEGRITY GATE [C-28/C-30] | C-28, C-30 | verify label matches |
| SCAN GATE [C-01/C-02/C-23] | C-01, C-02, C-23 | verify label matches |
| MILESTONE GATE [C-03/C-23] | C-03, C-23 | verify label matches |
| ACHIEVEMENT CLUSTER GATE [C-06/C-07/C-11/C-23] | C-06, C-07, C-11, C-23 | verify label matches |
| LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-25] | C-16, C-19, C-21, C-25 | verify label matches |
| 1-AWAY GATE [C-09/C-18/C-23] | C-09, C-18, C-23 | verify label matches |
| ACTIONS GATE [C-05/C-12/C-14/C-20/C-25] | C-05, C-12, C-14, C-20, C-25 | verify label matches |
| INSIGHT GATE [C-10/C-13/C-22/C-24/C-25] | C-10, C-13, C-22, C-24, C-25 | verify label matches |
| STRUCTURAL AUDIT GATE [C-26/C-27/C-34] | C-26, C-27, C-34 | verify label matches |

Row count = 9. N=9. All N enumerated. [C-34 satisfied]

(1) Every gate carries criterion IDs — column 1 confirms. [C-26]
(2) Every gate named by full label with exact expected IDs — column 2 confirms. [C-27]
(3) Table has 9 rows = all 9 cluster gates in this skill. [C-34]

If any row shows a mismatch: apply RETRY PROTOCOL — name the row.
If table has fewer than 9 rows: apply RETRY PROTOCOL — name the missing gate.
```

---

## Criterion Coverage Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 | SCAN GATE | SCAN GATE | SCAN GATE EXIT | SCAN GATE | SCAN GATE |
| C-02 | SCAN GATE | SCAN GATE | SCAN GATE EXIT | SCAN GATE | SCAN GATE |
| C-03 | MILESTONE GATE | MILESTONE GATE | MILESTONE EXIT | MILESTONE GATE | MILESTONE GATE |
| C-04 | LEADERBOARD section | LEADERBOARD section | LEADERBOARD section | LEADERBOARD section | LEADERBOARD section |
| C-05 | ACTIONS GATE | ACTIONS GATE | ACTIONS EXIT | ACTIONS GATE | ACTIONS GATE |
| C-06 | ACHIEVE CLUSTER | ACHIEVE CLUSTER | ACHIEVE EXIT | ACHIEVE CLUSTER | ACHIEVE CLUSTER |
| C-07 | ACHIEVE CLUSTER | ACHIEVE CLUSTER | ACHIEVE EXIT | ACHIEVE CLUSTER | ACHIEVE CLUSTER |
| C-08 | Phase 2 framing | Phase 2 framing | Phase 2 framing | Phase 3 framing | Phase 2 framing |
| C-09 | 1-AWAY GATE | 1-AWAY GATE | 1-AWAY EXIT | 1-AWAY GATE | 1-AWAY GATE |
| C-10 | INSIGHT GATE | INSIGHT GATE | INSIGHT EXIT | INSIGHT GATE | INSIGHT GATE |
| C-11 | ACHIEVE CLUSTER(3) | ACHIEVE CLUSTER(3) | ACHIEVE EXIT(3) | ACHIEVE CLUSTER(3) | ACHIEVE CLUSTER(3) |
| C-12 | ACTIONS GATE | ACTIONS GATE | ACTIONS EXIT | ACTIONS GATE | ACTIONS GATE |
| C-13 | INSIGHT GATE | INSIGHT GATE | INSIGHT EXIT | INSIGHT GATE | INSIGHT GATE |
| C-14 | ACTIONS GATE + registry | ACTIONS GATE + registry | ACTIONS EXIT + registry | ACTIONS GATE + registry | ACTIONS GATE + registry |
| C-15 | RETRY PROTOCOL | RETRY PROTOCOL | RETRY PROTOCOL | RETRY PROTOCOL MODULE | RETRY PROTOCOL |
| C-16 | LEADERBOARD CLUSTER | LEADERBOARD CLUSTER | LEADERBOARD EXIT | LEADERBOARD CLUSTER | LEADERBOARD CLUSTER |
| C-17 | Registry labels | Registry labels | Registry labels | Registry labels | Registry labels |
| C-18 | 1-AWAY GATE table | 1-AWAY GATE table | 1-AWAY EXIT table | 1-AWAY GATE table | SCHEMA-1AWAY |
| C-19 | LEADERBOARD CLUSTER | LEADERBOARD CLUSTER | LEADERBOARD EXIT | LEADERBOARD CLUSTER | LEADERBOARD CLUSTER |
| C-20 | All gate labels | All gate labels | All gate labels | All gate labels | All gate labels |
| C-21 | LEADERBOARD CLUSTER(3) | LEADERBOARD CLUSTER(3) | LEADERBOARD EXIT(3) | LEADERBOARD CLUSTER(3) | LEADERBOARD CLUSTER(3) |
| C-22 | INSIGHT GATE(1) | INSIGHT GATE(1) | INSIGHT EXIT(1) | INSIGHT GATE(1) | INSIGHT GATE(1) |
| C-23 | All gates numbered | All gates numbered | All EXIT contracts | All gates numbered | All gates numbered |
| C-24 | INSIGHT GATE(4) | INSIGHT GATE(4) | Phase 4 cross-phase | LEADERBOARD+INSIGHT | LEADERBOARD+INSIGHT |
| C-25 | LEADERBOARD/ACTIONS/INSIGHT | LEADERBOARD/ACTIONS/INSIGHT | All multi-gates | LEADERBOARD/ACTIONS/INSIGHT | LEADERBOARD/ACTIONS/INSIGHT |
| C-26 | STRUCT AUDIT(1) | STRUCT AUDIT(1) | STRUCT AUDIT(1) | STRUCT AUDIT(1) | STRUCT AUDIT(1) |
| C-27 | STRUCT AUDIT(2) | STRUCT AUDIT(2) | STRUCT AUDIT(2) | STRUCT AUDIT(2) | STRUCT AUDIT table |
| C-28 | All gates first-person | All gates first-person | All EXIT first-person | Universal first-person | All gates first-person |
| C-29 | RETRY PROTOCOL | RETRY PROTOCOL | RETRY PROTOCOL | RETRY PROTOCOL MODULE | RETRY PROTOCOL |
| C-30 | ATTRIB GATE(1-2) | PHASE-0 ATTRIB GATE | ATTRIB GATE pre-Phase | PHASE-0 ATTRIB GATE | ATTRIB GATE global |
| C-31 | Preamble module | Preamble module | Preamble module | Named MODULE v1 | Preamble module |
| C-32 | > RETRY / > END RETRY | > RETRY / > END RETRY | > RETRY / > END RETRY | > RETRY / > END RETRY | > RETRY / > END RETRY |
| C-33 | Standalone before leaderboard | Phase-0 standalone | Pre-Phase-1 standalone | Phase-0 standalone | Standalone pre-Phase-1 |
| C-34 | 9-gate prose list | 9-gate prose list | 9-gate prose list | 9-gate prose list | 9-row compliance table |

**All 34 criteria covered in all 5 variations.**

---

## Axis Differentiation Summary

| What varies | V-01 | V-02 | V-03 | V-04 | V-05 |
|-------------|------|------|------|------|------|
| Retry protocol presentation | Boxed module header | Compact inline | Compact inline | Versioned module box | Compact inline |
| Attribution gate position | After Phase 1 scan | Phase 0 (pre-scan) | Pre-Phase-1 standalone | Phase 0 (pre-scan) | Pre-Phase-1 standalone |
| Phase order | Scan→Milestones→Achieve→Leaderboard | Standard | Standard (entry/exit) | Insight-hypothesis-first | Stagnation-first |
| Output structure | Free-form sections | Free-form sections | Phase contracts | Free-form + hypothesis | Pre-declared schemas |
| Structural audit format | Prose enumeration | Prose enumeration | Inline prose | Prose enumeration | Compliance table |
| Phrasing register | Gate-local first-person | Gate-local first-person | Gate-local first-person | Universal first-person | Gate-local first-person |
| Lifecycle emphasis | Standard | Standard | Heavy (entry/exit contracts) | Standard + hypothesis | Schema-anchored |
| Inertia framing | Embedded | Embedded | Embedded | Pre-scan commitment | Leads output (Phase 2) |
