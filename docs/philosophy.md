# AI-First Development Philosophy

Work Agents & Agentverse — how we build software.

## The Principle

Every stage of the development lifecycle that used to be skipped, shallow, or bottlenecked on human availability — we run with AI. Not as autocomplete. AI as your research team, your review board, your simulation lab, your implementation force.

## Then vs Now

| Stage | Then | Now |
|---|---|---|
| Research | Skipped | AI researchers run hypothesis-driven experiments and kill bad ideas before they become code |
| Design | One architect, best guess | AI architects generate specs anchored to empirical findings |
| Design Review | Schedule a meeting, wait | AI experts find bugs in minutes across 12 disciplines simultaneously |
| Simulation | Didn't exist | AI simulators hand-compile scenarios to find spec gaps before code exists |
| Persona Walkthrough | Didn't exist | AI personas walk specs as maker, developer, compliance, supervisor, operator — find friction before code |
| Expert Review | One senior dev, if available | Named-expert AI reviewers (compiler theorists, ML researchers, formal methods) stress-test designs |
| Investigation | Ad hoc Slack threads | Structured hypothesis → experiment → findings loops with result files and cross-reference |
| User Testing | Ship to beta, hope | 12 AI customer personas score naming, UX, content prediction before real users see it |
| Academic Review | No rigor | 3-tier simulated peer review (paper → module → board) with 51 expert personas, scoring rubrics |
| Implementation | Weeks of coding, discovery | AI coders implement proven designs in hours, not weeks |
| Code Review | One dev, one pass, move on | AI reviewers stress-test code from 12 angles in three rounds |
| Customer Validation | Ship to beta, hope | AI testers model real customer workspaces and find failures in design |
| Customer Feedback | Wait for complaints | AI customers give us feedback before the real ones do |
| Rework | Constant | Near zero — every upstream stage actually ran |

---

## Simulation Catalog

Every technique we've built, organized by what gets simulated, who does the simulating, and where the technique lives. These aren't hypothetical — each one has been used in production design work with measured findings.

### 1. Hand-Compilation Simulation

**What**: Manually trace input through compiler passes, derive expected output, compare to actual.
**Who simulates**: The designer, acting as the compiler.
**Scale**: 375+ scenarios across 53 series, 120 DCRs filed.
**Sources**:
- `design/astro/scenarios/SIMULATION.md` — master protocol
- `design/astro/scenarios/<series>/` — 53 series directories (Wave 1-4 structure)
- `design/astro/DCR.md` — findings → design changes
- `design/agent/scenarios/SIMULATION.md` — 315+ scenarios, 356 findings across 31 series
- `design/flows/SCENARIOS.md` — 42 scenarios (all complete), 78 findings (all resolved)

**Pattern**: Read spec → trace passes with test input → write expected output → compare actual vs expected → file finding → amend spec.

### 2. Starting-State → Operation-Sequence → Expected-Outcome Simulation

**What**: Trace API operations through SDK/registry/storage layers, validate state transitions.
**Who simulates**: The designer, acting as the SDK runtime.
**Scale**: 199 scenarios across 6 series (admin, agent, craft, seals, suite, vault).
**Sources**:
- `design/admin/scenarios/admin/SIMULATION.md` — 47 scenarios, 7 waves
- `design/admin/scenarios/agent/SIMULATION.md` — 32 scenarios, 8 waves
- `design/admin/scenarios/craft/SIMULATION.md` — 42 scenarios, 7 waves
- `design/admin/scenarios/seals/SIMULATION.md` — 28 scenarios, 6 waves (complete, 101 findings)
- `design/admin/scenarios/suite/SIMULATION.md` — 24 scenarios, 6 waves (active)
- `design/admin/scenarios/vault/SIMULATION.md` — 26 scenarios, 5 waves

**Pattern**: Starting state → numbered operation steps with expected results → terminal assertions.

### 3. Hand-Derived Expected Output Simulation (3-Directory)

**What**: Hand-compile expected output files FIRST, then run script, then diff.
**Who simulates**: The designer, acting as the Python script.
**Scale**: 24 scenarios (15 complete), organized by pipeline.
**Sources**:
- `design/flash/scenarios/SIMULATION.md` — master protocol
- `design/flash/scenarios/NN+scenario-name/` — S01-S24 numbered directories
- `research/frost/POSTMORTEM.md` — bug history from findings

**Pattern**: `10+input/` (fixtures) → `20+expected/` (hand-derived) → `30+actual/` (script output). Detects "Two-System Trap" (same logical type, different representations).

### 4. Persona-Driven Walkthrough Simulation

**What**: 5 persona advocates walk through specs as their persona, identifying confusion, friction, fear, jargon, missing context.
**Who simulates**: AI acting as maker, developer, compliance officer, supervisor, operator.
**Scale**: 5 walkthroughs per feature area, findings tagged by severity.
**Sources**:
- `.craft/pipelines/suite/simulate.md` — pipeline stage definition
- `.craft/waves/*/simulate-*.md` — per-persona walkthrough reports

**Pattern**: Each persona reads specs → walks typical journey → produces findings (blocking/major/minor/cosmetic) → spec amendments → re-verification. Catches design problems technical reviewers miss.

### 5. Named-Expert Reviewer Simulation

**What**: Designs reviewed through the lens of specific domain experts (compiler theorists, ML researchers, formal methods, etc.).
**Who simulates**: AI acting as named researchers (Aho, Lattner, Ullman, Liang, Solar-Lezama, etc.).
**Scale**: 18 distinct reviewer perspectives, 100+ findings.
**Sources**:
- `design/astro/final/review-aho.md` — Alfred V. Aho (compiler fundamentals)
- `design/astro/final/review-lattner.md` — Chris Lattner (compiler architecture)
- `design/astro/final/review-ullman.md` — Jeffrey Ullman (algorithms, formal methods)
- `design/astro/final/review-khattab.md` — Omar Khattab (prompt optimization, RAG)
- `design/astro/final/review-liang.md` — Percy Liang (AI/ML systems)
- `design/astro/final/review-solar-lezama.md` — Armando Solar-Lezama (program synthesis)
- `design/astro/final/review-lam.md` — Monica S. Lam (static analysis)
- `design/astro/final/review-polikarpova.md` — Nadia Polikarpova (formal verification)
- Plus 10 more lens-based reviews (architecture, code quality, testing, documentation, process, implementation)

**Pattern**: Expert reads design through their specific lens → findings (F-NN) with severity and resolution status → opportunities (O-NN) with recommendations → concrete file paths and line numbers.

### 6. Discipline-Driven Peer Review Simulation

**What**: Multi-disciplinary code review from standardized lenses.
**Who simulates**: AI acting as architect, code quality reviewer, documentation reviewer, tester, PM, implementer.
**Scale**: 6 standard disciplines, applied to every design area.
**Sources**:
- `plugins/craft/shared/make/discipline-operations.md` — discipline definitions
- `plugins/craft/shared/make/discipline-resolver.md` — discipline matching
- `.craft/reviews/concepts/` — review output directories

**Pattern**: Same artifact reviewed by 6 disciplines independently → checkbox format `### F-01: Description (SEVERITY) — [ ] RESOLVED` → cross-discipline synthesis identifies systemic patterns.

### 7. Customer Persona Testing

**What**: 12 distinct customer personas score naming, UX, badge variants, content prediction.
**Who simulates**: AI acting as maker, developer, architect, PM, compliance officer, auditor, executive, partner, SRE, data scientist, team lead, regulator.
**Scale**: 12 personas (C-01 through C-12), 16 sub-investigations, quantified scoring.
**Sources**:
- `design/admin/focus/Q07/data/customer-personas.md` — 12 persona definitions
- `design/admin/focus/Q07/results/inv-*.md` — 16 investigation results

**Pattern**: Define persona (role, industry, tech depth, primary concern, mental model, blind spots) → present design options → score across dimensions → persona-weighted aggregation. Example: 12-persona naming study tested 15 candidates, CHARTERS won at 32/37 content prediction.

### 8. Hypothesis-Driven Investigation (`/research` Skill)

**What**: Iterative design decisions through structured hypothesis → experiment → findings loops.
**Who simulates**: The designer (or team members), with AI running experiments and analyzing results.
**Scale**: 7+ investigations in craftworks (Q01-Q07, 16+ sub-investigations), **59 research questions in Agentverse** (30 with experiment subdirectories), multi-contributor.
**Sources**:
- `.claude/skills/research/SKILL.md` — `/research` skill (hypothesis first, then validate)
- `design/admin/focus/Q07/README.md` — investigation methodology (craftworks)
- `design/admin/focus/Q0*/` — craftworks investigations
- `C:\src\agentverse\designs\questions.md` — master question registry (59 questions, 8 contributors)
- `C:\src\agentverse\designs\_consensus\questions\` — 59 question files, 30 with experiment subdirectories

**Pattern**: "We think X" → design experiment → run it → "Actually Y" → update hypothesis → next loop. Result files use prefixes: `exp-` (enterprise search / Work IQ), `inv-` (web/desk inquiry), `exp-` (code experiment). Each loop produces: "What we thought we learned" vs "What we actually learned."

**Multi-contributor model (Agentverse)**: Questions are owned by individual contributors (giodl, jamesol, edpiva, jeffand, aadkannan, etc.), prioritized P0/P1, and progress through Open → In Progress → Proposed → Answered. Each question resolves a specific design disagreement or validates an assumption. Resolution summaries are written directly in the registry table. Questions fork and block each other (e.g., Q23 blocks on Q01, Q141 revisits D01). This is the `/research` skill scaled to a real team — the same hypothesis-first methodology, but with ownership, priority, consensus gates, and cross-question dependency tracking.

### 9. Three-Tier Academic Peer Review (Panel)

**What**: Full academic paper review lifecycle with simulated expert reviewers at three tiers.
**Who simulates**: 51 AI expert personas across 10 categories (systems, compilers, AI agents, prompting, HCI, ML systems, ML research, DevOps, NLP, security).
**Scale**: 51 reviewers, 10 research papers, 3 tiers, 10-point scoring.
**Sources**:
- `C:\src\panel/` — complete panel system
- `C:\src\panel/.craft/roles/panel-reviewer/R-1.md` through `R-51.md` — OLE-format persona files
- `C:\src\panel/context/panel/reviewers/profiles/` — cached reviewer profiles (~2KB each)
- `C:\src\panel/config/scoring.yaml` — 4-point (paper) and 10-point (module/board) scales
- `C:\src\panel/config/stages.yaml` — 8-stage lifecycle

**Architecture**:
- **Tier 1 (Paper)**: 5-7 reviewers per paper, 8-stage lifecycle (draft → panel → synthesis → revision → recheck → ready → submit → accepted), P1/P2/P3 priority classification, threshold avg >= 2.5/4.
- **Tier 2 (Module)**: 7-member panel, cross-paper pattern detection, PP1/PP2/PP3 classification, 10-point scale, three structural properties (causal chain, no weak links, actionable numbers).
- **Tier 3 (Board)**: 7-member board, cross-module synthesis, B1/B2/B3 classification, track alignment mapping (aligned/subset/parallel/divergent/unique).

**Token efficiency**: Persistent profiles reduce per-paper token cost by 34.7%, module-level by 37.3%.

### 10. Wave-Based Complexity Graduation

**What**: Feature completeness validated through graduated complexity waves.
**Who simulates**: The designer, with scenarios organized by difficulty.
**Scale**: Used across all scenario series (~955+ scenarios total).
**Sources**: All scenario series use this structure.

**Pattern**:
- Wave 1: Core behavior, happy path
- Wave 2: Basic composition, secondary features
- Wave 3: Edge cases, composition with other features
- Wave 4: Adversarial inputs, error boundaries
- Wave 5+: Failure recovery, performance boundaries, cross-system

### 11. Session Driver Methodology

**What**: Enforced, structured simulation execution with vocabulary control and progress tracking.
**Who simulates**: The AI session, governed by a CLAUDE.md per series.
**Sources**:
- `design/astro/scenarios/<series>/CLAUDE.md` — per-series session drivers
- `design/agent/scenarios/<series>/CLAUDE.md`
- `design/flash/scenarios/CLAUDE.md`
- `design/admin/scenarios/<series>/SIMULATION.md`

**Pattern**: Enforced vocabulary table (wrong vs correct terms) → pipeline model diagram → progress table → current scenario pointer → bugs found table → key files reference → startup protocol.

### 12. Cross-Reference Simulation (Rosetta Stone)

**What**: Pattern consistency validated across different simulation domains.
**Who simulates**: The designer, comparing patterns.
**Sources**:
- `design/admin/research/simulate-examples.md` — cross-reference of astro, craft, flash patterns
- `docs/research/simulation-research.md` — complete survey of all simulation techniques

**Pattern**: Compare naming, directory structure, finding formats across domains → identify inconsistencies → standardize.

---

## Scale

| Domain | Series | Scenarios | Findings | Status |
|--------|--------|-----------|----------|--------|
| Astro (compiler) | 53 | 375+ | 120 DCRs | Active |
| Craft (runtime) | 31+ | 315+ | ~356 | Active |
| Flash (provisioning) | 1 (S01-S24) | 24 (15 done) | ~40 | Active |
| Admin (SDK lifecycle) | 6 | 199 | 101+ | Active |
| Flows (IR → output) | 7 | 42 | 78 (all resolved) | Complete |
| Personas (customer) | 1 | 12 profiles | N/A | Reference |
| Expert reviewers | 1 | 18 lenses | 100+ | Complete |
| Investigations (craftworks) | 7 | 16+ sub-studies | Merged into decisions | Complete |
| Investigations (Agentverse) | 59 questions | 30 with experiments | Multi-contributor consensus | Active |
| Panel (academic) | 51 reviewers | 10 papers | 3-tier scoring | Active |
| **Total** | **~217+** | **~1,060+** | **~700+** | |

---

## Principles Across All Techniques

1. **Hand-compile before automating** — manual tracing/walkthrough before automated validation
2. **Findings → fixes → updated scenarios** — every finding has a lifecycle
3. **Hypothesis first, then validate** — experiments without a prior hypothesis produce findings that are hard to act on
4. **Persona diversity beats expert depth** — a maker and a compliance officer find different bugs than two architects
5. **Wave complexity gradient** — happy path before adversarial, always
6. **Spec-scenario-implementation unity** — scenarios that validate specs become regression tests
7. **Named experts > generic reviewers** — "What would Lattner say?" produces sharper findings than "review this code"
8. **Quantify everything** — persona scores, content prediction rates, token costs, coverage percentages
9. **"What we thought we learned" vs "What we actually learned"** — every investigation loop surfaces the delta
