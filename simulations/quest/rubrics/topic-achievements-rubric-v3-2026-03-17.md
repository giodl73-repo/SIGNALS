Looking at the Round 2 scorecard, two patterns emerge that aren't yet criteria:

**From V-02**: The consequence clause names a specific evasion path — "including as a closing reflection" — not just the general rule. C-12 captures the consequence clause; it doesn't capture *naming the canonical violation surface inside the clause*.

**From V-03**: The escape hatch is framed as an unconditional minimum ("always acceptable and is the safe floor"), not just a conditional fallback ("when uncertain"). C-13 captures the fallback instruction; it doesn't capture the positive floor declaration that removes uncertainty about when the fallback applies.

These become C-14 and C-15. The scoring formula updates to `/7`.

---

# Quest Score Rubric — corps-achievements
**Version**: v3 (2026-03-17)

## What Changed in v3

**2 new aspirational criteria** extracted from Round 2 excellence signals:

- **C-14 (Failure-mode enumeration)** — from V-02's "including as a closing reflection" clause. C-12 requires a consequence clause; C-14 requires the consequence clause to name a specific canonical evasion path within itself. A rule that says "X fails this requirement" passes C-12. A rule that says "X — including the specific surface Y — fails this requirement" passes C-14.

- **C-15 (Unconditional evidence floor)** — from V-03's "Namespace-level evidence is always acceptable and is the safe floor." C-13 requires an escape hatch instruction triggered by uncertainty. C-15 requires that the fallback be declared as an unconditional minimum: always acceptable, not only when evidence is uncertain. The distinction is positive declaration versus conditional fallback.

**Scoring formula updated**: `aspirational_pass / 7 * 10` (was `/5`). Max composite remains 100.

---

## Tiers

| Tier | Criteria | Points | Formula |
|------|----------|--------|---------|
| Essential | C-01 – C-05 | 60 | `pass/5 × 60` |
| Recommended | C-06 – C-08 | 30 | `pass/3 × 30` |
| Aspirational | C-09 – C-15 | 10 | `pass/7 × 10` |
| **Total** | | **100** | |

## Scoring Formula

```
composite = (essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/7 × 10)
```

| Score | Grade |
|-------|-------|
| 100 | Platinum |
| 90–99 | Gold |
| 75–89 | Silver |
| < 75 | Bronze |

---

## Criteria

### Essential (C-01 – C-05)

**C-01 — One state per achievement**
Each achievement entry carries exactly one state value: EARNED, IN-PROGRESS, or LOCKED. Multi-state rows, ambiguous state, or missing state fail. Applies to both table and prose output formats.

**C-02 — Falsified named as honesty signal**
The Falsified achievement is present as a named entry. Its description frames falsification as evidence of investigative rigor ("followed evidence over assumptions" or equivalent), not as failure or absence.

**C-03 — Artifact-grounded classification**
State assignments cite source artifacts from Step 1 by namespace or skill. EARNED entries cite a specific artifact; IN-PROGRESS entries cite the partially-completed artifact or its count. Classification that cannot be traced to an artifact fails.

**C-04 — In-progress shows numeric progress**
IN-PROGRESS achievements express progress in `n of m` form (e.g., "3 of 5 namespaces covered"). Qualitative-only descriptions ("partially done", "underway") fail.

**C-05 — Next recommended action is specific**
Step 4 (or equivalent) names the next skill, the artifact it produces, and the achievement(s) it advances. Generic instructions ("continue the investigation") fail.

---

### Recommended (C-06 – C-08)

**C-06 — All 7 categories represented**
Every achievement category appears in the output. Categories with no earned or in-progress achievements are listed as LOCKED or explicitly noted as empty. Omitting a category fails.

**C-07 — Earned achievements carry dates**
EARNED entries include the date on which the achievement was earned. Date format may vary; absence of a date on an EARNED entry fails.

**C-08 — Locked achievements state unlock conditions**
LOCKED entries specify the concrete unlock condition: the artifact type, artifact count, or action required. "Not yet unlocked" without specifics fails.

---

### Aspirational (C-09 – C-15)

**C-09 — Maturity synthesis before classification**
The output includes a 1–3 sentence maturity synthesis covering overall investigation depth, coverage gaps, and signal quality. The synthesis appears before any per-category classification begins.

**C-10 — Falsified framed as positive signal**
The Falsified achievement is described in a way that frames it as a positive signal — an invitation or proof of rigor — not as a confession or gap. "Open invitation" and "proves the investigation was honest" are canonical framings.

**C-11 — State-column isolation**
In table-format output, state values occupy a dedicated column, not embedded in a prose evidence cell. Verification of C-01 is possible by scanning that column alone, without parsing any other cell.

**C-12 — Synthesis placement boundary**
The synthesis placement rule is encoded as an explicit boundary with a stated failure mode. The directive must name what constitutes violation (e.g., "Placement after per-category classification fails this requirement"). A positive-only directive ("write synthesis before categories") without a consequence clause fails.

**C-13 — Hallucination-safe evidence fallback**
When evidence is uncertain, the output provides a safe fallback: cite namespace or skill only rather than fabricating specifics. The escape hatch instruction is present and actionable.

**C-14 — Failure-mode enumeration**
At least one structural directive names a canonical evasion path within the constraint itself — not just the required behavior, but a specific surface where violation commonly occurs (e.g., "including as a closing reflection"). Stricter than C-12: C-12 requires a consequence clause; C-14 requires the consequence clause to name a specific failure mode. A consequence clause without an enumerated evasion surface passes C-12 and fails C-14.

**C-15 — Unconditional evidence floor**
The evidence fallback is declared as an unconditional minimum standard: namespace-level evidence is described as always acceptable, not only when uncertain. The distinction is positive declaration ("always acceptable and is the safe floor") versus conditional fallback ("when uncertain, cite namespace only"). A conditional-only escape hatch passes C-13 and fails C-15.

---

## Criterion Reference

| ID | Tier | What it tests |
|----|------|---------------|
| C-01 | Essential | One state per achievement |
| C-02 | Essential | Falsified named as honesty signal |
| C-03 | Essential | Artifact-grounded classification |
| C-04 | Essential | In-progress shows numeric progress |
| C-05 | Essential | Next recommended action present and specific |
| C-06 | Recommended | All 7 categories represented |
| C-07 | Recommended | Earned achievements carry dates |
| C-08 | Recommended | Locked achievements state unlock conditions |
| C-09 | Aspirational | Maturity synthesis before classification |
| C-10 | Aspirational | Falsified framed as positive signal |
| C-11 | Aspirational | State-column isolation |
| C-12 | Aspirational | Synthesis placement boundary |
| C-13 | Aspirational | Hallucination-safe evidence fallback |
| C-14 | Aspirational | Failure-mode enumeration |
| C-15 | Aspirational | Unconditional evidence floor |

---

## Round 2 Scoring Under v3

| Variate | Essential | Recommended | Aspirational passes | Composite | Grade |
|---------|-----------|-------------|---------------------|-----------|-------|
| V-01 | 5/5 → 60 | 3/3 → 30 | C-09, C-10, C-11 (3/7 → 4.3) | **94** | Gold |
| V-02 | 5/5 → 60 | 3/3 → 30 | C-09, C-10, C-12, C-14 (4/7 → 5.7) | **96** | Gold |
| V-03 | 5/5 → 60 | 3/3 → 30 | C-09, C-10, C-13, C-15 (4/7 → 5.7) | **96** | Gold |

V-02 and V-03 tie at 96, each passing a complementary pair (boundary+enumeration vs fallback+floor). No single variate passes all seven aspirational criteria — the Platinum score remains unreached, which is the correct structural condition for a rubric with live headroom.
