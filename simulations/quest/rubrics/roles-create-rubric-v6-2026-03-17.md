Written. Here is the complete v6 rubric:

---

**Two new aspirational criteria added — C-20 and C-21:**

**C-20: AUDIT-CHECKLIST items are thin CONTRACT references, not rule enumerations**
Extends C-19's no-restatement principle from execution phases to the audit declaration layer. A checklist item that names a CONTRACT block and scope ("FIELD-REGISTER compliance -- orientation and lens fields") is thin. An item that enumerates specific rules from the block ("orientation.frame must be self-directed; orientation.serves must name a beneficiary explicitly") is fat and fails, even if the CONTRACT block also exists. The rule lives in exactly three places: CONTRACT block (defined), phase step (cited), audit declaration (referenced by name). Prerequisite: C-16 + C-17 + C-19.

**C-21: Every phase-cited CONTRACT block has at least one AUDIT-CHECKLIST item**
Closes the define-cite-gate loop. Every CONTRACT block that a phase step cites must appear in the pre-declared AUDIT-CHECKLIST -- no unannounced checks. Inactive blocks (defined but never cited) are exempt. Prerequisite: C-16 + C-17 + C-19 + C-20.

**Design logic:**
- C-19 governs the *execution layer* (phases): no CONTRACT rule restatement in phase steps
- C-20 governs the *declaration layer* (checklist): same no-restatement rule applied to audit items
- C-21 governs *completeness* of the declaration: every active CONTRACT block declared for audit

**Scoring:** denominator bumped 12 → 14. `___ / 14 * 10`.

**Key R6 finding preserved:** C-20 and C-21 auto-fail via prerequisite chain for V-01, V-03, V-04 (all fail C-19). V-02 is the new live question -- it passes C-19, so its AUDIT-CHECKLIST item quality becomes the R7 discrimination point. V-05 stays sole 100.

**R7 adversarial target:** a variation that passes C-18+C-19 but fails C-20 or C-21 -- thin execution phases, bidirectional tracing, but AUDIT-CHECKLIST items that enumerate CONTRACT rules or omit a phase-cited block.
equisite chain. V-02 passes C-19; its score under v6 depends on whether its AUDIT-CHECKLIST items are thin (C-20) and whether they cover all phase-cited CONTRACT blocks (C-21). The R7 adversarial target is a variation that passes C-18+C-19 but has fat or incomplete checklist items -- bidirectional tracing with thin phases but a verbose or partial audit declaration.

**Design principle -- thin-audit declarations:** C-19 establishes that execution phases must not restate CONTRACT rules. C-20 extends this principle one layer deeper: AUDIT-CHECKLIST items must also be CONTRACT references, not rule enumerations. A checklist item that names a CONTRACT block and its validation scope (e.g., "FIELD-REGISTER compliance -- orientation and lens fields") is thin. An item that lists the specific rules it is checking (e.g., "orientation.frame must be self-directed; orientation.serves must name a beneficiary explicitly") is fat -- it restates the CONTRACT content in the declaration layer. With C-20, a rule appears in exactly three locations in the skill: defined in the CONTRACT block, cited in the phase step (C-19), and referenced by block name in the audit declaration (C-20). Everywhere else it is absent.

**Design principle -- CONTRACT-coverage completeness:** C-17 requires CONTRACT blocks to exist for key invariants. C-19 requires phases to cite them. C-21 closes the loop: every CONTRACT block that is actively cited by a phase step must have at least one AUDIT-CHECKLIST item that declares the check. A CONTRACT block cited in a phase but absent from the pre-declaration creates an unannounced gate -- the check fires in execution, but the declaration never committed to it. C-21 ensures the set of declared audit obligations is a superset of the set of active CONTRACT blocks: no CONTRACT block can be silently checked without first being announced. C-21 implies C-20 and requires C-17; a skill with no CONTRACT blocks auto-fails via the C-19 prerequisite chain before C-21 is reached.

---

## Essential Criteria (60%)

All 5 must pass for the output to be useful.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | Role file written to correct path | format | essential | A file exists at `.craft/roles/{area}/{subrole}.md` after the skill runs. Content shown only in chat with no file write = fail. File written to any other path (current directory, `simulations/`, etc.) = fail. |
| C-02 | All required frontmatter fields present | format | essential | The YAML frontmatter block contains: `name`, `version`, `archetype`, `orientation.frame`, `orientation.serves`, `lens.verify` (list), `lens.simplify` (list), `expertise.depth`, `expertise.relevance`, `scope`, `collaborates_with`, `artifacts`, and `workflow`. Any field missing or structurally absent = fail. |
| C-03 | Mode detection routes correctly | behavior | essential | Skill correctly reads the input as name-only (`area:subrole`), description (quoted natural language), or interactive (no argument), and routes to the appropriate generation path. Name-only treated as description, or interactive triggered when a name was given = fail. |
| C-04 | Frontmatter content is domain-specific | correctness | essential | `orientation.frame`, `orientation.serves`, `expertise.depth`, and `lens.verify` items are specific to the named domain -- not generic placeholder text. A `backend:healthcare` role that has finance or customer-service content = fail. |
| C-05 | Inertia-advocate is surfaced when absent | behavior | essential | If an `inertia-advocate` sub-role does not already exist in the target area, the skill suggests creating it (inline, as a follow-up prompt, or as a secondary output). Inertia-advocate already present in area = pass by absence. Neither surfaced nor blocked when absent = fail. |

---

## Recommended Criteria (30%)

Output is better with these.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | Lens.verify questions are sharp and actionable | depth | recommended | Each `lens.verify` item is phrased as a concrete boolean check ("Is X configured before Y?", "Are Z items set to...?") -- not a general topic heading. Vague items like "Check configuration" or "Review security" without specific conditions = fail. Minimum 4 items required. |
| C-07 | Body section includes a domain specializations table | coverage | recommended | The markdown body below the frontmatter contains at least one structured table (core entities, modules, components, or equivalents) that maps domain-specific constructs to their purpose. Body with only prose and no tables = fail. |

---

## Aspirational Criteria (10%)

Raise the bar once essential and recommended are stable.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | Archetype is calibrated to the area tier pattern | depth | aspirational | The `archetype` field matches the established archetype for the target area (e.g., `craft` for backend/developer/designer areas, process-specific for discovery/governance areas). Checking existing roles in the area and aligning to their pattern = pass. A generic or default archetype applied without consulting the established pattern = fail. If no established pattern exists, this criterion is skipped (counted as pass). |
| C-09 | Orientation register matches the stated audience | correctness | aspirational | Language register in `orientation.frame` is self-directed (how the role sees the domain) and `orientation.serves` is receiver-directed (who benefits and why). `serves` must name a beneficiary explicitly -- not describe the role itself. Both fields written in the same register, or `serves` written as a self-description, = fail. |
| C-10 | Body table uses domain-named column headers | coverage | aspirational | Column headers in the domain specializations table reference domain-specific terminology (e.g., "Module / GL Impact" for finance, "Regulation / Scope / Penalty" for compliance, "Command / Side Effect" for backend). Generic headers ("Entity / Purpose / Notes", "Item / Description") with domain content in the rows = fail. |
| C-11 | Inertia-advocate companion file is generated when absent | behavior | aspirational | When no `inertia-advocate.md` exists in the target area, the skill generates a complete companion role file -- with valid frontmatter and body -- in addition to the requested role. Mention or suggestion only = pass for C-05, fail for C-11. Inertia-advocate already present = pass by absence. |
| C-12 | Interactive mode holds for all inputs before writing | behavior | aspirational | In interactive mode, the skill explicitly waits for answers to all three questions (area, subrole, orientation seed) before generating any content. Proceeding after receiving only one or two answers, or generating a partial role mid-conversation, = fail. Non-interactive modes are exempt. |
| C-13 | Pre-write self-certification phase is executed | behavior | aspirational | Skill performs a structured self-audit -- explicit YES/NO (or equivalent pass/fail) check against each rubric dimension -- between content generation and file write. If any check fails, the skill fixes the issue before writing. The file written to disk is always the post-audit version; no unchecked draft is ever persisted. Proceeding directly from generation to write with no audit step = fail. |
| C-14 | Malformed inputs are routed before mode detection | behavior | aspirational | A pre-detection phase applies deterministic rules to classify inputs that fall outside the three clean modes -- bare area (area name with no subrole or colon), extra colons (more than one separator), vague phrase (natural language not matching either clean non-interactive mode), or empty -- and responds with explicit clarification or error before routing. Silent misclassification or silent fallthrough to a wrong mode = fail. If the test input is a valid clean-mode input, this criterion passes by absence. |
| C-15 | Audit checks are distributed as in-phase gates | behavior | aspirational | Each generation phase embeds its own explicit pass/fail gate; execution halts at the failing phase before advancing. A terminal-only audit (all checks batched at Phase 5 or equivalent) = pass for C-13, fail for C-15. In-phase gates at each content-producing step, with Phase 5 serving as final confirmation rather than sole checkpoint = pass. |
| C-16 | Audit obligations are pre-declared before generation | behavior | aspirational | The skill declares its complete audit checklist -- naming each criterion by ID or label -- before any content generation begins. The Phase 5 execution then runs against the pre-declared list. Defining the checklist for the first time at Phase 5 = pass for C-13, fail for C-16. Pre-declaration at skill entry (before Phase 1) with Phase 5 executing the declared list = pass. |
| C-17 | Hard constraints are extracted into named CONTRACT sections | structure | aspirational | Key invariants (field register rules, audit checklist, column header rules) are extracted into explicitly named CONTRACT: blocks that the audit phase references by name. Constraints expressed only as inline prose within instructional steps = fail. Named CONTRACT: blocks defined at the top level of the skill and cited by name in the audit phase = pass. |
| C-18 | Declaration-to-gate traceability is bidirectional | structure | aspirational | The pre-declared audit checklist names the gate phase that executes each item (e.g., "verified at Gate 3a"), AND each in-phase gate cites the declaration item it validates (e.g., `Gate 3a [B]`). One-directional annotation only = pass for C-15 and/or C-16, fail for C-18. Both ends annotated with matching identifiers = pass. C-18 implies both C-15 and C-16; if either prerequisite fails, C-18 fails. |
| C-19 | Content-producing phases are thin CONTRACT citations | structure | aspirational | Every content-producing phase step references a CONTRACT block by name and contains no restatement of the rules within that block. A phase step that copies or paraphrases any rule already defined in a CONTRACT block = fail, even if the CONTRACT block is also present. All phase steps reduced to "Apply CONTRACT: X" form or equivalent single-line citations = pass. C-19 implies C-17; if C-17 fails, C-19 fails. |
| C-20 | AUDIT-CHECKLIST items are thin CONTRACT references, not rule enumerations | structure | aspirational | Each criterion entry in the pre-declared AUDIT-CHECKLIST identifies what to check by naming the CONTRACT block and validation scope -- it does not reproduce the CONTRACT block rule content. A thin item names the block and scope (e.g., "FIELD-REGISTER compliance -- orientation and lens fields"). A fat item enumerates the specific rules (e.g., "orientation.frame must be self-directed; orientation.serves must name a beneficiary explicitly"). Fat items = fail even if the CONTRACT block is also present. The no-restatement rule applies in the declaration layer as it does in execution phases. C-20 implies C-19; if C-19 fails, C-20 fails. |
| C-21 | Every phase-cited CONTRACT block has at least one AUDIT-CHECKLIST item | structure | aspirational | For each CONTRACT block cited by at least one content-producing phase step, the pre-declared AUDIT-CHECKLIST contains at least one item that names that CONTRACT block. A CONTRACT block that is cited in a phase step but absent from the audit declaration = unannounced check = fail. CONTRACT blocks that are defined but never cited by any phase (inactive blocks) are exempt. C-21 implies C-20; if C-20 fails, C-21 fails. |

---

## Scoring Worksheet

```
Essential passed:    ___ / 5   =>  ___ * 60 / 5  = ___
Recommended passed:  ___ / 2   =>  ___ * 30 / 2  = ___
Aspirational passed: ___ / 14  =>  ___ * 10 / 14 = ___

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

- **Chat-only output** -- role content shown in the response but no file written to `.craft/roles/` (C-01 fail)
- **Wrong path** -- file written to current directory or `simulations/` instead of `.craft/roles/{area}/{subrole}.md` (C-01 fail)
- **Template bleed** -- frontmatter fields present but contain placeholder text from another domain (C-04 fail)
- **Silent inertia-advocate skip** -- target area has no inertia-advocate and skill creates the requested role without mentioning it (C-05 fail)
- **Generic verify items** -- `lens.verify` contains broad items ("Is the module configured?") rather than specific boolean checks ("Is posting profile mapped to GL accounts before transaction posting?") (C-06 fail)
- **Prose-only body** -- markdown body has paragraphs explaining the domain but no structured tables grounding the role in specific entities/modules/components (C-07 fail)
- **Mode ambiguity** -- skill prompts for clarification when the input clearly matches one mode pattern (C-03 fail by over-caution)
- **Generic table columns** -- table present but uses "Entity / Purpose / Notes" headers with no domain grounding (C-10 fail)
- **Suggestion-only inertia-advocate** -- skill mentions creating inertia-advocate but writes only the requested role file (C-11 fail)
- **Premature generation** -- interactive mode begins writing after first or second answer without waiting for all three inputs (C-12 fail)
- **Skip-to-write** -- skill generates content and writes it to disk without any self-audit phase; first file on disk is the unchecked draft (C-13 fail)
- **Silent misclassification** -- bare area (`backend` with no subrole), double colon (`backend::api`), or empty input is silently routed to a wrong mode rather than flagged (C-14 fail)
- **Terminal-only audit** -- all self-audit checks are batched at Phase 5; earlier phases produce content with no in-phase gate (C-15 fail)
- **Undeclared audit** -- Phase 5 checklist is defined for the first time at execution; no pre-declaration exists at skill entry (C-16 fail)
- **Inline-only constraints** -- field register rules, column header rules, or audit checklist are embedded as prose within instructional steps rather than extracted into named CONTRACT: blocks (C-17 fail)
- **One-way annotation** -- declaration names gate assignments but gates do not cite declaration IDs back, or vice versa; audit only traversable in one direction (C-18 fail)
- **Fat-phase rule restatement** -- CONTRACT blocks exist and are referenced, but phase steps also restate the rules inline; single source of truth is violated (C-19 fail)
- **Fat-checklist rule enumeration** -- AUDIT-CHECKLIST criterion descriptions reproduce the specific rules from CONTRACT blocks rather than naming the block and scope; the no-restatement principle is satisfied in execution phases but violated in the audit declaration (C-20 fail)
- **Uncovered active CONTRACT block** -- a CONTRACT block is cited by a phase step and checked by a gate, but the pre-declared AUDIT-CHECKLIST has no item for that block; the check fires but was never announced (C-21 fail)

---

## Score History

| Variation | v2 (R3) | v3 (R4) | v4 (R5) | v5 (R6 act.) | C-20 | C-21 | v6 (est.) |
|-----------|---------|---------|---------|--------------|------|------|-----------|
| V-01 (Bidirectional + Fat Phases) | 100 | 100 | 98 | ~97 | F (auto, C-19=F) | F (auto, C-20=F) | ~96 |
| V-02 (Thin Phases + No Back-Citation) | 100 | 100 | 98 | ~97 | ? | ? | ~97 or lower |
| V-03 (CONTRACT-Only + Terminal) | 100 | 100 | 98 | ~97 | F (auto, C-19=F) | F (auto, C-20=F) | ~96 |
| V-04 (In-Phase + Pre-Declared) | 100 | 100 | 99 | ~98 | F (auto, C-19=F) | F (auto, C-20=F) | ~97 |
| V-05 (Full Five-Criteria) | 100 | 100 | 100 | 100 | P | P | **100** |

_C-20 and C-21 auto-fail for any variation where C-19 fails (V-01, V-03, V-04), preserving their position in the ranking. V-02 passes C-19; its v6 score depends on whether its AUDIT-CHECKLIST items are thin (C-20) and whether they cover all phase-cited CONTRACT blocks (C-21). V-05 holds sole 100. R7 adversarial target: a variation that passes C-18+C-19 but fails C-20 or C-21 -- thin execution phases and bidirectional tracing, but AUDIT-CHECKLIST items that enumerate CONTRACT rules or omit a phase-cited block._
