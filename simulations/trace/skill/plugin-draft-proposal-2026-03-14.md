---
skill: trace-skill
topic: plugin
item: draft-proposal
date: 2026-03-14
skill_version: 0.1.0
input: simulations/draft/specs/signal-draft-2026-03-14.md
---

# /trace-skill -- draft-proposal

**Invocation**: `/draft-proposal "Signal delivery model: plugin vs. skills-in-repo vs. both"`
**Scenario**: PM drafts a proposal for the binding strategy after the decision was surfaced during design

## Phase 1: Setup

Scout artifacts found: competitors trace (skills-in-repo as primary recommendation),
feasibility trace (62/100 scoped). Stakeholder trace: not found -- inline assessment needed.
Decision framing: what delivery model maximizes adoption at the all-hands while preserving
team control?

## Phase 2: Execute

**PM** frames the decision:
"How should Signal be delivered to 5,000+ developers at the all-hands?"
Why now: all-hands is in 6 weeks. Delivery model affects install story, maintenance, and adoption.
Cost of inaction: shipping without a clear model means ad-hoc adoption and inconsistent experience.

**Strategy** presents 4 options:

| Dimension | A: Skills-in-repo | B: Plugin only | C: Both (phased) | D: CREST only |
|-----------|------------------|----------------|------------------|---------------|
| Install friction | Copy 1 file | Install plugin | Copy or install | Write CREST.md |
| Naming | /scout, /trace | /signal:scout | Both work | N/A |
| Customization | Fork the file | Hard to fork | Full range | High |
| Team control | Full (git) | Partial | Full | Full |
| Time to v0.1 | 6 weeks | 8 weeks | 10 weeks | 12 weeks |
| Audience fit | Dev-first | All-hands easy | Both | Power users |

**Architect** scores on technical dimensions:
- A: T2 body limit is the constraint (CF-03). Manageable with golden prompts.
- B: Colon syntax works in Claude Code but breaks on Windows filesystems (directory names).
- C: Same content, two packaging formats via craft generate. Adds 2-week overhead.
- D: CREST is Spec 109 -- not compiled yet. Experimental path.

Recommendation: **Option A (skills-in-repo) for v0.1, Option C (both) for v0.2.**
Confidence: HIGH. Conditions: (1) signal-install.sh ships with v0.1, (2) CF-01 frontmatter
bug fixed before demo, (3) golden prompts complete before all-hands.

## Phase 3: Findings

Assumption register:
- A1: CF-01 (double frontmatter) will be fixed -- validation plan: file issue, confirm fix ships
- A2: golden prompts for all 63 skills complete -- validation plan: quest-run-all.sh finishes
- A3: signal-install.sh ships -- validation plan: build it (FL-06 from flow:lifecycle trace)

Risk register:
- R1: Plugin format ready before v0.2 (colons on Windows) -- MEDIUM probability, HIGH impact
- R2: CREST experiment delays v0.1 scope -- LOW probability (CREST is v0.5)

## Phase 4: Amend

1. Add "Option E: Plugin manifest only (no skills-in-repo)" as a distinct option
2. Decision criteria weights need PM review -- currently equal weights
3. Add "community fork" consideration: skills-in-repo makes community contributions natural

## Verdict

**Result**: USEFUL. Proposal structure surfaces the binding decision cleanly.
SF-01: The "conditions" section is the most valuable part -- makes assumptions explicit.

### Findings Register
| ID | Finding | Severity |
|----|---------|----------|
| SF-01 | Assumption register is the key deliverable -- highlight it more prominently | MINOR |
| SF-02 | Option C (both) needs a clearer timeline -- "10 weeks" is vague | MINOR |
| SF-03 | Cross-reference to signal.bindings.md missing -- spec should link to it | MINOR |
