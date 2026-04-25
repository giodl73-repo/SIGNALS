# State-Operation-Outcome Simulation

Trace API operations through SDK/registry/storage layers, validate state transitions against the spec corpus.

## What It Simulates

The SDK runtime — the designer acts as the SDK, tracing CLI operations through layers and verifying expected state transitions.

## Scale

199 scenarios across 6 series (admin, agent, craft, seals, suite, vault). 101+ findings.

## Evidence Files

### Methodology (inline — scenarios live inside SIMULATION.md)

| File | Scenarios | Waves | Focus |
|------|-----------|-------|-------|
| `craftworks\design\admin\scenarios\admin\SIMULATION.md` | 47 | 9 | Core artifact lifecycle, SDK operations |
| `craftworks\design\admin\scenarios\agent\SIMULATION.md` | 32 | 8 | Agent contract validation (AD-08) |
| `craftworks\design\admin\scenarios\craft\SIMULATION.md` | 42 | 7 | Craft-layer operations |
| `craftworks\design\admin\scenarios\seals\SIMULATION.md` | 28 | 6 | Seals (complete, 101 findings) |
| `craftworks\design\admin\scenarios\suite\SIMULATION.md` | 24 | 6 | Cross-layer scenarios (active) |
| `craftworks\design\admin\scenarios\vault\SIMULATION.md` | 26 | 5 | Vault operations |

### Governing Specs

| File | Content |
|------|---------|
| `craftworks\design\admin\specs\sdk.md` | AD-01: SDK & Config File Schema |
| `craftworks\design\admin\specs\operations.md` | AD-02: Operations (17 Uniform Ops) |
| `craftworks\design\admin\specs\storage.md` | AD-03: Storage Layout & Type Details |
| `craftworks\design\admin\specs\workspaces.md` | AD-04: Workspaces & Runtime Environments |
| `craftworks\design\admin\specs\solutions.md` | AD-05: Solutions, Packaging & Deployment |
| `craftworks\design\admin\specs\versioning.md` | AD-06: Versioning & History |
| `craftworks\design\admin\specs\integrity.md` | AD-07: Integrity, Registry & Error Handling |

### Pitfall Catalogs (45 pitfalls scenarios guard against)

| File | Domain | Count |
|------|--------|-------|
| `craftworks\design\admin\pitfalls\pitfalls-solutions.md` | Solutions (SP-01..SP-13) | 13 |
| `craftworks\design\admin\pitfalls\pitfalls-versioning.md` | Versioning (VP-01..VP-06) | 6 |
| `craftworks\design\admin\pitfalls\pitfalls-environments.md` | Environments (EP-01..EP-13) | 13 |
| `craftworks\design\admin\pitfalls\pitfalls-alm.md` | ALM (AP-01..AP-13) | 13 |

## Pattern

```
Starting state (empty .roles/ workspace)
  → Operation sequence (1. API call → expected result, 2. ...)
    → Expected outcome (assertions on registry, storage, hashes)
```
