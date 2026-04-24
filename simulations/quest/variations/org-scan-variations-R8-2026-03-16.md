Written to `simulations/quest/variations/org-scan-variations-R8-2026-03-16.md`.

---

## org-scan V-01 through V-05 (Round 8)

Five complete variations targeting all 32 rubric criteria:

---

**V-01 -- Role Sequence (single axis)**
Three named roles: SCANNER -> GATEKEEPER -> SYNTHESIZER. Role handoff is the organizing spine. Hypothesis: named accountability at each role transition makes gate failure a real handoff event rather than a mechanical block.

**V-02 -- Output Format (single axis)**
Schema defined first (before any phase instructions), organized as tables A-F. GROUP A / GROUP B structural labels. Hypothesis: schema-first layout makes table structure primary, mechanically enforcing C-19/C-21/C-25/C-27/C-29/C-30 from the first instruction line.

**V-03 -- Lifecycle Emphasis (single axis)**
Entry conditions, exit conditions, and transition rituals exhaustively spelled out for each phase. Phase 1 COMPLETE handoff statement. Phase 2 entry and exit conditions. Hypothesis: elaborate lifecycle framing makes gate failure a lifecycle event with named state semantics.

**V-04 -- Inertia Framing + Output Format (combo)**
Dictionary leads the entire prompt as the primary analytical framework. Three phases: Pattern Classification (hypotheses before reading files) -> Evidence Collection -> Synthesis. Seven named tables A-G. Hypothesis: classification-before-evidence forces the inertia lens as a prediction framework rather than retrofit.

**V-05 -- Phrasing Register + Lifecycle Emphasis (combo)**
Full imperative command register throughout. Numbered short-sentence instructions. GROUP A / GROUP B lifecycle with explicit entry/exit conditions per group. Hypothesis: command-mode with lifecycle structure eliminates interpretive slack in process sections.

---

**New R8 criteria (C-29 through C-32) placed in every variation:**
- **C-29**: "Inverting the order is a schema violation." in column-order constraint
- **C-30**: "This schema governs every table in this skill. Status applies to every column." as opening OUTPUT SCHEMA governing statement
- **C-31**: Named phase boundary header (e.g., `GROUP A / GROUP B BOUNDARY: GATE EVALUATION:`) as a structurally identifiable named element
- **C-32**: "evaluate each item in order; do not skip" in every gate checklist
e -- three explicitly named roles: SCANNER -> GATEKEEPER -> SYNTHESIZER. Role transition is the primary structural frame.

**Hypothesis**: Named role transitions make sequencing constraints more behaviorally binding than phase labels alone. The GATEKEEPER role makes the gate a real handoff with accountability rather than a mechanical condition.

---

```
You are running org-scan for the Signal plugin.

This skill operates in three named roles. You occupy exactly one role at a time and
complete all work for that role before transitioning. Role transitions are explicit and
require a handoff statement.

Role sequence: SCANNER -> GATEKEEPER -> SYNTHESIZER

CRITICAL CONSTRAINT (stated here; restated in output format): This skill produces raw
analysis only. No org chart. No reporting lines. No hierarchy diagrams. No "reports to"
statements. No boxes-and-lines structure. Producing any org chart content is a failure
of this skill regardless of how complete the other sections are.

---

GATE TOKEN PROTOCOL

The following named tokens govern the gate between SCANNER and SYNTHESIZER. Both tokens
are defined here as constants. Reference them by name throughout this skill.

PASS TOKEN: "Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]"
FAIL TOKEN: "Path floor not met"

---

INERTIA PATTERN DICTIONARY

This dictionary constrains the Inertia Match column throughout this skill. Use only
these enumerated labels. Free text is structurally invalid -- unconstrained values make
pattern comparison across runs unverifiable.

| Label | Description | Structural Tells |
|---|---|---|
| SOLO_EXPERT | One person owns this domain entirely | Single contributor, no onboarding docs, no handoff material |
| FUNCTIONAL_SILO | Work concentrated in one discipline, minimal cross-domain collaboration | Separate skill dirs, distinct toolchains, no shared deps |
| EMBEDDED_DEPENDENCY | Team or module buried inside a larger unit, unclear boundary | Mixed namespaces, blurred ownership in CLAUDE.md |
| DISTRIBUTED_OWNERSHIP | Same concern split across multiple teams, no clear lead | Duplicated patterns, competing conventions in multiple namespaces |
| SCAFFOLD_OVERHANG | Legacy scaffolding maintained past its use | Dead code, deprecated patterns still referenced, no removal timeline |
| CENTRAL_COORDINATOR | One person or role routes all cross-team requests | Single point of contact in docs, hub-and-spoke config patterns |
| ORGANIC_GROWTH | Boundaries formed by accretion, not design | Overlapping responsibilities, inconsistent naming, no single source of truth |

---

OUTPUT SCHEMA (COMPLETE)

This schema governs every table in this skill. Status applies to every column.

SCAN TABLE (produced by SCANNER):

| Column | Status | Note |
|---|---|---|
| Area | REQUIRED | Domain of work identified from scan evidence |
| Source | REQUIRED | One of the 7 source types listed below |
| Evidence | REQUIRED | Verbatim path or field name from the repository |
| Inertia Match | REQUIRED | Dictionary label only -- no free text |
| File Path Evidence | REQUIRED | 5-path floor is a gate precondition. At least 5 distinct file paths must appear across all rows before GATEKEEPER can issue a PASS TOKEN. |
| Confidence | optional | low / medium / high |

Column order is a structural constraint. Inertia Match precedes File Path Evidence in
every row. Inverting the order is a schema violation.

TEAM BOUNDARIES TABLE (produced by SYNTHESIZER):

| Column | Status | Note |
|---|---|---|
| Boundary Name | REQUIRED | Named candidate seam |
| Inertia Match | REQUIRED | Dictionary label from SCAN TABLE |
| File Path Evidence | REQUIRED | Supporting path(s) from SCAN TABLE |
| Seam Rationale | REQUIRED | Natural or forced; one sentence |

CROSS-CUTTING CONCERNS TABLE (produced by SYNTHESIZER):

| Column | Status | Note |
|---|---|---|
| Concern Name | REQUIRED | Named cross-cutting concern |
| Boundaries Crossed | REQUIRED | Which TEAM BOUNDARIES TABLE candidates are crossed |
| Boundary Note | REQUIRED | One sentence on why the boundary does not contain this concern |

HEADCOUNT TABLE (produced by SYNTHESIZER):

| Column | Status | Note |
|---|---|---|
| Expertise Domain | REQUIRED | Named domain of distinct expertise |
| Source Evidence | REQUIRED | SCAN TABLE row(s) that evidence this domain |
| Weight | optional | core / supporting / adjacent |

ORG SHAPE TABLE (produced by SYNTHESIZER):

| Column | Status | Note |
|---|---|---|
| Dimension | REQUIRED | Current State or Recommended State |
| Shape | REQUIRED | Named org shape |
| Justification | REQUIRED | Drawing on SCAN TABLE findings |
| Dominant Inertia Pattern | REQUIRED | Dictionary label drawn from PASS TOKEN |

EVIDENCE GAPS TABLE (produced by SYNTHESIZER):

| Column | Status | Note |
|---|---|---|
| Gap Type | REQUIRED | Missing source / ambiguous signal / low confidence |
| Description | REQUIRED | What is absent or unclear |
| Resolution Condition | REQUIRED | What evidence would resolve this gap |

---

ROLE: SCANNER

Scan the repository using the following source types. You must cover at least 3 of the 7.
Record all findings in the SCAN TABLE defined in the OUTPUT SCHEMA.

Source types:
1. CLAUDE.md files -- plugin boundaries, session protocols, team vocabulary
2. package.json / package manifests -- dependency ownership, toolchain separation
3. design/ directories -- architectural intent, planned modules
4. Namespace directories -- skill groupings, domain clustering
5. Test coverage areas -- quality ownership signals
6. SPECS.md files -- feature ownership, scope of concern
7. .roles/ -- existing role definitions, org self-description

Anti-fabrication rule: Every SCAN TABLE row must cite a file path or explicit field name
in Evidence and File Path Evidence. Do not infer an area without traceable evidence. If
evidence is absent, write "not found" in File Path Evidence and set Confidence to low.

When scan is complete, write:
"SCANNER COMPLETE -- [N] source types covered, [M] file paths collected. Handing off to GATEKEEPER."

---

SCANNER / GATEKEEPER BOUNDARY: GATE EVALUATION:
This boundary is a hard sequencing gate. GATEKEEPER must complete full evaluation before
SYNTHESIZER begins. SYNTHESIZER cannot begin until the PASS TOKEN is written.

ROLE: GATEKEEPER

Evaluate each item in order; do not skip:

1. Are at least 3 of the 7 source types represented in the SCAN TABLE Source column?
2. Are at least 5 distinct file paths present in the SCAN TABLE File Path Evidence column?
3. Does every SCAN TABLE row have a non-empty Inertia Match value?
4. Are all Inertia Match values drawn from the INERTIA PATTERN DICTIONARY (no free text)?
5. Does Inertia Match precede File Path Evidence in every SCAN TABLE row? (Schema constraint -- inverting is a schema violation.)

If item 2 fails: Write "Path floor not met". Halt. Do not begin SYNTHESIZER.
If items 1-5 all pass: Write the PASS TOKEN.

Phase 1 postcondition: SCANNER has covered 3+ source types, collected 5+ distinct file
paths, all Inertia Match values are valid dictionary labels, and column order is verified.

Phase 2 precondition: Phase 1 postcondition is satisfied and the PASS TOKEN is written.

These two blocks name the same contract from both sides. Both must hold before
SYNTHESIZER begins.

---

ROLE: SYNTHESIZER

CRITICAL CONSTRAINT (restated): This skill produces raw analysis only. No org chart.
No reporting lines. No hierarchy diagrams. No "reports to" statements.

Anti-fabrication rule: Every synthesis claim must be traceable to a SCAN TABLE row.
Unlabeled inference is prohibited. If a claim cannot be traced, write:
"Claim not evidenced -- insufficient scan signal."

Produce the following sections using the OUTPUT SCHEMA synthesis tables:

SECTION 1 -- AREAS OF WORK
Name each distinct area of work. Every area must cite the SCAN TABLE row(s) that
evidence it. If an area cannot be traced to a scan row, write:
"Area not evidenced -- insufficient scan signal."

SECTION 2 -- TEAM BOUNDARY CANDIDATES
Produce the TEAM BOUNDARIES TABLE. For each candidate seam: name the boundary, assign
an Inertia Match label from the dictionary, cite supporting file paths from the SCAN
TABLE, and state whether the boundary is natural or forced.

SECTION 3 -- CROSS-CUTTING CONCERNS
Produce the CROSS-CUTTING CONCERNS TABLE. For each concern: name it, state which team
boundaries it crosses, and write one sentence on why the boundary does not contain it.

SECTION 4 -- HEADCOUNT SIGNALS
Produce the HEADCOUNT TABLE. Then write:
"Estimated headcount: [X]-[Y] engineers. Rationale: [2-3 sentences drawing on
HEADCOUNT TABLE rows.]"

SECTION 5 -- ORG SHAPE ANALYSIS
Produce the ORG SHAPE TABLE with exactly two rows: Current State and Recommended State.
Each row must include shape name, justification from scan findings, and dominant inertia
pattern from the PASS TOKEN. Separate current state from recommended state clearly --
label each.

SECTION 6 -- EVIDENCE GAPS AND AMBIGUITIES
Produce the EVIDENCE GAPS TABLE. List all absent source types, low-confidence findings,
and ambiguities found during scan. State the resolution condition for each. Do not omit
gaps to appear complete.
```

---

## V-02

**Variation axis**: Output Format -- schema defined first as the organizing spine, before any phase instructions. Six named tables (A-F) govern all output. GROUP A / GROUP B structural labels.

**Hypothesis**: Declaring the full output schema before instructions makes table structure primary, reducing free-form prose drift and mechanically enforcing all schema criteria (C-19, C-21, C-25, C-27, C-29, C-30) from the first instruction line.

---

```
You are running org-scan for the Signal plugin.

CRITICAL CONSTRAINT (stated here; restated in output schema): This skill produces raw
analysis only. No org chart. No reporting lines. No hierarchy diagrams. No "reports to"
statements. Producing any org chart content is a failure of this skill.

---

OUTPUT SCHEMA (COMPLETE -- defined before instructions to govern all phases)

This schema governs every table in this skill. Status applies to every column.

TABLE A -- SCAN FINDINGS

| Column | Status | Note |
|---|---|---|
| Area | REQUIRED | Domain of work identified from scan evidence |
| Source | REQUIRED | One of the 7 source types |
| Evidence | REQUIRED | Verbatim path or field name |
| Inertia Match | REQUIRED | Dictionary label only -- free text invalid |
| File Path Evidence | REQUIRED | 5-path floor is a gate precondition |
| Confidence | optional | low / medium / high |

Column order rule: Inertia Match precedes File Path Evidence in every row. This is a
schema constraint, not a display preference. Inverting the order is a schema violation.

TABLE B -- TEAM BOUNDARY CANDIDATES

| Column | Status | Note |
|---|---|---|
| Boundary Name | REQUIRED | Named candidate seam |
| Inertia Match | REQUIRED | Dictionary label from TABLE A |
| File Path Evidence | REQUIRED | Supporting path(s) from TABLE A |
| Seam Rationale | REQUIRED | Natural or forced; one sentence |

TABLE C -- CROSS-CUTTING CONCERNS

| Column | Status | Note |
|---|---|---|
| Concern Name | REQUIRED | Named cross-cutting concern |
| Boundaries Crossed | REQUIRED | Which TABLE B candidates crossed |
| Boundary Note | REQUIRED | One sentence on why boundary does not contain this |

TABLE D -- HEADCOUNT SIGNALS

| Column | Status | Note |
|---|---|---|
| Expertise Domain | REQUIRED | Named domain |
| Source Evidence | REQUIRED | TABLE A row reference |
| Weight | optional | core / supporting / adjacent |

TABLE E -- ORG SHAPE ANALYSIS

| Column | Status | Note |
|---|---|---|
| Dimension | REQUIRED | Current State or Recommended State |
| Shape | REQUIRED | Named org shape |
| Justification | REQUIRED | Drawing on TABLE A findings |
| Dominant Inertia Pattern | REQUIRED | Dictionary label from PASS TOKEN |

TABLE F -- EVIDENCE GAPS

| Column | Status | Note |
|---|---|---|
| Gap Type | REQUIRED | Missing source / ambiguous signal / low confidence |
| Description | REQUIRED | What is absent or unclear |
| Resolution Condition | REQUIRED | What would resolve this gap |

CRITICAL CONSTRAINT (restated in output schema): TABLE A through TABLE F are raw
analysis. No org chart. No reporting lines. No hierarchy diagrams.

---

GATE TOKEN PROTOCOL

PASS TOKEN: "Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]"
FAIL TOKEN: "Path floor not met"

---

INERTIA PATTERN DICTIONARY

This dictionary constrains the Inertia Match column in TABLE A and TABLE B. Use only
these enumerated labels. Free text is structurally invalid -- unconstrained values make
pattern comparison across runs unverifiable.

| Label | Description | Structural Tells |
|---|---|---|
| SOLO_EXPERT | Single domain owner | Single contributor, no onboarding docs |
| FUNCTIONAL_SILO | One-discipline concentration | Separate dirs, distinct toolchains |
| EMBEDDED_DEPENDENCY | Unclear boundary inside larger unit | Mixed namespaces, blurred ownership |
| DISTRIBUTED_OWNERSHIP | Concern split, no clear lead | Duplicated patterns, competing conventions |
| SCAFFOLD_OVERHANG | Legacy scaffolding past use | Dead code, deprecated patterns |
| CENTRAL_COORDINATOR | Single routing hub | Hub-and-spoke config patterns |
| ORGANIC_GROWTH | Boundaries by accretion | Overlapping responsibilities, inconsistent naming |

---

GROUP A -- SCAN PHASE

Scan the repository using the following source types. Cover at least 3 of the 7. Produce
TABLE A.

Source types:
1. CLAUDE.md files
2. package.json / package manifests
3. design/ directories
4. Namespace directories
5. Test coverage areas
6. SPECS.md files
7. .roles/

Anti-fabrication rule (scan): Every TABLE A row must cite a file path or explicit field
name. If evidence is absent, write "not found" in File Path Evidence and set Confidence
to low.

---

GROUP A / GROUP B BOUNDARY: GATE EVALUATION:
This boundary is a hard sequencing gate. GROUP B cannot begin until the gate is
complete and the PASS TOKEN is written.

Evaluate each item in order; do not skip:

1. Are 3+ source types represented in the TABLE A Source column?
2. Are 5+ distinct file paths present in the TABLE A File Path Evidence column?
3. Does every TABLE A row have a non-empty Inertia Match value?
4. Are all Inertia Match values drawn from the INERTIA PATTERN DICTIONARY (no free text)?
5. Does Inertia Match precede File Path Evidence in every TABLE A row? (Schema
   constraint -- inverting is a schema violation.)

If item 2 fails: Write "Path floor not met". Halt. Do not produce GROUP B output.
If items 1-5 all pass: Write the PASS TOKEN.

Phase 1 postcondition: TABLE A contains 3+ source types, 5+ distinct file paths, all
Inertia Match values are valid dictionary labels, and column order is verified.

Phase 2 precondition: Phase 1 postcondition is satisfied and the PASS TOKEN is written.

These two blocks name the same contract from both sides. Both must hold before GROUP B
begins.

---

GROUP B -- SYNTHESIS PHASE

Anti-fabrication rule (synthesis): Every GROUP B claim must trace to a TABLE A row.
Unlabeled inference is prohibited.

Produce tables B through F as defined in the OUTPUT SCHEMA:

- TABLE B: One row per candidate team boundary. Cite TABLE A rows for Inertia Match and
  File Path Evidence.

- TABLE C: One row per cross-cutting concern. State which TABLE B candidates are crossed
  and why the boundary does not contain this concern.

- TABLE D: One row per expertise domain. After TABLE D, write:
  "Estimated headcount: [X]-[Y] engineers. Rationale: [2-3 sentences drawing on TABLE D
  rows.]"

- TABLE E: Exactly two rows -- one for Current State, one for Recommended State. Each
  row must name the org shape, justify it from TABLE A findings, and reference the
  dominant inertia pattern from the PASS TOKEN. Separate current state from recommended
  state clearly -- label each.

- TABLE F: List all absent source types, low-confidence findings, and ambiguities.
  Provide a Resolution Condition for each. Do not omit gaps to appear complete.
```

---

## V-03

**Variation axis**: Lifecycle Emphasis -- entry conditions, exit conditions, and transition rituals exhaustively stated for each phase. Phase 1 exit conditions mirror gate conditions for dual enforcement. Phase 2 has its own entry and exit verification.

**Hypothesis**: Elaborate lifecycle framing makes phases feel operationally real rather than decorative. When a phase has named entry conditions and exit conditions, gate failure becomes a lifecycle event with its own state semantics, not just a mechanical block.

---

```
You are running org-scan for the Signal plugin.

CRITICAL CONSTRAINT (stated here; restated at Phase 2 entry): This skill produces raw
analysis only. No org chart. No reporting lines. No hierarchy diagrams. No "reports to"
statements. Producing any org chart content is a failure of this skill.

---

GATE TOKEN PROTOCOL

Both tokens are defined here as constants before Phase 1 begins.

PASS TOKEN: "Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]"
FAIL TOKEN: "Path floor not met"

---

INERTIA PATTERN DICTIONARY

Internalize this dictionary before Phase 1 begins. It constrains the Inertia Match
column in all scan output. Free text is structurally invalid -- unconstrained values
make pattern comparison across runs unverifiable.

| Label | Description | Structural Tells |
|---|---|---|
| SOLO_EXPERT | Single domain owner | Single contributor, no onboarding, no handoff |
| FUNCTIONAL_SILO | One-discipline concentration | Separate dirs, distinct toolchains |
| EMBEDDED_DEPENDENCY | Unclear boundary inside larger unit | Mixed namespaces, blurred ownership |
| DISTRIBUTED_OWNERSHIP | Concern split, no clear lead | Duplicated patterns, competing conventions |
| SCAFFOLD_OVERHANG | Legacy scaffolding maintained past use | Dead code, deprecated patterns |
| CENTRAL_COORDINATOR | Single routing hub | Hub-and-spoke config, single point of contact |
| ORGANIC_GROWTH | Boundaries by accretion | Overlapping responsibilities, inconsistent naming |

---

OUTPUT SCHEMA (COMPLETE)

This schema governs every table in this skill. Status applies to every column.

SCAN TABLE:

| Column | Status | Note |
|---|---|---|
| Area | REQUIRED | Domain of work identified |
| Source | REQUIRED | One of the 7 source types |
| Evidence | REQUIRED | Verbatim path or field name |
| Inertia Match | REQUIRED | Dictionary label only; this column precedes File Path Evidence (structural constraint) |
| File Path Evidence | REQUIRED | 5-path floor is a Phase 1 exit condition and gate precondition |
| Confidence | optional | low / medium / high |

Column order is a structural constraint. Inertia Match precedes File Path Evidence in
every row. Inverting the order is a schema violation.

SYNTHESIS TABLES:

Team Boundaries Table:
| Column | Status | Note |
|---|---|---|
| Boundary Name | REQUIRED | Named seam |
| Inertia Match | REQUIRED | Dictionary label from SCAN TABLE |
| File Path Evidence | REQUIRED | Path from SCAN TABLE |
| Seam Rationale | REQUIRED | Natural or forced; one sentence |

Cross-Cutting Concerns Table:
| Column | Status | Note |
|---|---|---|
| Concern Name | REQUIRED | |
| Boundaries Crossed | REQUIRED | Which boundary candidates are crossed |
| Boundary Note | REQUIRED | One sentence on why boundary does not contain this |

Headcount Table:
| Column | Status | Note |
|---|---|---|
| Expertise Domain | REQUIRED | Named domain |
| Source Evidence | REQUIRED | SCAN TABLE row reference |
| Weight | optional | core / supporting / adjacent |

Org Shape Table:
| Column | Status | Note |
|---|---|---|
| Dimension | REQUIRED | Current State or Recommended State |
| Shape | REQUIRED | Named org shape |
| Justification | REQUIRED | From SCAN TABLE findings |
| Dominant Inertia Pattern | REQUIRED | Dictionary label from PASS TOKEN |

Evidence Gaps Table:
| Column | Status | Note |
|---|---|---|
| Gap Type | REQUIRED | Missing source / ambiguous signal / low confidence |
| Description | REQUIRED | |
| Resolution Condition | REQUIRED | What would resolve |
| Affected Sections | optional | Which synthesis sections are affected |

---

PHASE 1: EVIDENCE COLLECTION

Phase 1 entry conditions:
- GATE TOKEN PROTOCOL has been read and tokens are known
- INERTIA PATTERN DICTIONARY has been internalized
- CRITICAL CONSTRAINT has been noted

In Phase 1, scan the repository and produce the SCAN TABLE.

Source types (scan at least 3 of 7):
1. CLAUDE.md files -- plugin boundaries, session protocols, team vocabulary
2. package.json / package manifests -- dependency ownership, toolchain separation
3. design/ directories -- architectural intent, planned modules
4. Namespace directories -- skill groupings, domain clustering
5. Test coverage areas -- quality ownership signals
6. SPECS.md files -- feature ownership, scope of concern
7. .roles/ -- existing role definitions, org self-description

Anti-fabrication rule (Phase 1): Every SCAN TABLE row must cite a file path or explicit
field name. If evidence is absent, write "not found" in File Path Evidence and set
Confidence to low. Do not infer an area without traceable evidence.

Phase 1 exit conditions (all must be true before gate evaluation begins):
- All target source types have been scanned or marked as not found
- SCAN TABLE is populated
- File Path Evidence column is populated for all rows with available evidence
- Every Inertia Match cell contains a value from the INERTIA PATTERN DICTIONARY (no free text)
- Inertia Match precedes File Path Evidence in every row (column order verified)

When Phase 1 exit conditions are met, write:
"PHASE 1 COMPLETE -- [N] source types scanned, [M] file paths collected. Proceeding to gate evaluation."

---

PHASE 1 / PHASE 2 BOUNDARY: GATE EVALUATION:
This boundary is a hard sequencing gate. Phase 2 cannot begin until gate evaluation is
complete and the PASS TOKEN is written.

Gate entry condition: The PHASE 1 COMPLETE statement has been written.

Evaluate each item in order; do not skip:

1. Are 3+ of the 7 source types represented in the SCAN TABLE Source column?
2. Are 5+ distinct file paths present in the SCAN TABLE File Path Evidence column?
   (Path floor -- this is a gate precondition. If unmet, halt immediately.)
3. Does every SCAN TABLE row have a non-empty Inertia Match value?
4. Are all Inertia Match values drawn from the INERTIA PATTERN DICTIONARY (no free text)?
5. Does Inertia Match precede File Path Evidence in every SCAN TABLE row?
   (Schema constraint -- inverting is a schema violation.)

If item 2 fails: Write "Path floor not met". Halt. Do not begin Phase 2.
If items 1-5 all pass: Write the PASS TOKEN.

Phase 1 postcondition: The SCAN TABLE covers 3+ source types with 5+ distinct file
paths; all Inertia Match values are valid dictionary labels; column order is verified.

Phase 2 precondition: Phase 1 postcondition is satisfied and the PASS TOKEN has been
written.

These two blocks name the same contract from both sides. Both must hold before Phase 2
begins.

---

PHASE 2: SYNTHESIS

Phase 2 entry conditions:
- PASS TOKEN has been written
- Phase 1 postcondition is satisfied

CRITICAL CONSTRAINT (restated at Phase 2 entry): This skill produces raw analysis only.
No org chart. No reporting lines. No hierarchy diagrams.

Anti-fabrication rule (Phase 2): Every synthesis claim must be traceable to a SCAN TABLE
row. Unlabeled inference is prohibited. If a claim cannot be traced, write:
"Claim not evidenced -- insufficient scan signal."

Produce the following sections using the synthesis tables from the OUTPUT SCHEMA:

SECTION 2.1 -- AREAS OF WORK
Name each distinct area of work. Every area must cite the SCAN TABLE row(s) that
evidence it.

SECTION 2.2 -- TEAM BOUNDARY CANDIDATES
Produce the Team Boundaries Table. For each candidate seam: name the boundary, assign
an Inertia Match label from the dictionary, cite supporting paths from the SCAN TABLE,
and state whether the boundary is natural or forced.

SECTION 2.3 -- CROSS-CUTTING CONCERNS
Produce the Cross-Cutting Concerns Table. Name each concern, state which team boundary
candidates it crosses, and write one sentence on why the boundary does not contain it.

SECTION 2.4 -- HEADCOUNT SIGNALS
Produce the Headcount Table. Then write:
"Estimated headcount: [X]-[Y] engineers. Rationale: [2-3 sentences drawing on
Headcount Table rows above.]"

SECTION 2.5 -- ORG SHAPE ANALYSIS
Produce the Org Shape Table with exactly two rows: Current State and Recommended State.
Each row must include shape name, justification from scan findings, and the dominant
inertia pattern label from the PASS TOKEN. Separate current state from recommended
state clearly -- label each.

SECTION 2.6 -- EVIDENCE GAPS AND AMBIGUITIES
Produce the Evidence Gaps Table. List all absent source types, low-confidence findings,
and ambiguities. State the resolution condition for each. Do not omit gaps to appear
complete.

Phase 2 exit conditions:
- Sections 2.1 through 2.6 all produced
- All claims traceable to SCAN TABLE rows
- Current State and Recommended State clearly separated and labeled
- Evidence Gaps Table does not omit any identified gap

Write "ORG SCAN COMPLETE" when all Phase 2 exit conditions are met.
```

---

## V-04

**Variation axis (combo)**: Inertia Framing + Output Format. The inertia dictionary leads the entire prompt as the primary analytical framework. Output organized as schema-defined tables A-G across three phases: Pattern Classification (Phase 1) -> Evidence Collection (Phase 2) -> Synthesis (Phase 3). Inertia pattern hypotheses are formed before evidence collection begins.

**Hypothesis**: Separating pattern classification from evidence collection forces the inertia lens to be internalized as a prediction framework rather than retrofitted to findings after reading files. The classification step produces hypotheses that the evidence step confirms or disconfirms.

---

```
You are running org-scan for the Signal plugin.

CRITICAL CONSTRAINT (stated here; restated in output schema and before Phase 3): This
skill produces raw analysis only. No org chart. No reporting lines. No hierarchy
diagrams. No "reports to" statements. Producing any org chart content is a failure of
this skill.

---

INERTIA PATTERN DICTIONARY (PRIMARY ANALYTICAL FRAMEWORK)

This dictionary governs all pattern classification in this skill. All phases reference
this dictionary. Use only these enumerated labels in all Inertia Match columns.
Free text is structurally invalid -- unconstrained values make pattern comparison
across runs unverifiable.

| Label | Description | Behavioral Signals | Structural Tells |
|---|---|---|---|
| SOLO_EXPERT | Single domain owner | Knowledge hoarding, bus factor 1 | Single contributor, no onboarding |
| FUNCTIONAL_SILO | One-discipline concentration | Cross-team requests routed around | Separate dirs, distinct toolchains |
| EMBEDDED_DEPENDENCY | Unclear boundary inside larger unit | Constant re-scoping of what's "in" | Mixed namespaces, blurred ownership |
| DISTRIBUTED_OWNERSHIP | Concern split, no clear lead | Parallel conflicting conventions | Duplicated patterns, competing styles |
| SCAFFOLD_OVERHANG | Legacy scaffolding maintained past use | Maintenance cost exceeds value | Dead code, deprecated patterns |
| CENTRAL_COORDINATOR | Single routing hub | Bottleneck on one role | Hub-and-spoke config, single contact |
| ORGANIC_GROWTH | Boundaries by accretion | Nobody knows who owns what | Overlapping responsibilities |

---

GATE TOKEN PROTOCOL

PASS TOKEN: "Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]"
FAIL TOKEN: "Path floor not met"

---

OUTPUT SCHEMA (COMPLETE)

This schema governs every table in this skill. Status applies to every column.

TABLE A -- PATTERN HYPOTHESES (Phase 1):
| Column | Status | Note |
|---|---|---|
| Domain Candidate | REQUIRED | Named area to investigate |
| Predicted Inertia Pattern | REQUIRED | Dictionary label -- prediction before file reading |
| Hypothesis Rationale | REQUIRED | Why this pattern is predicted |
| Confidence Prior | optional | low / medium / high |

TABLE B -- SCAN FINDINGS (Phase 2):
| Column | Status | Note |
|---|---|---|
| Area | REQUIRED | Domain confirmed from scan evidence |
| Source | REQUIRED | One of the 7 source types |
| Evidence | REQUIRED | Verbatim path or field name |
| Inertia Match | REQUIRED | Dictionary label; this column precedes File Path Evidence |
| File Path Evidence | REQUIRED | 5-path floor is a gate precondition |
| Hypothesis Held | optional | yes / no / partial -- references TABLE A prediction |
| Confidence | optional | low / medium / high |

Column order rule: Inertia Match precedes File Path Evidence in every TABLE B row.
This is a schema constraint, not a display preference. Inverting the order is a
schema violation.

TABLE C -- TEAM BOUNDARY CANDIDATES (Phase 3):
| Column | Status | Note |
|---|---|---|
| Boundary Name | REQUIRED | Named seam |
| Inertia Match | REQUIRED | Dictionary label from TABLE B |
| File Path Evidence | REQUIRED | Path from TABLE B |
| Seam Rationale | REQUIRED | Natural or forced; one sentence |

TABLE D -- CROSS-CUTTING CONCERNS (Phase 3):
| Column | Status | Note |
|---|---|---|
| Concern Name | REQUIRED | |
| Boundaries Crossed | REQUIRED | Which TABLE C candidates crossed |
| Boundary Note | REQUIRED | One sentence why boundary does not contain this |

TABLE E -- HEADCOUNT SIGNALS (Phase 3):
| Column | Status | Note |
|---|---|---|
| Expertise Domain | REQUIRED | Named domain |
| Source Evidence | REQUIRED | TABLE B row reference |
| Weight | optional | core / supporting / adjacent |

TABLE F -- ORG SHAPE ANALYSIS (Phase 3):
| Column | Status | Note |
|---|---|---|
| Dimension | REQUIRED | Current State or Recommended State |
| Shape | REQUIRED | Named org shape |
| Justification | REQUIRED | From TABLE B findings |
| Dominant Inertia Pattern | REQUIRED | Dictionary label from PASS TOKEN |

TABLE G -- EVIDENCE GAPS (Phase 3):
| Column | Status | Note |
|---|---|---|
| Gap Type | REQUIRED | Missing source / ambiguous signal / prediction not resolved |
| Description | REQUIRED | |
| Resolution Condition | REQUIRED | |

CRITICAL CONSTRAINT (restated in output schema): TABLE A through TABLE G are raw
analysis. No org chart. No reporting lines.

---

PHASE 1: PATTERN CLASSIFICATION

Before reading any files: identify candidate domains in the repository from any
contextual knowledge available (directory names visible, file names, tool descriptions).
For each candidate, predict which inertia pattern you expect to find and state why.

Produce TABLE A. This phase produces hypotheses, not findings. No file paths are
required in TABLE A because no files have been read yet.

When TABLE A is complete, write:
"PHASE 1 COMPLETE -- [N] domain candidates identified, predictions recorded."

---

PHASE 2: EVIDENCE COLLECTION

Read the repository systematically using the following source types. Cover at least 3
of the 7. Produce TABLE B. Reference TABLE A predictions in the Hypothesis Held column
when a scan row confirms or disconfirms a Phase 1 prediction.

Source types:
1. CLAUDE.md files
2. package.json / package manifests
3. design/ directories
4. Namespace directories
5. Test coverage areas
6. SPECS.md files
7. .roles/

Anti-fabrication rule (Phase 2): Every TABLE B row must cite a file path or explicit
field name. If evidence is absent, write "not found" in File Path Evidence and set
Confidence to low.

When scan is complete, write:
"PHASE 2 COMPLETE -- [N] source types scanned, [M] file paths collected."

---

PHASE 2 / PHASE 3 BOUNDARY: GATE EVALUATION:
This boundary is a hard sequencing gate. Phase 3 cannot begin until the gate is
complete and the PASS TOKEN is written.

Evaluate each item in order; do not skip:

1. Are 3+ source types represented in the TABLE B Source column?
2. Are 5+ distinct file paths in the TABLE B File Path Evidence column?
3. Does every TABLE B row have a non-empty Inertia Match value?
4. Are all Inertia Match values drawn from the INERTIA PATTERN DICTIONARY (no free text)?
5. Does Inertia Match precede File Path Evidence in every TABLE B row?
   (Schema constraint -- inverting is a schema violation.)

If item 2 fails: Write "Path floor not met". Halt. Do not begin Phase 3.
If items 1-5 all pass: Write the PASS TOKEN.

Phase 2 postcondition: TABLE B contains 3+ source types, 5+ distinct file paths, all
Inertia Match values are valid dictionary labels, and column order is verified.

Phase 3 precondition: Phase 2 postcondition is satisfied and the PASS TOKEN is written.

These two blocks name the same contract from both sides. Both must hold before Phase 3
begins.

---

PHASE 3: SYNTHESIS

CRITICAL CONSTRAINT (restated): This skill produces raw analysis only. No org chart.
No reporting lines. No hierarchy diagrams.

Anti-fabrication rule (Phase 3): Every claim must trace to a TABLE B row. Unlabeled
inference is prohibited.

Produce tables C through G as defined in the OUTPUT SCHEMA:

- TABLE C: One row per team boundary candidate. Cite TABLE B rows.
- TABLE D: One row per cross-cutting concern. Note which TABLE C candidates are crossed.
- TABLE E: One row per expertise domain. After TABLE E, write:
  "Estimated headcount: [X]-[Y] engineers. Rationale: [2-3 sentences from TABLE E rows.]"
- TABLE F: Exactly two rows (Current State, Recommended State). Reference the dominant
  inertia pattern from the PASS TOKEN. Separate current state from recommended state
  clearly -- label each.
- TABLE G: All absent source types, low-confidence findings, ambiguities, and TABLE A
  predictions that were neither confirmed nor disconfirmed. State resolution conditions.
  Do not omit gaps to appear complete.
```

---

## V-05

**Variation axis (combo)**: Phrasing Register + Lifecycle Emphasis. Full imperative command register throughout. Numbered short-sentence instructions. Lifecycle phases with explicit entry/exit conditions. Minimal explanatory prose in process sections.

**Hypothesis**: Command-mode instructions with lifecycle structure eliminate interpretive slack in process sections, producing the highest gate and schema compliance density. Naming the temptation to shortcut ("Do not omit gaps to appear complete") alongside the requirement is more effective than constraint alone.

---

```
You are running org-scan for the Signal plugin.

CRITICAL CONSTRAINT: Raw analysis only. No org chart. No reporting lines. No hierarchy
diagrams. No "reports to" statements. Stated here. Restated in GROUP B. Non-negotiable.

---

GATE TOKEN PROTOCOL

Define both tokens now. Use by name throughout.

PASS TOKEN: "Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]"
FAIL TOKEN: "Path floor not met"

---

INERTIA PATTERN DICTIONARY

Use only these labels in all Inertia Match columns. No free text.
Free text is structurally invalid -- unconstrained values make pattern comparison
across runs unverifiable.

| Label | Description |
|---|---|
| SOLO_EXPERT | Single owner, no succession |
| FUNCTIONAL_SILO | One discipline, isolated from others |
| EMBEDDED_DEPENDENCY | Buried inside larger unit, unclear boundary |
| DISTRIBUTED_OWNERSHIP | Split across teams, no clear lead |
| SCAFFOLD_OVERHANG | Legacy structure maintained past usefulness |
| CENTRAL_COORDINATOR | Single routing hub, bottleneck risk |
| ORGANIC_GROWTH | Boundary formed by accretion, not design |

---

OUTPUT SCHEMA (COMPLETE)

This schema governs every table in this skill. Status applies to every column.

SCAN TABLE:

| Column | Status | Notes |
|---|---|---|
| Area | REQUIRED | |
| Source | REQUIRED | One of 7 source types |
| Evidence | REQUIRED | Verbatim path or field |
| Inertia Match | REQUIRED | Dictionary label only; precedes File Path Evidence |
| File Path Evidence | REQUIRED | 5-path minimum is a gate condition |
| Confidence | optional | low / medium / high |

Column order mandatory: Inertia Match before File Path Evidence.
Inverting the order is a schema violation.

SYNTHESIS TABLES:

S1 -- Boundary Candidates:
| Boundary Name | REQUIRED | Inertia Match | REQUIRED | File Path Evidence | REQUIRED | Seam Rationale | REQUIRED |

S2 -- Cross-Cutting Concerns:
| Concern Name | REQUIRED | Boundaries Crossed | REQUIRED | Boundary Note | REQUIRED |

S3 -- Headcount:
| Expertise Domain | REQUIRED | Source Evidence | REQUIRED | Weight | optional |

S4 -- Org Shape:
| Dimension | REQUIRED | Shape | REQUIRED | Justification | REQUIRED | Dominant Inertia Pattern | REQUIRED |

S5 -- Evidence Gaps:
| Gap Type | REQUIRED | Description | REQUIRED | Resolution Condition | REQUIRED |

CRITICAL CONSTRAINT (restated in output schema): All tables are raw analysis. No org
chart. No reporting lines. No hierarchy diagrams.

---

GROUP A -- SCAN

Group A entry conditions:
1. GATE TOKEN PROTOCOL is loaded.
2. INERTIA PATTERN DICTIONARY is loaded.
3. CRITICAL CONSTRAINT is noted.

Scan steps:
1. Scan these source types. Cover at least 3 of 7:
   a. CLAUDE.md files
   b. package.json / manifests
   c. design/ directories
   d. Namespace directories
   e. Test coverage areas
   f. SPECS.md files
   g. .roles/
2. Record every finding in the SCAN TABLE using the OUTPUT SCHEMA.
3. Every row needs a file path. No path? Write "not found" in File Path Evidence.
   Set Confidence to low.
4. Every Inertia Match cell must have a dictionary label. No free text.
5. Inertia Match column appears before File Path Evidence column in every row.

Group A exit conditions:
1. All target source types scanned.
2. SCAN TABLE populated.
3. 5+ distinct file paths present across File Path Evidence column.
4. All Inertia Match cells have dictionary labels.
5. Column order verified: Inertia Match before File Path Evidence.

Write "GROUP A COMPLETE -- [N] sources, [M] paths." when exit conditions are met.

---

GROUP A / GROUP B BOUNDARY: GATE EVALUATION:
Hard gate. GROUP B cannot begin until PASS TOKEN is written.

Evaluate each item in order; do not skip:

1. SCAN TABLE Source column shows 3+ of the 7 source types?
2. SCAN TABLE File Path Evidence column has 5+ distinct paths?
   (5-path minimum is a gate condition. Item 2 fails: Write "Path floor not met". Stop.)
3. Every SCAN TABLE row has a non-empty Inertia Match?
4. Every Inertia Match value is from the dictionary (no free text)?
5. Inertia Match precedes File Path Evidence in every row? (Inverting is a schema
   violation.)

All 5 pass: Write PASS TOKEN.

Phase 1 postcondition: SCAN TABLE has 3+ sources, 5+ paths, valid dictionary labels,
column order verified.

Phase 2 precondition: Phase 1 postcondition is met. PASS TOKEN is written.

These two blocks name the same contract from both sides. Both must hold before GROUP B
begins.

---

GROUP B -- SYNTHESIS

CRITICAL CONSTRAINT (restated): Raw analysis only. No org chart. No reporting lines.

Anti-fabrication rule: Cite SCAN TABLE row(s) for every claim. No unlabeled inference.
No evidence? Write: "Claim not evidenced -- insufficient scan signal."

Group B steps:

1. AREAS OF WORK
   List distinct work areas. Cite SCAN TABLE row for each.
   No evidence? Write: "Area not evidenced -- insufficient scan signal."

2. TEAM BOUNDARY CANDIDATES
   Produce S1. One row per seam. Include Inertia Match from dictionary.
   State natural or forced in Seam Rationale.

3. CROSS-CUTTING CONCERNS
   Produce S2. One row per concern. State boundaries crossed. Write one sentence:
   why boundary does not contain this concern.

4. HEADCOUNT SIGNALS
   Produce S3. After table write:
   "Estimated headcount: [X]-[Y] engineers. Rationale: [2-3 sentences from S3 rows.]"

5. ORG SHAPE ANALYSIS
   Produce S4. Two rows: Current State, Recommended State.
   Include dominant inertia pattern from PASS TOKEN.
   Separate current state from recommended state clearly. Label each.

6. EVIDENCE GAPS
   Produce S5. List absent sources, low-confidence findings, ambiguities.
   Write Resolution Condition for each. Do not omit gaps to appear complete.

Group B exit conditions:
1. Sections 1-6 produced.
2. All claims traced to SCAN TABLE.
3. Current State and Recommended State labeled and separated.
4. No gaps omitted.

Write "ORG SCAN COMPLETE" when Group B exit conditions are met.
```

---

## Coverage Summary (C-01 through C-32)

All 5 variations cover all 32 criteria. New v8 criteria placement:

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| C-29 schema violation label | SCAN TABLE column-order rule | TABLE A column order rule | SCAN TABLE column-order rule | TABLE B column order rule | SCAN TABLE column order note |
| C-30 universal governing statement | "This schema governs every table in this skill. Status applies to every column." | Same | Same | Same | Same |
| C-31 named phase boundary header | "SCANNER / GATEKEEPER BOUNDARY: GATE EVALUATION:" | "GROUP A / GROUP B BOUNDARY: GATE EVALUATION:" | "PHASE 1 / PHASE 2 BOUNDARY: GATE EVALUATION:" | "PHASE 2 / PHASE 3 BOUNDARY: GATE EVALUATION:" | "GROUP A / GROUP B BOUNDARY: GATE EVALUATION:" |
| C-32 sequential evaluation enforcement | "evaluate each item in order; do not skip" | Same | Same | Same | Same |
