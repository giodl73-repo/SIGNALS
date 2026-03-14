# simulate / T2

Root tier. Workspace-wide skills visible to all tiers.

## Skills

- /setup -- Initialize simulation infrastructure in a project with CODEX, config, and directory skeleton
- /domain-add -- Register a design directory with its domain type (compiler, runtime, bridge, api, emitter)
- /domain-list -- List all registered design domains with status summaries
- /domain-remove -- Unregister a design directory from the simulation project
- /codex-register -- Register a new unique 5-letter series code in the project CODEX
- /codex-list -- List all registered series codes across all domains
- /codex-check -- Validate no code collisions exist in the CODEX
- /codex-reserve -- Reserve a 5-letter code for future use without creating a series
- /series-new -- Create and scaffold a new scenario series with domain-appropriate directory structure
- /series-show -- Display series status including scenario progress, wave completion, and open findings
- /series-list -- List all series across all registered domains with progress summaries
- /series-complete -- Mark a series as complete after all scenarios are validated
- /scenario-new -- Create a new scenario with intent, input fixtures, and expected output placeholder
- /scenario-trace -- Guide hand-compilation of expected output from specs (enforces hand-compile-first)
- /scenario-validate -- Validate scenario completeness against domain-specific checklist
- /scenario-status -- Update scenario lifecycle status (planned, in-progress, complete, validated, wired)
- /finding-new -- Record a new finding with ID, severity, description, and linked scenario
- /finding-resolve -- Annotate finding resolution with DCR reference, spec amendment, and scenario update
- /finding-batch -- Group related findings by pattern into a DCR proposal
- /finding-list -- List findings with filters by series, severity, and resolution status
- /dcr-new -- Create a design change request from batched findings with affected specs
- /dcr-update -- Update DCR lifecycle status (Draft, Active, Integrated, Implemented, Closed)
- /dcr-list -- List DCRs with status filters and spec linkage
- /wire-scaffold -- Generate test file scaffolds from validated scenario expected outputs
- /wire-status -- Show wiring status tracking design-only vs test-backed scenarios
- /wire-validate -- Run coverage gates on wired tests (95% lines, 90% branches default)
- /report-status -- Generate overall simulation dashboard with aggregate metrics
- /report-coverage -- Produce spec coverage matrix showing which specs have scenario coverage
- /report-findings -- Generate findings scorecard by total, resolved, open, and severity
- /report-full -- Comprehensive simulation report with coverage, findings, DCRs, and cross-series maps
