Written to `simulations/quest/golden/scout-requirements-golden-2026-03-14.md`.

**Summary:**

- **Score**: 130/138 (V-05 simplified — source was 138/138, -8 pts from removing Inertia Gates and verification table)
- **Golden**: yes (threshold 111/138)

**What made it golden (vs V-01 baseline at 132/138):**

1. **Definitional register throughout (C-29)** — "X is not Y without Z" is the primary explanatory voice everywhere: law declarations, step instructions, design contract. V-01 confines this register to the three absence clause sections only; extraction steps stay imperative.

2. **Compliance-first ordering (C-32)** — Step 1 = Compliance, Step 2 = PM (constrained by compliance), Step 3 = Architect (constrained by compliance + PM). Step headers name the constraint chain explicitly. V-01 uses standard order.

3. **Named Loop Absence Clause heading sections (C-30)** — shared with V-01, but the probe across R4 confirmed this is what makes C-28 structurally unavoidable vs. V-02's prose-embedded equivalent.

4. **Named Inertia Gate blocks at every step (C-31)** — present in V-05 pre-simplification; moved absence-clause coverage from loop granularity down to step granularity. Removed in simplification (aspirational-only, 637 words, zero essential dependency).

5. **Law chain entries in definitional form** — each C-18-A/B entry is framed as a definitional obligation ("A triggered step is not Law A compliant without..."), not just a procedure. V-01 names the chains procedurally.
lauses: "A requirements run that begins without this charter is not a requirements
  run with format enforcement — it is unstructured extraction"

The register is constitutive, not additive. Removing it would require rewriting the
substantive instruction text at each step, not just trimming sections.

### 2. Compliance-first extraction ordering (C-32)

V-01 uses standard extraction order (PM typically first, compliance somewhere in the sequence).
V-05 places Step 1 = Compliance, Step 2 = PM (constrained by compliance), Step 3 = Architect
(constrained by compliance + PM). The step sequence itself is a structural enforcement signal:
PM and architect requirements are extracted within scope already bounded by compliance. Each
step header names its constraint chain explicitly — "STEP 2: PM LENS (constrained by compliance
foundation)" — making the dependency visible in the outline, not only in the charter prose.

### 3. Named Loop Absence Clause heading sections (C-30)

Three `#### Loop N Absence Clause` heading sections make per-loop absence structure visible
at the document outline level. V-01 also has these (shared pattern). V-02 demonstrated that
prose-embedded absence statements satisfy C-28 (content present) but not C-30 (not structurally
navigable). The named headings make per-loop absence discoverable without reading the full
charter body.

### 4. Named Inertia Gate blocks at every Loop 2 extraction step (C-31) — present in V-05,
   removed in simplified

V-05 (pre-simplification) appended `**Inertia Gate (Step N)**` blocks after each extraction
step in definitional form: "A requirements set that lacks PM-lens output is not a product
requirements signal — it is an unstructured list." This moved absence-clause coverage from
loop granularity (C-28/C-30) down to step granularity within Loop 2. Removed in simplification
because C-31 is aspirational (2 pts) and the blocks added 637 words with zero essential
criterion dependency.

### 5. Law chain entries written in definitional form

Each C-18-A/B chain entry is framed as a definitional obligation, not just a procedure:
- "A triggered step is not Law A compliant without 'Apply Law A here' followed immediately
  by both interpretation paths inline"
- "A step that logs the AF- ID without writing both paths is not a Law A compliant application"

V-01 names the chains but writes them as procedural requirements. V-05's framing makes the
compliance test definitionally precise: a reader cannot satisfy the chain by checking the
box — they must satisfy the definitional condition.

---

## Prompt Body

```
You are running /scout-requirements for: {{topic}}

---

## CHARTER -- FORMAT LAWS AND THREE-LOOP META-REQUIREMENT

This charter constitutes Loop 1 (C-17 / declare) of the three-loop meta-requirement.
A requirements run is not a governed requirements run without this charter -- it is unstructured
extraction. The charter does not merely precede Loop 2; it is the precondition for Loop 2's
category membership as "enforcement application."

### Format Law A: Two-Path AF- Rule

An ambiguity flag is not a Law A compliant entry without two named interpretation paths and
their consequence. Every ambiguity encountered during extraction carries an inline notation
at first encounter:

  [AMBIG: "{exact source text}" -> A: {interpretation A} | B: {interpretation B}]

An AF- section that introduces ambiguities without prior inline notations is not a Law A
compliant section -- it is a deferred-work section that violates the AT FIRST ENCOUNTER rule.

### Format Law B: Downstream Closure Rule

A downstream findings section (AF-, SF-) is not a closed section without the following
explicit closure statement:

  "Every entry from the prior open [AF- / SF-] register appears in this section
   with a status: open / resolved / out-of-scope."

A section containing prior entries without this statement is not a closed section -- it is
an enumeration. The closure statement is the condition that converts enumeration into Law B
compliance.

### Law A Independent Enforcement Chain

- **C-17-A (Loop 1-A / declare)**: Law A declared here, independently of Law B.
  A failure in Law A's chain is not a failure of Law B's chain.
- **C-18-A (Loop 2-A / apply)**: A triggered step is not Law A compliant without "Apply Law A
  here" followed immediately by both interpretation paths inline. A step that logs the AF- ID
  without writing both paths is not a Law A compliant application.
- **C-19-A (Loop 3-A / verify)**: A verification row is not C-19-A compliant without auditing
  whether dual-interpretation [AMBIG:] notations appeared at each applicable extraction step --
  auditing the AF- section's existence is not a C-19-A process audit.

### Law B Independent Enforcement Chain

- **C-17-B (Loop 1-B / declare)**: Law B declared here, independently of Law A.
  A failure in Law B's chain is not a failure of Law A's chain.
- **C-18-B (Loop 2-B / apply)**: A downstream section is not Law B compliant without
  "Apply Law B here" followed immediately by the closure sentence inline.
- **C-19-B (Loop 3-B / verify)**: A verification row is not C-19-B compliant without auditing
  whether closure sentences appeared in each downstream section -- auditing whether prior entries
  appear anywhere is not a C-19-B audit.

### Three-Loop Meta-Requirement: Structural Closure

The two law chains unify under one self-closing declaration:

- **C-17 (Loop 1 / declare)** = this charter, including both Law A and Law B independent chains
- **C-18 (Loop 2 / apply)** = the step-level cross-references from both chains, applied per law
- **C-19 (Loop 3 / verify)** = the pre-output verification protocol table

#### Loop 1 Absence Clause

A requirements run that begins without this charter is not a requirements run with format
enforcement -- it is unstructured extraction. Without Loop 1, the format laws do not exist;
without format laws, Loop 2's reinstatements have no laws to reinstate, and the category
"enforcement application" cannot apply to any step. Loop 1 is not the first of three sequential
steps -- it is the definitional frame within which the other two steps acquire their enforcement
meaning.

**Structural Closure**: Declaring format laws without an application layer is not enforcement --
it is an incomplete declaration. A charter that declares Law A and Law B (C-17) without requiring
inline reinstatement at each triggering step (C-18) has not created enforcement; the category
"enforcement" requires Loop 2 by definition. Without Loop 2, what exists is a statement of
intent, not enforcement. Asserting C-17 simultaneously instantiates C-18 (both Law A's C-18-A
and Law B's C-18-B) as necessary consequences: the act of declaring laws constitutes the
obligation to apply them at each triggering step. C-19 closes the loop by auditing that C-18's
applications occurred.

#### Loop 2 Absence Clause

A charter that declares format laws without Loop 2's execution layer is not an enforcement
charter -- it is a declaration without operative mechanism. Without Loop 2 (C-18's step-level
reinstatements), Loop 3 has no artifacts to audit: C-18-A's inline [AMBIG:] notations are
the evidence C-19-A requires; C-18-B's inline closure sentences are the evidence C-19-B
requires. A Loop 3 verification table operating without C-18's artifacts is not a verification
pass -- it is structural theater: auditing a process that produced no checkable output.

#### Loop 3 Absence Clause

An extraction that applies format laws at each step without auditing those applications is not
a governed extraction -- it is an asserted-compliant extraction. Without Loop 3 (C-19's
verification table), Loop 2's prevention work is confirmed only by assertion; violations that
passed C-18's inline enforcement have no detection layer. A prevention-only system is not an
enforcement system -- it is half an enforcement system. Loop 3 is the verification condition
that makes the prevention-detection pair definitionally complete.

### Loop 2 -> Loop 3 Design Contract

This charter names the following as a constitutive structural obligation before extraction
begins, chartered here as a design contract and not inferred from structural proximity:

**C-18 (Loop 2) creates the execution artifacts that C-19 (Loop 3) requires as evidence.**

C-19 without C-18's artifacts is not a verification pass -- it is a verification of nothing.
Per law:
- **Law A's C-18-A** creates inline [AMBIG:] notations at each ambiguity step, each carrying
  Interpretation A and Interpretation B. A C-19-A audit row is not compliant without checking
  whether these dual-path notations are present at each applicable step -- a row that checks
  only whether the AF- section exists is not a C-19-A audit.
- **Law B's C-18-B** creates inline closure sentences in each downstream findings section.
  A C-19-B audit row is not compliant without checking whether closure sentences are present
  and correctly formed at each applicable section -- a row that checks only whether prior entries
  appear is not a C-19-B audit.

C-18 constitutes prevention. C-19 constitutes detection. A system with C-19 but no C-18 is not
a weaker enforcement system -- it is a detection system verifying the absence of artifacts it
never created. They are complementary layers, not alternatives.

---

## STEP 0: DUAL-DIRECTORY SEARCH

Search for prior scout signals in BOTH:
- simulations/scout/ -- real runs for {{topic}}
- simulations/trace/skill/ -- hand-compiled traces for {{topic}}

A search that does not state explicit results from both directories is not a compliant
dual-directory search -- it is a partial search regardless of what was found.

**Apply Law B here (Step 0)**: List all open AF- and SF- entries from prior runs.
State the closure sentence:
  "Every entry from the prior open findings register appears in this step with a status:
   open / resolved / out-of-scope."

SF-01 (undefined search path): CLOSED if trace found in simulations/trace/skill/; else OPEN.

---

## STEP 1: COMPLIANCE LENS (constitutes the non-negotiable tier foundation)

**Apply Law A here (Step 1)**: Write [AMBIG:] inline at first encounter.

Compliance requirements are not negotiable tier assignments -- they are Must Have by regulatory
category. Extract:
- Legal or regulatory mandates -> Must Have (the mandate constitutes the justification)
- Conditional compliance obligations (jurisdiction-scoped) -> Should/Could
- Audit, reporting, and data-retention requirements implied by the concept
- Compliance silences: features in regulated spaces without named obligations are not clean --
  they are features with undetected requirements

**Apply Law B here (Step 1)**: Write closure sentence inline for each compliance silence found.

Assign IDs: C-NN (compliance). Flag blockers: "BLOCKS: [list of requirement IDs blocked]."

---

## STEP 2: PM LENS (constrained by compliance foundation)

**Apply Law A here (Step 2)**: Write [AMBIG:] inline at first encounter.

A PM requirement that conflicts with a Step 1 compliance mandate is not a legitimate Should
or Could candidate -- it is a constraint violation. Extract:
- User goals -> Must Have (if compliance-anchored) or Should Have
- Competitive capabilities -> Should Have
- Delight features -> Could Have
- Explicit user exclusions -> Won't Have
- User scenario gaps -> SS- candidates

**Apply Law B here (Step 2)**: Write closure sentence inline for each scenario gap found.

Assign IDs: P-NN (PM). Flag blockers.

---

## STEP 3: ARCHITECT LENS (constrained by compliance + PM)

**Apply Law A here (Step 3)**: Write [AMBIG:] inline at first encounter.

A technical requirement enabling a compliance mandate inherits Must status by structural
entailment -- it is not a negotiable preference. Extract:
- System properties enabling compliance mandates -> Must (inherit tier from mandate)
- System properties enabling PM requirements -> Must/Should/Could
- Platform, data-contract, integration, and deployment constraints
- Technical silences: compliance or PM requirements with no architectural specification

**Apply Law B here (Step 3)**: Write closure sentence inline for each technical silence.

Assign IDs: A-NN (architect). Flag blockers.

---

## STEP 4: UX LENS (constrained by compliance + PM + architect)

**Apply Law A here (Step 4)**: Write [AMBIG:] inline at first encounter.

An accessibility requirement mandated by compliance is not a UX Could Have -- it is Must Have
by compliance category. Extract:
- Interaction requirements -> Must/Should/Could
- Error states and recovery flows: a feature without an error state is not a complete feature
- First-run and onboarding experience
- Accessibility (compliance-anchored = Must by category)
- UX silences: journey phases with no interaction coverage -> SS- candidates

**Apply Law B here (Step 4)**: Write closure sentence inline for each UX gap.

Assign IDs: U-NN (UX). Flag blockers.

---

## STEP 5: MOSCOW SYNTHESIS

Consolidate all requirements from Steps 1-4. Rules:
- Compliance mandates are not subject to tier negotiation -- they constitute immovable Must items
- A requirement blocking a Must-tier item is not optional -- it is Must by blocking dependency
- Tier promotions from Should->Must require justification note: "Promoted R-NN: [reason]"
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

Name at least one root blocker. State what category it constitutes and why it blocks.
Show second-order chains: R-NN -> R-MM -> R-PP with reasoning at each link.

---

## STEP 7: LIFECYCLE PHASE COVERAGE AUDIT

**Apply Law A here (Step 7)**: Write [AMBIG:] inline for any ambiguous coverage boundary.

| Phase | Coverage | SS- entry |
|-------|----------|-----------|
| First-run / onboarding | COVERED / PARTIAL / SILENT | [SS-NN or --] |
| Core-use / steady-state | COVERED / PARTIAL / SILENT | [SS-NN or --] |
| Upgrade / migration | COVERED / PARTIAL / SILENT | [SS-NN or --] |
| Error / recovery | COVERED / PARTIAL / SILENT | [SS-NN or --] |
| Observability / audit | COVERED / PARTIAL / SILENT | [SS-NN or --] |

---

## STEP 8: AMBIGUITY FLAGS

**Apply Law A here (Step 8)**: This section formalizes all [AMBIG:] notations from Steps 1-7.
An AF- section that introduces new ambiguities here is not a Law A compliant section.

**Apply Law B here (Step 8)**: Every entry from the prior open AF- register must appear below.
State the closure sentence:
  "Every entry from the prior open AF- register appears in this section with a status:
   open / resolved / out-of-scope."

**AF-NN: [requirement ID or spec phrase]**
- Source: "[exact quote from input]" -- an AF- without an exact source quote is not a documented
  ambiguity; it is an undocumented claim
- Interpretation A: [what team A would build]
- Interpretation B: [what team B would build]
- Consequence: [how the product diverges between A and B]
- Status: open / resolved / out-of-scope

[Zero AF- on a complex input is not a clean result -- it is an under-extracted one.]

Closure: Every entry from the prior open AF- register appears in this section with a status.

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

Closure: Every entry from the prior open SF- register appears in this section with a status.

---

Write artifact to: simulations/scout/requirements/{{topic}}-requirements-{{date}}.md
Frontmatter: skill: scout-requirements, topic: {{topic}}, date: {{date}},
             skill_version: 4.0, input: [source spec path]
```

---

## Final Rubric Criteria Summary — v5 (32 criteria, 138 pts)

### Essential (60 pts — 12 pts each)

| ID | Criterion | Simplified status |
|----|-----------|-------------------|
| C-01 | Dual-directory search (simulations/scout/ + simulations/trace/skill/) | PASS |
| C-02 | MoSCoW four-tier table (Must/Should/Could/Won't) with ID, Lens, Requirement, Blocks | PASS |
| C-03 | At least one root blocker named with dependent chain | PASS |
| C-04 | AF- entries with Source, Interpretation A, Interpretation B, Consequence, Status | PASS |
| C-05 | Three or more lenses traceable (compliance, PM, architect each present) | PASS |

### Recommended (30 pts — 10 pts each)

| ID | Criterion | Simplified status |
|----|-----------|-------------------|
| C-06 | SS- entries in lifecycle phase coverage audit (Step 7) | PASS |
| C-07 | SF- entries for spec gaps or contradictions (Step 9) | PASS |
| C-08 | Stable IDs: no renumbering, no collisions across steps | PASS |

### Aspirational (48 pts — 2 pts each)

| ID | Criterion | Simplified status | Note |
|----|-----------|-------------------|------|
| C-09 | Law A reinstatement inline at each triggering step | PASS | |
| C-10 | Law B reinstatement inline at each downstream section | PASS | |
| C-11 | AF- entries cite exact source quote | PASS | |
| C-12 | Blocked requirements carry "BLOCKS: [IDs]" notation | PASS | |
| C-13 | Tier promotions carry justification notes | PASS | |
| C-14 | Pre-output verification table present (self-check gate) | FAIL | Removed in simplification |
| C-15 | C-17/C-18/C-19 named explicitly in charter | PASS | |
| C-16 | Law A and Law B declared as independent chains | PASS | |
| C-17 | Three-loop structure present (declare / apply / verify) | PASS | |
| C-18 | Per-law independent enforcement chains (A and B separate) | PASS | |
| C-19 | Verification table rows audit per-law at each applicable step | FAIL | Removed in simplification |
| C-20 | Design contract names C-18/C-19 relationship as structural obligation | PASS | |
| C-21 | Per-law artifact form specified in design contract | PASS | |
| C-22 | Per-law independent chains each include declare/apply/verify | PASS | |
| C-23 | Structural closure names C-17/C-18/C-19 with sub-IDs | PASS | |
| C-24 | Charter includes C-26 (asserting C-17 instantiates C-18) | PASS | |
| C-25 | Charter opens with definitional framing of requirements run | PASS | |
| C-26 | Asserting C-17 simultaneously instantiates C-18 as necessary consequence | PASS | |
| C-27 | Structural closure contains global definitional statement | PASS | |
| C-28 | Per-loop absence clauses present in charter (all three loops) | PARTIAL | Inertia Gates removed; named sections preserved |
| C-29 | Definitional register is primary explanatory mode throughout | PASS | |
| C-30 | Per-loop absence clauses appear as named heading sections (not only prose) | PASS | |
| C-31 | Named Inertia Gate blocks at each Loop 2 extraction step | FAIL | Removed in simplification |
| C-32 | Compliance lens is first extraction step (compliance-first ordering) | PASS | |

### Scoring Bands

| Band | Score | Meaning |
|------|-------|---------|
| Golden | 125-138 | All essential + recommended pass; strong aspirational |
| Strong | 108-124 | All essential pass; most recommended; partial aspirational |
| Acceptable | 88-107 | All essential pass; partial recommended; minimal aspirational |
| Weak | 60-87 | All essential pass; recommended largely missing |
| Fail | < 60 | One or more essential criteria fail |

**Golden threshold**: all 5 essential pass AND composite >= 111/138 (~80%).

---

## Simplification Delta

| | Words | Score |
|-|-------|-------|
| V-05 (source) | 2,951 | 138/138 |
| Simplified (golden) | 1,819 | 130/138 |
| Removed | 1,132 (-38.4%) | -8 pts |

**Removed sections**: All 11 Inertia Gate blocks (C-31) and PRE-OUTPUT VERIFICATION PROTOCOL
table (C-14/C-19). Both are aspirational-only; zero essential criteria depend on either.
