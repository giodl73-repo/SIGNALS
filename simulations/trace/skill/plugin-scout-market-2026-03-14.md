---
skill: trace-skill
topic: plugin
item: scout-market
date: 2026-03-14
skill_version: 0.1.0
input: simulations/draft/specs/signal-scout-2026-03-14.md
---

# /trace-skill -- scout-market

**Invocation**: `/scout-market "Signal plugin -- structured pre-build investigation methodology for development teams"`
**Scenario**: PM sizing market before all-hands launch, 5,000+ Microsoft developers

## Phase 1: Setup

Auto-detected product categories: developer tooling (CLI plugin, git-native), AI-assisted methodology, Claude Code plugin. Segments identified without prompting: (1) craftworks beachhead, (2) Microsoft internal, (3) External Claude Code, (4) Enterprise AI teams, (5) Independent devs. Roles: Strategy, PM, GTM. PASS.

## Phase 2: Execute

### TAM/SAM/SOM per segment

| Segment | TAM | SAM | SOM (Y1) | Revenue model |
|---------|-----|-----|-----------|--------------|
| S1: craftworks beachhead | 3.5M devs | 350K | 12K | Free (methodology lock-in) |
| S2: Microsoft internal | 50K eng | 12K | 1,500 | Free (internal, reference case) |
| S3: External Claude Code | 500K installs | 80K | 4,000 | Freemium ($10/mo custom roles) |
| S4: Enterprise AI teams | $18B market | $900M | defer Y1 | Enterprise seat ($25-75/mo) |
| S5: Independent devs | 4M AI devs | 200K | 3,000 | Free |

### Segment fit scoring (PM: pain/WTP/accessibility)

| Segment | Fit | GTM Difficulty | Rank Score |
|---------|-----|----------------|------------|
| S1: craftworks beachhead | 8.3 | 1.3 | 17.0 |
| S2: Microsoft internal | 6.0 | 2.3 | 13.7 |
| S3: External Claude Code | 6.3 | 3.7 | 12.6 |
| S5: Independent devs | 5.0 | 4.7 | 10.3 |
| S4: Enterprise AI teams | 6.7 | 8.0 | 8.7 |

## Phase 3: Findings

**Beachhead**: S1 -- craftworks beachhead. Highest fit (8.3), lowest GTM friction (1.3), zero competitive alternatives, reachable in Y1 with zero marketing spend. S4 (highest WTP) ranks last because 8.0 GTM difficulty cancels it in Y1.

**Sequencing**: S1 (prove it) -> S2 (amplify with proof) -> S3 (marketplace) -> S4 (defer Y2+)

**Y1 revenue target**: $40K ARR from S3 freemium. Primary value is ecosystem adoption and S4 reference case.

## Phase 4: Amend

1. Disaggregate S2 by team type (Power Platform, Azure DevEx, M365)
2. Add time-to-first-value as 4th fit dimension (Signal = <10 min for S1/S3)
3. Price-test S3 freemium assumption via prove:interview before launch

## Verdict

**Result**: USEFUL. Composite rank score produced non-obvious result: S4 high WTP killed by GTM difficulty. Beachhead rationale directly supports all-hands credibility ("already in use in craftworks").

### Findings Register

| ID | Finding | Severity |
|----|---------|----------|
| SF-04 | Spec mixes dollar TAM and headcount TAM -- needs unit standardization | MAJOR |
| SF-05 | Scoring scale (1-10, equal weights, composite=average) not defined in spec | MINOR |
| SF-06 | Artifact path `simulations/scout/market/{topic}-market-{date}.md` confirmed | INFO |
