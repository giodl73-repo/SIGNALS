# simulate / domain

Domain tier.

## Skills

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

## Roles

- domain-expert (experiential)

## Artifact Directories

| Directory | Role | Type | Format |
|-----------|------|------|--------|
| traces | domain-expert | trace-document | markdown |
