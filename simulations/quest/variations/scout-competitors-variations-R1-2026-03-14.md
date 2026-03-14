---
skill: quest-variate
skill_target: scout-competitors
topic: plugin
date: 2026-03-14
round: 1
variations: 5
---

# Variations: scout-competitors Round 1

Test invocation: `/scout-competitors "Signal plugin -- structured pre-build investigation for development teams"`
Repo context: C:\src\sim

---

## V-01: Baseline (spec as written)

Axis: Baseline -- all 4 roles in spec order (PM, Strategy, Architect, GTM)

```
You are running /scout-competitors. Given a product concept, analyze the competitive
landscape by running 4 roles (PM, Strategy, Architect, GTM) through their lenses.

SETUP: Infer product domain from repo context. Identify 5-10 competitors by name.
Always include "none / status quo" as a competitor row. If context is insufficient,
ask the user for a one-line domain description.

EXECUTE:
- PM: Score feature parity for each competitor (1-10)
- Strategy: Score positioning gap (is there clear whitespace?)
- Architect: Score technical moat (what makes this defensible?)
- GTM: Score distribution advantage (how hard to reach customers?)

FINDINGS: Highlight whitespace. List table stakes. Assess threat level per competitor.

AMEND: List 3 things the user can change. For each: what changes in the output.

Write artifact to simulations/scout/competitors/{topic}-competitors-{date}.md with
standard frontmatter.
```

---

## V-02: Inertia-first (reorder -- start with "none", build from there)

Axis: Role sequence -- lead with the inertia finding, then build competitive context

```
You are running /scout-competitors. The most important competitor is always "none" --
teams that skip pre-build investigation entirely. Start there.

SETUP: Infer domain from repo context. Auto-detect without prompting.

EXECUTE: Build the competitive picture in this order:
1. None / status quo: WHY do teams do nothing? What makes inertia sticky?
   Score threat: always HIGH. This is the primary competitor.
2. Named competitors (5-8): Score each on feature parity, positioning gap,
   technical moat, distribution. Flag as complementary, direct, or adjacent.
3. Whitespace: What no competitor owns.

FINDINGS: Lead with the inertia analysis. Then whitespace. Then the competitive matrix.
Table stakes last (what any entrant must have).

AMEND: 3 specific adjustments with impact.

Artifact: simulations/scout/competitors/{topic}-competitors-{date}.md with frontmatter.
```

---

## V-03: Role-reduced (PM + Strategy only, remove technical roles)

Axis: Stock role selection -- test whether removing Architect and GTM improves focus

```
You are running /scout-competitors for a PM audience. Use 2 roles: PM and Strategy.

SETUP: Auto-detect domain from repo context without prompting.

EXECUTE:
- PM: Feature parity matrix (what does each competitor do vs. what we propose?)
- Strategy: Positioning analysis (where is the whitespace? what is the differentiation story?)

FINDINGS: Competitive matrix. Whitespace. Positioning recommendation. Table stakes.
Threat level per competitor. Inertia as a competitor row.

AMEND: 3 adjustments with impact.

Artifact: simulations/scout/competitors/{topic}-competitors-{date}.md with frontmatter.
```

---

## V-04: Traffic-light format (replace numeric scoring with HIGH/MEDIUM/LOW)

Axis: Output format -- test whether traffic-light format is more readable than 1-10 scores

```
You are running /scout-competitors. Produce a competitive brief using traffic-light
assessment, not numeric scores.

SETUP: Auto-detect domain. Include "none / status quo" row. Identify 5-8 competitors.

EXECUTE: For each competitor (including "none"), assess:
- Feature overlap: HIGH (direct), MEDIUM (partial), LOW (minimal)
- Positioning threat: HIGH (competes for same decision), MEDIUM (adjacent), LOW (complementary)
- Technical moat: HIGH (hard to replicate), MEDIUM (replicable in 6mo), LOW (easily copied)
- Distribution: HIGH (already in front of our users), MEDIUM (reachable), LOW (different channel)
- Overall threat: HIGH / MEDIUM / LOW

FINDINGS: Whitespace (where all competitors are LOW). Table stakes (features all HIGH competitors have).
Inertia analysis. --mode risk reframing for exec audiences.

AMEND: 3 specific adjustments with impact.

Artifact: simulations/scout/competitors/{topic}-competitors-{date}.md with frontmatter.
```

---

## V-05: Narrative-first (prose positioning statements before matrix)

Axis: Lifecycle emphasis -- findings-first structure, matrix is supporting evidence

```
You are running /scout-competitors. Lead with the strategic insight, use the matrix
as supporting evidence.

SETUP: Auto-detect domain. Include "none / status quo". Identify 5-8 competitors.

EXECUTE: Run all 4 roles (PM, Strategy, Architect, GTM). Collect their raw assessments.

FINDINGS: Structure as a brief, not a matrix:

1. The Primary Competitor (why inertia is the real threat)
2. The Whitespace (the specific unowned space)
3. The Table Stakes (what any entrant must ship)
4. The Matrix (supporting evidence for the above three claims)
5. Threat summary (1-2 sentences per competitor)
6. --mode risk: "The cost of building the wrong thing" framing for exec audiences

AMEND: 3 specific adjustments with impact.

Artifact: simulations/scout/competitors/{topic}-competitors-{date}.md with frontmatter.
```
