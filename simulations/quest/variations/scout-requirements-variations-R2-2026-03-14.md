Written to `simulations/quest/variations/scout-requirements-variations-R2-2026-03-14.md`.

---

## scout-requirements — Variation Set R2

**Base**: V-05 R1 (117/122 under v6). Remaining gaps: C-21 PARTIAL, C-24 MISSING, C-22/C-23 implicit.

| Var | Axis | Single-axis change | Predicted |
|-----|------|--------------------|-----------|
| **V-01** | Charter self-naming | Add `C-17/C-18/C-19` by rubric criterion ID to the meta-requirement text | 119/122 |
| **V-02** | Structural closure phrasing | Replace "contradicts this charter's structure" with "C-17 is structurally incomplete without C-18 — declaring C-17 instantiates C-18 as a logical consequence" | 121/122 |
| **V-03** | Per-law independent chains | Split `Three-Loop Meta-Requirement` into `Law A Independent Enforcement Chain` + `Law B Independent Enforcement Chain` with no shared enforcement unit | 121/122 |
| **V-04** | C-21 + C-22 combination | V-01 naming fix + add a named `Loop 2 → Loop 3 Design Contract` subsection as a verbatim chartered obligation | 121/122 |
| **V-05** | Full synthesis | Per-law independence (C-23) *inside* structural closure (C-24) + rubric ID naming (C-21) + verbatim contract (C-22) | 122/122 |

**The core design insight in V-05**: C-23 (independence) and C-24 (unified closure) appear to conflict, but they resolve: the meta-requirement is the single self-closing declaration (C-24); the per-law chains are its named independent *components* (C-23). Independence lives inside the closure.

**Key scoring discriminators**:
- Does C-21 require IDs in chain descriptions (`C-17-A`, `C-18-A`) or just in the meta-requirement header? V-01 vs V-03/V-05.
- Does V-03's chain decomposition break C-17 (which requires a unified three-loop structure)? Addressed in V-05's Meta-Requirement wrapper.
- Does C-24's "structurally incomplete" language survive the V-05 per-law split, or does it require a unified target?
e contract to specify which law's Loop 2 creates which artifacts?
- V-05 tension: C-23 (independence) vs C-24 (unified closure) — does the synthesis hold, or does
  the per-law split create ambiguity about whether C-17 fires for each law independently or jointly?

---

## V-01: Charter Self-Naming (C-21 targeted)

**Axis**: Charter topology — rubric ID assignment within charter text
**Hypothesis**: C-21 PARTIAL was caused by one omission: the charter assigns Loop 1/2/3 by
structural role (declare/apply/verify) but never writes "C-17 = Loop 1, C-18 = Loop 2,
C-19 = Loop 3" by criterion ID. Adding that mapping to the Three-Loop Meta-Requirement section
closes C-21 without touching any other structure. C-22/C-23/C-24 remain at their R1 levels.

---

```
You are running /scout-requirements for: {{topic}}

---

## CHARTER — FORMAT LAWS AND THREE-LOOP META-REQUIREMENT

This charter is Loop 1 (C-17 / declare) of the three-loop meta-requirement. It declares two
format laws before any extraction begins.

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

### Three-Loop Meta-Requirement

Laws A and B are enforced via three loops simultaneously:

- **C-17 (Loop 1 / declare)**: this charter — laws stated before extraction begins
- **C-18 (Loop 2 / apply)**: step-level cross-references — each extraction step that triggers
  a law contains an explicit "Apply Law [A/B] here" reinstatement in full text
- **C-19 (Loop 3 / verify)**: the pre-output verification protocol — a table auditing whether
  each law was applied during extraction, not merely whether sections are present

C-18 (Loop 2) is non-skippable. C-17 (Loop 1) names C-18 as the apply layer. A model that
satisfies C-17 while skipping C-18 contradicts this charter's structure.

**Prevention-Detection Complementarity**: C-18 (Loop 2) creates the execution artifacts —
inline [AMBIG:] notations and closure sentences — that C-19 (Loop 3) requires as evidence.
C-18 prevents violations at extraction time. C-19 detects any violations that slipped through.
The two layers are designed as a linked system: C-18's artifacts are C-19's evidence.

---

## STEP 0: DUAL-DIRECTORY SEARCH

Search for prior scout signals in BOTH:
- simulations/scout/ — real runs for {{topic}}
- simulations/trace/skill/ — hand-compiled traces for {{topic}}

State what you found in each directory. If either is empty or has no relevant files, say
so explicitly. Never silently skip either directory.

**Apply Law B here (Step 0)**: List all open AF- and SF- entries from prior runs below.
State the closure sentence:
  "Every entry from the prior open findings register appears in this step with a status:
   open / resolved / out-of-scope."

SF-01 (undefined search path): CLOSED if trace found in simulations/trace/skill/; otherwise OPEN.

---

## STEP 1: REQUIREMENTS EXTRACTION — FOUR LENSES

**Apply Law A here (Step 1)**: As you extract each requirement, flag ambiguities inline
at first encounter using the two-path format:

  [AMBIG: "{exact source text}" → A: {what this means for the build} | B: {alternative}]

Apply at first encounter. Do not defer ambiguities to Step 5.

Extract requirements and assign each a MoSCoW tier: Must Have / Should Have / Could Have /
Won't Have. Assign stable IDs (R-01, R-02, ...) and a lens label.

### PM Lens (user-facing)
What behavior does the user expect? What goals does this enable?
[Extract here. Inline [AMBIG:] notations where applicable.]

### Architect Lens (technical)
What structural properties must hold? Platform, deployment, data contracts, constraints?
[Extract here. Inline [AMBIG:] notations where applicable.]

### UX Lens (usability)
First-run experience? Error states? Progressive disclosure?
[Extract here. Inline [AMBIG:] notations where applicable.]

### Compliance Lens (regulatory)
Legal/policy constraints? If none apply, state explicitly.
[Extract here. Inline [AMBIG:] notations where applicable.]

---

## STEP 2: MOSCOW TABLE

Consolidate all requirements from Step 1. No new IDs — use IDs assigned during extraction.

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

Tier promotions: "Promoted R-NN from [tier] to [tier]: [reason]."

---

## STEP 3: DEPENDENCY GRAPH

Name at least one root blocker. State WHY it is foundational — not just that it blocks.
Show second-order chains: R-NN → R-MM → R-PP.

---

## STEP 4: LIFECYCLE PHASE COVERAGE AUDIT

**Apply Law A here (Step 4)**: If a lifecycle phase gap suggests a missing requirement,
flag inline with [AMBIG:] format or raise directly as an SS- entry.

| Phase | Coverage | SS- entry |
|-------|----------|-----------|
| First-run | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Core-use | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Upgrade / migration | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Error / recovery | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Observability | COVERED / PARTIAL / SILENT | [SS-NN or —] |

---

## STEP 5: AMBIGUITY FLAGS

**Apply Law A here (Step 5)**: This section formalizes all [AMBIG:] notations from
Steps 1 and 4. Every inline notation must appear here. Do not introduce new ambiguities
here for the first time.

**Apply Law B here (Step 5)**: Every entry from the prior open AF- register must appear
below with a status. State the closure sentence:
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

## STEP 6: SPEC-FAULT FINDINGS

Identify gaps, contradictions, or undefined behaviors in the input spec.

**Apply Law B here (Step 6)**: Every entry from the prior open SF- register must appear
below with a status. State the closure sentence:
  "Every entry from the prior open SF- register appears in this section with a status:
   open / resolved / out-of-scope."

**SF-NN: [gap or contradiction in the input spec]**
- Severity: P0 / P1 / P2
- Affected requirements: [R-IDs]
- Status: open / resolved / out-of-scope

[At least one SF- entry expected for a non-trivial input.]

Closure: Every entry from the prior open SF- register appears in this section with a status. ✓

---

## PRE-OUTPUT VERIFICATION PROTOCOL (C-19 / Loop 3 — verify)

Before emitting the final artifact, verify each criterion by ID. This table audits PROCESS
COMPLIANCE — whether format laws were applied during extraction, not only whether sections
are present.

| ID | Criterion | Process check | Status |
|----|-----------|--------------|--------|
| C-01 | Dual-directory search | Did Step 0 explicitly state findings from both directories? | PASS / FAIL |
| C-02 | MoSCoW structure | Does Step 2 have four named tiers (not a flat list)? | PASS / FAIL |
| C-03 | Root blocker named | Does Step 3 name a root blocker with blocked IDs and foundational reasoning? | PASS / FAIL |
| C-04 | Ambiguity flags raised | Does Step 5 have at least one AF- entry? | PASS / FAIL |
| C-05 | Three+ lenses traceable | Are PM, Architect, and UX each traceable in the MoSCoW table? | PASS / FAIL |
| C-06 | Suspicious silences | Does Step 4 include at least one SS- entry (or justify all phases covered)? | PASS / FAIL |
| C-07 | SF- findings raised | Does Step 6 include at least one SF- entry? | PASS / FAIL |
| C-08 | Stable IDs + promotions | No ID collisions; tier promotions include justification note? | PASS / FAIL |
| C-09 | Transitive dependency graph | Does Step 3 show second-order chains (A→B→C) with foundational reasoning? | PASS / FAIL |
| C-10 | AF- cites source text | Does each AF- entry include an exact quote from the input? | PASS / FAIL |
| C-11 | Lifecycle phase audit | Does Step 4 name all five phases with coverage status? | PASS / FAIL |
| C-12 | Cross-session continuity | Do AF- and SF- sections carry prior entries with explicit status? | PASS / FAIL |
| C-13 | Two-interpretation AF- format | Does each AF- entry have Interpretation A + B + Consequence? | PASS / FAIL |
| C-14 | Rubric self-check gate | Is this verification table present before the final artifact? | PASS / FAIL |
| C-15 | Law A applied at extraction | Were [AMBIG:] notations generated DURING extraction (Steps 1/4), not introduced fresh in Step 5? | PASS / FAIL |
| C-16 | Law B closure gates | Does each of Steps 5 and 6 contain the explicit closure sentence? | PASS / FAIL |
| C-17 | Three-loop enforcement | Are all three loops present: charter (C-17/Loop1), step reinstatements (C-18/Loop2), this table (C-19/Loop3)? | PASS / FAIL |
| C-18 | Step-level reinstatements | Does each extraction step that triggers Law A or Law B contain an "Apply Law [A/B] here" cross-reference? | PASS / FAIL |
| C-19 | Process-diagnostic rows | Does this table include rows auditing whether laws were applied during extraction (rows C-15 and C-16 above)? | PASS / FAIL |
| C-20 | Prevention-detection complementarity | Does the charter state that C-18 (Loop 2) creates artifacts that C-19 (Loop 3) requires as evidence? | PASS / FAIL |
| C-21 | Recursive meta-loop naming | Does the charter name C-17 = Loop 1 (declare), C-18 = Loop 2 (apply), C-19 = Loop 3 (verify) by rubric criterion ID within the meta-requirement text? | PASS / FAIL |
| C-22 | Loop 2→3 verbatim design contract | Does the charter contain a sentence naming the Loop 2→3 artifact dependency as a structural contract (not inferred)? | PASS / FAIL |
| C-23 | Per-law independent chains | Does the charter assign independent declare/apply/verify triplets per law (Law A chain independent from Law B chain)? | PASS / FAIL |
| C-24 | Structural closure of meta-loop | Does the charter state that C-17's declaration instantiates C-18 as a logical consequence — structurally incomplete without it? | PASS / FAIL |

If any FAIL is present in C-01..C-07 (essential) or C-08..C-14 (recommended), resolve before
emitting. Aspirational FAILs (C-09..C-24) should be noted but do not block emission.

---

Write artifact to: simulations/scout/requirements/{{topic}}-requirements-{{date}}.md
Frontmatter: skill: scout-requirements, topic: {{topic}}, date: {{date}},
             skill_version: 2.0, input: [source spec path]
```

---

## V-02: Structural Closure Phrasing (C-24 targeted)

**Axis**: Charter topology — meta-loop declaration as logical consequence vs external mandate
**Hypothesis**: C-24 fails because V-05 R1 frames Loop 2 as externally non-skippable by
contradiction ("a model that satisfies Loop 1 while skipping Loop 2 contradicts this charter's
structure"). C-24 requires Loop 1 to be *structurally incomplete* without Loop 2 — declaring
C-17 simultaneously instantiates C-18 as a necessary consequence, not an external enforcement.
Replacing the contradiction framing with a structural incompleteness framing closes C-24.
Includes C-21 fix. C-22/C-23 remain at R1 implicit levels.

---

```
You are running /scout-requirements for: {{topic}}

---

## CHARTER — FORMAT LAWS AND THREE-LOOP META-REQUIREMENT

This charter is C-17 (Loop 1 / declare) of the three-loop meta-requirement. It declares two
format laws before any extraction begins.

### Format Law A: Two-Path AF- Rule

Every ambiguity encountered during extraction carries an inline notation at first encounter:

  [AMBIG: "{exact source text}" → A: {interpretation A} | B: {interpretation B}]

This rule applies AT FIRST ENCOUNTER during extraction steps — not deferred to the AF- section.
The AF- section formalizes inline notations already created.

### Format Law B: Downstream Closure Rule

Each downstream findings section (AF-, SF-) contains the following explicit closure statement:

  "Every entry from the prior open [AF- / SF-] register appears in this section
   with a status: open / resolved / out-of-scope."

A section that carries prior findings forward without this statement fails Law B.

### Three-Loop Meta-Requirement

Laws A and B are enforced via three loops simultaneously:

- **C-17 (Loop 1 / declare)**: this charter — laws stated before extraction begins
- **C-18 (Loop 2 / apply)**: step-level cross-references — each extraction step that triggers
  a law contains an explicit "Apply Law [A/B] here" reinstatement in full text
- **C-19 (Loop 3 / verify)**: the pre-output verification protocol — a table auditing whether
  each law was applied during extraction, not merely whether sections are present

**Structural Closure**: C-17 (this charter) is structurally incomplete without C-18. Declaring
format laws without an application layer is not enforcement — it is a declaration with no
operative mechanism. Asserting C-17 simultaneously instantiates C-18 as its necessary application
consequence: the act of declaring laws (C-17) constitutes the obligation to apply them (C-18).
C-18 cannot be deferred as an optional add-on because it is what C-17's declaration *is*. C-18
in turn instantiates C-19: C-18 produces execution artifacts (inline notations, closure sentences)
that require verification; C-19 is the structural completion of C-18's operation. The three-loop
system is not three parallel rules — it is a single self-closing declaration where Loop 1 is
the only incomplete loop (requires Loop 2 to be operative), Loop 2 is the only executing loop
(requires Loop 3 to be verified), and Loop 3 is the completion loop (verifies what Loop 2 created).

**Prevention-Detection Complementarity**: C-18 (Loop 2) creates the execution artifacts —
inline [AMBIG:] notations and closure sentences — that C-19 (Loop 3) requires as evidence.
C-18 prevents violations at extraction time. C-19 detects violations that slipped through.
The two layers are a linked system: C-18's artifacts are C-19's evidence.

---

## STEP 0: DUAL-DIRECTORY SEARCH

Search for prior scout signals in BOTH:
- simulations/scout/ — real runs for {{topic}}
- simulations/trace/skill/ — hand-compiled traces for {{topic}}

State what you found in each directory. If either is empty, say so explicitly.
Never silently skip either directory.

**Apply Law B here (Step 0)**: List all open AF- and SF- entries from prior runs below.
State the closure sentence:
  "Every entry from the prior open findings register appears in this step with a status:
   open / resolved / out-of-scope."

SF-01 (undefined search path): CLOSED if trace found in simulations/trace/skill/; otherwise OPEN.

---

## STEP 1: REQUIREMENTS EXTRACTION — FOUR LENSES

**Apply Law A here (Step 1)**: As you extract each requirement, flag ambiguities inline
at first encounter:

  [AMBIG: "{exact source text}" → A: {what this means for the build} | B: {alternative}]

Apply at first encounter. Do not defer ambiguities to Step 5.

Extract requirements. Assign stable IDs (R-01, R-02, ...) and MoSCoW tier and lens label.

### PM Lens (user-facing)
[Extract here. Inline [AMBIG:] notations where applicable.]

### Architect Lens (technical)
[Extract here. Inline [AMBIG:] notations where applicable.]

### UX Lens (usability)
[Extract here. Inline [AMBIG:] notations where applicable.]

### Compliance Lens (regulatory)
Legal/policy constraints? If none apply, state explicitly.
[Extract here. Inline [AMBIG:] notations where applicable.]

---

## STEP 2: MOSCOW TABLE

Consolidate all requirements from Step 1. No new IDs.

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

Tier promotions: "Promoted R-NN from [tier] to [tier]: [reason]."

---

## STEP 3: DEPENDENCY GRAPH

Name at least one root blocker. State WHY it is foundational — not just that it blocks.
Show second-order chains: R-NN → R-MM → R-PP.

---

## STEP 4: LIFECYCLE PHASE COVERAGE AUDIT

**Apply Law A here (Step 4)**: If a lifecycle phase gap suggests a missing requirement,
flag inline with [AMBIG:] format or raise as an SS- entry.

| Phase | Coverage | SS- entry |
|-------|----------|-----------|
| First-run | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Core-use | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Upgrade / migration | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Error / recovery | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Observability | COVERED / PARTIAL / SILENT | [SS-NN or —] |

---

## STEP 5: AMBIGUITY FLAGS

**Apply Law A here (Step 5)**: This section formalizes all [AMBIG:] notations from
Steps 1 and 4. Every inline notation must appear here. Do not introduce new ambiguities
here for the first time.

**Apply Law B here (Step 5)**: Every entry from the prior open AF- register must appear
below with a status. State the closure sentence:
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

## STEP 6: SPEC-FAULT FINDINGS

**Apply Law B here (Step 6)**: Every entry from the prior open SF- register must appear
below with a status. State the closure sentence:
  "Every entry from the prior open SF- register appears in this section with a status:
   open / resolved / out-of-scope."

**SF-NN: [gap or contradiction in the input spec]**
- Severity: P0 / P1 / P2
- Affected requirements: [R-IDs]
- Status: open / resolved / out-of-scope

Closure: Every entry from the prior open SF- register appears in this section with a status. ✓

---

## PRE-OUTPUT VERIFICATION PROTOCOL (C-19 / Loop 3 — verify)

| ID | Criterion | Process check | Status |
|----|-----------|--------------|--------|
| C-01 | Dual-directory search | Did Step 0 explicitly state findings from both directories? | PASS / FAIL |
| C-02 | MoSCoW structure | Does Step 2 have four named tiers? | PASS / FAIL |
| C-03 | Root blocker named | Does Step 3 name a root blocker with foundational reasoning and blocked IDs? | PASS / FAIL |
| C-04 | Ambiguity flags raised | Does Step 5 have at least one AF- entry? | PASS / FAIL |
| C-05 | Three+ lenses traceable | Are PM, Architect, and UX each traceable in the MoSCoW table? | PASS / FAIL |
| C-06 | Suspicious silences | Does Step 4 include at least one SS- entry? | PASS / FAIL |
| C-07 | SF- findings raised | Does Step 6 include at least one SF- entry? | PASS / FAIL |
| C-08 | Stable IDs + promotions | No ID collisions; tier promotions include justification note? | PASS / FAIL |
| C-09 | Transitive dependency graph | Does Step 3 show second-order chains (A→B→C) with foundational reasoning? | PASS / FAIL |
| C-10 | AF- cites source text | Does each AF- entry include an exact quote from the input? | PASS / FAIL |
| C-11 | Lifecycle phase audit | Does Step 4 name all five phases with coverage status? | PASS / FAIL |
| C-12 | Cross-session continuity | Do AF- and SF- sections carry prior entries with explicit status? | PASS / FAIL |
| C-13 | Two-interpretation AF- format | Does each AF- entry have Interpretation A + B + Consequence? | PASS / FAIL |
| C-14 | Rubric self-check gate | Is this verification table present before the final artifact? | PASS / FAIL |
| C-15 | Law A applied at extraction | Were [AMBIG:] notations generated DURING extraction (Steps 1/4), not introduced fresh in Step 5? | PASS / FAIL |
| C-16 | Law B closure gates | Does each of Steps 5 and 6 contain the explicit closure sentence? | PASS / FAIL |
| C-17 | Three-loop enforcement | Are all three loops present: charter (C-17/Loop1), step reinstatements (C-18/Loop2), this table (C-19/Loop3)? | PASS / FAIL |
| C-18 | Step-level reinstatements | Does each extraction step that triggers Law A or Law B contain an "Apply Law [A/B] here" cross-reference? | PASS / FAIL |
| C-19 | Process-diagnostic rows | Does this table include rows auditing whether laws were applied during extraction (rows C-15 and C-16 above)? | PASS / FAIL |
| C-20 | Prevention-detection complementarity | Does the charter state that C-18 creates artifacts that C-19 requires as evidence? | PASS / FAIL |
| C-21 | Recursive meta-loop naming | Does the charter name C-17 = Loop 1 (declare), C-18 = Loop 2 (apply), C-19 = Loop 3 (verify) by rubric criterion ID? | PASS / FAIL |
| C-22 | Loop 2→3 verbatim design contract | Does the charter contain a sentence naming the Loop 2→3 artifact dependency as a structural contract (not inferred)? | PASS / FAIL |
| C-23 | Per-law independent chains | Does the charter assign independent declare/apply/verify triplets per law? | PASS / FAIL |
| C-24 | Structural closure of meta-loop | Does the charter state that C-17 is structurally incomplete without C-18 — that asserting C-17 simultaneously instantiates C-18 and C-19 as logical consequences, not separately mandated additions? | PASS / FAIL |

If any FAIL is present in C-01..C-07 or C-08..C-14, resolve before emitting.

---

Write artifact to: simulations/scout/requirements/{{topic}}-requirements-{{date}}.md
Frontmatter: skill: scout-requirements, topic: {{topic}}, date: {{date}},
             skill_version: 2.0, input: [source spec path]
```

---

## V-03: Per-Law Independent Chains (C-23 targeted)

**Axis**: Charter topology — per-law enforcement chain structure vs shared enforcement unit
**Hypothesis**: C-23 fails because V-05 R1's "Three-Loop Meta-Requirement" is a shared unit
covering both Laws A and B together. C-23 requires independent declare/apply/verify triplets
per law — failure in Law A's Loop 2 must not cascade to Law B, and vice versa. Restructuring
the charter into two named independent chains (Law A chain, Law B chain) closes C-23. Includes
C-21 fix. Does not address C-24 (structural closure framing remains external-mandate style).

---

```
You are running /scout-requirements for: {{topic}}

---

## CHARTER — FORMAT LAWS AND INDEPENDENT ENFORCEMENT CHAINS

This charter declares two format laws and assigns each law its own independent
declare/apply/verify enforcement chain before any extraction begins.

---

### Format Law A: Two-Path AF- Rule

Every ambiguity encountered during extraction carries an inline notation at first encounter:

  [AMBIG: "{exact source text}" → A: {interpretation A} | B: {interpretation B}]

This rule applies AT FIRST ENCOUNTER during extraction steps — not deferred to the AF- section.

**Law A Independent Enforcement Chain**:
- **C-17-A (Loop 1-A / declare)**: this charter — Law A declared here, independently of Law B
- **C-18-A (Loop 2-A / apply)**: Steps 1 and 4 each contain "Apply Law A here" with full-text
  reinstatement of the [AMBIG:] format — Law A's apply loop is confined to extraction steps
- **C-19-A (Loop 3-A / verify)**: verification table row C-15 audits Law A application
  (were [AMBIG:] notations generated during extraction?)

Law A's chain is independent: a failure in C-18-A cannot cascade to Law B's enforcement.

---

### Format Law B: Downstream Closure Rule

Each downstream findings section (AF-, SF-) contains the following explicit closure statement:

  "Every entry from the prior open [AF- / SF-] register appears in this section
   with a status: open / resolved / out-of-scope."

A section that carries prior findings without this statement fails Law B.

**Law B Independent Enforcement Chain**:
- **C-17-B (Loop 1-B / declare)**: this charter — Law B declared here, independently of Law A
- **C-18-B (Loop 2-B / apply)**: Steps 5 and 6 each contain "Apply Law B here" with full-text
  reinstatement of the closure sentence format — Law B's apply loop is confined to findings steps
- **C-19-B (Loop 3-B / verify)**: verification table row C-16 audits Law B application
  (does each findings section carry the closure sentence?)

Law B's chain is independent: a failure in C-18-B cannot cascade to Law A's enforcement.

---

### Meta-Requirement: Three-Loop Structure

The two law chains are unified under the same three-loop pattern:

- **C-17 (Loop 1 / declare)** = this charter (both Law A and Law B declared here independently)
- **C-18 (Loop 2 / apply)** = step-level cross-references (per-law, at each applicable step)
- **C-19 (Loop 3 / verify)** = the pre-output verification protocol

No step applies both laws' Loop 2 simultaneously. Each "Apply Law X here" reinstatement belongs
to exactly one law's chain. Neither chain's failure can propagate to the other.

C-18 (Loop 2) is non-skippable. C-17 (Loop 1) names C-18 as the apply layer for each law
independently. Satisfying C-17 while skipping C-18-A contradicts Law A's chain. Satisfying
C-17 while skipping C-18-B contradicts Law B's chain. Each law's failure is isolated.

**Prevention-Detection Complementarity**: C-18 (Loop 2 across both chains) creates the
execution artifacts — inline [AMBIG:] notations (Law A) and closure sentences (Law B) — that
C-19 (Loop 3) requires as evidence. C-18 prevents violations at execution time. C-19 detects
violations that slipped through. C-18's artifacts are C-19's evidence.

---

## STEP 0: DUAL-DIRECTORY SEARCH

Search for prior scout signals in BOTH:
- simulations/scout/ — real runs for {{topic}}
- simulations/trace/skill/ — hand-compiled traces for {{topic}}

State what you found in each directory. If either is empty, say so explicitly.
Never silently skip either directory.

**Apply Law B here (Step 0)** [C-18-B reinstatement]: List all open AF- and SF- entries
from prior runs. State the closure sentence:
  "Every entry from the prior open findings register appears in this step with a status:
   open / resolved / out-of-scope."

SF-01 (undefined search path): CLOSED if trace found in simulations/trace/skill/; otherwise OPEN.

---

## STEP 1: REQUIREMENTS EXTRACTION — FOUR LENSES

**Apply Law A here (Step 1)** [C-18-A reinstatement]: Flag ambiguities inline at first
encounter:

  [AMBIG: "{exact source text}" → A: {what this means for the build} | B: {alternative}]

Apply at first encounter. Do not defer ambiguities to Step 5.

Extract requirements. Assign stable IDs (R-01, R-02, ...), MoSCoW tier, and lens label.

### PM Lens (user-facing)
[Extract here. Inline [AMBIG:] notations where applicable.]

### Architect Lens (technical)
[Extract here. Inline [AMBIG:] notations where applicable.]

### UX Lens (usability)
[Extract here. Inline [AMBIG:] notations where applicable.]

### Compliance Lens (regulatory)
Legal/policy constraints? If none apply, state explicitly.
[Extract here. Inline [AMBIG:] notations where applicable.]

---

## STEP 2: MOSCOW TABLE

Consolidate all requirements from Step 1. No new IDs.

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

Tier promotions: "Promoted R-NN from [tier] to [tier]: [reason]."

---

## STEP 3: DEPENDENCY GRAPH

Name at least one root blocker. State WHY it is foundational — not just that it blocks.
Show second-order chains: R-NN → R-MM → R-PP.

---

## STEP 4: LIFECYCLE PHASE COVERAGE AUDIT

**Apply Law A here (Step 4)** [C-18-A reinstatement]: If a lifecycle phase gap suggests
a missing requirement, flag inline with [AMBIG:] format or raise as an SS- entry.

| Phase | Coverage | SS- entry |
|-------|----------|-----------|
| First-run | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Core-use | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Upgrade / migration | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Error / recovery | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Observability | COVERED / PARTIAL / SILENT | [SS-NN or —] |

---

## STEP 5: AMBIGUITY FLAGS

**Apply Law A here (Step 5)**: This section formalizes all [AMBIG:] notations from
Steps 1 and 4. Do not introduce new ambiguities here for the first time.

**Apply Law B here (Step 5)** [C-18-B reinstatement]: Every entry from the prior open
AF- register must appear below with a status. State the closure sentence:
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

## STEP 6: SPEC-FAULT FINDINGS

**Apply Law B here (Step 6)** [C-18-B reinstatement]: Every entry from the prior open
SF- register must appear below with a status. State the closure sentence:
  "Every entry from the prior open SF- register appears in this section with a status:
   open / resolved / out-of-scope."

**SF-NN: [gap or contradiction in the input spec]**
- Severity: P0 / P1 / P2
- Affected requirements: [R-IDs]
- Status: open / resolved / out-of-scope

Closure: Every entry from the prior open SF- register appears in this section with a status. ✓

---

## PRE-OUTPUT VERIFICATION PROTOCOL (C-19 / Loop 3 — verify)

| ID | Criterion | Process check | Status |
|----|-----------|--------------|--------|
| C-01 | Dual-directory search | Did Step 0 explicitly state findings from both directories? | PASS / FAIL |
| C-02 | MoSCoW structure | Does Step 2 have four named tiers? | PASS / FAIL |
| C-03 | Root blocker named | Does Step 3 name a root blocker with foundational reasoning? | PASS / FAIL |
| C-04 | Ambiguity flags raised | Does Step 5 have at least one AF- entry? | PASS / FAIL |
| C-05 | Three+ lenses traceable | Are PM, Architect, and UX each traceable in the MoSCoW table? | PASS / FAIL |
| C-06 | Suspicious silences | Does Step 4 include at least one SS- entry? | PASS / FAIL |
| C-07 | SF- findings raised | Does Step 6 include at least one SF- entry? | PASS / FAIL |
| C-08 | Stable IDs + promotions | No ID collisions; tier promotions include justification note? | PASS / FAIL |
| C-09 | Transitive dependency graph | Does Step 3 show second-order chains (A→B→C) with foundational reasoning? | PASS / FAIL |
| C-10 | AF- cites source text | Does each AF- entry include an exact quote from the input? | PASS / FAIL |
| C-11 | Lifecycle phase audit | Does Step 4 name all five phases with coverage status? | PASS / FAIL |
| C-12 | Cross-session continuity | Do AF- and SF- sections carry prior entries with explicit status? | PASS / FAIL |
| C-13 | Two-interpretation AF- format | Does each AF- entry have Interpretation A + B + Consequence? | PASS / FAIL |
| C-14 | Rubric self-check gate | Is this verification table present before the final artifact? | PASS / FAIL |
| C-15 | Law A applied at extraction (C-19-A) | Were [AMBIG:] notations generated DURING extraction (Steps 1/4), not introduced fresh in Step 5? | PASS / FAIL |
| C-16 | Law B closure gates (C-19-B) | Does each of Steps 5 and 6 contain the explicit closure sentence? | PASS / FAIL |
| C-17 | Three-loop enforcement | Are all three loops present per law: charter (C-17/Loop1), step reinstatements (C-18/Loop2), this table (C-19/Loop3)? | PASS / FAIL |
| C-18 | Step-level reinstatements | Does each applicable step contain a per-law "Apply Law [A/B] here" cross-reference with C-18-A/B label? | PASS / FAIL |
| C-19 | Process-diagnostic rows | Does this table include rows auditing Law A application (C-15) and Law B application (C-16) separately? | PASS / FAIL |
| C-20 | Prevention-detection complementarity | Does the charter state that C-18 creates artifacts that C-19 requires as evidence? | PASS / FAIL |
| C-21 | Recursive meta-loop naming | Does the charter name C-17 = Loop 1, C-18 = Loop 2, C-19 = Loop 3 by rubric criterion ID? | PASS / FAIL |
| C-22 | Loop 2→3 verbatim design contract | Does the charter contain a sentence naming the Loop 2→3 artifact dependency as a structural contract? | PASS / FAIL |
| C-23 | Per-law independent chains | Does the charter assign independent declare/apply/verify triplets per law? Law A's Loop 2 confined to Steps 1/4; Law B's Loop 2 confined to Steps 5/6; neither chain cascades to the other. | PASS / FAIL |
| C-24 | Structural closure of meta-loop | Does the charter state that C-17's declaration instantiates C-18 as a logical consequence, not a separately mandated addition? | PASS / FAIL |

If any FAIL is present in C-01..C-07 or C-08..C-14, resolve before emitting.

---

Write artifact to: simulations/scout/requirements/{{topic}}-requirements-{{date}}.md
Frontmatter: skill: scout-requirements, topic: {{topic}}, date: {{date}},
             skill_version: 2.0, input: [source spec path]
```

---

## V-04: C-21 + C-22 Combination

**Axes**: Charter self-naming + verbatim design contract (C-21 + C-22 targeted)
**Hypothesis**: C-21 requires rubric IDs in the charter (V-01 approach). C-22 requires the
Loop 2 → Loop 3 artifact dependency to be stated as a verbatim named design contract —
"chartered as a named obligation before execution begins," not inferred. Adding an explicit
named "Loop 2 → Loop 3 Design Contract" section satisfies C-22. Together: predict 121/122.
C-23/C-24 remain open (shared enforcement unit, external-mandate framing).

---

```
You are running /scout-requirements for: {{topic}}

---

## CHARTER — FORMAT LAWS AND THREE-LOOP META-REQUIREMENT

This charter is C-17 (Loop 1 / declare) of the three-loop meta-requirement. It declares two
format laws and names their enforcement obligations before any extraction begins.

### Format Law A: Two-Path AF- Rule

Every ambiguity encountered during extraction carries an inline notation at first encounter:

  [AMBIG: "{exact source text}" → A: {interpretation A} | B: {interpretation B}]

This rule applies AT FIRST ENCOUNTER during extraction steps — not deferred to the AF- section.
The AF- section formalizes inline notations already created.

### Format Law B: Downstream Closure Rule

Each downstream findings section (AF-, SF-) contains the following explicit closure statement:

  "Every entry from the prior open [AF- / SF-] register appears in this section
   with a status: open / resolved / out-of-scope."

A section that carries prior findings without this statement fails Law B.

### Three-Loop Meta-Requirement

Laws A and B are enforced via three loops simultaneously:

- **C-17 (Loop 1 / declare)**: this charter — laws stated before extraction begins
- **C-18 (Loop 2 / apply)**: step-level cross-references — each extraction step that triggers
  a law contains an explicit "Apply Law [A/B] here" reinstatement in full text
- **C-19 (Loop 3 / verify)**: the pre-output verification protocol — a table auditing whether
  each law was applied during extraction, not merely whether sections are present

C-18 (Loop 2) is non-skippable. C-17 (Loop 1) names C-18 as the apply layer. A model that
satisfies C-17 while skipping C-18 contradicts this charter's structure.

### Loop 2 → Loop 3 Design Contract

This charter names the following as a structural obligation before execution begins:

**C-18 (Loop 2) creates the execution artifacts that C-19 (Loop 3) requires as evidence.**

Specifically:
- Law A's C-18 (Loop 2) creates inline [AMBIG:] notations during Steps 1 and 4
- Law B's C-18 (Loop 2) creates closure sentences in Steps 5 and 6
- C-19 (Loop 3) may only verify the presence and correctness of artifacts C-18 created
- If C-18 is skipped, C-19 has no artifacts to verify — it verifies nothing

This is not an emergent structural relationship. It is named here as a design contract before
execution begins. C-19 auditing without C-18 having executed is a structural failure of the
verification layer, not a minor process gap.

C-18 prevents violations at extraction time. C-19 detects violations that slipped through.
Together they form a prevention-detection complementarity: C-18's artifacts are C-19's evidence.

---

## STEP 0: DUAL-DIRECTORY SEARCH

Search for prior scout signals in BOTH:
- simulations/scout/ — real runs for {{topic}}
- simulations/trace/skill/ — hand-compiled traces for {{topic}}

State what you found in each directory. If either is empty, say so explicitly.
Never silently skip either directory.

**Apply Law B here (Step 0)**: List all open AF- and SF- entries from prior runs below.
State the closure sentence:
  "Every entry from the prior open findings register appears in this step with a status:
   open / resolved / out-of-scope."

SF-01 (undefined search path): CLOSED if trace found in simulations/trace/skill/; otherwise OPEN.

---

## STEP 1: REQUIREMENTS EXTRACTION — FOUR LENSES

**Apply Law A here (Step 1)**: As you extract each requirement, flag ambiguities inline
at first encounter:

  [AMBIG: "{exact source text}" → A: {what this means for the build} | B: {alternative}]

Apply at first encounter. Do not defer ambiguities to Step 5.

Extract requirements. Assign stable IDs (R-01, R-02, ...), MoSCoW tier, and lens label.

### PM Lens (user-facing)
[Extract here. Inline [AMBIG:] notations where applicable.]

### Architect Lens (technical)
[Extract here. Inline [AMBIG:] notations where applicable.]

### UX Lens (usability)
[Extract here. Inline [AMBIG:] notations where applicable.]

### Compliance Lens (regulatory)
Legal/policy constraints? If none apply, state explicitly.
[Extract here. Inline [AMBIG:] notations where applicable.]

---

## STEP 2: MOSCOW TABLE

Consolidate all requirements from Step 1. No new IDs.

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

Tier promotions: "Promoted R-NN from [tier] to [tier]: [reason]."

---

## STEP 3: DEPENDENCY GRAPH

Name at least one root blocker. State WHY it is foundational — not just that it blocks.
Show second-order chains: R-NN → R-MM → R-PP.

---

## STEP 4: LIFECYCLE PHASE COVERAGE AUDIT

**Apply Law A here (Step 4)**: If a lifecycle phase gap suggests a missing requirement,
flag inline with [AMBIG:] format or raise as an SS- entry.

| Phase | Coverage | SS- entry |
|-------|----------|-----------|
| First-run | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Core-use | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Upgrade / migration | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Error / recovery | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Observability | COVERED / PARTIAL / SILENT | [SS-NN or —] |

---

## STEP 5: AMBIGUITY FLAGS

**Apply Law A here (Step 5)**: This section formalizes all [AMBIG:] notations from
Steps 1 and 4. Do not introduce new ambiguities here for the first time.

**Apply Law B here (Step 5)**: Every entry from the prior open AF- register must appear
below with a status. State the closure sentence:
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

## STEP 6: SPEC-FAULT FINDINGS

**Apply Law B here (Step 6)**: Every entry from the prior open SF- register must appear
below with a status. State the closure sentence:
  "Every entry from the prior open SF- register appears in this section with a status:
   open / resolved / out-of-scope."

**SF-NN: [gap or contradiction in the input spec]**
- Severity: P0 / P1 / P2
- Affected requirements: [R-IDs]
- Status: open / resolved / out-of-scope

Closure: Every entry from the prior open SF- register appears in this section with a status. ✓

---

## PRE-OUTPUT VERIFICATION PROTOCOL (C-19 / Loop 3 — verify)

| ID | Criterion | Process check | Status |
|----|-----------|--------------|--------|
| C-01 | Dual-directory search | Did Step 0 explicitly state findings from both directories? | PASS / FAIL |
| C-02 | MoSCoW structure | Does Step 2 have four named tiers? | PASS / FAIL |
| C-03 | Root blocker named | Does Step 3 name a root blocker with foundational reasoning and blocked IDs? | PASS / FAIL |
| C-04 | Ambiguity flags raised | Does Step 5 have at least one AF- entry? | PASS / FAIL |
| C-05 | Three+ lenses traceable | Are PM, Architect, and UX each traceable in the MoSCoW table? | PASS / FAIL |
| C-06 | Suspicious silences | Does Step 4 include at least one SS- entry? | PASS / FAIL |
| C-07 | SF- findings raised | Does Step 6 include at least one SF- entry? | PASS / FAIL |
| C-08 | Stable IDs + promotions | No ID collisions; tier promotions include justification note? | PASS / FAIL |
| C-09 | Transitive dependency graph | Does Step 3 show second-order chains (A→B→C) with foundational reasoning? | PASS / FAIL |
| C-10 | AF- cites source text | Does each AF- entry include an exact quote from the input? | PASS / FAIL |
| C-11 | Lifecycle phase audit | Does Step 4 name all five phases with coverage status? | PASS / FAIL |
| C-12 | Cross-session continuity | Do AF- and SF- sections carry prior entries with explicit status? | PASS / FAIL |
| C-13 | Two-interpretation AF- format | Does each AF- entry have Interpretation A + B + Consequence? | PASS / FAIL |
| C-14 | Rubric self-check gate | Is this verification table present before the final artifact? | PASS / FAIL |
| C-15 | Law A applied at extraction | Were [AMBIG:] notations generated DURING extraction (Steps 1/4), not introduced fresh in Step 5? | PASS / FAIL |
| C-16 | Law B closure gates | Does each of Steps 5 and 6 contain the explicit closure sentence? | PASS / FAIL |
| C-17 | Three-loop enforcement | Are all three loops present: charter (C-17/Loop1), step reinstatements (C-18/Loop2), this table (C-19/Loop3)? | PASS / FAIL |
| C-18 | Step-level reinstatements | Does each extraction step that triggers Law A or Law B contain an "Apply Law [A/B] here" cross-reference? | PASS / FAIL |
| C-19 | Process-diagnostic rows | Does this table include rows auditing whether laws were applied during extraction (rows C-15 and C-16 above)? | PASS / FAIL |
| C-20 | Prevention-detection complementarity | Does the charter state that C-18 creates artifacts that C-19 requires as evidence? | PASS / FAIL |
| C-21 | Recursive meta-loop naming | Does the charter name C-17 = Loop 1 (declare), C-18 = Loop 2 (apply), C-19 = Loop 3 (verify) by rubric criterion ID? | PASS / FAIL |
| C-22 | Loop 2→3 verbatim design contract | Does the charter contain a named "Loop 2 → Loop 3 Design Contract" section stating the artifact dependency as a structural obligation before execution? | PASS / FAIL |
| C-23 | Per-law independent chains | Does the charter assign independent declare/apply/verify triplets per law (Law A independent from Law B)? | PASS / FAIL |
| C-24 | Structural closure of meta-loop | Does the charter state that C-17's declaration instantiates C-18 as a logical consequence, not a separately mandated addition? | PASS / FAIL |

If any FAIL is present in C-01..C-07 or C-08..C-14, resolve before emitting.

---

Write artifact to: simulations/scout/requirements/{{topic}}-requirements-{{date}}.md
Frontmatter: skill: scout-requirements, topic: {{topic}}, date: {{date}},
             skill_version: 2.0, input: [source spec path]
```

---

## V-05: Full Synthesis (C-21 + C-22 + C-23 + C-24)

**Axes**: Charter topology — all four remaining gaps closed simultaneously
**Hypothesis**: The four gaps interact. C-23 (independent chains) and C-24 (structural closure)
pull in different directions: C-23 wants two separate enforcement units; C-24 wants a single
self-closing declaration. Resolution: the meta-requirement is the single self-closing declaration
(C-24); the per-law chains are its named independent components (C-23). Asserting C-17
simultaneously instantiates both Law A's independent chain AND Law B's independent chain as
structural consequences — the independence is inside the closure, not competing with it.
Combined with C-21 (rubric ID naming) and C-22 (verbatim design contract), this is the
golden candidate. Predicted 122/122.

---

```
You are running /scout-requirements for: {{topic}}

---

## CHARTER — FORMAT LAWS, INDEPENDENT CHAINS, AND STRUCTURAL CLOSURE

This charter is C-17 (Loop 1 / declare) of the three-loop meta-requirement. It declares two
format laws, assigns each an independent enforcement chain, and names the artifact contract
between Loop 2 and Loop 3 as a structural obligation before any extraction begins.

---

### Format Law A: Two-Path AF- Rule

Every ambiguity encountered during extraction carries an inline notation at first encounter:

  [AMBIG: "{exact source text}" → A: {interpretation A} | B: {interpretation B}]

This rule applies AT FIRST ENCOUNTER during extraction steps — not deferred to the AF- section.

**Law A Independent Enforcement Chain**:
- **C-17-A (Loop 1-A / declare)**: Law A declared here, independently of Law B
- **C-18-A (Loop 2-A / apply)**: Steps 1 and 4 contain "Apply Law A here" with full-text
  reinstatement — Law A's apply loop is confined to extraction steps (Steps 1 and 4) only
- **C-19-A (Loop 3-A / verify)**: verification table row C-15 audits Law A application

Law A's chain is independent: a failure in C-18-A cannot cascade to Law B's enforcement.

---

### Format Law B: Downstream Closure Rule

Each downstream findings section (AF-, SF-) contains the following explicit closure statement:

  "Every entry from the prior open [AF- / SF-] register appears in this section
   with a status: open / resolved / out-of-scope."

A section that carries prior findings without this statement fails Law B.

**Law B Independent Enforcement Chain**:
- **C-17-B (Loop 1-B / declare)**: Law B declared here, independently of Law A
- **C-18-B (Loop 2-B / apply)**: Steps 5 and 6 contain "Apply Law B here" with full-text
  reinstatement — Law B's apply loop is confined to findings steps (Steps 5 and 6) only
- **C-19-B (Loop 3-B / verify)**: verification table row C-16 audits Law B application

Law B's chain is independent: a failure in C-18-B cannot cascade to Law A's enforcement.

---

### Three-Loop Meta-Requirement: Structural Closure

The two law chains are unified under one self-closing declaration:

- **C-17 (Loop 1 / declare)** = this charter, including both Law A and Law B independent chains
- **C-18 (Loop 2 / apply)** = the step-level cross-references from both chains, per law
- **C-19 (Loop 3 / verify)** = the pre-output verification protocol

**Structural Closure**: C-17 is structurally incomplete without C-18. Declaring format laws
without an application layer is not enforcement — it is an incomplete declaration. Asserting
C-17 simultaneously instantiates C-18 (both Law A's C-18-A and Law B's C-18-B) as necessary
consequences: the laws have no operative meaning until C-18 executes. C-18 in turn instantiates
C-19: C-18 produces execution artifacts that require verification; C-19 is the structural
completion of C-18's operation. The three-loop system is a single self-closing declaration —
Loop 1 is incomplete without Loop 2; Loop 2 is unverified without Loop 3. Asserting C-17
simultaneously brings C-18 and C-19 into existence as logical consequences.

### Loop 2 → Loop 3 Design Contract

This charter names the following as a structural obligation before execution begins:

**C-18 (Loop 2) creates the execution artifacts that C-19 (Loop 3) requires as evidence.**

- Law A's C-18-A creates inline [AMBIG:] notations during Steps 1 and 4
- Law B's C-18-B creates closure sentences in Steps 5 and 6
- C-19 audits these specific artifacts — not general output structure
- If C-18 is skipped, C-19 has no artifacts to verify

This dependency is chartered here as a design contract, not inferred from structural proximity.
C-18 prevents violations at execution time. C-19 detects violations that slipped through.
C-18's artifacts are C-19's evidence.

---

## STEP 0: DUAL-DIRECTORY SEARCH

Search for prior scout signals in BOTH:
- simulations/scout/ — real runs for {{topic}}
- simulations/trace/skill/ — hand-compiled traces for {{topic}}

State what you found in each directory. If either is empty, say so explicitly.
Never silently skip either directory.

**Apply Law B here (Step 0)** [C-18-B reinstatement]: List all open AF- and SF- entries
from prior runs. State the closure sentence:
  "Every entry from the prior open findings register appears in this step with a status:
   open / resolved / out-of-scope."

SF-01 (undefined search path): CLOSED if trace found in simulations/trace/skill/; otherwise OPEN.

---

## STEP 1: REQUIREMENTS EXTRACTION — FOUR LENSES

**Apply Law A here (Step 1)** [C-18-A reinstatement]: Flag ambiguities inline at first
encounter:

  [AMBIG: "{exact source text}" → A: {what this means for the build} | B: {alternative}]

Apply at first encounter. Do not defer ambiguities to Step 5.

Extract requirements. Assign stable IDs (R-01, R-02, ...), MoSCoW tier, and lens label.

### PM Lens (user-facing)
What behavior does the user expect? What goals does this enable?
[Extract here. Inline [AMBIG:] notations where applicable.]

### Architect Lens (technical)
What structural properties must hold? Platform, deployment, data contracts, constraints?
[Extract here. Inline [AMBIG:] notations where applicable.]

### UX Lens (usability)
First-run experience? Error states? Progressive disclosure?
[Extract here. Inline [AMBIG:] notations where applicable.]

### Compliance Lens (regulatory)
Legal/policy constraints? If none apply, state explicitly.
[Extract here. Inline [AMBIG:] notations where applicable.]

---

## STEP 2: MOSCOW TABLE

Consolidate all requirements from Step 1. No new IDs.

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

Tier promotions: "Promoted R-NN from [tier] to [tier]: [reason]."

---

## STEP 3: DEPENDENCY GRAPH

Name at least one root blocker. State WHY it is foundational — not just that it blocks.
Show second-order chains: R-NN → R-MM → R-PP.

---

## STEP 4: LIFECYCLE PHASE COVERAGE AUDIT

**Apply Law A here (Step 4)** [C-18-A reinstatement]: If a lifecycle phase gap suggests
a missing requirement, flag inline with [AMBIG:] format or raise as an SS- entry.

| Phase | Coverage | SS- entry |
|-------|----------|-----------|
| First-run | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Core-use | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Upgrade / migration | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Error / recovery | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Observability | COVERED / PARTIAL / SILENT | [SS-NN or —] |

---

## STEP 5: AMBIGUITY FLAGS

**Apply Law A here (Step 5)**: This section formalizes all [AMBIG:] notations from
Steps 1 and 4. Do not introduce new ambiguities here for the first time.

**Apply Law B here (Step 5)** [C-18-B reinstatement]: Every entry from the prior open
AF- register must appear below with a status. State the closure sentence:
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

## STEP 6: SPEC-FAULT FINDINGS

**Apply Law B here (Step 6)** [C-18-B reinstatement]: Every entry from the prior open
SF- register must appear below with a status. State the closure sentence:
  "Every entry from the prior open SF- register appears in this section with a status:
   open / resolved / out-of-scope."

**SF-NN: [gap or contradiction in the input spec]**
- Severity: P0 / P1 / P2
- Affected requirements: [R-IDs]
- Status: open / resolved / out-of-scope

[At least one SF- entry expected for a non-trivial input.]

Closure: Every entry from the prior open SF- register appears in this section with a status. ✓

---

## PRE-OUTPUT VERIFICATION PROTOCOL (C-19 / Loop 3 — verify)

Before emitting the final artifact, verify each criterion by ID. This table audits PROCESS
COMPLIANCE — whether format laws were applied during extraction, not only whether sections
are present.

| ID | Criterion | Process check | Status |
|----|-----------|--------------|--------|
| C-01 | Dual-directory search | Did Step 0 explicitly state findings from both directories? | PASS / FAIL |
| C-02 | MoSCoW structure | Does Step 2 have four named tiers (not a flat list)? | PASS / FAIL |
| C-03 | Root blocker named | Does Step 3 name a root blocker with foundational reasoning and blocked IDs? | PASS / FAIL |
| C-04 | Ambiguity flags raised | Does Step 5 have at least one AF- entry? | PASS / FAIL |
| C-05 | Three+ lenses traceable | Are PM, Architect, and UX each traceable in the MoSCoW table? | PASS / FAIL |
| C-06 | Suspicious silences | Does Step 4 include at least one SS- entry (or justify all phases covered)? | PASS / FAIL |
| C-07 | SF- findings raised | Does Step 6 include at least one SF- entry? | PASS / FAIL |
| C-08 | Stable IDs + promotions | No ID collisions; tier promotions include justification note? | PASS / FAIL |
| C-09 | Transitive dependency graph | Does Step 3 show second-order chains (A→B→C) with foundational reasoning? | PASS / FAIL |
| C-10 | AF- cites source text | Does each AF- entry include an exact quote from the input? | PASS / FAIL |
| C-11 | Lifecycle phase audit | Does Step 4 name all five phases with coverage status? | PASS / FAIL |
| C-12 | Cross-session continuity | Do AF- and SF- sections carry prior entries with explicit status? | PASS / FAIL |
| C-13 | Two-interpretation AF- format | Does each AF- entry have Interpretation A + B + Consequence? | PASS / FAIL |
| C-14 | Rubric self-check gate | Is this verification table present before the final artifact? | PASS / FAIL |
| C-15 | Law A applied at extraction (C-19-A) | Were [AMBIG:] notations generated DURING extraction (Steps 1/4), not introduced fresh in Step 5? | PASS / FAIL |
| C-16 | Law B closure gates (C-19-B) | Does each of Steps 5 and 6 contain the explicit closure sentence in exact format? | PASS / FAIL |
| C-17 | Three-loop enforcement | Are all three loops present: charter (C-17/Loop1), step reinstatements (C-18/Loop2), this table (C-19/Loop3)? | PASS / FAIL |
| C-18 | Step-level reinstatements | Does each applicable step contain a per-law "Apply Law [A/B] here" cross-reference with C-18-A/B label? | PASS / FAIL |
| C-19 | Process-diagnostic rows | Does this table include separate rows auditing Law A (C-15) and Law B (C-16) application? | PASS / FAIL |
| C-20 | Prevention-detection complementarity | Does the charter state that C-18 creates artifacts that C-19 requires as evidence? | PASS / FAIL |
| C-21 | Recursive meta-loop naming | Does the charter name C-17 = Loop 1 (declare), C-18 = Loop 2 (apply), C-19 = Loop 3 (verify) by rubric criterion ID within the meta-requirement text? | PASS / FAIL |
| C-22 | Loop 2→3 verbatim design contract | Does the charter contain a named "Loop 2 → Loop 3 Design Contract" section stating C-18's artifact-creation obligation as a structural contract before execution? | PASS / FAIL |
| C-23 | Per-law independent chains | Does the charter assign independent declare/apply/verify triplets per law? Law A's Loop 2 confined to Steps 1/4; Law B's Loop 2 confined to Steps 5/6; neither chain cascades to the other. | PASS / FAIL |
| C-24 | Structural closure of meta-loop | Does the charter state that C-17 is structurally incomplete without C-18 — asserting C-17 simultaneously instantiates C-18 and C-19 as logical consequences, not separately mandated additions? | PASS / FAIL |

If any FAIL is present in C-01..C-07 (essential) or C-08..C-14 (recommended), resolve before
emitting. Aspirational FAILs (C-09..C-24) should be noted but do not block emission.

---

Write artifact to: simulations/scout/requirements/{{topic}}-requirements-{{date}}.md
Frontmatter: skill: scout-requirements, topic: {{topic}}, date: {{date}},
             skill_version: 2.0, input: [source spec path]
```

---

## Variation Design Summary

| Var | Axis | Primary hypothesis | Target criteria | Predicted score |
|-----|------|--------------------|-----------------|-----------------|
| V-01 | Charter self-naming (rubric IDs only) | Adding C-17/C-18/C-19 IDs in meta-requirement closes C-21 alone; no structural change | C-21 PASS | 119/122 |
| V-02 | Structural closure phrasing | Framing C-17 as structurally incomplete without C-18 closes C-24; includes C-21 fix | C-21 + C-24 PASS | 121/122 |
| V-03 | Per-law independent chains | Independent Law A / Law B triplets close C-23; includes C-21 fix; no structural closure | C-21 + C-23 PASS | 121/122 |
| V-04 | C-21 naming + C-22 contract | Rubric IDs + named Design Contract section; C-23/C-24 still open | C-21 + C-22 PASS | 121/122 |
| V-05 | Full synthesis | Per-law independence inside structural closure + naming + contract | C-21 + C-22 + C-23 + C-24 PASS | 122/122 |

**Key discriminators to watch in scoring:**
- V-01: does C-21 require the IDs to appear in the chain descriptions (C-17-A, C-18-A style),
  or is it satisfied by a single line "C-17 (Loop 1 / declare)" in the meta-requirement header?
- V-02 vs V-05: does "structurally incomplete" framing survive intact when combined with per-law
  chain decomposition, or does V-05's chain structure dilute the unified closure argument?
- V-03 vs V-05: V-03's per-law chains (C-23) may conflict with C-17 requirement for a unified
  three-loop structure — does the Meta-Requirement section preserve C-17 adequately?
- V-04 vs V-05: does the named Design Contract section in V-04 satisfy C-22 more cleanly (single
  named section) than V-05's approach (contract embedded within meta-requirement)?
- V-05 central tension: C-23 independence (two separate chains) and C-24 closure (one unified
  declaration) — does "independence inside closure" satisfy both, or does the scorer treat them
  as fundamentally incompatible framings?
