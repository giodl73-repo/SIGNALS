# sim-forge / T2

T2 tier.

## Skills

- /init-project -- Bootstrap a simulation project: create CODEX, global config, and default directory skeleton
- /register-design-dir -- Register a design directory with its domain type and convention metadata so it participates in simulations
- /configure-domain -- Define or update per-domain simulation conventions including directory structure, naming, finding format, and checklist templates
- /register-series-code -- Claim a unique 5-letter code in the CODEX, reject collisions, and bind it to a domain and owning series
- /scaffold-series -- Generate domain-appropriate directory structure, CLAUDE.md session driver, FINDINGS.md, INDEX.md, and COMPLETION-CRITERIA.md for a new series
- /create-scenario -- Create a new scenario with intent, input fixtures, and hand-compiled expected output; enforce hand-compile-first constraint
- /update-scenario-status -- Advance scenario lifecycle: planned → in-progress → complete → validated → wired
- /add-cross-series-ref -- Record a cross-series reference when a scenario touches features owned by another series
- /record-finding -- Append a new finding with ID, severity, description, and linked scenario; findings are immutable once recorded
- /resolve-finding -- Annotate a finding's resolution (DCR filed, spec amended, scenario updated) without modifying its original record
- /batch-findings-to-dcr -- Group related findings by pattern into a DCR proposal; link each finding to the new DCR
- /create-dcr -- Create a Design Change Request with affected specs, batched findings, and initial Draft status
- /update-dcr-status -- Advance DCR lifecycle: Draft → Active → Integrated → Implemented → Closed
- /wire-scenario-to-test -- Bridge a validated scenario to an automated test; blocked unless scenario status is 'validated'
- /generate-test-scaffold -- Emit test file scaffold from scenario's expected output, mapping scenario variations to individual test blocks
- /check-coverage-gates -- Validate coverage thresholds (95% lines/statements/functions, 90% branches) for wired scenarios
- /generate-coverage-report -- Produce spec coverage matrix showing which specs have scenario coverage and where gaps exist
- /generate-series-dashboard -- Render series-level progress: scenarios complete vs. planned, wave completion, open findings
- /generate-findings-scorecard -- Summarize findings by total, resolved, open, and severity across all series
- /generate-simulation-report -- Produce full simulation report: coverage matrix, findings scorecard, DCR rollup, cross-series dependency map
- /list-series -- List all scenario series across registered design directories with status summaries and wave progress *(inherited from T1)*
