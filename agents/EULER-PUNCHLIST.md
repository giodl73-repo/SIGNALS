# EULER Punchlist

Active work items, ordered by priority.

---

## IN PROGRESS

| # | Item | Status | Notes |
|---|------|--------|-------|
| 1 | `simulate-ode` quest loop | RUNNING | job `b29dcef5` dispatched 2026-03-20 |
| 2 | `validate-null` quest loop | RUNNING | job `3a1d6370` dispatched 2026-03-20 |

---

## QUEUED

| # | Item | Notes |
|---|------|-------|
| 3 | Promote `simulate-ode` golden to release | After quest loop converges |
| 4 | Promote `validate-null` golden to release | After quest loop converges |
| 5 | Run `release-update.sh --pr` to sync craftworks-research | After both goldens promoted |

---

## DONE

| # | Item | Date | Commit |
|---|------|------|--------|
| A | Read signal-builder.md + GH issues #1 and #2 | 2026-03-20 | — |
| B | Create EULER agent profile | 2026-03-20 | 8f3477c |
| C | Write `simulate-ode` v1 body (signals/ + release/) | 2026-03-20 | 8f3477c |
| D | Write `validate-null` v1 body (signals/ + release/) | 2026-03-20 | 8f3477c |
| E | Comment on issues #1 and #2 with status | 2026-03-20 | — |
| F | Push to simlab | 2026-03-20 | 8f3477c |

---

## RELAY DISPATCH COMMANDS

When relay is back up:

```bash
# Check relay
curl -s http://localhost:8716/list

# Dispatch from repo root (relay cwd must be set to the signals repo root)
curl -s -X POST http://localhost:8716/run \
  -H "Content-Type: application/json" \
  -d '{"script":"tools/quest-run-one.sh","args":["simulate-ode"],"cwd":"<repo-root>"}'

# Tail output
curl -s "http://localhost:8716/tail/<job_id>?lines=20"
```

Note: quest-run-one.sh now uses `$(pwd)` -- no hardcoded paths. Pass the repo root as cwd.
