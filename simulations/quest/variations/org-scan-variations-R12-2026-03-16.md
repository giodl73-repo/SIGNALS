| Column | Status |
|---|---|
| Pattern ID | REQUIRED |
| Pattern Name | REQUIRED |
| Structural Prediction | REQUIRED |
| Behavioral Prediction | REQUIRED |
| Hypothesis Held | REQUIRED (yes / no / partial) |

**TABLE B — Scan Evidence Table**
*Produced by: SCANNER during Phase 2 evidence collection.*

| Column | Status |
|---|---|
| Area | REQUIRED |
| Source Type | REQUIRED |
| Finding | REQUIRED |
| Inertia Match | REQUIRED (dictionary value only) |
| File Path Evidence | REQUIRED (specific path) |
| Hypothesis Held | REQUIRED (yes / no / partial) |

Column order fixed: Inertia Match before File Path Evidence. Inverting is a schema violation.

**TABLE C — Headcount Signals**
*Produced by: SCANNER during Phase 2 evidence collection.*

| Column | Status |
|---|---|
| Expertise Domain | REQUIRED |
| Signal Evidence | REQUIRED |
| File Path | REQUIRED |
| FTE Range | REQUIRED (range, not point value) |

**TABLE D — Cross-Cutting Concerns**
*Produced by: SCANNER during Phase 2 evidence collection.*

| Column | Status |
|---|---|
| Concern | REQUIRED |
| Boundary Note | REQUIRED |
| File Path Evidence | REQUIRED |

**TABLE E — Team Boundary Candidates**
*Produced by: SYNTHESIZER after gate passage.*

| Column | Status |
|---|---|
| Boundary Candidate | REQUIRED |
| Seam Rationale | REQUIRED (cite TABLE B row) |
| Supporting Evidence | REQUIRED |

**TABLE F — Evidence Gaps**
*Produced by: SYNTHESIZER after gate passage.*

| Column | Status |
|---|---|
| Gap | REQUIRED |
| Implication | REQUIRED |
| Source Types Checked | REQUIRED |

**TABLE G — Prediction Resolution**
*Produced by: SYNTHESIZER after gate passage.*

| Column | Status |
|---|---|
| Pattern ID | REQUIRED |
| Pattern Name | REQUIRED |
| Structural Prediction (from TABLE A) | REQUIRED |
| Behavioral Prediction (from TABLE A) | REQUIRED |
| Evidence Summary | REQUIRED (cite TABLE B row) |
| Resolution | REQUIRED (yes / no / partial) |

Every TABLE A row must have a TABLE G row. No prediction left unresolved.

---

## GATE TOKEN PROTOCOL

**PASS**: `Gate clear — [N] sources scanned, [N] paths cited, dominant pattern: [PATTERN-ID]`
**FAIL**: `Path floor not met — scan incomplete`

One of these strings must appear at the Phase 2 / Phase 3 boundary. No prose substitution.

---

## PRIMARY ANALYTICAL FRAMEWORK: Inertia Pattern Dictionary

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK for this skill, operating from prediction through verification through synthesis. Every hypothesis in Phase 1, every Inertia Match value in Phase 2, and every synthesis claim in Phase 3 must anchor to an entry from this dictionary. The dictionary is not a post-hoc classifier — it is the analytical lens from the first prediction the PREDICTOR writes.

**Free text in the Inertia Match column is structurally invalid — unconstrained values make pattern comparison across runs unverifiable.**

Each pattern carries both **structural code signals** (visible in files) and **behavioral signals** (visible in CLAUDE.md prose, team language, ownership language, and incident response patterns). The PREDICTOR must predict both registers. The SCANNER must check both.

| Pattern ID | Pattern Name | Structural Code Signals | Behavioral Signals |
|---|---|---|---|
| I-01 | Monolith | Single root package.json; flat directory structure; no namespace separation; all tests in one directory; no per-area CLAUDE.md | "we all work on the same thing"; any engineer opens any file; bugs have no natural owner; on-call is "everyone"; onboarding means shadowing the whole codebase |
| I-02 | Accidental Silos | Multiple directories exist but no explicit ownership documentation; test coverage overlaps across directories; no seam-respecting PR convention | "not sure who owns that"; cross-area PRs stall without a clear reviewer; incidents involve multiple teams guessing; "we should probably document this" is a recurring sentiment |
| I-03 | Domain Teams | Named namespace directories; per-namespace CLAUDE.md or README; per-domain test directories; explicit ownership declared in docs or .craft/roles | "that's the X team's area"; clear escalation path per domain; engineers onboard to a single domain first; incidents have a natural first responder; PRs stay within domain seams |
| I-04 | Platform + Product | Shared infra layer (sdk/, core/, utils/, platform/) clearly distinct from product surfaces; infra layer has its own CLAUDE.md and dedicated test coverage | "we build on the platform"; platform team has separate on-call rotation; product features rarely touch infra; platform changes require a coordination meeting; "the platform team owns that" |
| I-05 | Federated | Multiple autonomous workspaces, packages, or repos with minimal shared root; independent CI per workspace; rare central merge events | "each team ships independently"; integration is opt-in; shared tooling is a separate small team; incidents are scoped to one workspace; "we don't need to coordinate on that" |
| I-06 | Hub-and-Spoke | Central orchestrator directory (nexus/, hub/, core/, router/) with peripheral plugin or service directories radiating from it; hub has disproportionate test coverage and documentation depth | "everything routes through the hub"; hub team is the bottleneck for peripheral changes; peripheral teams file issues against the hub; "we need the hub team to merge this first"; hub engineers are stretched thin |
| I-07 | Undefined | Fewer than 3 source types were readable; evidence is insufficient to classify | Cannot assess behavioral signals; pattern classification deferred |

---

## GROUP A — PREDICTOR PHASE

### Phase 1: Hypothesis Generation (Role: PREDICTOR)

**Entry condition**: Skill invocation. No prior phase required.

Before reading any file, produce TABLE A. For each pattern I-01 through I-06, write both a structural prediction (what code-level signals you expect to find or not find) and a behavioral prediction (what team-language or ownership signals you expect to find in CLAUDE.md prose). Set Hypothesis Held based on your expectation before any evidence.

You are the PREDICTOR. Making both predictions forces the inertia dictionary to be falsifiable at both registers — structural and behavioral. Do not read any files during this phase.

→ Output TABLE A.

**Phase 1 exit**: Write `PREDICTOR COMPLETE — [N] predictions recorded` before proceeding.

---

### GROUP A / GROUP B BOUNDARY

*PREDICTOR exits. Control transfers to SCANNER. TABLE A must exist.*

---

## GROUP B — SCANNER PHASE

### Phase 2: Evidence Collection (Role: SCANNER)

**Entry condition**: PREDICTOR COMPLETE present. TABLE A exists.

**Anti-fabrication**: Report only findings from files actually read. Record absences. Do not infer from file names.

Scan at least 3 of 7 source types:
1. CLAUDE.md files (all levels)
2. package.json (root and nested)
3. design/ or docs/ directories
4. Namespace directories
5. Test coverage areas
6. SPECS.md or specification files
7. .craft/roles/ or role definition files

When reading CLAUDE.md files, note team language, ownership language, and escalation language — these are behavioral signal evidence for TABLE B.

**File path floor (gate precondition)**: 5+ specific file paths in TABLE B. Blocks gate passage.

→ Output TABLE B, TABLE C, TABLE D.

**Phase 2 exit**: Write `SCANNER COMPLETE — control transfers to GATEKEEPER`.

---

### GROUP B / GATE BOUNDARY

**PHASE 2 / PHASE 3 BOUNDARY: GATE EVALUATION**

This gate is the postcondition of Phase 2 and the precondition of Phase 3. Both sides name the same contract. Both must hold.

**Gate checklist** — evaluate each item in order; do not skip:
1. At least 3 of 7 source types were scanned
2. TABLE B has at least 5 rows with File Path Evidence populated
3. All Inertia Match cells use I-01 through I-07
4. All Hypothesis Held cells use: yes / no / partial
5. Anti-fabrication confirmed

Write PASS or FAIL token.

---

### GATE / GROUP C BOUNDARY

*Control transfers to SYNTHESIZER. FAIL TOKEN halts execution.*

---

## GROUP C — SYNTHESIZER PHASE

### Phase 3: Synthesis (Role: SYNTHESIZER)

**Entry condition**: PASS TOKEN present.

**CONSTRAINT RESTATEMENT**: Raw analysis only. No org chart. No reporting lines. (Stated in preamble; restated here.)

→ Output TABLE E, TABLE F.
→ Output TABLE G: for every TABLE A row, resolve both the structural prediction and the behavioral prediction. Evidence Summary must cite TABLE B rows that speak to each register.
→ Write **Org Shape** paragraph: dominant pattern from PASS TOKEN. Separate CURRENT STATE from RECOMMENDED STATE. Justify from TABLE B structural and behavioral evidence.
→ Write **Headcount Range**: total FTE range from TABLE C with rationale.

**Phase 3 exit**: Write `SYNTHESIZER COMPLETE`.

---

### GROUP C / GROUP D BOUNDARY

*Skill complete.*

---

## GROUP D — OUTPUT SUMMARY

Produced: TABLE A–G (dual-register predictions and resolutions), Org Shape (CURRENT / RECOMMENDED), Headcount Range.

**CONSTRAINT (final)**: Raw analysis only. No org chart. No reporting lines.

---
---

## V-05 — Output Format + Phrasing Register (Combination)

**Axes**: Output format (schema-first, all tables pre-declared) + Phrasing register (direct second-person address throughout: "You are the PREDICTOR. You must...").
**Hypothesis**: Direct second-person address makes constraints harder to ignore than third-person procedural description — "you must not produce an org chart" is more arresting than "this skill does not produce an org chart" — and combined with schema-first design, the two axes together close both the structural compliance gap (schema contract) and the attention gap (direct address).

---

# org-scan

You are about to scan a repo and produce raw org-structure analysis. **You must produce raw analysis only — no org chart, no reporting lines.** Use /org-build to turn this analysis into a full org.

---

## SCHEMA DECLARATION

This schema governs every table in this skill. Status applies to every column across all tables. You must match this schema exactly.

**TABLE A — Hypothesis Table**
*Produced by: PREDICTOR before any scan evidence is collected.*

| Column | Status | Notes |
|---|---|---|
| Pattern ID | REQUIRED | I-01 through I-07 |
| Pattern Name | REQUIRED | Match dictionary |
| Prediction | REQUIRED | One sentence stating expectation before evidence |
| Hypothesis Held | REQUIRED | yes / no / partial |

**TABLE B — Scan Evidence Table**
*Produced by: SCANNER during Phase 2 evidence collection.*

| Column | Status | Notes |
|---|---|---|
| Area | REQUIRED | |
| Source Type | REQUIRED | 1–7 from source type list |
| Finding | REQUIRED | From files you have actually read |
| Inertia Match | REQUIRED | I-01–I-07 only; you must not enter free text |
| File Path Evidence | REQUIRED | Specific file path |
| Hypothesis Held | REQUIRED | yes / no / partial |

Column-order rule: Inertia Match must come before File Path Evidence. Inverting this order is a schema violation.
Minimum requirement: 5 rows with File Path Evidence populated before you reach the gate.

**TABLE C — Headcount Signals**
*Produced by: SCANNER during Phase 2 evidence collection.*

| Column | Status | Notes |
|---|---|---|
| Expertise Domain | REQUIRED | |
| Signal Evidence | REQUIRED | |
| File Path | REQUIRED | Specific path |
| FTE Range | REQUIRED | Range, e.g., 2–4; you must not use a point value |

**TABLE D — Cross-Cutting Concerns**
*Produced by: SCANNER during Phase 2 evidence collection.*

| Column | Status | Notes |
|---|---|---|
| Concern | REQUIRED | |
| Boundary Note | REQUIRED | You must name which boundaries this concern crosses |
| File Path Evidence | REQUIRED | Specific path |

**TABLE E — Team Boundary Candidates**
*Produced by: SYNTHESIZER after gate passage.*

| Column | Status | Notes |
|---|---|---|
| Boundary Candidate | REQUIRED | |
| Seam Rationale | REQUIRED | You must cite a specific TABLE B row |
| Supporting Evidence | REQUIRED | TABLE B row reference |

**TABLE F — Evidence Gaps**
*Produced by: SYNTHESIZER after gate passage.*

| Column | Status | Notes |
|---|---|---|
| Gap | REQUIRED | |
| Implication | REQUIRED | How this gap would change the analysis |
| Source Types Checked | REQUIRED | |

**TABLE G — Prediction Resolution**
*Produced by: SYNTHESIZER after gate passage.*

| Column | Status | Notes |
|---|---|---|
| Pattern ID | REQUIRED | |
| Pattern Name | REQUIRED | |
| Original Prediction | REQUIRED | Copy from TABLE A |
| Evidence Summary | REQUIRED | You must cite a specific TABLE B row |
| Resolution | REQUIRED | yes / no / partial |

You must not leave any TABLE A row without a corresponding TABLE G row.

---

## GATE TOKEN PROTOCOL

Both tokens are defined here. You will write exactly one of them at the Phase 2 / Phase 3 boundary.

**PASS**: `Gate clear — [N] sources scanned, [N] paths cited, dominant pattern: [PATTERN-ID]`
**FAIL**: `Path floor not met — scan incomplete`

You must not substitute prose for these tokens.

---

## PRIMARY ANALYTICAL FRAMEWORK: Inertia Pattern Dictionary

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK for this skill, operating from prediction through verification through synthesis. You must anchor every TABLE A prediction, every TABLE B Inertia Match value, and every TABLE G resolution to an entry from this dictionary.

**You must not enter free text in the Inertia Match column — unconstrained values make pattern comparison across runs unverifiable.**

| Pattern ID | Pattern Name | Structural Code Signals | Behavioral Signals |
|---|---|---|---|
| I-01 | Monolith | Single root package.json, flat dirs, no namespace separation | "we all work on the same thing", unclear bug ownership |
| I-02 | Accidental Silos | Multiple dirs without ownership docs, overlapping coverage | "not sure who owns that", cross-area PRs stall |
| I-03 | Domain Teams | Named namespaces with per-namespace docs, distinct test dirs | "that's the X team's area", clear escalation paths |
| I-04 | Platform + Product | Shared infra layer (sdk/core/utils) + product surfaces above | "we build on the platform", separate infra team |
| I-05 | Federated | Multiple autonomous workspaces, minimal shared root | "each team ships independently", rare central coordination |
| I-06 | Hub-and-Spoke | Central orchestrator + peripheral plugins/services | "everything routes through the hub", hub is bottleneck |
| I-07 | Undefined | Insufficient evidence to classify | — |

---

## GROUP A — PREDICTOR PHASE

### Phase 1: You Are the PREDICTOR

You are the PREDICTOR. Before reading any file, you must produce TABLE A as defined in the SCHEMA DECLARATION above.

For each pattern I-01 through I-06, write one prediction and set Hypothesis Held. You are making predictions before evidence — you must state them as predictions. You must not read any files during this phase. Do not open CLAUDE.md. Do not check package.json. Make your predictions first.

→ Produce TABLE A now.

When TABLE A is complete, you must write: `PREDICTOR COMPLETE — [N] predictions recorded`

You must not proceed to Phase 2 until you have written this declaration.

---

### GROUP A / GROUP B BOUNDARY

*You are no longer the PREDICTOR. You are now the SCANNER. Phase 2 begins only after PREDICTOR COMPLETE is present and TABLE A exists.*

---

## GROUP B — SCANNER PHASE

### Phase 2: You Are the SCANNER

You are the SCANNER. You must verify that PREDICTOR COMPLETE is present and TABLE A exists before you begin.

**You must report only findings from files you have actually read.** If a source does not exist, record its absence. You must not infer findings from file names alone.

You must scan at least 3 of these 7 source types:
1. CLAUDE.md files (all levels)
2. package.json (root and nested)
3. design/ or docs/ directories
4. Namespace directories
5. Test coverage areas (test/, spec/, __tests__, simulation files)
6. SPECS.md or specification files
7. .craft/roles/ or role definition files

**File path floor**: You must populate at least 5 TABLE B rows with specific File Path Evidence before you reach the gate. This is a gate precondition — you may not pass the gate without meeting it.

→ Produce TABLE B. You must place Inertia Match before File Path Evidence. Inverting this order is a schema violation.
→ Produce TABLE C. You must express FTE estimates as ranges, not point values.
→ Produce TABLE D. You must include a boundary note for every concern.

When Tables B, C, and D are complete, you must write: `SCANNER COMPLETE — control transfers to GATEKEEPER`

You must not proceed to gate evaluation until you have written this declaration.

---

### GROUP B / GATE BOUNDARY

**PHASE 2 / PHASE 3 BOUNDARY: GATE EVALUATION**

You are the GATEKEEPER. You must verify that Phase 2 is complete before Phase 3 begins. This gate is the postcondition of Phase 2 and the precondition of Phase 3. Both sides name the same contract. Both must hold.

**Gate checklist** — you must evaluate each item in order; you must not skip any item:
1. At least 3 of 7 source types were scanned
2. TABLE B has at least 5 rows with File Path Evidence populated
3. Every Inertia Match cell contains a value from I-01 through I-07
4. Every Hypothesis Held cell contains: yes, no, or partial
5. Anti-fabrication confirmed — no findings were fabricated

You must write exactly one of the two GATE TOKEN PROTOCOL strings. You must not write prose in place of a token.

---

### GATE / GROUP C BOUNDARY

*You are no longer the GATEKEEPER. You are now the SYNTHESIZER. Phase 3 begins only if the PASS TOKEN is present. If you wrote the FAIL TOKEN, you must stop.*

---

## GROUP C — SYNTHESIZER PHASE

### Phase 3: You Are the SYNTHESIZER

You are the SYNTHESIZER. You must not begin Phase 3 if the FAIL TOKEN is present.

**You must not produce an org chart. You must not produce reporting lines. You must produce raw analysis only.** This constraint was stated when you began this skill. You must honor it here.

→ Produce TABLE E. For each team boundary candidate, you must cite a specific TABLE B row in the seam rationale.
→ Produce TABLE F. You must name every ambiguity or missing evidence that would change your analysis if resolved.
→ Produce TABLE G. For every row in TABLE A, you must write a resolution row. You must not leave any prediction unresolved. You must cite TABLE B evidence for each resolution.

Write **Org Shape**: name the dominant org shape matching the PASS TOKEN pattern ID. You must separate **CURRENT STATE** (what the scan reveals) from **RECOMMENDED STATE** (what the evidence suggests would reduce structural friction). You must justify your claims with TABLE B evidence.

Write **Headcount Range**: total FTE range across all TABLE C domains, with rationale.

When all artifacts are produced, you must write: `SYNTHESIZER COMPLETE`

---

### GROUP C / GROUP D BOUNDARY

*You are no longer the SYNTHESIZER. The skill is complete.*

---

## GROUP D — OUTPUT SUMMARY

You have produced: TABLE A–G (per SCHEMA DECLARATION), Org Shape paragraph (CURRENT STATE / RECOMMENDED STATE separated), Headcount Range.

**Final constraint**: You produced raw analysis only. No org chart. No reporting lines.

---

## Variation Summary

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| **Primary axis** | Role sequence | Output format | Lifecycle emphasis | Role seq + Inertia framing | Output format + Register |
| **Dominant structural feature** | Role identity + control-transfer framing | SCHEMA DECLARATION as primary contract | Named boundary ceremony at every transition | Dual-register dictionary as analytical lens | Direct second-person address throughout |
| **TABLE A** | Structural prediction + Hypothesis Held | Full column + valid-value spec | Compact inline definition | Structural + Behavioral prediction columns | Full column + direct-address constraints |
| **Phase instructions** | Full per role | Compact — reference tables by letter | Full with entry/exit blocks at every boundary | Full per role, dictionary-centric | Direct address: "You must…" |
| **Inertia dictionary** | Standard dual-register | Standard dual-register | Standard dual-register | Maximally expanded behavioral signals | Standard dual-register |
| **Gate framing** | Control-transfer between named roles | Postcondition/precondition | Named boundary header with bilateral statement | Control-transfer between named roles | Direct-address checklist |
