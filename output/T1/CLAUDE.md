# signal / T1

Root tier. Workspace-wide skills visible to all tiers.

## Skills

- /scout -- PM proves the idea. Market positioning, competitive landscape, feasibility, naming validation, compliance scan, market sizing, stakeholder alignment, positioning pitch, and requirements validation. Lightweight default.

- /draft -- Author writes the design. Guided authoring of specifications, proposals with trade-off analysis, and pitch deck narratives. Lightweight default.

- /review -- Team validates the design. Expert and discipline review of specs and code. Persona walkthrough for usability. 12-customer-persona evaluation for adoption. Full default.

- /flow -- Domain developer simulates the process. Business lifecycle flows, agent conversations, automation triggers, data pipelines, integrations, throttle limits, and resilience under failure. Full default.

- /trace -- System developer simulates the platform. Request tracing, state validation, contract testing, component trees, deployment impact, migration safety, and permission walk-through. Full default.

- /prove -- Prove what you believe. Hypothesis-first investigation decomposed into approachable steps -- state, research, prototype, analyze, interview, synthesize, publish. Full default.

- /listen -- Team simulates post-ship feedback. Customer reactions, support ticket forecasts, and adoption curve simulation before the feature ships. Lightweight default.

- /program -- Lead orchestrates all. Sequences scout -> draft -> review -> flow -> trace -> listen into a staged program plan with gates and topic tracking. Full default.

- /topic -- Anyone manages the topic narrative. Register topics, plan signal strategy, check coverage status, write shareable reports, synthesize the story, and capture the echo. Lightweight default.

- /trace-skill -- Hand-compile a skill execution before building it. Given a skill spec and a test invocation, trace the 4-phase lifecycle (setup, execute, findings, amend) step by step -- producing the expected artifact as if the skill had run. Read the spec. Simulate setup (auto-detect from repo context). Run each stock role through their lens. Synthesize findings into the artifact. List 3 amend options. Deliver a verdict: useful or needs redesign? The hand-compiled artifact becomes the scenario baseline for testing. Findings feed back to the skill spec before implementation.

- /quest-rubric -- Define what good output looks like for a skill. Given a skill spec and sample outputs, produce a scoring rubric: a ranked list of criteria (C-01, C-02...) each with a pass condition, weight, and category (correctness, depth, format, coverage). The rubric is the objective function for /quest:golden. Start with 3-5 essential criteria; the rubric grows as /quest:golden discovers excellence patterns.

- /quest-variate -- Generate N prompt variations of a skill body for comparison. Given a skill description and variation axes (role sequence, output format, lifecycle emphasis, stock role selection, phrasing), produce N distinct prompt formulations of the same skill. Each variation is a complete, runnable skill body -- not a diff. Variation axes are independent; combinations are intentional. Default N=5.

- /quest-score -- Score a set of skill outputs against a rubric. Given outputs from N skill runs and a rubric file, evaluate each output against every criterion. Produce: per-criterion pass/fail per output, composite score per output, ranked leaderboard, excellence signals (outputs scoring unusually high on specific criteria), and failure patterns (criteria that fail consistently across all outputs -- rubric gap or skill gap?).

- /quest-golden -- Find the golden prompt for a skill through systematic variation and scoring. Full loop: (1) load rubric or call quest-rubric to create one, (2) call quest-variate to generate N variations, (3) call quest-score to rank them, (4) identify excellence signals -- what made the top output better?, (5) extract the pattern, propose a rubric criterion update, (6) apply the update, (7) iterate from step 2 until dual convergence: all scenarios pass AND no new excellence patterns emerge across 2 consecutive rounds. Write the converged prompt as the skill body. Dual convergence = the golden prompt.

- /signal-lifecycle -- 4-phase lifecycle (setup/execute/findings/amend) shared by all skills. Lightweight mode merges execute+findings, makes amend optional. Full mode runs all 4 phases explicitly.

- /artifact-writer -- Writes signal artifacts with standard frontmatter (skill, topic, item, date, skill_version, input). Enforces topic-item-date naming convention. Supports --json sidecar flag.

- /topic-scanner -- Discovers all signals for a topic by globbing simulations/**/topic-* files. Computes coverage against strategy.md planned signals.

- /skill-tracer -- Executes the trace-skill hand-compilation protocol. Reads the skill spec, runs each lifecycle phase against the test input, writes the hand-compiled artifact, and produces a verdict with any findings.

- /quest-engine -- Runs the quest loop: variate -> score -> extract -> evolve rubric -> repeat until dual convergence. Tracks rounds, rubric versions, and excellence patterns. Produces a convergence report with the golden prompt and the final rubric that defines what golden means for this skill.

