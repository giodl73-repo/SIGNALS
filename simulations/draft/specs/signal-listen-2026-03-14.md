# Listen Specification

**Topic**: sim
**Namespace**: /listen:
**Skills**: 3
**Default mode**: Lightweight
**Audience**: PMs, UX researchers, support leads, team leads -- anyone who needs to anticipate customer reactions before shipping

## Purpose

Listen answers "What will customers say?" by simulating post-ship feedback from diverse personas before the product ships. It turns a spec or design document into a synthetic customer feedback corpus, surfacing adoption friction, support ticket patterns, and persona-specific objections that would otherwise take months to discover organically.

## Skills

### /listen:feedback

**What**: Simulate customer reactions to a spec or design by running 12 customer personas through the proposed experience and collecting their unfiltered feedback.
**Stock roles**: 12 customer personas (C-01 through C-12), PM, UX
**Input**: Spec, design document, or feature description to evaluate. Optional: subset of personas to focus on, specific aspects to probe.
**Output**: Customer feedback report (report artifact, Markdown)
**Lifecycle**:
- Setup: Load the 12 customer personas (C-01 Maria Chen through C-12 Frank Hoffmann). Each persona has a defined role, industry, technical depth, primary concern, mental model, key question, and blind spot. Read the target spec/design. For each persona, identify the 2-3 sections most relevant to their role and concern. If the user specifies a persona subset, scope to those personas only.
- Execute: Each persona reads the spec through their lens and produces feedback in their voice. Maria Chen (C-01, Maker) asks "Can I do this without reading a manual?" and flags jargon. James Okafor (C-02, Developer) asks "Where is the type system?" and flags missing schemas. Priya Sharma (C-03, Architect) asks "What is the formal grammar?" and flags portability gaps. David Kim (C-04, PM) asks "How do I coordinate my team around this?" and flags workflow gaps. All 12 personas contribute. PM synthesizes cross-persona themes. UX identifies friction patterns that appear across 3+ personas.
- Findings: Per-persona feedback cards (2-4 findings each). Cross-persona theme matrix (themes x personas who raised them). Severity classification: blocking (persona cannot complete their primary task), major (persona can complete but with significant friction), minor (persona notices but works around), cosmetic (persona has a preference). Net Promoter prediction per persona (would they recommend this? 1-10).
- Amend: User can add custom personas, focus on specific personas, request deeper analysis on a specific theme, or re-run after spec amendments to see if findings are resolved.
**Lightweight**: All 12 personas evaluate in a single pass. No iterative persona dialogue -- each persona gives feedback once. PM and UX synthesize inline. Theme matrix is computed, not deliberated.
**Artifact**: `listen/feedback/sim-feedback-{slug}-{date}.md`
**Example**:
```
User: /listen:feedback --spec draft/spec/sim-spec-simulation-plugin-2026-03-14.md
> Loading 12 customer personas...
> Reading spec: Simulation Plugin (SIM-01), 8 operations, 32 requirements...
>
> ## Persona Feedback
>
> ### C-01: Maria Chen (Maker, Low Tech)
> **Reaction**: "I don't understand what 'hand-compile expected output' means.
>   Is this for developers only? The setup looks like I need to know what a
>   'series code' is before I can start. I would close this doc."
> **Findings**:
> - F-01: "Hand-compile" jargon is blocking for non-technical users (BLOCKING)
> - F-02: No guided wizard or template selection for first-time users (MAJOR)
> **NPS**: 3/10
>
> ### C-02: James Okafor (Developer, High Tech)
> **Reaction**: "Where are the TypeScript types? I see Markdown everywhere but
>   no programmatic API. I want to import scenario results into my test runner,
>   not read Markdown files. Also, 5-letter codes? Just use UUIDs."
> **Findings**:
> - F-03: No programmatic API -- CLI/Markdown only (MAJOR)
> - F-04: 5-letter codes feel arbitrary; no explanation of why not UUIDs (MINOR)
> **NPS**: 6/10
>
> ### C-03: Priya Sharma (Architect, High Tech)
> **Reaction**: "The expansion model is unclear. What guarantees deterministic
>   output across runs? I need to understand idempotency before I approve this
>   for my teams. Also, how does this integrate with our existing ADR process?"
> **Findings**:
> - F-05: No determinism/idempotency guarantees documented (MAJOR)
> - F-06: No ADR/RFC integration pattern (MINOR)
> **NPS**: 7/10
>
> ### C-04: David Kim (PM, Medium Tech)
> **Reaction**: "I love the coverage reports. But how do I assign scenarios
>   to team members? There's no collaboration model. And the wave complexity
>   gradient -- who decides what wave we're on?"
> **Findings**:
> - F-07: No multi-user assignment or collaboration model (MAJOR)
> - F-08: Wave progression criteria are implicit, not documented (MINOR)
> **NPS**: 7/10
>
> ... [C-05 through C-12 continue] ...
>
> ## Cross-Persona Themes
> | Theme                        | Personas    | Severity | Count |
> |------------------------------|-------------|----------|-------|
> | Jargon barrier               | C-01,06,07  | BLOCKING | 3     |
> | No programmatic API          | C-02,09,10  | MAJOR    | 3     |
> | Collaboration model missing  | C-04,08,11  | MAJOR    | 3     |
> | Onboarding/first-run unclear | C-01,04,07  | MAJOR    | 3     |
>
> Aggregate NPS: 5.8/10 (below 7.0 threshold -- spec needs revision).
> Artifact written: listen/feedback/sim-feedback-simulation-plugin-2026-03-14.md
```

### /listen:support

**What**: Predict the top support tickets that will be filed in the first 90 days after shipping, ranked by volume and severity.
**Stock roles**: Support, SRE, PM, UX, 12 customer personas (background)
**Input**: Spec or shipped feature description. Optional: deployment context (SaaS, on-prem, hybrid), user base size estimate.
**Output**: Support ticket forecast (report artifact, Markdown)
**Lifecycle**:
- Setup: Read the spec/feature description. Identify failure modes from the design (error states, edge cases, ambiguous behaviors, missing defaults). Cross-reference with the 12 customer personas to identify which personas are most likely to file tickets (low-tech personas file "how do I" tickets, high-tech personas file "this doesn't work as documented" tickets).
- Execute: Support role generates the top 15-20 predicted tickets, each with: title, category (how-to, bug, feature-request, config-issue, integration), persona most likely to file it, predicted volume (high/medium/low), severity (P0-P3), and a sample ticket body written in the persona's voice. SRE identifies operational tickets (performance, reliability, monitoring gaps). PM identifies tickets that indicate missing features vs. missing docs. UX identifies tickets that indicate UX friction vs. actual bugs.
- Findings: Ticket forecast ranked by predicted volume. Category breakdown (how-to vs. bug vs. feature-request). Documentation gaps -- tickets that would be prevented by better docs. Design gaps -- tickets that indicate a missing feature or broken workflow. Operational gaps -- tickets that indicate monitoring/alerting blind spots.
- Amend: User can adjust the user base estimate, add deployment context, focus on a specific ticket category, or request deeper analysis on a specific predicted ticket.
**Lightweight**: Single-pass. Support role generates all tickets, others annotate inline. No ticket simulation dialogue -- predictions only. No priority negotiation -- ranked by predicted volume.
**Artifact**: `listen/support/sim-support-{slug}-{date}.md`
**Example**:
```
User: /listen:support --spec draft/spec/sim-spec-simulation-plugin-2026-03-14.md --users 500
> Reading spec... identifying failure modes and edge cases...
> Cross-referencing 12 personas for ticket propensity...
>
> ## Support Ticket Forecast (first 90 days, 500 users)
>
> ### Predicted Volume: 340 tickets (0.68 per user)
>
> | Rank | Title | Category | Persona | Volume | Sev |
> |------|-------|----------|---------|--------|-----|
> | 1 | "What is a series code?" | how-to | C-01 | HIGH | P3 |
> | 2 | "Scenario status stuck on in-progress" | bug | C-02 | HIGH | P2 |
> | 3 | "Coverage report doesn't include my test dir" | config | C-09 | MED | P2 |
> | 4 | "How do I share findings with my team?" | feature-req | C-04 | MED | P3 |
> | 5 | "Finding IDs collide across series" | bug | C-03 | MED | P1 |
> | 6 | "CLI hangs on large repos (>10k files)" | perf | C-09 | MED | P1 |
> | 7 | "Can I run simulations in CI/CD?" | how-to | C-02 | MED | P3 |
> | 8 | "DCR format doesn't match our ADR template" | feature-req | C-03 | LOW | P3 |
> ...
>
> ### Sample Ticket Body (Rank 1)
> **From**: Maria Chen (Ops Manager, RetailCo)
> **Subject**: What is a series code and how do I pick one?
> "I ran `simulate series new` and it asked me for a 5-letter code. The docs
> say 'register a series code in the CODEX' but I don't know what a CODEX is
> or where to find it. I tried typing 'test1' but it said 'must be exactly
> 5 letters.' I just want to test my workflow spec. Can you help?"
>
> ### Gap Analysis
> - Documentation gaps: 8 tickets preventable with better onboarding docs
> - Design gaps: 3 tickets indicate missing features (collaboration, CI mode, ADR integration)
> - Operational gaps: 2 tickets indicate missing perf monitoring
>
> Artifact written: listen/support/sim-support-simulation-plugin-2026-03-14.md
```

### /listen:adoption

**What**: Simulate the adoption curve for a feature across team archetypes, predicting who adopts first, who resists, and what interventions accelerate adoption.
**Stock roles**: PM, UX, 12 customer personas, Support, SRE
**Input**: Feature description or shipped spec, target org context (team count, culture, existing tools). Optional: rollout strategy (big-bang, phased, opt-in).
**Output**: Adoption simulation report (report artifact, Markdown)
**Lifecycle**:
- Setup: Map the 12 customer personas onto adoption archetypes (innovator, early adopter, early majority, late majority, laggard -- Rogers' diffusion curve). Identify each persona's switching cost (what they use today, how painful the switch is). Identify adoption triggers (what event causes them to try) and adoption blockers (what stops them from continuing).
- Execute: Simulate a 6-month adoption timeline. Month 1: who tries it first and why (innovators + early adopters). Month 2-3: what word-of-mouth signals emerge. Month 4-6: what makes the early majority cross the chasm. For each persona, produce: trial trigger, first-run experience prediction, day-7 retention prediction (still using?), day-30 status (champion, occasional, churned), and the one thing that would change their trajectory.
- Findings: Adoption curve projection (% of target users at month 1, 3, 6). Chasm risks -- the gap between early adopters and early majority, and what bridges it. Champion identification -- which personas become internal advocates. Churn risks -- which personas try and abandon, and why. Intervention recommendations -- specific actions ranked by impact on adoption rate (documentation, templates, workshops, integrations, defaults changes).
- Amend: User can adjust the rollout strategy, change org context, focus on a specific persona's journey, or simulate the impact of a specific intervention.
**Lightweight**: Single-pass. All personas assessed in one prompt. No month-by-month simulation -- snapshot at month 1, 3, 6 only. No intervention A/B testing -- ranked recommendations only.
**Artifact**: `listen/adoption/sim-adoption-{slug}-{date}.md`
**Example**:
```
User: /listen:adoption "simulation plugin" --teams 3 --rollout opt-in --culture "engineering-led, bottom-up"
> Mapping 12 personas to adoption archetypes...
> Assessing switching costs (current tools: ad-hoc Markdown, custom scripts, nothing)...
>
> ## Adoption Simulation: Simulation Plugin (3 teams, opt-in, 6 months)
>
> ### Adoption Curve Projection
> | Month | Users | % of Target | Phase |
> |-------|-------|-------------|-------|
> | 1     | 4     | 8%          | Innovators |
> | 3     | 18    | 36%         | Early Adopters |
> | 6     | 31    | 62%         | Early Majority (crossing chasm) |
>
> ### Persona Adoption Journey
> | Persona | Archetype | Trial Trigger | Day-7 | Day-30 | Trajectory Change |
> |---------|-----------|---------------|-------|--------|-------------------|
> | C-02 James | Innovator | Sees CLI, tries immediately | Active | Champion | -- (already ideal) |
> | C-09 Lisa | Innovator | Sees coverage reports | Active | Champion | -- (already ideal) |
> | C-03 Priya | Early Adopter | Reviews architecture | Active | Occasional | Determinism docs |
> | C-04 David | Early Adopter | Hears from James | Active | Champion | Team assignment feature |
> | C-10 Marcus | Early Majority | Sees team using it | Trying | Occasional | Jupyter integration |
> | C-11 Tomoko | Early Majority | David recommends | Trying | Active | Dashboard for team leads |
> | C-01 Maria | Late Majority | Required by team | Confused | Churned | Guided wizard |
> | C-07 Catherine | Laggard | Exec mandate only | N/A | N/A | ROI report |
>
> ### Chasm Analysis
> **The gap**: Between C-03/C-04 (early adopters who understand the methodology)
>   and C-10/C-11 (early majority who need it to "just work").
>
> **Bridge**: Three interventions ranked by chasm-crossing impact:
> 1. **Starter templates** (HIGH impact) -- Pre-built series configs for common
>    domains (API validation, compiler specs, workflow testing). Eliminates the
>    "blank page" problem for the early majority.
> 2. **Team dashboard** (MEDIUM impact) -- Aggregate view of series progress
>    across team members. Gives team leads (C-11) visibility without CLI fluency.
> 3. **Guided first-run** (MEDIUM impact) -- Interactive setup wizard that asks
>    3 questions and scaffolds the first series. Converts Maria (C-01) from
>    churned to occasional.
>
> ### Champion Network
> | Champion | Influence Radius | What They Tell Others |
> |----------|-----------------|----------------------|
> | C-02 James | 8-10 developers | "It's TDD for specs -- you write expected output first" |
> | C-09 Lisa | 5-6 SREs | "Finally, coverage reports for design decisions" |
> | C-04 David | 12-15 PMs | "I can see which specs have been validated and which haven't" |
>
> ### Churn Risks
> | Persona | Churn Point | Root Cause | Preventable? |
> |---------|-------------|------------|--------------|
> | C-01 Maria | Day 3 | Jargon + no wizard | Yes -- guided first-run |
> | C-07 Catherine | Never tries | No executive-facing value prop | Yes -- ROI template |
> | C-12 Frank | Day 1 | No compliance/audit integration | Partially -- audit export |
>
> Artifact written: listen/adoption/sim-adoption-simulation-plugin-2026-03-14.md
```

## Roles

### Stock roles

| Role | What it does in listen |
|------|----------------------|
| C-01 Maria Chen | Maker lens: flags jargon, missing wizards, "can I do this without a manual?" |
| C-02 James Okafor | Developer lens: flags missing APIs, schemas, machine-parseable output |
| C-03 Priya Sharma | Architect lens: flags portability gaps, determinism, formal grammar |
| C-04 David Kim | PM lens: flags coordination gaps, team workflow, progress visibility |
| C-05 Elena Vasquez | Compliance lens: flags audit trail gaps, evidence collection, regulatory alignment |
| C-06 Robert Tanaka | Auditor lens: flags accountability gaps, approval workflows, traceability |
| C-07 Catherine Moore | Executive lens: flags cost justification, ROI clarity, executive summary |
| C-08 Ahmad Al-Rashid | Partner lens: flags integration complexity, onboarding time, white-label readiness |
| C-09 Lisa Johansson | SRE lens: flags operational gaps, monitoring, performance, security |
| C-10 Marcus Rivera | Data Scientist lens: flags data export, programmatic access, notebook integration |
| C-11 Tomoko Watanabe | Team Lead lens: flags team visibility, assignment, progress tracking |
| C-12 Frank Hoffmann | Regulator lens: flags compliance evidence, audit export, regulatory reporting |
| Support | Predicts ticket categories, writes sample tickets in persona voice, identifies doc gaps |
| SRE | Identifies operational failure modes, performance risks, monitoring blind spots |
| PM | Synthesizes cross-persona themes, maps adoption curves, identifies chasm risks |
| UX | Identifies friction patterns across personas, classifies usability vs. feature issues |

### Custom roles (optional)

- **/listen:feedback** benefits from industry-specific personas (e.g., "Healthcare Compliance Officer" for health-tech products, "Financial Auditor" for fintech products) that bring domain-specific regulatory expectations and jargon sensitivity.
- **/listen:support** benefits from "Tier 2 Support Engineer" as a custom role that predicts escalation patterns beyond first-contact tickets.
- **/listen:adoption** benefits from "Change Management Lead" as a custom role that brings organizational psychology expertise to the adoption simulation (resistance patterns, coalition building, communication cadence).

## Artifacts

```
listen/
├── feedback/
│   └── sim-feedback-{slug}-{date}.md
├── support/
│   └── sim-support-{slug}-{date}.md
└── adoption/
    └── sim-adoption-{slug}-{date}.md
```

All artifacts use the `sim-` topic prefix. Slug is derived from the target spec or feature name (lowercased, hyphenated, truncated to 40 chars). Date is ISO 8601 (YYYY-MM-DD).

## Cross-Namespace Integration

- **draft:spec -> listen:feedback**: The spec produced by /draft:spec is the primary input to /listen:feedback. Each persona evaluates the spec as if it were a shipped product description. Findings from listen:feedback loop back as spec amendment recommendations.
- **draft:pitch -> listen:feedback**: The pitch narrative from /draft:pitch can be tested against customer personas to validate resonance before the pitch is delivered. Persona NPS scores predict audience reception.
- **draft:proposal -> listen:adoption**: The chosen option from /draft:proposal feeds into adoption simulation. If the proposal recommends "build," listen:adoption predicts who adopts and what accelerates it. If the proposal recommends "buy," listen:adoption predicts integration adoption friction.
- **listen:feedback -> scout:requirements (loop)**: Blocking and major findings from persona feedback generate new requirements for the next version. F-IDs from listen trace back to R-IDs in scout.
- **listen:support -> draft:spec (loop)**: Predicted support tickets that indicate design gaps (not doc gaps) feed back into spec amendments. A ticket forecast that predicts >50 tickets from a single design decision is a signal to revisit that decision.
- **listen:adoption -> scout:stakeholders (loop)**: Adoption simulation identifies champions and resistors. This feeds back into stakeholder mapping for the next planning cycle -- the champion network from listen becomes the engagement plan in scout.
- **listen:feedback -> listen:support (chain)**: Persona findings from feedback predict which personas will file tickets. The feedback severity map (blocking/major/minor) directly informs the support ticket volume prediction. A "blocking" finding for C-01 (Maria) predicts high-volume "how-to" tickets from non-technical users.
- **listen:adoption -> listen:support (chain)**: Churn predictions from adoption inform support ticket timing. Personas predicted to churn at day 3 will file tickets at day 1-2. Personas predicted to become champions will file feature requests at day 14-30.
