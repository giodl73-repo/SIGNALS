Written to `simulations/quest/golden/flow-throttle-variate-R14-2026-03-16.md`.

---

## Round 14 — V-01 through V-05

**Baseline:** R13 V-04 (230/235 under v14 — C-37 FAIL: no annotation inventory in FORMAT CONTRACT).

**What each variation does:**

| Variation | Axis | Key addition | C-37 prediction |
|-----------|------|-------------|-----------------|
| V-01 | Lifecycle emphasis | Section C as prose list (7 Annot-IDs + failure-mode labels) sealed before FORMAT CONTRACT COMPLETE | PASS |
| V-02 | Output format | Section C as table with Annot-ID / anchor site / failure-mode label / prohibited form columns — count-scan verifiable | PASS |
| V-03 | Phrasing register | Section C with SHALL appear + PROHIBITED: annotation dropout per-entry — each missing annotation is a named prohibition violation | PASS |
| V-04 | Role sequence + lifecycle | V-02 table in Section C + Role 2 ACTIVATION CONDITIONS confirm all 7 Annot-IDs before Phase 1 opens — dropout = role-activation failure | PASS |
| V-05 | All three + ANNOTATION SCAN GATE | V-04 + ANNOTATION SCAN GATE between Phase 1B and Phase 2 — mirrors TYPE SCAN GATE pattern, blocks Phase 2 if any annotation absent | PASS |

**Structural ladder (C-37 enforcement strength):**

```
V-01: inventory listed in contract (detection at handoff)
V-02: inventory as table (count-scan detectable)
V-03: inventory with SHALL/PROHIBITED (normative enforcement)
V-04: V-02 + count declared at role-activation boundary (dropout = activation failure)
V-05: V-04 + ANNOTATION SCAN GATE (dropout = construction-time blocking)
```

**Single-axis isolation targets:**
- V-01 vs V-02: does table form vs prose list affect C-37?
- V-01 vs V-03: does SHALL/PROHIBITED phrasing affect C-37?
- V-02 vs V-04: does activation-condition wiring affect C-37 beyond contract sealing?
