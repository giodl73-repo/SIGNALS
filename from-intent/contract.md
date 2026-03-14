---
plugin: sim-forge
model: orchestrator-stage
confidence: 0.93
use_case_category: developer-tools
---

# Part 1: User Specification

Codify a design-time simulation lifecycle: scaffold scenario series, track findings, batch DCRs, wire to tests, report coverage

## Entities

- SimulationProject: Top-level container for a simulation campaign; holds CODEX, config, and registered design directories
- DesignDirectory: A registered directory containing specs/designs to be simulated; carries domain-type and directory-convention metadata
- DomainConfig: Per-domain simulation conventions: directory structure, naming rules, finding format, and validation checklist templates (compiler, runtime, bridge, API, emitter)
- SeriesCode: A unique 5-letter code registered in the project CODEX; maps to a domain and a ScenarioSeries to prevent collisions
- ScenarioSeries: A scaffolded collection of related scenarios; includes CLAUDE.md session driver, FINDINGS.md, INDEX.md, COMPLETION-CRITERIA.md, and wave structure
- Scenario: An individual simulation unit: intent, input fixtures, hand-compiled expected output, validation checklist, wave level, and lifecycle status
- Finding: A discovered spec gap or design issue with ID (F-01/SIM-01.1), severity, linked scenario, optional DCR link, and append-only resolution history
- DCR: Design Change Request batching related findings; tracks affected specs, status (Draft→Active→Integrated→Implemented→Closed), and implementation phase linkage
- TestWire: Bridge record linking a validated scenario to an automated test; tracks scaffold generation, wiring status, and coverage gate results
- CoverageReport: Snapshot of spec coverage, series progress, findings scorecard, wave completion, and DCR rollup across the simulation project

## Actions

- init-project: Bootstrap a simulation project: create CODEX, global config, and default directory skeleton
- register-design-dir: Register a design directory with its domain type and convention metadata so it participates in simulations
- configure-domain: Define or update per-domain simulation conventions including directory structure, naming, finding format, and checklist templates
- register-series-code: Claim a unique 5-letter code in the CODEX, reject collisions, and bind it to a domain and owning series
- scaffold-series: Generate domain-appropriate directory structure, CLAUDE.md session driver, FINDINGS.md, INDEX.md, and COMPLETION-CRITERIA.md for a new series
- list-series: List all scenario series across registered design directories with status summaries and wave progress
- create-scenario: Create a new scenario with intent, input fixtures, and hand-compiled expected output; enforce hand-compile-first constraint
- update-scenario-status: Advance scenario lifecycle: planned → in-progress → complete → validated → wired
- add-cross-series-ref: Record a cross-series reference when a scenario touches features owned by another series
- record-finding: Append a new finding with ID, severity, description, and linked scenario; findings are immutable once recorded
- resolve-finding: Annotate a finding's resolution (DCR filed, spec amended, scenario updated) without modifying its original record
- batch-findings-to-dcr: Group related findings by pattern into a DCR proposal; link each finding to the new DCR
- create-dcr: Create a Design Change Request with affected specs, batched findings, and initial Draft status
- update-dcr-status: Advance DCR lifecycle: Draft → Active → Integrated → Implemented → Closed
- wire-scenario-to-test: Bridge a validated scenario to an automated test; blocked unless scenario status is 'validated'
- generate-test-scaffold: Emit test file scaffold from scenario's expected output, mapping scenario variations to individual test blocks
- check-coverage-gates: Validate coverage thresholds (95% lines/statements/functions, 90% branches) for wired scenarios
- generate-coverage-report: Produce spec coverage matrix showing which specs have scenario coverage and where gaps exist
- generate-series-dashboard: Render series-level progress: scenarios complete vs. planned, wave completion, open findings
- generate-findings-scorecard: Summarize findings by total, resolved, open, and severity across all series
- generate-simulation-report: Produce full simulation report: coverage matrix, findings scorecard, DCR rollup, cross-series dependency map

## Relationships

- SimulationProject has-many DesignDirectory
- SimulationProject has-many SeriesCode
- SimulationProject has-many DCR
- SimulationProject has-many DomainConfig
- DesignDirectory belongs-to DomainConfig
- DesignDirectory has-many ScenarioSeries
- SeriesCode has-one ScenarioSeries
- ScenarioSeries has-many Scenario
- ScenarioSeries has-many Finding
- Scenario has-many Finding
- Scenario has-one TestWire
- Finding many-to-many DCR
- ScenarioSeries many-to-many ScenarioSeries

# Part 2: System Commitment

Persist state as structured Markdown files co-located with specs (CODEX.md, FINDINGS.md, INDEX.md, CLAUDE.md) so the plugin is zero-infra and human-readable without the tool. SeriesCode uniqueness enforced via CODEX.md parse on every register call. Scenario hand-compile gate enforced at create time — expected-output field must be non-empty before status can advance past 'planned'. Finding records are append-only YAML/Markdown blocks with a resolutions sub-array. DomainConfig drives scaffolding templates via a strategy pattern (one adapter per domain type: compiler, runtime, bridge, api, emitter). TestWire generation uses scenario expected-output as the assertion source; coverage gate check shells out to the project's test runner. CoverageReport commands assemble live snapshots from on-disk files rather than a separate DB.
