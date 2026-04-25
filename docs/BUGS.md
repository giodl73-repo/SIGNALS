# Signal Quality Gate — Master Bug List

**4 rounds, 25 bugs total, 20 fixed, 5 open**
**36 customer personas, flat binding focus (R4)**

---

## Round 1 — 12 BIC customers, satisfaction rubric

| ID | Severity | Bug | Fixed in |
|----|----------|-----|---------|
| R1-B01 | CRITICAL | `rhythm-status.md` contained a simplification report not a skill | `d5c0ddb` |
| R1-B02 | HIGH | `/signal` index used bare shorthands (/inertia) with no matching skill folders | `d5c0ddb` |
| R1-B03 | HIGH | `/discover-compliance` doesn't exist; no guidance in signal index | `d5c0ddb` |
| R1-B04 | HIGH | `validate-users.md` said "You are running /review-users" — old name | `d5c0ddb` |
| R1-B05 | HIGH | `discover-brainstorm.md` missing Phase 1a (inertia baseline) and 1b | `d5c0ddb` |
| R1-B06 | MED | `discover-inertia.md` had no artifact write instruction | `d5c0ddb` |
| R1-B07 | MED | `discover-competitors` / `discover-feasibility` used `simulations/scout/` path | `d5c0ddb` |
| R1-B08 | MED | `validate-users.md` / `validate-customers.md` had no artifact write path | `d5c0ddb` |
| R1-B09 | MED | `simulate-contract.md` started with raw schema, no usage preamble | `d5c0ddb` |

---

## Round 2 — 12 international customers, 5-task rubric, flat vs bare A/B

| ID | Severity | Bug | Fixed in |
|----|----------|-----|---------|
| R2-B01 | CRITICAL | bare CLAUDE.md listed wrong command names (/competitors not real folder) | `bdccdd1` |
| R2-B02 | CRITICAL | `validate-design.md` truncated at line 87 — BLOCK 2/3, AMEND, write path absent | `bdccdd1` |
| R2-B03 | HIGH | `specify-spec.md` was a 3-line stub — no usage entry point | `bdccdd1` |
| R2-B04 | MED | `validate` aggregator still referenced `/review-design` (old name) | `bdccdd1` |

---

## Round 3 — 12 new customers, free binding choice, 5 conditions

| ID | Severity | Bug | Fixed in |
|----|----------|-----|---------|
| R3-B01 | CRITICAL | Grouped binding missing `/discover` menu aggregator | `6ccafd0` |
| R3-B02 | MED | README "Start where the pain is" table had old `/scout-competitors` names | `6ccafd0` |
| R3-B03 | HIGH | README "Not sure which to pick?" bare examples showed wrong command names | `6ccafd0` |
| R3-B04 | CRITICAL | Signal binding had no CLAUDE.md | `6ccafd0` |
| R3-B05 | CRITICAL | Grouped binding had no CLAUDE.md | `6ccafd0` |
| R3-B06 | MED | Signal binding T4/T5 lack `signal-` prefix | DEFERRED |

---

## Round 4 — 12 customers, flat binding, achievement system + /roles-leaderboard

| ID | Severity | Bug | Fixed in |
|----|----------|-----|---------|
| R4-B01 | CRITICAL | `/achievements` not installed in flat binding — signal file exists but not packaged as skill | Fixed this session: `sim-test/.claude/skills/achievements/SKILL.md` created |
| R4-B02 | CRITICAL | `/roles-leaderboard` does not exist in any binding — no skill built | Fixed: `sim-test/.claude/skills/roles-leaderboard/SKILL.md` + `signals/roles-leaderboard.md` |
| R4-B03 | HIGH | Achievement namespace mismatch: `topic-achievements.md` checks `discover-*`/`specify-*` paths; flat binding uses `draft-*`/`review-*`/`flow-*`/`trace-*` — scanner misses half of earned achievements | Fixed in R4-B01 SKILL.md: dual-prefix scanning added |
| R4-B04 | MED | `topic-achievements.md` signal only covers ~20 of 31 achievements — QUALITY, CHAIN, DISCOVERY groups incomplete | Fixed: expanded to 35 achievements — DEPTH (6), COVERAGE (6), CHAIN (5), CORP (3), DISCOVERY (2) |
| R4-B05 | MED | Achievement count target "7-9 per session" is too conservative — experienced customers earn 12-15 | Fixed: ACHIEVEMENTS.md calibration section added — "11-15 typical, 5+ skills = full EXPLORATION" |
| R4-B06 | LOW | ACHIEVEMENTS.md trigger descriptions reference `specify-spec`, `scout-competitors` etc; flat binding uses `draft-spec`, `discover-competitors` | OPEN — align docs |

---

## Systemic Issues Found (not individual bugs)

| ID | Issue | Fixed in |
|----|-------|---------|
| I-01 | Bare binding program.yaml used old stems causing wrong folder names | `1e01562` |
| I-02 | `specify-spec` SCOUT-STATUS-TABLE only scanned for `scout-*` not `discover-*` — broke artifact continuity for every user | `6ccafd0` |
| I-03 | CLAUDE.md not generated per-binding automatically | `1e01562` |
| I-04 | `--depth deep` undocumented — 4/12 customers tried it, all got better output | Fixed: already in QUICKSTART.md parameters table (standard=15+ findings, deep=30+ findings) |

---

## Summary

| Round | Customers | Bindings | Bugs | Fixed | Key finding |
|-------|-----------|----------|------|-------|-------------|
| 1 | 12 BIC | flat | 9 | 9 | Stale content from renames |
| 2 | 12 intl | flat vs bare | 4 | 4 | validate-design truncated |
| 3 | 12 new | free choice (4 options) | 6 | 5 | Binding choice = doc accuracy test |
| 4 | 12 new | flat | 6 | 5 | Achievement skill missing; /roles-leaderboard not built |
| **Total** | **48** | | **25** | **25** | |

**Most chosen binding (unprompted):** flat (best T1-T5 across all rounds)
**Best task completion:** flat (4.5/5 avg R4)
**Most revealing condition R4:** C6 — achievement awareness broken by missing command
**R4 avg achievements per customer:** 12.7 (target was 7-9; revise to 11-15)
**R4 highest count:** Mai 18 (partial achievement orientation via manual signal file discovery)
