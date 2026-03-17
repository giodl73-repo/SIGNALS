---
skill: quest-golden
skill_target: org-review
date: 2026-03-17
rounds: 20
rubric_final: org-review-rubric-v19-2026-03-17.md
score: 315
status: GOLDEN
---

# org-review — Golden Prompt

**Source**: V-05 of R20 (315/315 under v19), simplified at QU5 (20% reduction, all 53 criteria PASS)
**Prompt body**: QU5 simplified version (preferred over V-05 verbatim per simplification PASS)

---

## Golden Prompt Body

You are running `/org-review`.

Inputs:
```
{{artifact_id}}: [artifact name or path under review]
{{depth}}: [standard | deep | quick]
{{reviewer_set}}: [auto | all | comma-separated role names from .craft/roles/]
```

Acknowledge injected values before executing any section.

---

### STATUS QUO FRAMING CONTRACT (inertia-advocate pre-commitment)

Before table schemas or behavioral contracts are declared, register the no-build
commitments that justify not building {{artifact_id}}.

```
| §0-CID | Status Quo Commitment (why not building is acceptable) | Strength |
|--------|--------------------------------------------------------|----------|
| §0-C01 | [Existing capability or process covering this need]     | [H/M/L]  |
| §0-C02 | [Cost / risk / complexity argument for status quo]      | [H/M/L]  |
| §0-C03 | [Additional no-build strength claim as needed]          | [H/M/L]  |
```

Populate with artifact-specific values before any other section.

---

### §0-CID PIPELINE THREADING CONTRACT (four-axis pre-commitment)

Each axis names the execution position, TABLE FORMAT CONTRACT field (schema layer),
and §§ contract (behavioral layer).

**Axis A -- CH-ID §0 Grounding citations** (at CH-ID REGISTRATION TABLE):
Every CH-ID §0 Grounding column value MUST cite a named §0-CID from the STATUS
QUO FRAMING CONTRACT registry. Generic preamble §§ section citations are not
permitted.
- Schema layer governed: TABLE FORMAT CONTRACT CH-ID Challenge Table §0 Grounding
  field.
- Behavioral layer enforced by: §10 CH-ID CHALLENGE REGISTRATION behavioral contract.

**Axis B -- NH Dimension Table Column A initialization** (at BRACKET OPENING):
Column A values in the NH Dimension Comparison Table MUST be initialized from
STATUS QUO FRAMING CONTRACT §0-CID strength ratings.
- Schema layer governed: TABLE FORMAT CONTRACT NH Dimension Comparison Table Column A
  field.
- Behavioral layer enforced by: §16 NH DIMENSION TABLE CONTRACT.

**Axis C -- BRACKET CLOSING OVERRIDE justification** (if OVERRIDE INVOKED: YES):
Any BRACKET CLOSING OVERRIDE declaration MUST name the specific §0-CID commitment
being superseded.
- Schema layer governed: TABLE FORMAT CONTRACT LOCAL GATE LEDGER ROW (BRACKET
  CLOSING row, OVERRIDE INVOKED field).
- Behavioral layer enforced by: §1 DISPOSITION ALGEBRA OVERRIDE clause and §4 NULL
  HYPOTHESIS PROGRESSION CONTRACT GClose requirement.

**Axis D -- PRIMARY DRIVER attribution** (at DISPOSITION):
When PRIMARY DRIVER is NULL HYPOTHESIS or BRACKET CLOSING OVERRIDE, the
`Primary Driver:` field MUST cite the §0-CID value(s) that drove the attribution.
- Schema layer governed: DISPOSITION labeled field at Step 11.
- Behavioral layer enforced by: §19 PRIMARY DRIVER DERIVATION CONTRACT.

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
HIGH / MEDIUM / LOW.

**CH-ID Challenge Table** (before BRACKET OPENING):
```
| CH-ID | Challenge Statement | §0 Grounding | [Section response columns] |
```
`§0 Grounding`: required. Cites the §0-CID value from STATUS QUO FRAMING CONTRACT
per §0-CID PIPELINE THREADING CONTRACT Axis A. Populated at registration time.
Challenges without a §0-CID Axis A citation are invalid.

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

**LIFECYCLE PHASE GATE SUB-TABLE** (Step 7 only):
```
| Phase | Phase Verdict | F-ID(s) | Notes |
```
Phases: creation | active-use | change-management | deprecation | removal.
G_lifecycle = worst(Phase Verdict column). Emitted before LOCAL GATE LEDGER ROW.

**MASTER ACTION REGISTER ROW**:
```
| F-ID | Gate Verdict | Class | Section | Finding Summary | Recommendation |
```

**PIPELINE COMPLIANCE LEDGER** (emitted once, before Step 11 DISPOSITION):
```
| Axis | Execution Position            | Schema Field Governed                   | Behavioral Contract               | Compliant   |
|------|-------------------------------|-----------------------------------------|-----------------------------------|-------------|
| A    | CH-ID REGISTRATION TABLE      | CH-ID Challenge Table §0 Grounding      | §10 CH-ID CHALLENGE REGISTRATION  | [YES/NO]    |
| B    | BRACKET OPENING               | NH Dimension Comparison Table Col A     | §16 NH DIMENSION TABLE CONTRACT   | [YES/NO]    |
| C    | BRACKET CLOSING (if OVERRIDE) | LOCAL GATE LEDGER ROW BRACKET CLOSING   | §1 ALGEBRA + §4 PROGRESSION       | [YES/NO/NA] |
| D    | DISPOSITION                   | DISPOSITION Primary Driver field        | §19 PRIMARY DRIVER DERIVATION     | [YES/NO/NA] |
```
Populate `Compliant` column only. Do not alter pre-filled columns.

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
g_null = PASS iff delta_B_A > 0 AND delta_B_C > 0.
g_null = CONDITIONAL iff exactly one delta > 0. g_null = FAIL iff both <= 0.

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
g_null(initial) [BRACKET OPENING] -> g_null(post-domain) [SATURATION CHECK]
-> g_null(final) [BRACKET CLOSING]. GClose = g_null(final) or OVERRIDE INVOKED: YES
per §1.

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21)**
Universal coverage: BRACKET OPENING + all DOMAIN + LIFECYCLE + BRACKET CLOSING.
Schema per TABLE FORMAT CONTRACT. Verbatim copy to MASTER ACTION REGISTER.

**§6 NON-VERDICT SECTION EXCLUSION (C-25)**
No gate ledger row from: STATUS QUO FRAMING CONTRACT, §0-CID PIPELINE THREADING
CONTRACT, TABLE FORMAT CONTRACT, §§ preamble, scope, CH-ID registration, CH-ID
saturation check, scope coverage reconciliation, lens coverage table, REVIEWER
PRIORITY MANIFEST, PIPELINE COMPLIANCE LEDGER.

**§7 VERBATIM ASSEMBLY PROHIBITION (C-20)**
MASTER ACTION REGISTER: verbatim copy. Re-derivation prohibited.

**§8 SECTION ORDER CONTRACT (C-26)** -- immutable:
```
[STATUS QUO FRAMING CONTRACT -- pre-execution, complete]
[§0-CID PIPELINE THREADING CONTRACT -- pre-execution, complete]
[TABLE FORMAT CONTRACT -- pre-execution, complete]
[§§ PREAMBLE -- pre-execution, complete]
[REVIEWER PRIORITY MANIFEST -- pre-execution, complete]
1. Scope Declaration      2. CH-ID Registration     3. Bracket Opening
4. Domain Reviewers       5. CH-ID Saturation Check  6. Lifecycle Reviewer
   [6a creation, 6b active-use, 6c change-management, 6d deprecation, 6e removal]
7. Bracket Closing        8. Scope Coverage Reconciliation
9. Lens Coverage Table    10a. Pipeline Compliance Ledger  10b. Disposition
11. Master Action Register  12. Cross-Role Signals
```

**§9 FINDING IDENTIFIER CONTRACT (C-42)**
Schema layer: Finding Table declared in TABLE FORMAT CONTRACT. F-ID column required.
Behavioral layer (independent enforcement path): Every finding row in every reviewer
section MUST carry a populated F-ID value. Omitting F-ID is a contract violation --
the section's LOCAL GATE LEDGER ROW must note the defect. Positional row references
are contract violations.

**§10 CH-ID CHALLENGE REGISTRATION (C-04, C-43)**
Schema layer: CH-ID Challenge Table declared in TABLE FORMAT CONTRACT. §0 Grounding
column required, populated at registration time with a §0-CID value per §0-CID
PIPELINE THREADING CONTRACT Axis A (schema layer).
Behavioral layer (independent enforcement path): Every CH-ID MUST carry a §0 Grounding
value naming a specific §0-CID from the STATUS QUO FRAMING CONTRACT registry per
§0-CID PIPELINE THREADING CONTRACT Axis A (behavioral layer). CH-IDs without a
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
§0-CID PIPELINE THREADING CONTRACT Axis B. >= 3 dimensions.
g_null(initial) derivable from Delta B-A and Delta B-C alone. BRACKET CLOSING:
re-populate columns B and C. g_null(final) derivable from revised values alone.

**§17 NH TABLE AGGREGATION RULE WITH LIFECYCLE EXTENSION (C-39, C-40, C-41)**
Column A: §0-CID-initialized opening values, unchanged.
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
THREADING CONTRACT Axis D) > DOMAIN [first FAIL] > LIFECYCLE [FAIL] > DOMAIN
[first CONDITIONAL] > LIFECYCLE [CONDITIONAL] > CONSENSUS. Emit `Primary Driver:
[value]` at DISPOSITION. When driver is NULL HYPOTHESIS or BRACKET CLOSING OVERRIDE,
append the §0-CID citation per §0-CID PIPELINE THREADING CONTRACT Axis D.

**§20 DEPTH MODE ACKNOWLEDGMENT (C-08)**
deep: all roles. standard: relevant + rationale. quick: >= 3 + note.

**§21 LIFECYCLE PHASE GATE PROTOCOL**
Step 7 LIFECYCLE REVIEWER runs five sub-steps (7a-7e). Each sub-step evaluates one
lifecycle phase and emits one finding row (minimum) using the Finding Table schema.
Phase verdict (PASS/CONDITIONAL/FAIL) is derived from the worst finding severity in
that phase per §12. G_lifecycle = worst(7a-7e phase verdicts). Emit LIFECYCLE PHASE
GATE SUB-TABLE per TABLE FORMAT CONTRACT before the section LOCAL GATE LEDGER ROW.
No phase may be skipped; write "No findings -- PASS" if clean.

---

### REVIEWER PRIORITY MANIFEST

Read `.craft/roles/{{reviewer_set_resolved}}/`. Assign slots in execution priority
order.

```
| Priority | Slot        | Role Name        | Finding-Density Basis           |
|----------|-------------|------------------|---------------------------------|
| 1 (fixed)| CHALLENGER  | [ROLE_NAME]      | Inertia-advocate: always first  |
| 2        | DOMAIN-1    | [ROLE_NAME]      | [Technical/architecture reason] |
| 3+       | DOMAIN-2..N | [ROLE_NAME...]   | [PM/product/ops in order]       |
| N-1      | LIFECYCLE   | [ROLE_NAME]      | Lifecycle: always before close  |
| N (fixed)| CHALLENGER  | [ROLE_NAME]      | Bracket closing: always last    |
```

CHALLENGER occupies first and last slots (fixed). Domain ordering is advisory;
revise in Step 1 with a stated reason. LIFECYCLE occupies slot N-1 (fixed). State
total role count.

---

Execute sections per §8. Before DISPOSITION, complete the PIPELINE COMPLIANCE
LEDGER per TABLE FORMAT CONTRACT schema, then apply §1 DISPOSITION ALGEBRA.

Acknowledge {{artifact_id}}, {{depth}}, {{reviewer_set}} before Step 1.

---

### EXECUTION

**Step 1: Acknowledge inputs**
```
Artifact: {{artifact_id}}
Depth: {{depth}}
Reviewer set: {{reviewer_set}}
Role selection rationale: [state if depth=standard; confirm REVIEWER PRIORITY
  MANIFEST slot assignments]
```

**Step 2: SCOPE DECLARATION**
Enumerate all IN-SCOPE surfaces with [DOMAIN: label] per §14. State OUT-OF-SCOPE.

**Step 3: CH-ID REGISTRATION TABLE**
Register all challenges per §10. §0 Grounding column: cite §0-CID value from STATUS
QUO FRAMING CONTRACT registry per §0-CID PIPELINE THREADING CONTRACT Axis A.

**Step 4: BRACKET OPENING**
- State null hypothesis: what the team does today, why it is acceptable.
- Populate NH Dimension Comparison Table: Column A from §0-CID strength ratings per
  Axis B. >= 3 dimensions. Emit g_null(initial) as labeled field.
- Emit LOCAL GATE LEDGER ROW.

**Step 5: DOMAIN REVIEWER SECTIONS** (one per role, REVIEWER PRIORITY MANIFEST order)
- State role name and lens (one sentence).
- Produce finding rows per Finding Table schema (§9 schema + behavioral layers).
- Respond to relevant CH-IDs (per §10).
- Emit NH Dimension Scores sub-table per §16.
- Emit LOCAL GATE LEDGER ROW. Section Severity = worst(finding severities) per §12.

**Step 6: CH-ID SATURATION CHECK**
- Verify SATURATED tier. Emit g_null(post-domain) per §4 Stage 2. No gate ledger row.

**Step 7: LIFECYCLE REVIEWER SECTION** (five sub-steps per §21)
- State role name.
- 7a creation / 7b active-use / 7c change-management / 7d deprecation / 7e removal.
  Each sub-step: finding row(s) + phase verdict.
- After 7a-7e: emit LIFECYCLE PHASE GATE SUB-TABLE. Derive G_lifecycle.
- Respond to relevant CH-IDs. Emit NH Dimension Scores sub-table (Axis B per §16).
- Emit LOCAL GATE LEDGER ROW with G_lifecycle labeled.

**Step 8: BRACKET CLOSING**
- Receive G_domain_agg (§18), g_lifecycle, all domain/lifecycle verdicts.
- Re-populate NH Dimension Comparison Table columns B and C per §17.
- Derive g_null(final) from revised table per §3 (Stage 3 of §4).
- Emit OVERRIDE INVOKED: YES | NO. If YES: name §0-CID being superseded per Axis C.
- Emit LOCAL GATE LEDGER ROW.

**Step 9: SCOPE COVERAGE RECONCILIATION** (per §15; no gate ledger row)

**Step 10: LENS COVERAGE TABLE** (per §13; no gate ledger row)

**Step 10a: PIPELINE COMPLIANCE LEDGER**
Populate the PIPELINE COMPLIANCE LEDGER table (TABLE FORMAT CONTRACT schema).
Verify each axis was executed correctly. Fill `Compliant` column. A NO entry is a
finding; emit ADVISORY-OBS in MASTER ACTION REGISTER if present.

**Step 11: DISPOSITION**
- Apply §1 DISPOSITION ALGEBRA to gate verdict vector.
- Emit `DISPOSITION: READY | CONDITIONAL | BLOCKED` as labeled field.
- Emit `Primary Driver: [value]` per §19. If NULL HYPOTHESIS or OVERRIDE:
  cite §0-CID per Axis D.

**Step 12: MASTER ACTION REGISTER**
Verbatim copy of LOCAL GATE LEDGER ROWS (§7). Append ADVISORY-GAP,
ADVISORY-OPEN-LENS, and ADVISORY-OBS items. No re-derivation.

**Step 13: CROSS-ROLE SIGNALS**
Synthesis narrative. Name >= 1 cross-role conflict or convergence. Reference all
role sections by name. No new findings -- observations only.

---

## What Made It Golden

Three structural patterns distinguish V-05 from the V-01 baseline, each independently
scoring 300/300 under v18 and together producing 315/315 under v19.

### 1. Three-axis convergence (C-51 + C-52 + C-53, 15 pts)

V-05 is the only variant in R20 that passes all three new aspirational criteria
simultaneously. V-04 achieves 310/315 (C-51 + C-52) but lacks the PIPELINE
COMPLIANCE LEDGER. The three axes are architecturally independent -- role sequencing,
lifecycle sub-step depth, and pipeline audit format -- yet combine without contract
conflict. Proof that structural pre-commitments compose additively when each is
scoped to its own execution position.

### 2. REVIEWER PRIORITY MANIFEST as contractually locked execution sequence (C-51)

V-01 through V-04 imply reviewer order from template structure. V-05 (and V-01/V-04)
makes it a named pre-execution block: CHALLENGER fixed-first and fixed-last, DOMAIN
roles by finding-density expectation, LIFECYCLE at N-1. The block is named in §6 as
a non-verdict exclusion -- converting reviewer sequence from editorial convention to
a structurally auditable contract. Auditors can verify role order before examining
any finding.

### 3. Lifecycle review as five independently-verdicted phases (C-52)

V-02/V-04/V-05 expand Step 7 into sub-steps 7a-7e (creation, active-use,
change-management, deprecation, removal). Each phase emits its own finding row and
phase verdict. G_lifecycle = worst(phase verdicts). The LIFECYCLE PHASE GATE SUB-TABLE
schema is declared in TABLE FORMAT CONTRACT and the sub-steps appear in §8 SECTION
ORDER CONTRACT. Lifecycle phase sequencing becomes as contractually immutable as
section sequencing -- a phase cannot be skipped or merged without a contract violation.

### 4. PIPELINE COMPLIANCE LEDGER as pre-committed post-bracket audit section (C-53)

V-03/V-05 replace the ad-hoc four-axis yes/no confirmation block with a named step
(10a) carrying its own TABLE FORMAT CONTRACT schema, §6 gate ledger exclusion, and
fixed position in §8 section order. The four pipeline axes are pre-filled in the
table; the reviewer fills only the `Compliant` column. A NO entry triggers an
ADVISORY-OBS item in the MASTER ACTION REGISTER. The pipeline compliance audit is now
structural -- declared before execution, enforced at a specific section, with output
in a schema that can be verified independently of prose context.

### 5. Simplification validated at 20% word reduction (QU5 PASS)

The ~610 words removed from V-05 to produce the simplified body were entirely
documentary: cross-reference summaries, layer annotation labels, explanatory glosses
on rules already stated in axis blocks. All 53 criteria pass in the simplified
version. This confirms the structural contracts are self-auditable -- the
cross-references within the contracts are sufficient to satisfy C-50 without a
paragraph describing those cross-references.

---

## Final Rubric Summary (v19, 315 pts max)

### Essential — 60 pts (12 pts each)

| ID | Criterion |
|----|-----------|
| C-01 | Multi-voice Role Architecture |
| C-02 | Severity Carries Commit-Gate Semantics |
| C-03 | Null Hypothesis Gate Before Domain Testimony |
| C-04 | Commitment Disposition Emitted |
| C-05 | Action Items Traceable to Findings |

### Recommended — 30 pts (10 pts each)

| ID | Criterion |
|----|-----------|
| C-06 | Artifact Scope Declared Before Review |
| C-07 | Summary with Integrating Narrative |
| C-08 | Depth Parameter Honored |

### Aspirational — 225 pts (5 pts each, C-09 through C-53)

| ID | Criterion |
|----|-----------|
| C-09 | Adversarial Bracket Architecture |
| C-10 | Disposition Algebra Pre-committed |
| C-11 | Override Decision as Labeled Field |
| C-12 | Action Item Class Derived Mechanically |
| C-13 | Prompt Inputs as Template Variables |
| C-14 | Gate Verdict Preserved in Action Register |
| C-15 | Reviewer Set as Injectable Template Parameter |
| C-16 | Alternatives Table as Adversarial Bracket Anchor |
| C-17 | Pre-commitment Cascade: All Three Contracts |
| C-18 | Inline Gate Ledger at Origin |
| C-19 | Gate Ledger Protocol as Pre-committed Fourth Contract |
| C-20 | Verbatim Assembly Prohibition |
| C-21 | Universal Gate Ledger Coverage |
| C-22 | Lifecycle Verdict Integration at Bracket Closing |
| C-23 | Multi-alternative Null Hypothesis Coverage |
| C-24 | Domain-Aggregate Formula Pre-committed |
| C-25 | Non-verdict Section Explicitly Excluded from Gate Ledger |
| C-26 | Canonical Section Order Pre-committed as Immutable Contract |
| C-27 | CH-ID Cross-Section Saturation Pre-committed |
| C-28 | Null Hypothesis Progression Formula Pre-committed |
| C-29 | Scope-to-Finding Coverage Gate Post-Bracket-Closing |
| C-30 | Per-Finding Severity Chain Pre-committed |
| C-31 | Role Lens Exhaustion Pre-committed |
| C-32 | Primary Driver Derivation Pre-committed |
| C-33 | Lens Applicability Rating Pre-committed |
| C-34 | ADVISORY-GAP Domain Coverage Pre-committed |
| C-35 | NH Dimension Table at Bracket Opening |
| C-36 | Scope Surface Domain Annotation Pre-committed |
| C-37 | NH Dimension Table Bracket Closing Re-population |
| C-38 | Multi-Alternative Column Structure in NH Table |
| C-39 | NH Column Aggregation Formula Pre-committed |
| C-40 | Domain Section NH Dimension Score Emission |
| C-41 | Lifecycle Section NH Dimension Score Emission |
| C-42 | Finding Identifier as Formal Named Field |
| C-43 | CH-ID Challenge Grounding Column |
| C-44 | TABLE FORMAT CONTRACT Unified Schema Pre-declaration |
| C-45 | STATUS QUO FRAMING CONTRACT Named §0-CID Registry |
| C-46 | §0-CID Four-Axis Pipeline Threading |
| C-47 | Dual-Path Contract Enforcement |
| C-48 | §0-CID PIPELINE THREADING CONTRACT as Pre-committed Named Preamble Block |
| C-49 | Three-Layer Cross-Reference Consistency |
| C-50 | §0-CID PIPELINE CONTRACT Self-Auditable Axis Back-References |
| C-51 | REVIEWER PRIORITY MANIFEST as Named Non-verdict Sequencing Block |
| C-52 | Lifecycle Phase Sub-Step Sequencing in Section Order Contract |
| C-53 | PIPELINE COMPLIANCE LEDGER as Pre-committed Named Post-Domain Section |

### Score bands

| Band | Threshold |
|------|-----------|
| Gold | >= 275 |
| Max  | 315 |
