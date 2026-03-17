Written to `simulations/quest/golden/signal-setup-variate-R19-2026-03-17.md`.

---

## signal-setup Variations — Round 19 (v17 rubric)

**Rubric**: v17 | **Denominator**: 42 | **Formula**: `(essential/5 * 60) + (recommended/3 * 30) + (aspirational/42 * 10)`

---

### Context

R18 produced V-04 (letter-slot) and V-05 (word-suffix) as golden candidates that pass all v16 criteria. The v17 rubric adds C-41 (depth-2 recursive lineage encoding) and C-42 (word-suffix abbreviation uniqueness). Analysis confirms both R18 golden candidates already satisfy C-41 and C-42 — V-04 passes C-42 vacuously (no abbreviation step in letter-slot), V-05 passes C-42 non-vacuously (single branch with depth-2 children, no collision possible).

R19 focuses on establishing the **failure modes** through negative controls and stress-testing the criteria with a richer two-integration tree.

---

### Variations

| Variation | Primary Axis | C-41 | C-42 | C-31 | All Others |
|-----------|-------------|------|------|------|------------|
| **V-01** | C-41 failure — children of `GATE 6A` named `GATE 6-Found`/`GATE 6-Write`, dropping the `A` branch slot | FAIL | vacuous | FAIL | PASS (R18 V-04 base) |
| **V-02** | C-42 failure — word-suffix, two integrations (`6-Copilot` + `6-Code`), both abbreviate to `6C-` | structural PASS | FAIL | PASS | PASS |
| **V-03** | C-42 pass — same two-integration tree as V-02, distinct abbreviations `6Cop-` / `6VS-` | PASS | PASS | PASS | PASS |
| **V-04** | R18 V-04 verbatim confirmed under v17 — letter-slot golden candidate | PASS | vacuous | PASS | PASS |
| **V-05** | R18 V-05 verbatim confirmed under v17 — word-suffix golden candidate | PASS | PASS | PASS | PASS |

**V-04 and V-05** are the primary golden candidates — no text changes from R18, explicit v17 compliance annotated in headers.

**V-03** is a forward-look: previews what a multi-integration spec looks like when C-42 discipline is applied. If Signal extends to VS Code in a future version, `6Cop-`/`6VS-` is the template.
