Rubric written to `simulations/quest/rubrics/flow-throttle-rubric-v1-2026-03-15.md`.

**Structure:**

- **5 Essential** (60 pts) — bottleneck localization, backpressure trace, tier enumeration, UX per tier, burst path detection. These are the irreducible core: without them the output is speculation, not simulation.
- **3 Recommended** (30 pts) — retry-after gap analysis, cascading failure scenario, quantified thresholds. These separate a useful signal from a great one.
- **2 Aspirational** (10 pts) — mitigation+tradeoffs, severity ranking. Raise the bar once the essentials are stable.

**Key design decisions:**
- C-05 (burst paths) is essential, not recommended — initial outputs almost always miss burst analysis and focus only on steady-state throttle.
- C-08 (quantified thresholds) requires an actual number; qualitative-only descriptions fail. Numbers should come from Power Automate/Connector docs, not be invented.
- C-01+C-02 together enforce that this is a *trace*, not a summary — location + propagation chain required.
