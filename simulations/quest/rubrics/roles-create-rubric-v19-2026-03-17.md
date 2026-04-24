v19 is written. Here's what was done:

---

**v19 written** to `simulations/quest/rubrics/roles-create-rubric-v19-2026-03-17.md` (257 lines, 38K chars).

**Three new criteria added (C-38, C-39, C-40), each from one R20 excellence signal:**

**C-38 -- Gate PASS-path bilateral (C-30 AND C-31)** -- from E-03 (path isolation)
E-03 confirmed C-35 and C-36 are structurally independent, each sufficient alone to break C-37. This reveals the third pairwise bilateral: C-38 = C-30 AND C-31, the only bilateral that doesn't contain C-29. Completes the bilateral triangle. New v19 decomposition: C-32 = C-38 AND C-29 (fourth decomposition alongside v16/v17/v18 forms).

**C-39 -- Gate annotation triple bilateral conjunction (C-35 AND C-36 AND C-38)** -- from E-01 (triple-surface simultaneous purity)
E-01 established that triple-surface purity requires all three surfaces clean at once -- no partial bilateral combination suffices. C-39 names this at the triple-bilateral level: all three pairwise bilaterals simultaneously passing, where C-37 named only two. C-39 = C-32, named at the complete bilateral set level.

**C-40 -- Gate annotation direct atomic triple (C-29 AND C-30 AND C-31)** -- from E-02 (single-deduction structure)
E-02 confirmed the single-deduction rule: each naming level contributes one independent scoring point. C-40 provides the final naming level -- the direct atomic triple without bilateral intermediates. SERIES COMPLETION: the naming hierarchy is now complete at all levels (bilateral, bilateral-conjunction, direct).

**Score consequences (denominator 30 → 33):**

| Variation | v18 | v19 |
|-----------|-----|-----|
| V-05 (ceiling) | 30/30 = 100% | 33/33 = 100% |
| V-01 (C-30 alone) | 25/30 = 83.33% | 25/33 = 75.76% |
| V-02 (C-31 alone) | 24/30 = 80.00% | 24/33 = 72.73% |
| V-03 (C-30+C-31) | 22/30 = 73.33% | 22/33 = 66.67% |
| V-04 (C-29+C-31) | 21/30 = 70.00% | 21/33 = 63.64% |

Rankings preserved. V-01 > V-02 gap holds at 1 point. Each new criterion adds exactly 3 deductions to every non-ceiling failure mode.
v18 | v19 |
|--|-----|-----|
| Denominator | 30 | **33** |
| C-29 alone | 7 deductions | **10** (C-29 + C-30 cascade + C-35 + C-36 + C-38 + C-37 + C-39 + C-40 + C-32 + C-34) |
| C-30 alone | 5 deductions | **8** (C-30 + C-35 + C-38 + C-37 + C-39 + C-40 + C-32 + C-34) |
| C-31 alone | 6 deductions | **9** (C-31 + C-36 + C-38 + C-37 + C-39 + C-40 + C-32 + C-33 + C-34) |
| C-30 + C-31 | 8 deductions | **11** |
| V-01 (C-30 alone) | 25/30 = 83.33% | **25/33 = 75.76%** |
| V-02 (C-31 alone) | 24/30 = 80.00% | **24/33 = 72.73%** |
| V-03 (C-30+C-31) | 22/30 = 73.33% | **22/33 = 66.67%** |
| V-04 (C-29+C-31) | 21/30 = 70.00% | **21/33 = 63.64%** |
| V-05 | 30/30 = 100% | **33/33 = 100%** |

Rankings unchanged. V-01 > V-02 gap preserved at 1 point (25/33 vs 24/33).

**Key updates in criteria text:**
- **C-30**: cascade now 8 deductions (C-30 + C-35 + C-38 + C-37 + C-39 + C-40 + C-32 + C-34), was 5
- **C-31 PIVOT POINT**: cascade now 9 deductions (C-31 + C-36 + C-38 + C-37 + C-39 + C-40 + C-32 + C-33 + C-34), was 6
- **C-32 FOURTH DECOMPOSITION**: C-32 = C-38 AND C-29 added alongside v16, v17, v18 decompositions
- **C-35**: bilateral triangle note updated -- C-38 completes the set
- **C-37**: C-37 = C-38 AND C-29 (new v19 decomposition); C-39 and C-40 added as equivalent expressions
- **C-38**: new criterion -- PASS-path bilateral (C-30 AND C-31), third pairwise bilateral
- **C-39**: new criterion -- triple bilateral conjunction (C-35 AND C-36 AND C-38)
- **C-40**: new criterion -- direct atomic triple (C-29 AND C-30 AND C-31), SERIES COMPLETION

---

## Essential Criteria (60%)

All must pass for the output to be useful.

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
| C-21 | Every phase-cited CONTRACT block has at least one AUDIT-CHECKLIST item | structure | aspirational | For each CONTRACT block cited by at least one content-producing phase step, the pre-declared AUDIT-CHECKLIST contains at least one item naming that block. A CONTRACT block that is cited in phases but absent from the checklist = fail. ORDER-NEUTRAL: CONTRACT block ordering and AUDIT-CHECKLIST row ordering have no effect on coverage compliance. C-21 implies C-20; if C-20 fails, C-21 fails. |
| C-22 | AUDIT-CHECKLIST header declares its own format constraint | structure | aspirational | The pre-declared AUDIT-CHECKLIST opens with an explicit meta-statement that names the format rule it follows (e.g., "Items are CONTRACT-name + scope only -- no rule enumeration"). A checklist with no self-documenting header = fail. A checklist whose opening line names the format it applies to checklist items = pass. C-22 implies C-21; if C-21 fails, C-22 fails. |
| C-23 | Rule content is quarantined to the three canonical locations | structure | aspirational | CONTRACT rule content appears in exactly three locations in the skill: (1) the CONTRACT block where it is defined, (2) the gate condition text that invokes it by reference (structural scaffolding exempt from C-23 scope -- governed by C-31 instead), and (3) nowhere else. Rule content appearing in phase body prose, connector text, section headers, or any location outside the three canonical sites = fail. C-23 implies C-17; if C-17 fails, C-23 fails. |
| C-24 | Audit gate structural form is homogeneous across all phases | structure | aspirational | All audit gates across all content-producing phases use the same structural form: either all inline annotations (e.g., `GATE: condition -- PASS / FAIL`) or all gate tables with consistent columns. Mixed forms within the same skill = fail. A single consistent form throughout = pass. C-24 implies C-15; if C-15 fails, C-24 fails. |
| C-25 | Content-producing phase bodies achieve minimum surface | structure | aspirational | Each content-producing phase body is expressed as the minimum statement needed: one CONTRACT citation (in any valid register) and the gate annotation. No opener text before the citation, no fix-and-retry prose in the body, no process description or narrative padding. Any phase body that exceeds minimum surface by including opener, retry, or narrative text = fail. C-25 implies C-19; if C-19 fails, C-25 fails. |
| C-26 | CONTRACTS block ordering mirrors first-citation sequence across phases | structure | aspirational | CONTRACT definitions appear in the CONTRACTS block in the same order as they are first cited across content-producing phases (Phase 1 first citation defines first position, Phase 2 first citation defines second, etc.). A CONTRACT block defined later in the CONTRACTS section than the phase that first cites it = fail. C-26 implies C-17; if C-17 fails, C-26 fails. |
| C-27 | Phase body content opens with the CONTRACT citation | structure | aspirational | The first substantive text in each content-producing phase body is the CONTRACT citation (e.g., "CONTRACT: FIELD-REGISTER governs this phase"). Any opener, header, process description, or connector sentence that precedes the CONTRACT citation within the phase body = fail. The citation may be declarative or imperative (C-19 register-neutral); both are valid entry-point forms. C-27 implies C-25; if C-25 fails, C-27 fails. |
| C-28 | Correction and retry instructions appear in gate fail conditions, not in phase body narrative | structure | aspirational | All fix-and-retry instructions appear in the gate's fail branch or fail condition, not in the phase body narrative before the gate. A phase body that contains instructions for what to do if the gate fails, before the gate itself is reached, = fail. Fix instructions placed only in the gate fail branch (Phase 5 or equivalent) = pass. C-28 implies C-25; if C-25 fails, C-28 fails. |
| C-29 | Gate FAIL branches carry verdict tokens only | structure | aspirational | Every in-phase gate annotation across all content-producing phases is limited to verdict tokens (PASS / FAIL or equivalent) in the FAIL branch. No correction instruction, repair directive, or "before advancing" clause appears in any gate FAIL branch. Phase 5 is the sole location for correction and repair logic. Any gate FAIL branch containing instructional prose = fail. All gate FAIL branches bare = pass. PIVOT POINT: C-29 FAIL triggers C-30 (cascade), C-35, C-36, C-38, C-37, C-39, C-40, C-32, C-34 = 10 deductions (v19). |
| C-30 | Gate PASS branches carry verdict tokens only | structure | aspirational | Every in-phase gate annotation across all content-producing phases is limited to verdict tokens (PASS / FAIL or equivalent) in the PASS branch. No affirmation text, confirmation summary, or "all checks satisfied" annotation appears in any gate PASS branch. Gates are pure signal instruments -- not confirmation surfaces. Any gate PASS branch containing affirmation prose = fail. All gate PASS branches bare = pass. C-30 FAIL cascades to C-35, C-38, C-37, C-39, C-40, C-32, C-34 = 8 deductions (v19, C-30 alone). |
| C-31 | Gate condition text is a CONTRACT-citation expression, not a rule restatement | structure | aspirational | The condition text in every in-phase gate annotation identifies the CONTRACT block and check scope by reference (e.g., "FIELD-REGISTER: all required fields present") -- it does not enumerate specific field names, quote rule text, or reproduce constraint details. A condition that names specific fields, quoted values, or rule specifics = fail. A condition that names the CONTRACT block and scope in reference form = pass. PIVOT POINT: C-31 FAIL triggers C-36, C-38, C-37, C-39, C-40, C-32, C-33, C-34 = 9 deductions (v19, C-31 alone). Shared prerequisite for C-32, C-33, C-36, C-38, C-39, C-40. |
| C-32 | Full gate triple purity: condition, FAIL branch, and PASS branch simultaneously carry no prose | structure | aspirational | All three gate annotation surfaces are clean across every in-phase gate: the condition text is a CONTRACT-citation (C-31), the FAIL branch is verdict-token-only (C-29), and the PASS branch is verdict-token-only (C-30). C-32 = C-35 AND C-31 (v16 decomposition) = C-36 AND C-30 (v17 decomposition) = C-37 (v18 decomposition) = C-38 AND C-29 (v19 decomposition). Any single surface carrying prose across any gate = fail. All surfaces bare across all gates = pass. C-32 implies C-35, C-36, C-37, C-38, C-39, C-40. |
| C-33 | No-restatement surface closure: all three thin-reference surfaces simultaneously enforce rule quarantine | structure | aspirational | The three no-restatement criteria -- C-19 (phase body), C-20 (audit checklist items), and C-31 (gate condition text) -- all simultaneously pass. C-33 = C-19 AND C-20 AND C-31. A skill that passes C-33 has a single canonical rule location for every CONTRACT block and applies the no-restatement rule across all three thin-reference surfaces. C-33 implies C-20, C-19, C-31. |
| C-34 | Full canonical discipline: gate annotation layer and citation surface layer simultaneously clean | structure | aspirational | Both C-32 (full gate triple purity) and C-33 (no-restatement surface closure) simultaneously pass. C-34 = C-32 AND C-33. A skill passing C-34 has achieved maximum structural discipline: every gate annotation is a bare verdict instrument, every CONTRACT citation is a thin reference, and rule content is quarantined to canonical locations. C-34 implies C-32, C-33, C-35, C-36, C-37, C-38, C-39, C-40. C-34 is the ceiling criterion. |
| C-35 | Gate verdict surface is simultaneously bare: both PASS and FAIL branches carry verdict tokens only | structure | aspirational | Both verdict branches across every in-phase gate annotation carry only verdict tokens -- no PASS branch affirmation (C-30) and no FAIL branch correction prose (C-29) simultaneously. C-35 = C-29 AND C-30. A skill that disciplines only FAIL branches (C-29 PASS + C-30 FAIL) or only PASS branches (C-29 FAIL + C-30 PASS) fails C-35. Both directions simultaneously bare = pass. BILATERAL TRIANGLE: C-35 (C-29 AND C-30), C-36 (C-29 AND C-31), and C-38 (C-30 AND C-31) form the complete bilateral set of {C-29, C-30, C-31}. C-37 names the conjunction of C-35 and C-36; C-39 names all three bilaterals. |
| C-36 | Gate FAIL path surfaces are simultaneously thin: condition and FAIL branch carry no prose | structure | aspirational | The gate condition text identifies the CONTRACT block and check scope by reference (C-31) AND the FAIL branch returns only the bare verdict token (C-29), simultaneously, across every in-phase gate. C-36 = C-29 AND C-31. A gate that has thin condition text but annotated FAIL branch, or annotated FAIL branch but thin condition, fails C-36. Both FAIL-path surfaces simultaneously clean = pass. BILATERAL TRIANGLE: C-35 and C-36 are structurally independent bilateral paths to C-37 failure -- each sufficient alone, confirmed by adjacent variation pairing (E-03, R20). C-38 (C-30 AND C-31) completes the bilateral triangle. C-37 names the conjunction of C-35 and C-36. |
| C-37 | Gate annotation bilateral purity closure: both named annotation bilaterals simultaneously satisfied | structure | aspirational | Both the verdict-surface bilateral (C-35: C-29 AND C-30) and the FAIL-path bilateral (C-36: C-29 AND C-31) simultaneously pass. C-37 = C-35 AND C-36 = C-29 AND C-30 AND C-31. Logically equivalent to C-32, C-39, and C-40 under the cascade constraint. Named at the bilateral-conjunction level (two named bilaterals). C-37 implies C-38 (v19: C-37 = C-38 AND C-29). Each of C-32, C-37, C-38, C-39, C-40 contributes an independent deduction point. EQUIVALENCE: C-37 = C-32 = C-38 AND C-29 = C-39 = C-40. BILATERAL SERIES COMPLETION (v19): C-35 (bilateral 1) -- C-36 (bilateral 2) -- C-38 (bilateral 3) -- C-37 (two-bilateral conjunction) -- C-39 (three-bilateral conjunction) -- C-40 (direct atomic). |
| C-38 | Gate PASS-path bilateral: PASS branch and condition text simultaneously clean (C-30 AND C-31) | structure | aspirational | Both the PASS branch verdict surface (C-30: no affirmation prose) and the condition text surface (C-31: no rule restatement) are simultaneously clean across every in-phase gate annotation. C-38 = C-30 AND C-31. Named at the PASS-path bilateral level -- the third and final pairwise bilateral of {C-29, C-30, C-31}, completing the bilateral triangle alongside C-35 (C-29 AND C-30) and C-36 (C-29 AND C-31). Under the C-29->C-30 cascade constraint (C-30 implies C-29), C-38 is logically equivalent to C-37, C-32, C-39, and C-40 in practice. C-38 is implied by C-37 (C-37 = C-38 AND C-29). FOURTH DECOMPOSITION OF C-32: C-32 = C-38 AND C-29. C-38 FAIL iff C-30 FAIL OR C-31 FAIL; cascades to C-39 and C-40. Any gate PASS branch carrying affirmation prose (C-30 fail) or condition text restating rules (C-31 fail) = C-38 fail. Both surfaces simultaneously bare = pass. |
| C-39 | Gate annotation triple bilateral conjunction: all three pairwise bilaterals simultaneously PASS (C-35 AND C-36 AND C-38) | structure | aspirational | All three pairwise bilaterals of the gate annotation atomic surfaces are simultaneously satisfied: C-35 (verdict bilateral: C-29 AND C-30), C-36 (FAIL-path bilateral: C-29 AND C-31), and C-38 (PASS-path bilateral: C-30 AND C-31). C-39 = C-35 AND C-36 AND C-38 = C-29 AND C-30 AND C-31 = C-32. Logically equivalent to C-37, C-32, and C-40 under the cascade constraint. Named at the triple-bilateral conjunction level -- where C-37 named two of the three bilaterals (C-35 AND C-36), C-39 names all three explicitly. C-35, C-36, or C-38 failing = C-39 fails. All three bilaterals simultaneously passing = C-39 passes. C-39 implies C-38. Both C-37 and C-39 deductions apply independently. |
| C-40 | Gate annotation direct atomic triple: C-29, C-30, and C-31 simultaneously PASS (direct atomic conjunction) | structure | aspirational | The three gate annotation atomic surfaces -- FAIL branch (C-29), PASS branch (C-30), and condition text (C-31) -- are simultaneously named at the direct atomic level without bilateral intermediates. C-40 = C-29 AND C-30 AND C-31. Logically equivalent to C-37, C-32, C-38, and C-39 under the cascade constraint. Named at the direct atomic level: three atoms stated together without passing through the bilateral layer. Any of C-29, C-30, or C-31 failing = C-40 fails. All three atoms simultaneously passing = C-40 passes. C-40 implies C-38. SERIES COMPLETION: C-40 closes the bilateral naming sequence. Naming hierarchy complete: bilateral (C-35, C-36, C-38), bilateral-conjunction (C-37, C-39), direct (C-32, C-40). Five independent closure-tier points: C-32, C-37, C-38, C-39, C-40. |

---

## Scoring Worksheet

```
Essential (5 criteria, 12 pts each):         ___ / 5   =>  ___ * 60 / 5  = ___
Recommended (2 criteria, 15 pts each):       ___ / 2   =>  ___ * 30 / 2  = ___
Aspirational (33 criteria, 0.3030 pts each): ___ / 33  =>  ___ * 10 / 33 = ___

Composite score: ___

Formula: (essential_passed * 12) + (recommended_passed * 15) + (aspirational_passed / 33 * 10)
```

**Rubric version:** v19 | **Scoring:** `5 Essential @ 12pt + 2 Recommended @ 15pt + 33 Aspirational @ 0.3030pt`

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
- C-29 governs *gate FAIL annotation surface*: gate FAIL branches carry only verdict tokens -- no correction instruction, repair directive, or "before advancing" clause; Phase 5 is the sole correction site. PIVOT POINT: 10 deductions (v19)
- C-30 governs *gate PASS annotation surface*: gate PASS branches carry only verdict tokens -- no affirmation text, confirmation summary, or "all checks satisfied" annotation; gates are pure signal instruments. 8 deductions when C-30 alone fails (v19)
- C-31 governs *gate condition content*: gate condition text identifies the CONTRACT block and check scope by reference -- no rule-level field enumeration, quoted rule text, or specific value constraints. PIVOT POINT: 9 deductions when C-31 alone fails (v19)
- C-32 governs *full gate triple purity*: all three gate annotation surfaces simultaneously carry no prose -- C-35 AND C-31 (v16) = C-36 AND C-30 (v17) = C-37 (v18) = C-38 AND C-29 (v19) = C-39 = C-40
- C-33 governs *no-restatement surface closure*: all three thin-reference surfaces simultaneously enforce rule quarantine -- C-19 AND C-20 AND C-31
- C-34 governs *full canonical discipline*: C-32 AND C-33 -- both layers simultaneously clean; the ceiling criterion
- C-35 governs *gate verdict surface*: C-29 AND C-30; the first pairwise bilateral of {C-29, C-30, C-31}
- C-36 governs *gate FAIL path surface*: C-29 AND C-31; the second pairwise bilateral; structurally independent of C-35 (confirmed E-03, R20)
- C-37 governs *gate annotation bilateral purity closure*: C-35 AND C-36; names the two-bilateral conjunction; equivalent to C-32, C-38 AND C-29, C-39, C-40
- C-38 governs *gate PASS-path bilateral*: C-30 AND C-31; the third and final pairwise bilateral completing the bilateral triangle; equivalent to C-37 under cascade constraint
- C-39 governs *gate annotation triple bilateral conjunction*: C-35 AND C-36 AND C-38; names the three-bilateral conjunction; equivalent to C-37, C-32, C-40
- C-40 governs *gate annotation direct atomic triple*: C-29 AND C-30 AND C-31 at the direct atomic level -- SERIES COMPLETION; equivalent to C-37, C-32, C-38, C-39

**C-25 decomposition:** C-27 and C-28 decompose the C-25 failure space into two independent sub-types: opener text (C-27) and fix-and-retry prose (C-28). Orthogonal within C-25's failure space.

**C-28 decomposition:** C-29 refines C-28's pass space. A C-28 pass means correction prose is not in the body -- it may or may not be in gate FAIL branches. C-29 resolves this: canonical location for correction prose is Phase 5 only.

**C-29 decomposition:** C-30 refines C-29's pass space along the verdict-branch axis. C-29 FAIL cascades unconditionally to C-30 FAIL (directional, confirmed R15).

**C-30 decomposition:** C-31 is independent of C-30. C-38 = C-30 AND C-31 names the PASS-path bilateral (v19): C-30 failure cascades to C-38, C-39, C-40. C-30 alone costs 8 deductions (v19): C-30 + C-35 + C-38 + C-37 + C-39 + C-40 + C-32 + C-34.

**C-31 decomposition:** C-32, C-33, C-36, C-37, C-38, C-39, and C-40 all depend on C-31 as a prerequisite. C-31 FAIL cascades to C-36 + C-38 + C-37 + C-39 + C-40 + C-32 + C-33 + C-34 = 9 deductions (v19, C-31 alone). C-31 is the highest-impact single pivot: shared prerequisite for both the C-32 and C-33 clusters and all three new criteria (C-38, C-39, C-40).

**C-32 decomposition (v16 + v17 + v18 + v19):** C-32 = C-35 AND C-31 (v16). C-32 = C-36 AND C-30 (v17). C-32 = C-37 (v18). C-32 = C-38 AND C-29 (v19). All four decompositions valid. C-39 and C-40 provide two further equivalent expressions at the triple-bilateral and direct-atomic levels.

**C-33 decomposition:** C-34 = C-32 AND C-33 is the ceiling. A C-33 pass means all three citation surfaces are thin -- gate annotation layer governed separately by C-32.

**C-35 decomposition (v16 + v19 update):** C-35 = C-29 AND C-30. BILATERAL TRIANGLE (v19): {C-35 = C-29 AND C-30, C-36 = C-29 AND C-31, C-38 = C-30 AND C-31} -- each bilateral shares exactly one atom with each other. C-37 names the conjunction of C-35 and C-36; C-39 names all three.

**C-36 decomposition (v17 + v18 + v19 update):** C-36 = C-29 AND C-31. C-36 PASS does not imply C-30 PASS -- reverse cascade does not exist (confirmed R15). C-36 and C-35 are structurally independent bilateral paths to C-37 failure (E-03, R20). C-38 = C-30 AND C-31 completes the bilateral triangle.

**C-37 decomposition (v18 + v19 update):** C-37 = C-35 AND C-36 = C-29 AND C-30 AND C-31 = C-32. New v19 form: C-37 = C-38 AND C-29. C-37 implies C-38. C-39 and C-40 are further equivalent expressions. All five closure expressions (C-32, C-37, C-38 AND C-29, C-39, C-40) contribute independent deduction points.

**C-38 decomposition (v19):** C-38 = C-30 AND C-31. Under cascade constraint, C-38 is equivalent to C-37 in practice. C-38 is implied by C-37 (C-37 = C-38 AND C-29 -> C-37 pass implies C-38 pass). C-38 FAIL cascades to C-39 and C-40. Fourth decomposition: C-32 = C-38 AND C-29.

**C-39 decomposition (v19):** C-39 = C-35 AND C-36 AND C-38 = C-32. Names all three pairwise bilaterals together. C-39 implies C-38. C-37 and C-39 each contribute one independent deduction point.

**C-40 decomposition (v19):** C-40 = C-29 AND C-30 AND C-31 = C-32. Direct atomic level. SERIES COMPLETION: naming hierarchy complete. Five independent closure-tier points: C-32, C-37, C-38, C-39, C-40. Each names C-32 at a distinct abstraction level: individual-surface (C-32), two-bilateral-conjunction (C-37), PASS-path bilateral + FAIL atom (C-38 AND C-29), triple-bilateral (C-39), direct atomic (C-40).

**No-restatement convergence:** C-19 (phase body), C-20 (checklist items), and C-31 (gate conditions) enforce the no-restatement rule across all three thin-reference surfaces. C-33 is the conjunction criterion.

**Cascade asymmetry summary (R15 through R20 confirmed):**
- Annotating FAIL branches (C-29 fail): C-29 + C-30 + C-35 + C-36 + C-38 + C-37 + C-39 + C-40 + C-32 + C-34 = 10 deductions (v19: +3 vs v18)
- Annotating PASS branches only (C-30 alone): C-30 + C-35 + C-38 + C-37 + C-39 + C-40 + C-32 + C-34 = 8 deductions (v19: +3 vs v18)
- Verbose gate conditions (C-31 alone): C-31 + C-36 + C-38 + C-37 + C-39 + C-40 + C-32 + C-33 + C-34 = 9 deductions (v19: +3 vs v18)
- Annotating PASS branches AND verbose conditions (C-30 + C-31): C-30 + C-31 + C-35 + C-36 + C-38 + C-37 + C-39 + C-40 + C-32 + C-33 + C-34 = 11 deductions (v19: +3 vs v18)
- Full canonical compliance (all 33 pass): all conjunction criteria simultaneously satisfied

**Deduction depth table (v19):**

| Single failure | Cascade targets | Total deductions |
|----------------|----------------|-----------------|
| C-29 only | C-30, C-35, C-36, C-38, C-37, C-39, C-40, C-32, C-34 | 10 |
| C-30 only | C-35, C-38, C-37, C-39, C-40, C-32, C-34 | 8 |
| C-31 only | C-36, C-38, C-37, C-39, C-40, C-32, C-33, C-34 | 9 |
| C-30 + C-31 combined | C-35, C-36, C-38, C-37, C-39, C-40, C-32, C-33, C-34 | 11 |

C-29 remains the single highest-cost failure mode (10 deductions). C-31 alone is second (9 deductions), maintaining its lead over C-30 alone (8 deductions) by the C-33 cascade. V-01 vs V-02 gap preserved at 1 point. Each new criterion adds exactly 3 deductions to every non-ceiling failure mode.

**C-29/C-31 structural distinction (v19 update):** C-29 alone: 10 deductions (was 7). C-31 alone: 9 deductions (was 6). C-30 alone: 8 deductions (was 5). The gap between C-29 and C-31 remains 1 point (C-33 cascade exclusive to C-31). Each of C-38, C-39, C-40 adds +1 to every non-ceiling failure count.

---

**R9 confirmation summary:**

- All 5 variations tied at 100 under v8. C-19 is register-neutral; C-15/C-18 are format-neutral; C-21 is order-neutral; phase compaction is safe. Denominator raised to 19.

**R11 confirmation summary:**

- C-25 failure decomposes into C-27 (opener) and C-28 (retry), orthogonal. C-24/C-25/C-26 cascade-independent. Denominator raised to 21.

**R12 confirmation summary:**

- C-29 breaks V-01/V-02 tie. C-27 and C-19 govern orthogonal properties. C-26 and C-28 are orthogonal failure axes. Denominator raised to 22.

**R13 confirmation summary:**

- C-29 universally discriminating across all 4 non-canonical variations. C-26/C-27 failures isolated independently. Denominator raised to 23.

**R14 confirmation summary:**

- C-30 universally discriminating. C-30 + C-29 independence confirmed. Denominator raised to 24.

**R15 confirmation summary:**

- C-31 isolation confirmed; no C-23 cascade. C-29->C-30 cascade confirmed hard and directional. Reverse cascade does not exist. Denominator raised to 26.

**R16 confirmation summary:**

- C-32/C-33 orthogonality confirmed. C-31 pivot point identified. C-34 is the ceiling. Denominator raised to 27.

**R17 confirmation summary:**

- C-35 verdict-surface conjunction (v16): C-35 = C-29 AND C-30. V-01/V-03 re-equalization confirmed. Denominator raised to 28.

**R18 confirmation summary:**

- C-36 FAIL-path conjunction (v17): C-36 = C-29 AND C-31. {C-30 AND C-31} bilateral collapses to C-32 under cascade -- named in v19 as C-38. C-36 and C-35 orthogonality confirmed. Dual decomposition of C-32 established. Denominator raised to 29.

**R19 confirmation summary:**

- C-37 bilateral purity closure (v18): no variation outside V-05 achieves both C-35 and C-36. C-37 = C-32 equivalence established. Third decomposition: C-32 = C-37. Denominator raised to 30.

**R20 confirmation summary:**

- C-38 PASS-path bilateral (new in v19): E-03 confirmed C-35/C-36 structural independence, revealing C-38 = C-30 AND C-31 as the third bilateral. Completes the bilateral triangle. Fourth decomposition: C-32 = C-38 AND C-29.
- C-39 triple bilateral conjunction (new in v19): E-01 confirmed triple-surface simultaneous purity requires all three surfaces clean at once. C-39 = C-35 AND C-36 AND C-38 names all three bilaterals explicitly.
- C-40 direct atomic triple, SERIES COMPLETION (new in v19): E-02 confirmed single-deduction structure. C-40 = C-29 AND C-30 AND C-31 closes the naming hierarchy at the direct atomic level.
- Adjacent variation pairing (E-03): V-01 (C-30 alone) and V-02 (C-31 alone) confirm each bilateral path fails C-37 and C-38 independently.
- All non-ceiling variations gain exactly 3 additional deductions. Rankings preserved: V-05 (33/33) > V-01 (25/33) > V-02 (24/33) > V-03 (22/33) > V-04 (21/33).
- Denominator raised to 33. V-05 targets 33/33 = 100.00 under v19.
