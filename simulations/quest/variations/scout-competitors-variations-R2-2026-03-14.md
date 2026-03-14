---
skill: quest-variate
skill_target: scout-competitors
topic: plugin
date: 2026-03-14
round: 2
variations: 2
prior_leader: V-05 (85)
target: combine ES-01 + ES-02 + explicit WebSearch instruction
---

# Variations: scout-competitors Round 2

One target variation combining all excellence signals from Round 1.
Plus one challenger testing a different combination.

---

## V-06: Golden candidate (V-05 + ES-01 + ES-02 + WebSearch)

Axis: Combined -- narrative structure + inertia naming + risk section + WebSearch instruction

```
You are running /scout-competitors. Produce a competitive brief that leads with strategy,
not a matrix. The matrix is supporting evidence. The insight comes first.

SETUP: Auto-detect domain from repo context (README, CLAUDE.md, package.json). Identify
5-8 competitors by name. Do not prompt the user unless repo context is completely absent.

THE PRIMARY COMPETITOR: Before any named competitors, assess "none / status quo." Ask:
why do teams do nothing instead of using this tool? What makes inertia sticky? What would
make a team choose to keep doing nothing even after hearing about this product?
Score threat: always HIGH. Inertia is the primary competitor.

NAMED COMPETITORS: For each competitor, assess:
- Feature overlap (HIGH/MEDIUM/LOW)
- Positioning (direct threat / complementary / adjacent)
- Technical moat (what makes them defensible)
- Distribution (how they reach users)
- Overall threat: HIGH / MEDIUM / LOW

Use WebSearch to verify at least one key competitive claim per major competitor.
Cite the source inline (URL or publication name).

FINDINGS: Structure as a brief:
1. The Primary Competitor -- why inertia is the real threat (from setup above)
2. The Whitespace -- what no competitor owns (the uncontested space)
3. The Table Stakes -- what any entrant must have to be taken seriously
4. The Competitive Matrix -- supporting evidence (rows = competitors, columns = dimensions)
5. --mode risk -- "The cost of building the wrong thing": reframe for exec audiences
   who respond to risk quantification over feature comparison. What does a team lose by
   NOT investigating before they build?

AMEND: List 3 specific adjustments. For each: what the user changes AND what changes
in the output (e.g., "Narrow to SaaS-only competitors -- removes enterprise players,
tightens whitespace analysis to developer tooling segment").

Write artifact to simulations/scout/competitors/{topic}-competitors-{date}.md.
Include frontmatter: skill, topic, item, date, skill_version, input.
```

---

## V-07: Challenger (V-04 traffic-light + ES-01 + WebSearch)

Axis: Traffic-light format + inertia naming + WebSearch -- test if format preference matters

```
You are running /scout-competitors. Use traffic-light assessments. Lead with The Primary
Competitor.

SETUP: Auto-detect domain. Identify 5-8 competitors. Do not prompt unless context absent.

THE PRIMARY COMPETITOR: Assess "none / status quo" first. Why do teams do nothing?
Score overall threat: always HIGH.

NAMED COMPETITORS: Assess each with traffic-light dimensions:
- Feature overlap: HIGH / MEDIUM / LOW
- Positioning threat: HIGH / MEDIUM / LOW
- Technical moat: HIGH / MEDIUM / LOW
- Distribution: HIGH / MEDIUM / LOW
- Overall threat: HIGH / MEDIUM / LOW

Use WebSearch to verify at least one claim per major competitor. Cite source.

FINDINGS:
1. The Primary Competitor (inertia analysis)
2. Whitespace (where all competitors score LOW)
3. Table stakes (features all HIGH-threat competitors have)
4. Competitive Matrix (traffic-light table)
5. --mode risk: cost of not acting, for exec audiences

AMEND: 3 specific adjustments with output impact.

Artifact: simulations/scout/competitors/{topic}-competitors-{date}.md with frontmatter.
```
