Two new patterns from R7 V-05 are not yet captured as criteria:

1. **Self-documenting checklist** — V-05's AUDIT-CHECKLIST header explicitly declares its own format rule ("Items name the CONTRACT block and validation scope only — no rule enumeration"). A checklist that follows the thin format but doesn't announce that constraint is structurally opaque. This is separable from C-20 (which tests item content, not whether the format constraint is declared).

2. **Three-location quarantine** — The three-location rule says rule content appears in exactly three canonical places and *nowhere else*. C-19 covers phase steps; C-20 covers checklist items. Neither covers preamble, meta-commentary, structural annotations, or intro prose. A skill could pass C-19 + C-20 while restating rule content in an intro paragraph — that would violate the three-location rule without triggering any existing criterion.

These become **C-22** and **C-23**. Denominator 14 → 16. Here is the complete v7 rubric:

---

```markdown
# roles-create Rubric — v7 (2026-03-17)

## Version History

| Version | Change |
|---------|--------|
| v1 | 5 essential + 2 recommended + 2 aspirational (C-08/C-09) |
| v2–v5 | Aspirational expansion through C-15 (audit gate distribution) |
| v6 | C-16 through C-21 added (pre-declaration, CONTRACT structure, thin-citation layers); denominator 12 → 14 |
| **v7** | **C-22 and C-23 added (self-documenting checklist header; three-location quarantine); denominator 14 → 16** |

**v7 change notes:**

**C-22: AUDIT-CHECKLIST header declares its own format constraint**
V-05 distinguisher: the pre-declared AUDIT-CHECKLIST opens with an explicit meta-statement naming the format rule it follows — e.g., "Items name the CONTRACT block and validation scope only — no rule enumeration." A checklist that follows the thin-reference format (C-20 pass) but carries no header declaring that constraint is structurally opaque: readers cannot determine from the structure itself whether the format is intentional or accidental. With C-22, the format rule is declared within the structure, making the checklist self-documenting about its own constraint. Prerequisite: C-20.

**C-23: Rule content is quarantined to the three canonical locations**
C-19 and C-20 establish that phase steps and audit items must be thin citations. C-23 closes the remaining surface: rule content may appear in *exactly* three locations in the skill — (1) the CONTRACT block where it is defined, (2) the phase step that cites it by name, (3) the AUDIT-CHECKLIST item that references it by name — and nowhere else. Preamble prose, meta-commentary, structural annotations, introductory summaries, and inline comments that reproduce or paraphrase rule content = fail, even if C-19 and C-20 both pass. The adversarial target is a skill with thin phases and thin checklist items that still restates rule content in an intro section or explanatory aside. Prerequisite: C-19 + C-20.

**Design logic:**
- C-19 governs *execution phases*: no CONTRACT rule restatement in phase steps
- C-20 governs *audit declaration items*: same no-restatement rule applied to checklist entries
- C-21 governs *completeness* of the declaration: every active CONTRACT block pre-declared
- C-22 governs *self-documentation* of the checklist: the format constraint is declared within the structure
- C-23 governs *the full skill surface*: no rule content outside the three canonical locations

**Scoring:** denominator bumped 14 → 16. `___ / 16 * 10`.

**R7 finding preserved:** V-05 sole 100. V-02 and V-04 tied at 99.29 (C-21 and C-18 each cost one criterion). V-01 at 98.57 (C-20 failure auto-costs C-21). V-03 at 97.86 (C-19 cascade costs three). C-22 and C-23 are now the R8 discrimination targets: a variation that passes C-18 through C-21 but has an undeclared checklist format (C-22 fail) or restates rule content in a preamble section (C-23 fail).

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
| C-08 | Archetype is calibrated to the area tier pattern | depth | aspirational | The `archetype` field matches the established archetype for the target area (e.g., `craft` for backend/developer/designer areas, process-specific for discovery/governance areas). Checking existing roles in the area and aligning to their pattern = pass. A generic or default archetype applied without consulting the established pattern = fail. If no established pattern exists, this criterion is skipped (counted as pass). |
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
| C-20 | AUDIT-CHECKLIST items are thin CONTRACT references, not rule enumerations | structure | aspirational | Each criterion entry in the pre-declared AUDIT-CHECKLIST identifies what to check by naming the CONTRACT block and validation scope — it does not reproduce the CONTRACT block rule content. A thin item names the block and scope (e.g., "FIELD-REGISTER compliance — orientation and lens fields"). A fat item enumerates the specific rules (e.g., "orientation.frame must be self-directed; orientation.serves must name a beneficiary explicitly"). Fat items = fail even if the CONTRACT block is also present. The no-restatement rule applies in the declaration layer as it does in execution phases. C-20 implies C-19; if C-19 fails, C-20 fails. |
| C-21 | Every phase-cited CONTRACT block has at least one AUDIT-CHECKLIST item | structure | aspirational | For each CONTRACT block cited by at least one content-producing phase step, the pre-declared AUDIT-CHECKLIST contains at least one item that names that CONTRACT block. A CONTRACT block that is cited in a phase step but absent from the audit declaration = unannounced check = fail. CONTRACT blocks that are defined but never cited by any phase (inactive blocks) are exempt. C-21 implies C-20; if C-20 fails, C-21 fails. |
| C-22 | AUDIT-CHECKLIST header declares its own format constraint | structure | aspirational | The pre-declared AUDIT-CHECKLIST opens with an explicit meta-statement that names the format rule it follows — e.g., "Items name the CONTRACT block and validation scope only — no rule enumeration." A checklist that follows the thin-reference format (C-20 pass) but carries no such header declaration is structurally opaque: the format constraint is enforced but not announced. With C-22, the format rule is declared within the structure itself, making the checklist self-documenting about its own constraint. Absence of a format declaration header = fail, even when all items are thin. C-22 implies C-20; if C-20 fails, C-22 fails. |
| C-23 | Rule content is quarantined to the three canonical locations | structure | aspirational | CONTRACT rule content appears in exactly three locations in the skill: (1) the CONTRACT block where it is defined, (2) the phase step that cites it by name, (3) the AUDIT-CHECKLIST item that references it by name. No rule content appears anywhere else — not in preamble prose, introductory summaries, structural annotations, meta-commentary, or inline explanatory asides. A skill that passes C-19 (thin phases) and C-20 (thin checklist items) but restates rule content in an intro paragraph or structural comment = fail. The three-location rule is satisfied only when rule content is absent from all locations other than its canonical three. C-23 implies C-19 + C-20; if either prerequisite fails, C-23 fails. |

---

## Scoring Worksheet

```
Essential (5 criteria, 12 pts each):    ___ / 5   =>  ___ * 60 / 5  = ___
Recommended (2 criteria, 15 pts each):  ___ / 2   =>  ___ * 30 / 2  = ___
Aspirational (16 criteria, 0.625 pts each): ___ / 16  =>  ___ * 10 / 16 = ___

Composite score: ___

Formula: (essential_passed * 12) + (recommended_passed * 15) + (aspirational_passed / 16 * 10)
```

**Rubric version:** v7 | **Scoring:** `5 Essential @ 12pt + 2 Recommended @ 15pt + 16 Aspirational @ 0.625pt`

| Band | Score | Meaning |
|------|-------|---------|
| Golden | all essential + >= 80 | Role file is production-ready |
| Passing | all essential + 60–79 | Usable; recommended gaps noted |
| Failing | any essential fails | Not useful as a role artifact |
```

---

**Two new criteria added, denominator 14 → 16:**

- **C-22** catches the self-documentation gap: a checklist that is thin (C-20 pass) but structurally opaque about *why* it is thin — the format rule must be stated in the header, not just followed implicitly.
- **C-23** closes the remaining restatement surface: C-19 and C-20 cover phases and checklist items, but preamble and meta-commentary are unguarded. A skill can pass both while restating rule content in an intro section. C-23 quarantines rule content to exactly three canonical locations across the entire skill.

The R8 adversarial target follows directly: a skill that passes C-18 through C-21 (bidirectional, thin phases, thin items, complete coverage) but either omits the checklist format header (C-22 fail) or restates rule content in an introductory summary (C-23 fail).
