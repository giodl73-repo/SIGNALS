Written to `simulations/quest/rubrics/roles-create-rubric-v3-2026-03-17.md`.

---

**What changed from v2 to v3:**

| ID | Signal Source | What it captures |
|----|---------------|-----------------|
| C-13 | V-03 (unique) | Pre-write self-certification phase. Skill performs a structured YES/NO audit against each rubric dimension between generation and file write. Fix-in-place if any gate fails. The file on disk is always the post-audit version. Skip-to-write = fail. |
| C-14 | V-04 (unique) | Malformed-input routing before mode detection. A pre-detection phase handles bare area, extra colons, vague phrase, and empty inputs with deterministic rules and explicit clarification/error before routing. Silent misclassification = fail. Valid clean-mode input = pass by absence. |

**Categorical-prohibitions framing (V-05 signal)** is noted as a design principle in the rubric header but not promoted to a standalone C-NN — it already exercises through C-12's pass condition (hold enforcement), not through a separable observable.

**Scoring adjustment:** Aspirational pool stays at 10 pts, now divided 7 ways (`___ / 7 * 10`). 100-point total preserved.

**Effect on differentiation:** All five R3 variations scored 100 on v2. v3 restores separation — V-03 is the only variation that satisfies C-13, V-04 is the only one that satisfies C-14. Estimated ranks: V-03 = 100, V-04 ~99, V-01/V-02/V-05 ~97.
:** "These are categorical prohibitions, not preferences" is a design principle for how hard constraints should be expressed in a skill prompt, not a separable output criterion. It is not promoted to a standalone C-NN because it is already exercised by the C-12 pass condition (interactive hold enforcement). It surfaces here as a named pattern for skill authors, not as a scored dimension.

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
| C-13 | Pre-write self-certification phase is executed | behavior | aspirational | Skill performs a structured self-audit — explicit YES/NO (or equivalent pass/fail) check against each rubric dimension — between content generation and file write. If any check fails, the skill fixes the issue before writing. The file written to disk is always the post-audit version; no unchecked draft is ever persisted. Proceeding directly from generation to write with no audit step = fail. |
| C-14 | Malformed inputs are routed before mode detection | behavior | aspirational | A pre-detection phase applies deterministic rules to classify inputs that fall outside the three clean modes — bare area (area name with no subrole or colon), extra colons (more than one separator), vague phrase (natural language not matching either clean non-interactive mode), or empty — and responds with explicit clarification or error before routing. Silent misclassification or silent fallthrough to a wrong mode = fail. If the test input is a valid clean-mode input, this criterion passes by absence. |

---

## Scoring Worksheet

```
Essential passed:    ___ / 5   =>  ___ * 60 / 5  = ___
Recommended passed:  ___ / 2   =>  ___ * 30 / 2  = ___
Aspirational passed: ___ / 7   =>  ___ * 10 / 7  = ___

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
- **Skip-to-write** — skill generates content and writes it to disk without any self-audit phase; first file on disk is the unchecked draft (C-13 fail)
- **Silent misclassification** — bare area (`backend` with no subrole), double colon (`backend::api`), or empty input is silently routed to a wrong mode rather than flagged (C-14 fail)

---

## Score History

| Variation | v2 (R3 actual) | v3 (est.) | C-13 | C-14 |
|-----------|----------------|-----------|------|------|
| V-01 (Constraint-Minimal) | 100 | ~97 | F | F |
| V-02 (Template-First) | 100 | ~97 | F | F |
| V-03 (Pre-Write Audit) | 100 | 100 | P | ? |
| V-04 (Ambiguous-Input Routing) | 100 | ~99 | F | P |
| V-05 (Separation-of-Contracts) | 100 | ~97 | F | F |

_C-14 for V-03 requires an adversarial input test to confirm. All other v3 estimates assume the R3 variations are unchanged._
