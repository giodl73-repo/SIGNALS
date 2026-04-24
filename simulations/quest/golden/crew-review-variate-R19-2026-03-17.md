---
skill: quest-variate
skill_target: org-review
date: 2026-03-17
round: 19
rubric: org-review-rubric-v17-2026-03-17.md
---

# org-review -- Variate R19

5 complete prompt body variations. Single-axis first (V-01 through V-03), then
two-axis and three-axis combinations (V-04, V-05).

**R19 design target**: All five R18 variants scored 265/265 under v15 (perfect on
C-01 through C-43). R18 V-04 scored 280/295 under v17 (C-44+C-45+C-47 PASS,
C-46/C-48/C-49 FAIL). R18 V-05 scored 295/295 (all six new criteria PASS). The R19
primary target is 285/295 -- R18 V-04 + C-48: add the §0-CID PIPELINE THREADING
CONTRACT named block between STATUS QUO FRAMING CONTRACT and TABLE FORMAT CONTRACT.
Full 295/295 requires C-49 (three-layer cross-reference consistency: TABLE FORMAT
CONTRACT schema notes + behavioral §§ contracts + pipeline contract all cross-reference
each other).

**R19 gap analysis from R18 V-04:**

| Criterion | R18 V-04 | What it requires |
|-----------|----------|-----------------|
| C-48 | FAIL | Named §0-CID PIPELINE THREADING CONTRACT block with four axes in STATUS QUO FRAMING CONTRACT -> §0-CID PIPELINE THREADING CONTRACT -> TABLE FORMAT CONTRACT ordering; §8 and §6 updated to include the block |
| C-49 | FAIL | TABLE FORMAT CONTRACT schema notes for §0-CID-related fields cite pipeline threading by axis name; behavioral §§ contracts also cite pipeline threading by axis name; three-layer cross-referencing complete |

**R19 variation axes:**

- V-01: Inertia framing (single axis) -- §0-CID PIPELINE THREADING CONTRACT block added;
  no schema cross-refs in TABLE FORMAT CONTRACT; no behavioral cross-refs in §§ contracts.
  C-48 PASS, C-49 FAIL. Predicted: 285/295.

- V-02: Output format (single axis) -- pipeline block added; TABLE FORMAT CONTRACT schema
  notes for §0-CID-related fields cite pipeline threading by axis name; §§ behavioral
  contracts do NOT cite pipeline by axis name. C-48 PASS, C-49 FAIL (behavioral leg
  missing). Predicted: 285/295.

- V-03: Phrasing register (single axis) -- pipeline block added; §§ behavioral contracts
  (§1, §4, §10, §16, §19) cite pipeline threading by axis name; TABLE FORMAT CONTRACT
  schema notes do NOT. C-48 PASS, C-49 FAIL (schema leg missing). Predicted: 285/295.

- V-04: Output format + Phrasing register (two-axis) -- schema notes + behavioral §§
  both cite pipeline threading by axis name; pipeline contract describes execution
  positions but does not explicitly name the TABLE FORMAT CONTRACT fields or §§ contracts
  it governs. C-48 PASS, C-49 PASS. Predicted: 295/295.

- V-05: Output format + Phrasing register + Inertia framing (three-axis) -- V-04 plus
  explicit pipeline-to-(schema+behavioral) back-references: each axis block in the
  §0-CID PIPELINE THREADING CONTRACT names the TABLE FORMAT CONTRACT field it governs
  and the §§ behavioral contract that enforces it. C-48 PASS, C-49 PASS; introduces the
  three-way explicit naming pattern that may generate a criterion in v18.
  Predicted: 295/295.

**R19 single-axis predictions:**
- V-01: C-44+C-45+C-47+C-48 PASS, C-46/C-49 FAIL. Score: 285/295
- V-02: C-44+C-45+C-47+C-48 PASS, C-46/C-49 FAIL. Score: 285/295
- V-03: C-44+C-45+C-47+C-48 PASS, C-46/C-49 FAIL. Score: 285/295

**R19 two-axis and three-axis predictions:**
- V-04: C-44+C-45+C-47+C-48+C-49 PASS, C-46 FAIL. Score: 295/295
- V-05: C-44+C-45+C-47+C-48+C-49 PASS, C-46 FAIL. Score: 295/295

**C-48 isolation (V-01):** Does the pipeline contract block -- four named axes, correct
§8 ordering, §6 exclusion update -- satisfy C-48 with no schema or behavioral cross-refs
in the TABLE FORMAT CONTRACT or §§ contracts? C-49 FAIL because neither layer cites the
pipeline by axis name.

**C-49 leg isolation (V-02 vs V-03):** V-02 tests whether schema-layer cross-refs alone
move C-49; V-03 tests whether behavioral-layer cross-refs alone do. Both should FAIL C-49
because the criterion requires both layers simultaneously.

**C-49 two-leg threshold (V-04):** Both schema notes and behavioral §§ contracts cite
pipeline by axis name (same structure that earned C-49 PASS in R18 V-05). Pipeline
contract describes execution positions; does not explicitly back-name its downstream
schema fields and §§ contracts. Predicted PASS based on R18 V-05 structural precedent.

**C-49 explicit back-ref pattern (V-05):** Adds pipeline-to-(schema+behavioral) explicit
naming: each axis block in §0-CID PIPELINE THREADING CONTRACT names the TABLE FORMAT
CONTRACT field and §§ behavioral contract it governs. A pipeline-contract auditor can
see both schema and behavioral layers without reading other blocks. This is the new
structural pattern R19 introduces that V-04 lacks.

---

## V-01

**Axis**: Inertia framing -- §0-CID PIPELINE THREADING CONTRACT block added as
named pre-committed preamble block; TABLE FORMAT CONTRACT schema notes do NOT cite
pipeline threading by axis name; §§ behavioral contracts do NOT cite pipeline threading
by axis name; C-48 PASS, C-49 FAIL

**Hypothesis**: R18 V-04 has STATUS QUO FRAMING CONTRACT (§0-CID registry) + TABLE
FORMAT CONTRACT + dual-path behavioral §§ enforcement but no §0-CID PIPELINE THREADING
CONTRACT block. C-48 failed entirely because no such block existed. V-01 R19 adds the
minimal C-48 structure: a named block between STATUS QUO FRAMING CONTRACT and TABLE
FORMAT CONTRACT, four axes (A-D) declared as pre-committed requirements, §8 ordering
updated, §6 exclusion updated. TABLE FORMAT CONTRACT schema notes still reference
"§0-CID value from STATUS QUO FRAMING CONTRACT" but do not cite the pipeline contract
by axis name. §§ behavioral contracts reference "§0-CID from STATUS QUO FRAMING
CONTRACT registry" but do not cite the pipeline contract by axis name. The test: does
the block's existence and axis enumeration alone satisfy C-48, independent of schema
or behavioral cross-referencing? C-49 FAIL because neither TABLE FORMAT CONTRACT schema
notes nor §§ behavioral contracts contain pipeline axis citations.
Predicted score: 285/295.

---

You are running `/org-review`.

Inputs:
```
{{artifact_id}}: [artifact name or path under review]
{{depth}}: [standard | deep | quick]
{{reviewer_set}}: [auto | all | comma-separated role names from .roles/]
```

Acknowledge injected values before executing any section.

---

### STATUS QUO FRAMING CONTRACT (inertia-advocate pre-commitment)

Before table schemas or behavioral contracts are declared, register the no-build
commitments that justify not building {{artifact_id}}. These §0-CID values are the
ground truth for all §0-CID pipeline axes.

```
| §0-CID | Status Quo Commitment (why not building is acceptable) | Strength |
|--------|--------------------------------------------------------|----------|
| §0-C01 | [Existing capability or process covering this need]     | [H/M/L]  |
| §0-C02 | [Cost / risk / complexity argument for status quo]      | [H/M/L]  |
| §0-C03 | [Additional no-build strength claim as needed]          | [H/M/L]  |
```

Populate with artifact-specific values before any other section. Every CH-ID must
trace to a named §0-CID. Every finding must carry a named F-ID.

---

### §0-CID PIPELINE THREADING CONTRACT (four-axis pre-commitment)

The §0-CID values registered in STATUS QUO FRAMING CONTRACT flow through four
structural positions in this review. Each axis is a pre-committed requirement:

**Axis A -- CH-ID §0 Grounding citations** (at CH-ID REGISTRATION TABLE):
Every CH-ID §0 Grounding column value MUST cite a named §0-CID from the STATUS
QUO FRAMING CONTRACT registry. Generic preamble §§ section citations are not
permitted as §0 Grounding values.

**Axis B -- NH Dimension Table Column A initialization** (at BRACKET OPENING):
Column A values in the NH Dimension Comparison Table MUST be initialized from
STATUS QUO FRAMING CONTRACT §0-CID strength ratings. The §0-CID commitments
constitute the status-quo baseline; Column A scores reflect the claimed strength
of those commitments on each dimension.

**Axis C -- BRACKET CLOSING OVERRIDE justification** (if OVERRIDE INVOKED: YES):
Any BRACKET CLOSING OVERRIDE declaration MUST name the specific §0-CID commitment
being superseded (e.g., "OVERRIDE: domain evidence demonstrates §0-C02 cost
argument no longer holds given [evidence]"). A generic justification without
§0-CID citation does not satisfy this contract.

**Axis D -- PRIMARY DRIVER attribution** (at DISPOSITION):
When PRIMARY DRIVER is NULL HYPOTHESIS or BRACKET CLOSING OVERRIDE, the
`Primary Driver:` field MUST cite the §0-CID value(s) that drove the attribution
(e.g., "Primary Driver: NULL HYPOTHESIS (§0-C01 cost argument prevails)").
CONSENSUS and DOMAIN-driven attributions do not require §0-CID citation.

All four axes must be populated before the review is considered complete.

---

### TABLE FORMAT CONTRACT

All structured tables conform to schemas declared here. Required fields are mandatory
on every row.

**Finding Table** (every reviewer section):
```
| F-ID | Severity | Surface | Finding | Recommendation |
```
`F-ID`: named stable identifier (F-01, F-02, ...). NOT positional. `Severity`:
HIGH / MEDIUM / LOW. All downstream references use F-ID values.

**CH-ID Challenge Table** (before BRACKET OPENING):
```
| CH-ID | Challenge Statement | §0 Grounding | [Section response columns] |
```
`§0 Grounding`: required. Cites the §0-CID value from STATUS QUO FRAMING CONTRACT
(e.g., "§0-C01 -- tests whether existing capability argument holds"). Populated at
registration time. Challenges without a §0-CID citation are invalid.

**NH Dimension Scores Sub-table** (per DOMAIN and LIFECYCLE section):
```
| Dimension | B: Proposed-Build | C: Best-Non-Build-Alt |
```

**NH Dimension Comparison Table** (BRACKET OPENING and BRACKET CLOSING):
```
| Dimension | A: Status-Quo | B: Proposed-Build | C: Best-Non-Build-Alt | Delta B-A | Delta B-C |
```
Column A values initialized from STATUS QUO FRAMING CONTRACT §0-CID strength ratings.

**LOCAL GATE LEDGER ROW** (per verdict-emitting section):
```
| Gate Verdict | Section Severity | Class | F-ID(s) sourcing this verdict |
```

**MASTER ACTION REGISTER ROW**:
```
| F-ID | Gate Verdict | Class | Section | Finding Summary | Recommendation |
```

---

### §§ PREAMBLE CONTRACTS

**§1 DISPOSITION ALGEBRA (C-10, C-02)**
HIGH = blocks; MEDIUM = conditions; LOW = advisory.
FAIL -> BLOCKED | >= 1 CONDITIONAL, no FAIL -> CONDITIONAL | all PASS -> READY.
OVERRIDE: OVERRIDE INVOKED: YES | NO in BRACKET CLOSING. If YES, name the §0-CID
commitment being superseded.

**§2 CLASS DERIVATION CONTRACT (C-12)**
FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY (optional).
No editorial class assignment at assembly time.

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23)**
Three alternatives (A, B, C). g_null = PASS iff delta_B_A > 0 AND delta_B_C > 0.
g_null = CONDITIONAL iff exactly one delta > 0. g_null = FAIL iff both <= 0.

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
g_null(initial) [BRACKET OPENING] -> g_null(post-domain) [SATURATION CHECK]
-> g_null(final) [BRACKET CLOSING]. GClose = g_null(final) or OVERRIDE INVOKED: YES
with named §0-CID commitment.

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21)**
Universal coverage: BRACKET OPENING + all DOMAIN + LIFECYCLE + BRACKET CLOSING.
Schema per TABLE FORMAT CONTRACT. Verbatim copy to MASTER ACTION REGISTER.

**§6 NON-VERDICT SECTION EXCLUSION (C-25)**
No gate ledger row from: STATUS QUO FRAMING CONTRACT, §0-CID PIPELINE THREADING
CONTRACT, TABLE FORMAT CONTRACT, §§ preamble, scope, CH-ID registration, CH-ID
saturation check, scope coverage reconciliation, lens coverage table.

**§7 VERBATIM ASSEMBLY PROHIBITION (C-20)**
MASTER ACTION REGISTER: verbatim copy. Re-derivation prohibited.

**§8 SECTION ORDER CONTRACT (C-26)** -- immutable:
```
[STATUS QUO FRAMING CONTRACT -- pre-execution, complete]
[§0-CID PIPELINE THREADING CONTRACT -- pre-execution, complete]
[TABLE FORMAT CONTRACT -- pre-execution, complete]
[§§ PREAMBLE -- pre-execution, complete]
1. Scope Declaration      2. CH-ID Registration     3. Bracket Opening
4. Domain Reviewers       5. CH-ID Saturation Check  6. Lifecycle Reviewer
7. Bracket Closing        8. Scope Coverage Reconciliation
9. Lens Coverage Table    10. Disposition            11. Master Action Register
12. Cross-Role Signals
```

**§9 FINDING IDENTIFIER CONTRACT (C-42)**
Schema layer: Finding Table declared in TABLE FORMAT CONTRACT. F-ID column required.
Behavioral layer (independent enforcement path): Every finding row in every reviewer
section MUST carry a populated F-ID value. Omitting F-ID is a contract violation --
the section's LOCAL GATE LEDGER ROW must note the defect. Positional row references
are contract violations. All downstream references use F-ID values.

**§10 CH-ID CHALLENGE REGISTRATION (C-04, C-43)**
Schema layer: CH-ID Challenge Table declared in TABLE FORMAT CONTRACT. §0 Grounding
column required, populated at registration time with a §0-CID value.
Behavioral layer (independent enforcement path): Every CH-ID MUST carry a §0 Grounding
value naming a specific §0-CID from the STATUS QUO FRAMING CONTRACT registry. A §0
Grounding value citing a generic preamble §§ section ("§1 DISPOSITION ALGEBRA") rather
than a named §0-CID commitment does NOT satisfy this contract. CH-IDs without a valid
§0-CID citation are invalid and must be removed.

**§11 CH-ID SATURATION REQUIREMENT (C-27)**
SATURATED before LIFECYCLE. FULLY SATURATED at BRACKET CLOSING. BRACKET CLOSING
may not PASS when any CH-ID is UNSATURATED without waiver.

**§12 PER-FINDING SEVERITY AGGREGATION CONTRACT (C-30)**
Section Severity = worst(F-ID severities in section). No editorial assignment.

**§13 LENS COVERAGE TABLE PROTOCOL (C-31, C-33, C-34)**
Post-execution LENS COVERAGE TABLE: ADDRESSED/OPEN per lens.verify entry.
Applicability per entry. HIGH-applicability OPEN -> ADVISORY-OPEN-LENS items.
DOMAIN COVERAGE GAP-CHECK -> ADVISORY-GAP items.

**§14 SCOPE SURFACE DOMAIN ANNOTATION (C-36)**
Every IN-SCOPE surface: [DOMAIN: label] at enumeration time.

**§15 SCOPE COVERAGE GATE PROTOCOL (C-29)**
Post-bracket-closing reconciliation. GAP surfaces -> ADVISORY-GAP. No ledger row.

**§16 NH DIMENSION TABLE CONTRACT (C-35, C-37, C-38)**
BRACKET OPENING: NH Dimension Comparison Table per TABLE FORMAT CONTRACT. Column A
values initialized from STATUS QUO FRAMING CONTRACT §0-CID strength ratings. >= 3
dimensions. g_null(initial) derivable from Delta B-A and Delta B-C alone. BRACKET
CLOSING: re-populate columns B and C. g_null(final) derivable from revised values alone.

**§17 NH TABLE AGGREGATION RULE WITH LIFECYCLE EXTENSION (C-39, C-40, C-41)**
Column A: challenger's §0-CID-initialized opening values, unchanged.
Column B: avg(all DOMAIN B scores + LIFECYCLE B score).
Column C: avg(all DOMAIN C scores + LIFECYCLE C score).

DOMAIN NH SCORE EMISSION (C-40): every DOMAIN section emits NH Dimension Scores
sub-table per TABLE FORMAT CONTRACT before its LOCAL GATE LEDGER ROW.

LIFECYCLE NH SCORE EMISSION (C-41): LIFECYCLE section emits NH Dimension Scores
sub-table per TABLE FORMAT CONTRACT before its LOCAL GATE LEDGER ROW. Same dimensions
as §16 table. BRACKET CLOSING reads LIFECYCLE sub-table alongside DOMAIN sub-tables.
No prose extraction in the NH aggregation chain.

**§18 DOMAIN-AGGREGATE FORMULA (C-24)**
G_domain_agg = median(all DOMAIN gate verdicts). Labeled input to BRACKET CLOSING.

**§19 PRIMARY DRIVER DERIVATION CONTRACT (C-32)**
Precedence: BRACKET CLOSING OVERRIDE > NULL HYPOTHESIS > DOMAIN [first FAIL] >
LIFECYCLE [FAIL] > DOMAIN [first CONDITIONAL] > LIFECYCLE [CONDITIONAL] > CONSENSUS.
When PRIMARY DRIVER is NULL HYPOTHESIS or BRACKET CLOSING OVERRIDE, cite the §0-CID
value(s) driving the attribution. Emit `Primary Driver: [value]` at DISPOSITION.

**§20 DEPTH MODE ACKNOWLEDGMENT (C-08)**
deep: all roles. standard: relevant + rationale. quick: >= 3 + note.

---

Execute sections per §8. STATUS QUO FRAMING CONTRACT §0-CID registry is the ground
truth for §0-CID pipeline axes. TABLE FORMAT CONTRACT schemas and §§ behavioral
contracts are complementary and independently auditable. Before emitting DISPOSITION,
confirm four-axis §0-CID data flow:

```
Axis A (CH-ID §0 Grounding -- §0-CID citations):       [YES/NO]
Axis B (NH Column A -- §0-CID strength initialization): [YES/NO]
Axis C (BRACKET CLOSING OVERRIDE -- §0-CID named):     [YES/NO/NA]
Axis D (PRIMARY DRIVER -- §0-CID cited):                [YES/NO/NA]
```

Acknowledge {{artifact_id}}, {{depth}}, {{reviewer_set}} before Step 1.

---

### EXECUTION

**Step 1: Acknowledge inputs**
```
Artifact: {{artifact_id}}
Depth: {{depth}}
Reviewer set: {{reviewer_set}}
Role selection rationale: [state if depth=standard]
```

**Step 2: SCOPE DECLARATION**
Enumerate all IN-SCOPE surfaces with [DOMAIN: label] per §14. State OUT-OF-SCOPE.

**Step 3: CH-ID REGISTRATION TABLE**
Register all challenges per §10. §0 Grounding column: cite §0-CID value from STATUS
QUO FRAMING CONTRACT registry (Axis A per §0-CID PIPELINE THREADING CONTRACT).
Challenges without §0-CID citation are invalid.

**Step 4: BRACKET OPENING**
- State null hypothesis: what the team does today, why it is acceptable.
- Populate NH Dimension Comparison Table: Column A from §0-CID strength ratings
  (Axis B per §0-CID PIPELINE THREADING CONTRACT). >= 3 dimensions.
  Emit g_null(initial) as labeled field.
- Emit LOCAL GATE LEDGER ROW per TABLE FORMAT CONTRACT schema.

**Step 5: DOMAIN REVIEWER SECTIONS** (one per role, manifest order)
- State role name and lens (one sentence).
- Produce finding rows per Finding Table schema (§9 schema + behavioral layers).
- Respond to relevant CH-IDs.
- Emit NH Dimension Scores sub-table per TABLE FORMAT CONTRACT schema.
- Emit LOCAL GATE LEDGER ROW. Section Severity = worst(finding severities) per §12.

**Step 6: CH-ID SATURATION CHECK**
- Verify SATURATED tier. Emit g_null(post-domain) per §4 Stage 2. No gate ledger row.

**Step 7: LIFECYCLE REVIEWER SECTION**
- Evaluate lifecycle phases (creation, active use, change, deprecation, removal).
- Produce finding rows per Finding Table schema.
- Respond to relevant CH-IDs.
- Emit NH Dimension Scores sub-table per TABLE FORMAT CONTRACT schema.
- Emit LOCAL GATE LEDGER ROW with g_lifecycle labeled.

**Step 8: BRACKET CLOSING**
- Receive G_domain_agg (§18), g_lifecycle, all domain/lifecycle verdicts.
- Re-populate NH Dimension Comparison Table columns B and C per §17.
- Derive g_null(final) from revised table per §3 (Stage 3 of §4).
- Emit OVERRIDE INVOKED: YES | NO. If YES: name §0-CID being superseded (Axis C).
- Emit LOCAL GATE LEDGER ROW.

**Step 9: SCOPE COVERAGE RECONCILIATION** (per §15; no gate ledger row)

**Step 10: LENS COVERAGE TABLE** (per §13; no gate ledger row)

**Step 11: DISPOSITION**
- Apply §1 DISPOSITION ALGEBRA to gate verdict vector.
- Emit `DISPOSITION: READY | CONDITIONAL | BLOCKED` as labeled field.
- Emit `Primary Driver: [value]` per §19. If NULL HYPOTHESIS or OVERRIDE:
  cite §0-CID value(s) (Axis D per §0-CID PIPELINE THREADING CONTRACT).

**Step 12: MASTER ACTION REGISTER**
Verbatim copy of LOCAL GATE LEDGER ROWS (§7). Append ADVISORY-GAP and
ADVISORY-OPEN-LENS items. No re-derivation.

**Step 13: CROSS-ROLE SIGNALS**
Synthesis narrative. Name >= 1 cross-role conflict or convergence. Reference all
three g_null stages. Explain the disposition.

---

## V-02

**Axis**: Output format -- §0-CID PIPELINE THREADING CONTRACT block added; TABLE
FORMAT CONTRACT schema notes for §0-CID-related fields cite pipeline threading by
axis name; §§ behavioral contracts do NOT cite pipeline by axis name; C-48 PASS,
C-49 FAIL (behavioral leg missing)

**Hypothesis**: V-01 R19 isolates C-48 (pipeline block only, no cross-refs). V-02
isolates the schema-leg of C-49 by adding pipeline axis citations to TABLE FORMAT
CONTRACT schema notes for the two §0-CID-bearing fields: CH-ID Challenge Table §0
Grounding cites Axis A by name; NH Dimension Comparison Table Column A note cites
Axis B by name. The §§ behavioral contracts (§10, §16, §19) still reference "§0-CID
from STATUS QUO FRAMING CONTRACT" without citing the pipeline contract by axis name.
The test: does a schema-only pipeline cross-reference (without behavioral
cross-referencing) achieve C-49 PASS? It should not -- C-49 requires both layers.
The gap is the behavioral leg: §10's independent enforcement path names the registry
but not the pipeline contract. Predicted score: 285/295.

---

You are running `/org-review`.

Inputs:
```
{{artifact_id}}: [artifact name or path under review]
{{depth}}: [standard | deep | quick]
{{reviewer_set}}: [auto | all | comma-separated role names from .roles/]
```

Acknowledge injected values before executing any section.

---

### STATUS QUO FRAMING CONTRACT (inertia-advocate pre-commitment)

Before table schemas or behavioral contracts are declared, register the no-build
commitments that justify not building {{artifact_id}}. These §0-CID values are the
ground truth for all §0-CID pipeline axes.

```
| §0-CID | Status Quo Commitment (why not building is acceptable) | Strength |
|--------|--------------------------------------------------------|----------|
| §0-C01 | [Existing capability or process covering this need]     | [H/M/L]  |
| §0-C02 | [Cost / risk / complexity argument for status quo]      | [H/M/L]  |
| §0-C03 | [Additional no-build strength claim as needed]          | [H/M/L]  |
```

Populate with artifact-specific values before any other section. Every CH-ID must
trace to a named §0-CID. Every finding must carry a named F-ID.

---

### §0-CID PIPELINE THREADING CONTRACT (four-axis pre-commitment)

The §0-CID values registered in STATUS QUO FRAMING CONTRACT flow through four
structural positions in this review. Each axis is a pre-committed requirement:

**Axis A -- CH-ID §0 Grounding citations** (at CH-ID REGISTRATION TABLE):
Every CH-ID §0 Grounding column value MUST cite a named §0-CID from the STATUS
QUO FRAMING CONTRACT registry. Generic preamble §§ section citations are not
permitted as §0 Grounding values.

**Axis B -- NH Dimension Table Column A initialization** (at BRACKET OPENING):
Column A values in the NH Dimension Comparison Table MUST be initialized from
STATUS QUO FRAMING CONTRACT §0-CID strength ratings. The §0-CID commitments
constitute the status-quo baseline; Column A scores reflect the claimed strength
of those commitments on each dimension.

**Axis C -- BRACKET CLOSING OVERRIDE justification** (if OVERRIDE INVOKED: YES):
Any BRACKET CLOSING OVERRIDE declaration MUST name the specific §0-CID commitment
being superseded (e.g., "OVERRIDE: domain evidence demonstrates §0-C02 cost
argument no longer holds given [evidence]"). A generic justification without
§0-CID citation does not satisfy this contract.

**Axis D -- PRIMARY DRIVER attribution** (at DISPOSITION):
When PRIMARY DRIVER is NULL HYPOTHESIS or BRACKET CLOSING OVERRIDE, the
`Primary Driver:` field MUST cite the §0-CID value(s) that drove the attribution
(e.g., "Primary Driver: NULL HYPOTHESIS (§0-C01 cost argument prevails)").
CONSENSUS and DOMAIN-driven attributions do not require §0-CID citation.

All four axes must be populated before the review is considered complete.

---

### TABLE FORMAT CONTRACT

All structured tables conform to schemas declared here. Required fields are mandatory
on every row.

**Finding Table** (every reviewer section):
```
| F-ID | Severity | Surface | Finding | Recommendation |
```
`F-ID`: named stable identifier (F-01, F-02, ...). NOT positional. `Severity`:
HIGH / MEDIUM / LOW. All downstream references use F-ID values.

**CH-ID Challenge Table** (before BRACKET OPENING):
```
| CH-ID | Challenge Statement | §0 Grounding | [Section response columns] |
```
`§0 Grounding`: required. Cites the §0-CID value from STATUS QUO FRAMING CONTRACT
per §0-CID PIPELINE THREADING CONTRACT Axis A (e.g., "§0-C01 -- tests whether
existing capability argument holds"). Populated at registration time. Challenges
without a §0-CID Axis A citation are invalid.

**NH Dimension Scores Sub-table** (per DOMAIN and LIFECYCLE section):
```
| Dimension | B: Proposed-Build | C: Best-Non-Build-Alt |
```

**NH Dimension Comparison Table** (BRACKET OPENING and BRACKET CLOSING):
```
| Dimension | A: Status-Quo | B: Proposed-Build | C: Best-Non-Build-Alt | Delta B-A | Delta B-C |
```
Column A values initialized from STATUS QUO FRAMING CONTRACT §0-CID strength ratings
per §0-CID PIPELINE THREADING CONTRACT Axis B.

**LOCAL GATE LEDGER ROW** (per verdict-emitting section):
```
| Gate Verdict | Section Severity | Class | F-ID(s) sourcing this verdict |
```

**MASTER ACTION REGISTER ROW**:
```
| F-ID | Gate Verdict | Class | Section | Finding Summary | Recommendation |
```

---

### §§ PREAMBLE CONTRACTS

**§1 DISPOSITION ALGEBRA (C-10, C-02)**
HIGH = blocks; MEDIUM = conditions; LOW = advisory.
FAIL -> BLOCKED | >= 1 CONDITIONAL, no FAIL -> CONDITIONAL | all PASS -> READY.
OVERRIDE: OVERRIDE INVOKED: YES | NO in BRACKET CLOSING. If YES, name the §0-CID
commitment being superseded.

**§2 CLASS DERIVATION CONTRACT (C-12)**
FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY (optional).
No editorial class assignment at assembly time.

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23)**
Three alternatives (A, B, C). g_null = PASS iff delta_B_A > 0 AND delta_B_C > 0.
g_null = CONDITIONAL iff exactly one delta > 0. g_null = FAIL iff both <= 0.

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
g_null(initial) [BRACKET OPENING] -> g_null(post-domain) [SATURATION CHECK]
-> g_null(final) [BRACKET CLOSING]. GClose = g_null(final) or OVERRIDE INVOKED: YES
with named §0-CID commitment.

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21)**
Universal coverage: BRACKET OPENING + all DOMAIN + LIFECYCLE + BRACKET CLOSING.
Schema per TABLE FORMAT CONTRACT. Verbatim copy to MASTER ACTION REGISTER.

**§6 NON-VERDICT SECTION EXCLUSION (C-25)**
No gate ledger row from: STATUS QUO FRAMING CONTRACT, §0-CID PIPELINE THREADING
CONTRACT, TABLE FORMAT CONTRACT, §§ preamble, scope, CH-ID registration, CH-ID
saturation check, scope coverage reconciliation, lens coverage table.

**§7 VERBATIM ASSEMBLY PROHIBITION (C-20)**
MASTER ACTION REGISTER: verbatim copy. Re-derivation prohibited.

**§8 SECTION ORDER CONTRACT (C-26)** -- immutable:
```
[STATUS QUO FRAMING CONTRACT -- pre-execution, complete]
[§0-CID PIPELINE THREADING CONTRACT -- pre-execution, complete]
[TABLE FORMAT CONTRACT -- pre-execution, complete]
[§§ PREAMBLE -- pre-execution, complete]
1. Scope Declaration      2. CH-ID Registration     3. Bracket Opening
4. Domain Reviewers       5. CH-ID Saturation Check  6. Lifecycle Reviewer
7. Bracket Closing        8. Scope Coverage Reconciliation
9. Lens Coverage Table    10. Disposition            11. Master Action Register
12. Cross-Role Signals
```

**§9 FINDING IDENTIFIER CONTRACT (C-42)**
Schema layer: Finding Table declared in TABLE FORMAT CONTRACT. F-ID column required.
Behavioral layer (independent enforcement path): Every finding row in every reviewer
section MUST carry a populated F-ID value. Omitting F-ID is a contract violation --
the section's LOCAL GATE LEDGER ROW must note the defect. Positional row references
are contract violations. All downstream references use F-ID values.

**§10 CH-ID CHALLENGE REGISTRATION (C-04, C-43)**
Schema layer: CH-ID Challenge Table declared in TABLE FORMAT CONTRACT. §0 Grounding
column required, populated at registration time with a §0-CID value.
Behavioral layer (independent enforcement path): Every CH-ID MUST carry a §0 Grounding
value naming a specific §0-CID from the STATUS QUO FRAMING CONTRACT registry. A §0
Grounding value citing a generic preamble §§ section ("§1 DISPOSITION ALGEBRA") rather
than a named §0-CID commitment does NOT satisfy this contract. CH-IDs without a valid
§0-CID citation are invalid and must be removed.

**§11 CH-ID SATURATION REQUIREMENT (C-27)**
SATURATED before LIFECYCLE. FULLY SATURATED at BRACKET CLOSING. BRACKET CLOSING
may not PASS when any CH-ID is UNSATURATED without waiver.

**§12 PER-FINDING SEVERITY AGGREGATION CONTRACT (C-30)**
Section Severity = worst(F-ID severities in section). No editorial assignment.

**§13 LENS COVERAGE TABLE PROTOCOL (C-31, C-33, C-34)**
Post-execution LENS COVERAGE TABLE: ADDRESSED/OPEN per lens.verify entry.
Applicability per entry. HIGH-applicability OPEN -> ADVISORY-OPEN-LENS items.
DOMAIN COVERAGE GAP-CHECK -> ADVISORY-GAP items.

**§14 SCOPE SURFACE DOMAIN ANNOTATION (C-36)**
Every IN-SCOPE surface: [DOMAIN: label] at enumeration time.

**§15 SCOPE COVERAGE GATE PROTOCOL (C-29)**
Post-bracket-closing reconciliation. GAP surfaces -> ADVISORY-GAP. No ledger row.

**§16 NH DIMENSION TABLE CONTRACT (C-35, C-37, C-38)**
BRACKET OPENING: NH Dimension Comparison Table per TABLE FORMAT CONTRACT. Column A
values initialized from STATUS QUO FRAMING CONTRACT §0-CID strength ratings. >= 3
dimensions. g_null(initial) derivable from Delta B-A and Delta B-C alone. BRACKET
CLOSING: re-populate columns B and C. g_null(final) derivable from revised values alone.

**§17 NH TABLE AGGREGATION RULE WITH LIFECYCLE EXTENSION (C-39, C-40, C-41)**
Column A: challenger's §0-CID-initialized opening values, unchanged.
Column B: avg(all DOMAIN B scores + LIFECYCLE B score).
Column C: avg(all DOMAIN C scores + LIFECYCLE C score).

DOMAIN NH SCORE EMISSION (C-40): every DOMAIN section emits NH Dimension Scores
sub-table per TABLE FORMAT CONTRACT before its LOCAL GATE LEDGER ROW.

LIFECYCLE NH SCORE EMISSION (C-41): LIFECYCLE section emits NH Dimension Scores
sub-table per TABLE FORMAT CONTRACT before its LOCAL GATE LEDGER ROW. Same dimensions
as §16 table. BRACKET CLOSING reads LIFECYCLE sub-table alongside DOMAIN sub-tables.
No prose extraction in the NH aggregation chain.

**§18 DOMAIN-AGGREGATE FORMULA (C-24)**
G_domain_agg = median(all DOMAIN gate verdicts). Labeled input to BRACKET CLOSING.

**§19 PRIMARY DRIVER DERIVATION CONTRACT (C-32)**
Precedence: BRACKET CLOSING OVERRIDE > NULL HYPOTHESIS > DOMAIN [first FAIL] >
LIFECYCLE [FAIL] > DOMAIN [first CONDITIONAL] > LIFECYCLE [CONDITIONAL] > CONSENSUS.
When PRIMARY DRIVER is NULL HYPOTHESIS or BRACKET CLOSING OVERRIDE, cite the §0-CID
value(s) driving the attribution. Emit `Primary Driver: [value]` at DISPOSITION.

**§20 DEPTH MODE ACKNOWLEDGMENT (C-08)**
deep: all roles. standard: relevant + rationale. quick: >= 3 + note.

---

Execute sections per §8. TABLE FORMAT CONTRACT schema notes carry Axis A and Axis B
pipeline citations; §§ behavioral contracts are independently auditable without
reference to the pipeline contract. Before emitting DISPOSITION, confirm four-axis
§0-CID data flow:

```
Axis A (CH-ID §0 Grounding -- §0-CID citations):       [YES/NO]
Axis B (NH Column A -- §0-CID strength initialization): [YES/NO]
Axis C (BRACKET CLOSING OVERRIDE -- §0-CID named):     [YES/NO/NA]
Axis D (PRIMARY DRIVER -- §0-CID cited):                [YES/NO/NA]
```

Acknowledge {{artifact_id}}, {{depth}}, {{reviewer_set}} before Step 1.

---

### EXECUTION

Steps 1-13 as V-01. Step 3 CH-ID registration populates §0 Grounding citing §0-CID
value per Axis A (as declared in TABLE FORMAT CONTRACT CH-ID Challenge Table schema
note). Step 4 BRACKET OPENING Column A values populated per Axis B (as declared in
TABLE FORMAT CONTRACT NH Dimension Comparison Table Column A schema note).

---

## V-03

**Axis**: Phrasing register -- §0-CID PIPELINE THREADING CONTRACT block added; §§
behavioral contracts (§1, §4, §10, §16, §19) cite pipeline threading by axis name
where §0-CID requirements appear; TABLE FORMAT CONTRACT schema notes do NOT cite
pipeline by axis name; C-48 PASS, C-49 FAIL (schema leg missing)

**Hypothesis**: V-02 R19 isolates the schema leg of C-49 (TABLE FORMAT CONTRACT
notes cite pipeline) and should fail C-49 because the behavioral leg is absent.
V-03 tests the behavioral leg in isolation: §§ contracts (§1, §4, §10, §16, §19)
each add an explicit "per §0-CID PIPELINE THREADING CONTRACT Axis X" reference at
the point where they impose a §0-CID-related requirement. TABLE FORMAT CONTRACT
schema notes still say "cites the §0-CID value from STATUS QUO FRAMING CONTRACT"
without naming an axis. The test: does behavioral-only pipeline cross-referencing
achieve C-49? It should not -- C-49 requires both layers. The gap is the schema leg:
the TABLE FORMAT CONTRACT field definitions do not carry pipeline axis bindings.
Predicted score: 285/295.

---

You are running `/org-review`.

Inputs:
```
{{artifact_id}}: [artifact name or path under review]
{{depth}}: [standard | deep | quick]
{{reviewer_set}}: [auto | all | comma-separated role names from .roles/]
```

Acknowledge injected values before executing any section.

---

### STATUS QUO FRAMING CONTRACT (inertia-advocate pre-commitment)

Before table schemas or behavioral contracts are declared, register the no-build
commitments that justify not building {{artifact_id}}. These §0-CID values are the
ground truth for all §0-CID pipeline axes.

```
| §0-CID | Status Quo Commitment (why not building is acceptable) | Strength |
|--------|--------------------------------------------------------|----------|
| §0-C01 | [Existing capability or process covering this need]     | [H/M/L]  |
| §0-C02 | [Cost / risk / complexity argument for status quo]      | [H/M/L]  |
| §0-C03 | [Additional no-build strength claim as needed]          | [H/M/L]  |
```

Populate with artifact-specific values before any other section. Every CH-ID must
trace to a named §0-CID. Every finding must carry a named F-ID.

---

### §0-CID PIPELINE THREADING CONTRACT (four-axis pre-commitment)

The §0-CID values registered in STATUS QUO FRAMING CONTRACT flow through four
structural positions in this review. Each axis is a pre-committed requirement:

**Axis A -- CH-ID §0 Grounding citations** (at CH-ID REGISTRATION TABLE):
Every CH-ID §0 Grounding column value MUST cite a named §0-CID from the STATUS
QUO FRAMING CONTRACT registry. Generic preamble §§ section citations are not
permitted as §0 Grounding values.

**Axis B -- NH Dimension Table Column A initialization** (at BRACKET OPENING):
Column A values in the NH Dimension Comparison Table MUST be initialized from
STATUS QUO FRAMING CONTRACT §0-CID strength ratings. The §0-CID commitments
constitute the status-quo baseline; Column A scores reflect the claimed strength
of those commitments on each dimension.

**Axis C -- BRACKET CLOSING OVERRIDE justification** (if OVERRIDE INVOKED: YES):
Any BRACKET CLOSING OVERRIDE declaration MUST name the specific §0-CID commitment
being superseded (e.g., "OVERRIDE: domain evidence demonstrates §0-C02 cost
argument no longer holds given [evidence]"). A generic justification without
§0-CID citation does not satisfy this contract.

**Axis D -- PRIMARY DRIVER attribution** (at DISPOSITION):
When PRIMARY DRIVER is NULL HYPOTHESIS or BRACKET CLOSING OVERRIDE, the
`Primary Driver:` field MUST cite the §0-CID value(s) that drove the attribution
(e.g., "Primary Driver: NULL HYPOTHESIS (§0-C01 cost argument prevails)").
CONSENSUS and DOMAIN-driven attributions do not require §0-CID citation.

All four axes must be populated before the review is considered complete.

---

### TABLE FORMAT CONTRACT

All structured tables conform to schemas declared here. Required fields are mandatory
on every row.

**Finding Table** (every reviewer section):
```
| F-ID | Severity | Surface | Finding | Recommendation |
```
`F-ID`: named stable identifier (F-01, F-02, ...). NOT positional. `Severity`:
HIGH / MEDIUM / LOW. All downstream references use F-ID values.

**CH-ID Challenge Table** (before BRACKET OPENING):
```
| CH-ID | Challenge Statement | §0 Grounding | [Section response columns] |
```
`§0 Grounding`: required. Cites the §0-CID value from STATUS QUO FRAMING CONTRACT
(e.g., "§0-C01 -- tests whether existing capability argument holds"). Populated at
registration time. Challenges without a §0-CID citation are invalid.

**NH Dimension Scores Sub-table** (per DOMAIN and LIFECYCLE section):
```
| Dimension | B: Proposed-Build | C: Best-Non-Build-Alt |
```

**NH Dimension Comparison Table** (BRACKET OPENING and BRACKET CLOSING):
```
| Dimension | A: Status-Quo | B: Proposed-Build | C: Best-Non-Build-Alt | Delta B-A | Delta B-C |
```
Column A values initialized from STATUS QUO FRAMING CONTRACT §0-CID strength ratings.

**LOCAL GATE LEDGER ROW** (per verdict-emitting section):
```
| Gate Verdict | Section Severity | Class | F-ID(s) sourcing this verdict |
```

**MASTER ACTION REGISTER ROW**:
```
| F-ID | Gate Verdict | Class | Section | Finding Summary | Recommendation |
```

---

### §§ PREAMBLE CONTRACTS

**§1 DISPOSITION ALGEBRA (C-10, C-02)**
HIGH = blocks; MEDIUM = conditions; LOW = advisory.
FAIL -> BLOCKED | >= 1 CONDITIONAL, no FAIL -> CONDITIONAL | all PASS -> READY.
OVERRIDE: OVERRIDE INVOKED: YES | NO in BRACKET CLOSING. If YES, name the §0-CID
commitment being superseded per §0-CID PIPELINE THREADING CONTRACT Axis C.

**§2 CLASS DERIVATION CONTRACT (C-12)**
FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY (optional).
No editorial class assignment at assembly time.

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23)**
Three alternatives (A, B, C). g_null = PASS iff delta_B_A > 0 AND delta_B_C > 0.
g_null = CONDITIONAL iff exactly one delta > 0. g_null = FAIL iff both <= 0.

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
g_null(initial) [BRACKET OPENING] -> g_null(post-domain) [SATURATION CHECK]
-> g_null(final) [BRACKET CLOSING]. GClose = g_null(final) or OVERRIDE INVOKED: YES
with named §0-CID commitment per §0-CID PIPELINE THREADING CONTRACT Axis C.

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21)**
Universal coverage: BRACKET OPENING + all DOMAIN + LIFECYCLE + BRACKET CLOSING.
Schema per TABLE FORMAT CONTRACT. Verbatim copy to MASTER ACTION REGISTER.

**§6 NON-VERDICT SECTION EXCLUSION (C-25)**
No gate ledger row from: STATUS QUO FRAMING CONTRACT, §0-CID PIPELINE THREADING
CONTRACT, TABLE FORMAT CONTRACT, §§ preamble, scope, CH-ID registration, CH-ID
saturation check, scope coverage reconciliation, lens coverage table.

**§7 VERBATIM ASSEMBLY PROHIBITION (C-20)**
MASTER ACTION REGISTER: verbatim copy. Re-derivation prohibited.

**§8 SECTION ORDER CONTRACT (C-26)** -- immutable:
```
[STATUS QUO FRAMING CONTRACT -- pre-execution, complete]
[§0-CID PIPELINE THREADING CONTRACT -- pre-execution, complete]
[TABLE FORMAT CONTRACT -- pre-execution, complete]
[§§ PREAMBLE -- pre-execution, complete]
1. Scope Declaration      2. CH-ID Registration     3. Bracket Opening
4. Domain Reviewers       5. CH-ID Saturation Check  6. Lifecycle Reviewer
7. Bracket Closing        8. Scope Coverage Reconciliation
9. Lens Coverage Table    10. Disposition            11. Master Action Register
12. Cross-Role Signals
```

**§9 FINDING IDENTIFIER CONTRACT (C-42)**
Schema layer: Finding Table declared in TABLE FORMAT CONTRACT. F-ID column required.
Behavioral layer (independent enforcement path): Every finding row in every reviewer
section MUST carry a populated F-ID value. Omitting F-ID is a contract violation --
the section's LOCAL GATE LEDGER ROW must note the defect. Positional row references
are contract violations. All downstream references use F-ID values.

**§10 CH-ID CHALLENGE REGISTRATION (C-04, C-43)**
Schema layer: CH-ID Challenge Table declared in TABLE FORMAT CONTRACT. §0 Grounding
column required, populated at registration time with a §0-CID value.
Behavioral layer (independent enforcement path): Every CH-ID MUST carry a §0 Grounding
value naming a specific §0-CID from the STATUS QUO FRAMING CONTRACT registry per
§0-CID PIPELINE THREADING CONTRACT Axis A. A §0 Grounding value citing a generic
preamble §§ section does NOT satisfy this contract. CH-IDs without a valid §0-CID
citation are invalid and must be removed.

**§11 CH-ID SATURATION REQUIREMENT (C-27)**
SATURATED before LIFECYCLE. FULLY SATURATED at BRACKET CLOSING. BRACKET CLOSING
may not PASS when any CH-ID is UNSATURATED without waiver.

**§12 PER-FINDING SEVERITY AGGREGATION CONTRACT (C-30)**
Section Severity = worst(F-ID severities in section). No editorial assignment.

**§13 LENS COVERAGE TABLE PROTOCOL (C-31, C-33, C-34)**
Post-execution LENS COVERAGE TABLE: ADDRESSED/OPEN per lens.verify entry.
Applicability per entry. HIGH-applicability OPEN -> ADVISORY-OPEN-LENS items.
DOMAIN COVERAGE GAP-CHECK -> ADVISORY-GAP items.

**§14 SCOPE SURFACE DOMAIN ANNOTATION (C-36)**
Every IN-SCOPE surface: [DOMAIN: label] at enumeration time.

**§15 SCOPE COVERAGE GATE PROTOCOL (C-29)**
Post-bracket-closing reconciliation. GAP surfaces -> ADVISORY-GAP. No ledger row.

**§16 NH DIMENSION TABLE CONTRACT (C-35, C-37, C-38)**
BRACKET OPENING: NH Dimension Comparison Table per TABLE FORMAT CONTRACT. Column A
values initialized from STATUS QUO FRAMING CONTRACT §0-CID strength ratings per
§0-CID PIPELINE THREADING CONTRACT Axis B. >= 3 dimensions. g_null(initial) derivable
from Delta B-A and Delta B-C alone. BRACKET CLOSING: re-populate columns B and C.
g_null(final) derivable from revised values alone.

**§17 NH TABLE AGGREGATION RULE WITH LIFECYCLE EXTENSION (C-39, C-40, C-41)**
Column A: challenger's §0-CID-initialized opening values, unchanged.
Column B: avg(all DOMAIN B scores + LIFECYCLE B score).
Column C: avg(all DOMAIN C scores + LIFECYCLE C score).

DOMAIN NH SCORE EMISSION (C-40): every DOMAIN section emits NH Dimension Scores
sub-table per TABLE FORMAT CONTRACT before its LOCAL GATE LEDGER ROW.

LIFECYCLE NH SCORE EMISSION (C-41): LIFECYCLE section emits NH Dimension Scores
sub-table per TABLE FORMAT CONTRACT before its LOCAL GATE LEDGER ROW. Same dimensions
as §16 table. BRACKET CLOSING reads LIFECYCLE sub-table alongside DOMAIN sub-tables.
No prose extraction in the NH aggregation chain.

**§18 DOMAIN-AGGREGATE FORMULA (C-24)**
G_domain_agg = median(all DOMAIN gate verdicts). Labeled input to BRACKET CLOSING.

**§19 PRIMARY DRIVER DERIVATION CONTRACT (C-32)**
Precedence: BRACKET CLOSING OVERRIDE (cite §0-CID overridden per §0-CID PIPELINE
THREADING CONTRACT Axis C) > NULL HYPOTHESIS (cite §0-CID held per §0-CID PIPELINE
THREADING CONTRACT Axis D) > DOMAIN [first FAIL] > LIFECYCLE [FAIL] > DOMAIN [first
CONDITIONAL] > LIFECYCLE [CONDITIONAL] > CONSENSUS. Emit `Primary Driver: [value]`
at DISPOSITION. When driver is NULL HYPOTHESIS or BRACKET CLOSING OVERRIDE, append
the §0-CID citation per §0-CID PIPELINE THREADING CONTRACT Axis D.

**§20 DEPTH MODE ACKNOWLEDGMENT (C-08)**
deep: all roles. standard: relevant + rationale. quick: >= 3 + note.

---

Execute sections per §8. §§ behavioral contracts carry Axis A, B, C, D pipeline
citations; TABLE FORMAT CONTRACT schemas are independently auditable without reference
to the pipeline contract. Before emitting DISPOSITION, confirm four-axis §0-CID data
flow:

```
Axis A (CH-ID §0 Grounding -- §0-CID citations):       [YES/NO]
Axis B (NH Column A -- §0-CID strength initialization): [YES/NO]
Axis C (BRACKET CLOSING OVERRIDE -- §0-CID named):     [YES/NO/NA]
Axis D (PRIMARY DRIVER -- §0-CID cited):                [YES/NO/NA]
```

Acknowledge {{artifact_id}}, {{depth}}, {{reviewer_set}} before Step 1.

---

### EXECUTION

Steps 1-13 as V-01. Step 3 CH-ID registration populates §0 Grounding with §0-CID
value per §10 behavioral contract (Axis A per §0-CID PIPELINE THREADING CONTRACT).
Step 4 BRACKET OPENING Column A values populated per §16 (Axis B). Step 8 BRACKET
CLOSING OVERRIDE names §0-CID per §1 Axis C if invoked. Step 11 DISPOSITION Primary
Driver cites §0-CID per §19 Axis D when applicable.

---

## V-04

**Axis**: Output format + Phrasing register (two-axis) -- §0-CID PIPELINE THREADING
CONTRACT block; TABLE FORMAT CONTRACT schema notes cite pipeline by axis name (V-02);
§§ behavioral contracts cite pipeline by axis name (V-03); pipeline contract describes
execution positions but does not explicitly name the TABLE FORMAT CONTRACT fields or
§§ behavioral contracts it governs; C-48 PASS, C-49 PASS

**Hypothesis**: V-02 isolates schema-only cross-refs (C-49 FAIL). V-03 isolates
behavioral-only cross-refs (C-49 FAIL). V-04 combines both: every §0-CID-bearing
TABLE FORMAT CONTRACT schema note carries an Axis citation, and every §0-CID-related
§§ behavioral contract also carries an Axis citation. This is the same two-direction
cross-referencing architecture that earned C-49 PASS in R18 V-05. The pipeline
contract's axis definitions describe execution positions and constraints (Axis A: "at
CH-ID REGISTRATION TABLE"; Axis B: "at BRACKET OPENING"), which implicitly identifies
the schema fields and behavioral contracts governed -- but without naming them as
explicit back-references. Predicted: 295/295 based on structural parity with R18 V-05's
C-49 PASS pattern. C-46 FAIL is intentional: §0-CID threading is pre-declared but not
tested against all four axes in execution (that is C-46's requirement, not C-48/C-49).

---

You are running `/org-review`.

Inputs:
```
{{artifact_id}}: [artifact name or path under review]
{{depth}}: [standard | deep | quick]
{{reviewer_set}}: [auto | all | comma-separated role names from .roles/]
```

Acknowledge injected values before executing any section.

---

### STATUS QUO FRAMING CONTRACT (inertia-advocate pre-commitment)

Before table schemas or behavioral contracts are declared, register the no-build
commitments that justify not building {{artifact_id}}. These §0-CID values are the
ground truth for all §0-CID pipeline axes.

```
| §0-CID | Status Quo Commitment (why not building is acceptable) | Strength |
|--------|--------------------------------------------------------|----------|
| §0-C01 | [Existing capability or process covering this need]     | [H/M/L]  |
| §0-C02 | [Cost / risk / complexity argument for status quo]      | [H/M/L]  |
| §0-C03 | [Additional no-build strength claim as needed]          | [H/M/L]  |
```

Populate with artifact-specific values before any other section. Every CH-ID must
trace to a named §0-CID. Every finding must carry a named F-ID.

---

### §0-CID PIPELINE THREADING CONTRACT (four-axis pre-commitment)

The §0-CID values registered in STATUS QUO FRAMING CONTRACT flow through four
structural positions in this review. Each axis is a pre-committed requirement:

**Axis A -- CH-ID §0 Grounding citations** (at CH-ID REGISTRATION TABLE):
Every CH-ID §0 Grounding column value MUST cite a named §0-CID from the STATUS
QUO FRAMING CONTRACT registry. Generic preamble §§ section citations are not
permitted as §0 Grounding values.

**Axis B -- NH Dimension Table Column A initialization** (at BRACKET OPENING):
Column A values in the NH Dimension Comparison Table MUST be initialized from
STATUS QUO FRAMING CONTRACT §0-CID strength ratings. The §0-CID commitments
constitute the status-quo baseline; Column A scores reflect the claimed strength
of those commitments on each dimension.

**Axis C -- BRACKET CLOSING OVERRIDE justification** (if OVERRIDE INVOKED: YES):
Any BRACKET CLOSING OVERRIDE declaration MUST name the specific §0-CID commitment
being superseded (e.g., "OVERRIDE: domain evidence demonstrates §0-C02 cost
argument no longer holds given [evidence]"). A generic justification without
§0-CID citation does not satisfy this contract.

**Axis D -- PRIMARY DRIVER attribution** (at DISPOSITION):
When PRIMARY DRIVER is NULL HYPOTHESIS or BRACKET CLOSING OVERRIDE, the
`Primary Driver:` field MUST cite the §0-CID value(s) that drove the attribution
(e.g., "Primary Driver: NULL HYPOTHESIS (§0-C01 cost argument prevails)").
CONSENSUS and DOMAIN-driven attributions do not require §0-CID citation.

All four axes must be populated before the review is considered complete.

---

### TABLE FORMAT CONTRACT

All structured tables conform to schemas declared here. Required fields are mandatory
on every row.

**Finding Table** (every reviewer section):
```
| F-ID | Severity | Surface | Finding | Recommendation |
```
`F-ID`: named stable identifier (F-01, F-02, ...). NOT positional. `Severity`:
HIGH / MEDIUM / LOW. All downstream references use F-ID values.

**CH-ID Challenge Table** (before BRACKET OPENING):
```
| CH-ID | Challenge Statement | §0 Grounding | [Section response columns] |
```
`§0 Grounding`: required. Cites the §0-CID value from STATUS QUO FRAMING CONTRACT
per §0-CID PIPELINE THREADING CONTRACT Axis A (e.g., "§0-C01 -- tests whether
existing capability argument holds"). Populated at registration time. Challenges
without a §0-CID Axis A citation are invalid.

**NH Dimension Scores Sub-table** (per DOMAIN and LIFECYCLE section):
```
| Dimension | B: Proposed-Build | C: Best-Non-Build-Alt |
```

**NH Dimension Comparison Table** (BRACKET OPENING and BRACKET CLOSING):
```
| Dimension | A: Status-Quo | B: Proposed-Build | C: Best-Non-Build-Alt | Delta B-A | Delta B-C |
```
Column A values initialized from STATUS QUO FRAMING CONTRACT §0-CID strength ratings
per §0-CID PIPELINE THREADING CONTRACT Axis B.

**LOCAL GATE LEDGER ROW** (per verdict-emitting section):
```
| Gate Verdict | Section Severity | Class | F-ID(s) sourcing this verdict |
```

**MASTER ACTION REGISTER ROW**:
```
| F-ID | Gate Verdict | Class | Section | Finding Summary | Recommendation |
```

---

### §§ PREAMBLE CONTRACTS

**§1 DISPOSITION ALGEBRA (C-10, C-02)**
HIGH = blocks; MEDIUM = conditions; LOW = advisory.
FAIL -> BLOCKED | >= 1 CONDITIONAL, no FAIL -> CONDITIONAL | all PASS -> READY.
OVERRIDE: OVERRIDE INVOKED: YES | NO in BRACKET CLOSING. If YES, name the §0-CID
commitment being superseded per §0-CID PIPELINE THREADING CONTRACT Axis C.

**§2 CLASS DERIVATION CONTRACT (C-12)**
FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY (optional).
No editorial class assignment at assembly time.

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23)**
Three alternatives (A, B, C). g_null = PASS iff delta_B_A > 0 AND delta_B_C > 0.
g_null = CONDITIONAL iff exactly one delta > 0. g_null = FAIL iff both <= 0.

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
g_null(initial) [BRACKET OPENING] -> g_null(post-domain) [SATURATION CHECK]
-> g_null(final) [BRACKET CLOSING]. GClose = g_null(final) or OVERRIDE INVOKED: YES
with named §0-CID commitment per §0-CID PIPELINE THREADING CONTRACT Axis C.

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21)**
Universal coverage: BRACKET OPENING + all DOMAIN + LIFECYCLE + BRACKET CLOSING.
Schema per TABLE FORMAT CONTRACT. Verbatim copy to MASTER ACTION REGISTER.

**§6 NON-VERDICT SECTION EXCLUSION (C-25)**
No gate ledger row from: STATUS QUO FRAMING CONTRACT, §0-CID PIPELINE THREADING
CONTRACT, TABLE FORMAT CONTRACT, §§ preamble, scope, CH-ID registration, CH-ID
saturation check, scope coverage reconciliation, lens coverage table.

**§7 VERBATIM ASSEMBLY PROHIBITION (C-20)**
MASTER ACTION REGISTER: verbatim copy. Re-derivation prohibited.

**§8 SECTION ORDER CONTRACT (C-26)** -- immutable:
```
[STATUS QUO FRAMING CONTRACT -- pre-execution, complete]
[§0-CID PIPELINE THREADING CONTRACT -- pre-execution, complete]
[TABLE FORMAT CONTRACT -- pre-execution, complete]
[§§ PREAMBLE -- pre-execution, complete]
1. Scope Declaration      2. CH-ID Registration     3. Bracket Opening
4. Domain Reviewers       5. CH-ID Saturation Check  6. Lifecycle Reviewer
7. Bracket Closing        8. Scope Coverage Reconciliation
9. Lens Coverage Table    10. Disposition            11. Master Action Register
12. Cross-Role Signals
```

**§9 FINDING IDENTIFIER CONTRACT (C-42)**
Schema layer: Finding Table declared in TABLE FORMAT CONTRACT. F-ID column required.
Behavioral layer (independent enforcement path): Every finding row in every reviewer
section MUST carry a populated F-ID value. Omitting F-ID is a contract violation --
the section's LOCAL GATE LEDGER ROW must note the defect. Positional row references
are contract violations. All downstream references use F-ID values.

**§10 CH-ID CHALLENGE REGISTRATION (C-04, C-43)**
Schema layer: CH-ID Challenge Table declared in TABLE FORMAT CONTRACT. §0 Grounding
column required, populated at registration time with a §0-CID value per §0-CID
PIPELINE THREADING CONTRACT Axis A.
Behavioral layer (independent enforcement path): Every CH-ID MUST carry a §0 Grounding
value naming a specific §0-CID from the STATUS QUO FRAMING CONTRACT registry per
§0-CID PIPELINE THREADING CONTRACT Axis A. A §0 Grounding value citing a generic
preamble §§ section does NOT satisfy this contract. CH-IDs without a valid §0-CID
Axis A citation are invalid and must be removed.

**§11 CH-ID SATURATION REQUIREMENT (C-27)**
SATURATED before LIFECYCLE. FULLY SATURATED at BRACKET CLOSING. BRACKET CLOSING
may not PASS when any CH-ID is UNSATURATED without waiver.

**§12 PER-FINDING SEVERITY AGGREGATION CONTRACT (C-30)**
Section Severity = worst(F-ID severities in section). No editorial assignment.

**§13 LENS COVERAGE TABLE PROTOCOL (C-31, C-33, C-34)**
Post-execution LENS COVERAGE TABLE: ADDRESSED/OPEN per lens.verify entry.
Applicability per entry. HIGH-applicability OPEN -> ADVISORY-OPEN-LENS items.
DOMAIN COVERAGE GAP-CHECK -> ADVISORY-GAP items.

**§14 SCOPE SURFACE DOMAIN ANNOTATION (C-36)**
Every IN-SCOPE surface: [DOMAIN: label] at enumeration time.

**§15 SCOPE COVERAGE GATE PROTOCOL (C-29)**
Post-bracket-closing reconciliation. GAP surfaces -> ADVISORY-GAP. No ledger row.

**§16 NH DIMENSION TABLE CONTRACT (C-35, C-37, C-38)**
BRACKET OPENING: NH Dimension Comparison Table per TABLE FORMAT CONTRACT. Column A
values initialized from STATUS QUO FRAMING CONTRACT §0-CID strength ratings per
§0-CID PIPELINE THREADING CONTRACT Axis B. >= 3 dimensions. g_null(initial) derivable
from Delta B-A and Delta B-C alone. BRACKET CLOSING: re-populate columns B and C.
g_null(final) derivable from revised values alone.

**§17 NH TABLE AGGREGATION RULE WITH LIFECYCLE EXTENSION (C-39, C-40, C-41)**
Column A: challenger's §0-CID-initialized opening values, unchanged.
Column B: avg(all DOMAIN B scores + LIFECYCLE B score).
Column C: avg(all DOMAIN C scores + LIFECYCLE C score).

DOMAIN NH SCORE EMISSION (C-40): every DOMAIN section emits NH Dimension Scores
sub-table per TABLE FORMAT CONTRACT before its LOCAL GATE LEDGER ROW.

LIFECYCLE NH SCORE EMISSION (C-41): LIFECYCLE section emits NH Dimension Scores
sub-table per TABLE FORMAT CONTRACT before its LOCAL GATE LEDGER ROW. Same dimensions
as §16 table. BRACKET CLOSING reads LIFECYCLE sub-table alongside DOMAIN sub-tables.
No prose extraction in the NH aggregation chain.

**§18 DOMAIN-AGGREGATE FORMULA (C-24)**
G_domain_agg = median(all DOMAIN gate verdicts). Labeled input to BRACKET CLOSING.

**§19 PRIMARY DRIVER DERIVATION CONTRACT (C-32)**
Precedence: BRACKET CLOSING OVERRIDE (cite §0-CID overridden per §0-CID PIPELINE
THREADING CONTRACT Axis C) > NULL HYPOTHESIS (cite §0-CID held per §0-CID PIPELINE
THREADING CONTRACT Axis D) > DOMAIN [first FAIL] > LIFECYCLE [FAIL] > DOMAIN [first
CONDITIONAL] > LIFECYCLE [CONDITIONAL] > CONSENSUS. Emit `Primary Driver: [value]`
at DISPOSITION. When driver is NULL HYPOTHESIS or BRACKET CLOSING OVERRIDE, append
the §0-CID citation per §0-CID PIPELINE THREADING CONTRACT Axis D.

**§20 DEPTH MODE ACKNOWLEDGMENT (C-08)**
deep: all roles. standard: relevant + rationale. quick: >= 3 + note.

---

Execute sections per §8. TABLE FORMAT CONTRACT schemas carry Axis A and Axis B
pipeline citations. §§ behavioral contracts carry Axis A, B, C, D pipeline citations.
Both layers are independently auditable against §0-CID PIPELINE THREADING CONTRACT:
a schema-layer auditor sees Axis A in CH-ID Challenge Table, Axis B in NH Dimension
Comparison Table; a behavioral-contract auditor sees Axis A in §10, Axis B in §16,
Axis C in §1 and §4, Axis D in §19. Before emitting DISPOSITION, confirm four-axis
§0-CID data flow:

```
Axis A (CH-ID §0 Grounding -- §0-CID citations):       [YES/NO]
Axis B (NH Column A -- §0-CID strength initialization): [YES/NO]
Axis C (BRACKET CLOSING OVERRIDE -- §0-CID named):     [YES/NO/NA]
Axis D (PRIMARY DRIVER -- §0-CID cited):                [YES/NO/NA]
```

Acknowledge {{artifact_id}}, {{depth}}, {{reviewer_set}} before Step 1.

---

### EXECUTION

Steps 1-13 as V-01. Step 3 CH-ID registration populates §0 Grounding per §10
(schema layer: TABLE FORMAT CONTRACT Axis A note; behavioral layer: §10 Axis A
requirement). Step 4 BRACKET OPENING Column A per §16 and TABLE FORMAT CONTRACT
Axis B note. Step 8 OVERRIDE names §0-CID per §1/§4 Axis C. Step 11 Primary Driver
cites §0-CID per §19 Axis D when applicable.

---

## V-05

**Axis**: Output format + Phrasing register + Inertia framing (three-axis) --
V-04 plus explicit pipeline-to-(schema+behavioral) back-references in each axis block
of §0-CID PIPELINE THREADING CONTRACT; a pipeline-contract auditor can identify the
TABLE FORMAT CONTRACT field and §§ behavioral contract governed by each axis without
reading other blocks; C-48 PASS, C-49 PASS; introduces new structural pattern

**Hypothesis**: V-04 achieves C-49 PASS with bidirectional cross-referencing: schema
notes point to pipeline, behavioral contracts point to pipeline. The pipeline contract
describes each axis by execution position (Axis A: "at CH-ID REGISTRATION TABLE"),
which implicitly identifies the governed field and contract -- but a pipeline-contract
auditor would need to read TABLE FORMAT CONTRACT and §§ contracts to confirm which
specific field and contract each axis governs. V-05 adds explicit forward-naming
inside each axis block: "Axis A governs TABLE FORMAT CONTRACT CH-ID Challenge Table
§0 Grounding field (schema layer) and §10 CH-ID CHALLENGE REGISTRATION behavioral
contract." This makes the pipeline contract self-auditable: all three cross-referencing
directions -- schema->pipeline, behavioral->pipeline, pipeline->(schema+behavioral) --
are now present as explicit text rather than implicit position references. V-05
introduces the pattern that three-layer explicit naming may generate as a criterion in
v18. Score: 295/295. The new structural pattern has no criterion to earn above V-04
under v17, but the architecture is superior for future rubric extraction.

---

You are running `/org-review`.

Inputs:
```
{{artifact_id}}: [artifact name or path under review]
{{depth}}: [standard | deep | quick]
{{reviewer_set}}: [auto | all | comma-separated role names from .roles/]
```

Acknowledge injected values before executing any section.

---

### STATUS QUO FRAMING CONTRACT (inertia-advocate pre-commitment)

Before table schemas or behavioral contracts are declared, register the no-build
commitments that justify not building {{artifact_id}}. These §0-CID values are the
ground truth for all §0-CID pipeline axes.

```
| §0-CID | Status Quo Commitment (why not building is acceptable) | Strength |
|--------|--------------------------------------------------------|----------|
| §0-C01 | [Existing capability or process covering this need]     | [H/M/L]  |
| §0-C02 | [Cost / risk / complexity argument for status quo]      | [H/M/L]  |
| §0-C03 | [Additional no-build strength claim as needed]          | [H/M/L]  |
```

Populate with artifact-specific values before any other section. Every CH-ID must
trace to a named §0-CID. Every finding must carry a named F-ID.

---

### §0-CID PIPELINE THREADING CONTRACT (four-axis pre-commitment)

The §0-CID values registered in STATUS QUO FRAMING CONTRACT flow through four
structural positions in this review. Each axis names: the execution position where
the §0-CID constraint applies, the TABLE FORMAT CONTRACT field it governs (schema
layer), and the §§ behavioral contract that enforces it (behavioral layer).

**Axis A -- CH-ID §0 Grounding citations** (at CH-ID REGISTRATION TABLE):
Every CH-ID §0 Grounding column value MUST cite a named §0-CID from the STATUS
QUO FRAMING CONTRACT registry. Generic preamble §§ section citations are not
permitted.
- Schema layer governed: TABLE FORMAT CONTRACT CH-ID Challenge Table §0 Grounding
  field.
- Behavioral layer enforced by: §10 CH-ID CHALLENGE REGISTRATION behavioral contract.

**Axis B -- NH Dimension Table Column A initialization** (at BRACKET OPENING):
Column A values in the NH Dimension Comparison Table MUST be initialized from
STATUS QUO FRAMING CONTRACT §0-CID strength ratings. Column A scores reflect the
claimed strength of those commitments on each dimension.
- Schema layer governed: TABLE FORMAT CONTRACT NH Dimension Comparison Table Column A
  field.
- Behavioral layer enforced by: §16 NH DIMENSION TABLE CONTRACT.

**Axis C -- BRACKET CLOSING OVERRIDE justification** (if OVERRIDE INVOKED: YES):
Any BRACKET CLOSING OVERRIDE declaration MUST name the specific §0-CID commitment
being superseded. A generic justification without §0-CID citation does not satisfy
this contract.
- Schema layer governed: TABLE FORMAT CONTRACT LOCAL GATE LEDGER ROW (BRACKET
  CLOSING row, OVERRIDE INVOKED field).
- Behavioral layer enforced by: §1 DISPOSITION ALGEBRA OVERRIDE clause and §4 NULL
  HYPOTHESIS PROGRESSION CONTRACT GClose requirement.

**Axis D -- PRIMARY DRIVER attribution** (at DISPOSITION):
When PRIMARY DRIVER is NULL HYPOTHESIS or BRACKET CLOSING OVERRIDE, the
`Primary Driver:` field MUST cite the §0-CID value(s) that drove the attribution.
CONSENSUS and DOMAIN-driven attributions do not require §0-CID citation.
- Schema layer governed: DISPOSITION labeled field at Step 11.
- Behavioral layer enforced by: §19 PRIMARY DRIVER DERIVATION CONTRACT.

All four axes must be populated before the review is considered complete. A compliance
auditor reading only this block can identify which TABLE FORMAT CONTRACT field and
which §§ behavioral contract each axis governs; reading those blocks confirms the
cross-reference in the opposite direction.

---

### TABLE FORMAT CONTRACT

All structured tables conform to schemas declared here. Required fields are mandatory
on every row.

**Finding Table** (every reviewer section):
```
| F-ID | Severity | Surface | Finding | Recommendation |
```
`F-ID`: named stable identifier (F-01, F-02, ...). NOT positional. `Severity`:
HIGH / MEDIUM / LOW. All downstream references use F-ID values.

**CH-ID Challenge Table** (before BRACKET OPENING):
```
| CH-ID | Challenge Statement | §0 Grounding | [Section response columns] |
```
`§0 Grounding`: required. Cites the §0-CID value from STATUS QUO FRAMING CONTRACT
per §0-CID PIPELINE THREADING CONTRACT Axis A (e.g., "§0-C01 -- tests whether
existing capability argument holds"). Populated at registration time. Challenges
without a §0-CID Axis A citation are invalid.

**NH Dimension Scores Sub-table** (per DOMAIN and LIFECYCLE section):
```
| Dimension | B: Proposed-Build | C: Best-Non-Build-Alt |
```

**NH Dimension Comparison Table** (BRACKET OPENING and BRACKET CLOSING):
```
| Dimension | A: Status-Quo | B: Proposed-Build | C: Best-Non-Build-Alt | Delta B-A | Delta B-C |
```
Column A values initialized from STATUS QUO FRAMING CONTRACT §0-CID strength ratings
per §0-CID PIPELINE THREADING CONTRACT Axis B.

**LOCAL GATE LEDGER ROW** (per verdict-emitting section):
```
| Gate Verdict | Section Severity | Class | F-ID(s) sourcing this verdict |
```

**MASTER ACTION REGISTER ROW**:
```
| F-ID | Gate Verdict | Class | Section | Finding Summary | Recommendation |
```

---

### §§ PREAMBLE CONTRACTS

**§1 DISPOSITION ALGEBRA (C-10, C-02)**
HIGH = blocks; MEDIUM = conditions; LOW = advisory.
FAIL -> BLOCKED | >= 1 CONDITIONAL, no FAIL -> CONDITIONAL | all PASS -> READY.
OVERRIDE: OVERRIDE INVOKED: YES | NO in BRACKET CLOSING. If YES, name the §0-CID
commitment being superseded per §0-CID PIPELINE THREADING CONTRACT Axis C.

**§2 CLASS DERIVATION CONTRACT (C-12)**
FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY (optional).
No editorial class assignment at assembly time.

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23)**
Three alternatives (A, B, C). g_null = PASS iff delta_B_A > 0 AND delta_B_C > 0.
g_null = CONDITIONAL iff exactly one delta > 0. g_null = FAIL iff both <= 0.

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
g_null(initial) [BRACKET OPENING] -> g_null(post-domain) [SATURATION CHECK]
-> g_null(final) [BRACKET CLOSING]. GClose = g_null(final) or OVERRIDE INVOKED: YES
with named §0-CID commitment per §0-CID PIPELINE THREADING CONTRACT Axis C.

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21)**
Universal coverage: BRACKET OPENING + all DOMAIN + LIFECYCLE + BRACKET CLOSING.
Schema per TABLE FORMAT CONTRACT. Verbatim copy to MASTER ACTION REGISTER.

**§6 NON-VERDICT SECTION EXCLUSION (C-25)**
No gate ledger row from: STATUS QUO FRAMING CONTRACT, §0-CID PIPELINE THREADING
CONTRACT, TABLE FORMAT CONTRACT, §§ preamble, scope, CH-ID registration, CH-ID
saturation check, scope coverage reconciliation, lens coverage table.

**§7 VERBATIM ASSEMBLY PROHIBITION (C-20)**
MASTER ACTION REGISTER: verbatim copy. Re-derivation prohibited.

**§8 SECTION ORDER CONTRACT (C-26)** -- immutable:
```
[STATUS QUO FRAMING CONTRACT -- pre-execution, complete]
[§0-CID PIPELINE THREADING CONTRACT -- pre-execution, complete]
[TABLE FORMAT CONTRACT -- pre-execution, complete]
[§§ PREAMBLE -- pre-execution, complete]
1. Scope Declaration      2. CH-ID Registration     3. Bracket Opening
4. Domain Reviewers       5. CH-ID Saturation Check  6. Lifecycle Reviewer
7. Bracket Closing        8. Scope Coverage Reconciliation
9. Lens Coverage Table    10. Disposition            11. Master Action Register
12. Cross-Role Signals
```

**§9 FINDING IDENTIFIER CONTRACT (C-42)**
Schema layer: Finding Table declared in TABLE FORMAT CONTRACT. F-ID column required.
Behavioral layer (independent enforcement path): Every finding row in every reviewer
section MUST carry a populated F-ID value. Omitting F-ID is a contract violation --
the section's LOCAL GATE LEDGER ROW must note the defect. Positional row references
are contract violations. All downstream references use F-ID values.

**§10 CH-ID CHALLENGE REGISTRATION (C-04, C-43)**
Schema layer: CH-ID Challenge Table declared in TABLE FORMAT CONTRACT. §0 Grounding
column required, populated at registration time with a §0-CID value per §0-CID
PIPELINE THREADING CONTRACT Axis A (schema layer).
Behavioral layer (independent enforcement path): Every CH-ID MUST carry a §0 Grounding
value naming a specific §0-CID from the STATUS QUO FRAMING CONTRACT registry per
§0-CID PIPELINE THREADING CONTRACT Axis A (behavioral layer). A §0 Grounding value
citing a generic preamble §§ section does NOT satisfy this contract. CH-IDs without a
valid §0-CID Axis A citation are invalid and must be removed.

**§11 CH-ID SATURATION REQUIREMENT (C-27)**
SATURATED before LIFECYCLE. FULLY SATURATED at BRACKET CLOSING. BRACKET CLOSING
may not PASS when any CH-ID is UNSATURATED without waiver.

**§12 PER-FINDING SEVERITY AGGREGATION CONTRACT (C-30)**
Section Severity = worst(F-ID severities in section). No editorial assignment.

**§13 LENS COVERAGE TABLE PROTOCOL (C-31, C-33, C-34)**
Post-execution LENS COVERAGE TABLE: ADDRESSED/OPEN per lens.verify entry.
Applicability per entry. HIGH-applicability OPEN -> ADVISORY-OPEN-LENS items.
DOMAIN COVERAGE GAP-CHECK -> ADVISORY-GAP items.

**§14 SCOPE SURFACE DOMAIN ANNOTATION (C-36)**
Every IN-SCOPE surface: [DOMAIN: label] at enumeration time.

**§15 SCOPE COVERAGE GATE PROTOCOL (C-29)**
Post-bracket-closing reconciliation. GAP surfaces -> ADVISORY-GAP. No ledger row.

**§16 NH DIMENSION TABLE CONTRACT (C-35, C-37, C-38)**
BRACKET OPENING: NH Dimension Comparison Table per TABLE FORMAT CONTRACT. Column A
values initialized from STATUS QUO FRAMING CONTRACT §0-CID strength ratings per
§0-CID PIPELINE THREADING CONTRACT Axis B (schema layer: TABLE FORMAT CONTRACT NH
Dimension Comparison Table Column A note; behavioral layer: this contract). >= 3
dimensions. g_null(initial) derivable from Delta B-A and Delta B-C alone. BRACKET
CLOSING: re-populate columns B and C. g_null(final) derivable from revised values alone.

**§17 NH TABLE AGGREGATION RULE WITH LIFECYCLE EXTENSION (C-39, C-40, C-41)**
Column A: challenger's §0-CID-initialized opening values, unchanged.
Column B: avg(all DOMAIN B scores + LIFECYCLE B score).
Column C: avg(all DOMAIN C scores + LIFECYCLE C score).

DOMAIN NH SCORE EMISSION (C-40): every DOMAIN section emits NH Dimension Scores
sub-table per TABLE FORMAT CONTRACT before its LOCAL GATE LEDGER ROW.

LIFECYCLE NH SCORE EMISSION (C-41): LIFECYCLE section emits NH Dimension Scores
sub-table per TABLE FORMAT CONTRACT before its LOCAL GATE LEDGER ROW. Same dimensions
as §16 table. BRACKET CLOSING reads LIFECYCLE sub-table alongside DOMAIN sub-tables.
No prose extraction in the NH aggregation chain.

**§18 DOMAIN-AGGREGATE FORMULA (C-24)**
G_domain_agg = median(all DOMAIN gate verdicts). Labeled input to BRACKET CLOSING.

**§19 PRIMARY DRIVER DERIVATION CONTRACT (C-32)**
Precedence: BRACKET CLOSING OVERRIDE (cite §0-CID overridden per §0-CID PIPELINE
THREADING CONTRACT Axis C; schema layer: LOCAL GATE LEDGER ROW BRACKET CLOSING;
behavioral layer: §1 and §4) > NULL HYPOTHESIS (cite §0-CID held per §0-CID PIPELINE
THREADING CONTRACT Axis D; schema layer: DISPOSITION field; behavioral layer: this
contract) > DOMAIN [first FAIL] > LIFECYCLE [FAIL] > DOMAIN [first CONDITIONAL] >
LIFECYCLE [CONDITIONAL] > CONSENSUS. Emit `Primary Driver: [value]` at DISPOSITION.
When driver is NULL HYPOTHESIS or BRACKET CLOSING OVERRIDE, append the §0-CID citation
per §0-CID PIPELINE THREADING CONTRACT Axis D.

**§20 DEPTH MODE ACKNOWLEDGMENT (C-08)**
deep: all roles. standard: relevant + rationale. quick: >= 3 + note.

---

Execute sections per §8. Three-layer cross-reference architecture is complete: a
schema-layer auditor reading TABLE FORMAT CONTRACT sees Axis A at CH-ID Challenge
Table §0 Grounding field and Axis B at NH Dimension Comparison Table Column A; a
behavioral-layer auditor reading §§ contracts sees Axis A at §10, Axis B at §16,
Axis C at §1 and §4, Axis D at §19; a pipeline-contract auditor reading §0-CID
PIPELINE THREADING CONTRACT sees all four axes naming their governed schema fields
and behavioral contracts. Before emitting DISPOSITION, confirm four-axis §0-CID data
flow:

```
Axis A (CH-ID §0 Grounding -- §0-CID citations):       [YES/NO]
Axis B (NH Column A -- §0-CID strength initialization): [YES/NO]
Axis C (BRACKET CLOSING OVERRIDE -- §0-CID named):     [YES/NO/NA]
Axis D (PRIMARY DRIVER -- §0-CID cited):                [YES/NO/NA]
```

Acknowledge {{artifact_id}}, {{depth}}, {{reviewer_set}} before Step 1.

---

### EXECUTION

**Step 1: Acknowledge inputs**
```
Artifact: {{artifact_id}}
Depth: {{depth}}
Reviewer set: {{reviewer_set}}
Role selection rationale: [state if depth=standard]
```

**Step 2: SCOPE DECLARATION**
Enumerate all IN-SCOPE surfaces with [DOMAIN: label] per §14. State OUT-OF-SCOPE.

**Step 3: CH-ID REGISTRATION TABLE**
Register all challenges per §10. §0 Grounding column: cite §0-CID value from STATUS
QUO FRAMING CONTRACT registry per §0-CID PIPELINE THREADING CONTRACT Axis A (schema
layer: CH-ID Challenge Table note; behavioral layer: §10). Challenges without §0-CID
Axis A citation are invalid.

**Step 4: BRACKET OPENING**
- State null hypothesis: what the team does today, why it is acceptable.
- Populate NH Dimension Comparison Table: Column A from §0-CID strength ratings per
  §0-CID PIPELINE THREADING CONTRACT Axis B (schema layer: NH Dimension Comparison
  Table Column A note; behavioral layer: §16). >= 3 dimensions.
  Emit g_null(initial) as labeled field.
- Emit LOCAL GATE LEDGER ROW per TABLE FORMAT CONTRACT schema.

**Step 5: DOMAIN REVIEWER SECTIONS** (one per role, manifest order)
- State role name and lens (one sentence).
- Produce finding rows per Finding Table schema (§9 schema + behavioral layers).
- Respond to relevant CH-IDs.
- Emit NH Dimension Scores sub-table per TABLE FORMAT CONTRACT schema.
- Emit LOCAL GATE LEDGER ROW. Section Severity = worst(finding severities) per §12.

**Step 6: CH-ID SATURATION CHECK**
- Verify SATURATED tier. Emit g_null(post-domain) per §4 Stage 2. No gate ledger row.

**Step 7: LIFECYCLE REVIEWER SECTION**
- Evaluate lifecycle phases (creation, active use, change, deprecation, removal).
- Produce finding rows per Finding Table schema.
- Respond to relevant CH-IDs.
- Emit NH Dimension Scores sub-table per TABLE FORMAT CONTRACT schema.
- Emit LOCAL GATE LEDGER ROW with g_lifecycle labeled.

**Step 8: BRACKET CLOSING**
- Receive G_domain_agg (§18), g_lifecycle, all domain/lifecycle verdicts.
- Re-populate NH Dimension Comparison Table columns B and C per §17.
- Derive g_null(final) from revised table per §3 (Stage 3 of §4).
- Emit OVERRIDE INVOKED: YES | NO. If YES: name §0-CID being superseded per Axis C
  (schema layer: LOCAL GATE LEDGER ROW; behavioral layer: §1 and §4).
- Emit LOCAL GATE LEDGER ROW.

**Step 9: SCOPE COVERAGE RECONCILIATION** (per §15; no gate ledger row)

**Step 10: LENS COVERAGE TABLE** (per §13; no gate ledger row)

**Step 11: DISPOSITION**
- Apply §1 DISPOSITION ALGEBRA to gate verdict vector.
- Emit `DISPOSITION: READY | CONDITIONAL | BLOCKED` as labeled field.
- Emit `Primary Driver: [value]` per §19. If NULL HYPOTHESIS or OVERRIDE:
  cite §0-CID value(s) per Axis D (schema layer: DISPOSITION field; behavioral
  layer: §19).

**Step 12: MASTER ACTION REGISTER**
Verbatim copy of LOCAL GATE LEDGER ROWS (§7). Append ADVISORY-GAP and
ADVISORY-OPEN-LENS items. No re-derivation.

**Step 13: CROSS-ROLE SIGNALS**
Synthesis narrative. Name >= 1 cross-role conflict or convergence. Reference all
three g_null stages. Explain the disposition.
