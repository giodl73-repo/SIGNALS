Reading the scorecard carefully for differentiating patterns before writing.

Three signals stand out — all from per-criterion comparisons where the scorecard notes "strongest" implementations or names a "defining axis":

**C-21** — From V-02's C-19 note ("strongest C-19 implementation"): the differentiator is that V-02's gate says *"If the calc does not match the table, correct the table before proceeding."* V-01 and V-03 render the worked example but stop there. Adding an explicit reconciliation instruction turns the gate from a display check into an active correction loop — the model is required to close the consistency gap, not just expose it.

**C-22** — From V-03's C-10 note ("strongest C-10 instruction"): V-03's formulation is *"not derivable from any single topic view"* rather than just *"cross-topic or cross-contributor in scope."* A finding can satisfy scope without requiring synthesis — e.g., two topics that both independently show the same pattern. The single-topic-derivability test forces genuine cross-signal reasoning.

**C-23** — From V-03's defining axis ("per-section numbered self-test gate"): V-03 enumerates gate conditions as numbered sub-steps `(1)… (2)… (3)…`. V-01 and V-02 use prose commitment statements inside gates. Numbered sub-steps make each condition individually checkable and prevent a gate from being treated as passed when only some sub-conditions are satisfied — a structural improvement in gate precision.

Aspirational pool grows 12 → 15. Scoring formula denominator updates accordingly.

---

```markdown
# corps-achievements Rubric — v6

**Updated:** 2026-03-16
**Basis for upgrade:** R5 scorecard — all three variations scored 100; excellence signals from
V-02's correction-loop gate (C-21), V-03's single-topic-derivability test (C-22), and V-03's
numbered sub-step gate structure (C-23)
**Changes from v5:** Added C-21 (formula verification as correction loop), C-22 (single-topic-
derivability test for cross-topic insight), C-23 (numbered sub-steps in multi-condition gates);
aspirational pool grows from 12 to 15; scoring formula updated.

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

### ASPIRATIONAL (15)

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

---

## Scoring Formula

```
score = (essential_pass/5 × 60)
      + (recommended_pass/3 × 30)
      + (aspirational_pass/15 × 10)
```

**Golden threshold:** all 5 essential pass **and** composite score ≥ 80.

**Notes on PARTIAL:**
- PARTIAL counts as 0 for scoring purposes.
- A PARTIAL on any essential criterion is a gate failure regardless of composite score.
```
