Reading the scorecard carefully across all five variations for patterns not yet captured in v2.

**New excellence patterns identified:**

**C-13** — From V-03: The cross-topic insight isn't just stated as prose — it gets a named title (`**TEAM INSIGHT — [descriptive name]:**`), making it a referenceable artifact rather than an embedded observation. This upgrades C-10's existence requirement to a naming requirement.

**C-14** — From V-04 (strongest C-12 signal): The stagnation patterns in anti-inertia framing are drawn from a pre-existing named registry (`[PATTERN_LABEL from registry]`), not invented inline. Registry-backed vocabulary prevents label drift across runs and builds a team-legible vocabulary over time.

**C-15** — From V-04 and V-05 (partial): When a gate fails, the error message names the specific instance that triggered the failure — not just "halt" but "GATE-B: topic X missing → halt." This creates a self-documenting failure trace the operator can act on without re-reading the full output.

---

```markdown
# corps-achievements Rubric — v3

**Updated:** 2026-03-16
**Basis for upgrade:** R2 scorecard — excellence signals from V-01 (100), V-03 (100), V-04 (100)
**Changes from v2:** Added C-13 (named-insight artifact), C-14 (registry-backed stagnation vocabulary),
C-15 (gate failure names failing instance); aspirational pool grows from 4 to 7; scoring formula updated.

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

### ASPIRATIONAL (7)

| ID | What it checks |
|----|----------------|
| C-09 | "1 away" quantified close-to-unlock callouts — dedicated section with exact count and exact thing needed |
| C-10 | Cross-topic or cross-contributor insight stated as a named conclusion — and that conclusion differs from any stagnation pattern or gap statement already made |
| C-11 | Skill includes at least one inline pre-write self-test gate — a verification question or confirmation statement the model must answer before generating a section (e.g., "Does this next action name the exact achievement it unlocks?") |
| C-12 | Next actions use anti-inertia framing: each action names not only what it unlocks but what stagnation pattern it breaks — format `[Action] → Unlocks [Achievement] → Breaks [Pattern]` |
| C-13 | The cross-topic insight (C-10) is formatted as a titled, named artifact — `**TEAM INSIGHT — [descriptive name]:**` — making it referenceable by name rather than embedded in prose |
| C-14 | Stagnation patterns referenced in anti-inertia actions (C-12) are drawn from a pre-existing named registry, not invented inline — enforced via label syntax such as `[PATTERN_LABEL from registry]`, preventing vocabulary drift across runs |
| C-15 | When a gate check fails, the error message names the specific instance that triggered the failure (topic name, contributor name, or action row) — not just "halt" but "GATE-B: [topic X] missing → halt" — creating a self-documenting failure trace |

---

## Scoring Formula

```
score = (essential_pass/5 × 60)
      + (recommended_pass/3 × 30)
      + (aspirational_pass/7 × 10)
```

**Golden threshold:** all 5 essential pass **and** composite score ≥ 80.

**Notes on PARTIAL:**
- PARTIAL counts as 0 for scoring purposes.
- A PARTIAL on any essential criterion is a gate failure regardless of composite score.

---

## Upgrade Notes

### v1 → v2

| Change | Rationale |
|--------|-----------|
| Added C-11 (pre-write self-test gate) | V-03 (R1 score 100): structural self-enforcement, not just a satisfied criterion |
| Added C-12 (anti-inertia action framing) | V-04 (R1 score 90): framing that names the stagnation pattern broken, not just the unlock |
| Refined C-10 uniqueness constraint | Named conclusion must differ from stagnation patterns already stated |
| Refined C-02 failure mode label | "Omitting a topic is a PHASE 2 gate failure" — named failure mode, not just positive requirement |
| Aspirational pool: 2 → 4 | Scoring formula denominator updated accordingly |

### v2 → v3

| Change | Rationale |
|--------|-----------|
| Added C-13 (named-insight artifact) | V-03 (R2 score 100): `**TEAM INSIGHT — [name]:**` upgrades C-10 from existence to referenceable artifact |
| Added C-14 (registry-backed stagnation vocabulary) | V-04 (R2 score 100): strongest C-12 signal — `[PATTERN_LABEL from registry]` prevents label invention at write time |
| Added C-15 (gate failure names failing instance) | V-04 + V-05 (R2): failure message names the specific topic/contributor that triggered halt, enabling operator action without re-reading full output |
| Aspirational pool: 4 → 7 | Scoring formula denominator updated accordingly |
```
