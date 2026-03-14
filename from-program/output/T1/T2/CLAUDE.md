# simulate / T2

T2 tier.

## Skills

- /series -- Scenario series lifecycle -- create series with domain-appropriate scaffolding, manage scenarios within series, track findings, file DCRs, and manage wave-based complexity gradients. Operations: new, show, list, scenario (new/trace/validate/status), finding (new/resolve/batch/list), dcr (new/update/list), complete.

- /wire -- Test bridge -- generate test scaffolds from validated design scenarios, track wiring status, run coverage gates, and validate that design scenarios are backed by real tests. Operations: scaffold, status, validate, map, coverage.

- /series-scaffolder -- Create domain-appropriate directory structure for a new series. Generates CLAUDE.md session driver, FINDINGS.md, INDEX.md, COMPLETION-CRITERIA.md, and scenario templates based on domain type.

- /scenario-scaffolder -- Create individual scenario directories with intent, input fixtures, expected output placeholders, and validation checklists.

- /session-driver-generator -- Generate CLAUDE.md session drivers with enforced vocabulary table, pipeline model, progress table, current scenario pointer, and startup protocol. Adapts to domain conventions.

- /test-scaffolder -- Generate test file scaffolds from scenario expected outputs. Maps scenario variations to it() blocks, creates describe() structure matching series/wave hierarchy.

- /run -- Campaign orchestration -- setup projects, register domains, manage simulation campaigns, and run interactive simulation sessions. Operations: setup, domain (add/list/remove), session (new/resume/show), status, config.
 *(inherited from T1)*
- /codex -- Series code registry -- register, reserve, list, check, and manage 5-letter scenario series codes across all domains. Enforces uniqueness and tracks code-to-domain mappings. Operations: register, reserve, list, check, show, align.
 *(inherited from T1)*
- /report -- Simulation reporting -- dashboards, coverage matrices, findings scorecards, DCR rollups, and comprehensive simulation reports. Operations: status, coverage, findings, dcrs, full, export.
 *(inherited from T1)*
- /domain-scanner -- Discover and index simulation artifacts in a registered domain *(inherited from T1)*
- /codex-scanner -- Scan all domains for series codes and validate CODEX consistency *(inherited from T1)*
- /coverage-scanner -- Scan spec corpus and map scenario coverage per spec *(inherited from T1)*
- /finding-analyzer -- Analyze findings across series for patterns -- recurring themes, spec gaps, severity distributions. Proposes DCR batches.
 *(inherited from T1)*
- /coverage-analyzer -- Calculate spec coverage matrices, identify uncovered specs, and compute coverage percentages per domain.
 *(inherited from T1)*
- /gap-analyzer -- Identify gaps in simulation coverage -- specs without scenarios, series without adversarial waves, findings without DCRs.
 *(inherited from T1)*
- /scenario-tracker -- Track scenario lifecycle state transitions (planned → wired) *(inherited from T1)*
- /finding-tracker -- Track finding lifecycle (identified → resolved) with audit trail *(inherited from T1)*
- /dcr-tracker -- Track DCR lifecycle (Draft → Closed) with spec linkage *(inherited from T1)*
- /wire-tracker -- Track test wiring status and coverage gate results *(inherited from T1)*
