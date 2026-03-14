---
plugin: simulate
model: orchestrator-multi-tier
confidence: 0.92
use_case_category: developer-tools
source: design/simulate/intent.md
generated: 2026-03-12
---

# Part 1: User Specification

A Claude Code plugin that codifies design-time simulation methodology -- running hand-compiled scenarios against specs and designs to find gaps before writing code. Manages the full lifecycle from scenario creation through findings tracking, DCR filing, test wiring, and coverage reporting across multiple design domains.

## Entities

- Domain: A registered design directory with type and conventions, stored in _simulate.yaml
- Series: A collection of related scenarios with a 5-letter code, stored in {domain}/scenarios/{code}/
- Scenario: An individual test case within a series with intent, fixtures, expected output, and validation checklist
- Finding: A gap or issue discovered during simulation with ID, severity, scenario linkage, and resolution history
- DCR: A design change request batching related findings with affected specs and lifecycle status
- Codex: Project-wide registry of 5-letter series codes preventing collisions across domains
- Wave: Complexity grouping within a series (Wave 1 = happy path, Wave 4+ = adversarial)
- WireMap: Mapping from validated design scenarios to automated test files with coverage gate results
- Campaign: Top-level simulation campaign container with registered domains and aggregate metrics
- DomainConfig: Per-domain simulation conventions including directory structure, naming, finding format, and checklist templates

## Actions

- setup: Initialize simulation infrastructure in a project with CODEX, config, and directory skeleton
- domain-add: Register a design directory with its domain type (compiler, runtime, bridge, api, emitter)
- domain-list: List all registered design domains with status summaries
- domain-remove: Unregister a design directory from the simulation project
- codex-register: Register a new unique 5-letter series code in the project CODEX
- codex-list: List all registered series codes across all domains
- codex-check: Validate no code collisions exist in the CODEX
- codex-reserve: Reserve a 5-letter code for future use without creating a series
- series-new: Create and scaffold a new scenario series with domain-appropriate directory structure
- series-show: Display series status including scenario progress, wave completion, and open findings
- series-list: List all series across all registered domains with progress summaries
- series-complete: Mark a series as complete after all scenarios are validated
- scenario-new: Create a new scenario with intent, input fixtures, and expected output placeholder
- scenario-trace: Guide hand-compilation of expected output from specs (enforces hand-compile-first)
- scenario-validate: Validate scenario completeness against domain-specific checklist
- scenario-status: Update scenario lifecycle status (planned, in-progress, complete, validated, wired)
- finding-new: Record a new finding with ID, severity, description, and linked scenario
- finding-resolve: Annotate finding resolution with DCR reference, spec amendment, and scenario update
- finding-batch: Group related findings by pattern into a DCR proposal
- finding-list: List findings with filters by series, severity, and resolution status
- dcr-new: Create a design change request from batched findings with affected specs
- dcr-update: Update DCR lifecycle status (Draft, Active, Integrated, Implemented, Closed)
- dcr-list: List DCRs with status filters and spec linkage
- wire-scaffold: Generate test file scaffolds from validated scenario expected outputs
- wire-status: Show wiring status tracking design-only vs test-backed scenarios
- wire-validate: Run coverage gates on wired tests (95% lines, 90% branches default)
- report-status: Generate overall simulation dashboard with aggregate metrics
- report-coverage: Produce spec coverage matrix showing which specs have scenario coverage
- report-findings: Generate findings scorecard by total, resolved, open, and severity
- report-full: Comprehensive simulation report with coverage, findings, DCRs, and cross-series maps

## Relationships

- Campaign has-many Domain
- Campaign has-many Codex
- Campaign has-many DCR
- Domain belongs-to DomainConfig
- Domain has-many Series
- Codex has-one Series
- Series has-many Scenario
- Series has-many Finding
- Series has-many Wave
- Scenario has-many Finding
- Scenario has-one WireMap
- Finding many-to-many DCR
- Series many-to-many Series

# Part 2: System Commitment

Persist state as structured Markdown files co-located with specs (CODEX.md, FINDINGS.md, INDEX.md, CLAUDE.md) so the plugin is zero-infra and human-readable without the tool. SeriesCode uniqueness enforced via CODEX.md parse on every register call. Scenario hand-compile gate enforced at create time -- expected-output field must be non-empty before status can advance past planned. Finding records are append-only Markdown blocks with a resolutions sub-array. DomainConfig drives scaffolding templates via a strategy pattern (one adapter per domain type: compiler, runtime, bridge, api, emitter). WireMap generation uses scenario expected-output as the assertion source; coverage gate check shells out to the project's test runner. Reports assemble live snapshots from on-disk files rather than a separate database. Five domain type adapters ship built-in: compiler (astro-style with 13-pass trace), runtime (craft-style with Zod schemas and coverage-first), bridge (flash-style with input/expected/actual directories), api (admin-style with inline scenarios and operation sequences), and emitter (flows-style with IR-to-output comparison).
