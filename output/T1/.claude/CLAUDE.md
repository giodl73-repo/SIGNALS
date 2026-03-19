# signal / root

Root tier.

## Skills

- /discover-competitors -- Competitive landscape analysis with inertia-first framing. Use --focus to expand scope: --focus market (sizing + segment *(inherited from T1)*
- /discover-feasibility -- Technical feasibility assessment. Use --focus for additional discovery dimensions: --focus compliance (regulatory constr *(inherited from T1)*
- /discover-risk -- Risk register for a feature or decision. What could go wrong? Lists top risks across dimensions: technical (implementati *(inherited from T1)*
- /discover-inertia -- Deep analysis of the inertia competitor -- the option to do nothing. Why would teams keep their current workaround inste *(inherited from T1)*
- /specify-spec -- Author a specification from intent with guided section structure. Pulls context from any scout signals for the topic. Gu *(inherited from T1, T3 -- full content loaded on demand)*
- /specify-proposal -- Author a proposal or ADR with options and trade-offs. Three options minimum (including do-nothing). Each option: descrip *(inherited from T1)*
- /specify-pitch -- Author a pitch deck narrative in exec, developer, and maker versions. Pulls from scout-positioning if available. Each ve *(inherited from T1)*
- /discover-brainstorm -- Generate a pool of ideas for any topic -- more than you need, so you can rank and filter. Each idea gets: name, one-line *(inherited from T1)*
- /validate-design -- Multi-expert review of a design artifact through 6 standard disciplines and auto-selected domain experts. Auto-select 3- *(inherited from T1)*
- /validate-code -- Multi-discipline code review of source files, PRs, or diffs. If a spec is provided, each discipline checks spec complian *(inherited from T1)*
- /validate-users -- 5 persona advocates walk through a design from their user perspective. Each persona narrates in first person, flags conf *(inherited from T1, T3 -- full content loaded on demand)*
- /validate-customers -- 12 customer personas (C-01 through C-12) evaluate a feature for usefulness, clarity, and would-adopt (all 1-5). Primary *(inherited from T1)*
- /simulate-lifecycle -- Simulate the full business process lifecycle and flow behavior. Use --focus to zoom into a specific flow dimension: --fo *(inherited from T1)*
- /simulate-conversation -- Simulate a multi-turn agent conversation through a topic graph. Walk the dialog path: user intents, agent responses, top *(inherited from T1)*
- /simulate-stress -- Simulate degraded conditions: offline, partial failure, eventual consistency. For each failure scenario: what state is t *(inherited from T1, T3 -- full content loaded on demand)*
- /simulate-request -- Hand-compile a request through service boundaries, APIs, and middleware. Step by step: entry point, authentication, rout *(inherited from T1)*
- /simulate-state -- Hand-compile state transitions: starting state, operations applied, expected outcome at each step. For each operation: p *(inherited from T1)*
- /simulate-contract -- Verify implementation against spec contract. Use --type to target a specific verification dimension: --type component (U *(inherited from T1)*
- /simulate-permissions -- Trace who can do what through RBAC, security roles, teams, and field-level security. For each operation: which roles can *(inherited from T1)*
- /discover-hypothesis -- State what you believe and what would change your mind. Entry point to a prove investigation. A hypothesis has: a claim *(inherited from T1)*
- /discover-websearch -- Search the public web for evidence supporting or refuting the hypothesis. For each search: query used, sources found, ev *(inherited from T1)*
- /discover-analysis -- Analyze existing data, telemetry, schemas, or scenarios for patterns that bear on the hypothesis. For each data source: *(inherited from T1, T3 -- full content loaded on demand)*
- /discover-synthesize -- Merge all investigation signals into an answer-first synthesis. Structure: answer (yes/no/maybe), confidence (0-100), ke *(inherited from T1)*
- /discover-orchestrate -- Orchestrate a full prove evidence campaign. Runs hypothesis, websearch, intelligence, analysis, synthesize in sequence. *(inherited from T1)*
- /validate-feedback -- Simulate customer reactions to a spec or design before it ships. All 12 customer personas (C-01 through C-12) read the s *(inherited from T1)*
- /validate-support -- Predict the top support tickets filed in the first 90 days. For each predicted ticket: title, category (how-to/bug/featu *(inherited from T1, T3 -- full content loaded on demand)*
- /validate-adoption -- Simulate the adoption curve across team archetypes. Map personas to Rogers archetypes (innovator/early-adopter/early-maj *(inherited from T1)*
- /tools-coverage -- Generate synthetic signal artifacts for all 9 namespaces in a single pass. Each mock follows the structural requirements *(inherited from T1)*
- /tools-preview -- Generate a mock artifact for a single namespace. Same annotation and category rules as mock-all. Use --skill to target a *(inherited from T1)*
- /tools-accept -- Step 2 of mock-first workflow: review mock coverage picture and produce MOCK-ACCEPTED or REAL-REQUIRED decisions per nam *(inherited from T1, T3 -- full content loaded on demand)*
- /specify-commitment -- Sequence skills into a staged program plan with gates and topic tracking. Generate program.yaml for the topic: stages (n *(inherited from T1)*
- /signal -- Show the Signal command index. Lists all available skills organized by namespace with one-line descriptions. Type /signa *(inherited from T1)*
- /signal-setup -- Configure Signal in your workspace after installation. Checks for existing CLAUDE.md and .github/copilot-instructions.md *(inherited from T1)*
- /signal-layout -- Show or change your Signal navigation layout. Five variants: A) grouped (9 namespaces), B) groups (5 phases: discover/sp *(inherited from T1)*
- /rhythm-status -- Show topic coverage and commitment readiness. DISPLAY ONLY. Use --view for supplementary perspectives: --view roadmap (w *(inherited from T1)*
- /rhythm-story -- Synthesize all signals into a coherent narrative. NOT a summary of each signal -- an editorial synthesis in the author's *(inherited from T1)*
- /quest-rubric -- Define what good output looks like for a skill. Given a skill spec and sample outputs, produce a scoring rubric: ranked *(inherited from T1)*
- /quest-variate -- Generate N distinct prompt variations of a skill body. Each variation is a complete, runnable skill body -- not a diff. *(inherited from T1)*
- /quest-score -- Score N skill outputs against a rubric. Per-criterion PASS/PARTIAL/FAIL with evidence quote. Composite score per output. *(inherited from T1, T3 -- full content loaded on demand)*
- /quest-golden -- Find the golden prompt through systematic variation and scoring. Full loop: load or create rubric, generate variations, *(inherited from T1)*
- /roles-scan -- Walk a repo and produce a draft org.yaml -- the org configuration contract. Pivot modes: directory, concept, service, do *(inherited from T1)*
- /roles-build -- Read a confirmed org.yaml and generate the full org. Outputs: (1) org-chart.md with ASCII box diagram, headcount by grou *(inherited from T1)*
- /roles-product-review -- Run Review of Business (ROB) stages. Stages: leadership (exec briefing), teams (all team self-reviews), pm (PM cross-ali *(inherited from T1, T3 -- full content loaded on demand)*
- /roles-pull-request -- Run a PR through the full org. Selects reviewers based on files changed -- compiler changes get compiler roles, security *(inherited from T1, T3 -- full content loaded on demand)*
- /roles-generate -- Generate a typed role registry for a domain. Analyzes product/codebase to determine what expert perspectives are needed. *(inherited from T1)*
- /roles-chart -- Generate org structure for a product or domain: areas, divisions, committees, operating rhythms. Reads existing .craft/r *(inherited from T1)*
- /roles-check -- Run any artifact through the full org. Reads .craft/roles/ and selects relevant reviewers based on artifact type. Each r *(inherited from T1)*
- /roles-committee -- Simulate a committee meeting before the real one. Types: ROB (product review, service review), shiproom (go/no-go), arch *(inherited from T1)*
- /rhythm-decide -- Run the full pre-commitment decision campaign. Orchestrates: scout-competitors, scout-feasibility, scout-risk, prove-hyp *(inherited from T1)*
- /rhythm-behavior -- Run the full technical simulation campaign. Orchestrates: flow-lifecycle, flow-conversation, trace-state, trace-contract *(inherited from T1)*
- /rhythm-qa -- Run the full design validation campaign. Orchestrates: review-design, review-users, review-customers, listen-feedback, l *(inherited from T1)*
- /rhythm-brief -- Run the full topic narrative campaign. Orchestrates: topic-new (register), topic-roadmap (plan signals), topic-status (c *(inherited from T1)*
- /signal-check -- Self-check your signals before committing. Analyzes all signal artifacts for a topic across 4 dimensions: SEQUENCE (did *(inherited from T1)*
- /discover-causal -- Test whether the causal mechanism linking your feature to the claimed outcome is actually sound. Given: hypothesis X cau *(inherited from T1, T3 -- full content loaded on demand)*
- /discover-coherence -- Check whether your discover signals agree with each other. Surfaces contradictions: if discover-competitors rates inerti *(inherited from T1)*
- /discover-compare -- Structured A vs B comparison for two approaches, features, or options. For each option: feasibility, inertia (would team *(inherited from T1)*
- /validate-inertia -- Validate the adoption case by stress-testing the inertia scenario. Why would users NOT adopt this feature even if it wor *(inherited from T1)*
- /discover-competitors-alt -- UNIFIED VERSION (A/B test against discover-competitors). Single prompt handles base competitive analysis AND optional fo *(inherited from T1)*
- /discover-feasibility-alt -- UNIFIED VERSION (A/B test against discover-feasibility). Single prompt handles base feasibility AND optional focus dimen *(inherited from T1)*
- /roles-create -- Create a new role or sub-role in .craft/roles/. Three modes: (1) name only -- /roles-create backend:healthcare generates *(inherited from T1)*
- /signal-lifecycle -- 4-phase lifecycle (setup/execute/findings/amend) shared by all skills. Lightweight mode merges execute+findings, makes amend optional. Full mode runs all 4 phases explicitly.
 *(inherited from T1)*
- /artifact-writer -- Writes signal artifacts with standard frontmatter (skill, topic, item, date, skill_version, input). Enforces topic-item-date naming convention. Supports --json sidecar flag.
 *(inherited from T1)*
- /topic-scanner -- Discovers all signals for a topic by globbing simulations/**/topic-* files. Computes coverage against strategy.md planned signals.
 *(inherited from T1)*
- /skill-tracer -- Executes the trace-skill hand-compilation protocol. Reads the skill spec, runs each lifecycle phase against the test input, writes the hand-compiled artifact, and produces a verdict with any findings.
 *(inherited from T1)*
- /quest-engine -- Runs the quest loop: variate -> score -> extract -> evolve rubric -> repeat until dual convergence. Tracks rounds, rubric versions, and excellence patterns. Produces a convergence report with the golden prompt and the final rubric that defines what golden means for this skill.
 *(inherited from T1)*

## Roles

- signal-pm (experiential)
- signal-dev (craft)
