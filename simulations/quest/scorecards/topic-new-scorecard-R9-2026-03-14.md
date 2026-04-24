## Round 9 Scorecard — topic-new (v8 rubric)

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Golden? |
|------|-----------|-----------|-------------|--------------|-----------|---------|
| 1 | V-01 Lifecycle emphasis | 5/5 | 3/3 | 20/20 | **100** | YES |
| 1 | V-03 Phrasing register | 5/5 | 3/3 | 20/20 | **100** | YES |
| 1 | V-04 Lifecycle + Inertia | 5/5 | 3/3 | 20/20 | **100** | YES |
| 1 | V-05 Output + Role + Inertia | 5/5 | 3/3 | 20/20 | **100** | YES |
| 5 | V-02 Output format (list) | 5/5 | 3/3 | 18/20 | **99** | YES |

---

### The single discriminator: C-24 / C-26

V-02 uses a numbered PIPELINE INDEX list (`1. STAKEHOLDERS → exit: ...`) instead of a table with a dedicated Exit Gate column. C-24's pass condition requires "a pipeline overview or summary table that has an Exit Gate column." C-26 references "the pipeline overview table (C-24)." Both are PARTIAL. The functional intent — all gates visible before Step 1, read-before-execute directive present — is fully satisfied. The structural form is not.

**V-02 confirmation**: List-format schemas preserve mechanical coupling (C-23/C-27 PASS). The failure is form-not-function.

---

### Within-100 structural quality

| Criterion | Strongest carrier | Why |
|-----------|-------------------|-----|
| C-26 (read-before-execute) | **V-03** | Bold "STOP. READ THIS PIPELINE BEFORE YOU START." heading plus explicit "Do not start Phase 1 until you have read all eight rows." Two directive layers. |
| C-28 (column completeness) | **V-03** | "Check these two items **independently**" + "(1)... (2)..." + "Do not advance until both items are checked **separately**" — independence stated as a semantic instruction, not just inferred from two checkboxes. |
| C-14 (pervasive consequences) | **V-04** | Three-layer architecture: schema columns, "If skipped" per-row column in PIPELINE OVERVIEW, "Without this step" header at each phase. First variation with consequence framing at the architectural overview layer. |
| C-12 (priority vocab framing) | **V-05** | Names the specific substitution: "Teams default to 'high/medium/low'; commit gate cannot be evaluated mechanically." |

---

### Recommended Golden Candidate

**V-04** — strongest C-14 across all rounds; "If skipped" column in PIPELINE OVERVIEW is the R9 excellence signal that may become C-29. **V-03** is the robustness alternative if gate-skip resistance is the priority.

---

### Excellence Signals (R9)

**E-1 (V-04)**: Pipeline overview table with a per-row skip-cost column makes phase-level consequences visible at the architectural declaration layer — before Phase 1 execution begins. This is C-29 candidate territory: sharpens C-24 by requiring the overview to be consequence-informative, not just gate-declarative.

**E-2 (V-03)**: "Independently" stated as a label at the enforcement point closes the gap C-28 leaves open — two checkboxes can still be checked in sequence; "check these independently / do not advance until both checked separately" is a sequencing instruction that cannot be rationalized past.

**E-3 (V-05)**: "Status-Quo Default (if uncorrected)" is consequence-equivalent to Downstream Effect but frames harm as a behavioral prediction (what teams default to) rather than a technical failure. Combined with "## What This Supersedes," creates a named contrast point for the commit gate.

**E-4 (V-05)**: Priority-leading column order is an ergonomic intervention against C-04 failures — the hardest-to-catch violation appears at the leftmost position. Not testable by rubric scoring; requires live model runs to confirm.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Pipeline overview table carries a per-row consequence column (if-skipped / cost-of-skipping) alongside the Exit Gate column, making phase-level consequences visible at the architectural layer before Phase 1 begins -- extends C-24/C-26 by requiring the overview to be consequence-informative, not just gate-declarative", "Gate independence made explicit as a semantic instruction at the enforcement point itself -- not inferred from two separate checkboxes but stated as 'check these two items independently' and 'do not advance until both are checked separately' -- sharpens C-28 by requiring the independence label at the checkpoint", "Priority-leading signal table column order makes the hardest failure mode (C-04 priority vocabulary) the leftmost visible field -- an ergonomic intervention against priority-vocabulary substitution not captured by any current criterion"]}
```
Stakeholder fill-in minimum row count gate | PASS | Phase 1 exit: "[ ] >= 3 rows filled (S-01, S-02, S-03 minimum)" |
| C-23 | Schema constraints carry row-level IDs | PASS | F-01-F-05 and COV-01-COV-03 established as canonical IDs; all gate citations use these IDs, not prose |
| C-24 | Pipeline declares all exit gates in summary table | PASS | PIPELINE OVERVIEW table with Phase | Purpose | Produces | Exit Gate columns appears before any phase content |
| C-25 | Commit Gate in dedicated phase | PASS | Phase 8 explicitly: "This is a dedicated phase separate from signal plan production" |
| C-26 | Pipeline overview read-before-execute directive | PASS | "Read this entire table before executing Phase 1. All exit gate conditions are declared here. Do not begin Phase 1 until you have read every row." |
| C-27 | Schema row IDs at multiple gate boundaries | PASS | F-01-F-05 and COV-01-COV-03 cited at Phase 6 exit gate AND independently at Phase 7 exit gate |
| C-28 | Fill-in table exit gate enforces column completeness | PASS | Phase 1 exit: two distinct checkboxes -- "[ ] >= 3 rows filled" AND "[ ] All four columns populated in every filled row" |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 20/20

```
composite = (5/5 * 60) + (3/3 * 30) + (20/20 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 -- GOLDEN**

---

### V-02 -- Output Format (list-based schemas)

List-format PIPELINE INDEX instead of table; F-NN:/COV-NN: as inline prefix notation.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | TOPICS.md entry exists | PASS | Step 2 appends `| {topic} | active | simulations/{topic}/strategy.md |` to simulations/TOPICS.md |
| C-02 | Strategy file at correct path | PASS | All sections written to `simulations/{topic}/strategy.md` |
| C-03 | All five signal fields present | PASS | Step 7 columns: Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority |
| C-04 | Priority values valid | PASS | F-05: "Must be exactly -- essential / recommended / optional. No substitutions. Not 'high/medium/low'." |
| C-05 | At least one essential signal | PASS | COV-01 enforced at Step 6 and Step 7 |
| C-06 | Multi-namespace coverage | PASS | COV-02 enforced at both gate boundaries |
| C-07 | Narrative rationale | PASS | Step 3 requires ## Rationale with >= 2 sentences and explicit design decision |
| C-08 | Differentiated owner roles | PASS | COV-03 enforced at both gate boundaries |
| C-09 | Commit gate defined | PASS | Step 8: "Name every essential signal by item name. State the condition explicitly." |
| C-10 | Artifact naming convention | PASS | Step 5 ## Artifact Naming Convention; F-03 enforces pattern |
| C-11 | Checkbox-gate before phase transition | PASS | Every step (1-8) has exit checklist |
| C-12 | Invalid vocabulary as operational consequence | PASS | F-05 downstream: "Team commits without a defined stopping condition; coverage is unknown" |
| C-13 | Dedicated sections per aspirational criterion | PASS | Step 5 (Naming) and Step 8 (Commit Gate) are named steps |
| C-14 | Consequence framing pervasive | PASS | Every F-NN and COV-NN entry has "If wrong immediately" and "Downstream" sections |
| C-15 | Stakeholder-risk opener | PASS | Step 1 opens with "WHO BEARS THE RISK if this topic's strategy is wrong?" |
| C-16 | Every criterion enforced by structural mechanism | PASS | List-format constraints each have rule, immediate, downstream; gates cite by ID |
| C-17 | Stakeholder-risk section is active fill-in | PASS | Step 1 fill-in table with S-01..S-N rows |
| C-18 | Constraints in named schemas with consequence columns | PASS | FIELD RULES and COVERAGE RULES as named sections; both have two consequence tiers per rule |
| C-19 | FIELD SCHEMA includes Stakeholder traceability column | PASS | F-04 rule requires S-N citation; Step 7 table includes Stakeholder Ref column |
| C-20 | Consequence columns temporally layered | PASS | "If wrong immediately" and "Downstream" as two distinct labeled tiers per rule |
| C-21 | Per-phase exit gates at every boundary | PASS | Steps 1-8 each have their own exit checklist |
| C-22 | Stakeholder fill-in minimum row count gate | PASS | Step 1 exit: "[ ] >= 3 rows filled" |
| C-23 | Schema constraints carry row-level IDs | PASS | F-01-F-05 and COV-01-COV-03 established; gates cite by ID |
| C-24 | Pipeline declares all exit gates in summary table | PARTIAL | PIPELINE INDEX is a numbered list with inline "-> exit:" annotations, not a table with a dedicated Exit Gate column. All gate conditions are declared before phase content (intent satisfied) but the structural form -- "a pipeline overview or summary table that has an Exit Gate column" -- is not met. |
| C-25 | Commit Gate in dedicated phase | PASS | Step 8: "This is a dedicated step separate from signal plan production." |
| C-26 | Pipeline overview read-before-execute directive | PARTIAL | "Read this entire index before executing Step 1. All exit conditions are declared here." -- directive is present and clear, but C-26's pass condition references "the pipeline overview table (C-24)"; since C-24 is only partially met (list, not table), C-26's structural carrier is also only partially met. |
| C-27 | Schema row IDs at multiple gate boundaries | PASS | F-01-F-05 and COV-01-COV-03 cited at Step 6 exit AND Step 7 exit independently |
| C-28 | Fill-in table exit gate enforces column completeness | PASS | Step 1 exit: two distinct items -- "[ ] >= 3 rows filled" AND "[ ] All four columns populated in every filled row" |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 18/20 (C-24 PARTIAL, C-26 PARTIAL)

```
composite = (5/5 * 60) + (3/3 * 30) + (18/20 * 10)
          = 60 + 30 + 9
          = 99
```

**Score: 99 / 100 -- GOLDEN**

**Note**: The V-02 hypothesis -- that list-based schemas preserve mechanical coupling (C-23/C-27) -- is confirmed. F-NN/COV-NN IDs in list format work correctly at gate boundaries. The list PIPELINE INDEX does not satisfy the table-with-Exit-Gate-column form that C-24 requires. This is a structural form failure, not a functional one.

---

### V-03 -- Phrasing Register

Direct imperative voice throughout; "STOP." and "CHECK:" as gate markers.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | TOPICS.md entry exists | PASS | Phase 2 instructs appending exact row; Phase 2 gate checks all three values |
| C-02 | Strategy file at correct path | PASS | All sections written to `simulations/{topic}/strategy.md` |
| C-03 | All five signal fields present | PASS | Phase 7 columns: Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority |
| C-04 | Priority values valid | PASS | F-05: "Write exactly: essential OR recommended OR optional -- nothing else"; downstream: "team commits without knowing which signals must exist first" |
| C-05 | At least one essential signal | PASS | COV-01: "At least one signal is marked essential" enforced at Phase 6 and Phase 7 |
| C-06 | Multi-namespace coverage | PASS | COV-02 enforced at both boundaries |
| C-07 | Narrative rationale | PASS | Phase 3: "Tell the reader why this topic matters and which specific design decision cannot be made without these signals." |
| C-08 | Differentiated owner roles | PASS | COV-03 enforced at Phase 6 and Phase 7 |
| C-09 | Commit gate defined | PASS | Phase 8: "Name every essential signal by its item name. Write the condition so a team member can check it without re-reading the signal plan." |
| C-10 | Artifact naming convention | PASS | Phase 5 with pattern + real example requirement |
| C-11 | Checkbox-gate before phase transition | PASS | Every phase has "CHECK before Phase N" with checkboxes; "Do not advance until both items are checked separately" at Phase 1 |
| C-12 | Invalid vocabulary as operational consequence | PASS | F-05: "The strategy cannot be parsed as a commit gate" + "The team commits without knowing which signals must exist first" |
| C-13 | Dedicated sections per aspirational criterion | PASS | Phase 5 and Phase 8 are named phases with dedicated content |
| C-14 | Consequence framing pervasive | PASS | Every F-NN and COV-NN row has "If you get it wrong immediately" and "What that causes downstream" columns |
| C-15 | Stakeholder-risk opener | PASS | Phase 1: "Ask yourself: WHO GETS HURT if this topic's strategy is wrong?" |
| C-16 | Every criterion enforced by structural mechanism | PASS | All constraints enforced via table columns, "CHECK:" checkboxes, "STOP." markers |
| C-17 | Stakeholder-risk section is active fill-in | PASS | Phase 1 fill-in table with S-01..S-N; "These IDs will be the source of truth for every Owner Role you write in Phase 7" |
| C-18 | Constraints in named schemas with consequence columns | PASS | FIELD RULES and COVERAGE RULES as named sections; both have two-column consequence tiers |
| C-19 | FIELD SCHEMA includes Stakeholder traceability column | PASS | F-04: "Copy an S-N identifier from the Phase 1 table -- do not invent a role"; Phase 7 table has Stakeholder Ref column |
| C-20 | Consequence columns temporally layered | PASS | "If you get it wrong immediately" and "What that causes downstream" as two distinct columns in both schema tables |
| C-21 | Per-phase exit gates at every boundary | PASS | Phases 1-8 each have explicit "CHECK before Phase N"; "STOP when done. Check everything again before Phase 8" at Phase 7 |
| C-22 | Stakeholder fill-in minimum row count gate | PASS | Phase 1: "(1) >= 3 rows filled" as first of two enumerated independent items |
| C-23 | Schema constraints carry row-level IDs | PASS | F-01-F-05 and COV-01-COV-03; gate checkboxes cite by ID throughout |
| C-24 | Pipeline declares all exit gates in summary table | PASS | PIPELINE OVERVIEW table ("STOP. READ THIS PIPELINE BEFORE YOU START") with Phase | What you will do | What you will produce | What you must check columns; appears before Phase 1 |
| C-25 | Commit Gate in dedicated phase | PASS | Phase 8: "This phase is separate from signal production. Do not mix signal rows and commit gate text in the same section." |
| C-26 | Pipeline overview read-before-execute directive | PASS | "Read every row below before executing Phase 1. Every exit condition for every phase is declared in this table. Do not start Phase 1 until you have read all eight rows." Bold heading: "STOP. READ THIS PIPELINE BEFORE YOU START." Strongest C-26 implementation in R9. |
| C-27 | Schema row IDs at multiple gate boundaries | PASS | F-01-F-05 and COV-01-COV-03 cited at Phase 6 ("CHECK before Phase 7") AND Phase 7 ("STOP when done. Check everything again") independently |
| C-28 | Fill-in table exit gate enforces column completeness | PASS | "STOP. Check these two items independently before Phase 2: [ ] (1) >= 3 rows filled / [ ] (2) All four columns filled in every row you wrote / Do not advance until both items are checked separately." Independence made explicit at the checkpoint label level. Strongest C-28 implementation in R9. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 20/20

```
composite = (5/5 * 60) + (3/3 * 30) + (20/20 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 -- GOLDEN**

---

### V-04 -- Lifecycle Emphasis + Inertia Framing

Lifecycle with "If skipped" column in PIPELINE OVERVIEW and "Without this step" at every phase header.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | TOPICS.md entry exists | PASS | Phase 2 instructs append; Phase 2 gate checks all three fields |
| C-02 | Strategy file at correct path | PASS | All sections written to `simulations/{topic}/strategy.md` |
| C-03 | All five signal fields present | PASS | Phase 7 columns: Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority |
| C-04 | Priority values valid | PASS | F-05: "Must be exactly: essential / recommended / optional -- no other vocabulary" with downstream consequence |
| C-05 | At least one essential signal | PASS | COV-01 enforced at Phase 6 and Phase 7 |
| C-06 | Multi-namespace coverage | PASS | COV-02 enforced at both boundaries |
| C-07 | Narrative rationale | PASS | Phase 3 ## Rationale required with >= 2 sentences and named design decision |
| C-08 | Differentiated owner roles | PASS | COV-03 enforced at both boundaries |
| C-09 | Commit gate defined | PASS | Phase 8: "State the minimal set of signals required before design commit. Name each essential signal by item name, not by count." |
| C-10 | Artifact naming convention | PASS | Phase 5 with pattern and >= 1 real example |
| C-11 | Checkbox-gate before phase transition | PASS | Every phase (1-8) has its own "Phase N Exit Gate" with checkboxes |
| C-12 | Invalid vocabulary as operational consequence | PASS | F-05 downstream: "Team commits without knowing which signals must exist; evidence coverage unknown" |
| C-13 | Dedicated sections per aspirational criterion | PASS | Phase 5 and Phase 8 are named dedicated phases |
| C-14 | Consequence framing pervasive | PASS | FIELD SCHEMA and COVERAGE SCHEMA have Immediate Failure + Downstream Effect columns; PIPELINE OVERVIEW has "If skipped" column per phase row; every phase header has "Without this step" consequence statement. Three-layer consequence architecture. Strongest C-14 in R9. |
| C-15 | Stakeholder-risk opener | PASS | Phase 1: "WHO BEARS THE RISK if this topic's strategy is wrong?" |
| C-16 | Every criterion enforced by structural mechanism | PASS | All constraints enforced via schema columns, "If skipped" overview column, phase gate checkboxes |
| C-17 | Stakeholder-risk section is active fill-in | PASS | Phase 1 fill-in table with S-01..S-N |
| C-18 | Constraints in named schemas with consequence columns | PASS | FIELD SCHEMA and COVERAGE SCHEMA with Immediate Failure + Downstream Effect columns |
| C-19 | FIELD SCHEMA includes Stakeholder traceability column | PASS | F-04 Owner Role requires S-N citation; Phase 7 includes Stakeholder Ref column |
| C-20 | Consequence columns temporally layered | PASS | "Immediate Failure" and "Downstream Effect" as two distinct columns |
| C-21 | Per-phase exit gates at every boundary | PASS | Phases 1-8 each have "Phase N Exit Gate" with checkboxes |
| C-22 | Stakeholder fill-in minimum row count gate | PASS | Phase 1 exit: "[ ] >= 3 rows filled (row-count condition)" |
| C-23 | Schema constraints carry row-level IDs | PASS | F-01-F-05 and COV-01-COV-03 established; gate citations use IDs |
| C-24 | Pipeline declares all exit gates in summary table | PASS | PIPELINE OVERVIEW table with Phase | Purpose | If skipped | Exit Gate -- four-column table before Phase 1; "If skipped" column extends beyond minimum C-24 requirement |
| C-25 | Commit Gate in dedicated phase | PASS | Phase 8: "This is a dedicated phase separate from signal plan production." |
| C-26 | Pipeline overview read-before-execute directive | PASS | "Read the full overview before starting -- the cost of skipping a phase is visible at every row. Do not begin Phase 1 until you have read every entry." Inertia note woven into the directive itself. |
| C-27 | Schema row IDs at multiple gate boundaries | PASS | F-01-F-05 and COV-01-COV-03 cited at Phase 6 exit AND Phase 7 exit independently |
| C-28 | Fill-in table exit gate enforces column completeness | PASS | Phase 1 exit: "[ ] >= 3 rows filled (row-count condition)" AND "[ ] All four columns populated in every filled row (column-completeness condition)" -- labeled as distinct named conditions. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 20/20

```
composite = (5/5 * 60) + (3/3 * 30) + (20/20 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 -- GOLDEN**

---

### V-05 -- Output Format + Role Sequence + Inertia Framing

Priority-leading signal table; technical-first role sequence; "What This Supersedes" section.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | TOPICS.md entry exists | PASS | Phase 2 appends row; Phase 2 gate checks topic, status=active, path |
| C-02 | Strategy file at correct path | PASS | All sections written to `simulations/{topic}/strategy.md` |
| C-03 | All five signal fields present | PASS | Phase 7 columns: Priority | Namespace | Skill | Item Name | Stakeholder Ref | Owner Role -- all five fields present, order changed |
| C-04 | Priority values valid | PASS | F-05: "Must be exactly: essential / recommended / optional -- no substitutions"; downstream: "Teams default to 'high/medium/low'; commit gate cannot be evaluated mechanically" -- names the specific substitute vocabulary |
| C-05 | At least one essential signal | PASS | COV-01 enforced at Phase 6 and Phase 7 |
| C-06 | Multi-namespace coverage | PASS | COV-02 enforced at both boundaries |
| C-07 | Narrative rationale | PASS | Phase 3 ## Rationale with >= 2 sentences and named design decision |
| C-08 | Differentiated owner roles | PASS | COV-03 enforced at both boundaries; Phase 1 requires technical, decision, and user-facing perspectives |
| C-09 | Commit gate defined | PASS | Phase 8: "State the minimal signal set required before design commit -- as a contrast to the status-quo default named in Phase 3." |
| C-10 | Artifact naming convention | PASS | Phase 5 with pattern and real example |
| C-11 | Checkbox-gate before phase transition | PASS | Every phase (1-8) has "Phase N Exit Gate" checkboxes |
| C-12 | Invalid vocabulary as operational consequence | PASS | F-05 downstream: "Teams default to 'high/medium/low'; commit gate cannot be evaluated mechanically" -- strongest F-05 framing in R9 by naming the default substitution explicitly |
| C-13 | Dedicated sections per aspirational criterion | PASS | Phase 5 and Phase 8 are named dedicated phases |
| C-14 | Consequence framing pervasive | PASS | FIELD SCHEMA "Status-Quo Default (if uncorrected)" column; COVERAGE SCHEMA "Status-Quo Default" column; Phase 3 ## What This Supersedes section adds inertia framing |
| C-15 | Stakeholder-risk opener | PASS | Phase 1: "WHO BEARS THE RISK if this topic's strategy is wrong?" with technical-first prompt |
| C-16 | Every criterion enforced by structural mechanism | PASS | All constraints enforced via schema columns, gate checkboxes, phase section headers, template fields |
| C-17 | Stakeholder-risk section is active fill-in | PASS | Phase 1 fill-in table: S-01=[technical owner], S-02=[PM], S-03=[user-facing role] as prompted structure |
| C-18 | Constraints in named schemas with consequence columns | PASS | FIELD SCHEMA and COVERAGE SCHEMA with Immediate Failure + Status-Quo Default columns |
| C-19 | FIELD SCHEMA includes Stakeholder traceability column | PASS | F-04 Owner Role requires S-N citation; Phase 7 includes Stakeholder Ref column separate from Owner Role |
| C-20 | Consequence columns temporally layered | PASS | "Immediate Failure" and "Status-Quo Default (if uncorrected)" as two distinct temporal tiers -- relabeled but structurally equivalent to Downstream Effect |
| C-21 | Per-phase exit gates at every boundary | PASS | Phases 1-8 each have "Phase N Exit Gate" checkboxes |
| C-22 | Stakeholder fill-in minimum row count gate | PASS | Phase 1 exit: "[ ] >= 3 rows filled" |
| C-23 | Schema constraints carry row-level IDs | PASS | F-01-F-05 and COV-01-COV-03; gate citations use IDs |
| C-24 | Pipeline declares all exit gates in summary table | PASS | PIPELINE OVERVIEW table with Phase | Produces | Exit Gate columns before Phase 1 |
| C-25 | Commit Gate in dedicated phase | PASS | Phase 8: "This is a dedicated phase separate from signal plan production." |
| C-26 | Pipeline overview read-before-execute directive | PASS | "Read this entire table before executing Phase 1. All exit gate conditions are declared here. Do not begin Phase 1 until you have read every row." |
| C-27 | Schema row IDs at multiple gate boundaries | PASS | F-01-F-05 and COV-01-COV-03 cited at Phase 6 exit AND Phase 7 exit independently |
| C-28 | Fill-in table exit gate enforces column completeness | PASS | Phase 1 exit: "[ ] >= 3 rows filled" AND "[ ] All four columns populated in every filled row" as two distinct checkboxes |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 20/20

```
composite = (5/5 * 60) + (3/3 * 30) + (20/20 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 -- GOLDEN**

---

## Summary Table

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Golden? | C-24 | C-26 |
|------|-----------|-----------|-------------|--------------|-----------|---------|------|------|
| 1 | V-01 Lifecycle emphasis      | 5/5 | 3/3 | 20/20 | **100** | YES | PASS | PASS |
| 1 | V-03 Phrasing register       | 5/5 | 3/3 | 20/20 | **100** | YES | PASS | PASS |
| 1 | V-04 Lifecycle + Inertia     | 5/5 | 3/3 | 20/20 | **100** | YES | PASS | PASS |
| 1 | V-05 Output + Role + Inertia | 5/5 | 3/3 | 20/20 | **100** | YES | PASS | PASS |
| 5 | V-02 Output format (list)    | 5/5 | 3/3 | 18/20 | **99**  | YES | PARTIAL | PARTIAL |

**C-24 (table form) and C-26 (directive on the table) are the only discriminators.** All other 26 criteria pass across all variations.

---

## C-24/C-26 Failure Analysis -- V-02

| Criterion | V-02 design | What passes | What fails |
|-----------|-------------|-------------|------------|
| C-24 | Numbered list with "-> exit:" inline | All gate conditions declared before Step 1; architecturally visible | No table; no dedicated Exit Gate column; functional equivalent but wrong structural form |
| C-26 | "Read this entire index before executing Step 1" directive on list header | Read-before-execute intent satisfied | C-26 pass condition references "the pipeline overview table (C-24)"; table not present, so C-26 carries the same partial |

**V-02 finding**: The hypothesis -- "list format preserves mechanical coupling" -- is confirmed for C-23 and C-27 (F-NN/COV-NN IDs cited correctly at both boundaries in list form). The hypothesis fails at C-24 because C-24's structural requirement is explicitly a table with an Exit Gate column. A numbered list with inline annotations is not that. This is a form-not-function failure.

---

## Within-100 Structural Quality Comparison

All four top-scoring variations satisfy every criterion, but implementation strength differs:

| Criterion | Strongest carrier | Why |
|-----------|-------------------|-----|
| C-26 (read-before-execute) | V-03 | "STOP. READ THIS PIPELINE BEFORE YOU START." as a bold section header, then: "Read every row before executing Phase 1. Do not start until you have read all eight rows." Two layers of directive. |
| C-28 (column completeness independent of row count) | V-03 | "STOP. Check these two items independently before Phase 2" with "(1)" and "(2)" enumeration AND "Do not advance until both items are checked separately" -- independence made explicit at the language level, not just structural separation. |
| C-14 (pervasive consequence framing) | V-04 | Three-layer architecture: schema columns (Immediate Failure + Downstream Effect), PIPELINE OVERVIEW "If skipped" per-row column, "Without this step" header at each phase. Only variation with consequence framing at the architectural overview layer. |
| C-12 (priority vocabulary consequence framing) | V-05 | "Teams default to 'high/medium/low'; commit gate cannot be evaluated mechanically" -- names the specific substitute vocabulary and its mechanical failure mode. |

---

## Excellence Signals -- Round 9

### E-1: Consequence framing at the pipeline overview level (V-04)

V-04's PIPELINE OVERVIEW adds an "If skipped" column -- a per-phase consequence column at the architectural declaration layer. Prior rounds placed consequence framing in schema rows (C-14/C-18) and at phase headers; V-04 is the first variation to embed consequences into the summary table itself, so a reader who only reads the overview sees both gate conditions AND what breaks if they skip each phase before any phase content is encountered.

C-14 currently requires consequence framing in schema rows. A sharpening criterion would require consequence framing at the architectural overview level -- each phase row in the pipeline overview also carries its skip-cost, visible before execution begins. This would be the C-24/C-26 analog for consequence visibility: just as C-26 requires a read-before-execute directive on the overview, the new criterion would require a skip-cost column on the overview.

### E-2: Independence made explicit as language, not just structure (V-03)

V-03's Phase 1 exit uses: "STOP. Check these two items **independently** before Phase 2" + "(1)... (2)..." + "Do not advance until both items are checked **separately**." The word "independently" at the checkpoint label level makes the check independence a semantic instruction, not an inferred property of two bullet points. C-28 currently requires two separately listed conditions; this excellence signal goes further by making the separation a named constraint at the enforcement point itself. A sharpening criterion would require the independence label explicitly at the exit gate, not just structural separation of conditions.

### E-3: Relabeling Downstream Effect as "Status-Quo Default" is consequence-equivalent (V-05)

V-05 uses "Status-Quo Default (if uncorrected)" instead of "Downstream Effect." This framing shift -- from what-breaks to what-teams-default-to -- passes C-20 (temporal layering) because the second tier still describes what happens if the rule is not followed. Combined with "## What This Supersedes" in Phase 3, V-05 makes the contrast between the strategy being built and the assumption being replaced explicit and structurally enforced. The status-quo framing is consequence-equivalent to downstream-effect framing but may produce richer model output by naming the behavioral default rather than just the failure mode.

### E-4: Priority-leading column order makes the hardest failure mode front-left (V-05)

Placing Priority as the first column in the signal plan table means a scanning model sees the C-04/C-05 failure point before reading Namespace, Skill, or any other field. This is an ergonomic intervention against the most common failure mode (C-04 is flagged as "the hardest failure mode to catch" in the rubric). No prior round tested column-order effects on priority-vocabulary compliance. If live model runs confirm lower C-04 failure rates in V-05, priority-leading column order would be a new structural criterion.

---

## Recommended Golden Candidate

**V-04** is the recommended golden candidate for Round 9:
- Achieves 100/100 with the strongest C-14 implementation in any round to date
- "If skipped" column in PIPELINE OVERVIEW extends consequence framing to the architectural layer (E-1 -- candidate for C-29)
- "Without this step" at every phase header creates a three-layer consequence architecture not present in any prior variation
- C-26 directive woven with inertia framing: "the cost of skipping a phase is visible at every row" -- the read-before-execute instruction references its own structural evidence

**V-03** is the strongest alternative for gate-compliance robustness: "STOP." markers and "independently" language (E-2) make gate rationalization harder at the enforcement point itself. If the priority concern is gate-skip resistance rather than upfront consequence visibility, V-03 is the better choice.

**V-05** is the candidate to watch for C-04 failure rate improvement: priority-leading column order (E-4) and "Status-Quo Default" relabeling (E-3) are not testable by rubric scoring alone and require live model runs to assess.

---

## C-29 Candidate (from R9 excellence signals)

**E-1 suggests**: *Pipeline overview table carries a per-row consequence column (cost-of-skipping) alongside the Exit Gate column, making phase-level consequences visible at the architectural declaration layer before Phase 1 begins.*

Candidate criterion text: "Pipeline overview table includes a consequence column (skip-cost or 'if skipped') alongside the Exit Gate column -- so each phase row in the overview declares both the gate condition and the cost of not meeting it, making per-phase consequences architecturally visible before Phase 1 execution begins."

This sharpens C-24 (overview table) and C-26 (read-before-execute) by requiring the overview to be consequence-informative at the row level, not just gate-declarative. A model reading only the overview before execution sees both "what I must check" AND "what breaks if I skip this phase" for every phase, closing the gap between gate compliance and phase motivation.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Pipeline overview table carries a per-row consequence column (if-skipped / cost-of-skipping) alongside the Exit Gate column, making phase-level consequences visible at the architectural layer before Phase 1 begins -- extends C-24/C-26 by requiring the overview to be consequence-informative, not just gate-declarative", "Gate independence made explicit as a semantic instruction at the enforcement point itself -- not inferred from two separate checkboxes but stated as 'check these two items independently' and 'do not advance until both are checked separately' -- sharpens C-28 by requiring the independence label at the checkpoint", "Priority-leading signal table column order makes the hardest failure mode (C-04 priority vocabulary) the leftmost visible field -- an ergonomic intervention against priority-vocabulary substitution not captured by any current criterion"]}
```
