Written to `simulations/quest/rubrics/signal-setup-rubric-v14-2026-03-17.md`.

Here is the complete updated rubric:

---

```markdown
---
skill: quest-rubric
skill_target: signal-setup
date: 2026-03-17
version: 14
---

# Scoring Rubric: signal-setup
```

**What changed in v14 (from v13):**

Three new aspirational criteria extracted from the Round 15 scorecard, plus C-31 and C-32 which were already in the v13 spec file:

| ID | Pattern | Source | Key distinction |
|----|---------|--------|-----------------|
| C-31 | Sub-gate identifier scheme is fully uniform | Prior round | Separate from C-25 (lineage encoding): C-25 says *carry* lineage; C-31 says *all gates use the same convention* |
| C-32 | Consequence anchors are syntactically complete propositions | Prior round | Prerequisite for C-33/C-34: a phrase fragment can't be scored for adversary or causal structure |
| C-33 | Decline anchors name the adversary as the **winning party** | V-02 PASS on C-16 | "Inertia wins" vs "inertia remains unaddressed" — C-14 names what's forfeited; C-33 names who collects it |
| C-34 | Consequence anchors express a **two-step causal chain** | V-02 decline text | "spec committed without named competitor" → "question never gets asked" — passes C-32 but requires both links |
| C-35 | Routing blocks use `Route:` label + one-branch-per-line | V-03 structural improvement | Passes C-29 (completeness) but adds machine-parseable convention independent of prose quality |

**Denominator: A=32 → A=35**

The C-31/C-32/C-33 triad has a dependency order: C-32 is a prerequisite gate — a fragment that fails C-32 is disqualified from reaching C-33 or C-34. Scorers should evaluate C-32 first when any anchor is ambiguous.
