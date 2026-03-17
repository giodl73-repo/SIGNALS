Rubric written to `simulations/quest/rubrics/scout-risk-rubric-v1-2026-03-16.md`.

**5 essential, 3 recommended, 2 aspirational.**

Key design decisions:

- **C-01** (inertia first) is a hard structural rule — position matters, not just presence. This is the most distinctive requirement of this skill.
- **C-05** (specific mitigations) uses a "two or more fails" threshold to avoid penalizing a single weak mitigation in an otherwise strong register.
- **C-10** (AMEND) is aspirational because it only activates when the prompt includes an amendment directive — scoring it essential would make it untestable on base prompts.
- The "Quick Failure Modes" section at the bottom makes it easy to short-circuit scoring when an obvious essential fails early.
