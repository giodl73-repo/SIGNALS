# Discipline-Driven Peer Review Simulation

Multi-disciplinary code review from standardized lenses. Same artifact reviewed by 6 disciplines independently.

## What It Simulates

A review board — AI acts as architect, code quality reviewer, documentation reviewer, tester, PM, implementer.

## Scale

6 standard disciplines applied to every design area.

## Evidence Files

### Discipline System

| File | Purpose |
|------|---------|
| `C:\src\craftworks\plugins\craft\shared\make\discipline-operations.md` | CRUD operations for disciplines (new, show, list, edit, remove, assign, audit, brief) |
| `C:\src\craftworks\plugins\craft\shared\make\discipline-resolver.md` | 5-tier resolution chain — exact match, domain-prefix fallback, specialization fallback, interactive generation |
| `C:\src\craftworks\plugins\craft\templates\help\disciplines.md` | Discipline help documentation |

### Review Output

| Path | Content |
|------|---------|
| `C:\src\craftworks\.roles\reviews\concepts\` | Review output directories |
| `C:\src\craftworks\design\flash\reviews\` | Flash discipline reviews (R-B1 through R-B8) |
| `C:\src\craftworks\design\agent\reviews\founding\` | Agent founding review rounds (1-5) |

### Standard Disciplines

| Discipline | Focus |
|------------|-------|
| Architecture | System structure, layering, dependencies |
| Code Quality | Conventions, patterns, maintainability |
| Documentation | Accuracy, completeness, audience |
| Testing | Coverage, edge cases, validation |
| Process/PM | Workflow, gates, progress tracking |
| Implementation | Correctness, performance, security |

## Finding Format

```markdown
### F-01: Description (SEVERITY) — [ ] RESOLVED
### F-02: Description (SEVERITY) — [x] RESOLVED (one-line fix)
```

Cross-discipline synthesis identifies systemic patterns — issues raised by multiple disciplines are elevated.
