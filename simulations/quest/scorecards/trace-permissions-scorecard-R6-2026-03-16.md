## Round 6 Scorecard — trace-permissions (Rubric v12, N=28)

---

### Scoring Framework

Base: V-05/R12 = 25/28 = **98.9**. Three open criteria: C-34, C-35, C-36. Each aspirational = **0.36 pts**. A passing criterion closes 0.36 pts of deficit.

---

### Per-Variation Evidence Review

#### Inherited Pass (all 5 variations) — C-01 through C-33 (25 criteria)

All five variations share the V-05/R12 base architecture intact. No regression detected on any previously-passing criterion.

| Range | Verdict | Evidence |
|-------|---------|---------|
| C-01..C-05 (Essential) | PASS all | TABLE_1–5 schemas present with Tier columns, blank-cell prohibition, role-operation matrix, FLS, record scope, escalation vectors, gap inventory |
| C-06..C-08 (Recommended) | PASS all | Dataverse-native terminology throughout; CS-2 sharing rule conflict analysis; TABLE_5 three-field Remediation blocks |
| C-09..C-23 (Aspirational base) | PASS all | Defense-in-depth 4 layers, cross-role differential, pre-printed schemas, SHALL-A..G, three named expert personas, CA-first authorship, Schema Registry, closed authorship loop, phase execution attestation, double-anchor CA-1 rows |
| C-24..C-33 (R12 base) | PASS all | Distinct labeled Registry/Preamble anchor elements, CS-0 acknowledgment, TABLE_4 named rows, SE-updatable protocol co-located |

---

### Differential Scoring — C-34, C-35, C-36

#### C-34 — Preamble Orthogonal Dimensions Declaration

**Pass condition:** Step 0.2 contains a named table declaring D-1/D-2/D-3 as orthogonal axes with explicit non-interference statements and a binding "SHALL be simultaneously active" clause.

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| **V-01** | **PASS** | Step 0.2 has "R12 Orthogonal Dimensions Declaration (C-34):" with a 3-row table, D-1/D-2/D-3 IDs, mechanism descriptions, and per-row non-interference statements; binding clause: "All three dimensions SHALL be simultaneously active" |
| **V-02** | FAIL | Step 0.2 has SHALL-H but no axis declaration table; D-1/D-2/D-3 IDs not declared in preamble |
| **V-03** | FAIL | No axis declaration table; SHALL-A..G only in Step 0.2 |
| **V-04** | **PASS** | Identical axis declaration table as V-01, plus SHALL-H |
| **V-05** | **PASS** | Identical axis declaration table plus SHALL-H; D-2 mechanism in table explicitly cites SHALL-H and CA-1.9, closing chain forward |

---

#### C-35 — SE-4 STRUCTURED CLOSE TABLE_4 Row Cross-Reference + CA-1.9

**Pass condition:** SE-4 STRUCTURED CLOSE cites a named TABLE_4 SE-0 row (not generic prose); CA-1.9 verifies as distinct from CA-1.4 and CA-1.7.

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| **V-01** | FAIL | SE-4 STRUCTURED CLOSE: "citing SE-0 data" (generic prose, no named row); no CA-1.9 |
| **V-02** | **PASS** | SE-4: "TABLE_4 SE-0 row — Sharing rules — [cite by row name 'Sharing rules']"; CA-1.9 present with full double-anchor; SHALL-H declared as distinct from CA-1.4/CA-1.7 |
| **V-03** | FAIL | SE-4 STRUCTURED CLOSE: "TABLE_4 (filled at SE-0) evaluated all four escalation vectors with sharing rules explicitly cross-referenced" — shares rule mentioned but Sharing rules row not cited by row name; no CA-1.9 |
| **V-04** | **PASS** | SE-4: "TABLE_4 SE-0 — Sharing rules row [cite 'Sharing rules' by row name]" with cross-tier differential; CA-1.9 double-anchor row present; SHALL-H in preamble |
| **V-05** | **PASS** | SE-4: "TABLE_4 SE-0 — Sharing rules row [cite 'Sharing rules' by row name]"; CA-1.9 labels D-2 axis as distinct audit target; D-2's attestation entry in the verdict cites "per SHALL-H" and "CA-1.9 row present in Phase 3 with D-2 axis label" |

---

#### C-36 — CA Terminal Verdict Tri-Dimensional Self-Evidence Attestation

**Pass condition:** CA verdict contains a table naming each R12 dimension with its specific output-body evidence source; observable [ATTESTED / NOT ATTESTED] cells.

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| **V-01** | FAIL | Verdict: "[C-01 through C-05... CA-1.8. Overall: COMPLIANT / NON-COMPLIANT.]" — no attestation table |
| **V-02** | FAIL | Verdict cites CA-1.1..CA-1.9 results — no tri-dimensional attestation table |
| **V-03** | **PASS** | Verdict has "R12 Tri-Dimensional Self-Evidence Attestation (C-36):" table; D-1/D-2/D-3 each with Output-Body Evidence Source column and [ATTESTED / NOT ATTESTED] cells; D-2 entry honestly flags generic prose (NOT ATTESTED), making attestation observable not asserted |
| **V-04** | FAIL | Verdict ends at "C-35 SE-4 cross-reference: CA-1.9. Overall: COMPLIANT / NON-COMPLIANT." — no attestation table |
| **V-05** | **PASS** | Verdict has attestation table; D-2's evidence source correctly names "SE-4 STRUCTURED CLOSE body text above cites 'TABLE_4 SE-0 — Sharing rules row' by name (per SHALL-H); CA-1.9 row present in Phase 3 with D-2 axis label as distinct audit target" — all three ATTESTED from output body alone |

---

### Composite Scores

| Variation | C-34 | C-35 | C-36 | Passing | Score | Δ vs base |
|-----------|------|------|------|---------|-------|-----------|
| Base (R12 V-05) | — | — | — | 25/28 | **98.9** | — |
| **V-01** | PASS | FAIL | FAIL | 26/28 | **99.3** | +0.36 |
| **V-02** | FAIL | PASS | FAIL | 26/28 | **99.3** | +0.36 |
| **V-03** | FAIL | FAIL | PASS | 26/28 | **99.3** | +0.36 |
| **V-04** | PASS | PASS | FAIL | 27/28 | **99.6** | +0.72 |
| **V-05** | PASS | PASS | PASS | 28/28 | **100.0** | +1.08 |

---

### Rankings

1. **V-05 — 100.0** (28/28) — Full integration, all three axes closed
2. **V-04 — 99.6** (27/28) — Preamble + SE-4 cross-reference, missing verdict attestation
3. **V-01, V-02, V-03 — 99.3** (26/28 each) — Single-axis isolations, tied

---

### EXCELLENCE SIGNALS — V-05

**What makes V-05 better than V-04 (the one-step upgrade):**

1. **Tri-dimensional attestation table with observable cells** — [ATTESTED / NOT ATTESTED] forces the model to make an explicit, individually verifiable decision per dimension at terminal verdict time, rather than a single overall pass/fail assertion. Each dimension fails or passes independently at the most visible location in the output.

2. **D-2's attestation evidence source names SHALL-H and CA-1.9 explicitly** — The attestation entry for D-2 in V-05's verdict reads "per SHALL-H" and "CA-1.9 row present in Phase 3 with D-2 axis label as distinct audit target." This creates a four-anchor chain for a single dimension: preamble declaration (Step 0.2) → SE execution (SE-4 STRUCTURED CLOSE) → CA verification (CA-1.9) → terminal attestation (C-36 table) — making D-2 the most structurally redundant criterion in the output.

**What makes V-05 better than V-01 (axis declaration without execution + attestation):**

3. **Axis ID forward declaration in Step 0.2 creates a stable reference vocabulary** — V-01 declares D-1/D-2/D-3 but since the terminal verdict has no attestation table, the IDs are never used again. In V-05, the IDs flow: Step 0.2 declares them → SE-4 STRUCTURED CLOSE names D-2's mechanism text → CA-1.9 labels itself "(D-2 axis)" → verdict attestation table uses D-1/D-2/D-3 as keys. The ID naming in the preamble enables referencing without redefinition across phases.

**What makes V-05 better than V-03 (attestation without named row citation):**

4. **D-2's attestation is ATTESTED not PARTIAL** — In V-03, the attestation table honestly marks D-2 with a note that SE-4 "cites SE-0 data without naming the specific row." The table exists (C-36 passes) but D-2 self-attests as weak. In V-05, SE-4 STRUCTURED CLOSE cites the row by name, so D-2's attestation evidence source is verifiable and the [ATTESTED] cell is supportable from the output body alone.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["tri-dimensional attestation table with observable cells forces explicit per-dimension attestation decisions at terminal verdict rather than single asserted pass/fail", "dimension ID forward declaration in preamble creates stable reference vocabulary that flows through SE execution, CA verification, and terminal attestation without redefinition", "SHALL obligation as mechanism clause for a dimension converts an empirical structural observation into a four-anchor verifiable chain: preamble declaration, SE execution, CA-1.x verification, terminal attestation"]}
```
