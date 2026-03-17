Reading the R4 scorecard carefully for new patterns before writing.

The scorecard surfaces two distinct excellence patterns beyond what v4 captures:

**C-19** — From the C-16 analysis (V-01/V-03/V-05 pass, V-02/V-04 partial): The differentiator was not whether the formula was stated — all five do that — but whether the skill explicitly instructs the model to render a worked example calculation inline. V-01: *"Show formula calculation for rank-1 contributor: e.g., 'Score = 8×1 + 3×3 + 1×5 = 22.'"* V-02 only asserts *"the formula makes rank auditable"* without the instruction. Asserting a property and enforcing it with an instruction are different things.

**C-20** — From V-05's gate syntax: `[C-04/C-16]` as the gate label creates a direct traceable link between the skill's verification logic and rubric criterion IDs. V-03 achieves the same gate with natural language (*"I will show the formula and show the calculation"*) — both pass C-11 — but the criterion-ID notation makes gate coverage auditable against the rubric without narrative reconstruction.

Scoring formula: aspirational pool grows 10 → 12.

---

```markdown
# corps-achievements Rubric — v5

**Updated:** 2026-03-16
**Basis for upgrade:** R4 scorecard — excellence signals from V-01/V-03/V-05 (100) vs V-02/V-04 (99)
**Changes from v4:** Added C-19 (worked example for formula-driven output), C-20 (gate labels
reference criterion IDs); aspirational pool grows from 10 to 12; scoring formula updated.

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

### ASPIRATIONAL (12)

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

---

## Scoring Formula

```
score = (essential_pass/5 × 60)
      + (recommended_pass/3 × 30)
      + (aspirational_pass/12 × 10)
```

**Golden threshold:** all 5 essential pass **and** composite score ≥ 80.

**Notes on PARTIAL:**
- PARTIAL counts as 0 for scoring purposes.
- A PARTIAL on any essential criterion is a gate failure regardless of composite score.

---

## Upgrade Notes

### R4 → v5: Two new aspirational criteria

**C-19 — Worked example for formula-driven output**

The R4 scorecard split V-01/V-03/V-05 (100) from V-02/V-04 (99) on a single point in C-16:
all five state the weighted formula, all five show raw count columns, but only V-01/V-03/V-05
explicitly instruct the model to render a rank-1 worked example inline. V-02 asserts
*"the formula makes rank auditable from raw counts"* — a property claim. V-01 instructs
*"Show formula calculation for rank-1 contributor: e.g., 'Score = 8×1 + 3×3 + 1×5 = 22'"* —
an enforcement instruction. The distinction: asserting a property and enforcing it are different
things. C-19 captures this as a standalone criterion because the pattern generalizes beyond
leaderboards to any formula-driven section.

**C-20 — Gate labels reference criterion IDs**

V-05 uses `[C-04/C-16]` notation on gate labels; V-03 achieves the same gate effect through
natural language commitment. Both pass C-11. The V-05 pattern adds a layer: the gate label
creates a machine-readable link between skill verification logic and rubric criterion IDs,
making gate coverage auditable by inspection rather than narrative reconstruction. This is a
distinct property from C-11 (gate exists) and C-15 (gate failure names the instance).
```
