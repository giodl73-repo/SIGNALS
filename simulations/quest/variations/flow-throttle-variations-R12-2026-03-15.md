Written to `simulations/quest/golden/flow-throttle-variate-R12-2026-03-16.md`.

---

## flow-throttle — Round 12 Variations

**Rubric:** v12 | **Max composite:** 220 | **New criteria:** C-33 + C-34

### State at entry

R11 V-05 scores **210/220** under v12. Two gaps:

| Gap | Location | Failure |
|-----|----------|---------|
| C-33 | Section B annotation header | Names criteria (C-29, C-30) but not field count or field names — auditor must read body and criterion-match, cannot count-scan |
| C-34 | TYPE SCAN GATE audit paths | Observable count embedded in description prose ("confirm five named observables in sequence") — not at the path-label level |

---

### Variation Map

| Variation | Axis | C-33 | C-34 | Predicted |
|-----------|------|------|------|-----------|
| **V-01** | Inertia framing: baseline isolation (R11 V-04 carry, no count header) | FAIL | FAIL | 210/220 |
| **V-02** | Inertia framing: C-33 PASS (field-count header added, no observable count) | PASS | FAIL | 215/220 |
| **V-03** | Lifecycle emphasis: C-34 PASS (per-path count at label level, no field-count header) | FAIL | PASS | 215/220 |
| **V-04** | Combined: C-33 + C-34, single-role form | PASS | PASS | 220/220 |
| **V-05** | Role sequence + all axes: three-role pipeline with C-33 + C-34 | PASS | PASS | 220/220 |

---

### The two structural changes

**C-33** — annotation header transform (V-02, V-04, V-05):
```
BEFORE: **Inertia annotation for C-27 — why the register must be declared closed (C-29, C-30):**
AFTER:  **Inertia annotation for C-27 — why the register must be declared closed — 3 fields: Failure mode prevented | Gap above C-25 | Concrete example (C-29, C-30):**
```

**C-34** — audit path label transform (V-03, V-04, V-05):
```
BEFORE: *Gate-present audit method:* ... confirm five named observables in sequence:
AFTER:  *Gate-present audit method — 5 observables:* ... Confirm the following 5 observables in sequence:

BEFORE: *Gate-absent signature:* ... Named observable for the absent condition:
AFTER:  *Gate-absent signature — 1 observable:* ... Confirm the following 1 observable:
```

V-05 places both changes at role boundaries — the field-count header is a Format Analyst deliverable (locked before Role 2 opens), and the count-declared audit paths are the Consequence Analyst's TYPE SCAN GATE entry condition.
