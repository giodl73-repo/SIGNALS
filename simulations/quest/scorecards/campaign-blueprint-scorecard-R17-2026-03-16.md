## campaign-blueprint — Scorecard R17

### Rubric version: v17 | Ceiling: 263

---

## Criteria Reference (Key Chain)

| Criterion | Points | What it tests |
|-----------|--------|---------------|
| C-1 … C-33 | (base) | Structural scaffold through CONVICTION DELTA prose |
| C-34 | 5 | 4-col CONVICTION DELTA with in-cell Amplification chain template |
| C-35 | 5 | 6-col CONVICTION GAP DIAGNOSIS, pre-declared artifact rows, register-split columns |
| C-36 | 5 | 6-col TRACEABILITY AUDIT table form |
| C-38 | 5 | Named Req-ID rows in TRACEABILITY AUDIT, SETUP SCOUT TRACEABILITY TABLE match directive |
| C-40 | 5 | 4-col INERTIA MODEL MAP in SETUP, CONVICTION DELTA rows pre-named from MAP entries, explicit match directive |
| C-41 | 5 | Both SETUP-anchored tables carry pre-named rows (MAP→CONVICTION DELTA; SCOUT TABLE→TRACEABILITY AUDIT) |
| C-42 | 5 | In-table RULE sentinel inside INERTIA MODEL MAP (SETUP) |
| C-43 | 5 | Dual in-table sentinel chain — MAP sentinel + CONVICTION DELTA sentinel |
| **C-44** | **5** | **In-table RULE sentinel inside SCOUT TRACEABILITY TABLE (SETUP)** |
| **C-45** | **5** | **Complete four-sentinel chain — all four structural linkage tables carry in-table RULE sentinels** |

**Base score through C-43 (v16 ceiling, all variants):** 253

---

## Per-Variant Scoring

### V-01 — SCOUT TABLE Sentinel Only

**Axis:** Traceability lifecycle — SETUP sentinel in isolation, REFLECTION sentinel withheld

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-1 … C-33 | PASS | Base scaffold carried from v16 ceiling pattern |
| C-34 | PASS | 4-col CONVICTION DELTA with Amplification chain in-cell template present |
| C-35 | PASS | 6-col CONVICTION GAP DIAGNOSIS with pre-declared artifact rows and register-split columns |
| C-36 | PASS | TRACEABILITY AUDIT is a 6-col structural table |
| C-38 | PASS | Named Req-ID rows (R-01, R-02, R-03) linked to SCOUT TRACEABILITY TABLE entries; match directive present as prose |
| C-40 | PASS | 4-col INERTIA MODEL MAP in SETUP; CONVICTION DELTA rows pre-named CT-Spec, CT-Prop, CT-Pitch; explicit match directive |
| C-41 | PASS | Both SETUP-anchored tables supply named rows to their REFLECTION counterparts |
| C-42 | PASS | MAP carries in-table RULE sentinel row preceding CT data rows (inherited from V-04 R15 pattern) |
| C-43 | PASS | CONVICTION DELTA also carries in-table RULE sentinel; dual-sentinel chain for conviction-type axis complete |
| **C-44** | **PASS** | SCOUT TRACEABILITY TABLE (SETUP) carries non-data RULE sentinel row before Req-ID data rows; text declares TRACEABILITY AUDIT must contain exactly one row per SETUP entry and that a missing row is `R-[NN] absent`, not a count discrepancy |
| **C-45** | **FAIL** | TRACEABILITY AUDIT (REFLECTION) retains only the N+blank=FAIL cell-level RULE row from V-04 R15 — no Req-ID-to-SETUP-entry binding sentinel present. Four-sentinel chain incomplete; C-45 requires all four sentinels; only three are present |

**Subtotal:** 253 (base) + 5 (C-44) + 0 (C-45) = **258**

---

### V-02 — Minimum-Form Four-Sentinel

**Axis:** Sentinel text density — both new sentinels at minimum structurally valid text

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-1 … C-43 | PASS | Full v16 ceiling pattern intact; MAP sentinel, CONVICTION DELTA sentinel, C-38 named-row TRACEABILITY AUDIT all present |
| **C-44** | **PASS** | SCOUT TRACEABILITY TABLE (SETUP) carries terse but structurally valid RULE sentinel row: text declares one-row-per-SETUP-entry requirement and names `R-[NN] absent` as the failure mode; positioned before data rows; inside table boundary |
| **C-45** | **PASS** | TRACEABILITY AUDIT (REFLECTION) independently carries in-table RULE sentinel binding each Req-ID to a named SCOUT TRACEABILITY TABLE entry and declaring named-identifier absence as failure mode. All four sentinels present: MAP (SETUP, conviction axis), CONVICTION DELTA (REFLECTION, conviction axis), SCOUT TRACEABILITY TABLE (SETUP, traceability axis), TRACEABILITY AUDIT (REFLECTION, traceability axis). No linkage phase relies on external prose as sole enforcement mechanism |

**Subtotal:** 253 + 5 + 5 = **263**

---

### V-03 — Conversational Register

**Axis:** Register invariance — both new sentinels phrased in conversational register

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-1 … C-43 | PASS | v16 ceiling pattern carried; register invariance confirmed by D16/D17 — conversational register does not affect structural verdict for MAP sentinel and CONVICTION DELTA sentinel |
| **C-44** | **PASS** | SCOUT TRACEABILITY TABLE (SETUP) carries a conversational in-table RULE sentinel row (e.g., "One thing to track here — the TRACEABILITY AUDIT below needs exactly one row for each entry in this table; a missing row means R-[NN] is absent, not just undercounted"). Positioned inside table boundary before data rows. Per D17: "a conversational-register in-table RULE sentinel earns C-44 FULL." Structural placement is the evaluated property; register is non-load-bearing |
| **C-45** | **PASS** | TRACEABILITY AUDIT (REFLECTION) carries its own conversational in-table RULE sentinel binding Req-IDs to named SCOUT TRACEABILITY TABLE entries. All four sentinels present in conversational register. D17 register invariance applies symmetrically across both new sentinel positions. Four-sentinel chain complete |

**Subtotal:** 253 + 5 + 5 = **263**

---

### V-04 — Maximum-Density Four-Sentinel

**Axis:** Sentinel text density ceiling — exhaustive enforcement text in all four sentinels

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-1 … C-43 | PASS | v16 ceiling pattern intact; MAP sentinel and CONVICTION DELTA sentinel at maximum density (inherited from or extended from V-04 R15 base) |
| **C-44** | **PASS** | SCOUT TRACEABILITY TABLE (SETUP) carries an exhaustive RULE sentinel row enumerating: (a) one-to-one correspondence requirement, (b) named-identifier absence (R-[NN] absent) as failure mode, (c) explicit note that count-equality is insufficient — row identity must match. All requirements exceed C-44 minimum; sentinel is in-table, positioned before data rows |
| **C-45** | **PASS** | TRACEABILITY AUDIT (REFLECTION) carries maximum-density RULE sentinel: text explicitly names each Req-ID must match a SCOUT TRACEABILITY TABLE entry, declares named-identifier absence as failure mode, and notes that row omission is not a count error. Combined with C-44 FULL, all four structural sentinel positions occupied at maximum density. Per D17 density invariance: no scoring advantage over V-02 — structural placement is the sole evaluated property. C-45 FULL regardless of text length |

**Subtotal:** 253 + 5 + 5 = **263**

---

### V-05 — Minimum-Density Compression

**Axis:** Surrounding prose compression — minimum prose envelope with all four sentinels intact

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-1 … C-43 | PASS | v16 ceiling pattern retained; D16 density invariance confirms MAP sentinel and CONVICTION DELTA sentinel do not require dense surrounding prose to earn C-42/C-43 FULL |
| **C-44** | **PASS** | SCOUT TRACEABILITY TABLE (SETUP) carries minimum-form in-table RULE sentinel (structurally parallel to V-02 but with compressed surrounding prose sections). Sentinel itself is complete and in-table; only the prose sections wrapping the tables are compressed. C-44 evaluates table structure, not surrounding prose volume — FULL |
| **C-45** | **PASS** | TRACEABILITY AUDIT (REFLECTION) carries minimum-form in-table RULE sentinel. Surrounding prose stripped to essential headings only. Per D16 density invariance (extended to traceability axis by D17): prose volume surrounding the table is non-load-bearing. All four sentinels structurally present; chain complete. C-45 FULL |

**Subtotal:** 253 + 5 + 5 = **263**

---

## Summary Scorecard

| Variant | Base (C-1…C-43) | C-44 | C-45 | Total | Rank |
|---------|-----------------|------|------|-------|------|
| V-02 — Minimum-Form Four-Sentinel | 253 | +5 | +5 | **263** | 1 (tie) |
| V-03 — Conversational Register | 253 | +5 | +5 | **263** | 1 (tie) |
| V-04 — Maximum-Density Four-Sentinel | 253 | +5 | +5 | **263** | 1 (tie) |
| V-05 — Minimum-Density Compression | 253 | +5 | +5 | **263** | 1 (tie) |
| V-01 — SCOUT TABLE Sentinel Only | 253 | +5 | 0 | **258** | 5 |

---

## Diagnostic Yield

**D17 extended — four invariance properties now confirmed:**

| Property | Confirmed by | Axis |
|----------|-------------|------|
| Register invariance | V-03 (R17) — conversational sentinels earn C-44/C-45 FULL | Traceability |
| Density invariance | V-02 vs V-04 (R17) — min and max density both score 263 | Traceability |
| Prose-compression invariance | V-05 (R17) — surrounding prose stripped; sentinel chain survives | Traceability |
| Sentinel-independence | V-01 (R17) — C-44 without C-45 scores 258; confirms independent testability | Split-axis |

**Key finding — V-01 as diagnostic control:** The N+blank=FAIL RULE row carried in the TRACEABILITY AUDIT by V-04 R15 does **not** satisfy C-45. That row is a cell-level completeness rule (blank = fail), not an entry-level Req-ID-to-SETUP binding rule. C-45 requires the TRACEABILITY AUDIT sentinel to explicitly declare that each row's Req-ID must match a named SCOUT TRACEABILITY TABLE entry. V-01 isolates this distinction cleanly, confirming the two criteria test separable structural properties.

---

## Excellence Signals (Top-Scoring Variants)

The four 263-scoring variants (V-02 through V-05) share two structural patterns not present in V-01:

1. **Traceability-axis REFLECTION sentinel — Req-ID binding, not just completeness:** The TRACEABILITY AUDIT carries an in-table RULE sentinel that goes beyond N+blank=FAIL. It declares that each row's Req-ID must match a *named* SCOUT TRACEABILITY TABLE entry and that a missing row is a named-identifier absence (`R-[NN] absent`). This is the traceability-axis parallel of the CONVICTION DELTA sentinel (C-43): the REFLECTION table becomes self-enforcing, not just complete.

2. **Symmetric four-sentinel architecture:** All four structural linkage tables — INERTIA MODEL MAP (SETUP, conviction axis), CONVICTION DELTA (REFLECTION, conviction axis), SCOUT TRACEABILITY TABLE (SETUP, traceability axis), TRACEABILITY AUDIT (REFLECTION, traceability axis) — carry in-table RULE sentinel rows simultaneously. No structural linkage phase relies on external prose as its sole enforcement mechanism. The architecture is axis-symmetric and phase-symmetric.

---

```json
{"top_score": 263, "all_essential_pass": true, "new_patterns": ["Traceability-axis REFLECTION sentinel: TRACEABILITY AUDIT carries in-table RULE row binding each Req-ID to a named SCOUT TRACEABILITY TABLE entry and declaring R-[NN] absent as the failure mode — entry-level binding, not cell-level completeness", "Symmetric four-sentinel architecture: all four structural linkage tables (MAP, CONVICTION DELTA, SCOUT TRACEABILITY TABLE, TRACEABILITY AUDIT) carry in-table RULE sentinel rows simultaneously, achieving axis-symmetric and phase-symmetric in-table enforcement with no linkage phase relying on external prose"]}
```
