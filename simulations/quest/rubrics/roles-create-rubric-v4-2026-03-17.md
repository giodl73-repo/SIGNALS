Written to `simulations/quest/rubrics/roles-create-rubric-v4-2026-03-17.md`.

---

**What was extracted and why:**

| ID | Source | Pattern | Distinguishes from |
|----|--------|---------|-------------------|
| C-15 | V-03 (Distributed-Audit) | In-phase gates — each phase halts before advancing if its gate fails | C-13 only requires a terminal audit; C-15 requires per-phase gating |
| C-16 | V-04 (Front-Loaded-Guard) | Pre-declared obligations — full audit checklist declared at skill entry before generation begins | C-13 only requires the audit happens; C-16 requires the list to be committed upfront |
| C-17 | V-05 (Separation-of-Contracts) | CONTRACT: invariant sections — constraints extracted into named blocks referenced by the audit by name | Inline prose rules satisfy all lower criteria but not C-17 |

**Scoring change:** `___ / 7 * 10` → `___ / 10 * 10` (1 pt per aspirational criterion, 100-point total preserved).

**Estimated R4 ranks under v4:** V-03/V-04/V-05 ~98 (one new criterion each), V-01/V-02 ~97. Three-way tie at the top means R5 needs adversarial variations that fail exactly one of C-15/C-16/C-17 to confirm clean separation.
l preserved.

**Effect on differentiation:** All five R4 variations scored 100 on v3. v4 restores separation — V-03 is the only variation that satisfies C-15, V-04 is the only one that satisfies C-16, V-05 is the only one that satisfies C-17. Estimated ranks: V-03/V-04/V-05 ~98, V-01/V-02 ~97.

**Design principle — in-phase vs terminal audit:** C-13 establishes the minimum: a structured self-audit must occur before write. C-15 raises the bar: the audit is distributed so that each phase is gated before the next begins. These are complementary, not redundant — a skill can satisfy C-13 (terminal audit) without satisfying C-15 (in-phase gates), but cannot satisfy C-15 without implicitly satisfying C-13.

**Design principle — declaration before execution:** C-13 requires the audit to happen; C-16 requires the audit to be declared upfront. The pre-declaration creates a commitment contract: the skill cannot silently drop items from the Phase 5 checklist that were not in the declared obligations. These address different failure modes.

**Design principle — named invariants vs inline rules:** C-17 captures a structural pattern where constraints are extracted out of instructional prose into named, referenceable blocks. This is not merely a formatting preference — it makes the invariants scannable, auditable by name, and harder to accidentally override mid-prompt. A skill that embeds the same rules as inline prose satisfies all lower criteria but not C-17.

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
| C-15 | Audit checks are distributed as in-phase gates | behavior | aspirational | Each generation phase embeds its own explicit pass/fail gate; execution halts at the failing phase before advancing. A terminal-only audit (all checks batched at Phase 5 or equivalent) = pass for C-13, fail for C-15. In-phase gates at each content-producing step, with Phase 5 serving as final confirmation rather than sole checkpoint = pass. |
| C-16 | Audit obligations are pre-declared before generation | behavior | aspirational | The skill declares its complete audit checklist — naming each criterion by ID or label — before any content generation begins. The Phase 5 execution then runs against the pre-declared list. Defining the checklist for the first time at Phase 5 = pass for C-13, fail for C-16. Pre-declaration at skill entry (before Phase 1) with Phase 5 executing the declared list = pass. |
| C-17 | Hard constraints are extracted into named CONTRACT sections | structure | aspirational | Key invariants (field register rules, audit checklist, column header rules) are extracted into explicitly named CONTRACT: blocks that the audit phase references by name. Constraints expressed only as inline prose within instructional steps = fail. Named CONTRACT: blocks defined at the top level of the skill and cited by name in the audit phase = pass. |

---

## Scoring Worksheet

```
Essential passed:    ___ / 5   =>  ___ * 60 / 5  = ___
Recommended passed:  ___ / 2   =>  ___ * 30 / 2  = ___
Aspirational passed: ___ / 10  =>  ___ * 10 / 10 = ___

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
- **Terminal-only audit** — all self-audit checks are batched at Phase 5; earlier phases produce content with no in-phase gate (C-15 fail)
- **Undeclared audit** — Phase 5 checklist is defined for the first time at execution; no pre-declaration exists at skill entry (C-16 fail)
- **Inline-only constraints** — field register rules, column header rules, or audit checklist are embedded as prose within instructional steps rather than extracted into named CONTRACT: blocks (C-17 fail)

---

## Score History

| Variation | v2 (R3 actual) | v3 (R4 actual) | v4 (est.) | C-15 | C-16 | C-17 |
|-----------|----------------|----------------|-----------|------|------|------|
| V-01 (Minimal-Delta) | 100 | 100 | ~97 | F | F | F |
| V-02 (Checklist-Format) | 100 | 100 | ~97 | F | F | F |
| V-03 (Distributed-Audit) | 100 | 100 | ~98 | P | F | F |
| V-04 (Front-Loaded-Guard) | 100 | 100 | ~98 | F | P | F |
| V-05 (Separation-of-Contracts) | 100 | 100 | ~98 | F | F | P |

_v4 estimates assume R4 variations are unchanged. C-15/C-16/C-17 require adversarial variations in R5 to confirm separation holds._
