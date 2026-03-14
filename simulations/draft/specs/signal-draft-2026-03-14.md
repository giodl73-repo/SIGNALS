# Draft Specification

**Topic**: sim
**Namespace**: /draft:
**Skills**: 3
**Default mode**: Lightweight
**Audience**: Architects, senior developers, PMs -- anyone who writes the design document that engineering builds from

## Purpose

Draft answers "What exactly are we building?" by producing structured design documents from scout findings and author intent. It turns scattered requirements, competitive context, and compliance constraints into a single coherent artifact -- a spec, a proposal, or a pitch -- so the author stays in flow instead of context-switching between six scout outputs.

## Skills

### /draft:spec

**What**: Produce a structured technical specification from requirements, constraints, and domain context.
**Stock roles**: Architect, PM, Strategy
**Input**: Requirements brief (from /scout:requirements or freeform), optional scout artifacts to pull from, optional spec template
**Output**: Technical specification (plan artifact, Markdown)
**Lifecycle**:
- Setup: Locate prior scout artifacts in the workspace (requirements, feasibility, compliance). If a requirements brief exists, extract R-IDs for traceability. Detect repo conventions for spec formatting (numbered specs like AD-01, named sections, frontmatter style). If no scout artifacts exist, ask the user for a 3-5 sentence product description and extract requirements inline.
- Execute: Architect structures the spec into sections (overview, data model, operations, constraints, error handling, extensibility). PM validates that every P0 requirement from scout:requirements has a corresponding spec section. Strategy validates that competitive differentiation claims are reflected in the design (features competitors lack must appear). Each spec section gets a traceability footer linking back to requirement IDs.
- Findings: Coverage gap report -- requirements with no spec section. Contradiction flags -- places where two requirements conflict in the spec. Complexity hotspots -- spec sections that are disproportionately complex relative to their requirement priority.
- Amend: User can restructure sections, resolve contradictions, add/remove requirements from scope, or change the spec template.
**Lightweight**: Single-pass. Architect writes the spec in one shot. PM and Strategy review inline (annotations, not separate passes). No iterative refinement loop -- the spec is complete on first pass, with findings noted at the bottom for the author to address.
**Artifact**: `draft/spec/sim-spec-{slug}-{date}.md`
**Example**:
```
User: /draft:spec --from scout/requirements/sim-requirements-simulation-plugin-2026-03-14.md
> Loading requirements brief (32 requirements, 12 P0)...
> Pulling feasibility context (35/100 -- scope reduction recommended)...
> Pulling compliance context (4 blocking requirements)...
> Detecting spec conventions from repo... found AD-01 through AD-07 pattern.
>
> ## Specification: Simulation Plugin (SIM-01)
>
> ### 1. Overview
> Design-time simulation engine for validating specs before implementation.
> Codifies hand-compile methodology as a reusable CLI workflow.
>
> ### 2. Data Model
> - Series: 5-letter code, domain binding, wave progression
> - Scenario: intent + input + expected output + status
> - Finding: ID, severity, DCR linkage, resolution status
> - DCR: batched findings, spec amendments, implementation tracking
>
> ### 3. Operations (8)
> | Op | Input | Output | Traces to |
> |----|-------|--------|-----------|
> | series.new | domain, code, focus | Series dir | R-01 |
> | scenario.new | series, wave, intent | Scenario file | R-01 |
> | finding.record | scenario, severity, desc | Finding entry | R-02 |
> | coverage.report | domain | Coverage matrix | R-03 |
> ...
>
> ### Findings
> - Gap: R-14 (versioning) has no spec section -- AMBIGUITY (flagged in scout)
> - Contradiction: R-05 (cross-platform) vs R-22 (Windows-specific relay) -- needs scope decision
> - Hotspot: Section 3 (Operations) covers 8 ops for 12 P0 reqs -- may need splitting
>
> Artifact written: draft/spec/sim-spec-simulation-plugin-2026-03-14.md
```

### /draft:proposal

**What**: Produce a decision proposal that synthesizes scout findings into a go/no-go recommendation with clear options, tradeoffs, and a recommended path.
**Stock roles**: PM, Strategy, Architect
**Input**: Product concept, optional scout artifacts (feasibility, market, stakeholders, compliance)
**Output**: Decision proposal (plan artifact, Markdown)
**Lifecycle**:
- Setup: Locate prior scout artifacts. If feasibility, market, and stakeholder maps exist, pull key findings. If none exist, run an abbreviated inline assessment (lighter than full scout, focused on decision-relevant dimensions only).
- Execute: PM frames the decision (what are we deciding, why now, what happens if we do nothing). Strategy presents 2-4 options with tradeoffs (build, buy, partner, defer). Architect scores each option on technical dimensions (complexity, maintainability, time-to-ship, risk). Synthesize into a recommendation with confidence level (high/medium/low) and conditions ("recommended IF these 3 assumptions hold").
- Findings: Assumption register -- every assumption the recommendation depends on, with a plan to validate each. Risk register -- top 5 risks per option, with probability and impact. Decision criteria -- the 4-6 dimensions that matter most, with weights.
- Amend: User can add options, adjust decision criteria weights, challenge assumptions, or request deeper analysis on a specific option.
**Lightweight**: Single-pass. PM frames, Strategy presents options, Architect scores. No option deep-dive -- top-level comparison only. Recommendation delivered with the matrix, not after iterative deliberation.
**Artifact**: `draft/proposal/sim-proposal-{slug}-{date}.md`
**Example**:
```
User: /draft:proposal "should we build a simulation plugin or extend the existing test framework"
> Pulling scout context: feasibility (35/100), market ($12M SOM), stakeholders (5 mapped)...
>
> ## Decision Proposal: Simulation Capability
>
> **Decision**: How should we deliver design-time simulation to engineering teams?
> **Why now**: 3 teams are doing ad-hoc simulation (375+ scenarios). Methodology is proven but unscalable.
> **Cost of inaction**: Each new simulation campaign takes 2 weeks of setup. Knowledge stays in heads.
>
> ### Options
> | Dimension       | A: Build plugin | B: Extend test FW | C: Buy (Pact.io) | D: Defer 6mo |
> |-----------------|----------------|--------------------|-------------------|---------------|
> | Time to ship    | 3 months       | 1 month            | 2 weeks           | --            |
> | Feature fit     | 95%            | 40%                | 25%               | 0%            |
> | Maintenance     | Medium         | Low                | Low               | None          |
> | Risk            | Medium         | Low                | High (lock-in)    | High (churn)  |
> | Team buy-in     | High           | Medium             | Low               | --            |
>
> **Recommendation**: Option A (Build plugin) -- MEDIUM confidence.
> **Conditions**: (1) Scope to CLI only (no GUI), (2) One architect dedicated 50%,
>   (3) Ship V1 in 6 weeks with 3 commands, full suite at 3 months.
>
> ### Assumption Register
> | # | Assumption | Validation Plan |
> |---|-----------|-----------------|
> | A1 | Teams will adopt CLI-first workflow | Survey 3 team leads (week 1) |
> | A2 | Existing scenario corpus is portable | Migrate 50 scenarios as proof (week 2) |
> | A3 | One architect is available 50% | Confirm with VP Eng (this week) |
```

### /draft:pitch

**What**: Produce a persuasive narrative document that sells a product idea to a specific audience -- investor, executive, partner, or internal stakeholder.
**Stock roles**: Strategy, PM, Architect
**Input**: Product concept, target audience (who is being pitched), optional scout artifacts (positioning, competitors, market)
**Output**: Pitch document (brief artifact, Markdown)
**Lifecycle**:
- Setup: Identify the audience and their decision criteria (investor = ROI + market size, executive = cost + risk, partner = integration + revenue share, internal = productivity + team buy-in). Pull positioning and competitive context from prior scout runs if available.
- Execute: Strategy crafts the narrative arc (problem, insight, solution, proof, ask). PM provides concrete metrics and proof points (scenario counts, time savings, adoption numbers). Architect provides the "how it works" section calibrated to audience technical depth (investors get analogy, architects get architecture diagram, executives get a diagram with dollar signs).
- Findings: Narrative gap analysis -- claims without proof points. Audience calibration check -- jargon level appropriate for target? Ask clarity check -- is the ask specific and actionable?
- Amend: User can adjust the audience, add proof points, change the narrative arc, or strengthen specific claims.
**Lightweight**: Single-pass. Strategy writes the narrative, PM and Architect annotate. No audience testing -- single best pitch for the stated audience. No slide deck generation -- Markdown narrative only.
**Artifact**: `draft/pitch/sim-pitch-{slug}-{date}.md`
**Example**:
```
User: /draft:pitch "simulate plugin" --audience "VP Engineering (internal sponsor)"
> Pulling positioning context from scout:positioning...
> Audience: VP Engineering -- cares about cost, risk, team productivity, headcount.
>
> ## Pitch: Simulate -- Design Bugs Cost 10x More Than Code Bugs
>
> **Problem**: Your teams find 40% of design flaws after implementation starts.
> Each post-implementation design change costs 3 developer-weeks. Last quarter:
> 12 design changes, 36 developer-weeks burned.
>
> **Insight**: Three teams independently invented the same methodology --
> hand-compile expected outputs from specs, track findings, file design changes
> BEFORE writing code. It works (375 scenarios, 120 design bugs caught pre-code).
> But it takes 2 weeks to set up each campaign because there's no tooling.
>
> **Solution**: Simulate -- a CLI plugin that codifies this methodology.
> Setup drops from 2 weeks to 10 minutes. Any team can run design simulations
> on any spec set.
>
> **Proof**: Across 5 projects, simulation caught 120 design bugs that would
> have cost an estimated 60 developer-weeks to fix post-implementation.
> Cost of the simulation campaigns: 8 developer-weeks total. ROI: 7.5x.
>
> **Ask**: One architect at 50% for 3 months. Ship V1 in 6 weeks (3 commands).
> Full suite by month 3. Projected annual savings: 180 developer-weeks.
>
> Artifact written: draft/pitch/sim-pitch-simulate-plugin-2026-03-14.md
```

## Roles

### Stock roles

| Role | What it does in draft |
|------|----------------------|
| Architect | Structures specs into sections, scores options on technical dimensions, provides "how it works" calibrated to audience depth |
| PM | Validates requirement coverage in specs, frames decisions with cost-of-inaction, provides metrics and proof points for pitches |
| Strategy | Validates competitive differentiation in specs, presents options with tradeoffs in proposals, crafts narrative arcs for pitches |

### Custom roles (optional)

- **/draft:spec** benefits from domain-specific architect roles (e.g., "Data Platform Architect" for data-intensive specs, "Security Architect" for security-critical specs) that bring deeper structural conventions.
- **/draft:pitch** benefits from audience-specific roles (e.g., "VC Partner" as a shadow reviewer who flags what an investor would challenge, "CTO" as a shadow reviewer who flags what a technical executive would question).
- **/draft:proposal** benefits from "Devil's Advocate" as a custom role that stress-tests the recommendation and strengthens the assumption register.

## Artifacts

```
draft/
├── spec/
│   └── sim-spec-{slug}-{date}.md
├── proposal/
│   └── sim-proposal-{slug}-{date}.md
└── pitch/
    └── sim-pitch-{slug}-{date}.md
```

All artifacts use the `sim-` topic prefix. Slug is derived from the product concept (lowercased, hyphenated, truncated to 40 chars). Date is ISO 8601 (YYYY-MM-DD).

## Cross-Namespace Integration

- **scout:requirements -> draft:spec**: Requirements brief is the primary input. R-IDs carry through to spec traceability footers. Every P0 requirement must map to a spec section.
- **scout:feasibility -> draft:proposal**: Feasibility score and component-level risk ratings feed directly into option scoring.
- **scout:competitors + scout:positioning -> draft:pitch**: Competitive landscape and positioning statements become the differentiation backbone of the pitch narrative.
- **scout:market -> draft:pitch**: TAM/SAM/SOM numbers and beachhead segment feed into the market opportunity section of investor/executive pitches.
- **scout:stakeholders -> draft:proposal**: Stakeholder power/interest grid informs which options require which stakeholder buy-in.
- **scout:compliance -> draft:spec**: Blocking compliance requirements appear as architectural constraints (non-negotiable design decisions).
- **draft:spec -> listen:feedback**: The spec is the primary artifact that /listen:feedback evaluates from the customer perspective. Findings from listen loop back as spec amendments.
- **draft:proposal -> listen:adoption**: The chosen option from the proposal feeds into adoption simulation -- how will teams actually adopt this?
- **draft:pitch -> listen:feedback**: The pitch narrative is tested against customer personas to validate resonance before delivery.
