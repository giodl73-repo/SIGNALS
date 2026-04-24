Rubric written to `simulations/quest/rubrics/topic-status-rubric-2026-03-14.md`.

**Structure:**

- **4 Essential (60 pts):** Signal discovery (C-01), coverage percentage (C-02), gap identification (C-03), display-only behavior (C-04)
- **3 Recommended (30 pts):** Readiness verdict (C-05), namespace breakdown (C-06), strategy cross-reference (C-07)
- **2 Aspirational (10 pts):** Recency awareness (C-08), actionable next step (C-09)

**Key design decisions:**
- C-04 (display-only) is an automatic zero if failed — it's the defining contract of this skill vs. `topic-report`
- C-02 has a second fail condition: a percentage that contradicts the visible gap list also fails, catching hallucinated math
- C-07 makes strategy.md cross-reference explicit — a skill that computes coverage against zero without warning is misleading
least one globbed path or explicitly states zero signals found. No hard-coded or fabricated signal list. |
| C-02 | **Coverage percentage** — A numeric coverage figure is computed and displayed (e.g. "7 / 12 planned signals -- 58%"). | essential | correctness | A percentage or fraction is visible in the output. Must be derived from discovered vs. planned counts, not asserted without evidence. |
| C-03 | **Gap identification** — Signals planned in strategy.md but not yet present on disk are listed as open gaps. | essential | coverage | At least one gap section exists. If all planned signals are present, output explicitly states "no gaps". Gaps are named (namespace + signal type), not just counted. |
| C-04 | **Display-only behavior** — The skill writes nothing to disk. No file is created or modified. | essential | behavior | After execution, `git status` shows no new or modified files. Output is terminal-only. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-05 | **Readiness verdict** — Output provides a clear readiness signal for the stated target outcome (e.g. "NOT READY -- 3 essential gaps remain", "READY -- all scout + draft signals present"). | recommended | depth | A readiness label or verdict is present and connected to the gap list. Not just a coverage number -- a qualitative judgment. |
| C-06 | **Namespace breakdown** — Coverage is shown per namespace (scout, draft, review, flow, trace, prove, listen, program, topic), not only as a single aggregate. | recommended | format | At least namespace-level grouping visible in output. Namespaces with zero signals are shown as empty, not omitted. |
| C-07 | **Strategy cross-reference** — Output names the strategy.md file used as the planned-signal baseline and notes if strategy.md is missing or has no planned signals for this topic. | recommended | correctness | strategy.md reference appears in output. If missing, output says so explicitly rather than silently computing against zero. |

---

## Aspirational Criteria (10 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-08 | **Recency awareness** -- Output flags signals older than a configurable threshold (default: 30 days) as potentially stale, so coverage is not overstated by outdated evidence. | aspirational | depth | At least one signal is annotated with its age, or a staleness summary is shown. Does not require every signal to be dated -- a summary is sufficient. |
| C-09 | **Actionable next step** -- Output recommends the single highest-priority gap to close next, with the skill invocation that would produce it (e.g. "Run /scout:feasibility to fill scout-feasibility gap"). | aspirational | depth | A concrete "next step" line appears, naming a specific skill. Must match an open gap -- not a generic suggestion. |

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01, C-02, C-03, C-04 | 60 (15 each) |
| Recommended | C-05, C-06, C-07 | 30 (10 each) |
| Aspirational | C-08, C-09 | 10 (5 each) |

**Minimum passing**: all 4 essential pass + composite >= 80.

**Automatic fail conditions**:
- C-04 fails (file written to disk): skill violates its own contract, score = 0
- Coverage percentage present but visibly wrong (e.g. 100% when gaps are listed): C-02 fails regardless of other scores
