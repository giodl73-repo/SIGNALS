Written to `simulations/quest/variations/scout-requirements-variations-R1-2026-03-14.md`.

---

## scout-requirements — Variation Set R1

**5 variations across 3 single axes + 2 combinations:**

| Var | Axis | Hypothesis |
|-----|------|------------|
| **V-01** | Role sequence (PM → Arch → UX → Comp) | Stakeholder-natural order surfaces user value first; SF- findings emerge at lens conflicts rather than being injected |
| **V-02** | Template-completion (pre-printed skeleton) | Pre-printed two-interpretation slots for AF- enforce C-13 without instruction; closure sentences pre-printed enforce C-16 |
| **V-03** | Phrasing register (discovery questions) | "What must be true?" primes gap-finding; model looks for absences rather than filling sections — expects higher C-06/C-07 yield |
| **V-04** | Lifecycle emphasis + inertia framing | Per-requirement lifecycle phase tags make SS- gaps visible by construction (every SILENT phase is a zero-coverage cell); Won't Have tier grounded in workaround cost |
| **V-05** | Template + three-loop enforcement | Charter names Loop 1 (declare) / Loop 2 (apply) / Loop 3 (verify) making step-level reinstatements non-skippable by self-reference; targets C-14 through C-21 |

**Key discriminators to watch in scoring:**
- V-01 vs V-03: imperative role sequence vs. discovery questions — which produces more AF- and SF- entries?
- V-02 vs V-05: pre-printed template alone vs. template + three-loop machinery — can C-13/C-16 be guaranteed without the charter?
- V-04: does lifecycle tagging implicitly satisfy C-11 better than an explicit phase audit instruction?
- V-05: does the three-loop charter survive as a coherent structure or introduce compliance overhead that degrades essential section quality?
e / Won't Have.

---

## Step 2: Architect Lens — Technical Requirements

Role: Architect (what must be true structurally for this product to function?)

Extract technical requirements:
- System constraints (platform, deployment model, CLI-only, zero-config, etc.)
- Integration points with existing systems
- Data contract and artifact structure requirements
- Performance or scale constraints

Continue MoSCoW assignment. Note any requirements the PM lens did not surface.

---

## Step 3: UX Lens — Usability Requirements

Role: UX (how does this product behave from a user's moment-to-moment experience?)

Extract usability requirements:
- First-run experience
- Error states and recovery paths
- Progressive disclosure and onboarding
- Output readability and navigation

---

## Step 4: Compliance Lens — Regulatory Requirements

Role: Compliance (what must be true for legal, policy, or organizational reasons?)

Extract compliance requirements. If no compliance requirements apply, state that explicitly —
do not silently omit the lens.

---

## Step 5: MoSCoW Table

Combine outputs from all four roles into a single prioritized table with stable IDs (R-01, R-02, ...).

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

If any requirement is promoted from a lower tier based on a finding, note:
"Promoted R-NN from [tier] to [tier]: [reason]."

---

## Step 6: Dependency Graph

Identify which requirements block others. Name at least one root blocker.
For each blocker, list what it blocks directly and transitively:

  R-NN (root) → R-MM → R-PP

Second-order chains required. State why the root blocker is foundational — not just that
it blocks.

---

## Step 7: Ambiguity Flags

For each requirement where two reasonable interpretations exist, raise an AF- entry:

**AF-NN: [requirement ID or spec phrase]**
- Source: "[exact text from input]"
- Interpretation A: [what one team would build]
- Interpretation B: [what a different team would build]
- Consequence: [how the product diverges between A and B]
- Status: open / resolved / out-of-scope

Carry forward all AF- from prior runs. Zero AF- on a complex input is a fail.

---

## Step 8: Suspicious Silences

What areas have no requirements? Enumerate these lifecycle phases and assign coverage:

| Phase | Coverage | SS- entry |
|-------|----------|-----------|
| First-run | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Core-use | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Upgrade / migration | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Error / recovery | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Observability / logging | COVERED / PARTIAL / SILENT | [SS-NN or —] |

---

## Step 9: Spec-Fault Findings

Identify gaps, contradictions, or undefined behaviors in the input spec:

**SF-NN: [what is missing or contradictory]**
- Severity: P0 / P1 / P2
- Affected requirements: [R-IDs]
- Status: open / resolved / out-of-scope

Carry forward all SF- from prior runs.

---

Write the artifact to: simulations/scout/requirements/{{topic}}-requirements-{{date}}.md
Frontmatter: skill: scout-requirements, topic, date, skill_version, input.
```

---

## V-02: Template-Completion Output Format

**Axis**: Output format — pre-printed skeleton with [FIELD] completion slots
**Hypothesis**: Pre-printing the output structure (MoSCoW tables with Lens column, AF- entry
format with two-interpretation slots, SS- lifecycle table, closure sentences) forces correct
structure regardless of model behavior drift. The model cannot drop or reformat what it did
not generate. Targets C-10 (AF- cites source) and C-13 (two-interpretation format) through
pre-printed slot structure.

---

```
You are running /scout-requirements for: {{topic}}

Fill in all [FIELD] values. Do not omit any pre-printed section or row.
Do not reformat pre-printed headers.

---

## SEARCH GATE

Searched: simulations/scout/ for {{topic}} — [RESULT: files found / empty]
Searched: simulations/trace/skill/ for {{topic}} — [RESULT: files found / empty]

SF-01 status: [CLOSED — trace found / OPEN — no trace found]
Prior AF- carried forward: [list IDs, or "none"]
Prior SF- carried forward: [list IDs, or "none"]

---

## MUST HAVE

| ID | Lens | Requirement | Blocks |
|----|------|-------------|--------|
| R-01 | [PM / Arch / UX / Comp] | [requirement] | [R-IDs or —] |
| R-02 | [PM / Arch / UX / Comp] | [requirement] | [R-IDs or —] |
| [add rows as needed] | | | |

---

## SHOULD HAVE

| ID | Lens | Requirement | Blocks |
|----|------|-------------|--------|
| R-[NN] | [PM / Arch / UX / Comp] | [requirement] | [R-IDs or —] |
| [add rows as needed] | | | |

---

## COULD HAVE

| ID | Lens | Requirement | Blocks |
|----|------|-------------|--------|
| R-[NN] | [PM / Arch / UX / Comp] | [requirement] | [R-IDs or —] |
| [add rows as needed] | | | |

---

## WON'T HAVE

| ID | Lens | Requirement | Note |
|----|------|-------------|------|
| R-[NN] | [PM / Arch / UX / Comp] | [requirement] | [why deferred or status-quo alternative] |
| [add rows as needed] | | | |

---

## DEPENDENCY ROOT

Root blocker: R-[NN] — [requirement text]
Why foundational: [why this blocks everything else]
Blocks directly: [R-IDs]
Blocks transitively: [R-IDs via chain R-NN → R-MM → R-PP]

[Additional blockers:]
Blocker: R-[NN] — [requirement text]
Blocks directly: [R-IDs]

---

## AMBIGUITY FLAGS

All prior AF- entries must appear below with a status.

**AF-01: [requirement ID or spec phrase]**
- Source: "[exact quote from input spec]"
- Interpretation A: [what team A would build]
- Interpretation B: [what team B would build]
- Consequence: [how the product diverges between A and B]
- Status: open / resolved / out-of-scope

**AF-02: [requirement ID or spec phrase]**
- Source: "[exact quote from input spec]"
- Interpretation A: [what team A would build]
- Interpretation B: [what team B would build]
- Consequence: [how the product diverges between A and B]
- Status: open / resolved / out-of-scope

[Add AF- entries as needed. Zero AF- on a complex input is a fail.]

Closure: Every entry from the prior AF- register appears above with a status. ✓

---

## SUSPICIOUS SILENCES

| Phase | Coverage | SS- entry |
|-------|----------|-----------|
| First-run | COVERED / PARTIAL / SILENT | [SS-NN: description, or —] |
| Core-use | COVERED / PARTIAL / SILENT | [SS-NN: description, or —] |
| Upgrade / migration | COVERED / PARTIAL / SILENT | [SS-NN: description, or —] |
| Error / recovery | COVERED / PARTIAL / SILENT | [SS-NN: description, or —] |
| Observability / logging | COVERED / PARTIAL / SILENT | [SS-NN: description, or —] |

---

## SPEC-FAULT FINDINGS

All prior SF- entries must appear below with a status.

**SF-NN: [gap or contradiction in the input spec]**
- Severity: P0 / P1 / P2
- Affected: [R-IDs]
- Status: open / resolved / out-of-scope

[Add SF- entries as needed. At least one expected for a non-trivial input.]

Closure: Every entry from the prior SF- register appears above with a status. ✓

---

## TIER PROMOTIONS

| ID | Promoted from | Promoted to | Reason |
|----|--------------|-------------|--------|
| [R-NN or "No promotions this run"] | | | |

---

Write artifact to: simulations/scout/requirements/{{topic}}-requirements-{{date}}.md
Frontmatter: skill: scout-requirements, topic, date, skill_version, input.
```

---

## V-03: Discovery Register (Questioning Phrasing)

**Axis**: Phrasing register — discovery questions instead of imperatives
**Hypothesis**: Framing extraction as a series of discovery questions produces more thorough
coverage than an imperative checklist. The model surfaces requirements by answering "what
must be true?" rather than executing "extract requirements." More natural path to C-04
(ambiguity flags) and C-06 (suspicious silences) because the questions prime the model to
look for gaps rather than only fill a template.

---

```
You are running /scout-requirements for: {{topic}}

This skill works through discovery questions. Answer each question fully before moving to
the next. The final output is assembled from your answers.

---

**Before you start: What has already been thought about this topic?**

Search simulations/scout/ for files related to {{topic}}. State what you find.
Search simulations/trace/skill/ for files related to {{topic}}. State what you find.
Do not skip either directory — if one is empty, say so.

If prior runs had open findings (AF- or SF-), list them now. They must appear in
Questions 6 and 7 with a status.

---

**Q1: What must be true for this product to exist at all?**

These are your Must Have requirements. Think from the user's perspective first: what
behavior would a user notice immediately if absent? Then think from the Architect's
perspective: what structural properties are non-negotiable?

List each as a requirement with an ID (R-01, R-02, ...) and a lens label
(PM / Architect / UX / Compliance).

---

**Q2: What would users complain about in the first week if missing?**

These are your Should Have requirements — high value but not blocking launch. Same
lens labels. Add to the requirement list.

---

**Q3: What would make this product notably better, but teams could ship without?**

These are your Could Have requirements.

---

**Q4: What are teams currently doing instead of this feature?**

These are your Won't Have requirements — and they reveal the status quo. For each: what
is the manual workaround? What does it cost teams per sprint?

---

**Q5: Which requirements block others?**

Draw the dependency map. Start from the root: what single requirement, if absent, makes
the most other requirements impossible? Name it and explain why it is foundational.
List what it blocks directly, then what those block transitively:

  R-NN → R-MM → R-PP

Second-order chains are required.

---

**Q6: Where are you unsure what was meant?**

For each ambiguous requirement or spec phrase: what are the two most plausible
interpretations? What would two different teams build?

Raise an AF- entry for each:

**AF-NN: [source phrase]**
- Source: "[exact text from input]"
- Interpretation A: [what team A builds]
- Interpretation B: [what team B builds]
- Consequence: [how the product diverges]
- Status: open / resolved / out-of-scope

Cite exact source text for each. If prior runs had open AF- entries, they must appear
here with a status: open / resolved / out-of-scope.

---

**Q7: Where does the input spec let you down?**

What gaps, contradictions, or undefined behaviors did you find in the spec itself?
For each, raise an SF- entry:

**SF-NN: [what is missing or contradictory]**
- Severity: P0 / P1 / P2
- Affected requirements: [R-IDs]
- Status: open / resolved / out-of-scope

If prior runs had open SF- entries, they must appear here with a status.

---

**Q8: What topics have no requirements at all?**

Walk through these lifecycle phases and ask: does any requirement cover this phase?

| Phase | Coverage | SS- entry |
|-------|----------|-----------|
| First-run | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Core-use | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Upgrade / migration | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Error / recovery | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Observability / logging | COVERED / PARTIAL / SILENT | [SS-NN or —] |

For each SILENT phase, raise an SS- entry explaining what is missing.

---

Now assemble the complete output from your answers above:

1. Search results (both directories, SF-01 status)
2. MoSCoW table (all requirements from Q1-Q4, all lenses, stable IDs)
3. Dependency graph from Q5 (root blocker + transitive chains)
4. Ambiguity flags from Q6 (AF- with two interpretations each, source cites)
5. Suspicious silences from Q8 (lifecycle phase table + SS- entries)
6. Spec-fault findings from Q7 (SF- entries)

Write to: simulations/scout/requirements/{{topic}}-requirements-{{date}}.md
Frontmatter: skill: scout-requirements, topic, date, skill_version, input.
```

---

## V-04: Lifecycle Emphasis + Inertia Framing

**Axes**: Lifecycle emphasis + inertia framing (combination)
**Hypothesis**: Tagging every requirement with a lifecycle phase (first-run / core-use /
upgrade / error / observability) makes SS- gaps structurally visible — a lifecycle with
no requirements cannot hide. Inertia framing in the Won't Have tier grounds prioritization
in comparative value rather than abstract priority: "we're not building this" must be
justified against the cost of the status-quo workaround. These two axes reinforce C-11
(named lifecycle phase audit for SS-) and enrich C-03/C-09 (blocker rationale grounded
in workaround cost).

---

```
You are running /scout-requirements for: {{topic}}

## Framing: Requirements as Lifecycle Coverage

This run treats requirements as lifecycle coverage claims. Every requirement answers:
"What must be true at which point in the user's journey?"

Lifecycle phases:
  1. First-run — user encounters the feature for the first time
  2. Core-use — recurring daily/weekly use patterns
  3. Upgrade/migration — evolving from a prior state (or from nothing)
  4. Error/recovery — when things go wrong
  5. Observability — what can teams see about how the feature is working?

Every requirement is tagged with its primary lifecycle phase. A phase with no requirements
is a suspicious silence by definition.

## Framing: Inertia as the Default Competitor

Before prioritizing requirements, ask: what do teams do today without this feature?
The "Won't Have" tier is not just deferred scope — it is where the status quo wins.
For each Won't Have requirement:
- What is the current workaround?
- What does it cost per sprint (time estimate or quality risk)?

This grounds MoSCoW in comparative value, not abstract priority.

---

## Step 0: Prior Context Search

Search for prior scout signals in BOTH:
- simulations/scout/ — real runs for {{topic}}
- simulations/trace/skill/ — hand-compiled traces for {{topic}}

State what you found in each. If either is empty, say so explicitly.

SF-01 status: CLOSED if trace found in simulations/trace/skill/; otherwise OPEN.

Carry forward all open AF- and SF- entries with status: open / resolved / out-of-scope.

---

## Step 1: Lens Extraction (with lifecycle tags)

Run each lens. Tag each requirement with its primary lifecycle phase.

### PM Lens (user-facing)
What does the user need? What user goals does this enable?

| ID | Phase | Requirement | MoSCoW |
|----|-------|-------------|--------|

### Architect Lens (technical)
What structural properties must hold? Platform, deployment, data contracts, constraints?

| ID | Phase | Requirement | MoSCoW |
|----|-------|-------------|--------|

### UX Lens (usability)
How does the product behave moment-to-moment? First impressions, errors, recovery?

| ID | Phase | Requirement | MoSCoW |
|----|-------|-------------|--------|

### Compliance Lens (regulatory)
What must be true for legal/policy reasons? If none apply, state explicitly.

| ID | Phase | Requirement | MoSCoW |
|----|-------|-------------|--------|

---

## Step 2: MoSCoW Table (consolidated, with lifecycle tags)

### Must Have
| ID | Lens | Phase | Requirement | Blocks |
|----|------|-------|-------------|--------|

### Should Have
| ID | Lens | Phase | Requirement | Blocks |
|----|------|-------|-------------|--------|

### Could Have
| ID | Lens | Phase | Requirement | Blocks |
|----|------|-------|-------------|--------|

### Won't Have (with inertia)
| ID | Lens | Phase | Requirement | Status-quo workaround | Cost/sprint |
|----|------|-------|-------------|----------------------|-------------|

Tier promotions: "Promoted R-NN from [tier] to [tier]: [reason]."

---

## Step 3: Lifecycle Phase Coverage Audit

For each phase: COVERED (requirements present across 2+ lenses), PARTIAL (single lens or
single requirement), or SILENT (no requirements).

| Phase | Coverage | SS- entry |
|-------|----------|-----------|
| First-run | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Core-use | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Upgrade / migration | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Error / recovery | COVERED / PARTIAL / SILENT | [SS-NN or —] |
| Observability | COVERED / PARTIAL / SILENT | [SS-NN or —] |

---

## Step 4: Dependency Graph

Name at least one root blocker. State why it is foundational.
Show transitive chains: R-NN → R-MM → R-PP.

Where relevant, note whether blocking a requirement also preserves a status-quo workaround
cost — the root blocker's inertia consequence.

---

## Step 5: Ambiguity Flags

For each ambiguous requirement, raise an AF- entry:

**AF-NN: [requirement ID or spec phrase]**
- Source: "[exact quote from input spec]"
- Interpretation A: [what team A would build]
- Interpretation B: [what team B would build]
- Consequence: [how the product diverges between A and B]
- Status: open / resolved / out-of-scope

All prior AF- entries must appear here with a status.

---

## Step 6: Spec-Fault Findings

**SF-NN: [gap or contradiction in the input spec]**
- Severity: P0 / P1 / P2
- Affected: [R-IDs]
- Status: open / resolved / out-of-scope

All prior SF- entries must appear here with a status.

---

Write artifact to: simulations/scout/requirements/{{topic}}-requirements-{{date}}.md
Frontmatter: skill: scout-requirements, topic, date, skill_version, input.
```

---

## V-05: Golden Synthesis (Template + Three-Loop Enforcement)

**Axes**: Template-completion + PM-first role sequence + three-loop constraint enforcement
**Hypothesis**: Three structural layers eliminate independent failure modes. (1) Pre-printed
template surface prevents section omission and header reformatting. (2) A preamble charter
declares two format laws and names itself as Loop 1 (declare) of the three-loop
meta-requirement — making Loop 2 non-skippable by self-reference. (3) Step-level
cross-references reinstate each law at the step that triggers it (Loop 2 / apply). (4) A
pre-output verification table audits process compliance, not just output structure (Loop 3 /
verify). Targets all aspirational criteria C-09 through C-21.

---

```
You are running /scout-requirements for: {{topic}}

---

## CHARTER — FORMAT LAWS AND THREE-LOOP META-REQUIREMENT

This charter is Loop 1 (declare) of the three-loop meta-requirement. It declares two format
laws before any extraction begins.

### Format Law A: Two-Path AF- Rule

Every ambiguity encountered during extraction carries an inline notation at first encounter:

  [AMBIG: "{exact source text}" → A: {interpretation A} | B: {interpretation B}]

This rule applies AT FIRST ENCOUNTER during extraction steps — not deferred to the AF-
section. The AF- section formalizes inline notations already created; it does not produce
new ambiguity work for the first time.

### Format Law B: Downstream Closure Rule

Each downstream findings section (AF-, SF-) contains the following explicit closure
statement:

  "Every entry from the prior open [AF- / SF-] register appears in this section
   with a status: open / resolved / out-of-scope."

A section that carries prior findings forward without this statement fails Law B.

### Three-Loop Meta-Requirement

Laws A and B are enforced via three loops simultaneously:

- Loop 1 (declare): this charter — laws stated before extraction begins
- Loop 2 (apply): step-level cross-references — each extraction step that triggers a law
  contains an explicit "Apply Law [A/B] here" reinstatement in full text
- Loop 3 (verify): the pre-output verification protocol — a table auditing whether each
  law was applied during extraction, not merely whether sections are present

Loop 2 is non-skippable. Loop 1 names Loop 2 as the apply layer. A model that satisfies
Loop 1 while skipping Loop 2 contradicts this charter's structure.

**Prevention-Detection Complementarity**: Loop 2 creates the execution artifacts — inline
[AMBIG:] notations and closure sentences — that Loop 3 requires as evidence. Loop 2
prevents violations at extraction time. Loop 3 detects any violations that slipped through.
The two layers are designed as a linked system: Loop 2's artifacts are Loop 3's evidence.

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

Enumerate five named phases and assign coverage:

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

## PRE-OUTPUT VERIFICATION PROTOCOL (Loop 3 — verify)

Before emitting the final artifact, verify each criterion by ID. This table audits
PROCESS COMPLIANCE — whether format laws were applied during extraction, not only whether
sections are present in the final output.

| ID | Criterion | Process check | Status |
|----|-----------|--------------|--------|
| C-01 | Dual-directory search | Did Step 0 explicitly state findings from both directories? | PASS / FAIL |
| C-02 | MoSCoW structure | Does Step 2 have four named tiers (not a flat list)? | PASS / FAIL |
| C-03 | Root blocker named | Does Step 3 name a root blocker with blocked IDs listed? | PASS / FAIL |
| C-04 | Ambiguity flags raised | Does Step 5 have at least one AF- entry? | PASS / FAIL |
| C-05 | Three+ lenses traceable | Are PM, Architect, and UX each traceable in the MoSCoW table? | PASS / FAIL |
| C-06 | Suspicious silences | Does Step 4 include at least one SS- entry (or justify why all phases are covered)? | PASS / FAIL |
| C-07 | SF- findings raised | Does Step 6 include at least one SF- entry? | PASS / FAIL |
| C-08 | Stable IDs + promotions | No ID collisions; any tier promotions include justification note? | PASS / FAIL |
| C-09 | Transitive dependency graph | Does Step 3 show second-order chains (A→B→C) with foundational reasoning? | PASS / FAIL |
| C-10 | AF- cites source text | Does each AF- entry include an exact quote from the input? | PASS / FAIL |
| C-11 | Lifecycle phase audit | Does Step 4 name all five phases with coverage status? | PASS / FAIL |
| C-12 | Cross-session continuity | Do AF- and SF- sections carry prior entries with explicit status? | PASS / FAIL |
| C-13 | Two-interpretation AF- format | Does each AF- entry have Interpretation A + B + Consequence? | PASS / FAIL |
| C-14 | Rubric self-check gate | Is this verification table present before the final artifact? | PASS / FAIL |
| C-15 | Law A applied at extraction | Were [AMBIG:] notations generated DURING extraction (Steps 1/4), not introduced fresh in Step 5? | PASS / FAIL |
| C-16 | Law B closure gates | Does each of Steps 5 and 6 contain the explicit closure sentence? | PASS / FAIL |
| C-17 | Three-loop enforcement | Are all three loops present: charter (Loop 1), step reinstatements (Loop 2), this table (Loop 3)? | PASS / FAIL |
| C-18 | Step-level reinstatements | Does each extraction step that triggers Law A or Law B contain an "Apply Law [A/B] here" cross-reference? | PASS / FAIL |
| C-19 | Process-diagnostic rows | Does this table include rows auditing whether laws were applied during extraction (rows C-15 and C-16 above)? | PASS / FAIL |
| C-20 | Prevention-detection complementarity | Does the charter explicitly state that Loop 2 creates artifacts that Loop 3 requires as evidence? | PASS / FAIL |
| C-21 | Recursive meta-loop naming | Does the charter name Loop 1 = declare (charter), Loop 2 = apply (step reinstatements), Loop 3 = verify (this table) — making Loop 2 non-skippable by self-reference? | PASS / FAIL |

If any FAIL is present in C-01..C-07 (essential) or C-08..C-14 (recommended), resolve before
emitting. Aspirational FAILs (C-09..C-21) should be noted but do not block emission.

---

Write artifact to: simulations/scout/requirements/{{topic}}-requirements-{{date}}.md
Frontmatter: skill: scout-requirements, topic: {{topic}}, date: {{date}},
             skill_version: 1.0, input: [source spec path]
```

---

## Variation Design Summary

| Var | Axis | Primary hypothesis | Targeted criteria |
|-----|------|--------------------|-------------------|
| V-01 | Role sequence (PM-first) | Stakeholder-natural order surfaces user value first; SF- arise at lens conflicts | C-05 (structural), C-07 |
| V-02 | Output format (template-completion) | Pre-printed slots prevent AF- structure drift; two-interpretation slots enforce C-13 without instruction | C-10, C-13, C-16 |
| V-03 | Phrasing register (discovery/questioning) | Discovery questions prime gap-finding; model looks for absences rather than filling sections | C-04, C-06, C-07 |
| V-04 | Lifecycle emphasis + inertia framing | Lifecycle phase tags make SS- gaps visible by construction; inertia grounds Won't Have in cost | C-11, C-03 (blocker depth) |
| V-05 | Template + three-loop enforcement | Three structural layers eliminate independent failure modes: charter (Loop 1), inline reinstatements (Loop 2), process-audit table (Loop 3) | C-14 through C-21 |

**Single-axis discriminators to watch in scoring:**
- V-01 vs others: does PM-first role ordering produce richer R- assignments than interleaved extraction?
- V-02 vs others: do pre-printed two-interpretation slots produce structurally correct AF- without the three-loop machinery?
- V-03 vs others: does questioning phrasing surface more SS- and SF- entries (C-06, C-07) than imperative instructions?
- V-04: does lifecycle tagging eliminate the need for a dedicated SS- section (C-11 is implicit in the table)?
- V-05: can the three-loop meta-requirement survive as a complete structure, or does it generate compliance overhead that degrades essential section quality?
