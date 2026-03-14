# User Intent: Simulate

## Original Goal (Natural Language)

I want a Claude Code plugin that helps me run design-time simulations on specs, designs, and architecture documents to find gaps before writing code. I've been doing this manually across 5 different projects -- hand-compiling expected outputs from specs, tracking findings, filing design change requests, and eventually wiring scenarios to real tests. It works incredibly well but the process is entirely manual and undocumented as a reusable methodology.

The plugin should codify the complete simulation lifecycle:

1. **Set up scenario runs** on designs in any directory structure -- not just one project, but across multiple design directories simultaneously (compiler specs, SDK APIs, provisioning bridges, flow emitters, etc.)
2. **Manage a codex** of 5-letter code names for scenario series, preventing collisions and tracking which codes map to which domains
3. **Scaffold scenario series** with the right directory structure, session drivers (CLAUDE.md), findings files, and validation checklists -- adapting to the domain's conventions
4. **Run simulations** by hand-compiling expected outputs from specs before automation -- the core "trace through the system manually" methodology
5. **Track findings** with severity, DCR linkage, and resolution status across hundreds of scenarios
6. **Batch findings into design change requests** (DCRs) when patterns emerge across scenarios
7. **Wire completed scenarios to real tests** after implementation -- bridge from design validation to code validation
8. **Report on coverage** -- which specs have scenario coverage, which don't, where gaps exist
9. **Support multiple simulation styles** -- directory-based (astro/flash/flows), inline (admin), numbered (flash), and wave-based complexity gradients

## Key Requirements

### Scenario Series Management
- Register and manage 5-letter series codes in a project-wide CODEX
- Scaffold new series with domain-appropriate directory structures
- Support multiple directory conventions: numbered prefixes (00+, 10+, 20+, 30+, 80+, 90+), named directories, and inline scenarios
- Generate CLAUDE.md session drivers with enforced vocabulary, pipeline model, progress tables
- Generate FINDINGS.md, INDEX.md, COMPLETION-CRITERIA.md per series
- Track series across multiple design directories (poly-directory)

### Scenario Lifecycle
- Create individual scenarios with intent, input fixtures, expected output, and validation checklists
- Support the hand-compile-first methodology: expected output is written BEFORE implementation
- Track scenario status: planned → in-progress → complete → validated → wired
- Wave-based complexity gradients (Wave 1 = happy path, Wave 2-3 = edge cases, Wave 4+ = adversarial)
- Cross-series references when scenarios touch multiple features

### Findings Engine
- Track findings with IDs (F-01, SIM-01.1, etc.), severity, and resolution status
- Link findings to scenarios that discovered them
- Link findings to DCRs when they reveal spec gaps
- Batch related findings into DCR proposals
- Checkbox-based resolution tracking: `### F-01: Description (SEVERITY) -- [ ] RESOLVED`
- Finding lifecycle: identified → DCR filed → spec amended → scenario updated → resolved

### Design Change Requests (DCRs)
- Maintain a DCR index with status tracking (Draft → Active → Integrated → Implemented → Closed)
- Group related findings into batched DCRs
- Track which specs each DCR affects
- Link DCRs to implementation phases

### Test Wiring
- After implementation, help bridge design scenarios to automated tests
- Generate test scaffolds from scenario expected outputs
- Map scenario variations to test cases (each variation = one `it()` block)
- Track which scenarios have been wired to tests vs. still design-only
- Support coverage gates (95% lines/statements/functions, 90% branches)

### Coverage & Reporting
- Spec coverage matrix: which specs have scenario coverage
- Series progress dashboards (scenarios complete vs. planned)
- Findings scorecard (total, resolved, open, by severity)
- Wave completion tracking
- Cross-series dependency maps
- DCR status rollup

### Multi-Domain Support
- Configure per-domain simulation conventions (directory structure, naming, finding format)
- Support at least 5 domain types out of the box:
  - **Compiler/IR** (astro-style): spec-driven, 13-pass trace, DCR lifecycle
  - **Runtime/Function** (craft-style): pure functions, defense-in-depth, Zod schemas, coverage-first
  - **Bridge/Sync** (flash-style): input/expected/actual directories, pipeline-organized, aspect checklists
  - **API/SDK** (admin-style): inline scenarios, operation sequences, pitfall mapping
  - **Emitter/Output** (flows-style): IR input → output comparison, format-specific validation

## Workflow/Process

### Starting a New Simulation Campaign
1. Initialize simulation in a project: `simulate setup` (creates CODEX, config, directory structure)
2. Register design directories: `simulate domain add ./design/astro --type compiler`
3. Create a new series: `simulate series new boost --domain astro --focus "composable compiler passes"`
4. Series is scaffolded with CLAUDE.md, FINDINGS.md, INDEX.md, templates

### Running Simulations
1. Create scenario: `simulate scenario new S01-smoke-test --series boost --wave 1`
2. Write intent (what behavior is being tested)
3. Hand-compile expected output from specs
4. Mark scenario in-progress, then complete when traces match
5. Record findings as they emerge
6. Batch findings into DCRs when patterns appear

### After Implementation
1. Wire scenarios to tests: `simulate wire boost --test-dir tests/`
2. Generate test scaffolds from expected outputs
3. Run tests against implementation
4. Track wired vs. design-only scenarios
5. Validate coverage gates

### Reporting
1. `simulate status` -- overall dashboard
2. `simulate coverage --domain astro` -- spec coverage matrix
3. `simulate findings --series boost` -- findings scorecard
4. `simulate report` -- full simulation report

## Constraints

- **NEVER skip the hand-compile step** -- expected output must exist before automation runs
- **NEVER modify spec files** -- simulation finds gaps, DCRs propose amendments, humans approve
- **NEVER auto-resolve findings** -- findings require human review and explicit resolution
- **NEVER collide series codes** -- CODEX enforces uniqueness across all domains
- **NEVER wire tests without validated scenarios** -- design validation must pass first
- **NEVER assume one directory structure** -- support poly-directory, poly-convention projects
- **NEVER lose finding history** -- findings are append-only with resolution annotations

## Inspiration

Based on:
- **Astro-Boost scenario methodology** -- 375+ scenarios across 53 series, 120 DCRs filed from findings
- **Panel plugin lifecycle** -- 8-stage progression with gates, re-entrant state machine, schema-validated state
- **Flash provisioning bridge** -- input/expected/actual directory pattern, pipeline-organized scenarios
- **Admin SDK validation** -- inline scenarios with operation sequences, pitfall mapping
- **Flows emitter validation** -- IR → output comparison, format-specific validation
- **TDD (Test-Driven Development)** -- write expected output before implementation, but applied to design
