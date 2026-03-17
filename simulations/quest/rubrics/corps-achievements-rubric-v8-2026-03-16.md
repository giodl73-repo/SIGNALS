Two new excellence signals from V-05. Now I have everything needed to write v8.

**E-01 → C-27**: V-05's structural audit gate names each super-gate by its full label and specifies the exact IDs expected in it — catching wrong-enumeration failures (`[C-16/C-19]` vs `[C-16/C-19/C-21]`) that V-04's presence-only check misses.

**E-02 → C-28**: V-05 super-gate pass messages explicitly record `"Label enumeration (C-25): [C-16/C-19/C-21] verified."` as a named line item — making C-25 compliance auditable from the pass record alone without re-reading the gate body.

Aspirational pool grows 18 → 20.

```markdown
# corps-achievements Rubric — v8

**Updated:** 2026-03-16
**Basis for upgrade:** R8 scorecard — V-05 scored 100; excellence signals from
V-05's expected-enumeration audit (C-27) and enumeration-in-pass-record (C-28)
**Changes from v7:** Added C-27 (expected-enumeration audit in structural gate),
C-28 (enumeration verification named in pass confirmation); aspirational pool
grows from 18 to 20; scoring formula updated.

---

## Criteria

### ESSENTIAL (5) — all must pass

| ID | What it checks |
|----|----------------|
| C-01 | Artifact scan grounded in real workspace files — no hallucinated topics |
| C-02 | Every discovered topic appears in achievements output |
| C-03 | All three named milestones present by name (First Team Signal, Shared Coverage, Debate Starter) |
| C-04 | Contributor leaderboard section exists and is populated |
| C-05 | Next actions name both the action AND the achievement it unlocks |

---

### RECOMMENDED (3)

| ID | What it checks |
|----|----------------|
| C-06 | Earned vs. available achievements visually separated |
| C-07 | Achievements grouped into at least 2 named categories with explicit labels |
| C-08 | Sprint/date framing present in output |

---

### ASPIRATIONAL (20)

| ID | What it checks |
|----|----------------|
| C-09 | "1 away" quantified close-to-unlock callouts — dedicated section with exact count and exact thing needed |
| C-10 | Cross-topic or cross-contributor insight stated as a named conclusion — and that conclusion differs from any stagnation pattern or gap statement already made |
| C-11 | Skill includes at least one inline pre-write self-test gate — a verification question or confirmation statement the model must answer before generating a section (e.g., "Does this next action name the exact achievement it unlocks?") |
| C-12 | Next actions use anti-inertia framing: each action names not only what it unlocks but what stagnation pattern it breaks — format `[Action] → Unlocks [Achievement] → Breaks [Pattern]` |
| C-13 | The cross-topic insight (C-10) is formatted as a titled, named artifact — `**TEAM INSIGHT — [descriptive name]:**` — making it referenceable by name rather than embedded in prose |
| C-14 | Stagnation patterns referenced in anti-inertia actions (C-12) are drawn from a pre-existing named registry, not invented inline — enforced via label syntax such as `[PATTERN_LABEL from registry]`, preventing vocabulary drift across runs |
| C-15 | When a gate check fails, the error message names the specific instance that triggered the failure (topic name, contributor name, or action row) — not just "halt" but "GATE-B: [topic X] missing → halt" — creating a self-documenting failure trace |
| C-16 | The contributor leaderboard uses an explicit weighted scoring formula (e.g., Signals×1 + Topics×3 + Milestones×5) — not a rank-ordered count — making each contributor's score auditable from raw counts and the team's value judgment about signal types explicit and debatable |
| C-17 | Stagnation pattern labels (C-14) use semantic names that encode the pattern type without requiring a definition lookup (e.g., SOLO_ISLAND, NAMESPACE_MOAT, SPRINT_FREEZE) — opaque codes such as PATTERN_1 do not satisfy this criterion |
| C-18 | The 1-away callout (C-09) is rendered as a structured table with distinct columns for at minimum: topic/target, achievement to unlock, gap (what's missing), and exact action needed — preventing prose from omitting any field for individual entries |
| C-19 | When the skill includes a formula-driven ranked section (e.g., contributor leaderboard), the skill explicitly instructs the model to render a worked example calculation for the top-ranked contributor inline — e.g., `"Rank-1 calculation: Score = {n}×1 + {n}×3 + {n}×5 = {total}"` — so the reader can verify the ranking without reconstruction; asserting that the formula "makes scores auditable" without this instruction does not satisfy this criterion |
| C-20 | Inline gate checks reference criterion IDs (e.g., `[C-04/C-16]`) as part of the gate label — creating a direct, traceable link between the skill's verification logic and rubric criteria — making gate coverage auditable against the rubric without narrative reconstruction |
| C-21 | When the skill includes a formula verification gate (C-19), the gate explicitly instructs the model to reconcile the ranked table if the worked example calculation reveals a mismatch — e.g., "If the calculated total does not match the Score column entry, correct the table before proceeding" — turning the gate from a display check into an active correction loop; a gate that renders the calculation but does not instruct correction does not satisfy this criterion |
| C-22 | The cross-topic insight gate (C-10) applies a single-topic-derivability test — the skill explicitly instructs that the insight must NOT be derivable from any single topic view alone, not merely cross-topic or cross-contributor in scope — forcing genuine synthesis rather than parallel observation; a gate that only checks scope without testing derivability does not satisfy this criterion |
| C-23 | Multi-condition gate checks enumerate their conditions as numbered sub-steps — e.g., "(1) Every topic I list is traced to a real file. (2) Every topic appears in the achievement section. (3) …" — making each condition individually checkable and preventing a gate from being treated as passed when only some sub-conditions are satisfied; prose commitment statements inside a gate do not satisfy this criterion |
| C-24 | When the skill uses multi-phase execution, at least one later-phase gate explicitly asks whether findings from a prior phase alter the current phase's output — e.g., "Did Phase 2's milestone gaps surface topics not already in the Phase 1 scan?" — creating dynamic cross-phase continuity; a gate that only verifies the current phase's own output without referencing prior-phase findings does not satisfy this criterion |
| C-25 | When a single gate covers multiple interdependent criteria simultaneously, the gate label enumerates all criterion IDs it covers — e.g., `[C-05/C-12/C-14/C-20]` — making inter-criterion dependency explicit and preventing partial-cluster passes where some criteria in the group are verified but related ones are silently omitted; a gate label that names only one criterion ID for a multi-criterion check does not satisfy this criterion |
| C-26 | The skill includes at least one gate condition that verifies whether all other gate labels in the skill carry criterion ID references — a meta-verification step that makes structural compliance (C-20) self-enforcing rather than dependent on external rubric review; C-20 is satisfied by gates that carry criterion IDs, but C-26 is only satisfied when a gate condition audits that requirement across the skill's own gate labels |
| C-27 | When the skill includes a structural audit gate (C-26), that gate names each multi-criterion super-gate by its full label and specifies the exact criterion IDs expected in it — e.g., `"'LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]' — confirm label enumerates C-16, C-19, C-21"` — enabling detection of wrong-enumeration failures (a label that reads `[C-16/C-19]` when `[C-16/C-19/C-21]` is required) that a generic presence check cannot catch; a structural audit that only checks whether any criterion ID appears in a gate label does not satisfy this criterion |
| C-28 | When the skill includes multi-criterion super-gates (C-25), each gate's pass confirmation message explicitly records the criterion IDs verified in the label as a named line item — e.g., `"Label enumeration (C-25): [C-16/C-19/C-21] verified."` — making C-25 compliance auditable from the run's pass record alone without re-reading the gate body; a pass message that confirms per-criterion outcomes but does not name the enumeration verification as a separate item does not satisfy this criterion |

---

## Scoring Formula

```
score = (essential_pass/5 × 60) + (recommended_pass/3 × 20) + (aspirational_pass/20 × 20)
PARTIAL = 0.5 weight
```

**Essential**: 5 criteria × 12 pts = 60 pts maximum
**Recommended**: 3 criteria × 6.67 pts = 20 pts maximum
**Aspirational**: 20 criteria × 1 pt = 20 pts maximum

To reach 100: all essential pass + all recommended pass + all aspirational pass.
```
