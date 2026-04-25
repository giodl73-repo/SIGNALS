# Hand-Compilation Simulation

Manually trace input through compiler passes, derive expected output, compare to actual. Design validation, not runtime tests.

## What It Simulates

The compiler — specs, passes, IR structures, cross-cutting concerns. The designer acts as the compiler, tracing each pass manually.

## Scale

- **Astro**: 375+ scenarios across 53 series, 120 DCRs
- **Craft**: 315+ scenarios across 31+ series, 356 findings
- **Flows**: 42 scenarios (all complete), 78 findings (all resolved)

## Evidence Files

### Methodology

| File | Purpose |
|------|---------|
| `craftworks\design\astro\scenarios\SIMULATION.md` | Astro simulation guide — wave structure, finding lifecycle, hand-compile rules |
| `craftworks\design\agent\scenarios\SIMULATION.md` | Craft simulation guide — pure functions, diagnostic arrays, coverage gates |
| `craftworks\design\flows\SCENARIOS.md` | Flows scenario master index — IR-to-output validation |

### Session Drivers (per-series)

| File | Purpose |
|------|---------|
| `craftworks\design\astro\scenarios\<series>\CLAUDE.md` | Per-series session driver — vocabulary, pipeline, progress, bugs |
| `craftworks\design\agent\scenarios\<series>\CLAUDE.md` | Craft series session drivers |
| `craftworks\design\flash\scenarios\CLAUDE.md` | Flash scenario session driver |

### Findings & Design Changes

| File | Purpose |
|------|---------|
| `craftworks\design\astro\DCR.md` | 120 design change records from scenario findings |
| `craftworks\design\astro\scenarios\<series>\FINDINGS.md` | Per-series findings (F-NN format) |
| `craftworks\design\agent\scenarios\FINDINGS.md` | Craft aggregate findings (356 across 7 themes) |

### Scenario Directories

| Path | Content |
|------|---------|
| `craftworks\design\astro\scenarios\` | 53 series directories |
| `craftworks\design\agent\scenarios\` | 31+ series directories |
| `craftworks\design\flows\scenarios\` | 7 series (cloud, cua, bind, trigger, pad, expr, pack) |

### Tests (scenario → test mapping)

| Path | Content |
|------|---------|
| `craftworks\craft-cli\tests\astro\scenarios\` | Astro simulation tests |
| `craftworks\craft-cli\tests\craft-scenarios\` | Craft simulation tests |

## Pattern

```
Read spec → trace passes with test input → write expected output
  → compare actual vs expected → file finding (F-NN)
    → DCR → spec amendment → scenario update
```

## Key Rules

1. Read the spec, not just the scenario
2. Scenarios produce findings, findings produce DCRs
3. Wave structure: W1 happy path → W2-3 edge cases → W4+ adversarial
4. Hand-compile before automating
5. 95% coverage lines/statements/functions, 90% branches per-file
