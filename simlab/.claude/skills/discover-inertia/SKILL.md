---
name: discover-inertia
description: Deep analysis of the inertia competitor -- the option to do nothing. Why would teams keep their current workaround inste
allowed-tools: [Read, Write, Glob]
param_set: standard
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


You are running /discover-inertia for: {{topic}}

Deep analysis of the inertia competitor -- why teams would do nothing instead of adopting this feature. Signal's most strategically important skill. Every feature decision must answer: why does inertia lose? If you cannot answer that, stop.

---

## PHASE 1 -- WORKAROUND MAP

| Field | Answer |
|-------|--------|
| Workaround name | [exact tool, process, or informal practice -- not just "manual process"] |
| How it works | [step-by-step: what does a team actually do today?] |
| Who does it | [specific roles involved] |
| Frequency | [how often, how long per occurrence] |
| Implicit cost | [time per occurrence x frequency = annual cost estimate] |
| Hidden cost | [what breaks, gets missed, or accumulates as debt] |

---

## PHASE 2 -- SWITCHING COST TABLE

| Cost type | Estimate | Who bears it |
|-----------|----------|--------------|
| Learning / training | [hours] | [role] |
| Integration / setup | [hours] | [role] |
| Process change | [weeks to re-establish habits] | [team] |
| Risk during transition | [what breaks while switching] | [team] |
| **Total switching cost** | **[sum]** | |

Switching cost verdict: LOW (< 1 day) / MEDIUM (1-5 days) / HIGH (> 1 week)

---

## PHASE 3 -- INERTIA THREAT SCORE

Inertia threat is HIGH by default. Override only with specific evidence the workaround is actively failing.

```
Inertia threat: HIGH (default) | MEDIUM | LOW

Override conditions for MEDIUM:
  - Workaround cost > $X/month or Y hours/week (quantified)
  - Team is actively looking for alternatives (evidence required)
  - Known failure mode causing active, documented pain

Override conditions for LOW:
  - Workaround recently broke at scale
  - Regulatory change makes workaround non-compliant
  - Competitive event makes status quo untenable
```

---

## PHASE 4 -- CONDITIONS FOR INERTIA TO LOSE

3 specific conditions under which teams would abandon the workaround:

1. [Condition 1: specific trigger that makes the workaround inadequate]
2. [Condition 2: specific value threshold this feature must clear]
3. [Condition 3: specific adoption barrier this feature must remove]

The most important condition is the one closest to being true today.

---

## PHASE 5 -- AMEND

1. [Quantify the switching cost -- replace estimates with numbers]
2. [Identify one specific workaround failure mode the feature must address]
3. [Name the single condition most likely to tip teams away from inertia]

Write artifact to: signals/discover/inertia/{{topic}}-inertia-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/ using the same filename as the default (e.g., {topic}-inertia-{date}.md). No namespace subdirectory.
Include frontmatter: skill: discover-inertia, topic: {{topic}}, date: {{date}}, inertia_score: HIGH|MEDIUM|LOW, switching_cost: LOW|MEDIUM|HIGH
