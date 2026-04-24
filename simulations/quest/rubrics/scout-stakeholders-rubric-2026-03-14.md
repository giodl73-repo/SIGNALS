Rubric written to `simulations/quest/rubrics/scout-stakeholders-rubric-2026-03-14.md`.

**5 essential, 3 recommended, 2 aspirational** — here's what drove each decision:

**Essential** (the output is not useful without these):
- **C-01** — The CODEOWNERS fallback is the core behavioral contract of the skill. Silent org inference is the named failure mode in the spec.
- **C-02** — Power/Interest grid is the primary deliverable; without it there's nothing.
- **C-03** — Veto risks ranked by probability is explicitly listed in the skill spec as a required output.
- **C-04** — Champion activation with a *concrete action* (not "engage") is what makes this actionable vs. decorative.
- **C-05** — Communication strategy per quadrant with timing is the second primary deliverable.

**Recommended** (makes the output substantially better):
- **C-06** — Conflict identification is where Strategy role earns its value; surfacing the exec/user framing split was the hardest insight in the trace.
- **C-07** — Explicit role framing (PM/Strategy/UX) ensures the three stock roles are actually applied.
- **C-08** — Critical-path gating is distinct from quadrant placement; the trace specifically called out this gap (agenda coordinator owns the slot, Security Review blocks the launch).

**Aspirational** (raises the bar):
- **C-09** — Amendment phase catches what initial analysis missed (splitting "all developers" into bulk vs. early adopter segment was the key trace finding).
- **C-10** — Negative-space framing for gatekeepers ("what we are NOT doing") was listed as a Phase 4 amendment in the trace — useful but only matters once essentials are stable.
ity + impact. Order must reflect probability rank, not alphabetical or grid-order. |
| C-04 | **Champion identified** — At least one stakeholder is explicitly designated as champion, with a concrete activation action (not just "engage"). | correctness | One or more stakeholders labelled champion with a specific action (e.g., "give demo slot", "co-present", "early access"). Generic "engage champion" language = FAIL. |
| C-05 | **Communication strategy per quadrant** — Output maps a communication approach to each quadrant (keep satisfied / engage / inform / champion), including message framing and timing. | depth | Four quadrant rows are present in the strategy, each with a distinct message and at least a relative timing signal (e.g., "3 weeks before", "now", "day of"). |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Conflict identification** — Output surfaces at least two conflicts between stakeholder groups (e.g., exec framing vs. user framing, gatekeeper inertia vs. event deadline). | depth | Two or more distinct conflicts named, each identifying the stakeholder groups in tension and the nature of the conflict. Single-stakeholder risks do not count as conflicts. |
| C-07 | **Role framing** — PM, Strategy, and UX stock roles are applied: PM owns power/interest mapping, Strategy surfaces conflicts, UX identifies journey implications or experience-path concerns. | coverage | All three roles are invoked or their perspective is traceable in the output. May be implicit if the output structure clearly separates these concerns. Roles absent or collapsed = FAIL. |
| C-08 | **Critical-path gatekeepers flagged** — Any stakeholder whose scheduling or approval constrains the launch timeline is called out on the critical path, not just placed in the keep-satisfied quadrant. | correctness | At least one gatekeeper explicitly tagged as critical-path with a deadline or lead-time note (e.g., "Security Review must start 2 weeks before slot confirmation"). |

---

## Aspirational Criteria (10 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Amendment phase** — Output includes at least one finding that was not evident from the initial stakeholder list, discovered through analysis (e.g., a downstream segment within a bulk group, a missing actor, a reframe of the message for a gatekeeper). | depth | A distinct amendment, finding, or "what we missed" item that adds a stakeholder, splits an existing group, or reframes an action based on analysis -- not restating something already in the grid. |
| C-10 | **"What we are NOT doing" framing** — For compliance or security gatekeepers, output provides a concise negative-space summary: what data the tool does not collect, what it does not do, to reduce review friction. | coverage | At least one sentence or table row explicitly addresses a gatekeeper's likely concern by describing what the product does not do. Absence = partial credit not awarded. |

---

## Scoring Reference

| Result | Meaning |
|--------|---------|
| All C-01..C-05 pass | Essential gate cleared |
| Composite >= 80 | Golden threshold met |
| Any essential fails | Output not useful regardless of total score |

```
Example: C-01..C-05 pass (60), C-06+C-07 pass (20), C-09 pass (5) = 85 -> GOLDEN
Example: C-03 fails = essential gate broken -> NOT GOLDEN even if composite is high
```
