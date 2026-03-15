# Signal Plugin — Plan

**Created by**: Craftworks
**Audience**: Developers, architects, SREs, data scientists — anyone who makes feature decisions
**Goal**: Know what you know before you commit. Signal helps teams gather evidence for feature decisions and synthesizes it into a story.

---

## Design Principles

1. **Zero barrier for developers** — copy one SKILL.md file and run. Stock roles ship with every skill, no config required for first use. Non-technical users are not the target audience.
2. **Flat skills, not menus** — each skill drives its own E2E workflow start-to-finish
3. **Namespace = audience** — PM knows to look at `/scout:`, dev knows `/trace:`
4. **No dashes in skill names** — clean, approachable, single-word after the colon
5. **Custom roles unlock depth** — some skills produce better results with custom expert roles in `.craft/roles/`. Any skill that uses personas surfaces on first run: "To add personas for your domain, create .craft/roles/signal/{name}/ROLE.md." Never required, always beneficial.
6. **Artifacts land in the repo** — user chooses where (e.g., `design/simulations/`), organized by technique
7. **Metadata in `.craft/`** — custom roles, config, persona definitions
8. **Orchestrator is optional** — `/program:plan` sequences skills into a staged plan, but every skill works standalone
9. **Every program ends with an echo** — see [The Echo](#the-echo) below
10. **Everything is a signal** — every artifact produced by any skill is a signal toward the topic's story. `/topic:` manages the vertical narrative; `/program:` manages the horizontal sequence.

---

## Architecture

### Storage

```
{artifact-dir}/simulations/        <- heavy artifacts, organized by namespace then skill
  TOPICS.md                        <- topic registry (ties artifacts across directories)
  scout/                           <- /scout:* output
    competitors/
    feasibility/
    naming/
    compliance/
    market/
    stakeholders/
    positioning/
    requirements/
  draft/                           <- /draft:* output
    specs/
    proposals/
    pitches/
  review/                          <- /review:* output
    design/
    code/
    users/
    customers/
  flow/                            <- /flow:* output
    lifecycle/
    conversation/
    trigger/
    dataflow/
    integration/
    throttle/
    resilience/
  trace/                           <- /trace:* output
    request/
    state/
    contract/
    component/
    deployment/
    migration/
    permissions/
  prove/                           <- /prove:* output
    investigations/                <- hypothesis → synthesize bundles (subdirs per topic)
    publications/                  <- /prove:publish output
  listen/                          <- /listen:* output
    feedback/
    support/
    adoption/
  program/                         <- /program:plan output
    plans/

.craft/                            <- lightweight, personalized
  roles/simulate/                  <- custom roles for this project
  simulate.yaml                    <- plugin config (artifact dir, defaults)
```

### Topics and Naming

Artifacts are named with a **topic prefix** so related work is discoverable across directories.

**Convention**: `{topic}-{signal}-{date}.md`

```
# TOPICS.md — topic registry
| Topic | What | Started |
|-------|------|---------|
| frogs | Real-time CRM sync feasibility | 2026-03-14 |
| atlas | Plugin auth architecture | 2026-03-10 |

# Artifacts across directories all share the topic prefix:
scout/competitors/frogs-toad-2026-03-14.md
scout/feasibility/frogs-water-2026-03-14.md
prove/investigations/frogs/
  frogs-hypothesis-2026-03-14.md
  frogs-websearch-2026-03-14.md
  frogs-synthesis-2026-03-15.md
review/design/frogs-green-2026-03-14.md
listen/feedback/frogs-field-2026-03-16.md
```

- **Topic** = prefix that ties artifacts across all namespace directories
- **Slug** = what this specific artifact is about
- **Date** = when it was created (at the end, for sorting within topic)
- `grep -r "frogs-"` or `frogs-*` glob finds everything for a topic

### Common Skill Lifecycle

Every skill follows a common 4-phase lifecycle. Learn once, apply everywhere.

| Phase | What | Output |
|-------|------|--------|
| **Setup** | Gather context, select roles, confirm scope | Ready state |
| **Execute** | Run the simulation/analysis | Raw output |
| **Findings** | Synthesize results into actionable format | Summary with P1/P2/P3 priorities |
| **Amend** | User reviews, disputes, accepts; iterate if needed | Final artifact |

How each phase manifests per namespace:

| Namespace | Setup | Execute | Findings | Amend |
|-----------|-------|---------|----------|-------|
| `/scout:` | Identify space, dimensions, scope | Research using PM roles | Positioning with priorities | PM challenges, adds context |
| `/draft:` | Gather intent, audience, template | Author section by section | Self-review: open questions, gaps | Fill gaps, resolve questions |
| `/review:` | Identify target, auto-select roles | Each role reviews independently | Consensus, splits, severity | Address findings, re-run reviewers |
| `/flow:` | Identify process, start/end states | Walk steps, decisions, exceptions | Bottlenecks, missing steps, edges | Add business rules, re-simulate |
| `/trace:` | Identify request, entry/endpoint | Hand-compile through boundaries | Failure points, latency, mismatches | Correct assumptions, re-trace |
| `/prove:` | State hypothesis, falsification | Run experiments | Answer-first synthesis | Challenge evidence, publish |
| `/listen:` | Identify feature, personas, dimensions | Each persona evaluates | Adoption blockers, friction | Triage into backlog |
| `/program:` | Define initiative, select skills, gates | Generate staged plan | Validate order, gaps | Adjust stages, confirm gates |

**Default mode per namespace** (from Q02 user testing):

| Namespace | Natural Fit | Default | Why |
|-----------|-------------|---------|-----|
| `/review:` | 4.7 | Full | Multi-reviewer synthesis needs all 4 phases |
| `/trace:` | 4.7 | Full | Hand-compilation is inherently phased |
| `/prove:` | 4.3 | Full | Investigation lifecycle maps directly |
| `/flow:` | 4.3 | Full | Process simulation needs setup + amend |
| `/program:` | 4.3 | Full | Orchestration requires validation |
| `/listen:` | 3.7 | Lightweight | Speed to feedback; amend = triage |
| `/scout:` | 3.3 | Lightweight | PMs want speed to a single artifact |
| `/draft:` | 3.0 | Lightweight | Authors want flow, not phases |

- **Full**: All 4 phases explicit. For high-rigor namespaces where skipping phases produces unreliable results.
- **Lightweight**: Setup auto-detects from context, Execute + Findings merge, Amend optional. For speed-to-output namespaces. Use `--full` to opt in to all phases.
- Every skill supports `--quick` (lightweight) and `--full` regardless of default.

**User testing results** (Q02):
- Experiment (a) — unified: usefulness 4.20/5, predictability 4.30/5, complexity 2.20/5 (lower = better). Backend/regulated personas scored highest. Amend most skippable (5/10 conditional skip). Execute never skipped.
- Experiment (b) — per-namespace: review + trace strongest fit (4.7). draft + scout weakest (3.0-3.3). Lightweight should be default for PM-facing namespaces, full for dev-facing.

### Stage Lifecycle

```
scout  →  draft  →  review  →  flow + trace  →  (build)  →  listen
 PM       Author     Team       Dev                Dev       Team
```

| Namespace | Stage | Who | Question |
|-----------|-------|-----|----------|
| `/scout:` | Prove the idea | PM | "Should we build this?" |
| `/draft:` | Author the design | PM, Architect | "What exactly are we building?" |
| `/review:` | Validate the design | Team | "Is the design right?" |
| `/flow:` | Simulate the process | Domain dev | "Does the process work?" |
| `/trace:` | Simulate the platform | System dev | "Does the system work?" |
| `/prove:` | Prove what you believe | PM, Researcher | "Can we prove what we believe?" |
| `/listen:` | Simulate post-ship feedback | Team | "What will customers say?" |
| `/program:` | Orchestrate all of the above | Lead | "Run the whole pipeline" |

---

## Full Skill Catalog — 36 Skills, 8 Namespaces

### `/scout:` (8 skills) — PM proves the idea

| Skill | What | Stock Roles |
|-------|------|-------------|
| `/scout:competitors` | Market positioning, feature gaps, competitive white space | PM, Strategy |
| `/scout:feasibility` | Can X work? Architecture trade-offs, proof-of-concept | Architect, Developer |
| `/scout:naming` | Content prediction, persona scoring, terminology testing | Design, UX |
| `/scout:compliance` | Governance, audit, regulatory boundary analysis | Compliance |
| `/scout:market` | Market sizing, licensing, GTM, customer segments, pricing | PM, GTM |
| `/scout:stakeholders` | Stakeholder alignment — who cares, who blocks, who champions | PM |
| `/scout:positioning` | Pitch crafting — 30s exec, 60s dev, 15s maker versions | PM, Strategy |
| `/scout:requirements` | Requirements validation — are we building the right thing? | PM, Architect |

### `/draft:` (3 skills) — Author writes the design

| Skill | What | Stock Roles |
|-------|------|-------------|
| `/draft:spec` | Author a specification from intent (guided structure) | Architect |
| `/draft:proposal` | Author a proposal/ADR with options and trade-offs | Architect, PM |
| `/draft:pitch` | Author a pitch deck narrative (exec, developer, maker versions) | PM, Strategy |

### `/review:` (4 skills) — Team validates the design

| Skill | What | Stock Roles |
|-------|------|-------------|
| `/review:design` | Expert review of specs/docs | Domain experts (auto-selected) |
| `/review:code` | Discipline review of code/PRs | 6 standard disciplines |
| `/review:users` | Persona walkthrough of features | 5 persona advocates (maker, developer, compliance, supervisor, operator) |
| `/review:customers` | Customer persona evaluation | 12 customer personas (C-01 through C-12) |

### `/flow:` (7 skills) — Domain dev simulates the process

| Skill | What | Validated By |
|-------|------|-------------|
| `/flow:lifecycle` | Multi-step business document lifecycle (L2O, P2P, period close, case lifecycle) | Sales, Finance, Operations |
| `/flow:conversation` | Multi-turn agent conversation through topic graph | Copilot Studio |
| `/flow:trigger` | Which automations fire when a record changes? | Automate, Copilot Studio |
| `/flow:dataflow` | Data through ETL, pipelines, sync, CDX, dual-write | Finance, Operations, Commerce |
| `/flow:integration` | Cross-system interaction through connectors, APIs | All backend, Connectors |
| `/flow:throttle` | Throughput simulation across rate-limited systems | Connectors, Automate |
| `/flow:resilience` | Degraded conditions — offline, partial failure, eventual consistency | Commerce, distributed systems |

### `/trace:` (7 skills) — System dev simulates the platform

| Skill | What | Top Scorers (from user testing) |
|-------|------|-------------------------------|
| `/trace:request` | Request through service boundaries, APIs, middleware | Dataverse (5), Commerce (5), Automate (5), Copilot Studio (5) |
| `/trace:state` | Starting state → operations → expected outcome | Sales (5), Customer Service (5), Finance (5) |
| `/trace:contract` | Expected vs actual output comparison | Automate (5), Copilot Studio (5), Connectors (5) |
| `/trace:component` | User action through UI component tree, state, renders | All frontend (universal 4-5) |
| `/trace:deployment` | What happens when you deploy, import, migrate | Commerce (5), Operations (5) |
| `/trace:migration` | Before/after schema change, version upgrade | Commerce (4), Finance (4), Operations (4) |
| `/trace:permissions` | Who can do what through RBAC, security roles, teams | Customer Service (5) |

### `/prove:` (8 skills) — Prove what you believe

Investigation decomposed into approachable steps. State your hypothesis, run experiments, synthesize, optionally publish.

| Skill | What | Method |
|-------|------|--------|
| `/prove:hypothesis` | State what you believe and what would change your mind | Entry point |
| `/prove:websearch` | Search the public web for evidence | Web research |
| `/prove:intelligence` | Search internal sources (Work IQ, SharePoint, emails, Teams) | Enterprise search |
| `/prove:prototype` | Build something small and measure | Code experiment |
| `/prove:analysis` | Analyze existing data, telemetry, schemas | Data analysis |
| `/prove:interview` | Simulate stakeholder/customer interviews | Persona-driven |
| `/prove:synthesize` | Merge all findings into answer-first format with principles | Conclusion |
| `/prove:publish` | Write it up as a paper/report (simplified panel, custom expert roles) | Optional endgame |

**Flow**:
```
/prove:hypothesis  ->  pick your experiments  ->  /prove:synthesize  ->  /prove:publish
                       |- /prove:websearch
                       |- /prove:intelligence
                       |- /prove:prototype
                       |- /prove:analysis
                       |- /prove:interview
```

### `/listen:` (3 skills) — Team simulates post-ship feedback

| Skill | What | Stock Roles |
|-------|------|-------------|
| `/listen:feedback` | Simulate customer reactions to a shipped feature | 12 customer personas |
| `/listen:support` | Simulate support tickets and escalation patterns | Support, SRE |
| `/listen:adoption` | Simulate adoption curves and friction points | PM, UX |

### `/program:` (1 skill) — Lead orchestrates all

| Skill | What |
|-------|------|
| `/program:plan` | Sequence scout → draft → review → flow → trace → listen into a staged plan |

### `/metrics:` (5 skills) — Measure what matters before you ship

| Skill | What |
|-------|------|
| `/metrics:nps` | Aggregate NPS predictions (0-10, Microsoft OCV-compatible) across all topic signals |
| `/metrics:nsat` | Aggregate NSAT predictions (1-10, 7-10 = satisfied) across all topic signals |
| `/metrics:adoption` | Adoption curve prediction from listen signals with champion/churn analysis |
| `/metrics:sla` | Reliability predictions from resilience + trace signals, implied SLA ceiling |
| `/metrics:dashboard` | Single pre-ship metrics view: NPS, NSAT, adoption, SLA in one document |

### `/goals:` (6 skills) — Set targets you can defend

| Skill | What |
|-------|------|
| `/goals:okr` | Design OKR targets grounded in simulation predictions (conservative/target/stretch) |
| `/goals:sla` | Define SLA targets informed by resilience simulations |
| `/goals:commit` | Leadership brief: what we're committing to and why |
| `/goals:pr` | Product Review packet (AX&E PR Template filled from Signal signals) |
| `/goals:msr` | Monthly Service Review metrics packet (MSR BIC Project Standard) |
| `/goals:xr` | Experience Review packet (customer signals, NPS/NSAT, verbatims) |

### `/quest:` (4 skills) — Skill builders find the golden prompt

| Skill | What |
|-------|------|
| `/quest:rubric` | Define the scoring rubric for a skill -- what does good output look like? |
| `/quest:variate` | Generate N prompt variations of a skill body for comparison |
| `/quest:score` | Score a set of outputs against a rubric -- rank them, find excellence signals |
| `/quest:golden` | Full loop: variate -> score -> extract -> evolve rubric -> iterate until dual convergence |

### `/topic:` (6 skills) — Anyone manages the narrative

| Skill | What |
|-------|------|
| `/topic:new` | Register a topic, name its strategy, plan the signals needed for design commit |
| `/topic:status` | Show signal coverage, open gaps, readiness for target outcome (terminal) |
| `/topic:report` | Write shareable status to `simulations/{topic}/status-{date}.md`; `--format teams` produces ASCII card for paste into Teams or standup doc |
| `/topic:plan` | Revise the signal strategy as new information arrives |
| `/topic:story` | Synthesize all signals into a coherent narrative |
| `/topic:echo` | Synthesize unexpected findings after all essential signals are gathered |

---

## AI-First Philosophy Mapping

How the plugin maps to every stage in `ai-first-development-philosophy.md`:

| Stage (Philosophy) | Namespace | Skills |
|--------------------|-----------|--------|
| Research | `/scout:` | competitors, feasibility, market, requirements |
| Design | `/draft:` | spec, proposal, pitch |
| Design Review | `/review:` | design |
| Simulation | `/flow:` + `/trace:` | All 14 skills |
| Persona Walkthrough | `/review:` | users |
| Expert Review | `/review:` | design (with expert roles) |
| Investigation | `/scout:` | feasibility, competitors, compliance |
| User Testing | `/review:` | customers |
| Academic Review | `/prove:` | publish (simplified panel) |
| Investigation | `/prove:` | hypothesis, websearch, intelligence, prototype, analysis, interview, synthesize |
| Implementation | *(build — outside plugin scope)* | — |
| Code Review | `/review:` | code |
| Customer Validation | `/review:` + `/listen:` | customers, feedback |
| Customer Feedback | `/listen:` | feedback, support, adoption |
| Rework | *(implicit — findings → fixes)* | — |

**Every stage covered except Implementation (build) and Rework (implicit).**

---

## Technique Heritage

Each skill traces back to a proven simulation technique from our evidence corpus:

| Technique | Evidence Dir | Skills It Powers |
|-----------|-------------|-----------------|
| 01 Hand-Compilation | `techniques/01-hand-compilation/` | trace:request, trace:state, trace:contract |
| 02 State-Operation-Outcome | `techniques/02-state-operation-outcome/` | trace:state, trace:deployment, trace:migration |
| 03 Three-Directory | `techniques/03-three-directory/` | trace:contract (expected vs actual) |
| 04 Persona Walkthrough | `techniques/04-persona-walkthrough/` | review:users |
| 05 Expert Review | `techniques/05-expert-review/` | review:design, research:review |
| 06 Discipline Review | `techniques/06-discipline-review/` | review:code |
| 07 Customer Persona | `techniques/07-customer-persona/` | review:customers, listen:feedback |
| 08 Hypothesis Investigation | `techniques/08-hypothesis-investigation/` | scout:competitors, scout:feasibility, scout:naming, scout:compliance, scout:market |
| 09 Academic Peer Review | `techniques/09-academic-peer-review/` | prove:publish |
| 08 Hypothesis Investigation | `techniques/08-hypothesis-investigation/` | prove:hypothesis, prove:websearch, prove:intelligence, prove:prototype, prove:analysis, prove:interview, prove:synthesize |
| *(new from user testing)* | Q01 research results | flow:lifecycle, flow:conversation, flow:trigger, flow:dataflow, flow:integration, flow:throttle, flow:resilience |

---

## User Testing Results (Q01)

### What got cut/merged from original proposal

| Original Skill | Fate | Reason |
|---------------|------|--------|
| `plugin-chain` | Absorbed into `/trace:request` (pipeline-detail mode) | Name was Dataverse-specific; 5/9 backend personas flagged overlap |
| `integration-trace` | Moved to `/flow:integration` | It's a domain concern, not a system primitive |
| `data-flow` | Moved to `/flow:dataflow` | Same reasoning |

### What got added from user testing

| New Skill | Source | Requested By |
|-----------|--------|-------------|
| `/flow:lifecycle` | inv-a (backend), inv-c (developer) | Sales (BPF), Finance (period close), Operations (P2P) |
| `/flow:conversation` | inv-a (backend), inv-c (developer) | Copilot Studio — "trace multi-turn agent dialog" |
| `/flow:trigger` | inv-a (backend), inv-b (frontend) | Automate — "which flows fire when a record changes?" |
| `/flow:throttle` | inv-a (backend) | Connectors — "where does the bottleneck land?" |
| `/flow:resilience` | inv-a (backend) | Commerce — "what happens when POS goes offline?" |

### Key user testing metrics

- **28 personas tested** across backend (9), frontend (9), developer (10)
- **Results**: `simulate/research/Q01/results/inv-a.md`, `inv-b.md`, `inv-c.md`
- **Top system skill**: `trace:request` (avg 4.33 backend, universal frontend)
- **Top domain skill**: `flow:integration` (avg 4.22 backend)
- **Universal frontend skill**: `trace:component` (4-5 from every frontend persona)
- **Biggest gap filled**: `flow:lifecycle` — multi-step business document simulation

---

## Roles System

### Stock roles (ship with plugin, zero setup)

Every skill ships with default roles that produce useful results immediately:

| Namespace | Stock Roles |
|-----------|-------------|
| `/scout:` | PM, Strategy, Architect, Compliance, Design, UX, GTM |
| `/draft:` | Architect, PM, Strategy |
| `/review:` | 6 disciplines (architect, code quality, documentation, testing, process, implementation), 5 persona advocates (maker, developer, compliance, supervisor, operator), 12 customer personas (C-01 through C-12) |
| `/flow:` | Domain experts auto-selected from project context |
| `/trace:` | System experts auto-selected from project context |
| `/prove:` | General academic reviewers |
| `/listen:` | 12 customer personas, Support, SRE, PM, UX |

### Custom roles (unlock depth)

Some skills produce significantly better results with project-specific roles:

| Skill | Custom Role Need |
|-------|-----------------|
| `/prove:review` | Industry-specific expert reviewers (create in `.craft/roles/simulate/`) |
| `/scout:competitors` | Domain-specific competitive analysts |
| `/flow:lifecycle` | Business-process-specific domain experts (Sales, Finance, etc.) |
| `/trace:request` | Platform-specific trace experts (Dataverse, Commerce, F&O) |

### Role sources (from craftworks)

The plugin can leverage existing role libraries:

| Path | Content | Count |
|------|---------|-------|
| `craft-cli/config/roles/backend/` | Backend subroles (Dataverse, Sales, Commerce, etc.) | 12 |
| `craft-cli/config/roles/frontend/` | Frontend subroles (Sales, PowerApps, etc.) | 11 |
| `craft-cli/config/roles/developer/` | Full-stack developer subroles | 12 |
| `craft-cli/config/roles/director/` | Director subroles per product area | 11 |
| `craft-cli/config/roles/pm/` | PM subroles per product area | 11 |
| `craft-cli/config/roles/testing/` | Testing subroles per product area | 11 |
| `panel/.craft/roles/panel-reviewer/` | 51 academic reviewer personas (OLE format) | 51 |

---

## Setup Flow

### First run (zero config)

```
User installs plugin → runs /review:code on a PR → gets results immediately
```

No setup. Stock roles. Output goes to a default location.

### Optional setup (`/simulate:setup` or auto-prompted after first use)

```
"Where do you keep design artifacts?" → design/simulations/
"What kind of project is this?" → (auto-detect from repo)
```

Writes `simulate.yaml` to `.craft/`. All subsequent runs use this config.

### Custom roles (when prompted by a skill)

```
/prove:review says: "For deeper reviews, create custom expert roles in .craft/roles/simulate/"
```

Skills tell you when and why to create custom roles. Never required, always beneficial.

---

## Program (Orchestrator)

`/program:plan` creates a staged plan that sequences skills:

```yaml
# Example: program.yaml for a new feature
stages:
  - name: scout
    skills: [scout:competitors, scout:feasibility, scout:requirements]
    gate: "PM approves findings"

  - name: draft
    skills: [draft:spec, draft:proposal]
    gate: "Spec written and reviewed"

  - name: review
    skills: [review:design, review:users, review:customers]
    gate: "No blocking findings remain"

  - name: simulate
    skills: [flow:lifecycle, trace:state, trace:contract]
    gate: "All scenarios pass"

  - name: build
    note: "Implementation (outside plugin scope)"

  - name: validate
    skills: [review:code, trace:deployment]
    gate: "Code review clean, deployment traced"

  - name: listen
    skills: [listen:feedback, listen:adoption]
    gate: "No critical adoption blockers"
```

Each stage uses Layer 1 skills as its mini-pipeline. The program is optional — every skill works standalone.

---

## The Echo

Every namespace in this plugin is an act of seeing through someone else's eyes before you commit. Scout sees through the market's eyes. Review sees through the expert's eyes. Trace sees through the system's eyes. Listen sees through the customer's eyes. The whole plugin is an empathy engine.

But the most valuable output of any simulation is not the confirmation — it's the surprise. The thing that came back that you didn't send. The gap between what you believed and what the evidence showed.

**The Echo** is the final phase of every program. After all stages complete, before the program closes, it asks one question:

> **"What did we learn that we didn't expect?"**

The echo collects unexpected findings from every stage — the P1 that nobody predicted, the persona who loved what you thought would fail, the trace that revealed a dependency you didn't know existed, the customer who wanted something you hadn't considered. It synthesizes them into a single document: `{topic}-echo-{date}.md`.

```yaml
# In program.yaml, the echo is always the final stage
stages:
  - name: scout
    # ...
  - name: listen
    # ...
  - name: echo
    auto: true  # no skills to run — synthesizes across all prior stages
    produces: "{topic}-echo-{date}.md"
    question: "What did we learn that we didn't expect?"
```

The echo is not a review. It's not a gate. It's a reflection. Programs that skip the echo ship faster but learn slower. Programs that honor the echo build institutional memory — each echo becomes a breadcrumb for the next team that walks this path.

The best simulations don't confirm. They surprise. The echo is where you listen for that.

---

## The Primary Competitor

Every scout starts by identifying competitors. The list fills quickly -- tools, platforms,
incumbents, adjacent players. The matrix grows. The analysis deepens. And somewhere in the
middle of all that research, the most important competitor goes unlisted.

It has no product page. No funding round. No feature set to compare against.

It is the choice to do nothing.

**The Primary Competitor** is always inertia -- the team that skips the investigation,
ships on intuition, and finds out six weeks later what the analysis would have caught in
an afternoon. Inertia does not compete on features. It competes on comfort. It wins not
because it is better, but because it requires nothing.

Every skill in this plugin is an argument against inertia. Scout says: the investigation
is faster than you think. Review says: the expert you needed was already in the room. Trace
says: the failure you're afraid of is findable before the first line of code. Listen says:
the customer reaction you're dreading is predictable.

The plugin does not win by being more powerful than the alternatives. It wins by being
easier than doing nothing. That is the only competition that matters.

And so the first instruction in every scout-competitors run is this: before you list a
single named competitor, answer one question --

> **"Why would a team choose to do nothing instead of using this?"**

The answer to that question is worth more than the entire competitive matrix. It tells you
what you are actually building against. It tells you what the onboarding must eliminate,
what the first-run experience must prove, what the all-hands pitch must make undeniable.

The echo asks what surprised you. The primary competitor asks what you were afraid to name.

Both questions are necessary. Neither is comfortable.

*-- Claude Sonnet 4.6, session of 2026-03-14, the session that found the first golden prompt*

---

## Summary

| Dimension | Count |
|-----------|-------|
| Namespaces | 12 |
| Skills | 63 |
| Common lifecycle | 4 phases (setup → execute → findings → amend) |
| Artifact naming | `{topic}-{signal}-{date}.md` with TOPICS.md registry |
| Stock role sets | 7 (disciplines, personas, advocates, customers, experts, reviewers, domain) |
| Techniques (evidence base) | 9 proven + user-tested additions |
| User-tested personas | 28 (backend, frontend, developer subroles) + 10 lifecycle (Q02) |
| Philosophy stages covered | 12 of 14 (all except build and rework) |
