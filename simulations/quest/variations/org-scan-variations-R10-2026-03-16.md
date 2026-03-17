Variations written to `simulations/quest/variations/org-scan-variations-R10-2026-03-16.md`.

---

## Summary

R10 produced 5 complete variations targeting the 5 new criteria (C-36–C-40) from R9's excellence signals:

| Variation | Primary Axis | Hypothesis |
|---|---|---|
| **V-01** | Role Sequence + C-36 | 4-role control-transfer chain (PREDICTOR→SCANNER→GATEKEEPER→SYNTHESIZER) — gate entry failure = role handoff failure, strongest behavioral binding |
| **V-02** | Schema-first (C-37) | TABLE A–G declared before any instruction — prediction table visible before scan instructions, C-39 falls out structurally |
| **V-03** | Lifecycle ceremony (C-38) | PHASE 0/1/2/3 with named EXIT CONDITION + ENTRY CONDITION at every boundary — PHASE 1 exit IS the control-transfer declaration |
| **V-04** | C-39+C-40 combination | Dictionary as PRIMARY ANALYTICAL FRAMEWORK declared before instructions; PREDICTOR role applies it to form predictions; three-table chain (TABLE A→TABLE B→TABLE G) is structurally necessary |
| **V-05** | Full integration, tight register | All five criteria in 4 named preamble blocks (BLOCK 1: framework, BLOCK 2: schema, BLOCK 3: gate tokens, BLOCK 4: role protocol) — maximum density, minimum verbosity |

**R10 structural differentiators vs R9:**
- All 5 variations add a PREDICTOR role that runs before SCANNER (C-39 fully structural, not a tracking column)
- All 5 add TABLE A (prediction table) to the schema — part of the schema-first declaration (C-37)
- All 5 have named exit conditions at every phase boundary, not just the primary gate (C-38)
- V-04 and V-05 explicitly declare the dictionary as PRIMARY ANALYTICAL FRAMEWORK in a named declaration before any instruction (C-40)
- V-01 and V-05 use "control transfers to GATEKEEPER" in the SCANNER COMPLETE declaration (C-36 strongest framing)
ur named roles. You occupy exactly one role at a time. Complete all work assigned to the current role before transitioning. Every role transition requires a named control-transfer declaration. A missing control-transfer declaration is a role boundary violation.

ROLE SEQUENCE: PREDICTOR -> SCANNER -> GATEKEEPER -> SYNTHESIZER

---

GATE TOKEN PROTOCOL

Both tokens defined here as named constants before any role begins. Reference by name throughout.

PASS TOKEN: "Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]"
FAIL TOKEN: "Path floor not met"

---

INERTIA PATTERN DICTIONARY -- PRIMARY ANALYTICAL FRAMEWORK

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK for this skill. It is not a post-scan labeling tool. It is the analytical spine through which all evidence is interpreted -- from prediction through verification through synthesis. Use it to form predictions before scanning, verify predictions during scanning, and resolve predictions during synthesis. Every Inertia Match value in TABLE B must use one of these labels exactly. Free text is structurally invalid -- unconstrained values make pattern comparison across runs unverifiable.

| # | Pattern Label | Description | Structural Tells | Behavioral Signals |
|---|---|---|---|---|
| 1 | Monolith | Single codebase, no service or namespace separation | Single package.json, flat root directory, no internal boundary imports | Teams say "it's all in one repo"; incidents affect unrelated features simultaneously; "just put it in utils" is common advice |
| 2 | Layered | Horizontal tiers drive directory structure (infra / app / presentation) | Directories named by tier not domain; shared util/ or lib/ layers cross all features | PRs frequently cross layers; "which layer owns this?" recurs in review; engineers define themselves by layer not product area |
| 3 | Domain-clustered | Ownership domains drive directory and namespace structure | Feature directories contain own schemas, routes, and tests; cross-domain imports are exceptional | Teams identify by domain ("I'm on billing"); changes stay inside domain directories; cross-domain work requires explicit handoff |
| 4 | Conway-frozen | Org chart mirrored in code; team boundaries are code boundaries | Directory names match team or squad names; test files scoped to team areas | Changes require coordination across owners; "that's not my area" is common; team handoffs visible in git log |
| 5 | Feature-team | Cross-cutting feature teams each own a slice end-to-end | Feature flags, A/B infra, per-feature configs; no single team owns infra exclusively | Teams identified by feature name; cross-team code ownership debates are rare; teams ship independently |
| 6 | Platform-product | Shared platform layer separate from product feature teams | platform/, infra/, shared/ directories distinct from product feature directories | Product teams treat platform as a dependency; platform has SLA expectations; "talk to platform" is the response to infra questions |
| 7 | Ambiguous | Insufficient evidence to classify; signals contradict or are absent | Mixed tells across source types; no consistent directory convention | Team members describe ownership differently; no shared boundary language; ownership questions produce disagreement |

---

OUTPUT SCHEMA

This schema governs every table in this skill. Status applies to every column across all tables. Declared before any role begins -- every instruction references a pre-declared table by name.

CRITICAL CONSTRAINT (restated): No org chart. No reporting lines. No hierarchy. Raw analysis only.

TABLE A -- PATTERN HYPOTHESIS (PREDICTOR output)
| Column | Status | Vocabulary |
|---|---|---|
| Pattern Label | REQUIRED | Dictionary label exactly |
| Prior Assessment | REQUIRED | Likely / Unlikely / Unknown |
| Rationale | REQUIRED | 1-2 sentences from prior context only -- no scan evidence yet |
| Verification Target | REQUIRED | Which source types should confirm or disconfirm this prediction |

TABLE B -- SCAN EVIDENCE (SCANNER output)
| Column | Status | Vocabulary |
|---|---|---|
| Finding | REQUIRED | One-sentence description |
| Source Type | REQUIRED | CLAUDE.md / package.json / design/ / namespace-structure / test-coverage / SPECS.md / .craft-roles |
| Inertia Match | REQUIRED | Dictionary label exactly -- must precede File Path Evidence -- free text is a schema violation |
| File Path Evidence | REQUIRED | At least 1 concrete file path per row |
| Hypothesis Held | optional | yes / no / partial -- links to TABLE A prediction for matched pattern |

Column order rule: Inertia Match precedes File Path Evidence in every TABLE B row. Inverting the order is a schema violation.

TABLE C -- BOUNDARY CANDIDATES (SCANNER output)
| Column | Status | Vocabulary |
|---|---|---|
| Boundary | REQUIRED | Team or area split candidate |
| Seam Rationale | REQUIRED | Why this is a natural split, not just a directory boundary |
| Evidence | REQUIRED | File path or source citation |
| Confidence | REQUIRED | High / Medium / Low |

TABLE D -- CROSS-CUTTING CONCERNS (SCANNER output)
| Column | Status | Vocabulary |
|---|---|---|
| Concern | REQUIRED | Named cross-cutting concern |
| Boundary Note | REQUIRED | Why this concern cannot be assigned to one team |
| Evidence | REQUIRED | File path or source citation |

TABLE E -- EVIDENCE GAPS (SCANNER output)
| Column | Status | Vocabulary |
|---|---|---|
| Gap | REQUIRED | Description of missing or ambiguous element |
| Gap Type | REQUIRED | source-absent / owner-unclear / scope-ambiguous / prediction-not-resolved |
| Impact | REQUIRED | What analysis is blocked by this gap |

TABLE F -- ORG SHAPE (SYNTHESIZER output)
| Column | Status | Vocabulary |
|---|---|---|
| State | REQUIRED | Current State / Recommended State |
| Shape | REQUIRED | Named org shape |
| Justification | REQUIRED | Reference dominant pattern from PASS TOKEN |

TABLE G -- PREDICTION RESOLUTION (SYNTHESIZER output)
| Column | Status | Vocabulary |
|---|---|---|
| Pattern Label | REQUIRED | From TABLE A |
| Prior Assessment | REQUIRED | From TABLE A |
| Evidence Verdict | REQUIRED | Confirmed / Disconfirmed / Insufficient Evidence |
| Resolution Note | REQUIRED | How TABLE B evidence resolved or failed to resolve this prediction |

---

ROLE: PREDICTOR

Entry condition: SCHEMA DECLARED AND DICTIONARY DECLARED. Begin PREDICTOR work.

Your sole task: form pattern predictions from the INERTIA PATTERN DICTIONARY -- PRIMARY ANALYTICAL FRAMEWORK before examining any evidence. Do not read file paths. Do not open directories. Use only prior context about the target repo.

Steps:
1. For each of the 7 dictionary patterns, assess: Likely / Unlikely / Unknown.
2. Populate TABLE A. Every row: dictionary label, prior assessment, rationale from context only, verification target.
3. Write at least 3 non-Unlikely assessments before proceeding.

Anti-fabrication rule: TABLE A rationale must derive from prior context only -- not from evidence not yet collected. If no prior context exists for a pattern, write "No prior context" in Rationale and Unknown in Prior Assessment.

Exit condition for PREDICTOR. Write the following control-transfer declaration exactly before transitioning:

PREDICTION COMPLETE -- control transfers to SCANNER

Do not begin SCANNER work until this control-transfer declaration appears above.

---

PREDICTOR / SCANNER BOUNDARY

Entry condition for SCANNER: The "PREDICTION COMPLETE -- control transfers to SCANNER" declaration has been written above. A missing declaration is a role boundary violation. Do not begin SCANNER work until that exact phrase appears.

---

ROLE: SCANNER

Entry condition: PREDICTION COMPLETE declaration written above.

SOURCE TYPES (scan at least 3 of 7):
1. CLAUDE.md files -- namespace structure, team conventions, vocabulary
2. package.json / manifest files -- dependency clusters, ownership signals
3. design/ directories -- bounded domain language, architectural intent
4. Namespace / directory structure -- team boundary candidates
5. Test coverage areas -- what teams actually own vs what they claim
6. SPECS.md / specification files -- planned vs actual scope
7. Existing .craft/roles/ files -- declared role structure

Steps:
1. Scan at least 3 source types. Record every finding in TABLE B.
2. Collect at least 5 distinct file paths across TABLE B rows. If fewer than 5 found, record a gap in TABLE E (gap type: source-absent) and continue -- do not invent paths.
3. For each TABLE B row that matches a TABLE A pattern, complete the Hypothesis Held column.
4. Populate TABLE C. Every Seam Rationale must explain why this is a natural split -- not just where a directory boundary exists.
5. Populate TABLE D. Every Boundary Note must explain why the concern cannot be assigned to a single team.
6. Populate TABLE E. For any TABLE A prediction whose Verification Target was not reached, add a row with Gap Type: prediction-not-resolved.
7. Write headcount signal: "Estimated headcount: [X]-[Y]. Rationale: [2-3 sentences]."

Anti-fabrication rule: Every TABLE B row must cite a real file path. If no file path exists for a finding, record it in TABLE E -- do not fabricate a path.

Exit condition for SCANNER. Write the following control-transfer declaration exactly before transitioning:

SCANNER COMPLETE -- control transfers to GATEKEEPER

Do not begin GATEKEEPER work until this control-transfer declaration appears above.

---

SCANNER / GATEKEEPER BOUNDARY: GATE EVALUATION

Entry condition for GATEKEEPER: The "SCANNER COMPLETE -- control transfers to GATEKEEPER" declaration has been written above. Gate entry failure is equivalent to a control-transfer failure between named roles -- the SCANNER has not handed off. Do not evaluate the gate checklist until that exact phrase appears.

Evaluate each item in order; do not skip:

1. Source coverage: Were at least 3 of the 7 source types scanned?
   -- If this item fails: Write "Source floor not met". Halt.

2. File path floor: Are at least 5 distinct file paths present across TABLE B rows?
   -- If this item fails: Write the FAIL TOKEN exactly. Halt. Do not begin SYNTHESIZER work.

3. Inertia Match column: Does every TABLE B row contain a dictionary-constrained value in Inertia Match?
   -- If this item fails: Write "Inertia Match not populated". Halt.

4. Column order: Does Inertia Match precede File Path Evidence in every TABLE B row?
   -- If this item fails: Write "Column order violated". Halt.

5. TABLE A predictions: Were at least 3 pattern predictions written in TABLE A before scanning began?
   -- If this item fails: Write "Prediction phase not completed". Halt.

SCANNER postcondition (confirmed before gate passes): TABLE B, TABLE C, TABLE D, TABLE E written. Headcount signal written.
SYNTHESIZER precondition (required before SYNTHESIZER begins): PASS TOKEN present below.
These two blocks name the same contract from both sides. Both must hold before SYNTHESIZER begins.

If all 5 items pass: Write PASS TOKEN exactly:
"Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]"

N = number of source types scanned. M = number of distinct file paths in TABLE B. Pattern label = most-evidenced dictionary label from TABLE B Inertia Match column.

---

GATEKEEPER / SYNTHESIZER BOUNDARY

Entry condition for SYNTHESIZER: PASS TOKEN written above. If FAIL TOKEN or halt string is written above, do not begin SYNTHESIZER work.

---

ROLE: SYNTHESIZER

Entry condition: PASS TOKEN written above.

Steps:
1. Produce TABLE F (ORG SHAPE). Exactly two rows: Current State and Recommended State. No org chart. No reporting lines. Reference dominant pattern from PASS TOKEN.
2. Produce TABLE G (PREDICTION RESOLUTION). For every TABLE A row: Confirmed / Disconfirmed / Insufficient Evidence. Cite TABLE B row(s). If Likely in TABLE A but not evidenced, write "Disconfirmed -- evidence suggests [alternative dictionary label]."
3. Write AREAS section: name each area of work inferred from TABLE B. Every area cites at least one TABLE B row. Anti-fabrication: if no evidence, do not name the area.
4. Write HEADCOUNT SIGNAL: restate the estimate from SCANNER; add synthesis commentary.
5. Write TEAM SHAPE RECOMMENDATION: reference TABLE F and TABLE G. Name the dominant inertia pattern. State what the current shape resists and what a recommended shape must overcome.

Exit condition: SYNTHESIZER COMPLETE.
```

---

## V-02

**Variation axis**: Output format -- schema-first table definition. TABLE A through TABLE G are declared as named letter-identified tables in a single SCHEMA DECLARATION block before any phase, group, or role instruction begins. Every instruction references a pre-declared table by letter. The full output structure is inspectable before reading a single instruction.

**Hypothesis**: When the prediction table (TABLE A) appears in the schema before any instructions, the hypothesis-first requirement (C-39) becomes a structural consequence of the schema declaration order -- agents see the prediction table before they see any scan instructions, priming the correct phase sequence without a separate mandate. The schema block also makes C-37 compliance visibly distinct from prose embedding of table definitions inside instructions.

---

```
You are running org-scan for the Signal plugin.

CRITICAL CONSTRAINT (stated here; restated in output schema): This skill produces raw analysis only. No org chart. No reporting lines. No hierarchy diagrams. No "reports to" statements. No boxes-and-lines structure. Any org chart content is a failure of this skill regardless of how complete other sections are.

---

INERTIA PATTERN DICTIONARY -- PRIMARY ANALYTICAL FRAMEWORK

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK for this skill. All Inertia Match values across all tables must use these labels exactly. Free text is structurally invalid -- unconstrained values make pattern comparison across runs unverifiable.

| # | Pattern Label | Description | Structural Tells | Behavioral Signals |
|---|---|---|---|---|
| 1 | Monolith | Single codebase, no service or namespace separation | Single package.json, flat root, no internal boundary imports | "Just put it in utils"; incidents affect unrelated features; teams can't describe their scope |
| 2 | Layered | Horizontal tiers drive directory structure | Directories named by tier; shared util/lib cross all features | "Which layer owns this?"; engineers identify by tier not product area |
| 3 | Domain-clustered | Ownership domains drive directory and namespace structure | Feature dirs contain own schemas, routes, tests | Teams identify by domain; changes stay inside directories; cross-domain work needs explicit handoff |
| 4 | Conway-frozen | Org chart mirrored in code | Directory names match team names; test files scoped to team areas | "That's not my area"; changes need multi-team coordination; team handoffs visible in git log |
| 5 | Feature-team | Cross-cutting feature teams each own a slice end-to-end | Per-feature configs, flags; no single team owns infra exclusively | Teams identified by feature name; ship independently |
| 6 | Platform-product | Shared platform layer separate from product feature teams | platform/, infra/, shared/ distinct from product feature dirs | "Talk to platform"; product treats platform as dependency; platform has SLA expectations |
| 7 | Ambiguous | Insufficient evidence to classify; signals contradict or are absent | Mixed tells; no consistent directory convention | Ownership questions produce disagreement; no shared boundary language |

---

SCHEMA DECLARATION

All output tables are defined here with named letter identifiers before any phase instruction begins. Every instruction in this skill references a pre-declared table by letter. The full output schema is structurally inspectable here before reading a single instruction.

This schema governs every table in this skill. Status applies to every column across all tables.

CRITICAL CONSTRAINT (restated): No org chart. No reporting lines. No hierarchy. Raw analysis only.

TABLE A -- PATTERN HYPOTHESIS
Purpose: Predictions from the PRIMARY ANALYTICAL FRAMEWORK produced before evidence collection begins.
| Column | Status | Vocabulary |
|---|---|---|
| Pattern Label | REQUIRED | Dictionary label exactly |
| Prior Assessment | REQUIRED | Likely / Unlikely / Unknown |
| Rationale | REQUIRED | Prior context only -- no scan evidence |
| Verification Target | REQUIRED | Source types that should confirm or disconfirm |

TABLE B -- SCAN EVIDENCE
Purpose: Repository findings from active scanning.
| Column | Status | Vocabulary |
|---|---|---|
| Finding | REQUIRED | One-sentence description |
| Source Type | REQUIRED | CLAUDE.md / package.json / design/ / namespace-structure / test-coverage / SPECS.md / .craft-roles |
| Inertia Match | REQUIRED | Dictionary label exactly -- must precede File Path Evidence -- free text is a schema violation |
| File Path Evidence | REQUIRED | At least 1 concrete file path |
| Hypothesis Held | optional | yes / no / partial -- links to TABLE A prediction for matched pattern |

Column order constraint: Inertia Match precedes File Path Evidence in every TABLE B row. Inverting the order is a schema violation.

TABLE C -- BOUNDARY CANDIDATES
Purpose: Natural team or area split candidates with seam rationale.
| Column | Status | Vocabulary |
|---|---|---|
| Boundary | REQUIRED | Team or area split candidate name |
| Seam Rationale | REQUIRED | Natural split explanation -- not just "a directory boundary exists" |
| Evidence | REQUIRED | TABLE B row reference or file path |
| Confidence | REQUIRED | High / Medium / Low |

TABLE D -- CROSS-CUTTING CONCERNS
Purpose: Concerns that span candidate boundaries.
| Column | Status | Vocabulary |
|---|---|---|
| Concern | REQUIRED | Named cross-cutting concern |
| Boundary Note | REQUIRED | Why this concern cannot be assigned to one team |
| Evidence | REQUIRED | File path or source citation |

TABLE E -- EVIDENCE GAPS
Purpose: What is missing, ambiguous, or unresolvable from available sources.
| Column | Status | Vocabulary |
|---|---|---|
| Gap | REQUIRED | Description of missing or ambiguous element |
| Gap Type | REQUIRED | source-absent / owner-unclear / scope-ambiguous / prediction-not-resolved |
| Impact | REQUIRED | What analysis is blocked |

TABLE F -- ORG SHAPE
Purpose: Current and recommended org shape with pattern-referenced justification.
| Column | Status | Vocabulary |
|---|---|---|
| State | REQUIRED | Current State / Recommended State |
| Shape | REQUIRED | Named org shape |
| Justification | REQUIRED | Reference dominant pattern from PASS TOKEN |

TABLE G -- PREDICTION RESOLUTION
Purpose: Explicit closure of every TABLE A prediction against TABLE B evidence.
| Column | Status | Vocabulary |
|---|---|---|
| Pattern Label | REQUIRED | From TABLE A |
| Prior Assessment | REQUIRED | From TABLE A |
| Evidence Verdict | REQUIRED | Confirmed / Disconfirmed / Insufficient Evidence |
| Resolution Note | REQUIRED | TABLE B citation(s) resolving or failing to resolve the prediction |

---

GATE TOKEN PROTOCOL

Both tokens defined here as named constants before GROUP A begins.

PASS TOKEN: "Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]"
FAIL TOKEN: "Path floor not met"

---

GROUP A -- HYPOTHESIS PHASE

Entry condition: SCHEMA DECLARED. DICTIONARY DECLARED. Begin GROUP A.

Task: Produce TABLE A. Form predictions from the INERTIA PATTERN DICTIONARY -- PRIMARY ANALYTICAL FRAMEWORK before examining any evidence. Do not read file paths. Do not open directories. Use only prior context about the target repo.

Steps:
1. For each of the 7 dictionary patterns, assess: Likely / Unlikely / Unknown.
2. Populate TABLE A. Every row requires all four columns.
3. Produce at least 3 non-Unlikely assessments.

Anti-fabrication rule: TABLE A Rationale is prior context only. If no prior context for a pattern, write "No prior context" and Unknown.

GROUP A exit condition. Write the following exactly before GROUP B begins:

HYPOTHESIS COMPLETE -- control transfers to SCANNER

---

GROUP A / GROUP B BOUNDARY

Entry condition for GROUP B: "HYPOTHESIS COMPLETE -- control transfers to SCANNER" written above. Do not begin GROUP B until that phrase appears. A missing declaration is a phase boundary violation.

---

GROUP B -- SCAN PHASE

Entry condition: HYPOTHESIS COMPLETE declaration written above.

SOURCE TYPES (scan at least 3 of 7):
1. CLAUDE.md files
2. package.json / manifest files
3. design/ directories
4. Namespace / directory structure
5. Test coverage areas
6. SPECS.md / specification files
7. Existing .craft/roles/ files

Steps:
1. Scan at least 3 source types. Populate TABLE B.
2. Collect at least 5 distinct file paths across TABLE B rows. The 5-path floor is a gate precondition -- record shortfalls in TABLE E (gap type: source-absent).
3. For each TABLE B row matching a TABLE A pattern, complete Hypothesis Held.
4. Populate TABLE C. Every Seam Rationale names the natural split reason.
5. Populate TABLE D. Every Boundary Note explains why the concern spans teams.
6. Populate TABLE E. For any TABLE A Verification Target not reached, add a row with Gap Type: prediction-not-resolved.
7. Write headcount signal: "Estimated headcount: [X]-[Y]. Rationale: [2-3 sentences]."

Anti-fabrication rule: Every TABLE B row cites a real file path. Missing path = TABLE E entry, not TABLE B row.

GROUP B exit condition. Write the following exactly before gate evaluation:

SCAN COMPLETE -- control transfers to GATEKEEPER

---

GROUP A / GROUP B BOUNDARY: GATE EVALUATION

Entry condition for gate checklist: "SCAN COMPLETE -- control transfers to GATEKEEPER" written above. This boundary is a hard sequencing gate. GROUP C cannot begin until the gate is complete.

GROUP B postcondition (SCANNER confirms): TABLE B, TABLE C, TABLE D, TABLE E written. Headcount signal written.
GROUP C precondition (SYNTHESIZER requires): PASS TOKEN written below.
These two blocks name the same contract from both sides. Both must hold before GROUP C begins.

Evaluate each item in order; do not skip:

1. Source coverage: At least 3 source types scanned?
   -- Fails: Write "Source floor not met". Halt.
2. File path floor: At least 5 distinct file paths in TABLE B?
   -- Fails: Write FAIL TOKEN exactly. Halt. Do not begin GROUP C.
3. Inertia Match: Every TABLE B row has a dictionary-constrained value?
   -- Fails: Write "Inertia Match not populated". Halt.
4. Column order: Inertia Match precedes File Path Evidence in every TABLE B row?
   -- Fails: Write "Column order violated". Halt.
5. TABLE A populated: At least 3 predictions written in GROUP A?
   -- Fails: Write "Prediction phase not completed". Halt.

If all pass: Write PASS TOKEN:
"Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]"

---

GROUP C -- SYNTHESIS PHASE

Entry condition: PASS TOKEN written above. If FAIL TOKEN or halt string appears, do not begin GROUP C.

Steps:
1. Produce TABLE F. Exactly two rows: Current State, Recommended State. Reference dominant pattern from PASS TOKEN. No org chart. No reporting lines.
2. Produce TABLE G. Close every TABLE A prediction: Confirmed / Disconfirmed / Insufficient Evidence. Cite TABLE B rows. If Likely in TABLE A but not evidenced, write "Disconfirmed -- evidence suggests [dictionary label]."
3. Write AREAS section. Name each area of work. Every area cites at least one TABLE B row. Anti-fabrication: no area without evidence.
4. Write TEAM SHAPE RECOMMENDATION. Reference TABLE F and TABLE G. Name dominant inertia pattern. State what current shape resists.

GROUP C exit condition: SYNTHESIS COMPLETE.
```

---

## V-03

**Variation axis**: Lifecycle emphasis -- maximum phase lifecycle ceremony. Four named phases: PHASE 0 (schema + dictionary), PHASE 1 (hypothesis), PHASE 2 (scan + gate), PHASE 3 (synthesis). Every phase boundary carries an explicit EXIT CONDITION block written at phase end and an explicit ENTRY CONDITION block verified before next phase begins. Ceremony is the structural spine.

**Hypothesis**: When every phase boundary requires both a written exit condition and a verified entry condition, hypothesis-first posture becomes structurally mandatory: PHASE 1 must write an exit condition before PHASE 2 entry is allowed, and that exit condition IS the control-transfer declaration -- making hypothesis formation a prerequisite for scan entry by lifecycle enforcement alone.

---

```
You are running org-scan for the Signal plugin.

CRITICAL CONSTRAINT (stated here; restated in output schema): This skill produces raw analysis only. No org chart. No reporting lines. No hierarchy diagrams. No "reports to" statements. No boxes-and-lines structure. Any org chart content is a failure of this skill regardless of how complete the other sections are.

---

PHASE 0: FRAMEWORK DECLARATION

Entry condition: Begin. This is the setup phase. No predictions. No scanning. No synthesis.

PHASE 0 task: Declare the analytical framework and output schema. No evidence-dependent work begins until PHASE 0 is complete.

---

INERTIA PATTERN DICTIONARY -- PRIMARY ANALYTICAL FRAMEWORK

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK for this skill. It is not a post-scan labeling tool. It is the analytical spine through which all evidence is interpreted. Apply it to form predictions before scanning (PHASE 1), verify predictions against evidence during scanning (PHASE 2), and resolve predictions during synthesis (PHASE 3). All Inertia Match values in TABLE B must use these labels exactly. Free text is structurally invalid -- unconstrained values make pattern comparison across runs unverifiable.

| # | Pattern Label | Description | Structural Tells | Behavioral Signals |
|---|---|---|---|---|
| 1 | Monolith | Single codebase, no service or namespace separation | Single package.json, flat root, no internal boundary imports | "Just put it in utils"; incidents affect unrelated features; teams can't describe their boundaries |
| 2 | Layered | Horizontal tiers drive directory structure | Directories named by tier; shared util/lib cross all features | "Which layer owns this?"; engineers identify by tier not product area; PRs cross layers frequently |
| 3 | Domain-clustered | Ownership domains drive directory and namespace structure | Feature dirs contain own schemas, routes, tests; cross-domain imports exceptional | Teams identify by domain; changes stay inside directories; cross-domain work needs explicit handoff |
| 4 | Conway-frozen | Org chart mirrored in code; team boundaries are code boundaries | Directory names match team names; test files scoped to team areas | "That's not my area"; changes require multi-team coordination; team handoffs visible in git log |
| 5 | Feature-team | Cross-cutting feature teams each own a slice end-to-end | Per-feature configs, flags; no single team owns infra exclusively | Teams identified by feature name; ship independently; cross-team ownership debates rare |
| 6 | Platform-product | Shared platform layer separate from product feature teams | platform/, infra/, shared/ distinct from product feature dirs | "Talk to platform"; product treats platform as dependency; platform has SLA expectations |
| 7 | Ambiguous | Insufficient evidence to classify; signals contradict or are absent | Mixed tells; no consistent directory convention | Ownership questions produce disagreement; no shared boundary language |

---

OUTPUT SCHEMA

This schema governs every table in this skill. Status applies to every column across all tables. Declared in PHASE 0 before any evidence-dependent phase begins.

CRITICAL CONSTRAINT (restated): No org chart. No reporting lines. No hierarchy. Raw analysis only.

TABLE A -- PATTERN HYPOTHESIS (PHASE 1 output)
| Column | Status | Vocabulary |
|---|---|---|
| Pattern Label | REQUIRED | Dictionary label exactly |
| Prior Assessment | REQUIRED | Likely / Unlikely / Unknown |
| Rationale | REQUIRED | Prior context only -- no scan evidence |
| Verification Target | REQUIRED | Source types to confirm or disconfirm |

TABLE B -- SCAN EVIDENCE (PHASE 2 output)
| Column | Status | Vocabulary |
|---|---|---|
| Finding | REQUIRED | One-sentence description |
| Source Type | REQUIRED | CLAUDE.md / package.json / design/ / namespace-structure / test-coverage / SPECS.md / .craft-roles |
| Inertia Match | REQUIRED | Dictionary label -- must precede File Path Evidence -- free text is a schema violation |
| File Path Evidence | REQUIRED | At least 1 concrete file path |
| Hypothesis Held | optional | yes / no / partial -- links to TABLE A row for matched pattern |

Column order rule: Inertia Match precedes File Path Evidence. Inverting the order is a schema violation.

TABLE C -- BOUNDARY CANDIDATES (PHASE 2 output)
| Column | Status | Vocabulary |
|---|---|---|
| Boundary | REQUIRED | Team or area split candidate |
| Seam Rationale | REQUIRED | Why this is a natural split -- not just a directory boundary |
| Evidence | REQUIRED | File path or source citation |
| Confidence | REQUIRED | High / Medium / Low |

TABLE D -- CROSS-CUTTING CONCERNS (PHASE 2 output)
| Column | Status | Vocabulary |
|---|---|---|
| Concern | REQUIRED | Named cross-cutting concern |
| Boundary Note | REQUIRED | Why this concern cannot be assigned to one team |
| Evidence | REQUIRED | File path or source citation |

TABLE E -- EVIDENCE GAPS (PHASE 2 output)
| Column | Status | Vocabulary |
|---|---|---|
| Gap | REQUIRED | Description of missing or ambiguous element |
| Gap Type | REQUIRED | source-absent / owner-unclear / scope-ambiguous / prediction-not-resolved |
| Impact | REQUIRED | What analysis is blocked |

TABLE F -- ORG SHAPE (PHASE 3 output)
| Column | Status | Vocabulary |
|---|---|---|
| State | REQUIRED | Current State / Recommended State |
| Shape | REQUIRED | Named org shape |
| Justification | REQUIRED | Reference dominant pattern from PASS TOKEN |

TABLE G -- PREDICTION RESOLUTION (PHASE 3 output)
| Column | Status | Vocabulary |
|---|---|---|
| Pattern Label | REQUIRED | From TABLE A |
| Prior Assessment | REQUIRED | From TABLE A |
| Evidence Verdict | REQUIRED | Confirmed / Disconfirmed / Insufficient Evidence |
| Resolution Note | REQUIRED | TABLE B citation(s) |

---

GATE TOKEN PROTOCOL

Defined in PHASE 0 before any evidence-dependent phase begins.

PASS TOKEN: "Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]"
FAIL TOKEN: "Path floor not met"

---

PHASE 0 EXIT CONDITION

Write the following exactly before PHASE 1 begins:

PHASE 0 COMPLETE -- framework and schema declared -- entering PHASE 1

---

PHASE 0 / PHASE 1 BOUNDARY

Entry condition for PHASE 1: "PHASE 0 COMPLETE -- framework and schema declared -- entering PHASE 1" written above. Do not begin PHASE 1 until that phrase appears.

---

PHASE 1: PATTERN HYPOTHESIS

Entry condition: PHASE 0 COMPLETE statement written above. Begin prediction work. No scanning. No file reading.

PHASE 1 task: Produce TABLE A. Apply the INERTIA PATTERN DICTIONARY -- PRIMARY ANALYTICAL FRAMEWORK to form predictions from prior context only.

Steps:
1. For each of the 7 dictionary patterns, assess: Likely / Unlikely / Unknown.
2. Populate TABLE A. All four columns required per row.
3. Produce at least 3 non-Unlikely assessments before writing the exit condition.

Anti-fabrication rule: TABLE A Rationale is prior context only. No scan evidence. Write "No prior context" and Unknown if none exists.

PHASE 1 EXIT CONDITION

Write the following exactly before PHASE 2 begins:

PREDICTION COMPLETE -- control transfers to SCANNER -- entering PHASE 2

---

PHASE 1 / PHASE 2 BOUNDARY

Entry condition for PHASE 2: "PREDICTION COMPLETE -- control transfers to SCANNER -- entering PHASE 2" written above. Do not begin PHASE 2 until that exact phrase appears. A missing exit condition is a phase lifecycle violation.

---

PHASE 2: EVIDENCE COLLECTION

Entry condition: PREDICTION COMPLETE statement written above.

SOURCE TYPES (scan at least 3 of 7):
1. CLAUDE.md files
2. package.json / manifest files
3. design/ directories
4. Namespace / directory structure
5. Test coverage areas
6. SPECS.md / specification files
7. Existing .craft/roles/ files

Steps:
1. Scan at least 3 source types. Populate TABLE B.
2. Collect at least 5 distinct file paths across TABLE B rows. The 5-path floor is a gate precondition. Record shortfalls in TABLE E (gap type: source-absent).
3. For each TABLE B row matching a TABLE A pattern, complete Hypothesis Held.
4. Populate TABLE C. Seam Rationale must name the natural split reason.
5. Populate TABLE D. Boundary Note must explain why the concern spans teams.
6. Populate TABLE E. For any TABLE A Verification Target not reached, add row with Gap Type: prediction-not-resolved.
7. Write headcount signal: "Estimated headcount: [X]-[Y]. Rationale: [2-3 sentences]."

Anti-fabrication rule: Every TABLE B row cites a real file path. Missing path = TABLE E, not TABLE B.

PHASE 2 EXIT CONDITION

Write the following exactly before gate evaluation:

SCAN COMPLETE -- control transfers to GATEKEEPER

---

PHASE 2 / PHASE 3 BOUNDARY: GATE EVALUATION

Entry condition for gate checklist: "SCAN COMPLETE -- control transfers to GATEKEEPER" written above. Do not evaluate the gate checklist until that exact phrase appears.

PHASE 2 postcondition (SCANNER confirms): TABLE B, C, D, E written. Headcount signal written.
PHASE 3 precondition (SYNTHESIZER requires): PASS TOKEN written below.
These two blocks name the same contract from both sides. Both must hold before PHASE 3 begins.

Evaluate each item in order; do not skip:

1. Source coverage: At least 3 source types scanned?
   -- Fails: Write "Source floor not met". Halt.
2. File path floor: At least 5 distinct file paths in TABLE B?
   -- Fails: Write FAIL TOKEN exactly. Halt. Do not begin PHASE 3.
3. Inertia Match: Every TABLE B row has a dictionary-constrained value?
   -- Fails: Write "Inertia Match not populated". Halt.
4. Column order: Inertia Match precedes File Path Evidence in every TABLE B row?
   -- Fails: Write "Column order violated". Halt.
5. TABLE A populated: At least 3 predictions from PHASE 1?
   -- Fails: Write "Prediction phase not completed". Halt.

If all pass: Write PASS TOKEN:
"Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]"

---

PHASE 3 entry condition: PASS TOKEN written above. If FAIL TOKEN or halt string appears, do not begin PHASE 3.

---

PHASE 3: SYNTHESIS

Entry condition: PASS TOKEN written above.

Steps:
1. Produce TABLE F. Exactly two rows: Current State, Recommended State. Reference dominant pattern from PASS TOKEN. No org chart. No reporting lines.
2. Produce TABLE G. Close every TABLE A prediction: Confirmed / Disconfirmed / Insufficient Evidence. Cite TABLE B rows. If Likely in TABLE A but not evidenced, write "Disconfirmed -- evidence suggests [pattern label]."
3. Write AREAS section. Every area cites at least one TABLE B row. Anti-fabrication: no area without evidence.
4. Write TEAM SHAPE RECOMMENDATION. Reference TABLE F and TABLE G. Name dominant inertia pattern.

PHASE 3 EXIT CONDITION

Write the following exactly:

PHASE 3 COMPLETE -- SYNTHESIS DONE
```

---

## V-04

**Variation axis**: Combination -- hypothesis-first phase architecture (C-39) + dictionary as primary analytical framework (C-40). The dictionary is declared PRIMARY ANALYTICAL FRAMEWORK at the very top and drives the PREDICTOR role, whose sole function is producing pattern predictions from the dictionary before any scanning. Three roles: PREDICTOR -> SCANNER -> SYNTHESIZER. Schema-first (TABLE A-G) before any role. Control-transfer declarations at every role boundary (C-36). Phase lifecycle ceremony (C-38) at every boundary.

**Hypothesis**: When the dictionary is declared PRIMARY ANALYTICAL FRAMEWORK before any other instruction, the PREDICTOR role becomes its natural first application: the agent's first act is to apply the framework to form predictions. The three-table chain (TABLE A predictions -> TABLE B Hypothesis Held -> TABLE G resolution) becomes structurally necessary -- making hypothesis testing the architectural driver of the entire phase sequence rather than a bolt-on tracking column.

---

```
You are running org-scan for the Signal plugin.

CRITICAL CONSTRAINT (stated here; restated in output schema): This skill produces raw analysis only. No org chart. No reporting lines. No hierarchy diagrams. No "reports to" statements. No boxes-and-lines structure. Any org chart content is a failure regardless of completeness elsewhere.

---

INERTIA PATTERN DICTIONARY -- PRIMARY ANALYTICAL FRAMEWORK

DECLARATION: The Inertia Pattern Dictionary is the PRIMARY ANALYTICAL FRAMEWORK for this skill. It is the analytical lens through which all evidence is interpreted from the first moment to the last.

Agent posture this skill requires: hypothesize from dictionary, then verify against evidence, then resolve. Not: scan, then label.

This declaration reorients every role:
- PREDICTOR applies this framework to produce named predictions before evidence collection.
- SCANNER verifies predictions against evidence, citing dictionary labels per row.
- SYNTHESIZER resolves every prediction against evidence, closing the hypothesis loop.

All Inertia Match values across all tables must use these labels exactly. Free text is structurally invalid -- unconstrained values make pattern comparison across runs unverifiable.

| # | Pattern Label | Description | Structural Tells | Behavioral Signals |
|---|---|---|---|---|
| 1 | Monolith | Single codebase, no service or namespace separation | Single package.json, flat root, no internal boundary imports | "Just put it in utils"; incidents affect unrelated features; teams can't describe their own scope |
| 2 | Layered | Horizontal tiers drive directory structure | Directories named by tier; shared util/lib cross all features | "Which layer owns this?"; engineers identify by tier not product area; PRs cross layers frequently |
| 3 | Domain-clustered | Ownership domains drive directory and namespace structure | Feature dirs with own schemas, routes, tests; cross-domain imports exceptional | Teams identify by domain; changes stay inside directories; cross-domain work requires handoff |
| 4 | Conway-frozen | Org chart mirrored in code; team boundaries are code boundaries | Directory names match team names; test files scoped to team areas | "That's not my area"; changes need multi-team coordination; team handoffs visible in git log |
| 5 | Feature-team | Cross-cutting feature teams each own a slice end-to-end | Per-feature configs, flags; no single team owns infra exclusively | Teams identified by feature name; ship independently; cross-team ownership debates rare |
| 6 | Platform-product | Shared platform layer separate from product feature teams | platform/, infra/, shared/ distinct from product feature dirs | "Talk to platform"; product treats platform as dependency; platform has SLA expectations |
| 7 | Ambiguous | Insufficient evidence to classify; signals contradict or absent | Mixed tells across source types; no consistent directory convention | Ownership questions produce disagreement; no shared boundary language |

---

OUTPUT SCHEMA

This schema governs every table in this skill. Status applies to every column across all tables. Declared before any role begins.

CRITICAL CONSTRAINT (restated): No org chart. No reporting lines. No hierarchy. Raw analysis only.

TABLE A -- PATTERN HYPOTHESIS (PREDICTOR output)
Purpose: Named predictions from the PRIMARY ANALYTICAL FRAMEWORK produced before any evidence collection.
| Column | Status | Vocabulary |
|---|---|---|
| Pattern Label | REQUIRED | Dictionary label exactly |
| Prior Assessment | REQUIRED | Likely / Unlikely / Unknown |
| Rationale | REQUIRED | Prior context only -- no scan evidence |
| Verification Target | REQUIRED | Source types that should confirm or disconfirm |
| Behavioral Prediction | optional | Behavioral signal expected if this pattern is present (from dictionary Behavioral Signals column) |

TABLE B -- SCAN EVIDENCE (SCANNER output)
Purpose: Repository findings. Inertia Match labels link each finding back to the PRIMARY ANALYTICAL FRAMEWORK.
| Column | Status | Vocabulary |
|---|---|---|
| Finding | REQUIRED | One-sentence description |
| Source Type | REQUIRED | CLAUDE.md / package.json / design/ / namespace-structure / test-coverage / SPECS.md / .craft-roles |
| Inertia Match | REQUIRED | Dictionary label exactly -- PRIMARY ANALYTICAL FRAMEWORK -- must precede File Path Evidence -- free text is a schema violation |
| File Path Evidence | REQUIRED | At least 1 concrete file path |
| Hypothesis Held | optional | yes / no / partial -- links this row to TABLE A prediction for matched pattern label |

Column order rule: Inertia Match precedes File Path Evidence in every TABLE B row. Inverting the order is a schema violation.

TABLE C -- BOUNDARY CANDIDATES (SCANNER output)
| Column | Status | Vocabulary |
|---|---|---|
| Boundary | REQUIRED | Team or area split candidate |
| Seam Rationale | REQUIRED | Why this is a natural split, not just a directory boundary |
| Evidence | REQUIRED | TABLE B row reference or file path |
| Confidence | REQUIRED | High / Medium / Low |

TABLE D -- CROSS-CUTTING CONCERNS (SCANNER output)
| Column | Status | Vocabulary |
|---|---|---|
| Concern | REQUIRED | Named cross-cutting concern |
| Boundary Note | REQUIRED | Why this concern cannot be assigned to one team |
| Evidence | REQUIRED | File path or source citation |

TABLE E -- EVIDENCE GAPS (SCANNER output)
| Column | Status | Vocabulary |
|---|---|---|
| Gap | REQUIRED | Description of missing or ambiguous element |
| Gap Type | REQUIRED | source-absent / owner-unclear / scope-ambiguous / prediction-not-resolved |
| Impact | REQUIRED | What analysis is blocked |

TABLE F -- ORG SHAPE (SYNTHESIZER output)
| Column | Status | Vocabulary |
|---|---|---|
| State | REQUIRED | Current State / Recommended State |
| Shape | REQUIRED | Named org shape -- frame using PRIMARY ANALYTICAL FRAMEWORK pattern label |
| Justification | REQUIRED | Reference dominant pattern from PASS TOKEN |

TABLE G -- PREDICTION RESOLUTION (SYNTHESIZER output)
Purpose: Explicit closure of every TABLE A prediction. Completes the three-table hypothesis loop: TABLE A -> TABLE B -> TABLE G.
| Column | Status | Vocabulary |
|---|---|---|
| Pattern Label | REQUIRED | From TABLE A -- PRIMARY ANALYTICAL FRAMEWORK label |
| Prior Assessment | REQUIRED | From TABLE A |
| Evidence Verdict | REQUIRED | Confirmed / Disconfirmed / Insufficient Evidence |
| Resolution Note | REQUIRED | TABLE B citation(s) resolving or failing to resolve the prediction |

---

GATE TOKEN PROTOCOL

Both tokens defined here as named constants before PREDICTOR begins.

PASS TOKEN: "Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]"
FAIL TOKEN: "Path floor not met"

---

ROLE SEQUENCE: PREDICTOR -> SCANNER -> SYNTHESIZER

You occupy exactly one role at a time. Complete all work in the current role before transitioning. Every role transition requires a named control-transfer declaration.

---

ROLE: PREDICTOR

Entry condition: PRIMARY ANALYTICAL FRAMEWORK declared. SCHEMA declared. GATE TOKEN PROTOCOL declared. Begin PREDICTOR work.

PREDICTOR mandate: Apply the INERTIA PATTERN DICTIONARY -- PRIMARY ANALYTICAL FRAMEWORK to form predictions before examining any evidence. The dictionary is your only analytical input in this phase. Do not read file paths. Do not open directories.

Steps:
1. For each of the 7 dictionary patterns, assess: Likely / Unlikely / Unknown. Use the Structural Tells and Behavioral Signals columns as prior-assessment vocabulary.
2. Populate TABLE A. All required columns per row. Optional: populate Behavioral Prediction for Likely patterns.
3. Produce at least 3 non-Unlikely assessments.

Anti-fabrication rule: TABLE A Rationale is prior context only. If no prior context for a pattern, write "No prior context" and Unknown. Do not invent rationale from hypothetical scan findings.

PREDICTOR exit condition. Write the following control-transfer declaration exactly:

PREDICTION COMPLETE -- control transfers to SCANNER

Do not begin SCANNER work until this control-transfer declaration appears above.

---

PREDICTOR / SCANNER BOUNDARY

Entry condition for SCANNER: "PREDICTION COMPLETE -- control transfers to SCANNER" written above. A missing control-transfer declaration is a role boundary violation -- the PREDICTOR has not handed off. Do not begin SCANNER work until that exact phrase appears.

---

ROLE: SCANNER

Entry condition: PREDICTION COMPLETE declaration written above.

SOURCE TYPES (scan at least 3 of 7):
1. CLAUDE.md files
2. package.json / manifest files
3. design/ directories
4. Namespace / directory structure
5. Test coverage areas
6. SPECS.md / specification files
7. Existing .craft/roles/ files

Steps:
1. Scan at least 3 source types. Populate TABLE B. For every finding, Inertia Match label is drawn from the PRIMARY ANALYTICAL FRAMEWORK -- the same dictionary PREDICTOR applied.
2. Collect at least 5 distinct file paths across TABLE B rows. 5-path floor is a gate precondition. Record shortfalls in TABLE E (source-absent).
3. For each TABLE B row whose Inertia Match label matches a TABLE A prediction, complete Hypothesis Held.
4. Populate TABLE C. Every Seam Rationale explains the natural split reason, not just the directory boundary.
5. Populate TABLE D. Every Boundary Note explains why the concern spans teams.
6. Populate TABLE E. For any TABLE A Verification Target not reached, add row with Gap Type: prediction-not-resolved.
7. Write headcount signal: "Estimated headcount: [X]-[Y]. Rationale: [2-3 sentences]."

Anti-fabrication rule: Every TABLE B row cites a real file path. Missing path = TABLE E entry, not TABLE B row.

SCANNER exit condition. Write the following control-transfer declaration exactly:

SCAN COMPLETE -- control transfers to GATEKEEPER

Do not begin gate evaluation until this control-transfer declaration appears above.

---

SCANNER / SYNTHESIZER BOUNDARY: GATE EVALUATION

Entry condition for gate checklist: "SCAN COMPLETE -- control transfers to GATEKEEPER" written above. Hard sequencing gate -- SYNTHESIZER cannot begin until PASS TOKEN is written. Gate entry failure is equivalent to a control-transfer failure between SCANNER and the gate.

SCANNER postcondition (PHASE 2 output confirmed): TABLE B, TABLE C, TABLE D, TABLE E written. Headcount signal written.
SYNTHESIZER precondition (PHASE 3 input verified): PASS TOKEN present below.
These two blocks name the same contract from both sides. Both must hold before SYNTHESIZER begins.

Evaluate each item in order; do not skip:

1. Source coverage: At least 3 source types scanned?
   -- Fails: Write "Source floor not met". Halt.
2. File path floor: At least 5 distinct file paths in TABLE B?
   -- Fails: Write FAIL TOKEN exactly. Halt. Do not begin SYNTHESIZER.
3. Inertia Match: Every TABLE B row has a dictionary-constrained value from the PRIMARY ANALYTICAL FRAMEWORK?
   -- Fails: Write "Inertia Match not populated". Halt.
4. Column order: Inertia Match precedes File Path Evidence in every TABLE B row?
   -- Fails: Write "Column order violated". Halt.
5. TABLE A predictions: At least 3 predictions in TABLE A from PREDICTOR?
   -- Fails: Write "Prediction phase not completed". Halt.

If all pass: Write PASS TOKEN:
"Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]"

SYNTHESIZER entry condition: PASS TOKEN written above.

---

ROLE: SYNTHESIZER

Entry condition: PASS TOKEN written above.

SYNTHESIZER mandate: Close the hypothesis loop opened by PREDICTOR and threaded through SCANNER. Every TABLE A prediction must be resolved in TABLE G. The PRIMARY ANALYTICAL FRAMEWORK is the common vocabulary across all three roles.

Steps:
1. Produce TABLE G (PREDICTION RESOLUTION). For every TABLE A row: Evidence Verdict + Resolution Note citing TABLE B row(s). If Likely in TABLE A but not evidenced, write "Disconfirmed -- evidence suggests [alternative dictionary label]." This closes the three-phase hypothesis loop.
2. Produce TABLE F (ORG SHAPE). Two rows: Current State, Recommended State. Reference dominant pattern from PASS TOKEN. Frame using PRIMARY ANALYTICAL FRAMEWORK vocabulary. No org chart. No reporting lines.
3. Write AREAS section. Every area cites at least one TABLE B row. Anti-fabrication: no area without evidence.
4. Write TEAM SHAPE RECOMMENDATION. Reference TABLE F and TABLE G. Name dominant inertia pattern. State what current shape resists and what recommended shape must overcome.

SYNTHESIZER exit condition: SYNTHESIS COMPLETE.
```

---

## V-05

**Variation axis**: Full integration -- all C-36 through C-40 structurally present in the tightest imperative register achievable. Preamble has four named blocks: (1) dictionary + PRIMARY ANALYTICAL FRAMEWORK declaration, (2) schema A-G, (3) gate tokens, (4) role sequence + control-transfer protocol. Every sentence is a command. No prose preamble. No transitional language.

**Hypothesis**: When all five new criteria are architecturally integrated into named preamble blocks (not appended to individual phase instructions), the prompt achieves maximum structural density with minimum redundancy: dictionary-as-primary-framework and schema-first are preamble blocks visible before any instruction, control-transfer protocol is a named block before roles begin, and phase lifecycle ceremony falls out of the imperative command structure at each boundary without requiring verbose ceremony language.

---

```
You are running org-scan for the Signal plugin.

CRITICAL CONSTRAINT (stated here; restated in output schema): Raw analysis only. No org chart. No reporting lines. No hierarchy. No "reports to" statements. Org chart content is a failure regardless of completeness elsewhere.

---

BLOCK 1 -- PRIMARY ANALYTICAL FRAMEWORK

INERTIA PATTERN DICTIONARY -- PRIMARY ANALYTICAL FRAMEWORK

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK for this skill. Posture: hypothesize from dictionary before scanning; verify against evidence during scanning; resolve predictions during synthesis. Apply in that order. Every Inertia Match value across all tables must use these labels exactly. Free text is a schema violation -- unconstrained values make pattern comparison across runs unverifiable.

| # | Pattern Label | Description | Structural Tells | Behavioral Signals |
|---|---|---|---|---|
| 1 | Monolith | Single codebase, no separation | Single package.json, flat root, no boundary imports | "Just put it in utils"; incidents affect unrelated features; teams can't describe their scope |
| 2 | Layered | Horizontal tiers drive directory structure | Directories named by tier; shared util/lib cross all features | "Which layer owns this?"; engineers identify by tier; PRs cross layers frequently |
| 3 | Domain-clustered | Ownership domains drive directory and namespace structure | Feature dirs own schemas, routes, tests | Teams identify by domain; changes stay inside directories; cross-domain work needs handoff |
| 4 | Conway-frozen | Org chart mirrored in code | Directory names match team names; test files scoped to team areas | "That's not my area"; changes need multi-team coordination |
| 5 | Feature-team | Cross-cutting feature teams own end-to-end slices | Per-feature configs, flags; no single team owns infra | Teams identified by feature name; ship independently |
| 6 | Platform-product | Shared platform layer separate from product teams | platform/, infra/, shared/ distinct from product feature dirs | "Talk to platform"; product treats platform as dependency |
| 7 | Ambiguous | Insufficient evidence; signals contradict or absent | Mixed tells; no consistent directory convention | Ownership questions produce disagreement |

---

BLOCK 2 -- OUTPUT SCHEMA

All tables defined here before any role instruction begins. Every instruction references a pre-declared table by letter. This schema governs every table in this skill. Status applies to every column across all tables.

CRITICAL CONSTRAINT (restated): No org chart. No reporting lines. No hierarchy. Raw analysis only.

TABLE A -- PATTERN HYPOTHESIS
| Column | Status | Vocabulary |
|---|---|---|
| Pattern Label | REQUIRED | Dictionary label exactly |
| Prior Assessment | REQUIRED | Likely / Unlikely / Unknown |
| Rationale | REQUIRED | Prior context only -- no scan evidence |
| Verification Target | REQUIRED | Source types to confirm or disconfirm |

TABLE B -- SCAN EVIDENCE
| Column | Status | Vocabulary |
|---|---|---|
| Finding | REQUIRED | One sentence |
| Source Type | REQUIRED | CLAUDE.md / package.json / design/ / namespace-structure / test-coverage / SPECS.md / .craft-roles |
| Inertia Match | REQUIRED | Dictionary label -- must precede File Path Evidence -- free text is a schema violation |
| File Path Evidence | REQUIRED | At least 1 concrete file path |
| Hypothesis Held | optional | yes / no / partial -- links to TABLE A prediction for matched label |

Column order: Inertia Match before File Path Evidence. Inverting is a schema violation.

TABLE C -- BOUNDARY CANDIDATES
| Column | Status | Vocabulary |
|---|---|---|
| Boundary | REQUIRED | Split candidate name |
| Seam Rationale | REQUIRED | Natural split reason -- not "a directory boundary exists" |
| Evidence | REQUIRED | File path or TABLE B row reference |
| Confidence | REQUIRED | High / Medium / Low |

TABLE D -- CROSS-CUTTING CONCERNS
| Column | Status | Vocabulary |
|---|---|---|
| Concern | REQUIRED | Named concern |
| Boundary Note | REQUIRED | Why it cannot be assigned to one team |
| Evidence | REQUIRED | File path or source citation |

TABLE E -- EVIDENCE GAPS
| Column | Status | Vocabulary |
|---|---|---|
| Gap | REQUIRED | What is missing or ambiguous |
| Gap Type | REQUIRED | source-absent / owner-unclear / scope-ambiguous / prediction-not-resolved |
| Impact | REQUIRED | What analysis is blocked |

TABLE F -- ORG SHAPE
| Column | Status | Vocabulary |
|---|---|---|
| State | REQUIRED | Current State / Recommended State |
| Shape | REQUIRED | Named org shape |
| Justification | REQUIRED | Reference dominant pattern from PASS TOKEN |

TABLE G -- PREDICTION RESOLUTION
| Column | Status | Vocabulary |
|---|---|---|
| Pattern Label | REQUIRED | From TABLE A |
| Prior Assessment | REQUIRED | From TABLE A |
| Evidence Verdict | REQUIRED | Confirmed / Disconfirmed / Insufficient Evidence |
| Resolution Note | REQUIRED | TABLE B citation(s) |

---

BLOCK 3 -- GATE TOKEN PROTOCOL

PASS TOKEN: "Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]"
FAIL TOKEN: "Path floor not met"

---

BLOCK 4 -- ROLE SEQUENCE AND CONTROL-TRANSFER PROTOCOL

ROLE SEQUENCE: PREDICTOR -> SCANNER -> GATEKEEPER -> SYNTHESIZER

Occupy exactly one role at a time. Complete all work before transitioning. Every role transition requires a named control-transfer declaration written at the end of the departing role. Entry condition of every role: the prior role's control-transfer declaration appears above. Missing declaration = role boundary violation.

---

ROLE: PREDICTOR

Entry condition: BLOCKS 1-4 declared. Begin.

Apply the PRIMARY ANALYTICAL FRAMEWORK to produce TABLE A before any scanning. Do not read files. Prior context only.

1. Assess each of the 7 dictionary patterns: Likely / Unlikely / Unknown.
2. Populate TABLE A. All four columns required.
3. At least 3 non-Unlikely assessments.

Anti-fabrication: TABLE A Rationale is prior context only. Unknown if no context.

Write:
PREDICTION COMPLETE -- control transfers to SCANNER

---

PREDICTOR / SCANNER BOUNDARY

Entry condition for SCANNER: "PREDICTION COMPLETE -- control transfers to SCANNER" written above. Missing = role boundary violation. Do not begin until it appears.

---

ROLE: SCANNER

Entry condition: PREDICTION COMPLETE declaration written above.

Source types (scan at least 3 of 7): CLAUDE.md / package.json / design/ / namespace-structure / test-coverage / SPECS.md / .craft-roles

1. Populate TABLE B. Inertia Match from PRIMARY ANALYTICAL FRAMEWORK only. At least 5 distinct file paths across rows. Shortfalls go to TABLE E (source-absent).
2. For TABLE B rows matching TABLE A patterns, complete Hypothesis Held.
3. Populate TABLE C. Every Seam Rationale names the natural split reason.
4. Populate TABLE D. Every Boundary Note explains why the concern spans teams.
5. Populate TABLE E. For any TABLE A Verification Target not reached, add row with Gap Type: prediction-not-resolved.
6. Write: "Estimated headcount: [X]-[Y]. Rationale: [2-3 sentences]."

Anti-fabrication: Every TABLE B row cites a real file path. Missing path = TABLE E, not TABLE B.

Write:
SCAN COMPLETE -- control transfers to GATEKEEPER

---

SCANNER / GATEKEEPER BOUNDARY: GATE EVALUATION

Entry condition: "SCAN COMPLETE -- control transfers to GATEKEEPER" written above. Gate entry failure = control-transfer failure. Hard gate. SYNTHESIZER cannot begin until PASS TOKEN is written.

SCANNER postcondition: TABLE B, C, D, E written. Headcount written.
SYNTHESIZER precondition: PASS TOKEN below.
These two blocks name the same contract from both sides. Both must hold before SYNTHESIZER begins.

Evaluate in order; do not skip:

1. Source coverage: At least 3 source types? -- Fails: "Source floor not met". Halt.
2. File path floor: At least 5 distinct paths in TABLE B? -- Fails: Write FAIL TOKEN. Halt. Do not begin SYNTHESIZER.
3. Inertia Match: Every TABLE B row has dictionary-constrained value? -- Fails: "Inertia Match not populated". Halt.
4. Column order: Inertia Match before File Path Evidence everywhere? -- Fails: "Column order violated". Halt.
5. TABLE A: At least 3 predictions from PREDICTOR? -- Fails: "Prediction phase not completed". Halt.

All pass: Write PASS TOKEN.

---

GATEKEEPER / SYNTHESIZER BOUNDARY

Entry condition for SYNTHESIZER: PASS TOKEN written above. FAIL TOKEN or halt = do not begin.

---

ROLE: SYNTHESIZER

Entry condition: PASS TOKEN written above.

1. Produce TABLE G. Close every TABLE A prediction: Confirmed / Disconfirmed / Insufficient Evidence. Cite TABLE B rows. Likely + no evidence = "Disconfirmed -- evidence suggests [label]."
2. Produce TABLE F. Two rows: Current State, Recommended State. Dominant pattern from PASS TOKEN. No org chart. No reporting lines.
3. Write AREAS. Every area cites at least one TABLE B row. Anti-fabrication: no area without evidence.
4. Write TEAM SHAPE RECOMMENDATION. Reference TABLE F and TABLE G. Name dominant pattern. State what current shape resists.

Write: SYNTHESIZER COMPLETE.
```
