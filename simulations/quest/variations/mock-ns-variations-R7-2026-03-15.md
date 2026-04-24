Written to `simulations/quest/golden/mock-ns-variate-R7-2026-03-15.md`.

---

## mock-ns -- Round 7 Variations (summary)

Rubric: v7 (C-01 through C-24, denominator 16). New criteria: **C-23** (failure-consequence at compute site) and **C-24** (no-instruction-exempt affirmative at consumption site).

| Variant | Axis | New criteria | Expected |
|---------|------|-------------|---------|
| **V-01** | Inertia framing | C-23 only | ~99.4 |
| **V-02** | Phrasing register | C-24 only | ~99.4 |
| **V-03** | Lifecycle emphasis | none (R6 baseline) | ~98.8 |
| **V-04** | Output format + role sequence | C-23 minimal + C-24 full | 100 |
| **V-05** | Full convergence (prose) | C-23 + C-24 | 100 |

**Structural logic of the five axes:**

- **V-01** tests C-23 as standalone: S-3 gets the full contamination-mechanism sentence ("A-1 will inherit a corrupted value that cannot be distinguished from a correctly-computed one") while A-1 keeps R6 V-01's catch-all but no positive-coverage affirmative (no C-24).

- **V-02** tests C-24 as standalone: S-3 keeps R6 V-02's C-21 affirmative closure without a consequence statement (no C-23), while A-1 adds "Every instruction in this step -- named or unnamed -- is governed by this rule. No instruction in this step is exempt." immediately after the catch-all.

- **V-03** is the regression baseline: exact R6 V-05 structure, confirming neither C-23 nor C-24 is needed for that score band. Establishes the floor against which V-01 and V-02 gains are measured.

- **V-04** combines C-23 (minimal, single sentence) + C-24 (full two-component form) with table-structured flag-case decision at S-3. Tests whether C-23 minimal form is rubric-sufficient.

- **V-05** is full convergence: C-23 with explicit contamination-mechanism + downstream-effect naming, C-24 with both components, all prior layers intact. Only variant predicted to score 100 with certainty.

**Key discriminant**: V-04 vs V-05 isolates whether C-23 requires extended elaboration or if a single-sentence consequence statement passes the criterion.
