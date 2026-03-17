Reading the scorecard carefully across both variations for patterns not yet captured in v3.

**New excellence patterns identified:**

**C-16** — From V-01 (Phase 3) and V-02 (Step 4): The contributor leaderboard uses an explicit weighted scoring formula (Signals×1 + Topics×3 + Milestones×5), not just a rank-ordered count. The formula makes each contributor's score auditable from raw counts and encodes the team's value judgment about signal types — making the ranking debatable rather than opaque.

**C-17** — From V-01 (Phase 4): The stagnation pattern labels use semantic names that encode the pattern type without requiring a definition lookup (SOLO_ISLAND, NAMESPACE_MOAT, SPRINT_FREEZE, ORPHAN_TOPIC). An opaque code like PATTERN_1 does not satisfy this. Readable labels compress lookup cost and let the anti-inertia actions (C-12) be self-interpreting at a glance.

**C-18** — From V-02 (Step 5): The 1-away callout (C-09) is rendered as a structured table with distinct columns for at minimum topic/target, achievement to unlock, gap (what's missing), and exact action needed. A prose "almost there" section can omit fields for individual entries; a table cannot — every row must be complete.

---

```markdown
# corps-achievements Rubric — v4

**Updated:** 2026-03-16
**Basis for upgrade:** R3 scorecard — excellence signals from V-01 (89), V-02 (partial scored)
**Changes from v3:** Added C-16 (weighted leaderboard formula), C-17 (semantic stagnation labels),
C-18 (1-away structured table); aspirational pool grows from 7 to 10; scoring formula updated.

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

### ASPIRATIONAL (10)

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

---

## Scoring Formula

```
score = (essential_pass/5 × 60)
      + (recommended_pass/3 × 30)
      + (aspirational_pass/10 × 10)
```

**Golden threshold:** all 5 essential pass **and** composite score ≥ 80.

**Notes on PARTIAL:**
- PARTIAL counts as 0 for scoring purposes.
- A PARTIAL on any essential criterion is a gate failure regardless of composite score.

---

## Upgrade Notes

### v3 → v4

Scorecard basis: R3, V-01 (89) and V-02 (partial).

Three new aspirational criteria extracted from R3 excellence signals:

- **C-16** (weighted leaderboard formula): Both V-01 and V-02 used an explicit point-weight formula
  for the leaderboard rather than raw counts. The formula surfaces the team's value judgment and
  makes ranking auditable — a plain rank list does not satisfy this.

- **C-17** (semantic stagnation labels): V-01 defined SOLO_ISLAND, NAMESPACE_MOAT, SPRINT_FREEZE,
  ORPHAN_TOPIC. Each label is self-interpreting without a definition lookup. This upgrades C-14's
  registry-existence requirement to a readability requirement on the labels themselves.

- **C-18** (1-away structured table): V-02's Step 5 used a four-column table (Topic | Achievement |
  Gap | Exact Action Needed) rather than prose. A table enforces field completeness per row in a
  way prose cannot — any missing field creates a visible blank cell.

Aspirational pool: 7 → 10. Scoring formula denominator updated accordingly.

### v2 → v3

Scorecard basis: R2, V-01 (100), V-03 (100), V-04 (100).

Three new aspirational criteria extracted from R2 excellence signals:

- **C-13** (named-insight artifact): upgrades C-10's existence requirement — the cross-topic
  insight must carry a titled header making it referenceable by name.

- **C-14** (registry-backed stagnation vocabulary): stagnation pattern labels must come from a
  pre-existing named registry, not be invented inline, enforced via `[PATTERN_LABEL from registry]`
  syntax.

- **C-15** (gate failure names failing instance): gate error messages must name the specific topic,
  contributor, or action row that triggered the failure, not just emit a generic halt signal.

Aspirational pool: 4 → 7. Scoring formula denominator updated accordingly.

### v1 → v2

Scorecard basis: R1 (details in prior session).

Added C-09 (1-away callouts), C-10 (cross-topic insight), C-11 (inline pre-write gates),
C-12 (anti-inertia framing). Aspirational pool: 0 → 4. Scoring formula introduced.
```
