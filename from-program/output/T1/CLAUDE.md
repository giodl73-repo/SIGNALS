# simulate / T1

Root tier. Workspace-wide skills visible to all tiers.

## Skills

- /run -- Campaign orchestration -- setup projects, register domains, manage simulation campaigns, and run interactive simulation sessions. Operations: setup, domain (add/list/remove), session (new/resume/show), status, config.

- /codex -- Series code registry -- register, reserve, list, check, and manage 5-letter scenario series codes across all domains. Enforces uniqueness and tracks code-to-domain mappings. Operations: register, reserve, list, check, show, align.

- /report -- Simulation reporting -- dashboards, coverage matrices, findings scorecards, DCR rollups, and comprehensive simulation reports. Operations: status, coverage, findings, dcrs, full, export.

- /domain-scanner -- Discover and index simulation artifacts in a registered domain
- /codex-scanner -- Scan all domains for series codes and validate CODEX consistency
- /coverage-scanner -- Scan spec corpus and map scenario coverage per spec
- /finding-analyzer -- Analyze findings across series for patterns -- recurring themes, spec gaps, severity distributions. Proposes DCR batches.

- /coverage-analyzer -- Calculate spec coverage matrices, identify uncovered specs, and compute coverage percentages per domain.

- /gap-analyzer -- Identify gaps in simulation coverage -- specs without scenarios, series without adversarial waves, findings without DCRs.

- /scenario-tracker -- Track scenario lifecycle state transitions (planned → wired)
- /finding-tracker -- Track finding lifecycle (identified → resolved) with audit trail
- /dcr-tracker -- Track DCR lifecycle (Draft → Closed) with spec linkage
- /wire-tracker -- Track test wiring status and coverage gate results
