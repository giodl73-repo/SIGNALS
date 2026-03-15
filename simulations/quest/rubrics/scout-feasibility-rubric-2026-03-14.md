Rubric written to `simulations/quest/rubrics/scout-feasibility-rubric-2026-03-14.md`.

---

**Design notes:**

The 5 essential criteria are anchored directly to the three trace findings:

- **C-01/C-02** — the core deliverable (traffic lights + score+label). Without these the output is structurally useless.
- **C-03** maps to **SF-03** — explicit inference disclosure for team/timeline. The skill description calls this out as a hard requirement ("never silently infer").
- **C-04** maps to **SF-01** — stack fallback must be disclosed, not silent.
- **C-05** maps to **SF-02** — RED blockers must carry rationale, not just a color.

The recommended criteria add the Strategy layer (C-06), the scoped-fallback pattern (C-07 — which the trace demonstrates by splitting 38/100 full vs 62/100 scoped), and prerequisites (C-08).

The aspirational criteria reward PM-quality hour budgeting (C-09) and a closing amendment list (C-10) — both present in the trace's Phase 3/4 but not expected from a baseline run.

**Scoring**: A run that hits all 5 essential + all 3 recommended scores 90 — above the 80 golden threshold even with no aspirational points.
hard fail. |
| C-04 | Stack inference disclosed when canonical files absent | essential | correctness | When no package.json / tsconfig.json / Cargo.toml is found, output contains an explicit disclosure sentence naming the fallback source (CLAUDE.md, program.yaml, etc.) and stating what was inferred from it. |
| C-05 | RED blockers enumerated with rationale | essential | coverage | Every RED-rated component is listed in a dedicated blockers section or inline note explaining *why* it is a blocker and what would need to change to lift the rating. |

### Recommended (30 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-06 | Build-vs-buy recommendation per component | recommended | depth | At least 50% of components carry a Build / Buy / Use existing label. The Strategy role (or equivalent framing) must be attributed or implied. |
| C-07 | Scoped fallback score when full scope is infeasible | recommended | depth | When overall score is below 50 (NOT FEASIBLE), output includes a scoped alternative score with the constraint that enables it (e.g., "Scoped to flat binding only: 62/100"). Omitting this when blockers exist is a fail. |
| C-08 | Prerequisites listed for conditional feasibility | recommended | coverage | When score is FEASIBLE with caveats, output contains a numbered or bulleted prerequisite list. All RED-rated items must be represented. |

### Aspirational (10 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-09 | PM timeline overlay with hour budget comparison | aspirational | depth | Output contains an estimated-hours figure for the full scope and compares it to available hours for the inferred timeline and team size. Must flag over-budget or under-budget explicitly. |
| C-10 | Amendment actions list at close | aspirational | behavior | Output ends with a short action list (numbered) that converts RED findings into concrete next steps for the requesting team. Each action must be traceable to a specific RED or YELLOW component. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Common Failure Modes

Derived from trace findings:

| Finding | Criterion | Failure Pattern |
|---------|-----------|-----------------|
| SF-01 | C-04 | Skill falls back to CLAUDE.md assertion but never tells the user |
| SF-02 | C-05 | Missing canonical schema not flagged as blocker; Architect scores complexity without noting the gap |
| SF-03 | C-03 | "One sprint" used in calculations without a visible inference statement |
