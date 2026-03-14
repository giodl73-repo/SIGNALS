---
skill: quest-golden
skill_target: scout-competitors
topic: plugin
date: 2026-03-14
rounds: 2
rubric_final: scout-competitors-rubric-v2-2026-03-14.md
score: 100
status: GOLDEN
---

# Golden Prompt: scout-competitors

Dual convergence achieved in Round 2.
Trial converged (5/5 essential pass) + Quest plateaued (no new excellence patterns).

---

## The Golden Prompt Body

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

## What Made It Golden

The 5 patterns that distinguish the golden prompt from the baseline (V-01):

1. **"THE PRIMARY COMPETITOR" naming** -- uppercase section title forces the narrative.
   "Why do teams do nothing?" is a question the skill must answer. This produces C-06
   and C-11 together.

2. **Narrative-first structure** -- findings ordered as Brief (insight) → Matrix (evidence),
   not Matrix → Findings. The insight leads. This produces C-02, C-03 as naturally scoped
   sections rather than undifferentiated matrix analysis.

3. **Explicit --mode risk section** -- named in the findings structure, not implied.
   A section header in the prompt forces a section in the output. This produces C-08 and C-12.

4. **WebSearch + cite source inline** -- the tool is declared but must also be instructed.
   "Use WebSearch...cite the source inline" produces C-07. Without the instruction, the tool
   is available but not used.

5. **Amend impact specification** -- "what the user changes AND what changes in the output"
   produces C-10. Requiring the impact prevents generic amend options.

---

## Final Rubric (v2)

5 essential, 3 recommended, 4 aspirational. All pass in the golden prompt.
See: scout-competitors-rubric-v2-2026-03-14.md

---

## Next step

Update signal.skills.yaml scout-competitors description with this golden prompt body.
Run craft generate to bake it into the binding SKILL.md.
