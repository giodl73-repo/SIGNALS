---
skill: quest-variate
skill_target: org-review
date: 2026-03-17
round: 18
rubric: org-review-rubric-v16-2026-03-17.md
---

# org-review -- Variate R18

5 complete prompt body variations. Single-axis first (V-01 through V-03), then
two-axis and three-axis combinations (V-04, V-05).

**R18 design target**: All five R17 variants scored 265/265 under v15 (perfect).
Under v16, the four new criteria (C-44 through C-47) differentiate them. No R17
variant achieves C-44+C-45+C-47 simultaneously without C-46. The R18 primary
target is 280/285 -- the V-04+V-03 hybrid (TABLE FORMAT CONTRACT + §0-CID registry
+ dual-path enforcement) that was architecturally implied but never executed in R17.
Full 285/285 requires four-axis §0-CID threading (C-46).

**Gap analysis from R17:**

| Criterion | R17 V-04 | R17 V-03 | R17 V-05 | What it requires |
|-----------|----------|----------|----------|-----------------|
| C-44 TABLE FORMAT CONTRACT | PASS | FAIL | PASS | Unified schema block pre-§§; §§ reference schemas rather than redeclare |
| C-45 §0-CID ARTIFACT REGISTRY | FAIL | PASS | PASS | Named §0-CID values; CH-ID §0 Grounding cites §0-CID not generic §§ sections |
| C-46 §0-CID FOUR-AXIS THREADING | FAIL | FAIL | PASS | §0-CID at: (a) CH-ID grounding, (b) NH Column A init, (c) OVERRIDE justification, (d) PRIMARY DRIVER |
| C-47 DUAL-PATH ENFORCEMENT | PASS | FAIL | PASS | TABLE FORMAT CONTRACT schema + independent behavioral §§ per C-42/C-43 field |

**R18 synthesis path**: R17 V-04 achieved C-44+C-47 but no §0-CID (C-45 FAIL). R17 V-03
achieved C-45 but no TABLE FORMAT CONTRACT (C-44 FAIL makes C-47 vacuous, C-46 FAIL). No R17
variant had C-44+C-45+C-47 without also having C-46. R18 V-04 is the first explicit test of that
combination. R18 V-05 tests whether four-axis threading can be achieved with a more explicit
structural contract than R17 V-05's inline closing note.

**R18 variation axes:**

- V-01: Output format (single axis) -- TABLE FORMAT CONTRACT block pre-§§ with all schema
  declarations. §§ contracts for C-42 and C-43 cite TABLE FORMAT CONTRACT only (no independent
  behavioral violation text). C-47 FAIL: schema declared once in TABLE FORMAT CONTRACT, no
  independent behavioral path. No §0-CID registry (C-45 FAIL).

- V-02: Phrasing register (single axis) -- TABLE FORMAT CONTRACT block pre-§§. §9 FINDING
  IDENTIFIER CONTRACT and §10 CH-ID CHALLENGE REGISTRATION each carry BOTH a TABLE FORMAT
  CONTRACT schema citation AND a self-contained behavioral violation clause (defines when to
  populate the field, what constitutes a violation, what remediation is required). Two independent
  enforcement paths for C-42 and C-43. No §0-CID registry (C-45 FAIL). C-47 PASS: dual-path
  active.

- V-03: Inertia framing (single axis) -- STATUS QUO FRAMING CONTRACT registers named §0-CID
  commitments. CH-ID §0 Grounding cites §0-CID values, not generic preamble §§ section numbers.
  No TABLE FORMAT CONTRACT block (C-44 FAIL makes C-47 vacuous). §0-CID threads only axis (a) --
  CH-ID grounding column. C-45 PASS; C-46 FAIL; C-44 FAIL; C-47 vacuous.

- V-04: Output format + Inertia framing (two-axis) -- TABLE FORMAT CONTRACT + STATUS QUO FRAMING
  CONTRACT §0-CID registry. §9 and §10 each have schema reference + independent behavioral
  contract. §0-CID threads only axis (a). C-44+C-45+C-47 PASS; C-46 FAIL. Predicted: 280/285.

- V-05: Output format + Inertia framing + §0-CID four-axis pipeline (three-axis) -- all three
  patterns combined. §0-CID PIPELINE THREADING CONTRACT explicitly names the four structural
  axes and commits them as pre-execution contracts. C-44+C-45+C-46+C-47 PASS. Predicted:
  285/285.

**R18 single-axis predictions:**
- V-01: C-44 PASS, C-45 FAIL, C-46 FAIL, C-47 FAIL. Score: 270/285
- V-02: C-44 PASS, C-45 FAIL, C-46 FAIL, C-47 PASS. Score: 275/285
- V-03: C-44 FAIL, C-45 PASS, C-46 FAIL, C-47 vacuous/FAIL. Score: 270/285

**R18 two-axis and three-axis predictions:**
- V-04: C-44+C-45+C-47 PASS, C-46 FAIL. Score: 280/285
- V-05: C-44+C-45+C-46+C-47 PASS. Score: 285/285

---

## V-01

**Axis**: Output format -- TABLE FORMAT CONTRACT pre-§§ with schema-reference §§ contracts;
no independent behavioral text for C-42/C-43; no §0-CID registry

**Hypothesis**: R17 V-02 introduced TABLE FORMAT CONTRACT and achieved C-44 PASS but C-47 FAIL
because the §§ contracts for C-42 and C-43 merely said "per TABLE FORMAT CONTRACT schema" with
no independent behavioral enforcement path. V-01 R18 replicates this structure intentionally to
isolate the TABLE FORMAT CONTRACT contribution (C-44) from the dual-path enforcement contribution
(C-47). The distinction between a schema reference and an independent behavioral contract is the
axis V-02 R18 will vary. V-01 is the clean C-44-only baseline: TABLE FORMAT CONTRACT declares all
schemas, §§ contracts reference them but add nothing behavioral. Predicted score: 270/285.

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

### TABLE FORMAT CONTRACT

All structured tables produced by this review conform to the schemas declared here.
Every schema field is required on every row unless marked optional. A row that omits
a required field is a format violation auditable from this block alone.

**Finding Table** (emitted in every reviewer section):
```
| F-ID | Severity | Surface | Finding | Recommendation |
```
- `F-ID`: named stable identifier (F-01, F-02, ...). NOT a positional row number.
  All downstream references use F-ID values -- action register, CH-ID response
  columns, lens coverage citations. No positional row references.
- `Severity`: exactly HIGH / MEDIUM / LOW.
- `Surface`: named artifact surface (section, field, diagram element, assumption).
- `Finding`: specific observation on the named surface.
- `Recommendation`: what to change and where in the artifact.

**CH-ID Challenge Table** (emitted once before BRACKET OPENING):
```
| CH-ID | Challenge Statement | §0 Grounding | [Section response columns] |
```
- `CH-ID`: named identifier (CH-01, CH-02, ...).
- `Challenge Statement`: the specific question or challenge being posed.
- `§0 Grounding`: required. Cites the preamble §§ contract section (e.g., "§1
  DISPOSITION ALGEBRA") that authorizes this challenge. Populated at registration
  time. Challenges without a §0 grounding citation are invalid and may not be
  registered.
- Section columns: one per reviewer section, populated during execution.

**NH Dimension Scores Sub-table** (emitted per DOMAIN and LIFECYCLE section):
```
| Dimension | B: Proposed-Build | C: Best-Non-Build-Alt |
```
- Same dimension rows as the NH Dimension Comparison Table (BRACKET OPENING).

**NH Dimension Comparison Table** (BRACKET OPENING and BRACKET CLOSING):
```
| Dimension | A: Status-Quo | B: Proposed-Build | C: Best-Non-Build-Alt | Delta B-A | Delta B-C |
```
- Three alternatives required. g_null derivable from Delta B-A and Delta B-C alone.

**LOCAL GATE LEDGER ROW** (emitted per verdict-emitting section):
```
| Gate Verdict | Section Severity | Class | F-ID(s) sourcing this verdict |
```

**MASTER ACTION REGISTER ROW** (assembled by verbatim copy from LOCAL GATE LEDGER ROWS):
```
| F-ID | Gate Verdict | Class | Section | Finding Summary | Recommendation |
```

---

### §§ PREAMBLE CONTRACTS

**§1 DISPOSITION ALGEBRA (C-10, C-02)**
```
HIGH = blocks commitment | MEDIUM = conditions commitment | LOW = advisory
FAIL -> DISPOSITION: BLOCKED
>= 1 CONDITIONAL, no FAIL -> DISPOSITION: CONDITIONAL
All PASS -> DISPOSITION: READY
```
BLOCKED may not be overridden except via BRACKET CLOSING OVERRIDE with labeled
OVERRIDE INVOKED: YES | NO field and named justification.

**§2 CLASS DERIVATION CONTRACT (C-12)**
```
Gate verdict FAIL        -> Action item class: BLOCKED
Gate verdict CONDITIONAL -> Action item class: CONDITIONAL
Gate verdict PASS        -> Action item class: ADVISORY (skip if no advisory intent)
```
No editorial class assignment at action register assembly time.

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23)**
```
Let delta_B_A = Proposed-Build score - Status-Quo score
Let delta_B_C = Proposed-Build score - Best-Non-Build-Alt score

g_null = PASS        if delta_B_A > 0 AND delta_B_C > 0
g_null = CONDITIONAL if exactly one delta > 0
g_null = FAIL        if delta_B_A <= 0 AND delta_B_C <= 0
```
Applied at all three g_null checkpoints per §4.

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
```
Stage 1: g_null(initial)     [emitted at BRACKET OPENING]
Stage 2: g_null(post-domain) [emitted at CH-ID SATURATION CHECK]
         if G_domain_agg = FAIL:        g_null(post-domain) = g_null(initial)
         if G_domain_agg = PASS:        g_null(post-domain) weakens one tier toward PASS
         if G_domain_agg = CONDITIONAL: g_null(post-domain) = CONDITIONAL
Stage 3: g_null(final)       [emitted at BRACKET CLOSING]
         same logic substituting G_lifecycle
```
BRACKET CLOSING GClose MUST equal g_null(final), or declare OVERRIDE INVOKED: YES.

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21)**
Universal coverage: BRACKET OPENING, every DOMAIN section, LIFECYCLE section,
BRACKET CLOSING each emit exactly one LOCAL GATE LEDGER ROW per TABLE FORMAT
CONTRACT schema. MASTER ACTION REGISTER assembled by verbatim copy. No re-derivation.

**§6 NON-VERDICT SECTION EXCLUSION (C-25)**
No gate ledger row from: §§ preamble, TABLE FORMAT CONTRACT, SCOPE DECLARATION,
CH-ID REGISTRATION TABLE, CH-ID SATURATION CHECK, SCOPE COVERAGE RECONCILIATION,
LENS COVERAGE TABLE.

**§7 VERBATIM ASSEMBLY PROHIBITION (C-20)**
MASTER ACTION REGISTER assembly: copy all LOCAL GATE LEDGER ROWS verbatim. Re-
derivation of Gate Verdict or Class at assembly time is prohibited.

**§8 SECTION ORDER CONTRACT (C-26)** -- immutable:
```
[TABLE FORMAT CONTRACT -- pre-execution, complete]
[§§ PREAMBLE -- pre-execution, complete]
1. Scope Declaration
2. CH-ID Registration Table
3. Bracket Opening (challenger / inertia-advocate)
4. Domain Reviewer Sections (one per role, manifest order)
5. CH-ID Saturation Check
6. Lifecycle Reviewer Section
7. Bracket Closing (challenger, post-domain)
8. Scope Coverage Reconciliation
9. Lens Coverage Table
10. Disposition + Primary Driver
11. Master Action Register
12. Cross-Role Signals
```
Reordering any numbered step is a contract violation.

**§9 FINDING IDENTIFIER CONTRACT (C-42)**
Every finding row in every reviewer section uses the Finding Table schema per
TABLE FORMAT CONTRACT. F-ID is the named stable identifier column. All downstream
references use F-ID values.

**§10 CH-ID CHALLENGE REGISTRATION (C-04, C-43)**
CH-ID tracing table uses the CH-ID Challenge Table schema per TABLE FORMAT CONTRACT.
§0 Grounding column: populated at registration time with the preamble §§ contract
section that authorizes each challenge. Every CH-ID must carry a §0 grounding
citation; challenges without one are invalid.

**§11 CH-ID SATURATION REQUIREMENT (C-27)**
```
SATURATED:       every CH-ID has >= 1 DOMAIN section response (verified before LIFECYCLE)
FULLY SATURATED: every CH-ID has domain + lifecycle responses (verified at BRACKET CLOSING)
```
BRACKET CLOSING may not emit PASS when any CH-ID is UNSATURATED without explicit waiver.

**§12 PER-FINDING SEVERITY AGGREGATION CONTRACT (C-30)**
Section Severity = worst(Severity of all F-IDs in this section).
worst order: HIGH > MEDIUM > LOW. No editorial section-level severity assignment.

**§13 LENS COVERAGE TABLE PROTOCOL (C-31, C-33, C-34)**
After all reviewer sections (before DISPOSITION): emit LENS COVERAGE TABLE. For each
active reviewer role, every `lens.verify` entry appears as ADDRESSED (>= 1 finding by
F-ID) or OPEN (no finding). Each entry carries Applicability (HIGH/MEDIUM/LOW)
specific to this artifact. HIGH-applicability OPEN entries -> ADVISORY-OPEN-LENS
items in MASTER ACTION REGISTER. Run DOMAIN COVERAGE GAP-CHECK: artifact domains
with no HIGH-applicability reviewer -> ADVISORY-GAP items (domain name + gap reason).

**§14 SCOPE SURFACE DOMAIN ANNOTATION (C-36)**
Every IN-SCOPE surface carries [DOMAIN: label] at enumeration time. The domain
annotation registry is the source for the §13 DOMAIN COVERAGE GAP-CHECK. No
editorial domain inference at gap-check time.

**§15 SCOPE COVERAGE GATE PROTOCOL (C-29)**
Post-bracket-closing SCOPE COVERAGE RECONCILIATION: every IN-SCOPE surface is
classified COVERED (>= 1 F-ID reference) or GAP (no reference). GAP surfaces ->
ADVISORY-GAP items in MASTER ACTION REGISTER. Emits no gate ledger row (§6).

**§16 NH DIMENSION TABLE CONTRACT (C-35, C-37, C-38)**
BRACKET OPENING: NH Dimension Comparison Table per TABLE FORMAT CONTRACT. At minimum
3 dimensions on a defined scale. g_null(initial) derivable from Delta B-A and Delta
B-C alone per §3. BRACKET CLOSING: re-populate columns B and C per §17 aggregation
formula. g_null(final) derivable from revised table values alone.

**§17 NH TABLE AGGREGATION RULE WITH LIFECYCLE EXTENSION (C-39, C-40, C-41)**
```
Column A (Status-Quo):         challenger's opening value, unchanged
Column B (Proposed-Build):     avg(all DOMAIN B scores + LIFECYCLE B score)
Column C (Best-Non-Build-Alt): avg(all DOMAIN C scores + LIFECYCLE C score)
```
DOMAIN NH SCORE EMISSION (C-40): every DOMAIN section emits NH Dimension Scores
sub-table per TABLE FORMAT CONTRACT schema before its LOCAL GATE LEDGER ROW.

LIFECYCLE NH SCORE EMISSION (C-41): LIFECYCLE section emits NH Dimension Scores
sub-table per TABLE FORMAT CONTRACT schema before its LOCAL GATE LEDGER ROW. Same
dimension rows as §16 table. BRACKET CLOSING reads LIFECYCLE sub-table alongside
DOMAIN sub-tables. No prose extraction permitted in the NH aggregation chain.

**§18 DOMAIN-AGGREGATE FORMULA (C-24)**
G_domain_agg = median(all DOMAIN gate verdicts). Provided as labeled input to
BRACKET CLOSING.

**§19 PRIMARY DRIVER DERIVATION CONTRACT (C-32)**
Precedence (first match wins):
```
Rule 1: BRACKET CLOSING with OVERRIDE INVOKED: YES -> Primary Driver: BRACKET CLOSING OVERRIDE
Rule 2: BRACKET OPENING gate = FAIL               -> Primary Driver: NULL HYPOTHESIS
Rule 3: Any DOMAIN gate = FAIL                     -> Primary Driver: DOMAIN [first FAIL role]
Rule 4: LIFECYCLE gate = FAIL                      -> Primary Driver: LIFECYCLE
Rule 5: Any DOMAIN gate = CONDITIONAL              -> Primary Driver: DOMAIN [first CONDITIONAL]
Rule 6: LIFECYCLE gate = CONDITIONAL               -> Primary Driver: LIFECYCLE
Rule 7: All gates = PASS                           -> Primary Driver: CONSENSUS
```
Emit `Primary Driver: [value]` at DISPOSITION.

**§20 DEPTH MODE ACKNOWLEDGMENT (C-08)**
`deep`: all roles from .roles/. `standard`: roles relevant to artifact type;
selection rationale stated. `quick`: >= 3 highest-priority roles; abbreviation note
included. {{reviewer_set}} overrides depth-based selection when non-auto.

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
Enumerate all IN-SCOPE surfaces with [DOMAIN: label] per §14. State OUT-OF-SCOPE
surfaces. Flag any surface discovered mid-review as a scope gap.

**Step 3: CH-ID REGISTRATION TABLE**
Register all challenges per §10. Populate §0 Grounding column at registration time.
Use CH-ID Challenge Table schema from TABLE FORMAT CONTRACT.

**Step 4: BRACKET OPENING**
- State null hypothesis: what the team does today instead, why that is acceptable.
- Populate NH Dimension Comparison Table (TABLE FORMAT CONTRACT schema; >= 3 dimensions).
- Emit g_null(initial) as labeled field.
- Emit LOCAL GATE LEDGER ROW (TABLE FORMAT CONTRACT schema).

**Step 5: DOMAIN REVIEWER SECTIONS** (one per role, manifest order)
For each role:
- State role name and lens (one sentence: "As a [role], I care about [concern]").
- Produce finding rows per Finding Table schema (TABLE FORMAT CONTRACT).
- Respond to relevant CH-IDs.
- Emit NH Dimension Scores sub-table (TABLE FORMAT CONTRACT schema).
- Emit LOCAL GATE LEDGER ROW. Section Severity = worst(finding severities) per §12.

**Step 6: CH-ID SATURATION CHECK**
- Verify SATURATED tier: every CH-ID has >= 1 domain response.
- Emit g_null(post-domain) per §4 Stage 2 formula.
- No gate ledger row (§6).

**Step 7: LIFECYCLE REVIEWER SECTION**
- Evaluate artifact through lifecycle phases (creation, active use, change, deprecation,
  removal). Surface findings specific to lifecycle transitions and long-term maintenance.
- Produce finding rows per Finding Table schema.
- Respond to relevant CH-IDs.
- Emit NH Dimension Scores sub-table (TABLE FORMAT CONTRACT schema).
- Emit LOCAL GATE LEDGER ROW with g_lifecycle labeled.

**Step 8: BRACKET CLOSING**
- Receive G_domain_agg (per §18), g_lifecycle, and all domain/lifecycle gate verdicts.
- Re-populate NH Dimension Comparison Table columns B and C per §17 formula.
- Derive g_null(final) from revised table per §3 (Stage 3 of §4).
- Emit OVERRIDE INVOKED: YES | NO as labeled field.
- Emit LOCAL GATE LEDGER ROW.

**Step 9: SCOPE COVERAGE RECONCILIATION** (per §15; no gate ledger row)

**Step 10: LENS COVERAGE TABLE** (per §13; no gate ledger row)

**Step 11: DISPOSITION**
- Apply §1 DISPOSITION ALGEBRA to gate verdict vector.
- Emit `DISPOSITION: READY | CONDITIONAL | BLOCKED` as labeled field.
- Emit `Primary Driver: [value]` per §19.

**Step 12: MASTER ACTION REGISTER**
Copy all LOCAL GATE LEDGER ROWS verbatim (§7). Append ADVISORY-GAP items from §15
and ADVISORY-OPEN-LENS items from §13. Do not re-derive Gate Verdict or Class.

**Step 13: CROSS-ROLE SIGNALS**
Synthesis narrative integrating findings across roles. Name >= 1 cross-role conflict
or convergence. Reference g_null progression (all three stages). Explain the
disposition rather than restating it.

---

## V-02

**Axis**: Phrasing register -- TABLE FORMAT CONTRACT pre-§§ with independent behavioral
contracts in §9 and §10; no §0-CID registry; dual-path enforcement active (C-47 PASS)

**Hypothesis**: R17 V-02 had TABLE FORMAT CONTRACT (C-44 PASS) but C-47 FAIL because §9
and §10 merely cited "per TABLE FORMAT CONTRACT schema" -- no independent behavioral text.
R17 V-04 achieved C-47 PASS because §9 and §10 contained behavioral violation clauses that
were structurally independent of the TABLE FORMAT CONTRACT: an auditor reading only §9 (without
the TABLE FORMAT CONTRACT) could still determine when F-ID is required and what constitutes a
violation. V-02 R18 isolates this behavioral independence axis by combining TABLE FORMAT
CONTRACT (C-44) with fully independent behavioral §§ contracts for C-42 and C-43 (C-47), while
keeping no §0-CID registry (C-45 FAIL). The test: C-47 PASS requires the behavioral contract
to be self-sufficient, not a reference to the schema block. Predicted score: 275/285.

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

### TABLE FORMAT CONTRACT

All structured tables in this review conform to schemas declared here. Required fields
are mandatory on every row.

**Finding Table** (every reviewer section):
```
| F-ID | Severity | Surface | Finding | Recommendation |
```
`F-ID`: named stable identifier (F-01, F-02, ...). NOT positional. `Severity`:
HIGH / MEDIUM / LOW. `Surface`: named artifact surface. `Finding`: specific
observation. `Recommendation`: what to change and where.

**CH-ID Challenge Table** (before BRACKET OPENING):
```
| CH-ID | Challenge Statement | §0 Grounding | [Section response columns] |
```
`§0 Grounding`: required at registration time. Preamble §§ contract section
authorizing this challenge. Challenges without §0 grounding are invalid.

**NH Dimension Scores Sub-table** (per DOMAIN and LIFECYCLE section):
```
| Dimension | B: Proposed-Build | C: Best-Non-Build-Alt |
```

**NH Dimension Comparison Table** (BRACKET OPENING and BRACKET CLOSING):
```
| Dimension | A: Status-Quo | B: Proposed-Build | C: Best-Non-Build-Alt | Delta B-A | Delta B-C |
```

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
FAIL -> BLOCKED | >= 1 CONDITIONAL + no FAIL -> CONDITIONAL | all PASS -> READY.
OVERRIDE: labeled field OVERRIDE INVOKED: YES | NO in BRACKET CLOSING.

**§2 CLASS DERIVATION CONTRACT (C-12)**
FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY (optional).
No editorial class assignment at assembly time.

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23)**
Three alternatives. g_null = PASS iff delta_B_A > 0 AND delta_B_C > 0.
g_null = CONDITIONAL iff exactly one delta > 0. g_null = FAIL iff both <= 0.

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
g_null(initial) [BRACKET OPENING] -> g_null(post-domain) [CH-ID SATURATION CHECK]
-> g_null(final) [BRACKET CLOSING]. GClose = g_null(final) or OVERRIDE INVOKED: YES.

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21)**
Universal coverage: BRACKET OPENING + all DOMAIN + LIFECYCLE + BRACKET CLOSING each
emit one LOCAL GATE LEDGER ROW per TABLE FORMAT CONTRACT schema. Verbatim copy to
MASTER ACTION REGISTER. No re-derivation.

**§6 NON-VERDICT SECTION EXCLUSION (C-25)**
No gate ledger row from: TABLE FORMAT CONTRACT, §§ preamble, scope declaration, CH-ID
registration, CH-ID saturation check, scope coverage reconciliation, lens coverage table.

**§7 VERBATIM ASSEMBLY PROHIBITION (C-20)**
MASTER ACTION REGISTER: verbatim copy of LOCAL GATE LEDGER ROWS. Re-derivation of
Gate Verdict or Class is prohibited.

**§8 SECTION ORDER CONTRACT (C-26)** -- immutable:
```
1. Scope Declaration      2. CH-ID Registration     3. Bracket Opening
4. Domain Reviewers       5. CH-ID Saturation Check  6. Lifecycle Reviewer
7. Bracket Closing        8. Scope Coverage Reconciliation
9. Lens Coverage Table    10. Disposition            11. Master Action Register
12. Cross-Role Signals
```

**§9 FINDING IDENTIFIER CONTRACT (C-42)**
Schema layer: Finding Table declared in TABLE FORMAT CONTRACT; F-ID column is required.
Behavioral layer (independent enforcement path): Every finding row in every reviewer
section MUST carry a populated F-ID value. Omitting F-ID from any finding row is a
contract violation -- the section is non-compliant and its LOCAL GATE LEDGER ROW must
note the defect. Referencing a finding by row position when an F-ID column exists is
a contract violation. All downstream references (action register, CH-ID response
tracking, lens coverage citations) MUST use F-ID values.

**§10 CH-ID CHALLENGE REGISTRATION (C-04, C-43)**
Schema layer: CH-ID Challenge Table declared in TABLE FORMAT CONTRACT; §0 Grounding
column is required, populated at registration time.
Behavioral layer (independent enforcement path): Every CH-ID row MUST carry a §0
Grounding value populated before any reviewer section executes. The §0 Grounding
value names the preamble contract section whose behavioral requirement the challenge
is designed to probe. A CH-ID with an empty or post-hoc §0 Grounding column is
invalid -- it must be removed from the challenge table or deferred to the next review
session. Challenges whose §0 Grounding cannot be traced to a pre-committed preamble
contract are inadmissible.

**§11 CH-ID SATURATION REQUIREMENT (C-27)**
SATURATED: every CH-ID >= 1 DOMAIN response (before LIFECYCLE).
FULLY SATURATED: domain + lifecycle (at BRACKET CLOSING).
BRACKET CLOSING may not PASS when any CH-ID is UNSATURATED without waiver.

**§12 PER-FINDING SEVERITY AGGREGATION CONTRACT (C-30)**
Section Severity = worst(all F-ID severities in section). No editorial assignment.

**§13 LENS COVERAGE TABLE PROTOCOL (C-31, C-33, C-34)**
Post-execution LENS COVERAGE TABLE: ADDRESSED/OPEN per lens.verify entry.
Applicability (HIGH/MEDIUM/LOW) per entry, specific to this artifact.
HIGH-applicability OPEN entries -> ADVISORY-OPEN-LENS items.
DOMAIN COVERAGE GAP-CHECK: uncovered domains -> ADVISORY-GAP items.

**§14 SCOPE SURFACE DOMAIN ANNOTATION (C-36)**
Every IN-SCOPE surface: [DOMAIN: label] at enumeration time.

**§15 SCOPE COVERAGE GATE PROTOCOL (C-29)**
Post-bracket-closing SCOPE COVERAGE RECONCILIATION. GAP surfaces -> ADVISORY-GAP.
No gate ledger row.

**§16 NH DIMENSION TABLE CONTRACT (C-35, C-37, C-38)**
BRACKET OPENING: NH Dimension Comparison Table per TABLE FORMAT CONTRACT. >= 3
dimensions. g_null(initial) derivable from Delta B-A and Delta B-C alone.
BRACKET CLOSING: re-populate columns B and C. g_null(final) derivable from revised
values alone.

**§17 NH TABLE AGGREGATION RULE WITH LIFECYCLE EXTENSION (C-39, C-40, C-41)**
Column A: challenger's opening value, unchanged.
Column B: avg(all DOMAIN B scores + LIFECYCLE B score).
Column C: avg(all DOMAIN C scores + LIFECYCLE C score).

DOMAIN NH SCORE EMISSION (C-40): every DOMAIN section emits NH Dimension Scores
sub-table per TABLE FORMAT CONTRACT before its LOCAL GATE LEDGER ROW.

LIFECYCLE NH SCORE EMISSION (C-41): LIFECYCLE section emits NH Dimension Scores
sub-table per TABLE FORMAT CONTRACT before its LOCAL GATE LEDGER ROW. Same dimension
rows as §16 table. BRACKET CLOSING reads this sub-table alongside DOMAIN sub-tables.
No prose extraction at any step in the NH aggregation chain.

**§18 DOMAIN-AGGREGATE FORMULA (C-24)**
G_domain_agg = median(all DOMAIN gate verdicts). Labeled input to BRACKET CLOSING.

**§19 PRIMARY DRIVER DERIVATION CONTRACT (C-32)**
Precedence (first match): BRACKET CLOSING OVERRIDE > NULL HYPOTHESIS > DOMAIN [first
FAIL] > LIFECYCLE [FAIL] > DOMAIN [first CONDITIONAL] > LIFECYCLE [CONDITIONAL] >
CONSENSUS. Emit `Primary Driver: [value]` at DISPOSITION.

**§20 DEPTH MODE ACKNOWLEDGMENT (C-08)**
deep: all roles. standard: relevant + rationale. quick: >= 3 + abbreviation note.

---

Execute sections per §8 SECTION ORDER CONTRACT. TABLE FORMAT CONTRACT schemas are the
structural declarations; §9 and §10 behavioral contracts are the independent enforcement
paths. Both layers are binding and independently auditable: a compliance check may use
either the TABLE FORMAT CONTRACT or the §§ behavioral contracts to verify field presence,
without reference to the other.

Acknowledge {{artifact_id}}, {{depth}}, {{reviewer_set}} before Step 1.

---

### EXECUTION

Steps 1-13 as V-01. Step 5 finding rows and Step 3 CH-ID registration additionally
satisfy the behavioral requirements of §9 and §10 as independent enforcement paths.

---

## V-03

**Axis**: Inertia framing -- STATUS QUO FRAMING CONTRACT registers named §0-CID
commitments; CH-ID §0 Grounding cites §0-CID values; one-axis threading only;
no TABLE FORMAT CONTRACT (C-44 FAIL, C-47 vacuous)

**Hypothesis**: R17 V-03 introduced STATUS QUO FRAMING CONTRACT with §0-CID registry and
achieved C-45 PASS: CH-ID §0 Grounding column cited §0-CID values rather than generic "§1
DISPOSITION CONTRACT" references. However, C-46 FAIL because §0-CID values only appeared at
axis (a) -- CH-ID §0 Grounding. The three remaining axes (NH Column A initialization, BRACKET
CLOSING OVERRIDE justification, PRIMARY DRIVER attribution) did not consume §0-CID values. V-03
R18 replicates R17 V-03's one-axis structure to establish the C-45 PASS / C-46 FAIL baseline
that V-04 and V-05 will build on. No TABLE FORMAT CONTRACT block (C-44 FAIL makes C-47
vacuous). Predicted score: 270/285.

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

Before any preamble contract executes, the inertia-advocate registers the specific
no-build commitments that justify the status quo. These are the §0-CID values that
every CH-ID must trace to.

```
| §0-CID | Status Quo Commitment (why not building is acceptable) | Strength |
|--------|--------------------------------------------------------|----------|
| §0-C01 | [Existing capability or process covering this need]     | [H/M/L]  |
| §0-C02 | [Cost / risk / complexity argument for status quo]      | [H/M/L]  |
| §0-C03 | [Additional no-build strength claim as needed]          | [H/M/L]  |
```

Populate this table with artifact-specific values before executing any section. The
inertia-advocate requires: (a) every registered CH-ID must trace to a named §0-CID
commitment (CH-ID §0 Grounding column cites the §0-CID value, not a generic preamble
§§ section reference); (b) every finding carries a named F-ID so the disposition audit
can verify whether each finding overturned a specific §0 commitment.

---

### §§ PREAMBLE CONTRACTS

**§1 DISPOSITION ALGEBRA (C-10, C-02)**
HIGH = blocks; MEDIUM = conditions; LOW = advisory.
FAIL -> BLOCKED | >= 1 CONDITIONAL, no FAIL -> CONDITIONAL | all PASS -> READY.
OVERRIDE: OVERRIDE INVOKED: YES | NO labeled field in BRACKET CLOSING.

**§2 CLASS DERIVATION CONTRACT (C-12)**
FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY (optional).

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23)**
Three alternatives (A, B, C). g_null = PASS iff delta_B_A > 0 AND delta_B_C > 0.
g_null = CONDITIONAL iff exactly one delta > 0. g_null = FAIL iff both <= 0.

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
g_null(initial) [BRACKET OPENING] -> g_null(post-domain) [SATURATION CHECK]
-> g_null(final) [BRACKET CLOSING]. GClose = g_null(final) or OVERRIDE INVOKED: YES.

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21)**
Every verdict-emitting section (BRACKET OPENING, all DOMAIN, LIFECYCLE, BRACKET
CLOSING) emits a LOCAL GATE LEDGER ROW:
```
| Gate Verdict | Section Severity | Class | F-ID(s) sourcing this verdict |
```
Verbatim copy to MASTER ACTION REGISTER. No re-derivation.

**§6 NON-VERDICT SECTION EXCLUSION (C-25)**
No gate ledger row from: STATUS QUO FRAMING CONTRACT, §§ preamble, scope, CH-ID
registration, CH-ID saturation check, scope coverage reconciliation, lens coverage table.

**§7 VERBATIM ASSEMBLY PROHIBITION (C-20)**
MASTER ACTION REGISTER: verbatim copy only. Re-derivation prohibited.

**§8 SECTION ORDER CONTRACT (C-26)** -- immutable:
STATUS QUO FRAMING CONTRACT precedes all §§ contracts and all execution sections.
```
1. Scope Declaration      2. CH-ID Registration     3. Bracket Opening
4. Domain Reviewers       5. CH-ID Saturation Check  6. Lifecycle Reviewer
7. Bracket Closing        8. Scope Coverage Reconciliation
9. Lens Coverage Table    10. Disposition            11. Master Action Register
12. Cross-Role Signals
```

**§9 FINDING IDENTIFIER CONTRACT (C-42)**
The inertia-advocate requires named, stable finding identifiers for disposition
auditability. Every finding row:
```
| F-ID | Severity | Surface | Finding | Recommendation |
```
F-ID format: F-NN (F-01, F-02, ...). NOT a positional row number. All downstream
references use F-ID values. Row-positional references are contract violations.

**§10 CH-ID CHALLENGE REGISTRATION (C-04, C-43)**
CH-ID tracing table:
```
| CH-ID | Challenge Statement | §0 Grounding | [Section columns] |
```
§0 Grounding column: cites the §0-CID value from the STATUS QUO FRAMING CONTRACT
registry that this challenge is designed to probe (e.g., "§0-C01 -- tests whether
existing capability argument holds under the proposed build"). Every CH-ID must
carry a §0-CID citation. Challenges that cannot be grounded in a registered §0-CID
are invalid and may not be registered.

**§11 CH-ID SATURATION REQUIREMENT (C-27)**
SATURATED before LIFECYCLE. FULLY SATURATED at BRACKET CLOSING. BRACKET CLOSING
may not PASS when any CH-ID is UNSATURATED without waiver.

**§12 PER-FINDING SEVERITY AGGREGATION CONTRACT (C-30)**
Section Severity = worst(F-ID severities in section). No editorial assignment.

**§13 LENS COVERAGE TABLE PROTOCOL (C-31, C-33, C-34)**
Post-execution LENS COVERAGE TABLE: ADDRESSED/OPEN per lens.verify entry.
Applicability per entry specific to this artifact. HIGH-applicability OPEN ->
ADVISORY-OPEN-LENS items. DOMAIN COVERAGE GAP-CHECK -> ADVISORY-GAP items.

**§14 SCOPE SURFACE DOMAIN ANNOTATION (C-36)**
Every IN-SCOPE surface: [DOMAIN: label] at enumeration time.

**§15 SCOPE COVERAGE GATE PROTOCOL (C-29)**
Post-bracket-closing reconciliation. GAP surfaces -> ADVISORY-GAP. No ledger row.

**§16 NH DIMENSION TABLE CONTRACT (C-35, C-37, C-38)**
BRACKET OPENING: NH Dimension Comparison Table (A, B, C columns; >= 3 dimensions).
Delta B-A and Delta B-C computed. g_null(initial) derivable from deltas alone.
BRACKET CLOSING: re-populate columns B and C. g_null(final) from revised values.

**§17 NH TABLE AGGREGATION RULE WITH LIFECYCLE EXTENSION (C-39, C-40, C-41)**
Column A: challenger's opening value, unchanged.
Column B: avg(all DOMAIN B scores + LIFECYCLE B score).
Column C: avg(all DOMAIN C scores + LIFECYCLE C score).

DOMAIN NH SCORE EMISSION (C-40): each DOMAIN section emits NH Dimension Scores
sub-table before its gate ledger row.

LIFECYCLE NH SCORE EMISSION (C-41): LIFECYCLE section emits NH Dimension Scores
sub-table before its gate ledger row. Same dimensions as §16 table. BRACKET CLOSING
reads LIFECYCLE sub-table alongside DOMAIN sub-tables for columns B and C aggregation.

**§18 DOMAIN-AGGREGATE FORMULA (C-24)**
G_domain_agg = median(all DOMAIN gate verdicts). Labeled input to BRACKET CLOSING.

**§19 PRIMARY DRIVER DERIVATION CONTRACT (C-32)**
Precedence: BRACKET CLOSING OVERRIDE > NULL HYPOTHESIS (§0-CID held by challenger)
> DOMAIN [first FAIL] > LIFECYCLE [FAIL] > DOMAIN [first CONDITIONAL] > LIFECYCLE
[CONDITIONAL] > CONSENSUS. Emit `Primary Driver: [value]` at DISPOSITION.

**§20 DEPTH MODE ACKNOWLEDGMENT (C-08)**
deep: all roles. standard: relevant + rationale. quick: >= 3 + note.

---

Execute sections per §8 SECTION ORDER CONTRACT. The STATUS QUO FRAMING CONTRACT
§0-CID registry is the ground truth for CH-ID §0 Grounding citations (axis a only).
Every F-ID is the audit trail the inertia-advocate requires to verify findings against
§0-CID commitments.

Acknowledge {{artifact_id}}, {{depth}}, {{reviewer_set}} before Step 1.

---

### EXECUTION

Steps 1-13 as V-01. Step 3 CH-ID registration populates §0 Grounding with §0-CID
values from STATUS QUO FRAMING CONTRACT registry.

---

## V-04

**Axis**: Output format + Inertia framing (two-axis) -- TABLE FORMAT CONTRACT +
STATUS QUO FRAMING CONTRACT §0-CID registry + dual-path behavioral enforcement;
§0-CID threads axis (a) only; predicted 280/285

**Hypothesis**: No R17 variant achieved C-44+C-45+C-47 without also having C-46.
R17 V-04 had C-44+C-47 (no §0-CID). R17 V-03 had C-45 (no TABLE FORMAT CONTRACT).
R17 V-05 had all four. The V-04 R18 hybrid places STATUS QUO FRAMING CONTRACT (inertia
framing axis) before TABLE FORMAT CONTRACT (output format axis), then §§ contracts carry
independent behavioral paths for both C-42 F-ID and C-43 §0 Grounding. The §0 Grounding
behavioral contract (§10) cites §0-CID values from the STATUS QUO FRAMING CONTRACT
registry, satisfying C-45. The TABLE FORMAT CONTRACT schema declarations (C-44) and the
independent behavioral §§ contracts (C-47) are both present. §0-CID values thread only
through axis (a) -- CH-ID §0 Grounding column -- not through NH Column A initialization,
BRACKET CLOSING OVERRIDE justification, or PRIMARY DRIVER attribution. C-46 FAIL is
intentional: V-05 R18 will add the remaining three axes. Predicted score: 280/285.

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
ground truth for all CH-ID §0 Grounding citations.

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

**LOCAL GATE LEDGER ROW** and **MASTER ACTION REGISTER ROW**: same schemas as V-01.

---

### §§ PREAMBLE CONTRACTS

**§1 DISPOSITION ALGEBRA (C-10, C-02)**
HIGH = blocks; MEDIUM = conditions; LOW = advisory.
FAIL -> BLOCKED | >= 1 CONDITIONAL, no FAIL -> CONDITIONAL | all PASS -> READY.
OVERRIDE: OVERRIDE INVOKED: YES | NO in BRACKET CLOSING.

**§2 CLASS DERIVATION CONTRACT (C-12)**
FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY (optional).

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23)**
Three alternatives (A, B, C). g_null = PASS iff delta_B_A > 0 AND delta_B_C > 0.
g_null = CONDITIONAL iff exactly one delta > 0. g_null = FAIL iff both <= 0.

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
g_null(initial) [BRACKET OPENING] -> g_null(post-domain) [SATURATION CHECK]
-> g_null(final) [BRACKET CLOSING]. GClose = g_null(final) or OVERRIDE INVOKED: YES.

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21)**
Universal coverage: BRACKET OPENING + all DOMAIN + LIFECYCLE + BRACKET CLOSING.
Schema per TABLE FORMAT CONTRACT. Verbatim copy to MASTER ACTION REGISTER.

**§6 NON-VERDICT SECTION EXCLUSION (C-25)**
No gate ledger row from: STATUS QUO FRAMING CONTRACT, TABLE FORMAT CONTRACT, §§
preamble, scope, CH-ID registration, CH-ID saturation check, scope coverage
reconciliation, lens coverage table.

**§7 VERBATIM ASSEMBLY PROHIBITION (C-20)**
MASTER ACTION REGISTER: verbatim copy. Re-derivation prohibited.

**§8 SECTION ORDER CONTRACT (C-26)** -- immutable:
```
[STATUS QUO FRAMING CONTRACT -- pre-execution, complete]
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
the section's LOCAL GATE LEDGER ROW must note the defect. Referencing a finding by
row position is a contract violation. All downstream references use F-ID values.

**§10 CH-ID CHALLENGE REGISTRATION (C-04, C-43)**
Schema layer: CH-ID Challenge Table declared in TABLE FORMAT CONTRACT. §0 Grounding
column required, populated at registration time with a §0-CID value from STATUS QUO
FRAMING CONTRACT.
Behavioral layer (independent enforcement path): Every CH-ID MUST carry a §0 Grounding
value that names a specific §0-CID from the STATUS QUO FRAMING CONTRACT registry. A
§0 Grounding value that cites a generic preamble §§ section ("§1 DISPOSITION ALGEBRA")
rather than a named §0-CID commitment does NOT satisfy this contract. A CH-ID with
empty or non-§0-CID §0 Grounding is invalid and must be removed.

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
BRACKET OPENING: NH Dimension Comparison Table per TABLE FORMAT CONTRACT. >= 3
dimensions. g_null derivable from Delta B-A and Delta B-C alone. BRACKET CLOSING:
re-populate columns B and C. g_null(final) derivable from revised values alone.

**§17 NH TABLE AGGREGATION RULE WITH LIFECYCLE EXTENSION (C-39, C-40, C-41)**
Column A: challenger's opening value, unchanged.
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
Emit `Primary Driver: [value]` at DISPOSITION.

**§20 DEPTH MODE ACKNOWLEDGMENT (C-08)**
deep: all roles. standard: relevant + rationale. quick: >= 3 + note.

---

Execute sections per §8. STATUS QUO FRAMING CONTRACT §0-CID registry is the ground
truth for CH-ID §0 Grounding citations. TABLE FORMAT CONTRACT schemas and §§ behavioral
contracts are complementary and independently auditable: the TABLE FORMAT CONTRACT
declares what each field is; §9 and §10 declare when it must be populated and what
constitutes a violation.

Acknowledge {{artifact_id}}, {{depth}}, {{reviewer_set}} before Step 1.

---

### EXECUTION

Steps 1-13 as V-01. Step 3 CH-ID registration populates §0 Grounding with §0-CID
values from STATUS QUO FRAMING CONTRACT. Step 5 finding rows and Step 3 CH-ID rows
satisfy both the TABLE FORMAT CONTRACT schema and the §9/§10 independent behavioral
contracts.

---

## V-05

**Axis**: Output format + Inertia framing + §0-CID four-axis pipeline (three-axis) --
C-44 + C-45 + C-46 + C-47; §0-CID PIPELINE THREADING CONTRACT pre-commits all four
axes as named structural positions; predicted 285/285

**Hypothesis**: R17 V-05 achieved all four criteria, but C-46 threading was declared
only in the closing execution note ("§0-CID values flow through: (a)...(b)...(c)...(d)...")
rather than as a named pre-execution contract. An auditor wanting to verify C-46 compliance
had to read the closing note and infer the threading requirement. V-05 R18 elevates the four-
axis threading requirement to a named structural contract (§0-CID PIPELINE THREADING CONTRACT)
declared before execution, co-located with STATUS QUO FRAMING CONTRACT and TABLE FORMAT
CONTRACT. Each axis is named, defined, and pre-committed. BRACKET CLOSING explicitly receives
§0-CID input at axis (c). PRIMARY DRIVER DERIVATION CONTRACT at §19 explicitly references
§0-CID values at axis (d). The test: does pre-committing the four-axis pipeline as a named
contract (vs. a closing note) increase C-46 compliance reliability? Predicted score: 285/285.

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
ground truth for all four §0-CID pipeline axes.

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
Every CH-ID §0 Grounding column value MUST cite a named §0-CID from the STATUS QUO
FRAMING CONTRACT registry. Generic preamble §§ section citations are not permitted.

**Axis B -- NH Dimension Table Column A initialization** (at BRACKET OPENING):
Column A values in the NH Dimension Comparison Table MUST be initialized from STATUS
QUO FRAMING CONTRACT §0-CID strength ratings. The §0-CID commitments constitute the
status-quo baseline; Column A scores reflect the claimed strength of those commitments
on each dimension.

**Axis C -- BRACKET CLOSING OVERRIDE justification** (if OVERRIDE INVOKED: YES):
Any BRACKET CLOSING OVERRIDE declaration MUST name the specific §0-CID commitment
being superseded (e.g., "OVERRIDE: domain evidence demonstrates §0-C02 cost argument
no longer holds given [evidence]"). A generic justification without §0-CID citation
does not satisfy the BRACKET CLOSING OVERRIDE contract.

**Axis D -- PRIMARY DRIVER attribution** (at DISPOSITION):
When PRIMARY DRIVER is NULL HYPOTHESIS or BRACKET CLOSING OVERRIDE, the `Primary
Driver:` field MUST cite the §0-CID value(s) that drove the attribution (e.g.,
"Primary Driver: NULL HYPOTHESIS (§0-C01 cost argument prevails)"). CONSENSUS and
DOMAIN-driven attributions do not require §0-CID citation.

All four axes must be populated before the review is considered complete. The execution
closing note confirms four-axis data flow was achieved.

---

### TABLE FORMAT CONTRACT

All structured tables conform to schemas declared here.

**Finding Table** (every reviewer section):
```
| F-ID | Severity | Surface | Finding | Recommendation |
```
`F-ID`: named stable identifier (F-01, F-02, ...). NOT positional. All downstream
references use F-ID values.

**CH-ID Challenge Table** (before BRACKET OPENING):
```
| CH-ID | Challenge Statement | §0 Grounding | [Section response columns] |
```
`§0 Grounding`: required. Cites §0-CID value from STATUS QUO FRAMING CONTRACT per
§0-CID PIPELINE THREADING CONTRACT Axis A. Generic preamble §§ citations are invalid.

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
OVERRIDE: OVERRIDE INVOKED: YES | NO in BRACKET CLOSING, naming the §0-CID being
overridden per §0-CID PIPELINE THREADING CONTRACT Axis C.

**§2 CLASS DERIVATION CONTRACT (C-12)**
FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY (optional).

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23)**
Three alternatives (A, B, C). g_null = PASS iff delta_B_A > 0 AND delta_B_C > 0.
g_null = CONDITIONAL iff exactly one delta > 0. g_null = FAIL iff both <= 0.

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
g_null(initial) [BRACKET OPENING] -> g_null(post-domain) [SATURATION CHECK]
-> g_null(final) [BRACKET CLOSING]. GClose = g_null(final) or OVERRIDE INVOKED: YES
with named §0-CID per §0-CID PIPELINE THREADING CONTRACT Axis C.

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
section MUST carry a populated F-ID value. Omitting F-ID is a contract violation.
Positional row references are contract violations. All downstream references use F-ID
values. The inertia-advocate traces each F-ID to verify whether the finding overturned
a specific §0-CID commitment.

**§10 CH-ID CHALLENGE REGISTRATION (C-04, C-43)**
Schema layer: CH-ID Challenge Table declared in TABLE FORMAT CONTRACT. §0 Grounding
column required, populated at registration time with a §0-CID value.
Behavioral layer (independent enforcement path): Every CH-ID MUST carry a §0 Grounding
value naming a specific §0-CID from STATUS QUO FRAMING CONTRACT per §0-CID PIPELINE
THREADING CONTRACT Axis A. A §0 Grounding value citing a generic preamble §§ section
reference does NOT satisfy this contract. CH-IDs without a valid §0-CID citation are
invalid.

**§11 CH-ID SATURATION REQUIREMENT (C-27)**
SATURATED before LIFECYCLE. FULLY SATURATED at BRACKET CLOSING. BRACKET CLOSING
may not PASS when any CH-ID is UNSATURATED without waiver citing §0-CID justification.

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
Column A: challenger's §16 opening values (from §0-CID strength ratings), unchanged.
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
Precedence: BRACKET CLOSING OVERRIDE (cite §0-CID overridden per Axis C) > NULL
HYPOTHESIS (cite §0-CID held per Axis D) > DOMAIN [first FAIL] > LIFECYCLE [FAIL]
> DOMAIN [first CONDITIONAL] > LIFECYCLE [CONDITIONAL] > CONSENSUS.
Emit `Primary Driver: [value]` at DISPOSITION. When driver is NULL HYPOTHESIS or
BRACKET CLOSING OVERRIDE, append the §0-CID citation per §0-CID PIPELINE THREADING
CONTRACT Axis D.

**§20 DEPTH MODE ACKNOWLEDGMENT (C-08)**
deep: all roles. standard: relevant + rationale. quick: >= 3 + note.

---

Execute sections per §8. The STATUS QUO FRAMING CONTRACT, §0-CID PIPELINE THREADING
CONTRACT, TABLE FORMAT CONTRACT, and §§ behavioral contracts form a four-layer pre-
commitment architecture. Before closing, confirm four-axis §0-CID data flow:

```
Axis A confirmation: every CH-ID §0 Grounding column cites a §0-CID value [YES/NO]
Axis B confirmation: NH Column A values initialized from §0-CID strength ratings [YES/NO]
Axis C confirmation: if OVERRIDE INVOKED: YES -- §0-CID named in justification [YES/NO/NA]
Axis D confirmation: Primary Driver cites §0-CID when driver is NH or OVERRIDE [YES/NO/NA]
```

All four axes YES (or NA where not applicable) before emitting DISPOSITION.

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
QUO FRAMING CONTRACT registry (Axis A). Challenges without §0-CID citation invalid.

**Step 4: BRACKET OPENING**
- State null hypothesis: what the team does today, why it is acceptable.
- Populate NH Dimension Comparison Table: Column A values from §0-CID strength ratings
  (Axis B). >= 3 dimensions. Emit g_null(initial) as labeled field.
- Emit LOCAL GATE LEDGER ROW per TABLE FORMAT CONTRACT.

**Step 5: DOMAIN REVIEWER SECTIONS** (one per role, manifest order)
- State role name and lens.
- Produce finding rows per Finding Table schema (§9 schema + behavioral layers).
- Respond to relevant CH-IDs.
- Emit NH Dimension Scores sub-table per TABLE FORMAT CONTRACT.
- Emit LOCAL GATE LEDGER ROW. Section Severity = worst(finding severities) per §12.

**Step 6: CH-ID SATURATION CHECK**
- Verify SATURATED tier.
- Emit g_null(post-domain) per §4 Stage 2. No gate ledger row.

**Step 7: LIFECYCLE REVIEWER SECTION**
- Evaluate lifecycle phases (creation, active use, change, deprecation, removal).
- Produce finding rows per Finding Table schema.
- Respond to relevant CH-IDs.
- Emit NH Dimension Scores sub-table per TABLE FORMAT CONTRACT.
- Emit LOCAL GATE LEDGER ROW with g_lifecycle labeled.

**Step 8: BRACKET CLOSING**
- Receive G_domain_agg (§18), g_lifecycle, all domain/lifecycle verdicts as labeled inputs.
- Re-populate NH Dimension Comparison Table columns B and C per §17.
- Derive g_null(final) from revised table per §3 (Stage 3 of §4).
- Emit OVERRIDE INVOKED: YES | NO. If YES: name the §0-CID being superseded (Axis C).
- Emit LOCAL GATE LEDGER ROW.

**Step 9: SCOPE COVERAGE RECONCILIATION** (per §15; no gate ledger row)

**Step 10: LENS COVERAGE TABLE** (per §13; no gate ledger row)

**Step 11: DISPOSITION**
- Apply §1 DISPOSITION ALGEBRA.
- Emit `DISPOSITION: READY | CONDITIONAL | BLOCKED` as labeled field.
- Emit `Primary Driver: [value]` per §19. If NULL HYPOTHESIS or OVERRIDE: append
  §0-CID citation per Axis D.

**Step 12: MASTER ACTION REGISTER**
Verbatim copy of LOCAL GATE LEDGER ROWS (§7). Append ADVISORY-GAP and
ADVISORY-OPEN-LENS items. No re-derivation.

**Step 13: CROSS-ROLE SIGNALS**
Synthesis narrative. Name >= 1 cross-role conflict or convergence. Reference all
three g_null stages. Explain the disposition.

**§0-CID four-axis pipeline confirmation** (before closing):
```
Axis A (CH-ID §0 Grounding -- §0-CID citations):      [YES/NO]
Axis B (NH Column A -- §0-CID strength initialization): [YES/NO]
Axis C (BRACKET CLOSING OVERRIDE -- §0-CID named):    [YES/NO/NA]
Axis D (PRIMARY DRIVER -- §0-CID cited):               [YES/NO/NA]
```
