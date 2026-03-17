---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 1
rubric: trace-skill-rubric-v11-2026-03-15.md
---

# trace-skill -- Variations R1 (v11 rubric, 2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

## Context

v11 advances the aspirational tier with two new criteria:

- **C-09**: VC-N checks formatted as compliance ledger rows with biconditional invariant-witness
  cells. Expected behavior stated as "X is valid if and only if Y". Observed behavior names
  the invariant hold status and specific evidence locus. Fill-in language ("as expected",
  "compliant") is a FAIL.
- **C-10**: Coverage Matrix satisfies closed-world completeness. Direction (a): no orphan
  entries -- every declared schema is referenced by at least one execution phase. Direction (b):
  no undeclared references -- every schema referenced in any phase appears in the matrix.
  An explicit verification step names both directions with PASS/FAIL and evidence. Orphan
  entries or undeclared references are named trace defects, not silently omitted.

All five R1 v11 variations inherit the full R8 architecture:

- Coverage Matrix with 5 schemas and Role-binding column before Stage 1
- Role-Schema Binding Summary before Stage 2
- Schema 2 gap taxonomy (SA/SG/EG/QO) with SA-to-SG promotion lifecycle
- Enforcement Gate Registry (G-1, G-2, G-3) with hard-stop BLOCKED language
- 4-phase lifecycle (Setup, Execute, Findings, Amend)
- Artifact in `{topic}-{signal}-{date}.md` format
- VC-1 through VC-5 in Verdict

The R1 v11 variations target C-09 and C-10 specifically:

- V-01: Phrasing register (biconditional VC cells) -- targets C-09
- V-02: Lifecycle emphasis (explicit CLOSED-WORLD AUDIT step) -- targets C-10
- V-03: Output format (Coverage Matrix rows as pre-populated invariant contracts) -- targets C-10
- V-04: Combined role sequence (Coverage Auditor role) + lifecycle emphasis (audit gate) -- targets C-09 + C-10
- V-05: Combined phrasing register (interrogative biconditional) + inertia framing -- targets C-09 + C-10

---

## V-01 -- Single axis: Phrasing register (biconditional invariant-witness VC cells)

**Axis**: Phrasing register -- the Verdict section's VC-N checks are reformatted as compliance
ledger rows where the Expected behavior cell is pre-filled as a biconditional invariant ("Schema
N is valid if and only if [precise condition]") and the Observed behavior cell names the invariant
hold status with a specific evidence locus rather than a compliance confirmation.

**Hypothesis**: Pre-filling the Expected cell as a biconditional forces the tracer to state the
schema's validity condition precisely before checking. Fill-in language ("as expected",
"compliant") cannot satisfy the Observed cell's required form because the cell demands
invariant-hold status with evidence. This makes C-09 achievable without structural overhead --
the VC table template enforces the form. Risk: biconditional formulation may be difficult to
write for schemas with multi-condition validity (Schema 5 sub-step ordering), producing
approximations that satisfy the letter but not the spirit.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

Declare all schemas before Stage 1 runs. Every label and taxonomy used in any phase must appear
in this matrix. Phases reference only schemas declared here -- any schema referenced without a
matrix entry is a Coverage Matrix defect flagged in the closed-world check.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles (Source label in relay uses only SA/SG/EG/QO) | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Applies to Phase 4 amendments across all roles | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 checks Source column coverage across all roles' findings in Step 3b | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 sub-step transitions | N/A -- applies to Findings phase structure, not individual roles | VC-5 |

#### Schema 1 -- Severity Vocabulary

| Label | Definition | Blocks? |
|-------|-----------|---------|
| P1 | Must address before artifact is useful -- blocks implementation or invocation | YES |
| P2 | Should address to improve quality | NO |
| P3 | Advisory only -- no immediate action required | NO |

#### Schema 2 -- Gap Type Taxonomy

| Type | Meaning | Promotion rule |
|------|---------|----------------|
| SA | Spec absent -- not declared in spec | Evaluate at SA-TO-SG PROMOTION; promoted gaps relabeled SG downstream |
| SG | Setup gap -- declared; invoker cannot supply at runtime | Carry with SG label through all phases |
| EG | Execute gap -- contract requires it; role structurally cannot produce it | Surface in Execute; carry to Findings |
| QO | Quality observation -- improvable but not structural | Surface anywhere; P3 severity typical |

#### Schema 3 -- Remediation Channel Taxonomy

| Channel | Targets | Activated-at |
|---------|---------|-------------|
| spec | Skill spec or artifact contract | Step 3d |
| invocation | How the skill is invoked | Step 3d |
| artifact | Output document content | Step 3d |
| quality | Quality improvement with no source-layer finding | Step 3d |

#### Schema 4 -- Enforcement Gate Registry

| Gate | Property | Hard-stop condition |
|------|---------|-------------------|
| G-1 | Source diversity: >= 2 distinct Source types in Step 3b | Phase 4 BLOCKED while G-1 = FAIL |
| G-2 | Action diversity: no two same-Source findings share identical Action text | Phase 4 BLOCKED while G-2 = FAIL |
| G-3 | Severity completeness: all Step 3b entries use only P1/P2/P3 | Phase 4 BLOCKED while G-3 = FAIL |

#### Schema 5 -- Sub-Step Ordering

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| 3a | Phase 2 artifact | Findings list with IDs | 3b |
| 3b | 3a complete | Findings + Source column + Severity | 3c |
| 3c | 3b complete | Gate results (G-1/G-2/G-3) with PASS/FAIL | 3d or BLOCKED |
| 3d | 3c PASS | Remediation channel assigned per finding | Phase 4 |

---

### Stage 1 -- Spec Audit

Read `{{skill_spec_path}}` in full before handling the test invocation.

**Source-layer audit**: For every input the skill requires, determine whether the spec declares
it. Each undeclared requirement is a source gap -- label it SA-NN.

**SA-TO-SG PROMOTION**: For each SA gap: can the invoker supply it at runtime from the test
invocation `{{invocation}}`? If YES: relabel SG-NN (promoted) and record the promotion decision.
If NO: retain SA label; carry to Findings as a spec defect.

**Role sequence audit**: List every stock role in the order the spec defines them. For each
role, state the input it receives and the output it produces. If input/output is not defined:
SA-NN. If role order is unspecified: SA-NN.

**Artifact contract audit**: Does the spec define the `{signal}` value for this skill? Does it
define every required artifact section? Flag undefined elements SA-NN.

---

### Stage 2 -- Hand-Compilation

#### Role-Schema Binding Summary

Before any role runs, declare the schema obligations for every role in the execution sequence.
A role without a declared schema obligation is ungoverned.

| Role | Schema 1 binding (severities it may produce) | Schema 2 binding (Source labels it may use; promotion rules) | Additional obligations |
|------|----------------------------------------------|--------------------------------------------------------------|----------------------|
| [list each stock role per spec] | | | |

---

#### Phase 1 -- Setup

Carrying forward from Stage 1: source-layer audit complete, SA-TO-SG promotions recorded.

Confirm and record:

- **TOPIC**: parsed from invocation
- **SCOPE**: what is in; what is explicitly excluded
- **ROLE-SELECTION**: stock roles only / stock + custom (list each)
- **STACK-DETECTION**: detection method and result
- **GAPS**: all SG-NN gaps that cannot be resolved before Execute begins

**Phase gate**: Topic, scope, and role selection must be confirmed before Phase 2. Any item
that cannot be confirmed is flagged SG-NN in Setup. Do not begin Phase 2 until this gate is
explicitly noted as PASSED.

---

#### Phase 2 -- Execute

Carrying forward from Phase 1: TOPIC `{{topic}}`, SCOPE `{{scope}}`, roles `{{roles}}`.

Produce the hand-compiled artifact: `{topic}-{signal}-{date}.md`

Run each role in the order declared in the Role-Schema Binding Summary. For each role:

1. Input received (from invocation, prior role output, or auto-detected context)
2. Schema 2 compliance: which Source label(s) this role used and why
3. Output produced: contribution to the artifact
4. EG-NN: any gap the role structurally cannot resolve

Produce the complete artifact body after the role relay. Every required section must be present.
Sections the role relay cannot populate are marked EG-NN, not left blank.

---

#### Phase 3 -- Findings

**Step 3a -- Declare findings**

Carry forward: artifact from Phase 2, all SA/SG/EG/QO gaps from Stages 1-2.

| ID | Finding | Source | Phase found |
|----|---------|--------|------------|
| F-01 | | SA / SG / EG / QO | |

**Step 3b -- Assign severity and action**

| ID | Finding | Source | Severity | Action required |
|----|---------|--------|----------|----------------|

**Step 3c -- Run Enforcement Gates**

| Gate | Result | Evidence |
|------|--------|---------|
| G-1 (source diversity >= 2 Source types) | PASS / FAIL | [names Source types found] |
| G-2 (no two same-Source findings share identical Action text) | PASS / FAIL | [confirms or names duplicate] |
| G-3 (all severities are P1/P2/P3 only) | PASS / FAIL | [confirms or names violation] |

If any gate FAILs: **Phase 4 BLOCKED: [gate condition]**. Do not proceed to Phase 4.

**Step 3d -- Assign remediation channels** (only if Step 3c passes)

| ID | Finding | Channel | Target |
|----|---------|---------|--------|

---

#### Phase 4 -- Amend

Carrying forward from Step 3d: highest-priority finding is `{{F-NN}}`, channel `{{channel}}`.

Apply one finding to the artifact. State:

1. **Finding ID**: the finding that drove this amendment
2. **Target**: the section or field changed
3. **Change**: before and after (or addition text)

If no amendment is warranted: name the finding evaluated, state why it was dismissed, and
confirm the artifact is accepted as-is with that reasoning on record.

---

### Verdict

For each schema in the Coverage Matrix, one VC-N check formatted as a compliance ledger row.

**Pre-fill the Expected behavior column before running any VC check. Do not fill Observed
behavior until after executing the phase in question. Fill-in language ("as expected",
"compliant") fails the Observed cell -- it must name the invariant hold status and specific
evidence locus.**

| VC | Schema | Expected behavior (biconditional invariant) | Observed behavior (invariant hold status + evidence locus) | Result |
|----|--------|---------------------------------------------|------------------------------------------------------------|--------|
| VC-1 | Schema 1 -- Severity Vocabulary | Schema 1 is valid if and only if every finding in Step 3b carries exactly one of P1, P2, or P3, and no other label appears | Invariant holds: [YES/NO] -- [names labels observed at Step 3b and any role-produced EG entries; names evidence locus] | PASS / FAIL |
| VC-2 | Schema 2 -- Gap Type Taxonomy | Schema 2 is valid if and only if every gap entry carries exactly one Source label from {SA, SG, EG, QO}, SA-to-SG promotions are recorded as named lifecycle events at the SA-TO-SG PROMOTION boundary, and no promoted gap retains its SA label downstream | Invariant holds: [YES/NO] -- [names gaps observed, their labels at each phase, and whether promotion events were recorded; names evidence locus] | PASS / FAIL |
| VC-3 | Schema 3 -- Remediation Channel Taxonomy | Schema 3 is valid if and only if every Phase 4 amendment is drawn from Step 3d's remediation channel table and the channel assigned matches the finding's Source type | Invariant holds: [YES/NO] -- [names the amendment made in Phase 4 and the channel it was drawn from; names evidence locus] | PASS / FAIL |
| VC-4 | Schema 4 -- Enforcement Gate Registry | Schema 4 is valid if and only if G-1, G-2, and G-3 each produce an explicit PASS or FAIL result in Step 3c, and any FAIL produces "Phase 4 BLOCKED" before the Amend section | Invariant holds: [YES/NO] -- [names gate results observed at Step 3c and whether BLOCKED language appeared; names evidence locus] | PASS / FAIL |
| VC-5 | Schema 5 -- Sub-Step Ordering | Schema 5 is valid if and only if Phase 3 sub-steps execute in the order 3a -> 3b -> 3c -> 3d, with each sub-step's prerequisite confirmed complete before its successor begins | Invariant holds: [YES/NO] -- [names sub-steps observed in execution order and confirms each prerequisite; names evidence locus] | PASS / FAIL |

**Overall result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Basis**: One sentence per schema with a failing VC. If all VC checks PASS: one sentence
stating the artifact is acceptable as a golden baseline for `{{skill_name}}`.

**Artifact written to**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-02 -- Single axis: Lifecycle emphasis (explicit CLOSED-WORLD AUDIT step before Amend)

**Axis**: Lifecycle emphasis -- a dedicated CLOSED-WORLD AUDIT step runs between Step 3c/3d
and Phase 4. The step walks both directions of the Coverage Matrix bijection: direction (a)
confirms no orphan entries (every declared schema is referenced by at least one execution phase),
direction (b) confirms no undeclared references (every schema referenced in any phase appears
in the matrix). Any defect found is a named trace defect classified SA/SG/EG/QO, not omitted.
Phase 4 is gated on the CLOSED-WORLD AUDIT result.

**Hypothesis**: Isolating the closed-world check as a named lifecycle step -- not embedded in
the Verdict -- makes C-10 a first-class execution deliverable that is auditable independently.
Running the audit before Phase 4 means any Coverage Matrix defect surfaces before the amendment
decision, creating the possibility that the amendment addresses the matrix defect itself. Risk:
Adding a named audit step between Findings and Amend breaks the clean 4-phase boundary
(C-01). Mitigation: label the audit as "Step 3e" inside Phase 3, preserving the 4-phase
structure while adding sub-step granularity.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

Declare all schemas here before Stage 1. All phases reference only schemas declared in this
matrix. Any schema referenced without a matrix entry is a closed-world violation discovered
at Step 3e.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles (Source label in relay) | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments across all roles | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 checks Source coverage across all roles in Step 3b | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d -> 3e | Here, before Stage 1 | Phase 3 sub-step transitions | N/A | VC-5 |

*(Schema sub-tables identical to V-01 above; omitted for brevity in this variation.)*

---

### Stage 1 -- Spec Audit

Read `{{skill_spec_path}}`. Run the source-layer audit and SA-TO-SG PROMOTION as in V-01.
Record all SA-NN and SG-NN gaps before Stage 2 begins.

---

### Stage 2 -- Hand-Compilation

#### Role-Schema Binding Summary

Before any role runs, declare schema obligations per role (table format as in V-01).

---

#### Phase 1 -- Setup

Confirm TOPIC, SCOPE, ROLE-SELECTION, STACK-DETECTION. Flag SG-NN for any unresolvable input.
Phase gate: all three confirmed or flagged before Phase 2 begins.

---

#### Phase 2 -- Execute

Carry forward from Phase 1. Run each role in the declared sequence. Produce the artifact:
`{topic}-{signal}-{date}.md`. Record EG-NN for any gap the role structurally cannot resolve.

---

#### Phase 3 -- Findings

**Step 3a**: Declare all findings (ID, finding, source, phase found).

**Step 3b**: Add severity and action direction to each finding.

**Step 3c**: Run Enforcement Gates G-1, G-2, G-3. Record PASS/FAIL for each.

If any gate FAILs: **Phase 4 BLOCKED: [gate condition]**. Step 3e still runs.

**Step 3d**: Assign remediation channels (only if Step 3c passes).

---

**Step 3e -- CLOSED-WORLD AUDIT**

This step verifies the Coverage Matrix satisfies the closed-world completeness invariant.
Run both directions. Record defects as named trace defects (SA/SG/EG as appropriate).

**Direction (a) -- No orphan entries: every declared schema is referenced by at least one phase**

| Schema (from Coverage Matrix) | Referenced-by (from matrix "Referenced-by" column) | Confirmed referenced? | Defect if NO |
|-------------------------------|---------------------------------------------------|----------------------|-------------|
| Schema 1 -- Severity Vocabulary | Step 3a, Step 3b, Step 3c G-3, Phase 4 Amend | [YES/NO -- name phase where reference was observed] | |
| Schema 2 -- Gap Type Taxonomy | Stage 1, SA-TO-SG PROMOTION, Step 3b, Execute relay | [YES/NO] | |
| Schema 3 -- Remediation Channel Taxonomy | Step 3d, Phase 4 Amend | [YES/NO] | |
| Schema 4 -- Enforcement Gate Registry | Step 3c, Phase 4 pre-check | [YES/NO] | |
| Schema 5 -- Sub-Step Ordering | Phase 3 sub-step transitions | [YES/NO] | |

**Direction (b) -- No undeclared references: every schema referenced in any phase appears in the matrix**

Walk each phase in execution order. For each schema vocabulary or taxonomy used, confirm it
appears as a row in the Coverage Matrix above.

| Phase / Step | Schema vocabularies referenced | Appears in Coverage Matrix? | Defect if NO |
|-------------|-------------------------------|----------------------------|-------------|
| Stage 1 audit | SA label | [YES/NO] | |
| SA-TO-SG PROMOTION | SA, SG labels | [YES/NO] | |
| Phase 1 Setup | SG label | [YES/NO] | |
| Phase 2 Execute role relay | SA/SG/EG/QO Source labels, EG label | [YES/NO] | |
| Step 3a | Finding IDs (schema-free) | -- | |
| Step 3b | SA/SG/EG/QO Source, P1/P2/P3 Severity | [YES/NO] | |
| Step 3c | G-1, G-2, G-3 labels | [YES/NO] | |
| Step 3d | spec/invocation/artifact/quality channels | [YES/NO] | |
| Phase 4 Amend | P1/P2/P3 (severity reference), channel reference | [YES/NO] | |

**Closed-world result**: PASS (both directions clear) / FAIL (name defects found)

If FAIL: classify each defect (orphan entry = Coverage Matrix overclaims; undeclared reference
= Coverage Matrix underclaims) and add to Step 3b findings. Phase 4 BLOCKED if closed-world
FAIL produces any P1 finding.

---

#### Phase 4 -- Amend

Carrying forward from Step 3d and Step 3e. Apply the highest-priority finding to the artifact.
Record finding ID, target, and change (before/after or addition).

---

### Verdict

VC-N checks for each schema (one per row). Record result as PASS/FAIL with specific evidence.
Use evidence format: "[invariant description] -- observed at [phase/step reference]".

| VC | Schema | Property verified | Usage site | Result |
|----|--------|-----------------|-----------|--------|
| VC-1 | Schema 1 | Severity labels P1/P2/P3 only in Step 3b and Phase 4 | Step 3b, Phase 4 Amend | PASS/FAIL |
| VC-2 | Schema 2 | Source labels SA/SG/EG/QO only; promotion lifecycle recorded | Stage 1, SA-TO-SG PROMOTION, Step 3b, Execute relay | PASS/FAIL |
| VC-3 | Schema 3 | Remediation channel assigned in Step 3d; Phase 4 amendment draws from Step 3d | Step 3d, Phase 4 | PASS/FAIL |
| VC-4 | Schema 4 | G-1/G-2/G-3 each explicit; FAIL produces BLOCKED language | Step 3c, Phase 4 pre-check | PASS/FAIL |
| VC-5 | Schema 5 | Sub-steps execute 3a -> 3b -> 3c -> 3d -> 3e in order | Phase 3 sub-step sequence | PASS/FAIL |

**Overall result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact written to**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-03 -- Single axis: Output format (Coverage Matrix rows as pre-populated invariant contracts)

**Axis**: Output format -- the Coverage Matrix is reformatted as a compliance contract. Each
schema row is expanded with two additional columns: an Expected column pre-populated with the
closed-world invariant for that schema ("this schema is in the matrix if and only if [condition]"),
and an Observed column left blank until execution completes. After Phase 2, return to the
Coverage Matrix and fill in the Observed column for each row. The matrix then serves as
both the schema registry AND the closed-world verification record.

**Hypothesis**: Pre-populating the Coverage Matrix with Expected invariants (before Stage 1
runs) commits the tracer to a specific validity condition for each schema's presence in the
matrix. Returning to the matrix after Phase 2 to fill in the Observed column makes the
closed-world check continuous (interleaved with execution) rather than a separate end-of-trace
step. The matrix is auditable at any point because Expected and Observed are always paired.
Risk: expanding the Coverage Matrix to 8 columns may produce a table too wide to reason about
clearly; the additional column overhead may obscure the schema content itself.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix + Closed-World Contract)

This matrix is the schema registry AND the closed-world completeness contract for this trace.
Pre-fill the Expected column now. Leave the Observed column blank -- return to fill it after
Phase 2 completes. After filling Observed, run the Direction-check column.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check | Expected invariant (pre-fill now) | Observed (fill after Phase 2) | Direction-check |
|--------|---------|-------------|---------------|--------------|---------------|----------------------------------|-------------------------------|----------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b, Step 3c G-3, Phase 4 Amend | All roles producing EG findings | VC-1 | Schema 1 is present IFF findings in Step 3b carry exactly one label from {P1, P2, P3} AND Phase 4 applies severity before amending | [holds / does not hold: name evidence] | (a) declared -- referenced at Step 3b? [YES/NO] / (b) Step 3b usage -- in matrix? [YES/NO] |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Step 3b, Execute relay | All roles (Source label in relay) | VC-2 | Schema 2 is present IFF every gap entry carries exactly one Source label from {SA, SG, EG, QO} AND SA-to-SG promotions are recorded as named lifecycle events | [holds / does not hold: name evidence] | (a) declared -- referenced at Stage 1? [YES/NO] / (b) Stage 1 SA label usage -- in matrix? [YES/NO] |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d, Phase 4 Amend | Phase 4 amendments across all roles | VC-3 | Schema 3 is present IFF every Phase 4 amendment is drawn from a Step 3d channel assignment AND the channel matches the finding's Source type | [holds / does not hold: name evidence] | (a) declared -- referenced at Step 3d? [YES/NO] / (b) Step 3d channel usage -- in matrix? [YES/NO] |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1 checks Source coverage across all roles in Step 3b | VC-4 | Schema 4 is present IFF G-1, G-2, and G-3 each produce an explicit PASS or FAIL in Step 3c AND any FAIL produces BLOCKED language before Phase 4 | [holds / does not hold: name evidence] | (a) declared -- referenced at Step 3c? [YES/NO] / (b) Step 3c G-1/G-2/G-3 usage -- in matrix? [YES/NO] |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 sub-step transitions | N/A | VC-5 | Schema 5 is present IFF Phase 3 sub-steps execute in exactly the order 3a -> 3b -> 3c -> 3d with each sub-step's prerequisite confirmed before its successor begins | [holds / does not hold: name evidence] | (a) declared -- referenced at Phase 3 transitions? [YES/NO] / (b) Phase 3 transition labels -- in matrix? [YES/NO] |

After filling in the Observed and Direction-check columns, scan for any row where:
- Direction-check (a) = NO: this is an orphan entry -- the schema is declared but never
  referenced. Add to Step 3b findings, Source = SA, Severity = P2.
- Direction-check (b) = NO: this is an undeclared reference -- a schema is referenced without
  a matrix entry. Add to Step 3b findings, Source = SA, Severity = P1.

*(Schema sub-tables for individual schemas identical to V-01; omitted for brevity.)*

---

### Stage 1 -- Spec Audit

Read `{{skill_spec_path}}`. Run source-layer audit. Record SA-NN gaps. Run SA-TO-SG PROMOTION.

---

### Stage 2 -- Hand-Compilation

#### Role-Schema Binding Summary

Declare schema obligations per role before Stage 2 begins (table format as in V-01).

#### Phase 1 -- Setup

Confirm TOPIC, SCOPE, ROLE-SELECTION, STACK-DETECTION. Flag SG-NN for any unresolvable input.
Phase gate: all confirmed or flagged before Phase 2.

#### Phase 2 -- Execute

Carry forward from Phase 1. Run each role in the declared sequence. Produce the artifact:
`{topic}-{signal}-{date}.md`. Record EG-NN for structural gaps.

**After Phase 2**: Return to the Coverage Matrix above. Fill in the Observed column for each
schema row. Fill in the Direction-check column. Add any defects found to Step 3b.

#### Phase 3 -- Findings

Step 3a: Declare findings. Step 3b: Add severity and action (include any Coverage Matrix
defects from the Direction-check column). Step 3c: Run G-1, G-2, G-3.

If any gate FAILs: **Phase 4 BLOCKED: [gate condition]**

Step 3d: Assign remediation channels.

#### Phase 4 -- Amend

Apply the highest-priority finding to the artifact. Record finding ID, target, change.

---

### Verdict

VC-N checks drawn from the Coverage Matrix's Verdict-check column. One row per schema.

| VC | Schema | Property verified | Usage site | Result |
|----|--------|-----------------|-----------|--------|
| VC-1 | Schema 1 | [from Expected invariant in Coverage Matrix: severity completeness] | Step 3b, Phase 4 | PASS/FAIL: [Observed from Coverage Matrix row] |
| VC-2 | Schema 2 | [from Expected invariant in Coverage Matrix: Source label completeness + promotion lifecycle] | Stage 1, SA-TO-SG PROMOTION, Step 3b, Execute relay | PASS/FAIL: [Observed from Coverage Matrix row] |
| VC-3 | Schema 3 | [from Expected invariant in Coverage Matrix: channel assignment and match] | Step 3d, Phase 4 | PASS/FAIL: [Observed from Coverage Matrix row] |
| VC-4 | Schema 4 | [from Expected invariant in Coverage Matrix: gate completeness + BLOCKED enforcement] | Step 3c, Phase 4 pre-check | PASS/FAIL: [Observed from Coverage Matrix row] |
| VC-5 | Schema 5 | [from Expected invariant in Coverage Matrix: sub-step ordering] | Phase 3 sub-step sequence | PASS/FAIL: [Observed from Coverage Matrix row] |

**Overall result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact written to**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-04 -- Combined axes: Role sequence (Coverage Auditor role) + lifecycle emphasis (audit gate before Amend)

**Axes**:
- Role sequence: a dedicated Coverage Auditor role is added at Stage 3 (after Execute,
  before Findings consolidation). The Coverage Auditor's sole job is to perform the
  closed-world bijection check and produce a coverage audit certificate.
- Lifecycle emphasis: Phase 4 has an explicit audit gate -- if the Coverage Auditor's
  certificate shows a closed-world FAIL, Phase 4 is BLOCKED alongside any enforcement
  gate failure. The audit certificate is a first-class artifact appendix.

**Hypothesis**: Separating the closed-world check into a named role (not just a Verdict section)
makes it a first-class execution step that can be audited, upgraded, or replaced independently.
The Coverage Auditor running at Stage 3 means defects surface before Findings are consolidated,
so a coverage defect can become a finding with a remediation channel -- not just a Verdict
observation. Combining with the audit gate before Phase 4 creates two enforcement mechanisms
for C-10: the Coverage Auditor role (produces the evidence) and the gate (enforces the result).
Risk: Stage 3 overlap with Phase 3 sub-steps may blur the lifecycle boundary (C-01). Mitigation:
Coverage Auditor runs between Phase 2 and Phase 3 (not inside Phase 3), preserving the
four-phase structure.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

Declare all schemas before Stage 1 runs. The Coverage Auditor at Stage 3 will verify this
matrix against the execution using the closed-world completeness invariant.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b, Step 3c G-3, Phase 4 Amend | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Step 3b, Execute relay | All roles (Source label in relay) | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d, Phase 4 Amend | Phase 4 amendments | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1 checks Source coverage in Step 3b | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 sub-step transitions | N/A | VC-5 |

*(Schema sub-tables identical to V-01.)*

---

### Stage 1 -- Spec Audit

Read `{{skill_spec_path}}`. Run source-layer audit. Record SA-NN gaps. Run SA-TO-SG PROMOTION.

---

### Stage 2 -- Hand-Compilation

#### Role-Schema Binding Summary

The Coverage Auditor is a Stage 3 role, not a hand-compilation role. List only the execution
roles here. The Coverage Auditor's schema obligations are declared separately below.

| Role | Schema 1 binding | Schema 2 binding | Additional obligations |
|------|-----------------|-----------------|----------------------|
| [stock roles per spec] | | | |

**Coverage Auditor role obligations**: Schema 1 (none -- does not produce severity labels),
Schema 2 (none -- reads but does not produce gap labels), Coverage Matrix (primary obligation:
closed-world bijection check per the matrix declared above).

#### Phase 1 -- Setup

Confirm TOPIC, SCOPE, ROLE-SELECTION, STACK-DETECTION. Flag SG-NN for unresolvable inputs.

#### Phase 2 -- Execute

Carry forward confirmed inputs. Run each stock role in declared sequence. Produce the artifact:
`{topic}-{signal}-{date}.md`. Record EG-NN for structural gaps.

---

### Stage 3 -- Coverage Auditor

The Coverage Auditor runs after Phase 2 and before Phase 3. Its output is the Coverage Audit
Certificate. The certificate has two sections, one per direction of the closed-world check.

**Coverage Audit Certificate**

**Direction (a) -- No orphan entries**

Walk the Coverage Matrix. For each schema row, name the phase(s) that referenced it during
Stage 2 execution.

| Schema | Referenced-by (from matrix) | Observed reference in Stage 2 | Orphan? |
|--------|---------------------------|------------------------------|---------|
| Schema 1 -- Severity Vocabulary | Step 3a, Step 3b, Step 3c G-3, Phase 4 Amend | [name phase where severity label was used] | YES / NO |
| Schema 2 -- Gap Type Taxonomy | Stage 1, SA-TO-SG PROMOTION, Step 3b, Execute relay | [name phase where Source label was used] | YES / NO |
| Schema 3 -- Remediation Channel Taxonomy | Step 3d, Phase 4 Amend | [name phase where channel was assigned] | YES / NO |
| Schema 4 -- Enforcement Gate Registry | Step 3c, Phase 4 pre-check | [name phase where gate ran] | YES / NO |
| Schema 5 -- Sub-Step Ordering | Phase 3 transitions | [name phase where sub-step order was enforced] | YES / NO |

**Direction (b) -- No undeclared references**

Walk each phase in Stage 2 execution. For each schema vocabulary used, confirm it appears
in the Coverage Matrix.

| Phase / Step | Schema vocabulary used | In Coverage Matrix? | Undeclared? |
|-------------|----------------------|--------------------|-----------:|
| Stage 1 | SA label | YES (Schema 2) | NO |
| SA-TO-SG PROMOTION | SA→SG promotion | YES (Schema 2, promotion rule) | NO |
| Phase 1 Setup | SG label | YES (Schema 2) | NO |
| Execute role relay | SA/SG/EG/QO; EG label | YES (Schema 2) | NO |
| Step 3b | Source labels, P1/P2/P3 | YES (Schema 2, Schema 1) | NO |
| Step 3c | G-1, G-2, G-3 | YES (Schema 4) | NO |
| Step 3d | spec/invocation/artifact/quality | YES (Schema 3) | NO |
| Phase 4 Amend | Severity reference, channel | YES (Schema 1, Schema 3) | NO |

**Certificate result**:

- Direction (a): PASS (no orphans) / FAIL (list orphan schemas)
- Direction (b): PASS (no undeclared references) / FAIL (list undeclared vocabularies)
- **Overall**: PASS / FAIL

If FAIL: carry each defect to Step 3b as a finding with Source = SA, Severity = P1 (undeclared
reference) or P2 (orphan entry).

---

### Phase 3 -- Findings

**Step 3a**: Declare findings from Stage 1, Stage 2, and Stage 3 (Coverage Auditor defects).

**Step 3b**: Add severity and action direction. Include any Coverage Auditor defects.

**Step 3c**: Run Enforcement Gates G-1, G-2, G-3.

If any gate FAILs: **Phase 4 BLOCKED: [gate condition]**

**Coverage audit gate**: If Coverage Auditor Certificate result = FAIL and any audit defect
is P1: **Phase 4 BLOCKED: Coverage Matrix closed-world check failed -- [name defect]**

**Step 3d**: Assign remediation channels (only if all gates and audit gate pass).

---

### Phase 4 -- Amend

Apply the highest-priority finding to the artifact. Record finding ID, target, and change.

---

### Verdict

VC-N checks per schema, one row each. Reference the Coverage Audit Certificate for VC evidence.

| VC | Schema | Property | Usage site | Result |
|----|--------|---------|-----------|--------|
| VC-1 | Schema 1 -- Severity Vocabulary | Severity labels P1/P2/P3 only in Step 3b and Phase 4 | Step 3b, Phase 4 | PASS/FAIL + evidence |
| VC-2 | Schema 2 -- Gap Type Taxonomy | Source labels SA/SG/EG/QO only; promotion lifecycle recorded | Stage 1, SA-TO-SG PROMOTION, Step 3b, Execute relay | PASS/FAIL + evidence |
| VC-3 | Schema 3 -- Remediation Channel Taxonomy | Channel assigned in Step 3d; Phase 4 draws from it | Step 3d, Phase 4 | PASS/FAIL + evidence |
| VC-4 | Schema 4 -- Enforcement Gate Registry | G-1/G-2/G-3 each explicit; FAIL produces BLOCKED | Step 3c, Phase 4 pre-check | PASS/FAIL + evidence |
| VC-5 | Schema 5 -- Sub-Step Ordering | Sub-steps 3a->3b->3c->3d in order | Phase 3 sub-step sequence | PASS/FAIL + evidence |
| VC-CW | Coverage Audit Certificate | Both directions clear (no orphans, no undeclared refs) | Stage 3 Certificate | PASS/FAIL + certificate result |

**Overall result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact written to**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-05 -- Combined axes: Phrasing register (interrogative biconditional) + inertia framing

**Axes**:
- Phrasing register: VC check headers are interrogative biconditionals -- "Does Schema N
  hold if and only if [condition]?" -- pre-loaded as questions before execution begins.
  The Observed cell answers "YES, invariant holds: [evidence]" or "NO, invariant fails:
  [evidence]". The question pre-loads the expected answer form, activating biconditional
  reasoning without requiring the tracer to construct the invariant from scratch.
- Inertia framing: The Verdict opens with a status-quo contrast. Without this skill, a
  developer validating `{{skill_name}}` before implementing it must audit coverage manually
  per run and trust narrative claims about schema compliance. With this skill, the Coverage
  Matrix is its own audit surface -- closed-world verification is a trace artifact, not a
  claim. The Verdict's USEFUL/NEEDS-REDESIGN/NEEDS-SPEC-REVISION result is framed as a
  build-vs-defer-vs-redesign decision.

**Hypothesis**: Interrogative form activates the biconditional without requiring the model to
construct the invariant -- the question commits the tracer to a specific hold/fail binary
before checking evidence. Inertia framing elevates the Verdict from a scoring result to a
decision recommendation that makes the trace's purpose concrete. Combined, the two axes
produce a trace that is self-justifying: the Verdict explains why the hand-compiled artifact
has value (or why it doesn't) in terms a developer would recognize. Risk: interrogative headers
may feel inconsistent with the imperative phase structure (C-01). Mitigation: phase headers
remain imperative ("Phase 1 -- Setup"), while VC headers alone use interrogative form.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

Declare all schemas here. For each schema, pre-load the Verdict question now -- the biconditional
question you will answer in the Verdict after all phases complete. Do not answer the question
yet. A question left unanswered in the Verdict is a FAIL.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check | Verdict question (pre-load now; answer in VC row) |
|--------|---------|-------------|---------------|--------------|---------------|--------------------------------------------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b, Step 3c G-3, Phase 4 Amend | All roles producing EG findings | VC-1 | Does Schema 1 hold if and only if every finding carries exactly one of P1/P2/P3 AND no other severity label appears in Step 3b or Phase 4? |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Step 3b, Execute relay | All roles (Source label in relay) | VC-2 | Does Schema 2 hold if and only if every gap entry carries exactly one Source label from {SA, SG, EG, QO} AND every SA-to-SG promotion is recorded as a named lifecycle event at the SA-TO-SG PROMOTION boundary? |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d, Phase 4 Amend | Phase 4 amendments | VC-3 | Does Schema 3 hold if and only if every Phase 4 amendment is drawn from a Step 3d channel entry AND the channel value matches the finding's Source type? |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1 checks Source coverage in Step 3b | VC-4 | Does Schema 4 hold if and only if G-1, G-2, and G-3 each produce an explicit PASS/FAIL in Step 3c AND any FAIL is followed immediately by "Phase 4 BLOCKED" language? |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 sub-step transitions | N/A | VC-5 | Does Schema 5 hold if and only if Phase 3 sub-steps execute in exactly the order 3a -> 3b -> 3c -> 3d with each predecessor confirmed complete before its successor begins? |

*(Schema sub-tables identical to V-01.)*

---

### Stage 1 -- Spec Audit

Read `{{skill_spec_path}}`. Run source-layer audit and SA-TO-SG PROMOTION. Record all SA-NN
and SG-NN gaps before Stage 2 begins.

---

### Stage 2 -- Hand-Compilation

#### Role-Schema Binding Summary

Declare schema obligations per role before any role runs.

| Role | Schema 1 binding | Schema 2 binding | Additional |
|------|-----------------|-----------------|-----------|
| [each stock role from spec] | | | |

---

#### Phase 1 -- Setup

Confirm TOPIC, SCOPE, ROLE-SELECTION, STACK-DETECTION. Flag SG-NN for unresolvable inputs.
Phase gate: all confirmed or flagged before Phase 2.

#### Phase 2 -- Execute

Carry forward from Phase 1. Run each role. Produce the artifact: `{topic}-{signal}-{date}.md`.
Record EG-NN for gaps the role structurally cannot resolve.

#### Phase 3 -- Findings

Step 3a: Declare findings. Step 3b: Add severity and action direction. Step 3c: Run G-1/G-2/G-3.

If any gate FAILs: **Phase 4 BLOCKED: [gate condition]**

Step 3d: Assign remediation channels.

**Closed-world check**: Walk both directions before Phase 4.

Direction (a): For each Coverage Matrix row, name the phase where it was referenced. Any schema
declared but never referenced: orphan entry -- add to findings (P2, Source = SA).

Direction (b): For each schema vocabulary used in any phase, confirm it appears in the Coverage
Matrix. Any schema used without a matrix row: undeclared reference -- add to findings
(P1, Source = SA).

If any undeclared reference found: **Phase 4 BLOCKED: undeclared schema reference -- [name it]**

#### Phase 4 -- Amend

Apply the highest-priority finding. Record finding ID, target, and change.

---

### Verdict

For each schema in the Coverage Matrix, answer the pre-loaded biconditional question.
The answer must name the invariant hold status and specific evidence locus -- "YES" or "NO"
alone does not pass. "As expected" or "compliant" does not pass.

| VC | Schema | Question (from Coverage Matrix "Verdict question" column) | Answer (invariant hold status + specific evidence locus) | Result |
|----|--------|----------------------------------------------------------|----------------------------------------------------------|--------|
| VC-1 | Schema 1 | Does Schema 1 hold IFF every finding carries exactly one of P1/P2/P3 AND no other label appears? | [YES, invariant holds / NO, invariant fails]: [names specific labels observed at Step 3b, names any anomaly; locus = Step 3b row IDs] | PASS / FAIL |
| VC-2 | Schema 2 | Does Schema 2 hold IFF every gap entry carries exactly one Source label AND SA-to-SG promotions are recorded as named lifecycle events? | [YES/NO]: [names Source labels observed at Stage 1, SA-TO-SG PROMOTION, Step 3b; confirms or names missing promotion event; locus] | PASS / FAIL |
| VC-3 | Schema 3 | Does Schema 3 hold IFF every Phase 4 amendment is drawn from Step 3d AND channel matches Source type? | [YES/NO]: [names the amendment, the Step 3d entry it was drawn from, and whether channel matched; locus = Phase 4 amendment record] | PASS / FAIL |
| VC-4 | Schema 4 | Does Schema 4 hold IFF G-1/G-2/G-3 each produce explicit PASS/FAIL AND any FAIL is followed by BLOCKED language? | [YES/NO]: [names gate results at Step 3c; confirms or denies BLOCKED language appearance; locus = Step 3c] | PASS / FAIL |
| VC-5 | Schema 5 | Does Schema 5 hold IFF sub-steps execute 3a->3b->3c->3d in order with each predecessor confirmed? | [YES/NO]: [names sub-step execution sequence observed; confirms or denies each prerequisite check; locus = Phase 3] | PASS / FAIL |

**Without this skill**: A developer validating `{{skill_name}}` before implementing it must read
the spec, mentally simulate each phase, guess at role outputs, and audit schema coverage manually
per run -- trusting narrative claims rather than a verifiable matrix.

**With this skill**: The Coverage Matrix is its own audit surface. The closed-world check
produces a certificate, not a claim. Schema compliance is biconditionally verifiable at each
VC row without running the skill again.

**Decision**:
- `USEFUL` -- implement now; the hand-compiled artifact is an acceptable golden baseline
- `NEEDS-SPEC-REVISION` -- one or more SA gaps block implementation; spec must be updated first
- `NEEDS-REDESIGN` -- structural gaps in the skill's architecture prevent a viable hand-compilation

**Overall result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact written to**: `simulations/trace/skill/{topic}-{signal}-{date}.md`
