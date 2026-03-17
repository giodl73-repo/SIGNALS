The R4 variations are written. Here's the summary:

---

## Variation Set R4 — scout-requirements

All 5 variations embed the full C-25/C-26/C-27 charter block from R3. R4 introduces new structural approaches targeting the two new criteria.

| Var | Axis | Predicted | Key mechanism |
|-----|------|-----------|---------------|
| **V-01** | Named per-loop absence sections | 132/132 | `#### Loop N Absence Clause` headers in charter make C-28 structurally unavoidable |
| **V-02** | Definitional register throughout | 132/132 | Every explanatory statement uses "X is not Y without Z" — C-29 constitutive, C-28 derived |
| **V-03** | Named inertia gates at each step | 132/132 | `**Inertia Gate (Step N)**` blocks distribute C-28 across all 10 steps + verification |
| **V-04** | V-01 + V-02 combined | 132/132 | Per-loop sections written in definitional voice — C-28 and C-29 mutually reinforcing |
| **V-05** | Full synthesis | 132/132 | All four axes: per-loop sections + definitional register + inertia gates + compliance-first |

**Three single-axis isolations**: V-01 probes whether structural section headers alone satisfy C-28 without pervasive C-29; V-02 probes whether register pervasion alone satisfies both; V-03 probes whether step-distributed inertia gates (rather than charter-level sections) satisfy C-28.

**Orthogonality probe**: If V-01 inadvertently passes C-29 and V-02 inadvertently passes C-28, the scorecard will confirm the criteria are less orthogonal than the rubric implies — useful signal for R5.

**Key structural innovation across R4**: V-03's `**Inertia Gate**` named blocks are a new delivery mechanism not present in R3. V-05 combines them with V-04's charter-level absence sections, creating dual-layer C-28 coverage (charter sections + step gates).
udes `"declaring format laws without an application layer is
  not enforcement — it is an incomplete declaration"`

**The two new patterns targeted in R4:**

- **C-28**: Each loop section in the charter carries its own per-loop absence clause naming what
  that loop cannot produce without its predecessor — distinct from the charter-level C-27 claim
- **C-29**: Definitional register ("X is not Y without Z") is the primary explanatory mode for
  loop relationships, MoSCoW anchoring, and design contract obligations throughout the document

**Single-axis discrimination**: V-01 realizes C-28 via structural section headers (dedicated
`#### Loop N Absence Clause` subsections in the charter). V-02 realizes C-29 via register
pervasion (all explanatory prose in definitional form). V-03 realizes C-28 at the extraction
step level via named `**Inertia Gate**` blocks, testing whether C-28 can be distributed across
steps rather than confined to the charter. The three single-axis variations probe whether C-28
and C-29 are independently achievable — a variation passing only one confirms they are orthogonal.

---

## V-01: Named Per-Loop Absence Sections

**Axis**: Charter structure — per-loop named subsections
**Hypothesis**: Adding explicit `#### Loop N Absence Clause` subsections after each loop in
the Three-Loop Meta-Requirement section makes C-28 a structural inevitability: the absence
clause for each loop is not distributed prose but a named section that cannot be omitted
without removing a visible structural element. C-29 inherits partially from the section
framing because the absence clause language uses definitional voice by construction ("Without
Loop N, Loop N+1 is not a [function] — it is [lesser category]"). The risk is that C-29
may not fully satisfy the "primary voice throughout" condition if the remainder of the
document reverts to requirement or necessity register. Standard PM-first extraction order,
prose output format, full 9-step structure.

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

#### Loop 1 Absence Clause

Without Loop 1 (this charter), Loop 2 has no format laws to apply. An extraction run that
begins without this charter is not an extraction run with enforcement — it is unstructured
requirements listing. The format laws do not exist until declared; declaring them is the
precondition for applying them. Without Loop 1, what exists is not a weakened enforcement
system — it is the absence of an enforcement frame altogether.

**Structural Closure**: Declaring format laws without an application layer is not enforcement —
it is an incomplete declaration. A charter that declares Law A and Law B (C-17) without requiring
inline reinstatement at each triggering step (C-18) has not created enforcement; the category
"enforcement" requires Loop 2 by definition. Without Loop 2, what exists is a statement of intent,
not enforcement. Asserting C-17 simultaneously instantiates C-18 (both Law A's C-18-A and Law B's
C-18-B) as necessary consequences: the act of declaring laws constitutes the obligation to apply
them at each triggering step. C-19 closes the loop by auditing that C-18's applications occurred.

#### Loop 2 Absence Clause

Without Loop 2 (step-level reinstatements), Loop 3 has no artifacts to audit. C-18-A's inline
[AMBIG:] notations are the evidence C-19-A requires; C-18-B's inline closure sentences are the
evidence C-19-B requires. A verification table that runs without C-18's artifacts is not a
verification pass — it is structural theater. Prevention without artifacts for detection to find
is not an enforcement system — it is a declaration that ran without producing checkable output.

#### Loop 3 Absence Clause

Without Loop 3 (this verification table), Loop 2's applications are asserted but unconfirmed.
Prevention without detection is not a complete enforcement mechanism — it is half an enforcement
mechanism. C-18's inline work may include violations that slipped through; without C-19's audit
table, those violations have no detection layer. Loop 3 is not an optional quality gate — it is
the condition that converts Loop 2's prevention claims into a verified process record.

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

## STEP 1: PM LENS

**Apply Law A here (Step 1)**: Flag ambiguities inline at first encounter using the two-path
format [AMBIG:] before assigning an AF- ID. Do not defer.

Extract user-facing requirements:
- User goals this concept must achieve → Must Have / Should Have
- Competitive capabilities → Should Have
- Delight features → Could Have
- Out-of-scope user needs → Won't Have
- User scenario gaps with no requirement coverage → SS- candidates

**Apply Law B here (Step 1)**: Write closure sentence inline for each scenario gap found.

Assign IDs: P-NN (PM). Flag blockers: "BLOCKS: [list of requirement IDs blocked]."

---

## STEP 2: ARCHITECT LENS

**Apply Law A here (Step 2)**: Flag ambiguities inline at first encounter.

Extract technical requirements against the PM baseline from Step 1:
- System properties required to satisfy PM requirements → Must/Should/Could
- Platform, data-contract, integration, and deployment constraints
- Technical silences: PM requirements with no architectural specification

**Apply Law B here (Step 2)**: Write closure sentence inline for each technical silence gap.

Assign IDs: A-NN (architect). Flag blockers.

---

## STEP 3: UX LENS

**Apply Law A here (Step 3)**: Flag ambiguities inline at first encounter.

Extract interaction requirements against the PM + Architect baseline:
- Interaction requirements → Must/Should/Could
- Error states and recovery flows
- First-run and onboarding experience
- UX silences: user journey phases with no interaction requirement

**Apply Law B here (Step 3)**: Write closure sentence inline for each UX gap found.

Assign IDs: U-NN (UX). Flag blockers.

---

## STEP 4: COMPLIANCE LENS

**Apply Law A here (Step 4)**: Flag ambiguities inline at first encounter.

Extract regulatory requirements:
- Legal or regulatory mandates → automatic MoSCoW Must (note the specific regulation/policy)
- Conditional compliance obligations → Should/Could
- Audit, reporting, and data-retention requirements implied by the concept
- Compliance silences: areas where the concept implies regulatory obligations without naming them

**Apply Law B here (Step 4)**: Write closure sentence inline for each compliance silence found.

Assign IDs: C-NN (compliance). Flag blockers. Where a compliance mandate conflicts with a
lower tier assigned in Steps 1-3, the mandate governs: promote and justify:
"Promoted R-NN from [tier] to Must: [regulation/mandate]."

---

## STEP 5: MOSCOW SYNTHESIS

Consolidate all requirements from Steps 1-4. Rules:
- Compliance mandates (Step 4) govern tier assignment — no PM or UX vote can demote them
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

Note: Observability/audit phase must be checked against compliance requirements from Step 4 —
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
| C-05 | Three+ lenses traceable | Are PM, Architect, and at least one of UX/Compliance traceable in the MoSCoW table? | PASS/FAIL |
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
| C-28 | Per-loop absence clauses | Does the charter contain named Loop 1, Loop 2, and Loop 3 Absence Clause subsections, each with a localized absence statement distinct from the C-27 global closure? | PASS/FAIL |
| C-29 | Definitional register as primary voice | Does the definitional register ("X is not Y without Z") appear as the primary explanatory mode in loop absence clauses and design contract language — not only in the C-27 closure? | PASS/FAIL |

If any FAIL in C-01..C-07, resolve before emitting. Aspirational FAILs noted but do not block.

---

Write artifact to: simulations/scout/requirements/{{topic}}-requirements-{{date}}.md
Frontmatter: skill: scout-requirements, topic: {{topic}}, date: {{date}},
             skill_version: 4.0, input: [source spec path]
```

---

## V-02: Definitional Register as Structural Imperative

**Axis**: Phrasing register — definitional voice as document-level structural mode
**Hypothesis**: Rewriting all explanatory prose in the definitional register ("X is not Y
without Z") makes C-29 a structural inevitability: removing the definitional framing would
require rewriting the document, not patching a single statement. The same register naturally
produces C-28 because per-loop absence clauses are the definitional form of "what each loop
is not without its predecessor." V-04 R3 demonstrated this for compliance-first structure;
V-02 R4 tests whether definitional register alone (without compliance-first ordering) is
sufficient to pass both C-28 and C-29 — isolating register from role-sequence effects.
Standard PM-first extraction order, prose output.

---

```
You are running /scout-requirements for: {{topic}}

---

## CHARTER — FORMAT LAWS AND THREE-LOOP META-REQUIREMENT

This charter constitutes Loop 1 (C-17 / declare) of the three-loop meta-requirement.
A requirements run is not a governed requirements run without this charter — it is
unstructured extraction without enforcement scope.

### Format Law A: Two-Path AF- Rule

An ambiguity flag is not a Law A compliant entry without two named interpretation paths and
their consequences. Every ambiguity encountered during extraction therefore carries an inline
notation at first encounter:

  [AMBIG: "{exact source text}" → A: {interpretation A} | B: {interpretation B}]

An AF- section that introduces ambiguities for the first time is not a Law A compliant section —
it is a deferred-work section. Law A compliance requires inline notation at first encounter;
the AF- section is not a work-creation step.

### Format Law B: Downstream Closure Rule

A downstream findings section (AF-, SF-) is not a closed section without the following explicit
closure statement:

  "Every entry from the prior open [AF- / SF-] register appears in this section
   with a status: open / resolved / out-of-scope."

A section that contains prior entries without this statement is not a closed section — it is
an enumeration. The closure statement is not a summary; it is the condition that converts an
enumeration into a compliant findings closure.

### Law A Independent Enforcement Chain

- **C-17-A (Loop 1-A / declare)**: Law A declared here, independently of Law B.
  Law A's enforcement chain is not weakened by a failure in Law B's chain — they are independent.
- **C-18-A (Loop 2-A / apply)**: An extraction step that encounters an ambiguity is not compliant
  without a full-text reinstatement — "Apply Law A here" — followed immediately by both
  interpretation paths inline. A step that logs the AF- ID without writing both paths inline
  is not a Law A compliant step.
- **C-19-A (Loop 3-A / verify)**: A verification row is not a C-19-A compliant row without
  auditing whether dual-interpretation [AMBIG:] notations appeared at each applicable extraction
  step — auditing whether the AF- summary section exists is not a C-19-A audit.

### Law B Independent Enforcement Chain

- **C-17-B (Loop 1-B / declare)**: Law B declared here, independently of Law A.
  Law B's enforcement chain is not weakened by a failure in Law A's chain.
- **C-18-B (Loop 2-B / apply)**: A downstream findings section is not Law B compliant without
  a full-text reinstatement — "Apply Law B here" — followed immediately by the closure sentence
  inline before the section closes.
- **C-19-B (Loop 3-B / verify)**: A verification row is not a C-19-B compliant row without
  auditing whether closure sentences appeared in each downstream section — auditing whether
  prior entries appear anywhere is not a C-19-B audit.

### Three-Loop Meta-Requirement: Structural Closure

The two law chains unify under one self-closing declaration:

- **C-17 (Loop 1 / declare)** = this charter, including both Law A and Law B independent chains
- **C-18 (Loop 2 / apply)** = the step-level cross-references from both chains, applied per law
- **C-19 (Loop 3 / verify)** = the pre-output verification protocol table

Loop 1 without Loop 2 is not an enforcement system — it is a statement of intent. Without
Loop 2, the format laws exist as declarations but have no application layer; a declaration
without an application layer is not enforcement by definition. Declaring format laws without
an application layer is not enforcement — it is an incomplete declaration. A charter that
declares Law A and Law B (C-17) without requiring inline reinstatement at each triggering step
(C-18) has not created enforcement; the category "enforcement" requires Loop 2 by definition.
Without Loop 2, what exists is a statement of intent, not enforcement. Asserting C-17
simultaneously instantiates C-18 (both Law A's C-18-A and Law B's C-18-B) as necessary
consequences: the act of declaring laws constitutes the obligation to apply them at each
triggering step.

Loop 2 without Loop 3 is not a verified process — it is an unaudited one. C-18's applications
may include violations that passed the inline enforcement gate; without C-19's audit table,
those violations have no detection layer. A process with prevention but no detection is not a
governed process — it is a process of declared intent without confirmation. C-19 closes the
loop by auditing that C-18's applications occurred.

### Loop 2 → Loop 3 Design Contract

This charter names the following as a structural obligation before extraction begins, chartered
here as a design contract and not inferred from structural proximity:

**C-18 (Loop 2) creates the execution artifacts that C-19 (Loop 3) requires as evidence.**

C-19 without C-18's artifacts is not a verification pass — it is structural theater. Per law:
- **Law A's C-18-A** creates inline [AMBIG:] notations at each ambiguity step, each carrying
  Interpretation A and Interpretation B. A C-19-A audit row is not a compliant row without
  checking whether these dual-path notations are present at each applicable step — checking
  whether the AF- section exists is not a C-19-A audit.
- **Law B's C-18-B** creates inline closure sentences in each downstream findings section.
  A C-19-B audit row is not a compliant row without checking whether closure sentences are
  present and correctly formed at each applicable section — checking whether prior entries
  are listed is not a C-19-B audit.

C-18 is not an optional loop — it is the prevention layer that makes C-19's detection possible.
A process with C-19 but no C-18 is not a weaker enforcement system — it is a system verifying
the absence of artifacts it never created.

---

## STEP 0: DUAL-DIRECTORY SEARCH

Search for prior scout signals in BOTH:
- simulations/scout/ — real runs for {{topic}}
- simulations/trace/skill/ — hand-compiled traces for {{topic}}

A search that does not state explicit results from both directories is not a compliant
dual-directory search — it is a partial search regardless of what was found.

**Apply Law B here (Step 0)**: List all open AF- and SF- entries from prior runs.
State the closure sentence:
  "Every entry from the prior open findings register appears in this step with a status:
   open / resolved / out-of-scope."

SF-01 (undefined search path): CLOSED if trace found in simulations/trace/skill/; else OPEN.

---

## STEP 1: PM LENS

**Apply Law A here (Step 1)**: Write [AMBIG:] inline at first encounter. A step that defers
ambiguity notation to Step 8 is not a Law A compliant step.

A PM requirement without a user goal it satisfies is not a signal-quality requirement — it is
a feature wish. Extract:
- User goals this concept must achieve → Must Have / Should Have
- Competitive capabilities that the concept cannot claim without this feature → Should Have
- Delight features that improve the experience but do not define it → Could Have
- User needs the concept explicitly excludes → Won't Have
- User journey phases where no requirement provides coverage → SS- candidates

A MoSCoW tier assignment without a lens-traceable rationale is not a stable tier assignment —
it is an opinion that will not survive cross-role synthesis.

**Apply Law B here (Step 1)**: Write closure sentence inline for each scenario gap found.

Assign IDs: P-NN (PM). Flag blockers: "BLOCKS: [list of requirement IDs blocked]."

---

## STEP 2: ARCHITECT LENS

**Apply Law A here (Step 2)**: Write [AMBIG:] inline at first encounter.

A technical requirement that is not traceable to a PM or compliance parent is not a
requirements-signal artifact — it is an architectural preference. Extract:
- System properties required to satisfy PM requirements → Must/Should/Could (inherit tier from parent)
- Platform, data-contract, integration, and deployment constraints
- Technical silences: PM requirements with no architectural coverage are not PM risks — they are
  blocking gaps that prevent PM requirements from being buildable

**Apply Law B here (Step 2)**: Write closure sentence inline for each technical silence.

Assign IDs: A-NN (architect). Flag blockers.

---

## STEP 3: UX LENS

**Apply Law A here (Step 3)**: Write [AMBIG:] inline at first encounter.

A UX requirement that a user journey phase cannot complete without is not a Could Have —
it is a Must Have by the flow-completion definition. Extract:
- Interaction requirements → Must/Should/Could
- Error states and recovery flows: a feature without an error state is not a complete feature —
  it is a happy-path stub
- First-run and onboarding experience
- UX silences: journey phases with no interaction coverage

**Apply Law B here (Step 3)**: Write closure sentence inline for each UX gap.

Assign IDs: U-NN (UX). Flag blockers.

---

## STEP 4: COMPLIANCE LENS

**Apply Law A here (Step 4)**: Write [AMBIG:] inline at first encounter.

A compliance obligation is not a negotiable tier — it is non-negotiable by the definition of
regulatory mandate. Extract:
- Legal or regulatory mandates → automatic Must Have (the regulation is the justification)
- Conditional compliance obligations (jurisdiction-dependent) → Should/Could
- Audit, reporting, and data-retention requirements implied by the concept's scope
- Compliance silences: a concept operating in a regulated space without named compliance
  requirements is not a clean concept — it is a concept with undetected obligations

**Apply Law B here (Step 4)**: Write closure sentence inline for each compliance silence found.

Assign IDs: C-NN (compliance). Flag blockers. Compliance-sourced tier promotions override
prior lens assignments: "Promoted R-NN from [tier] to Must: [regulation/mandate]."

---

## STEP 5: MOSCOW SYNTHESIS

A MoSCoW table without four named tiers is not a MoSCoW table — it is a flat requirements
list. Consolidate all requirements from Steps 1-4. Rules:
- Compliance mandates (Step 4) are not subject to negotiation — they govern tier assignment
- A requirement blocking a Must-tier item is not optional — it is Must by blocking dependency
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

A root blocker is not a root blocker without a chain of dependent Must-tier items that cannot
exist without it. Name at least one root blocker. State WHY it is foundational — not merely
which IDs it blocks. Show second-order chains: R-NN → R-MM → R-PP with reasoning at each link.
Compliance requirements that are foundational are not optional root blockers — they are mandatory
roots whose absence makes the entire dependent chain non-buildable.

---

## STEP 7: LIFECYCLE PHASE COVERAGE AUDIT

**Apply Law A here (Step 7)**: Write [AMBIG:] inline for any ambiguous coverage boundary.

A lifecycle phase that has no requirements coverage is not a gap to note — it is a silent
specification zone that will produce unplanned work at implementation time.

| Phase | Coverage | SS- entry |
|-------|----------|-----------|
| First-run / onboarding | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Core-use / steady-state | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Upgrade / migration | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Error / recovery | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Observability / audit | COVERED / PARTIAL / SILENT | [SS-NN or —] |

Note: An observability/audit phase that shows COVERED without compliance cross-check from
Step 4 is not a verified COVERED — it is an unchecked assumption.

---

## STEP 8: AMBIGUITY FLAGS

**Apply Law A here (Step 8)**: This section formalizes all [AMBIG:] notations from Steps 1-7.
An AF- section that introduces new ambiguities here is not a Law A compliant section.

**Apply Law B here (Step 8)**: Every entry from the prior open AF- register must appear below.
State the closure sentence:
  "Every entry from the prior open AF- register appears in this section with a status:
   open / resolved / out-of-scope."

**AF-NN: [requirement ID or spec phrase]**
- Source: "[exact quote from input]" — an AF- without an exact source quote is not a documented
  ambiguity; it is an undocumented one
- Interpretation A: [what team A would build]
- Interpretation B: [what team B would build]
- Consequence: [how the product diverges between A and B — an ambiguity without a stated
  consequence is not a decision-forcing ambiguity]
- Status: open / resolved / out-of-scope

[Zero AF- on a complex input is not a clean result — it is a missed extraction.]

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

[Zero SF- on a non-trivial input is not a clean spec — it is an underscrutinized one.]

Closure: Every entry from the prior open SF- register appears in this section with a status. ✓

---

## PRE-OUTPUT VERIFICATION PROTOCOL (C-19 / Loop 3 — verify)

A verification protocol that does not check process compliance is not a C-19 compliant table —
it is a section-presence audit. This table checks whether laws were applied during extraction.

| ID | Criterion | Process check | Status |
|----|-----------|--------------|--------|
| C-01 | Dual-directory search | Did Step 0 state results from both simulations/scout/ AND simulations/trace/skill/? | PASS/FAIL |
| C-02 | MoSCoW structure | Does Step 5 have four named tiers (not a flat list)? | PASS/FAIL |
| C-03 | Root blocker named | Does Step 6 name a root blocker with blocked IDs and foundational reasoning? | PASS/FAIL |
| C-04 | Ambiguity flags raised | Does Step 8 have at least one AF- entry? | PASS/FAIL |
| C-05 | Three+ lenses traceable | Are PM, Architect, and at least one of UX/Compliance traceable in the MoSCoW table? | PASS/FAIL |
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
| C-28 | Per-loop absence clauses | Does the definitional register naturally produce per-loop absence statements — Loop 1 ("without Loop 1, Loop 2 is not enforcement application"), Loop 2 ("without Loop 2, Loop 3 is not a verification"), Loop 3 ("without Loop 3, Loop 2 is not confirmed") — distinct from the C-27 global closure? | PASS/FAIL |
| C-29 | Definitional register as primary voice | Is the definitional register ("X is not Y without Z") pervasive throughout — in loop relationships, MoSCoW anchoring, design contract obligations, and step explanations — such that removing it would require rewriting most of the document? | PASS/FAIL |

If any FAIL in C-01..C-07, resolve before emitting. Aspirational FAILs noted but do not block.

---

Write artifact to: simulations/scout/requirements/{{topic}}-requirements-{{date}}.md
Frontmatter: skill: scout-requirements, topic: {{topic}}, date: {{date}},
             skill_version: 4.0, input: [source spec path]
```

---

## V-03: Named Inertia Gates at Each Extraction Step

**Axis**: Step structure — named `**Inertia Gate (Step N)**` block at each step's opening
**Hypothesis**: Distributing C-28's per-loop absence logic beyond the charter and into each
extraction step creates a second realization point for the per-loop claim. V-05 R3 embedded
inertia framing as inline prose; V-03 R4 elevates it to a named structural gate — a dedicated
`**Inertia Gate (Step N)**` block at each step's opening. Named gates cannot be silently
dropped; they are visible structural elements. C-29 inherits from the density of definitional
framing across the gate network — when every step opens with a definitional absence claim,
the register is pervasive by construction. Standard PM-first order; charter from R3 baseline
without V-01's named per-loop sections (isolating the axis).

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

**Inertia Gate (Step 0)**: Without this search, the extraction run has no continuity signal
from prior work. A requirements run that begins without checking prior sessions is not a
sessions-aware extraction — it is a from-scratch extraction that will independently rediscover
known ambiguities and reopen closed findings. The cost of skipping Step 0 is not one missed
lookup; it is the loss of every prior AF- and SF- entry the current run must rediscover.

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

## STEP 1: PM LENS

**Inertia Gate (Step 1)**: Without this step, the extraction has no user-facing requirements.
A requirements signal that lacks PM-lens output is not a product requirements signal — it is a
technical or regulatory specification without a product narrative. Architect and Compliance
requirements extracted without a PM lens have no user-goal rationale; they cannot be prioritized
against user value, only against internal constraints.

**Apply Law A here (Step 1)**: Flag ambiguities inline at first encounter using [AMBIG:] format.
Do not defer.

Extract user-facing requirements:
- User goals this concept must achieve → Must Have / Should Have
- Competitive capabilities → Should Have
- Delight features → Could Have
- Out-of-scope user needs → Won't Have
- User scenario gaps with no requirement coverage → SS- candidates

**Apply Law B here (Step 1)**: Write closure sentence inline for each scenario gap found.

Assign IDs: P-NN (PM). Flag blockers: "BLOCKS: [list of requirement IDs blocked]."

---

## STEP 2: ARCHITECT LENS

**Inertia Gate (Step 2)**: Without this step, the extraction has no buildability signal. A
requirements set that lacks Architect-lens output is not a buildable specification — it is a
product wishlist without system constraints. PM requirements without architectural coverage
cannot be assigned reliable complexity estimates; technical silences found here are not minor
gaps — they are blockers to the PM requirements that depend on them.

**Apply Law A here (Step 2)**: Flag ambiguities inline at first encounter.

Extract technical requirements:
- System properties required to satisfy PM requirements → Must/Should/Could
- Platform, data-contract, integration, and deployment constraints
- Technical silences: PM requirements with no architectural specification

**Apply Law B here (Step 2)**: Write closure sentence inline for each technical silence gap.

Assign IDs: A-NN (architect). Flag blockers.

---

## STEP 3: UX LENS

**Inertia Gate (Step 3)**: Without this step, the extraction has no interaction signal. A
requirements set that lacks UX-lens output is not a user-interaction specification — it is a
functional spec without flow coverage. Error states have no requirements backing; teams design
them ad hoc, producing implementation divergence. Accessibility requirements mandated by
compliance have no UX articulation and cannot be evaluated against interaction design.

**Apply Law A here (Step 3)**: Flag ambiguities inline at first encounter.

Extract interaction requirements:
- Interaction requirements → Must/Should/Could
- Error states and recovery flows
- First-run and onboarding experience
- UX silences: user journey phases with no interaction coverage

**Apply Law B here (Step 3)**: Write closure sentence inline for each UX gap.

Assign IDs: U-NN (UX). Flag blockers.

---

## STEP 4: COMPLIANCE LENS

**Inertia Gate (Step 4)**: Without this step, the extraction has no regulatory boundary. A
requirements set without Compliance-lens output is not a regulated-product specification — it
is a specification that will encounter compliance obligations at implementation or launch.
Compliance silences found here are not audit findings — they are unrecognized Must-tier
requirements currently unclassified.

**Apply Law A here (Step 4)**: Flag ambiguities inline at first encounter.

Extract regulatory requirements:
- Legal or regulatory mandates → automatic Must Have (note the specific regulation/policy)
- Conditional compliance obligations → Should/Could
- Audit, reporting, and data-retention requirements implied by the concept
- Compliance silences → SS- candidates

**Apply Law B here (Step 4)**: Write closure sentence inline for each compliance silence found.

Assign IDs: C-NN (compliance). Flag blockers. Compliance mandate tier promotions override
prior lens assignments: "Promoted R-NN from [tier] to Must: [regulation/mandate]."

---

## STEP 5: MOSCOW SYNTHESIS

**Inertia Gate (Step 5)**: Without this step, the extracted requirements have no unified tier
structure. Four lenses running in parallel produce four unreconciled priority views; without
synthesis, there is no single MoSCoW signal. A requirements set without four named tiers is
not a MoSCoW-structured set — it is a requirements list with informal prioritization.

Consolidate all requirements from Steps 1-4. Rules:
- Compliance mandates (Step 4) govern tier assignment — no PM or UX vote can demote them
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

**Inertia Gate (Step 6)**: Without this step, the MoSCoW table has no execution order signal.
A flat list of Must-tier requirements without dependency chains is not a buildable roadmap —
it is a set of obligations without sequencing. A dependency chain that does not name a root
blocker is not a dependency chain — it is a list of related items.

Name at least one root blocker. State WHY it is foundational — not just which IDs it blocks.
Show second-order chains: R-NN → R-MM → R-PP with reasoning at each link.

---

## STEP 7: LIFECYCLE PHASE COVERAGE AUDIT

**Inertia Gate (Step 7)**: Without this step, the requirements have no lifecycle completeness
signal. A requirements set that covers core-use without first-run, upgrade, or error-recovery
coverage is not a lifecycle-complete specification — it is a steady-state specification with
undetected gaps. Compliance audit requirements frequently appear only at the observability/audit
phase; without this step, they have no phase-coverage verification.

**Apply Law A here (Step 7)**: Write [AMBIG:] inline for any ambiguous coverage boundary.

| Phase | Coverage | SS- entry |
|-------|----------|-----------|
| First-run / onboarding | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Core-use / steady-state | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Upgrade / migration | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Error / recovery | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Observability / audit | COVERED / PARTIAL / SILENT | [SS-NN or —] |

---

## STEP 8: AMBIGUITY FLAGS

**Inertia Gate (Step 8)**: Without this step, the inline [AMBIG:] notations from Steps 1-7
have no formal register. A set of inline notations without a formalized AF- section is not a
documented ambiguity record — it is distributed notes that cannot be tracked across sessions.

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

[Zero AF- on a complex input is a fail.]

Closure: Every entry from the prior open AF- register appears in this section with a status. ✓

---

## STEP 9: SPEC-FAULT FINDINGS

**Inertia Gate (Step 9)**: Without this step, spec gaps found during extraction have no
severity triage. SF- candidates are unclassified findings; without this step, blocking P0 gaps
are indistinguishable from minor P2 notes and cannot drive pre-commitment resolution decisions.

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

**Inertia Gate (Verification)**: Without this table, the extraction has no process compliance
record. An output without a completed verification table is not a governed requirements signal —
it is an ungoverned requirements list. Law A and Law B applications during Steps 1-9 are
prevention assertions; without this table's detection audit, violations have no detection layer.

Before emitting the final artifact, verify each criterion by ID.

| ID | Criterion | Process check | Status |
|----|-----------|--------------|--------|
| C-01 | Dual-directory search | Did Step 0 state results from both simulations/scout/ AND simulations/trace/skill/? | PASS/FAIL |
| C-02 | MoSCoW structure | Does Step 5 have four named tiers (not a flat list)? | PASS/FAIL |
| C-03 | Root blocker named | Does Step 6 name a root blocker with blocked IDs and foundational reasoning? | PASS/FAIL |
| C-04 | Ambiguity flags raised | Does Step 8 have at least one AF- entry? | PASS/FAIL |
| C-05 | Three+ lenses traceable | Are PM, Architect, and at least one of UX/Compliance traceable in the MoSCoW table? | PASS/FAIL |
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
| C-26 | Per-law sub-IDs in unified closure statement | Does the structural closure name "C-18 (both Law A's C-18-A and Law B's C-18-B)" by sub-ID? | PASS/FAIL |
| C-27 | Definitional non-enforcement framing | Does the structural closure include "declaring X without Y is not enforcement — it is an incomplete declaration"? | PASS/FAIL |
| C-28 | Per-loop absence clauses | Does each Inertia Gate block at Steps 0-9 and the Verification gate carry a per-step absence clause stating what the extraction cannot produce without that step — with the charter (Loop 1), extraction steps (Loop 2), and verification (Loop 3) each naming their own absence consequence? | PASS/FAIL |
| C-29 | Definitional register as primary voice | Do the Inertia Gate blocks use definitional register ("X is not Y without Z") as their primary explanatory mode throughout, making it the structural voice of the document? | PASS/FAIL |

If any FAIL in C-01..C-07, resolve before emitting. Aspirational FAILs noted but do not block.

---

Write artifact to: simulations/scout/requirements/{{topic}}-requirements-{{date}}.md
Frontmatter: skill: scout-requirements, topic: {{topic}}, date: {{date}},
             skill_version: 4.0, input: [source spec path]
```

---

## V-04: Per-Loop Sections + Definitional Register (Combined)

**Axis**: V-01 + V-02 combined — named per-loop absence sections AND definitional register
as structural voice throughout
**Hypothesis**: V-01 establishes C-28 through named structural section headers in the charter.
V-02 establishes C-29 through register pervasion. In combination, each named per-loop absence
section is written in definitional voice, making C-28 and C-29 mutually reinforcing: the
absence clause headers are the structural delivery mechanism for the definitional claims, and
the definitional register makes each absence clause a categorical statement rather than a
process warning. This combination should independently satisfy C-28 and C-29 without either
needing the other to reinforce it. Compliance-first role order (R3 V-01/V-04), which proved
compatible with the full charter machinery.

---

```
You are running /scout-requirements for: {{topic}}

---

## CHARTER — FORMAT LAWS AND THREE-LOOP META-REQUIREMENT

This charter constitutes Loop 1 (C-17 / declare) of the three-loop meta-requirement.
A requirements run is not a governed requirements run without this charter — it is unstructured
extraction. The charter is not documentation — it is the precondition for Loop 2's existence.

### Format Law A: Two-Path AF- Rule

An ambiguity flag is not a Law A compliant entry without two named interpretation paths and
their consequence. Every ambiguity encountered during extraction carries an inline notation
at first encounter:

  [AMBIG: "{exact source text}" → A: {interpretation A} | B: {interpretation B}]

An AF- section that introduces ambiguities without prior inline notations is not a Law A
compliant section — it is a deferred-work section. Law A compliance requires inline notation
at first encounter; the AF- section is not a work-creation step.

### Format Law B: Downstream Closure Rule

A downstream findings section (AF-, SF-) is not a closed section without the explicit closure
statement:

  "Every entry from the prior open [AF- / SF-] register appears in this section
   with a status: open / resolved / out-of-scope."

A section containing prior entries without this statement is not a closed findings section —
it is an enumeration. The closure statement is the condition that converts enumeration into
Law B compliance.

### Law A Independent Enforcement Chain

- **C-17-A (Loop 1-A / declare)**: Law A declared here, independently of Law B.
  A failure in Law A's chain is not a failure of Law B's chain.
- **C-18-A (Loop 2-A / apply)**: A triggered step is not Law A compliant without "Apply Law A
  here" followed immediately by both interpretation paths inline. A step that logs the AF- ID
  without writing both paths is not a Law A compliant step.
- **C-19-A (Loop 3-A / verify)**: A verification row is not C-19-A compliant without auditing
  whether dual-interpretation [AMBIG:] notations appeared at each applicable extraction step —
  auditing whether the AF- section exists is not a C-19-A audit.

### Law B Independent Enforcement Chain

- **C-17-B (Loop 1-B / declare)**: Law B declared here, independently of Law A.
  A failure in Law B's chain is not a failure of Law A's chain.
- **C-18-B (Loop 2-B / apply)**: A downstream findings section is not Law B compliant without
  "Apply Law B here" followed immediately by the closure sentence inline.
- **C-19-B (Loop 3-B / verify)**: A verification row is not C-19-B compliant without auditing
  whether closure sentences appeared in each downstream section — auditing whether prior entries
  appear anywhere is not a C-19-B audit.

### Three-Loop Meta-Requirement: Structural Closure

The two law chains unify under one self-closing declaration:

- **C-17 (Loop 1 / declare)** = this charter, including both Law A and Law B independent chains
- **C-18 (Loop 2 / apply)** = the step-level cross-references from both chains, applied per law
- **C-19 (Loop 3 / verify)** = the pre-output verification protocol table

#### Loop 1 Absence Clause

A requirements run that begins without this charter is not a requirements run with format
enforcement — it is unstructured extraction. Without Loop 1, format laws do not exist; without
format laws, Loop 2's reinstatements have no laws to reinstate. Loop 1 is not merely prior to
Loop 2 — it is the definitional precondition for Loop 2's category membership as "enforcement
application." An extraction that skips Loop 1 has not weakened its enforcement — it has removed
the frame in which enforcement is definable.

**Structural Closure**: Declaring format laws without an application layer is not enforcement —
it is an incomplete declaration. A charter that declares Law A and Law B (C-17) without requiring
inline reinstatement at each triggering step (C-18) has not created enforcement; the category
"enforcement" requires Loop 2 by definition. Without Loop 2, what exists is a statement of
intent, not enforcement. Asserting C-17 simultaneously instantiates C-18 (both Law A's C-18-A
and Law B's C-18-B) as necessary consequences: the act of declaring laws constitutes the
obligation to apply them at each triggering step. C-19 closes the loop by auditing that C-18's
applications occurred.

#### Loop 2 Absence Clause

A charter that declares format laws without Loop 2's step-level application is not an
enforcement charter — it is a charter without an execution layer. Without Loop 2 (C-18's
inline reinstatements), Loop 3 has no artifacts to audit: C-18-A's [AMBIG:] notations are
the evidence C-19-A requires; C-18-B's closure sentences are the evidence C-19-B requires.
A Loop 3 verification table that runs without C-18's artifacts is not a verification pass —
it is structural theater. Loop 2 is not the middle step of three — it is the artifact-creation
layer without which Loop 3 cannot execute its detection function.

#### Loop 3 Absence Clause

An extraction that applies format laws at each step without auditing that application is not
a governed extraction — it is an asserted-compliant extraction. Without Loop 3 (C-19's
verification table), Loop 2's applications are prevention claims without confirmation;
violations that passed C-18's inline enforcement have no detection layer. A process with
prevention but no detection is not a complete enforcement mechanism — it is a half-mechanism
that produces outputs indistinguishable from a non-compliant process when C-18 fails silently.
Loop 3 is not a final quality check — it is the verification condition that makes the
prevention-detection system definitionally complete.

### Loop 2 → Loop 3 Design Contract

This charter names the following as a constitutive structural obligation before extraction
begins, chartered here as a design contract and not inferred from structural proximity:

**C-18 (Loop 2) creates the execution artifacts that C-19 (Loop 3) requires as evidence.**

C-19 without C-18's artifacts is not a verification pass — it is a verification of nothing.
Per law:
- **Law A's C-18-A** creates inline [AMBIG:] notations at each ambiguity step, each carrying
  Interpretation A and Interpretation B. A C-19-A audit row is not compliant without checking
  whether these dual-path notations are present at each applicable step — a row that checks
  only whether the AF- section exists is not a C-19-A process audit.
- **Law B's C-18-B** creates inline closure sentences in each downstream findings section.
  A C-19-B audit row is not compliant without checking whether closure sentences are present
  and correctly formed at each applicable section — a row that checks only whether prior entries
  appear is not a C-19-B process audit.

C-18 constitutes prevention. C-19 constitutes detection. A system with detection but no
prevention is not a weaker enforcement system — it is a detection system verifying the absence
of artifacts it never created.

---

## STEP 0: DUAL-DIRECTORY SEARCH

Search for prior scout signals in BOTH:
- simulations/scout/ — real runs for {{topic}}
- simulations/trace/skill/ — hand-compiled traces for {{topic}}

A search that does not state explicit results from both directories is not a compliant
dual-directory search — it is a partial search regardless of what was found.

**Apply Law B here (Step 0)**: List all open AF- and SF- entries from prior runs.
State the closure sentence:
  "Every entry from the prior open findings register appears in this step with a status:
   open / resolved / out-of-scope."

SF-01 (undefined search path): CLOSED if trace found in simulations/trace/skill/; else OPEN.

---

## STEP 1: COMPLIANCE LENS (constitutes the non-negotiable tier foundation)

**Apply Law A here (Step 1)**: Write [AMBIG:] inline at first encounter. A step that defers
ambiguity notation is not a Law A compliant step.

Compliance requirements are not negotiable tier assignments — they are Must Have by regulatory
category. A requirements process that does not begin with compliance is not a compliant
requirements process; it is a process that may discover mandatory requirements after PM and UX
preferences have been set. Extract:
- Legal or regulatory mandates → Must Have (the mandate is the justification — a Must assigned
  for compliance is not subject to PM demotion)
- Conditional compliance obligations (jurisdiction-scoped) → Should/Could
- Audit, reporting, and data-retention requirements implied by the concept
- Compliance silences: a feature operating in a regulated space without named compliance
  requirements is not a clean feature — it is a feature with undetected obligations

**Apply Law B here (Step 1)**: Write closure sentence inline for each compliance silence found.

Assign IDs: C-NN (compliance). Flag blockers: "BLOCKS: [list of requirement IDs blocked]."

---

## STEP 2: PM LENS (constrained by compliance foundation)

**Apply Law A here (Step 2)**: Write [AMBIG:] inline at first encounter.

A PM requirement that conflicts with a Step 1 compliance mandate is not a legitimate Should
or Could candidate — it is a constraint violation. PM requirements exist within the space
compliance has left unspecified. Extract:
- User goals → Must Have (if compliance-anchored) or Should Have
- Competitive capabilities → Should Have
- Delight features → Could Have
- Explicit user exclusions → Won't Have
- User scenario gaps → SS- candidates

**Apply Law B here (Step 2)**: Write closure sentence inline for each scenario gap found.

Assign IDs: P-NN (PM). Flag blockers.

---

## STEP 3: ARCHITECT LENS (constrained by compliance + PM)

**Apply Law A here (Step 3)**: Write [AMBIG:] inline at first encounter.

A technical requirement that enables a compliance mandate inherits Must status by structural
entailment — it is not a negotiable architectural preference. A PM requirement without
architectural coverage is not a buildable requirement; it is a requirements-signal gap. Extract:
- System properties enabling compliance mandates → Must (inherit tier from mandate)
- System properties enabling PM requirements → Must/Should/Could
- Platform, data-contract, integration, and deployment constraints
- Technical silences: compliance or PM requirements with no architectural specification

**Apply Law B here (Step 3)**: Write closure sentence inline for each technical silence.

Assign IDs: A-NN (architect). Flag blockers.

---

## STEP 4: UX LENS (constrained by compliance + PM + architect)

**Apply Law A here (Step 4)**: Write [AMBIG:] inline at first encounter.

An accessibility requirement mandated by compliance is not a UX Could Have — it is Must Have
by compliance category. UX negotiation applies only within the space compliance has left
unspecified. Extract:
- Interaction requirements → Must/Should/Could
- Error states and recovery flows: a feature without an error state is not a complete feature
- First-run and onboarding experience
- Accessibility (compliance-anchored = Must by category)
- UX silences: user journey phases with no interaction requirement → SS- candidates

**Apply Law B here (Step 4)**: Write closure sentence inline for each UX gap.

Assign IDs: U-NN (UX). Flag blockers.

---

## STEP 5: MOSCOW SYNTHESIS

A MoSCoW table without four named tiers is not a MoSCoW table — it is a flat prioritization
list. Consolidate all requirements from Steps 1-4. Rules:
- Compliance mandates are not subject to tier negotiation — they constitute immovable Must items
- A requirement blocking a Must-tier item is not optional — it is Must by blocking dependency
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

A root blocker is not a root blocker without a chain of dependent Must-tier items that cannot
exist without it. Name at least one root blocker. State what category it constitutes and why
it blocks. Show second-order chains: R-NN → R-MM → R-PP with reasoning at each link.

---

## STEP 7: LIFECYCLE PHASE COVERAGE AUDIT

**Apply Law A here (Step 7)**: Write [AMBIG:] inline for any ambiguous coverage boundary.

A lifecycle phase with no requirements coverage is not a minor gap — it is a silent
specification zone that will produce unplanned work at implementation time.

| Phase | Coverage | SS- entry |
|-------|----------|-----------|
| First-run / onboarding | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Core-use / steady-state | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Upgrade / migration | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Error / recovery | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Observability / audit | COVERED / PARTIAL / SILENT | [SS-NN or —] |

Note: An observability/audit phase marked COVERED without compliance cross-check from Step 1
is not a verified COVERED — it is an unchecked assumption.

---

## STEP 8: AMBIGUITY FLAGS

**Apply Law A here (Step 8)**: This section formalizes all [AMBIG:] notations from Steps 1-7.
An AF- section that introduces new ambiguities here is not a Law A compliant section.

**Apply Law B here (Step 8)**: Every entry from the prior open AF- register must appear below.
State the closure sentence:
  "Every entry from the prior open AF- register appears in this section with a status:
   open / resolved / out-of-scope."

**AF-NN: [requirement ID or spec phrase]**
- Source: "[exact quote from input]" — an AF- without an exact source quote is not a documented
  ambiguity; it is an undocumented claim
- Interpretation A: [what team A would build]
- Interpretation B: [what team B would build]
- Consequence: [how the product diverges between A and B]
- Status: open / resolved / out-of-scope

[Zero AF- on a complex input is not a clean result — it is an under-extracted one.]

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

[Zero SF- on a non-trivial input is not a clean spec — it is an underscrutinized one.]

Closure: Every entry from the prior open SF- register appears in this section with a status. ✓

---

## PRE-OUTPUT VERIFICATION PROTOCOL (C-19 / Loop 3 — verify)

A verification table that checks only section presence is not a process compliance audit —
it is a structural inventory. This table checks whether format laws were applied during
extraction, not only whether expected sections exist.

| ID | Criterion | Process check | Status |
|----|-----------|--------------|--------|
| C-01 | Dual-directory search | Did Step 0 state results from both simulations/scout/ AND simulations/trace/skill/? | PASS/FAIL |
| C-02 | MoSCoW structure | Does Step 5 have four named tiers (not a flat list)? | PASS/FAIL |
| C-03 | Root blocker named | Does Step 6 name a root blocker with blocked IDs and foundational reasoning? | PASS/FAIL |
| C-04 | Ambiguity flags raised | Does Step 8 have at least one AF- entry? | PASS/FAIL |
| C-05 | Three+ lenses traceable | Are Compliance, PM, and Architect each traceable in the MoSCoW table? | PASS/FAIL |
| C-06 | Suspicious silences | Does Step 7 include at least one SS- entry? | PASS/FAIL |
| C-07 | SF- findings raised | Does Step 9 include at least one SF- entry? | PASS/FAIL |
| C-08 | Stable IDs + promotions | No ID collisions; tier promotions justified? | PASS/FAIL |
| C-09 | Transitive dependency graph | Does Step 6 show second-order chains (A→B→C) with reasoning? | PASS/FAIL |
| C-10 | AF- cites source text | Does each AF- entry include an exact quote? | PASS/FAIL |
| C-11 | Lifecycle phase audit | Does Step 7 name all five phases with coverage status? | PASS/FAIL |
| C-12 | Cross-session continuity | Do Steps 8 and 9 carry prior entries with explicit status? | PASS/FAIL |
| C-13 | Two-interpretation AF- format | Does each AF- have Interpretation A + B + Consequence? | PASS/FAIL |
| C-14 | Rubric self-check gate | Is this table present before the final artifact? | PASS/FAIL |
| C-15 (Law A) | Law A applied at extraction | Were [AMBIG:] notations generated DURING Steps 1-7, not introduced fresh in Step 8? | PASS/FAIL |
| C-16 (Law B) | Law B closure gates | Do Steps 8 and 9 each contain the explicit closure sentence? | PASS/FAIL |
| C-17 | Three-loop enforcement | Charter / step reinstatements / this table — all three present? | PASS/FAIL |
| C-18 | Step-level reinstatements | Does each extraction step (1-9) that triggers Law A or B contain "Apply Law [A/B] here"? | PASS/FAIL |
| C-19 | Process-diagnostic rows | Does this table include rows C-15 and C-16 auditing process compliance? | PASS/FAIL |
| C-20 | Prevention-detection complementarity | Does charter state C-18 creates the artifacts C-19 requires? | PASS/FAIL |
| C-21 | Recursive meta-loop naming | Does charter name C-17=Loop1, C-18=Loop2, C-19=Loop3 by rubric ID? | PASS/FAIL |
| C-22 | Loop 2→3 design contract | Does charter name the artifact dependency as a constitutive structural contract? | PASS/FAIL |
| C-23 | Per-law independent chains | Does charter assign independent enforce chains per law? | PASS/FAIL |
| C-24 | Structural closure | Does charter state C-17 instantiates C-18 as necessary constitutive consequence? | PASS/FAIL |
| C-25 | Per-law artifact form | Does design contract specify C-18-A creates [AMBIG:] notations and C-18-B creates closure sentences, with per-artifact C-19-A/B audit rows? | PASS/FAIL |
| C-26 | Per-law sub-IDs in closure | Does unified closure name "C-18 (both Law A's C-18-A and Law B's C-18-B)" by sub-ID? | PASS/FAIL |
| C-27 | Definitional framing | Does structural closure include "declaring X without Y is not enforcement — it is an incomplete declaration"? | PASS/FAIL |
| C-28 | Per-loop absence clauses | Does the charter contain named Loop 1, Loop 2, and Loop 3 Absence Clause subsections, each with a localized definitional absence statement distinct from the C-27 global closure? | PASS/FAIL |
| C-29 | Definitional register as primary voice | Is definitional framing ("X is not Y without Z") the primary explanatory register throughout — in absence clauses, design contract language, step introductions, and MoSCoW anchoring — such that removing it would require rewriting the document? | PASS/FAIL |

If any FAIL in C-01..C-07, resolve before emitting. Aspirational FAILs noted but do not block.

---

Write artifact to: simulations/scout/requirements/{{topic}}-requirements-{{date}}.md
Frontmatter: skill: scout-requirements, topic: {{topic}}, date: {{date}},
             skill_version: 4.0, input: [source spec path]
```

---

## V-05: Full Synthesis — All Five Patterns

**Axis**: Full combination — per-loop sections + definitional register + inertia gates +
compliance-first (V-04 + V-03 + compliance-first ordering from R3 V-01)
**Hypothesis**: Combining all four axes creates maximum redundancy across C-25 through C-29.
The charter delivers C-28 via named per-loop absence sections (V-01 axis) and C-29 via
definitional register throughout (V-02 axis). Each extraction step delivers a secondary C-28
realization via named inertia gates (V-03 axis). Compliance-first ordering ensures compliance
requirements are the tier foundation before PM and UX can assign lower tiers. The combination
is constitutive: definitional register in named absence sections is stronger C-28 evidence
than prose alone; inertia gates at each step reinforce C-29 by distributing the definitional
voice throughout the entire document rather than confining it to the charter. The verification
table contains all 29 rows including C-28 and C-29 with explicit per-mechanism checks.

---

```
You are running /scout-requirements for: {{topic}}

---

## CHARTER — FORMAT LAWS AND THREE-LOOP META-REQUIREMENT

This charter constitutes Loop 1 (C-17 / declare) of the three-loop meta-requirement.
A requirements run is not a governed requirements run without this charter — it is unstructured
extraction. The charter does not merely precede Loop 2; it is the precondition for Loop 2's
category membership as "enforcement application."

### Format Law A: Two-Path AF- Rule

An ambiguity flag is not a Law A compliant entry without two named interpretation paths and
their consequence. Every ambiguity encountered during extraction carries an inline notation
at first encounter:

  [AMBIG: "{exact source text}" → A: {interpretation A} | B: {interpretation B}]

An AF- section that introduces ambiguities without prior inline notations is not a Law A
compliant section — it is a deferred-work section that violates the AT FIRST ENCOUNTER rule.

### Format Law B: Downstream Closure Rule

A downstream findings section (AF-, SF-) is not a closed section without the following
explicit closure statement:

  "Every entry from the prior open [AF- / SF-] register appears in this section
   with a status: open / resolved / out-of-scope."

A section containing prior entries without this statement is not a closed section — it is
an enumeration. The closure statement is the condition that converts enumeration into Law B
compliance.

### Law A Independent Enforcement Chain

- **C-17-A (Loop 1-A / declare)**: Law A declared here, independently of Law B.
  A failure in Law A's chain is not a failure of Law B's chain.
- **C-18-A (Loop 2-A / apply)**: A triggered step is not Law A compliant without "Apply Law A
  here" followed immediately by both interpretation paths inline. A step that logs the AF- ID
  without writing both paths is not a Law A compliant application.
- **C-19-A (Loop 3-A / verify)**: A verification row is not C-19-A compliant without auditing
  whether dual-interpretation [AMBIG:] notations appeared at each applicable extraction step —
  auditing the AF- section's existence is not a C-19-A process audit.

### Law B Independent Enforcement Chain

- **C-17-B (Loop 1-B / declare)**: Law B declared here, independently of Law A.
  A failure in Law B's chain is not a failure of Law A's chain.
- **C-18-B (Loop 2-B / apply)**: A downstream section is not Law B compliant without
  "Apply Law B here" followed immediately by the closure sentence inline.
- **C-19-B (Loop 3-B / verify)**: A verification row is not C-19-B compliant without auditing
  whether closure sentences appeared in each downstream section — auditing whether prior entries
  appear anywhere is not a C-19-B process audit.

### Three-Loop Meta-Requirement: Structural Closure

The two law chains unify under one self-closing declaration:

- **C-17 (Loop 1 / declare)** = this charter, including both Law A and Law B independent chains
- **C-18 (Loop 2 / apply)** = the step-level cross-references from both chains, applied per law
- **C-19 (Loop 3 / verify)** = the pre-output verification protocol table

#### Loop 1 Absence Clause

A requirements run that begins without this charter is not a requirements run with format
enforcement — it is unstructured extraction. Without Loop 1, the format laws do not exist;
without format laws, Loop 2's reinstatements have no laws to reinstate, and the category
"enforcement application" cannot apply to any step. Loop 1 is not the first of three sequential
steps — it is the definitional frame within which the other two steps acquire their enforcement
meaning.

**Structural Closure**: Declaring format laws without an application layer is not enforcement —
it is an incomplete declaration. A charter that declares Law A and Law B (C-17) without requiring
inline reinstatement at each triggering step (C-18) has not created enforcement; the category
"enforcement" requires Loop 2 by definition. Without Loop 2, what exists is a statement of
intent, not enforcement. Asserting C-17 simultaneously instantiates C-18 (both Law A's C-18-A
and Law B's C-18-B) as necessary consequences: the act of declaring laws constitutes the
obligation to apply them at each triggering step. C-19 closes the loop by auditing that C-18's
applications occurred.

#### Loop 2 Absence Clause

A charter that declares format laws without Loop 2's execution layer is not an enforcement
charter — it is a declaration without operative mechanism. Without Loop 2 (C-18's step-level
reinstatements), Loop 3 has no artifacts to audit: C-18-A's inline [AMBIG:] notations are
the evidence C-19-A requires; C-18-B's inline closure sentences are the evidence C-19-B
requires. A Loop 3 verification table operating without C-18's artifacts is not a verification
pass — it is structural theater: auditing a process that produced no checkable output.

#### Loop 3 Absence Clause

An extraction that applies format laws at each step without auditing those applications is not
a governed extraction — it is an asserted-compliant extraction. Without Loop 3 (C-19's
verification table), Loop 2's prevention work is confirmed only by assertion; violations that
passed C-18's inline enforcement have no detection layer. A prevention-only system is not an
enforcement system — it is half an enforcement system. Loop 3 is the verification condition
that makes the prevention-detection pair definitionally complete.

### Loop 2 → Loop 3 Design Contract

This charter names the following as a constitutive structural obligation before extraction
begins, chartered here as a design contract and not inferred from structural proximity:

**C-18 (Loop 2) creates the execution artifacts that C-19 (Loop 3) requires as evidence.**

C-19 without C-18's artifacts is not a verification pass — it is a verification of nothing.
Per law:
- **Law A's C-18-A** creates inline [AMBIG:] notations at each ambiguity step, each carrying
  Interpretation A and Interpretation B. A C-19-A audit row is not compliant without checking
  whether these dual-path notations are present at each applicable step — a row that checks
  only whether the AF- section exists is not a C-19-A audit.
- **Law B's C-18-B** creates inline closure sentences in each downstream findings section.
  A C-19-B audit row is not compliant without checking whether closure sentences are present
  and correctly formed at each applicable section — a row that checks only whether prior entries
  appear is not a C-19-B audit.

C-18 constitutes prevention. C-19 constitutes detection. A system with C-19 but no C-18 is not
a weaker enforcement system — it is a detection system verifying the absence of artifacts it
never created. They are complementary layers, not alternatives.

---

## STEP 0: DUAL-DIRECTORY SEARCH

**Inertia Gate (Step 0)**: Without this search, the extraction has no continuity signal from
prior work. A requirements run that begins without prior-session context is not a sessions-aware
extraction — it is a from-scratch extraction that will independently rediscover known ambiguities
and reopen closed findings. The cost of skipping Step 0 is not a single missed lookup — it is
the loss of every prior AF- and SF- entry the current run must rediscover independently.

Search for prior scout signals in BOTH:
- simulations/scout/ — real runs for {{topic}}
- simulations/trace/skill/ — hand-compiled traces for {{topic}}

A search that does not state explicit results from both directories is not a compliant
dual-directory search — it is a partial search regardless of what was found.

**Apply Law B here (Step 0)**: List all open AF- and SF- entries from prior runs.
State the closure sentence:
  "Every entry from the prior open findings register appears in this step with a status:
   open / resolved / out-of-scope."

SF-01 (undefined search path): CLOSED if trace found in simulations/trace/skill/; else OPEN.

---

## STEP 1: COMPLIANCE LENS (constitutes the non-negotiable tier foundation)

**Inertia Gate (Step 1)**: Without this step, the extraction has no regulatory boundary.
A requirements set that does not begin with compliance is not a regulated-product requirements
signal — it is a specification that may encounter mandatory obligations at implementation or
launch. Compliance mandates discovered after PM and UX preferences are set will force tier
promotions and dependency rewrites. Compliance silences found here are not audit findings —
they are unrecognized Must-tier requirements currently unclassified.

**Apply Law A here (Step 1)**: Write [AMBIG:] inline at first encounter.

Compliance requirements are not negotiable tier assignments — they are Must Have by regulatory
category. Extract:
- Legal or regulatory mandates → Must Have (the mandate constitutes the justification)
- Conditional compliance obligations (jurisdiction-scoped) → Should/Could
- Audit, reporting, and data-retention requirements implied by the concept
- Compliance silences: features in regulated spaces without named obligations are not clean —
  they are features with undetected requirements

**Apply Law B here (Step 1)**: Write closure sentence inline for each compliance silence found.

Assign IDs: C-NN (compliance). Flag blockers: "BLOCKS: [list of requirement IDs blocked]."

---

## STEP 2: PM LENS (constrained by compliance foundation)

**Inertia Gate (Step 2)**: Without this step, the extraction has no product narrative.
A requirements set that lacks PM-lens output is not a product requirements signal — it is
a technical or regulatory specification without user-goal rationale. Architect and Compliance
requirements extracted without PM context have no product shape to justify them; they can only
be prioritized against internal constraints.

**Apply Law A here (Step 2)**: Write [AMBIG:] inline at first encounter.

A PM requirement that conflicts with a Step 1 compliance mandate is not a legitimate Should
or Could candidate — it is a constraint violation. Extract:
- User goals → Must Have (if compliance-anchored) or Should Have
- Competitive capabilities → Should Have
- Delight features → Could Have
- Explicit user exclusions → Won't Have
- User scenario gaps → SS- candidates

**Apply Law B here (Step 2)**: Write closure sentence inline for each scenario gap found.

Assign IDs: P-NN (PM). Flag blockers.

---

## STEP 3: ARCHITECT LENS (constrained by compliance + PM)

**Inertia Gate (Step 3)**: Without this step, the extraction has no buildability signal.
A requirements set without Architect-lens output is not a buildable specification — it is a
product wishlist without system constraints. PM requirements without architectural coverage
cannot be assigned reliable complexity estimates. Technical silences found here are not minor
gaps — they are blockers to PM requirements that depend on them.

**Apply Law A here (Step 3)**: Write [AMBIG:] inline at first encounter.

A technical requirement enabling a compliance mandate inherits Must status by structural
entailment — it is not a negotiable preference. Extract:
- System properties enabling compliance mandates → Must (inherit tier from mandate)
- System properties enabling PM requirements → Must/Should/Could
- Platform, data-contract, integration, and deployment constraints
- Technical silences: compliance or PM requirements with no architectural specification

**Apply Law B here (Step 3)**: Write closure sentence inline for each technical silence.

Assign IDs: A-NN (architect). Flag blockers.

---

## STEP 4: UX LENS (constrained by compliance + PM + architect)

**Inertia Gate (Step 4)**: Without this step, the extraction has no interaction signal.
A requirements set that lacks UX-lens output is not a user-interaction specification — it is
a functional spec without flow coverage. Error states have no requirements backing; teams
design them ad hoc. Accessibility requirements mandated by compliance have no UX articulation
and cannot be evaluated against interaction design.

**Apply Law A here (Step 4)**: Write [AMBIG:] inline at first encounter.

An accessibility requirement mandated by compliance is not a UX Could Have — it is Must Have
by compliance category. Extract:
- Interaction requirements → Must/Should/Could
- Error states and recovery flows: a feature without an error state is not a complete feature
- First-run and onboarding experience
- Accessibility (compliance-anchored = Must by category)
- UX silences: journey phases with no interaction coverage → SS- candidates

**Apply Law B here (Step 4)**: Write closure sentence inline for each UX gap.

Assign IDs: U-NN (UX). Flag blockers.

---

## STEP 5: MOSCOW SYNTHESIS

**Inertia Gate (Step 5)**: Without this step, the extracted requirements have no unified tier
structure. Four lenses running in parallel produce four unreconciled priority views; without
synthesis, there is no single MoSCoW signal. A requirements set without four named tiers is
not a MoSCoW-structured set — it is a requirements list with informal prioritization.

Consolidate all requirements from Steps 1-4. Rules:
- Compliance mandates are not subject to tier negotiation — they constitute immovable Must items
- A requirement blocking a Must-tier item is not optional — it is Must by blocking dependency
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

**Inertia Gate (Step 6)**: Without this step, the MoSCoW table has no execution order signal.
A flat list of Must-tier requirements without dependency chains is not a buildable roadmap —
it is a set of obligations without sequencing. A dependency chain that does not name a root
blocker is not a dependency chain — it is a list of related items.

Name at least one root blocker. State what category it constitutes and why it blocks.
Show second-order chains: R-NN → R-MM → R-PP with reasoning at each link.

---

## STEP 7: LIFECYCLE PHASE COVERAGE AUDIT

**Inertia Gate (Step 7)**: Without this step, the requirements have no lifecycle completeness
signal. A requirements set that covers core-use without first-run, upgrade, or error-recovery
coverage is not a lifecycle-complete specification — it is a steady-state specification with
undetected gaps. An observability/audit phase without compliance cross-check is not a verified
COVERED — it is an unchecked assumption.

**Apply Law A here (Step 7)**: Write [AMBIG:] inline for any ambiguous coverage boundary.

| Phase | Coverage | SS- entry |
|-------|----------|-----------|
| First-run / onboarding | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Core-use / steady-state | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Upgrade / migration | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Error / recovery | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Observability / audit | COVERED / PARTIAL / SILENT | [SS-NN or —] |

---

## STEP 8: AMBIGUITY FLAGS

**Inertia Gate (Step 8)**: Without this step, the inline [AMBIG:] notations from Steps 1-7
have no formal register. A set of inline notations without a formalized AF- section is not a
documented ambiguity record — it is distributed notes that cannot be tracked across sessions.

**Apply Law A here (Step 8)**: This section formalizes all [AMBIG:] notations from Steps 1-7.
An AF- section that introduces new ambiguities here is not a Law A compliant section.

**Apply Law B here (Step 8)**: Every entry from the prior open AF- register must appear below.
State the closure sentence:
  "Every entry from the prior open AF- register appears in this section with a status:
   open / resolved / out-of-scope."

**AF-NN: [requirement ID or spec phrase]**
- Source: "[exact quote from input]" — an AF- without an exact source quote is not a documented
  ambiguity; it is an undocumented claim
- Interpretation A: [what team A would build]
- Interpretation B: [what team B would build]
- Consequence: [how the product diverges between A and B]
- Status: open / resolved / out-of-scope

[Zero AF- on a complex input is not a clean result — it is an under-extracted one.]

Closure: Every entry from the prior open AF- register appears in this section with a status. ✓

---

## STEP 9: SPEC-FAULT FINDINGS

**Inertia Gate (Step 9)**: Without this step, spec gaps identified during extraction have no
severity triage. SF- candidates are unclassified findings; without severity classification,
P0 blocking gaps are indistinguishable from P2 notes. An SF- section without at least one
entry on a non-trivial input is not a clean spec — it is an underscrutinized one.

**Apply Law B here (Step 9)**: Every entry from the prior open SF- register must appear below.
State the closure sentence:
  "Every entry from the prior open SF- register appears in this section with a status:
   open / resolved / out-of-scope."

**SF-NN: [gap or contradiction in the input spec]**
- Severity: P0 / P1 / P2
- Affected requirements: [IDs]
- Status: open / resolved / out-of-scope

Closure: Every entry from the prior open SF- register appears in this section with a status. ✓

---

## PRE-OUTPUT VERIFICATION PROTOCOL (C-19 / Loop 3 — verify)

**Inertia Gate (Verification)**: Without this table, the extraction has no process compliance
record. An output without a completed verification table is not a governed requirements signal —
it is an ungoverned requirements list. Law A and Law B applications during Steps 1-9 are
prevention assertions; without this table's detection audit, violations that passed C-18's
inline enforcement have no detection layer. This table is the condition that makes the
extraction definitionally governed.

Before emitting the final artifact, verify each criterion by ID.

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
| C-22 | Loop 2→3 design contract | Does the charter name the Loop 2→3 artifact dependency as a constitutive structural contract (not inferred)? | PASS/FAIL |
| C-23 | Per-law independent chains | Does the charter assign independent declare/apply/verify triplets per law? | PASS/FAIL |
| C-24 | Structural closure of meta-loop | Does the charter state C-17 instantiates C-18 as necessary constitutive consequence? | PASS/FAIL |
| C-25 | Per-law artifact form in design contract | Does the design contract specify that C-18-A creates inline [AMBIG:] notations and C-18-B creates closure sentences, with per-artifact C-19-A/B audit rows? | PASS/FAIL |
| C-26 | Per-law sub-IDs in unified closure statement | Does the structural closure name "C-18 (both Law A's C-18-A and Law B's C-18-B)" by sub-ID? | PASS/FAIL |
| C-27 | Definitional non-enforcement framing | Does the structural closure include "declaring X without Y is not enforcement — it is an incomplete declaration"? | PASS/FAIL |
| C-28 | Per-loop absence clauses | Does the charter contain named Loop 1, Loop 2, and Loop 3 Absence Clause sections, each with a localized definitional absence statement distinct from the C-27 global closure? AND do the Inertia Gate blocks at each extraction step and the Verification gate each echo a per-step absence clause in definitional form? | PASS/FAIL |
| C-29 | Definitional register as primary voice | Is definitional framing ("X is not Y without Z") pervasive throughout — in per-loop absence clauses, inertia gates, design contract language, MoSCoW anchoring, and step explanations — such that removing it would require rewriting the document, not just the C-27 closure statement? | PASS/FAIL |

If any FAIL in C-01..C-07, resolve before emitting. Aspirational FAILs noted but do not block.

---

Write artifact to: simulations/scout/requirements/{{topic}}-requirements-{{date}}.md
Frontmatter: skill: scout-requirements, topic: {{topic}}, date: {{date}},
             skill_version: 4.0, input: [source spec path]
```

---

```json
{"top_predicted_score": 132, "all_essential_guaranteed": true, "new_patterns_targeted": ["C-28: per-loop named absence sections in charter (V-01, V-04, V-05) + inertia gates at each extraction step (V-03, V-05)", "C-29: definitional register as primary structural voice throughout (V-02, V-04, V-05)"], "single_axis_variations": ["V-01: named per-loop absence sections in charter", "V-02: definitional register throughout", "V-03: named inertia gates at each extraction step"], "combined_variations": ["V-04: per-loop sections + definitional register + compliance-first", "V-05: full synthesis — per-loop sections + definitional register + inertia gates + compliance-first"], "orthogonality_probe": "V-01 and V-02 are designed to each independently satisfy one of C-28/C-29; if V-01 passes C-29 and V-02 passes C-28, the criteria are less orthogonal than the rubric implies — useful signal for the next rubric iteration"}
```
