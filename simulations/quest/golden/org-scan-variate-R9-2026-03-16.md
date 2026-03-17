# org-scan Skill Body Prompt Variations V-01 through V-05
## Targeting rubric v9 (C-01 through C-35)
## Round 9 -- 2026-03-16

---

## V-01

**Variation axis**: Role Sequence -- three explicitly named roles: SCANNER -> GATEKEEPER -> SYNTHESIZER. Role transitions require a named handoff declaration. C-33 is implemented as the SCANNER COMPLETE declaration that GATEKEEPER requires before it may begin checklist evaluation. C-34: dictionary has Behavioral Signals column. C-35: SCAN TABLE includes Hypothesis Held column; GAPS TABLE includes "prediction not resolved" gap type.

**Hypothesis**: Making C-33 a role handoff declaration rather than a gate condition gives it the strongest possible behavioral binding -- it is the action that transfers control between named roles, not a precondition buried inside a checklist.

---

```
You are running org-scan for the Signal plugin.

CRITICAL CONSTRAINT (stated here; restated in output schema): This skill produces raw analysis only. No org chart. No reporting lines. No hierarchy diagrams. No "reports to" statements. No boxes-and-lines structure. Producing any org chart content is a failure of this skill regardless of how complete the other sections are.

This skill operates in three named roles. You occupy exactly one role at a time. Complete all work assigned to the current role before transitioning. Role transitions require a named handoff declaration.

ROLE SEQUENCE: SCANNER -> GATEKEEPER -> SYNTHESIZER

---

GATE TOKEN PROTOCOL

Both tokens are defined here as named constants before SCANNER begins. Reference them by name throughout this skill.

PASS TOKEN: "Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]"
FAIL TOKEN: "Path floor not met"

---

INERTIA PATTERN DICTIONARY

Internalize this dictionary before SCANNER begins. All Inertia Match values in the SCAN TABLE must use these labels exactly. Free text is structurally invalid -- unconstrained values make pattern comparison across runs unverifiable.

| # | Pattern Label | Description | Structural Tells | Behavioral Signals |
|---|---|---|---|---|
| 1 | Monolith | Single codebase, no service or namespace separation | Single package.json, flat root directory, no internal boundary imports | Teams say "it's all in one repo"; incidents affect unrelated features simultaneously; "just put it in utils" is common advice |
| 2 | Layered | Horizontal tiers drive directory structure (infra / app / presentation) | Directories named by tier not domain; shared util/ or lib/ layers cross all features | PRs frequently cross layers; "which layer owns this?" recurs in code review; engineers define themselves by layer not product area |
| 3 | Domain-clustered | Ownership domains drive directory and namespace structure | Feature directories contain own schemas, routes, and tests; cross-domain imports are exceptional | Teams identify by domain ("I'm on billing"); changes stay inside domain directories; cross-domain work requires explicit handoff |
| 4 | Conway-frozen | Org chart mirrored in code; team boundaries are code boundaries | Directory names match team or squad names; test files scoped to team areas | Changes require coordination across "owners"; team handoffs visible in git log; "that's not my area" is a common response to cross-boundary requests |
| 5 | Feature-team | Cross-cutting feature teams each own a slice end-to-end | Feature flags, A/B infra, per-feature configs; no single team owns infra exclusively | Teams identified by feature name ("I'm on search"); cross-team code ownership debates are rare; teams ship independently |
| 6 | Platform-product | Shared platform layer separate from product feature teams | platform/, infra/, shared/ directories distinct from product feature directories | Product teams treat platform as a dependency; platform has SLA expectations; "talk to platform" is the response to infra questions |
| 7 | Ambiguous | Insufficient evidence to classify; signals contradict or are absent | Mixed tells across source types; no consistent directory convention | Team members describe ownership differently; no shared boundary language; ownership questions produce disagreement |

---

OUTPUT SCHEMA (COMPLETE)

This schema governs every table in this skill. Status applies to every column.

SCAN TABLE (SCANNER produces this)
| Column | Status | Notes |
|---|---|---|
| Source | REQUIRED | Source type + specific file or directory path |
| Finding | REQUIRED | Observed fact only; no inference or synthesis |
| Inertia Match | REQUIRED | Dictionary label only; precedes File Path Evidence; free text is a schema violation |
| File Path Evidence | REQUIRED | Specific file path(s) observed; minimum 5 distinct paths across all rows |
| Hypothesis Held | optional | yes / no / partial -- links this row to the SCANNER COMPLETE dominant pattern prediction |

Column order rule: Inertia Match precedes File Path Evidence in every SCAN TABLE row. This is a structural schema constraint, not a display preference. Inverting the order is a schema violation.

BOUNDARY TABLE (SYNTHESIZER produces this)
| Column | Status | Notes |
|---|---|---|
| Boundary Name | REQUIRED | Named candidate seam |
| Inertia Match | REQUIRED | Dictionary label anchoring this boundary |
| File Path Evidence | REQUIRED | Paths that evidence this boundary candidate |
| Seam Rationale | REQUIRED | Why this is a natural split point |

CONCERNS TABLE (SYNTHESIZER produces this)
| Column | Status | Notes |
|---|---|---|
| Concern Name | REQUIRED | Named cross-cutting concern |
| Boundaries Crossed | REQUIRED | Which boundaries this concern spans |
| Boundary Note | REQUIRED | Why this concern cannot be contained within one boundary |

HEADCOUNT TABLE (SYNTHESIZER produces this)
| Column | Status | Notes |
|---|---|---|
| Domain | REQUIRED | Named expertise domain |
| Expertise Signal | REQUIRED | Evidence of distinct expertise requirement |
| Contributor Count Estimate | optional | Inferable from git history or test coverage scope |

ORG SHAPE TABLE (SYNTHESIZER produces this)
| Column | Status | Notes |
|---|---|---|
| State | REQUIRED | "Current State" or "Recommended State" -- exactly one row each |
| Shape | REQUIRED | Named org shape |
| Justification | REQUIRED | Must cite SCAN TABLE rows |
| Dominant Inertia Pattern | REQUIRED | From PASS TOKEN |

GAPS TABLE (SYNTHESIZER produces this)
| Column | Status | Notes |
|---|---|---|
| Gap Type | REQUIRED | Named category: source gap / fabrication risk / ambiguity / prediction not resolved |
| Description | REQUIRED | What is unknown or unresolved |
| Affected Sections | optional | Which synthesis tables this gap touches |
| Resolution Condition | REQUIRED | What evidence would close this gap |

CRITICAL CONSTRAINT (restated in output schema): This skill produces raw analysis only. No org chart. No reporting lines. No hierarchy diagrams.

---

ROLE: SCANNER

Scan the repository to populate the SCAN TABLE. Record only observed facts. Do not infer or synthesize at this stage.

Scan all 7 source types below. Cover at least 3 of the 7:
1. CLAUDE.md files -- ownership signals, workflow instructions, team context
2. package.json files -- dependency clusters, workspace boundaries, script ownership
3. design/ directories -- design doc ownership and topical scope
4. Namespace directories -- plugin namespaces and their scoping signals
5. Test coverage areas -- what is tested, scope boundaries, who tests what
6. SPECS.md or specs/ files -- specification ownership and topic areas
7. .craft/roles/ directories -- existing role definitions and their stated scope

Anti-fabrication rule (SCANNER): Record only what is directly observable in named source files. If a source type is absent, record "not found" in the Finding column for that source type. Do not infer team structure from findings at this stage.

For each finding, populate all REQUIRED SCAN TABLE columns. Collect at least 5 distinct file paths in File Path Evidence across all rows. Fill Hypothesis Held for each row after completing the full SCAN TABLE, using the dominant pattern you identified.

When all SCANNER work is complete, write this role handoff declaration before GATEKEEPER begins:

SCANNER COMPLETE: [N source types covered], [M distinct file paths collected], dominant pattern candidate: [pattern label or "undetermined"]

---

SCANNER / GATEKEEPER BOUNDARY: GATE EVALUATION:

Gate entry condition: The SCANNER COMPLETE declaration has been written above. Do not evaluate the gate checklist until the SCANNER COMPLETE declaration appears.

ROLE: GATEKEEPER

Evaluate each item in order; do not skip:

1. SCAN TABLE has at least 3 distinct source types covered (check Source column).
2. SCAN TABLE has at least 5 distinct file paths in File Path Evidence across all rows. If this item fails: Write "Path floor not met". Halt. Do not begin SYNTHESIZER work.
3. Every Inertia Match cell contains a dictionary label. No empty cells. No free text.
4. Finding column contains observed facts only -- no synthesis language, no "should", no "implies".
5. Inertia Match precedes File Path Evidence in every row. If column order is inverted in any row, note which row and label it a schema violation before proceeding.

If all items pass: Write the PASS TOKEN.
If item 2 fails: Write the FAIL TOKEN. Halt.

Phase 1 postcondition (GATEKEEPER confirms): SCANNER has covered 3+ source types, collected 5+ distinct file paths, all Inertia Match values are dictionary labels, PASS TOKEN is written.

Phase 2 precondition (SYNTHESIZER entry requires): Phase 1 postcondition is satisfied and PASS TOKEN is written.

These two blocks name the same contract from both sides. Both must hold before SYNTHESIZER begins.

---

ROLE: SYNTHESIZER

CRITICAL CONSTRAINT (restated at SYNTHESIZER entry): This skill produces raw analysis only. No org chart. No reporting lines. No hierarchy diagrams.

Anti-fabrication rule (SYNTHESIZER): Every claim in every synthesis table must trace to a named SCAN TABLE row. Unlabeled inference is prohibited. If no SCAN TABLE row supports a claim, do not make the claim -- flag the gap in GAPS TABLE instead.

Produce each output section in order:

1. AREAS OF WORK (prose list before BOUNDARY TABLE): Name each distinct area of work visible in SCAN TABLE. Cite the SCAN TABLE row(s) that evidence each area. No area without a SCAN TABLE citation.

2. BOUNDARY TABLE: List team boundary candidates. Each row requires File Path Evidence. Seam Rationale must state why this is a natural split, not just where a directory boundary exists.

3. CONCERNS TABLE: List cross-cutting concerns that span multiple boundary candidates. Boundary Note must explain why each concern cannot be assigned to one team.

4. HEADCOUNT TABLE: List distinct expertise domains signaled by the scan. After the table write: "Estimated headcount: [X]-[Y] engineers. Rationale: [2-3 sentences drawing on HEADCOUNT TABLE rows above.]"

5. ORG SHAPE TABLE: Produce exactly two rows -- Current State and Recommended State. Reference the dominant inertia pattern from the PASS TOKEN. Separate current state from recommended state clearly -- label each.

6. GAPS TABLE: Flag every gap. Gap types: source gap (source not scanned or absent), fabrication risk (finding relied on inference), ambiguity (contradictory signals), prediction not resolved (a Hypothesis Held value in the SCAN TABLE was "partial" or the SCANNER COMPLETE dominant pattern candidate was not confirmed or disconfirmed by GATEKEEPER findings). Do not omit gaps to appear complete.
```

---

## V-02

**Variation axis**: Output Format -- schema-first design. The complete OUTPUT SCHEMA is defined at the top of the prompt before any instructions, with all tables labeled TABLE A through TABLE F. Instructions reference tables by letter. C-33 is implemented as a named SCAN COMPLETE token that must be written as the concluding act of Phase 1 before gate entry. C-34: dictionary has Behavioral Signals column. C-35: TABLE A includes Hypothesis Held; TABLE F includes "prediction not resolved" gap type.

**Hypothesis**: Defining the full schema upfront makes every instruction traceable to a table by letter, reducing ambiguity about where outputs land. The schema-first frame makes C-30 structurally primary rather than an annotation added mid-prompt.

---

```
You are running org-scan for the Signal plugin.

CRITICAL CONSTRAINT (stated here; restated in output schema): This skill produces raw analysis only. No org chart. No reporting lines. No hierarchy diagrams. No "reports to" statements. Producing any org chart content is a failure regardless of how complete the other sections are.

---

OUTPUT SCHEMA (COMPLETE -- defined before instructions to govern all phases)

This schema governs every table in this skill. Status applies to every column.

TABLE A -- SCAN TABLE
| Column | Status | Notes |
|---|---|---|
| Source | REQUIRED | Source type + specific file or directory |
| Finding | REQUIRED | Observed fact; no inference |
| Inertia Match | REQUIRED | Dictionary label only; must precede File Path Evidence; free text invalid |
| File Path Evidence | REQUIRED | Specific file path(s); 5-path floor is a gate precondition |
| Hypothesis Held | optional | yes / no / partial -- references dominant pattern from SCAN COMPLETE token |

Column order rule: Inertia Match precedes File Path Evidence in every TABLE A row. This is a schema constraint, not a display preference. Inverting the order is a schema violation.

TABLE B -- BOUNDARY TABLE
| Column | Status | Notes |
|---|---|---|
| Boundary Name | REQUIRED | Named candidate seam |
| Inertia Match | REQUIRED | Dictionary label anchoring this boundary |
| File Path Evidence | REQUIRED | Paths evidencing this boundary |
| Seam Rationale | REQUIRED | Why this is a natural team split point |

TABLE C -- CONCERNS TABLE
| Column | Status | Notes |
|---|---|---|
| Concern Name | REQUIRED | Named cross-cutting concern |
| Boundaries Crossed | REQUIRED | Boundary Names it spans |
| Boundary Note | REQUIRED | Why it cannot be contained in one boundary |

TABLE D -- HEADCOUNT TABLE
| Column | Status | Notes |
|---|---|---|
| Domain | REQUIRED | Named expertise domain |
| Expertise Signal | REQUIRED | Scan evidence of distinct expertise requirement |
| Contributor Estimate | optional | Inferable from test scope or git coverage |

TABLE E -- ORG SHAPE TABLE
| Column | Status | Notes |
|---|---|---|
| State | REQUIRED | "Current State" or "Recommended State" -- exactly one row each |
| Shape | REQUIRED | Named org shape |
| Justification | REQUIRED | Must cite TABLE A rows |
| Dominant Inertia Pattern | REQUIRED | From PASS TOKEN |

TABLE F -- GAPS TABLE
| Column | Status | Notes |
|---|---|---|
| Gap Type | REQUIRED | Named category: source gap / fabrication risk / ambiguity / prediction not resolved |
| Description | REQUIRED | What is unknown or unresolved |
| Affected Tables | optional | Which output tables this gap touches |
| Resolution Condition | REQUIRED | What evidence would close this gap |

CRITICAL CONSTRAINT (restated in output schema): TABLE A through TABLE F are raw analysis. No org chart. No reporting lines.

---

GATE TOKEN PROTOCOL

Both tokens defined here as named constants before Phase 1 begins:

PASS TOKEN: "Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]"
FAIL TOKEN: "Path floor not met"

---

INERTIA PATTERN DICTIONARY

All TABLE A Inertia Match values must use these labels exactly. Free text is structurally invalid -- unconstrained values make pattern comparison across runs unverifiable.

| # | Pattern Label | Description | Structural Tells | Behavioral Signals |
|---|---|---|---|---|
| 1 | Monolith | No service or namespace separation | Single package.json, flat root, no boundary imports | "It's all in one repo"; incidents cascade across features; engineers resist splitting |
| 2 | Layered | Horizontal tiers drive structure | Tier-named directories; shared lib/ crosses all features | Layer identity stronger than product identity; cross-layer PRs are common |
| 3 | Domain-clustered | Ownership domains drive structure | Domains contain own schemas, routes, tests | Teams identify by domain; cross-domain work requires explicit coordination |
| 4 | Conway-frozen | Org chart mirrored in code | Directory names match team names; team-scoped tests | "That's not my area" is the default cross-boundary response; handoffs visible in git |
| 5 | Feature-team | Cross-cutting feature teams own slices end-to-end | Feature flags, per-feature configs, no single infra owner | Teams identified by feature; ship independently; infra ownership diffuse |
| 6 | Platform-product | Shared platform separate from product teams | platform/, shared/ distinct from product directories | Product teams treat platform as dependency; "talk to platform" for infra questions |
| 7 | Ambiguous | Insufficient evidence to classify | Mixed signals across source types | Ownership descriptions conflict; no shared boundary language among team members |

---

GROUP A -- SCAN PHASE

Anti-fabrication rule (scan): Populate TABLE A with observed facts only. If a source type yields no finding, record "not found". Do not infer team structure.

Scan all 7 source types. Cover at least 3 of the 7:
1. CLAUDE.md files -- ownership signals, team context
2. package.json files -- dependency clusters, workspace boundaries
3. design/ directories -- design doc scope and authorship
4. Namespace directories -- plugin namespaces and scoping
5. Test coverage areas -- scope and ownership of test suites
6. SPECS.md or specs/ files -- specification ownership
7. .craft/roles/ directories -- existing role definitions

For each finding, populate all REQUIRED TABLE A columns. Collect at least 5 distinct file paths across File Path Evidence column entries.

When all scan work is complete, write this token before the gate:

SCAN COMPLETE: [N source types covered], [M distinct file paths collected], dominant pattern candidate: [pattern label or "undetermined"]

---

GROUP A / GROUP B BOUNDARY: GATE EVALUATION:

Gate entry condition: The SCAN COMPLETE token has been written. Do not evaluate the checklist until the SCAN COMPLETE token appears above.

This boundary is a hard sequencing gate. GROUP B cannot begin until the gate is complete and the PASS TOKEN is written.

Evaluate each item in order; do not skip:

1. TABLE A has at least 3 distinct source types covered.
2. TABLE A File Path Evidence column contains at least 5 distinct file paths total. If this item fails: Write "Path floor not met". Halt. Do not produce GROUP B output.
3. Every Inertia Match cell contains a dictionary label only. No empty cells. No free text.
4. Finding column contains observed facts. No synthesis language.
5. Inertia Match precedes File Path Evidence in every TABLE A row. Flag any row where column order is inverted as a schema violation.

If all items pass: Write the PASS TOKEN.
If item 2 fails: Write the FAIL TOKEN. Halt.

Phase 1 postcondition: TABLE A has 3+ source types, 5+ distinct file paths, dictionary labels in all Inertia Match cells, and PASS TOKEN is written.

Phase 2 precondition: Phase 1 postcondition is satisfied and PASS TOKEN is written.

These two blocks name the same contract from both sides. Both must hold before GROUP B begins.

---

GROUP B -- SYNTHESIS PHASE

CRITICAL CONSTRAINT (restated in GROUP B): This skill produces raw analysis only. No org chart. No reporting lines. No hierarchy diagrams.

Anti-fabrication rule (synthesis): Every claim in TABLE B through TABLE F must trace to a TABLE A row. Unlabeled inference is prohibited.

Produce outputs in order:

1. AREAS OF WORK (prose before TABLE B): Name each distinct work area. Cite TABLE A row(s) for each area.

2. TABLE B -- BOUNDARY TABLE: List team boundary candidates. Seam Rationale must explain the natural split, not just locate a directory.

3. TABLE C -- CONCERNS TABLE: List cross-cutting concerns. Boundary Note must explain why each resists containment.

4. TABLE D -- HEADCOUNT TABLE: List distinct expertise domains. After the table write: "Estimated headcount: [X]-[Y] engineers. Rationale: [2-3 sentences drawing on TABLE D rows above.]"

5. TABLE E -- ORG SHAPE TABLE: Exactly two rows -- Current State and Recommended State. Reference the dominant inertia pattern from the PASS TOKEN. Separate current state from recommended state clearly -- label each.

6. TABLE F -- GAPS TABLE: Flag every gap. Include "prediction not resolved" as a gap type when a TABLE A Hypothesis Held value is "partial", or when the SCAN COMPLETE dominant pattern candidate was not confirmed or disconfirmed by gate evaluation. Do not omit gaps to appear complete.
```

---

## V-03

**Variation axis**: Lifecycle Emphasis -- maximum phase structure. Each phase has an explicit named entry header, entry conditions, exit conditions, and a phase-completion statement. C-33 is implemented as a required PHASE 1 COMPLETE statement that must be written before gate checklist evaluation begins, making the completion statement the structurally enforced gate entry event. C-34: dictionary with Behavioral Signals column. C-35: SCAN TABLE Hypothesis Held column + GAPS TABLE "prediction not resolved" gap type.

**Hypothesis**: Maximum lifecycle ceremony -- named entry, named exit, explicit pre/postconditions per phase -- makes phase boundaries the most structurally resistant to collapse. The gate entry condition in C-33 becomes a natural artifact of a lifecycle that already requires named entry and exit statements at every boundary.

---

```
You are running org-scan for the Signal plugin.

CRITICAL CONSTRAINT (stated here; restated at Phase 2 entry): This skill produces raw analysis only. No org chart. No reporting lines. No hierarchy diagrams. No "reports to" statements. No boxes-and-lines structure. Producing any org chart content is a failure of this skill.

---

GATE TOKEN PROTOCOL

Both tokens are defined here as named constants before Phase 1 begins.

PASS TOKEN: "Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]"
FAIL TOKEN: "Path floor not met"

---

INERTIA PATTERN DICTIONARY

Internalize this dictionary before Phase 1 begins. All Inertia Match values must use these labels exactly. Free text is structurally invalid -- unconstrained values make pattern comparison across runs unverifiable.

| # | Pattern Label | Description | Structural Tells | Behavioral Signals |
|---|---|---|---|---|
| 1 | Monolith | No service or namespace boundaries | Single package.json; flat root; no internal boundary imports | "Put it anywhere" is accepted guidance; incidents cascade; engineers resist decomposition proposals |
| 2 | Layered | Horizontal tiers drive directory structure | Tier-named directories (infra/app/ui); shared lib/ cuts across all domains | PRs cross layers frequently; engineers define themselves by tier not product; layer debates in code review |
| 3 | Domain-clustered | Domains drive directory and namespace structure | Domains contain own schemas, routes, tests | Teams identify by domain; cross-domain work requires explicit coordination; changes stay inside domain directories |
| 4 | Conway-frozen | Org chart mirrored in code structure | Directory names match team or squad names; team-scoped test areas | "That's not my area" is the boundary signal; git log reveals team handoffs; cross-boundary changes require approvals |
| 5 | Feature-team | Cross-cutting feature teams own slices end-to-end | Feature flags; per-feature configs; no exclusive infra owner | Teams identified by feature name; independent shipping; cross-team ownership disputes are rare |
| 6 | Platform-product | Shared platform layer separate from product teams | platform/, infra/, shared/ directories distinct from product features | Product teams treat platform as a dependency with SLA expectations; "talk to platform" for infra questions |
| 7 | Ambiguous | Insufficient evidence to classify | Mixed structural signals across source types | Ownership descriptions conflict among team members; no consistent boundary language |

---

OUTPUT SCHEMA (COMPLETE)

This schema governs every table in this skill. Status applies to every column.

SCAN TABLE (Phase 1 produces this)
| Column | Status | Notes |
|---|---|---|
| Source | REQUIRED | Source type + specific file or directory path |
| Finding | REQUIRED | Observed fact only; no inference |
| Inertia Match | REQUIRED | Dictionary label only; precedes File Path Evidence; free text is invalid |
| File Path Evidence | REQUIRED | Specific file path(s); 5-path floor is Phase 1 exit condition |
| Hypothesis Held | optional | yes / no / partial -- links to dominant pattern candidate from PHASE 1 COMPLETE statement |

Column order rule: Inertia Match precedes File Path Evidence in every SCAN TABLE row. This is a structural schema constraint, not a layout preference. Inverting the order is a schema violation.

BOUNDARY TABLE (Phase 2 produces this)
| Column | Status | Notes |
|---|---|---|
| Boundary Name | REQUIRED | Named candidate seam |
| Inertia Match | REQUIRED | Dictionary label anchoring this boundary |
| File Path Evidence | REQUIRED | Paths that evidence this boundary |
| Seam Rationale | REQUIRED | Why this is a natural team split point |

CONCERNS TABLE (Phase 2 produces this)
| Column | Status | Notes |
|---|---|---|
| Concern Name | REQUIRED | Named cross-cutting concern |
| Boundaries Crossed | REQUIRED | Which boundaries this concern spans |
| Boundary Note | REQUIRED | Why it cannot be contained within one boundary |

HEADCOUNT TABLE (Phase 2 produces this)
| Column | Status | Notes |
|---|---|---|
| Domain | REQUIRED | Named expertise domain |
| Expertise Signal | REQUIRED | Scan evidence for distinct expertise |
| Contributor Estimate | optional | Inferable from test scope or git ownership signals |

ORG SHAPE TABLE (Phase 2 produces this)
| Column | Status | Notes |
|---|---|---|
| State | REQUIRED | "Current State" or "Recommended State" -- exactly one row each |
| Shape | REQUIRED | Named org shape |
| Justification | REQUIRED | Must cite SCAN TABLE rows |
| Dominant Inertia Pattern | REQUIRED | From PASS TOKEN |

GAPS TABLE (Phase 2 produces this)
| Column | Status | Notes |
|---|---|---|
| Gap Type | REQUIRED | Named category: source gap / fabrication risk / ambiguity / prediction not resolved |
| Description | REQUIRED | What is unknown or unresolved |
| Affected Sections | optional | Which synthesis tables this gap touches |
| Resolution Condition | REQUIRED | What evidence would close this gap |

CRITICAL CONSTRAINT (restated in output schema): All tables are raw analysis. No org chart. No reporting lines.

---

PHASE 1: EVIDENCE COLLECTION

Entry condition: Inertia Pattern Dictionary has been internalized. Gate Token Protocol tokens are defined. This is the first phase -- no gate has been passed yet.

Objective: Populate SCAN TABLE with observed facts from the repository. Do not infer or synthesize at this stage.

Anti-fabrication rule (Phase 1): Record only what is directly observable in named source files. If a source type is absent or yields no finding, record "not found" in the Finding column. Do not infer team structure from findings.

Scan all 7 source types. Cover at least 3 of the 7:
1. CLAUDE.md files -- ownership signals, team context, workflow instructions
2. package.json files -- dependency clusters, workspace or script boundaries
3. design/ directories -- design doc ownership and topical scope
4. Namespace directories -- plugin namespaces and their scoping signals
5. Test coverage areas -- what is tested, test scope boundaries
6. SPECS.md or specs/ files -- specification ownership and topic areas
7. .craft/roles/ directories -- existing role definitions and their stated scope

For each finding, populate all REQUIRED SCAN TABLE columns. Collect at least 5 distinct file paths across File Path Evidence entries. Fill Hypothesis Held for each row using the dominant pattern you identified by end of scan.

Phase 1 exit conditions (all must be true before the PHASE 1 COMPLETE statement is written):
- At least 3 distinct source types are covered
- At least 5 distinct file paths appear in File Path Evidence across all rows
- Every Inertia Match cell contains a dictionary label
- Column order is correct in every row (Inertia Match before File Path Evidence)

Write this statement when Phase 1 exit conditions are met:

PHASE 1 COMPLETE: [N source types covered], [M distinct file paths collected], dominant pattern candidate: [pattern label or "undetermined"]

---

PHASE 1 / PHASE 2 BOUNDARY: GATE EVALUATION:

Gate entry condition: The PHASE 1 COMPLETE statement has been written above. Do not evaluate the gate checklist until that statement appears.

This boundary is a hard sequencing gate. Phase 2 cannot begin until gate evaluation is complete and the PASS TOKEN is written.

Evaluate each item in order; do not skip:

1. SCAN TABLE has at least 3 distinct source types (check Source column values).
2. SCAN TABLE has at least 5 distinct file paths in File Path Evidence across all rows. If this item fails: Write "Path floor not met". Halt. Do not begin Phase 2.
3. Every Inertia Match cell contains a dictionary label. No empty cells. No free text entries.
4. Finding column entries are observed facts. No synthesis language, no modal verbs (should, implies, suggests) in Phase 1 findings.
5. Inertia Match precedes File Path Evidence in every row. Note any row where column order is inverted as a schema violation.

If all items pass: Write the PASS TOKEN.
If item 2 fails: Write the FAIL TOKEN. Halt.

Phase 1 postcondition: SCAN TABLE has 3+ source types, 5+ distinct file paths, dictionary labels in all Inertia Match cells, no synthesis language in findings, column order verified, and PASS TOKEN is written.

Phase 2 precondition: Phase 1 postcondition is satisfied and PASS TOKEN is written.

These two blocks name the same contract from both sides. Both must hold before Phase 2 begins.

---

PHASE 2: SYNTHESIS

Entry condition: PASS TOKEN has been written. Phase 1 postcondition is satisfied.

CRITICAL CONSTRAINT (restated at Phase 2 entry): This skill produces raw analysis only. No org chart. No reporting lines. No hierarchy diagrams.

Anti-fabrication rule (Phase 2): Every claim in every synthesis table must trace to a named SCAN TABLE row. Unlabeled inference is prohibited. If no SCAN TABLE row supports a claim, do not make it -- add it to GAPS TABLE as a fabrication risk.

Produce each output section in order:

SECTION 2.1: AREAS OF WORK (prose list): Name each distinct area of work visible in the SCAN TABLE. Cite the SCAN TABLE row(s) that evidence each area. No area without a citation.

SECTION 2.2: BOUNDARY TABLE: List team boundary candidates. Seam Rationale must explain why the boundary is a natural split point, not just where a directory boundary exists.

SECTION 2.3: CONCERNS TABLE: List cross-cutting concerns that span multiple boundaries. Boundary Note must explain why each resists containment within a single team.

SECTION 2.4: HEADCOUNT TABLE: List distinct expertise domains signaled by the scan. After the table write: "Estimated headcount: [X]-[Y] engineers. Rationale: [2-3 sentences drawing on HEADCOUNT TABLE rows above.]"

SECTION 2.5: ORG SHAPE TABLE: Exactly two rows -- Current State and Recommended State. Reference the dominant inertia pattern from the PASS TOKEN. Separate current state from recommended state clearly -- label each.

SECTION 2.6: GAPS TABLE: Flag every gap. Gap types: source gap (source not scanned or absent), fabrication risk (inference without SCAN TABLE support), ambiguity (contradictory signals), prediction not resolved (a Hypothesis Held value is "partial" or the PHASE 1 COMPLETE dominant pattern candidate was not confirmed or disconfirmed by gate evaluation). Do not omit gaps to appear complete.

Phase 2 exit conditions: All six sections produced. GAPS TABLE does not omit known gaps. ORG SHAPE TABLE has exactly two rows with Current State and Recommended State labeled and separated.
```

---

## V-04

**Variation axis**: Inertia Framing + Output Format (combined) -- the Inertia Pattern Dictionary leads the entire prompt as PRIMARY ANALYTICAL FRAMEWORK before any other content. Three-phase structure: HYPOTHESIS -> EVIDENCE -> SYNTHESIS. Phase 1 is hypothesis formation: classify the likely inertia pattern before scanning. Phase 2 is evidence collection with hypothesis tracking. C-33: EVIDENCE COLLECTION COMPLETE statement required before gate entry. C-34: most prominent dictionary treatment (dictionary as the analytical spine of the skill). C-35: SCAN TABLE has Hypothesis Held column linking each row to Phase 1 prediction; GAPS TABLE has "prediction not resolved" gap type completing the hypothesis-test-result loop.

**Hypothesis**: Leading with the dictionary as PRIMARY ANALYTICAL FRAMEWORK changes the agent's posture from "scan then classify" to "hypothesize then verify" -- the hypothesis-driven framing makes Hypothesis Held in C-35 structurally necessary rather than a bolted-on tracking column.

---

```
You are running org-scan for the Signal plugin.

CRITICAL CONSTRAINT (stated here; restated in output schema): This skill produces raw analysis only. No org chart. No reporting lines. No hierarchy diagrams. No "reports to" statements. No boxes-and-lines structure. Producing any org chart content is a failure of this skill.

---

INERTIA PATTERN DICTIONARY (PRIMARY ANALYTICAL FRAMEWORK)

This dictionary is the analytical spine of this skill. Every finding, boundary, and synthesis claim is anchored to a dictionary label. Internalize this dictionary before Phase 1 begins. All Inertia Match values must use these labels exactly. Free text is structurally invalid -- unconstrained values make pattern comparison across runs unverifiable.

| # | Pattern Label | Description | Structural Tells | Behavioral Signals |
|---|---|---|---|---|
| 1 | Monolith | Single codebase, no service or namespace separation | Single package.json; flat root directory; no internal boundary imports | "It's all in one repo" is accepted truth; incidents cascade across features; "just add it to main" is default guidance; engineers resist decomposition |
| 2 | Layered | Horizontal tiers drive directory and ownership structure | Tier-named directories (infra/app/presentation); shared util/ or lib/ crosses all features | Engineers identify as "infra person" not "billing person"; layer debates dominate code review; "which layer owns this?" recurs in retrospectives |
| 3 | Domain-clustered | Ownership domains drive directory and namespace structure | Domains contain own schemas, routes, tests; cross-domain imports are exceptional | Teams identify by domain; cross-domain work requires explicit handoff; incidents stay within domain boundaries |
| 4 | Conway-frozen | Current org chart mirrored in code; team ownership encoded in directory structure | Directory names match team or squad names; tests scoped to team areas | "That's not my area" is the cross-boundary signal; git log reveals team handoffs; approval chains follow org chart |
| 5 | Feature-team | Cross-cutting feature teams own a vertical slice end-to-end | Feature flags; A/B infra; per-feature configs; no exclusive infra owner | Teams identified by feature name; ship independently; cross-team code ownership disputes are rare |
| 6 | Platform-product | Shared platform layer separate from product feature teams | platform/, infra/, shared/ directories distinct from product feature directories | Product teams treat platform as a service with SLA expectations; "file a platform ticket" for infra changes |
| 7 | Ambiguous | Insufficient evidence to classify; signals contradict or are absent | Mixed tells across source types; no consistent directory convention | Team members describe ownership differently; "it depends who you ask" is a common answer |

---

GATE TOKEN PROTOCOL

Both tokens defined here as named constants before Phase 1 begins.

PASS TOKEN: "Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]"
FAIL TOKEN: "Path floor not met"

---

OUTPUT SCHEMA (COMPLETE -- defined before instructions to govern all phases)

This schema governs every table in this skill. Status applies to every column.

TABLE A -- PATTERN HYPOTHESES (Phase 1 produces this)
| Column | Status | Notes |
|---|---|---|
| Pattern Label | REQUIRED | Dictionary label being evaluated |
| Prior Assessment | REQUIRED | Likely / possible / unlikely -- initial classification before scanning |
| Supporting Signals | REQUIRED | What repository signals would confirm this pattern |
| Confidence Prior | optional | High / medium / low -- how strong is the prior before evidence |

TABLE B -- SCAN TABLE (Phase 2 produces this)
| Column | Status | Notes |
|---|---|---|
| Source | REQUIRED | Source type + specific file or directory path |
| Finding | REQUIRED | Observed fact only; no inference |
| Inertia Match | REQUIRED | Dictionary label only; precedes File Path Evidence; free text is a schema violation |
| File Path Evidence | REQUIRED | Specific file path(s); 5-path floor is a gate precondition |
| Hypothesis Held | optional | yes / no / partial -- references TABLE A pattern assessment for the matched label |

Column order rule: Inertia Match precedes File Path Evidence in every TABLE B row. This is a schema constraint, not a display preference. Inverting the order is a schema violation.

TABLE C -- BOUNDARY TABLE (Phase 3 produces this)
| Column | Status | Notes |
|---|---|---|
| Boundary Name | REQUIRED | Named candidate seam |
| Inertia Match | REQUIRED | Dictionary label anchoring this boundary |
| File Path Evidence | REQUIRED | Paths that evidence this boundary candidate |
| Seam Rationale | REQUIRED | Why this is a natural team split point |

TABLE D -- CONCERNS TABLE (Phase 3 produces this)
| Column | Status | Notes |
|---|---|---|
| Concern Name | REQUIRED | Named cross-cutting concern |
| Boundaries Crossed | REQUIRED | Which TABLE C boundaries this concern spans |
| Boundary Note | REQUIRED | Why it cannot be contained within one boundary |

TABLE E -- HEADCOUNT TABLE (Phase 3 produces this)
| Column | Status | Notes |
|---|---|---|
| Domain | REQUIRED | Named expertise domain |
| Expertise Signal | REQUIRED | Evidence of distinct expertise requirement |
| Contributor Estimate | optional | Inferable from test scope or git coverage signals |

TABLE F -- ORG SHAPE TABLE (Phase 3 produces this)
| Column | Status | Notes |
|---|---|---|
| State | REQUIRED | "Current State" or "Recommended State" -- exactly one row each |
| Shape | REQUIRED | Named org shape |
| Justification | REQUIRED | Must cite TABLE B rows |
| Dominant Inertia Pattern | REQUIRED | From PASS TOKEN |

TABLE G -- GAPS TABLE (Phase 3 produces this)
| Column | Status | Notes |
|---|---|---|
| Gap Type | REQUIRED | Named category: source gap / fabrication risk / ambiguity / prediction not resolved |
| Description | REQUIRED | What is unknown or unresolved |
| Affected Tables | optional | Which output tables this gap touches |
| Resolution Condition | REQUIRED | What evidence would close this gap |

CRITICAL CONSTRAINT (restated in output schema): TABLE A through TABLE G are raw analysis. No org chart. No reporting lines. No hierarchy diagrams.

---

PHASE 1: PATTERN HYPOTHESIS

Before scanning any files, form initial pattern hypotheses using the INERTIA PATTERN DICTIONARY as your analytical framework.

Produce TABLE A -- PATTERN HYPOTHESES:
- For each dictionary label, assess Prior: Likely / possible / unlikely based on any context signals available (repository name, CLAUDE.md excerpt if visible, plugin description).
- Name the Supporting Signals you will look for when scanning.
- TABLE A is your prediction. Phase 2 will test it.

---

PHASE 2: EVIDENCE COLLECTION

Anti-fabrication rule (Phase 2): Populate TABLE B with observed facts only. If a source type is absent, record "not found". Do not infer team structure at this stage.

Scan all 7 source types. Cover at least 3 of the 7:
1. CLAUDE.md files -- ownership signals, team context, workflow notes
2. package.json files -- dependency clusters, workspace or monorepo boundaries
3. design/ directories -- design doc scope and authorship signals
4. Namespace directories -- plugin namespaces and their scoping
5. Test coverage areas -- what is tested, who owns which test suites
6. SPECS.md or specs/ files -- specification ownership and topic scope
7. .craft/roles/ directories -- existing role definitions

For each finding, populate all REQUIRED TABLE B columns. Collect at least 5 distinct file paths in File Path Evidence. Fill Hypothesis Held for each row using TABLE A: "yes" if the finding confirms the matched pattern was predicted Likely, "no" if it contradicts, "partial" if evidence is mixed.

When all Phase 2 work is complete, write this statement before gate entry:

EVIDENCE COLLECTION COMPLETE: [N source types covered], [M distinct file paths collected], dominant pattern: [pattern label that received the most confirming Hypothesis Held values]

---

PHASE 2 / PHASE 3 BOUNDARY: GATE EVALUATION:

Gate entry condition: The EVIDENCE COLLECTION COMPLETE statement has been written above. Do not evaluate the gate checklist until that statement appears.

This boundary is a hard sequencing gate. Phase 3 cannot begin until gate evaluation is complete and the PASS TOKEN is written.

Evaluate each item in order; do not skip:

1. TABLE B has at least 3 distinct source types covered.
2. TABLE B has at least 5 distinct file paths in File Path Evidence across all rows. If this item fails: Write "Path floor not met". Halt. Do not begin Phase 3.
3. Every Inertia Match cell contains a dictionary label. No free text.
4. Finding column contains observed facts only. No synthesis language.
5. Inertia Match precedes File Path Evidence in every TABLE B row. Note any schema violation.

If all items pass: Write the PASS TOKEN.
If item 2 fails: Write the FAIL TOKEN. Halt.

Phase 2 postcondition: TABLE B has 3+ source types, 5+ distinct file paths, dictionary labels in all Inertia Match cells, and PASS TOKEN is written.

Phase 3 precondition: Phase 2 postcondition is satisfied and PASS TOKEN is written.

These two blocks name the same contract from both sides. Both must hold before Phase 3 begins.

---

PHASE 3: SYNTHESIS

CRITICAL CONSTRAINT (restated at Phase 3 entry): This skill produces raw analysis only. No org chart. No reporting lines. No hierarchy diagrams.

Anti-fabrication rule (Phase 3): Every claim in TABLE C through TABLE G must trace to a named TABLE B row. Unlabeled inference is prohibited.

Produce outputs in order:

1. AREAS OF WORK (prose list before TABLE C): Name each distinct work area visible in TABLE B. Cite TABLE B row(s) for each. No area without evidence.

2. TABLE C -- BOUNDARY TABLE: List team boundary candidates. Seam Rationale must justify the split point analytically.

3. TABLE D -- CONCERNS TABLE: List cross-cutting concerns. Boundary Note must explain why each resists single-team ownership.

4. TABLE E -- HEADCOUNT TABLE: List distinct expertise domains. After the table write: "Estimated headcount: [X]-[Y] engineers. Rationale: [2-3 sentences drawing on TABLE E rows above.]"

5. TABLE F -- ORG SHAPE TABLE: Exactly two rows -- Current State and Recommended State. Reference the dominant inertia pattern from the PASS TOKEN. Separate current state from recommended state clearly -- label each.

6. TABLE G -- GAPS TABLE: Flag every gap. Include "prediction not resolved" as a gap type when: (a) a TABLE B Hypothesis Held value is "partial", or (b) a TABLE A pattern rated Likely was neither confirmed nor disconfirmed by TABLE B findings. Do not omit gaps to appear complete.
```

---

## V-05

**Variation axis**: Phrasing Register + Lifecycle Emphasis (combined) -- tightest command register throughout. All instructions are imperative verb phrases. GROUP A / GROUP B structural labels. Named entry and exit conditions per group, stated as brief numbered lists. C-33: required sentence before checklist stated in shortest possible form ("Write SCAN COMPLETE before evaluating:"). C-34: behavioral signals in compact three-column dictionary. C-35: Hypothesis Held column stated as mandatory output constraint with vocabulary enforcement.

**Hypothesis**: Maximum concision reduces ambiguity surface. Every rule is a verb phrase with no hedging. The tight register makes non-compliance structurally obvious because any output that doesn't match the named token or table structure is visibly wrong at a glance.

---

```
You are running org-scan for the Signal plugin.

CRITICAL CONSTRAINT (stated here; restated in GROUP B): This skill produces raw analysis only. No org chart. No reporting lines. No hierarchy diagrams. Non-negotiable.

---

GATE TOKEN PROTOCOL

Define both tokens now. Use by name throughout.

PASS TOKEN: "Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]"
FAIL TOKEN: "Path floor not met"

---

INERTIA PATTERN DICTIONARY

Use these labels only in all Inertia Match columns. No free text. Free text is structurally invalid -- unconstrained values make pattern comparison across runs unverifiable.

| # | Pattern Label | Structural Tells | Behavioral Signals |
|---|---|---|---|
| 1 | Monolith | Single package.json; flat root; no boundary imports | "Put it anywhere"; incidents cascade; engineers resist decomposition |
| 2 | Layered | Tier-named directories; shared lib/ cuts all features | Engineers identify by tier not domain; layer debates in code review |
| 3 | Domain-clustered | Domains own schemas + routes + tests | Teams identify by domain; cross-domain work needs explicit handoff |
| 4 | Conway-frozen | Directory names match team names; team-scoped tests | "That's not my area" signals boundaries; handoffs visible in git log |
| 5 | Feature-team | Feature flags; per-feature configs; no single infra owner | Teams identified by feature name; ship independently |
| 6 | Platform-product | platform/ and shared/ distinct from product directories | Product treats platform as dependency with SLA expectations |
| 7 | Ambiguous | Mixed structural signals across source types | Ownership descriptions conflict; "it depends who you ask" |

---

OUTPUT SCHEMA (COMPLETE)

This schema governs every table in this skill. Status applies to every column.

SCAN TABLE
| Column | Status | Notes |
|---|---|---|
| Source | REQUIRED | Source type + specific file path |
| Finding | REQUIRED | Observed fact; no inference |
| Inertia Match | REQUIRED | Dictionary label only; precedes File Path Evidence |
| File Path Evidence | REQUIRED | Specific file path(s); 5-path minimum is a gate condition |
| Hypothesis Held | optional | yes / no / partial -- vocabulary constrained; no other values accepted |

Column order mandatory: Inertia Match before File Path Evidence in every row. Inverting the order is a schema violation.

S1 -- BOUNDARY TABLE
| Column | Status | Notes |
|---|---|---|
| Boundary Name | REQUIRED | Named candidate seam |
| Inertia Match | REQUIRED | Dictionary label |
| File Path Evidence | REQUIRED | Paths evidencing this boundary |
| Seam Rationale | REQUIRED | Why this is a natural split |

S2 -- CONCERNS TABLE
| Column | Status | Notes |
|---|---|---|
| Concern Name | REQUIRED | Named cross-cutting concern |
| Boundaries Crossed | REQUIRED | Which boundaries it spans |
| Boundary Note | REQUIRED | Why it resists containment |

S3 -- HEADCOUNT TABLE
| Column | Status | Notes |
|---|---|---|
| Domain | REQUIRED | Named expertise domain |
| Expertise Signal | REQUIRED | Scan evidence for distinct expertise |
| Contributor Estimate | optional | Inferable from test scope or git signals |

S4 -- ORG SHAPE TABLE
| Column | Status | Notes |
|---|---|---|
| State | REQUIRED | "Current State" or "Recommended State" -- one row each |
| Shape | REQUIRED | Named org shape |
| Justification | REQUIRED | Cite SCAN TABLE rows |
| Dominant Inertia Pattern | REQUIRED | From PASS TOKEN |

S5 -- GAPS TABLE
| Column | Status | Notes |
|---|---|---|
| Gap Type | REQUIRED | Named: source gap / fabrication risk / ambiguity / prediction not resolved |
| Description | REQUIRED | What is unknown |
| Affected Sections | optional | Which synthesis tables this gap touches |
| Resolution Condition | REQUIRED | What evidence closes this gap |

CRITICAL CONSTRAINT (restated in output schema): Raw analysis only. No org chart. No reporting lines.

---

GROUP A -- SCAN

Entry: Inertia Pattern Dictionary internalized. Gate tokens defined. Phase has not begun yet.

Anti-fabrication rule (scan): Record observed facts only. "Not found" if a source is absent. No inference.

Scan at least 3 of these 7 source types:
1. CLAUDE.md files
2. package.json files
3. design/ directories
4. Namespace directories
5. Test coverage areas
6. SPECS.md or specs/ files
7. .craft/roles/ directories

For each finding: populate all REQUIRED SCAN TABLE columns. Collect 5+ distinct file paths across File Path Evidence entries. Fill Hypothesis Held using yes / no / partial vocabulary only.

Group A exit conditions (all must be true before SCAN COMPLETE is written):
- 3+ source types covered
- 5+ distinct file paths in File Path Evidence
- All Inertia Match cells contain dictionary labels
- Column order correct in every row

Write SCAN COMPLETE before evaluating the gate checklist:

SCAN COMPLETE: [N source types covered], [M distinct file paths collected], dominant pattern: [pattern label or "undetermined"]

---

GROUP A / GROUP B BOUNDARY: GATE EVALUATION:

Gate entry condition: SCAN COMPLETE token written above. Do not evaluate until it appears.

Hard gate. GROUP B cannot begin until PASS TOKEN is written.

Evaluate each item in order; do not skip:

1. SCAN TABLE: 3+ distinct source types covered.
2. SCAN TABLE: 5+ distinct file paths in File Path Evidence total. Item 2 fails: Write "Path floor not met". Stop.
3. All Inertia Match cells: dictionary labels only. No empty cells. No free text.
4. Finding column: observed facts only. No modal or synthesis language.
5. Inertia Match precedes File Path Evidence in every row. Flag any inversion. Inverting the order is a schema violation.

Pass: Write PASS TOKEN.
Fail item 2: Write FAIL TOKEN. Stop.

Phase 1 postcondition: SCAN TABLE has 3+ sources, 5+ paths, dictionary labels in all Inertia Match cells, PASS TOKEN written.

Phase 2 precondition: Phase 1 postcondition is met. PASS TOKEN is written.

These two blocks name the same contract from both sides. Both must hold before GROUP B begins.

---

GROUP B -- SYNTHESIS

Entry: PASS TOKEN written. Phase 1 postcondition verified.

CRITICAL CONSTRAINT (restated): Raw analysis only. No org chart. No reporting lines.

Anti-fabrication rule: Cite SCAN TABLE row for every claim. No unlabeled inference.

Produce in order:

Step 1 -- AREAS OF WORK (prose): List distinct work areas. Cite SCAN TABLE row for each. No evidence? Write: "Area not evidenced -- insufficient scan signal."

Step 2 -- S1 BOUNDARY TABLE: List boundary candidates. Seam Rationale: explain the natural split, not just the directory location.

Step 3 -- S2 CONCERNS TABLE: List cross-cutting concerns. Boundary Note: explain why each resists single-team ownership.

Step 4 -- S3 HEADCOUNT TABLE: List expertise domains. After the table write: "Estimated headcount: [X]-[Y] engineers. Rationale: [2-3 sentences from S3 rows.]"

Step 5 -- S4 ORG SHAPE TABLE: Two rows: Current State, Recommended State. Reference dominant inertia pattern from PASS TOKEN. Separate current state from recommended state clearly. Label each.

Step 6 -- S5 GAPS TABLE: Flag every gap. Include "prediction not resolved" when a SCAN TABLE Hypothesis Held value is "partial" or when the SCAN COMPLETE dominant pattern was not confirmed or disconfirmed by gate evaluation. Do not omit gaps to appear complete.

Group B exit conditions:
- All six steps produced.
- S4 has exactly two labeled rows.
- S5 does not omit known gaps.
- Current State and Recommended State labeled and separated.
```
