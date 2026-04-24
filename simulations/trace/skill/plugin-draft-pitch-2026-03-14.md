---
skill: trace-skill
topic: plugin
item: draft-pitch
date: 2026-03-14
skill_version: 0.1.0
input: simulations/draft/specs/signal-draft-2026-03-14.md
prior_signals: [plugin-scout-competitors-w2, plugin-scout-positioning]
---

# /trace-skill -- draft-pitch

**Invocation**: `/draft-pitch "Signal" --audience "VP Engineering (all-hands sponsor)"`
**Scenario**: PM writing the all-hands pitch for Signal to the VP who will give them the slot

## Phase 1: Setup

Positioning context loaded from: plugin-scout-competitors-w2 (inertia as primary competitor),
plugin-scout-positioning (narrative-first structure, outcome-first framing).
Audience: VP Engineering -- cares about cost reduction, developer productivity, risk.
Does NOT want feature lists. Wants ROI and risk framing.

## Phase 2: Execute

**Strategy** crafts the narrative arc:

```
# Signal: Know What You Know Before You Commit

## The Problem (cost framing)
Your teams find design flaws after implementation starts.
Post-implementation design changes cost an average of 3 developer-weeks each.
At 5,000 engineers making feature decisions daily, this adds up.

## The Primary Competitor (insight)
The real competition isn't Cursor or Copilot.
It's the meeting that never happened, the spec that was never reviewed,
the compliance question that was never asked -- until week 6 of implementation.
The primary competitor is doing nothing. And right now, doing nothing wins by default.

## The Solution (outcome-first)
Signal gives every developer the investigation they needed before they started building.
Copy one file. Run one command. Get a competitive analysis, feasibility check, or
system trace in minutes -- not days.

The investigation that used to take 2 weeks now takes an afternoon.
The design bug that used to cost 3 developer-weeks gets caught before line one of code.

## The Proof
9 proven simulation techniques. 730+ scenarios of evidence from our own teams.
Teams using this methodology today catch 40% of design bugs before implementation.
ROI from documented campaigns: 7.5x.

## The Ask
30 minutes at the all-hands for a live demo.
Claude Code approval in IT tooling catalog (it's already approved in 3 teams).
One champion engineer to run the demo (we have two volunteers).
```

**PM** validates proof points:
- "730+ scenarios" -- confirmed from techniques/01-09 evidence
- "40% of design bugs" -- from Q01/Q02 research data
- "7.5x ROI" -- from flow:lifecycle analysis (60 dev-weeks caught vs 8 dev-weeks cost)
- "3 teams already approved" -- needs verification before all-hands (ACTION)

**Architect** calibrates technical depth for VP audience:
VP doesn't need to know about namespaces, bindings, or CREST.
The "copy one file" framing is correct -- validates P-05 (zero barrier).
The demo should show an artifact produced, not the CLI internals.

## Phase 3: Findings

Narrative gaps:
- "40% of design bugs" needs a source citation for the VP -- can't claim without evidence
- "3 teams already approved" is unverified -- needs PM action before pitch delivery

Audience calibration: PASS -- no jargon, outcome framing throughout.
Ask clarity: PASS -- 3 specific asks, all actionable.

## Phase 4: Amend

1. Add NPS/NSAT predictions from review:customers to strengthen "the proof" section
2. Verify "3 teams approved" claim before delivering
3. Add a one-sentence anti-positioning ("Signal is not another AI coding assistant")

## Verdict

**Result**: USEFUL and HIGH IMPACT. The pitch narrative is clean and VP-calibrated.
The "Primary Competitor is doing nothing" reframe is the strongest line -- use it to open.

### Findings Register
| ID | Finding | Severity |
|----|---------|----------|
| SF-01 | "40% design bugs" claim needs source before all-hands delivery | MAJOR |
| SF-02 | "3 teams approved" unverified -- PM action required | MAJOR |
| SF-03 | NPS/NSAT predictions from simulations should appear in "The Proof" | MINOR |
| SF-04 | Anti-positioning statement missing -- add before delivery | MINOR |
| SF-05 | Pitch connects naturally to goals:commit for VP sponsorship sign-off | DELIGHT |
