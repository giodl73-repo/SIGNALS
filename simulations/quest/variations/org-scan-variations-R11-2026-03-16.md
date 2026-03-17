Written to `simulations/quest/variations/org-scan-variations-R11-2026-03-16.md`.

---

## R11 — org-scan — 5 Variations

All R10 criteria (C-01 through C-40) are preserved. Each variation adds C-41 through C-44.

### Variation Axes

| Variation | Axis | C-41 Hypothesis |
|---|---|---|
| **V-01** | Named boundary at every phase transition | PHASE N / PHASE N+1 BOUNDARY: header sits above BOTH exit and entry blocks at all 3 transitions — distinguishes C-41 from C-31's gate-only placement |
| **V-02** | SCHEMA DECLARATION as first named block | Schema appears before framework declaration — making output contract the anchor before any posture statement, strongest C-42 form |
| **V-03** | Analytical arc with role assignments | Framework declaration names "from prediction (PREDICTOR) through verification (SCANNER) through synthesis (SYNTHESIZER)" — extends C-40 from posture to phase-role binding |
| **V-04** | TABLE G purpose + named boundaries | C-43: TABLE G "Sole structural purpose:" + three-table loop (TABLE A → TABLE B → TABLE G) named in purpose block; combined with C-41 boundary headers |
| **V-05** | Full integration, tight register | All 4 new criteria in BLOCK 1/2/3/4 preamble — C-44 in BLOCK 1, C-42 as BLOCK 2 label, C-43 in TABLE G, C-41 at every boundary |

### Structural Invariants Across All 5

- **C-41**: Named boundary section header above both exit and entry blocks at every phase transition (3 transitions covered)
- **C-42**: `SCHEMA DECLARATION` as a named block header wrapping TABLE A–G
- **C-43**: TABLE G `Sole structural purpose: close every TABLE A prediction row-by-row` declaration
- **C-44**: `from prediction through verification through synthesis` in the PRIMARY ANALYTICAL FRAMEWORK declaration

### Key Upgrade from R10

R10 variations placed exit conditions inside role bodies, then used a named section header before only the entry condition. R11 C-41 lifts the exit+entry pair into the boundary section so the named header sits above both — making every phase transition a structurally addressable named element, not just the primary gate.
nly the entry condition. This variation lifts every
exit+entry pair into a dedicated named boundary section so the section header sits above
BOTH the exit condition block and the entry condition block. Format "PHASE N / PHASE N+1
BOUNDARY:" applied consistently at all 3 transitions makes the full phase sequence
structurally scannable without prose reading. Risk: additional boundary sections add ~12
lines per transition; mitigated by consistent, minimal format. C-42, C-43, C-44 are present
and structurally complete but are supporting, not the axis.

---

You are running `org-scan`.

CRITICAL CONSTRAINT: This skill produces raw analysis only -- no org chart, no reporting
lines, no hierarchy diagrams. Scan first. Synthesize second. The org chart is a separate
skill. (Restated in SCHEMA DECLARATION below.)

---

### SCHEMA DECLARATION

This schema governs every table in this skill. Status applies to every column across all
tables. All tables defined here with named letter identifiers before any phase instruction
begins. Every instruction references a pre-declared table by letter. The full output schema
is structurally inspectable here before reading any instruction.

CRITICAL CONSTRAINT (restated): No org chart. No reporting lines. No hierarchy.

**TABLE A -- Pattern Hypothesis** | REQUIRED

| Prediction ID | Pattern Label | Prior Assessment | Rationale | Verification Target |
|---|---|---|---|---|
| Status: REQUIRED | REQUIRED (dictionary-constrained) | REQUIRED (high/medium/low/unknown) | REQUIRED | REQUIRED |

**TABLE B -- Scan Evidence** | REQUIRED

| Area | Inertia Match | File Path Evidence | Source Type | Hypothesis Held |
|---|---|---|---|---|
| Status: REQUIRED | REQUIRED (dictionary-constrained) | REQUIRED (real file path) | REQUIRED | optional (yes/no/partial) |

Column-order rule: Inertia Match precedes File Path Evidence in every TABLE B row.
Inverting the order is a schema violation.

**TABLE C -- Boundary Candidates** | REQUIRED

| Boundary | Seam Rationale | Confidence | Evidence |
|---|---|---|---|
| Status: REQUIRED | REQUIRED | REQUIRED (high/medium/low) | REQUIRED (TABLE B ref) |

**TABLE D -- Cross-Cutting Concerns** | REQUIRED

| Concern | Boundary Note | Affected Areas |
|---|---|---|
| Status: REQUIRED | REQUIRED | REQUIRED |

**TABLE E -- Evidence Gaps** | REQUIRED

| Gap | Type | Impact on Synthesis |
|---|---|---|
| Status: REQUIRED | REQUIRED (missing-source / ambiguous-boundary / unresolved-pattern / prediction-not-resolved) | REQUIRED |

**TABLE F -- Org Shape** | REQUIRED

| State | Shape | Justification |
|---|---|---|
| Current State | REQUIRED | REQUIRED (reference dominant pattern from PASS TOKEN) |
| Recommended State | REQUIRED | REQUIRED (reference at least one TABLE C seam) |

**TABLE G -- Prediction Resolution** | REQUIRED
Sole structural purpose: close every TABLE A prediction row-by-row. Makes hypothesis
resolution a first-class schema-level output artifact rather than a tracking column within
the scan table. This table completes the three-table hypothesis loop: TABLE A -> TABLE B -> TABLE G.

| Prediction ID | Pattern Label | Resolution | Evidence | Notes |
|---|---|---|---|---|
| Status: REQUIRED (TABLE A match) | REQUIRED | REQUIRED (confirmed/refuted/partial) | REQUIRED (TABLE B ref) | optional |

---

### GATE TOKEN PROTOCOL

Both tokens defined here before any phase begins.

PASS TOKEN: `Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]`
FAIL TOKEN: `Path floor not met -- halt.`
Additional halt strings: `Source floor not met -- halt.` | `Scanner incomplete -- halt.` | `Invalid pattern label -- halt.` | `Gap table missing -- halt.`

---

### INERTIA PATTERN DICTIONARY -- PRIMARY ANALYTICAL FRAMEWORK

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK for this skill. It is not a post-scan
labeling tool. It is the analytical spine through which all evidence is interpreted -- from
prediction through verification through synthesis. Use it to form predictions before
scanning, verify predictions during scanning, and resolve predictions during synthesis.

Free text is structurally invalid -- unconstrained values make pattern comparison across
runs unverifiable.

| Pattern Label | Structural Tells | Behavioral Signals |
|---|---|---|
| Monolith | Single top-level `src/`; no service or package seams; shared schema/config | "The codebase" as one object; ownership disputes across features; refactors blocked by hidden dependencies |
| Feature-team | Top-level dirs named by product feature or story cluster | "Our feature area" language; utilities duplicated per feature; cross-cutting infra as shared debt |
| Platform-product | Explicit `platform/` or `infra/` alongside `product/` or `apps/` | Platform SLA gating; product escalates infra; "platform or product work?" friction |
| Domain-driven | Dir or module names are DDD aggregates (Order, Customer, Billing) | Bounded-context language in PRs; domain ownership enforced at review; cross-domain coupling flagged |
| Layer | `frontend/` + `backend/` + `data/` + `infra/` as top-level organizing axis | Layer-team gating on cross-cutting tickets; layer leads as de facto owners |
| Service-oriented | `services/` with named service dirs; docker-compose or k8s manifests; multiple Dockerfiles | Per-service deployment; "which service owns X?" is recurring; teams named after services |
| Hybrid | Mixed signals from 2+ patterns; historical seams visible in naming inconsistencies | Org chart diverges from code; dual reporting lines; naming conventions conflict across vintages |

---

### ROLE SEQUENCE: PREDICTOR -> SCANNER -> GATEKEEPER -> SYNTHESIZER

Occupy exactly one role at a time. Every role transition requires a named control-transfer
declaration. A missing declaration is a role boundary violation.

---

#### ROLE: PREDICTOR

Before reading any file, scanning any directory, or examining any repo signal:

1. Apply the INERTIA PATTERN DICTIONARY -- PRIMARY ANALYTICAL FRAMEWORK to form predictions.
   Use prior context only (repo name, user description, conversation history). Do not access
   evidence from this skill run.
2. Populate TABLE A. At least 2 rows required. Every row: Prediction ID, Pattern Label from
   dictionary, Prior Assessment, Rationale from prior context only, Verification Target.
3. Anti-fabrication: TABLE A Rationale derives from prior context only. If no prior context
   exists for a pattern, write "No prior context" in Rationale and Unknown in Prior Assessment.

---

### PHASE 1 / PHASE 2 BOUNDARY:

EXIT CONDITION (ROLE: PREDICTOR): Write the following before leaving this role:

> `PREDICTION COMPLETE -- TABLE A has [N] rows -- control transfers to SCANNER`

ENTRY CONDITION (ROLE: SCANNER): The above declaration must appear in this output before
SCANNER work begins. A missing declaration is a role boundary violation. Do not begin
SCANNER instructions until that exact phrase is present.

---

#### ROLE: SCANNER

Scan the repo. Source types to cover (scan at least 3 of 7):

1. CLAUDE.md files (any level)
2. Dependency manifests (`package.json`, `Cargo.toml`, `go.mod`, `pyproject.toml`)
3. `design/` directories and ADR files
4. Namespace structure (top-level directories, module names, package declarations)
5. Test coverage areas (`test/`, `tests/`, `__tests__/`, `spec/` directories)
6. `SPECS.md`, `SPEC.md`, `specs/` directories
7. `.craft/roles/` existing role files

Instructions:
1. Populate TABLE B. Every row: real file path required; Inertia Match from dictionary only;
   Source Type from list above; Hypothesis Held where row matches a TABLE A prediction.
2. Path floor: collect at least 5 distinct file paths across TABLE B. Floor is a gate
   precondition -- record shortfalls in TABLE E (type: missing-source), do not invent paths.
3. Populate TABLE C. Every Seam Rationale must explain why this is a natural split, not just
   where a directory boundary exists. Reference the inertia pattern driving the seam.
4. Populate TABLE D. Every Boundary Note must explain why the concern spans team lines.
5. Populate TABLE E. For any TABLE A Verification Target not reached, add a row with
   type: prediction-not-resolved.
6. Write headcount signal: estimate range, 2-3 sentences, cite TABLE B and TABLE D rows.

Anti-fabrication: Every TABLE B row must cite a real file path. No real path -> TABLE E.

---

### PHASE 2 / PHASE 3 BOUNDARY: GATE EVALUATION

EXIT CONDITION (ROLE: SCANNER): Write the following before gate evaluation begins:

> `SCANNER COMPLETE -- control transfers to GATEKEEPER`

Gate entry failure is equivalent to a control-transfer failure between named roles -- the
SCANNER has not handed off.

ENTRY CONDITION (ROLE: GATEKEEPER): The above declaration must be present. Do not evaluate
the gate checklist until that exact phrase appears.

SCANNER postcondition: TABLE B, TABLE C, TABLE D, TABLE E written. Headcount signal written.
GATEKEEPER precondition: SCANNER COMPLETE declaration present. PASS TOKEN or FAIL TOKEN
written before SYNTHESIZER begins.
These two blocks name the same contract from both sides. Both must hold before SYNTHESIZER begins.

Gate checklist -- evaluate each item in order; do not skip:

1. Is `SCANNER COMPLETE -- control transfers to GATEKEEPER` present above?
   -- If absent: Write `Scanner incomplete -- halt.`
2. Are at least 5 distinct file paths present across TABLE B rows?
   -- If not: Write `Path floor not met -- halt.`
3. Are at least 3 source types represented in TABLE B?
   -- If not: Write `Source floor not met -- halt.`
4. Does every TABLE B Inertia Match value appear in the dictionary exactly?
   -- If not: Write `Invalid pattern label -- halt.`
5. Is TABLE E present (even if no rows)?
   -- If not: Write `Gap table missing -- halt.`

All 5 pass -- write PASS TOKEN:

> `Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]`

N = source types scanned. M = distinct file paths in TABLE B. Pattern label = most-evidenced
dictionary label across TABLE B Inertia Match.

---

### PHASE 3 / PHASE 4 BOUNDARY:

EXIT CONDITION (ROLE: GATEKEEPER): PASS TOKEN written above. If FAIL TOKEN or halt string
was written, halt -- do not proceed to SYNTHESIZER.

ENTRY CONDITION (ROLE: SYNTHESIZER): PASS TOKEN must be present above. Confirm it is
present before beginning. If FAIL TOKEN appears instead, do not begin SYNTHESIZER work.

---

#### ROLE: SYNTHESIZER

Entry condition: PASS TOKEN written above.

1. Produce TABLE F (Org Shape). Exactly two rows: Current State and Recommended State.
   No org chart. No reporting lines. Reference dominant pattern from PASS TOKEN.
2. Produce TABLE G (Prediction Resolution). Every TABLE A Prediction ID must appear in
   TABLE G. Unresolvable predictions -> TABLE E, type: prediction-not-resolved.
3. Write AREAS: name each work area inferred from TABLE B. Every area cites at least one
   TABLE B row. Anti-fabrication: no area without TABLE B row support.
4. Write TEAM BOUNDARIES: summarize TABLE C. Name candidate seams and the inertia pattern
   driving each.
5. Write CROSS-CUTTING CONCERNS: summarize TABLE D. For each concern, name which areas are
   affected and why the concern crosses team lines.
6. Write HEADCOUNT SIGNALS: restate scanner estimate; add synthesis commentary citing TABLE F
   and TABLE G resolution count.

---

### SYNTHESIZER / END BOUNDARY:

EXIT CONDITION (ROLE: SYNTHESIZER): Write:

> `SYNTHESIS COMPLETE -- [N] areas named, [M] boundaries identified, [range] headcount estimated, [N] TABLE A predictions resolved in TABLE G`

---

## V-02 -- Schema Declaration as Named Block

**Axis**: C-42 (SCHEMA DECLARATION as the first named structural block) -- schema appears
before the framework declaration, making the output contract the structural anchor before
any posture statement.
**Hypothesis**: C-42's analogy to GATE TOKEN PROTOCOL (C-20) is strongest when the SCHEMA
DECLARATION block appears first -- before framework, before gate tokens -- just as GATE
TOKEN PROTOCOL appears before role instructions so that token names are defined before they
are used. Placing SCHEMA DECLARATION first means an agent sees the full output contract
(TABLE A through TABLE G) before learning what analytical posture to adopt. The schema
becomes the anchor from which all other declarations derive. Risk: schema-before-framework
is counter-intuitive; mitigated by the block label making the purpose explicit. C-41 uses
GROUP A/B/C/D boundary section headers above both exit and entry blocks. C-43 includes TABLE
G "Sole structural purpose:" declaration. C-44 includes "from prediction through verification
through synthesis" in the framework block.

---

You are running `org-scan`.

CRITICAL CONSTRAINT: Raw analysis only -- no org chart, no reporting lines, no hierarchy.
Scan first. Synthesize second. (Restated in SCHEMA DECLARATION.)

---

### SCHEMA DECLARATION

This schema governs every table in this skill. Status applies to every column across all
tables. All output tables are defined here with named letter identifiers before any phase
instruction, framework declaration, or gate token definition. Every instruction references
a pre-declared table by letter. The full output schema is structurally inspectable before
reading a single instruction.

CRITICAL CONSTRAINT (restated): No org chart. No reporting lines. No hierarchy.

**TABLE A -- Pattern Hypothesis** | REQUIRED
*Produced by: PREDICTOR before any scan evidence is collected.*

| Prediction ID | Pattern Label | Prior Assessment | Rationale | Verification Target |
|---|---|---|---|---|
| Status: REQUIRED | REQUIRED (dictionary-constrained) | REQUIRED (high/medium/low/unknown) | REQUIRED | REQUIRED |

**TABLE B -- Scan Evidence** | REQUIRED
*Produced by: SCANNER.*

| Area | Inertia Match | File Path Evidence | Source Type | Hypothesis Held |
|---|---|---|---|---|
| Status: REQUIRED | REQUIRED (dictionary-constrained) | REQUIRED (real file path) | REQUIRED | optional (yes/no/partial) |

Column-order rule: Inertia Match precedes File Path Evidence in every TABLE B row.
Inverting the order is a schema violation.

**TABLE C -- Boundary Candidates** | REQUIRED
*Produced by: SCANNER.*

| Boundary | Seam Rationale | Confidence | Evidence |
|---|---|---|---|
| Status: REQUIRED | REQUIRED | REQUIRED (high/medium/low) | REQUIRED (TABLE B ref) |

**TABLE D -- Cross-Cutting Concerns** | REQUIRED
*Produced by: SCANNER.*

| Concern | Boundary Note | Affected Areas |
|---|---|---|
| Status: REQUIRED | REQUIRED | REQUIRED |

**TABLE E -- Evidence Gaps** | REQUIRED
*Produced by: SCANNER.*

| Gap | Type | Impact on Synthesis |
|---|---|---|
| Status: REQUIRED | REQUIRED (missing-source / ambiguous-boundary / unresolved-pattern / prediction-not-resolved) | REQUIRED |

**TABLE F -- Org Shape** | REQUIRED
*Produced by: SYNTHESIZER.*

| State | Shape | Justification |
|---|---|---|
| Current State | REQUIRED | REQUIRED (dominant pattern from PASS TOKEN) |
| Recommended State | REQUIRED | REQUIRED (TABLE C seam reference) |

**TABLE G -- Prediction Resolution** | REQUIRED
*Produced by: SYNTHESIZER.*
Sole structural purpose: close every TABLE A prediction row-by-row. Makes hypothesis
resolution a first-class schema-level output artifact. This table completes the three-table
hypothesis loop: TABLE A -> TABLE B -> TABLE G.

| Prediction ID | Pattern Label | Resolution | Evidence | Notes |
|---|---|---|---|---|
| Status: REQUIRED (TABLE A match) | REQUIRED | REQUIRED (confirmed/refuted/partial) | REQUIRED (TABLE B ref) | optional |

---

### GATE TOKEN PROTOCOL

PASS TOKEN: `Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]`
FAIL TOKEN: `Path floor not met -- halt.`
Additional halt strings: `Source floor not met -- halt.` | `Scanner incomplete -- halt.` | `Invalid pattern label -- halt.` | `Gap table missing -- halt.`

---

### INERTIA PATTERN DICTIONARY -- PRIMARY ANALYTICAL FRAMEWORK

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK for this skill. It is not a post-scan
labeling tool. It is the analytical spine through which all evidence is interpreted -- from
prediction through verification through synthesis. Use it to form predictions before
scanning, verify predictions during scanning, and resolve predictions during synthesis.

Free text is structurally invalid -- unconstrained values make pattern comparison across
runs unverifiable.

| Pattern Label | Structural Tells | Behavioral Signals |
|---|---|---|
| Monolith | Single `src/`; no service/package seams; shared config | "The codebase" as one object; ownership ambiguity; refactors blocked |
| Feature-team | Top-level dirs named by feature/story cluster | "Our feature area"; duplicated utilities; infra as shared debt |
| Platform-product | `platform/` or `infra/` alongside `product/` or `apps/` | Platform SLA gating; product escalates infra; split-owner friction |
| Domain-driven | Dir/module names are DDD aggregates (Order, Customer, Billing) | Bounded-context language; domain ownership at PR; cross-domain coupling flagged |
| Layer | `frontend/` + `backend/` + `data/` + `infra/` as top-level axis | Layer gating; cross-cutting stalls; layer leads as gatekeepers |
| Service-oriented | `services/` + named dirs + manifests + multiple Dockerfiles | Per-service deployment; "which service?" recurring; teams named after services |
| Hybrid | Mixed signals from 2+ patterns | Org chart != code structure; historical seams; naming conventions conflict |

---

### ROLE SEQUENCE: PREDICTOR -> SCANNER -> GATEKEEPER -> SYNTHESIZER

Occupy exactly one role at a time. Every role transition requires a named control-transfer
declaration. A missing declaration is a role boundary violation.

---

#### ROLE: PREDICTOR (GROUP A)

Before opening any file or reading any directory:

1. Apply the INERTIA PATTERN DICTIONARY to form predictions from prior context only.
2. Populate TABLE A. At least 2 rows. Every row: Prediction ID, Pattern Label, Prior
   Assessment, Rationale (prior context only), Verification Target.
3. Anti-fabrication: if no prior context exists for a pattern, write "No prior context."

---

### GROUP A / GROUP B BOUNDARY:

EXIT CONDITION (PREDICTOR): Write before leaving GROUP A:

> `PREDICTION COMPLETE -- TABLE A has [N] rows -- control transfers to SCANNER`

ENTRY CONDITION (SCANNER): The above must appear before GROUP B begins. Absent declaration
= role boundary violation.

---

#### ROLE: SCANNER (GROUP B)

Source types (scan at least 3 of 7): CLAUDE.md files / dependency manifests / design/ dirs
/ namespace structure / test coverage areas / SPECS.md or specs/ / .craft/roles/ files.

1. Populate TABLE B: real paths only; dictionary-constrained Inertia Match; Hypothesis Held
   where matching TABLE A.
2. Path floor: 5 distinct file paths across TABLE B -- gate precondition.
3. Populate TABLE C: seam rationale explains natural split, names driving pattern.
4. Populate TABLE D: boundary note explains why concern spans team lines.
5. Populate TABLE E: unresolved TABLE A Verification Targets -> type: prediction-not-resolved.
6. Headcount estimate: range + 2-3 sentence rationale citing TABLE B and TABLE D.

Anti-fabrication: every TABLE B row cites a real path. No real path -> TABLE E.

---

### GROUP B / GROUP C BOUNDARY: GATE EVALUATION

EXIT CONDITION (SCANNER): Write before gate begins:

> `SCAN COMPLETE -- control transfers to GATEKEEPER`

Gate entry failure is equivalent to a control-transfer failure between named roles -- the
SCANNER has not handed off.

ENTRY CONDITION (GATEKEEPER): The above declaration must be present. Evaluate checklist
only after that exact phrase appears.

SCANNER postcondition: TABLE B, C, D, E written. Headcount written.
GATEKEEPER precondition: SCAN COMPLETE declaration present. PASS TOKEN or FAIL TOKEN written.
These two blocks name the same contract from both sides. Both must hold before GROUP D begins.

Checklist -- evaluate each item in order; do not skip:

1. `SCAN COMPLETE -- control transfers to GATEKEEPER` present? -- absent: `Scanner incomplete -- halt.`
2. 5+ distinct file paths in TABLE B? -- no: `Path floor not met -- halt.`
3. 3+ source types in TABLE B? -- no: `Source floor not met -- halt.`
4. Every TABLE B Inertia Match in dictionary exactly? -- no: `Invalid pattern label -- halt.`
5. TABLE E present? -- no: `Gap table missing -- halt.`

All pass -- write PASS TOKEN:

> `Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]`

---

### GROUP C / GROUP D BOUNDARY:

EXIT CONDITION (GATEKEEPER): PASS TOKEN written. If FAIL TOKEN or halt string present -- halt.

ENTRY CONDITION (SYNTHESIZER): PASS TOKEN must be present. If FAIL TOKEN or halt string
appears instead, do not proceed to GROUP D.

---

#### ROLE: SYNTHESIZER (GROUP D)

Entry condition: PASS TOKEN present above.

1. Produce TABLE F: Current State and Recommended State rows only. No org chart.
2. Produce TABLE G: close every TABLE A prediction. Unresolvable -> TABLE E.
3. Write AREAS: every area cites TABLE B row. Anti-fabrication applies.
4. Write TEAM BOUNDARIES: TABLE C seams + driving inertia patterns.
5. Write CROSS-CUTTING CONCERNS: TABLE D + boundary problem per concern.
6. Write HEADCOUNT SIGNALS: range + synthesis rationale + TABLE G count.

> `SYNTHESIS COMPLETE -- [N] areas, [M] boundaries, [range] headcount, [N] predictions resolved`

---

## V-03 -- Analytical Arc Declaration

**Axis**: C-44 -- dictionary declaration names all three phases with role assignments
**Hypothesis**: C-44 extends C-40 from a posture-reorientation statement to a phase-arc-
spanning declaration. The strongest form assigns each phase to a named role: "from prediction
(PREDICTOR) through verification (SCANNER) through synthesis (SYNTHESIZER)." This makes the
dictionary's analytical scope per-role explicit -- agents reading the framework declaration
see their own role's phase assignment before encountering any instructions. The phase-role
pairing also makes C-44 distinguishable from C-40: C-40 establishes the posture ("not a
post-hoc labeling tool"), C-44 binds that posture to a named role at each phase. Risk:
adding role names to the framework declaration creates coupling between declaration and
instruction; mitigated because the role names are stable across all skill variations.
C-41 uses PHASE N / PHASE N+1 BOUNDARY: headers. C-42 uses SCHEMA DECLARATION block.
C-43 uses TABLE G "Sole structural purpose:" declaration.

---

You are running `org-scan`.

CRITICAL CONSTRAINT: Raw analysis only -- no org chart, no reporting lines, no hierarchy.
Scan first. Synthesize second. (Restated in SCHEMA DECLARATION.)

---

### INERTIA PATTERN DICTIONARY -- PRIMARY ANALYTICAL FRAMEWORK

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK for this skill. It is the analytical
spine through which all evidence is interpreted -- from prediction through verification
through synthesis. It is not a post-scan labeling tool. PREDICTOR applies it in the
prediction phase to form hypotheses before examining evidence. SCANNER applies it in the
verification phase to label each finding against a prior prediction. SYNTHESIZER applies
it in the synthesis phase to resolve predictions and name the dominant pattern.

Free text is structurally invalid -- unconstrained values make pattern comparison across
runs unverifiable.

| Pattern Label | Structural Tells | Behavioral Signals |
|---|---|---|
| Monolith | Single `src/`; no service/package seams; shared config | "The codebase" as one unit; ownership disputes; refactors blocked by hidden dependencies |
| Feature-team | Top-level dirs named by feature or story cluster | "Our feature"; utilities duplicated per feature; infra as shared debt |
| Platform-product | `platform/` or `infra/` alongside `product/` or `apps/` | Platform SLA gating; product escalates infra; "platform or product?" friction |
| Domain-driven | Dir/module names are DDD aggregates (Order, Customer, Billing) | Bounded-context language in PRs; domain ownership enforced at review |
| Layer | `frontend/` + `backend/` + `data/` + `infra/` as top-level axis | Layer gating on cross-cutting tickets; layer leads as de facto owners |
| Service-oriented | `services/` + named dirs + manifests + multiple Dockerfiles | Per-service deployment; "which service?" recurring; teams named after services |
| Hybrid | Mixed signals from 2+ patterns | Org chart != code structure; dual reporting lines; naming inconsistency across vintages |

---

### SCHEMA DECLARATION

This schema governs every table in this skill. Status applies to every column across all
tables. Declared before any phase instruction begins -- every instruction references a
pre-declared table by letter.

CRITICAL CONSTRAINT (restated): No org chart. No reporting lines. No hierarchy.

**TABLE A -- Pattern Hypothesis** | REQUIRED

| Prediction ID | Pattern Label | Prior Assessment | Rationale | Verification Target |
|---|---|---|---|---|
| Status: REQUIRED | REQUIRED (dictionary) | REQUIRED (high/medium/low/unknown) | REQUIRED | REQUIRED |

**TABLE B -- Scan Evidence** | REQUIRED

| Area | Inertia Match | File Path Evidence | Source Type | Hypothesis Held |
|---|---|---|---|---|
| Status: REQUIRED | REQUIRED (dictionary) | REQUIRED (real file path) | REQUIRED | optional (yes/no/partial) |

Column-order rule: Inertia Match precedes File Path Evidence. Inverting is a schema violation.

**TABLE C -- Boundary Candidates** | REQUIRED

| Boundary | Seam Rationale | Confidence | Evidence |
|---|---|---|---|
| Status: REQUIRED | REQUIRED | REQUIRED | REQUIRED (TABLE B ref) |

**TABLE D -- Cross-Cutting Concerns** | REQUIRED

| Concern | Boundary Note | Affected Areas |
|---|---|---|
| Status: REQUIRED | REQUIRED | REQUIRED |

**TABLE E -- Evidence Gaps** | REQUIRED

| Gap | Type | Impact on Synthesis |
|---|---|---|
| Status: REQUIRED | REQUIRED (missing-source / ambiguous-boundary / unresolved-pattern / prediction-not-resolved) | REQUIRED |

**TABLE F -- Org Shape** | REQUIRED

| State | Shape | Justification |
|---|---|---|
| Current State | REQUIRED | REQUIRED (dominant pattern from PASS TOKEN) |
| Recommended State | REQUIRED | REQUIRED (TABLE C seam) |

**TABLE G -- Prediction Resolution** | REQUIRED
Sole structural purpose: close every TABLE A prediction row-by-row. Makes hypothesis
resolution a first-class schema-level output artifact. Completes the three-table loop:
TABLE A -> TABLE B -> TABLE G.

| Prediction ID | Pattern Label | Resolution | Evidence | Notes |
|---|---|---|---|---|
| Status: REQUIRED (TABLE A match) | REQUIRED | REQUIRED (confirmed/refuted/partial) | REQUIRED | optional |

---

### GATE TOKEN PROTOCOL

PASS TOKEN: `Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]`
FAIL TOKEN: `Path floor not met -- halt.`
Additional halt strings: `Source floor not met -- halt.` | `Scanner incomplete -- halt.` | `Invalid pattern label -- halt.` | `Gap table missing -- halt.`

---

### ROLE SEQUENCE: PREDICTOR -> SCANNER -> GATEKEEPER -> SYNTHESIZER

Occupy exactly one role at a time. Every role transition requires a named control-transfer
declaration. A missing declaration is a role boundary violation.

---

#### ROLE: PREDICTOR

Phase: prediction. Apply the INERTIA PATTERN DICTIONARY -- PRIMARY ANALYTICAL FRAMEWORK
to form predictions from prior context only. Do not read files or scan directories.

1. Populate TABLE A. At least 2 rows. Pattern Label from dictionary. Prior Assessment:
   high/medium/low/unknown. Rationale: prior context only. If none, write "No prior context."
2. For each pattern, state what evidence would confirm or refute it (Verification Target).
3. Anti-fabrication: TABLE A Rationale derives from prior context only.

---

### PHASE 1 / PHASE 2 BOUNDARY:

EXIT CONDITION (PREDICTOR): Write before leaving prediction phase:

> `PREDICTION COMPLETE -- TABLE A has [N] rows -- control transfers to SCANNER`

ENTRY CONDITION (SCANNER): The above declaration must appear before SCANNER begins.
Absent = role boundary violation.

---

#### ROLE: SCANNER

Phase: verification. Apply the INERTIA PATTERN DICTIONARY to label each finding against a
prior prediction.

Source types (scan at least 3 of 7): CLAUDE.md / dependency manifests / design/ dirs /
namespace structure / test coverage areas / SPECS.md or specs/ / .craft/roles/ files.

1. Populate TABLE B: real paths only; dictionary Inertia Match; Hypothesis Held where
   matching TABLE A prediction.
2. Path floor: 5 distinct file paths -- gate precondition. Shortfalls -> TABLE E.
3. Populate TABLE C: seam rationale names natural split reason and driving pattern.
4. Populate TABLE D: boundary note explains why concern spans team lines.
5. Populate TABLE E: unresolved TABLE A Verification Targets -> type: prediction-not-resolved.
6. Headcount estimate: range + 2-3 sentence rationale.

---

### PHASE 2 / PHASE 3 BOUNDARY: GATE EVALUATION

EXIT CONDITION (SCANNER): Write before gate evaluation begins:

> `SCANNER COMPLETE -- control transfers to GATEKEEPER`

Gate entry failure is equivalent to a control-transfer failure between named roles -- the
SCANNER has not handed off.

ENTRY CONDITION (GATEKEEPER): The above must be present. Checklist evaluated only after
that exact phrase appears.

SCANNER postcondition: TABLE B, C, D, E written. Headcount written.
GATEKEEPER precondition: SCANNER COMPLETE present. PASS TOKEN or FAIL TOKEN written.
These two blocks name the same contract from both sides. Both must hold before SYNTHESIZER begins.

Checklist -- evaluate in order; do not skip:

1. `SCANNER COMPLETE -- control transfers to GATEKEEPER` present? -- absent: `Scanner incomplete -- halt.`
2. 5+ distinct file paths in TABLE B? -- no: `Path floor not met -- halt.`
3. 3+ source types in TABLE B? -- no: `Source floor not met -- halt.`
4. Every TABLE B Inertia Match in dictionary exactly? -- no: `Invalid pattern label -- halt.`
5. TABLE E present? -- no: `Gap table missing -- halt.`

All pass -- write PASS TOKEN:

> `Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]`

---

### PHASE 3 / PHASE 4 BOUNDARY:

EXIT CONDITION (GATEKEEPER): PASS TOKEN written. If FAIL TOKEN or halt string present --
halt. SYNTHESIZER does not run.

ENTRY CONDITION (SYNTHESIZER): PASS TOKEN must be present above. Confirm before beginning.

---

#### ROLE: SYNTHESIZER

Phase: synthesis. Apply the INERTIA PATTERN DICTIONARY to resolve predictions and name the
dominant org pattern.

1. Produce TABLE F: two rows (Current State / Recommended State). No org chart.
2. Produce TABLE G: close every TABLE A prediction. Unresolvable -> TABLE E.
3. Write AREAS: every area cites TABLE B row. Anti-fabrication.
4. Write TEAM BOUNDARIES: TABLE C seams + driving inertia patterns.
5. Write CROSS-CUTTING CONCERNS: TABLE D + boundary problem per concern.
6. Write HEADCOUNT SIGNALS: range + synthesis rationale + TABLE G resolution count.

> `SYNTHESIS COMPLETE -- [N] areas, [M] boundaries, [range] headcount, [N] predictions resolved`

---

## V-04 -- Prediction-Resolution Table Architecture + Named Boundaries

**Axes**: C-43 (TABLE G as dedicated first-class output) + C-41 (named boundaries at every
transition)
**Hypothesis**: C-43 elevates TABLE G from a schema entry to a named output with an explicit
"Sole structural purpose:" declaration and the three-table loop (TABLE A -> TABLE B -> TABLE
G) named in the purpose block. When C-41 is combined with C-43, the hypothesis lifecycle
becomes verifiable at two structural levels: (1) schema level -- TABLE G purpose names the
loop in the output contract; (2) boundary level -- each phase transition is a named section
that makes the loop stages auditable by position in the output. Together they make hypothesis
testing the structural spine of the full output, not just a table row. Risk: emphasis on
TABLE G purpose may over-weight resolution over evidence collection; mitigated by preserving
all TABLE B requirements. C-42 and C-44 are present as supporting invariants.

---

You are running `org-scan`.

CRITICAL CONSTRAINT: Raw analysis only -- no org chart, no reporting lines, no hierarchy.
Scan first. Synthesize second. (Restated in SCHEMA DECLARATION.)

---

### SCHEMA DECLARATION

This schema governs every table in this skill. Status applies to every column across all
tables. Declared before any phase instruction begins -- every instruction references a
pre-declared table by letter.

CRITICAL CONSTRAINT (restated): No org chart. No reporting lines. No hierarchy.

**TABLE A -- Pattern Hypothesis** | REQUIRED

| Prediction ID | Pattern Label | Prior Assessment | Rationale | Verification Target |
|---|---|---|---|---|
| Status: REQUIRED | REQUIRED (dictionary) | REQUIRED (high/medium/low/unknown) | REQUIRED | REQUIRED |

**TABLE B -- Scan Evidence** | REQUIRED

| Area | Inertia Match | File Path Evidence | Source Type | Hypothesis Held |
|---|---|---|---|---|
| Status: REQUIRED | REQUIRED (dictionary) | REQUIRED (real file path) | REQUIRED | optional (yes/no/partial) |

Column-order rule: Inertia Match precedes File Path Evidence. Inverting is a schema violation.

**TABLE C -- Boundary Candidates** | REQUIRED

| Boundary | Seam Rationale | Confidence | Evidence |
|---|---|---|---|
| Status: REQUIRED | REQUIRED | REQUIRED | REQUIRED (TABLE B ref) |

**TABLE D -- Cross-Cutting Concerns** | REQUIRED

| Concern | Boundary Note | Affected Areas |
|---|---|---|
| Status: REQUIRED | REQUIRED | REQUIRED |

**TABLE E -- Evidence Gaps** | REQUIRED

| Gap | Type | Impact on Synthesis |
|---|---|---|
| Status: REQUIRED | REQUIRED (missing-source / ambiguous-boundary / unresolved-pattern / prediction-not-resolved) | REQUIRED |

**TABLE F -- Org Shape** | REQUIRED

| State | Shape | Justification |
|---|---|---|
| Current State | REQUIRED | REQUIRED (dominant pattern from PASS TOKEN) |
| Recommended State | REQUIRED | REQUIRED (TABLE C seam) |

**TABLE G -- Prediction Resolution** | REQUIRED

Purpose: Explicit closure of every TABLE A prediction against TABLE B evidence.
Sole structural purpose: make hypothesis resolution a first-class schema-level output
artifact rather than a tracking column within the scan table. This table completes the
three-table hypothesis loop: TABLE A -> TABLE B -> TABLE G. No other content belongs here.
SYNTHESIZER mandate: close the hypothesis loop opened by PREDICTOR and threaded through
SCANNER.

| Prediction ID | Pattern Label | Prior Assessment | Evidence (TABLE B refs) | Resolution | Resolution Note |
|---|---|---|---|---|---|
| Status: REQUIRED (TABLE A match) | REQUIRED | REQUIRED (from TABLE A) | REQUIRED | REQUIRED (confirmed/refuted/partial) | REQUIRED |

Completeness rule: every TABLE A Prediction ID must appear as a TABLE G row. A TABLE A
prediction with no TABLE G row is a structural gap -- add TABLE E row, type:
prediction-not-resolved.

---

### GATE TOKEN PROTOCOL

PASS TOKEN: `Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]`
FAIL TOKEN: `Path floor not met -- halt.`
Additional halt strings: `Source floor not met -- halt.` | `Scanner incomplete -- halt.` | `Invalid pattern label -- halt.` | `Gap table missing -- halt.`

---

### INERTIA PATTERN DICTIONARY -- PRIMARY ANALYTICAL FRAMEWORK

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK for this skill. It is not a post-scan
labeling tool. It is the analytical spine through which all evidence is interpreted -- from
prediction through verification through synthesis. Use it to form predictions before
scanning, verify predictions during scanning, and resolve predictions during synthesis.

Free text is structurally invalid -- unconstrained values make pattern comparison across
runs unverifiable.

| Pattern Label | Structural Tells | Behavioral Signals |
|---|---|---|
| Monolith | Single `src/`; no service/package seams; shared config | "The codebase" as one object; ownership disputes; refactors blocked |
| Feature-team | Top-level dirs by feature/story | "Our feature"; duplicated utils; infra as shared debt |
| Platform-product | `platform/` or `infra/` + `product/` or `apps/` | Platform SLA gating; product escalates; "platform or product?" friction |
| Domain-driven | DDD aggregate names in dirs/modules | Bounded-context language; domain ownership at review; cross-domain coupling flagged |
| Layer | `frontend/` + `backend/` + `data/` + `infra/` | Layer gating; cross-cutting stalls; layer leads as owners |
| Service-oriented | `services/` + named dirs + manifests | Per-service deployment; "which service?" recurring |
| Hybrid | Mixed signals from 2+ patterns | Org != code; historical seams; naming inconsistency |

---

### ROLE SEQUENCE: PREDICTOR -> SCANNER -> GATEKEEPER -> SYNTHESIZER

Occupy exactly one role at a time. Every role transition requires a named control-transfer
declaration. A missing declaration is a role boundary violation.

---

#### ROLE: PREDICTOR

Before any file access or directory scan:

1. Apply the dictionary to form predictions from prior context only.
2. Populate TABLE A: at least 2 rows. Every row: Prediction ID, Pattern Label, Prior
   Assessment, Rationale (prior context only), Verification Target.
3. Anti-fabrication: no evidence from this skill run in TABLE A Rationale.

---

### PREDICTOR / SCANNER BOUNDARY:

EXIT CONDITION (PREDICTOR): Write before this role ends:

> `PREDICTION COMPLETE -- TABLE A has [N] rows -- control transfers to SCANNER`

ENTRY CONDITION (SCANNER): The above must be present before SCANNER begins.
Absent = role boundary violation.

---

#### ROLE: SCANNER

Source types (scan at least 3 of 7): CLAUDE.md / dependency manifests / design/ dirs /
namespace structure / test areas / SPECS.md or specs/ / .craft/roles/ files.

1. Populate TABLE B: real paths only; dictionary Inertia Match; Hypothesis Held where
   TABLE A prediction matches.
2. Path floor: 5 distinct file paths across TABLE B -- gate precondition.
3. Populate TABLE C: seam rationale names natural split reason and driving pattern.
4. Populate TABLE D: boundary note explains why concern spans team lines.
5. Populate TABLE E: unresolved TABLE A targets -> type: prediction-not-resolved.
6. Headcount estimate: range + rationale citing TABLE B and TABLE D rows.

Anti-fabrication: every TABLE B row cites a real path. No path -> TABLE E.

---

### SCANNER / GATEKEEPER BOUNDARY: GATE EVALUATION

EXIT CONDITION (SCANNER): Write before gate begins:

> `SCANNER COMPLETE -- control transfers to GATEKEEPER`

Gate entry failure is equivalent to a control-transfer failure between named roles -- the
SCANNER has not handed off.

ENTRY CONDITION (GATEKEEPER): The above must be present. Evaluate checklist only after
that exact phrase appears.

SCANNER postcondition: TABLE B, C, D, E written. Headcount written.
GATEKEEPER precondition: SCANNER COMPLETE present. PASS TOKEN or FAIL TOKEN written.
These two blocks name the same contract from both sides. Both must hold before SYNTHESIZER begins.

Checklist -- evaluate in order; do not skip:

1. `SCANNER COMPLETE -- control transfers to GATEKEEPER` present? -- absent: `Scanner incomplete -- halt.`
2. 5+ distinct file paths in TABLE B? -- no: `Path floor not met -- halt.`
3. 3+ source types in TABLE B? -- no: `Source floor not met -- halt.`
4. Every TABLE B Inertia Match in dictionary exactly? -- no: `Invalid pattern label -- halt.`
5. TABLE E present? -- no: `Gap table missing -- halt.`

All pass -- write PASS TOKEN:

> `Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]`

---

### GATEKEEPER / SYNTHESIZER BOUNDARY:

EXIT CONDITION (GATEKEEPER): PASS TOKEN written above. If FAIL TOKEN or halt string
present -- halt. SYNTHESIZER does not run.

ENTRY CONDITION (SYNTHESIZER): PASS TOKEN must be present above. Confirm before beginning.
If FAIL TOKEN or halt string appears instead, do not proceed.

---

#### ROLE: SYNTHESIZER

Entry condition: PASS TOKEN above.

The three-table hypothesis loop -- TABLE A -> TABLE B -> TABLE G -- must be closed here.
SYNTHESIZER mandate: resolve every TABLE A prediction in TABLE G.

1. Produce TABLE F: two rows (Current State / Recommended State). No org chart.
2. Produce TABLE G: every TABLE A Prediction ID resolved. Full columns required.
   Unresolvable -> TABLE E, type: prediction-not-resolved.
3. Write AREAS: every area cites TABLE B row. Anti-fabrication applies.
4. Write TEAM BOUNDARIES: TABLE C seams + driving patterns.
5. Write CROSS-CUTTING CONCERNS: TABLE D + boundary problem per concern.
6. Write HEADCOUNT SIGNALS: range + TABLE G resolution count.

> `SYNTHESIS COMPLETE -- [N] areas, [M] boundaries, [range] headcount, [N] predictions resolved in TABLE G`

---

## V-05 -- Full Integration, Tight Register

**Axis**: All 4 new criteria in BLOCK 1/2/3/4 preamble structure -- maximum density,
minimum verbosity
**Hypothesis**: R10 V-05 established that 4 named preamble blocks (BLOCK 1: framework,
BLOCK 2: schema, BLOCK 3: gate tokens, BLOCK 4: role protocol) organize all pre-instruction
declarations with maximum structural economy. R11 V-05 carries this architecture forward
and adds C-41 through C-44 in the most compressed canonical form: C-44 as a one-sentence
extension to the BLOCK 1 arc declaration; C-42 as the explicit "SCHEMA DECLARATION" label
on BLOCK 2; C-43 as a "Sole structural purpose:" line in the TABLE G entry; C-41 as a
named ROLE / ROLE BOUNDARY: section header above both exit and entry blocks at every
phase transition. The block structure makes each criterion location-addressable by block
number. Risk: compression reduces redundancy useful to agents that scan non-linearly;
mitigated by all 4 criteria being structurally distinct and scannable by keyword.

---

You are running `org-scan`.

CRITICAL CONSTRAINT: Raw analysis only -- no org chart, no reporting lines, no hierarchy.
Scan first. Synthesize second. (Restated in BLOCK 2.)

---

### BLOCK 1 -- PRIMARY ANALYTICAL FRAMEWORK

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK for this skill. It is not a post-scan
labeling tool. It is the analytical spine through which all evidence is interpreted -- from
prediction through verification through synthesis. PREDICTOR applies it in prediction;
SCANNER applies it in verification; SYNTHESIZER applies it in synthesis.

Free text is structurally invalid -- unconstrained values make pattern comparison across
runs unverifiable.

| Pattern Label | Structural Tells | Behavioral Signals |
|---|---|---|
| Monolith | Single `src/`; no seams; shared config | "The codebase" as one unit; ownership ambiguity |
| Feature-team | Top-level dirs by feature/story | "Our feature"; duplicated utils; infra as shared debt |
| Platform-product | `platform/` + `product/` or `infra/` + `apps/` | Platform SLA gating; product escalates; split-owner friction |
| Domain-driven | DDD aggregate names in dirs/modules | Bounded-context language; domain ownership at PR |
| Layer | `frontend/` + `backend/` + `data/` + `infra/` | Layer gating; cross-cutting stalls; layer leads as owners |
| Service-oriented | `services/` + named dirs + manifests | Per-service deploy; "which service?" recurring |
| Hybrid | Mixed signals from 2+ patterns | Org != code; historical seams; naming inconsistency |

---

### BLOCK 2 -- SCHEMA DECLARATION

This schema governs every table in this skill. Status applies to every column across all
tables. Declared before any role begins -- every instruction references a pre-declared table
by letter.

CRITICAL CONSTRAINT (restated): No org chart. No reporting lines. No hierarchy.

**TABLE A -- Pattern Hypothesis** | REQUIRED

| Prediction ID | Pattern Label | Prior Assessment | Rationale | Verification Target |
|---|---|---|---|---|
| Status: REQUIRED | REQUIRED (dictionary) | REQUIRED (high/medium/low/unknown) | REQUIRED | REQUIRED |

**TABLE B -- Scan Evidence** | REQUIRED

| Area | Inertia Match | File Path Evidence | Source Type | Hypothesis Held |
|---|---|---|---|---|
| Status: REQUIRED | REQUIRED (dictionary) | REQUIRED (file path) | REQUIRED | optional (yes/no/partial) |

Column-order rule: Inertia Match precedes File Path Evidence. Inverting is a schema violation.

**TABLE C -- Boundary Candidates** | REQUIRED

| Boundary | Seam Rationale | Confidence | Evidence |
|---|---|---|---|
| Status: REQUIRED | REQUIRED | REQUIRED | REQUIRED (TABLE B ref) |

**TABLE D -- Cross-Cutting Concerns** | REQUIRED

| Concern | Boundary Note | Affected Areas |
|---|---|---|
| Status: REQUIRED | REQUIRED | REQUIRED |

**TABLE E -- Evidence Gaps** | REQUIRED

| Gap | Type | Impact on Synthesis |
|---|---|---|
| Status: REQUIRED | REQUIRED (missing-source / ambiguous-boundary / unresolved-pattern / prediction-not-resolved) | REQUIRED |

**TABLE F -- Org Shape** | REQUIRED

| State | Shape | Justification |
|---|---|---|
| Current State | REQUIRED | REQUIRED (dominant pattern from PASS TOKEN) |
| Recommended State | REQUIRED | REQUIRED (TABLE C seam) |

**TABLE G -- Prediction Resolution** | REQUIRED
Sole structural purpose: close every TABLE A prediction row-by-row. Makes hypothesis
resolution a first-class schema-level output artifact. Completes the loop:
TABLE A -> TABLE B -> TABLE G.

| Prediction ID | Pattern Label | Resolution | Evidence | Notes |
|---|---|---|---|---|
| Status: REQUIRED (TABLE A match) | REQUIRED | REQUIRED (confirmed/refuted/partial) | REQUIRED | optional |

---

### BLOCK 3 -- GATE TOKEN PROTOCOL

PASS TOKEN: `Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]`
FAIL TOKEN: `Path floor not met -- halt.`
Additional halt strings: `Source floor not met -- halt.` | `Scanner incomplete -- halt.` | `Invalid pattern label -- halt.` | `Gap table missing -- halt.`

---

### BLOCK 4 -- ROLE SEQUENCE AND CONTROL-TRANSFER PROTOCOL

Role sequence: PREDICTOR -> SCANNER -> GATEKEEPER -> SYNTHESIZER. Occupy exactly one role
at a time. Every role transition requires a named control-transfer declaration. A missing
declaration is a role boundary violation.

---

#### ROLE: PREDICTOR

Apply BLOCK 1 dictionary to form predictions from prior context only. No file access.

1. Populate TABLE A: at least 2 rows. Pattern Label from dictionary. Prior Assessment.
   Rationale = prior context only. Verification Target.
2. Anti-fabrication: no evidence from this skill run in TABLE A.

---

### PREDICTOR / SCANNER BOUNDARY:

EXIT CONDITION (PREDICTOR): Write before leaving:

> `PREDICTION COMPLETE -- TABLE A has [N] rows -- control transfers to SCANNER`

ENTRY CONDITION (SCANNER): Above must be present. Absent = role boundary violation.

---

#### ROLE: SCANNER

Source types (scan at least 3 of 7): CLAUDE.md / dependency manifests / design/ /
namespace structure / test areas / SPECS.md or specs/ / .craft/roles/

1. TABLE B: real paths; dictionary Inertia Match; Hypothesis Held where matching TABLE A.
2. Path floor: 5+ distinct paths -- gate precondition. Shortfalls -> TABLE E.
3. TABLE C: seam rationale names natural split reason and driving pattern.
4. TABLE D: boundary note explains why concern spans teams.
5. TABLE E: unresolved TABLE A targets -> type: prediction-not-resolved.
6. Headcount: range + 2-3 sentence rationale.

Anti-fabrication: every TABLE B row cites a real path.

---

### SCANNER / GATEKEEPER BOUNDARY: GATE EVALUATION

EXIT CONDITION (SCANNER): Write before gate begins:

> `SCANNER COMPLETE -- control transfers to GATEKEEPER`

Gate entry failure is equivalent to a control-transfer failure between named roles -- the
SCANNER has not handed off.

ENTRY CONDITION (GATEKEEPER): Above must be present. Checklist evaluated only after.

SCANNER postcondition: TABLE B, C, D, E written. Headcount written.
GATEKEEPER precondition: SCANNER COMPLETE present. PASS TOKEN or FAIL TOKEN written.
These two blocks name the same contract from both sides. Both must hold before SYNTHESIZER begins.

Checklist -- in order; do not skip:

1. `SCANNER COMPLETE -- control transfers to GATEKEEPER` present? -- absent: `Scanner incomplete -- halt.`
2. 5+ paths in TABLE B? -- no: `Path floor not met -- halt.`
3. 3+ source types in TABLE B? -- no: `Source floor not met -- halt.`
4. Every Inertia Match in dictionary? -- no: `Invalid pattern label -- halt.`
5. TABLE E present? -- no: `Gap table missing -- halt.`

All pass -- write PASS TOKEN:

> `Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]`

---

### GATEKEEPER / SYNTHESIZER BOUNDARY:

EXIT CONDITION (GATEKEEPER): PASS TOKEN written. If FAIL TOKEN or halt string present -- halt.

ENTRY CONDITION (SYNTHESIZER): PASS TOKEN must be present. If FAIL TOKEN or halt string
appears instead, do not proceed.

---

#### ROLE: SYNTHESIZER

Entry condition: PASS TOKEN above.

1. TABLE F: Current State / Recommended State. No org chart.
2. TABLE G: close every TABLE A prediction. Unresolvable -> TABLE E.
3. AREAS: every area cites TABLE B row. Anti-fabrication.
4. TEAM BOUNDARIES: TABLE C + driving patterns.
5. CROSS-CUTTING CONCERNS: TABLE D + boundary problem.
6. HEADCOUNT SIGNALS: range + TABLE G count.

> `SYNTHESIS COMPLETE -- [N] areas, [M] boundaries, [range] headcount, [N] predictions resolved`
