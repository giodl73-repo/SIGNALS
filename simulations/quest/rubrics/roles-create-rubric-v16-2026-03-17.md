v16 is written to `simulations/quest/rubrics/roles-create-rubric-v16-2026-03-17.md`.

---

**What changed: one new criterion, C-35**

**C-35 — Gate verdict surface is simultaneously bare (C-29 ∧ C-30)**

R17's V-01/V-02/V-03/V-04 matrix fully isolated C-29, C-30, and C-31 in all pairwise combinations. The gap exposed: **V-03 has no criterion it passes that V-01 doesn't.** V-03 achieves C-29 PASS + C-30 PASS + C-31 FAIL — the verdict surface is clean in both directions — but there's no criterion that names this state. C-32 (triple purity) fails because C-31 fails; C-29 and C-30 pass individually; nothing names the bilateral conjunction. C-35 fills that gap.

**Pass condition:** Both verdict branches carry bare tokens simultaneously. C-35 = C-29 ∧ C-30. C-35 implies C-29 and C-30; if either fails, C-35 fails. C-32 implies C-35; if C-35 fails, C-32 fails. So C-32 = C-35 ∧ C-31.

**Three consequences:**

| Effect | v15 | v16 |
|--------|-----|-----|
| C-29 alone deduction count | 4 | **5** (C-35 adds one) |
| C-30 alone deduction count | 3 | **4** (C-35 adds one) |
| C-30 + C-31 combined | 5 | **6** (highest pairwise) |
| V-01 vs V-03 ranking | V-01 > V-03 (24 vs 23) | **tied** at 24/28 |
| Denominator | 27 | **28** |

C-31 alone stays at 4 deductions — C-35 is unaffected when verdict branches are bare, so the pivot cost is unchanged. C-29 now exceeds C-31 as the single highest-cost failure mode (5 vs 4).
bination (C-30 + C-31) is the new highest-cost pairwise combination.** V-04 fails C-30 (annotated PASS branches) and C-31 (verbose conditions) independently — the two criteria govern different gate surfaces and have no cascade between them. But their combination cascades to C-35 (via C-30), C-32 (via C-35 and C-31), C-33 (via C-31), and C-34 = 6 deductions total. With C-35 added, C-29 alone costs 5 deductions (was 4 in v15); C-30 alone costs 4 (was 3); C-31 alone costs 4 (unchanged). C-30 + C-31 combined costs 6 deductions. Updated deduction depth table added below.

**Why C-35 is not redundant with C-32:** C-35 passes when C-32 fails (V-03 case: bare verdict branches, verbose condition). V-03 achieves C-35 PASS but C-32 FAIL — demonstrating that C-35 is a strict prerequisite for C-32 with a non-empty pass space that C-32 doesn't cover. C-32 implies C-35, not the reverse.

**Scoring changes:**

| | v15 | v16 |
|--|-----|-----|
| Denominator | 27 | 28 |
| Per-criterion weight | 0.3704 | 0.3571 |
| V-05 target | 27/27 = 100.00 | 28/28 = 100.00 |

**Updated R17 scores under v16:**

| Variation | v15 score | v16 score | C-35 verdict | Note |
|-----------|-----------|-----------|--------------|------|
| V-01 | 24/27 | 24/28 | FAIL | C-30 FAIL -> C-35 FAIL; pass count unchanged |
| V-02 | 23/27 | 23/28 | FAIL | C-29 FAIL (cascade to C-30) -> C-35 FAIL; pass count unchanged |
| V-03 | 23/27 | 24/28 | PASS | C-29 PASS + C-30 PASS -> C-35 PASS; V-03 gains one pass |
| V-04 | 22/27 | 22/28 | FAIL | C-30 FAIL -> C-35 FAIL; pass count unchanged |
| V-05 | 27/27 | 28/28 | PASS | All criteria pass; C-35 adds one pass |

V-01 and V-03 now tie at 24/28 -- a structural consequence of C-35 naming exactly what V-03 achieves (clean verdict surface) and what V-01 loses (C-35 FAIL from C-30 FAIL). Under v15, they were unequal (24 vs 23); under v16, C-35 equalizes them.

---

## Essential Criteria (60%)

All 5 must pass for the output to be useful.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | Role file written to correct path | format | essential | A file exists at `.roles/{area}/{subrole}.md` after the skill runs. Content shown only in chat with no file write = fail. File written to any other path (current directory, `simulations/`, etc.) = fail. |
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
| C-15 | Audit checks are distributed as in-phase gates | behavior | aspirational | Each generation phase embeds its own explicit pass/fail gate; execution halts at the failing phase before advancing. A terminal-only audit (all checks batched at Phase 5 or equivalent) = pass for C-13, fail for C-15. In-phase gates at each content-producing step, with Phase 5 serving as final confirmation rather than sole checkpoint = pass. Gate form is structural (inline annotation or gate table); both are valid. |
| C-16 | Audit obligations are pre-declared before generation | behavior | aspirational | The skill declares its complete audit checklist -- naming each criterion by ID or label -- before any content generation begins. The Phase 5 execution then runs against the pre-declared list. Defining the checklist for the first time at Phase 5 = pass for C-13, fail for C-16. Pre-declaration at skill entry (before Phase 1) with Phase 5 executing the declared list = pass. |
| C-17 | Hard constraints are extracted into named CONTRACT sections | structure | aspirational | Key invariants (field register rules, audit checklist, column header rules) are extracted into explicitly named CONTRACT: blocks that the audit phase references by name. Constraints expressed only as inline prose within instructional steps = fail. Named CONTRACT: blocks defined at the top level of the skill and cited by name in the audit phase = pass. |
| C-18 | Declaration-to-gate traceability is bidirectional | structure | aspirational | The pre-declared audit checklist names the gate phase that executes each item (e.g., "verified at Gate 3a"), AND each in-phase gate cites the declaration item it validates (e.g., `Gate 3a [B]`). One-directional annotation only = pass for C-15 and/or C-16, fail for C-18. Both ends annotated with matching identifiers = pass. The backward reference may appear as an inline suffix (`[B]`) or as an `[ID]` column in a gate table -- structural form is neutral; presence is the requirement. C-18 implies both C-15 and C-16; if either prerequisite fails, C-18 fails. |
| C-19 | Content-producing phases are thin CONTRACT citations | structure | aspirational | Every content-producing phase step references a CONTRACT block by name and contains no restatement of the rules within that block. A phase step that copies or paraphrases any rule already defined in a CONTRACT block = fail, even if the CONTRACT block is also present. All phase steps reduced to CONTRACT-name citation form = pass. REGISTER-NEUTRAL: declarative phrasing ("CONTRACT: X governs this phase") and imperative phrasing ("Apply CONTRACT: X") are equally valid thin citations -- the violation is rule restatement, not phrasing style. C-19 implies C-17; if C-17 fails, C-19 fails. |
| C-20 | AUDIT-CHECKLIST items are thin CONTRACT references, not rule enumerations | structure | aspirational | Each criterion entry in the pre-declared AUDIT-CHECKLIST identifies what to check by naming the CONTRACT block and validation scope -- it does not reproduce the CONTRACT block rule content. A thin item names the block and scope (e.g., "FIELD-REGISTER compliance -- orientation and lens fields"). A fat item enumerates the specific rules (e.g., "orientation.frame must be self-directed; orientation.serves must name a beneficiary explicitly"). Fat items = fail even if the CONTRACT block is also present. The no-restatement rule applies in the declaration layer as it does in execution phases. C-20 implies C-19; if C-19 fails, C-20 fails. |
| C-21 | Every phase-cited CONTRACT block has at least one AUDIT-CHECKLIST item | structure | aspirational | For each CONTRACT block cited by at least one content-producing phase step, the pre-declared AUDIT-CHECKLIST contains at least one item that names that CONTRACT block. A CONTRACT block that is cited in a phase step but absent from the audit declaration = unannounced check = fail. CONTRACT blocks that are defined but never cited by any phase (inactive blocks) are exempt. ORDER-NEUTRAL: CONTRACT block ordering in the CONTRACTS section and row ordering in the AUDIT-CHECKLIST have no effect on this criterion -- coverage is the invariant. C-21 implies C-20; if C-20 fails, C-21 fails. |
| C-22 | AUDIT-CHECKLIST header declares its own format constraint | structure | aspirational | The pre-declared AUDIT-CHECKLIST opens with an explicit meta-statement that names the format rule it follows -- e.g., "Items name the CONTRACT block and validation scope only -- no rule enumeration." A checklist that follows the thin-reference format (C-20 pass) but carries no such header declaration is structurally opaque: the format constraint is enforced but not announced. With C-22, the format rule is declared within the structure itself, making the checklist self-documenting about its own constraint. Absence of a format declaration header = fail, even when all items are thin. C-22 implies C-20; if C-20 fails, C-22 fails. |
| C-23 | Rule content is quarantined to the three canonical locations | structure | aspirational | CONTRACT rule content appears in exactly three locations in the skill: (1) the CONTRACT block where it is defined, (2) the phase step that cites it by name, (3) the AUDIT-CHECKLIST item that references it by name. No rule content appears anywhere else -- not in preamble prose, introductory summaries, meta-commentary, or inline explanatory asides. A skill that passes C-19 (thin phases) and C-20 (thin checklist items) but restates rule content in an intro paragraph = fail. STRUCTURAL-SCAFFOLDING EXEMPTION (R15 confirmed): gate condition text and verdict branch content are structural scaffolding -- they identify which check is running and signal the outcome; they are not phase steps, checklist items, or CONTRACT blocks. Rule content appearing in gate condition text is a C-31 violation, not a C-23 violation. C-23 and C-31 are independent; verbose gate conditions do not cascade to C-23. C-23 implies C-19 + C-20; if either prerequisite fails, C-23 fails. |
| C-24 | Audit gate structural form is homogeneous across all phases | structure | aspirational | All audit gates across all content-producing phases use the same structural form: either all inline annotations (`-> Gate N [ID]: ... PASS / FAIL`) or all gate tables (columns: Gate / [ID] / Criterion / Verdict). Both canonical forms are valid; the requirement is consistency. A skill that mixes inline annotations in some phases and gate tables in others = fail. V-04 demonstrates full gate-table consistency; V-01/V-02/V-03/V-05 demonstrate full inline-annotation consistency. C-24 implies C-15 and C-18; if either prerequisite fails, C-24 fails. |
| C-25 | Content-producing phase bodies achieve minimum surface | structure | aspirational | Each content-producing phase body is expressed as the minimum statement needed: one CONTRACT citation (in any valid register -- declarative or imperative) plus one artifact or action reference, with no bridging prose, no fix-and-retry workflow text, and no narrative expansion of what the CONTRACT does. V-02 demonstrates the canonical minimum form ("CONTRACT: X applied. [one artifact reference]."). A phase body that satisfies C-19 (no restatement) but includes additional prose beyond citation + artifact reference = fail. The gate annotation (inline or table) is structural scaffolding and does not count against minimum surface. C-25 implies C-19; if C-19 fails, C-25 fails. |
| C-26 | CONTRACTS block ordering mirrors first-citation sequence across phases | structure | aspirational | CONTRACT definitions appear in the CONTRACTS block in the same order as they are first cited when reading phases from Phase 0 onward. The first CONTRACT cited in Phase 0 is defined first in CONTRACTS; the next new CONTRACT first cited in Phase 1 is defined second; and so on. Any CONTRACT defined out of first-citation sequence = fail. This makes the CONTRACTS block self-indexing relative to execution: a reader scanning CONTRACTS top-to-bottom encounters each definition exactly when its first phase reference would be reached. C-26 implies C-17; if C-17 fails, C-26 fails. |
| C-27 | Phase body content opens with the CONTRACT citation | structure | aspirational | The first substantive text in each content-producing phase body is the CONTRACT citation (e.g., "CONTRACT: FIELD-REGISTER applied." or "Apply CONTRACT: FIELD-REGISTER."). Any text between the phase section heading and the CONTRACT citation -- process description headers, purpose statements, context framing, or connector prose -- = fail. Phase section headings and gate annotations are structural scaffolding and are exempt. A skill that passes C-25 (minimum surface) trivially passes C-27. C-27 implies C-25; if C-25 fails, C-27 fails. |
| C-28 | Correction and retry instructions appear in gate fail conditions, not in phase body narrative | structure | aspirational | All fix-and-retry instructions appear in the gate's fail branch or fail condition annotation -- not in phase body prose. A phase body that contains "If Gate N fails, apply the correction action... and re-run the failed gate before advancing" or equivalent conditional retry text = fail, regardless of whether the gate annotation itself also specifies a fail path. The gate is the canonical location for correction logic; the body is the canonical location for the CONTRACT citation and artifact reference only. A skill that passes C-25 (minimum surface) trivially passes C-28. C-28 implies C-25; if C-25 fails, C-28 fails. |
| C-29 | Gate FAIL branches carry verdict tokens only | structure | aspirational | Every in-phase gate annotation across all content-producing phases is limited to verdict tokens (PASS / FAIL or equivalent) in its FAIL branch. No correction instruction, repair directive, or "before advancing" clause appears in any gate FAIL branch. Phase 5 (or equivalent final confirmation phase) is the sole correction path -- it handles repair implicitly by re-running the pre-declared AUDIT-CHECKLIST against current state. A gate annotation of the form `-> Gate 3 [FR]: FIELD-REGISTER -- 12-field completeness -- FAIL: Regenerate missing fields before advancing` = fail, even though it passes C-28 (correction is in the gate, not the body). A gate annotation of the form `-> Gate 3 [FR]: FIELD-REGISTER -- 12-field completeness -- PASS / FAIL` = pass. C-29 implies C-28 and C-15; if either prerequisite fails, C-29 fails. A skill that passes C-25 (minimum surface) and C-29 (verdict-only FAIL gates) has no correction prose anywhere in its phase structure -- Phase 5 is the universal repair loop. |
| C-30 | Gate PASS branches carry verdict tokens only | structure | aspirational | Every in-phase gate annotation across all content-producing phases is limited to verdict tokens (PASS / FAIL or equivalent) in its PASS branch. No affirmation text, confirmation summary, "all checks satisfied" annotation, or equivalent positive commentary appears in any gate PASS branch. A gate annotation of the form `-> Gate 3 [FR]: FIELD-REGISTER -- 12-field completeness -- PASS: Frontmatter complete and correctly typed. / FAIL` = fail, even though it passes C-29 (FAIL branch is verdict-only). A gate annotation of the form `-> Gate 3 [FR]: FIELD-REGISTER -- 12-field completeness -- PASS / FAIL` = pass. Gates are pure signal in both directions -- neither verdict branch carries prose. C-30 implies C-29; if C-29 fails, C-30 fails. CASCADE DIRECTIONALITY (R15 confirmed): the C-29->C-30 cascade is unconditional and forward-only. Bare PASS branches cannot rescue C-30 when FAIL branches carry correction directives; C-30 fails regardless of PASS branch content when C-29 fails. Conversely, annotated PASS branches (C-30 fail) do not cascade to C-29 -- C-29 is scored independently on FAIL branch content alone. A skill that passes C-25 (minimum surface), C-29 (verdict-only FAIL gates), and C-30 (verdict-only PASS gates) has eliminated annotation prose from all structural positions. Phase 5 is the sole location where state is interpreted and acted upon. |
| C-31 | Gate condition text is a CONTRACT-citation expression, not a rule restatement | structure | aspirational | The condition text in every in-phase gate annotation identifies the CONTRACT block and check scope by reference -- it does not enumerate specific fields, values, or rules already defined in a CONTRACT block. A gate condition of "FIELD-REGISTER -- 12-field completeness" = pass (CONTRACT block name + scope). A gate condition of "All 12 frontmatter fields present and correctly typed" = fail (rule-level field enumeration in the condition, even without quoting rules verbatim). A gate condition naming specific YAML keys, type constraints, or value requirements drawn from CONTRACT rule content = fail. This extends the no-restatement principle (C-19, C-20) to the gate condition surface: the gate condition answers "which CONTRACT check is being executed"; the CONTRACT block answers "what that check entails." SUBSTRATE LINK (R15 confirmed): verbose gate conditions supply the specific language that PASS-branch affirmations echo back. Thin conditions eliminate this substrate, making PASS-branch affirmations structurally unmotivated. C-31 and C-30 are causally linked (thin conditions protect against affirmation drift) but independently scored. C-31 implies C-17 (CONTRACT blocks must exist to be cited by reference) and C-19; if either fails, C-31 fails. C-31 is independent of C-29 and C-30 -- gate condition thinness and verdict branch thinness govern different surface locations within the same annotation; all three must pass for the gate to be fully thin. A skill that passes C-29 + C-30 + C-31 has a gate of the canonical form `-> Gate N [ID]: {CONTRACT-reference} -- PASS / FAIL` with no prose in any position. PIVOT POINT (R16 confirmed): C-31 is the shared prerequisite for both C-32 (gate triple purity) and C-33 (no-restatement surface closure). A single C-31 failure cascades to C-32 fail + C-33 fail + C-34 fail = 4 total deductions. |
| C-32 | Full gate triple purity: condition, FAIL branch, and PASS branch simultaneously carry no prose | structure | aspirational | All three gate annotation surfaces are clean across every in-phase gate: thin condition (C-31 pass), bare FAIL branch (C-29 pass), and bare PASS branch (C-30 pass). The gate annotation is of the canonical form `-> Gate N [ID]: {CONTRACT-reference} -- PASS / FAIL` with no prose in any of the three positions. Any prose in any position of any gate = fail. This criterion scores the conjunction property: it does not replace the individual deductions at C-29, C-30, C-31, and C-35, but adds a deduction when any of those individual criteria fails -- confirming that triple purity was not achieved. Full triple purity requires all three surfaces clean independently and simultaneously. C-32 implies C-35, C-31, C-29, and C-30; if any fails, C-32 fails. DECOMPOSITION (v16): C-32 = C-35 (verdict surface clean) AND C-31 (condition surface clean). C-35 subsumes C-29 AND C-30; a C-32 pass requires a clean verdict surface (C-35 pass) AND a thin condition (C-31 pass) as the two independent components of the gate annotation layer. |
| C-33 | No-restatement surface closure: all three thin-reference surfaces simultaneously enforce rule quarantine | structure | aspirational | The three no-restatement criteria -- C-19 (phase body), C-20 (AUDIT-CHECKLIST items), and C-31 (gate conditions) -- govern the complete set of thin-reference surfaces in the skill. A skill that passes all three has closed the no-restatement property: CONTRACT rule content appears in exactly one canonical location per rule, with no restatement at any of the three citation surfaces. This criterion formalizes the closure as a conjunction independent of C-32. A variation can achieve C-33 (thin citations everywhere) while failing C-32 (some gate has annotated verdict branches). A variation can achieve C-32 (bare gate verdict branches and thin conditions) while failing C-33 (phase body or checklist items restate rules). Both conjunctions are required for full canonical discipline at both the citation and annotation layers. C-33 implies C-19, C-20, and C-31; if any fails, C-33 fails. A skill that passes C-33 has complete rule quarantine: CONTRACT content appears in exactly one canonical location -- the CONTRACT block itself -- with no restatement at any citation surface. |
| C-34 | Full canonical discipline: gate annotation layer and citation surface layer simultaneously clean | structure | aspirational | Both C-32 (full gate triple purity) and C-33 (no-restatement surface closure) pass simultaneously. The skill has eliminated prose from all three gate annotation surfaces (condition, FAIL branch, PASS branch) and from all three thin-reference citation surfaces (phase body, checklist item, gate condition) at the same time. A skill that passes C-32 but fails C-33 (gate annotations clean, phase body or checklist items restate rules) = fail. A skill that passes C-33 but fails C-32 (citations thin everywhere, PASS branches carry affirmation text) = fail. C-34 adds a conjunction-level deduction above any individual C-32 or C-33 failure -- confirming that the full canonical form was not achieved at both layers simultaneously. C-34 implies C-32 and C-33; if either fails, C-34 fails. A skill that passes C-34 has achieved complete canonical discipline: no prose in any gate annotation surface, no rule restatement in any citation surface, with all rule content in exactly one canonical location -- the CONTRACT block. C-34 is the ceiling criterion: a skill that passes C-34 has satisfied every structural criterion in the aspirational tier. |
| C-35 | Gate verdict surface is simultaneously bare: both PASS and FAIL branches carry verdict tokens only | structure | aspirational | Both verdict branches across every in-phase gate annotation carry bare tokens simultaneously -- no affirmation text in the PASS branch (C-30) and no correction directive in the FAIL branch (C-29). C-35 is the verdict-surface conjunction: C-29 AND C-30. Where C-29 tests the FAIL branch in isolation and C-30 tests the PASS branch in isolation, C-35 tests that the bare-token decision is applied to both verdict branches at the same time. The three distinct verdict-surface states are: (1) both bare -- C-35 PASS, exemplified by V-05; (2) annotated PASS, bare FAIL -- C-35 FAIL even though C-29 passes, exemplified by V-01; (3) annotated FAIL, bare PASS (bare PASS cannot rescue C-30 by cascade) -- C-35 FAIL, both C-29 and C-30 fail, exemplified by V-02. A skill in state (2) satisfies C-29 but fails C-30 and C-35; a skill in state (3) fails C-29, C-30, and C-35 by the C-29 cascade. Only state (1) achieves C-35. The canonical gate form `-> Gate N [ID]: {CONTRACT-reference} -- PASS / FAIL` with no prose on either verdict branch satisfies C-35. C-35 implies C-29 and C-30; if either fails, C-35 fails. C-32 implies C-35; if C-35 fails, C-32 fails. V-03 (R17) demonstrates that C-35 PASS and C-32 FAIL can coexist: bare verdict branches with verbose gate conditions satisfies the verdict surface criterion (C-35) but fails triple purity (C-32) -- the two criteria are independently scored with C-35 as a proper subset of C-32's pass requirements. |

---

## Scoring Worksheet

```
Essential (5 criteria, 12 pts each):         ___ / 5   =>  ___ * 60 / 5  = ___
Recommended (2 criteria, 15 pts each):       ___ / 2   =>  ___ * 30 / 2  = ___
Aspirational (28 criteria, 0.3571 pts each): ___ / 28  =>  ___ * 10 / 28 = ___

Composite score: ___

Formula: (essential_passed * 12) + (recommended_passed * 15) + (aspirational_passed / 28 * 10)
```

**Rubric version:** v16 | **Scoring:** `5 Essential @ 12pt + 2 Recommended @ 15pt + 28 Aspirational @ 0.3571pt`

| Band | Score | Meaning |
|------|-------|---------|
| Golden | all essential + >= 80 | Role file is production-ready |
| Passing | all essential + 60-79 | Usable; recommended gaps noted |
| Failing | any essential fails | Not useful as a role artifact |

---

**Criterion surface map:**

- C-19 governs *phase step content*: no CONTRACT rule restatement in phase steps
- C-20 governs *audit declaration items*: same no-restatement rule applied to checklist entries
- C-21 governs *completeness* of the declaration: every active CONTRACT block pre-declared
- C-22 governs *self-documentation* of the checklist: the format constraint is declared within the structure
- C-23 governs *the full skill surface*: no rule content outside the three canonical locations (gate condition text is structural scaffolding exempt from C-23 scope -- governed by C-31 instead)
- C-24 governs *gate structural consistency*: a single gate form used across all phases
- C-25 governs *phase surface area*: minimum viable phrase length -- citation + artifact, nothing more
- C-26 governs *CONTRACT definition ordering*: definitions appear in first-citation sequence
- C-27 governs *phase body entry point*: the CONTRACT citation is the first element -- no opener, header, or process description precedes it within the body
- C-28 governs *correction logic placement*: fix-and-retry instructions belong in gate fail conditions, not phase body narrative
- C-29 governs *gate FAIL annotation surface*: gate FAIL branches carry only verdict tokens -- no correction instruction, repair directive, or "before advancing" clause; Phase 5 is the sole correction path
- C-30 governs *gate PASS annotation surface*: gate PASS branches carry only verdict tokens -- no affirmation text, confirmation summary, or "all checks satisfied" annotation; gates are pure signal in both directions; C-29->C-30 cascade is forward-only and unconditional
- C-31 governs *gate condition content*: gate condition text identifies the CONTRACT block and check scope by reference -- no rule-level field enumeration, quoted rule text, or specific value constraint; thin conditions eliminate the substrate for PASS-branch affirmation drift; C-31 is the pivot shared prerequisite for both C-32 and C-33
- C-32 governs *full gate triple purity*: all three gate annotation surfaces (condition, FAIL branch, PASS branch) simultaneously carry no prose -- the conjunction of C-35 (verdict surface) AND C-31 (condition surface); C-35 is the intermediate verdict-surface conjunction introduced in v16
- C-33 governs *no-restatement surface closure*: all three thin-reference surfaces (phase body, checklist item, gate condition) simultaneously enforce rule quarantine -- the conjunction of C-19 + C-20 + C-31
- C-34 governs *full canonical discipline*: the meta-conjunction of C-32 (gate annotation layer) and C-33 (citation surface layer) -- both layers simultaneously clean; the ceiling criterion of the aspirational tier
- C-35 governs *gate verdict surface*: both PASS and FAIL verdict branches simultaneously carry bare tokens only -- the conjunction of C-29 AND C-30; names the partial conjunction that sits between the individual branch criteria (C-29, C-30) and full gate triple purity (C-32); a skill can pass C-35 while failing C-32 when gate conditions are verbose (V-03 pattern, R17)

**C-25 decomposition:** C-27 and C-28 together decompose the C-25 failure space into two independent sub-types. A skill that fails C-25 may fail C-27 (opener text), C-28 (retry text), or both -- the violations are orthogonal. A skill that passes C-25 (minimum surface satisfied) trivially passes both C-27 and C-28.

**C-28 decomposition:** C-29 refines C-28's pass space. A C-28 pass means correction prose is not in the body -- it may or may not be in gate FAIL branches. C-29 resolves this ambiguity: the canonical form has correction prose nowhere (gate or body).

**C-29 decomposition:** C-30 refines C-29's pass space. A C-29 pass means gate FAIL carries no correction prose -- gate PASS may or may not carry affirmation prose. C-30 resolves this ambiguity: the canonical form has annotation prose nowhere in either verdict branch. C-35 further refines the conjunction: where C-29 and C-30 each govern one verdict branch independently, C-35 tests that the bare-token decision is applied bilaterally. A C-35 pass collapses the C-29 + C-30 question into a single verdict: the verdict surface is entirely prose-free. CASCADE NOTE: C-30 fails when C-29 fails (forward cascade, confirmed unconditional by R15); C-29 does not fail when C-30 fails (no reverse cascade).

**C-30 decomposition:** C-31 is independent of C-30, not a refinement. A C-30 pass means gate verdict branches carry no prose -- gate condition text may or may not carry rule-level enumeration. C-31 governs a different gate surface location. A skill that passes C-29 + C-30 (bare verdict tokens in both branches) satisfies C-35 (verdict surface clean) but may still fail C-31 (rule-enumerating gate condition) and therefore fail C-32. V-03 (R17) is the canonical instance: C-35 PASS + C-31 FAIL + C-32 FAIL. The full gate purity property requires both the verdict surface (C-35) and the condition surface (C-31) to be simultaneously clean, which is what C-32 formalizes.

**C-31 decomposition:** C-32 and C-33 both depend on C-31 as a prerequisite. C-32 requires C-35 + C-31 (full gate triple purity). C-33 requires C-31 + C-19 + C-20 (no-restatement surface closure). C-31 is the pivot: the only single criterion whose failure simultaneously breaks two independent conjunction criteria (C-32 and C-33), and through them, C-34. A skill that passes C-31 satisfies a prerequisite for both conjunctions but achieves neither unless the co-prerequisites also pass. A skill that fails C-31 alone loses C-31 + C-32 + C-33 + C-34 = 4 total deductions.

**C-32 decomposition (v16 update):** C-32 = C-35 (verdict surface) AND C-31 (condition surface). C-35 is the new intermediate that C-32 implies. A C-32 pass means all three gate annotation surfaces are clean -- the conjunction is now more precisely expressed as two clean surfaces: verdict (C-35) and condition (C-31). C-34 adds the meta-conjunction level above C-32: a C-32 pass means gate annotations are clean; citations may or may not restate rule content in phase bodies or checklist items. C-33 governs those surfaces independently.

**C-33 decomposition:** C-34 adds the meta-conjunction level above C-33. A C-33 pass means all three citation surfaces are thin -- gate PASS/FAIL branches may or may not carry annotation prose. C-32 governs those surfaces independently. C-34 formalizes the conjunction of both.

**C-35 decomposition (v16):** C-35 names the partial conjunction of C-29 AND C-30. A C-35 pass means the verdict surface is fully bare -- no prose in either verdict branch direction. C-35 PASS does not imply C-32 PASS (the condition surface may still be verbose, as in V-03). C-32 PASS implies C-35 PASS (triple purity requires a clean verdict surface). The three verdict-surface states map cleanly to: (1) both bare = C-35 PASS; (2) annotated PASS + bare FAIL = C-35 FAIL with C-29 PASS; (3) annotated FAIL (cascade to C-30) = C-35 FAIL with C-29 FAIL. C-35 gives a name to what V-03 achieves: a partially-clean gate that has disciplined its verdict branches but not its condition text.

**No-restatement convergence:** C-19 (phase body), C-20 (checklist items), and C-31 (gate conditions) together enforce the no-restatement rule across all three thin-reference surfaces. C-33 is the conjunction criterion: a skill that passes C-33 has a single canonical rule location for every CONTRACT constraint -- the CONTRACT block itself -- with no restatement at any citation surface.

**Cascade asymmetry summary (R15 + R16 + R17 confirmed):**
- Annotating FAIL branches (C-29 fail): C-29 + C-30 (cascade) + C-35 + C-32 + C-34 = 5 deductions (v16: +1 vs v15 due to C-35)
- Annotating PASS branches only (C-30 alone): C-30 + C-35 + C-32 + C-34 = 4 deductions (v16: +1 vs v15 due to C-35)
- Verbose gate conditions (C-31 alone): C-31 + C-32 + C-33 + C-34 = 4 deductions (unchanged; C-35 unaffected when verdict branches are bare)
- Annotating PASS branches AND verbose conditions (C-30 + C-31): C-30 + C-31 + C-35 + C-32 + C-33 + C-34 = 6 deductions (R17 V-04 pattern; highest pairwise combination)
- Full canonical compliance (all 28 pass): C-35 PASS + C-32 PASS + C-33 PASS + C-34 PASS (all conjunction criteria satisfied)

**Deduction depth table (v16):**

| Single failure | Cascade targets | Total deductions |
|----------------|----------------|-----------------|
| C-29 only | C-30, C-35, C-32, C-34 | 5 |
| C-30 only | C-35, C-32, C-34 | 4 |
| C-31 only | C-32, C-33, C-34 | 4 |
| C-30 + C-31 combined | C-35, C-32, C-33, C-34 | 6 |

C-29 is now the single highest-cost failure mode (5 deductions), exceeding C-31 (4 deductions) due to the C-35 conjunction layer. C-30 alone matches C-31 alone at 4 deductions. The C-30 + C-31 combination (V-04 pattern) is the costliest pairwise combination at 6 deductions.

**C-29/C-31 structural distinction (v16 update):** In v15, C-29 and C-31 were equally costly (4 deductions each). With C-35 added, C-29 becomes the single highest-multiplier failure mode (5 deductions) through the cascade C-29 -> C-30 -> C-35 -> C-32 -> C-34. C-31 remains at 4 deductions (C-35 is unaffected by C-31 failure alone when verdict branches are bare). The two paths remain structurally distinct: C-29 breaks the verdict surface forward (C-30 -> C-35 -> C-32 -> C-34); C-31 breaks both layer conjunctions simultaneously through the pivot (C-32 + C-33 -> C-34).

---

**R9 confirmation summary:**

- All 5 variations tied at 100 under v8. The equivalence class of valid skill structures is structurally diverse: declarative register, compact phases, reordered CONTRACTs, tabular gates, and canonical form all achieve the ceiling under 16 criteria.
- C-19 is register-neutral (confirmed by V-01): declarative and imperative phase citations are equally valid thin citations. The violation is rule restatement, not phrasing style. Annotated into C-19 pass condition.
- C-15 and C-18 are format-neutral (confirmed by V-04): tabular gate blocks with an `[ID]` column satisfy both distributed-in-phase and bidirectional traceability. The backward reference is a structural identifier -- not required to appear as inline prose. Annotated into C-18 pass condition.
- C-21 is order-neutral (confirmed by V-03): CONTRACT block ordering and AUDIT-CHECKLIST row ordering have no effect on coverage compliance. Coverage is the invariant; sequence is a presentation choice. Annotated into C-21 pass condition.
- Phase compaction is safe (confirmed by V-02): single-sentence CONTRACT citation + gate annotation preserves all structural criteria. Narrative richness in phase bodies was optional under v8 -- and a failure mode under v9 (C-25).
- Denominator raised to 19. V-05 (canonical form) is the sole v9 target -- the only R9 variation that passes all three new criteria: C-24 (consistent inline gates), C-25 (minimum phase surface), and C-26 (citation-ordered CONTRACTs).

**R11 confirmation summary:**

- All three R11 variations scored below 100 under v9 (max 98.95), confirming C-24/C-25/C-26 as discriminating criteria.
- C-25 failure decomposes into two orthogonal sub-types (confirmed by V-01 vs V-02 contrast): opener text before the citation (V-01/V-03 failure mode) and fix-and-retry prose in the body (V-01/V-03 failure mode). V-02 passes C-25 by having neither. C-27 and C-28 formalize these sub-types as independent criteria.
- C-24/C-25/C-26 cascade independence confirmed (V-03 cascade check): C-25 failure does not imply C-19 failure (connector openers are process narrative, not rule restatement); C-26 failure does not imply C-17 failure (reordering does not remove CONTRACT blocks). All three deductions are independent.
- Denominator raised to 21. V-05 (canonical form) is the sole v10 target -- the only variation that passes C-27 (citation-first phase bodies) and C-28 (no retry text in body narrative) in addition to all prior criteria. V-02 is the highest-scoring failing variation at 19/21 (99.05), correctly reflecting canonical phase body discipline with only gate form and CONTRACTS ordering diverging.

**R12 confirmation summary:**

- Under v10 (21 criteria), V-01 and V-02 tied at 19/21 (99.05). C-29 breaks the tie by distinguishing where correction prose is absent vs. where it is never introduced.
- C-27 and C-19 govern orthogonal properties of the same text (confirmed by V-01): a connector opener before the CONTRACT citation fails C-27 (wrong position) while passing C-19 (no rule restatement). The two criteria decompose phase body violations into content-type (C-19/C-23) and entry-point (C-27) axes independently.
- C-26 and C-28 are orthogonal independent failure axes (confirmed by V-04): CONTRACT definition ordering and phase body surface area can each be violated without affecting the other, combining to exactly 3 deductions (C-25 + C-26 + C-28) with no cascade.
- C-28 / C-29 distinction separates the previously tied variations: V-01 passes C-28 (correction in gate FAIL branch, not body) but fails C-29 (gate FAIL branch carries "FAIL: Add missing fields before advancing.") -> 19/22 (98.64). V-02 fails C-28 (correction in body prose) but passes C-29 (gate annotations are verdict-only) -> 20/22 (99.09).
- Denominator raised to 22. V-05 (canonical form) holds the sole 100 at 22/22. V-02 correctly remains the highest-scoring failing variation under v11 -- gate annotation discipline is canonical, phase body discipline is canonical; only CONTRACTS ordering (C-26) and body retry prose placement (C-28) diverge.

**R13 confirmation summary:**

- All four non-canonical variations fail C-29 in R13 (V-01, V-02, V-03, V-04). This broadens from R12, where only V-01 failed C-29 and V-02 passed -- demonstrating that the gate annotation surface gap is systemic, not incidental.
- C-29 co-occurs with C-25 failures: V-03 fails C-25 + C-28 + C-29; V-04 fails C-25 + C-27 + C-29. Skills with excess phase body surface tend to also carry correction prose in gate FAIL branches -- the two pathologies share an architectural root. The violations are structurally independent (C-25 does not imply C-29) but empirically correlated.
- C-26 failure is isolated: V-02 fails only C-26 and C-29 -- no C-25, C-27, or C-28 failure. CONTRACTS ordering violations can occur independently of all phase body and gate annotation pathologies.
- C-27 failure is isolated: V-04 fails C-25 + C-27 + C-29 with no C-28 failure. A skill may have opener prose before the citation (C-27 fail) without also having correction prose in the body (C-28 pass). C-27 and C-28 are orthogonal, as established in R11.
- The PASS branch gap: R13 confirms C-29 as strongly discriminating but leaves the gate PASS branch ungoverned. V-05's canonical form uses bare verdict tokens on both sides of every gate. C-30 formalizes the PASS branch discipline. C-30 assessment deferred to R14 (requires reviewing gate PASS branch content in R13 variations).
- Denominator raised to 23. V-05 (canonical form) holds the sole 100 at 23/23. The highest-scoring failing variation under v12 is determined after C-30 assessment in R14.

**R14 confirmation summary:**

- C-30 confirmed universally discriminating: all four non-canonical variations fail in R14. The failure pattern is consistent -- PASS branches carry named-field affirmation summaries that restate the gate condition text in confirmation form ("PASS: All 12 frontmatter fields confirmed present.", "PASS: orientation.frame in first-person observational register.", etc.).
- C-30 + C-29 independence confirmed: V-01/V-03/V-04 pass C-29 (bare FAIL branches) while failing C-30 (annotated PASS branches). The asymmetry -- annotating PASS branches while respecting FAIL branch discipline -- confirms PASS-branch annotation is an independent behavioral pattern. V-02 fails both C-29 and C-30, demonstrating that prose in one verdict branch does not require prose in the other.
- Implication chain closure: With C-28 + C-29 + C-30 all governed, annotation prose has been eliminated from all verdict-branch and phase-body positions. Phase 5 is confirmed as the sole interpretive path for correction and repair.
- R14 ranking: V-05 (100.00, 23/23) > V-01 (99.57, 22/23, C-30 only) > V-02 = V-03 (99.13, 21/23, C-29+C-30 and C-26+C-30 respectively) > V-04 (98.70, 20/23, C-25+C-28+C-30).
- New signal from R14: The C-30 violations are PASS branch restatements of verbose gate condition text. Gate conditions enumerating rule-level field checks create the semantic substrate for affirmation restatements in the PASS branch. Making gate conditions thin (CONTRACT reference + scope) eliminates the restatement opportunity. C-31 formalizes gate condition thinness, completing the no-restatement coverage across all three thin-reference surfaces: phase bodies (C-19), checklist items (C-20), and gate conditions (C-31).
- Denominator raised to 24. V-05 (canonical form) targets 24/24 = 100.00 under v13. C-31 retrospective scoring deferred to R15 (gate condition content not isolated in R14 scorecard evidence).

**R15 confirmation summary:**

- C-31 isolation confirmed (V-01 = 23/24): C-31 fires on verbose gate conditions in isolation without cascading to C-23. Gate condition text is structural scaffolding; C-23's three-canonical-locations rule does not govern it. C-31 is the fully independent criterion for the gate condition surface. V-01 scores 99.58, resolving the primary R15 open question.
- C-23 non-cascade confirmed: verbose gate conditions do not trigger C-23. The three canonical rule locations remain: CONTRACT block, thin phase citation, thin checklist item. Gate annotations are structural scaffolding exempt from C-23 scope. C-23 updated with explicit structural-scaffolding exemption.
- C-29->C-30 cascade confirmed hard and directional (V-03 = 21/24, below design estimate of 22/24): the variation was designed for C-31 + C-29 (2 deductions = 22/24). Actual: C-31 + C-29 + C-30 (3 deductions = 21/24). The cascade is unconditional -- bare PASS branches cannot rescue C-30 when FAIL branches carry correction directives.
- Cascade directionality confirmed (V-02 = 22/24, C-31 + C-30): V-02 has annotated PASS branches (C-30 fail) with bare FAIL branches (C-29 pass), demonstrating the reverse cascade does not exist. C-30 can fail independently when C-29 passes.
- V-03 vs V-02 asymmetry confirmed: annotated FAIL branches (V-03, 3 deductions via cascade) are categorically more costly than annotated PASS branches (V-02, 2 deductions with no cascade). The cascade is directional and asymmetric.
- C-31 + C-26 orthogonality confirmed (V-04 = 22/24): gate condition verbosity (C-31) and CONTRACT definition ordering (C-26) are orthogonal across entirely different structural dimensions. Two independent deductions, no cascade.
- C-31 + C-30 substrate link confirmed: verbose gate conditions supply the specific language that PASS-branch affirmations echo back. Thin conditions eliminate this substrate, making affirmation restatements structurally unmotivated. Causally linked but independently scored.
- R15 ranking: V-05 (100.00, 24/24) > V-01 (99.58, 23/24, C-31 only) > V-02 = V-04 (99.17, 22/24, C-31+C-30 and C-31+C-26 respectively) > V-03 (98.75, 21/24, C-31+C-29+C-30).
- Denominator raised to 26. V-05 (canonical form) targets 26/26 = 100.00 under v14. C-32 and C-33 retrospective scoring deferred to R16 (conjunction failure modes not yet isolated in R15 evidence; R15 variations confirm the constituent criteria but do not test conjunction-specific failure modes independently).

**R16 confirmation summary:**

- C-32/C-33 orthogonality confirmed (V-01 = 24/26 under v14, C-30 + C-32 = 2 deductions): V-01 achieves C-33 PASS while failing C-32 FAIL. PASS-branch annotation breaks gate triple purity (C-32) without breaking no-restatement surface closure (C-33), because C-33 depends on C-19 + C-20 + C-31 -- none of which fail when only C-30 fails. The two conjunction criteria are genuinely orthogonal, as designed in v14 but now empirically confirmed.
- C-30 deduction count confirmed (V-01 under v14 = 2; under v15 = 3): PASS-branch annotation alone with C-29 + C-31 passing costs exactly C-30 + C-32 = 2 deductions under v14. Under v15, C-34 adds a third: C-30 + C-32 + C-34 = 3 deductions from C-30 alone.
- C-31 pivot point identified: C-31 is the shared prerequisite for both C-32 (gate triple purity) and C-33 (no-restatement surface closure) -- the only single criterion whose failure simultaneously breaks two independent conjunction criteria. A single C-31 violation cascades to C-32 fail + C-33 fail + C-34 fail = 4 total deductions. C-31 is tied with C-29 as the highest-multiplier single failure mode in the rubric (both produce 4-deduction cascades through structurally distinct paths).
- C-34 closure: V-05 (canonical form) achieves C-34 by simultaneously achieving C-32 and C-33. C-34 is the ceiling criterion -- a skill that passes C-34 has satisfied every structural criterion in the aspirational tier. No structural criterion exists above C-34.
- R16 ranking (under v14): V-05 (100.00, 26/26) > ... > V-01 (24/26, C-30 + C-32).
- Denominator raised to 27. V-05 targets 27/27 = 100.00 under v15.

**R17 confirmation summary:**

- C-35 verdict-surface conjunction (new in v16): R17's five-variation matrix isolates C-29, C-30, and C-31 in all pairwise combinations, revealing that the state "both verdict branches bare, condition verbose" (V-03) has no named criterion in v15. V-03 achieves C-29 PASS + C-30 PASS + C-31 FAIL + C-32 FAIL -- the verdict surface is clean but C-32 fails because the condition surface is verbose. C-35 names this partial conjunction (C-29 AND C-30) and fills the gap between individual branch criteria and full triple purity.
- C-35 + C-32 relationship confirmed: C-35 PASS and C-32 FAIL can coexist (V-03 pattern). C-32 PASS requires C-35 PASS (C-32 implies C-35). C-35 is a named intermediate in the implication chain: C-32 -> C-35 -> (C-29, C-30).
- V-01/V-03 re-equalization: Under v15, V-01 (24/27) outscored V-03 (23/27). Under v16, both score 24/28 -- C-35 adds a FAIL to V-01 (C-30 fail propagates to C-35) and a PASS to V-03 (bare verdict branches earn C-35). The re-equalization is a structural consequence of C-35 correctly naming what V-03 achieves and V-01 misses.
- C-29 cost raised to 5 deductions: With C-35 added, annotating FAIL branches now costs C-29 + C-30 + C-35 + C-32 + C-34 = 5 deductions (was 4 under v15). C-29 becomes the single highest-cost failure mode, exceeding C-31 (4 deductions) for the first time.
- C-30 + C-31 combination cost: V-04 (C-30 FAIL + C-31 FAIL) cascades to C-35 + C-32 + C-33 + C-34 = 6 total deductions under v16. This is the highest pairwise combination in the rubric.
- R17 ranking (under v16): V-05 (100.00, 28/28) > V-01 = V-03 (98.57, 24/28) > V-02 (98.21, 23/28) > V-04 (97.86, 22/28).
- Denominator raised to 28. V-05 targets 28/28 = 100.00 under v16.
