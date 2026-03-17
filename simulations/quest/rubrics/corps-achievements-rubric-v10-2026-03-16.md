**corps-achievements-rubric-v10** written to `simulations/quest/rubrics/corps-achievements-rubric-v10-2026-03-16.md`.

---

### What changed v9 → v10

**C-28 (carried from v9)** — Redefined from "enumeration-in-pass-record" to **first-person owner confirmation syntax**. The old behavior (pass messages recording enumerated IDs) is absorbed as baseline. The new bar: the gate must frame confirmation as `"Before I write this section, I confirm [C-28]: …"` — binding the model as committed agent, not auditor.

**C-29** (new, from ES-1 / V-05) — **Gate-failure retry loop**. The named correction triad:
```
GATE FAILED [C-XX]: [specific instance] — CORRECTION: [action]. Re-running this section.
```
Converts gate violation from terminal prohibition to recoverable procedure. A gate that halts or flags without re-running does not satisfy this criterion.

**C-30** (new, from ES-2 / V-01+V-04) — **Achievement-derived attribution constraint**. A pre-write leaderboard gate must explicitly prohibit backward inference — contributor scores must derive *from* Phase 1 census evidence, not from the model's prior knowledge of who the prominent contributors are. Closes a correctness gap C-02 (topic coverage) and C-16 (formula) don't address.

**Scoring**: aspirational pool grows 20 → 22; each criterion now worth `20/22 ≈ 0.909 pts`. Maximum still 100.
parated |
| C-07 | Achievements grouped into at least 2 named categories with explicit labels |
| C-08 | Sprint/date framing present in output |

---

### ASPIRATIONAL (22)

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
| C-28 | When a gate includes a criterion-confirmation condition, the gate frames that confirmation as a first-person ownership statement from the model — e.g., "Before I write this section, I confirm [C-28]: …" — rather than a procedural sub-step or external instruction; framing that reads "Does X satisfy C-28?" or "Check C-28 before proceeding" does not satisfy this criterion because it positions the model as an auditor rather than a committed agent |
| C-29 | When a gate check fails, the skill instructs the model to emit a named correction triad — `"GATE FAILED [C-XX]: [specific instance] — CORRECTION: [action]. Re-running this section."` — and then re-run the affected section; converting gate violation from a terminal halt event to a named, recoverable correction procedure; a skill that instructs the model to halt or flag without specifying the re-run step does not satisfy this criterion |
| C-30 | When the skill includes a contributor leaderboard, the skill includes a pre-write gate condition that explicitly prohibits inferring achievements backward from contributor identity — requiring that contributor scores derive from the Phase 1 achievement census, not from the model's prior knowledge of contributors' roles or prominence; a gate that verifies formula correctness (C-16) or phase ordering (C-24) without this backward-inference prohibition does not satisfy this criterion |

---

## Scoring Formula

```
score = (essential_pass/5 × 60) + (recommended_pass/3 × 20) + (aspirational_pass/22 × 20)
PARTIAL = 0.5 weight
```

**Essential**: 5 criteria × 12 pts = 60 pts maximum
**Recommended**: 3 criteria × 6.67 pts = 20 pts maximum
**Aspirational**: 22 criteria × 0.909 pts = 20 pts maximum

To reach 100: all essential pass + all recommended pass + all aspirational pass.
