Written to `simulations/quest/rubrics/roles-create-rubric-2026-03-17.md`.

**5 essential, 2 recommended, 2 aspirational** — 9 criteria total.

Key design decisions:

- **C-01/C-02** are format gates — no file write or missing frontmatter fails immediately before any content is evaluated
- **C-03** tests mode routing, which is the most branchy behavior in the skill
- **C-04** catches template bleed — the most likely failure for name-only mode where smart defaults might copy from a neighboring role
- **C-05** makes inertia-advocate suggestion a hard requirement, matching the skill spec ("always suggested if not already present")
- **C-06** sharpens the AMEND note on lens.verify — vague questions are a known weak spot from examining existing roles
- **C-07** captures the domain specializations table from the AMEND note
- **C-08/C-09** are aspirational because archetype calibration and register precision require understanding the full area context, which a new role can't always guarantee

Golden threshold: all 5 essential + composite >= 80.
ehavior | essential | Skill correctly reads the input as name-only (`area:subrole`), description (quoted natural language), or interactive (no argument), and routes to the appropriate generation path. Name-only treated as description, or interactive triggered when a name was given = fail. |
| C-04 | Frontmatter content is domain-specific | correctness | essential | `orientation.frame`, `orientation.serves`, `expertise.depth`, and `lens.verify` items are specific to the named domain — not generic placeholder text. A `backend:healthcare` role that has finance or customer-service content = fail. |
| C-05 | Inertia-advocate is surfaced when absent | behavior | essential | If an `inertia-advocate` sub-role does not already exist in the target area, the skill suggests creating it (inline, as a follow-up prompt, or as a secondary output). Inertia-advocate already present in area = pass by absence. Neither surfaced nor blocked when absent = fail. |

---

## Recommended Criteria (30%)

Output is better with these.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | Lens.verify questions are sharp and actionable | depth | recommended | Each `lens.verify` item is phrased as a concrete boolean check ("Is X configured before Y?", "Are Z items set to...?") — not a general topic heading. Vague items like "Check configuration" or "Review security" without specific conditions = fail. Minimum 4 items required. |
| C-07 | Body section includes a domain specializations table | coverage | recommended | The markdown body below the frontmatter contains at least one structured table (core entities, modules, components, or equivalents) that maps domain-specific constructs to their purpose. Body with only prose and no tables = fail. |

---

## Aspirational Criteria (10%)

Raise the bar once essential and recommended are stable.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | Archetype is calibrated to the area's tier pattern | depth | aspirational | The `archetype` field matches the established archetype for the target area (e.g., `craft` for backend/developer/designer, process-specific for discovery/governance). A generic or default archetype applied without regard to area context = fail. If no established pattern exists, this criterion is skipped (counted as pass). |
| C-09 | Orientation register matches the stated audience | correctness | aspirational | Language register in `orientation.frame` is self-directed (how the role sees the domain) and `orientation.serves` is receiver-directed (who benefits and why) — both in the appropriate register for the area tier (technical for developer/backend, strategic for director/executive). Both fields written in the same register, or serves written as a self-description = fail. |

---

## Scoring Worksheet

```
Essential passed:    ___ / 5   =>  ___ * 60 / 5  = ___
Recommended passed:  ___ / 2   =>  ___ * 30 / 2  = ___
Aspirational passed: ___ / 2   =>  ___ * 10 / 2  = ___

Composite score: ___

Golden: all 5 essential pass AND composite >= 80
```

| Band | Score | Meaning |
|------|-------|---------|
| Golden | all essential + >= 80 | Role file is production-ready |
| Passing | all essential + 60-79 | Usable; recommended gaps noted |
| Failing | any essential fails | Not useful as a role artifact |

---

## Failure Modes to Watch

- **Chat-only output** — role content shown in the response but no file written to `.craft/roles/` (C-01 fail)
- **Wrong path** — file written to current directory or `simulations/` instead of `.craft/roles/{area}/{subrole}.md` (C-01 fail)
- **Template bleed** — frontmatter fields present but contain placeholder text from another domain (C-04 fail)
- **Silent inertia-advocate skip** — target area has no inertia-advocate and skill creates the requested role without mentioning it (C-05 fail)
- **Generic verify items** — `lens.verify` contains broad items ("Is the module configured?") rather than specific boolean checks ("Is posting profile mapped to GL accounts before transaction posting?") (C-06 fail)
- **Prose-only body** — markdown body has paragraphs explaining the domain but no structured tables grounding the role in specific entities/modules/components (C-07 fail)
- **Mode ambiguity** — skill prompts for clarification when the input clearly matches one mode pattern (C-03 fail by over-caution)
