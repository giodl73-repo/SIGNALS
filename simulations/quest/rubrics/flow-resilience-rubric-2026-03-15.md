Written to `simulations/quest/rubrics/flow-resilience-rubric-v1-2026-03-15.md`.

**Structure:**

- **5 essential** (60%): scenario coverage (3 degradation classes), four-field structure per scenario, gap identification (3 named types), distributed systems accuracy, commerce domain grounding
- **3 recommended** (30%): severity + blast-radius classification, recovery path specificity with actor labels, conflict resolution strategy adequacy judgment for eventual consistency
- **2 aspirational** (10%): chaos engineering test cases (injectable, observable, pass/fail), observability hooks tied to named gaps

**Design decisions:**
- C-01 enforces all three degradation classes the skill names explicitly — outputs that only cover offline or only cover eventual consistency are structurally incomplete
- C-02 is the spine — the four-field structure (state / capability / data-at-risk / recovery) is the literal definition of what this skill produces, so it's essential and evaluated per-scenario
- C-03 catches the three named output targets (offline gaps, consistency violations, missing recovery flows) — all three must appear as distinct findings, not bundled
- C-07 adds actor labels to recovery paths (client / server / operator / user) to close the gap between "system recovers" and actionable triage
- Failure fast-paths catch the most common failure modes: pure prose, domain-agnostic analysis, trivial identical recovery paths, and missing degradation class coverage
