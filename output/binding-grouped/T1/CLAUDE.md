# signal / T1

Root tier. Workspace-wide skills visible to all tiers.

## Skills

- /scout -- Scout namespace -- 8 skills for discovery and research.

/scout-competitors  -> competitive landscape + inertia analysis
/scout-feasibility  -> technical feasibility + team/timeline assessment
/scout-naming       -> name validation + trademark + domain search
/scout-compliance   -> regulatory framework scan
/scout-market       -> market sizing + segment analysis
/scout-stakeholders -> stakeholder map + power/interest grid
/scout-positioning  -> positioning framework + category definition
/scout-requirements -> requirements extraction + ambiguity flags

Run any sub-skill directly, or describe your topic and the most relevant scout skill will run.

- /draft -- Draft namespace -- 4 skills for authoring design artifacts.

/draft-spec        -> technical specification with guided section structure
/draft-proposal    -> proposal or ADR with three-option minimum
/draft-pitch       -> pitch deck narrative in exec, developer, and maker versions
/draft-brainstorm  -> idea pool with inertia baseline and peer-comparison scoring

Run any sub-skill directly, or describe your artifact and the most relevant draft skill will run.

- /review -- Review namespace -- 4 skills for design and code validation.

/review-design     -> multi-expert design review through 6 disciplines
/review-code       -> multi-discipline code review with file-level annotations
/review-users      -> 5 persona advocates walk through design with usability scores
/review-customers  -> 12 customer personas evaluate for usefulness and would-adopt

Run any sub-skill directly, or describe your artifact and the most relevant review skill will run.

- /flow -- Flow namespace -- 7 skills for domain process simulation.

/flow-lifecycle    -> business document lifecycle with phase contracts and exception flows
/flow-conversation -> multi-turn agent conversation with dead-end and loop detection
/flow-trigger      -> automation trigger fire order and side effects per event
/flow-dataflow     -> ETL pipeline tracing with data loss and schema mismatch detection
/flow-integration  -> cross-system integration tracing with gap analysis
/flow-throttle     -> rate-limit throughput and backpressure propagation
/flow-resilience   -> degraded-condition simulation: offline, partial failure, eventual consistency

Run any sub-skill directly, or describe your scenario and the most relevant flow skill will run.
 *(T3 -- full runbook loaded on demand)*
- /trace -- Trace namespace -- 7 skills for platform-level simulation.

/trace-request     -> request hand-compilation through service boundaries
/trace-state       -> state transition with preconditions, postconditions, invariants
/trace-contract    -> expected vs actual output comparison with mismatch severity
/trace-component   -> user action through UI component tree and re-render chain
/trace-deployment  -> deployment sequence with pre-checks and rollback path
/trace-migration   -> schema change with before/after data state and loss detection
/trace-permissions -> RBAC walk-through with privilege escalation detection

Run any sub-skill directly, or describe your system and the most relevant trace skill will run.

- /prove -- Prove namespace -- 9 skills for hypothesis-driven investigation.

/prove-hypothesis  -> hypothesis framing with claim, falsification, confidence, experiments
/prove-websearch   -> web evidence with direct quotes, URLs, strength-of-evidence rating
/prove-intelligence -> internal source search with file-path citations
/prove-prototype   -> smallest-possible prototype with predicted vs actual results
/prove-analysis    -> data pattern analysis distinguishing correlation from causation
/prove-interview   -> persona-driven stakeholder interview simulation
/prove-synthesize  -> answer-first evidence synthesis with confidence and counter-evidence
/prove-publish     -> investigation write-up as paper with abstract and limitations
/prove-topic       -> full prove campaign orchestrating hypothesis through synthesis

Run any sub-skill directly, or describe your hypothesis and the most relevant prove skill will run.

- /listen -- Listen namespace -- 3 skills for post-ship signal simulation.

/listen-feedback  -> pre-ship customer reaction with per-persona NPS prediction
/listen-support   -> top support ticket prediction for first 90 days
/listen-adoption  -> adoption curve simulation across Rogers archetypes with chasm analysis

Run any sub-skill directly, or describe your feature and the most relevant listen skill will run.

- /program -- Program namespace -- 2 skills for orchestration and planning.

/program-plan  -> staged program plan with gates and topic tracking
/prove-program -> general-purpose research orchestrator for open-ended questions

Run any sub-skill directly, or describe your program and the most relevant skill will run.
 *(T3 -- full runbook loaded on demand)*
- /topic -- Topic namespace -- 6 skills for narrative management.

/topic-new     -> topic registration with strategy planning and signal coverage plan
/topic-status  -> terminal coverage display computed from signal glob
/topic-report  -> shareable status document with progress table and readiness statement
/topic-plan    -> signal strategy revision as new information arrives
/topic-story   -> editorial synthesis of all signals into a coherent narrative
/topic-echo    -> unexpected findings synthesis: what did we learn that we did not expect?

Run any sub-skill directly, or describe your topic management need and the most relevant skill will run.

- /quest -- Quest namespace -- 4 skills for prompt engineering and golden prompt discovery.

/quest-rubric  -> define what good output looks like: ranked criteria with pass conditions
/quest-variate -> generate N prompt variations of a skill body for comparison
/quest-score   -> score skill outputs against a rubric with leaderboard and failure patterns
/quest-golden  -> find the golden prompt through systematic variation and scoring

Run any sub-skill directly, or describe your optimization goal and the most relevant quest skill will run.

- /mock -- Mock namespace -- 3 skills for synthetic signal generation.

/mock-all     -> synthetic signal artifacts for all 9 namespaces with coverage picture
/mock-ns      -> mock artifact for a single namespace with category annotation
/mock-review  -> coverage review writing MOCK-ACCEPTED or REAL-REQUIRED per namespace

Run any sub-skill directly, or describe your coverage need and the most relevant mock skill will run.
 *(T3 -- full runbook loaded on demand)*
- /org -- Org namespace -- 4 skills for organizational simulation.

/org-roles      -> typed role registry with orientation, lens, and expertise
/org-chart      -> org structure with areas, committees, and operating rhythms
/org-review     -> full org review running artifact through all relevant roles
/org-committee  -> committee meeting simulation for ROB, shiproom, or architecture board

Run any sub-skill directly, or describe your organizational need and the most relevant skill will run.

- /trace-skill -- Hand-compile a skill execution before building it. Given a skill spec and a test invocation, trace the 4-phase lifecycle (setup, execute, findings, amend) step by step -- producing the expected artifact as if the skill had run. Read the spec. Simulate setup (auto-detect from repo context). Run each stock role through their lens. Synthesize findings into the artifact. List 3 amend options. Deliver a verdict: useful or needs redesign? The hand-compiled artifact becomes the scenario baseline for testing. Findings feed back to the skill spec before implementation.
 *(T3 -- full runbook loaded on demand)*
- /quest-rubric -- Define what good output looks like for a skill. Given a skill spec and sample outputs, produce a scoring rubric: a ranked list of criteria (C-01, C-02...) each with a pass condition, weight, and category (correctness, depth, format, coverage). The rubric is the objective function for /quest:golden. Start with 3-5 essential criteria; the rubric grows as /quest:golden discovers excellence patterns.
 *(T3 -- full runbook loaded on demand)*
- /quest-variate -- Generate N prompt variations of a skill body for comparison. Given a skill description and variation axes (role sequence, output format, lifecycle emphasis, stock role selection, phrasing), produce N distinct prompt formulations of the same skill. Each variation is a complete, runnable skill body -- not a diff. Variation axes are independent; combinations are intentional. Default N=5.

- /quest-score -- Score a set of skill outputs against a rubric. Given outputs from N skill runs and a rubric file, evaluate each output against every criterion. Produce: per-criterion pass/fail per output, composite score per output, ranked leaderboard, excellence signals (outputs scoring unusually high on specific criteria), and failure patterns (criteria that fail consistently across all outputs -- rubric gap or skill gap?).
 *(T3 -- full runbook loaded on demand)*
- /quest-golden -- Find the golden prompt for a skill through systematic variation and scoring. Full loop: (1) load rubric or call quest-rubric to create one, (2) call quest-variate to generate N variations, (3) call quest-score to rank them, (4) identify excellence signals -- what made the top output better?, (5) extract the pattern, propose a rubric criterion update, (6) apply the update, (7) iterate from step 2 until dual convergence: all scenarios pass AND no new excellence patterns emerge across 2 consecutive rounds. Write the converged prompt as the skill body. Dual convergence = the golden prompt.

- /scout-competitors -- Competitive landscape analysis leading with inertia as primary competitor.
- /scout-feasibility -- Technical feasibility assessment with traffic-light ratings and budget chain.
- /scout-naming -- Name generation and evaluation with multi-persona scoring.
- /scout-compliance -- Regulatory and policy constraint scan before design begins.
- /scout-market -- Market sizing and segment ranking by fit score.
- /scout-stakeholders -- Stakeholder mapping with power/interest grid and veto risk ranking.
- /scout-positioning -- Per-audience positioning statements with competitive differentiation.
- /scout-requirements -- Requirements extraction with MoSCoW prioritization and dependency graph.
- /draft-spec -- Specification authoring with guided section structure and self-review.
- /draft-proposal -- Proposal or ADR with three-option minimum and recommendation rationale.
- /draft-pitch -- Pitch deck narrative in exec, developer, and maker versions.
- /draft-brainstorm -- Idea pool generation with inertia baseline and peer-comparison scoring. *(T3 -- full runbook loaded on demand)*
- /review-design -- Multi-expert design review through 6 disciplines and domain-selected experts.
- /review-code -- Multi-discipline code review with file-level annotations and pass/fail per discipline.
- /review-users -- Five persona advocates walk through design with usability scores and cross-persona synthesis.
- /review-customers -- Twelve customer personas evaluate feature for usefulness, clarity, and would-adopt.
- /flow-lifecycle -- Multi-step business document lifecycle simulation with phase contracts and exception flows. *(T3 -- full runbook loaded on demand)*
- /flow-conversation -- Multi-turn agent conversation simulation through topic graph with dead-end and loop detection.
- /flow-trigger -- Automation trigger simulation showing fire order and side effects per field/event change. *(T3 -- full runbook loaded on demand)*
- /flow-dataflow -- ETL pipeline and sync process tracing with data loss and schema mismatch detection.
- /flow-integration -- Cross-system integration tracing through connectors and APIs with gap analysis.
- /flow-throttle -- Rate-limit throughput simulation showing backpressure propagation and burst path gaps. *(T3 -- full runbook loaded on demand)*
- /flow-resilience -- Degraded-condition simulation covering offline, partial failure, and eventual consistency. *(T3 -- full runbook loaded on demand)*
- /trace-request -- Request hand-compilation through service boundaries with no boundary skipped.
- /trace-state -- State transition hand-compilation with preconditions, postconditions, and invariant checks. *(T3 -- full runbook loaded on demand)*
- /trace-contract -- Expected vs actual output comparison using three-directory pattern with mismatch severity. *(T3 -- full runbook loaded on demand)*
- /trace-component -- User action tracing through UI component tree, state management, and re-render chain.
- /trace-deployment -- Deployment sequence tracing with pre-checks, validation, and rollback path.
- /trace-migration -- Schema change tracing with before/after data state and data loss detection.
- /trace-permissions -- RBAC walk-through tracing who can do what with privilege escalation detection. *(T3 -- full runbook loaded on demand)*
- /prove-hypothesis -- Hypothesis framing with claim, falsification condition, confidence, and experiment list.
- /prove-websearch -- Web evidence gathering with direct quotes, URLs, and strength-of-evidence rating per source.
- /prove-intelligence -- Internal source evidence search with file-path citations and relevance assessment.
- /prove-prototype -- Smallest-possible prototype with defined measure and predicted vs actual results.
- /prove-analysis -- Data pattern analysis distinguishing correlation from causation with source attribution.
- /prove-interview -- Persona-driven stakeholder interview simulation grounded in documented role knowledge. *(T3 -- full runbook loaded on demand)*
- /prove-synthesize -- Answer-first evidence synthesis with confidence rating and counter-evidence.
- /prove-publish -- Investigation write-up as paper with abstract, method, findings, and limitations.
- /prove-topic -- Full prove evidence campaign orchestrating hypothesis through synthesis in one command. *(T3 -- full runbook loaded on demand)*
- /prove-program -- General-purpose research orchestrator for open-ended research questions.
- /listen-feedback -- Pre-ship customer reaction simulation with per-persona NPS prediction and threshold gate.
- /listen-support -- Top support ticket prediction for first 90 days with gap analysis. *(T3 -- full runbook loaded on demand)*
- /listen-adoption -- Adoption curve simulation across Rogers archetypes with chasm analysis.
- /program-plan -- Staged program plan generation with gates and topic tracking. *(T3 -- full runbook loaded on demand)*
- /topic-new -- Topic registration with strategy planning and signal coverage plan.
- /topic-status -- Terminal coverage display computed from signal glob against strategy.
- /topic-report -- Shareable status document with progress table and readiness statement.
- /topic-plan -- Signal strategy revision as new information arrives with user confirmation. *(T3 -- full runbook loaded on demand)*
- /topic-story -- Editorial synthesis of all signals into a coherent narrative with recommendation. *(T3 -- full runbook loaded on demand)*
- /topic-echo -- Unexpected findings synthesis asking what we learned that we did not expect. *(T3 -- full runbook loaded on demand)*
- /mock-all -- Synthetic signal artifacts for all 9 namespaces with coverage picture. *(T3 -- full runbook loaded on demand)*
- /mock-ns -- Mock artifact for a single namespace with category annotation. *(T3 -- full runbook loaded on demand)*
- /mock-review -- Mock coverage review writing MOCK-ACCEPTED or REAL-REQUIRED per namespace. *(T3 -- full runbook loaded on demand)*
- /org-roles -- Typed role registry generation for a domain with orientation, lens, and expertise.
- /org-chart -- Org structure generation with areas, committees, and operating rhythms. *(T3 -- full runbook loaded on demand)*
- /org-review -- Full org review running artifact through all relevant roles from .craft/roles/. *(T3 -- full runbook loaded on demand)*
- /org-committee -- Committee meeting simulation for ROB, shiproom, or architecture board. *(T3 -- full runbook loaded on demand)*
- /signal-lifecycle -- 4-phase lifecycle (setup/execute/findings/amend) shared by all skills. Lightweight mode merges execute+findings, makes amend optional. Full mode runs all 4 phases explicitly.

- /artifact-writer -- Writes signal artifacts with standard frontmatter (skill, topic, item, date, skill_version, input). Enforces topic-item-date naming convention. Supports --json sidecar flag.

- /topic-scanner -- Discovers all signals for a topic by globbing simulations/**/topic-* files. Computes coverage against strategy.md planned signals.

- /skill-tracer -- Executes the trace-skill hand-compilation protocol. Reads the skill spec, runs each lifecycle phase against the test input, writes the hand-compiled artifact, and produces a verdict with any findings.

- /quest-engine -- Runs the quest loop: variate -> score -> extract -> evolve rubric -> repeat until dual convergence. Tracks rounds, rubric versions, and excellence patterns. Produces a convergence report with the golden prompt and the final rubric that defines what golden means for this skill.

