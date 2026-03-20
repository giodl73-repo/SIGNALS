# EULER Punchlist

Active work items, ordered by priority.

---

## IN PROGRESS

| # | Item | Status | Notes |
|---|------|--------|-------|
| 1 | Dispatch `simulate-ode` to quest loop | BLOCKED | Relay is down |
| 2 | Dispatch `validate-null` to quest loop | BLOCKED | Relay is down |

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
curl -s http://localhost:8716/list | python -m json.tool

# Dispatch both (max 2 parallel -- these are the only active jobs)
curl -s -X POST http://localhost:8716/run \
  -H "Content-Type: application/json" \
  -d '{"script":"tools/quest-run-one.sh","args":["simulate-ode"],"cwd":"C:/src/sim"}'

curl -s -X POST http://localhost:8716/run \
  -H "Content-Type: application/json" \
  -d '{"script":"tools/quest-run-one.sh","args":["validate-null"],"cwd":"C:/src/sim"}'
```
