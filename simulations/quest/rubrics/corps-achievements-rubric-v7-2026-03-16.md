Reading the scorecard evidence column line-by-line for differentiating patterns before writing.

Three signals stand out — all from evidence notes that describe something one variation does that goes beyond what the current rubric requires:

**C-24** — From V-03's C-09 and C-11 notes ("Phase 2 milestone gaps fed into condition (3)" and "PHASE 3 gate explicitly asks whether milestone gaps from Phase 2 surface topics not yet in scan"): V-03 threads earlier-phase outputs directly into later-phase gate conditions — the Phase 3 gate asks whether Phase 2's gaps reveal topics the Phase 1 scan missed. V-01 and V-02 run each phase's gate in isolation. Making a gate explicitly ask "does this phase's output alter what a prior phase computed?" turns sequential execution into a dynamic feedback loop across phases.

**C-25** — From V-02's C-05 and C-20 notes ("Actions check [C-05/C-12/C-14/C-20]"): V-02 clusters four interdependent criteria into a single named gate whose label enumerates all criterion IDs it covers. V-01 and V-03 use one gate per criterion or criterion pair. When related criteria are checked together under a shared label, the label itself documents inter-criterion dependency and prevents partial-cluster passes where some criteria are verified but related ones are silently skipped.

**C-26** — From V-01's C-20 note ("ACTIONS GATE condition (5) self-validates the label"): V-01 includes a gate condition that checks whether the gate label carrying it is itself properly formatted with criterion IDs — a meta-verification step. C-20 requires gates to carry criterion ID references; C-26 goes further by requiring the skill to contain at least one gate condition that audits whether that requirement is satisfied elsewhere in the skill, making structural compliance self-enforcing rather than dependent on external rubric review.

Aspirational pool grows 15 → 18. Scoring formula denominator updates accordingly.

---

```markdown
# corps-achievements Rubric — v7

**Updated:** 2026-03-16
**Basis for upgrade:** R7 scorecard — all five variations scored 100; excellence signals from
V-03's cross-phase gate threading (C-24), V-02's multi-criterion gate clustering (C-25), and
V-01's meta-verification gate condition (C-26)
**Changes from v6:** Added C-24 (cross-phase gate threading), C-25 (multi-criterion gate
clustering with enumerated label), C-26 (meta-verification gate for structural compliance);
aspirational pool grows from 15 to 18; scoring formula updated.

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

### ASPIRATIONAL (18)

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

---

## Scoring Formula

```
score = (essential_pass/5 × 60)
      + (recommended_pass/3 × 30)
      + (aspirational_pass/18 × 10)
```
```
