Written to `simulations/quest/rubrics/roles-create-rubric-v5-2026-03-17.md`.

---

**What was added:**

| ID | Source | Pattern | Prerequisite |
|----|--------|---------|-------------|
| C-18 | V-05 | Bidirectional traceability — declaration names which gate executes each item; each gate cites the declaration ID it validates | C-15 + C-16 |
| C-19 | V-05 | Thin-phase referencing — every content-producing phase is a single-line CONTRACT citation with no rule restatement | C-17 |

**Scoring:** `___ / 12 * 10` (denominator bumped from 10 to 12; 100-point total preserved).

**Estimated v5 ranks:**

| Variation | v4 | C-18 | C-19 | v5 (est.) |
|-----------|-----|------|------|-----------|
| V-05 (Full Five-Criteria) | 100 | P | P | **100** |
| V-04 (In-Phase + Pre-Declared) | 99 | P | F | ~98 |
| V-03 (CONTRACT-Only + Terminal) | 98 | F | P | ~97 |
| V-01 (Pre-Declared + Terminal) | 98 | F | F | ~96 |
| V-02 (In-Phase + No Pre-Declaration) | 98 | F | F | ~96 |

V-05 stays sole 100. The prerequisite relationships make C-18 and C-19 structural: if C-15+C-16 fail then C-18 auto-fails; if C-17 fails then C-19 auto-fails.

**R6 adversarial target:** a variation that passes C-18 but fails C-19 — bidirectional traceability with fat phases — to confirm the two new criteria are independently additive.
 * 10` (1 pt per aspirational criterion, 100-point total preserved).

**R5 actual ranks under v5:** V-05 = 100 (all 12 pass), V-04 ~98 (C-17/C-19 fail), V-03 ~97 (C-15/C-16/C-18 fail), V-01/V-02 ~96 (each failing four of the new five). V-05 holds sole 100; V-04 separates above V-03 by one point; V-01/V-02 tie below V-03.

**Design principle — in-phase vs terminal audit:** C-13 establishes the minimum: a structured self-audit must occur before write. C-15 raises the bar: the audit is distributed so that each phase is gated before the next begins. These are complementary, not redundant — a skill can satisfy C-13 (terminal audit) without satisfying C-15 (in-phase gates), but cannot satisfy C-15 without implicitly satisfying C-13.

**Design principle — declaration before execution:** C-13 requires the audit to happen; C-16 requires the audit to be declared upfront. The pre-declaration creates a commitment contract: the skill cannot silently drop items from the Phase 5 checklist that were not in the declared obligations. These address different failure modes.

**Design principle — named invariants vs inline rules:** C-17 captures a structural pattern where constraints are extracted out of instructional prose into named, referenceable blocks. This is not merely a formatting preference — it makes the invariants scannable, auditable by name, and harder to accidentally override mid-prompt. A skill that embeds the same rules as inline prose satisfies all lower criteria but not C-17.

**Design principle — bidirectional traceability:** C-18 requires the link between declaration and gate to run in both directions. The declared checklist must name which gate executes each item (e.g., "verified at Gate 3a"), and each in-phase gate must cite the declaration ID it validates (e.g., `Gate 3a [B]`). One-way annotation — declaration maps to gates but gates do not cite back, or gates cite back but declaration has no gate assignments — is pass for C-16, fail for C-18. Bidirectional citation makes the audit fully traversable: from the checklist, find the gate; from the gate, find the checklist item. C-18 implies both C-15 and C-16.

**Design principle — thin-phase referencing:** C-19 captures the reduction in phase verbosity that becomes possible once all invariants live in CONTRACT blocks. A phase that restates a CONTRACT rule — even correctly — is longer and potentially divergent from the canonical definition. Thin referencing eliminates the drift risk: the rule lives in exactly one place, and every execution site points to it rather than copying it. "Apply CONTRACT: FIELD-REGISTER" is thin; repeating the register rules inline within the phase step is not. C-19 implies C-17.

---

## Essential Criteria (60%)

All 5 must pass for the output to be useful.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | Role file written to correct path | format | essential | A file exists at `.craft/roles/{area}/{subrole}.md` after the skill runs. Content shown only in chat with no file write = fail. File written to any other path (current directory, `simulations/`, etc.) = fail. |
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
| C-18 | Declaration-to-gate traceability is bidirectional | structure | aspirational | The pre-declared audit checklist names the gate phase that executes each item (e.g., "verified at Gate 3a"), AND each in-phase gate cites the declaration item it validates (e.g., `Gate 3a [B]`). One-directional annotation only = pass for C-15 and/or C-16, fail for C-18. Both ends annotated with matching identifiers = pass. C-18 implies both C-15 and C-16; if either prerequisite fails, C-18 fails. |
| C-19 | Content-producing phases are thin CONTRACT citations | structure | aspirational | Every content-producing phase step references a CONTRACT block by name and contains no restatement of the rules within that block. A phase step that copies or paraphrases any rule already defined in a CONTRACT block = fail, even if the CONTRACT block is also present. All phase steps reduced to "Apply CONTRACT: X" form or equivalent single-line citations = pass. C-19 implies C-17; if C-17 fails, C-19 fails. |

---

## Scoring Worksheet

```
Essential passed:    ___ / 5   =>  ___ * 60 / 5  = ___
Recommended passed:  ___ / 2   =>  ___ * 30 / 2  = ___
Aspirational passed: ___ / 12  =>  ___ * 10 / 12 = ___

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
- **Generic table columns** — table present but uses "Entity / Purpose / Notes" headers with no domain grounding (C-10 fail)
- **Suggestion-only inertia-advocate** — skill mentions creating inertia-advocate but writes only the requested role file (C-11 fail)
- **Premature generation** — interactive mode begins writing after first or second answer without waiting for all three inputs (C-12 fail)
- **Skip-to-write** — skill generates content and writes it to disk without any self-audit phase; first file on disk is the unchecked draft (C-13 fail)
- **Silent misclassification** — bare area (`backend` with no subrole), double colon (`backend::api`), or empty input is silently routed to a wrong mode rather than flagged (C-14 fail)
- **Terminal-only audit** — all self-audit checks are batched at Phase 5; earlier phases produce content with no in-phase gate (C-15 fail)
- **Undeclared audit** — Phase 5 checklist is defined for the first time at execution; no pre-declaration exists at skill entry (C-16 fail)
- **Inline-only constraints** — field register rules, column header rules, or audit checklist are embedded as prose within instructional steps rather than extracted into named CONTRACT: blocks (C-17 fail)
- **One-way annotation** — declaration names gate assignments but gates do not cite declaration IDs back, or vice versa; audit only traversable in one direction (C-18 fail)
- **Fat-phase rule restatement** — CONTRACT blocks exist and are referenced, but phase steps also restate the rules inline; single source of truth is violated (C-19 fail)

---

## Score History

| Variation | v2 (R3) | v3 (R4) | v4 (R5) | C-15 | C-16 | C-17 | C-18 | C-19 | v5 (est.) |
|-----------|---------|---------|---------|------|------|------|------|------|-----------|
| V-01 (Pre-Declared + Terminal) | 100 | 100 | 98 | F | P | F | F | F | ~96 |
| V-02 (In-Phase + No Pre-Declaration) | 100 | 100 | 98 | P | F | F | F | F | ~96 |
| V-03 (CONTRACT-Only + Terminal) | 100 | 100 | 98 | F | F | P | F | P | ~97 |
| V-04 (In-Phase + Pre-Declared) | 100 | 100 | 99 | P | P | F | P | F | ~98 |
| V-05 (Full Five-Criteria) | 100 | 100 | 100 | P | P | P | P | P | 100 |

_v5 estimates: C-18 requires both C-15 and C-16 (V-04 passes; V-01/V-02/V-03 fail). C-19 requires C-17 (V-03/V-05 pass; V-01/V-02/V-04 fail). V-05 holds sole 100. R6 adversarial target: a variation that passes C-18 but fails C-19 (bidirectional traceability without thin phases) to confirm the two new criteria are independently additive._
