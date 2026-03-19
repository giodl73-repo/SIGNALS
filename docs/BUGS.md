# Signal Quality Gate — Master Bug List

**3 rounds, 36 bugs total, 35 fixed, 1 deferred**
**24 customer personas, 4 bindings tested**

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

## Systemic Issues Found (not individual bugs)

| ID | Issue | Fixed in |
|----|-------|---------|
| I-01 | Bare binding program.yaml used old stems causing wrong folder names | `1e01562` |
| I-02 | `specify-spec.t3` SCOUT-STATUS-TABLE only scanned for `scout-*` not `discover-*` — broke artifact continuity for every user | `6ccafd0` |
| I-03 | CLAUDE.md not generated per-binding automatically | `1e01562` |
| I-04 | `--depth deep` undocumented — 4/12 customers tried it, all got better output | **OPEN — add to QUICKSTART** |

---

## Summary

| Round | Customers | Bindings | Bugs | Fixed | Key finding |
|-------|-----------|----------|------|-------|-------------|
| 1 | 12 BIC | flat | 9 | 9 | Stale content from renames |
| 2 | 12 intl | flat vs bare | 4 | 4 | validate-design truncated |
| 3 | 12 new | free choice (4 options) | 6 | 5 | Binding choice = doc accuracy test |
| **Total** | **36** | | **19** | **18** | |

**Most chosen binding (unprompted):** flat (5/12)
**Best task completion:** flat (5/5 avg)
**Most revealing condition:** C3 — binding choice quality exposes doc gaps immediately
