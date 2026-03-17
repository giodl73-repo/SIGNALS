# signal / T1

Root tier. Workspace-wide skills visible to all tiers.

## Skills

- /signal-scout -- PM proves the idea. Market positioning, competitive landscape, feasibility, naming validation, compliance scan, market sizing, stakeholder alignment, positioning pitch, and requirements validation. Lightweight default.

- /signal-draft -- Author writes the design. Guided authoring of specifications, proposals with trade-off analysis, and pitch deck narratives. Lightweight default.

- /signal-review -- Team validates the design. Expert and discipline review of specs and code. Persona walkthrough for usability. 12-customer-persona evaluation for adoption. Full default.

- /signal-flow -- Domain developer simulates the process. Business lifecycle flows, agent conversations, automation triggers, data pipelines, integrations, throttle limits, and resilience under failure. Full default.
 *(T3 -- full runbook loaded on demand)*
- /signal-trace -- System developer simulates the platform. Request tracing, state validation, contract testing, component trees, deployment impact, migration safety, and permission walk-through. Full default.

- /signal-prove -- Prove what you believe. Hypothesis-first investigation decomposed into approachable steps -- state, research, prototype, analyze, interview, synthesize, publish. Full default.

- /signal-listen -- Team simulates post-ship feedback. Customer reactions, support ticket forecasts, and adoption curve simulation before the feature ships. Lightweight default.

- /signal-program -- Lead orchestrates all. Sequences scout -> draft -> review -> flow -> trace -> listen into a staged program plan with gates and topic tracking. Full default.
 *(T3 -- full runbook loaded on demand)*
- /signal-topic -- Anyone manages the topic narrative. Register topics, plan signal strategy, check coverage status, write shareable reports, synthesize the story, and capture the echo. Lightweight default.

- /signal-trace-skill -- Hand-compile a skill execution before building it. Given a skill spec and a test invocation, trace the 4-phase lifecycle (setup, execute, findings, amend) step by step -- producing the expected artifact as if the skill had run. Read the spec. Simulate setup (auto-detect from repo context). Run each stock role through their lens. Synthesize findings into the artifact. List 3 amend options. Deliver a verdict: useful or needs redesign? The hand-compiled artifact becomes the scenario baseline for testing. Findings feed back to the skill spec before implementation.
 *(T3 -- full runbook loaded on demand)*
- /signal-quest -- Quest namespace: define rubrics (/signal-quest-rubric), generate variations (/signal-quest-variate), score outputs (/signal-quest-score), find the golden prompt (/signal-quest-golden).

- /signal-mock -- Mock namespace: synthetic signal artifacts (/signal-mock-all), single namespace mock (/signal-mock-ns), coverage review (/signal-mock-review).
 *(T3 -- full runbook loaded on demand)*
- /signal-org -- Org namespace: role registry (/signal-org-roles), org chart (/signal-org-chart), org review (/signal-org-review), committee simulation (/signal-org-committee).

- /signal-quest-rubric -- Define what good output looks like for a skill. Given a skill spec and sample outputs, produce a scoring rubric: a ranked list of criteria (C-01, C-02...) each with a pass condition, weight, and category (correctness, depth, format, coverage). The rubric is the objective function for /signal-quest-golden. Start with 3-5 essential criteria; the rubric grows as /signal-quest-golden discovers excellence patterns.
 *(T3 -- full runbook loaded on demand)*
- /signal-quest-variate -- Generate N prompt variations of a skill body for comparison. Given a skill description and variation axes (role sequence, output format, lifecycle emphasis, stock role selection, phrasing), produce N distinct prompt formulations of the same skill. Each variation is a complete, runnable skill body -- not a diff. Variation axes are independent; combinations are intentional. Default N=5.

- /signal-quest-score -- Score a set of skill outputs against a rubric. Given outputs from N skill runs and a rubric file, evaluate each output against every criterion. Produce: per-criterion pass/fail per output, composite score per output, ranked leaderboard, excellence signals (outputs scoring unusually high on specific criteria), and failure patterns (criteria that fail consistently across all outputs -- rubric gap or skill gap?).
 *(T3 -- full runbook loaded on demand)*
- /signal-quest-golden -- Find the golden prompt for a skill through systematic variation and scoring. Full loop: (1) load rubric or call signal-quest-rubric to create one, (2) call signal-quest-variate to generate N variations, (3) call signal-quest-score to rank them, (4) identify excellence signals -- what made the top output better?, (5) extract the pattern, propose a rubric criterion update, (6) apply the update, (7) iterate from step 2 until dual convergence: all scenarios pass AND no new excellence patterns emerge across 2 consecutive rounds. Write the converged prompt as the skill body.

- /signal-scout-competitors -- Competitive landscape analysis leading with inertia as primary competitor.
- /signal-scout-feasibility -- Technical feasibility assessment with traffic-light ratings and budget chain.
- /signal-scout-naming -- Name generation and evaluation with multi-persona scoring.
- /signal-scout-compliance -- Regulatory and policy constraint scan before design begins.
- /signal-scout-market -- Market sizing and segment ranking by fit score.
- /signal-scout-stakeholders -- Stakeholder mapping with power/interest grid and veto risk ranking.
- /signal-scout-positioning -- Per-audience positioning statements with competitive differentiation.
- /signal-scout-requirements -- Requirements extraction with MoSCoW prioritization and dependency graph.
- /signal-draft-spec -- Specification authoring with guided section structure and self-review.
- /signal-draft-proposal -- Proposal or ADR with three-option minimum and recommendation rationale.
- /signal-draft-pitch -- Pitch deck narrative in exec, developer, and maker versions.
- /signal-draft-brainstorm -- Idea pool generation with inertia baseline and peer-comparison scoring. *(T3 -- full runbook loaded on demand)*
- /signal-review-design -- Multi-expert design review through 6 disciplines and domain-selected experts.
- /signal-review-code -- Multi-discipline code review with file-level annotations and pass/fail per discipline.
- /signal-review-users -- Five persona advocates walk through design with usability scores and cross-persona synthesis.
- /signal-review-customers -- Twelve customer personas evaluate feature for usefulness, clarity, and would-adopt.
- /signal-flow-lifecycle -- Multi-step business document lifecycle simulation with phase contracts and exception flows. *(T3 -- full runbook loaded on demand)*
- /signal-flow-conversation -- Multi-turn agent conversation simulation through topic graph with dead-end and loop detection.
- /signal-flow-trigger -- Automation trigger simulation showing fire order and side effects per field/event change. *(T3 -- full runbook loaded on demand)*
- /signal-flow-dataflow -- ETL pipeline and sync process tracing with data loss and schema mismatch detection.
- /signal-flow-integration -- Cross-system integration tracing through connectors and APIs with gap analysis.
- /signal-flow-throttle -- Rate-limit throughput simulation showing backpressure propagation and burst path gaps. *(T3 -- full runbook loaded on demand)*
- /signal-flow-resilience -- Degraded-condition simulation covering offline, partial failure, and eventual consistency. *(T3 -- full runbook loaded on demand)*
- /signal-trace-request -- Request hand-compilation through service boundaries with no boundary skipped.
- /signal-trace-state -- State transition hand-compilation with preconditions, postconditions, and invariant checks. *(T3 -- full runbook loaded on demand)*
- /signal-trace-contract -- Expected vs actual output comparison using three-directory pattern with mismatch severity. *(T3 -- full runbook loaded on demand)*
- /signal-trace-component -- User action tracing through UI component tree, state management, and re-render chain.
- /signal-trace-deployment -- Deployment sequence tracing with pre-checks, validation, and rollback path.
- /signal-trace-migration -- Schema change tracing with before/after data state and data loss detection.
- /signal-trace-permissions -- RBAC walk-through tracing who can do what with privilege escalation detection. *(T3 -- full runbook loaded on demand)*
- /signal-prove-hypothesis -- Hypothesis framing with claim, falsification condition, confidence, and experiment list.
- /signal-prove-websearch -- Web evidence gathering with direct quotes, URLs, and strength-of-evidence rating per source.
- /signal-prove-intelligence -- Internal source evidence search with file-path citations and relevance assessment.
- /signal-prove-prototype -- Smallest-possible prototype with defined measure and predicted vs actual results.
- /signal-prove-analysis -- Data pattern analysis distinguishing correlation from causation with source attribution.
- /signal-prove-interview -- Persona-driven stakeholder interview simulation grounded in documented role knowledge. *(T3 -- full runbook loaded on demand)*
- /signal-prove-synthesize -- Answer-first evidence synthesis with confidence rating and counter-evidence.
- /signal-prove-publish -- Investigation write-up as paper with abstract, method, findings, and limitations.
- /signal-prove-topic -- Full prove evidence campaign orchestrating hypothesis through synthesis in one command. *(T3 -- full runbook loaded on demand)*
- /signal-prove-program -- General-purpose research orchestrator for open-ended research questions.
- /signal-listen-feedback -- Pre-ship customer reaction simulation with per-persona NPS prediction and threshold gate.
- /signal-listen-support -- Top support ticket prediction for first 90 days with gap analysis. *(T3 -- full runbook loaded on demand)*
- /signal-listen-adoption -- Adoption curve simulation across Rogers archetypes with chasm analysis.
- /signal-program-plan -- Staged program plan generation with gates and topic tracking. *(T3 -- full runbook loaded on demand)*
- /signal-topic-new -- Topic registration with strategy planning and signal coverage plan.
- /signal-topic-status -- Terminal coverage display computed from signal glob against strategy.
- /signal-topic-report -- Shareable status document with progress table and readiness statement.
- /signal-topic-plan -- Signal strategy revision as new information arrives with user confirmation. *(T3 -- full runbook loaded on demand)*
- /signal-topic-story -- Editorial synthesis of all signals into a coherent narrative with recommendation. *(T3 -- full runbook loaded on demand)*
- /signal-topic-echo -- Unexpected findings synthesis asking what we learned that we did not expect. *(T3 -- full runbook loaded on demand)*
- /signal-mock-all -- Synthetic signal artifacts for all 9 namespaces with coverage picture. *(T3 -- full runbook loaded on demand)*
- /signal-mock-ns -- Mock artifact for a single namespace with category annotation. *(T3 -- full runbook loaded on demand)*
- /signal-mock-review -- Mock coverage review writing MOCK-ACCEPTED or REAL-REQUIRED per namespace. *(T3 -- full runbook loaded on demand)*
- /signal-org-roles -- Typed role registry generation for a domain with orientation, lens, and expertise.
- /signal-org-chart -- Org structure generation with areas, committees, and operating rhythms. *(T3 -- full runbook loaded on demand)*
- /signal-org-review -- Full org review running artifact through all relevant roles from .craft/roles/. *(T3 -- full runbook loaded on demand)*
- /signal-org-committee -- Committee meeting simulation for ROB, shiproom, or architecture board. *(T3 -- full runbook loaded on demand)*
- /signal-lifecycle -- 4-phase lifecycle (setup/execute/findings/amend) shared by all skills. Lightweight mode merges execute+findings, makes amend optional. Full mode runs all 4 phases explicitly.

- /artifact-writer -- Writes signal artifacts with standard frontmatter (skill, topic, item, date, skill_version, input). Enforces topic-item-date naming convention. Supports --json sidecar flag.

- /topic-scanner -- Discovers all signals for a topic by globbing simulations/**/topic-* files. Computes coverage against strategy.md planned signals.

- /skill-tracer -- Executes the trace-skill hand-compilation protocol. Reads the skill spec, runs each lifecycle phase against the test input, writes the hand-compiled artifact, and produces a verdict with any findings.

- /quest-engine -- Runs the quest loop: variate -> score -> extract -> evolve rubric -> repeat until dual convergence. Tracks rounds, rubric versions, and excellence patterns. Produces a convergence report with the golden prompt and the final rubric that defines what golden means for this skill.

