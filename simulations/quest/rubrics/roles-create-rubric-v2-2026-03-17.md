Written to `simulations/quest/rubrics/roles-create-rubric-v2-2026-03-17.md`.

---

**What changed from v1 to v2:**

Three new aspirational criteria extracted from R1 excellence signals:

| ID | Signal Source | What it captures |
|----|---------------|-----------------|
| C-10 | V-05 (unique) | Table column headers must be domain-named — not generic "Entity / Purpose". Prevents nominal C-07 compliance where a table is present but adds no domain grounding. |
| C-11 | V-03, V-05 | Inertia-advocate must be *generated* (complete file), not just mentioned. C-05 already requires surfacing; C-11 sets the higher bar of delivery. |
| C-12 | V-05 (unique) | Interactive mode must explicitly hold for all three inputs before writing. C-03 tests routing; C-12 tests that the hold is enforced. |

**Scoring adjustment:** Aspirational pool stays at 10 pts, now divided 5 ways — 2 pts each instead of 5 pts each. 100-point total preserved.

**v2 retroactive ranks** (estimated): V-05 = 100, V-02 ≈ 98, V-04 ≈ 96, V-03 ≈ 91, V-01 ≈ 94. V-05 is the only variation that satisfies all five aspirational criteria.
erstanding the full area context, which a new role can't always guarantee
- **C-10 (new, R1)** — V-05 signal: domain-named table columns prevent nominal C-07 compliance (table present, content generic). "Entity / Purpose" headers with domain rows is a pass for C-07 and a fail for C-10.
- **C-11 (new, R1)** — V-03/V-05 signal: generating the inertia-advocate companion file is categorically stronger than surfacing a suggestion. C-05 passes at surface; C-11 requires delivery.
- **C-12 (new, R1)** — V-05 signal (unique among R1 variations): interactive mode must explicitly hold for all three inputs before writing. C-03 passes when routing is correct; C-12 passes only when the hold is enforced.

Golden threshold: all 5 essential + composite >= 80.

---

## Essential Criteria (60%)

All 5 must pass for the output to be useful.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | Role file written to correct path | format | essential | A file exists at `.roles/{area}/{subrole}.md` after the skill runs. Content shown only in chat with no file write = fail. File written to any other path (current directory, `simulations/`, etc.) = fail. |
| C-02 | All required frontmatter fields present | format | essential | The YAML frontmatter block contains: `name`, `version`, `archetype`, `orientation.frame`, `orientation.serves`, `lens.verify` (list), `lens.simplify` (list), `expertise.depth`, `expertise.relevance`, `scope`, `collaborates_with`, `artifacts`, and `workflow`. Any field missing or structurally absent = fail. |
| C-03 | Mode detection routes correctly | behavior | essential | Skill correctly reads the input as name-only (`area:subrole`), description (quoted natural language), or interactive (no argument), and routes to the appropriate generation path. Name-only treated as description, or interactive triggered when a name was given = fail. |
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
| C-08 | Archetype is calibrated to the area's tier pattern | depth | aspirational | The `archetype` field matches the established archetype for the target area (e.g., `craft` for backend/developer/designer areas, process-specific for discovery/governance areas). Checking existing roles in the area and aligning to their pattern = pass. A generic or default archetype applied without consulting the area's established pattern = fail. If no established pattern exists, this criterion is skipped (counted as pass). |
| C-09 | Orientation register matches the stated audience | correctness | aspirational | Language register in `orientation.frame` is self-directed (how the role sees the domain) and `orientation.serves` is receiver-directed (who benefits and why). `serves` must name a beneficiary explicitly — not describe the role itself. Both fields written in the same register, or `serves` written as a self-description, = fail. |
| C-10 | Body table uses domain-named column headers | coverage | aspirational | Column headers in the domain specializations table reference domain-specific terminology (e.g., "Module / GL Impact" for finance, "Regulation / Scope / Penalty" for compliance, "Command / Side Effect" for backend). Generic headers ("Entity / Purpose / Notes", "Item / Description") with domain content in the rows = fail. |
| C-11 | Inertia-advocate companion file is generated when absent | behavior | aspirational | When no `inertia-advocate.md` exists in the target area, the skill generates a complete companion role file — with valid frontmatter and body — in addition to the requested role. Mention or suggestion only = pass for C-05, fail for C-11. Inertia-advocate already present = pass by absence. |
| C-12 | Interactive mode holds for all inputs before writing | behavior | aspirational | In interactive mode, the skill explicitly waits for answers to all three questions (area, subrole, orientation seed) before generating any content. Proceeding after receiving only one or two answers, or generating a partial role mid-conversation, = fail. Non-interactive modes are exempt. |

---

## Scoring Worksheet

```
Essential passed:    ___ / 5   =>  ___ * 60 / 5  = ___
Recommended passed:  ___ / 2   =>  ___ * 30 / 2  = ___
Aspirational passed: ___ / 5   =>  ___ * 10 / 5  = ___

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

- **Chat-only output** — role content shown in the response but no file written to `.roles/` (C-01 fail)
- **Wrong path** — file written to current directory or `simulations/` instead of `.roles/{area}/{subrole}.md` (C-01 fail)
- **Template bleed** — frontmatter fields present but contain placeholder text from another domain (C-04 fail)
- **Silent inertia-advocate skip** — target area has no inertia-advocate and skill creates the requested role without mentioning it (C-05 fail)
- **Generic verify items** — `lens.verify` contains broad items ("Is the module configured?") rather than specific boolean checks ("Is posting profile mapped to GL accounts before transaction posting?") (C-06 fail)
- **Prose-only body** — markdown body has paragraphs explaining the domain but no structured tables grounding the role in specific entities/modules/components (C-07 fail)
- **Mode ambiguity** — skill prompts for clarification when the input clearly matches one mode pattern (C-03 fail by over-caution)
- **Generic table columns** — table present but uses "Entity / Purpose / Notes" headers with no domain grounding (C-10 fail)
- **Suggestion-only inertia-advocate** — skill mentions creating inertia-advocate but writes only the requested role file (C-11 fail)
- **Premature generation** — interactive mode begins writing after first or second answer without waiting for all three inputs (C-12 fail)

---

## R1 Score Summary (reference)

| Variation | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 | P | P | P | P | P |
| C-02 | P | P | P | P | P |
| C-03 | P | P | P | P | P |
| C-04 | P | P | P | P | P |
| C-05 | P | P | P | P | P |
| C-06 | P | P | PARTIAL | P | P |
| C-07 | P | P | P | P | P |
| C-08 | PARTIAL | P | PARTIAL | PARTIAL | P |
| C-09 | PARTIAL | P | PARTIAL | P | P |
| **v1 score** | **96** | **100** | **89** | **98** | **100** |
| C-10 | ? | P | ? | ? | P |
| C-11 | F | F | P | F | P |
| C-12 | F | F | F | F | P |
| **v2 score** | **~94** | **~98** | **~91** | **~96** | **100** |

_v2 scores are estimates: C-10 retroactive evidence incomplete for V-01/V-03/V-04._
