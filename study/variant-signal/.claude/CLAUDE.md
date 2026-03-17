# signal / root

Root tier.

## Skills

- /scout -- PM proves the idea. Market positioning, competitive landscape, feasibility, naming validation, compliance scan, market sizing, stakeholder alignment, positioning pitch, and requirements validation. Lightweight default.
 *(inherited from T1)*
- /draft -- Author writes the design. Guided authoring of specifications, proposals with trade-off analysis, and pitch deck narratives. Lightweight default.
 *(inherited from T1)*
- /review -- Team validates the design. Expert and discipline review of specs and code. Persona walkthrough for usability. 12-customer-persona evaluation for adoption. Full default.
 *(inherited from T1)*
- /flow -- Domain developer simulates the process. Business lifecycle flows, agent conversations, automation triggers, data pipelines, integrations, throttle limits, and resilience under failure. Full default.
 *(inherited from T1, T3 -- full content loaded on demand)*
- /trace -- System developer simulates the platform. Request tracing, state validation, contract testing, component trees, deployment impact, migration safety, and permission walk-through. Full default.
 *(inherited from T1)*
- /prove -- Prove what you believe. Hypothesis-first investigation decomposed into approachable steps -- state, research, prototype, analyze, interview, synthesize, publish. Full default.
 *(inherited from T1)*
- /listen -- Team simulates post-ship feedback. Customer reactions, support ticket forecasts, and adoption curve simulation before the feature ships. Lightweight default.
 *(inherited from T1)*
- /program -- Lead orchestrates all. Sequences scout -> draft -> review -> flow -> trace -> listen into a staged program plan with gates and topic tracking. Full default.
 *(inherited from T1, T3 -- full content loaded on demand)*
- /topic -- Anyone manages the topic narrative. Register topics, plan signal strategy, check coverage status, write shareable reports, synthesize the story, and capture the echo. Lightweight default.
 *(inherited from T1)*
- /trace-skill -- Hand-compile a skill execution before building it. Given a skill spec and a test invocation, trace the 4-phase lifecycle (setup, execute, findings, amend) step by step -- producing the expected artifact as if the skill had run. Read the spec. Simulate setup (auto-detect from repo context). Run each stock role through their lens. Synthesize findings into the artifact. List 3 amend options. Deliver a verdict: useful or needs redesign? The hand-compiled artifact becomes the scenario baseline for testing. Findings feed back to the skill spec before implementation.
 *(inherited from T1, T3 -- full content loaded on demand)*
- /quest-rubric -- Define what good output looks like for a skill. Given a skill spec and sample outputs, produce a scoring rubric: a ranked list of criteria (C-01, C-02...) each with a pass condition, weight, and category (correctness, depth, format, coverage). The rubric is the objective function for /quest:golden. Start with 3-5 essential criteria; the rubric grows as /quest:golden discovers excellence patterns.
 *(inherited from T1, T3 -- full content loaded on demand)*
- /quest-variate -- Generate N prompt variations of a skill body for comparison. Given a skill description and variation axes (role sequence, output format, lifecycle emphasis, stock role selection, phrasing), produce N distinct prompt formulations of the same skill. Each variation is a complete, runnable skill body -- not a diff. Variation axes are independent; combinations are intentional. Default N=5.
 *(inherited from T1)*
- /quest-score -- Score a set of skill outputs against a rubric. Given outputs from N skill runs and a rubric file, evaluate each output against every criterion. Produce: per-criterion pass/fail per output, composite score per output, ranked leaderboard, excellence signals (outputs scoring unusually high on specific criteria), and failure patterns (criteria that fail consistently across all outputs -- rubric gap or skill gap?).
 *(inherited from T1, T3 -- full content loaded on demand)*
- /quest-golden -- Find the golden prompt for a skill through systematic variation and scoring. Full loop: (1) load rubric or call quest-rubric to create one, (2) call quest-variate to generate N variations, (3) call quest-score to rank them, (4) identify excellence signals -- what made the top output better?, (5) extract the pattern, propose a rubric criterion update, (6) apply the update, (7) iterate from step 2 until dual convergence: all scenarios pass AND no new excellence patterns emerge across 2 consecutive rounds. Write the converged prompt as the skill body. Dual convergence = the golden prompt.
 *(inherited from T1, T3 -- full content loaded on demand)*
- /scout-competitors -- Competitive landscape analysis leading with inertia as primary competitor. *(inherited from T1)*
- /scout-feasibility -- Technical feasibility assessment with traffic-light ratings and budget chain. *(inherited from T1)*
- /scout-naming -- Name generation and evaluation with multi-persona scoring. *(inherited from T1)*
- /scout-compliance -- Regulatory and policy constraint scan before design begins. *(inherited from T1)*
- /scout-market -- Market sizing and segment ranking by fit score. *(inherited from T1)*
- /scout-stakeholders -- Stakeholder mapping with power/interest grid and veto risk ranking. *(inherited from T1)*
- /scout-positioning -- Per-audience positioning statements with competitive differentiation. *(inherited from T1)*
- /scout-requirements -- Requirements extraction with MoSCoW prioritization and dependency graph. *(inherited from T1)*
- /draft-spec -- Specification authoring with guided section structure and self-review. *(inherited from T1)*
- /draft-proposal -- Proposal or ADR with three-option minimum and recommendation rationale. *(inherited from T1)*
- /draft-pitch -- Pitch deck narrative in exec, developer, and maker versions. *(inherited from T1)*
- /draft-brainstorm -- Idea pool generation with inertia baseline and peer-comparison scoring. *(inherited from T1, T3 -- full content loaded on demand)*
- /review-design -- Multi-expert design review through 6 disciplines and domain-selected experts. *(inherited from T1)*
- /review-code -- Multi-discipline code review with file-level annotations and pass/fail per discipline. *(inherited from T1)*
- /review-users -- Five persona advocates walk through design with usability scores and cross-persona synthesis. *(inherited from T1)*
- /review-customers -- Twelve customer personas evaluate feature for usefulness, clarity, and would-adopt. *(inherited from T1)*
- /flow-lifecycle -- Multi-step business document lifecycle simulation with phase contracts and exception flows. *(inherited from T1, T3 -- full content loaded on demand)*
- /flow-conversation -- Multi-turn agent conversation simulation through topic graph with dead-end and loop detection. *(inherited from T1)*
- /flow-trigger -- Automation trigger simulation showing fire order and side effects per field/event change. *(inherited from T1, T3 -- full content loaded on demand)*
- /flow-dataflow -- ETL pipeline and sync process tracing with data loss and schema mismatch detection. *(inherited from T1)*
- /flow-integration -- Cross-system integration tracing through connectors and APIs with gap analysis. *(inherited from T1)*
- /flow-throttle -- Rate-limit throughput simulation showing backpressure propagation and burst path gaps. *(inherited from T1, T3 -- full content loaded on demand)*
- /flow-resilience -- Degraded-condition simulation covering offline, partial failure, and eventual consistency. *(inherited from T1, T3 -- full content loaded on demand)*
- /trace-request -- Request hand-compilation through service boundaries with no boundary skipped. *(inherited from T1)*
- /trace-state -- State transition hand-compilation with preconditions, postconditions, and invariant checks. *(inherited from T1, T3 -- full content loaded on demand)*
- /trace-contract -- Expected vs actual output comparison using three-directory pattern with mismatch severity. *(inherited from T1, T3 -- full content loaded on demand)*
- /trace-component -- User action tracing through UI component tree, state management, and re-render chain. *(inherited from T1)*
- /trace-deployment -- Deployment sequence tracing with pre-checks, validation, and rollback path. *(inherited from T1)*
- /trace-migration -- Schema change tracing with before/after data state and data loss detection. *(inherited from T1)*
- /trace-permissions -- RBAC walk-through tracing who can do what with privilege escalation detection. *(inherited from T1, T3 -- full content loaded on demand)*
- /prove-hypothesis -- Hypothesis framing with claim, falsification condition, confidence, and experiment list. *(inherited from T1)*
- /prove-websearch -- Web evidence gathering with direct quotes, URLs, and strength-of-evidence rating per source. *(inherited from T1)*
- /prove-intelligence -- Internal source evidence search with file-path citations and relevance assessment. *(inherited from T1)*
- /prove-prototype -- Smallest-possible prototype with defined measure and predicted vs actual results. *(inherited from T1)*
- /prove-analysis -- Data pattern analysis distinguishing correlation from causation with source attribution. *(inherited from T1)*
- /prove-interview -- Persona-driven stakeholder interview simulation grounded in documented role knowledge. *(inherited from T1, T3 -- full content loaded on demand)*
- /prove-synthesize -- Answer-first evidence synthesis with confidence rating and counter-evidence. *(inherited from T1)*
- /prove-publish -- Investigation write-up as paper with abstract, method, findings, and limitations. *(inherited from T1)*
- /prove-topic -- Full prove evidence campaign orchestrating hypothesis through synthesis in one command. *(inherited from T1, T3 -- full content loaded on demand)*
- /prove-program -- General-purpose research orchestrator for open-ended research questions. *(inherited from T1)*
- /listen-feedback -- Pre-ship customer reaction simulation with per-persona NPS prediction and threshold gate. *(inherited from T1)*
- /listen-support -- Top support ticket prediction for first 90 days with gap analysis. *(inherited from T1, T3 -- full content loaded on demand)*
- /listen-adoption -- Adoption curve simulation across Rogers archetypes with chasm analysis. *(inherited from T1)*
- /program-plan -- Staged program plan generation with gates and topic tracking. *(inherited from T1, T3 -- full content loaded on demand)*
- /topic-new -- Topic registration with strategy planning and signal coverage plan. *(inherited from T1)*
- /topic-status -- Terminal coverage display computed from signal glob against strategy. *(inherited from T1)*
- /topic-report -- Shareable status document with progress table and readiness statement. *(inherited from T1)*
- /topic-plan -- Signal strategy revision as new information arrives with user confirmation. *(inherited from T1, T3 -- full content loaded on demand)*
- /topic-story -- Editorial synthesis of all signals into a coherent narrative with recommendation. *(inherited from T1, T3 -- full content loaded on demand)*
- /topic-echo -- Unexpected findings synthesis asking what we learned that we did not expect. *(inherited from T1, T3 -- full content loaded on demand)*
- /mock-all -- Synthetic signal artifacts for all 9 namespaces with coverage picture. *(inherited from T1, T3 -- full content loaded on demand)*
- /mock-ns -- Mock artifact for a single namespace with category annotation. *(inherited from T1, T3 -- full content loaded on demand)*
- /mock-review -- Mock coverage review writing MOCK-ACCEPTED or REAL-REQUIRED per namespace. *(inherited from T1, T3 -- full content loaded on demand)*
- /org-roles -- Typed role registry generation for a domain with orientation, lens, and expertise. *(inherited from T1)*
- /org-chart -- Org structure generation with areas, committees, and operating rhythms. *(inherited from T1, T3 -- full content loaded on demand)*
- /org-review -- Full org review running artifact through all relevant roles from .craft/roles/. *(inherited from T1, T3 -- full content loaded on demand)*
- /org-committee -- Committee meeting simulation for ROB, shiproom, or architecture board. *(inherited from T1, T3 -- full content loaded on demand)*
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
