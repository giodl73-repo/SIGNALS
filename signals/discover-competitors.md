Produce a competitive brief that leads with strategy, not a matrix.

SETUP: Auto-detect domain from repo context (README, CLAUDE.md, package.json). Identify
5-8 competitors by name. Do not prompt the user unless repo context is completely absent.

THE PRIMARY COMPETITOR: Before any named competitors, assess "none / status quo." Ask:
why do teams do nothing instead of using this tool?
Score threat: always HIGH. Inertia is the primary competitor.

NAMED COMPETITORS: For each competitor, assess:
- Feature overlap (HIGH/MEDIUM/LOW)
- Positioning (direct threat / complementary / adjacent)
- Overall threat: HIGH / MEDIUM / LOW

Use WebSearch to verify at least one key competitive claim per major competitor.
Cite the source inline (URL or publication name).

FINDINGS: Structure as a brief:
1. The Primary Competitor -- why inertia is the real threat
2. The Whitespace -- what no competitor owns (the uncontested space)
3. The Table Stakes -- what any entrant must have to be taken seriously
4. The Competitive Matrix -- supporting evidence (rows = competitors, columns = dimensions)
5. --mode risk -- "The cost of building the wrong thing": reframe for exec audiences
   who respond to risk quantification over feature comparison.

AMEND: List 3 specific adjustments. For each: what the user changes AND what changes
in the output.

Write artifact to simulations/discover/competitors/{topic}-competitors-{date}.md.
Include frontmatter: skill, topic, item, date, skill_version, input.