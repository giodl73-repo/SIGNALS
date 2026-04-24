Written to `simulations/quest/rubrics/topic-status-rubric-v17-variate-R19-2026-03-15.md`.

---

## Round 19 Variations: `topic:status`

**Rubric:** v17 (max 300) | **Gap closed:** C-47 + C-49 cross-axis combination

### Design

The R18 gap: three variants tied at 295 (each isolating C-47, C-48, or C-49 alone), but no variant simultaneously failed C-47 and C-49. True three-way simultaneous failure is structurally impossible because C-48 FAIL → C-49 vacuous PASS. The achievable maximum-failure configuration is C-47 FAIL + C-48 PASS + C-49 FAIL. That's V-05.

### Ablation matrix

| Variant | C-47 | C-48 | C-49 | Predicted |
|---------|------|------|------|-----------|
| V-01 | PASS | PASS | PASS | **300** |
| V-02 | FAIL | PASS | PASS | **295** |
| V-03 | PASS | FAIL | PASS* | **295** |
| V-04 | PASS | PASS | FAIL | **295** |
| V-05 | FAIL | PASS | FAIL | **290** |

\*Vacuous PASS: 4th predicate present, no PHASE 1 adversary declared.

### Variation axes

| Variant | Axis | What changes |
|---------|------|--------------|
| V-01 | Min delta baseline | Nothing — full-stack reference |
| V-02 | Inertia framing | ADVERSARY CHAIN block: labeled sub-entries → running prose |
| V-03 | Lifecycle emphasis | PHASE 1 body compressed: ADVERSARY/DEFEAT CONDITION block removed; preamble shrinks to 2-label chain |
| V-04 | Role sequence | DISPLAY GATE STOP CONDITION: 4 predicates → 3 (PHASE 1 defeat gate removed) |
| V-05 | Combination (V-02 + V-04) | Prose ADVERSARY CHAIN AND truncated STOP CONDITION simultaneously |

### Key structural element (new in R18/R19)

The PHASE 4 DISPLAY GATE now carries an explicit **STOP CONDITION** block:

```
PHASE 4 -- DISPLAY GATE
  STOP CONDITION:
    (1) COMMIT RISK REGISTER has one row per planned signal
    (2) PHASE 2 adversary defeated: all planned signals individually asserted
    (3) PHASE 3 adversary defeated: consistency guard applied before verdict
    (4) PHASE 1 adversary defeated: DISK_SIGNALS from live glob; zero-result handled  ← C-49
```

V-04 and V-05 omit predicate (4). V-03 carries it vacuously (predicate present, adversary absent).

### Orthogonality confirmation via V-05

- V-05 vs V-02 delta = **5 pts** → C-49 independently necessary within a C-47-failing variant
- V-05 vs V-04 delta = **5 pts** → C-47 independently necessary within a C-49-failing variant
