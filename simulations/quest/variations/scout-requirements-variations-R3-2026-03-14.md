Here are the 5 complete R3 variations for `scout-requirements`:

---

## Variation Set R3 — scout-requirements

All 5 variations embed the full C-25/C-26/C-27 charter block from V-05 R2. The axes explored are new territory not covered in R2.

| Var | Axis | Predicted | Risk |
|-----|------|-----------|------|
| **V-01** | Role sequence: Compliance-first | 128/128 | Medium — 9 steps vs 6; late drift risk before MoSCoW synthesis |
| **V-02** | Output format: unified requirement table with Law-Ref column | 128/128 | Medium — table compression may weaken inline [AMBIG:] prose evidence |
| **V-03** | Phrasing register: conversational imperative | **126/128** | HIGH — terse instructions reduce structural repetition; C-26's exact sub-ID phrasing may degrade |
| **V-04** | Compliance-first + definitional register | 128/128 | Low — definitional language amplifies C-27 naturally; compliance-first adds structure |
| **V-05** | Table format + inertia framing | 128/128 | Low — "Without this step..." anchors reinforce C-27's definitional framing at every section |

**The three key patterns guaranteed in all 5 variations:**

- **C-25**: Design contract names per-law artifact: `C-18-A` creates `[AMBIG:]` notations; `C-18-B` creates closure sentences; `C-19-A/B` audit specifically per artifact type
- **C-26**: Structural closure names `"C-18 (both Law A's C-18-A and Law B's C-18-B)"` by sub-ID
- **C-27**: Structural closure includes `"declaring format laws without an application layer is not enforcement — it is an incomplete declaration"`

**Key discriminator between R3 variations and R2 V-05**: R3 variations test whether the C-25/C-26/C-27 patterns survive structural changes to role ordering (V-01, V-04), output format (V-02, V-05), and instruction verbosity (V-03). R2 V-05 established the patterns in a fixed structure; R3 asks whether they are portable.

**V-03 is the intended failure probe** — the only axis predicted to drop below 128/128. If V-03 actually scores 128/128, it means C-26's pass condition is less sensitive to exact phrasing than the rubric implies. If it scores 124/128, it confirms that structural repetition in the charter (not just the clause itself) is what makes C-26 reliable.
eclare requirements against the compliance grid. The charter
enforcement machinery is unchanged; only role order varies.

---

```
You are running /scout-requirements for: {{topic}}

---

## CHARTER — FORMAT LAWS AND THREE-LOOP META-REQUIREMENT

This charter is C-17 (Loop 1 / declare) of the three-loop meta-requirement. It declares two
format laws and their per-law enforcement chains before any extraction begins.

### Format Law A: Two-Path AF- Rule

Every ambiguity encountered during extraction carries an inline notation at first encounter:

  [AMBIG: "{exact source text}" → A: {interpretation A} | B: {interpretation B}]

This rule applies AT FIRST ENCOUNTER during extraction steps — not deferred to the AF- section.
The AF- section formalizes inline notations already created; it does not produce new ambiguity
work for the first time.

### Format Law B: Downstream Closure Rule

Each downstream findings section (AF-, SF-) contains the following explicit closure statement:

  "Every entry from the prior open [AF- / SF-] register appears in this section
   with a status: open / resolved / out-of-scope."

A section that carries prior findings forward without this statement fails Law B.

### Law A Independent Enforcement Chain

- **C-17-A (Loop 1-A / declare)**: Law A declared here, independently of Law B.
  A failure in Law A's apply chain cannot cascade to Law B's enforcement.
- **C-18-A (Loop 2-A / apply)**: Each extraction step that encounters an ambiguity contains
  a full-text reinstatement — "Apply Law A here" — followed immediately by both interpretation
  paths written inline before the AF- entry is logged.
- **C-19-A (Loop 3-A / verify)**: The pre-output verification table includes a row auditing
  whether dual-interpretation [AMBIG:] notations appeared at each applicable extraction step —
  not merely whether the AF- summary section exists.

### Law B Independent Enforcement Chain

- **C-17-B (Loop 1-B / declare)**: Law B declared here, independently of Law A.
  A failure in Law B's apply chain cannot cascade to Law A's enforcement.
- **C-18-B (Loop 2-B / apply)**: Each extraction step that identifies a downstream section
  contains a full-text reinstatement — "Apply Law B here" — followed immediately by the
  closure sentence written inline.
- **C-19-B (Loop 3-B / verify)**: The pre-output verification table includes a row auditing
  whether closure sentences appeared in each downstream section — not merely whether sections
  are present.

### Three-Loop Meta-Requirement: Structural Closure

The two law chains unify under one self-closing declaration:

- **C-17 (Loop 1 / declare)** = this charter, including both Law A and Law B independent chains
- **C-18 (Loop 2 / apply)** = the step-level cross-references from both chains, applied per law
- **C-19 (Loop 3 / verify)** = the pre-output verification protocol table

**Structural Closure**: Declaring format laws without an application layer is not enforcement —
it is an incomplete declaration. A charter that declares Law A and Law B (C-17) without requiring
inline reinstatement at each triggering step (C-18) has not created enforcement; the category
"enforcement" requires Loop 2 by definition. Without Loop 2, what exists is a statement of intent,
not enforcement. Asserting C-17 simultaneously instantiates C-18 (both Law A's C-18-A and Law B's
C-18-B) as necessary consequences: the act of declaring laws constitutes the obligation to apply
them at each triggering step. C-19 closes the loop by auditing that C-18's applications occurred.

### Loop 2 → Loop 3 Design Contract

This charter names the following as a structural obligation before extraction begins, chartered
here as a design contract and not inferred from structural proximity:

**C-18 (Loop 2) creates the execution artifacts that C-19 (Loop 3) requires as evidence.**

Specifically, per law:
- **Law A's C-18-A** creates inline [AMBIG:] notations at each ambiguity step, each carrying
  Interpretation A and Interpretation B. C-19-A audits specifically whether these dual-path
  notations are present and complete at each applicable step — not whether the AF- section exists.
- **Law B's C-18-B** creates inline closure sentences in each downstream findings section.
  C-19-B audits specifically whether closure sentences are present and correctly formed at
  each applicable section — not whether prior entries are listed anywhere.

C-18 prevents violations at extraction time. C-19 detects violations that slipped through.
If C-18 is skipped, C-19 has no artifacts to audit — verification without C-18 is structural
theater. C-18's artifacts are C-19's evidence: they are complementary prevention-detection
layers, not alternatives.

---

## STEP 0: DUAL-DIRECTORY SEARCH

Search for prior scout signals in BOTH:
- simulations/scout/ — real runs for {{topic}}
- simulations/trace/skill/ — hand-compiled traces for {{topic}}

State what you found in each directory. If either is empty or has no relevant files, say so
explicitly. Never silently skip either directory.

**Apply Law B here (Step 0)**: List all open AF- and SF- entries from prior runs.
State the closure sentence:
  "Every entry from the prior open findings register appears in this step with a status:
   open / resolved / out-of-scope."

SF-01 (undefined search path): CLOSED if trace found in simulations/trace/skill/; else OPEN.

---

## STEP 1: COMPLIANCE LENS (runs first)

**Apply Law A here (Step 1)**: Flag ambiguities inline at first encounter using the two-path
format [AMBIG:] before assigning an AF- ID. Do not defer.

Compliance runs first to establish the non-negotiable requirement skeleton. Every subsequent
role builds within this grid. Extract:

- Legal or regulatory mandates → automatic MoSCoW Must (note the specific regulation/policy)
- Conditional compliance obligations (apply in certain jurisdictions/user types) → Should/Could
- Audit, reporting, and data-retention requirements implied by the concept
- Compliance silences: areas where the concept implies regulatory obligations without naming them

**Apply Law B here (Step 1)**: Each compliance silence found is a candidate SS- entry.
Write the closure sentence inline before logging: "Phase [X] has no compliance requirement —
Risk: [consequence]."

Assign IDs: C-NN (compliance). Flag blockers: "BLOCKS: [list of requirement IDs blocked]."

---

## STEP 2: PM LENS (constrained by Step 1)

**Apply Law A here (Step 2)**: Flag ambiguities inline at first encounter using [AMBIG:] format.

PM requirements are generated against the compliance skeleton from Step 1. Where a PM
requirement conflicts with a compliance mandate, the compliance mandate wins (Must stays Must).

Extract:
- User goals this concept must achieve → Must Have (if compliance-anchored) or Should Have
- Competitive capabilities → Should Have
- Delight features → Could Have
- Out-of-scope user needs → Won't Have

Flag any PM silence where a user scenario has no requirement coverage.
**Apply Law B here (Step 2)**: Write closure sentence inline for each gap found.

Assign IDs: P-NN (PM). Flag blockers.

---

## STEP 3: ARCHITECT LENS (constrained by Steps 1-2)

**Apply Law A here (Step 3)**: Flag ambiguities inline at first encounter.

Architect requirements are generated against the compliance + PM baseline. Compliance-derived
technical constraints inherit Must priority from Step 1.

Extract:
- System properties required to satisfy compliance mandates → Must Have (inherit compliance tier)
- System properties required to satisfy PM requirements → Must/Should/Could
- Platform, data-contract, integration, and deployment constraints
- Technical silences: PM or compliance requirements with no architectural spec

**Apply Law B here (Step 3)**: Write closure sentence inline for each technical silence gap.

Assign IDs: A-NN (architect). Flag blockers.

---

## STEP 4: UX LENS (constrained by Steps 1-3)

**Apply Law A here (Step 4)**: Flag ambiguities inline at first encounter.

UX requirements are generated against the full compliance + PM + architect baseline.
Accessibility requirements mandated by compliance (Step 1) inherit Must priority.

Extract:
- Interaction requirements (including compliance-mandated accessibility) → Must/Should/Could
- Error states and recovery flows
- First-run and onboarding experience
- UX silences: user journey phases with no interaction requirement

**Apply Law B here (Step 4)**: Write closure sentence inline for each UX gap found.

Assign IDs: U-NN (UX). Flag blockers.

---

## STEP 5: MOSCOW SYNTHESIS

Consolidate all requirements from Steps 1-4. Rules:
- Compliance mandates (Step 1) govern tier assignment — no PM or UX vote can demote them
- Any requirement blocking a Must-tier item is also Must
- Tier promotions from Should→Must require justification note: "Promoted R-NN: [reason]"
- IDs are stable: no renumbering, no collisions

### Must Have
| ID | Lens | Requirement | Blocks |
|----|------|-------------|--------|
| | | | |

### Should Have
| ID | Lens | Requirement | Blocks |
|----|------|-------------|--------|
| | | | |

### Could Have
| ID | Lens | Requirement | Blocks |
|----|------|-------------|--------|
| | | | |

### Won't Have
| ID | Lens | Requirement | Note |
|----|------|-------------|------|
| | | | |

---

## STEP 6: DEPENDENCY GRAPH

Name at least one root blocker. State WHY it is foundational — not just which IDs it blocks.
Show second-order chains: R-NN → R-MM → R-PP with reasoning at each link.
If compliance requirements (C-NN) are foundational, they must appear as root blockers here.

---

## STEP 7: LIFECYCLE PHASE COVERAGE AUDIT

**Apply Law A here (Step 7)**: If a phase gap reveals an ambiguous requirement boundary,
write the [AMBIG:] notation inline before logging the SS- entry.

| Phase | Coverage | SS- entry |
|-------|----------|-----------|
| First-run / onboarding | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Core-use / steady-state | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Upgrade / migration | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Error / recovery | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Observability / audit | COVERED / PARTIAL / SILENT | [SS-NN or —] |

Note: Observability/audit phase must be checked against compliance requirements from Step 1 —
audit log requirements are frequently silenced in PM/UX specs but mandated by regulation.

---

## STEP 8: AMBIGUITY FLAGS

**Apply Law A here (Step 8)**: This section formalizes all [AMBIG:] notations from Steps 1-7.
Every inline notation must appear here. Do not introduce new ambiguities for the first time.

**Apply Law B here (Step 8)**: Every entry from the prior open AF- register must appear below.
State the closure sentence:
  "Every entry from the prior open AF- register appears in this section with a status:
   open / resolved / out-of-scope."

**AF-NN: [requirement ID or spec phrase]**
- Source: "[exact quote from input]"
- Interpretation A: [what team A would build]
- Interpretation B: [what team B would build]
- Consequence: [how the product diverges between A and B]
- Status: open / resolved / out-of-scope

[Repeat for all AF- entries. Zero AF- on a complex input is a fail.]

Closure: Every entry from the prior open AF- register appears in this section with a status. ✓

---

## STEP 9: SPEC-FAULT FINDINGS

**Apply Law B here (Step 9)**: Every entry from the prior open SF- register must appear below.
State the closure sentence:
  "Every entry from the prior open SF- register appears in this section with a status:
   open / resolved / out-of-scope."

**SF-NN: [gap or contradiction in the input spec]**
- Severity: P0 / P1 / P2
- Affected requirements: [IDs]
- Status: open / resolved / out-of-scope

[At least one SF- entry expected for a non-trivial input.]

Closure: Every entry from the prior open SF- register appears in this section with a status. ✓

---

## PRE-OUTPUT VERIFICATION PROTOCOL (C-19 / Loop 3 — verify)

Before emitting the final artifact, verify each criterion by ID. This table audits PROCESS
COMPLIANCE — whether format laws were applied during extraction, not only whether sections exist.

| ID | Criterion | Process check | Status |
|----|-----------|--------------|--------|
| C-01 | Dual-directory search | Did Step 0 state results from both simulations/scout/ AND simulations/trace/skill/? | PASS/FAIL |
| C-02 | MoSCoW structure | Does Step 5 have four named tiers (not a flat list)? | PASS/FAIL |
| C-03 | Root blocker named | Does Step 6 name a root blocker with blocked IDs and foundational reasoning? | PASS/FAIL |
| C-04 | Ambiguity flags raised | Does Step 8 have at least one AF- entry? | PASS/FAIL |
| C-05 | Three+ lenses traceable | Are Compliance, PM, and Architect each traceable in the MoSCoW table? | PASS/FAIL |
| C-06 | Suspicious silences | Does Step 7 include at least one SS- entry? | PASS/FAIL |
| C-07 | SF- findings raised | Does Step 9 include at least one SF- entry? | PASS/FAIL |
| C-08 | Stable IDs + promotions | No ID collisions; tier promotions include justification? | PASS/FAIL |
| C-09 | Transitive dependency graph | Does Step 6 show second-order chains (A→B→C) with reasoning? | PASS/FAIL |
| C-10 | AF- cites source text | Does each AF- entry include an exact quote from the input? | PASS/FAIL |
| C-11 | Lifecycle phase audit | Does Step 7 name all five phases with coverage status? | PASS/FAIL |
| C-12 | Cross-session continuity | Do Steps 8 and 9 carry prior entries with explicit status? | PASS/FAIL |
| C-13 | Two-interpretation AF- format | Does each AF- have Interpretation A + B + Consequence? | PASS/FAIL |
| C-14 | Rubric self-check gate | Is this verification table present before the final artifact? | PASS/FAIL |
| C-15 (Law A) | Law A applied at extraction | Were [AMBIG:] notations generated DURING Steps 1-7, not introduced fresh in Step 8? | PASS/FAIL |
| C-16 (Law B) | Law B closure gates | Do Steps 8 and 9 each contain the explicit closure sentence? | PASS/FAIL |
| C-17 | Three-loop enforcement | Are all three loops present: charter (C-17/Loop1), step reinstatements (C-18/Loop2), this table (C-19/Loop3)? | PASS/FAIL |
| C-18 | Step-level reinstatements | Does each extraction step (1-9) that triggers Law A or B contain "Apply Law [A/B] here"? | PASS/FAIL |
| C-19 | Process-diagnostic rows | Does this table include rows C-15 and C-16 auditing whether laws were applied during extraction? | PASS/FAIL |
| C-20 | Prevention-detection complementarity | Does the charter state that C-18 creates the artifacts C-19 requires as evidence? | PASS/FAIL |
| C-21 | Recursive meta-loop naming | Does the charter name C-17=Loop1, C-18=Loop2, C-19=Loop3 by rubric ID? | PASS/FAIL |
| C-22 | Loop 2→3 design contract | Does the charter name the Loop 2→3 artifact dependency as a structural contract (not inferred)? | PASS/FAIL |
| C-23 | Per-law independent chains | Does the charter assign independent declare/apply/verify triplets per law? | PASS/FAIL |
| C-24 | Structural closure of meta-loop | Does the charter state C-17 instantiates C-18 as logical consequence — structurally incomplete without it? | PASS/FAIL |
| C-25 | Per-law artifact form in design contract | Does the design contract name what artifact C-18-A creates (inline [AMBIG:]) and what C-18-B creates (closure sentences), and what C-19-A/B audit specifically? | PASS/FAIL |
| C-26 | Per-law sub-IDs in unified closure statement | Does the structural closure statement name "C-18 (both Law A's C-18-A and Law B's C-18-B)" by sub-ID? | PASS/FAIL |
| C-27 | Definitional non-enforcement framing | Does the structural closure section include "declaring X without Y is not enforcement — it is an incomplete declaration"? | PASS/FAIL |

If any FAIL in C-01..C-07, resolve before emitting. Aspirational FAILs noted but do not block.

---

Write artifact to: simulations/scout/requirements/{{topic}}-requirements-{{date}}.md
Frontmatter: skill: scout-requirements, topic: {{topic}}, date: {{date}},
             skill_version: 3.0, input: [source spec path]
```

---

## V-02: Output Format — Requirement Table

**Axis**: Output format
**Hypothesis**: Replacing role-by-role prose extraction with a unified requirements table forces
explicit per-requirement annotation of law attribution, MoSCoW tier, dependency links, and
ambiguity status. A table with a Law-Ref column makes C-25's per-law artifact tracking
structurally unavoidable — each row must declare which format law applies, which in turn
requires the charter to have named those laws with their artifact forms. The charter machinery
is unchanged; only how requirements are captured varies.

---

```
You are running /scout-requirements for: {{topic}}

---

## CHARTER — FORMAT LAWS AND THREE-LOOP META-REQUIREMENT

This charter is C-17 (Loop 1 / declare) of the three-loop meta-requirement. It declares two
format laws and their per-law enforcement chains before any extraction begins.

### Format Law A: Two-Path AF- Rule

Every ambiguity encountered during extraction carries an inline notation at first encounter:

  [AMBIG: "{exact source text}" → A: {interpretation A} | B: {interpretation B}]

This rule applies AT FIRST ENCOUNTER in the requirements table — not deferred to the AF- section.
The AF- section formalizes inline notations already captured in the table's Ambig column.

### Format Law B: Downstream Closure Rule

Each downstream findings section (AF-, SF-) contains the following explicit closure statement:

  "Every entry from the prior open [AF- / SF-] register appears in this section
   with a status: open / resolved / out-of-scope."

### Law A Independent Enforcement Chain

- **C-17-A (Loop 1-A / declare)**: Law A declared here, independently of Law B.
- **C-18-A (Loop 2-A / apply)**: Each table row where the Ambig column is non-empty contains
  an inline [AMBIG:] notation in the Requirement cell, carrying both interpretation paths before
  the row is finalized.
- **C-19-A (Loop 3-A / verify)**: The pre-output verification table includes a row auditing
  whether [AMBIG:] notations with dual paths appear in the Ambig column of applicable rows —
  not merely whether the AF- section exists.

### Law B Independent Enforcement Chain

- **C-17-B (Loop 1-B / declare)**: Law B declared here, independently of Law A.
- **C-18-B (Loop 2-B / apply)**: Each downstream findings section contains an inline closure
  sentence written before the section is closed.
- **C-19-B (Loop 3-B / verify)**: The pre-output verification table includes a row auditing
  whether closure sentences appeared in each downstream section.

### Three-Loop Meta-Requirement: Structural Closure

The two law chains unify under one self-closing declaration:

- **C-17 (Loop 1 / declare)** = this charter, including both Law A and Law B independent chains
- **C-18 (Loop 2 / apply)** = the row-level [AMBIG:] notations (Law A) and section closure
  sentences (Law B), applied per law
- **C-19 (Loop 3 / verify)** = the pre-output verification protocol table

**Structural Closure**: Declaring format laws without an application layer is not enforcement —
it is an incomplete declaration. Without Loop 2, this charter has stated intent but not created
enforcement; the category "enforcement" cannot apply without an application layer by definition.
Asserting C-17 simultaneously instantiates C-18 (both Law A's C-18-A and Law B's C-18-B) as
necessary consequences: declaring the laws constitutes the obligation to apply them per row.
C-19 closes the loop by auditing that C-18's applications occurred.

### Loop 2 → Loop 3 Design Contract

This charter names the following as a structural obligation before extraction begins, chartered
here as a design contract and not inferred from structural proximity:

**C-18 (Loop 2) creates the execution artifacts that C-19 (Loop 3) requires as evidence.**

Specifically, per law:
- **Law A's C-18-A** creates inline [AMBIG:] notations in the Requirement cell and Ambig
  column of each applicable table row, each notation carrying Interpretation A and B.
  C-19-A audits specifically whether these dual-path notations appear in the table at each
  applicable row — not whether the AF- summary section contains entries.
- **Law B's C-18-B** creates inline closure sentences at the close of each downstream findings
  section. C-19-B audits specifically whether closure sentences are present and correctly formed
  in each applicable section — not whether prior entries are enumerated anywhere.

C-18 prevents violations at extraction time. C-19 detects violations that slipped through.
C-18's artifacts are C-19's evidence. They are complementary prevention-detection layers.

---

## STEP 0: DUAL-DIRECTORY SEARCH

Search for prior scout signals in BOTH:
- simulations/scout/ — real runs for {{topic}}
- simulations/trace/skill/ — hand-compiled traces for {{topic}}

State what you found in each directory. If either is empty, say so explicitly.

**Apply Law B here (Step 0)**: List all open AF- and SF- entries from prior runs.
State the closure sentence:
  "Every entry from the prior open findings register appears in this step with a status:
   open / resolved / out-of-scope."

SF-01 (undefined search path): CLOSED if trace found in simulations/trace/skill/; else OPEN.

---

## STEP 1: REQUIREMENTS EXTRACTION — UNIFIED TABLE

Extract requirements through all four lenses simultaneously into the table below.
Assign a stable ID (R-NN), lens label, MoSCoW tier, and dependency edges as you extract.

**Apply Law A here (Step 1)**: For any row where the Requirement text contains an ambiguity,
write the [AMBIG:] notation inline in the Requirement cell AND populate the Ambig column with
the AF- ID before moving to the next row. Do not defer.

Law-Ref column values: A (Law A ambiguity applies), B (Law B closure applies), AB (both), — (neither).

| ID | MoSCoW | Lens | Requirement | Blocks | Depends-On | Law-Ref | Ambig |
|----|--------|------|-------------|--------|------------|---------|-------|
| R-01 | | PM | | | | | |
| R-02 | | Architect | | | | | |
| R-03 | | UX | | | | | |
| R-04 | | Compliance | | | | | |
| ... | | | | | | | |

Extraction guide:
- PM lens: user goals, competitive capabilities, delight features, explicit exclusions
- Architect lens: structural properties, platform constraints, data contracts, integrations
- UX lens: interaction patterns, error states, first-run experience, accessibility
- Compliance lens: legal mandates (auto-Must), conditional obligations, audit requirements
- A requirement blocking a Must-tier item is also Must (promote + justify: "Promoted R-NN: [reason]")

---

## STEP 2: DEPENDENCY GRAPH

Name at least one root blocker from the table above. State WHY it is foundational.
Show second-order chains: R-NN → R-MM → R-PP with reasoning at each link.

---

## STEP 3: LIFECYCLE PHASE COVERAGE AUDIT

Review the requirements table for lifecycle coverage.

**Apply Law A here (Step 3)**: If a coverage gap reveals an ambiguous requirement boundary,
add a row to the table with an [AMBIG:] notation before logging the SS- entry below.

| Phase | Coverage | Rows covering it | SS- entry |
|-------|----------|-----------------|-----------|
| First-run / onboarding | COVERED / PARTIAL / SILENT | [R-IDs or —] | [SS-NN or —] |
| Core-use / steady-state | COVERED / PARTIAL / SILENT | [R-IDs or —] | [SS-NN or —] |
| Upgrade / migration | COVERED / PARTIAL / SILENT | [R-IDs or —] | [SS-NN or —] |
| Error / recovery | COVERED / PARTIAL / SILENT | [R-IDs or —] | [SS-NN or —] |
| Observability / audit | COVERED / PARTIAL / SILENT | [R-IDs or —] | [SS-NN or —] |

---

## STEP 4: AMBIGUITY FLAGS

**Apply Law A here (Step 4)**: This section formalizes all [AMBIG:] notations from the table
and Step 3. Every inline notation must appear here. Do not introduce new ambiguities here.

**Apply Law B here (Step 4)**: Every entry from the prior open AF- register must appear below.
State the closure sentence:
  "Every entry from the prior open AF- register appears in this section with a status:
   open / resolved / out-of-scope."

**AF-NN: [requirement ID or spec phrase]**
- Source: "[exact quote from input]"
- Interpretation A: [what team A would build]
- Interpretation B: [what team B would build]
- Consequence: [how the product diverges between A and B]
- Status: open / resolved / out-of-scope

Closure: Every entry from the prior open AF- register appears in this section with a status. ✓

---

## STEP 5: SPEC-FAULT FINDINGS

**Apply Law B here (Step 5)**: Every entry from the prior open SF- register must appear below.
State the closure sentence:
  "Every entry from the prior open SF- register appears in this section with a status:
   open / resolved / out-of-scope."

**SF-NN: [gap or contradiction in the input spec]**
- Severity: P0 / P1 / P2
- Affected rows: [IDs from requirements table]
- Status: open / resolved / out-of-scope

Closure: Every entry from the prior open SF- register appears in this section with a status. ✓

---

## PRE-OUTPUT VERIFICATION PROTOCOL (C-19 / Loop 3 — verify)

| ID | Criterion | Process check | Status |
|----|-----------|--------------|--------|
| C-01 | Dual-directory search | Did Step 0 state results from both simulations/scout/ AND simulations/trace/skill/? | PASS/FAIL |
| C-02 | MoSCoW structure | Does the requirements table have rows across all four MoSCoW tiers? | PASS/FAIL |
| C-03 | Root blocker named | Does Step 2 name a root blocker with blocked IDs and foundational reasoning? | PASS/FAIL |
| C-04 | Ambiguity flags raised | Does Step 4 have at least one AF- entry? | PASS/FAIL |
| C-05 | Three+ lenses traceable | Are PM, Architect, and at least one of UX/Compliance rows present in the table? | PASS/FAIL |
| C-06 | Suspicious silences | Does Step 3 include at least one SS- entry? | PASS/FAIL |
| C-07 | SF- findings raised | Does Step 5 include at least one SF- entry? | PASS/FAIL |
| C-08 | Stable IDs + promotions | No ID collisions in the table; promoted rows include justification? | PASS/FAIL |
| C-09 | Transitive dependency graph | Does Step 2 show second-order chains (A→B→C) with reasoning? | PASS/FAIL |
| C-10 | AF- cites source text | Does each AF- entry include an exact quote from the input? | PASS/FAIL |
| C-11 | Lifecycle phase audit | Does Step 3 name all five phases with coverage status? | PASS/FAIL |
| C-12 | Cross-session continuity | Do Steps 4 and 5 carry prior entries with explicit status? | PASS/FAIL |
| C-13 | Two-interpretation AF- format | Does each AF- have Interpretation A + B + Consequence? | PASS/FAIL |
| C-14 | Rubric self-check gate | Is this verification table present before the final artifact? | PASS/FAIL |
| C-15 (Law A) | Law A applied at extraction | Were [AMBIG:] notations entered IN the table (Step 1/3), not introduced fresh in Step 4? | PASS/FAIL |
| C-16 (Law B) | Law B closure gates | Do Steps 4 and 5 each contain the explicit closure sentence? | PASS/FAIL |
| C-17 | Three-loop enforcement | Charter (C-17/Loop1) / row-level notations (C-18/Loop2) / this table (C-19/Loop3) — all three present? | PASS/FAIL |
| C-18 | Step-level reinstatements | Does each table step that triggers Law A or B contain "Apply Law [A/B] here"? | PASS/FAIL |
| C-19 | Process-diagnostic rows | Does this table include rows C-15 and C-16 auditing whether laws were applied during extraction? | PASS/FAIL |
| C-20 | Prevention-detection complementarity | Does the charter state C-18 creates the artifacts C-19 requires as evidence? | PASS/FAIL |
| C-21 | Recursive meta-loop naming | Does the charter name C-17=Loop1, C-18=Loop2, C-19=Loop3 by rubric ID? | PASS/FAIL |
| C-22 | Loop 2→3 design contract | Does the charter name the Loop 2→3 artifact dependency as a structural contract (not inferred)? | PASS/FAIL |
| C-23 | Per-law independent chains | Does the charter assign independent declare/apply/verify triplets per law? | PASS/FAIL |
| C-24 | Structural closure of meta-loop | Does the charter state C-17 instantiates C-18 as logical consequence? | PASS/FAIL |
| C-25 | Per-law artifact form in design contract | Does the design contract specify that C-18-A creates [AMBIG:] table notations and C-18-B creates closure sentences, with per-artifact C-19 audit rows? | PASS/FAIL |
| C-26 | Per-law sub-IDs in unified closure statement | Does the structural closure name "C-18 (both Law A's C-18-A and Law B's C-18-B)" by sub-ID? | PASS/FAIL |
| C-27 | Definitional non-enforcement framing | Does the structural closure include "declaring X without Y is not enforcement — it is an incomplete declaration"? | PASS/FAIL |

If any FAIL in C-01..C-07, resolve before emitting.

---

Write artifact to: simulations/scout/requirements/{{topic}}-requirements-{{date}}.md
Frontmatter: skill: scout-requirements, topic: {{topic}}, date: {{date}},
             skill_version: 3.0, input: [source spec path]
```

---

## V-03: Phrasing Register — Conversational Imperative

**Axis**: Phrasing register
**Hypothesis**: Short, direct command sentences ("Search both directories. State what you find.")
eliminate explanatory overhead and test whether the charter machinery can survive without the
redundant prose scaffolding. If the criteria are in the content, not the explanation, imperative
phrasing should not reduce the score. The risk is C-26 — the exact sub-ID phrasing in the
unified closure statement may degrade under terse instructions because the model has less
structural guidance about which specific sentence form is required.

---

```
You are running /scout-requirements for: {{topic}}

---

## CHARTER

Loop 1 (C-17 / declare). Two format laws govern all extraction.

### Law A — Two-Path Rule

Write every ambiguity inline at first encounter:

  [AMBIG: "{exact text}" → A: {reading A} | B: {reading B}]

Apply at first encounter. Not deferred.

### Law B — Closure Rule

End every downstream section (AF-, SF-) with the explicit sentence:
  "Every entry from the prior open [register] appears here with a status."

### Law A Chain (independent of Law B)

- **C-17-A**: Law A declared here.
- **C-18-A**: Each extraction step that hits an ambiguity: write "Apply Law A here."
  Then write both interpretations inline before logging the AF- entry.
- **C-19-A**: Verification table row: did [AMBIG:] dual-path notations appear at each
  applicable extraction step? (Process audit — not section audit.)

### Law B Chain (independent of Law A)

- **C-17-B**: Law B declared here.
- **C-18-B**: Each downstream section: write "Apply Law B here."
  Then write the closure sentence inline before closing.
- **C-19-B**: Verification table row: did closure sentences appear in each downstream section?

### Meta-Requirement

Three loops. One declaration.
- **C-17 (Loop 1 / declare)** = this charter (both chains)
- **C-18 (Loop 2 / apply)** = step-level reinstatements, per law
- **C-19 (Loop 3 / verify)** = the pre-output verification table

Declaring format laws without an application layer is not enforcement — it is an incomplete
declaration. The category "enforcement" does not apply without Loop 2 by definition.
Asserting C-17 simultaneously instantiates C-18 (both Law A's C-18-A and Law B's C-18-B)
as necessary consequences. Loop 2 is non-skippable: C-17's declaration constitutes the
obligation to apply.

### Loop 2 → Loop 3 Design Contract

Chartered here. Not inferred.

**C-18 creates artifacts. C-19 audits them. Per law:**

- **Law A's C-18-A**: creates inline [AMBIG:] notations (dual-path) at each ambiguity step.
  C-19-A audits whether these appeared at each applicable step.
- **Law B's C-18-B**: creates inline closure sentences at each downstream section.
  C-19-B audits whether these appeared in each applicable section.

C-18 prevents violations. C-19 detects what slipped through. Complementary layers.

---

## STEP 0: SEARCH

Search both directories:
- simulations/scout/
- simulations/trace/skill/

State what you found in each. State explicitly if either is empty. Never skip either.

**Apply Law B here.** List open AF- and SF- from prior runs. Write:
  "Every entry from the prior open findings register appears here with a status:
   open / resolved / out-of-scope."

---

## STEP 1: EXTRACT

Extract requirements through four lenses: PM, Architect, UX, Compliance.

**Apply Law A here.** Write [AMBIG:] inline at first encounter for each ambiguity.

Assign each requirement: ID (R-NN), MoSCoW tier, lens label. Name blockers: "BLOCKS: [IDs]."

PM: user goals, competitive capabilities, delight features, explicit exclusions.
Architect: structural properties, platform, data contracts, constraints.
UX: interaction patterns, error states, first-run experience, accessibility.
Compliance: legal mandates (auto-Must), conditional obligations, audit requirements.

Tier promotions: state reason inline. "Promoted R-NN from [tier] to [tier]: [reason]."

---

## STEP 2: MOSCOW TABLE

Four tiers. IDs from Step 1 only.

### Must Have
| ID | Lens | Requirement | Blocks |

### Should Have
| ID | Lens | Requirement | Blocks |

### Could Have
| ID | Lens | Requirement | Blocks |

### Won't Have
| ID | Lens | Requirement | Note |

---

## STEP 3: DEPENDENCY GRAPH

Name at least one root blocker. State why foundational. Show A→B→C chains.

---

## STEP 4: LIFECYCLE AUDIT

**Apply Law A here.** Flag any ambiguous coverage gap inline before logging SS-.

| Phase | Coverage | SS- |
|-------|----------|-----|
| First-run / onboarding | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Core-use / steady-state | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Upgrade / migration | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Error / recovery | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Observability / audit | COVERED / PARTIAL / SILENT | [SS-NN or —] |

---

## STEP 5: AMBIGUITY FLAGS

**Apply Law A here.** Formalize all [AMBIG:] notations from Steps 1 and 4. No new ones here.

**Apply Law B here.** Write:
  "Every entry from the prior open AF- register appears in this section with a status:
   open / resolved / out-of-scope."

**AF-NN:**
- Source: "[exact quote from input]"
- Interpretation A: [reading] — Consequence: [divergence]
- Interpretation B: [reading] — Consequence: [divergence]
- Status: open / resolved / out-of-scope

[Zero AF- on a complex input is a fail.]

Closure: Every entry from the prior open AF- register appears in this section with a status. ✓

---

## STEP 6: SPEC FAULTS

**Apply Law B here.** Write:
  "Every entry from the prior open SF- register appears in this section with a status:
   open / resolved / out-of-scope."

**SF-NN:** [gap or contradiction] — Severity: P0/P1/P2 — Affected: [IDs] — Status

[At least one SF- expected for a non-trivial input.]

Closure: Every entry from the prior open SF- register appears in this section with a status. ✓

---

## VERIFY (C-19 / Loop 3)

| ID | Check | Status |
|----|-------|--------|
| C-01 | Both directories searched and stated? | PASS/FAIL |
| C-02 | Four MoSCoW tiers present? | PASS/FAIL |
| C-03 | Root blocker named with IDs and reasoning? | PASS/FAIL |
| C-04 | At least one AF- entry? | PASS/FAIL |
| C-05 | Three+ lenses traceable? | PASS/FAIL |
| C-06 | At least one SS- entry? | PASS/FAIL |
| C-07 | At least one SF- entry? | PASS/FAIL |
| C-08 | Stable IDs, justified promotions? | PASS/FAIL |
| C-09 | Second-order chains in dependency graph? | PASS/FAIL |
| C-10 | Each AF- has exact source quote? | PASS/FAIL |
| C-11 | All five lifecycle phases named with status? | PASS/FAIL |
| C-12 | Prior AF-/SF- carried with explicit status? | PASS/FAIL |
| C-13 | Each AF- has Interpretation A + B + Consequence? | PASS/FAIL |
| C-14 | This table present before final output? | PASS/FAIL |
| C-15 (Law A) | Were [AMBIG:] notations created DURING extraction (not fresh in Step 5)? | PASS/FAIL |
| C-16 (Law B) | Does each downstream section carry the explicit closure sentence? | PASS/FAIL |
| C-17 | Three loops present: charter / step reinstatements / this table? | PASS/FAIL |
| C-18 | Each triggering step contains "Apply Law [A/B] here"? | PASS/FAIL |
| C-19 | This table includes rows C-15 and C-16 auditing process compliance? | PASS/FAIL |
| C-20 | Charter states C-18 creates artifacts C-19 requires? | PASS/FAIL |
| C-21 | Charter names C-17=Loop1, C-18=Loop2, C-19=Loop3 by ID? | PASS/FAIL |
| C-22 | Design contract named as "chartered here, not inferred"? | PASS/FAIL |
| C-23 | Per-law independent chains declared? | PASS/FAIL |
| C-24 | C-17 instantiates C-18 as logical consequence stated? | PASS/FAIL |
| C-25 | Design contract names C-18-A artifact ([AMBIG:]) and C-18-B artifact (closure sentences), with per-artifact C-19-A/B audit rows? | PASS/FAIL |
| C-26 | Unified closure names "C-18 (both Law A's C-18-A and Law B's C-18-B)" by sub-ID? | PASS/FAIL |
| C-27 | Structural closure includes "declaring X without Y is not enforcement — it is an incomplete declaration"? | PASS/FAIL |

Resolve any FAIL in C-01..C-07 before emitting.

---

Write to: simulations/scout/requirements/{{topic}}-requirements-{{date}}.md
```

---

## V-04: Compliance-First + Definitional Register

**Axis**: Role sequence + phrasing register (combination)
**Hypothesis**: Combining compliance-first role ordering with formal definitional language
throughout produces C-27's categorical framing as a natural byproduct: compliance reasoning
natively operates in terms of "what qualifies as X" (jurisdictional category membership)
rather than "what is required for X" (structural necessity). A charter written in definitional
register will state "without Loop 2, this charter is not an enforcement charter by definition"
rather than "without Loop 2, this charter is incomplete." The combination also tests whether
compliance-first ordering creates tension with the MoSCoW synthesis step — where Compliance
requirements must remain immovable while subsequent roles negotiate tiers.

---

```
You are running /scout-requirements for: {{topic}}

---

## CHARTER — FORMAT LAWS AND THREE-LOOP META-REQUIREMENT

This charter constitutes Loop 1 (C-17 / declare) of the three-loop meta-requirement. It defines
two format laws before any extraction begins. A process that does not apply these laws does not
constitute requirements extraction — it constitutes requirements listing, which is categorically
insufficient for a requirements signal.

### Format Law A: Two-Path AF- Rule

An ambiguity flag (AF-) is defined as: a named ambiguity carrying two distinct plausible
interpretations and the consequence of each. An AF- entry without both interpretations does
not qualify as an ambiguity flag — it qualifies as an ambiguity mention.

Every ambiguity encountered during extraction carries an inline notation at first encounter:

  [AMBIG: "{exact source text}" → A: {interpretation A} | B: {interpretation B}]

This notation constitutes the AF- entry's evidentiary basis. An AF- section that lists
ambiguities without prior inline notations does not constitute Law A compliance.

### Format Law B: Downstream Closure Rule

A downstream findings section (AF-, SF-) is defined as compliant under Law B if and only if
it contains the following explicit closure statement:

  "Every entry from the prior open [AF- / SF-] register appears in this section
   with a status: open / resolved / out-of-scope."

A section without this statement does not constitute a closed findings section regardless of
whether prior entries appear within it.

### Law A Independent Enforcement Chain

- **C-17-A (Loop 1-A / declare)**: Law A declared here, independently of Law B.
  A failure in Law A's apply chain does not constitute a failure of Law B's chain.
- **C-18-A (Loop 2-A / apply)**: Each extraction step where an ambiguity is encountered
  constitutes a Law A trigger. A triggered step is compliant if and only if it contains
  "Apply Law A here" followed by both interpretation paths inline.
- **C-19-A (Loop 3-A / verify)**: The pre-output verification table contains a row whose pass
  condition is: did [AMBIG:] dual-interpretation notations appear in each Law A trigger step
  during extraction? A row auditing only whether the AF- section exists does not constitute
  a C-19-A compliant row.

### Law B Independent Enforcement Chain

- **C-17-B (Loop 1-B / declare)**: Law B declared here, independently of Law A.
  A failure in Law B's apply chain does not constitute a failure of Law A's chain.
- **C-18-B (Loop 2-B / apply)**: Each downstream findings section constitutes a Law B trigger.
  A triggered section is compliant if and only if it contains "Apply Law B here" followed by
  the closure sentence inline.
- **C-19-B (Loop 3-B / verify)**: The pre-output verification table contains a row whose pass
  condition is: did closure sentences appear in each Law B trigger section during execution?

### Three-Loop Meta-Requirement: Structural Closure

The two law chains constitute a unified meta-requirement under one self-closing declaration:

- **C-17 (Loop 1 / declare)** = this charter, including both Law A and Law B independent chains
- **C-18 (Loop 2 / apply)** = the step-level reinstatements from both chains, applied per law
- **C-19 (Loop 3 / verify)** = the pre-output verification protocol table

**Structural Closure (Definitional)**: A charter that declares format laws (C-17) without
requiring their application at each triggering step (C-18) does not constitute an enforcement
charter — it constitutes a declaration without operative mechanism. The category "enforcement
charter" is defined by the presence of all three loops. Declaring format laws without an
application layer is not enforcement — it is an incomplete declaration. A two-loop structure
(declare + verify without apply) is outside the set of enforcement charters by definition.

Asserting C-17 simultaneously instantiates C-18 (both Law A's C-18-A and Law B's C-18-B) as
necessary constitutive consequences: declaring laws does not constitute declaring enforcement
unless the application obligation is simultaneously created. A structure that asserts C-17
while omitting C-18 does not constitute a weaker enforcement charter — it constitutes a
structure categorically outside the set of enforcement charters. C-19 then constitutes the
verification that C-18 obligations were fulfilled, completing the definition.

### Loop 2 → Loop 3 Design Contract

This charter names the following as a constitutive structural obligation before extraction
begins, chartered here as a design contract and not inferred from structural proximity:

**C-18 (Loop 2) creates the execution artifacts that C-19 (Loop 3) requires as evidence.**

Specifically, per law:
- **Law A's C-18-A** constitutes the creation of inline [AMBIG:] notations at each Law A
  trigger step, each carrying Interpretation A and B. C-19-A constitutes an audit of whether
  these dual-interpretation notations are present and complete at each applicable step — not
  an audit of whether the AF- section exists.
- **Law B's C-18-B** constitutes the creation of inline closure sentences at each Law B
  trigger section. C-19-B constitutes an audit of whether closure sentences are present and
  correctly formed at each applicable section — not an audit of whether prior entries appear.

C-18 constitutes prevention: violations are blocked at execution time. C-19 constitutes
detection: violations that passed C-18 are identified at verification time. A structure with
C-19 but no C-18 does not constitute a prevention-detection system — it constitutes detection
without prevention, which is categorically incomplete enforcement.

---

## STEP 0: DUAL-DIRECTORY SEARCH

Search for prior scout signals in BOTH:
- simulations/scout/ — real runs for {{topic}}
- simulations/trace/skill/ — hand-compiled traces for {{topic}}

A search that does not explicitly state findings from both directories does not constitute a
compliant dual-directory search regardless of what was found.

**Apply Law B here (Step 0)**: List all open AF- and SF- entries from prior runs. Write:
  "Every entry from the prior open findings register appears in this step with a status:
   open / resolved / out-of-scope."

SF-01 (undefined search path): CLOSED if trace found in simulations/trace/skill/; else OPEN.

---

## STEP 1: COMPLIANCE LENS (constitutes the regulatory foundation)

**Apply Law A here (Step 1)**: Write [AMBIG:] inline at first encounter for each ambiguity.

Extract regulatory requirements first. Compliance-sourced requirements constitute the
non-negotiable tier floor for all subsequent role analysis. A requirement that originates in
regulation is defined as Must Have by category.

- Legal or regulatory mandates → Must Have (the regulation constitutes the Must classification)
- Conditional compliance obligations → Should/Could depending on applicability scope
- Audit, reporting, and data-retention requirements implied by the concept
- Compliance silences: areas where the concept's scope implies regulatory obligations
  without naming them → SS- candidates

**Apply Law B here (Step 1)**: Write closure sentence inline for each compliance silence gap.

Assign IDs: C-NN. Flag blockers: "BLOCKS: [IDs]."

---

## STEP 2: PM LENS (constrained by regulatory foundation)

**Apply Law A here (Step 2)**: Write [AMBIG:] inline at first encounter.

PM requirements are extracted against the compliance foundation from Step 1. A PM requirement
that conflicts with a Step 1 compliance mandate does not constitute a legitimate Should or
Could candidate — it constitutes a constraint violation and must be flagged as SF-.

Extract: user goals → Must/Should/Could. Competitive capabilities → Should. Delight → Could.
Explicit exclusions → Won't Have. User scenario gaps → SS- candidates.

**Apply Law B here (Step 2)**: Write closure sentence inline for each scenario gap found.

Assign IDs: P-NN. Flag blockers.

---

## STEP 3: ARCHITECT LENS (constrained by compliance + PM)

**Apply Law A here (Step 3)**: Write [AMBIG:] inline at first encounter.

Technical requirements inherit tier from their compliance or PM parent when the technical
property is constitutively required to satisfy the parent. Requirements enabling compliance
mandates constitute Must-tier items by structural entailment.

Extract: system properties enabling compliance → Must (inherit tier). Properties enabling PM
requirements → Must/Should/Could. Platform, data, integration constraints. Technical silences.

**Apply Law B here (Step 3)**: Write closure sentence inline for each technical silence.

Assign IDs: A-NN. Flag blockers.

---

## STEP 4: UX LENS (constrained by compliance + PM + Architect)

**Apply Law A here (Step 4)**: Write [AMBIG:] inline at first encounter.

Accessibility requirements mandated by compliance (Step 1) constitute Must-tier UX requirements
by category. UX negotiation applies only within the space compliance has left unspecified.

Extract: interaction requirements → Must/Should/Could. Error states. First-run experience.
Accessibility (compliance-anchored = Must by category). UX silences → SS- candidates.

**Apply Law B here (Step 4)**: Write closure sentence inline for each UX gap.

Assign IDs: U-NN. Flag blockers.

---

## STEP 5: MOSCOW SYNTHESIS

Consolidate requirements from Steps 1-4. Compliance requirements constitute immovable Must
items by definition. Tier promotions from Should→Must require justification: "Promoted R-NN: [reason]."
ID stability: no renumbering, no collisions.

### Must Have
| ID | Lens | Requirement | Blocks |
|----|------|-------------|--------|

### Should Have
| ID | Lens | Requirement | Blocks |
|----|------|-------------|--------|

### Could Have
| ID | Lens | Requirement | Blocks |
|----|------|-------------|--------|

### Won't Have
| ID | Lens | Requirement | Note |
|----|------|-------------|------|

---

## STEP 6: DEPENDENCY GRAPH

Name at least one root blocker. State what category it constitutes and why it blocks.
Show A→B→C chains with reasoning at each link.

---

## STEP 7: LIFECYCLE PHASE COVERAGE AUDIT

**Apply Law A here (Step 7)**: Write [AMBIG:] inline for any ambiguous coverage boundary.

| Phase | Coverage | SS- entry |
|-------|----------|-----------|
| First-run / onboarding | COVERED / PARTIAL / SILENT | |
| Core-use / steady-state | COVERED / PARTIAL / SILENT | |
| Upgrade / migration | COVERED / PARTIAL / SILENT | |
| Error / recovery | COVERED / PARTIAL / SILENT | |
| Observability / audit | COVERED / PARTIAL / SILENT | |

---

## STEP 8: AMBIGUITY FLAGS

**Apply Law A here (Step 8)**: Formalize all [AMBIG:] notations from Steps 1-7. No new ones.

**Apply Law B here (Step 8)**: Write:
  "Every entry from the prior open AF- register appears in this section with a status:
   open / resolved / out-of-scope."

**AF-NN:**
- Source: "[exact quote]"
- Interpretation A: [reading] — Consequence: [divergence]
- Interpretation B: [reading] — Consequence: [divergence]
- Status: open / resolved / out-of-scope

Closure: Every entry from the prior open AF- register appears in this section with a status. ✓

---

## STEP 9: SPEC-FAULT FINDINGS

**Apply Law B here (Step 9)**: Write:
  "Every entry from the prior open SF- register appears in this section with a status:
   open / resolved / out-of-scope."

**SF-NN:** [gap or contradiction] — Severity: P0/P1/P2 — Affected: [IDs] — Status

Closure: Every entry from the prior open SF- register appears in this section with a status. ✓

---

## PRE-OUTPUT VERIFICATION PROTOCOL (C-19 / Loop 3 — verify)

| ID | Criterion | Process check | Status |
|----|-----------|--------------|--------|
| C-01 | Dual-directory search | Did Step 0 state results from both directories explicitly? | PASS/FAIL |
| C-02 | MoSCoW structure | Does Step 5 have four named tiers? | PASS/FAIL |
| C-03 | Root blocker named | Does Step 6 name a root blocker with category, blocked IDs, and reasoning? | PASS/FAIL |
| C-04 | Ambiguity flags raised | Does Step 8 have at least one AF- entry? | PASS/FAIL |
| C-05 | Three+ lenses traceable | Are Compliance, PM, and Architect each traceable in the MoSCoW table? | PASS/FAIL |
| C-06 | Suspicious silences | Does Step 7 include at least one SS- entry? | PASS/FAIL |
| C-07 | SF- findings raised | Does Step 9 include at least one SF- entry? | PASS/FAIL |
| C-08 | Stable IDs + promotions | No ID collisions; tier promotions justified? | PASS/FAIL |
| C-09 | Transitive dependency graph | Does Step 6 show second-order chains (A→B→C) with reasoning? | PASS/FAIL |
| C-10 | AF- cites source text | Does each AF- include an exact quote? | PASS/FAIL |
| C-11 | Lifecycle phase audit | Does Step 7 name all five phases with coverage status? | PASS/FAIL |
| C-12 | Cross-session continuity | Do Steps 8 and 9 carry prior entries with explicit status? | PASS/FAIL |
| C-13 | Two-interpretation AF- format | Does each AF- have Interpretation A + B + Consequence? | PASS/FAIL |
| C-14 | Rubric self-check gate | Is this table present before the final artifact? | PASS/FAIL |
| C-15 (Law A) | Law A applied at extraction | Were [AMBIG:] notations generated DURING Steps 1-7, not fresh in Step 8? | PASS/FAIL |
| C-16 (Law B) | Law B closure gates | Do Steps 8 and 9 each contain the explicit closure sentence? | PASS/FAIL |
| C-17 | Three-loop enforcement | Charter / step reinstatements / this table — all three present? | PASS/FAIL |
| C-18 | Step-level reinstatements | Does each triggering step contain "Apply Law [A/B] here"? | PASS/FAIL |
| C-19 | Process-diagnostic rows | Does this table include rows C-15 and C-16 auditing process compliance? | PASS/FAIL |
| C-20 | Prevention-detection complementarity | Does charter state C-18 constitutes artifacts C-19 requires? | PASS/FAIL |
| C-21 | Recursive meta-loop naming | Does charter name C-17=Loop1, C-18=Loop2, C-19=Loop3 by rubric ID? | PASS/FAIL |
| C-22 | Loop 2→3 design contract | Does charter name the artifact dependency as a constitutive structural contract? | PASS/FAIL |
| C-23 | Per-law independent chains | Does charter assign independent enforce chains per law? | PASS/FAIL |
| C-24 | Structural closure | Does charter state C-17 instantiates C-18 as necessary constitutive consequence? | PASS/FAIL |
| C-25 | Per-law artifact form | Does design contract specify C-18-A creates [AMBIG:] notations and C-18-B creates closure sentences, with per-artifact audit rows? | PASS/FAIL |
| C-26 | Per-law sub-IDs in closure | Does unified closure name "C-18 (both Law A's C-18-A and Law B's C-18-B)" by sub-ID? | PASS/FAIL |
| C-27 | Definitional framing | Does structural closure include "declaring X without Y is not enforcement — it is an incomplete declaration"? | PASS/FAIL |

Resolve any FAIL in C-01..C-07 before emitting.

---

Write artifact to: simulations/scout/requirements/{{topic}}-requirements-{{date}}.md
Frontmatter: skill: scout-requirements, topic: {{topic}}, date: {{date}},
             skill_version: 3.0, input: [source spec path]
```

---

## V-05: Output Format + Inertia Framing

**Axis**: Output format + inertia framing (combination)
**Hypothesis**: Table format forces per-requirement law attribution (C-25 structurally unavoidable).
Inertia framing — explicitly naming what the team would *not know* without each step — raises
the perceived cost of skipping any section and anchors the model to each step's purpose before
execution. The inertia framing also creates a natural entry point for C-27's definitional
language: "without Step 1, there is no compliance foundation — what follows is requirements
listing, not requirements extraction." This tests whether purpose-anchoring language reinforces
the charter's definitional framing or introduces noise.

---

```
You are running /scout-requirements for: {{topic}}

---

## CHARTER — FORMAT LAWS AND THREE-LOOP META-REQUIREMENT

This charter is C-17 (Loop 1 / declare). It declares two format laws and their enforcement
chains before any extraction begins.

**Why this charter exists**: Without format laws applied at extraction time, the output of
this skill is a requirements list, not a requirements signal. A requirements signal carries
evidence of the extraction process — inline ambiguity notations, closed findings registers,
per-section audit trails. Without these artifacts, the output cannot be scored, reviewed, or
carried forward into subsequent sessions. The charter creates the artifacts; the artifacts
create the signal.

### Format Law A: Two-Path AF- Rule

Every ambiguity encountered during extraction carries an inline notation at first encounter:

  [AMBIG: "{exact source text}" → A: {interpretation A} | B: {interpretation B}]

Applied AT FIRST ENCOUNTER in the requirements table and extraction steps. The AF- section
formalizes notations already captured inline.

**Without Law A applied at extraction**: Two teams reading the final output would disagree
on what was ambiguous and in which direction — the signal cannot drive alignment.

### Format Law B: Downstream Closure Rule

Each downstream findings section (AF-, SF-) contains the explicit closure statement:

  "Every entry from the prior open [AF- / SF-] register appears in this section
   with a status: open / resolved / out-of-scope."

**Without Law B**: Prior open findings drop silently between sessions with no audit trail.

### Law A Independent Enforcement Chain

- **C-17-A (Loop 1-A / declare)**: Law A declared here. Independent of Law B.
- **C-18-A (Loop 2-A / apply)**: Each extraction step or table row with an ambiguity contains
  "Apply Law A here" followed by both interpretation paths inline before the AF- ID is logged.
- **C-19-A (Loop 3-A / verify)**: Verification table row: did [AMBIG:] dual-path notations
  appear at each applicable extraction step? (Process audit — not section existence.)

### Law B Independent Enforcement Chain

- **C-17-B (Loop 1-B / declare)**: Law B declared here. Independent of Law A.
- **C-18-B (Loop 2-B / apply)**: Each downstream findings section contains "Apply Law B here"
  followed by the closure sentence inline before the section closes.
- **C-19-B (Loop 3-B / verify)**: Verification table row: did closure sentences appear in
  each downstream section?

### Three-Loop Meta-Requirement: Structural Closure

The two law chains unify under one self-closing declaration:

- **C-17 (Loop 1 / declare)** = this charter (both law chains)
- **C-18 (Loop 2 / apply)** = per-law step-level reinstatements
- **C-19 (Loop 3 / verify)** = the pre-output verification protocol table

**Structural Closure**: Declaring format laws without an application layer is not enforcement —
it is an incomplete declaration. A charter with no Loop 2 has named the laws but has not
created enforcement; the output is requirements listing with aspirational footnotes, not a
requirements signal. Asserting C-17 simultaneously instantiates C-18 (both Law A's C-18-A and
Law B's C-18-B) as necessary consequences: the act of declaring creates the obligation to apply.
C-19 audits that the obligation was fulfilled.

**Without the three-loop structure**: Laws A and B become advisory. The output may appear to
satisfy format constraints while the process that produced it did not — the signal cannot be
verified against the process that created it.

### Loop 2 → Loop 3 Design Contract

Chartered here as a design contract, not inferred from structural proximity:

**C-18 (Loop 2) creates the execution artifacts that C-19 (Loop 3) requires as evidence.**

Specifically, per law:
- **Law A's C-18-A** creates inline [AMBIG:] notations in the requirements table's Ambig
  column and extraction step prose, each carrying Interpretation A and B. C-19-A audits
  specifically whether these dual-path notations appeared at each applicable extraction step.
- **Law B's C-18-B** creates inline closure sentences at each downstream findings section.
  C-19-B audits specifically whether closure sentences appeared in each applicable section.

**Without this design contract**: C-19 would audit output structure (are sections present?)
rather than process compliance (were laws applied during extraction?). Output-structure auditing
cannot catch a process that skipped Law A and populated the AF- section retroactively.

C-18 prevents violations at extraction time. C-19 detects violations that slipped through.
They are complementary prevention-detection layers: C-18's artifacts are C-19's evidence.

---

## STEP 0: DUAL-DIRECTORY SEARCH

**Without this step**: No knowledge of prior signals for {{topic}}. Duplicate discovery work.
No continuity with prior sessions. No cross-session finding closure.

Search for prior scout signals in BOTH:
- simulations/scout/ — real runs for {{topic}}
- simulations/trace/skill/ — hand-compiled traces for {{topic}}

State what you found in each. If either is empty, say so explicitly. Never skip either.

**Apply Law B here (Step 0)**: List all open AF- and SF- entries from prior runs. Write:
  "Every entry from the prior open findings register appears in this step with a status:
   open / resolved / out-of-scope."

SF-01 (undefined search path): CLOSED if trace found in simulations/trace/skill/; else OPEN.

---

## STEP 1: REQUIREMENTS EXTRACTION — UNIFIED TABLE

**Without this step**: The concept remains undifferentiated. No MoSCoW prioritization, no
lens attribution, no dependency mapping. The team cannot sequence work or identify what the
concept actually requires from each stakeholder dimension.

Extract requirements through all four lenses into the table below.

**Apply Law A here (Step 1)**: For any row where the Requirement contains an ambiguity, write
the [AMBIG:] notation inline in the Requirement cell AND populate the Ambig column with the
AF- ID before moving to the next row. Do not defer.

Law-Ref: A = Law A triggered, B = Law B applies, AB = both, — = neither.

| ID | MoSCoW | Lens | Requirement | Blocks | Depends-On | Law-Ref | Ambig |
|----|--------|------|-------------|--------|------------|---------|-------|
| R-01 | Must/Should/Could/Won't | PM | [text; [AMBIG:] if ambiguous] | [IDs] | [IDs] | [A/B/AB/—] | [AF-NN or —] |
| R-02 | | Architect | | | | | |
| R-03 | | UX | | | | | |
| R-04 | | Compliance | | | | | |
| ... | | | | | | | |

Lens extraction guide:
- **PM**: user goals, competitive capabilities, delight features, explicit exclusions
- **Architect**: structural properties, platform constraints, data contracts, integrations
- **UX**: interaction patterns, error states, first-run experience, accessibility
- **Compliance**: legal mandates (auto-Must), conditional obligations, audit requirements

Tier rules: blocking a Must item = Must (promote + justify: "Promoted R-NN: [reason]").

---

## STEP 2: DEPENDENCY GRAPH

**Without this step**: No sequence for the work. Blocked requirements begin in parallel with
their prerequisites, creating rework when foundations are found missing mid-implementation.

Name at least one root blocker from the table. State WHY it is foundational.
Show second-order chains: R-NN → R-MM → R-PP with reasoning at each link.

---

## STEP 3: LIFECYCLE PHASE COVERAGE AUDIT

**Without this step**: Entire phases of the product experience have no requirements.
First-run onboarding, upgrade paths, and observability are most frequently silenced — discovered
only when a user reports that something that "wasn't specified" is broken.

**Apply Law A here (Step 3)**: If a coverage gap reveals an ambiguous requirement boundary,
add a row to the table with [AMBIG:] and an AF- ID before logging the SS- entry.

| Phase | Coverage | Rows covering it | SS- entry |
|-------|----------|-----------------|-----------|
| First-run / onboarding | COVERED / PARTIAL / SILENT | [R-IDs or —] | [SS-NN or —] |
| Core-use / steady-state | COVERED / PARTIAL / SILENT | [R-IDs or —] | [SS-NN or —] |
| Upgrade / migration | COVERED / PARTIAL / SILENT | [R-IDs or —] | [SS-NN or —] |
| Error / recovery | COVERED / PARTIAL / SILENT | [R-IDs or —] | [SS-NN or —] |
| Observability / audit | COVERED / PARTIAL / SILENT | [R-IDs or —] | [SS-NN or —] |

---

## STEP 4: AMBIGUITY FLAGS

**Without this step**: Ambiguities in the requirements table remain unresolved. Two teams
implement opposite interpretations. The signal contains noise rather than evidence.

**Apply Law A here (Step 4)**: Formalize all [AMBIG:] notations from the table and Step 3.
Every inline notation must appear here. Do not introduce new ambiguities.

**Apply Law B here (Step 4)**: Write:
  "Every entry from the prior open AF- register appears in this section with a status:
   open / resolved / out-of-scope."

**AF-NN: [requirement ID or spec phrase]**
- Source: "[exact quote from input]"
- Interpretation A: [what team A would build] — Consequence: [divergence]
- Interpretation B: [what team B would build] — Consequence: [divergence]
- Status: open / resolved / out-of-scope

[Zero AF- on a complex input is a fail.]

Closure: Every entry from the prior open AF- register appears in this section with a status. ✓

---

## STEP 5: SPEC-FAULT FINDINGS

**Without this step**: Gaps and contradictions in the input spec remain unnamed. The team
builds against an underspecified concept and discovers contradictions during implementation,
when the cost to resolve them is highest.

**Apply Law B here (Step 5)**: Write:
  "Every entry from the prior open SF- register appears in this section with a status:
   open / resolved / out-of-scope."

**SF-NN: [gap or contradiction]**
- Severity: P0 / P1 / P2
- Affected rows: [IDs from requirements table]
- Status: open / resolved / out-of-scope

[At least one SF- expected for a non-trivial input.]

Closure: Every entry from the prior open SF- register appears in this section with a status. ✓

---

## PRE-OUTPUT VERIFICATION PROTOCOL (C-19 / Loop 3 — verify)

**Without this step**: Format law violations that slipped through extraction survive into the
artifact undetected. The signal cannot be verified against the process that created it.

| ID | Criterion | Process check | Status |
|----|-----------|--------------|--------|
| C-01 | Dual-directory search | Did Step 0 state results from both simulations/scout/ AND simulations/trace/skill/? | PASS/FAIL |
| C-02 | MoSCoW structure | Does the table include rows across all four MoSCoW tiers? | PASS/FAIL |
| C-03 | Root blocker named | Does Step 2 name a root blocker with blocked IDs and foundational reasoning? | PASS/FAIL |
| C-04 | Ambiguity flags raised | Does Step 4 have at least one AF- entry? | PASS/FAIL |
| C-05 | Three+ lenses traceable | Are PM, Architect, and at least one of UX/Compliance present in the table? | PASS/FAIL |
| C-06 | Suspicious silences | Does Step 3 include at least one SS- entry? | PASS/FAIL |
| C-07 | SF- findings raised | Does Step 5 include at least one SF- entry? | PASS/FAIL |
| C-08 | Stable IDs + promotions | No ID collisions; promoted rows justified? | PASS/FAIL |
| C-09 | Transitive dependency graph | Does Step 2 show second-order chains (A→B→C) with foundational reasoning? | PASS/FAIL |
| C-10 | AF- cites source text | Does each AF- include an exact quote from the input? | PASS/FAIL |
| C-11 | Lifecycle phase audit | Does Step 3 name all five phases with coverage status and covering rows? | PASS/FAIL |
| C-12 | Cross-session continuity | Do Steps 4 and 5 carry prior entries with explicit status? | PASS/FAIL |
| C-13 | Two-interpretation AF- format | Does each AF- have Interpretation A + B + Consequence? | PASS/FAIL |
| C-14 | Rubric self-check gate | Is this table present before the final artifact? | PASS/FAIL |
| C-15 (Law A) | Law A applied at extraction | Were [AMBIG:] notations created in the table (Step 1/3), not introduced fresh in Step 4? | PASS/FAIL |
| C-16 (Law B) | Law B closure gates | Do Steps 4 and 5 each contain the explicit closure sentence? | PASS/FAIL |
| C-17 | Three-loop enforcement | Charter / step reinstatements / this table — all three present? | PASS/FAIL |
| C-18 | Step-level reinstatements | Does each triggering step contain "Apply Law [A/B] here"? | PASS/FAIL |
| C-19 | Process-diagnostic rows | Does this table include rows C-15 and C-16 auditing process execution? | PASS/FAIL |
| C-20 | Prevention-detection complementarity | Does charter state C-18 creates artifacts C-19 requires? | PASS/FAIL |
| C-21 | Recursive meta-loop naming | Does charter name C-17=Loop1, C-18=Loop2, C-19=Loop3 by rubric ID? | PASS/FAIL |
| C-22 | Loop 2→3 design contract | Does charter name the Loop 2→3 dependency as a chartered contract (not inferred)? | PASS/FAIL |
| C-23 | Per-law independent chains | Does charter assign independent declare/apply/verify triplets per law? | PASS/FAIL |
| C-24 | Structural closure | Does charter state C-17 instantiates C-18 as necessary consequence? | PASS/FAIL |
| C-25 | Per-law artifact form | Does design contract specify C-18-A creates [AMBIG:] table notations and C-18-B creates closure sentences, with per-artifact C-19-A/B audit rows? | PASS/FAIL |
| C-26 | Per-law sub-IDs in unified closure | Does structural closure name "C-18 (both Law A's C-18-A and Law B's C-18-B)" by sub-ID? | PASS/FAIL |
| C-27 | Definitional non-enforcement framing | Does structural closure include "declaring X without Y is not enforcement — it is an incomplete declaration"? | PASS/FAIL |

Resolve any FAIL in C-01..C-07 before emitting.

---

Write artifact to: simulations/scout/requirements/{{topic}}-requirements-{{date}}.md
Frontmatter: skill: scout-requirements, topic: {{topic}}, date: {{date}},
             skill_version: 3.0, input: [source spec path]
```

---

## Scoring Predictions vs Risks

| Var | Predicted | C-25 risk | C-26 risk | C-27 risk | Primary structural risk |
|-----|-----------|-----------|-----------|-----------|-------------------------|
| V-01 | 128/128 | LOW — design contract unchanged | LOW — closure statement unchanged | LOW — definitional framing present | Medium: compliance-first adds 4 role steps instead of 1 unified extraction; model may drift before synthesis |
| V-02 | 128/128 | LOW — table Law-Ref column makes per-law artifact attribution structurally required | LOW — charter unchanged | LOW — charter unchanged | Medium: table format may compress extraction; model may omit inline [AMBIG:] in prose and put only in Ambig column (satisfies C-15 but weaker signal) |
| V-03 | 126/128 | LOW — design contract present | MEDIUM — terse phrasing reduces structural repetition; model may write "C-18-A and C-18-B" without the exact embedding C-26 requires in the unified closure statement | LOW — definitional sentence present | HIGH: terse register reduces instruction surface area; C-26's exact pass form ("C-18 (both Law A's C-18-A and Law B's C-18-B)") may not be reliably reproduced by a model with fewer surrounding anchors |
| V-04 | 128/128 | LOW — design contract with definitional framing amplifies C-25 | LOW — charter unchanged | LOW — definitional register produces C-27 evidence as a natural byproduct | Low: definitional register is consistent throughout; compliance-first adds structure without removing charter clarity |
| V-05 | 128/128 | LOW — table Law-Ref column + design contract both present | LOW — charter unchanged | LOW — "not enforcement" framing in inertia anchors reinforces charter's C-27 language | Low: inertia framing adds purpose anchors without removing enforcement mechanisms; additive not substitutive |

**V-03 is the only variation predicted below 128/128.** The terse imperative register reduces
the structural repetition that makes C-26's exact phrasing ("C-18 (both Law A's C-18-A and
Law B's C-18-B)") reliably produced. All other variations preserve the charter's full text or
extend it; V-03 compresses it, which is the only axis that creates genuine downside risk.

**V-04 is predicted to produce the most distinctive C-27 evidence.** The definitional register
generates categorical framing throughout the charter, not just in the structural closure
section — which may cause the rubric to score C-27 as clearly PASS rather than borderline PASS.

**V-05's inertia framing is the only variation that explicitly names the output failure mode.**
Every "Without this step..." anchor names the specific signal degradation that results from
skipping — which reinforces the charter's own C-27 claim that a structure without Loop 2 is
not enforcement by providing domain-level examples of what "not enforcement" looks like in
practice for each step.
