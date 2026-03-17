Looking at the scorecard, I'll extract the excellence patterns that distinguish V-03 (100) and V-04 (90) from the others, then emit the full v2 rubric.

**Patterns identified:**

1. **V-03 C-05** — Pre-write self-test gate: before generating next-actions, the skill asks "Does it name the exact achievement or milestone it unlocks?" This is structural self-enforcement, not just a criterion the output satisfies.

2. **V-04 C-05** — Anti-inertia action framing: next actions include the stagnation pattern they break (`[Action] → Unlocks [Achievement] → Breaks [Stagnation Pattern]`), not just the unlock. Stronger motivational signal.

3. **V-03 C-02** — Named failure mode labels: "Omitting a topic is a PHASE 2 gate failure" — the skill names the failure mode explicitly, not just the positive requirement.

4. **V-04 C-10** — Insight uniqueness constraint: team insight "must differ from the stagnation pattern statement" — ensures the insight adds net-new information rather than restating what was already said.

Items 3 and 4 are refinements to existing criteria (C-02, C-10); items 1 and 2 are genuinely new patterns worth adding as C-11 and C-12.

---

```markdown
# corps-achievements Rubric — v2

**Updated:** 2026-03-16  
**Basis for upgrade:** R1 scorecard — excellence signals from V-03 (score 100) and V-04 (score 90)  
**Changes from v1:** Added C-11 (pre-write self-test gate) and C-12 (anti-inertia action framing); aspirational pool grows from 2 to 4; scoring formula updated accordingly.

---

## Criteria

### ESSENTIAL (5) — all must pass

| ID | What it checks |
|----|---------------|
| C-01 | Artifact scan grounded in real workspace files — no hallucinated topics |
| C-02 | Every discovered topic appears in achievements output |
| C-03 | All three named milestones present by name (first team signal, shared coverage, debate starter) |
| C-04 | Contributor leaderboard section exists and is populated |
| C-05 | Next actions name both the action AND the achievement it unlocks |

---

### RECOMMENDED (3)

| ID | What it checks |
|----|---------------|
| C-06 | Earned vs. available achievements visually separated |
| C-07 | Achievements grouped into at least 2 categories |
| C-08 | Sprint/date framing present in output |

---

### ASPIRATIONAL (4)

| ID | What it checks |
|----|---------------|
| C-09 | "1 away" quantified close-to-unlock callouts — dedicated section with exact count and exact thing needed |
| C-10 | Cross-topic or cross-contributor insight stated as a named conclusion — and that conclusion differs from any stagnation pattern or gap statement already made |
| C-11 | Skill includes at least one inline pre-write self-test gate — a verification question or confirmation statement the model must answer before generating a section (e.g., "Does this next action name the exact achievement it unlocks?") |
| C-12 | Next actions use anti-inertia framing: each action names not only what it unlocks but what stagnation pattern it breaks — format `[Action] → Unlocks [Achievement] → Breaks [Pattern]` |

---

## Scoring Formula

```
score = (essential_pass/5 × 60)
      + (recommended_pass/3 × 30)
      + (aspirational_pass/4 × 10)
```

**Golden threshold:** all 5 essential pass **and** composite score ≥ 80.

**Notes on PARTIAL:**
- PARTIAL counts as 0 for scoring purposes.
- A PARTIAL on any essential criterion is a gate failure regardless of composite score.

---

## Upgrade Notes (v1 → v2)

| Change | Rationale |
|--------|-----------|
| Added C-11: pre-write self-test gate | V-03 achieved the only 100 score; its C-05 used an inline verification question that prevented weak output structurally, not just aspirationally. Pattern is generalisable beyond C-05. |
| Added C-12: anti-inertia action framing | V-04 explicitly named the stagnation pattern each action breaks. Scored as "strongest of all variations" by the scorer. Adds motivational framing absent in all other variates. |
| Aspirational pool: 2 → 4 | Scoring formula denominator updated from `/2` to `/4` to preserve aspirational weight at 10 total points. Each criterion now contributes 2.5 points to the composite. |
| C-10 clarification (no file change) | V-04 introduced a uniqueness constraint: insight must differ from stagnation pattern statement. This nuance is now reflected in C-10's description without changing its identity. |
```
