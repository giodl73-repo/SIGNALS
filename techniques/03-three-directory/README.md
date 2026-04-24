# Three-Directory Simulation (Hand-Derived Expected Output)

Hand-compile expected output files FIRST, then run script, then diff. The `10+input → 20+expected → 30+actual` pattern.

## What It Simulates

Python provisioning scripts — the designer acts as the script, manually deriving expected output before running.

## Scale

24 scenarios (15 complete), organized by pipeline (schema, data, diff, pull).

## Evidence Files

### Methodology

| File | Purpose |
|------|---------|
| `C:\src\craftworks\design\flash\scenarios\SIMULATION.md` | Flash simulation guide — 3-directory structure, vocabulary, Two-System Trap |
| `C:\src\craftworks\design\flash\scenarios\CLAUDE.md` | Session driver — pipeline model, progress table, aspect checklist triggers |

### Scenario Directories

| Path | Pipeline | Scenarios |
|------|----------|-----------|
| `C:\src\craftworks\design\flash\scenarios\01+smoke-test-schema\` | Schema | S01 |
| `C:\src\craftworks\design\flash\scenarios\02+all-field-types\` | Schema | S02 |
| `C:\src\craftworks\design\flash\scenarios\03+picklist-offset\` | Schema | S03 |
| `C:\src\craftworks\design\flash\scenarios\06+smoke-test-data\` | Data | S06 |
| `C:\src\craftworks\design\flash\scenarios\10+diff-clean\` | Diff | S10 |
| `C:\src\craftworks\design\flash\scenarios\14+pull-scalar-fields\` | Pull | S14 |

Each scenario directory contains:
- `10+input/` — fixtures (entity.yaml, source files)
- `20+expected/` — hand-derived expected output
- `30+actual/` — actual script output (populated by running)
- `SCENARIO.md` — hypotheses + findings

### Scripts Under Test

| File | Pipeline | Direction |
|------|----------|-----------|
| `C:\src\craftworks\research\frost\scripts\generate_solution.py` | Schema | M→A |
| `C:\src\craftworks\research\frost\scripts\load_data.py` | Data | M→A |
| `C:\src\craftworks\research\frost\scripts\diff_data.py` | Diff | M↔A |
| `C:\src\craftworks\research\frost\scripts\pull_data.py` | Pull | A→M |

### Bug History

| File | Purpose |
|------|---------|
| `C:\src\craftworks\research\frost\POSTMORTEM.md` | All known bugs from scenario findings |

### Aspect Specs (source of truth)

| File | Aspect |
|------|--------|
| `C:\src\craftworks\design\flash\aspects\corpus-config.md` | ASP-01 |
| `C:\src\craftworks\design\flash\aspects\local-representation.md` | ASP-02 |
| `C:\src\craftworks\design\flash\aspects\local-contract.md` | ASP-03 |
| `C:\src\craftworks\design\flash\aspects\remote-contract.md` | ASP-04 |
| `C:\src\craftworks\design\flash\aspects\field-mapping.md` | ASP-05 |
| `C:\src\craftworks\design\flash\aspects\diffgram.md` | ASP-06 |
| `C:\src\craftworks\design\flash\aspects\form-fallback.md` | ASP-07 |

## Pattern

```
Hand-compile 20+expected/
  → run script, populate 30+actual/
    → compare
      → mismatch? Is the script wrong or is expected wrong?
        → fix → re-run → verify
```
